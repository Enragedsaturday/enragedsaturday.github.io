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

## GROUP: _overhaul2/lake/cases/State v. Wint.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: State v. Wint
type: case
citation: "236 N.J. 174 (2018)"
parallel_cite: 198 A.3d 963
neutral_cite: ""
court: N.J. 2018
court_level: state
circuit: ""
year: 2018
date_decided: 2018-12-12
docket: "A-28/29 September Term 2017; 079660"
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
  opinion_url: "https://www.courtlistener.com/opinion/8267547/state-v-wint/"
  cluster_id: 8267547
  opinion_id: null
  identity_checked: true
lake:
  record_id: State v. Wint
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: Key
related:
  - "[[Miranda Waiver and Invocation]]"
  - "[[Edwards v. Arizona]]"
  - "[[Miranda v. Arizona]]"
tags:
  - case
  - fifth-amendment
  - miranda
  - right-to-counsel
  - custodial-interrogation
  - state-court
holding: "A suspect's six months of continuous pre-indictment custody is not a 'break in custody' under Maryland v. Shatzer, so the Edwards bar on police-initiated reinterrogation after an invocation of counsel remained in force; because none of the three exceptions — counsel provided, defendant-initiated communication, or a break in custody — applied, a later Mirandized waiver could not validate the interrogation and the incriminating statements had to be suppressed."
---

# State v. Wint

*236 N.J. 174 (2018)* (No. A-28/29 September Term 2017; 079660) · Supreme Court of New Jersey · **Persuasive — state, illustrative** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 8267547 → opinion 8232868 (236 N.J. 174, decided 2018-12-12); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
New Jersey officers arrested Laurie Wint on a New Jersey murder charge and questioned him at the Camden County Prosecutor's Office. After *[[Miranda v. Arizona|Miranda]]* warnings Wint invoked his right to counsel, and questioning stopped; immediately, two Pennsylvania detectives investigating an unrelated Bucks County murder entered, re-warned him, and Wint again requested counsel. Wint then remained in continuous pre-indictment custody in New Jersey for six months. He was transported to Bucks County, where the Pennsylvania detectives administered *[[Miranda v. Arizona|Miranda]]* warnings a third time but did not provide the counsel Wint had twice requested; this time he waived his rights and allegedly incriminated himself in the New Jersey murder. The trial court admitted the statements — finding Wint had reinitiated contact and that the six-month lapse was a *[[Maryland v. Shatzer|Shatzer]]* "break in custody" — and a jury convicted him of passion/provocation manslaughter. The Appellate Division [[Reading and Citing Cases#on-remand|remanded]] for [[Fruits and Attenuation|attenuation]] and break-in-custody analysis.

## Issue
Whether a suspect who invokes his right to counsel and then remains in continuous pre-indictment custody for six months experiences a "break in custody" under *[[Maryland v. Shatzer]]* that dissolves the *[[Edwards v. Arizona|Edwards]]* bar and permits police-initiated reinterrogation without counsel.

## Rule
Under *[[Edwards v. Arizona|Edwards]]*, once an accused invokes counsel during custodial interrogation, any statement obtained in a later police-initiated custodial interrogation must be suppressed unless counsel was provided, the accused initiated the communication, or a break in custody of sufficient duration intervened. The New Jersey Supreme Court reversed, holding that none of those exceptions was satisfied: "Wint remained in continuous pre-indictment custody for a period of six months before the questioning in Bucks County. Therefore, no 'break in custody' occurred within the intendment of *Shatzer*." — 236 N.J. at 181. ^pin-181

## Application
Wint invoked counsel twice, never initiated the Bucks County interrogation, and was never given the counsel he had requested; repeated *[[Miranda v. Arizona|Miranda]]* warnings did not cure the *[[Edwards v. Arizona|Edwards]]* violation. His six unbroken months of pre-indictment custody were the opposite of the release that *[[Maryland v. Shatzer|Shatzer]]* treated as a break — he never returned to normal life or shook off custody's coercive pressures, which only intensified as indictment was delayed. Because none of the three *[[Edwards v. Arizona|Edwards]]* exceptions applied, the later waiver could not validate the interrogation and the statements were inadmissible.

## Conclusion
The Appellate Division's judgment was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]] for a new trial at which the incriminating statements must be suppressed. Albin, J., wrote for the Court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Wint* applies the *[[Edwards v. Arizona|Edwards]]*–*[[Maryland v. Shatzer|Shatzer]]* invocation rule to a pretrial detainee: continuous pre-indictment custody is not a "break in custody," so a fresh set of *[[Miranda v. Arizona|Miranda]]* warnings and a subsequent waiver cannot rehabilitate a police-initiated reinterrogation conducted after the accused invoked his right to counsel.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key*

## Sources
- [*State v. Wint*, 236 N.J. 174 (2018)](https://www.courtlistener.com/opinion/8267547/state-v-wint/) — pinpoint: 181 (no break-in-custody holding; the CL opinion text carries N.J.-reporter page labels). Parallel cite 198 A.3d 963. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3e8a8a6abc58cfc0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "State v. Wint"}, "payload": {"all": [{"cite": "198 A.3d 963", "page": "963", "reporter": "A.3d", "selected_official": false, "source": "cluster.citations[]", "type": 3, "volume": "198"}, {"cite": "236 N.J. 174", "page": "174", "reporter": "N.J.", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "236"}], "display": "236 N.J. 174", "official": {"cite": "236 N.J. 174", "page": "174", "reporter": "N.J.", "selected_official": true, "source": "cluster.citations[]", "type": 2, "volume": "236"}, "official_selection_present": true, "record_id": "State v. Wint"}}
{"assertion_id": "6aecdcd9abae573d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "State v. Wint"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "State v. Wint", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — State v. Wint

```json
{
  "schema_version": "s2.v1",
  "record_id": "State v. Wint",
  "status": "under_review",
  "identity": {
    "case_name": "State v. Wint",
    "case_name_short": "Wint",
    "case_name_full": "STATE of New Jersey, Plaintiff-Respondent/Cross-Appellant v. Laurie WINT, a/k/a Laurie A. Wint, Jr., Laurie Ainsworth Wint, Lance, Defendant-Appellant/Cross-Respondent.",
    "input_case_name": "State v. Wint",
    "court": "N.J. 2018",
    "court_id": "nj",
    "court_level": "state",
    "circuit": null,
    "state": "nj",
    "date_decided": "2018-12-12",
    "year": 2018,
    "docket": "A-28/29 September Term 2017; 079660",
    "cluster_id": 8267547,
    "lead_opinion_id": 8232868,
    "sibling_ids": [],
    "absolute_url": "/opinion/8267547/state-v-wint/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "236 N.J. 174",
      "volume": "236",
      "reporter": "N.J.",
      "page": "174",
      "type": 2,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "198 A.3d 963",
        "volume": "198",
        "reporter": "A.3d",
        "page": "963",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "198 A.3d 963",
        "volume": "198",
        "reporter": "A.3d",
        "page": "963",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "236 N.J. 174",
        "volume": "236",
        "reporter": "N.J.",
        "page": "174",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "236 N.J. 174",
    "official_selection": {
      "court_class": "state",
      "selected": "236 N.J. 174",
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
    "date_created": "2026-07-06T05:49:01Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:49:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:49:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:49:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:49:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "state-v-wint--8267547",
      "to_record_id": "State v. Wint",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — State v. Wint (truncated)

```
<opinion type="majority">
<author id="p-9">JUSTICE ALBIN delivered the opinion of the Court.</author>
<p id="p-10"><a class="page-label" data-citation-index="1" data-label="966" href="#p966" id="p966">*966</a><a class="page-label" data-citation-index="2" data-label="180" href="#p180" id="p180">**180</a>In <em>Edwards v. Arizona</em>, the United States Supreme Court held that when an accused invokes his right to have counsel present during a custodial interrogation, questioning must cease unless the accused initiates further communication or conversation. <extracted-citation case-ids="6187603" index="0" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U.S. 477</a></span></extracted-citation>, 484-85, <extracted-citation case-ids="6187603" index="1" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">101 S.Ct. 1880</a></span></extracted-citation>, <extracted-citation case-ids="6187603" index="2" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">68 L.Ed.2d 378</a></span></extracted-citation> (1981). The <em>Edwards</em> doctrine, which bars continuing an interrogation after a request for counsel, applies even if a different law enforcement agency seeks to question the accused about an unrelated crime, <em>Arizona v. Roberson</em>, <extracted-citation case-ids="6222614" index="3" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">486 U.S. 675</a></span></extracted-citation>, 686-88, <extracted-citation case-ids="6222614" index="4" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">108 S.Ct. 2093</a></span></extracted-citation>, <extracted-citation case-ids="6222614" index="5" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">100 L.Ed.2d 704</a></span></extracted-citation> (1988), and even if the accused has consulted with an attorney, <em>Minnick v. Mississippi</em>, <extracted-citation case-ids="6220774" index="6" url="https://cite.case.law/us/498/146/#p153"><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">498 U.S. 146</a></span></extracted-citation>, 153, <extracted-citation case-ids="6220774" index="7" url="https://cite.case.law/us/498/146/#p153"><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">111 S.Ct. 486</a></span></extracted-citation>, <extracted-citation case-ids="6220774" index="8" url="https://cite.case.law/us/498/146/#p153"><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">112 L.Ed.2d 489</a></span></extracted-citation> (1990). The <em>Edwards</em> doctrine, however, does not apply "when a suspect who initially requested counsel is reinterrogated after a <em>break in custody</em> that is of sufficient duration to dissipate its coercive effects." <em>Maryland v. Shatzer</em>, <extracted-citation case-ids="3582023" index="9" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">559 U.S. 98</a></span></extracted-citation>, 109, <extracted-citation case-ids="3582023" index="10" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>, <extracted-citation case-ids="3582023" index="11" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">175 L.Ed.2d 1045</a></span></extracted-citation> (2010) (emphasis added).</p>
<p id="p-11">In this case, law enforcement officers arrested defendant Laurie Wint on a New Jersey murder charge and brought him to the Camden County Prosecutor's Office for questioning. Wint invoked his right to counsel after receiving <em>Miranda</em> <footnotemark>1</footnotemark> warnings, and the interrogation ceased. Immediately afterwards, two detectives from Pennsylvania investigating an unrelated murder in Bucks County entered the interrogation room to question Wint. After receiving his rights for the second time, Wint again requested the presence of counsel, ending the interrogation. Wint remained in continuous pre-indictment custody in Camden County when, six months later, he was transported to Bucks County. There, Pennsylvania detectives again administered <em>Miranda</em> warnings but did not provide counsel as Wint had earlier requested. This time, Wint waived his rights and allegedly incriminated himself in the New Jersey murder.</p>
<p id="p-12"><a class="page-label" data-citation-index="2" data-label="181" href="#p181" id="p181">**181</a>The trial court denied Wint's motion to suppress his incriminating remarks believing that, for <em>Edwards</em> purposes, Wint reinitiated communication with the Pennsylvania detectives. The court also determined that the six-month lapse in time between interrogations satisfied the <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em>"break-in-custody" requirement. With the admission of Wint's incriminating statements at trial, a jury convicted Wint of passion/provocation manslaughter and other related offenses.</p>
<p id="p-13">The Appellate Division remanded to the trial court for reconsideration of the suppression issue. The panel held that the Pennsylvania detectives violated <em>Edwards</em> by attempting to interrogate Wint just minutes after he had requested counsel <a class="page-label" data-citation-index="1" data-label="967" href="#p967" id="p967">*967</a>from New Jersey law enforcement officers. The panel also found that Wint did not initiate the third interrogation in Bucks County. The panel, however, stopped short of suppressing Wint's incriminating statements. The panel determined that the trial court must engage in an attenuation analysis and also decide whether the six-month period between Wint's requests for counsel and the third round of questioning in Bucks County constituted a "break in custody" within the purview of <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em>.</p>
<p id="p-14">We now reverse. We agree with the Appellate Division that the Pennsylvania detectives violated <em>Edwards</em> by attempting to question Wint in Camden after his earlier request for counsel. We also agree that Wint did not initiate the interrogation that occurred in Bucks County. That third and last interrogation proceeded without the presence of counsel despite Wint's two previous requests for counsel. Here, the giving of repeated <em>Miranda</em> warnings did not cure the <em>Edwards</em> violation.</p>
<p id="p-15">Wint remained in continuous pre-indictment custody for a period of six months before the questioning in Bucks County. Therefore, no "break in custody" occurred within the intendment of <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em>. The Supreme Court set a bright line in <em>Edwards</em> and <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em>: after a defendant requests counsel during a custodial interrogation, any statement secured during a subsequent custodial interrogation must be suppressed unless (1) counsel was provided <a class="page-label" data-citation-index="2" data-label="182" href="#p182" id="p182">**182</a>during the questioning, (2) defendant initiated the communication, or (3) a break in custody occurred. None of those exceptions apply here. We therefore part with the panel's decision to remand for an attenuation analysis and a break-in-custody analysis.</p>
<p id="p-16">Accordingly, we reverse the judgment of the Appellate Division and remand for a new trial on the charge of passion/provocation manslaughter at which the incriminating statements made by Wint in Pennsylvania will be inadmissible.</p>
<p id="p-17">I.</p>
<p id="p-18">A.</p>
<p id="p-19">On September 26, 2012, Wint was charged in a Camden County indictment with murder, N.J.S.A. 2C:11-3(a)(1) and (2) ; second-degree possession of a firearm for an unlawful purpose, N.J.S.A. 2C:39-4(a) ; second-degree unlawful possession of a firearm, N.J.S.A. 2C:39-5(b) ; fourth-degree resisting arrest, N.J.S.A. 2C:29-2(a) ; and second-degree certain persons not to possess weapons, N.J.S.A. 2C:39-7(b). Wint moved to suppress a statement he allegedly made to Pennsylvania detectives in Bucks County. He claimed that the Pennsylvania detectives violated <em>Edwards</em> by initiating an interrogation despite his earlier request for counsel in New Jersey.</p>
<p id="p-20">A suppression hearing was conducted in the Camden County Superior Court, Law Division. At the hearing, the State elicited testimony from three witnesses: Investigator Lance Saunders of the Camden County Prosecutor's Office and two Pennsylvania detectives -- Detective John Bonargo of the Warminster Township Police Department and Detective Martin McDonough of the Bucks County District Attorney's Office. The testimony focused on three interrogations of Wint while he remained in pre-indictment custody.</p>
<p id="p-21">Wint was charged on June 16, 2011 with the murder of Kevin Miller in the city of Camden and on July 29, 2011 with the murder of Tyrone Newman in Warminster Township, Pennsylvania. On <a class="page-label" data-citation-index="2" data-label="183" href="#p183" id="p183">**183</a>July 31, 2011, Camden police officers arrested Wint and transported him to the Camden County Prosecutor's Office for questioning.</p>
<p id="p-22">Investigator Saunders began interrogating Wint while Detectives Bonargo and McDonough from Pennsylvania watched <a class="page-label" data-citation-index="1" data-label="968" href="#p968" id="p968">*968</a>from an adjacent room. Investigator Saunders advised Wint of his <em>Miranda</em> rights, including his right to the presence and appointment of counsel. Following a brief exchange, Wint responded, "I think I should call my lawyer" and "I really don't want to talk to anybody." All questioning then ceased.</p>
<p id="p-23">After leaving the interrogation room, Investigator Saunders informed Detectives Bonargo and McDonough that Wint had invoked his right to counsel. Nevertheless, approximately three minutes later, the two Pennsylvania detectives entered the interrogation room to question Wint about their case. The detectives introduced themselves and, while acknowledging that Wint had chosen not to speak about the Camden case, asked whether he would be willing to speak about the Bucks County investigation. Wint responded he would if given a cigarette. However, after the detectives read him his <em>Miranda</em> rights, Wint requested the presence of counsel:</p>
<blockquote id="p-24">[McDonough]: Do you wish to speak to us without a lawyer being present?</blockquote>
<blockquote id="p-25">[Wint]: I want him to sit here while we talk.</blockquote>
<blockquote id="p-26">[McDonough]: I didn't hear. Do you wish to speak to us without a lawyer being present?</blockquote>
<blockquote id="p-27">[Wint]: I want him to sit here while we talk.</blockquote>
<blockquote id="p-28">[McDonough]: You want a lawyer here with us?</blockquote>
<blockquote id="p-29">[Wint]: Yeah --</blockquote>
<blockquote id="p-30">[McDonough]: Okay, so that, that won't happen today because we don't have a lawyer here with you --</blockquote>
<blockquote id="p-31">[Wint]: Oh --</blockquote>
<blockquote id="p-32">[McDonough]: But if you want one, that, that, that's fine.</blockquote>
<blockquote id="p-33">[Wint]: Yeah.</blockquote>
<blockquote id="p-34">[McDonough]: You're welcome to that.</blockquote>
<blockquote id="p-35">[Wint]: Okay.</blockquote>
<blockquote id="p-36">[McDonough]: But, um, if you wanted to talk to us today then, then your answer here would be no?</blockquote>
<blockquote id="p-37">[Wint]: No. It would be no.</blockquote>
<blockquote id="p-38"><a class="page-label" data-citation-index="2" data-label="184" href="#p184" id="p184">**184</a>[McDonough]: Or do you want to talk to us today?</blockquote>
<blockquote id="p-39">[Wint]: I wanna talk to ya'll but I want a lawyer here present cause I don't, I don't --</blockquote>
<blockquote id="p-40">[McDonough]: I got ya. I got ya. If that's, that, if that's your answer, that, that's your answer.</blockquote>
<blockquote id="p-41">[Wint]: Yeah. So --</blockquote>
<blockquote id="p-42">[McDonough]: So, you do not want to talk to us right now?</blockquote>
<blockquote id="p-43">[Wint]: Without a lawyer.</blockquote>
<p id="p-44">In light of that dialogue, the Pennsylvania detectives stopped the questioning and exited the room. When Wint left the room, the detectives initiated an unrecorded verbal exchange with him. The detectives wished him good luck and stated, "[W]hen we get you back to Bucks County we can talk about this again." Wint responded, "[Y]eah, I'll talk to you when we get back to Bucks County."</p>
<p id="p-45">Several months later, the Pennsylvania detectives returned to Camden to secure DNA samples from Wint, who was being held in the Camden County jail. In their encounter with Wint, the detectives informed him that they were taking steps to transfer him to Bucks County where they would like to talk to him. Wint reportedly responded, "I'll talk to you when I get back to Bucks [County]." During neither of those informal conversations -- prompted by the detectives -- did Wint indicate that he wished to speak without counsel present.</p>
<p id="p-46">On January 18, 2012, six months after Wint had invoked his right to counsel in two separate interrogations, the Pennsylvania detectives transported Wint to the Warminster police station in Bucks County <a class="page-label" data-citation-index="1" data-label="969" href="#p969" id="p969">*969</a>for processing on the Pennsylvania murder charge. The booking process was audio recorded. Then, Wint was taken to a room with video- but not audio-recording capability. There, Detective McDonough advised Wint of his <em>Miranda</em> rights from the same form he used six months earlier. Wint signed the form and this time waived his rights.</p>
<p id="p-47">The detectives then questioned Wint about the circumstances surrounding the death of Tyrone Newman in Warminster. Detective McDonough penned a fifteen-page statement summarizing <a class="page-label" data-citation-index="2" data-label="185" href="#p185" id="p185">**185</a>Wint's first-person account of the events. In explaining the reason for his presence in Warminster at the time of the Newman homicide, Wint allegedly said: "In June 2011 I committed a murder in Camden. About three weeks after the murder I saw my picture on TV. J-Rock and I decided we needed to leave from Camden and go and stay in Warminster." According to Detective McDonough, Wint reviewed the fifteen-page statement, made some corrections in his own handwriting, and signed the statement.</p>
<p id="p-48">The trial court determined that Wint's admission that he committed a murder in Camden in June 2011 would be admissible at Wint's upcoming trial on the Camden County charges. The court found that Wint had knowingly, intelligently, and voluntarily waived his <em>Miranda</em> rights before making the incriminating statement. The court also concluded that, by saying "that he would speak to them when back in Pennsylvania," Wint reinitiated the conversation with the Pennsylvania detectives in Camden. In the court's view, that remark opened a pathway for the detectives to interrogate Wint six months later in the Warminster police station. Additionally, applying <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em>, the court maintained that the six-month gap between defendant's invocation of his right to counsel in Camden and the interrogation in Warminster was "a substantial lapse in time to warrant his questioning about the Camden homicide."</p>
<p id="p-49">B.</p>
<p id="p-50">At Wint's jury trial, the State presented evidence of a deadly confrontation between Wint and Kevin Miller in Eutaw Park in Camden on the evening of June 8, 2011. The State argued that Wint purposely and without justification shot and killed Miller. In contrast, Wint claimed that he acted in self-defense after being jumped by Miller and his cohorts.</p>
<p id="p-51">The State's testimony revealed that on June 8, Miller went to his girlfriend's home to celebrate her birthday only to learn that she was not there but in the company of Wint with whom she <a class="page-label" data-citation-index="2" data-label="186" href="#p186" id="p186">**186</a>formerly had an intimate relationship. Miller, angered by this revelation, drove around Camden with a friend, Clifton Bailey, in search of his girlfriend and Wint. Miller and Bailey eventually met up with a friend at Eutaw Park. Miller entered the park while his two friends remained at the park's entrance. When Bailey heard a gunshot, he raced inside the park and observed a person running from the scene. He found Miller seriously injured with a gunshot wound and took him to the hospital, where Miller died during surgery.</p>
<p id="p-52">The State presented no eyewitnesses to the shooting. The State, however, placed on the stand John Briggs -- Wint's best friend -- who testified to the account that Wint gave him of the confrontation in the park. According to that account, Miller, Bailey, and other individuals attempted to jump Wint. One person from Miller's group reached for a gun at which point Wint pulled out a handgun he was carrying and fired in self-defense.</p>
<p id="p-53">Wint testified that he learned that Miller was looking for him and that he believed that Miller and Bailey were members of the Bloods street gang. He <a class="page-label" data-citation-index="1" data-label="970" href="#p970" id="p970">*970</a>admitted that he was armed with a gun for his self-protection although he had no permit to carry the weapon. He stated that Miller and three others accosted him in Eutaw Park. Three members of the group started punching him, and he fell to the ground. Then, Bailey pulled out a gun as another person from the group reached for a second gun. At that point, Wint drew his gun and, without aiming, pulled the trigger. Wint claimed that, at the time, he did not know that he struck anyone, asserting, "I wasn't trying to kill anyone. I was just trying to save myself." Wint then ran from the park and discarded the weapon. He fled to Pennsylvania several weeks later, in part because he feared retaliation by the Bloods gang.</p>
<p id="p-54">To preemptively discredit that version of the shooting, the State earlier presented both the medical examiner's testimony that the deadly shot was fired at a downward angle and Detective McDonough's testimony that Wint admitted at the Warminster police station that he had "committed a murder" in Camden. Concerning <a class="page-label" data-citation-index="2" data-label="187" href="#p187" id="p187">**187</a>the alleged admission, Wint explained, "I told [Detective McDonough] I did a shooting in Camden," and that the detective characterized it as a murder.</p>
<p id="p-55">The jury acquitted Wint of murder but found him guilty of the lesser-included offense of passion/provocation manslaughter, N.J.S.A. 2C:11-4(b)(2), and the other charged offenses. The court sentenced Wint to an extended term of fourteen years on the manslaughter conviction, subject to the No Early Release Act, N.J.S.A. 2C:43-7.2 ; a consecutive term of eight years with a five-year period of parole disqualification on the certain-persons conviction; and a concurrent one-year term on the resisting-arrest conviction. The other firearm possessory offenses were merged. The court ran the aggregate twenty-two year term, subject to a sixteen-year and eleven-month period of parole ineligibility, consecutive to the sentence Wint was serving in Pennsylvania.</p>
<p id="p-56">C.</p>
<p id="p-57">In an unpublished opinion, the Appellate Division primarily focused on Wint's argument that the trial court's admission of Wint's incriminating statement to the Pennsylvania detectives in Warminster violated his constitutional rights as articulated in the <em>Edwards</em> line of cases. In addressing that issue, the panel made some preliminary findings: (1) "the Pennsylvania detectives had no right to initiate <em>any</em> interrogation of [Wint], only minutes after he had invoked his right to counsel in the same interrogation room to the Camden detectives"; (2) their attempted interrogation of Wint in Camden was constitutionally prohibited in the absence of summoning counsel for Wint; and (3) the detectives -- not Wint -- initiated the post-interrogation discussions in Camden and the later interrogation in the Warminster police station.<footnotemark>2</footnotemark></p>
<p id="p-58"><a class="page-label" data-citation-index="2" data-label="188" href="#p188" id="p188">**188</a>As the panel observed, " <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em> recognized an important doctrinal distinction between the interrogation of persons who are confined due to past convictions, as opposed to persons who are pretrial detainees," citing <em>Shatzer</em>, <extracted-citation case-ids="3582023" index="12" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">559 U.S. at 106</a></span>-08</extracted-citation>, <extracted-citation case-ids="3582023" index="13" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>. The panel acknowledged that, under <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em>, a break in custody after an interrogation means one thing for convicted prison inmates and another thing for pretrial detainees. For interrogated inmates, a break in custody is a release back to the general prison population, where "they return to their accustomed surroundings and daily routine,"</p>
<p id="p-59"><a class="page-label" data-citation-index="1" data-label="971" href="#p971" id="p971">*971</a>whereas for interrogated pretrial detainees, a break in custody is a release from pretrial custody and a return to a normal life in the free world, quoting <em>Shatzer</em>, <extracted-citation case-ids="3582023" index="14" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">559 U.S. at 113</a></span></extracted-citation>, <extracted-citation case-ids="3582023" index="15" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>.</p>
<p id="p-60">Despite the differences that <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em> delineated between prison inmates and pretrial detainees, the panel examined whether, for break-in-custody purposes, the circumstances of an interrogated pretrial detainee who remains in custody for six months in a county jail is any different from that of an interrogated convicted inmate who is released back into the general prison population. The panel questioned whether the ability of the Pennsylvania authorities to place coercive pressures or exert leverage on Wint, who was confined in a Camden jail, was any different than if he were a convicted inmate serving time in prison. Thus, the panel concluded that the record was "incomplete and inconclusive to enable the <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em>'break-in-custody' analysis to be resolved definitively."</p>
<p id="p-61">The panel also determined that the record was inadequate to analyze whether the six-month gap in time before the Warminster interrogation dissipated the taint of the improper attempted interrogation in Camden at which defendant invoked his right to counsel. The panel looked to <em>Michigan v. Mosley</em>, <extracted-citation case-ids="6175104" index="16" url="https://cite.case.law/us/423/96/"><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">423 U.S. 96</a></span></extracted-citation>, <extracted-citation case-ids="6175104" index="17" url="https://cite.case.law/us/423/96/"><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">96 S.Ct. 321</a></span></extracted-citation>, <extracted-citation case-ids="6175104" index="18" url="https://cite.case.law/us/423/96/"><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">46 L.Ed.2d 313</a></span></extracted-citation> (1975) ; <em>State v. Maltese</em>, <extracted-citation case-ids="4322636" index="19" url="https://cite.case.law/nj/222/525/"><span class="citation" data-id="2828534"><a href="/opinion/2828534/state-v-michael-a-maltese-073584/" aria-description="Citation for case: State v. Michael A. Maltese (073584)">222 N.J. 525</a></span></extracted-citation>, <extracted-citation case-ids="4322636" index="20" url="https://cite.case.law/nj/222/525/"><span class="citation" data-id="2828534"><a href="/opinion/2828534/state-v-michael-a-maltese-073584/" aria-description="Citation for case: State v. Michael A. Maltese (073584)">120 A.3d 197</a></span></extracted-citation> (2015) ; and <em>State v. Hartley</em>, <extracted-citation case-ids="1356367" index="21" url="https://cite.case.law/nj/103/252/"><span class="citation" data-id="9646552"><a href="/opinion/1520309/state-v-hartley/" aria-description="Citation for case: State v. Hartley">103 N.J. 252</a></span></extracted-citation>, <extracted-citation index="22" url="https://cite.case.law/citations/?q=511%20A.2d%2080"><span class="citation" data-id="9646552"><a href="/opinion/1520309/state-v-hartley/" aria-description="Citation for case: State v. Hartley">511 A.2d 80</a></span></extracted-citation> (1986), cases where courts conducted an attenuation analysis after the defendants invoked their right to remain silent, rather <a class="page-label" data-citation-index="2" data-label="189" href="#p189" id="p189">**189</a>than the <em>Edwards</em> line of cases where defendants invoked their right to an attorney. The panel directed that, on remand, the trial court conduct an attenuation analysis and examine a non-exhaustive list of factors: the time between the interviews; the place of the interviews; whether adequate <em>Miranda</em> warnings were given; the effect of any admissions made at the first interrogation on the second interrogation; and the "purpose and flagrancy" of the police misconduct, citing <em>Brown v. Illinois</em>, <extracted-citation case-ids="9639" index="23" url="https://cite.case.law/us/422/590/#p604"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590</a></span></extracted-citation>, 604, <extracted-citation case-ids="9639" index="24" url="https://cite.case.law/us/422/590/#p604"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>, <extracted-citation case-ids="9639" index="25" url="https://cite.case.law/us/422/590/#p604"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">45 L.Ed.2d 416</a></span></extracted-citation> (1975). The panel did "not subscribe to the extreme view that [Wint]'s invocation of his Fifth Amendment rights ... inexorably barred all law enforcement agents from any jurisdiction from attempting to interview him about the crimes during his lengthy period of pretrial detention."</p>
<p id="p-62">The panel instructed the trial court to decide, after conducting a break-in-custody and attenuation analysis, whether to suppress or admit Wint's incriminating statement. The panel stated that if the court orders suppression then "[Wint]'s conviction must be vacated and a new trial shall proceed, at which the statement will be excluded." The panel did not elaborate on whether any potential new trial applied just to the manslaughter conviction or also to the resisting-arrest and gun-possession convictions.</p>
<p id="p-63">Last, the panel rejected Wint's contentions that the prosecutor denied him a fair trial by arguing in summation that "he should have waited for the police at the scene of the shooting if indeed his conduct was innocuous" and that the trial court should have declared a mistrial after removing and replacing two deliberating jurors.</p>
<p id="p-64">We granted Wint's petition for certification, <extracted-citation case-ids="12492112,12460932" index="26" url="https://cite.case.law/nj/231/564/"><span class="citation multiple-matches"><a href="/c/N.J./231/564/">231 N.J. 564</a></span></extracted-citation>, <extracted-citation case-ids="12460930,12460931,12460932,12492110,12492111,12492112" index="27" url="https://cite.case.law/a3d/177/132/"><span class="citation multiple-matches"><a href="/c/A.3d/177/132/">177 A.3d 132</a></span></extracted-citation> (2017), and the State's cross-petition, <extracted-citation case-ids="12492080,12460901,12460902,12492079" index="28" url="https://cite.case.law/nj/231/546/"><span class="citation multiple-matches"><a href="/c/N.J./231/546/">231 N.J. 546</a></span></extracted-citation>, <extracted-citation case-ids="12460902,12460903,12460904,12492080,12492081,12492082" index="29" url="https://cite.case.law/a3d/177/122/"><span class="citation multiple-matches"><a href="/c/A.3d/177/122/">177 A.3d 122</a></span></extracted-citation> (2017).<footnotemark>3</footnotemark> We also granted the motions <a class="page-label" data-citation-index="1" data-label="972" href="#p972" id="p972">*972</a>of the American <a class="page-label" data-citation-index="2" data-label="190" href="#p190" id="p190">**190</a>Civil Liberties Union of New Jersey (ACLU) and the Association of Criminal Defense Lawyers of New Jersey (ACDL) to participate as amici curiae.</p>
<p id="p-65">II.</p>
<p id="p-66">A.</p>
<p id="p-67">Wint contends that the Appellate Division failed to follow the commands of <em>Edwards</em> and <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em> by remanding to the trial court for a break-in-custody and attenuation analysis. Wint asserts that he remained in continuous, uninterrupted pre-indictment custody from the time he repeatedly invoked his right to counsel during separate interrogations by New Jersey and Pennsylvania law enforcement authorities until he was questioned later in Pennsylvania without counsel. Given the absence of a break in custody, Wint submits, <em>Edwards</em> barred his subsequent interrogation without counsel because he did not initiate a discussion with the Pennsylvania detectives. He reasons that the amount of time a suspect spends in pre-indictment custody does not constitute a break in custody because the longer the period awaiting indictment, the greater the coercive pressure to cooperate without the counsel he earlier requested, citing <em>Minnick</em>, <extracted-citation case-ids="6220774" index="30" url="https://cite.case.law/us/498/146/#p153"><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">498 U.S. at 153</a></span></extracted-citation>, <extracted-citation case-ids="6220774" index="31" url="https://cite.case.law/us/498/146/#p153"><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">111 S.Ct. 486</a></span></extracted-citation>, and <em>Roberson</em>, <extracted-citation case-ids="6222614" index="32" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">486 U.S. at 686</a></span></extracted-citation>, <extracted-citation case-ids="6222614" index="33" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">108 S.Ct. 2093</a></span></extracted-citation>.</p>
<p id="p-68">Wint emphasizes that in erroneously requiring an attenuation analysis, the Appellate Division followed the line of <em>Miranda</em> cases involving a suspect's invocation of his right to remain silent, such as <em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">Mosley</a></span></em>, <em><span class="citation" data-id="2828534"><a href="/opinion/2828534/state-v-michael-a-maltese-073584/" aria-description="Citation for case: State v. Michael A. Maltese (073584)">Maltese</a></span></em>, and <em><span class="citation" data-id="9646552"><a href="/opinion/1520309/state-v-hartley/" aria-description="Citation for case: State v. Hartley">Hartley</a></span></em>. He notes that in the <em>Edwards</em> line of cases involving a suspect's invocation of his right to counsel, the Supreme Court suppresses statements elicited in the absence of counsel; no attenuation analysis is conducted.</p>
<p id="p-69">Amici ACLU and ACDL advance many of the same arguments as Wint. The ACLU contends that <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em>'s break-in-custody rule <a class="page-label" data-citation-index="2" data-label="191" href="#p191" id="p191">**191</a>applies to interrogated convicted inmates who are returned to the general prison population for fourteen days or longer but not to interrogated suspects awaiting indictment who are returned to pretrial detention rather than released into the community. According to the ACLU, <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em> made very clear that pretrial detention is different from post-conviction incarceration in an <em>Edwards</em> context. The ACDL argues that law enforcement would be given a perverse incentive if the longer a pre-indictment detainee is held in jail after invoking his right to counsel, the easier it becomes to continue to question him without counsel. Both the ACLU and ACDL point out New Jersey's strong and independent commitment to the privilege against self-incrimination, which is codified in N.J.S.A. 2A:84A-19 and N.J.R.E. 503, as well as our state-law jurisprudence.</p>
<p id="p-70">B.</p>
<p id="p-71">The State acknowledges that a defendant who is in pre-indictment custody and has invoked his right to counsel cannot be reinterrogated until an attorney is provided unless the defendant reinitiates contact with the police or a break in custody of at least fourteen days occurs. The State, however, asserts that "[Wint] only conditionally invoked his right to counsel initially." According to the State, Wint's verbal exchanges with the Pennsylvania detectives indicated that Wint wanted an attorney present if the detectives intended to take a statement from him in Camden but that "he would freely speak with [them] once he was transported back to Pennsylvania." The State takes the position that Wint initiated contact with the Pennsylvania detectives because "on two occasions over the course of three months, [he] told [those] detectives he would talk with them when he was brought to Pennsylvania."</p>
<p id="p-72">The State, moreover, maintains that "a six-month break in <em>Miranda</em> custody" occurred <a class="page-label" data-citation-index="1" data-label="973" href="#p973" id="p973">*973</a>between the attempted interrogations in Camden, where defendant invoked his right to counsel, and the interrogation in Warminster, where defendant waived his rights <a class="page-label" data-citation-index="2" data-label="192" href="#p192" id="p192">**192</a>and gave a voluntary statement. The State rejects the proposition that "the <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em> break-in-custody analysis applies <em>only</em> to prisoners who are serving a sentence upon conviction, and <em>never</em> to pre-trial detainees."</p>
<p id="p-73">In the State's view, the question posed by <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em> is not whether Wint had the opportunity "to return to the normalcy of his pre-arrest life outside of prison," but rather whether Wint's return to jail "following the initial interrogation represented the same sort of 'return to normalcy' experienced by Shatzer after his initial interrogation" and return to the general prison population. The State answers that question by stressing that Wint was simply subject to the ordinary restrictions of daily life in the county jail during his six-month detention and not to "the sort of coercive pressures inherent in 'interrogative custody' that <em>Miranda</em> and <em>Edwards</em> are meant to deflect," citing <em>Shatzer</em>, <extracted-citation case-ids="3582023" index="34" url="https://cite.case.law/us/559/98/#p109">559 U.S. at </extracted-citation>113 n.8, <extracted-citation case-ids="3582023" index="35" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>. Accordingly, the State contends that if Shatzer's return to the general prison population after his interrogation constituted a break in custody, so too does Wint's return to the county jail population.</p>
<p id="p-74">The State therefore asks this Court to reverse the Appellate Division's remand for a break-in-custody and attenuation analysis and affirm Wint's convictions.</p>
<p id="p-75">III.</p>
<p id="p-76">A.</p>
<p id="p-77">One of the fundamental guarantees of the United States Constitution and our state law is that no person can be compelled to be a witness against himself in a criminal case. <em>See</em> <em>U.S. Const.</em> amend. V ("No person ... shall be compelled in any criminal case to be a witness against himself ....");<footnotemark>4</footnotemark> N.J.S.A. 2A:84A-19 ("[E]very <a class="page-label" data-citation-index="2" data-label="193" href="#p193" id="p193">**193</a>natural person has a right to refuse to disclose in an action or to a police officer or other official any matter that will incriminate him or expose him to a penalty or a forfeiture of his estate ...."); N.J.R.E. 503 (same as N.J.S.A. 2A:84A-19 ).</p>
<p id="p-78">In the landmark case of <em>Miranda v. Arizona</em>, the United States Supreme Court imposed safeguards to enable an individual to exercise meaningfully the right against self-incrimination when interrogated while in police custody. <extracted-citation case-ids="12046400" index="36" url="https://cite.case.law/us/384/436/#p477"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U.S. 436</a></span></extracted-citation>, 477, <extracted-citation case-ids="12046400" index="37" url="https://cite.case.law/us/384/436/#p477"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602</a></span></extracted-citation>, <extracted-citation case-ids="12046400" index="38" url="https://cite.case.law/us/384/436/#p477"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L.Ed.2d 694</a></span></extracted-citation> (1966). To counteract the inherent psychological pressures that might compel a person subject to a custodial interrogation "to speak where he would not otherwise do so freely," the Court mandated that the police advise a suspect of certain basic rights. <em><extracted-citation case-ids="12046400" index="39" url="https://cite.case.law/us/384/436/#p477">Id.</extracted-citation></em><extracted-citation case-ids="12046400" index="39" url="https://cite.case.law/us/384/436/#p477"> at 467, 479</extracted-citation>, <extracted-citation case-ids="12046400" index="40" url="https://cite.case.law/us/384/436/#p477"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602</a></span></extracted-citation>. Before questioning a suspect during a custodial interrogation, the police must warn him that</p>
<blockquote id="p-79">he has the right to remain silent, that anything he says can be used against him in a court of law, that he has <em>the right to the presence of an attorney</em>, and that if he cannot afford an attorney one will be appointed for him prior to any questioning if he so desires.</blockquote>
<blockquote id="p-80">[ <em><extracted-citation case-ids="12046400" index="41" url="https://cite.case.law/us/384/436/#p477"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12046400" index="41" url="https://cite.case.law/us/384/436/#p477"> at 479</extracted-citation>, <extracted-citation case-ids="12046400" index="42" url="https://cite.case.law/us/384/436/#p477"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602</a></span></extracted-citation> (emphasis added).]</blockquote>
<p id="p-81"><em>Miranda</em> further instructed that "[i]f the individual states that he wants an attorney, <em>the interrogation must cease until an attorney is present</em>."</p>
<p id="p-82"><a class="page-label" data-citation-index="1" data-label="974" href="#p974" id="p974">*974</a><em><extracted-citation case-ids="12046400" index="43" url="https://cite.case.law/us/384/436/#p477"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12046400" index="43" url="https://cite.case.law/us/384/436/#p477"> at 474</extracted-citation>, <extracted-citation case-ids="12046400" index="44" url="https://cite.case.law/us/384/436/#p477"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602</a></span></extracted-citation> (emphasis added). An individual who requests counsel must be given "an opportunity to confer with the attorney and to have him <em>present</em> during any subsequent questioning." <em><extracted-citation case-ids="12046400" index="45" url="https://cite.case.law/us/384/436/#p477"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></extracted-citation></em> (emphasis added). If the State fails to honor a defendant's exercise of the right to counsel, including the right to appointed counsel, "no evidence obtained as a result of interrogation can be used against him." <em><extracted-citation case-ids="12046400" index="46" url="https://cite.case.law/us/384/436/#p477"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12046400" index="46" url="https://cite.case.law/us/384/436/#p477"> at 479</extracted-citation>, <extracted-citation case-ids="12046400" index="47" url="https://cite.case.law/us/384/436/#p477"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602</a></span></extracted-citation>.</p>
<p id="p-83">In <em>Edwards v. Arizona</em>, the Supreme Court took additional steps to ensure that the right to counsel guaranteed in <em>Miranda</em> would not be circumvented. <extracted-citation case-ids="6187603" index="48" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U.S. 477</a></span></extracted-citation>, <extracted-citation case-ids="6187603" index="49" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">101 S.Ct. 1880</a></span></extracted-citation>. <em>Edwards</em> held that "when an accused has invoked his right to have counsel present during custodial interrogation, a valid waiver of that right cannot be established by showing only that he responded to further police-initiated custodial interrogation even if he has been <a class="page-label" data-citation-index="2" data-label="194" href="#p194" id="p194">**194</a>advised of his rights." <em><extracted-citation case-ids="6187603" index="50" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6187603" index="50" url="https://cite.case.law/us/451/477/#p484"> at 484</extracted-citation>, <extracted-citation case-ids="6187603" index="51" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">101 S.Ct. 1880</a></span></extracted-citation>. The Court further held that an accused, who has "expressed his desire to deal with the police only through counsel, is not subject to further interrogation by the authorities until counsel has been made available to him, unless the accused himself initiates further communication, exchanges, or conversations with the police." <em><extracted-citation case-ids="6187603" index="52" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6187603" index="52" url="https://cite.case.law/us/451/477/#p484"> at 484-85</extracted-citation>, <extracted-citation case-ids="6187603" index="53" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">101 S.Ct. 1880</a></span></extracted-citation>.</p>
<p id="p-84">In that case, the police arrested Edwards on charges of murder, robbery, and burglary. <em><extracted-citation case-ids="6187603" index="54" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6187603" index="54" url="https://cite.case.law/us/451/477/#p484"> at 478</extracted-citation>, <extracted-citation case-ids="6187603" index="55" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">101 S.Ct. 1880</a></span></extracted-citation>. After initially waiving his <em>Miranda</em> rights and speaking to the police at the stationhouse, Edwards said, "I want an attorney before making a deal," at which point the questioning ceased. <em><extracted-citation case-ids="6187603" index="56" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6187603" index="56" url="https://cite.case.law/us/451/477/#p484"> at 479</extracted-citation>, <extracted-citation case-ids="6187603" index="57" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">101 S.Ct. 1880</a></span></extracted-citation>. The next morning, two detectives visited Edwards in the county jail and advised him again of his <em>Miranda</em> rights, including his right to counsel. <em><extracted-citation case-ids="6187603" index="58" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Ibid.</a></span></extracted-citation></em> That time, Edwards waived his rights and confessed. <em><extracted-citation case-ids="6187603" index="59" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Ibid.</a></span></extracted-citation></em> The Supreme Court suppressed the confession because Edwards requested counsel at the first interrogation and did not initiate the meeting the next day with the detectives, and because the detectives questioned him without making counsel available to him at the second interrogation. <em><extracted-citation case-ids="6187603" index="60" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6187603" index="60" url="https://cite.case.law/us/451/477/#p484"> at 487</extracted-citation>, <extracted-citation case-ids="6187603" index="61" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">101 S.Ct. 1880</a></span></extracted-citation>.</p>
<p id="p-85">In <em>Arizona v. Roberson</em>, the Supreme Court elaborated on <em>Edwards</em> and made clear that once a suspect requests the presence of counsel during an interrogation relating to one investigation, neither the same nor another law enforcement agency may initiate a second interrogation, even one relating to a different investigation, without providing the suspect with the counsel he earlier requested. <extracted-citation case-ids="6222614" index="62" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/#677" aria-description="Citation for case: Arizona v. Roberson">486 U.S. at 677-78</a></span>, 687-88</extracted-citation>, <extracted-citation case-ids="6222614" index="63" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">108 S.Ct. 2093</a></span></extracted-citation>. In <em><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">Roberson</a></span></em>, the defendant was arrested for burglary, advised of his <em>Miranda</em> rights, and told the arresting officer that he "wanted a lawyer before answering any questions." <em><extracted-citation case-ids="6222614" index="64" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6222614" index="64" url="https://cite.case.law/us/486/675/#p686"> at 678</extracted-citation>, <extracted-citation case-ids="6222614" index="65" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">108 S.Ct. 2093</a></span></extracted-citation>. Three days later, a different officer, unaware that the defendant earlier requested the assistance of counsel, interrogated the defendant about another burglary. <em><extracted-citation case-ids="6222614" index="66" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">Ibid.</a></span></extracted-citation></em> That time, despite being informed <a class="page-label" data-citation-index="2" data-label="195" href="#p195" id="p195">**195</a>that he had the right to counsel, the defendant made an incriminating statement. <em><extracted-citation case-ids="6222614" index="67" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">Ibid.</a></span></extracted-citation></em></p>
<p id="p-86">The Supreme Court affirmed the suppression of the statement. <em><extracted-citation case-ids="6222614" index="68" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6222614" index="68" url="https://cite.case.law/us/486/675/#p686"> at 688</extracted-citation>, <extracted-citation case-ids="6222614" index="69" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">108 S.Ct. 2093</a></span></extracted-citation>. The Court explained its rationale: "[T]he presumption raised by a suspect's request for counsel -- that he considers himself unable to deal with the pressures of custodial interrogation without legal assistance -- does not disappear simply because the police have approached the suspect, still in custody, still without counsel, about a separate investigation." <em><extracted-citation case-ids="6222614" index="70" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6222614" index="70" url="https://cite.case.law/us/486/675/#p686"> at 683</extracted-citation>, <extracted-citation case-ids="6222614" index="71" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">108 S.Ct. 2093</a></span></extracted-citation>. Moreover, when the suspect requests the presence of an attorney to deal with the inherent pressures of his custodial status, "there is no reason to assume that a suspect's state of mind is in any way investigation-specific." <em><extracted-citation case-ids="6222614" index="72" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6222614" index="72" url="https://cite.case.law/us/486/675/#p686"> at 684</extracted-citation>, <extracted-citation case-ids="6222614" index="73" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">108 S.Ct. 2093</a></span></extracted-citation>. The obligation <a class="page-label" data-citation-index="1" data-label="975" href="#p975" id="p975">*975</a>is on the law enforcement officers seeking to reinterrogate a suspect to inquire whether he had earlier invoked the right to counsel. <em><extracted-citation case-ids="6222614" index="74" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6222614" index="74" url="https://cite.case.law/us/486/675/#p686"> at 687-88</extracted-citation>, <extracted-citation case-ids="6222614" index="75" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">108 S.Ct. 2093</a></span></extracted-citation>. Although nothing prevents a law enforcement agency from advising a suspect that he is the subject of separate investigations, if the suspect has earlier requested the assistance of counsel and not initiated discussions with the authorities, he "can determine how to deal with the separate investigations with counsel's advice." <em><extracted-citation case-ids="6222614" index="76" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6222614" index="76" url="https://cite.case.law/us/486/675/#p686"> at 687</extracted-citation>, <extracted-citation case-ids="6222614" index="77" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">108 S.Ct. 2093</a></span></extracted-citation>.</p>
<p id="p-87">The Court in <em><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">Roberson</a></span></em> distinguished the bright line barring a subsequent interrogation in a case where the suspect has invoked his right to counsel from a case where the suspect has merely decided to cut off questioning, as in <em>Mosley</em>, <extracted-citation case-ids="6175104" index="78" url="https://cite.case.law/us/423/96/"><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">423 U.S. at 103</a></span>-04</extracted-citation>, <extracted-citation case-ids="6175104" index="79" url="https://cite.case.law/us/423/96/"><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">96 S.Ct. 321</a></span></extracted-citation>. <em>Roberson</em>, <extracted-citation case-ids="6222614" index="80" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">486 U.S. at 682</a></span>-83</extracted-citation>, <extracted-citation case-ids="6222614" index="81" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">108 S.Ct. 2093</a></span></extracted-citation>. The request for counsel, unlike the decision to remain silent, "raise[s] the presumption that [the suspect] is unable to proceed without a lawyer's advice." <em><extracted-citation case-ids="6222614" index="82" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6222614" index="82" url="https://cite.case.law/us/486/675/#p686"> at 683</extracted-citation>, <extracted-citation case-ids="6222614" index="83" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">108 S.Ct. 2093</a></span></extracted-citation>. Last, the Court reaffirmed the benefits of the "clear and unequivocal" guidelines provided by the <em>Edwards</em> rule: The police and prosecutors are given specific instructions on how to conduct custodial interrogations and know that the failure to follow those instructions will <a class="page-label" data-citation-index="2" data-label="196" href="#p196" id="p196">**196</a>result in suppression of otherwise "trustworthy and highly probative evidence." <em><extracted-citation case-ids="6222614" index="84" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6222614" index="84" url="https://cite.case.law/us/486/675/#p686"> at 681-82</extracted-citation>, <extracted-citation case-ids="6222614" index="85" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">108 S.Ct. 2093</a></span></extracted-citation>.</p>
<p id="p-88"><em>Minnick v. Mississippi</em> further fortified <em>Miranda</em>'s and <em>Edwards</em>'s focus on the importance of the actual presence of counsel at a custodial interrogation when a suspect invokes his right to counsel. <extracted-citation case-ids="6220774" index="86" url="https://cite.case.law/us/498/146/#p153"><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">498 U.S. at 152</a></span>-53</extracted-citation>, <extracted-citation case-ids="6220774" index="87" url="https://cite.case.law/us/498/146/#p153"><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">111 S.Ct. 486</a></span></extracted-citation>. The Court held "that when counsel is requested, interrogation must cease, and officials may not reinitiate interrogation without counsel present, whether or not the accused has consulted with his attorney." <em><extracted-citation case-ids="6220774" index="88" url="https://cite.case.law/us/498/146/#p153"><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6220774" index="88" url="https://cite.case.law/us/498/146/#p153"> at 153</extracted-citation>, <extracted-citation case-ids="6220774" index="89" url="https://cite.case.law/us/498/146/#p153"><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">111 S.Ct. 486</a></span></extracted-citation>. The Court stressed that the presence of counsel is not a mere procedural formality but a safeguard to ensure that the "police interrogation conform[s] to the dictates of the [Fifth Amendment]" and "that statements made in the government-established atmosphere are not the product of compulsion." <em><extracted-citation case-ids="6220774" index="90" url="https://cite.case.law/us/498/146/#p153"><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6220774" index="90" url="https://cite.case.law/us/498/146/#p153"> at 152</extracted-citation>, <extracted-citation case-ids="6220774" index="91" url="https://cite.case.law/us/498/146/#p153"><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">111 S.Ct. 486</a></span></extracted-citation> (second alteration in original) (quoting <em>Miranda</em>, <extracted-citation case-ids="12046400" index="92" url="https://cite.case.law/us/384/436/#p477"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U.S. at 466</a></span></extracted-citation>, <extracted-citation case-ids="12046400" index="93" url="https://cite.case.law/us/384/436/#p477"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602</a></span></extracted-citation> ). Thus, the Court "decline[d] to remove protection from police-initiated questioning based on isolated consultations with counsel who is absent when the interrogation resumes." <em>Id.</em> at 154, <extracted-citation case-ids="6220774" index="94" url="https://cite.case.law/us/498/146/#p153"><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">111 S.Ct. 486</a></span></extracted-citation>.</p>
<p id="p-89">B.</p>
<p id="p-90">In <em>Maryland v. Shatzer</em>, the Supreme Court announced a break-in-custody exception to the <em>Edwards</em> rule, which presumes that, after a defendant invokes his right to counsel, any statement taken during a subsequent custodial interrogation without counsel is not voluntary. <extracted-citation case-ids="3582023" index="95" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">559 U.S. at 104</a></span>-05</extracted-citation>, <extracted-citation case-ids="3582023" index="96" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>. What constitutes a break in custody is hotly debated between the parties in the present case. The United States Supreme Court has never explicitly placed any temporal limits on the <em>Edwards</em> rule when a statement is the product of a police-initiated interrogation of a defendant who earlier invoked his right to counsel and who remains in continuous pre-indictment, pretrial custody. The question is whether, in the circumstances of the present case, <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em> opened the door to police-initiated questioning of a pre-indictment, pretrial detainee in the absence of counsel.</p>
<p id="p-91"><a class="page-label" data-citation-index="2" data-label="197" href="#p197" id="p197">**197</a>In <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em>, a township police detective investigating allegations that Shatzer had sexually abused his son sought to interview Shatzer, who was imprisoned in a state correctional institution on an unrelated offense. <em><extracted-citation case-ids="3582023" index="97" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Id.</a></span></extracted-citation></em><extracted-citation case-ids="3582023" index="97" url="https://cite.case.law/us/559/98/#p109"> at 100-01</extracted-citation>, <extracted-citation case-ids="3582023" index="98" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>. The detective read Shatzer his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></em> rights, and after a short colloquy, Shatzer <a class="page-label" data-citation-index="1" data-label="976" href="#p976" id="p976">*976</a>declined to speak without an attorney, ending the interview. <em><extracted-citation case-ids="3582023" index="99" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span></extracted-citation></em><extracted-citation case-ids="3582023" index="99" url="https://cite.case.law/us/559/98/#p109"> at 101</extracted-citation>, <extracted-citation case-ids="3582023" index="100" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>. Two-and-a-half years later, another detective from the same police department, armed with more specific information, visited a correctional institution to interview Shatzer. <em><extracted-citation case-ids="3582023" index="101" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Ibid.</a></span></extracted-citation></em> The detective explained the allegations to Shatzer, read him his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></em> rights, and secured a written waiver of those rights. <em><extracted-citation case-ids="3582023" index="102" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></extracted-citation></em> During the interview, Shatzer made an incriminating statement. <em><extracted-citation case-ids="3582023" index="103" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span></extracted-citation></em><extracted-citation case-ids="3582023" index="103" url="https://cite.case.law/us/559/98/#p109"> at 101-02</extracted-citation>, <extracted-citation case-ids="3582023" index="104" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>. At no point did Shatzer request to speak with an attorney. <em><extracted-citation case-ids="3582023" index="105" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Id.</a></span></extracted-citation></em><extracted-citation case-ids="3582023" index="105" url="https://cite.case.law/us/559/98/#p109"> at 102</extracted-citation>, <extracted-citation case-ids="3582023" index="106" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>. Five days later, the interrogating detective and another detective returned to the correctional institution. <em><extracted-citation case-ids="3582023" index="107" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Ibid.</a></span></extracted-citation></em> Shatzer again waived his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></em> rights and made a further inculpatory statement, after which he requested counsel and the interrogation ceased. <em><extracted-citation case-ids="3582023" index="108" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></extracted-citation></em></p>
<p id="p-92">The Supreme Court held that <em>Edwards</em> did not mandate suppression of Shatzer's incriminating statements because, after his first interrogation, Shatzer experienced a break in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></em> custody by returning to the general prison population and because the second round of interrogations occurred more than two-and-a-half years later. <em><extracted-citation case-ids="3582023" index="109" url="https://cite.case.law/us/559/98/#p109">Id.</extracted-citation></em><extracted-citation case-ids="3582023" index="109" url="https://cite.case.law/us/559/98/#p109"> at 114, 116-17</extracted-citation>, <extracted-citation case-ids="3582023" index="110" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>. The Court maintained that a break in custody means different things for pretrial detainees and prison inmates. <em><extracted-citation case-ids="3582023" index="111" url="https://cite.case.law/us/559/98/#p109">Id.</extracted-citation></em><extracted-citation case-ids="3582023" index="111" url="https://cite.case.law/us/559/98/#p109"> at 106-07, 112-14</extracted-citation>, <extracted-citation case-ids="3582023" index="112" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>.</p>
<p id="p-93">In the case of a suspect who is "arrested for a particular crime and is held in uninterrupted pretrial custody while that crime is being actively investigated[,] ... he remains cut off from his normal life and companions, 'thrust into' and isolated in an 'unfamiliar,' 'police-dominated atmosphere,' where his captors 'appear to control [his] fate.' " <em><extracted-citation case-ids="3582023" index="113" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Id.</a></span></extracted-citation></em><extracted-citation case-ids="3582023" index="113" url="https://cite.case.law/us/559/98/#p109"> at 106</extracted-citation>, <extracted-citation case-ids="3582023" index="114" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation> (third alteration in original) (first quoting <em>Miranda</em>, <extracted-citation case-ids="12046400" index="115" url="https://cite.case.law/us/384/436/#p477"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U.S. at 456</a></span>-57</extracted-citation>, <extracted-citation case-ids="12046400" index="116" url="https://cite.case.law/us/384/436/#p477"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602</a></span></extracted-citation> ; then quoting <a class="page-label" data-citation-index="2" data-label="198" href="#p198" id="p198">**198</a><em>Illinois v. Perkins</em>, <extracted-citation case-ids="12122654" index="117" url="https://cite.case.law/us/496/292/#p297"><span class="citation" data-id="9432050"><a href="/opinion/112452/illinois-v-perkins/" aria-description="Citation for case: Illinois v. Perkins">496 U.S. 292</a></span></extracted-citation>, 297, <extracted-citation case-ids="12122654" index="118" url="https://cite.case.law/us/496/292/#p297"><span class="citation" data-id="9432050"><a href="/opinion/112452/illinois-v-perkins/" aria-description="Citation for case: Illinois v. Perkins">110 S.Ct. 2394</a></span></extracted-citation>, <extracted-citation case-ids="12122654" index="119" url="https://cite.case.law/us/496/292/#p297"><span class="citation" data-id="9432050"><a href="/opinion/112452/illinois-v-perkins/" aria-description="Citation for case: Illinois v. Perkins">110 L.Ed.2d 243</a></span></extracted-citation> (1990) ). That was the scenario faced by the defendants in <em>Edwards</em>, <em><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">Roberson</a></span></em>, and <em>Minnick</em> because none of those defendants "regained a sense of control or normalcy after they were initially taken into custody for the crime under investigation." <em>Id.</em> at 106-07, <extracted-citation case-ids="3582023" index="120" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>. The "continued detention [of those defendants] rested with those controlling their interrogation, and [<em>they] confronted the uncertainties of what final charges they would face, whether they would be convicted, and what sentence they would receive</em>." <em><extracted-citation case-ids="3582023" index="121" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Id.</a></span></extracted-citation></em><extracted-citation case-ids="3582023" index="121" url="https://cite.case.law/us/559/98/#p109"> at 114</extracted-citation>, <extracted-citation case-ids="3582023" index="122" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation> (emphasis added).</p>
<p id="p-94">The <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em> Court explained, however, that when "a suspect has been released from his <em>pretrial custody</em> and has returned to his normal life for some time before the later attempted interrogation, there is little reason to think that his change of heart regarding interrogation without counsel has been coerced." <em><extracted-citation case-ids="3582023" index="123" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Id.</a></span></extracted-citation></em><extracted-citation case-ids="3582023" index="123" url="https://cite.case.law/us/559/98/#p109"> at 107</extracted-citation>, <extracted-citation case-ids="3582023" index="124" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation> (emphasis added). In that situation, the suspect "has no longer been isolated. He has likely been able to seek advice from an attorney, family members, and friends. And he knows from his earlier experience that he need only demand counsel to bring the interrogation to a halt; and that investigative custody does not last indefinitely." <em><extracted-citation case-ids="3582023" index="125" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Id.</a></span></extracted-citation></em><extracted-citation case-ids="3582023" index="125" url="https://cite.case.law/us/559/98/#p109"> at 107-08</extracted-citation>, <extracted-citation case-ids="3582023" index="126" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation> (footnote omitted). The Court concluded that "an extension of <em>Edwards</em> is not justified ... when a suspect who initially requested counsel is reinterrogated after a break in custody that is of sufficient duration to dissipate its coercive effects." <em><extracted-citation case-ids="3582023" index="127" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Id.</a></span></extracted-citation></em><extracted-citation case-ids="3582023" index="127" url="https://cite.case.law/us/559/98/#p109"> at 109</extracted-citation>, <extracted-citation case-ids="3582023" index="128" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>. In that circumstance, the fresh administration of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></em> warnings when the suspect is reinterrogated is "deemed sufficient" to protect his constitutional right to counsel. <em><extracted-citation case-ids="3582023" index="129" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></extracted-citation></em></p>
<p id="p-95">The Court applied this paradigm to Shatzer, a convicted inmate, who, after his initial interrogation at which he invoked his right to counsel, was returned to the <a class="page-label" data-citation-index="1" data-label="977" href="#p977" id="p977">*977</a>general prison population where he remained for two-and-a-half years before detectives reinterrogated him. <em><extracted-citation case-ids="3582023" index="130" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span></extracted-citation></em><extracted-citation case-ids="3582023" index="130" url="https://cite.case.law/us/559/98/#p109"> at 112</extracted-citation>, <extracted-citation case-ids="3582023" index="131" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>. The Court ultimately determined that Shatzer's return to the general prison population qualified as a break in custody. <em><extracted-citation case-ids="3582023" index="132" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Id.</a></span></extracted-citation></em><extracted-citation case-ids="3582023" index="132" url="https://cite.case.law/us/559/98/#p109"> at 117</extracted-citation>, <extracted-citation case-ids="3582023" index="133" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>. It reached that conclusion because, in its view, "<em>lawful imprisonment imposed</em> <a class="page-label" data-citation-index="2" data-label="199" href="#p199" id="p199">**199</a><em>upon conviction of a crime</em> does not create the coercive pressures identified in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></em>." <em><extracted-citation case-ids="3582023" index="134" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span></extracted-citation></em><extracted-citation case-ids="3582023" index="134" url="https://cite.case.law/us/559/98/#p109"> at 113</extracted-citation>, <extracted-citation case-ids="3582023" index="135" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation> (emphasis added). The Court gave the following rationale for considering a convicted inmate's return to the general prison population a break in custody:</p>
<blockquote id="p-96">Interrogated suspects who have previously been convicted of crime live in prison. When they are released back into the general prison population, they return to their accustomed surroundings and daily routine -- they regain the degree of control they had over their lives prior to the interrogation. Sentenced prisoners, in contrast to the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></em> paradigm, are not isolated with their accusers. They live among other inmates, guards, and workers, and often can receive visitors and communicate with people on the outside by mail or telephone.</blockquote>
<blockquote id="p-97">Their detention, moreover, is relatively disconnected from their prior unwillingness to cooperate in an investigation. The former interrogator has no power to increase the duration of incarceration, which was determined at sentencing.</blockquote>
<blockquote id="p-98">[ <em><extracted-citation case-ids="3582023" index="136" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span></extracted-citation></em><extracted-citation case-ids="3582023" index="136" url="https://cite.case.law/us/559/98/#p109"> at 113</extracted-citation>, <extracted-citation case-ids="3582023" index="137" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>.]</blockquote>
<p id="p-99">The Court adopted a bright-line rule for determining when a break in custody is of adequate length to overcome the <em>Edwards</em> presumption of involuntariness attaching to a police-initiated reinterrogation of a suspect who earlier has requested counsel. <em><extracted-citation case-ids="3582023" index="138" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Id.</a></span></extracted-citation></em><extracted-citation case-ids="3582023" index="138" url="https://cite.case.law/us/559/98/#p109"> at 109-10</extracted-citation>, <extracted-citation case-ids="3582023" index="139" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>. A break in custody of fourteen days, the Court held, is sufficient "time for the suspect to get reacclimated to his normal life, to consult with friends and counsel, and to shake off any residual coercive effects of his prior custody." <em><extracted-citation case-ids="3582023" index="140" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Id.</a></span></extracted-citation></em><extracted-citation case-ids="3582023" index="140" url="https://cite.case.law/us/559/98/#p109"> at 110</extracted-citation>, <extracted-citation case-ids="3582023" index="141" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>. Because Shatzer's break in custody lasted two-and-a-half years, the incriminating statements made at his reinterrogation were admissible. <em><extracted-citation case-ids="3582023" index="142" url="https://cite.case.law/us/559/98/#p109">Id.</extracted-citation></em><extracted-citation case-ids="3582023" index="142" url="https://cite.case.law/us/559/98/#p109"> at 110, 117</extracted-citation>, <extracted-citation case-ids="3582023" index="143" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>.</p>
<p id="p-100"><em>Shatzer</em> did not suggest that, for break-in-custody purposes, a convicted inmate returning to the general prison population is comparable to a pre-indictment, pretrial detainee returning to his jail cell. <em>See</em> <em>Howes v. Fields</em>, <extracted-citation case-ids="12186663" index="144" url="https://cite.case.law/us/565/499/#p510"><span class="citation" data-id="9485375"><a href="/opinion/623144/howes-v-fields/" aria-description="Citation for case: Howes v. Fields">565 U.S. 499</a></span></extracted-citation>, 510, <extracted-citation case-ids="12186663" index="145" url="https://cite.case.law/us/565/499/#p510"><span class="citation" data-id="9485375"><a href="/opinion/623144/howes-v-fields/" aria-description="Citation for case: Howes v. Fields">132 S.Ct. 1181</a></span></extracted-citation>, <extracted-citation case-ids="12186663" index="146" url="https://cite.case.law/us/565/499/#p510"><span class="citation" data-id="9485375"><a href="/opinion/623144/howes-v-fields/" aria-description="Citation for case: Howes v. Fields">182 L.Ed.2d 17</a></span></extracted-citation> (2012) (noting that <em>Shatzer</em>"held that a break in custody may occur while a suspect is serving a term in prison"). Indeed, in discussing the coercive effects of custodial interrogation in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></em> context, the Court in <em><span class="citation" data-id="9485375"><a href="/opinion/623144/howes-v-fields/" aria-description="Citation for case: Howes v. Fields">Howes</a></span></em> took pains to distinguish between convicted inmates on the one hand and pretrial detainees on the other. <em><extracted-citation case-ids="12186663" index="147" url="https://cite.case.law/us/565/499/#p510"><span class="citation" data-id="9485375"><a href="/opinion/623144/howes-v-fields/" aria-description="Citation for case: Howes v. Fields">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12186663" index="147" url="https://cite.case.law/us/565/499/#p510"> at 511-12</extracted-citation>, <extracted-citation case-ids="12186663" index="148" url="https://cite.case.law/us/565/499/#p510"><span class="citation" data-id="9485375"><a href="/opinion/623144/howes-v-fields/" aria-description="Citation for case: Howes v. Fields">132 S.Ct. 1181</a></span></extracted-citation> ("[A] prisoner, unlike a person who has not been convicted and sentenced, knows <a class="page-label" data-citation-index="2" data-label="200" href="#p200" id="p200">**200</a>that the law enforcement officers who question him probably lack the authority to affect the duration of his sentence." (citing <em>Shatzer</em>, <extracted-citation case-ids="3582023" index="149" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">559 U.S. at 103</a></span>-14</extracted-citation>, <extracted-citation case-ids="3582023" index="150" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation> ) ).</p>
<p id="p-101">Some courts, but not all, have concluded that <em>Shatzer</em> expressed the "view that sentenced prisoners are distinct from pretrial detainees for purposes of [the <em>Edwards</em> ] presumption of involuntariness." <em>United States v. Coles</em>, <extracted-citation case-ids="12266327" index="151" url="https://cite.case.law/f-supp-3d/264/667/#p683"><span class="citation" data-id="7244467"><a href="/opinion/7326553/united-states-v-coles/" aria-description="Citation for case: United States v. Coles">264 F.Supp.3d 667</a></span></extracted-citation>, 683 (M.D. Pa. 2017) (holding that pretrial detainee "did not experience a break in <em>Miranda</em> custody when he was returned to pretrial detention for 35 days between interrogations"); <em>Trotter v. United States</em>, <extracted-citation case-ids="6844305" index="152" url="https://cite.case.law/a3d/121/40/#p48"><span class="citation" data-id="2819362"><a href="/opinion/2819362/gregory-trotter-ernest-pee-v-united-states/" aria-description="Citation for case: Gregory Trotter &amp; Ernest Pee v. United States">121 A.3d 40</a></span></extracted-citation>, 48-49 (D.C. 2015) (holding that for <em>Shatzer</em> purposes five-month period between interrogations did not constitute break in custody for pretrial detainee).</p>
<p id="p-102"><a class="page-label" data-citation-index="1" data-label="978" href="#p978" id="p978">*978</a><em>But see</em> <em>Commonwealth v. Champney</em>, <extracted-citation case-ids="12317117" index="153" url="https://cite.case.law/a3d/161/265/#p284"><span class="citation" data-id="4163509"><a href="/opinion/4386256/commonwealth-v-champney/" aria-description="Citation for case: Commonwealth v. Champney">161 A.3d 265</a></span></extracted-citation>, 284 (Pa. Super. Ct. 2017) (holding that "the nearly five-month break between [pretrial detainee's] invocation of his right to counsel and the prison interrogation removed the <em>Edwards</em> presumption of involuntariness").</p>
<p id="p-103">IV.</p>
<p id="p-104">We now apply the legal principles developed in the <em>Edwards</em> line of cases to the facts before us.</p>
<p id="p-105">Wint faced separate murder charges in Camden County and Bucks County when police officers arrested him and took him to the Camden County Prosecutor's Office for questioning. Wint was placed in an interrogation room, where an investigator from the Camden County Prosecutor's Office proceeded to interview him as two Pennsylvania detectives watched from an adjacent room. After the investigator advised Wint of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></em> rights, Wint told him, "<em>I think I should call my lawyer</em>" and "I really don't want to talk to anybody." (emphasis added). The investigator then stopped the interview.</p>
<p id="p-106">Despite having observed Wint invoke his right to counsel and having been told about that invocation, the two Pennsylvania detectives entered the room to question Wint about the Pennsylvania <a class="page-label" data-citation-index="2" data-label="201" href="#p201" id="p201">**201</a>murder charge. That attempt by the Pennsylvania detectives to interrogate Wint about their investigation, approximately three minutes after they knew he had unequivocally requested counsel, was a clear violation of <em>Edwards</em>. <em>See</em> <em>Roberson</em>, <extracted-citation case-ids="6222614" index="154" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/#677" aria-description="Citation for case: Arizona v. Roberson">486 U.S. at 677-78</a></span>, 687-88</extracted-citation>, <extracted-citation case-ids="6222614" index="155" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">108 S.Ct. 2093</a></span></extracted-citation> (stating that when defendant requests counsel during interrogation by one law enforcement agency, another law enforcement agency may not initiate second interrogation relating to another investigation); <em>see also</em> <em>McNeil v. Wisconsin</em>, <extracted-citation case-ids="1108476" index="156" url="https://cite.case.law/us/501/171/#p177"><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/" aria-description="Citation for case: McNeil v. Wisconsin">501 U.S. 171</a></span></extracted-citation>, 177, <extracted-citation case-ids="1108476" index="157" url="https://cite.case.law/us/501/171/#p177"><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/" aria-description="Citation for case: McNeil v. Wisconsin">111 S.Ct. 2204</a></span></extracted-citation>, <extracted-citation case-ids="1108476" index="158" url="https://cite.case.law/us/501/171/#p177"><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/" aria-description="Citation for case: McNeil v. Wisconsin">115 L.Ed.2d 158</a></span></extracted-citation> (1991) ("The <em>Edwards</em> rule ... is <em>not</em> offense specific: Once a suspect invokes the <em>Miranda</em> right to counsel for interrogation regarding one offense, he may not be reapproached regarding <em>any</em> offense unless counsel is present." (citing <em>Roberson</em>, <extracted-citation case-ids="6222614" index="159" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">486 U.S. at 675</a></span></extracted-citation>, <extracted-citation case-ids="6222614" index="160" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">108 S.Ct. 2093</a></span></extracted-citation> ) ). At that point, our constitutional jurisprudence required the detectives, as a precondition to any interrogation, to provide Wint with the attorney he requested. <em>See</em> <em>Roberson</em>, <extracted-citation case-ids="6222614" index="161" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">486 U.S. at 687</a></span></extracted-citation>, <extracted-citation case-ids="6222614" index="162" url="https://cite.case.law/us/486/675/#p686"><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">108 S.Ct. 2093</a></span></extracted-citation> ; <em>see also</em> <em>State v. Wright</em>, <extracted-citation case-ids="1383967" index="163" url="https://cite.case.law/nj/97/113/#p126"><span class="citation" data-id="1506424"><a href="/opinion/1506424/state-v-wright/" aria-description="Citation for case: State v. Wright">97 N.J. 113</a></span></extracted-citation>, 126, <extracted-citation index="164" url="https://cite.case.law/citations/?q=477%20A.2d%201265"><span class="citation" data-id="1506424"><a href="/opinion/1506424/state-v-wright/" aria-description="Citation for case: State v. Wright">477 A.2d 1265</a></span></extracted-citation> (1984).</p>
<p id="p-107">After the Pennsylvania detectives advised Wint of his right to the presence of a lawyer, Wint responded, "I want him to sit here while we talk." Wint repeated five more times that he did not want to answer questions without a lawyer, and then the detectives ceased the interrogation. With two sets of interrogating officers, Wint made clear that he wanted to avail himself of his constitutional right to counsel.</p>
<p id="p-108">The record does not support the trial court's finding that Wint <em>initiated</em> a conversation with the Pennsylvania detectives in which Wint agreed to speak with them at some later time without counsel. Like the Appellate Division, we cannot defer to factual findings that are not "supported by sufficient credible evidence in the record" and therefore are clearly mistaken. <em>State v. Elders</em>, <extracted-citation case-ids="3154660" index="165" url="https://cite.case.law/nj/192/224/#p243"><span class="citation" data-id="9757740"><a href="/opinion/2353203/state-v-elders/" aria-description="Citation for case: State v. Elders">192 N.J. 224</a></span></extracted-citation>, 243-44, <extracted-citation case-ids="3154660" index="166" url="https://cite.case.law/nj/192/224/#p243"><span class="citation" data-id="9757740"><a href="/opinion/2353203/state-v-elders/" aria-description="Citation for case: State v. Elders">927 A.2d 1250</a></span></extracted-citation> (2007) (citation omitted); <em>see also</em> <em>State v. S.S.</em>, <extracted-citation case-ids="12435418" index="167" url="https://cite.case.law/nj/229/360/#p381"><span class="citation" data-id="7331346"><a href="/opinion/7412006/state-v-ss/" aria-description="Citation for case: State v. S.S.">229 N.J. 360</a></span></extracted-citation>, 381, <extracted-citation case-ids="12435418" index="168" url="https://cite.case.law/nj/229/360/#p381"><span class="citation" data-id="7331346"><a href="/opinion/7412006/state-v-ss/" aria-description="Citation for case: State v. S.S.">162 A.3d 1058</a></span></extracted-citation> (2017).</p>
<p id="p-109"><a class="page-label" data-citation-index="2" data-label="202" href="#p202" id="p202">**202</a>Detective McDonough's testimony at the motion hearing left no doubt that the Pennsylvania detectives <em>initiated</em> a conversation with Wint as he left the interrogation room and stood in the hallway of the Camden County Prosecutor's Office. Undeterred, the detectives initiated a new colloquy by saying, "[W]hen we get back to Bucks County we can talk about this again." To that prompting, defendant responded, <a class="page-label" data-citation-index="1" data-label="979" href="#p979" id="p979">*979</a>mimicking their words, "Yeah, I'll talk to you when we get back to Bucks County." A similar exchange occurred three months later when the detectives visited Wint in the Camden County jail to secure a DNA sample. Again, according to Detective McDonough, the detectives initiated the conversation by saying to Wint they would talk with him after his transfer to Pennsylvania -- "when he got back to Bucks [County]" -- and Wint responded as he had earlier, "Yeah, I'll talk to you when I get back to Bucks." Based on the undisputed evidence before us, Wint did not "initiate[ ] further communication, exchanges, or conversations with the police" to open the door to an interrogation without counsel. <em>Edwards</em>, <extracted-citation case-ids="6187603" index="169" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U.S. at 485</a></span></extracted-citation>, <extracted-citation case-ids="6187603" index="170" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">101 S.Ct. 1880</a></span></extracted-citation> ; <em>see also</em> <em>State v. Alston</em>, <extracted-citation case-ids="4146725" index="171" url="https://cite.case.law/nj/204/614/#p620"><span class="citation" data-id="2551534"><a href="/opinion/2551534/state-v-alston/" aria-description="Citation for case: State v. Alston">204 N.J. 614</a></span></extracted-citation>, 620, <extracted-citation case-ids="4146725" index="172" url="https://cite.case.law/nj/204/614/#p620"><span class="citation" data-id="2551534"><a href="/opinion/2551534/state-v-alston/" aria-description="Citation for case: State v. Alston">10 A.3d 880</a></span></extracted-citation> (2011) (stating suspect must "initiate[ ] further communication sufficient to waive the right to counsel" (citing <em>Edwards</em>, <extracted-citation case-ids="6187603" index="173" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U.S. at 484</a></span>-85</extracted-citation>, <extracted-citation case-ids="6187603" index="174" url="https://cite.case.law/us/451/477/#p484"><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">101 S.Ct. 1880</a></span></extracted-citation> ) ).</p>
<p id="p-110">Wint remained in continuous pre-indictment, pretrial custody in the Camden County jail when he was transported to the Warminster police station in Pennsylvania where the same detectives -- who had interrogated him six months earlier when he had requested the presence of counsel -- interrogated him again without providing him with counsel. The detectives read Wint his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></em> rights, which this time he waived, and Wint made an incriminating admission -- one that he disputed at trial -- concerning the Camden County murder charge.</p>
<p id="p-111">We conclude that Wint did not experience a break in custody within the intendment of <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em> before he was interrogated without counsel in Pennsylvania, and therefore the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></em> presumption of involuntariness applies to the admission Wint made to <a class="page-label" data-citation-index="2" data-label="203" href="#p203" id="p203">**203</a>the detectives. For break-in-custody purposes, <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em> distinguished the very different worlds and circumstances of a pretrial detainee and a convicted inmate.</p>
<p id="p-112">A pre-indictment, pretrial detainee's status is conditional and of limited duration. Changed circumstances may result in his release from pretrial detention. Under the New Jersey Criminal Justice Reform Act, "[t]he eligible defendant shall not remain detained in jail for more than 90 days, not counting excludable time for reasonable delays ... , prior to the return of an indictment." N.J.S.A. 2A:162-22(a)(1)(a). As such, extended pre-indictment detainment should be the exception, not the rule. Indictment triggers the onset of the formal adversarial judicial process, which in turn entitles a defendant to the assistance of counsel under the Sixth Amendment, <em>Kirby v. Illinois</em>, <extracted-citation case-ids="6173132" index="175" url="https://cite.case.law/us/406/682/#p688"><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">406 U.S. 682</a></span></extracted-citation>, 688-89, <extracted-citation case-ids="6173132" index="176" url="https://cite.case.law/us/406/682/#p688"><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">92 S.Ct. 1877</a></span></extracted-citation>, <extracted-citation case-ids="6173132" index="177" url="https://cite.case.law/us/406/682/#p688"><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">32 L.Ed.2d 411</a></span></extracted-citation> (1972), as well as Article I, Paragraph 10 of the New Jersey Constitution, <em>State v. Sanchez</em>, <extracted-citation case-ids="1368422" index="178" url="https://cite.case.law/nj/129/261/#p274"><span class="citation" data-id="2309262"><a href="/opinion/2309262/state-v-sanchez/" aria-description="Citation for case: State v. Sanchez">129 N.J. 261</a></span></extracted-citation>, 274-78, <extracted-citation case-ids="1368422" index="179" url="https://cite.case.law/nj/129/261/#p274"><span class="citation" data-id="2309262"><a href="/opinion/2309262/state-v-sanchez/" aria-description="Citation for case: State v. Sanchez">609 A.2d 400</a></span></extracted-citation> (1992). "[A]fter the return of an indictment, prosecutors and their representatives should not initiate conversations with an uncounselled defendant." <em><extracted-citation case-ids="1368422" index="180" url="https://cite.case.law/nj/129/261/#p274"><span class="citation" data-id="2309262"><a href="/opinion/2309262/state-v-sanchez/" aria-description="Citation for case: State v. Sanchez">Id.</a></span></extracted-citation></em><extracted-citation case-ids="1368422" index="180" url="https://cite.case.law/nj/129/261/#p274"> at 277</extracted-citation>, <extracted-citation case-ids="1368422" index="181" url="https://cite.case.law/nj/129/261/#p274"><span class="citation" data-id="2309262"><a href="/opinion/2309262/state-v-sanchez/" aria-description="Citation for case: State v. Sanchez">609 A.2d 400</a></span></extracted-citation>.<footnotemark>5</footnotemark> If returning a pre-indictment detainee to the county jail after he has requested counsel during an interrogation counted as a break in custody, then the prosecutor might have a perverse incentive to delay an indictment's return to allow repeated attempts to interrogate a defendant every couple of weeks.</p>
<p id="p-113">During the pre-indictment period, a pretrial detainee remains in custody while his criminal charges are under investigation, and his interrogators appear to control his fate, including the final charges he might <a class="page-label" data-citation-index="1" data-label="980" href="#p980" id="p980">*980</a>face and the sentence he might receive if convicted. <em>See</em> <em>Shatzer</em>, <extracted-citation case-ids="3582023" index="182" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/#106" aria-description="Citation for case: Maryland v. Shatzer">559 U.S. at 106</a></span>, 114</extracted-citation>, <extracted-citation case-ids="3582023" index="183" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>. During this time, "he remains cut off from his normal life and companions, [and] 'thrust</p>
<p id="p-114">into' and isolated in an 'unfamiliar,' 'police-dominated atmosphere.' " <em><extracted-citation case-ids="3582023" index="184" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Id.</a></span></extracted-citation></em><extracted-citation case-ids="3582023" index="184" url="https://cite.case.law/us/559/98/#p109"> at 106</extracted-citation>, <extracted-citation case-ids="3582023" index="185" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation> (quoting <em>Miranda</em>, <extracted-citation case-ids="12046400" index="186" url="https://cite.case.law/us/384/436/#p477"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U.S. at 456</a></span>-57</extracted-citation>, <extracted-citation case-ids="12046400" index="187" url="https://cite.case.law/us/384/436/#p477"><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602</a></span></extracted-citation> ). When a pretrial detainee is released into the free world he experiences a break in custody. <em>Id.</em> at 110, <extracted-citation case-ids="3582023" index="188" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>. He is no longer "isolated," he returns "to his normal life for some time before the later attempted interrogation," he is "able to seek advice from an attorney, family members, and friends," and "he knows from his earlier experience that he need only demand counsel to bring the interrogation to a halt." <em><extracted-citation case-ids="3582023" index="189" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Id.</a></span></extracted-citation></em><extracted-citation case-ids="3582023" index="189" url="https://cite.case.law/us/559/98/#p109"> at 107-08</extracted-citation>, <extracted-citation case-ids="3582023" index="190" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation> ; <em>see also</em> <em>State v. Wessells</em>, <extracted-citation case-ids="4153113" index="191" url="https://cite.case.law/nj/209/395/#p413"><span class="citation" data-id="7328622"><a href="/opinion/7409342/state-v-wessells/" aria-description="Citation for case: State v. Wessells">209 N.J. 395</a></span></extracted-citation>, 413, <extracted-citation case-ids="4153113" index="192" url="https://cite.case.law/nj/209/395/#p413"><span class="citation" data-id="7328622"><a href="/opinion/7409342/state-v-wessells/" aria-description="Citation for case: State v. Wessells">37 A.3d 1122</a></span></extracted-citation> (2012) (holding that nine days in community was insufficient break in custody to dissipate coercive taint of initial interrogation).</p>
<p id="p-115">As <em><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">Shatzer</a></span></em> explained, convicted inmates stand in a very different position because their world is prison. After they are interrogated, "they are released back into the general prison population," where "they return to their accustomed surroundings and daily routine," and where "they regain the degree of control they had over their lives prior to the interrogation." <extracted-citation case-ids="3582023" index="193" url="https://cite.case.law/us/559/98/#p109"><span class="citation" data-id="9413177"><a href="/opi

[...TRUNCATED 19599 of 139599 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Steagald v. United States.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Steagald v. United States"
type: case
citation: "451 U.S. 204 (1981)"
parallel_cite: "101 S. Ct. 1642; 68 L. Ed. 2d 38; 49 U.S.L.W. 4418"
neutral_cite: 1981 U.S. LEXIS 89
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1981
date_decided: 1981-04-21
docket: 79-6777
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1981-04-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Steagald v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110464/steagald-v-united-states/"
  cluster_id: 110464
  opinion_id: 9428299
  identity_checked: true
homes:
  - page: "[[Arrest in the Home]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Entry to Arrest]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Securing the Scene]]"
    role: "Related (cross-doctrine)"
related: ["[[Payton v. New York]]", "[[Bailey v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "arrest-warrant", "search-warrant", "third-party-home"]
holding: "To search a THIRD PARTY'S home for the subject of an arrest warrant, police need a SEARCH warrant (absent exigency or consent); an…"
lake:
  record_id: Steagald v. United States
  status: verified
  projected_at: 2026-07-06
---

# Steagald v. United States

*451 U.S. 204 (1981)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Armed with an arrest warrant for fugitive Ricky Lyons, DEA agents entered and searched Steagald's home—where they believed Lyons might be found—without a search warrant and without Steagald's consent. They did not find Lyons but found cocaine, and Steagald, who was not named in the arrest warrant, was convicted.

## Issue
Whether an arrest warrant for one person justifies entering and searching a third party's home, without that person's consent and absent [[Exigent Circumstances and Hot Pursuit|exigent circumstances]], to look for the subject of the arrest warrant.

## Rule
An arrest warrant does not authorize searching a third party's home. "The issue in this case is whether, under the Fourth Amendment, a law enforcement officer may legally search for the subject of an arrest warrant in the home of a third party without first obtaining a search warrant. Concluding that a search warrant must be obtained absent exigent circumstances or consent, we reverse ...." — 451 U.S. at 205–206. ^pin-205

## Application
The agents held only an arrest warrant for Lyons, which protected Lyons's interests but did nothing to protect Steagald's privacy in his own home. Absent [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] or consent, the agents needed a search warrant to enter Steagald's home to look for Lyons; because they had none, the search violated Steagald's Fourth Amendment rights and the evidence against him should have been suppressed.

## Conclusion
A search warrant was required to search the third party's home for the subject of the arrest warrant; the judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Companion to [[Payton v. New York]] (an arrest warrant suffices to enter the suspect's own home to arrest him); the related authority to detain occupants incident to a premises search is bounded in [[Bailey v. United States]].

## Appears on
- [[Arrest in the Home]] — *Key — Progeny / Refinement*
- [[Entry to Arrest]] — *Key — Progeny / Refinement*
- [[Securing the Scene]] — *Related (cross-doctrine)*

## Sources
- *Steagald v. United States*, 451 U.S. 204 (1981) — https://www.courtlistener.com/opinion/110464/steagald-v-united-states/ — pinpoint: 205–206.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6539d5ff8aba7712", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Steagald v. United States"}, "payload": {"all": [{"cite": "451 U.S. 204", "page": "204", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "451"}, {"cite": "101 S. Ct. 1642", "page": "1642", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "101"}, {"cite": "68 L. Ed. 2d 38", "page": "38", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "68"}, {"cite": "1981 U.S. LEXIS 89", "page": "89", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1981"}, {"cite": "49 U.S.L.W. 4418", "page": "4418", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "49"}], "display": "451 U.S. 204", "official": {"cite": "451 U.S. 204", "page": "204", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "451"}, "official_selection_present": true, "record_id": "Steagald v. United States"}}
{"assertion_id": "8956cf805a2d31c1", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-205", "record_id": "Steagald v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-205", "pinpoint_status": "slip-only", "quote": "--- # Steagald v. United States *451 U.S. 204 (1981)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Armed with an arrest warrant for fugitive Ricky Lyons, DEA agents entered and searched Steagald's home—where they believed Lyons might be found—without a search warrant and without Steagald's consent. They did not find Lyons but found cocaine, and Steagald, who was not named in the arrest warrant, was convicted. ## Issue Whether an arrest warrant for one person justifies entering and searching a third party's home, without that person's consent and absent exigent circumstances, to look for the subject of the arrest warrant. ## Rule An arrest warrant does not authorize searching a third party's home.", "quote_fidelity": "mismatch", "record_id": "Steagald v. United States", "star_marker": null}}
{"assertion_id": "cf8e6d3cf5e8f47f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Steagald v. United States"}, "payload": {"as_of_content": "1981-04-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Steagald v. United States", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Steagald v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Steagald v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Steagald v. United States",
    "case_name_short": "Steagald",
    "case_name_full": "Steagald v. United States",
    "input_case_name": "Steagald v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1981-04-21",
    "year": 1981,
    "docket": "79-6777",
    "cluster_id": 110464,
    "lead_opinion_id": 9428299,
    "sibling_ids": [
      110464,
      9428299,
      9428300
    ],
    "absolute_url": "/opinion/110464/steagald-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "451 U.S. 204",
      "volume": "451",
      "reporter": "U.S.",
      "page": "204",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "101 S. Ct. 1642",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "1642",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 L. Ed. 2d 38",
        "volume": "68",
        "reporter": "L. Ed. 2d",
        "page": "38",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 U.S.L.W. 4418",
        "volume": "49",
        "reporter": "U.S.L.W.",
        "page": "4418",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1981 U.S. LEXIS 89",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "89",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "451 U.S. 204",
        "volume": "451",
        "reporter": "U.S.",
        "page": "204",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 S. Ct. 1642",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "1642",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 L. Ed. 2d 38",
        "volume": "68",
        "reporter": "L. Ed. 2d",
        "page": "38",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1981 U.S. LEXIS 89",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "89",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 U.S.L.W. 4418",
        "volume": "49",
        "reporter": "U.S.L.W.",
        "page": "4418",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "451 U.S. 204",
    "official_selection": {
      "court_class": "scotus",
      "selected": "451 U.S. 204",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-205",
      "page": null,
      "quote": "--- # Steagald v. United States *451 U.S. 204 (1981)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Armed with an arrest warrant for fugitive Ricky Lyons, DEA agents entered and searched Steagald's home\u2014where they believed Lyons might be found\u2014without a search warrant and without Steagald's consent. They did not find Lyons but found cocaine, and Steagald, who was not named in the arrest warrant, was convicted. ## Issue Whether an arrest warrant for one person justifies entering and searching a third party's home, without that person's consent and absent exigent circumstances, to look for the subject of the arrest warrant. ## Rule An arrest warrant does not authorize searching a third party's home.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1981-04-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Steagald v. United States",
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
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
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
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Darrell Mark Babcock",
          "cluster_id": 4623035,
          "cite": [
            "924 F.3d 1180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Doe v. United States",
          "cluster_id": 4590628,
          "cite": [
            "915 F.3d 905"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Garrett",
          "cluster_id": 4552162,
          "cite": [
            "2018 Ohio 4530",
            "123 N.E.3d 327"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hinshaw",
          "cluster_id": 4545610,
          "cite": [
            "2018 Ohio 4226",
            "120 N.E.3d 514"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532256,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
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
        "journal_ref": "Steagald v. United States:lane1_negative"
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
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532251,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
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
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Causey v. the State",
          "cluster_id": 3148713,
          "cite": [
            "334 Ga. App. 170",
            "778 S.E.2d 800"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
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
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. McCollum",
          "cluster_id": 6589541,
          "cite": [
            "79 Mass. App. Ct. 239",
            "945 N.E.2d 937",
            "2011 Mass. App. LEXIS 546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Al-Kidd v. Ashcroft",
          "cluster_id": 1204118,
          "cite": [
            "580 F.3d 949",
            "2009 U.S. App. LEXIS 20000",
            "2009 WL 2836448"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ricky Dale Williams v. State",
          "cluster_id": 2857082,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Anderson v. Creighton",
          "cluster_id": 111953,
          "cite": [
            "97 L. Ed. 2d 523",
            "107 S. Ct. 3034",
            "483 U.S. 635",
            "1987 U.S. LEXIS 2894",
            "55 U.S.L.W. 5092"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of St. Louis v. Praprotnik",
          "cluster_id": 112017,
          "cite": [
            "99 L. Ed. 2d 107",
            "108 S. Ct. 915",
            "485 U.S. 112",
            "1988 U.S. LEXIS 1069"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Welsh v. Wisconsin",
          "cluster_id": 111173,
          "cite": [
            "80 L. Ed. 2d 732",
            "104 S. Ct. 2091",
            "466 U.S. 740",
            "1984 U.S. LEXIS 82",
            "52 U.S.L.W. 4581"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Birchfield v. N. Dakota. William Robert Bernard",
          "cluster_id": 3216497,
          "cite": [
            "579 U.S. 438",
            "195 L. Ed. 2d 560",
            "2016 U.S. LEXIS 4058",
            "136 S. Ct. 2160"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
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
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The PEOPLE of the State of Colorado v. Joshua M. AARNESS",
          "cluster_id": 10014025,
          "cite": [
            "150 P.3d 1271",
            "2006 WL 2998823"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donovan v. Dewey",
          "cluster_id": 110530,
          "cite": [
            "69 L. Ed. 2d 262",
            "101 S. Ct. 2534",
            "452 U.S. 594",
            "1980 U.S. LEXIS 58"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brian A. Moreland, United States of America v. Brian A. Moreland",
          "cluster_id": 793267,
          "cite": [
            "437 F.3d 424",
            "69 Fed. R. Serv. 627",
            "2006 U.S. App. LEXIS 4166",
            "2006 WL 399691"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robbins v. California",
          "cluster_id": 110558,
          "cite": [
            "69 L. Ed. 2d 744",
            "101 S. Ct. 2841",
            "453 U.S. 420",
            "1981 U.S. LEXIS 132"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Oody",
          "cluster_id": 1740610,
          "cite": [
            "823 S.W.2d 554",
            "1991 Tenn. Crim. App. LEXIS 405"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cooke",
          "cluster_id": 1332990,
          "cite": [
            "291 S.E.2d 618",
            "306 N.C. 132",
            "1982 N.C. LEXIS 1378"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lebron v. National Railroad Passenger Corporation",
          "cluster_id": 117895,
          "cite": [
            "130 L. Ed. 2d 902",
            "115 S. Ct. 961",
            "513 U.S. 374",
            "1995 U.S. LEXIS 909",
            "95 Cal. Daily Op. Serv. 1228",
            "63 U.S.L.W. 4109",
            "8 Fla. L. Weekly Fed. S 564",
            "95 Daily Journal DAR 2219"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steagald v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110464 OR 9428299 OR 9428300) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjI3NjU3NjAwMDAwJnM9MzA0NTU0MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110464+OR+9428299+OR+9428300%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 16,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 17,
        "triage_snippet_classified": 183
      },
      "lane2_top_cited": {
        "query": "cites:(110464 OR 9428299 OR 9428300)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNDkmcz01NjA3OTQ0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110464+OR+9428299+OR+9428300%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110464 OR 9428299 OR 9428300)",
        "reviewed": 14,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 14,
        "triage_read": 1,
        "triage_snippet_classified": 13
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110464 OR 9428299 OR 9428300)",
    "indexed_citing_opinions": 1037,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110464,
        "count": 926,
        "count_source": "search"
      },
      {
        "opinion_id": 9428299,
        "count": 135,
        "count_source": "search"
      },
      {
        "opinion_id": 9428300,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1585,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/steagald-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc5OTA1Mzkmcz04NDM2ODEzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110464+OR+9428299+OR+9428300%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110464,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 108223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 109504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 110061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 110234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 110325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 272664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 276331,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 319014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 343372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 344771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 358848,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 370304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 374768,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 377954,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 380771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 382937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110464,
        "cited_id": 1356897,
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
    "date_created": "2026-07-05T20:36:09Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:36:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:36:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:41:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:36:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Steagald v. United States

```
<opinion type="majority">
<author id="b271-10">Justice Marshall</author>
<p id="AL1">delivered the opinion of the Court.</p>
<p id="b271-11">The issue in this case is whether, under the Fourth Amendment, a law enforcement officer may legally search for the subject of an arrest warrant in the home of a third party without first obtaining a search warrant. Concluding that a search warrant must be obtained absent exigent circum<page-number citation-index="1" label="206">*206</page-number>stances or consent, we reverse the judgment of the United States Court of Appeals for the Fifth Circuit affirming petitioner’s conviction.</p>
<p id="b272-5">I</p>
<p id="b272-6">In early January 1978, an agent of the Drug Enforcement Administration (DEA) was contacted in Detroit, Mich., by a confidential informant who suggested that he might be able to locate Ricky Lyons, a federal fugitive wanted on drug charges. On January 14, 1978, the informant called the agent again, and gave him a telephone number in the Atlanta, Ga., area where, according to the informant, Ricky Lyons could be reached during the next 24 hours. On January 16, 1978, the agent called fellow DEA Agent Kelly Goodowens in Atlanta and relayed the information he had obtained from the informant. Goodowens contacted Southern Bell Telephone Co., and secured the address corresponding to the telephone number obtained by the informant. Good-owens also discovered that Lyons was the subject of a 6-month-old arrest warrant.</p>
<p id="b272-7">Two days later, Goodowens and 11 other officers drove to the address supplied by the telephone company to search for Lyons. The officers observed two men standing outside the house to be searched. These men were Hoyt Gaultney and petitioner Gary Steagald. The officers approached with guns drawn, frisked both men, and, after demanding identification, determined that neither man was Lyons. Several agents proceeded to the house. Gaultney’s wife answered the door, and informed the agents that she was alone in the house. She was told to place her hands against the wall and was guarded in that position while one agent searched the house. Ricky Lyons was not found, but during the search of the house the agent observed what he believed to be cocaine. Upon being informed of this discovery, Agent Goodowens sent an officer to obtain a search warrant and in the meantime conducted a second search of the house, which uncovered <page-number citation-index="1" label="207">*207</page-number>additional incriminating evidence. During a third search conducted pursuant to a search warrant, the agents uncovered 43 pounds of cocaine. Petitioner was arrested and indicted on- federal drug charges.</p>
<p id="b273-5">Prior to trial, petitioner moved to suppress all evidence uncovered during the various searches on the ground that it was illegally obtained because the agents had failed to secure a search warrant before entering the house. Agent Goodowens testified at the suppression hearing that there had been no “physical hinderance” preventing him from obtaining a search warrant and that he did not do so because he believed that the arrest warrant for Ricky Lyons was sufficient to justify the entry and search. The District Court agreed with this view, and denied the suppression motion. Petitioner was convicted, and renewed his challenge to the search in his appeal. A divided Court of Appeals for the Fifth Circuit affirmed the District Court’s denial of petitioner’s suppression motion. <em>United States </em>v. <em>Gaultney, </em><span class="citation" data-id="9466112"><a href="/opinion/370304/united-states-v-hoyt-albert-gaultney-united-states-of-america-v-gary/" aria-description="Citation for case: United States v. Hoyt Albert Gaultney, United States of...">606 F. 2d 540</a></span> (1979).<footnotemark>1</footnotemark> Because the issue presented by this case is an important one<footnotemark>2</footnotemark> that has divided the Circuits,<footnotemark>3</footnotemark> we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./449/819/">449 U. S. 819</a></span>.</p>
<p id="b274-4"><page-number citation-index="1" label="208">*208</page-number>II</p>
<p id="b274-5">The Government initially seeks to avert our consideration of the Fifth Circuit’s decision by suggesting that petitioner may, regardless of the merits of that decision, lack an expectation of privacy in the house sufficient to prevail on his Fourth Amendment claim. This argument was never raised by the Government in the courts below. Moreover, in its brief in opposition to certiorari the Government represented <page-number citation-index="1" label="209">*209</page-number>to this Court that the house in question was “petitioner’s residence” and was “occupied by petitioner, Gaultney, and Gaultney’s wife.” Brief in Opposition 1, 3. However, the Government now contends that the record does not clearly show that petitioner had a reasonable expectation of privacy in the house, and hence urges us to remand the case to the District Court for re-examination of this factual question.</p>
<p id="b275-5">We decline to follow the suggested disposition. Aside from arguing that a search warrant was not constitutionally required, the Government was initially entitled to defend against petitioner’s charge of an unlawful search by asserting that petitioner lacked a reasonable expectation of privacy in the searched home, or that he consented to the search, or that exigent circumstances justified the entry. The Government, however, may lose its right to raise factual issues of this sort before this Court when it has made contrary assertions in the courts below, when it has acquiesced in contrary findings by those courts, or when it has failed to raise such questions in a timely fashion during the litigation.</p>
<p id="b275-6">We conclude that this is such a case. The Magistrate’s report on petitioner’s suppression motion, which was adopted by the District Court, characterized the issue as whether an arrest warrant was sufficient to justify the search of “the home of a third person” for the subject of the warrant. App. 12. The Government never sought to correct this characterization on appeal, and instead acquiesced in the District Court’s view of petitioner’s Fourth Amendment claim. Moreover, during both the trial and the appeal in this case the Government argued successfully that petitioner’s connection with the searched home was sufficient to establish his constructive possession of the cocaine found in a suitcase in the closet of the house.<footnotemark>4</footnotemark> Moreover, the Court of Appeals concluded, as <page-number citation-index="1" label="210">*210</page-number>had the Magistrate and the District Court, that petitioner’s Fourth Amendment claim involved the type of warrant necessary to search “premises belonging to a third party.” <span class="citation" data-id="9466112"><a href="/opinion/370304/united-states-v-hoyt-albert-gaultney-united-states-of-america-v-gary/#544" aria-description="Citation for case: United States v. Hoyt Albert Gaultney, United States of...">606 F. 2d, at 544</a></span>. Again, the Government declined to disturb this characterization. When petitioner sought review in this Court, the Government could have filed a cross-petition for certiorari suggesting, as it does now, that the case be remanded to the District Court for further proceedings. Instead, the Government argued that further review was unnecessary. Finally, the Government in its opposition to certiorari expressly represented that the searched home was petitioner’s residence.</p>
<p id="b276-5">Thus, during the course of these proceedings the Government has directly sought to connect petitioner with the house, has acquiesced in statements by the courts below characterizing the search as one of petitioner’s residence, and has made similar concessions of its own. Now, two years after petitioner’s trial, the Government seeks to return the case to the District Court for a re-examination of this factual issue.<footnotemark>5</footnotemark> <page-number citation-index="1" label="211">*211</page-number>The tactical advantages to the Government of this disposition are obvious, for if the Government prevailed on this claim upon a remand, it would be relieved of the task of defending the judgment of the Court of Appeals before this Court. We conclude, however, that the Government, through its assertions, concessions, and acquiescence, has lost its right to challenge petitioner’s assertion that he possessed a legitimate expectation of privacy in the searched home. We therefore turn to the merits of petitioner’s claim.</p>
<p id="b277-5">Ill</p>
<p id="b277-6">The question before us is a narrow one.<footnotemark>6</footnotemark> The search at issue here took place in the absence of consent or exigent circumstances. Except in such special situations, we have consistently held that the entry into a home to conduct a search or make an arrest is unreasonable under the Fourth Amendment unless done pursuant to a warrant. See <em>Payton </em>v. <em>New </em><page-number citation-index="1" label="212">*212</page-number><em>York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980); <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-15</a></span> (1948). Thus, as we recently observed: “[I]n terms that apply equally to seizures of property and to seizures of persons, the Fourth Amendment has drawn a firm line at the entrance 'to the house. Absent exigent circumstances, that threshold may not reasonably be crossed without a warrant.” <em>Payton </em>v. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York"><em>New York, supra, </em>at 590</a></span>. See <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#474" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 474-475, 477-478</a></span> (1971); <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#497" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 497-498</a></span> <em>(1958); Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#32" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 32-33</a></span> (1925). Here, of course, the agents had a warrant — one authorizing the arrest of Ricky Lyons. However, the Fourth Amendment claim here is not being raised by Ricky Lyons. Instead, the challenge to the search is asserted by a person not named in the warrant who was convicted on the basis of evidence uncovered during a search of his residence for Ricky Lyons. Thus, the narrow issue before us is whether an arrest warrant — as opposed to a search warrant — is adequate to protect the Fourth Amendment interests of persons not named in the warrant, when their homes are searched without their consent and in the absence of exigent circumstances.</p>
<p id="b278-5">The purpose of a warrant is to allow a neutral judicial officer to' assess whether the police have probable cause to make an arrest or conduct a search. As we have often explained, the placement of this checkpoint between the Government and the citizen implicitly acknowledges that an “officer engaged in the often competitive enterprise of ferreting out crime,” <em>Johnson </em>v. <em>United States, supra, </em>at 14, may lack sufficient objectivity to weigh correctly the strength of the evidence supporting the contemplated action against the individual’s interests in protecting his own liberty and the privacy of his home. <em>Coolidge </em>v. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#449" aria-description="Citation for case: Coolidge v. New Hampshire"><em>New Hampshire, supra, </em>at 449-451</a></span>; <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 455-456</a></span> (1948). However, while an arrest warrant and a search warrant both serve to subject the probable-cause determina<page-number citation-index="1" label="213">*213</page-number>tion of the police to judicial review, the interests protected by the two warrants differ. An arrest warrant is issued by a magistrate upon a showing that probable cause exists to believe that the subject of the warrant has committed an offense and thus the warrant primarily serves to protect an individual from an unreasonable seizure. A search warrant, in contrast, is issued upon a showing of probable cause to believe that the legitimate object of a search is located in a particular place, and therefore safeguards an individual’s interest in the privacy of his home and possessions against the unjustified intrusion of the police.</p>
<p id="b279-5">Thus, whether the arrest warrant issued in this case adequately safeguarded the interests protected by the Fourth Amendment depends upon what the warrant authorized the agents to do. To be sure, the warrant embodied a judicial finding that there was probable cause to believe that Ricky Lyons had committed a felony, and the warrant therefore authorized the officers to seize Lyons. However, the agents sought to do more than use the warrant to arrest Lyons in a public place or in his home; instead, they relied on the warrant as legal authority to enter the home of a third person based on their belief that Ricky Lyons might be a guest there. Regardless of how reasonable this belief might have been, it was never subjected to the detached scrutiny of a judicial officer. Thus, while the warrant in this case may have protected Lyons from an unreasonable seizure, it' did absolutely nothing to protect petitioner’s privacy interest in being free from an unreasonable invasion and search of his home. Instead, petitioner’s only protection from an illegal entry and search was the agent’s personal determination of probable cause. In the absence of exigent circumstances, we have consistently held that such judicially untested determinations are not reliable enough to justify an entry into a person’s home to arrest him without a warrant, or a search of a home for objects in the absence of a search warrant. <page-number citation-index="1" label="214">*214</page-number><em>Payton </em>v. <em>New <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">York, supra;</a></span> Johnson </em>v. <em>United States, supra. </em>We see no reason to depart from this settled course when the search of a home is for a person rather than an object.<footnotemark>7</footnotemark></p>
<p id="b281-4"><page-number citation-index="1" label="215">*215</page-number>A contrary conclusion — that the police, acting alone and in the absence of exigent circumstances, may decide when there is sufficient justification for searching the home of a third party for the subject of an arrest warrant — would create a significant potential for abuse. Armed solely with an arrest warrant for a single person, the police could search all the homes of that individual’s friends and acquaintances. See, <em>e. g., Lankford </em>v. <em>Gelston, </em><span class="citation" data-id="8876108"><a href="/opinion/8889937/lankford-v-gelston/" aria-description="Citation for case: Lankford v. Gelston">364 F. 2d 197</a></span> (CA4 1966) (enjoining police practice under which 300 homes were searched pursuant to arrest warrants for two fugitives). Moreover, an arrest warrant may serve as the pretext for entering a home in which the police have a suspicion, but not probable cause to believe, that illegal activity is taking place. Cf. <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#767" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 767</a></span> (1969). The Government recognizes the potential for such abuses,<footnotemark>8</footnotemark> but contends that existing remedies — such as motions to suppress illegally procured evidence and damages actions for Fourth Amendment violations — provide adequate means of redress. We do not agree. As we observed on a previous occasion, “[t]he [Fourth] Amendment is designed to prevent, not simply to redress, unlawful police action.” <em>Chimel </em>v. <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#766" aria-description="Citation for case: Chimel v. California"><em>California, supra, </em>at 766, n. 12</a></span>. Indeed, if suppression motions and damages actions were sufficient to implement the Fourth Amendment’s prohibition against unreasonable searches and seizures, there would be no need for the constitutional requirement that in the absence of exigent circumstances a warrant <page-number citation-index="1" label="216">*216</page-number>must be obtained for a home arrest or a search of a home for objects. We have instead concluded that in such cases the participation of a detached magistrate in the probable-cause determination is an essential element of a reasonable search or seizure, and we believe that the same conclusion should apply here.<footnotemark>9</footnotemark></p>
<p id="b282-5">In sum, two distinct interests were implicated by the search at issue here — Ricky Lyons’ interest in being free from an unreasonable seizure and petitioner’s interest in being free from an unreasonable search of his home. Because the arrest warrant for Lyons addressed only the former interest, the search of petitioner’s home was no more reasonable from petitioner’s perspective than it would have been if conducted in the absence of any warrant. Since warrantless searches of a home are impermissible absent consent or exigent circumstances, we conclude that the instant search violated the Fourth Amendment.</p>
<p id="b282-6">IV</p>
<p id="b282-7">The Government concedes that this view is “apparently logical,” that it furthers the general policies underlying the Fourth Amendment, and that it “has the virtue of producing symmetry between the law of entry to conduct a search for things to be seized and the law of entry to conduct a search for persons to be seized.” Brief for United States 36. Yet we are informed that this conclusion is “not without its flaws” in that it is contrary to common-law precedent and creates some practical problems of law enforcement. We treat these contentions in turn.</p>
<p id="b283-4"><page-number citation-index="1" label="217">*217</page-number>A</p>
<p id="b283-5">The common law may, within limits,<footnotemark>10</footnotemark> be instructive in determining what sorts of searches the Framers of the Fourth Amendment regarded as reasonable. See, <em>e. g., Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#591" aria-description="Citation for case: Payton v. New York">445 U. S., at 591</a></span>. The Government contends that at common law an officer could forcibly enter the home of a third party to execute an arrest warrant. To be sure, several commentators do suggest that a constable could “break open doors” to effect such an arrest. See 1 J. Chitty, Criminal Law *57 <em>(Chitty); </em>M. Foster, Crown Law 320 (1762) (Foster); 2 M. Hale, Pleas of the Crown 116-117 (1st Am. ed. 1847) (Hale). But see 4 E. Coke, Institutes *177. As support for this proposition, these commentators all rely on a single decision, <em>Semayne’s Case, 5 Co. </em>Rep. 91a, 92b-93a, 77 Eng. Rep. 194, 198 (K. B. 1603).<footnotemark>11</footnotemark> See 1 Chitty *57; <page-number citation-index="1" label="218">*218</page-number>Foster 320; 2 Hale 116. Although that case involved only the authority of a sheriff to effect civil service on a person within his own home, the court noted in dictum that a person could not “escape the ordinary process of law” by seeking refuge in the home of a third party. 5 Co. Rep., at 93a, 77 Eng. Rep., at 198. However, the language of the decision, while not free from ambiguity, suggests that forcible entry into a third party’s house was permissible only when the person to be arrested was pursued to the house. The decision refers to a person who “flies” to another’s home, <em>ibid., </em>and the annotation notes that “in order to justify the breaking of the outer door; after denial on request to take a person . . . in the house of a stranger, it must be understood . . . that the person <em>upon a pursuit </em>taketh refuge in the house of another.” <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Id.,</a></span> </em>at 93a, n. (I), 77 Eng. Rep., at 198, n. (I) (emphasis in original). The common-law commentators appear to have adopted this limitation. See 1 Chitty *57 (sheriff may enter third parties’ home “if the offender fly to it for refuge”); Foster 320 (“For if a Stranger whose ordinary Residence is elsewhere, upon a Pursuit taketh Refuge in the House of another, this is not <em>his </em>Castle, He cannot claim the Benefit of Sanctuary in it”); 2 Hale 116, n. 20 (forcible entry permissible “only upon strong necessity”). We have long recognized that such “hot pursuit” cases fall within the exigent-circumstances exception to the warrant requirement, see <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967), and therefore are distinguishable from the routine search situation presented here.</p>
<p id="b284-5">More important, the general question addressed by the common-law commentators was very different from the issue presented by this case. The authorities on which the Government relies were concerned with whether the <em>subject </em>of the arrest warrant could claim sanctuary from arrest by hiding <page-number citation-index="1" label="219">*219</page-number>in the home of a third party. See 1 Chitty *57; Foster 320; 2 Hale 116-117. Thus, in <em>Semayne’s Case </em>it was observed:</p>
<blockquote id="ATD">“[T]he house of any one is not a castle or privilege but for himself, and shall not extend to protect any person who flies to his house, or the goods of any other which are brought and conveyed into his house, to prevent a lawful execution, and to escape the ordinary process of law; for the privilege of his house extends only to him and his family, and to his own proper goods.” 5 Co. Rep., at 93a, 77 Eng. Rep., at 128.</blockquote>
<p id="b285-5">The common law thus recognized, as have our recent decisions, that rights such as those conferred by the Fourth Amendment are personal in nature, and cannot bestow vicarious protection on those who do not have a reasonable expectation of privacy in the place to be searched. See <em>United States </em>v. <em>Salvucci, </em><span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">448 U. S. 83</a></span> (1980); <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978). The issue here, however, is not whether the subject of an arrest warrant can object to the absence of a search warrant when he is apprehended in another person’s home, but rather whether the residents of that home can complain of the search. Because the authorities relied on by the Government focus on the former question without addressing the latter, we find their usefulness limited. Indeed, if anything, the little guidance that can be gleaned from common-law authorities undercuts the Government’s position. The language of <em>Semayne’s Case </em>quoted above, for example, suggests that although the subject of an arrest warrant could not find sanctuary in the home of the third party, the home remained a “castle or privilege” for its residents. Similarly, several commentators suggested that a search warrant, rather than an arrest warrant, was necessary to fully insulate a constable from an action for trespass brought by a party whose home was searched. See, <em>e. g., </em>1 Chitty *57; 2 Hale 116-117, 151.</p>
<p id="b286-4"><page-number citation-index="1" label="220">*220</page-number>While the common law thus sheds relatively little light on the narrow question before us, the history of the Fourth Amendment strongly suggests that its Framers would not have sanctioned the instant search. The Fourth Amendment was intended partly to protect against the abuses of the general warrants that had occurred in England and of the writs of assistance used in the Colonies. See <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#608" aria-description="Citation for case: Payton v. New York">445 U. S., at 608-609</a></span> (White, J., dissenting); <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 624-629</a></span> (1886); N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 13-78 (1937). The general warrant specified only an offense — typically seditious libel— and left to the discretion of the executing officials the decision as to which persons should be arrested and which places should be searched. Similarly, the writs of assistance used in the Colonies noted only the object of the search — any uncus-tomed goods — and thus left customs officials completely free to search any place where they believed such goods might be. The central objectionable feature of both warrants was that they provided no judicial check on the determination of the executing officials that the evidence available justified an intrusion into any particular home. <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476</a></span>, 481 — 485 (1965). An arrest warrant, to the extent that it is invoked as authority to enter the homes of third parties, suffers from the same infirmity.<footnotemark>12</footnotemark> Like a writ of assistance, it specifies only the object of a search — in this case, Ricky Lyons — and leaves to the unfettered discretion of the police the decision as to which particular homes should be searched. We do not believe that the Framers of the Fourth Amendment would have condoned such a result.</p>
<p id="b286-5">B</p>
<p id="b286-6">The Government also suggests that practical problems might arise if law enforcement officers are required to obtain <page-number citation-index="1" label="221">*221</page-number>a search warrant before entering the home of a third party to make an arrest.<footnotemark>13</footnotemark> The basis of this concern is that persons, as opposed to objects, are inherently mobile, and thus officers seeking to effect an arrest may be forced to return to the magistrate several times as the subject of the arrest warrant moves from place to place. We are convinced, however, that a search warrant requirement will not significantly impede effective law enforcement efforts.</p>
<p id="b287-5">First, the situations in which a search warrant will be necessary are few. As noted in <em>Payton </em>v. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#602" aria-description="Citation for case: Payton v. New York"><em>New York, supra, </em>at 602-603</a></span>, an arrest warrant alone will suffice to enter a suspect’s own residence to effect his arrest. Furthermore, if probable cause exists, no warrant is required to apprehend a suspected felon in a public place. <em>United States </em>v. <em>Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976). Thus, the subject of an arrest warrant can be readily seized before entering or after leaving the home of a third party.<footnotemark>14</footnotemark> Finally, the exigent-circumstances doctrine significantly limits the situations in which a search warrant would be needed. For example, a warrant-less entry of a home would be justified if the police were in “hot pursuit” of a fugitive. See <em>United States </em>v. <em>Santana, </em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#42" aria-description="Citation for case: United States v. Santana">427 U. S. 38, 42-43</a></span> (1976); <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> <page-number citation-index="1" label="222">*222</page-number>(1967). Thus, to the extent that searches for persons pose special problems, we believe that the exigent-circumstances doctrine is adequate to accommodate legitimate law enforcement needs.</p>
<p id="b288-4">Moreover, in those situations in which a search warrant is necessary, the inconvenience incurred by the police is simply not that significant. First, if the police know of the location of the felon when they obtain an arrest warrant, the additional burden of obtaining a search warrant at the same time is miniscule. The inconvenience of obtaining such a warrant does not increase significantly when an outstanding arrest warrant already exists. In this case, for example, Agent Goodowens knew the address of the house to be searched two days in advance, and planned the raid from the federal courthouse in Atlanta where, we are informed, three full-time magistrates were on duty. In routine search cases such as this, the short time required to obtain a search warrant from a magistrate will seldom hinder efforts to apprehend a felon. Finally, if a magistrate is not nearby, a telephonic search warrant can usually be obtained. See Fed. Rule Crim. Proc. 41 (c)(1), (2).</p>
<p id="b288-5">Whatever practical problems remain, however, cannot outweigh the constitutional interests at stake. Any warrant requirement impedes to some extent the vigor with which the Government can . seek to enforce its laws, yet the Fourth Amendment recognizes that this restraint is necessary in some cases to protect against unreasonable searches and seizures. We conclude that this is such a case. The additional burden imposed on the police by a warrant requirement is minimal. In contrast, the right protected — that of presumptively innocent people to be secure in their homes from unjustified, forcible intrusions by the Government — is weighty. Thus, in order to render the instant search reasonable under the Fourth Amendment, a search warrant was required.</p>
<p id="b289-4"><page-number citation-index="1" label="223">*223</page-number>Accordingly, the judgment of the Court of Appeals is reversed, and the case is remanded to that court for further proceedings consistent with this opinion.</p>
<p id="b289-5">
<em>So ordered.</em>
</p>
<p id="b289-6">The Chief Justice concurs in the judgment.</p>
<footnote label="1">
<p id="b273-6"> The court relied on a previous decision in the Circuit that held that “when an officer holds a valid arrest warrant and reasonably believes that its subject is within premises belonging to a third party, he need not obtain a search warrant to enter for the purpose of arresting the subject.” <em>United States </em>v. <em>Cravero, </em>545 E. 2d 406, 421 (1976), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./430/983/">430 U. S. 983</a></span> (1977). Circuit Judge Kraviteh dissented on the ground that the information known to the agents was insufficient to establish a reasonable belief that Lyons could be found in the house to be searched. <span class="citation" data-id="9466112"><a href="/opinion/370304/united-states-v-hoyt-albert-gaultney-united-states-of-america-v-gary/#548" aria-description="Citation for case: United States v. Hoyt Albert Gaultney, United States of...">606 F. 2d at 548</a></span>. On the petition for rehearing, Judge Kraviteh, again in dissent, contended that the majority’s decision announced a “rule of questionable validity and wisdom” and represented a “disturbing erosion of the Fourth Amendment rights of third parties.” <em>United States </em>v. <em>Gaultney, </em><span class="citation" data-id="9466489"><a href="/opinion/374768/united-states-v-hoyt-albert-gaultney-united-states-of-america-v-gary/#644" aria-description="Citation for case: United States v. Hoyt Albert Gaultney, United States of...">615 F. 2d 642, 644</a></span> (1980).</p>
</footnote>
<footnote label="2">
<p id="b273-7"> Last Term we noted that this question remained unresolved. See <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 583</a></span> (1980).</p>
</footnote>
<footnote label="3">
<p id="b273-8"> Three Circuits have held that in ,the absence of exigent circumstances a search warrant is required before law officers may enter the home of <page-number citation-index="1" label="208">*208</page-number>a third party to execute an arrest warrant. See <em>Government of Virgin Islands </em>v. <em>Gereau, </em><span class="citation" data-id="8173389"><a href="/opinion/8210936/government-of-virgin-islands-v-gereau/#928" aria-description="Citation for case: Government of Virgin Islands v. Gereau">502 <em>F. 2d 914, </em>928</a></span> (CA3 1974), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./420/909/">420 U. S. 909</a></span> (1975); <em>Wallace </em>v. <em>King, </em><span class="citation" data-id="8911894"><a href="/opinion/8922855/wallace-v-king/#1158" aria-description="Citation for case: Wallace v. King">626 F. 2d 1157, 1158-1159</a></span> (CA4 1980), cert. pending, No. 80-503; <em>United States v. Prescott, </em><span class="citation" data-id="9465056"><a href="/opinion/358848/united-states-v-saundra-prescott/#1347" aria-description="Citation for case: United States v. Saundra Prescott">581 F. 2d 1343, 1347-1350</a></span> (CA9 1978). Two Circuits have joined the Court of Appeals in this case in adopting the contrary view that a search warrant is not required in such situations if the police have an arrest warrant an'd reason to believe that the person to be arrested is within the home to be searched. See <em>United States </em>v. <em>McKinney, </em><span class="citation" data-id="276331"><a href="/opinion/276331/united-states-v-roy-mckinney/#262" aria-description="Citation for case: United States v. Roy McKinney">379 F. 2d 259, 262-263</a></span> (CA6 1967); <em>United States </em>v. <em>Harper, </em><span class="citation" data-id="343372"><a href="/opinion/343372/united-states-v-maurice-harper/#612" aria-description="Citation for case: United States v. Maurice Harper">550 F. 2d 610, 612-614</a></span> (CA10), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./434/837/">434 U. S. 837</a></span> (1977). The Second Circuit has suggested in dictum that it subscribes to this latter view, see <em>United States </em>v. <em>Manley, </em><span class="citation" data-id="382937"><a href="/opinion/382937/united-states-v-david-manley-and-fluer-williams/#983" aria-description="Citation for case: United States v. David Manley and Fluer Williams">632 F. 2d 978, 983</a></span> (1980), while the Court of Appeals for the District of Columbia Circuit has recently indicated that it would require a search warrant in such cases. See <em>United States </em>v. <em>Ford, </em>180 U. S. App. D. C. 1, 14, n. 45, <span class="citation multiple-matches"><a href="/c/F.%202d/553/146/">553 F. 2d 146</a></span>, 159, n. 45 (1977). Two other Courts of Appeals have left the issue open. See <em>United States </em>v. <span class="citation" data-id="377954"><a href="/opinion/377954/united-states-v-carol-e-adams/#44" aria-description="Citation for case: United States v. Carol E. Adams"><em>Adams, 621 </em>F. 2d 41, 44, n. 7</a></span> (CA1 1980); <em>Rice </em>v. <em>Wolff, </em>513 F. 2d-1280, 1291-1292, and n. 7 (CA8 1975), rev’d on other grounds <em>sub nom. Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U. S. 465</a></span> (1976). The Seventh Circuit has not considered the question.</p>
<p id="b274-7">While the courts are in conflict, most modem commentators agree that a search warrant is necessary to fully protect the privacy interests of third parties when their home is searched for the subject of an arrest warrant. See 2 W. LaFave, Search and Seizure: A Treatise on the Fourth Amendment 374, 38A-385 (1978); Rotenberg &amp; Tanzer, Searching for the Person to Be Seized, 35 Ohio St. L. J. 56, 67-71 (1974); Groot, Arrests in Private Dwellings, <span class="citation no-link">67 Va. L. Rev. 275</span> (1981); Note, The Neglected Fourth Amendment Problem in Arrest Entries, <span class="citation no-link">23 Stan. L. Rev. 995</span>, 997-999 (1971); Comment, Arresting a Suspect in a Third Party’s Home: What is Reasonable?, 72 J. Crim. L. &amp; C. 293 <em>(1981). </em>But see Mascolo, Arrest Warrants and Search Warrants: The Seizure of A Suspect in the Home of a Third Party, 54 Conn. Bar J. 299 (1980).</p>
</footnote>
<footnote label="4">
<p id="b275-7"> The Court of Appeals, in accepting this contention, cited the Government’s own evidence that several checks and papers bearing petitioner’s name were found in the house and that “Steagald, when taken into cus<page-number citation-index="1" label="210">*210</page-number>tody, was wearing only slacks and a long-sleeve shirt, clothing inconsistent with the coldness of the January afternoon, and that once taken inside the . . . house, told a DEA agent that he was cold and requested that she get a sweater or coat for him from the kitchen area.” <span class="citation" data-id="9466112"><a href="/opinion/370304/united-states-v-hoyt-albert-gaultney-united-states-of-america-v-gary/#546" aria-description="Citation for case: United States v. Hoyt Albert Gaultney, United States of...">606 F. 2d, at 546-547</a></span>.</p>
</footnote>
<footnote label="5">
<p id="b276-10"> The Government asserts that it was unable to raise this issue in the courts below because both courts had acted before this Court decided <em>United States </em>v. <em>Salvucci, </em><span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">448 U. S. 83</a></span> (1980). We do not find this justification to be compelling. Under the “automatic standing” rule of <em>Jones </em>v. <em>United States, </em>362 U. S.-257 (1960), any person charged with a possessory offense could challenge the search in which the incriminating evidence was obtained. <em><span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">Salvucci</a></span> </em>overruled <em><span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>and instead limited such Fourth Amendment claims to those persons who had a reasonable expecta^tion of privacy in the area or object of the search. Although <em><span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">Salvucci</a></span> </em>thus altered Fourth Amendment jurisprudence to some extent, the rationale of that decision was in large part simply an extension of this Court’s earlier reasoning in <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978). The <em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span> </em>decision held that an illegal search violated the Fourth Amendment rights only of those persons who had a “legitimate expectation of <page-number citation-index="1" label="211">*211</page-number>privacy in the invaded place.” <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois"><em>Id., </em>at 143</a></span>. While that decision did not directly address the “automatic standing” rule of <em>Jones </em>v. <em>United States, </em>it was clearly an ill omen for the continued vitality of that decision. Since <em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span> </em>was decided well before this case was briefed and argued in the Court of Appeals, the Government could easily have raised before that court the question of whether petitioner’s Fourth Amendment rights were even implicated by the search at issue here. Indeed, the Government in <em><span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">Salvucci</a></span> </em>clearly recognized the significance of <em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span>, </em>for in that case, despite the contrary authority of <em>Jones </em>v. <em>United States, </em>it argued from the outset that the defendant lacked a sufficient expectation of privacy to challenge the legality of the search under the Fourth Amendment. We are given no explanation why the Government failed to regard <em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span> </em>as of equal significance to this case. In any event, <em><span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">Salvucci</a></span> </em>was decided before certiorari was sought in this case, but rather than oppose certiorari on the ground that petitioner lacked a legitimate expectation of privacy in the searched home, the Government made explicit concessions to the contrary.</p>
</footnote>
<footnote label="6">
<p id="b277-8"> Initially, we assume without deciding that the information relayed to Agent Goodowens concerning the whereabouts of Ricky Lyons would have been sufficient to establish probable Cause to believe that Lyons was at the house searched by the agents.</p>
</footnote>
<footnote label="7">
<p id="b280-5"> Indeed, the plain wording of the Fourth Amendment admits of no exemption from the warrant requirement when the search of a home is for a person rather than for a thing. As previously noted, absent exigent circumstances or consent, an entry into a private dwelling to conduct a search or effect an arrest is unreasonable without a warrant. The second clause of the Fourth Amendment, which governs the issuance of such warrants, provides that “no Warrants shall issue but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.” This language plainly suggests that the same sort of judicial determination must be made when the search of a person’s home is for another person as is necessary when the search is for an object. Specifically, absent exigent circumstances the magistrate, rather than the police officer, must make the decision that probable cause exists- to believe that the person or object to be seized is within a particular place.</p>
<p id="b280-6">In <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>of course, we recognized that an arrest warrant alone was sufficient to authorize the entry into a person’s home to effect his arrest. We reasoned:</p>
<blockquote id="b280-7">“If there is sufficient evidence of a citizen’s participation in a felony to persuade a judicial officer that his arrest is justified, it is constitutionally reasonable to require him to open his doors to the officers of the law. Thus, for Fourth Amendment purposes, an arrest warrant founded on probable cause implicitly carries with it the limited authority to enter a dwelling in which the suspect lives when there is reason to believe the suspect is within.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#602" aria-description="Citation for case: Payton v. New York">445 U. S., at 602-603</a></span>.</blockquote>
<p id="b280-8">Because an arrest warrant authorizes the police to deprive a person of his liberty, it necessarily also authorizes a limited invasion of that person’s privacy interest when it is necessary to arrest him in his home. This analysis, however, is plainly inapplicable when the police seek to use an arrest warrant as legal authority to enter the home of a third party to conduct a search. Such a warrant embodies no judicial determination whatsoever regarding the person whose home is to be searched. Because it does not authorize the police to deprive the third person of his liberty, it cannot embody any derivative authority to deprive this person of his interest in the privacy of his home. Such a deprivation must instead be based on an independent showing that a legitimate object of a search is located in the third party’s home. We have consistently held, however, <page-number citation-index="1" label="215">*215</page-number>that such a determination is the province of the magistrate, and not that of the police officer.</p>
</footnote>
<footnote label="8">
<p id="b281-7"> The Government concedes that "an arrest warrant may be thought to have some of the undesirable attributes of a general warrant if it authorizes entry into third party premises.” Brief for United States 42. Similarly, the Government agrees that “the potential for abuse is much less if the implicit entry authorization of an arrest warrant is confined to the suspect’s own residence and is not held to make the police free to search for the suspect in anyone else’s house without obtaining a particularized judicial determination that the suspect is present.” <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Ibid.</a></span></em></p>
</footnote>
<footnote label="9">
<p id="b282-8"> Moreover, the remedies suggested by the Government are not without their pitfalls and limitations. For example, absent a search warrant requirement, a person seeking to recover civil damages for the unjustified search of his home may possibly be thwarted if a good-faith defense to such unlawful conduct is recognized. See, e. <em>g., Wallace </em>v. <em>King, </em><span class="citation" data-id="8911894"><a href="/opinion/8922855/wallace-v-king/#1161" aria-description="Citation for case: Wallace v. King">626 F. 2d, at <em>1161.</em></a></span></p>
</footnote>
<footnote label="10">
<p id="b283-6"> The significance accorded to such authority, however, must be kept in perspective, for our decisions in this area have not "simply frozen into constitutional law those enforcement practices that existed at the time of the Fourth Amendment’s passage.” <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#591" aria-description="Citation for case: Payton v. New York">445 U. S., at 591, n. 33</a></span>. The common-law rules governing searches and arrests evolved in a society far simpler than ours is today. Crime has changed, as have the means of law enforcement, and it would therefore be naive to assume that those actions a constable could take in an English or American village three centuries ago should necessarily govern what we, as a society, now regard as proper. Cf. <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 352-353</a></span> (1967). Instead, the Amendment’s prohibition against “unreasonable searches and seizures” must be interpreted “in light of contemporary norms, and conditions.” <em>Payton </em>v. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#591" aria-description="Citation for case: Payton v. New York"><em>New York, supra, </em>at 591, n. 33</a></span>.</p>
</footnote>
<footnote label="11">
<p id="b283-7"> The three other decisions cited by the Government do not address the issue raised here. <em>Johnson </em>v. <em>Leigh, </em>6 Taunt. 246, 248, 128 Eng. Rep. 1029, 1029-1030 (C. P. 1815), dealt with the authority of a constable to enter the home of a third person to make an arrest when the “outer door” was open. Under the common law, “a privilege attaches to the outer door of a dwelling, because ... it is the owner’s castle.” <em>Hutchison </em>v. <em>Birch, 4 </em>Taunt. 619, 625, 128 Eng. Rep. 473, 476 (C. P. 1812). Thus, an open outer door was apparently regarded as the equivalent of a consent of the occupant for the constable to enter the home and conduct a search. The other two decisions cited by the Government, <em>Sheers </em>v. <em>Brooks, </em>2 Bl. H. <page-number citation-index="1" label="218">*218</page-number>120, 122, 126 Eng. Rep. 463, 464 (C. P. 1792), and <em>Kelsy </em>v. <span class="citation" data-id="6613353"><a href="/opinion/6731697/kelsy-v-wright/" aria-description="Citation for case: Kelsy v. Wright"><em>Wright, 1 </em>Root 83</a></span> (Conn. 1783), dealt only with the authority of the constable to enter the home of the person to be arrested.</p>
</footnote>
<footnote label="12">
<p id="b286-7"> The Government recognizes this problem. See n. 8, <em>supra.</em></p>
</footnote>
<footnote label="13">
<p id="b287-6"> A number of Circuits already require a search warrant for entries of this sort, see n. 3, supra, and there is no indication in the record that law enforcement efforts in these jurisdictions have suffered as a result. Thus, we are inclined to view the Government’s argument on this point with considerable skepticism. Cf. <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#602" aria-description="Citation for case: Payton v. New York">445 U. S., at 602</a></span>.</p>
<p id="b287-7">Moreover, we are informed by the Government that “it is the present policy of the Drug Enforcement Administration, whose agents conducted the search in the present case, to secure a search warrant prior to making an arrest entry into third party premises, in the absence of exigent circumstances or consent.” Brief in Opposition 0, n. 7.</p>
</footnote>
<footnote label="14">
<p id="b287-8"> Indeed, the “inherent mobility” of persons noted by the Government suggests that in most situations the police may avoid altogether the need to obtain a search warrant simply by waiting for a suspect to leave the third person’s home before attempting to arrest that suspect.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Steele v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Steele v. United States"
type: case
citation: "267 U.S. 498 (1925)"
parallel_cite: "45 S. Ct. 414; 69 L. Ed. 757"
neutral_cite: 1925 U.S. LEXIS 386
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1925
date_decided: 1925-04-13
docket: 235
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1925-04-13
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Steele v. United States
  varies_by_point: false
  scope_note: "Controlling and canonical: the particularity-of-place requirement is satisfied if an officer can, with reasonable effort, ascertain and identify the place intended."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/100621/steele-v-united-states-no-1/"
  cluster_id: 100621
  opinion_id: 100621
  identity_checked: true
homes:
  - page: "[[Particularity]]"
    role: "Progeny"
related: ["[[Maryland v. Garrison]]", "[[Groh v. Ramirez]]", "[[Stanford v. Texas]]"]
aliases: ["Steele v. United States No. 1"]
tags: ["case", "fourth-amendment", "warrant-requirement", "particularity", "description-of-place"]
holding: "A warrant satisfies the Fourth Amendment's particularity-of-place requirement if its description is such that the executing officer can, with reasonable effort, ascertain and identify the place intended to be searched."
lake:
  record_id: Steele v. United States
  status: verified
  projected_at: 2026-07-06
---

# Steele v. United States

*267 U.S. 498 (1925)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A prohibition agent saw cases marked "whiskey" being unloaded at a building at 611 W. 46th Street and confirmed there was no permit to store liquor there. A warrant issued to search the building — described as a garage used for business purposes — and any rooms, basement, or sub-cellar connected with the garage, for "cases of whiskey." Executing it, agents seized large quantities of liquor across multiple floors. Steele sought return of the property, arguing the warrant failed to describe the place to be searched with sufficient [[Particularity|particularity]].

## Issue
Did the warrant's description of the place to be searched satisfy the Fourth Amendment's [[Particularity|particularity]] requirement?

## Rule
Yes. "It is enough if the description is such that the officer with a search warrant can with reasonable effort ascertain and identify the place intended." — 267 U.S. at 503. ^pin-503

A description identifying the building by its address and character, reaching the rooms and spaces connected with it, suffices.

## Application
The warrant described the building at 611 W. 46th Street as a garage for business purposes and reached the rooms and basement connected with it. "The description of the building as a garage and for business purposes at 611 W. 46th Street clearly indicated the whole building as the place intended to be searched," — *Id.* — and the garage's elevator connected it with every floor. An officer could, with reasonable effort, identify the premises. The search did not exceed the warrant, the description "cases of whiskey" was specific enough, and probable cause supported issuance. The warrant therefore satisfied constitutional requirements. ^pin-503b

## Conclusion
The warrant complied with the Fourth Amendment; the liquor was lawfully seized and need not be returned. The decree was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Steele* remains the canonical statement of the [[Particularity|particularity]]-of-place standard — reasonable-effort identification of the premises — and is regularly cited in the line that includes [[Maryland v. Garrison]] and [[Groh v. Ramirez]]. No negative treatment.

## Appears on
- [[Particularity]] — *Progeny*

## Sources
- *Steele v. United States No. 1*, 267 U.S. 498 (1925) — https://www.courtlistener.com/opinion/100621/steele-v-united-states-no-1/ — pinpoint: 503.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c971f49486f86f00", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Steele v. United States"}, "payload": {"all": [{"cite": "267 U.S. 498", "page": "498", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "267"}, {"cite": "45 S. Ct. 414", "page": "414", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "45"}, {"cite": "69 L. Ed. 757", "page": "757", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "69"}, {"cite": "1925 U.S. LEXIS 386", "page": "386", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1925"}], "display": "267 U.S. 498", "official": {"cite": "267 U.S. 498", "page": "498", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "267"}, "official_selection_present": true, "record_id": "Steele v. United States"}}
{"assertion_id": "3f89acee210cd333", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-503", "record_id": "Steele v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-503", "pinpoint_status": "slip-only", "quote": "Executing it, agents seized large quantities of liquor across multiple floors. Steele sought return of the property, arguing the warrant failed to describe the place to be searched with sufficient particularity. ## Issue Did the warrant's description of the place to be searched satisfy the Fourth Amendment's particularity requirement? ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Steele v. United States", "star_marker": null}}
{"assertion_id": "9b139e34e55fd0f8", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-503b", "record_id": "Steele v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-503b", "pinpoint_status": "slip-only", "quote": "The description of the building as a garage and for business purposes at 611 W. 46th Street clearly indicated the whole building as the place intended to be searched,", "quote_fidelity": "mismatch", "record_id": "Steele v. United States", "star_marker": null}}
{"assertion_id": "9713b803a18e21b3", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Steele v. United States"}, "payload": {"as_of_content": "1925-04-13", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Steele v. United States", "scope_note": "Controlling and canonical: the particularity-of-place requirement is satisfied if an officer can, with reasonable effort, ascertain and identify the place intended.", "varies_by_point": false}}
```

### lake record — Steele v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Steele v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Steele v. United States No. 1",
    "case_name_short": "Steele",
    "case_name_full": "STEELE v. UNITED STATES No. 1",
    "input_case_name": "Steele v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1925-04-13",
    "year": 1925,
    "docket": "235",
    "cluster_id": 100621,
    "lead_opinion_id": 100621,
    "sibling_ids": [
      100621
    ],
    "absolute_url": "/opinion/100621/steele-v-united-states-no-1/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "267 U.S. 498",
      "volume": "267",
      "reporter": "U.S.",
      "page": "498",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "45 S. Ct. 414",
        "volume": "45",
        "reporter": "S. Ct.",
        "page": "414",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 757",
        "volume": "69",
        "reporter": "L. Ed.",
        "page": "757",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1925 U.S. LEXIS 386",
        "volume": "1925",
        "reporter": "U.S. LEXIS",
        "page": "386",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "267 U.S. 498",
        "volume": "267",
        "reporter": "U.S.",
        "page": "498",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "45 S. Ct. 414",
        "volume": "45",
        "reporter": "S. Ct.",
        "page": "414",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 757",
        "volume": "69",
        "reporter": "L. Ed.",
        "page": "757",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1925 U.S. LEXIS 386",
        "volume": "1925",
        "reporter": "U.S. LEXIS",
        "page": "386",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "267 U.S. 498",
    "official_selection": {
      "court_class": "scotus",
      "selected": "267 U.S. 498",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-503",
      "page": null,
      "quote": "Executing it, agents seized large quantities of liquor across multiple floors. Steele sought return of the property, arguing the warrant failed to describe the place to be searched with sufficient particularity. ## Issue Did the warrant's description of the place to be searched satisfy the Fourth Amendment's particularity requirement? ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-503b",
      "page": null,
      "quote": "The description of the building as a garage and for business purposes at 611 W. 46th Street clearly indicated the whole building as the place intended to be searched,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1925-04-13",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Steele v. United States",
    "varies_by_point": false,
    "scope_note": "Controlling and canonical: the particularity-of-place requirement is satisfied if an officer can, with reasonable effort, ascertain and identify the place intended.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Steele v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bonds, Michael Ray",
          "cluster_id": 2948505,
          "cite": [
            "403 S.W.3d 867",
            "2013 Tex. Crim. App. LEXIS 531",
            "2013 WL 1136522"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Eikenberry, 22017 (3-14-2008)",
          "cluster_id": 4023636,
          "cite": [
            "2008 Ohio 1159"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Murphy",
          "cluster_id": 1781916,
          "cite": [
            "693 S.W.2d 255",
            "1985 Mo. App. LEXIS 4042"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Guarino",
          "cluster_id": 432229,
          "cite": [
            "729 F.2d 864",
            "1984 U.S. App. LEXIS 25026"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Olivas v. State",
          "cluster_id": 1659675,
          "cite": [
            "631 S.W.2d 553",
            "1982 Tex. App. LEXIS 4221"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Allan Michael Klein",
          "cluster_id": 350518,
          "cite": [
            "565 F.2d 183",
            "196 U.S.P.Q. (BNA) 273",
            "1977 U.S. App. LEXIS 10758"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Eduardo Bermudez",
          "cluster_id": 331417,
          "cite": [
            "526 F.2d 89"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Louis M. Darensbourg",
          "cluster_id": 329404,
          "cite": [
            "520 F.2d 985",
            "1975 U.S. App. LEXIS 12416"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane1_negative"
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
        "journal_ref": "Steele v. United States:lane2_top_cited"
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
        "journal_ref": "Steele v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brinegar v. United States",
          "cluster_id": 104716,
          "cite": [
            "93 L. Ed. 2d 1879",
            "69 S. Ct. 1302",
            "338 U.S. 160",
            "1949 U.S. LEXIS 2084"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Draper v. United States",
          "cluster_id": 105820,
          "cite": [
            "3 L. Ed. 2d 327",
            "79 S. Ct. 329",
            "358 U.S. 307",
            "1959 U.S. LEXIS 1607"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane2_top_cited"
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
        "journal_ref": "Steele v. United States:lane2_top_cited"
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
        "journal_ref": "Steele v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marron v. United States",
          "cluster_id": 101164,
          "cite": [
            "275 U.S. 192",
            "48 S. Ct. 74",
            "72 L. Ed. 231",
            "1927 U.S. LEXIS 273"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane2_top_cited"
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
        "journal_ref": "Steele v. United States:lane2_top_cited"
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
        "journal_ref": "Steele v. United States:lane2_top_cited"
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
        "journal_ref": "Steele v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stanford v. Texas",
          "cluster_id": 106964,
          "cite": [
            "13 L. Ed. 2d 431",
            "85 S. Ct. 506",
            "379 U.S. 476",
            "1965 U.S. LEXIS 2380"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. United States",
          "cluster_id": 105749,
          "cite": [
            "2 L. Ed. 2d 1514",
            "78 S. Ct. 1253",
            "357 U.S. 493",
            "1958 U.S. LEXIS 1928",
            "2 C.B. 1005",
            "2 A.F.T.R.2d (RIA) 6467"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carroll v. United States",
          "cluster_id": 105542,
          "cite": [
            "1 L. Ed. 2d 1442",
            "77 S. Ct. 1332",
            "354 U.S. 394",
            "1957 U.S. LEXIS 583"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Sprague",
          "cluster_id": 3160073,
          "cite": [
            "303 Kan. 418",
            "362 P.3d 828",
            "2015 Kan. LEXIS 935"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McCarty",
          "cluster_id": 2045025,
          "cite": [
            "858 N.E.2d 15",
            "223 Ill. 2d 109",
            "306 Ill. Dec. 570",
            "2006 Ill. LEXIS 1649"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane2_top_cited"
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
        "journal_ref": "Steele v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Martin",
          "cluster_id": 1651199,
          "cite": [
            "721 N.W.2d 815",
            "271 Mich. App. 280"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Terry",
          "cluster_id": 8926810,
          "cite": [
            "702 F.2d 299"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cogen v. United States",
          "cluster_id": 101354,
          "cite": [
            "278 U.S. 221",
            "49 S. Ct. 118",
            "73 L. Ed. 275",
            "1929 U.S. LEXIS 7"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Falcone",
          "cluster_id": 1500782,
          "cite": [
            "109 F.2d 579",
            "1940 U.S. App. LEXIS 3954"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Nieves",
          "cluster_id": 5681167,
          "cite": [
            "36 N.Y.2d 396",
            "330 N.E.2d 26",
            "369 N.Y.S.2d 50",
            "1975 N.Y. LEXIS 1819"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Dumas",
          "cluster_id": 1164023,
          "cite": [
            "512 P.2d 1208",
            "9 Cal. 3d 871",
            "109 Cal. Rptr. 304",
            "1973 Cal. LEXIS 234"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mary Velardi and Frances Velardi v. Cornelius R. Walsh, Jr. And Robert L. Boek",
          "cluster_id": 682739,
          "cite": [
            "40 F.3d 569",
            "1994 U.S. App. LEXIS 32582"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Russell R. George, AKA Rusty, and Pamela A. Johnson-Sherman, Francis R. Lajoice",
          "cluster_id": 590903,
          "cite": [
            "975 F.2d 72",
            "1992 U.S. App. LEXIS 22728"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Steele v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(100621) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjczNTY4MDAwMDAmcz0xMTkwMTU3JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28100621%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 60,
        "triage_read": 6,
        "triage_snippet_classified": 54
      },
      "lane2_top_cited": {
        "query": "cites:(100621)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDUmcz0yOTQ4NTA1JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28100621%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(100621)",
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
    "complete_query": "cites:(100621)",
    "indexed_citing_opinions": 480,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 100621,
        "count": 480,
        "count_source": "search"
      }
    ],
    "citation_count": 727,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/steele-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY2MjEzOTgmcz00NzEzOTc1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28100621%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 100621,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100621,
        "cited_id": 3554462,
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
    "date_created": "2026-07-05T20:41:05Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:41:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:41:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:03:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:41:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Steele v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b539-10">
  Me. Chief Justice Taft
 </author>
<p id="A89">
  delivered the opinion of the Court.
 </p>
<p id="b539-11">
  This is an appeal, under § 238 of the Judicial Code, direct from the District Court, being a case involving the application of the Federal Constitution. The judgment complained of denied a petition of Steele for an order vacating a search warrant, by authority of which Steele’s premises were searched and a large amount of whiskey and other intoxicating liquor was found and seized. He contends that the search warrant violated the Fourth Amendment, because not issued upon probable cause, and not particularly describing the place to be searched or the property to be seized; and because the search conducted under the warrant was unreasonable. The affidavit for search warrant was as follows:
 </p>
<blockquote id="b539-12">
  “Southern District of New York, ss:
 </blockquote>
<blockquote id="b539-13">
  “Isidor Einstein, being duly sworn, deposes and says: I am a General Prohibition Agent assigned to duty in.
  <span citation-index="1" class="star-pagination" label="500"> 
   *500
   </span>
  the State of New York. On December 6, 1922, at about 10 o’clock A. M., accompanied by Agent Moe W. Smith, I was standing in front of the garage located in the building at 611 West '46th Street, Borough of Manhattan, City and Southern District of New York. This building is used for- business purposes only. I saw a small truck driven into the entrance of the garage and I saw the driver unload from the end of the truck a number of cases stencilled whiskey. They were the size and appearance of whiskey cases and I believe that they contained whiskey. A search of the records of the Federal Prohibition Director’s office fails to disclose any' permit for the manufacture, sale or possession of intoxicating liquors at the premises above referred to.
 </blockquote>
<blockquote id="b540-4">
  “ The said premises are within the Southern District of New York and upon information and belief, have thereon a quantity of intoxicating liquor containing more than one-half of one per cent of alcohol by volume, and fit for use for beverage purposes, which is used, has been used and is intended for use in violation of the Statute of the United States, to wit,'the National Prohibition Act.
 </blockquote>
<blockquote id="b540-5">
  “ This affidavit is made to procure a search warrant, to search said building at the above address, any building or rooms connected or used in connection with said garage, the basement or sub-cellar beneath the same, and to seize all intoxicating liquors found therein.
 </blockquote>
<blockquote id="b540-6">
<em>
   “
  </em>
  Isidor Einstein.
 </blockquote>
<blockquote id="b540-7">
<em>
   “
  </em>
  Sworn to.before me this 6th day of December, 1922. •Sáml.' M. Hitchcock, U. S. Commissioner, -Southern District of New York.”
 </blockquote>
<p id="b540-8">
  The search warrant issued by, the Commissioner' followed the affidavit in the description of the place and property to be searched and seized and was directed to Einstein as General Prohibition Agent.
 </p>
<p id="b540-9">
  Section 25, Title II, of the National Prohibition Act, c. 85, <span class="citation no-link">41 Stat. 305</span>, 315, provides for the issue of a search
  <span citation-index="1" class="star-pagination" label="501"> 
   *501
   </span>
  warrant to seize liquor and its containers intended for use in violating the Act, and provides that the search warrant shall be issued as provided in Title XI of the Espionage Act of June 15, 1917, c. 30, <span class="citation no-link">40 Stat. 217</span>, 228.
 </p>
<p id="b541-4">
  Under that Title, in conformity with the Fourth Amendment, the warrant can be issued only upon probable cause, supported by affidavit, particularly describing the property and place to be searched. The judge or commissioner must before issuing the warrant examine on oath the complainant and any witness he may produce, and require their affidavits or take their depositions in writing and cause them to be subscribed by the parties making them. The affidavits or depositions must set forth the facts tending to establish the grounds of the application or probable cause for believing that'they exist. If the judge or commissioner is satisfied of the existence of the grounds for the application, or that there is probable cause to believe their existence, he must' issue a search warrant, signed by him with his name of office, to a civil officer of the United States duly authorized to enforce or assist in enforcing any law thereof, stating the particular grounds or probable cause for its issue and the names of the persons whose affidavits have been taken in support thereof, and. commanding him forthwith to search the person or place named, for the property specified, and to bring it before the judge or commissioner. If the grounds on which the warrant was issued be controverted, the judge or commissioner must proceed to take testimony in relation thereto, and the testimony of each witness must be reduced to writing and subscribed by each witness. If it appears that the property taken is not the same as that described in the warrant, or that there is no probable cause for believing the existence of the grounds .on which the warrant was issued, the judge or commissioner must cause The property to be restored to the person from whom it was taken; but if it appears that the
  <span citation-index="1" class="star-pagination" label="502"> 
   *502
   </span>
  property taken is the same as that described in the warrant, and that there is probable cause for believing the existence of the grounds on which the warrant whs issued, then the judge or commissioner shall order the same retained in the custody of the person seizing, or to be otherwise disposed of according to law.
 </p>
<p id="b542-5">
  The facts developed before the Commissioner on hearing this petition for return of the seized goods were these: Einstein and Moe Smith were prohibition agents. They saw a truck depositing cases in a garage on the opposite side of 46th Street from where they were. Einstein crossed the street and saw they were cases stenciled as whiskey. Einstein left his companion to remain in the neighborhood until he could get the warrant, and in somewhat more than an hour returned with it and made the seizure. The building searched w,as a four-story building in New York City on the south side of West 46th Street, with a sign on it: “ Indian Head Auto Truck Service — Indian Head Storage Warehouse, No. 609 and 611.” It was all under lease to Steele. It was entered by three entrances from the street, one on the 609 side, which is used, and which leads to a staircase running up to the four floors. On the 611 side there is .another staircase of a similar character, which is closed, and in the middle of the building is an automobile entrance from the street into a garage, and opposite to the entrance on the south side is an elevator reaching to the four stories, of sufficient size to take up a Ford machine. There is no partition between 611 and 609 on the ground or garage floor, and there were only partial partitions above, and none which prevented access to the- elevator on any floor from either the 609 or 611 side. The evidence left no doubt that, though the building had two numbers, the garage business covering the whole first floor and the storage business above were of such a character and so related to the elevator that there was no real
  <span citation-index="1" class="star-pagination" label="503"> 
   *503
   </span>
  division in fact or in use of the building into separate halves. The places searched and in which the liquor was found were all rooms connected with the garage by the elevator. One of them was a room on the second floor with a door open toward the elevator, in which, when Einstein made his search, three men were bottling and corking whiskey. There was a room on one of the floors, flimsily boarded off, in which an employee had a cot and a cook stove. The prohibition agents seized 150 cases of whiskey, 92 bags of whiskey, and one 5-gallon can of alcohol, on the third floor on the 609 side. On the second floor, 33 cases, of gin were seized on the 609 side, and six 5-gallon jugs of whiskey, 33 cases of gin, 102 quarts of whiskey, and two 50-gallon barrels of whiskey, and a corking machine, were taken on the 611 side of the building.
 </p>
<p id="b543-4">
  The description of the building as a garage and for business purposes at 611 W. 46th Street clearly indicated the whole building as the place intended to be searched. It is enough if the description is such that the officer with a search' warrant can with reasonable effort ascertain and identify the place intended.
  <em>
   Rothlisberger
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8830376"><a href="/opinion/8845128/rothlisberger-v-united-states/" aria-description="Citation for case: Rothlisberger v. United States">289 Fed. 72</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Borkowski,
  </em>
  <span class="citation" data-id="8817957"><a href="/opinion/8832968/united-states-v-borkowski/#411" aria-description="Citation for case: United States v. Borkowski">268 Fed. 408, 411</a></span>;
  <em>
   Commonwealth
  </em>
  v.
  <em>
   Dana,
  </em>
  <span class="citation no-link">2 Metc. 329</span>, 336;
  <em>
   Metcalf
  </em>
  v.
  <em>
   Weed,
  </em>
  66 N. H. 176;
  <em>
   Rose
  </em>
  v.
  <em>
   State,
  </em>
  <span class="citation" data-id="7055656"><a href="/opinion/7147278/rose-v-state/" aria-description="Citation for case: Rose v. State">171 Ind. 662</a></span>;
  <em>
   McSherry
  </em>
  v.
  <em>
   Heimer,
  </em>
  <span class="citation" data-id="7977970"><a href="/opinion/8022410/mcsherry-v-heimer/" aria-description="Citation for case: McSherry v. Heimer">132 Minn. 260</a></span>.
 </p>
<p id="b543-5">
  Nor did the search go too far. A warrant was applied for to search any building or rooms connected or used in connection with the garage, or the basement or sub-cellar beneath the same. It is quite evident that the elevator of the garage connected it with every floor and room in the building and was intended to be used with it.
 </p>
<p id="b543-6">
  The attempt to give the building the character of. a dwelling house by reason of the fact that an employee’ slept and cooked in a room on one of the floors was of
  <span citation-index="1" class="star-pagination" label="504"> 
   *504
   </span>
  course futile. Section 25 of the Prohibition Act forbids the-search of any private dwelling unless it is used for the unlawful sale of intoxicating liquor, or unless it is in'part used for some business purpose, such as a store, shop, saloon, restaurant, hotel or boarding house. It provides that “ private dwelling ” is to be construed to include- the room or rooms used and occupied not transiently but solely as a residence in an apartment house,'.hotel or boarding house. Certainly the room occupied in this case was not a private dwelling within these, descriptions, but more than this, it was not searched and no liquor was found in it.
  <em>
   Forni
  </em>
  v.
  <em>
   United States,
  </em>
  3 Fed. (2d) 354.
 </p>
<p id="b544-4">
  The search warrant properly described the building searched as a garage and one for business purposes.
 </p>
<p id="Ax4">
  Then it is said that the property seized was not sufficiently identified in the warrant.' It was described as “ cases of whiskey/' and while there is no evidence specifically identifying the particular cases which were seized as those which Einstein saw, the description, as “cases of whiskey” is quite specific enough.
  <em>
   Elrod
  </em>
  v.
  <em>
   Moss,
  </em>
  (C. C. A. 4th) <span class="citation" data-id="8823999"><a href="/opinion/8838892/elrod-v-moss/#129" aria-description="Citation for case: Elrod v. Moss">278 Fed. 123, 129</a></span>;
  <em>
   Sutton
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8830471"><a href="/opinion/8845218/sutton-v-united-states/" aria-description="Citation for case: Sutton v. United States">289 Fed. 488</a></span> (C. C. A. 5th);
  <em>
   Tynan
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="6569159"><a href="/opinion/6689467/tynan-v-united-states/" aria-description="Citation for case: Tynan v. United States">297 Fed. 177</a></span> (C. C. A. 9th);
  <em>
   Forni
  </em>
  v.
  <em>
   United States,
  </em>
  3 Fed. (2d) 354 (C. C. A. 9th).
 </p>
<p id="b544-6">
  Finally it- is said there was no probable-cause for the warrant and the seizure. Einstein, a man of experience in such prosecutions and in, such seizures, saw the name “ whiskey ” stenciled on cases and said they looked, like whiskey cases. He ascertained by his own investigation of .the official records that there was no permit for thé legal storage of whiskey on these premises. In a recent case we have had occasion to lay. down what is probable cause for a search.
  <em>
   Carroll
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>. “ If the facts and circumstances before the officer are such as to warrant a man of prudence and caution in
  <span citation-index="1" class="star-pagination" label="505"> 
   *505
   </span>
  believing that the offense has been committed, it is sufficient.” What Einstein saw .and ascertained was quite sufficient to warrant a man of prudence and caution and his experience in believing that the offense had been committed 'of possessing illegally whiskey and intoxicating liquor, and that it was in the building he described.
 </p>
<p id="b545-4">
  The search warrant fully complied with the statutory and constitutional requirements, as set; forth above, the liquor was lawfully seized and the District Court rightly held that it should not be returned.
 </p>
<p id="b545-5">
  The decree is affirmed.
 </p>
<p id="b545-6">
<em>
   Affirmed.
  </em>
</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Stone v. Powell.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Stone v. Powell
type: case
citation: "428 U.S. 465 (1976)"
parallel_cite: "96 S. Ct. 3037; 49 L. Ed. 2d 1067"
neutral_cite: 1976 U.S. LEXIS 86
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-10-04
docket: No. 74-1055
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
  opinion_url: "https://www.courtlistener.com/opinion/109540/stone-v-powell/"
  cluster_id: 109540
  opinion_id: null
  identity_checked: true
lake:
  record_id: Stone v. Powell
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[The Exclusionary Rule]]"
    role: Anchor
related:
  - "[[The Exclusionary Rule]]"
  - "[[Mapp v. Ohio]]"
  - "[[United States v. Calandra]]"
  - "[[United States v. Janis]]"
  - "[[United States v. Leon]]"
tags:
  - case
  - fourth-amendment
  - exclusionary-rule
  - habeas-corpus
  - deterrence
  - collateral-review
holding: "Where the State has provided an opportunity for full and fair litigation of a Fourth Amendment claim, a state prisoner may not be granted federal habeas corpus relief on the ground that evidence obtained in an unconstitutional search or seizure was introduced at his trial; the exclusionary rule's deterrent purpose is not meaningfully served by relitigating settled Fourth Amendment claims on collateral review."
aliases:
  - Stone v. Powell
  - "Stone v. Powell (1976)"
---

# Stone v. Powell

*428 U.S. 465 (1976)* (No. 74-1055) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 109540 → combined opinion 109540 (Powell, J.; 428 U.S. 465, argued Feb. 24, 1976, decided July 6, 1976; consolidated with No. 74-1222, Wolff v. Rice). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*494`). S9 promotes. -->

## Background
Lloyd Powell was convicted of murder in a California state court after a killing during a liquor-store altercation. Ten hours later, a Nevada officer arrested him under a local vagrancy ordinance, and a search incident to that arrest turned up a .38 revolver later identified as the murder weapon. Powell argued the vagrancy ordinance was unconstitutional, so the arrest and search were unlawful and the revolver evidence should have been excluded; he litigated that Fourth Amendment claim in the California courts and lost. He then sought federal [[Common Legal Terms#habeas-corpus|habeas corpus]], and the Ninth Circuit granted relief. In a companion case (*Wolff v. Rice*), a Nebraska prisoner similarly obtained federal [[Common Legal Terms#habeas-corpus|habeas]] relief on a Fourth Amendment claim. The State wardens sought review.

## Issue
Whether a federal court, on a state prisoner's petition for [[Common Legal Terms#habeas-corpus|habeas corpus]], should entertain a claim that evidence obtained in an unconstitutional search or seizure was admitted at trial, when the prisoner already had an opportunity for full and fair litigation of that claim in the state courts.

## Rule
Reasoning that the exclusionary rule is a judicially created deterrent remedy rather than a personal constitutional right, the Court weighed its marginal deterrent value on collateral review against the costs of excluding reliable evidence and disrupting final state judgments, and found the balance decisively against relitigation. It held: "In sum, we conclude that where the State has provided an opportunity for full and fair litigation of a Fourth Amendment claim, a state prisoner may not be granted federal habeas corpus relief on the ground that evidence obtained in an unconstitutional search or seizure was introduced at his trial." — 428 U.S. at 494. ^pin-494

## Application
Whatever added deterrence federal [[Common Legal Terms#habeas-corpus|habeas]] review might supply in isolated cases, it would come long after the police conduct, would fall on officers who had no way to anticipate a later collateral ruling, and would be swamped by the costs to truth-seeking and finality — the diversion of the trial from guilt or innocence, the release of the plainly guilty, and the erosion of respect for the criminal-justice system. Because Powell and Rice had each been afforded a full and fair opportunity to press their Fourth Amendment claims in state court, no further federal [[Common Legal Terms#habeas-corpus|habeas]] remedy was constitutionally required.

## Conclusion
The judgments of the Courts of Appeals were **reversed**. Powell, J., delivered the opinion of the Court. Burger, C.J., filed a [[Common Legal Terms#concurring-opinion|concurring opinion]]; Brennan, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], in which Marshall, J., joined; White, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Stone* is an exclusionary-rule anchor for the deterrence-and-cost framework and its limits on where the rule reaches: on federal [[Common Legal Terms#habeas-corpus|habeas]], a fully and fairly litigated Fourth Amendment claim is not a ground for relief. It belongs with the cost-benefit line — *[[United States v. Calandra]]* (grand jury), *[[United States v. Janis]]* (civil tax), and later *[[United States v. Leon]]* (good faith) — that treats suppression as a deterrent remedy applied only where its benefits outweigh its costs, all downstream of *[[Mapp v. Ohio]]*.

## Appears on
- [[The Exclusionary Rule]] — *Anchor*

## Sources
- [*Stone v. Powell*, 428 U.S. 465 (1976)](https://www.courtlistener.com/opinion/109540/stone-v-powell/) — pinpoint: 494 (Powell, J., for the Court; the CL opinion text places the quoted "In sum" holding between the reporter stars `*494` and `*495`, i.e., on page 494; the dissent cites the same holding as "Ante, at 494"). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a1f66efa3a1a7cd6", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Stone v. Powell"}, "payload": {"all": [{"cite": "428 U.S. 465", "page": "465", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "428"}, {"cite": "96 S. Ct. 3037", "page": "3037", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "96"}, {"cite": "49 L. Ed. 2d 1067", "page": "1067", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "49"}, {"cite": "1976 U.S. LEXIS 86", "page": "86", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1976"}], "display": "428 U.S. 465", "official": {"cite": "428 U.S. 465", "page": "465", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "428"}, "official_selection_present": true, "record_id": "Stone v. Powell"}}
{"assertion_id": "b8484cb334ee5012", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Stone v. Powell"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Stone v. Powell", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Stone v. Powell

```json
{
  "schema_version": "s2.v1",
  "record_id": "Stone v. Powell",
  "status": "under_review",
  "identity": {
    "case_name": "Stone v. Powell",
    "case_name_short": "Powell",
    "case_name_full": "Stone, Warden v. Powell",
    "input_case_name": "Stone v. Powell",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-10-04",
    "year": 1976,
    "docket": "No. 74-1055",
    "cluster_id": 109540,
    "lead_opinion_id": 9426587,
    "sibling_ids": [],
    "absolute_url": "/opinion/109540/stone-v-powell/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "428 U.S. 465",
      "volume": "428",
      "reporter": "U.S.",
      "page": "465",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 3037",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "3037",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 1067",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "1067",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 86",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "86",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "428 U.S. 465",
        "volume": "428",
        "reporter": "U.S.",
        "page": "465",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 3037",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "3037",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 1067",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "1067",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 86",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "86",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "428 U.S. 465",
    "official_selection": {
      "court_class": "scotus",
      "selected": "428 U.S. 465",
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
    "date_created": "2026-07-06T13:42:36Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:42:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:42:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:42:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:42:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "stone-v-powell--109540",
      "to_record_id": "Stone v. Powell",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Stone v. Powell

```
<opinion type="majority">
<author id="b492-4"><page-number citation-index="1" label="468">*468</page-number>Mr. Justice Powell</author>
<p id="A4I">delivered the opinion of the Court.</p>
<p id="b492-5">Respondents in these cases were convicted of criminal offenses in state courts, and their convictions were affirmed on appeal. The prosecution in each case relied upon evidence obtained by searches and seizures alleged by respondents to have been unlawful. Each respondent subsequently sought relief in a Federal District Court by filing a petition for a writ of federal habeas corpus under <page-number citation-index="1" label="469">*469</page-number><span class="citation no-link">28 U. S. C. § 2254</span>. The question presented is whether a federal court should consider, in ruling on a petition for habeas corpus relief filed by a state prisoner, a claim that evidence obtained by an unconstitutional search or seizure was introduced at his trial, when he has previously been afforded an opportunity for full and fair litigation of his claim in the state courts. The issue is of considerable importance to the administration of criminal justice.</p>
<p id="b493-4">I</p>
<p id="b493-5">We summarize first the relevant facts and procedural history of these cases.</p>
<p id="b493-6">A</p>
<p id="b493-7">Respondent Lloyd Powell was convicted of murder in June 1968 after trial in a California state court. At about midnight on February 17, 1968, he and three companions entered the Bonanza Liquor Store in San Ber-nardino, Cal., where Powell became involved in an altercation with Gerald Parsons, the store manager, over the theft of a bottle of wine. In the scuffling that followed Powell shot and killed Parsons’ wife. Ten hours later an officer of the Henderson, Nev., Police Department arrested Powell for violation of the Henderson vagrancy ordinance,<footnotemark>1</footnotemark> and in the search incident to the arrest discovered a .38-caliber revolver with six expended cartridges in the cylinder.</p>
<p id="b493-8">Powell was extradited to California and convicted of <page-number citation-index="1" label="470">*470</page-number>second-degree murder in the Superior Court of San Ber-nardino County. Parsons and Powell’s accomplices at the liquor store testified against him. A criminologist testified that the revolver found on Powell was the gun that killed Parsons’ wife. The trial court rejected Powell’s contention that testimony by the Henderson police officer as to the search and the discovery of the revolver should have been excluded because the vagrancy ordinance was unconstitutional. In October 1969, the conviction was affirmed by a California District Court of Appeal. Although the issue was duly presented, that court found it unnecessary to pass upon the legality of the arrest and search because it concluded that the error, if any, in admitting the testimony of the Henderson officer was harmless beyond a reasonable doubt under <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967). The Supreme Court of California denied Powell’s petition for habeas corpus relief.</p>
<p id="b494-5">In August 1971 Powell filed an amended petition for a writ of federal habeas corpus under <span class="citation no-link">28 U. S. C. § 2254</span> in the United States District Court for the Northern District of California, contending that the testimony concerning the .38-caliber revolver should have been excluded as the fruit of an illegal search. He argued that his arrest had been unlawful because the Henderson vagrancy ordinance was unconstitutionally vague, and that the arresting officer lacked probable cause to believe that he was violating it. The District Court concluded that the arresting officer had probable cause and held that even if the vagrancy ordinance was unconstitutional, the deterrent purpose of the exclusionary rule does not require that it be applied to bar admission of the fruits of a search incident to an otherwise valid arrest. In the alternative, that court agreed with the California District Court of Appeal that the admission of the evidence con<page-number citation-index="1" label="471">*471</page-number>cerning Powell’s arrest, if error, was harmless beyond a reasonable doubt.</p>
<p id="b495-5">In December 1974, the Court of Appeals for the Ninth Circuit reversed. <span class="citation" data-id="323709"><a href="/opinion/323709/lloyd-charles-powell-v-w-t-stone-warden/" aria-description="Citation for case: Lloyd Charles Powell v. W. T. Stone, Warden">507 F. 2d 93</a></span>. The court concluded that the vagrancy ordinance was unconstitutionally vague,<footnotemark>2</footnotemark> that Powell’s arrest was therefore illegal, and that although exclusion of the evidence would serve no deterrent purpose with regard to police officers who were enforcing statutes in good faith, exclusion would serve the public interest by deterring legislators from enacting unconstitutional statutes. <span class="citation" data-id="323709"><a href="/opinion/323709/lloyd-charles-powell-v-w-t-stone-warden/#98" aria-description="Citation for case: Lloyd Charles Powell v. W. T. Stone, Warden"><em>Id., </em>at 98</a></span>. After an independent review of the evidence the court concluded that the admission of the evidence was not harmless error since it supported the testimony of Parsons and Powell’s accomplices. <span class="citation" data-id="323709"><a href="/opinion/323709/lloyd-charles-powell-v-w-t-stone-warden/#99" aria-description="Citation for case: Lloyd Charles Powell v. W. T. Stone, Warden"><em>Id., </em>at 99</a></span>.</p>
<p id="b495-6">B</p>
<p id="b495-7">Respondent David Rice was convicted of murder in April 1971 after trial in a Nebraska state court. At 2:05 a. m. on August 17, 1970, Omaha police received a telephone call that a woman had been heard screaming at 2867 Ohio Street. As one of the officers sent to that address examined a suitcase lying in the doorway, it exploded, killing him instantly. By August 22 the investigation of the murder centered on Duane Peak, a 15-year-old member of the National Committee to Com<page-number citation-index="1" label="472">*472</page-number>bat Fascism (NCCF), and that afternoon a warrant was issued for Peak’s arrest. The investigation also focused on other known members of the NCCF, including Rice, some of whom were believed to be planning to kill Peak before he could incriminate them. In their search for Peak, the police went to Rice’s home at 10:30 that night and found lights and a television on, but there was no response to their repeated knocking. While some officers remained to watch the premises, a warrant was obtained to search for explosives and illegal weapons believed to be in Rice’s possession. Peak was not in the house, but upon entering the police discovered, in plain view, dynamite, blasting caps, and other materials useful in the construction of explosive devices. Peak subsequently was arrested, and on August 27, Rice voluntarily surrendered. The clothes Rice was wearing at that time were subjected to chemical analysis, disclosing dynamite particles.</p>
<p id="b496-5">Rice was tried for first-degree murder in the District Court of Douglas County. At trial Peak admitted planting the suitcase and making the telephone call, and implicated Rice in the bombing plot. As corroborative evidence the State introduced items seized during the search, as well as the results of the chemical analysis of Rice’s clothing. The court denied Rice’s motion to suppress this evidence. On appeal the Supreme Court of Nebraska affirmed the conviction, holding that the search of Rice’s home had been pursuant to a valid search warrant. <em>State </em>v. <em>Rice, </em><span class="citation" data-id="9591942"><a href="/opinion/1346717/state-v-rice/" aria-description="Citation for case: State v. Rice">188 Neb. 728</a></span>, <span class="citation" data-id="9591942"><a href="/opinion/1346717/state-v-rice/" aria-description="Citation for case: State v. Rice">199 N. W. 2d 480</a></span> (1972).</p>
<p id="b496-6">In September 1972 Rice filed a petition for a writ of habeas corpus in the United States District Court for Nebraska. Rice’s sole contention was that his incarceration was unlawful because the evidence underlying his conviction had been discovered as the result of an illegal <page-number citation-index="1" label="473">*473</page-number>search of his home. The District Court concluded that the search warrant was invalid, as the supporting affidavit was defective under <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969), and <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964). <span class="citation" data-id="2313059"><a href="/opinion/2313059/rice-v-wolff/#190" aria-description="Citation for case: Rice v. Wolff">388 F. Supp. 185, 190-194</a></span> (1974).<footnotemark>3</footnotemark> The court also rejected the State’s contention that even if the warrant was invalid the search was justified because of the valid arrest warrant for Peak and because of the exigent circumstances of the situation — danger to Peak and search for bombs and explosives believed in possession of the NCCF. The court reasoned that the arrest warrant did not justify the entry as the police lacked probable cause to believe Peak was in the house, and further concluded that the circumstances were not sufficiently exigent to justify an immediate warrantless <page-number citation-index="1" label="474">*474</page-number>search. <span class="citation" data-id="2313059"><a href="/opinion/2313059/rice-v-wolff/#194" aria-description="Citation for case: Rice v. Wolff"><em>Id., </em>at 194-202</a></span>.<footnotemark>4</footnotemark> The Court of Appeals for the Eighth Circuit affirmed, substantially for the reasons stated by the District Court. <span class="citation" data-id="326825"><a href="/opinion/326825/david-l-rice-v-charles-l-wolff-jr-warden-nebraska-penal-and/" aria-description="Citation for case: David L. Rice v. Charles L. Wolff, Jr., Warden, Nebraska...">513 F. 2d 1280</a></span> (1975).</p>
<p id="b498-5">Petitioners Stone and Wolff, the wardens of the respective state prisons where Powell and Rice are incarcerated, petitioned for review of these decisions, raising questions concerning the scope of federal habeas corpus and the role of the exclusionary rule upon collateral review of cases involving Fourth Amendment claims. We granted their petitions for certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./422/1055/">422 U. S. 1055</a></span> (1975).<footnotemark>5</footnotemark> We now reverse.</p>
<p id="b498-6">II</p>
<p id="b498-7">The authority of federal courts to issue the writ of habeas corpus <em>ad subjiciendum </em><footnotemark>6</footnotemark> was included in the first <page-number citation-index="1" label="475">*475</page-number>grant of federal-court jurisdiction, made by the Judiciary Act of 1789, c. 20, § 14, <span class="citation no-link">1 Stat. 81</span>, with the limitation that the writ extend only to prisoners held in custody by the United States. The original statutory authorization did not define the substantive reach of the writ. It merely stated that the courts of the United States “shall have power to issue writs of . . . <em>habeas corpus . . . <span class="citation no-link">Ibid.</span> </em>The courts defined the scope of the writ in accordance with the common law and limited it to an inquiry as to the jurisdiction of the sentencing tribunal. See, <em>e. g., Ex parte Watkins, </em><span class="citation" data-id="85668"><a href="/opinion/85668/ex-parte-tobias-watkins/" aria-description="Citation for case: Ex Parte Tobias Watkins">3 Pet. 193</a></span> (1830) (Marshall, C. J.).</p>
<p id="b499-5">In 1867 the writ was extended to state prisoners. Act of Feb. 5, 1867, c. 28, § 1, <span class="citation no-link">14 Stat. 385</span>. Under the 1867 Act federal courts were authorized to give relief in “all cases where any person may be restrained of his or her liberty in violation of the constitution, or of any treaty or law of the United States . . . .” But the limitation of federal habeas corpus jurisdiction to consideration of the jurisdiction of the sentencing court persisted. See'; <em>e. g., In re Wood, </em><span class="citation" data-id="93092"><a href="/opinion/93092/in-re-wood/" aria-description="Citation for case: In Re Wood">140 U. S. 278</a></span> <em>(1891); In re Rahrer, </em><span class="citation" data-id="93112"><a href="/opinion/93112/in-re-rahrer/" aria-description="Citation for case: In Re Rahrer">140 U. S. 545</a></span> (1891); <em>Andrews </em>v. <em>Swartz, </em><span class="citation" data-id="94093"><a href="/opinion/94093/andrews-v-swartz/" aria-description="Citation for case: Andrews v. Swartz">156 U. S. 272</a></span> (1895); <em>Bergemann </em>v. <em>Backer, </em><span class="citation" data-id="94176"><a href="/opinion/94176/bergemann-v-backer/" aria-description="Citation for case: Bergemann v. Backer">157 U. S. 655</a></span> (1895); <em>Pettibone </em>v. <em>Nichols, </em><span class="citation" data-id="9418069"><a href="/opinion/96517/pettibone-v-nichols/" aria-description="Citation for case: Pettibone v. Nichols">203 U. S. 192</a></span> (1906). And, although the concept of “jurisdiction” was subjected to considerable strain as the substantive scope of the writ was expanded,<footnotemark>7</footnotemark> this <page-number citation-index="1" label="476">*476</page-number>expansion was limited to only a few classes of cases<footnotemark>8</footnotemark> until <em>Frank </em>v. <em>Mangum, </em><span class="citation" data-id="9418283"><a href="/opinion/98441/frank-v-mangum/" aria-description="Citation for case: Frank v. Mangum">237 U. S. 309</a></span>, in 1915. In <em><span class="citation" data-id="9418283"><a href="/opinion/98441/frank-v-mangum/" aria-description="Citation for case: Frank v. Mangum">Frank</a></span>, </em>the prisoner had claimed in the state courts that the proceedings which resulted in his conviction for murder had been dominated by a mob. After the State Supreme Court rejected his contentions, Frank unsuccessfully sought habeas corpus relief in the Federal District Court. This Court affirmed the denial of relief because Frank’s federal claims had been considered by a competent and unbiased state tribunal. The Court recognized, however, that if a habeas corpus court found that the State had failed to provide adequate “corrective process” for the full and fair litigation of federal claims, whether or not “jurisdictional,” the court could inquire into the merits to determine whether a detention was lawful. <em>Id,., </em>at 333-336.</p>
<p id="b500-5">In the landmark decision in <em>Brown </em>v. <em>Allen, </em><span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#482" aria-description="Citation for case: Brown v. Allen">344 U. S. 443, 482-487</a></span> (1953), the scope of the writ was expanded still further.<footnotemark>9</footnotemark> In that case and its companion case, <em>Daniels </em>v. <em><span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">Allen</a></span>, </em>state prisoners applied for federal habeas corpus relief claiming that the trial courts had erred <page-number citation-index="1" label="477">*477</page-number>in failing to quash their indictments due to alleged discrimination in the selection of grand jurors and in ruling certain confessions admissible. In <em><span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">Brown</a></span>, </em>the highest court of the State had rejected these claims oil direct appeal, <em>State </em>v. <em>Brown, </em><span class="citation" data-id="1242993"><a href="/opinion/1242993/state-v-brown/" aria-description="Citation for case: State v. Brown">233 N. C. 202</a></span>, <span class="citation" data-id="1242993"><a href="/opinion/1242993/state-v-brown/" aria-description="Citation for case: State v. Brown">63 S. E. 2d 99</a></span>, and this Court had denied certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./341/943/">341 U. S. 943</a></span> (1951). Despite the apparent adequacy of the state corrective process, the Court reviewed the denial of the writ of habeas corpus and held that Brown was entitled to a full reconsideration of these constitutional claims, including, if appropriate, a hearing in the Federal District Court. In <em>Daniels, </em>however, the State Supreme Court on direct review had refused to consider the appeal because the papers were filed out of time. This Court held that since the state-court judgment rested on a reasonable application of the State’s legitimate procedural rules, a ground that would have barred direct review of his federal claims by this Court, the District Court lacked authority to grant habeas corpus relief. See <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#458" aria-description="Citation for case: Brown v. Allen">344 U. S., at 458, 486</a></span>.</p>
<p id="b501-5">This final barrier to broad collateral re-examination of state criminal convictions in federal habeas corpus proceedings was removed in <em>Fay </em>v. <em>Noia, </em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">372 U. S. 391</a></span> (1963) .<footnotemark>10</footnotemark> Noia and two codefendants had been convicted <page-number citation-index="1" label="478">*478</page-number>of felony murder. The sole evidence against each defendant was a signed confession. Noia’s codefendants, but not Noia himself, appealed their convictions. Although their appeals were unsuccessful, in subsequent state proceedings they were able to establish that their confessions had been coerced and their convictions therefore procured in violation of the Constitution. In a subsequent federal habeas corpus proceeding, it was stipulated that Noia’s confession also had been coerced, but the District Court followed <em>Daniels </em>in holding that Noia’s failure to appeal barred habeas corpus review. See <em>United States </em>v. <em>Fay, </em><span class="citation" data-id="1973566"><a href="/opinion/1973566/united-states-ex-rel-noia-v-fay/#225" aria-description="Citation for case: United States Ex Rel. Noia v. Fay">183 F. Supp. 222, 225</a></span> (SDNY 1960). The Court of Appeals reversed, ordering that Noia’s conviction be set aside and that he be released from custody or that a new trial be granted. This Court affirmed the grant of the writ, narrowly restricting the circumstances in which a federal court may refuse to consider the merits of federal constitutional claims<footnotemark>11</footnotemark></p>
<p id="AeAh">During the period in which the substantive scope of the writ was expanded, the Court did not consider whether exceptions to full review might exist with respect <page-number citation-index="1" label="479">*479</page-number>to particular categories of constitutional claims. Prior to the Court’s decision in <em>Kaufman </em>v. <em>United States, </em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">394 U. S. 217</a></span> (1969), however, a substantial majority of the Federal Courts of Appeals had concluded that collateral review of search-and-seizure claims was inappropriate on motions filed by federal prisoners under <span class="citation no-link">28 U. S. C. § 2255</span>, the modem postconviction procedure available to federal prisoners in lieu of habeas corpus.<footnotemark>12</footnotemark> The primary rationale advanced in support of those decisions was that Fourth Amendment violations are different in kind from denials of Fifth or Sixth Amendment rights in that claims of illegal search and seizure do not “impugn the integrity of the fact-finding process or challenge evidence as inherently unreliable; rather, the exclusion of illegally seized evidence is simply a prophylactic device intended generally to deter Fourth Amendment violations by law enforcement officers.” <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#224" aria-description="Citation for case: Kaufman v. United States">394 U. S., at 224</a></span>. See <em>Thornton </em>v. <em>United States, </em>125 U. S. App. D. C. 114, <span class="citation" data-id="9452299"><a href="/opinion/273740/charles-j-thornton-v-united-states/" aria-description="Citation for case: Charles J. Thornton v. United States">368 F. 2d 822</a></span> (1966).</p>
<p id="b503-5"><em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span> </em>rejected this rationale and held that search- and-seizure claims are cognizable in § 2255 proceedings. The Court noted that “the federal habeas remedy extends to state prisoners alleging that unconstitutionally obtained evidence was admitted against them at trial,” <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#225" aria-description="Citation for case: Kaufman v. United States">394 U. S., at 225</a></span>, citing, <em>e. g., Mancusi </em>v. <em>DeForte, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 <page-number citation-index="1" label="480">*480</page-number>U. S. 364</a></span> (1968); <em>Carafas </em>v. <em>LaVallee, </em><span class="citation" data-id="9423702"><a href="/opinion/107689/carafas-v-lavallee/" aria-description="Citation for case: Carafas v. LaVallee">391 U. S. 234</a></span> (1968), and concluded, as a matter of statutory construction, that there was no basis for restricting “access by federal prisoners with illegal search-and-seizure claims to federal collateral remedies, while placing no similar restriction on access by state prisoners,” <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#226" aria-description="Citation for case: Kaufman v. United States">394 U. S., at 226</a></span>. Although in recent years the view has been expressed that the Court should re-examine the substantive scope of federal habeas jurisdiction and limit collateral review of search-and-seizure claims “solely to the question of whether the petitioner was provided a fair opportunity to raise and have adjudicated the question in state courts,” <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#250" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 250</a></span> (1973) (Powell, J., concurring),<footnotemark>13</footnotemark> the Court, without discussion or consideration of the issue, has continued to accept jurisdiction in cases raising such claims. See <em>Lefkowitz </em>v. <em>Newsome, </em><span class="citation" data-id="9426003"><a href="/opinion/109196/lefkowitz-v-newsome/" aria-description="Citation for case: Lefkowitz v. Newsome">420 U. S. 283</a></span> (1975); <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span> (1973); <em>Cardwell </em>v. <em>Lewis, </em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583</a></span> (1974) (plurality opinion).<footnotemark>14</footnotemark></p>
<p id="b504-5">The discussion in <em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span> </em>of the scope of federal habeas corpus rests on the view that the effectuation of the Fourth Amendment, as applied to the States through the Fourteenth Amendment, requires the granting of habeas corpus relief when a prisoner has been con<page-number citation-index="1" label="481">*481</page-number>victed in state court on the basis of evidence obtained in an illegal search or seizure since those Amendments were held in <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), to require exclusion of such evidence at trial and reversal of conviction upon direct review.<footnotemark>15</footnotemark> Until these cases we have not had occasion fully to consider the validity of this view. See, <em>e. g., Schneckloth </em>v. <em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Bustamonte, supra,</a></span> </em>at 249 n. 38; <em>Cardwell </em>v. <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#596" aria-description="Citation for case: Cardwell v. Lewis"><em>Lewis, supra, </em>at 596</a></span>, and n. 12. Upon examination, we conclude, in light of the nature and purpose of the Fourth Amendment exclusionary rule, that this view is unjustified.<footnotemark>16</footnotemark> We hold, therefore, that <page-number citation-index="1" label="482">*482</page-number>where .the State has provided an opportunity for full and fair litigation of a Fourth Amendment claim, the Constitution does not require that a.state prisoner be granted federal habeas corpus relief on the ground that evidence obtained in an unconstitutional search or seizure was introduced at his trial.<footnotemark>17</footnotemark></p>
<p id="b506-5">Ill</p>
<p id="b506-6">The Fourth Amendment assures the “right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures.” The Amendment was primarily a reaction to the evils associated with the use of the general warrant in England and the writs of assistance in the Colonies, <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481-485</a></span> (1965); <em>Frank </em>v. <em>Maryland, </em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#363" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360, 363-365</a></span> (1959), and was intended to protect the “sanctity of a man’s home and the privacies of life,” <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span> (1886), from searches under unchecked general authority.<footnotemark>18</footnotemark></p>
<p id="b506-7">The exclusionary rule was a judicially created means of effectuating the rights secured by the Fourth Amendment. Prior to the Court’s decisions in <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), and <em>Gouled </em>v. <em>United States, </em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span> (1921), there existed no barrier to the introduction in criminal trials of evidence obtained in violation of the Amendment. See <em>Adams </em>v. <em>New York, </em><page-number citation-index="1" label="483">*483</page-number><span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U. S. 585</a></span> (1904).<footnotemark>19</footnotemark> In <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>the Court held that the defendant could petition before trial for the return of property secured through an illegal search or seizure conducted by federal authorities. In <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>the Court held broadly that such evidence could not be introduced in a federal prosecution. See <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#304" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 304-305</a></span> (1967). See also <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920) (fruits of illegally seized evidence). Thirty-five years after <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>the Court held in <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span> (1949), that the right to be free from arbitrary intrusion by the police that is protected by the Fourth Amendment is “implicit in 'the concept of ordered liberty’ and as such enforceable against the States through the [Fourteenth Amendment] Due Process Clause.” <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado"><em>Id., </em>at 27-28</a></span>. The Court concluded, however, that the <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>exclusionary rule would not be imposed upon the States as “an essential ingredient of [that] right.” <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#29" aria-description="Citation for case: Wolf v. Colorado">338 U. S., at 29</a></span>. The -full force of <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span> </em>was eroded in subsequent decisions, see <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S. 206</a></span> (1960); <em>Rea </em>v. <em>United States, </em><span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/" aria-description="Citation for case: Rea v. United States">350 U. S. 214</a></span> (1956), and a little more than a decade later the exclusionary rule was held applicable to the States in <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961).</p>
<p id="b508-4"><page-number citation-index="1" label="484">*484</page-number>Decisions prior to <em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span> </em>advanced two principal reasons for application of the rule in federal trials. The Court in <em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">Elkins</a></span>, </em>for example, in the context of its special supervisory role over the lower federal courts, referred to the “imperative of judicial integrity,” suggesting that exclusion of illegally seized evidence prevents contamination of the judicial process. <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#222" aria-description="Citation for case: Elkins v. United States">364 U. S., at 222</a></span>.<footnotemark>20</footnotemark> But even in that context a more pragmatic ground was emphasized:</p>
<blockquote id="b508-5">“The rule is calculated to prevent, not to repair. Its purpose is to deter — to compel respect for the constitutional guaranty in the only effectively available way — by removing the incentive to disregard it.” <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States"><em>Id., </em>at 217</a></span>.</blockquote>
<p id="b508-6">The <em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span> </em>majority justified the application of the rule to the States on several grounds,<footnotemark>21</footnotemark> but relied principally upon the belief that exclusion would deter future unlawful police conduct. <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#658" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 658</a></span>.</p>
<p id="b509-4"><page-number citation-index="1" label="485">*485</page-number>Although our decisions often have alluded to the “imperative of judicial integrity,” <em>e. g., United States </em>v. <em>Peltier, </em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#536" aria-description="Citation for case: United States v. Peltier">422 U. S. 531, 536-539</a></span> (1975), they demonstrate the limited role of this justification in the determination whether to apply the rule in a particular context.<footnotemark>22</footnotemark> Logically extended this justification would require that courts exclude unconstitutionally seized evidence despite lack of objection by the defendant, or even over his assent. Cf. <em>Henry </em>v. <em>Mississippi, </em><span class="citation" data-id="9422929"><a href="/opinion/106962/henry-v-mississippi/" aria-description="Citation for case: Henry v. Mississippi">379 U. S. 443</a></span> (1965). It also would require abandonment of the standing limitations on who may object to the introduction of unconstitutionally seized evidence, <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span> (1969), and retreat from the proposition that judicial proceedings need not abate when the defendant’s person is unconstitutionally seized, <em>Gerstein </em>v. <em>Pugh, </em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#119" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 119</a></span> (1975); <em>Frisbie </em>v. <em>Collins, </em><span class="citation" data-id="104977"><a href="/opinion/104977/frisbie-v-collins/" aria-description="Citation for case: Frisbie v. Collins">342 U. S. 519</a></span> (1952). Similarly, the interest in promoting judicial integrity does not prevent the use of illegally seized evidence in grand jury proceedings. <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">414 U. S. 338</a></span> (1974). Nor does it require that the trial court exclude such evidence from use for impeachment of a defendant, even though its introduction is certain to result in conviction in some cases. <em>Walder </em>v. <em>United States, </em><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span> (1954). The teaching of these cases is clear. While courts, of course, must ever be concerned with preserving the integrity of the judicial process, this concern has limited force as a justification for the exclusion of highly probative evidence.<footnotemark>23</footnotemark> <page-number citation-index="1" label="486">*486</page-number>The force of this justification becomes minimal where federal habeas corpus relief is sought by a prisoner who previously has been afforded the opportunity for full and fair consideration of his search-and-seizure claim at trial and on direct review.</p>
<p id="b510-4">The primary justification for the exclusionary rule then is the deterrence of police conduct that violates Fourth Amendment rights. <em>Post-Mapp </em>decisions have established that the rule is not a personal constitutional right. It is not calculated to redress the injury to the privacy of the victim of the search or seizure, for any “ [r] eparation comes too late.” <em>Linkletter </em>v. <em>Walker, </em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#637" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 637</a></span> (1965). Instead,</p>
<blockquote id="b510-5">“the rule is a judicially created remedy designed to safeguard Fourth Amendment rights generally through its deterrent effect . . . .” <em>United States </em>v. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>.</blockquote>
<p id="b510-6">Accord, <em>United States </em>v. <span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#538" aria-description="Citation for case: United States v. Peltier"><em>Peltier, supra, </em>at 538-539</a></span>; <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#28" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 28-29</a></span> (1968); <em>Linkletter </em>v. <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#636" aria-description="Citation for case: Linkletter v. Walker"><em>Walker, supra, </em>at 636-637</a></span>; <em>Tehan </em>v. <em>United States ex rel. Shott, </em><span class="citation" data-id="6751647"><a href="/opinion/6862154/tehan-v-united-states-ex-rel-shott/#416" aria-description="Citation for case: Tehan v. United States ex rel. Shott">382 U. S. 406, 416</a></span> (1966).</p>
<p id="b510-7"><em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span> </em>involved the enforcement of the exclusionary rule at state trials and on direct review. The decision in <em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span>, </em>as noted above, is premised on the view that implementation of the Fourth Amendment also requires the consideration of search-and-seizure claims upon collateral review of state convictions. But despite the broad deterrent purpose of the exclusionary rule, it has never been interpreted to proscribe the introduction of illegally seized evidence in all proceedings or against all persons. As in the case of any remedial device, “the application of the rule has been restricted to those areas where its reme<page-number citation-index="1" label="487">*487</page-number>dial objectives are thought most efficaciously served.” <em>United States </em>v. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>.<footnotemark>24</footnotemark> Thus, our refusal to extend the exclusionary rule to grand jury proceedings was based on a balancing of the potential injury to the historic role and function of the grand jury by such extension against the potential contribution to the effectuation of the Fourth Amendment through deterrence of police misconduct:</p>
<blockquote id="b511-5">“Any incremental deterrent effect which might be achieved by extending the rule to grand jury proceedings is uncertain at best. Whatever deterrence of police misconduct may result from the exclusion of illegally seized evidence from criminal trials, it is unrealistic to assume that application of the rule to grand jury proceedings would significantly further that goal. Such an extension would deter only police investigation consciously directed toward the discovery of evidence solely for use in a grand jury investigation. . . . We therefore decline to embrace a view that would achieve a speculative and undoubtedly minimal advance in the deterrence of police misconduct at the expense of substantially <page-number citation-index="1" label="488">*488</page-number>impeding the role of the grand jury.” <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#351" aria-description="Citation for case: United States v. Calandra">414 U. S., at 351-352</a></span> (footnote omitted).</blockquote>
<p id="b512-5">The same pragmatic analysis of the exclusionary rule’s usefulness in a particular context was evident earlier in <em>Walder </em>v. <em>United </em>States, <em>supra, </em>where the Court permitted the Government to use unlawfully seized evidence to impeach the credibility of a defendant who had testified broadly in his own defense. The Court held, in effect, that the interests safeguarded by the exclusionary rule in that context were outweighed by the need to prevent perjury and to assure the integrity of the trial process. The judgment in <em><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span> </em>revealed most clearly that the policies behind the exclusionary rule are not absolute. Rather, they must be evaluated in light of competing policies. In that case, the public interest in determination of truth at trial<footnotemark>25</footnotemark> was deemed to outweigh the incremental contribution that might have been made to the protection of Fourth Amendment values by application of the rule.</p>
<p id="b512-6">The balancing process at work in these cases also finds expression in the standing requirement. Standing to invoke the exclusionary rule has been found to exist only when the Government attempts to use illegally obtained evidence to incriminate the victim of the illegal search. <em>Brown </em>v. <em>United States, </em><span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/" aria-description="Citation for case: Brown v. United States">411 U. S. 223</a></span> (1973); <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span> (1969); <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#491" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 491-492</a></span> (1963). See <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 261</a></span> (1960). The standing requirement is premised on the view that the “additional benefits of extending the . . . rule” to defendants other than the victim of the search or seizure are outweighed by the “further encroachment upon the <page-number citation-index="1" label="489">*489</page-number>public interest in prosecuting those accused of crime and having them acquitted or convicted on the basis of all the evidence which exposes the truth." <em>Alderman </em>v. <em>United States, supra, </em>at 174-175.<footnotemark>26</footnotemark></p>
<p id="b513-5">IV</p>
<p id="b513-6">We turn now to the specific question presented by these cases. Respondents allege violations of Fourth Amendment rights guaranteed them through the Fourteenth Amendment. The question is whether state prisoners— who have been afforded the opportunity for full and fair consideration of their reliance upon the exclusionary rule with respect to seized evidence by the state courts at trial and on direct review — may invoke their claim again on federal habeas corpus review. The answer is to be found by weighing the utility of the exclusionary rule against the costs of extending it to collateral review of Fourth Amendment claims.</p>
<p id="b513-7">The costs of applying the exclusionary rule even at trial and on direct review are well known: <footnotemark>27</footnotemark> the focus <page-number citation-index="1" label="490">*490</page-number>of the trial, and the attention of the participants therein, are diverted from the ultimate question of guilt or innocence that should be the central concern in a criminal proceeding.<footnotemark>28</footnotemark> Moreover, the physical evidence sought to be excluded is typically reliable and often the most probative information bearing on the guilt or innocence of the defendant. As Mr. Justice Black emphasized in his dissent in <em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span>:</em></p>
<blockquote id="b514-5"><em>“A </em>claim of illegal search and seizure under the Fourth Amendment is crucially different from many other constitutional rights; ordinarily the evidence seized can in no way have been rendered untrustworthy by the means of its seizure and indeed often this evidence alone establishes beyond virtually any shadow of a doubt that the defendant is guilty.” 394 U. S., at 237.</blockquote>
<p id="b514-6">Application of the rule thus deflects the truthfinding process and often frees the guilty. The disparity in particular cases between the error committed by the police officer and the windfall afforded a guilty defendant by application of the rule is contrary to the idea of proportionality that is essential to the concept of justice.<footnotemark>29</footnotemark> Thus, <page-number citation-index="1" label="491">*491</page-number>although the rule is thought to deter unlawful police activity in part through the nurturing of respect for Fourth Amendment values, if applied indiscriminately it may well have the opposite effect of generating disrespect for the law and administration of justice.<footnotemark>30</footnotemark> These long-recognized costs of the rule persist when a criminal conviction is sought to be overturned on collateral review on the ground that a search-and-seizure claim was erroneously rejected by two or more tiers of state courts.<footnotemark>31</footnotemark></p>
<p id="b516-4"><page-number citation-index="1" label="492">*492</page-number>Evidence obtained by police officers in violation of the Fourth Amendment is excluded at trial in the hope that the frequency of future violations will decrease. Despite the absence of supportive empirical evidence,<footnotemark>32</footnotemark> we have assumed that the immediate effect of exclusion will be to discourage law enforcement officials from violating the Fourth Amendment by removing the incentive to disregard it. More importantly, over the long term, this demonstration that our society attaches serious consequences to violation of constitutional rights is thought to encourage those who formulate law enforcement policies, and the officers who implement them, to incorporate Fourth Amendment ideals into their value system.<footnotemark>33</footnotemark></p>
<p id="b517-4"><page-number citation-index="1" label="493">*493</page-number>We adhere to the view that these considerations support the implementation of the exclusionary rule at trial and its enforcement on direct appeal of state-court convictions. But the additional contribution, if any, of the consideration of search-and-seizure claims of state prisoners on collateral review is small in relation to the costs. To be sure, each case in which such claim is considered may add marginally to an awareness of the values protected by the Fourth Amendment. There is no reason to believe, however, that the overall educative effect of the exclusionary rule would be appreciably diminished if search-and-seizure claims could not be raised in federal habeas corpus review of state convictions.<footnotemark>34</footnotemark> Nor is there reason to assume that any specific disincentive already created by the risk of exclusion of evidence at trial or the reversal of convictions on direct review would be enhanced if there were the further risk that a conviction obtained in state court and affirmed on direct review might be overturned in collateral proceedings often occurring years after the incarceration of the defendant. The view that the deterrence of Fourth Amendment violations would be furthered rests on the dubious assumption that law enforcement authorities would fear that federal habeas review might reveal flaws in a search or seizure that went undetected at trial and on appeal.<footnotemark>35</footnotemark> Even if one rationally could assume that <page-number citation-index="1" label="494">*494</page-number>some additional incremental deterrent effect would be present in isolated cases, the resulting advance of the legitimate goal of furthering Fourth Amendment rights would be outweighed by the acknowledged costs to other values vital to a rational system of criminal justice.</p>
<p id="b518-5">In sum, we conclude that where the State has provided an opportunity for full and fair litigation of a Fourth Amendment claim,<footnotemark>36</footnotemark> a state prisoner may not be granted federal habeas corpus relief on the ground that evidence obtained in an unconstitutional search or seizure was introduced at his trial.<footnotemark>37</footnotemark> In this context the <page-number citation-index="1" label="495">*495</page-number>contribution of the exclusionary rule, if any, to the effec-tuation of the Fourth Amendment is minimal and the substantial societal costs of application of the rule persist with special force.<footnotemark>38</footnotemark></p>
<p id="b520-3"><page-number citation-index="1" label="496">*496</page-number>Accordingly, the judgments of the Courts of Appeals are</p>
<p id="b520-4">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b493-9"> The ordinance provides:</p>
<blockquote id="b493-10">“Every person is a vagrant wbo:</blockquote>
<blockquote id="b493-11">“[1] Loiters or wanders upon the streets or from place to place without apparent reason or business and [2] who refuses to identify himself and to account for his presence when asked by a police officer to do so [3] if surrounding circumstances are such as to indicate to a reasonable man that the public safety demands such identification.”</blockquote>
</footnote>
<footnote label="2">
<p id="b495-8"> In support of the vagueness holding the court relied principally on <em>Papachristou </em>v. <em>Jacksonville, </em><span class="citation" data-id="108472"><a href="/opinion/108472/papachristou-v-city-of-jacksonville/" aria-description="Citation for case: Papachristou v. City of Jacksonville">405 U. S. 156</a></span> (1972), where we invalidated a city ordinance in part defining vagrants as "persons wandering or strolling around from place to place without any lawful purpose or object . . . <span class="citation" data-id="108472"><a href="/opinion/108472/papachristou-v-city-of-jacksonville/#156" aria-description="Citation for case: Papachristou v. City of Jacksonville"><em>Id., </em>at 156-157, n. 1</a></span>. Noting the similarity between the first element of the Henderson ordinance, see n. 1, <em>supra, </em>and the Jacksonville ordinance, it concluded that the second and third elements of the Henderson ordinance were not sufficiently specific to cure its overall vagueness. <span class="citation" data-id="323709"><a href="/opinion/323709/lloyd-charles-powell-v-w-t-stone-warden/#95" aria-description="Citation for case: Lloyd Charles Powell v. W. T. Stone, Warden">507 F. 2d, at 95-97</a></span>. Petitioner Stone challenges these conclusions, but in view of our disposition of the case we need not consider this issue.</p>
</footnote>
<footnote label="3">
<p id="b497-5"> The sole evidence presented to the magistrate was the affidavit in support of the warrant application. It indicated that the police believed explosives and illegal weapons were present in Rice’s home because (1) Rice was an official of the NCCF, (2) a violent killing of an officer had occurred and it appeared that the NCCF was involved, and (3) police had received information in the past that Rice possessed weapons and explosives, which he had said should be used against the police. See <span class="citation" data-id="2313059"><a href="/opinion/2313059/rice-v-wolff/" aria-description="Citation for case: Rice v. Wolff">388 F. Supp., at 189</a></span> n. 1. In concluding that there existed probable cause for issuance of the warrant, although the Nebraska Supreme Court found the affidavit alone sufficient, it also referred to information contained in testimony adduced at the suppression hearing but not included in the affidavit. <span class="citation" data-id="9591942"><a href="/opinion/1346717/state-v-rice/#738" aria-description="Citation for case: State v. Rice">188 Neb. 728, 738-739</a></span>, <span class="citation" data-id="9591942"><a href="/opinion/1346717/state-v-rice/#487" aria-description="Citation for case: State v. Rice">199 N. W. 2d 480, 487-488</a></span>. See also <span class="citation" data-id="9591942"><a href="/opinion/1346717/state-v-rice/#754" aria-description="Citation for case: State v. Rice"><em>id., </em>at 754</a></span>, <span class="citation" data-id="9591942"><a href="/opinion/1346717/state-v-rice/#495" aria-description="Citation for case: State v. Rice">199 N. W. 2d, at 495</a></span> (concurring opinion). The District Court limited its probable-cause inquiry to the face of the affidavit, see <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 413</a></span> n. 3; <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 109</a></span> n. 1, and concluded probable cause was lacking. Petitioner Wolff contends that police should be permitted to supplement the information contained in an affidavit for a search warrant at the hearing on a motion to suppress, a contention that we have several times rejected, see, <em>e. g., Whiteley </em>v. <em>Warden, </em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560</a></span>, 565 n. 8 (1971); <em>Aguilar </em>v. <em>Texas, supra, </em>at 109 n. 1, and need not reach again here.</p>
</footnote>
<footnote label="4">
<p id="b498-8"> The District Court further held that the evidence of dynamite particles found on Rice’s clothing should have been suppressed as the tainted fruit of an arrest warrant that would not have been issued but for the unlawful search of his home. <span class="citation" data-id="2313059"><a href="/opinion/2313059/rice-v-wolff/#202" aria-description="Citation for case: Rice v. Wolff">388 F. Supp., at 202-207</a></span>. See <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963); <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920).</p>
</footnote>
<footnote label="5">
<p id="b498-9"> In the orders granting certiorari in these cases we requested that counsel in <em>Stone </em>v. <em>Powell </em>and <em>Wolff </em>v. <em><span class="citation" data-id="9591942"><a href="/opinion/1346717/state-v-rice/" aria-description="Citation for case: State v. Rice">Rice</a></span> </em>respectively address the questions:</p>
<blockquote id="b498-10">“Whether, in light of the fact that the District Court found that the Henderson, Nev., police officer had probable cause to arrest respondent for violation of an ordinance which at the time of the arrest had not been authoritatively determined to be unconstitutional, respondent’s claim that the gun discovered as a result of a search incident to that arrest violated his rights under the Fourth and Fourteenth Amendments to the United States Constitution is one cognizable under <span class="citation no-link">28 U. S. C. §2254</span>.</blockquote>
<blockquote id="b498-11">“Whether the constitutional validity of the entry and search of respondent’s premises by Omaha police officers under the circumstances of this case is a question properly cognizable under <span class="citation no-link">28 U. S. C. § 2254</span>.”</blockquote>
</footnote>
<footnote label="6">
<p id="b498-12"> It is now well established that the phrase “habeas corpus” used alone refers to the common-law writ of habeas corpus <em>ad subjicien-</em><page-number citation-index="1" label="475">*475</page-number><em>dum, </em>known as the “Great Writ.” <em>Ex parte Bollman, </em><span class="citation" data-id="9416259"><a href="/opinion/84842/ex-parte-bollman-and-swartwout/#95" aria-description="Citation for case: Ex Parte Bollman and Swartwout">4 Cranch 75, 95</a></span> (1807) (Marshall, C. J.).</p>
</footnote>
<footnote label="7">
<p id="b499-8"> Prior to 1889 there was, in practical effect, no appellate review in federal criminal cases. The possibility of Supreme Court review on certificate of division of opinion in the circuit court was remote because of the practice of single district judges’ holding circuit court. See P. Bator, P. Mishkin, E&gt;. Shapiro, &amp; H. Wechsler, Hart &amp; Wech-sler’s The Federal Courts and the Federal System 1539-1540 (2d ed. 1973); F. Frankfurter &amp; J. Landis, The Business of the Supreme Court 31-32, 79-80, and n. 107 (1927). Pressure naturally developed for expansion of the scope of habeas corpus to reach otherwise <page-number citation-index="1" label="476">*476</page-number>unreviewable decisions involving fundamental rights. See <em>Ex parte Siebold, </em><span class="citation" data-id="90042"><a href="/opinion/90042/ex-parte-siebold/#376" aria-description="Citation for case: Ex Parte Siebold">100 U. S. 371, 376-377</a></span> (1880); Bator, Finality in Criminal Law and Federal Habeas Corpus For State Prisoners, <span class="citation no-link">76 Harv. L. Rev. 441</span>, 473, and n. 75 (1963).</p>
</footnote>
<footnote label="8">
<p id="b500-10"> The expansion occurred primarily with regard to (i) convictions based on assertedly unconstitutional statutes, <em>e. g., Ex parte <span class="citation" data-id="90042"><a href="/opinion/90042/ex-parte-siebold/" aria-description="Citation for case: Ex Parte Siebold">Siebold, supra,</a></span> </em>or (ii) detentions based upon an allegedly illegal sentence, <em>e. g., Ex parte Lange, </em><span class="citation" data-id="9416939"><a href="/opinion/88804/ex-parte-lange/" aria-description="Citation for case: Ex Parte Lange">18 Wall. 163</a></span> (1874). See Bator, <em>supra, </em>n. 7, at 465-474.</p>
</footnote>
<footnote label="9">
<p id="b500-11"> There has been disagreement among scholars as to whether the result in <em>Brown </em>v. <em><span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">Allen</a></span> </em>was foreshadowed by the Court’s decision in <em>Moore </em>v. <em>Dempsey, </em><span class="citation" data-id="9418497"><a href="/opinion/100122/moore-v-dempsey/" aria-description="Citation for case: Moore v. Dempsey">261 U. S. 86</a></span> (1923). Compare Hart, Foreword: The Time Chart of the Justices, <span class="citation no-link">73 Harv. L. Rev. 84</span>, 105 (1959); Reitz, Federal Habeas Corpus; Impact of an Abortive State Proceeding, <span class="citation no-link">74 Harv. L. Rev. 1315</span>, 1328-1329 (1961), with Bator, <em>supra, </em>n. 7, at 488-491. See also <em>Fay </em>v. <em>Noia, </em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#421" aria-description="Citation for case: Fay v. Noia">372 U. S. 391, 421</a></span>, and n. 30 (1963); <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#457" aria-description="Citation for case: Fay v. Noia"><em>id., </em>at 457-460</a></span> (Harlan, J., dissenting).</p>
</footnote>
<footnote label="10">
<p id="b501-6"> Despite the expansion of the scope of the writ, there has been no change in the established rule with respect to nonconstitutional claims. The writ of habeas corpus and its federal counterpart, <span class="citation no-link">28 U. S. C. § 2255</span>, “will not be allowed to do service for an appeal.” <em>Sunal </em>v. <em>Large, </em><span class="citation" data-id="8163802"><a href="/opinion/8201865/sunal-v-large/#178" aria-description="Citation for case: Sunal v. Large">332 U. S. 174, 178</a></span> (1947). For this reason, non-constitutional claims that could have been raised on appeal, but were not, may not be asserted in collateral proceedings. <span class="citation" data-id="8163802"><a href="/opinion/8201865/sunal-v-large/#178" aria-description="Citation for case: Sunal v. Large"><em>Id., </em>at 178-179</a></span>; <em>Davis </em>v. <em>United States, </em><span class="citation" data-id="9425745"><a href="/opinion/109059/davis-v-united-states/#345" aria-description="Citation for case: Davis v. United States">417 U. S. 333, 345-346</a></span>, and n. 15 (1974). Even those nonconstitutional claims that could not have been asserted on direct appeal can be raised on collateral review only if the alleged error constituted “ 'a fundamental defect which inherently results in a complete miscarriage of justice,’ ” <span class="citation" data-id="9425745"><a href="/opinion/109059/davis-v-united-states/#346" aria-description="Citation for case: Davis v. United States"><em>id., </em>at 346</a></span>, quoting <em>Hill </em>v. <em>United States, </em><span class="citation" data-id="9422329"><a href="/opinion/106329/hill-v-united-states/#428" aria-description="Citation for case: Hill v. United States">368 U. S. 424, 428</a></span> (1962).</p>
</footnote>
<footnote label="11">
<p id="b502-5"> In construing broadly the power of a federal district court to consider constitutional claims presented in a petition for writ of habeas corpus, the Court in <em>Fay </em>also reaffirmed the equitable nature of the writ, noting that “[discretion is implicit in the statutory command that the judge . . . 'dispose of the matter as law and justice require.’ <span class="citation no-link">28 U. S. C. §2243</span>.” <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#438" aria-description="Citation for case: Fay v. Noia">372 U. S., at 438</a></span>. More recently, in <em>Francis </em>v. <em>Henderson, </em><span class="citation" data-id="9426387"><a href="/opinion/109439/francis-v-henderson/" aria-description="Citation for case: Francis v. Henderson">425 U. S. 536</a></span> (1976), holding that a state prisoner who failed to malee a timely challenge to the composition of the grand jury that indicted him cannot bring such a challenge in a post-conviction federal habeas corpus proceeding absent a claim of actual prejudice, we emphasized:</p>
<blockquote id="b502-6">“This Court has long recognized that in some circumstances considerations of comity and concerns for the orderly administration of criminal justice require a federal court to forgo the exercise of its habeas corpus power. See <em>Fay </em>v. <em>Noia, </em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#425" aria-description="Citation for case: Fay v. Noia">372 U. S. 391, 425-426</a></span>.” <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#539" aria-description="Citation for case: Fay v. Noia"><em>Id., </em>at 539</a></span>.</blockquote>
</footnote>
<footnote label="12">
<p id="b503-6"> Compare, <em>e. g., United States </em>v. <em>Re, </em><span class="citation" data-id="9452511"><a href="/opinion/274722/united-states-v-gerardo-a-re-also-known-as-jerry-a-re-and-gerard-f-re/" aria-description="Citation for case: United States v. Gerardo A. Re, Also Known as Jerry A. Re...">372 F. 2d 641</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./388/912/">388 U. S. 912</a></span> (1967); <em>United States </em>v. <em>Jenkins, </em><span class="citation" data-id="251645"><a href="/opinion/251645/united-states-v-ernest-jenkins/" aria-description="Citation for case: United States v. Ernest Jenkins">281 F. 2d 193</a></span> (CA3 1960); <em>Eisner </em>v. <em>United States, </em><span class="citation" data-id="269188"><a href="/opinion/269188/samson-eisner-v-united-states/" aria-description="Citation for case: Samson Eisner v. United States">351 F. 2d 55</a></span> (CA6 1965); <em>De Welles </em>v. <em>United States, </em><span class="citation" data-id="274584"><a href="/opinion/274584/roy-w-de-welles-v-united-states/" aria-description="Citation for case: Roy W. De Welles v. United States">372 F. 2d 67</a></span> (CA7), cert denied, <span class="citation multiple-matches"><a href="/c/U.%20S./388/919/">388 U. S. 919</a></span> (1967); <em>Williams </em>v. <em>United States, </em><span class="citation" data-id="258120"><a href="/opinion/258120/joseph-kenneth-williams-v-united-states/" aria-description="Citation for case: Joseph Kenneth Williams v. United States">307 F. 2d 366</a></span> (CA9 1962); <em>Armstead </em>v. <em>United States, </em><span class="citation" data-id="260927"><a href="/opinion/260927/george-armstead-v-united-states/" aria-description="Citation for case: George Armstead v. United States">318 F. 2d 725</a></span> (CA5 1963), with, <em>e. g., United States </em>v. <em>Sutton, </em><span class="citation" data-id="261495"><a href="/opinion/261495/united-states-v-paul-sutton/" aria-description="Citation for case: United States v. Paul Sutton">321 F. 2d 221</a></span> (CA4 1963); <em>Gaitan </em>v. <em>United States, 317 </em>F. 2d 494 (CA10 1963). See also <em>Thornton </em>v. <em>United States, </em>125 U. S. App. D. C. 114, <span class="citation" data-id="9452299"><a href="/opinion/273740/charles-j-thornton-v-united-states/" aria-description="Citation for case: Charles J. Thornton v. United States">368 F. 2d 822</a></span> (1966) (search-and-seizure claims not cognizable under § 2255 absent special circumstances).</p>
</footnote>
<footnote label="13">
<p id="b504-6"> See, <em>e. g., </em>Friendly, Is Innocence Irrelevant? Collateral Attack on Criminal Judgments, 38 U. CM. L. Rev. 142 (1970).</p>
</footnote>
<footnote label="14">
<p id="b504-7"> In <em><span class="citation" data-id="9426003"><a href="/opinion/109196/lefkowitz-v-newsome/" aria-description="Citation for case: Lefkowitz v. Newsome">Newsome</a></span> </em>the Court focused on the issue whether a state defendant’s plea of guilty waives federal habeas corpus review where state law does not foreclose review of the plea on direct appeal, and did not consider the substantive scope of the writ. See 420 U. S., at 287 n. 4. Similarly, in <em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/" aria-description="Citation for case: Cardwell v. Lewis">Cardwell</a></span> </em>and <em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Cady</a></span> </em>the question considered here was not presented in the petition for certiorari, and in neither case was relief granted on the basis of a search-and-seizure claim. In <em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/" aria-description="Citation for case: Cardwell v. Lewis">Cardwell</a></span> </em>the plurality expressly noted that it was not addressing the issue of the substantive scope of the writ. See 417 U. S., at 596, and a. 12.</p>
</footnote>
<footnote label="15">
<p id="b505-5"> As Mr. Justice Black commented in dissent, 394 U. S., at 231, 239, the <em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span> </em>majority made no effort to justify its result in light of the long-recognized deterrent purpose of the exclusionary rule. Instead, the Court relied on a series of prior cases as implicitly establishing the proposition that search-and-seizure claims are cognizable in federal habeas corpus proceedings. See <em>Mancusi </em>v. <em>DeForte, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364</a></span> (1968); <em>Carafas </em>v. <em>LaValee, </em><span class="citation" data-id="9423702"><a href="/opinion/107689/carafas-v-lavallee/" aria-description="Citation for case: Carafas v. LaVallee">391 U. S. 234</a></span> (1968); <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967). But only in <em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">Mancusi</a></span> </em>did this Court order habeas relief on the basis of a search-and-seizure claim, and in that case, as well as in <em>Warden, </em>the issue of the substantive scope of the writ was not presented to the Court in the petition for writ of certiorari. Moreover, of the other “numerous occasions” cited by Mr. Justice BreNNAN’s dissent, <em>post, </em>at 518-519, in which the Court has accepted jurisdiction over collateral attacks by state prisoners raising Fourth Amendment claims, in only one <em>case</em>—Whiteley v. <em>Warden, </em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560</a></span> (1971)—was relief granted on that basis. And in <em>Whiteley, </em>as in <em>Man-cusi, </em>the issue of the substantive scope of the writ was not presented in the petition for certiorari. As emphasized by Mr. Justice Black, only in the most exceptional cases will we consider issues not raised in the petition. 394 U. S., at 239, and n. 7.</p>
</footnote>
<footnote label="16">
<p id="b505-6"> The issue in <em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span> </em>was the scope of § 2255. Our decision today rejects the dictum in <em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span> </em>concerning the applicability of the exclusionary rule in federal habeas corpus review of state-court decisions pursuant to § 2254. To the extent the application of the exclusionary rule in <em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span> </em>did not rely upon the supervisory role of this Court over the lower federal courts, cf. <em>Elkins </em>v. <page-number citation-index="1" label="482">*482</page-number><em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S. 206</a></span> (1960), see <em>infra, </em>at 484, the rationale for its application in that context is also rejected.</p>
</footnote>
<footnote label="17">
<p id="b506-9"> We find it unnecessary to consider the other issues concerning the exclusionary rule, or the statutory scope of the habeas corpus statute, raised by the parties. These include, principally, whether in view of the purpose of the rule, it should be applied on a <em>per se </em>basis without regard to the nature of the constitutional claim or the circumstances of the police action.</p>
</footnote>
<footnote label="18">
<p id="b506-10"> See generally J. Landynski, Search and Seizure and the Supreme Court (1966); N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution (1937).</p>
</footnote>
<footnote label="19">
<p id="b507-4"> The roots of the <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>decision lay in an early decision, <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886), where the Court held that the compulsory production of a person’s private books and papers for introduction against him at trial violated the Fourth and Fifth Amendments. <em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>, </em>however, had been severely limited in <em>Adams </em>v. <em><span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">New York</a></span>, </em>where the Court, emphasizing that the “law held unconstitutional [in Boyd] virtually compelled the defendant to furnish testimony against himself,” <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/#598" aria-description="Citation for case: Adams v. New York">192 U. S., at 598</a></span>, adhered to the common-law rule that a trial court must not inquire, on Fourth Amendment grounds, into the method by which otherwise competent evidence was acquired. See, <em>e. g., Commonwealth </em>v. <em>Dana, </em><span class="citation" data-id="6407794"><a href="/opinion/6534076/commonwealth-v-dana/" aria-description="Citation for case: Commonwealth v. Dana">43 Mass. 329</a></span> (1841).</p>
</footnote>
<footnote label="20">
<p id="b508-7"> See <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#12" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 12-13</a></span> (1968); <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#391" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 391-392, 394</a></span> (1914); <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#470" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 470</a></span> (1928) (Holmes, J., dissenting); <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#484" aria-description="Citation for case: Olmstead v. United States"><em>id., </em>at 484</a></span> (Brandéis, J., dissenting).</p>
</footnote>
<footnote label="21">
<p id="b508-8"> See <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#656" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 656</a></span> (prevention of introduction of evidence where introduction is “tantamount” to a coerced confession); <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#658" aria-description="Citation for case: Mapp v. Ohio"><em>id., </em>at 658</a></span> (deterrence of Fourth Amendment violations); <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#659" aria-description="Citation for case: Mapp v. Ohio"><em>id., </em>at 659</a></span> (preservation of judicial integrity).</p>
<p id="b508-9">Only four Justices adopted the view that the Fourth Amendment itself requires the exclusion of unconstitutionally seized evidence in state criminal trials. See <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#656" aria-description="Citation for case: Mapp v. Ohio"><em>id., </em>at 656</a></span>; <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#666" aria-description="Citation for case: Mapp v. Ohio"><em>id., </em>at 666</a></span> (Douglas, J., concurring). Mr. Justice Black adhered to his view that the Fourth Amendment, standing alone, was not sufficient, see <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#39" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 39</a></span> (1949) (concurring opinion), but concluded that, when the Fourth Amendment is considered in conjunction with the Fifth Amendment ban against compelled self-incrimination, a constitutional basis emerges for requiring exclusion. <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#661" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 661</a></span> (concurring opinion). See n. 19, <em>supra.</em></p>
</footnote>
<footnote label="22">
<p id="b509-5"> See Monaghan, Foreword: Constitutional Common Law, <span class="citation no-link">89 Harv. L. Rev. 1</span>,- 5 — 6, and n. 33 (1975).</p>
</footnote>
<footnote label="23">
<p id="b509-6"> As we recognized last Term, judicial integrity is “not offended if law enforcement officials reasonably believed in good faith that their conduct was in accordance with the law even if decisions subsequent to the search and seizure have held that conduct of the type engaged in by the law enforcement officials is not permitted by the <page-number citation-index="1" label="486">*486</page-number>Constitution.” <em>United States </em>v. <em>Peltier, </em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#538" aria-description="Citation for case: United States v. Peltier">422 U. S. 531, 538</a></span> (1975) (emphasis omitted).</p>
</footnote>
<footnote label="24">
<p id="b511-6"> As Professor Amsterdam has observed:</p>
<blockquote id="b511-7">“The rule is unsupportable as reparation or compensatory dispensation to the injured criminal; its sole rational justification is the experience of its indispensability in fexert[ing] general legal pressures to secure obedience to the Fourth Amendment on the part of . . . law-enforcing officers.’ As it serves this function, the rule is a needed, but grud[g]ingly taken, medicament; no more should be swallowed than is needed to combat the disease. Granted that so many criminals must go free as will deter the constables from blundering, pursuance of this policy of liberation beyond the confines of necessity inflicts gratuitous harm on the public interest . . . .” Search, Seizure, and Section 2255: A Comment, <span class="citation no-link">112 U. Pa. L. Rev. 378</span>, 388-389 (1964) (footnotes omitted).</blockquote>
</footnote>
<footnote label="25">
<p id="b512-7"> See generally M. Frankel, The Search For Truth — An Umpireal View, 31st Annual Benjamin N. Cardozo Lecture, Association of the Bar of the City of New York, Dec. 16, 1974.</p>
</footnote>
<footnote label="26">
<p id="b513-8"> Cases addressing the question, whether search-and-seizure holdings should be applied retroactively also have focused on the deterrent purpose served by the exclusionary rule, consistently with the balancing analysis applied generally in the exclusionary rule context. See <em>Desist </em>v. <em>United States, </em><span class="citation" data-id="9423951"><a href="/opinion/107875/desist-v-united-states/#249" aria-description="Citation for case: Desist v. United States">394 U. S. 244, 249-251, 253-254</a></span>, and n. 21 (1969); <em>Linkletter </em>v. <em>Walker, </em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#636" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 636-637</a></span> (1965). Cf. <em>Fuller </em>v. <em>Alaska, </em><span class="citation" data-id="9423835"><a href="/opinion/107788/fuller-v-alaska/#81" aria-description="Citation for case: Fuller v. Alaska">393 U. S. 80, 81</a></span> (1968). The “attenuation-of-t-he-taint” doctrine also is consistent with the balancing approach. See <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975); <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#491" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 491-492</a></span>; Amsterdam, <em>supra, </em>n. 24, at 389-390.</p>
</footnote>
<footnote label="27">
<p id="b513-9"> See, <em>e. g., Irvine </em>v. <em>California, </em><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#136" aria-description="Citation for case: Irvine v. California">347 U. S. 128, 136</a></span> (1954); <em>Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#411" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388, 411</a></span> (1971) (Burger, C. J., dissenting); <em>People </em>v. <em>Defore, </em><span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">242 N. Y. 13</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">150 N. E. 585</a></span> (1926) (Cardozo, J.); 8 J. Wigmore, Evidence § 2184a, pp. 51-52 (McNaughton ed. 1961); Amsterdam, <em>supra, </em>n. 24, at 388-391; Friendly, <em>supra, </em>n. 13, at 161; Oaks, Studying the Exclusionary Rule in Search and Seizure, <span class="citation no-link">37 U. Chi. L. Rev. 665</span>, 736-754 (1970), and <page-number citation-index="1" label="490">*490</page-number>sources cited therein; Paulsen, The Exclusionary Rule and Misconduct by the Police, 52 J. Crim. L. C. &amp; P. S. 255, 256 (1961); Wright, Must the Criminal Go Free If the Constable Blunders?, <span class="citation no-link">50 Tex. L. Rev. 736</span> (1972).</p>
</footnote>
<footnote label="28">
<p id="b514-8"> See address by Justice Schaefer of the Supreme Court of Illinois, Is the Adversary System Working in Optimal Fashion?, delivered at the National Conference on the Causes of Popular Dissatisfaction With the Administration of Justice, pp. 8-9, Apr. 8, 1976; cf. Frankel, <em>supra, </em>n. 25.</p>
</footnote>
<footnote label="29">
<p id="b514-9"> Many of the proposals for modification of the scope of the exclusionary rule recognize at least implicitly the role of proportionality in the criminal justice system and the potential value of establishing a direct relationship between the nature of the violation and the decision whether to invoke the rule. See ALI, A <page-number citation-index="1" label="491">*491</page-number>Model Code of Pre-arraignment Procedure, § 290.2, pp. 181-183 (1975) (“substantial violations”); H. Friendly, Benchmarks 260-262 (1967) (even at trial, exclusion should be limited to “the fruit of activity intentionally or flagrantly illegal”); 8 Wigmore, <em>supra, </em>n. 27, at 52-53. See n. 17, <em>supra.</em></p>
</footnote>
<footnote label="30">
<p id="b515-6"> In a different context, Dallin H. Oaks has observed:</p>
<blockquote id="b515-7">“I am criticizing, not our concern with procedures, but our preoccupation, in which we may lose sight of the fact that our procedures are not the ultimate goals of our legal system. Our goals are truth and justice, and procedures are but means to these ends. . . .</blockquote>
<blockquote id="b515-8">“Truth and justice are ultimate values, so understood by our people, and the law and the legal profession will not be worthy of public respect and loyalty if we allow our attention to be diverted from these goals.” Ethics, Morality and Professional Responsibility, 1975 B. Y. U. L. Rev. 591, 596.</blockquote>
</footnote>
<footnote label="31">
<p id="b515-9"> Resort to habeas corpus, especially for purposes other than to assure that no innocent person suffers an unconstitutional loss of liberty, results in serious intrusions on values important to our system of government. They include “(i) the most effective utilization of limited judicial resources, (ii) the necessity of finality in criminal trials, (iii) the minimization of friction between our federal and state systems of justice, and (iv) the maintenance of the constitutional balance upon which the doctrine of federalism is founded.” <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#259" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., at 259</a></span> (Powell, J., concurring). See also <em>Kaufman </em>v. <em>United States, </em>394 U. S., at 231 (Black, J., dissenting); Friendly, <em>supra, </em>n. 13.</p>
<p id="b515-10">We nevertheless afford broad habeas corpus relief, recognizing the need in a free society for an additional safeguard against <page-number citation-index="1" label="492">*492</page-number>compelling an innocent man to suffer an unconstitutional loss of liberty. The Court in <em>Fay </em>v. <em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">Noia</a></span> </em>described habeas corpus as a remedy for “whatever society deems to be intolerable restraints,” and recognized that those to whom the writ should be granted “are persons whom society has grievously wronged.” <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#401" aria-description="Citation for case: Fay v. Noia">372 U. S., at 401, 441</a></span>. But in the case of a typical Fourth Amendment claim, asserted on collateral attack, a convicted defendant is usually asking society to redetermine an issue that has no bearing on the basic justice of his incarceration.</p>
</footnote>
<footnote label="32">
<p id="b516-6"> The efficacy of the exclusionary rule has long been the subject of sharp debate. Until recently, scholarly empirical research was unavailable. <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#218" aria-description="Citation for case: Elkins v. United States">364 U. S., at 218</a></span>, And, the evidence derived from recent empirical research is still inconclusive. Compare, <em>e. g., </em>Oaks, <em>supra, </em>n. 27; Spiotto, Search and Seizure: An Empirical Study of the Exclusionary Rule and Its Alternatives, 2 J. Legal Studies 243 (1973), with, <em>e. g., </em>Canon, Is the Exclusionary Rule in Failing Health?, Some New Data an,d a Plea Against a Precipitous Conclusion, 62 Ky. L. J. 681 (1974). See <em>United States </em>v. <em>Janis, ante, </em>at 450-452, n. 22; Amsterdam, Perspectives on the Fourth Amendment, <span class="citation no-link">58 Minn. L. Rev. 349</span>, 475 n. 593 (1974); Comment, On the Limitations of Empirical Evaluations of the Exclusionary Rule: A Critique of the Spiotto Research and United States v. Calandra, <span class="citation no-link">69 Nw. U. L. Rev. 740</span> (1974).</p>
</footnote>
<footnote label="33">
<p id="b516-7"> See Oaks, <em>supra, </em>n. 27, at 756.</p>
</footnote>
<footnote label="34">
<p id="b517-5"> “As the exclusionary rule is applied time after time, it seems that its deterrent efficacy at some stage reaches a point of diminishing returns, and beyond that point its continued application is a public nuisance.” Amsterdam, <em>supra, </em>n. 24, at 389.</p>
</footnote>
<footnote label="35">
<p id="b517-6"> The policy arguments that respondents marshal in support of the view that federal habeas corpus review is necessary to effectuate the Fourth Amendment stem from a basic mistrust of the state courts as fair and competent forums for the adjudication of federal constitutional rights. The argument is that state courts cannot be trusted to effectuate Fourth Amendment values through <page-number citation-index="1" label="494">*494</page-number>fair application of the rule, and the oversight jurisdiction of this Court on certiorari is an inadequate safeguard. The principal rationale for this view emphasizes the broad differences in the respective institutional settings within which federal judges and state judges operate. Despite differences in institutional environment and the unsympathetic attitude to federal constitutional claims of some state judges in years past, we are unwilling to assume that there now exists a general lack of appropriate sensitivity to constitutional rights in the trial and appellate courts of the several States. State courts, like federal courts, have a constitutional obligation to safeguard personal liberties and to uphold federal law. <em>Martin </em>v. <em>Hunter’s Lessee, </em><span class="citation" data-id="85160"><a href="/opinion/85160/martin-v-hunters-lessee/#341" aria-description="Citation for case: Martin v. Hunter&#x27;s Lessee">1 Wheat. 304, 341-344</a></span> (1816). Moreover, the argument that federal judges are more expert in applying federal constitutional law is especially unpersuasive in the context of search-and-seizure claims, since they are dealt with on a daily basis by trial level judges in both systems. In sum, there is “no intrinsic reason why the fact that a man is a federal judge should make him more competent, or conscientious, or learned with respect to the [consideration of Fourth Amendment claims] than his neighbor in the state courthouse.” Bator, <em>supra, </em>n. 7, at 509.</p>
</footnote>
<footnote label="36">
<p id="b518-7"> Cf. <em>Townsend </em>v. <em>Sain, </em><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">372 U. S. 293</a></span> (1963).</p>
</footnote>
<footnote label="37">
<p id="b518-8"> Mr. Justice Brennan’s dissent characterizes the Court’s opinion as laying the groundwork for a “drastic withdrawal of federal habeas jurisdiction, if not for all grounds . . . , then at least [for many] <em>Post, </em>at 517. It refers variously to our opinion as a “novel reinterpretation of the habeas statutes,” <em>post, </em>at 515; as a “harbinger of future eviscerations of the habeas statutes,” <em>post, </em>at 516; as “rewriting] Congress’ jurisdictional statutes . . . and [bar<page-number citation-index="1" label="495">*495</page-number>ring] access to federal courts by state prisoners with constitutional claims distasteful to a majority” of the Court, <em>post, </em>at 522; and as a “denigration of constitutional guarantees [that] must appall citizens taught to expect judicial respect” of constitutional rights, <em>post, </em>at 523.</p>
<p id="b519-6">With all respect, the hyperbole of the dissenting opinion is misdirected. Our decision today is <em>not </em>concerned with the scope of the habeas corpus statute as authority for litigating constitutional claims generally. We do reaffirm that the exclusionary rule is a judicially created remedy rather than a personal constitutional right, see <em>supra, </em>at 486, and we emphasize the minimal utility of the rule when sought to be applied to Fourth Amendment claims in a habeas corpus proceeding. As Mr. Justice Black recognized in this context, “ordinarily the evidence seized can in no way have been rendered untrustworthy . . . and indeed often . . . alone establishes beyond virtually any shadow of a doubt that the defendant is guilty.” <em>Kaufman </em>v. <em>United States, </em>394 U. S., at 237 (dissenting opinion). In sum, we hold only that a federal court need not apply the exclusionary rule on habeas review of a Fourth Amendment claim absent a showing that the state prisoner was denied an opportunity for a full and fair litigation of that claim at trial and on direct review. Our decision does not mean that the federal court lacks jurisdiction over such a claim, but only that the application of the rule is limited to cases in which there has been both such a showing and a Fourth Amendment violation.</p>
</footnote>
<footnote label="38">
<p id="b519-7"> See n. 31, <em>supra. </em>Respondents contend that since they filed petitions for federal habeas corpus rather than seeking direct review by this Court through an application for a writ of certiorari, and since the time to apply for certiorari has now passed, any diminution in their ability to obtain habeas corpus relief on the ground evidence obtained in an unconstitutional search or seizure was introduced at their trials should be prospective. Cf. <em>England </em>v. <em>Louisiana State Board of Medical Examiners, </em><span class="citation" data-id="9422712"><a href="/opinion/106729/england-v-louisiana-state-board-of-medical-examiners/#422" aria-description="Citation for case: England v. Louisiana State Board of Medical Examiners">375 U. S. 411, 422-423</a></span> (1964). We reject these contentions. Although not required to do so under the Court’s prior decisions, see <em>Fay </em>v. <em>Noia, </em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">372 U. S. 391</a></span> (1963), respondents were, of course, free to file a timely petition for certiorari prior to seeking federal habeas corpus relief.</p>
</footnote>
</opinion>
```

---
