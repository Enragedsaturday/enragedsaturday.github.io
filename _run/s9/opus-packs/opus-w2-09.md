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

## GROUP: _overhaul2/lake/cases/Case v. Montana.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Case v. Montana"
type: case
citation: ""
parallel_cite: ""
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2026
date_decided: 2026-01-14
docket: 24-624
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2026-01-14
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Case v. Montana
  varies_by_point: false
  scope_note: "Decided January 14, 2026 (slip opinion; final U.S. Reports pagination pending). Kagan, J., for a unanimous Court; Sotomayor, J., and Gorsuch, J., concurring. Current good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10774335/case-v-montana/"
  cluster_id: 10774335
  opinion_id: 11240920
  identity_checked: false
homes:
  - page: "[[Emergency Aid]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brigham City v. Stuart]]", "[[Caniglia v. Strom]]", "[[Michigan v. Fisher]]", "[[Mincey v. Arizona]]", "[[Ohio v. Robinette]]"]
aliases: []
tags: ["case", "fourth-amendment", "emergency-aid", "exigent-circumstances", "objectively-reasonable", "suicide", "mental-health"]
holding: "Brigham City's objective-reasonableness standard for warrantless home entries to render emergency aid applies without further gloss — it is neither lowered to Terry reasonable suspicion nor raised to probable cause — and asks only whether an officer had an objectively reasonable basis for believing entry was needed to prevent or deal with serious harm."
lake:
  record_id: Case v. Montana
  status: under_review
  projected_at: 2026-07-06
---

# Case v. Montana

*607 U.S. ___ (2026)* (No. 24-624) · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Montana officers responded to the home of William Trevor Case after his ex-girlfriend called 911 to report that Case — whom the officers knew had mental-health and alcohol problems and had spoken of suicide — was threatening suicide, had spoken of a suicide note, and may have cocked or shot a gun before the call cut off. Officers knocked and yelled into an open window with no response; through the windows they saw empty beer cans, an empty handgun holster, and a notepad. After roughly 40 minutes, they entered to render [[Emergency Aid|emergency aid]]. When an officer approached a closet where Case was hiding, Case threw open the curtain holding what looked like a gun, and the officer shot and injured him; a handgun was found where he had stood. Charged with assaulting an officer, Case moved to suppress, arguing the warrantless entry was unlawful. The Montana Supreme Court upheld the entry under the State's "community caretaker" doctrine.

## Issue
Whether the warrantless home entry to render [[Emergency Aid|emergency aid]] satisfied the Fourth Amendment, and what standard governs such an entry — Brigham City's objective reasonableness, a lower reasonable-suspicion test, or a higher probable-cause test.

## Rule
Brigham City's standard governs, and it applies without further gloss. The Court declined to lower it to reasonable suspicion: "Brigham City did not adopt *Terry*'s reasonable-suspicion standard for home entries. . . . Rather, Brigham City formulated its own standard for dealing with household emergencies — again, whether an officer has 'an objectively reasonable basis for believing' that an occupant is seriously injured or imminently threatened with such harm." — slip op. at 7 (quoting *Brigham City*, 547 U.S. at 400). ^pin-slip7

And it declined to raise it to probable cause: "We decline Case's invitation to put a new probable-cause spin onto Brigham City. . . . So Brigham City adopted a different approach. Rather than strain to relate probable-cause decisions to emergency-aid situations, we asked simply whether an officer had 'an objectively reasonable basis for believing' that his entry was direly needed to prevent or deal with serious harm." — slip op. at 8. ^pin-slip8

The entry is also scope-limited: "an emergency-aid entry provides no basis to search the premises beyond what is reasonably needed to deal with the emergency while maintaining the officers' safety. But we assess the reasonableness of that limited entry on its own terms, rather than through the lens generally used to consider investigative activity." — slip op. at 9. ^pin-slip9

The bottom line: "We repeat today what we have held before: An officer may enter a home without a warrant if he has 'an objectively reasonable basis for believing that an occupant is seriously injured or imminently threatened with such injury.' . . . The officers' entry satisfied that test." — slip op. at 10–11. ^pin-slip10

## Application
Judged on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], the officers had an objectively reasonable basis to believe Case needed [[Emergency Aid|emergency aid]]: they knew of his mental-health and alcohol problems and prior suicide talk; they learned he had threatened suicide, spoke of a suicide note, and possibly fired a gun before the call ended; and they saw empty beer cans, an empty holster, and a notepad through the windows, with no response to urgent knocking. Whether Case had already shot himself (needing care) or had not (acute suicide risk), entry to prevent that result was reasonable — and the Fourth Amendment did not require officers to "leave him to his fate." The Court rejected Case's "suicide-by-cop" theory that the entry itself created the only danger.

## Conclusion
Affirmed (the judgment, though not all the reasoning, of the Montana Supreme Court). *Brigham City*'s objective-reasonableness test for emergency-aid home entries applies on its own terms and was satisfied here.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (Kagan, J., unanimous; Sotomayor, J., and Gorsuch, J., concurring).
- *Case* reaffirms and clarifies [[Brigham City v. Stuart]], rejecting both a *[[Terry v. Ohio|Terry]]*-style reasonable-suspicion gloss and a probable-cause gloss on the emergency-aid standard. It is consistent with [[Caniglia v. Strom]] (no freestanding community-caretaking home entry — welfare entries must route through [[Emergency Aid|emergency aid]]) and applies the totality-of-the-circumstances approach reaffirmed in [[Ohio v. Robinette]].

## Appears on
- [[Emergency Aid]] — *Key — Progeny / Refinement*

## Sources
- *Case v. Montana*, 607 U.S. ___ (2026) (No. 24-624) — https://www.courtlistener.com/opinion/10774335/case-v-montana/ — pinpoints: slip op. at 7, 8, 9, 10–11. Below: *State v. Case*, 417 Mont. 354, 553 P.3d 985 (2024), affirmed.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "57c5c88515c7f56c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-slip10", "record_id": "Case v. Montana"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-slip10", "pinpoint_status": "slip-only", "quote": "We repeat today what we have held before: An officer may enter a home without a warrant if he has 'an objectively reasonable basis for believing that an occupant is seriously injured or imminently threatened with such injury.' . . . The officers' entry satisfied that test.", "quote_fidelity": "mismatch", "record_id": "Case v. Montana", "star_marker": null}}
{"assertion_id": "8689873972a646ef", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-slip7", "record_id": "Case v. Montana"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-slip7", "pinpoint_status": "slip-only", "quote": "doctrine. ## Issue Whether the warrantless home entry to render emergency aid satisfied the Fourth Amendment, and what standard governs such an entry — Brigham City's objective reasonableness, a lower reasonable-suspicion test, or a higher probable-cause test. ## Rule Brigham City's standard governs, and it applies without further gloss. The Court declined to lower it to reasonable suspicion:", "quote_fidelity": "mismatch", "record_id": "Case v. Montana", "star_marker": null}}
{"assertion_id": "e457a56f153a9c2e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-slip8", "record_id": "Case v. Montana"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-slip8", "pinpoint_status": "slip-only", "quote": "We decline Case's invitation to put a new probable-cause spin onto Brigham City. . . . So Brigham City adopted a different approach. Rather than strain to relate probable-cause decisions to emergency-aid situations, we asked simply whether an officer had 'an objectively reasonable basis for believing' that his entry was direly needed to prevent or deal with serious harm.", "quote_fidelity": "mismatch", "record_id": "Case v. Montana", "star_marker": null}}
{"assertion_id": "eb26c3420a1d930e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-slip9", "record_id": "Case v. Montana"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-slip9", "pinpoint_status": "slip-only", "quote": "an emergency-aid entry provides no basis to search the premises beyond what is reasonably needed to deal with the emergency while maintaining the officers' safety. But we assess the reasonableness of that limited entry on its own terms, rather than through the lens generally used to consider investigative activity.", "quote_fidelity": "mismatch", "record_id": "Case v. Montana", "star_marker": null}}
{"assertion_id": "56af28724b6898d4", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Case v. Montana"}, "payload": {"as_of_content": "2026-01-14", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Case v. Montana", "scope_note": "Decided January 14, 2026 (slip opinion; final U.S. Reports pagination pending). Kagan, J., for a unanimous Court; Sotomayor, J., and Gorsuch, J., concurring. Current good law.", "varies_by_point": false}}
```

### lake record — Case v. Montana

```json
{
  "schema_version": "s2.v1",
  "record_id": "Case v. Montana",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Case v. Montana",
    "case_name_short": "Case",
    "case_name_full": "",
    "input_case_name": "Case v. Montana",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2026-01-14",
    "year": 2026,
    "docket": "24-624",
    "cluster_id": 10774335,
    "lead_opinion_id": 11240920,
    "sibling_ids": [
      11240920
    ],
    "absolute_url": "/opinion/10774335/case-v-montana/",
    "identity_method": "name+docket",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": "scotus",
      "selected": null,
      "reason": "no_official_class_citation"
    }
  },
  "pinpoints": [
    {
      "id": "pin-slip7",
      "page": null,
      "quote": "doctrine. ## Issue Whether the warrantless home entry to render emergency aid satisfied the Fourth Amendment, and what standard governs such an entry \u2014 Brigham City's objective reasonableness, a lower reasonable-suspicion test, or a higher probable-cause test. ## Rule Brigham City's standard governs, and it applies without further gloss. The Court declined to lower it to reasonable suspicion:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-slip8",
      "page": null,
      "quote": "We decline Case's invitation to put a new probable-cause spin onto Brigham City. . . . So Brigham City adopted a different approach. Rather than strain to relate probable-cause decisions to emergency-aid situations, we asked simply whether an officer had 'an objectively reasonable basis for believing' that his entry was direly needed to prevent or deal with serious harm.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-slip9",
      "page": null,
      "quote": "an emergency-aid entry provides no basis to search the premises beyond what is reasonably needed to deal with the emergency while maintaining the officers' safety. But we assess the reasonableness of that limited entry on its own terms, rather than through the lens generally used to consider investigative activity.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-slip10",
      "page": null,
      "quote": "We repeat today what we have held before: An officer may enter a home without a warrant if he has 'an objectively reasonable basis for believing that an occupant is seriously injured or imminently threatened with such injury.' . . . The officers' entry satisfied that test.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2026-01-14",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Case v. Montana",
    "varies_by_point": false,
    "scope_note": "Decided January 14, 2026 (slip opinion; final U.S. Reports pagination pending). Kagan, J., for a unanimous Court; Sotomayor, J., and Gorsuch, J., concurring. Current good law.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(11240920) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 0,
        "triage_read": 0,
        "triage_snippet_classified": 0
      },
      "lane2_top_cited": {
        "query": "cites:(11240920)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(11240920)",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 0,
        "triage_read": 0,
        "triage_snippet_classified": 0
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(11240920)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 11240920,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/case-v-montana.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 11240920,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 171142,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 856347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 1184823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 2381644,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 2764455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 4227836,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 4248565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 4287285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 4677033,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 4687473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 4697833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 5432529,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 6585877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9413217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9416513,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9421885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9423752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9427279,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9429232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9430773,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9430897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9431609,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9431641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9433390,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9434949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9441559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9837829,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 9888304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 10499459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11240920,
        "cited_id": 11051434,
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
    "date_created": "2026-07-04T23:43:23Z",
    "date_modified": "2026-07-06T13:36:09Z",
    "warnings": [
      "official cite selection failed closed: no_official_class_citation",
      "legacy treatment migrated: good -> good_law",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:43:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:43:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T13:36:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:43:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Case v. Montana

```
(Slip Opinion)              OCTOBER TERM, 2025                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                            CASE v. MONTANA

       CERTIORARI TO THE SUPREME COURT OF MONTANA

   No. 24–624.      Argued October 15, 2025—Decided January 14, 2026


In Brigham City v. Stuart, 547 U. S. 398, 400, the Court held that the
  Fourth Amendment allows police officers to enter a home without a
  warrant if they have an “objectively reasonable basis for believing”
  that someone inside needs emergency assistance. In this case, Mon-
  tana police officers responded to the home of petitioner William Case
  after his ex-girlfriend called 9–1–1 to report that he was threatening
  suicide and may have shot himself. The officers knocked on the doors
  and yelled into an open window, but got no response. They could see
  an empty handgun holster and something that looked like a suicide
  note inside, and they ultimately decided to enter the home to render
  emergency aid. When one officer approached a bedroom closet in
  which Case was hiding, Case threw open the closet curtain while hold-
  ing an object that looked like a gun. Fearing that he was about to be
  shot, the officer shot and injured Case. An ambulance was called to
  take Case to the hospital, and officers found a handgun next to where
  Case had stood.
     Case was charged with assaulting a police officer. Case moved to
  suppress all evidence obtained from the home entry, arguing that the
  police violated the Fourth Amendment by entering without a warrant.
  The trial court denied the motion, and a jury found Case guilty. A
  divided Montana Supreme Court upheld the officers’ entry as lawful
  under Montana’s caretaker doctrine, rejecting the contention that an
  officer must have probable cause to believe that an occupant needs
  emergency aid.
Held: Brigham City’s objective reasonableness standard for warrantless
 home entries to render emergency aid applies without further gloss
 and was satisfied in this case. Pp. 5–11.
2                           CASE v. MONTANA

                                  Syllabus

       (a) “[S]earches and seizures inside a home without a warrant are
    presumptively unreasonable” under the Fourth Amendment. Brigham
    City, 547 U. S., at 403. But the “warrant requirement is subject to
    certain exceptions,” Lange v. California, 594 U. S. 295, 301, including
    the need to render emergency assistance. The Court first approved a
    warrantless home entry to render emergency assistance in Brigham
    City, holding that officers may enter when they have “an objectively
    reasonable basis for believing that an occupant is seriously injured or
    imminently threatened with such injury.” 547 U. S., at 400.
       The Montana Supreme Court’s opinion below strayed from that rule.
    Most important, the emergency-aid test incorporated in Montana’s
    caretaker doctrine evokes the Fourth Amendment standard of “reason-
    able suspicion” that applies to relatively non-invasive street stops. But
    Brigham City adopted a different standard for home entries.
       Case now urges the Court to understand Brigham City as sounding
    in probable cause, but the Court declines to put a new probable-cause
    spin onto the emergency-aid standard. Probable cause is “peculiarly
    related to criminal investigations,” Treasury Employees v. Von Raab,
    489 U. S. 656, 667, and that body of law would fit awkwardly, if at all,
    in the non-criminal, non-investigatory setting at issue here. Rather
    than strain to relate probable-cause decisions to emergency-aid situa-
    tions, Brigham City asked simply whether an officer had “an objec-
    tively reasonable basis for believing” that entry was direly needed to
    prevent or deal with serious harm. 547 U. S., at 400. Courts should
    assess the reasonableness of an emergency-aid entry on its own terms,
    rather than through the lens generally used to consider investigative
    activity. Pp. 5–9.
       (b) The officers here had an “objectively reasonable basis for believ-
    ing” that their entry was needed to prevent Case from ending his life.
    The information the officers obtained from Case’s ex-girlfriend, com-
    bined with their observations at the scene, suggested that Case may
    already have shot himself or would do so absent intervention. The of-
    ficers’ decision to enter his home to prevent that result was reasonable.
    Accordingly, the Court affirms the judgment (even though not all the
    reasoning) of the Montana Supreme Court. Pp. 9–11.
417 Mont. 354, 553 P. 3d 985, affirmed.

   KAGAN, J., delivered the opinion for a unanimous Court. SOTOMAYOR,
J., and GORSUCH, J., filed concurring opinions.
                        Cite as: 607 U. S. ____ (2026)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     United States Reports. Readers are requested to notify the Reporter of
     Decisions, Supreme Court of the United States, Washington, D. C. 20543,
     pio@supremecourt.gov, of any typographical or other formal errors.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 24–624
                                   _________________


WILLIAM TREVOR CASE, PETITIONER v. MONTANA
      ON WRIT OF CERTIORARI TO THE SUPREME COURT
                      OF MONTANA
                               [January 14, 2026]

   JUSTICE KAGAN delivered the opinion of the Court.
   In Brigham City v. Stuart, 547 U. S. 398, 400 (2006), this
Court held that police officers may enter a home without a
warrant if they have an “objectively reasonable basis for be-
lieving” that someone inside needs emergency assistance.
The question presented is whether that standard means
that officers must have “probable cause” for the intrusion,
as they typically would when investigating a crime. We
hold it does not. The probable-cause requirement is rooted
in, and derives its meaning from, the criminal context, and
we decline to transplant it to this different one. Brigham
City’s reasonableness standard means just what it says,
with no further gloss. And here it was satisfied because the
police had “an objectively reasonable basis for believing”
that a homeowner intended to take his own life and, indeed,
may already have shot himself.
                              I
   This case began with an alarming phone call—from peti-
tioner William Case to his ex-girlfriend J. H., both residents
of a small town in Montana. Case told J. H. on the call that
“he was going to kill himself.” App. 67 (testimony of J. H.).
Because Case sounded “erratic,” J. H. assumed he had been
2                     CASE v. MONTANA

                      Opinion of the Court

drinking. Ibid. She tried to talk Case out of committing
suicide, but “couldn’t reel him back”: With each passing mo-
ment, Case “became more methodical about what he was
going to do.” Id., at 68. Case said that he was “going to get
a note”—presumably meaning a suicide note, for J. H. or
others to find. Ibid. And then J. H. heard a “clicking”
sound, like the “cock[ing of] a gun.” Ibid. J. H. told Case
she was going to call the police, but that seemed only to an-
tagonize him: Case replied “he would shoot them all too.”
Id., at 69. Finally, J. H. heard “a pop” followed by “noth-
ing”—“just dead air.” Ibid. She “yelled [Case’s] name a few
times,” but got no response, leading her to think he had
“pulled the trigger.” Ibid. So she called 9–1–1 to report the
incident and drove as fast as she could to Case’s home.
   Three police officers, dispatched to do “a welfare check on
a suicidal male,” met J. H. outside the house. Id., at 104
(testimony of officer). They decided the situation was “very
serious,” based both on what J. H. told them about the call
and on what they already knew about Case. Id., at 75, 157.
The officers were aware that Case had a history of alcohol
abuse and mental-health issues; that he had previously
threatened suicide at the school where he worked; and that
he had once seemed to attempt “suicide-by-cop,” by con-
fronting the police in a way that was likely to provoke a le-
thal response. So the three officers requested that the chief
of police come to the scene. While waiting for him, they cir-
cled the house looking for signs of injury or danger. They
knocked on the doors and yelled into an open window, but
got no response. Shining their flashlights inside, they could
make out empty beer cans, an empty handgun holster, and
a notepad with writing on it, which they took to be the sui-
cide note Case had mentioned to J. H. At that point, how-
ever, they saw no sign of Case.
   Once the chief came, the officers conferred and decided to
enter the house “to render emergency aid.” Id., at 198. In
the best-case scenario, they hoped to “talk [Case] down” and
                  Cite as: 607 U. S. ____ (2026)              3

                      Opinion of the Court

prevent any injury. Id., at 174. But given J. H.’s account,
the officers considered as well another possibility—that
Case had already shot himself and might be “in there bleed-
ing.” Id., at 85. At the same time, they worried that if Case
remained unharmed, their entry could spark a confronta-
tion. See id., at 174, 192–193. So they equipped themselves
with long-barrel guns and a ballistic shield before going in.
   The officers entered the house through the front door,
about 40 minutes after they first arrived. They announced
themselves loudly, and continued to call out as they walked
through the home. Case did not answer; he was hiding in
the closet of a bedroom upstairs. When one of the officers
entered that room, Case threw open the closet curtain and
appeared from behind it, holding “a black object” which
looked like a gun. Id., at 194. Fearing that he was about
to be shot, the officer fired his own rifle. The bullet hit Case
in the abdomen, and another officer rushed to administer
first aid. An ambulance was called to take Case to the near-
est hospital (where he recovered). Meanwhile, one of the
officers found a handgun in a laundry basket next to the
place where Case had stood.
   The county attorney charged Case with assaulting a po-
lice officer. Case moved to suppress all evidence obtained
as a result of the home entry, arguing that the police had
violated the Fourth Amendment by coming into his house
without a warrant. The trial court denied the motion on the
ground that the police officers were responding legitimately
to an “emergency.” App. to Pet. for Cert. 42a. A Montana
jury then found Case guilty of the crime charged.
   On appeal, a divided Montana Supreme Court upheld the
trial court’s ruling that the officers’ entry was lawful. The
majority analyzed the issue under its “community care-
taker doctrine.” 553 P. 3d 985, 990 (Mont. 2024). It noted
that a recent Fourth Amendment decision of this Court,
Caniglia v. Strom, 593 U. S. 194, 198 (2021), had rejected a
“community caretaking rule” allowing a warrantless home
4                        CASE v. MONTANA

                          Opinion of the Court

entry even absent a “need to render emergency assistance”
to an occupant. But the Montana court thought its commu-
nity-caretaker doctrine survived that holding because it de-
manded such an emergency. Under that doctrine, the court
explained, police could enter a home to do a “welfare check”
only when “objective, specific and articulable facts” would
lead an “experienced officer [to] suspect” that a person in-
side “is in need of help or is in peril.” 553 P. 3d, at 990, 991.
And the court found that facts meeting that description ex-
isted here because of the likelihood of suicide. See id., at
994. The court rejected Case’s alternative standard: that a
police officer must have “probable cause to believe” the oc-
cupant in need of emergency aid. Id., at 992. The “probable
cause” locution, the court suggested, applies only when the
police are “engaged in a criminal investigation.” Ibid. The
dissenting justices, by contrast, favored the proposed prob-
able-cause rule, which they concluded the officers here did
not satisfy. See id., at 996, 998 (opinion of McKinnon, J.).
In the dissent’s view, the court’s different approach resem-
bled the “mere reasonable suspicion” standard applicable to
comparatively non-invasive street stops. Id., at 999. That
standard, the dissent thought, was too easily met to support
a warrantless entry into a home. See id., at 996, 999.
   We granted certiorari, 605 U. S. 968 (2025), because
courts have differed on whether police officers entering a
home to provide emergency aid need “probable cause” to be-
lieve that an occupant is in peril.* We conclude that stand-
ard, borrowed from the criminal context, is inapt. We in-
stead hold just what we have held before: that the officers
——————
  *Compare, e.g., Estate of Chamberlain v. White Plains, 960 F. 3d 100,
105 (CA2 2020) (requiring probable cause); United States v. Cooks, 920
F. 3d 735, 742 (CA11 2019) (same); Corrigan v. District of Columbia, 841
F. 3d 1022, 1030 (CADC 2016) (same), with, e.g., Hill v. Walsh, 884 F. 3d
16, 23 (CA1 2018) (not requiring probable cause); United States v. Quar-
terman, 877 F. 3d 794, 800 (CA8 2017) (same); United States v. Gambino-
Zavala, 539 F. 3d 1221, 1225 (CA10 2008) (same).
                 Cite as: 607 U. S. ____ (2026)             5

                     Opinion of the Court

may enter if, but only if, they have an “objectively reasona-
ble basis for believing” that an occupant faces serious dan-
ger. Brigham City, 547 U. S., at 400.
                               II
   The Fourth Amendment provides that “[t]he right of the
people to be secure in their persons, houses, papers, and ef-
fects, against unreasonable searches and seizures, shall not
be violated.” At the “very core” of that guarantee, as this
Court has often stated, “stands the right of a man to retreat
into his own home and there be free from unreasonable gov-
ernmental intrusion.” Caniglia, 593 U. S., at 198 (quoting
Florida v. Jardines, 569 U. S. 1, 6 (2013)). When the intru-
sion is into that most private place, “reasonableness” usu-
ally means having a warrant. Brigham City, 547 U. S., at
403 (“It is a basic principle of Fourth Amendment law that
searches and seizures inside a home without a warrant are
presumptively unreasonable”). “But not always: The war-
rant requirement is subject to certain exceptions.” Lange v.
California, 594 U. S. 295, 301 (2021). And among those is
one pertinent here, involving the need to provide an occu-
pant with emergency aid.
   This Court first approved a warrantless home entry to
render emergency assistance in Brigham City. There, po-
lice officers responding to a noise complaint observed
through a kitchen window a physical altercation between
an adolescent and several adults. As they watched, the
teenager punched one of the adults in the face, “sending
[him] to the sink spitting blood.” 547 U. S., at 406. The
officers immediately entered the home through a nearby
screen door and, announcing their presence, caused the
fight to cease. We unanimously approved the warrantless
entry as “reasonable under the circumstances.” Ibid. And
we explained what made it so: The officers had “an objec-
tively reasonable basis for believing that an occupant [was]
6                    CASE v. MONTANA

                     Opinion of the Court

seriously injured or imminently threatened with such in-
jury.” Id., at 400.
   Three years later, in Michigan v. Fisher, we reiterated
what we had said in Brigham City about the “emergency
aid exception.” 558 U. S. 45, 47 (2009) (per curiam). The
police in Fisher, also responding to a neighbor’s report,
found a scene redolent of violence and danger. Three win-
dows were broken, with the glass strewn on the ground out-
side; blood was smeared on one of the doors, as well as on
the smashed-in hood of a pickup truck in the driveway; and,
visible through a window, a man inside the house was
“screaming and throwing things” at an unseen target. Id.,
at 48. We held that the officers’ entry in those circum-
stances was “reasonable under the Fourth Amendment,”
just as it had been in Brigham City. 558 U. S., at 48. Using
the same standard articulated there, we concluded that the
officers had “an objectively reasonable basis for believing”
that an occupant of the home needed immediate aid. Id., at
47 (quoting Brigham City, 547 U. S., at 406).
   Finally, in Caniglia, we reaffirmed Brigham City even as
we rejected a broader “community caretaking” justification
for warrantless home entries. The police had gone to Ed-
ward Caniglia’s home after his wife reported that he was
suicidal. Caniglia spoke with the officers on his front porch
and agreed to go to a hospital for psychiatric testing. Then,
once he had left, the officers went inside and took away two
handguns he owned. The lower courts approved the entry
on the ground that the officers were performing “commu-
nity caretaking functions.” 593 U. S., at 196. But we de-
clined to recognize such an “open-ended license” for law en-
forcement officers to enter private homes. Id., at 199.
Citing Brigham City, we readily acknowledged that officers
may enter a home to “render emergency assistance to an
injured occupant or to protect an occupant from imminent
injury.” 593 U. S., at 198. But such emergency conditions
                  Cite as: 607 U. S. ____ (2026)            7

                      Opinion of the Court

were indeed necessary and, given the facts, the officers had
never tried to defend their entry on that basis.
   The Montana Supreme Court’s opinion strayed from the
Fourth Amendment rule that trio of decisions sets out. To
begin with, the court’s use of “community caretaker” doc-
trine was ill-advised, given that Caniglia contrasted “com-
munity caretaking” with “render[ing] emergency assis-
tance” and concluded that the former cannot alone justify a
warrantless home entry. Ibid. The Montana court, to be
sure, tried to reconcile its approach with Caniglia by depict-
ing its community-caretaker rule as allowing home entries
only in emergencies. See 553 P. 3d, at 991. But using ter-
minology that this Court has held misplaced in home-entry
cases could serve only to confuse the issue. And yet more
fundamental, the emergency-aid test incorporated in Mon-
tana’s caretaker doctrine is different from the one adopted
in Brigham City. As noted above, Montana’s test finds a
home entry “reasonable” when an officer has “specific and
articulable facts” from which to “suspect” that someone
needs help. 553 P. 3d, at 991; see supra, at 4. That test’s
language, as the dissenting justices noted, evokes the
Fourth Amendment standard applying to brief, investiga-
tive street stops: “reasonable suspicion” based on “specific
and articulable facts.” United States v. Sokolow, 490 U. S.
1, 7 (1989); Terry v. Ohio, 392 U. S. 1, 21 (1968); 553 P. 3d,
at 999 (McKinnon, J.). But Brigham City did not adopt
Terry’s reasonable-suspicion standard for home entries, as
both the State of Montana and the United States as amicus
curiae acknowledge. See Tr. of Oral Arg. 56, 68–69, 80. Ra-
ther, Brigham City formulated its own standard for dealing
with household emergencies—again, whether an officer has
“an objectively reasonable basis for believing” that an occu-
pant is seriously injured or imminently threatened with
such harm. 547 U. S., at 400.
   Case, however, wants something more. He recognizes
that the Brigham City test applies here, and that it has had
8                     CASE v. MONTANA

                      Opinion of the Court

but one formulation: In describing and applying that stand-
ard, we have never used any different terms. See Brief for
Case 24. But still, Case urges us now to understand the
Brigham City test as “sound[ing] in probable cause.” Brief
for Case 15, 24. What the test really requires, Case con-
tends, is that police officers “have probable cause to believe
[an occupant is] seriously injured or imminently threatened
with such injury.” Id., at 2. Case reaches that conclusion
based mainly on the Fourth Amendment’s recognition of the
“sanctity of the home.” Id., at 29. Given that special status,
he argues, a home entry’s aid-giving, “noninvestigatory
purpose” should make no difference: The same probable-
cause principles used in deciding whether “criminal activity
[is] afoot” should apply as well in “assessing the risk and
gravity of an emergency.” Reply Brief 1–2, 8, 16.
   We decline Case’s invitation to put a new probable-cause
spin onto Brigham City. “[T]he probable-cause standard,”
this Court has often stated, “is peculiarly related to crimi-
nal investigations.” Treasury Employees v. Von Raab, 489
U. S. 656, 667 (1989) (quoting Colorado v. Bertine, 479 U. S.
367, 371 (1987)). The standard’s history is “rooted” in the
“criminal investigatory context.” O’Connor v. Ortega, 480
U. S. 709, 723 (1987) (plurality opinion); see Henry v.
United States, 361 U. S. 98, 100–102 (1959). And the stand-
ard has acquired meaning over time by virtue of that con-
text, as judges have assessed, in case after case, the requi-
site likelihood of finding criminal contraband or evidence.
See, e.g., Illinois v. Gates, 462 U. S. 213, 238–239 (1983).
The resulting body of law would fit awkwardly, if at all, in
the non-criminal, non-investigatory setting at issue here.
So Brigham City adopted a different approach. Rather than
strain to relate probable-cause decisions to emergency-aid
situations, we asked simply whether an officer had “an ob-
jectively reasonable basis for believing” that his entry was
direly needed to prevent or deal with serious harm. 547
U. S., at 400. In adhering to that question, we respect as
                 Cite as: 607 U. S. ____ (2026)            9

                     Opinion of the Court

ever the “first among equals” status the Fourth Amend-
ment affords the home. Jardines, 569 U. S., at 6; see
Caniglia, 593 U. S., at 198–199. And in that vein, we note
that an emergency-aid entry provides no basis to search the
premises beyond what is reasonably needed to deal with the
emergency while maintaining the officers’ safety. But we
assess the reasonableness of that limited entry on its own
terms, rather than through the lens generally used to con-
sider investigative activity.
   Doing so here yields a ready conclusion: The officers had,
as Brigham City requires, an “objectively reasonable basis
for believing” that their intervention was needed to prevent
serious harm. As earlier described, the officers knew first-
hand that Case suffered from mental-health and alcohol-
abuse problems, and that he had previously talked about
committing suicide. See supra, at 2. When they reached
Case’s house, they learned about J. H. and Case’s just-
concluded phone call—that Case, in an apparently inebri-
ated state, threatened to kill himself, spoke of preparing a
suicide note, and quite possibly cocked or even shot a gun
before the line went dead. The concerns that call raised
were heightened by what the officers could see through the
windows—empty beer cans, an empty holster, and a note-
pad—as well as by Case’s failure to respond to their urgent
knocking. If Case had already shot himself, he could have
been severely injured and in need of immediate medical
care. And if he had not, the risk of suicide remained acute,
given all the facts then known to the officers. It was thus
objectively reasonable for the police to believe that Case
needed emergency aid.
   Case counters that only the police entry itself created a
“likely danger.” Brief for Case 45. His argument turns on
the prospect of suicide-by-cop. As noted earlier, Case had
once before acted in a way seemingly designed to provoke a
lethal police response, as the officers knew. See supra, at
2. And J. H. told the officers that Case had threatened to
10                    CASE v. MONTANA

                      Opinion of the Court

“shoot them all too” if they came to the scene. Ibid. So the
“main risk the officers objectively faced,” Case posits, was
that “their very entry would induce” a shoot-out, leading to
a “suicide-by-cop.” Brief for Case 18. And indeed, Case con-
tends, the officers knew that: Why else would they have
“waited roughly 40 minutes after their arrival” before en-
tering his home? Id., at 43. Case concludes that if the of-
ficers had only left well enough alone, nothing would have
happened.
   But Case much oversimplifies a complex situation. The
objective reasonableness of an officer’s conduct under
Brigham City, as in other Fourth Amendment contexts, is
evaluated by looking at the “totality of the circumstances.”
E.g., Barnes v. Felix, 605 U. S. 73, 80 (2025); Ohio v. Robi-
nette, 519 U. S. 33, 39 (1996). One of those circumstances
was no doubt that Case could provoke a confrontation. As
noted earlier, that was partly why the officers called the po-
lice chief to the scene and why they carefully considered
protective measures—leading to some delay in their entry.
See supra, at 2. But there is no basis for thinking that the
officers would have gone into Case’s home just so he could
instigate a gunfight. The circumstances making their entry
reasonable, as just stated, were those suggesting that Case
may already have shot himself or would do so absent inter-
vention. The statements Case made to J. H. plus the visual
evidence corroborating them indicated that Case wanted to
end his life. The decision of the officers to enter his home
to prevent that result—even at some significant risk to
themselves—was (at the least) reasonable. The Fourth
Amendment did not require them, as Case now argues, to
leave him to his fate.
                        *    *     *
  We repeat today what we have held before: An officer may
enter a home without a warrant if he has “an objectively
reasonable basis for believing that an occupant is seriously
                  Cite as: 607 U. S. ____ (2026)                 11

                      Opinion of the Court

injured or imminently threatened with such injury.”
Brigham City, 547 U. S., at 400. The officers’ entry satisfied
that test. Accordingly, we affirm the judgment (even
though not all the reasoning) of the Montana Supreme
Court.
                                                   It is so ordered.
                  Cite as: 607 U. S. ____ (2026)             1

                   SOTOMAYOR, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 24–624
                          _________________


WILLIAM TREVOR CASE, PETITIONER v. MONTANA
     ON WRIT OF CERTIORARI TO THE SUPREME COURT
                     OF MONTANA
                       [January 14, 2026]

   JUSTICE SOTOMAYOR, concurring.
   I join the Court’s opinion, which holds that police officers
may enter a home without a warrant if they have an “ ‘ob-
jectively reasonable basis for believing’ ” that an occupant is
seriously injured or imminently threatened with such
harm. Ante, at 5, 7, 10. Although the Montana Supreme
Court’s opinion appeared, erroneously, to apply a lower
standard akin to reasonable suspicion, I agree that the of-
ficers here had an “ ‘objectively reasonable basis for believ-
ing’ ” that Case needed emergency assistance because he
may have already shot himself or was imminently going to
do so. Ante, at 7–10.
   I write separately to underscore the unique considera-
tions that law enforcement and courts should bear in mind
when assessing whether there is an “objectively reasonable
basis to believe” that a person experiencing a mental-health
crisis needs law enforcement to “render emergency assis-
tance.” Brigham City v. Stuart, 547 U. S. 398, 403 (2006).
As Brigham City explained, the “ ‘justification for what
would be otherwise’ ” an illegal warrantless entry of a home
in this context is “ ‘[t]he need to protect or preserve life or
avoid serious injury.’ ” Ibid. (quoting Mincey v. Arizona, 437
U. S. 385, 392 (1978)). The officers in Brigham City, for in-
stance, needed to enter the house to break up an ongoing
fight to protect a person whom they saw through a window
being struck in the face and to prevent further violence. 547
2                        CASE v. MONTANA

                      SOTOMAYOR, J., concurring

U. S., at 406. When an officer is called to respond to a per-
son at risk of suicide, however, entering the house may not
always be the objectively reasonable course of action to
“ ‘preserve life or avoid serious injury.’ ” Id., at 403 (quoting
Mincey, 437 U. S., at 392).
   In these kinds of circumstances, the presence of law en-
forcement at times can escalate the situation rather that
ameliorate it, putting both the occupant and the officers in
danger. See, e.g., Chamberlain v. White Plains, 960 F. 3d
100, 101–104, 108 (CA2 2020) (officers repeatedly at-
tempted entry of the home of a person with a known “his-
tory of mental illness,” eventually shooting and killing the
occupant after he repeatedly said he was “ ‘okay’ ” and offic-
ers saw he did not need medical attention); Bailey v. Ken-
nedy, 349 F. 3d 731, 734–736, 744 (CA4 2003) (officers at-
tempted to enter house based on a neighbor’s report of
suicide, eventually kicking and striking occupant to arrest
him, despite occupant telling the officers that he was not
suicidal and that they should leave). The risk of escalation
is also heightened by the prevalence of firearms in nearly
half of American households.1 Police may employ more
forceful tactics when they know a firearm is in the house,
and an occupant who is experiencing an acute mental-
health crisis may react more unpredictably in response.
See, e.g., Corrigan v. District of Columbia, 841 F. 3d 1022,
1025–1028 (CADC 2016) (despite occupant voluntarily
meeting the police outside and disclaiming any intention to
harm himself, the officers triggered occupant’s post-
traumatic stress disorder after kicking his door and search-
ing his house, based on report that he was suicidal and
owned firearms); Frazier v. Miller, 404 Mont. 1, 484 P. 3d
912, 916 (2021) (occupant initially told police he was “ ‘fine’ ”
and to “go away” but drew pistol to his own head when the
——————
 1 In 2025, 42% of Americans reported living in a gun-owning household.

Gallup, Guns, https://news.gallup.com/poll/1645/guns.aspx.
                     Cite as: 607 U. S. ____ (2026)                   3

                      SOTOMAYOR, J., concurring

officer continued to attempt entry, leading the officer to
draw his gun in response and eventually shoot the occu-
pant).
   Studies show that individuals with serious mental-health
conditions are disproportionately likely to be injured and
seven times more likely to be killed during police interac-
tions compared to the general population.2 One report
showed that over a 2-year period, “calls for help resulted in
law enforcement officers shooting and killing the very peo-
ple they were called on to assist” in 178 cases.3 Another
study found that police shooting incidents involving behav-
ioral health concerns (suicidal behavior, substance use, or
serious mental illness) were 2.1 times more likely to result
in fatal injury than other police shooting incidents.4 Fur-
ther, individuals with a mental illness were “2.8 times more
likely” to “be killed in their own homes” compared to those
without a mental illness.5
   Given these risks, in some circumstances it may be more
reasonable for officers to try different means of de-escala-
tion before entering the home of a person experiencing a
mental-health crisis. Officers could, for example, attempt
to speak with the occupant from a distance or over the
phone; contact family, friends, or neighbors to help inter-
vene; call in specialized police units, such as negotiators or

——————
  2 See H. Jun, J. DeVylder, & L. Fedina, Police Violence Among Adults

Diagnosed With Mental Disorders, 45 Health & Soc. Work 81 (May
2020); A. Saleh, P. Applebaum, X. Liu, T. Stroup, & M. Wall, Deaths of
People with Mental Illness During Interactions With Law Enforcement,
58 Int’l J. L. & Psychiatry 110, 114 (May-June 2018) (Saleh).
  3 J. Gerberg & A. Li, When a Call to the Police for Help Turns Deadly,

Washington Post, June 22, 2022, https://www.washingtonpost.com/
investigations/interactive/2022/police-shootings-mental-health-calls/.
  4 J. Ward et al., National Burden of Injury and Deaths From Shootings

by Police in the United States, 2015–2020, 4 Am. J. Pub. Health 387,
391–392 (2024).
  5 Saleh 114.
4                          CASE v. MONTANA

                        SOTOMAYOR, J., concurring

officers trained in crisis intervention;6 or otherwise work
with mental-health professionals to approach the occu-
pant.7 Officers called to respond to these kinds of situations
should carefully investigate and assess the nature of the po-
tential crisis and determine whether there is an objectively
reasonable basis to believe that the occupant needs emer-
gency aid inside before entering without a warrant. Once
the decision is made to enter, moreover, the “manner” of the
officers’ entry and their subsequent conduct inside must
also be “reasonable.” Brigham City, 547 U. S., at 406.
    This case highlights the very complexities that will often
attend emergency-aid interventions involving reported
mental-health crises. Multiple facts suggested that Case
did not need emergency aid but was instead waiting inside
for the officers in order to provoke a confrontation that
would result in “suicide-by-cop.”
    Case had told his girlfriend, J. H., on the phone that he
would “shoot them all” if she called the police to his house.
App. 69. Once J. H. arrived at the house, she told the offic-
ers that Case threatened to “shoot it out” with the police.
Id., at 70–74. The officers also knew that in a prior incident
in which police were called to respond to a suicide attempt
by Case, Case had confronted the police in a way that sug-
gested he was attempting suicide-by-cop. Then, while sur-
veying the house, the officers discussed how Case had
“ ‘tried suicide by cop before’ ” and that it was likely Case
——————
   6 See id., at 114–115; Brief for American Psychiatric Association et al.

as Amici Curiae 18–25 (describing programs that involve sending teams
of specially trained police to respond to calls about mental-health crises).
   7 Many jurisdictions around the country have introduced programs in

which police officers and mental-health professionals jointly respond to
calls about mental-health crises. See Policy Research, Inc. & National
League of Cities, A. Krider, R. Huerter, K. Gaherty, & A. Moore, Re-
sponding to Individuals in Behavioral Health Crisis Via Co-responder
Models (Jan. 2020), https://www.theiacp.org/sites/default/files/SJC
Responding%20to%20Individuals.pdf (describing “co-responder” pro-
grams).
                     Cite as: 607 U. S. ____ (2026)                    5

                       SOTOMAYOR, J., concurring

was “ ‘going to pull a gun on us’ ” once they “ ‘go in the
house.’ ” 417 Mont. 354, 373, 553 P. 3d 985, 998 (2024).
   These facts, taken together, suggested that Case was nei-
ther already injured nor about to injure himself, but rather
that the primary danger he faced would arise only if the
officers entered his house. In other words, these facts
tended to undermine the officers’ basis to believe that he
needed emergency assistance inside.
   The officers’ warrantless entry ultimately did not violate
the Fourth Amendment, however, because there were suf-
ficient facts on the other side of the ledger supporting an
objectively reasonable basis to believe that Case had shot
himself. Critically, Case had told J. H. he had a “loaded
gun” and J. H. heard a “clicking” sound like the “cock[ing]”
of “a gun,” a “pop,” and then “just dead air” despite J. H.
yelling Case’s name multiple times over the phone. App.
68–69; 417 Mont., at 357, 553 P. 3d, at 988. Case also told
J. H. that he was “going to get a note” and “kill himself.”
App. 67–68. When the officers arrived, they saw an empty
handgun holster and notepad with writing inside Case’s
house, and Case did not respond when they shouted his
name into an open window. Considered together, those
facts gave rise to an objectively reasonable basis for the of-
ficers to believe that Case was already injured and in need
of emergency medical assistance, and was not necessarily
waiting inside for the officers seeking to provoke an escala-
tion leading to suicide-by-cop. As a result, the officers did
not violate the Fourth Amendment when they entered
Case’s home.8
   That conclusion, on the facts of this case, does not mean
it will always be objectively reasonable for officers respond-
ing to a mental-health crisis to make a warrantless entry.
——————
  8 Case has not challenged the reasonableness of the officers’ manner of

entry or their conduct inside his house after entry. As a result, neither
the decision below nor this Court had occasion to consider the reasona-
bleness of that conduct.
6                     CASE v. MONTANA

                   SOTOMAYOR, J., concurring

A different mix of information might have led to the conclu-
sion that the officers’ entry itself would put the occupant
(and officers) at a greater risk of escalation and serious in-
jury. Because the “objectively reasonable basis” test, as re-
affirmed by the Court today, demands careful attention to
the case-specific risks that attend mental-health crises, and
requires officers to act reasonably in response, I join the
Court’s opinion in full.
                  Cite as: 607 U. S. ____ (2026)            1

                    GORSUCH, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 24–624
                          _________________


WILLIAM TREVOR CASE, PETITIONER v. MONTANA
     ON WRIT OF CERTIORARI TO THE SUPREME COURT
                     OF MONTANA
                       [January 14, 2026]

   JUSTICE GORSUCH, concurring.
   Today’s case, like another before it, holds that police of-
ficers generally do not violate a person’s Fourth Amend-
ment rights when they enter his house without a warrant,
but with an “ ‘objectively reasonable basis’ ” for believing
someone inside is in physical danger and in need of imme-
diate aid. Ante, at 7 (quoting Brigham City v. Stuart, 547
U. S. 398, 400 (2006)). Importantly, the Court observes,
this exception to the warrant requirement permits entry
only to the extent reasonably necessary to address the ap-
parent emergency and does not authorize officers to search
a home more broadly. See ante, at 9. With all that, I agree.
   But to me, a question lingers: Why? Does the Fourth
Amendment tolerate this limited emergency aid exception
to the warrant requirement just because five or more Jus-
tices of this Court happen to believe that such entries are
“reasonable”? Or is this exception more directly “tied to the
law”? Carpenter v. United States, 585 U. S. 296, 397 (2018)
(GORSUCH, J., dissenting). The answer, I believe, is the lat-
ter.
   From before the founding through the present day, the
common law has generally permitted a private citizen to en-
ter another’s house and property in order to avert serious
physical harm. In those circumstances, and many others,
courts have historically held that property rights give way
to concern for human safety. See, e.g., 37 Hen. 6, pl. 26;
2                          CASE v. MONTANA

                         GORSUCH, J., concurring

Mouse’s Case, 12 Co. Rep. 63, 77 Eng. Rep. 1341 (K. B.
1608); Respublica v. Sparhawk, 1 Dall. 357, 363 (Pa. 1788);
Ploof v. Putnam, 81 Vt. 471, 474–475, 71 A. 188, 189 (1908).
Courts have long described property-law necessity defenses
like these as turning, too, on the adequacy of the defend-
ant’s judgment, not a post-hoc assessment of necessity in
fact. See, e.g., Mitchell v. Harmony, 13 How. 115, 134–135
(1852); Stone v. Mayor of City of New York, 25 Wend. 157,
176 (N. Y. 1840) (opinion of Verplanck, Sen.); Surocco v.
Geary, 3 Cal. 69, 72 (1853).*
   The common-law emergency rule is now often summa-
rized this way: “One is privileged to enter or remain on land
in the possession of another if it is or reasonably appears to
be necessary to prevent serious harm to . . . the actor[,] . . .
the other[,] or a third person . . . unless the actor knows or
has reason to know that the one for whose benefit he enters
is unwilling that he shall take such action.” Restatement
(Second) of Torts §197(1) (1963–1964). But, of course, this
privilege comes with its logical limitations. So, for example,
a private citizen who enters a home to render emergency
aid lacks license to do so in a manner “which a reasonable
man would not regard as necessary to” address the appar-
ent emergency. Id., §214, and Comment a; see also id., §197,
Comment a; Des Moines v. Webster, 861 N. W. 2d 878, 883–
885 (Iowa App. 2014); State v. Lukus, 149 Mont. 45, 50–51,
423 P. 2d 49, 52–53 (1967).
——————
   *Contrary to Mr. Case’s argument, King v. Coate, Lofft. 73, 98 Eng.
Rep. 539 (K. B. 1772), does not establish that the common law demanded
an exacting showing of actual necessity to defeat a claim for trespass.
True, Lord Mansfield explained that any necessity defense in that case
would need to “stand the strictest test,” with the “necessity manifestly
proved.” Id., at 75, 98 Eng. Rep., at 540. But Coate involved an effort to
involuntarily “confin[e] a person in a madhouse” for two months, not a
claim over a home entry. Id., at 74, 98 Eng. Rep., at 539. And it is hardly
surprising that the common law would demand a good deal more to jus-
tify a serious deprivation of liberty than to excuse an invasion of property
rights aimed at protecting human safety.
                   Cite as: 607 U. S. ____ (2026)              3

                     GORSUCH, J., concurring

   Today’s decision echoes both the common-law emergency
aid rule and its limitations. It does so, to be sure, in the con-
text of a law enforcement officer, not a private citizen, who
sought to enter another’s home. But on this point as well the
common law has spoken, long providing that officers gener-
ally enjoy the same legal privileges as private citizens. See,
e.g., Entick v. Carrington, 19 How. St. Tr. 1029, 1066 (C. P.
1765); 1 J. Chitty, Criminal Law 36 (1819); 2 M. Hale, His-
toria Placitorum Coronae 91 (1736). And, reflecting the
common law here again, this Court has held that the Fourth
Amendment usually permits officers lacking a valid war-
rant to “take actions that any private citizen might do with-
out fear of liability.” Caniglia v. Strom, 593 U. S. 194, 198
(2021) (internal quotation marks omitted). But they nor-
mally may do “no more” than that. Kentucky v. King, 563
U. S. 452, 469 (2011); see also Entick, 19 How. St. Tr., at
1066.
   It should come as no surprise that our decision today
might accord with the accumulated learning of the common
law—just as it should come as no surprise that our applica-
tion of the Fourth Amendment ought to be informed by the
common law’s lessons rather than mere intuition. For a pe-
riod, to be sure, the miasma created by this Court’s Katz era
led some to think the scope of the rights guaranteed by the
Fourth Amendment depend on nothing more than current
judicial instincts about “reasonable expectations of pri-
vacy.” See Carpenter, 585 U. S., at 394–395, 405–406
(GORSUCH, J., dissenting). But that confusion cannot last
forever, for no one should think the rights of Americans
hang on so thin a thread. Instead, and as Justice Story rec-
ognized, the Fourth Amendment is made of sturdier stuff,
representing “the affirmance of a great constitutional doc-
trine of the common law.” 3 Commentaries on the Consti-
tution of the United States 748 (1833).

```

---

## GROUP: _overhaul2/lake/cases/Chambers v. Florida.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Chambers v. Florida"
type: case
citation: "309 U.S. 227 (1940)"
parallel_cite: "60 S. Ct. 472; 84 L. Ed. 716"
neutral_cite: 1940 U.S. LEXIS 911
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1940
date_decided: 1940-02-12
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1940-02-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Chambers v. Florida
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/103301/chambers-v-florida/"
  cluster_id: 103301
  opinion_id: 103301
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brown v. Mississippi]]", "[[Ashcraft v. Tennessee]]", "[[Colorado v. Connelly]]"]
aliases: []
tags: ["case", "fifth-amendment", "due-process", "confessions", "voluntariness", "coercion"]
holding: "Confessions extracted through prolonged, incommunicado interrogation of helpless prisoners were the product of compulsion and their use…"
lake:
  record_id: Chambers v. Florida
  status: verified
  projected_at: 2026-07-09
---

# Chambers v. Florida

*309 U.S. 227 (1940)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Four Black tenant farmers were arrested without warrants after a robbery-murder and held incommunicado, without counsel, friends, or formal charges. Over five days they were subjected to protracted, repeated interrogation — culminating in an all-night session — amid an atmosphere of mob hostility, until they confessed. The confessions were the basis of their death sentences, affirmed by the Florida courts.

## Issue
Whether confessions extracted by sustained, coercive incommunicado interrogation may be used to convict consistent with the Due Process Clause of the Fourteenth Amendment.

## Rule
No. The confessions were the product of compulsion, not free will, and their use violates due process: "To permit human lives to be forfeited upon confessions thus obtained would make of the constitutional requirement of due process of law a meaningless symbol." — 309 U.S. 227, 240. ^pin-240

"Under our constitutional system, courts stand against any winds that blow as havens of refuge for those who might otherwise suffer because they are helpless, weak, outnumbered, or because they are non-conforming victims of prejudice and public excitement." — [*Id.* at 241](https://www.courtlistener.com/opinion/103301/chambers-v-florida/#:~:text=Under%20our%20constitutional%20system%2C%20courts). ^pin-241

## Application
For five days these petitioners were held without charges, isolated, and interrogated under circumstances "calculated to break the strongest nerves and the stoutest resistance," with the fear of mob violence surrounding them. On those facts the confessions were compelled rather than freely given, and using them to send the petitioners to death denied due process.

## Conclusion
The coerced confessions could not support the convictions; the judgments of the Supreme Court of Florida were reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Chambers* applies the due-process voluntariness rule of [[Brown v. Mississippi]] to psychological/incommunicado coercion, a line later extended in [[Ashcraft v. Tennessee]] and cabined to require state coercion in [[Colorado v. Connelly]].

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Chambers v. Florida*, 309 U.S. 227 (1940) — https://www.courtlistener.com/opinion/103301/chambers-v-florida/ — pinpoints: 240, 241.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "10df84d0bfdd0fe7", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Chambers v. Florida"}, "payload": {"all": [{"cite": "309 U.S. 227", "page": "227", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "309"}, {"cite": "60 S. Ct. 472", "page": "472", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "60"}, {"cite": "84 L. Ed. 716", "page": "716", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "84"}, {"cite": "1940 U.S. LEXIS 911", "page": "911", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1940"}], "display": "309 U.S. 227", "official": {"cite": "309 U.S. 227", "page": "227", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "309"}, "official_selection_present": true, "record_id": "Chambers v. Florida"}}
{"assertion_id": "00c61ae0fb80b1c5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-240", "record_id": "Chambers v. Florida"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-240", "pinpoint_status": "slip-only", "quote": "--- # Chambers v. Florida *309 U.S. 227 (1940)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Four Black tenant farmers were arrested without warrants after a robbery-murder and held incommunicado, without counsel, friends, or formal charges. Over five days they were subjected to protracted, repeated interrogation — culminating in an all-night session — amid an atmosphere of mob hostility, until they confessed. The confessions were the basis of their death sentences, affirmed by the Florida courts. ## Issue Whether confessions extracted by sustained, coercive incommunicado interrogation may be used to convict consistent with the Due Process Clause of the Fourteenth Amendment. ## Rule No. The confessions were the product of compulsion, not free will, and their use violates due process:", "quote_fidelity": "mismatch", "record_id": "Chambers v. Florida", "star_marker": null}}
{"assertion_id": "7cc724812ba16c43", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-241", "record_id": "Chambers v. Florida"}, "payload": {"fragment": "#:~:text=Under%20our%20constitutional%20system%2C%20courts", "page": null, "pin_id": "pin-241", "pinpoint_status": "star-verified", "quote": "Under our constitutional system, courts stand against any winds that blow as havens of refuge for those who might otherwise suffer because they are helpless, weak, outnumbered, or because they are non-conforming victims of prejudice and public excitement.", "quote_fidelity": "matched", "record_id": "Chambers v. Florida", "star_marker": "241"}}
{"assertion_id": "375a5f8426b5768f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Chambers v. Florida"}, "payload": {"as_of_content": "1940-02-12", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Chambers v. Florida", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Chambers v. Florida

```json
{
  "schema_version": "s2.v1",
  "record_id": "Chambers v. Florida",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Chambers v. Florida",
    "case_name_short": "Chambers",
    "case_name_full": "CHAMBERS Et Al. v. FLORIDA",
    "input_case_name": "Chambers v. Florida",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1940-02-12",
    "year": 1940,
    "docket": null,
    "cluster_id": 103301,
    "lead_opinion_id": 103301,
    "sibling_ids": [
      103301
    ],
    "absolute_url": "/opinion/103301/chambers-v-florida/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "309 U.S. 227",
      "volume": "309",
      "reporter": "U.S.",
      "page": "227",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "60 S. Ct. 472",
        "volume": "60",
        "reporter": "S. Ct.",
        "page": "472",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 716",
        "volume": "84",
        "reporter": "L. Ed.",
        "page": "716",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1940 U.S. LEXIS 911",
        "volume": "1940",
        "reporter": "U.S. LEXIS",
        "page": "911",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "309 U.S. 227",
        "volume": "309",
        "reporter": "U.S.",
        "page": "227",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 S. Ct. 472",
        "volume": "60",
        "reporter": "S. Ct.",
        "page": "472",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 716",
        "volume": "84",
        "reporter": "L. Ed.",
        "page": "716",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1940 U.S. LEXIS 911",
        "volume": "1940",
        "reporter": "U.S. LEXIS",
        "page": "911",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "309 U.S. 227",
    "official_selection": {
      "court_class": "scotus",
      "selected": "309 U.S. 227",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-240",
      "page": null,
      "quote": "--- # Chambers v. Florida *309 U.S. 227 (1940)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Four Black tenant farmers were arrested without warrants after a robbery-murder and held incommunicado, without counsel, friends, or formal charges. Over five days they were subjected to protracted, repeated interrogation \u2014 culminating in an all-night session \u2014 amid an atmosphere of mob hostility, until they confessed. The confessions were the basis of their death sentences, affirmed by the Florida courts. ## Issue Whether confessions extracted by sustained, coercive incommunicado interrogation may be used to convict consistent with the Due Process Clause of the Fourteenth Amendment. ## Rule No. The confessions were the product of compulsion, not free will, and their use violates due process:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-241",
      "page": null,
      "quote": "Under our constitutional system, courts stand against any winds that blow as havens of refuge for those who might otherwise suffer because they are helpless, weak, outnumbered, or because they are non-conforming victims of prejudice and public excitement.",
      "star_marker": "241",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 18800,
      "fragment": "#:~:text=Under%20our%20constitutional%20system%2C%20courts",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1940-02-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Chambers v. Florida",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Singleton",
          "cluster_id": 9506618,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Phipps",
          "cluster_id": 9440775,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
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
        "journal_ref": "Chambers v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Michael E. HARRIS, Petitioner-Appellant, v. Robert WRIGHT, Superintendent, Clallam Bay Correction Center, Respondent-Appellee",
          "cluster_id": 724945,
          "cite": [
            "93 F.3d 581",
            "96 Cal. Daily Op. Serv. 6150",
            "96 Daily Journal DAR 10051",
            "1996 U.S. App. LEXIS 20643"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Avendano-Lopez",
          "cluster_id": 1387134,
          "cite": [
            "904 P.2d 324",
            "79 Wash. App. 706"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
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
        "journal_ref": "Chambers v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Leroy Mitchell",
          "cluster_id": 483891,
          "cite": [
            "812 F.2d 1250",
            "1987 U.S. App. LEXIS 3549"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Walter McKinley Harris v. John D. Rees, Superintendent, Kentucky State Reformatory",
          "cluster_id": 472621,
          "cite": [
            "794 F.2d 1168",
            "1986 U.S. App. LEXIS 27282"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jerry Lane Jurek v. W. J. Estelle, Jr., Director, Texas Department of Corrections, Respondent",
          "cluster_id": 379222,
          "cite": [
            "623 F.2d 929",
            "1980 U.S. App. LEXIS 14967"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Maria Irma Navia-Duran v. Immigration and Naturalization Service",
          "cluster_id": 352273,
          "cite": [
            "568 F.2d 803",
            "1977 U.S. App. LEXIS 5395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane1_negative"
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
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
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
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re WINSHIP",
          "cluster_id": 108111,
          "cite": [
            "25 L. Ed. 2d 368",
            "90 S. Ct. 1068",
            "397 U.S. 358",
            "1970 U.S. LEXIS 56"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
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
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "North Carolina v. Pearce",
          "cluster_id": 107978,
          "cite": [
            "23 L. Ed. 2d 656",
            "89 S. Ct. 2072",
            "395 U.S. 711",
            "1969 U.S. LEXIS 1165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brady v. United States",
          "cluster_id": 108137,
          "cite": [
            "25 L. Ed. 2d 747",
            "90 S. Ct. 1463",
            "397 U.S. 742",
            "1970 U.S. LEXIS 45"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
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
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Fulminante",
          "cluster_id": 112566,
          "cite": [
            "113 L. Ed. 2d 302",
            "111 S. Ct. 1246",
            "499 U.S. 279",
            "1991 U.S. LEXIS 1854"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McMann v. Richardson",
          "cluster_id": 108138,
          "cite": [
            "25 L. Ed. 2d 763",
            "90 S. Ct. 1441",
            "397 U.S. 759",
            "1970 U.S. LEXIS 46"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griswold v. Connecticut",
          "cluster_id": 107082,
          "cite": [
            "14 L. Ed. 2d 510",
            "85 S. Ct. 1678",
            "381 U.S. 479",
            "1965 U.S. LEXIS 2282"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ashe v. Swenson",
          "cluster_id": 108114,
          "cite": [
            "25 L. Ed. 2d 469",
            "90 S. Ct. 1189",
            "397 U.S. 436",
            "1970 U.S. LEXIS 54"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. Illinois",
          "cluster_id": 105382,
          "cite": [
            "100 L. Ed. 2d 891",
            "76 S. Ct. 585",
            "351 U.S. 12",
            "1956 U.S. LEXIS 1059"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
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
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
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
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williams v. New York",
          "cluster_id": 104681,
          "cite": [
            "93 L. Ed. 2d 1337",
            "69 S. Ct. 1079",
            "337 U.S. 241",
            "1949 U.S. LEXIS 2308",
            "93 L. Ed. 1337"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sheppard v. Maxwell",
          "cluster_id": 107247,
          "cite": [
            "16 L. Ed. 2d 600",
            "86 S. Ct. 1507",
            "384 U.S. 333",
            "1966 U.S. LEXIS 1413",
            "1 Media L. Rep. (BNA) 1220",
            "6 Ohio Misc. 231",
            "35 Ohio Op. 2d 431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
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
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robinson v. California",
          "cluster_id": 106451,
          "cite": [
            "8 L. Ed. 2d 758",
            "82 S. Ct. 1417",
            "370 U.S. 660",
            "1962 U.S. LEXIS 850"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kennedy v. Mendoza-Martinez",
          "cluster_id": 106534,
          "cite": [
            "9 L. Ed. 2d 644",
            "83 S. Ct. 554",
            "372 U.S. 144",
            "1963 U.S. LEXIS 2095"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re Oliver",
          "cluster_id": 104521,
          "cite": [
            "92 L. Ed. 2d 682",
            "68 S. Ct. 499",
            "333 U.S. 257",
            "1948 U.S. LEXIS 2452",
            "92 L. Ed. 682"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
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
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
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
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
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
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
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
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
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
        "journal_ref": "Chambers v. Florida:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(103301) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04MDM1MjAwMDAwMCZzPTE0MTg4NjEmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28103301%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(103301)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTY0JnM9MTA1OTE3JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28103301%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(103301)",
        "reviewed": 9,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 9,
        "triage_read": 2,
        "triage_snippet_classified": 7
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(103301)",
    "indexed_citing_opinions": 540,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 103301,
        "count": 540,
        "count_source": "search"
      }
    ],
    "citation_count": 844,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/chambers-v-florida.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU3NDcyOTkmcz00NDY5MTQ5JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28103301%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 103301,
        "cited_id": 89446,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 92743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 93324,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 95204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 96885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 97242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 102188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 102407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 103162,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 103226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 3267432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 3381494,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 3382712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 3383257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 3390304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 3390887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103301,
        "cited_id": 3396558,
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
    "date_created": "2026-07-04T23:44:10Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:44:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:44:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:47:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:44:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Chambers v. Florida

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b297-13">
  Mr. Justice Black
 </author>
<p id="AkAq">
  delivered' the opinion of the Court.
 </p>
<p id="b297-14">
  The grave question presented by the petition for cer-tiorari, granted in forma pauperis,
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  is whether proceedings in which confessions, were utilized, and which culminated in sentences of death upon four young negro men in the State of Florida, failed to afford the safeguard of that due process of law guaranteed by the Fourteenth Amendment.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b298-3">
<span citation-index="1" class="star-pagination" label="228"> 
   *228
   </span>
<em>
   First.
  </em>
  The State of Florida challenges our jurisdiction to look behind the judgments below claiming that the issues of fact upon which petitioners base their claim that due process was denied them have been finally determined because passed upon by a jury. 'However, use by a State of an improperly obtained confession may constitute a denial of due process of law as guaranteed in the Fourteenth Amendment.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  Since petitioners have seasonably asserted the right under the federal Constitution to have (their guilt or innocence of a capital crime determined without reliance upon confessions obtained by means
  <span citation-index="1" class="star-pagination" label="229"> 
   *229
   </span>
  proscribed by the due process clause of the Fourteenth' Amendment, we must determine independently whether petitioners’ confessions were so obtained, by review of the facts upon which that issue necessarily turns.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
</p>
<p id="b299-4">
<em>
   Second.
  </em>
  The record shows—
 </p>
<p id="b299-5">
  About nine o’clock on the night of Saturday, May 13, 1933, Robert Darsey, an elderly white man, was robbed and murdered in Ppmpano, Florida, a small town in Broward County about twelve miles from Fort Lauderdale, the County seat. The opinion of the Supreme Court of Florida affirming petitioners’ conviction for this crime stated that “It was one of those crimes that induced* an enraged community . . .”
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  And, as the dissenting judge pointed out, “The murder and robbery of the elderly Mr. Darsey . . . was a most dastardly and atrocious crime. It naturally aroused great and well justified public indignation.”
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
</p>
<p id="b299-6">
  Between 9:30 and 10 o’clock after the murder, petitioner Charlie Davis was arrested, and within the next twenty-four hours from twenty-five to forty negroes living in the community, including petitioners Williamson, Chambers, and Woodward, were arrested without warrants and confined in the Broward County jail, at Fort Lauderdale. On the night of the crime, attempts to trail the murderers by bloodhounds brought J. T. Williams, a convict guard, into the proceedings. From then until confessions were obtained and petitioners were sentenced, he took a prominent part. About 11 P. M. on the following Monday, May 15, the sheriff and Williams took several of the imprisoned' negroes, including Williamson and Chambers, to the Dade County jail at Miami. The
  <span citation-index="1" class="star-pagination" label="230"> 
   *230
   </span>
  sheriff testified that they were taken there because he felt a possibility of mob violence and “wanted to give protection to every prisoner ... in jail.” Evidence of petitioners was that on the way to Miami a motorcycle patrolman drew up to the car in which the men were riding and the sheriff “told the cop that he had some negroes that he — [was] taking down to Miami to escape a mob.” This statement was not denied by the sheriff in his testimony and Williams did not testify at all; Williams apparently has now disappeared. Upon order of Williams, petitioner Williamson was kept in the death cell of the Dade County jail. The prisoners thus spirited to Miami were returned to the Fort Lauderdale jail the next day, Tuesday.
 </p>
<p id="b300-4">
  It is clear from the evidence of both the State and petitioners that from Sunday, May 14, to Saturday, May 20, the thirty to forty negro suspects were subjected to questioning and cross questioning (with the exception that several of the suspects were in Dade County jail over one night). From the afternoon of Saturday, May 20, until sunrise of the 21st, petitioners and possibly one or two others underwent persistent and repeated questioning. The Supreme Court of .Florida said the questioning “was in progress several days and all night before the confessions were secured” and referred to the last night as an “all night vigil.” The sheriff who supervised the procedure of continued interrogation testified that he questioned the prisoners “in the day time all the week,” but did not question them during any night before the all night vigil' of Saturday, May 20, because after having “questioned them all day . . . [he] was tired.” Other evidence of the State was “that the officers of Broward County were in that jail almost ■ continually during the whole week questioning these boys, and other boys, in connection with this” case.
 </p>
<p id="b301-5">
<span citation-index="1" class="star-pagination" label="231"> 
   *231
   </span>
  The process of repeated questioning took place in the jailer’s quarters on the fourth floor of the jail. During the week following their arrest and until their confessions were finally acceptable to the State’s Attorney in the early' dawn of Sunday, May 21st, petitioners and their fellow prisoners were led one at a -time from their cells to the questioning room, quizzed, and returned to their cells to await another turn. So'far as appears, the prisoners at no time during the week were permitted to see or confer with counsel or a single friend or relative. When carried singly from his cell and subjected to questioning, each found himself, a single prisoner, surrounded in a fourth floor jail room by four to ten men, the county sheriff, his deputies; a convict guard, and other white officers and citizens of the community.
 </p>
<p id="b301-6">
  The testimony is in conflict as to whether all four petitioners were continually threatened and physically mistreated until they finally, in hopeless desperation and fear of their lives, agreed to confess on Sunday morning just after daylight. Be that as it may, it is certain that by Saturday, May 20th, five days of continued questioning had elicited no confession. Admittedly, a concentration of effort — directed against a small number of prisoners including petitioners — on the part of the questioners, principally the sheriff and Williams, the convict guard, began about 3: 30 that Saturday afternoon. From that hour on, with only short intervals for food and rest for the questioners — “They all stayed up all night.” “They bring one of them at a time backwards and forwards . . . until they confessed.” And Williams was present and participating that night, during the whole' of which the jail cook served coffee and sandwiches to the men who “grilled” the prisoners.
 </p>
<p id="b301-7">
  Sometime in the early hours of Sunday, the 21st, probably about 2:30 A. M., Woodward apparently “broke” — '
  <span citation-index="1" class="star-pagination" label="232"> 
   *232
   </span>
  as one of the state’s witnesses put it — after a fifteen or twenty minute period of questioning by Williams, the sheriff and the constable “one right after the other.” The State’s Attorney was awakened at his home, and called to the jail. He came, but was dissatisfied with the confession of-Woodward which he took down in writing at that time, and said something like “tear this paper up, that isn’t what I want, when you get something worth while call me.”
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  This same State’s Attorney conducted the state’s case in the circuit court below and also made himself a witness, but did not testify as to. why Woodward’s
  <span citation-index="1" class="star-pagination" label="233"> 
   *233
   </span>
  first alleged confession was unsatisfactory to him. The sheriff did, however:
 </p>
<blockquote id="b303-4">
  “A. No, it wasn’t false, part of it was true and part of it wasn’t; Mr. Maire [the State’s Attorney] said there wasn’t enough. It wasn’t clear enough.
 </blockquote>
<blockquote id="b303-7">
<em>
   " ...
  </em>
</blockquote>
<blockquote id="b303-8">
  “Q. . . . Was that voluntarily made at that time?
 </blockquote>
<blockquote id="ABK">
  “A. Yes, sir.
 </blockquote>
<blockquote id="b303-9">
  “Q. It was voluntarily made that time'?
 </blockquote>
<blockquote id="b303-10">
  “A. Yes, sir..
 </blockquote>
<blockquote id="b304-3">
<span citation-index="1" class="star-pagination" label="234"> 
   *234
   </span>
  “Q. You didn’t consider it sufficient?
 </blockquote>
<blockquote id="A8P">
  “A. Mr. Maire.
 </blockquote>
<blockquote id="b304-5">
  “Q. Mr.' Maire told you that it wasn’t sufficient, so you kept on questioning him until the time you got him to make a free and voluntary confession of other matters that he hadn’t included in the first?
 </blockquote>
<blockquote id="b304-6">
  “A. .No, sir, we questioned him there and we caught him in lies..
 </blockquote>
<blockquote id="b304-7">
  “Q. Caught all of them telling lies?
 </blockquote>
<blockquote id="b304-8">
  “A. Caught every one of them lying to us that night, yes, sir.
 </blockquote>
<blockquote id="b304-9">
  “Q. Did you tell them they were lying?
 </blockquote>
<blockquote id="b304-10">
  “A. Yes, sir.
 </blockquote>
<blockquote id="b304-11">
  “Q. Just how would you tell them that?
 </blockquote>
<blockquote id="b304-12">
  “A. Just like I am talking to you.
 </blockquote>
<blockquote id="b305-5">
<span citation-index="1" class="star-pagination" label="235"> 
   *235
   </span>
  “Q. You said ‘Jack, you told me a lie’?
 </blockquote>
<blockquote id="b305-6">
  “A. Yes, sir.”
 </blockquote>
<p id="b305-7">
  After one week’s constant denial of all guilt, petitioner “broke.”
 </p>
<p id="b305-8">
  Just before sunrise, the state officials got something “worthwhile” from petitioners which the State’s Attorney would “want”; again he was called; he came;- in the presence of'those who had carried on and witnessed the all-night questioning, he caused his questions and petitioners’ answers to be stenographically reported. These are the confessions utilized by the State to obtain the judgments upon which petitioners were sentenced' to death. No formal charges had been brought before the confessions. Two days thereafter, petitioners-were indicted, were arraigned and Williamson and Woodward pleaded guilty; Chambers and Davis pleaded not guilty. Later the sheriff, accompanied by Williams, informed an-attorney who presumably had been appointed to defend Davis that Davis wanted his plea of not guilty withdrawn. This was done, and Davis then pleaded guilty. When Chambers was tried, his conviction rested upon his confession and testimony of the other three confessors. The convict guard and the sheriff “were in the Court room sitting down in a seat.” And from arrest until sentenced to death, petitioners were never — either in jail or in court— wholly removed from the constant observation, influence, custody and control of those whose persistent pressure brought about the' sunrise confessions.
 </p>
<p id="b305-9">
<em>
   Third.
  </em>
  The scope and operation of the Fourteenth Amendment have been fruitful sources of controversy in our constitutional history.
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
  However, in view of its his-
  <span citation-index="1" class="star-pagination" label="236"> 
   *236
   </span>
  torieal setting and the wrongs which called it into being, the due process provision of the Fourteenth Amendment — just as that in the Fifth — has led few to doubt that it was intended to guarantee procedural standards adequate and appropriate, then and thereafter,
  <a class="footnote" href="#fn9" id="fn9_ref">
   9
  </a>
  to protect, at all times, people charged with or suspected of crime by those holding positions of power and authority. Tyrannical governments had immemorially utilized dictatorial criminal procedure and punishment to make scapegoats of the weak, or of helpless political, religious, or racial minorities and those who differed, who would not conform and who resisted tyranny. ■ The instruments of such governments were, in the main, two. Conduct, innocent when engaged in, was subsequently made by fiat criminally punishable without legislation. And a liberty loving people won the principle that criminal punishments could not be inflicted save for that which proper legislative action had already by “the law of the land” forbidden when done. But even more was needed. From the popular hatred and abhorrence of illegal confinement, torture and extortion of confessions of violations of the “law of the land” evolved the fundamental idea that no man’s life, liberty or property be forfeited as criminal punishment for violation of that law until there had been a charge fairly made and fairly tried in a pub-
  <span citation-index="1" class="star-pagination" label="237"> 
   *237
   </span>
  lie tribunal free of prejudice, passion, excitement, and tyrannical power. Thus, as assurance against ancient evils, our country, in order to preserve “the blessings of liberty,” wrote into its basic law the requirement, among others, that the forfeiture of the lives, liberties or property of people accused of crime can only follow if procedural safeguards of due process have been obeyed.
  <a class="footnote" href="#fn10" id="fn10_ref">
   10
  </a>
</p>
<p id="b307-6">
  The determination to preserve an accused’s right to procedural due process sprang in large part from knowledge of the historical truth that the rights and liberties of people accused of crime could not be safely entrusted to secret inquisitorial processes. The testimony of centuries, in governments of varying kinds over populations of different races and beliefs, stood as proof that physical and mental torture and coercion had brought about the tragically unjust sacrifices of some who were the noblest and most useful of their generations. The rack, the thumbscrew, the wheel, solitary confinement, protracted questioning and cross questioning, and other ingenious forms.of entrapment of the helpless or unpopular had .left their wake of mutilated bodies and shattered minds along the way to the cross, the guillotine, the stake and
  <span citation-index="1" class="star-pagination" label="238"> 
   *238
   </span>
  the hangman's noose. And they who have suffered most from -secret and dictatorial proceedings have almost always been the poor, the ignorant, the numerically weak, the friendless, and the powerless.
  <a class="footnote" href="#fn11" id="fn11_ref">
   11
  </a>
</p>
<p id="b308-4">
  This requirement — of conforming to fundamental standards of procedure in criminal trials — was made operative against the States by the Fourteenth Amendment. Where one of several accused had limped into the trial court as a result of admitted physical mistreatment inflicted to obtain confessions upon which a jury had returned a verdict of guilty of murder, this Court recently declared,
  <em>
   Brown
  </em>
  v. Mississippi, that “It would be difficult to conceive of methods more revolting to the sense of justice than those taken to procure the confessions of these petitioners, and the use of the confessions thus obtained as the basis for conviction and sentence was a clear denial of due process.”
  <a class="footnote" href="#fn12" id="fn12_ref">
<em>
    12
   </em>
</a>
</p>
<p id="b308-5">
  Here, the record develops a sharp conflict upon the issue of physical, violence and mistreatment, but shows, without conflict, the dragnet methods of arrest on suspicion without warrant, and the protracted questioning and cross questioning of these ignorant young colored tenant farmers by state officers and other white citizens, in a fourth floor jail room, where as prisoners they were without friends, advisers or counselors, and under circumstances calculated to break the strongest nerves and
  <span citation-index="1" class="star-pagination" label="239"> 
   *239
   </span>
  the stoutest resistance. Just as our decision in
  <em>
   Brown
  </em>
  v.
  <em>
   Mississippi
  </em>
  was based upon the fact that the confessions were the result of compulsion, so in the present case, the admitted practices were such as to justify the statement that “The undisputed facts showed that compulsion was applied.”'
  <a class="footnote" href="#fn13" id="fn13_ref">
   13
  </a>
</p>
<p id="b309-4">
  For five days petitioners were subjected to interrogations culminating in Saturday’s (May 20th) all night examination. Over a period of five days they steadily refused to confess and disclaimed any guilt. The very circumstances surrounding their confinement and their questioning' without any formal charges having been brought, were such as to fill petitioners with terror and frightful misgivings.
  <a class="footnote" href="#fn14" id="fn14_ref">
   14
  </a>
  Some were practical strangers in
  <span citation-index="1" class="star-pagination" label="240"> 
   *240
   </span>
  the community; three were arrested in a one-room farm tenant house which was their home; the haunting fear of mob violence was around them in an atmosphere charged with excitement and public indignation. From virtually the moment of their arrest until their eventual confessions, they never knew just when any one would be called back to the fourth floor room, and there, surrounded by his accusers and others, interrogated by men who held their very lives — so far as these ignorant petitioners could know — in the balance. The rejection of petitioner Woodward’s first “confession,” given in the early hours of Sunday morning, because it was found wanting, demonstrates the relentless tenacity which “broke” petitioners’ will and rendered them helpless to resist their accusers further. To permit human lives to be forfeited upon confessions thus obtained would make of the constitutional requirement of due process of law a meaningless symbol.
 </p>
<p id="b310-5">
  We are not impressed by the argument that law enforcement methods such as those under review are necessary to uphold our laws.
  <a class="footnote" href="#fn15" id="fn15_ref">
   15
  </a>
  The Constitution proscribes
  <span citation-index="1" class="star-pagination" label="241"> 
   *241
   </span>
  such lawless means irrespective of the end. And this argument flouts the basic principle that all people must stand on an equalit-y before the bar of justice in every American court. Today, as in ages past, we are not without tragic proof that the exalted power of some governments to punish manufactured crime dictatorially is the handmaid of tyranny. Under our constitutional system, courts stand against any winds that blow as havens of refuge for those who might otherwise suffer because they are helpless, weak, outnumbered, or because they are non-conforming victims of prejudice and public excitement. Due process of law, preserved for all by our Constitution, commands that no such practice as that disclosed by this record shall send any accused to his death. No higher duty, no more solemn responsibility, rests upon this Court, than that of translating into living law and maintaining this constitutional shield deliberately planned and inscribed for the benefit of every human being subject to our Constitution — of whatever race, creed or persuasion.
 </p>
<p id="b312-3">
<span citation-index="1" class="star-pagination" label="242"> 
   *242
   </span>
  The Supreme Court of .Florida was in' error and' its judgment is
 </p>
<p id="b312-4">
<em>
   Reversed.
  </em>
</p>
<judges id="b312-5">
  Mr. Justice Murphy took no part in the consideration or decision of- this case.
 </judges>















<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b297-15">
   <span class="citation multiple-matches"><a href="/c/U.%20S./308/541/">308 U. S. 541</a></span>.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b297-16">
   Petitioners Williamson, Woodward and Davis pleaded guilty of murder and petitioner Chambers was found guilty by a jury; all
   <span citation-index="1" class="star-pagination" label="228"> 
    *228
    </span>
   were sentenced to death, and the Supreme Court of Florida affirmed. <span class="citation" data-id="3393132"><a href="/opinion/3399600/chambers-v-state/" aria-description="Citation for case: Chambers v. State">111 Fla. 707</a></span>, <span class="citation" data-id="3393132"><a href="/opinion/3399600/chambers-v-state/" aria-description="Citation for case: Chambers v. State">151 So. 499</a></span>; <span class="citation" data-id="3383257"><a href="/opinion/3390999/chambers-v-state/" aria-description="Citation for case: Chambers v. State">152 So. 437</a></span>. Upon the allegation that, unknown to the trial judge, the confessions on which the judgments and sentences of death were based were not voluntary and had been obtained by coercion and. duress, the State Supreme Court granted leave to present a petition for writ of error eoram nobis to the Broward County Circuit Court, <span class="citation" data-id="3393132"><a href="/opinion/3399600/chambers-v-state/" aria-description="Citation for case: Chambers v. State">111 Fla. 707</a></span>; <span class="citation" data-id="3383257"><a href="/opinion/3390999/chambers-v-state/" aria-description="Citation for case: Chambers v. State">152 So. 437</a></span>. The Circuit Court denied the petition without trial of the issues raised by it and the State Supreme Court reversed and ordered the issues submitted to a jury. <span class="citation" data-id="3382712"><a href="/opinion/3390517/chambers-v-state/" aria-description="Citation for case: Chambers v. State">117 Fla. 642</a></span>; <span class="citation" data-id="3382712"><a href="/opinion/3390517/chambers-v-state/" aria-description="Citation for case: Chambers v. State">158 So. 153</a></span>. Upon a verdict adverse to petitioners, the Circuit Court re-affirmed the original judgments and sentences. Again, the State Supreme Court reversed, holding that the issue of force, fear of personal violence and duress had been properly submitted to the jury, but the issue raised by the assignment of error alleging "that the confessions and pleas “were not in fact freely and voluntarily made” had not been clearly submitted to the jury. <span class="citation" data-id="3380781"><a href="/opinion/3388867/chambers-v-state/#737" aria-description="Citation for case: Chambers v. State">123 Fla. 734, 737</a></span>; <span class="citation" data-id="3380781"><a href="/opinion/3388867/chambers-v-state/#700" aria-description="Citation for case: Chambers v. State">167 So. 697, 700</a></span>. A change of venue, to Palm Beach County, was granted, a jury again found against petitioners and the Broward Circuit Court once more reaffirmed the júdgments and sentences of death. The. Supreme Court of Florida, one judge dissenting, affirmed, <span class="citation" data-id="3379805"><a href="/opinion/3388037/chambers-v-state/" aria-description="Citation for case: Chambers v. State">136 Fla. 568</a></span>; <span class="citation" data-id="3379805"><a href="/opinion/3388037/chambers-v-state/" aria-description="Citation for case: Chambers v. State">187 So. 156</a></span>. While the petition thus seeks review of the judgments and sentences of death rendered in the Broward Circuit Court and reaffirmed in the Palm Beach Circuit Court, the evidence before us consists solely of the transcript of proceedings (on writ of error cpram nobis) in Palm- Beach County Court wherein the circumstances surrounding the obtaining of petitioners’ alleged confessions were passed on by a jury.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b298-5">
<em>
    Brown
   </em>
   v.
   <em>
    Mississippi,
   </em>
   <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span>.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b299-7">
<em>
    Pierre
   </em>
   v.
   <em>
    Louisiana,
   </em>
   <span class="citation" data-id="103162"><a href="/opinion/103162/pierre-v-louisiana/#358" aria-description="Citation for case: Pierre v. Louisiana">306 U. S. 354, 358</a></span>;
   <em>
    Norris
   </em>
   v.
   <em>
    Alabama,
   </em>
   <span class="citation" data-id="102407"><a href="/opinion/102407/norris-v-alabama/#590" aria-description="Citation for case: Norris v. Alabama">294 U. S. 587, 590</a></span>.
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b299-8">
   <span class="citation" data-id="3379805"><a href="/opinion/3388037/chambers-v-state/#572" aria-description="Citation for case: Chambers v. State">136 Fla. 568, 572</a></span>; <span class="citation" data-id="3379805"><a href="/opinion/3388037/chambers-v-state/#157" aria-description="Citation for case: Chambers v. State">187 So. 156, 157</a></span>.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b299-9">
<span class="citation" data-id="3379805"><a href="/opinion/3388037/chambers-v-state/#574" aria-description="Citation for case: Chambers v. State"><em>
    Id.,
   </em>
   574</a></span>.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b302-4">
   A constable of the community, testifying about this particular incident, said in part:
  </p>
<blockquote id="b302-5">
   “Q. Were you there when Mr. Maire [State’s Attorney] talked to Walter Woodward the first time he came over there?
  </blockquote>
<blockquote id="b302-6">
   “A. Yes, sir.
  </blockquote>
<blockquote id="b302-7">
   “Q. Take his confession down in writing?
  </blockquote>
<blockquote id="b302-8">
   “A. Yes.
  </blockquote>
<blockquote id="b302-9">
   “Q. If he made a confession why did you all keep on questioning him about it. As a matter of fact, what he said that time wasn’t what you. wanted him to say, was it ?
  </blockquote>
<blockquote id="b302-10">
   “A. It wasn’t what he said the last time.
  </blockquote>
<blockquote id="b302-11">
   “Q. It wasn’t what you wanted him to say, was it?
  </blockquote>
<blockquote id="b302-12">
   “A. We didn’t think it was all correct.
  </blockquote>
<blockquote id="b302-13">
   “ Q. What part of it did you think wasn’t correct. Would you say what he told you there at that time was freely and voluntarily made?
  </blockquote>
<blockquote id="b302-14">
   “A. Yes, sir.
  </blockquote>
<blockquote id="b302-15">
   “Q. What he freely and voluntarily told you in the way of a confession at that time, it wasn’t what you wanted?
  </blockquote>
<blockquote id="b302-16">
   “A. It didn’t make up like it should.
  </blockquote>
<blockquote id="b302-17">
   “Q. What matter didn’t make up ?
  </blockquote>
<blockquote id="b302-18">
   “A. There was some things he told us that couldn’t possible be true.
  </blockquote>
<blockquote id="b302-19">
   “Q. What did'Mr. Maire say about it at that time; did you hear Mr. Maire say at this time 'tear this paper up, that isn’t what I want,
   <span citation-index="1" class="star-pagination" label="233"> 
    *233
    </span>
   when you get something worth while call me,’ or words to that,effect?
  </blockquote>
<blockquote id="ALWq">
   “A. Something similar to that.
  </blockquote>
<blockquote id="b303-12">
   “Q. That did happen that night?
  </blockquote>
<blockquote id="b303-13">
   “A. Yes, sir.
  </blockquote>
<blockquote id="b303-14">
   “Q. That was in the presence of Walter Woodward?
  </blockquote>
<blockquote id="b303-15">
   “A. Yes, sir.”
  </blockquote>
<p id="b303-16">
   And petitioner Woodward testified on this subject as follows:
  </p>
<blockquote id="b303-17">
   “A. ... I was taken out several times on the night of the 20th ... So I still denied it. . . .
  </blockquote>
<blockquote id="b303-18">
   “A. He- said I had told lies and kept him sitting up all the week and he was tired and if I didn't come across I would never see the sun rise.
  </blockquote>
<blockquote id="b303-19">
   “A. . . . then I was taken back to the private cell. . . . and shortly after that they come back, shortly after that, twenty or twenty-five minutes, and bring me out. ... I [told Williams] if he would send for the State Attorney he could take down what I said, I said send for him and I will tell him what I know. So he sent for Mr. Maire some time during Saturday night, must have been around one or two o’clock in the night, it was after midnight, and so he sent for Mr. Maire, I didn’t know Mr. Maire then, but I know him now by his face.
  </blockquote>
<blockquote id="b303-20">
   “A. Well he come in and said 'this boy got something to tell mo’- and Captain Williams says ‘yes, he is ready to tell you.’ ....
  </blockquote>
<blockquote id="b303-21">
   “. . . Mr.'Maire had a pen and a book to take down what I told him, which he said had to be on the typewriter, but I didn’t see any typewriter, I saw him with a pen and book, so whether it was short
   <span citation-index="1" class="star-pagination" label="234"> 
    *234
    </span>
   hand or regular writing I don’t know, but he took it down with pen. After I told him my story he said it was no good, and he tore it up. . . .
  </blockquote>
<blockquote id="b304-14">
   “Q. What was it Mr. Maire said?
  </blockquote>
<blockquote id="b304-15">
   “A. He told them it wasn’t no good, when they got something out of me he would be back. It was late he had to go back and go to bed.
  </blockquote>
<blockquote id="b304-16">
   “A. ... I wasn’t in the cell long before they come back. . . .
  </blockquote>
<blockquote id="b304-17">
   “Q. How long was that from the time you was brought into that room until Mr. Maire left there?
  </blockquote>
<blockquote id="b304-18">
   “A. Something like two or three hours, I guess, because it was around sunrise when I went into the room.
  </blockquote>
<blockquote id="b304-19">
   “Q. Had you slept any that night, Walter?
  </blockquote>
<blockquote id="b304-20">
<em>
    “A.
   </em>
   No, sir. I was wálked all night, not continually, but I didn’t have no time R- sleep except in short spaces of the night.
  </blockquote>
<blockquote id="b304-21">
   "Q. When Mr. Maire got there it was after daylight?
  </blockquote>
<blockquote id="b304-22">
   “A. Yes, sir.
  </blockquote>
<blockquote id="b304-23">
   “Q. Why did you say to them that morning anything after you were brought into the room?
  </blockquote>
<blockquote id="b304-24">
<em>
    “A.
   </em>
   Because I was scared, ...
  </blockquote>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b305-10">
   There have been long-continued and constantly recurring differences of opinion as -to whether general 1-gislative acts regulating the use of property could be invalidated as violating the-due process clause of the Fourteenth Amendment.
   <em>
    Munn
   </em>
   v.
   <em>
    Illinois,
   </em>
   <span class="citation" data-id="9417073"><a href="/opinion/89446/munn-v-illinois/#125" aria-description="Citation for case: Munn v. Illinois">94 U. S. 113, 125</a></span>, dissent 136-154;
   <em>
    Chicago M. &amp; St. P. R. Co.
   </em>
   v. Minnesota,
   <span citation-index="1" class="star-pagination" label="236"> 
    *236
    </span>
   <span class="citation" data-id="9841772"><a href="/opinion/92743/chicago-milwaukee-st-paul-railway-co-v-minnesota/" aria-description="Citation for case: Chicago, Milwaukee &amp; St. Paul Railway Co. v. Minnesota">134 U. S. 418</a></span>, dissent 461-466. And there has been a current of opinion — which this court has declined to adopt in many previous cases — that the Fourteenth Amendment was intended to make secure against state invasion all the rights, privileges and immunities protected from federal violation by the Bill of Rights (Amendments I to VIII). See, e. g.,
   <em>
    Twining
   </em>
   v.
   <em>
    New Jersey,
   </em>
   <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#98" aria-description="Citation for case: Twining v. New Jersey">211 U. S. 78, 98-9</a></span>, Mr. Justice Harlan, dissenting, 114;
   <em>
    Maxwell
   </em>
   v.
   <em>
    Dow,
   </em>
   <span class="citation" data-id="9417812"><a href="/opinion/95204/maxwell-v-dow/" aria-description="Citation for case: Maxwell v. Dow">176 U. S. 581</a></span>, dissent 606;
   <em>
    O’Neil
   </em>
   v.
   <em>
    Vermont,
   </em>
   <span class="citation" data-id="9841791"><a href="/opinion/93324/oneil-v-vermont/" aria-description="Citation for case: O&#x27;Neil v. Vermont">144 U. S. 323</a></span>, dissent 361;
   <em>
    Palko
   </em>
   v.
   <em>
    Connecticut,
   </em>
   <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319, 325, 326</a></span>;
   <em>
    Hague
   </em>
   v.
   <em>
    C. I. O.,
   </em>
   <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">307 U. S. 496</a></span>.
  </p>
</div><div class="footnote" id="fn9" label="9">
<a class="footnote" href="#fn9_ref">
   9
  </a>
<p id="b306-7">
   Cf.
   <em>
    Weems
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9418181"><a href="/opinion/97242/weems-v-united-states/#372" aria-description="Citation for case: Weems v. United States">217 U. S. 349, 372, 373</a></span>, and dissent setting out (p. 396) argument of Patrick Henry, 3 Elliot, Debates 447.
  </p>
</div><div class="footnote" id="fn10" label="10">
<a class="footnote" href="#fn10_ref">
   10
  </a>
<p id="b307-7">
   As adopted, the Constitution provided, “The Privilege of the Writ of Habeas Corpus shall not be suspended, unless when in Cases of Rebellion or Invasion the public Safety may require it.” (Art. I, § 9.) “No Bill of Attainder or ex post facto Law shall be passed”
   <em>
    (Id.),
   </em>
   “No State shall . .. pass any Bill of Attainder, or ex post facto Law. .
   <em>
    .(Id.,
   </em>
   § 10), and “No Person shall be convicted of Treason unless on the Testimony of two Witnesses to the same overt Act, or on Confession in open Court” (Art. III, § 3). The Bill of Rights (Amend. I to VIII). Cf. Magna Carta, 1297 (<span class="citation no-link">25 Edw. 1</span>); The Petition of Right, 1627 (3 Car. 1, c. 1.); The Habeas Corpus Act, 1640 (16 Car. 1, c. 10.), An Act for [the Regulating] the Privie Councell and for taking away the Court commonly called the Star Chamber; Stat. (1661) 13 Car. 2, Stat. 1, C. 1 (Treason); The Bill of Rights (1688) (1 Will. &amp; Mar. sess. 2, c. 2.); all collected in “Halsbury’s Stat. of Eng.” (1929) Vol. 3.
  </p>
</div><div class="footnote" id="fn11" label="11">
<a class="footnote" href="#fn11_ref">
   11
  </a>
<p id="b308-6">
   “In-all third degree cases, it is remarkable to note that the confessions were taken from ‘men of humble station in life and of a comparatively low degree of intelligence, and most of them apparently too poor to employ counsel and too friendless to have any one advise them of their rights.’” Filamor, “Third Degree Confession,” 13 Bombay L. J., 339, 346. “That the third degree is especially used against the poor and uninfluential is asserted by several writers, and confirmed by official informants and judicial decisions.” IV National Commission On Law Observance and Enforcement, Reports, (1931) Ch. 3, p. 159. Cf.
   <em>
    Morrison
   </em>
   v.
   <em>
    California,
   </em>
   <span class="citation" data-id="102188"><a href="/opinion/102188/morrison-v-california/#95" aria-description="Citation for case: Morrison v. California">291 U. S. 82, 95</a></span>.
  </p>
</div><div class="footnote" id="fn12" label="12">
<a class="footnote" href="#fn12_ref">
   12
  </a>
<p id="b308-7">
   <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#286" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278, 286</a></span>.
  </p>
</div><div class="footnote" id="fn13" label="13">
<a class="footnote" href="#fn13_ref">
   13
  </a>
<p id="b309-5">
   See
   <em>
    Ziang Sung Wan
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/#16" aria-description="Citation for case: Ziang Sung Wan v. United States">266 U. S. 1, 16</a></span>. The dissenting Judge below noted, <span class="citation" data-id="3379805"><a href="/opinion/3388037/chambers-v-state/#576" aria-description="Citation for case: Chambers v. State">136 Fla. 568, 576</a></span>; <span class="citation" data-id="3379805"><a href="/opinion/3388037/chambers-v-state/#159" aria-description="Citation for case: Chambers v. State">187 So. 156, 159</a></span>, that, in a prior appeal of this same case, the Supreme Court of Florida had said: “Even if the jury totally disbelieved the testimony of the petitioners, the testimony of Sheriff Walter Clark, and one or two of the other witnesses introduced by the State, was sufficient to show that these confessions were only made after such' constantly repeated and persistent questioning and cross-questioning on the part of the officers and one J. T. Williams, a convict guard, at frequent intervals while they were in jail, over a period of about a week, and culminating in an all-night questioning of the petitioners separately in succession, throughout practically all of Saturday night, until confessions had been obtained from all of them, when they were all brought into a room in the jailer’s quarters at 6:30 on Sunday morning and made their confessions before the state attorney, the officers, said J. T. Williams, and several disinterested outsiders, the confessions, in the form of questions and answers, being taken down by the court reporter, and then typewritten.
  </p>
<blockquote id="b309-6">
   “Under the principles laid down in Nickels
   <em>
    v.
   </em>
   State, <span class="citation" data-id="3381494"><a href="/opinion/3389464/nickels-v-state/" aria-description="Citation for case: Nickels v. State">90 Fla. 659</a></span>, <span class="citation" data-id="3381494"><a href="/opinion/3389464/nickels-v-state/" aria-description="Citation for case: Nickels v. State">106 So. 479</a></span>; Davis
   <em>
    v.
   </em>
   State, <span class="citation" data-id="4921824"><a href="/opinion/5103863/davis-v-state/" aria-description="Citation for case: Davis v. State">90 Fla. 317</a></span>, <span class="citation" data-id="3390887"><a href="/opinion/3397624/daviss-v-state/" aria-description="Citation for case: Daviss. v. State">105 So. 843</a></span>; Deiterle
   <em>
    v.
   </em>
   State <span class="citation" data-id="3396558"><a href="/opinion/3402562/deiterle-v-state/" aria-description="Citation for case: Deiterle v. State">98 Fla. 739</a></span>, <span class="citation" data-id="3396558"><a href="/opinion/3402562/deiterle-v-state/" aria-description="Citation for case: Deiterle v. State">124 So. 47</a></span>; Mathieu
   <em>
    v.
   </em>
   State, <span class="citation" data-id="3390304"><a href="/opinion/3397120/mathieu-v-state/" aria-description="Citation for case: Mathieu v. State">101 Fla. 94</a></span>, <span class="citation" data-id="3390304"><a href="/opinion/3397120/mathieu-v-state/" aria-description="Citation for case: Mathieu v. State">133 So. 550</a></span>, these confessions were not legally obtained.” <span class="citation" data-id="3380781"><a href="/opinion/3388867/chambers-v-state/#741" aria-description="Citation for case: Chambers v. State">123 Fla. 734, 741</a></span>; <span class="citation" data-id="3380781"><a href="/opinion/3388867/chambers-v-state/#700" aria-description="Citation for case: Chambers v. State">167 So. 697, 700</a></span>.
  </blockquote>
</div><div class="footnote" id="fn14" label="14">
<a class="footnote" href="#fn14_ref">
   14
  </a>
<p id="b309-7">
   Cf. the statement of the Supreme Court of Arkansas,
   <em>
    Bell
   </em>
   v.
   <em>
    State,
   </em>
   <span class="citation" data-id="3267432"><a href="/opinion/3265128/bell-v-state/#89" aria-description="Citation for case: Bell v. State">180 Ark. 79, 89</a></span>; <span class="citation" data-id="3267432"><a href="/opinion/3265128/bell-v-state/" aria-description="Citation for case: Bell v. State">20 S. W. 2d 618</a></span>, 622: “This negro boy was
   <span citation-index="1" class="star-pagination" label="240"> 
    *240
    </span>
   taken, on the day after the discovery of the homicide while he was at his usual work, and placed in jail. He had heard them whipping Swain in the jail; he was taken from the jail to the penitentiary at Little Rock and turned over to the warden, Captain Todhunter, who was requested by the sheriff to question him. This Todhunter proceeded to do, day after day, an hour at a time. There Bell was, an ignorant country boy surrounded by all of those things that strike terror to the negro heart; . . ." See Münsterberg, On the Witness Stand, (1927) 137
   <em>
    et seq.
   </em>
</p>
</div><div class="footnote" id="fn15" label="15">
<a class="footnote" href="#fn15_ref">
   15
  </a>
<p id="b310-7">
   The police practices here examined are to some degree widespread throughout our country. See Report of Comm. on Lawless Enforcement of the Law (Amer. Bar Ass’n) 1 Amer. Journ. of Pol. Sci., 575; Note 43 H. L. R. 617; IV National Commission On Law Observance And Enforcement,
   <em>
    supra,
   </em>
   Ch. 2, § 4. Yet our national record for crime detection and criminal law enforcement compares poorly with that of Great Britain where secret interrogation of an
   <span citation-index="1" class="star-pagination" label="241"> 
    *241
    </span>
   accused or suspect is not tolerated. See, Report of Comm. on Lawless Enforcement of the Law,
   <em>
    supra,
   </em>
   588; 43 H. L. <span class="citation" data-id="9841772"><a href="/opinion/92743/chicago-milwaukee-st-paul-railway-co-v-minnesota/#618" aria-description="Citation for case: Chicago, Milwaukee &amp; St. Paul Railway Co. v. Minnesota">R.,
   <em>
    supra,
   </em>
   618</a></span>. It has even been suggested that the use of the “third degree” has lowered the esteem in which administration of justice is held by the public and has engendered an attitude of hostility to and unwillingness to cooperate with the police on the part of many people. See, IV National Commission, etc.,
   <em>
    supra,
   </em>
   p. 190. And, after scholarly investigation, the conclusion has been reached “that such methods, aside from their brutality, tend in the long run to defeat their ówn purpose; they encourage inefficiency on the part of the police.” Glueck, Crime and Justice, (1936) 76. See IV National Commission, etc.,
   <em>
    supra,
   </em>
   5; cf. 4 Wigmore, Evidence, (2d ed.) § 2251. The requirement that an accused be brought promptly before a magistrate has been sought by some as a solution to the problem of fostering law enforcement without sacrificing the liberties and procedural rights of the individual. 2 Wig.,
   <em>
    supra,
   </em>
   § 851, IV National Commission, etc.,
   <em>
    supra,
   </em>
   5.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Chambers v. Maroney.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Chambers v. Maroney"
type: case
citation: "399 U.S. 42 (1970)"
parallel_cite: "90 S. Ct. 1975; 26 L. Ed. 2d 419"
neutral_cite: 1970 U.S. LEXIS 19
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1970
date_decided: 1970-10-12
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1970-06-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Chambers v. Maroney
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108184/chambers-v-maroney/"
  cluster_id: 108184
  opinion_id: 9424320
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[Carroll v. United States]]", "[[California v. Acevedo]]", "[[California v. Carney]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "warrantless-search", "vehicle", "station-house"]
holding: "Where there was PC and mobility at the scene, officers may search the vehicle without a warrant later at the station house; immediate…"
lake:
  record_id: Chambers v. Maroney
  status: verified
  projected_at: 2026-07-06
---

# Chambers v. Maroney

*399 U.S. 42 (1970)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police, acting on probable cause from witness descriptions, stopped a station wagon shortly after an armed service-station robbery, arrested the occupants, and drove the car to the police station, where they searched it without a warrant and found weapons and evidence of the robbery. Chambers challenged the warrantless station-house search.

## Issue
Whether police who had probable cause and a lawfully stopped vehicle at the scene may instead search it without a warrant later at the station house.

## Rule
Yes. Given probable cause to search a vehicle that was mobile when stopped, a warrantless search at the station house is reasonable: "For constitutional purposes, we see no difference between on the one hand seizing and holding a car before presenting the probable cause issue to a magistrate and on the other hand carrying out an immediate search without a warrant. Given probable cause to search, either course is reasonable under the Fourth Amendment." — 399 U.S. 42, 52. ^pin-52

## Application
The officers had probable cause to search the station wagon and could lawfully have searched it on the spot, where it was a "fleeting target." Because both the probable cause and the car's mobility persisted, searching it without a warrant after it had been taken to the station house was, on these facts, no less reasonable than an immediate roadside search.

## Conclusion
The warrantless station-house search was reasonable; the conviction was upheld. *Chambers* extends the [[Carroll v. United States]] automobile exception to a later search away from the scene.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Chambers* elaborates the [[Carroll v. United States]] rule and is part of the line later unified for containers in [[California v. Acevedo]] and grounded in the exception's two justifications in [[California v. Carney]].

## Appears on
- [[Automobile Exception]] — *Key — Progeny / Refinement*

## Sources
- *Chambers v. Maroney*, 399 U.S. 42 (1970) — https://www.courtlistener.com/opinion/108184/chambers-v-maroney/ — pinpoint: 52.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "fadd5866bc60e216", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Chambers v. Maroney"}, "payload": {"all": [{"cite": "399 U.S. 42", "page": "42", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "399"}, {"cite": "90 S. Ct. 1975", "page": "1975", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "90"}, {"cite": "26 L. Ed. 2d 419", "page": "419", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "26"}, {"cite": "1970 U.S. LEXIS 19", "page": "19", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1970"}], "display": "399 U.S. 42", "official": {"cite": "399 U.S. 42", "page": "42", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "399"}, "official_selection_present": true, "record_id": "Chambers v. Maroney"}}
{"assertion_id": "f18bbfe5a5ea69e2", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-52", "record_id": "Chambers v. Maroney"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-52", "pinpoint_status": "slip-only", "quote": "--- # Chambers v. Maroney *399 U.S. 42 (1970)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police, acting on probable cause from witness descriptions, stopped a station wagon shortly after an armed service-station robbery, arrested the occupants, and drove the car to the police station, where they searched it without a warrant and found weapons and evidence of the robbery. Chambers challenged the warrantless station-house search. ## Issue Whether police who had probable cause and a lawfully stopped vehicle at the scene may instead search it without a warrant later at the station house. ## Rule Yes. Given probable cause to search a vehicle that was mobile when stopped, a warrantless search at the station house is reasonable:", "quote_fidelity": "mismatch", "record_id": "Chambers v. Maroney", "star_marker": null}}
{"assertion_id": "cf423a24c54fd5d7", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Chambers v. Maroney"}, "payload": {"as_of_content": "1970-06-22", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Chambers v. Maroney", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Chambers v. Maroney

```json
{
  "schema_version": "s2.v1",
  "record_id": "Chambers v. Maroney",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Chambers v. Maroney",
    "case_name_short": "Chambers",
    "case_name_full": "Chambers v. Maroney, Correctional Superintendent",
    "input_case_name": "Chambers v. Maroney",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1970-10-12",
    "year": 1970,
    "docket": null,
    "cluster_id": 108184,
    "lead_opinion_id": 9424320,
    "sibling_ids": [
      108184,
      9424320,
      9424321,
      9424322
    ],
    "absolute_url": "/opinion/108184/chambers-v-maroney/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8978955,
        "score": 20,
        "case_name": "Chambers v. Maroney"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "399 U.S. 42",
      "volume": "399",
      "reporter": "U.S.",
      "page": "42",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "90 S. Ct. 1975",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "1975",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 L. Ed. 2d 419",
        "volume": "26",
        "reporter": "L. Ed. 2d",
        "page": "419",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1970 U.S. LEXIS 19",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "19",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "399 U.S. 42",
        "volume": "399",
        "reporter": "U.S.",
        "page": "42",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 S. Ct. 1975",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "1975",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 L. Ed. 2d 419",
        "volume": "26",
        "reporter": "L. Ed. 2d",
        "page": "419",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1970 U.S. LEXIS 19",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "19",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "399 U.S. 42",
    "official_selection": {
      "court_class": "scotus",
      "selected": "399 U.S. 42",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-52",
      "page": null,
      "quote": "--- # Chambers v. Maroney *399 U.S. 42 (1970)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police, acting on probable cause from witness descriptions, stopped a station wagon shortly after an armed service-station robbery, arrested the occupants, and drove the car to the police station, where they searched it without a warrant and found weapons and evidence of the robbery. Chambers challenged the warrantless station-house search. ## Issue Whether police who had probable cause and a lawfully stopped vehicle at the scene may instead search it without a warrant later at the station house. ## Rule Yes. Given probable cause to search a vehicle that was mobile when stopped, a warrantless search at the station house is reasonable:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1970-06-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Chambers v. Maroney",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. McCarthy",
          "cluster_id": 10160868,
          "cite": [
            "369 Or. 129",
            "501 P.3d 478"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Podrazo",
          "cluster_id": 2645492,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Williams v. State",
          "cluster_id": 2542111,
          "cite": [
            "356 S.W.3d 508",
            "2011 WL 5220350"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Curtis Leo Williams v. State",
          "cluster_id": 3089627,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dahlem v. State",
          "cluster_id": 2274819,
          "cite": [
            "322 S.W.3d 685",
            "2010 WL 1854413"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane1_negative"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cronic",
          "cluster_id": 111169,
          "cite": [
            "80 L. Ed. 2d 657",
            "104 S. Ct. 2039",
            "466 U.S. 648",
            "1984 U.S. LEXIS 78",
            "52 U.S.L.W. 4560"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. Sykes",
          "cluster_id": 109717,
          "cite": [
            "53 L. Ed. 2d 594",
            "97 S. Ct. 2497",
            "433 U.S. 72",
            "1977 U.S. LEXIS 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Fulminante",
          "cluster_id": 112566,
          "cite": [
            "113 L. Ed. 2d 302",
            "111 S. Ct. 1246",
            "499 U.S. 279",
            "1991 U.S. LEXIS 1854"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Belton",
          "cluster_id": 110559,
          "cite": [
            "69 L. Ed. 2d 768",
            "101 S. Ct. 2860",
            "453 U.S. 454",
            "1981 U.S. LEXIS 13"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Opperman",
          "cluster_id": 109537,
          "cite": [
            "49 L. Ed. 2d 1000",
            "96 S. Ct. 3092",
            "428 U.S. 364",
            "1976 U.S. LEXIS 15"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cady v. Dombrowski",
          "cluster_id": 108850,
          "cite": [
            "37 L. Ed. 2d 706",
            "93 S. Ct. 2523",
            "413 U.S. 433",
            "1973 U.S. LEXIS 48"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rose v. Clark",
          "cluster_id": 111750,
          "cite": [
            "92 L. Ed. 2d 460",
            "106 S. Ct. 3101",
            "478 U.S. 570",
            "1986 U.S. LEXIS 135",
            "54 U.S.L.W. 5023"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morris v. Slappy",
          "cluster_id": 110914,
          "cite": [
            "75 L. Ed. 2d 610",
            "103 S. Ct. 1610",
            "461 U.S. 1",
            "1983 U.S. LEXIS 5",
            "51 U.S.L.W. 4399"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marshall v. Barlow's, Inc.",
          "cluster_id": 109866,
          "cite": [
            "56 L. Ed. 2d 305",
            "98 S. Ct. 1816",
            "436 U.S. 307",
            "1978 U.S. LEXIS 26",
            "8 Envtl. L. Rep. (Envtl. Law Inst.) 20434",
            "6 OSHC (BNA) 1571"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
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
        "journal_ref": "Chambers v. Maroney:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108184 OR 9424320 OR 9424321 OR 9424322) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjEzNjYwODAwMDAwJnM9MjMzNTE5NSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108184+OR+9424320+OR+9424321+OR+9424322%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108184 OR 9424320 OR 9424321 OR 9424322)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MDMmcz0xMTA1NTgmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28108184+OR+9424320+OR+9424321+OR+9424322%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108184 OR 9424320 OR 9424321 OR 9424322)",
        "reviewed": 31,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 31,
        "triage_read": 0,
        "triage_snippet_classified": 31
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108184 OR 9424320 OR 9424321 OR 9424322)",
    "indexed_citing_opinions": 2970,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108184,
        "count": 2726,
        "count_source": "search"
      },
      {
        "opinion_id": 9424320,
        "count": 358,
        "count_source": "search"
      },
      {
        "opinion_id": 9424321,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424322,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4392,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/chambers-v-maroney.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1MTM2Mjgmcz05NDM5ODM1JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108184+OR+9424320+OR+9424321+OR+9424322%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108184,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 103100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 103272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 103597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 104196,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 106191,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107689,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107952,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 108138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 284134,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 286933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108184,
        "cited_id": 1236300,
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
    "date_created": "2026-07-04T23:47:16Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:47:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:47:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:50:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:47:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Chambers v. Maroney

```
<opinion type="majority">
<author id="b79-13">Mr. Justice White</author>
<p id="AG1">delivered the opinion of the Court.</p>
<p id="A5B">The principal question in this case concerns the admissibility of evidence seized from an automobile, in which petitioner was riding at the time of his arrest, after the automobile was taken to a police station and was there thoroughly searched without a warrant. The Court of Appeals for the Third Circuit found no violation of petitioner’s Fourth Amendment rights. We affirm.</p>
<p id="b80-5"><page-number citation-index="1" label="44">*44</page-number>I</p>
<p id="b80-6">During the night of May 20, 1963, a Gulf service station in North Braddock, Pennsylvania, was robbed by two men, each of whom carried and displayed a gun. The robbers took the currency from the cash register; the service station attendant, one Stephen Kovacich, was directed to place the coins in his right-hand glove, which was then taken by the robbers. Two teen-agers, who had earlier noticed a blue compact station wagon circling the block in the vicinity of the Gulf station, then saw the station wagon speed away from a parking lot close to the Gulf station. About the same time, they learned that the Gulf station had been robbed. They reported to police, who arrived immediately, that four men were in the station wagon and one was wearing a green sweater. Kova-cich told the police that one of the men who robbed him was wearing a green sweater and the other was wearing a trench coat. A description of the car and the two robbers was broadcast over the police radio. Within an hour, a light blue compact station wagon answering the description and carrying four men was stopped by the police about two miles from the Gulf station. Petitioner was one of the men in the station wagon. He was wearing a green sweater and there was a trench coat in the car. The occupants were arrested and the car was driven to the police station. In the course of a thorough search of the car at the station, the police found concealed in a compartment under the dashboard two .38-caliber revolvers (one loaded with dumdum bullets), a right-hand glove containing small change, and certain cards bearing the name of Raymond Havicon, the attendant at a Boron service station in McKeesport, Pennsylvania, who had been robbed at gunpoint on May 13, 1963. In the course of a warrant-authorized search of petitioner’s home the day after petitioner’s arrest, police found and <page-number citation-index="1" label="45">*45</page-number>seized certain .38-caliber ammunition, including some dumdum bullets similar' to those found in one of the guns taken from the station wagon.</p>
<p id="b81-5">Petitioner was indicted for both robberies.<footnotemark>1</footnotemark> His first trial ended in a mistrial but he was convicted of both robberies at the second trial. Both Kovacieh and Hav-icon identified petitioner as one of the robbers.<footnotemark>2</footnotemark> The materials taken from the station wagon were introduced into evidence, Kovacieh identifying his glove and Hav-icon the cards taken in the May 13 robbery. The bullets seized at petitioner’s house were also introduced over objections of petitioner’s counsel.<footnotemark>3</footnotemark> Petitioner was sentenced to a term of four to eight years’ imprisonment for the May 13 robbery and to a term of two to seven years’ imprisonment for the May 20 robbery, the sentences to run consecutively.<footnotemark>4</footnotemark> Petitioner did not take a direct appeal from these convictions. In 1965, petitioner sought a writ of habeas corpus in the state court, which denied the writ after a brief evidentiary hearing; the denial of <page-number citation-index="1" label="46">*46</page-number>the writ was affirmed on appeal in the Pennsylvania appellate courts. Habeas corpus proceedings were then commenced in the United States District Court for the Western District of Pennsylvania. An order to show cause was issued. Based on the State’s response and the state court record, the petition for habeas corpus was denied without a hearing. The Court of Appeals for the Third Circuit affirmed, <span class="citation" data-id="284134"><a href="/opinion/284134/united-states-of-america-ex-rel-frank-chambers-v-james-f-maroney/" aria-description="Citation for case: United States of America Ex Rel. Frank Chambers v. James...">408 F. 2d 1186</a></span>, and we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./396/900/">396 U. S. 900</a></span> (1969).<footnotemark>5</footnotemark></p>
<p id="b82-6">II</p>
<p id="b82-7">We pass quickly the claim that the search of the automobile was the fruit of an unlawful arrest. Both the courts below thought the arresting officers had probable cause to make the arrest. We agree. Having talked to the teen-age observers and to the victim Kova-cich, the police had ample cause to stop a light blue compact station wagon carrying four men and to arrest the occupants, one of whom was wearing a green sweater <page-number citation-index="1" label="47">*47</page-number>and one of whom had a trench coat with him in the car.<footnotemark>6</footnotemark></p>
<p id="b83-4">Even so, the search that produced the incriminating evidence was made at the police station some time after the arrest and cannot be justified as a search incident to an arrest: “Once an accused is under arrest and in custody, then a search made at another place, without a warrant, is simply not incident to the arrest.” <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964). <em>Dyke </em>v. <em>Taylor Implement Mfg. Co., </em><span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S. 216</a></span> (1968), is to the same effect; the reasons that have been thought sufficient to justify warrantless searches carried out in connection with an. arrest no longer obtain when the accused is safely in custody at the station house.</p>
<p id="b83-5">There are, however, alternative grounds arguably justifying the search of the car in this case. In <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston, supra,</a></span> </em>the arrest was for vagrancy; it was apparent that the officers had no cause to believe that evidence of crime was concealed in the auto. In <em><span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">Dyke, supra,</a></span> </em>the Court expressly rejected the suggestion that there was probable cause to search the car, <span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/#221" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S., at 221-222</a></span>. Here the situation is different, for the police had probable cause to believe that the robbers, carrying guns and the fruits of the crime, had fled the scene in a light blue compact station wagon which would be carrying four men, one wearing a green sweater and another wearing a trench coat. As the state courts correctly held, there was probable cause to arrest the occupants of the station wagon that the officers stopped; just as obviously was <page-number citation-index="1" label="48">*48</page-number>there probable cause to search the car for guns and stolen money.</p>
<p id="b84-4">In terms of the circumstances justifying a warrantless search, the Court has long distinguished between an automobile and a home or office. In <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), the issue was the admissibility in evidence of contraband liquor seized in a war-rantless search of a car on the highway. After surveying the law from the time of the adoption of the Fourth Amendment onward, the Court held that automobiles and other conveyances may be searched without a warrant in circumstances that would not justify the search without a warrant of a house or an office, provided that there is probable cause to believe that the car contains articles that the officers are entitled to seize. The Court expressed its holding as follows:</p>
<blockquote id="b84-5">“We have made a somewhat extended reference to these statutes to show that the guaranty of freedom from unreasonable searches and seizures by the Fourth Amendment has been construed, practically since the beginning of the Government, as recognizing a necessary difference between a search of a store, dwelling house or other structure in respect of which a proper official warrant readily may be obtained, and a search of a ship, motor boat, wagon or automobile, for contraband goods, where it is not practicable to secure a warrant because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought.</blockquote>
<blockquote id="b84-6">“Having thus established that contraband goods concealed and illegally transported in an automobile or other vehicle may be searched for without a warrant, we come now to consider under what circumstances such search may be made. . . . [T]hose lawfully within the country, entitled to use <page-number citation-index="1" label="49">*49</page-number>the public highways, have a right to free passage without interruption or search unless there is known to a competent official authorized to search, probable cause for believing that their vehicles are carrying contraband or illegal merchandise. . . .</blockquote>
<blockquote id="b85-5">“The measure of legality of such a seizure is, therefore, that the seizing officer shall have reasonable or probable cause for believing that the automobile which he stops and seizes has contraband liquor therein which is being illegally transported.” <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S., at 153-154, 155-156</a></span>.</blockquote>
<p id="b85-6">The Court also noted that the search of an auto on probable cause proceeds on a theory wholly different from that justifying the search incident to an arrest:</p>
<blockquote id="b85-7">“The right to search and the validity of the seizure are not dependent on the right to arrest. They are dependent on the reasonable cause the seizing officer has for belief that the contents of the automobile offend against the law.” <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S., at 158-159</a></span>.</blockquote>
<p id="b85-8">Finding that there was probable cause for the search and seizure at issue before it, the Court affirmed the convictions.</p>
<p id="b85-9"><em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>was followed and applied in <em>Husty </em>v. <em>United States, </em><span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/" aria-description="Citation for case: Husty v. United States">282 U. S. 694</a></span> (1931), and <em>Scher </em>v. <em>United States, </em><span class="citation" data-id="103100"><a href="/opinion/103100/scher-v-united-states/" aria-description="Citation for case: Scher v. United States">305 U. S. 251</a></span> (1938). It was reaffirmed and followed in <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949). In 1964, the opinion in <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston, supra,</a></span> </em>cited both <em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span> </em>and <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>with approval, <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#366" aria-description="Citation for case: Preston v. United States">376 U. S., at 366-367</a></span>. In <em>Cooper </em>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span> (1967),<footnotemark>7</footnotemark> <page-number citation-index="1" label="50">*50</page-number>the Court read <em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston</a></span> </em>as dealing primarily with a search incident to arrest and cited that case for the proposition that the mobility of a car may make the search of a car without a warrant reasonable “although the result might be the opposite in a search of a home, a store, or other fixed piece of property.” <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#59" aria-description="Citation for case: Cooper v. California">386 U. S., at 59</a></span>. The Court’s opinion in <em>Dyke, </em><span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/#221" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S., at 221</a></span>, recognized that “[a]utomobiles, because of their mobility, may be searched without a warrant upon facts not justifying a warrantless search of a residence or office,” citing <em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span> </em>and <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll, supra.</a></span> </em>However, because there was insufficient reason to search the car involved in the <em><span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">Dyke</a></span> </em>case, the Court did not reach the question of whether those cases “extend to a warrant-less search, based upon probable cause, of an automobile which, having been stopped originally on a highway, is parked outside a courthouse.” <span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/#222" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S., at 222</a></span>.<footnotemark>8</footnotemark></p>
<p id="AKg">Neither <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll, supra,</a></span> </em>nor other cases in this Court require or suggest that in every conceivable circumstance the search of an auto even with probable cause may be made without the extra protection for privacy that a warrant affords. But the circumstances that <page-number citation-index="1" label="51">*51</page-number>furnish probable cause to search a particular auto for particular articles are most often unforeseeable; moreover, the opportunity to search is fleeting since a car is readily movable. Where this is true, as in <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>and the case before us now, if an effective search is to be made at any time, either the search must be made immediately without a warrant or the car itself must be seized and held without a warrant for whatever period is necessary to obtain a warrant for the search.<footnotemark>9</footnotemark></p>
<p id="b87-5">In enforcing the Fourth Amendment’s prohibition against unreasonable searches and seizures, the Court has insisted upon probable cause as a minimum requirement for a reasonable search permitted by the Constitution. As a general rule, it has also required the judgment of a magistrate on the probable-cause issue and the issuance of a warrant before a search is made. Only in exigent circumstances will the judgment of the police as to probable cause serve as a sufficient authorization for a search. <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll, supra,</a></span> </em>holds a search warrant unnecessary where there is probable cause to search an automobile stopped on the highway; the car is movable, the occupants are alerted, and the car’s contents may never be found again if a warrant must be obtained. Hence an immediate search is constitutionally permissible.</p>
<p id="b87-6">Arguably, because of the preference for a magistrate’s judgment, only the immobilization of the car should be permitted until a search warrant is obtained; arguably, only the “lesser” intrusion is permissible until the magistrate authorizes the “greater.” But which is the “greater” and which the “lesser” intrusion is itself a debatable question and the answer may depend on a variety <page-number citation-index="1" label="52">*52</page-number>of circumstances. For constitutional purposes, we see no difference between on the one hand seizing and holding a car before presenting the probable cause issue to a magistrate and on the other hand carrying out an immediate search without a warrant. Given probable cause to search, either course is reasonable under the Fourth Amendment.</p>
<p id="b88-5">On the facts before us, the blue station wagon could have been searched on the spot when it was stopped since there was probable cause to search and it was a fleeting target for a search. The probable-cause factor still obtained at the station house and so did the mobility of the car unless the Fourth Amendment permits a warrantless seizure of the car and the denial of its use to anyone until a warrant is secured. In that event there is little to choose in terms of practical consequences between an immediate search without a warrant and the car’s immobilization until a warrant i's obtained.<footnotemark>10</footnotemark> The same consequences may not follow where there is unforeseeable cause to search a house. Compare <em>Vale </em>v. <em>Louisiana, ante, </em>p. 30. But as <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll, supra,</a></span> </em>held, for the purposes of the Fourth Amendment there is a constitutional difference between houses and cars.</p>
<p id="b88-6">Ill</p>
<p id="b88-7">Neither of petitioner’s remaining contentions warrants reversal of the judgment of the Court of Appeals. One of them challenges the admissibility at trial of the .38-caliber ammunition seized in the course of a search of petitioner’s house. The circumstances relevant to this <page-number citation-index="1" label="53">*53</page-number>issue are somewhat confused, involving as they do questions of probable cause, a lost search warrant, and the Pennsylvania procedure for challenging the admissibility of evidence seized. Both the District Court and the Court of Appeals, however, after careful examination of the record, found that if there was error in admitting the ammunition, the error was harmless beyond a reasonable doubt. Having ourselves studied this record, we are not prepared to differ with the two courts below. See <em>Harrington </em>v. <em>California, </em><span class="citation" data-id="9424056"><a href="/opinion/107952/harrington-v-california/" aria-description="Citation for case: Harrington v. California">395 U. S. 250</a></span> (1969).</p>
<p id="b89-5">The final claim is that petitioner was not afforded the effective assistance of counsel. The facts pertinent to this claim are these: The Legal Aid Society of Allegheny County was appointed to represent petitioner prior to his first trial. A representative of the society conferred with petitioner, and a member of its staff, Mr. Middleman, appeared for petitioner at the first trial. There is no claim that petitioner was not then adequately represented by fully prepared counsel. The difficulty arises out of the second trial. Apparently no one from the Legal Aid Society again conferred with petitioner until a few minutes before the second trial began. The attorney who then appeared to represent petitioner was not Mr. Middleman but Mr. Tamburo, another Legal Aid Society attorney. No charge is made that Mr. Tamburo was incompetent or inexperienced; rather the claim is that his appearance for petitioner was so belated that he could not have furnished effective legal assistance at the second trial. Without granting an evidentiary hearing, the District Court rejected petitioner’s claim. The Court of Appeals dealt with the matter in an extensive opinion. After carefully examining the state court record, which it had before it, the court found ample grounds for holding that the appearance of a different attorney at the second trial had not resulted in prejudice to petitioner. The claim that Mr. Tamburo <page-number citation-index="1" label="54">*54</page-number>was unprepared centered around his allegedly inadequate efforts to have the guns and ammunition excluded from evidence. But the Court of Appeals found harmless any error in the admission of the bullets and ruled that the guns and other materials seized from the car were admissible evidence. Hence the claim of prejudice from the substitution of counsel was without substantial basis.<footnotemark>11</footnotemark> In this posture of the case we are not inclined to disturb the judgment of the Court of Appeals as to what the state record shows with respect to the adequacy of counsel. Unquestionably, the courts should make every effort to effect early appointments of counsel in all cases. But we are not disposed to fashion a <em>per se </em>rule requiring reversal of every conviction following tardy appointment of counsel or to hold that, whenever a habeas corpus petition alleges a belated appointment, an evidentiary hearing must be held to determine whether the defendant has been denied his constitutional right to counsel. The Court of Appeals reached the right result in denying a hearing in this case.</p>
<p id="b90-4">
<em>Affirmed.</em>
</p>
<judges id="b90-5">Mr. Justice Blackmun took no part in the consideration or decision of this case.</judges>
<footnote label="1">
<p id="b81-6"> Petitioner was indicted separately for each robbery. One of the other three men was similarly indicted and the other two were indicted only for the Gulf robbery. All indictments and all defendants were tried together. In a second trial following a mistrial, the jury found all defendants guilty as charged.</p>
</footnote>
<footnote label="2">
<p id="b81-7"> Kovacieh identified petitioner at a pretrial stage of the proceedings, and so testified, but could not identify him at the trial. Havieon identified petitioner both before trial and at trial.</p>
</footnote>
<footnote label="3">
<p id="b81-8"> The bullets were apparently excluded at the first trial. The grounds for the exclusion do not clearly appear from the record now before us.</p>
</footnote>
<footnote label="4">
<p id="b81-9"> The four-to-eight-year sentence was to be served concurrently with another sentence, for an unrelated armed robbery offense, imposed earlier but vacated subsequent to imposition of sentence in this case. The two-to-seven-year term was to be consecutive to the other sentences. It appears that the offenses here at issue caused revocation of petitioner’s parole in connection with a prior conviction. Apparently petitioner has now begun to serve the first of the two sentences imposed for the convictions here challenged.</p>
</footnote>
<footnote label="5">
<p id="b82-8"> Since <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), the federal courts have regularly entertained and ruled on petitions for habeas corpus filed by state prisoners alleging that unconstitutionally seized evidence was admitted at their trials. See, <em>e. g., Mancusi </em>v. <em>DeForte, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364</a></span> (1968); <em>Carafas </em>v. <em>LaVallee, </em><span class="citation" data-id="9423702"><a href="/opinion/107689/carafas-v-lavallee/" aria-description="Citation for case: Carafas v. LaVallee">391 U. S. 234</a></span> (1968); <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967). As for federal prisoners, a divided Court held that relief under <span class="citation no-link">28 U. S. C. § 2255</span> was available to vindicate Fourth Amendment rights. <em>Kaufman </em>v. <em>United States, </em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">394 U. S. 217</a></span> (1969). Right-to-counsel claims of course have regularly been pressed and entertained in federal habeas corpus proceedings.</p>
<p id="b82-9">It is relevant to note here that petitioner Chambers at trial made no objection to the introduction of the items seized from the car; however his Fourth Amendment claims with respect to the auto search were raised and passed on by the Pennsylvania courts in the state habeas corpus proceeding. His objection to the search of his house was raised at his trial and rejected both on the merits and because he had not filed a motion to suppress; similar treatment was given the point in the state collateral proceedings, which took <page-number citation-index="1" label="47">*47</page-number>place before the same judge who had tried the criminal case. The counsel claim was not presented at trial but was raised and rejected in the state collateral proceedings.</p>
</footnote>
<footnote label="6">
<p id="b83-9"> In any event, as we point out below, the validity of an arrest is not necessarily determinative of the right to search a car if there is probable cause to make the search. Here, as will be true in many cases, the circumstances justifying the arrest are also those furnishing probable cause for the search.</p>
</footnote>
<footnote label="7">
<p id="b85-10"> <em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">Cooper</a></span> </em>involved the warrantless search of a car held for forfeiture under state law. Evidence seized from the car in that search was held admissible. In the case before us no claim is made that state law authorized that the station wagon be held as <page-number citation-index="1" label="50">*50</page-number>evidence or as an instrumentality of the crime; nor was the station wagon an abandoned or stolen vehicle. The question here is whether probable cause justifies a warrantless search in. the circumstances presented.</p>
</footnote>
<footnote label="8">
<p id="b86-7"> Nothing said last term in <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), purported to modify or affect the rationale of <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>. </em>As the Court noted:</p>
<blockquote id="b86-8">“Our holding today is of course entirely consistent with the recognized principle that, assuming the existence of probable cause, automobiles and other vehicles may be searched without warrants 'where it is not practicable to secure a warrant because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought.’ <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 153</a></span>; see <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span>.” 395 U. S., at 764 n. 9.</blockquote>
</footnote>
<footnote label="9">
<p id="b87-7"> Following the car until a warrant can be obtained seems an impractical alternative since, among other things, the car may be taken out of the jurisdiction. Tracing the car and searching it hours or days later would of course permit instruments or fruits of crime to be removed from the car before the search.</p>
</footnote>
<footnote label="10">
<p id="b88-8"> It was not unreasonable in this case to take the car to the station house. All occupants in the car were arrested in a dark parking lot in the middle of the night. A careful search at that point was impractical and perhaps not safe for the officers, and it would serve the owner’s convenience and the safety of his car to have the vehicle and the keys together at the station house.</p>
</footnote>
<footnote label="11">
<p id="b90-8"> It is pertinent to note that each of the four defendants was represented by separate counsel. The attorney for Lawson, who was the car owner and who was the only defendant to take the stand, appears to have been the lead counsel. As far as the record before us reveals, no counsel made any objection at the trial to the admission of the items taken from the car. Petitioner’s counsel objected to the introduction of the bullets seized from petitioner’s house.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Chandler v. Miller.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Chandler v. Miller"
type: case
citation: "520 U.S. 305 (1997)"
parallel_cite: "117 S. Ct. 1295; 137 L. Ed. 2d 513"
neutral_cite: 1997 U.S. LEXIS 2505
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1997
date_decided: 1997-04-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1997-04-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Chandler v. Miller
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118100/chandler-v-miller/"
  cluster_id: 118100
  opinion_id: 9433438
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[City of Indianapolis v. Edmond]]", "[[Ferguson v. City of Charleston]]", "[[Board of Education v. Earls]]"]
aliases: []
tags: ["case", "fourth-amendment", "special-needs", "drug-testing", "suspicionless-search"]
holding: "Georgia's suspicionless drug-testing requirement for candidates for state office is unconstitutional — there was no concrete, special…"
lake:
  record_id: Chandler v. Miller
  status: verified
  projected_at: 2026-07-06
---

# Chandler v. Miller

*520 U.S. 305 (1997)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Georgia required candidates for designated state offices to certify they had passed a urinalysis drug test within 30 days of qualifying for the ballot. Two Libertarian Party candidates challenged the requirement as an unreasonable suspicionless search under the Fourth Amendment.

## Issue
Whether a State's suspicionless drug-testing requirement for candidates for elective office fits the special-needs exception to the Fourth Amendment's individualized-suspicion baseline.

## Rule
No, absent a genuine, concrete danger the testing is designed to meet. Where public safety is substantial and real, suspicionless searches calibrated to the risk may be reasonable; "[b]ut where, as in this case, public safety is not genuinely in jeopardy, the Fourth Amendment precludes the suspicionless search, no matter how conveniently arranged." — 520 U.S. 305, 323. ^pin-323

"However well meant, the candidate drug test Georgia has devised diminishes personal privacy for a symbol's sake. The Fourth Amendment shields society against that state action." — *Id.* at 322. ^pin-322

## Application
Georgia identified no concrete drug problem among its officeholders and the certification scheme was not designed to detect actual use (candidates chose their own test date and could abstain beforehand). Because the State showed no special need substantial enough to override the individualized-suspicion requirement, the suspicionless testing requirement was unconstitutional on these facts.

## Conclusion
Georgia's candidate drug-testing statute violated the Fourth Amendment; the judgment upholding it was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Chandler* marks the outer limit of the special-needs doctrine, distinguishing the safety-justified testing upheld in earlier cases and foreshadowing the law-enforcement-purpose limits of [[Ferguson v. City of Charleston]] and [[City of Indianapolis v. Edmond]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *Chandler v. Miller*, 520 U.S. 305 (1997) — https://www.courtlistener.com/opinion/118100/chandler-v-miller/ — pinpoints: 322, 323.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c9cb4e5bd3f1cac4", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Chandler v. Miller"}, "payload": {"all": [{"cite": "520 U.S. 305", "page": "305", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "520"}, {"cite": "117 S. Ct. 1295", "page": "1295", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "117"}, {"cite": "137 L. Ed. 2d 513", "page": "513", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "137"}, {"cite": "1997 U.S. LEXIS 2505", "page": "2505", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1997"}], "display": "520 U.S. 305", "official": {"cite": "520 U.S. 305", "page": "305", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "520"}, "official_selection_present": true, "record_id": "Chandler v. Miller"}}
{"assertion_id": "04779f0e9d565702", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-322", "record_id": "Chandler v. Miller"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-322", "pinpoint_status": "slip-only", "quote": "However well meant, the candidate drug test Georgia has devised diminishes personal privacy for a symbol's sake. The Fourth Amendment shields society against that state action.", "quote_fidelity": "mismatch", "record_id": "Chandler v. Miller", "star_marker": null}}
{"assertion_id": "f84c3069665f03a6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-323", "record_id": "Chandler v. Miller"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-323", "pinpoint_status": "slip-only", "quote": "--- # Chandler v. Miller *520 U.S. 305 (1997)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Georgia required candidates for designated state offices to certify they had passed a urinalysis drug test within 30 days of qualifying for the ballot. Two Libertarian Party candidates challenged the requirement as an unreasonable suspicionless search under the Fourth Amendment. ## Issue Whether a State's suspicionless drug-testing requirement for candidates for elective office fits the special-needs exception to the Fourth Amendment's individualized-suspicion baseline. ## Rule No, absent a genuine, concrete danger the testing is designed to meet. Where public safety is substantial and real, suspicionless searches calibrated to the risk may be reasonable;", "quote_fidelity": "mismatch", "record_id": "Chandler v. Miller", "star_marker": null}}
{"assertion_id": "ea9640ffbd0af8db", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Chandler v. Miller"}, "payload": {"as_of_content": "1997-04-15", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Chandler v. Miller", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Chandler v. Miller

```json
{
  "schema_version": "s2.v1",
  "record_id": "Chandler v. Miller",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Chandler v. Miller",
    "case_name_short": "",
    "case_name_full": "CHANDLER Et Al. v. MILLER, GOVERNOR OF GEORGIA, Et Al.",
    "input_case_name": "Chandler v. Miller",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1997-04-15",
    "year": 1997,
    "docket": null,
    "cluster_id": 118100,
    "lead_opinion_id": 9433438,
    "sibling_ids": [
      118100,
      9433438,
      9433439
    ],
    "absolute_url": "/opinion/118100/chandler-v-miller/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "520 U.S. 305",
      "volume": "520",
      "reporter": "U.S.",
      "page": "305",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "117 S. Ct. 1295",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "1295",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 L. Ed. 2d 513",
        "volume": "137",
        "reporter": "L. Ed. 2d",
        "page": "513",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1997 U.S. LEXIS 2505",
        "volume": "1997",
        "reporter": "U.S. LEXIS",
        "page": "2505",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "520 U.S. 305",
        "volume": "520",
        "reporter": "U.S.",
        "page": "305",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "117 S. Ct. 1295",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "1295",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 L. Ed. 2d 513",
        "volume": "137",
        "reporter": "L. Ed. 2d",
        "page": "513",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1997 U.S. LEXIS 2505",
        "volume": "1997",
        "reporter": "U.S. LEXIS",
        "page": "2505",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "520 U.S. 305",
    "official_selection": {
      "court_class": "scotus",
      "selected": "520 U.S. 305",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-323",
      "page": null,
      "quote": "--- # Chandler v. Miller *520 U.S. 305 (1997)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Georgia required candidates for designated state offices to certify they had passed a urinalysis drug test within 30 days of qualifying for the ballot. Two Libertarian Party candidates challenged the requirement as an unreasonable suspicionless search under the Fourth Amendment. ## Issue Whether a State's suspicionless drug-testing requirement for candidates for elective office fits the special-needs exception to the Fourth Amendment's individualized-suspicion baseline. ## Rule No, absent a genuine, concrete danger the testing is designed to meet. Where public safety is substantial and real, suspicionless searches calibrated to the risk may be reasonable;",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-322",
      "page": null,
      "quote": "However well meant, the candidate drug test Georgia has devised diminishes personal privacy for a symbol's sake. The Fourth Amendment shields society against that state action.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1997-04-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Chandler v. Miller",
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
        "journal_ref": "Chandler v. Miller:lane1_negative"
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
        "journal_ref": "Chandler v. Miller:lane1_negative"
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
        "journal_ref": "Chandler v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ferguson v. City of Charleston",
          "cluster_id": 2967360,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Schenekl v. State",
          "cluster_id": 1472762,
          "cite": [
            "996 S.W.2d 305",
            "1999 WL 374216"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane1_negative"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Yeargan",
          "cluster_id": 1060948,
          "cite": [
            "958 S.W.2d 626",
            "1997 Tenn. LEXIS 574",
            "1997 WL 724993"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of Education of Independent School District No. 92 of Pottawatomie County v. Earls",
          "cluster_id": 121171,
          "cite": [
            "153 L. Ed. 2d 735",
            "122 S. Ct. 2559",
            "536 U.S. 822",
            "2002 U.S. LEXIS 4882",
            "2002 Cal. Daily Op. Serv. 5761",
            "2002 Daily Journal DAR 7275",
            "70 U.S.L.W. 4737",
            "15 Fla. L. Weekly Fed. S 483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wolfson v. Brammer",
          "cluster_id": 153018,
          "cite": [
            "616 F.3d 1045",
            "2010 U.S. App. LEXIS 16766",
            "2010 WL 3191159"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Comite De Jornaleros De Redondo Beach v. City of Redondo Beach",
          "cluster_id": 613771,
          "cite": [
            "657 F.3d 936",
            "2011 WL 4336667"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pierce v. Smith",
          "cluster_id": 12443,
          "cite": [
            "117 F.3d 866",
            "13 I.E.R. Cas. (BNA) 8",
            "1997 U.S. App. LEXIS 17907",
            "1997 WL 395259"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "American Civil Liberties Union v. United States Conference of Catholic Bishops",
          "cluster_id": 815386,
          "cite": [
            "705 F.3d 44",
            "2013 WL 150321",
            "2013 U.S. App. LEXIS 976"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marcavage v. City of New York",
          "cluster_id": 805786,
          "cite": [
            "689 F.3d 98",
            "2012 WL 3125225",
            "2012 U.S. App. LEXIS 16081"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
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
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Los Angeles v. Patel",
          "cluster_id": 2810524,
          "cite": [
            "576 U.S. 409"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brandon Michael Lifshitz",
          "cluster_id": 786321,
          "cite": [
            "369 F.3d 173",
            "2004 WL 1043468"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raymond Lee Scott",
          "cluster_id": 794629,
          "cite": [
            "450 F.3d 863",
            "2006 U.S. App. LEXIS 14182"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Wiedeman",
          "cluster_id": 1033708,
          "cite": [
            "286 Neb. 193",
            "835 N.W.2d 698"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chandler v. Miller:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118100 OR 9433438 OR 9433439) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05MjI4Mzg0MDAwMDAmcz0zMDIyMjc2JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118100+OR+9433438+OR+9433439%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118100 OR 9433438 OR 9433439)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02OSZzPTEyNzM0NTgmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118100+OR+9433438+OR+9433439%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118100 OR 9433438 OR 9433439)",
        "reviewed": 11,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 11,
        "triage_read": 0,
        "triage_snippet_classified": 11
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118100 OR 9433438 OR 9433439)",
    "indexed_citing_opinions": 321,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118100,
        "count": 290,
        "count_source": "search"
      },
      {
        "opinion_id": 9433438,
        "count": 38,
        "count_source": "search"
      },
      {
        "opinion_id": 9433439,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 525,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/chandler-v-miller.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY4NDg3OTkmcz00NzY3NjMyJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118100+OR+9433438+OR+9433439%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118100,
        "cited_id": 101887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 107301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 108902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 109831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 111927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 111965,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 111990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 112220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 112632,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 355692,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 422035,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 486563,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118100,
        "cited_id": 711061,
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
    "date_created": "2026-07-04T23:50:05Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:53:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Chandler v. Miller

```
<opinion type="majority">
<author id="b400-5">Justice Ginsburg</author>
<p id="A5R">delivered the opinion of the Court.</p>
<p id="b400-6">The Fourth Amendment requires government to respect “[t]he right of the people to be secure in their persons . . . against unreasonable searches and seizures.” This restraint on government conduct generally bars officials from undertaking a search or seizure absent individualized suspicion. Searches conducted without grounds for suspicion of particular individuals have been upheld, however, in “certain limited circumstances.” See <em>Treasury Employees </em>v. <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#668" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656, 668</a></span> (1989). These circumstances include brief stops for questioning or observation at a fixed Border Patrol checkpoint, <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#545" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 545-550, 566-567</a></span> (1976), or at a sobriety checkpoint, <em>Michigan Dept. of State Police </em>v. <em>Sitz, </em><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#447" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S. 444, 447, 455</a></span> (1990), and administrative inspections in “closely regulated” businesses, <em>New York </em>v. <em>Burger, </em><span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#703" aria-description="Citation for case: New York v. Burger">482 U. S. 691, 703-704</a></span> (1987).</p>
<p id="b400-7">Georgia requires candidates for designated state offices to certify that they have taken a drug test and that the test result was negative. <span class="citation no-link">Ga. Code Ann. §21-2-140</span> (1993) (hereinafter §21-2-140). We confront in this case the question whether that requirement ranks among the limited circumstances in which suspicionless searches are warranted. Relying on this Court's precedents sustaining drug-testing <page-number citation-index="1" label="309">*309</page-number>programs for student athletes, customs employees, and railway employees, see <em>Vernonia School Dist. 47J </em>v. <em>Acton, </em><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#650" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646, 650, 665-666</a></span> (1995) (random drug testing of students who participate in interscholastic sports); <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#659" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 659</a></span> (drug tests for United States Customs Service employees who seek transfer or promotion to certain positions); <em>Skinner </em>v. <em>Railway Labor Executives’ Assn., </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#608" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602, 608-613</a></span> (1989) (drug and alcohol tests for railway employees involved in train accidents and for those who violate particular safety rules), the United States Court of Appeals for the Eleventh Circuit judged Georgia’s law constitutional. We reverse that judgment. Georgia’s requirement that candidates for state office pass a drug test, we hold, does not fit within the closely guarded category of constitutionally permissible suspicionless searches.</p>
<p id="AOqb">I</p>
<p id="b401-3">The prescription at issue, approved by the Georgia Legislature in 1990, orders that “[ejach candidate seeking to qualify for nomination or election to a state office shall as a condition of such qualification be required to certify that such candidate has tested negative for illegal drugs.” §21 — 2— 140(b). Georgia was the first, and apparently remains the only, State to condition candidacy for state office on a drug test.</p>
<p id="b401-4">Under the Georgia statute, to qualify for a place on the ballot, a candidate must present a certificate from a state-approved laboratory, in a form approved by the Secretary of State, reporting that the candidate submitted to a urinalysis drug test within 30 days prior to qualifying for nomination or election and that the results were negative. § 21 — 2— 140(c). The statute lists as “[ijllegal drug[s]”: marijuana, cocaine, opiates, amphetamines, and phencyclidines. § 21-2-140(a)(3). The designated state offices are: “the Governor, Lieutenant Governor, Secretary of State, Attorney General, State School Superintendent, Commissioner of Insurance, <page-number citation-index="1" label="310">*310</page-number>Commissioner of Agriculture, Commissioner of Labor, Justices of the Supreme Court, Judges of the Court of Appeals, judges of the superior courts, district attorneys, members of the General Assembly, and members of the Public Service Commission.” § 21-2-140(a)(4).</p>
<p id="b402-5">Candidate drug tests are to be administered in a manner consistent with the United States Department of Health and Human Services Guidelines, <span class="citation no-link">53 Fed. Reg. 11979</span>-11989 (1988), or other professionally valid procedures approved by Georgia’s Commissioner of Human Resources. See § 21-2-140(a)(2). A candidate may provide the test specimen at a laboratory approved by the State, or at the office of the candidate’s personal physician, see App. 4-5 (Joint Statement of Undisputed Facts). Once a urine sample is obtained, an approved laboratory determines whether any of the five specified illegal drugs are present, <em>id., </em>at 5; §21-2-140(c), and prepares a certificate reporting the test results to the candidate.</p>
<p id="b402-6">Petitioners were Libertarian Party nominees in 1994 for state offices subject to the requirements of §21-2-140. The Party nominated Walker L. Chandler for the office of Lieutenant Governor, Sharon T. Harris for the office of Commissioner of Agriculture, and James D. Walker for the office of member of the General Assembly. In May 1994, about one month before the deadline for submission of the certificates required by §21-2-140, petitioners Chandler, Harris, and Walker filed this action in the United States District Court for the Northern District of Georgia. They asserted, <em>inter alia, </em>that the drug tests required by §21-2-140 violated their rights under the First, Fourth, and Fourteenth Amendments to the United States Constitution. Naming as defendants Governor Zell D. Miller and two other state officials involved in the administration of §21-2-140, petitioners requested declaratory and injunctive relief barring enforcement of the statute.</p>
<p id="b403-4"><page-number citation-index="1" label="311">*311</page-number>In June 1994, the District Court denied petitioners’ motion for a preliminary injunction. Stressing the importance of the state offices sought and the relative unintrusiveness of the testing procedure, the court found it unlikely that petitioners would prevail on the merits of their claims. App. to Pet. for Cert. 5B. Petitioners apparently submitted to the drug tests, obtained the certificates required by § 21-2-140, and appeared on the ballot. See Tr. of Oral Arg. 5. After the 1994 election, the parties jointly moved for the entry of final judgment on stipulated facts. In January 1995, the District Court entered final judgment for respondents.</p>
<p id="b403-5">A divided Eleventh Circuit panel affirmed. <span class="citation multiple-matches"><a href="/c/F.%203d/73/1543/">73 F. 3d 1543</a></span> (1996). It is settled law, the court accepted, that the drug tests required by the statute rank as searches. But, as was true of the drug-testing programs at issue in <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span> </em>and <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span>, </em>the court reasoned, §21-2-140 serves “special needs,” interests other than the ordinary needs of law enforcement. The court therefore endeavored to “ ‘balance the individual’s privacy expectations against the Government’s interests to determine whether it [was] impractical to require a warrant or some level of individualized suspicion in the particular context.’” 73 F. 3d, at 1545 (quoting <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#665" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 665-666</a></span>).</p>
<p id="b403-6">Examining the state interests involved, the court acknowledged the absence of any record of drug abuse by elected officials in Georgia. Nonetheless, the court observed, “[t]he people of Georgia place in the trust of their elected officials ... their liberty, their safety, their economic well-being, [and] ultimate responsibility for law enforcement.” 73 F. 3d, at 1546. Consequently, “those vested with the highest executive authority to make public policy in general and frequently to supervise Georgia’s drug interdiction efforts in particular must be persons appreciative of the perils of drug use.” <em>Ibid. </em>The court further noted that “[t]he nature of high public office in itself demands the highest levels of honesty, clear-sightedness, and clear-thinking.” <em>Ibid. </em>Re<page-number citation-index="1" label="312">*312</page-number>citing responsibilities of the offices petitioners sought, the Court of Appeals perceived those “positions [as] particularly susceptible to the ‘risks of bribery and blackmail against which the Government is entitled to guard.’ ” <em>Ibid, </em>(quoting <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#674" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 674</a></span>).</p>
<p id="b404-5">Turning to petitioners’ privacy interests, the Eleventh Circuit emphasized that the tests could be conducted in the office of the candidate’s private physician, making the “intrusion here . . . even less than that approved in <em>Von Raab." </em>73 F. 3d, at 1547. The court also noted the statute’s reference to federally approved drug-testing guidelines. <em>Ibid. </em>The drug test itself would reveal only the presence or absence of indicia <em>of </em>the use of particular drugs, and not any other information about the health of the candidate. Furthermore, the candidate would control release of the test results: Should the candidate test positive, he or she could forfeit the opportunity to run for office, and in that event, nothing would be divulged to law enforcement officials. <em>Ibid. </em>Another consideration, the court said, is the reality that “candidates for high office must expect the voters to demand some disclosures about their physical, emotional, and mental fitness for the position.” <em>Ibid. </em>Concluding that the State’s interests outweighed the privacy intrusion caused by the required certification, the court held the statute, as applied to petitioners, not inconsistent' with the Fourth and Fourteenth Amendments. <em>Ibid.</em><footnotemark><em>1</em></footnotemark></p>
<p id="b404-6">Judge Barkett dissented. In her view, a balance of the State’s and candidates’ interests was not appropriate, for the State had failed to establish a special governmental need for the regime. “There is nothing so special or immediate about the generalized governmental interests involved here,” she observed, “as to warrant suspension of the Fourth <page-number citation-index="1" label="313">*313</page-number>Amendment’s requirement of individualized suspicion for searches and seizures.” <em>Id., </em>at 1551.</p>
<p id="b405-5">We granted the petition for certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./518/1057/">518 U. S. 1057</a></span> (1996), and now reverse.<footnotemark>2</footnotemark></p>
<p id="b405-6">II</p>
<p id="b405-7">We begin our discussion of this case with an uncontested point: Georgia’s drug-testing requirement, imposed by law and enforced by state officials, effects a search within the meaning of the Fourth and Fourteenth Amendments. See <em>Skinner, </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#617" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 617</a></span>; Tr. of Oral Arg. 36; Brief for United States as <em>Amicus Curiae </em>Í0 (collection and testing of urine to meet Georgia’s certification statute “constitutes a search subject to the demands of the Fourth Amendment” (internal quotation marks omitted)). As explained in <em>Sjkin-ner, </em>government-ordered “collection and testing of urine intrudes upon expectations of privacy that society has long recognized as reasonable.” 489 U. S., at 617. Because “these intrusions [are] searches under the Fourth Amendment,” <em>ibid., </em>we focus on the question: Are the searches reasonable?</p>
<p id="b405-8">To be reasonable under the Fourth Amendment, a search ordinarily must be based on individualized suspicion of wrongdoing. See <em>Vernonia, </em><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#652" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 652-653</a></span>. But particularized exceptions to the main rule are sometimes warranted based on “special needs, beyond the normal need for law enforcement.” <em>Skinner, </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#619" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 619</a></span> (internal <page-number citation-index="1" label="314">*314</page-number>quotation marks omitted). When such “special needs”— concerns other than crime detection — are alleged in justification of a Fourth Amendment intrusion, courts must undertake a context-specific inquiry, examining closely the competing private and public interests advanced by the parties. See <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#665" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 665-666</a></span>; see also <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#668" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><em>id., </em>at 668</a></span>. As <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span> </em>stated: “In limited circumstances, where the privacy interests implicated by the search are minimal, and where an important governmental interest furthered by the intrusion would be placed in jeopardy by a requirement of individualized suspicion, a search may be reasonable despite the absence of such suspicion.” 489 U. S., at 624.</p>
<p id="b406-5">In evaluating Georgia’s ballot-access, drug-testing statute — a measure plainly not tied to individualized suspicion— the Eleventh Circuit sought to “ ‘balance the individual’s privacy expectations against the [State’s] interests,’ ” 73 F. 3d, at 1545 (quoting <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#665" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 665</a></span>), in line with our precedents most immediately in point: <em>Skinner, Von Raab, </em>and <em>Vernonia. </em>We review those decisions before inspecting Georgia’s law.</p>
<p id="b406-6">A</p>
<p id="b406-7"><em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span> </em>concerned Federal Railroad Administration (FRA) regulations that required blood and urine tests of rail employees involved in train accidents; the regulations also authorized railroads to administer breath and urine tests to employees who violated certain safety rules. 489 U. S., at 608-612. The FRA adopted the drug-testing program in response to evidence of drug and alcohol abuse by some railroad employees, the obvious safety hazards posed by such abuse, and the documented link between drug- and alcohol-impaired employees and the incidence of train accidents. <em>Id., </em>at 607-608. Recognizing that the urinalysis tests, most conspicuously, raised evident privacy concerns, the Court noted two offsetting considerations: First, the regulations reduced the intrusiveness of the collection process, <em>id., </em>at 626; <page-number citation-index="1" label="315">*315</page-number>and, more important, railway employees, “by reason of their participation in an industry that is regulated pervasively to ensure safety,” had diminished expectations of privacy, <em>id., </em>at 627.</p>
<p id="b407-5">“[Surpassing safety interests,” the Court concluded, warranted the FRA testing program. <em>Id., </em>at 634. The drug tests could deter illegal drug use by railroad employees, workers positioned to “cause great human loss before any signs of impairment become noticeable to supervisors.” <em>Id., </em>at 628. The program also helped railroads to obtain invaluable information about the causes of major train accidents. See <em>id., </em>at 630. Testing without a showing of individualized suspicion was essential, the Court explained, if these vital interests were to be served. See <em>id., </em>at 628. Employees could not forecast the timing of an accident or a safety violation, events that would trigger testing. The employee’s inability to avoid detection simply by staying drug free at a prescribed test time significantly enhanced the deterrent effect of the program. See <em>ibid. </em>Furthermore, imposing an individualized suspicion requirement for a drug test in the chaotic aftermath of a train accident would seriously impede an employer’s ability to discern the cause of the accident; indeed, waiting until suspect individuals could be identified “likely would result in the loss or deterioration of the evidence furnished by the tests.” <em>Id., </em>at 631.</p>
<p id="b407-6">In <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span>, </em>the Court sustained a United States Customs Service program that made drug tests a condition of promotion or transfer to positions directly involving drug interdiction or requiring the employee to carry a firearm. 489 U. S., at 660-661, 667-677.<footnotemark>3</footnotemark> While the Service’s regime was <page-number citation-index="1" label="316">*316</page-number>not prompted by a demonstrated drug abuse problem, <em>id., </em>at 660, it was developed for an agency with an “almost unique mission,” <em>id., </em>at 674, as the “first line of defense” against the smuggling of illicit drugs into the United States, <em>id., </em>at 668. Work directly involving drug interdiction and posts that require the employee to carry a firearm pose grave safety threats to employees who hold those positions, and also expose them to large amounts of illegal narcotics and to persons engaged in crime; illicit drug users in such high-risk positions might be unsympathetic to the Service’s mission, tempted by bribes, or even threatened with blackmail. See <em>id., </em>at 668-671. The Court held that the Government had a “compelling” interest in assuring that employees placed in these positions would not include drug users. See <em>id., </em>at 670-671. Individualized suspicion would not work in this setting, the Court determined, because it was “not feasible to subject [these] employees and their work product to the kind of day-to-day scrutiny that is the norm in more traditional office environments.” <em>Id., </em>at 674.</p>
<p id="b408-5">Finally, in <em>Vernonia, </em>the Court sustained a random drug-testing program for-high school students engaged in interscholastic athletic competitions. The program’s context was critical, for a local government bears large “responsibilities, under a public school system, as guardian and tutor of children entrusted to its care.” <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#665" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 665</a></span>. An “immediate crisis,” <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#663" aria-description="Citation for case: Vernonia School District 47J v. Acton"><em>id., </em>at 663</a></span>, caused by “a sharp increase in drug use” in the school district, <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#648" aria-description="Citation for case: Vernonia School District 47J v. Acton"><em>id., </em>at 648</a></span>, sparked installation of the program. District Court findings established that student athletes were not only “among the drug users,” they were “leaders of the drug culture.” <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#649" aria-description="Citation for case: Vernonia School District 47J v. Acton"><em>Id., </em>at 649</a></span>. Our decision noted that “‘students within the school environment have a lesser expectation of privacy than members of the population generally.’ ” <em><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">Id.,</a></span> </em>at 657 (quoting <em>New Jersey </em>v. <page-number citation-index="1" label="317">*317</page-number><em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#348" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 348</a></span> (1985) (Powell, J., concurring)). We emphasized the importance of deterring drug use by schoolchildren and the risk of injury a drug-using student athlete east on himself and those engaged with him on the playing field. See <em>Vernonia, </em><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#662" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 662</a></span>.</p>
<p id="b409-5">B</p>
<p id="b409-6">Respondents urge that the precedents just examined are not the sole guides for assessing the constitutional validity of the Georgia statute. The “special needs” analysis, they contend, must be viewed through a different lens because § 21-2-140 implicates Georgia’s sovereign power, reserved to it under the Tenth Amendment, to establish qualifications for those who seek state office. Respondents rely on <em>Gregory </em>v. <em>Ashcroft, </em><span class="citation" data-id="9842118"><a href="/opinion/112632/gregory-v-ashcroft/" aria-description="Citation for case: Gregory v. Ashcroft">501 U. S. 452</a></span> (1991), which upheld against federal statutory and Equal Protection Clause challenges Missouri’s mandatory retirement age of 70 for state judges. The Court found this age classification reasonable and not barred by the federal legislation. See <span class="citation" data-id="9842118"><a href="/opinion/112632/gregory-v-ashcroft/#473" aria-description="Citation for case: Gregory v. Ashcroft"><em>id., </em>at 473</a></span>. States, <em><span class="citation" data-id="9842118"><a href="/opinion/112632/gregory-v-ashcroft/" aria-description="Citation for case: Gregory v. Ashcroft">Gregory</a></span> </em>reaffirmed, enjoy wide latitude to establish conditions of candidacy for state office, but in setting such conditions, they may not disregard basic constitutional protections. See <span class="citation" data-id="9842118"><a href="/opinion/112632/gregory-v-ashcroft/#463" aria-description="Citation for case: Gregory v. Ashcroft"><em>id., </em>at 463</a></span>; <em>McDaniel </em>v. <em>Paty, </em><span class="citation" data-id="9427133"><a href="/opinion/109831/mcdaniel-v-paty/" aria-description="Citation for case: McDaniel v. Paty">435 U. S. 618</a></span> (1978) (invalidating state provision prohibiting members of clergy from serving as delegates to state constitutional convention); <em>Communist Party of Ind. </em>v. <em>Whitcomb, </em><span class="citation" data-id="9425495"><a href="/opinion/108902/communist-party-of-indiana-v-whitcomb/" aria-description="Citation for case: Communist Party of Indiana v. Whitcomb">414 U. S. 441</a></span> (1974) (voiding loyalty oath as a condition of ballot access); <em>Bond </em>v. <em>Floyd, </em><span class="citation" data-id="107301"><a href="/opinion/107301/bond-v-floyd/" aria-description="Citation for case: Bond v. Floyd">385 U. S. 116</a></span> (1966) (Georgia Legislature could not exclude elected representative on ground that his antiwar statements cast doubt on his ability to take an oath). We are aware of no precedent suggesting that a State’s power to establish qualifications for state offices — any more than its sovereign power to prosecute crime — diminishes the constraints on state action imposed by the Fourth Amendment. We therefore reject respondents’ invitation to apply in this case a framework extraordinarily deferential to state meas<page-number citation-index="1" label="318">*318</page-number>ures setting conditions of candidacy for state office. Our guides remain <em>Skinner, Von Raab, </em>and <em>Vernonia.</em></p>
<p id="b410-5">Turning to those guides, we note, first, that the testing method the Georgia statute describes is relatively noninvasive; therefore, if the “special needs” showing had been made, the State could not be faulted for excessive intrusion. Georgia’s statute invokes the drug-testing guidelines applicable to the federal programs upheld in <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span> </em>and <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span>. </em>See Brief for United States as <em>Amicus Curiae </em>20-21; <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#661" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 661-662, n. 1</a></span>. The State permits a candidate to provide the urine specimen in the office of his or her private physician; and the results of the test are given first to the candidate, who controls further dissemination of the report. Because the State has effectively limited the invasiveness of the testing procedure, we concentrate on the core issue: Is the certification requirement warranted by a special need?</p>
<p id="b410-6">Our precedents establish that the proffered special need for drug testing must be substantial — important enough to override the individual’s acknowledged privacy interest, sufficiently vital to suppress the Fourth Amendment’s normal requirement of individualized suspicion. See <em>supra, </em>at 313-317 and this page. Georgia has failed to show, in justification of § 21-2-140, a special need of that kind.</p>
<p id="b410-7">Respondents’ defense of the statute rests primarily on the incompatibility of unlawful drug use with holding high state office. The statute is justified, respondents contend, because the use of illegal drugs draws into question an official’s judgment and integrity; jeopardizes the discharge of public functions, including antidrug law enforcement efforts; and undermines public confidence and trust in elected officials. Brief for Respondents 11-18. The statute, according to respondents, serves to deter unlawful drug users from becoming candidates and thus stops them from attaining high state office. <em>Id., </em>at 17-18. Notably lacking in respondents’ pres<page-number citation-index="1" label="319">*319</page-number>entation is any indication of a concrete danger demanding departure from the Fourth Amendment’s main rule.</p>
<p id="b411-5">Nothing in the record hints that the hazards respondents broadly describe are real and not simply hypothetical for Georgia’s polity. The statute was not enacted, as counsel for respondents readily acknowledged at oral argument, in response to any fear or suspicion of drug use by state officials:</p>
<blockquote id="b411-6">“QUESTION: Is there any indication anywhere in this record that Georgia has a particular problem here with State officeholders being drug abusers?</blockquote>
<blockquote id="b411-7">“[COUNSEL FOR RESPONDENTS]: No, there is no such evidence, [and] to be frank, there is no such problem as we sit here today.” Tr. of Oral Arg. 32.</blockquote>
<p id="b411-8">See also <em>id., </em>at 31 (counsel for respondents affirms absence of evidence that state officeholders in Georgia have drug problems). A demonstrated problem of drug abuse, while not in all cases necessary to the validity of a testing regime, see <em>Von </em>Raab, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#673" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 673-675</a></span>, would shore up an assertion of special need for a suspicionless general search program. Proof of unlawful drug use may help to clarify — and to substantiate — the precise hazards posed by such use. Thus, the evidence of drug and alcohol use by railway employees engaged in safety-sensitive tasks in <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span>, </em>see 489 U. S., at 606-608, and the immediate crisis prompted by a sharp rise in students’ use of unlawful drugs in <em>Vernonia, </em>see <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#662" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 662-663</a></span>, bolstered the Government’s and school officials’ arguments that drug-testing programs were warranted and appropriate.</p>
<p id="b411-9">In contrast to the effective testing regimes upheld in <em>Skinner, Von Raab, </em>and <em>Vernonia, </em>Georgia’s certification requirement is not well designed to identify candidates who violate antidrug laws. Nor is the scheme a credible means to deter illicit drug users from seeking election to state office. The test date — to be scheduled by the candidate anytime within <page-number citation-index="1" label="320">*320</page-number>30 days prior to qualifying for a place on the ballot — is no secret. As counsel for respondents acknowledged at oral argument, users of illegal drugs, save for those prohibitively addicted, could abstain for a pretest period sufficient to avoid detection. See Tr. of Oral Arg. 44-46.<footnotemark>4</footnotemark> Even if we indulged respondents’ argument that one purpose of §21-2-140 might be to detect those unable so to abstain, see <em>id., </em>at 46, respondents have not shown or argued that such persons are likely to be candidates for public office in Georgia. Moreover, respondents have offered no reason why ordinary law enforcement methods would not suffice to apprehend such addicted individuals, should they appear in the limelight of a public stage. Section 21-2-140, in short, is not needed and cannot work to ferret out lawbreakers, and respondents barely attempt to support the statute on that ground.</p>
<p id="b412-5">Respondents and the United States as <em>amicus curiae </em>rely most heavily on our decision in <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span>, </em>which sustained a drug-testing program for Customs Service officers prior to promotion or transfer to certain high-risk positions, despite the absence of any documented drug abuse problem among Service employees. 489 U. S., at 660; see Brief for Respondents 12-14; Brief for United States as <em>Amicus Curiae </em>18; see also 73 F. 3d, at 1646. The posts in question in <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span> </em>directly involved drug interdiction or otherwise required the Service member to carry a firearm. See 489 U. S., at 670 (“Government has a compelling interest in ensuring that front-line interdiction personnel are physically fit, and have unimpeachable integrity and judgment.”); <em>id., </em>at 670-671 (“[T]he public should not bear the risk that employees who may suffer from impaired perception and judgment will be promoted to positions where they may need to employ deadly force.”).</p>
<p id="b413-4"><page-number citation-index="1" label="321">*321</page-number>Hardly a decision opening broad vistas for suspicionless searches, <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span> </em>must be read in its unique context. As the Customs Service reported in announcing the testing program: “Customs employees, more than any other Federal workers, are routinely exposed to the vast network of organized crime that is inextricably tied to illegal drug use.” <em>National Treasury Employees Union </em>v. <em>Von Raab, </em><span class="citation" data-id="486563"><a href="/opinion/486563/national-treasury-employees-union-and-argent-acosta-president-chapter/#173" aria-description="Citation for case: National Treasury Employees Union and Argent Acosta,...">816 F. 2d 170, 173</a></span> (CA5 1987) (internal quotation marks omitted), aff’d in part, vacated in part, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656</a></span> (1989). We stressed that “[d]rug interdiction ha[d] become the agency’s primary enforcement mission,” <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#660" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><em>id., </em>at 660</a></span>, and that the employees in question would have “access to vast sources of valuable contraband,” <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#669" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><em>id., </em>at 669</a></span>. Furthermore, Customs officers “ha[dj been the targets of bribery by drug smugglers on numerous occasions,” and several had succumbed to the temptation. <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Ibid.</a></span></em></p>
<p id="b413-5">Respondents overlook a telling difference between <em>Von Raab </em>and Georgia’s candidate drug-testing program. In <em>Von Raab </em>it was “not feasible to subject employees [required to carry firearms or concerned with interdiction of controlled substances] and their work product to the kind of day-to-day scrutiny that is the norm in more traditional office environments.” <em>Id., </em>at 674. Candidates for public office, in contrast, are subject to relentless scrutiny — by their peers, the public, and the press. Their day-to-day conduct attracts attention notably beyond the norm in ordinary work environments.</p>
<p id="b413-6">What is left, after close review of Georgia’s scheme, is the image the State seeks to project. By requiring candidates for public office to submit to drug testing, Georgia displays its commitment to the struggle against drug abuse. The suspicionless tests, according to respondents, signify that candidates, if elected, will be fit to serve their constituents free from the influence of illegal drugs. But Georgia asserts no evidence of a drug problem among the State’s elected officials, those officials typically do not perform high-risk, <page-number citation-index="1" label="322">*322</page-number>safety-sensitive tasks, and the required certification immediately aids no interdiction effort. The need revealed, in short, is symbolic, not “special,” as that term draws meaning from our case law.</p>
<p id="b414-5">In <em>Von Raab, </em>the Customs Service had defended its officer drug-testing program in part as a way to demonstrate the agency’s commitment to enforcement of the law. See Brief for United States in <em>Treasury Employees </em>v. <em>Von Raab, </em>O. T. 1988, No. 86-1879, pp. 35-36. The <em>Von Raab </em>Court, however, did not rely on that justification. Indeed, if a need of the “set a good example” genre were sufficient to overwhelm a Fourth Amendment objection, then the care this Court took to explain why the needs in <em>Skinner, Von Raab, </em>and <em>Vernonia </em>ranked as “special” wasted many words in entirely unnecessary, perhaps even misleading, elaborations.</p>
<p id="b414-6">In a pathmarking dissenting opinion, Justice Brandéis recognized the importance of teaching by example: “Our Government is the potent, the omnipresent teacher. For good or for ill, it teaches the whole people by its example.” <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#485" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 485</a></span> (1928). Justice Brandéis explained in <em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">Olmstead</a></span> </em>why the Government set a bad example when it introduced in a criminal proceeding evidence obtained through an unlawful Government wiretap:</p>
<blockquote id="b414-7">“[I]t is . . . immaterial that the intrusion was in aid of law enforcement. Experience should teach us to be most on our guard to protect liberty when the Government’s purposes are beneficent. Men born to freedom are naturally alert to repel invasion of their liberty by evil-minded rulers. The greatest dangers to liberty lurk in insidious encroachment by men of zeal, well-meaning but without understanding.” <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#479" aria-description="Citation for case: Olmstead v. United States"><em>Id., </em>at 479</a></span>.</blockquote>
<p id="b414-8">However well meant, the candidate drug test Georgia has devised diminishes personal privacy <em>for </em>a symbol’s sake. The Fourth Amendment shields society against that state action.</p>
<p id="Am"><page-number citation-index="1" label="323">*323</page-number>III</p>
<p id="b415-3">We note, finally, matters this opinion does not treat. Georgia’s singular drug test for candidates is not part of a medical examination designed to provide certification of a candidate’s general health, and we express no opinion on such examinations. Nor do we touch on financial disclosure requirements, which implicate different concerns and procedures. See, <em>e. g., Barry </em>v. <em>City of New York, </em><span class="citation" data-id="8917405"><a href="/opinion/8927506/barry-v-city-of-new-york/" aria-description="Citation for case: Barry v. City of New York">712 F. 2d 1554</a></span> (CA2 1983) (upholding city’s financial disclosure law for elected and appointed officials, candidates for city office, and certain city employees); <em>Plante </em>v. <em>Gonzalez, </em><span class="citation" data-id="355692"><a href="/opinion/355692/kenneth-a-plante-v-larry-gonzalez-etc-jon-c-thomas-v-larry-gonzalez/" aria-description="Citation for case: Kenneth A. Plante v. Larry Gonzalez, Etc., Jon C. Thomas...">575 F. 2d 1119</a></span> (CA5 1978) (upholding Florida’s financial disclosure requirements for certain public officers, candidates, and employees). And we do not speak to drug testing in the private sector, a domain unguarded by Fourth Amendment constraints. See <em>United States </em>v. <em>Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 113</a></span> (1984).</p>
<p id="b415-4">We reiterate, too, that where the risk to public safety is substantial and real, blanket suspicionless searches calibrated to the risk may rank as “reasonable” — for example, searches now routine at airports and at entrances to courts and other official buildings. See <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#674" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 674-676</a></span>, and n. 3. But where, as in this case, public safety is not genuinely in jeopardy, the Fourth Amendment precludes the suspicionless search, no matter how conveniently arranged.</p>
<p id="b415-5">* * *</p>
<p id="b415-6">For the reasons stated, the judgment of the Court of Appeals for the Eleventh Circuit is</p>
<p id="b415-7">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b404-7"> The court also rejected equal protection and free speech pleas made by petitioners. 73 F. 3d, at 1547-1549. We hold § 21-2-140 incompatible with the Fourth and Fourteenth Amendments, and do not reach petitioners’ further pleas.</p>
</footnote>
<footnote label="2">
<p id="b405-9"> The United States, as <em>amicus curiae </em>in support of respondents, suggests that this case may have become moot because there is no continuing controversy regarding the now-completed 1994 election, and petitioners, who did not sue on behalf of a class, failed to assert in the courts below that they intended to run for a covered state office in a future election. See Brief for United States as <em>Amicus Curiae </em>9-10, n. 4. We reject the suggestion of mootness. Petitioner Chandler represented, as an officer of this Court, that he plans to run again, and counsel for the State does not contest that representation. See Tr. of Oral Arg. 4-6, 27; see also <span class="citation no-link">28 U. S. C. § 1653</span> (defective allegations of jurisdiction curable by amendment at trial or in appellate stages).</p>
</footnote>
<footnote label="3">
<p id="b407-7"> The Service’s program also required tests for individuals promoted or transferred to positions in which they would handle “classified” material. 489 U. S., at 661. The Court agreed that the Government “ha[d] a compelling interest in protecting truly sensitive information.” <em>Id,., </em>at 677. However, we did not rule on this aspect of the program, see <em>id., </em>at 677-678, <page-number citation-index="1" label="316">*316</page-number>because the record did not clarify “whether the category defined by the [regulation] encompassed] only those Customs employees likely to gain access to sensitive information," <em>id., </em>at 678.</p>
</footnote>
<footnote label="4">
<p id="b412-6"> In <em>Treasury Employees v. Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656</a></span> (1989), the applicant for promotion or transfer could not know precisely when action would be taken on the application. In contrast, the potential candidate knows from the start the timing of all relevant events.</p>
</footnote>
</opinion>
```

---
