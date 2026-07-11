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

## GROUP: _overhaul2/lake/cases/State v. Demesme.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: State v. Demesme
type: case
citation: "228 So. 3d 1206 (2017)"
parallel_cite: ""
neutral_cite: 2017 WL 4876733
court: La. 2017
court_level: state
circuit: ""
year: 2017
date_decided: 2017-10-27
docket: No. 2017-KK-0954
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
  opinion_url: "https://www.courtlistener.com/opinion/5035127/state-v-demesme/"
  cluster_id: 5035127
  opinion_id: null
  identity_checked: true
lake:
  record_id: State v. Demesme
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: Key
related:
  - "[[Miranda Waiver and Invocation]]"
  - "[[Edwards v. Arizona]]"
tags:
  - case
  - fifth-amendment
  - miranda
  - right-to-counsel
  - invocation
  - ambiguous-request
  - davis
holding: "The Louisiana Supreme Court denied review of a suppression ruling; in a solo concurrence, Justice Crichton wrote that the defendant's ambiguous reference to a 'lawyer dog' was not an unambiguous request for counsel under Davis v. United States and so did not require officers to stop questioning."
---

# State v. Demesme

*228 So. 3d 1206 (La. 2017)* (No. 2017-KK-0954) · Supreme Court of Louisiana · **Persuasive — state, illustrative** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 5035127 → per curiam writ denial (opinion 4848796) + Crichton, J., concurrence (opinion 4848797); 228 So. 3d 1206, decided 2017-10-27. Quote string-matched to the CL opinion text 2026-07-07. NOTE: this is a writ denial + single-justice concurrence, not a merits holding — see Rule/Treatment. S9 promotes. -->

## Background
Warren Demesme was interviewed twice about alleged sexual misconduct with minors. Both times detectives gave *[[Miranda v. Arizona|Miranda]]* warnings, which he acknowledged and waived. During the second interview he made an equivocal remark, embedded in a longer sentence, that referenced wanting a lawyer — the request the courts would go on to scrutinize. The trial court declined to suppress his statements, and Demesme sought review in the Louisiana Supreme Court, arguing that he had invoked his right to counsel.

## Issue
Whether a suspect's ambiguous or equivocal reference to counsel during a *[[Miranda v. Arizona|Miranda]]* interview obligates officers to cease questioning.

## Rule
The Louisiana Supreme Court **denied the writ application** without a merits opinion. Justice Crichton concurred, writing separately to explain his view under the governing federal standard. Applying the rule of *[[Davis v. United States]]* — that questioning need not cease when a suspect's reference to counsel is so ambiguous or equivocal that a reasonable officer would understand only that he *might* be invoking the right — he concluded: "In my view, the defendant's ambiguous and equivocal reference to a 'lawyer dog' does not constitute an invocation of counsel." — 228 So. 3d at 1206 (Crichton, J., concurring). ^pin-crichton

## Application
On the [[Common Legal Terms#concurring-opinion|concurrence]]'s reasoning, Demesme's earlier valid *[[Miranda v. Arizona|Miranda]]* waivers remained in effect, and his later reference to a "lawyer dog," embedded in an equivocal sentence, would not have communicated to a reasonable officer a clear, present demand for counsel under the *[[Davis v. United States|Davis]]* clear-articulation rule. Because the request was not unambiguous, *[[Edwards v. Arizona|Edwards]]*'s bar on continued interrogation was not triggered.

## Conclusion
The writ application was **denied**; the suppression ruling was left undisturbed. Justice Crichton concurred; no [[Common Legal Terms#majority-opinion|majority opinion]] issued.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified; posture caveat below.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Demesme* is procedurally a **writ denial**, and its widely-cited reasoning appears only in **Justice Crichton's solo [[Common Legal Terms#concurring-opinion|concurrence]]** — it is not a binding merits holding of the Louisiana Supreme Court. It is included as a notable (and much-debated) illustration of the *[[Davis v. United States]]* rule that an ambiguous invocation of counsel does not require police to stop questioning; the [[Common Legal Terms#concurring-opinion|concurrence]]'s parsing of "lawyer dog" drew national attention to how courts apply the clear-articulation requirement.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key*

## Sources
- [*State v. Demesme*, 228 So. 3d 1206 (La. 2017) (Crichton, J., concurring)](https://www.courtlistener.com/opinion/5035127/state-v-demesme/) — writ denial; quote from the concurring opinion, string-matched to the CL opinion text 2026-07-07. Applies *Davis v. United States*, 512 U.S. 452 (1994).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0dcbaa258a053172", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "State v. Demesme"}, "payload": {"all": [{"cite": "228 So. 3d 1206", "page": "1206", "reporter": "So. 3d", "selected_official": false, "source": "cluster.citations[]", "type": 3, "volume": "228"}, {"cite": "2017 WL 4876733", "page": "4876733", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2017"}], "display": "228 So. 3d 1206", "official": {"cite": "228 So. 3d 1206", "page": "1206", "reporter": "So. 3d", "selected_official": true, "source": "cluster.citations[]", "type": 3, "volume": "228"}, "official_selection_present": true, "record_id": "State v. Demesme"}}
{"assertion_id": "8b1583523a7e4d64", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "State v. Demesme"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "State v. Demesme", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — State v. Demesme

```json
{
  "schema_version": "s2.v1",
  "record_id": "State v. Demesme",
  "status": "under_review",
  "identity": {
    "case_name": "State v. Demesme",
    "case_name_short": "Demesme",
    "case_name_full": "STATE of Louisiana v. Warren DEMESME",
    "input_case_name": "State v. Demesme",
    "court": "La. 2017",
    "court_id": "la",
    "court_level": "state",
    "circuit": null,
    "state": "la",
    "date_decided": "2017-10-27",
    "year": 2017,
    "docket": "No. 2017-KK-0954",
    "cluster_id": 5035127,
    "lead_opinion_id": 4848796,
    "sibling_ids": [],
    "absolute_url": "/opinion/5035127/state-v-demesme/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "228 So. 3d 1206",
      "volume": "228",
      "reporter": "So. 3d",
      "page": "1206",
      "type": 3,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2017 WL 4876733",
        "volume": "2017",
        "reporter": "WL",
        "page": "4876733",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "228 So. 3d 1206",
        "volume": "228",
        "reporter": "So. 3d",
        "page": "1206",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 WL 4876733",
        "volume": "2017",
        "reporter": "WL",
        "page": "4876733",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "228 So. 3d 1206",
    "official_selection": {
      "court_class": "state",
      "selected": "228 So. 3d 1206",
      "reason": "selected_rank_2"
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
    "date_created": "2026-07-06T05:48:20Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:48:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:48:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:48:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:48:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "state-v-demesme--5035127",
      "to_record_id": "State v. Demesme",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — State v. Demesme

```
<opinion type="majority"> <p id="b1276-14" pgmap="1276">ON WRIT OF CERTIORARI TO THE COURT OF APPEAL, FOURTH CIRCUIT, PARISH OF ORLEANS</p> <p id="b1276-15" pgmap="1276">Writ denied.</p> </opinion>
```

---

## GROUP: _overhaul2/lake/cases/State v. Karston.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: State v. Karston
type: case
citation: "588 So. 2d 165 (1991)"
parallel_cite: ""
neutral_cite: 1991 WL 205679
court: La. Ct. App. 1991
court_level: state
circuit: ""
year: 1991
date_decided: 1991-10-15
docket: 91-K-1134
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
  opinion_url: "https://www.courtlistener.com/opinion/1767998/state-v-karston/"
  cluster_id: 1767998
  opinion_id: null
  identity_checked: true
lake:
  record_id: State v. Karston
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Curtilage]]"
    role: Key
related:
  - "[[Curtilage]]"
  - "[[Florida v. Jardines]]"
  - "[[Katz v. United States]]"
tags:
  - case
  - fourth-amendment
  - search
  - curtilage
  - reasonable-expectation-of-privacy
  - state-court
holding: "A tenant has a reasonable expectation of privacy in the fenced, gated common courtyard of a private apartment complex; an officer who, without probable cause or reasonable suspicion, opens a closed (though unlocked) gate and enters that courtyard to establish surveillance conducts an unreasonable search, so evidence derived from the resulting warrant must be suppressed."
---

# State v. Karston

*588 So. 2d 165 (La. Ct. App. 1991)* (No. 91-K-1134) · Court of Appeal of Louisiana, Fourth Circuit · **Persuasive — state, illustrative** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 1767998 → opinion 1767998 (588 So. 2d 165, decided 1991-10-15); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Acting on a tip that a man known as "Les" was selling narcotics from apartment 9 at 1350 Bourbon Street, New Orleans detectives set up surveillance at roughly 2:40 a.m. To reach a vantage point, Detective Dabdoub pushed open a closed but unlocked solid black gate, entered the courtyard of the private apartment building, and concealed himself on a second-floor balcony. At about 3:15 a.m. he watched Leslie Karston step from apartment 9 to the gate and conduct what appeared to be a hand-to-hand drug sale. The detectives used that observation to obtain a search warrant for apartment 9, executed it at about 4:55 a.m., and seized marijuana, two handguns, and paraphernalia. Karston, charged with distribution of marijuana and possession of cocaine, moved to suppress; the trial court granted the motion, and the State sought review.

## Issue
Whether an officer who lacks probable cause or reasonable suspicion may open a closed (though unlocked) gate and enter the fenced courtyard of a private apartment complex to establish surveillance, or whether that entry invades a tenant's [[Reasonable Expectation of Privacy|reasonable expectation of privacy]].

## Rule
The court began from the settled premise that not every intrusion onto private property invades a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] — the question is whether the expectation is one "society at large is prepared to recognize as being reasonable." But this courtyard was enclosed by a brick wall and a solid black gate and was not open to the public, so a tenant retained a protected privacy interest in it: "Thus the defendant, a tenant in the apartment complex, had a reasonable expectation of privacy in the area outside his apartment. This legitimate privacy interest was violated when Officer Dabdoub, without probable cause, opened the gate and entered the courtyard." — 588 So. 2d at 167. ^pin-167

## Application
The detectives conceded they had neither probable cause nor reasonable suspicion when Dabdoub crossed the gate; the tip was uncorroborated and came from an untested informant. Because the enclosed courtyard was not a public vantage point but a private, fenced space shared by the building's tenants, entering it to watch the apartment was itself an unreasonable search. Everything the officer observed — and the warrant that observation produced — flowed from that unlawful entry, so the evidence was properly suppressed.

## Conclusion
Writ **denied**; the trial court's suppression order was affirmed. Becker, J., wrote for the panel (Byrnes, Armstrong, Becker, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Karston* illustrates that the [[Curtilage|curtilage]]-style protection recognized in *[[Florida v. Jardines|Jardines]]* reaches the enclosed common areas of a multi-unit dwelling: a fenced, gated apartment courtyard is not a public vantage point, and an officer may not cross a closed gate without justification to build a surveillance post against a resident.

## Appears on
- [[Curtilage]] — *Key*

## Sources
- [*State v. Karston*, 588 So. 2d 165 (La. Ct. App. 1991)](https://www.courtlistener.com/opinion/1767998/state-v-karston/) — pinpoint: 167 (reasonable-expectation-of-privacy holding; the CL opinion text star-paginates the So. 2d reporter). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9e450e093660a055", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "State v. Karston"}, "payload": {"all": [{"cite": "588 So. 2d 165", "page": "165", "reporter": "So. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 3, "volume": "588"}, {"cite": "1991 WL 205679", "page": "205679", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "1991"}], "display": "588 So. 2d 165", "official": {"cite": "588 So. 2d 165", "page": "165", "reporter": "So. 2d", "selected_official": true, "source": "cluster.citations[]", "type": 3, "volume": "588"}, "official_selection_present": true, "record_id": "State v. Karston"}}
{"assertion_id": "4dfeb7924dd4fdab", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "State v. Karston"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "State v. Karston", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — State v. Karston

```json
{
  "schema_version": "s2.v1",
  "record_id": "State v. Karston",
  "status": "under_review",
  "identity": {
    "case_name": "State v. Karston",
    "case_name_short": "Karston",
    "case_name_full": "",
    "input_case_name": "State v. Karston",
    "court": "La. Ct. App. 1991",
    "court_id": "lactapp",
    "court_level": "state",
    "circuit": null,
    "state": "la",
    "date_decided": "1991-10-15",
    "year": 1991,
    "docket": "91-K-1134",
    "cluster_id": 1767998,
    "lead_opinion_id": 1767998,
    "sibling_ids": [],
    "absolute_url": "/opinion/1767998/state-v-karston/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "588 So. 2d 165",
      "volume": "588",
      "reporter": "So. 2d",
      "page": "165",
      "type": 3,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1991 WL 205679",
        "volume": "1991",
        "reporter": "WL",
        "page": "205679",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "588 So. 2d 165",
        "volume": "588",
        "reporter": "So. 2d",
        "page": "165",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 WL 205679",
        "volume": "1991",
        "reporter": "WL",
        "page": "205679",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "588 So. 2d 165",
    "official_selection": {
      "court_class": "state",
      "selected": "588 So. 2d 165",
      "reason": "selected_rank_2"
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
    "date_created": "2026-07-06T05:48:30Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:48:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:48:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:48:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:48:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "state-v-karston--1767998",
      "to_record_id": "State v. Karston",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — State v. Karston

```
<div>
<center><b><span class="citation no-link">588 So.2d 165</span> (1991)</b></center>
<center><h1>STATE of Louisiana<br>
v.<br>
Leslie KARSTON.</h1></center>
<center>No. 91-K-1134.</center>
<center><p><b>Court of Appeal of Louisiana, Fourth Circuit.</b></p></center>
<center>October 15, 1991.</center>
<p><span class="star-pagination">*166</span> Harry F. Connick, Dist. Atty., Ralph Brandt, Asst. Dist. Atty., New Orleans, for relator.</p>
<p>W. Kenneth Klein, Slidell, for respondent.</p>
<p>Before BYRNES, ARMSTRONG and BECKER, JJ.</p>
<p>BECKER, Judge.</p>
<p>On February 26, 1990, the defendant, Leslie Karston, was charged by two separate bills of information with distribution of marijuana, a violation of R.S. 40:966, and possession of cocaine, a violation of R.S. 40:967. The defendant filed a motion to suppress evidence on April 11, 1990. A hearing on this motion was held in both cases, after which the trial court granted the defendant's motion to suppress the evidence. It is from this ruling that the State now complains.</p>
<p>On January 15, 1990, Detectives Lewis Dabdoub and Lawrence Delsa spoke to a "concerned individual" who had not given information in the past, but "has proven himself to be truthful." This individual told the detectives that within the past three days he was inside 1350 Bourbon Street, apartment 9 and had observed narcotics being sold. The individual said that the occupant of the apartment, known to him as "Les", was selling marijuana and cocaine to customers and that he had purchased narcotics from Les within the past 72 hours.</p>
<p>Detective Delsa then attempted to corroborate this individual's information. He contacted a confidential informant who stated that he knew that Les sold narcotics but "has not dealt with him recently."</p>
<p>Shortly after learning of this information, at approximately 2:40 a.m., the detectives established surveillance at this location. The search warrant states "Detective Dabdoub affixed himself in a location where he would be able to [observe] any activity at the apartment or within the courtyard. Detective Delsa affixed himself where he would be able to watch any activity outside of the courtyard." Detective Dabdoub testified at the motion to suppress hearing that he pushed open a solid black gate which was unlocked in order to secure entry into the courtyard and in turn enter into this private apartment building. After entering, he went to the second floor of the apartment building and concealed himself on the floor of the second floor balcony to watch the activity below.</p>
<p>At approximately 3:15 a.m. a subject approached the gate to the courtyard and "stood in front of it as if he were waiting for someone or something." About five minutes later, a man, later identified as the defendant, exited apartment 9 and walked to the gate. The search warrant application then states "when he got to the gate, he opened it and allowed the white male that was waiting outside in. They held a brief conversation, and the subject that exited the apartment reached into his robe <span class="star-pagination">*167</span> pocket and handed the other subject a plastic bag containing a dark material. In return the other subject went into his pocket and in return gave him what appeared to be U.S. currency." The Detectives, believing that they had witnessed a narcotic transaction, obtained a search warrant for 1350 Bourbon Street, apartment number 9. The search warrant was executed at approximately at 4:55 a.m. and a large amount of marijuana was seized from the bedroom closet and the kitchen. Also found were two handguns and "numerous pieces of paraphanalia." The defendant, the occupant of this apartment, was then arrested.</p>
<p>The issue presented in the present writ application is whether Detective Dabdoub could enter a closed but unlocked gate to a private apartment complex courtyard to establish a surveillance during which Officer Dabdoub witnessed the defendant engage in a drug transaction without violating the defendant's reasonable expectation of privacy.</p>
<p>There is no question that Detective Dabdoub did not possess probable cause or even reasonable suspicion when he entered the apartment courtyard. The Detective received an anonymous tip, which was not corroborated with independent police surveillance. The informant was untested (i.e. his reliability was not established). Without more information the Detective could not constitutionally infringe on the defendant's Fourth Amendment right to be free from unreasonable searches and seizures.</p>
<p>However, not all intrusions onto private property infringe on a person's reasonable expectation of privacy. In <i>State v. Ragsdale,</i> <span class="citation" data-id="1928519"><a href="/opinion/1928519/state-v-ragsdale/#497" aria-description="Citation for case: State v. Ragsdale">381 So.2d 492, 497</a></span> (La.1980), the Louisiana Supreme Court noted "the test for determining whether one has a reasonable expectation of privacy is not only whether the person has a reasonable or subjective expectation of privacy, but also whether that expectation is of a type which society at large is prepared to recognize as being reasonable."<sup>[1]</sup></p>
<p>However, in the present case, the area from which Detective Dabdoub observed the alleged drug transaction was not open to the public but rather was a courtyard to a private apartment complex which was fenced off to the general public by a brick wall and a solid black gate. Thus the defendant, a tenant in the apartment complex, had a reasonable expectation of privacy in the area outside his apartment. This legitimate privacy interest was violated when Officer Dabdoub, without probable cause, opened the gate and entered the courtyard. Accordingly, the trial court was not in error in granting the defendant's motion to suppress the evidence.</p>
<p>WRIT DENIED.</p>
<h2>NOTES</h2>
<p>[1]  For cases in which the courts have found the defendant did not have reasonable expedition of privacy see <i>State v. Brown,</i> <span class="citation" data-id="1720614"><a href="/opinion/1720614/state-v-brown/" aria-description="Citation for case: State v. Brown">395 So.2d 1301</a></span> (La. 1981), unfenced driveway; <i>State v. Dupuis,</i> <span class="citation" data-id="1947785"><a href="/opinion/1947785/state-v-dupuis/" aria-description="Citation for case: State v. Dupuis">378 So.2d 934</a></span> (La. 1979) unfenced field; <i>State v. Hines,</i> <span class="citation" data-id="1669913"><a href="/opinion/1669913/state-v-hines/" aria-description="Citation for case: State v. Hines">323 So.2d 449</a></span> (La.1975) unfenced common yard of apartment complex.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/State v. Larson.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: State v. Larson
type: case
citation: "159 Or. App. 34 (1999)"
parallel_cite: "977 P.2d 1175; 1999 Ore. App. LEXIS 384"
neutral_cite: ""
court: Or. Ct. App.
court_level: state
circuit: ""
year: 1999
date_decided: 1999-03-17
docket: 9601-30752
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
  opinion_url: "https://www.courtlistener.com/opinion/1187724/state-v-larson/"
  cluster_id: 1187724
  opinion_id: null
  identity_checked: true
lake:
  record_id: State v. Larson
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Curtilage]]"
    role: Key
related:
  - "[[Curtilage]]"
  - "[[Oliver v. United States]]"
tags:
  - case
  - fourth-amendment
  - curtilage
  - apartment
  - common-area
  - reasonable-expectation-of-privacy
  - oregon-court-of-appeals
holding: "An apartment dweller can hold a protected privacy interest in a shared common area outside the unit; rather than mechanically applying single-family curtilage factors, a court evaluates the physical layout and the residents' use of the area — and because officers entered a partially enclosed strip behind the building to smell marijuana from the defendant's window, they invaded his protected privacy interest, so the resulting warrant evidence was suppressed."
aliases:
  - State v. Larson
  - "State v. Larson (Or. Ct. App. 1999)"
---

# State v. Larson

*159 Or. App. 34 (1999)* (No. CA A96052) · Oregon Court of Appeals · **Persuasive — state, illustrative** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 1187724 → majority opinion 1187724 (Deits, C.J.; 159 Or. App. 34, decided Mar. 17, 1999). Decided under Article I, section 9, of the Oregon Constitution. Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*40`); pin to 159 Or. App. at 40. S9 promotes. -->

## Background
Acting on a tip that marijuana was being grown at the defendant's address, Portland officers knocked at his upstairs apartment; a visitor let them in briefly, but the defendant, reached by phone, refused consent and told them to leave. The officers then walked to a narrow, partially fenced strip of land behind the apartment building — a "common area" — and, standing below the defendant's second-story window, smelled marijuana coming from a ventilation tube. That observation supported a warrant, and a grow operation was found. The trial court suppressed the evidence, holding the back area was within the [[Curtilage|curtilage]] and that the defendant, as a cotenant, had a privacy interest in it.

## Issue
Whether an apartment dweller has a protected privacy interest in a partially enclosed common area behind the building, such that the officers' warrantless entry to gather evidence was unlawful.

## Rule
Because multi-family dwellings differ from single-family homes, traditional [[Curtilage|curtilage]] factors are relevant but not determinative of privacy in an apartment's surrounding areas. The court held: "because of the differences between a typical single-family dwelling and multiple-family dwellings, a strict application of the traditional curtilage doctrine to apartment dwellings should not be determinative of whether privacy rights exist. We believe that the better approach is to evaluate whether a privacy right exists based on the application of general legal principles relating to privacy interests to the circumstances of each case. Of particular significance is the physical layout of the living units and the residents' use of the area in question." — 159 Or. App. at 40. ^pin-40

## Application
The strip behind the building was adjacent to the residence and partly enclosed by a fence, functioned as a common backyard used by the tenants for maintenance access and occasional recreation, and was not open to the general public in a way that would defeat the residents' privacy. Evaluating the layout and the residents' actual use, the court concluded the defendant retained a privacy interest there; the officers invaded it when they entered to smell marijuana at his window, so that information had to be excised from the warrant affidavit.

## Conclusion
**Affirmed.** The Court of Appeals upheld the suppression order. Chief Judge Deits wrote for the court. (Decided under Article I, section 9, of the Oregon Constitution.)

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Larson* is a useful, illustrative state-court treatment of [[Curtilage|curtilage]] in the multi-family context: it rejects a mechanical single-home [[Curtilage|curtilage]] test for apartments and asks instead about physical layout and resident use. It is persuasive authority decided under the Oregon Constitution, illustrative for the federal *[[Curtilage]]* analysis rather than binding on it.

## Appears on
- [[Curtilage]] — *Key*

## Sources
- [*State v. Larson*, 159 Or. App. 34 (1999)](https://www.courtlistener.com/opinion/1187724/state-v-larson/) — pinpoint: 159 Or. App. at 40 (privacy in an apartment common area turns on layout and resident use, not mechanical curtilage factors). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*40`); parallel 977 P.2d 1175.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ccb8904a7d716dd1", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "State v. Larson"}, "payload": {"all": [{"cite": "977 P.2d 1175", "page": "1175", "reporter": "P.2d", "selected_official": false, "source": "cluster.citations[]", "type": 3, "volume": "977"}, {"cite": "159 Or. App. 34", "page": "34", "reporter": "Or. App.", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "159"}, {"cite": "1999 Ore. App. LEXIS 384", "page": "384", "reporter": "Ore. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "1999"}], "display": "159 Or. App. 34", "official": {"cite": "159 Or. App. 34", "page": "34", "reporter": "Or. App.", "selected_official": true, "source": "cluster.citations[]", "type": 2, "volume": "159"}, "official_selection_present": true, "record_id": "State v. Larson"}}
{"assertion_id": "9b734d8cc040eafa", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "State v. Larson"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "State v. Larson", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — State v. Larson

```json
{
  "schema_version": "s2.v1",
  "record_id": "State v. Larson",
  "status": "under_review",
  "identity": {
    "case_name": "State v. Larson",
    "case_name_short": "Larson",
    "case_name_full": "STATE OF OREGON, Appellant, v. JUDAH S. LARSON, Respondent",
    "input_case_name": "State v. Larson",
    "court": "Or. Ct. App.",
    "court_id": null,
    "court_level": "state",
    "circuit": null,
    "state": null,
    "date_decided": "1999-03-17",
    "year": 1999,
    "docket": "9601-30752",
    "cluster_id": 1187724,
    "lead_opinion_id": 1187724,
    "sibling_ids": [],
    "absolute_url": "/opinion/1187724/state-v-larson/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "159 Or. App. 34",
      "volume": "159",
      "reporter": "Or. App.",
      "page": "34",
      "type": 2,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "977 P.2d 1175",
        "volume": "977",
        "reporter": "P.2d",
        "page": "1175",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1999 Ore. App. LEXIS 384",
        "volume": "1999",
        "reporter": "Ore. App. LEXIS",
        "page": "384",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "977 P.2d 1175",
        "volume": "977",
        "reporter": "P.2d",
        "page": "1175",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "159 Or. App. 34",
        "volume": "159",
        "reporter": "Or. App.",
        "page": "34",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1999 Ore. App. LEXIS 384",
        "volume": "1999",
        "reporter": "Ore. App. LEXIS",
        "page": "384",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "159 Or. App. 34",
    "official_selection": {
      "court_class": "state",
      "selected": "159 Or. App. 34",
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
    "date_created": "2026-07-07T18:20:18Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:20:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:20:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:20:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:20:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "state-v-larson--1187724",
      "to_record_id": "State v. Larson",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — State v. Larson

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b58-3">
<span citation-index="1" class="star-pagination" label="36"> 
   *36
   </span>
  DEITS, C. J.
 </author>
<p id="b58-4">
  The state seeks reversal of the trial court’s pretrial order, ORS 138.060(3), suppressing evidence seized pursuant to a search warrant that was based, in part, on information obtained when officers went into an area behind defendant’s apartment and smelled the odor of marijuana emanating from a ventilation tube protruding from a window in defendant’s upstairs apartment. We affirm.
 </p>
<p id="b58-5">
  In April 1996, the Portland Police Bureau received information that the occupants at 1340 S.E. Tacoma were growing marijuana. Defendant lived at that address. In July, Officers Keist and Riley went to defendant’s apartment and knocked on the door. Nicole Gagnier, sister of defendant’s girlfriend, answered the door and allowed the officers into the apartment. Nicole told the officers that she was visiting her sister, Karen Gagnier, who lived in the apartment with defendant. Neither defendant nor Karen was home. Inside the apartment, the officers saw a towel pushed against the bottom of a closed door and a small picture of a marijuana plant sitting on a table in the living room. The officers asked Nicole to contact defendant or Karen. Nicole called her sister, Karen, at work. Officer Keist asked Karen if there was marijuana growing inside the apartment. She said that she didn’t know, that the officers should talk to defendant. The officers then paged defendant who returned the page by calling the apartment. Defendant refused the officers’ request for consent to search his apartment and told them to leave, which they did.
 </p>
<p id="b58-6">
  The officers waited outside the apartment for defendant to return. While they were waiting, they walked to what they described as a “common area” at the rear of the apartment building and stood below a second-story window of defendant’s apartment. From this vantage point they saw a ventilation system using a dryer hose, in the screen of the window of defendant’s apartment. Both officers reported that they could smell a definite marijuana odor coming from the ventilation system. Defendant arrived at the apartment a short time later. He again refused to consent to a search of his apartment. He was arrested and, based, in part, on the information obtained by the officers while they were in the back
  <span citation-index="1" class="star-pagination" label="37"> 
   *37
   </span>
  area, a warrant was obtained to search defendant’s apartment. During the search, the officers found a marijuana-growing operation of 14 plants in a bedroom.
 </p>
<p id="b59-7">
  There are two floors in defendant’s building. The area behind defendant’s building, where the officers stood to see the ventilation system and smell the marijuana, is a small strip of land about 10-feet wide. It is bounded on the west by the back of the apartment building and on the east and south by a poorly maintained wooden slat fence. Access to the strip of land behind the building can be gained by going around the north side of the building or by passing through a gate at the southwest corner of the building.
 </p>
<p id="b59-3">
  [[Image here]]
 </p>
<p id="b59-5">
  The apartment on the first floor, directly under defendant’s apartment, has a sliding glass door that opens to a small concrete slab surrounded by barkdust. The downstairs resident, Marilyn Lipko, refers to this area as her
  <span citation-index="1" class="star-pagination" label="38"> 
   *38
   </span>
  patio. Access to Lipko’s patio can be gained by going through' the gate at the southwest corner of the building or by going along the strip behind the building. The tenants of the second-story apartments have no direct access from their apartments to the Lipko patio area or to the strip behind the building. Lipko had posted a sign on the gate at the southeast corner of the back area, facing north, that read “We like you but
  <em>
   not
  </em>
  in our backyard.
  <em>
   Please
  </em>
  KEEP OUT!” Defendant testified that he did nothing on his own to exclude people but that he depended on Lipko’s sign. A friend of defendant testified that she generally did not see people in the yard area behind defendant’s apartment but that she “might see kids occasionally^]”
 </p>
<p id="b60-4">
  At the hearing on the motion to suppress, the state sought to introduce a note signed by another tenant of the building, Bashaw, in which she stated that she gave retroactive consent to the police to search the area behind her apartment. The address of Bashaw’s apartment was 1334 S.E. Tacoma, but the exact location of her apartment was not identified at the suppression hearing. The trial court refused to admit the note, concluding that, although Bashaw may have had equal access to the back area, retroactive consent is legally invalid, and that, therefore, such evidence would be irrelevant.
 </p>
<p id="b60-5">
  The trial court concluded that the area behind defendant’s apartment was part of the common area of defendant’s apartment building and that defendant, as a cotenant, had a privacy interest in it. The court also held that the officers violated defendant’s privacy interest when they entered that area. Consequently, the court struck the portion of Officer Keist’s affidavit in support of the search warrant, in which she stated that she had smelled marijuana coming from the vent in defendant’s apartment window. The court then concluded that, without the evidence discovered during the search in the back area, the affidavit failed to establish probable cause to support the warrant. Accordingly, the court granted defendant’s motion to suppress the evidence found during the search of defendant’s apartment pursuant to the warrant.
 </p>
<p id="b61-3">
<span citation-index="1" class="star-pagination" label="39"> 
   *39
   </span>
  On appeal, the state assigns error to the trial court’s suppression order. It argues that the officers did not violate defendant’s privacy interests when they entered the area behind the building because the area was not sufficiently private, as to defendant, to violate such interests. The state argues alternatively that the evidence of retroactive consent from Bashaw should have been admitted and that that consent authorized the search.
 </p>
<p id="b61-4">
  The state’s first argument turns on whether the officers invaded a privacy interest protected by Article I, section 9, of the Oregon Constitution,
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  when they entered the narrow strip of land running behind defendant’s apartment building and made their observations. The privacy rights granted by the Oregon Constitution are not defined by a reasonable expectation of privacy, but in terms of “the privacy to which one has a
  <em>
   right” State v. Campbell,
  </em>
  <span class="citation" data-id="1215380"><a href="/opinion/1215380/state-v-campbell/#164" aria-description="Citation for case: State v. Campbell">306 Or 157, 164</a></span>, <span class="citation" data-id="1215380"><a href="/opinion/1215380/state-v-campbell/" aria-description="Citation for case: State v. Campbell">759 P2d 1040</a></span> (1988) (emphasis in original). The privacy rights protected by Article I, section 9, are defined by an objective test of whether the government’s conduct “would significantly impair an individual’s interest in freedom from scrutiny,
  <em>
   i.e.,
  </em>
  his privacy.”
  <em>
   State v. Dixson/Digby,
  </em>
  <span class="citation" data-id="1349523"><a href="/opinion/1349523/state-v-dixson/#211" aria-description="Citation for case: State v. Dixson">307 Or 195, 211</a></span>, <span class="citation" data-id="1349523"><a href="/opinion/1349523/state-v-dixson/" aria-description="Citation for case: State v. Dixson">766 P2d 1015</a></span> (1988). “One indication of whether a government action intrudes on a person’s privacy right is whether a private individual would offend social and legal norms of behavior by engaging in the same kind of intrusion.”
  <em>
   State v. Portrey,
  </em>
  <span class="citation" data-id="1288359"><a href="/opinion/1288359/state-v-portrey/#464" aria-description="Citation for case: State v. Portrey">134 Or App 460, 464</a></span>, <span class="citation" data-id="1288359"><a href="/opinion/1288359/state-v-portrey/" aria-description="Citation for case: State v. Portrey">896 P2d 7</a></span> (1995).
 </p>
<p id="b61-5">
  The trial court began its analysis of the issues presented by the motion to suppress by considering whether the area in question was within the curtilage of defendant’s residence. The court concluded that the area was within the curtilage and went on to explain that even though this was a common area for the tenants of the apartments, that fact did not defeat the apartment dwellers’ right to privacy in the area. Based on these findings, the trial court concluded that defendant’s privacy interests had been violated.
 </p>
<p id="b62-3">
<span citation-index="1" class="star-pagination" label="40"> 
   *40
   </span>
  The factors used to determine whether an area is within the curtilage of a private dwelling are often relevant in assessing whether a particular area of an apartment complex is one in which an individual has privacy rights for purposes of Article I, section
  <em>
   9.
  </em>
<a class="footnote" href="#fn2" id="fn2_ref">
<em>
    2
   </em>
</a>
<em>
</em>
  Nonetheless, because of the differences between a typical single-family dwelling and multiple-family dwellings, a strict application of the traditional curtilage doctrine to apartment dwellings should not be determinative of whether privacy rights exist. We believe that the better approach is to evaluate whether a privacy right exists based on the application of general legal principles relating to privacy interests to the circumstances of each case. Of particular significance is the physical layout of the living units and the residents’ use of the area in question.
 </p>
<p id="b62-4">
  That is essentially what we have done in the cases in which we have decided whether a privacy right under Article I, section 9, has been violated by a police officer’s entry into an area surrounding an apartment dwelling.
  <em>
   See State v. Erb,
  </em>
  <span class="citation" data-id="6942056"><a href="/opinion/7039177/state-v-erb/" aria-description="Citation for case: State v. Erb">135 Or App 421</a></span>, <span class="citation" data-id="6942056"><a href="/opinion/7039177/state-v-erb/" aria-description="Citation for case: State v. Erb">899 P2d 716</a></span>,
  <em>
   rev den
  </em>
  <span class="citation no-link">322 Or 421</span> (1995) (under particular circumstances, officer’s entry into apartment complex parking lot did not impair defendant’s freedom from scrutiny);
  <em>
   Portrey,
  </em>
  <span class="citation" data-id="1288359"><a href="/opinion/1288359/state-v-portrey/" aria-description="Citation for case: State v. Portrey">134 Or App 460</a></span> (although defendant had impliedly consented to visitors coming to his apartment door, he retained a privacy interest in articles not entirely visible to someone standing on his doorstep);
  <em>
   State v. Breshears / Oliver,
  </em>
  <span class="citation" data-id="9545641"><a href="/opinion/1167699/state-v-breshears/" aria-description="Citation for case: State v. Breshears">98 Or App 105</a></span>, <span class="citation" data-id="9545641"><a href="/opinion/1167699/state-v-breshears/" aria-description="Citation for case: State v. Breshears">779 P2d 158</a></span> (1989) (defendants had a privacy interest in side yard of their apartment which was surrounded by a fence, apartment buildings and brush and reached by walking across a grassy area off the walkway);
  <em>
   State v. Roles,
  </em>
  <span class="citation" data-id="1116054"><a href="/opinion/1116054/state-v-roles/" aria-description="Citation for case: State v. Roles">75 Or App 63</a></span>, <span class="citation" data-id="1116054"><a href="/opinion/1116054/state-v-roles/" aria-description="Citation for case: State v. Roles">705 P2d 227</a></span> (1985) (because roof area was accessible only from defendant’s second-floor apartment, it was a protected area).
 </p>
<p id="b63-3">
<span citation-index="1" class="star-pagination" label="41"> 
   *41
   </span>
  Here, the area in question was adjacent to the apartment building and was partially enclosed by a fence. However, there was open access to the area through a walkway in the center of the building. The area appeared to function somewhat as a common backyard for the apartment’s residents. Children occasionally played there, one resident had a cement patio area there and the area provided access for all of the residents of the building to the back of their units to do maintenance work such as washing windows or adjusting window screens. As we have recognized before, in determining whether police entries into backyards of private dwellings violate privacy interests, backyards are generally, by nature, more private than areas in the front of a house. We stated in
  <em>
   State v. Ohling,
  </em>
  <span class="citation" data-id="9535056"><a href="/opinion/1132320/state-v-ohling/#253" aria-description="Citation for case: State v. Ohling">70 Or App 249, 253</a></span>, <span class="citation" data-id="9535056"><a href="/opinion/1132320/state-v-ohling/" aria-description="Citation for case: State v. Ohling">688 P2d 1384</a></span>,
  <em>
   rev den
  </em>
  <span class="citation no-link">298 Or 334</span> (1984):
 </p>
<blockquote id="b63-5">
  “Going to the back of the house is a different matter. Such an action is both less common and less acceptable in our society. There is no implied consent for a stranger to do so. ‘[W]e do not place things of a private nature on our front porches that we may very well entrust to the seclusion of a backyard, patio or deck.’
  <em>
   State v. Corbett,
  </em>
  <span class="citation" data-id="1272735"><a href="/opinion/1272735/state-v-corbett/#475" aria-description="Citation for case: State v. Corbett">15 Or App 470, 475</a></span>, <span class="citation" data-id="1272735"><a href="/opinion/1272735/state-v-corbett/" aria-description="Citation for case: State v. Corbett">516 P2d 487</a></span> (1973),
  <em>
   rev den
  </em>
  (1974).”
 </blockquote>
<p id="b63-6">
  The backyard of an apartment dwelling, of course, offers less privacy to the tenants. That is particularly true of an area such as this that functions as “a common” backyard of the tenants. However, the fact that a common area of an apartment building is involved is not, in itself, determinative of whether a privacy interest exists. Although the area was available for use by all of the tenants, and perhaps their guests, it was not available for use by other members of the public. The presence of an individual, other than a resident or guest, in the back area peering up at the second-floor windows would offend social and legal norms of behavior.
 </p>
<p id="b63-7">
  In addition, the sign posted by apartment resident, Lipko, on the fence at the southeast comer of the back area that read ‘We like you but
  <em>
   not
  </em>
  in our backyard.
  <em>
   Please
  </em>
  KEEP OUT!” supports the conclusion that defendant had privacy interests in that area. The state points to Lipko’s testimony, that she did not intend the sign to exclude the police, to argue that the sign is not evidence of an intent to exclude the public from the area. However, the test is an objective one and,
  <span citation-index="1" class="star-pagination" label="42"> 
   *42
   </span>
  viewed objectively, the words of the sign did not limit who it was intended to exclude. Rather, the words manifest an intent to exclude the public.
  <em>
   See State v. Glines,
  </em>
  <span class="citation" data-id="1123582"><a href="/opinion/1123582/state-v-glines/#24" aria-description="Citation for case: State v. Glines">134 Or App 21, 24</a></span>, <span class="citation" data-id="1123582"><a href="/opinion/1123582/state-v-glines/" aria-description="Citation for case: State v. Glines">894 P2d 516</a></span>,
  <em>
   rev den
  </em>
  <span class="citation no-link">321 Or 512</span> (1995) (citing
  <em>
   State v. Wacker,
  </em>
  <span class="citation" data-id="9602574"><a href="/opinion/1364515/state-v-wacker/#425" aria-description="Citation for case: State v. Wacker">317 Or 419, 425</a></span>, <span class="citation" data-id="9602574"><a href="/opinion/1364515/state-v-wacker/" aria-description="Citation for case: State v. Wacker">856 P2d 1029</a></span> (1993), and
  <em>
   Dixson / Digby,
  </em>
  <span class="citation" data-id="1349523"><a href="/opinion/1349523/state-v-dixson/#211" aria-description="Citation for case: State v. Dixson">307 Or at 211</a></span>). Accordingly, the sign is a further indication that the apartment residents did have privacy interests in the area. We conclude that the officers’ entry into the back area violated privacy interests protected by .Article I, section 9.
 </p>
<p id="b64-4">
  The state next argues that, even if the officers violated defendant’s privacy when , they walked behind his apartment, their actions were justified by the consent that they subsequently obtained from one of defendant’s neighbors. On November 20,1996, the day before the suppression hearing, Officer Keist returned to defendant’s apartment building and obtained a handwritten document from Bashaw, a tenant in another apartment. The document purported to give Bashaw’s consent for police officers to “go on the east side, back of [her] apartment.” The document further said “I also now give my permission for officers to have been on the east side, back area of my apartment when the officers were here investigating a marijuana grow earlier this year.”
 </p>
<p id="b64-5">
  The state argues that under
  <em>
   State v. Weaver,
  </em>
  <span class="citation" data-id="9566079"><a href="/opinion/1219169/state-v-weaver/" aria-description="Citation for case: State v. Weaver">319 Or 212</a></span>, <span class="citation" data-id="9566079"><a href="/opinion/1219169/state-v-weaver/" aria-description="Citation for case: State v. Weaver">874 P2d 1322</a></span> (1994), consent may “relate back” and validate a prior search as long as there is evidence that the person giving consent has actual authority to give it and intends for the consent to relate back to the prior search. The state is correct that, in
  <em>
   <span class="citation" data-id="9566079"><a href="/opinion/1219169/state-v-weaver/" aria-description="Citation for case: State v. Weaver">Weaver</a></span>,
  </em>
  under some circumstances, a defendant’s consent may “relate back” to the beginning of a search if there is evidence in the record that the defendant intended the consent to be retroactive. By consenting to the search after the fact, the defendant is essentially waiving any objection to the unlawfulness of the earlier police conduct. This case, however, presents a different question from
  <em>
   <span class="citation" data-id="9566079"><a href="/opinion/1219169/state-v-weaver/" aria-description="Citation for case: State v. Weaver">Weaver</a></span>
  </em>
  because the consent here was not obtained from the defendant but, rather, from a third party. We decline to hold that, under the circumstances here, a third party may waive the
  <span citation-index="1" class="star-pagination" label="43"> 
   *43
   </span>
  unlawfulness of police conduct with respect to the defendant.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  The trial court did not err in concluding that Bashaw’s retroactive consent did not provide authority for the officers’ entry into the area behind defendant’s apartment.
 </p>
<p id="b65-4">
  We conclude that the trial court was correct in excising the portion of the affidavit in support of the search warrant that was a result of the officers’ entry into the area behind defendant’s apartment. The state has not argued that probable cause exists without the excised portion of the affidavit and, therefore, we affirm the court’s suppression of the evidence seized under the warrant.
 </p>
<p id="b65-5">
  Affirmed.
 </p>



<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b61-6">
   Article I, section 9, of the Oregon Constitution, provides:
  </p>
<blockquote id="b61-7">
   “No law shall violate the right of the people to be secure in their persons, houses, papers, and effects, against unreasonable search, or seizure * *
  </blockquote>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b62-5">
   The pertinent factors in determining whether an area is within the curtilage of a private dwelling are
  </p>
<blockquote id="b62-6">
   “its proximity or annexation to the dwelling, its inclusion within the general enclosure surrounding the dwelling and its use and enjoyment as an adjunct to the domestic economy of the family.”
   <em>
    State v. Russo,
   </em>
   <span class="citation" data-id="1159722"><a href="/opinion/1159722/state-v-russo/#763" aria-description="Citation for case: State v. Russo">68 Or App 760, 763</a></span>, <span class="citation" data-id="1159722"><a href="/opinion/1159722/state-v-russo/" aria-description="Citation for case: State v. Russo">683 P2d 163</a></span> (1984) (citing
   <em>
    Care v. United States,
   </em>
   231 F2d 22, 25 (10th Cir 1956),
   <em>
    cert den
   </em>
   <span class="citation" data-id="8929450"><a href="/opinion/8939050/care-v-united-states/" aria-description="Citation for case: Care v. United States">351 US 932</a></span> (1956)).
  </blockquote>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b65-6">
   Defendant also argues that the introduction of the retroactive consent would be improper because, in effect, it adds additional facts to the affidavit supporting the search warrant. Because of our disposition, we need not reach that issue.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/State v. Mansor.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "State v. Mansor"
type: case
citation: "363 Or. 185 (2018)"
parallel_cite: 421 P.3d 323
neutral_cite: ""
court: Oregon Supreme Court
court_level: state
circuit: ""
year: 2018
date_decided: 2018-06-28
docket: ""
authority_weight: "Persuasive — state, illustrative"
treatment:
  field_i_validity: good_law
  as_of_content: 2018-06-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: State v. Mansor
  varies_by_point: false
  scope_note: "Decided under Article I, section 9 of the Oregon Constitution, not the Fourth Amendment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/6656738/state-v-mansor/"
  cluster_id: 6656738
  opinion_id: 6534035
  identity_checked: true
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Recent development (role-based)"
related: ["[[Riley v. California]]", "[[Carpenter v. United States]]", "[[State v. Volle]]"]
aliases: []
tags: ["case", "state-constitution", "digital-search", "computer-warrant", "particularity", "oregon"]
holding: "Decided under Article I, section 9 of the OREGON Constitution: the State may not USE information found in a computer search that the…"
lake:
  record_id: State v. Mansor
  status: verified
  projected_at: 2026-07-09
---

# State v. Mansor

*363 Or. 185, 421 P.3d 323 (2018)* · Oregon Supreme Court · **Persuasive — state, illustrative** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating the death of Kaliq Mansor's infant son, police obtained a warrant—limited by its supporting affidavit to specified search terms—to search his home computers. The forensic examination produced voluminous additional data (browsing history and other files) beyond those terms, which the State sought to use at trial. Mansor moved to suppress.

## Issue
Under Article I, section 9 of the Oregon Constitution, what [[Particularity|particularity]] a computer-search warrant must satisfy, and whether the State may use data found on the computer that the warrant did not authorize the police to search for.

## Rule
The Oregon Supreme Court set a [[Particularity|particularity]] rule for computer warrants and limited the use of unauthorized data. "[T]o meet the particularity requirement of Article I, section 9, a warrant to search for and seize a computer—and to search the computer itself for information related to a crime—must be based on probable cause to believe that such evidence will be found on the computer and must describe the information the state seeks (the 'what') with as much specificity as reasonably possible under the circumstances ...." — 363 Or. 185 (2018). ^pin-185

"We also hold that, because of the possibility that a computer search will uncover information that is not authorized by the warrant, a defendant's Article I, section 9, privacy rights prevent the state from using such information unless it comes within an exception to the warrant requirement." — [*Id.*](https://www.courtlistener.com/opinion/6656738/state-v-mansor/#:~:text=We%20also%20hold%20that%2C%20because) ^pin-185a

## Application
The warrant here, as limited by its affidavit, was valid because the affidavit established probable cause to search the computers and identified the information to be sought. But it did not authorize the police to search for and recover much of the other voluminous material on Mansor's computers, so the trial court erred in admitting that unauthorized material, and the error was not harmless.

## Conclusion
The warrant was valid, but the State could not use data outside its authorization; the trial court's decision was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Persuasive — state, illustrative** (decided on independent state-constitutional grounds).
- A state-constitutional development on digital-search scope, informed by [[Riley v. California]] and paralleling the federal digital-data concerns of [[Carpenter v. United States]]; compare the digital-warrant [[Particularity|particularity]] analysis in [[State v. Volle]].

## Appears on
- [[Plain View Doctrine]] — *Recent development (role-based)*

## Sources
- *State v. Mansor*, 363 Or. 185, 421 P.3d 323 (2018) — https://www.courtlistener.com/opinion/6656738/state-v-mansor/ (lead opinion id 6534035). The CourtListener text carries no internal reporter pagination; quotations are cited to the case.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c8679d52bea391e1", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "State v. Mansor"}, "payload": {"all": [{"cite": "421 P.3d 323", "page": "323", "reporter": "P.3d", "selected_official": false, "source": "cluster.citations[]", "type": 3, "volume": "421"}, {"cite": "363 Or. 185", "page": "185", "reporter": "Or.", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "363"}], "display": "363 Or. 185", "official": {"cite": "363 Or. 185", "page": "185", "reporter": "Or.", "selected_official": true, "source": "cluster.citations[]", "type": 2, "volume": "363"}, "official_selection_present": true, "record_id": "State v. Mansor"}}
{"assertion_id": "0f4ebd70e64b4a4f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-185", "record_id": "State v. Mansor"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-185", "pinpoint_status": "slip-only", "quote": "--- # State v. Mansor *363 Or. 185, 421 P.3d 323 (2018)* · Oregon Supreme Court · **Persuasive — state, illustrative** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigating the death of Kaliq Mansor's infant son, police obtained a warrant—limited by its supporting affidavit to specified search terms—to search his home computers. The forensic examination produced voluminous additional data (browsing history and other files) beyond those terms, which the State sought to use at trial. Mansor moved to suppress. ## Issue Under Article I, section 9 of the Oregon Constitution, what particularity a computer-search warrant must satisfy, and whether the State may use data found on the computer that the warrant did not authorize the police to search for. ## Rule The Oregon Supreme Court set a particularity rule for computer warrants and limited the use of unauthorized data.", "quote_fidelity": "mismatch", "record_id": "State v. Mansor", "star_marker": null}}
{"assertion_id": "2f5c6e1c64b2d6a1", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-185a", "record_id": "State v. Mansor"}, "payload": {"fragment": "#:~:text=We%20also%20hold%20that%2C%20because", "page": null, "pin_id": "pin-185a", "pinpoint_status": "star-verified", "quote": "We also hold that, because of the possibility that a computer search will uncover information that is not authorized by the warrant, a defendant's Article I, section 9, privacy rights prevent the state from using such information unless it comes within an exception to the warrant requirement.", "quote_fidelity": "matched", "record_id": "State v. Mansor", "star_marker": "345"}}
{"assertion_id": "7e241603331e4176", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "State v. Mansor"}, "payload": {"as_of_content": "2018-06-28", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "State v. Mansor", "scope_note": "Decided under Article I, section 9 of the Oregon Constitution, not the Fourth Amendment.", "varies_by_point": false}}
```

### lake record — State v. Mansor

```json
{
  "schema_version": "s2.v1",
  "record_id": "State v. Mansor",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "State v. Mansor",
    "case_name_short": "Mansor",
    "case_name_full": "STATE of Oregon, on Review v. Kaliq Michael MANSOR, on Review.",
    "input_case_name": "State v. Mansor",
    "court": "Oregon Supreme Court",
    "court_id": "or",
    "court_level": "state",
    "circuit": null,
    "state": null,
    "date_decided": "2018-06-28",
    "year": 2018,
    "docket": null,
    "cluster_id": 6656738,
    "lead_opinion_id": 6534035,
    "sibling_ids": [
      6534035
    ],
    "absolute_url": "/opinion/6656738/state-v-mansor/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "363 Or. 185",
      "volume": "363",
      "reporter": "Or.",
      "page": "185",
      "type": 2,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "421 P.3d 323",
        "volume": "421",
        "reporter": "P.3d",
        "page": "323",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "421 P.3d 323",
        "volume": "421",
        "reporter": "P.3d",
        "page": "323",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "363 Or. 185",
        "volume": "363",
        "reporter": "Or.",
        "page": "185",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "363 Or. 185",
    "official_selection": {
      "court_class": "state",
      "selected": "363 Or. 185",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-185",
      "page": null,
      "quote": "--- # State v. Mansor *363 Or. 185, 421 P.3d 323 (2018)* \u00b7 Oregon Supreme Court \u00b7 **Persuasive \u2014 state, illustrative** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigating the death of Kaliq Mansor's infant son, police obtained a warrant\u2014limited by its supporting affidavit to specified search terms\u2014to search his home computers. The forensic examination produced voluminous additional data (browsing history and other files) beyond those terms, which the State sought to use at trial. Mansor moved to suppress. ## Issue Under Article I, section 9 of the Oregon Constitution, what particularity a computer-search warrant must satisfy, and whether the State may use data found on the computer that the warrant did not authorize the police to search for. ## Rule The Oregon Supreme Court set a particularity rule for computer warrants and limited the use of unauthorized data.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-185a",
      "page": null,
      "quote": "We also hold that, because of the possibility that a computer search will uncover information that is not authorized by the warrant, a defendant's Article I, section 9, privacy rights prevent the state from using such information unless it comes within an exception to the warrant requirement.",
      "star_marker": "345",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 122041,
      "fragment": "#:~:text=We%20also%20hold%20that%2C%20because",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2018-06-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "State v. Mansor",
    "varies_by_point": false,
    "scope_note": "Decided under Article I, section 9 of the Oregon Constitution, not the Fourth Amendment.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Hargrove",
          "cluster_id": 10143743,
          "cite": [
            "327 Or. App. 437",
            "536 P.3d 612"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Vesa",
          "cluster_id": 10135689,
          "cite": [
            "324 Or. App. 674",
            "527 P.3d 786"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Serrano (A173250)",
          "cluster_id": 10135658,
          "cite": [
            "324 Or. App. 453",
            "527 P.3d 54"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tardie",
          "cluster_id": 10135114,
          "cite": [
            "319 Or. App. 229",
            "509 P.3d 705"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Turay",
          "cluster_id": 10134420,
          "cite": [
            "313 Or. App. 45",
            "493 P.3d 1058"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Paye",
          "cluster_id": 10134177,
          "cite": [
            "310 Or. App. 408",
            "486 P.3d 808"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane1_negative"
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
        "journal_ref": "State v. Mansor:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Pittman",
          "cluster_id": 10160783,
          "cite": [
            "367 Or. 498",
            "479 P.3d 1028"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cazee",
          "cluster_id": 10133950,
          "cite": [
            "308 Or. App. 748",
            "482 P.3d 140"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Monger",
          "cluster_id": 10133634,
          "cite": [
            "306 Or. App. 50",
            "472 P.3d 270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. McNutt",
          "cluster_id": 10133380,
          "cite": [
            "303 Or. App. 142",
            "463 P.3d 563"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Turay",
          "cluster_id": 10160992,
          "cite": [
            "532 P.3d 57",
            "371 Or. 128"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Short",
          "cluster_id": 5305353,
          "cite": [
            "964 N.W.2d 272",
            "310 Neb. 81"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Sassarini",
          "cluster_id": 10133108,
          "cite": [
            "300 Or. App. 106",
            "452 P.3d 457"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cannon",
          "cluster_id": 10133093,
          "cite": [
            "299 Or. App. 616",
            "450 P.3d 567"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Monica v. Myers",
          "cluster_id": 10135107,
          "cite": [
            "319 Or. App. 376",
            "510 P.3d 238"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Curry",
          "cluster_id": 10265977,
          "cite": [
            "560 P.3d 694",
            "336 Or. App. 72"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. James",
          "cluster_id": 10265972,
          "cite": [
            "560 P.3d 747",
            "336 Or. App. 55"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Goode",
          "cluster_id": 10120747,
          "cite": [
            "557 P.3d 1132",
            "335 Or. App. 108"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. DiMolfetto",
          "cluster_id": 10648835,
          "cite": [
            "342 Or. App. 456"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Meyers",
          "cluster_id": 10336394,
          "cite": [
            "565 P.3d 463",
            "338 Or. App. 59"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 10143994,
          "cite": [
            "542 P.3d 467",
            "329 Or. App. 588"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lee",
          "cluster_id": 10135118,
          "cite": [
            "319 Or. App. 191",
            "509 P.3d 689"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gustafson",
          "cluster_id": 10133126,
          "cite": [
            "300 Or. App. 438",
            "452 P.3d 962"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Venable",
          "cluster_id": 10134750,
          "cite": [
            "316 Or. App. 235",
            "502 P.3d 250"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gaskill",
          "cluster_id": 10583993,
          "cite": [
            "340 Or. App. 459"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "State v. Mansor:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(6534035) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR or OR orctapp)",
        "reviewed": 44,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 11,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 44,
        "triage_read": 13,
        "triage_snippet_classified": 31
      },
      "lane2_top_cited": {
        "query": "cites:(6534035)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0wJnM9MTA1ODY3NDQmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%286534035%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(6534035)",
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
    "complete_query": "cites:(6534035)",
    "indexed_citing_opinions": 54,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 6534035,
        "count": 54,
        "count_source": "search"
      }
    ],
    "citation_count": 85,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/state-v-mansor.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5ODkyODImcz0xMDEyMDc0NyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%286534035%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T20:26:55Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:27:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:27:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:31:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:27:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — State v. Mansor (truncated)

```
<opinion type="majority">
<p id="p-14">Rookhuyzen prepared a seven-page affidavit in support of his warrant application. The Court of Appeals summarized the affidavit's contents, which recounted Rookhuyzen's interactions with defendant and observations of the home:</p>
<blockquote id="p-15">"At the beginning of the interview, Rookhuyzen noted that defendant was 'non-emotive'-which, in Rookhuyzen's training and experience, was 'highly unusual' in such circumstances because '[p]arents are usually crying, sobbing, and exhibiting signs of sadness or anxiety.' Defendant told Rookhuyzen that he had been home alone with B and his twin brother, while his wife was working. According to defendant, as he had been feeding B a mixture of formula and liquid vitamins, the mixture had started to come out of the baby's nose and the baby had started coughing, so defendant had turned him over, shaken him, and 'smacked' him on the back. The baby's eyes became 'fixed' and 'droopy,' and his breathing became 'very much labored.' Defendant told Rookhuyzen that he then shook B more, and the baby began going 'a minute or two between breaths.'</blockquote>
<blockquote id="p-16">"Defendant did not call 9-1-1 at that point. Instead, he told Rookhuyzen, he 'went online' on a computer in the baby's room to conduct research about what he should do. When, after 15 minutes, the baby's condition did not improve, defendant called 9-1-1.</blockquote>
<blockquote id="p-17">"Defendant did not call his wife during that period-and, indeed, had not attempted to contact her by the time Rookhuyzen began to interview him. In Rookhuyzen's experience, that was 'extremely unusual': '[W]ith these kind of incidents, spouses want to call each other instantly, even before speaking with law enforcement.'</blockquote>
<blockquote id="p-18">"Rookhuyzen's affidavit further recounted that, at the hospital, B was examined by a pediatrician, Dr. Lindsay, who determined that the baby had no brain activity and <a class="page-label" data-citation-index="2" data-label="190" href="#p190" id="p190">**190</a>would die soon. Lindsay further determined, <em>inter alia</em> , that the baby had experienced head trauma resulting in a skull fracture, bi-lateral retinal hemorrhages, and an 'old rib fracture.' In Lindsay's opinion, defendant's account was not consistent with the baby's condition, and he ultimately rendered a diagnosis of 'shaken baby syndrome ' as a result of intentionally inflicted abuse.</blockquote>
<blockquote id="p-19">"*** Further, as specifically pertinent to the lawfulness of the seizure and search of defendant's computers, the affidavit included the following averment:</blockquote>
<blockquote id="p-20">" 'I know based upon my training and experience that computers can be connected to the internet to find information using computer software that browse internet sites for information. Internet search engine sites such as Google and Yahoo! are often used to search the internet for information related to a user's requests. I know that the computer will retain a history of internet sites visited and the search terms used on the internet. I know that to retain the integrity of a computer's memory and how the system was used, the computer needs to be searched in a laboratory and carefully examined by a trained computer forensic examiner in order to ensure that the data is not corrupted, damaged, or otherwise changed from the time when the machine was seized. [Defendant] told me that he searched the internet between the time he noticed [B] was <a class="page-label" data-citation-index="1" data-label="328" href="#p328" id="p328">*328</a>having difficulty breathing and the time he called emergency dispatch. He told me that he was using a computer to search the internet for advice on what he should do. When I was in the residence, I saw two laptop computers and two desktop computers. [Defendant] did not specify which computer he was using just before he called 9-1-1.'</blockquote>
<blockquote id="p-21">"The affidavit also included a detailed description of defendant's residence. Finally, in a section titled 'Conclusion,' the affidavit stated Rookhuyzen's belief that there was probable cause to seize and search 11 types of evidence, including '[t]wo laptop computers in the residence' and '[t]wo desktop computer towers located in the office/baby room.' "</blockquote>
<p id="p-22"><em>Mansor</em> , <extracted-citation case-ids="12167760" index="2" url="https://cite.case.law/or-app/279/778/#p801">279 Or. App. at 780-81</extracted-citation>, <extracted-citation case-ids="12167760" index="3" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">381 P.3d 930</a></span></extracted-citation> (brackets in <em><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">Mansor</a></span></em> ; footnotes omitted).</p>
<p id="p-23">A circuit court judge signed the search warrant that evening. The search warrant instructed executing <a class="page-label" data-citation-index="2" data-label="191" href="#p191" id="p191">**191</a>officers to "seize and search and forensically examine the following objects: See attachment A." (Emphasis omitted.) Attachment A was captioned "items to be searched for, to be seized, and to be analyzed." It repeated verbatim the list of eleven items included in Rookhuyzen's affidavit, including "[t]wo laptop computers" and "[t]wo desktop computer towers." The warrant itself contained no instructions or limitations regarding how the computers were to be analyzed.</p>
<p id="p-24">The warrant was executed that night. Two laptop computers, two desktop computers, and other items from B's room were seized. The computers were taken to the Northwest Regional Computer Forensics Laboratory, operated by the FBI, which performed the forensic analysis. The lab's report summarized the request:</p>
<blockquote id="p-25">"[Rookhuyzen] requested that the [seized computer drives] be examined for internet history and internet search terms input by the user on [June 12] especially from 2pm onward. Per a discussion with Det. Rookhuyzen, the suspect searched the internet 15 minutes prior to calling 9-1-1 in regards to his 11-week old child suffering injuries. Suspect claimed that the internet searches were regarding how to aid an injured infant. Pertinent examination results should be regarding child abuse and a possible history thereof."</blockquote>
<p id="p-26">When Rookhuyzen made the initial request to the lab, he provided a list of 19 search terms. A week later, another detective, Hays, added eight more search terms.<footnotemark>1</footnotemark></p>
<p id="p-27">The scope of the analysis of the computers expanded further. The report noted that about a month after the initial request, a detective directed that the search of the computer be expanded to include email, although no relevant emails were ultimately located. The forensic examiners also included in the report search terms that were not provided by the detectives, but that, in their opinion, "yielded possibly pertinent results."<footnotemark>2</footnotemark> The forensic examiner stated that <a class="page-label" data-citation-index="2" data-label="192" href="#p192" id="p192">**192</a>he had no knowledge of the case itself, other than what he had learned from the detective's request regarding the examination of the computers.</p>
<p id="p-28">The report also summarized the lab's methods and findings. For each computer and laptop, the storage media were removed and imaged.<footnotemark>3</footnotemark> An initial analysis revealed that some of the hard drives had last been used in 2009, and those were not examined further. For the remaining drives, the forensic examiner assembled a "complete Internet history <a class="page-label" data-citation-index="1" data-label="329" href="#p329" id="p329">*329</a>," including "deleted Internet history records." "Internet history" is a broad term. The software used by the lab-"Net Analysis"-compiled many types of data, for example, cookies, cached data, "leaks," and other types of data that are generated as part of normal internet browsing activity, to create the internet history dataset.<footnotemark>4</footnotemark> Each piece of internet history data might contain or be associated with information useful to investigators, such as the identity of the computer user logged in at the time, the time and date that a particular web page was visited, or search terms entered into search engines, but each piece of data was not associated with all of those types of information. For example, not all records were associated with a date and time or revealed how the user navigated to a particular web page.</p>
<p id="p-29">The internet history dataset was compiled into a large spreadsheet containing over 360,000 records dating back to 2005-six years before B was born. Net Analysis allowed the forensic examiner to search for text in any of the <a class="page-label" data-citation-index="2" data-label="193" href="#p193" id="p193">**193</a>websites visited and to organize the internet history records by date and time. In addition to a printed summary of its findings, the lab provided detectives with a DVD containing that dataset and several lengthy reports on specific searches requested by detectives. For example, one report listed all web URLs visited on the date of the 9-1-1 call, beginning with a visit to Netflix nine seconds after midnight and continuing until that afternoon. That report is 630 pages long. Another report that listed results for the search term "abuse" was 101 pages long, and contained URLs dating from a 16 month period as well as many other URLs not associated with a date and time. The lab also provided reports for the search terms that "originated during the examination" as yielding "possibly pertinent results," listed above. Similarly, the DVD contained files that were not internet history, but that the forensic examiner believed might be relevant, such as a Microsoft Word document containing a narrative description of the child's birth, photos of B, and a downloaded computer game that allowed the user to simulate child abuse.</p>
<p id="p-30">Before trial, defendant moved to suppress the evidence discovered on the computers, arguing that the warrant was "worded so broadly as to constitute a general warrant." Defendant suggested that "search protocols" should have been included in the warrant to restrict the potentially unlimited search of the computer hard drives. A search protocol, for example, could limit the search to specific files or types of data on the computer-such as emails, internet searches, or photographs-or to search terms used in an internet browser. <em>See</em> <em>United States v. Comprehensive Drug Testing, Inc.</em> , <extracted-citation case-ids="3783527" index="4" url="https://cite.case.law/f3d/621/1162/#p1179"><span class="citation" data-id="9438359"><a href="/opinion/175207/united-states-v-comprehensive-drug-testing-inc/" aria-description="Citation for case: United States v. Comprehensive Drug Testing, Inc.">621 F.3d 1162</a></span></extracted-citation>, 1179 (9th Cir. 2010) (on rehearing en banc) (Kozinski, C.J., concurring) (discussing search protocols in warrants to search computers).</p>
<p id="p-31">The trial court denied the motion in a written opinion. The trial court first noted that defendant had conceded that the search warrant properly permitted law enforcement officials to search the computers for the June 12 internet search history. The court then rejected defendant's argument that the lack of search protocols in the warrant rendered the warrant unconstitutional, noting that the majority view is that such protocols are not constitutionally required. The court found that the affidavit did not provide <a class="page-label" data-citation-index="2" data-label="194" href="#p194" id="p194">**194</a>probable cause to search the computer for evidence of any crimes other than those related to B's injuries on June 12. Nevertheless, and apparently relying on the "traditional rules for the plain view exception," the court concluded that "all evidence obtained through the execution of the warrant [was] admissible."<footnotemark>5</footnotemark> <a class="page-label" data-citation-index="1" data-label="330" href="#p330" id="p330">*330</a>At trial, Detective Hays relied on the forensic lab's reports to testify about defendant's internet history. He stated that shortly before the 9-1-1 call, defendant searched the term "baby pulse no breathing"-a search consistent with defendant's explanation of events. The focus of Hays's testimony on defendant's internet history, however, was computer activity that occurred before that day. Interpreting reports generated by the forensic examiner, Hays concluded that on five separate occasions-the day of the 9-1-1 call and four earlier occasions, the earliest 54 days before the call-the computer had been used to conduct searches about or related to child abuse. The prosecutor implied that the search terms typed into the computer, often in quick succession, provided a snapshot of defendant's thought process and conduct. For example, three days before the 9-1-1 call, there were many relevant searches, including, at 6:24 a.m., a search for "afraid of abusing my baby," then shortly after that, "how do I deal with a screaming baby," then three minutes later, "baby, swelling, back of head."<footnotemark>6</footnotemark></p>
<p id="p-32">The evidence gathered from defendant's computer was undoubtedly helpful to the state's case. In the state's closing argument, the prosecutor called internet search history "a looking glass" into a person's character and "a record <a class="page-label" data-citation-index="2" data-label="195" href="#p195" id="p195">**195</a>of what's going on in [defendant's] head." The prosecutor recited strings of sequential search terms to the jury, such as those quoted above, and used those to speculate about defendant's thought process. Defendant's ex-wife and B's mother also relied on the internet history to understand what had happened. She said that in the first two weeks after B's death, she supported defendant because she couldn't believe that he would hurt B. But "[w]hen the evidence came to light about [defendant's] computer searches, I stopped supporting him."</p>
<p id="p-33">The state charged defendant with six counts relating to three discrete incidents of abuse against B and B's twin in the weeks before B's death, and four counts relating to the incident that caused B's death. After an eleven day trial, the jury convicted defendant of all charged counts: murder, assault in the first degree, three counts of assault in the third degree, and three counts of criminal mistreatment in the first degree.</p>
<p id="p-34">On appeal, defendant challenged the warrant as facially invalid because it failed to satisfy the particularity requirement of Article I, section 9, of the Oregon Constitution. Defendant also asserted that, to determine whether the warrant was valid, the court should look at the warrant alone and not consider information contained in the affidavit that supported the warrant application.</p>
<p id="p-35">The Court of Appeals first addressed whether its review of the warrant was limited to the face of the warrant or whether it also could look at the affidavit. <em>Mansor</em> , <extracted-citation case-ids="12167760" index="5" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">279 Or. App. at 788</a></span></extracted-citation>, <extracted-citation case-ids="12167760" index="6" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">381 P.3d 930</a></span></extracted-citation>. It noted that the state had introduced evidence at trial that supported its contention that the affidavit was attached to the warrant at the time defendant's house was searched, and that defendant had not produced any evidence to the contrary. <em><extracted-citation case-ids="12167760" index="7" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12167760" index="7" url="https://cite.case.law/or-app/279/778/#p801"> at 790</extracted-citation>, <extracted-citation case-ids="12167760" index="8" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">381 P.3d 930</a></span></extracted-citation>. A defendant bears the burden to rebut the presumption that a warranted search is valid. <em>State v. Walker</em> , <extracted-citation case-ids="3674252" index="9" url="https://cite.case.law/or/350/540/#p553"><span class="citation" data-id="834902"><a href="/opinion/834902/state-v-walker/" aria-description="Citation for case: State v. Walker">350 Or. 540</a></span></extracted-citation>, 553, <extracted-citation case-ids="3674252" index="10" url="https://cite.case.law/or/350/540/#p553"><span class="citation" data-id="834902"><a href="/opinion/834902/state-v-walker/" aria-description="Citation for case: State v. Walker">258 P.3d 1228</a></span></extracted-citation> (2011). Because defendant had not presented any evidence supporting his argument, the court held that it would consider the contents of the affidavit in the challenge to the warrant. <em>Mansor</em> , <extracted-citation case-ids="12167760" index="11" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">279 Or. App. at 791</a></span></extracted-citation>, <extracted-citation case-ids="12167760" index="12" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">381 P.3d 930</a></span></extracted-citation>.</p>
<p id="p-36"><a class="page-label" data-citation-index="2" data-label="196" href="#p196" id="p196">**196</a>But on the broader issue of the warrant's validity, the court held that, even considering the information in the affidavit as well as the warrant, the warrant was unconstitutionally overbroad in authorizing the forensic <a class="page-label" data-citation-index="1" data-label="331" href="#p331" id="p331">*331</a>examination of defendant's computers. It recognized that the case presented a question of first impression and reviewed decisions from other courts, some of which invalidated computer search warrants for failing to meet particularity requirements. It quoted with approval <em>Wheeler v. State</em> , <extracted-citation case-ids="6807397" index="13" url="https://cite.case.law/a3d/135/282/"><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/" aria-description="Citation for case: Wheeler v. State">135 A.3d 282</a></span></extracted-citation> (Del 2016), which adopted a requirement that warrants "describe what investigating officers believe will be found on electronic devices with as much specificity as possible under the circumstances." <em>Mansor</em> , <extracted-citation case-ids="12167760" index="14" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">279 Or. App. at 796</a></span></extracted-citation>, <extracted-citation case-ids="12167760" index="15" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">381 P.3d 930</a></span></extracted-citation> (quoting <em>Wheeler</em> , <extracted-citation case-ids="6807397" index="16" url="https://cite.case.law/a3d/135/282/">135 A.3d at </extracted-citation>304 ). The court, in light of the "unique functionality and capacity of electronic devices," concluded that</p>
<blockquote id="p-37">"for purposes of the constitutional particularity requirement, personal electronic devices are more akin to the 'place' to be searched than to the 'thing' to be seized and examined. Concomitantly, that requires that the search of that 'place' be limited to the 'thing(s)'-the digital data-for which there is probable cause to search."</blockquote>
<p id="p-38"><em>Id</em> . at 801, <extracted-citation case-ids="12167760" index="17" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">381 P.3d 930</a></span></extracted-citation>.<footnotemark>7</footnotemark></p>
<p id="p-39">The court then applied that rule. It read the warrant and affidavit as establishing probable cause</p>
<blockquote id="p-40">"with respect to internet searches during the 15-minute period preceding the 9-1-1 call-and, arguably, with respect to all electronic communications and photos during the entire time that B was in defendant's care on June 12, 2011. However, nothing in Rookhuyzen's affidavit established probable cause that a temporally unlimited examination of the contents of defendant's computers, including of files and functions unrelated to internet searches and emails, would yield other evidence of the events of June 12, 2011."</blockquote>
<p id="p-41"><em><extracted-citation case-ids="12167760" index="18" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12167760" index="18" url="https://cite.case.law/or-app/279/778/#p801"> at 802</extracted-citation>, <extracted-citation case-ids="12167760" index="19" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">381 P.3d 930</a></span></extracted-citation>. The court also found that the trial court's error in denying the motion to suppress was not harmless and, for those reasons, reversed and remanded. We allowed the state's petition for review to consider those important issues.</p>
<p id="p-42"><a class="page-label" data-citation-index="2" data-label="197" href="#p197" id="p197">**197</a>II. THE DIGITAL CONTEXT</p>
<p id="p-43">Before addressing the parties' legal arguments, it is helpful to identify some of the ways that digital data, whether stored on a computer or other digital device, differs from physical evidence. First, raw digital data-the 1s and 0s that make up binary signals-must be processed and displayed by intermediating programs and hardware to be meaningful. A user may conceive of the information on her computer as being "files," organized into "folders" that are stored in various locations on the computer and accessed through particular software programs. But a computer forensic examiner views the same data differently. As demonstrated by the facts of this case, a category of information that is a likely source of evidence-say, the internet search history on a given computer-may be composed of many types of data and files, and the physical locations of data on a computer hard drive and even the software's organization of those data and files may be unrelated to the user's perception of how their data is organized. <em>See</em> Josh Goldfoot, <em>The Physical Computer and the Fourth Amendment</em> , 16 Berkeley J. Crim. L. 112, 128 (2011) (explaining that "files do not correspond to organizational choices made by computer users").</p>
<p id="p-44">Similarly, some data on a computer may not be in the form of "files." For example, when a user deletes a file, fragments of the file's raw data often continue to exist on the hard drive. A forensic examiner may be able to reconstitute a new file from that residual data that can then be read by a program. That concept-that digital information is perceived in fundamentally different ways by users than by forensic examiners-means that a user's honest statements about a file, such as "it's in the 'My Documents' folder," "that document is gone, I didn't save it," or "no one can use my computer without my password," may not be "true" to a forensic <a class="page-label" data-citation-index="1" data-label="332" href="#p332" id="p332">*332</a>examiner.<footnotemark>8</footnotemark> We discuss the implications of the foregoing context below. <a class="page-label" data-citation-index="2" data-label="198" href="#p198" id="p198">**198</a>Digital evidence also differs from physical evidence in that, for most files, there is no way to know what data a file contains without opening it, meaning that desired data may be located in any part of the digital media or organizational structure. Indeed, data stored on a computer hard drive may be physically located in multiples places on the drive, and it is unhelpful and often inaccurate to think of the data as being located at any particular "place" or "places." In the physical world, a handgun cannot be disguised as-and will not be mistaken for-a kitchen table, nor will it be found in a pill bottle. But in the virtual world, that kind of deception-or error-is possible. A picture file may be intentionally disguised as a text file, for example, by changing the extension of the file name or by including the picture in a Microsoft Word document, which would be properly saved as a .doc (or similar) file. A picture file may contain text information if, for example, the picture is of a page of a book. Sophisticated users can hide digital data in much more complex ways, including changing date and time metadata and encrypting files so that they cannot be opened. <em>See</em> Orin S. Kerr, <em>Executing Warrants for Digital Evidence: The case for use restrictions on nonresponsive data</em> , <extracted-citation index="20" url="https://cite.case.law/citations/?q=48%20Tex.%20Tech%20L.%20Rev.%201">48 Tex. Tech. L. Rev. 1</extracted-citation>, 16 (2015) ("Data can always be changed. Maybe the modification will be easy or maybe it will be hard. But it can always be done."). Similarly, information can be hidden unintentionally. Most of us have had the experience of neglecting to name or properly "save" a document, only to have it disappear into an obscure temporary file, with its sole identifier a number assigned by the software. And even those with limited computer skills can easily delete their internet search "history" on a particular internet browser, <a class="page-label" data-citation-index="2" data-label="199" href="#p199" id="p199">**199</a>although evidence of those searches will likely remain elsewhere on the hard drive. A forensic examiner who locates intentionally (or unintentionally) hidden information on a computer likely has responded to clues, followed instincts, and pursued many dead ends before being successful. <em>See</em> Orin S. Kerr, <em>Searches and Seizures in a Digital World</em> , <extracted-citation index="21" url="https://cite.case.law/citations/?q=119%20Harv.%20L.%20Rev.%20531"><span class="citation no-link">119 Harv. L. Rev. 531</span></extracted-citation>, 545 (2005) ("[G]ood forensic analysis is an art more than a science.").</p>
<p id="p-45">For those reasons, commentators and courts sometimes refer to searches of computers in a criminal investigation as involving "two basic steps: the data acquisition phase and the data reduction phase." Kerr, 119 Harv. L. Rev. at 547 ; <em>see also</em> <em>United States v. Stabile</em> , <extracted-citation case-ids="4092190" index="22" url="https://cite.case.law/f3d/633/219/#p234"><span class="citation" data-id="183984"><a href="/opinion/183984/united-states-v-stabile/" aria-description="Citation for case: United States v. Stabile">633 F.3d 219</a></span></extracted-citation>, 234 (3d Cir. 2011), <em>cert. den.</em> , <extracted-citation case-ids="12226946,12226954,12226963,12226973,12226984,12226996,12227009,12443612,12443613,12443614,12443615,12443616,12443617,12443618,12443619,12443620,12443621,12226918,12226919,12443624,12226921,12443625,12443623,12226924,12443622,12226928,12226933,12226939" index="23" url="https://cite.case.law/us/565/942/"><span class="citation multiple-matches"><a href="/c/U.S./565/942/">565 U.S. 942</a></span></extracted-citation>, <extracted-citation case-ids="12443617,12443618,12443619,12443620,12443608,12443609" index="24" url="https://cite.case.law/s-ct/132/399/"><span class="citation" data-id="7266455"><a href="/opinion/7348477/stabile-v-united-states/" aria-description="Citation for case: Stabile v. United States">132 S.Ct. 399</a></span></extracted-citation>, <extracted-citation case-ids="12443616,12443617,12443618,12443619,12443620,12443613,12443614,12443615" index="25" url="https://cite.case.law/l-ed-2d/181/256/"><span class="citation multiple-matches"><a href="/c/L.Ed.2d/181/256/">181 L.Ed.2d 256</a></span></extracted-citation> (2011) (applying two step perspective). In the data acquisition phase, the warrant authorizes the police to search a location for a computer and to seize it. As we discuss below, that physical search and seizure must comply with constitutional requirements, including the usual particularity rules for describing the physical place to be searched and the computer to be seized. But, generally, the seized computer or data itself has not yet been determined to have any evidentiary value.<footnotemark>9</footnotemark></p>
<p id="p-46"><a class="page-label" data-citation-index="1" data-label="333" href="#p333" id="p333">*333</a>In the data reduction phase, there is an examination ("search") of the digital data, this time by a forensic examiner, to identify the particular data that may be useful as evidence. Using the familiar analogy of searching for a needle in a haystack, "data acquisition refers to collecting the hay, and data reduction involves looking through the haystack for the needle." Kerr, 119 Harv. L. Rev. at 547. Because, as noted earlier, the location or form of specific information on a computer often cannot be known before the computer is actually examined, examiners conducting a reasonable computer search ordinarily will be permitted to look widely on the computer's hard drive to ensure that all material within the scope of the warrant is found. Goldfoot, 16 Berkley J. Crim. L. at 141 (noting consensus among federal circuit courts permitting "human forensic examiners to look at every file, albeit briefly, to determine whether it is in the warrant's scope"; citing cases); <em>see</em> <em>Andresen v. Maryland,</em> <extracted-citation case-ids="6179008" index="26" url="https://cite.case.law/us/427/463/"><span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">427 U.S. 463</a></span></extracted-citation>, 482 n. 11, <extracted-citation case-ids="6179008" index="27" url="https://cite.case.law/us/427/463/"><span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">96 S.Ct. 2737</a></span></extracted-citation>, <extracted-citation case-ids="6179008" index="28" url="https://cite.case.law/us/427/463/"><span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">49 L.Ed.2d 627</a></span></extracted-citation> (1976) (holding, in nondigital context, that warranted search of attorney's office for certain papers did not violate Fourth Amendment when executing officers "cursorily" examined "innocuous documents *** to determine whether they [were], in fact, among those papers authorized to be seized"). For that reason, courts generally have not required that warrants include specific search protocols or <em>ex ante</em> limitations on computer searches. <em>See</em> <em>Stabile</em> , <extracted-citation case-ids="4092190" index="29" url="https://cite.case.law/f3d/633/219/#p234"><span class="citation" data-id="183984"><a href="/opinion/183984/united-states-v-stabile/#238" aria-description="Citation for case: United States v. Stabile">633 F.3d at 238</a></span></extracted-citation> ("[I]t would be folly for a search warrant to structure the mechanics of the search because imposing such limits would unduly restrict legitimate search objectives." (Internal quotation marks omitted.)); Wayne R. LaFave, 2 <em>Search and Seizure</em> § 4.10(d), 969 (5th ed. 2012) (noting courts are "disinclined" to impose <em>ex ante</em> search limitations). Moreover, a magistrate presented with a search warrant request, often early in a criminal investigation, would have little basis to make an informed decision as to whether proposed protocols regarding the seizure and search of a computer are sufficient to protect constitutional privacy interests or impose a constitutionally unnecessary burden on a criminal investigation. <em>See</em> Orin S. Kerr, <em>Ex Ante Regulation of Computer Search and Seizure,</em> <extracted-citation index="30" url="https://cite.case.law/citations/?q=96%20Va.%20L.%20Rev.%201241"><span class="citation no-link">96 Va. L. Rev. 1241</span></extracted-citation>, 1293 (2010) ("The factual vacuum of <em>ex ante</em> and <em>ex parte</em> decisionmaking leads such restrictions to introduce constitutional errors that inadvertently prohibit reasonable search and seizure practices.").</p>
<p id="p-47">Finally, the novel nature of digital devices has led courts to apply search and seizure principles to those devices in a manner somewhat different from other physical evidence. The Supreme Court addressed some of those issues in <em>Riley v. California</em> , --- U.S. ----, <extracted-citation case-ids="12581677" index="31" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. 2473</a></span></extracted-citation>, <extracted-citation case-ids="12581677" index="32" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">189 L.Ed.2d 430</a></span></extracted-citation> (2014), and we discuss that case as background, because many of the parties' arguments in this case about searches of digital devices also were raised there.</p>
<p id="p-48">In <em><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Riley</a></span>,</em> the Court considered a petitioner's post-conviction challenge to the warrantless search of his "smart phone" that police officers found in his pocket at the time of his arrest following a traffic stop and that they later examined at the police station.<footnotemark>10</footnotemark> <em><extracted-citation case-ids="12581677" index="33" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12581677" index="33" url="https://cite.case.law/s-ct/134/2473/"> at 2480-81</extracted-citation>. The police found, among other things, gang-affiliated material and a photo of the defendant with a car linked to a shooting; the evidence ultimately supported his conviction for three crimes, including attempted murder, that were unrelated to the initial arrest. <em><extracted-citation case-ids="12581677" index="34" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12581677" index="34" url="https://cite.case.law/s-ct/134/2473/"> at 2481</extracted-citation>. The government <a class="page-label" data-citation-index="1" data-label="334" href="#p334" id="p334">*334</a>argued that, because the phone had been lawfully seized when the defendant was arrested, any information on the phone also was legitimately seized and could be used at trial. The government suggested that a search of all data on a cell phone was "materially indistinguishable" from searches of other physical items that might be found in a defendant's pocket. <em><extracted-citation case-ids="12581677" index="35" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12581677" index="35" url="https://cite.case.law/s-ct/134/2473/"> at 2488</extracted-citation>.</p>
<p id="p-49">The Court rejected that argument:</p>
<blockquote id="p-50">"That is like saying a ride on horseback is materially indistinguishable from a flight to the moon. * * * Modern cell phones, as a category, implicate privacy concerns far beyond those implicated by the search of a cigarette pack, a wallet, or a purse. A conclusion that inspecting the contents of an arrestee's pockets works no substantial additional intrusion on privacy beyond the arrest itself may make sense as applied to physical items, but any extension of that reasoning to digital data has to rest on its own bottom."</blockquote>
<p id="p-51"><em><extracted-citation case-ids="12581677" index="36" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12581677" index="36" url="https://cite.case.law/s-ct/134/2473/"> at 2488-89</extracted-citation>. The Court identified the several ways in which cell phones "differ in both a quantitative and a qualitative sense" from other objects that might be found on an arrestee's person-and many of those characteristics also describe defendant's computer here. <em><extracted-citation case-ids="12581677" index="37" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12581677" index="37" url="https://cite.case.law/s-ct/134/2473/"> at 2489</extracted-citation>.</p>
<p id="p-52">The Court noted that the "immense storage capacity" of cell phones means that the physical limitation on the amount of information a person could carry no longer applied. <em><extracted-citation case-ids="12581677" index="38" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Id.</a></span></extracted-citation></em> A large storage capacity means that even a single category of information, such as emails or photographs, can "convey far more than previously possible. The sum of an individual's private life can be reconstructed through a thousand photographs labeled with dates, locations, and descriptions; the same cannot be said of a photograph or two of loved ones tucked into a wallet." <em><extracted-citation case-ids="12581677" index="39" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Id.</a></span></extracted-citation></em> Further, a cell phone collects "many distinct types of information-an address, a note, a prescription, a bank statement, a video-that reveal much more in combination than any isolated record." <em><extracted-citation case-ids="12581677" index="40" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Id.</a></span></extracted-citation></em> Internet history can reveal "an individual's private interests or concerns"; location data can show where a person has been; and apps on a phone may provide information about, for example, an individual's political views, addiction treatment, dating, buying and selling, pregnancy, budgeting, and communicating. <em><extracted-citation case-ids="12581677" index="41" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12581677" index="41" url="https://cite.case.law/s-ct/134/2473/"> at 2490</extracted-citation>. The Court not only rejected the government's claim that a cell phone was more like a "thing" than a "place," it also stated that even treating a cell phone like a house is insufficient to protect the privacy interests that many individuals have in the information stored in their phones:</p>
<blockquote id="p-53">"[A] cell phone search would typically expose to the government far <em>more</em> than the most exhaustive search of a house: A phone not only contains in digital form many sensitive records previously found in the home; it also contains a broad array of private information never found in a home in any form-unless the phone is."</blockquote>
<p id="p-54"><em><extracted-citation case-ids="12581677" index="42" url="https://cite.case.law/s-ct/134/2473/">Id.</extracted-citation></em><extracted-citation case-ids="12581677" index="42" url="https://cite.case.law/s-ct/134/2473/"> at 2491</extracted-citation> (emphasis in original).</p>
<p id="p-55">The Court explained that the development of the cell phone had undermined assumptions supporting the incident to arrest exception to the warrant requirement; with a cell phone, an arrestee could be carrying the equivalent of all the information in his house, or more. Therefore, the Court held that the exception could not be used to justify the search of cell phones, and it instead directed officers seeking to examine the contents of a cell phone to "get a warrant." <em><extracted-citation case-ids="12581677" index="43" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Id.</a></span></extracted-citation></em><extracted-citation case-ids="12581677" index="43" url="https://cite.case.law/s-ct/134/2473/"> at 2495</extracted-citation>.</p>
<p id="p-56">In this case, of course, the officers had a warrant, and we return to the facts here and the question of the validity of the warrant and the search of defendant's computer.</p>
<p id="p-57">III. MAY THE AFFIDAVIT BE CONSIDERED WITH THE WARRANT?</p>
<p id="p-58">We first address the issue of whether the information contained in Rookhuyzen's affidavit is properly considered part of the warrant itself. In the Court of Appeals, the state asserted that the affidavit was "attached to and referenced by" the warrant and, as a result, the court should consider the contents of the affidavit as part of the warrant in deciding defendant's challenge to the warrant's facial validity. In his response, defendant agreed that an affidavit may be considered part of the warrant if it physically accompanies the warrant and the warrant <a class="page-label" data-citation-index="1" data-label="335" href="#p335" id="p335">*335</a>explicitly incorporates it by reference; however, defendant disputed that the state had established that the warrant here met those requirements, and, therefore, he claimed that the contents of the affidavit should not be considered.<footnotemark>11</footnotemark></p>
<p id="p-59">The Court of Appeals observed that, when a search is conducted pursuant to a warrant, the defendant bears "the burden of establishing facts pertaining to his 'challenge [to] the validity of the warrant itself.' " <em>Mansor</em> , <extracted-citation case-ids="12167760" index="44" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">279 Or. App. at 790</a></span></extracted-citation>, <extracted-citation case-ids="12167760" index="45" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">381 P.3d 930</a></span></extracted-citation> (quoting <em>Walker</em> , <extracted-citation case-ids="3674252" index="46" url="https://cite.case.law/or/350/540/#p553"><span class="citation" data-id="834902"><a href="/opinion/834902/state-v-walker/" aria-description="Citation for case: State v. Walker">350 Or. at 555</a></span></extracted-citation>, <extracted-citation case-ids="3674252" index="47" url="https://cite.case.law/or/350/540/#p553"><span class="citation" data-id="834902"><a href="/opinion/834902/state-v-walker/" aria-description="Citation for case: State v. Walker">258 P.3d 1228</a></span></extracted-citation> (brackets in <em><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">Mansor</a></span></em> ) ). Here, the state's contention that the affidavit was attached to and referenced in the warrant at the time of execution was supported, as the Court of Appeals said, by "permissible, albeit hardly indubitable, inference." <em><extracted-citation case-ids="3674252" index="48" url="https://cite.case.law/or/350/540/#p553"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">Id.</a></span></extracted-citation></em> Defendant presented no evidence to controvert that inference. <em><extracted-citation case-ids="3674252" index="49" url="https://cite.case.law/or/350/540/#p553"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">Id.</a></span></extracted-citation></em> On that record, the Court of Appeals concluded that defendant fell short of his burden of production and therefore considered the affidavit to be part of the warrant for purposes of its review.</p>
<p id="p-60">We agree with the Court of Appeals that defendant failed in the trial court to establish the factual basis for his argument on appeal; for purposes of this case, we consider the text of the affidavit to be part of the warrant. That said, we note that parties may spend substantial time litigating whether the contents of an affidavit should be considered in a challenge to a warrant. <em>See</em> LaFave, 2 <em>Search and Seizure</em> § 4.6(1) at 778 (noting a "great variety of viewpoints" on the issue). In our view, rather than relying on indirect inferences to establish a connection between the warrant and an affidavit, the better practice is for the warrant to include specific text from the affidavit or to incorporate the affidavit by express reference in the warrant. Merely attaching the affidavit or an exhibit with an attached affidavit to the warrant, without some textual reference, creates the ambiguous situation apparently present here. Moreover, as we discuss in greater detail below, in order to guide the persons conducting the forensic examination of a properly seized computer, the warrant itself should describe, with as much specificity as reasonably possible, the category or categories of information to be searched for on the computer, including, if available and relevant, the time period when the information was created, accessed, or otherwise used. That description, of course, must be based on affidavits or other record evidence that establishes probable cause to search the computer for such information.</p>
<p id="p-61">Because we have concluded that the affidavit should be considered as part of the warrant in this case, it follows that the contents of the affidavit assist us in determining the scope of the search that the warrant permitted. The warrant itself authorized police to "seize and search and forensically examine" certain items listed in an attachment, and the listed items included defendant's computers. The affidavit also referred to, and sought authority to search for and seize, those items, and an exhibit to the affidavit refers to "items to be searched for, to be seized, and to be analyzed." The only reference in the affidavit to relevant information that Rookhuyzen believed was on the computer was the paragraph set out above, 363 Or. at 204, 421 P.3d at 328 (and one related sentence in the affidavit), regarding defendant's statements about searching the internet for first aid advice in the 15 minutes before he made the 9-1-1 call. Although the warrant, supplemented by the affidavit, authorized the "search," "analy[sis]," and "forensic[ ] examinat[ion]" of all the items seized, including the computers, the only description of any relevant information that Rookhuyzen believed might be found on the computers was that of the June 12 internet search history. We therefore view that description of the information to be searched for as a limitation on the search, analysis, and forensic examination authorized by the warrant.<footnotemark>12</footnotemark></p>
<p id="p-62"><a class="page-label" data-citation-index="1" data-label="336" href="#p336" id="p336">*336</a>IV. IS THE WARRANT VALID?</p>
<p id="p-63">A. <em>Search and Seizure Principles and History</em></p>
<p id="p-64">This case raises questions under Article I, section 9, of the specificity with which a warrant must describe the digital information that the state seeks, the search that the state may conduct, and the evidence that the state may use when police have probable cause to believe that a computer contains information related to a crime. Those questions implicate fundamental issues of personal privacy and the state's responsibility to prosecute crime in the novel and rapidly evolving context of digital evidence. Although this court previously has addressed the application of Article I, section 9, to some types of electronic evidence, we have not yet considered the application of the constitutional principles to the unique characteristics of a personal computer.</p>
<p id="p-65">To do so, "we consider the 'specific wording of Article I, section 9, the case law surrounding it, and the historical circumstances that led to its creation.' " <em>State v. Carter</em> , <extracted-citation case-ids="3561709" index="50" url="https://cite.case.law/or/342/39/#p42"><span class="citation" data-id="835510"><a href="/opinion/835510/state-v-carter/" aria-description="Citation for case: State v. Carter">342 Or. 39</a></span></extracted-citation>, 42, <extracted-citation case-ids="3561709" index="51" url="https://cite.case.law/or/342/39/#p42"><span class="citation" data-id="835510"><a href="/opinion/835510/state-v-carter/" aria-description="Citation for case: State v. Carter">147 P.3d 1151</a></span></extracted-citation> (2006) (quoting <em>Priest v. Pearce</em> , <extracted-citation case-ids="2192812" index="52" url="https://cite.case.law/or/314/411/#p415"><span class="citation" data-id="9632733"><a href="/opinion/1450023/priest-v-pearce/" aria-description="Citation for case: Priest v. Pearce">314 Or. 411</a></span></extracted-citation>, 415-16, <extracted-citation case-ids="2192812" index="53" url="https://cite.case.law/or/314/411/#p415"><span class="citation" data-id="9632733"><a href="/opinion/1450023/priest-v-pearce/" aria-description="Citation for case: Priest v. Pearce">840 P.2d 65</a></span></extracted-citation> (1992) (brackets omitted) ). The purpose of the historical analysis required under <em><span class="citation" data-id="9632733"><a href="/opinion/1450023/priest-v-pearce/" aria-description="Citation for case: Priest v. Pearce">Priest</a></span></em> is not to "freeze" the meaning of the state constitution at the time of its adoption. <em>State v. Davis</em> , <extracted-citation case-ids="3674483" index="54" url="https://cite.case.law/or/350/440/#p446"><span class="citation" data-id="834912"><a href="/opinion/834912/state-v-davis/" aria-description="Citation for case: State v. Davis">350 Or. 440</a></span></extracted-citation>, 446, <extracted-citation case-ids="3674483" index="55" url="https://cite.case.law/or/350/440/#p446"><span class="citation" data-id="834912"><a href="/opinion/834912/state-v-davis/" aria-description="Citation for case: State v. Davis">256 P.3d 1075</a></span></extracted-citation> (2011). "Rather it is to identify, in light of the meaning understood by the framers, relevant underlying principles that may inform our application of the constitutional text to modern circumstances." <em><extracted-citation case-ids="3674483" index="56" url="https://cite.case.law/or/350/440/#p446"><span class="citation" data-id="834912"><a href="/opinion/834912/state-v-davis/" aria-description="Citation for case: State v. Davis">Id.</a></span></extracted-citation></em></p>
<p id="p-66">Article I, section 9, of the Oregon Constitution provides:</p>
<blockquote id="p-67">"No law shall violate the right of the people to be secure in their persons, houses, papers, and effects, against unreasonable search, or seizure; and no warrant shall issue but upon probable cause, supported by oath, or affirmation, and particularly describing the place to be searched, and the person or thing to be seized."</blockquote>
<p id="p-68">Using that text as a starting point, we review this court's Article I, section 9, case law and our earlier discussions of historical circumstances. We consider whether the unique characteristics of computers make them unlike other "things" that may be seized. Then we determine what it means to "particularly describ[e] *** [the] thing to be seized" in the warrant, when that "thing" is information on a computer. Finally, we apply the results of our discussion to the facts of this case.</p>
<p id="p-69">The text and principles of Article I, section 9, can be traced directly to the Fourth Amendment to the United States Constitution, and from there to state constitutional documents dating to the American Revolution. <em>See</em> <em>State v. Bridewell</em> , <extracted-citation case-ids="2205383" index="57" url="https://cite.case.law/or/306/231/#p241"><span class="citation" data-id="9564908"><a href="/opinion/1215390/state-v-bridewell/" aria-description="Citation for case: State v. Bridewell">306 Or. 231</a></span></extracted-citation>, 241, <extracted-citation case-ids="2205383" index="58" url="https://cite.case.law/or/306/231/#p241"><span class="citation" data-id="9564908"><a href="/opinion/1215390/state-v-bridewell/" aria-description="Citation for case: State v. Bridewell">759 P.2d 1054</a></span></extracted-citation> (1988) (Peterson, C. J., concurring in part, dissenting in part) (discussing history of Article I, section 9 ); <em>see also</em> Jack L. Landau, <em>The Search for the Meaning of Oregon's Search and Seizure Clause</em> , <extracted-citation index="59" url="https://cite.case.law/citations/?q=87%20Or.%20L.%20Rev.%20819"><span class="citation no-link">87 Or. L. Rev. 819</span></extracted-citation>, 836-840 (2008) (recounting the origins of Article I, section 9 ). Those provisions themselves were, among other things, reactions to abusive "general warrants" of the English colonial government, which gave government agents "unlimited authority to search and seize." <em>State v. Blackburn/Barber</em> , <extracted-citation case-ids="2130981" index="60" url="https://cite.case.law/or/266/28/#p34"><span class="citation" data-id="9551175"><a href="/opinion/1183382/state-v-blackburn/" aria-description="Citation for case: State v. Blackburn">266 Or. 28</a></span></extracted-citation>, 34, <extracted-citation case-ids="2130981" index="61" url="https://cite.case.law/or/266/28/#p34"><span class="citation" data-id="9551175"><a href="/opinion/1183382/state-v-blackburn/" aria-description="Citation for case: State v. Blackburn">511 P.2d 381</a></span></extracted-citation> (1973) (explaining that a historical motivation for Article I, section 9, was a fear of general warrants); <em>see also</em> Landau, 87 Or. L. Rev. at 822-23 (" 'General warrants' referred to writs that authorized the bearer to search unspecified places or arrest persons suspected of having been involved with a criminal offense."); Laura K. Donohue, <em>The Original Fourth Amendment</em> , <extracted-citation index="62" url="https://cite.case.law/citations/?q=83%20U.%20Chi.%20L.%20Rev.%201181"><span class="citation no-link">83 U. Chi. L. Rev. 1181</span></extracted-citation> (2016) (relating the role of general warrants in the framers' development of the Fourth Amendment).</p>
<p id="p-70">As we have previously explained, "[t]he privacy interests protected from unreasonable searches under Article I, section 9, are defined by an objective test of whether the government's conduct 'would significantly impair an individual's interest in freedom from scrutiny, <em>i.e.</em> , his privacy.' " <em>State v. Wacker</em> , <extracted-citation case-ids="2210073" index="63" url="https://cite.case.law/or/317/419/#p425"><span class="citation" data-id="9602574"><a href="/opinion/1364515/state-v-wacker/" aria-description="Citation for case: State v. Wacker">317 Or. 419</a></span></extracted-citation>, 425, <extracted-citation case-ids="2210073" index="64" url="https://cite.case.law/or/317/419/#p425"><span class="citation" data-id="9602574"><a href="/opinion/1364515/state-v-wacker/" aria-description="Citation for case: State v. Wacker">856 P.2d 1029</a></span></extracted-citation> (1993) (quoting <em>State v. Dixson/Digby</em> , <extracted-citation case-ids="2204188" index="65" url="https://cite.case.law/or/307/195/#p211"><span class="citation" data-id="1349523"><a href="/opinion/1349523/state-v-dixson/" aria-description="Citation for case: State v. Dixson">307 Or. 195</a></span></extracted-citation>, 211, <extracted-citation case-ids="2204188" index="66" url="https://cite.case.law/or/307/195/#p211"><span class="citation" data-id="1349523"><a href="/opinion/1349523/state-v-dixson/" aria-description="Citation for case: State v. Dixson">766 P.2d 1015</a></span></extracted-citation> (1988) ). Because "private <em>space</em> and privacy <em>interests</em> often are inextricably intertwined[,] * * * privacy interests that are protected by Article I, section 9, commonly are circumscribed by the <a class="page-label" data-citation-index="1" data-label="337" href="#p337" id="p337">*337</a>space in which they exist and, more particularly, by the barriers to public entry (physical and sensory) that define that private space." <em>State v. Smith</em> , <extracted-citation case-ids="701795" index="67" url="https://cite.case.law/or/327/366/#p372"><span class="citation" data-id="836553"><a href="/opinion/836553/state-v-smith/" aria-description="Citation for case: State v. Smith">327 Or. 366</a></span></extracted-citation>, 372-73, <extracted-citation case-ids="701795" index="68" url="https://cite.case.law/or/327/366/#p372"><span class="citation" data-id="836553"><a href="/opinion/836553/state-v-smith/" aria-description="Citation for case: State v. Smith">963 P.2d 642</a></span></extracted-citation> (1998) (emphasis in original). At the same time, we have recognized that Article I, section 9, "must be read in light of the ever-expanding capacity of individuals and the government to gather information by technological means." <em><extracted-citation case-ids="701795" index="69" url="https://cite.case.law/or/327/366/#p372"><span class="citation" data-id="836553"><a href="/opinion/836553/state-v-smith/" aria-description="Citation for case: State v. Smith">Id.</a></span></extracted-citation></em><extracted-citation case-ids="701795" index="69" url="https://cite.case.law/or/327/366/#p372"> at 373</extracted-citation>, <extracted-citation case-ids="701795" index="70" url="https://cite.case.law/or/327/366/#p372"><span class="citation" data-id="836553"><a href="/opinion/836553/state-v-smith/" aria-description="Citation for case: State v. Smith">963 P.2d 642</a></span></extracted-citation>. That is, Article I, section 9, applies to "every possible form of invasion-physical, electronic, technological, and the like." <em><extracted-citation case-ids="701795" index="71" url="https://cite.case.law/or/327/366/#p372"><span class="citation" data-id="836553"><a href="/opinion/836553/state-v-smith/" aria-description="Citation for case: State v. Smith">Id.</a></span></extracted-citation></em> We discuss the permissible scope of that legal intrusion below.</p>
<p id="p-71">B. <em>Search for and Seizure of Computers</em></p>
<p id="p-72">1. <em>Seizure of the computers</em></p>
<p id="p-73">We begin by considering briefly the search for and seizure of defendant's computers themselves. Although defendant's motion to suppress challenged the seizure of the computers as well as the forensic examination of the computers for evidence and the use of that evidence at trial, defendant no longer argues that the seizure of the physical computers violated Article I, section 9. That argument would fail in any event. The warrant recounted defendant's statements to Rookhuyzen about his internet searches, identified two laptop computers and two desktop computer towers in the apartment, and included statements by Rookhuyzen about how internet search engines are used to seek information (as defendant stated that he had done when B was not breathing) and about the need to have an examination conducted by a trained computer forensic examiner. The warrant was sufficiently particular in its description of the computers to be seized and the grounds for believing that evidence related to the criminal investigation was likely to be found on one or more of them to meet the particularity requirement of Article I, section 9, with respect to the seizure of the computers.</p>
<p id="p-74">2. <em>Search of a lawfully seized computer</em></p>
<p id="p-75">The more difficult issue is whether the warrant's authorization of lawful seizure of the computers similarly authorized the state to conduct a search of the computers to locate and seize information or data on the computers for evidence of a crime. The principles underlying Article I, section 9, establish that an individual generally has a privacy interest in the information on his or her personal computer. A computer often is either located in a private space, such as a home, or secured by a password or biometric identification, or both. Those "barriers to public entry" are the sort contemplated in <em>Smith</em> , <extracted-citation case-ids="701795" index="72" url="https://cite.case.law/or/327/366/#p372"><span class="citation" data-id="836553"><a href="/opinion/836553/state-v-smith/" aria-description="Citation for case: State v. Smith">327 Or. at 373</a></span></extracted-citation>, <extracted-citation case-ids="701795" index="73" url="https://cite.case.law/or/327/366/#p372"><span class="citation" data-id="836553"><a href="/opinion/836553/state-v-smith/" aria-description="Citation for case: State v. Smith">963 P.2d 642</a></span></extracted-citation>, that indicate the presence of constitutionally protected privacy interests. The state does not disagree. The state argues, however, that if police obtain a valid warrant to search for and seize a computer, they are "free to examine it as they see fit." The state asserts that "a computer is a thing, and a warrant to examine it need only identify the particular computer, not the data that the examination is intended to find." The state relies on cases involving other "things" seized in warranted searches and argues that once a "thing" is seized and examined for any purpose, "any privacy interest in that object is destroyed, and no purpose would be served by further limitation on the nature of examinations that may be performed on the object."</p>
<p id="p-76">We agree with defendant and the Court of Appeals that the state's argument is not well taken. For reasons that we will explain, the fact that police have a warrant, based on probable cause, to search for and seize "things," including computers, does not necessarily mean that they may conduct a comprehensive forensic examination of a computer that they seize, and then use at trial anything they find on the computer, without limit.</p>
<p id="p-77">As noted, the state accepts that individuals have a protected privacy interest in their computers and the information on them. The state's legal argument, however, fails to account for the fact that, unlike most other "things" that may be seized in a search, a computer or other digital device is a repository with a historically unprecedented capacity to collect and store a diverse and vast array of personal information. Moreover, that information is stored in a manner that ordinarily makes it inaccessible to others. We discussed in detail above the reasons that <a class="page-label" data-citation-index="1" data-label="338" href="#p338" id="p338">*338</a>computers and digital devices are different from most other "things" that can be seized in the course of criminal investigations and the Supreme Court's recognition in <em><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Riley</a></span></em> that different search and seizure rules apply to those devices than to other "things." Indeed, the state's argument here is similar to the argument that the government made in <em><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Riley</a></span></em> and that the Supreme Court rejected: If the item (the phone or computer) is lawfully seized, then any information that can be discovered within the item also is legitimately seized and can be used at trial. Although <em><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Riley</a></span></em> involved a warrantless search incident to arrest and this case involves a computer seized pursuant to a warrant, defendant urges us to follow the Court's approach in <em><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Riley</a></span></em> and hold that computers deserve more protection than other "things" under Article I, section 9.</p>
<p id="p-78">The state argues that this court has previously held that an individual retains no privacy interest in storage media that is lawfully in the possession of the police. In <em>State v. Munro</em> , <extracted-citation case-ids="3026081" index="74" url="https://cite.case.law/or/339/545/"><span class="citation" data-id="835700"><a href="/opinion/835700/state-v-munro/" aria-description="Citation for case: State v. Munro">339 Or. 545</a></span></extracted-citation>, <extracted-citation case-ids="3026081" index="75" url="https://cite.case.law/or/339/545/"><span class="citation" data-id="835700"><a href="/opinion/835700/state-v-munro/" aria-description="Citation for case: State v. Munro">124 P.3d 1221</a></span></extracted-citation> (2005), the police raided a home pursuant to a warrant in connection with a drug investigation and seized a beta format videotape and various contraband. The defendant was prosecuted for possession of the other contraband, but the videotape appeared to be blank. About a year later, acting on new information, police were able to view the contents of the tape, discovered that it contained child pornography, and prosecuted defendant based on that evidence. The defendant challenged the later examination of the tape-which the state conceded was a "search"-as violating Article I, section 9. This court held that no violation had occurred, because "[o]nce the police seized the videotape under the authority of the warrant, any privacy interest that defendant had in the contents of the videotape was destroyed by the authority of the warrant permitting the examination and exhibition of the contents of the videotape." <em>Id</em> . at 552, <extracted-citation case-ids="3026081" index="76" url="https://cite.case.law/or/339/545/"><span class="citation" data-id="835700"><a href="/opinion/835700/state-v-munro/" aria-description="Citation for case: State v. Munro">124 P.3d 1221</a></span></extracted-citation>.</p>
<p id="p-79">The state erroneously assumes, however, that the videotape in <em><span class="citation" data-id="835700"><a href="/opinion/835700/state-v-munro/" aria-description="Citation for case: State v. Munro">Munro</a></span></em> is analogous to a computer or a cell phone. Of the unique characteristics of the cell phone described in <em><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Riley</a></span></em> -such as containing many types of information, having immense storage capacity, and playing a role in many aspects of life-a videotape has none. In contrast with a cell phone, which continually creates and stores data as it is used, the only possible "search" of a videotape is for the police to view the tape as it was recorded. <em><span class="citation" data-id="835700"><a href="/opinion/835700/state-v-munro/" aria-description="Citation for case: State v. Munro">Munro</a></span></em> held only that a single analog videotape is a "thing" for purposes of search and seizure analysis, and once it was seized pursuant to a valid warrant, the owner lost all privacy interest in it. That holding does not assist the state here.</p>
<p id="p-80">Further, the state's semantic observation that a computer is literally a "thing" is a truism that does not compel a legal conclusion. And the state provides no persuasive rejoinder to the Court's description in <em><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">Riley</a></span></em> of the technological changes that led the Court to exempt cell phones from the "search incident to arrest" doctrine. The data contained on a personal computer is qualitatively and quantitatively different from the sort of information that could be found in other single objects, or even an entire house not containing digital data. <em>See</em> <em>Riley</em> , <extracted-citation case-ids="12581677" index="77" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. at 2491</a></span></extracted-citation>. We reject the state's argument that a computer is merely a "thing to be seized" and that, once lawfully seized, the state is free to analyze or examine the computer without limit and to use any information that is found.<footnotemark>13</footnotemark></p>
<p id="p-81">We observe at this point that the state does not rely on the plain view doctrine-or any other exception to the warrant requirement-to justify the seizure and use at trial of information from defendant's computer; instead, its remaining arguments, <a class="page-label" data-citation-index="1" data-label="339" href="#p339" id="p339">*339</a>which we discuss in detail below, turn on the scope of the warrant. The plain view doctrine permits police to seize evidence without a warrant if they are in a place where they have a right to be and have probable cause to believe that the evidence that they see in "plain view" is contraband or evidence of a crime. <em>Carter,</em> <extracted-citation case-ids="3561709" index="78" url="https://cite.case.law/or/342/39/#p42"><span class="citation" data-id="835510"><a href="/opinion/835510/state-v-carter/" aria-description="Citation for case: State v. Carter">342 Or. at 45</a></span></extracted-citation>, <extracted-citation case-ids="3561709" index="79" url="https://cite.case.law/or/342/39/#p42"><span class="citation" data-id="835510"><a href="/opinion/835510/state-v-carter/" aria-description="Citation for case: State v. Carter">147 P.3d 1151</a></span></extracted-citation>. A number of courts have considered the application of the plain view doctrine in computer search cases, and the cases are divided. <em>Compare</em> <em>United States v. Williams,</em> <extracted-citation case-ids="5686340" index="80" url="https://cite.case.law/f3d/592/511/#p521"><span class="citation" data-id="1031286"><a href="/opinion/1031286/united-states-v-williams/" aria-description="Citation for case: United States v. Williams">592 F.3d 511</a></span></extracted-citation>, 521-24 (4th Cir. 2010), <em>cert. den.</em> , <extracted-citation case-ids="12438785,12438786,12438787,6004100,12438788,12438790,12438791,5951368,12438793,12438794,12438795,12438796,12438797,12438789,12438792,5902610,5987351,5970972,5930154,5984179,5927887,5919582,5954926,5951726,6033520,5994619" index="81" url="https://cite.case.law/us/562/1044/"><span class="citation multiple-matches"><a href="/c/U.S./562/1044/">562 U.S. 1044</a></span></extracted-citation>, <extracted-citation case-ids="12438785,12438786,12438787,12438806,12438778,12438781" index="82" url="https://cite.case.law/s-ct/131/595/"><span class="citation" data-id="7258325"><a href="/opinion/7340402/williams-v-united-states/" aria-description="Citation for case: Williams v. United States">131 S.Ct. 595</a></span></extracted-citation>, <extracted-citation case-ids="12438784,12438785,12438786,12438787,12438788,12438789,12438783" index="83" url="https://cite.case.law/l-ed-2d/178/434/"><span class="citation multiple-matches"><a href="/c/L.Ed.2d/178/434/">178 L.Ed.2d 434</a></span></extracted-citation> (2010) (admitting computer search data under plain view doctrine) <em>with</em> <em>Comprehensive Drug Testing, Inc.</em> , <extracted-citation case-ids="3783527" index="84" url="https://cite.case.law/f3d/621/1162/#p1179"><span class="citation" data-id="9438359"><a href="/opinion/175207/united-states-v-comprehensive-drug-testing-inc/#1170" aria-description="Citation for case: United States v. Comprehensive Drug Testing, Inc.">621 F.3d at 1170</a></span></extracted-citation> (rejecting application of plain view doctrine as "too clever by half"). Commentators also have expressed differing views. <em>Compare</em> Kerr, 119 Harv. L. Rev. at 577 (rejecting plain view in computer search cases) <em>with</em> Thomas K. Clancy, <em>The Fourth Amendment Aspects of Computer Searches and Seizures: A perspective and a primer</em> , <extracted-citation index="85" url="https://cite.case.law/citations/?q=75%20Miss.%20L.J.%20193">75 Miss. L. J. 193</extracted-citation>, 262 (2005) (approving plain view, citing cases). Moreover, it is not clear how a doctrine developed in connection with physical objects, the "incriminating character" of which must be "immediately apparent," <em>Minnesota v. Dickerson</em> , <extracted-citation case-ids="12205" index="86" url="https://cite.case.law/us/508/366/#p375"><span class="citation" data-id="9432823"><a href="/opinion/112873/minnesota-v-dickerson/" aria-description="Citation for case: Minnesota v. Dickerson">508 U.S. 366</a></span></extracted-citation>, 375, <extracted-citation case-ids="12205" index="87" url="https://cite.case.law/us/508/366/#p375"><span class="citation" data-id="9432823"><a href="/opinion/112873/minnesota-v-dickerson/" aria-description="Citation for case: Minnesota v. Dickerson">113 S.Ct. 2130</a></span></extracted-citation>, <extracted-citation case-ids="12205" index="88" url="https://cite.case.law/us/508/366/#p375"><span class="citation" data-id="9432823"><a href="/opinion/112873/minnesota-v-dickerson/" aria-description="Citation for case: Minnesota v. Dickerson">124 L.Ed.2d 334</a></span></extracted-citation> (1993), would apply to bits and files digitally stored on a computer hard drive.</p>
<p id="p-82">We recognize that some of the legal conclusions that we reach in this case likely would have implications for a plain view argument, if raised in a computer search case. However, as noted, the state does not rely on that doctrine here and neither party has briefed the issue; in these circumstances, further discussion regarding the application <em>vel non</em> of that doctrine to computer searches should await a future case.</p>
<p id="p-83">3. <em>The particularity requirement as applied to computer searches</em></p>
<p id="p-84">Our conclusion that the lawful seizure of defendant's computer does not, by itself, permit the state to analyze and use all of the information found on the computer leaves us with the task of considering the scope of the warrant and defendant's argument that the warrant was impermissibly overbroad. That task requires us to apply the particularity requirement of Article I, section 9, to the search of the computer's contents. We sketch the particularity requirement as set out in our prior cases, and then discuss that standard as it applies here.</p>
<p id="p-85">A search warrant must "particularly describ[e] the place to be searched, and the person or thing to be seized." Or. Const., Art. I, § 9. Regarding places, the particularity requirement exists to "narrow the scope of the search to those premises for which a magistrate has found probable cause to authorize the search." <em>State v. Trax</em> , <extracted-citation case-ids="175889" index="89" url="https://cite.case.law/or/335/597/#p602"><span class="citation" data-id="835916"><a href="/opinion/835916/state-v-trax/" aria-description="Citation for case: State v. Trax">335 Or. 597</a></span></extracted-citation>, 602, <extracted-citation case-ids="175889" index="90" url="https://cite.case.law/or/335/597/#p602"><span class="citation" data-id="835916"><a href="/opinion/835916/state-v-trax/" aria-description="Citation for case: State v. Trax">75 P.3d 440</a></span></extracted-citation> (2003) (quoting <em>State v. Cortman</em> , <extracted-citation case-ids="2119976" index="91" url="https://cite.case.law/or/251/566/#p569"><span class="citation" data-id="9534296"><a href="/opinion/1129902/state-v-cortman/" aria-description="Citation for case: State v. Cortman">251 Or. 566</a></span></extracted-citation>, 569, <extracted-citation case-ids="2119976" index="92" url="https://cite.case.law/or/251/566/#p569"><span class="citation" data-id="9534296"><a href="/opinion/1129902/state-v-cortman/" aria-description="Citation for case: State v. Cortman">446 P.2d 681</a></span></extracted-citation> (1968), <em>cert. den.</em> , <extracted-citation case-ids="6263938,6262981,6263367,6261870,6262703,6263633,6264241,6261527,6262366,6262143" index="93" url="https://cite.case.law/us/394/951/"><span class="citation multiple-matches"><a href="/c/U.S./394/951/">394 U.S. 951</a></span></extracted-citation>, <extracted-citation index="94" url="https://cite.case.law/citations/?q=89%20S.%20Ct.%201294"><span class="citation no-link">89 S.Ct. 1294</span></extracted-citation>, <extracted-citation index="95" url="https://cite.case.law/citations/?q=22%20L.%20Ed.%202d%20487"><span class="citation no-link">22 L.Ed.2d 487</span></extracted-citation> (1969) ). It is satisfied if the warrant "permits the executing officer 'to locate with reasonable effort the premises to be searched.' " <em>Trax</em> , <extracted-citation case-ids="175889" index="96" url="https://cite.case.law/or/335/597/#p602"><span class="citation" data-id="835916"><a href="/opinion/835916/state-v-trax/" aria-description="Citation for case: State v. Trax">335 Or. at 603</a></span></extracted-citation>, <extracted-citation case-ids="175889" index="97" url="https://cite.case.law/or/335/597/#p602"><span class="citation" data-id="835916"><a href="/opinion/835916/state-v-trax/" aria-description="Citation for case: State v. Trax">75 P.3d 440</a></span></extracted-citation> (quoting <em>Cortman</em> , <extracted-citation case-ids="2119976" index="98" url="https://cite.case.law/or/251/566/#p569"><span class="citation" data-id="9534296"><a href="/opinion/1129902/state-v-cortman/" aria-description="Citation for case: State v. Cortman">251 Or. at 568</a></span>-69</extracted-citation>, <extracted-citation case-ids="2119976" index="99" url="https://cite.case.law/or/251/566/#p569"><span class="citation" data-id="9534296"><a href="/opinion/1129902/state-v-cortman/" aria-description="Citation for case: State v. Cortman">446 P.2d 681</a></span></extracted-citation> ). We have decided fewer cases that address the particularity requirement as it applies to the "thing to be seized." The doctrine in that area is highly fact dependent and eludes a single, concrete articulation. <em>See</em> LaFave, 2 <em>Search and Seizure</em> § 4.6(a) at 769-75 (listing 12 principles as "useful guideposts" in determining if a description of an item meets the Fourth Amendment particularity requirement). But the purposes of the particularity requirement as to things are the same for the requirement of particularity as to places, <em>viz.</em> : The warrant must allow the executing officer to identify with "reasonable effort" the things to be seized "for which a magistrate has found probable cause." <em>Trax</em> , <extracted-citation case-ids="175889" index="100" url="https://cite.case.law/or/335/597/#p602"><span class="citation" data-id="835916"><a href="/opinion/835916/state-v-trax/" aria-description="Citation for case: State v. Trax">335 Or. at 602</a></span>-03</extracted-citation>, <extracted-citation case-ids="175889" index="101" url="https://cite.case.law/or/335/597/#p602"><span class="citation" data-id="835916"><a href="/opinion/835916/state-v-trax/" aria-description="Citation for case: State v. Trax">75 P.3d 440</a></span></extracted-citation>.</p>
<p id="p-86">Our cases have identified two related, but distinct, concepts that inform the particularity analysis-specificity and overbreadth. <em>See</em> <em>Mansor</em> , <extracted-citation case-ids="12167760" index="102" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">279 Or. App. at 792</a></span>-802</extracted-citation>, <extracted-citation case-ids="12167760" index="103" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">381 P.3d 930</a></span></extracted-citation> (discussing and applying specificity and overbreadth concepts). A warrant must be sufficiently specific in describing the items to be seized and examined that the officers can, "with reasonable effort ascertain" those items to a "reasonable degree of certainty."</p>
<p id="p-87"><a class="page-label" data-citation-index="1" data-label="340" href="#p340" id="p340">*340</a><em>Blackburn/Barber</em> , <extracted-citation case-ids="2130981" index="104" url="https://cite.case.law/or/266/28/#p34"><span class="citation" data-id="9551175"><a href="/opinion/1183382/state-v-blackburn/" aria-description="Citation for case: State v. Blackburn">266 Or. at 35</a></span></extracted-citation>, <extracted-citation case-ids="2130981" index="105" url="https://cite.case.law/or/266/28/#p34"><span class="citation" data-id="9551175"><a href="/opinion/1183382/state-v-blackburn/" aria-description="Citation for case: State v. Blackburn">511 P.2d 381</a></span></extracted-citation>. But, even if the warrant is sufficiently specific, it must not authorize a search that is "broader than the supporting affidavit supplies probable cause to justify." <em>State v. Reid</em> , <extracted-citation case-ids="2212256" index="106" url="https://cite.case.law/or/319/65/#p71"><span class="citation" data-id="1189700"><a href="/opinion/1189700/state-v-reid/" aria-description="Citation for case: State v. Reid">319 Or. 65</a></span></extracted-citation>, 71, <extracted-citation case-ids="2212256" index="107" url="https://cite.case.law/or/319/65/#p71"><span class="citation" data-id="1189700"><a href="/opinion/1189700/state-v-reid/" aria-description="Citation for case: State v. Reid">872 P.2d 416</a></span></extracted-citation> (1994).</p>
<p id="p-88">The state argues that a warrant is sufficiently specific and not overbroad-and therefore satisfies the particularity requirement-if the warrant identifies the crime being investigated. It asserts that the warrant here met that requirement because it referred to the crimes under investigation at the time the warrant was issued-criminal mistreatment and assault. Defendant responds that, for purposes of the search of a computer, the particularity requirement means that the warrant must identify (1) "a specific file or type of evidence supported by probable cause," (2) "a specific location on [the] computer," and (3) a specific time period, consistent with the probable cause justifying the warrant-essentially, the "what," the "where," and the "when" of the data or information that police have probable cause to search for on the computer.</p>
<p id="p-89">Turning first to the state's argument that the warrant here was sufficiently particular because it authorized the search of the computer for "evidence of a particular crime," we disagree. The state suggests that we previously held in <em>State v. Farrar</em> , <extracted-citation case-ids="2201284" index="108" url="https://cite.case.law/or/309/132/#p149"><span class="citation" data-id="2611058"><a href="/opinion/2611058/state-v-farrar/" aria-description="Citation for case: State v. Farrar">309 Or. 132</a></span></extracted-citation>, 149-50, <extracted-citation case-ids="2201284" index="109" url="https://cite.case.law/or/309/132/#p149"><span class="citation" data-id="2611058"><a href="/opinion/2611058/state-v-farrar/" aria-description="Citation for case: State v. Farrar">786 P.2d 161</a></span></extracted-citation>, <em>cert. den.</em> , <extracted-citation case-ids="6443011,6442467,6442085,6442790,6442310,6442188,6442573,6442897,6442681" index="110" url="https://cite.case.law/us/498/879/"><span class="citation multiple-matches"><a href="/c/U.S./498/879/">498 U.S. 879</a></span></extracted-citation>, <extracted-citation index="111" url="https://cite.case.law/citations/?q=111%20S.%20Ct.%20212"><span class="citation multiple-matches"><a href="/c/S.Ct./111/212/">111 S.Ct. 212</a></span></extracted-citation>, <extracted-citation index="112" url="https://cite.case.law/citations/?q=112%20L.%20Ed.%202d%20171"><span class="citation multiple-matches"><a href="/c/L.Ed.2d/112/171/">112 L.Ed.2d 171</a></span></extracted-citation> (1990), that a search warrant was sufficiently particular if it referred to the crime under investigation. The warrants there instructed officers to search identified locations for a number of specific items and "any other physical evidence of the aggravated murder of [the victim]." <em>Id.</em> at 149, <extracted-citation case-ids="2201284" index="113" url="https://cite.case.law/or/309/132/#p149"><span class="citation" data-id="2611058"><a href="/opinion/2611058/state-v-farrar/" aria-description="Citation for case: State v. Farrar">786 P.2d 161</a></span></extracted-citation>. We explained that the warrants-and the phrase "any other physical evidence of the aggravated murder" as a description of the scope of the search-were valid because <em>former</em> ORS 133.585 (1973), <em>repealed by</em> Or. Laws 1997, ch. 313, § 37, authorized the seizure of items not specifically described in a warrant. <em><extracted-citation case-ids="2201284" index="114" url="https://cite.case.law/or/309/132/#p149">Id.</extracted-citation></em><extracted-citation case-ids="2201284" index="114" url="https://cite.case.law/or/309/132/#p149"> at 151</extracted-citation>, <extracted-citation case-ids="2201284" index="115" url="https://cite.case.law/or/309/132/#p149"><span class="citation" data-id="2611058"><a href="/opinion/2611058/state-v-farrar/" aria-description="Citation for case: State v. Farrar">786 P.2d 161</a></span></extracted-citation>. The applicable statute allowed officers searching a person or place to seize "things, not specified in the warrant, which the officer has probable cause to believe to be subject to seizure," articulating a version of the "plain view" exception to the warrant requirement.<footnotemark>14</footnotemark> <em><extracted-citation case-ids="2201284" index="116" url="https://cite.case.law/or/309/132/#p149"><span class="citation" data-id="2611058"><a href="/opinion/2611058/state-v-farrar/" aria-description="Citation for case: State v. Farrar">Id.</a></span></extracted-citation></em> (quoting <em>former</em> ORS 133.585(1973) ). That statute applied in the circumstances of that case, the court explained, because the officers knew the instrumentality of the crime and several related items that they were looking for-the murder weapon, stolen jewelry-but did not know if other physical evidence linking the defendant to the crime might be present in the locations they were authorized to search. <em>Id</em> .</p>
<p id="p-90"><em>Farrar</em> thus did not turn on the fact that the warrants at issue there identified a particular crime. Rather, that decision was based on the court's determinations, first, that seizing the numerous specific physical items identified in the warrants (as to which there was probable cause) was permissible, and, second, that seizing other physical items related to the charged crime that officers might find in plain view as they conducted the warranted searches was permissible under the catch-all provision codified in <em>former</em> ORS 133.585 (1990). <em>Farrar</em> was a case-specific application of a statute (later repealed) and essentially upheld a search based on probable cause as described in a detailed affidavit and warrants. This court's statements in <em>Farrar,</em> quoted above, are not a blanket endorsement of nonspecific terms in search warrants and provide no support for the state's proposed rule that merely identifying the crime under investigation provides sufficient particularity to search the entire contents of a lawfully seized computer.</p>
<p id="p-91">Defendant's proposed rules for determining when a search warrant for a computer is sufficiently particular are closer to the mark, although not without their own difficulties, which arise primarily because the particularity requirement developed in a world of physical evidence rather than in the digital context described above. We discuss that context and the Delaware Supreme Court's decision <a class="page-label" data-citation-index="1" data-label="341" href="#p341" id="p341">*341</a>in <em><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/" aria-description="Citation for case: Wheeler v. State">Wheeler</a></span>,</em> and then evaluate defendant's argument that to meet the particularity requirement of Article I, section 9, a warrant to search a computer must identify the "what," the "where," and the "when" of the evidence that police seek.</p>
<p id="p-92">The unique characteristics of computers, outlined above, have implications for the application of the particularity requirement as it applies to computer searches. In the physical world, "different spatial regions are used for different purposes," which allows police and courts to make probable cause determinations "as to where evidence may or may not be found." Orin S. Kerr, <em>Digital Evidence and the New Criminal Procedure</em> , <extracted-citation index="117" url="https://cite.case.law/citations/?q=105%20Colum.%20L.%20Rev.%20279"><span class="citation no-link">105 Colum. L. Rev. 279</span></extracted-citation>, 303 (2005). Inside computers, however, there is "no way to know ahead of time where * * * a particular file or piece of information may be located." <em><extracted-citation index="118" url="https://cite.case.law/citations/?q=105%20Colum.%20L.%20Rev.%20279"><span class="citation no-link">Id.</span></extracted-citation></em> As a result, although the particularity doctrine is an effective means of restraining the state's power to search and can protect against general warrants in the physical world, "the particularity requirement presents difficult challenges in the context of computer searches." <em>Wheeler</em> , <extracted-citation case-ids="6807397" index="119" url="https://cite.case.law/a3d/135/282/"><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/#299" aria-description="Citation for case: Wheeler v. State">135 A.3d at 299</a></span></extracted-citation> (emphasis omitted; capitalization corrected); <em>see also</em> Kerr, 48 Tex. Tech. L. Rev. at 17 (concluding that "particularity alone is unlikely to provide sufficient limits on computer warrant searches").</p>
<p id="p-93">In <em><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/" aria-description="Citation for case: Wheeler v. State">Wheeler</a></span></em> , the Delaware Supreme Court reversed convictions for possession of digital child pornography because the material was found pursuant to an unconstitutionally overbroad warrant. The warrant authorized an unrestricted search of a defendant's computer and other digital equipment as part of an investigation into the defendant's alleged witness tampering. <extracted-citation case-ids="6807397" index="120" url="https://cite.case.law/a3d/135/282/"><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/" aria-description="Citation for case: Wheeler v. State">135 A.3d at 289</a></span></extracted-citation>. The evidence of the witness tampering was suspected to be a kind of "text" file, but the examiner did not use an available feature of the forensic software to limit his view to text-type files. <em><extracted-citation case-ids="6807397" index="121" url="https://cite.case.law/a3d/135/282/"><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/" aria-description="Citation for case: Wheeler v. State">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6807397" index="121" url="https://cite.case.law/a3d/135/282/"> at 290</extracted-citation>. Instead, he viewed all file types and found, but did not open, video files with titles suggesting that they depicted child pornography. Based on those video files, the state obtained another search warrant authorizing the search of digital media already in its possession for evidence of child pornography, leading to the defendant's conviction. <em><extracted-citation case-ids="6807397" index="122" url="https://cite.case.law/a3d/135/282/"><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/" aria-description="Citation for case: Wheeler v. State">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6807397" index="122" url="https://cite.case.law/a3d/135/282/"> at 291</extracted-citation>.</p>
<p id="p-94">In holding that the first warrant was not sufficiently particular, the court stated that the warrant, by purporting to authorize an unlimited examination of the defendant's digital media, paved the way for "unconstitutional exploratory rummaging." <em><extracted-citation case-ids="6807397" index="123" url="https://cite.case.law/a3d/135/282/"><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/" aria-description="Citation for case: Wheeler v. State">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6807397" index="123" url="https://cite.case.law/a3d/135/282/"> at 305</extracted-citation>. Notably, the court did not rest its invalidation of the warrant on the executing officer's failure to exclude nontext video files from the examination-as discussed above, such court-prescribed "search protocols" are, in the majority view, unworkable. Rather, the warrant was unconstitutionally overbroad because it "fail[ed] to limit the search to the relevant time frame." <em><extracted-citation case-ids="6807397" index="124" url="https://cite.case.law/a3d/135/282/"><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/" aria-description="Citation for case: Wheeler v. State">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6807397" index="124" url="https://cite.case.law/a3d/135/282/"> at 304</extracted-citation>. Some federal and state courts have held that a warrant for a computer search is insufficiently particular if it does not include a temporal description of the evidence sought, in cases where relevant time information is available to the police. <em><extracted-citation case-ids="6807397" index="125" url="https://cite.case.law/a3d/135/282/"><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/" aria-description="Citation for case: Wheeler v. State">Id.</a></span></extracted-citation></em> at 304 n. 117, 305 n. 118 (citing cases). In addition, the warrant expressly authorized the seizure and examination of all digital equipment, including video DVDs and digital cameras, despite the absence of any indication that those objects would contain textual evidence of witness tampering. <em><extracted-citation case-ids="6807397" index="126" url="https://cite.case.law/a3d/135/282/"><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/" aria-description="Citation for case: Wheeler v. State">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6807397" index="126" url="https://cite.case.law/a3d/135/282/"> at 306</extracted-citation>. In all, the court declined to "prescribe rigid rules" governing the application of the particularity requirement in computer search contexts; rather, it concluded that a warrant "must describe what investigating officers believe will be found on electronic devices with as much specificity as possible under the circumstances." <em><extracted-citation case-ids="6807397" index="127" url="https://cite.case.law/a3d/135/282/"><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/" aria-description="Citation for case: Wheeler v. State">Id.</a></span></extracted-citation></em><extracted-citation case-ids="6807397" index="127" url="https://cite.case.law/a3d/135/282/"> at 304</extracted-citation>.</p>
<p id="p-95">We return to the components of defendant's proposed rule. Following <em><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/" aria-description="Citation for case: Wheeler v. State">Wheeler</a></span></em> -and, indeed, general principles of search and seizure law-we agree that to satisfy the particularity requirement, a warrant must describe, with as much specificity as reasonably possible under the circumstances, <em>what</em> investigating officers believe will be found on the electronic devices. <em>See <extracted-citation case-ids="6807397" index="128" url="https://cite.case.law/a3d/135/282/"><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/" aria-description="Citation for case: Wheeler v. State">id.</a></span></extracted-citation></em> Defendant clarifies that that element does not necessarily mean the type of computer file, such as an email, text, or photograph. Rather, for the reasons discussed above regarding the nature of digital evidence, the "what" is a description of the <em>information</em> related to the <a class="page-label" data-citation-index="1" data-label="342" href="#p342" id="p342">*342</a>alleged criminal conduct which there is probable cause to believe will be found on the computer. Given the protean variety of factual settings in which such warrants are likely to be sought, it would be a fool's errand to set out, in the abstract, detailed guidelines for determining how specific the "what" of the search must be to meet the particularity requirement of Article I, section 9, in the computer search context, and we decline to do so.</p>
<p id="p-96">Defendant also argues that, to be sufficiently particular, a warrant authorizing a computer search must identify "where" the search may be conducted on the computer. Defendant contends that any search must be limited to "the place or specific location in the computer where the evidence is likely to be found without much effort or rummaging-in this case, defendant's 'internet browsing history.' " Defendant suggests that locations on a computer hard drive are like rooms in a house, and that the warrant must limit the search to specified rooms, such as "internet browsing history, document files, hard drive, emails, call logs, and varying application folders." We disagree.</p>
<p id="p-97">It is certainly true that many warrants authorizing computer searches will identify commonly used software programs-email clients, internet browsers, document management tools-where relevant evidence is likely to be found. For the practical reasons explained above, however, a search warrant may be sufficiently particular without being limited to searching in those "places." Imposing such limits on a computer search would require police and the reviewing magistrate to know the technological specifications, including the configuration of the operating system and applications software on a computer, before a warrant could be obtained. Limiting a search to certain "places" on a computer, defined in terms of the computer's internal organization, such as the "My Documents" folder, is an <em>ex ante</em> limitation on the search. Such <em>ex ante</em> limitations would require a valid warrant to be based on more detailed knowledge of a specific computer and its software than would be required to meet the usual probable cause standard for the information being sought. And defining "places" on a computer in terms of a person's particular use of them, such as "places where a user may store documents," is essentially redundant of the "what" element discussed above. Moreover, information on a computer easily can be moved from one virtual location to another, either intentionally or by mistake. We do not think that it is useful to conceive of a computer as consisting of multiple "rooms" or containers, and a valid warrant to search a computer need not identify "places" to search at that level of abstraction.</p>
<p id="p-98">Defendant also argues that a warrant for a computer search should include a "temporal limitation" or "when" requirement, if one is available and relevant. In <em><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/" aria-description="Citation for case: Wheeler v. State">Wheeler</a></span></em> , the court held that the warrant was unconstitutionally broad because, among other things, it failed to "limit the search to the relevant time frame." <extracted-citation case-ids="6807397" index="129" url="https://cite.case.law/a3d/135/282/"><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/" aria-description="Citation for case: Wheeler v. State">135 A.3d at 304</a></span></extracted-citation>. In reaching that conclusion, the court noted that federal and state courts have concluded that "warrants lacking temporal constraints, where relevant dates are available to the police, are insufficiently particular." <em><extracted-citation case-ids="6807397" index="130" url="https://cite.case.law/a3d/135/282/"><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/" aria-description="Citation for case: Wheeler v. State">Id.</a></span></extracted-citation></em> at 304 n. 117, 305 n. 118 (listing cases). Certainly, consideration of the time when relevant documents were created or internet sites visited can be helpful in ensuring that the warrant describes that which the executing officers may search for with sufficient specificity, but without impermissible overbreadth. And we agree with the reasoning in <em><span class="citation" data-id="3182276"><a href="/opinion/3182294/wheeler-v-state/" aria-description="Citation for case: Wheeler v. State">Wheeler</a></span></em> and the cases cited there that when a time-based description of the information sought on a computer is relevant and available to the police, it ordinarily should be set out in the affidavit, and the warrant should include that description. That said, analytically, "temporal limitations" are more accurately seen as a way of identifying with greater specificity the "what" that is being searched for, rather than as a separate, independently required element, in meeting the particularity requirement for a computer search.</p>
<p id="p-99">We thus agree in substantial part with defendant. The warrant to search a computer must be based on affidavits that establish probable cause to believe that the computer contains information relevant to the criminal investigation. To meet the particularity <a class="page-label" data-citation-index="1" data-label="343" href="#p343" id="p343">*343</a>requirement of Article I, section 9, the warrant must identify, as specifically as reasonably possible in the circumstances, the information to be searched for, including, if relevant and available, the time period during which that information was created, accessed, or otherwise used. We emphasize, however, based on our discussion of digital devices and computer searches above, <em>see</em> 363 Or. at 196-203, 421 P.3d at 331-34, that the forensic examination likely will need to examine, at least briefly, some information or data beyond that identified in the warrant.<footnotemark>15</footnotemark></p>
<p id="p-100">4. <em>Was the warrant here sufficiently particular?</em></p>
<p id="p-101">Returning to the facts of this case, the affidavit established probable cause to believe that child abuse was the cause of B's injuries and probable cause to believe that evidence related to the crime would be found on the computer. When Rookhuyzen interviewed defendant in his apartment, defendant was "completely non-emotive" and had not called his wife, behavior that Rookhuyzen called "highly" and "extremely" unusual. Based on defendant's statements regarding his searches shortly before the 9-1-1 call, there also was probable cause to believe that one or more of the computers at the apartment contained information that would confirm or refute defendant's statements about what happened in the minutes before that call:</p>
<blockquote id="p-102">"[Defendant] told [Rookhuyzen] that he searched the internet between the time he noticed [B] was having difficulty breathing and the time he called emergency dispatch. He told [Rookhuyzen] that he was using a computer to search the internet for advice on what he should do."</blockquote>
<p id="p-103">Additionally, the affidavit recited statements of the pediatrician who examined B that B's injuries were "clearly the result of intentionally inflicted abuse" and that "[defendant's] version of events was not consistent with [B]'s condition"; that B had a brain injury"unrelated to choking"; and that B had a recent skull fracture and bilateral retinal hemorrhages. Finally, the affidavit stated Rookhuyzen's view, based on his training and experience, that computers retain a history of internet use and that examination of a computer needs to be done in a forensic laboratory.</p>
<p id="p-104">The affidavit thus established probable cause to believe that a crime had occurred on June 12 and explained, based on case-specific facts and the officer's training and experience, that there was probable cause to believe that evidence relevant to the investigation would be found on the computer. The affidavit described with particularity certain evidence likely to be found on the computer. Indeed, as the Court of Appeals noted, defendant twice conceded at the suppression hearing "the lawfulness of a search of the computers with respect to the 15 minutes preceding the 9-1-1 call." <em>Mansor</em> , <extracted-citation case-ids="12167760" index="131" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">279 Or. App. at 791</a></span></extracted-citation>, <extracted-citation case-ids="12167760" index="132" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">381 P.3d 930</a></span></extracted-citation>.</p>
<p id="p-105">The warrant, read in conjunction with and limited by the affidavit, met the particularity requirement of Article I, section 9, as we have articulated it above. It sufficiently described the "what" to be searched for and the relevant time frame: The June 12 internet search history. It informed those executing the warrant as to what they were to look for "with a reasonable degree of certainty." <em>Blackburn/ Barber</em> , <extracted-citation case-ids="2130981" index="133" url="https://cite.case.law/or/266/28/#p34"><span class="citation" data-id="9551175"><a href="/opinion/1183382/state-v-blackburn/" aria-description="Citation for case: State v. Blackburn">266 Or. at 35</a></span></extracted-citation>, <extracted-citation case-ids="2130981" index="134" url="https://cite.case.law/or/266/28/#p34"><span class="citation" data-id="9551175"><a href="/opinion/1183382/state-v-blackburn/" aria-description="Citation for case: State v. Blackburn">511 P.2d 381</a></span></extracted-citation>. And, because that description limited the extent of the search that was authorized by the warrant, as we read it, the permitted search was not "broader than the supporting affidavit supplie[d] probable cause to justify." <em>Reid,</em> <extracted-citation case-ids="2212256" index="135" url="https://cite.case.law/or/319/65/#p71"><span class="citation" data-id="1189700"><a href="/opinion/1189700/state-v-reid/" aria-description="Citation for case: State v. Reid">319 Or. at 71</a></span></extracted-citation>, <extracted-citation case-ids="2212256" index="136" url="https://cite.case.law/or/319/65/#p71"><span class="citation" data-id="1189700"><a href="/opinion/1189700/state-v-reid/" aria-description="Citation for case: State v. Reid">872 P.2d 416</a></span></extracted-citation>. For that reason, although we agree with much of the Court of Appeals' learned analysis, we disagree with its legal conclusion that the warrant was overbroad on its face and therefore invalid <em>in toto.</em> In our view, the warrant was not facially invalid because it authorized a search for only the June 12 internet history.</p>
<p id="p-106">V. USE OF RESULTS OF COMPUTER SEARCHES</p>
<p id="p-107">It does not follow, however, that the trial court was correct in denying defendant's <a class="page-label" data-citation-index="1" data-label="344" href="#p344" id="p344">*344</a>motion to suppress the results of the forensic examination in their entirety. As we have discussed, the warrant authorized a search only for the June 12 internet search history. That search was supported by probable cause, was sufficiently specific, and was not overbroad. The nature of a computer search, however, means that, in searching for that history, that the forensic examiners were likely to come across or discover additional information. And, in this case, the forensic examination searched for and uncovered information, later used at trial, that went far beyond the scope of the warrant.</p>
<p id="p-108">To ensure the protection of Article I, section 9, rights, we must consider what restrictions, if any, should be imposed on the use of information police obtain through reasonably executed warranted computer searches when those searches uncover evidence beyond that authorized in the warrant, and when no exception to the warrant requirement supports the collection or use of that evidence.</p>
<p id="p-109">In our view, the privacy interests underlying Article I, section 9, are best protected by recognizing a necessary trade-off when the state searches a computer that has been lawfully seized. Even a reasonable search authorized by a valid warrant necessarily may require examination of at least some information that is beyond the scope of the warrant. Such state searches raise the possibility of computer search warrants becoming the digital equivalent of general warrants and of sanctioning the "undue rummaging that the particularity requirement was enacted to preclude." <em>Mansor,</em> <extracted-citation case-ids="12167760" index="137" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">279 Or. App. at 803</a></span></extracted-citation>, <extracted-citation case-ids="12167760" index="138" url="https://cite.case.law/or-app/279/778/#p801"><span class="citation" data-id="9347796"><a href="/opinion/9352324/state-v-mansor/" aria-description="Citation for case: State v. Mansor">381 P.3d 930</a></span></extracted-citation> (internal quotation marks omitted). Although such searches are lawful and appropriate, individual privacy interests preclude the state from benefiting from that necessity by being permitted to use that evidence at trial. We thus conclude that the state should not be permitted to use information obtained in a computer search if the warrant did not authorize the search for that information, unless some other warrant exception applies. <em>See</em> Kerr, 48 Tex Tech L Rev at 24 (suggesting use restrictions for data "nonresponsive" to the warrant). Put differently, when the state conducts a reasonably targeted search of a person's computer for information pursuant to a warrant that properly identifies the information being sought, the state has not unreasonably invaded the person's privacy interest, and the state may use the information identified in the warrant in a prosecution or any other lawful manner. But when the state looks for other information or uncovers information that was not authorized by the warrant, Article I, section 9, prohibits the state from using that information at trial, unless it comes within an exception to the warrant requirement.</p>
<p id="p-110">That approach is consistent with our explanation that the purpose of rules requiring the suppression of evidence gathered in violation of the constitution is to restore the parties to the position they would have been in had the violation not occurred:</p>
<blockquote id="p-111">"[R]ules of law designed to protect citizens against unauthorized or illegal searches or seizures of their persons, property, or private effects are to be given effect by denying the state the use of evidence secured in violation of those rules against the persons whose rights were violated, or, in effect, by restoring the parties to their position as if the state's officers had remained within the limits of their authority."</blockquote>
<p id="p-112"><em>State v. Davis</em> , <extracted-citation case-ids="2187208" index="139" url="https://cite.case.law/or/295/227/#p237"><span class="citation" data-id="9537056"><a href="/opinion/1142777/state-v-davis/" aria-description="Citation for case: State v. Davis">295 Or. 227</a></span></extracted-citation>, 237, <extracted-citation case-ids="2187208" index="140" url="https://cite.case.law/or/295/227/#p237"><span class="citation" data-id="9537056"><a href="/opinion/1142777/state-v-davis/" aria-description="Citation for case: State v. Davis">666 P.2d 802</a></span></extracted-citation> (1983). Here, the warrant authorized the police to search for specific information on defendant's computer-the June 12 internet search history. The state properly searched for and found that evidence and used it at trial. But the state also searched for and obtained, and used at trial, a substantial amount of evidence from the computer that was not within the scope of the warrant. We have rejected the state's arguments that the warrant authorized the seizure of that additional evidence, and the state has identified no exception to the warrant requirement that supported its acquisition, and use, of that evidence. To restore defendant to the position he would have been in had the police not obtained that additional evidence, the evidence other than the June 12 internet search history should have been suppressed.</p>
<p id="p-113"><a class="page-label" data-citation-index="1" data-label="345" href="#p345" id="p345">*345</a>VI. CONCLUSION</p>
<p id="p-114">In summary: Article I, section 9, prohibits general warrants that give "the bearer an unlimited authority to search and seize." <em>Carter</em> , <extracted-citation case-ids="3561709" index="141" url="https://cite.case.law/or/342/39/#p42"><span class="citation" data-id="835510"><a href="/opinion/835510/state-v-carter/" aria-description="Citation for case: State v. Carter">342 Or. at 43</a></span></extracted-citation>, <extracted-citation case-ids="3561709" index="142" url="https://cite.case.law/or/342/39/#p42"><span class="citation" data-id="835510"><a href="/opinion/835510/state-v-carter/" aria-description="Citation for case: State v. Carter">147 P.3d 1151</a></span></extracted-citation> (quoting <em>Reid</em> , <extracted-citation case-ids="2212256" index="143" url="https://cite.case.law/or/319/65/#p71"><span class="citation" data-id="1189700"><a href="/opinion/1189700/state-v-reid/" aria-description="Citation for case: State v. Reid">319 Or. at 69</a></span></extracted-citation>, <extracted-citation case-ids="2212256" index="144" url="https://cite.case.law/or/319/65/#p71"><span class="citation" data-id="1189700"><a href="/opinion/1189700/state-v-reid/" aria-description="Citation for case: State v. Reid">872 P.2d 416</a></span></extracted-citation> ). Instead, subject to certain exceptions, that provision requires a warrant based on probable cause and describing with particularity that which the state may search for and seize. As the Supreme Court explained in <em><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United

[...TRUNCATED 16294 of 136294 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
