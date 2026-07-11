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

## GROUP: _overhaul2/lake/cases/Dalia v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Dalia v. United States"
type: case
citation: "441 U.S. 238 (1979)"
parallel_cite: "99 S. Ct. 1682; 60 L. Ed. 2d 177"
neutral_cite: 1979 U.S. LEXIS 89
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-04-18
docket: 77-1722
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1979-04-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Dalia v. United States
  varies_by_point: false
  scope_note: Constitutional holdings on covert entry and manner-of-execution remain good law and are regularly applied to surveillance-installation warrants.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110061/dalia-v-united-states/"
  cluster_id: 110061
  opinion_id: 110061
  identity_checked: true
homes:
  - page: "[[Scope Manner and Related Issues]]"
    role: "Progeny (manner of execution / covert entry)"
related: ["[[Berger v. New York]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant", "search-warrant", "electronic-surveillance", "covert-entry", "warrant-execution", "title-iii"]
holding: "A court order authorizing Title III electronic surveillance implicitly authorizes the covert entry needed to install the device; the Fourth Amendment does not require a warrant to specify the manner of its execution, including covert entry."
lake:
  record_id: Dalia v. United States
  status: verified
  projected_at: 2026-07-09
---

# Dalia v. United States

*441 U.S. 238 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Acting under a Title III order (18 U.S.C. § 2518) authorizing interception of oral communications in Dalia's business office, FBI agents covertly entered the office at night, installed a bug in the ceiling, and later re-entered to remove it. The authorizing order did not expressly state that the surveillance would be carried out by a covert entry. Dalia moved to suppress the resulting evidence, arguing the unannounced break-in to install the device was unconstitutional and unauthorized.

## Issue
(1) Whether the Fourth Amendment categorically forbids covert entry of private premises to install electronic surveillance equipment; and (2) whether a Title III surveillance order must include an explicit, advance statement authorizing such a covert entry.

## Rule
Covert entry to install lawful bugging equipment is not [[Common Legal Terms#per-se|per se]] unconstitutional. "We make explicit, therefore, what has long been implicit in our decisions dealing with this subject: The Fourth Amendment does not prohibit *per se* a covert entry performed for the purpose of installing otherwise legal electronic bugging equipment." — 441 U.S. at 248. ^pin-248

A warrant authorizing surveillance need not separately spell out that it will be executed by covert entry. "Nothing in the language of the Constitution or in this Court's decisions interpreting that language suggests that, in addition to the three requirements discussed above, search warrants also must include a specification of the precise manner in which they are to be executed. On the contrary, it is generally left to the discretion of the executing officers to determine the details of how best to proceed with the performance of a search authorized by warrant" — subject to the general protection "against unreasonable searches and seizures." — [*Id.* at 257](https://www.courtlistener.com/opinion/110061/dalia-v-united-states/#:~:text=Nothing%20in%20the%20language%20of). ^pin-257

## Application
Title III's language, structure, and history showed Congress meant to authorize courts to approve electronic surveillance "without limitation on the means necessary to its accomplishment, so long as they are reasonable," and Congress understood that "[a]bsent covert entry … almost all electronic bugging would be impossible." The April 5 order therefore implicitly authorized the covert entry needed to install the device; and because the Fourth Amendment does not require a warrant to specify its manner of execution, the order's silence about the break-in did not invalidate the surveillance. The covert entry was a reasonable means of executing a valid order.

## Conclusion
The covert entry to install the bug was constitutional and authorized by the Title III order; Dalia's conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Dalia*'s constitutional holdings — that covert entry to install lawful surveillance equipment is not [[Common Legal Terms#per-se|per se]] unreasonable, and that a warrant need not specify the manner of its execution — remain good law and govern surveillance-installation and analogous warrant-execution questions.

## Appears on
- [[Scope Manner and Related Issues]] — *Progeny (manner of execution / covert entry)*

## Sources
- *Dalia v. United States*, 441 U.S. 238 (1979) — https://www.courtlistener.com/opinion/110061/dalia-v-united-states/ — pinpoints: 248, 257.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "520b7e94e6f20c6a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Dalia v. United States"}, "payload": {"all": [{"cite": "441 U.S. 238", "page": "238", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "441"}, {"cite": "99 S. Ct. 1682", "page": "1682", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "99"}, {"cite": "60 L. Ed. 2d 177", "page": "177", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "60"}, {"cite": "1979 U.S. LEXIS 89", "page": "89", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1979"}], "display": "441 U.S. 238", "official": {"cite": "441 U.S. 238", "page": "238", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "441"}, "official_selection_present": true, "record_id": "Dalia v. United States"}}
{"assertion_id": "b7470b1229c729a5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-257", "record_id": "Dalia v. United States"}, "payload": {"fragment": "#:~:text=Nothing%20in%20the%20language%20of", "page": null, "pin_id": "pin-257", "pinpoint_status": "star-verified", "quote": "Nothing in the language of the Constitution or in this Court's decisions interpreting that language suggests that, in addition to the three requirements discussed above, search warrants also must include a specification of the precise manner in which they are to be executed. On the contrary, it is generally left to the discretion of the executing officers to determine the details of how best to proceed with the performance of a search authorized by warrant", "quote_fidelity": "matched", "record_id": "Dalia v. United States", "star_marker": "257"}}
{"assertion_id": "f1edede47d131b4f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-248", "record_id": "Dalia v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-248", "pinpoint_status": "slip-only", "quote": "--- # Dalia v. United States *441 U.S. 238 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting under a Title III order (18 U.S.C. § 2518) authorizing interception of oral communications in Dalia's business office, FBI agents covertly entered the office at night, installed a bug in the ceiling, and later re-entered to remove it. The authorizing order did not expressly state that the surveillance would be carried out by a covert entry. Dalia moved to suppress the resulting evidence, arguing the unannounced break-in to install the device was unconstitutional and unauthorized. ## Issue (1) Whether the Fourth Amendment categorically forbids covert entry of private premises to install electronic surveillance equipment; and (2) whether a Title III surveillance order must include an explicit, advance statement authorizing such a covert entry. ## Rule Covert entry to install lawful bugging equipment is not per se unconstitutional.", "quote_fidelity": "mismatch", "record_id": "Dalia v. United States", "star_marker": null}}
{"assertion_id": "1e0f8a6559b57efc", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Dalia v. United States"}, "payload": {"as_of_content": "1979-04-18", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Dalia v. United States", "scope_note": "Constitutional holdings on covert entry and manner-of-execution remain good law and are regularly applied to surveillance-installation warrants.", "varies_by_point": false}}
```

### lake record — Dalia v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Dalia v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Dalia v. United States",
    "case_name_short": "Dalia",
    "case_name_full": "Dalia v. United States",
    "input_case_name": "Dalia v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-04-18",
    "year": 1979,
    "docket": "77-1722",
    "cluster_id": 110061,
    "lead_opinion_id": 110061,
    "sibling_ids": [
      110061,
      9427537,
      9427538,
      9427539
    ],
    "absolute_url": "/opinion/110061/dalia-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "441 U.S. 238",
      "volume": "441",
      "reporter": "U.S.",
      "page": "238",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 1682",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1682",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 L. Ed. 2d 177",
        "volume": "60",
        "reporter": "L. Ed. 2d",
        "page": "177",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 89",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "89",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "441 U.S. 238",
        "volume": "441",
        "reporter": "U.S.",
        "page": "238",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 1682",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1682",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 L. Ed. 2d 177",
        "volume": "60",
        "reporter": "L. Ed. 2d",
        "page": "177",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 89",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "89",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "441 U.S. 238",
    "official_selection": {
      "court_class": "scotus",
      "selected": "441 U.S. 238",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-248",
      "page": null,
      "quote": "--- # Dalia v. United States *441 U.S. 238 (1979)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting under a Title III order (18 U.S.C. \u00a7 2518) authorizing interception of oral communications in Dalia's business office, FBI agents covertly entered the office at night, installed a bug in the ceiling, and later re-entered to remove it. The authorizing order did not expressly state that the surveillance would be carried out by a covert entry. Dalia moved to suppress the resulting evidence, arguing the unannounced break-in to install the device was unconstitutional and unauthorized. ## Issue (1) Whether the Fourth Amendment categorically forbids covert entry of private premises to install electronic surveillance equipment; and (2) whether a Title III surveillance order must include an explicit, advance statement authorizing such a covert entry. ## Rule Covert entry to install lawful bugging equipment is not per se unconstitutional.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-257",
      "page": null,
      "quote": "Nothing in the language of the Constitution or in this Court's decisions interpreting that language suggests that, in addition to the three requirements discussed above, search warrants also must include a specification of the precise manner in which they are to be executed. On the contrary, it is generally left to the discretion of the executing officers to determine the details of how best to proceed with the performance of a search authorized by warrant",
      "star_marker": "257",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 30611,
      "fragment": "#:~:text=Nothing%20in%20the%20language%20of",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1979-04-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Dalia v. United States",
    "varies_by_point": false,
    "scope_note": "Constitutional holdings on covert entry and manner-of-execution remain good law and are regularly applied to surveillance-installation warrants.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Lonnell Glover",
          "cluster_id": 2641656,
          "cite": [
            "407 U.S. App. D.C. 189",
            "736 F.3d 509",
            "2013 WL 5951521",
            "2013 U.S. App. LEXIS 22667"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane1_negative"
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
        "journal_ref": "Dalia v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Christi Lynn Johnston",
          "cluster_id": 2855234,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cunningham",
          "cluster_id": 197364,
          "cite": [
            "113 F.3d 289",
            "1997 U.S. App. LEXIS 11632",
            "1997 WL 251388"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Garner",
          "cluster_id": 6577195,
          "cite": [
            "423 Mass. 735",
            "672 N.E.2d 510",
            "1996 Mass. LEXIS 305"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Joan Cody v. Keith Mello and Thomas Murray",
          "cluster_id": 698733,
          "cite": [
            "59 F.3d 13",
            "32 Fed. R. Serv. 3d 1002",
            "1995 U.S. App. LEXIS 15863",
            "1995 WL 377409"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chen",
          "cluster_id": 9012794,
          "cite": [
            "979 F.2d 714"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Koyomejian",
          "cluster_id": 9002607,
          "cite": [
            "946 F.2d 1450",
            "1991 WL 204462"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pembaur v. City of Cincinnati",
          "cluster_id": 111615,
          "cite": [
            "89 L. Ed. 2d 452",
            "106 S. Ct. 1292",
            "475 U.S. 469",
            "1986 U.S. LEXIS 33",
            "54 U.S.L.W. 4289"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
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
        "journal_ref": "Dalia v. United States:lane2_top_cited"
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
        "journal_ref": "Dalia v. United States:lane2_top_cited"
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
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lewis v. United States",
          "cluster_id": 110213,
          "cite": [
            "63 L. Ed. 2d 198",
            "100 S. Ct. 915",
            "445 U.S. 55",
            "1980 U.S. LEXIS 85"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Grubbs",
          "cluster_id": 145670,
          "cite": [
            "164 L. Ed. 2d 195",
            "126 S. Ct. 1494",
            "547 U.S. 90",
            "2006 U.S. LEXIS 2496"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lawmaster v. Ward",
          "cluster_id": 155277,
          "cite": [
            "125 F.3d 1341",
            "1997 WL 577708"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mink v. Knox",
          "cluster_id": 158328,
          "cite": [
            "613 F.3d 995",
            "38 Media L. Rep. (BNA) 1961",
            "2010 U.S. App. LEXIS 14684",
            "2010 WL 2802729"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cynthia Archer v. John Chisholm",
          "cluster_id": 4422481,
          "cite": [
            "870 F.3d 603",
            "2017 WL 3709149",
            "2017 U.S. App. LEXIS 16493"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. George Wuagneux",
          "cluster_id": 406519,
          "cite": [
            "683 F.2d 1343",
            "1982 U.S. App. LEXIS 16435",
            "11 Fed. R. Serv. 334"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
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
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Liston v. County of Riverside",
          "cluster_id": 7049587,
          "cite": [
            "120 F.3d 965",
            "97 Daily Journal DAR 9229",
            "97 Cal. Daily Op. Serv. 5742",
            "1997 U.S. App. LEXIS 18962",
            "1997 WL 403988"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Henning Heldt and Duke Snider, United States of America v. Mary Sue Hubbard, United States of America v. Sharon Thomas, United States of America v. Gregory Willardson, United States of America v. Richard Weigand, United States of America v. Cindy Raymond, United States of America v. Gerald Bennett Wolfe, United States of America v. Mitchell Hermann",
          "cluster_id": 398883,
          "cite": [
            "668 F.2d 1238"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Southard",
          "cluster_id": 8926695,
          "cite": [
            "700 F.2d 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gilmere v. City Of Atlanta",
          "cluster_id": 459876,
          "cite": [
            "774 F.2d 1495"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Euge",
          "cluster_id": 110191,
          "cite": [
            "63 L. Ed. 2d 141",
            "100 S. Ct. 874",
            "444 U.S. 707",
            "1980 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lawmaster v. Ward",
          "cluster_id": 746807,
          "cite": [
            "125 F.3d 1341",
            "1997 Colo. J. C.A.R. 2061",
            "1997 U.S. App. LEXIS 25248"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Abu-Jihaad",
          "cluster_id": 181375,
          "cite": [
            "630 F.3d 102",
            "2010 U.S. App. LEXIS 25832",
            "2010 WL 5140864"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fred Tarpley, Sr. v. Raymond J. Greene",
          "cluster_id": 406593,
          "cite": [
            "684 F.2d 1",
            "221 U.S. App. D.C. 227",
            "1982 U.S. App. LEXIS 17751"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Purdy Lambert (84-5660) Philip M. Block (84-5661), Defendants",
          "cluster_id": 457615,
          "cite": [
            "771 F.2d 83",
            "1985 U.S. App. LEXIS 22335"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jack Southard, United States of America v. Monsour Ferris, A/K/A Monte, United States of America v. Lester Banker, A/K/A Lem, United States of America v. John Brian, A/K/A John Baborian, United States of America v. Anna Quinterno, United States of America v. Vincent Quinterno, United States of America v. Harry Kachougian, A/K/A Tom and Tommy, United States of America v. Robert Martin, United States of America v. Bernard Falk, United States of America v. Anthony Lauro, A/K/A Poochie",
          "cluster_id": 414332,
          "cite": [
            "700 F.2d 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
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
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mark L. Simons",
          "cluster_id": 767973,
          "cite": [
            "206 F.3d 392",
            "2000 U.S. App. LEXIS 2877",
            "2000 WL 223332"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dalia v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110061 OR 9427537 OR 9427538 OR 9427539) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NDQ0NTc2MDAwMDAmcz04OTg4ODEzJnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110061+OR+9427537+OR+9427538+OR+9427539%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110061 OR 9427537 OR 9427538 OR 9427539)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05MiZzPTgxMDEzMyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110061+OR+9427537+OR+9427538+OR+9427539%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110061 OR 9427537 OR 9427538 OR 9427539)",
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
    "complete_query": "cites:(110061 OR 9427537 OR 9427538 OR 9427539)",
    "indexed_citing_opinions": 348,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110061,
        "count": 285,
        "count_source": "search"
      },
      {
        "opinion_id": 9427537,
        "count": 67,
        "count_source": "search"
      },
      {
        "opinion_id": 9427538,
        "count": 1,
        "count_source": "search"
      },
      {
        "opinion_id": 9427539,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 641,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/dalia-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2NzE2NjImcz05NDc2MzI0JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110061+OR+9427537+OR+9427538+OR+9427539%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110061,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 105021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 105172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 106078,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 106288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 106525,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 107319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 107735,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 108582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 108596,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 108767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 109572,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 109584,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 109755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 109876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 308678,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 324480,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 339006,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 344771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 345743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 349546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 350102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 355846,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 359575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 359662,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 1442699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 1595144,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110061,
        "cited_id": 2443377,
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
    "date_created": "2026-07-05T01:55:39Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T01:55:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T01:55:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:04:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T01:55:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Dalia v. United States (truncated)

```
<div>
<center><b><span class="citation" data-id="9427537"><a href="/opinion/110061/dalia-v-united-states/" aria-description="Citation for case: Dalia v. United States">441 U.S. 238</a></span> (1979)</b></center>
<center><h1>DALIA<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 77-1722.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 9, 10, 1979.</center>
<center>Decided April 18, 1979.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE THIRD CIRCUIT.
<p><span class="star-pagination">*240</span> <i>Louis Ruprecht</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Deputy Solicitor General Frey</i> argued the cause for the United States. With him on the brief were <i>Solicitor General McCree, Assistant Attorney General Heymann, William C. Bryson, Kenneth S. Geller,</i> and <i>Jerome M. Feit.</i></p>
<p>MR. JUSTICE POWELL delivered the opinion of the Court.</p>
<p>Title III of the Omnibus Crime Control and Safe Streets Act of 1968 (Title III), <span class="citation no-link">18 U. S. C. §§ 2510-2520</span>, permits courts to authorize electronic surveillance<sup>[1]</sup> by Government officers in specified situations. We took this case by writ of <span class="star-pagination">*241</span> certiorari to resolve two questions concerning the implementation of Title III surveillance orders. <span class="citation multiple-matches"><a href="/c/U.%20S./439/817/">439 U. S. 817</a></span>. First, may courts authorize electronic surveillance that requires covert entry<sup>[2]</sup> into private premises for installation of the necessary equipment? Second, must authorization for such surveillance include a specific statement by the court that it approves of the covert entry?<sup>[3]</sup></p>
<p></p>
<h2>I</h2>
<p>On March 14, 1973, Justice Department officials applied to the United States District Court for the District of New Jersey, seeking authorization under <span class="citation no-link">18 U. S. C. § 2518</span> to intercept telephone conversations on two telephones in petitioner's business office. After examining the affidavits submitted in support of the Government's request, the District Court authorized the wiretap for a period of 20 days or until the purpose of the interception was achieved, whichever came first. The court found probable cause to believe that petitioner was a member of a conspiracy the purpose of which was to steal goods being shipped in interstate commerce in violation of <span class="citation no-link">18 U. S. C. § 659</span>. Moreover, the court found reason to believe that petitioner's business telephones were being used to further this conspiracy and that means of investigating the conspiracy <span class="star-pagination">*242</span> other than electronic surveillance would be unlikely to succeed and would be dangerous. The wiretap order carefully enumerated the telephones to be affected and the types of conversations to be intercepted. Finally, the court ordered the officials in charge of the interceptions to take all reasonable precautions "to minimize the interception of communications not otherwise subject to interception," and required the officials to make periodic progress reports.</p>
<p>At the end of the 20-day period covered by the March 14 court order, the Government requested an extension of the wiretap authorization. In addition, the Government for the first time asked the court to allow it to intercept all oral communications taking place in petitioner's office, including those not involving the telephone. On April 5, 1973, the court granted the Government's second request. Its order concerning the wiretap of petitioner's telephones closely tracked the March 14 order. Finding reasonable cause to believe that petitioner's office was being used by petitioner and others in connection with the alleged conspiracy, the court also authorized, for a maximum period of 20 days, the interception of all oral communications concerning the conspiracy at "the business office of Larry Dalia, consisting of an enclosed room, approximately fifteen (15) by eighteen (18) feet in dimension, and situated in the northwesterly corner of a one-story building housing Wrap-O-Matic Machinery Company, Ltd., and Precise Packaging, and located at 1105 West St. George Avenue, Linden, New Jersey." The order included protective provisions similar to those in the March 14 wiretapping order.<sup>[4]</sup> The electronic surveillance order of April 5 was extended by court order on April 27, 1973.</p>
<p><span class="star-pagination">*243</span> On November 6, 1975, petitioner was indicted in a five-count indictment charging that he had been involved in a <span class="star-pagination">*244</span> conspiracy to steal an interstate shipment of fabric.<sup>[5]</sup> At trial, the Government introduced evidence showing that petitioner had been approached in March 1973 and asked to store in his New Jersey warehouse "a load of merchandise." Although petitioner declined the request, he directed the requesting party to Higgins, an associate, with whom he agreed to share the $1,500 storage fee that was offered. The merchandise stored under this contract proved to be a tractor-trailer full of fabric worth $250,000 that three men stole on April 3, 1973, and transported to Higgins' warehouse. Two days after the theft, FBI agents arrested Higgins and the individuals involved in the robbery.</p>
<p>The Government introduced into evidence at petitioner's trial various conversations intercepted pursuant to the court <span class="star-pagination">*245</span> orders of March 14, April 5, and April 27, 1973. Intercepted telephone conversations showed that petitioner had arranged for the storage at Higgins' warehouse and had helped negotiate the terms for that storage. One telephone conversation that took place after Higgins' arrest made clear that petitioner had given advice to others involved in the robbery to "sit tight" and not to use the telephone. Finally, the Government introduced transcripts of conversations intercepted from petitioner's office under the April 5 bugging order. In these conversations, petitioner had discussed with various participants in the robbery how best to proceed after their confederates had been arrested. The unmistakable inference to be drawn from petitioner's statements in these conversations is that he was an active participant in the scheme to steal the truckload of fabric.</p>
<p>Before trial, petitioner moved to suppress evidence obtained through the interception of conversations by means of the device installed in his office. The District Court denied the suppression motion without prejudice to its being renewed following trial. After petitioner was convicted on two counts,<sup>[6]</sup> he renewed his motion and the court held an evidentiary hearing concerning the method by which the electronic device had been installed. At this hearing it was shown that, although the April 5 court order did not explicitly authorize entry of petitioner's business, the FBI agents assigned the task of implementing the order had entered petitioner's office secretly at midnight on April 5 and had spent three hours in the building installing an electronic bug in the ceiling. All electronic surveillance of petitioner ended on May 16, 1973, at which time the agents re-entered petitioner's office and removed the bug.</p>
<p>In denying a second time petitioner's motion to suppress the evidence obtained from the bug, the trial court ruled <span class="star-pagination">*246</span> that under Title III a covert entry to install electronic eavesdropping equipment is not unlawful merely because the court approving the surveillance did not explicitly authorize such an entry. <span class="citation" data-id="1595144"><a href="/opinion/1595144/united-states-v-dalia/" aria-description="Citation for case: United States v. Dalia">426 F. Supp. 862</a></span> (1977). Indeed, in the court's view, "implicit in the court's order [authorizing electronic surveillance] is concomitant authorization for agents to covertly enter the premises in question and install the necessary equipment." <span class="citation" data-id="1595144"><a href="/opinion/1595144/united-states-v-dalia/#866" aria-description="Citation for case: United States v. Dalia"><i>Id.,</i> at 866</a></span>. As the court concluded that the FBI agents who had installed the electronic device were executing a lawful warrant issued by the court, the sole question was whether the method they chose for execution was reasonable. Under the circumstances, the court found the covert entry of petitioner's office to have been "the safest and most successful method of accomplishing the installation." <i><span class="citation" data-id="1595144"><a href="/opinion/1595144/united-states-v-dalia/" aria-description="Citation for case: United States v. Dalia">Ibid.</a></span></i> Indeed, noting that petitioner himself had indicated that such a device could only have been installed through such an entry, the court observed that "[i]n most cases the only form of installing such devices is through breaking and entering. The nature of the act is such that entry must be surreptitious and must not arouse suspicion, and the installation must be done without the knowledge of the residents or occupants." <i><span class="citation" data-id="1595144"><a href="/opinion/1595144/united-states-v-dalia/" aria-description="Citation for case: United States v. Dalia">Ibid.</a></span></i></p>
<p>The Court of Appeals for the Third Circuit affirmed petitioner's conviction. <span class="citation" data-id="355846"><a href="/opinion/355846/united-states-v-lawrence-dalia/" aria-description="Citation for case: United States v. Lawrence Dalia">575 F. 2d 1344</a></span> (1978). Agreeing with the District Court, it rejected petitioner's contention that separate court authorization was necessary for the covert entry of petitioner's office, although it noted that "the more prudent or preferable approach for government agents would be to include a statement regarding the need of a surreptitious entry in a request for the interception of oral communications when a break-in is contemplated." <span class="citation" data-id="355846"><a href="/opinion/355846/united-states-v-lawrence-dalia/#1346" aria-description="Citation for case: United States v. Lawrence Dalia"><i>Id.,</i> at 1346-1347</a></span>.</p>
<p></p>
<h2>II</h2>
<p>Petitioner first contends that the Fourth Amendment prohibits covert entry of private premises in all cases, irrespective of the reasonableness of the entry or the approval of a court. <span class="star-pagination">*247</span> He contends that Title III is unconstitutional insofar as it enables courts to authorize covert entries for the installation of electronic bugging devices.</p>
<p>In several cases this Court has implied that in some circumstances covert entry to install electronic bugging devices would be constitutionally acceptable if done pursuant to a search warrant. Thus, for example, in <i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">347 U. S. 128</a></span> (1954), the plurality stated that in conducting electronic surveillance, state police officers had "flagrantly, deliberately, and persistently violated the fundamental principle declared by the Fourth Amendment as a restriction on the Federal Government." <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#132" aria-description="Citation for case: Irvine v. California"><i>Id.,</i> at 132</a></span>. It emphasized that the bugging equipment was installed through a covert entry of the defendant's home "<i>without a search warrant</i> or other process." <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Ibid.</a></span></i> (emphasis added). Similarly, in <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 511-512</a></span> (1961), it was noted that "[t]his Court has never held that a federal officer may <i>without warrant</i> and without consent physically entrench into a man's office or home, there secretly observe or listen, and relate at the man's subsequent criminal trial what was seen or heard." (Emphasis added.) Implicit in decisions such as <i><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">Silverman</a></span></i> and <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Irvine</a></span></i> has been the Court's view that covert entries are constitutional in some circumstances, at least if they are made pursuant to warrant.</p>
<p>Moreover, we find no basis for a constitutional rule proscribing all covert entries. It is well established that law officers constitutionally may break and enter to execute a search warrant where such entry is the only means by which the warrant effectively may be executed. See, <i>e. g., </i><i>Payne</i> v. <i>United States,</i> <span class="citation" data-id="324480"><a href="/opinion/324480/charles-edward-payne-v-united-states/#1394" aria-description="Citation for case: Charles Edward Payne v. United States">508 F. 2d 1391, 1394</a></span> (CA5 1975); cf. <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#28" aria-description="Citation for case: Ker v. California">374 U. S. 23, 28, 38</a></span> (1963); <span class="citation no-link">18 U. S. C. § 3109</span>. Petitioner nonetheless argues that covert entries are unconstitutional for their lack of notice. This argument is frivolous, as was indicated in <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span>, 355 n. 16 (1967), where the Court stated that "officers need not <span class="star-pagination">*248</span> announce their purpose before conducting an otherwise [duly] authorized search if such an announcement would provoke the escape of the suspect or the destruction of critical evidence."<sup>[7]</sup> In <i>United States</i> v. <i>Donovan,</i> <span class="citation" data-id="9426645"><a href="/opinion/109584/united-states-v-donovan/" aria-description="Citation for case: United States v. Donovan">429 U. S. 413</a></span>, 429 n. 19 (1977), we held that Title III provided a constitutionally adequate substitute for advance notice by requiring that once the surveillance operation is completed the authorizing judge must cause notice to be served on those subjected to surveillance. See <span class="citation no-link">18 U. S. C. § 2518</span> (8) (d). There is no reason why the same notice is not equally sufficient with respect to electronic surveillances requiring covert entry. We make explicit, therefore, what has long been implicit in our decisions dealing with this subject: The Fourth Amendment does not prohibit <i>per se</i> a covert entry performed for the purpose of installing otherwise legal electronic bugging equipment.<sup>[8]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*249</span> III</h2>
<p>Petitioner's second contention is that Congress has not given the courts statutory authority to approve covert entries for the purpose of installing electronic surveillance equipment, even if constitutionally it could have done so. Petitioner emphasizes that although Title III sets forth with meticulous care the circumstances in which electronic surveillance is permitted, there is no comparable indication in the statute that covert entry ever may be ordered. Accord, <i>United States</i> v. <i>Santora,</i> <span class="citation" data-id="359575"><a href="/opinion/359575/united-states-v-ronald-santora-earl-rardin-maurice-eugene-lickteig/#457" aria-description="Citation for case: United States v. Ronald Santora, Earl Rardin, Maurice...">583 F. 2d 453, 457-458</a></span> (CA9 1978).</p>
<p>Title III does not refer explicitly to covert entry. The language, structure, and history of the statute, however, demonstrate that Congress meant to authorize courtsin certain specified circumstancesto approve electronic surveillance without limitation on the means necessary to its accomplishment, so long as they are reasonable under the circumstances. Title III provides a comprehensive scheme for the regulation of electronic surveillance, prohibiting all secret interception of communications except as authorized by certain state and federal judges in response to applications from specified federal and state law enforcement officials. See <span class="citation no-link">18 U. S. C. §§ 2511</span>, 2515, and 2518; <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#301" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 301-302</a></span> (1972). Although Congress was fully aware of the distinction between bugging and wiretapping, see S. Rep. No. 1097, 90th Cong., 2d Sess., 68 (1968), Title III by its terms deals with each form of surveillance in essentially the same manner. See <span class="citation no-link">18 U. S. C. §§ 2510</span> (1) and (2); n. 1, <i>supra.</i> Orders authorizing interceptions of either wire or oral communications may be entered only after the court has made specific determinations concerning the likelihood that the interception will disclose evidence of criminal conduct. See <span class="citation no-link">18 U. S. C. § 2518</span> (3). Moreover, with respect to both wiretapping and bugging, an authorizing court must <span class="star-pagination">*250</span> specify the exact scope of the surveillance undertaken, enumerating the parties whose communications are to be overheard (if they are known), the place to be monitored, and the agency that will do the monitoring. See <span class="citation no-link">18 U. S. C. § 2518</span> (4).</p>
<p>The plain effect of the detailed restrictions of § 2518 is to guarantee that wiretapping or bugging occurs only when there is a genuine need for it and only to the extent that it is needed.<sup>[9]</sup> Once this need has been demonstrated in accord with the requirements of § 2518, the courts have broad authority to "approv[e] interception of wire or oral communications," <span class="citation no-link">18 U. S. C. §§ 2516</span> (1), (2), subject of course to constitutional limitations. See Part II, <i>supra.</i><sup>[10]</sup> Nowhere in Title III is there any indication that the authority of courts under § 2518 is to be limited to approving those methods of interception that do not require covert entry for installation of the intercepting equipment.<sup>[11]</sup></p>
<p><span class="star-pagination">*251</span> The legislative history of Title III underscores Congress' understanding that courts would authorize electronic surveillance in situations where covert entry of private premises was necessary. Indeed, a close examination of that history reveals that Congress did not explicitly address the question of covert entries in the Act, only because it did not perceive surveillance requiring such entries to differ in any important way from that performed without entry. Testimony before subcommittees considering Title III and related bills indicated that covert entries were a necessary part of most electronic bugging operations. See, <i>e. g.,</i> Anti-Crime Program: Hearings on H. R. 5037, etc., before Subcommittee No. 5 of the House Committee on the Judiciary, 90th Cong., 1st Sess., 1031 (1967). Moreover, throughout the Senate Report on Title III indiscriminate reference is made to the types of surveillance this Court reviewed in <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967), and <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967). See, <i>e. g.,</i> S. Rep. No. 1097, <i>supra,</i> at 74-75, 97, 101-102, 105. Apparently Committee members did not find it significant that <i><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span></i> involved a covert entry, whereas <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> did not. Compare <i>Berger</i> v. <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#45" aria-description="Citation for case: Berger v. New York"><i>New York, supra,</i> at 45</a></span>, with <i>Katz</i> v. <i>United States, supra,</i> at 348.<sup>[12]</sup></p>
<p>It is understandable, therefore, that by the time Title III <span class="star-pagination">*252</span> was discussed on the floor of Congress, those Members who referred to covert entries indicated their understanding that such entries would necessarily be a part of bugging authorized under Title III. Thus, for example, in voicing his support for Title III Senator Tydings emphasized the difficulties attendant upon installing necessary equipment:</p>
<blockquote>"[S]urveillance is very difficult to use. Tape [<i>sic</i>] must be installed on telephones, and wires strung. <i>Bugs are difficult to install in many places since surreptitious entry is often impossible. Often, more than one entry is necessary to adjust equipment.</i>" 114 Cong. Rec. 12989 (1968) (emphasis added).</blockquote>
<p>In the face of this record, one simply cannot assume that Congress, aware that most bugging requires covert entry, nonetheless wished to except surveillance requiring such entries from the broad authorization of Title III, and that it resolved to do so by remaining silent on the subject. On the contrary, the language and history of Title III convey quite a different explanation for Congress' failure to distinguish between surveillance that requires covert entry and that which does not: Those considering the surveillance legislation understood that, by authorizing electronic interception of oral communications in addition to wire communications, they were necessarily authorizing surreptitious entries.</p>
<p>Finally, Congress' purpose in enacting the statute would be largely thwarted if we were to accept petitioner's invitation to read into Title III a limitation on the courts' authority under § 2518. Congress permitted limited electronic surveillance under Title III because it concluded that both wiretapping and bugging were necessary to enable law enforcement authorities to combat successfully certain forms of crime.<sup>[13]</sup><span class="star-pagination">*253</span> Absent covert entry, however, almost all electronic bugging would be impossible.<sup>[14]</sup> See <i>United States</i> v. <i>Ford,</i> <span class="citation" data-id="1442699"><a href="/opinion/1442699/united-states-v-ford/#882" aria-description="Citation for case: United States v. Ford">414 F. Supp. 879, 882</a></span> (DC 1976), aff'd, 180 U. S. App. D. C. 1, <span class="citation" data-id="344771"><a href="/opinion/344771/united-states-v-carroll-d-ford-united-states-of-america-v-wesley/" aria-description="Citation for case: United States v. Carroll D. Ford. United States of...">553 F. 2d 146</a></span> (1977); McNamara, The Problem of Surreptitious Entry <span class="star-pagination">*254</span> to Effectuate Electronic Eavesdrops: How Do You Proceed After the Court Says "Yes"?, <span class="citation no-link">15 Am. Crim. L. Rev. 1</span>, 3 (1977). As recently as 1976, a congressional commission established to study and evaluate the effectiveness of Title III concluded that in most cases electronic surveillance cannot be performed without covert entry into the premises being monitored. See U. S. National Commission for Review of Federal and State Laws Relating to Wiretapping and Electronic Surveillance, Electronic Surveillance 15, 43, and n. 19, 86 (1976). The same conclusion was reached by the American Bar Association committee charged with formulating standards governing use of electronic surveillance. See ABA Project on Minimum Standards for Criminal Justice, Electronic Surveillance 65 n. 175, 149 (App. Draft 1971).<sup>[15]</sup></p>
<p>In sum, we conclude that Congress clearly understood that it was conferring power upon the courts to authorize covert entries ancillary to their responsibility to review and approve surveillance applications under the statute. To read the statute otherwise would be to deny the "respect for the policy of Congress [that] must save us from imputing to it a self-defeating, if not disingenuous purpose." <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span> (1939).<sup>[16]</sup></p>
<p></p>
<h2>IV</h2>
<p>Petitioner's final contention is that, if covert entries are to be authorized under Title III, the authorizing court must <span class="star-pagination">*255</span> explicitly set forth its approval of such entries before the fact. In this case, as is customary, the court's order constituted the sole written authorization of the surveillance of petitioner's office. As it did not state in terms that the surveillance was to include a covert entry, petitioner insists that the entry violated his Fourth Amendment privacy rights. Accord, <i>United States</i> v. <i><span class="citation" data-id="1442699"><a href="/opinion/1442699/united-states-v-ford/" aria-description="Citation for case: United States v. Ford">Ford</a></span>,</i> 180 U. S. App. D. C., at 25, <span class="citation" data-id="344771"><a href="/opinion/344771/united-states-v-carroll-d-ford-united-states-of-america-v-wesley/#170" aria-description="Citation for case: United States v. Carroll D. Ford. United States of...">553 F. 2d, at 170</a></span>; <i>Application of United States,</i> <span class="citation" data-id="349546"><a href="/opinion/349546/application-of-the-united-states-for-an-order-authorizing-the-interception/#644" aria-description="Citation for case: Application of the United States for an Order Authorizing...">563 F. 2d 637, 644</a></span> (CA4 1977).<sup>[17]</sup></p>
<p>The Fourth Amendment requires that search warrants be issued only "upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." Finding these words to be "precise and clear," <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481</a></span> (1965), this Court has interpreted them to require only three things. First, warrants must be issued by neutral, disinterested magistrates. See, <i>e. g., </i><i>Connally</i> v. <i>Georgia,</i> <span class="citation" data-id="109572"><a href="/opinion/109572/connally-v-georgia/#250" aria-description="Citation for case: Connally v. Georgia">429 U. S. 245, 250-251</a></span> (1977) (<i>per curiam</i>); <i>Shadwick</i> v. <i>Tampa,</i> <span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/#350" aria-description="Citation for case: Shadwick v. City of Tampa">407 U. S. 345, 350</a></span> (1972); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#459" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 459-460</a></span> (1971). Second, those seeking the warrant must demonstrate to the magistrate their probable cause to believe that "the evidence sought will aid in a particular apprehension or conviction" for a particular offense. <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#307" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 307</a></span> (1967). Finally, "warrants must particularly describe the `things to be seized,' " as well as the place to be searched. <i>Stanford</i> v. <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas"><i>Texas, supra,</i> at 485</a></span>.</p>
<p><span class="star-pagination">*256</span> In the present case, the April 5 court order authorizing the interception of oral communications occurring within petitioner's office was a warrant issued in full compliance with these traditional Fourth Amendment requirements. It was based upon a neutral magistrate's independent finding of probable cause to believe that petitioner had been and was committing specifically enumerated federal crimes, that petitioner's office was being used "in connection with the commission of [these] offenses," and that bugging the office would result in the interception of "oral communications concerning these offenses." App. 6a-7a. Moreover, the exact location and dimensions of petitioner's office were set forth, see n. 4, <i>supra,</i> and the extent of the search was restricted to the "[i]ntercept[ion of] oral communications of Larry Dalia and others as yet unknown, concerning the above-described offenses at the business office of Larry Dalia . . . ." App. 8a.<sup>[18]</sup></p>
<p>Petitioner contends, nevertheless, that the April 5 order was insufficient under the Fourth Amendment for its failure to specify that it would be executed by means of a covert <span class="star-pagination">*257</span> entry of his office. Nothing in the language of the Constitution or in this Court's decisions interpreting that language suggests that, in addition to the three requirements discussed above, search warrants also must include a specification of the precise manner in which they are to be executed. On the contrary, it is generally left to the discretion of the executing officers to determine the details of how best to proceed with the performance of a search authorized by warrant<sup>[19]</sup>subject of course to the general Fourth Amendment protection "against unreasonable searches and seizures."</p>
<p>Recognizing that the specificity required by the Fourth Amendment does not generally extend to the means by which warrants are executed, petitioner further argues that warrants for electronic surveillance are unique because often they impinge upon two different Fourth Amendment interests: The surveillance itself interferes only with the right to hold private conversations, whereas the entry subjects the suspect's property to possible damage and personal effects to unauthorized examination. This view of the Warrant Clause parses too finely the interests protected by the Fourth Amendment. Often in executing a warrant the police may find it necessary to interfere with privacy rights not explicitly considered by the judge who issued the warrant. For example, police executing an arrest warrant commonly find it necessary to enter <span class="star-pagination">*258</span> the suspect's home in order to take him into custody, and they thereby impinge on both privacy and freedom of movement. See, <i>e. g., </i><i>United States</i> v. <i>Cravero,</i> <span class="citation" data-id="8900306"><a href="/opinion/8912462/united-states-v-cravero/#421" aria-description="Citation for case: United States v. Cravero">545 F. 2d 406, 421</a></span> (CA5 1976) (on petition for rehearing). Similarly, officers executing search warrants on occasion must damage property in order to perform their duty. See, <i>e. g., </i><i>United States</i> v. <i>Brown,</i> <span class="citation" data-id="345743"><a href="/opinion/345743/united-states-v-henry-joie-brown/#305" aria-description="Citation for case: United States v. Henry Joie Brown">556 F. 2d 304, 305</a></span> (CA5 1977); <i>United States</i> v. <i>Gervato,</i> <span class="citation" data-id="308678"><a href="/opinion/308678/united-states-v-frank-gervato/#41" aria-description="Citation for case: United States v. Frank Gervato">474 F. 2d 40, 41</a></span> (CA3), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/864/">414 U. S. 864</a></span> (1973).</p>
<p>It would extend the Warrant Clause to the extreme to require that, whenever it is reasonably likely that Fourth Amendment rights may be affected in more than one way, the court must set forth precisely the procedures to be followed by the executing officers. Such an interpretation is unnecessary, as we have heldand the Government concedesthat the manner in which a warrant is executed is subject to later judicial review as to its reasonableness. See <i>Zurcher</i> v. <i>Stanford Daily,</i> <span class="citation" data-id="9427224"><a href="/opinion/109876/zurcher-v-stanford-daily/#559" aria-description="Citation for case: Zurcher v. Stanford Daily">436 U. S. 547, 559-560</a></span> (1978).<sup>[20]</sup> More important, we would promote empty formalism were we to require magistrates to make explicit what unquestionably is implicit in bugging authorizations:<sup>[21]</sup> that a covert entry, with its attendant interference with Fourth Amendment interests, may be necessary for the installation of the surveillance equipment. See <i>United States</i> v. <i>London,</i> <span class="citation" data-id="1444545"><a href="/opinion/1444545/united-states-v-london/#560" aria-description="Citation for case: United States v. London">424 F. Supp. 556, 560</a></span> (Md. 1976). We conclude, therefore, that the Fourth Amendment does not require that a Title III electronic surveillance order include a <span class="star-pagination">*259</span> specific authorization to enter covertly the premises described in the order.<sup>[22]</sup></p>
<p>The judgment of the Court of Appeals is</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE BRENNAN, with whom MR. JUSTICE STEWART joins except as to Part I, concurring in part and dissenting in part.</p>
<p>I concur in Parts I and II of the Court's opinion.</p>
<p></p>
<h2>I</h2>
<p>I dissent from Part III for the reasons stated in the dissenting opinion of MR. JUSTICE STEVENS which I join.</p>
<p></p>
<h2>II</h2>
<p>I also dissent from Part IV. In my view, even reading Title III to authorize covert entries, the Justice Department's present practice of securing specific authorization for covert entries is not only preferable, see <i>ante,</i> this page n. 22, but also constitutionally required.</p>
<p>Breaking and entering into private premises for the purpose of planting a bug cannot be characterized as a mere mode of warrant execution to be left to the discretion of the executing officer. See <i>ante,</i> at 257. The practice entails an invasion <span class="star-pagination">*260</span> of privacy of constitutional significance distinct from that which attends nontrespassory surveillance; indeed, it is tantamount to an independent search and seizure. First, rooms may be bugged without the need for surreptitious entry and physical invasion of private premises. See <i>Lopez</i> v. <i>United States,</i> <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#467" aria-description="Citation for case: Lopez v. United States">373 U. S. 427, 467-468</a></span> (1963) (BRENNAN, J., dissenting). Second, covert entry, a practice condemned long before we condemned unwarranted eavesdropping, see <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961), breaches physical as well as conversational privacy. The home or office itself, that "inviolate place which is a man's castle," <i><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">id.,</a></span></i> at 512 n. 4, is invaded. Third, the practice is particularly intrusive and susceptible to abuse since it leaves naked to the hands and eyes of government agents items beyond the reach of simple eavesdropping.</p>
<p>Because of these additional intrusions attendant to covert entries, the Constitution requires that government agents who wish to break into private premises first secure specific judicial authorization for the surreptitious entry. Authority for the physical invasion cannot be derived from a Title III order authorizing only electronic surveillance.</p>
<p>"[T]he Fourth Amendment confines an officer executing a search warrant strictly within the bounds set by the warrant," <i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span>, 394 n. 7 (1971), in order to assure that those "searches deemed necessary [remain] as limited as possible." <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#467" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 467</a></span> (1971). See <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 485</a></span> (1965); <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 196</a></span> (1927).<sup>[*]</sup> As a consequence, a warrant that describes <span class="star-pagination">*261</span> only the seizure of conversations cannot be read expansively to authorize constitutionally distinct physical invasions of privacy at the discretion of the executing officer. Rather, the Constitution demands that the necessity for home invasion be decided "by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948).</p>
<p>I cannot agree that adherence to this principle would amount to "specification of the precise manner" in which Title III orders are executed. See <i>ante,</i> at 257. The warrant could, consistent with the command of the Fourth Amendment, leave the details of how best to proceed with the covert entry to the discretion of the executing officers. The warrant need only state, as under the present Justice Department practice, that "surreptitious entry for the purpose of installing and removing any electronic interception devices [is] to be utilized in accomplishing the oral interception." <i>Ante,</i> at 259 n. 22.</p>
<p>Nor can I agree that adherence to the strictures of the Warrant and Particularity Clauses of the Fourth Amendment would amount to "empty formalism." See <i>ante,</i> at 258. Since premises may be bugged through means less drastic than home invasion, requiring police to secure prior approval for covert entries may well prevent unnecessary and improper intrusions. In any event, that the present case may not appear particularly abusive cannot justify the Court's crabbed interpretation of the Fourth Amendment. Mr. Justice Bradley's <span class="star-pagination">*262</span> admonition almost a century ago has even greater cogency in today's world of ever more intrusive governmental invasions of privacy:</p>
<blockquote>"It may be that it is the obnoxious thing in its mildest and least repulsive form; but illegitimate and unconstitutional practices get their first footing in that way, namely, by silent approaches and slight deviations from legal modes of procedure. This can only be obviated by adhering to the rule that constitutional provisions for the security of person and property should be liberally construed. A close and literal construction deprives them of half their efficacy, and leads to gradual depreciation of the right, as if it consisted more in sound than in substance. It is the duty of courts to be watchful for the constitutional rights of the citizen, and against any stealthy encroachments thereon." <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 635</a></span> (1886).</blockquote>
<p>MR. JUSTICE STEVENS, with whom MR. JUSTICE BRENNAN and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>At midnight on the night of April 5-6, 1973, three persons pried open a window to petitioner's business office and secretly entered the premises. During the next three hours they moved freely about the building, eventually implanting a listening device in the ceiling. Several weeks later, they again broke into the office at night and removed the device.</p>
<p>The perpetrators of these break-ins were agents of the Federal Bureau of Investigation. Their office, however, carries with it no general warrant to trespass on private property. Without legislative or judicial sanction, the conduct of these agents was unquestionably "unreasonable" and therefore prohibited by the Fourth Amendment.<sup>[1]</sup> Moreover, that conduct <span class="star-pagination">*263</span> violated the Criminal Code of the State of New Jersey unless it was duly authorized.<sup>[2]</sup></p>
<p>The only consideration that arguably might legitimate these "otherwise tortious and possibly criminal" invasions of petitioner's private property,<sup>[3]</sup> is the fact that a federal judge had entered an order authorizing the agents to use electronic equipment to intercept oral communications at petitioner's office. The order, however, did not describe the kind of equipment to be used and made no reference to an entry, covert or otherwise, into private property. Nor does any statute expressly permit such activity or even authorize a federal judge to enter orders granting federal agents a license to commit criminal trespass. The initial question this case raises, therefore, is whether this kind of power should be read into a statute that does not expressly grant it.</p>
<p>In my opinion, there are three reasons, each sufficient by itself, for refusing to do so. First, until Congress has stated otherwise, our duty to protect the rights of the individual should hold sway over the interest in more effective law enforcement. Second, the structural detail of this statute precludes a reading that converts silence into thunder. Third, the legislative history affirmatively demonstrates that Congress never contemplated the situation now before the Court.</p>
<p></p>
<h2>I</h2>
<p>"Congress, like this Court, has an obligation to obey the mandate of the Fourth Amendment." <i>Marshall</i> v. <i>Barlow's Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#334" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 334</a></span> (STEVENS, J., dissenting). But Congress is better equipped than the Judiciary to make the empirical <span class="star-pagination">*264</span> judgment that a previously unauthorized investigative technique represents a "reasonable" accommodation between the privacy interests protected by the Fourth Amendment and effective law enforcement.<sup>[4]</sup> Throughout our history, therefore, it has been Congress that has taken the lead in granting new authority to invade the citizen's privacy.<sup>[5]</sup> It is appropriate to accord special deference to Congress whenever it has expressly balanced the need for a new investigatory technique against the undesirable consequences of any intrusion on constitutionally protected interests in privacy. See <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#334" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><i>id.,</i> at 334-339</a></span>.</p>
<p>But no comparable deference should be given federal intrusions on privacy that are not expressly authorized by Congress.<sup>[6]</sup> In my view, a proper respect for Congress' important <span class="star-pagination">*265</span> role in this area, as well as our tradition of interpreting statutes to avoid constitutional issues,<sup>[7]</sup> compels this conclusion.</p>
<p>The Court does not share this view. For this is the third time in as many years that it has condoned a serious intrusion on privacy that was not explicitly authorized by statute and that admittedly raised a substantial constitutional question. In <i>United States</i> v. <i>Ramsey,</i> <span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">431 U. S. 606</a></span>, the Court upheld an Executive regulation authorizing postal inspectors to open private letters without probable cause to believe they contained contraband.<sup>[8]</sup> In <i>United States</i> v. <i>New York Telephone Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S. 159</a></span>, the Court upheld orders authorizing the surreptitious pen-register surveillance of an individual and directing a private company to lend its assistance in that endeavor. Again, no explicit statutory authority existed for either order, despite Congress' otherwise comprehensive treatment of wire surveillance in Title III of the Omnibus Crime Control and Safe Streets Act of 1968 (Title III).<sup>[9]</sup></p>
<p><span class="star-pagination">*266</span> Today the Court has gone even further in finding an implicit grant of Executive power in Title III. That Title "does not refer explicitly to covert entry" of any kind, much less to entries that are tortious or criminal. <i>Ante,</i> at 249. Nevertheless, the Court holds that Congress, without having said so explicitly, has authorized the agents of a national police force in carrying out a surveillance order to break into private premises<sup>[10]</sup> in violation of state law. Moreover, the Court finds in the silent statute an open-ended authorization to effect such illegal entries without an explicit judicial determination that there is probable cause to believe they are necessary or even appropriate. In my judgment, it is most unrealistic to assume that Congress granted such broad and controversial authority to the Executive without making its intention to do so unmistakably plain. This is the paradigm case in which "the exact words of the statute provide the surest guide to determining Congress' intent."<sup>[11]</sup> I would not enlarge the coverage of the statute beyond its plain meaning.</p>
<p></p>
<h2>II</h2>
<p>The Court's conclusion that the statute implicitly authorizes breaking and entering is especially anomalous because the statutory scheme in all other respects is exhaustive and explicit.<sup>[12]</sup><span class="star-pagination">*267</span> "It simply does not make sense"<sup>[13]</sup> to conclude that Congresshaving minutely detailed (1) the process that "[t]he Attorney General, or any Assistant Attorney General specially designated by the Attorney General" must follow in authorizing federal police officers to seek an electronic surveillance order,<sup>[14]</sup> (2) the limited number of suspected offenses that will justify such an order,<sup>[15]</sup> (3) the showing that must be made to "a Federal judge" before he issues the order,<sup>[16]</sup> (4) the <span class="star-pagination">*268</span> standard the judge must apply in approving, and the format he must follow in preparing, the order,<sup>[17]</sup> (5) the time frame of execution and the manner of execution with respect to <span class="star-pagination">*269</span> minimizing the interception of communications not likely to involve criminal activity,<sup>[18]</sup> and even having more recently specified (6) certain "unobtrusive" means by which those <span class="star-pagination">*270</span> orders might be carried out without the awareness of the suspect<sup>[19]</sup>was content to leave national police officers with unbounded authority to carry out the resulting orders in any unspecified and obtrusive fashion they chose "subject of course to constitutional limitations." <i>Ante,</i> at 250.<sup>[20]</sup></p>
<p><span class="star-pagination">*271</span> In my view, it is the opposite conclusion that is true to the statutory structure. For "one simply cannot assume that Congress," see <i>ante,</i> at 252, wished to erect various procedural barriers against poor judgment on the part of the Attorney General and his subordinates in seeking, and on the part of federal district judges in issuing, eavesdropping orders only to commit their execution, even through illegal means, entirely to "the judgment and moderation of officers whose own interests and records are often at stake in the search." <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#182" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 182</a></span> (Jackson, J., dissenting). The detailed timing and minimization restrictions on the executing officer, see n. 18, <i>supra,</i> as well as the 1970 amendment to Title III concerning "unobtrusive" execution, see n. 19, <i>supra,</i> lead inescapably to the conclusion that Congress withheld authority to trespass on private property except through the limited means expressly dealt with in the statute.<sup>[21]</sup></p>
<p></p>
<h2>III</h2>
<p>Only one relevant conclusion can be drawn from a review of the entire legislative history of Title III. The legislators never even considered the possibility that they were passing a statute that would authorize federal agents to break into private premises without any finding of necessity by a neutral and detached magistrate.</p>
<p></p>
<h2>A</h2>
<p>The meager legislative remarks that are said to demonstrate that Title III's supporters implicitly endorsed breaking and <span class="star-pagination">*272</span> entering in order to install listening devices actually provide no support for that conclusion.</p>
<p>The reference to "judicial warrants authorizing [police] to hide bugs in the premises of criminal suspects," see <i>ante,</i> at 251 n. 12, was a comment by an <i>opponent</i> of the bill on investigative techniques that he believed this Court had ruled <i>illegal</i> in <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span>.<sup>[22]</sup> Since neither he, nor any supporter of the bill, suggested that those techniques would be authorized by Title III, his comment is hardly indicative of a legislative endorsement of such practices. Moreover, there is a marked difference between the judicially warranted "hid[ing of] bugs in the premises of criminal suspects" and a forcible entry that has not been expressly authorized by any judge. The difference between subterfuge and forcible trespass should not be ignored.</p>
<p>That difference explains why the Court's reliance on two statements by proponents of Title III that emphasize the technological limitations on "bugs" and "taps" is misplaced. The proponents believed these limitations would discourage the frequent use and abuse of electronic surveillance. Thus, in answer to repeated charges that passage of Title III would recreate Hitler's Germany or anticipate Orwell's "1984," Senator Tydings, in a passage partially quoted by the Court, <i>ante,</i> at 252, argued:</p>
<blockquote>"Contrary to what we have heard, electronic surveillance is not a lazy way to conduct an investigation. <i>It</i> <span class="star-pagination">*273</span> <i>will not be used wholesale as a substitute for physical investigation.</i>
</blockquote>
<p></p>
<h2>.....</h2>
<blockquote>"The reason[s] for such sparing use are simple. First, electronic surveillance is really useful only in conspiratorial activities. . . .</blockquote>
<blockquote>"Second, surveillance is very difficult to use. Tape must be installed on telephones and wires strung. <i>Bugs are difficult to install in many places since surreptitious entry is often impossible.</i> Often, more than one entry is necessary to adjust equipment. . . .</blockquote>
<blockquote>"Third, monitoring this equipment requires the expenditure of a great amount of law enforcement's time. . . ." 114 Cong. Rec. 12988-12989 (1968) (emphasis added).<sup>[23]</sup></blockquote>
<p>Read in context, this and like commentary are inconsistent with, rather than an endorsement of, unauthorized break-ins. For although it is of course true that surreptitious entry is often "impossible" when it must be accomplished without violating the law, surreptitious entry is by no means impossible (indeed, it is hardly "difficult") if it may be effected by whatever means the policeunhampered by the provisions of the criminal lawcan bring to their disposal. Despite the Court's understanding of it, I read Senator Tydings' remark as only one of many expressions by Title III's supporters of their belief that authorized electronic surveillance would be "carefully circumscribed," <i>id.,</i> at 13203 (Sen. Scott) and "rigidly controlled," <i>id.,</i> at 14715 (Sen. Tydings), not only by technology but also by "strict court supervision," <i>id.,</i> at 13200 (Sen. Scott), the "strictest guidelines," <i>id.,</i> at 16076 <span class="star-pagination">*274</span> (Rep. Harsha), and "an elaborate system of checks and safeguards." <i>Id.,</i> at 13204 (Sen. Scott).<sup>[24]</sup></p>
<p>Even the opponents of Title III, in parading before Congress the various invasions of privacy that they felt would accompany the passage of the statute, never once referred to breaking and entering private property. <i>E. g., id.,</i> at 14710 (Sen. Cooper); <i>id.,</i> at 14732 (Sen. Yarborough); <i>id.,</i> at 16066 (Rep. Celler). That they omitted such references while decrying far less aggravated invasions is strong evidence that they, at least, never thought about the issue that this case raises.<sup>[25]</sup> And since the sponsors of the legislation expressly stated that they had specified "every possible constitutional safeguard for the rights of individual privacy," <i>id.,</i> at <span class="star-pagination">*275</span> 14469 (Sen. McClellan),<sup>[26]</sup> their omission of any significant reference to these aggravated intrusions surely demonstrates that they did not consider this issue either.</p>
<p>In sum, as far as my research reveals, during the debates on Title III neither the proponents nor the opponents of the bill directly or indirectly expressed the view that the statute would authorize uninvited forcible trespasses by police officers as a means of implanting a listening device.</p>
<p></p>
<h2>B</h2>
<p>Because the drafters of Title III made "indiscriminate reference. . . to the types of surveillance this Court reviewed" in prior cases, <i>ante,</i> at 251, the Court draws the conclusion that Congress meant to authorize all "types of surveillance" discussed in those cases. The premise does not support the conclusion.</p>
<p>Many of those cases, including the two specifically cited by the Court,<sup>[27]</sup> held that the police conduct involved was unlawful. Rather than endorsing all of the techniques discussed in those cases, Congress was quite clearly trying to <i>avoid</i> the incidents of unconstitutionality those cases had <span class="star-pagination">*276</span> identified.<sup>[28]</sup> Moreover, in drafting Title III, the Senate Judiciary Committee did more than merely isolate and exclude from the bill the illegal elements of the police activity involved in those cases. Thus, the Chairman of the Committee, in answer to a colleague's question whether Title III was drafted in conformity with the Fourth Amendment, stated:</p>
<blockquote>"Completely so, let me say to my friend. Completely so, and it is <i>even more restrictive.</i> We have gone to every length which is proper, we think, to protect people's privacy." 114 Cong. Rec. 14470 (1968).</blockquote>
<p>It is of greater importance, however, that although Congress was concerned with the "types of <i>surveillance</i>" involved in our prior cases, none of the congressional references to those cases discussed the type of <i>entry</i> made to effectuate the surveillance. Not a word in any of those pre-1968 opinions, save one, described an illegal entry or even implied that such an entry had occurred. Those opinions instead described situations in which a listening device had been surreptitiously placed: against an office wall in order to hear conversations in the next office, <i>Goldman</i> v. <i>United States,</i> <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">316 U. S. 129</a></span>; on the person of a federal agent who recorded a conversation in the defendant's laundry, <i>On Lee</i> v. <i>United States,</i> <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/" aria-description="Citation for case: On Lee v. United States">343 U. S. 747</a></span>; in a cabaret, <i>Lopez</i> v. <i>United States,</i> <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">373 U. S. 427</a></span>; in a law office, <i>Osborn</i> v. <i>United States,</i> <span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/" aria-description="Citation for case: Osborn v. United States">385 U. S. 323</a></span>; against a spike inserted under a party wall, <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span>; on the outside of a public telephone booth, <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span>; and inside a private office, <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span>. It is, of course, true that the conduct in each cited case was surreptitious, but there is a vast difference between detective work that is merely clandestine and work that involves breaking and entering into private property. Before the decisions in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> and <i><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span>,</i> the former technique was considered to be lawful, warrant or <span class="star-pagination">*277</span> no warrant,<sup>[29]</sup> whereas the latter was considered unlawful.<sup>[30]</sup> The fact that Congress was prepared to enact a statute authorizing practices previously thought to be lawful surely does not justify the conclusion that it was equally prepared to authorize conduct that had always been made unlawful by the criminal laws of the various States.</p>
<p><i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">347 U. S. 128</a></span>, was the only pre-1968 case in which this Court had actually confronted the implantation of an electronic listening device by way of a "trespass, and probably a burglary, for which any unofficial person should be, and probably would be, severely punished." <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#132" aria-description="Citation for case: Irvine v. California"><i>Id.,</i> at 132</a></span>.<sup>[31]</sup> The plurality of four, speaking through Mr. Justice Jackson, had this to say about the police conduct in that case:</p>
<blockquote>"That officers of the law would break and enter a home, secrete such a device even in a bedroom, and listen to the conversations of the occupants for over a month would be incredible if it were not admitted. Few police measures have come to our attention that more flagrantly, deliberately, and persistently violated the fundamental <span class="star-pagination">*278</span> principle declared by the Fourth Amendment . . . ." <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Ibid.</a></span></i>
</blockquote>
<p>No Member of the Court disagreed with this assessment, although a majority refused to overturn the conviction because the exclusionary rule did not then apply to the States. While it is true, as the Court points out, <i>ante,</i> at 247, that four Members of the <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Irvine</a></span></i> Court adverted to the lack of a "search warrant or other process" to support the entry, <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#132" aria-description="Citation for case: Irvine v. California">347 U. S., at 132</a></span> (while the other three Members who discussed the issue found the police activity "offensive" and "revolting" without relying on the lack of a warrant<sup>[32]</sup>), it is also true that no Justice condoned a break-in absent some court order explicitly contemplating physical entry on the premises. Under any reading of the case, it cannot be taken as condoning official trespass and burglary absent specific authorization.</p>
<p>More importantly, the fact that Congress cited <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Irvine</a></span>,</i> without comment or explanation, when it was considering Title III cannot fairly be interpreted as an endorsement of the questionable police behavior that had been condemned so thunderously by Mr. Justice Jackson 14 years earlier. My respect for the lawmaking process forecloses the inference that Congress authorized burglarious conduct by such stealthy legislative history.</p>
<p></p>
<h2>IV</h2>
<p>Because it is not supported by either the text of the statute or the scraps of relevant legislative history,<sup>[33]</sup> I fear that the <span class="star-pagination">*279</span> Court's holding may reflect an unarticulated presumption that national police officers have the power to carry out a surveillance order by whatever means may be necessary unless explicitly prohibited by the statute or by the Constitution.</p>
<p>But surely the presumption should run the other way. Congressional silence should not be construed to authorize the Executive to violate state criminal laws or to encroach upon constitutionally protected privacy interests. Before confronting the serious constitutional issues raised by the Court's reading of Title III,<sup>[34]</sup> we should insist upon an unambiguous statement by Congress that this sort of police conduct may be authorized by a court and that a specific showing of necessity, or at least probable cause, must precede such an authorization. Without a legislative mandate that is both explicit and specific, I would presume that this flagrant invasion of the citizen's privacy is prohibited. Cf. <i>United States</i> v. <i>New York Telephone Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/#178" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S., at 178-179</a></span> (STEVENS, J., dissenting <span class="star-pagination">*280</span> in part); <i>United States</i> v. <i>Ramsey,</i> <span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#632" aria-description="Citation for case: United States v. Ramsey">431 U. S., at 632</a></span> (STEVENS, J., dissenting).<sup>[35]</sup></p>
<p>I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[1]  All types of electronic surveillance have the same purpose and effect: the secret interception of communications. As the Court set forth in <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#45" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 45-47</a></span> (1967), however, this surveillance is performed in two quite different ways. Some surveillance is performed by "wiretapping," which is confined to the interception of communication by telephone and telegraph and generally may be performed from outside the premises to be monitored. For a detailed description, see Note, Minimization of Wire Interception: Presearch Guidelines and Postsearch Remedies, <span class="citation no-link">26 Stan. L. Rev. 1411</span>, 1414 n. 18 (1974). At issue in the present case is the form of surveillance commonly known as "bugging," which includes the interception of all oral communication in a given location. Unlike wiretapping, this interception typically is accomplished by installation of a small microphone in the room to be bugged and transmission to some nearby receiver. See McNamara, The Problem of Surreptitious Entry to Effectuate Electronic Eavesdrops: How Do You Proceed After the Court Says "Yes"?, <span class="citation no-link">15 Am. Crim. L. Rev. 1</span>, 2 (1977); Blakey, Aspects of the Evidence Gathering Process in Organized Crime Cases: A Preliminary Analysis, reprinted in the President's Commission on Law Enforcement and Administration of Justice, Task Force Report: Organized Crime, App. C, 92, 97 (1967). Both wiretapping and bugging are regulated under Title III. See <span class="citation no-link">18 U. S. C. §§ 2510</span> (1) and (2).</p>
<p>[2]  Every electronic surveillance necessarily is "covert" in the sense that it must be "hidden; secret; disguised" to be effective. Webster's New International Dictionary 613 (2d ed. 1953). As used here, "covert entry" refers to the physical entry by a law enforcement officer into private premises without the owner's permission or knowledge in order to install bugging equipment. Generally, such an entry will require a breaking and entering. See discussion <i>infra,</i> at 253-254.</p>
<p>[3]  The Federal Courts of Appeals have given conflicting answers to these questions. See <i>United States</i> v. <i>Finazzo,</i> <span class="citation" data-id="9465129"><a href="/opinion/359662/united-states-v-salvatore-finazzo-dominic-j-licavoli/" aria-description="Citation for case: United States v. Salvatore Finazzo, Dominic J. Licavoli">583 F. 2d 837</a></span> (CA6 1978); <i>United States</i> v. <i>Santora,</i> <span class="citation" data-id="359575"><a href="/opinion/359575/united-states-v-ronald-santora-earl-rardin-maurice-eugene-lickteig/" aria-description="Citation for case: United States v. Ronald Santora, Earl Rardin, Maurice...">583 F. 2d 453</a></span> (CA9 1978); <i>United States</i> v. <i>Scafidi,</i> <span class="citation" data-id="8903769"><a href="/opinion/8915597/united-states-v-scafidi/" aria-description="Citation for case: United States v. Scafidi">564 F. 2d 633</a></span> (CA2 1977), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./436/903/">436 U. S. 903</a></span> (1978); <i>United States</i> v. <i>Ford,</i> 180 U. S. App. D. C. 1, <span class="citation multiple-matches"><a href="/c/F.%202d/553/146/">553 F. 2d 146</a></span> (1977); <i>United States</i> v. <i>Agrusa,</i> <span class="citation" data-id="9463064"><a href="/opinion/339006/united-states-v-salvatore-ross-agrusa/" aria-description="Citation for case: United States v. Salvatore Ross Agrusa">541 F. 2d 690</a></span> (CA8 1976), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./429/1045/">429 U. S. 1045</a></span> (1977).</p>
<p>[4]  In relevant part, the Title III order of April 5 provided:
</p>
<p>"[T]he Court finds:</p>
<p>"(a) There is probable cause to believe that Larry Dalia and others as yet unknown, have committed and are committing offenses involving theft from interstate shipments, in violation of Title <span class="citation no-link">18, United States Code, Section 659</span>; sale or receipt of stolen goods, in violation of Title <span class="citation no-link">18, United States Code, Section 2315</span>; and interference with commerce by threats or violence, in violation of Title <span class="citation no-link">18, United States Code, Section 1951</span>; and are conspiring to commit such offenses in violation of Section 371 of Title 18, United States Code.</p>
<p>"(b) There is probable cause to believe that particular wire and oral communications concerning these offenses will be obtained through these interceptions, authorization for which is herewith applied. In particular, these wire and oral communications will concern the theft or robbery of goods moving in interstate commerce, and the transportation, sale, receipt, storage, or distribution of these stolen goods, and the participants in the commission of said offenses.</p>
<p>"(c) Normal investigative procedures reasonably appear to be unlikely to succeed and are too dangerous to be used.</p>
<p>.....</p>
<p>"(e) There is probable cause to believe that the business office of Larry Dalia, consisting of an enclosed room, approximately fifteen (15) by eighteen (18) feet in dimension, and situated in the northwesterly corner of a one-story building housing Wrap-O-Matic Machinery Company, Ltd., and Precise Packaging, and located at 1105 West St. George Avenue, Linden, New Jersey, has been used, and is being used by Larry Dalia and others as yet unknown in connection with the commission of the above-described offenses.</p>
<p>"WHEREFORE, it is hereby ordered that:</p>
<p>"Special Agents of the Federal Bureau of Investigation, United States Department of Justice, are authorized . . . to:</p>
<p>.....</p>
<p>"(b) Intercept oral communications of Larry Dalia, and others as yet unknown, concerning the above-described offenses at the business office of Larry Dalia, consisting of an enclosed room, approximately fifteen (15) by eighteen (18) feet in dimension, and situated in the northwesterly corner of a one-story building housing Wrap-O-Matic Machinery Company, Ltd., and Precise Packaging, and located at 1105 West St. George Avenue, Linden, New Jersey.</p>
<p>"(c) Such interceptions shall not automatically terminate when the type of communication described above in paragraphs (a) and (b) have first been obtained, but shall continue until communications are intercepted which reveal the manner in which Larry Dalia and others as yet unknown participate in theft from interstate shipments; sale or receipt of stolen goods; and interference with commerce by threats or violence; and which reveal the identities of his confederates, their places of operation, and the nature of the conspiracy involved therein, or for a period of twenty (20) days from the date of this Order, whichever is earlier.</p>
<p>.....</p>
<p>"PROVIDING THAT, this authorization to intercept oral and wire communications shall be executed as soon as practicable after signing of this Order and shall be conducted in such a way as to minimize the interception of communications not otherwise subject to interception under Chapter 119 of Title 18 of the United States Code, and must terminate upon attainment of the authorized objective, [or] in any event, at the end of twenty (20) days from the date of this Order.</p>
<p>"PROVIDING ALSO, that Special Attorney James M. Deichert shall provide the Court with a report on the fifth, tenth, and fifteenth day following the date of this Order showing what progress has been made toward achievement of the authorized objective and the need for continued interception."</p>
<p>[5]  Count one charged petitioner and others with conspiring to transport, receive, and possess stolen goods in violation of <span class="citation no-link">18 U. S. C. §§ 2</span>, 2314, 2115, and 659. Count two charged petitioner and others with conspiring to obstruct interstate commerce in violation of <span class="citation no-link">18 U. S. C. § 1951</span> (b) (1). Count three charged that petitioner had transported stolen goods; count four charged that he had received stolen goods; and count five charged petitioner with possession of stolen goods.</p>
<p>[6]  Petitioner was convicted of receiving stolen goods and conspiring to transport, receive, and possess stolen goods. See n. 5, <i>supra.</i></p>
<p>[7]  One authority has said that the constitutional validity of covert entries to install bugs "is plainly the consequence of [the] reasoning" of <i>Katz</i> v. <i>United States</i><i>.</i> T. Taylor, Two Studies in Constitutional Interpretation 114 (1969).</p>
<p>[8]  Petitioner argues that, even if a covert entry would be constitutional in some cases, it was not in the present case, as there was no need for such entry. The District Court, however, specifically found that the "safest and most successful method of accomplishing the installation of the wiretapping device was through breaking and entering [the office]." <span class="citation" data-id="1595144"><a href="/opinion/1595144/united-states-v-dalia/#866" aria-description="Citation for case: United States v. Dalia">426 F. Supp. 862, 866</a></span> (1977). Moreover, in issuing the Title III order, the court found that "[n]ormal investigative procedures reasonably appear to be unlikely to succeed and are too dangerous to be used." App. 7a. And in his opinion denying petitioner's subsequent suppression motion, the same judge stated:
</p>
<p>"The affidavits which supported the application for the warrant in question indicated that resort to electronic surveillance, to overhear meetings at Dalia's office and conversations on Dalia's telephones, was required to identify the sources of Dalia's stolen goods, those working with him to transport and store stolen property, and the scope of the conspiracy. Oral evidence of this criminal enterprise was only available inside Dalia's business premises." <span class="citation" data-id="1595144"><a href="/opinion/1595144/united-states-v-dalia/#866" aria-description="Citation for case: United States v. Dalia">426 F. Supp., at 866</a></span>.</p>
<p>The District Court, therefore, concluded that the circumstances required the approach used by the officers, and nothing in the record brings this conclusion into question.</p>
<p>[9]  It is clear that Title III serves a substantial public interest. See n. 13, <i>infra.</i> Congress and this Court have recognized, however, that electronic surveillance can be a threat to the "cherished privacy of law-abiding citizens" unless it is subjected to the careful supervision prescribed by Title III. See <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#312" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 312</a></span> (1972).</p>
<p>[10]  Congress explicitly confirmed the breadth of the power it had conferred on courts acting under Title III when it amended the Act in 1970. <span class="citation no-link">Pub. L. 91-358, </span>Title II, § 211 (b), <span class="citation no-link">84 Stat. 654</span>. Section 2518 (4) now empowers a court authorizing electronic surveillance to "direct that a . . . landlord, custodian or other person shall furnish the applicant forthwith all information, facilities, and technical assistance necessary to accomplish the interception <i>unobtrusively</i> . . . ." (Emphasis added.) Thus, it appears that Congress anticipated that landlords and custodians may be enlisted to aid law enforcement officials covertly to enter and place the necessary equipment in private areas.</p>
<p>[11]  The only limitation Title III places on the manner in which these court orders are to be executed is in its requirements that no order extend beyond 30 days, and that every order must include provisions that it is to be executed as soon as practicable and in a manner that will minimize the interception of communications not within the purview of the order. See <span class="citation no-link">18 U. S. C. § 2518</span> (5).</p>
<p>[12]  Indeed, the nature of electronic surveillance involved in <i>Berger</i> v. <i><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">New York</a></span></i> was mentioned on the floor of the Senate, when Senator Long observed that under the New York law, police could "obtain judicial warrants authorizing them to hide bugs in the premises of criminal suspects." 114 Cong. Rec. 14708 (1968). To be sure, in his comments Senator Long did not explicitly suggest that Title III would authorize such covert entries. See <i>post,</i> at 272. His statement confirmed, however, what had been strongly indicated prior to the bill's consideration by the full Congress: Members of Congress simply saw no distinction between electronic surveillance which required covert entry and that which required covert tapping of one's telephone. The invasion of the privacy of conversation is the same in both situations.</p>
<p>[13]  Title <span class="citation no-link">18 U. S. C. § 2516</span> specifies that authorization for electronic surveillance may be sought only with respect to certain enumerated crimes. These include espionage, sabotage, treason, kidnaping, robbery, extortion, murder, various corrupt practices, and counterfeiting. According to the Senate Report concerning Title III, "[e]ach offense has been chosen either because it is intrinsically serious or because it is characteristic of the operations of organized crime." S. Rep. No. 1097, 90th Cong., 2d Sess., 97 (1968). The need for use of electronic surveillance against organized crime had been thoroughly considered and documented, shortly before Congress began considering Title III, by a special organized-crime Task Force of a Presidential Commission charged with considering crime in the United States. The President's Commission on Law Enforcement and Administration of Justice, Task Force Report: Organized Crime 91-104 (1967); see <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S., at 310</a></span> n. 9. A summary of the Task Force's conclusions appeared in the Commission's report, which was repeatedly referred to during consideration of Title III. See The President's Commission on Law Enforcement and Administration of Justice, The Challenge of Crime in a Free Society 200-203 (1967). In Congress, proponents of Title III, after hearing numerous witnesses testify concerning the importance of electronic surveillance in fighting organized crime, recommended the bill to their colleagues as "[l]egislation meeting the constitutional standards set out in [Supreme Court] decisions, and granting law enforcement officers the authority to tap telephone wires and install electronic surveillance devices in the investigation of major crimes." S. Rep. No. 1097, <i>supra,</i> at 75; see <i>id.,</i> at 74. Indeed, the Senate Report on Title III unequivocally stated that "[t]he major purpose of title III is to combat organized crime." <i>Id.,</i> at 70. The rapid developments in technology available to the criminal underworld make it all the more imperative that the Government not "deny to itself the prudent and lawful employment of those very techniques which are employed against the Government and its law-abiding citizens." <i>United States</i> v. <i>United States District Court, supra,</i> at 312.</p>
<p>[14]  Although he cites no authority, MR. JUSTICE STEVENS apparently believes that a practicable alternative to covert entry would be installation of bugging devices through subterfuge. See <i>post,</i> at 272. Nowhere in the legislative history of Title III is there any indication that Congress wished to limit its authorization to bugs installed through subterfuge. Moreover, it is difficult to perceive why one means of gaining entry would be less intrusive than another. See, <i>e. g., </i><i>United States</i> v. <i>Ford,</i> <span class="citation" data-id="1442699"><a href="/opinion/1442699/united-states-v-ford/" aria-description="Citation for case: United States v. Ford">414 F. Supp. 879</a></span> (DC 1976), aff'd, 180 U. S. App. D. C. 1, <span class="citation" data-id="344771"><a href="/opinion/344771/united-states-v-carroll-d-ford-united-states-of-america-v-wesley/" aria-description="Citation for case: United States v. Carroll D. Ford. United States of...">553 F. 2d 146</a></span> (1977) (bombscare ruse).</p>
<p>[15]  Those few available devices that intercept conversation from outside of a building in many cases are impractical, either because of cost, reliability, or the configuration of the area being monitored. See U. S. National Commission for Review of Federal and State Laws Relating to Wiretapping and Electronic Surveillance, Commission Studies 168-183 (1976); see, <i>e. g., </i><i>United States</i> v. <i>Ford,</i> <span class="citation" data-id="1442699"><a href="/opinion/1442699/united-states-v-ford/#881" aria-description="Citation for case: United States v. Ford">414 F. Supp., at 881</a></span>.</p>
<p>[16]  As we have concluded that Title III authorizes courts to approve covert entries to install electronic surveillance equipment, we do not consider whether such authority also is conferred by other federal enactments, such as Fed. Rule Crim. Proc. 41 or the All Writs Act, <span class="citation no-link">28 U. S. C. § 1651</span>.</p>
<p>[17]  There is no requirement in Title III that explicit authorization of covert entries be set forth in the court's order. The statutory requirement that the surveillance "should remain under the control and supervision of the authorizing court" <span class="citation no-link">82 Stat. 211</span>, § 801 (d), merely emphasizes that courts acting under <span class="citation no-link">18 U. S. C. § 2518</span> should utilize their power under § 2518 (6) to require periodic progress reports after the installation of the wiretap or bug. If there is a requirement of explicit judicial authorization for covert entry, therefore, it must come from the Fourth Amendment alone.</p>
<p>[18]  Because of the strict requirements of Title III, all of the indicia of a warrant necessarily are present whenever an order under Title III is issued. Accord, <i>United States</i> v. <i>Scafidi,</i> <span class="citation" data-id="8903769"><a href="/opinion/8915597/united-states-v-scafidi/#644" aria-description="Citation for case: United States v. Scafidi">564 F. 2d, at 644</a></span> (Gurfein, J., concurring). Indeed, it was Congress' express design to create under Title III a mechanism by which search warrants valid under the Fourth Amendment would be issued for electronic surveillance. See S. Rep. No. 1097, <i>supra</i> n. 13, at 105; Controlling Crime Through More Effective Law Enforcement: Hearings on S. 300, etc., before the Subcommittee on Criminal Laws and Procedures of the Senate Committee on the Judiciary, 90th Cong., 1st Sess., 176, 570, 919 (1967); Hearings on H. R. 5037, etc., before Subcommittee No. 5 of the House Committee on the Judiciary, 90th Cong., 1st Sess., 917, 934 (1967). No less would be required for the court authorization of electronic surveillance under Title III to be constitutional, as electronic surveillance undeniably is a Fourth Amendment intrusion requiring a warrant. See, <i>e. g., </i><i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 352-353, 356-357</a></span> (1967). And we have explicitly recognized the necessity of a warrant in cases of electronic surveillance. See <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#316" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S., at 316-320</a></span>.</p>
<p>[19]  For example, courts have upheld the use of forceful breaking and entering where necessary to effect a warranted search, even though the warrant gave no indication that force had been contemplated. See, <i>e. g., </i><i>United States</i> v. <i>Gervato,</i> <span class="citation" data-id="308678"><a href="/opinion/308678/united-states-v-frank-gervato/#41" aria-description="Citation for case: United States v. Frank Gervato">474 F. 2d 40, 41</a></span> (CA3), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/864/">414 U. S. 864</a></span> (1973). To be sure, often it is impossible to anticipate when these actions will be necessary. See Note, Covert Entry in Electronic Surveillance: The Fourth Amendment Requirements, 47 Ford. L. Rev. 203, 214 (1978). Nothing in the decisions of this Court, however, indicates that officers requesting a warrant would be constitutionally required to set forth the anticipated means for execution even in those cases where they know beforehand that unannounced or forced entry likely will be necessary. See 2 W. LaFave, Search and Seizure 140 (1978).</p>
<p>[20]  The District Court found that covert entry in the present case was reasonable. The officers entered petitioner's office only twice: once to install the bug and once to remove it. There is no indication that their intrusion went beyond what was necessary to install and remove the equipment. See n. 8, <i>supra.</i></p>
<p>[21]  In the present case, the District Court specifically noted that its order implicitly had authorized covert entry. See <i>supra,</i> at 246. Thus, contrary to the suggestion of the dissent, see <i>post,</i> at 270 n. 20, there is no question in this case "of the <i>Executive's</i> authority to break and enter at will <i>without</i> any judicial authorization."</p>
<p>[22]  Although explicit authorization of the entry is not constitutionally required, we do agree with the Court of Appeals that the "preferable approach" would be for Government agents in the future to make explicit to the authorizing court their expectation that some form of surreptitious entry will be required to carry out the surveillance. Indeed, the Solicitor General has informed us that the Department of Justice has adopted a policy requiring its officers "[to] include [in applications for Title III orders] a request that the order providing for the interception specifically authorize surreptitious entry for the purpose of installing and removing any electronic interception devices to be utilized in accomplishing the oral interception." See Brief for United States 56.</p>
<p>[*]  The Court's reliance upon <i>United States</i> v. <i>Cravero,</i> <span class="citation" data-id="8900306"><a href="/opinion/8912462/united-states-v-cravero/#421" aria-description="Citation for case: United States v. Cravero">545 F. 2d 406, 421</a></span> (CA5 1976) (on petition for rehearing), for the opposite proposition is misplaced. In <i><span class="citation" data-id="8900306"><a href="/opinion/8912462/united-states-v-cravero/" aria-description="Citation for case: United States v. Cravero">Cravero</a></span>,</i> police could not have anticipated the need to arrest the suspect at his home at the time the arrest warrant was issued. It would have been unreasonable, therefore, to require the warrant to specify a home arrest. Here, by contrast, the covert entry was easily foreseeable. There is no reason why the federal agents who secured the warrant could not have advised the judge who issued the warrant that they contemplated covert entry. Indeed, the current Justice Department practice of securing specific prior authorization for covert entries demonstrates the practicability of a constitutional prior-authorization requirement.
</p>
<p><i>United States</i> v. <i>Gervato,</i> <span class="citation" data-id="308678"><a href="/opinion/308678/united-states-v-frank-gervato/#41" aria-description="Citation for case: United States v. Frank Gervato">474 F. 2d 40, 41</a></span> (CA3 1973), is distinguishable for the same reason and also because <i><span class="citation" data-id="308678"><a href="/opinion/308678/united-states-v-frank-gervato/" aria-description="Citation for case: United States v. Frank Gervato">Gervato</a></span></i> involved a mere mode of warrant execution (forcible entry) rather than an invasion of two separate expectations of privacy.</p>
<p>[1]  See <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297</a></span>. The Fourth Amendment provides:
</p>
<p>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</p>
<p>[2]  N. J. Stat. Ann. §§ 2A:94-1, 2A:94-3 (West 1969).</p>
<p>[3]  T. Taylor, Two Studies in Constitutional Interpretation 110 (1969).</p>
<p>[4]  Cf. <i>G. M. Leasing Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#353" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 353</a></span>; <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span>; <i>Colonnade Catering Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#76" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72, 76</a></span>.</p>
<p>[5]  "Beginning with the Act of July 31, 1789, <span class="citation no-link">1 Stat. 29</span>, 43, and concluding with the Omnibus Crime Control and Safe Streets Act of 1968, <span class="citation no-link">82 Stat. 197</span>, 219, 238, Congress has enacted a series of over 35 different statutes granting federal judges the power to issue search warrants of one form or another. These statutes have one characteristic in common: they are specific in their grants of authority and in their inclusion of limitations on either the places to be searched, the objects of the search, or the requirements for the issuance of a warrant." <i>United States</i> v. <i>New York Telephone Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/#179" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S. 159, 179-180</a></span> (STEVENS, J., dissenting in part) (footnote omitted).
</p>
<p>Mr. Justice Frankfurter gathered the pre-1945 statutes in his dissenting opinion in <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/#616" aria-description="Citation for case: Davis v. United States">328 U. S. 582, 616-623</a></span>. He commented that "[w]hat is significant about this legislation is the recognition by Congress of the necessity for specific Congressional authorization even for the search of vessels and other moving vehicles and the seizures of goods technically contraband." <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/#616" aria-description="Citation for case: Davis v. United States"><i>Id.,</i> at 616</a></span>, n.</p>
<p>[6]  I realize that since <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, the Court has applied the same Fourth Amendment principles to state and federal law enforcement officers alike. Nonetheless, I purposely limit my discussion here to the federal context. For purposes of discussing the necessity of statutory authority, it seems useful to me to treat the Fourth Amendment concept of reasonableness as flexible enough to recognize differences between state and federal courts and police forces. Thus, because the power of the Federal Government to combat crime, like the jurisdiction of its courts, is more limited than the comparable power and jurisdiction inhering in the States, it is logical in the federal context to assume that governmental authority is lacking unless expressly mandated by legislation. See, <i>e. g., </i><i>Palmore</i> v. <i>United States,</i> <span class="citation" data-id="9425255"><a href="/opinion/108767/palmore-v-united-states/#396" aria-description="Citation for case: Palmore v. United States">411 U. S. 389, 396</a></span>; <i>Cheng Fan Kwok</i> v. <i>INS,</i> <span class="citation" data-id="9423777"><a href="/opinion/107735/cheng-fan-kwok-v-immigration-naturalization-service/" aria-description="Citation for case: Cheng Fan Kwok v. Immigration &amp; Naturalization Service">392 U. S. 206</a></span>; <i>United States</i> v. <i>Five Gambling Devices,</i> <span class="citation" data-id="9421009"><a href="/opinion/105172/united-states-v-five-gambling-devices/" aria-description="Citation for case: United States v. Five Gambling Devices">346 U. S. 441</a></span>.</p>
<p>[7]  See <i>McCulloch</i> v. <i>Sociedad Nacional de Marineros de Honduras,</i> <span class="citation" data-id="9422521"><a href="/opinion/106525/mcculloch-v-sociedad-nacional-de-marineros-de-honduras/" aria-description="Citation for case: McCulloch v. Sociedad Nacional De Marineros De Honduras">372 U. S. 10</a></span>; <i>Machinists</i> v. <i>Street,</i> <span class="citation" data-id="9422287"><a href="/opinion/106288/international-assn-of-machinists-v-street/" aria-description="Citation for case: International Ass&#x27;n of MacHinists v. Street">367 U. S. 740</a></span>; <i>Hannah</i> v. <i>Larche,</i> <span class="citation" data-id="9422021"><a href="/opinion/106078/hannah-v-larche/#430" aria-description="Citation for case: Hannah v. Larche">363 U. S. 420, 430</a></span>; <i>Murray</i> v. <i>The Charming Betsy,</i> <span class="citation" data-id="84778"><a href="/opinion/84778/murray-v-schooner-charming-betsy/" aria-description="Citation for case: Murray v. Schooner Charming Betsy">2 Cranch 64</a></span>.</p>
<p>[8]  It found authority for those searches in the Postal Service's recent reinterpretation of an awkwardly drawn 1866 statute that authorized certain border searches of "vessels" but that could not reasonably be read to authorize either the mail openings themselves or the regulation allowing them. Moreover, its adoption of that interpretation left it no choice but to resolve a troublesome constitutional question without any considered guidance from Congress. See <span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#625" aria-description="Citation for case: United States v. Ramsey">431 U. S., at 625-632</a></span> (STEVENS, J., dissenting).</p>
<p>[9]  See <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/#178" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S., at 178-190</a></span> (STEVENS, J., dissenting in part).</p>
<p>[10]  Although this case involves an office, the invasion of a home would raise precisely the same statutory issue.</p>
<p>[11]  "Congress drafted [Title III] with exacting precision. As its principal sponsor, Senator McClellan, put it:
</p>
<p>" `[A] bill as controversial as this . . . requires close attention to the dotting of every "i" and the crossing of every "t" . . . .' [114 Cong. Rec. 14751 (1968).]</p>
<p>"Under these circumstances, the exact words of the statute provide the surest guide to determining Congress' intent, and we would do well to confine ourselves to that area." <i>United States</i> v. <i>Donovan,</i> <span class="citation" data-id="9426645"><a href="/opinion/109584/united-states-v-donovan/#441" aria-description="Citation for case: United States v. Donovan">429 U. S. 413, 441</a></span> (BURGER, C. J., concurring in part and dissenting in part).</p>
<p>[12]  See <i>ante,</i> at 249-250; nn. 13-18, <i>infra,</i> and text accompanying.</p>
<p>[13]  As Judge Merritt, writing for the Sixth Circuit, cogently observed:
</p>
<p>"It simply does not make sense to imply Congressional authority for official break-ins when not a single line or word of the statute even mentions the possibility, much less limits or defines the scope of the power or describes the circumstances under which such conduct, normally unlawful, may take place. As the dissents of Holmes and Brandeis in <i>Olmstead</i> [v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span>] suggest, this is a serious, if not a `dirty,' business; and we do not believe we should imply the power to break in under the statute, as the government argues, when Congress has not confronted and debated the issue and expressed such an intention clearly.</p>
<p>.....</p>
<p>"In some circumstances, the installation of an electronic bug may not be possible without a forcible breaking and entering of the suspect's premises, but that does not imply that the power to break and enter is subsumed in the warrant to seize the words. The breaking and entering aggravates the search, and it intrudes upon property and privacy interests not weighed in the statutory scheme, interests which have independent social value unrelated to confidential speech. We are not inclined to give the government the right by implication to intrude upon these interests by conducting official break-ins, especially when the purpose is secretly to monitor and record private conversations, a dangerous power otherwise carefully limited and defined by statute." <i>United States</i> v. <i>Finazzo,</i> <span class="citation" data-id="9465129"><a href="/opinion/359662/united-states-v-salvatore-finazzo-dominic-j-licavoli/#841" aria-description="Citation for case: United States v. Salvatore Finazzo, Dominic J. Licavoli">583 F. 2d 837, 841-842</a></span> (CA6 1978). See also <i>United States</i> v. <i>Santora,</i> <span class="citation" data-id="359575"><a href="/opinion/359575/united-states-v-ronald-santora-earl-rardin-maurice-eugene-lickteig/#456" aria-description="Citation for case: United States v. Ronald Santora, Earl Rardin, Maurice...">583 F. 2d 453, 456-466</a></span> (CA9 1978).</p>
<p>[14]  <span class="citation no-link">18 U. S. C. § 2516</span> (1).</p>
<p>[15]  <span class="citation no-link">18 U. S. C. §§ 2516</span> (1) (a)-(g).</p>
<p>[16]  "Each application for an order authorizing or approving the interception of a wire or oral communication shall be made in writing upon oath or affirmation to a judge of competent jurisdiction and shall state the applicant's authority to make such application. Each application shall include the following information:
</p>
<p>"(a) the identity of the investigative or law enforcement officer making the application, and the officer authorizing the application;</p>
<p>"(b) a full and complete statement of the facts and circumstances relied upon by the applicant, to justify his belief that an order should be issued, including (i) details as to the particular offense that has been, is being, or is about to be committed, (ii) a particular description of the nature and location of the facilities from which or the place where the communication is to be intercepted, (iii) a particular description of the type of communications sought to be intercepted, (iv) the identity of the person, if known, committing the offense and whose communications are to be intercepted;</p>
<p>"(c) a full and complete statement as to whether or not other investigative procedures have been tried and failed or why they reasonably appear to be unlikely to succeed if tried or to be too dangerous;</p>
<p>"(d) a statement of the period of time for which the interception is required to be maintained. If the nature of the investigation is such that the authorization for interception should not automatically terminate when the described type of communication has been first obtained, a particular description of facts establishing probable cause to believe that additional communications of the same type will occur thereafter;</p>
<p>"(e) a full and complete statement of the facts concerning all previous applications known to the individual authorizing and making the application, made to any judge for authorization to intercept, or for approval of interceptions of, wire or oral communications involving any of the same persons, facilities or places specified in the application, and the action taken by the judge on each such application; and</p>
<p>"(f) where the application is for the extension of an order, a statement setting forth the results thus far obtained from the interception, or a reasonable explanation of the failure to obtain such results." <span class="citation no-link">18 U. S. C. § 2518</span> (1).</p>
<p>[17]  "(3) Upon such application the judge may enter an ex parte order, as requested or as modified, authorizing or approving interception of wire or oral communications within the territorial jurisdiction of the court in which the judge is sitting, if the judge determines on the basis of the facts submitted by the applicant that
</p>
<p>"(a) there is probable cause for belief that an individual is committing, has committed, or is about to commit a particular offense enumerated in section 2516 of this chapter;</p>
<p>"(b) there is probable cause for belief that particular communications concerning that offense will be obtained through such interception;</p>
<p>"(c) normal investigative procedures have been tried and have failed or reasonably appear to be unlikely to succeed if tried or to be too dangerous;</p>
<p>"(d) there is probable cause for belief that the facilities from which, or the place where, the wire or oral communications are to be intercepted are being used, or are about to be used, in connection with the commission of such offense, or are leased to, listed in the name of, or commonly used by such person.</p>
<p>"(4) Each order authorizing or approving the interception of any wire or oral communication shall specify</p>
<p>"(a) the identity of the person, if known, whose communications are to be intercepted;</p>
<p>"(b) the nature and location of the communications facilities as to which, or the place where, authority to intercept is granted;</p>
<p>"(c) a particular description of the type of communication sought to be intercepted, and a statement of the particular offense to which it relates;</p>
<p>"(d) the identity of the agency authorized to intercept the communications, and of the person authorizing the application; and</p>
<p>"(e) the period of time during which such interception is authorized, including a statement as to whether or not the interception shall automatically terminate when the described communication has been first obtained. . . ." <span class="citation no-link">18 U. S. C. §§ 2518</span> (3), (4).</p>
<p>[18]  "No order entered under this section may authorize or approve the interception of any wire or oral communication for any period longer than is necessary to achieve the objective of the authorization, nor in any event longer than thirty days. Extensions of an order may be granted, but only upon application for an extension made in accordance with subsection (1) of this section and the court making the findings required by subsection (3) of this section. The period of extension shall be no longer than the authorizing judge deems necessary to achieve the purposes for which it was granted and in no event for longer than thirty days. Every order and extension thereof shall contain a provision that the authorization to intercept shall be executed as soon as practicable, shall be conducted in such a way as to minimize the interception of communications not otherwise subject to interception under this chapter, and must terminate upon attainment of the authorized objective, or in any event in thirty days." <span class="citation no-link">18 U. S. C. § 2518</span> (5).
</p>
<p>The statute also details procedures for the storage and protective custody of the resulting tapes, <span class="citation no-link">18 U. S. C. §§ 2518</span> (8) (a)-(c), for authorized disclosures and uses of the tapes both in and out of court, <span class="citation no-link">18 U. S. C. §§ 2517</span>, 2518 (9), and for after-the-fact notice to persons whose conversations were overheard. <span class="citation no-link">18 U. S. C. § 2518</span> (8) (d).</p>
<p>[19]  The following provision was added to Title III in 1970:
</p>
<p>"An order authorizing the interception of a wire or oral communication shall, upon request of the applicant, direct that a communication common carrier, landlord, custodian or other person shall furnish the applicant forthwith all information, facilities, and technical assistance necessary to accomplish the interception unobtrusively and with a minimum of interference with the services that such carrier, landlord, custodian, or person is according the person whose communications are to be intercepted. Any communication common carrier, landlord, custodian or other person furnishing such facilities or technical assistance shall be compensated therefor by the applicant at the prevailing rates." <span class="citation no-link">18 U. S. C. § 2518</span> (4).</p>
<p>[20]  The Court analyzes this problem as simply one of <i>Judicial</i> authority under the statute. <i>Ante,</i> at 250, and n. 10. Even if I could agree that Title III afforded judges "broad" and unconfined authority with respect to break-ins, I would still be left with the problem, never mentioned by the Court, of the <i>Executive's</i> authority to break and enter at will <i>without</i> any judicial authorization.
</p>
<p>Indeed, I am not at all certain that the Court puts any confines on either Judicial or Executive authority in this area, despite the lip service it pays to "constitutional limitations." For, having stated that "breaking and entering" in execution of a search warrant is constitutionally permissible "where such entry is the <i>only</i> means by which the warrant effectively may be executed," <i>ante,</i> at 247 (emphasis added), the Court then equates a surveillance order with a search warrant, but see Taylor, <i>supra</i> n. 3, at 84-85, and allows a break-in under the former upon a showing merely that the break-in was "the safest and most successful," rather than the "only," method of installing the device. <span class="citation" data-id="1595144"><a href="/opinion/1595144/united-states-v-dalia/#866" aria-description="Citation for case: United States v. Dalia">426 F. Supp. 862, 866</a></span>.</p>
<p>[21]  A Congress that was careful to limit the temporal extent of electronic surveillance and the opportunity for it to infringe on protected (<i>i. e.,</i> noncriminal) conversations, and one so quick to amend the statute to provide for "unobtrusive" entry through the aid of private persons (<i>i. e.,</i> "custodians" and "landlords") who already have a degree of access to the property, surely cannot have condoned unlimited and unauthorized breaking and entering by police officers with the aid of nothing but a burglar's tools.</p>
<p>[22]  In full, the paragraph excerpted by the Court is as follows:
</p>
<p>"In Berger against the State of New York, decided on June 12, 1967, the majority of the Court, speaking through Mr. Justice Clark, threw out the New York State court-approved eavesdropping statute, declaring it to be unconstitutional. The New York statute permitted the police to obtain judicial warrants authorizing them to hide bugs in the premises of criminal suspects. The Court's majority opinion outlawed this bugging statute because, it said, the procedures did not contain specific safeguards against violations of the fourth amendment, which limited police searches." 114 Cong. Rec. 14708 (1968) (Sen. Long of Missouri).</p>
<p>[23]  See also Anti-Crime Programs: Hearings on H. R. 5037, etc., before Subcommittee No. 5 of the House Committee on the Judiciary, 90th Cong., 1st Sess., 1031 (1967), cited <i>ante,</i> at 251.</p>
<p>[24]  "[Title III] sets forth in the most elaborate and precise detail the safeguards surrounding the application to a court of competent jurisdiction for authority to make a wiretap. I am satisfied that it is fully designed to guard against any unwarranted invasion of the precious right of privacy." 114 Cong. Rec. 16296 (1968) (Rep. MacGregor). See also <i>id.,</i> at 14763 (Sen. Percy); <i>id.,</i> at 16296 (Rep. Boland); S. Rep. No. 1097, 90th Cong., 2d Sess., 66 (1968).
</p>
<p>On at least two occasions the Court has commented on the circumspection with which Title III was drafted:</p>
<p>"[Title III] sets forth the detailed and particularized application necessary to obtain such an order as well as the <i>carefully circumscribed conditions for its use.</i> The Act represents a comprehensive attempt by Congress to promote more effective control of crime while protecting the privacy of individual thought and expression." <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#302" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S., at 302</a></span> (emphasis added). See also <i>Gelbard</i> v. <i>United States,</i> <span class="citation" data-id="9424980"><a href="/opinion/108596/gelbard-v-united-states/#48" aria-description="Citation for case: Gelbard v. United States">408 U. S. 41, 48</a></span>. See also n. 8, <i>supra.</i></p>
<p>[25]  Had Congress expressly considered the issue, I am confident that it would not have granted the Executive the broad authority to break and enter that is conferred by the Court in today's decision. Illustrative of its probable reaction to such investigative techniques are the responses of some Members to the officially sanctioned break-in committed against the office of Daniel Ellsberg's psychiatrist, and to the possibility of official participation in the Watergate break-in <i>E. g.,</i> 119 Cong. Rec. 14607-14608 (1973) (Sen. Edwards); <i>id.,</i> at 15332 (Rep. Sarasin).</p>
<p>[26]  The dimensions of the constitutional protection of privacy were certainly not underestimated by the supporters of Title III. Senator Lausche, for example, had this to say about the intent of the Framers of the Fourth Amendment:
</p>
<p>"[T]hey also knew that the innocent individual would be protected in his home; that no one shall enter. Even though it is a hovel, to him it is a palace. So they wrote into the Constitution, regardless of how poor one's home may be, that it shall not be entered by the government without the law-enforcement official having first obtained a warrant for search and seizure issued on the basis of evidence establishing probable cause." 114 Cong. Rec. 14729 (1968).</p>
<p>[27]  <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span>; <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span>. See also <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span>; <i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">347 U. S. 128</a></span>.</p>
<p>[28]  See S. Rep. No. 1097, <i>supra,</i> at 66, 75, 101.</p>
<p>[29]  <i>E. g., </i><i>On Lee</i> v. <i>United States,</i> <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/" aria-description="Citation for case: On Lee v. United States">343 U. S. 747</a></span>; <i>Goldman</i> v. <i>United States,</i> <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">316 U. S. 129</a></span>; <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span>.</p>
<p>[30]  <i>E. g., </i><i>Silverman</i> v. <i>United States, supra</i><i>; </i><i>Irvine</i> v. <i>California, supra</i><i>.</i></p>
<p>[31]  Mr. Justice Jackson described the entry as follows:
</p>
<p>"On December 1, 1951, while Irvine and his wife were absent from their home, an officer arranged to have a locksmith go there and make a door key. Two days later, again in the absence of occupants, officers and a technician made entry into the home by the use of this key and installed a concealed microphone in the hall. A hole was bored in the roof of the house and wires were strung to transmit to a neighboring garage whatever sounds the microphone might pick up. Officers were posted in the garage to listen. On December 8, police again made surreptitious entry and moved the microphone, this time hiding it in the bedroom. Twenty days later, they again entered and placed the microphone in a closet, where the device remained until its purpose of enabling the officers to overhear incriminating statements was accomplished." <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#130" aria-description="Citation for case: Irvine v. California">347 U. S., at 130-131</a></span>.</p>
<p>[32]  <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#145" aria-description="Citation for case: Irvine v. California"><i>Id.,</i> at 145</a></span> (Frankfurter, J., dissenting, joined by Burton, J.); <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#150" aria-description="Citation for case: Irvine v. California"><i>id.,</i> at 150</a></span> (Douglas, J., dissenting).</p>
<p>[33]  The Court argues that Congress' goals in enacting the statute would be frustrated if Title III were not read to include the authority exercised by the Government in this case. <i>Ante,</i> at 252-254. Of course, if Congress intended to sanction "even the most reprehensible means for securing a conviction," <i>Irvine,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#146" aria-description="Citation for case: Irvine v. California">347 U. S., at 146</a></span> (Frankfurter, J., dissenting), then withholding some of those means would indeed frustrate the legislative purpose. But there is no reason to impute such an intent to Congress or to ignore its conscientious attention to the importance of safeguarding the rights of individual privacy. See 114 Cong. Rec. 14469-14470 (1968) (Sen. McClellan); see <i>supra,</i> at 272-273, 276.
</p>
<p>Congress quite clearly expected exterior <i>wiretaps</i> to provide the most effective means of electronic surveillance authorized by Title III. The unavailability of certain interior <i>"bugs"</i><i>i. e.,</i> those implanted by means of forcible trespasscan hardly be seen as frustrating the entire law enforcement scheme. <i>E. g.,</i> S. Rep. No. 1097, supra n. 24, at 72; 114 Cong. Rec. 12988 (1968) (Sen. Tydings); <i>id.,</i> at 13206 (Sen. Scott); <i>id.,</i> at 14481 (Sen. McClellan); <i>id.,</i> at 14714 (Sen. Murphy).</p>
<p>Congress' prediction proved correct:</p>
<p>"Telephone taps apparently account for most instances of electronic surveillance, and this can be accomplished in most circumstances by placing a tap on the line outside the premises of the suspect. According to the final report of the National Commission for Review of Federal and State Laws Relating to Wiretapping and Electronic Surveillance, only 26 out of some 1,220 electronic surveillance orders executed between 1968 and 1973 involved a trespassory intrusion. <i>National Wiretap Commission, Electronic Surveillance</i> 15 (1967) . . . ." <i>United States</i> v. <i>Finazzo,</i> <span class="citation" data-id="9465129"><a href="/opinion/359662/united-states-v-salvatore-finazzo-dominic-j-licavoli/" aria-description="Citation for case: United States v. Salvatore Finazzo, Dominic J. Licavoli">583 F. 2d, at 841</a></span> n. 13.</p>
<p>[34] 

[...TRUNCATED 1376 of 121376 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Davis v. Mississippi.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Davis v. Mississippi"
type: case
citation: "394 U.S. 721 (1969)"
parallel_cite: "89 S. Ct. 1394; 22 L. Ed. 2d 676"
neutral_cite: 1969 U.S. LEXIS 1869
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1969
date_decided: 1969-04-23
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1969-04-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Davis v. Mississippi
  varies_by_point: false
  scope_note: "Good law; dragnet station-house detention for fingerprinting without probable cause or judicial authorization is unreasonable. The Court reserved whether a narrowly circumscribed fingerprinting procedure on less than probable cause might be permissible — a question revisited in Hayes v. Florida."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107912/davis-v-mississippi/"
  cluster_id: 107912
  opinion_id: 107912
  identity_checked: true
homes:
  - page: "[[Seizure of the Person]]"
    role: "Limiting"
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Related (cross-doctrine)"
related: ["[[Hayes v. Florida]]", "[[Terry v. Ohio]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure", "fingerprinting", "investigative-detention", "dragnet"]
holding: "Detaining and transporting a suspect to the station for fingerprinting without probable cause or judicial authorization is an unreasonable seizure; the fingerprints are suppressible."
lake:
  record_id: Davis v. Mississippi
  status: verified
  projected_at: 2026-07-09
---

# Davis v. Mississippi

*394 U.S. 721 (1969)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating a rape in which the only leads were the victim's general description and a set of fingerprints, police rounded up and questioned at least two dozen young Black men, taking many to headquarters for fingerprinting without warrants or probable cause. Davis was among those detained; his prints, taken during a station-house detention, matched those at the scene and were used to convict him. He moved to suppress the fingerprint evidence as the fruit of an unlawful detention.

## Issue
Whether fingerprints obtained during an investigative detention undertaken without probable cause or judicial authorization must be excluded as the product of an unreasonable Fourth Amendment seizure.

## Rule
Investigative seizures are subject to the Fourth Amendment regardless of the label: "Nothing is more clear than that the Fourth Amendment was meant to prevent wholesale intrusions upon the personal security of our citizenry, whether these intrusions be termed 'arrests' or 'investigatory detentions.'" — 394 U.S. at 726–727. ^pin-726

That protection reaches detentions for fingerprinting: "Detentions for the sole purpose of obtaining fingerprints are no less subject to the constraints of the Fourth Amendment." — [*Id.* at 727](https://www.courtlistener.com/opinion/107912/davis-v-mississippi/#:~:text=Detentions%20for%20the%20sole%20purpose). ^pin-727

## Application
Davis was seized in a dragnet — taken to police headquarters and fingerprinted without probable cause to arrest, without a warrant, and without any judicial authorization for the detention. Because that station-house detention was an unreasonable seizure, the fingerprints obtained during it were its fruit and had to be suppressed. The Court added a caveat: because fingerprinting is a brief, reliable, non-coercive process, a narrowly circumscribed procedure conducted under judicial authorization might in some future case satisfy the Fourth Amendment even on less than probable cause — but no such procedure was used here.

## Conclusion
The dragnet fingerprinting detention was unreasonable and the fingerprints were inadmissible; the conviction was reversed. *Davis* establishes that investigatory detentions, including for fingerprinting, are full Fourth Amendment seizures requiring justification.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Reaffirmed and extended in [[Hayes v. Florida]] (transporting a suspect to the station for fingerprinting without probable cause is an arrest), which also developed the reserved question of brief field fingerprinting on reasonable suspicion; consistent with the seizure framework of [[Terry v. Ohio]].

## Appears on
- [[Seizure of the Person]] — *Limiting*
- [[Terry Stops and Reasonable Suspicion]] — *Related (cross-doctrine)*

## Sources
- *Davis v. Mississippi*, 394 U.S. 721 (1969) — https://www.courtlistener.com/opinion/107912/davis-v-mississippi/ — pinpoints: 726–727.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "643aeca1ecd3ef3b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Davis v. Mississippi"}, "payload": {"all": [{"cite": "394 U.S. 721", "page": "721", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "394"}, {"cite": "89 S. Ct. 1394", "page": "1394", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "89"}, {"cite": "22 L. Ed. 2d 676", "page": "676", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "22"}, {"cite": "1969 U.S. LEXIS 1869", "page": "1869", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1969"}], "display": "394 U.S. 721", "official": {"cite": "394 U.S. 721", "page": "721", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "394"}, "official_selection_present": true, "record_id": "Davis v. Mississippi"}}
{"assertion_id": "90d4ee7c79c90c77", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-727", "record_id": "Davis v. Mississippi"}, "payload": {"fragment": "#:~:text=Detentions%20for%20the%20sole%20purpose", "page": null, "pin_id": "pin-727", "pinpoint_status": "star-verified", "quote": "Detentions for the sole purpose of obtaining fingerprints are no less subject to the constraints of the Fourth Amendment.", "quote_fidelity": "matched", "record_id": "Davis v. Mississippi", "star_marker": "727"}}
{"assertion_id": "e09707cd1e97cac7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-726", "record_id": "Davis v. Mississippi"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-726", "pinpoint_status": "slip-only", "quote": "--- # Davis v. Mississippi *394 U.S. 721 (1969)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigating a rape in which the only leads were the victim's general description and a set of fingerprints, police rounded up and questioned at least two dozen young Black men, taking many to headquarters for fingerprinting without warrants or probable cause. Davis was among those detained; his prints, taken during a station-house detention, matched those at the scene and were used to convict him. He moved to suppress the fingerprint evidence as the fruit of an unlawful detention. ## Issue Whether fingerprints obtained during an investigative detention undertaken without probable cause or judicial authorization must be excluded as the product of an unreasonable Fourth Amendment seizure. ## Rule Investigative seizures are subject to the Fourth Amendment regardless of the label:", "quote_fidelity": "mismatch", "record_id": "Davis v. Mississippi", "star_marker": null}}
{"assertion_id": "8ada5117ad37d467", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Davis v. Mississippi"}, "payload": {"as_of_content": "1969-04-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Davis v. Mississippi", "scope_note": "Good law; dragnet station-house detention for fingerprinting without probable cause or judicial authorization is unreasonable. The Court reserved whether a narrowly circumscribed fingerprinting procedure on less than probable cause might be permissible — a question revisited in Hayes v. Florida.", "varies_by_point": false}}
```

### lake record — Davis v. Mississippi

```json
{
  "schema_version": "s2.v1",
  "record_id": "Davis v. Mississippi",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Davis v. Mississippi",
    "case_name_short": "Davis",
    "case_name_full": "Davis v. Mississippi",
    "input_case_name": "Davis v. Mississippi",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1969-04-23",
    "year": 1969,
    "docket": null,
    "cluster_id": 107912,
    "lead_opinion_id": 107912,
    "sibling_ids": [
      107912,
      9424010,
      9424011,
      9424012,
      9424013
    ],
    "absolute_url": "/opinion/107912/davis-v-mississippi/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8975607,
        "score": 20,
        "case_name": "Davis v. Mississippi"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "394 U.S. 721",
      "volume": "394",
      "reporter": "U.S.",
      "page": "721",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "89 S. Ct. 1394",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "1394",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 676",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "676",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1969 U.S. LEXIS 1869",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "1869",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "394 U.S. 721",
        "volume": "394",
        "reporter": "U.S.",
        "page": "721",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 S. Ct. 1394",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "1394",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 676",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "676",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1969 U.S. LEXIS 1869",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "1869",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "394 U.S. 721",
    "official_selection": {
      "court_class": "scotus",
      "selected": "394 U.S. 721",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-726",
      "page": null,
      "quote": "--- # Davis v. Mississippi *394 U.S. 721 (1969)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigating a rape in which the only leads were the victim's general description and a set of fingerprints, police rounded up and questioned at least two dozen young Black men, taking many to headquarters for fingerprinting without warrants or probable cause. Davis was among those detained; his prints, taken during a station-house detention, matched those at the scene and were used to convict him. He moved to suppress the fingerprint evidence as the fruit of an unlawful detention. ## Issue Whether fingerprints obtained during an investigative detention undertaken without probable cause or judicial authorization must be excluded as the product of an unreasonable Fourth Amendment seizure. ## Rule Investigative seizures are subject to the Fourth Amendment regardless of the label:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-727",
      "page": null,
      "quote": "Detentions for the sole purpose of obtaining fingerprints are no less subject to the constraints of the Fourth Amendment.",
      "star_marker": "727",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 10565,
      "fragment": "#:~:text=Detentions%20for%20the%20sole%20purpose",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1969-04-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Davis v. Mississippi",
    "varies_by_point": false,
    "scope_note": "Good law; dragnet station-house detention for fingerprinting without probable cause or judicial authorization is unreasonable. The Court reserved whether a narrowly circumscribed fingerprinting procedure on less than probable cause might be permissible \u2014 a question revisited in Hayes v. Florida.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Southerland v. City of New York",
          "cluster_id": 8441115,
          "cite": [
            "667 F.3d 87",
            "2012 WL 310836",
            "2011 U.S. App. LEXIS 26144"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Opinion Number",
          "cluster_id": 3463196,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cerrone v. Brown",
          "cluster_id": 7090171,
          "cite": [
            "246 F.3d 194",
            "2001 WL 356717"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Guardiola v. State",
          "cluster_id": 1383318,
          "cite": [
            "20 S.W.3d 216",
            "2000 WL 552189"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Firth",
          "cluster_id": 1997671,
          "cite": [
            "708 A.2d 526",
            "1998 R.I. LEXIS 53",
            "1998 WL 97794"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Donald Johnson v. Bart Ross, Superintendent, Arthur Kill Correctional Facility",
          "cluster_id": 577020,
          "cite": [
            "955 F.2d 178",
            "1992 U.S. App. LEXIS 1068"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Boyle v. State",
          "cluster_id": 1522051,
          "cite": [
            "820 S.W.2d 122",
            "1989 WL 114545"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane1_negative"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cortez",
          "cluster_id": 110377,
          "cite": [
            "66 L. Ed. 2d 621",
            "101 S. Ct. 690",
            "449 U.S. 411",
            "1981 U.S. LEXIS 58",
            "49 U.S.L.W. 4099"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Illinois",
          "cluster_id": 109304,
          "cite": [
            "45 L. Ed. 2d 416",
            "95 S. Ct. 2254",
            "422 U.S. 590",
            "1975 U.S. LEXIS 82"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brignoni-Ponce",
          "cluster_id": 109311,
          "cite": [
            "45 L. Ed. 2d 607",
            "95 S. Ct. 2574",
            "422 U.S. 873",
            "1975 U.S. LEXIS 10"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Browder v. Director, Dept. of Corrections of Ill.",
          "cluster_id": 109761,
          "cite": [
            "54 L. Ed. 2d 521",
            "98 S. Ct. 556",
            "434 U.S. 257",
            "1978 U.S. LEXIS 53"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kolender v. Lawson",
          "cluster_id": 110926,
          "cite": [
            "75 L. Ed. 2d 903",
            "103 S. Ct. 1855",
            "461 U.S. 352",
            "1983 U.S. LEXIS 159",
            "51 U.S.L.W. 4532"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. DeFillippo",
          "cluster_id": 110127,
          "cite": [
            "61 L. Ed. 2d 343",
            "99 S. Ct. 2627",
            "443 U.S. 31",
            "1979 U.S. LEXIS 135"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dionisio",
          "cluster_id": 108709,
          "cite": [
            "35 L. Ed. 2d 67",
            "93 S. Ct. 764",
            "410 U.S. 1",
            "1973 U.S. LEXIS 110"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cantor",
          "cluster_id": 5681132,
          "cite": [
            "36 N.Y.2d 106",
            "324 N.E.2d 872",
            "365 N.Y.S.2d 509",
            "1975 N.Y. LEXIS 3100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. White",
          "cluster_id": 108304,
          "cite": [
            "28 L. Ed. 2d 453",
            "91 S. Ct. 1122",
            "401 U.S. 745",
            "1971 U.S. LEXIS 132"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Crews",
          "cluster_id": 110230,
          "cite": [
            "63 L. Ed. 2d 537",
            "100 S. Ct. 1244",
            "445 U.S. 463",
            "1980 U.S. LEXIS 1293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107912 OR 9424010 OR 9424011 OR 9424012 OR 9424013) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NTM4NzUyMDAwMDAmcz0xNzY3NTQ4JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107912+OR+9424010+OR+9424011+OR+9424012+OR+9424013%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(107912 OR 9424010 OR 9424011 OR 9424012 OR 9424013)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNDImcz0zOTkzMDkmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107912+OR+9424010+OR+9424011+OR+9424012+OR+9424013%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107912 OR 9424010 OR 9424011 OR 9424012 OR 9424013)",
        "reviewed": 6,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 6,
        "triage_read": 0,
        "triage_snippet_classified": 6
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107912 OR 9424010 OR 9424011 OR 9424012 OR 9424013)",
    "indexed_citing_opinions": 898,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107912,
        "count": 852,
        "count_source": "search"
      },
      {
        "opinion_id": 9424010,
        "count": 69,
        "count_source": "search"
      },
      {
        "opinion_id": 9424011,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424012,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424013,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1385,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/davis-v-mississippi.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU3OTcwOTUmcz00NDgyOTUzJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107912+OR+9424010+OR+9424011+OR+9424012+OR+9424013%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107912,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 107800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 107848,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 246966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 250068,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 1722004,
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
    "date_created": "2026-07-05T02:04:14Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:05:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:05:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:15:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:05:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Davis v. Mississippi

```
<div>
<center><b><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U.S. 721</a></span> (1969)</b></center>
<center><h1>DAVIS<br>
v.<br>
MISSISSIPPI.</h1></center>
<center>No. 645.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 26-27, 1969.</center>
<center>Decided April 22, 1969.</center>
CERTIORARI TO THE SUPREME COURT OF MISSISSIPPI.
<p><i>Melvyn Zarr</i> argued the cause for petitioner. With him on the brief were <i>Jack Greenberg, Michael Meltsner, Anthony G. Amsterdam,</i> and <i>Jack Young.</i></p>
<p><span class="star-pagination">*722</span> <i>G. Garland Lyell, Jr.,</i> Assistant Attorney General of Mississippi, argued the cause for respondent. With him on the brief was <i>Joe T. Patterson,</i> Attorney General.</p>
<p>MR. JUSTICE BRENNAN delivered the opinion of the Court.</p>
<p>Petitioner was convicted of rape and sentenced to life imprisonment by a jury in the Circuit Court of Lauderdale County, Mississippi. The only issue before us is whether fingerprints obtained from petitioner should have been excluded from evidence as the product of a detention which was illegal under the Fourth and Fourteenth Amendments.</p>
<p>The rape occurred on the evening of December 2, 1965, at the victim's home in Meridian, Mississippi. The victim could give no better description of her assailant than that he was a Negro youth. Finger and palm prints found on the sill and borders of the window through which the assailant apparently entered the victim's home constituted the only other lead available at the outset of the police investigation. Beginning on December 3, and for a period of about 10 days, the Meridian police, without warrants, took at least 24 Negro youths to police headquarters where they were questioned briefly, fingerprinted, and then released without charge. The police also interrogated 40 or 50 other Negro youths either at police headquarters, at school, or on the street. Petitioner, a 14-year-old youth who had occasionally worked for the victim as a yardboy, was brought in on December 3 and released after being fingerprinted and routinely questioned. Between December 3 and December 7, he was interrogated by the police on several occasions sometimes in his home or in a car, other times at police headquarters. This questioning apparently related primarily to investigation of other potential suspects. Several times during this same period petitioner was exhibited <span class="star-pagination">*723</span> to the victim in her hospital room. A police officer testified that these confrontations were for the purpose of sharpening the victim's description of her assailant by providing "a gauge to go by on size and color." The victim did not identify petitioner as her assailant at any of these confrontations.</p>
<p>On December 12, the police drove petitioner 90 miles to the city of Jackson and confined him overnight in the Jackson jail. The State conceded on oral argument in this Court that there was neither a warrant nor probable cause for this arrest. The next day, petitioner, who had not yet been afforded counsel, took a lie detector test and signed a statement.<sup>[1]</sup> He was then returned to and confined in the Meridian jail. On December 14, while so confined, petitioner was fingerprinted a second time. That same day, these December 14 prints, together with the fingerprints of 23 other Negro youths apparently still under suspicion, were sent to the Federal Bureau of Investigation in Washington, D. C., for comparison with the latent prints taken from the window of the victim's house. The FBI reported that petitioner's prints matched those taken from the window. Petitioner was subsequently indicted and tried for the rape, and the fingerprint evidence was admitted in evidence at trial over petitioner's timely objections that the fingerprints should be excluded as the product of an unlawful detention. The Mississippi Supreme Court sustained the admission of the fingerprint evidence and affirmed the conviction. <span class="citation multiple-matches"><a href="/c/So.%202d/204/270/">204 So. 2d 270</a></span> (1967). We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./393/821/">393 U. S. 821</a></span> (1968). We reverse.</p>
<p>At the outset, we find no merit in the suggestion in the Mississippi Supreme Court's opinion that fingerprint evidence, because of its trustworthiness, is not subject to the proscriptions of the Fourth and Fourteenth <span class="star-pagination">*724</span> Amendments.<sup>[2]</sup> Our decisions recognize no exception to the rule that illegally seized evidence is inadmissible at trial, however relevant and trustworthy the seized evidence may be as an item of proof. The exclusionary rule was fashioned as a sanction to redress and deter overreaching governmental conduct prohibited by the Fourth Amendment. To make an exception for illegally seized evidence which is trustworthy would fatally undermine these purposes. Thus, in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#655" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 655</a></span> (1961), we held that "<i>all</i> evidence obtained by searches and seizures in violation of the Constitution is, by that same authority, inadmissible in a state court." (Italics supplied.) Fingerprint evidence is no exception to this comprehensive rule. We agree with and adopt the conclusion of the Court of Appeals for the District of Columbia Circuit in <i>Bynum</i> v. <i>United States,</i> 104 U. S. App. D. C. 368, 370, <span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/#467" aria-description="Citation for case: Clayborne Bynum v. United States">262 F. 2d 465, 467</a></span> (1958):</p>
<blockquote>"True, fingerprints can be distinguished from statements given during detention. They can also be distinguished from articles taken from a prisoner's possession. Both similarities and differences of each type of evidence to and from the others are apparent. But all three have the decisive common characteristic of being something of evidentiary value which the public authorities have caused an arrested person to yield to them during illegal detention. If one such product of illegal detention is proscribed, by the same token all should be proscribed."</blockquote>
<p>We turn then to the question whether the detention of petitioner during which the fingerprints used at trial were taken constituted an unreasonable seizure of his <span class="star-pagination">*725</span> person in violation of the Fourth Amendment. The opinion of the Mississippi Supreme Court proceeded on the mistaken premise that petitioner's prints introduced at trial were taken during his brief detention on December 3. In fact, as both parties before us agree, the fingerprint evidence used at trial was obtained on December 14, while petitioner was still in detention following his December 12 arrest. The legality of his arrest was not determined by the Mississippi Supreme Court. However, on oral argument here, the State conceded that the arrest on December 12 and the ensuing detention through December 14 were based on neither a warrant nor probable cause and were therefore constitutionally invalid. The State argues, nevertheless, that this invalidity should not prevent us from affirming petitioner's conviction. The December 3 prints were validly obtained, it is argued, and "it should make no difference in the practical or legal sense which [fingerprint] card was sent to the F. B. I. for comparison."<sup>[3]</sup> It may be that it does make a difference in light of the objectives of the exclusionary rule, see <i>Bynum</i> v. <span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/#371" aria-description="Citation for case: Clayborne Bynum v. United States"><i>United States, supra,</i> at 371-372</a></span>, <span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/#468" aria-description="Citation for case: Clayborne Bynum v. United States">262 F. 2d, at 468-469</a></span>,<sup>[4]</sup> but we need not decide the question since we have concluded that the prints of December 3 were not validly obtained.</p>
<p><span class="star-pagination">*726</span> The State makes no claim that petitioner voluntarily accompanied the police officers to headquarters on December 3 and willingly submitted to fingerprinting. The State's brief also candidly admits that "[a]ll that the Meridian Police could possibly have known about petitioner at the time . . . would not amount to probable cause for his arrest . . . ."<sup>[5]</sup> The State argues, however, that the December 3 detention was of a type which does not require probable cause. Two rationales for this position are suggested. First, it is argued that the detention occurred during the investigatory rather than accusatory stage and thus was not a seizure requiring probable cause. The second and related argument is that, at the least, detention for the sole purpose of obtaining fingerprints does not require probable cause.</p>
<p>It is true that at the time of the December 3 detention the police had no intention of charging petitioner with the crime and were far from making him the primary focus of their investigation. But to argue that the Fourth Amendment does not apply to the investigatory stage is fundamentally to misconceive the purposes of the Fourth Amendment. Investigatory seizures would subject unlimited numbers of innocent persons to the harassment and ignominy incident to involuntary detention. Nothing is more clear than that the Fourth Amendment was meant to prevent wholesale intrusions upon the personal security of our citizenry, whether these intrusions <span class="star-pagination">*727</span> be termed "arrests" or "investigatory detentions."<sup>[6]</sup> We made this explicit only last Term in <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19</a></span> (1968), when we rejected "the notions that the Fourth Amendment does not come into play at all as a limitation upon police conduct if the officers stop short of something called a `technical arrest' or a `full-blown search.' "</p>
<p>Detentions for the sole purpose of obtaining fingerprints are no less subject to the constraints of the Fourth Amendment. It is arguable, however, that, because of the unique nature of the fingerprinting process, such detentions might, under narrowly defined circumstances, be found to comply with the Fourth Amendment even though there is no probable cause in the traditional sense. See <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967). Detention for fingerprinting may constitute a much less serious intrusion upon personal security than other types of police searches and detentions. Fingerprinting involves none of the probing into an individual's private life and thoughts that marks an interrogation or search. Nor can fingerprint detention be employed repeatedly to harass any individual, since the police need only one set of each person's prints. Furthermore, fingerprinting is an inherently more reliable and effective crime-solving tool than eyewitness identifications or confessions and is not subject to such abuses as the improper line-up and the "third degree." Finally, because there is no danger of destruction of fingerprints, the limited detention need not come unexpectedly or at an inconvenient time. <span class="star-pagination">*728</span> For this same reason, the general requirement that the authorization of a judicial officer be obtained in advance of detention would seem not to admit of any exception in the fingerprinting context.</p>
<p>We have no occasion in this case, however, to determine whether the requirements of the Fourth Amendment could be met by narrowly circumscribed procedures for obtaining, during the course of a criminal investigation, the fingerprints of individuals for whom there is no probable cause to arrest. For it is clear that no attempt was made here to employ procedures which might comply with the requirements of the Fourth Amendment: the detention at police headquarters of petitioner and the other young Negroes was not authorized by a judicial officer; petitioner was unnecessarily required to undergo two fingerprinting sessions; and petitioner was not merely fingerprinted during the December 3 detention but also subjected to interrogation. The judgment of the Mississippi Supreme Court is therefore</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE FORTAS took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE HARLAN, concurring.</p>
<p>I join the opinion of the Court, with one reservation. The Court states in dictum that, because fingerprinting may be scheduled for a time convenient to the citizen, "the general requirement that the authorization of a judicial officer be obtained in advance of detention would seem not to admit of any exception in the fingerprinting context." <i>Ante,</i> this page. I cannot concur in so sweeping a proposition. There may be circumstances, falling short of the "dragnet" procedures employed in this case, where compelled submission to fingerprinting would not amount to a violation of the Fourth Amendment even in the <span class="star-pagination">*729</span> absence of a warrant, and I would leave that question open.</p>
<p>MR. JUSTICE BLACK, dissenting.</p>
<p>The petitioner here was convicted of a brutal rape of a woman, committed in her own home. Fingerprints of the petitioner, left on the window sill of her home, were the clinching evidence bringing about petitioner's conviction. The Court, by once more expanding the reach of the judicially declared exclusionary rule, ostensibly resting on the Fourth Amendment, holds the fingerprint evidence constitutionally inadmissible and thereby reverses petitioner's conviction. The rape occurred on December 2, 1965, and, as was their duty, the police authorities began to make a searching investigation the morning of December 3. The raped woman was originally able to describe the rapist only as a young Negro male. With this evidence the police proceeded to interrogate a number of young Negroes on the streets, at their homes, or at the police station, and then permitted them to go on their way. The petitioner was among those so interrogated on December 3, at which time his fingerprints were made. The fingerprints were again taken on December 14. The record does not show that petitioner or any other young man who was questioned and fingerprinted ever made the slightest objection. Apparently all of them cooperated with the police in efforts to find out who had committed the rape. This case is but one more in an ever-expanding list of cases in which this Court has been so widely blowing up the Fourth Amendment's scope that its original authors would be hard put to recognize their creation.<sup>[*]</sup> For this most <span class="star-pagination">*730</span> unnecessary expansion of the Amendment, the Court is compelled to put its chief reliance on a Court of Appeals decision, <i>Bynum</i> v. <i>United States,</i> 104 U. S. App. D. C. 368, <span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/" aria-description="Citation for case: Clayborne Bynum v. United States">262 F. 2d 465</a></span>. I think it is high time this Court, in the interest of the administration of criminal justice, made a new appraisal of the language and history of the Fourth Amendment and cut it down to its intended size. Such a judicial action would, I believe, make our cities a safer place for men, women, and children to live.</p>
<p>I dissent from this reversal.</p>
<p>MR. JUSTICE STEWART, dissenting.</p>
<p>I do not disagree with the Court's conclusion that the petitioner was arrested and detained without probable cause. But it does not follow that his fingerprints were inadmissible at the trial.</p>
<p>Fingerprints are not "evidence" in the conventional sense that weapons or stolen goods might be. Like the color of a man's eyes, his height, or his very physiognomy, the tips of his fingers are an inherent and unchanging characteristic of the man. And physical impressions of his fingertips can be exactly and endlessly reproduced.</p>
<p>We do not deal here with a confession wrongfully obtained or with property wrongfully seizedso tainted as to be forever inadmissible as evidence against a defendant. We deal, instead, with "evidence" that can be identically reproduced and lawfully used at any subsequent trial.<sup>[*]</sup></p>
<p>I cannot believe that the doctrine of <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, requires so useless a gesture as the reversal of this conviction.</p>
<h2>NOTES</h2>
<p>[1]  The statement was not introduced at the trial.</p>
<p>[2]  Fingerprint evidence would seem no more "trustworthy" than other types of evidencesuch as guns, narcotics, gambling equipment which are routinely excluded if illegally obtained.</p>
<p>[3]  Brief for Respondent 8.</p>
<p>[4]  The Government argued in <i><span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/" aria-description="Citation for case: Clayborne Bynum v. United States">Bynum</a></span></i> that the controversy over the introduction in evidence of a particular set of fingerprints was "much ado over very little," because another set properly taken was available and might have been used. The Court of Appeals rejected this argument: "It bears repeating that the matter of primary judicial concern in all cases of this type is the imposition of effective sanctions implementing the Fourth Amendment guarantee against illegal arrest and detention. Neither the fact that the evidence obtained through such detention is itself trustworthy or the fact that equivalent evidence can conveniently be obtained in a wholly proper way militates against this overriding consideration. It is entirely irrelevant that it may be relatively easy for the government to prove guilt without using the product of illegal detention. The important thing is that those administering the criminal law understand that they must do it that way." 104 U. S. App. D. C., at 371-372, <span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/#468" aria-description="Citation for case: Clayborne Bynum v. United States">262 F. 2d, at 468-469</a></span>. On Bynum's retrial another set of fingerprints in no way connected with his unlawful arrest was used, and he was again convicted. The Court of Appeals affirmed this conviction. 107 U. S. App. D. C. 109, <span class="citation" data-id="250068"><a href="/opinion/250068/clayborne-bynum-v-united-states/" aria-description="Citation for case: Clayborne Bynum v. United States">274 F. 2d 767</a></span> (1960).</p>
<p>[5]  Brief for Respondent 3.</p>
<p>[6]  The State relies on various statements in our cases which approve general questioning of citizens in the course of investigating a crime. See <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#477" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 477-478</a></span> (1966); <i>Culombe</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#635" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568, 635</a></span> (concurring opinion) (1961). But these statements merely reiterated the settled principle that while the police have the right to request citizens to answer voluntarily questions concerning unsolved crimes they have no right to compel them to answer.</p>
<p>[*]  See, <i>e. g., </i><i>Bumper</i> v. <i>North Carolina,</i> 391 U. S. 543another rape case; <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span>; <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span>; <i>Recznik</i> v. <i>City of Lorain,</i> <span class="citation" data-id="9423850"><a href="/opinion/107800/recznik-v-city-of-lorain/" aria-description="Citation for case: Recznik v. City of Lorain">393 U. S. 166</a></span>; and <i>Griswold</i> v. <i>Connecticut,</i> <span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/" aria-description="Citation for case: Griswold v. Connecticut">381 U. S. 479</a></span>.</p>
<p>[*]  At the original trial the victim of the rape, under oath, positively identified the petitioner as her assailant. There now exists, therefore, ample probable cause to detain him and take his fingerprints.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Davis v. United States (2011).json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Davis v. United States (2011)"
type: case
citation: "564 U.S. 229 (2011)"
parallel_cite: "131 S. Ct. 2419; 180 L. Ed. 2d 285"
neutral_cite: 2011 U.S. LEXIS 4560
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2011
date_decided: 2011-06-16
docket: 09-11328
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2011-06-16
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "Davis v. United States (2011)"
  varies_by_point: false
  scope_note: Extends the Leon good-faith line to objectively reasonable reliance on binding appellate precedent later overruled. Good law.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/218926/davis-v-united-states/"
  cluster_id: 218926
  opinion_id: 9441776
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny (good faith)"
related: ["[[United States v. Leon]]", "[[Herring v. United States]]", "[[Illinois v. Krull]]", "[[Arizona v. Gant]]", "[[New York v. Belton]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "good-faith", "automobile", "search-incident-to-arrest"]
holding: "The exclusionary rule does not apply to evidence obtained during a search conducted in objectively reasonable reliance on binding appellate precedent that is only later overruled, because there is no culpable police misconduct to deter."
lake:
  record_id: "Davis v. United States (2011)"
  status: under_review
  projected_at: 2026-07-09
---

# Davis v. United States (2011)

*564 U.S. 229 (2011)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above; this is the 2011 good-faith case — distinct from the 1994 Miranda-invocation [[Davis v. United States]] -->

## Background
During an Alabama traffic stop, Davis, a passenger, gave a false name, was arrested for that, handcuffed, and placed in a patrol car. Officers then searched the passenger compartment incident to the arrest under then-binding Eleventh Circuit precedent (which read [[New York v. Belton]] to authorize the search) and found a revolver in his jacket. He was convicted of being a felon in possession. While his appeal was pending, [[Arizona v. Gant]] was decided, which made the search unconstitutional. The Eleventh Circuit agreed the search violated *[[Arizona v. Gant|Gant]]* but declined to suppress.

## Issue
Whether the exclusionary rule applies to evidence obtained during a search conducted in objectively reasonable reliance on binding appellate precedent that is later overruled.

## Rule
No. The exclusionary rule is a deterrent sanction, and it is unjustified where the police are not culpable. "Because suppression would do nothing to deter police misconduct in these circumstances, and because it would come at a high cost to both the truth and the public safety, we hold that searches conducted in objectively reasonable reliance on binding appellate precedent are not subject to the exclusionary rule." — 564 U.S. at 232. ^pin-232

## Application
The officers searched Davis's car in strict compliance with the Eleventh Circuit precedent that governed at the time; they "act[ed] as a reasonable officer would and should act." Their conduct was not deliberate, reckless, or grossly negligent — the culpability that alone makes exclusion worth its costs under the *[[United States v. Leon|Leon]]* / *[[Herring v. United States|Herring]]* line. Suppressing the revolver would deter no misconduct and would only penalize an officer for following the law, while exacting the high social cost of releasing a felon caught with a firearm. That *[[Arizona v. Gant|Gant]]* later changed the rule did not retroactively make the officers' reliance unreasonable.

## Conclusion
"We therefore hold that when the police conduct a search in objectively reasonable reliance on binding appellate precedent, the exclusionary rule does not apply." — *Id.* at 249–250. ^pin-249

The Eleventh Circuit's refusal to suppress was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Davis* extends the [[The Good-Faith Exception|good-faith exception]] of [[United States v. Leon]], [[Illinois v. Krull]], and [[Herring v. United States]] to reliance on binding appellate precedent, applying it to a search valid under [[New York v. Belton]] but unlawful after [[Arizona v. Gant]].
- **Disambiguation:** this is the **2011 good-faith** decision; the bare wikilink [[Davis v. United States]] resolves to the distinct **1994** Miranda ambiguous-invocation case.

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny (good faith)*

## Sources
- *Davis v. United States*, 564 U.S. 229 (2011) — https://www.courtlistener.com/opinion/218926/davis-v-united-states/ — pinpoints: 232, 249–250.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f4e0444b98230812", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Davis v. United States (2011)"}, "payload": {"all": [{"cite": "181 L. Ed. 2d 563", "page": "563", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "181"}, {"cite": "2011 U.S. LEXIS 8943", "page": "8943", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2011"}, {"cite": "132 S. Ct. 864", "page": "864", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "132"}, {"cite": "565 U.S. 1100", "page": "1100", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "565"}, {"cite": "80 U.S.L.W. 3555", "page": "3555", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "80"}], "display": "565 U.S. 1100", "official": {"cite": "565 U.S. 1100", "page": "1100", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "565"}, "official_selection_present": true, "record_id": "Davis v. United States (2011)"}}
{"assertion_id": "278aedb92d2c6d10", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-232", "record_id": "Davis v. United States (2011)"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-232", "pinpoint_status": "slip-only", "quote": "--- # Davis v. United States (2011) *564 U.S. 229 (2011)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above; this is the 2011 good-faith case — distinct from the 1994 Miranda-invocation [[Davis v. United States]] --> ## Background During an Alabama traffic stop, Davis, a passenger, gave a false name, was arrested for that, handcuffed, and placed in a patrol car. Officers then searched the passenger compartment incident to the arrest under then-binding Eleventh Circuit precedent (which read [[New York v. Belton]] to authorize the search) and found a revolver in his jacket. He was convicted of being a felon in possession. While his appeal was pending, [[Arizona v. Gant]] was decided, which made the search unconstitutional. The Eleventh Circuit agreed the search violated *Gant* but declined to suppress. ## Issue Whether the exclusionary rule applies to evidence obtained during a search conducted in objectively reasonable reliance on binding appellate precedent that is later overruled. ## Rule No. The exclusionary rule is a deterrent sanction, and it is unjustified where the police are not culpable.", "quote_fidelity": "mismatch", "record_id": "Davis v. United States (2011)", "star_marker": null}}
{"assertion_id": "bbbd1147ec9b65c9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-249", "record_id": "Davis v. United States (2011)"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-249", "pinpoint_status": "slip-only", "quote": "Their conduct was not deliberate, reckless, or grossly negligent — the culpability that alone makes exclusion worth its costs under the *Leon* / *Herring* line. Suppressing the revolver would deter no misconduct and would only penalize an officer for following the law, while exacting the high social cost of releasing a felon caught with a firearm. That *Gant* later changed the rule did not retroactively make the officers' reliance unreasonable. ## Conclusion", "quote_fidelity": "mismatch", "record_id": "Davis v. United States (2011)", "star_marker": null}}
{"assertion_id": "2d5e4ea5c727025c", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Davis v. United States (2011)"}, "payload": {"as_of_content": "2011-06-16", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Davis v. United States (2011)", "scope_note": "Extends the Leon good-faith line to objectively reasonable reliance on binding appellate precedent later overruled. Good law.", "varies_by_point": false}}
```

### lake record — Davis v. United States (2011)

```json
{
  "schema_version": "s2.v1",
  "record_id": "Davis v. United States (2011)",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Davis v. United States",
    "case_name_short": "Davis",
    "case_name_full": "Tyrone Roswell Davis v. United States",
    "input_case_name": "Davis v. United States (2011)",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2011-06-16",
    "year": 2011,
    "docket": "09-11328",
    "cluster_id": 218926,
    "lead_opinion_id": 9441776,
    "sibling_ids": [
      218926,
      9441776,
      9441777,
      9441778
    ],
    "absolute_url": "/opinion/218926/davis-v-united-states/",
    "identity_method": "panel-cluster-rekey",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 7350071,
        "score": 20,
        "case_name": "Davis v. United States"
      },
      {
        "cluster_id": 7349256,
        "score": 20,
        "case_name": "Davis v. United States"
      }
    ],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "564 U.S. 229",
      "volume": "564",
      "reporter": "U.S.",
      "page": "229",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "131 S. Ct. 2419",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "2419",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "180 L. Ed. 2d 285",
        "volume": "180",
        "reporter": "L. Ed. 2d",
        "page": "285",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2011 U.S. LEXIS 4560",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "4560",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "131 S. Ct. 2419",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "2419",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "180 L. Ed. 2d 285",
        "volume": "180",
        "reporter": "L. Ed. 2d",
        "page": "285",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "564 U.S. 229",
        "volume": "564",
        "reporter": "U.S.",
        "page": "229",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 U.S. LEXIS 4560",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "4560",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "564 U.S. 229",
    "official_selection": {
      "court_class": "scotus",
      "selected": "564 U.S. 229",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-232",
      "page": null,
      "quote": "--- # Davis v. United States (2011) *564 U.S. 229 (2011)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above; this is the 2011 good-faith case \u2014 distinct from the 1994 Miranda-invocation [[Davis v. United States]] --> ## Background During an Alabama traffic stop, Davis, a passenger, gave a false name, was arrested for that, handcuffed, and placed in a patrol car. Officers then searched the passenger compartment incident to the arrest under then-binding Eleventh Circuit precedent (which read [[New York v. Belton]] to authorize the search) and found a revolver in his jacket. He was convicted of being a felon in possession. While his appeal was pending, [[Arizona v. Gant]] was decided, which made the search unconstitutional. The Eleventh Circuit agreed the search violated *Gant* but declined to suppress. ## Issue Whether the exclusionary rule applies to evidence obtained during a search conducted in objectively reasonable reliance on binding appellate precedent that is later overruled. ## Rule No. The exclusionary rule is a deterrent sanction, and it is unjustified where the police are not culpable.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-249",
      "page": null,
      "quote": "Their conduct was not deliberate, reckless, or grossly negligent \u2014 the culpability that alone makes exclusion worth its costs under the *Leon* / *Herring* line. Suppressing the revolver would deter no misconduct and would only penalize an officer for following the law, while exacting the high social cost of releasing a felon caught with a firearm. That *Gant* later changed the rule did not retroactively make the officers' reliance unreasonable. ## Conclusion",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2011-06-16",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Davis v. United States (2011)",
    "varies_by_point": false,
    "scope_note": "Extends the Leon good-faith line to objectively reasonable reliance on binding appellate precedent later overruled. Good law.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(7268220) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
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
        "query": "cites:(7268220)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(7268220)",
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
    "complete_query": "cites:(7268220)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 7268220,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/davis-v-united-states-2011.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T02:15:41Z",
    "date_modified": "2026-07-09T23:22:57Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law",
      "panel cluster re-key -> cluster 218926 (evidence: S9 F-S9-DN-003; _run/s9/rekey-targets.jsonl 2026-07-09; stub cluster 7350241 -> merits 218926 (Davis v. United States, 564 U.S. 229, 2011); L.Ed.2d dup 7345713 noted)"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:16:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:16:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:18:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:16:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Davis v. United States (2011)

```
<opinion type="majority">
<author id="b275-7">Justice Alito</author>
<p id="AG6">delivered the opinion of the Court.</p>
<p id="b275-8">The Fourth Amendment protects the right, to be free from “unreasonable searches and seizures,” but it is silent about how this right is to be enforced. To supplement the bare text, this Court created the exclusionary rule, a deterrent <page-number citation-index="1" label="232">*232</page-number>sanction that bars the prosecution from introducing evidence obtained by way of a Fourth Amendment violation. The question here is whether to apply this sanction when the police conduct a search in compliance with binding precedent that is later overruled. Because suppression would do nothing to deter police misconduct in these circumstances, and because it would come at a high cost to both the truth and the public safety, we hold that searches conducted in objectively reasonable reliance on binding appellate precedent are not subject to the exclusionary rule.</p>
<p id="b276-9">&gt; — Í</p>
<p id="b276-3">The question presented arises in this case as a result of a shift in our Fourth Amendment jurisprudence on searches of automobiles incident to arrests of recent occupants.</p>
<p id="b276-4">A</p>
<p id="b276-5">Under this Court’s decision in <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), a police officer who makes a lawful arrest may conduct a warrantless search of the arrestee’s person and the area “within his immediate control.” <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California"><em>Id., </em>at 763</a></span> (internal quotation marks omitted). This rule “may be stated clearly enough,” but in the early going after <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>it proved difficult to apply, particularly in cases that involved searches “inside [of] automobile[s] after the arrestees [we]re no longer in [them].” See <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#458" aria-description="Citation for case: New York v. Belton">453 U. S. 454, 458-459</a></span> (1981). A number of courts upheld the constitutionality of vehicle searches that were “substantially contemporaneous” with occupants’ arrests.<footnotemark>1</footnotemark> Other courts disapproved of automobile searches incident to arrests, at least absent some continuing threat that the arrestee might gain access to the vehicle and “destroy evidence or grab a <page-number citation-index="1" label="233">*233</page-number>weapon.”<footnotemark>2</footnotemark> In <em>New York </em>v. <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>, </em>this Court granted cer-tiorari to resolve the conflict. See <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#459" aria-description="Citation for case: New York v. Belton"><em>id., </em>at 459-460</a></span>.</p>
<p id="b277-5">In <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>, </em>a police officer conducting a traffic stop lawfully-arrested four occupants of a vehicle and ordered the arrest-ees to line up, unhandcuffed, along the side of the thruway. <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#456" aria-description="Citation for case: New York v. Belton"><em>Id., </em>at 456</a></span>; see Brief for Petitioner in <em>New York </em>v. <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>, </em>O. T. 1980, No. 80-328, p. 3. The officer then searched the vehicle’s passenger compartment and found cocaine inside a jacket that lay on the backseat. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#456" aria-description="Citation for case: New York v. Belton">453 U. S., at 456</a></span>. This Court upheld the search as reasonable incident to the occupants’ arrests. In an opinion that repeatedly stressed the need for a “straightforward,” “workable rule” to guide police conduct, the Court announced “that when a policeman has made a lawful custodial arrest of the occupant of an automobile, he may, as a contemporaneous incident of that arrest, search the passenger compartment of that automobile.” <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#459" aria-description="Citation for case: New York v. Belton"><em>Id., </em>at 459-460</a></span> (footnote omitted).</p>
<p id="b277-6">For years, <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>was widely -understood to have set down a simple, bright-line rule. Numerous courts read the decision to authorize automobile searches incident to arrests of recent occupants, regardless of whether the arrestee in any particular ease was within reaching distance of the vehicle at the time of the search. See <em>Thornton </em>v. <em>United States, </em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/#628" aria-description="Citation for case: Thornton v. United States">541 U. S. 615, 628</a></span> (2004) (Scalia, J., concurring in judgment) (collecting cases). Even after the arrestee had stepped out of the vehicle and had been subdued by police, the prevailing understanding was that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>still authorized a substantially contemporaneous search of the automobile’s passenger compartment.<footnotemark>3</footnotemark></p>
<p id="b278-4"><page-number citation-index="1" label="234">*234</page-number>Not every court, however, agreed with this reading of <em>Bel-ton. </em>In <em>State </em>v. <em>Gant, </em><span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/" aria-description="Citation for case: State v. Gant">216 Ariz. 1</a></span>, <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/" aria-description="Citation for case: State v. Gant">162 P. 3d 640</a></span> (2007), the Arizona Supreme Court considered an automobile search conducted after the vehicle’s occupant had been arrested, handcuffed, and locked in a patrol car. The court distinguished <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>as a case in which “four unsecured” arrestees "presented an immediate risk of loss of evidence and an obvious threat to [a] lone officer’s safety.” <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#4" aria-description="Citation for case: State v. Gant">216 Ariz., at 4</a></span>, <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#643" aria-description="Citation for case: State v. Gant">162 P. 3d, at 643</a></span>. The court held that where no such “exigencies exis[t]” — where the arrestee has been subdued and the scene secured — the rule of <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>does not apply. <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#4" aria-description="Citation for case: State v. Gant">216 Ariz., at 4</a></span>, <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#643" aria-description="Citation for case: State v. Gant">162 P. 3d, at 643</a></span>.</p>
<p id="b278-5">This Court granted certiorari in <em><span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/" aria-description="Citation for case: State v. Gant">Gant</a></span>, </em>see <span class="citation no-link">552 U. S. 1230</span> (2008), and affirmed in a 5-to-4 decision. <em>Arizona </em>v. Gant, <span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">556 U. S. 332</a></span> (2009). Four of the Justices in the majority agreed with the Arizona Supreme Court that <em>Belton's </em>holding applies only where “the arrestee is unsecured and within reaching distance of the passenger compartment at the time of the search.” <span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/#343" aria-description="Citation for case: Arizona v. Gant">556 U. S., at 343</a></span>. The four dissenting Justices, by contrast, understood <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>to have explicitly adopted the simple, bright-line rule stated in the <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>Court’s opinion. 556 ü. S., at 357-358 (opinion of Alito, J.); see <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton"><em>Belton, supra, </em>at 460</a></span> (“[W]e hold that when a policeman has made a lawful custodial arrest of the occupant of an automobile, he may, as a contemporaneous incident of that arrest, search the passenger compartment of that automobile” (footnote omitted)). To limit <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>to cases involving unsecured arrestees, the dissenters thought, was to overrule the decision’s clear holding. <em>Gant, supra, </em>at 357-358. Justice Scalia, who provided the fifth vote to affirm in <em>Gant, </em>agreed with the dissenters’ understanding of <em>Belton’s </em>holding. <span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/#351" aria-description="Citation for case: Arizona v. Gant">556 U. S., at 351-352</a></span> (concurring opinion). Justice Scalia favored a more explicit and complete overruling of <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>, </em>but he joined what became the majority opinion to avoid “a 4-to-l-to-4” disposition. <span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/#354" aria-description="Citation for case: Arizona v. Gant">556 U. S., at 354</a></span>. As a result, the Court adopted a new, two-part rule under which an auto<page-number citation-index="1" label="235">*235</page-number>mobile search incident to a recent occupant’s arrest is constitutional (1) if the arrestee is within reaching distance of the vehicle during the search, or (2) if the police have reason to believe that the vehicle contains “evidence relevant to the crime of arrest.” <em><span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">Id.,</a></span> </em>at 343 (citing <span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/#632" aria-description="Citation for case: Thornton v. United States"><em>Thornton, supra, </em>at 632</a></span> (Scalia, J., concurring in judgment); internal quotation marks omitted).</p>
<p id="b279-5">B</p>
<p id="b279-6">The search at issue in this case took place a full two years before this Court announced its new rule in <em>Gant </em>On an April evening in 2007, police officers in Greenville, Alabama, conducted a routine traffic stop that eventually resulted in the arrests of driver Stella Owens (for driving while intoxicated) and passenger Willie Davis (for giving a false name to police). The police handcuffed both Owens and Davis, and they placed the arrestees in the back of separate patrol cars. The police then searched the passenger compartment of Owens’ vehicle and found a revolver inside Davis’ jacket pocket.</p>
<p id="b279-7">Davis was indicted in the Middle District of Alabama on one count of possession of a firearm by a convicted felon. See <span class="citation no-link">18 U. S. C. § 922</span>(g)(1). In his motion to suppress the revolver, Davis acknowledged that the officers’ search fully complied with “existing Eleventh Circuit precedent.” App. 13-15. Like most courts, the Eleventh Circuit had long read <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>to establish a bright-line rule authorizing substantially contemporaneous <em>vehicle searches incident to </em>arrests of recent occupants. See <em>United States </em>v. <em>Gonzalez, </em><span class="citation" data-id="709244"><a href="/opinion/709244/united-states-v-augustin-gonzalez/#822" aria-description="Citation for case: United States v. Augustin Gonzalez">71 F. 3d 819, 822, 824-827</a></span> (CA11 1996) (upholding automobile search conducted after the defendant had been “pulled from the vehicle, handcuffed, laid on the ground, and placed under arrest”). Davis recognized that the District Court was obligated to follow this precedent, but he raised a Fourth Amendment challenge to preserve “the issue for review” on appeal. App. 15. The District Court denied the motion, and Davis was convicted on the firearms charge.</p>
<p id="b280-5"><page-number citation-index="1" label="236">*236</page-number>While Davis’ appeal was pending, this Court decided <em>Gant. </em>The Eleventh Circuit, in the opinion below, applied <em>Ganfs </em>new rule and held that the vehicle search incident to Davis’ arrest “violated [his] Fourth Amendment rights.” <span class="citation multiple-matches"><a href="/c/F.%203d/598/1259/">598 F. 3d 1259</a></span>, 1263 (CA11 2010). As for whether this constitutional violation warranted suppression, the Eleventh Circuit viewed that as a separate issue that turned on “the potential of exclusion to deter wrongful police conduct.” <em>Id., </em>at 1265 (quoting <em>Herring </em>v. <em>United States, </em><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#137" aria-description="Citation for case: Herring v. United States">555 U. S. 135, 137</a></span> (2009); internal quotation marks omitted). The court concluded that “penalizing the [arresting] officer” for following binding appellate precedent would do nothing to “dete[r]. . . Fourth Amendment violations.” 598 F. 3d, at 1265-1266 (bracketing and internal quotation marks omitted). It therefore declined to apply the exclusionary rule and affirmed Davis’ conviction. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./562/1002/">562 U. S. 1002</a></span> (2010).</p>
<p id="b280-6">II</p>
<p id="b280-3">The Fourth Amendment protects the “right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures.” The Amendment says nothing about suppressing evidence obtained in violation of this command. That rule — the exclusionary rule — is a “prudential” doctrine, <em>Pennsylvania Bd. of Probation and Parole </em>v. <em>Scott, </em><span class="citation" data-id="9433685"><a href="/opinion/118235/pennsylvania-bd-of-probation-and-parole-v-scott/#363" aria-description="Citation for case: Pennsylvania Bd. of Probation and Parole v. Scott">524 U. S. 357, 363</a></span> (1998), created by this Court to “compel respect for the constitutional guaranty.” <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 217</a></span> (1960); see <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914); <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961). Exclusion is “not a personal constitutional right,” nor is it designed to “redress the injury” occasioned by an unconstitutional search. <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 486</a></span> (1976); see <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#454" aria-description="Citation for case: United States v. Janis">428 U. S. 433, 454, n. 29</a></span> (1976) (exclusionary rule “unsupportable as reparation or compensatory dispensation to the injured criminal” (internal quotation marks omitted)). The rule’s sole purpose, we have repeatedly held, is to deter future Fourth <page-number citation-index="1" label="237">*237</page-number>Amendment violations. <span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#141" aria-description="Citation for case: Herring v. United States"><em>E. g., Herring, supra, </em>at 141</a></span>, and n. 2; <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#909" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 909, 921, n. 22</a></span> (1984); <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States"><em>Elkins, supra, </em>at 217</a></span> (“calculated to prevent, not to repair”). Our cases have thus limited the rule’s operation to situations in which this purpose is “thought most efficaciously served.” <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 348</a></span> (1974). Where suppression fails to yield “appreciable deterrence,” exclusion is “clearly . . . unwarranted.” <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#454" aria-description="Citation for case: United States v. Janis"><em>Janis, supra, </em>at 454</a></span>.</p>
<p id="b281-5">Real deterrent value is a “necessary condition for exclusion,” but it is not “a sufficient” one. <em>Hudson </em>v. <em>Michigan, </em><span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/#596" aria-description="Citation for case: Hudson v. Michigan">547 U. S. 586, 596</a></span> (2006). The analysis must also account for the “substantial social costs” generated by the rule. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#907" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 907</a></span>. Exclusion exacts a heavy toll on both the judicial system and society at large. <em>Stone, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#490" aria-description="Citation for case: Stone v. Powell">428 U. S., at 490-491</a></span>. It almost always requires courts to ignore reliable, trustworthy evidence bearing on guilt or innocence. <em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Ibid.</a></span> </em>And its bottom-line effect, in many cases, is to suppress the truth and set the criminal loose in the community without punishment. See <span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#141" aria-description="Citation for case: Herring v. United States"><em>Herring, supra, </em>at 141</a></span>. Orn-eases hold that society must swallow this bitter pill when necessary, but only as a “last resort.” <span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/#591" aria-description="Citation for case: Hudson v. Michigan"><em>Hudson, supra, </em>at 591</a></span>. For exclusion to be appropriate, the deterrence benefits of suppression must outweigh its heavy costs. See <span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#141" aria-description="Citation for case: Herring v. United States"><em>Herring, supra, </em>at 141</a></span>; <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#910" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 910</a></span>.</p>
<p id="b281-6">Admittedly, there was a time when our exclusionary-rule cases were not nearly so discriminating in <em>their </em>approach to the doctrine. “Expansive dicta” in several decisions, see <span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/#591" aria-description="Citation for case: Hudson v. Michigan"><em>Hudson, supra, </em>at 591</a></span>, suggested that the rule was a self-executing mandate implicit in the Fourth Amendment itself. See <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#462" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 462</a></span> (1928) (remarking <em>on </em>the “striking outcome of the <em>Weeks </em>case” that “the Fourth Amendment, although not referring to or limiting the use of evidence in courts, really forbade its introduction”); <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#655" aria-description="Citation for case: Mapp v. Ohio"><em>Mapp, supra, </em>at 655</a></span> ("[A]ll evidence obtained by searches and seizures in violation of the Constitution is, by <page-number citation-index="1" label="238">*238</page-number>that same authority, inadmissible in a state court”). As late as our 1971 decision in <em>Whiteley </em>v. <em>Warden, Wyo. State Penitentiary, </em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#568" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560, 568-569</a></span>, the Court “treated identification of a Fourth Amendment violation as synonymous with application of the exclusionary rule.” <em>Arizona </em>v. <em>Evans, </em><span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#13" aria-description="Citation for case: Arizona v. Evans">514 U. S. 1, 13</a></span> (1995). In time, however, we came to acknowledge the exclusionary rule for what it undoubtedly is— a “judicially created remedy” of this Court’s own making. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>. We abandoned the old, “reflexive” application of the doctrine, and imposed a more rigorous weighing of its costs and deterrence benefits. <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#13" aria-description="Citation for case: Arizona v. Evans"><em>Evans, supra, </em>at 13</a></span>; see, <em>e. g., <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">Calandra, supra;</a></span> <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis, supra;</a></span> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone, supra;</a></span> INS </em>v. <em>Lopez-Mendoza, </em><span class="citation" data-id="9429772"><a href="/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Lopez-Mendoza">468 U. S. 1032</a></span> (1984); <em>United States </em>v. <em>Havens, </em><span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/" aria-description="Citation for case: United States v. Havens">446 U. S. 620</a></span> (1980). In a line of cases beginning with <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U. S. 897</a></span>, we also recalibrated our cost-benefit analysis in exclusion cases to focus the inquiry on the “flagrancy of the police misconduct” at issue. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#909" aria-description="Citation for case: United States v. Leon"><em>Id., </em>at 909, 911</a></span>.</p>
<p id="b282-4">The basic insight of the <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>line of cases is that the deterrence benefits of exclusion “var[y] with the culpability of the law enforcement conduct” at issue. <em>Herring, </em><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#143" aria-description="Citation for case: Herring v. United States">555 U. S., at 143</a></span>. When the police exhibit “deliberate,” “reckless,” or “grossly negligent” disregard for Fourth Amendment rights, the deterrent value of exclusion is strong and tends to outweigh the resulting costs. <span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#144" aria-description="Citation for case: Herring v. United States"><em>Id., </em>at 144</a></span>. But when the police act with an objectively “reasonable good-faith belief” that their conduct is lawful, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#909" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 909</a></span> (internal quotation marks omitted), or when their conduct involves only simple, “isolated” negligence, <span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#137" aria-description="Citation for case: Herring v. United States"><em>Herring, supra, </em>at 137</a></span>, the “'deterrence rationale loses much of its force,”’ and exclusion cannot “pay its way,” <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#919" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 919, 908</a></span>, n. 6 (quoting <em>United States </em>v. <em>Peltier, </em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#539" aria-description="Citation for case: United States v. Peltier">422 U. S. 531, 539</a></span> (1975)).</p>
<p id="b282-5">The Court has over time applied this “good-faith” exception across a range of cases. <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>itself, for example, held that the exclusionary rule does not apply when the police conduct a search in “objectively reasonable reliance” on a <page-number citation-index="1" label="239">*239</page-number>warrant later held invalid. 468 U. S., at 922. The error in such a case rests with the issuing magistrate, not the police officer, and “punish[ing] the errors of judges” is not the office of the exclusionary rule. <em>Id., </em>at 916; see also <em>Massachusetts </em>v. <em>Sheppard, </em><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#990" aria-description="Citation for case: Massachusetts v. Sheppard">468 U. S. 981, 990</a></span> (1984) (companion case declining to apply exclusionary rule where warrant held invalid as a result of judge’s clerical error).</p>
<p id="b283-6">Other good-faith eases have sounded a similar theme. <em>Illinois </em>v. <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">480 U. S. 340</a></span> (1987), extended the good-faith exception to searches conducted in reasonable reliance on subsequently invalidated statutes. <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#349" aria-description="Citation for case: Illinois v. Krull"><em>Id., </em>at 349-350</a></span> (“legislators, like judicial officers, are not the focus of the rule”). In <em><span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/" aria-description="Citation for case: Arizona v. Evans">Evans, supra,</a></span> </em>the Court applied the good-faith exception in a case where the police reasonably relied on erroneous information concerning an arrest warrant in a database maintained by judicial employees. <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#14" aria-description="Citation for case: Arizona v. Evans"><em>Id., </em>at 14</a></span>. Most recently, in <em><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/" aria-description="Citation for case: Herring v. United States">Herring, supra,</a></span> </em>we extended <em><span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/" aria-description="Citation for case: Arizona v. Evans">Evans</a></span> </em>in a case where <em>police </em>employees erred in maintaining records in a warrant database. “[IJsolated,” “nonrecurring” police negligence, we determined, lacks the culpability required to justify the harsh sanction of exclusion. <span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#137" aria-description="Citation for case: Herring v. United States">555 U. S., at 137, 144</a></span>.</p>
<p id="b283-7">1 — I I — i ) — I</p>
<p id="b283-3">The question in this ease is whether to apply the exclusionary rule when the police conduct a search in objectively reasonable reliance on binding judicial precedent. At the time of the search at issue here, we had not yet decided <em>Gant, </em><span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">556 U. S. 332</a></span>, and the Eleventh Circuit had interpreted our decision in <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span>, to establish a bright-line rule authorizing the search of a vehicle’s passenger compartment incident to a recent occupant’s arrest. <em>Gonzalez, </em><span class="citation" data-id="709244"><a href="/opinion/709244/united-states-v-augustin-gonzalez/#825" aria-description="Citation for case: United States v. Augustin Gonzalez">71 F. 3d, at 825</a></span>. The search incident to Davis’ arrest in this case followed the Eleventh Circuit’s <em><span class="citation" data-id="709244"><a href="/opinion/709244/united-states-v-augustin-gonzalez/" aria-description="Citation for case: United States v. Augustin Gonzalez">Gonzalez</a></span> </em>precedent to the letter. Although the search turned out to be unconstitutional under <em>Gant, </em>all agree that the officers’ conduct was in strict compliance with then-binding Circuit law and was not <page-number citation-index="1" label="240">*240</page-number>culpable in any way. See Brief for Petitioner 49 (“suppression” in this case would “impl[y] no assignment of blame”).</p>
<p id="b284-5">Under our exclusionary-rule precedents, this acknowledged absence of police culpability dooms Davis’ claim. Police practices trigger the harsh sanction of exclusion only when they are deliberate enough to yield “meaningful 1]” deterrence, and culpable enough to be “worth the price paid by the justice system.” <em>Herring, </em><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#144" aria-description="Citation for case: Herring v. United States">555 U. S., at 144</a></span>. The conduct of the officers here was neither of these things. The officers who conducted the search did not violate Davis’ Fourth Amendment rights deliberately, recklessly, or with gross negligence. See <em><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/" aria-description="Citation for case: Herring v. United States">ibid.</a></span> </em>Nor does this case involve any “recurring or systemic negligence” on the part of law enforcement. <em><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/" aria-description="Citation for case: Herring v. United States">Ibid.</a></span> </em>The police acted in strict compliance with binding precedent, and their behavior was not wrongful. Unless the exclusionary rule is to become a strict-liability regime, it can have no application in this case.</p>
<p id="b284-6">Indeed, in 27 years of practice under <em>Leon’s </em>good-faith exception, we have “never applied” the exclusionary rule to suppress evidence obtained as a result of noneulpable, innocent police conduct. <span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#144" aria-description="Citation for case: Herring v. United States"><em>Herring, supra, </em>at 144</a></span>. If the police in this case had reasonably relied on a warrant in conducting their search, see <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon, supra,</a></span> </em>or on an erroneous warrant record in a government database, <em><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/" aria-description="Citation for case: Herring v. United States">Herring, supra,</a></span> </em>the exclusionary rule would not apply. And if Congress or the Alabama Legislature had enacted a statute codifying the precise holding of the Eleventh Circuit’s decision in <em><span class="citation" data-id="709244"><a href="/opinion/709244/united-states-v-augustin-gonzalez/" aria-description="Citation for case: United States v. Augustin Gonzalez">Gonzalez</a></span>,</em><footnotemark><em>4</em></footnotemark><em>, </em>we <page-number citation-index="1" label="241">*241</page-number>would swiftly conclude that “ ‘[penalizing the officer for the [legislature’s] error . . . cannot logically contribute to the deterrence of Fourth Amendment violations.’” <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#350" aria-description="Citation for case: Illinois v. Krull">480 U. S., at 350</a></span>. The same should be true of Davis’ attempt here to “ ‘[p]enaliz[e] the officer for the [appellate judges’] error.’” <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Ibid.</a></span></em></p>
<p id="b285-5">About all that exclusion would deter in this case is conscientious police work. Responsible law enforcement officers will take care to learn “what is required of them” under Fourth Amendment precedent and will conform their conduct to these rules. <em>Hudson, </em><span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/#599" aria-description="Citation for case: Hudson v. Michigan">547 U. S., at 599</a></span>. But by the same token, when binding appellate precedent specifically <em>authorizes </em>a particular police practice, well-trained officers will and should use that tool to fulfill their crime-detection and public-safety responsibilities. An officer who conducts a search in reliance on binding appellate precedent does no more than ‘“ac[t] as a reasonable officer would and should act’ ” under the circumstances. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U. S., at 920</a></span> (quoting <em>Stone, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#539" aria-description="Citation for case: Stone v. Powell">428 U. S., at 539-540</a></span> (White, J., dissenting)). The deterrent effect of exclusion in such a case can only be to discourage the officer from ‘“do[ing] his duty.’” 468 U. S., at 920.</p>
<p id="b285-6">That is not the kind of deterrence the exclusionary rule seeks to foster. We have stated before, and we reaffirm today, that the harsh sanction of exclusion “should not be applied to deter objectively reasonable law enforcement activity.” <em>Id., </em>at 919. Evidence obtained during a search conducted in reasonable reliance on binding precedent is not subject to the exclusionary rule.</p>
<p id="b285-7">IV</p>
<p id="b285-8">Justice Breyer’s dissent and Davis argue that, although the police conduct in this case was in no way culpable, other considerations should prevent the good-faith exception from applying. We are not persuaded.</p>
<p id="b286-4"><page-number citation-index="1" label="242">*242</page-number>A</p>
<p id="b286-5">1</p>
<p id="b286-6">The principal argument of both the dissent and Davis is that the exclusionary rule’s availability to enforce new Fourth Amendment precedent is a retroactivity issue, see <em>Griffith </em>v. <em>Kentucky, </em><span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/" aria-description="Citation for case: Griffith v. Kentucky">479 U. S. 314</a></span> (1987), not a good-faith issue. They contend that applying the good-faith exception where police have relied on overruled precedent effectively revives the discarded retroactivity regime of <em>Linkletter </em>v. <em>Walker, </em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618</a></span> (1965). See <em>post, </em>at 254-256.</p>
<p id="b286-7">In <em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span>, </em>we held that the retroactive effect of a new constitutional rule of criminal procedure should be determined on a case-by-case weighing of interests. For each new rule, <em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span> </em>required courts to consider a three-faetor balancing test that looked to the “purpose” of the new rule, “reliance” on the old rule by law enforcement and others, and the effect retroactivity would have “on the administration of justice.” <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#636" aria-description="Citation for case: Linkletter v. Walker">381 U. S., at 636</a></span>. After “weighting] the merits and demerits in each case,” courts decided whether and to what extent a new rule should be given retroactive effect. <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#629" aria-description="Citation for case: Linkletter v. Walker"><em>Id., </em>at 629</a></span>. In <em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span> </em>itself, the balance of interests prompted this Court to conclude that <em>Mapp </em>v. <em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Ohio</a></span>, </em>367 U. S. 643—which incorporated the exclusionary rule against the States — should not apply retroactively to cases already final on direct review. <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#639" aria-description="Citation for case: Linkletter v. Walker">381 U. S., at 639-640</a></span>. The next year, we extended <em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span> </em>to retroactivity determinations in eases on direct review. See <em>Johnson </em>v. <em>New </em>Jersey, <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#733" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719, 733</a></span> (1966) (holding that <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), and <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964), applied retroactively only to trials commenced after the decisions were released).</p>
<p id="b286-8">Over time, <em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span> </em>proved difficult to apply in a consistent, coherent way. Individual applications of the standard “produced strikingly divergent results,” <em>Danforth </em>v. <em>Minnesota, </em><span class="citation" data-id="9046929"><a href="/opinion/9053440/danforth-v-minnesota/#273" aria-description="Citation for case: Danforth v. Minnesota">552 U. S. 264, 273</a></span> (2008), that many saw as “incompatible” and “inconsistent,” <em>Desist </em>v. <em>United States, </em><span class="citation" data-id="9423951"><a href="/opinion/107875/desist-v-united-states/#258" aria-description="Citation for case: Desist v. United States">394 U. S. 244, 258</a></span> (1969) (Harlan, J., dissenting). Justice Harlan in particu<page-number citation-index="1" label="243">*243</page-number>lar, who had endorsed the <em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span> </em>standard early on, offered a strong critique in which he argued that “basic judicial” norms required full retroactive application of new rules to all eases still subject to direct review. <span class="citation" data-id="9423951"><a href="/opinion/107875/desist-v-united-states/#258" aria-description="Citation for case: Desist v. United States">394 U. S., at 258-259</a></span>.; see also <em>Mackey </em>v. <em>United </em>States, <span class="citation" data-id="9424506"><a href="/opinion/108302/mackey-v-united-states/#675" aria-description="Citation for case: MacKey v. United States">401 U. S. 667, 675-702</a></span> (1971) (Harlan, J., concurring in part and dissenting in part). Eventually, and after more than 20 years of toil under <em>Link-</em>letter, the Court adopted Justice Harlan’s view and held that newly announced rules of constitutional criminal procedure must apply “retroactively to all cases, state or federal, pending on direct review or not yet final, with no exception.” <span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/#328" aria-description="Citation for case: Griffith v. Kentucky"><em>Griffith, supra, </em>at 328</a></span>.</p>
<p id="b287-5">2</p>
<p id="b287-6">The dissent and Davis argue that applying the good-faith exception in this case is “incompatible” with our retroactivity precedent under <em><span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/" aria-description="Citation for case: Griffith v. Kentucky">Griffith</a></span>. </em>See <em>post, </em>at 254; Reply Brief for Petitioner 3-7. We think this argument conflates what are two distinct doctrines.</p>
<p id="b287-7">Our retroactivity jurisprudence is concerned with whether, as a categorical matter, a new rule is available on direct review as a <em>potential </em>ground for relief. Retroactive application under <em><span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/" aria-description="Citation for case: Griffith v. Kentucky">Griffith</a></span> </em>lifts what would otherwise be a categorical bar to obtaining redress for the government's violation of a newly announced constitutional rule. See <em>Dan-forth, supra, </em>at 271, n. 5 (noting that it may “make more sense to speak in terms of the ‘redressability’ of violations of new rules, rather than the ‘retroactivity’ of such new rules”). Retroactive application does not, however, determine what “appropriate remedy” (if any) the defendant should obtain. See <em>Powell </em>v. <em>Nevada, </em><span class="citation" data-id="9432977"><a href="/opinion/117833/powell-v-nevada/#84" aria-description="Citation for case: Powell v. Nevada">511 U. S. 79, 84</a></span> (1994) (noting that it “does not necessarily follow” from retroactive application of a new rule that the defendant will “gain . . . relief”). Remedy is a separate, analytically distinct issue. Cf. <em>American Trucking Assns., Inc. </em>v. <em>Smith, </em><span class="citation" data-id="9432043"><a href="/opinion/112450/american-trucking-assns-inc-v-smith/#189" aria-description="Citation for case: American Trucking Assns., Inc. v. Smith">496 U. S. 167, 189</a></span> (1990) (plurality opinion) (“[T]he Court has never equated its retroac-tivity principles with remedial principles”). As a result, the retroactive application of a new rule of substantive Fourth <page-number citation-index="1" label="244">*244</page-number>Amendment law <em>raises </em>the question whether a suppression remedy applies; it does not answer that question. See <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon">468 U. S., at 906</a></span> (‘Whether the exclusionary sanction is appropriately imposed in a particular case ... is ‘an issue separate from the question whether the Fourth Amendment rights of the party seeking to invoke the rule were violated by police conduct’ ”).</p>
<p id="b288-5">When this Court announced its decision in <em>Gant, </em>Davis’ conviction had not yet become final on direct review. <em>Gant </em>therefore applies retroactively to this case. Davis may invoke its newly announced rule of substantive Fourth Amendment law as a basis for seeking relief. See <span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/#326" aria-description="Citation for case: Griffith v. Kentucky"><em>Griffith, supra, </em>at 326, 328</a></span>. The question, then, becomes one of remedy, and on that issue Davis seeks application of the exclusionary rule. But exclusion of evidence does not automatically follow from the fact that a Fourth Amendment violation occurred. See <em>Evans, </em><span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#13" aria-description="Citation for case: Arizona v. Evans">514 U. S., at 13-14</a></span>. The remedy is subject to exceptions and applies only where its “purpose is effectively advanced.” <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#347" aria-description="Citation for case: Illinois v. Krull">480 U. S., at 347</a></span>.</p>
<p id="b288-6">The dissent and Davis recognize that at least some of the established exceptions to the exclusionary rule limit its availability in cases involving new Fourth Amendment rules. Suppression would thus be inappropriate, the dissent and Davis acknowledge, if the inevitable-discovery exception were applicable in this case. See <em>post, </em>at 254; Reply Brief for Petitioner 22 (“Doctrines such as inevitable discovery, independent source, attenuated basis, [and] standing . . . sharply limit the impact of newly-announced rules”). The good-faith exception, however, is no less an established limit on the <em>remedy </em>of exclusion than is inevitable discovery. Its application here neither contravenes <em><span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/" aria-description="Citation for case: Griffith v. Kentucky">Griffith</a></span> </em>nor denies retroactive effect to <em>Gant.</em><footnotemark><em>5</em></footnotemark></p>
<p id="b289-4"><page-number citation-index="1" label="245">*245</page-number>It is true that, under the old retroactivity regime of <em>Link-letter, </em>the Court's decisions on the “retroactivity problem in the context of the exclusionary rule” did take into account whether “law enforcement officers reasonably believed in good faith” that their conduct was in compliance with governing law. <em>Peltier, </em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#535" aria-description="Citation for case: United States v. Peltier">422 U. S., at 535-537</a></span>. As a matter of retroactivity analysis, that approach is no longer applicable. See <em>Griffith, </em><span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/" aria-description="Citation for case: Griffith v. Kentucky">479 U. S. 314</a></span>. It does not follow, however, that reliance on binding precedent is irrelevant in applying the good-faith exception to the exclusionary rule. When this Court adopted the good-faith exception in <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>, </em>the Court’s opinion explicitly relied on <em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/" aria-description="Citation for case: United States v. Peltier">Peltier</a></span> </em>and imported its reasoning into the good-faith inquiry. See 468 U. S., at 918-919. That reasonable reliance by police was once a factor in our retroactivity cases does not make it any less relevant under our <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>line of eases.<footnotemark>6</footnotemark></p>
<p id="b289-5">B</p>
<p id="b289-6">Davis also contends that applying the good-faith exception to searches conducted in reliance on binding precedent will stunt the development of Fourth Amendment <page-number citation-index="1" label="246">*246</page-number>law. With no possibility of suppression, criminal defendants will have no incentive, Davis maintains, to request that courts overrule precedent.<footnotemark>7</footnotemark></p>
<p id="b290-5">1</p>
<p id="b290-6">This argument is difficult to reconcile with our modern understanding of the role of the exclusionary rule. We have never held that facilitating the overruling of precedent is a relevant consideration in an exclusionary-rule case. Rather, we have said time and again that the <em>sole </em>purpose of the exclusionary rule is to deter misconduct by law enforcement. See, <em>e. g., Sheppard, </em>468 U. S., at 990 (“ 'adopted to deter unlawful searches by police’ ”); <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#14" aria-description="Citation for case: Arizona v. Evans"><em>Evans, supra, </em>at 14</a></span> (“historically designed as a means of deterring police misconduct”).</p>
<p id="b290-7">We have also repeatedly rejected efforts to expand the focus of the exclusionary rule beyond deterrence of culpable police conduct. In <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>, </em>for example, we made clear that “the exclusionary rule is designed to deter police misconduct rather than to punish the errors of judges.” 468 U. S., at 916; see <em>id., </em>at 918 (“If exclusion of evidence obtained pursuant to a subsequently invalidated warrant is to have any deterrent effect... it must alter the behavior of individual law enforcement officers or the policies of their departments”). <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull</a></span> </em>too noted that “legislators, like judicial officers, are not the focus” of the exclusionary.rule. <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#850" aria-description="Citation for case: Illinois v. Krull">480 U. S., at 850</a></span>. And in <em><span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/" aria-description="Citation for case: Arizona v. Evans">Evans</a></span>, </em>we said that the exclusionary rule was aimed at deterring “police misconduct, not mistakes by court employees.” <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#14" aria-description="Citation for case: Arizona v. Evans">514 U. S., at 14</a></span>. These cases do not suggest that the exclusionary rule should be modified to serve a purpose other than deterrence of culpable law enforcement conduct.</p>
<p id="Atb"><page-number citation-index="1" label="247">*247</page-number>2</p>
<p id="b291-4">And in any event, applying the good-faith exception in this context will not prevent judicial reconsideration of prior Fourth Amendment precedents. In most instances, as in this case, the precedent sought to be challenged will be a decision of a federal court of appeals or state supreme court. But a good-faith exception for objectively reasonable reliance on binding precedent will not prevent review and correction of such decisions. This Court reviews criminal convictions from 12 Federal Courts of Appeals, 50 state courts of last resort, and the District of Columbia Court of Appeals. If one or even many of these courts uphold a particular type of search or seizure, defendants in jurisdictions in which the question remains open will still have an undiminished incentive to litigate the issue. This Court can then grant certio-rari, and the development of Fourth Amendment law will in no way be stunted.<footnotemark>8</footnotemark></p>
<p id="b291-5">Davis argues that Fourth Amendment precedents of <em>this </em>Court will be effectively insulated from challenge under a good-faith exception for reliance on appellate precedent. But this argumentas overblown. For one thing, it is important to keep in mind that this argument applies to an exceedingly small set of cases. Decisions overruling this Court's Fourth Amendment precedents are rare. Indeed, it has been more than 40 years since the Court last handed down a decision of the type to which Davis refers. <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (overruling <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span> (1950), and <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span> (1947)). And even in those cases, Davis points out that <page-number citation-index="1" label="248">*248</page-number>no fewer than eight separate doctrines may preclude a defendant who successfully challenges an existing precedent from getting any relief. Brief for Petitioner 50. Moreover, as a practical matter, defense counsel in many cases will test this Cuurt’s Fourth Amendment precedents in the same way that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>was tested in <em>Gant </em>— by arguing that the precedent is distinguishable. See Brief for Respondent in <em>Arizona </em>v. <em>Gant, </em>O. T. 2008, No. 07-542, pp. 22-29.<footnotemark>9</footnotemark></p>
<p id="b292-5">At most, Davis’ argument might suggest that — to prevent Fourth Amendment law from becoming ossified — the petitioner in a case that results in the overruling of one of this Court’s Fourth Amendment precedents should be given the benefit of the victory by permitting the suppression of evidence in that one case. Such a result would undoubtedly be a windfall to this one random litigant. But the exclusionary rule is “not a personal constitutional right.” <em>Stone, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell">428 U. S., at 486</a></span>. It is a “judicially created” sanction, <em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">Calandra</a></span>, </em>414 TI. ñ., at 848, specifically designed as a “windfall” remedy to deter future Fourth Amendment violations. See <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#490" aria-description="Citation for case: Stone v. Powell"><em>Stone, supra, </em>at 490</a></span>. The good-faith exception is a judicially created exception to this judicially created rule. Therefore, in a future case, we could, if necessary, recognize a limited exception to the good-faith exception for a defendant who obtains a judgment overruling one of our Fourth Amendment precedents. Cf. Friendly, The Bill of Rights as a Code of Criminal Procedure, <span class="citation no-link">53 Cal. L. Rev. 929</span>, 952-953 (1965) (“[T]he same authority that empowered the Court to supplement the amendment by the exclusionary rule a hundred and twenty-five years after its adoption, likewise allows it to <page-number citation-index="1" label="249">*249</page-number>modify that rule as the lessons of experience may teach” (internal quotation marks and footnotes omitted)).<footnotemark>10</footnotemark></p>
<p id="b293-5">But this is not such a case. Davis did not secure a decision overturning a Supreme Court precedent; the police in his case reasonably relied on binding Circuit precedent. See <em>Gonzalez, </em><span class="citation" data-id="709244"><a href="/opinion/709244/united-states-v-augustin-gonzalez/" aria-description="Citation for case: United States v. Augustin Gonzalez">71 F. 3d 819</a></span>. That sort of blameless police conduct, we hold, comes within the good-faith exception and is not properly subject to the exclusionary rule.</p>
<p id="b293-6">* * *</p>
<p id="b293-7">It is one thing for the criminal “to go free because the constable has blundered.” <em>People </em>v. <em>Before, </em><span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#21" aria-description="Citation for case: People v. Defore">242 N. Y. 13, 21</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#587" aria-description="Citation for case: People v. Defore">150 N. E. 585, 587</a></span> (1926) (Cardozo, J.). It is quite another to set the criminal free because the constable has scrupulously adhered to governing law. Excluding evidence in such cases deters no police misconduct and imposes substantial social costs. We therefore hold that when the police conduct a search in objectively reasonable reliance on binding appellate <page-number citation-index="1" label="250">*250</page-number>precedent, the exclusionary rule does not apply. The judgment of the Court of Appeals for the Eleventh Circuit is</p>
<p id="b294-4">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b276-6"> See, <em>e. g., United States </em>v. <em>Sanders, </em><span class="citation" data-id="9467153"><a href="/opinion/382713/united-states-v-willard-r-sanders/#1313" aria-description="Citation for case: United States v. Willard R. Sanders">631 F. 2d 1309, 1313-1314</a></span> (CA8 1980); <em>United States </em>v. <em>Dixon, </em><span class="citation" data-id="347138"><a href="/opinion/347138/united-states-v-lewis-nathaniel-dixon/#922" aria-description="Citation for case: United States v. Lewis Nathaniel Dixon">558 F. 2d 919, 922</a></span> (CA9 1977); <em>United States </em>v. <em>Frick, </em><span class="citation" data-id="9460209"><a href="/opinion/316377/united-states-v-robert-lee-frick-and-quimet-john-petersen/#668" aria-description="Citation for case: United States v. Robert Lee Frick and Quimet John Petersen">490 F. 2d 666, 668-669</a></span> (CA5 1973); <em>Hinkel </em>v. <em>Anchorage, </em><span class="citation" data-id="9617077"><a href="/opinion/1391930/hinkel-v-anchorage/#1069" aria-description="Citation for case: Hinkel v. Anchorage">618 P. 2d 1069, 1069-1071</a></span> (Alaska 1980).</p>
</footnote>
<footnote label="2">
<p id="b277-7"> See, <em>e. g., United States v. Benson, </em><span class="citation" data-id="9467155"><a href="/opinion/382715/united-states-v-jeffrey-joseph-benson/#1340" aria-description="Citation for case: United States v. Jeffrey Joseph Benson">631 F. 2d 1336, 1340</a></span> (CA8 1980); see also <em>United States </em>v. <em>Rigales, </em><span class="citation" data-id="382105"><a href="/opinion/382105/united-states-v-ernesto-g-rigales-jr/#366" aria-description="Citation for case: United States v. Ernesto G. Rigales, Jr.">630 F. 2d 364, 366-367</a></span> (CA5 1980); <em>Ulesky </em>v. <em>State, </em><span class="citation" data-id="1687668"><a href="/opinion/1687668/ulesky-v-state/#125" aria-description="Citation for case: Ulesky v. State">379 So. 2d 121, 125-126</a></span> (Fla. App. 1979).</p>
</footnote>
<footnote label="3">
<p id="b277-8"> See, <em>e. g., United States </em>v. <em>Dorsey, </em><span class="citation" data-id="9498265"><a href="/opinion/791442/united-states-v-nikos-delano-dorsey/#1041" aria-description="Citation for case: United States v. Nikos Delano Dorsey">418 F. 3d 1038, 1041, 1043-1044</a></span> (CA9 2005) (upholding automobile search conducted after the officer had “hand cuffed [tho arrcotcc] and put him in the back of [the] patrol car”); <em>United States </em>v. <em>Barnes, </em><span class="citation" data-id="9497145"><a href="/opinion/786840/united-states-v-angelo-barnes/#604" aria-description="Citation for case: United States v. Angelo Barnes">374 F. 3d 601, 604</a></span> (CA8 2004) (same).</p>
</footnote>
<footnote label="4">
<p id="b284-7"> Cf. <span class="citation no-link">Kan. Stat. Ann. § 22-2501</span>(c) (2007) (“When a lawful arrest is ef-fécted a law enforcement officer may reasonably search the person arrested and the area within such person’s immediate presence for the purpose of . . . [discovering the fruits, instrumentalities, or evidence of a crime”). The Kansas Supreme Court recently struck this provision down in light of <em>Arizona </em>v. <em>Gant, </em><span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">556 U. S. 332</a></span> (2009). <em>State </em>v. <em>Henning, </em><span class="citation" data-id="2625720"><a href="/opinion/2625720/state-v-henning/#137" aria-description="Citation for case: State v. Henning">289 Kan. 136, 137</a></span>, <span class="citation" data-id="2625720"><a href="/opinion/2625720/state-v-henning/#714" aria-description="Citation for case: State v. Henning">209 P. 3d 711, 714</a></span> (2009). But it has applied <em>Illinois </em>v. <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">480 U. S. 340</a></span> (1987), and the good-faith exception to searches conducted in reasonable reliance on the statute. See <em>State </em>v. <em>Daniel, </em><span class="citation" data-id="9761057"><a href="/opinion/2373665/state-v-daniel/#497" aria-description="Citation for case: State v. Daniel">291 Kan. 490, 497-504</a></span>, <span class="citation" data-id="9761057"><a href="/opinion/2373665/state-v-daniel/#1191" aria-description="Citation for case: State v. Daniel">242 P. 3d 1186, 1191-1195</a></span> (2010).</p>
</footnote>
<footnote label="5">
<p id="b288-7"> The dissent argues that the good-faith exception is “unlike ... inevitable discovery” because the former applies in all cases where the police reasonably rely on binding precedent, while the latter “applies only upon occasion.” <em>Post, </em>at 254. We fail to see how this distinction makes any dif-<page-number citation-index="1" label="245">*245</page-number>forcncc. Tho same could bo said indoed, tho oame <em>wao </em>oaid <em>■ of </em>searches conducted in reasonable reliance on statutes. See <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#368" aria-description="Citation for case: Illinois v. Krull">480 U. S., at 368-369</a></span> (O'Connor, <em>J., </em>dissenting) (arguing that result in <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull</a></span> </em>was inconsistent with <em>Griffith). </em>When this Court strikes down a statute on Fourth Amendment grounds, the good-faith exception may prevent the exclusion ary rulo from applying “in <em>every </em>case pending when [the statute] is over turned.” <em>Post, </em>at 254. This result does not make the Court’s newly announced rule of Fourth Amendment law any less retroactive. It simply limits the applicability of a suppression remedy. See <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#354" aria-description="Citation for case: Illinois v. Krull"><em>Krull, supra, </em>at 354-355, n. 11</a></span>.</p>
</footnote>
<footnote label="6">
<p id="b289-12"> Nor does <em>United States </em>v. <em>Johnson, </em><span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">457 U. S. 537</a></span> (1982), foreclose application of the good faith exception in eases involving changing law. <em>John son </em>distinguished <em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/" aria-description="Citation for case: United States v. Peltier">Peltier</a></span> </em>and held that all Fourth Amendment cases should be retroactivo on direct review so long as tho new decision is not a “clear break” from prior precedent. <span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/#562" aria-description="Citation for case: United States v. Johnson">457 U. S., at 562</a></span>. <em>Johnson </em>had no occasion to opino on tho good faith exception to the exclusionary rule, which we adopted two years later in <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>.</em></p>
</footnote>
<footnote label="7">
<p id="b290-8"> Davis also asserts that a good faith rule would permit “new Fourth Amendment dccioiono to be applied only prospoctivoly,” thus amounting to “a regime of rule-ereation by advisory opinion.” Brief for Petitioner 23, 25. For reasons discussed in connection with Davis’ argument that application of tho good faith exception hero would revive tho <em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span> </em>regime, this argument eonflatoa tho quoetion of retroactivity with tho question of remedy.</p>
</footnote>
<footnote label="8">
<p id="b291-6"> Tho diooent docs not dispute this point, but it claims that the good faith exception will prevent us from “retyping] upon lower courts to work out Fourth Amendment differences among themselves.” <em>Post, </em>at 256. If that is correct, then today’c holding may well lead to <em>moro </em>oirouit oplito in Fourth Amendment eaccs and a <em>fullov </em>docket of Fourth Amendment caceo in this Court. See this Court’s Rule 10. Such a state of affairs is unlikely to result in ossification of Fourth Amendment doctrine.</p>
</footnote>
<footnote label="9">
<p id="b292-6"> Where the search at issue is conducted in accordance with a municipal “policy” or “custom,” Fourth Amendment precedents may also be challenged, without the obotaclc of the good-faith exception or qualified immunity, in civil suits against municipalities. See <span class="citation no-link">42 U. S. C. § 1988</span>; <em>Los Angeles County </em>v. <em>Humphries, </em><span class="citation" data-id="180037"><a href="/opinion/180037/los-angeles-county-v-humphries/#36" aria-description="Citation for case: Los Angeles County v. Humphries">562 U. S. 29, 36</a></span> (2010) (citing <em>Monell </em>v. <em>New York City Dept. of Social Servs., </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#690" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658, 690-691</a></span> (1978)).</p>
</footnote>
<footnote label="10">
<p id="b293-8"> Davis contends that a criminal defendant will lack Article III standing to challenge an existing Fourth Amendment precedent if the good-faith exception to the exclusionary rule precludes the defendant from obtaining relief based on police conduct that conformed to that precedent. This argument confuses weakness on the merits with absence of Article III standing. See <em>ASARCO Inc. </em>v. <em>Radish, </em><span class="citation" data-id="9431683"><a href="/opinion/112268/asarco-inc-v-kadish/#624" aria-description="Citation for case: Asarco Inc. v. Kadish">490 U. S. 605, 624</a></span> (1989) (standing does not “ ‘depen[d] on the merits of [a claim]’ ”). And as a practical matter, the argument is also overstated. In many instances, as in <em>Gant, </em>see <span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/#841" aria-description="Citation for case: Arizona v. Gant">556 U. S., at 841</a></span>, defendants will not simply concede that the police conduct conformed to the precedent; they will argue instead that the police conduct did not fall within the scope of the precedent.</p>
<p id="b293-9">In any event, even if some criminal defendants will be unable to challenge some precedents for the reason that Davis suggests, that provides no good reason for refusing to apply the good-faith exception. As noted, the exclusionary rule is not a personal right, see <em>Stone, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell">428 U. S., at 486, 490</a></span>, and therefore the rights of these defendants will not be impaired. And because (at least in almost all instances) the precedent can be challenged by others, Fourth Amendment ease law will not be insulated from reconsideration.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Davis v. United States.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Davis v. United States"
type: case
citation: "512 U.S. 452 (1994)"
parallel_cite: "114 S. Ct. 2350; 129 L. Ed. 2d 362"
neutral_cite: 1994 U.S. LEXIS 4827
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1994
date_decided: 1994-06-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1994-06-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Davis v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/117863/davis-v-united-states/"
  cluster_id: 117863
  opinion_id: 9433017
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Edwards v. Arizona]]", "[[Berghuis v. Thompkins]]", "[[Arizona v. Roberson]]"]
aliases: ["Davis v. United States (1994)"]
tags: ["case", "fifth-amendment", "miranda", "invocation", "right-to-counsel", "ambiguous-request"]
holding: "A suspect must invoke the right to counsel UNAMBIGUOUSLY; an equivocal or ambiguous reference (\"maybe I should talk to a lawyer\") does…"
lake:
  record_id: Davis v. United States
  status: under_review
  projected_at: 2026-07-09
---

# Davis v. United States

*512 U.S. 452 (1994)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
During a Naval Investigative Service custodial interrogation about a murder, Davis waived his rights and answered questions, then said that maybe he should talk to a lawyer. The agents asked clarifying questions; Davis said he did not want a lawyer, and questioning continued, producing incriminating statements. He moved to suppress, arguing his remark invoked his right to counsel.

## Issue
Whether an ambiguous or equivocal reference to counsel during custodial interrogation requires police to stop questioning under *[[Edwards v. Arizona]]*.

## Rule
No; the invocation of counsel must be unambiguous. "[T]he suspect must unambiguously request counsel. . . . [H]e must articulate his desire to have counsel present sufficiently clearly that a reasonable police officer in the circumstances would understand the statement to be a request for an attorney. If the statement fails to meet the requisite level of clarity, *Edwards* does not require that the officers stop questioning the suspect." — 512 U.S. 452, 459. ^pin-459

A merely ambiguous reference to a lawyer — one that a reasonable officer would understand only as a possible invocation — does not trigger the *[[Edwards v. Arizona|Edwards]]* bar, and officers are not required (though it may be good practice) to ask clarifying questions.

## Application
Davis's remark that maybe he should talk to a lawyer was, on these facts, not a clear request for counsel a reasonable officer would have understood as an invocation; indeed, when the agents sought clarification, Davis disclaimed wanting a lawyer. Because his reference was ambiguous and not an unambiguous request, the agents were not required to cease questioning, and his subsequent statements were admissible.

## Conclusion
The ambiguous reference did not invoke the right to counsel; the conviction was affirmed. Invocation of *[[Edwards v. Arizona|Edwards]]* protection requires a clear, unambiguous request.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Davis* refines [[Edwards v. Arizona]] by setting the clarity threshold for invoking counsel; [[Berghuis v. Thompkins]] later applied the same unambiguous-invocation logic to the right to remain silent.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *Davis v. United States*, 512 U.S. 452 (1994) — https://www.courtlistener.com/opinion/117863/davis-v-united-states/ — pinpoint: 459.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ae16c26336c5d383", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Davis v. United States"}, "payload": {"all": [{"cite": "513 U.S. 1008", "page": "1008", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "513"}], "display": "513 U.S. 1008", "official": {"cite": "513 U.S. 1008", "page": "1008", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "513"}, "official_selection_present": true, "record_id": "Davis v. United States"}}
{"assertion_id": "72fe4f48a1dc72d3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-459", "record_id": "Davis v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-459", "pinpoint_status": "slip-only", "quote": "--- # Davis v. United States *512 U.S. 452 (1994)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background During a Naval Investigative Service custodial interrogation about a murder, Davis waived his rights and answered questions, then said that maybe he should talk to a lawyer. The agents asked clarifying questions; Davis said he did not want a lawyer, and questioning continued, producing incriminating statements. He moved to suppress, arguing his remark invoked his right to counsel. ## Issue Whether an ambiguous or equivocal reference to counsel during custodial interrogation requires police to stop questioning under *Edwards v. Arizona*. ## Rule No; the invocation of counsel must be unambiguous.", "quote_fidelity": "mismatch", "record_id": "Davis v. United States", "star_marker": null}}
{"assertion_id": "344b32bab94c7f8d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Davis v. United States"}, "payload": {"as_of_content": "1994-06-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Davis v. United States", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Davis v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Davis v. United States",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Davis v. United States",
    "case_name_short": "Davis",
    "case_name_full": "Davis v. United States",
    "input_case_name": "Davis v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1994-06-24",
    "year": 1994,
    "docket": null,
    "cluster_id": 117863,
    "lead_opinion_id": 9433017,
    "sibling_ids": [
      117863,
      9433017,
      9433018
    ],
    "absolute_url": "/opinion/117863/davis-v-united-states/",
    "identity_method": "panel-cluster-rekey",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9148720,
        "score": 20,
        "case_name": "Davis v. United States"
      },
      {
        "cluster_id": 9147571,
        "score": 20,
        "case_name": "Davis v. United States"
      },
      {
        "cluster_id": 9147570,
        "score": 20,
        "case_name": "Davis v. United States"
      },
      {
        "cluster_id": 9147150,
        "score": 20,
        "case_name": "Davis v. United States"
      },
      {
        "cluster_id": 9147149,
        "score": 20,
        "case_name": "Davis v. United States"
      }
    ],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "512 U.S. 452",
      "volume": "512",
      "reporter": "U.S.",
      "page": "452",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "114 S. Ct. 2350",
        "volume": "114",
        "reporter": "S. Ct.",
        "page": "2350",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 L. Ed. 2d 362",
        "volume": "129",
        "reporter": "L. Ed. 2d",
        "page": "362",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1994 U.S. LEXIS 4827",
        "volume": "1994",
        "reporter": "U.S. LEXIS",
        "page": "4827",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "512 U.S. 452",
        "volume": "512",
        "reporter": "U.S.",
        "page": "452",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "114 S. Ct. 2350",
        "volume": "114",
        "reporter": "S. Ct.",
        "page": "2350",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 L. Ed. 2d 362",
        "volume": "129",
        "reporter": "L. Ed. 2d",
        "page": "362",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1994 U.S. LEXIS 4827",
        "volume": "1994",
        "reporter": "U.S. LEXIS",
        "page": "4827",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "512 U.S. 452",
    "official_selection": {
      "court_class": "scotus",
      "selected": "512 U.S. 452",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-459",
      "page": null,
      "quote": "--- # Davis v. United States *512 U.S. 452 (1994)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background During a Naval Investigative Service custodial interrogation about a murder, Davis waived his rights and answered questions, then said that maybe he should talk to a lawyer. The agents asked clarifying questions; Davis said he did not want a lawyer, and questioning continued, producing incriminating statements. He moved to suppress, arguing his remark invoked his right to counsel. ## Issue Whether an ambiguous or equivocal reference to counsel during custodial interrogation requires police to stop questioning under *Edwards v. Arizona*. ## Rule No; the invocation of counsel must be unambiguous.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1994-06-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Davis v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(9143409) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
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
        "query": "cites:(9143409)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(9143409)",
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
    "complete_query": "cites:(9143409)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 9143409,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/davis-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T02:18:01Z",
    "date_modified": "2026-07-09T23:22:52Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law",
      "panel cluster re-key -> cluster 117863 (evidence: S9 F-S9-DN-002 miskey-sweep; _run/s9/rekey-targets.jsonl 2026-07-09; stub cluster 9148721 -> merits 117863 (Davis v. United States, 512 U.S. 452, 1994))"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:20:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:20:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:20:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:20:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Davis v. United States

```
<opinion type="majority">
<author id="b504-4"><page-number citation-index="1" label="454">*454</page-number>Justice O’Connor</author>
<p id="A-h">delivered the opinion of the Court.</p>
<p id="b504-5">In <em>Edwards </em>v. Arizona, <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981), we held that law enforcement officers must immediately cease questioning a suspect who has clearly asserted his right to have counsel present during custodial interrogation. In this case we decide how law enforcement officers should respond when a suspect makes a reference to counsel that is insufficiently clear to invoke the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>prohibition on further questioning.</p>
<p id="b504-6">I</p>
<p id="b504-7">Pool brought trouble — not to River City, but to the Charleston Naval Base. Petitioner, a member of the United States Navy, spent the evening of October 2, 1988, shooting pool at a club on the base. Another sailor, Keith Shackleton, lost a game and a $30 wager to petitioner, but Shackleton refused to pay. After the club closed, Shackleton was beaten to death with a pool cue on a loading dock behind the commissary. The body was found early the next morning.</p>
<p id="b504-8">The investigation by the Naval Investigative Service (NIS) gradually focused on petitioner. Investigative agents determined that petitioner was at the club that evening, and that he was absent without authorization from his duty station the next morning. The agents also learned that only privately owned pool cues could be removed from the club premises, and that petitioner owned two cues — one of which had a bloodstain on it. The agents were told by various people that petitioner either had admitted committing the crime or had recounted details that clearly indicated his involvement in the killing.</p>
<p id="b504-9">On November 4, 1988, petitioner was interviewed at the NIS office. As required by military law, the agents advised petitioner that he was a suspect in the killing, that he was not required to make a statement, that any statement could be used against him at a trial by court-martial, and that he was entitled to speak with an attorney and have an attorney present during questioning. See Art. 31, Uniform Code of <page-number citation-index="1" label="455">*455</page-number>Military Justice (UCMJ), <span class="citation no-link">10 U.S.C. §831</span>; Mil. Rule Evid. 305; Manual for Courts-Martial A22-13 (1984). Petitioner waived his rights to remain silent and to counsel, both orally and in writing.</p>
<p id="b505-5">About an hour and a half into the interview, petitioner said, “Maybe I should talk to a lawyer.” App. 135. According to the uncontradicted testimony of one of the interviewing agents, the interview then proceeded as follows:</p>
<blockquote id="b505-6">“[We m]ade it very clear that we’re not here to violate his rights, that if he wants a lawyer, then we will stop any kind of questioning with him, that we weren’t going to pursue the matter unless we have it clarified is he asking for a lawyer or is he just making a comment about a lawyer, and he said, [‘]No, I’m not asking for a lawyer,’ and then he continued on, and said, ‘No, I don’t want a lawyer.’” <span class="citation no-link"><em>Id., </em>at 136</span>.</blockquote>
<p id="b505-7">After a short break, the agents reminded petitioner of his rights to remain silent and to counsel. The interview then continued for another hour, until petitioner said, “I think I want a lawyer before I say anything else.” <span class="citation no-link"><em>Id., </em>at 137</span>. At that point, questioning ceased.</p>
<p id="b505-8">At his general court-martial, petitioner moved to suppress statements made during the November 4 interview. The Military Judge denied the motion, holding that “the mention of a lawyer by [petitioner] during the course of the interrogation [was] not in the form of a request for counsel and . . . the agents properly determined that [petitioner] was not indicating a desire for or invoking his right to counsel.” <span class="citation no-link"><em>Id., </em>at 164</span>. Petitioner was convicted on one specification of unpremeditated murder, in violation of Art. 118, UCMJ, <span class="citation no-link">10 U. S. C. § 918</span>. He was sentenced to confinement for life, a dishonorable discharge, forfeiture of all pay and allowances, and a reduction to the lowest pay grade. The convening authority approved the findings and sentence. The Navy-<page-number citation-index="1" label="456">*456</page-number>Marine Corps Court of Military Review affirmed. App. to Pet. for Cert. 12a-15a.</p>
<p id="b506-5">The United States Court of Military Appeals granted discretionary review and affirmed. <span class="citation" data-id="8650321"><a href="/opinion/8668432/united-states-v-davis/" aria-description="Citation for case: United States v. Davis">36 M. J. 337</a></span> (1993). The court recognized that the state and federal courts have developed three different approaches to a suspect’s ambiguous or equivocal request for counsel:</p>
<blockquote id="b506-6">“Some jurisdictions have held that any mention of counsel, however ambiguous, is sufficient to require that all questioning cease. Others have attempted to define a threshold standard of clarity for invoking the right to counsel and have held that comments falling short of the threshold do not invoke the right to counsel. Some jurisdictions . . . have held that all interrogation about the offense must immediately cease whenever a suspect mentions counsel, but they allow interrogators to ask narrow questions designed to clarify the earlier statement and the [suspect’s] desires respecting counsel.” <span class="citation" data-id="8650321"><a href="/opinion/8668432/united-states-v-davis/#341" aria-description="Citation for case: United States v. Davis"><em>Id., </em>at 341</a></span> (internal quotation marks omitted).</blockquote>
<p id="b506-7">Applying the third approach, the court held that petitioner’s comment was ambiguous, and that the NIS agents properly clarified petitioner’s wishes with respect to counsel before continuing questioning him about the offense. <span class="citation" data-id="8650321"><a href="/opinion/8668432/united-states-v-davis/#341" aria-description="Citation for case: United States v. Davis"><em>Id., </em>at 341-342</a></span>.</p>
<p id="b506-8">Although we have twice previously noted the varying approaches the lower courts have adopted with respect to ambiguous or equivocal references to counsel during custodial interrogation, see <em>Connecticut </em>v. <em>Barrett, </em><span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/#529" aria-description="Citation for case: Connecticut v. Barrett">479 U. S. 523, 529-530, n. 3</a></span> (1987); <em>Smith </em>v. <em>Illinois, </em><span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#96" aria-description="Citation for case: Smith v. Illinois">469 U. S. 91, 96, n. 3</a></span> (1984) <em>(per curiam), </em>we have not addressed the issue on the merits. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./510/942/">510 U. S. 942</a></span> (1993), to do so.</p>
<p id="b506-9">II</p>
<p id="b506-10">The Sixth Amendment right to counsel attaches only at the initiation of adversary criminal proceedings, see <em>United </em><page-number citation-index="1" label="457">*457</page-number><em>States </em>v. <em>Gouveia, </em><span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/#188" aria-description="Citation for case: United States v. Gouveia">467 U. S. 180, 188</a></span> (1984), and before proceedings are initiated a suspect in a criminal investigation has no constitutional right to the assistance of counsel. Nevertheless, we held in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#469" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 469-473</a></span> (1966), that a suspect subject to custodial interrogation has the right to consult with an attorney and to have counsel present during questioning, and that the police must explain this right to him before questioning begins. The right to counsel established in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was one of a “series of recommended ‘procedural safeguards’... [that] were not themselves rights protected by the Constitution but were instead measures to insure that the right against compulsory self-incrimination was protected.” <em>Michigan </em>v. <em>Tucker, </em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#443" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 443-444</a></span> (1974); see U. S. Const., Arndt. 5 (“No person . . . shall be compelled in any criminal case to be a witness against himself”).<footnotemark>*</footnotemark></p>
<p id="b508-4"><page-number citation-index="1" label="458">*458</page-number>The right to counsel recognized in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>is sufficiently important to suspects in criminal investigations, we have held, that it “requires] the special protection of the knowing and intelligent waiver standard.” <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#483" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 483</a></span>. See <em>Oregon </em>v. <em>Bradshaw, </em><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1046" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S. 1039, 1046-1047</a></span> (1983) (plurality opinion); <span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1051" aria-description="Citation for case: Oregon v. Bradshaw"><em>id., </em>at 1051</a></span> (Powell, J., concurring in judgment). If the suspect effectively waives his right to counsel after receiving the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, law enforcement officers are free to question him. <em>North Carolina </em>v. <em>Butler, </em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#372" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369, 372-376</a></span> (1979). But if a suspect requests counsel at any time during the interview, he is not subject to further questioning until a lawyer has been made available or the suspect himself reinitiates conversation. <em>Edwards </em>v. <em>Arizona, supra, </em>at 484-485. This “second layer of prophylaxis for the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel,” <em>McNeil </em>v. <em>Wisconsin, </em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/#176" aria-description="Citation for case: McNeil v. Wisconsin">501 U. S. 171, 176</a></span> (1991), is “designed to prevent police from badgering a defendant into waiving his previously asserted <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights,” <em>Michigan </em>v. <em>Harvey, </em><span class="citation" data-id="9431937"><a href="/opinion/112385/michigan-v-harvey/#350" aria-description="Citation for case: Michigan v. Harvey">494 U. S. 344, 350</a></span> (1990). To that end, we have held that a suspect who has invoked the right to counsel cannot be questioned regarding any offense unless an attorney is actually present. <em>Minnick </em>v. <em>Mississippi, </em><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">498 U. S. 146</a></span> (1990); <em>Arizona </em>v. <em>Roberson, </em><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">486 U. S. 675</a></span> (1988). “It remains clear, however, that this prohibition on further questioning — like other aspects of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>— is not itself required by the Fifth Amendment’s prohibition on coerced confessions, but is instead justified only by reference to its prophylactic purpose.” <em>Connecticut </em>v. <span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/#528" aria-description="Citation for case: Connecticut v. Barrett"><em>Barrett, supra, </em>at 528</a></span>.</p>
<p id="b508-5">The applicability of the “ ‘rigid’ prophylactic rule” of <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>requires courts to “determine whether the accused <em>actually invoked </em>his right to counsel.” <em>Smith </em>v. <span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#95" aria-description="Citation for case: Smith v. Illinois"><em>Illinois, supra, </em>at 95</a></span> (emphasis added), quoting <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#719" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 719</a></span> (1979). To avoid difficulties of proof and to <page-number citation-index="1" label="459">*459</page-number>provide guidance to officers conducting interrogations, this is an objective inquiry. See <em>Connecticut </em>v. <span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/#529" aria-description="Citation for case: Connecticut v. Barrett"><em>Barrett, supra, </em>at 529</a></span>. Invocation of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel “requires, at a minimum, some statement that can reasonably be construed to be an expression of a desire for the assistance of an attorney.” <em>McNeil </em>v. <em>Wisconsin, </em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/#178" aria-description="Citation for case: McNeil v. Wisconsin">501 U. S., at 178</a></span>. But if a suspect makes a reference to an attorney that is ambiguous or equivocal in that a reasonable officer in light of the circumstances would have understood only that the suspect <em>might </em>be invoking the right to counsel, our precedents do not require the cessation of questioning. See <em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/" aria-description="Citation for case: McNeil v. Wisconsin">ibid.</a></span> </em>(“[T]he <em>likelihood </em>that a suspect would wish counsel to be present is not the test for applicability of <em>Edwards”); Edwards </em>v. <em>Arizona, supra, </em>at 485 (impermissible for authorities “to re-interrogate an accused in custody if he has <em>clearly asserted </em>his right to counsel”) (emphasis added).</p>
<p id="b509-5">Rather, the suspect must unambiguously request counsel. As we have observed, “a statement either is such an assertion of the right to counsel or it is not.” <em>Smith </em>v. <em>Illinois, </em><span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#97" aria-description="Citation for case: Smith v. Illinois">469 U. S., at 97-98</a></span> (brackets and internal quotation marks omitted). Although a suspect need not “speak with the discrimination of an Oxford don,” <em>post, </em>at 476 (Souter, J., concurring in judgment), he must articulate his desire to have counsel present sufficiently clearly that a reasonable police officer in the circumstances would understand the statement to be a request for an attorney. If the statement fails to meet the requisite level of clarity, <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>does not require that the officers stop questioning the suspect. See <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#433" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 433, n. 4</a></span> (1986) (“[T]he interrogation must cease until an attorney is present <em>only </em>[i]f the individual states that he wants an attorney”) (citations and internal quotation marks omitted).</p>
<p id="b509-6">We decline petitioner’s invitation to extend <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>and require law enforcement officers to cease questioning immediately upon the making of an ambiguous or equivocal reference to an attorney. See <em>Arizona </em>v. <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/#688" aria-description="Citation for case: Arizona v. Roberson"><em>Roberson, supra, </em>at 688</a></span> <page-number citation-index="1" label="460">*460</page-number>(Kennedy, J., dissenting) (“[T]he rule of <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>is our rule, not a constitutional command; and it is our obligation to justify its expansion”). The rationale underlying <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>is that the police must respect a suspect’s wishes regarding his right to have an attorney present during custodial interrogation. But when the officers conducting the questioning reasonably do not know whether or not the suspect wants a lawyer, a rule requiring the immediate cessation of questioning “would transform the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>safeguards into wholly irrational obstacles to legitimate police investigative activity,” <em>Michigan </em>v. <em>Mosley, </em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#102" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 102</a></span> (1975), because it would needlessly prevent the police from questioning a suspect in the absence of counsel even if the suspect did not wish to have a lawyer present. Nothing in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>requires the provision of counsel to a suspect who consents to answer questions without the assistance of a lawyer. In <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>itself, we expressly rejected the suggestion “that each police station must have a ‘station house lawyer’ present at all times to advise prisoners,” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 474</a></span>, and held instead that a suspect must be told of his right to have an attorney present and that he may not be questioned after invoking his right to counsel. We also noted that if a suspect is “indecisive in his request for counsel,” the officers need not always cease questioning. See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#485" aria-description="Citation for case: Miranda v. Arizona"><em>id., </em>at 485</a></span>.</p>
<p id="b510-5">We recognize that requiring a clear assertion of the right to counsel might disadvantage some suspects who — because of fear, intimidation, lack of linguistic skills, or a variety of other reasons — will not clearly articulate their right to counsel although they actually want to have a lawyer present. But the primary protection afforded suspects subject to custodial interrogation is the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings themselves. “[F]ull comprehension of the rights to remain silent and request an attorney [is] sufficient to dispel whatever coercion is inherent in the interrogation process.” <em>Moran </em>v. <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#427" aria-description="Citation for case: Moran v. Burbine"><em>Burbine, supra, </em>at 427</a></span>. A suspect who knowingly and voluntarily waives his right to counsel after having that right explained <page-number citation-index="1" label="461">*461</page-number>to him has indicated his willingness to deal with the police unassisted. Although <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>provides an additional protection — if a suspect subsequently requests an attorney, questioning must cease — it is one that must be affirmatively invoked by the suspect.</p>
<p id="b511-5">In considering how a suspect must invoke the right to counsel, we must consider the other side of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>equation: the need for effective law enforcement. Although the courts ensure compliance with the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requirements through the exclusionary rule, it is police officers who must actually decide whether or not they can question a suspect. The <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule — questioning must cease if the suspect asks for a lawyer — provides a bright line that can be applied by officers in the real world of investigation and interrogation without unduly hampering the gathering of information. But if we were to require questioning to cease if a suspect makes a statement that <em>might </em>be a request for an attorney, this clarity and ease of application would be lost. Police officers would be forced to make difficult judgment calls about whether the suspect in fact wants a lawyer even though he has not said so, with the threat of suppression if they guess wrong. We therefore hold that, after a knowing and voluntary waiver of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, law enforcement officers may continue questioning until and unless the suspect clearly requests an attorney.</p>
<p id="b511-6">Of course, when a suspect makes an ambiguous or equivocal statement it will often be good police practice for the interviewing officers to clarify whether or not he actually wants an attorney. That was the procedure followed by the NIS agents in this case. Clarifying questions help protect the rights of the suspect by ensuring that he gets an attorney if he wants one, and will minimize the chance of a confession being suppressed due to subsequent judicial second-guessing as to the meaning of the suspect’s statement regarding counsel. But we decline to adopt a rule requiring officers to ask clarifying questions. If the suspect’s state<page-number citation-index="1" label="462">*462</page-number>ment is not an unambiguous or unequivocal request for counsel, the officers have no obligation to stop questioning him.</p>
<p id="b512-5">To recapitulate: We held in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>that a suspect is entitled to the assistance of counsel during custodial interrogation even though the Constitution does not provide for such assistance. We held in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>that if the suspect invokes the right to counsel at any time, the police must immediately cease questioning him until an attorney is present. But we are unwilling to create a third layer of prophylaxis to prevent police questioning when the suspect <em>might </em>want a lawyer. Unless the suspect actually requests an attorney, questioning may continue.</p>
<p id="b512-6">The courts below found that petitioner’s remark to the NIS agents — “Maybe I should talk to a lawyer” — was not a request for counsel, and we see no reason to disturb that conclusion. The NIS agents therefore were not required to stop questioning petitioner, though it was entirely proper for them to clarify whether petitioner in fact wanted a lawyer. Because there is no ground for suppression of petitioner’s statements, the judgment of the Court of Military Appeals is</p>
<p id="b512-7">
<em>Affirmed.</em>
</p>
<footnote label="*">
<p id="b507-5">We have never had occasion to consider whether the Fifth Amendment privilege against self-incrimination, or the attendant right to counsel during custodial interrogation, applies of its own force to the military, and we need not do so here. The President, exercising his authority to prescribe procedures for military criminal proceedings, see Art. 36(a), UCMJ, <span class="citation no-link">10 U. S. C. § 836</span>(a), has decreed that statements obtained in violation of the Self-Incrimination Clause are generally not admissible at trials by court-martial. Mil. Rules Evid. 304(a) and (c)(3). Because the Court of Military Appeals has held that our cases construing the Fifth Amendment right to counsel apply to military interrogations and control the admissibility of evidence at trials by court-martial, see, <em>e. g., United States </em>v. <em>McLaren, </em><span class="citation" data-id="8650768"><a href="/opinion/8668774/united-states-v-mclaren/#115" aria-description="Citation for case: United States v. McLaren">38 M. J. 112, 115</a></span> (1993); <em>United States </em>v. <em>Applewhite, </em><span class="citation" data-id="8647228"><a href="/opinion/8666011/united-states-v-applewhite/#198" aria-description="Citation for case: United States v. Applewhite">23 M. J. 196, 198</a></span> (1987), and the parties do not contest this point, we proceed on the assumption that our precedents apply to courts-martial just as they apply to state and federal criminal prosecutions.</p>
<p id="b507-6">We also note that the Government has not sought to rely in this case on <span class="citation no-link">18 U. S. C. §3501</span>, “the statute governing the admissibility of confessions in federal prosecutions,” <em>United States </em>v. <em>Alvarez-Sanchez, </em><span class="citation" data-id="9527039"><a href="/opinion/1087948/united-states-v-alvarez-sanchez/#351" aria-description="Citation for case: United States v. Alvarez-Sanchez">511 U. S. 350, 351</a></span> (1994), and we therefore decline the invitation of some <em>amici </em>to consider it. See Brief for Washington Legal Foundation et al. as <em>Amici Curiae </em>7-14. Although we will consider arguments raised only in an <em>amicus </em>brief, see <em>Teague </em>v. <em>Lane, </em><span class="citation" data-id="9431581"><a href="/opinion/112206/teague-v-lane/#300" aria-description="Citation for case: Teague v. Lane">489 U. S. 288, 300</a></span> (1989) (plurality opinion), we are reluctant to do so when the issue is one of first impression involving <page-number citation-index="1" label="458">*458</page-number>the interpretation of a federal statute on which the Department of Justice expressly declines to take a position. See Tr. of Oral Arg. 44-47.</p>
</footnote>
</opinion>
```

---
