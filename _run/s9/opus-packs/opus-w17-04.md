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

## GROUP: _overhaul2/lake/cases/United States v. Lundin.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Lundin"
type: case
citation: "817 F.3d 1151 (2016)"
parallel_cite: ""
neutral_cite: "2016 WL 1104851; 2016 U.S. App. LEXIS 5236"
court: "U.S. Court of Appeals, 9th Circuit"
court_level: coa
circuit: 9th
year: 2016
date_decided: 2016-03-22
docket: ""
authority_weight: "Binding in-circuit — 9th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2016-03-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Lundin
  varies_by_point: false
  scope_note: "Good law. Holds the knock-and-talk implied license is bounded by time and purpose, and that an officer's intent to arrest defeats the exception."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/3187682/united-states-v-eric-lundin/"
  cluster_id: 3187682
  opinion_id: 3187625
  identity_checked: true
homes:
  - page: "[[Knock and Talk]]"
    role: "Illustrates a circuit split"
  - page: "[[Curtilage]]"
    role: "Related (cross-doctrine)"
related: ["[[Florida v. Jardines]]", "[[Kentucky v. King]]", "[[Oliver v. United States]]", "[[United States v. Carloss]]", "[[United States v. Walker]]"]
aliases: ["United States v. Eric Lundin", "United States v. Lundin (9th Cir. 2016)"]
tags: ["case", "fourth-amendment", "knock-and-talk", "implied-license", "curtilage", "arrest", "ninth-circuit"]
holding: "The knock-and-talk implied license is bounded by both time and purpose: a pre-dawn (around 4:00 a.m.) knock, undertaken with the intent to arrest the occupant rather than to ask questions, exceeds the customary license — so the exception does not apply and the porch knock (and the search it precipitated) violated the Fourth Amendment."
lake:
  record_id: United States v. Lundin
  status: verified
  projected_at: 2026-07-09
---

# United States v. Lundin

*817 F.3d 1151 (9th Cir. 2016)* · U.S. Court of Appeals, 9th Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After Susan Hinds reported that Eric Lundin had assaulted and briefly kidnapped her, deputies issued a be-on-the-lookout and a request for Lundin's warrantless arrest. Around 4:00 a.m. on April 23, 2013, three officers approached Lundin's home — without an arrest warrant or a search warrant — came onto his front porch, and knocked with the intent of arresting him. From the porch they heard crashing noises from the backyard, ran to the back, ordered Lundin out of the fenced-in yard, and arrested him. Officers then searched the home and patio and found two handguns in open view. The district court suppressed the handguns as the fruit of an illegal search, and the United States appealed.

## Issue
Whether the "knock and talk" exception authorized officers to enter the [[Curtilage|curtilage]] and knock on the front door at 4:00 a.m. with the intent to arrest the occupant, where the knock precipitated the noises the officers then used to justify a warrantless search.

## Rule
The [[Knock and Talk|knock-and-talk]] exception is "coterminous with th[e] implicit license" to approach and knock, and the court held the officers exceeded that license "[f]or two reasons." First, time: "unexpected visitors are customarily expected to knock on the front door of a home only during normal waking hours," and here the officers "knocked on Lundin's door around 4:00 a.m. without evidence that Lundin generally accepted visitors at that hour, and without a reason for knocking that a resident would ordinarily accept as sufficiently weighty to justify the disturbance." — 817 F.3d at 1159. ^pin-1159

Second, purpose: "the scope of a license is often limited to a specific purpose," the customary license "is generally limited to the 'purpose of asking questions of the occupants,'" and "[o]fficers who knock on the door of a home for other purposes generally exceed the scope of the customary license and therefore do not qualify for the 'knock and talk' exception." — [*Id.*](https://www.courtlistener.com/opinion/3187682/united-states-v-eric-lundin/#:~:text=the%20scope%20of%20a%20license) ^pin-1159a

After *[[Florida v. Jardines|Jardines]]*, "the 'knock and talk' exception depends at least in part on an officer's subjective intent," and the court held: "The 'knock and talk' exception to the warrant requirement does not apply when officers encroach upon the curtilage of a home with the intent to arrest the occupant." — 817 F.3d at 1160. ^pin-1160

## Application
The front porch is the "classic exemplar" of [[Curtilage|curtilage]], so the officers' presence there and their knock were a presumptively unreasonable search unless licensed. They were not: the approach occurred around 4:00 a.m., outside normal waking hours and without any reason a resident would accept as justifying so early a disturbance, and the district court found the officers' clear purpose was to arrest Lundin, not to ask questions. Because the knock exceeded the customary license on both the time and purpose dimensions, the [[Knock and Talk|knock-and-talk]] exception did not apply; and since the officers' own unlawful knock caused the crashing noises, they could not rely on those noises as [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] to justify the ensuing warrantless search.

## Conclusion
The officers exceeded the implied license, so the porch knock was an unlawful search and the search it precipitated was illegal; the Ninth Circuit affirmed suppression of the handguns.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 9th Cir.**
- *Lundin* applies [[Florida v. Jardines]] to hold the implied license is limited by **time** and **purpose**, and that an officer's intent to arrest takes the approach outside the [[Knock and Talk|knock-and-talk]] exception — making the officer's subjective purpose relevant, an approach that divides the circuits. It also invokes [[Kentucky v. King]]'s rule that police may not rely on [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] they create through their own Fourth Amendment violation. Contrast [[United States v. Walker]] (11th Cir.), upholding a pre-dawn knock and talk on its facts, and [[United States v. Carloss]] (10th Cir.) on what conduct withdraws the license.

## Appears on
- [[Knock and Talk]] — *Illustrates a circuit split*
- [[Curtilage]] — *Related (cross-doctrine)*

## Sources
- *United States v. Lundin*, 817 F.3d 1151 (9th Cir. 2016) — https://www.courtlistener.com/opinion/3187682/united-states-v-eric-lundin/ — pinpoints: 1159, 1160.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "cdb7ba03edf59951", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Lundin"}, "payload": {"all": [{"cite": "817 F.3d 1151", "page": "1151", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "817"}, {"cite": "2016 WL 1104851", "page": "1104851", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2016"}, {"cite": "2016 U.S. App. LEXIS 5236", "page": "5236", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2016"}], "display": "817 F.3d 1151", "official": {"cite": "817 F.3d 1151", "page": "1151", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "817"}, "official_selection_present": true, "record_id": "United States v. Lundin"}}
{"assertion_id": "071b3e0efc40cd75", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1159", "record_id": "United States v. Lundin"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1159", "pinpoint_status": "slip-only", "quote": "exception authorized officers to enter the curtilage and knock on the front door at 4:00 a.m. with the intent to arrest the occupant, where the knock precipitated the noises the officers then used to justify a warrantless search. ## Rule The knock-and-talk exception is", "quote_fidelity": "mismatch", "record_id": "United States v. Lundin", "star_marker": null}}
{"assertion_id": "077f643d38e8774d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1160", "record_id": "United States v. Lundin"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1160", "pinpoint_status": "slip-only", "quote": "the 'knock and talk' exception depends at least in part on an officer's subjective intent,", "quote_fidelity": "mismatch", "record_id": "United States v. Lundin", "star_marker": null}}
{"assertion_id": "6f5583953939cf92", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1159a", "record_id": "United States v. Lundin"}, "payload": {"fragment": "#:~:text=the%20scope%20of%20a%20license", "page": null, "pin_id": "pin-1159a", "pinpoint_status": "slip-only", "quote": "the scope of a license is often limited to a specific purpose,", "quote_fidelity": "matched", "record_id": "United States v. Lundin", "star_marker": null}}
{"assertion_id": "61547c0e62963171", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Lundin"}, "payload": {"as_of_content": "2016-03-22", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Lundin", "scope_note": "Good law. Holds the knock-and-talk implied license is bounded by time and purpose, and that an officer's intent to arrest defeats the exception.", "varies_by_point": false}}
```

### lake record — United States v. Lundin

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Lundin",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Eric Lundin",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellant, v. Eric Eugene LUNDIN, AKA Whitey, Defendant-Appellee",
    "input_case_name": "United States v. Lundin",
    "court": "U.S. Court of Appeals, 9th Circuit",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "9th",
    "state": null,
    "date_decided": "2016-03-22",
    "year": 2016,
    "docket": null,
    "cluster_id": 3187682,
    "lead_opinion_id": 3187625,
    "sibling_ids": [
      3187625
    ],
    "absolute_url": "/opinion/3187682/united-states-v-eric-lundin/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "817 F.3d 1151",
      "volume": "817",
      "reporter": "F.3d",
      "page": "1151",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2016 WL 1104851",
        "volume": "2016",
        "reporter": "WL",
        "page": "1104851",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 U.S. App. LEXIS 5236",
        "volume": "2016",
        "reporter": "U.S. App. LEXIS",
        "page": "5236",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "817 F.3d 1151",
        "volume": "817",
        "reporter": "F.3d",
        "page": "1151",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 WL 1104851",
        "volume": "2016",
        "reporter": "WL",
        "page": "1104851",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 U.S. App. LEXIS 5236",
        "volume": "2016",
        "reporter": "U.S. App. LEXIS",
        "page": "5236",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "817 F.3d 1151",
    "official_selection": {
      "court_class": "coa",
      "selected": "817 F.3d 1151",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1159",
      "page": null,
      "quote": "exception authorized officers to enter the curtilage and knock on the front door at 4:00 a.m. with the intent to arrest the occupant, where the knock precipitated the noises the officers then used to justify a warrantless search. ## Rule The knock-and-talk exception is",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1159a",
      "page": null,
      "quote": "the scope of a license is often limited to a specific purpose,",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 19208,
      "fragment": "#:~:text=the%20scope%20of%20a%20license",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-1160",
      "page": null,
      "quote": "the 'knock and talk' exception depends at least in part on an officer's subjective intent,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2016-03-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Lundin",
    "varies_by_point": false,
    "scope_note": "Good law. Holds the knock-and-talk implied license is bounded by time and purpose, and that an officer's intent to arrest defeats the exception.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "French v. Merrill",
          "cluster_id": 5273192,
          "cite": [
            "15 F.4th 116"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Andre Staggers",
          "cluster_id": 4759755,
          "cite": [
            "961 F.3d 745"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Aaron Holmes, Jr.",
          "cluster_id": 10273168,
          "cite": [
            "121 F.4th 727"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Christopher Esqueda",
          "cluster_id": 9451359,
          "cite": [
            "88 F.4th 818"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Escobar",
          "cluster_id": 7330094,
          "cite": [
            "309 F. Supp. 3d 778"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brett Parkins",
          "cluster_id": 9475415,
          "cite": [
            "92 F.4th 882"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brett Parkins",
          "cluster_id": 9475001,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Hylton, Jr.",
          "cluster_id": 6458860,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murchison v. County of Tehama",
          "cluster_id": 5178968,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(3187625) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca9)",
        "reviewed": 5,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 5,
        "triage_read": 0,
        "triage_snippet_classified": 5
      },
      "lane2_top_cited": {
        "query": "cites:(3187625)",
        "reviewed": 9,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 9,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(3187625)",
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
    "complete_query": "cites:(3187625)",
    "indexed_citing_opinions": 9,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 3187625,
        "count": 9,
        "count_source": "search"
      }
    ],
    "citation_count": 68,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-lundin.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 9,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 3187625,
        "cited_id": 100047,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 112136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 112384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 216733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 217703,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 380517,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 461076,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 475484,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 622304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 691388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 706974,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 755893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 770197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 771671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 782687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 801335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 856347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 1348637,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 1382743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 1447779,
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
    "date_created": "2026-07-06T01:24:15Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:24:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:24:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:26:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:24:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Lundin

```
                FOR PUBLICATION

  UNITED STATES COURT OF APPEALS
       FOR THE NINTH CIRCUIT


UNITED STATES OF AMERICA,                No. 14-10365
               Plaintiff-Appellant,
                                           D.C. No.
                 v.                     4:13-cr-00402-
                                            JST-1
ERIC EUGENE LUNDIN, AKA
Whitey,
              Defendant-Appellee.           OPINION


      Appeal from the United States District Court
        for the Northern District of California
        Jon S. Tigar, District Judge, Presiding

               Argued and Submitted
    September 18, 2015—San Francisco, California

                 Filed March 22, 2016

    Before: William A. Fletcher, Marsha S. Berzon,
          and Carlos T. Bea, Circuit Judges.

             Opinion by Judge W. Fletcher
2                  UNITED STATES V. LUNDIN

                           SUMMARY*


                          Criminal Law

    In an interlocutory appeal by the government, the panel
affirmed the district court’s order suppressing handguns
seized from the defendant’s home, and remanded for further
proceedings.

    The panel held that the warrantless search of the
defendant’s home was not justified by exigent circumstances.
The panel explained that the “knock and talk” exception to
the warrant requirement does not apply when officers
encroach upon the curtilage of a home with the intent to arrest
the occupant. The panel saw no reason to disturb the district
court’s finding that the officers’ purpose in knocking on the
defendant’s door at 4:00 a.m., in response to a deputy’s
request that the defendant be arrested, was to find and arrest
him. The panel held that the officers therefore violated the
defendant’s Fourth Amendment right to be free from
unlawful searches when they stood on his porch and knocked
on his front door. Since this unconstitutional conduct caused
the allegedly exigent circumstance— crashing noises in the
backyard—the panel concluded that that circumstance cannot
justify the search resulting in the seizure of the handguns.

    The panel held that the warrantless search was not
justified as a protective sweep, because the officers lacked a
reasonable ground for believing that there was a danger that
would have justified the sweep of the defendant’s home.

  *
    This summary constitutes no part of the opinion of the court. It has
been prepared by court staff for the convenience of the reader.
                 UNITED STATES V. LUNDIN                     3

    The panel held that the inevitable discovery exception to
the exclusionary rule does not apply, because the officers
knew they had probable cause to arrest the defendant but
failed to obtain any warrant before coming onto his porch and
knocking on his door with the intention of arresting him.


                         COUNSEL

Barbara J. Valliere (argued), Chief, Appellate Division, and
Melinda Haag, United States Attorney, San Francisco,
California, for Plaintiff-Appellant.

Geoffrey A. Hansen (argued), Chief Assistant Federal Public
Defender, Steven G. Kalar, Federal Public Defender, and
Steven J. Koeninger, Research and Writing Attorney, San
Francisco, California, for Defendant-Appellee.


                         OPINION

W. FLETCHER, Circuit Judge:

    Around 4:00 a.m. on April 23, 2013, three northern
California law enforcement officers approached Defendant
Eric Lundin’s home without either an arrest warrant or a
search warrant. They came onto his front porch and knocked
on his door with the intent of arresting him. From the front
porch where they were standing, the officers heard crashing
noises coming from the back of the house. They ran to the
back, ordered Lundin to come out of the fenced-in backyard,
and arrested him. After putting Lundin in a patrol car, several
officers briefly searched Lundin’s home, including the back
patio where they found two handguns in open view. The
4                UNITED STATES V. LUNDIN

district court suppressed the handguns as the result of an
illegal search. The United States appeals. We hold that the
officers violated the Fourth Amendment when they knocked
on the door at 4:00 a.m. without a warrant with the intent of
arresting Lundin, and that the immediately ensuing search
was illegal. We therefore affirm.

                        I. Background

    At 12:24 a.m. on April 23, 2013, Deputy Sheriff Scott
Aponte of the Humboldt County Sheriff’s Office (“HCSO”)
was dispatched to the Mad River Community Hospital to
interview Susan Hinds, a 63-year-old patient who claimed she
had been kidnapped several hours earlier. In a tape-recorded
statement, Hinds told Deputy Aponte that sometime after
8:00 p.m. on April 22, shortly after her son, Joseph Miller,
had left to go to the store, Eric “Whitey” Lundin knocked on
the door of her mobile home. When Hinds opened the door,
Lundin grabbed her by the neck, forced his way inside, and
accused Miller of stealing marijuana from him.

    Hinds told Deputy Aponte that, once inside the mobile
home, Lundin took two firearms from his pockets — a
compact silver handgun and a large black handgun. He then
took out a bottle of pills and forced Hinds to ingest one of the
pills. He described the pills to Hinds as “methadone” and
told her that they were the easiest way to overdose. After
forcing Hinds to ingest the pill, Lundin broke her television
by striking it with one of the handguns. Lundin then pressed
the black handgun against Hinds’s temple and forced her to
call Miller to tell him to come home. When the call ended,
Lundin snatched Hinds’s cell phone and threw it across the
room.
                 UNITED STATES V. LUNDIN                    5

    Hinds told Deputy Aponte that Lundin repeatedly said
that she was going to die and that, as a member of the
Mongols motorcycle gang, he does not “leave witnesses.”
Lundin received two calls on his cell phone while still at the
mobile home. Hinds heard him say during one of the calls,
“I’m taking care of it. I’ve got her right here on the couch.”

     Hinds said that Lundin then forced her into his Dodge
truck. They passed Miller as they drove out of the mobile
home park. Lundin told Hinds, “Wave good-bye to your son.
You’ll never see him again.” During the drive, Lundin forced
Hinds to ingest two more pills and pointed out locations
where he could safely dispose of her body. Lundin then
spoke with Miller on his cell phone and accused Miller of
stealing his marijuana. After ending the call with Miller,
Lundin told Hinds that he no longer believed Miller had
stolen his marijuana. Lundin drove Hinds back to her mobile
home, told her that he only meant to scare her, and warned
her not to call the police. He told her that he would buy her
a new television. Hinds had been in the truck a total of about
fifteen minutes.

    After concluding the interview with Hinds at the hospital,
Deputy Aponte interviewed Miller, who had come to the
hospital to see his mother. Miller told Aponte that Hinds had
called him while he was at the grocery store and had told him
to come home immediately. When he returned, the mobile
home was in disarray, and the television was broken. Miller
then called Lundin on his cell phone. Miller recounted to
Aponte that Lundin had accused him of stealing marijuana
and had told him that Lundin was going to send his “Mongol
brothers” to get Miller. After concluding the interview with
Miller, Aponte visited Hinds’s mobile home to photograph
the damage.
6                UNITED STATES V. LUNDIN

    Deputy Aponte asked dispatch to issue a “Be On the Look
Out” (“BOLO”) for Lundin and a request for Lundin’s arrest
under California Penal Code § 836. Section 836 authorizes
a warrantless arrest when there is probable cause to believe a
suspect has committed a felony. However, § 836 does not —
because it may not — authorize a warrantless arrest of a
suspect in his own home. Payton v. New York, 445 U.S. 573,
589–90 (1980). Aponte believed there was probable cause to
arrest Lundin for burglary, false imprisonment, kidnapping,
vandalism, brandishing a firearm, administering a drug to
commit a felony, administering a controlled substance, and
battery. HCSO dispatch issued the BOLO and arrest request
just before 2:00 a.m.

    Upon receiving the BOLO and arrest request, Arcata
Police Department (“APD”) Officer Matthew O’Donovan
used vehicle registration files to determine Lundin’s address.
O’Donovan then drove to Lundin’s home. When he arrived,
he saw a vehicle matching the description of Lundin’s Dodge
truck parked in the driveway and saw that lights were on
inside the house. O’Donovan called for backup. APD
Officer Jeremiah Kasinger, APD Sergeant Keith Altizer, and
HCSO Deputy Matthew Tomlin responded to the call,
arriving just before 4:00 a.m.

    Officer O’Donovan wrote in a declaration that he, Officer
Kasinger, and Deputy Tomlin approached Lundin’s front
door. O’Donovan wrote that without identifying themselves
they stood on the porch, knocked loudly, waited thirty
seconds for an answer, and then knocked more loudly. After
the second knock, the officers heard several loud crashing
noises coming from the back of the house. The officers ran
to the back of the house and heard someone moving around
in the backyard. The officers identified themselves and
                 UNITED STATES V. LUNDIN                     7

ordered Lundin “to put his hands in the air and come out
slowly.” When Lundin did so, Tomlin handcuffed him and
placed him in a patrol car.

    Officers O’Donovan and Kasinger then searched Lundin’s
backyard and patio, which were enclosed by a high fence.
They also searched inside the house. At the end of the search,
O’Donovan saw on the patio, in open view and within arm’s
reach of a common walkway, a clear plastic freezer bag
containing a silver revolver and a black semiautomatic
handgun. The bag was lying admidst a number of five-gallon
buckets that had been knocked over. The crashing noises
heard by the officers had likely been the buckets falling over.
O’Donovan notified Deputy Tomlin that he had found a bag
containing handguns, which Tomlin then photographed and
seized. When Deputy Aponte arrived, he confirmed that the
handguns matched Hinds’s description of the guns used
during the earlier incident. Aponte then advised Lundin of
his Miranda rights.

    On the morning of April 24, HCSO Deputy Todd Fulton
prepared an affidavit, statement of probable cause, and an
application for a warrant to search Lundin’s home. The
statement of probable case described Hinds’s report to
Deputy Aponte and stated, inter alia, that two firearms had
been located during the arrest at Lundin’s residence. A
California magistrate judge approved the warrant. At about
10:30 a.m. that morning, state and federal law enforcement
officers executed the warrant and seized numerous items from
inside the house, including guns, cell phones, a prescription
pill bottle for methadone, computers and hard drives, and
various Mongols paraphernalia.
8                UNITED STATES V. LUNDIN

    On June 20, Lundin was charged with being a felon in
possession of a firearm and ammunition in violation of
18 U.S.C. § 922(g)(1). Lundin moved to suppress the
evidence obtained from the patio and inside the house, as well
as statements he had made before he was read his Miranda
rights. Lundin contended that the two handguns seized from
the patio on April 23 should be suppressed as the fruits of an
unreasonable warrantless search, that the evidence seized
from his house on April 24 should be suppressed as the fruits
of an invalid search warrant, and that the pre-warning
information elicited by officers should be suppressed under
Miranda. On June 26, the district court suppressed the two
handguns seized on the patio. It otherwise denied Lundin’s
motion.

    On July 24, a grand jury returned a superseding
indictment charging Lundin with kidnapping in aid of
racketeering (18 U.S.C. § 1959(a)(1)), assault in aid of
racketeering (18 U.S.C. § 1959(a)(3)), kidnapping (18 U.S.C.
§ 1201(a)(1)), possession with intent to distribute and
manufacture marijuana (21 U.S.C. §§ 841(a)(1), (b)(1)(C)),
use or possession of a firearm in furtherance of a crime of
violence or a drug trafficking crime (18 U.S.C. § 924(c)(1)),
and being a felon in possession of a firearm (18 U.S.C.
§ 922(g)(1)). On July 25, after Lundin was arraigned on new
charges, the government timely took an interlocutory appeal
under 18 U.S.C. § 3731.

                  II. Standard of Review

    “Whether the exclusionary rule applies to a given case is
reviewed de novo, while the underlying factual findings are
reviewed for clear error.” United States v. Perea-Rey,
680 F.3d 1179, 1183 (9th Cir. 2012) (citation omitted). “We
                 UNITED STATES V. LUNDIN                     9

review the district court’s application of the inevitable
discovery doctrine for clear error because, although it is a
mixed question of law and fact, it is essentially a factual
inquiry.” United States v. Reilly, 224 F.3d 986, 994 (9th Cir.
2000); see United States v. Ruckes, 586 F.3d 713, 716 (9th
Cir. 2009); United States v. Lang, 149 F.3d 1044, 1048 (9th
Cir. 1998).

                       III. Discussion

    The Fourth Amendment protects “[t]he right of the people
to be secure in their persons, houses, papers, and effects,
against unreasonable searches and seizures . . . .” U.S. Const.
amend. IV. “At [its] very core stands the right of a [person]
to retreat into his own home and there be free from
unreasonable governmental intrusion.” Silverman v. United
States, 365 U.S. 505, 511 (1961). “[S]earches and seizures
inside a home without a warrant are,” therefore,
“presumptively unreasonable.” Payton, 445 U.S. at 586.
Evidence derived from an illegal search cannot “constitute
proof against the victim of the search.” Wong Sun v. United
States, 371 U.S. 471, 484 (1963).

    It is undisputed that the officers seized the two handguns
during a warrantless search of Lundin’s home. The handguns
are therefore the product of a presumptively unreasonable
search. To avoid suppression of the handguns, the
government must demonstrate that either an exception to the
warrant requirement or an exception to the exclusionary rule
applies. The government argues that the warrantless search
of Lundin’s home was justified either due to exigent
circumstances or as a protective sweep. In the alternative, the
government contends the handguns are admissible under the
10               UNITED STATES V. LUNDIN

inevitable discovery exception to the exclusionary rule. We
agree with the district court that these arguments fail.

                 A. Exigent Circumstances

    Law enforcement officers may conduct a warrantless
search of a home when “the exigencies of the situation make
the needs of law enforcement so compelling that [a]
warrantless search is objectively reasonable under the Fourth
Amendment.” Kentucky v. King, 563 U.S. 452, 460 (2011)
(alteration in original) (citation omitted). However, exigent
circumstances cannot justify a warrantless search when the
police “create the exigency by engaging . . . in conduct that
violates the Fourth Amendment.” Id. at 462.

    The officers in this case had no reason other than the
crashing noises coming from the backyard to believe that
there were exigent circumstances justifying a warrantless
search of Lundin’s home. However, the evidence shows that
the officers’ knock at Lundin’s front door caused him to make
the crashing noises. Thus, to show that exigent circumstances
justified the warrantless search, the government must show
that the officers lawfully stood on Lundin’s front porch and
knocked on his door.

    The area “immediately surrounding and associated with
the home” — the “curtilage” — is treated as “part of [the]
home itself for Fourth Amendment purposes.” Oliver v.
United States, 466 U.S. 170, 180 (1984). Like searches and
seizures inside the home itself, “searches and seizures in the
curtilage without a warrant are also presumptively
unreasonable.” Perea-Rey, 680 F.3d at 1184. The
presumption against warrantless searches and seizures “would
be of little practical value if the State’s agents could stand in
                 UNITED STATES V. LUNDIN                    11

a home’s porch or side garden and trawl for evidence with
impunity.” Florida v. Jardines, 569 U.S. —, —, 133 S. Ct.
1409, 1414 (2013).

    A government agent conducts a “search” within the
meaning of the Fourth Amendment when the agent infringes
“an expectation of privacy that society is prepared to consider
reasonable,” United States v. Jacobsen, 466 U.S. 109, 113
(1984), or “physically occupie[s] private property for the
purpose of obtaining information.” United States v. Jones,
565 U.S. —, —, 132 S. Ct. 945, 949 (2012). It is undisputed
that the officers physically occupied the curtilage of Lundin’s
home when they stood on the front porch and knocked on his
door. Indeed, the front porch of a home is the “classic
exemplar” of curtilage. Jardines, 133 S. Ct. at 1415. The
district court concluded that the officers’ clear purpose was
to determine whether Lundin was home and, if so, to arrest
him. Thus, the officers’ presence on Lundin’s front porch
and their knock at his door constituted a presumptively
unreasonable search.

    The government contends that the officers were permitted
to knock on Lundin’s door under the so-called “knock and
talk” exception to the warrant requirement, which permits law
enforcement officers to “‘encroach upon the curtilage of a
home for the purpose of asking questions of the occupants.’”
Perea-Rey, 680 F.3d at 1187 (quoting United States v.
Hammett, 236 F.3d 1054, 1059 (9th Cir. 2001)). The “knock
and talk” exception resembles to some degree the exception
for consensual searches. The relevant “consent” in a “knock
and talk” case is implied from the custom of treating the
“knocker on the front door” as an invitation (i.e., license) to
approach the home and knock. Jardines, 133 S. Ct. at 1415
(citation omitted). The scope of the exception is coterminous
12               UNITED STATES V. LUNDIN

with this implicit license. Stated otherwise, to qualify for the
exception, the government must demonstrate that the officers
conformed to “‘the habits of the country,’” id. (quoting
McKee v. Gratz, 260 U.S. 127, 136 (1922) (Holmes, J.)), by
doing “‘no more than any private citizen might do,’” id. at
1416 (quoting King, 563 U.S. at 469). In the typical case, if
the police do not have a warrant they may “approach the
home by the front path, knock promptly, wait briefly to be
received, and then (absent invitation to linger longer) leave.”
Id. at 1415. For two reasons, we agree with the district court
that the officers exceeded the scope of the customary license
to approach a home and knock.

    First, unexpected visitors are customarily expected to
knock on the front door of a home only during normal waking
hours. This does not mean that the “knock and talk”
exception never applies when officers knock on the door of
a home in the early morning. In some circumstances, an early
morning visit may be “consistent with an attempt to initiate
consensual contact with the occupants of the home.” Perea-
Rey, 680 F.3d at 1188. For example, officers may have
reason to believe that the resident in question generally
expects strangers on his porch early in the morning —
perhaps he sells fresh croissants out of his home. Or the
officers may have a reason for knocking that a resident would
ordinarily regard as important enough to warrant an early
morning disturbance — perhaps a fox has gotten into the
resident’s henhouse. Here, however, the officers knocked on
Lundin’s door around 4:00 a.m. without evidence that Lundin
generally accepted visitors at that hour, and without a reason
for knocking that a resident would ordinarily accept as
sufficiently weighty to justify the disturbance. Indeed, the
officers here acted for a purpose that virtually no resident
would willingly accept.
                 UNITED STATES V. LUNDIN                      13

    Second, the scope of a license is often limited to a specific
purpose, Jardines, 133 S. Ct. at 1416, and the customary
license to approach a home and knock is generally limited to
the “purpose of asking questions of the occupants,” Perea-
Rey, 680 F.3d at 1187 (citation omitted). Officers who knock
on the door of a home for other purposes generally exceed the
scope of the customary license and therefore do not qualify
for the “knock and talk” exception.

     “Reasonableness” under the Fourth Amendment “is
predominantly an objective inquiry.” Ashcroft v. al-Kidd,
563 U.S. 731, —, 131 S. Ct. 2074, 2080 (2011) (citation
omitted). A court’s task is usually to determine only
“whether the circumstances, viewed objectively, justify [the
challenged] action.” Id. (alteration in original) (citation
omitted). However, the Supreme Court has recognized
several “limited exception[s]” to this general rule, where
“actual motivations” matter. Id. (alteration in original)
(citation omitted). For example, police do not need a judicial
warrant or probable cause to conduct a search or seizure that
is justified by “special needs,” see, e.g., Vernonia Sch. Dist.
47J v. Acton, 515 U.S. 646, 665 (1995) (deterring drug use in
public schools), or to conduct an administrative inspection,
see, e.g., Michigan v. Clifford, 464 U.S. 287, 294 (1984)
(authorizing fire inspection).

    Before Jardines, it was not clear whether the proper
application of the “knock and talk” exception is an entirely
objective inquiry, or whether, as in special-needs-search and
administrative-inspection cases, the actual motivation of the
officers matters. The Court answered the question in
Jardines, explaining that the scope of the license to approach
a home and knock “is limited not only to a particular area but
also to a specific purpose.” 133 S. Ct. at 1416 (emphasis
14               UNITED STATES V. LUNDIN

added). That is, the application of the “knock and talk”
exception ultimately “depends upon whether the officers
ha[ve] an implied license to enter the [curtilage], which in
turn depends upon the purpose for which they enter[].” Id. at
1417 (emphasis added). After Jardines, it is clear that, like
the special-needs and administrative-inspection exceptions,
the “knock and talk” exception depends at least in part on an
officer’s subjective intent.

    The “knock and talk” exception to the warrant
requirement does not apply when officers encroach upon the
curtilage of a home with the intent to arrest the occupant.
Just as “the background social norms that invite a visitor to
the front door do not invite him there to conduct a search,” id.
at 1416, those norms also do not invite a visitor there to arrest
the occupant. We do not hold that an officer may never
conduct a “knock and talk” when he or she has probable
cause to arrest a resident but does not have an arrest warrant.
An officer does not violate the Fourth Amendment by
approaching a home at a reasonable hour and knocking on the
front door with the intent merely to ask the resident questions,
even if the officer has probable cause to arrest the resident.

    In this case, however, Deputy Aponte had asked dispatch
to broadcast a request that Lundin be arrested. The officers
who arrived at Lundin’s home were responding to that
request. Rather than obtain a warrant or wait for a time of
day when strangers might ordinarily visit, the officers
approached Lundin’s door at about 4:00 a.m. without a
warrant, immediately after they arrived at his home. Based
on this evidence, the district court found, as a matter of fact,
that the officers’ purpose in knocking on Lundin’s door was
to find and arrest him, and we see no reason to disturb that
finding. Thus, the officers violated Lundin’s Fourth
                 UNITED STATES V. LUNDIN                     15

Amendment right to be free from unlawful searches when
they stood on his porch and knocked on his front door. And
since this unconstitutional conduct caused the allegedly
exigent circumstance — the crashing noises in the backyard
— that circumstance cannot justify the search resulting in the
seizure of the two handguns.

     We note that our decision in United States v. Vaneaton,
49 F.3d 1423 (9th Cir. 1995), may be on infirm ground after
Jardines. In Vaneaton, officers had probable cause to arrest
the defendant for receiving stolen property and for violating
his parole, and they had reason to believe that he was staying
at the Rainbow Motel. Id. at 1425. The officers approached
the defendant’s motel room, knocked on the door, and
arrested him when he opened the door. Id. Our opinion did
not expressly note the officers’ purpose in knocking on the
defendant’s door, but it is fairly clear from our description of
the facts that they intended to arrest him. Although the
defendant was standing inside the doorway of his room, we
held that the officers lawfully arrested him because he
“‘voluntarily exposed himself to warrantless arrest’ by freely
opening the door of his motel room to the police.” Id. at 1426
(quoting United States v. Johnson, 626 F.2d 753, 757 (9th
Cir. 1980)).

    Unlike the officers in Jardines and in this case, the
officers in Vaneaton were standing in the common space of
a motel when they knocked, rather than in the curtilage of a
home. We therefore have no need to overrule Vaneaton. See
Miller v. Gammie, 335 F.3d 889, 899–900 (9th Cir. 2003) (en
banc) (holding that “a three-judge panel is free to reexamine
the holding of a prior panel” when the Supreme Court has
“undercut the theory or reasoning underlying the prior circuit
precedent in such a way that the cases are clearly
16               UNITED STATES V. LUNDIN

irreconcilable”). Whether Vaneaton remains good law after
Jardines is therefore a question for another case and another
day.

                    B. Protective Sweep

    The protective sweep doctrine authorizes “quick and
limited” warrantless inspections “of those spaces where a
person may be found” when “there are articulable facts
which, taken together with the rational inferences from those
facts, would warrant a reasonably prudent officer in believing
that the area to be swept harbor[ed] an individual posing a
danger to those on the arrest scene.” United States v. Lemus,
582 F.3d 958, 962 (9th Cir. 2009) (citation omitted)
(alteration in original). In this case, the officers had no
“reasonable, articulable suspicion” that anyone other than
Lundin was present at his residence. Maryland v. Buie,
494 U.S. 325, 336 (1990). Thus, the only plausible threat to
the safety of those on the scene was Lundin himself. By the
time the officers conducted the sweep of Lundin’s home,
however, he had already been handcuffed and placed in a
police vehicle. Thus, the officers lacked a reasonable ground
for believing that there was a danger that would have justified
the sweep of Lundin’s home.

                  C. Inevitable Discovery

     The inevitable discovery exception does not apply when
officers have probable cause to apply for a warrant but simply
fail to do so. See United States v. Mejia, 69 F.3d 309, 320
(9th Cir. 1995); United States v. Echegoyen, 799 F.2d 1271,
1280 n.7 (9th Cir. 1986). The government erroneously
suggests our decision in United States v. Merriweather,
777 F.2d 503 (9th Cir. 1985), holds to the contrary.
                 UNITED STATES V. LUNDIN                    17

    In Merriweather, federal agents performed a lawful
protective sweep of a motel room incident to an arrest.
During the sweep, an agent unlawfully searched the inside of
a toilet tank and found money hidden there. Id. at 505. The
police then obtained a search warrant for the motel room
without relying on the discovery of the money, and officers
who were unaware of the money executed the search warrant
and found it. Id. We held that the money was admissible. In
our opinion, we inaccurately characterized our decision as an
application of the “inevitable discovery doctrine.” Id. at 506.
Our decision in Merriweather is, instead, properly
characterized as an application of the independent source
doctrine. Unlike the inevitable discovery doctrine, which
asks whether evidence “would have” been discovered by
lawful means rather than by means of the illegal search, Nix
v. Williams, 467 U.S. 431, 447 (1984) (emphasis added), the
independent source doctrine asks whether the evidence
actually was “obtained independently from activities
untainted by the initial illegality.” Murray v. United States,
487 U.S. 533, 537 (1988).

    The two doctrines are, of course, related. See id. at 539
(“The inevitable discovery doctrine, with its distinct
requirements, is in reality an extrapolation from the
independent source doctrine.”). But the distinction between
the two doctrines is important because they create different
incentives. We do not apply the inevitable discovery doctrine
to warrantless searches where probable cause existed and a
warrant could therefore have been obtained because “[i]f
evidence were admitted notwithstanding the officers’
unexcused failure to obtain a warrant, simply because
probable cause existed, then there would never be any reason
for officers to seek a warrant.” Mejia, 69 F.3d at 320. Thus,
“to excuse the failure to obtain a warrant merely because the
18               UNITED STATES V. LUNDIN

officers had probable cause and could have inevitably
obtained a warrant would completely obviate the warrant
requirement of the fourth amendment.” United States v.
Young, 573 F.3d 711, 723 (9th Cir. 2009) (citation omitted).
Put differently, allowing the government to claim
admissibility under the inevitable discovery doctrine when
officers have probable cause to obtain a warrant but fail to do
so would encourage officers never to bother to obtain a
warrant.

    The independent source rule, by contrast, does not create
this incentive. As the Supreme Court has explained, a
rational officer who already has probable cause to obtain a
search warrant will ordinarily not enter the premises without
a warrant because “his action would add to the normal burden
of convincing a magistrate that there is probable cause the
much more onerous burden of convincing a trial court that no
information gained from the illegal entry affected either the
law enforcement officers’ decision to seek a warrant or the
magistrate’s decision to grant it.” Murray, 487 U.S. at 540.

    The officers here knew they had probable cause to arrest
Lundin. Deputy Aponte received corroborated information
from two witnesses that hours earlier Lundin had committed
numerous violent felonies. Aponte therefore requested
Lundin’s arrest under California Penal Code § 836.
However, the officers who arrived at Lundin’s home had no
right, absent an arrest warrant, to arrest Lundin in his home,
or, absent a search warrant, to search his home. Payton,
445 U.S. at 589–90. The officers nonetheless failed to obtain
any warrant before coming onto Lundin’s porch and knocking
on his door with the intention of arresting him. Thus, the
district court correctly held that the inevitable discovery
exception to the exclusionary rule does not apply. Indeed, it
                UNITED STATES V. LUNDIN                   19

would have erred had it held to the contrary. See Reilly,
224 F.3d at 995 (“[T]he district court committed clear error
in applying the inevitable discovery doctrine based on the
agents’ actual but unexercised opportunity to secure a search
warrant.”).

                        Conclusion

   For the foregoing reasons, we affirm the district court’s
grant of Lundin’s motion to suppress the two handguns seized
from Lundin’s home on April 23. We remand for further
proceedings.

   AFFIRMED.

```

---

## GROUP: _overhaul2/lake/cases/United States v. Lyle.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Lyle
type: case
citation: "919 F.3d 716 (2019)"
parallel_cite: ""
neutral_cite: ""
court: 2d Cir.
court_level: coa
circuit: ca2
year: 2019
date_decided: 2019-04-01
docket: 15-958
authority_weight: "Binding in-circuit — 2d Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/8443943/united-states-v-lyle/"
  cluster_id: 8443943
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Lyle
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: Key
related:
  - "[[Standing to Challenge a Search]]"
  - "[[Byrd v. United States]]"
  - "[[Rakas v. Illinois]]"
  - "[[Abandonment]]"
tags:
  - case
  - fourth-amendment
  - standing
  - reasonable-expectation-of-privacy
  - rental-car
  - byrd
  - inventory-search
  - second-circuit
holding: "On remand from the Supreme Court in light of Byrd v. United States, the Second Circuit reaffirmed that Lyle lacked standing to challenge the inventory search of a rental car, holding that he had no reasonable expectation of privacy in it because he was not merely an unauthorized driver but an unlicensed one — his possession was both unauthorized and unlawful — so Byrd, which protects an unauthorized driver in lawful possession, did not require a different result; convictions affirmed."
---

# United States v. Lyle

*919 F.3d 716 (2d Cir. 2019)* (No. 15-958) · U.S. Court of Appeals for the Second Circuit · **Binding in-circuit — 2d Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 8443943 → majority opinion 8415374 (919 F.3d 716, decided 2019-04-01, Chin, J.); Rule quote star-matched to the F.3d reporter pagination in the CL opinion text 2026-07-07. S9 promotes. -->

## Background
James Lyle and Michael Van Praagh were convicted in the Southern District of New York of offenses relating to methamphetamine distribution. On December 11, 2013, NYPD officers saw Lyle park and exit a car in midtown Manhattan, noticed an illegal gravity knife clipped to his pants, confirmed that his driver's license was suspended, and determined that the car was a rental for which he was not an authorized driver (Lyle said his girlfriend had rented it and let him drive). The officers arrested Lyle for driving on a suspended license and possessing the knife, impounded the car, and at the precinct conducted an inventory search that turned up over a pound of methamphetamine and roughly $39,000 in the trunk. The district court denied Lyle's motion to suppress. On his first appeal the Second Circuit affirmed; the Supreme Court then granted [[Reading and Citing Cases#certiorari-cert|certiorari]], [[Reading and Citing Cases#vacated|vacated]], and [[Reading and Citing Cases#on-remand|remanded]] for reconsideration in light of *[[Byrd v. United States|Byrd v. United States]]*, 138 S. Ct. 1518 (2018).

## Issue
Whether Lyle had a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] — and thus standing — to challenge the inventory search of a rental car he was driving without authorization and on a suspended license, given *[[Byrd v. United States|Byrd]]*'s holding that an unauthorized driver in lawful possession of a rental car may nonetheless retain a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]].

## Rule
*[[Byrd v. United States|Byrd]]* held that the "mere fact that a driver in lawful possession or control of a rental car is not listed on the rental agreement will not defeat his or her otherwise reasonable expectation of privacy" — but its protection is confined to **lawful** possession. Where the driver is not only unauthorized but also unlicensed, his possession is unlawful and he retains no legitimate privacy interest: "we concluded, and now reaffirm, that Lyle lacked standing not just because he was an unauthorized driver, but because he was an unlicensed one. Accordingly, Lyle's use of the rental car was both unauthorized *and* unlawful." — 919 F.3d at 729. ^pin-729

## Application
Lyle was not merely off the rental agreement: his license was suspended, so under N.Y. Vehicle & Traffic Law § 511 he could not lawfully operate any car, and a rental company aware of the facts certainly would not have permitted him to drive its car. His possession was therefore both unauthorized and unlawful — unlike the driver in *[[Byrd v. United States|Byrd]]*, who could have lawful possession and control and the attendant right to exclude. Because Lyle lacked a legitimate expectation of privacy, he had no [[Standing to Challenge a Search|standing to challenge]] the search, and the district court properly denied suppression. The court added, in the alternative, that the impoundment and inventory search were independently reasonable.

## Conclusion
**Affirmed.** Judge Chin wrote for the court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Lyle* is the Second Circuit's post-*[[Byrd v. United States|Byrd]]* marker on **standing / [[Reasonable Expectation of Privacy|reasonable expectation of privacy]]** in a rental car: *[[Byrd v. United States|Byrd]]* rejected a *[[Common Legal Terms#per-se|per se]]* no-privacy rule for unauthorized drivers, but it protects only those in **lawful** possession — a driver who is both unlisted on the rental agreement and unlicensed falls outside its shelter and lacks standing. Pair it with *[[Byrd v. United States|Byrd]]* and *[[Rakas v. Illinois|Rakas]]* on the possession-and-right-to-exclude basis for [[Standing to Challenge a Search|Fourth Amendment standing]].

## Appears on
- [[Standing to Challenge a Search]] — *Key*

## Sources
- [*United States v. Lyle*, 919 F.3d 716 (2d Cir. 2019)](https://www.courtlistener.com/opinion/8443943/united-states-v-lyle/) — pinpoint: 729 (no-reasonable-expectation-of-privacy / *Byrd*-does-not-help holding; the CL opinion text star-paginates the F.3d reporter). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c4abece525453afd", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Lyle"}, "payload": {"all": [{"cite": "919 F.3d 716", "page": "716", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "919"}], "display": "919 F.3d 716", "official": {"cite": "919 F.3d 716", "page": "716", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "919"}, "official_selection_present": true, "record_id": "United States v. Lyle"}}
{"assertion_id": "57d0d4ed79c01ffc", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Lyle"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Lyle", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Lyle

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Lyle",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Lyle",
    "case_name_short": "Lyle",
    "case_name_full": "United States v. James LYLE, aka Sealed 3, Michael Van Praagh, aka Sealed 1, Anthony Tarantino, aka Sealed 2",
    "input_case_name": "United States v. Lyle",
    "court": "2d Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca2",
    "state": null,
    "date_decided": "2019-04-01",
    "year": 2019,
    "docket": "15-958",
    "cluster_id": 8443943,
    "lead_opinion_id": 8415374,
    "sibling_ids": [],
    "absolute_url": "/opinion/8443943/united-states-v-lyle/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "919 F.3d 716",
      "volume": "919",
      "reporter": "F.3d",
      "page": "716",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "919 F.3d 716",
        "volume": "919",
        "reporter": "F.3d",
        "page": "716",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "919 F.3d 716",
    "official_selection": {
      "court_class": "coa",
      "selected": "919 F.3d 716",
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
    "date_created": "2026-07-07T18:16:34Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:16:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:16:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:16:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:16:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-lyle--8443943",
      "to_record_id": "United States v. Lyle",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Lyle

```
<opinion type="majority">
<author id="p-10">Chin, Circuit Judge:</author>
<p id="p-11"><a class="page-label" data-citation-index="1" data-label="722" href="#p722" id="p722">*722</a>Defendants-appellants James Lyle and Michael Van Praagh appeal from judgments of the United States District Court for the Southern District of New York (Crotty, <em>J.</em> ) convicting them on charges relating to the distribution of methamphetamine. Lyle challenges the admission at trial of evidence seized during a December 11, 2013 inventory search of a rental car and a January 9, 2014 search of his hotel room. He also challenges the admission at trial of certain post-arrest and proffer statements. Van Praagh challenges the sufficiency of the evidence of his participation in a methamphetamine distribution conspiracy, the admission of Lyle's post-arrest and proffer statements in their joint trial, and the reasonableness of his sentence. Because we conclude that the evidence at trial was sufficient to support all convictions, the challenged searches and seizures did not violate the Fourth Amendment, the admission of Lyle's statements did not violate the Fifth Amendment, and Van Praagh's sentence was reasonable, we affirm the judgments of the district court.</p>
<p id="p-12"><strong><em>BACKGROUND</em></strong></p>
<p id="p-13"><strong>I. <em>The Facts</em></strong></p>
<p id="p-14">Because Van Praagh and Lyle appeal convictions following a jury trial, we view the evidence in "the light most favorable to the government, crediting any inferences that the jury might have drawn in its favor." <em>United States v. Rosemond</em> , <extracted-citation case-ids="12173717" index="0" url="https://cite.case.law/f3d/841/95/#p99"><span class="citation" data-id="8414347"><a href="/opinion/8443021/united-states-v-rosemond/" aria-description="Citation for case: United States v. Rosemond">841 F.3d 95</a></span></extracted-citation>, 99-100 (2d Cir. 2016) (quoting <em>United States v. Dhinsa</em> , <extracted-citation case-ids="11124472" index="1" url="https://cite.case.law/f3d/243/635/#p643"><span class="citation" data-id="9843214"><a href="/opinion/772486/united-states-v-gurmeet-singh-dhinsa/" aria-description="Citation for case: United States v. Gurmeet Singh Dhinsa">243 F.3d 635</a></span></extracted-citation>, 643 (2d Cir. 2001) ).</p>
<p id="p-15"><strong><em>A. Overview</em></strong></p>
<p id="p-16">Throughout 2013, Van Praagh regularly sold pound quantities of methamphetamine. These deals generally occurred once a week and often took place in Manhattan hotels. Van Praagh also sold smaller quantities of methamphetamine out of his apartment in Queens and through in-person deliveries to his customers. Brandon Hodges, an Arizona-based methamphetamine supplier, sent Van Praagh methamphetamine on three or four occasions during this time, with the largest shipment containing four ounces of methamphetamine. Van Praagh regularly sold methamphetamine to Lyle, who was also a methamphetamine dealer in the New York area. Lyle regularly sold methamphetamine to Anthony Tarantino. Tarantino initially purchased methamphetamine for personal use, but eventually started selling small quantities of methamphetamine to his own clients. Both Hodges and Tarantino cooperated with the government and testified at trial.</p>
<p id="p-17">In January 2013, Lyle introduced Tarantino to Van Praagh. Tarantino accompanied Lyle to Van Praagh's apartment so that Lyle could restock his methamphetamine supply. While at Van Praagh's apartment, Tarantino saw Lyle purchase methamphetamine from Van Praagh, which Lyle later sold to Tarantino. In April 2013, Lyle took Tarantino to Van <a class="page-label" data-citation-index="1" data-label="723" href="#p723" id="p723">*723</a>Praagh's apartment a second time, where Tarantino again observed Lyle "re-up," <em>i.e.</em> , purchase methamphetamine, from Van Praagh. After this second visit, Tarantino and Van Praagh became romantically involved, and eventually Tarantino moved in with Van Praagh and began helping him sell methamphetamine.</p>
<p id="p-18"><strong><em>B. The Seizure of Methamphetamine from Van Praagh's Hotel Room</em></strong></p>
<p id="p-19">On May 29, 2013, Van Praagh and Tarantino checked into the Out Hotel in midtown Manhattan. That night, they sold pound quantities of methamphetamine to several customers, including Lyle. The next day, they checked out of the hotel but accidentally left approximately a pound of methamphetamine and $20,000 cash in the hotel room safe. Hotel staff found the drugs and money and called the New York City Police Department ("NYPD"), and officers arrived to seize the drugs and cash. After Van Praagh realized his mistake later that day, he returned to the hotel, where he was arrested by the NYPD. During the arrest, the officers seized a cellular phone and over $1,000 cash from Van Praagh's pocket. The officers also searched Van Praagh's Vespa scooter parked outside the hotel, where they found part of and packaging for a digital scale.</p>
<p id="p-20">Soon thereafter, Tarantino brought Lyle money to give to Van Praagh's father to bail Van Praagh out of jail. The day after Van Praagh got out of jail, he and Tarantino flew to Arizona to ensure that Van Praagh's methamphetamine suppliers would continue to sell to him. Van Praagh and Tarantino returned to New York and continued their sale of methamphetamine.</p>
<p id="p-21"><strong><em>C. Lyle's Arrests</em></strong></p>
<p id="p-22">On December 11, 2013, NYPD officers observed Lyle park and exit a car in midtown Manhattan. The officers noticed a knife clipped to Lyle's pants, which they later determined to be an illegal gravity knife. The officers approached Lyle as he was closing the trunk of the car. Lyle told the officers that he was legally permitted to carry a gravity knife because he was a member of the stagehands union and used the knife to perform his job. Lyle initially said he had not driven the car but when the officers informed him that they had seen him driving it, Lyle admitted as much. When asked for identification, Lyle produced a New York State ID with the expiration date scratched off. The officers confirmed that Lyle's driver's license was suspended. The officers also determined that the vehicle Lyle was driving was a rental car and that Lyle was not an authorized driver under the rental agreement. Lyle claimed that his girlfriend had rented the car and had given him permission to drive it. The officers arrested Lyle for driving with a suspended license and for possessing an illegal knife.</p>
<p id="p-23">Before heading to the station for processing, Lyle asked if the car could be left at the location and stated that his girlfriend would pick it up. The officers denied the request and impounded the vehicle. At the police precinct, an inventory search was conducted. Over one pound of methamphetamine and approximately $39,000 cash were found in the trunk of the car.</p>
<p id="p-24">The following day-December 12, 2013-Lyle was brought to the District Attorney's Office where he made certain statements in custody after being read his <em>Miranda</em> rights. When asked about the methamphetamine that was in the trunk of the rental car, Lyle stated that "an individual ... had contacted him and asked him to hold something for him." Tr. 435.<footnotemark>1</footnotemark> He <a class="page-label" data-citation-index="1" data-label="724" href="#p724" id="p724">*724</a>stated that upon meeting with that individual and another individual, he stayed in the car and did not see what was placed in the trunk but presumed it to be drugs because the individual that he was meeting with was known to distribute large quantities of methamphetamine in the New York area. When asked about his relationship with these two individuals, Lyle stated that he was friends with them, and had eventually begun working with one of them in delivering methamphetamine to the individual's customers.</p>
<p id="p-25">Lyle stated that the person in charge had a source of supply in Arizona named either Brendan or Brandon. Lyle also "provided a few names" of other people in the New York area who distributed large quantities of methamphetamine. Tr. 436.</p>
<p id="p-26">On January 9, 2014, police in East Windsor, New Jersey responded to an anonymous call that people were using methamphetamine in a hotel room. When they got to the hotel room, Lyle opened the door and invited the officers inside. The officers heard the toilet flush and saw Lyle's girlfriend come out of the bathroom. The officers observed a torch lighter on the bathroom shelf, a small clear bag next to the trash can, and a partial clear straw wrapper containing white residue on the bathroom floor. Additionally, they observed a towel under the bathroom doorway. In the bedroom, the officers noticed that a clear bag had been affixed to the smoke detector with rubber bands.</p>
<p id="p-27">Officers then performed a consent search of the room, and found approximately fourteen grams of methamphetamine, $3,270 cash, a digital scale, and numerous plastic baggies. Lyle and his girlfriend were both arrested.</p>
<p id="p-28"><strong>II. <em>The Proceedings Below</em></strong></p>
<p id="p-29"><strong><em>A. The Indictment and Van Praagh's Arrest</em></strong></p>
<p id="p-30">Van Praagh, Lyle, and Tarantino were indicted on March 20, 2014. On March 31, 2014, Drug Enforcement Administration ("DEA") agents arrested Van Praagh at his apartment. After receiving consent to search the apartment, agents found tools used to sell drugs, including a heat-sealer, packaging materials, and multiple scales, and a note from Hodges asking Van Praagh to have Lyle call him.</p>
<p id="p-31">On April 6, 2013, Van Praagh called his father from jail and told him, in a recorded call, "they got nothing.... I sterilized the house like I told you." Supp. App. 104. He also told him, "[t]hey got Anthony [Tarantino], but I'm expecting that he'll be disappearing any day now.... I believe that he had been talking." Supp. App. 105.</p>
<p id="p-32"><strong><em>B. Lyle's Proffer Session</em></strong></p>
<p id="p-33">On April 7, 2014, Lyle participated in a proffer session with the government in hope of reaching a cooperation agreement. A proffer agreement was executed, stipulating that the government would not use any of Lyle's statements made during the proffer sessions against him, except "to rebut any evidence or arguments offered by or on behalf of [Lyle]." Lyle App. 36.</p>
<p id="p-34">During the proffer session, Lyle admitted that (1) around 2011 or 2012, he sometimes stayed with Van Praagh while working on projects in New York City; (2) he observed Van Praagh smoking and using methamphetamine; (3) he occasionally delivered packages to Van Praagh's clients; (4) he accompanied Van Praagh to deliver methamphetamine thirty to fifty times; (5) Van Praagh told Lyle his supplier was in <a class="page-label" data-citation-index="1" data-label="725" href="#p725" id="p725">*725</a>Arizona; and (6) on one occasion, Lyle accompanied Van Praagh to pick up methamphetamine from a library in New York City.</p>
<p id="p-35"><strong><em>C. The Superseding Indictment and Pretrial Motions</em></strong></p>
<p id="p-36">A superseding indictment was filed September 30, 2014, charging (1) Van Praagh and Lyle with conspiring to distribute 500 grams or more of methamphetamine, in violation of <extracted-citation index="2" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%C2%A7%20846"><span class="citation no-link">21 U.S.C. §§ 846</span></extracted-citation> and 841(b)(1)(A), from December 2012 to January 2014; (2) Van Praagh with distributing and possessing with intent to distribute 50 grams or more of methamphetamine, in violation of <extracted-citation index="3" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%C2%A7%20841"><span class="citation no-link">21 U.S.C. §§ 841</span></extracted-citation>(a)(1) and 841(b)(1)(B), on or about May 30, 2013; and (3) Lyle with distributing and possessing with intent to distribute 50 grams or more of methamphetamine, in violation of <extracted-citation index="4" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%C2%A7%20841"><span class="citation no-link">21 U.S.C. §§ 841</span></extracted-citation>(a)(1) and 841(b)(1)(B), on or about December 11, 2013.</p>
<p id="p-37">Before trial, Lyle moved to suppress the physical evidence recovered from the search of the automobile, as well as his subsequent post-arrest statements. In an affidavit filed in support of the motion, Lyle admitted that (1) just prior to his arrest, he had been driving the car that had been rented by his girlfriend with her permission; (2) he possessed a gravity knife that day; (3) he initially told the police officers he had not been driving the car but later admitted to driving the car; and (4) his license was suspended at the time.</p>
<p id="p-38">On September 11, 2014, the district court held an evidentiary hearing on the voluntariness of Lyle's post-arrest statements and, on October 1, 2014, the court denied Lyle's motion to suppress. The court found there was probable cause for Lyle's arrest, based on his possession of a gravity knife. The court then concluded that the search of the rental car was justified on two independent bases. First, Lyle had no reasonable expectation of privacy in the rental car because he was not an authorized driver under the rental agreement. Second, the search of the rental car was a valid inventory search. The court also found that Lyle's post-arrest statements were made voluntarily and pursuant to a valid <em>Miranda</em> waiver.</p>
<p id="p-39"><strong><em>D. The Trial</em></strong></p>
<p id="p-40">Lyle and Van Praagh's trial began on October 14, 2014, and ended on October 20, 2014. The government called nineteen witnesses, and introduced physical evidence consisting of drugs and drug processing materials, text messages between the defendants, testimony regarding Lyle's post-arrest and proffer statements, and the recorded call Van Praagh made to his father while incarcerated. Van Praagh called one witness who testified about the circumstances of Van Praagh's March 31, 2014 arrest. Lyle did not put on a case.</p>
<p id="p-41">During his opening statement, Lyle's counsel stated that "[Lyle] obtained, bought, borrowed, was given methamphetamine for his own use. Where we dispute is the idea that he was a dealer." Tr. 28. Later that day, the government submitted a letter brief, asserting that Lyle's counsel's argument that Lyle was not a dealer opened the door to Lyle's proffer statements about distributing drugs with Van Praagh.</p>
<p id="p-42">Lyle's statements to law enforcement were admitted in two contexts. First, the district court allowed testimony regarding Lyle's December 12, 2013 post-arrest statements to law enforcement to be admitted only as against him, prohibiting mention of Van Praagh. Van Praagh did not object to the redacted testimony. Government witnesses testified that Lyle admitted that an "individual" for whom he worked as a "runner" "asked him to hold something for him" in the trunk of the <a class="page-label" data-citation-index="1" data-label="726" href="#p726" id="p726">*726</a>rental car, which Lyle "presumed ... to be drugs" because Lyle knew "[t]hat individual along with another individual" distributed "large quantities of crystal meth in the New York area." Tr. 435, 534. Lyle was friends "[m]ore so with the individual that had not placed the drugs in the trunk.... He said that he began as friends, and eventually he began working with that individual"-the "individual who was in charge"-"assisting him in delivering ... methamphetamine to that individual's customers." Tr. 435-36. Lyle told law enforcement that the individuals for whom he was working as a runner had a source of supply in Arizona named either Brendan or Brandon. Lyle also gave law enforcement "a few names" of other people in the New York area who distributed methamphetamine, including the names of three competitor drug dealers. Tr. 436. On cross-examination, Lyle's attorney elicited testimony that, during the post-arrest interview, Lyle "gave names of people during the conversation," one of which was Brandon or Brendan. Tr. 448.</p>
<p id="p-43">Second, toward the close of the government's case, the district court ruled-over Lyle's objection-that Lyle's proffer statements were admissible, but again prohibited mention of Van Praagh. Van Praagh did not object. The government witness then testified that Lyle admitted he had "first become involved in methamphetamine" in 2012 through "someone" he "knew ... from work." Tr. 517-18. Lyle observed "that person ... using and distributing crystal methamphetamine." Tr. 518. Lyle "began distributing small packages" for that person and "accompanying that person on deals as well as picking up crystal methamphetamine." <em><extracted-citation index="5" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%C2%A7%20841"><span class="citation no-link">Id.</span></extracted-citation></em> Lyle admitted that "he accompanied this person ... [on] between 30 to 50 occasions. And that at one point they had gone to a library in the New York City area ... to pick up crystal methamphetamine." <em><extracted-citation index="6" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%C2%A7%20841"><span class="citation no-link">Id.</span></extracted-citation></em> Lyle said the methamphetamine supplier was in Arizona.</p>
<p id="p-44">On cross-examination, Lyle's attorney elicited from the witness that "[Lyle] actually g[a]ve real names of people" during his proffer session, and provided "some names of people whose last names he didn't know." Tr. 524. These names included "Zaron," "Ted," "Bob," and "Joe." Tr. at 525.</p>
<p id="p-45">At the close of trial, the district court instructed the jury, in pertinent part: "There has been evidence that Mr. Lyle made statements to law enforcement authorities.... I want to let you know that ... Mr. Lyle's statement about his own conduct may not be considered or discussed by you with regard to Mr. Van Praagh." Tr. 713.</p>
<p id="p-46">On October 20, 2014, the jury found the defendants guilty on all counts. On March 25, 2015, the district court sentenced Lyle principally to the statutory mandatory minimum of 120 months' imprisonment and, on April 2, 2015, the district court sentenced Van Praagh principally to 144 months' imprisonment. In imposing a higher sentence on Van Praagh, the district court concluded that "Van Praagh had a higher role, more important role. He dealt in more drugs than did Mr. Lyle." Van Praagh App. 62.</p>
<p id="p-47">These appeals followed. On May 9, 2017, we issued an opinion affirming the district court's judgments. <em>United States v. Lyle</em> , <extracted-citation case-ids="12276679" index="7" url="https://cite.case.law/f3d/856/191/"><span class="citation" data-id="8414644"><a href="/opinion/8443281/united-states-v-lyle/" aria-description="Citation for case: United States v. Lyle">856 F.3d 191</a></span></extracted-citation> (2d Cir. 2017). Lyle petitioned for and was granted certiorari by the Supreme Court. On May 21, 2018, the Supreme Court vacated the judgment and remanded the case for further consideration in light of its intervening decision in <em>Byrd v. United States</em> , --- U.S. ----, <extracted-citation case-ids="12611477" index="8" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">138 S.Ct. 1518</a></span></extracted-citation>, <extracted-citation case-ids="12611477" index="9" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">200 L.Ed.2d 805</a></span></extracted-citation> (2018), which addressed the issue of the reasonable expectation of privacy of an unauthorized driver of a rental car. On July 6, 2018, the parties submitted letter briefs addressing <em><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">Byrd</a></span></em> 's impact upon this case. For the reasons <a class="page-label" data-citation-index="1" data-label="727" href="#p727" id="p727">*727</a>set forth below, we adhere to our original decision.</p>
<p id="p-48"><strong><em>DISCUSSION</em></strong></p>
<p id="p-49">Six issues are presented: (1) the validity of the warrantless search and seizure of the rental car; (2) the interpretation of Lyle's proffer agreement; (3) the sufficiency of the redactions to Lyle's proffer statements; (4) the admissibility of Lyle's New Jersey arrest; (5) the sufficiency of the conspiracy evidence against Van Praagh; and (6) the reasonableness of Van Praagh's sentence. We address each issue in turn.</p>
<p id="p-50"><strong>I. <em>Warrantless Search of Rental Car</em></strong></p>
<p id="p-51">We review a district court's ruling on a suppression motion for clear error as to factual findings, "giving special deference to findings that are based on determinations of witness credibility," and <em>de novo</em> as to questions of law. <em>United States v. Hussain</em> , <extracted-citation case-ids="4354628" index="10" url="https://cite.case.law/f3d/835/307/#p312"><span class="citation" data-id="8414221"><a href="/opinion/8442908/united-states-v-hussain/" aria-description="Citation for case: United States v. Hussain">835 F.3d 307</a></span></extracted-citation>, 312-13 (2d Cir. 2016) (quoting <em>United States v. Lucky</em> , <extracted-citation case-ids="3660831" index="11" url="https://cite.case.law/f3d/569/101/#p106"><span class="citation" data-id="1238356"><a href="/opinion/1238356/united-states-v-lucky/" aria-description="Citation for case: United States v. Lucky">569 F.3d 101</a></span></extracted-citation>, 106 (2d Cir. 2009) ). We conclude that Lyle's motion was properly denied for two independent reasons: first, Lyle had no reasonable expectation of privacy in the rental car, and, second, the inventory search of the rental car was reasonable.</p>
<p id="p-52"><strong><em>A. Applicable Law</em></strong></p>
<p id="p-53"><strong><em>i. Reasonable Expectation of Privacy in Rental Car</em></strong></p>
<p id="p-54">The Fourth Amendment guarantees citizens the "right ... to be secure in their ... effects, against unreasonable searches and seizures." U.S. Const. amend. IV. To prove that a search violated the Fourth Amendment, "an accused must show that he had a legitimate expectation of privacy in a searched place or item." <em>United States v. Rahme</em> , <extracted-citation case-ids="1689797" index="12" url="https://cite.case.law/f2d/813/31/#p34"><span class="citation" data-id="484266"><a href="/opinion/484266/united-states-v-riad-youssef-rahme/" aria-description="Citation for case: United States v. Riad Youssef Rahme">813 F.2d 31</a></span></extracted-citation>, 34 (2d Cir. 1987) (citing <em>Rawlings v. Kentucky</em> , <extracted-citation case-ids="1787600" index="13" url="https://cite.case.law/us/448/98/#p104"><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">448 U.S. 98</a></span></extracted-citation>, 104, <extracted-citation case-ids="1787600" index="14" url="https://cite.case.law/us/448/98/#p104"><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">100 S.Ct. 2556</a></span></extracted-citation>, <extracted-citation case-ids="1787600" index="15" url="https://cite.case.law/us/448/98/#p104"><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">65 L.Ed.2d 633</a></span></extracted-citation> (1980) ). The person challenging the search must demonstrate a subjective expectation of privacy in the place searched, and that expectation must be objectively reasonable. <em>United States v. Paulino</em> , <extracted-citation case-ids="1792539" index="16" url="https://cite.case.law/f2d/850/93/#p97"><span class="citation" data-id="9477828"><a href="/opinion/508162/united-states-v-francisco-paulino/" aria-description="Citation for case: United States v. Francisco Paulino">850 F.2d 93</a></span></extracted-citation>, 97 (2d Cir. 1988).</p>
<p id="p-55">When we previously ruled in this case, the question of whether an unauthorized driver has a reasonable expectation of privacy in a rental car divided the various circuit courts, resulting in at least three approaches. <em>See</em> <em>Lyle</em> , <extracted-citation case-ids="12276679" index="17" url="https://cite.case.law/f3d/856/191/"><span class="citation" data-id="8414644"><a href="/opinion/8443281/united-states-v-lyle/#200" aria-description="Citation for case: United States v. Lyle">856 F.3d at 200-01</a></span></extracted-citation> (reviewing circuit split). We did not rule on the question, as we decided the appeal on other grounds, as discussed below.</p>
<p id="p-56">The Supreme Court's recent decision in <em>Byrd v. United States</em> resolved the circuit split, holding that the "mere fact that a driver in lawful possession or control of a rental car is not listed on the rental agreement will not defeat his or her otherwise reasonable expectation of privacy." <extracted-citation case-ids="12611477" index="18" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">138 S.Ct. at 1531</a></span></extracted-citation>. The Court rejected the government's suggestion of a <em>per se</em> rule that unauthorized drivers "always lack an expectation of privacy in the automobile based on the rental company's lack of authorization alone." <em><extracted-citation case-ids="12611477" index="19" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12611477" index="19" url="https://cite.case.law/s-ct/138/1518/"> at 1527</extracted-citation>. Drawing from property principles, the Supreme Court reasoned that "[o]ne of the main rights attaching to property is the right to exclude others, and, in the main, one who owns or lawfully possesses or controls property will in all likelihood have a legitimate expectation of privacy by virtue of the right to exclude." <em><extracted-citation case-ids="12611477" index="20" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12611477" index="20" url="https://cite.case.law/s-ct/138/1518/"> at 1527</extracted-citation> (quoting <em>Rakas v. Illinois</em> , <extracted-citation case-ids="11329017" index="21" url="https://cite.case.law/us/439/128/"><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U.S. 128</a></span></extracted-citation>, 144 n. 12, <extracted-citation case-ids="11329017" index="22" url="https://cite.case.law/us/439/128/"><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. 421</a></span></extracted-citation>, <extracted-citation case-ids="11329017" index="23" url="https://cite.case.law/us/439/128/"><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">58 L.Ed.2d 387</a></span></extracted-citation> (1978) (internal quotation marks omitted)). It further noted, however, that the concept of lawful possession is central to the expectation of privacy inquiry, for a " 'wrongful' presence at the scene of a search would not enable a defendant to object to the legality of the search." <em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Id.</a></span></em> at 1529 (quoting <em>Rakas</em> , <extracted-citation case-ids="11329017" index="24" url="https://cite.case.law/us/439/128/">439 U.S. at </extracted-citation>141 n. 9, <extracted-citation case-ids="11329017" index="25" url="https://cite.case.law/us/439/128/"><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. 421</a></span></extracted-citation> ). Thus, "a person present in a stolen automobile at the time of the search may [not] object to the lawfulness of the search of the automobile"</p>
<p id="p-57"><a class="page-label" data-citation-index="1" data-label="728" href="#p728" id="p728">*728</a>regardless of his level of possession and control over the automobile. <em>See</em> <em>id</em> .</p>
<p id="p-58"><strong><em>ii. Community Caretaking Function</em></strong></p>
<p id="p-59">It is well established that police have the authority, despite the absence of a warrant, to seize and remove from the streets automobiles in the interests of public safety and as part of their community caretaking functions-an authority that is beyond reasonable challenge. <em>South Dakota v. Opperman</em> , <extracted-citation case-ids="6177992" index="26" url="https://cite.case.law/us/428/364/#p368"><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U.S. 364</a></span></extracted-citation>, 368-69, <extracted-citation case-ids="6177992" index="27" url="https://cite.case.law/us/428/364/#p368"><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">96 S.Ct. 3092</a></span></extracted-citation>, <extracted-citation case-ids="6177992" index="28" url="https://cite.case.law/us/428/364/#p368"><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">49 L.Ed.2d 1000</a></span></extracted-citation> (1976). In <em>Colorado v. Bertine</em> , the Supreme Court explained that, under this community caretaking exception to the warrant requirement, police officers may exercise their discretion in deciding whether to impound a vehicle, "so long as that discretion is exercised according to standard criteria and on the basis of something other than suspicion of evidence of criminal activity." <extracted-citation case-ids="6216740" index="29" url="https://cite.case.law/us/479/367/#p375"><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">479 U.S. 367</a></span></extracted-citation>, 375, <extracted-citation case-ids="6216740" index="30" url="https://cite.case.law/us/479/367/#p375"><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">107 S.Ct. 738</a></span></extracted-citation>, <extracted-citation case-ids="6216740" index="31" url="https://cite.case.law/us/479/367/#p375"><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">93 L.Ed.2d 739</a></span></extracted-citation> (1987). The question of whether <em>Bertine</em> and similar Supreme Court precedent require an officer's decision to impound a car to be made pursuant to standardized criteria, a question we have not addressed, has created a split among the circuits.</p>
<p id="p-60">Relying on a stricter interpretation of <em>Bertine</em> , two circuits have concluded that an officer's decision to impound a vehicle as part of its role as a community caretaker must be guided by a standardized procedure. <em>See</em> <em>United States v. Petty</em> , <extracted-citation case-ids="9249130" index="32" url="https://cite.case.law/f3d/367/1009/#p1012"><span class="citation" data-id="786133"><a href="/opinion/786133/united-states-v-jerry-l-petty/" aria-description="Citation for case: United States v. Jerry L. Petty">367 F.3d 1009</a></span></extracted-citation>, 1012 (8th Cir. 2004) (holding that "[s]ome degree of standardized criteria or established routine must regulate these police actions ... to ensure that impoundments and inventory searches are not merely a ruse for general rummaging in order to discover incriminating evidence" (internal quotation marks omitted)); <em>United States v. Duguay</em> , <extracted-citation case-ids="7630921" index="33" url="https://cite.case.law/f3d/93/346/#p351"><span class="citation" data-id="9489468"><a href="/opinion/724910/united-states-v-christopher-duguay/" aria-description="Citation for case: United States v. Christopher Duguay">93 F.3d 346</a></span></extracted-citation>, 351 (7th Cir. 1996) ("Among those criteria which must be standardized are the circumstances in which a car may be impounded."). Taking a slightly different approach, the D.C. Circuit has held that "if a standard impoundment procedure exists, a police officer's failure to adhere thereto is unreasonable and violates the Fourth Amendment." <em>United States v. Proctor</em> , <extracted-citation case-ids="3484762,3563372" index="34" url="https://cite.case.law/f3d/489/1348/"><span class="citation" data-id="186948"><a href="/opinion/186948/united-states-v-proctor-douglas/" aria-description="Citation for case: United States v. Proctor, Douglas">489 F.3d 1348</a></span></extracted-citation>, 1354 (D.C. Cir. 2007). The Tenth Circuit has held that standardized procedures are not required where an officer exercises "the community-caretaking functions of protecting public safety and promoting the efficient movement of traffic," but are required in other cases. <em>United States v. Sanders</em> , <extracted-citation case-ids="5767964" index="35" url="https://cite.case.law/f3d/796/1241/#p1245"><span class="citation" data-id="8413595"><a href="/opinion/8442347/united-states-v-sanders/" aria-description="Citation for case: United States v. Sanders">796 F.3d 1241</a></span></extracted-citation>, 1245 (10th Cir. 2015).</p>
<p id="p-61">The First, Third, and Fifth Circuits, however, have rejected the standardized criteria requirement, and instead focus their inquiry on the reasonableness of the impoundment under the circumstances. <em>See</em> <em>United States v. McKinnon</em> , <extracted-citation case-ids="3885876" index="36" url="https://cite.case.law/f3d/681/203/#p208"><span class="citation" data-id="2310827"><a href="/opinion/2310827/united-states-v-mckinnon/" aria-description="Citation for case: United States v. McKinnon">681 F.3d 203</a></span></extracted-citation>, 208 (5th Cir. 2012) (per curiam) (hinging analysis upon "the reasonableness of the 'community caretaker' impound viewed in the context of the facts and circumstances encountered by the officer" (citation omitted)); <em>United States v. Smith</em> , <extracted-citation case-ids="3761335" index="37" url="https://cite.case.law/f3d/522/305/#p314"><span class="citation" data-id="1240302"><a href="/opinion/1240302/united-states-v-smith/" aria-description="Citation for case: United States v. Smith">522 F.3d 305</a></span></extracted-citation>, 314 (3d Cir. 2008) (declining to adopt "the more structured approach ... requiring that there be standardized police procedures governing impoundments"); <em>United States v. Coccia</em> , <extracted-citation case-ids="2843114" index="38" url="https://cite.case.law/f3d/446/233/#p239"><span class="citation" data-id="202190"><a href="/opinion/202190/united-states-v-coccia/" aria-description="Citation for case: United States v. Coccia">446 F.3d 233</a></span></extracted-citation>, 239 (1st Cir. 2006) ("[I]mpoundments of vehicles for community caretaking purposes are consonant with the Fourth Amendment so long as the impoundment decision was reasonable under the circumstances."). These circuits read <em>Bertine</em> "to indicate that an impoundment decision made pursuant to standardized procedures will most likely, although not necessarily always, satisfy the Fourth Amendment." <em>Coccia</em> , <extracted-citation case-ids="2843114" index="39" url="https://cite.case.law/f3d/446/233/#p239"><span class="citation" data-id="202190"><a href="/opinion/202190/united-states-v-coccia/" aria-description="Citation for case: United States v. Coccia">446 F.3d at 238</a></span></extracted-citation>.</p>
<p id="p-62"><a class="page-label" data-citation-index="1" data-label="729" href="#p729" id="p729">*729</a><strong><em>B. Application</em></strong></p>
<p id="p-63"><strong><em>i. Reasonable Expectation of Privacy in Rental Car</em></strong></p>
<p id="p-64">In our prior decision, we specifically declined to decide whether an unauthorized driver ever has a reasonable expectation of privacy in a rental car. Instead, we concluded, and now reaffirm, that Lyle lacked standing not just because he was an unauthorized driver, but because he was an unlicensed one. Accordingly, Lyle's use of the rental car was both unauthorized <em>and</em> unlawful. <em>See</em> <extracted-citation index="40" url="https://cite.case.law/citations/?q=N.Y.%20Vehicle%20%26%20Traffic%20Law%20%C2%A7%20511"><span class="citation no-link">N.Y. Vehicle &amp; Traffic Law § 511</span></extracted-citation> (prohibiting operating a car without a valid license). Lyle should not have been driving any car because his license was suspended, and a rental company with knowledge of the relevant facts certainly would not have given him permission to drive its car nor allowed a renter to let him do so. Under these circumstances, Lyle did not have a reasonable expectation of privacy in the rental car. <em>See</em> <em>United States v. Haywood</em> , <extracted-citation case-ids="2160886" index="41" url="https://cite.case.law/f3d/324/514/#p516"><span class="citation" data-id="781422"><a href="/opinion/781422/united-states-v-eugene-haywood/" aria-description="Citation for case: United States v. Eugene Haywood">324 F.3d 514</a></span></extracted-citation>, 516 (7th Cir. 2003) (declining to resolve circuit split over whether unauthorized driver had reasonable expectation of privacy in rental car, because unauthorized driver also had suspended license and the combination resulted in no reasonable expectation of privacy); <em>cf.</em> <em>United States v. Tropiano</em> , <extracted-citation case-ids="7412372" index="42" url="https://cite.case.law/f3d/50/157/#p161"><span class="citation" data-id="691961"><a href="/opinion/691961/united-states-v-daniel-michael-tropiano/" aria-description="Citation for case: United States v. Daniel Michael Tropiano">50 F.3d 157</a></span></extracted-citation>, 161 (2d Cir. 1995) ("[W]e think it obvious that a defendant who knowingly possesses a stolen car has no legitimate expectation of privacy in the car."); <em>United States v. Ponce</em> , <extracted-citation case-ids="10522522" index="43" url="https://cite.case.law/f2d/947/646/#p649"><span class="citation" data-id="570497"><a href="/opinion/570497/united-states-v-gerardo-i-ponce-juan-c-gonzalez-calas-and-hipolito/" aria-description="Citation for case: United States v. Gerardo I. Ponce, Juan C. Gonzalez-Calas...">947 F.2d 646</a></span></extracted-citation>, 649 (2d Cir. 1991) ("To mount a challenge to a search of a vehicle, defendants must show, among other things, a legitimate basis for being in it, such as permission from the owner.").</p>
<p id="p-65"><em><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">Byrd</a></span></em> does not require a different result. The Court there held that an unauthorized driver in sole possession of a rental car could have a legitimate expectation of privacy in the vehicle because even an unauthorized driver, in the right circumstances, could have "lawful possession and control and the attendant right to exclude." <extracted-citation case-ids="12611477" index="44" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">138 S.Ct. at 1528</a></span></extracted-citation>. The Court noted that "there may be countless innocuous reasons why an unauthorized driver might get behind the wheel of a rental car and drive it-perhaps the renter is drowsy or inebriated." <em><extracted-citation case-ids="12611477" index="45" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12611477" index="45" url="https://cite.case.law/s-ct/138/1518/"> at 1529</extracted-citation>.</p>
<p id="p-66">This reasoning does not apply to the circumstances here, where Lyle was not only the driver of the vehicle but the sole occupant. Because Lyle did not have a valid driver's license, it was unlawful for him to be operating the vehicle. He did not have <em>lawful</em> possession and control of the vehicle in the sense that he unlawfully drove the vehicle onto the scene and could not lawfully drive it away. <em>See <extracted-citation case-<span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">ids="12611477" index="46" url="https://cite.</a></span>case.law/s-ct/138/1518/">id.</extracted-citation></em> (reaffirming conclusion in <em>Rakas v. Illinois</em> that " 'wrongful' presence at the scene of a search would not enable a defendant to object to the legality of the search," "[n]o matter the degree of [a defendant's] possession and control.")<em>.</em> While the absence of a valid license alone may not destroy an unauthorized driver's expectation of privacy, Lyle's possession and control of the car was unlawful the moment he started driving it. Just as a car thief would not have a reasonable expectation of privacy in a stolen car, <em><extracted-citation case-ids="12611477" index="47" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">id.</a></span></extracted-citation></em> , an unauthorized, unlicensed driver in sole possession of a rental car does not have a reasonable expectation of privacy in the vehicle. Therefore, because Lyle's operation of the car rendered his possession and control unlawful, <em><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">Byrd</a></span></em> is distinguishable.</p>
<p id="p-67">Further, unlike the Eighth and Ninth Circuits, which have held that a defendant may have standing to challenge a search of a rental car despite lacking a valid license and authorization under the rental agreement if he received an authorized driver's permission, <em>United States v. Best</em> , <extracted-citation case-ids="11877555" index="48" url="https://cite.case.law/f3d/135/1223/"><span class="citation" data-id="751576"><a href="/opinion/751576/united-states-v-tony-cornelius-best/" aria-description="Citation for case: United States v. Tony Cornelius Best">135 F.3d 1223</a></span></extracted-citation> (8th Cir. 1998) ;</p>
<p id="p-68"><a class="page-label" data-citation-index="1" data-label="730" href="#p730" id="p730">*730</a><em>United States v. Thomas</em> , <extracted-citation case-ids="5860809" index="49" url="https://cite.case.law/f3d/447/1191/"><span class="citation" data-id="794349"><a href="/opinion/794349/united-states-v-roshon-e-thomas-aka-rollin-roy-phillips/" aria-description="Citation for case: United States v. Roshon E. Thomas, AKA Rollin Roy Phillips">447 F.3d 1191</a></span></extracted-citation> (9th Cir. 2006), we conclude that an authorized renter's permission is not determinative of whether a defendant has a reasonable expectation of privacy. Indeed, <em><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">Byrd</a></span></em> explicitly rejected the notion that legitimate presence alone affords a defendant with a reasonable expectation of privacy. <extracted-citation case-ids="12611477" index="50" url="https://cite.case.law/s-ct/138/1518/"><span class="citation" data-id="4274911"><a href="/opinion/4497658/byrd-v-united-states/" aria-description="Citation for case: Byrd v. United States">138 S.Ct. at 1527</a></span></extracted-citation> (quoting <em>Rakas</em> , <extracted-citation case-ids="11329017" index="51" url="https://cite.case.law/us/439/128/"><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U.S. at 148</a></span></extracted-citation>, <extracted-citation case-ids="11329017" index="52" url="https://cite.case.law/us/439/128/"><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. 421</a></span></extracted-citation> (noting that legitimate presence is relevant, but not controlling)). While a defendant does not lose all his Fourth Amendment rights simply by engaging in illegal acts, he may still lack standing to challenge a search when the law prevents him from being there in the first place, even with the owner's permission. <em>See</em> <em>United States v. Schram</em> , <extracted-citation case-ids="12518285" index="53" url="https://cite.case.law/f3d/901/1042/#p1045"><span class="citation" data-id="4305748"><a href="/opinion/4528495/united-states-v-gerald-schram/" aria-description="Citation for case: United States v. Gerald Schram">901 F.3d 1042</a></span></extracted-citation>, 1045 (9th Cir. 2018) (rejecting argument that defendant had standing to object to the search of his girlfriend's house because the no-contact order prohibiting him from contacting his girlfriend was vitiated by her consent to enter the property). Here, even assuming that, under different circumstances, an unlicensed driver may have an expectation of privacy in a rental car, Lyle's possession and control was unlawful while driving the rental car both without a license and without authorization. <em>Cf.</em> <em>United States v. Walton</em> , <extracted-citation case-ids="4180655" index="54" url="https://cite.case.law/f3d/763/655/#p663"><span class="citation" data-id="2717801"><a href="/opinion/2717801/united-states-v-kenyon-walton/" aria-description="Citation for case: United States v. Kenyon Walton">763 F.3d 655</a></span></extracted-citation>, 663 (7th Cir. 2014) (holding that defendant, who was passenger at time of search and sole authorized driver listed on rental agreement, had reasonable expectation of privacy in rental car despite lacking driver's license because "[a] driver of a car does not lose all Fourth Amendment protections simply because his license is invalid," but observing that conclusion would not obtain if person were both unlicensed and unauthorized).</p>
<p id="p-69">Lyle argues that he was not operating the vehicle when he was arrested and that he lawfully possessed the vehicle. These arguments ignore the fact that Lyle was seen by the agents driving the vehicle, and, indeed, he eventually admitted as much. Because he was driving the vehicle illegally, Lyle did not have <em>lawful</em> possession or control of the vehicle and he does not have standing to challenge the search.</p>
<p id="p-70">Lyle's reliance on the Sixth Circuit's decision in <em>United States v. Smith</em> , <extracted-citation case-ids="9484437" index="55" url="https://cite.case.law/f3d/263/571/#p586"><span class="citation" data-id="774727"><a href="/opinion/774727/united-states-v-steven-eugene-smith-randy-ray-smith/" aria-description="Citation for case: United States v. Steven Eugene Smith, Randy Ray Smith">263 F.3d 571</a></span></extracted-citation>, 586 (6th Cir. 2001), is misplaced. <em>Smith</em> presented unique facts. Specifically, Smith was not only the husband of the renter, but he also "had a business relationship with the rental company" because he had "called the rental company to reserve the rental vehicle," "was given a reservation number," and "provided the company with his credit card number, and that credit card was subsequently billed for the rental of the vehicle." <em><extracted-citation case-ids="9484437" index="56" url="https://cite.case.law/f3d/263/571/#p586">Id.</extracted-citation></em> In light of these facts, the Sixth Circuit determined that "Smith was the <em>de facto</em> renter of the vehicle" and that, therefore, he had a legitimate expectation of privacy in the rental car. <em><extracted-citation case-ids="9484437" index="57" url="https://cite.case.law/f3d/263/571/#p586">Id.</extracted-citation></em><extracted-citation case-ids="9484437" index="57" url="https://cite.case.law/f3d/263/571/#p586"> at 586-87</extracted-citation>. Lyle was not the <em>de facto</em> renter of the car at issue here. Moreover, the Sixth Circuit also noted that Smith was a licensed driver. <em><extracted-citation case-ids="9484437" index="58" url="https://cite.case.law/f3d/263/571/#p586">Id.</extracted-citation></em><extracted-citation case-ids="9484437" index="58" url="https://cite.case.law/f3d/263/571/#p586"> at 586</extracted-citation> ("Smith was a licensed driver .... Therefore, it was not illegal for Smith [to] drive the vehicle."). For these reasons, <em>Smith</em> is distinguishable.</p>
<p id="p-71">Accordingly, we adhere to our original conclusion that Lyle lacked a reasonable expectation of privacy in the rental car, and the district court did not err in denying his motion to suppress.</p>
<p id="p-72"><strong><em>ii. Impoundment of Rental Car</em></strong></p>
<p id="p-73">Even assuming Lyle had a legitimate privacy interest in the rental car, his challenge to the inventory search fails on the merits as the impoundment of the rental car did not violate the Fourth Amendment.<footnotemark>2</footnotemark> The Supreme Court has repeatedly <a class="page-label" data-citation-index="1" data-label="731" href="#p731" id="p731">*731</a>held that the touchstone of the Fourth Amendment is reasonableness, <em>see</em> <em>United States v. Ramirez</em> , <extracted-citation case-ids="11503214" index="59" url="https://cite.case.law/us/523/65/#p71"><span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/" aria-description="Citation for case: United States v. Ramirez">523 U.S. 65</a></span></extracted-citation>, 71, <extracted-citation case-ids="11503214" index="60" url="https://cite.case.law/us/523/65/#p71"><span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/" aria-description="Citation for case: United States v. Ramirez">118 S.Ct. 992</a></span></extracted-citation>, <extracted-citation case-ids="11503214" index="61" url="https://cite.case.law/us/523/65/#p71"><span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/" aria-description="Citation for case: United States v. Ramirez">140 L.Ed.2d 191</a></span></extracted-citation> (1998), which "in turn, is measured in objective terms by examining the totality of the circumstances," <em>Ohio v. Robinette</em> , <extracted-citation case-ids="11594631" index="62" url="https://cite.case.law/us/519/33/#p39"><span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/" aria-description="Citation for case: Ohio v. Robinette">519 U.S. 33</a></span></extracted-citation>, 39, <extracted-citation case-ids="11594631" index="63" url="https://cite.case.law/us/519/33/#p39"><span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/" aria-description="Citation for case: Ohio v. Robinette">117 S.Ct. 417</a></span></extracted-citation>, <extracted-citation case-ids="11594631" index="64" url="https://cite.case.law/us/519/33/#p39"><span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/" aria-description="Citation for case: Ohio v. Robinette">136 L.Ed.2d 347</a></span></extracted-citation> (1996). Thus, in line with the First, Third, and Fifth Circuits, we conclude that "whether a decision to impound is reasonable under the Fourth Amendment is based on all the facts and circumstances of a given case." <em>Coccia</em> , <extracted-citation case-ids="2843114" index="65" url="https://cite.case.law/f3d/446/233/#p239"><span class="citation" data-id="202190"><a href="/opinion/202190/united-states-v-coccia/" aria-description="Citation for case: United States v. Coccia">446 F.3d at 239</a></span></extracted-citation>. While the existence of and an officer's adherence to a standardized criteria may be helpful in evaluating the reasonableness of an impoundment, we decline to adopt a standardized impoundment procedure requirement.</p>
<p id="p-74">Using a totality of the circumstances analysis, we conclude that the impoundment here was reasonable under the Fourth Amendment even absent standardized procedures. Here, at the time of his arrest for driving with a suspended license and for possessing an illegal knife, Lyle was the rental car's driver and sole occupant. As there was no third party immediately available to entrust with the vehicle's safekeeping, the officers could not be certain how long the rental car would be unattended in Lyle's absence. Even if Lyle did not expect to be in custody long, Lyle would not have been able to operate the car himself upon release due to his suspended license. Although Lyle asked for the opportunity to arrange for his girlfriend, the authorized driver under the rental agreement, to remove the rental car, the police were not required to grant the request. <em>See</em> <em>Bertine</em> , <extracted-citation case-ids="6216740" index="66" url="https://cite.case.law/us/479/367/#p375"><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">479 U.S. at 374</a></span>-75</extracted-citation>, <extracted-citation case-ids="6216740" index="67" url="https://cite.case.law/us/479/367/#p375"><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">107 S.Ct. 738</a></span></extracted-citation> ; <em>see also</em> <em>Duguay</em> , <extracted-citation case-ids="7630921" index="68" url="https://cite.case.law/f3d/93/346/#p351">93 F.3d at </extracted-citation>353 &amp; n. 2 (holding impoundment of car unconstitutional when the vehicle's other occupant was present at the arrest and could "provide for the speedy and efficient removal of the car from public thoroughfares," but noting that the Seventh Circuit has affirmed impoundments where the arrestee is the vehicle's sole occupant and is legitimately arrested). Instead, by impounding the vehicle, the officer ensured that the rental vehicle was not left on a public street in a busy midtown Manhattan location where it could have become a nuisance or been stolen or damaged and could have become illegally parked the next day. <em>See</em> <em>Opperman</em> , <extracted-citation case-ids="6177992" index="69" url="https://cite.case.law/us/428/364/#p368"><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U.S. at 368</a></span>-69</extracted-citation>, <extracted-citation case-ids="6177992" index="70" url="https://cite.case.law/us/428/364/#p368"><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">96 S.Ct. 3092</a></span></extracted-citation> (describing as "beyond challenge" the authority of police "to seize and remove from the streets vehicles impeding traffic or threatening public safety and convenience," such as vehicles that "violate parking ordinances"); <em>Sanders</em> , <extracted-citation case-ids="5767964" index="71" url="https://cite.case.law/f3d/796/1241/#p1245"><span class="citation" data-id="8413595"><a href="/opinion/8442347/united-states-v-sanders/#1249" aria-description="Citation for case: United States v. Sanders">796 F.3d at 1249</a></span></extracted-citation> (" <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span></em> establishes that if a vehicle is obstructing or impeding traffic on public property, it can be impounded regardless of whether the impoundment is guided by standardized procedures."). Moreover, there is no indication that the officers did not act in good faith or solely for the purpose of investigation in exercising their discretion to impound the rental car.</p>
<p id="p-75">Our decision in <em>United States v. Lopez</em> , <extracted-citation case-ids="6051917" index="72" url="https://cite.case.law/f3d/547/364/"><span class="citation" data-id="1225666"><a href="/opinion/1225666/united-states-v-lopez/" aria-description="Citation for case: United States v. Lopez">547 F.3d 364</a></span></extracted-citation> (2d Cir. 2008), is instructive. There, although our discussion primarily concerned the constitutionality of the inventory search itself, we concluded that the circumstances called for the impoundment of Lopez's car despite any showing of a standardized impoundment policy. <em><extracted-citation case-ids="6051917" index="73" url="https://cite.case.law/f3d/547/364/"><span class="citation" data-id="1225666"><a href="/opinion/1225666/united-states-v-lopez/" aria-description="Citation for case: United States v. Lopez">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6051917" index="73" url="https://cite.case.law/f3d/547/364/"> at 372</extracted-citation>. Similar to Lyle, Lopez was arrested <a class="page-label" data-citation-index="1" data-label="732" href="#p732" id="p732">*732</a>and there was no one immediately available to move his car for safekeeping in Lopez's case because the only other passenger was also arrested. <em>See</em> <em>id</em> . at 366-67. Moreover, like Lyle's car, Lopez's car was parked on a city street. <em><extracted-citation case-ids="6051917" index="74" url="https://cite.case.law/f3d/547/364/"><span class="citation" data-id="1225666"><a href="/opinion/1225666/united-states-v-lopez/" aria-description="Citation for case: United States v. Lopez">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6051917" index="74" url="https://cite.case.law/f3d/547/364/"> at 366</extracted-citation>.</p>
<p id="p-76">Thus, even if Lyle had a reasonable expectation of privacy in the rental car, the district court did not err in denying his motion to suppress.</p>
<p id="p-77"><strong>II. <em>The Proffer Agreement Waiver</em></strong></p>
<p id="p-78">We review the district court's interpretation of the scope of a proffer agreement waiver <em>de novo</em> and its evidentiary rulings for abuse of discretion. <em>Rosemond</em> , <extracted-citation case-ids="12173717" index="75" url="https://cite.case.law/f3d/841/95/#p99"><span class="citation" data-id="8414347"><a href="/opinion/8443021/united-states-v-rosemond/" aria-description="Citation for case: United States v. Rosemond">841 F.3d at 107</a></span></extracted-citation>.</p>
<p id="p-79"><strong><em>A. Applicable Law</em></strong></p>
<p id="p-80">Ordinarily, a "statement made during plea discussions with an attorney for the prosecuting authority" that does not result in a guilty plea is not admissible against the defendant who made the statement. Fed. R. Evid. 410(a)(4). The protections provided by Rule 410, however, can be waived, including in a proffer agreement with the government, provided that such waiver is knowing and voluntary. <em>Rosemond</em> , <extracted-citation case-ids="12173717" index="76" url="https://cite.case.law/f3d/841/95/#p99">841 F.3d at </extracted-citation>107 ; <em>United States v. Velez</em> , <extracted-citation case-ids="9294404" index="77" url="https://cite.case.law/f3d/354/190/#p194"><span class="citation" data-id="784640"><a href="/opinion/784640/united-states-v-jose-velez/" aria-description="Citation for case: UNITED STATES v. JOSÉ VELEZ">354 F.3d 190</a></span></extracted-citation>, 194-95 (2d Cir. 2004).</p>
<p id="p-81">To determine whether a proffer agreement's waiver provision applies, we ask first whether the defendant has offered any evidence or made a factual assertion that would trigger the Rule 410 waiver, and, "if so, whether the proffer statement 'fairly rebut[s]' the fact asserted or evidence offered or elicited." <em>Rosemond</em> , <extracted-citation case-ids="12173717" index="78" url="https://cite.case.law/f3d/841/95/#p99"><span class="citation" data-id="8414347"><a href="/opinion/8443021/united-states-v-rosemond/" aria-description="Citation for case: United States v. Rosemond">841 F.3d at 107</a></span></extracted-citation>. If the waiver has been triggered and the proffer statement properly rebuts the assertion triggering the waiver, the government may offer the proffer statement. <em><extracted-citation case-ids="12173717" index="79" url="https://cite.case.law/f3d/841/95/#p99"><span class="citation" data-id="8414347"><a href="/opinion/8443021/united-states-v-rosemond/" aria-description="Citation for case: United States v. Rosemond">Id.</a></span></extracted-citation></em></p>
<p id="p-82">In <em><span class="citation" data-id="8414347"><a href="/opinion/8443021/united-states-v-rosemond/" aria-description="Citation for case: United States v. Rosemond">Rosemond</a></span></em> , we gave examples of factual assertions that will trigger the proffer waiver, including "asserting, in an opening statement, that someone other than the defendant was the real perpetrator of the crime," <em><extracted-citation case-<span class="citation" data-id="8414347"><a href="/opinion/8443021/united-states-v-rosemond/" aria-description="Citation for case: United States v. Rosemond">ids="12173717" index="80" url="https://cite.</a></span>case.law/f3d/841/95/#p99">id.</extracted-citation></em> at 109 (citing <em>United States v. Barrow</em> , <extracted-citation case-ids="9170857" index="81" url="https://cite.case.law/f3d/400/109/#p114"><span class="citation" data-id="789452"><a href="/opinion/789452/united-states-v-leotha-barrow-also-known-as-petey-calvin-johnson-also/" aria-description="Citation for case: United States v. Leotha Barrow, Also Known as &quot;Petey&quot;,...">400 F.3d 109</a></span></extracted-citation>, 114, 119 (2d Cir. 2005) ), and "arguing that a shooting was 'an intended kidnapping gone wrong,' when the defendant admitted in a proffer session that the shooting was 'an intentional murder,' " <em><extracted-citation case-<span class="citation" data-id="789452"><a href="/opinion/789452/united-states-v-leotha-barrow-also-known-as-petey-calvin-johnson-also/" aria-description="Citation for case: United States v. Leotha Barrow, Also Known as &quot;Petey&quot;,...">ids="9170857" index="82" url="https://cite.</a></span>case.law/f3d/400/109/#p114">id.</extracted-citation></em><extracted-citation case-ids="9170857" index="82" url="https://cite.case.law/f3d/400/109/#p114"> at 110</extracted-citation> (quoting <em>United States v. Gomez</em> , <extracted-citation case-ids="9403243" index="83" url="https://cite.case.law/f-supp-2d/210/465/#p472"><span class="citation" data-id="2579550"><a href="/opinion/2579550/united-states-v-gomez/" aria-description="Citation for case: United States v. Gomez">210 F.Supp.2d 465</a></span></extracted-citation>, 472 (S.D.N.Y. 2002) ).</p>
<p id="p-83"><strong><em>B. Application</em></strong></p>
<p id="p-84">The district court properly held that the waiver was triggered by Lyle's counsel's statement during opening argument that "we dispute [ ] the idea that [Lyle] was a dealer." Tr. 28. Lyle's proffer agreement contained a waiver that allowed his statements to come in "to rebut any evidence or arguments offered by or on behalf of [Lyle]." Lyle App. 36.</p>
<p id="p-85">As this Court has recognized, a defense argument does not trigger a waiver if it "simply challenge[s] the sufficiency of government proof on [the] elements." <em>Barrow</em> , <extracted-citation case-ids="9170857" index="84" url="https://cite.case.law/f3d/400/109/#p114"><span class="citation" data-id="789452"><a href="/opinion/789452/united-states-v-leotha-barrow-also-known-as-petey-calvin-johnson-also/" aria-description="Citation for case: United States v. Leotha Barrow, Also Known as &quot;Petey&quot;,...">400 F.3d at 119</a></span></extracted-citation>. But "a statement of fact in a defense opening, such as [a] statement ... unequivocally identifying [someone other than defendant] as the real perpetrator of the charged crimes," is a factual assertion that would trigger a waiver provision. <em><extracted-citation case-ids="9170857" index="85" url="https://cite.case.law/f3d/400/109/#p114"><span class="citation" data-id="789452"><a href="/opinion/789452/united-states-v-leotha-barrow-also-known-as-petey-calvin-johnson-also/" aria-description="Citation for case: United States v. Leotha Barrow, Also Known as &quot;Petey&quot;,...">Id.</a></span></extracted-citation></em> Here, defense counsel did not ascribe the charged crime to someone else, but he did more than challenge the sufficiency of the government's proof. Rather than argue that the government would not adduce credible evidence that Lyle was a drug dealer, counsel disputed the very idea that Lyle was a dealer. This is the functional equivalent of an affirmative statement that Lyle, in fact, did not deal methamphetamine. This assertion was belied by Lyle's proffer admissions and, thus, triggered <a class="page-label" data-citation-index="1" data-label="733" href="#p733" id="p733">*733</a>the waiver provision in the proffer agreement.</p>
<p id="p-86">Lyle's proffer statements fairly rebut his counsel's opening argument that Lyle was not a dealer. The proffer statements at issue included that (1) Lyle repeatedly distributed "small packages" of methamphetamine; (2) Lyle accompanied another person to obtain and deliver methamphetamine; and (3) Lyle knew the location of the methamphetamine supplier. Taken together, these statements imply participation in a drug distribution operation and thus fairly rebut Lyle's counsel's argument in his opening statement that Lyle was a mere user of methamphetamine and not a dealer. <em>See</em> <em>Barrow</em> , <extracted-citation case-ids="9170857" index="86" url="https://cite.case.law/f3d/400/109/#p114"><span class="citation" data-id="789452"><a href="/opinion/789452/united-states-v-leotha-barrow-also-known-as-petey-calvin-johnson-also/#120" aria-description="Citation for case: United States v. Leotha Barrow, Also Known as &quot;Petey&quot;,...">400 F.3d at 120-21</a></span></extracted-citation> (emphasizing that "proper rebuttal is not limited to direct contradiction" but "encompasses any evidence that the trial judge concludes fairly counters and casts doubt on the truthfulness of factual assertions advanced, whether directly or implicitly, by an adversary").</p>
<p id="p-87">Hence, we conclude that the district court did not abuse its discretion in admitting Lyle's proffer statements.</p>
<p id="p-88"><strong>III. <em>The Admission of Lyle's Redacted Statements</em></strong></p>
<p id="p-89"><strong><em>A. Applicable Law</em></strong></p>
<p id="p-90">In <em>Bruton v. United States</em> , <extracted-citation case-ids="1767670" index="87" url="https://cite.case.law/us/391/123/#p135"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">391 U.S. 123</a></span></extracted-citation>, 135-36, <extracted-citation case-ids="1767670" index="88" url="https://cite.case.law/us/391/123/#p135"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">88 S.Ct. 1620</a></span></extracted-citation>, <extracted-citation case-ids="1767670" index="89" url="https://cite.case.law/us/391/123/#p135"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">20 L.Ed.2d 476</a></span></extracted-citation> (1968), the Supreme Court held that admission of a non-testifying co-defendant's confession naming the defendant as a perpetrator at their joint trial violates the latter's Sixth Amendment right to cross-examination. The Court later made clear that a non-obvious redaction of a co-defendant's confession to eliminate any references to the defendant will eliminate any <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> problem. <em>See</em> <em>Gray v. Maryland</em> , <extracted-citation case-ids="11503401" index="90" url="https://cite.case.law/us/523/185/#p195"><span class="citation" data-id="9433593"><a href="/opinion/118184/gray-v-maryland/" aria-description="Citation for case: Gray v. Maryland">523 U.S. 185</a></span></extracted-citation>, 195-97, <extracted-citation case-ids="11503401" index="91" url="https://cite.case.law/us/523/185/#p195"><span class="citation" data-id="9433593"><a href="/opinion/118184/gray-v-maryland/" aria-description="Citation for case: Gray v. Maryland">118 S.Ct. 1151</a></span></extracted-citation>, <extracted-citation case-ids="11503401" index="92" url="https://cite.case.law/us/523/185/#p195"><span class="citation" data-id="9433593"><a href="/opinion/118184/gray-v-maryland/" aria-description="Citation for case: Gray v. Maryland">140 L.Ed.2d 294</a></span></extracted-citation> (1998) ; <em>Richardson v. Marsh</em> , <extracted-citation case-ids="6212712" index="93" url="https://cite.case.law/us/481/200/#p208"><span class="citation" data-id="9430922"><a href="/opinion/111865/richardson-v-marsh/" aria-description="Citation for case: Richardson v. Marsh">481 U.S. 200</a></span></extracted-citation>, 208-09, <extracted-citation case-ids="6212712" index="94" url="https://cite.case.law/us/481/200/#p208"><span class="citation" data-id="9430922"><a href="/opinion/111865/richardson-v-marsh/" aria-description="Citation for case: Richardson v. Marsh">107 S.Ct. 1702</a></span></extracted-citation>, <extracted-citation case-ids="6212712" index="95" url="https://cite.case.law/us/481/200/#p208"><span class="citation" data-id="9430922"><a href="/opinion/111865/richardson-v-marsh/" aria-description="Citation for case: Richardson v. Marsh">95 L.Ed.2d 176</a></span></extracted-citation> (1987).</p>
<p id="p-91">We have consistently held that the introduction of a co-defendant's confession with the defendant's name replaced by a neutral noun or pronoun does not violate <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> . <em>See, e.g.</em> , <em>United States v. Jass</em> , <extracted-citation case-ids="3660376" index="96" url="https://cite.case.law/f3d/569/47/#p58"><span class="citation" data-id="2507"><a href="/opinion/2507/united-states-v-jass/" aria-description="Citation for case: United States v. Jass">569 F.3d 47</a></span></extracted-citation>, 58 (2d Cir. 2009) (noting that operative questions when evaluating <em>Bruton</em> claim are "(1) did the redacted statement give any indication to the jury that the original statement contained actual names, and (2) did the statement standing alone otherwise connect co-defendants to the crimes" (internal quotation marks and ellipsis omitted)). In <em>United States v. Tutino</em> , <extracted-citation case-ids="10535824" index="97" url="https://cite.case.law/f2d/883/1125/"><span class="citation" data-id="8972330"><a href="/opinion/8980459/united-states-v-tutino/" aria-description="Citation for case: United States v. Tutino">883 F.2d 1125</a></span></extracted-citation> (2d Cir. 1989), for example, we affirmed a conviction based in part on a co-defendant's statement that was redacted to reference "others," "other people," and "another person." <em><extracted-citation case-ids="10535824" index="98" url="https://cite.case.law/f2d/883/1125/"><span class="citation" data-id="8972330"><a href="/opinion/8980459/united-states-v-tutino/" aria-description="Citation for case: United States v. Tutino">Id.</a></span></extracted-citation></em><extracted-citation case-ids="10535824" index="98" url="https://cite.case.law/f2d/883/1125/"> at 1135</extracted-citation>.</p>
<p id="p-92">To determine whether a redaction is sufficient under <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> , we view the redacted statement separate and apart from any other evidence admitted at trial. <em><extracted-citation case-ids="10535824" index="99" url="https://cite.case.law/f2d/883/1125/"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Id.</a></span></extracted-citation></em> (citing <em>United States v. Wilkinson</em> , <extracted-citation case-ids="287351" index="100" url="https://cite.case.law/f2d/754/1427/#p1435"><span class="citation" data-id="8927971"><a href="/opinion/8937596/united-states-v-wilkinson/" aria-description="Citation for case: United States v. Wilkinson">754 F.2d 1427</a></span></extracted-citation>, 1435 (2d Cir. 1985) ); <em>see also</em> <em>United States v. Williams</em> , <extracted-citation case-ids="10527462" index="101" url="https://cite.case.law/f2d/936/698/#p700"><span class="citation" data-id="563663"><a href="/opinion/563663/united-states-v-conrad-williams-and-wilbert-mckenzie-conrad-williams/" aria-description="Citation for case: United States v. Conrad Williams and Wilbert McKenzie...">936 F.2d 698</a></span></extracted-citation>, 700-01 (2d Cir. 1991) ("[T]he appropriate analysis to be used when applying the <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> rule requires that we view the redacted confession in isolation from the other evidence introduced at trial. If the confession, when so viewed, does not incriminate the defendant, then it may be admitted with a proper limiting instruction even though other evidence in the case indicates that the neutral pronoun is in fact a reference to the defendant.").</p>
<p id="p-93"><strong><em>B. Application</em></strong></p>
<p id="p-94">Van Praagh contends that his constitutional rights were violated by the admission of Lyle's redacted proffer and post-arrest statements. We ordinarily review evidentiary rulings for abuse of discretion; however, Van Praagh did not object to the introduction of the redacted <a class="page-label" data-citation-index="1" data-label="734" href="#p734" id="p734">*734</a>statements at trial, and so we review the admission of this evidence for plain error. <em>See</em> <em>United States v. Pierce</em> , <extracted-citation case-ids="4182445" index="102" url="https://cite.case.law/f3d/785/832/#p840"><span class="citation" data-id="8413417"><a href="/opinion/8442193/united-states-v-pierce/" aria-description="Citation for case: United States v. Pierce">785 F.3d 832</a></span></extracted-citation>, 840 (2d Cir.), <em>cert. denied</em> , --- U.S. ----, <extracted-citation case-ids="12597176,12597177,12597178,12597179,12597180,12597181,12597182" index="103" url="https://cite.case.law/s-ct/136/172/"><span class="citation multiple-matches"><a href="/c/S.Ct./136/172/">136 S.Ct. 172</a></span></extracted-citation>, <extracted-citation case-ids="12597179,12597182,12597177,12597178,12597115,12597180,12597181,12597114" index="104" url="https://cite.case.law/l-ed-2d/193/139/"><span class="citation multiple-matches"><a href="/c/L.Ed.2d/193/139/">193 L.Ed.2d 139</a></span></extracted-citation> (2015).<footnotemark>3</footnotemark></p>
<p id="p-95">The redacted statements did not violate <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> . The neutral terms "individual" and "person," which were substituted for proper names with the exception of that of a supplier-"Brendan or Brandon," Tr. 436, 534-were not so obvious as to indicate to the jury that the original statements contained actual names. This was an ongoing criminal enterprise where many people were involved and the government introduced evidence of methamphetamine dealing by several people. Thus, the substitutions alone did not necessarily identify Van Praagh. Further, Lyle's redacted statements sounded sufficiently natural. For instance, he admitted that he had "first become involved in methamphetamine" through "someone" he "knew ... from work," Tr. 517-18, and that the individual for whom he worked as a "runner" "asked him to hold something for him" in the trunk of the rental car. Tr. 435, 534. Because such statements "might actually have been said by a person admitting his own culpability in the charged conspiracy while shielding the specific identity of his confederate," they do not violate <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> . <em>Jass</em> , <extracted-citation case-ids="3660376" index="105" url="https://cite.case.law/f3d/569/47/#p58"><span class="citation" data-id="2507"><a href="/opinion/2507/united-states-v-jass/" aria-description="Citation for case: United States v. Jass">569 F.3d at 62</a></span></extracted-citation>. Nor did the redacted statements, viewed in isolation, contain any information indicating that Van Praagh was the "individual" in question, let alone information that would "immediately inculpate" him. <em><extracted-citation case-ids="3660376" index="106" url="https://cite.case.law/f3d/569/47/#p58">Id.</extracted-citation></em><extracted-citation case-ids="3660376" index="106" url="https://cite.case.law/f3d/569/47/#p58"> at 61</extracted-citation> (internal quotation marks omitted).</p>
<p id="p-96">Van Praagh relies on <em>United States v. Taylor</em> , <extracted-citation case-ids="4237500" index="107" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">745 F.3d 15</a></span></extracted-citation> (2d Cir. 2014), to support his contention that the redactions violated <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> , but <em><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Taylor</a></span></em> is distinguishable. <em><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Taylor</a></span></em> involved a <em>single</em> robbery of a drug store by four people. <em><extracted-citation case-ids="4237500" index="108" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Id.</a></span></extracted-citation></em><extracted-citation case-ids="4237500" index="108" url="https://cite.case.law/f3d/745/15/"> at 20-21</extracted-citation>. One of the four, Luana Miller, became a cooperating witness, and another, Curtis Taylor, gave post-arrest confessions. <em><extracted-citation case-ids="4237500" index="109" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Id.</a></span></extracted-citation></em> At the trial of Taylor and the two other co-defendants, the trial court admitted Taylor's post-arrest confessions but required their redaction to omit identifications of his two co-defendants. In the portions of the confessions that were admitted, Miller's name was mentioned but the names of the two co-defendants were replaced with "two other individuals," "the person," and "the driver." <em><extracted-citation case-ids="4237500" index="110" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Id.</a></span></extracted-citation></em><extracted-citation case-ids="4237500" index="110" url="https://cite.case.law/f3d/745/15/"> at 29</extracted-citation>. We determined that in this circumstance the redactions were so obvious as to violate <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> . Our reasoning was as follows. First, Miller's name was used throughout and, "[i]f Taylor had been trying to avoid naming his confederates, he would not have identified one of them-Miller-in the very phrase in which the names of the other confederates are omitted." <em><extracted-citation case-ids="4237500" index="111" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Id.</a></span></extracted-citation></em> Second, the wording of the redacted statements, <em>i.e.</em> , "[t]he robbery was the idea of the person who waited with Luana Miller and Taylor at the gas station," was stilted and unnatural. <em><extracted-citation case-ids="4237500" index="112" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Id.</a></span></extracted-citation></em> Third, in this context, the "reference to 'two other individuals' [was] suspiciously closer to the speech of a prosecutor than that of a perpetrator." <em><extracted-citation case-ids="4237500" index="113" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Id.</a></span></extracted-citation></em> On the basis of these factors, we determined that it was obvious that names had been omitted from the statements and, therefore, "the choice of implied identity [was] narrow. The unnamed persons correspond[ed] by number (two) and by role to the pair of co-defendants ... [and] [t]he jury could immediately <a class="page-label" data-citation-index="1" data-label="735" href="#p735" id="p735">*735</a>infer, on the evidence of the redacted confession alone, that Taylor had likely named the co-defendants." <em><extracted-citation case-ids="4237500" index="114" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Id.</a></span></extracted-citation></em></p>
<p id="p-97">This case is unlike <em><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Taylor</a></span></em> . First, Lyle's statements referred to <em>multiple</em> people-not only one unnamed person to correspond to the one co-defendant, Van Praagh. This did not present the necessary process-of-elimination problem that left the jury's "choice of implied identity narrow" as in <em><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Taylor</a></span></em> . <em><extracted-citation case-ids="4237500" index="115" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Id.</a></span></extracted-citation></em> Second, in addition to Van Praagh's methamphetamine dealing, the government introduced evidence of methamphetamine dealing by its two cooperating witnesses-Tarantino and Hodges-as well as several others. Because Lyle's statements did not reference by name those cooperating witnesses, the jury could reasonably have inferred that <em>they</em> were the "other persons" Lyle was referring to in his redacted statements. Third, Lyle's statements referred to people involved in a conspiracy to engage in <em>ongoing</em> criminal conduct, not a single criminal act like in <em><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Taylor</a></span></em> . For all of these reasons, <em><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/" aria-description="Citation for case: United States v. Taylor">Taylor</a></span></em> is inapposite.</p>
<p id="p-98">We also note that the district court here gave a limiting instruction. <em>See</em> <em>Taylor</em> , <extracted-citation case-ids="4237500" index="116" url="https://cite.case.law/f3d/745/15/"><span class="citation" data-id="2655399"><a href="/opinion/2655399/united-states-v-taylor/#28" aria-description="Citation for case: United States v. Taylor">745 F.3d at 28</a></span></extracted-citation> ("It matters that the district court gave limiting instructions" because "[w]e normally assume that jurors follow limiting instructions"). The district court specifically instructed the jury that "Lyle's statement about his own conduct may not be considered or discussed by you with regard to Mr. Van Praagh." Tr. 713.</p>
<p id="p-99">Finally, Van Praagh's constitutional rights were not violated by Lyle's counsel eliciting testimony on cross-examination that his client's statements had been redacted for presentation at trial and that his client had indeed provided actual names in his proffer and post-arrest statements. Again, because Van Praagh did not object during Lyle's attorney's cross-examination, we review for plain error. In urging error, Van Praagh relies on <em>Gray v. Maryland</em> , <extracted-citation case-ids="11503401" index="117" url="https://cite.case.law/us/523/185/#p195"><span class="citation" data-id="9433593"><a href="/opinion/118184/gray-v-maryland/" aria-description="Citation for case: Gray v. Maryland">523 U.S. 185</a></span></extracted-citation>, <extracted-citation case-ids="11503401" index="118" url="https://cite.case.law/us/523/185/#p195"><span class="citation" data-id="9433593"><a href="/opinion/118184/gray-v-maryland/" aria-description="Citation for case: Gray v. Maryland">118 S.Ct. 1151</a></span></extracted-citation>, <extracted-citation case-ids="11503401" index="119" url="https://cite.case.law/us/523/185/#p195"><span class="citation" data-id="9433593"><a href="/opinion/118184/gray-v-maryland/" aria-description="Citation for case: Gray v. Maryland">140 L.Ed.2d 294</a></span></extracted-citation> (holding that "considered as a class, redactions that ... notify the jury that a name has been deleted" violated the Confrontation Clause). But <em><span class="citation" data-id="9433593"><a href="/opinion/118184/gray-v-maryland/" aria-description="Citation for case: Gray v. Maryland">Gray</a></span></em> 's focus was on the inadequacy of the government's redaction. Van Praagh can point to no case plainly identifying <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> error when a defendant, whose post-arrest statements are being offered against him, elicits the fact of redaction, or elicits parts of the redacted statement.</p>
<p id="p-100">Van Praagh fails to show plain error here. First, his case is distinguishable from <em><span class="citation" data-id="9433593"><a href="/opinion/118184/gray-v-maryland/" aria-description="Citation for case: Gray v. Maryland">Gray</a></span></em> in that there the redaction inadequacy was attributable to the prosecution. In any event, Van Praagh cannot satisfy the prejudice prong of plain error because in his case the redacted statements referred to multiple "individuals," which means the revelation could not have been immediately inculpatory. <em>See</em> <em>Jass</em> , <span class="citation" data-id="2507"><a href="/opinion/2507/united-states-v-jass/#61" aria-description="Citation for case: United States v. Jass">569 F.3d at 61</a></span>.</p>
<p id="p-101">Further, during cross-examination, Lyle's attorney elicited from the same witness several of the names that Lyle mentioned during his post-arrest and proffer statements, including "Zaron," "Ted," "Bob," and "Joe." Tr. 525. In our view, that testimony made it <em>less</em> , not more, obvious to the jury that Lyle had also mentioned Van Praagh. Van Praagh's name was not mentioned at all, and Lyle's counsel's elicitation of other names suggested that the "other persons" mentioned were the individuals whose names Lyle's counsel elicited, not Van Praagh. For all of these reasons, the admission of Lyle's redacted statements was not plainly erroneous.</p>
<p id="p-102"><strong>IV. <em>Admissibility of Lyle's New Jersey Arrest</em></strong></p>
<p id="p-103">We review a district court's evidentiary rulings for abuse of discretion, which we will find only if the district court "acted arbitrarily and irrationally."</p>
<p id="p-104"><a class="page-label" data-citation-index="1" data-label="736" href="#p736" id="p736">*736</a><em>United States v. Greer</em> , <extracted-citation case-ids="4085145" index="120" url="https://cite.case.law/f3d/631/608/#p614"><span class="citation" data-id="184262"><a href="/opinion/184262/united-states-v-greer/" aria-description="Citation for case: United States v. Greer">631 F.3d 608</a></span></extracted-citation>, 614 (2d Cir. 2011) (quoting <em>United States v. Garcia</em> , <extracted-citation case-ids="9429305" index="121" url="https://cite.case.law/f3d/291/127/#p136"><span class="citation" data-id="777745"><a href="/opinion/777745/united-states-v-carlos-garcia/" aria-description="Citation for case: United States v. Carlos Garcia">291 F.3d 127</a></span></extracted-citation>, 136 (2d Cir. 2002) ).</p>
<p id="p-105"><strong><em>A. Applicable Law</em></strong></p>
<p id="p-106">Federal Rule of Evidence 404(b) provides:</p>
<blockquote id="p-107">Evidence of a crime, wrong, or other act is not admissible to prove a person's character in order to show that on a particular occasion the person acted in accordance with the character.</blockquote>
<p id="p-108">Fed. R. Evid. 404(b). "The Second Circuit's 'inclusionary rule' allows the admission of such evidence 'for any purpose other than to show a defendant's criminal propensity, as long as the evidence is relevant and satisfies the probative-prejudice balancing test of Rule 403 of the Federal Rules of Evidence.' " <em>Greer</em> , <extracted-citation case-ids="4085145" index="122" url="https://cite.case.law/f3d/631/608/#p614"><span class="citation" data-id="184262"><a href="/opinion/184262/united-states-v-greer/" aria-description="Citation for case: United States v. Greer">631 F.3d at 614</a></span></extracted-citation> (quoting <em>United States v. Inserra</em> , <extracted-citation case-ids="10522168" index="123" url="https://cite.case.law/f3d/34/83/#p89"><span class="citation" data-id="9487269"><a href="/opinion/677324/united-states-v-george-a-inserra-john-inserra-and-john-giura-dennis/" aria-description="Citation for case: United States v. George A. Inserra John Inserra and John...">34 F.3d 83</a></span></extracted-citation>, 89 (2d Cir. 1994) ).</p>
<p id="p-109">Not all evidence of uncharged misconduct, however, is prohibited by Rule 404(b). Rather,</p>
<blockquote id="p-110">[E]vidence of uncharged criminal activity is not considered other crimes evidence ... if it arose out of the same transaction or series of transactions as the charged offense, if it is inextricably intertwined with the evidence regarding the charged offense, or if it is necessary to complete the story of the crime on trial.</blockquote>
<p id="p-111"><em>United States v. Carboni</em> , <extracted-citation case-ids="11467212" index="124" url="https://cite.case.law/f3d/204/39/#p44"><span class="citation" data-id="767698"><a href="/opinion/767698/united-states-v-harry-r-carboni/" aria-description="Citation for case: United States v. Harry R. Carboni">204 F.3d 39</a></span></extracted-citation>, 44 (2d Cir. 2000) (internal quotation marks omitted); <em>see also</em> <em>Inserra</em> , <extracted-citation case-ids="10522168" index="125" url="https://cite.case.law/f3d/34/83/#p89"><span class="citation" data-id="9487269"><a href="/opinion/677324/united-states-v-george-a-inserra-john-inserra-and-john-giura-dennis/#89" aria-description="Citation for case: United States v. George A. Inserra John Inserra and John...">34 F.3d at 89</a></span></extracted-citation> ("[E]vidence of other bad acts may be admitted to provide the jury with the complete story of the crimes charged by demonstrating the context of certain events relevant to the charged offense.").</p>
<p id="p-112"><strong><em>B. Application</em></strong></p>
<p id="p-113">The district court did not abuse its discretion in admitting the evidence seized during the New Jersey arrest in January 2014. First, that evidence was not barred by Rule 404(b) because the arrest "arose out of the same transaction or series of transactions as the charged offense." <em>Carboni</em> , <extracted-citation case-ids="11467212" index="126" url="https://cite.case.law/f3d/204/39/#p44"><span class="citation" data-id="767698"><a href="/opinion/767698/united-states-v-harry-r-carboni/" aria-description="Citation for case: United States v. Harry R. Carboni">204 F.3d at 44</a></span></extracted-citation>. Specifically, as discussed above, Lyle argued at trial that he was only a methamphetamine user-not a dealer. The government rebutted that argument with evidence of Lyle's New Jersey arrest. In summation, the government argued:</p>
<blockquote id="p-114">14 or 15 grams [of methamphetamine] is still many hundreds, if not thousands, of dollars of meth.... Also, you know what else was in that room? A dozen baggies, a scale, $3,000 in cash. He was not weighing out meth for his own personal use. That was meth he was going to sell.</blockquote>
<p id="p-115">Tr. 629. In other words, the evidence seized pursuant to the New Jersey arrest was not evidence of <em>other</em> crimes; it was evidence of the very crime charged in count one of the indictment, a conspiracy involving Lyle, Van Praagh, and others to distribute methamphetamine from in or about December 2012 through in or about January 2014. Accordingly, evidence of the New Jersey arrest was admissible as direct proof of the methamphetamine distribution conspiracy.</p>
<p id="p-116">Second, and in any event, the evidence of the New Jersey arrest fits within the Rule 404(b) inclusionary rule because it shows Lyle's knowledge and intent regarding the contents of the rental car. Because Lyle argued throughout trial that he did not know what was in the trunk of the rental car, his knowledge and intent were at issue. <em>United States v. Ramirez</em> , <extracted-citation case-ids="10534202" index="127" url="https://cite.case.law/f2d/894/565/#p568"><span class="citation" data-id="535595"><a href="/opinion/535595/united-states-v-john-alonso-ramirez-and-zeir-marulanda/" aria-description="Citation for case: United States v. John Alonso Ramirez, and Zeir Marulanda">894 F.2d 565</a></span></extracted-citation>, 568 (2d Cir. 1990) ("When the defendant disavows awareness that a crime was being perpetrated, and the government bears the burden of proving the defendant's knowing possession as an element of the crime, knowledge is properly put in issue."). The fact that Lyle was in possession of 14-15 grams of methamphetamine <a class="page-label" data-citation-index="1" data-label="737" href="#p737" id="p737">*737</a>and tools of the drug trade less than a month after he was arrested with the rental car is probative of his knowledge and intent regarding the contents of the rental car. In addition, the probative value of this evidence was not "substantially outweighed" by the risk of unfair prejudice as it "did not involve conduct any more sensational or disturbing than the crimes with which [Lyle was] charged." <em>United States v. Pitre</em> , <extracted-citation case-ids="10524117" index="128" url="https://cite.case.law/f2d/960/1112/#p1120"><span class="citation" data-id="580870"><a href="/opinion/580870/united-states-v-joseph-pitre-edwyn-pitre-angel-m-otero-richard-pitre/" aria-description="Citation for case: United States v. Joseph Pitre Edwyn Pitre Angel M. Otero...">960 F.2d 1112</a></span></extracted-citation>, 1120 (2d Cir. 1992) (quoting <em>United States v. Roldan-Zapata</em> , <extracted-citation case-ids="10537862" index="129" url="https://cite.case.law/f2d/916/795/#p804"><span class="citation" data-id="550091"><a href="/opinion/550091/united-states-v-oscar-roldan-zapata-and-pedro-osario-serna/" aria-description="Citation for case: United States v. Oscar Roldan-Zapata and Pedro Osario-Serna">916 F.2d 795</a></span></extracted-citation>, 804 (2d Cir. 1990) ). Accordingly, the district court acted well within its discretion in finding that the probative value of the evidence outweighed the threat of unfair prejudice.</p>
<p id="p-117"><strong>V. <em>Sufficiency of the Conspiracy Evidence</em></strong></p>
<p id="p-118">We review Van Praagh's challenge to whether the evidence was sufficient to support his conspiracy conviction <em>de novo</em> , "view[ing] the evidence in the light most favorable to the government, crediting every inference that could have been drawn in the government's favor, and deferring to the jury's assessment of witness credibility and its assessment of the weight of the evidence." <em>Rosemond</em> , <extracted-citation case-ids="12173717" index="130" url="https://cite.case.law/f3d/841/95/#p99"><span class="citation" data-id="8414347"><a href="/opinion/8443021/united-states-v-rosemond/" aria-description="Citation for case: United States v. Rosemond">841 F.3d at 113</a></span></extracted-citation> (quoting <em>United States v. Coplan</em> , <extracted-citation case-ids="3649269" index="131" url="https://cite.case.law/f3d/703/46/#p62"><span class="citation" data-id="9501731"><a href="/opinion/812765/united-states-v-coplan/" aria-description="Citation for case: United States v. Coplan">703 F.3d 46</a></span></extracted-citation>, 62 (2d Cir. 2012) ). We must affirm if "<em>any</em> rational trier of fact could have found the essential elements of the crime beyond a reasonable doubt." <em><extracted-citation case-ids="3649269" index="132" url="https://cite.case.law/f3d/703/46/#p62"><span class="citation" data-id="9501731"><a href="/opinion/812765/united-states-v-coplan/" aria-description="Citation for case: United States v. Coplan">Id.</a></span></extracted-citation></em> (quoting <em>United States v. Vernace</em> , <extracted-citation case-ids="4082128" index="133" url="https://cite.case.law/f3d/811/609/#p615"><span class="citation" data-id="8413796"><a href="/opinion/8442529/united-states-v-vernace/" aria-description="Citation for case: United States v. Vernace">811 F.3d 609</a></span></extracted-citation>, 615 (2d Cir. 2016) ).</p>
<p id="p-119">The crux of a conspiracy is an agreement between two or more persons to join together to accomplish something illegal. <em>United States v. Parker</em> , <extracted-citation case-ids="3684820" index="134" url="https://cite.case.law/f3d/554/230/#p234"><span class="citation" data-id="1278099"><a href="/opinion/1278099/united-states-v-parker/" aria-description="Citation for case: United States v. Parker">554 F.3d 230</a></span></extracted-citation>, 234 (2d Cir. 2009) ("To prove a conspiracy, the evidence must show that 'two or more persons agreed to participate in a joint venture intended to commit an unlawful act.' " (quoting <em>United States v. Desimone</em> , <extracted-citation case-ids="199978" index="135" url="https://cite.case.law/f3d/119/217/#p223"><span class="citation" data-id="6951731"><a href="/opinion/7048410/united-states-v-desimone/" aria-description="Citation for case: United States v. Desimone">119 F.3d 217</a></span></extracted-citation>, 223 (2d Cir. 1997) )). We have recognized a "narrow exception" to the conspiracy rule for a transaction between a buyer and seller of drugs. <em><extracted-citation case-ids="199978" index="136" url="https://cite.case.law/f3d/119/217/#p223"><span class="citation" data-id="6951731"><a href="/opinion/7048410/united-states-v-desimone/" aria-description="Citation for case: United States v. Desimone">Id.</a></span></extracted-citation></em> Under this exception, "the existence of a buyer-seller relationship does not <em>itself</em> establish a conspiracy; however, where there is additional evidence showing an agreement to join together to accomplish an objective beyond the sale transaction, the evidence may support a finding that the parties intentionally participated in a conspiracy." <em>United States v. Hawkins</em> , <extracted-citation case-ids="6050917" index="137" url="https://cite.case.law/f3d/547/66/#p72"><span class="citation" data-id="1225840"><a href="/opinion/1225840/united-states-v-hawkins/" aria-description="Citation for case: United States v. Hawkins">547 F.3d 66</a></span></extracted-citation>, 72 (2d Cir. 2008) ; <em>see also</em> <em>United States v. Rojas</em> , <extracted-citation case-ids="3771399" index="138" url="https://cite.case.law/f3d/617/669/#p674"><span class="citation" data-id="152881"><a href="/opinion/152881/united-states-v-rojas/" aria-description="Citation for case: United States v. Rojas">617 F.3d 669</a></span></extracted-citation>, 674 (2d Cir. 2010) ("[T]he exception does not protect either the seller or buyer from a charge that they conspired together to transfer drugs if the evidence supports a finding that they shared a conspiratorial purpose to advance other transfers, whether by the seller or by the buyer." (alteration and internal quotation marks omitted)). The question thus becomes "whether the evidence in its totality suffices to permit a jury to find beyond a reasonable doubt that the defendant was not merely a buyer or seller of narcotics, but rather that the defendant knowingly and intentionally participated in the narcotics-distribution conspiracy by agreeing to accomplish its illegal objective beyond the mere purchase or sale." <em>Hawkins</em> , <extracted-citation case-ids="6050917" index="139" url="https://cite.case.law/f3d/547/66/#p72"><span class="citation" data-id="1225840"><a href="/opinion/1225840/united-states-v-hawkins/" aria-description="Citation for case: United States v. Hawkins">547 F.3d at 73</a></span>-74</extracted-citation>.</p>
<p id="p-120">Van Praagh did not request a buyer-seller instruction at trial and so we review for plain error. <em>Pierce</em> , <extracted-citation case-ids="4182445" index="140" url="https://cite.case.law/f3d/785/832/#p840"><span class="citation" data-id="8413417"><a href="/opinion/8442193/united-states-v-pierce/" aria-description="Citation for case: United States v. Pierce">785 F.3d at 840</a></span></extracted-citation>. The district court did not plainly err in failing to give a buyer-seller instruction because the government presented ample evidence of a narcotics conspiracy beyond a buyer-seller relationship between Van Praagh and Lyle.</p>
<p id="p-121">First, Van Praagh sold methamphetamine not just to Lyle, but to others. Indeed, he received weekly shipments of methamphetamine, which he then sold to others. With assistance from Tarantino, he <a class="page-label" data-citation-index="1" data-label="738" href="#p738" id="p738">*738</a>regularly sold methamphetamine out of his apartment in Queens as well as out of hotels, and he made deliveries to "[p]robably 50" customers. Tr. 124.</p>
<p id="p-122">Second, the quantity of drugs was consistent with a drug trafficking operation. Tarantino testified that Lyle repeatedly purchased pound-level quantities of methamphetamine at $19,000 to $25,000 per pound. <em>See</em> <em>United States v. Contreras</em> , <extracted-citation case-ids="11099115" index="141" url="https://cite.case.law/f3d/249/595/#p600"><span class="citation" data-id="773155"><a href="/opinion/773155/united-states-v-eliseo-contreras/" aria-description="Citation for case: United States v. Eliseo Contreras">249 F.3d 595</a></span></extracted-citation>, 600 (7th Cir. 2001) (noting that repeat sales suggest "more than a transient relationship," but are "by themselves" insufficient to support an inference of a conspiracy between the supplier and purchaser); <em>see also</em> <em>United States v. Murray</em> , <extracted-citation case-ids="1380727" index="142" url="https://cite.case.law/f2d/618/892/#p902"><span class="citation" data-id="376822"><a href="/opinion/376822/united-states-v-dale-murray-paul-leahey-ronald-vanderbosch-lawrence/" aria-description="Citation for case: United States v. Dale Murray, Paul Leahey, Ronald...">618 F.2d 892</a></span></extracted-citation>, 902 (2d Cir. 1980) ("[O]ne who deals in large quantities of narcotics may be presumed to know that he is a part of a venture which extends beyond his individual participation." (quoting <em>United States v. Magnano</em> , <extracted-citation case-ids="1024903" index="143" url="https://cite.case.law/f2d/543/431/#p433"><span class="citation" data-id="339842"><a href="/opinion/339842/united-states-v-joseph-magnano-aka-joe-the-grind/" aria-description="Citation for case: United States v. Joseph Magnano, A/K/A &quot;Joe the Grind&quot;">543 F.2d 431</a></span></extracted-citation>, 433-34 (2d Cir. 1976) )).</p>
<p id="p-123">Accordingly, the district court did not plainly err in failing to <em>sua sponte</em> give a buyer-seller instruction. <em>See</em> <em>United States v. Medina</em> , <extracted-citation case-ids="10521074" index="144" url="https://cite.case.law/f2d/944/60/#p65"><span class="citation" data-id="567926"><a href="/opinion/567926/united-states-v-luz-medina-silverio-polanco-franklin-marmolejo-juan-a/" aria-description="Citation for case: United States v. Luz Medina, Silverio Polanco, Franklin...">944 F.2d 60</a></span></extracted-citation>, 65-66 (2d Cir. 1991) (holding that the district court was not required to give a buyer-seller instruction "where ... there is advanced planning among the alleged co-conspirators to deal in wholesale quantities of drugs obviously not intended for personal use" because "[u]nder such circumstances, the participants in the transaction may be presumed to know that they are part of a broader conspiracy").</p>
<p id="p-124"><strong>VI. <em>Reasonableness of Van Praagh's Sentence</em></strong></p>
<p id="p-125">We review the substantive reasonableness of a sentence under a "deferential abuse-of-discretion standard." <em>United States v. Aldeen</em> , <extracted-citation case-ids="4275829" index="145" url="https://cite.case.law/f3d/792/247/#p251"><span class="citation" data-id="8413509"><a href="/opinion/8442268/united-states-v-aldeen/" aria-description="Citation for case: United States v. Aldeen">792 F.3d 247</a></span></extracted-citation>, 251 (2d Cir. 2015) (quoting <em>Gall v. United States</em> , <extracted-citation case-ids="3675664" index="146" url="https://cite.case.law/us/552/38/#p41"><span class="citation" data-id="9435287"><a href="/opinion/145843/gall-v-united-states/" aria-description="Citation for case: Gall v. United States">552 U.S. 38</a></span></extracted-citation>, 41, <extracted-citation case-ids="3675664" index="147" url="https://cite.case.law/us/552/38/#p41"><span class="citation" data-id="9435287"><a href="/opinion/145843/gall-v-united-states/" aria-description="Citation for case: Gall v. United States">128 S.Ct. 586</a></span></extracted-citation>, <extracted-citation case-ids="3675664" index="148" url="https://cite.case.law/us/552/38/#p41"><span class="citation" data-id="9435287"><a href="/opinion/145843/gall-v-united-states/" aria-description="Citation for case: Gall v. United States">169 L.Ed.2d 445</a></span></extracted-citation> (2007) ). The question is whether Van Praagh's below-Guidelines sentence of 144 months' imprisonment "shock[s] the conscience," constitutes a "manifest injustice," or is otherwise substantively unreasonable. <em><span class="citation" data-id="9435287"><a href="/opinion/145843/gall-v-united-states/" aria-description="Citation for case: Gall v. United States">Id.</a></span></em> at 255 (quoting <em>United States v. Rigas</em> , <extracted-citation case-ids="5756241" index="149" url="https://cite.case.law/f3d/583/108/#p123"><span class="citation" data-id="2467"><a href="/opinion/2467/united-states-v-rigas/" aria-description="Citation for case: United States v. Rigas">583 F.3d 108</a></span></extracted-citation>, 123 (2d Cir. 2009) ); <em>see also</em> <em>United States v. Perez-Frias</em> , <extracted-citation case-ids="4103975" index="150" url="https://cite.case.law/f3d/636/39/#p43"><span class="citation" data-id="213681"><a href="/opinion/213681/united-states-v-perez-frias/" aria-description="Citation for case: United States v. Perez-Frias">636 F.3d 39</a></span></extracted-citation>, 43 (2d Cir. 2011) (per curiam) ("[I]n the overwhelming majority of cases, a Guidelines sentence will fall comfortably within the broad range of sentences that would be reasonable in the particular circumstances. It is therefore difficult to find that a below-Guidelines sentence is unreasonable." (internal quotation marks and citation omitted)).</p>
<p id="p-126">Van Praagh's below-Guidelines sentence of 144 months was substantively reasonable. The district court fully explained its reasoning. It considered Van Praagh's "very unhappy upbringing," and the "very positive change" that Van Praagh "seem[ed] to be undergoing." Van Praagh App. 58-59. The district court determined, however, that a 144-month sentence was sufficient but not greater than necessary because Van Praagh (1) had committed a "very serious" crime; (2) had a "long history of drug dealing" and "plenty of opportunities to change"; (3) clearly had been "in charge of dealing more drugs at a higher level than [Lyle]"; and (4) had a "prior record suggest[ing] that he still continues to be a danger to the community." <em><extracted-citation case-ids="4103975" index="151" url="https://cite.case.law/f3d/636/39/#p43"><span class="citation" data-id="213681"><a href="/opinion/213681/united-states-v-perez-frias/" aria-description="Citation for case: United States v. Perez-Frias">Id.</a></span></extracted-citation></em></p>
<p id="p-127">Van Praagh's argument that, like Lyle, he should have been sentenced to the statutory mandatory minimum of 120 months' imprisonment is unavailing. As the district court noted, Van Praagh had a "more important role" than Lyle. <em>See</em> Van Praagh App. 62. Van Praagh supplied Lyle with pound quantities of methamphetamine on multiple occasions. Van Praagh had people working for him to make drug deliveries. Moreover, Van Praagh's criminal history was clearly more serious than Lyle's. Although <a class="page-label" data-citation-index="1" data-label="739" href="#p739" id="p739">*739</a>neither man had previously served any jail time for his crimes, Van Praagh's previous convictions included crimes relating to methamphetamine, while Lyle had only a violation for marijuana possession twenty years prior to the instant offense conduct. In these circumstances, we identify no abuse of the district court's sentencing discretion and no merit in Van Praagh's claim that his sentence is substantively unreasonable.</p>
<p id="p-128"><strong><em>CONCLUSION</em></strong></p>
<p id="p-129">To summarize, we conclude as follows:</p>
<blockquote id="p-130">1. Because Lyle was an unlicensed, as well as unauthorized, driver of the rental car, he had no reasonable expectation of privacy in that car, and the district court did not err in denying his motion to suppress. Even assuming Lyle had a legitimate privacy interest, the search and seizure of the rental car did not violate the Fourth Amendment.</blockquote>
<blockquote id="p-131">2. Lyle's counsel's statement in his opening argument that "we dispute [ ] the idea that [Lyle] was a dealer," Tr. 28, triggered the waiver in Lyle's proffer agreement, and the proffer statements, taken together, fairly rebutted his counsel's argument that Lyle was a mere user of methamphetamine and not a dealer.</blockquote>
<blockquote id="p-132">3. The admission of Lyle's redacted proffer and post-arrest statements in the defendants' joint trial was not plainly erroneous because the statements substituted neutral terms for actual names and had no otherwise identifying information. Further, the district court did not plainly err in allowing Lyle's counsel, without Van Praagh's objection, to elicit testimony that Lyle's statements had been redacted, that Lyle had provided actual names in his proffer and post-arrest statements, and what several of those names were because those disclosures did not prejudice Van Praagh and, indeed, made it <em>less</em> obvious to the jury that Lyle was referring to Van Praagh in his statements.</blockquote>
<blockquote id="p-133">4. The district court did not abuse its discretion in admitting the evidence seized during Lyle's New Jersey arrest because (a) it was direct evidence of the conspiracy charged in count one of the superseding indictment, and (b) even if it was not direct evidence, it was not "other crimes evidence" prohibited by Federal Rule of Evidence 404(b) because it showed Lyle's knowledge and intent regarding the contents of the rental car on December 11, 2013.</blockquote>
<blockquote id="p-134">5. The district court did not plainly err in failing to <em>sua sponte</em> give a buyer-seller instruction to the jury because the government presented ample evidence of a narcotics conspiracy.</blockquote>
<blockquote id="p-135">6. Van Praagh's below-Guidelines sentence of 144 months' imprisonment was substantively reasonable.</blockquote>
<p id="p-136">Accordingly, the judgments of the district court are <strong>AFFIRMED</strong> .</p>
<footnote label="1">
<p id="p-139">Lyle identified this individual as Van Praagh, but at trial, "individual" was substituted for Van Praagh's name pursuant to <em>Bruton v. United States</em> , <extracted-citation case-ids="1767670" index="152" url="https://cite.case.law/us/391/123/#p135"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">391 U.S. 123</a></span></extracted-citation>, <extracted-citation case-ids="1767670" index="153" url="https://cite.case.law/us/391/123/#p135"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">88 S.Ct. 1620</a></span></extracted-citation>, <extracted-citation case-ids="1767670" index="154" url="https://cite.case.law/us/391/123/#p135"><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">20 L.Ed.2d 476</a></span></extracted-citation> (1968).</p>
</footnote>
<footnote label="2">
<p id="p-140">Some courts have concluded that there are two inquiries: first, whether the impoundment of a car is reasonable; and second, if so, whether the subsequent search of the car after the impoundment is reasonable. <em>See, e.g.,</em> <em>Duguay</em> , <extracted-citation case-ids="7630921" index="155" url="https://cite.case.law/f3d/93/346/#p351"><span class="citation" data-id="9489468"><a href="/opinion/724910/united-states-v-christopher-duguay/#351" aria-description="Citation for case: United States v. Christopher Duguay">93 F.3d at 351</a></span></extracted-citation> ("[T]he decision to impound (the 'seizure') is properly analyzed as distinct from the decision to inventory (the 'search')."); <em>Coccia</em> , <extracted-citation case-ids="2843114" index="156" url="https://cite.case.law/f3d/446/233/#p239">446 F.3d at </extracted-citation>237 n. 5 (same). Here, Lyle has challenged only the impoundment and not the subsequent search of the rental vehicle. Hence, we need not reach the second inquiry.</p>
</footnote>
<footnote label="3">
<p id="p-141">Van Praagh contends that his <em><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></em> argument was preserved by his counsel's objection to the admission of Lyle's unredacted statements and by Lyle's counsel's objection to the redacted statements. Admission of unredacted statements, however, is a different and independent issue, and Van Praagh cites no authority suggesting that one party's counsel may preserve another party's claim of error when the other party's counsel fails timely to join in the objection. Accordingly, plain error review applies.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Maez.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Maez
type: case
citation: "872 F.2d 1444 (1989)"
parallel_cite: ""
neutral_cite: "1989 U.S. App. LEXIS 5092; 1989 WL 36532"
court: "U.S. Court of Appeals, 10th Cir."
court_level: coa
circuit: ca10
year: 1989
date_decided: 1989-04-19
docket: 88-1128
authority_weight: "Binding in-circuit — 10th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/521939/united-states-v-arthur-maez/"
  cluster_id: 521939
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Maez
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Entry to Arrest]]"
    role: "Key — constructive-entry (10th Cir. recognizing side: SWAT loudspeaker order = warrantless in-home arrest, 872 F.2d at 1451)"
  - page: "[[Arrest in the Home]]"
    role: "Related — constructive-entry cross-ref"
related:
  - "[[Entry to Arrest]]"
  - "[[Arrest in the Home]]"
  - "[[Payton v. New York]]"
  - "[[Seizure of the Person]]"
  - "[[The Exclusionary Rule]]"
tags:
  - case
  - fourth-amendment
  - arrest-in-the-home
  - payton
  - constructive-entry
  - warrantless-arrest
  - show-of-force
  - tenth-circuit
holding: "The Tenth Circuit held that police effected an unlawful warrantless arrest in the home in violation of Payton v. New York when, without an arrest warrant, a SWAT team surrounded Maez's mobile home and ordered the occupants out over loudspeakers, coercing him from the home into custody — physical entry across the threshold is not required, because such a show of force that makes a suspect come out under coercion is a Payton violation — so the evidence obtained after the tainted arrest required suppression, and the court reversed."
---

# United States v. Maez

*872 F.2d 1444 (10th Cir. 1989)* (No. 88-1128) · U.S. Court of Appeals for the Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 521939 → majority opinion 521939 (872 F.2d 1444, decided 1989-04-19, Holloway, C.J.); Rule quote reporter-page-verified against the CL opinion text (the court's own cross-reference to p. 1451) 2026-07-07. S9 promotes. -->

## Background
Two men robbed an Albuquerque bank in August 1987. A witness's tip led the FBI to trace a getaway truck to Arthur Maez, and officers located his mobile home — the truck parked outside — and put it under surveillance. Without obtaining an arrest warrant, Albuquerque police, the FBI, and a SWAT team planned the arrest, then arrived and surrounded the trailer, which had a single exit. SWAT members dressed in black, with rifles pointed at the home, ordered the occupants out over loudspeakers; no officer went to the door. Maez's wife watched their fifteen-year-old son — never a suspect — be handcuffed across the street, told her husband what was happening, and Maez said, "we have to go outside." He exited and was taken into custody. Maez's wife then signed consent-to-search forms, and officers seized cash, ammunition, and clothing; Maez made incriminating statements. Convicted of armed bank robbery, Maez appealed the denial of his motion to suppress.

## Issue
Whether an unlawful warrantless arrest in the home, in violation of *[[Payton v. New York]]*, occurred where armed officers and a SWAT team — having no arrest warrant — surrounded Maez's home and, over loudspeakers, ordered the occupants out, coercing Maez from the home into custody, even though no officer physically entered the trailer.

## Rule
*[[Payton v. New York|Payton]]* forbids a warrantless, non-consensual entry into the home to make a routine arrest, and that protection is not defeated by the absence of a physical threshold crossing. Following the Ninth and Sixth Circuits, the Tenth Circuit adopted the coercion rule: "Those courts have held that *Payton* is violated where there is such a show of force that a defendant comes out of a home under coercion and submits to being taken in custody." — 872 F.2d at 1451. ^pin-1451

## Application
The officers had no arrest warrant, yet they surrounded Maez's trailer with a SWAT team, trained rifles on it, handcuffed his teenage son in plain view, and ordered the occupants out over loudspeakers — an "extreme coercion" that made Maez leave the home involuntarily. Because it is the location of the arrested person, not the arresting agents, that determines whether an arrest occurs within a home, Maez was arrested inside his home without a warrant, in violation of *[[Payton v. New York|Payton]]*. The evidence and statements obtained after that tainted arrest — including the consent search Mrs. Maez signed while surrounded by officers — were fruits of the illegal arrest and should have been suppressed.

## Conclusion
**Reversed.** Chief Judge Holloway wrote for the panel (Holloway, C.J.; Brorby, Circuit Judge; and Anderson, District Judge, sitting by designation).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Maez* is a leading Tenth Circuit statement of **constructive entry** under *[[Payton v. New York|Payton]]*: police who mount a coercive show of force to draw a suspect out of his home and arrest him have made a warrantless arrest "in the home," even without crossing the threshold — the arrestee's location, not the officers', controls. Pair it with *[[Payton v. New York|Payton]]*'s firm line at the entrance to the house and with the fruit-of-the-poisonous-tree consequences for evidence and consent obtained afterward.

## Appears on
- [[Entry to Arrest]] — *Key*
- [[Arrest in the Home]] — *Related*

## Sources
- [*United States v. Maez*, 872 F.2d 1444 (10th Cir. 1989)](https://www.courtlistener.com/opinion/521939/united-states-v-arthur-maez/) — pinpoint: 1451 (the constructive-entry / show-of-force *Payton* holding; the CL majority text is paragraph-numbered, and the court's own opinion cross-references this holding to reporter page 1451). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a8431b114f94af20", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Maez"}, "payload": {"all": [{"cite": "872 F.2d 1444", "page": "1444", "reporter": "F.2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "872"}, {"cite": "1989 U.S. App. LEXIS 5092", "page": "5092", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1989"}, {"cite": "1989 WL 36532", "page": "36532", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "1989"}], "display": "872 F.2d 1444", "official": {"cite": "872 F.2d 1444", "page": "1444", "reporter": "F.2d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "872"}, "official_selection_present": true, "record_id": "United States v. Maez"}}
{"assertion_id": "6a3b970108fb4eb8", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Maez"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Maez", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Maez

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Maez",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Arthur Maez",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Arthur MAEZ, Defendant-Appellant",
    "input_case_name": "United States v. Maez",
    "court": "U.S. Court of Appeals, 10th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": "1989-04-19",
    "year": 1989,
    "docket": "88-1128",
    "cluster_id": 521939,
    "lead_opinion_id": 9478941,
    "sibling_ids": [],
    "absolute_url": "/opinion/521939/united-states-v-arthur-maez/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "872 F.2d 1444",
      "volume": "872",
      "reporter": "F.2d",
      "page": "1444",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1989 U.S. App. LEXIS 5092",
        "volume": "1989",
        "reporter": "U.S. App. LEXIS",
        "page": "5092",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 WL 36532",
        "volume": "1989",
        "reporter": "WL",
        "page": "36532",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "872 F.2d 1444",
        "volume": "872",
        "reporter": "F.2d",
        "page": "1444",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 U.S. App. LEXIS 5092",
        "volume": "1989",
        "reporter": "U.S. App. LEXIS",
        "page": "5092",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 WL 36532",
        "volume": "1989",
        "reporter": "WL",
        "page": "36532",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "872 F.2d 1444",
    "official_selection": {
      "court_class": "coa",
      "selected": "872 F.2d 1444",
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
    "date_created": "2026-07-07T13:26:52Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:27:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:27:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:27:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:27:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-maez--521939",
      "to_record_id": "United States v. Maez",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Maez

```
<opinion type="majority">
<author id="b1538-9">HOLLOWAY, Chief Judge.</author>
<p id="b1538-10">Defendant Maez (Maez) was charged with armed bank robbery, a violation of <span class="citation no-link">18 U.S.C. § 2113</span>(a) &amp; (d) (1982) and aiding and abetting, a violation of <span class="citation no-link">18 U.S.C. § 2</span> (1982). He filed a pretrial motion to suppress evidence seized during a search of his home and truck and incriminating statements he made thereafter. That motion was denied after a suppression hearing and the evidence was admitted at trial. Maez was convicted. He appeals, arguing that the motion to suppress should have been granted.</p>
<p id="b1538-11">The paramount question presented is whether a violation of <em>Payton v. New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U.S. 573</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980), occurred when a number of armed officers and a SWAT team, having no warrant for an arrest, surrounded a mobile home occupied by Maez, his wife and children, and over loud speakers asked the occupants to remove themselves from the home, which they did, Maez then being taken into custody. We hold that a violation and unlawful arrest occurred. Because evidence obtained after the arrest and admitted at trial over Maez’ objection was tainted, we reverse.</p>
<p id="b1538-15">I</p>
<p id="b1538-16">
<em>Factual Background and Procedural Posture</em>
</p>
<p id="b1538-17">A.</p>
<p id="b1538-18">
<em>The Arrest of Maez</em>
</p>
<p id="b1538-19">Two men robbed an Albuquerque bank on Friday, August 14, 1987. A bank customer reported that an early 1960’s Ford or Dodge pickup truck with a wooden tailgate and a New Mexico license plate number KO-1919 was involved in the robbery. There was no such number, but an FBI dispatcher found that license number KD-1919 belonged to a 1959 Ford pickup truck registered to Maez. A description of the truck, both robbers, and Maez’ address was given over the radio.</p>
<p id="b1538-20">Deputy Sheriff Pacheco heard the broadcast at 3:00 p.m. He knew Maez and contacted a confidential informant who knew where Maez lived. The informant directed Pacheco to the Maez’ home. At the home he saw a truck matching the description he had been given. By now it was 3:30 p.m. II R. 18-19. Pacheco left and the Albuquerque police department and FBI were contacted. The Maez home was left unguarded between approximately 3:30 and 4:30 p.m. Pacheco returned at approximately 4:30 p.m. after meeting with his supervisor. From that point on the trailer (which had only one exit — the front door) was under surveillance. The truck at the residence was later identified as the getaway truck.</p>
<p id="b1538-21">Several Albuquerque police officers, a SWAT team and the FBI met in a restau<page-number citation-index="1" label="1447">*1447</page-number>rant parking lot to plan Maez’ arrest.<footnotemark>1</footnotemark> They arrived at the Maez’ home between 6:00 and 6:30 p.m. Ill R. 106. SWAT team members dressed in black surrounded the trailer and (over loud speakers) asked the occupants of the home to come out. II R. 38-39; III R. 143. None of the officers went to the door. Mrs. Maez heard some commotion outside. When she looked out the front door she saw her fifteen year old son walking across the street with his hands in the air. She watched as he was searched and handcuffed. An FBI agent testified the boy was handcuffed; he was never a suspect in the robbery however. Ill R. 132. There were rifles pointed at the house. Ill R. 152. Mrs. Maez told her husband what was happening and he looked outside and said, “we have to go outside_” III R. 152. Mr. and Mrs. Maez were told to exit one at a time.</p>
<p id="b1539-7">B.</p>
<p id="b1539-8">
<em>Mrs. Maez’ Consents to Search</em>
</p>
<p id="A2HN">By the time Mrs. Maez had left the trailer it was approximately 6:45 p.m. II R. 49-50; III R. 75. She was escorted, with her two month old baby, outside the trailer park fence, past approximately ten police officers and into the presence of five more. Shortly thereafter, she was asked to read and sign consent forms authorizing a search of the trailer. She owned the trailer. Police officer Whitson filled in the blanks on an Albuquerque police department consent form and explained the form to Mrs. Maez before she signed it.<footnotemark>2</footnotemark> Mrs. Maez was given time to read the form.<footnotemark>3</footnotemark> No evidence was seized pursuant to this consent. II R. 44-45.</p>
<p id="b1539-10">After she had signed the Albuquerque police department consent form, Mrs. Maez was asked to sign an FBI consent to search form. Agent Guyman explained that they would be looking for money, weapons, or clothing. He told Mrs. Maez that her husband had been arrested. Guyman filled out the form and had Mrs. Maez read it out loud. Agent Marrero, who was present when the form was signed, testified that Mrs. Maez was visibly upset when she signed the form. She said that she signed the forms only because she had to. Ill R. 97, 157.<footnotemark>4</footnotemark> A bag containing $5,800, a blue stocking cap, a box of ammunition, and two red bandannas were seized. Mrs. Maez signed a third consent to search form relating to her personal automobile; no evidence was seized from the automobile.<footnotemark>5</footnotemark></p>
<p id="b1539-11">C.</p>
<p id="b1539-12">
<em>Maez’ Interrogation</em>
</p>
<p id="b1539-13">Maez was taken into custody by the Albuquerque Police Department and turned over to the FBI at approximately 7:15 p.m. The officers asked if they could search the trailer and vehicles and when they indicated they had no search warrant, Maez <page-number citation-index="1" label="1448">*1448</page-number>said no.<footnotemark>6</footnotemark> He was then taken to an interview room where he was given <em>Miranda </em>warnings and signed a waiver of rights form. There was no conversation prior to their arrival. It was now 8:00 p.m. Maez’ interrogation lasted for an hour and one half. II R. 35. He signed a consent to search form relating to his truck during the interrogation. Guyman was called and he searched the truck.</p>
<p id="b1540-4">During the interrogation FBI agent Ga-ray asked Maez about the dark veins on his arm. Maez admitted that he used heroin three times a week and said that he had taken two valiums two hours before he was taken into custody. Ill R. 122. Maez explained that he had been driving his pickup in the vicinity of the bank (picking up pop cans) on the day of the robbery. He also admitted ownership of the cap found outside the bank doors. However, when Agent Denniston explained where it had been found, Maez denied that it was his. Agent Garay testified that about three quarters of the way through the interview, Maez vomited. Ill R. 135. The interview continued. Garay testified that Maez did not appear to him to be confused, frightened, or under the influence of drugs. Maez said that he felt dizzy from the vali-ums and that he was confused by the questions of the three officers. Ill R. 145-146.</p>
<p id="b1540-5">D.</p>
<p id="b1540-6">
<em>The Trial Court’s Ruling on the Motion to Suppress</em>
</p>
<p id="AA0O">The trial court orally denied the motion to suppress. The court found that “there was probable cause to arrest the defendant,” a fact not disputed on appeal. II R. 162-164. The court further found that Maez was arrested “legally ... after he came out of his trailer.” II R. 164.</p>
<p id="b1540-7">The court found that “while the circumstances may have been tense and while the environment may not have been ... ideal ..., that nevertheless [Ms. Patsy Maez] voluntarily and willingly gave the officers a permission to search.” II R. 164. The court concluded that all of the items which were seized from the trailer were “legally and validly taken under the permission to search....” II R. 164.</p>
<p id="b1540-10">The court further found that after being given <em>Miranda </em>warnings, Maez willingly and knowingly gave permission to search the Ford pickup “in which the holster was found.” II R. 165. The court held that the statements made by Maez, including the statements regarding his cap, were “knowingly and willingly given” after he had been given <em>Miranda </em>warnings. II R. 165.</p>
<p id="b1540-11">E.</p>
<p id="b1540-12">
<em>Evidence At Trial</em>
</p>
<p id="b1540-13">At trial, bank teller Christina Carlsen testified that one of the robbers was wearing a hat and had a red bandanna over his face. The bandanna, which was found during the search of the trailer conducted pursuant to the FBI consent form signed by Mrs. Maez, was admitted into evidence. Carlson identified Maez as the taller of the two robbers and the one who struck Mariana Griego, another teller, unconscious with the gun he was carrying. Griego identified Maez as one of the robbers. IV R. 111. She said that he put a gun under her chin. Griego said that although she could not clearly see his face during the robbery (because it was covered by the bandanna and he was wearing a cap), she was able to see his eyes, a mustache, and dark graying hair. She remembered Maez being about five feet seven inches tall. Griego also said that she recognized a number of tattoos on Maez’ arms and on the web of his thumb. IV R. 105-114.</p>
<p id="b1540-14">On the way out of the bank, one of the robbers hit Ernest Harrison, Jr., vice presi<page-number citation-index="1" label="1449">*1449</page-number>dent of the bank (and a former FBI agent) and knocked him to the ground. The taller robber’s hat fell off. Harrison followed the robbers around a corner and saw them leaving in a light colored pickup with a wooden tailgate. He said that the taller robber was wearing grey pants and was approximately five feet nine inches tall. IV R. 42-43. At the same time, a bank customer, Michael Barnes, saw what he thought was a gun and followed the truck to see the license plate number. He reported the number and also described the truck as an early 1960’s Ford with a wooden tailgate. He testified that the taller robber was wearing a light blue shirt. He also identified photographs of the truck.</p>
<p id="b1541-5">A box of .25 caliber ammunition, which was found in Maez’ trailer during the search, was admitted in evidence, as were the bandannas, cash totalling $5,844, and various pictures of the items seized. The cash consisted of 294 one dollar bills, 118 five dollar bills, 71 ten dollar bills, 120 twenty dollar bills, 7 fifty dollar bills, and 15 one hundred dollar bills. The bank had baited four twenty dollar bills, but none were found in the trailer. No guns or bank wrappers were found.</p>
<p id="b1541-6">Agent Garay testified that a holster had been found in Maez’ truck, but the holster itself was never offered in evidence. Agent Denniston testified regarding statements Maez made during his interrogation. Maez said he had been driving his truck in the vicinity of the bank (picking up cans). Maez denied the robbery, and claimed that the money found in the trailer was his. Denniston also testified that Maez admitted that the cap was his, and then recanted after being told that it had been found outside the bank.</p>
<p id="b1541-7">The sole defense witness was Mrs. Maez. She testified that when her husband left the trailer on the morning of August 14, 1987, he was wearing tennis shoes, green khaki pants, a white shirt, and a yellow hat. Later that day she left. When she returned around 3:00 p.m. Maez was there, wearing the same pants and a t-shirt. Mrs. Maez brought three of her husband’s hats to court, all of which were admitted in evidence.</p>
<p id="b1541-12">The jury returned a guilty verdict. Maez filed a motion for a new trial, arguing that Griego’s identification was impermissibly suggestive and unreliable, violating his due process right to a fair trial. The trial court denied the motion and a timely notice of appeal was filed.</p>
<p id="b1541-13">II</p>
<p id="b1541-14">
<em>Analysis</em>
</p>
<p id="b1541-15">Maez argues that his arrest at his home without a warrant violated the Fourth Amendment and that evidence subsequently obtained was tainted. We first consider whether Maez’ arrest was lawful. If his arrest was unlawful, we must then decide whether the subsequent consents to search given by Mr. and Mrs. Maez and Maez’ incriminating statements were tainted by the unlawful arrest.</p>
<p id="b1541-16">A.</p>
<p id="b1541-17">
<em>Maez’ Warrantless Arrest</em>
</p>
<p id="b1541-18">The Fourth Amendment provides that “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.” In <em>Payton v. New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#576" aria-description="Citation for case: Payton v. New York">445 U.S. 573, 576, 590</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1375" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371, 1375, 1382</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980), the Supreme Court held that, absent exigent circumstances, police officers may not enter an individual’s home without consent to make a warrantless routine felony arrest even with probable cause.<footnotemark>7</footnotemark> In the instant case, police officers, FBI agents and a SWAT team surrounded the Maez’ trailer, and with guns pointed at the home, asked him and his family to come <page-number citation-index="1" label="1450">*1450</page-number>out. They did and Maez was taken into custody.</p>
<p id="b1542-4">i</p>
<p id="b1542-5">
<em>The Application of Payton</em>
</p>
<p id="A5l">An arrest or seizure occurs “when the officer, by means of physical force or show of authority, has in some way restrained the liberty of a citizen....” <em>Terry v. Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, 19 n. 16, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, 1879 n. 16, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968). <em>See also Dunaway v. New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U.S. 200</a></span>, 207 n. 6, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">99 S.Ct. 2248</a></span>, 2253 n. 6, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">60 L.Ed.2d 824</a></span> (1979). A show “of official authority such that ‘a reasonable person would have believed he was not free to leave’ ” indicates that an arrest has occurred. <em>Florida v. Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#502" aria-description="Citation for case: Florida v. Royer">460 U.S. 491, 502</a></span>, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#1326" aria-description="Citation for case: Florida v. Royer">103 S.Ct. 1319, 1326</a></span>, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">75 L.Ed.2d 229</a></span> (1983) (plurality opinion) (quoting <em>United States v. Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U.S. 544, 554</a></span>, <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#1877" aria-description="Citation for case: United States v. Mendenhall">100 S.Ct. 1870, 1877</a></span>, <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">64 L.Ed.2d 497</a></span> (1980) (opinion of Justice Stewart joined by Justice Rehnquist)). “Examples of circumstances that might indicate a seizure, even when the person did not attempt to leave, would be the threatening presence of several officers, the display of a weapon by an officer ... or the use of language or tone of voice indicating that compliance with the officer’s request might be compelled.” <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U.S. at 554</a></span>, <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#1877" aria-description="Citation for case: United States v. Mendenhall">100 S.Ct. at 1877</a></span>. “[T]he determination of whether an arrest has occurred is not dependent on whether the citizen is formally placed under arrest....” <em>United States v. Hatfield, </em><span class="citation" data-id="486411"><a href="/opinion/486411/united-states-v-richard-lee-hatfield/#1071" aria-description="Citation for case: United States v. Richard Lee Hatfield">815 F.2d 1068, 1071</a></span> (6th Cir.1987) (quoting <em>United States v. Hardnett, </em><span class="citation" data-id="478767"><a href="/opinion/478767/united-states-v-anthony-hardnett/#356" aria-description="Citation for case: United States v. Anthony Hardnett">804 F.2d 353, 356</a></span> (6th Cir.1986), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./479/1097/">479 U.S. 1097</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./107/1318/">107 S.Ct. 1318</a></span>, <span class="citation" data-id="9060060"><a href="/opinion/9066393/mahoney-v-south-dakota/" aria-description="Citation for case: Mahoney v. South Dakota">94 L.Ed.2d 171</a></span> (1987)).</p>
<p id="b1542-7">The government argues that Maez “chose to exit his home. He was arrested in a public place.” Brief of Appellee at 14. And the trial court found that Maez “was requested to come out of his home, or out of the trailer in which he was living and he was arrested after he came out into the open.” II R. 164. We cannot agree in light of the undisputed facts. The Albuquerque SWAT team had surrounded the Maez’ trailer with rifles pointed at the home. II R. 39-41; III R. 152. Over the loud speakers the occupants “were asked to remove themselves from the mobile home ...,” as Officer Whitson testified. II R. 39. Mrs. Maez saw the officers with rifles pointed at the house and her son being searched and handcuffed. She told her husband what had happened. “[H]e went to the door and he looked out and he said, [‘]We have to go outside,[’] and he got the baby and we were going outside.” Ill R. 152. Given the presence of some ten officers, the drawn weapons of the SWAT team surrounding the trailer, the use of the loudspeakers, and the frightening circumstances his family faced, a reasonable person would have believed he had to come out of the home and submit to the show of authority. Accordingly, we hold that Maez was arrested while in his home.<footnotemark>8</footnotemark></p>
<p id="b1542-11">The government strenuously argues that <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>does not apply here because there was no warrantless entry into Maez’ home. It says that the Court drew a firm line at the threshold of the home. Brief of Appellee at 11-14. The contention has considerable force because <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>does make repeated references to entry such as “non-consensual entry into a suspect’s home....” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#576" aria-description="Citation for case: Payton v. New York">445 U.S. at 576</a></span>, 100 S.Ct. at 1375. The Court said the Fourth Amendment “has drawn a firm line at the entrance to the house. Absent exigent circumstances, that threshold may not reasonably be crossed without a warrant.” <em>Id. </em>at 590, 100 S.Ct. at 1382. And the Court noted that “ ‘physical entry of the home is the chief evil against which the wording of <page-number citation-index="1" label="1451">*1451</page-number>the Fourth Amendment is directed.’ ” <em>Id. </em>at 585, 100 S.Ct. at 1379 (quoting <em>United States v. United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U.S. 297, 313</a></span>, <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#2135" aria-description="Citation for case: United States v. United States District Court for the...">92 S.Ct. 2125, 2135</a></span>, <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">32 L.Ed.2d 752</a></span> (1972)).</p>
<p id="b1543-5">It is true also that <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>involved cases where police officers, acting with probable cause but without a warrant, entered the defendants’ homes to make arrests. In the case of Payton, the officers used crowbars to break open the door and enter the apartment. <em>Payton, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#576" aria-description="Citation for case: Payton v. New York">445 U.S. at 576-77</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1374" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1374-75</a></span>. In the case of Riddick, the officers knocked on the door of the house where Riddick lived, and when his son opened the door, entered and arrested Riddick. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#578" aria-description="Citation for case: Payton v. New York"><em>Id. </em>at 578</a></span>, 100 S.Ct. at 1376. In both cases there was physical entry. The government argues that <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>does not condemn the arrest in this case because the officers did not physically enter the trailer.</p>
<p id="b1543-6">We are persuaded, however, by the decisions of the courts which have applied <em>Pay-ton </em>where a physical crossing of the threshold did not occur and their reasoning that the lack of physical entry alone is not dispositive. Those courts have held that <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>is violated where there is such a show of force that a defendant comes out of a home under coercion and submits to being taken in custody. <em>United States v. Al-Azzawy, </em><span class="citation" data-id="465254"><a href="/opinion/465254/united-states-v-riad-abed-al-azzawy/" aria-description="Citation for case: United States v. Riad Abed Al-Azzawy">784 F.2d 890</a></span>, 893 and n. 1 (9th Cir.1985), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./476/1144/">476 U.S. 1144</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./106/2255/">106 S.Ct. 2255</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/90/700/">90 L.Ed.2d 700</a></span> (1986); <em>United States v. Morgan, </em><span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1164" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d 1158, 1164</a></span> (6th Cir.1984), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./471/1061/">471 U.S. 1061</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./105/2126/">105 S.Ct. 2126</a></span>, <span class="citation no-link">85 L.Ed.2d 490</span> (1985); <em>Scroggins v. State of Arkansas, </em><span class="citation" data-id="1509909"><a href="/opinion/1509909/scroggins-v-state/" aria-description="Citation for case: Scroggins v. State">276 Ark. 177</a></span>, <span class="citation" data-id="1509909"><a href="/opinion/1509909/scroggins-v-state/#37" aria-description="Citation for case: Scroggins v. State">633 S.W.2d 33, 37</a></span> (1982). <em>Cf. United States v. Edmondson, </em><span class="citation" data-id="471027"><a href="/opinion/471027/united-states-v-gerald-lee-edmondson/#1514" aria-description="Citation for case: United States v. Gerald Lee Edmondson">791 F.2d 1512, 1514-15</a></span> (11th Cir.1986) (FBI agents, with weapons drawn, knocked on door, directed occupant to open the door, which he did, and agents arrested him inside). In both <em><span class="citation" data-id="465254"><a href="/opinion/465254/united-states-v-riad-abed-al-azzawy/" aria-description="Citation for case: United States v. Riad Abed Al-Azzawy">Al-Azzawy</a></span> </em>and <em><span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">Morgan</a></span>, </em>as in the case now before us, the police had surrounded the defendants’ homes and requested their exit by bullhorn. Both courts reasoned that <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>was violated. <em>Al-Azzawy, </em><span class="citation" data-id="465254"><a href="/opinion/465254/united-states-v-riad-abed-al-azzawy/#893" aria-description="Citation for case: United States v. Riad Abed Al-Azzawy">784 F.2d at 893</a></span>; <em>Morgan, </em><span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1166" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d at 1166</a></span>. “In these circumstances, it is the location of the arrested person, and not the arresting agents, that determines whether an arrest occurs within a home.” <em>United States v. Al-Azzawy, </em><span class="citation" data-id="465254"><a href="/opinion/465254/united-states-v-riad-abed-al-azzawy/#893" aria-description="Citation for case: United States v. Riad Abed Al-Azzawy">784 F.2d at 893</a></span>. We agree and think the important point is that in cases of physical intrusion, or coercion to leave the home, as in this case, the privacy of the home is effectively invaded. Commentators have endorsed such a view of <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>where a defendant’s coming out of his home resulted from coercion. <em>See </em>2 LaFave, <em>Search and Seizure </em>§ 6.1(e) at 592-94 (2nd ed. 1987).</p>
<p id="b1543-8"><em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>recognizes that at the “very core [of the Fourth Amendment] stands the right of a man to retreat into his own home and there be free from unreasonable governmental intrusion.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#589" aria-description="Citation for case: Payton v. New York">445 U.S. at 589-590</a></span>, 100 S.Ct. at 1381-1382 (quoting <em>Silverman v. United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U.S. 505, 511</a></span>, <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#682" aria-description="Citation for case: Silverman v. United States">81 S.Ct. 679, 682</a></span>, <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">5 L.Ed.2d 734</a></span> (1961)). While “physical entry of the home is the chief evil against which the wording of the Fourth Amendment is directed” the Court has “refused to lock the Fourth Amendment into instances of actual physical trespass.” <em>United States v. United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U.S. 297, 313</a></span>, <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#2135" aria-description="Citation for case: United States v. United States District Court for the...">92 S.Ct. 2125, 2135</a></span>, <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">32 L.Ed.2d 752</a></span> (1972). Here the governmental intrusion, without consent and without a warrant, was in the form of extreme coercion which effected the arrest of Maez while he was in his home. We hold that the finding of the trial judge to the contrary is clearly erroneous and that, given the undisputed circumstances here, there was a violation of Maez’ Fourth Amendment rights.</p>
<p id="b1543-9">ii</p>
<p id="b1543-10">
<em>Exigent Circumstances</em>
</p>
<p id="b1543-11">In addition to its argument — which we have rejected — that there was no arrest of Maez in the home, the government says that both probable cause for the arrest and exigent circumstances existed so that there was in any event no violation of <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>. </em>Brief of Appellee at 13, 15. Emergency conditions may make a warrantless search or arrest constitutional where probable cause exists, <em>see Welsh v. Wisconsin, </em><span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#749" aria-description="Citation for case: Welsh v. Wisconsin">466 U.S. 740, 749-50</a></span>, <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#2097" aria-description="Citation for case: Welsh v. Wisconsin">104 S.Ct. 2091, 2097-98</a></span>, <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">80 L.Ed.2d 732</a></span> (1984), and here Maez does not dispute the existence of such prob<page-number citation-index="1" label="1452">*1452</page-number>able cause. Moreover, <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>recognized that if exigent circumstances exist, the constitutional bar against a suspect’s arrest in his home without a warrant does not apply. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York">445 U.S. at 590</a></span>, 100 S.Ct. at 1382. Here, however, Maez contends there was no assertion of exigency made in the trial court by the government’s law enforcement witnesses or its counsel. Appellant Maez’ Reply Brief at 12.<footnotemark>9</footnotemark> We agree and reject the government’s argument of exigent circumstances made for the first time on appeal.</p>
<p id="b1544-4">We cannot accept the government’s belated assertion of the exigent circumstances claim for basic reasons. Where police seek to enter a home without a warrant the state bears the burden of proving that sufficient exigency exists. <em>United States v. Aquino, </em><span class="citation" data-id="499820"><a href="/opinion/499820/united-states-v-luis-raul-aquino/#1271" aria-description="Citation for case: United States v. Luis Raul Aquino">836 F.2d 1268, 1271</a></span> (10th Cir.1988) (citing <em>Coolidge v. New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#455" aria-description="Citation for case: Coolidge v. New Hampshire">403 U.S. 443, 455</a></span>, <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#2032" aria-description="Citation for case: Coolidge v. New Hampshire">91 S.Ct. 2022, 2032</a></span>, <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">29 L.Ed.2d 564</a></span> (1971)). That burden is particularly heavy where the police seek to enter a suspect’s home or the home of a third person because warrantless seizures inside a home are presumptively unreasonable. <em>Aquino, </em><span class="citation" data-id="499820"><a href="/opinion/499820/united-states-v-luis-raul-aquino/" aria-description="Citation for case: United States v. Luis Raul Aquino">836 F.2d at 1271</a></span> (quoting <em>Payton, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U.S. at 586</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1380" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1380</a></span>). It is important that the facts on exigent circumstances be developed and that findings be made on them. <em>E.g., United States v. Cuaron, </em>700 F.2d at 586-91.</p>
<p id="b1544-5">In the <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>opinion itself, the Supreme Court noted that while it was arguable that the warrantless arrest of Payton might have been justified by exigent circumstances, none of the lower courts had relied on any such justification and accordingly the Court had no occasion to consider such an emergency or dangerous situation. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York">445 U.S. at 583</a></span>, 100 S.Ct. at 1378. In <em>Steagald v. United States, </em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">451 U.S. 204</a></span>, <span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">101 S.Ct. 1642</a></span>, <span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">68 L.Ed.2d 38</a></span> (1981), the government argued for the first time on appeal that the record did not clearly show that the petitioner, who was arrested in a third party’s house, had a reasonable expectation of privacy in the home. The Court declined to grant the government’s request for a remand for factual findings on the issue:</p>
<blockquote id="b1544-9">... [T]he Government was initially entitled to defend against petitioner’s charge of an unlawful search by asserting that petitioner lacked a reasonable expectation of privacy in the searched home, or that he consented to the search, <em>or that exigent circumstances justified the entry. The Government, however, may lose its right to raise factual issues of this sort before this Court </em>when it has made contrary assertions in the courts below, when it has acquiesced in contrary findings by those courts, <em>or when it has failed to raise such questions in a timely fashion during the litigation.</em></blockquote>
<blockquote id="b1544-10">We conclude that this is such a case. The Magistrate’s report on petitioner’s suppression motion, which was adopted by the District Court, characterized the issue as whether an arrest warrant was sufficient to justify the search of ‘the home of a third person’ for the subject of the warrant. App. 12. <em>The Government never sought to correct this characterization on appeal, and instead ac</em><page-number citation-index="1" label="1453">*1453</page-number><em>quiesced in the District Court’s view of petitioner’s Fourth Amendment claim.</em></blockquote>
<p id="ANxb"><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/#209" aria-description="Citation for case: Steagald v. United States"><em>Id. </em>at 209</a></span>, <span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/#1646" aria-description="Citation for case: Steagald v. United States">101 S.Ct. at 1646</a></span> (emphasis added). Here, the government concedes in its brief that it did not argue the issue below. Brief of Appellee, 15-16. In fact, the defendant specifically argued below that exigent circumstances did not exist and the government did not dispute the argument.<footnotemark>10</footnotemark> Hence the district court had no reason to consider the issue.</p>
<p id="b1545-5">For these reasons, we must reject the government’s argument that its claim of exigent circumstances be taken up for the first time on this appeal.</p>
<p id="b1545-6">B.</p>
<p id="b1545-7">
<em>The Taint Caused by the Payton Violation</em>
</p>
<p id="b1545-8">Having determined that Maez' warrant-less arrest violated <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>and the Fourth Amendment, we must now go on to consider whether the illegal arrest tainted the consents to search subsequently given by him and his wife and his custodial statements, or whether any taint was sufficiently removed and attenuated by intervening circumstances.</p>
<p id="b1545-9">i</p>
<p id="b1545-10">
<em>Mrs. Maez’ Consent to Search</em>
</p>
<p id="AFXS">We first consider whether the consent to search given by Mrs. Maez to the FBI was voluntary in fact so as to remove the taint of Maez’ unlawful arrest. A consent to search which is preceded by a Fourth Amendment violation is valid only if it is voluntary in fact. <em>United States v. Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/#1520" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d 1512, 1520-21</a></span> (10th Cir.1988); <em>United States v. Carson, </em><span class="citation" data-id="9475015"><a href="/opinion/471869/united-states-v-george-l-carson/#1151" aria-description="Citation for case: United States v. George L. Carson">793 F.2d 1141, 1151</a></span> (10th Cir.1986), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./479/914/">479 U.S. 914</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./107/315/">107 S.Ct. 315</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/93/289/">93 L.Ed.2d 289</a></span> (1986)). If the consent is not sufficiently an act of free will to purge the primary taint of the illegal arrest, it must be suppressed as fruit of the poisonous tree. <em>See Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d at 1520</a></span> (quoting <em>Brown v. Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#601" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590, 601</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2260" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254, 2260</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">45 L.Ed.2d 416</a></span> (1975)).</p>
<p id="b1545-15">Without citation to authority, the government initially argues that because Mrs. Maez was not arrested,<footnotemark>11</footnotemark> her consent to search the trailer cannot be tainted by her husband’s prior illegal arrest. We disagree and think the issue, as stated in <em>Wong Sun v. United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States">371 U.S. 471, 488</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#417" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407, 417</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">9 L.Ed.2d 441</a></span> (1963), is whether “granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint.” This conclusion is mandated by the Supreme Court’s decision in <em>United States v. Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">435 U.S. 268</a></span>, <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">98 S.Ct. 1054</a></span>, <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">55 L.Ed.2d 268</a></span> (1978). <em>See also United States v. Howard, </em><span class="citation" data-id="493964"><a href="/opinion/493964/united-states-v-randy-ray-howard-united-states-of-america-v-robert-leroy/#556" aria-description="Citation for case: United States v. Randy Ray Howard, United States of...">828 F.2d 552, 556</a></span> (9th Cir.1987).</p>
<p id="b1545-16">In <em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">Ceccolini</a></span>, </em>the defendant (a businessman suspected of gambling) moved to suppress damaging statements of an employee, resulting from an unlawful search of his business premises. <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#269" aria-description="Citation for case: United States v. Ceccolini"><em>Id. </em>at 269-72</a></span>, <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#1056" aria-description="Citation for case: United States v. Ceccolini">98 S.Ct. at 1056-58</a></span>. The employee was not arrested. The Court rejected the government’s argument that “the testimony of a live witness should not be excluded at trial no matter how close and proximate the connection between it and a violation of the Fourth Amendment.” <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#274" aria-description="Citation for case: United States v. Ceccolini"><em>Id. </em>at 274-75</a></span>, <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#1059" aria-description="Citation for case: United States v. Ceccolini">98 S.Ct. at 1059-60</a></span>. While the primary issue before the Court was whether a categorical distinction should be drawn between physical and verbal evidence found as the result of an unlawful search, the Court specifically noted that the witness whose testimony was at issue was not a <page-number citation-index="1" label="1454">*1454</page-number>defendant. <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#275" aria-description="Citation for case: United States v. Ceccolini"><em>Id. </em>at 275, 277</a></span>, <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#1059" aria-description="Citation for case: United States v. Ceccolini">98 S.Ct. at 1059, 1060-61</a></span>. The Court nevertheless concluded that “ ‘verbal evidence which derives so immediately from an unlawful entry and an unauthorized arrest as the officers’ action in the present case is no less the “fruit” of the official illegality than the more common tangible fruits of the unwarranted intrusion.’ ” <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#275" aria-description="Citation for case: United States v. Ceccolini"><em>Id. </em>at 275</a></span>, <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">98 S.Ct. at 1059</a></span> (quoting <em>Wong Sun, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#485" aria-description="Citation for case: Wong Sun v. United States">371 U.S. at 485</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#416" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. at 416</a></span>). Thus, the defendant could raise the taint issue as to the statements made by his employee. And while the witness in <em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">Ceccolini</a></span> </em>gave statements, as opposed to a consent to search, the same analysis is required here. The question is whether the statements of the witness (or in our case the consent) have “become so attenuated as to dissipate the taint.” <em>Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#274" aria-description="Citation for case: United States v. Ceccolini">435 U.S. at 274</a></span>, <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">98 S.Ct. at 1059</a></span> (quoting <em>Wong Sun, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#487" aria-description="Citation for case: Wong Sun v. United States">371 U.S. at 487, 491</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#417" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. at 417, 419</a></span>).</p>
<p id="b1546-4">Whether a consent to search preceded by a Fourth Amendment violation is sufficiently an act of free will to purge the primary taint of the illegal arrest depends upon whether it is voluntary in fact, which in turn depends upon the totality of circumstances surrounding the consent. <em>See Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d at 1520</a></span> (citing <em>Schneckloth v. Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#248" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218, 248-49</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#2058" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041, 2058-59</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L.Ed.2d 854</a></span> (1973) and <em>Carson, </em><span class="citation" data-id="9475015"><a href="/opinion/471869/united-states-v-george-l-carson/#1149" aria-description="Citation for case: United States v. George L. Carson">793 F.2d at 1149</a></span>). In applying the <em>Schneckloth v. Bustamonte </em>voluntariness test to consents to search obtained subsequent to Fourth Amendment violations, this court has considered the three factors articulated in <em>Brown v. Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">45 L.Ed.2d 416</a></span> (1975), which apply to confessions. <em>Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/#1520" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d at 1520-1521</a></span>. These factors include “[t]he temporal proximity of the arrest and the confession, the presence of intervening circumstances, and particularly, the purpose and flagrancy of the official misconduct....” <em>Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 603-04</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2261" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2261-62</a></span> (citation omitted). Weighing these factors the court must decide the ultimate question whether the consent was sufficiently an act of free will to purge the primary taint of the illegal arrest. <em>See Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/#1520" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d at 1520</a></span>. <em>See also Florida v. Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#501" aria-description="Citation for case: Florida v. Royer">460 U.S. 491, 501</a></span>, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#1326" aria-description="Citation for case: Florida v. Royer">103 S.Ct. 1319, 1326</a></span>, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">75 L.Ed.2d 229</a></span> (1983); <em>Wong Sun v. United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U.S. 471, 486</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#416" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407, 416</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">9 L.Ed.2d 441</a></span> (1963); <em>Carson, </em><span class="citation" data-id="9475015"><a href="/opinion/471869/united-states-v-george-l-carson/#1152" aria-description="Citation for case: United States v. George L. Carson">793 F.2d at 1152</a></span>; <em>United States v. Recalde, </em><span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1458" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d 1448, 1458</a></span> (10th Cir.1985).</p>
<p id="b1546-12">As noted, the district judge found that Mrs. Maez’ consent was voluntarily and willingly given, although he expressed reluctance in making this finding.<footnotemark>12</footnotemark> The judge had also held there was no illegal arrest of Mr. Maez and thus had no reason to consider whether Mrs. Maez’ consent was sufficiently an act of free will to purge the primary taint of her husband’s unlawful arrest.</p>
<p id="b1546-13">When consent is obtained after an illegal arrest there must be a break in the causal connection between the illegality and the evidence thereby obtained. <em>Dunaway v. New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#217" aria-description="Citation for case: Dunaway v. New York">442 U.S. 200, 217-19</a></span>, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#2259" aria-description="Citation for case: Dunaway v. New York">99 S.Ct. 2248, 2259-60</a></span>, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">60 L.Ed.2d 824</a></span> (1979). Here the violation of <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>and the undisputed train of events that followed compel us to hold that Mrs. Maez’ consent was tainted and invalid.<footnotemark>13</footnotemark> First, <page-number citation-index="1" label="1455">*1455</page-number>the proximity of the arrest and Mrs. Maez’ consents clearly indicate that taint of the <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>violation was not purged. The FBI consent form was signed by Mrs. Maez at approximately 7:15 p.m., just after she had been summoned from the trailer by the bullhorn. And when she signed the form she was still in the trailer park. Ill R. 64-66.</p>
<p id="b1547-5">Second, the intervening circumstances indicate no purging of the primary taint of her husband’s illegal arrest. After leaving the trailer, Mrs. Maez was immediately asked by Albuquerque police officer Whit-son to sign the police department’s consent to search form. II R. 39. She was then approached by FBI agent Gyman who explained that the FBI wanted to search for money, weapons, and clothing, and the second consent form was signed. Ill R. 65-66. There were no intervening circumstances of any significance to purge the taint of the unlawful warrantless arrest of Maez.</p>
<p id="b1547-6">With respect to the purpose and flagrancy of the violation, the last <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span> </em>factor, it cannot be said that the officers purposefully violated <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>in the sense that they were aware of the impropriety of their actions, as was the case in <em>Brown. See Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#605" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 605</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2262" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2262</a></span>. The manner of the arrest, however, created a frightening scene for the Maez family as did Brown’s arrest.<footnotemark>14</footnotemark> <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Id.</a></span> </em>Agent Marrero, who was present when Mrs. Maez signed the FBI consent form, testified that she was crying and upset when she signed the form. She said that she signed the consent forms only because she had to. Before leaving the trailer Mrs. Maez had seen her fifteen year old son walking across the street with his hands in the air, and she watched as he was handcuffed. She was holding her two month old baby from the time she left the trailer throughout the signing of all three consent forms. II R. 41, 56-57. The undisputed facts clearly indicate that the taint of Maez’ arrest had not been purged when Mrs. Maez signed the FBI consent to search form and the police department consent.<footnotemark>15</footnotemark></p>
<p id="b1548-3"><page-number citation-index="1" label="1456">*1456</page-number>The government argues that Mrs. Maez was advised of her right to refuse consent, both orally and on the consent forms themselves. While this fact is indeed probative it is not dispositive of the voluntariness issue. <em>Schneckloth, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#227" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. at 227, 249</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#2047" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. at 2047-48, 2059</a></span>; <em>Recalde, </em><span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1458" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d at 1458-59</a></span>. We note that Mrs. Maez testified that she was told by the officers that if she refused consent they could simply get a warrant while she waited outside. Ill R. 156. This tends to undermine any salutary effect that advice of the right to refuse consent might have had. <em>United States v. Ocheltree, </em><span class="citation" data-id="9466775"><a href="/opinion/378921/united-states-v-jeffrey-dean-ocheltree/#993" aria-description="Citation for case: United States v. Jeffrey Dean Ocheltree">622 F.2d 992, 993-94</a></span> (9th Cir.1980).</p>
<p id="b1548-4">We hold that Maez’ illegal arrest tainted the subsequent consents to search the trailer given by Mrs. Maez and that her consents were not “ ‘sufficiently an act of free will to purge the primary taint’ [of the illegal arrest].” <em>Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#602" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 602</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2261</a></span> (quoting <em>Wong Sun, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U.S. at 486</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#416" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. at 416</a></span>). The evidence seized pursuant to the FBI consent to search form, including the paper bag containing $5,844, the box of ammunition, two red bandannas, and the dark blue knit cap should have been suppressed, along with various photographs of the seized evidence.<footnotemark>16</footnotemark></p>
<p id="b1548-5">ii</p>
<p id="b1548-6">
<em>Maez’ Consent to Search</em>
</p>
<p id="A2f_">After exiting the trailer Maez was taken into custody by the Albuquerque police department. He was then turned over to the FBI and given <em>Miranda </em>warnings. He was taken to an interview room at the Albuquerque office of the FBI. He signed a waiver of rights form at 8:00 p.m., approximately 45 minutes after he had been taken into custody. Ill R. 110-111. He was then interrogated. During the interrogation he signed a consent to search form, authorizing a search of his pickup truck. Ill R. 112-115. Doc. 11, Exh. B. Officer Guyman searched the truck and found a holster. The district judge found that Maez, after being advised of his <em>Miranda </em>rights, “willingly and knowingly gave permission to search the Ford pickup....” Ill R. 165. As was true with respect to Mrs. Maez’ consent, the district judge did not discuss the effect of the prior illegal arrest, having held that no violation or unlawful arrest occurred.</p>
<p id="b1548-9">To determine whether Maez’ consent to search the truck was sufficiently an act of free will to purge the taint of his illegal arrest we again consider the three factors enunciated in <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>. </em>The proximity of Maez’ arrest and his subsequent consent given 45 minutes later does not indicate that the taint of the <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>violation was purged. In <em>Brown v. Illinois, </em>Brown’s initial statement was separated from his illegal arrest by less than two hours. <em>Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 604</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2262" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2262</a></span>. The Court there held that Brown’s statement, like James Wah Toy’s statement in <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>, </em>was the fruit of the poisonous tree. <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Id.</a></span> </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 604-05</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2262" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2262-63</a></span>. <em>See also Wong Sun, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U.S. at 486-87</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#416" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. at 416-17</a></span>. From the time Maez was taken to the FBI interview room he was in the custody of at least three officers, <em>see </em>III R. 109, and was initially in the presence of ten. <em>See Patino, </em>830 F.2d at 1418 (taint not purged where defendant continually in the company of one officer). His removal to the interview room does not indicate a break in the causal connection between his arrest and the subsequent consent. <em>Hayes v. Florida, </em><span class="citation" data-id="9429967"><a href="/opinion/111382/hayes-v-florida/#816" aria-description="Citation for case: Hayes v. Florida">470 U.S. 811, 816</a></span>, <span class="citation" data-id="9429967"><a href="/opinion/111382/hayes-v-florida/#1647" aria-description="Citation for case: Hayes v. Florida">105 S.Ct. 1643, 1647</a></span>, <span class="citation" data-id="9429967"><a href="/opinion/111382/hayes-v-florida/" aria-description="Citation for case: Hayes v. Florida">84 L.Ed.2d 705</a></span> (1985); <em>Dunaway, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#212" aria-description="Citation for case: Dunaway v. New York">442 U.S. at 212-13</a></span>, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#2256" aria-description="Citation for case: Dunaway v. New York">99 S.Ct. at 2256-57</a></span>.</p>
<p id="b1549-4"><page-number citation-index="1" label="1457">*1457</page-number>With respect to the second <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span> </em>factor, the effect of any intervening circumstances, the government does not point to and we do not find in the record any circumstances which would tend to dissipate the taint.<footnotemark>17</footnotemark> With respect to the last factor, the purpose and flagrancy of the official misconduct, the manner of the arrest was such that it would cause surprise, fright and confusion. <em>See Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#605" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 605</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2262" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2262</a></span>. Maez testified that he felt dizzy during his interrogation; he vomitted approximately three quarters of the way through the interview, as one of the FBI agents testified. Ill R. 135. Considering all three <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span> </em>factors, we hold that Maez’ consent to search the truck was not sufficiently an act of free will to purge the primary taint. <em>See Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/#1520" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d at 1520</a></span>.</p>
<p id="b1549-6">The government notes that the consent form was signed after Maez had been advised of his <em>Miranda </em>rights, which is probative. But as the Supreme Court noted, “[i]f <em>Miranda </em>warnings, by themselves, were held to attenuate the taint of an unconstitutional arrest, regardless of how wanton and purposeful the Fourth Amendment violation, the effect of the exclusionary rule would be substantially diluted.” <em>Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#602" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 602-03</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2261" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2261</a></span>. <em>Miranda </em>warnings do not per se break the causal connection between an illegal arrest and evidence subsequently obtained. <em>See Dunaway, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#216" aria-description="Citation for case: Dunaway v. New York">442 U.S. at 216-17</a></span>, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#2258" aria-description="Citation for case: Dunaway v. New York">99 S.Ct. at 2258-59</a></span>.</p>
<p id="b1549-7">We hold that in these circumstances, notwithstanding the <em>Miranda </em>warnings, Maez’ consent was tainted by his prior illegal arrest and the testimony regarding the holster should have been suppressed.</p>
<p id="Av1j">III</p>
<p id="b1549-10">
<em>Maez’ Custodial Statements</em>
</p>
<p id="AVXA">During his interrogation Maez explained where he had been and what he had been doing on the day of the robbery. He said that he had been in possession of his pickup throughout the day and had been in the area of the bank. He admitted ownership of a cap shown to him during the interrogation by Agent Denniston. When told that the cap had been found outside the doors of the bank which had been robbed, Maez then denied ownership of the cap. Officer Denniston testified about those statements at trial and the cap was admitted. IV R. 153-160.</p>
<p id="b1549-11">The exculpatory and incriminating statements made by Maez during his interrogation are subject to the same analysis as the consent to search the truck. <em>See Taylor v. Alabama, </em><span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/#690" aria-description="Citation for case: Taylor v. Alabama">457 U.S. 687, 690-94</a></span>, <span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/#2667" aria-description="Citation for case: Taylor v. Alabama">102 S.Ct. 2664, 2667-69</a></span>, <span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/" aria-description="Citation for case: Taylor v. Alabama">73 L.Ed.2d 314</a></span> (1982); <em>Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#593" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 593-95</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2256" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2256-58</a></span>; <em>Wong Sun, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U.S. at 486-87</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#416" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. at 416-17</a></span> (exculpatory and incriminating statements entitled to the protection of the exclusionary rule). Applying the same <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span> </em>analysis, which we made earlier, we hold that the statements should have been suppressed.<footnotemark>18</footnotemark></p>
<p id="b1549-12">IV</p>
<p id="b1549-13">The judgment is accordingly REVERSED and the case is REMANDED for further proceedings in accord with this opinion.</p>
<footnote label="1">
<p id="b1539-14">. It is not clear from the record precisely when the meeting took place. FBI agent Garay testified that it began around 4:00 p.m. Ill R. 130. Police officer Whitson said that he was at the meeting between 4:30 and 5:00 p.m. II R. 46. Agent Guyman said that he was at the meeting at 5:45 p.m. Ill R. 73.</p>
</footnote>
<footnote label="2">
<p id="b1539-15">. This first consent to search form was obtained so that the officers could enter the trailer to search for Maez, who had not yet exited. By the time the form was signed, he had exited.</p>
</footnote>
<footnote label="3">
<p id="b1539-16">. The form indicates that there is a constitutional right to deny permission to search the property. I R. 11, Exh. C.</p>
</footnote>
<footnote label="4">
<p id="b1539-17">. Mrs. Maez also testified that before she signed the Albuquerque police department consent form she was told that the officers did not have a warrant to search the house, but could get one. Ill R. 156. She thought that she would have to wait outside while they were getting the warrant if she did not sign the consent form. During this time Mrs. Maez was holding their baby. II R. 56; III R. 156, 158.</p>
</footnote>
<footnote label="5">
<p id="b1539-19">.The dissent’s focus on the voluntariness of the third consent and its quotation of testimony about it are misplaced. Nothing was seized pursuant to the third consent to search. Its validity is not at issue. We note this because the consent to search which is at issue, the second consent to search, preceded this third consent to search the automobile. In fact, the third consent form was signed over an hour after the search of the trailer. Ill R. 85. It is difficult to validate the second consent by events which occurred over an hour after it was signed.</p>
</footnote>
<footnote label="6">
<p id="b1540-8">. Maez said that he and his wife communicated with their heads regarding consent to search their trailer. "[S]he was reading the paper and she went like this, you know, and something like that (indicating), you know, to let me know if it’s all right if they can search the trailer. I told her *Well, it's your trailer. It’s up to you,’ and I shook my head up and down, to go ahead if she wanted to, because the trailer is under her name." Ill R. 145. Mrs. Maez said that she had no communication with her husband, although she was not asked specifically about nonverbal communication.</p>
</footnote>
<footnote label="7">
<p id="b1541-8">. A warrantless arrest in public with probable cause does not violate the Fourth Amendment, even though exigent circumstances do not exist. <em>United States v. Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#423" aria-description="Citation for case: United States v. Watson">423 U.S. 411, 423-24</a></span>, <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#827" aria-description="Citation for case: United States v. Watson">96 S.Ct. 820, 827-28</a></span>, <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">46 L.Ed.2d 598</a></span> (1976).</p>
</footnote>
<footnote label="8">
<p id="b1542-8">. As noted, the trial judge found that the "defendant was arrested legally. He came out of his— he was requested to come out of his home, or out of the trailer in which he was living and he was arrested after he came out into the open.” Ill R. 164.</p>
<p id="b1542-9">We review the findings on a motion to suppress under the clearly erroneous standard. <em>United States v. Alonso, </em><span class="citation" data-id="470081"><a href="/opinion/470081/united-states-v-fabio-alonso/#1493" aria-description="Citation for case: United States v. Fabio Alonso">790 F.2d 1489, 1493</a></span> (10th Cir.1986). However, where only an ultimate finding such as consent is made and there are undisputed underlying facts supporting a contrary conclusion, that conclusion may be drawn by the appellate court. <em>See United States v. Recalde, </em><span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d 1448</a></span>, 1455 n. 7, and 1456 (10th Cir.1985) (citing <em>Brown v. Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590, 604</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2262" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254, 2262</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">45 L.Ed.2d 416</a></span> (1975)).</p>
</footnote>
<footnote label="9">
<p id="b1544-6">. The government argues that the record supports the existence of exigent circumstances because: (1) the police knew that one of the bank robbers was armed and had used the butt of his handgun to disable (knock unconscious) a bank customer; (2) a large sum of money had been stolen from a bank; (3) the police had physical descriptions of items worn by the robbers which might be destroyed; (4) Maez might seek to warn the other robber or seek assistance if he should become aware of the presence of the police; and (5) the police knew Maez was a heroin addict and a convicted felon.</p>
<p id="b1544-7">Citing <em>United States v. McConney, </em><span class="citation" data-id="9471865"><a href="/opinion/431931/united-states-v-winston-bryant-mcconney/" aria-description="Citation for case: United States v. Winston Bryant McConney">728 F.2d 1195</a></span> (9th Cir.1984) (en banc), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./469/824/">469 U.S. 824</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./105/101/">105 S.Ct. 101</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/83/46/">83 L.Ed.2d 46</a></span> (1984), the government argues that the existence of exigent circumstances is supported by the record and "dictated the arrest procedure.” Brief of Appellee, at pp. 15-16. <em><span class="citation" data-id="9471865"><a href="/opinion/431931/united-states-v-winston-bryant-mcconney/" aria-description="Citation for case: United States v. Winston Bryant McConney">McConney</a></span> </em>held that the "mixed question of exigency is reviewable de novo as a question of law.” <span class="citation" data-id="9471865"><a href="/opinion/431931/united-states-v-winston-bryant-mcconney/#1204" aria-description="Citation for case: United States v. Winston Bryant McConney">728 F.2d at 1204-05</a></span>. In <em>United States v. Cuaron, </em><span class="citation" data-id="9470300"><a href="/opinion/414423/united-states-v-frank-armando-cuaron/#586" aria-description="Citation for case: United States v. Frank Armando Cuaron">700 F.2d 582, 586</a></span> (10th Cir.1983), we said that in assessing whether the government’s burden demonstrating exigent circumstances was met, we "evaluate the circumstances as they would have appeared to prudent, cautious and trained officers.” (citations omitted). Since we conclude that the government waived its right to raise the issue of exigent circumstances on appeal for reasons stated in the text, we do not undertake an evaluation of the record.</p>
</footnote>
<footnote label="10">
<p id="b1545-11">. In his "Motion To Suppress Physical Evidence" the defendant argued that “[n]o exigent circumstances existed to justify the search of the residence_” IR. 8. The argument was again made in the "Memorandum Brief In Support of Defendant’s Motion To Suppress Physical Evidence and Motion To Suppress Statements." I R. 12, p. 6. The government’s response brief does not contest these arguments. I R. 11.</p>
</footnote>
<footnote label="11">
<p id="b1545-17">. We accept the government’s contention that Mrs. Maez was not arrested only for the sake of analysis, given our conclusion that Mr. Maez was arrested while in the trailer. If under the <em>Terry, Dunaway, Mendenhall, </em>and <em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span> </em>arrest analysis, supra, Mr. Maez was arrested, it follows that Mrs. Maez was also arrested. She was in the same position.</p>
</footnote>
<footnote label="12">
<p id="b1546-5">. The court stated in part:</p>
<blockquote id="b1546-6">And I will find that while the circumstances may have been tense and while the environment may not have been that of the most ideal for considering the signing of a permission to search, that nevertheless she voluntarily and willingly gave the officers a permission to search. This is Government’s Exhibit 1.</blockquote>
<p id="b1546-7">Ill R. 164-165.</p>
</footnote>
<footnote label="13">
<p id="b1546-8">. The district court did not discuss the taint issue resulting from the <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>violation. It is not our function to try facts or to substitute our judgment for that of the trial court in determining factual issues. <em>Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/#1521" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d at 1521</a></span>. However, where the proceedings below "resulted in a record of amply sufficient detail and depth from which the determination may be made,” the appellate court may conduct a taint analysis. <em>Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 604</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2262" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2262</a></span>; quoted in <em>Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d at 1521</a></span> n. 10. <em>See also Recalde, </em><span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1458" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d at 1458-59</a></span> (voluntariness determination held clearly erroneous where, although there was some evidence to support it, the entire record indicated that the defendant’s consent was tainted); <em>United States v. Patino, </em><span class="citation" data-id="495451"><a href="/opinion/495451/united-states-v-josan-wolf-patino/#1418" aria-description="Citation for case: United States v. Josan Wolf Patino">830 F.2d 1413, 1418-19</a></span> (7th Cir.1987).</p>
<p id="A7Go">The dissent argues that it is inappropriate for us to conduct a taint analysis, that only the trial <page-number citation-index="1" label="1455">*1455</page-number>court is in a position to assess credibility and discern truth and that the case should be remanded. But none of the facts relating to the proximity of the arrest and confession, the presence of intervening circumstances, or the flagrancy of official misconduct are in dispute. And these <em>are </em>the facts which are crucial to the taint analysis and upon which the government bore the burden of proof. <em>See Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 603-04</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2261" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2261-62</a></span>; <em>Guzman, </em><span class="citation" data-id="516479"><a href="/opinion/516479/united-states-v-jose-luis-guzman-and-sonia-cruz-lazo/#1520" aria-description="Citation for case: United States v. Jose Luis Guzman and Sonia Cruz-Lazo">864 F.2d at 1520-21</a></span>; <em>Recalde, </em><span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1457" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d at 1457-59</a></span>. The record is of "amply sufficient detail and depth” for us to conclude, as the Court did in <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>, </em>that the taint of the Fourth Amendment violation was not purged. <em>Brown, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois">422 U.S. at 603-04</a></span>, <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#2261" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. at 2261-62</a></span>. The suppression hearing developed the circumstances in detail (II R. at 4-58; III R. at 62-162) and the basic facts vitiating the consents and statements are undisputed, as noted throughout our opinion.</p>
<p id="A8L">Applying the proper test of considering the whole record, and not merely relying on portions as the dissent does to support its view, we are left with the firm conviction that a mistake was made in finding the consents and Mr. Maez’ statements valid. The correct standard of review is whether "although there is evidence to support [the findings], the reviewing court on the entire evidence is left with the definite and firm conviction that a mistake has been committed.” <em>United States v. Grier, </em><span class="citation" data-id="517661"><a href="/opinion/517661/united-states-v-charles-h-grier-and-isaac-harper/#935" aria-description="Citation for case: United States v. Charles H. Grier and Isaac Harper">866 F.2d 908, 935</a></span> (7th Cir.1989) (quoting <em>United States v. D’Antoni, </em><span class="citation" data-id="511654"><a href="/opinion/511654/united-states-v-todd-a-dantoni/#978" aria-description="Citation for case: United States v. Todd A. D&#x27;Antoni">856 F.2d 975, 978-79</a></span> (7th Cir. 1988)).</p>
</footnote>
<footnote label="14">
<p id="b1547-10">. The dissent rejects the majority’s view that the circumstances created a frightening scene for the Maez family. The dissent’s reasoning is difficult to understand since the dissent accepts the majority’s holding that a violation of <em>Payton v. New York </em>occurred — that holding being grounded on the frightening scene that exerted "extreme coercion which effected the arrest of Maez while he was in his home.” <em>See supra </em>at p. 1451. Our <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>holding follows state and federal courts which hold that a <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>violation occurs where there is such a show of force that a defendant comes out of his home under coercion and submits to being taken into custody. <em>See supra </em>at p. 1451. The essential facts leading us to hold there was a frightening scene here were undisputed — the presence of ten armed SWAT team members with rifles pointed at the trailer, the request to come out over the bull horn, and the handcuffing of the fifteen year old son.</p>
</footnote>
<footnote label="15">
<p id="b1547-11">. The dissent contends that our opinion misreads the record. When reviewing the denial of a motion to suppress an appellate court must consider the evidence in the light most favorable to the government and must accept the trial court’s findings of fact unless clearly erroneous. <em>United States v. Jimenez, </em><span class="citation" data-id="516255"><a href="/opinion/516255/united-states-v-alfonso-steve-jimenez/#688" aria-description="Citation for case: United States v. Alfonso Steve Jimenez">864 F.2d 686, 688</a></span> (10th Cir.1988). But an appellate court must not simply consider from the record those facts which might support a trial court’s findings and ignore the record as a whole. A trial court’s factual <page-number citation-index="1" label="1456">*1456</page-number>determinations in criminal cases, as in civil cases, <em>see Anderson v. Bessemer City, </em><span class="citation" data-id="9429949"><a href="/opinion/111373/anderson-v-city-of-bessemer-city/#573" aria-description="Citation for case: Anderson v. City of Bessemer City">470 U.S. 564, 573</a></span>, <span class="citation" data-id="9429949"><a href="/opinion/111373/anderson-v-city-of-bessemer-city/#1510" aria-description="Citation for case: Anderson v. City of Bessemer City">105 S.Ct. 1504, 1510</a></span>, <span class="citation" data-id="9429949"><a href="/opinion/111373/anderson-v-city-of-bessemer-city/" aria-description="Citation for case: Anderson v. City of Bessemer City">84 L.Ed.2d 518</a></span> (1985), may be clearly erroneous even where supported by some evidence, if on the whole record the court is left with a firm and definite conviction that a mistake has been committed. <em>United States v. Grier, </em><span class="citation" data-id="517661"><a href="/opinion/517661/united-states-v-charles-h-grier-and-isaac-harper/#935" aria-description="Citation for case: United States v. Charles H. Grier and Isaac Harper">866 F.2d 908, 935</a></span> (7th Cir.1989). <em>See e.g. United States </em>v. <em>Recalde, </em><span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1457" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d 1448, 1457-59</a></span> (10th Cir.1985) (voluntariness determination held clearly erroneous where, although there was some evidence to support it, the entire record indicated that the defendant's consent was tainted).</p>
</footnote>
<footnote label="16">
<p id="b1548-11">. The photographs referred to Eire only those photographs of the tainted evidence which were admitted at trial.</p>
</footnote>
<footnote label="17">
<p id="b1549-8">. The government argues that because Maez refused to consent to a search of his home he was capable of exercising his rights, free from the taint of the illegal arrest. While relevant, this fact is not dispositive. In <em><span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/" aria-description="Citation for case: United States v. Miguel Angel Recalde">Recalde</a></span>, </em>the defendant refused to answer questions and yet subsequently signed a consent form; we nevertheless found that consent tainted. <em>Recalde, </em><span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1459" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d at 1459</a></span>.</p>
</footnote>
<footnote label="18">
<p id="b1549-9">. While Maez’ Fourth Amendment rights were violated and the evidence outlined in Part B should have been suppressed, we could affirm the conviction if the constitutional errors were harmless beyond a reasonable doubt. <em>Harrington v. California, </em><span class="citation" data-id="9424056"><a href="/opinion/107952/harrington-v-california/#254" aria-description="Citation for case: Harrington v. California">395 U.S. 250, 254</a></span>, <span class="citation" data-id="9424056"><a href="/opinion/107952/harrington-v-california/#1728" aria-description="Citation for case: Harrington v. California">89 S.Ct. 1726, 1728</a></span>, <span class="citation" data-id="9424056"><a href="/opinion/107952/harrington-v-california/" aria-description="Citation for case: Harrington v. California">23 L.Ed.2d 284</a></span> (1969); <em>United States v. Morales Quinones, </em><span class="citation" data-id="483643"><a href="/opinion/483643/united-states-v-miguel-morales-quinones/#610" aria-description="Citation for case: United States v. Miguel Morales-Quinones">812 F.2d 604, 610</a></span> (10th Cir.1987). The government concedes, however, that if admission of the paper bag containing the money, the box of ammunition, the red bandannas, the photographs, and the dark blue knit cap was error, its admission cannot be considered harmless error. Brief of Appellee, p. 21.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Martinez-Fuerte.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Martinez-Fuerte"
type: case
citation: "428 U.S. 543 (1976)"
parallel_cite: "96 S. Ct. 3074; 49 L. Ed. 2d 1116"
neutral_cite: 1976 U.S. LEXIS 87
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-07-06
docket: 74-1560
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-07-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Martinez-Fuerte
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109541/united-states-v-martinez-fuerte/"
  cluster_id: 109541
  opinion_id: 109541
  identity_checked: true
homes:
  - page: "[[Border Searches]]"
    role: "Key — Anchor"
  - page: "[[Checkpoints and Roadblocks]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Brignoni-Ponce]]", "[[Almeida-Sanchez v. United States]]", "[[Michigan Dept. of State Police v. Sitz]]", "[[City of Indianapolis v. Edmond]]"]
aliases: []
tags: ["case", "fourth-amendment", "border-searches", "immigration-checkpoint", "fixed-checkpoint", "individualized-suspicion"]
holding: "Brief stops at fixed/permanent interior immigration checkpoints are constitutional without any individualized suspicion; routine…"
lake:
  record_id: United States v. Martinez-Fuerte
  status: verified
  projected_at: 2026-07-09
---

# United States v. Martinez-Fuerte

*428 U.S. 543 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
At the San Clemente, California fixed immigration checkpoint on Interstate 5 — a permanent, clearly marked installation well inside the border — Border Patrol agents stopped passing vehicles for brief questioning about citizenship and referred some cars to a secondary inspection area. Martinez-Fuerte and other defendants were prosecuted for transporting illegal aliens found through these stops. They challenged the checkpoint stops and the secondary referrals as unreasonable seizures.

## Issue
Whether routine stops for brief questioning at a permanent immigration checkpoint, and selective referral of motorists to a secondary inspection area, are consistent with the Fourth Amendment when conducted without individualized suspicion or a warrant.

## Rule
Yes. "In summary, we hold that stops for brief questioning routinely conducted at permanent checkpoints are consistent with the Fourth Amendment and need not be authorized by warrant." — 428 U.S. at 566. ^pin-566

No individualized suspicion is required for the initial stop: "Accordingly, we hold that the stops and questioning at issue may be made in the absence of any individualized suspicion at reasonably located checkpoints." — [*Id.* at 562](https://www.courtlistener.com/opinion/109541/united-states-v-martinez-fuerte/#:~:text=Accordingly%2C%20we%20hold%20that%20the). ^pin-562

Nor must referral to secondary inspection meet the roving-patrol standard: "We further believe that it is constitutional to refer motorists selectively to the secondary inspection area at the San Clemente checkpoint on the basis of criteria that would not sustain a roving-patrol stop. Thus, even if it be assumed that such referrals are made largely on the basis of apparent Mexican ancestry, we perceive no constitutional violation." — *Id.* at 563. ^pin-563

## Application
On these facts the checkpoint procedures were reasonable. The San Clemente checkpoint was fixed and permanent, so motorists had advance notice and the stops were brief, predictable, and minimally intrusive — unlike the roving patrols that *[[United States v. Brignoni-Ponce|Brignoni-Ponce]]* required to be supported by reasonable suspicion. The public interest in policing the border, and the impracticality of demanding individualized suspicion for each of the many vehicles passing a high-volume checkpoint, justified the suspicionless stops; the decision to seize was governed by the location of the checkpoint and the judgment of higher-ranking officials, not the unbridled discretion of the field officer. Because the intrusion of a secondary referral was also minimal, that referral did not require reasonable suspicion. The stops and referrals of these defendants were therefore constitutional.

## Conclusion
Routine stops and secondary referrals at permanent immigration checkpoints are reasonable under the Fourth Amendment without individualized suspicion or a warrant; Martinez-Fuerte's conviction was affirmed and the contrary judgments reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Martinez-Fuerte* is the foundational fixed-checkpoint case, distinguished from roving patrols ([[United States v. Brignoni-Ponce]], [[Almeida-Sanchez v. United States]]) and later defining the suspicionless-checkpoint line applied in [[Michigan Dept. of State Police v. Sitz]] (sobriety checkpoints upheld) and limited in [[City of Indianapolis v. Edmond]] (general crime-control checkpoints struck down).

## Appears on
- [[Border Searches]] — *Key — Anchor*

## Sources
- *United States v. Martinez-Fuerte*, 428 U.S. 543 (1976) — https://www.courtlistener.com/opinion/109541/united-states-v-martinez-fuerte/ — pinpoints: 562, 563, 566.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e9c2723b52264e3c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Martinez-Fuerte"}, "payload": {"all": [{"cite": "428 U.S. 543", "page": "543", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "428"}, {"cite": "96 S. Ct. 3074", "page": "3074", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "96"}, {"cite": "49 L. Ed. 2d 1116", "page": "1116", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "49"}, {"cite": "1976 U.S. LEXIS 87", "page": "87", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1976"}], "display": "428 U.S. 543", "official": {"cite": "428 U.S. 543", "page": "543", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "428"}, "official_selection_present": true, "record_id": "United States v. Martinez-Fuerte"}}
{"assertion_id": "0d6c70efeaf5e30a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-563", "record_id": "United States v. Martinez-Fuerte"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-563", "pinpoint_status": "slip-only", "quote": "We further believe that it is constitutional to refer motorists selectively to the secondary inspection area at the San Clemente checkpoint on the basis of criteria that would not sustain a roving-patrol stop. Thus, even if it be assumed that such referrals are made largely on the basis of apparent Mexican ancestry, we perceive no constitutional violation.", "quote_fidelity": "mismatch", "record_id": "United States v. Martinez-Fuerte", "star_marker": null}}
{"assertion_id": "4e17a951134427fa", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-562", "record_id": "United States v. Martinez-Fuerte"}, "payload": {"fragment": "#:~:text=Accordingly%2C%20we%20hold%20that%20the", "page": null, "pin_id": "pin-562", "pinpoint_status": "star-verified", "quote": "Accordingly, we hold that the stops and questioning at issue may be made in the absence of any individualized suspicion at reasonably located checkpoints.", "quote_fidelity": "matched", "record_id": "United States v. Martinez-Fuerte", "star_marker": "562"}}
{"assertion_id": "dd1a7b865ebdf937", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-566", "record_id": "United States v. Martinez-Fuerte"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-566", "pinpoint_status": "slip-only", "quote": "--- # United States v. Martinez-Fuerte *428 U.S. 543 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background At the San Clemente, California fixed immigration checkpoint on Interstate 5 — a permanent, clearly marked installation well inside the border — Border Patrol agents stopped passing vehicles for brief questioning about citizenship and referred some cars to a secondary inspection area. Martinez-Fuerte and other defendants were prosecuted for transporting illegal aliens found through these stops. They challenged the checkpoint stops and the secondary referrals as unreasonable seizures. ## Issue Whether routine stops for brief questioning at a permanent immigration checkpoint, and selective referral of motorists to a secondary inspection area, are consistent with the Fourth Amendment when conducted without individualized suspicion or a warrant. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "United States v. Martinez-Fuerte", "star_marker": null}}
{"assertion_id": "3a7e783477af7d6f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Martinez-Fuerte"}, "payload": {"as_of_content": "1976-07-06", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Martinez-Fuerte", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Martinez-Fuerte

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Martinez-Fuerte",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Martinez-Fuerte",
    "case_name_short": "Martinez-Fuerte",
    "case_name_full": "UNITED STATES v. MARTINEZ-FUERTE Et Al.",
    "input_case_name": "United States v. Martinez-Fuerte",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-07-06",
    "year": 1976,
    "docket": "74-1560",
    "cluster_id": 109541,
    "lead_opinion_id": 109541,
    "sibling_ids": [
      109541,
      9426591,
      9426592
    ],
    "absolute_url": "/opinion/109541/united-states-v-martinez-fuerte/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "428 U.S. 543",
      "volume": "428",
      "reporter": "U.S.",
      "page": "543",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 3074",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "3074",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 1116",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "1116",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 87",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "87",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "428 U.S. 543",
        "volume": "428",
        "reporter": "U.S.",
        "page": "543",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 3074",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "3074",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 1116",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "1116",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 87",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "87",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "428 U.S. 543",
    "official_selection": {
      "court_class": "scotus",
      "selected": "428 U.S. 543",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-566",
      "page": null,
      "quote": "--- # United States v. Martinez-Fuerte *428 U.S. 543 (1976)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background At the San Clemente, California fixed immigration checkpoint on Interstate 5 \u2014 a permanent, clearly marked installation well inside the border \u2014 Border Patrol agents stopped passing vehicles for brief questioning about citizenship and referred some cars to a secondary inspection area. Martinez-Fuerte and other defendants were prosecuted for transporting illegal aliens found through these stops. They challenged the checkpoint stops and the secondary referrals as unreasonable seizures. ## Issue Whether routine stops for brief questioning at a permanent immigration checkpoint, and selective referral of motorists to a secondary inspection area, are consistent with the Fourth Amendment when conducted without individualized suspicion or a warrant. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-562",
      "page": null,
      "quote": "Accordingly, we hold that the stops and questioning at issue may be made in the absence of any individualized suspicion at reasonably located checkpoints.",
      "star_marker": "562",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 36917,
      "fragment": "#:~:text=Accordingly%2C%20we%20hold%20that%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-563",
      "page": null,
      "quote": "We further believe that it is constitutional to refer motorists selectively to the secondary inspection area at the San Clemente checkpoint on the basis of criteria that would not sustain a roving-patrol stop. Thus, even if it be assumed that such referrals are made largely on the basis of apparent Mexican ancestry, we perceive no constitutional violation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-07-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Martinez-Fuerte",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Johnny Vasquez-Algarin",
          "cluster_id": 3199633,
          "cite": [
            "821 F.3d 467",
            "2016 U.S. App. LEXIS 7889",
            "2016 WL 1730540"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Warren",
          "cluster_id": 2806866,
          "cite": [
            "87 Mass. App. Ct. 476"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grice",
          "cluster_id": 2792904,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grice",
          "cluster_id": 2772730,
          "cite": [
            "367 N.C. 753",
            "767 S.E.2d 312",
            "2015 N.C. LEXIS 69"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kenneth Lee Douds v. State",
          "cluster_id": 2983813,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Price",
          "cluster_id": 2728832,
          "cite": [
            "233 N.C. App. 386",
            "757 S.E.2d 309",
            "2014 WL 1366446",
            "2014 N.C. App. LEXIS 317"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bell v. Wolfish",
          "cluster_id": 110075,
          "cite": [
            "60 L. Ed. 2d 447",
            "99 S. Ct. 1861",
            "441 U.S. 520",
            "1979 U.S. LEXIS 100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mendenhall",
          "cluster_id": 110264,
          "cite": [
            "64 L. Ed. 2d 497",
            "100 S. Ct. 1870",
            "446 U.S. 544",
            "1980 U.S. LEXIS 102"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Delaware v. Prouse",
          "cluster_id": 110045,
          "cite": [
            "59 L. Ed. 2d 660",
            "99 S. Ct. 1391",
            "440 U.S. 648",
            "1979 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tennessee v. Garner",
          "cluster_id": 111397,
          "cite": [
            "85 L. Ed. 2d 1",
            "105 S. Ct. 1694",
            "471 U.S. 1",
            "1985 U.S. LEXIS 195",
            "53 U.S.L.W. 4410"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Mimms",
          "cluster_id": 109751,
          "cite": [
            "54 L. Ed. 2d 331",
            "98 S. Ct. 330",
            "434 U.S. 106",
            "1977 U.S. LEXIS 157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sharpe",
          "cluster_id": 111378,
          "cite": [
            "84 L. Ed. 2d 605",
            "105 S. Ct. 1568",
            "470 U.S. 675",
            "1985 U.S. LEXIS 74",
            "53 U.S.L.W. 4346"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Texas",
          "cluster_id": 110128,
          "cite": [
            "61 L. Ed. 2d 357",
            "99 S. Ct. 2637",
            "443 U.S. 47",
            "1979 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. Delgado",
          "cluster_id": 111148,
          "cite": [
            "80 L. Ed. 2d 247",
            "104 S. Ct. 1758",
            "466 U.S. 210",
            "1984 U.S. LEXIS 57",
            "52 U.S.L.W. 4436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arkansas v. Sanders",
          "cluster_id": 110119,
          "cite": [
            "61 L. Ed. 2d 235",
            "99 S. Ct. 2586",
            "442 U.S. 753",
            "1979 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109541 OR 9426591 OR 9426592) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzAyNzM5MjAwMDAwJnM9MjQ4NDY3MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109541+OR+9426591+OR+9426592%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109541 OR 9426591 OR 9426592)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02MDQmcz0xMTEzODImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109541+OR+9426591+OR+9426592%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109541 OR 9426591 OR 9426592)",
        "reviewed": 21,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 21,
        "triage_read": 0,
        "triage_snippet_classified": 21
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109541 OR 9426591 OR 9426592)",
    "indexed_citing_opinions": 1385,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109541,
        "count": 1267,
        "count_source": "search"
      },
      {
        "opinion_id": 9426591,
        "count": 162,
        "count_source": "search"
      },
      {
        "opinion_id": 9426592,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2153,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-martinez-fuerte.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg0Njk5OTYmcz05NDMwNzA2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109541+OR+9426591+OR+9426592%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109541,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 109313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 109332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 109504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 109522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 319859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 320555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 320688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 326898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 1802688,
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
    "date_created": "2026-07-06T01:26:35Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:26:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:26:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:29:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:26:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Martinez-Fuerte

```
<div>
<center><b><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U.S. 543</a></span> (1976)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
MARTINEZ-FUERTE ET AL.</h1></center>
<center>No. 74-1560.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued April 26, 1976.</center>
<center>Decided July 6, 1976.<sup>[*]</sup></center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><span class="star-pagination">*544</span> <i>Mark L. Evans</i> argued the cause for the United States in both cases. With him on the briefs were <i>Solicitor General Bork, Assistant Attorney General Thornburgh,</i> and <i>Sidney M. Glazer.</i></p>
<p><i>Ballard Bennett,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./423/1030/">423 U. S. 1030</a></span>, argued the cause and filed briefs for petitioner in No. 75-5387.</p>
<p><i>Charles M. Sevilla,</i> by appointment of the Court, <span class="citation" data-id="8998003"><a href="/opinion/9005294/payton-v-united-states-court-of-appeals-for-the-seventh-circuit/" aria-description="Citation for case: Payton v. United States Court of Appeals for the Seventh...">423 U. S. 922</a></span>, argued the cause for respondents in No. 74-1560. With him on the brief was <i>Michael J. McCabe.</i><sup>[]</sup></p>
<p><span class="star-pagination">*545</span> MR. JUSTICE POWELL delivered the opinion of the Court.</p>
<p>These cases involve criminal prosecutions for offenses relating to the transportation of illegal Mexican aliens. Each defendant was arrested at a permanent checkpoint operated by the Border Patrol away from the international border with Mexico, and each sought the exclusion of certain evidence on the ground that the operation of the checkpoint was incompatible with the Fourth Amendment. In each instance whether the Fourth Amendment was violated turns primarily on whether a vehicle may be stopped at a fixed checkpoint for brief questioning of its occupants even though there is no reason to believe the particular vehicle contains illegal aliens. We reserved this question last Term in <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891</a></span>, 897 n. 3 (1975). We hold today that such stops are consistent with the Fourth Amendment. We also hold that the operation of a fixed checkpoint need not be authorized in advance by a judicial warrant.</p>
<p></p>
<h2>I</h2>
<p></p>
<h2>A</h2>
<p>The respondents in No. 74-1560 are defendants in three separate prosecutions resulting from arrests made on three different occasions at the permanent immigration checkpoint on Interstate 5 near San Clemente, Cal. Interstate 5 is the principal highway between San Diego and Los Angeles, and the San Clemente checkpoint is 66 road miles north of the Mexican border. We previously have described the checkpoint as follows:</p>
<blockquote>" `Approximately one mile south of the checkpoint is a large black on yellow sign with flashing yellow lights over the highway stating "ALL VEHICLES, STOP AHEAD, 1 MILE." Three-quarters of a <span class="star-pagination">*546</span> mile further north are two black on yellow signs suspended over the highway with flashing lights stating "WATCH FOR BRAKE LIGHTS." At the checkpoint, which is also the location of a State of California weighing station, are two large signs with flashing red lights suspended over the highway. These signs each state "STOP HEREU. S. OFFICERS." Placed on the highway are a number of orange traffic cones funneling traffic into two lanes where a Border Patrol agent in full dress uniform, standing behind a white on red "STOP" sign checks traffic. Blocking traffic in the unused lanes are official U. S. Border Patrol vehicles with flashing red lights. In addition, there is a permanent building which houses the Border Patrol office and temporary detention facilities. There are also floodlights for nighttime operation.' " <i>United States</i> v. <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#893" aria-description="Citation for case: United States v. Ortiz"><i>Ortiz, supra,</i> at 893</a></span>, quoting <i>United States</i> v. <i>Baca,</i> <span class="citation" data-id="1802688"><a href="/opinion/1802688/united-states-v-baca/#410" aria-description="Citation for case: United States v. Baca">368 F. Supp. 398, 410-411</a></span> (SD Cal. 1973).</blockquote>
<p>The "point" agent standing between the two lanes of traffic visually screens all northbound vehicles, which the checkpoint brings to a virtual, if not a complete, halt.<sup>[1]</sup> Most motorists are allowed to resume their progress without any oral inquiry or close visual examination. In a relatively small number of cases the "point" agent will conclude that further inquiry is in order. He directs these cars to a secondary inspection area, where their occupants are asked about their citizenship and immigration status. The Government informs us that at San <span class="star-pagination">*547</span> Clemente the average length of an investigation in the secondary inspection area is three to five minutes. Brief for United States 53. A direction to stop in the secondary inspection area could be based on something suspicious about a particular car passing through the checkpoint, but the Government concedes that none of the three stops at issue in No. 74-1560 was based on any articulable suspicion. During the period when these stops were made, the checkpoint was operating under a magistrate's "warrant of inspection," which authorized the Border Patrol to conduct a routine-stop operation at the San Clemente location.<sup>[2]</sup></p>
<p>We turn now to the particulars of the stops involved in No. 74-1560. and the procedural history of the case. Respondent Amado Martinez-Fuerte approached the checkpoint driving a vehicle containing two female passengers. The women were illegal Mexican aliens who had entered the United States at the San Ysidro port of entry by using false papers and rendezvoused with Martinez-Fuerte in San Diego to be transported northward. At the checkpoint their car was directed to the secondary inspection area. Martinez-Fuerte produced documents showing him to be a lawful resident alien, but his passengers admitted being present in the country unlawfully. He was charged, <i>inter alia,</i> with two counts of illegally transporting aliens in violation <span class="star-pagination">*548</span> of <span class="citation no-link">8 U. S. C. § 1324</span> (a) (2). He moved before trial to suppress all evidence stemming from the stop on the ground that the operation of the checkpoint was in violation of the Fourth Amendment.<sup>[3]</sup> The motion to suppress was denied, and he was convicted on both counts after a jury trial.</p>
<p>Respondent Jose Jiminez-Garcia attempted to pass through the checkpoint while driving a car containing one passenger. He had picked the passenger up by prearrangement in San Ysidro after the latter had been smuggled across the border. Questioning at the secondary inspection area revealed the illegal status of the passenger, and Jiminez-Garcia was charged in two counts with illegally transporting an alien. <span class="citation no-link">8 U. S. C. § 1324</span> (a) (2), and conspiring to commit that offense, <span class="citation no-link">18 U. S. C. § 371</span>. His motion to suppress the evidence derived from the stop was granted.</p>
<p>Respondents Raymond Guillen and Fernando Medrano-Barragan approached the checkpoint with Guillen driving and Medrano-Barragan and his wife as passengers. Questioning at the secondary inspection area revealed that Medrano-Barragan and his wife were illegal aliens. A subsequent search of the car uncovered three other illegal aliens in the trunk. Medrano-Barragan had led the other aliens across the border at the beach near Tijuana, Mexico, where they rendezvoused with Guillen, a United States citizen. Guillen and Medrano-Barragan were jointly indicted on four counts of illegally transporting <span class="star-pagination">*549</span> aliens. <span class="citation no-link">8 U. S. C. § 1324</span> (a) (2), four counts of inducing the illegal entry of aliens, § 1324 (a) (4), and one conspiracy count, <span class="citation no-link">18 U. S. C. § 371</span>. The District Court granted the defendants' motion to suppress.</p>
<p>Martinez-Fuerte appealed his conviction, and the Government appealed the granting of the motions to suppress in the respective prosecutions of Jiminez-Garcia and of Guillen and Medrano-Barragan.<sup>[4]</sup> The Court of Appeals for the Ninth Circuit consolidated the three appeals, which presented the common question whether routine stops and interrogations at checkpoints are consistent with the Fourth Amendment.<sup>[5]</sup> The Court of Appeals held, with one judge dissenting, that these stops violated the Fourth Amendment, concluding that a stop for inquiry is constitutional only if the Border Patrol reasonably suspects the presence of illegal aliens on the basis of articulable facts. It reversed Martinez-Fuerte's conviction, and affirmed the orders to suppress in the other cases. <span class="citation multiple-matches"><a href="/c/F.%202d/514/308/">514 F. 2d 308</a></span> (1975). We reverse and remand.</p>
<p></p>
<h2>B</h2>
<p>Petitioner in No. 75-5387, Rodolfo Sifuentes, was arrested at the permanent immigration checkpoint on U. S. Highway 77 near Sarita. Tex. Highway 77 originates in Brownsville, and it is one of the two major highways running north from the lower Rio Grande valley. The Sarita checkpoint is about 90 miles north of Brownsville, <span class="star-pagination">*550</span> and 65-90 miles from the nearest points of the Mexican border. The physical arrangement of the checkpoint resembles generally that at San Clemente, but the checkpoint is operated differently in that the officers customarily stop all northbound motorists for a brief inquiry. Motorists whom the officers recognize as local inhabitants, however, are waved through the checkpoint without inquiry. Unlike the San Clemente checkpoint the Sarita operation was conducted without a judicial warrant.</p>
<p>Sifuentes drove up to the checkpoint without any visible passengers. When an agent approached the vehicle, however, he observed four passengers, one in the front seat and the other three in the rear, slumped down in the seats. Questioning revealed that each passenger was an illegal alien, although Sifuentes was a United States citizen. The aliens had met Sifuentes in the United States, by prearrangement, after swimming across the Rio Grande.</p>
<p>Sifuentes was indicted on four counts of illegally transporting aliens. <span class="citation no-link">8 U. S. C. § 1324</span> (a) (2). He moved on Fourth Amendment grounds to suppress the evidence derived from the stop. The motion was denied and he was convicted after a jury trial. Sifuentes renewed his Fourth Amendment argument on appeal, contending primarily that stops made without reason to believe a car is transporting aliens illegally are unconstitutional. The United States Court of Appeals for the Fifth Circuit affirmed the conviction, <span class="citation multiple-matches"><a href="/c/F.%202d/517/1402/">517 F. 2d 1402</a></span> (1975), relying on its opinion in <i>United States</i> v. <i>Santibanez,</i> <span class="citation" data-id="328159"><a href="/opinion/328159/united-states-v-jose-rodriguez-santibanez/" aria-description="Citation for case: United States v. Jose Rodriguez Santibanez">517 F. 2d 922</a></span> (1975). There the Court of Appeals had ruled that routine checkpoint stops are consistent with the Fourth Amendment. We affirm.<sup>[6]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*551</span> II</h2>
<p>The Courts of Appeals for the Ninth and the Fifth Circuits are in conflict on the constitutionality of a law enforcement technique considered important by those charged with policing the Nation's borders. Before turning to the constitutional question, we examine the context in which it arises.</p>
<p></p>
<h2>A</h2>
<p>It has been national policy for many years to limit immigration into the United States. Since July 1, 1968, the annual quota for immigrants from all independent countries of the Western Hemisphere, including Mexico, has been 120,000 persons. Act of Oct. 3, 1965, § 21 (e), <span class="citation no-link">79 Stat. 921</span>. Many more aliens than can be accommodated under the quota want to live and work in the United States. Consequently, large numbers of aliens seek illegally to enter or to remain in the United States. We noted last Term that "[e]stimates of the number of illegal immigrants [already] in the United States vary widely. A conservative estimate in 1972 produced a figure of about one million, but the Immigration and Naturalization Service now suggests there may be as many as 10 or 12 million aliens illegally in the country." <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975) (footnote omitted). It is estimated that 85% of the illegal immigrants are from Mexico, drawn by the fact that economic opportunities are significantly greater in the United States than they are in Mexico. <i>United States</i> v. <i>Baca,</i> <span class="citation" data-id="1802688"><a href="/opinion/1802688/united-states-v-baca/#402" aria-description="Citation for case: United States v. Baca">368 F. Supp., at 402</a></span>.</p>
<p><span class="star-pagination">*552</span> Interdicting the flow of illegal entrants from Mexico poses formidable law enforcement problems. The principal problem arises from surreptitious entries. <span class="citation" data-id="1802688"><a href="/opinion/1802688/united-states-v-baca/#405" aria-description="Citation for case: United States v. Baca"><i>Id.,</i> at 405</a></span>. The United States shares a border with Mexico that is almost 2,000 miles long, and much of the border area is uninhabited desert or thinly populated arid land. Although the Border Patrol maintains personnel, electronic equipment, and fences along portions of the border, it remains relatively easy for individuals to enter the United States without detection. It also is possible for an alien to enter unlawfully at a port of entry by the use of falsified papers or to enter lawfully but violate restrictions of entry in an effort to remain in the country unlawfully.<sup>[7]</sup> Once within the country, the aliens seek to travel inland to areas where employment is believed to be available, frequently meeting by prearrangement with friends or professional smugglers who transport them in private vehicles. <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#879" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 879</a></span>.</p>
<p>The Border Patrol conducts three kinds of inland traffic-checking operations in an effort to minimize illegal immigration. Permanent checkpoints, such as those at San Clemente and Sarita, are maintained at or near intersections of important roads leading away from the border. They operate on a coordinated basis designed to avoid circumvention by smugglers and others who transport the illegal aliens. Temporary checkpoints, which operate like permanent ones, occasionally are established in other strategic locations. Finally, roving patrols are maintained to supplement the checkpoint system. See <i>Almeida-Sanchez</i> v. <i>United</i> <span class="star-pagination">*553</span> <i>States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#268" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 268</a></span> (1973).<sup>[8]</sup> In fiscal 1973, 175,-511 deportable aliens were apprehended throughout the Nation by "line watch" agents stationed at the border itself. Traffic-checking operations in the interior apprehended approximately 55,300 more deportable aliens.<sup>[9]</sup> Most of the traffic-checking apprehensions were at checkpoints, though precise figures are not available. <i>United States</i> v. <span class="citation" data-id="1802688"><a href="/opinion/1802688/united-states-v-baca/#405" aria-description="Citation for case: United States v. Baca"><i>Baca, supra,</i> at 405, 407</a></span>, and n. 2.</p>
<p></p>
<h2>B</h2>
<p>We are concerned here with permanent checkpoints, the locations of which are chosen on the basis of a number of factors. The Border Patrol believes that to assure effectiveness, a checkpoint must be (i) distant enough from the border to avoid interference with traffic in populated areas near the border, (ii) close to the confluence of two or more significant roads leading away from the border, (iii) situated in terrain that restricts vehicle passage around the checkpoint, (iv) on a stretch of highway compatible with safe operation, and (v) beyond the 25-mile zone in which "border passes," see n. 7, <i>supra,</i> are valid. <i>United States</i> v. <span class="citation" data-id="1802688"><a href="/opinion/1802688/united-states-v-baca/#406" aria-description="Citation for case: United States v. Baca"><i>Baca, supra,</i> at 406</a></span>.</p>
<p><span class="star-pagination">*554</span> The record in No. 74-1560 provides a rather complete picture of the effectiveness of the San Clemente checkpoint. Approximately 10 million cars pass the checkpoint location each year, although the checkpoint actually is in operation only about 70% of the time.<sup>[10]</sup> In calendar year 1973, approximately 17,000 illegal aliens were apprehended there. During an eight-day period in 1974 that included the arrests involved in No. 74-1560, roughly 146,000 vehicles passed through the checkpoint during 124 1/6 hours of operation. Of these, 820 vehicles were referred to the secondary inspection area, where Border Patrol agents found 725 deportable aliens in 171 vehicles. In all but two cases, the aliens were discovered without a conventional search of the vehicle. A similar rate of apprehensions throughout the year would have resulted in an annual total of over 33,000, although the Government contends that many illegal aliens pass through the checkpoint undetected. The record in No. 75-5387 does not provide comparable statistical information regarding the Sarita checkpoint. While it appears that fewer illegal aliens are apprehended there, it may be assumed that fewer pass by undetected, as every motorist is questioned.</p>
<p></p>
<h2>III</h2>
<p>The Fourth Amendment imposes limits on search-and-seizure powers in order to prevent arbitrary and oppressive interference by enforcement officials with the privacy and personal security of individuals. See <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 878</a></span>; <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#895" aria-description="Citation for case: United States v. Ortiz">422 U. S., at 895</a></span>; <i>Camara</i> v. <i>Municipal Court,</i> <span class="star-pagination">*555</span> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span> (1967). In delineating the constitutional safeguards applicable in particular contexts, the Court has weighed the public interest against the Fourth Amendment interest of the individual, <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 878</a></span>; <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20-21</a></span> (1968), a process evident in our previous cases dealing with Border Patrol traffic-checking operations.</p>
<p>In <i>Almeida-Sanchez</i> v. <i>United States, supra</i><i>,</i> the question was whether a roving-patrol unit constitutionally could search a vehicle for illegal aliens simply because it was in the general vicinity of the border. We recognized that important law enforcement interests were at stake but held that searches by roving patrols impinged so significantly on Fourth Amendment privacy interests that a search could be conducted without consent only if there was probable cause to believe that a car contained illegal aliens, at least in the absence of a judicial warrant authorizing random searches by roving patrols in a given area. Compare <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#273" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S., at 273</a></span>, with <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#283" aria-description="Citation for case: Almeida-Sanchez v. United States"><i>id.,</i> at 283-285</a></span> (POWELL, J., concurring), and <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#288" aria-description="Citation for case: Almeida-Sanchez v. United States"><i>id.,</i> at 288</a></span> (WHITE, J., dissenting). We held in <i>United States</i> v. <i><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">Ortiz, supra</a></span></i><i>,</i> that the same limitations applied to vehicle searches conducted at a permanent checkpoint.</p>
<p>In <i>United States</i> v. <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce, supra</a></span></i><i>,</i> however, we recognized that other traffic-checking practices involve a different balance of public and private interests and appropriately are subject to less stringent constitutional safeguards. The question was under what circumstances a roving patrol could stop motorists in the general area of the border for brief inquiry into their residence status. We found that the interference with Fourth Amendment interests involved in such a stop was "modest," 422 U. S., at 880, while the inquiry served significant law enforcement needs. We therefore held that a roving-patrol stop need not be justified by probable <span class="star-pagination">*556</span> cause and may be undertaken if the stopping officer is "aware of specific articulable facts, together with rational inferences from those facts, that reasonably warrant suspicion" that a vehicle contains illegal aliens. <i>Id.,</i> at 884.<sup>[11]</sup></p>
<p></p>
<h2>IV</h2>
<p>It is agreed that checkpoint stops are "seizures" within the meaning of the Fourth Amendment. The defendants contend primarily that the routine stopping of vehicles at a checkpoint is invalid because <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> must be read as proscribing any stops in the absence of reasonable suspicion. Sifuentes alternatively contends in No. 75-5387 that routine checkpoint stops are permissible only when the practice has the advance judicial authorization of a warrant. There was a warrant authorizing the stops at San Clemente but none at Sarita. As we reach the issue of a warrant requirement only if reasonable suspicion is not required, we turn first to whether reasonable suspicion is a prerequisite to a valid stop, a question to be resolved by balancing the interests at stake.</p>
<p></p>
<h2>A</h2>
<p>Our previous cases have recognized that maintenance of a traffic-checking program in the interior is necessary because the flow of illegal aliens cannot be controlled effectively at the border. We note here only the substantiality of the public interest in the practice of routine stops for inquiry at permanent checkpoints, a practice which the Government identifies as the most important of the traffic-checking operations. Brief for United States in No. 74-1560, pp. 19-20.<sup>[12]</sup> These checkpoints <span class="star-pagination">*557</span> are located on important highways; in their absence such highways would offer illegal aliens a quick and safe route into the interior. Routine checkpoint inquiries apprehend many smugglers and illegal aliens who succumb to the lure of such highways. And the prospect of such inquiries forces others onto less efficient roads that are less heavily traveled, slowing their movement and making them more vulnerable to detection by roving patrols. Cf. <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#883" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 883-885</a></span>.</p>
<p>A requirement that stops on major routes inland always be based on reasonable suspicion would be impractical because the flow of traffic tends to be too heavy to allow the particularized study of a given car that would enable it to be identified as a possible carrier of illegal aliens. In particular, such a requirement would largely eliminate any deterrent to the conduct of well-disguised smuggling operations, even though smugglers are known to use these highways regularly.</p>
<p></p>
<h2>B</h2>
<p>While the need to make routine checkpoint stops is great, the consequent intrusion on Fourth Amendment interests is quite limited. The stop does intrude to a limited extent on motorists' right to "free passage without <span class="star-pagination">*558</span> interruption," <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#154" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 154</a></span> (1925), and arguably on their right to personal security. But it involves only a brief detention of travelers during which</p>
<blockquote>" `[a]ll that is required of the vehicle's occupants is a response to a brief question or two and possibly the production of a document evidencing a right to be in the United States.' " <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#880" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 880</a></span>.</blockquote>
<p>Neither the vehicle nor its occupants are searched, and visual inspection of the vehicle is limited to what can be seen without a search. This objective intrusionthe stop itself, the questioning, and the visual inspection also existed in roving-patrol stops. But we view checkpoint stops in a different light because the subjective intrusionthe generating of concern or even fright on the part of lawful travelersis appreciably less in the case of a checkpoint stop. In <i><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">Ortiz</a></span>,</i> we noted:</p>
<blockquote>"[T]he circumstances surrounding a checkpoint stop and search are far less intrusive than those attending a roving-patrol stop. Roving patrols often operate at night on seldom-traveled roads, and their approach may frighten motorists. At traffic checkpoints the motorist can see that other vehicles are being stopped, he can see visible signs of the officers' authority, and he is much less likely to be frightened or annoyed by the intrusion." 422 U. S., at 894-895.</blockquote>
<p>In <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span>,</i> we recognized that Fourth Amendment analysis in this context also must take into account the overall degree of interference with legitimate traffic. 422 U. S., at 882-883. We concluded there that random roving-patrol stops could not be tolerated because they "would subject the residents of . . . [border] areas to <span class="star-pagination">*559</span> potentially unlimited interference with their use of the highways, solely at the discretion of Border Patrol officers.. . . [They] could stop motorists at random for questioning, day or night, anywhere within 100 air miles of the 2,000-mile border, on a city street, a busy highway, or a desert road . . . ." <i>Ibid.</i> There also was a grave danger that such unreviewable discretion would be abused by some officers in the field. <i>Ibid.</i></p>
<p>Routine checkpoint stops do not intrude similarly on the motoring public. First, the potential interference with legitimate traffic is minimal. Motorists using these highways are not taken by surprise as they know, or may obtain knowledge of, the location of the checkpoints and will not be stopped elsewhere. Second, checkpoint operations both appear to and actually involve less discretionary enforcement activity. The regularized manner in which established checkpoints are operated is visible evidence, reassuring to law-abiding motorists, that the stops are duly authorized and believed to serve the public interest. The location of a fixed checkpoint is not chosen by officers in the field, but by officials responsible for making overall decisions as to the most effective allocation of limited enforcement resources. We may assume that such officials will be unlikely to locate a checkpoint where it bears arbitrarily or oppressively on motorists as a class. And since field officers may stop only those cars passing the checkpoint, there is less room for abusive or harassing stops of individuals than there was in the case of roving-patrol stops. Moreover, a claim that a particular exercise of discretion in locating or operating a checkpoint is unreasonable is subject to post-stop judicial review.<sup>[13]</sup></p>
<p><span class="star-pagination">*560</span> The defendants arrested at the San Clemente checkpoint suggest that its operation involves a significant extra element of intrusiveness in that only a small percentage of cars are referred to the secondary inspection area, thereby "stigmatizing" those diverted and reducing the assurances provided by equal treatment of all motorists. We think defendants overstate the consequences. Referrals are made for the sole purpose of conducting a routine and limited inquiry into residence status that cannot feasibly be made of every motorist where the traffic is heavy. The objective intrusion of the stop and inquiry thus remains minimal. Selective referral may involve some annoyance, but it remains true that the stops should not be frightening or offensive because of their public and relatively routine nature. Moreover, selective referralsrather than questioning the occupants of every cartend to advance some Fourth Amendment interests by minimizing the intrusion on the general motoring public.</p>
<p></p>
<h2>C</h2>
<p>The defendants note correctly that to accommodate public and private interests some quantum of individualized suspicion is usually a prerequisite to a constitutional search or seizure.<sup>[14]</sup> See <i>Terry</i> v. <i>Ohio,</i> 392 <span class="star-pagination">*561</span> U. S., at 21, and n. 18. But the Fourth Amendment imposes no irreducible requirement of such suspicion. This is clear from <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967). See also <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#283" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S., at 283-285</a></span> (POWELL, J., concurring); <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#288" aria-description="Citation for case: Almeida-Sanchez v. United States"><i>id.,</i> at 288</a></span> (WHITE, J., dissenting); <i>Colonnade Catering Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970); <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972); <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#154" aria-description="Citation for case: Carroll v. United States">267 U. S., at 154</a></span>. In <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> the Court required an "area" warrant to support the reasonableness of inspecting private residences within a particular area for building code violations, but recognized that "specific knowledge of the condition of the particular dwelling" was not required to enter any given residence. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#538" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 538</a></span>. In so holding, the Court examined the government interests advanced to justify such routine intrusions "upon the constitutionally protected interests of the private citizen," <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>id.,</i> at 534-535</a></span>, and concluded that under the circumstances the government interest outweighed those of the private citizen.</p>
<p>We think the same conclusion is appropriate here, where we deal neither with searches nor with the sanctity of private dwellings, ordinarily afforded the most stringent Fourth Amendment protection. See, <i>e. g., </i><i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span> (1948). As we have noted earlier, one's expectation of privacy in an automobile and of freedom in its operation are significantly different from the traditional expectation of privacy and freedom in one's residence. <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">422 U. S., at 896</a></span> n. 2; see <i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590-591</a></span> (1974) (plurality <span class="star-pagination">*562</span> opinion). And the reasonableness of the procedures followed in making these checkpoint stops makes the resulting intrusion on the interests of motorists minimal. On the other hand, the purpose of the stops is legitimate and in the public interest, and the need for this enforcement technique is demonstrated by the records in the cases before us. Accordingly, we hold that the stops and questioning at issue may be made in the absence of any individualized suspicion at reasonably located checkpoints.<sup>[15]</sup></p>
<p><span class="star-pagination">*563</span> We further believe that it is constitutional to refer motorists selectively to the secondary inspection area at the San Clemente checkpoint on the basis of criteria that would not sustain a roving-patrol stop. Thus, even if it be assumed that such referrals are made largely on the basis of apparent Mexican ancestry,<sup>[16]</sup> we perceive no constitutional violation. Cf. <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#885" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 885-887</a></span>. As the intrusion here is sufficiently minimal that no particularized reason need exist to justify it, we think it follows that the Border Patrol <span class="star-pagination">*564</span> officers must have wide discretion in selecting the motorists to be diverted for the brief questioning involved.<sup>[17]</sup></p>
<p></p>
<h2>V</h2>
<p>Sifuentes' alternative argument is that routine stops at a checkpoint are permissible only if a warrant has given judicial authorization to the particular checkpoint location and the practice of routine stops. A warrant requirement in these circumstances draws some support from <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span>,</i> where the Court held that, absent consent, an "area" warrant was required to make a building code inspection, even though the search could be conducted absent cause to believe that there were violations in the building searched.<sup>[18]</sup></p>
<p>We do not think, however, that <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> is an apt <span class="star-pagination">*565</span> model. It involved the search of private residences, for which a warrant traditionally has been required. See, <i>e. g., </i><i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span> (1948). As developed more fully above, the strong Fourth Amendment interests that justify the warrant requirement in that context are absent here. The degree of intrusion upon privacy that may be occasioned by a search of a house hardly can be compared with the minor interference with privacy resulting from the mere stop for questioning as to residence. Moreover, the warrant requirement in <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> served specific Fourth Amendment interests to which a warrant requirement here would make little contribution. The Court there said:</p>
<blockquote>"[W]hen [an] inspector [without a warrant] demands entry, the occupant has no way of knowing whether enforcement of the municipal code involved requires inspection of his premises, no way of knowing the lawful limits of the inspector's power to search, and no way of knowing whether the inspector himself is acting under proper authorization." <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 532</a></span>.</blockquote>
<p>A warrant provided assurance to the occupant on these scores. We believe that the visible manifestations of the field officers' authority at a checkpoint provide substantially the same assurances in this case.</p>
<p>Other purposes served by the requirement of a warrant also are inapplicable here. One such purpose is to prevent hindsight from coloring the evaluation of the reasonableness of a search or seizure. Cf. <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#455" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 455-456, n. 22</a></span> (1976) (MARSHALL, J., dissenting). The reasonableness of checkpoint stops, however, turns on factors such as the location and method of operation of the checkpoint, factors that are not susceptible to the distortion of hindsight, and therefore will be open to post-stop review notwithstanding <span class="star-pagination">*566</span> the absence of a warrant. Another purpose for a warrant requirement is to substitute the judgment of the magistrate for that of the searching or seizing officer. <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#316" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 316-318</a></span> (1972). But the need for this is reduced when the decision to "seize" is not entirely in the hands of the officer in the field, and deference is to be given to the administrative decisions of higher ranking officials.</p>
<p></p>
<h2>VI</h2>
<p>In summary, we hold that stops for brief questioning routinely conducted at permanent checkpoints are consistent with the Fourth Amendment and need not be authorized by warrant.<sup>[19]</sup> The principal protection of Fourth <span class="star-pagination">*567</span> Amendment rights at checkpoints lies in appropriate limitations on the scope of the stop. See <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 24-27</a></span>; <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 881-882</a></span>. We have held that checkpoint searches are constitutional only if justified by consent or probable cause to search. <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891</a></span> (1975). And our holding today is limited to the type of stops described in this opinion. "[A]ny further detention . . . must be based on consent or probable cause." <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#882" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 882</a></span>. None of the defendants in these cases argues that the stopping officers exceeded these limitations. Consequently, we affirm the judgment of the Court of Appeals for the Fifth Circuit, which had affirmed the conviction of Sifuentes. We reverse the judgment of the Court of Appeals for the Ninth Circuit and remand the case with directions to affirm the conviction of Martinez-Fuerte and to remand the other cases to the District Court for further proceedings.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE BRENNAN, with whom MR. JUSTICE MARSHALL joins, dissenting.</p>
<p>Today's decision is the ninth this Term marking the continuing evisceration of Fourth Amendment protections against unreasonable searches and seizures. Early in the Term, <i>Texas</i> v. <i>White,</i> <span class="citation" data-id="9426226"><a href="/opinion/109332/texas-v-white/" aria-description="Citation for case: Texas v. White">423 U. S. 67</a></span> (1975), permitted the warrantless search of an automobile in police custody despite the unreasonableness of the custody <span class="star-pagination">*568</span> and opportunity to obtain a warrant. <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976), held that regardless of whether opportunity exists to obtain a warrant, an arrest in a public place for a previously committed felony never requires a warrant, a result certainly not fairly supported by either history or precedent. See <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#433" aria-description="Citation for case: United States v. Watson"><i>id.,</i> at 433</a></span> (MARSHALL, J., dissenting). <i>United States</i> v. <i>Santana,</i> <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">427 U. S. 38</a></span> (1976), went further and approved the warrantless arrest for a felony of a person standing on the front porch of her residence. <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">425 U. S. 435</a></span> (1976), narrowed the Fourth Amendment's protection of privacy by denying the existence of a protectible interest in the compilation of checks, deposit slips, and other records pertaining to an individual's bank account. <i>Stone</i> v. <i>Powell, ante,</i> p. 465, precluded the assertion of Fourth Amendment claims in federal collateral relief proceedings. <i>United States</i> v. <i>Janis, ante,</i> p. 433, held that evidence unconstitutionally seized by a state officer is admissible in a civil proceeding by or against the United States. <i>South Dakota</i> v. <i>Opperman, ante,</i> p. 364, approved sweeping inventory searches of automobiles in police custody irrespective of the particular circumstances of the case. Finally, in <i>Andresen</i> v. <i>Maryland,</i> <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">427 U. S. 463</a></span> (1976), the Court, in practical effect, weakened the Fourth Amendment prohibition against general warrants.</p>
<p>Consistent with this purpose to debilitate Fourth Amendment protections, the Court's decision today virtually empties the Amendment of its reasonableness requirement by holding that law enforcement officials manning fixed checkpoint stations who make standardless seizures of persons do not violate the Amendment. This holding cannot be squared with this Court's recent decisions in <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891</a></span> (1975); <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975); <span class="star-pagination">*569</span> and <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973). I dissent.</p>
<p>While the requisite justification for permitting a search or seizure may vary in certain contexts, compare <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span> (1964), with <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), and <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967), even in the exceptional situations permitting intrusions on less than probable cause, it has long been settled that justification must be measured by objective standards. Thus in the seminal decision justifying intrusions on less-than-probable cause, <i>Terry</i> v. <i>Ohio, supra</i><i>,</i> the Court said:</p>
<blockquote>"The scheme of the Fourth Amendment becomes meaningful only when it is assured that at some point the conduct of those charged with enforcing the laws can be subjected to the more detached, neutral scrutiny of a judge who must evaluate the reasonableness of a particular search or seizure in light of the particular circumstances. And in making that assessment it is imperative that the facts be judged against an <i>objective standard</i> . . . . Anything less would invite intrusions upon constitutionally guaranteed rights based on nothing more substantial than inarticulate hunches, a result this Court has consistently refused to sanction." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 21-22</a></span> (emphasis added, footnote omitted).</blockquote>
<blockquote>"This demand for specificity in the information upon which police action is predicated is the central teaching of this Court's Fourth Amendment jurisprudence." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 21</a></span> n. 18.</blockquote>
<p><i>Terry</i> thus made clear what common sense teaches: Conduct, to be reasonable, must pass muster under objective standards applied to specific facts.</p>
<p>We are told today, however, that motorists without number may be individually stopped, questioned, visually <span class="star-pagination">*570</span> inspected, and then further detained without even a showing of articulable suspicion, see <i>ante,</i> at 547, let alone the heretofore constitutional minimum of reasonable suspicion, a result that permits search and seizure to rest upon "nothing more substantial than inarticulate hunches." This defacement of Fourth Amendment protections is arrived at by a balancing process that overwhelms the individual's protection against unwarranted official intrusion by a governmental interest said to justify the search and seizure. But that method is only a convenient cover for condoning arbitrary official conduct, for the governmental interests relied on as warranting intrusion here are the same as those in <i><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">Almeida-Sanchez</a></span></i> and <i><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">Ortiz</a></span>,</i> which required a showing of probable cause for roving-patrol and fixed checkpoint searches, and <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span>,</i> which required at least a showing of reasonable suspicion based on specific articulable facts to justify roving-patrol stops. Absent some difference in the nature of the intrusion, the same minimal requirement should be imposed for checkpoint stops.</p>
<p>The Court assumes, and I certainly agree, that persons stopped at fixed checkpoints, whether or not referred to a secondary detention area, are "seized" within the meaning of the Fourth Amendment. Moreover, since the vehicle and its occupants are subjected to a "visual inspection," the intrusion clearly exceeds mere physical restraint, for officers are able to see more in a stopped vehicle than in vehicles traveling at normal speeds down the highway. As the Court concedes, <i>ante,</i> at 558, the checkpoint stop involves essentially the same intrusions as a roving-patrol stop, yet the Court provides no principled basis for distinguishing checkpoint stops.</p>
<p>Certainly that basis is not provided in the Court's reasoning that the subjective intrusion here is appreciably less than in the case of a stop by a roving patrol. <span class="star-pagination">*571</span> <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> nowhere bases the requirement of reasonable suspicion upon the subjective nature of the intrusion. In any event, the subjective aspects of checkpoint stops, even if different from the subjective aspects of roving-patrol stops, just as much require some principled restraint on law enforcement conduct. The motorist whose conduct has been nothing but innocent and this is overwhelmingly the casesurely resents his own detention and inspection. And checkpoints, unlike roving stops, detain thousands of motorists, a dragnetlike procedure offensive to the sensibilities of free citizens. Also, the delay occasioned by stopping hundreds of vehicles on a busy highway is particularly irritating.</p>
<p>In addition to overlooking these dimensions of subjective intrusion, the Court, without explanation, also ignores one major source of vexation. In abandoning any requirement of a minimum of reasonable suspicion, or even articulable suspicion, the Court in every practical sense renders meaningless, as applied to checkpoint stops, the <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> holding that "standing alone [Mexican appearance] does not justify stopping all Mexican-Americans to ask if they are aliens."<sup>[1]</sup> 422 <span class="star-pagination">*572</span> U. S., at 887. Since the objective is almost entirely the Mexican illegally in the country, checkpoint officials, uninhibited by any objective standards and therefore free to stop any or all motorists without explanation or excuse, wholly on whim, will perforce target motorists of Mexican appearance. The process will then inescapably discriminate against citizens of Mexican ancestry and Mexican aliens lawfully in this country for no other reason than that they unavoidably possess the same "suspicious" physical and grooming characteristics of illegal Mexican aliens.</p>
<p>Every American citizen of Mexican ancestry and every Mexican alien lawfully in this country must know after today's decision that he travels the fixed checkpoint highways at the risk of being subjected not only to a stop, but also to detention and interrogation, both prolonged and to an extent far more than for non-Mexican appearing motorists. To be singled out for referral and to be detained and interrogated must be upsetting to any motorist. One wonders what actual experience supports my Brethren's conclusion that referrals "should not be frightening or offensive because of their public and relatively routine nature." <i>Ante,</i> at 560.<sup>[2]</sup> In point of fact, referrals, <span class="star-pagination">*573</span> viewed in context, are not relatively routine; thousands are otherwise permitted to pass. But for the arbitrarily selected motorists who must suffer the delay and humiliation of detention and interrogation, the experience can obviously be upsetting.<sup>[3]</sup> And that experience is particularly vexing for the motorist of Mexican ancestry who is selectively referred, knowing that the officers' target is the Mexican alien. That deep resentment will be stirred by a sense of unfair discrimination is not difficult to foresee.<sup>[4]</sup></p>
<p><span class="star-pagination">*574</span> In short, if a balancing process is required, the balance should be struck, as in <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span>,</i> to require that Border Patrol officers act upon at least reasonable suspicion in making checkpoint stops. In any event, even if a different balance were struck, the Court cannot, without ignoring the Fourth Amendment requirement of reasonableness, justify wholly unguided seizures by officials manning the checkpoints. The Court argues, however, that practicalities necessitate otherwise: "A requirement that stops on major routes inland always be based on reasonable suspicion would be impractical because the flow of traffic tends to be too heavy to allow the particularized study of a given car that would enable it to be identified as a possible carrier of illegal aliens." <i>Ante,</i> at 557.</p>
<p>As an initial matter, whatever force this argument may have, it cannot apply to the secondary detentions that occurred in No. 74-1560. Once a vehicle has been slowed and observed at a checkpoint, ample opportunity <span class="star-pagination">*575</span> exists to formulate the reasonable suspicion which, if it actually exists, would justify further detention. Indeed, though permitting roving stops based on reasonable suspicion, <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> required that "any further detention or search must be based on [the greater showing of] consent or probable cause." 422 U. S., at 882. The Court today, however, does not impose a requirement of even reasonable suspicion for these secondary stops.</p>
<p>The Court's rationale is also not persuasive because several of the factors upon which officers may rely in establishing reasonable suspicion are readily ascertainable, regardless of the flow of traffic. For example, with checkpoint stops as with roving-patrol stops, "[a]spects of the vehicle itself may justify suspicion." <i>Id.,</i> at 885. Thus it is relevant that the vehicle is a certain type of station wagon, appears to be heavily loaded, contains an extraordinary number of persons, or contains persons trying to hide. See <i>ibid.</i> If such factors are satisfactory to permit the imposition of a reasonable-suspicion requirement in the more demanding circumstances of a roving patrol, where officers initially deal with a vehicle traveling, not at a crawl, but at highway speeds, they clearly should suffice in the circumstances of a checkpoint stop.</p>
<p>Finally, the Court's argument fails for more basic reasons. There is no principle in the jurisprudence of fundamental rights which permits constitutional limitations to be dispensed with merely because they cannot be conveniently satisfied. Dispensing with reasonable suspicion as a prerequisite to stopping and inspecting motorists because the inconvenience of such a requirement would make it impossible to identify a given car as a possible carrier of aliens is no more justifiable than dispensing with probable cause as prerequisite to the search of an individual because the inconvenience of <span class="star-pagination">*576</span> such a requirement would make it impossible to identify a given person in a high-crime area as a possible carrier of concealed weapons. "The needs of law enforcement stand in constant tension with the Constitution's protections of the individual against certain exercises of official power. It is precisely the predictability of these pressures that counsels a resolute loyalty to constitutional safeguards." <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#273" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S., at 273</a></span>.</p>
<p>The Court also attempts to justify its approval of standardless conduct on the ground that checkpoint stops "involve less discretionary enforcement activity" than roving stops. <i>Ante,</i> at 559. This view is at odds with its later more revealing statement that "officers must have wide discretion in selecting the motorists to be diverted for the brief questioning involved." <i>Ante,</i> at 564. Similarly unpersuasive is the statement that "since field officers may stop only those cars passing the checkpoint, there is less room for abusive or harassing stops of individuals than there was in the case of roving-patrol stops." <i>Ante,</i> at 559.<sup>[5]</sup> The Fourth Amendment standard <span class="star-pagination">*577</span> of reasonableness admits of neither intrusion at the discretion of law enforcement personnel nor abusive or harassing stops, however infrequent. Action based merely on whatever may pique the curiosity of a particular officer is the antithesis of the objective standards requisite to reasonable conduct and to avoiding abuse and harassment. Such action, which the Court now permits, has expressly been condemned as contrary to basic Fourth Amendment principles. Certainly today's holding is far removed from the proposition emphatically affirmed in <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#317" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 317</a></span> (1972), that "those charged with . . . investigative and prosecutorial duty should not be the sole judges of when to utilize constitutionally sensitive means in pursuing their tasks. The historical judgment, which the Fourth Amendment accepts, is that unreviewed executive discretion may yield too readily to pressures to obtain incriminating evidence and overlook potential invasions of privacy . . . ." Indeed, it is far removed from the even more recent affirmation that "the central concern of the Fourth Amendment is to protect liberty and privacy from arbitrary and oppressive interference by government officials." <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#895" aria-description="Citation for case: United States v. Ortiz">422 U. S., at 895</a></span>.<sup>[6]</sup></p>
<p><span class="star-pagination">*578</span> The cornerstone of this society, indeed of any free society, is orderly procedure. The Constitution, as originally adopted, was therefore, in great measure, a procedural document. For the same reasons the drafters of the Bill of Rights largely placed their faith in procedural limitations on government action. The Fourth Amendment's requirement that searches and seizures be reasonable enforces this fundamental understanding in erecting its buffer against the arbitrary treatment of citizens by government. But to permit, as the Court does today, police discretion to supplant the objectivity of reason and, thereby, expediency to reign in the place of order, is to undermine Fourth Amendment safeguards and threaten erosion of the cornerstone of our system of a government, for, as Mr. Justice Frankfurter reminded us, "[t]he history of American freedom is, in no small measure, the history of procedure." <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#414" aria-description="Citation for case: Malinski v. New York">324 U. S. 401, 414</a></span> (1945).</p>
<h2>NOTES</h2>
<p>[*]  Together with No. 75-5387, <i>Sifuentes</i> v. <i>United States,</i> on certiorari to the United States Court of Appeals for the Fifth Circuit.</p>
<p>[]  <i>Melvin L. Wulf, Joel M. Gora, Vilma S. Martinez, Sanford J. Rosen,</i> and <i>Jerome B. Falk, Jr.,</i> filed a brief for the American Civil Liberties Union et al. as <i>amici curiae</i> urging affirmance in No. 74-1560.</p>
<p>[1]  The parties disagree as to whether vehicles not referred to the secondary inspection area are brought to a complete halt or merely "roll" slowly through the checkpoint. Resolution of this dispute is not necessary here, as we may assume, <i>arguendo,</i> that all motorists passing through the checkpoint are so slowed as to have been "seized."</p>
<p>[2]  The record does not reveal explicitly why a warrant was sought. Shortly before the warrant application, however, the Court of Appeals for the Ninth Circuit had held unconstitutional a routine stop and search conducted at a permanent checkpoint without such a warrant. See <i>United States</i> v. <i>Bowen,</i> <span class="citation" data-id="9460842"><a href="/opinion/320688/united-states-v-john-lee-bowen/" aria-description="Citation for case: United States v. John Lee Bowen">500 F. 2d 960</a></span> (1974), aff'd on other grounds, <span class="citation" data-id="109313"><a href="/opinion/109313/bowen-v-united-states/" aria-description="Citation for case: Bowen v. United States">422 U. S. 916</a></span> (1975); <i>United States</i> v. <i>Juarez-Rodriguez,</i> <span class="citation" data-id="319859"><a href="/opinion/319859/united-states-v-camilo-juarez-rodriguez/" aria-description="Citation for case: United States v. Camilo Juarez-Rodriguez">498 F. 2d 7</a></span> (1974). Soon after the warrant issued, the Court of Appeals also held unconstitutional routine checkpoint stops conducted without a warrant. See <i>United States</i> v. <i>Esquer-Rivera,</i> <span class="citation" data-id="320555"><a href="/opinion/320555/united-states-v-laura-elena-esquer-rivera-united-states-of-america-v/" aria-description="Citation for case: United States v. Laura Elena Esquer-Rivera, United States...">500 F. 2d 313</a></span> (1974). See also n. 15, <i>infra.</i></p>
<p>[3]  Each of the defendants in No. 74-1560 and the defendant in No. 75-5387 sought to suppress, among other things, the testimony of one or more illegal aliens. We noted in <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span>, 876 n. 2 (1975), that "[t]here may be room to question whether voluntary testimony of a witness at trial, as opposed to a Government agent's testimony about objects seized or statements overheard, is subject to suppression . . . ." The question again is not before us.</p>
<p>[4]  The prosecution of Martinez-Fuerte was before a different District Judge than were the other cases.</p>
<p>[5]  The principal question before the Court of Appeals was the constitutional significance of the "warrant of inspection" under which the checkpoint was operating when the defendants were stopped. See n. 15, <i>infra.</i> The Government, however, preserved the question whether routine checkpoint stops could be made absent a warrant.</p>
<p>[6]  We initially granted the Government's petition for a writ of certiorari in No. 74-1560, <span class="citation multiple-matches"><a href="/c/U.%20S./423/822/">423 U. S. 822</a></span>, and later granted Sifuentes' petition in No. 75-5387 and directed that the cases be argued in tandem. <span class="citation multiple-matches"><a href="/c/U.%20S./423/945/">423 U. S. 945</a></span>. Subsequently we granted the motion of the Solicitor General to consolidate the cases for oral argument. <span class="citation multiple-matches"><a href="/c/U.%20S./425/931/">425 U. S. 931</a></span>.</p>
<p>[7]  The latter occurs particularly where "border passes" are issued to simplify passage between interrelated American and Mexican communities along the border. These passes authorize travel within 25 miles of the border for a 72-hour period. See <span class="citation no-link">8 CFR § 212.6</span> (1976).</p>
<p>[8]  All these operations are conducted pursuant to statutory authorizations empowering Border Patrol agents to interrogate those believed to be aliens as to their right to be in the United States and to inspect vehicles for aliens. <span class="citation no-link">8 U. S. C. §§ 1357</span> (a) (1), (a) (3). Under current regulations the authority conferred by § 1357 (a) (3) may be exercised anywhere within 100 air miles of the border. <span class="citation no-link">8 CFR § 287.1</span> (a) (1976).</p>
<p>[9]  As used in these statistics, the term "deportable alien" means "a person who has been found to be deportable by an immigration judge, or who admits his deportability upon questioning by official agents." <i>United States</i> v. <i>Baca,</i> <span class="citation" data-id="1802688"><a href="/opinion/1802688/united-states-v-baca/#404" aria-description="Citation for case: United States v. Baca">368 F. Supp. 398, 404</a></span> (SD Cal. 1973). Most illegal aliens are simply deported without prosecution. The Government routinely prosecutes persons though to be smugglers, many of whom are lawfully in the United States.</p>
<p>[10]  The Sarita checkpoint is operated a comparable proportion of the time. "Down" periods are caused by personnel shortages, weather conditions, andat San Clementepeak traffic loads.</p>
<p>[11]  On the facts of the case, we concluded that the stop was impermissible because reasonable suspicion was lacking.</p>
<p>[12]  The defendants argue at length that the public interest in maintaining checkpoints is less than is asserted by the Government because the flow of illegal immigrants could be reduced by means other than checkpoint operations. As one alternative they suggest legislation prohibiting the knowing employment of illegal aliens. The logic of such elaborate less-restrictive-alternative arguments could raise insuperable barriers to the exercise of virtually all search-and-seizure powers. In any event, these arguments tend to go to the general proposition that all traffic-checking procedures are impermissible, a premise our previous cases reject. The defendants do not suggest persuasively that the particular law enforcement needs served by checkpoints could be met without reliance on routine checkpoint stops. Compare <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#883" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 883</a></span> (effectiveness of roving patrols not defeated by reasonable suspicion requirement), with <i>infra,</i> this page.</p>
<p>[13]  The choice of checkpoint locations must be left largely to the discretion of Border Patrol officials, to be exercised in accordance with statutes and regulations that may be applicable. See n. 15, <i>infra.</i> Many incidents of checkpoint operation also must be committed to the discretion of such officials. But see <i>infra,</i> at 565-566.</p>
<p>[14]  Stops for questioning, not dissimilar to those involved here, are used widely at state and local levels to enforce laws regarding drivers' licenses, safety requirements, weight limits, and similar matters. The fact that the purpose of such laws is said to be administrative is of limited relevance in weighing their intrusiveness on one's right to travel; and the logic of the defendant's position, if realistically pursued, might prevent enforcement officials from stopping motorists for questioning on these matters in the absence of reasonable suspicion that a law was being violated. As such laws are not before us, we intimate no view respecting them other than to note that this practice of stopping automobiles briefly for questioning has a long history evidencing its utility and is accepted by motorists as incident to highway use.</p>
<p>[15]  As a judicial warrant authorized the Border Patrol to make routine stops at the San Clemente checkpoint, the principal question addressed by the Court of Appeals for the Ninth Circuit in No. 74-1560 was whether routine checkpoint stops were constitutional when authorized by warrant. Cf. n. 5, <i>supra.</i> The Court of Appeals held alternatively that a warrant never could authorize such stops, <span class="citation multiple-matches"><a href="/c/F.%202d/514/308/">514 F. 2d 308</a></span>, 318 (1975), and that it was unreasonable to issue a warrant authorizing routine stops at the San Clemente location. <i>Id.,</i> at 321-322. In reaching the latter conclusion, the Court of Appeals relied on (i) "the [low] frequency with which illegal aliens pass through the San Clemente checkpoint," (ii) the distance of the checkpoint from the border, and (iii) the interference with legitimate traffic. <i>Ibid.</i> We need not address these holdings specifically, as we conclude that no warrant is needed. But we deem the argument by the defendants in No. 74-1560 in support of the latter holding to raise the question whether, even though a warrant is not required, it is unreasonable to locate a checkpoint at San Clemente.
</p>
<p>We answer this question in the negative. As indicated above, the choice of checkpoint locations is an administrative decision that must be left largely within the discretion of the Border Patrol, see n. 13, <i>supra;</i> cf. <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#538" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 538</a></span> (1967). We think the decision to locate a checkpoint at San Clemente was reasonable. The location meets the criteria prescribed by the Border Patrol to assure effectiveness, see <i>supra,</i> at 553, and the evidence supports the view that the needs of law enforcement are furthered by this location. The absolute number of apprehensions at the checkpoint is high, see <i>supra,</i> at 554, confirming Border Patrol judgment that significant numbers of illegal aliens regularly use Interstate 5 at this point. Also, San Clemente was selected as the location where traffic is lightest between San Diego and Los Angeles, thereby minimizing interference with legitimate traffic.</p>
<p>No question has been raised about the reasonableness of the location of the Sarita checkpoint.</p>
<p>[16]  The Government suggests that trained Border Patrol agents rely on factors in addition to apparent Mexican ancestry when selectively diverting motorists. Brief for United States in No. 75-5387, p. 9; see <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 884-885</a></span>. This assertion finds support in the record. Less than 1% of the motorists passing the checkpoint are stopped for questioning, whereas American citizens of Mexican ancestry and legally resident Mexican citizens constitute a significantly larger proportion of the population of southern California. The 1970 census figures, which may not fully reflect illegal aliens, show the population of California to be approximately 19,958,000 of whom some 3,102,000, or 16%, are Spanish-speaking or of Spanish surname. The equivalent percentages for metropolitan San Diego and Los Angeles are 13% and 18% respectively. U. S. Department of Commerce, 1970 Census of Population, vol. 1, pt. 6, Tables 48, 140. If the statewide population ratio is applied to the approximately 146,000 vehicles passing through the checkpoint during the eight days surrounding the arrests in No. 74-1560, roughly 23,400 would be expected to contain persons of Spanish or Mexican ancestry, yet only 820 were referred to the secondary area. This appears to refute any suggestion that the Border Patrol relies extensively on apparent Mexican ancestry standing alone in referring motorists to the secondary area.</p>
<p>[17]  Of the 820 vehicles referred to the secondary inspection area during the eight days surrounding the arrests involved in No. 74-1560, roughly 20% contained illegal aliens. <i>Supra,</i> at 554. Thus, to the extent that the Border Patrol relies on apparent Mexican ancestry at this checkpoint, see n. 16, <i>supra,</i> that reliance clearly is relevant to the law enforcement need to be served. Cf. <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#886" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 886-887</a></span>, where we noted that "[t]he likelihood that any given person of Mexican ancestry is an alien is high enough to make Mexican appearance a relevant factor . . . ," although we held that apparent Mexican ancestry by itself could not create the reasonable suspicion required for a roving-patrol stop. Different considerations would arise if, for example, reliance were put on apparent Mexican ancestry at a checkpoint operated near the Canadian border.</p>
<p>[18]  There also is some support for a warrant requirement in the concurring and dissenting opinions in <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973), which commanded the votes of five Justices. See <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#283" aria-description="Citation for case: Almeida-Sanchez v. United States"><i>id.,</i> at 283-285</a></span> (POWELL, J., concurring); <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#288" aria-description="Citation for case: Almeida-Sanchez v. United States"><i>id.,</i> at 288</a></span> (WHITE, J., dissenting). The burden of these opinions, however, was that an "area" warrant could serve as a substitute for the individualized probable cause to search that otherwise was necessary to sustain roving-patrol searches. As particularized suspicion is not necessary here, the warrant function discussed in <i><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">Almeida-Sanchez</a></span></i> is not an issue in these cases.</p>
<p>[19]  MR. JUSTICE BRENNAN'S dissenting opinion reflects unwarranted concern in suggesting that today's decision marks a radical new intrusion on citizens' rights: It speaks of the "evisceration of Fourth Amendment protections," and states that the Court "virtually empties the Amendment of its reasonableness requirement." <i>Post,</i> at 567, 568. Since 1952, Act of June 27, 1952, <span class="citation no-link">66 Stat. 233</span>, Congress has expressly authorized persons believed to be aliens to be interrogated as to residence, and vehicles "within a reasonable distance" from the border to be searched for aliens. See n. 8, <i>supra.</i> The San Clemente checkpoint has been operating at or near its present location throughout the intervening 24 years. Our prior cases have limited significantly the reach of this congressional authorization, requiring probable cause for any vehicle search in the interior and reasonable suspicion for inquiry stops by roving patrols. See <i>supra,</i> at 555-556. Our holding today, approving routine stops for brief questioning (a type of stop familiar to all motorists) is confined to permanent checkpoints. We understand, of course, that neither longstanding congressional authorization nor widely prevailing practice justifies a constitutional violation. We do suggest, however, that against this background and in the context of our recent decisions, the rhetoric of the dissent reflects unjustified concern.
</p>
<p>The dissenting opinion further warns:</p>
<p>"Every American citizen of Mexican ancestry and every Mexican alien lawfully in this country must know after today's decision that he travels the fixed checkpoint highways at [his] risk . . . ." <i>Post,</i> at 572.</p>
<p>For the reason stated in n. 16, <i>supra,</i> this concern is misplaced. Moreover, upon a proper showing, courts would not be powerless to prevent the misuse of checkpoints to harass those of Mexican ancestry.</p>
<p>[1]  <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span>,</i> which involved roving-patrol stops, said:
</p>
<p>"[Mexican ancestry] alone would justify neither a reasonable belief that they were aliens, nor a reasonable belief that the car concealed other aliens who were illegally in the country. Large numbers of native-born and naturalized citizens have the physical characteristics identified with Mexican ancestry, and even in the border area a relatively small proportion of them are aliens. The likelihood that any given person of Mexican ancestry is an alien is high enough to make Mexican appearance a relevant factor, but standing alone it does not justify stopping all Mexican-Americans to ask if they are aliens." 422 U. S., at 886-887 (footnote omitted).</p>
<p>Today we are told that secondary referrals may be based on criteria that would not sustain a roving-patrol stop, and specifically that such referrals may be based largely on Mexican ancestry. <i>Ante,</i> at 563. Even if the difference between <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> and this decision is only a matter of degree, we are not told what justifies the different treatment of Mexican appearance or why greater emphasis is permitted in the less demanding circumstances of a checkpoint. That law in this country should tolerate use of one's ancestry as probative of possible criminal conduct is repugnant under any circumstances.</p>
<p>[2]  The Court's view that "selective referralsrather than questioning the occupants of every cartend to advance some Fourth Amendment interests by minimizing the intrusion on the general motoring public," <i>ante,</i> at 560, stands the Fourth Amendment on its head. The starting point of this view is the unannounced assumption that intrusions are generally permissible; hence, any minimization of intrusions serves Fourth Amendment interests. Under the Fourth Amendment, however, the status quo is nonintrusion, for as a general matter, it is unreasonable to subject the average citizen or his property to search or seizure. Thus, minimization of intrusion only lessens the aggravation to Fourth Amendment interest; it certainly does not further those interests.</p>
<p>[3]  <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891</a></span> (1975), expressly recognized that such selectivity is a source of embarrassment: "Nor do checkpoint procedures significantly reduce the likelihood of embarrassment. Motorists whose cars are searched, unlike those who are only questioned, may not be reassured by seeing that the Border Patrol searches other cars as well." <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#895" aria-description="Citation for case: United States v. Ortiz"><i>Id.,</i> at 895</a></span>.</p>
<p>[4]  Though today's decision would clearly permit detentions to be based solely on Mexican ancestry, the Court takes comfort in what appears to be the Border Patrol practice of not relying on Mexican ancestry standing alone in referring motorists for secondary detentions. <i>Ante,</i> at 563 n. 16. See also <i>ante,</i> at 566-567, n. 19. Good faith on the part of law enforcement officials, however, has never sufficed in this tribunal to substitute as a safeguard for personal freedoms or to remit our duty to effectuate constitutional guarantees. Indeed, with particular regard to the Fourth Amendment, <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 22</a></span> (1968), held that "simple `"good faith on the part of the arresting officer is not enough." . . . If subjective good faith alone were the test, the protections of the Fourth Amendment would evaporate, and the people would be "secure in their persons, houses, papers, and effects," only in the discretion of the police.' <i>Beck</i> v. <i>Ohio,</i> [<span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span>,] 97 [1964]."
</p>
<p>Even if good faith is assumed, the affront to the dignity of American citizens of Mexican ancestry and Mexican aliens lawfully within the country is in no way diminished. The fact still remains that people of Mexican ancestry are targeted for examination at checkpoints and that the burden of checkpoint intrusions will lie heaviest on them. That, as the Court observes, <i>ante,</i> at 563 n. 16, "[l]ess than 1% of the motorists passing the checkpoint are stopped for questioning," whereas approximately 16% of the population of California is Spanish-speaking or of Spanish surname, has little bearing on this pointor, for that matter, on the integrity of Border Patrol practices. There is no indication how many of the 16% have physical and grooming characteristics identifiable as Mexican. There is no indication what portion of the motoring public in California is of Spanish or Mexican ancestry. Given the socioeconomic status of this portion, it is likely that the figure is significantly less than 16%. Neither is there any indication that those of Mexican ancestry are not subjected to lengthier initial stops than others, even if they are not secondarily detained. Finally, there is no indication of the ancestral makeup of the 1% who are referred for secondary detention. If, as is quite likely the case, it is overwhelmingly Mexican, the sense of discrimination which will be felt is only enhanced.</p>
<p>[5]  As an empirical proposition, this observation is hardly self-evident. No small number of vehicles pass through a checkpoint. Indeed, better than 1,000 pass through the San Clemente checkpoint during each hour of operation. <i>Ante,</i> at 554. Thus there is clearly abundant opportunity for abuse and harassment at checkpoints through lengthier detention and questioning of some individuals or arbitrary secondary detentions. Such practices need not be confined to those of Mexican ancestry. And given that it is easier to deal with a vehicle which has already been slowed than it is to observe and then chase and apprehend a vehicle travelling at highway speeds, if anything, there is more, not less, room for abuse or harassment at checkpoints. Indeed, in <i><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">Ortiz</a></span>,</i> the Court was "not persuaded that the checkpoint limits to any meaningful extent the officer's discretion to select cars for search." 422 U. S., at 895. <i>A fortiori,</i> discretion can be no more limited simply because the activity is detention or questioning rather than searching.</p>
<p>[6]  <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967), does not support the Court's result. Contrary to the Court's characterization, <i>ante,</i> at 561, the searches condoned there were not "routine intrusions." The Court required that administrative searches proceed according to reasonable standards satisfied with respect to each particular dwelling searched. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#538" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 538</a></span>. The search of any dwelling at the whim of administrative personal was not permitted. The Court, however, imposes no such standards today. Instead, any vehicle and its passengers are subject to detention at a fixed checkpoint, and "no particularized reason need exist to justify" the detention. <i>Ante,</i> at 563. To paraphrase an apposite observation by the Court in <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#270" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 270</a></span> (1973), "[checkpoints] thus embodied precisely the evil the Court saw in <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> when it insisted that the `discretion of the official in the field' be circumscribed . . . ."</p>

</div>
```

---
