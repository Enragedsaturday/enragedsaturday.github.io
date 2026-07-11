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

## GROUP: _overhaul2/lake/cases/United States v. Williams.json  (`lake-record`, 2 assertions)

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
{"assertion_id": "9cdd28d11b981144", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Williams"}, "payload": {"all": [{"cite": "435 F.3d 1148", "page": "1148", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "435"}, {"cite": "2006 U.S. App. LEXIS 2235", "page": "2235", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2006"}, {"cite": "2006 WL 213852", "page": "213852", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2006"}], "display": "435 F.3d 1148", "official": {"cite": "435 F.3d 1148", "page": "1148", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "435"}, "official_selection_present": true, "record_id": "United States v. Williams"}}
{"assertion_id": "a8a72e8453095251", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Williams"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Williams", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/United States v. Wilson.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Wilson
type: case
citation: "13 F.4th 961 (2021)"
parallel_cite: ""
neutral_cite: ""
court: 9th Cir.
court_level: coa
circuit: ca9
year: 2021
date_decided: 2021-09-21
docket: 18-50440
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
  opinion_url: "https://www.courtlistener.com/opinion/5296785/united-states-v-luke-wilson/"
  cluster_id: 5296785
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Wilson
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Private and Foreign Searches]]"
    role: "Key — hash-match split (9th Cir.)"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
related:
  - "[[Fourth Amendment Framework]]"
  - "[[Two Definitions of Search]]"
  - "[[United States v. Jacobsen]]"
  - "[[United States v. Reddick]]"
  - "[[Carpenter v. United States]]"
tags:
  - case
  - fourth-amendment
  - private-search-doctrine
  - hash-value
  - child-pornography
  - digital-privacy
  - ninth-circuit
holding: "Under the private-search doctrine of Walter and Jacobsen, the government may repeat a private party's search without a warrant only insofar as it does not exceed the scope of that private search; where Google's automated system flagged four email attachments as matching known child-pornography hashes but no person had actually viewed those images, a government agent's warrantless opening and viewing of them exceeded the antecedent private search — learning new information and expanding the intrusion — so it was not justified by the private-search exception, and Wilson's conviction was reversed."
aliases:
  - United States v. Wilson
  - "United States v. Wilson (9th Cir. 2021)"
---

# United States v. Wilson

*13 F.4th 961 (9th Cir. 2021)* (No. 18-50440) · U.S. Court of Appeals for the Ninth Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 5296785 → lead opinion 5125347 (13 F.4th 961, decided 2021-09-21); Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — CL text is slip-paginated). S9 promotes. -->

## Background
Google's automated systems detected that four email attachments in Luke Wilson's account matched the hash values of images previously identified as child pornography, and Google reported them to the National Center for Missing and Exploited Children, which forwarded the report to a law-enforcement task force. Critically, no Google employee — or any other person — had actually opened and viewed those particular four images; the match was generated by algorithm alone. A government agent then opened and viewed the four attachments without a warrant, described them in detail, and used them to obtain warrants to search Wilson's email account and home. The district court denied suppression, reasoning the agent's viewing did not exceed Google's private search.

## Issue
Whether a government agent's warrantless opening and viewing of email attachments — flagged by a private company's automated hash-matching but never actually viewed by any person — was justified by the private-search exception to the Fourth Amendment.

## Rule
The private-search doctrine excuses a warrant only when the government's search does not exceed the scope of an antecedent private search; the government may not learn new, critical information or intrude on privacy interests beyond what the private party already exposed. Measuring the agent's conduct against Google's algorithmic match, the panel held: "we hold that it was not. We therefore reverse the district court's denial of Wilson's motion to suppress and vacate Wilson's conviction." — 13 F.4th 961, slip op. at 6. ^pin-op6

## Application
The court concluded the agent's warrantless viewing exceeded Google's antecedent private search in two ways. First, it produced new, critical information: because no person had ever viewed the four images, opening them told the government something Google's hash-matching had not — the actual visual content — which the agent then used to secure warrants and prosecute. Second, it expanded the intrusion on Wilson's privacy: the agent's human viewing of the images went beyond the algorithm's limited, non-visual comparison, and on the record the government had not shown the flagged files were exact duplicates of images a person had previously seen. Because the government thereby went beyond the frustrated portion of Wilson's expectation of privacy, the private-search exception did not apply and the warrantless viewing violated the Fourth Amendment.

## Conclusion
The Ninth Circuit **reversed** the denial of suppression and **[[Reading and Citing Cases#vacated|vacated]]** Wilson's conviction, holding the warrantless viewing exceeded the private search.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Wilson* is the Ninth Circuit's counterweight on the digital **private-search** frontier: applying *[[United States v. Jacobsen|Jacobsen]]*'s exceed-the-scope test, it holds that an **algorithmic hash-match no human has viewed** does not let the government open the file without a warrant. That squarely diverges from the Fifth Circuit's *[[United States v. Reddick|Reddick]]* (and the Sixth Circuit's *[[United States v. Miller|Miller]]*), which treat the confirmatory viewing as within the private search — an unresolved split worth teaching alongside *[[Carpenter v. United States|Carpenter]]*'s caution about extending old doctrines to new technology.

## Appears on
- [[Private and Foreign Searches]] — *Key — hash-match split (9th Cir.)*
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*

## Sources
- [*United States v. Wilson*, 13 F.4th 961 (9th Cir. 2021)](https://www.courtlistener.com/opinion/5296785/united-states-v-luke-wilson/) — pinpoint: slip op. at 6 (government's warrantless viewing exceeded the antecedent private search; the CL opinion text carries slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7c7c37c439f31331", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Wilson"}, "payload": {"all": [{"cite": "13 F.4th 961", "page": "961", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "13"}], "display": "13 F.4th 961", "official": {"cite": "13 F.4th 961", "page": "961", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "13"}, "official_selection_present": true, "record_id": "United States v. Wilson"}}
{"assertion_id": "438f18cf14a4f2ba", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Wilson"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Wilson", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Wilson

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Wilson",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Luke Wilson",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Wilson",
    "court": "9th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": "2021-09-21",
    "year": 2021,
    "docket": "18-50440",
    "cluster_id": 5296785,
    "lead_opinion_id": 5125347,
    "sibling_ids": [],
    "absolute_url": "/opinion/5296785/united-states-v-luke-wilson/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "13 F.4th 961",
      "volume": "13",
      "reporter": "F.4th",
      "page": "961",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "13 F.4th 961",
        "volume": "13",
        "reporter": "F.4th",
        "page": "961",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "13 F.4th 961",
    "official_selection": {
      "court_class": "coa",
      "selected": "13 F.4th 961",
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
    "date_created": "2026-07-07T18:19:50Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:19:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:19:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:19:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:19:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-wilson--5296785",
      "to_record_id": "United States v. Wilson",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Wilson

```
                       FOR PUBLICATION

   UNITED STATES COURT OF APPEALS
        FOR THE NINTH CIRCUIT


 UNITED STATES OF AMERICA,                     No. 18-50440
           Plaintiff-Appellee,
                                                 D.C. No.
                  v.                       3:15-cr-02838-GPC-1

 LUKE NOEL WILSON,
        Defendant-Appellant.                      OPINION

        Appeal from the United States District Court
          for the Southern District of California
        Gonzalo P. Curiel, District Judge, Presiding

         Argued and Submitted November 15, 2019
                   Pasadena, California

                    Filed September 21, 2021

   Before: Marsha S. Berzon and Paul J. Watford, Circuit
      Judges, and Robert H. Whaley, * District Judge.

                    Opinion by Judge Berzon




     *
       The Honorable Robert H. Whaley, United States District Judge for
the Eastern District of Washington, sitting by designation.
2                  UNITED STATES V. WILSON

                          SUMMARY **


                          Criminal Law

    The panel vacated a conviction for possession and
distribution of child pornography, reversed the district
court’s denial of a motion to suppress, and remanded for
further proceedings in a case in which the panel addressed
whether the government’s warrantless search of the
defendant’s email attachments was justified by the private
search exception to the Fourth Amendment.

    As required by federal law, Google reported to the
National Center for Missing and Exploited Children
(NCMEC) that the defendant had uploaded four images of
apparent child pornography to his email account as email
attachments. No one at Google had opened or viewed the
defendant’s email attachments; its report was based on an
automated assessment that the images the defendant
uploaded were the same as images other Google employees
had earlier viewed and classified as child pornography.
Someone at NCMEC then, also without opening or viewing
them, sent the defendant’s email attachments to the San
Diego Internet Crimes Against Children Task Force, where
an officer ultimately viewed the email attachments without
a warrant. The officer then applied for warrants to search
both the defendant’s email account and his home, describing
the attachments in detail in the application.




    **
       This summary constitutes no part of the opinion of the court. It
has been prepared by court staff for the convenience of the reader.
                 UNITED STATES V. WILSON                       3

    The private search doctrine concerns circumstances in
which a private party’s intrusions would have constituted a
search had the government conducted it and the material
discovered by the private party then comes into the
government’s possession. Invoking the precept that when
private parties provide evidence to the government on their
own accord, it is not incumbent on the police to avert their
eyes, the Supreme Court formalized the private search
doctrine in Walter v. United States, 447 U.S. 649 (1980),
which produced no majority decision, and United States v.
Jacobson, 466 U.S. 109 (1984), which did.

    The panel held that the government did not meet its
burden to prove that the officer’s warrantless search was
justified by the private search exception to the Fourth
Amendment’s warrant requirement. The panel wrote that
both as to the information the government obtained and the
additional privacy interests implicated, the government’s
actions here exceed the limits of the private search exception
as delineated in Walter and Jacobsen and their progeny.
First, the government search exceeded the scope of the
antecedent private search because it allowed the government
to learn new, critical information that it used first to obtain a
warrant and then to prosecute the defendant. Second, the
government search also expanded the scope of the
antecedent private search because the government agent
viewed the defendant’s email attachments even though no
Google employee—or other person—had done so, thereby
exceeding any earlier privacy intrusion. Moreover, on the
limited evidentiary record, the government has not
established that what a Google employee previously viewed
were exact duplicates of the defendant’s images. And, even
if they were duplicates, such viewing of others’ digital
communications would not have violated the defendant’s
expectation of privacy in his images, as Fourth Amendment
4               UNITED STATES V. WILSON

rights are personal. The panel concluded that the officer
therefore violated the defendant’s Fourth Amendment right
to be free from unreasonable searches when he examined the
defendant’s email attachments without a warrant.


                       COUNSEL

Devin Burstein (argued), Warren & Burstein, San Diego,
California, for Defendant-Appellant.

Peter Ko (argued), Assistant United States Attorney; Helen
H. Hong, Chief, Appellate Section, Criminal Division;
Robert S. Brewer, Jr., United States Attorney; United States
Attorney’s Office, San Diego, California; for Plaintiff-
Appellee.

Jennifer Lynch and Andrew Crocker, Electronic Frontier
Foundation, San Francisco, California; Jennifer Stisa
Granick, American Civil Liberties Union Foundation, San
Francisco, California; Brett Max Kaufman and Nathan Freed
Wessler, American Civil Liberties Union Foundation, New
York, New York; for Amici Curiae Electronic Frontier
Foundation and American Civil Liberties Union Foundation.

Marc Rotenberg, Alan Butler, and Megan Iorio, Electronic
Privacy Information Center, Washington, D.C., for Amicus
Curiae Electronic Privacy Information Center (EPIC).

Ryan T. Mrazik, Erin K. Earl, and Rachel A.S. Haney,
Perkins Coie LLP, Seattle, Washington, for Amici Curiae
Google LLC and Facebook, Inc.
                 UNITED STATES V. WILSON                    5

                         OPINION

BERZON, Circuit Judge:

    We once again consider the application of the Fourth
Amendment’s warrant requirement to new forms of
communication technology. See, e.g., United States v. Cano,
934 F.3d 1002 (9th Cir. 2019); cf. Carpenter v. United
States, 138 S. Ct. 2206 (2018). “When confronting [such]
concerns wrought by digital technology, th[e] [Supreme]
Court [and this court] ha[ve] been careful not to uncritically
extend existing precedents.” Id. at 2222. Our question this
time concerns the private search exception to the Fourth
Amendment—specifically, the intersection between
electronic communications providers’ control over material
on their own servers and the Fourth Amendment’s restriction
of warrantless searches and seizures, which limits only
governmental action. See Burdeau v. McDowell, 256 U.S.
465 (1921); Walter v. United States, 447 U.S. 649 (1980);
United States v. Jacobsen, 466 U.S. 109 (1984).

    The events giving rise to Luke Wilson’s conviction and
this appeal were triggered when Google, as required by
federal law, reported to the National Center for Missing and
Exploited Children (NCMEC) that Wilson had uploaded
four images of apparent child pornography to his email
account as email attachments. No one at Google had opened
or viewed Wilson’s email attachments; its report was based
on an automated assessment that the images Wilson
uploaded were the same as images other Google employees
had earlier viewed and classified as child pornography.
Someone at NCMEC then, also without opening or viewing
them, sent Wilson’s email attachments to the San Diego
Internet Crimes Against Children Task Force (ICAC), where
an officer ultimately viewed the email attachments without
a warrant. The officer then applied for warrants to search
6                   UNITED STATES V. WILSON

both Wilson’s email account and Wilson’s home, describing
the attachments in detail in the application.

    Our question is whether the government’s warrantless
search of Wilson’s email attachments was justified by the
private search exception to the Fourth Amendment. See
Walter, 447 U.S. at 655–56; Jacobsen, 466 U.S. at 113–14.
For the reasons that follow, we hold that it was not. We
therefore reverse the district court’s denial of Wilson’s
motion to suppress and vacate Wilson’s conviction.

I. Background

    A. Google’s Identification              of    Apparent        Child
       Pornography

    Electronic communication service providers are not
required “affirmatively [to] search, screen, or scan” for
apparent violations on their platforms of federal child
pornography laws. 18 U.S.C. §§ 2258A(f), 2258E. But “[i]n
order to reduce . . . and . . . prevent the online sexual
exploitation of children,” such providers, including Google,
are directed, “as soon as reasonably possible after obtaining
actual knowledge” of “any facts or circumstances from
which there is an apparent violation of . . . child pornography
[statutes],” to “mak[e] a report of such facts or
circumstances” to NCMEC. 18 U.S.C. § 2258A(a). 1
NCMEC then forwards what is known as a CyberTip to the


    1
      “A provider that knowingly and willfully failed to make a report
required . . . shall be fined.” 18 U.S.C. § 2258A(e). Further, in the case
of “intentional, reckless, or other misconduct,” there may be “a civil
claim or criminal charge against a provider . . . arising from the
performance of the reporting or preservation responsibilities.” Id. at
§§ 2258B(a), (b).
                   UNITED STATES V. WILSON                           7

appropriate law enforcement agency for                       possible
investigation. Id. at §§ 2258A(a)(1)(B)(ii), (c).

    According to a two-page declaration from a senior
manager at Google, the company “independently and
voluntarily take[s] steps to monitor and safeguard [its]
platform,” including using a “proprietary hashing
technology” to identify apparent child pornography. 2

    As described in the record—vaguely, and with the gaps
noted—the process works as follows:

   First, a team of Google employees are “trained by
counsel on the federal statutory definition of child
pornography and how to recognize it.” Neither the training
materials themselves nor a description of their contents
appear in or are attached to the Google manager’s
declaration.

    Second, these employees “visually confirm[]” an image
“to be apparent child pornography.” According to an
industry classification standard created by various electronic
service providers, there are four industry categorizations:
“A1” for a sex act involving a prepubescent minor; “A2” for
a lascivious exhibition involving a prepubescent minor;
“B1” for a sex act involving a pubescent minor; and “B2”
for a lascivious exhibition involving a pubescent minor.

    Third, “[e]ach offending image” judged to be “apparent
child pornography as defined in 18 USC § 2256” is given a
hash value, which is “added to [the] repository of hashes.”

    2
      “A hash value is (usually) a short string of characters generated
from a much larger string of data (say, an electronic image) using an
algorithm.” United States v. Ackerman, 831 F.3d 1292, 1294 (10th Cir.
2016).
8               UNITED STATES V. WILSON

As far as the record shows, Google “stores only the hash
values” of images identified as apparent child pornography,
not the actual images. The government does not represent
otherwise.

    Finally, Google “[c]ompare[s] these hashes to hashes of
content uploaded to [their] services.” The exact manner in
which hash values are assigned to either the original
photographs or the ones deemed to replicate them is not
described in the Google manager’s declaration or anywhere
else in the record.

    B. Government Search

    On June 4, 2015, Google, using its propriety technology,
“became aware” that Wilson had attached to emails in his
email account—which may or may not have been sent—four
files that included apparent child pornography. United States
v. Wilson, No. 3:15-cr-02838-GPC, 2017 WL 2733879, at
*3 (S.D. Cal. June 26, 2017). In compliance with its
reporting obligations, Google automatically generated and
sent an electronic CyberTipline report to NCMEC. The
CyberTipline report included Wilson’s four email
attachments. According to the Google manager’s
declaration, “a Google employee did not view the images . . .
concurrently to submitting the report to NCMEC.” The
CyberTipline report did specify that Google had classified
each of Wilson’s four email attachments as “A1” under an
industry classification standard for “content [which]
contain[s] a depiction of a prepubescent minor engaged in a
sexual act.”

   Google’s report included Wilson’s email address,
secondary email address, and IP addresses. NCMEC
supplemented Google’s report with geolocation information
                    UNITED STATES V. WILSON                             9

associated with Wilson’s IP addresses, but did “not open[]
or view[] any uploaded files submitted with this report.”

    NCMEC then forwarded the CyberTip to the San Diego
Internet Crimes Against Children Task Force (“ICAC”).
Agent Thompson, a member of the San Diego ICAC,
received the report. He followed San Diego ICAC
procedure, which at the time called for inspecting the images
without a warrant whether or not a Google employee had
reviewed them. 3

    After Agent Thompson looked at Wilson’s four email
attachments, he applied for a search warrant of Wilson’s
email account. His affidavit asserted that probable cause for
the warrant was based on two facts: first, that “Google
became aware of four (4) image files depicting suspected
child pornography;” and second, that he had “reviewed the
four (4) images reported by Google to NCMEC and
determined they depict child pornography.” In support of his
own child pornography assessment, he included in the
warrant application detailed “descriptions of each of these
images.” The affidavit did not include the fact that Google
had originally classified the images as “A1” or provide any
detail about how Google had either classified or later
automatically identified Wilson’s images as apparent child
pornography.

   On the basis of the application and affidavit submitted
by Agent Thompson, a magistrate judge issued a search


    3
      Agent Thompson testified that San Diego ICAC, which includes
both local, county, regional, and federal agencies, now obtains a search
warrant before opening a CyberTip when the provider has not viewed
the images. It is not clear from the record whether other ICAC task forces
across the country have adopted the same policy.
10              UNITED STATES V. WILSON

warrant for Wilson’s email account. When Agent Thompson
executed the warrant, he discovered numerous email
exchanges in which Wilson received and sent images and
video files of alleged child pornography and in which
Wilson offered to pay for the creation of child pornography.

    Agent Thompson then obtained a search warrant for
Wilson’s residence. On executing the warrant, law
enforcement officers found and seized several electronic
devices that contained evidence of child pornography. One
officer observed a backpack being tossed over Wilson’s
balcony at the time officers were knocking on Wilson’s door
and announcing their presence. Wilson’s checkbook and a
thumb drive containing thousands of images of child
pornography—including the four images reported by
Google—were found in the backpack.

     C. Motion to Suppress

    Wilson filed a motion to suppress all evidence seized
from his email account and residence, arguing that Agent
Thompson’s review of his email attachments without a
warrant was impermissible under the Fourth Amendment.
Relying principally on Jacobsen, 466 U.S. 109, and United
States v. Tosti, 733 F.3d 816 (9th Cir. 2013), the government
maintained in response that Agent Thompson’s review of the
four images did not exceed the scope of Google’s private
search and so, under the private search doctrine as
enunciated in Jacobsen and Tosti, was valid without a
warrant.

    The district court agreed. The court denied Wilson’s
motion to suppress on the ground that the government’s
warrantless search did not exceed the scope of the antecedent
private search and so did not require a warrant. The district
court also concluded that “if [Agent] Thompson’s
                     UNITED STATES V. WILSON                            11

warrantless viewing of the four images constituted an illegal
search, neither excising the tainted evidence from the
affidavit nor the good faith exception would prevent
operation of the exclusionary rule.” 4 Wilson, 2017 WL
2733879, at *12–13.

   After waiving his right to a jury trial, Wilson was
convicted of possession and distribution of child
pornography 5 and sentenced to 11 years of incarceration and


    4
        The government does not contest these contingent rulings.
      5
        While this appeal was pending, the California Court of Appeal held
that “the government’s warrantless search of Wilson’s four images was
permissible under the private search doctrine.” People v. Wilson, 56 Cal.
App. 5th 128, 147 (2020), as modified on denial of reh’g (Nov. 6, 2020),
review denied (Jan. 20, 2021). We have not squarely addressed the
preclusive effect of the denial of a suppression motion in an earlier state-
court proceeding. Other circuits, however, have held that “the
government may not collaterally estop a criminal defendant from
relitigating an issue against the defendant in a different court in a prior
proceeding.” United States v. Harnage, 976 F.2d 633, 636 (11th Cir.
1992); accord United States v. Pelullo, 14 F.3d 881, 896 (3d Cir. 1994);
United States v. Gallardo-Mendez, 150 F.3d 1240, 1244 (10th Cir.
1998). Citing those cases, we came to the similar conclusion that, in
criminal trials, the government “may not use collateral estoppel to
establish, as a matter of law, an element of an offense or to conclusively
rebut an affirmative defense on which the Government bears the burden
of proof beyond a reasonable doubt.” United States v. Smith-Baltiher,
424 F.3d 913, 920 (9th Cir. 2005) (quoting United States v. Arnett,
353 F.3d 765, 766 (9th Cir. 2003) (en banc) (per curiam)).

     We need not definitively resolve the preclusion question as it relates
to a motion to suppress, here, as the government has not asserted
collateral estoppel, so the argument is waived. Harbeson v. Parke Davis,
Inc., 746 F.2d 517, 520 (9th Cir. 1984) (“The United States was unaware
that Mr. Wilson had raised the same issue in his state appeal until the
letter filed in this case by [defense counsel] on October 16, 2020.”).
12                  UNITED STATES V. WILSON

10 years of supervised release for each count, to run
concurrently. 6

II. Discussion

    The government does not dispute for purposes of this
case Wilson’s assertion that Agent Thompson’s review of
his email attachments was a search within the meaning of the
Fourth Amendment. We proceed on that assumption as
well—that is, we assume that Wilson had a subjective
expectation of privacy in his email attachments that society
is prepared to recognize as reasonable, see Kyllo v. United
States, 533 U.S. 27, 33 (2001) (citing Katz v. United States,
389 U.S. 347, 361 (1967) (Harlan, J., concurring)); see also
United States v. Miller, 982 F.3d 412, 427 (6th Cir. 2020)
(taking the same approach); cf. United States v. Ackerman,
831 F.3d 1292, 1308 (10th Cir. 2016) (holding that when the
government views email attachments it is a “search” for
Fourth Amendment purposes under both an expectation-of-
privacy and a trespass-to-chattels theory). 7 Our question,
then, is whether Agent Thompson was permitted to look at
Wilson’s email attachments under the private search


     6
      Wilson maintains that the district court did not obtain a valid
waiver of his right to a jury trial, as required by Fed. R. Crim. P. 23(a).
Because we vacate Wilson’s conviction and reverse the district court’s
denial of Wilson’s motion to suppress, we do not reach this issue.
     7
      Because we hold that the government’s warrantless search violated
Wilson’s privacy-based Fourth Amendment rights, we do not consider
Wilson’s alternative argument that the government’s search violated his
property-based Fourth Amendment rights. See Carpenter v. United
States, 138 S. Ct. 2206, 2269 (2018) (Gorsuch, J. dissenting) (“[F]ew
doubt that e-mail should be treated much like the traditional mail it has
largely supplanted—as a bailment in which the owner retains a vital and
protected legal interest.”).
                UNITED STATES V. WILSON                   13

exception, such that the Fourth Amendment did not require
him to procure a warrant.

    We review the district court’s denial of Wilson’s motion
to suppress de novo and the district court’s underlying
factual findings for clear error. See United States v. Camou,
773 F.3d 932, 937 (9th Cir. 2014); see also United States v.
Mulder, 808 F.2d 1346, 1348 (9th Cir. 1987).

   A. Private Search Exception

    As the Fourth Amendment protects individuals from
government actors, not private ones, see Burdeau v.
McDowell, 256 U.S. 465 (1921), a private party may conduct
a search that would be unconstitutional if conducted by the
government. The private search doctrine concerns
circumstances in which a private party’s intrusions would
have constituted a search had the government conducted it
and the material discovered by the private party then comes
into the government’s possession. Invoking the precept that
when private parties provide evidence to the government “on
[their] own accord[,] … it [i]s not incumbent on the police
to . . . avert their eyes,” Coolidge v. New Hampshire,
403 U.S. 443, 489 (1971), the Supreme Court formalized the
private search doctrine in a pair of decisions about four
decades ago: Walter v. United States, 447 U.S. 649 (1980),
which produced no majority decision, and United States v.
Jacobsen, 466 U.S. 109 (1984), which did.

       1. Doctrinal Foundations

    Beginning from the initial articulation of the private
search doctrine, the extent to which it excuses the
government from compliance with the warrant requirement
of the Fourth Amendment has been the subject of concern.
The exception has, for example, been described as
14               UNITED STATES V. WILSON

“unsettling” for its potential reach. 1 Wayne R. LaFave,
Search and Seizure: A Treatise on the Fourth Amendment
§1.8(b) (6th ed. 2020); see also Jacobsen, 466 U.S. at 129–
34 (White, J., concurring in part and concurring in
judgment). On examination, however, the history of the
exception confirms that it is, in truth, a narrow doctrine with
limited applications.

    Beginning with Burdeau, the Supreme Court has
distinguished between government agents and private
parties for purposes of the Fourth Amendment. Burdeau
considered whether the Fourth Amendment restricts the
government’s ability to use papers incriminating an
individual when those papers were volunteered to the
government by a private party who had stolen them. Burdeau
disregarded the private theft, noting that although “[t]he
Fourth Amendment gives protection against unlawful
searches and seizures, . . . its protection applies to
governmental action.” 256 U.S. at 475.

    Coolidge, decided 50 years after Burdeau, addressed
whether a private party who provides the government with
another person’s contraband or evidentiary material can be
considered an agent of the government for purposes of the
Fourth Amendment. In that case, local police officers arrived
at a suspect’s home, questioned his wife about his
involvement in a murder, and obtained from his wife a rifle
and articles of clothing belonging to the suspect. Coolidge,
403 U.S. at 446, 486. The opinion does not explain whether
the suspect’s wife had proper possession of the items. The
Court stated only that, had the suspect’s wife, “wholly on her
own initiative, sought out her husband’s guns and clothing
and then taken them to the police station to be used as
evidence against him, there can be no doubt under [Burdeau]
that the articles would later have been admissible in
                UNITED STATES V. WILSON                   15

evidence.” Id. at 487. The relevant inquiry, according to the
Court, was whether the suspect’s wife, “in light of all the
circumstances of the case, must be regarded as having acted
as an instrument or agent of the state when she produced her
husband’s belongings.” Id. (internal quotation marks
omitted). As the record showed that the suspect’s wife had
shared the suspect’s guns and clothes with the local police
“of her own accord,” Coolidge held that “it was not
incumbent on the police to stop her or avert their eyes” when
offered the critical evidence. Id. at 489.

       2. Doctrinal Scope

    Following Burdeau and Coolidge, both Walter and
Jacobsen considered a warrantless government search after
a private party “freely made available” certain information
for the government’s inspection. Jacobsen, 466 U.S. at 119–
20 (citing Coolidge, 403 U.S. at 487–90). Together, the cases
determined that an antecedent private search excuses the
government from obtaining a warrant to repeat the search but
only when the government search does not exceed the scope
of the private one. That is, “[t]he additional invasions of
respondents’ privacy by the government agent must be tested
by the degree to which they exceeded the scope of the private
search.” Id. at 115.

    In Walter, a package of obscene films was mistakenly
delivered to the wrong recipient. 447 U.S. at 651. The
recipient opened the external packaging and examined the
boxes containing individual films. Id. at 651–52. Each box
displayed “suggestive drawings” on one side and “explicit
descriptions of the contents” of the film on the other. Id.
at 652. After reading these descriptions, and “attempt[ing]
without success to view portions of the film by holding it up
to the light,” the recipient notified the FBI about the
mistaken delivery. Id. The FBI then seized the boxes and
16               UNITED STATES V. WILSON

screened one of the films without first obtaining a warrant.
Id.

    Walter did not result in a majority opinion, but a majority
of the justices concluded that there had been a violation of
the Fourth Amendment, and a different majority of justices
agreed on the standard to be applied.

    Justice Stevens, joined by Justice Stewart, announced the
judgment of the Court. Their opinion concluded that the
government search exceeded the scope of the antecedent
actions by the private individuals in two respects. First, the
government agents had screened the film for the purpose of
learning information necessary to determine that a crime had
been committed:

       It is perfectly obvious that the agents’ reason
       for viewing the films was to determine
       whether their owner was guilty of a federal
       offense. To be sure, the labels on the film
       boxes gave them probable cause to believe
       that the films were obscene and that their
       shipment in interstate commerce had
       offended the federal criminal code. . . . [But]
       a search of the contents of the films . . . was
       necessary in order to obtain the evidence
       which was to be used at trial.

Id. at 654. Second, the government agents had gone beyond
the physical bounds of the private search, because “the
private party had not actually viewed the films.” Id. at 657.
“The private search [thus] merely frustrated [the]
expectation [of privacy] in part,” not in full. Id. at 659. “It
                    UNITED STATES V. WILSON                          17

did not simply strip the remaining unfrustrated portion of
that expectation of all Fourth Amendment protection.” Id. 8

    The four justices in dissent would have concluded that
there was no Fourth Amendment violation. The dissenters
disputed not the basic approach of Justice Stevens’ opinion
but its application to the facts of the case. Specifically, the
dissent stressed that “[t]he containers . . . clearly revealed the
nature of their contents,” such that the private employees “so
fully ascertained the nature of the films . . . [that] the FBI’s
subsequent viewing of the movies . . . was not an additional
search subject to the warrant requirement.” Id. at 663–64
(Blackmun, J., dissenting, joined by Burger, C.J., and Powell
and Rehnquist, JJ.).

    Four years after Walter, the Supreme Court again applied
the private search doctrine. Importantly, Jacobsen
recognized “the agreement [in Walter] on the standard to be
applied in evaluating the relationship between the two
searches.” 466 U.S. at 117 n.12.

   Jacobsen concerned a government search of a Federal
Express (“FedEx”) package that had been partially opened
by FedEx employees. See 466 U.S. at 111. While examining
a damaged package, the FedEx employees “opened the

     8
       Justice Marshall concurred only in the judgment. Justice White,
joined by Justice Brennan, concurred, noting that “the packages already
had been opened, and the Government saw no more than what was
exposed to plain view.” Walter, 447 U.S. at 661 (White, J., concurring
in part and concurring in judgment). Although Justice Stevens
emphasized that the private parties had not screened the film, see id. at
657 & n.9, the concurring justices would have found a Fourth
Amendment violation even if the private parties had done so, as “a
private screening of the films would not have destroyed petitioners’
privacy interest in them.” Id. at 662.
18               UNITED STATES V. WILSON

package,” “cut open the tube” within the package, and
“found a series of four zip-lock plastic bags, the outermost
enclosing the other three and the innermost containing about
six and a half ounces of white powder.” Id. The employees
“observed . . . white powder in the innermost plastic bag,”
but did not open the (presumably transparent) bag. Id.
Instead, they called the Drug Enforcement Administration
(DEA), put the plastic bags back in the tube, and placed the
tube back in the box. Id.

    When DEA agents arrived, they did two things: First, to
visually inspect the contents of the plastic bags, DEA agents
removed the tube from the box and the plastic bags from the
tube. See id. Second, federal agents “opened each of the four
bags and removed a trace of the white substance with a knife
blade.” Id. at 111–12. They performed a field test to
determine whether the powder in the plastic bags was
cocaine. See id.

    Jacobsen considered whether the private search
exception as adopted by a majority of justices in Walter
applied to the facts at hand. In doing so, Jacobsen, like
Justice Stevens’ opinion in Walter, looked at both the degree
to which the government’s actions led to observing new
information not uncovered by the private search and the
extent to which the government’s investigation intruded on
the package owner’s privacy interests to a greater degree
than had the private party’s actions. As to the first parameter,
the information gleaned by the government, Jacobsen
permitted the government agent to “reexamine”—that is,
examine in the same manner—the package previously
examined by FedEx, the private party. The government
“could utilize the [private] employees’ testimony concerning
the contents of the package,” noted Jacobsen; “[p]rotecting
the risk of misdescription . . . is not protected by the Fourth
                UNITED STATES V. WILSON                   19

Amendment.” 466 U.S. at 119. As to the second parameter,
the additional impairment of privacy interests, Jacobsen
emphasized that the private search exception turns on parity
with the impact of the private search: “[O]nce frustration of
the original expectation of privacy occurs, the Fourth
Amendment does not prohibit governmental use of the now-
nonprivate information.” Id. at 117.

    Applying these precepts, Jacobsen concluded that the
“removal of the plastic bags from the tube and the
[government] agent’s visual inspection of their contents” did
not exceed the scope of the private search as to the
information obtained. Id. at 120. “[T]he agent[s] . . .
learn[ed] nothing [from those actions] that had not
previously been learned during the private search” and
conveyed to the federal agents by the FedEx employees. Id.
And as to the privacy interests, the governmental search to
that point “infringed no legitimate expectation of privacy
and hence was not a ‘search’ within the meaning of the
Fourth Amendment,” id., as “[t]he package itself, which had
previously been opened, remained unsealed, and the Federal
Express employees had invited the agents to examine its
contents,” such that “the package could no longer support
any expectation of privacy,” id. at 121.

    Jacobsen then separately considered the chemical field
test, conducted by the DEA agents, including the federal
agents’ removal of the white powder from the plastic bag.
Critically for our purposes, Jacobsen began this inquiry from
the premise that because the field test “had not been
conducted by the Federal Express agents,” it “therefore
exceeded the scope of the private search.” Id. at 122
(emphasis added). The majority then determined that the
government’s chemical field test of the substance in the
properly seized plastic bags was nonetheless not a search
20                 UNITED STATES V. WILSON

within the meaning of the Fourth Amendment, because
“governmental conduct that can reveal whether a substance
is cocaine, and no other arguably ‘private’ fact, compromises
no legitimate privacy interest.” Id. at 122–23. This
conclusion, Jacobsen explained, was “dictated” by the
Court’s earlier decision in United States v. Place, 462 U.S.
696 (1983), “in which the Court held that subjecting luggage
to a ‘sniff test’ by a trained narcotics detection dog was not
a ‘search’ within the meaning of the Fourth Amendment.”
Jacobsen, 466 U.S. at 123.

     B. Application of the Private Search Exception to
        This Case

    The government bears the burden to prove Agent
Thompson’s warrantless search was justified by the private
search exception to the Fourth Amendment’s warrant
requirement. Before considering the private search
exception, Coolidge emphasized “the most basic
constitutional rule” in the Fourth Amendment arena:
warrantless searches are per se unreasonable, subject to few
exceptions that are “jealously and carefully drawn.”
403 U.S. at 454–55. Accordingly, “[t]he burden is on those
seeking the exemption.” Id. at 455 (quoting United States v.
Jeffers, 342 U.S. 48, 51 (1951)). The government has not
met its burden here.

    Both as to the information the government obtained and
the additional privacy interests implicated, the government’s
actions here exceed the limits of the private search exception
as delineated in Walter and Jacobsen and their progeny. 9

     Wilson opines that the private search exception to the Fourth
     9

Amendment should be overruled, and seeks to preserve that question for
any Supreme Court review of this case. As a court of appeals, we of
                    UNITED STATES V. WILSON                            21

First, the government search exceeded the scope of the
antecedent private search because it allowed the government
to learn new, critical information that it used first to obtain a
warrant and then to prosecute Wilson. Second, the
government search also expanded the scope of the
antecedent private search because the government agent
viewed Wilson’s email attachments even though no Google
employee—or other person—had done so, thereby


course cannot overrule Supreme Court cases. United States v. Weiland,
420 F.3d 1062, 1079 n.16 (9th Cir. 2005) (“[W]e are bound to follow a
controlling Supreme Court precedent until it is explicitly overruled by
that Court.”); accord Nunez-Reyes v. Holder, 646 F.3d 684, 692 (9th Cir.
2011). We do note that the private search doctrine rests directly on the
same precepts concerning the equivalence of private intrusions by
private parties and the government that underlie the so-called third-party
doctrine. See e.g., Smith v. Maryland, 442 U.S. 735, 744 (1979) (holding
that by “voluntarily” conveying to his telephone company the phone
numbers he dialed, the defendant forsook his reasonable expectation of
privacy in that information); United States v. Miller, 425 U.S. 435, 442
(1976) (holding the defendant lacked a reasonable expectation of privacy
in “information [he had] voluntarily conveyed to [his] bank[]” like
financial statements and deposit slips). In Jacobsen, the Supreme Court
reasoned that the private search exception follows from the premise,
underlying the third-party doctrine, that “when an individual reveals
private information to another, he assumes the risk that his confidant will
reveal that information to the authorities.” 466 U.S. at 117. In recent
years, however, the Court has refused to “mechanically apply[] the third-
party doctrine,” stressing that “the fact of ‘diminished privacy interests
does not mean that the Fourth Amendment falls out of the picture
entirely.’” Carpenter, 138 S. Ct. at 2219 (quoting Riley, 573 U.S. at 392);
see United States v. Jones, 565 U.S. 400, 417 (2012) (Sotomayor, J.,
concurring) (explaining that the third-party doctrine “is ill suited to the
digital age, in which people reveal a great deal of information about
themselves to third parties in the course of carrying out mundane tasks”);
Susan Freiwald & Stephen Wm. Smith, The Carpenter Chronicle: A
Near-Perfect Surveillance, 132 Harv. L. Rev. 205, 224 (2018) (noting
that Carpenter “significantly narrowed the [third-party] doctrine’s
scope”).
22              UNITED STATES V. WILSON

exceeding any earlier privacy intrusion. Moreover, on the
limited evidentiary record, the government has not
established that what a Google employee previously viewed
were exact duplicates of Wilson’s images. And, even if they
were duplicates, such viewing of others’ digital
communications would not have violated Wilson’s
expectation of privacy in his images, as Fourth Amendment
rights are personal.

       1. Additional Information

    The district court analogized Agent Thompson’s review
of Wilson’s email attachments to the government search in
Jacobsen, concluding that Agent Thompson’s search
allowed him to “learn nothing new,” because Google had
already classified the images as child pornography. Wilson,
2017 WL 2733879, at *10–11. The government similarly
argues on appeal that its official search did not
impermissibly expand the scope of the private search
because it “just confirmed what Google employees already
knew and could say.” Both the district court’s conclusion
and the governments’ argument misstate the record.

    The record indicates that Google does not keep a
repository of child pornography images, so no Google
employee could have shown the government the images it
believed to match Wilson’s. Nor does the record identify the
individual who viewed those images in the repository, so no
identified Google employee “knew and could say” what
those images showed. Instead, Google keeps a repository of
unique hash values corresponding to illicit images, and tags
each image with one of four generic labels. All Google
communicated to NCMEC in its CyberTip was that the four
images Wilson uploaded to his email account matched
images previously identified by some Google employee at
some time in the past as child pornography and classified as
                  UNITED STATES V. WILSON                         23

depicting a sex act involving a prepubescent minor (the “A1”
classification). 10 Based only on the barebones CyberTip,
Agent Thompson testified, he opened and reviewed each of
Wilson’s images to determine “whether or not it is a case
that . . . can be investigated” for violations of federal law.

    A detailed description of the images was then included
in the applications for search warrants. The gulf between
what Agent Thompson knew about Wilson’s images from
the CyberTip and what he subsequently learned is apparent
from those descriptions. In contrast to Google’s label of the
images just as “A1,” which the government did not mention
in the warrant application, the government learned the
following:

         1. 140005125216.jpg – This image depicts a
         young nude girl, approximately five (5) to
         nine (9) years of age, who is lying on her
         stomach with her face in the nude genital
         region of an older female who is seated with
         her legs spread. A second young girl,
         approximately five (5) to nine (9) years of
         age, is also visible in this image and she is
         partially nude with her vagina exposed.
         Google identified this image was uploaded
         on June 4, 2015, at 16:11:04 UTC.

         2. 140005183260.jpg – This image depicts a
         young nude girl, approximately five (5) to
         nine (9) years of age, who is lying on top of

    10
       Perhaps a Google employee could also have testified to details
about the company’s proprietary technology. But no such information
appears in the record, and the CyberTip did not convey any more
information than what is now included in the record.
24              UNITED STATES V. WILSON

       an older nude female, approximately
       eighteen years of age. Within this image the
       girl’s genital regions are pressed against one
       another and the older girl appears to be
       touching the face of the younger child with
       her tongue. Google identified this image was
       uploaded on June 4, 2015, at 16:11:21 UTC.

       3. 140005129034.jpg – This image depicts a
       partially nude young girl, approximately five
       (5) to nine (9) years of age, who is lying on
       her back with her legs spread and her vagina
       exposed. An older female is positioned in
       front of this girl’s exposed vagina in this
       image and the younger girl has her left hand
       on the vaginal/buttocks area of a second nude
       girl of similar age. Google identified this
       image was uploaded on June 4, 2015, at
       16:11:06 UTC.

       4. 1400052000787.jpg – This image depicts
       a wider angle view of the previously
       referenced images possessing file names
       140005125216.jpg and 140005129034.jpg as
       reported by Google.

Wilson, 2017 WL 2733879, at *4–5.

    Given the large gap between the information in the
CyberTip and the information the government obtained and
used to support the warrant application and to prosecute
Wilson, the government search in Walter offers a much more
apt comparison to the circumstances here than does the
government search in Jacobsen. Google’s categorization of
Wilson’s email attachments as “A1” functioned as a label for
                 UNITED STATES V. WILSON                    25

the images in the same way that the boxes describing the
films in Walter suggested that the images on the films were
obscene. The “A1” labels, in fact, provided less information
about the images’ contents than did the boxes in Walter,
which had “explicit descriptions of the contents” of the film.
447 U.S. at 652. The “A1” labels, in contrast, specified only
the general age of the child and the general nature of the acts
shown.

    Viewing Wilson’s email attachments—like viewing the
movie in Walter—substantively expanded the information
available to law enforcement far beyond what the label alone
conveyed, and was used to provide probable cause to search
further and to prosecute. The government learned at least
two things above and beyond the information conveyed by
the CyberTip by viewing Wilson’s images: First, Agent
Thompson learned exactly what the image showed. Second,
Agent Thompson learned the image was in fact child
pornography. Until he viewed the images, they were at most
“suspected” child pornography. Just as it “was clearly
necessary for the FBI to screen the films [in Walter], which
the private party had not done, in order to obtain the evidence
needed to accomplish its law enforcement objectives,”
Walter, 447 U.S. at 659 n.14 (plurality), so here, to prosecute
Wilson it was necessary for Agent Thompson to view the
images no Google employee had opened. Id. Until Agent
Thompson viewed Wilson’s images, no one involved in
enforcing the child pornography ban had seen them. Only by
viewing the images did the government confirm, and convey
to the fact finder in Wilson’s criminal case, that they
depicted child pornography under the applicable federal
standard.

    Importantly, the district court found—and we agree—
that if Agent Thompson’s affidavit in support of a warrant
26                 UNITED STATES V. WILSON

had been “excise[d]” of “the tainted evidence,” “the affidavit
would not support issuance of the search warrant for
Defendant’s email account.” Wilson, 2017 WL 2733879,
at *12. 11 The district court’s findings about the inadequacy
of the warrant application without the important information
Agent Thompson obtained by viewing Wilson’s images
demonstrate that the government learned new, critical
information by viewing Wilson’s images, information “not
previously . . . learned during the private search,” Jacobsen,
466 U.S. at 120. Because the government saw more from its
search than the private party had seen, it exceeded the scope
of the private search.

          2. Additional Intrusion on Wilson’s Privacy
             Interest

    The government also maintains that directly viewing
Wilson’s images for the first time was not a further invasion
of Wilson’s privacy, beyond any privacy invasion by
Google. The government’s expectation of privacy analysis
fails for much the same reason as did its argument that it
learned nothing new by viewing the images.

    The government’s central submission in this regard is
that Wilson’s expectation of privacy in his images was fully
frustrated when Google’s computer technology scanned
them, such that any further government search of the images




      We also agree with the district court that the government might
     11

have been able to demonstrate probable cause sufficient to obtain a
warrant without the descriptions of Wilson’s images, by presenting, for
example, more “information about Google’s screening process for child
pornography,” Wilson, 2017 WL 2733879, at *12.
                   UNITED STATES V. WILSON                          27

should be exempt from the Fourth Amendment’s warrant
requirement. 12 We cannot agree.

     Although Google’s proprietary technology labelled
Wilson’s email attachments as “A1,” “the content of the
[images] . . . was [no more] apparent” to Google than the
image content was to the private party in Walter, as no
Google employee had opened and viewed the attachments,
and Google does not appear to retain any record of the
original images used to generate hash matches. See Tosti,
733 F.3d at 823. Agent Thompson did not obtain a specific
description of the content of Wilson’s attachments from
Google, so he was not simply confirming what he had been
told. Until he viewed the images, he had no image at hand at
all; the entire composition was hidden. Only the image itself
could reveal, for example, the number of minors depicted,
their identity, the number of adults depicted alongside the
minors, the setting, and the actual sexual acts depicted.
Reading a label affixed to an image is a different experience
entirely from looking at the image itself. To read even a
detailed description, which this A1 classification was not, is
still not to see. Wilson’s privacy interest was in the actual
image—which could have included features in addition to
child pornography—not just in its classification as child
pornography.

   The government’s argument to the contrary
mischaracterizes the record, by representing that Google’s
scan “equates to a full-color, high-definition view” of
Wilson’s images. It does not. The critical fact is that no
Google employee viewed Wilson’s files before Agent

    12
       The government stated at oral argument that it is not relying on
the contraband nature of child pornography as a justification for the
search.
28               UNITED STATES V. WILSON

Thompson did. When the government views anything other
than the specific materials that a private party saw during the
course of a private search, the government search exceeds
the scope of the private search. That is the clear holding of
Jacobsen. In that case, “[t]he field test . . . had not been
conducted by the Federal Express agents and therefore
exceeded the scope of the private search.” 466 U.S. at 122
(emphasis added); see supra Part II.B.1.

       3. Personal Nature of the Fourth Amendment

    The government attempts to save its warrantless search
by shifting the analysis from the private search of Wilson’s
files, flagged by Google and classified as A1 by its
proprietary technology, to the private search of other
individuals’ files, which some Google employee previously
viewed and classified as child pornography in Google’s
database of hash values. The government argues that Agent
Thompson’s search did not exceed the bounds of the private
search because a Google employee had previously viewed
different child pornography files, and Google’s computers
flagged Wilson’s email attachments as containing the same
images as those files, using an unspecified hash value
comparison system. This line of argument cannot save the
validity of the government’s search. Even if Wilson’s email
attachments were precise duplicates of different files a
Google employee had earlier reviewed and categorized as
child pornography, both Walter and Jacobsen—and general
Fourth Amendment principles—instruct that we must
specifically focus on the extent of Google’s private search of
Wilson’s effects, not of other individuals’ belongings, to
assess whether “the additional invasions of [Wilson’s]
privacy by the government agent . . . exceeded the scope of
the private search.” Jacobsen, 466 U.S. at 115.
                 UNITED STATES V. WILSON                    29

    To see why, consider whether Walter would have come
out differently had the misdirected package come into the
hands of someone who had previously viewed another copy
of the same film and, recognizing the box, told the police
that the film in it was, in her view, legally obscene. Under
Walter, the government in the hypothesized circumstance
would still need a warrant to view the film in the box.
Viewing the copy of the film actually in the box, which the
mistaken recipient of the box had not done, would still entail
an additional governmental intrusion on both the physical
integrity of the film and the owner’s privacy interest in its
content.

     Fourth Amendment rights are personal rights. Rakas v.
Illinois, 439 U.S. 128 (1978), is illustrative: Rakas held that
a passenger could not challenge a police search as violative
of the Fourth Amendment because he owned neither the
vehicle that was searched nor the rifle found. Although the
owners of each item had an expectation of privacy, the
defendant did not. See id. at 134.

    So Wilson did not have an expectation of privacy in
other individuals’ files, even if their files were identical to
his files. The corollary of this principle must also be true:
Wilson did have an expectation of privacy in his files, even
if others had identical files. If, for example, police officers
search someone else’s house and find documents evidencing
wrongdoing along with notes indicating that I have identical
documents in my house, they cannot, without a warrant or
some distinct exception to the warrant requirement, seize my
copies. I would retain a personal expectation of privacy in
them, and in my connection to them, even if law enforcement
had a strong basis for anticipating what my copies would
contain. A violation of a third party’s privacy has no bearing
30               UNITED STATES V. WILSON

on my reasonable expectation of privacy in my own
documents. The government does not argue otherwise.

    In short, whether Google had previously reviewed, at
some earlier time, other individuals’ files is not pertinent to
whether a private search eroded Wilson’s expectation of
privacy. Under the private search doctrine, the Fourth
Amendment remains implicated “if the authorities use
information with respect to which the expectation of privacy
has not already been frustrated.” Jacobsen, 466 U.S. at 117
(emphasis added).

     C. Relevant Appellate Caselaw

    (i) Our application of Jacobsen and Walter is consistent
with Ninth Circuit case law. The district court misapplied
United States v. Tosti, 733 F.3d 816 (9th Cir. 2013), in
reaching the contrary conclusion.

    In Tosti, a private party entrusted with the defendant’s
computer found thumbnails of images believed to be child
pornography and alerted law enforcement officers. 733 F.3d
at 818–19. The private party showed the thumbnails to law
enforcement, and the agents “could tell from viewing the
thumbnails that the images contained child pornography.”
Id. at 822.

    Tosti held that law enforcement’s enlarging of the
thumbnails did not expand on the antecedent private search.
For one, based on the standard articulated in Jacobsen, “the
police learned nothing new through their actions.” Tosti,
733 F.3d at 822. Further, “scrolling through the images [the
private party] had already viewed was not a search because
any private interest in those images had been extinguished.”
Id.
                 UNITED STATES V. WILSON                    31

    Neither is true in this case. Here, what was conveyed to
Agent Thompson was that a not-yet-viewed image uploaded
by Wilson matched a different image that an unidentified
Google employee had previously viewed and classified as
child pornography. So until Agent Thompson actually
viewed the images, he knew only that Google’s propriety
technology had identified a match between Wilson’s images
and other images that Google had classified as child
pornography. He “learned . . . [a]new through [his] actions,”
for the first time, what the images actually showed. See
supra pp. 23–24. And, as no one at Google had previously
viewed Wilson’s attachments, “any privacy interest in those
images had [not] been extinguished.” Tosti, 733 F.3d at 822.
Google’s algorithm “frustrated [Wilson’s] [privacy]
expectation in part,” but it “did not . . . strip the remaining
unfrustrated portion of that expectation of all Fourth
Amendment protection.” Walter 447 U.S. at 659 (plurality);
see also Jacobsen, 466 U.S. at 116 n.11.

   For these reasons, Tosti is fully consistent with our
conclusion that Agent Thompson’s search exceeded the
scope of the private search and so required a warrant.

   (ii) In so holding, we contribute to a growing tension in
the circuits about the application of the private search
doctrine to the detection of child pornography.

    In United States v. Ackerman, 831 F.3d 1292, 1294 (10th
Cir. 2016), AOL automatically identified one of the
defendant’s four email attachments as apparent child
pornography, based on a hash value match. AOL then sent
the text of the defendant’s email and all four attachments to
NCMEC, where an analyst “opened the email, viewed each
of the attached images, and confirmed that all four [images]
(not just the one AOL’s automated filed identified) appeared
to be child pornography.” Id. Ackerman emphasized that
32              UNITED STATES V. WILSON

“AOL never opened the email itself. Only NCMEC did
that.” Id. at 1305–06. Then-Judge Gorsuch, after holding that
NCMEC is either a governmental entity or a government
agent, see id. at 1308, concluded that “in at least this way
[the government] exceeded rather than repeated AOL’s
private search,” id. at 1305–06.

    Ackerman did suggest that, had the government viewed
only the attachment AOL identified as a hash value match
and not other attachments and the text of the defendant’s
email, that distinction might “bring the government closer to
a successful invocation of the private search doctrine.” Id.
at 1308 (emphasis added). But Ackerman also noted that in
that circumstance—which appears to be what happened
here—the government’s action may still be a new search, as
the government, “might . . . have risked exposing new and
protected information, maybe because the hash value match
could have proven mistaken . . . or because the AOL
employee who identified the original image as child
pornography was mistaken in his assessment.” Id. at 1306.
Although Ackerman did not decide the precise issue before
us, and expressly disavowed “prejudg[ing]” it, id. at 1308–
09, its underlying analysis is entirely consistent with ours,
and its suggestions about why there could be a search in our
circumstances echo some of the reasons we have given for
so concluding.

    Other private search cases concerning the discovery of
child pornography, outside the context of automated hash
value matching, have also ruled consistently with our
understanding of the limited scope of the private search
exception. For example, in United States v. Lichtenberger,
786 F.3d 478 (6th Cir. 2015), the defendant’s girlfriend had
discovered child pornography on his computer. She later
showed his computer to the police and opened some
                    UNITED STATES V. WILSON                            33

computer files that were determined to contain child
pornography. But the defendant’s girlfriend was “not at all
sure whether she opened the same files with [the police] as
she had opened earlier that day.” Id. at 490. As a result, the
Sixth Circuit concluded that the government search
exceeded the scope of the private search. This reasoning
supports our result here. The record does not identify the
Google analyst who could have stated that the images Agent
Thompson viewed were identical to images the analyst
previously viewed, nor does it explain Google’s algorithm in
any detail. Given these gaps, there is no way to be “at all
sure” that the images Agent Thompson viewed were the
same images a Google analyst had earlier viewed, so the
government search exceeded the scope of Google’s search.

    Further, in United States v. Sparks, 806 F.3d 1323 (11th
Cir. 2015), overruled on other grounds by United States v.
Ross, 963 F.3d 1056 (11th Cir. 2020), a store employee and
her fiancé discovered child pornography on a lost cell phone
and showed the phone to the police. The police officer
ultimately viewed two videos on the cell phone, one of
which the private parties “had not watched.” Id. at 1332.
Because the government search exposed new information,
not seen by the private party, the Eleventh Circuit concluded
that the government search exceeded the scope of the private
search. 13


    13
       Both the Fifth Circuit and the Seventh Circuit have held that an
individual’s privacy interest in a digital container, such as an email
account, cell phone, or laptop, is entirely frustrated whenever any part of
the container is searched. See United States v. Runyan, 275 F.3d 449, 465
(5th Cir. 2001); Rann v. Atchison, 689 F.3d 832 (7th Cir. 2012). But this
approach is squarely contrary to the Ninth Circuit’s approach to digital
devices, has been undermined by more recent Supreme Court cases about
34                  UNITED STATES V. WILSON

    Conversely, the Fifth and Sixth Circuits recently decided
the issue before us and came to a conclusion contrary to the
one we reach, although the reasoning of the two opinions
diverged. The circumstances in both cases were similar to
those here. See United States v. Reddick, 900 F.3d 636 (5th
Cir. 2018); United States v. Miller, 982 F.3d 412, 427 (6th
Cir. 2020). In both cases, after an electronic service provider
flagged certain email attachments as apparent child
pornography, the attachments were forwarded to a local law
enforcement agency, whose officers viewed the images for
the first time without a warrant.

    The Fifth Circuit held the private search exception
justified the government’s warrantless search because the
government agent’s “visual review of the suspect images . . .

the scope of digital information, and is inconsistent with Jacobsen. For
starters, Tosti did not regard the viewing of some files as sufficient for
purposes of the private search doctrine to show that the government only
invaded a defendant’s privacy interests to the same extent as the private
party. See 733 F.3d at 822. More generally, and dispositively, the Ninth
Circuit has not treated digital devices as unitary, such that a permissible
search of one file or attachment justifies a search of a larger swatch of
digital material. See United States v. Cotterman, 709 F.3d 952 (9th Cir.
2013) (en banc); United States v. Cano, 934 F.3d 1002, 1007 (9th Cir.
2019). Further, Runyan and Rann are in tension with recent Supreme
Court cases, which express concern that given the “immense storage
capacity” of modern technology, the Fourth Amendment will be
undermined unless government searches of digital material are
meaningfully confined in accord with established Fourth Amendment
doctrine. Riley v. California, 573 U.S. 373, 393 (2014); see also
Carpenter v. United States, 138 S. Ct. 2206, 2214 (2018). Finally, if, in
Jacobsen, law enforcement officers had opened and searched not only
the specific containers investigated by the FedEx employees but others
included in the same box, the private search doctrine would not have
applied to the still-sealed containers. There is no basis for ruling
otherwise with regard to unopened digital files. Runyan and Rann were
in our view wrongly decided.
                 UNITED STATES V. WILSON                   35

was akin to the government agents’ decision to conduct
chemical tests on the white powder in Jacobsen,” insofar as
“opening the file merely confirmed that the flagged file was
indeed child pornography, as suspected.” Reddick, 900 F.3d
at 639.

    We cannot accept this analysis for several reasons. First,
and most important, Reddick conflates Jacobsen’s first
holding regarding the private search exception to the Fourth
Amendment with its second holding regarding whether the
field test constituted a search under the Fourth Amendment.
The private search exception excuses a warrantless
government search that would otherwise violate the Fourth
Amendment; the field test determination in Jacobsen, based
on Fourth Amendment law outside the private search
context, was that a warrantless government field drug test
simply does not trigger the Fourth Amendment’s
protections. 466 U.S. at 123–24. In other words, the
warrantless chemical test in Jacobsen was not excused via
the private search exception but for an entirely different
reason—that confirming through a field test that an already
exposed and seized contraband substance was a drug is not
a search for Fourth Amendment purposes. Id. at 122.

    Moreover, in Jacobsen, the white powder was fully
visible to the government officers when they repeated the
steps taken by the FedEx employees to inspect the package.
Not so here, as no human had viewed Wilson’s images
before. The part of Jacobsen that does elucidate the private
search doctrine cannot govern here.

   Notably, we have held that the chemical field test
exception to the Fourth Amendment’s warrant requirement
does not apply to a more complete chemical analysis of a
drug. In United States v. Mulder, 808 F.2d 1346 (9th Cir.
1987), a hotel security officer removed items left behind in
36               UNITED STATES V. WILSON

a hotel room after a guest’s scheduled departure, including
plastic bags full of tablets, and provided them to federal
agents. Id. at 1347. The tablets “were tested at the Western
Regional Laboratory through the use of mass spectrometry,
infrared spectroscopy and gas chromatography.” Id. at 1348.
Mulder distinguished between the chemical field test in
Jacobsen and a laboratory test: “[T]he chemical testing in
this case was not a field test which could merely disclose
whether or not the substance was a particular substance, but
was a series of tests designed to reveal the molecular
structure of a substance and indicate precisely what it is.
Because of the greater sophistication of these tests, they
could have revealed an arguably private fact,” and thus
compromised the defendant’s legitimate privacy interest. Id.
at 1348–49.

    To the extent opening an email attachment to view its
contents is analogous to drug testing at all, it is akin to a
laboratory test with the potential to reveal new private
information, as in Mulder, not a binary field test that yields
either a positive or negative result. Just as a laboratory test
of a suspected drug reveals its precise molecular structure
and so potentially exposes additional private information
like other illicit contaminants or the source of the substance,
so viewing an image of suspected child pornography reveals
innumerable granular private details—for example, the faces
of the people depicted, the setting, and, perhaps, other
speech or conduct also in the frame. Viewing the images
here allowed the government to do more than just confirm
the images’ classification as child pornography, implicating
privacy interests beyond a binary classification. Contrary to
Reddick, the government’s “visual review of the suspect
images” was not analogous to “the government agents’
decision to conduct chemical tests on the white powder in
Jacobsen.” 900 F.3d at 639 (emphasis added).
                 UNITED STATES V. WILSON                    37

    The Sixth Circuit recognized the error in Reddick
concerning the reach of the private search holding in
Jacobsen and “opt[ed] not to rely” on it. Miller, 982 F.3d
at 429. As Miller points out, the government agent’s
“inspection (unlike the [field] test) qualifies as the invasion
of a ‘legitimate privacy interest’ unless Google’s actions had
already frustrated the privacy interest in the files.” Id.

     Miller instead resolved the Fourth Amendment question
it faced by focusing exclusively on the assumed reliability of
Google’s proprietary technology. “At bottom,” Miller
explained, “this case turns on the question whether Google’s
hash-value matching is sufficiently reliable.” Id. at 429–30.
Because the defendant in Miller “never challenged the
reliability of hashing,” id. at 430 (internal brackets and
quotation omitted) (Miller thought the burden was on the
defendant, see id. at 430), Miller deferred to the district
court’s finding “that the technology was ‘highly reliable.’”
Id.

    Wilson, by contrast, did challenge the “accuracy and
reliability” of Google’s hashing technology in the district
court. And, contrary to Miller’s assertion, the government
bears the burden to prove its warrantless search was
permissible, see supra p. 20—a burden it failed to carry.

    Our analysis, however, relies only contingently on the
adequacy of the record with regard to the hash match
technology. In our view, the critical factors in the private
search analysis, both unacknowledged in Miller, include the
personal nature of Fourth Amendment rights and the breadth
of essential information Agent Thompson obtained by
opening the attachment, information—and a privacy
invasion—well beyond what Google communicated to
NCMEC. See supra Parts II.B.1, II.B.2. The reliability of
Google’s proprietary technology, in our estimation, is
38              UNITED STATES V. WILSON

pertinent to whether probable cause could be shown to
obtain a warrant, not to whether the private search doctrine
precludes the need for the warrant.

    And, as the district court noted, and we have noted as
well, the warrant application here contained inadequate
information about Google’s proprietary technology to
establish probable cause without reliance on the descriptions
of the actual images. See supra p. 25.

III.   Conclusion

    “When confronting new concerns wrought by digital
technology, this Court has been careful not to uncritically
extend existing precedents.” Carpenter, 138 S. Ct. at 2222.
The government reports there were 18.4 million CyberTips
in 2018, making it all the more important that we take care
that the automated scanning of email, and the automated
reporting of suspected illegal content, not undermine
individuals’ Fourth Amendment protections.

    Having examined this case with the requisite care, we
hold, for the reasons explained, that Agent Thompson
violated Wilson’s Fourth Amendment right to be free from
unreasonable searches when he examined Wilson’s email
attachments without a warrant. Wilson’s conviction is
vacated, the district court’s denial of Wilson’s motion to
                   UNITED STATES V. WILSON                         39

suppress is reversed, and this case is remanded for further
proceedings. 14




    14
       As noted, the district court concluded that if Agent Thompson’s
warrantless actions constituted an illegal search, no exception “would
prevent operation of the exclusionary rule.” Wilson, 2017 WL 2733879,
at *13. The government did not raise before us any argument to the
contrary, and thus waived any challenge. See United States v. Gamboa-
Cardenas, 508 F.3d 491, 502 (9th Cir. 2007).

```

---

## GROUP: _overhaul2/lake/cases/United States v. Xiang.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Xiang
type: case
citation: "67 F.4th 895 (2023)"
parallel_cite: ""
neutral_cite: ""
court: 8th Cir. 2023
court_level: coa
circuit: ca8
year: 2023
date_decided: 2023-05-05
docket: 22-1801
authority_weight: "Binding in-circuit — 8th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/9397097/united-states-v-haitao-xiang/"
  cluster_id: 9397097
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Xiang
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Border Searches]]"
    role: Key
related:
  - "[[Border Searches]]"
  - "[[United States v. Kolsuz]]"
  - "[[Riley v. California]]"
  - "[[United States v. Flores-Montano]]"
tags:
  - case
  - fourth-amendment
  - border-search
  - outbound-search
  - forensic-search
  - electronic-devices
  - economic-espionage
  - eighth-circuit
holding: "The border-search exception applies with equal force to travelers and objects leaving the country, so CBP's warrantless seizure and forensic examination of Haitao Xiang's electronic devices as he departed for China fell within the exception; the court adopted the consensus that a non-routine forensic device search requires reasonable, individualized suspicion but not a warrant or probable cause, and held the officers had reasonable suspicion here, so it affirmed the denial of suppression."
aliases:
  - United States v. Xiang
  - "United States v. Xiang (8th Cir. 2023)"
---

# United States v. Xiang

*67 F.4th 895 (8th Cir. 2023)* (No. 22-1801) · U.S. Court of Appeals for the Eighth Circuit · **Binding in-circuit — 8th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 9397097 → lead opinion 9392573 (Loken, J.; 67 F.4th 895, decided 2023-05-05); Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — CL text is slip-paginated). S9 promotes. -->

## Background
Haitao Xiang, a Chinese citizen who worked for Monsanto in St. Louis, was suspected of stealing a proprietary agricultural algorithm. The day after his company exit interview, he boarded a one-way flight from Chicago's O'Hare International Airport bound for Shanghai, without his family. Alerted by the FBI and Monsanto, U.S. Customs and Border Protection conducted an interview and initial border inspection at O'Hare and seized his cell phone, laptop, SD card, and SIM card as he was leaving the country. The devices were sent to St. Louis, where an FBI Computer Analysis Response Team created forensic images and examined them. Xiang was convicted of economic espionage under 18 U.S.C. § 1831 and moved to suppress the device evidence; the district court, applying the border-search exception, found reasonable suspicion supported the non-routine forensic searches.

## Issue
Whether the warrantless seizure and forensic search of a departing traveler's electronic devices falls within the Fourth Amendment's border-search exception, and if so, whether the officers needed — and had — the requisite suspicion.

## Rule
The border-search exception permits routine searches and seizures at the border without a warrant or probable cause, and — critically here — it "applies with equal force to persons or objects leaving the country," not just those entering. Distinguishing routine from non-routine searches, the Eighth Circuit adopted the cross-circuit consensus that a forensic or "advanced" device search is non-routine and requires reasonable, individualized suspicion (though not probable cause or a warrant): "We think it is an appropriate standard, particularly given the heightened personal privacy interest in electronic devices recognized in Riley." — 67 F.4th 895, slip op. at 8. ^pin-op8

## Application
The court had little difficulty concluding that CBP's seizure and forensic examination of the devices Xiang was carrying abroad was a "border search," rejecting his argument that *[[Riley v. California|Riley]]* — a search-incident-to-arrest case — required a warrant to open electronic devices at a port of entry. It also rejected the contention that the search was untethered to border-search justifications: protecting the nation's economic and trade-secret interests is a legitimate border objective, and the border-search power reaches evidence of crime. The court did not have to decide categorically whether reasonable suspicion is always required for a forensic device search, because it agreed with the district court that the officers had reasonable suspicion — Xiang's abrupt one-way departure, his suspicious searches, his extreme nervousness, and his signed trade-secret obligations supplied particularized, objective facts. The denial of suppression was therefore correct.

## Conclusion
**Affirmed.** Judge Loken wrote for the panel (Smith, C.J., Wollman, and Loken, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Xiang* is a useful **outbound**-border-search anchor: the border-search exception protects departures as well as arrivals, and a forensic examination of seized electronic devices is a **non-routine** border search calling for reasonable suspicion. Like the Fourth Circuit's *[[United States v. Kolsuz|Kolsuz]]*, the court reserved whether reasonable suspicion is strictly *required* for forensic device searches, resolving the case on the ground that suspicion was present. Teach the routine/non-routine line and note the unresolved circuit split on the precise standard for forensic device searches.

## Appears on
- [[Border Searches]] — *Key*

## Sources
- [*United States v. Xiang*, 67 F.4th 895 (8th Cir. 2023)](https://www.courtlistener.com/opinion/9397097/united-states-v-haitao-xiang/) — pinpoint: slip op. at 8 (adopting the reasonable-suspicion standard for non-routine forensic border searches of electronic devices; the CL opinion text carries slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6b96eb682674a068", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Xiang"}, "payload": {"all": [{"cite": "67 F.4th 895", "page": "895", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "67"}], "display": "67 F.4th 895", "official": {"cite": "67 F.4th 895", "page": "895", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "67"}, "official_selection_present": true, "record_id": "United States v. Xiang"}}
{"assertion_id": "0bca214bfdeb2d84", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Xiang"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Xiang", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Xiang

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Xiang",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Haitao Xiang",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Xiang",
    "court": "8th Cir. 2023",
    "court_id": "ca8",
    "court_level": "coa",
    "circuit": "ca8",
    "state": null,
    "date_decided": "2023-05-05",
    "year": 2023,
    "docket": "22-1801",
    "cluster_id": 9397097,
    "lead_opinion_id": 9392573,
    "sibling_ids": [],
    "absolute_url": "/opinion/9397097/united-states-v-haitao-xiang/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "67 F.4th 895",
      "volume": "67",
      "reporter": "F.4th",
      "page": "895",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "67 F.4th 895",
        "volume": "67",
        "reporter": "F.4th",
        "page": "895",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "67 F.4th 895",
    "official_selection": {
      "court_class": "state",
      "selected": "67 F.4th 895",
      "reason": "selected_rank_3"
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
    "date_created": "2026-07-06T06:01:10Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T06:01:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T06:01:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T06:01:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T06:01:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-xiang--9397097",
      "to_record_id": "United States v. Xiang",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Xiang

```
               United States Court of Appeals
                          For the Eighth Circuit
                      ___________________________

                              No. 22-1801
                      ___________________________

                           United States of America

                      lllllllllllllllllllllPlaintiff - Appellee

                                         v.

                                  Haitao Xiang

                    lllllllllllllllllllllDefendant - Appellant

                           ------------------------------

       Electronic Frontier Foundation; American Civil Liberties Union;
          Knight First Amendment Institute at Columbia University;
                Reporters Committee for Freedom of the Press

                 lllllllllllllllllllllAmici on Behalf of Appellant
                                      ____________

                  Appeal from United States District Court
                for the Eastern District of Missouri - St. Louis
                                ____________

                         Submitted: January 12, 2023
                            Filed: May 5, 2023
                              ____________

Before SMITH, Chief Judge, WOLLMAN and LOKEN, Circuit Judges.
                             ____________
LOKEN, Circuit Judge.

      “Congress, since the beginning of our Government, has granted the Executive
plenary authority to conduct routine searches and seizures at the border, without
probable cause or a warrant, in order to regulate the collection of duties and to
prevent the introduction of contraband into this country.” United States v. Flores-
Montano, 541 U.S. 149, 153 (2004) (quotation omitted). “[T]he rationale behind this
[border search] exception [to the Fourth Amendment’s warrant requirement] applies
with equal force to persons or objects leaving the country.” United States v. Udofot,
711 F.2d 831, 839 (8th Cir. 1983).

       Haitao Xiang, a citizen of the People’s Republic of China and long-time
resident of the United States, conditionally pleaded guilty to conspiracy to commit
economic espionage in violation of 18 U.S.C. §§ 1831(a)(5).1 He appeals the
conviction and sentence. The principal issue is whether the district court2 erred in
denying Xiang’s motion to suppress evidence obtained by a warrantless seizure and
forensic search of Xiang’s digital devices as he was leaving Chicago’s O’Hare
International Airport, with Shanghai, China his final destination. Applying the
Fourth Amendment border search exception, the district court concluded that U.S.
Customs and Border Protection (“CBP”) officers had reasonable suspicion to conduct
non-routine forensic searches of Xiang’s electronic devices and acted reasonably in
doing so. We agree. We also conclude that Xiang waived his appeal of the $150,000
fine the district court imposed as part of his sentence. Accordingly, we affirm.


      1
        As relevant, the statute is violated by “[w]hoever, intending or knowing that
the offense will benefit any foreign government, foreign instrumentality, or foreign
agent, knowingly” conspires to “steal[], or without authorization . . . carr[y] away . . .
a trade secret.”
      2
        The Honorable Henry E. Autrey, United States District Judge for the Eastern
District of Missouri, adopting the Report and Recommendation of the Honorable John
M. Bodenhausen, United States Magistrate Judge for the Eastern District of Missouri.

                                           -2-
                                  I. Background

       From September 2008 to June 2017, Xiang was employed as an Advanced
Imaging Scientist with Monsanto Co., headquartered in St. Louis, Missouri. On May
25, 2017, Xiang tendered his resignation. On June 5 and June 8, Anne Luther, a
Senior Investigator for Monsanto’s Global Security Team, met with FBI Special
Agent Jaret Depke, who was then assigned to the Foreign Counterintelligence Squad
and was an officer with the Joint Terrorism Task Force at the FBI office in St. Louis.
Luther advised Agent Depke that Xiang was a senior research application engineer
who had been on Monsanto Security’s radar in 2008 for misrepresenting himself as
a University of Illinois student while attempting to acquire information about
hyperspectral imaging technology; that Xiang had submitted his resignation; and that
an exit interview was scheduled for June 9. Depke also talked to others at Monsanto.
He learned that Xiang had “conducted some suspicious Google searches” that
suggested a plan to send company documents to a third party; “sent packets of
information” to a Chinese competitor called NERCITA; and “sent confidential
Monsanto information from his work email to his personal email.” Xiang was also
known to be an associate of a former Monsanto employee named Jiunnren Chen, who
the FBI investigated after he took a job with China National Seed, a Monsanto
competitor; downloaded documents containing trade secrets; and sent emails
containing confidential information from his work account to a personal account.
Xiang was telling people that he planned to work for a potential Monsanto competitor
called Ag-Sensus, a remote-sensing agriculture start-up company with Lei Tian, his
former PhD advisor at the University of Illinois. Agent Depke considered this a
national security investigation involving potential theft of trade secrets.

      On June 8, following his second meeting with Luther, Depke contacted CBP
Officer Art Beck, a fellow member of the Joint Terrorism Task Force and the
Counterintelligence Squad, to discuss what Depke learned from his Monsanto
contacts. Beck ran a check on Xiang, learning he was married with one child residing

                                         -3-
in St. Louis. A travel notification told Beck that Xiang planned to travel to Shanghai
on a one-way ticket without his family on June 10th, the day after his exit interview.
Beck considered this information and the fact that Xiang was leaving Monsanto to
work for a start-up company to be suspicious “red flags.” He decided to subject
Xiang to a CBP inspection at O’Hare Airport on June 10 and advised Agent Depke
of CBP’s inspection, interview, and border search capabilities.3 Beck put in a CBP
“Record Lookout” alerting O’Hare officials that a secondary inspection of electronic
devices might be needed, based on national security concerns such as theft of trade
secrets. See Directive 3340-049, § 5.3, Detention and Review in Continuation of
Border Search of Information. Because the port of entry decides whether to inspect,
Beck advised CBP Officer Swiatek in Chicago of the reasons for Beck’s suspicions
(“the articulables,” as he described them at the suppression hearing).

       After Xiang’s June 9 exit interview, Monsanto personnel told Agent Depke that
Xiang was “extremely nervous” and “sweating” when asked about the suspicious
Google searches. Luther gave Depke a copy of Xiang’s signed termination in which
he agreed he would have no devices, records, data, notes, etc. in his possession that
belonged to Monsanto and would not share confidential information with any third
parties. Monsanto personnel described Xiang as extremely nervous while reviewing


      3
        See CBP Directive 3340-049, Border Searches of Electronic Devices
Containing Information, § 5.1, Border Searches (Aug. 20, 2009). This Directive was
in effect when Xiang’s devices were searched in 2017. CBP issued Directive 3340-
049A in January 2018, which superseded Directive 3340-049. Section 5.1.4 of the
later Directive expressly provides that “an Officer may perform an advanced search
of an electronic device,” which includes forensic searches, if “there is reasonable
suspicion of activity in violation of the laws enforced or administered by CBP, or in
which there is a national security concern.” Directive 3340-049 did not address this
issue. The government has argued to many of our sister circuits that reasonable
suspicion is not required, with mixed results. Our decision in this case is consistent
with the current Directive. We need not decide whether reasonable suspicion was
required under the prior Directive, on which there is circuit conflict.

                                         -4-
those provisions and assessed him as “blatantly deceptive.” Monsanto provided
Depke a copy of Xiang’s “suspicious Google searches” that included searches for
“company information to the third party,” “I don’t want it to be an evidence,” and “as
evidence to accuse me.”

      Xiang rented a car in St. Louis on June 9 and drove to Chicago. At O’Hare on
June 10, CBP Agents conducted an interview and initial border search of Xiang’s
checked and carry-on baggage prior to his flight. Based on the interview and prior
information, CBP seized a cell phone, laptop computer, SD card, and a SIM card from
Xian’s baggage for a secondary inspection. Xiang boarded his flight and left. Officer
Swiatek took custody of the seized devices and advised Officer Beck of the seizure.
Beck alerted FBI Agent Depke. Because Monsanto’s trade secret personnel are in St.
Louis and Depke had an established relationship with Monsanto, Depke had “a better
chance of quickly and expediently identifying anything that would be of interest or
potentially identified as that company’s trade secrets.” Therefore, exercising
Chicago’s extended CBP border search authority, Beck had the devices sent to St.
Louis for “subject matter expertise review” by an assisting federal agency. See
Directive 3340-049, § 5.3.2.3.

       Depke received the devices on June 13. The FBI Chief Division Counsel
confirmed that Depke could, within the authority of CBP, review the electronic
devices. The devices were opened and examined by a Computer Analysis Response
Team (“CART”) on June 14, 2017. CART created forensic images, and Depke began
a preliminary search on June 20. He identified six documents believed to be
Monsanto trade secrets or intellectual property, which Monsanto confirmed that day
or on June 21. At that point, CBP transferred its seizing authority to the FBI. See
Directive 3340-049, § 5.4.2.3. On July 27, the FBI applied for and obtained a warrant
to search the electronic devices.




                                         -5-
                           II. Motion to Suppress Issues

       After the district court denied his motion to suppress, Xiang entered a
conditional plea of guilty, reserving the right to appeal that ruling. See Fed. R. Crim.
P. 11(a)(2). When reviewing the denial of a motion to suppress, we review findings
of fact for clear error and conclusions of law de novo. See United States v. Taylor,
519 F.3d 832, 833 (8th Cir. 2008) (standard of review).

       A. Xiang’s primary argument on appeal is that the government needed a
warrant to search his electronic devices “because the forensic search did not fall
within the Fourth Amendment border search exception,” and therefore the general
rule applies that, “[i]n the absence of a warrant, a search is reasonable only if it falls
within a specific exception to the warrant requirement.” See Riley v. California, 573
U.S. 373, 382 (2014). As the opening paragraph of this opinion hopefully makes
clear, it blinks at reality to assert that CBP’s seizure and search of the electronic
devices Xiang was about to carry abroad was not a “border search” of the type
conducted by the Executive throughout our nation’s history. Xiang’s argument is that
“electronic devices are different,” as the Supreme Court recognized in Riley, and
therefore the government must get a warrant to even open them up at a port of entry,
when all other property is subject to “routine searches and seizures at the border,
without probable cause or a warrant.” Flores-Montano, 541 U.S. at 153. Riley
involved a different Fourth Amendment exception, searches incident to arrest. No
Circuit has held that the government must obtain a warrant to conduct a routine
border search of electronic devices. The First Circuit carefully explained why
Xiang’s broad argument “rests on a misapprehension of the applicability” of Riley.
Alasaad v. Mayorkas, 988 F.3d 8, 16-19 (1st Cir. 2021); see United States v.
Wanjiku, 919 F.3d 472, 484-85 (7th Cir. 2019). We agree.

      Xiang further argues that the search of his electronic devices was outside the
scope of the border search exception because it was “not tethered to any border search

                                           -6-
justifications.” The Ninth Circuit has stated that “[a] border search must be
conducted to enforce importation laws, and not for general law enforcement
purposes.” United States v. Cano, 934 F.3d 1002, 1013 (9th Cir. 2019) (quotation
omitted); see United States v. Aigbekaen, 943 F.3d 713, 721 (4th Cir. 2019).
Conversely, the Second Circuit has stated, more sensibly in our view, that CBP
officers “have the authority to search and review a traveler’s documents and other
items at the border when they reasonably suspect that the traveler is engaged in
criminal activity, even if the crime falls outside the primary scope of their official
duties.” United States v. Levy, 803 F.3d 120, 124 (2d Cir. 2015). But regardless of
whether there is any limitation on using border searches “to investigate general
criminal wrongdoing,” the assertion that the search of Xiang’s electronic devices was
“not tethered to any border search justifications” is absurd. Congress passed the
Economic Espionage Act of 1996 because:

      There can be no question that the development of proprietary economic
      information is an integral part of America’s economic well-being.
      Moreover, the nation’s economic interests are a part of its national
      security interests. Thus, threats to the nation’s economic interest are
      threats to the nation’s vital security interests.

H.R. Rep. No. 104-788, at 4 (1996), as reprinted in 1996 U.S.C.C.A.N. 4021, 4023;
see United States v. Hsu, 155 F.3d 189, 194-95 (3d Cir. 1998).

       Xiang’s additional assertion that the Fourth Amendment does not permit border
searches for mere evidence of criminal activity was rejected by the Supreme Court
over fifty years ago, see Warden v. Hayden, 387 U.S. 294, 300-02 (1967), and more
recently by circuit courts in this context, see Alasaad, 988 F.3d at 20.

       The real issue in this case is not whether the border search exception applies,
but whether the extended border search conducted by CBP officers, with technical
assistance from the FBI and Monsanto, is consistent with the Fourth Amendment’s

                                         -7-
overriding purpose to protect “against unreasonable searches and seizures.” In
United States v. Montoya de Hernandez, the Supreme Court held that when a routine
border search becomes non-routine -- in that case, the 16-hour detention of an
arriving traveler -- “customs agents, considering all the facts surrounding the traveler
and her trip, [must] reasonably suspect that the traveler is smuggling contraband in
her alimentary canal.” 473 U.S. 531, 541 (1985).

       Many of our sister circuits have distinguished between “routine” and “non-
routine” border searches of electronic devices. Most have concluded that a seizure
at the port of entry, followed by a forensic or “advanced” search, particularly if time
consuming and conducted away from the port of entry, becomes a non-routine border
searches requiring some level of reasonable, individualized suspicion, but not
probable cause or a warrant.4 As discussed, see note 3 supra, Directive 3340-049A
adopted this fact-intensive approach. We think it is an appropriate standard,
particularly given the heightened personal privacy interest in electronic devices
recognized in Riley. But like the Seventh Circuit in Wanjiku, we need not decide
today whether reasonable suspicion is required for an advanced or forensic border
search of electronic devices because we agree with the district court that CBP officers
had reasonable suspicion for the forensic search they conducted.

       B. Xiang argues that, if the border search exception does apply, the CBP
officers lacked the requisite reasonable suspicion. “Reasonable suspicion exists when
an officer is aware of particularized, objective facts which, taken together with


      4
        Compare Alasaad, 988 F.3d at 13 (1st Cir. 2021); United States v. Kolsuz, 890
F.3d 133, 144 (4th Cir. 2018); and United States v. Cotterman, 709 F.3d 952, 967-68
(9th Cir. 2013) (en banc), with United States v. Touset, 890 F.3d 1227, 1233 (11th
Cir. 2018) (reasonable suspicion not required for personal property including
electronic devices), and Wanjiku, 919 F.3d at 489 (7th Cir. 2019) (declining to reach
the issue).


                                          -8-
rational inferences from those facts, reasonably warrant suspicion that a crime is
being committed.” United States v. Tamayo-Baez, 820 F.3d 308, 312 (8th Cir. 2016)
(quotation omitted). We must review “the totality of the circumstances of each case
to see whether the detaining officer has a particularized and objective basis for
suspecting legal wrongdoing.” United States v. Arvizu, 534 U.S. 266, 273 (2002)
(quotation omitted).

      When CBP Officers seized Xiang’s devices at O’Hare Airport, officers were
aware of the following information: Xiang resigned from his position as a Monsanto
imaging scientist the day before; he was leaving the country without his family on a
one-way trip to China and then planned to work for an agricultural start-up company;
Monsanto personnel were concerned about Xiang stealing trade secrets -- he had
conducted suspicious Google searches and was visibly nervous when asked about the
searches during his exit interview; he had transferred unknown company information
from his company email account to a personal email account and appeared nervous
and deceptive when signing a termination contract that barred him from sharing
Monsanto trade secrets and confidential information with others; previously, Xiang
associated with a former colleague who downloaded and transmitted confidential
Monsanto documents to a personal email account before leaving to work for a
Chinese competitor; Xiang had sent packets of unknown information to a Chinese
competitor, NERCITA; and Monsanto’s security team believed that Xiang, as a new
Monsanto employee in 2008, misrepresented himself as a University of Illinois
student in an attempt to acquire information about an imaging company named
SpecTIR.

       Xiang argues that this gave CBP officers no reasonable suspicion he was
engaged in even a violation of company policy, much less economic espionage or
criminal theft of trade secrets. They did not know what “packets of information” he
sent to NERCITA. Sending emails from his work account to a personal account does
not point to criminal activity. There was no evidence he was involved in coworker

                                        -9-
Chen’s wrongdoing. The Google searches were stale evidence -- over a year prior to
the seizure of his electronic devices. Resigning and traveling to visit his family in
China are not indicative of any criminal wrongdoing. The agents’ “background” on
the “trend” of Chinese trade are “profiling” that provides little to no value, nothing
more than “unparticularized suspicion or hunch.”

       We agree with the district court that this argument is contrary to well-
established Fourth Amendment principles. “The totality-of-the-circumstances test
precludes this sort of divide-and-conquer analysis.” United States v. Quinn, 812 F.3d
694, 698 (8th Cir. 2016) (quotation omitted). Even though “each of these
[suspicious] factors alone is susceptible of innocent explanation, and some factors are
more probative than others[,] . . . together . . . they sufficed to form a particularized
and objective basis.” Arvizu, 534 U.S. at 277. The officers and agents had
background information, much of it corroborated, that provided a basis for assessing
Xiang’s actions in May and June 2017. Their experience and training in international
economic espionage and theft of trade secrets gave them reasonable suspicion for an
extended border search that included a forensic search of electronic devices.

       C. Finally, Xiang argues the search of his devices was constitutionally
unreasonable because it was akin to an “invasive rummage,” violated CBP policies,
was unreasonable in duration, and CBP calling on the FBI for subject matter expertise
was pretextual. These contentions require little discussion. The “rummaging” cases
on which Xiang relies -- Kremen v. United States, 353 U.S. 346, 347-48 (1957) and
Go-Bart Importing Co. v. United States, 282 U.S. 344, 358 (1931) -- bear no
resemblance to the focused search of electronic devices in this case. If law
enforcement officers have reasonable suspicion to search a container, such as a
backpack, briefcase, or electronic device, they have not conducted an unconstitutional
“rummaging” if they find the contraband at issue at the bottom of the backpack,
underneath lots of innocent items they did not seize or further search. As presented,
the argument is frivolous.

                                          -10-
       Xiang’s other arguments are likewise without merit. We agree with the district
court that “exclusion based on a failure to follow regulatory procedure is only
warranted if (1) the procedure is mandated by the Constitution or (2) the defendants
reasonably relied on the procedure in governing his conduct.” United States v. Xiang,
No. 4:19CR980, 2021 WL 4810556 at *3 (E.D. Mo. Oct. 15, 2021), citing United
States v. Caceres, 440 U.S. 741, 749-53 (1979). There was no such showing here.
Xiang’s argument that the CBP search was “a pre-textual search . . . to gather
evidence for SA Depke’s investigation” disregards Officer Beck’s credited testimony
that his actions were taken in exercise of CBP border search authority; the express
authorization for interagency cooperation and sharing of information in Directive
3340-049, § 5.4; and the common sense reality that there is nothing “pretextual”
about members of an interagency Counterintelligence Squad working together to
ferret out economic espionage and international trade secret theft that violates 18
U.S.C. § 1831(a).

       Finally, as we have explained, the record demonstrates why, after Xiang’s
devices were retained for extended inspection, it took time to send the devices to St.
Louis, where FBI Agent Depke could most efficiently conduct the search, and
Monsanto’s trade secrets security professionals could then confirm that the devices
contained trade secrets and proprietary information. During the interim, neither
Xiang nor anyone acting on his behalf asked that the devices be returned, or even
inquired about them. Thus, the extended seizure “did not meaningfully interfere with
his possessory interests,” United States v. Clutter, 674 F.3d 980, 984 (8th Cir.), cert.
denied, 133 S. Ct. 272 (2012), and CBP was obligated to “appropriately safeguard
information retained, copied, or seized under this Directive and during transmission
to another federal agency.” Directive 3340-049, § 5.4.1.5. The search was not
constitutionally unreasonable.




                                         -11-
                             III. Imposition of a Fine

       In his plea agreement, Xiang “waive[d] all rights to appeal all sentencing
issues” except for those explicitly preserved -- the district court’s determination of
the applicable guidelines and Xiang’s criminal history and the substantive
reasonableness of any sentence above the guidelines sentencing or fine range.
Xiang’s PSR stated that he has “the ability to pay a fine” and calculated his advisory
guidelines range as 10-16 months imprisonment, one to three years supervised
release, and a fine of $55,000.00 to $5,000,000.00. At sentencing, Xiang renewed his
objection to the PSR’s restitution recommendation. The district court imposed an
above-range sentence of twenty-nine months’ imprisonment, imposed a $150,000
fine, and held “in abeyance its judgment on restitution.” Xiang did not object to the
fine.

       Xiang appeals imposition of the $150,000 fine, arguing “the district court made
no factual findings.” He does not challenge the substantive reasonableness of the
fine, only the imposition of a fine without factual findings. This is an alleged
procedural error he waived in his plea agreement. Moreover, as he did not object at
sentencing, the challenge is not only waived but forfeited and may only be reviewed
for plain error. See United States v. Wohlman, 651 F.3d 878, 886 (8th Cir. 2011).
The district court did not err, much less plainly err in imposing a $150,000 fine.

      The judgment of the district court is affirmed.
                     ______________________________




                                        -12-

```

---

## GROUP: _overhaul2/lake/cases/United States v. Young.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Young
type: case
citation: "964 F.3d 938 (2020)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, 10th Cir."
court_level: coa
circuit: ca10
year: 2020
date_decided: 2020-07-07
docket: 18-6221
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
  opinion_url: "https://www.courtlistener.com/opinion/4766220/united-states-v-young/"
  cluster_id: 4766220
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Young
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: Key
related:
  - "[[Due-Process Voluntariness of Confessions]]"
  - "[[Colorado v. Connelly]]"
  - "[[Miranda v. Arizona]]"
tags:
  - case
  - fifth-amendment
  - due-process
  - voluntariness
  - coerced-confession
  - police-deception
  - promises-of-leniency
  - tenth-circuit
holding: "A confession is involuntary under the Due Process Clause when, under the totality of the circumstances, the defendant's capacity for self-determination is critically impaired by coercive police conduct; where an agent materially misrepresented the sentence the defendant faced, falsely promised to speak to a federal judge about his cooperation, and dangled leniency, and the defendant's ordinary personal characteristics could not withstand that pressure, the resulting confession was involuntary and had to be suppressed."
aliases:
  - United States v. Young
  - "United States v. Young (10th Cir. 2020)"
---

# United States v. Young

*964 F.3d 938 (10th Cir. 2020)* (No. 18-6221) · U.S. Court of Appeals for the Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4766220 → lead opinion 4546567 (964 F.3d 938, decided 2020-07-07); Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — CL text is slip-paginated). S9 promotes. -->

## Background
During a custodial interrogation, federal Agent Brown obtained a confession from Young. The district court found — and the government did not challenge on appeal — that Brown made false representations to Young about the sentence he faced, misstating how the drug quantity would drive his exposure; falsely told Young he would speak to a federal judge about Young's cooperation and how Young could "buy down" his sentence; and made promises of leniency. Young, who was forty-three years old with a GED and only prior state-system experience, was visibly shocked to learn he faced federal charges. He confessed, and the district court admitted the statements.

## Issue
Whether Young's confession was voluntary under the Due Process Clause, given the interrogating agent's misrepresentations of the sentence and false promises of leniency.

## Rule
Voluntariness is judged under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], and a confession must be suppressed when coercive government conduct overbears the suspect's will; an officer's material misrepresentation of the penalties a suspect faces, coupled with false promises of leniency, weighs heavily toward coercion. Applying that standard, the court held: "Under the totality of the circumstances, we conclude that Young's capacity for self-determination was critically impaired, rendering his confession involuntary." — 964 F.3d 938, slip op. at 15. ^pin-op15

## Application
The court first agreed that Agent Brown's conduct was coercive: misrepresenting the sentence Young faced, falsely promising to intercede with a federal judge, and offering leniency were the kind of deceptions that render a confession involuntary. It then asked whether Young's personal characteristics let him withstand that coercion, and found they did not — he was of ordinary age and education, showed no unusual resilience, and his prior experience was confined to the state system, doing nothing to inoculate him against a federal officer's misrepresentations about federal exposure and cooperation. Weighing the coercive conduct against Young's characteristics under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], the court concluded his will was overborne and his confession was not the product of a rational, free choice.

## Conclusion
The Tenth Circuit **reversed** the district court, **[[Reading and Citing Cases#vacated|vacated]]** the judgment against Young, and **[[Reading and Citing Cases#on-remand|remanded]]** for further proceedings, holding the confession involuntary.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Young* is a clean modern **due-process voluntariness** application: it is not a *[[Miranda v. Arizona|Miranda]]* case but a coercion case, holding that an officer's **misrepresentation of sentencing exposure** plus **false promises of leniency** can overbear an ordinary suspect's will. Read against *[[Colorado v. Connelly|Connelly]]*'s requirement of state action / coercive police conduct, *Young* illustrates the totality inquiry when the coercion is psychological rather than physical.

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key*

## Sources
- [*United States v. Young*, 964 F.3d 938 (10th Cir. 2020)](https://www.courtlistener.com/opinion/4766220/united-states-v-young/) — pinpoint: slip op. at 15 (confession involuntary under the totality of the circumstances; the CL opinion text carries slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7fe85aa9469aba8a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Young"}, "payload": {"all": [{"cite": "964 F.3d 938", "page": "938", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "964"}], "display": "964 F.3d 938", "official": {"cite": "964 F.3d 938", "page": "938", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "964"}, "official_selection_present": true, "record_id": "United States v. Young"}}
{"assertion_id": "48f0100a9df90913", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Young"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Young", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Young

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Young",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Young",
    "case_name_short": "Young",
    "case_name_full": "",
    "input_case_name": "United States v. Young",
    "court": "U.S. Court of Appeals, 10th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": "2020-07-07",
    "year": 2020,
    "docket": "18-6221",
    "cluster_id": 4766220,
    "lead_opinion_id": 4546567,
    "sibling_ids": [],
    "absolute_url": "/opinion/4766220/united-states-v-young/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "964 F.3d 938",
      "volume": "964",
      "reporter": "F.3d",
      "page": "938",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "964 F.3d 938",
        "volume": "964",
        "reporter": "F.3d",
        "page": "938",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "964 F.3d 938",
    "official_selection": {
      "court_class": "coa",
      "selected": "964 F.3d 938",
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
    "date_created": "2026-07-07T13:48:58Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:49:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:49:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:49:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:49:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-young--4766220",
      "to_record_id": "United States v. Young",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Young

```
                                                                               FILED
                                                                   United States Court of Appeals
                                     PUBLISH                               Tenth Circuit

                     UNITED STATES COURT OF APPEALS                        July 7, 2020
                                                                      Christopher M. Wolpert
                           FOR THE TENTH CIRCUIT                          Clerk of Court
                       _________________________________

 UNITED STATES OF AMERICA,

      Plaintiff - Appellee,

 v.                                                        No. 18-6221

 SHANE THOMAS YOUNG,

      Defendant - Appellant.
                     _________________________________

                    Appeal from the United States District Court
                       for the Western District of Oklahoma
                          (D.C. No. 5:18-CR-00096-HE-1)
                      _________________________________

Howard Pincus, Assistant Federal Public Defender, Denver, Colorado (Virginia Grady,
Federal Public Defender, Denver, Colorado with him on the briefs) for Defendant-
Appellant.

Steven Creager, Assistant United States Attorney, Oklahoma City, Oklahoma (Timothy
Downing, United States Attorney, and Nicholas Patterson, Assistant United States
Attorney, with him on the brief) for Plaintiff-Appellee.
                        _________________________________

Before LUCERO, KELLY, and PHILLIPS, Circuit Judges.
                  _________________________________

LUCERO, Circuit Judge.
                    _________________________________

      Defendant Shane Young appeals the district court’s denial of his motion to

suppress a confession. He argues the confession was involuntary because the law

enforcement officer who interrogated him deceived him about having access to the
federal judge on the case. Exercising jurisdiction under 28 U.S.C. § 1291, we reverse

and remand to the district court.

                                           I

      In the early morning hours of March 16, 2018, a Woodward County Sheriff’s

Office deputy observed Young’s vehicle swerving on the roadway and signaled for

Young to stop his car. Young continued to drive, ultimately pulling into a nearby

residential property, stopping his car, and fleeing on foot. The deputy pursued, tasing

and arresting Young. After the arrest, the deputy retraced Young’s path and found a

small headphones case containing about four grams 1 of a mixture or substance

containing methamphetamine. Young was released later that day.

      In the late afternoon of March 16, officers returned to the area and found a

black bag containing about 93 grams of a mixture or substance containing

methamphetamine near where Young stopped his car. A resident of the property

stated that he did not recognize the bag the deputies had found in his yard and had

not observed anyone walking around the property earlier that day. Later that night,

the deputy rearrested and interviewed Young. Young admitted to possessing the

smaller quantity of methamphetamine but denied that the larger quantity was his. He

then cut off questioning and revoked his consent to speak.




      1
       The record alternately states the quantity in the headphones case was 3.5
grams and 4 grams. The amount does not affect the outcome of this appeal.

                                          2
      Four days later, while still held in the county jail, Young was interrogated by

Federal Bureau of Investigations Special Agent Kent Brown and a state narcotics

agent. 2 Agent Brown advised Young of his Miranda rights, which he waived. At the

beginning of the interrogation, Young informed the agents that he was concerned

about who would pick up his pregnant fiancée on her release from rehab the next day

and worried about how criminal charges would affect his ability to raise his new

baby. He told the agents he was sick to his stomach and wanted to “roll over and

die.” Agent Brown told Young that he tried to help people in trouble if they were

trying to “do what’s right and get on the right path,” and that after their conversation

he would do his best to try and help.

      Agent Brown then told Young he had gone to Oklahoma City the prior

afternoon to meet with the Assistant United States Attorney and brief the prosecutor

about Young’s arrest. He said the prosecutor had met with the judge. Agent Brown

then showed Young a federal warrant for his arrest. Young was visibly shocked.

Agent Brown told Young he wanted to proceed from the “bad news” that Young was

facing federal charges “to the good news.” He urged Young to trust him and told him

that “from this moment on, I’m on your side.” Young queried, “Is any of this going



      2
        A video recording of the interrogation was introduced at the suppression
hearing. There are no allegations that the footage has been doctored or altered, so we
may rely on this video evidence. See Scott v. Harris, 550 U.S. 372, 381 (2007)
(holding appellate court “should have viewed the facts in the light depicted by the
videotape”); cf. Carabajal v. City of Cheyenne, Wyo., 847 F.3d 1203, 1207 (10th Cir.
2017) (“[W]e cannot ignore clear, contrary video evidence in the record depicting the
events as they occurred.”).
                                           3
to help me?” Agent Brown responded, “Yes, absolutely,” and pivoted again to the

“good news,” telling Young that he was on his side and that Young had to trust him.

      Agent Brown continued, describing his trip to Oklahoma City the previous day

to obtain the federal warrant and telling Young that he had spoken with the judge

who had reviewed the case. He said the judge had looked at Young’s criminal

record. Agent Brown emphasized that he was “not bullshitting” and repeatedly told

Young to trust him. Then, he told Young that with the smaller amount of

methamphetamine, the judge was willing to charge “anywhere from five to ten

years.” Agent Brown said that Young had two options and that he could “physically

buy down the amount of time you see in a federal prison,” with the difference

depending on Young’s “willingness to own to the information.” He continued,

“every time you answer a question truthfully, it ticks time off that record, it ticks

time off how much you’re going to actually see.” He also repeatedly told Young that

he would go back to the judge and tell him what Young said at the interview,

invoking his supposed relationship with the judge numerous times. Agent Brown

reiterated yet again that Young needed to trust him, and he asked Young about the

bag with the larger quantity of drugs in it, suggesting that Young could explain that

he threw the bags in different directions as he ran from the car.

      In response, Young wondered aloud whether he should have a lawyer present.

Then, he said, “I want to help myself out, man, but at the same time I feel like I’m

buying the farm.” Following Agent Brown’s earlier suggestion, Young admitted that



                                            4
after he exited his vehicle, he lost his grip on the containers of methamphetamine,

and they flew in different directions as he was running away.

      After his confession, Young was charged with possession with intent to

distribute approximately 97 grams of a mixture or substance containing a detectable

amount of methamphetamine. He moved to suppress his confession as involuntary.

The district court held a suppression hearing, at which Agent Brown testified that his

“number of mentions” of having spoken with the judge were all “error[s] in

specificity of speech” and that his intent was to say “prosecutor.” Agent Brown also

stated that at the time of Young’s interview, although he had spoken about the case to

the federal magistrate judge who signed Young’s warrant, they had not discussed

potential charges. Agent Brown further testified that he did not know the actual

sentencing range for the offenses for which Young was charged and that when he

used the five- to ten-year figure, he was providing a tangible number to explain to

Young that “cooperation can pay dividends.”

      Although the court found Agent Brown made false representations and

improper promises of leniency that were “coercive in nature under the

circumstances,” it ultimately concluded Young’s confession was not involuntary and

denied his motion to suppress. Young pled guilty and was sentenced to 188 months’

imprisonment and five years’ supervised release. He timely appealed.

                                          II

      “When a party challenges a district court’s ruling on a motion to suppress a

confession, we review its conclusions of law de novo and its factual findings for clear

                                          5
error. We consider the evidence in the light most favorable to the district court’s

determination.” United States v. Pettigrew, 468 F.3d 626, 633 (10th Cir. 2006)

(citation omitted). Thus, “when reviewing the denial of a motion to suppress, an

appellate court must consider the evidence adduced at the suppression hearing . . . in

the light most favorable to the Government.” United States v. Rodebaugh, 798 F.3d

1281, 1290 (10th Cir. 2015) (alteration and quotation omitted).

      “[C]onvictions following the admission into evidence of confessions which are

involuntary, i.e., the product of coercion, either physical or psychological, cannot

stand.” Rogers v. Richmond, 365 U.S. 534, 540 (1961). “To be admiss[i]ble, a

confession must be made freely and voluntarily; it must not be extracted by threats in

violation of due process or obtained by compulsion or inducement of any sort.”

Griffin v. Strong, 983 F.2d 1540, 1542 (10th Cir. 1993). Voluntariness is determined

under the totality of the circumstances, and no single factor is determinative. See

United States v. Lopez, 437 F.3d 1059, 1063 (10th Cir. 2006).

      The district court found that Agent Brown made false representations to Young

when he stated that he was “on your side” and that he had discussions with the judge

about Young’s charges and sentence. It also found Agent Brown’s statement that

Young could “buy down” his time by answering questions truthfully was a promise

of leniency. Its findings that there were false representations and promises of

leniency are factual findings subject to clear error review. See id. at 1062, 1064.

The government does not challenge these findings on appeal.



                                           6
      We review de novo the legal conclusion that Young’s statement was voluntary.

Id. at 1062. The government bears the burden of showing voluntariness by a

preponderance of the evidence. Id. at 1063. “The central consideration in

determining whether a confession has been coerced always involves this question:

did the governmental conduct complained of bring about a confession not freely self-

determined?” Griffin, 983 F.2d at 1543 (quotations omitted). Put another way, the

issue is whether the confession is “the product of an essentially free and

unconstrained choice by its maker.” United States v. Perdue, 8 F.3d 1455, 1466

(10th Cir. 1993) (quotation omitted). If not, “if his will has been overborne and his

capacity for self-determination critically impaired, the use of his confession offends

due process.” Id. (quotation omitted). The inquiry is based on the totality of the

circumstances and requires consideration of “both the characteristics of the accused

and the details of the interrogation.” United States v. Toles, 297 F.3d 959, 966 (10th

Cir. 2002). This test “does not favor any one of these factors over the others—it is a

case-specific inquiry where the importance of any given factor can vary in each

situation.” Sharp v. Rohling, 793 F.3d 1216, 1233 (10th Cir. 2015).

      “[C]oercive police activity is a necessary predicate to the finding that a

confession is not ‘voluntary.’” Colorado v. Connelly, 479 U.S. 157, 167 (1986).

Accordingly, we first address Agent Brown’s conduct—his misrepresentations and

promises of leniency. We then turn to other factors that may contribute to

involuntariness, including the defendant’s mental condition. See id. at 164 (“[A]s

interrogators have turned to more subtle forms of psychological persuasion, courts

                                           7
have found the mental condition of the defendant a more significant factor in the

‘voluntariness’ calculus.”); United States v. Erving L., 147 F.3d 1240, 1249-50 (10th

Cir. 1998) (defendant’s personal characteristics relevant if officers’ conduct

coercive).

                                           A

      Promises of leniency are “relevant to determining whether a confession was

involuntary and, depending on the totality of the circumstances, may render a

confession coerced.” Clanton v. Cooper, 129 F.3d 1147, 1159 (10th Cir. 1997),

overruled on other grounds by Becker v. Kroll, 494 F.3d 904 (10th Cir. 2007).

Similarly, an officer’s deceptions or misrepresentations may, but do not necessarily,

render a confession coerced. See Lopez, 437 F.3d at 1065.

      During the interrogation, Agent Brown told Young that he was facing a

sentence of five to ten years’ imprisonment and that the length of the sentence

depended primarily on Young’s cooperation. He also told Young he could

“physically buy down the amount of time you see in a federal prison.” These were

misrepresentations. Possession with intent to distribute 97 grams of a mixture or

substance containing methamphetamine carries a minimum sentence of five years and

a maximum sentence of forty years. 21 U.S.C. § 841(b)(1)(B). In contrast,

possession with intent to distribute four grams of a mixture or substance containing

methamphetamine carries a maximum sentence of 20 years and no mandatory

minimum. § 841(b)(1)(C). The latter may also be prosecuted as simple possession,

with a maximum sentence of one, two, or three years depending on the defendant’s

                                           8
prior criminal history. 21 U.S.C. § 844(a). Similarly, under the Sentencing

Guidelines, possession of 97 grams of a mixture or substance containing

methamphetamine corresponds to a much longer sentence than possession of four

grams, contrary to Agent Brown’s misrepresentations.

       Although we do not require a law enforcement officer to inform a suspect of

the penalties for all the charges he may face, if he misrepresents these penalties, then

that deception affects our evaluation of the voluntariness of any resulting statements.

In this interrogation, Agent Brown misrepresented the law to Young, a factor that

weighs in favor of concluding his actions were coercive. See Clanton, 129 F.3d at

1158 (“[C]ourts are much less likely to tolerate misrepresentations of law.”).

       Although “the fact that an officer promises to make a defendant’s cooperation

known to prosecutors will not produce a coerced confession,” Lopez, 437 F.3d at

1064, Agent Brown did not merely inform Young that cooperation would be viewed

favorably by the prosecutor. Instead, Agent Brown repeatedly told Young he had

spoken with a federal judge who had reviewed the case. He emphasized to Young

that he would tell the judge whether Young had cooperated and that cooperation

would “physically buy down the amount of time you see in a federal prison.” He

said, “every time you answer a question truthfully, it ticks time off that record, . . .

that’s the way it works.” But that is not the way the federal system works. Agents

do not provide information directly to federal judges for use in determining the

charges or sentences suspects face.



                                             9
      At the suppression hearing, Agent Brown tried to walk back his statements

about talking to the “judge,” testifying that he had meant to refer to the prosecutor. 3

But we do not consider what Agent Brown intended to say. Rather, we view the

coercive nature of assertions from the standpoint of the defendant. See United States

v. Walton, 10 F.3d 1024, 1029 (3d Cir. 1993); United States v. Shears, 762 F.2d 397,

402 (4th Cir. 1985) (evaluating “the defendant’s perception of what government

agents have promised”).

      Turning to Agent Brown’s promises of leniency, we have held that “a promise

of leniency is relevant to determining whether a confession was involuntary and,

depending on the totality of the circumstances, may render a confession coerced.”

Clanton, 129 F.3d at 1159; see also Griffin, 983 F.2d at 1543 (“Where a promise of

leniency has been made in exchange for a statement, an inculpatory statement would

be the product of inducement, and thus not an act of free will.” (quotations omitted));

cf. United States v. Nguyen, 155 F.3d 1219, 1223 (10th Cir. 1998) (holding statement

that prosecutor will be informed of defendant’s cooperation does not, without more,

constitute a promise of leniency). In this case, Agent Brown told Young he could




      3
        The district court did not explicitly rule on whether it credited Agent
Brown’s explanation. It ultimately determined that even if credited, the explanation
did “not change the coercive nature of the assertions when viewed from the
standpoint of the defendant.”

                                           10
“physically buy down” the length of the sentence and that each truthful response

would “tick[] time off” his sentence. 4

      We faced a similar situation in Lopez. In that case, law enforcement officers

wrote the words “mistake,” “murder,” “6,” and “60” on slips of paper to show the

defendant he would receive a six-year sentence if he cooperated and a sixty-year

sentence if he did not. 437 F.3d at 1064. We held this was not a permissible “limited

assurance,” but rather an improper promise of leniency “of the sort that may . . .

critically impair a defendant’s capacity for self-determination.” Id. at 1065. The

government contends that Lopez is distinguishable because it involved a quid pro quo

promise of leniency, arguing that Agent Brown’s improper promises were not as

specific as the agents’ promises in Lopez. We are not persuaded.

      In Lopez, we held the defendant’s confession was involuntary because of the

officers’ promise of leniency, combined with their misrepresentation or exaggeration

of the evidence against the defendant. Id. at 1064-65. The government argues, and

Young does not contest, that Agent Brown did not misrepresent or exaggerate the

evidence against him. But like the officers in Lopez, Agent Brown made inaccurate

representations about the sentence Young faced and promised leniency if Young

incriminated himself. Critically, Agent Brown also made improper representations




      4
        Although Agent Brown did tell Young he made no promises as to a particular
sentence or disposition, he did not explicitly say so until after Young incriminated
himself.

                                          11
about his purported access to a federal judge—misconduct as coercive as the officers’

misrepresentation or exaggeration of the evidence in Lopez.

      The government points out that just four days before Agent Brown’s

interrogation, 5 Young stopped the sheriff’s deputy’s interrogation by revoking his

consent to speak. The government argues that this shows that Young generally knew

he could stop an interrogation. In contrast, about eleven minutes into Agent Brown’s

questioning, Young confessed. By that time, Young had been confronted with a

federal arrest warrant and told that federal charges had been filed against him. But

the main difference between the two interrogations is that before the second, Agent

Brown misrepresented the law and made false promises of leniency, including a

particularly troubling false promise of access to the federal judiciary. 6 Young’s

awareness that he could stop the interrogation did little to mitigate the coercive

nature of Agent Brown’s actions.

      We acknowledge that some aspects of the interrogation were not coercive. In

Sharp, we noted that we should consider “whether the suspect was advised of his or



      5
        Agent Brown erroneously testified that the first interrogation occurred the
day prior to his. The district court repeated this error. The first interrogation
occurred on March 16, 2018, whereas Agent Brown’s interrogation was on March 20.
      6
         The government points out other differences between the interviews: it states
that Young seemed more willing to confess at the beginning of the second interview,
that Agent Brown developed a rapport with Young, and that Agent Brown confirmed
that he had seen the dashboard camera video and offered to explain why the agents
were asking about Young’s possession of the container with 93 grams. But in our
view, the key difference was Agent Brown’s misrepresentations and promises of
leniency.
                                           12
her constitutional rights, the length of his or her detention, the nature of the

questioning, and any physical punishment such as deprivation of food or sleep.” 793

F.3d at 1233. None of these forms of coercion occurred in this case, and admittedly,

several factors weigh against concluding the interrogation was coercive. The

questioning was friendly and short: Young confessed within minutes of the

beginning of the interrogation. Cf. Lopez, 437 F.3d at 1062, 1065 (implying

interrogations lasting thirty minutes or one hour are short). Young was fully advised

of his constitutional rights 7 and knew that he could stop the interrogation, as

demonstrated by his stopping of the deputy’s questioning four days earlier. And well

into the interrogation, he asked the agents whether he should wait for his lawyer to be

present and declined to consent to a search of his phone.

       But these factors are not dispositive. Cf. United States v. Bustillos-Munoz,

235 F.3d 505, 517 n.8 (10th Cir. 2000) (“A suspect cannot be subjected to invalid

coercion to obtain a confession just because he earlier was given a valid Miranda

warning.”). Our inquiry is based on the totality of the circumstances. Considering

all of the evidence, we agree with the district court that Agent Brown’s conduct was



       7
         Notably, before the Miranda warning, the state narcotics agent elicited what
could be construed as an incriminating statement. After Young was brought into the
interrogation room but before he received a Miranda warning, Agent Brown left the
room. Young asked the state officer if the agents were going to get him out of jail,
and the officer responded that it would depend on Agent Brown. After a brief
silence, the officer asked Young if he had anything else “going on,” and Young
responded that he had been “working selling dope.” Because Young did not argue at
the district court or on appeal that this pre-warning questioning contributed to the
involuntariness of his confession, we do not consider it.
                                            13
coercive in nature, particularly in light of his misrepresentation of the sentence

Young faced, his false statement that he would speak to a federal judge about

Young’s cooperation, and his promises of leniency.

                                           B

      Because we agree that Agent Brown’s conduct was coercive, we turn to

Young’s personal characteristics to answer the ultimate question: whether Young’s

statements were voluntary. See Lopez, 437 F.3d at 1064. There is no evidence in the

record to indicate that Young was “unusually susceptible to coercion because of age,

lack of education, or intelligence.” Toles, 297 F.3d at 966 (quotation omitted).

Young was 43 years old and had completed a GED. And nothing in the record

suggests that he has limited intelligence. See Lopez, 437 F.3d at 1060 (age and

education did not weigh in favor of involuntariness for 33-year old defendant who

finished eleventh grade); Toles, 297 F.3d at 966.

      The district court correctly noted that Young had prior experience with the

criminal justice system. Although that is relevant to our analysis of voluntariness,

see id., Young’s prior experience was solely in the state system. This prior

experience did not necessarily make him less susceptible to believing promises of

leniency and misrepresentations by a federal law enforcement officer explaining his

access to a federal judge and how Young could “buy down” his sentence. And

Young was visibly shocked when Agent Brown told him he faced federal charges.

      Young’s personal characteristics are not dispositive, and they do not convince

us that Young could withstand the coercion created by Agent Brown’s legal

                                           14
misrepresentations and promises of leniency. See Lopez, 437 F.3d. at 1066

(concluding coerced confession was involuntary even though defendant’s personal

characteristics did not suggest unusual susceptibility to coercion). Under the totality

of the circumstances, we conclude that Young’s capacity for self-determination was

critically impaired, rendering his confession involuntary.

                                          III

      For the foregoing reasons, we REVERSE the decision of the district court,

VACATE the judgment entered against Young, and REMAND for proceedings

consistent with this decision.




                                          15

```

---
