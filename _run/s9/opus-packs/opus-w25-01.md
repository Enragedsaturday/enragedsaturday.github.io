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

## GROUP: _overhaul2/lake/cases/united-states-v-morrison--110372.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "19d00fff15f529e8", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "united-states-v-morrison--110372"}, "payload": {"all": [{"cite": "449 U.S. 361", "page": "361", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "449"}, {"cite": "101 S. Ct. 665", "page": "665", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "101"}, {"cite": "66 L. Ed. 2d 564", "page": "564", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "66"}, {"cite": "1981 U.S. LEXIS 54", "page": "54", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1981"}], "display": null, "official": null, "official_selection_present": false, "record_id": "united-states-v-morrison--110372"}}
{"assertion_id": "17dcb0d8c1595b17", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-morrison--110372"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-morrison--110372", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-morrison--110372

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-morrison--110372",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "United States v. Morrison",
    "case_name_short": "Morrison",
    "case_name_full": "United States v. Morrison",
    "input_case_name": "United States v. Morrison",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1981-02-23",
    "year": 1981,
    "docket": null,
    "cluster_id": 110372,
    "lead_opinion_id": 110372,
    "sibling_ids": [],
    "absolute_url": "/opinion/110372/united-states-v-morrison/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "449 U.S. 361",
        "volume": "449",
        "reporter": "U.S.",
        "page": "361",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 S. Ct. 665",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "665",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "66 L. Ed. 2d 564",
        "volume": "66",
        "reporter": "L. Ed. 2d",
        "page": "564",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1981 U.S. LEXIS 54",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "54",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "449 U.S. 361",
        "volume": "449",
        "reporter": "U.S.",
        "page": "361",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 S. Ct. 665",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "665",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "66 L. Ed. 2d 564",
        "volume": "66",
        "reporter": "L. Ed. 2d",
        "page": "564",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1981 U.S. LEXIS 54",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "54",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "other",
      "selected": null,
      "reason": "unlisted_reporter:U.S."
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
    "date_created": "2026-07-06T13:49:03Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:49:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:49:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:49:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:49:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — united-states-v-morrison--110372

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b560-11">
  Justice White
 </author>
<p id="AvZ">
  delivered the opinion of the Court.
 </p>
<p id="b560-12">
  Hazel Morrison, respondent here, was indicted on two counts of distributing heroin in violation of <span class="citation no-link">21 U. S. C. § 841</span> (a)(1). She retained private counsel to represent her in the impending criminal proceedings. Thereafter, two agents of the Drug Enforcement Agency, aware that she had been indicted and had retained counsel, sought to obtain her cooperation in a related investigation. They met and conversed with her without the knowledge or permission of her counsel. Furthermore, in the course of the conversation, the agents disparaged respondent’s counsel, stating that respondent should think about the type of representation she could expect for the $200 retainer she had paid him and suggesting that she could be better represented by the public defender. In addition, the agents indicated that respondent would gain various benefits if she cooperated but would face a stiff jail term if she did not. Respondent declined to cooperate and immediately notified her attorney. The agents visited respondent again in the absence of counsel, but at no time did respondent agree to cooperate with them, incriminate herself, or supply any in
  <span citation-index="1" class="star-pagination" label="363"> 
   *363
   </span>
  formation pertinent to her case. Contrary to the agents’ advice, respondent continued to rely upon the services of the attorney whom she had retained.
 </p>
<p id="b561-5">
  Respondent subsequently moved to dismiss the indictment with prejudice on the ground that the conduct of the agents had violated her Sixth Amendment right to counsel. The motion contained no allegation that the claimed violation had prejudiced the quality or effectiveness of respondent’s legal representation; nor did it assert that the behavior of the agents had induced her to plead guilty, had resulted in the prosecution having a stronger case against her, or had any other adverse impact on her legal position. The motion was based solely upon the egregious behavior of the agents, which was described as having “interfered” in some unspecified way ■with respondent’s right to counsel. This interference, unaccompanied by any allegation of adverse effect, was urged as a sufficient basis for the requested disposition.
 </p>
<p id="b561-6">
  The District Court denied the motion and respondent, pursuant to a prior agreement with the Government, entered a conditional plea of guilty to one count of the indictment.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  On appeal to the Court of Appeals for the Third Circuit, the judgment of the District Court was reversed. The appellate court concluded that respondent’s Sixth Amendment right to counsel had been violated and that whether or not any tangible effect upon respondent’s representation had been demonstrated or alleged, the appropriate remedy was dismissal of the indictment with prejudice. <span class="citation" data-id="9465932"><a href="/opinion/368285/united-states-v-morrison-hazel/" aria-description="Citation for case: United States v. Morrison, Hazel">602 F. 2d 529</a></span> (1979). We granted the United States’ petition for certiorari to consider whether this extraordinary relief was appropriate in the absence of some adverse consequence to the representation re
  <span citation-index="1" class="star-pagination" label="364"> 
   *364
   </span>
  spondent received or to the fairness of the proceedings leading to her conviction. <span class="citation multiple-matches"><a href="/c/U.%20S./448/906/">448 U. S. 906</a></span>. We reverse.
 </p>
<p id="b562-5">
  The United States initially urges that absent some showing of prejudice, there could be no Sixth Amendment violation to be remedied. Because we agree with the United States, however, that the dismissal of the indictment was error in any event, we shall assume, without deciding, that the Sixth Amendment was violated in the circumstances of this case.
 </p>
<p id="b562-6">
  The Sixth Amendment provides that an accused shall enjoy the right “to have the Assistance of Counsel for his defense.” This right, fundamental to our system of justice, is meant to assure fairness in the adversary criminal process.
  <em>
   Gideon
  </em>
  v.
  <em>
   Wainwright,
  </em>
  <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/#344" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335, 344</a></span> (1963);
  <em>
   Glasser
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="103597"><a href="/opinion/103597/glasser-v-united-states/#69" aria-description="Citation for case: Glasser v. United States">315 U. S. 60, 69-70, 75-76</a></span> (1942);
  <em>
   Johnson
  </em>
  v.
  <em>
   Zerbst,
  </em>
  <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#462" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 462-463</a></span> (1938). Our cases have accordingly been responsive to proved claims that governmental conduct has rendered counsel's assistance to the defendant ineffective.
  <em>
   Moore
  </em>
  v.
  <em>
   Illinois,
  </em>
  <span class="citation" data-id="9427017"><a href="/opinion/109757/moore-v-illinois/" aria-description="Citation for case: Moore v. Illinois">434 U. S. 220</a></span> (1977);
  <em>
   Geders
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9426342"><a href="/opinion/109416/geders-v-united-states/" aria-description="Citation for case: Geders v. United States">425 U. S. 80</a></span> (1976);
  <em>
   Herring
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="9426194"><a href="/opinion/109310/herring-v-new-york/" aria-description="Citation for case: Herring v. New York">422 U. S. 853</a></span> (1975);
  <em>
   Gilbert
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967) ;
  <em>
   United States
  </em>
  v.
  <em>
   Wade,
  </em>
  <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967);
  <em>
   Massiah
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964).
 </p>
<p id="b562-7">
  At the same time and without detracting from the fundamental importance of the right to counsel in criminal cases, we have implicitly recognized the necessity for preserving society’s interest in the administration of criminal justice. Cases involving Sixth Amendment deprivations are subject to the general rule that remedies should be tailored to the injury suffered from the constitutional violation and should not unnecessarily infringe on competing interests. Our relevant cases reflect this approach. In
  <em>
   Gideon
  </em>
  v.
  <em>
   <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">Wainwright, supra,</a></span>
  </em>
  the defendant was totally denied the assistance of counsel at his criminal trial. In
  <em>
   Geders
  </em>
  v.
  <em>
   United States, supra, Herring
  </em>
  v.
  <em>
   New <span class="citation" data-id="9426194"><a href="/opinion/109310/herring-v-new-york/" aria-description="Citation for case: Herring v. New York">York, supra,</a></span>
  </em>
  and
  <em>
   Powell
  </em>
  v.
  <em>
   Alabama,
  </em>
  <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span> (1932), judicial action before or during trial prevented counsel from being fully effective. In
  <em>
   Black
  </em>
  v.
  <em>
   United States,
  </em>
  385
  <span citation-index="1" class="star-pagination" label="365"> 
   *365
   </span>
  U. S. 26 (1966), and
  <em>
   O’Brien
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9423374"><a href="/opinion/107396/obrien-v-united-states/" aria-description="Citation for case: O&#x27;BRIEN v. United States">386 U. S. 345</a></span> (1967), law enforcement officers improperly overheard pretrial conversations between a defendant and his lawyer. None of these deprivations, however, resulted in the dismissal of the indictment. Rather, the conviction in each case was reversed and the Government was free to proceed with a new trial. Similarly, when before trial but after the institution of adversary proceedings, the prosecution has improperly obtained incriminating information from the defendant in the absence of his counsel, the remedy characteristically imposed is not to dismiss the indictment but to suppress the evidence or to order a new trial if the evidence has been wrongfully admitted and the defendant convicted.
  <em>
   Gilbert
  </em>
  v.
  <em>
   <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">California, supra;</a></span> United States
  </em>
  v.
  <em>
   <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade, supra;</a></span> Massiah
  </em>
  v.
  <em>
   United States, supra.
  </em>
  In addition, certain violations of the right to counsel may be disregarded as harmless error. Compare
  <em>
   Moore
  </em>
  v.
  <span class="citation" data-id="9427017"><a href="/opinion/109757/moore-v-illinois/#232" aria-description="Citation for case: Moore v. Illinois"><em>
   Illinois, supra,
  </em>
  at 232</a></span>, with
  <em>
   Chapman
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#23" aria-description="Citation for case: Chapman v. California">386 U. S. 18, 23</a></span>, and n. 8 (1967).
 </p>
<p id="b563-5">
  Our approach has thus been to identify and then neutralize the taint by tailoring relief appropriate in the circumstances to assure the defendant the effective assistance of counsel and a fair trial. The premise of our prior cases is that the constitutional infringement identified has had or threatens some adverse effect upon the effectiveness of counsel’s representation or has produced some other prejudice to the defense. Absent such impact on the criminal proceeding, however, there is no basis for imposing a remedy in that proceeding, which can go forward with full recognition of the defendant’s right to counsel and to a fair trial.
 </p>
<p id="b563-6">
  More particularly, absent demonstrable prejudice, or substantial threat thereof, dismissal of the indictment is plainly inappropriate, even though the violation may have been deliberate.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  This has been the result reached where a Fifth
  <span citation-index="1" class="star-pagination" label="366"> 
   *366
   </span>
  Amendment violation has occurred,
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  and we have not suggested that searches and seizures contrary to the Fourth Amendment warrant dismissal of the indictment. The remedy in the criminal proceeding is limited to denying the prosecution the fruits of its transgression.
 </p>
<p id="b564-5">
  Here, respondent has demonstrated no prejudice of any kind, either transitory or permanent, to the ability of her counsel to provide adequate representation in these criminal proceedings. There is no effect of a constitutional dimension which needs to be purged to make certain that respondent has been effectively represented and not unfairly convicted. The Sixth Amendment violation, if any, accordingly provides no justification for interfering with the criminal proceedings against
  <span citation-index="1" class="star-pagination" label="367"> 
   *367
   </span>
  respondent Morrison, much less the drastic relief granted by the Court of Appeals.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
</p>
<p id="b565-5">
  In arriving at this conclusion, we do not condone the egregious behavior of the Government agents. Nor do we suggest that in cases such as this, a Sixth Amendment violation may not be remedied in other proceedings. We simply conclude that the solution provided by the Court of Appeals is inappropriate where the violation, which we assume has occurred, has had no adverse impact upon the criminal proceedings.
 </p>
<p id="b565-6">
  The judgment of the Court of Appeals is accordingly reversed, and the case is remanded for proceedings consistent with this opinion.
 </p>
<p id="b565-7">
<em>
   So ordered.
  </em>
</p>




<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b561-7">
   A second count was dismissed as required by the plea agreement. The plea was conditioned on respondent’s right to appeal the District Court’s denial of the motion to dismiss. The Third Circuit has approved this procedure.
   <em>
    United States
   </em>
   v.
   <em>
    Moskow, 588
   </em>
   F. 2d 882 (1978);
   <em>
    United States
   </em>
   v.
   <em>
    Zudick,
   </em>
   <span class="citation" data-id="330342"><a href="/opinion/330342/united-states-v-morris-zudick-and-pauline-zudick/" aria-description="Citation for case: United States v. Morris Zudick, and Pauline Zudick">523 F. 2d 848</a></span> (1975). We express no view on the propriety of such conditional pleas.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b563-7">
   There is no claim here that there was continuing prejudice which, because it could not be remedied by a new trial or suppression of evidence,
   <span citation-index="1" class="star-pagination" label="366"> 
    *366
    </span>
   called for more drastic treatment. Cf.
   <em>
    United States
   </em>
   v.
   <em>
    Marion,
   </em>
   <span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#325" aria-description="Citation for case: United States v. Marion">404 U. S. 307, 325-326</a></span> (1971). Indeed, there being no claim of any discernible taint, even the traditional remedies were beside the point. The Court of Appeals seemed to reason that because there was no injury claimed and because other remedies would not be fruitful, dismissal of the indictment was appropriate. But as the dissent below indicated, it is odd to reserve the most drastic remedy for those situations where there has been no discernible injury or other impact.
  </p>
<p id="b564-7">
   The Court of Appeals also thought dismissal was appropriate to deter deliberate infringements of the right to counsel. But this proves too much, for it would warrant dismissal, not just in this case, but in any case where there has been a knowing violation. Furthermore, we note that the record before us does not reveal a pattern of recurring violations by investigative officers that might warrant the imposition of a more extreme remedy in order to deter further lawlessness.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b564-8">
   This is clear from
   <em>
    United States
   </em>
   v.
   <em>
    Blue,
   </em>
   <span class="citation" data-id="107238"><a href="/opinion/107238/united-states-v-blue/#255" aria-description="Citation for case: United States v. Blue">384 U. S.
   <em>
    251, 255
   </em></a></span>
   (1966):
  </p>
<blockquote id="b564-9">
   “Even if we assume that the Government did acquire incriminating evidence in violation of the Fifth Amendment, Blue would at most be entitled to suppress the evidence and its fruits if they were sought to be used against him at trial. . . . Our numerous precedents ordering the exclusion of such illegally obtained evidence assume implicitly that the remedy does not extend to barring the prosecution altogether. So drastic a step might advance marginally some of the ends served by exclusionary rules, but it would also increase to an intolerable degree interference with the public interest in having the guilty brought to book.” (Footnote omitted.)
  </blockquote>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b565-8">
   The position we have adopted finds substantial support in the Courts of Appeals.
   <em>
    United States
   </em>
   v.
   <em>
    Jimenez,
   </em>
   <span class="citation" data-id="380373"><a href="/opinion/380373/united-states-v-jane-nadia-jimenez/#41" aria-description="Citation for case: United States v. Jane Nadia Jimenez">626 F. 2d 39, 41-42</a></span> (CA7 1980);
   <em>
    United States
   </em>
   v.
   <em>
    Artuso,
   </em>
   <span class="citation" data-id="376667"><a href="/opinion/376667/united-states-v-vincent-artuso-united-states-of-america-v-bradford-wedra/#196" aria-description="Citation for case: United States v. Vincent Artuso, United States of America...">618 F. 2d 192, 196-197</a></span> (CA2 1980);
   <em>
    United States
   </em>
   v.
   <em>
    Glover,
   </em>
   <span class="citation" data-id="365595"><a href="/opinion/365595/united-states-v-robert-andrew-glover-united-states-of-america-v-marvin/#861" aria-description="Citation for case: United States v. Robert Andrew Glover, United States of...">596 F. 2d 857, 861-864</a></span> (CA9 1979);
   <em>
    United States
   </em>
   v.
   <em>
    Crow Dog,
   </em>
   <span class="citation" data-id="9462608"><a href="/opinion/334526/united-states-v-leonard-crow-dog/#1196" aria-description="Citation for case: United States v. Leonard Crow Dog">532 F. 2d 1182, 1196-1197</a></span> (CA8 1976);
   <em>
    United States
   </em>
   v. Acosta, <span class="citation" data-id="8897995"><a href="/opinion/8910321/united-states-v-acosta/#674" aria-description="Citation for case: United States v. Acosta">526 F. 2d 670, 674</a></span> (CA5
   <em>
    1976);
   </em>
   but see
   <em>
    United States
   </em>
   v.
   <em>
    McCord,
   </em>
   166 U. S. App. D. C. 1, 15-18, <span class="citation" data-id="9461375"><a href="/opinion/324542/united-states-v-james-w-mccord-jr-aka-edward-j-warren-aka-edward/#348" aria-description="Citation for case: United States v. James W. McCord Jr., A/K/A Edward J....">509 F. 2d 334, 348-351</a></span> (1974) (en banc) (dicta). The Supreme Judicial Court of Massachusetts has adopted a contrary view. See
   <em>
    Commonwealth
   </em>
   v.
   <em>
    Manning,
   </em>
   <span class="citation" data-id="2056759"><a href="/opinion/2056759/commonwealth-v-manning/" aria-description="Citation for case: Commonwealth v. Manning">373 Mass. 438</a></span>, <span class="citation" data-id="2056759"><a href="/opinion/2056759/commonwealth-v-manning/" aria-description="Citation for case: Commonwealth v. Manning">367 N. E. 2d 635</a></span> (1977).
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/united-states-v-new-york-telephone-co--109755.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6ee747cbf602792b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "united-states-v-new-york-telephone-co--109755"}, "payload": {"all": [{"cite": "434 U.S. 159", "page": "159", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "434"}, {"cite": "98 S. Ct. 364", "page": "364", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "98"}, {"cite": "54 L. Ed. 2d 376", "page": "376", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "54"}, {"cite": "1977 U.S. LEXIS 161", "page": "161", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1977"}], "display": null, "official": null, "official_selection_present": false, "record_id": "united-states-v-new-york-telephone-co--109755"}}
{"assertion_id": "339a1262914ec3d7", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-new-york-telephone-co--109755"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-new-york-telephone-co--109755", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-new-york-telephone-co--109755

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-new-york-telephone-co--109755",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "United States v. New York Telephone Co.",
    "case_name_short": "",
    "case_name_full": "United States v. New York Telephone Co.",
    "input_case_name": "United States v. New York Telephone Co.",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-12-07",
    "year": 1977,
    "docket": "No. 76-835",
    "cluster_id": 109755,
    "lead_opinion_id": 9427010,
    "sibling_ids": [],
    "absolute_url": "/opinion/109755/united-states-v-new-york-telephone-co/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "434 U.S. 159",
        "volume": "434",
        "reporter": "U.S.",
        "page": "159",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 S. Ct. 364",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "364",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 L. Ed. 2d 376",
        "volume": "54",
        "reporter": "L. Ed. 2d",
        "page": "376",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 161",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "161",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "434 U.S. 159",
        "volume": "434",
        "reporter": "U.S.",
        "page": "159",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 S. Ct. 364",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "364",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 L. Ed. 2d 376",
        "volume": "54",
        "reporter": "L. Ed. 2d",
        "page": "376",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 161",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "161",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "other",
      "selected": null,
      "reason": "unlisted_reporter:U.S."
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
    "date_created": "2026-07-06T13:53:57Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:54:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:54:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:54:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:54:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — united-states-v-new-york-telephone-co--109755

```
<opinion type="majority">
<author id="b333-7">Mr. Justice White</author>
<p id="AEi">delivered the opinion of the Court.</p>
<p id="b333-8">This case presents the question of whether a United States District Court may properly direct a telephone company to provide federal law enforcement officials the facilities and technical assistance necessary for the implementation of its order authorizing the use of pen registers<footnotemark>1</footnotemark> to investigate offenses which there was probable cause to believe were being committed by means of the telephone.</p>
<p id="b333-9">I</p>
<p id="b333-10">On March 19, 1976, the United States District Court for the Southern District of New York issued an order authorizing agents of the Federal Bureau of Investigation (FBI) to install and use pen registers with respect to two telephones and directing the New York Telephone Co. (Company) to furnish the FBI “all information, facilities and technical assistance” necessary to employ the pen registers unobtrusively. The FBI was ordered to compensate the Company at prevailing rates for any assistance which it furnished. App. 6-7. The order was issued on the basis of an affidavit sub<page-number citation-index="1" label="162">*162</page-number>mitted by an FBI agent which stated that certain individuals were conducting an illegal gambling enterprise at 220 East I4th Street in New York City and that, on the basis of facts set forth therein, there was probable cause to believe that two telephones bearing different numbers were being used at that address in furtherance of the illegal activity. <em>Id., </em>at 1-5. The District Court found that there was probable cause to conclude that an illegal gambling enterprise using the facilities of interstate commerce was being conducted at the East 14th Street address in violation of 18 U. S. C. §§ .371 and 1952, and that the two telephones had been, were currently being, and would continue to be used in connection with those offenses. Its order authorized the FBI to operate the pen registers with respect to the two telephones until knowledge of the numbers dialed led to the identity of the associates and confederates of those believed to be conducting the illegal operation or for 20 days, “whichever is earlier.”</p>
<p id="b334-5">The Company declined to comply fully with the court order. It did inform the FBI of the location of the relevant “appearances,” that is, the places where specific telephone lines emerge from the sealed telephone cable. In addition, the Company agreed to identify the relevant “pairs,” or the specific pairs of wires that constituted the circuits of the two telephone lines. This information is required to install a pen register. The Company, however, refused to lease lines to the FBI which were needed to install the pen registers in an unobtrusive fashion. Such lines were required by the FBI in order to install the pen registers in inconspicuous locations away from the building containing the telephones. A “leased line” is an unused telephone line which makes an “appearance” in the same terminal box as the telephone line in connection with which it is desired to install a pen register. If the leased line is connected to the subject telephone line, the pen register can then be installed on the leased line at a remote location and be monitored from that point. The <page-number citation-index="1" label="163">*163</page-number>Company, instead of providing the leased lines, which it conceded that the court’s order required it to do, advised the FBI to string cables from the “subject apartment” to another location where pen registers could be installed. The FBI determined after canvassing the neighborhood of the apartment for four days that there was no location where it could string its own wires and attach the pen registers without alerting the suspects,<footnotemark>2</footnotemark> in which event, of course, the gambling operation would cease to function. App. 15-22.</p>
<p id="b335-5">On March 30, 1976, the Company moved in the District Court to vacate that portion of the pen register order directing it to furnish facilities and technical assistance to the FBI in connection with the use of the pen registers on the ground that such a directive could be issued only in connection with a wiretap order conforming to the requirements of Title III of the Omnibus Crime Control and Safe Streets Act of 1968, <span class="citation no-link">18 U. S. C. §§2510-2520</span> (1970 ed. and Supp. V). It contended that neither Fed. Rule Crim. Proc. 41 nor the All Writs Act, <span class="citation no-link">28 U. S. C. § 1651</span> (a), provided any basis for such an order. App. 10-14. The District Court ruled that pen registers are not governed by the proscriptions of Title III because they are not devices used to intercept oral communications. It concluded that it had jurisdiction to authorize the installation of the pen registers upon a showing of probable cause and that both the All Writs Act and its inherent powers provided authority for the order directing the Company to assist in the installation of the pen registers.</p>
<p id="b335-6">On April 9, 1976, after the District Court and the Court of Appeals denied the Company’s motion to stay the pen register order pending appeal, the Company provided the leased lines.<footnotemark>3</footnotemark></p>
<p id="b336-4"><page-number citation-index="1" label="164">*164</page-number>The Court of Appeals affirmed in part and reversed in part, with one judge dissenting on the ground that the order below should have been affirmed in its entirety. <em>Application of United States in re Pen Register Order, </em><span class="citation" data-id="9462905"><a href="/opinion/337714/application-of-the-united-states-of-america-in-the-matter-of-an-order/" aria-description="Citation for case: Application of the United States of America in the Matter...">538 F. 2d 956</a></span> (CA2 1976). It agreed with the District Court that pen registers do not fall within the scope of Title III and are not otherwise prohibited or regulated by statute. The Court of Appeals also concluded that district courts have the power, either inherently or as a logical derivative of Fed. Crim. Proc. 41, to authorize pen register surveillance upon an adequate showing of probable cause. The majority held, however, that the District Court abused its discretion in ordering the Company to assist in the installation and operation of the pen registers. It assumed, <em>arguendo, </em>that “a district court has inherent discretionary authority or discretionary power under the All Writs Act to compel technical assistance by the Telephone Company,” but concluded that “in the absence of specific and properly limited Congressional action, it was an abuse of discretion for the District Court to order the Telephone Company to furnish technical assistance.” <span class="citation" data-id="9462905"><a href="/opinion/337714/application-of-the-united-states-of-america-in-the-matter-of-an-order/#961" aria-description="Citation for case: Application of the United States of America in the Matter...">538 F. 2d, at 961</a></span>.<footnotemark>4</footnotemark> The majority expressed concern that “such an order could establish a most undesirable, if not dangerous and unwise, precedent for the authority of federal courts to impress unwilling aid on private third parties” and that “there is no assurance that the court will always be able to protect '[third parties] from excessive or overzealous Government activity or compulsion.” <span class="citation" data-id="9462905"><a href="/opinion/337714/application-of-the-united-states-of-america-in-the-matter-of-an-order/#962" aria-description="Citation for case: Application of the United States of America in the Matter..."><em>Id., </em>at 962-963</a></span>.<footnotemark>5</footnotemark></p>
<p id="b337-4"><page-number citation-index="1" label="165">*165</page-number>We granted the United States’ petition for certiorari challenging the Court of Appeals’ invalidation of the District Court’s order against respondent.<footnotemark>6</footnotemark> <span class="citation multiple-matches"><a href="/c/U.%20S./429/1072/">429 U. S. 1072</a></span>.</p>
<p id="b337-5">II</p>
<p id="b337-6">We first reject respondent’s contention, which is renewed here, that the District Court lacked authority to order the Company to provide assistance because the use of pen registers may be authorized only in conformity with the procedures set forth in Title III<footnotemark>7</footnotemark> for securing judicial authority to inter<page-number citation-index="1" label="166">*166</page-number>cept wire communications.<footnotemark>8</footnotemark> Both the language of the statute and its legislative history establish beyond any doubt that pen registers are not governed by Title III.<footnotemark>9</footnotemark></p>
<p id="b338-5">Title III is concerned only with orders “authorizing or approving the <em>interception </em>of a wire or oral communication . . . .” <span class="citation no-link">18 U. S. C. §2518</span>(1) (emphasis added).<footnotemark>10</footnotemark> Congress defined “intercept” to mean “the <em>aural </em>acquisition of the <em>contents </em>of any wire or oral <em>communication </em>through the use of any electronic, mechanical, or other device.” <span class="citation no-link">18 U. S. C. <page-number citation-index="1" label="167">*167</page-number>§ 2510</span> (4) (emphasis added). Pen registers do not “intercept” because they do not acquire the “contents” of communications, as that term is defined by <span class="citation no-link">18 U. S. C. § 2510</span> (8).<footnotemark>11</footnotemark> Indeed, a law enforcement official could not even determine from the use of a pen register whether a communication existed. These devices do not hear sound. They disclose only the telephone numbers that have been dialed — a means of establishing communication. Neither the purport of any communication between the caller and the recipient of the call, their identities, nor whether the call was even completed is disclosed by pen registers. Furthermore, pen registers do not accomplish the “aural acquisition” of anything. They decode outgoing telephone numbers by responding to changes in electrical voltage caused by the turning of the telephone dial (or the pressing of buttons on pushbutton telephones) and present the information in a form to be interpreted by sight rather than by hearing.<footnotemark>12</footnotemark></p>
<p id="b339-5">The legislative history confirms that there was no congressional intent to subject pen registers to the requirements of Title III. The Senate Report explained that the definition of “intercept” was designed to exclude pen registers:</p>
<blockquote id="b339-6">“Paragraph 4 [of § 2510] defines 'intercept’ to include the aural acquisition of the contents of any wire or oral communication by any electronic, mechanical, or other device. Other forms of surveillance are not within the proposed legislation. . . . The proposed legislation is not designed to prevent'the tracing of phone calls. The use of a 'pen register/ for example, would be permissible. But see <em>United States </em>v. <em>Dote, </em><span class="citation" data-id="274344"><a href="/opinion/274344/united-states-v-rocco-dote-and-theodore-p-veesart-united-states-of/" aria-description="Citation for case: United States v. Rocco Dote and Theodore P. Veesart,...">371 F. 2d 176</a></span> (7th 1966). The proposed legislation is intended to protect the privacy of the communication itself and not the means of <page-number citation-index="1" label="168">*168</page-number>communication.” S. Rep. No. 1097, 90th Cong., 2d Sess., 90 (1968).<footnotemark>13</footnotemark></blockquote>
<p id="b340-5">It is clear that Congress did not view pen registers as posing a threat to privacy of the same dimension as the interception of oral communications and did not intend to impose Title III restrictions upon their use.</p>
<p id="b340-6">Ill</p>
<p id="b340-7">We also agree with the Court of Appeals that the District Court had power to authorize the installation of the pen registers.<footnotemark>14</footnotemark> It is undisputed that the order in this case was predicated upon a proper finding of probable cause, and no claim is made that it was in any way inconsistent with the <page-number citation-index="1" label="169">*169</page-number>Fourth Amendment. Federal Rule Crim. Proc. 41 (b) authorizes the issuance of a warrant to:</p>
<blockquote id="b341-5">“search for and seize any (1) property that constitutes evidence of the commission of a criminal offense; or (2) contraband, the fruits of crime, or things otherwise criminally possessed; or (3) property designed or intended for use or which is or has been used as the means of committing a criminal offense.”</blockquote>
<p id="b341-6">This authorization is broad enough to encompass a “search” designed to ascertain the use which is being made of a telephone suspected of being employed as a means of facilitating a criminal venture and the “seizure” of evidence which the “search” of the telephone produces. Although Rule 41 (h) defines property “to include documents, books, papers and any other tangible objects,” it does not restrict or purport to exhaustively enumerate all the items which may be seized pursuant to Rule 41.<footnotemark>15</footnotemark> Indeed, we recognized in <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), which held that telephone conversations were protected by the Fourth Amendment, that Rule 41 is not limited to tangible items but is sufficiently flexible to include within its scope electronic intrusions authorized upon a finding of probable cause. <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#354" aria-description="Citation for case: Katz v. United States">389 U. S., at 354-356</a></span>, and n. 16.<footnotemark>16</footnotemark> See also <em>Osborn </em>v. <em>United States, </em><span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/#329" aria-description="Citation for case: Osborn v. United States">385 U. S. 323, 329-331</a></span> (1966).</p>
<p id="b342-4"><page-number citation-index="1" label="170">*170</page-number>Our conclusion that Rule 41 authorizes the use of pen registers under appropriate circumstances is supported by Fed. Rule Crim. Proc. 57 (b), which provides: “If no procedure is specifically prescribed by rule, the court may proceed in any lawful manner not inconsistent with these rules or with any applicable statute.” <footnotemark>17</footnotemark> Although we need not and do not decide whether Rule 57 (b) by itself would authorize the issuance of pen register orders, it reinforces our conclusion that Rule 41 is sufficiently broad to include seizures of intangible items such as dial impulses recorded by pen registers as well as tangible items.</p>
<p id="b342-5">Finally, we could not hold that the District Court lacked any power to authorize the use of pen registers without defying the congressional judgment that the use of pen registers “be permissible.” S. Rep. No. 1097, <em>supra, </em>at 90. Indeed, it would be anomalous to permit the recording of conversations by means of electronic surveillance while prohibiting the far lesser intrusion accomplished by pen registers. Congress intended no such result. We are unwilling to impose it in the absence of some showing that the issuance of such orders would be inconsistent with Rule 41. Cf. Rule 57 (b), <em>supra.</em><footnotemark><em>18</em></footnotemark></p>
<p id="b343-4"><page-number citation-index="1" label="171">*171</page-number>IV</p>
<p id="b343-5">The Court of Appeals held that even though the District Court had ample authority to issue the pen register warrant and even assuming the applicability of the All Writs Act, the order compelling the Company to provide technical assistance constituted an abuse of discretion. Since the Court of Appeals conceded that a compelling case existed for requiring the assistance of the Company and did not point to any fact particular to this case which would warrant a finding of abuse of discretion, we interpret its holding as generally barring district courts from ordering any party to assist in the installation or operation of a pen register. It was apparently concerned that sustaining the District Court's order would authorize courts to compel third parties to render assistance without limitation regardless of the burden involved and pose a severe threat to the autonomy of third parties who for whatever reason prefer not to render such assistance. Consequently the Court of Appeals concluded that courts should not <page-number citation-index="1" label="172">*172</page-number>embark upon such a course without specific legislative authorization. We agree that the power of federal courts to impose duties upon third parties is not without limits; unreasonable burdens may not be imposed. We conclude, however, that the order issued here against respondent was clearly authorized by the All Writs Act and was consistent with the intent of Congress.<footnotemark>19</footnotemark></p>
<p id="AIZ">The All Writs Act provides:</p>
<blockquote id="b344-6">“The Supreme Court and all courts established by Act of Congress may issue all writs necessary or appropriate in aid of their respective jurisdictions and agreeable to the usages and principles of law.” <span class="citation no-link">28 U. S. C. § 1651</span> (a).</blockquote>
<p id="b344-7">The assistance of the Company was required here to implement a pen register order which we have held the District Court was empowered to issue by Rule 41. This Court has repeatedly recognized the power of a federal court to issue such commands under the All Writs Act as may be necessary or appropriate to effectuate and prevent the frustration of orders it has previously issued in its exercise of jurisdiction otherwise obtained: “This statute has served since its inclusion, in substance, in the original Judiciary Act as a ‘legislatively approved source of procedural instruments designed to achieve “the rational ends of law.” ’ ” <em>Harris </em>v. <em>Nelson, </em><span class="citation" data-id="9423958"><a href="/opinion/107877/harris-v-nelson/#299" aria-description="Citation for case: Harris v. Nelson">394 U. S. 286, 299</a></span> (1969), quoting <em>Price </em>v. <em>Johnston, </em><span class="citation" data-id="9420168"><a href="/opinion/104557/price-v-johnston/#282" aria-description="Citation for case: Price v. Johnston">334 U. S. 266, 282</a></span> (1948). Indeed, “[ujnless appropriately confined by <page-number citation-index="1" label="173">*173</page-number>Congress, a federal court may avail itself of all auxiliary writs as aids in the performance of its duties, when the use of such historic aids is calculated in its sound judgment to achieve the ends of justice entrusted to it.” <em>Adams </em>v. <em>United States ex rel. McCann, </em><span class="citation" data-id="9419274"><a href="/opinion/103735/adams-v-united-states-ex-rel-mccann/#273" aria-description="Citation for case: Adams v. United States Ex Rel. McCann">317 U. S. 269, 273</a></span> (1942).</p>
<p id="b345-4">The Court has consistently applied the Act .flexibly in conformity with these principles. Although § 262 of the Judicial Code, the predecessor to § 1651, did not expressly authorize courts, as does § 1651, to issue writs “appropriate” to the proper exercise of their jurisdiction but only “necessary” writs, <em><span class="citation" data-id="9419274"><a href="/opinion/103735/adams-v-united-states-ex-rel-mccann/" aria-description="Citation for case: Adams v. United States Ex Rel. McCann">Adams</a></span> </em>held that these supplemental powers are not limited to those situations where it is “necessary” to issue the writ or order “in the sense that the court could not otherwise physically discharge its appellate duties.” <span class="citation" data-id="9419274"><a href="/opinion/103735/adams-v-united-states-ex-rel-mccann/#273" aria-description="Citation for case: Adams v. United States Ex Rel. McCann">317 U. S., at 273</a></span>. In <em>Price </em>v. <em><span class="citation" data-id="9420168"><a href="/opinion/104557/price-v-johnston/" aria-description="Citation for case: Price v. Johnston">Johnston, supra,</a></span> </em>§ 262 supplied the authority for a United States Court of Appeals to issue an order commanding that a prisoner be brought before the court for the purpose of arguing his own appeal. Similarly, in order to avoid frustrating the “very purpose” of <span class="citation no-link">28 U. S. C. § 2255</span>, § 1651 furnished the District Court with authority to order that a federal prisoner be produced in court for purposes of a hearing. <em>United States </em>v. <em>Hayman, </em><span class="citation" data-id="104948"><a href="/opinion/104948/united-states-v-hayman/#220" aria-description="Citation for case: United States v. Hayman">342 U. S. 205, 220-222</a></span> (1952). The question in <em>Harris </em>v. <em><span class="citation" data-id="9423958"><a href="/opinion/107877/harris-v-nelson/" aria-description="Citation for case: Harris v. Nelson">Nelson, supra,</a></span> </em>was whether, despite the absence of specific statutory authority, the District Court could issue a discovery order in connection with a habeas corpus proceeding pending before it. Eight Justices agreed that the district courts have power to require discovery when essential to render a habeas corpus proceeding effective. The Court has also held that despite the absence of express statutory authority to do so, the Federal Trade Commission may petition for, and a Court of Appeals may issue, pursuant to § 1651, an order preventing a merger pending hearings before the Commission to avoid impairing or frustrating the Court of Appeals’ appellate jurisdiction. <em>FTC </em>v. <em>Dean Foods Co., </em><span class="citation" data-id="9423244"><a href="/opinion/107255/federal-trade-commission-v-dean-foods-co/" aria-description="Citation for case: Federal Trade Commission v. Dean Foods Co.">384 U. S. 597</a></span> (1966).</p>
<p id="b346-4"><page-number citation-index="1" label="174">*174</page-number>The power conferred by the Act extends, under appropriate circumstances, to persons who, though not parties to the original action or engaged in wrongdoing, are in a position to frustrate the implementation of a court order or the proper administration of justice, <em>Mississippi Valley Barge Line Co. </em>v. <em>United </em>States, <span class="citation" data-id="2248513"><a href="/opinion/2248513/mississippi-valley-barge-line-company-v-united-states/#6" aria-description="Citation for case: Mississippi Valley Barge Line Company v. United States">273 F. Supp. 1, 6</a></span> (ED Mo. 1967), summarily aff’d, <span class="citation" data-id="107581"><a href="/opinion/107581/osbourne-v-mississippi-valley-barge-line-co/" aria-description="Citation for case: Osbourne v. Mississippi Valley Barge Line Co.">389 U. S. 579</a></span> (1968); <em>Board of Education </em>v. <em>York, </em><span class="citation" data-id="291169"><a href="/opinion/291169/board-of-education-of-independent-school-district-89-oklahoma-county-v/" aria-description="Citation for case: Board of Education of Independent School District 89,...">429 F. 2d 66</a></span> (CA10 1970), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./401/954/">401 U. S. 954</a></span> (1971), and encompasses even those who have not taken any affirmative action to hinder justice. <em>United States </em>v. <em>McHie, </em><span class="citation" data-id="8783372"><a href="/opinion/8799251/united-states-v-mchie/" aria-description="Citation for case: United States v. McHie">196 F. 586</a></span> (ND Ill. 1912); <em>Field </em>v. <em>United States, </em><span class="citation" data-id="9443042"><a href="/opinion/228335/united-states-v-field/#95" aria-description="Citation for case: United States v. Field">193 F. 2d 92, 95-96</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./342/894/">342 U. S. 894</a></span> (1951).<footnotemark>20</footnotemark></p>
<p id="b346-5">Turning to the facts of this case, we do not think that the Company was a third party so far removed from the underlying controversy that its assistance could not be permissibly compelled. A United States District Court found that there was probable cause to believe that the Company’s facilities were being employed to facilitate a criminal enterprise on a continuing basis. For the Company, with this knowledge, to refuse to supply the meager assistance required by the FBI in its efforts to put an end to this venture threatened obstruction of an investigation which would determine whether the Company’s facilities were being lawfully used. Moreover, it can hardly be contended that the Company, a highly regulated public utility with a duty to serve the public,<footnotemark>21</footnotemark> had a substantial interest in not providing assistance. Certainly the use of pen registers is by no means offensive to it. The Company concedes that it regularly employs such devices without court order for the purposes of checking billing operations, detecting fraud, and <page-number citation-index="1" label="175">*175</page-number>preventing violations of law.<footnotemark>22</footnotemark> It also agreed to supply the FBI with all the information required to install its own pen registers. Nor was the District Court’s order in any way burdensome. The order provided that the Company be fully reimbursed at prevailing rates, and compliance with it required minimal effort on the part of the Company and no disruption to its operations.</p>
<p id="b347-4">Finally, we note, as the Court of Appeals recognized, that without the Company’s assistance there is no conceivable way in which the surveillance authorized by the District Court could have been successfully accomplished.<footnotemark>23</footnotemark> The FBI, after an exhaustive search, was unable to find a location where it could install its own pen registers without tipping off the targets of the investigation. The provision of a leased line by the Company was essential to the fulfillment of the purpose— to learn the identities of those connected with the gambling operation — for which the pen register order had been issued.<footnotemark>24</footnotemark></p>
<p id="b348-4"><page-number citation-index="1" label="176">*176</page-number>The order compelling the Company to provide assistance was not only consistent with the Act but also with more recent congressional actions. As established in Part II, <em>supra, </em>Congress clearly intended to permit the use of pen registers by federal law enforcement officials. Without the assistance of the Company in circumstances such as those presented here, however, these devices simply cannot be effectively employed. Moreover, Congress provided in a 1970 amendment to Title III that “fa]n order authorizing the interception of a wire or oral communication shall, upon request of the applicant, direct that a communication common carrier . . . shall furnish the applicant forthwith all information, facilities, and technical assistance necessary to accomplish the interception unobtrusively . . . .” <span class="citation no-link">18 U. S. C. § 2518</span> (4). In light of this direct <page-number citation-index="1" label="177">*177</page-number>command to federal courts to compel, upon request, any assistance necessary to accomplish an electronic interception, it would be remarkable if Congress thought it beyond the power of the federal courts to exercise, where required, a discretionary authority to order telephone companies to assist in the installation and operation of pen registers, which accomplish a far lesser invasion of privacy.<footnotemark>25</footnotemark> We are convinced that <page-number citation-index="1" label="178">*178</page-number>to prohibit the order challenged here would frustrate the clear indication by Congress that the pen register is a permissible law enforcement tool by enabling a public utility to thwart a judicial determination that its use is required to apprehend and prosecute successfully those employing the utility’s facilities to conduct a criminal venture. The contrary judgment of the Court of Appeals is accordingly reversed.</p>
<p id="b350-5">
<em>So ordered.</em>
</p>
<footnote label="1">
<p id="b333-11">A pen. register is a mechanical device that records the numbers dialed on a telephone by monitoring the electrical impulses caused when the dial on the telephone is released. It does not overhear oral communications and does not indicate whether calls are actually completed.</p>
</footnote>
<footnote label="2">
<p id="b335-7"> The gambling operation was known to employ countersurveillance techniques. App. 21.</p>
</footnote>
<footnote label="3">
<p id="b335-8"> On the same date another United States District Court judge extended the original order of March 19 for an additional 20 days. <span class="citation no-link"><em>Id., </em>at 33</span>.</p>
</footnote>
<footnote label="4">
<p id="b336-5"> The Court of Appeals recognized that "without [the Company’s] technical aid, the order authorizing the use of a pen register will be worthless. Federal law enforcement agents simply cannot implement pen register surveillance without the Telephone Company’s help. The assistance requested requires no extraordinary expenditure of time or effort by [the Company]; indeed, as we understand it, providing lease or private lines is a relatively simple, routine procedure.” <span class="citation" data-id="9462905"><a href="/opinion/337714/application-of-the-united-states-of-america-in-the-matter-of-an-order/#961" aria-description="Citation for case: Application of the United States of America in the Matter...">538 F. 2d, at 961-962</a></span>.</p>
</footnote>
<footnote label="5">
<p id="b336-6"> Judge Mansfield dissented in part on the ground that the District Court possessed a discretionary power under the All Writs Act to direct the <page-number citation-index="1" label="165">*165</page-number>company to render such assistance as was necessary to implement its valid order authorizing the use of pen registers and that a compelling case had been established for the exercise of discretion in favor of the assistance order. He argued that district court judges could be trusted to exercise their powers under the All Writs Act only in cases of clear necessity and to balance the burden imposed upon the party required to render assistance against the necessity.</p>
</footnote>
<footnote label="6">
<p id="b337-12"> Although the pen register surveillance had been completed by the time the Court of Appeals issued its decision on July 13, 1976, this fact does not render the case moot, because the controversy here is one “capable of repetition, yet evading review.” <em>Southern Pacific Terminal Co. </em>v. <em>ICC, </em><span class="citation" data-id="97365"><a href="/opinion/97365/southern-pacific-terminal-co-v-interstate-commerce-commission/#515" aria-description="Citation for case: Southern Pacific Terminal Co. v. Interstate Commerce...">219 U. S. 498, 515</a></span> (1911); <em>Roe </em>v. <em>Wade, </em><span class="citation" data-id="9425157"><a href="/opinion/108713/roe-v-wade/#125" aria-description="Citation for case: Roe v. Wade">410 U. S. 113, 125</a></span> (1973). Pen register orders issued pursuant to Fed. Rule Crim. Proc. 41 authorize surveillance only for brief periods. Here, despite expedited action by the Court of Appeals, the order, as.extended, expired six days after oral argument. Moreover, even had the pen register order been stayed pending appeal, the mootness problem would have remained, because the showing of probable cause upon which the order authorizing the installation of the pen registers was based would almost certainly have become stale before review could have been completed. It is also plain, given the Company’s policy of refusing to render voluntary assistance in installing pen registers and the Government’s determination to continue to utilize them,, that the Company will be subjected to similar orders in the future. See <em>Weinstein </em>v. <em>Bradford, </em><span class="citation" data-id="109338"><a href="/opinion/109338/weinstein-v-bradford/#149" aria-description="Citation for case: Weinstein v. Bradford">423 U. S. 147, 149</a></span> (1975).</p>
</footnote>
<footnote label="7">
<p id="b337-13"> The Court of Appeals held that pen register surveillance was subject to the requirements of the Fourth Amendment. This conclusion is not challenged by either party, and we find it unnecessary to consider the matter. The Government concedes that its application for the pen register order did not' conform to the requirements of Title III.</p>
</footnote>
<footnote label="8">
<p id="b338-6"> Although neither this issue nor that of the scope of Fed. Rule Crim. Proc. 41 is encompassed within the question posed in the petition for certiorari and the Company has not filed a cross-petition, we have discretion to consider them because the prevailing party may defend a judgment on any ground which the law and the record permit that would not expand the relief it has been granted. <em>Langnes </em>v. <em>Green, </em><span class="citation" data-id="101669"><a href="/opinion/101669/langnes-v-green/#538" aria-description="Citation for case: Langnes v. Green">282 U. S. 531, 538-539</a></span> (1931); <em>Dandridge </em>v. <em>Williams, </em><span class="citation" data-id="9424234"><a href="/opinion/108115/dandridge-v-williams/" aria-description="Citation for case: Dandridge v. Williams">397 U. S. 471</a></span>, 475 n. 6 (1970). The only relief sought by the Company is that granted by the Court of Appeals: the reversal of the District Court’s order directing it to assist in the installation and operation of the pen registers. The Title III and Rule 41 questions were considered by both the District Court and the Court of Appeals and fully argued here.</p>
</footnote>
<footnote label="9">
<p id="b338-7"> Four Justices reached this conclusion in <em>United States </em>v. <em>Giordano, </em><span class="citation" data-id="9425702"><a href="/opinion/109020/united-states-v-giordano/#553" aria-description="Citation for case: United States v. Giordano">416 U. S. 505, 553-554</a></span> (1974) (Powell, J., joined by Burger, C. J., and Blackmun and Rehnquist, JJ., concurring in part and dissenting in part). The Court’s opinion did not reach the issue since the evidence derived from a pen register was suppressed as being in turn derived from an illegal wire interception. Every Court of Appeals that has considered the matter has agreed that pen registers are not within the scope of Title III. See <em>United States </em>v. <em>Illinois Bell Tel. Co., </em><span class="citation" data-id="333926"><a href="/opinion/333926/united-states-of-america-applicant-appellee-v-illinois-bell-telephone/" aria-description="Citation for case: United States of America, Applicant-Appellee v. Illinois...">531 F. 2d 809</a></span> (CA7 1976); <em>United States </em>v. <em>Southwestern Bell Tel. Co., </em><span class="citation" data-id="8900411"><a href="/opinion/8912555/united-states-v-southwestern-bell-telephone-co/" aria-description="Citation for case: United States v. Southwestern Bell Telephone Co.">546 F. 2d 243</a></span> (CA8 1976); <em>Michigan Bell Tel. Co. </em>v. <em>United States, </em><span class="citation" data-id="9464272"><a href="/opinion/350566/michigan-bell-telephone-company-v-united-states/" aria-description="Citation for case: Michigan Bell Telephone Company v. United States">565 F. 2d 385</a></span> (CA6 1977); <em>United States </em>v. <em>Falcone, </em><span class="citation" data-id="9461166"><a href="/opinion/322631/united-states-v-pasquale-falcone-appeal-of-pasquale-falconio-in-no/" aria-description="Citation for case: United States v. Pasquale Falcone Appeal of Pasquale...">505 F. 2d 478</a></span> (CA3 1974), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./420/955/">420 U. S. 955</a></span> (1975); <em>Hodge </em>v. <em>Mountain States Tel. &amp; Tel. Co., 555 </em>F. 2d 254 (CA9 1977); <em>United States </em>v. <em>Clegg, </em><span class="citation" data-id="324659"><a href="/opinion/324659/united-states-v-michael-william-clegg/" aria-description="Citation for case: United States v. Michael William Clegg">509 F. 2d 605</a></span>, 610 n. 6 (CA5 1975).</p>
</footnote>
<footnote label="10">
<p id="b338-10"> Similarly, the sanctions of Title III are aimed only at one who “willfully intercepts, endeavors to intercept, or procures any other person to intercept or endeavor to intercept, any wire or oral communication ... .” <span class="citation no-link">18 U. S. C. §2511</span> (l)(a).</p>
</footnote>
<footnote label="11">
<p id="b339-7"> “ ‘Contents’. . . includes any information concerning the identity of the parties to [the] communication or the 'existence, substance, purport, or meaning of [the] communication.”</p>
</footnote>
<footnote label="12">
<p id="b339-8"> See 538 P. 2d, at 957.</p>
</footnote>
<footnote label="13">
<p id="b340-8"> <em>United States </em>v. Dote, <span class="citation" data-id="274344"><a href="/opinion/274344/united-states-v-rocco-dote-and-theodore-p-veesart-united-states-of/" aria-description="Citation for case: United States v. Rocco Dote and Theodore P. Veesart,...">371 F. 2d 176</a></span> (CA7 1966), held that § 605 of the Communications Act of 1934, <span class="citation no-link">47 U. S. C. § 605</span>, which prohibited the interception and divulgence of “any communication” by wire or radio, included pen registers within the scope of its ban. In § 803 of Title III, <span class="citation no-link">82 Stat. 223</span>, Congress amended § 605 by restricting it to the interception of “any radio communication.” Thus it is clear that pen registers are no longer within the scope of § 605. See <em>Korman </em>v. <em>United States, </em><span class="citation" data-id="8891180"><a href="/opinion/8904074/korman-v-united-states/#931" aria-description="Citation for case: Korman v. United States">486 F. 2d 926, 931-932</a></span> (CA7 1973). The reference to <em><span class="citation" data-id="274344"><a href="/opinion/274344/united-states-v-rocco-dote-and-theodore-p-veesart-united-states-of/" aria-description="Citation for case: United States v. Rocco Dote and Theodore P. Veesart,...">Dote</a></span> </em>in the Senate Report is indicative of Congress’ intention not to place restrictions upon their use. We find no merit in the Company’s suggestion that the reference to <em><span class="citation" data-id="274344"><a href="/opinion/274344/united-states-v-rocco-dote-and-theodore-p-veesart-united-states-of/" aria-description="Citation for case: United States v. Rocco Dote and Theodore P. Veesart,...">Dote</a></span> </em>is merely an oblique expression of Congress’ desire that telephone companies be permitted to use pen registers in the ordinary course of business, as <em><span class="citation" data-id="274344"><a href="/opinion/274344/united-states-v-rocco-dote-and-theodore-p-veesart-united-states-of/" aria-description="Citation for case: United States v. Rocco Dote and Theodore P. Veesart,...">Dote</a></span> </em>allowed, so long as they are not used to assist law enforcement. Brief for Respondent 16. The sentences preceding the reference to' <em><span class="citation" data-id="274344"><a href="/opinion/274344/united-states-v-rocco-dote-and-theodore-p-veesart-united-states-of/" aria-description="Citation for case: United States v. Rocco Dote and Theodore P. Veesart,...">Dote</a></span> </em>state unequivocally that pen registers are not within the scope of Title III. In addition, a separate provision of Title III, <span class="citation no-link">18 U. S. C. § 2511</span> (2) (a) (i), specifically excludes all normal telephone company business practices from the prohibitions of the Act. Congress clearly intended to disavow <em><span class="citation" data-id="274344"><a href="/opinion/274344/united-states-v-rocco-dote-and-theodore-p-veesart-united-states-of/" aria-description="Citation for case: United States v. Rocco Dote and Theodore P. Veesart,...">Dote</a></span> </em>to the extent that it prohibited the use of pen registers by law enforcement authorities.</p>
</footnote>
<footnote label="14">
<p id="b340-9"> The Courts of Appeals that have considered the question have agreed that pen register orders are authorized by Fed. Rule Crim. Proc. 41 or by an inherent power closely akin to it to issue search warrants under circumstances conforming to the Fourth Amendment. See <em>Michigan Bell Tel. Co., supra; Southwestern Bell Tel. Co., supra; Illinois Bell Tel. Co., supra.</em></p>
</footnote>
<footnote label="15">
<p id="b341-7"> Where the definition of a term in Rule 41 (h) was intended to be all inclusive, it is introduced by the phrase “to mean” rather than “to include.” Cf. <em>Helvering, </em>v. <em>Morgan’s, Inc., </em><span class="citation" data-id="102316"><a href="/opinion/102316/helvering-v-morgans-inc/" aria-description="Citation for case: Helvering v. Morgan&#x27;s, Inc.">293 U. S. 121</a></span>, 125 n. 1 (1934).</p>
</footnote>
<footnote label="16">
<p id="b341-8"> The question of whether the FBI, in its implementation of the District Court’s pen register authorization, complied with all the requirements of Rule 41 is not before us. In <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>the Court stated that the notice requirement of Rule 41 (d) is not so inflexible as to require invariably that notice be given the person “searched” prior to the commencement of the search. 389 U. S., at 355-356, n. 16. Similarly, it is clear to us that the requirement of Rule 41 (c) that the warrant command that the search be conducted within 10 days of its issuance does not mean that the duration of a pen register surveillance may not exceed 10 days. Thus <page-number citation-index="1" label="170">*170</page-number>the District Court’s order, which authorized surveillance for a 20-day period, did not conflict with Rule 41.</p>
</footnote>
<footnote label="17">
<p id="b342-7"> See <em>United States </em>v. <em>Baird, </em><span class="citation" data-id="286043"><a href="/opinion/286043/united-states-v-earl-s-baird/#710" aria-description="Citation for case: United States v. Earl S. Baird">414 F. 2d 700, 710</a></span> (CA2 1969), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./396/1005/">396 U. S. 1005</a></span> (1970); <em>Jackson </em>v. <em>United States, </em>122 U. S. App. D. C. 324, 326, <span class="citation" data-id="9451218"><a href="/opinion/269987/henry-w-jackson-v-united-states/#864" aria-description="Citation for case: Henry W. Jackson v. United States">353 F. 2d 862, 864</a></span> (1965); <em>United States </em>v. <em>Remolif, </em>227 F: Supp. 420, 423 (Nev. 1964); <em>Link </em>v. <em>Wabash R. Co., </em><span class="citation" data-id="9422469"><a href="/opinion/106449/link-v-wabash-railroad/" aria-description="Citation for case: Link v. Wabash Railroad">370 U. S. 626</a></span>, 633 n. 8 (1962) (applying the analogous provision of Fed. Rule Civ. Proc. 83).</p>
</footnote>
<footnote label="18">
<p id="b342-8"> The dissent argues, <em>post, </em>at 182-184, that Rule 41 (b), as modified following <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967), to explicitly authorize searches for any property that constitutes evidence of a crime, falls short of authorizing warrants to “search” for and "seize” intangible evidence. The elimination of the restriction against seizing property that is “mere evidence,” however, has no bearing whatsoever on the scope of the definition of property set forth in Rule 41 (h) which, as the dissent acknowledges, remained unchanged. Moreover, the definition of property set forth in <page-number citation-index="1" label="171">*171</page-number>Rule 41 (h) is introduced by the phrase, “[t]he term 'property’ is used in this rule to <em>include" </em>(emphasis added), which indicates that it was not intended to be exhaustive. See <em>supra, </em>at 169.</p>
<p id="b343-7">We are unable to comprehend the logic supporting the dissent’s contention, <em>post, </em>at 184-185, that the conclusion of <em>Katz </em>v. <em>United States </em>that Rule 41 was not confined to tangible property did not survive the enactment of Title III and Title IX of the Omnibus Crime Control and Safe Streets Act of 1968, because Congress failed to expand the definition of property contained in Rule 41 (h). There was obviously no need for any such action in light of the Court’s construction of the Rule in <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>. </em>The dissent’s assertion that it “strains credulity” to conclude that Congress intended to permit the seizure of intangibles outside the scope of Title III without its safeguards disregards the congressional judgment that the use of pen registers be permissible without Title III restrictions. Indeed, the dissent concedes that pen registers are not governed by Title III. What “strains credulity” is the dissent’s conclusion, directly contradicted by the legislative history of Title III, that Congress intended to permit the interception of telephone conversations while prohibiting the use of pen registers to obtain much more limited information.</p>
</footnote>
<footnote label="19">
<p id="b344-8"> The three other Courts of Appeals which have considered the question reached a different conclusion from the Second Circuit. The Sixth Circuit in <em>Michigan Bell Tel. Co. </em>v. <em>United States, </em><span class="citation" data-id="9464272"><a href="/opinion/350566/michigan-bell-telephone-company-v-united-states/" aria-description="Citation for case: Michigan Bell Telephone Company v. United States">565 F. 2d 385</a></span> (1977), and the Seventh Circuit in <em>United States </em>v. <em>Illinois Bell Tel. Co., </em><span class="citation" data-id="333926"><a href="/opinion/333926/united-states-of-america-applicant-appellee-v-illinois-bell-telephone/" aria-description="Citation for case: United States of America, Applicant-Appellee v. Illinois...">531 F. 2d 809</a></span> (1976), held that the Act did authorize the issuance of orders compelling a telephone company to assist in the use of surveillance devices not covered by Title III such as pen registers. The Eighth Circuit found such authority to be part of the inherent power of district courts and “concomitant of the power to authorize pen register surveillance.” <em>United States </em>v. <em>Southwestern Bell Tel. Co., </em><span class="citation" data-id="8900411"><a href="/opinion/8912555/united-states-v-southwestern-bell-telephone-co/#246" aria-description="Citation for case: United States v. Southwestern Bell Telephone Co.">546 F. 2d, at 246</a></span>.</p>
</footnote>
<footnote label="20">
<p id="b346-6"> See <em>Labette County Comm’rs </em>v. <em>Moulton, </em><span class="citation" data-id="91198"><a href="/opinion/91198/labette-county-commissioners-v-united-states-ex-rel-moulton/#221" aria-description="Citation for case: Labette County Commissioners v. United States Ex Rel....">112 U. S. 217, 221</a></span> (1884): “[I]t does not follow because the jurisdiction in mandamus [now included in § 1651] is ancillary merely that it cannot be exercised over persons not parties to the judgment sought to be enforced.”</p>
</footnote>
<footnote label="21">
<p id="b346-7"> See <span class="citation no-link">47 U. S. C. § 201</span> (a) and N. Y. Pub. Serv. Law § 91 (McKinney 1955 and Supp. 1977-1978).</p>
</footnote>
<footnote label="22">
<p id="b347-5"> Tr. of Oral Arg. 27-28, 40.</p>
</footnote>
<footnote label="23">
<p id="b347-6"> The dissent’s attempt to draw a distinction between orders in aid of a court’s own duties and jurisdiction and orders designed to better enable a party to effectuate his rights and duties, <em>post, </em>a.t 189-190, is specious. Courts normally exercise their jurisdiction only in order to protect the legal rights of parties. In <em>Price </em>v. <em>Johnston, </em><span class="citation" data-id="9420168"><a href="/opinion/104557/price-v-johnston/" aria-description="Citation for case: Price v. Johnston">334 U. S. 266</a></span> (1948), for example, the production of the federal prisoner in court was required in order to enable him to effectively present his appeal which the court had jurisdiction to hear. Similarly, in <em>Harris </em>v. <em>Nelson, </em><span class="citation" data-id="9423958"><a href="/opinion/107877/harris-v-nelson/" aria-description="Citation for case: Harris v. Nelson">394 U. S. 286</a></span> (1969), discovery was ordered in connection with a habeas corpus proceeding for the purpose of enabling a prisoner adequately to protect his rights. Here, we have held that Fed. Rule Crim. Proc. 41 provided the District Court with power to authorize the FBI to install pen registers. The order issued by the District Court compelling the Company to provide technical assistance was required to prevent nullification of the court’s warrant and the frustration of the Government’s right under the warrant to conduct a pen register surveillance, just as the orders issued in <em><span class="citation" data-id="9420168"><a href="/opinion/104557/price-v-johnston/" aria-description="Citation for case: Price v. Johnston">Price</a></span> </em>and <em><span class="citation" data-id="9423958"><a href="/opinion/107877/harris-v-nelson/" aria-description="Citation for case: Harris v. Nelson">Harris</a></span> </em>were necessary to protect the rights of prisoners.</p>
</footnote>
<footnote label="24">
<p id="b347-7"> We are unable to agree with the Company’s assertion that “it is extraordinary to expect citizens to directly involve themselves in the law <page-number citation-index="1" label="176">*176</page-number>enforcement process.” Tr. of Oral Arg. 41. The conviction that private citizens have a duty to provide assistance to law enforcement officials when it is required is by no means foreign to our traditions, as the Company apparently believes. See <em>Babington </em>v. <em>Yellow Taxi Corp., </em><span class="citation" data-id="3582809"><a href="/opinion/3601389/matter-of-babington-v-yellow-taxi-corp/#17" aria-description="Citation for case: Matter of Babington v. Yellow Taxi Corp.">250 N. Y. 14, 17</a></span>, <span class="citation" data-id="3582809"><a href="/opinion/3601389/matter-of-babington-v-yellow-taxi-corp/#727" aria-description="Citation for case: Matter of Babington v. Yellow Taxi Corp.">164 N. E. 726, 727</a></span> (1928) (Cardozo, C. J.) (“Still, as in the days of Edward I, the citizenry may be called upon to enforce the justice of the state, not faintly and with lagging steps, but honestly and bravely and with whatever implements and facilities are convenient and at hand”). See also <em>In re Quarles and Butler, </em><span class="citation" data-id="94235"><a href="/opinion/94235/in-re-quarles-and-butler/#535" aria-description="Citation for case: In Re Quarles and Butler">158 U. S. 532, 535</a></span> (1895) (“It is the duty ... of every citizen, to assist in prosecuting, and in securing the punishment of, any breach of the peace of the United States”); <em>Hamilton </em>v. <em>Regents, </em><span class="citation" data-id="9418825"><a href="/opinion/102334/hamilton-v-regents-of-the-university-of-california/" aria-description="Citation for case: Hamilton v. Regents of the University of California">293 U. S. 245</a></span>, 265 n. (1934) (Cardozo, J., concurring) ; <em>Elrod </em>v. <em>Moss, </em><span class="citation" data-id="8823999"><a href="/opinion/8838892/elrod-v-moss/#129" aria-description="Citation for case: Elrod v. Moss">278 F. 123, 129</a></span> (CA4 1921). The concept that citizens have a duty to assist in enforcement of the laws is at least in part the predicate of Fed. Rule Crim. Proc. 17, which clearly contemplates power in the district courts to issue ssubpoenas and subpoenas <em>duces tecum </em>to nonparty witnesses and to hold noncomplying, nonparty witnesses in contempt. Cf. <em>Roviaro </em>v. <em>United States, </em><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/#59" aria-description="Citation for case: Roviaro v. United States">353 U. S. 53, 59</a></span> (1957) (“The [informer’s] privilege recognizes the obligation of citizens to communicate their knowledge of the commission of crimes to law-enforcement officials and, by preserving their anonymity, encourages them to perform that obligation”). Of course we do not address the question of whether and to what extent such a general duty may be legally enforced in the diverse contexts in which it may arise.</p>
</footnote>
<footnote label="25">
<p id="b349-5"> We reject the Court of Appeals’ suggestion that the fact that Congress amended Title III to require that communication common carriers provide necessary assistance in connection with electronic surveillance within the scope of Title III reveals a congressional “doubt that the courts possessed inherent power to issue such orders” and therefore “it seems reasonable to conclude that similar authorization should be required in connection with pen register orders . . . .” <span class="citation" data-id="9462905"><a href="/opinion/337714/application-of-the-united-states-of-america-in-the-matter-of-an-order/#962" aria-description="Citation for case: Application of the United States of America in the Matter...">538 F. 2d, at 962</a></span>. The amendment was passed following the decision of the Ninth Circuit in <em>Application of United States, </em><span class="citation" data-id="290598"><a href="/opinion/290598/application-of-the-united-states-for-relief/" aria-description="Citation for case: Application of the United States for Relief">427 F. 2d 639</a></span> (1970), which held that absent specific statutory authority, a United States District Court was without power to compel a telephone company to assist in a wiretap conducted pursuant to Title III. The court refused to infer such authority in light of Congress’ silence in a statute which constituted a “comprehensive legislative treatment” of wiretapping. <span class="citation" data-id="290598"><a href="/opinion/290598/application-of-the-united-states-for-relief/#643" aria-description="Citation for case: Application of the United States for Relief"><em>Id., </em>at 643</a></span>. We think that Congress’ prompt action in amending the Act was not an acceptance of the Ninth Circuit’s view but “more in the nature of an overruling of that opinion.” <em>United States </em>v. <em>Illinois Bell Tel. Co., </em><span class="citation" data-id="333926"><a href="/opinion/333926/united-states-of-america-applicant-appellee-v-illinois-bell-telephone/#813" aria-description="Citation for case: United States of America, Applicant-Appellee v. Illinois...">531 F. 2d, at 813</a></span>. The meager legislative history of the amendment indicates that Congress was only providing an unequivocal statement of its intent under Title III. See 115 Cong. Rec. 37192 (1969) (remarks of Sen. McClellan). We decline to infer from a congressional grant of authority under these circumstances that such authority was previously lacking. See <em>FTC </em>v. <em>Dean Foods Co,, </em><span class="citation" data-id="9423244"><a href="/opinion/107255/federal-trade-commission-v-dean-foods-co/#608" aria-description="Citation for case: Federal Trade Commission v. Dean Foods Co.">384 U. S. 597, 608-612</a></span> (1966); <em>Wong Yang Sung </em>v. <em>McGrath, </em><span class="citation" data-id="9420439"><a href="/opinion/104768/wong-yang-sung-v-mcgrath/#47" aria-description="Citation for case: Wong Yang Sung v. McGrath">339 U. S. 33, 47</a></span> (1950).</p>
<p id="b349-6">Moreover, even if Congress’ action were viewed as indicating acceptance of the Ninth Circuit’s view that there was no authority for the issuance of orders compelling telephone companies to provide assistance in connection with wiretaps without an explicit statutory provision, it would not follow that explicit congressional authorization was also needed to order telephone companies to assist in the installation and operation of pen registers which, unlike wiretaps, are not regulated by a comprehensive statutory scheme. In any event, by amending Title III Congress has now required that at the Government’s request telephone companies be directed to provide <page-number citation-index="1" label="178">*178</page-number>assistance in connection with wire interceptions. It is plainly unlikely that Congress intended at the same time to leave federal courts without authority to requiré assistance in connection with pen registers.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/united-states-v-shakir--152638.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a29cdc62a6d7b2fd", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "united-states-v-shakir--152638"}, "payload": {"all": [{"cite": "616 F.3d 315", "page": "315", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "616"}, {"cite": "2010 U.S. App. LEXIS 16492", "page": "16492", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2010"}, {"cite": "2010 WL 3122808", "page": "3122808", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2010"}], "display": "616 F.3d 315", "official": {"cite": "616 F.3d 315", "page": "315", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "616"}, "official_selection_present": true, "record_id": "united-states-v-shakir--152638"}}
{"assertion_id": "b038a3b81a3db800", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-shakir--152638"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-shakir--152638", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-shakir--152638

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-shakir--152638",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "United States v. Shakir",
    "case_name_short": "Shakir",
    "case_name_full": "UNITED STATES of America v. Naim Nafis SHAKIR, A/K/A Naim Shakir A/K/A James Perry Naim Nafis Shakir, Appellant",
    "input_case_name": "United States v. Shakir",
    "court": "U.S. Court of Appeals, 3d Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca3",
    "state": null,
    "date_decided": null,
    "year": 2010,
    "docket": null,
    "cluster_id": 152638,
    "lead_opinion_id": 152638,
    "sibling_ids": [],
    "absolute_url": "/opinion/152638/united-states-v-shakir/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "616 F.3d 315",
      "volume": "616",
      "reporter": "F.3d",
      "page": "315",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2010 U.S. App. LEXIS 16492",
        "volume": "2010",
        "reporter": "U.S. App. LEXIS",
        "page": "16492",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 WL 3122808",
        "volume": "2010",
        "reporter": "WL",
        "page": "3122808",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "616 F.3d 315",
        "volume": "616",
        "reporter": "F.3d",
        "page": "315",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 U.S. App. LEXIS 16492",
        "volume": "2010",
        "reporter": "U.S. App. LEXIS",
        "page": "16492",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 WL 3122808",
        "volume": "2010",
        "reporter": "WL",
        "page": "3122808",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "616 F.3d 315",
    "official_selection": {
      "court_class": "coa",
      "selected": "616 F.3d 315",
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
    "date_created": "2026-07-06T13:14:17Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:14:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:14:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:14:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:14:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — united-states-v-shakir--152638

```
                                           PRECEDENTIAL

       UNITED STATES COURT OF APPEALS
            FOR THE THIRD CIRCUIT


                      No. 09-2665


           UNITED STATES OF AMERICA

                           v.

                NAIM NAFIS SHAKIR,
                  a/k/a Naim Shakir
                   a/k/a James Perry

                    NAIM NAFIS SHAKIR,
                                 Appellant


     On Appeal from the United States District Court
        for the Eastern District of Pennsylvania
                 (D.C. No. 07-cr-00488)
       District Judge: Honorable Anita B. Brody


                 Argued April 13, 2010
Before: FISHER, HARDIMAN and COWEN, Circuit Judges.

                (Filed: August 10, 2010)
Joseph F. Minni [Argued]
Office of United States Attorney
615 Chestnut Street
Suite 1250
Philadelphia, PA 19106-0000
       Attorney for Appellee

Christy Unger [Argued]
David L. McColgin
James J. McHugh, Jr.
Leigh M. Skipper
Brett G. Sweitzer
Defender Association of Philadelphia
Federal Court Division
601 Walnut Street
The Curtis Center, Suite 540 West
Philadelphia, PA 19106-0000
       Attorneys for Appellant




                 OPINION OF THE COURT




HARDIMAN, Circuit Judge.

       In this appeal we consider the legality of a warrantless
search incident to arrest in light of the Supreme Court’s decision
in Arizona v. Gant, 129 S. Ct. 1710 (2009).


                                2
                                I.

       On May 22, 2007, a Pennsylvania state magistrate judge
issued an arrest warrant for Naim Nafis Shakir, who police
believed was involved in an armed robbery of a PNC Bank a
month earlier. The warrant was promptly entered into the
database of the National Crime Information Center and came to
the attention of Federal Bureau of Investigation agents in
Pennsylvania. Because those agents believed Shakir had
gambling ties to Atlantic City, New Jersey, they enlisted the help
of FBI Special Agent Joseph Furey in New Jersey.

       The following day, Special Agent Furey learned that
Shakir had recently stayed in the Trump Plaza Hotel and Casino.
In response, Furey asked Atlantic City Police Detective David
Smith, who was assigned to an FBI task force, to investigate the
lead. Detective Smith visited the Trump Plaza and was
informed that not only had Shakir been gambling at the casino
the previous day, but he was expected to check into the hotel at
4:00 that afternoon. Since it was already around 2:00 p.m.,
Smith immediately notified Special Agent Furey, who began to
organize a team to arrest Shakir upon his appearance at the
hotel. Before the arrest team arrived, however, security spotted
Shakir entering the hotel. When he learned this, Smith asked
Special Agent Furey to expedite his arrival to effectuate the
arrest. Smith also called the Atlantic City Police to request a
squad car. Smith then proceeded to the lobby with two hotel
security personnel; all three were dressed in plainclothes.

      Soon after he entered the lobby, Detective Smith spotted
Shakir standing at the end of the check-in line some 25 feet

                                3
away, holding a gym bag. As Smith drew closer to Shakir, he
heard a man about 15 feet away yell “shit!,” which Smith took
as a warning to Shakir. Although Shakir turned as if to respond,
he simply maintained eye contact with the shouter. Meanwhile,
Detective Smith asked the hotel security agents, both of whom
were unarmed, to detain Shakir’s apparent confederate while
Smith hurried over to Shakir, grabbed his arm, and placed him
under arrest. Shakir complied and dropped his bag on the floor
at his feet.

        Detective Smith immediately patted down Shakir and
found no weapons on his person. Smith attempted to handcuff
Shakir, but was unable to do so because of Shakir’s girth.
Indeed, Shakir advised Smith that police “usually use three sets
of handcuffs.” Shakir was polite and compliant during the
arrest, and after the initial excitement, the arrest was “very low
key.” There were approximately 20 people in the hotel lobby
during and following the arrest.

        Within five minutes of Shakir’s initial arrest, two armed
police officers arrived with handcuffs which Smith used to
restrain Shakir. While the other officers held Shakir by the
arms, Smith bent down to investigate the contents of the bag at
Shakir’s feet. Therein Smith found clothes and a large amount
of cash, but no weapons. Some of the cash in the bag was later
identified as having been stolen during an armed robbery of the
Belco Credit Union in Lancaster, Pennsylvania on May 21, 2007
(not from the PNC Bank robbery that prompted the warrant for
Shakir’s arrest).



                                4
        Shakir was indicted on one count of armed robbery of the
Belco Credit Union in violation of 18 U.S.C. §§ 2113(d) and 2.
Prior to trial, Shakir filed a motion to suppress evidence,
claiming Detective Smith’s search of his gym bag violated his
Fourth Amendment right to be free from unreasonable searches.
After the District Court denied the motion, Shakir proceeded to
trial and was convicted by a jury.

                                II.

       The District Court had jurisdiction under 18 U.S.C. §
3231 and we have jurisdiction under 28 U.S.C. § 1291. We
review the District Court’s factual findings for clear error, and
we exercise plenary review over its application of law to those
facts. United States v. Bond, 581 F.3d 128, 133 (3d Cir. 2009).

                               III.

        Shakir’s sole argument on appeal is that the cash found
by police was inadmissible at trial because it was the fruit of an
illegal search. The Government counters that it conducted a
legal search incident to arrest. Under this well-recognized
exception to the warrant requirement of the Fourth Amendment,
“[w]hen an arrest is made, it is reasonable for the arresting
officer to search the person arrested in order to remove any
weapons that the latter might seek to use in order to resist arrest
or effect his escape.” Chimel v. California, 395 U.S. 752, 762-
63 (1969). The permissible scope of a search incident to arrest
includes “the arrestee’s person and the area ‘within his
immediate control’—construing that phrase to mean the area


                                5
from within which he might gain possession of a weapon or
destructible evidence.” Id. at 763.

       The crux of Shakir’s appeal is that because he was
already handcuffed at the time Detective Smith searched his bag,
he had no access to any weapon or destructible evidence that
might have been in the bag. The Government responds by citing
several appellate decisions upholding searches incident to arrest
conducted after the suspect was handcuffed. See, e.g., Virgin
Islands v. Rasool, 657 F.2d 582, 584-85, 588-89 (3d Cir. 1981);
United States v. Horne, 4 F.3d 579, 587 (8th Cir. 1993); United
States v. Nohara, 3 F.3d 1239, 1243 (9th Cir. 1993); United
States v. Helmstetter, 56 F.3d 21, 23 (5th Cir.1995); United
States v. Mitchell, 64 F.3d 1105, 1110-11 (7th Cir. 1995);
United States v. Abdul-Saboor, 85 F.3d 664, 668-69 (D.C. Cir.
1996). These decisions followed a general trend among the
courts of appeals, following the Supreme Court’s decision in
New York v. Belton, 453 U.S. 454, 460 (1981), toward a rule that
although “the search is limited to the area under the defendant’s
control at the time of his arrest, the fact that it is no longer under
his control at the time of the search does not invalidate the
search.” United States v. Tejada, 524 F.3d 809, 812 (7th Cir.
2008); see also Abdul-Saboor, 85 F.3d at 669 (“[I]f the courts
were to focus exclusively upon the moment of the search, we
might create a perverse incentive for an arresting officer to
prolong the period during which the arrestee is kept in an area
where he could pose a danger to the officer.”); United States v.
McLaughlin, 170 F.3d 889, 893 (9th Cir. 1999); United States
v. Currance, 446 F.3d 554, 557 (4th Cir. 2006) (“[O]fficers may
separate the suspect from the item to be searched, thereby


                                  6
alleviating their safety concerns, before they conduct the
search.”) (citation, quotation marks and alteration omitted).

        Like the District Court’s decision denying Shakir’s
motion to suppress, however, the cases upon which the
Government relies all predated the Supreme Court’s decision in
Arizona v. Gant, 129 S. Ct. 1710 (2009), which narrowed the
scope of the search-incident-to-arrest doctrine. In Gant the
Supreme Court held that officers could not search an arrestee’s
car after he had been removed from the vehicle and secured,
noting that “[t]o read Belton as authorizing a vehicle search
incident to every recent occupant’s arrest would thus untether
the rule from the justifications [i.e., officer safety and preventing
the destruction of evidence] underlying the Chimel exception.”
Gant, 129 S. Ct. at 1719. Accordingly, the Gant Court
concluded that searches of a suspect’s automobile are not
permitted incident to an arrest when the police “could not
reasonably have believed . . . that [the arrestee] could have
accessed his car at the time of the search.” Id.

        Because Gant involved an automobile search, and
because it interpreted Belton, another automobile case, the
Government contends that the rule of Gant applies only to
vehicle searches. We do not read Gant so narrowly. The Gant
Court itself expressly stated its desire to keep the rule of Belton
tethered to “the justifications underlying the Chimel exception,”
id., and Chimel did not involve a car search. Moreover, as we
noted above, many courts of appeals perceived Belton to
establish a relaxed rule for searches incident to arrest in all
contexts. See, e.g., Tejada, 524 F.3d at 812 (applying Belton to
search of a cabinet in a home); Abdul-Saboor, 85 F.3d at 669

                                 7
(applying Belton to an apartment search). Because Gant
foreclosed such a relaxed reading of Belton, there is no plausible
reason why it should be held to do so only with respect to
automobile searches, rather than in any situation where the item
searched is removed from the suspect’s control between the time
of the arrest and the time of the search. Although this Court has
never explicitly adopted a “time of the arrest” rule like that
adopted in the aforementioned cases, we do read Gant as
refocusing our attention on a suspect’s ability (or inability) to
access weapons or destroy evidence at the time a search incident
to arrest is conducted.

        It is in this vein that Shakir points to our decision in
United States v. Myers, 308 F.3d 251 (3d Cir. 2002), which we
regard as being consistent with Gant despite predating it. In
Myers, a single policeman responded to a 911 call reporting a
disturbance involving a gun in an apartment. Id. at 253. Upon
arriving at the scene, he found the defendant hiding. The
defendant came out and laid face down on the floor when
ordered, throwing a bag down three feet away from himself in
the process. Id. The officer handcuffed the defendant and
patted him down, finding nothing. Two other officers then
arrived, and they took custody of the defendant while the first
officer went downstairs to briefly interview a woman who had
been arguing with the defendant. Id. at 254. The first officer
later returned upstairs, where Myers was still lying face down,
handcuffed and attended by the two officers. Noticing that
Myers was looking at the bag on the floor and acting nervously,
the first officer searched the bag and found a gun inside. Id.



                                8
       We held that this search was not lawfully incident to
Myers’s arrest.1 In doing so, we quoted with approval an
opinion of the Court of Appeals for the District of Columbia
Circuit which suggested that a search under these circumstances
would be valid as incident to the arrest “[a]bsent some objective
basis upon which to conclude that the arresting officer had no
reason to fear either the arrestee or the environment in which the
arrest unfolded.” Id. at 267 (quoting United States v. Abdul-
Saboor, 85 F.3d 664, 670 (D.C. Cir. 1996) (emphasis omitted)).
We also acknowledged that “where, in the heat of an arrest, an
officer concludes that a particular item is within the arrestee’s
grasp, courts are extremely reluctant to subsequently determine
that the officer’s conclusion was unreasonable and thereby
suppress whatever evidence may have been found.” Id. at 273.
Nevertheless, the facts of Myers’s case presented an objective
basis to conclude that he was no longer dangerous when the
search occurred: he was lying on the floor and guarded by two
policemen, he had already been frisked for weapons, the bag
that was searched was three feet away from him and zipped shut,
and the searching officer had not seen the need to search the bag


       1
         The Government notes that we also concluded that there
was no probable cause to arrest Myers, which was an alternative
basis for suppression. The Government therefore argues that
our conclusions in Myers with respect to the search-incident-to-
arrest doctrine were dicta. Contrary to the Government’s
argument, “[w]hen two independent reasons support a decision,
neither can be considered obiter dictum; each represents a valid
holding of the court.” Kushner v. Winterthur Swiss Ins. Co., 620
F.2d 404, 408 n.4 (3d Cir. 1980).

                                9
at the time of arrest, but instead went downstairs and
interviewed a witness first. Id. Significantly for purposes of the
instant appeal, we noted that, “[h]ad [the officer] searched the
bag . . . before going downstairs, we would have a different set
of circumstances to consider against the teachings of Chimel and
its progeny.” Id. at 274. We also emphasized that the officer’s
testimony suggested that he was not concerned about the
possible presence of a weapon until after he opened the bag. Id.
at 274.

       As in Myers, Shakir was handcuffed and restrained by
two policemen at the time his bag was searched. Unlike in
Myers, however, Shakir was standing up at the time of the
search, he was in a public place with some 20 people around,
and his bag was right next to him. In addition, the police had
reason to believe that one or possibly more of Shakir’s
accomplices was nearby, and the suspected accomplice Smith
had identified was restrained only by two unarmed private
security officers. Moreover, Detective Smith did not leave the
scene before searching the bag, and he testified that his chief
concern in searching the bag was to prevent any weapons that
might be inside from being used to injure police or the innocent
bystanders in the hotel lobby. As a result, several of the key
elements of the objective basis on which we concluded that
Myers was no longer dangerous are not present in this case.

       Because Myers is not binding here, we are left to
consider, under Gant and other relevant precedents, whether
Shakir retained sufficient potential access to his bag to justify a
warrantless search. Specifically, we must consider whether the
fact that Shakir was handcuffed and guarded by two armed

                                10
policemen precluded his access to the contents of the bag. Gant
makes clear that whether a suspect is “secured” is an important
consideration in assessing the lawfulness of a warrantless
search. In fact, the Gant Court “h[e]ld that the Chimel rationale
authorizes police to search a vehicle incident to a recent
occupant’s arrest only when the arrestee is unsecured and within
reaching distance of the passenger compartment at the time of
the search.” Gant, 129 S. Ct. at 1719. This language could be
read to prohibit the search of the bag unless at the time of the
search Shakir was both (1) unsecured and (2) within reaching
distance of the bag. Under this reading, once a suspect is
“secured,” no searches would be permitted incident to his arrest,
regardless of whether the searched items are within his reaching
distance.

       We find such an aggressive reading of Gant to be
unpersuasive, however, because it is inconsistent with the
remainder of the Gant opinion, with other Supreme Court
precedents, and with the valid concern for the safety of police
and the public. First, a closer reading of Gant reveals that the
Court’s references to a suspect being “unsecured” and being
“within reaching distance” of a vehicle are two ways of
describing a single standard rather than independent prongs of
a two-part test. In later formulations of its holding, the Gant
Court omitted any reference to whether Gant was secured or
unsecured, and looked instead simply to Gant’s ability to access
his vehicle. Thus, the Court stated: “[b]ecause police could not
reasonably have believed . . . that Gant could have accessed his
car at the time of the search . . . the search in this case was
unreasonable.” Id. at 1719. And in its final summation, the
Court explained that “[p]olice may search a vehicle incident to

                               11
a recent occupant’s arrest only if the arrestee is within reaching
distance of the passenger compartment at the time of the search
. . . .” Id. at 1723. The conspicuous absence of any mention of
the “secured” status of a suspect suggests that the Court did not
regard it as an independent element that must be satisfied in
order to justify a search incident to arrest. Accordingly, we
understand Gant to stand for the proposition that police cannot
search a location or item when there is no reasonable possibility
that the suspect might access it.

       Second, if Gant is construed to forbid all container
searches after a suspect is handcuffed or held by police, it would
not only narrow Belton but also effectively eliminate a major
element of the search-incident-to-arrest doctrine. In Chimel, the
Supreme Court stated that searches of “the arrestee’s person”
and “the area into which an arrestee might reach” could be
aimed at finding weapons the arrestee might use to “effect his
escape.” 395 U.S. at 763. The Court thus contemplated that
such searches would take place after the suspect is restrained in
some way. To hold that a container search incident to arrest
may not occur once the suspect is under the control of the
police, but before he has been moved away from the item to be
searched, would eviscerate this portion of Chimel. Gant did not
purport to do any such thing.

      Third, we note that handcuffs are not fail-safe. As the
Court of Appeals for the Fifth Circuit has stated, it is not true
that

       by handcuffing a suspect, the police instantly and
       completely eliminate all risks that the suspect will

                               12
       flee or do them harm. . . . Handcuffs are a
       temporary restraining device; they limit but do not
       eliminate a person’s ability to perform various
       acts. They obviously do not impair a person’s
       ability to use his legs and feet, whether to walk,
       run, or kick. Handcuffs do limit a person’s ability
       to use his hands and arms, but the degree of the
       effectiveness of handcuffs in this role depends on
       a variety of factors, including the handcuffed
       person's size, strength, bone and joint structure,
       flexibility, and tolerance of pain. Albeit difficult,
       it is by no means impossible for a handcuffed
       person to obtain and use a weapon concealed on
       his person or within lunge reach, and in so doing
       to cause injury to his intended victim, to a
       bystander, or even to himself. Finally, like any
       mechanical device, handcuffs can and do fail on
       occasion.

United States v. Sanders, 994 F.2d 200, 209 (5th Cir. 1993).
The Sanders court noted that “in 1991 alone . . . at least four
police officers were killed by persons who had already been
handcuffed.” Id. at 209-10. And such incidents continue. See,
e.g., United States Dep’t of Justice, 2008 Law Enforcement
O f f i c e r s      K i l l e d     &     A s s a u l t e d ,
http://www.fbi.gov/ucr/killed/2008/summaries.html (follow
“TX” link) (officer killed by handcuffed suspect); United States
Dep’t of Justice, 2006 Law Enforcement Officers Killed &
Assaulted, http://www.fbi.gov/ucr/killed/2006/summaries.html
(follow “TX” link) (same). Thus, reading Gant to prohibit a


                                13
search incident to arrest whenever an arrestee is handcuffed
would expose police to an unreasonable risk of harm.

        For the foregoing reasons, we hold that a search is
permissible incident to a suspect’s arrest when, under all the
circumstances, there remains a reasonable possibility that the
arrestee could access a weapon or destructible evidence in the
container or area being searched. Although this standard
requires something more than the mere theoretical possibility
that a suspect might access a weapon or evidence, it remains a
lenient standard.

                               IV.

        Applying the legal standard we have enunciated to the
facts of this appeal, we conclude that there remained a sufficient
possibility that Shakir could access a weapon in his bag to
justify its search. Although he was handcuffed and guarded by
two policemen, Shakir’s bag was literally at his feet, so it was
accessible if he had dropped to the floor. Although it would
have been more difficult for Shakir to open the bag and retrieve
a weapon while handcuffed, we do not regard this possibility as
remote enough to render unconstitutional the search incident to
arrest. This is especially true when we consider that Shakir was
subject to an arrest warrant for armed bank robbery, and that he
was arrested in a public area near some 20 innocent bystanders,
as well as at least one suspected confederate who was guarded
only by unarmed hotel security officers.            Under these
circumstances, the police were entitled to search Shakir’s bag
incident to arresting him. Consequently, suppression of the cash


                               14
found within the bag was not required and we will affirm the
judgment of the District Court.




                            15

```

---

## GROUP: _overhaul2/lake/cases/united-states-v-valenzuela-bernal--110797.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b769cbb341cc1586", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "united-states-v-valenzuela-bernal--110797"}, "payload": {"all": [{"cite": "458 U.S. 858", "page": "858", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "458"}, {"cite": "102 S. Ct. 3440", "page": "3440", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "102"}, {"cite": "73 L. Ed. 2d 1193", "page": "1193", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "73"}, {"cite": "1982 U.S. LEXIS 159", "page": "159", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1982"}, {"cite": "50 U.S.L.W. 5108", "page": "5108", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "50"}], "display": null, "official": null, "official_selection_present": false, "record_id": "united-states-v-valenzuela-bernal--110797"}}
{"assertion_id": "47c1dec10475872f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-valenzuela-bernal--110797"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-valenzuela-bernal--110797", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-valenzuela-bernal--110797

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-valenzuela-bernal--110797",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "United States v. Valenzuela-Bernal",
    "case_name_short": "Valenzuela-Bernal",
    "case_name_full": "United States v. Valenzuela-Bernal",
    "input_case_name": "United States v. Valenzuela-Bernal",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1982-07-02",
    "year": 1982,
    "docket": null,
    "cluster_id": 110797,
    "lead_opinion_id": 9428945,
    "sibling_ids": [],
    "absolute_url": "/opinion/110797/united-states-v-valenzuela-bernal/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "458 U.S. 858",
        "volume": "458",
        "reporter": "U.S.",
        "page": "858",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 S. Ct. 3440",
        "volume": "102",
        "reporter": "S. Ct.",
        "page": "3440",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "73 L. Ed. 2d 1193",
        "volume": "73",
        "reporter": "L. Ed. 2d",
        "page": "1193",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 U.S.L.W. 5108",
        "volume": "50",
        "reporter": "U.S.L.W.",
        "page": "5108",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1982 U.S. LEXIS 159",
        "volume": "1982",
        "reporter": "U.S. LEXIS",
        "page": "159",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "458 U.S. 858",
        "volume": "458",
        "reporter": "U.S.",
        "page": "858",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 S. Ct. 3440",
        "volume": "102",
        "reporter": "S. Ct.",
        "page": "3440",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "73 L. Ed. 2d 1193",
        "volume": "73",
        "reporter": "L. Ed. 2d",
        "page": "1193",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1982 U.S. LEXIS 159",
        "volume": "1982",
        "reporter": "U.S. LEXIS",
        "page": "159",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 U.S.L.W. 5108",
        "volume": "50",
        "reporter": "U.S.L.W.",
        "page": "5108",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "other",
      "selected": null,
      "reason": "unlisted_reporter:U.S."
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
    "date_created": "2026-07-06T13:49:12Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:49:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:49:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:49:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:49:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — united-states-v-valenzuela-bernal--110797

```
<opinion type="majority">
<author id="b898-7"><page-number citation-index="1" label="860">*860</page-number>Justice Rehnquist</author>
<p id="AMBE">delivered the opinion of the Court.</p>
<p id="b898-8">Respondent, a citizen of Mexico, was indicted in the United States District Court for the Southern District of California for transporting one Romero-Morales in violation of <span class="citation no-link">8 U. S. C. § 1324</span>(a)(2). That section generally prohibits the knowing transportation of an alien illegally in the United States who last entered the country within three years prior to the date of the transportation.<footnotemark>1</footnotemark> Respondent was found guilty after a bench trial, but his conviction was overturned by the United States Court of Appeals for the Ninth Circuit. That court held that the action of the Government in deporting two aliens other than Romero-Morales violated respondent’s right under the Sixth Amendment to the United States Constitution to compulsory process, and his right under the Fifth Amendment to due process of law. We granted certiorari in order to review the Court of Appeals’ application of these constitutional provisions to this case, <span class="citation multiple-matches"><a href="/c/U.%20S./454/963/">454 U. S. 963</a></span> (1981),<footnotemark>2</footnotemark> and we now reverse.</p>
<p id="b898-9">H-1</p>
<p id="b898-3">Respondent entered the United States illegally on March 23, 1980, and was taken by smugglers to a house in Escondido, Cal. Six days later, in exchange for his not having to pay the smugglers for bringing him across the border, respondent agreed to drive himself and five other passengers to Los Angeles. When the car which respondent was driving <page-number citation-index="1" label="861">*861</page-number>approached the Border Patrol checkpoint at Temecula, agents noticed the five passengers lying down inside the car and motioned to respondent to stop. Respondent accelerated through the checkpoint and was chased at high speed for approximately one mile before stopping the car and fleeing on foot along with the five passengers. Three of the passengers and respondent were apprehended by the Border Patrol agents.</p>
<p id="b899-4">Following their arrest, respondent and the other passengers were interviewed by criminal investigators. Respondent admitted his illegal entry into the country and explained his reason for not stopping at the checkpoint: “I was bringing the people [and] I already knew I had had it — too late — it was done.” App. 27. The three passengers also admitted that they were illegally in the country and each identified respondent as the driver of the car. <em>Id., </em>at 66. An Assistant United States Attorney concluded that the passengers possessed no evidence material to the prosecution or defense of respondent for transporting illegal aliens, and two of the passengers were deported to Mexico. The third, Enrique Romero-Morales, was detained to provide a nonhearsay basis for establishing that respondent had transported an illegal alien in violation of <span class="citation no-link">8 U. S. C. § 1324</span>(a)(2).</p>
<p id="b899-5">Respondent moved in the District Court to dismiss the indictment, claiming that the Government’s deportation of the two passengers other than Romero-Morales violated his Fifth Amendment right to due process of law and his Sixth Amendment right to compulsory process for obtaining favorable witnesses. He claimed that the deportation had deprived him of the opportunity to interview the two remaining passengers to determine whether they could aid in his defense. Although he had been in their presence throughout the allegedly criminal activity, respondent made no attempt to explain how the deported passengers could assist him in proving that he did not know that Romero-Morales was an illegal alien who had last entered the United States within the preceding three years.</p>
<p id="b900-4"><page-number citation-index="1" label="862">*862</page-number>At least one evidentiary hearing was held on respondent’s motion, at which Romero-Morales testified that he had not spoken to respondent during the entire time that they were together. At the same hearing the Government offered, without obtaining agreement by respondent, to stipulate that none of the passengers in the car told respondent that they were in the United States illegally. The District Court denied respondent’s motion and, following a bench trial on stipulated evidence, found respondent guilty as charged.<footnotemark>3</footnotemark></p>
<p id="b900-5">The Court of Appeals reversed the conviction. The court relied upon the rule, first stated in <em>United States </em>v. <em>Mendez-Rodriguez, </em><span class="citation" data-id="9457477"><a href="/opinion/299642/united-states-v-manuel-mendez-rodriguez/" aria-description="Citation for case: United States v. Manuel Mendez-Rodriguez">450 F. 2d 1</a></span> (CA9 1971), that the Government violates the Fifth and Sixth Amendments when it deports alien witnesses before defense counsel has an opportunity to interview them. <span class="citation" data-id="389588"><a href="/opinion/389588/united-states-v-ricardo-valenzuela-bernal/#73" aria-description="Citation for case: United States v. Ricardo Valenzuela-Bernal">647 F. 2d 72, 73-75</a></span> (1981). Although it stated that a constitutional violation occurs only when “the alien’s testimony could conceivably benefit the defendant,” <span class="citation" data-id="389588"><a href="/opinion/389588/united-states-v-ricardo-valenzuela-bernal/#74" aria-description="Citation for case: United States v. Ricardo Valenzuela-Bernal"><em>id., </em>at 74</a></span>, the court’s application of the “conceivable benefit” test demonstrated that the test will be satisfied whenever the deported aliens were eyewitnesses to the crime.<footnotemark>4</footnotemark> Respond<page-number citation-index="1" label="863">*863</page-number>ent’s failure to explain what beneficial evidence would have been provided by the two passengers was thus inapposite, for “the deported aliens were eyewitnesses to, and active participants in, the crime charged, thus establishing a strong possibility that they could have provided material and relevant information concerning the events constituting the crime.” <span class="citation" data-id="389588"><a href="/opinion/389588/united-states-v-ricardo-valenzuela-bernal/#75" aria-description="Citation for case: United States v. Ricardo Valenzuela-Bernal"><em>Id., </em>at 75</a></span>. Accordingly, the Court of Appeals held that respondent’s motion to dismiss the indictment should have been granted by the District Court.</p>
<p id="b901-8">i — I 1 — I</p>
<p id="b901-3">We think that the decision of the Court of Appeals in this case, and some of the additional arguments made in support of it by respondent, misapprehend the varied nature of the duties assigned to the Executive Branch by Congress. The Constitution imposes on the President the duty to “take Care that the Laws be faithfully executed.” U. S. Const., Art. II, § 3. One of the duties of the Executive Branch, and a vitally important one, is that of apprehending and obtaining the conviction of those who have violated criminal statutes of the United States. The prosecution of respondent is of course one example of the Executive’s effort to discharge that responsibility.</p>
<p id="b902-4"><page-number citation-index="1" label="864">*864</page-number>But the Government is charged with a dual responsibility when confronted with incidents such as that which resulted in the apprehension of respondent. One or more of the persons in the car may have violated the criminal laws enacted by Congress; but some or all of the persons in the car may also be subject to deportation as provided by Congress. The Government may, therefore, find itself confronted with the obligation of prosecuting persons in the position of respondent on criminal charges, and at the same time obligated to deport other persons involved in the event in order to carry out the immigration policies that Congress has enacted.</p>
<p id="b902-5">The power to regulate immigration — an attribute of sovereignty essential to the preservation of any nation — has been entrusted by the Constitution to the political branches of the Federal Government. See <em>Mathews </em>v. <em>Diaz, </em><span class="citation" data-id="109463"><a href="/opinion/109463/mathews-v-diaz/#81" aria-description="Citation for case: Mathews v. Diaz">426 U. S. 67, 81</a></span> (1976). “The Court without exception has sustained Congress’ ‘plenary power to make rules for the admission of aliens.’” <em>Kleindienst </em>v. <em>Mandel, </em><span class="citation multiple-matches"><a href="/c/U.%20S./408/758/">408 U. S. 758</a></span>, 766 (1972) (quoting <em>Boutilier </em>v. <em>INS, </em><span class="citation" data-id="9423425"><a href="/opinion/107450/boutilier-v-immigration-naturalization-service/#123" aria-description="Citation for case: Boutilier v. Immigration &amp; Naturalization Service">387 U. S. 118, 123</a></span> (1967)). In exercising this power, Congress has adopted a policy of apprehending illegal aliens at or near the border and deporting them promptly. Border Patrol agents are authorized by statute to make warrantless arrests of aliens suspected of “attempting to enter the United States in violation of . . . law,” <span class="citation no-link">8 U. S. C. § 1357</span>(a)(2), and are directed to examine them without “unnecessary delay” to determine whether “there is prima facie evidence establishing” their attempted illegal entry. <span class="citation no-link">8 CFR §287.3</span> (1982). Aliens against whom such evidence exists may be granted immediate voluntary departure from the country. See <span class="citation no-link">8 U. S. C. § 1252</span>(b); <span class="citation no-link">8 CFR §242.5</span>(a)(2)(i) (1982). Thus, Congress has determined that prompt deportation, such as occurred in this case, constitutes the most effective method for curbing the enormous flow of illegal aliens across our southern border.<footnotemark>5</footnotemark></p>
<p id="b903-4"><page-number citation-index="1" label="865">*865</page-number>In addition to satisfying immigration policy, the prompt deportation of alien witnesses who are determined by the Government to possess no material evidence relevant to a criminal trial is justified by several practical considerations. During fiscal year 1979, almost one-half of the more than 11,000 inmates incarcerated in federal facilities in the Southern District of California were material witnesses who had neither been charged with nor convicted of a criminal offense. App. 18. The average period of detention for such witnesses exceeded 5 days, and many were detained for more than 20 days. <span class="citation no-link"><em>Id., </em>at 20</span>. The resulting overcrowded conditions forced the Government to house many detainees in federal facilities located outside the Southern District of California or in state-operated jails. <span class="citation no-link"><em>Id., </em>at 21-22</span>; Brief for United States 19. Thus, the detention of alien eyewitnesses imposes substantial financial and physical burdens upon the Government, not to mention the human cost to potential witnesses who are incarcerated though charged with no crime. In addition, the rule adopted by the Court of Appeals significantly constrains the Government’s prosecutorial discretion. As explained by the United States:</p>
<blockquote id="b903-5">“Because of budget limitations and the unavailability of adequate detention facilities, it is simply impossible as a practical matter to prosecute many cases involving the transportation or harboring of large numbers of illegal aliens, where all the aliens must be incarcerated for a substantial period of time to avoid dismissal of the charges, even though the prosecution’s case may be overwhelming. As a consequence, many valid and appropriate prosecutions are foregone.” <span class="citation no-link"><em>Id., </em>at 21-22</span>.</blockquote>
<p id="b903-6">It simply will not do, therefore, to minimize the Government’s dilemma in cases like this with statements such as “[t]he prosecution may not deny access to a witness by hiding <page-number citation-index="1" label="866">*866</page-number>him out. See <em>Freeman </em>v. <em>State of Georgia, </em><span class="citation" data-id="366422"><a href="/opinion/366422/holman-freeman-v-state-of-georgia/" aria-description="Citation for case: Holman Freeman v. State of Georgia">599 F. 2d 65</a></span> (5th Cir. 1979) (police detective concealed location of witness).” Brief for Respondent 35. Congress’ immigration policy and the practical considerations discussed above demonstrate that the Government had good reason to deport respondent’s passengers once it concluded that they possessed no evidence relevant to the prosecution or the defense of respondent’s criminal charge. No onus, in the sense of “hiding out” or “concealing” witnesses, attached to the Government by reason of its discharge of the obligations imposed upon it by Congress; its exercise of these manifold responsibilities is not to be judged by standards which might be appropriate if the Government’s only responsibility were to prosecute criminal offenses.</p>
<p id="b904-5">Ill</p>
<p id="b904-6">Viewing the Government’s conduct in this light, we turn to the evaluation of the Court of Appeals’ “conceivable benefit” test. There seems to us to be little doubt that this test is a virtual <em>“per se” </em>rule which requires little if any showing on the part of the accused defendant that the testimony of the absent witness would have been either favorable or material. As we said with respect to a similar test — phrased in terms of information “that might affect the jury’s verdict” — for determining when a prosecutor must disclose information to a criminal defendant:</p>
<blockquote id="b904-7">“If everything that might influence a jury must be disclosed, the only way a prosecutor could discharge his constitutional duty would be to allow complete discovery of his files as a matter of routine practice.” <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#109" aria-description="Citation for case: United States v. Agurs">427 U. S. 97, 109</a></span> (1976).</blockquote>
<p id="b904-8">So it is with the “conceivable benefit” test. Given the vagaries of a typical jury trial, it would be a bold statement indeed to say that the testimony of any missing witness could not have “conceivably benefited” the defense. To us, the <page-number citation-index="1" label="867">*867</page-number>number of situations which will satisfy this test is limited only by the imaginations of judges or defense counsel.<footnotemark>6</footnotemark></p>
<p id="b905-5">A</p>
<p id="b905-6">The only recent decision of this Court dealing with the right to compulsory process guaranteed by the Sixth Amendment suggests that more than the mere absence of testimony is necessary to establish a violation of the right. See <em>Washington </em>v. <em>Texas, </em><span class="citation" data-id="9423455"><a href="/opinion/107481/washington-v-texas/" aria-description="Citation for case: Washington v. Texas">388 U. S. 14</a></span> (1967). Indeed, the Sixth Amendment does not by its terms grant to a criminal defendant the right to secure the attendance and testimony of any and all witnesses: it guarantees him “compulsory process for obtaining <em>witnesses in his favor.” </em>U. S. Const., Arndt. 6 (emphasis added). In <em><span class="citation" data-id="9423455"><a href="/opinion/107481/washington-v-texas/" aria-description="Citation for case: Washington v. Texas">Washington</a></span>, </em>this Court found a violation of this Clause of the Sixth Amendment when the defendant was arbitrarily deprived of “testimony [that] would have been <em>relevant </em>and <em>material, </em>and . . . <em>vital </em>to the defense.” <span class="citation" data-id="9423455"><a href="/opinion/107481/washington-v-texas/#16" aria-description="Citation for case: Washington v. Texas">388 U. S., at 16</a></span> (emphasis added). This language suggests that respondent cannot establish a violation of his constitutional right to compulsory process merely by showing that deportation of the passengers deprived him of their testimony. He must at least make some plausible showing of how their testimony would have been both material and favorable to his defense.<footnotemark>7</footnotemark></p>
<p id="b905-7">When we turn from <em><span class="citation" data-id="9423455"><a href="/opinion/107481/washington-v-texas/" aria-description="Citation for case: Washington v. Texas">Washington</a></span> </em>to other cases in what might loosely be called the area of constitutionally guaranteed access to evidence, we find <em>Washington's </em>intimation of a <page-number citation-index="1" label="868">*868</page-number>materiality requirement more than borne out. <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), held “that the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution.” <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland"><em>Id., </em>at 87</a></span>. This materiality requirement was emphasized in <em>Moore </em>v. <em>Illinois, </em><span class="citation" data-id="9425027"><a href="/opinion/108613/moore-v-illinois/" aria-description="Citation for case: Moore v. Illinois">408 U. S. 786</a></span> (1972), where we stated that a defendant will prevail upon a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>claim “where the evidence is favorable to the accused and is material either to guilt or to punishment.” <em>Id., </em>at 794. And in <em>United States </em>v. <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs, supra,</a></span> </em>we noted that “[a] fair analysis of the holding in <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>indicates that implicit in the requirement of materiality is a concern that the suppressed evidence might have affected the outcome of the trial.” <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#104" aria-description="Citation for case: Brady v. Maryland"><em>Id., </em>at 104</a></span>. We further explained:</p>
<blockquote id="b906-5">“The proper standard of materiality must reflect our overriding concern with the justice of the finding of guilt. . . . This means that the omission must be evaluated in the context of the entire record. If there is no reasonable doubt about guilt whether or not the additional evidence is considered, there is no justification for a new trial. On the other hand, if the verdict is already of questionable validity, additional evidence of relatively minor importance might be sufficient to create a reasonable doubt.” <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#112" aria-description="Citation for case: Brady v. Maryland"><em>Id., </em>at 112-113</a></span> (footnotes omitted).</blockquote>
<p id="b906-6">Similarly, when the Government has been responsible for delay resulting in a loss of evidence to the accused, we have recognized a constitutional violation only when loss of the evidence prejudiced the defense. In <em>United States </em>v. <em>Marion, </em><span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/" aria-description="Citation for case: United States v. Marion">404 U. S. 307</a></span> (1971), for example, the Court held that preindictment delay claims were governed by the Due Process Clause of the Fifth Amendment, not by the speedy-trial guarantee of the Sixth Amendment. Elaborating on the nature of the guarantee provided by the Due Process Clause <page-number citation-index="1" label="869">*869</page-number>in such cases, the Court emphasized the requirement of materiality:</p>
<blockquote id="b907-5">“Nor have appellees adequately demonstrated that the pre-indictment delay by the Government violated the Due Process Clause. No actual prejudice to the conduct of the defense is alleged or proved, and there is no showing that the Government intentionally delayed to gain some tactical advantage over appellees or to harass them.” <span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#325" aria-description="Citation for case: United States v. Marion"><em>Id., </em>at 325</a></span>.</blockquote>
<p id="b907-6">Five Terms later, in <em>United States </em>v. <em>Lovasco, </em><span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/" aria-description="Citation for case: United States v. Lovasco">431 U. S. 783</a></span> (1977), we summarized this aspect of <em><span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/" aria-description="Citation for case: United States v. Marion">Marion</a></span>:</em></p>
<blockquote id="b907-7">“Thus <em><span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/" aria-description="Citation for case: United States v. Marion">Marion</a></span> </em>makes clear that proof of prejudice is generally a necessary but not sufficient element of a due process claim, and that the due process inquiry must consider the reasons for the delay as well as the prejudice to the accused.” <em>Id., </em>at 790.</blockquote>
<p id="b907-8">The same “prejudice” requirement has been applied to cases of postindictment “delay. In <em>Barker </em>v. <em>Wingo, </em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">407 U. S. 514</a></span> (1972), the Court set forth several factors to be considered in determining whether an accused has been denied his Sixth Amendment right to a speedy trial by the Government’s pretrial delay. One of the four factors identified by the Court, and a factor more fully discussed in <em>United States </em>v. <em>MacDonald, </em><span class="citation" data-id="109838"><a href="/opinion/109838/united-states-v-macdonald/#858" aria-description="Citation for case: United States v. MacDonald">435 U. S. 850, 858-859</a></span> (1978), was whether there had been any “prejudice to the defendant from the delay.” <span class="citation" data-id="109838"><a href="/opinion/109838/united-states-v-macdonald/#858" aria-description="Citation for case: United States v. MacDonald"><em>Id., </em>at 858</a></span>. Although the Court recognized that prejudice may take the form of “ ‘oppressive pretrial incarceration’” or “‘anxiety and concern of the accused,’” the “‘most serious’” consideration, analogous to considerations in this case, was impairment of the ability to mount a defense. See <em>ibid, </em>(quoting <em>Barker </em>v. <span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/#532" aria-description="Citation for case: Barker v. Wingo"><em>Wingo, supra, </em>at 532</a></span>). Thus, other interests protected by the Sixth Amendment look to the degree of prejudice incurred by a defendant as a result of governmental action or inaction.</p>
<p id="b908-4"><page-number citation-index="1" label="870">*870</page-number>The principal difference between these cases in related areas of the law and the present case is that respondent simply had no access to the witnesses who were deported after he was criminally charged. Respondent contends that requiring him to show materiality is unreasonable in light of the fact that neither he nor his attorney was afforded an opportunity to interview the deported witnesses to determine what favorable information they possessed. But while this difference may well support a relaxation of the specificity required in showing materiality, we do not think that it affords the basis for wholly dispensing with such a showing.</p>
<p id="b908-5">The closest case in point is <em>Roviaro </em>v. <em>United States, </em><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">353 U. S. 53</a></span> (1957). While <em><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">Roviaro</a></span> </em>was not decided on the basis of constitutional claims, its subsequent affirmation in <em>McCray </em>v. <em>Illinois, </em><span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300</a></span> (1967), where both due process and confrontation claims were considered by the Court, suggests that <em><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">Roviaro</a></span> </em>would not have been decided differently if those claims had actually been called to the Court’s attention.</p>
<p id="b908-6"><em><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">Roviaro</a></span> </em>deals with the obligation of the prosecution to disclose to the defendant the name of an informer-eyewitness, and was cast in terms of the traditional governmental privilege to refuse disclosure of such an identity. The <em><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">Roviaro</a></span> </em>Court held that the informer’s identity had to be disclosed, but only after it concluded that the informer’s testimony would be highly relevant:</p>
<blockquote id="b908-7">“This is a case where the Government’s informer was the sole participant, other than the accused, in the transaction charged. The informer was the only witness in a position to amplify or contradict the testimony of government witnesses. Moreover, a government witness testified that [the informer] denied knowing petitioner or ever having seen him before. We conclude that, under these circumstances, the trial court committed prejudicial error in permitting the Government to withhold the identity of its undercover employee in the face of re<page-number citation-index="1" label="871">*871</page-number>peated demands by the accused for his disclosure.” <span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/#64" aria-description="Citation for case: Roviaro v. United States">353 U. S., at 64-65</a></span>.</blockquote>
<p id="b909-6">“What <em><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">Roviaro</a></span> </em>thus makes clear is that this Court was unwilling to impose any absolute rule requiring disclosure of an informer’s identity,” <em>McCray </em>v. <em>Illinois, supra, </em>at 311, despite the fact that criminal defendants otherwise have no access to such informers to determine what relevant information they possess. <em><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">Roviaro</a></span> </em>supports the conclusion that while a defendant who has not had an opportunity to interview a witness may face a difficult task in making a showing of materiality, the task is not an impossible one. In such circumstances it is of course not possible to make any avowal of <em>how </em>a witness may testify. But the events to which a witness might testify, and the relevance of those events to the crime charged, may well demonstrate either the presence or absence of the required materiality.</p>
<p id="b909-7">In addition, it should be remembered that respondent was present throughout the commission of this crime. No one knows better than he what the deported witnesses actually said to him, or in his presence, that might bear upon whether he knew that Romero-Morales was an illegal alien who had entered the country within the past three years. And, in light of the actual charge made in the indictment, it was only the status of Romero-Morales which was relevant to the defense. Romero-Morales, of course, remained fully available for examination by the defendant and his attorney. We thus conclude that the respondent can establish no Sixth Amendment violation without making some plausible explanation of the assistance he would have received from the testimony of the deported witnesses.<footnotemark>8</footnotemark></p>
<p id="b910-4"><page-number citation-index="1" label="872">*872</page-number>B</p>
<p id="b910-5">Having borrowed much of our reasoning with respect to the Compulsory Process Clause of the Sixth Amendment from cases involving the Due Process Clause of the Fifth Amendment, we have little difficulty holding that at least the same materiality requirement obtains with respect to a due process claim. Due process guarantees that a criminal defendant will be treated with “that fundamental fairness essential to the very concept of justice. In order to declare a denial of it we must find that the absence of that fairness fatally infected the trial; the acts complained of must be of such quality as necessarily prevents a fair trial.” <em>Lisenba </em>v. <em>California, </em><span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#236" aria-description="Citation for case: Lisenba v. California">314 U. S. 219, 236</a></span> (1941). In another setting, we recognized that Jencks Act violations, wherein the Government withholds evidence required by statute to be disclosed, rise to the level of due process violations only when they so infect the fairness of the trial as to make it “more a spectacle or trial by ordeal than a disciplined contest.” <em>United States </em>v. <em>Augenblick, </em><span class="citation" data-id="107821"><a href="/opinion/107821/united-states-v-augenblick/#356" aria-description="Citation for case: United States v. Augenblick">393 U. S. 348, 356</a></span> (1969) (citations omitted). Such an absence of fairness is not made out by the Government’s deportation of the witnesses in this case unless there is some explanation of how their testimony would have been favorable and material. See <em>United States </em>v. <em>Lovasco, </em><span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/" aria-description="Citation for case: United States v. Lovasco">431 U. S. 783</a></span> (1977); <em>United States </em>v. <em>Marion, </em><span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/" aria-description="Citation for case: United States v. Marion">404 U. S. 307</a></span> (1971).</p>
<p id="b910-6">IV</p>
<p id="b910-7">To summarize, the responsibility of the Executive Branch faithfully to execute the immigration policy adopted by Congress justifies the prompt deportation of illegal-alien witnesses upon the Executive’s good-faith determination that they possess no evidence favorable to the defendant in a criminal prosecution. The mere fact that the Government <page-number citation-index="1" label="873">*873</page-number>deports such witnesses is not sufficient to establish a violation of the Compulsory Process Clause of the Sixth Amendment or the Due Process Clause of the Fifth Amendment. A violation of these provisions requires some showing that the evidence lost would be both material and favorable to the defense.</p>
<p id="b911-5">Because prompt deportation deprives the defendant of an opportunity to interview the witnesses to determine precisely what favorable evidence they possess, however, the defendant cannot be expected to render a detailed description of their lost testimony. But this does not, as the Court of Appeals concluded, relieve the defendant of the duty to make some showing of materiality. Sanctions may be imposed on the Government for deporting witnesses only if the criminal defendant makes a plausible showing that the testimony of the deported witnesses would have been material and favorable to his defense, in ways not merely cumulative to the testimony of available witnesses. In some cases such a showing may be based upon agreed facts, and will be in the nature of a legal argument rather than a submission of additional facts. In other cases the criminal defendant may advance additional facts, either consistent with facts already known to the court or accompanied by a reasonable explanation for their inconsistency with such facts, with a view to persuading the court that the testimony of a deported witness would have been material and favorable to his defense.<footnotemark>9</footnotemark> Because in the latter situation the explanation of materiality is testimonial in nature, and constitutes evidence of the prejudice incurred as a result of the deportation, it should be verified by oath or affirmation of either the defendant or his attorney. See Fed. Rule Evid. 603; Fed. Rule Crim. Proc. 47.</p>
<p id="b911-6">As in other cases concerning the loss of material evidence, sanctions will be warranted for deportation of alien witnesses <page-number citation-index="1" label="874">*874</page-number>only if there is a reasonable likelihood that the testimony could have affected the judgment of the trier of fact. See <em>Giglio </em>v. <em>United States, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 154</a></span> (1972). In making such a determination, courts should afford some leeway for the fact that the defendant necessarily proffers a description of the material evidence rather than the evidence itself. Because determinations of materiality are often best made in light of all of the evidence adduced at trial, judges may wish to defer ruling on motions until after the presentation of evidence.<footnotemark>10</footnotemark></p>
<p id="b912-4">In this case the respondent made no effort to explain what material, favorable evidence the deported passengers would have provided for his defense. Under the principles set forth today, he' therefore failed to establish a violation of the Fifth or Sixth Amendment, and the District Court did not err in denying his motion to dismiss the indictment. Accordingly, the judgment of the Court of Appeals is</p>
<p id="b912-5">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b898-4"> Section 1324(a)(2) applies to “[a]ny person” who “transports, or moves, or attempts to transport or move,” “any alien,” “knowing that [the alien] is in the United States in violation of law, and knowing or having reasonable grounds to believe that his last entry into the United States occurred less than three years prior” to the transportation or attempted transportation with which the person is charged.</p>
</footnote>
<footnote label="2">
<p id="b898-5"> Other Courts of Appeals have adopted slight variations of the position held by the Court of Appeals for the Ninth Circuit. See, <em>e. g., United States </em>v. <em>Armijo-Martinez, </em><span class="citation" data-id="9468847"><a href="/opinion/399129/united-states-v-carlos-armijo-martinez-and-carlos-armijo-deleon/" aria-description="Citation for case: United States v. Carlos Armijo-Martinez and Carlos...">669 F. 2d 1131</a></span> (CA6 1982); <em>United States </em>v. <em>Rose, </em><span class="citation" data-id="398897"><a href="/opinion/398897/united-states-v-robert-rose-sr-united-states-of-america-v-james-hill/" aria-description="Citation for case: United States v. Robert Rose, Sr., United States of...">669 F. 2d 23</a></span> (CA1 1982); <em>United States </em>v. <em>Avila-Dominguez, </em><span class="citation" data-id="372539"><a href="/opinion/372539/united-states-v-maximo-avila-dominguez-albert-perez-evangeline-salazar/" aria-description="Citation for case: United States v. Maximo Avila-Dominguez, Albert Perez,...">610 F. 2d 1266</a></span> (CA5 1980); <em>United States </em>v. <em>Calzada, </em><span class="citation" data-id="8907202"><a href="/opinion/8918744/united-states-v-calzada/" aria-description="Citation for case: United States v. Calzada">579 F. 2d 1358</a></span> (CA7 1978).</p>
</footnote>
<footnote label="3">
<p id="b900-6"> The joint appendix contains excerpts of transcribed testimony from a hearing on June 2, 1980, at which the District Court heard arguments of counsel and the testimony of Romero-Morales. At the conclusion of this testimony, counsel for respondent proposed the highly unusual step of calling the Assistant United States Attorney as a witness. App. 45. The attorney testified at further proceedings held on June 12, 1980, and was interrogated, <em>inter alia, </em>about his understanding of various decisions of the Court of Appeals for the Ninth Circuit and about the Government’s litigating strategy in these cases. <em>Id., </em>at 63-64. This procedure seems to us highly unusual, if not bizarre; ordinarily the litigating strategies of the United States Attorney are no more the subject of permissible inquiry by his opponent than would be the litigating strategies of the Public Defender by his opponent.</p>
</footnote>
<footnote label="4">
<p id="b900-7"> As the Court of Appeals explained:</p>
<p id="b900-8">“The conceivable benefit in <em><span class="citation" data-id="9457477"><a href="/opinion/299642/united-states-v-manuel-mendez-rodriguez/" aria-description="Citation for case: United States v. Manuel Mendez-Rodriguez">Mendez-Rodriguez</a></span> </em>stemmed from the fact that the deported aliens were eyewitnesses to, and active participants in, the crime charged, so that there was a strong possibility that they could have provided material and relevant evidence concerning the events constituting the crime. Conversely, where a missing deported alien was not an <page-number citation-index="1" label="863">*863</page-number>eyewitness to the offense, we have been unwilling to assume that the alien’s testimony could conceivably benefit the defendant.” <span class="citation" data-id="389588"><a href="/opinion/389588/united-states-v-ricardo-valenzuela-bernal/#74" aria-description="Citation for case: United States v. Ricardo Valenzuela-Bernal">647 F. 2d, at 74</a></span> (citation and footnotes omitted).</p>
<p id="b901-5">As described by the Court of Appeals, the “conceivable benefit” test “impose[s] no requirement of government misconduct or negligence before dismissal of an indictment is warranted. Nor is a defendant required to show specific prejudice caused by the unavailability of the alien eyewitnesses.” <em>Ibid, </em>(citation omitted). Other Courts of Appeals have recognized the Ninth Circuit rule as requiring no showing of prejudice, <em>United States </em>v. <em>Calzada, </em><span class="citation" data-id="8907202"><a href="/opinion/8918744/united-states-v-calzada/#1362" aria-description="Citation for case: United States v. Calzada">579 F. 2d, at 1362</a></span>, and as permitting dismissal of the indictment even when the “ ‘record is completely devoid of anything which would suggest that the testimony of any one, or more, of the deported persons would have been helpful’ to the defendants.” <em>United States </em>v. <em>Avila-Dominguez, </em><span class="citation" data-id="372539"><a href="/opinion/372539/united-states-v-maximo-avila-dominguez-albert-perez-evangeline-salazar/" aria-description="Citation for case: United States v. Maximo Avila-Dominguez, Albert Perez,...">610 F. 2d, at 1269</a></span>-1270 (quoting <em>United States </em>v. <em>Mendez-Rodriguez, </em><span class="citation" data-id="9457477"><a href="/opinion/299642/united-states-v-manuel-mendez-rodriguez/#6" aria-description="Citation for case: United States v. Manuel Mendez-Rodriguez">450 F. 2d 1, 6</a></span> (CA9 1971) (Kilkenny, J., dissenting)).</p>
</footnote>
<footnote label="5">
<p id="b902-6"> As evidence of the effectiveness of Congress’ policy and of the colossal problem presented by illegal entries from Mexico, the United States notes that approximately one million illegal aliens were detained by Border Pa<page-number citation-index="1" label="865">*865</page-number>trol officials during each of the three years preceding 1981. Brief for United States 19; see U. S. Department of Justice, Internal Audit Report, U. S. Border Patrol Management of the Mexican Border 1, 6 (Jan. 1981).</p>
</footnote>
<footnote label="6">
<p id="b905-8"> See n. 4, <em>supra.</em></p>
</footnote>
<footnote label="7">
<p id="b905-9"> That the Sixth Amendment does not guarantee criminal defendants the right to compel the attendance of any and all witnesses is reflected in the Federal Rules of Criminal Procedure. Rule 17(b) requires the Government to subpoena witnesses on behalf of indigent defendants, but only “upon a satisfactory showing. . . that the presence of the witness is necessary to an adequate defense.” See also <em>Isaacs </em>v. <em>United States, </em><span class="citation" data-id="94272"><a href="/opinion/94272/isaacs-v-united-states/#489" aria-description="Citation for case: Isaacs v. United States">159 U. S. 487, 489</a></span> (1895); <em>Crumpton </em>v. <em>United States, </em><span class="citation" data-id="92957"><a href="/opinion/92957/crumpton-v-united-states/#364" aria-description="Citation for case: Crumpton v. United States">138 U. S. 361, 364-365</a></span> (1891).</p>
</footnote>
<footnote label="8">
<p id="b909-8"> Respondent’s knowledge of the truth distinguishes this ease from <em>United States </em>v. <em>Burr, </em><span class="citation" data-id="8638368"><a href="/opinion/8658517/united-states-v-burr/" aria-description="Citation for case: United States v. Burr">25 F. Cas. 187</a></span> (No. 14,694) (CC Va. 1807), a ease cited by respondent in support of his argument that it is unreasonable to require him to explain the relevance of the missing testimony. In <em><span class="citation" data-id="8638368"><a href="/opinion/8658517/united-states-v-burr/" aria-description="Citation for case: United States v. Burr">Burr</a></span>, </em>Chief Justice Marshall found it unreasonable to require Aaron Burr to explain the relevancy of General Wilkinson’s letter to President Jefferson, <page-number citation-index="1" label="872">*872</page-number>upon which the President’s allegations of treason were based, precisely because Burr had never read the letter and was unaware of its contents. In this case, respondent observed the passengers, heard their comments, and is fully aware of the ways in which they influenced his knowledge about the status of Romero-Morales.</p>
</footnote>
<footnote label="9">
<p id="b911-7"> In adopting this standard, we express no opinion on the showing which a criminal defendant must make in order to obtain compulsory process for securing the attendance at his criminal trial of witnesses within the United States.</p>
</footnote>
<footnote label="10">
<p id="b912-8"> The counsel of <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#112" aria-description="Citation for case: United States v. Agurs">427 U. S. 97, 112-113</a></span> (1976), is helpful here:</p>
<p id="b912-9">“[T]he omission must be evaluated in the context of the entire record. If there is no reasonable doubt about guilt whether or not additional evidence is considered, there is no justification for a new trial. On the other hand, if the verdict is already of questionable validity, additional evidence of relatively minor importance might be sufficient to create a reasonable doubt.”</p>
</footnote>
</opinion>
```

---
