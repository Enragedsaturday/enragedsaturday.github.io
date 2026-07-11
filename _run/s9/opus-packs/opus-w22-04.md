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

## GROUP: _overhaul2/lake/cases/albright-v-oliver--112924.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0a4484d8a687c4c4", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "albright-v-oliver--112924"}, "payload": {"all": [{"cite": "510 U.S. 266", "page": "266", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "510"}, {"cite": "114 S. Ct. 807", "page": "807", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "114"}, {"cite": "127 L. Ed. 2d 114", "page": "114", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "127"}, {"cite": "1994 U.S. LEXIS 1319", "page": "1319", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1994"}], "display": null, "official": null, "official_selection_present": false, "record_id": "albright-v-oliver--112924"}}
{"assertion_id": "d70a53993385c3d5", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "albright-v-oliver--112924"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "albright-v-oliver--112924", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — albright-v-oliver--112924

```json
{
  "schema_version": "s2.v1",
  "record_id": "albright-v-oliver--112924",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Albright v. Oliver",
    "case_name_short": "Albright",
    "case_name_full": "ALBRIGHT v. OLIVER Et Al.",
    "input_case_name": "Albright v. Oliver",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1994-01-24",
    "year": 1994,
    "docket": "No. 92-833",
    "cluster_id": 112924,
    "lead_opinion_id": 9432926,
    "sibling_ids": [],
    "absolute_url": "/opinion/112924/albright-v-oliver/",
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
        "cite": "510 U.S. 266",
        "volume": "510",
        "reporter": "U.S.",
        "page": "266",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "114 S. Ct. 807",
        "volume": "114",
        "reporter": "S. Ct.",
        "page": "807",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "127 L. Ed. 2d 114",
        "volume": "127",
        "reporter": "L. Ed. 2d",
        "page": "114",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1994 U.S. LEXIS 1319",
        "volume": "1994",
        "reporter": "U.S. LEXIS",
        "page": "1319",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "510 U.S. 266",
        "volume": "510",
        "reporter": "U.S.",
        "page": "266",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "114 S. Ct. 807",
        "volume": "114",
        "reporter": "S. Ct.",
        "page": "807",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "127 L. Ed. 2d 114",
        "volume": "127",
        "reporter": "L. Ed. 2d",
        "page": "114",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1994 U.S. LEXIS 1319",
        "volume": "1994",
        "reporter": "U.S. LEXIS",
        "page": "1319",
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
    "date_created": "2026-07-06T13:42:08Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:42:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:42:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:42:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:42:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — albright-v-oliver--112924

```
<opinion type="majority">
<author id="b472-5">Chief Justice Rehnquist</author>
<judges id="Az88">announced the judgment of the Court and delivered an opinion, in which Justice O’Connor, Justice Scalia, and Justice Ginsburg join.</judges>
<p id="b472-6">A warrant was issued for petitioner’s arrest by Illinois authorities, and upon learning of it he surrendered and was released on bail. The prosecution was later dismissed on the ground that the charge did not state an offense under Illinois law. Petitioner asks us to recognize a substantive right under the Due Process Clause of the Fourteenth Amendment to be free from criminal prosecution except upon probable cause. We decline to do so.</p>
<p id="b472-7">We review a decision of the Court of Appeals for the Seventh Circuit affirming the grant of a motion to dismiss the complaint pursuant to Federal Rule of Civil Procedure 12(b)(6), and we must therefore accept the well-pleaded allegations of the complaint as true. Illinois authorities issued an arrest warrant for petitioner Kevin Albright, charging him on the basis of a previously filed criminal information with the sale of a substance which looked like an illegal drug. When he learned of the outstanding warrant, petitioner surrendered to respondent, Roger Oliver, a police detective employed by the city of Macomb, but denied his guilt of such an offense. He was released after posting bond, one of the conditions of which was that he not leave the State without permission of the court.<footnotemark>1</footnotemark></p>
<p id="b473-4"><page-number citation-index="1" label="269">*269</page-number>At a preliminary hearing, respondent Oliver testified that petitioner sold the look-alike substance to Moore, and the court found probable cause to bind petitioner over for trial. At a later pretrial hearing, the court dismissed the criminal action against petitioner on the ground that the charge did not state an offense under Illinois law.</p>
<p id="b473-5">Albright then instituted this action under Rev. Stat. § 1979,<span class="citation no-link">42 U. S. C. § 1983</span>, against Detective Oliver in his individual and official capacities, alleging that Oliver deprived him of substantive due process under the Fourteenth Amendment — his “liberty interest” — to be free from criminal prosecution except upon probable cause.<footnotemark>2</footnotemark> The District Court granted respondent’s motion to dismiss under Rule 12(b)(6) on the ground that the complaint did not state a claim under § 1983.<footnotemark>3</footnotemark> The Court of Appeals for the Seventh Circuit affirmed, <span class="citation multiple-matches"><a href="/c/F.%202d/975/343/">975 F. 2d 343</a></span> (1992), relying on our decision in <em>Paul </em>v. <em>Davis, </em><span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/" aria-description="Citation for case: Paul v. Davis">424 U. S. 693</a></span> (1976). The Court of Appeals held that prosecution without probable cause is a constitutional tort actionable under §1983 only if accompanied by incarceration or loss of employment or some other “palpable <page-number citation-index="1" label="270">*270</page-number>consequenc[e].” 975 F. 2d, at 346-347. The panel of the Seventh Circuit reasoned that “just as in the garden-variety public-officer defamation case that does not result in exclusion from an occupation, state tort remedies should be adequate and the heavy weaponry of constitutional litigation can be left at rest.” <em>Id., </em>at 347.<footnotemark>4</footnotemark> We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./507/959/">507 <page-number citation-index="1" label="271">*271</page-number>U. S. 959</a></span> (1993), and while we affirm the judgment below, we do so on different grounds. We hold that it is the Fourth Amendment, and not substantive due process, under which petitioner Albright’s claim must be judged.</p>
<p id="b475-5">Section 1983 “is not itself a source of substantive rights,” but merely provides “a method for vindicating federal rights elsewhere conferred.” <em>Baker </em>v. <em>McCollan, </em><span class="citation" data-id="9427663"><a href="/opinion/110132/baker-v-mccollan/#144" aria-description="Citation for case: Baker v. McCollan">443 U. S. 137, 144, n. 3</a></span> (1979). The first step in any such claim is to identify the specific constitutional right allegedly infringed. <em>Graham </em>v. <em>Connor, </em><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#394" aria-description="Citation for case: Graham v. Connor">490 U. S. 386, 394</a></span> (1989); and <em>Baker </em>v. <span class="citation" data-id="9427663"><a href="/opinion/110132/baker-v-mccollan/#140" aria-description="Citation for case: Baker v. McCollan"><em>McCollan, supra, </em>at 140</a></span>.</p>
<p id="b475-6">Petitioner’s claim before this Court is a very limited one. He claims that the action of respondents infringed his substantive due process right to be free of prosecution without probable cause. He does not claim that Illinois denied him the procedural due process guaranteed by the Fourteenth Amendment. Nor does he claim a violation of his Fourth Amendment rights, notwithstanding the fact that his surrender to the State’s show of authority constituted a seizure for purposes of the Fourth Amendment. <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19</a></span> (1968); <em>Brower </em>v. <em>County of Inyo, </em><span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/#596" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo">489 U. S. 593, 596</a></span> (1989).<footnotemark>5</footnotemark></p>
<p id="b475-7">We begin analysis of petitioner’s claim by repeating our observation in <em>Collins </em>v. <em>Harker Heights, </em><span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/#125" aria-description="Citation for case: Collins v. City of Harker Heights">503 U. S. 115, 125</a></span> (1992). “As a general matter, the Court has always been reluctant to expand the concept of substantive due process <page-number citation-index="1" label="272">*272</page-number>because the guideposts for responsible decisionmaking in this unchartered area are scarce and open-ended.” The protections of substantive due process have for the most part been accorded to matters relating to marriage, family, procreation, and the right to bodily integrity. See, <em>e. g., Planned Parenthood of Southeastern Pa. </em>v. <em>Casey, </em><span class="citation" data-id="9432680"><a href="/opinion/112786/planned-parenthood-of-southeastern-pa-v-casey/#847" aria-description="Citation for case: Planned Parenthood of Southeastern Pa. v. Casey">505 U. S. 833, 847-849</a></span> (1992) (describing cases in which substantive due process rights have been recognized). Petitioner’s claim to be free from prosecution except on the basis of probable cause is markedly different from those recognized in this group of cases.</p>
<p id="b476-5">Petitioner relies on our observations in cases such as <em>United States </em>v. <em>Salerno, </em><span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/#746" aria-description="Citation for case: United States v. Salerno">481 U. S. 739, 746</a></span> (1987), and <em>Daniels </em>v. <em>Williams, </em><span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/#331" aria-description="Citation for case: Daniels v. Williams">474 U. S. 327, 331</a></span> (1986), that the Due Process Clause of the Fourteenth Amendment confers both substantive and procedural rights. This is undoubtedly true, but it sheds little light on the scope of substantive due process. Petitioner points in particular to language from <em>Hurtado </em>v. <em>California, </em><span class="citation" data-id="9417375"><a href="/opinion/91054/hurtado-v-california/#527" aria-description="Citation for case: Hurtado v. California">110 U. S. 516, 527</a></span> (1884), later quoted in <em><span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/" aria-description="Citation for case: Daniels v. Williams">Daniels, supra,</a></span> </em>stating that the words “by the law of the land” from the Magna Carta were “ ‘intended to secure the individual from the arbitrary exercise of the powers of government.’” This, too, may be freely conceded, but it does not follow that, in all of the various aspects of a criminal prosecution, the only inquiry mandated by the Constitution is whether, in the view of the Court, the governmental action in question was “arbitrary.”</p>
<p id="b476-6"><em><span class="citation" data-id="9417375"><a href="/opinion/91054/hurtado-v-california/" aria-description="Citation for case: Hurtado v. California">Hurtado</a></span> </em>held that the Due Process Clause did not make, applicable to the States the Fifth Amendment’s requirement that all prosecutions for an infamous crime be instituted by the indictment of a grand jury. In the more than 100 years which have elapsed since <em><span class="citation" data-id="9417375"><a href="/opinion/91054/hurtado-v-california/" aria-description="Citation for case: Hurtado v. California">Hurtado</a></span> </em>was decided, the Court has concluded that a number of the procedural protections contained in the Bill of Rights were made applicable to the States by the Fourteenth Amendment. See <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), overruling <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. <page-number citation-index="1" label="273">*273</page-number>25</a></span> (1949), and holding the Fourth Amendment’s exclusionary rule applicable to the States; <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964), overruling <em>Twining </em>v. <em>New Jersey, </em><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">211 U. S. 78</a></span> (1908), and holding the Fifth Amendment’s privilege against self-incrimination applicable to the States; <em>Benton </em>v. <em>Maryland, </em><span class="citation" data-id="9424099"><a href="/opinion/107980/benton-v-maryland/" aria-description="Citation for case: Benton v. Maryland">395 U. S. 784</a></span> (1969), overruling <em>Palko </em>v. <em>Connecticut, </em><span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319</a></span> (1937), and holding the Double Jeopardy Clause of the Fifth Amendment applicable to the States; <em>Gideon </em>v. <em>Wainwright, </em><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span> (1963), overruling <em>Betts </em>v. <em>Brady, </em><span class="citation" data-id="103694"><a href="/opinion/103694/betts-v-brady/" aria-description="Citation for case: Betts v. Brady">316 U. S. 455</a></span> (1942), and holding that the Sixth Amendment’s right to counsel was applicable to the States. See also <em>Klopfer </em>v. <em>North Carolina, </em><span class="citation" data-id="9423364"><a href="/opinion/107369/klopfer-v-north-carolina/" aria-description="Citation for case: Klopfer v. North Carolina">386 U. S. 213</a></span> (1967) (Sixth Amendment speedy trial right applicable to the States); <em>Washington </em>v. <em>Texas, </em><span class="citation" data-id="9423455"><a href="/opinion/107481/washington-v-texas/" aria-description="Citation for case: Washington v. Texas">388 U. S. 14</a></span> (1967) (Sixth Amendment right to compulsory process applicable to the States); <em>Duncan </em>v. <em>Louisiana, </em><span class="citation" data-id="9423691"><a href="/opinion/107685/duncan-v-louisiana/" aria-description="Citation for case: Duncan v. Louisiana">391 U. S. 145</a></span> (1968) (Sixth Amendment right to jury trial applicable to the States).</p>
<p id="b477-4">This course of decision has substituted, in these areas of criminal procedure, the specific guarantees of the various provisions of the Bill of Rights embodied in the first 10 Amendments to the Constitution for the more generalized language contained in the earlier cases construing the Fourteenth Amendment. It was through these provisions of the Bill of Rights that their Framers sought to restrict the exercise of arbitrary authority by the Government in particular situations. Where a particular Amendment “provides an explicit textual source of constitutional protection” against a particular sort of government behavior, “that Amendment, not the more generalized notion of ‘substantive due process,’ must be the guide for analyzing these claims.” <em>Graham </em>v. <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#395" aria-description="Citation for case: Graham v. Connor"><em>Connor, supra, </em>at 395</a></span>.<footnotemark>6</footnotemark></p>
<p id="b478-4"><page-number citation-index="1" label="274">*274</page-number>We think this principle is likewise applicable here. The Framers considered the matter of pretrial deprivations of liberty and drafted the Fourth Amendment to address it. The Fourth Amendment provides:</p>
<blockquote id="b478-5">“The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”</blockquote>
<p id="b478-6">We have in the past noted the Fourth Amendment’s relevance to the deprivations of liberty that go hand in hand with criminal prosecutions. See <em>Gerstein </em>v. <em>Pugh, </em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#114" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 114</a></span> (1975) (holding that the Fourth Amendment requires a judicial determination of probable cause as a prerequisite to any extended restraint on liberty following an arrest). We have said that the accused is not “entitled to judicial oversight or review of the decision to prosecute.” <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#118" aria-description="Citation for case: Gerstein v. Pugh"><em>Id., </em>at 118-119</a></span>. See also <em>Beck </em>v. <em>Washington, </em><span class="citation" data-id="9422400"><a href="/opinion/106391/beck-v-washington/#545" aria-description="Citation for case: Beck v. Washington">369 U. S. 541, 545</a></span> (1962); <em>Lem Woon </em>v. <em>Oregon, </em><span class="citation" data-id="97944"><a href="/opinion/97944/lem-woon-v-oregon/" aria-description="Citation for case: Lem Woon v. Oregon">229 U. S. 586</a></span> (1913). But here petitioner was not merely charged; he submitted himself to arrest.</p>
<p id="b479-4"><page-number citation-index="1" label="275">*275</page-number>We express no view as to whether petitioner’s claim would succeed under the Fourth Amendment, since he has not presented that question in his petition for certiorari. We do hold that substantive due process, with its “scarce and open-ended” “guideposts,” <em>Collins </em>v. <em>Harker Heights, </em><span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/#125" aria-description="Citation for case: Collins v. City of Harker Heights">503 U. S., at 125</a></span>, can afford him no relief.<footnotemark>7</footnotemark></p>
<p id="b479-5">The judgment of the Court of Appeals is therefore</p>
<p id="b479-6">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b472-10"> Before the criminal information was filed, one Veda Moore, an undercover informant, had told Oliver that she bought cocaine from one John Albright, Jr., at a student hotel in Macomb. The “cocaine” turned out to <page-number citation-index="1" label="269">*269</page-number>be baking powder, however, and the grand jury indicted John Albright, Jr., for selling a “look-alike” substance. When Detective Oliver went to serve the arrest warrant, he discovered that John Albright, Jr., was a retired pharmacist in his sixties, and apparently realized he was on a false scent. After discovering that it could not have been the elderly Al-bright’s son, John David, who was involved in the incident, Detective Oliver contacted Moore to see if the sale was actually made by petitioner Kevin Albright, a second son of John Albright, Jr. Moore confirmed that petitioner Kevin Albright made the sale.</p>
</footnote>
<footnote label="2">
<p id="b473-7"> The complaint also named the city of Macomb as a defendant to the §1983 action and charged a common-law malicious prosecution claim against Detective Oliver.</p>
</footnote>
<footnote label="3">
<p id="b473-8"> The District Court also held that Detective Oliver was entitled to a defense of qualified immunity, and that the complaint failed to allege facts sufficient to support municipal liability against the city of Macomb. The District Court also dismissed without prejudice the common-law claim of malicious prosecution against Detective Oliver. These issues are not before this Court.</p>
</footnote>
<footnote label="4">
<p id="b474-5"><em> </em>As noted by the Court of Appeals below, the extent to which a claim of malicious prosecution is actionable under § 1983 is one “on which there is an embarrassing diversity of judicial opinion.” 975 F. 2d, at 345, citing <em>Brummett </em>v. <em>Camble, </em><span class="citation" data-id="570053"><a href="/opinion/570053/jay-brummett-v-jimmy-camble-jim-boles-doug-sanders-dan-boulware-john/#1180" aria-description="Citation for case: Jay Brummett v. Jimmy Camble, Jim Boles, Doug Sanders,...">946 F. 2d 1178, 1180, n. 2</a></span> (CA5 1991) (cataloging divergence of approaches by the Courts of Appeals). Most of the lower courts recognize some form of malicious prosecution action under § 1983. The disagreement among the courts concerns whether malicious prosecutions, standing alone, can violate the Constitution. The most expansive approach is exemplified by the Third Circuit, which holds that the elements of a malicious prosecution action under § 1983 are the same as the common-law tort of malicious prosecution. See, <em>e. g., Lee </em>v. <em>Mihalich, </em><span class="citation multiple-matches"><a href="/c/F.%202d/847/66/">847 F. 2d 66</a></span>, 70 (1988) (“[T]he elements of liability for the constitutional tort of malicious prosecution under § 1983 coincide with those of the common law tort”). See also <em>Sanders </em>v. <em>English, </em><span class="citation" data-id="573101"><a href="/opinion/573101/floyd-sanders-iii-v-don-english-curtis-mccoy-ed-perry-and-the-city-of/#1159" aria-description="Citation for case: Floyd Sanders, III v. Don English, Curtis McCoy Ed Perry,...">950 F. 2d 1152, 1159</a></span> (CA5 1992) (“[0]ur circuit recognizes causes of action under § 1983 for false arrest, illegal detention . . . and malicious prosecution” because these causes of action “implicate the constitutional ‘guarantees of the fourth and fourteenth amendments’ ”); <em>Robinson </em>v. <em>Maruffi, </em><span class="citation" data-id="536136"><a href="/opinion/536136/van-bering-robinson-v-john-maruffi-joseph-polisar-clarence-kraemer-and/" aria-description="Citation for case: Van Bering Robinson v. John Maruffi, Joseph Polisar,...">895 F. 2d 649</a></span> (CA10 1990); <em>Strength </em>v. <em>Hubert, </em><span class="citation" data-id="510193"><a href="/opinion/510193/martha-s-strength-v-wl-hubert-charles-carroll-individually-william/#426" aria-description="Citation for case: Martha S. Strength v. W.L. Hubert, Charles Carroll,...">854 F. 2d 421, 426</a></span>, and n. 5 (CA11 1988) (recognizing that “freedom from malicious prosecution is a federal right protected by § 1983”). Other Circuits, however, require a showing of some injury or deprivation of a constitutional magnitude in addition to the traditional elements of common-law malicious prosecution. The exact standards announced by the courts escape easy classification. See, <em>e. g., Torres </em>v. <em>Superintendent of Police of Puerto Rico, </em><span class="citation" data-id="534774"><a href="/opinion/534774/jose-antonio-torres-v-superintendent-of-the-police-of-puerto-rico/#409" aria-description="Citation for case: Jose Antonio Torres v. Superintendent of the Police of...">893 F. 2d 404, 409</a></span> (CA1 1990) (the challenged conduct must be “so egregious that it violated substantive or procedural due process rights under the Fourteenth Amendment”); <em>Usher </em>v. <em>Los Angeles, </em><span class="citation" data-id="493965"><a href="/opinion/493965/sterling-usher-v-city-of-los-angeles-richard-a-gonzales-michael-e/#561" aria-description="Citation for case: Sterling Usher v. City of Los Angeles, Richard A....">828 F. 2d 556, 561-562</a></span> (CA9 1987) (“[T]he general rule is that a claim of malicious prosecution is not cognizable under <span class="citation no-link">42 U. S. C. § 1983</span> if process is available within the state judicial system to provide a remedy .... However, ‘an exception exists to the general rule when a malicious prosecution is conducted with the intent to deprive a person of equal protection of the laws or is otherwise intended to subject a person to a denial of constitutional rights’ ”); <em>Coogan </em>v. <em>Wixom, </em><span class="citation" data-id="489359"><a href="/opinion/489359/edward-coogan-and-margaret-coogan-v-city-of-wixom-bruce-kirby-and-philip/#175" aria-description="Citation for case: Edward Coogan and Margaret Coogan v. City of Wixom, Bruce...">820 F. 2d 170, 175</a></span> (CA6 1987) (in addition to elements of malicious prosecution under <page-number citation-index="1" label="271">*271</page-number>state law, plaintiff must show an egregious misuse of a legal proceeding resulting in a constitutional deprivation). In holding that malicious prosecution is not actionable under § 1983 unless it is accompanied by incarceration, loss of protected status, or some other palpable consequence, the Seventh Circuit’s decision below places it in this latter camp. In view of our disposition of this case, it is evident that substantive due process may not furnish the constitutional peg on which to hang such a “tort.”</p>
</footnote>
<footnote label="5">
<p id="b475-9"> Thus, Albright may have missed the statute of limitations for any claim he had based on an unconstitutional arrest or seizure. <span class="citation multiple-matches"><a href="/c/F.%202d/975/343/">975 F. 2d 343</a></span>, 345 (CA7 1992). We express no opinion as to the timeliness of any such claim he might have.</p>
</footnote>
<footnote label="6">
<p id="b477-5">Justice Stevens’ dissent faults us for ignoring, <em>inter alia, </em>our decision in <em>In re Winship, </em><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">397 U. S. 358</a></span> (1970). <em><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span> </em>undoubtedly rejected the notion that all of the required incidents of a fundamentally fair trial were to be found in the provisions of the Bill of Rights, but it did so as a matter of procedural due process: “ ‘This notion [that the government must prove <page-number citation-index="1" label="274">*274</page-number>the elements of a criminal case beyond a reasonable doubt] — basic in our law and rightly one of the boasts of a free society — is a requirement and a safeguard of due process of law in the historic, procedural content of “due process.’”” <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#362" aria-description="Citation for case: In Re WINSHIP"><em>Id., </em>at 362</a></span>, quoting <em>Leland </em>v. <em>Oregon, </em><span class="citation" data-id="9420774"><a href="/opinion/105024/leland-v-oregon/#802" aria-description="Citation for case: Leland v. Oregon">343 U. S. 790, 802-803</a></span> (1952) (Frankfurter, J., dissenting).</p>
<p id="b478-8">Similarly, other cases relied on by the dissent, including <em>Mooney </em>v. <em>Holohan, </em><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103</a></span> (1935), <em>Napue </em>v. <em>Illinois, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264</a></span> (1959), <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), <em>Giglio </em>v. <em>United States, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">405 U. S. 150</a></span> (1972), and <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">427 U. S. 97</a></span> (1976), were accurately described in the latter opinion as “dealing with the defendant’s right to a fair trial mandated by the Due Process Clause of the Fifth Amendment to the Constitution.” <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#107" aria-description="Citation for case: United States v. Agurs"><em>Id., </em>at 107</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b479-10"> Petitioner appears to have argued in the Court of Appeals some variant of a violation of his constitutional right to interstate travel because of the condition imposed upon him pursuant to his release on bond. But he has not presented any such question in his petition for certiorari and has not briefed the issue here. We therefore do not consider it.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/beautiful-struggle-v-baltimore-police-dep-t--uf407874b.json  (`lake-record`, 1 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7a2cfaa930122d37", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "beautiful-struggle-v-baltimore-police-dep-t--uf407874b"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "beautiful-struggle-v-baltimore-police-dep-t--uf407874b", "scope_note": null, "varies_by_point": false}}
```

### lake record — beautiful-struggle-v-baltimore-police-dep-t--uf407874b

```json
{
  "schema_version": "s2.v1",
  "record_id": "beautiful-struggle-v-baltimore-police-dep-t--uf407874b",
  "stub": true,
  "status": "not_found",
  "identity": {
    "case_name": null,
    "case_name_short": null,
    "case_name_full": null,
    "input_case_name": "Beautiful Struggle v. Baltimore Police Dep't",
    "court": "4th Cir. 2021",
    "court_id": null,
    "court_level": null,
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": null,
    "docket": null,
    "cluster_id": null,
    "lead_opinion_id": null,
    "sibling_ids": [],
    "absolute_url": null,
    "identity_method": "not_found",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": null,
    "alternates": [],
    "reason_code": "frontier_no_candidate_cluster"
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": null,
      "selected": null,
      "reason": null
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
    "scope_note": null,
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
    "date_created": "2026-07-06T05:44:10Z",
    "date_modified": "2026-07-06T05:44:10Z",
    "warnings": [
      "frontier not_found requires web/second-source cross-check before fabrication inference"
    ],
    "field_provenance": {
      "identity": {
        "src": "pending",
        "at": "2026-07-06T05:44:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "pending",
        "at": "2026-07-06T05:44:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "pending",
        "at": "2026-07-06T05:44:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "pending",
        "at": "2026-07-06T05:44:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

---

## GROUP: _overhaul2/lake/cases/black-v-united-states--107287.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b02d4b9a68e10b6f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "black-v-united-states--107287"}, "payload": {"all": [{"cite": "385 U.S. 26", "page": "26", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "385"}, {"cite": "87 S. Ct. 190", "page": "190", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "87"}, {"cite": "17 L. Ed. 2d 26", "page": "26", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "17"}, {"cite": "1966 U.S. LEXIS 2943", "page": "2943", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1966"}, {"cite": "18 A.F.T.R.2d (RIA) 5886", "page": "5886", "reporter": "A.F.T.R.2d (RIA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "18"}], "display": null, "official": null, "official_selection_present": false, "record_id": "black-v-united-states--107287"}}
{"assertion_id": "82d1d3623bda466a", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "black-v-united-states--107287"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "black-v-united-states--107287", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — black-v-united-states--107287

```json
{
  "schema_version": "s2.v1",
  "record_id": "black-v-united-states--107287",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Black v. United States",
    "case_name_short": "Black",
    "case_name_full": "Black v. United States",
    "input_case_name": "Black v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1966-11-07",
    "year": 1966,
    "docket": null,
    "cluster_id": 107287,
    "lead_opinion_id": 9423273,
    "sibling_ids": [],
    "absolute_url": "/opinion/107287/black-v-united-states/",
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
        "cite": "385 U.S. 26",
        "volume": "385",
        "reporter": "U.S.",
        "page": "26",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 190",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "190",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 26",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "26",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 A.F.T.R.2d (RIA) 5886",
        "volume": "18",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "5886",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1966 U.S. LEXIS 2943",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "2943",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "385 U.S. 26",
        "volume": "385",
        "reporter": "U.S.",
        "page": "26",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 190",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "190",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 26",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "26",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1966 U.S. LEXIS 2943",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "2943",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 A.F.T.R.2d (RIA) 5886",
        "volume": "18",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "5886",
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
    "date_created": "2026-07-06T13:52:04Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:52:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:52:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:52:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:52:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — black-v-united-states--107287

```
<opinion data-order="7" data-type="opinion" id="x999-1" type="majority">
<author id="b130-12">Per Curiam.</author>
<p id="b130-13">In <em>Davis </em>v. <em>United States, post, </em>p. 927, we today denied the- petition for certiorari. The sole question raised there (but not passed upon by the Court of Appeals because not necessary to its disposition) involved petitioners’ claim that conferences between petitioners and their counsel were surreptitiously overheard <page-number citation-index="1" label="27">*27</page-number>and intercepted by law enforcement officials through concealed monitorial devices built into the jail where petitioners were being held for federal authorities. The Solicitor General did not deny the existence of the devices but said that there were no recordings of the conversations in question. He pointed out that since the case has been remanded by the Court of Appeals for a new trial on other grounds, a full exploration of this question could be made on retrial. In the light of these representations we denied the petition for certiorari so that the question might be fully explored at the new trial, as suggested by the Solicitor General.</p>
<p id="b131-5">In the instant case, <em>Black </em>v. <em>United States, </em>the petition for rehearing now raises a similar question and while <em>Davis </em>v. <em>United States, supra, </em>is not controlling, its relation is obvious. In <em>Black </em>the Solicitor General advised the Court voluntarily on May 24, 1966, after the petition for certiorari had been denied, <span class="citation multiple-matches"><a href="/c/U.%20S./384/927/">384 U. S. 927</a></span>, but before an application for rehearing had been filed, that agents of the Federal Bureau of Investigation, in a matter unrelated to this case, on February 7, 1963, installed a listening device in petitioner’s hotel suite in Washington, D. C. The device monitored and taped conversations held in the hotel suite during the period the offense was being investigated and beginning some two months before and continuing until about one month after the evidence in this case was presented to the Grand Jury. During that period, “the monitoring agents,” the Solicitor General advised, “overheard, among other conversations, exchanges between petitioner and the attorney who was then representing him [Black]” in this case. In a supplemental memorandum filed July 13, 1966, the Solicitor General, in response to an inquiry by the Court, stated that the recordings of such interceptions had been erased from the tapes but that notes summarizing and sometimes <page-number citation-index="1" label="28">*28</page-number>quoting the conversations intercepted were available, and that reports and memoranda concerning the same had been made. “Neither the reports nor the memoranda,” he reported, “were seen by attorneys of the Tax Division responsible for the prosecution of” this case until January 1964, when in preparing for trial they were included in material transmitted to them; the reports and memo-randa of the intercepted conversations were examined by the Tax Division attorneys and retained by them until April 15, 1964, when petitioner’s trial began; and the attorneys never realized until April 21, 1966, that any conversations between Black and his attorney had been overheard and included in the transcriptions.</p>
<p id="b132-6">The Solicitor General advised further that the “Tax Division attorneys found nothing in the F. B. I. reports or memoranda which they considered relevant to the tax evasion case.” He suggests that the judgment be vacated and remanded to the District Court in which the “relevant materials would be produced and the court would determine, upon an adversary hearing, whether petitioner’s conviction should stand.” We have sometimes used this technique in federal criminal cases, <em>United States </em>v. <em>Shotwell Mfg. Co., </em><span class="citation" data-id="9421525"><a href="/opinion/105597/united-states-v-shotwell-manufacturing-co/" aria-description="Citation for case: United States v. Shotwell Manufacturing Co.">355 U. S. 233</a></span>. However, its use has never been automatic. Indeed, in <em>Remmer </em>v. <em>United States, </em><span class="citation" data-id="105202"><a href="/opinion/105202/remmer-v-united-states/" aria-description="Citation for case: Remmer v. United States">347 U. S. 227</a></span>, we found it necessary, despite the hearing in the District Court, to subsequently order a new trial on the merits, <span class="citation" data-id="105357"><a href="/opinion/105357/remmer-v-united-states/" aria-description="Citation for case: Remmer v. United States">350 U. S. 377</a></span>. There are other complicating factors here that were not present in <em><span class="citation" data-id="105202"><a href="/opinion/105202/remmer-v-united-states/" aria-description="Citation for case: Remmer v. United States">Remmer</a></span>. </em>There the judge had been informed of the alleged jury tampering, but here neither the judge, the petitioner nor his counsel knew of the action of the federal agents. Moreover, the Solicitor General advises that the Tax Division attorneys did not know at the time of the trial that conversations between Black and his attorney were included in the transcriptions. In view of these facts it appears that justice'requires that a <page-number citation-index="1" label="29">*29</page-number>new trial be held so as to afford the petitioner an opportunity to protect himself from the use of evidence that might be otherwise inadmissible.</p>
<p id="b133-5">This Court has never been disposed to vacate convictions without adequate justification, but, under the circumstances presented by the Solicitor Ceneral in this case we believe that a new trial must be held. This will give the parties an opportunity to present the relevant evidence and permit the trial judge to decide the questions involved. It will also permit the removal of any doubt as to Black’s receiving a fair trial with full consideration being, given to the new evidence reported to us by the Solicitor General.</p>
<p id="b133-6">The petition for rehearing is therefore granted, the order denying certiorari vacated, certiorari granted, the judgment of the Court of Appeals vacated and the cause remanded to the District Court for a new trial.</p>
<judges id="b133-7">Mr. Justice White and Mr. Justice Fortas took no part in the consideration or decision of this case.</judges>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/calero-toledo-v-pearson-yacht-leasing-co--109026.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "dbabc1640eca088e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "calero-toledo-v-pearson-yacht-leasing-co--109026"}, "payload": {"all": [{"cite": "416 U.S. 663", "page": "663", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "416"}, {"cite": "94 S. Ct. 2080", "page": "2080", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "94"}, {"cite": "40 L. Ed. 2d 452", "page": "452", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "40"}, {"cite": "1974 U.S. LEXIS 140", "page": "140", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1974"}], "display": null, "official": null, "official_selection_present": false, "record_id": "calero-toledo-v-pearson-yacht-leasing-co--109026"}}
{"assertion_id": "acf8b1f10318d987", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "calero-toledo-v-pearson-yacht-leasing-co--109026"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "calero-toledo-v-pearson-yacht-leasing-co--109026", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — calero-toledo-v-pearson-yacht-leasing-co--109026

```json
{
  "schema_version": "s2.v1",
  "record_id": "calero-toledo-v-pearson-yacht-leasing-co--109026",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Calero-Toledo v. Pearson Yacht Leasing Co.",
    "case_name_short": "Calero-Toledo",
    "case_name_full": "CALERO-TOLEDO Et Al. v. PEARSON YACHT LEASING CO.",
    "input_case_name": "Calero-Toledo v. Pearson Yacht Leasing Co.",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1974-06-17",
    "year": 1974,
    "docket": "No. 73-157",
    "cluster_id": 109026,
    "lead_opinion_id": 9425711,
    "sibling_ids": [],
    "absolute_url": "/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/",
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
        "cite": "416 U.S. 663",
        "volume": "416",
        "reporter": "U.S.",
        "page": "663",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 S. Ct. 2080",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "2080",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "40 L. Ed. 2d 452",
        "volume": "40",
        "reporter": "L. Ed. 2d",
        "page": "452",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1974 U.S. LEXIS 140",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "140",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "416 U.S. 663",
        "volume": "416",
        "reporter": "U.S.",
        "page": "663",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 S. Ct. 2080",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "2080",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "40 L. Ed. 2d 452",
        "volume": "40",
        "reporter": "L. Ed. 2d",
        "page": "452",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1974 U.S. LEXIS 140",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "140",
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
    "date_created": "2026-07-06T13:16:56Z",
    "date_modified": "2026-07-09T23:29:56Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:17:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:17:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:17:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:17:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — calero-toledo-v-pearson-yacht-leasing-co--109026

```
<opinion type="majority">
<author id="b732-9">Mr. Justice Brennan</author>
<p id="AYU">delivered the opinion of the Court.</p>
<p id="b732-10">The question presented is whether the Constitution is violated by application to appellee, the lessor of a yacht, of Puerto Rican statutes providing' for seizure and .forfeiture of vessels used for unlawful purposes when (1) the yacht was seized without prior notice or hearing after allegedly being used by a lessee for an - unlawful purpose, and (2) the appellee was neither involved in nor aware of the act of the lessee which resulted in the forfeiture.</p>
<p id="Ai0o"><page-number citation-index="1" label="665">*665</page-number>- In March 1971, appellee, Pearson Yacht Leasing Co., leased a pleasure yacht to two Puerto Rican residents. Puerto Rican authorities' discovered marihuana on board the yacht in early May 1972, and charged one of the lessees with violation of the Controlled Substances Act of Puerto Rico, P. R. Laws Ann., Tit. 24, •§ 2101 <em>et seq. </em>(Supp. 1973). On July 11,1972, the Superintendent of Police seized the yacht pursuant to P. R. Laws Ann., Tit. 24, §§ 2512 (a)(4), (b) (Supp. 1973),<footnotemark>1</footnotemark> and Tit. 34, § 1722 (1971),<footnotemark>2</footnotemark> which provide that vessels used to. <page-number citation-index="1" label="666">*666</page-number>transport, or to. facilitate the transportation of, controlled substances, .including marihuana, are subject to seizure and forfeiture to the Commonwealth <page-number citation-index="1" label="667">*667</page-number>of Puerto Rico. The vessel was seized without prior notice to appellee or either lessee and without a prior adversary hearing. The lessees, who had registered the yacht with the Ports Authority of the Commonwealth, were thereafter given notice within 10 days of the <page-number citation-index="1" label="668">*668</page-number>seizure, as required by § 1722 (a).<footnotemark>3</footnotemark> But when a challenge to the seizure was not made within 15 .days after service of the notice, the yacht was forfeited for official use of the Government of Puerto Rico pursuant to § 1722 (c).<footnotemark>4</footnotemark> Appellee shortly thereafter first learned of the seizure and forfeiture when attempting to repossess the yacht from the lessees, because of their apparent failure to pay rent.. It is conceded that appellee was. “in no way . . involved in the criminal enterprise carried oh'by : [the]' lessee” and “had no knowledge that its property was being used in connection with or in•• violation of [Puerto Rican Law].”</p>
<p id="b736-4">. Qfi November 6, 1972, appellee filed this suit, seeking a» declaration that application of P. R. Laws'Ann., Tit. 24, §§ 2512 (a)(4), (b), and Tit.- 34, § 1722, had(l) unconstitutionally denied it due process of law insofar as the statutes authorized appellants, the Superintendent of Police.and the Chief of the Office of Transportation of the Commonwealth, to seize the yacht without notice or a prior adversary hearing, and (2) unconstitutionally deprived appellee of its property without just compensation.<footnotemark>5</footnotemark> Injunctive relief was also sought.</p>
<p id="b737-2"><page-number citation-index="1" label="669">*669</page-number>A three-judge District Court,<footnotemark>6</footnotemark> relying principally upon <em>Fuentes </em>v. <em>Shevin, </em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67</a></span> (1972), held that the. failure of the statutes to provide for preseizure notice and hearing rendered them constitutionally defective. <span class="citation" data-id="8807912"><a href="/opinion/8823179/pearson-yacht-leasing-co-v-massa/#1342" aria-description="Citation for case: Pearson Yacht Leasing Co. v. Massa">363 F. Supp. 1337, 1342-1343</a></span> (PR 1973). Viewing <em>United States </em>v. <em>United States Coin &amp; Currency, </em><span class="citation" data-id="9424510"><a href="/opinion/108303/united-states-v-united-states-coin-currency/" aria-description="Citation for case: United States v. United States Coin &amp; Currency">401 U. S. 715</a></span> (1971), as having effectively overruled our prior decisions that the property owner’s innocence has no constitutional significance for purposes of forfeiture, the District Court further declared that the Puerto Rican statutes, insofar as applied to forfeit appellee’s interest in the yacht, unconstitutionally deprived it of property without just compensation. <span class="citation" data-id="8807912"><a href="/opinion/8823179/pearson-yacht-leasing-co-v-massa/#1341" aria-description="Citation for case: Pearson Yacht Leasing Co. v. Massa">363 F. Supp., at 1341-1342</a></span>. Appellants were ^accordingly enjoined from enforcing the statutes “insofar as they deny the owner or person in charge of property an opportunity for a hearing due to the lack of notice, before the seizure and forfeiture of its property and insofar as a penalty is imposed upon innocent parties.” <span class="citation" data-id="8807912"><a href="/opinion/8823179/pearson-yacht-leasing-co-v-massa/#1343" aria-description="Citation for case: Pearson Yacht Leasing Co. v. Massa"><em>Id., </em>at 1343-1344</a></span>. We noted probable jurisdiction. <span class="citation multiple-matches"><a href="/c/U.%20S./414/816/">414 U. S. 816</a></span> (1973). We reverse.</p>
<p id="b737-3">I</p>
<p id="b737-4">Although the parties consented to the convening of the three-judge court and hence do not challenge our juris<page-number citation-index="1" label="670">*670</page-number>diction to decide this direct appeal, we nevertheless may not entertain the appeal under <span class="citation no-link">28 U. S. C. § 1253</span><footnotemark>7</footnotemark> unless statutes of Puerto Rico are “State statute [s]” for purposes of the Three-Judge .Court Act, <span class="citation no-link">28 U. S. C. § 2281</span>.<footnotemark>8</footnotemark> We therefore turn first to that question.</p>
<p id="b738-4">In <em>Stainback </em>v. <em>Mo Hock Ke Lok Po, </em><span class="citation" data-id="104642"><a href="/opinion/104642/stainback-v-mo-hock-ke-lok-po/" aria-description="Citation for case: Stainback v. Mo Hock Ke Lok Po">336 U. S. 368</a></span> (4949), this Court held.that enactments of the Territory of. Hawaii were not “State statute[s] <em>” </em>for purposes of Judicial Code § 266, the predecessor to <span class="citation no-link">28 U. S. C. § 2281</span>, reasoning:</p>
<blockquote id="b738-5">“While, of course, great respect is to be paid to the enactments of a territorial legislature by all courts as it is to the- adjudications of territorial courts, the predominant reason for the énactment of Judicial Code § 266 does not exist as respects territories. <em>This reason was a congressional purpose to avoid unnecessary interference with </em>the. <em>laws of a sovereign state. </em>In our dual system of government, the position of the state as sovereign over matters not ruled by the Constitution requires a deference to state <page-number citation-index="1" label="671">*671</page-number>legislative action beyond that required for the laws of a territory. A territory is subject'to congressional regulation.” <span class="citation" data-id="104642"><a href="/opinion/104642/stainback-v-mo-hock-ke-lok-po/#377" aria-description="Citation for case: Stainback v. Mo Hock Ke Lok Po">336 U. S., at 377-378</a></span> (footnotes omitted) (emphasis added).</blockquote>
<p id="b739-4">Similar reasoning — that the purpose of insulating a sovereign Spate’s laws from interference by a single judge would not be furthered by broadly interpreting the word “State” — led the Court of Appeals for the First Circuit some 55 years ago to hold § 266 inapplicable to the laws of the' Territory of Puerto Rico. <em>Benedicto </em>v. <em>West India &amp; Panama Tel. Co., </em><span class="citation" data-id="8811062"><a href="/opinion/8826249/benedicto-v-west-india-panama-telegraph-co/" aria-description="Citation for case: Benedicto v. West India &amp; Panama Telegraph Co.">256 F. 417</a></span> (1919).</p>
<p id="b739-5">Congress, however, created .the Commonwealth of Puerto Rico after <em><span class="citation" data-id="8811062"><a href="/opinion/8826249/benedicto-v-west-india-panama-telegraph-co/" aria-description="Citation for case: Benedicto v. West India &amp; Panama Telegraph Co.">Benedicto</a></span> </em>was decided. Following the Spanish-American War, Puerto Rico was ceded to this country in the Treaty of Paris, <span class="citation no-link">30 Stat. 1754</span> (1898). A brief interlude of military control Was followed by congressional enactment of a series of Organic Acts fob the government of the island. Initially these enactments established a local governmental structure with high officials appointed by the President. These Acts also retained veto power in the President, and Congress over local legislation. By 1950, however, pressures for greater autonomy led to congressional enactment of Pub. L. 600, <span class="citation no-link">64 Stat. 319</span>, which offered the people of Puerto Rico a compact whereby they might-establish a government under their own constitution. Puerto Rico accepted the compact, and on July 3, 1952, Congress approved, with minor amendments, a constitution adopted by -the Puerto Rican populace, 66 Stat.,327; see note accompanying 48 U. S. C.J 731d. Pursuant to that constitution the Commonwealth now “elects its Governor and legislature; appoints its judges, all cabinet officials, and lesser officials in the executive branch; sets its own educational policies; determines its own budget; and amends its own civil and criminal code.” Leibowitz, The Applicability of Fed-<page-number citation-index="1" label="672">*672</page-number>era! Law to the Commonwealth of Puerto Rico, 56 Geo. L. J. 219, 221 (1967); see 28 Dept. of State Bull. 584-589 (1953); <em>Americana of Puerto Rico, Inc. </em>v. <em>Kaplus, </em><span class="citation" data-id="273627"><a href="/opinion/273627/americana-of-puerto-rico-inc-v-samuel-r-kaplus-and-j-kaplus-sons/" aria-description="Citation for case: Americana of Puerto Rico, Inc. v. Samuel R. Kaplus and J....">368 F. 2d 431</a></span> (CA3 1966); Magruder, The Commonwealth Status of Puerto Rico, <span class="citation no-link">15 U. Pitt. L. Rev. 1</span> (1953).</p>
<p id="b740-4">These significant changes in Puerto Rico’s governmental structure formed the backdrop to Judge Magruder’s observations in <em>Mora </em>v. <em>Mejias, </em><span class="citation" data-id="232303"><a href="/opinion/232303/mora-v-mejias/" aria-description="Citation for case: Mora v. Mejias">206 F. 2d 377</a></span> (CA1 1953):</p>
<blockquote id="AMT">“[I]t may be that the Commonwealth of Puerto Rico — ‘El Estado Libre Asociado de Puerto Rico’ in the Spanish version — organized as a body politic by the. people of Puerto. Rico under their owp constitution,. pursuant to the terms of the compact offered to them in‘Pub. L. 600, and by them accepted, is a State-within the meaning of <span class="citation no-link">28 U. S. C. §2281</span>. The preamble to this constitution refers to the Commonwealth . . T which ‘in the- exercise of our natural rights, we [the people of Puerto Rico] now create within our union with 'the -United States of America,’ Puerto Rico has thus not become a State in the federal Union like.the 48 States, but it would seem to have become a State within a common and accepted meaning of the word. Cf. <em>State of Texas </em>v. <em>White, </em>1868, <span class="citation" data-id="9416757"><a href="/opinion/88061/texas-v-white/#721" aria-description="Citation for case: Texas v. White">7 Wall. 700, 721</a></span>. ... It is a political entity-created by the act and with the consent of the people of Puerto Rico and joined in union with the United States of America under the terms of the compact.</blockquote>
<blockquote id="b740-7">“A serious argument could therefore be made that the Commonwealth of Puerto Rico is a State within the intendment and policy of <span class="citation no-link">28 U. S. C. § 2281</span>. .. . If the constitution of the Commonwealth of Puerto Rico is really a ‘constitution’ — as the Congress says it is, <span class="citation no-link">66 Stat. 327</span>, — and- not just another Organic <page-number citation-index="1" label="673">*673</page-number>Act approved and enacted by the Congress, then the question is whether the Commonwealth of Puerto Rico is to be deemed ‘sovereign over matters not ruled by the Constitution’, of the United States and thus a ‘State’ within the policy, of <span class="citation no-link">28 U. S. C. §2281</span>, which enactment, in prescribing a'three-judge federal district court, expresses ‘a deference to. state legislative action beyond that required for- the laws of . a territory’ <em>[Stainhack </em>v. <em>Mo Hock Ke Lok Po( </em><span class="citation" data-id="104642"><a href="/opinion/104642/stainback-v-mo-hock-ke-lok-po/#378" aria-description="Citation for case: Stainback v. Mo Hock Ke Lok Po">336 U. S., at 378</a></span>]. whose local affairs are subject tó congressionál regulation.” <span class="citation" data-id="232303"><a href="/opinion/232303/mora-v-mejias/#387" aria-description="Citation for case: Mora v. Mejias">206 F. 2d, at 387-388</a></span> (footnote omitted).</blockquote>
<p id="AcJ">Lower federal courts. since 1953 have adopted ^this analysis and concluded that Puerto Rico is' to be deemed “sovereign over matters not ruled by the Constitution” and thus a State within the policy of the'Three-Judge Court Act.. See <em>Mora </em>v. <em>Mejias, </em><span class="citation" data-id="1968307"><a href="/opinion/1968307/mora-v-mejias/" aria-description="Citation for case: Mora v. Mejias">115 F. Supp. 610</a></span> (PR 1953);<footnotemark>9</footnotemark> <em>Marin </em>v. <em>University of Puerto Rico, </em><span class="citation" data-id="1878558"><a href="/opinion/1878558/marin-ex-rel-melendez-v-university-of-puerto-rico/#481" aria-description="Citation for case: Marin Ex Rel. Meléndez v. University of Puerto Rico">346 F. <page-number citation-index="1" label="674">*674</page-number>Supp. 470, 481</a></span> (PR 1972); <em>Suarez </em>v. <em>Administrador del Deporte Hipico de Puerto Rico, </em><span class="citation" data-id="1380641"><a href="/opinion/1380641/suarez-v-administrador-del-deporte-hipico-de-puerto-rico/" aria-description="Citation for case: Suarez v. Administrador Del Deporte Hipico De Puerto Rico">354 F. Supp. 320</a></span> (PR 1972). And in <em>Wackenhut Corp. </em>v. <em>Aponte, </em><span class="citation" data-id="107374"><a href="/opinion/107374/wackenhut-corp-v-aponte/" aria-description="Citation for case: Wackenhut Corp. v. Aponte">386 U. S. 268</a></span> (1967), we summarily affirmed the decision of a three-judge court for the District of Puerto Rico that had ordered abstention and said:</p>
<blockquote id="AbhR">“[Application of the doctrine of abstention is particularly appropriate in a case . . . involving] the construction and validity of a statute of the Commonwealth of Puerto Rico. For a due regard for the status of that Commonwealth under its compact with the Congress of the United States dictates, we believe, that it should have the primary opportunity through its. courts to determine the intended scope of its own legislation and. to pass upon the validity of that legislation under its own constitution as well as under the Constitution of the United States.” 266&gt;F. Supp. 401, 405 (.1966).</blockquote>
<p id="b742-6">Although the question of Puerto Rico’s status , under <span class="citation no-link">28 U. S. C. § 2281</span> was raised in neither the Jurisdictional Statement nor the Motion to Affirm in <em>Wackenhut, </em>and we do not normally feel ourselves bound by a <em>sub silentio </em>exercise of jurisdiction, see <em>Hagans </em>v. <em>Lavine, </em><span class="citation" data-id="9425636"><a href="/opinion/108987/hagans-v-lavine/#533" aria-description="Citation for case: Hagans v. Lavine">415 U. S. 528, 533-535, n. 5</a></span> (1974); <em>United States </em>v. <em>More, </em><span class="citation" data-id="6607492"><a href="/opinion/6726239/united-states-v-more/#172" aria-description="Citation for case: United States v. More">3 Cranch 159, 172</a></span> (1805), this Court has noted that in threéjudge court cases, “where . . . the responsibility [is] on the courts to see that the three-judge rule [is] followed,” unexplained action may take on added significance. <em>Stainback </em>v. <em>Mo Hock Ke Lok Po, </em><span class="citation" data-id="104642"><a href="/opinion/104642/stainback-v-mo-hock-ke-lok-po/#379" aria-description="Citation for case: Stainback v. Mo Hock Ke Lok Po">336 U. S., at 379-380</a></span>. This is particularly so, when as in <em>Wackenhut, </em>the opinion supporting the judgment over which we exercised appellate jurisdiction had expressed the view that, abstention was appropriate for reasons of comity, an oft-repeated justification for the abstention doctrine, see, <em>e. g., Railroad Comm’n of Texas </em>v. <em>Pullman Co., </em><span class="citation" data-id="103481"><a href="/opinion/103481/railroad-commn-of-tex-v-pullman-co/#500" aria-description="Citation for case: Railroad Comm&#x27;n of Tex. v. Pullman Co.">312 U. S. <page-number citation-index="1" label="675">*675</page-number>496, 500</a></span> (1941),<footnotemark>10</footnotemark> as well as the principal underpinning of the Three-Judge Court Act. See <em>Steffel </em>v. <em>Thompson, </em><span class="citation" data-id="9425630"><a href="/opinion/108985/steffel-v-thompson/#465" aria-description="Citation for case: Steffel v. Thompson">415 <em>U. </em>S. 452, 465-466</a></span> (1974).</p>
<p id="b743-4">While still of the view, that §’2281 is not “a measure of broad social policy to be construed with- great liberality,” <em>Phillips </em>v. <em>United States, </em><span class="citation" data-id="103452"><a href="/opinion/103452/phillips-v-united-states/#251" aria-description="Citation for case: Phillips v. United States">312 U. S. 246, 251</a></span> (1941), we believe that the established federal judiciál practice of' treating enactments of the Commonwealth of Puerto Rico as “State statute[s]” for purposes of the Three-Judge Court Act, serves, and does not expand, the purposes of § 2281. We therefore hold that a'three-judge court was properly convened under that statute,<footnotemark>11</footnotemark> and that direct <page-number citation-index="1" label="676">*676</page-number>appeal to this Court was proper under <span class="citation no-link">28 U. S. C. § 1253</span>. Accordingly, we now'turn to the merits.</p>
<p id="b744-5">II</p>
<p id="b744-6">Appellants challenge the District Court’s holding that the appellee was denied düe process of law by the omis<page-number citation-index="1" label="677">*677</page-number>sion from § 2512(b),,as it incorporates § 1722, of provisions for preseizure notice and hearing. They argue that seizure for purposes of forfeiture is one of those “ ‘extraordinary situations’ that justify postponing notice and opportunity for a hearing.” <em>Fuentes </em>v. <em>Shepin, </em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#90" aria-description="Citation for case: Fuentes v. Shevin">407 U. S., at 90</a></span>; see <em>Sniadach </em>v. <em>Family Finance Corp., </em><span class="citation" data-id="9424067"><a href="/opinion/107960/sniadach-v-family-finance-corp-of-bay-view/#339" aria-description="Citation for case: Sniadach v. Family Finance Corp. of Bay View">395 U. S. 337, 339</a></span> (1969); <em>Boddie </em>v. <em>Connecticut, </em><span class="citation" data-id="9424471"><a href="/opinion/108281/boddie-v-connecticut/#378" aria-description="Citation for case: Boddie v. Connecticut">401 U. S. 371, 378-379</a></span> (1971). We agree.<footnotemark>12</footnotemark></p>
<p id="b746-4"><page-number citation-index="1" label="678">*678</page-number>In holding that lack of preseizure notice and hearing denied due process, the District. Court réiied primarily upon our decision in <em>Fuentes </em>v. <em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">Shevin, supra.</a></span> Fuentes </em>involved the validity of Floridá and Pennsylvania replevin statutes permitting creditors to seize goods allegedly wrongfully detained. A writ of replevin could be obtained under the Florida statute upon the creditor’s bare assertion to a, court clerk that he was entitled to the próperty, and under the Pennsylvania statute, upon filing an .affidavit' fixing the value of the property, without alleging legal entitlement-to the property. <em>Fuentes-</em>held that the statutory procedures deprived debtors of their property without due process by failing to provide for hearings “ 'at a meaningful time.- ” <span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#80" aria-description="Citation for case: Fuentes v. Shevin">407 U. S., at 80</a></span>.</p>
<p id="b746-5"><em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">Fuentes</a></span> </em>reaffirmed, however, that, in limited circumstances, immediate seizure of a property interest, without, an opportunity for prior hearing, is constitutionally permissible. ' Such circumstances are those in which</p>
<blockquote id="b746-6">“the seizure has ,been directly fiecessary to secure an important governmental or.general public interest. Second, there has been a special need for very prompt action. Third, the State'has. képt. strict control over its monopoly of legitimate force: the person initiating the seizure has been a-government official responsible for determining, under the standards of a narrowly drawn statute, that it was necessary and justified in the particular instance.” <span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#91" aria-description="Citation for case: Fuentes v. Shevin"><em>Id., </em>at 91</a></span>.</blockquote>
<p id="b747-3"><page-number citation-index="1" label="679">*679</page-number>Thus, for example, due process is not denied when postponement of notice and hearing is necessary to protect the public from contaminated food, <em>North American Storage Co. </em>v. <em>Chicago, </em><span class="citation" data-id="96902"><a href="/opinion/96902/north-american-cold-storage-co-v-city-of-chicago/" aria-description="Citation for case: North American Cold Storage Co. v. City of Chicago">211 U. S. 306</a></span> (1908) from a bank failure, <em>Coffin Bros. &amp; Co. </em>v. <em>Bennett, </em><span class="citation" data-id="101280"><a href="/opinion/101280/coffin-brothers-co-v-bennett/" aria-description="Citation for case: Coffin Brothers &amp; Co. v. Bennett">277 U. S. 29</a></span> (1928); or from misbranded drugs, <em>Ewing </em>v. <em>Mytinger &amp; Casselberry, Inc., </em><span class="citation" data-id="9420486"><a href="/opinion/104801/ewing-v-mytinger-casselberry-inc/" aria-description="Citation for case: Ewing v. Mytinger &amp; Casselberry, Inc.">339 U. S. 594</a></span> (1950); or to aid the collection of taxes, <em>Phillips </em>v. <em>Commissioner, </em><span class="citation" data-id="101764"><a href="/opinion/101764/phillips-v-commissioner/" aria-description="Citation for case: Phillips v. Commissioner">283 U. S. 589</a></span> (1931); or the war effort, <em>United States </em>v. <em>Pfitsch, </em><span class="citation" data-id="99831"><a href="/opinion/99831/united-states-v-pfitsch/" aria-description="Citation for case: United States v. Pfitsch">256 U. S. 547</a></span> (1921).</p>
<p id="b747-4">The considerations that justified postponement of notice and hearing in those cases are present here. First, seizure under the Puerto Rican statutes serves significant governmental purposes: Seizure peripits Puerto Rico to assert <em>in rem </em>jurisdiction over the property in order to conduct forfeiture proceedings,<footnotemark>13</footnotemark> . thereby fostering the public interest in preventing continued illicit use of the property and in enforcing criminal sanctions. Second, preseizure notice and hearing might frustrate the interests served by the statutes, since the property seized — as here, a yacht — will often be of a sort that could be removed to another jurisdiction, destroyed, or concealed, if advance warning of confiscation were given. And finally, unlike the situation in <em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">Fuentes</a></span>, </em>seizure'is not initiated by self-interested private parties; rather, Commonwealth officials determine whether seizure is appropriate under the.provisions of the Puerto.Rican statutes.<footnotemark>14</footnotemark> In these circumstances, we hold that this case <page-number citation-index="1" label="680">*680</page-number>presents an “extraordinary” situation in which postponement of notice and hearing until after. seizure did not deny due process.<footnotemark>15</footnotemark></p>
<p id="b748-4">m</p>
<p id="b748-5">Appellants next argue that the District Court, erred in holding that the forfeiture statutes unconstitutionally authorized the taking for government use of innocent parties’ property without -just compensation. They urge that a long line of prior decisions of this Court éstablish the principle that statutory forfeiture schemes are not rendered unconstitutional because of their applicability to the property iñterests. of innocents, and further that <em>United States </em>v. <em>United States Coin &amp; Currency, </em><span class="citation" data-id="9424510"><a href="/opinion/108303/united-states-v-united-states-coin-currency/" aria-description="Citation for case: United States v. United States Coin &amp; Currency">401 U. S. 715</a></span> (1971), did not — contrary .to the opinion of the District Court — overrule those prior precedents <em>sub silentio. </em>We agree. The historical background, of forfeiture statutes in this country and this. Court’s prior decisions sustaining their constitutionality lead to that conclusion.</p>
<p id="b748-6">At common law the value of an inanimate object directly or indirectly causing the accidental .death of a <page-number citation-index="1" label="681">*681</page-number>King’s subject was forfeited to the Crown as a deodand.<footnotemark>16</footnotemark> The origins of the deodand are traceable to Biblical<footnotemark>17</footnotemark> and pre-Judeo-Christian practices, which reflected the view that the instrument of death was accused and,that religious expiation was required. See O. Holmes, The Common Law, c. 1 (1881). The value of the instrument was forfeited to the King, in the belief that the King would provide -the money' for Masses to be said, for the good of the dead man’s soul, or insure that the deodand was put to charitable uses. 1 W. Blackstóne, Commentaries *300.<footnotemark>18</footnotemark> When application of the deodand to religious or eleemosynary purposes ceased, and the deodand became a source of Crown revenue, the institution was justified as a penalty for carelessness.<footnotemark>19</footnotemark></p>
<p id="b750-3"><page-number citation-index="1" label="682">*682</page-number>Forfeiture also resulted at common law from conviction for felonies and treason. The convicted felon forfeited his chattels to the Crown and his lands escheated to his lord; the convicted traitor forfeited all of his property, real and personal, to the Crown. See 3 W. Holdsworth, History of English Law 68-71 (3d ed. 1927); 1 F. Pollock &amp; F. Maitland, History of English Law 351 (2d ed. 1909). The basis for these forfeitures was that a breach of the criminal law was an offense to the King’s peace, which was felt to justify denial of the right to own property. See 1 W. Blackstone, Commentaries *299.<footnotemark>20</footnotemark> •</p>
<p id="b750-4">In addition, English Law provided for statutory forfeitures of offending objects used in violation of the customs and revenue laws — likely a product of the. confluence and merger of the deodand tradition and the belief that the right to own property could be denied the wrongdoer. Statutory forfeitures were most often enforced under the <em>in rem </em>procedure utilized in the Court of Exchequer to forfeit the property of felons. See 3 W. Blackstone, Commentaries *261-262; <em>C. J. Hendry Co. </em>v. <em>Moore, </em><span class="citation" data-id="9419300"><a href="/opinion/103775/c-j-hendry-co-v-moore/#137" aria-description="Citation for case: C. J. Hendry Co. v. Moore">318 U. S. 133, 137-138</a></span> (1943).</p>
<p id="b750-5">. Deodands did not become part of the common-iaw tradition of this country. See <em>Parker-Harris Co. </em>v. <em>Tate </em><span class="citation" data-id="8301436"><a href="/opinion/8333412/parker-harris-co-v-tate/" aria-description="Citation for case: Parker-Harris Co. v. Tate">135 Tenn. 509</a></span>, <span class="citation no-link">188 S. W. 54</span> (1916). Nor <em>has </em>forfeiture <page-number citation-index="1" label="683">*683</page-number>of estates as a consequence of federal criminal conviction been permitted, see <span class="citation no-link">18 U. S. C. § 3563</span>; Rev. Stat. § 5326 (1874); <span class="citation no-link">1 Stat. 117</span> (1790). Forfeiture of estates resulting from a conviction for treason has been constitutionally proscribed by Art. Ill, s 3, though forfeitures of estates for the lifetime of a traitor have been sanctioned, see <em>Wallach </em>v. <em>Van Riswick, </em><span class="citation" data-id="89265"><a href="/opinion/89265/wallach-v-van-riswick/" aria-description="Citation for case: Wallach v. Van Riswick">92 U. S. 202</a></span> (1876). But “[l]ong before the adoption of the Constitution the common law courts in the Colonies — and later in the states during the period of Confederation — were exercising jurisdiction, <em>in rem </em>in the enforcement of [English and local] forfeiture statutes,” <em>C. J. Hendry Co. </em>v. <span class="citation" data-id="9419300"><a href="/opinion/103775/c-j-hendry-co-v-moore/#139" aria-description="Citation for case: C. J. Hendry Co. v. Moore"><em>Moore, supra, </em>at 139</a></span>, which provided’ for the forfeiture of commodities and vessels used in violations of customs and revenue laws. See <span class="citation" data-id="9419300"><a href="/opinion/103775/c-j-hendry-co-v-moore/#145" aria-description="Citation for case: C. J. Hendry Co. v. Moore"><em>id., </em>at 145-148</a></span>; <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#623" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 623</a></span> (1886). And almost immediately after adoption of the Constitution, ships and cargoes involved’ in customs offenses were made subject to forfeiture under, federal law,<footnotemark>21</footnotemark> as were vessels used to deliver slaves to foreign countries,<footnotemark>22</footnotemark> and somewhat later those used to deliver slaves to this country.<footnotemark>23</footnotemark> The enactment of forfeiture statutes has not abated; contemporary federal and state forfeiture statutes reach virtually any type of property that might be used in the conduct of a criminal enterprise.</p>
<p id="b751-4">Despite this proliferation of forfeiture enactments, the innocence of the owner of property subject’to forfeiture has almost uniformly been rejected as a defense. Thus, Mr. Justice Story observed in <em>The Palmyra, </em><span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/" aria-description="Citation for case: The Palmyra">12 Wheat. 1</a></span> (1827), that a conviction for piracy was not a prerequi<page-number citation-index="1" label="684">*684</page-number>site to a proceeding to forfeit a ship allegedly engaged in piratical aggression in violation of a federal statute:</p>
<blockquote id="b752-5">“It is well known, that at the common law, immany _ cases of felonies, the party forfeited his goods and chattels to the crown. The forfeiture did; not, strictly speaking, attach <em>in rem; </em>but it was a part, or at least a consequence, of the judgment of conviction. . . . [T]he [Crown’s right to the goods and chattels] attached only by the conviction of the offender. . . . But this doctrine never was applied to seizures and forfeitures, created by statute, <em>in rem, </em>cognizable on the revenue side of the Exchequer. The thing is here primarily considered as the offender, or rather the offence is attached primarily to the thing; and this, whether the offence be malum" <em>prohibitum, </em>or <em>malum in se </em>... . [T]he practice has been, and so this Coürt understand the law to be, that the proceeding <em>in rem </em>stands independent of, and wholly unaffected by any criminal proceeding <em>in personam.” Id., </em>at 14-15.</blockquote>
<p id="b752-6">This rationale was relied upon to sustain the statutory forfeiture of a vessel found to have been engaged in piratical conduct where the innocence of the owner was “fully established.” <em>United States </em>v. <em>Brig Malek Adhel, </em><span class="citation" data-id="86274"><a href="/opinion/86274/united-states-v-brig-malek-adhel/#238" aria-description="Citation for case: United States v. Brig Malek Adhel">2 How. 210, 238</a></span> (1844). The vessel was “treated as the offender,” without regard to the owner’s conduct,, “as the only adequate means of suppressing the offence or wrong, or insuring an indemnity to the injured party.” <span class="citation" data-id="86274"><a href="/opinion/86274/united-states-v-brig-malek-adhel/#233" aria-description="Citation for case: United States v. Brig Malek Adhel"><em>Id., </em>at 233</a></span>.<footnotemark>24</footnotemark></p>
<p id="b753-2"><page-number citation-index="1" label="685">*685</page-number><em>Dobbins’s Distillery </em>v. <em>United States, </em><span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">96 U. S. 395</a></span> (1878), is an illustration of how severely this principle has been applied. That case involved a lessee’s violations of the revenue laws which led to the seizure of real .and personal property used in connection with a distillery. The lessor’s assertions of innocence were rejected as a defense to a federal statutory forfeiture of his entire property, for the offense “attached primarily to the distillery, and the real and personal property used in connection with the same, without any regard whatsoever to the personal misconduct or responsibility of the owner, beyond what necessarily arises from the fact that he leased the property to the distiller, and suffered it to be occupied and used by the lessee as a distillery.” <span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/#401" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States"><em>Id., </em>at 401</a></span>; see <em>United States </em>v. <em>Stowell, </em><span class="citation" data-id="92645"><a href="/opinion/92645/united-states-v-stowell/#13" aria-description="Citation for case: United States v. Stowell">133 U. S. 1, 13-14</a></span> (1890).</p>
<p id="b753-3">Decisions reaching the same conclusion have continued into this century. In <em>Goldsmith-Grant Co. </em>v. <em>United States, </em><span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States">254 U. S. 505</a></span> (1921), it was held that the federal tax-fraud' forfeiture statute did not deprive an innocent owner of his property in violation of the Fifth Amendment. There, the claimant was a conditional vendor of a taxicab that had been used in the1 removal and concealment of distilled spirits upon which the federal tax was unpaid. Although recognizing that arguments against the application of the statute to (¡over an innocent owner were not without force, the Court rejected them, saying:</p>
<blockquote id="AFWZ">“In breaches of revenue provisions some forms of property, are facilities, and therefore it may be said, that Congress interposes the care and responsibility <page-number citation-index="1" label="686">*686</page-number>of their owners in aid of the prohibitions of the law and its punitive provisions, by ascribing to the property a certain personality, a power of complicity arid guilt in the wrong. In such case there is some analogy to the law óf <em>deodand </em>by which a personal chattel that was the immediate cause of the death of any reasonable creature was- forfeited. To the superstitious reason to which the rule was ascribed, Blackstone adds ‘that such misfortunes are in part owing to the negligence of the owner, and therefore he is . properly punished by such forfeiture.’ . . .</blockquote>
<blockquote id="b754-4">“But whether the reason for [the forfeiture] be artificial or real, it is too firmly fixed in the punitive and remedial jurisprudence of the country. to be. now displaced.” <span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#510" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States"><em>Id., </em>at 510-511</a></span>.</blockquote>
<p id="b754-5">See also <em>United States </em>v. <em>One Ford Coupe Automobile, </em><span class="citation" data-id="9418568"><a href="/opinion/100931/united-states-v-one-ford-coupe-automobile/" aria-description="Citation for case: United States v. One Ford Coupe Automobile">272 U. S. 321</a></span> (1926) (Brandeis, J.); <em>General Motors Acceptance Corp. </em>v. <em>United States, </em><span class="citation" data-id="101907"><a href="/opinion/101907/general-motors-acceptance-corp-v-united-states/" aria-description="Citation for case: General Motors Acceptance Corp. v. United States">286 U. S. 49</a></span> (1932) (Cardozo, J.). In <em>Van Oster </em>v. <em>Kansas, </em><span class="citation" data-id="100943"><a href="/opinion/100943/van-oster-v-kansas/" aria-description="Citation for case: Van Oster v. Kansas">272 U. S. 465</a></span> (1926),. the Court upheld, against a Fourteenth Amendment attack, a forfeiture under state law of an innocent owner’s interest in an automobile that he had entrusted to an alleged wrongdoer. Judicial inquiry into the guilt or innocence of the owner could be dispensed with, the Court held, because state lawmakers, in the exercise of the police power, were free to determine that certain uses-of property were undesirable and then establish “a secondary defense against a forbidden use . . . .” <span class="citation" data-id="100943"><a href="/opinion/100943/van-oster-v-kansas/#467" aria-description="Citation for case: Van Oster v. Kansas"><em>Id., </em>at 467</a></span>.</p>
<p id="A5V">'Plainly, the Puerto Rican forfeiture statutes further the punitive and deterrent purposes that have been found sufficient to uphold, against constitutional challenge, the application of other forfeiture statutes to the property of innocents.<footnotemark>25</footnotemark> Forfeiture of conveyances that have been <page-number citation-index="1" label="687">*687</page-number>used — and may be used again — in violation of the narcotics laws fosters the purposes served by the underlying criminal statutes, both by .preventing further illicit use of the conveyance and by imposing an economic penalty, thereby rendering illegal, behavior unprofitable. See, <em>e. g., </em>H. R. Rep. No. 1064, 76th Cong., 1st Sess. (1939); S. Rep. No. 926, 76th Cong., 1st Sess. (1939); H. R. Rep. No. 2751, 81st Cong., 2d Sess. (1950); S. Rep. No. 1755, 81st Cong., 2d Sess. (1950).<footnotemark>26</footnotemark> To. the extent that <page-number citation-index="1" label="688">*688</page-number>such forfeiture provisions are applied to lessors, bailors^ or secured creditors who are innocent of any wrongdoing, confiscation may have the desirable effect of inducing them to exercise greater care in transferring possession of their property. Cf. <em>United States </em>v. <em>One Ford Coach, </em><span class="citation" data-id="9419033"><a href="/opinion/103208/united-states-v-one-1936-model-ford-v-8-de-luxe-coach-commercial-credit/#238" aria-description="Citation for case: United States v. One 1936 Model Ford V-8 De Luxe Coach,...">307 U. S. 219, 238-241</a></span> (1939) (Douglas, J., dissenting).</p>
<p id="Av6Z">Against the legitimate governmental interests served by the Puerto Rican statutes and the long line of this Court’s decisions which squarely collide with appellee’s assertion of a constitutional violation, the District Court opposed our decision in <em>United States </em>v. <em>United States Coin &amp; Currency, </em><span class="citation" data-id="9424510"><a href="/opinion/108303/united-states-v-united-states-coin-currency/" aria-description="Citation for case: United States v. United States Coin &amp; Currency">401 U. S. 715</a></span> (1971). This reliance was misplaced. In <em>Coin &amp; Currency, </em>.the Government claimed that the; privilege against self-incrimination could not be asserted in a forfeiture proceeding under <span class="citation no-link">26 U. S. C. § 7302</span> by one in possession of money seized from him when used in an illegal bookmaking operation. In the Government’s view, the proceeding was not “criminal” because the forfeiture was authorized without regard to the guilt' or innocence of. the owner of the money. The Court’s answer was that § 7302, read in conjunction with <span class="citation no-link">19 U. S. C. § 1618</span>, manifested a clear intention “to impose a penalty only upon those who [were] significantly involved in a criminal enterprise,” 401 U. S., at 721-722, and in that circumstance the privilege could be asserted in the forfeiture proceeding by the person from- whom the money was taken. ; Thus, <em>Coin &amp; Currency </em>did not overrule prior decisions that sustained ap-. plication to innocents of forfeiture, statutes, like the Puerto Rican statutes, not limited in application to persons “significantly involved in a criminal enterprise.”</p>
<p id="b756-5">This is not to say, however, that the “broad sweep” <page-number citation-index="1" label="689">*689</page-number>of forfeiture statutes remarked in <em>Coin &amp; Currency </em>could not, in other circumstances, give rise to serious constitutional questions. Mr. Chief Justice Marshall intimated as much over a century and a half ago in observing that “a forfeiture can only be applied to those cases in which the means that are prescribed for the pievention of a forfeiture may be employed.” <em>Peisch </em>v. <em>Ware, </em><span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/#363" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C.">4 Cranch 347, 363</a></span> (1808). It therefore has been implied that it would be difficult to reject the constitutional claim of an owner whose property subjected to forfeiture had been taken from him without his privity or consent. See, <span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/#364" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C."><em>id., </em>at 364</a></span>; <em>Goldsmith-Grant Co. v. United States, </em><span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#512" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States">254 U. S., at 512</a></span>; <em>United States </em>v. <em>One Ford Coupe Automobile, </em><span class="citation" data-id="9418568"><a href="/opinion/100931/united-states-v-one-ford-coupe-automobile/#333" aria-description="Citation for case: United States v. One Ford Coupe Automobile">272 U. S., at 333</a></span>; <em>Van Oster </em>v. <em>Kansas, </em><span class="citation" data-id="100943"><a href="/opinion/100943/van-oster-v-kansas/#467" aria-description="Citation for case: Van Oster v. Kansas">272 U. S., at 467</a></span>. Similarly, the same might be said of an owner who proved not only that he was unirivolved in and unaware of the wrongful activity, but also that he had done all that reasonably could be expected to prevent the proscribed-use of his property;<footnotemark>27</footnotemark> for, in that circumstancé,.'it <page-number citation-index="1" label="690">*690</page-number>would be difficult to conclude that forfeiture served legitimate' purposes and was not unduly oppressive. Cf. <em>Armstrong </em>v. <em>United States, </em><span class="citation" data-id="9422049"><a href="/opinion/106097/armstrong-v-united-states/#49" aria-description="Citation for case: Armstrong v. United States">364 U. S. 40, 49</a></span> (1960).</p>
<p id="b758-5">But in this case appellee voluntarily entrusted the lessees with possession of the yacht, and no allegation, has been made or proof offered that the company did all that it reasonably could to avoid having its property put to an unlawful use. Cf. <em>Goldblatt </em>v. <em>Town of Hempstead, </em><span class="citation" data-id="106392"><a href="/opinion/106392/goldblatt-v-town-of-hempstead/#596" aria-description="Citation for case: Goldblatt v. Town of Hempstead">369 U. S. 590, 596</a></span> (1962). The judgment of the District Court is</p>
<p id="b758-6">
<em>Reversed.</em>
</p>
<author id="b758-7">Mr. Justice Stewart</author>
<p id="A1a">joins. Parts I and II of the-Court’s opinion, but, for the reasons stated in the dis<page-number citation-index="1" label="691">*691</page-number>senting opinion of Mk. Justice Douglas, he would hold that the- forfeiture of property belonging to an innocent and. nonnegligent owner violates the Fifth- and Fourteenth Amendments.</p>
<footnote label="1">
<p id="b733-4"> Title-24, §§2512 (a)(4) and (b) provide:</p>
<blockquote id="b733-5">“(a) The following shall be subject to forfeiture to the Commonwealth of Puerto Rico:</blockquote>
<blockquote id="b733-6">“ (4) Ali'conveyanees, including aircraft, vehicles, mount or vessels, which are used, or are intended for use, to transport, or in any manner to facilitate the transportation, sale, receipt, possession, or concealment of property described in clauses (1) and (2) of this subsection;</blockquote>
<blockquote id="b733-7">“(b) Any property subject to forfeiture under clause (4) of subsection (a) of this section shall be seized by process issued pursuant to Act No. 39, of June 4, 1960, as amended, known as the Uniform Vehicle, Mount, Vessel and Plane Seizure Act, sections 1721 and 1722 of Title 34.”</blockquote>
</footnote>
<footnote label="2">
<p id="b733-8"> Title 34, § 1722, provides:</p>
<blockquote id="b733-9">“Whenever any vehicle, mount, or other vessel or plane is seized . . . such seizure shall be conducted as follows:</blockquote>
<blockquote id="ArHK">“■(a) The proceedings shall be begun by the seizure of the property by the Secretary of Justice, the Secretary of the Treasury or-the Police Superintendent, through their delegates, policemen or other peace officers. The officer under whose authority the- action is taken shall serve notice on the owner of the property seized or the person in charge thereof or any person having any known right or interest therein, of the seizure and of the appraisal of the properties so seized, said notice to be served in an authentic manner, within ten (10) days following such seizure and such notice shall be understood to have been served upon the mailing thereof with return receipt requested. The owners, persons in charge, and <page-number citation-index="1" label="666">*666</page-number>other persons having a known interest in the property so seized may challenge the confiscation within the fifteen (15) days following the, service of the notice on them, through a complaint against the officer under whose authority the confiscation has been made, on whom notice s^all be served, and which complaint shall be filed in the Part of the Superior Court corresponding to the place where the seizure was made and shall be heard without subjection to docket. All questions that may arise shall be decided and all other proceedings shall be conducted as in an ordinary civil action. Against the judgment entered no remedy shall lie other than a certiorari before the Supreme Court, limited to issues of law. The filing of such complaint within the period herein established shall be .considered a jurisdictional prerequisite for the availing of the action herein authorized.</blockquote>
<blockquote id="b734-6">“(b) Every vehicle, mount,- or any vessel or plane <em>so </em>seized shall be appraised. as soon as taken possession of by the officer under whose authority the seizure took place, or by his delegate, with the exception of motor vehicles, which shall be placed under the custody of the Office of Transportation of the Commonwealth of Puerto Rico, which shall appraise same immediately upon receipt thereof.</blockquote>
<blockquote id="b734-7">“In the event of a judicial challenge of the seizure, the court shall, upon request of the plaintiff and after hearing the parties, determine the reasonableness of the appraisal as an incident of the challenge.</blockquote>
<blockquote id="b734-8">"Within ten (10) days after the filing of the challenge, the plaintiff shall have the.right to give bond in favor of the Commonwealth of Puerto- Rico before the pertinent court’s clerk to the satisfaction of the court, for the amount of the assessed value of the seized property, which bond may be in legal tender, by certified check, hypothecary debentures, or by insurance companies. Upon the acceptance of the bond, the court shall direct that the property be returned to the owner thereof. In such case, the provisions of the following paragraphs (c),.(d) and (e) shall not apply.</blockquote>
<blockquote id="b734-9">“When bond is accepted the subsequent substitution' of the seized property in lieu of the bond shall not be permitted, said bond to answer for the.seizure if the lawfulness of the latter is upheld, and the court shall provide in the resolution issued to that effect, -for <page-number citation-index="1" label="667">*667</page-number>the summary forfeiture execution of said bond by the clerk of the court and for the covering of such bond into the general funds of the Government of Puerto Rico in case it may be in legal tender or by certified check; the hypothecary debentures or debentures of insurance companies shall be transmitted by the pertinent clerk of the court to the Secretary of Justice for execution.</blockquote>
<blockquote id="b735-5">“(c) After fifteen (15) days have elapsed since servicé of notice of the seizure without the person or persons with. interest in the property seized have [sic] filed the corresponding challenge, or after twenty-five (25) days have elapsed since service of notice of the seizure without the court’s having directed that the seized property be returned on account of the bond to that effect having been given, the officer under whose authority the seizure took place, the delegate thereof, or the Office of Transportation, as the ease may be, may provide for the sale at auction of the seized property, or may set the same aside for official use of the Government of PuertoRico. In case the seized property cannot be sold at auction or set aside for official use of the Government, ,the property may be destroyed by the officer in charge, setting forth in a minute which he shall draw up for the purpose, the description of the property, the-reasons for its destruction and the date and place where it is destroyed, and he shall serve notice with a copy thereof on the Secretary of Justice.</blockquote>
<blockquote id="AFIq">“(d) In case the vehicle, mount, or vessel pr plane is so’d at' auction, the proceeds from the sale shall be covered into the general fund of the Government of Puerto Rico, after deducting and reimbursing expenses incurred. ' .</blockquote>
<blockquote id="b735-7">“(e) If the seizure is judicially challenged and the court declares same illegal, the Secretary of the Treasury of Puerto Rico shall, upon presentation of a certified copy of the final decision or judgment of the court, pay to the challenger the amount of the appraisal or the proceeds from the public auction sale of such property, whichever sum is the highest, plus interest thereon at the rate of 6% per annum, counting from the date of the seizure.”</blockquote>
</footnote>
<footnote label="3">
<p id="b736-5"> P. R. Laws Ann., Tit. 23, §§ 451 (e), 451b, and 451c, provide that no person shall “operate or give permission for the operation of” a vessel in Commonwealth waters without registering his interest in the vessel. Only the lessees had registered the yacht, and this led the District Court to conclude that “[f]rom the record in this case, we are not disposed to rule that the Commonwealth of PuertoRico did not have reason to believe that .[postseizure] notice to .the owner was, in fact, given.” <span class="citation" data-id="8807912"><a href="/opinion/8823179/pearson-yacht-leasing-co-v-massa/#1342" aria-description="Citation for case: Pearson Yacht Leasing Co. v. Massa">363 F. Supp. 1337, 1342</a></span> (PR 1973). Appellee does not contest this ruling.</p>
</footnote>
<footnote label="4">
<p id="b736-6"> It is agreed that the yacht was appraised at a value of $19,800, and that the Chief of the Office of Transportation of the Commonwealth purports to maintain possession of the yacht as legal-owner.</p>
</footnote>
<footnote label="5">
<p id="b736-7"> Unconstitutionality of the statutes was 'alleged under both the 'Fifth and Fourteenth Amendments. The District Court deemed it unnecessary to determine which Amendment applied to Puerto Rico,' <page-number citation-index="1" label="669">*669</page-number>see <em>Fornaris </em>v. <em>Ridge Tool Co., </em><span class="citation" data-id="108216"><a href="/opinion/108216/fornaris-v-ridge-tool-co/#43" aria-description="Citation for case: Fornaris v. Ridge Tool Co.">400 U. S. 41, 43-44</a></span> (1970), and we agree. The Joint Resolution of Congress approving the Constitution of- the Commonwealth of Puerto Rico, subjects its government to “the applicable provisions oí the Constitution of the United States,” <span class="citation no-link">66 Stat. 327</span>, and-“there cannot exist under the American rflag any governmental authority untrammeled by the requirement’s of due process of law as guaranteed by the Constitution of the United States.” <em>Mora </em>v. <em>Mejias, </em>206 E. 2d 377, 382 (CA1 1953) (Magruder, C. J.). See <span class="citation no-link">48 U. S. C. § 737</span>.</p>
</footnote>
<footnote label="6">
<p id="b737-6"> Appellants initially opposed the convening of a three-judge court, arguing that the District Court should abstain. After a hearing, appellants withdrew their opposition and consented to the convening of a three-judge court.</p>
</footnote>
<footnote label="7">
<p id="b738-6"> That section provides:</p>
<blockquote id="b738-7">“Except as otherwise provided by law, any party may appeal to the Supreme Court from an order, granting or denying, after notice and-hearing, an intérlocutory or permanent injunction in any civil action; suit or proceeding <em>required by any Act of Gongress to be heard and determined by a district court of three </em>judges.”. (Emphasis added.)</blockquote>
</footnote>
<footnote label="8">
<p id="b738-8"> That section provides:</p>
<blockquote id="ATp">“An interlocutory or permanent injunction restraining the enforce-; ment, operation or execution, of any <em>State statute </em>by restraining the áction of any Officer of- such State in the enforcement or execution of such statute or of an order made by. an administrative board or commission acting under State statutes, shall not be granted by any district court or judge thereof upon the ground of the unconstitutionality of such statute ’ unless the application therefor is heard ^nd.determined by a district court of three judges tinder section 2284 of this tille.”- (Emphasis added.) ..</blockquote>
</footnote>
<footnote label="9">
<p id="b741-5"> The court in <em>Mora </em>quoted from the statement of the United States to. the Secretary General of the United Nations explaining its decision to cease transmission of information concerning Puerto Rico under Art. 73 (e) of the United Nations Charter, which requires the. communication of certain technical information by countries, responsible .for administering territories whose people haye pot yet attained a full measure of self-government, <span class="citation" data-id="1968307"><a href="/opinion/1968307/mora-v-mejias/" aria-description="Citation for case: Mora v. Mejias">115 F. Supp., at 612</a></span>:</p>
<blockquote id="AVZ">“ ‘By the various actions taken by the Congress and the people of Puerto Rico, Congress has agreed that Puerto Rico shall have, under that Constitution, freedom from control or interference by the Congress in respect of internal government and administration, subject only to compliance with applicable provisions of the Federal Constitution, the Tuerto Rican Federal Relations Act and the acts of Congress authorizing and approving the Constitution, as may be interpreted by Judicial decision. Those laws which directed or authorized interference with matters of local government by the Féderal Government have been repealed.’ ”</blockquote>
<p id="b741-6">28 Dept. of State Bull. 584, 587 (1953). But cf. Note, Tuerto Rich; Colony or Commonwealth? 6 N. Y. U. J. Int'l L. &amp; P. 115 (1973).</p>
</footnote>
<footnote label="10">
<p id="b743-5"> See also H. Friendly, Federal Jurisdiction: A General View 93 (1973).</p>
</footnote>
<footnote label="11">
<p id="b743-6"><em> Fornaris </em>v. <em>Ridge Tool Co., </em><span class="citation" data-id="108216"><a href="/opinion/108216/fornaris-v-ridge-tool-co/" aria-description="Citation for case: Fornaris v. Ridge Tool Co.">400 U. S. 41</a></span> (1970), does not militate against this holding. There, we held that a Puerto Rican statute was not a “State statute” within <span class="citation no-link">28 U. S. C. § 1254</span> (2), which' permits appeals from judgments of federal courts of appeals holding <em>state </em>statutes unconstitutional. We noted that <span class="citation no-link">28 U. S. C. § 1258</span>, requiring that we permit final judgments of the' Supreme Court of the Commonwealth of Puerto Rico to be reviewed by appeal or by certiorari, directly corresponded to the provisions of <span class="citation no-link">28 U. S. C. §1257</span> providing for review of final judgments of “state”- courts. Since no parallel-provision was added to § 1254 (2) to permit'appeals from' the courts of appeals holding Puerto Rican statutes unconstitutional, we said:</p>
<blockquote id="b743-7">“Whether the omission was by accident or by design, our practice of strict construction of statutes authorizing appeals dictates that we not give an expansive interpretation to'the word ‘State.’ ” 400 U, S., at 42 n. 1.</blockquote>
<p id="b743-8">This conclusion seems compelled by the history of the close relationship between <span class="citation no-link">28 U. S. C. § 1254</span> (2) and <span class="citation no-link">28 U. S. C. § 1257</span>. In the Judiciary Act of 1789, <span class="citation no-link">1 Stat. 73</span>, 85-86, final decisions of state courts sustaining state statutes against challenges, under the Federal Constitution were subjected to review by this Court on writ of error. See <em>King Mfg. Co. </em>v. <em>City Council of Augusta, </em><span class="citation" data-id="9418631"><a href="/opinion/101288/king-manufacturing-co-v-city-council-of-augusta/" aria-description="Citation for case: King Manufacturing Co. v. City Council of Augusta">277 U. S. 100</a></span> (1928). But prior to 1925, there was no appeal from “final”''judgments of the federal circuit courts. See <span class="citation no-link">36 Stat. 1157</span> (1911). When con<page-number citation-index="1" label="676">*676</page-number>sideratiori was being given to amendment of the Judiciary Act in 1924 and 1925</p>
<blockquote id="AFJ">“[attention was drawn to the disparity between the want of obligatory review over [decisions of the circuit courts involving the constitutionality of state_.statutes] and the existence of obligatory jurisdiction over a similar class of cases in the state courts. Senator Copeland rehearsed before the Senate correspondence he had had on this point with the Chief Justice, who had urged that if it was desirable to put the circuit courts of appeals on the same level with the state courts, it would be better to withdraw review as of right from the state courts and subject the decisions of both the state courts and the circuit courts solely to a discretionary review by the Supreme Court, rather than to allow obligatory review over all constitutional cases from both courts. The Chief Justice, however, justified the proposed discrimination on the ground that a circuit court of appeals in- deciding a federal constitutional question ‘would be more likely to preserve the Federal view of the issue than the-State court, at least to an extent to justify making a review of its décision by our' court conditional upon. our approval.’ However, an amendment prevailed which met this discrimination by allowing •writ of error to the circuit courts of appeals in cases sustaining a constitutional claim against a state statute. The argument advanced by the Chief Justice thus became the basis for a new development of the principle. which since 1789 had been the basis of Supreme Court review of the highest courts of the states. Due to the belief that the state courts would be more jealous of local rights than of federal claims, reviéw had lain as of right where the constitutional claim was advanced and denied. _ Now, due to the belief . . . that the federal court would sustain constitutional' claims as opposed to the local right, review was provided from the circuit courts of appeals where the constitutional claim was advanced and allowed. Thereby, the Senate, ‘intended to put the two on a perfect parity, allowing a writ of error from the circuit court of appeals under <page-number citation-index="1" label="677">*677</page-number>conditions exactly the same, except reversed, and allowing a writ; of certiorari in the one case as in the other case, so that the two would be entirely harmonious.’” F. Frankfurter &amp; J. Landis, The. Business of the Supreme Court 277-278 (1928) (footnotes omitted).</blockquote>
<p id="b745-5">Thus, against that background, when Congress made § 1258 only a counterpart o'f'§ 1257, there could be no basis for an expansive reading of the word “State” in §1254(2), in the absence of its congressional amendment.</p>
<p id="b745-6">We have no occasion to address the question whether Puerto Rico is a “State” for purposes of <span class="citation no-link">28 U. S. C. § 1343</span>, a jurisdictional basis of appellee’s complaint. Since the complaint and lease agreement, as incorporated, fairly read, leave little doubt that the matter in controversy exceeds $10,000 and arises under the Constitution of- the United States, there is jurisdiction under <span class="citation no-link">28 U. S. C. § 1331</span>.</p>
</footnote>
<footnote label="12">
<p id="b745-7"> Appellants also argue that the seizure did not result-in any injury to appellee that constituted failure of preseizure' notice and hearing a denial of due process. This is so,, they contend, because the lease gave the lessees exclusive right to possession at the time of the seizure, and therefore appellee’s nonpossessory interest was adequately protected by the statutory provisions for a post-t. seizure hearing. But the lease provides that lessees’ failure, <em>inter alia, </em>within 15 days after notice from appellee to pay arrears of rent or usé the yacht solely for legal purposes would establish a default entitling appellee to possession. Whether a default had in fact occurred between May 6, 1972, when a lessee was first accused of a. narcotics violation, and the date of seizure, July 11, 1972, is.not clear from the record, although it is clear that appellee did not attempt to repossess the yacht until October 19, 1972.</p>
<p id="b745-8">Since, however, our holding is that preseizure notice and hearing are not required by due process in the .context of this forfeiture, <page-number citation-index="1" label="678">*678</page-number>we have no occasion to remand for a determination- (1) whether the company had an immediate, but as yet unexercised, right to possession on the date of seizure or merely a right to collect rents, together .with a reversionary interest, and (2) whether either or both of these ■ property interests would be of sufficient significance to require that the company be given an- advance opportunity to contest the seizure. Cf. <em>Fuentes </em>v. <em>Shevin, </em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#86" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67, 86-87</a></span> (1972).</p>
</footnote>
<footnote label="13">
<p id="b747-5"> Cf. <em>Ownbey </em>v. <em>Morgan, </em><span class="citation" data-id="99782"><a href="/opinion/99782/ownbey-v-morgan/" aria-description="Citation for case: Ownbey v. Morgan">256 U. S. 94</a></span> (1921), cited with approval in <em>Fuentes </em>v. <em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">Shevin, supra,</a></span> </em>at 91 n. 23.</p>
</footnote>
<footnote label="14">
<p id="b747-6"><em> <span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">Fuentes</a></span> </em>expressly distinguished seizure under a search warrant from seizure under a writ of replevin:</p>
<blockquote id="b747-7">“First, a search warrant is generally issued to serve a highly important governmental <em>need </em>— e. <em>g:, </em>the apprehension' and conviction of criminals — rather than the mere private advantage of a private party in an economic transaction. Second, a search warrant is <page-number citation-index="1" label="680">*680</page-number>generally issued in situations demanding prompt action. The danger is all too obvious that a criminal will destroy or hide evidence or fruits of his crime if given any prior notice. Third, the Fourth Amendment guarantees that' the State will not issue search warrants merely upon the conclusory application of a -private party. It- guarantees that the State will not abdicate control over thee issuance of warrants and that no warrant will be issued without a prior showing of probable cause.” 407 TJ. S., at 93-94, n. 30.</blockquote>
<p id="b748-8">We have no occasion to address the question whether the Fourth Amendment warrant or probable-cause requirements are applicable to seizures under the Puerto Rican statutes.</p>
</footnote>
<footnote label="15">
<p id="b748-9"> No challenge is made to the District Court’s'determination'that the form of postseizure notice satisfied due process requirements. See n. <span class="citation" data-id="9419033"><a href="/opinion/103208/united-states-v-one-1936-model-ford-v-8-de-luxe-coach-commercial-credit/" aria-description="Citation for case: United States v. One 1936 Model Ford V-8 De Luxe Coach,...">3, <em>supra. </em></a></span>Notice, of course, was required to be “ ‘reasonably-calculated’ to apprise [the company] of the pendency of the forfeiture proceedings.” <em>Robinson </em>v. <em>Hanrahan, </em><span class="citation" data-id="108624"><a href="/opinion/108624/robinson-v-hanrahan/#40" aria-description="Citation for case: Robinson v. Hanrahan">409 U. S. 38, 40</a></span> (1972).</p>
</footnote>
<footnote label="16">
<p id="b749-4"> Deodand derives from the Latin <em>Deo dandum, </em>“to be giygn to God.”</p>
</footnote>
<footnote label="17">
<p id="b749-5"> See Exodus 21:28 (“[i]f an ox gore a man or a woman, and they die, he shall be stoned: and his flesh shall not be eaten”).</p>
</footnote>
<footnote label="18">
<p id="b749-6"> See 1 M. Hale, Pleas of the Crown 419, 423-424 (1st Am. ed. 1847); 2 F. Pollock &amp; F. Maitland, History of English Law 473 (2d ed. 1909); Law of Deodands, 34 Law Mag. 188, 189 (1845); Finkelstein, The Goring Ox: Some Historical Perspectives on Deodands, Forfeitures, Wrongful Death and the Western Notion of Sovereignty, 46 Temp. L. Q. 169, 182 (1973).</p>
</footnote>
<footnote label="19">
<p id="b749-7"> See Hale, n. 18, <em>supra, </em>at 424. Indeed, the abolition of the deodand institution in England in 1846, 9 &amp; 10 Vict. c. 62, went hand in hand with the passage of Lord Campbell’s Act creating a cause of action for wrongful death, 9 &amp; 10 Vict. c. 93 (1846). Passage of the two bills was linked, because Lord Campbell was unwilling to eliminate the deodand institution, with its tendency to deter carelessness, particularly by railroads, unless a right of action was granted to the dead man’s survivors. See 77 Hansard’s Parliamentary Debates, Third Series 1031 (1845). See generally Finkelstein, n. 18, <em>supra, </em>at 170-171.</p>
<p id="b749-8">The adaptation of the deodand institution to serve the more contemporary function of deterrence is an example of a phenomenon discussed by Mr. Justice Holmes:</p>
<blockquote id="b749-9">“The customs, beliefs, or needs of a primitive time establish a rule -or a formula. In the course of centuries the custom, belief, or <page-number citation-index="1" label="682">*682</page-number>necessity disappears, but the rule remains, The reason which gave rise to the rule has been forgotten, and ingenious .minds set themselves to inquire how it is to be accounted for. Some ground of policy is thought of, which seems to explain it and to reconcile it with the present state of things; and then the rule adapts itself to the new reasons which have been found for it, and enters on. a new career. The old form receives a new content, and in time even the form modifies itself to fit the meaning which it has received.” ■ The Common Law 5 (1881). .</blockquote>
</footnote>
<footnote label="20">
<p id="b750-7"> In 1870, England eliminated most forfeitures of those convicted of felonies or treason. 33 <em>&amp; </em>34 Vict. c. 23.</p>
</footnote>
<footnote label="21">
<p id="b751-5"> Act of July 31, 1789, §§ 12, 36, <span class="citation no-link">1 Stat. 39</span>, 47; see also Act of Aug. 4, 1790, §§ 13, 22, 27, 28, 67, <span class="citation no-link">1 Stat. 157</span>, 161, 163, 176.</p>
</footnote>
<footnote label="22">
<p id="b751-6"> Act of Mar. 22, 1794, <span class="citation no-link">1 Stat. 347</span>.</p>
</footnote>
<footnote label="23">
<p id="b751-7"> Act of Mar. 2, 1807, <span class="citation no-link">2 Stat. 426</span>.</p>
</footnote>
<footnote label="24">
<p id="b752-7"> Thirty years earlier, .the Court upheld a forfeiture of a quantity of coffee which had been transferred to .bona fide purchasers, after violation of the Non-Intercourse Act of 1809, upon reasoning .that “[i]n the eternal struggle that exists between the avarice, enterprise and. combinations of individuals on the one hand, and <page-number citation-index="1" label="685">*685</page-number>the power charged with the administration of the laws on the other, severe laws are rendered necessary to enable the executive to carry into effect the measure of policy adopted by the legislature.” <em>United States </em>v. <em>1960 Bags of Coffee, </em><span class="citation" data-id="9416272"><a href="/opinion/85079/united-states-v-1960-bags-of-coffee/#405" aria-description="Citation for case: United States v. 1960 Bags of Coffee">8 Cranch 398, 405</a></span> (1814).</p>
</footnote>
<footnote label="25">
<p id="b754-7"> But for unimportant differences, P. R. Laws Ann., Tit. 24, <page-number citation-index="1" label="687">*687</page-number>§ 2512 (a) (Supp. 1973) is modeled after <span class="citation no-link">21 U. S. C. § 881</span> (a). The latter section provides:</p>
<blockquote id="b755-6">“(a) The following shall be subject to forfeiture to the United-States and no .property right shall exist in them: -</blockquote>
<blockquote id="APfQ">“(4) All conveyances, including aircraft, vehicles, or vessels, which are used, or are intended for use, to transport, or in any manner to facilitate the transportation, sale, receipt, possession, or concealment of property described in paragraph (1) or. (2), except that—</blockquote>
<blockquote id="b755-8">“(A) no conveyance used by any person, as a common carrier in the transaction of business as á. common carrier shall be forfeited under the provisions of this section unless it shall appear that the owner or other person in charge of such conveyance was a consenting party- or privy to a violation of this subchapter or-subchapter II of this chapter; and</blockquote>
<blockquote id="b755-9">“.(B) no conveyance shall be forfeited under the provisions of this- section by reason of any act or omission established' by the ownér thereof to have been committed or omitted by any person other than such owner while such conveyance was' unlawfully in the possession of a person other than the owner in violation of the criminal laws of the United States, or of any State.- . ..”</blockquote>
<p id="b755-10">See n. 1, <em>supra. </em>The exceptions contained in subparagraphs (A) and (B) of the federal statute, although having no specific counterpart in . §2512 (a)(4), have been judicially recognized by the Supreme Court of Puerto Rico. See <em>General Motors Acceptance Corp. </em>v. <em>Brañuela, </em>61 P. R. R. 701 (1943); <em>Metro Taxicabs, Inc. </em>v. <em>Treasurer of Puerto Rico, </em>73 P. R. R. 164 (1952); <em>Commonwealth </em>v. <em>Superior Court, </em>94 P. R. R. 687 (1967).</p>
</footnote>
<footnote label="26">
<p id="b755-11"> Seizure and forfeiture statutes also help compensate the Government for its enforcement efforts and provide methods for obtaining <page-number citation-index="1" label="688">*688</page-number>security for subsequently imposed penalties and fines. See, <em>e. g., One Lot Emerald Cut Stones </em>v. <em>United States, </em><span class="citation" data-id="108643"><a href="/opinion/108643/one-lot-emerald-cut-stones-and-one-ring-v-united-states/#237" aria-description="Citation for case: One Lot Emerald Cut Stones and One Ring v. United States">409 U. S. 232 237</a></span> (1972).</p>
</footnote>
<footnote label="27">
<p id="b757-5"> The common law sought to mitigate the 'harshness pf felony and deodand forfeitures. The writ of restitution was available to an individual whose goods were stolen by a thief and forfeited to the crown as a consequence of the thief’s conviction. See 2 F. Pollock &amp; F. Maitland, <em>supra, </em>n. 18, at 165-166; 3 W. Holdsworth, History of English Law 280 and n. 3 (3d ed. 1927). Mitigation with respeet'to deoda-nds was less formalized:</p>
<blockquote id="b757-6">“It seems also clear from the ancient authorities, that jurors always determined the amount of deodand to be imposed with great moderation, and with' a due regard to the rights of property .and. the moral innocence of the party incurring the. penalty. Our ancestors seem fully to have perceived the hardship of inflicting such penalty on one who had been guilty of no moral or indeed legal offence; and in all-cases, therefore, where death was purely the'result of accident, and not of negligence or carelessness, imposed a nominal fine, or found that only to' be the deodand which by its immediate contact occasioned'death.” Law of Deodands, <em>supra, </em>n. 18, at 190.</blockquote>
<p id="b757-7">Since 1790 the Federal Government’ has applied the ameliorative policy — first adopted in England', see <em>United States </em>v. Morris, <page-number citation-index="1" label="690">*690</page-number>10. Wheat. 246, 293-295 (1825) — of. providing administrative remissions' and mitigations of statutory forfeitures in most cases where the violations, are incurred “without- willful negligence” or-an intent to commit the offense. See <span class="citation no-link">1 Stat. 122</span>, c. 12 <em>(1790); </em><span class="citation no-link">1 Stat. 506</span> (1797); Rev. Stat. §§5292-5293 (1874); 19 .U. S. C. § 1618; <em>The Laura, </em><span class="citation" data-id="91384"><a href="/opinion/91384/the-laura/#414" aria-description="Citation for case: The Laura">114 U. S. 411, 414-415</a></span> (1885); <em>United States </em>v. <em>United States Coin </em>&amp; <em>Currency, </em><span class="citation" data-id="9424510"><a href="/opinion/108303/united-states-v-united-states-coin-currency/#721" aria-description="Citation for case: United States v. United States Coin &amp; Currency">401 U. S. 715, 721</a></span> (1971). Indeed, forfeitures incurred under <span class="citation no-link">21 U. S. C. § 881</span> (a), which served.as the model for enactment of the, disputed Puerto Rican statute, see n. 25, <em>supra, </em>are subject to the remission and mitigation procedures of <span class="citation no-link">19 U. S. C. § 1618</span>. See <span class="citation no-link">21 U. S. C. § 881</span> (A). Regulations implementing §1618 provide that, if the seized property was in the possession of another-who was responsible for the act which resulted in the seizure, the petitioner must produce evidence explaining the manner in which the other person acquired possession and showing that, prior to parting with the property, he did not know or have reasonable cause to believe that the property would be used in violation of the law or that the violator had a criminal record or a reputation for commercial crime. <span class="citation no-link">19 CFR §171.13</span> (a). These provisions are also extended' to those individuals holding chattel mortgages or conditional sales contracts. <span class="citation no-link">19 CFR § 171.13</span> (b). See also 18 U. g. C. § 3617 (b), establishing standards for judicial remission and mitigation of forfeitures resulting from violations of the internal revenue laws relating to liquor. , •</p>
</footnote>
</opinion>
```

---
