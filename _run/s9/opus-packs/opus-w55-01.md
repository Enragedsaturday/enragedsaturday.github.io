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

## GROUP: content/cases/United States v. Williams.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Williams
type: case
citation: "435 F.3d 1148 (2006)"
parallel_cite: ""
neutral_cite: "2006 U.S. App. LEXIS 2235; 2006 WL 213852"
court: "U.S. Court of Appeals, 9th Cir."
court_level: coa
circuit: ca9
year: 2006
date_decided: 2006-01-30
docket: 04-50182
authority_weight: "Binding in-circuit — 9th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/793121/united-states-v-tashiri-wayne-williams/"
  cluster_id: 793121
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Williams
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: Key
related:
  - "[[Miranda Waiver and Invocation]]"
  - "[[Missouri v. Seibert]]"
  - "[[Miranda v. Arizona]]"
  - "[[Oregon v. Elstad]]"
tags:
  - case
  - fifth-amendment
  - miranda
  - question-first
  - two-step-interrogation
  - midstream-warning
  - ninth-circuit
holding: "Under Missouri v. Seibert, a court must suppress a postwarning confession obtained through a deliberate two-step 'question-first' interrogation when the midstream Miranda warning was objectively ineffective at conveying to the suspect a genuine choice whether to follow up on his earlier, unwarned admission; because agents here questioned Williams until he confessed and only then gave the warning, and the district court — lacking the benefit of Seibert — never determined whether the two-step tactic was deliberate or the warning effective, the admission of the written confession was reversed."
aliases:
  - United States v. Williams
  - "United States v. Williams (9th Cir. 2006)"
---

# United States v. Williams

*435 F.3d 1148 (9th Cir. 2006)* (No. 04-50182) · U.S. Court of Appeals for the Ninth Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 793121 → lead opinion 793121 (Fisher, J.; 435 F.3d 1148, decided 2006-01-30); Rule quote string-matched to the CL opinion text 2026-07-07. Reporter star-pagination is sparse in the CL text (first marker *1151, mid-facts); the opening two-step rule is pinned to the opinion's opening reporter page (1149) — S9 to confirm 1148 vs 1149. S9 promotes. -->

## Background
Tashiri Williams filed a passport application bearing his own identifying information but the photograph of an acquaintance, Hussein Iddrissu. A fraud manager flagged the discrepancy, and Diplomatic Security Service agents brought Williams in for questioning after the building had closed. According to the investigation report, the agents interrogated Williams in two steps: they questioned him — telling him he could cooperate or be arrested and let the courts sort it out — until he orally confessed to submitting Iddrissu's photograph; only then did they read him his *[[Miranda v. Arizona|Miranda]]* rights, give him a waiver form, and ask him to write out what he had already said. The district court suppressed the unwarned oral statements as *[[Miranda v. Arizona|Miranda]]* violations but admitted the postwarning written confession as "voluntarily made." A jury convicted Williams on three counts, and he appealed the admission of the written statement.

## Issue
Whether a written confession obtained immediately after a midstream *[[Miranda v. Arizona|Miranda]]* warning must be suppressed when it followed a deliberate two-step, question-first interrogation, in light of *[[Missouri v. Seibert]]*.

## Rule
*[[Miranda v. Arizona|Miranda]]* protects the privilege against self-incrimination during custodial interrogation, and a "question-first" tactic — eliciting an unwarned confession and then warning the suspect and repeating the questions — can render the midstream warning ineffective. As the panel stated the governing rule: "a trial court must suppress postwarning confessions obtained during a deliberate two-step interrogation where the midstream *Miranda* warning was objectively ineffective." — 435 F.3d at 1149. ^pin-1149

## Application
*[[Missouri v. Seibert]]*, decided after the district court's ruling, supplied the framework the district court never applied. The relevant questions were whether the DSS agents deliberately withheld the *[[Miranda v. Arizona|Miranda]]* warning until after securing an oral confession, and, if so, whether the warning ultimately given effectively apprised Williams that he had a genuine choice whether to follow up on his earlier admission. Because the district court had ruled without the benefit of *[[Missouri v. Seibert|Seibert]]*, it made neither finding — it treated the written confession as admissible simply because it was "voluntarily made," which does not answer the distinct two-step inquiry. The Ninth Circuit therefore could not sustain the admission of the written confession on the existing record and reversed for reconsideration under the correct standard.

## Conclusion
**Reversed.** Judge Fisher wrote for the panel; the case was returned for the district court to apply the *[[Missouri v. Seibert|Seibert]]* two-step framework to the written confession.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Williams* applies *[[Missouri v. Seibert|Seibert]]*'s rule against the deliberate **question-first** interrogation: a valid-looking midstream *[[Miranda v. Arizona|Miranda]]* warning does not cure a confession if the two-step sequence was deliberate and the warning was objectively ineffective. Teach it as the boundary between *[[Missouri v. Seibert|Seibert]]* (deliberate two-step) and *[[Oregon v. Elstad|Oregon v. Elstad]]* (a good-faith, unwarned first statement not designed to circumvent *[[Miranda v. Arizona|Miranda]]*), and note that "voluntariness" alone does not resolve the two-step question.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key*

## Sources
- [*United States v. Williams*, 435 F.3d 1148 (9th Cir. 2006)](https://www.courtlistener.com/opinion/793121/united-states-v-tashiri-wayne-williams/) — pinpoint: 1149 (the *Seibert* two-step suppression rule; the CL opinion text star-paginates the F.3d reporter but the markers are sparse — the opening rule is pinned to the opinion's opening reporter page). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bceeae927edded0a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "435 F.3d 1148 (2006)", "court": "U.S. Court of Appeals, 9th Cir.", "neutral_cite": "2006 U.S. App. LEXIS 2235; 2006 WL 213852", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Williams", "year": "2006"}}
{"assertion_id": "33f46531e3fefc95", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key", "title": "United States v. Williams"}}
{"assertion_id": "4c48eef733a9dd03", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Under Missouri v. Seibert, a court must suppress a postwarning confession obtained through a deliberate two-step 'question-first' interrogation when the midstream Miranda warning was objectively ineffective at conveying to the suspect a genuine choice whether to follow up on his earlier, unwarned admission; because agents here questioned Williams until he confessed and only then gave the warning, and the district court — lacking the benefit of Seibert — never determined whether the two-step tactic was deliberate or the warning effective, the admission of the written confession was reversed.", "title": "United States v. Williams"}}
{"assertion_id": "62057cbd121b09f9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Williams", "varies_by_point": "false"}}
{"assertion_id": "87515033603e1719", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 9th Cir.", "title": "United States v. Williams"}}
```

### lake record — United States v. Williams

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Williams",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Tashiri Wayne Williams",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Tashiri Wayne WILLIAMS, Defendant-Appellant",
    "input_case_name": "United States v. Williams",
    "court": "U.S. Court of Appeals, 9th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": "2006-01-30",
    "year": 2006,
    "docket": "04-50182",
    "cluster_id": 793121,
    "lead_opinion_id": 793121,
    "sibling_ids": [],
    "absolute_url": "/opinion/793121/united-states-v-tashiri-wayne-williams/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "435 F.3d 1148",
      "volume": "435",
      "reporter": "F.3d",
      "page": "1148",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2006 U.S. App. LEXIS 2235",
        "volume": "2006",
        "reporter": "U.S. App. LEXIS",
        "page": "2235",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2006 WL 213852",
        "volume": "2006",
        "reporter": "WL",
        "page": "213852",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "435 F.3d 1148",
        "volume": "435",
        "reporter": "F.3d",
        "page": "1148",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2006 U.S. App. LEXIS 2235",
        "volume": "2006",
        "reporter": "U.S. App. LEXIS",
        "page": "2235",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2006 WL 213852",
        "volume": "2006",
        "reporter": "WL",
        "page": "213852",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "435 F.3d 1148",
    "official_selection": {
      "court_class": "coa",
      "selected": "435 F.3d 1148",
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
    "date_created": "2026-07-07T13:49:23Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:49:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:49:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:49:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:49:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-williams--793121",
      "to_record_id": "United States v. Williams",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Williams

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b1174-8">
  FISHER, Circuit Judge:
 </author>
<p id="b1174-9">
  Tashiri Williams (“Williams”) appeals a district court order denying his motion to suppress a written confession that he gave to United States Diplomatic Security Service (“DSS”) agents during interrogation. According to a DSS investigation report, the agents interrogated Williams in two steps — first, they asked him questions until he confessed; then, immediately after his oral confession, they read him his
  <em>
   Miranda
  </em>
  rights and asked him to write down what he had previously told them. The district court suppressed Williams’ oral statements because they were elicited in violation of
  <em>
   Miranda,
  </em>
  but admitted his postwarning written confession on the ground that the statement “was voluntarily made.” We reverse.
 </p>
<p id="b1174-10">
  Under the Supreme Court’s recent decision in
  <em>
   Missouri v. Seibert,
  </em>
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">542 U.S. 600</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">159 L.Ed.2d 643</a></span> (2004), rendered after the district court’s ruling, a trial court must suppress postwarning confessions obtained during a deliberate two-step interrogation where the midstream
  <em>
   Miranda
  </em>
  warning was objectively ineffective. Because the district court did not have the benefit of
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>,
  </em>
  it did not determine whether the agents deliberately withheld the
  <em>
   Miranda
  </em>
  warning, and if so, whether the warning finally given effectively apprised Williams that he had a “genuine choice whether to follow up on [his] earlier admission.”
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#616" aria-description="Citation for case: Missouri v. Seibert"><em>
   Id.
  </em>
  at 616</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Souter, J., plurality opinion). We therefore remand to the district court for further findings consistent with this opinion.
 </p>
<p id="b1174-13">
  I.
 </p>
<p id="b1174-14">
  On July 11, 2003, Williams filed a passport application at the United States Passport Office in Los Angeles, California. The application he submitted contained his own identification information, but the photographs he attached were those of his acquaintance, Hussein Iddrissu (“Iddris-su”). A fraud manager noticed the discrepancy and notified DSS agents. Four days later, when Iddrissu arrived at the Passport Office to pick up the completed passport, DSS Special Agents O’Neil and Dobbs stopped him for questioning. During questioning, they requested that Id-drissu call Williams and ask him to come to the office.
 </p>
<p id="b1174-15">
  Williams and Iddrissu’s brother, Hassan, arrived at the government building shortly after it closed, around 6 p.m. According to the investigation report (prepared by Agent Dobbs), the agents met Williams and Hassan at the building entrance, took them into the DSS offices and separated the two men for questioning. The agents escorted Williams into a reception area and began interrogating him.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  They started by showing Williams his passport appli
  <span citation-index="1" class="star-pagination" label="1151"> 
   *1151
   </span>
  cation. Williams immediately responded, “[t]hat’s not my picture.” Agent O’Neil then told Williams that he had a choice: “We can do this the easy way or the hard way.... I think we have enough to arrest you now and let the courts figure it out, or you can talk to us and tell us what’s going on and, you know, it might be better for you in the long run.” Williams complied and told the agents that he and Iddrissu had planned a joint trip to London and taken passport pictures together for the trip. The pictures, Williams explained, must have been inadvertently switched.
 </p>
<p id="b1175-5">
  Agent O’Neil called Williams’ account a “bullshit story” and described to him how criminal charges could affect his professional ambitions. In response, Williams changed his story and admitted to submitting Iddrissu’s photograph on the passport application.
 </p>
<p id="b1175-6">
  After this oral confession, Agent O’Neil read Williams his
  <em>
   Miranda
  </em>
  rights, gave him a waiver of rights form and asked him to write a statement.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  When Williams asked what he should write, both agents declined to specify, though Agent Dobbs testified that in response to such questions agents generally tell suspects that they should write “what you’ve told us.” Williams wrote: “There is nothing I can say, but I made a mistake. I just tried to get a passport without my picture for someone else. I just don’t want this to be on my record.”
 </p>
<p id="b1175-7">
  A federal grand jury indicted Williams on three counts: (1) conspiracy to make a false statement in a passport application in violation of <span class="citation no-link">18 U.S.C. § 371</span>; (2) making a false statement in a passport application in violation of <span class="citation no-link">18 U.S.C. § 1542</span>; and (3) making a false statement within the jurisdiction of the United States in violation of <span class="citation no-link">18 U.S.C. § 1001</span>. Before trial, Williams moved to suppress both his oral and his written statements. The district court granted suppression of the oral confession because “the government [had] not met its burden of showing by a preponderance of the evidence that Williams waived his
  <em>
   Miranda
  </em>
  rights before he made[the] incriminating statements” to the agents. However, the court denied Williams’ motion to suppress the written confession because neither his oral statements nor written confession were coerced and his written confession “was voluntarily made.” After trial, a jury found Williams guilty of all three felony charges and the district court sentenced him to four years of probation, including six months of home detention.
 </p>
<p id="b1175-10">
  II.
 </p>
<p id="b1175-11">
  The adequacy of a
  <em>
   Miranda
  </em>
  warning and the voluntariness of a suspect’s statements are questions of law that are reviewed de novo.
  <em>
   United States v. San Juan-Cruz,
  </em>
  <span class="citation" data-id="780271"><a href="/opinion/780271/united-states-v-isaac-san-juan-cruz/#387" aria-description="Citation for case: United States v. Isaac San Juan-Cruz">314 F.3d 384, 387</a></span> (9th Cir.2002);
  <em>
   United States v. Bautista,
  </em>
  <span class="citation" data-id="785582"><a href="/opinion/785582/united-states-v-kevin-joseph-bautista/#589" aria-description="Citation for case: United States v. Kevin Joseph Bautista">362 F.3d 584, 589</a></span> (9th Cir.2004). “The admission of statements made in violation of a person’s
  <em>
   Miranda
  </em>
  rights is reviewed for harmless error.”
  <em>
   United States v. Butler,
  </em>
  <span class="citation" data-id="773222"><a href="/opinion/773222/united-states-v-rogers-butler-jr/#1098" aria-description="Citation for case: United States v. Rogers Butler, Jr.">249 F.3d 1094, 1098</a></span> (9th Cir.2001).
 </p>
<p id="b1175-12">
  III.
 </p>
<p id="b1175-13">
  “In order to combat [the pressures inherent in custodial interrogation] and to permit a full opportunity to exercise the privilege against self-incrimination, the accused must be adequately and effectively apprised of his rights.”
  <em>
   Miranda v. Ari
  </em>
<span citation-index="1" class="star-pagination" label="1152"> 
   *1152
   </span>
<em>
   zona,
  </em>
  <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U.S. 436, 467</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L.Ed.2d 694</a></span> (1966). A
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning functions both to reduce the risk that an involuntary or coerced statement will be admitted at trial and to implement the Fifth Amendment’s self-incrimination clause.
  <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#457" aria-description="Citation for case: Miranda v. Arizona"><em>
   Id.
  </em>
  at 457-58</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602</a></span>;
  <em>
   see also Chavez v. Martinez,
  </em>
  <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#790" aria-description="Citation for case: Chavez v. Martinez">538 U.S. 760, 790</a></span>, <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/" aria-description="Citation for case: Chavez v. Martinez">123 S.Ct. 1994</a></span>, <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/" aria-description="Citation for case: Chavez v. Martinez">155 L.Ed.2d 984</a></span> (2003) (Kennedy, J., concurring in part and dissenting in part). Thus, if a suspect in custody does not receive an adequate warning effectively apprising him of his rights before he incriminates himself, his statements may not be admitted as evidence against him.
  <em>
   Miranda,
  </em>
  <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona">384 U.S. at 479</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602</a></span>. Williams contends that the midinterrogation
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning he received did not adequately apprise him of his rights and therefore his written confession should not have been admitted.
 </p>
<p id="b1176-4">
  A.
 </p>
<p id="b1176-5">
  The Supreme Court has twice addressed the admissibility of a confession obtained after a
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning but preceeded by the suspect’s earlier,
  <em>
   unwarned
  </em>
  incriminating statements. In
  <em>
   Oregon v. Elstad,
  </em>
  <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#301" aria-description="Citation for case: Oregon v. Elstad">470 U.S. 298, 301</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">84 L.Ed.2d 222</a></span> (1985), Elstad, a burglary suspect, made incriminating comments to a police officer at his home without first receiving a
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning. Officers then took him to the county sheriffs office, placed him in an interrogation room, read him his
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  rights and questioned him at length.
  <em>
   See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">id.</a></span>
  </em>
  During this interrogation, and approximately 30 minutes after making his original inculpatory comments, Elstad expanded significantly on his earlier statements and made a full confession.
  <em>
   Id.
  </em>
  at 301-02, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span>.
 </p>
<p id="b1176-9">
  Before the Supreme Court, Elstad argued that his confession should be suppressed as “fruit of the poisonous tree” because, although made after a proper
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning, his confession was tainted by the earlier unwarned comments.
  <em>
   Id.
  </em>
  at 303, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span>. In a related argument, Elstad asserted that the coercive impact of his unwarned statement — inherent in a defendant’s having “let the cat out of the bag” — required suppression because the statement compromised the voluntariness of his postwarning statement.
  <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#302" aria-description="Citation for case: Oregon v. Elstad"><em>
   Id.
  </em>
  at 302-04</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span>. Focusing on the voluntariness of Elstad’s unwarned comments, the Court rejected both arguments.
  <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#306" aria-description="Citation for case: Oregon v. Elstad"><em>
   Id.
  </em>
  at 306-14</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span>. The Court reasoned that “absent deliberately coercive or improper tactics in obtaining the initial statement, the mere fact that a suspect has made an unwarned admission does not warrant a presumption of compulsion” with respect to the postwarning confession.
  <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#314" aria-description="Citation for case: Oregon v. Elstad"><em>
   Id.
  </em>
  at 314</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span>. Rather, “[ojnce warned, the suspect is free to exercise his own volition in deciding whether or not to make a statement to the authorities.”
  <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#308" aria-description="Citation for case: Oregon v. Elstad"><em>
   Id.
  </em>
  at 308</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span>. The Court thus held that a “suspect who has once responded to unwarned yet uncoercive questioning is not thereby disabled from waiving his rights and confessing after he has been given the requisite
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warnings.”
  <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#318" aria-description="Citation for case: Oregon v. Elstad"><em>
   Id
  </em>
  at 318, 105 S.Ct. 1285</a></span>.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b1177-4">
<span citation-index="1" class="star-pagination" label="1153"> 
   *1153
   </span>
  As Justice O’Connor explained in her
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  dissent,
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>
  </em>
  also held that “if [the prewarning] statement is shown to have been
  <em>
   involuntary,
  </em>
  the - court must examine whether the taint dissipated through the passing of time or a change in circumstances.”
  <em>
   Seibert,
  </em>
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#628" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 628</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (emphasis added).
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  Similarly,
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>
  </em>
  requires the court to suppress a postwarning statement if the suspect demonstrates that his statement was involuntary despite the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning.
  <em>
   Elstad,
  </em>
  <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#318" aria-description="Citation for case: Oregon v. Elstad">470 U.S. at 318</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span> (explaining that “the finder of fact must examine the surrounding circumstances and the entire course of police conduct with respect to the suspect in evaluating the voluntariness of his statements”). Thus, under
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>,
  </em>
  if the prewarning statement was voluntary (or if involuntary, 'the change in time and circumstances dissipated the taint), then the postwarning confession is admissible unless it was involuntarily made despite the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning.
  <em>
   See United States v. Wauneka,
  </em>
  <span class="citation" data-id="457572"><a href="/opinion/457572/united-states-v-allen-wauneka/#1440" aria-description="Citation for case: United States v. Allen Wauneka">770 F.2d 1434, 1440</a></span> (9th Cir.1985);
  <em>
   accord United States v. Stewart,
  </em>
  <span class="citation" data-id="788327"><a href="/opinion/788327/united-states-v-timothy-stewart/#1090" aria-description="Citation for case: United States v. Timothy Stewart">388 F.3d 1079, 1090</a></span> (7th Cir.2004).
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
</p>
<p id="b1177-10">
  We followed
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>
  </em>
  in
  <em>
   United States v. Orso,
  </em>
  <span class="citation" data-id="9494408"><a href="/opinion/775079/united-states-v-jody-myesha-orso/" aria-description="Citation for case: United States v. Jody Myesha Orso">266 F.3d 1030</a></span> (9th Cir.2001) (en banc). Orso made inculpatory statements in a patrol car en route to a police station and then, immediately upon arriving at the station, received a
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning and confessed. <span class="citation" data-id="9494408"><a href="/opinion/775079/united-states-v-jody-myesha-orso/#1032" aria-description="Citation for case: United States v. Jody Myesha Orso">266 F.3d at 1032-33</a></span>. Pointing to
  <em>
   Elstad’s
  </em>
  disjunctive clause, “[a]bsent deliberately coercive or improper tactics,” Orso argued that her postwarning statements, should be suppressed because the officers engaged in improper tactics (questioning her during the car ride without
  <span citation-index="1" class="star-pagination" label="1154"> 
   *1154
   </span>
  giving a
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning), which “tainted” her warned confession.
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span>
  </em>
  at 1034-36 (quoting
  <em>
   Elstad,
  </em>
  <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#314" aria-description="Citation for case: Oregon v. Elstad">470 U.S. at 314</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span>). We declined to distinguish
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>.
  </em>
  Reasoning that “the overriding theme running through
  <em>
   [.Elstad
  </em>
  ] is the voluntariness of the unwarned statement,” we held that where a suspect’s initial, unwarned statements are voluntary, her subsequent, warned statements are admissible regardless of alleged improper police tactics.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
<em>
   Id.
  </em>
  at 1036, 1038. “[T]he most persuasive reading of the ‘improper tactics’ passage [of
  <em>
   Elstad],”
  </em>
  we explained, “is that the Court simply meant to connect such police conduct to the potential involuntariness of the unwarned statements.”
  <em>
   Id.
  </em>
  at 1037. Thus,
  <em>
   <span class="citation" data-id="9494408"><a href="/opinion/775079/united-states-v-jody-myesha-orso/" aria-description="Citation for case: United States v. Jody Myesha Orso">Orso</a></span>
  </em>
  held that where a postwarning statement is voluntarily made, the “warned confession should ... be suppressed only if [the pre-warning statements] were involuntary, and any taint therefrom had not dissipated by the time [the suspect] was read the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warnings.”
  <em>
   Id.
  </em>
  at 1039.
 </p>
<p id="b1178-4">
  B.
 </p>
<p id="b1178-5">
  At issue in
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  was the admissibility of a confession obtained by the use of a two-step interrogation strategy, termed “question-first,” that called for the deliberate with-holding of the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning until the suspect confessed, followed by a
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning and a repetition of the confession already given. <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#604" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 604, 609-11</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>(Souter, J., plurality opinion). As the facts in
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  make clear, “[t]he object of [the] question-first [tactic] is to render
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warnings ineffective by waiting for a particularly opportune time to give them, after the suspect has already confessed.”
  <em>
   Id.
  </em>
  at 611, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>;
  <em>
   see also Orso,
  </em>
  <span class="citation" data-id="9494408"><a href="/opinion/775079/united-states-v-jody-myesha-orso/#1043" aria-description="Citation for case: United States v. Jody Myesha Orso">266 F.3d at 1043-44</a></span> (Paez, J., concurring) (the fact that the interrogating officer deliberately withheld the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning “deprived Orso of information that was indispensable to her exercise of free will”).
 </p>
<p id="b1178-8">
  Like defendants Elstad and Orso, Sei-bert made incriminating statements both before and after receiving a
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning. Officers awakened Seibert, suspected of murdering a teenager in a mobile home fire, at 3 a.m. and drove her to a police station where one officer, who later testified that he was explicitly instructed not to provide a
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning at this point, interrogated her for 30 to 40 minutes until she confessed.
  <em>
   Seibert,
  </em>
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#604" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 604-05</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>. Immediately after Seibert confessed, she was given a 20-minute coffee and cigarette break.
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#605" aria-description="Citation for case: Missouri v. Seibert"><em>
   Id.
  </em>
  at 605</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>. Officer Hanrahan then turned on a tape recorder, gave her a
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning and resumed questioning:
 </p>
<blockquote id="b1178-9">
  Hanrahan: “ ‘Trice, didn’t you tell me that he was supposed to die in his sleep?”
 </blockquote>
<blockquote id="b1178-10">
  Seibert: “If that would happen, ‘cause he was on that new medicine, you know
 </blockquote>
<blockquote id="b1178-11">
  Hanrahan: “The Prozac? And it makes him sleepy. So he was supposed to die in his sleep?”
 </blockquote>
<blockquote id="b1178-12">
  Seibert: “Yes.”
 </blockquote>
<p id="b1178-13">
<em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span>
  </em>
  As in
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>,
  </em>
  the trial court suppressed the prewarning statements but admitted the postwarning confession.
  <em>
   See id.
  </em>
  at 606, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>.
 </p>
<p id="b1178-14">
  Five Justices of the Supreme Court, however, found
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  distinguishable from
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>
  </em>
  even though Seibert’s pre-warning statements were, like Elstad’s, uncoerced and made voluntarily. Justice Souter, joined in a plurality by Justices Stevens, Ginsburg and Breyer, and Justice Kennedy concurring separately, voted to suppress Seibert’s self-incriminating statements, despite the fact that she gave them
  <span citation-index="1" class="star-pagination" label="1155"> 
   *1155
   </span>
  after receiving her
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning and ostensibly waiving her rights.
  <em>
   See id.
  </em>
  at 609, 616-17, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Souter, J., plurality opinion) (acknowledging that a
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning largely guarantees the admissibility of confessions);
  <em>
   id.
  </em>
  at 618, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Kennedy, J., concurring in the judgment). Contrary to
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>,
  </em>
  these Justices acknowledged that some two-step interrogations yield inadmissible statements even in the absence of coercion. They were therefore unwilling to permit interrogators to exploit the mere form of the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning while depriving it of any meaningful substance. As Justice Souter explained, the circumstances of Sei-bert’s interrogation “challeng[ed] the comprehensibility and efficacy of the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warnings to the point that a reasonable person in the suspect’s shoes would not have understood them to convey a message that she retained a choice about continuing to talk.”
  <em>
   Id.
  </em>
  at 617, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Souter, J., plurality opinion). Justice Kennedy agreed, stating that a two-step interrogation technique “designed to circumvent
  <em>
   Miranda," id.
  </em>
  at 618, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>, “simply creates too high a risk that postwarning statements will be obtained when a suspect was deprived of knowledge essential to his ability to understand the nature of his rights and the consequences of abandoning them.”
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#621" aria-description="Citation for case: Missouri v. Seibert"><em>
   Id.
  </em>
  at 621</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Kennedy, J., concurring in the judgment) (internal quotation marks omitted).
 </p>
<p id="b1179-5">
  Although five Justices agreed that Sei-bert’s postwarning statement was inadmissible, the case did not produce a majority opinion. According to the plurality, when interrogators question first and warn later, the threshold inquiry is “whether it would be reasonable to find that in these circumstances the warnings could function ‘effectively’ as
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  requires.”
  <em>
   Seibert,
  </em>
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#611" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 611-12</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>. The plurality therefore focused on several objective factors to determine whether the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning given in each case fulfilled the function of advising the suspect that he or she had “a real choice about giving an admissible statement” during the second stage of interrogation.
  <em>
   Id.
  </em>
  at 612, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>.
 </p>
<blockquote id="b1179-8">
  The contrast between
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>
  </em>
  and
  <em>
   [Sei-
  </em>
  bert] reveals a series of relevant facts that bear on whether
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warnings delivered midstream could be effective enough to accomplish their object: the completeness and detail of the questions and answers in the first round of interrogation, the overlapping content of the two statements, the timing and setting of the first and the second, the continuity of police personnel, and the degree to which the interrogator’s questions treated the second round as continuous with the first.
 </blockquote>
<p id="b1179-9">
<em>
   Id.
  </em>
  at 615, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>. The plurality reasoned that the interrogation of Elstad at the police station “present[ed] a markedly different experience” — separate in time, location and tone — from the brief interaction at Elstad’s home; as a result, the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning given at the station offered Elstad a “genuine choice whether to follow up on [his] earlier admission.”
  <em>
   Id.
  </em>
  at 615-16, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>.
 </p>
<p id="b1179-10">
  In
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>,
  </em>
  by contrast, officers interrogated Seibert at length before giving the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning and gave her only a short break without any change of location after she confessed, and then the same officer from the prewarning interrogation expressly used her unwarned statements to obtain a warned confession.
  <em>
   Id.
  </em>
  at 616, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>. In the plurality’s view, these facts
  <em>
   “by any objective measure
  </em>
  revealed] a police strategy adapted to undermine the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warnings.”
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span>
  </em>
  (emphasis added).
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  In determining whether
  <span citation-index="1" class="star-pagination" label="1156"> 
   *1156
   </span>
  the warning was effective, the plurality expressly stated that the “focus is on facts apart from [the interrogator’s] intent that show the question-first tactic at work.”
  <em>
   Id.
  </em>
  at 616-17, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#6" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601 n. 6</a></span>. Because the facts in
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  did not “reasonably support a conclusion that the warnings given could have served them purpose,” the plurality held that Seibert’s postwarn-ing statements were inadmissible.
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#617" aria-description="Citation for case: Missouri v. Seibert"><em>
   Id.
  </em>
  at 617</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>.
 </p>
<p id="b1180-4">
  Although Justice Kennedy agreed that
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  could be distinguished from
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>,
  </em>
  he viewed the plurality’s test for admissibility as “eut[ting] too broadly” because the objective inquiry into a midstream
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning’s effectiveness applied “to every two-stage interrogation.”
  <em>
   Id.
  </em>
  at 621-22, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>. At the same time, he recognized that in Seibert’s case, the police withheld the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning “to obscure both the practical and legal significance of the admonition when finally given.”
  <em>
   Id.
  </em>
  at 620, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>. To avoid undermining
  <em>
   Miranda’s
  </em>
  “clarity,” Justice Kennedy would also evaluate the effectiveness of a midstream warning using an
  <em>
   objective
  </em>
  inquiry, but only in cases in which the police
  <em>
   deliberately
  </em>
  employed the two-step strategy to undermine
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>:
  </em>
</p>
<blockquote id="AebG">
  If the deliberate two-step strategy has been used, postwarning statements that are related to the substance of prewarn-ing statements must be excluded unless curative measures are taken before the postwarning statement is made. Cura-five measures should be designed to ensure that a
  <em>
   reasonable person in the suspect’s situation would understand the import and effect of the
  </em>
  Miranda
  <em>
   warning and of the
  </em>
  Miranda
  <em>
   waiver.
  </em>
  For example, a substantial break in time and circumstances between the prewarn-ing statement and the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning may suffice in most circumstances.... Alternatively, an additional warning that explains the likely inadmissibility of the prewarning custodial statement may be sufficient.
 </blockquote>
<p id="b1180-7">
<em>
   Id.
  </em>
  at 622, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (emphasis added). However, absent a showing that the law enforcement officers deliberately used the question-first tactic to lessen the warning’s effectiveness, Justice Kennedy would apply
  <em>
   Elstad’s
  </em>
  voluntariness standards to determine whether the postwarning confession is admissible.
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#622" aria-description="Citation for case: Missouri v. Seibert"><em>
   Id.
  </em>
  at 622</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>. Because the officers in
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  deliberately employed the question-first technique and then took no curative measures to ensure that the midstream warning effectively apprised Seibert of her rights, Justice Kennedy joined the plurality in concluding that Seibert’s postwarning statement was inadmissible.
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Id.</a></span>
  </em>
<a class="footnote" href="#fn8" id="fn8_ref">
<em>
    8
   </em>
</a>
</p>
<p id="b1180-8">
  Justice O’Connor, writing for the four dissenting Justices, disagreed with the majority’s conclusion that
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>
  </em>
  could be distinguished, but agreed with the plurality that Justice Kennedy’s proposed “intent-based test” should not be applied.
  <em>
   Id.
  </em>
  at 622-29 (O’Connor, J., dissenting). In
  <span citation-index="1" class="star-pagination" label="1157"> 
   *1157
   </span>
  addition, the dissenting Justices viewed the objective inquiry into the midstream warning’s effectiveness as “inform[ing] the
  <em>
   psychological
  </em>
  judgment regarding whether the suspect has been informed effectively of her right to remain silent.”
  <em>
   Id.
  </em>
  at 624, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>. Because they viewed this inquiry as relying on the theory that the “lingering compulsion” of the unwarned statement requires suppression of the postwarning statement — which
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>
  </em>
  rejected — the dissenting Justices would have evaluated the two-step interrogation procedure under
  <em>
   Elstad’s
  </em>
  voluntariness standards.
  <em>
   Id.
  </em>
  at 627-28, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>.
 </p>
<p id="b1181-5">
  C.
 </p>
<p id="b1181-6">
  To determine whether Williams’ confession falls within the exception to
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>
  </em>
  carved out in
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>,
  </em>
  we must first decide how to interpret
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  in light of these splintered opinions. This is a question of first impression in this circuit, although Judge Berzon has provided thoughtful guidance in a recent dissenting opinion.
  <em>
   See United States v. Rodriguez-Preciado,
  </em>
  <span class="citation" data-id="9497799"><a href="/opinion/789441/united-states-v-antonio-rodriguez-preciado-aka-tony-rodriguez-preciado/#1138" aria-description="Citation for case: United States v. Antonio Rodriguez-Preciado, AKA Tony...">399 F.3d 1118, 1138-43</a></span> (9th Cir.2005) (Berzon, J., dissenting).
 </p>
<p id="b1181-7">
  Ordinarily, “[w]hen a fragmented Court decides a case and no single rationale explaining the result enjoys the assent of five Justices, the holding of the Court may be viewed as that position taken by those Members who concurred in the judgments on the narrowest grounds.”
  <em>
   Marks v. United States,
  </em>
  <span class="citation" data-id="9004890"><a href="/opinion/9011945/marks-v-united-states/#193" aria-description="Citation for case: Marks v. United States">430 U.S. 188, 193</a></span>, <span class="citation" data-id="109611"><a href="/opinion/109611/marks-v-united-states/" aria-description="Citation for case: Marks v. United States">97 S.Ct. 990</a></span>, <span class="citation" data-id="109611"><a href="/opinion/109611/marks-v-united-states/" aria-description="Citation for case: Marks v. United States">51 L.Ed.2d 260</a></span> (1977) (citation and internal quotation marks omitted). We need not find a legal opinion which a majority joined, but merely “a legal standard which, when applied, will necessarily produce results with which a majority of the Court from that case would agree.”
  <em>
   Planned Parenthood v. Casey,
  </em>
  <span class="citation" data-id="8995225"><a href="/opinion/9002635/planned-parenthood-v-casey/#693" aria-description="Citation for case: Planned Parenthood v. Casey">947 F.2d 682, 693</a></span> (3d Cir.1991),
  <em>
   aff'd in part and rev’d in part on other grounds,
  </em>
  <span class="citation" data-id="9432680"><a href="/opinion/112786/planned-parenthood-of-southeastern-pa-v-casey/" aria-description="Citation for case: Planned Parenthood of Southeastern Pa. v. Casey">505 U.S. 833</a></span>, <span class="citation" data-id="9432680"><a href="/opinion/112786/planned-parenthood-of-southeastern-pa-v-casey/" aria-description="Citation for case: Planned Parenthood of Southeastern Pa. v. Casey">112 S.Ct. 2791</a></span>, <span class="citation" data-id="9432680"><a href="/opinion/112786/planned-parenthood-of-southeastern-pa-v-casey/" aria-description="Citation for case: Planned Parenthood of Southeastern Pa. v. Casey">120 L.Ed.2d 674</a></span> (1992);
  <em>
   see also Smith v. Univ. of Wash. Law Sch.,
  </em>
  <span class="citation" data-id="771312"><a href="/opinion/771312/katuria-e-smith-angela-rock-michael-pyle-for-themselves-and-all-others/#1200" aria-description="Citation for case: Katuria E. Smith Angela Rock Michael Pyle for Themselves...">233 F.3d 1188, 1200</a></span> (9th Cir.2000) (concluding that Justice Powell’s analysis in
  <em>
   Bakke
  </em>
  is “the narrowest footing upon which a race-conscious decision making process could stand”);
  <em>
   King v. Palmer,
  </em>
  <span class="citation" data-id="9843062"><a href="/opinion/573058/mabel-a-king-v-james-f-palmer-director-dc-department-of-corrections/#781" aria-description="Citation for case: Mabel A. King v. James F. Palmer, Director, D.C....">950 F.2d 771, 781-82</a></span> (D.C.Cir.1991) (en banc) (explaining that “the narrowest opinion must represent a common denominator of the Court’s reasoning”).
  <a class="footnote" href="#fn9" id="fn9_ref">
   9
  </a>
  To determine whether
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  contains a precedential holding, we must identify and apply a test which satisfies the requirements of both Justice Souter’s plurality opinion and Justice Kennedy’s concurrence.
 </p>
<p id="b1181-10">
  Applying the
  <em>
   Marks
  </em>
  rule to
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>,
  </em>
  we hold that a trial court must suppress postwarning confessions obtained during a deliberate two-step interrogation where the midstream
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning — in light of the objective facts and circumstances— did not effectively apprise the suspect of his rights. Although the plurality would consider all two-stage interrogations eligible for a
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  inquiry, Justice Kennedy’s opinion narrowed the
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  exception to those cases involving deliberate use of the two-step procedure to weaken
  <em>
   Miranda’s
  </em>
  protections.
  <em>
   See Rodriguez-Preciado,
  </em>
  <span class="citation" data-id="9497799"><a href="/opinion/789441/united-states-v-antonio-rodriguez-preciado-aka-tony-rodriguez-preciado/#1139" aria-description="Citation for case: United States v. Antonio Rodriguez-Preciado, AKA Tony...">399 F.3d at 1139</a></span> (Berzon, J., dissenting) (“Justice Kennedy concurred in
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  on a ground arguably narrower than that relied upon by the plurality.”);
  <em>
   United States v. Kiam,
  </em>
  <span class="citation" data-id="792714"><a href="/opinion/792714/united-states-v-long-tong-kiam/#532" aria-description="Citation for case: United States v. Long Tong Kiam">432 F.3d 524, 532</a></span> (3d Cir.2006) (stating that the Third Circuit “applies the
 </p>
<p id="b1182-3">
<span citation-index="1" class="star-pagination" label="1158"> 
   *1158
   </span>
<em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  plurality opinion as narrowed by Justice Kennedy”);
  <em>
   United States v. Briones,
  </em>
  <span class="citation" data-id="788484"><a href="/opinion/788484/united-states-of-america-plaintiffappellee-v-eriberto-melesio-briones/#613" aria-description="Citation for case: UNITED STATES OF AMERICA, PLAINTIFF—APPELLEE v. ERIBERTO...">390 F.3d 610, 613-14</a></span> (8th Cir.2004) (explaining that the “first step” in Justice Kennedy’s “narrower test” is “to determine whether a [two-step] interrogation process was used as a deliberate strategy”);
  <em>
   Stewart,
  </em>
  <span class="citation" data-id="788327"><a href="/opinion/788327/united-states-v-timothy-stewart/#1090" aria-description="Citation for case: United States v. Timothy Stewart">388 F.3d at 1090</a></span>(“Justice Kennedy thus provided a fifth vote to depart from
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>,
  </em>
  but only where the police set out deliberately to withhold
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warnings until after a confession has been secured.”). In other words, both the plurality and Justice Kennedy agree that where law enforcement officers
  <em>
   deliberately
  </em>
  employ a two-step interrogation to obtain a confession and where separations of time and circumstance and additional curative warnings are absent or fail to apprise a
  <em>
   reasonable person
  </em>
  in the suspect’s shoes of his rights, the trial court should suppress the confession.
  <a class="footnote" href="#fn10" id="fn10_ref">
   10
  </a>
  This narrower test — that excludes confessions made after a deliberate, objectively ineffective mid-stream warning — represents
  <em>
   Seibert’s
  </em>
  holding. In situations where the two-step strategy was not deliberately employed,
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>
  </em>
  continues to govern the admissibility of postwarning statements.
  <em>
   See also United States v. Mashburn,
  </em>
  <span class="citation" data-id="790073"><a href="/opinion/790073/united-states-v-eric-kevin-mashburn/#309" aria-description="Citation for case: United States v. Eric Kevin Mashburn">406 F.3d 303, 309</a></span> (4th Cir.2005) (“The admissibility of postwarning statements is governed by
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>
  </em>
  unless the deliberate ‘question-first’ strategy is employed.”);
  <em>
   Briones,
  </em>
  <span class="citation" data-id="788484"><a href="/opinion/788484/united-states-of-america-plaintiffappellee-v-eriberto-melesio-briones/#614" aria-description="Citation for case: UNITED STATES OF AMERICA, PLAINTIFF—APPELLEE v. ERIBERTO...">390 F.3d at 614</a></span> (applying
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>
  </em>
  after determining that law enforcement officers did not use a “deliberate strategy” of two-step interrogation to circumvent Miranda);
  <em>
   Stewart,
  </em>
  <span class="citation" data-id="788327"><a href="/opinion/788327/united-states-v-timothy-stewart/#1090" aria-description="Citation for case: United States v. Timothy Stewart">388 F.3d at 1090</a></span> (“Where the initial violation of
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  was not part of a deliberate strategy to undermine the warnings,
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>
  </em>
  appears to have survived
  <em>
   Seibert.”).
  </em>
</p>
<p id="b1182-6">
  1.
  <em>
   Determining Deliberateness
  </em>
</p>
<p id="A3F">
  As an initial matter, we note that Justice Kennedy did not articulate how a court should determine whether an interrogator used a deliberate two-step strategy.
  <a class="footnote" href="#fn11" id="fn11_ref">
   11
  </a>
  Justice Kennedy envisioned a deliberateness test that focuses on intent, but as the plurality noted, “the intent of the officer will rarely be as candidly admitted as it was here.”
  <em>
   Seibert,
  </em>
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#617" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 617</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#6" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601 n. 6</a></span> (Souter, J., plurality opinion). Consistent with our sister circuits, we hold that in determining whether the interrogator deliberately withheld the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning, courts should consider whether objective evidence and any available subjective evidence, such as an officer’s testimony, support an inference that the two-step interrogation procedure was used to undermine the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning.
  <a class="footnote" href="#fn12" id="fn12_ref">
   12
  </a>
<em>
   See id.
  </em>
  at 616, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>(Sout-er, J., plurality opinion) (concluding that the facts present in
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  “by any objective measure reveal a police strategy
  <span citation-index="1" class="star-pagination" label="1159"> 
   *1159
   </span>
  adapted to undermine the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warnings.”);
  <em>
   see also Briones,
  </em>
  <span class="citation" data-id="788484"><a href="/opinion/788484/united-states-of-america-plaintiffappellee-v-eriberto-melesio-briones/#614" aria-description="Citation for case: UNITED STATES OF AMERICA, PLAINTIFF—APPELLEE v. ERIBERTO...">390 F.3d at 614</a></span> (examining objective evidence in the record to conclude that interrogators did not use a deliberate strategy of two-step interrogations). Such objective evidence would include the timing, setting and completeness of the prewarning interrogation, the continuity of police personnel and the overlapping content of the pre- and post-warning statements.
  <span class="citation" data-id="788484"><a href="/opinion/788484/united-states-of-america-plaintiffappellee-v-eriberto-melesio-briones/#615" aria-description="Citation for case: UNITED STATES OF AMERICA, PLAINTIFF—APPELLEE v. ERIBERTO..."><em>
   Id.
  </em>
  at 615</a></span> (Souter, J., plurality opinion);
  <em>
   see also id.
  </em>
  at 621 (Kennedy, J., concurring in the judgment) (describing the overlapping content of Sei-bert’s two confessions as evidence of “the temptations for abuse inherent in the two-step technique”).
  <a class="footnote" href="#fn13" id="fn13_ref">
   13
  </a>
  By focusing on both “facts apart from intent that show the question-first tactic at work,”
  <em>
   Seibert,
  </em>
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#616" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 616-17</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#6" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601 n. 6</a></span> (Souter, J., plurality opinion), and any available subjective evidence of deliberateness, courts will better ensure that law enforcement officers do not circumvent the Fifth Amendment right against self-incrimination through the use of “interrogation practices ... likely ... to disable [an individual] from making a free and rational choice” about speaking.
  <em>
   Miranda,
  </em>
  <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#464" aria-description="Citation for case: Miranda v. Arizona">384 U.S. at 464-65</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602</a></span>.
 </p>
<p id="b1183-5">
  Once a law enforcement officer has detained a suspect
  <em>
   and subjects him to interrogation
  </em>
  — as was the case in
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  and is the case here — there is rarely, if ever, a legitimate reason to delay giving a
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning until after the suspect has confessed.
  <a class="footnote" href="#fn14" id="fn14_ref">
   14
  </a>
  Instead, the most plausible reason for the delay is an
  <em>
   illegitimate
  </em>
  one, which is the interrogator’s desire to weaken the warning’s effectiveness. As Justice Souter explained:
 </p>
<blockquote id="b1183-8">
  By any objective measure ... it is likely that if the interrogators employ the technique of withholding warnings until after interrogation succeeds in eliciting a confession, the warnings will be ineffective in preparing the suspect for successive interrogation, close in time and similar in content. After all, the reason that question-first is catching on is as obvious as its manifest purpose, which is to get a confession the suspect would not make if he understood his rights at the outset; the sensible underlying assumption is that with one confession in hand before the warnings, the interrogator can count on getting its duplicate, with trifling additional trouble.
 </blockquote>
<p id="b1183-9">
<em>
   Seibert,
  </em>
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#613" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 613</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Souter, J., plurality opinion). Justice Kennedy agreed: “the two-step technique permits the accused to conclude that the right not to respond did not exist when the earlier incriminating statements were made. The strategy is based on the assumption that
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warnings will tend
  <span citation-index="1" class="star-pagination" label="1160"> 
   *1160
   </span>
  to mean less when recited midinterrogation, after inculpatory statements have already been obtained.”
  <em>
   Id.
  </em>
  at 620, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Kennedy, J., concurring in the judgment). Because law enforcement officers generally retain control over the timing of a
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning and giving the warning to a custodial suspect imposes only a minimal burden, the officer’s deferral of the warning until after a suspect’s incriminating response further supports an inference of deliberateness.
 </p>
<p id="b1184-4">
  In sum, when a law enforcement officer interrogates a suspect but does not give a
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning until after obtaining a confession or an incriminating statement, a court in deciding whether to suppress a subsequent, postwarning confession must determine whether the warning was deliberately withheld. The court should consider any objective evidence or available expressions of subjective intent suggesting that the officer acted deliberately to undermine and obscure the warning’s meaning and effect.
 </p>
<p id="b1184-5">
  2.
  <em>
   Determining Effectiveness
  </em>
</p>
<p id="b1184-6">
  When an interrogator has deliberately employed the two-step strategy,
  <em>
   Sei-bert
  </em>
  requires the court then to evaluate the effectiveness of the midstream
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning to determine whether the post-warning statement is admissible.
  <em>
   Seibert,
  </em>
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#615" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 615</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Souter, J., plurality opinion);
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#622" aria-description="Citation for case: Missouri v. Seibert"><em>
   id.
  </em>
  at 622</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Kennedy, J., concurring in the judgment). The court must determine, based on objective evidence, whether the midstream warning adequately and effectively apprised the suspect that he had a “genuine choice whether to follow up on [his] earlier admission.”
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#616" aria-description="Citation for case: Missouri v. Seibert"><em>
   Id.
  </em>
  at 616</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Souter, J., plurality opinion). In its analysis, the court should look both to the objective circumstances the plurality cited as “bearing] on whether
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warnings delivered midstream could be effective enough to accomplish their object,”
  <em>
   id.
  </em>
  at 615, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Souter, J., plurality opinion), and to the curative measures characterized by Justice Kennedy as “designed to ensure that a reasonable person in the suspect’s situation would understand the import and effect of the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning,”
  <em>
   id.
  </em>
  at 622, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>(Kennedy, J., concurring in the judgment).
  <em>
   See also Stewart,
  </em>
  <span class="citation" data-id="788327"><a href="/opinion/788327/united-states-v-timothy-stewart/#1091" aria-description="Citation for case: United States v. Timothy Stewart">388 F.3d at 1091</a></span> (explaining that if the two-step interrogation was deliberately used, “then the analysis of the
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  plurality and Justice Kennedy’s concurrence merge, requiring an inquiry into the sufficiency of the break in time and circumstances between the unwarned and warned confessions”).
 </p>
<p id="b1184-10">
  Thus, the court must address (1) the completeness and detail of the pre-warning interrogation, (2) the overlapping content of the two rounds of interrogation, (3) the timing and circumstances of both interrogations, (4) the continuity of police personnel, (5) the extent to which the interrogator’s questions treated the second round of interrogation as continuous with the first and (6) whether any curative measures were taken.
  <em>
   See Seibert,
  </em>
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#615" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 615</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>(Souter, J., plurality opinion);
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#622" aria-description="Citation for case: Missouri v. Seibert"><em>
   id.
  </em>
  at 622</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Kennedy, J., concurring in the judgment). Notably, both the plurality and Justice Kennedy found significant that in giving Seibert her
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning, “the police did not advise that her prior statement could not be used.”
  <em>
   Id.
  </em>
  at 616, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Souter, J., plurality opinion);
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#622" aria-description="Citation for case: Missouri v. Seibert"><em>
   id.
  </em>
  at 622</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>(Kennedy, J., concurring in the judgment) (noting that an additional warning that explains the inadmissibility of the prewarning statement would serve as a curative measure).
  <a class="footnote" href="#fn15" id="fn15_ref">
   15
  </a>
  Justice Kennedy also
  <span citation-index="1" class="star-pagination" label="1161"> 
   *1161
   </span>
  found particularly troubling the overlapping content of the officers’ pre- and postwarning questions: “[rjeference to the prewarning statement [during the post-warning questioning] was an implicit suggestion that the mere repetition of the earlier statement was not independently incriminating. The implicit suggestion was false.”
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#621" aria-description="Citation for case: Missouri v. Seibert"><em>
   Id.
  </em>
  at 621</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Kennedy, J., concurring in the judgment). Finally, Justice Kennedy viewed the continuous nature of the interrogation relevant to the suspect’s experience of interrogation, suggesting — again, as a curative measure — that a “substantial break in time and circumstances” between pre- and post-warning questioning, would “in most circumstances, ... allow[ ] the accused to distinguish the two contexts and appreciate that the interrogation ha[d] taken a new turn.”
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#622" aria-description="Citation for case: Missouri v. Seibert"><em>
   Id.
  </em>
  at 622</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>.
 </p>
<p id="b1185-5">
  On the other hand, where the court finds deliberateness to be absent, “[t]he admissibility of postwarning statements should continue to be governed by the principles of
  <em>
   Elstad:’ Id.
  </em>
  at 622, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Kennedy, J., concurring in the judgment).
 </p>
<p id="b1185-6">
  3. Seibert’s
  <em>
   effect on relevant precedent
  </em>
</p>
<p id="b1185-7">
<em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  diminishes
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>
  </em>
  but does not destroy it. We conclude, however, that
  <em>
   <span class="citation" data-id="9494408"><a href="/opinion/775079/united-states-v-jody-myesha-orso/" aria-description="Citation for case: United States v. Jody Myesha Orso">Orso</a></span>
  </em>
  cannot stand as the law of the circuit in light of
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>.
  </em>
  Under
  <em>
   <span class="citation" data-id="9494408"><a href="/opinion/775079/united-states-v-jody-myesha-orso/" aria-description="Citation for case: United States v. Jody Myesha Orso">Orso</a></span>,
  </em>
  regardless of the police tactics employed, voluntary postwarning inculpatory statements are excluded
  <em>
   only
  </em>
  when the prewarning statements were not only unwarned but also involuntary, and any taint therefrom had not dissipated by the time the
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warning was given.
  <em>
   Orso,
  </em>
  <span class="citation" data-id="9494408"><a href="/opinion/775079/united-states-v-jody-myesha-orso/#1039" aria-description="Citation for case: United States v. Jody Myesha Orso">266 F.3d at 1039</a></span>. However, a majority of the Justices in
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
  </em>
  would bar postwarning confessions elicited during deliberate and un-remedied two-step interrogations, even if they were given after voluntary unwarned statements.
 </p>
<p id="b1185-8">
  This holding abrogates
  <em>
   <span class="citation" data-id="9494408"><a href="/opinion/775079/united-states-v-jody-myesha-orso/" aria-description="Citation for case: United States v. Jody Myesha Orso">Orso</a></span>,
  </em>
  because it indicates that there are some “improper tactics,” short of coercion, that taint a two-step confession.
  <em>
   See Orso,
  </em>
  <span class="citation" data-id="9494408"><a href="/opinion/775079/united-states-v-jody-myesha-orso/#1036" aria-description="Citation for case: United States v. Jody Myesha Orso">266 F.3d at 1036</a></span> (rejecting petitioner’s contention that confession was inadmissible because it was obtained by “improper tactics”). Because a majority of the Court has held that in some category of cases involving voluntary prewarning statements, police conduct may nonetheless render
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warnings ineffective, we cannot simply revert to our prior law.
  <em>
   See Miller v. Gammie,
  </em>
  <span class="citation" data-id="8408008"><a href="/opinion/8437592/miller-v-gammie/#893" aria-description="Citation for case: Miller v. Gammie">335 F.3d 889, 893</a></span> (9th Cir.2003) (en banc) (holding that when a three-judge panel is faced with intervening precedent from a higher court that is “clearly-irreconcilable” with a prior holding of this court, the panel is bound by the intervening authority).
 </p>
<p id="b1185-9">
  D.
 </p>
<p id="b1185-10">
  Because the district court did not have the benefit of
  <em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>,
  </em>
  it did not make the requisite factual inquiries to determine whether Agents O’Neil and Dobbs deliberately employed the two-step interrogation, and if so, whether the midstream warning effectively apprised Williams of his rights. Without this targeted factual analysis, we cannot be certain that Williams’ postwarn-ing statement was properly admitted as evidence.' Although the evidence strongly suggests that the midstream warning did not “function ‘effectively’ as
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  requires,”
  <em>
   Seibert,
  </em>
  <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#611" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 611-12</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Souter, J., plurality opinion), we are unable to determine on the record before us whether the two-step strategy was used deliberately to undermine
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  (and therefore whether
  <em>
   Seibert’s
  </em>
  objective inquiry into effectiveness applies). We therefore reverse the district court’s order denying suppression of Williams’ postwarning confession, vacate the judgment of conviction and remand for the district court to hold a new suppression hearing consistent with this opinion. The
  <span citation-index="1" class="star-pagination" label="1162"> 
   *1162
   </span>
  district court shall determine, based on objective as well as any available subjective evidence, whether the two-step interrogation was deliberately used to circumvent
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,
  </em>
  and if so, whether objective evidence demonstrates that the midstream warning failed to apprise Williams effectively of his rights, thereby requiring suppression of the postwarning confession.
  <a class="footnote" href="#fn16" id="fn16_ref">
   16
  </a>
  If the district court finds that the confession must be suppressed, Williams’ conviction cannot stand.
 </p>
<p id="b1186-4">
  IV.
 </p>
<p id="b1186-5">
  The government argues that even if the district court erred in denying suppression, we should uphold Williams’ conviction because any erroneous admission of Williams’ written confession was harmless. “On direct review, the government’s commission of a constitutional error requires reversal of a conviction unless the government proves ‘beyond a reasonable doubt that the error complained of did not contribute to the verdict obtained.’ ”
  <em>
   United States v. Garibay,
  </em>
  <span class="citation" data-id="754206"><a href="/opinion/754206/united-states-of-america-plaintiff-appellee-v-jose-rosario-garibay-jr/#539" aria-description="Citation for case: UNITED STATES of America, Plaintiff-Appellee, v. Jose...">143 F.3d 534, 539</a></span> (9th Cir.1998) (quoting
  <em>
   Chapman v. California,
  </em>
  <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#24" aria-description="Citation for case: Chapman v. California">386 U.S. 18, 24</a></span>, <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">87 S.Ct. 824</a></span>, <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">17 L.Ed.2d 705</a></span> (1967)). Any error in this case was not harmless beyond a reasonable doubt.
  <a class="footnote" href="#fn17" id="fn17_ref">
   17
  </a>
</p>
<p id="b1186-7">
  Erroneous admission of a confession does not constitute structural error.
  <em>
   See Arizona v. Fulminante,
  </em>
  <span class="citation" data-id="9432240"><a href="/opinion/112566/arizona-v-fulminante/#306" aria-description="Citation for case: Arizona v. Fulminante">499 U.S. 279, 306-12</a></span>, <span class="citation" data-id="9432240"><a href="/opinion/112566/arizona-v-fulminante/" aria-description="Citation for case: Arizona v. Fulminante">111 S.Ct. 1246</a></span>, <span class="citation" data-id="9432240"><a href="/opinion/112566/arizona-v-fulminante/" aria-description="Citation for case: Arizona v. Fulminante">113 L.Ed.2d 302</a></span> (1991). The Supreme Court has, however, acknowledged that:
 </p>
<blockquote id="b1186-8">
  A confession is like no other evidence. Indeed, “the defendant’s own confession is probably the most probative and damaging evidence that can be admitted against him.... Certainly, confessions have profound impact on the jury, so much so that we may justifiably doubt its ability to put them out of mind even if told to do so.”
 </blockquote>
<p id="b1186-9">
<span class="citation" data-id="9432240"><a href="/opinion/112566/arizona-v-fulminante/#296" aria-description="Citation for case: Arizona v. Fulminante"><em>
   Id.
  </em>
  at 296</a></span>, <span class="citation" data-id="9432240"><a href="/opinion/112566/arizona-v-fulminante/" aria-description="Citation for case: Arizona v. Fulminante">111 S.Ct. 1246</a></span>(quoting
  <em>
   Bruton v. United States,
  </em>
  <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/#139" aria-description="Citation for case: Bruton v. United States">391 U.S. 123, 139-40</a></span>, <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">88 S.Ct. 1620</a></span>, <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">20 L.Ed.2d 476</a></span> (1968) (White, J., dissenting)). In
  <em>
   <span class="citation" data-id="9432240"><a href="/opinion/112566/arizona-v-fulminante/" aria-description="Citation for case: Arizona v. Fulminante">Fulminante</a></span>,
  </em>
  the Court distinguished between two types of erroneously admitted confessions — those that “concern isolated aspects of the crime or may be incriminating only when linked to other evidence” and “full confession^] in which the defendant discloses the motive for and means of the crime.”
  <em>
   <span class="citation" data-id="9432240"><a href="/opinion/112566/arizona-v-fulminante/" aria-description="Citation for case: Arizona v. Fulminante">Id.</a></span>
  </em>
  The latter, the Court explained, will seldom be harmless because they “may tempt the jury to rely upon that evidence alone in reaching its decision.”
  <em>
   <span class="citation" data-id="9432240"><a href="/opinion/112566/arizona-v-fulminante/" aria-description="Citation for case: Arizona v. Fulminante">Id.</a></span>
  </em>
</p>
<p id="b1187-3">
<span citation-index="1" class="star-pagination" label="1163"> 
   *1163
   </span>
  Our case law tracks this distinction. We have held erroneous admission of inculpatory statements harmless under the
  <em>
   <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span>
  </em>
  standard only where the confession did not go to the heart of the case.
  <em>
   See, e.g., Garibay,
  </em>
  <span class="citation" data-id="754206"><a href="/opinion/754206/united-states-of-america-plaintiff-appellee-v-jose-rosario-garibay-jr/#539" aria-description="Citation for case: UNITED STATES of America, Plaintiff-Appellee, v. Jose...">143 F.3d at 539-40</a></span> (holding admission not harmless where defendant’s statements “were the thrust of the prosecution’s case”);
  <em>
   United States v. Harrison,
  </em>
  <span class="citation" data-id="677448"><a href="/opinion/677448/united-states-v-sonja-harrison/" aria-description="Citation for case: United States v. Sonja Harrison">34 F.3d 886</a></span> (9th Cir.1994) (reversing conviction where district court erroneously admitted defendant’s statement that provided a detailed account of the crimes charged);
  <em>
   cf. United States v. Padilla,
  </em>
  <span class="citation" data-id="788215"><a href="/opinion/788215/united-states-v-nicholas-padilla/#1093" aria-description="Citation for case: United States v. Nicholas Padilla">387 F.3d 1087, 1093-94</a></span> (9th Cir.2004) (holding error harmless where “[t]he only usefulness of the statement was that it was inconsistent with the defense Padilla put on”). Williams’ full confession went to the heart of his case.
 </p>
<p id="b1187-4">
  Additionally, contrary to the government’s assertion, we cannot be certain on the record before us that the jury would have pieced together the other evidence presented by the government and reached a guilty verdict. In addition to the confession, the government submitted Williams’ application, which listed Williams’ height as 5'8" (a height between Williams’ actual height and Iddrissu’s), the testimony of a clerk that he showed Williams his application with Iddrissu’s photographs attached and Williams’ testimony that plans for the trip to London, mentioned in the application, had not been finalized. This evidence clearly supported the government’s argument that Williams intended to obtain a passport for Iddrissu. But Williams also presented contrary evidence to the jury. He testified that the photographs must have been switched inadvertently, or, in the alternative, that Iddrissu must have intentionally switched the photographs without telling Williams. In the absence of the confession, it is not clear that the jury would have credited the government’s story over Williams’ version. As we cannot be certain “beyond a reasonable doubt that the error complained of did not contribute to the verdict obtained,” and in light of the Court’s guidance in
  <em>
   Fulmi nante,
  </em>
  we hold that the admission of Williams’ written confession, if erroneous, was not harmless.
  <em>
   Chapman,
  </em>
  <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#24" aria-description="Citation for case: Chapman v. California">386 U.S. at 24</a></span>, <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">87 S.Ct. 824</a></span>.
 </p>
<p id="b1187-6">
  V.
 </p>
<p id="b1187-7">
  We REVERSE the district court’s order denying suppression, VACATE the judgment of conviction and REMAND the case to the district court for further proceedings consistent with this opinion.
 </p>

















<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b1174-11">
   . The district court found that Williams was in custody at this point.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b1175-8">
   . Before the district court, the agents testified that they read Williams his rights before asking any questions. This testimony contradicted the investigation report filed by Agent Dobbs immediately after the incident. The district court held an evidentiary hearing on the matter and found that the agents did not issue
   <em>
    <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
   </em>
   warnings until after Williams made his inculpatory comments, immediately before he wrote his statement. The government has not appealed this factual finding.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b1176-6">
   . The Court’s belief that Elstad's prewarning statements were voluntary played a decisive role in its analysis. The Court reasoned that in cases where a postwarning confession was preceeded by a "clearly voluntary” but unwarned statement, a "careful and thorough” midstream warning
   <em>
    ''ordinarily
   </em>
   should suffice to remove the conditions that precluded admission of the earlier statement” because it "conveys the relevant information” regarding a suspect's Fifth Amendment rights.
   <em>
    Elstad,
   </em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#310" aria-description="Citation for case: Oregon v. Elstad">470 U.S. at 310-11, 314</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span> (emphasis added). In such circumstances, "the suspect’s choice whether to exercise his privilege to remain silent should
   <em>
    ordinarily
   </em>
   be viewed as an act of free will.”
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#311" aria-description="Citation for case: Oregon v. Elstad"><em>
    Id.
   </em>
   at 311</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span> (emphasis added) (internal quotation marks and internal citations omitted). However,
   <em>
    <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>
   </em>
   also appeared to limit its holding to the circumstances of the case:
  </p>
<blockquote id="A5O">
<span citation-index="1" class="star-pagination" label="1153"> 
    *1153
    </span>
   "[i]t is an unwarranted extension of
   <em>
    <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
   </em>
   to hold that a
   <em>
    simple failure
   </em>
   to administer the warnings,
   <em>
    unaccompanied by any actual coercion or other circumstances calculated to undermine the suspect’s ability to exercise his free will,
   </em>
   so taints the investigatory process that a subsequent voluntary and informed waiver is ineffective for some indeterminate period. Though
   <em>
    <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
   </em>
   requires that the unwarned admission must be suppressed, the admissibility of any subsequent statement should turn
   <em>
    in these circumstances
   </em>
   solely on whether it is knowingly and voluntarily
   <em>
    made."
   </em>
</blockquote>
<p id="b1177-6">
<em>
    Id.
   </em>
   at 309, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span> (emphasis added).
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b1177-7">
   . As stated in
   <em>
    <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>,
   </em>
   ”[w]hen a prior statement is actually coerced, the time that passes between confessions, the change in place of interrogations, and the change in identity of the interrogators all bear on whether _ that coercion has carried over into the second confession.” <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#310" aria-description="Citation for case: Oregon v. Elstad">470 U.S. at 310</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S.Ct. 1285</a></span>.
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b1177-8">
   . Voluntariness is a totality of circumstances inquiry that assesses “both the characteristics of the accused and the details of the interrogation.”
   <em>
    Schneckloth v. Bustamonte,
   </em>
   <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218, 226-27</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L.Ed.2d 854</a></span> (1973) (noting that although “the state of the accused’s mind, and the failure of the police to advise the accused of his rights, [are] certainly factors to be evaluated in / assessing ... ’voluntariness,’ ... they [are] not in and of themselves determinative”). The court should therefore “determine[ ] the factual circumstances surrounding the confession, assess!] the psychological impact on the accused, and evaluate! ] the legal significance of how the accused reacted.”
   <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte"><em>
    Id.
   </em>
   at 226</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041</a></span>. In the past, for example, the Court considered “the youth of the accused, his lack of education, or his low intelligence, the lack of any advice to the accused of his constitutional rights, the length of detention, the repeated and prolonged nature of the questioning, and the use of physical punishment such as the deprivation of food or sleep.”
   <em>
    <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Id.</a></span>
   </em>
   (internal citations omitted). We have similarly stated that voluntariness depends on such factors as “the surrounding circumstances, the combined effect of the entire course of the officer’s conduct upon the defendant, including the effect of his previously having made a confession, and the manner in which the officers utilized this prior confession in obtaining a second confession.”
   <em>
    Wauneka,
   </em>
   <span class="citation" data-id="457572"><a href="/opinion/457572/united-states-v-allen-wauneka/#1440" aria-description="Citation for case: United States v. Allen Wauneka">770 F.2d at 1440</a></span>. In addition, the government must prove voluntariness by a preponderance of the evidence.
   <em>
    Lego v. Twomey,
   </em>
   <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#489" aria-description="Citation for case: Lego v. Twomey">404 U.S. 477, 489</a></span>, <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/" aria-description="Citation for case: Lego v. Twomey">92 S.Ct. 619</a></span>, <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/" aria-description="Citation for case: Lego v. Twomey">30 L.Ed.2d 618</a></span> (1972);
   <em>
    see also Seibert,
   </em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#609" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 609</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#1" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601 n. 1</a></span>.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b1178-6">
   . Because Orso did not argue that her post-warning confession was involuntary, we did not address the voluntariness of the warned statement.
   <em>
    See Orso,
   </em>
   <span class="citation" data-id="9494408"><a href="/opinion/775079/united-states-v-jody-myesha-orso/" aria-description="Citation for case: United States v. Jody Myesha Orso">266 F.3d at 1039</a></span> n. 4.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b1179-6">
   . As the plurality explained, "[w]hen the same officer who had conducted the first phase recited the
   <em>
    <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
   </em>
   warnings, he ... did not advise that her prior statement could not be
   <span citation-index="1" class="star-pagination" label="1156"> 
    *1156
    </span>
   used.... The impression that the further questioning was a mere continuation of the earlier questions and responses was fostered by references back to the confession already given. It would have been reasonable to regard the two sessions as parts of a continuum, in which it would have been unnatural to refuse to repeat at the second stage what had been said before.”
   <em>
    Seibert,
   </em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#616" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 616-17</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>.
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b1180-9">
   . Justice Breyer also wrote a brief concurrence indicating that he would instruct courts to exclude the "fruits” of the unwarned questioning unless the "failure to warn was in good faith.”
   <em>
    Seibert,
   </em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#617" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 617</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Breyer, J., concurring). Although Justice Breyer joined the plurality opinion in full, he also stated that he agreed with Justice Kennedy’s opinion “insofar as it is consistent with [the application of a] good-faith exception” to an exclusionary rule.
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#618" aria-description="Citation for case: Missouri v. Seibert"><em>
    Id.
   </em>
   at 618</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span>.
  </p>
</div><div class="footnote" id="fn9" label="9">
<a class="footnote" href="#fn9_ref">
   9
  </a>
<p id="b1181-8">
   . Applying
   <em>
    Marks’
   </em>
   rule, we have often construed one Justice's concurring opinion as representing a logical subset of the plurality's and as adopting a holding that would affect a narrower range of cases than that of the plurality.
   <em>
    See, e.g., United States
   </em>
   v.
   <em>
    Antelope,
   </em>
   <span class="citation" data-id="789030"><a href="/opinion/789030/united-states-v-lawrence-antelope-united-states-of-america-v-lawrence/#1135" aria-description="Citation for case: United States v. Lawrence Antelope, United States of...">395 F.3d 1128, 1135-38</a></span> (9th Cir.2005);
   <em>
    Ctr. for Fair Pub. Policy v. Maricopa County,
   </em>
   <span class="citation multiple-matches"><a href="/c/F.3d/336/1153/">336 F.3d 1153</a></span>, 1161 (9th Cir.2003);
   <em>
    Smith,
   </em>
   <span class="citation" data-id="771312"><a href="/opinion/771312/katuria-e-smith-angela-rock-michael-pyle-for-themselves-and-all-others/#1199" aria-description="Citation for case: Katuria E. Smith Angela Rock Michael Pyle for Themselves...">233 F.3d at 1199-1200</a></span>. Accordingly, we have held such a concurrence binding under
   <em>
    Marks.
   </em>
</p>
</div><div class="footnote" id="fn10" label="10">
<a class="footnote" href="#fn10_ref">
   10
  </a>
<p id="b1182-4">
   .Justices Souter and Kennedy may differ on one aspect of the
   <em>
    <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
   </em>
   exception analysis, which is the effectiveness of additional curative warnings. Justice Souter explained that the plurality does not "hold that a formal addendum warning that a previous statement could not be used would be sufficient to change the character of the question-first procedure to the point of rendering an ensuing statement admissible,” but that "its absence is clearly a factor.”
   <em>
    Seibert,
   </em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#616" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 616</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#7" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601 n. 7</a></span> (Souter, J., plurality opinion). Justice Kennedy suggested that an addendum warning "may be sufficient.”
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#622" aria-description="Citation for case: Missouri v. Seibert"><em>
    Id.
   </em>
   at 622</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Kennedy, J., concurring in the judgment). Because no curative warnings were given here, we need not determine the Court’s holding on this issue.
  </p>
</div><div class="footnote" id="fn11" label="11">
<a class="footnote" href="#fn11_ref">
   11
  </a>
<p id="b1182-8">
   . For example, Justice Kennedy's opinion is silent as to what, if any, presumptions apply or which parly bears the burden of proving or disproving deliberateness.
  </p>
</div><div class="footnote" id="fn12" label="12">
<a class="footnote" href="#fn12_ref">
   12
  </a>
<p id="b1182-9">
   . This test functions appropriately as a combination of Justice Souter's plurality opinion and Justice Kennedy’s concurrence.
   <em>
    See Siegmund v. Gen. Commodities Corp.,
   </em>
   <span class="citation" data-id="1474306"><a href="/opinion/1474306/siegmund-v-general-commodities-corporation/#953" aria-description="Citation for case: Siegmund v. General Commodities Corporation">175 F.2d 952, 953</a></span> (9th Cir.1949) (“The reasons assigned by the two groups of Justices who concurred in the result are ... applicable....”).
  </p>
</div><div class="footnote" id="fn13" label="13">
<a class="footnote" href="#fn13_ref">
   13
  </a>
<p id="b1183-6">
   . For example, in
   <em>
    United States v. Briones,
   </em>
   the Eighth Circuit concluded that the record contained no evidence suggesting that law enforcement officers deliberately delayed the
   <em>
    <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
   </em>
   warning to circumvent the suspect's rights. <span class="citation" data-id="788484"><a href="/opinion/788484/united-states-of-america-plaintiffappellee-v-eriberto-melesio-briones/#614" aria-description="Citation for case: UNITED STATES OF AMERICA, PLAINTIFF—APPELLEE v. ERIBERTO...">390 F.3d at 614</a></span>. The court noted that the suspect did not make an incriminating statement during the first interview as it was cut short by the suspect's unwillingness to answer the officer's questions.
   <em>
    <span class="citation" data-id="788484"><a href="/opinion/788484/united-states-of-america-plaintiffappellee-v-eriberto-melesio-briones/" aria-description="Citation for case: UNITED STATES OF AMERICA, PLAINTIFF—APPELLEE v. ERIBERTO...">Id.</a></span>
   </em>
   Instead, the suspect's "unexpected” (and unwarned) inculpatory statement "did not result from interrogation” because it was made in the lobby after the initial questioning had ended.
   <em>
    <span class="citation" data-id="788484"><a href="/opinion/788484/united-states-of-america-plaintiffappellee-v-eriberto-melesio-briones/" aria-description="Citation for case: UNITED STATES OF AMERICA, PLAINTIFF—APPELLEE v. ERIBERTO...">Id.</a></span>
   </em>
   Moreover, the suspect's postwarning confession came a day and a half after the initial interview during a meeting with law enforcement officers which the suspect himself requested.
  </p>
</div><div class="footnote" id="fn14" label="14">
<a class="footnote" href="#fn14_ref">
   14
  </a>
<p id="b1183-11">
   . Justice Kennedy suggested that in some situations, there may be a legitimate reason for not giving a suspect an immediate
   <em>
    <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
   </em>
   warning, such as when an officer does not plan to question the suspect or is waiting for a more appropriate time to do so.
   <em>
    Seibert,
   </em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#620" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 620</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Kennedy, J„ concurring in the judgment). However, unlike the facts in
   <em>
    <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
   </em>
   and this case, those situations assume that the officer has not begun interrogating the suspect.
  </p>
</div><div class="footnote" id="fn15" label="15">
<a class="footnote" href="#fn15_ref">
   15
  </a>
<p id="b1184-7">
   . The plurality, however, noted that including such a cautionary statement would not, on its own, necessarily cure the defects of the question-first procedure.
   <em>
    Seibert,
   </em>
   <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#617" aria-description="Citation for case: Missouri v. Seibert">542 U.S. at 617</a></span>, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/#7" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601 n. 7</a></span> (Souter, J., plurality opinion).
  </p>
</div><div class="footnote" id="fn16" label="16">
<a class="footnote" href="#fn16_ref">
   16
  </a>
<p id="b1186-6">
   . The objective inquiries into deliberateness and effectiveness function practically as an analysis of whether the facts of a particular case more closely resemble those in
   <em>
    <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">Seibert</a></span>
   </em>
   or
   <em>
    <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>.
   </em>
   Although we leave this analysis for the district court, several facts should guide its inquiries. For example, Williams was in custody from the point at which Agents O’Neil and Dobbs took him into the old reception area and began questioning him. Before giving the
   <em>
    <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
   </em>
   warning, Agent O'Neil questioned Williams using standard interrogation techniques and until he obtained a confession; then, without any break in time or change of venue, he read Williams his
   <em>
    <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
   </em>
   rights and asked Williams to write down what he had already told them. Finally, the court should determine whether the agents took any curative measures "to ensure that a reasonable person in the suspect's situation would understand the import and effect of the
   <em>
    <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
   </em>
   warning and of the
   <em>
    <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
   </em>
   waiver.”
   <em>
    Seibert, 542
   </em>
   U.S. at 622, <span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">124 S.Ct. 2601</a></span> (Kennedy, J., concurring in the judgment).
  </p>
</div><div class="footnote" id="fn17" label="17">
<a class="footnote" href="#fn17_ref">
   17
  </a>
<p id="b1186-11">
   . Assuming Williams' postwarning confession was improperly admitted, we would also conclude under the standard of
   <em>
    Brecht v. Abrahamson,
   </em>
   <span class="citation" data-id="9432778"><a href="/opinion/112845/brecht-v-abrahamson/" aria-description="Citation for case: Brecht v. Abrahamson">507 U.S. 619</a></span>, <span class="citation" data-id="9432778"><a href="/opinion/112845/brecht-v-abrahamson/" aria-description="Citation for case: Brecht v. Abrahamson">113 S.Ct. 1710</a></span>, <span class="citation" data-id="9432778"><a href="/opinion/112845/brecht-v-abrahamson/" aria-description="Citation for case: Brecht v. Abrahamson">123 L.Ed.2d 353</a></span> (1993), that the written confession "likely had a substantial and injurious impact on the verdict.”
   <em>
    Sims v. Brown,
   </em>
   <span class="citation" data-id="9843292"><a href="/opinion/792125/mitchell-carlton-sims-v-jill-brown-warden/#570" aria-description="Citation for case: Mitchell Carlton Sims v. Jill Brown, Warden">425 F.3d 560, 570</a></span> (9th Cir.2005) (quoting
   <em>
    Taylor v. Maddox,
   </em>
   <span class="citation" data-id="786028"><a href="/opinion/786028/leif-taylor-v-thomas-m-maddox-interim-director-george-galaza-cal-terhune/#1016" aria-description="Citation for case: Leif Taylor v. Thomas M. Maddox, Interim Director George...">366 F.3d 992, 1016</a></span> (9th Cir.2004)). Unlike in
   <em>
    <span class="citation" data-id="9843292"><a href="/opinion/792125/mitchell-carlton-sims-v-jill-brown-warden/" aria-description="Citation for case: Mitchell Carlton Sims v. Jill Brown, Warden">Sims</a></span>,
   </em>
   the evidence of Williams’ guilt is not so "over-whelming” as to preclude the "reasonable likelihood that the challenged statement ] actually prejudiced him.”
   <span class="citation" data-id="9843292"><a href="/opinion/792125/mitchell-carlton-sims-v-jill-brown-warden/#571" aria-description="Citation for case: Mitchell Carlton Sims v. Jill Brown, Warden"><em>
    Id.
   </em>
   at 571</a></span>.
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Utah v. Strieff.md  (`case`, 5 assertions)

### content_page

```
---
title: "Utah v. Strieff"
type: case
citation: ""
parallel_cite: "579 U.S. 232; 136 S. Ct. 2056; 195 L. Ed. 2d 400; 84 U.S.L.W. 4430; 26 Fla. L. Weekly Fed. S 288"
neutral_cite: 2016 U.S. LEXIS 3926
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2016
date_decided: 2016-06-20
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2016-06-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Utah v. Strieff
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/8176208/utah-v-strieff/"
  cluster_id: 8176208
  opinion_id: 8137990
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brown v. Illinois]]", "[[Segura v. United States]]", "[[Herring v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "attenuation", "fruit-of-the-poisonous-tree", "arrest-warrant"]
holding: "Attenuation: discovery of a valid pre-existing arrest warrant during an unlawful stop was an intervening circumstance that attenuated…"
lake:
  record_id: Utah v. Strieff
  status: verified
  projected_at: 2026-07-09
---

# Utah v. Strieff

*579 U.S. 232 (2016)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After an anonymous tip about drug activity at a house, Detective Fackrell conducted intermittent surveillance, observed visitors consistent with drug dealing, and stopped Strieff after he left the house. The State later conceded the stop lacked reasonable suspicion. During the stop, Fackrell ran Strieff's identification, discovered a valid outstanding arrest warrant for a traffic offense, arrested Strieff on that warrant, and — searching him incident to the arrest — found methamphetamine and drug paraphernalia. Strieff moved to suppress; the Utah Supreme Court ordered suppression, and the State sought review.

## Issue
Whether the discovery of a valid pre-existing arrest warrant during an unlawful investigatory stop attenuates the connection between the unlawful stop and evidence seized incident to the arrest on that warrant, making the evidence admissible.

## Rule
The [[Fruits and Attenuation|attenuation]] exception is governed by the three *[[Brown v. Illinois]]* factors. The Court looks to "the 'temporal proximity'" between the misconduct and the discovery of evidence; "the presence of intervening circumstances"; and, "'particularly' significant," "the purpose and flagrancy of the official misconduct." — 136 S. Ct. at 2061–2062. ^pin-2062

Here, the intervening-circumstances factor controlled: "the second factor, the presence of intervening circumstances, strongly favors the State" — the valid arrest warrant predated the stop and was entirely independent of it. — [136 S. Ct. at 2062](https://www.courtlistener.com/opinion/8176208/utah-v-strieff/#:~:text=the%20second%20factor%2C%20the%20presence). ^pin-2062a

## Application
Although temporal proximity favored suppression — only minutes passed between the unlawful stop and the search — the discovery of the valid, pre-existing arrest warrant was an intervening circumstance that strongly favored the State, and Officer Fackrell's conduct was at most negligent rather than purposeful or flagrant. On balance, the warrant broke the causal chain between the unlawful stop and the evidence, so the methamphetamine and paraphernalia found incident to the lawful arrest on that warrant were admissible.

## Conclusion
The discovery of the valid arrest warrant attenuated the connection between the unlawful stop and the seized evidence; the evidence was admissible, and the judgment of the Utah Supreme Court was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Strieff* applies the [[Fruits and Attenuation|attenuation]] doctrine of [[Brown v. Illinois]]: a valid pre-existing arrest warrant discovered during an unlawful stop is an intervening circumstance that, absent flagrant police misconduct, attenuates the taint of the illegal stop. (Justice Sotomayor filed a vigorous [[Common Legal Terms#dissenting-opinion|dissent]], but the decision is controlling law.)

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *Utah v. Strieff*, 579 U.S. 232 (2016) — https://www.courtlistener.com/opinion/8176208/utah-v-strieff/ — pinpoints given to the parallel S. Ct. reporter (CourtListener star-paginates *Strieff* by 136 S. Ct.): 2061–2062. Cluster 8176208 → opinion 8137990.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "36c5313b2f404213", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2016 U.S. LEXIS 3926", "official_citation_present": false, "parallel_cite": "579 U.S. 232; 136 S. Ct. 2056; 195 L. Ed. 2d 400; 84 U.S.L.W. 4430; 26 Fla. L. Weekly Fed. S 288", "title": "Utah v. Strieff", "year": "2016"}}
{"assertion_id": "73809e90c8c5a3f3", "dimension": "support", "kind": "home_role", "locator": {"home": "Fruits & Attenuation"}, "payload": {"home": "Fruits & Attenuation", "role": "Key — Progeny / Refinement", "title": "Utah v. Strieff"}}
{"assertion_id": "c3bccf8b94de907b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Attenuation: discovery of a valid pre-existing arrest warrant during an unlawful stop was an intervening circumstance that attenuated…", "title": "Utah v. Strieff"}}
{"assertion_id": "20c11795d33a9e1d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2016-06-20", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Utah v. Strieff", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Utah v. Strieff", "varies_by_point": "false"}}
{"assertion_id": "cbe3adfb4d878b39", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Utah v. Strieff"}}
```

### lake record — Utah v. Strieff

```json
{
  "schema_version": "s2.v1",
  "record_id": "Utah v. Strieff",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Utah v. Strieff",
    "case_name_short": "Strieff",
    "case_name_full": "UTAH v. Edward Joseph STRIEFF, Jr.",
    "input_case_name": "Utah v. Strieff",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2016-06-20",
    "year": 2016,
    "docket": null,
    "cluster_id": 8176208,
    "lead_opinion_id": 8137990,
    "sibling_ids": [
      8137990
    ],
    "absolute_url": "/opinion/8176208/utah-v-strieff/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 3214882,
        "score": 120,
        "case_name": "Utah v. Strieff"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "579 U.S. 232",
        "volume": "579",
        "reporter": "U.S.",
        "page": "232",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "136 S. Ct. 2056",
        "volume": "136",
        "reporter": "S. Ct.",
        "page": "2056",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "195 L. Ed. 2d 400",
        "volume": "195",
        "reporter": "L. Ed. 2d",
        "page": "400",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 U.S.L.W. 4430",
        "volume": "84",
        "reporter": "U.S.L.W.",
        "page": "4430",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 288",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "288",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2016 U.S. LEXIS 3926",
        "volume": "2016",
        "reporter": "U.S. LEXIS",
        "page": "3926",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "579 U.S. 232",
        "volume": "579",
        "reporter": "U.S.",
        "page": "232",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "136 S. Ct. 2056",
        "volume": "136",
        "reporter": "S. Ct.",
        "page": "2056",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "195 L. Ed. 2d 400",
        "volume": "195",
        "reporter": "L. Ed. 2d",
        "page": "400",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 U.S.L.W. 4430",
        "volume": "84",
        "reporter": "U.S.L.W.",
        "page": "4430",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 288",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "288",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 U.S. LEXIS 3926",
        "volume": "2016",
        "reporter": "U.S. LEXIS",
        "page": "3926",
        "type": 6,
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
      "id": "pin-2062",
      "page": null,
      "quote": "--- # Utah v. Strieff *579 U.S. 232 (2016)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After an anonymous tip about drug activity at a house, Detective Fackrell conducted intermittent surveillance, observed visitors consistent with drug dealing, and stopped Strieff after he left the house. The State later conceded the stop lacked reasonable suspicion. During the stop, Fackrell ran Strieff's identification, discovered a valid outstanding arrest warrant for a traffic offense, arrested Strieff on that warrant, and \u2014 searching him incident to the arrest \u2014 found methamphetamine and drug paraphernalia. Strieff moved to suppress; the Utah Supreme Court ordered suppression, and the State sought review. ## Issue Whether the discovery of a valid pre-existing arrest warrant during an unlawful investigatory stop attenuates the connection between the unlawful stop and evidence seized incident to the arrest on that warrant, making the evidence admissible. ## Rule The attenuation exception is governed by the three *Brown v. Illinois* factors. The Court looks to",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-2062a",
      "page": null,
      "quote": "the second factor, the presence of intervening circumstances, strongly favors the State",
      "star_marker": "2062",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 23227,
      "fragment": "#:~:text=the%20second%20factor%2C%20the%20presence",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2016-06-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Utah v. Strieff",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dancy v. McGinley",
          "cluster_id": 4327925,
          "cite": [
            "843 F.3d 93",
            "2016 U.S. App. LEXIS 21753",
            "2016 WL 7118403"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Hall v. City of Chicago",
          "cluster_id": 4738333,
          "cite": [
            "953 F.3d 945"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tyslen Baker",
          "cluster_id": 4788854,
          "cite": [
            "976 F.3d 636"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Young",
          "cluster_id": 4249369,
          "cite": [
            "835 F.3d 13",
            "2016 U.S. App. LEXIS 15275",
            "2016 WL 4410064"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Levin",
          "cluster_id": 4438375,
          "cite": [
            "874 F.3d 316",
            "2017 U.S. App. LEXIS 21354"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Oniel McKenzie",
          "cluster_id": 5092475,
          "cite": [
            "13 F.4th 223"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lambis",
          "cluster_id": 7321245,
          "cite": [
            "197 F. Supp. 3d 606",
            "2016 WL 3870940"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ellis",
          "cluster_id": 4773617,
          "cite": [
            "469 P.3d 65"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kelvin Baez",
          "cluster_id": 4843626,
          "cite": [
            "983 F.3d 1029"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Fiseku",
          "cluster_id": 8443878,
          "cite": [
            "915 F.3d 863"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mark McGill",
          "cluster_id": 4906577,
          "cite": [
            "8 F.4th 617"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Taurus Cooper",
          "cluster_id": 6248903,
          "cite": [
            "24 F.4th 1086"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Bruce Akers",
          "cluster_id": 5093384,
          "cite": [
            "259 A.3d 127",
            "2021 ME 43"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kyle Matthews",
          "cluster_id": 5064152,
          "cite": [
            "12 F.4th 647"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ramey",
          "cluster_id": 10607224,
          "cite": [
            "473 P.3d 13",
            "2020 NMCA 041"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. McGovern",
          "cluster_id": 7862081,
          "cite": [
            "974 N.W.2d 595",
            "311 Neb. 705"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Latecia Watkins",
          "cluster_id": 5094052,
          "cite": [
            "13 F.4th 1202"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Edwards",
          "cluster_id": 10606090,
          "cite": [
            "452 P.3d 413",
            "2019 NMCA 070"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jeremy Lillich",
          "cluster_id": 4903633,
          "cite": [
            "6 F.4th 869"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Washington v. State",
          "cluster_id": 10048684,
          "cite": [
            "482 Md. 395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harold William Barney Iii v. The State of Wyoming",
          "cluster_id": 9998680,
          "cite": [
            "2022 WY 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Malik Ngumezi",
          "cluster_id": 4808091,
          "cite": [
            "980 F.3d 1285"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Bray",
          "cluster_id": 4446093,
          "cite": [
            "902 N.W.2d 98",
            "297 Neb. 916"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Javier Garcia",
          "cluster_id": 4784058,
          "cite": [
            "974 F.3d 1071"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(8137990) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 58,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 58,
        "triage_read": 0,
        "triage_snippet_classified": 58
      },
      "lane2_top_cited": {
        "query": "cites:(8137990)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xJnM9NzMzNTgzNCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%288137990%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(8137990)",
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
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(8137990)",
    "indexed_citing_opinions": 79,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 8137990,
        "count": 79,
        "count_source": "search"
      }
    ],
    "citation_count": 424,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/utah-v-strieff.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc0MTg2MTMmcz01MDkzMzg0JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%288137990%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T03:39:55Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:40:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:40:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:43:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:40:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Utah v. Strieff (truncated)

```
<opinion type="majority">
<author id="p-8">Justice THOMAS delivered the opinion of the Court.</author>
<p id="p-9">To enforce the Fourth Amendment's prohibition against "unreasonable searches and seizures," this Court has at times required courts to exclude evidence obtained by unconstitutional police conduct. But the Court has also held that, even when there is a Fourth Amendment violation, this exclusionary rule does not apply when the costs of exclusion outweigh its deterrent benefits. In some cases, for example, the link between the unconstitutional conduct and the discovery of the evidence is too attenuated to justify suppression. The question in this case is whether this attenuation doctrine applies when an officer makes an unconstitutional investigatory stop; learns during that stop that the suspect is subject to a valid arrest warrant; and proceeds to arrest the suspect and seize incriminating evidence during a search incident to that arrest. We hold that the evidence the officer seized as part of the search incident to arrest is admissible because the officer's discovery of the arrest warrant attenuated the connection between the unlawful stop and the evidence seized incident to arrest.</p>
<p id="p-10">I</p>
<p id="p-11">This case began with an anonymous tip. In December 2006, someone called the South Salt Lake City police's drug-tip line to report "narcotics activity" at a particular residence. App. 15. Narcotics detective Douglas Fackrell investigated the tip. Over the course of about a week, Officer Fackrell conducted intermittent surveillance of the home. He observed visitors who left a few minutes after arriving at the house. These visits were sufficiently frequent to raise his suspicion that the occupants were dealing drugs.</p>
<p id="p-12"><a class="page-label" data-citation-index="1" data-label="2060" href="#p2060" id="p2060">*2060</a>One of those visitors was respondent Edward Strieff. Officer Fackrell observed Strieff exit the house and walk toward a nearby convenience store. In the store's parking lot, Officer Fackrell detained Strieff, identified himself, and asked Strieff what he was doing at the residence.</p>
<p id="p-13">As part of the stop, Officer Fackrell requested Strieff's identification, and Strieff produced his Utah identification card. Officer Fackrell relayed Strieff's information to a police dispatcher, who reported that Strieff had an outstanding arrest warrant for a traffic violation. Officer Fackrell then arrested Strieff pursuant to that warrant. When Officer Fackrell searched Strieff incident to the arrest, he discovered a baggie of methamphetamine and drug paraphernalia.</p>
<p id="p-14">The State charged Strieff with unlawful possession of methamphetamine and drug paraphernalia. Strieff moved to suppress the evidence, arguing that the evidence was inadmissible because it was derived from an unlawful investigatory stop. At the suppression hearing, the prosecutor conceded that Officer Fackrell lacked reasonable suspicion for the stop but argued that the evidence should not be suppressed because the existence of a valid arrest warrant attenuated the connection between the unlawful stop and the discovery of the contraband.</p>
<p id="p-15">The trial court agreed with the State and admitted the evidence. The court found that the short time between the illegal stop and the search weighed in favor of suppressing the evidence, but that two countervailing considerations made it admissible. First, the court considered the presence of a valid arrest warrant to be an " 'extraordinary intervening circumstance.' " App. to Pet. for Cert. 102 (quoting <em>United States v. Simpson,</em> <extracted-citation case-ids="31264" index="0" url="https://cite.case.law/f3d/439/490/#p496"><span class="citation" data-id="793479"><a href="/opinion/793479/united-states-v-bryan-lee-simpson/" aria-description="Citation for case: United States v. Bryan Lee Simpson">439 F.3d 490</a></span></extracted-citation>, 496 (C.A.8 2006) ). Second, the court stressed the absence of flagrant misconduct by Officer Fackrell, who was conducting a legitimate investigation of a suspected drug house.</p>
<p id="p-16">Strieff conditionally pleaded guilty to reduced charges of attempted possession of a controlled substance and possession of drug paraphernalia, but reserved his right to appeal the trial court's denial of the suppression motion. The Utah Court of Appeals affirmed. 2012 UT App ¶ 245, <extracted-citation case-ids="6980961" index="1" url="https://cite.case.law/p3d/286/317/"><span class="citation" data-id="9823262"><a href="/opinion/5308578/state-v-strieff/" aria-description="Citation for case: State v. Strieff">286 P.3d 317</a></span></extracted-citation>.</p>
<p id="p-17">The Utah Supreme Court reversed. 2015 UT ¶ 2, <extracted-citation case-ids="6842912" index="2" url="https://cite.case.law/p3d/357/532/"><span class="citation" data-id="2770744"><a href="/opinion/2770744/state-v-strieff/" aria-description="Citation for case: State v. Strieff">357 P.3d 532</a></span></extracted-citation>. It held that the evidence was inadmissible because only "a voluntary act of a defendant's free will (as in a confession or consent to search)" sufficiently breaks the connection between an illegal search and the discovery of evidence. <em><extracted-citation case-ids="6842912" index="3" url="https://cite.case.law/p3d/357/532/"><span class="citation" data-id="2770744"><a href="/opinion/2770744/state-v-strieff/" aria-description="Citation for case: State v. Strieff">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="6842912" index="3" url="https://cite.case.law/p3d/357/532/"> at 536</extracted-citation>. Because Officer Fackrell's discovery of a valid arrest warrant did not fit this description, the court ordered the evidence suppressed. <em>Ibid</em> .</p>
<p id="p-18">We granted certiorari to resolve disagreement about how the attenuation doctrine applies where an unconstitutional detention leads to the discovery of a valid arrest warrant. 576 U.S. ----, <extracted-citation case-ids="12599313,12599314,12599315,12599316,12599317,12599318" index="4" url="https://cite.case.law/s-ct/136/27/"><span class="citation multiple-matches"><a href="/c/S.Ct./136/27/">136 S.Ct. 27</a></span></extracted-citation>, <extracted-citation case-ids="12599248,12599313,12599314,12599315,12599451" index="5" url="https://cite.case.law/l-ed-2d/192/997/"><span class="citation multiple-matches"><a href="/c/L.Ed.2d/192/997/">192 L.Ed.2d 997</a></span></extracted-citation> (2015). Compare, <em>e.g.,</em> <em>United States v. Green,</em> <extracted-citation case-ids="11912832" index="6" url="https://cite.case.law/f3d/111/515/#p522"><span class="citation" data-id="739711"><a href="/opinion/739711/united-states-v-david-lee-green/" aria-description="Citation for case: United States v. David Lee Green">111 F.3d 515</a></span></extracted-citation>, 522-523 (C.A.7 1997) (holding that discovery of the warrant is a dispositive intervening circumstance where police misconduct was not flagrant), with, <em>e.g.,</em> <em>State v. Moralez,</em> <extracted-citation case-ids="12416938" index="7" url="https://cite.case.law/kan/297/397/#p415"><span class="citation" data-id="7923492"><a href="/opinion/7971077/state-v-moralez/" aria-description="Citation for case: State v. Moralez">297 Kan. 397</a></span></extracted-citation>, 415, <extracted-citation case-ids="12416938" index="8" url="https://cite.case.law/kan/297/397/#p415"><span class="citation" data-id="7923492"><a href="/opinion/7971077/state-v-moralez/" aria-description="Citation for case: State v. Moralez">300 P.3d 1090</a></span></extracted-citation>, 1102 (2013) (assigning little significance to the discovery of the warrant). We now reverse.</p>
<p id="p-19">II</p>
<p id="p-20">A</p>
<p id="p-21">The Fourth Amendment protects "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures." Because officers who violated the <a class="page-label" data-citation-index="1" data-label="2061" href="#p2061" id="p2061">*2061</a>Fourth Amendment were traditionally considered trespassers, individuals subject to unconstitutional searches or seizures historically enforced their rights through tort suits or self-help. Davies, Recovering the Original Fourth Amendment, <extracted-citation index="9" url="https://cite.case.law/citations/?q=98%20Mich.%20L.%20Rev.%20547"><span class="citation no-link">98 Mich. L. Rev. 547</span></extracted-citation>, 625 (1999). In the 20th century, however, the exclusionary rule-the rule that often requires trial courts to exclude unlawfully seized evidence in a criminal trial-became the principal judicial remedy to deter Fourth Amendment violations. See, <em>e.g.,</em> <em>Mapp v. Ohio,</em> <extracted-citation case-ids="1785580" index="10" url="https://cite.case.law/us/367/643/#p655"><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U.S. 643</a></span></extracted-citation>, 655, <extracted-citation case-ids="1785580" index="11" url="https://cite.case.law/us/367/643/#p655"><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">81 S.Ct. 1684</a></span></extracted-citation>, <extracted-citation case-ids="1785580" index="12" url="https://cite.case.law/us/367/643/#p655"><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">6 L.Ed.2d 1081</a></span></extracted-citation> (1961).</p>
<p id="p-22">Under the Court's precedents, the exclusionary rule encompasses both the "primary evidence obtained as a direct result of an illegal search or seizure" and, relevant here, "evidence later discovered and found to be derivative of an illegality," the so-called " 'fruit of the poisonous tree.' " <em>Segura v. United States,</em> <extracted-citation case-ids="11340278" index="13" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">468 U.S. 796</a></span></extracted-citation>, 804, <extracted-citation case-ids="11340278" index="14" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>, <extracted-citation case-ids="11340278" index="15" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">82 L.Ed.2d 599</a></span></extracted-citation> (1984). But the significant costs of this rule have led us to deem it "applicable only ... where its deterrence benefits outweigh its substantial social costs." <em>Hudson v. Michigan,</em> <extracted-citation case-ids="3276422" index="16" url="https://cite.case.law/us/547/586/#p591"><span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/" aria-description="Citation for case: Hudson v. Michigan">547 U.S. 586</a></span></extracted-citation>, 591, <extracted-citation case-ids="3276422" index="17" url="https://cite.case.law/us/547/586/#p591"><span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/" aria-description="Citation for case: Hudson v. Michigan">126 S.Ct. 2159</a></span></extracted-citation>, <extracted-citation case-ids="3276422" index="18" url="https://cite.case.law/us/547/586/#p591"><span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/" aria-description="Citation for case: Hudson v. Michigan">165 L.Ed.2d 56</a></span></extracted-citation> (2006) (internal quotation marks omitted). "Suppression of evidence ... has always been our last resort, not our first impulse." <em><extracted-citation case-ids="3276422" index="19" url="https://cite.case.law/us/547/586/#p591"><span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/" aria-description="Citation for case: Hudson v. Michigan">Ibid.</a></span></extracted-citation></em></p>
<p id="p-23">We have accordingly recognized several exceptions to the rule. Three of these exceptions involve the causal relationship between the unconstitutional act and the discovery of evidence. First, the independent source doctrine allows trial courts to admit evidence obtained in an unlawful search if officers independently acquired it from a separate, independent source. See <em>Murray v. United States,</em> <extracted-citation case-ids="1775229" index="20" url="https://cite.case.law/us/487/533/#p537"><span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/" aria-description="Citation for case: Murray v. United States">487 U.S. 533</a></span></extracted-citation>, 537, <extracted-citation case-ids="1775229" index="21" url="https://cite.case.law/us/487/533/#p537"><span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/" aria-description="Citation for case: Murray v. United States">108 S.Ct. 2529</a></span></extracted-citation>, <extracted-citation case-ids="1775229" index="22" url="https://cite.case.law/us/487/533/#p537"><span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/" aria-description="Citation for case: Murray v. United States">101 L.Ed.2d 472</a></span></extracted-citation> (1988). Second, the inevitable discovery doctrine allows for the admission of evidence that would have been discovered even without the unconstitutional source. See <em>Nix v. Williams,</em> <extracted-citation case-ids="6201711" index="23" url="https://cite.case.law/us/467/431/#p443"><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">467 U.S. 431</a></span></extracted-citation>, 443-444, <extracted-citation case-ids="6201711" index="24" url="https://cite.case.law/us/467/431/#p443"><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">104 S.Ct. 2501</a></span></extracted-citation>, <extracted-citation case-ids="6201711" index="25" url="https://cite.case.law/us/467/431/#p443"><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">81 L.Ed.2d 377</a></span></extracted-citation> (1984). Third, and at issue here, is the attenuation doctrine: Evidence is admissible when the connection between unconstitutional police conduct and the evidence is remote or has been interrupted by some intervening circumstance, so that "the interest protected by the constitutional guarantee that has been violated would not be served by suppression of the evidence obtained." <span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/#593" aria-description="Citation for case: Hudson v. Michigan"><em>Hudson, supra,</em> at 593</a></span>, <extracted-citation case-ids="3276422" index="26" url="https://cite.case.law/us/547/586/#p591"><span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/" aria-description="Citation for case: Hudson v. Michigan">126 S.Ct. 2159</a></span></extracted-citation>.</p>
<p id="p-24">B</p>
<p id="p-25">Turning to the application of the attenuation doctrine to this case, we first address a threshold question: whether this doctrine applies at all to a case like this, where the intervening circumstance that the State relies on is the discovery of a valid, pre-existing, and untainted arrest warrant. The Utah Supreme Court declined to apply the attenuation doctrine because it read our precedents as applying the doctrine only "to circumstances involving an independent act of a defendant's 'free will' in confessing to a crime or consenting to a search." <extracted-citation case-ids="6842912" index="27" url="https://cite.case.law/p3d/357/532/"><span class="citation" data-id="2770744"><a href="/opinion/2770744/state-v-strieff/" aria-description="Citation for case: State v. Strieff">357 P.3d, at 544</a></span></extracted-citation>. In this Court, Strieff has not defended this argument, and we disagree with it, as well. The attenuation doctrine evaluates the causal link between the government's unlawful act and the discovery of evidence, which often has nothing to do with a defendant's actions. And the logic of our prior attenuation cases is not limited to independent acts by the defendant.</p>
<p id="p-26">It remains for us to address whether the discovery of a valid arrest warrant was a sufficient intervening event to break the causal chain between the unlawful stop and the discovery of drug-related evidence on Strieff's person. The three factors articulated in <a class="page-label" data-citation-index="1" data-label="2062" href="#p2062" id="p2062">*2062</a><em>Brown v. Illinois,</em> <extracted-citation case-ids="9639" index="28" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590</a></span></extracted-citation>, <extracted-citation case-ids="9639" index="29" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>, <extracted-citation case-ids="9639" index="30" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">45 L.Ed.2d 416</a></span></extracted-citation> (1975), guide our analysis. First, we look to the "temporal proximity" between the unconstitutional conduct and the discovery of evidence to determine how closely the discovery of evidence followed the unconstitutional search. <em><extracted-citation case-ids="9639" index="31" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="9639" index="31" url="https://cite.case.law/us/422/590/"> at 603</extracted-citation>, <extracted-citation case-ids="9639" index="32" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>. Second, we consider "the presence of intervening circumstances." <em><extracted-citation case-ids="9639" index="33" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="9639" index="33" url="https://cite.case.law/us/422/590/"> at 603-604</extracted-citation>, <extracted-citation case-ids="9639" index="34" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>. Third, and "particularly" significant, we examine "the purpose and flagrancy of the official misconduct." <em><extracted-citation case-ids="9639" index="35" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="9639" index="35" url="https://cite.case.law/us/422/590/"> at 604</extracted-citation>, <extracted-citation case-ids="9639" index="36" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>. In evaluating these factors, we assume without deciding (because the State conceded the point) that Officer Fackrell lacked reasonable suspicion to initially stop Strieff. And, because we ultimately conclude that the warrant breaks the causal chain, we also have no need to decide whether the warrant's existence alone would make the initial stop constitutional even if Officer Fackrell was unaware of its existence.</p>
<p id="p-27">1</p>
<p id="p-28">The first factor, temporal proximity between the initially unlawful stop and the search, favors suppressing the evidence. Our precedents have declined to find that this factor favors attenuation unless "substantial time" elapses between an unlawful act and when the evidence is obtained. <em>Kaupp v. Texas,</em> <extracted-citation case-ids="9031233" index="37" url="https://cite.case.law/us/538/626/#p633"><span class="citation" data-id="127919"><a href="/opinion/127919/kaupp-v-texas/" aria-description="Citation for case: Kaupp v. Texas">538 U.S. 626</a></span></extracted-citation>, 633, <extracted-citation case-ids="9031233" index="38" url="https://cite.case.law/us/538/626/#p633"><span class="citation" data-id="127919"><a href="/opinion/127919/kaupp-v-texas/" aria-description="Citation for case: Kaupp v. Texas">123 S.Ct. 1843</a></span></extracted-citation>, <extracted-citation case-ids="9031233" index="39" url="https://cite.case.law/us/538/626/#p633"><span class="citation" data-id="127919"><a href="/opinion/127919/kaupp-v-texas/" aria-description="Citation for case: Kaupp v. Texas">155 L.Ed.2d 814</a></span></extracted-citation> (2003) (<em>per curiam</em> ). Here, however, Officer Fackrell discovered drug contraband on Strieff's person only minutes after the illegal stop. See App. 18-19. As the Court explained in <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>,</em> such a short time interval counsels in favor of suppression; there, we found that the confession should be suppressed, relying in part on the "less than two hours" that separated the unconstitutional arrest and the confession. <extracted-citation case-ids="9639" index="40" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U.S., at 604</a></span></extracted-citation>, <extracted-citation case-ids="9639" index="41" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>.</p>
<p id="p-29">In contrast, the second factor, the presence of intervening circumstances, strongly favors the State. In <em>Segura,</em> <extracted-citation case-ids="11340278" index="42" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">468 U.S. 796</a></span></extracted-citation>, <extracted-citation case-ids="11340278" index="43" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>, <extracted-citation case-ids="11340278" index="44" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">82 L.Ed.2d 599</a></span></extracted-citation>, the Court addressed similar facts to those here and found sufficient intervening circumstances to allow the admission of evidence. There, agents had probable cause to believe that apartment occupants were dealing cocaine. <em><extracted-citation case-ids="11340278" index="45" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11340278" index="45" url="https://cite.case.law/us/468/796/#p804"> at 799-800</extracted-citation>, <extracted-citation case-ids="11340278" index="46" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>. They sought a warrant. In the meantime, they entered the apartment, arrested an occupant, and discovered evidence of drug activity during a limited search for security reasons. <em><extracted-citation case-ids="11340278" index="47" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11340278" index="47" url="https://cite.case.law/us/468/796/#p804"> at 800-801</extracted-citation>, <extracted-citation case-ids="11340278" index="48" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>. The next evening, the Magistrate Judge issued the search warrant. <em><extracted-citation case-ids="11340278" index="49" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Ibid.</a></span></extracted-citation></em> This Court deemed the evidence admissible notwithstanding the illegal search because the information supporting the warrant was "wholly unconnected with the [arguably illegal] entry and was known to the agents well before the initial entry." <em><extracted-citation case-ids="11340278" index="50" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11340278" index="50" url="https://cite.case.law/us/468/796/#p804"> at 814</extracted-citation>, <extracted-citation case-ids="11340278" index="51" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>.</p>
<p id="p-30"><em><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Segura</a></span>,</em> of course, applied the independent source doctrine because the unlawful entry "did not contribute in any way to discovery of the evidence seized under the warrant." <em><extracted-citation case-ids="11340278" index="52" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11340278" index="52" url="https://cite.case.law/us/468/796/#p804"> at 815</extracted-citation>, <extracted-citation case-ids="11340278" index="53" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>. But the <em><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Segura</a></span></em> Court suggested that the existence of a valid warrant favors finding that the connection between unlawful conduct and the discovery of evidence is "sufficiently attenuated to dissipate the taint." <em><extracted-citation case-ids="11340278" index="54" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Ibid.</a></span></extracted-citation></em> That principle applies here.</p>
<p id="p-31">In this case, the warrant was valid, it predated Officer Fackrell's investigation, and it was entirely unconnected with the stop. And once Officer Fackrell discovered the warrant, he had an obligation to arrest Strieff. "A warrant is a judicial mandate to an officer to conduct a search or make an arrest, and the officer has a sworn duty to carry out its provisions." <em>United States v. Leon,</em> <extracted-citation case-ids="11340969" index="55" url="https://cite.case.law/us/468/897/#p920"><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U.S. 897</a></span></extracted-citation>, 920, n. 21, <extracted-citation case-ids="11340969" index="56" url="https://cite.case.law/us/468/897/#p920"><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span></extracted-citation>, <extracted-citation case-ids="11340969" index="57" url="https://cite.case.law/us/468/897/#p920"><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">82 L.Ed.2d 677</a></span></extracted-citation> (1984) (internal quotation marks omitted). Officer <a class="page-label" data-citation-index="1" data-label="2063" href="#p2063" id="p2063">*2063</a>Fackrell's arrest of Strieff thus was a ministerial act that was independently compelled by the pre-existing warrant. And once Officer Fackrell was authorized to arrest Strieff, it was undisputedly lawful to search Strieff as an incident of his arrest to protect Officer Fackrell's safety. See <em>Arizona v. Gant,</em> <extracted-citation case-ids="3653882" index="58" url="https://cite.case.law/us/556/332/#p339"><span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">556 U.S. 332</a></span></extracted-citation>, 339, <extracted-citation case-ids="3653882" index="59" url="https://cite.case.law/us/556/332/#p339"><span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">129 S.Ct. 1710</a></span></extracted-citation>, <extracted-citation case-ids="3653882" index="60" url="https://cite.case.law/us/556/332/#p339"><span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">173 L.Ed.2d 485</a></span></extracted-citation> (2009) (explaining the permissible scope of searches incident to arrest).</p>
<p id="p-32">Finally, the third factor, "the purpose and flagrancy of the official misconduct," <em>Brown, <extracted-citation case-ids="9639" index="61" url="https://cite.case.law/us/422/590/">supra,</extracted-citation></em><extracted-citation case-ids="9639" index="61" url="https://cite.case.law/us/422/590/"> at 604</extracted-citation>, <extracted-citation case-ids="9639" index="62" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>, also strongly favors the State. The exclusionary rule exists to deter police misconduct. <em>Davis v. United States,</em> <extracted-citation case-ids="5928256,12450488" index="63" url="https://cite.case.law/us/564/229/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">564 U.S. 229</a></span></extracted-citation>, 236-237, <extracted-citation case-ids="5928256,12450488" index="64" url="https://cite.case.law/us/564/229/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">131 S.Ct. 2419</a></span></extracted-citation>, <extracted-citation case-ids="12450488,5928256" index="65" url="https://cite.case.law/l-ed-2d/180/285/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">180 L.Ed.2d 285</a></span></extracted-citation> (2011). The third factor of the attenuation doctrine reflects that rationale by favoring exclusion only when the police misconduct is most in need of deterrence-that is, when it is purposeful or flagrant.</p>
<p id="p-33">Officer Fackrell was at most negligent. In stopping Strieff, Officer Fackrell made two good-faith mistakes. First, he had not observed what time Strieff entered the suspected drug house, so he did not know how long Strieff had been there. Officer Fackrell thus lacked a sufficient basis to conclude that Strieff was a short-term visitor who may have been consummating a drug transaction. Second, because he lacked confirmation that Strieff was a short-term visitor, Officer Fackrell should have asked Strieff whether he would speak with him, instead of demanding that Strieff do so. Officer Fackrell's stated purpose was to "find out what was going on [in] the house." App. 17. Nothing prevented him from approaching Strieff simply to ask. See <em>Florida v. Bostick,</em> <extracted-citation case-ids="1108039" index="66" url="https://cite.case.law/us/501/429/#p434"><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">501 U.S. 429</a></span></extracted-citation>, 434, <extracted-citation case-ids="1108039" index="67" url="https://cite.case.law/us/501/429/#p434"><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">111 S.Ct. 2382</a></span></extracted-citation>, <extracted-citation case-ids="1108039" index="68" url="https://cite.case.law/us/501/429/#p434"><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">115 L.Ed.2d 389</a></span></extracted-citation> (1991) ("[A] seizure does not occur simply because a police officer approaches an individual and asks a few questions"). But these errors in judgment hardly rise to a purposeful or flagrant violation of Strieff's Fourth Amendment rights.</p>
<p id="p-34">While Officer Fackrell's decision to initiate the stop was mistaken, his conduct thereafter was lawful. The officer's decision to run the warrant check was a "negligibly burdensome precautio[n]" for officer safety. <em>Rodriguez v. United States,</em> 575 U.S. ----, ----, <extracted-citation case-ids="12588788" index="69" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">135 S.Ct. 1609</a></span></extracted-citation>, 1616, <extracted-citation case-ids="12588788" index="70" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">191 L.Ed.2d 492</a></span></extracted-citation> (2015). And Officer Fackrell's actual search of Strieff was a lawful search incident to arrest. See <em>Gant, <extracted-citation case-ids="3653882" index="71" url="https://cite.case.law/us/556/332/#p339">supra,</extracted-citation></em><extracted-citation case-ids="3653882" index="71" url="https://cite.case.law/us/556/332/#p339"> at 339</extracted-citation>, <extracted-citation case-ids="3653882" index="72" url="https://cite.case.law/us/556/332/#p339"><span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">129 S.Ct. 1710</a></span></extracted-citation>.</p>
<p id="p-35">Moreover, there is no indication that this unlawful stop was part of any systemic or recurrent police misconduct. To the contrary, all the evidence suggests that the stop was an isolated instance of negligence that occurred in connection with a bona fide investigation of a suspected drug house. Officer Fackrell saw Strieff leave a suspected drug house. And his suspicion about the house was based on an anonymous tip and his personal observations.</p>
<p id="p-36">Applying these factors, we hold that the evidence discovered on Strieff's person was admissible because the unlawful stop was sufficiently attenuated by the pre-existing arrest warrant. Although the illegal stop was close in time to Strieff's arrest, that consideration is outweighed by two factors supporting the State. The outstanding arrest warrant for Strieff's arrest is a critical intervening circumstance that is wholly independent of the illegal stop. The discovery of that warrant broke the causal chain between the unconstitutional stop and the discovery of evidence by compelling Officer Fackrell to arrest Strieff. And, it is especially significant that there is no evidence that Officer Fackrell's illegal stop reflected flagrantly unlawful police misconduct.</p>
<p id="p-37"><a class="page-label" data-citation-index="1" data-label="2064" href="#p2064" id="p2064">*2064</a>2</p>
<p id="p-38">We find Strieff's counterarguments unpersuasive.</p>
<p id="p-39">First, he argues that the attenuation doctrine should not apply because the officer's stop was purposeful and flagrant. He asserts that Officer Fackrell stopped him solely to fish for evidence of suspected wrongdoing. But Officer Fackrell sought information from Strieff to find out what was happening inside a house whose occupants were legitimately suspected of dealing drugs. This was not a suspicionless fishing expedition "in the hope that something would turn up." <em>Taylor v. Alabama,</em> <extracted-citation case-ids="6193489" index="73" url="https://cite.case.law/us/457/687/#p691"><span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/" aria-description="Citation for case: Taylor v. Alabama">457 U.S. 687</a></span></extracted-citation>, 691, <extracted-citation case-ids="6193489" index="74" url="https://cite.case.law/us/457/687/#p691"><span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/" aria-description="Citation for case: Taylor v. Alabama">102 S.Ct. 2664</a></span></extracted-citation>, <extracted-citation case-ids="6193489" index="75" url="https://cite.case.law/us/457/687/#p691"><span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/" aria-description="Citation for case: Taylor v. Alabama">73 L.Ed.2d 314</a></span></extracted-citation> (1982).</p>
<p id="p-40">Strieff argues, moreover, that Officer Fackrell's conduct was flagrant because he detained Strieff without the necessary level of cause (here, reasonable suspicion). But that conflates the standard for an illegal stop with the standard for flagrancy. For the violation to be flagrant, more severe police misconduct is required than the mere absence of proper cause for the seizure. See, <em>e.g.,</em> <em>Kaupp,</em> <extracted-citation case-ids="9031233" index="76" url="https://cite.case.law/us/538/626/#p633"><span class="citation" data-id="127919"><a href="/opinion/127919/kaupp-v-texas/#628" aria-description="Citation for case: Kaupp v. Texas">538 U.S., at 628</a></span>, 633</extracted-citation>, <extracted-citation case-ids="9031233" index="77" url="https://cite.case.law/us/538/626/#p633"><span class="citation" data-id="127919"><a href="/opinion/127919/kaupp-v-texas/" aria-description="Citation for case: Kaupp v. Texas">123 S.Ct. 1843</a></span></extracted-citation> (finding flagrant violation where a warrantless arrest was made in the arrestee's home after police were denied a warrant and at least some officers knew they lacked probable cause). Neither the officer's alleged purpose nor the flagrancy of the violation rise to a level of misconduct to warrant suppression.</p>
<p id="p-41">Second, Strieff argues that, because of the prevalence of outstanding arrest warrants in many jurisdictions, police will engage in dragnet searches if the exclusionary rule is not applied. We think that this outcome is unlikely. Such wanton conduct would expose police to civil liability. See <extracted-citation index="78" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation> ; <em>Monell v. New York City Dept. of Social Servs.,</em> <extracted-citation case-ids="1490618" index="79" url="https://cite.case.law/us/436/658/#p690"><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U.S. 658</a></span></extracted-citation>, 690, <extracted-citation case-ids="1490618" index="80" url="https://cite.case.law/us/436/658/#p690"><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">98 S.Ct. 2018</a></span></extracted-citation>, <extracted-citation case-ids="1490618" index="81" url="https://cite.case.law/us/436/658/#p690"><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">56 L.Ed.2d 611</a></span></extracted-citation> (1978) ; see also <em>Segura,</em> <extracted-citation case-ids="11340278" index="82" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">468 U.S., at 812</a></span></extracted-citation>, <extracted-citation case-ids="11340278" index="83" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>. And in any event, the <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></em> factors take account of the purpose and flagrancy of police misconduct. Were evidence of a dragnet search presented here, the application of the <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></em> factors could be different. But there is no evidence that the concerns that Strieff raises with the criminal justice system are present in South Salt Lake City, Utah.</p>
<p id="p-42">* * *</p>
<p id="p-43">We hold that the evidence Officer Fackrell seized as part of his search incident to arrest is admissible because his discovery of the arrest warrant attenuated the connection between the unlawful stop and the evidence seized from Strieff incident to arrest. The judgment of the Utah Supreme Court, accordingly, is reversed.</p>
<p id="p-44"><em>It is so ordered.</em></p>
<p id="p-45">Justice SOTOMAYOR, with whom Justice GINSBURG joins as to Parts I, II, and III, dissenting.</p>
<p id="p-46">The Court today holds that the discovery of a warrant for an unpaid parking ticket will forgive a police officer's violation of your Fourth Amendment rights. Do not be soothed by the opinion's technical language: This case allows the police to stop you on the street, demand your identification, and check it for outstanding traffic warrants-even if you are doing nothing wrong. If the officer discovers a warrant for a fine you forgot to pay, courts will now excuse his illegal stop and will admit into evidence anything he happens to find by searching you after arresting you on the warrant. Because the Fourth Amendment should prohibit, not permit, such misconduct, I dissent.</p>
<p id="p-47">I</p>
<p id="p-48">Minutes after Edward Strieff walked out of a South Salt Lake City home, an officer stopped him, questioned him, and took his <a class="page-label" data-citation-index="1" data-label="2065" href="#p2065" id="p2065">*2065</a>identification to run it through a police database. The officer did not suspect that Strieff had done anything wrong. Strieff just happened to be the first person to leave a house that the officer thought might contain "drug activity." App. 16-19.</p>
<p id="p-49">As the State of Utah concedes, this stop was illegal. App. 24. The Fourth Amendment protects people from "unreasonable searches and seizures." An officer breaches that protection when he detains a pedestrian to check his license without any evidence that the person is engaged in a crime. <em>Delaware v. Prouse,</em> <extracted-citation case-ids="6187389" index="84" url="https://cite.case.law/us/440/648/#p663"><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U.S. 648</a></span></extracted-citation>, 663, <extracted-citation case-ids="6187389" index="85" url="https://cite.case.law/us/440/648/#p663"><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">99 S.Ct. 1391</a></span></extracted-citation>, <extracted-citation case-ids="6187389" index="86" url="https://cite.case.law/us/440/648/#p663"><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">59 L.Ed.2d 660</a></span></extracted-citation> (1979) ; <em>Terry v. Ohio,</em> <extracted-citation case-ids="6167798" index="87" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span></extracted-citation>, 21, <extracted-citation case-ids="6167798" index="88" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation>, <extracted-citation case-ids="6167798" index="89" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span></extracted-citation> (1968). The officer deepens the breach when he prolongs the detention just to fish further for evidence of wrongdoing. <em>Rodriguez v. United States,</em> 575 U.S. ----, ---- - ----, <extracted-citation case-ids="12588788" index="90" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">135 S.Ct. 1609</a></span></extracted-citation>, 1615-1616, <extracted-citation case-ids="12588788" index="91" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">191 L.Ed.2d 492</a></span></extracted-citation> (2015). In his search for lawbreaking, the officer in this case himself broke the law.</p>
<p id="p-50">The officer learned that Strieff had a "small traffic warrant." App. 19. Pursuant to that warrant, he arrested Strieff and, conducting a search incident to the arrest, discovered methamphetamine in Strieff's pockets.</p>
<p id="p-51">Utah charged Strieff with illegal drug possession. Before trial, Strieff argued that admitting the drugs into evidence would condone the officer's misbehavior. The methamphetamine, he reasoned, was the product of the officer's illegal stop. Admitting it would tell officers that unlawfully discovering even a "small traffic warrant" would give them license to search for evidence of unrelated offenses. The Utah Supreme Court unanimously agreed with Strieff. A majority of this Court now reverses.</p>
<p id="p-52">II</p>
<p id="p-53">It is tempting in a case like this, where illegal conduct by an officer uncovers illegal conduct by a civilian, to forgive the officer. After all, his instincts, although unconstitutional, were correct. But a basic principle lies at the heart of the Fourth Amendment: Two wrongs don't make a right. See <em>Weeks v. United States,</em> <extracted-citation case-ids="3672825" index="92" url="https://cite.case.law/us/232/383/#p392"><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U.S. 383</a></span></extracted-citation>, 392, <extracted-citation case-ids="3672825" index="93" url="https://cite.case.law/us/232/383/#p392"><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">34 S.Ct. 341</a></span></extracted-citation>, <extracted-citation case-ids="3672825" index="94" url="https://cite.case.law/us/232/383/#p392"><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">58 L.Ed. 652</a></span></extracted-citation> (1914). When "lawless police conduct" uncovers evidence of lawless civilian conduct, this Court has long required later criminal trials to exclude the illegally obtained evidence. <em>Terry,</em> <extracted-citation case-ids="6167798" index="95" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S., at 12</a></span></extracted-citation>, <extracted-citation case-ids="6167798" index="96" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation> ; <em>Mapp v. Ohio,</em> <extracted-citation case-ids="1785580" index="97" url="https://cite.case.law/us/367/643/#p655"><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U.S. 643</a></span></extracted-citation>, 655, <extracted-citation case-ids="1785580" index="98" url="https://cite.case.law/us/367/643/#p655"><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">81 S.Ct. 1684</a></span></extracted-citation>, <extracted-citation case-ids="1785580" index="99" url="https://cite.case.law/us/367/643/#p655"><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">6 L.Ed.2d 1081</a></span></extracted-citation> (1961). For example, if an officer breaks into a home and finds a forged check lying around, that check may not be used to prosecute the homeowner for bank fraud. We would describe the check as " 'fruit of the poisonous tree.' " <em>Wong Sun v. United States,</em> <extracted-citation case-ids="450611" index="100" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U.S. 471</a></span></extracted-citation>, 488, <extracted-citation case-ids="450611" index="101" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407</a></span></extracted-citation>, <extracted-citation case-ids="450611" index="102" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">9 L.Ed.2d 441</a></span></extracted-citation> (1963). Fruit that must be cast aside includes not only evidence directly found by an illegal search but also evidence "come at by exploitation of that illegality." <em>Ibid</em> .</p>
<p id="p-54">This "exclusionary rule" removes an incentive for officers to search us without proper justification. <em>Terry,</em> <extracted-citation case-ids="6167798" index="103" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S., at 12</a></span></extracted-citation>, <extracted-citation case-ids="6167798" index="104" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation>. It also keeps courts from being "made party to lawless invasions of the constitutional rights of citizens by permitting unhindered governmental use of the fruits of such invasions." <em><extracted-citation case-ids="6167798" index="105" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="6167798" index="105" url="https://cite.case.law/us/392/1/#p21"> at 13</extracted-citation>, <extracted-citation case-ids="6167798" index="106" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation>. When courts admit only lawfully obtained evidence, they encourage "those who formulate law enforcement polices, and the officers who implement them, to incorporate Fourth Amendment ideals into their value system." <em>Stone v. Powell,</em> <extracted-citation case-ids="6178753" index="107" url="https://cite.case.law/us/428/465/#p492"><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U.S. 465</a></span></extracted-citation>, 492, <extracted-citation case-ids="6178753" index="108" url="https://cite.case.law/us/428/465/#p492"><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">96 S.Ct. 3037</a></span></extracted-citation>, <extracted-citation case-ids="6178753" index="109" url="https://cite.case.law/us/428/465/#p492"><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">49 L.Ed.2d 1067</a></span></extracted-citation> (1976). But when courts admit illegally obtained evidence as well, they reward "manifest neglect if not an open defiance of the prohibitions of the <a class="page-label" data-citation-index="1" data-label="2066" href="#p2066" id="p2066">*2066</a>Constitution." <em>Weeks,</em> <extracted-citation case-ids="3672825" index="110" url="https://cite.case.law/us/232/383/#p392"><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U.S., at 394</a></span></extracted-citation>, <extracted-citation case-ids="3672825" index="111" url="https://cite.case.law/us/232/383/#p392"><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">34 S.Ct. 341</a></span></extracted-citation>.</p>
<p id="p-55">Applying the exclusionary rule, the Utah Supreme Court correctly decided that Strieff's drugs must be excluded because the officer exploited his illegal stop to discover them. The officer found the drugs only after learning of Strieff's traffic violation; and he learned of Strieff's traffic violation only because he unlawfully stopped Strieff to check his driver's license.</p>
<p id="p-56">The court also correctly rejected the State's argument that the officer's discovery of a traffic warrant unspoiled the poisonous fruit. The State analogizes finding the warrant to one of our earlier decisions, <em>Wong Sun v. United States</em> . There, an officer illegally arrested a person who, days later, voluntarily returned to the station to confess to committing a crime. <extracted-citation case-ids="450611" index="112" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U.S., at 491</a></span></extracted-citation>, <extracted-citation case-ids="450611" index="113" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407</a></span></extracted-citation>. Even though the person would not have confessed "but for the illegal actions of the police," <em><extracted-citation case-ids="450611" index="114" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">id.,</a></span></extracted-citation></em><extracted-citation case-ids="450611" index="114" url="https://cite.case.law/us/371/471/#p488"> at 488</extracted-citation>, <extracted-citation case-ids="450611" index="115" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407</a></span></extracted-citation> we noted that the police did not exploit their illegal arrest to obtain the confession, <em><extracted-citation case-ids="450611" index="116" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">id.,</a></span></extracted-citation></em><extracted-citation case-ids="450611" index="116" url="https://cite.case.law/us/371/471/#p488"> at 491</extracted-citation>, <extracted-citation case-ids="450611" index="117" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407</a></span></extracted-citation><em>.</em> Because the confession was obtained by "means sufficiently distinguishable" from the constitutional violation, we held that it could be admitted into evidence. <em><extracted-citation case-ids="450611" index="118" url="https://cite.case.law/us/371/471/#p488">Id.,</extracted-citation></em><extracted-citation case-ids="450611" index="118" url="https://cite.case.law/us/371/471/#p488"> at 488, 491</extracted-citation>, <extracted-citation case-ids="450611" index="119" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407</a></span></extracted-citation>. The State contends that the search incident to the warrant-arrest here is similarly distinguishable from the illegal stop.</p>
<p id="p-57">But <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></em> explains why Strieff's drugs must be excluded. We reasoned that a Fourth Amendment violation may not color every investigation that follows but it certainly stains the actions of officers who exploit the infraction. We distinguished evidence obtained by innocuous means from evidence obtained by exploiting misconduct after considering a variety of factors: whether a long time passed, whether there were "intervening circumstances," and whether the purpose or flagrancy of the misconduct was "calculated" to procure the evidence. <em>Brown v. Illinois,</em> <extracted-citation case-ids="9639" index="120" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590</a></span></extracted-citation>, 603-604, <extracted-citation case-ids="9639" index="121" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>, <extracted-citation case-ids="9639" index="122" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">45 L.Ed.2d 416</a></span></extracted-citation> (1975).</p>
<p id="p-58">These factors confirm that the officer in this case discovered Strieff's drugs by exploiting his own illegal conduct. The officer did not ask Strieff to volunteer his name only to find out, days later, that Strieff had a warrant against him. The officer illegally stopped Strieff and immediately ran a warrant check. The officer's discovery of a warrant was not some intervening surprise that he could not have anticipated. Utah lists over 180,000 misdemeanor warrants in its database, and at the time of the arrest, Salt Lake County had a "backlog of outstanding warrants" so large that it faced the "potential for civil liability." See Dept. of Justice, Bureau of Justice Statistics, Survey of State Criminal History Information Systems, 2014 (2015) (Systems Survey) (Table 5a), online at https://www.ncjrs.gov/pdffiles1/bjs/grants/249799.pdf (all Internet materials as last visited June 16, 2016); Inst. for Law and Policy Planning, Salt Lake County Criminal Justice System Assessment 6.7 (2004), online at http://www.slco.org/cjac/resources/SaltLakeCJSAfinal.pdf. The officer's violation was also calculated to procure evidence. His sole reason for stopping Strieff, he acknowledged, was investigative-he wanted to discover whether drug activity was going on in the house Strieff had just exited. App. 17.</p>
<p id="p-59">The warrant check, in other words, was not an "intervening circumstance" separating the stop from the search for drugs. It was part and parcel of the officer's illegal "expedition for evidence in the hope that something might turn up." <em>Brown,</em> <extracted-citation case-ids="9639" index="123" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U.S., at 605</a></span></extracted-citation>, <extracted-citation case-ids="9639" index="124" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>. Under our precedents, because the officer found Strieff's drugs by exploiting his own constitutional <a class="page-label" data-citation-index="1" data-label="2067" href="#p2067" id="p2067">*2067</a>violation, the drugs should be excluded.</p>
<p id="p-60">III</p>
<p id="p-61">A</p>
<p id="p-62">The Court sees things differently. To the Court, the fact that a warrant gives an officer cause to arrest a person severs the connection between illegal policing and the resulting discovery of evidence. <em>Ante,</em> at 2062-2063. This is a remarkable proposition: The mere existence of a warrant not only gives an officer legal cause to arrest and search a person, it also forgives an officer who, with no knowledge of the warrant at all, unlawfully stops that person on a whim or hunch.</p>
<p id="p-63">To explain its reasoning, the Court relies on <em>Segura v. United States,</em> <extracted-citation case-ids="11340278" index="125" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">468 U.S. 796</a></span></extracted-citation>, <extracted-citation case-ids="11340278" index="126" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>, <extracted-citation case-ids="11340278" index="127" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">82 L.Ed.2d 599</a></span></extracted-citation> (1984). There, federal agents applied for a warrant to search an apartment but illegally entered the apartment to secure it before the judge issued the warrant. <em><extracted-citation case-ids="11340278" index="128" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11340278" index="128" url="https://cite.case.law/us/468/796/#p804"> at 800-801</extracted-citation>, <extracted-citation case-ids="11340278" index="129" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>. After receiving the warrant, the agents then searched the apartment for drugs. <em><extracted-citation case-ids="11340278" index="130" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11340278" index="130" url="https://cite.case.law/us/468/796/#p804"> at 801</extracted-citation>, <extracted-citation case-ids="11340278" index="131" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>. The question before us was what to do with the evidence the agents then discovered. We declined to suppress it because "[t]he illegal entry into petitioners' apartment did not contribute in any way to discovery of the evidence seized under the warrant." <em><extracted-citation case-ids="11340278" index="132" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11340278" index="132" url="https://cite.case.law/us/468/796/#p804"> at 815</extracted-citation>, <extracted-citation case-ids="11340278" index="133" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>.</p>
<p id="p-64">According to the majority, <em><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Segura</a></span></em> involves facts "similar" to this case and "suggest[s]" that a valid warrant will clean up whatever illegal conduct uncovered it. <em>Ante,</em> at 2062 - 2063. It is difficult to understand this interpretation. In <em><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Segura</a></span>,</em> the agents' illegal conduct in entering the apartment had nothing to do with their procurement of a search warrant. Here, the officer's illegal conduct in stopping Strieff was essential to his discovery of an arrest warrant. <em><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Segura</a></span></em> would be similar only if the agents used information they illegally obtained from the apartment to procure a search warrant or discover an arrest warrant. Precisely because that was not the case, the Court admitted the untainted evidence. 468 U.S., at 814, <extracted-citation case-ids="11340278" index="134" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>.</p>
<p id="p-65">The majority likewise misses the point when it calls the warrant check here a " 'negligibly burdensome precautio[n]' " taken for the officer's "safety." <em>Ante,</em> at 2063 (quoting <em><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">Rodriguez</a></span>,</em> 575 U.S., at ----, <extracted-citation case-ids="12588788" index="135" url="https://cite.case.law/s-ct/135/1609/#p1616">135 S.Ct., at </extracted-citation>1615 ). Remember, the officer stopped Strieff without suspecting him of committing any crime. By his own account, the officer did not fear Strieff. Moreover, the safety rationale we discussed in <em><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">Rodriguez</a></span>,</em> an opinion about highway patrols, is conspicuously absent here. A warrant check on a highway "ensur[es] that vehicles on the road are operated safely and responsibly." <em><extracted-citation case-ids="12588788" index="136" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12588788" index="137" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">135 S.Ct., at 1615</a></span></extracted-citation>. We allow such checks during legal traffic stops because the legitimacy of a person's driver's license has a "close connection to roadway safety." <em><extracted-citation case-ids="12588788" index="138" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12588788" index="139" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">135 S.Ct., at 1615</a></span></extracted-citation>. A warrant check of a pedestrian on a sidewalk, "by contrast, is a measure aimed at 'detect[ing] evidence of ordinary criminal wrongdoing.' " <em><extracted-citation case-ids="12588788" index="140" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">Ibid.</a></span></extracted-citation></em> (quoting <em>Indianapolis v. Edmond,</em> <extracted-citation case-ids="9505377" index="141" url="https://cite.case.law/us/531/32/#p40"><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U.S. 32</a></span></extracted-citation>, 40-41, <extracted-citation case-ids="9505377" index="142" url="https://cite.case.law/us/531/32/#p40"><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S.Ct. 447</a></span></extracted-citation>, <extracted-citation case-ids="9505377" index="143" url="https://cite.case.law/us/531/32/#p40"><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L.Ed.2d 333</a></span></extracted-citation> (2000) ). Surely we would not allow officers to warrant-check random joggers, dog walkers, and lemonade vendors just to ensure they pose no threat to anyone else.</p>
<p id="p-66">The majority also posits that the officer could not have exploited his illegal conduct because he did not violate the Fourth Amendment on purpose. Rather, he made "good-faith mistakes." <em>Ante,</em> at 2063. Never mind that the officer's sole purpose was to fish for evidence. The majority casts his unconstitutional actions as "negligent"</p>
<p id="p-67"><a class="page-label" data-citation-index="1" data-label="2068" href="#p2068" id="p2068">*2068</a>and therefore incapable of being deterred by the exclusionary rule. <em><extracted-citation case-ids="9505377" index="144" url="https://cite.case.law/us/531/32/#p40"><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Ibid.</a></span></extracted-citation></em></p>
<p id="p-68">But the Fourth Amendment does not tolerate an officer's unreasonable searches and seizures just because he did not know any better. Even officers prone to negligence can learn from courts that exclude illegally obtained evidence. <em>Stone,</em> <extracted-citation case-ids="6178753" index="145" url="https://cite.case.law/us/428/465/#p492"><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U.S., at 492</a></span></extracted-citation>, <extracted-citation case-ids="6178753" index="146" url="https://cite.case.law/us/428/465/#p492"><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">96 S.Ct. 3037</a></span></extracted-citation>. Indeed, they are perhaps the most in need of the education, whether by the judge's opinion, the prosecutor's future guidance, or an updated manual on criminal procedure. If the officers are in doubt about what the law requires, exclusion gives them an "incentive to err on the side of constitutional behavior." <em>United States v. Johnson,</em> <extracted-citation case-ids="6191611" index="147" url="https://cite.case.law/us/457/537/#p561"><span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">457 U.S. 537</a></span></extracted-citation>, 561, <extracted-citation case-ids="6191611" index="148" url="https://cite.case.law/us/457/537/#p561"><span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">102 S.Ct. 2579</a></span></extracted-citation>, <extracted-citation case-ids="6191611" index="149" url="https://cite.case.law/us/457/537/#p561"><span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">73 L.Ed.2d 202</a></span></extracted-citation> (1982).</p>
<p id="p-69">B</p>
<p id="p-70">Most striking about the Court's opinion is its insistence that the event here was "isolated," with "no indication that this unlawful stop was part of any systemic or recurrent police misconduct." <em>Ante,</em> at 2063. Respectfully, nothing about this case is isolated.</p>
<p id="p-71">Outstanding warrants are surprisingly common. When a person with a traffic ticket misses a fine payment or court appearance, a court will issue a warrant. See, <em>e.g.,</em> Brennan Center for Justice, Criminal Justice Debt 23 (2010), online at https://www.brennancenter.org/sites/default/files/legacy/Fees% 20and% 20Fines% 20FINAL.pdf. When a person on probation drinks alcohol or breaks curfew, a court will issue a warrant. See, <em>e.g.,</em> Human Rights Watch, Profiting from Probation 1, 51 (2014), online at https://www.hrw.org/report/2014/02/05/profiting-probation/americas-offender-funded-probation-industry. The States and Federal Government maintain databases with over 7.8 million outstanding warrants, the vast majority of which appear to be for minor offenses. See Systems Survey (Table 5a). Even these sources may not track the "staggering" numbers of warrants, " 'drawers and drawers' " full, that many cities issue for traffic violations and ordinance infractions. Dept. of Justice, Civil Rights Div., Investigation of the Ferguson Police Department 47, 55 (2015) (Ferguson Report), online at https://www.justice.gov/sites/default/files/opa/press-releases/attachments/2015/03/04/ferguson_police_department_report.pdf. The county in this case has had a "backlog" of such warrants. See <em>supra,</em> at 2066. The Department of Justice recently reported that in the town of Ferguson, Missouri, with a population of 21,000, 16,000 people had outstanding warrants against them. Ferguson Report, at 6, 55.</p>
<p id="p-72">Justice Department investigations across the country have illustrated how these astounding numbers of warrants can be used by police to stop people without cause. In a single year in New Orleans, officers "made nearly 60,000 arrests, of which about 20,000 were of people with outstanding traffic or misdemeanor warrants from neighboring parishes for such infractions as unpaid tickets." Dept. of Justice, Civil Rights Div., Investigation of the New Orleans Police Department 29 (2011), online at https://www.justice.gov/sites/default/files/crt/legacy/2011/03/17/nopd_report.pdf. In the St. Louis metropolitan area, officers "routinely" stop people-on the street, at bus stops, or even in court-for no reason other than "an officer's desire to check whether the subject had a municipal arrest warrant pending." Ferguson Report, at 49, 57<em>.</em> In Newark, New Jersey, officers stopped 52,235 pedestrians within a 4-year period and ran warrant checks on 39,308 of them. Dept. of Justice, Civil Rights Div., Investigation of the Newark Police Department 8, 19, n. 15 <a class="page-label" data-citation-index="1" data-label="2069" href="#p2069" id="p2069">*2069</a>(2014), online at https://www.justice.gov/sites/default/files/crt/legacy/2014/07/22/newark_ findings_7-22-14.pdf. The Justice Department analyzed these warrant-checked stops and reported that "approximately 93% of the stops would have been considered unsupported by articulated reasonable suspicion." <em>Id.,</em> at 9, n. 7.</p>
<p id="p-73">I do not doubt that most officers act in "good faith" and do not set out to break the law. That does not mean these stops are "isolated instance[s] of negligence," however. <em>Ante,</em> at 2063. Many are the product of institutionalized training procedures. The New York City Police Department long trained officers to, in the words of a District Judge, "stop and question first, develop reasonable suspicion later." <em>Ligon v. New York,</em> <extracted-citation case-ids="4328781" index="150" url="https://cite.case.law/f-supp-2d/925/478/#p537"><span class="citation" data-id="8706198"><a href="/opinion/8723002/ligon-v-city-of-new-york/" aria-description="Citation for case: Ligon v. City of New York">925 F.Supp.2d 478</a></span></extracted-citation>, 537-538 (S.D.N.Y.), stay granted on other grounds, <extracted-citation case-ids="3726977" index="151" url="https://cite.case.law/f3d/736/118/"><span class="citation" data-id="8412659"><a href="/opinion/8441531/ligon-ex-rel-jg-v-city-of-new-york/" aria-description="Citation for case: Ligon ex rel. J.G. v. City of New York">736 F.3d 118</a></span></extracted-citation> (C.A.2 2013). The Utah Supreme Court described as " 'routine procedure' or 'common practice' " the decision of Salt Lake City police officers to run warrant checks on pedestrians they detained without reasonable suspicion. <em>State v. Topanotes,</em> <extracted-citation case-ids="9096354" index="152" url="https://cite.case.law/p3d/76/1159/"><span class="citation" data-id="2598446"><a href="/opinion/2598446/state-v-topanotes/" aria-description="Citation for case: State v. Topanotes">2003 UT 30</a></span></extracted-citation>, ¶ 2, <extracted-citation case-ids="9096354" index="153" url="https://cite.case.law/p3d/76/1159/"><span class="citation" data-id="2598446"><a href="/opinion/2598446/state-v-topanotes/" aria-description="Citation for case: State v. Topanotes">76 P.3d 1159</a></span></extracted-citation>, 1160. In the related context of traffic stops, one widely followed police manual instructs officers looking for drugs to "run at least a warrants check on all drivers you stop. Statistically, narcotics offenders are ... more likely to fail to appear on simple citations, such as traffic or trespass violations, leading to the issuance of bench warrants. Discovery of an outstanding warrant gives you cause for an immediate custodial arrest and search of the suspect." C. Remsberg, Tactics for Criminal Patrol 205-206 (1995); C. Epp et al., Pulled Over 23, 33-36 (2014).</p>
<p id="p-74">The majority does not suggest what makes this case "isolated" from these and countless other examples. Nor does it offer guidance for how a defendant can prove that his arrest was the result of "widespread" misconduct. Surely it should not take a federal investigation of Salt Lake County before the Court would protect someone in Strieff's position.</p>
<p id="p-75">IV</p>
<p id="p-76">Writing only for myself, and drawing on my professional experiences, I would add that unlawful "stops" have severe consequences much greater than the inconvenience suggested by the name. This Court has given officers an array of instruments to probe and examine you. When we condone officers' use of these devices without adequate cause, we give them reason to target pedestrians in an arbitrary manner. We also risk treating members of our communities as second-class citizens.</p>
<p id="p-77">Although many Americans have been stopped for speeding or jaywalking, few may realize how degrading a stop can be when the officer is looking for more. This Court has allowed an officer to stop you for whatever reason he wants-so long as he can point to a pretextual justification after the fact. <em>Whren v. United States,</em> <extracted-citation case-ids="11746960" index="154" url="https://cite.case.law/us/517/806/#p813"><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U.S. 806</a></span></extracted-citation>, 813, <extracted-citation case-ids="11746960" index="155" url="https://cite.case.law/us/517/806/#p813"><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S.Ct. 1769</a></span></extracted-citation>, <extracted-citation case-ids="11746960" index="156" url="https://cite.case.law/us/517/806/#p813"><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L.Ed.2d 89</a></span></extracted-citation> (1996). That justification must provide specific reasons why the officer suspected you were breaking the law, <em>Terry,</em> <extracted-citation case-ids="6167798" index="157" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S., at 21</a></span></extracted-citation>, <extracted-citation case-ids="6167798" index="158" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation> but it may factor in your ethnicity, <em>United States v. Brignoni-Ponce,</em> <extracted-citation case-ids="9550" index="159" url="https://cite.case.law/us/422/873/#p886"><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U.S. 873</a></span></extracted-citation>, 886-887, <extracted-citation case-ids="9550" index="160" url="https://cite.case.law/us/422/873/#p886"><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">95 S.Ct. 2574</a></span></extracted-citation>, <extracted-citation case-ids="9550" index="161" url="https://cite.case.law/us/422/873/#p886"><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">45 L.Ed.2d 607</a></span></extracted-citation> (1975), where you live, <em>Adams v. Williams,</em> <extracted-citation case-ids="9137003" index="162" url="https://cite.case.law/us/407/143/#p147"><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U.S. 143</a></span></extracted-citation>, 147, <extracted-citation case-ids="9137003" index="163" url="https://cite.case.law/us/407/143/#p147"><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">92 S.Ct. 1921</a></span></extracted-citation>, <extracted-citation case-ids="9137003" index="164" url="https://cite.case.law/us/407/143/#p147"><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">32 L.Ed.2d 612</a></span></extracted-citation> (1972), what you were wearing, <em>United States v. Sokolow,</em> <extracted-citation case-ids="605100" index="165" url="https://cite.case.law/us/490/1/#p4"><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">490 U.S. 1</a></span></extracted-citation>, 4-5, <extracted-citation case-ids="605100" index="166" url="https://cite.case.law/us/490/1/#p4"><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">109 S.Ct. 1581</a></span></extracted-citation>, <extracted-citation case-ids="605100" index="167" url="https://cite.case.law/us/490/1/#p4"><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">104 L.Ed.2d 1</a></span></extracted-citation> (1989), and how you behaved, <em>Illinois v. Wardlow,</em> <extracted-citation case-ids="9476180" index="168" url="https://cite.case.law/us/528/119/#p124"><span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/" aria-description="Citation for case: Illinois v. Wardlow">528 U.S. 119</a></span></extracted-citation>, 124-125, <extracted-citation case-ids="9476180" index="169" url="https://cite.case.law/us/528/119/#p124"><span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/" aria-description="Citation for case: Illinois v. Wardlow">120 S.Ct. 673</a></span></extracted-citation>, <extracted-citation case-ids="9476180" index="170" url="https://cite.case.law/us/528/119/#p124"><span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/" aria-description="Citation for case: Illinois v. Wardlow">145 L.Ed.2d 570</a></span></extracted-citation> (2000). The officer does not even need to know which law you might have broken so long as he can later point to any possible infraction-even one that is minor, unrelated, or ambiguous. <em>Devenpeck v. Alford,</em> <a class="page-label" data-citation-index="1" data-label="2070" href="#p2070" id="p2070">*2070</a><extracted-citation case-ids="5916678" index="171" url="https://cite.case.law/us/543/146/#p154"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">543 U.S. 146</a></span></extracted-citation>, 154-155, <extracted-citation case-ids="5916678" index="172" url="https://cite.case.law/us/543/146/#p154"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">125 S.Ct. 588</a></span></extracted-citation>, <extracted-citation case-ids="5916678" index="173" url="https://cite.case.law/us/543/146/#p154"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">160 L.Ed.2d 537</a></span></extracted-citation> (2004) ; <em>Heien v. North Carolina,</em> 574 U.S. ----, <extracted-citation case-ids="12593411" index="174" url="https://cite.case.law/s-ct/135/530/"><span class="citation" data-id="9805193"><a href="/opinion/2760668/heien-v-north-carolina/" aria-description="Citation for case: Heien v. North Carolina">135 S.Ct. 530</a></span></extracted-citation>, <extracted-citation case-ids="12593411" index="175" url="https://cite.case.law/s-ct/135/530/"><span class="citation" data-id="9805193"><a href="/opinion/2760668/heien-v-north-carolina/" aria-description="Citation for case: Heien v. North Carolina">190 L.Ed.2d 475</a></span></extracted-citation> (2014).</p>
<p id="p-78">The indignity of the stop is not limited to an officer telling you that you look like a criminal. See Epp, Pulled Over, at 5. The officer may next ask for your "consent" to inspect your bag or purse without telling you that you can decline. See <em>Florida v. Bostick,</em> <extracted-citation case-ids="1108039" index="176" url="https://cite.case.law/us/501/429/#p434"><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">501 U.S. 429</a></span></extracted-citation>, 438, <extracted-citation case-ids="1108039" index="177" url="https://cite.case.law/us/501/429/#p434"><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">111 S.Ct. 2382</a></span></extracted-citation>, <extracted-citation case-ids="1108039" index="178" url="https://cite.case.law/us/501/429/#p434"><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">115 L.Ed.2d 389</a></span></extracted-citation> (1991). Regardless of your answer, he may order you to stand "helpless, perhaps facing a wall with [your] hands raised." <em>Terry,</em> <extracted-citation case-ids="6167798" index="179" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S., at 17</a></span></extracted-citation>, <extracted-citation case-ids="6167798" index="180" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation>. If the officer thinks you might be dangerous, he may then "frisk" you for weapons. This involves more than just a pat down. As onlookers pass by, the officer may " 'feel with sensitive fingers every portion of [your] body. A thorough search [may] be made of [your] arms and armpits, waistline and back, the groin and area about the testicles, and entire surface of the legs down to the feet.' " <em><extracted-citation case-ids="6167798" index="181" url="https://cite.case.law/us/392/1/#p21">Id.,</extracted-citation></em><extracted-citation case-ids="6167798" index="181" url="https://cite.case.law/us/392/1/#p21"> at 17, n. 13</extracted-citation>, <extracted-citation case-ids="6167798" index="182" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation>.</p>
<p id="p-79">The officer's control over you does not end with the stop. If the officer chooses, he may handcuff you and take you to jail for doing nothing more than speeding, jaywalking, or "driving [your] pickup truck ... with [your] 3-year-old son and 5-year-old daughter ... without [your] seatbelt fastened." <em>Atwater v. Lago Vista,</em> <extracted-citation case-ids="9301256" index="183" url="https://cite.case.law/us/532/318/#p323"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">532 U.S. 318</a></span></extracted-citation>, 323-324, <extracted-citation case-ids="9301256" index="184" url="https://cite.case.law/us/532/318/#p323"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">121 S.Ct. 1536</a></span></extracted-citation>, <extracted-citation case-ids="9301256" index="185" url="https://cite.case.law/us/532/318/#p323"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">149 L.Ed.2d 549</a></span></extracted-citation> (2001). At the jail, he can fingerprint you, swab DNA from the inside of your mouth, and force you to "shower with a delousing agent" while you "lift [your] tongue, hold out [your] arms, turn around, and lift [your] genitals." <em>Florence v. Board of Chosen Freeholders of County of Burlington,</em> 566 U.S. ----, ---- - ----, <extracted-citation case-ids="12189139" index="186" url="https://cite.case.law/us/566/318/#p1514"><span class="citation" data-id="9485643"><a href="/opinion/626454/florence-v-board-of-chosen-freeholders-of-county-of-burlington/" aria-description="Citation for case: Florence v. Board of Chosen Freeholders of County of...">132 S.Ct. 1510</a></span></extracted-citation>, 1514, <extracted-citation case-ids="12189139" index="187" url="https://cite.case.law/us/566/318/#p1514"><span class="citation" data-id="9485643"><a href="/opinion/626454/florence-v-board-of-chosen-freeholders-of-county-of-burlington/" aria-description="Citation for case: Florence v. Board of Chosen Freeholders of County of...">182 L.Ed.2d 566</a></span></extracted-citation> (2012) ; <em>Maryland v. King,</em> 569 U.S. ----, ----, <extracted-citation case-ids="12697054" index="188" url="https://cite.case.law/us/569/435/#p1980"><span class="citation" data-id="873669"><a href="/opinion/873669/maryland-v-king/" aria-description="Citation for case: Maryland v. King">133 S.Ct. 1958</a></span></extracted-citation>, 1980, <extracted-citation case-ids="12697054" index="189" url="https://cite.case.law/us/569/435/#p1980"><span class="citation" data-id="873669"><a href="/opinion/873669/maryland-v-king/" aria-description="Citation for case: Maryland v. King">186 L.Ed.2d 1</a></span></extracted-citation> (2013). Even if you are innocent, you will now join the 65 million Americans with an arrest record and experience the "civil death" of discrimination by employers, landlords, and whoever else conducts a background check. Chin, The New Civil Death, <extracted-citation index="190" url="https://cite.case.law/citations/?q=160%20U.%20Pa.%20L.%20Rev.%201789"><span class="citation no-link">160 U. Pa. L. Rev. 1789</span></extracted-citation>, 1805 (2012) ; see J. Jacobs, The Eternal Criminal Record 33-51 (2015); Young &amp; Petersilia, Keeping Track, <extracted-citation index="191" url="https://cite.case.law/citations/?q=129%20Harv.%20L.%20Rev.%201318"><span class="citation no-link">129 Harv. L. Rev. 1318</span></extracted-citation>, 1341-1357 (2016). And, of course, if you fail to pay bail or appear for court, a judge will issue a warrant to render you "arrestable on sight" in the future. A. Goffman, On the Run 196 (2014).</p>
<p id="p-80">This case involves a <em>suspicionless</em> stop, one in which the officer initiated this chain of events without justification. As the Justice Department notes, <em><extracted-citation case-ids="9096354" index="192" url="https://cite.case.law/p3d/76/1159/">supra,</extracted-citation></em> at 2068 - 2069, many innocent people are subjected to the humiliations of these unconstitutional searches. The white defendant in this case shows that anyone's dignity can be violated in this manner. See M. Gottschalk, Caught 119-138 (2015). But it is no secret that people of color are disproportionate victims of this type of scrutiny. See M. Alexander, The New Jim Crow 95-136 (2010). For generations, black and brown parents have given their children "the talk"-instructing them never to run down the street; always keep your hands where they can be seen; do not even think of talking back to a stranger-all out of fear of how an officer with a gun will react to them. See, <em>e.g.,</em> W.E.B. Du Bois, The Souls of Black Folk (1903); J. Baldwin, The Fire Next Time (1963); T. Coates, Between the World and Me (2015).</p>
<p id="p-81">By legitimizing the conduct that produces this double consciousness, this case tells everyone, white and black, guilty and innocent, that an officer can verify your legal status at any time. It says that your body is subject to invasion while courts excuse the violation of your rights. It <a class="page-label" data-citation-index="1" data-label="2071" href="#p2071" id="p2071">*2071</a>implies that you are not a citizen of a democracy but the subject of a carceral state, just waiting to be cataloged.</p>
<p id="p-82">We must not pretend that the countless people who are routinely targeted by police are "isolated." They are the canaries in the coal mine whose deaths, civil and literal, warn us that no one can breathe in this atmosphere. See L. Guinier &amp; G. Torres, The Miner's Canary 274-283 (2002). They are the ones who recognize that unlawful police stops corrode all our civil liberties and threaten all our lives. Until their voices matter too, our justice system will continue to be anything but.</p>
<p id="p-83">* * *</p>
<p id="p-84">I dissent.</p>
<p id="p-85">Justice KAGAN, with whom Justice GINSBURG joins, dissenting.</p>
<p id="p-86">If a police officer stops a person on the street without reasonable suspicion, that seizure violates the Fourth Amendment. And if the officer pats down the unlawfully detained individual and finds drugs in his pocket, the State may not use the contraband as evidence in a criminal prosecution. That much is beyond dispute. The question here is whether the prohibition on admitting evidence dissolves if the officer discovers, after making the stop but before finding the drugs, that the person has an outstanding arrest warrant. Because that added wrinkle makes no difference under the Constitution, I respectfully dissent.</p>
<p id="p-87">This Court has established a simple framework for determining whether to exclude evidence obtained through a Fourth Amendment violation: Suppression is necessary when, but only when, its societal benefits outweigh its costs. See <em>ante,</em> at 2060 - 2061; <em>Davis v. United States,</em> <extracted-citation case-ids="5928256,12450488" index="193" url="https://cite.case.law/us/564/229/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">564 U.S. 229</a></span></extracted-citation>, 237, <extracted-citation case-ids="5928256,12450488" index="194" url="https://cite.case.law/us/564/229/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">131 S.Ct. 2419</a></span></extracted-citation>, <extracted-citation case-ids="12450488,5928256" index="195" url="https://cite.case.law/l-ed-2d/180/285/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">180 L.Ed.2d 285</a></span></extracted-citation> (2011). The exclusionary rule serves a crucial function-to deter unconstitutional police conduct. By barring the use of illegally obtained evidence, courts reduce the temptation for police officers to skirt the Fourth Amendment's requirements. See <em>James v. Illinois,</em> <extracted-citation case-ids="11331446" index="196" url="https://cite.case.law/us/493/307/#p319"><span class="citation" data-id="9431873"><a href="/opinion/112350/james-v-illinois/" aria-description="Citation for case: James v. Illinois">493 U.S. 307</a></span></extracted-citation>, 319, <extracted-citation case-ids="11331446" index="197" url="https://cite.case.law/us/493/307/#p319"><span class="citation" data-id="9431873"><a href="/opinion/112350/james-v-illinois/" aria-description="Citation for case: James v. Illinois">110 S.Ct. 648</a></span></extracted-citation>, <extracted-citation case-ids="11331446" index="198" url="https://cite.case.law/us/493/307/#p319"><span class="citation" data-id="9431873"><a href="/opinion/112350/james-v-illinois/" aria-description="Citation for case: James v. Illinois">107 L.Ed.2d 676</a></span></extracted-citation> (1990). But suppression of evidence also "exacts a heavy toll": Its consequence in many cases is to release a criminal without just punishment. <em>Davis,</em> <extracted-citation case-ids="5928256,12450488" index="199" url="https://cite.case.law/us/564/229/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">564 U.S., at 237</a></span></extracted-citation>, <extracted-citation case-ids="5928256,12450488" index="200" url="https://cite.case.law/us/564/229/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">131 S.Ct. 2419</a></span></extracted-citation>. Our decisions have thus endeavored to strike a sound balance between those two competing considerations-rejecting the "reflexive" impulse to exclude evidence every time an officer runs afoul of the Fourth Amendment, <em><extracted-citation case-ids="5928256,12450488" index="201" url="https://cite.case.law/us/564/229/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">id.,</a></span></extracted-citation></em><extracted-citation case-ids="5928256,12450488" index="201" url="https://cite.case.law/us/564/229/"> at 238</extracted-citation>, <extracted-citation case-ids="5928256,12450488" index="202" url="https://cite.case.law/us/564/229/"><span class="citation multiple-matches"><a href="/c/S.Ct./131/2419/">131 S.Ct. 2419</a></span></extracted-citation> but insisting on suppression when it will lead to "appreciable deterrence" of police misconduct, <em>Herring v. United States,</em> <extracted-citation case-ids="3679252" index="203" url="https://cite.case.law/us/555/135/#p141"><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/" aria-description="Citation for case: Herring v. United States">555 U.S. 135</a></span></extracted-citation>, 141, <extracted-citation case-ids="3679252" index="204" url="https://cite.case.law/us/555/135/#p141"><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/" aria-description="Citation for case: Herring v. United States">129 S.Ct. 695</a></span></extracted-citation>, <extracted-citation case-ids="3679252" index="205" url="https://cite.case.law/us/555/135/#p141"><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/" aria-description="Citation for case: Herring v. United States">172 L.Ed.2d 496</a></span></extracted-citation> (2009).</p>
<p id="p-88">This case thus requires the Court to determine whether excluding the fruits of Officer Douglas Fackrell's unjustified stop of Edward Strieff would significantly deter police from committing similar constitutional violations in the future. And as the Court states, that inquiry turns on application of the "attenuation doctrine," <em>ante,</em> at 2061 - 2062-our effort to "mark the point" at which the discovery of evidence "become[s] so attenuated" from the police misconduct that the deterrent benefit of exclusion drops below its cost. <em>United States v. Leon,</em> <extracted-citation case-ids="11340969" index="206" url="https://cite.case.law/us/468/897/#p920"><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U.S. 897</a></span></extracted-citation>, 911, <extracted-citation case-ids="11340969" index="207" url="https://cite.case.law/us/468/897/#p920"><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span></extracted-citation>, <extracted-citation case-ids="11340969" index="208" url="https://cite.case.law/us/468/897/#p920"><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">82 L.Ed.2d 677</a></span></extracted-citation> (1984). Since <em>Brown v. Illinois,</em> <extracted-citation case-ids="9639" index="209" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590</a></span></extracted-citation>, 604-605, <extracted-citation case-ids="9639" index="210" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>, <extracted-citation case-ids="9639" index="211" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">45 L.Ed.2d 416</a></span></extracted-citation> (1975), three factors have guided that analysis. First, the closer the "temporal proximity" between the unlawful act and the discovery of evidence, the greater the deterrent value of suppression. <em><extracted-citation case-ids="9639" index="212" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="9639" index="212" url="https://cite.case.law/us/422/590/"> at 603</extracted-citation>, <extracted-citation case-ids="9639" index="213" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>. Second, the more "purpose[ful]" or "flagran[t]" the police illegality, the clearer the necessity, and better the chance, of preventing similar misbehavior. <em><extracted-citation case-ids="9639" index="214" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="9639" index="214" url="https://cite.case.law/us/422/590/"> at 604</extracted-citation>, <extracted-citation case-ids="9639" index="215" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>.</p>
<p id="p-89"><a class="page-label" data-citation-index="1" data-label="2072" href="#p2072" id="p2072">*2072</a>And third, the presence (or absence) of "intervening circumstances" makes a difference: The stronger the causal chain between the misconduct and the evidence, the more exclusion will curb future constitutional violations. <em><extracted-citation case-ids="9639" index="216" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="9639" index="216" url="https://cite.case.law/us/422/590/"> at 603-604</extracted-citation>, <extracted-citation case-ids="9639" index="217" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>. Here, as shown below, each of those considerations points toward suppression: Nothing in Fackrell's discovery of an outstanding warrant so attenuated the connection between his wrongful behavior and his detection of drugs as to diminish the exclusionary rule's deterrent benefits.</p>
<p id="p-90">Start where the majority does: The temporal proximity factor, it forthrightly admits, "favors suppressing the evidence." <em>Ante,</em> at 2062. After all, Fackrell's discovery of drugs came just minutes after the unconstitutional stop. And in prior decisions, this Court has made clear that only the lapse of "substantial time" between the two could favor admission. <em>Kaupp v. Texas,</em> <extracted-citation case-ids="9031233" index="218" url="https://cite.case.law/us/538/626/#p633"><span class="citation" data-id="127919"><a href="/opinion/127919/kaupp-v-texas/" aria-description="Citation for case: Kaupp v. Texas">538 U.S. 626</a></span></extracted-citation>, 633, <extracted-citation case-ids="9031233" index="219" url="https://cite.case.law/us/538/626/#p633"><span class="citation" data-id="127919"><a href="/opinion/127919/kaupp-v-texas/" aria-description="Citation for case: Kaupp v. Texas">123 S.Ct. 1843</a></span></extracted-citation>, <extracted-citation case-ids="9031233" index="220" url="https://cite.case.law/us/538/626/#p633"><span class="citation" data-id="127919"><a href="/opinion/127919/kaupp-v-texas/" aria-description="Citation for case: Kaupp v. Texas">155 L.Ed.2d 814</a></span></extracted-citation> (2003) (<em>per curiam</em> ); see, <em>e.g.,</em> <em>Brown,</em> <extracted-citation case-ids="9639" index="221" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U.S., at 604</a></span></extracted-citation>, <extracted-citation case-ids="9639" index="222" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation> (suppressing a confession when "less than two hours" separated it from an unlawful arrest). So the State, by all accounts, takes strike one.</p>
<p id="p-91">Move on to the purposefulness of Fackrell's conduct, where the majority is less willing to see a problem for what it is. The majority chalks up Fackrell's Fourth Amendment violation to a couple of innocent "mistakes." <em>Ante,</em> at 2063. But far from a Barney Fife-type mishap, Fackrell's seizure of Strieff was a calculated decision, taken with so little justification that the State has never tried to defend its legality. At the suppression hearing, Fackrell acknowledged that the stop was designed for investigatory purposes-<em>i.e.,</em> to "find out what was going on [in] the house" he had been watching, and to figure out "what [Strieff] was doing there." App. 17-18. And Fackrell frankly admitted that he had no basis for his action except that Strieff "was coming out of the house." <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Id.,</a></span></em> at 17<em>.</em> Plug in Fackrell's and Strieff's names, substitute "stop" for "arrest" and "reasonable suspicion" for "probable cause," and this Court's decision in <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></em> perfectly describes this case:</p>
<blockquote id="p-92">"[I]t is not disputed that [Fackrell stopped Strieff] without [reasonable suspicion]. [He] later testified that [he] made the [stop] for the purpose of questioning [Strieff] as part of [his] investigation.... The illegality here ... had a quality of purposefulness. The impropriety of the [stop] was obvious. [A]wareness of that fact was virtually conceded by [Fackrell] when [he] repeatedly acknowledged, in [his] testimony, that the purpose of [his] action was 'for investigation': [Fackrell] embarked upon this expedition for evidence in the hope that something might turn up." 422 U.S., at 592, 605, <extracted-citation case-ids="9639" index="223" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation> (some internal punctuation altered; footnote, citation, and paragraph break omitted).</blockquote>
<p id="p-93">In <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>,</em> the Court held those facts to support suppression-and they do here as well. Swing and a miss for strike two.</p>
<p id="p-94">Finally, consider whether any intervening circumstance "br[oke] the causal chain" between the stop and the evidence. <em>Ante,</em> at 2062. The notion of such a disrupting event comes from the tort law doctrine of proximate causation. See <em>Bridge v. Phoenix Bond &amp; Indemnity Co.,</em> <extracted-citation case-ids="3674023" index="224" url="https://cite.case.law/us/553/639/#p658"><span class="citation" data-id="145799"><a href="/opinion/145799/bridge-v-phoenix-bond-indemnity-co/" aria-description="Citation for case: Bridge v. Phoenix Bond &amp; Indemnity Co.">553 U.S. 639</a></span></extracted-citation>, 658-659, <extracted-citation case-ids="3674023" index="225" url="https://cite.case.law/us/553/639/#p658"><span class="citation" data-id="145799"><a href="/opinion/145799/bridge-v-phoenix-bond-indemnity-co/" aria-description="Citation for case: Bridge v. Phoenix Bond &amp; Indemnity Co.">128 S.Ct. 2131</a></span></extracted-citation>, <extracted-citation case-ids="3674023" index="226" url="https://cite.case.law/us/553/639/#p658"><span class="citation" data-id="145799"><a href="/opinion/145799/bridge-v-phoenix-bond-indemnity-co/" aria-description="Citation for case: Bridge v. Phoenix Bond &amp; Indemnity Co.">170 L.Ed.2d 1012</a></span></extracted-citation> (2008) (explaining that a party cannot "establish [ ] proximate cause" when "an intervening cause break[s] the chain of causation between" the act and the injury); Kerr, Good Faith, New Law, and the Scope of the Exclusionary Rule, <extracted-citation index="227" url="https://cite.case.law/citations/?q=99%20Geo.%20L.J.%201077">99 Geo. L. J. 1077</extracted-citation>, 1099 (2011) (Fourth Amendment attenuation analysis "looks to <a class="page-label" data-citation-index="1" data-label="2073" href="#p2073" id="p2073">*2073</a>whether the constitutional violation was the proximate cause of the discovery of the evidence"). And as in the tort context, a circumstance counts as intervening only when it is unforeseeable-not when it can be seen coming from miles away. See W. Keeton, D. Dobbs, B. Keeton, &amp; D. Owen, Prosser and Keeton on Law of Torts 312 (5th ed. 1984). For rather than breaking the causal chain, predictable effects (<em>e.g.,</em> X leads naturally to Y leads naturally to Z) are its very links.</p>
<p id="p-95">And Fackrell's discovery of an arrest warrant-the only event the majority thinks intervened-was an eminently foreseeable consequence of stopping Strieff. As Fackrell testified, checking for outstanding warrants during a stop is the "normal" practice of South Salt Lake City police. App. 18; see also <em>State v. Topanotes,</em> <extracted-citation case-ids="9096354" index="228" url="https://cite.case.law/p3d/76/1159/"><span class="citation" data-id="2598446"><a href="/opinion/2598446/state-v-topanotes/" aria-description="Citation for case: State v. Topanotes">2003 UT 30</a></span></extracted-citation>, ¶ 2, <extracted-citation case-ids="9096354" index="229" url="https://cite.case.law/p3d/76/1159/"><span class="citation" data-id="2598446"><a href="/opinion/2598446/state-v-topanotes/" aria-description="Citation for case: State v. Topanotes">76 

[...TRUNCATED 5369 of 125369 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/Vale v. Louisiana.md  (`case`, 6 assertions)

### content_page

```
---
title: "Vale v. Louisiana"
type: case
citation: "399 U.S. 30 (1970)"
parallel_cite: "90 S. Ct. 1969; 26 L. Ed. 2d 409"
neutral_cite: 1970 U.S. LEXIS 18
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1970
date_decided: 1970-06-22
docket: 727
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1970-06-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Vale v. Louisiana
  varies_by_point: false
  scope_note: "Applies Chimel's spatial limit to dwellings; still the controlling rule that a search incident to arrest cannot reach a house when the arrest occurs outside it."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108183/vale-v-louisiana/"
  cluster_id: 108183
  opinion_id: 108183
  identity_checked: true
homes:
  - page: "[[SIA Persons]]"
    role: "Limiting"
  - page: "[[Arrest in the Home]]"
    role: "Related (cross-doctrine)"
related: ["[[Chimel v. California]]", "[[Shipley v. California]]", "[[Agnello v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "warrant-requirement", "exigent-circumstances"]
holding: "A search of a house cannot be justified as incident to an arrest made outside the house; a warrantless dwelling search requires a recognized exception, and a street arrest is not its own exigent circumstance."
lake:
  record_id: Vale v. Louisiana
  status: verified
  projected_at: 2026-07-09
---

# Vale v. Louisiana

*399 U.S. 30 (1970)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers holding two arrest warrants for Vale, and information that he lived at a specified address, set up surveillance of the house. They watched what they took to be a narcotics sale to the driver of a car at the curb, then approached. They arrested Vale on the front steps of the house, entered, made a cursory check that no one else was inside, and searched a rear bedroom, where they found narcotics.

## Issue
May a warrantless search of a house be justified as incident to an arrest made outside the house (on the front steps), or by the ready destructibility of narcotics, absent any exigent circumstance?

## Rule
No. A search "may be incident to an arrest ' "only if it is substantially contemporaneous with the arrest and is confined to the *immediate* vicinity of the arrest." ' " — 399 U.S. at 33 (quoting *Shipley v. California*). ^pin-33

"If a search of a house is to be upheld as incident to an arrest, that arrest must take place inside the house . . . not somewhere outside — whether two blocks away . . . twenty feet away . . . or on the sidewalk near the front steps." — *Id.* at 34. ^pin-34

Beyond the search-incident rationale, only "a few specifically established and well-delineated" situations let a warrantless dwelling search survive even on probable cause, and "[t]he burden rests on the State to show the existence of such an exceptional situation." — [*Id.*](https://www.courtlistener.com/opinion/108183/vale-v-louisiana/#:~:text=a%20few%20specifically%20established%20and) ^pin-34b

The Court "decline[d] to hold that an arrest on the street can provide its own 'exigent circumstance' so as to justify a warrantless search of the arrestee's house." — *Id.* at 35. ^pin-35

## Application
Vale was arrested on the front steps, not inside the dwelling, so the search of the rear bedroom was neither within the immediate vicinity of the arrest nor incident to it. Nor did any exception excuse the warrant: by the officers' own account they had satisfied themselves no one else was in the house when they entered, so there was no one to destroy evidence; no one consented; the officers were not responding to an emergency or in [[Exigent Circumstances and Hot Pursuit|hot pursuit]]; the seized goods were not in the process of destruction and were not about to be removed; and the officers who had obtained two arrest warrants had no apparent reason they could not also obtain a search warrant. The street arrest supplied no [[Exigent Circumstances and Hot Pursuit|exigency]] of its own.

## Conclusion
The warrantless search of the house was unconstitutional, and admitting its fruits was constitutional error. The judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Vale* remains the controlling statement that a search incident to a recent arrest cannot reach a dwelling when the arrest occurred outside it, and that the State bears the burden of justifying any warrantless home search. It applies the spatial limit of [[Chimel v. California]] and is regularly cited alongside [[Shipley v. California]] and [[Agnello v. United States]]. No negative treatment.

## Appears on
- [[SIA Persons]] — *Limiting*
- [[Arrest in the Home]] — *Related (cross-doctrine)*

## Sources
- *Vale v. Louisiana*, 399 U.S. 30 (1970) — https://www.courtlistener.com/opinion/108183/vale-v-louisiana/ — pinpoints: 33, 34, 35.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "fe2fca7e739e387f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "399 U.S. 30 (1970)", "court": "U.S. Supreme Court", "neutral_cite": "1970 U.S. LEXIS 18", "official_citation_present": true, "parallel_cite": "90 S. Ct. 1969; 26 L. Ed. 2d 409", "title": "Vale v. Louisiana", "year": "1970"}}
{"assertion_id": "09ec8fa9ed983452", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Persons"}, "payload": {"home": "SIA Persons", "role": "Limiting", "title": "Vale v. Louisiana"}}
{"assertion_id": "6fd92ed665bc28f5", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Related (cross-doctrine)", "title": "Vale v. Louisiana"}}
{"assertion_id": "c50735b5a4f02e19", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A search of a house cannot be justified as incident to an arrest made outside the house; a warrantless dwelling search requires a recognized exception, and a street arrest is not its own exigent circumstance.", "title": "Vale v. Louisiana"}}
{"assertion_id": "2deab033e7041b4c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Vale v. Louisiana"}}
{"assertion_id": "f0ff08f25b37d9b7", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1970-06-22", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Vale v. Louisiana", "field_i_validity": "good_law", "scope_note": "Applies Chimel's spatial limit to dwellings; still the controlling rule that a search incident to arrest cannot reach a house when the arrest occurs outside it.", "title": "Vale v. Louisiana", "varies_by_point": "false"}}
```

### lake record — Vale v. Louisiana

```json
{
  "schema_version": "s2.v1",
  "record_id": "Vale v. Louisiana",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Vale v. Louisiana",
    "case_name_short": "Vale",
    "case_name_full": "Vale v. Louisiana",
    "input_case_name": "Vale v. Louisiana",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1970-06-22",
    "year": 1970,
    "docket": "727",
    "cluster_id": 108183,
    "lead_opinion_id": 108183,
    "sibling_ids": [
      108183,
      9424318,
      9424319
    ],
    "absolute_url": "/opinion/108183/vale-v-louisiana/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "399 U.S. 30",
      "volume": "399",
      "reporter": "U.S.",
      "page": "30",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "90 S. Ct. 1969",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "1969",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 L. Ed. 2d 409",
        "volume": "26",
        "reporter": "L. Ed. 2d",
        "page": "409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1970 U.S. LEXIS 18",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "18",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "399 U.S. 30",
        "volume": "399",
        "reporter": "U.S.",
        "page": "30",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 S. Ct. 1969",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "1969",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 L. Ed. 2d 409",
        "volume": "26",
        "reporter": "L. Ed. 2d",
        "page": "409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1970 U.S. LEXIS 18",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "18",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "399 U.S. 30",
    "official_selection": {
      "court_class": "scotus",
      "selected": "399 U.S. 30",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-33",
      "page": null,
      "quote": "--- # Vale v. Louisiana *399 U.S. 30 (1970)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers holding two arrest warrants for Vale, and information that he lived at a specified address, set up surveillance of the house. They watched what they took to be a narcotics sale to the driver of a car at the curb, then approached. They arrested Vale on the front steps of the house, entered, made a cursory check that no one else was inside, and searched a rear bedroom, where they found narcotics. ## Issue May a warrantless search of a house be justified as incident to an arrest made outside the house (on the front steps), or by the ready destructibility of narcotics, absent any exigent circumstance? ## Rule No. A search",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-34",
      "page": null,
      "quote": "If a search of a house is to be upheld as incident to an arrest, that arrest must take place inside the house . . . not somewhere outside \u2014 whether two blocks away . . . twenty feet away . . . or on the sidewalk near the front steps.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-34b",
      "page": null,
      "quote": "a few specifically established and well-delineated",
      "star_marker": "34",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 9600,
      "fragment": "#:~:text=a%20few%20specifically%20established%20and",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-35",
      "page": null,
      "quote": "decline[d] to hold that an arrest on the street can provide its own 'exigent circumstance' so as to justify a warrantless search of the arrestee's house.",
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
    "composite_basis_ref": "Vale v. Louisiana",
    "varies_by_point": false,
    "scope_note": "Applies Chimel's spatial limit to dwellings; still the controlling rule that a search incident to arrest cannot reach a house when the arrest occurs outside it.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "The People v. Shawn J. Sivertson",
          "cluster_id": 4396228,
          "cite": [
            "29 N.Y.3d 1006",
            "77 N.E.3d 349"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Frankie Dean Pair, Jr. v. State",
          "cluster_id": 2850893,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vela v. State",
          "cluster_id": 5248598,
          "cite": [
            "775 S.W.2d 11",
            "1989 Tex. App. LEXIS 1522",
            "1989 WL 61440"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Baird",
          "cluster_id": 1281144,
          "cite": [
            "763 P.2d 1214",
            "94 Utah Adv. Rep. 40",
            "1988 Utah App. LEXIS 163",
            "1988 WL 116729"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Livingston v. State",
          "cluster_id": 5243642,
          "cite": [
            "731 S.W.2d 744",
            "1987 Tex. App. LEXIS 7761"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane1_negative"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mincey v. Arizona",
          "cluster_id": 109905,
          "cite": [
            "57 L. Ed. 2d 290",
            "98 S. Ct. 2408",
            "437 U.S. 385",
            "1978 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ledesma",
          "cluster_id": 1228080,
          "cite": [
            "729 P.2d 839",
            "43 Cal. 3d 171",
            "233 Cal. Rptr. 404",
            "1987 Cal. LEXIS 278"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McGee v. State",
          "cluster_id": 1960022,
          "cite": [
            "105 S.W.3d 609",
            "2003 Tex. Crim. App. LEXIS 75",
            "2003 WL 1918091"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wyman v. James",
          "cluster_id": 108223,
          "cite": [
            "27 L. Ed. 2d 408",
            "91 S. Ct. 381",
            "400 U.S. 309",
            "1971 U.S. LEXIS 106"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ramey",
          "cluster_id": 1185860,
          "cite": [
            "545 P.2d 1333",
            "16 Cal. 3d 263",
            "127 Cal. Rptr. 629",
            "1976 Cal. LEXIS 220"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Webster Bivens v. Six Unknown Named Agents of the Federal Bureau of Narcotics",
          "cluster_id": 302266,
          "cite": [
            "456 F.2d 1339",
            "1972 U.S. App. LEXIS 10860"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Francisco Sangineto-Miranda, (87-5667) Luray Betts, (87-5668) Enrique Vargas, (87-5711) & Benjamin Nelson, (87-5712)",
          "cluster_id": 513263,
          "cite": [
            "859 F.2d 1501"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Huddleston",
          "cluster_id": 2435833,
          "cite": [
            "924 S.W.2d 666",
            "1996 Tenn. LEXIS 387",
            "1996 WL 328642"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Juan Castillo, Aka: Luis Hong Rojas, United States of America v. Antonio De La Renta",
          "cluster_id": 517687,
          "cite": [
            "866 F.2d 1071"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Joe Whitten, John Elmer Gaiefsky, Jack Wayne Gish, Richard Lawrence Shimel",
          "cluster_id": 418069,
          "cite": [
            "706 F.2d 1000",
            "13 Fed. R. Serv. 384",
            "1983 U.S. App. LEXIS 27369"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 1162553,
          "cite": [
            "756 P.2d 221",
            "45 Cal. 3d 1268",
            "248 Cal. Rptr. 834",
            "1988 Cal. LEXIS 155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Paul Gary Rubin United States of America v. Louis Martin Agnes A/K/A Louis Martin",
          "cluster_id": 308715,
          "cite": [
            "474 F.2d 262"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Servis v. Commonwealth",
          "cluster_id": 1349258,
          "cite": [
            "371 S.E.2d 156",
            "6 Va. App. 507",
            "5 Va. Law Rep. 37",
            "1988 Va. App. LEXIS 66"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ernest Raymond Basurto",
          "cluster_id": 319510,
          "cite": [
            "497 F.2d 781"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108183 OR 9424318 OR 9424319) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MzY1NDQwMDAwMDAmcz0xMjI4MDgwJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108183+OR+9424318+OR+9424319%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(108183 OR 9424318 OR 9424319)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzYmcz0xMDU3NzI3JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108183+OR+9424318+OR+9424319%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108183 OR 9424318 OR 9424319)",
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
    "complete_query": "cites:(108183 OR 9424318 OR 9424319)",
    "indexed_citing_opinions": 631,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108183,
        "count": 565,
        "count_source": "search"
      },
      {
        "opinion_id": 9424318,
        "count": 90,
        "count_source": "search"
      },
      {
        "opinion_id": 9424319,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1044,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/vale-v-louisiana.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQ2ODE1NzMmcz00MjY1NTA3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108183+OR+9424318+OR+9424319%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108183,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 104314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 107102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 107982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 1714335,
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
    "date_created": "2026-07-06T03:43:44Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:43:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:43:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:47:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:43:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Vale v. Louisiana

```
<div>
<center><b><span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/" aria-description="Citation for case: Vale v. Louisiana">399 U.S. 30</a></span> (1970)</b></center>
<center><h1>VALE<br>
v.<br>
LOUISIANA.</h1></center>
<center>No. 727.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 4-5, 1970.</center>
<center>Decided June 22, 1970.</center>
APPEAL FROM THE SUPREME COURT OF LOUISIANA.
<p><i>Eberhard P. Deutsch,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./396/883/">396 U. S. 883</a></span>, argued the cause for appellant. With him on the brief was <i>Rene H. Himel, Jr.</i></p>
<p><span class="star-pagination">*31</span> <i>Louise Korns</i> argued the cause for appellee. With her on the brief were <i>Jack P. F. Gremillion,</i> Attorney General of Louisiana, and <i>Jim Garrison.</i></p>
<p>MR. JUSTICE STEWART delivered the opinion of the Court.</p>
<p>The appellant, Donald Vale, was convicted in a Louisiana court on a charge of possessing heroin and was sentenced as a multiple offender to 15 years' imprisonment at hard labor. The Louisiana Supreme Court affirmed the conviction, rejecting the claim that evidence introduced at the trial was the product of an unlawful search and seizure. <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/" aria-description="Citation for case: State v. Vale">252 La. 1056</a></span>, <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/" aria-description="Citation for case: State v. Vale">215 So. 2d 811</a></span>. We granted Vale's motion to proceed <i>in forma pauperis,</i> postponed consideration of the question of jurisdiction to the hearing of the case on the merits, and limited review to the search-and-seizure question. <span class="citation multiple-matches"><a href="/c/U.%20S./396/813/">396 U. S. 813</a></span>.<sup>[*]</sup></p>
<p>The evidence adduced at the pretrial hearing on a motion to suppress showed that on April 24, 1967, officers possessing two warrants for Vale's arrest and having information that he was residing at a specified address proceeded there in an unmarked car and set up a surveillance of the house. The evidence of what then took <span class="star-pagination">*32</span> place was summarized by the Louisiana Supreme Court as follows:</p>
<blockquote>"After approximately 15 minutes the officers observed a green 1958 Chevrolet drive up and sound the horn and after backing into a parking place, again blew the horn. At this juncture Donald Vale, who was well known to Officer Brady having arrested him twice in the previous month, was seen coming out of the house and walk up to the passenger side of the Chevrolet where he had a close brief conversation with the driver; and after looking up and down the street returned inside of the house. Within a few minutes he reappeared on the porch, and again cautiously looked up and down the street before proceeding to the passenger side of the Chevrolet, leaning through the window. From this the officers were convinced a narcotics sale had taken place. They returned to their car and immediately drove toward Donald Vale, and as they reached within approximately three cars lengths from the accused, (Donald Vale) he looked up and, obviously recognizing the officers, turned around, walking quickly toward the house. At the same time the driver of the Chevrolet started to make his get away when the car was blocked by the police vehicle. The three officers promptly alighted from the car, whereupon Officers Soule and Laumann called to Donald Vale to stop as he reached the front steps of the house, telling him he was under arrest. Officer Brady at the same time, seeing the driver of the Chevrolet, Arizzio Saucier, whom the officers knew to be a narcotic addict, place something hurriedly in his mouth, immediately placed him under arrest and joined his co-officers. Because of the transaction <span class="star-pagination">*33</span> they had just observed they, informed Donald Vale they were going to search the house, and thereupon advised him of his constitutional rights. After they all entered the front room, Officer Laumann made a cursory inspection of the house to ascertain if anyone else was present and within about three minutes Mrs. Vale and James Vale, mother and brother of Donald Vale, returned home carrying groceries and were informed of the arrest and impending search." <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/#1067" aria-description="Citation for case: State v. Vale">252 La., at 1067-1068</a></span>, <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/#815" aria-description="Citation for case: State v. Vale">215 So. 2d, at 815</a></span>. (Footnote omitted.)</blockquote>
<p>The search of a rear bedroom revealed a quantity of narcotics.</p>
<p>The Louisiana Supreme Court held that the search of the house did not violate the Fourth Amendment because it occurred "in the immediate vicinity of the arrest" of Donald Vale and was "substantially contemporaneous therewith . . . ." <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/#1070" aria-description="Citation for case: State v. Vale">252 La., at 1070</a></span>, <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/#816" aria-description="Citation for case: State v. Vale">215 So. 2d, at 816</a></span>. We cannot agree. Last Term in <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>, we held that when the search of a dwelling is sought to be justified as incident to a lawful arrest, it must constitutionally be confined to the area within the arrestee's reach at the time of his arrest"the area from within which he might gain possession of a weapon or destructible evidence." <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S., at 763</a></span>. But even if <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> is not accorded retroactive effecta question on which we do not now express an opinionno precedent of this Court can sustain the constitutional validity of the search in the case before us.</p>
<p>A search may be incident to an arrest " `only if it is substantially contemporaneous with the arrest and is confined to the <i>immediate</i> vicinity of the arrest.' " <i>Shipley</i> v. <i>California,</i> <span class="citation" data-id="9424104"><a href="/opinion/107982/shipley-v-california/#819" aria-description="Citation for case: Shipley v. California">395 U. S. 818, 819</a></span>; <i>Stoner</i> v. <i>California,</i> <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#486" aria-description="Citation for case: Stoner v. California">376 U. S. 483, 486</a></span>. If a search of a house is to be upheld <span class="star-pagination">*34</span> as incident to an arrest, that arrest must take place <i>inside</i> the house, cf. <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#32" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 32</a></span>, not somewhere outsidewhether two blocks away, <i>James</i> v. <i>Louisiana,</i> <span class="citation" data-id="107102"><a href="/opinion/107102/james-v-louisiana/" aria-description="Citation for case: James v. Louisiana">382 U. S. 36</a></span>, twenty feet away, <i>Shipley</i> v. <i>California, supra</i><i>,</i> or on the sidewalk near the front steps. "Belief, however well founded, that an article sought is concealed in a dwelling house furnishes no justification for a search of that place without a warrant." <i>Agnello</i> v. <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States"><i>United States, supra,</i> at 33</a></span>. That basic rule "has never been questioned in this Court." <i>Stoner</i> v. <i>California, supra,</i> at 487 n. 5.</p>
<p>The Louisiana Supreme Court thought the search independently supportable because it involved narcotics, which are easily removed, hidden, or destroyed. It would be unreasonable, the Louisiana court concluded, "to require the officers under the facts of the case to first secure a search warrant before searching the premises, as time is of the essence inasmuch as the officers never know whether there is anyone on the premises to be searched who could very easily destroy the evidence." <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/#1070" aria-description="Citation for case: State v. Vale">252 La., at 1070</a></span>, <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/#816" aria-description="Citation for case: State v. Vale">215 So. 2d, at 816</a></span>. Such a rationale could not apply to the present case, since by their own account the arresting officers satisfied themselves that no one else was in the house when they first entered the premises. But entirely apart from that point, our past decisions make clear that only in "a few specifically established and well-delineated" situations, <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span>, may a warrantless search of a dwelling withstand constitutional scrutiny, even though the authorities have probable cause to conduct it. The burden rests on the State to show the existence of such an exceptional situation. <i>Chimel</i> v. <i>California, supra,</i> at 762; <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span>; <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#456" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 456</a></span>. And the record before us discloses none.</p>
<p><span class="star-pagination">*35</span> There is no suggestion that anyone consented to the search. Cf. <i>Zap</i> v. <i>United States,</i> <span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/#628" aria-description="Citation for case: Zap v. United States">328 U. S. 624, 628</a></span>. The officers were not responding to an emergency. <i>United States</i> v. <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#52" aria-description="Citation for case: United States v. Jeffers"><i>Jeffers, supra,</i> at 52</a></span>; <i>McDonald</i> v. <i>United States, supra,</i> at 454. They were not in hot pursuit of a fleeing felon. <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 298-299</a></span>; <i>Chapman</i> v. <i>United States,</i> <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/#615" aria-description="Citation for case: Chapman v. United States">365 U. S. 610, 615</a></span>; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#15" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 15</a></span>. The goods ultimately seized were not in the process of destruction. <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 770-771</a></span>; <i>United States</i> v. <i><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Jeffers, supra</a></span></i><i>; </i><i>McDonald</i> v. <i>United States, supra,</i> at 455. Nor were they about to be removed from the jurisdiction. <i>Chapman</i> v. <i>United States, supra</i><i>; </i><i>Johnson</i> v. <i>United States, supra</i><i>; </i><i>United States</i> v. <i><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Jeffers, supra</a></span></i><i>.</i></p>
<p>The officers were able to procure two warrants for Vale's arrest. They also had information that he was residing at the address where they found him. There is thus no reason, so far as anything before us appears, to suppose that it was impracticable for them to obtain a search warrant as well. Cf. <i>McDonald</i> v. <i>United States, supra,</i> at 454-455; <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/#705" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699, 705-706</a></span>; <i>Johnson</i> v. <i>United States, supra</i><i>; </i><i>Taylor</i> v. <i>United States,</i> <span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/#6" aria-description="Citation for case: Taylor v. United States">286 U. S. 1, 6</a></span>; <i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#358" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 358</a></span>; <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 156</a></span>; cf. <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#42" aria-description="Citation for case: Ker v. California">374 U. S. 23, 42</a></span> (opinion of Clark, J.). We decline to hold that an arrest on the street can provide its own "exigent circumstance" so as to justify a warrantless search of the arrestee's house.</p>
<p>The Louisiana courts committed constitutional error in admitting into evidence the fruits of the illegal search. <i>Shipley</i> v. <i>California, supra,</i> at 819; <i>James</i> v. <i>Louisiana, supra,</i> at 37; <i>Ker</i> v. <i>California, supra,</i> at 30-34; <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>. Accordingly, the judgment is <span class="star-pagination">*36</span> reversed and the case is remanded to the Louisiana Supreme Court for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE BLACKMUN took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE BLACK, with whom THE CHIEF JUSTICE joins, dissenting.</p>
<p>The Fourth Amendment to the United States Constitution prohibits only "unreasonable searches."<sup>[*]</sup> A warrant has never been thought to be an absolute requirement for a constitutionally proper search. Searches, whether with or without a warrant, are to be judged by whether they are reasonable, and, as I said, speaking for the Court in <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#366" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 366-367</a></span> (1964), common sense dictates that reasonableness varies with the circumstances of the search. See, <i>e. g., </i><i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span> (1959); <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949). The Louisiana Supreme Court held not only that the police action here was reasonable but also that failure to conduct an immediate search would have been unreasonable. <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/#1070" aria-description="Citation for case: State v. Vale">252 La. 1056, 1070</a></span>, <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/#816" aria-description="Citation for case: State v. Vale">215 So. 2d 811, 816</a></span>. With that view I am in complete agreement, for the following reasons.</p>
<p>The police, having warrants for Vale's arrest, were watching his mother's house from a short distance away. Not long after they began their vigil a car arrived, <span class="star-pagination">*37</span> sounded its horn, and backed into a parking space near the house. The driver did not get out, but instead honked the car horn again. Vale, who had been arrested twice the month before and against whom an indictment for a narcotics offense was then pending, came out of his mother's house and talked to the driver of the car. At the conclusion of the conversation Vale looked both ways, up and down the street, and then went back inside the house. When he reappeared he stopped before going to the car and stood, as one of the officers testified, "[l]ooking back and forth like to see who might be coming or who was in the neighborhood." He then walked to the car and leaned in.</p>
<p>From this behavior the officers were convinced that a narcotics transaction was taking place at that very moment. They drove down the street toward Vale and the parked car. When they came within a few car lengths of the two men Vale saw them and began to walk quickly back toward the house. At the same time the driver of the car attempted to pull away. The police brought both parties to the transaction to a stop. They then saw that the driver of the car was one Saucier, a known narcotics addict. He hurriedly placed something in his mouth, and apparently swallowed it. The police placed both Vale and Saucier under arrest.</p>
<p>At this point the police had probable cause to believe that Vale was engaged in a narcotics transfer, and that a supply of narcotics would be found in the house, to which Vale had returned after his first conversation, from which he had emerged furtively bearing what the police could readily deduce was a supply of narcotics, and toward which he hurried after seeing the police. But the police did not know then who else might be in the house. Vale's arrest took place near the house, and anyone observing from inside would surely have been alerted to destroy the stocks of contraband which <span class="star-pagination">*38</span> the police believed Vale had left there. The police had already seen Saucier, the narcotics addict, apparently swallow what Vale had given him. Believing that some evidence had already been destroyed and that other evidence might well be, the police were faced with the choice of risking the immediate destruction of evidence or entering the house and conducting a search. I cannot say that their decision to search was unreasonable. Delay in order to obtain a warrant would have given an accomplice just the time he needed.</p>
<p>That the arresting officers did, in fact, believe that others might be in the house is attested to by their actions upon entering the door left open by Vale. The police at once checked the small house to determine if anyone else was present. Just as they discovered the house was empty, however, Vale's mother and brother arrived. Now what had been a suspicion became a certainty: Vale's relatives were in possession and knew of his arrest. To have abandoned the search at this point, and left the house with Vale, would not have been the action of reasonable police officers. As MR. JUSTICE WHITE said, dissenting in <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#775" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 775</a></span> (1969):</p>
<blockquote>"For the police to search the house while the evidence they had probable cause to search out and seize was still there cannot be considered unreasonable."</blockquote>
<p>In my view, whether a search incident to a lawful arrest is reasonable should still be determined by the facts and circumstances of each case. <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#34" aria-description="Citation for case: Ker v. California">374 U. S. 23, 34-36</a></span> (1963); <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#63" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 63-64</a></span> (1950). For the reasons given above I am convinced that the search here was reasonable, even though Vale had not yet crossed the threshold of the house toward which he was headed.</p>
<p><span class="star-pagination">*39</span> Moreover, the circumstances here were sufficiently exceptional to justify a search, even if the search was not strictly "incidental" to an arrest. The Court recognizes that searches to prevent the destruction or removal of evidence have long been held reasonable by this Court. <i>Preston</i> v. <i>United States, supra</i><i>; </i><i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 455</a></span> (1948); <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925). Whether the "exceptional circumstances" justifying such a search exist or not is a question that may be, as it is here, quite distinct from whether or not the search was incident to a valid arrest. See <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span> (1951); <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (1948). It is thus unnecessary to determine whether the search was valid as incident to the arrest under either <i>Chimel</i> v. <i>California, supra</i><i>,</i> or under the pre-<span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California"><i>Chimel</i></a></span> standard as interpreted in <i>Shipley</i> v. <i>California,</i> <span class="citation" data-id="9424104"><a href="/opinion/107982/shipley-v-california/" aria-description="Citation for case: Shipley v. California">395 U. S. 818</a></span> (1969). It is only necessary to find that, given Vale's arrest in a spot readily visible to anyone in the house and the probable existence of narcotics inside, it was reasonable for the police to conduct an immediate search of the premises.</p>
<p>The Court, however, finds the search here unreasonable. First, the Court suggests that the contraband was not "in the process of destruction." None of the cases cited by the Court supports the proposition that "exceptional circumstances" exist only when the process of destruction has already begun. On the contrary we implied that those circumstances did exist when "evidence or contraband was <i>threatened</i> with removal or destruction." <i>Johnson</i> v. <i>United States, supra,</i> at 15 (emphasis added). See also <i>Chapman</i> v. <i>United States,</i> <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/#615" aria-description="Citation for case: Chapman v. United States">365 U. S. 610, 615</a></span> (1961); <i>Hernandez</i> v. <i>United States,</i> <span class="citation" data-id="8874330"><a href="/opinion/8888212/hernandez-v-united-states/" aria-description="Citation for case: Hernandez v. United States">353 F. 2d 624</a></span> (C. A. 9th Cir. 1965), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./384/1008/">384 U. S. 1008</a></span> (1966).</p>
<p><span class="star-pagination">*40</span> Second, the Court seems to argue that the search was unreasonable because the police officers had time to obtain a warrant. I agree that the opportunity to obtain a warrant is one of the factors to be weighed in determining reasonableness. <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span> (1948); <i>United States</i> v. <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz"><i>Rabinowitz, supra,</i> at 66</a></span> (BLACK, J., dissenting). But the record conclusively shows that there was no such opportunity here. As I noted above, once the officers had observed Vale's conduct in front of the house they had probable cause to believe that a felony had been committed and that immediate action was necessary. At no time after the events in front of Mrs. Vale's house would it have been prudent for the officers to leave the house in order to secure a warrant.</p>
<p>The Court asserts, however, that because the police obtained two warrants for Vale's arrest there is "no reason . . . to suppose that it was impracticable for them to obtain a search warrant as well." The difficulty is that the two arrest warrants on which the Court seems to rely so heavily were not issued because of any present misconduct of Vale's; they were issued because the bond had been increased for an earlier narcotics charge then pending against Vale. When the police came to arrest Vale, they knew only that his bond had been increased. There is nothing in the record to indicate that, absent the increased bond, there would have been probable cause for an arrest, much less a search. Probable cause for the search arose for the first time when the police observed the activity of Vale and Saucier in and around the house.</p>
<p>I do not suggest that all arrests necessarily provide the basis for a search of the arrestee's house. In this case there is far more than a mere street arrest. The police also observed Vale's use of the house as a base of operations for his commercial business, his attempt to <span class="star-pagination">*41</span> return hurriedly to the house on seeing the officers, and the apparent destruction of evidence by the man with whom Vale was dealing. Furthermore the police arrival and Vale's arrest were plainly visible to anyone within the house, and the police had every reason to believe that someone in the house was likely to destroy the contraband if the search were postponed.</p>
<p>This case raises most graphically the question how does a policeman protect evidence necessary to the State if he must leave the premises to get a warrant, allowing the evidence he seeks to be destroyed. The Court's answer to that question makes unnecessarily difficult the conviction of those who prey upon society.</p>
<h2>NOTES</h2>
<p>[*]  In his Notice of Appeal, Vale asserted that the Louisiana Supreme Court in affirming the conviction had relied upon a state statute, Article 225 of the Louisiana Code of Criminal Procedure (1967), which provides in pertinent part:
</p>
<p>"A peace officer making an arrest shall take from the person arrested all weapons and incriminating articles which he may have about his person."</p>
<p>Although the state court referred to this statute in the course of its opinion, we do not understand its decision to be grounded on the statute. We therefore dismiss the appeal and treat the papers as a petition for certiorari, which is hereby granted. <span class="citation no-link">28 U. S. C. § 2103</span>.</p>
<p>[*]  The Fourth Amendment says:
</p>
<p>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</p>

</div>
```

---

## GROUP: content/cases/Walter v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Walter v. United States"
type: case
citation: "447 U.S. 649 (1980)"
parallel_cite: "100 S. Ct. 2395; 65 L. Ed. 2d 410"
neutral_cite: 1980 U.S. LEXIS 135
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-06-20
docket: 79-67
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1980-06-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Walter v. United States
  varies_by_point: false
  scope_note: "Plurality (Stevens, J., announcing the judgment); private-search principle later adopted and refined in United States v. Jacobsen (1984); good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110314/walter-v-united-states/"
  cluster_id: 110314
  opinion_id: 9428007
  identity_checked: true
homes:
  - page: "[[Private and Foreign Searches]]"
    role: "Key — scope limit"
related: ["[[United States v. Jacobsen]]"]
aliases: ["Walter v. US"]
tags: ["case", "fourth-amendment", "private-search", "scope", "search-definition"]
holding: "The government may not exceed the scope of a prior private search; the FBI's screening of films the private party had not viewed was a separate, unlawful search."
lake:
  record_id: Walter v. United States
  status: verified
  projected_at: 2026-07-09
---

# Walter v. United States

*447 U.S. 649 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Twelve sealed packages of 8-millimeter films were shipped by private carrier but misdelivered to L'Eggs Products, Inc. Employees opened the packages and found individual film boxes bearing suggestive drawings and explicit written descriptions of the contents; one employee opened a box and tried, without success, to view the film by holding it to the light. The employees turned the shipment over to the FBI, which — without a warrant — projected the films and used them to obtain obscenity convictions. The defendants moved to suppress.

## Issue
Whether the FBI's warrantless screening of films that a private party had received and inspected (but had not actually viewed) was a search requiring a warrant, or was instead authorized by the prior private search.

## Rule
The Government's later examination is measured against the scope of the prior private search: "the Government may not exceed the scope of the private search unless it has the right to make an independent search." — 447 U.S. at 657. ^pin-657

Projecting the films went beyond what the private party had done: "The projection of the films was a significant expansion of the search that had been conducted previously by a private party and therefore must be characterized as a separate search." — *Id.* And that separate, warrantless viewing was unreasonable: "the unauthorized exhibition of the films constituted an unreasonable invasion of their owner's constitutionally protected interest in privacy. It was a search; there was no warrant; the owner had not consented; and there were no exigent circumstances." — [*Id.* at 654](https://www.courtlistener.com/opinion/110314/walter-v-united-states/#:~:text=The%20projection%20of%20the%20films). ^pin-654

## Application
On these facts the private parties had opened the packages and examined the boxes — including the suggestive labels — but had not actually viewed the films. The FBI therefore could lawfully do what the private parties had already done, but projecting the films revealed contents the private search had not exposed and significantly expanded that search. Because the labels supplied probable cause and a warrant could easily have been obtained, the warrantless screening — unsupported by consent or [[Exigent Circumstances and Hot Pursuit|exigency]] — was an unreasonable search, and the films had to be suppressed.

## Conclusion
The warrantless projection of the films exceeded the scope of the private search and was an unreasonable search; the convictions were reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (judgment announced in a Stevens plurality).
- No negative treatment. The private-search principle — that government agents may not exceed the scope of an earlier private search without independent justification — was adopted and refined by [[United States v. Jacobsen]] (1984), which framed the inquiry as whether the official conduct exceeded the scope of the private search.

## Appears on
- [[Private and Foreign Searches]] — *Key — scope limit*

## Sources
- *Walter v. United States*, 447 U.S. 649 (1980) — https://www.courtlistener.com/opinion/110314/walter-v-united-states/ — pinpoints: 654, 657.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a21c5c19fd6d9579", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "447 U.S. 649 (1980)", "court": "U.S. Supreme Court", "neutral_cite": "1980 U.S. LEXIS 135", "official_citation_present": true, "parallel_cite": "100 S. Ct. 2395; 65 L. Ed. 2d 410", "title": "Walter v. United States", "year": "1980"}}
{"assertion_id": "46502c1ef38b1674", "dimension": "support", "kind": "home_role", "locator": {"home": "Private and Foreign Searches"}, "payload": {"home": "Private and Foreign Searches", "role": "Key — scope limit", "title": "Walter v. United States"}}
{"assertion_id": "e592993b6860acb3", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The government may not exceed the scope of a prior private search; the FBI's screening of films the private party had not viewed was a separate, unlawful search.", "title": "Walter v. United States"}}
{"assertion_id": "4b4a5d24d6b07db3", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1980-06-20", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Walter v. United States", "field_i_validity": "good_law", "scope_note": "Plurality (Stevens, J., announcing the judgment); private-search principle later adopted and refined in United States v. Jacobsen (1984); good law.", "title": "Walter v. United States", "varies_by_point": "false"}}
{"assertion_id": "5186337abb6b8a53", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Walter v. United States"}}
```

### lake record — Walter v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Walter v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Walter v. United States",
    "case_name_short": "Walter",
    "case_name_full": "Walter v. United States",
    "input_case_name": "Walter v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-06-20",
    "year": 1980,
    "docket": "79-67",
    "cluster_id": 110314,
    "lead_opinion_id": 9428007,
    "sibling_ids": [
      110314,
      9428007,
      9428008,
      9428009
    ],
    "absolute_url": "/opinion/110314/walter-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "447 U.S. 649",
      "volume": "447",
      "reporter": "U.S.",
      "page": "649",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 2395",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2395",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 410",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "410",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 135",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "135",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "447 U.S. 649",
        "volume": "447",
        "reporter": "U.S.",
        "page": "649",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 2395",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2395",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 410",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "410",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 135",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "135",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "447 U.S. 649",
    "official_selection": {
      "court_class": "scotus",
      "selected": "447 U.S. 649",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-657",
      "page": null,
      "quote": "--- # Walter v. United States *447 U.S. 649 (1980)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Twelve sealed packages of 8-millimeter films were shipped by private carrier but misdelivered to L'Eggs Products, Inc. Employees opened the packages and found individual film boxes bearing suggestive drawings and explicit written descriptions of the contents; one employee opened a box and tried, without success, to view the film by holding it to the light. The employees turned the shipment over to the FBI, which \u2014 without a warrant \u2014 projected the films and used them to obtain obscenity convictions. The defendants moved to suppress. ## Issue Whether the FBI's warrantless screening of films that a private party had received and inspected (but had not actually viewed) was a search requiring a warrant, or was instead authorized by the prior private search. ## Rule The Government's later examination is measured against the scope of the prior private search:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-654",
      "page": null,
      "quote": "The projection of the films was a significant expansion of the search that had been conducted previously by a private party and therefore must be characterized as a separate search.",
      "star_marker": "657",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 11610,
      "fragment": "#:~:text=The%20projection%20of%20the%20films",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1980-06-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Walter v. United States",
    "varies_by_point": false,
    "scope_note": "Plurality (Stevens, J., announcing the judgment); private-search principle later adopted and refined in United States v. Jacobsen (1984); good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Tyrone Davis",
          "cluster_id": 3212685,
          "cite": [
            "825 F.3d 1014",
            "2016 U.S. App. LEXIS 10661",
            "2016 WL 3245043"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bruce",
          "cluster_id": 2803531,
          "cite": [
            "412 S.C. 504",
            "772 S.E.2d 753",
            "2015 S.C. LEXIS 194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jenschke v. State",
          "cluster_id": 1795866,
          "cite": [
            "116 S.W.3d 173",
            "2003 WL 21696528"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. William Adderson Jarrett",
          "cluster_id": 782958,
          "cite": [
            "338 F.3d 339",
            "61 Fed. R. Serv. 1530",
            "2003 U.S. App. LEXIS 15017",
            "2003 WL 21744122"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dawson v. State",
          "cluster_id": 1635091,
          "cite": [
            "106 S.W.3d 388",
            "2003 WL 21027168"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane1_negative"
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
        "journal_ref": "Walter v. United States:lane2_top_cited"
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
        "journal_ref": "Walter v. United States:lane2_top_cited"
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
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Kraft",
          "cluster_id": 2590211,
          "cite": [
            "5 P.3d 68",
            "99 Cal. Rptr. 2d 1",
            "23 Cal. 4th 978",
            "2000 Daily Journal DAR 8825",
            "2000 Cal. Daily Op. Serv. 6660",
            "2000 Cal. LEXIS 5822"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
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
        "journal_ref": "Walter v. United States:lane2_top_cited"
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
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stoker v. State",
          "cluster_id": 2464243,
          "cite": [
            "788 S.W.2d 1",
            "1989 Tex. Crim. App. LEXIS 167",
            "1989 WL 107536"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brimage v. State",
          "cluster_id": 2417512,
          "cite": [
            "918 S.W.2d 466",
            "1996 Tex. Crim. App. LEXIS 5",
            "1994 WL 511395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reedy v. Evanson",
          "cluster_id": 152023,
          "cite": [
            "615 F.3d 197",
            "2010 U.S. App. LEXIS 15974",
            "2010 WL 2991378"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Belton",
          "cluster_id": 5685394,
          "cite": [
            "55 N.Y.2d 49",
            "432 N.E.2d 745",
            "447 N.Y.S.2d 873",
            "1982 N.Y. LEXIS 3067"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Joe Whitten, John Elmer Gaiefsky, Jack Wayne Gish, Richard Lawrence Shimel",
          "cluster_id": 418069,
          "cite": [
            "706 F.2d 1000",
            "13 Fed. R. Serv. 384",
            "1983 U.S. App. LEXIS 27369"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
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
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bittaker",
          "cluster_id": 1179588,
          "cite": [
            "774 P.2d 659",
            "48 Cal. 3d 1046",
            "259 Cal. Rptr. 630",
            "1989 Cal. LEXIS 1462"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Amador Rodriguez Chaidez, A/K/A Rodriguez Amador Chaidez and Amador Rodriguez",
          "cluster_id": 543654,
          "cite": [
            "906 F.2d 377",
            "1990 U.S. App. LEXIS 11006",
            "1990 WL 88172"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karyn Rene Walther, United States of America v. Graciela Barba-Barba",
          "cluster_id": 391946,
          "cite": [
            "652 F.2d 788",
            "1981 U.S. App. LEXIS 20059"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Reid",
          "cluster_id": 2348536,
          "cite": [
            "811 A.2d 530",
            "571 Pa. 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Elkins Carol Elkins, United States of America v. Carol Elkins James Elkins",
          "cluster_id": 778775,
          "cite": [
            "300 F.3d 638"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Howard Christine, Perry Grabosky",
          "cluster_id": 408050,
          "cite": [
            "687 F.2d 749"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Russell B. Allen",
          "cluster_id": 735355,
          "cite": [
            "106 F.3d 695",
            "1997 U.S. App. LEXIS 2129",
            "1997 WL 49827"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miles v. State",
          "cluster_id": 1872653,
          "cite": [
            "241 S.W.3d 28",
            "2007 Tex. Crim. App. LEXIS 1456",
            "2007 WL 3010420"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Finley",
          "cluster_id": 47945,
          "cite": [
            "477 F.3d 250",
            "72 Fed. R. Serv. 377",
            "2007 U.S. App. LEXIS 1806",
            "2007 WL 196531"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yong Hyon Kim",
          "cluster_id": 672873,
          "cite": [
            "27 F.3d 947",
            "1994 U.S. App. LEXIS 16298",
            "1994 WL 287235"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Conley v. State",
          "cluster_id": 1849099,
          "cite": [
            "790 So. 2d 773",
            "2001 WL 393827"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
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
        "journal_ref": "Walter v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110314 OR 9428007 OR 9428008 OR 9428009) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDE1MzcyODAwMDAwJnM9MjMwNTQ4NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110314+OR+9428007+OR+9428008+OR+9428009%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(110314 OR 9428007 OR 9428008 OR 9428009)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTkmcz02NjE4MDYmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110314+OR+9428007+OR+9428008+OR+9428009%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110314 OR 9428007 OR 9428008 OR 9428009)",
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
    "complete_query": "cites:(110314 OR 9428007 OR 9428008 OR 9428009)",
    "indexed_citing_opinions": 532,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110314,
        "count": 447,
        "count_source": "search"
      },
      {
        "opinion_id": 9428007,
        "count": 95,
        "count_source": "search"
      },
      {
        "opinion_id": 9428008,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428009,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 793,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/walter-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg0MTA1NTMmcz05NDIxNzEzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110314+OR+9428007+OR+9428008+OR+9428009%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110314,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 106287,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 107898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 108854,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 344085,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 363614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 365664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 1484849,
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
    "date_created": "2026-07-06T03:59:28Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:59:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:59:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:05:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:59:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Walter v. United States

```
<opinion type="majority">
<author id="b693-7">Mr. Justice Stevens</author>
<p id="Auj">announced the judgment of the Court and delivered an opinion, in which Mr. Justice Stewart joined.</p>
<p id="b693-8">Having lawfully acquired possession of a dozen cartons of motion pictures, law enforcement officers viewed several reels of 8-millimeter film on a Government projector. Labels on the individual film boxes indicated that they contained obscene pictures. The question is whether the Fourth Amendment required the agents to obtain a warrant before they screened the films.</p>
<p id="b693-9">Only a few of the bizarre facts need be recounted. On September 25, 1975, 12 large, securely sealed packages containing 871 boxes of 8-millimeter film depicting homosexual activities were shipped by private carrier from St. Petersburg, Fla., to Atlanta, Ga. The shipment was addressed to “Leggs, Inc.,” <footnotemark>1</footnotemark> but was mistakenly delivered to a substation in the suburbs of Atlanta, where “L’Eggs Products, Inc.,” regularly received deliveries. Employees of the latter company opened <page-number citation-index="1" label="652">*652</page-number>each of the packages, finding the individual boxes of film. They examined the boxes, on one side of which were suggestive drawings, and on the other were explicit descriptions of the contents. One employee opened one or two of the boxes, and attempted without success to view portions of the film by holding it up to the light.<footnotemark>2</footnotemark> Shortly thereafter, they called a Federal Bureau of Investigation agent who picked up the packages on October 1,1975.</p>
<p id="b694-5">Thereafter, without making any effort to obtain a warrant or to communicate with the consignor or the consignee of the shipment, FBI agents viewed the films with a projector. The record does not indicate exactly when they viewed the films, but at least one of them was not screened until more than two months after the FBI had taken possession of the shipment.<footnotemark>3</footnotemark></p>
<p id="b694-6">On April 6, 1977, petitioners were indicted on obscenity charges relating to the interstate transportation of 5 of the 871 films in the shipment. A motion to suppress and return the films was denied, and petitioners were convicted on multiple counts of violating <span class="citation no-link">18 U. S. C. §§ 371</span>, 1462, and 1465. Over Judge Wisdom’s dissent, the Court of Appeals for the Fifth Circuit affirmed, <span class="citation" data-id="9465518"><a href="/opinion/363614/united-states-v-arthur-randall-sanders-jr-gulf-coast-news-agency-inc/" aria-description="Citation for case: United States v. Arthur Randall Sanders, Jr., Gulf Coast...">592 F. 2d 788</a></span>, and rehearing was denied, <span class="citation" data-id="365664"><a href="/opinion/365664/united-states-v-arthur-randall-sanders-jr-gulf-coast-news-agency-inc/" aria-description="Citation for case: United States v. Arthur Randall Sanders, Jr., Gulf Coast...">597 F. 2d 63</a></span> (1979). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./444/914/">444 U. S. 914</a></span>,<footnotemark>4</footnotemark> and now reverse.</p>
<p id="b695-4"><page-number citation-index="1" label="653">*653</page-number>In his concurrence in <em>Stanley </em>v. <em>Georgia, </em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/#569" aria-description="Citation for case: Stanley v. Georgia">394 U. S. 557, 569</a></span>, Mr. Justice Stewart expressed the opinion that the war-rantless projection of motion picture films was an unconstitutional invasion of the privacy of the owner of the films. After noting that the agents in that case were lawfully present in the defendant’s home pursuant to a warrant to search for wagering paraphernalia, Mr. Justice Stewart wrote:</p>
<blockquote id="b695-5">“This is not a case where agents in the course of a lawful search came upon contraband, criminal activity, or criminal evidence in plain view. For the record makes clear that the contents of the films could not be determined by mere inspection. . . . After finding them, the agents spent some 50 minutes exhibiting them by means of the appellant’s projector in another upstairs room. Only then did the agents return downstairs and arrest the appellant.</blockquote>
<blockquote id="b695-6">“Even in the much-criticized case of <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>, the Court emphasized that 'exploratory searches . . . cannot be undertaken by officers with or without a warrant.’ <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#62" aria-description="Citation for case: United States v. Rabinowitz"><em>Id., </em>at 62</a></span>. This record presents a bald violation of that basic constitutional rule. To condone what happened here is to invite a government official to use a seemingly precise and legal warrant only as a ticket to get into a man’s home, and, once inside, to launch forth upon unconfined searches and indiscriminate seizures as if armed with all the unbridled and illegal power of a general warrant.</blockquote>
<blockquote id="b695-7">“Because the films were seized in violation of the Fourth and Fourteenth Amendments, they were inadmis<page-number citation-index="1" label="654">*654</page-number>sible in evidence at the appellant’s trial.” <em>Id., </em>at 571-572 (footnote omitted).</blockquote>
<p id="b696-5">Even though the cases before us involve no invasion of the privacy of the home, and notwithstanding that the nature of the contents of these films was indicated by descriptive material on their individual containers, we are nevertheless persuaded that the unauthorized exhibition of the films constituted an unreasonable invasion of their owner’s constitutionally protected interest in privacy. It was a search; there was no warrant; the owner had not consented; and there were no exigent circumstances.</p>
<p id="b696-6">It is perfectly obvious that the agents’ reason for viewing the films was to determine whether their owner was guilty of a federal offense. To be sure, the labels on the film boxes gave them probable cause to believe that the films were obscene and that their shipment in interstate commerce had offended the federal criminal code. But the labels were not sufficient to support a conviction and were not mentioned in the indictment. Further investigation — that is to say, a search of the contents of the films — was necessary in order to obtain the evidence which was to be used at trial.</p>
<p id="b696-7">The fact that FBI agents were lawfully in possession of the boxes of film did not give them authority to search their contents. Ever since 1878 when Mr. Justice Field’s opinion for the Court in <em>Ex parte Jackson, </em><span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727</a></span>, established that sealed packages in the mail cannot be opened without a warrant, it has been settled that an officer’s authority to possess a package is distinct from his authority to examine its contents.<footnotemark>5</footnotemark> See <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#758" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 758</a></span>; <em>United </em><page-number citation-index="1" label="655">*655</page-number><em>States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#10" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 10</a></span>. When the contents of the package are books or other materials arguably protected by the First Amendment, and when the basis for the seizure is disapproval of the message contained therein, it is especially important that this requirement be scrupulously observed.<footnotemark>6</footnotemark></p>
<p id="b698-4"><page-number citation-index="1" label="656">*656</page-number>Nor does the fact that the packages and one or more of the boxes had been opened by a private party before they were acquired by the FBI excuse the failure to obtain a search warrant. It has, of course, been settled since <em>Burdeau </em>v. <em>McDowell, </em><span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465</a></span>, that a wrongful search or seizure conducted by a private party does not violate the Fourth Amendment and that such private wrongdoing does not deprive the government of the right to use evidence that it has acquired lawfully. See <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#487" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 487-490</a></span>. In these cases there was nothing wrongful about the Government’s acquisition of the packages or its examination of their contents to the extent that they had already been examined by third parties. Since that examination had uncovered the labels, and since the labels established probable cause to believe the films were obscene, the Government argues that the limited private search justified an unlimited official search. That argument must fail, whether we view the official search as an expansion of the private search or as an independent search supported by its own probable cause.</p>
<p id="b698-5">When an official search is properly authorized — whether by consent or by the issuance of a valid warrant — the scope of the search is limited by the terms of its authorization.<footnotemark>7</footnotemark> Consent <page-number citation-index="1" label="657">*657</page-number>to search a garage would not implicitly authorize a search of an adjoining house; a warrant to search for a stolen refrigerator would not authorize the opening of desk drawers. Because “indiscriminate searches and seizures conducted under the authority of ‘general warrants’ were the immediate evils that motivated the framing and adoption of the Fourth Amendment,” <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 583</a></span>, that Amendment requires that the scope of every authorized search be particularly described.<footnotemark>8</footnotemark></p>
<p id="b699-5">If a properly authorized official search is limited by the particular terms of its authorization, at least the same kind of strict limitation must be applied to any official use of a private party’s invasion of another person’s privacy. Even though some circumstances — for example, if the results of the private search are in plain view when materials are turned over to the Government — may justify the Government’s reexamination of the materials, surely the Government may not exceed the scope of the private search unless it has the right to make an independent search. In these cases, the private party had not actually viewed the films. Prior to the Government screening, one could only draw inferences about what was on the films.<footnotemark>9</footnotemark> The projection of the films was a significant expansion of the search that had been conducted previously by a private party and therefore must be characterized as a separate search. That separate search was not supported by any exigency, or by a warrant even though one could have easily been obtained.<footnotemark>10</footnotemark></p>
<p id="b700-4"><page-number citation-index="1" label="658">*658</page-number>The Government claims, however, that because the packages had been opened by a private party, thereby exposing the descriptive labels on the boxes, petitioners no longer had any reasonable expectation of privacy in the films, and that the warrantless screening therefore did not invade any privacy interest protected by the Fourth Amendment. But petitioners expected no one except the intended recipient either to open the 12 packages or to project the films. The 12 cartons were securely wrapped and sealed, with no labels or markings to indicate the character of their contents.<footnotemark>11</footnotemark> There is no reason why the consignor of such a shipment would have any lesser expectation of privacy than the consignor of an ordinary locked suitcase.<footnotemark>12</footnotemark> The fact that the cartons were unexpectedly <page-number citation-index="1" label="659">*659</page-number>opened by a third party before the shipment was delivered to its intended consignee does not alter the consignor’s legitimate expectation of privacy. The private search merely frustrated that expectation in part.<footnotemark>13</footnotemark> It did not simply strip the remaining unfrustrated portion of that expectation of all Fourth Amendment protection.<footnotemark>14</footnotemark> Since the additional search conducted by the FBI — the screening of the films — was not supported by any justification, it violated that Amendment.</p>
<p id="b701-5">We therefore conclude that the rationale of Mr. Justice Stewart’s concurrence in <em>Stanley </em>v. <em>Georgia, </em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/" aria-description="Citation for case: Stanley v. Georgia">394 U. S. 557</a></span>, <page-number citation-index="1" label="660">*660</page-number>is applicable to these cases and that it requires that the judgments of the Court of Appeals be reversed.</p>
<p id="b702-5">
<em>It is so ordered.</em>
</p>
<p id="b702-6">Mr. Justice Marshall concurs in the judgment.</p>
<footnote label="1">
<p id="b693-10"> There was no “Leggs, Inc.” “Leggs” was the nickname of a woman employed by one of petitioners’ companies. The packages indicated that the intended recipient would pick them up and pay for them at the carrier’s terminal in Atlanta.</p>
</footnote>
<footnote label="2">
<p id="b694-7"> Each reel was eight millimeters in width. Petitioner Walter informs us that, excluding three millimeters for sprocketing and one millimeter for the border, the film itself is only four millimeters wide. Brief for Petitioner in No. 79-67, p. 30, n. 8. Since the scenes depicted within the frame are necessarily even more minute, it is easy to understand why such films cannot be examined successfully with the naked eye.</p>
</footnote>
<footnote label="3">
<p id="b694-8"> The FBI had meanwhile received no request from the consignee or the consignor of the films for their return, but the agents had been told by employees of L’Eggs Products, Inc., that inquiries had been made as to their whereabouts.</p>
</footnote>
<footnote label="4">
<p id="b694-9"> The petition for certiorari in No. 79-67 presented 10 separate questions, and the petition in No. 79-148 presented 5 separate questions. Except <page-number citation-index="1" label="653">*653</page-number>with respect to the issues discussed in the text, we have determined that certiorari was improvidently granted. We therefore dismiss as to the other questions that have been briefed and argued. For purposes of decision, we accept the Government’s argument that the delivery of the films to the FBI by a third party was not a “seizure” subject to the warrant requirement of the Fourth Amendment.</p>
</footnote>
<footnote label="5">
<p id="b696-8"><em> </em>“In th[e] enforcement [of regulations as to what may be transported in the mails], a distinction is to be made between different kinds of mail matter, — between what is intended to be kept free from inspection, such as letters, and sealed packages subject to letter postage; and what is open to inspection, such as newspapers, magazines, pamphlets, and other printed matter, purposely left in a condition to be examined. Letters and <page-number citation-index="1" label="655">*655</page-number>sealed packages of this kind in the mail are as fully guarded from examination and inspection, except as to their outward form and weight, as if they were retained by the parties forwarding them in their own domiciles. The constitutional guaranty of the right of the people to be secure in their papers against unreasonable searches and seizures extends to their papers, thus closed against inspection, wherever they may be. Whilst in the mail, they can only be opened and examined under like warrant, issued upon similar oath or affirmation, particularly describing the thing to be seized, as is required when papers are subjected to search in one’s own household. No law of Congress can place in the hands of officials connected with the postal service any authority to invade the secrecy of letters and such sealed packages in the mail; and all regulations adopted as to mail matter of this kind must be in subordination to the great principle embodied in the fourth amendment of the Constitution.” <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#732" aria-description="Citation for case: Ex Parte Jackson">96 U. S., at 732-733</a></span>.</p>
<p id="A6H">And later in his opinion, Mr. Justice Field again noted that “regulations excluding matter from the mail cannot be enforced in a way which would require or permit an examination into letters, or sealed packages subject to letter postage, without warrant, issued upon oath or affirmation, in the search for prohibited matter. . . .” <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#735" aria-description="Citation for case: Ex Parte Jackson"><em>Id., </em>at 735</a></span>.</p>
</footnote>
<footnote label="6">
<p id="b697-10"> “This is the history which prompted the Court less than four years ago to remark that ‘[t]he use by government of the power of search and seizure as an adjunct to a system for the suppression of objectionable publications is not new.’ <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#724" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717, at 724</a></span>. ‘This history was, of course, part of the intellectual matrix within which our constitutional fabric was shaped. The Bill of Rights was fashioned against the background of knowledge that unrestricted power of search and seizure could also be an instrument for stifling liberty of expression.’ <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#729" aria-description="Citation for case: Marcus v. Search Warrant of Property"><em>Id., </em>at 729</a></span>. As MR. Justice Douglas has put it, ‘The commands of our First Amendment (as well as the prohibitions of the Fourth and the Fifth) reflect the teachings of <em>Entick </em>v. <em>Carrington, </em>[19 How. St. Tr. 1029 (1765)]. These three amendments are indeed closely related, safeguarding not only privacy and protection against self-incrimination <page-number citation-index="1" label="656">*656</page-number>but "conscience and human dignity and freedom of expression as well.”’ <em>Frank </em>v. <em>Maryland, </em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#376" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360, 376</a></span> (dissenting opinion).</p>
<blockquote id="b698-7">“In short, what this history indispensably teaches is that the constitutional requirement that warrants must particularly describe the ‘things to be seized’ is to be accorded the most scrupulous exactitude when the ‘things’ are books, and the basis for their seizure is the ideas which they contain.” <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#484" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 484-485</a></span>.</blockquote>
<p id="b698-11">See also <em>Roaden </em>v. <em>Kentucky, </em><span class="citation" data-id="9425416"><a href="/opinion/108854/roaden-v-kentucky/#501" aria-description="Citation for case: Roaden v. Kentucky">413 U. S. 496, 501</a></span>. Although there were 871 reels of film in the shipment, there were only 25 different titles. Since only five of the titles were used as a basis for prosecution, it may be presumed that the other films were not obscene.</p>
</footnote>
<footnote label="7">
<p id="b698-12"> “The requirement that warrants shall particularly describe the things to be seized makes general searches under them impossible and prevents the seizure of one thing under a warrant describing another.” <em>Manon </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 196</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b699-6"> The Warrant Clause of the Fourth Amendment expressly provides that no warrant may issue except those “particularly describing the place to be searched, and the persons or things to be seized.”</p>
</footnote>
<footnote label="9">
<p id="pACiC"> Since the viewing was first done by the Government when it screened the films with a projector, we have no occasion to decide whether the Government would have been required to obtain a warrant had the private party been the first to view them.</p>
</footnote>
<footnote label="10">
<p id="b699-8"> The fact that the labels on the boxes established probable cause to believe the films were obscene clearly cannot excuse the failure to obtain a <page-number citation-index="1" label="658">*658</page-number>warrant; for if probable cause dispensed with the necessity of a warrant, one would never be needed.</p>
<p id="A-ej">Contrary to the dissent, <em>post, </em>at 665-666, n. 3, there were no impracticalities in these cases that would vitiate the warrant requirement. The inability to serve a warrant on the owner of property to be searched does not make execution of the warrant unlawful. See ALI, Model Code of Pre-Arraignment Procedure §220.3 (4) (Prop. Off. Draft 1975). Obviously, such inability does not render a warrant unnecessary under the Fourth Amendment. Nor is it clear in these cases that it would have been impossible to serve petitioners with a search warrant had the FBI made any effort to find them prior to screening the films. See n. 3, <em>supra.</em></p>
</footnote>
<footnote label="11">
<p id="b700-7"> For the same reason, one may not deem petitioners to have consented to the screening merely because the labels on the unexposed boxes were explicit.</p>
<p id="b700-8">Nor can petitioners’ failure to make a more prompt claim to the Gov- ■ emment for return of the films be fairly regarded as an abandonment of their interest in preserving the privacy of the shipment. As subsequent events have demonstrated, such a request could reasonably be expected to precipitate criminal proceedings. We cannot equate an unwillingness to invite a criminal prosecution with a voluntary abandonment of any interest in the contents of the cartons. In any event, the record in these cases does indicate that the defendants made a number of attempts to locate the films before they were examined by the FBI agents.</p>
</footnote>
<footnote label="12">
<p id="b700-9"> The consignor’s expectation of privacy in the contents of a carton delivered to a private carrier must be measured by the condition of the package at the time it was shipped unless there is reason to assume that <page-number citation-index="1" label="659">*659</page-number>it would be opened before it arrived at its destination. Thus, for example, if a gun case is delivered to a carrier, there could then be no expectation that the contents would remain private, cf. <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 764-765, n. 13</a></span>; but if the gun case were enclosed in a locked suitcase, the shipper would surely expect that the privacy of its contents would be respected.</p>
<p id="AHbV">The dissent asserts, <em>post, </em>at 665, that “[a]ny subjective expectation of privacy on the part of petitioners was undone ... by their own actions and the private search.” But it is difficult to understand how petitioners’ subjective expectation of privacy could have been altered in any way by subsequent events of which they were obviously unaware.</p>
</footnote>
<footnote label="13">
<p id="b701-8"> A partial invasion of privacy cannot automatically justify a total invasion. As Learned Hand noted in a somewhat different context: “It is true that when one has been arrested in his home or his office, his privacy has already been invaded; but that interest, though lost, is altogether separate from the interest in protecting his papers from indiscriminate rummage, even though both are customarily grouped together as parts of the 'right of privacy.’ ” <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9638337"><a href="/opinion/1484849/united-states-v-rabinowitz/#735" aria-description="Citation for case: United States v. Rabinowitz">176 F. 2d 732, 735</a></span> (CA2 1949), rev’d, <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>. Judge Hand’s view was ultimately vindicated in <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#768" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 768</a></span>, which specifically disapproved this Court’s decision in <em>Rabinowitz. </em>See also Mr. Justice Stewart’s opinion concurring in the result in <em>Stanley </em>v. <em>Georgia, </em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/#571" aria-description="Citation for case: Stanley v. Georgia">394 U. S. 557, 571-572</a></span>, quoted <em>supra, </em>at 653-654.</p>
</footnote>
<footnote label="14">
<p id="b701-9"> It is arguable that a third party’s inspection of the contents of “private books, papers, memoranda, etc.” could be so complete that there would be no additional search by the FBI when it re-examines the materials. Cf. <em>Burdeau </em>v. <em>McDowell, </em><span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/#470" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465, 470</a></span>. But this is not such a case, because it was clearly necessary for the FBI to screen the films, which the private party had not done, in order to obtain the evidence needed to accomplish its law enforcement objectives.</p>
</footnote>
</opinion>
```

---
