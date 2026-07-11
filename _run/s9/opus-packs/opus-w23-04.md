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

## GROUP: _overhaul2/lake/cases/lefkowitz-v-cunningham--109683.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8a543bc0a41dc219", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "lefkowitz-v-cunningham--109683"}, "payload": {"all": [{"cite": "431 U.S. 801", "page": "801", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "431"}, {"cite": "97 S. Ct. 2132", "page": "2132", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "97"}, {"cite": "53 L. Ed. 2d 1", "page": "1", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "53"}, {"cite": "1977 U.S. LEXIS 19", "page": "19", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1977"}], "display": null, "official": null, "official_selection_present": false, "record_id": "lefkowitz-v-cunningham--109683"}}
{"assertion_id": "ff9e19e886c662c8", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "lefkowitz-v-cunningham--109683"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "lefkowitz-v-cunningham--109683", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — lefkowitz-v-cunningham--109683

```json
{
  "schema_version": "s2.v1",
  "record_id": "lefkowitz-v-cunningham--109683",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Lefkowitz v. Cunningham",
    "case_name_short": "Lefkowitz",
    "case_name_full": "LEFKOWITZ, ATTORNEY GENERAL OF NEW YORK v. CUNNINGHAM Et Al.",
    "input_case_name": "Lefkowitz v. Cunningham",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-06-13",
    "year": 1977,
    "docket": null,
    "cluster_id": 109683,
    "lead_opinion_id": 9426845,
    "sibling_ids": [],
    "absolute_url": "/opinion/109683/lefkowitz-v-cunningham/",
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
        "cite": "431 U.S. 801",
        "volume": "431",
        "reporter": "U.S.",
        "page": "801",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 2132",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "2132",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 L. Ed. 2d 1",
        "volume": "53",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 19",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "19",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "431 U.S. 801",
        "volume": "431",
        "reporter": "U.S.",
        "page": "801",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 2132",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "2132",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 L. Ed. 2d 1",
        "volume": "53",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 19",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "19",
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
    "date_created": "2026-07-06T13:51:44Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:51:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:51:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:51:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:51:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — lefkowitz-v-cunningham--109683

```
<opinion type="majority">
<author id="b864-10">Mr. Chief Justice Burger</author>
<p id="AVQ">delivered the opinion of the Court.</p>
<p id="b864-11">This appeal presents the question whether a political party officer can be removed from his position by the State of New York and barred for five years from holding any other party or public office, because he has refused to waive his constitutional privilege against compelled self-incrimination.</p>
<p id="b864-12">(1)</p>
<p id="b864-13">Under § 22 of the New York Election Law,<footnotemark>1</footnotemark> an officer of a <page-number citation-index="1" label="803">*803</page-number>political party may be subpoenaed by a grand jury or other authorized tribunal and required to testify concerning his conduct of the party office he occupies. If the officer refuses to answer any question, or if he declines to waive immunity from the use of his testimony against him in a later prosecution, the statute immediately terminates his party office and prohibits him from holding any other party or public office for a period of five years.</p>
<p id="b865-5">In December 1975, appellee Patrick J. Cunningham (hereafter appellee) was subpoenaed pursuant to § 22 to appear and testify before a special grand jury authorized to investigate his conduct in the political offices he then held, which consisted of four unsalaried elective positions in the Democratic Party of the State of New York.<footnotemark>2</footnotemark> Appellee moved to quash the subpoena in the state courts, arguing in part that § 22 violated his federal constitutional right to be free of compelled self-incrimination; his motion was denied. <em>In re Cunningham </em>v. <em>Nadjari, </em>51 App. Div. 2d 927, 383 N. Y. S. 2d 311, aff’d, 39 N. Y. 2d 314, <span class="citation" data-id="5530476"><a href="/opinion/5681999/cunningham-v-nadjari/" aria-description="Citation for case: Cunningham v. Nadjari">347 N. E. 2d 915</a></span> (1976). On April 12, 1976, he appeared before the grand jury in response to the subpoena. Appellee refused to sign a waiver of immunity form which would have waived his constitutional right not to be compelled to incriminate himself.<footnotemark>3</footnotemark> Because § 22 is self-executing, appel<page-number citation-index="1" label="804">*804</page-number>lee’s refusal to waive his constitutional immunity automatically divested him of all his party offices and activated the five-year ban on holding any public or party office.</p>
<p id="b866-5">The following day, appellee commenced this action in the United States District Court for the Southern District of New York. After hearing, the District Judge entered a temporary restraining order against enforcement of § 22. A three-judge court was then convened, and that court granted appellee declaratory and permanent injunctive relief against enforcement of § 22 on the ground that it violated appellee’s Fifth and Fourteenth Amendment rights. We noted probable jurisdiction, <span class="citation multiple-matches"><a href="/c/U.%20S./429/893/">429 U. S. 893</a></span> (1976). We affirm.</p>
<p id="b866-6">(2)</p>
<p id="b866-7">We begin with the proposition that the Fifth Amendment privilege against compelled self-incrimination protects grand <page-number citation-index="1" label="805">*805</page-number>jury witnesses from being forced to give testimony which may later be used to convict them in a criminal proceeding. See, <em>e. g., United States </em>v. <em>Washington, ante, </em>at 186-187. Moreover, since the test is whether the testimony might later subject the witness to criminal prosecution, the privilege is available to a witness in a civil proceeding, as well as to a defendant in a criminal prosecution. <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#11" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 11</a></span> (1964). In either situation the witness may “refuse to answer unless and until he is protected at least against the use of his compelled answers and evidence derived therefrom in any subsequent criminal case in which he is a defendant.” <em>Lefkowitz </em>v. <em>Turley, </em><span class="citation" data-id="108882"><a href="/opinion/108882/lefkowitz-v-turley/#78" aria-description="Citation for case: Lefkowitz v. Turley">414 U. S. 70, 78</a></span> (1973).</p>
<p id="b867-5">Thus, when a State compels testimony by threatening to inflict potent sanctions unless the constitutional privilege is surrendered, that testimony is obtained in violation of the Fifth Amendment and cannot be used against the declarant in a subsequent criminal prosecution. In <em>Garrity </em>v. <em>New Jersey, </em><span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">385 U. S. 493</a></span> (1967), for example, police officers under investigation were told that if they declined to answer potentially incriminating questions they would be removed from office, but that any answers they did give could be used against them in a criminal prosecution. We held that statements given under such circumstances were made involuntarily and could not be used to convict the officers of crime.</p>
<p id="b867-6">Similarly, our cases have established that a State may not impose substantial penalties because a witness elects to exercise his Fifth Amendment right not to give incriminating testimony against himself. In <em>Gardner </em>v. <em>Broderick, </em><span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">392 U. S. 273</a></span> (1968), a police officer appearing before a grand jury investigating official corruption was subject to discharge if he did not waive his Fifth Amendment privilege and answer, without immunity, all questions asked of him. When he refused, and his employment was terminated, this Court held that the officer could not be discharged solely for his refusal to forfeit the rights guaranteed him by the Fifth Amendment; the privilege against compelled self-inerimina<page-number citation-index="1" label="806">*806</page-number>tion could not abide any “attempt, regardless of its ultimate effectiveness, to coerce a waiver of the immunity it confers on penalty of the loss of employment.” <span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/#279" aria-description="Citation for case: Gardner v. Broderick"><em>Id., </em>at 279</a></span>. Accord, <em>Sanitation Men </em>v. <em>Sanitation Comm’r, </em><span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">392 U. S. 280</a></span> (1968). At the same time, the Court provided for effectuation of the important public interest in securing from public employees an accounting of their public trust. Public employees may constitutionally be discharged for refusing to answer potentially incriminating questions concerning their official duties if they have not been required to surrender their constitutional immunity. <span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/#278" aria-description="Citation for case: Gardner v. Broderick"><em>Gardner, supra, </em>at 278-279</a></span>.</p>
<p id="b868-5">We affirmed the teaching of <em><span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">Gardner</a></span> </em>more recently in <em>Lefkowitz </em>v. <em><span class="citation" data-id="108882"><a href="/opinion/108882/lefkowitz-v-turley/" aria-description="Citation for case: Lefkowitz v. Turley">Turley, supra,</a></span> </em>where two architects who did occasional work for the State of New York refused to waive their Fifth Amendment privilege before a grand jury investigating corruption in public contracting practices. State law provided that if a contractor refused to surrender his constitutional privilege before a grand jury, his existing state contracts would be canceled, and he would be barred from future contracts with the State for five years. The Court saw no constitutional distinction between discharging a public employee and depriving an independent contractor of the opportunity to secure public contracts; in both cases the State had sought to compel testimony by imposing a sanction as the price of invoking the Fifth Amendment right.</p>
<p id="b868-6">These cases settle that government cannot penalize assertion of the constitutional privilege against compelled self-incrimination by imposing sanctions to compel testimony which has not been immunized. It is true, as appellant points out, that our earlier cases were concerned with penalties having a substantial economic impact. But the touchstone of the Fifth Amendment is comjpulsion, and direct economic sanctions and imprisonment are not the only penalties capable of forcing the self-incrimination which the Amendment forbids.</p>
<p id="b869-4"><page-number citation-index="1" label="807">*807</page-number>(3)</p>
<p id="b869-5">Section 22 confronted appellee with grave consequences solely because he refused to waive immunity from prosecution and give self-incriminating testimony. Section 22 is therefore constitutionally indistinguishable from the coercive provisions we struck down in <em>Gardner, Sanitation Men, </em>and <em><span class="citation" data-id="108882"><a href="/opinion/108882/lefkowitz-v-turley/" aria-description="Citation for case: Lefkowitz v. Turley">Turley</a></span>. </em>Appellee’s party offices carry substantial prestige and political influence, giving him a powerful voice in recommending or selecting candidates for office and in other political decisions. The threatened loss of such widely sought positions, with their power and perquisites, is inherently coercive. Additionally, compelled forfeiture of these posts diminishes appellee’s general reputation in his community.</p>
<p id="b869-6">There are also economic consequences; appellee’s professional standing as a practicing lawyer would suffer by his removal from his political offices under these circumstances. Further, § 22 bars appellee from holding any other party or public office for five years. Many such offices carry substantial compensation. Appellant argues that appellee has no enforceable property interest in future office, but neither did the architects in <em><span class="citation" data-id="108882"><a href="/opinion/108882/lefkowitz-v-turley/" aria-description="Citation for case: Lefkowitz v. Turley">Turley</a></span> </em>have an enforceable claim to future government contracts. Nevertheless, we found that disqualification from eligibility for such contracts was a substantial economic burden. In assessing the coercion which § 22 exerts, we must take into account potential economic benefits realistically likely of attainment. Prudent persons weigh heavily such legally unenforceable prospects in making decisions; to that extent, removal of those prospects constitutes economic coercion.<footnotemark>4</footnotemark></p>
<p id="b869-7">Section 22 is coercive for yet another reason: It requires appellee to forfeit one constitutionally protected right as the <page-number citation-index="1" label="808">*808</page-number>price for exercising another. See <em>Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#394" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 394</a></span> (1968). As an officer in a private political party, appellee is in a far different position from a government policymaking official holding office at the pleasure of the President or Governor. By depriving appellee of his offices, § 22 impinges on his right to participate in private, voluntary political associations. That right is an important aspect of First Amendment freedom which this Court has consistently found entitled to constitutional protection. <em>Kusper </em>v. <em>Pontikes, </em><span class="citation" data-id="9425459"><a href="/opinion/108881/kusper-v-pontikes/" aria-description="Citation for case: Kusper v. Pontikes">414 U. S. 51</a></span> (1973); <em>Williams </em>v. <em>Rhodes, </em><span class="citation" data-id="9423829"><a href="/opinion/107783/williams-v-rhodes/" aria-description="Citation for case: Williams v. Rhodes">393 U. S. 23</a></span> (1968).</p>
<p id="b870-5">Appellant argues that even if § 22 is violative of Fifth Amendment rights, the State’s overriding interest in preserving public confidence in the integrity of its political process justifies the constitutional infringement. We have already rejected the notion that citizens may be forced to incriminate themselves because it serves a governmental need. <em>E. g., Lefkowitz </em>v. <em>Turley, </em><span class="citation" data-id="108882"><a href="/opinion/108882/lefkowitz-v-turley/#78" aria-description="Citation for case: Lefkowitz v. Turley">414 U. S., at 78-79</a></span>. Government has compelling interests in maintaining an honest police force and civil service, but this Court did not permit those interests to justify infringement of Fifth Amendment rights in <em>Garrity, Gardner, </em>and <em><span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">Sanitation Men</a></span>, </em>where alternative methods of promoting state aims were no more apparent than here.<footnotemark>5</footnotemark></p>
<p id="b870-6">(4)</p>
<p id="b870-7">It may be, as appellant contends, that “[a] State <page-number citation-index="1" label="809">*809</page-number>forced to choose between an accounting from or a prosecution of a party officer is in an intolerable position.” Brief for Appellant 12-13. But this dilemma is created by New York’s transactional immunity law, which immunizes grand jury witnesses from prosecution for any transaction about which they testify. The more limited use immunity required by the Fifth Amendment would permit the State to prosecute appellee for any crime of which he may be guilty in connection with his party office, provided only that his own compelled testimony is not used to convict him. Once proper use immunity is granted, the State may use its contempt powers to compel testimony concerning the conduct of public office, without forfeiting the opportunity to prosecute the witness on the basis of evidence derived from other sources.</p>
<p id="b871-5">Accordingly, the judgment is</p>
<p id="b871-6">
<em>Affirmed.</em>
</p>
<judges id="b871-7">Mr. Justice Rehnquist took no part in the consideration or decision of this case.</judges>
<footnote label="1">
<p id="b864-15"> “If any party officer shall, after lawful notice of process, wilfully refuse or fail to appear before any court or judge, grand jury, legislative committee, officer, board or body authorized to conduct any hearing or inquiry concerning the conduct of his party office or the performance of his duties, or having appeared, shall refuse to testify or answer any relevant question, or shall refuse to sign a waiver of immunity against subsequent criminal prosecution, his term or tenure of office shall terminate, <page-number citation-index="1" label="803">*803</page-number>such office shall be vacant and he shall be disqualified from holding any party or public office for a period of five years.” N. Y. Elec. Law § 22 (McKinney 1964).</p>
<p id="AEH">New York Election Law § 2 (9) (McKinney 1964) defines a party officer as “one who holds any party position or any party office whether by election, appointment or otherwise.”</p>
</footnote>
<footnote label="2">
<p id="b865-8"> Appellee was chairman of the State Democratic Committee and the Bronx County Democratic Executive Committee, and a member of the Executive Committee of the New York State Democratic Committee and the Bronx County Democratic Executive Committee. We are advised that appellee has recently resigned as chairman of the state organization. He retains his other party offices.</p>
</footnote>
<footnote label="3">
<p id="b865-9"> In the absence of an effective waiver, New York law would have entitled appellee to transactional immunity from prosecution on all matters <page-number citation-index="1" label="804">*804</page-number>about which he testified. N. Y. Crim. Proc. Law §§ 50.10, 190.40, 190.45 (McKinney 1971 and Supp. 1976-1977). As appellant concedes, however, Tr. of Oral Arg. 4r-5, and as the record reflects, the State also insisted on a waiver of the more limited use immunity which we have held essential to protect Fifth Amendment rights. <em>Kastigar </em>v. <em>United States, </em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441</a></span> (1972).</p>
<p id="Aig">The waiver form which appellee’s counsel represents is presented to grand jury witnesses waives “all immunity and privileges which I would otherwise obtain under the provisions of the Constitution of the United States and of the State of New York” and further “consent[s] to the use against me of the testimony so given . . . upon any criminal trial, investigation, prosecution or proceeding.” McKinney’s Forms for the Criminal Procedure Law § 190.45, Form 1 (1971). See N. Y. Crim. Proc. Law § 190.45. Appellee’s refusal to sign this waiver form, pressed on him immediately before talcing the oath, was in these circumstances an effective assertion of his Fifth Amendment privilege.</p>
<p id="AAnG">Of course, New York’s procedure in this regard is not constitutionally required. Rather than permit an assertion of the Fifth Amendment privilege to confer immunity with respect to all matters testified to before the grand jury, New York could, if it chose, require a witness to assert his constitutional privilege to the specific questions • he deems potentially incriminating, withholding constitutional use immunity until the validity of the assertion is upheld.</p>
</footnote>
<footnote label="4">
<p id="b869-8"> That appellee’s refusal to waive immunity and answer questions concerning his conduct of office may have already damaged his reputation and standing is irrelevant to the issues in this case; it is inescapable that public judgments are often made on such factors.</p>
</footnote>
<footnote label="5">
<p id="b870-8"><em> Baxter </em>v. <em>Palmigiano, </em><span class="citation" data-id="9426363"><a href="/opinion/109429/baxter-v-palmigiano/" aria-description="Citation for case: Baxter v. Palmigiano">425 U. S. 308</a></span> (1976), is not to the contrary. That case involved an administrative disciplinary proceeding in which the respondent was advised that he was not required to testify, but that if he chose to remain silent his silence could be considered against him. <em><span class="citation" data-id="9426363"><a href="/opinion/109429/baxter-v-palmigiano/" aria-description="Citation for case: Baxter v. Palmigiano">Baxter</a></span> </em>did no more than permit an inference to be drawn in a civil case from a party’s refusal to testify. Respondent’s silence in <em><span class="citation" data-id="9426363"><a href="/opinion/109429/baxter-v-palmigiano/" aria-description="Citation for case: Baxter v. Palmigiano">Baxter</a></span> </em>was only one of a number of factors to be considered by the finder of fact in assessing a penalty, and was given no more probative value than the facts of the case warranted; here, refusal to waive the Fifth Amendment privilege leads automatically and without more to imposition of sanctions.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/long-lake-township-v-maxon--ucb0bfc28.json  (`lake-record`, 1 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9655dc88e0d91ac6", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "long-lake-township-v-maxon--ucb0bfc28"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "long-lake-township-v-maxon--ucb0bfc28", "scope_note": null, "varies_by_point": false}}
```

### lake record — long-lake-township-v-maxon--ucb0bfc28

```json
{
  "schema_version": "s2.v1",
  "record_id": "long-lake-township-v-maxon--ucb0bfc28",
  "stub": true,
  "status": "not_found",
  "identity": {
    "case_name": null,
    "case_name_short": null,
    "case_name_full": null,
    "input_case_name": "Long Lake Township v. Maxon",
    "court": "Michigan (COA 2021; Sup. Ct. 2024)",
    "court_id": null,
    "court_level": "state",
    "circuit": null,
    "state": "MI",
    "date_decided": null,
    "year": 2024,
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
      "court_class": "coa",
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
    "date_created": "2026-07-06T13:12:04Z",
    "date_modified": "2026-07-06T13:12:18Z",
    "warnings": [
      "frontier not_found requires web/second-source cross-check before fabrication inference"
    ],
    "field_provenance": {
      "identity": {
        "src": "pending",
        "at": "2026-07-06T13:12:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "pending",
        "at": "2026-07-06T13:12:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "pending",
        "at": "2026-07-06T13:12:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "pending",
        "at": "2026-07-06T13:12:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

---

## GROUP: _overhaul2/lake/cases/marron-v-united-states--101164.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "04bfa25fc7fba993", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "marron-v-united-states--101164"}, "payload": {"all": [{"cite": "275 U.S. 192", "page": "192", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "275"}, {"cite": "48 S. Ct. 74", "page": "74", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "48"}, {"cite": "72 L. Ed. 231", "page": "231", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "72"}, {"cite": "1927 U.S. LEXIS 273", "page": "273", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1927"}], "display": null, "official": null, "official_selection_present": false, "record_id": "marron-v-united-states--101164"}}
{"assertion_id": "c19a7be5acbba0f1", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "marron-v-united-states--101164"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "marron-v-united-states--101164", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — marron-v-united-states--101164

```json
{
  "schema_version": "s2.v1",
  "record_id": "marron-v-united-states--101164",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Marron v. United States",
    "case_name_short": "Marron",
    "case_name_full": "Marron v. United States.",
    "input_case_name": "Marron v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1927-11-21",
    "year": 1927,
    "docket": null,
    "cluster_id": 101164,
    "lead_opinion_id": 101164,
    "sibling_ids": [],
    "absolute_url": "/opinion/101164/marron-v-united-states/",
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
        "cite": "275 U.S. 192",
        "volume": "275",
        "reporter": "U.S.",
        "page": "192",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "48 S. Ct. 74",
        "volume": "48",
        "reporter": "S. Ct.",
        "page": "74",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 L. Ed. 231",
        "volume": "72",
        "reporter": "L. Ed.",
        "page": "231",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1927 U.S. LEXIS 273",
        "volume": "1927",
        "reporter": "U.S. LEXIS",
        "page": "273",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "275 U.S. 192",
        "volume": "275",
        "reporter": "U.S.",
        "page": "192",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "48 S. Ct. 74",
        "volume": "48",
        "reporter": "S. Ct.",
        "page": "74",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 L. Ed. 231",
        "volume": "72",
        "reporter": "L. Ed.",
        "page": "231",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1927 U.S. LEXIS 273",
        "volume": "1927",
        "reporter": "U.S. LEXIS",
        "page": "273",
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
    "date_created": "2026-07-06T13:52:36Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:52:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:52:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:52:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:52:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — marron-v-united-states--101164

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b245-3">
<span citation-index="1" class="star-pagination" label="193"> 
   *193
   </span>
  Mr. Justice Butler
 </author>
<p id="AWh">
  delivered the opinion of the ' Court.
 </p>
<p id="b245-4">
  October 17, 1924, the above named petitioner, one Birdsall, and five others were indicted in the southern division of the northern district of California. . It was charged that they conspired to commit various offenses against the National'Prohibition Act, including the maintenance of a nuisance at 1249 Polk Street, San Francisco. § 37 Criminal Code (U. S. C., Tit. 18, § 88). One defendant was never apprehended; one was acquitted; the rest were found guilty. Of these, Marrón, Birdsall, and two others obtained review, in the Circuit Court of Appeals. The judgment .was affirmed as to all except petitioner. He secured reversál and a new trial. 8 F. (2d) 251., He was again found guilty; and the conviction was affirmed. 18 F. (2d) 218.
 </p>
<p id="b245-6">
  Petitioner insists that a ledger and certain bills were obtained through an illegal search and seizure and put in evidence, against him in violation of the Fourth and Fifth Amendments. The question arose at the first trial. The Circuit Court of Appeals held that the book and papers were-lawfully seized and admissible. When the second, conviction was before it, that court held the earlier decision governed the trial, established the law of the case, and foreclosed further consideration.
 </p>
<p id="b245-7">
  For some time prior to October 1, 1924, petitioner was the lessee of the entire second floor of 1249 Polk Street. On that day a prohibition agent obtained from a United States commissioner a warrant' for the search of that place, particularly describing the things to be seized — ■ intoxicating liquors and articles for their manufacture. The next day, four prohibition agents went to the place and secured admission by causing the doorbell to be rung. There were six or seven rooms containing slot machines,
  <span citation-index="1" class="star-pagination" label="194"> 
   *194
   </span>
  an ice box, tables, chairs and a cash register. The evidence shows that the place was used for retailing and drinking intoxicating liquors. About a dozen men and women were there and some of'them were being furnished intoxicating liquors. The petitioner, was not there; Bird-sail was in charge. The agents handed him the warrant and put him under arrest. They searched for and found large quantities of liquor, some of which was in a closet. While in the closet, they noticed a ledger showing inventories of liquors, receipts, expenses, including gifts to police officers, and other things relating to the business.' And they found beside the cash register a number of bills against petitioner for gas, electric light, water and telephone service furnished on the. premises. They seized the ledger and bills. The retum made on the search warrant showed only the seizure of the intoxicating liquors. It did not show the discovery Or seizure of the ledger or bills. After indictment and before trial, petitioner applied to the court for the return of the ledger and bills and to suppress evidence concerning them. The application was denied. At the trial there was evidence to show that petitioner made most of the entries in the ledger and that he was concerned as proprietor or partner in carrying on'the business of selling intoxicating liquors.
 </p>
<p id="b246-4">
  It has long been settled that the Fifth Amendment protects every person against incrimination by the use of evidence obtained through search or seizure made in violation of his rights under the Fourth Amendment.
  <em>
   Agnello
  </em>
  v.
  <em>
   United
  </em>
  States, <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#34" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 34</a></span>, and cases cited.
 </p>
<p id="b246-5">
  The petitioner insists th$t because the ledger -and bills were not described in the; warrant and as he .was not arrested with them on his person, their seizure violated the Fourth Amendment. The United States contends that the seizure-may be justified either as an incident to the execution of the-search warrant, or as an incident to the
  <span citation-index="1" class="star-pagination" label="195"> 
   *195
   </span>
  right of search arising from the arrest of Rirdsall whila in charge of the saloon. Both questions are presented. Lower courts have expressed divers views in respect of searches in similar cases. The brief for the Government states that the facts of this case present one of the most frequent causes of appeals in current cases. And for these reasons we deal with both contentions.
 </p>
<p id="b247-4">
  1. The Fourth Amendment declares that the right to be secure against unreasonable searches shall not be violated, and it further declares that “no Warrants shall issue, hot upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched and the persons or things to be seized.” General searches have long been deemed to violate fundamental rights. It is plain that the Amendment forbids them. In
  <em>
   Boyd
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, Mr. Justice Bradley, writing for the court, said (p. 624): “ In order to ascertain the nature of the proceedings intended by the Fourth Amendment to the Constitution under the terms ‘ unreasonable searches and seizures/ it is only necessary to recall the contemporary or then recent history of the controversies on the subject, both in this country and in England. The practice had obtained in the colonies of issuing writs of assistance to the revenue officers, empowering them, in their discretion, to search suspected places for smuggled goods, which James Otis pronounced ‘the worst instrument of arbitrary, power, the most destructive of English liberty, and the fundamental principles of law, that éver was found in an English law book; ’ since they placed * the liberty of every man in the hands of every petty officer.’ ” And in
  <em>
   Weeks
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, Mr. Justice Day, writing for the court, said (p.- 391): “ The effect of the Fourth Amendment is to put the courts of the United States and Federal officials, in the
  <span citation-index="1" class="star-pagination" label="196"> 
   *196
   </span>
  exercise of their power and authority, under limitations and restraints as to the exercise of such power and authority, and to forever secure the people, their persons, houses, papéis and effects against, all unreasonable searches and seizures .under the guise of law.' This protection reaches all alike, whether accused of crime or not, and the duty of giving to it force and effect is obligatory upon all entrusted under our Federal' system with the enforcement of the laws. The tendency of those who execute the criminal laws of the country to obtain conviction by means of unlawful seizures aiid enforced confessions . . . should find no sanction in the judgments of the courts which are charged at all times with the support of the Constitution and to which people of all conditions have a right to appeal for the maintenance of such fundamental rights.”
 </p>
<p id="Aqd">
  ■ The requirement that warrants shall1 particularly describe the things to be seized makes general searches under them impossible and prevents the seizure- of one thing under a, warrant describing another. As to what is to be taken, nothing is left to the discretion of the officer executing the warrant.
 </p>
<p id="b248-6">
  And the Congress in enacting the laws governing the issue and execution of this search warrant was diligent to limit seizures to things particularly described. Section 39 of Title 27, U. S. C., provides that such warrant may issue as provided in Title 18, §§ 611 to 631 and § 633.
  <a class="footnote" href="#fn*" id="fn*_ref">
   *
  </a>
  Section 613 provides that a search warrant cannot be issued but upon probable cause, supported by affidavit naming or describing the person, and particularly describing property and. place to be searched. Section
  <span citation-index="1" class="star-pagination" label="197"> 
   *197
   </span>
  622 requires the officer executing the warrant to give to .the person in whose possession the property taken was found a receipt specifying it in detail. Section 623 requires him forthwith to return the warrant to the judge or commissioner with a verified inventory and detailed account of the property taken. Section 624 gives the person from whom the property is taken a right to have a copy of the inventory. Section 626 provides that, if it appears that the property or paper taken is not the same as that described in the warrant, the judge or commissioner must cause it to be returned to the person from whom it was taken. And § 631 provides for punishment of an officer who willfully exceeds his authority in executing a search warrant.
 </p>
<p id="b249-3">
  The Government relies on
  <em>
   Adams
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U. S. 585</a></span>. That was a prosecution, in a state court. It involved no search or seizure under a law, or by an officer, of the United States. Adams was convicted of having gambling paraphernalia in violation of the Penal Code of New' York. It appeared that he occupied an office where were his desk, trunk, tin boxes and other articles. Officers came and stated that they had a search warrant. He said it was not his office. They arrested him, searched the place, found “ policy slips,” etc., and also papers relating to., his private affairs. The policy papers were introduced in evidence. There were endorsements in his handwriting on some of them. Over his objection, the private papers were received to furnish specimens of his writing and to show that he occupied the office. He had taken no steps to secure the return of his private papers or to prevent their use as evidence. But at the trial he contended their seizure violated his right to be secure against unreasonable searches, and that their use as evidence compelled him to be a witness against himself in violation of the Fourth and Fifth Amendments, and in violation of similar provisions of
  <span citation-index="1" class="star-pagination" label="198"> 
   *198
   </span>
  the state constitution. The Court of Appeals (<span class="citation multiple-matches"><a href="/c/N.%20Y./176/351/">176 N. Y. 351</a></span>) held that the provisions of the Federal Constitution did not apply; that the use of the private papers as evidence did not violate the state constitution; declared that it expressed no opinion as to the seizure, and applied "the rule that a court, when engaged in trying a criminal case, will not take notice of the manner in which the witnesses obtained papers offered in evidence. And this court, assuming without deciding that the Fourth and Fifth Amendments were applicable, held the use of the private papers as evidence did not violate any right saféguarded by these Amendments; and, after reference to the procedure at the trial, declared that “ courts do not stop to inquire as to the means by which the evidence was obtained.” The court did not decide whether the seizure violated the Fourth Amendment. It decided that the admission in evidence of the private papers did not infringe the Fourth or Fifth Amendments. The case does not support the Government’s contention. And see
  <em>
   Weeks
  </em>
  v.
  <em>
   United States, supra,
  </em>
  394-396;
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span>;
  <em>
   Agnello
  </em>
  v.
  <em>
   United States, supra,
  </em>
  34. And it is clear that the seizure of the ledger and bills, in .the case now under consideration, was not authorized by the warrant. Cf.
  <em>
   Kirvin
  </em>
  v.
  <em>
   United States,
  </em>
  5 F. (2d) 282, 285;
  <em>
   United States
  </em>
  v.
  <em>
   Kirschenblatt,
  </em>
  16 F. (2d) 202;
  <em>
   Steele
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100621"><a href="/opinion/100621/steele-v-united-states-no-1/" aria-description="Citation for case: Steele v. United States No. 1">267 U. S. 498</a></span>.
 </p>
<p id="b250-4">
  2. When arrested, Birdsall was actually engaged in a conspiracy to maintain, and was actually in charge of, the premises where intoxicating liquors were being unlawfully sold. Every such place is by the National Prohibition Act declared to be a common nuisance, the maintenance of which is punishable by fine, imprisonment or both. § 21, Tit. II, Act of October 28, 1919, c. .85, <span class="citation no-link">41 Stat. 305</span>, 314 (U. S. C., Tit. 27, § 33). The officers were authorized to arrest for crime being committed in their presence, and
  <span citation-index="1" class="star-pagination" label="199"> 
   *199
   </span>
  they lawfully arrested Birdsall, They had a right without a warrant contemporaneously to. search the place in order- to find and seize the things used to carry on the criminal enterprise.
  <em>
   Agnello
  </em>
  v.
  <em>
   United States, supra,
  </em>
  30;
  <em>
   Carroll
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#168" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 168</a></span>;
  <em>
   Weeks
  </em>
  v.
  <em>
   United States, supra,
  </em>
  392. The closet in which liquor and the ledger were found was used as a part of the saloon. And, if the ledger was not as essential to the maintenance of the establishment as were bottles, liquors and glasses, it was none the less a part of the outfit or equipment actually used to commit the offense. And, while it was not on Birdsall’s person at the time of his arrest, it was in his immediate possession and control. The authority of officers to search and seize the things by which the nuisance was being maintained, extended to all parts of the premises used for the unlawful purpose. Cf.
  <em>
   Sayers
  </em>
  v.
  <em>
   United States,
  </em>
  2 F. (2d) 146;
  <em>
   Kirvin
  </em>
  v.
  <em>
   United States, supra; United States
  </em>
  v.
  <em>
   Kirschenblatt, supra.
  </em>
  The bills for gas, electric light, water and telephone services disclosed items of expense; they were convenient, if not in fact necessary, for the keeping of the accounts; and, as they were so closely related to the business, it is not un-. reasonable to consider them as used to carry it on. It follows that the ledger and bills were lawfully seized as an incident of the arrest.
 </p>
<p id="b251-3">
<em>
   Judgment affirmed.
  </em>
</p>

<div class="footnotes"><div class="footnote" id="fn*" label="*">
<a class="footnote" href="#fn*_ref">
   *
  </a>
<p id="b248-7">
   Section 25, Title II, Act of October 28, 1919, c. 85, <span class="citation no-link">41 Stat. 305</span>, 315, is § 39, Title 27, U. S.' C. It provides that a search warrant may issue as provided in Title XI of the Espionage Act (June 15, 1917), <span class="citation no-link">40 Stat. 217</span>, 228. Title XI is §§ 611 to 631 and § 633, Title 18, U. S. C.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/michigan-v-harvey--112385.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d57037b71d326d93", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "michigan-v-harvey--112385"}, "payload": {"all": [{"cite": "494 U.S. 344", "page": "344", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "494"}, {"cite": "110 S. Ct. 1176", "page": "1176", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "110"}, {"cite": "108 L. Ed. 2d 293", "page": "293", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "108"}, {"cite": "1990 U.S. LEXIS 1229", "page": "1229", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1990"}], "display": null, "official": null, "official_selection_present": false, "record_id": "michigan-v-harvey--112385"}}
{"assertion_id": "88eb61caa299f732", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "michigan-v-harvey--112385"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "michigan-v-harvey--112385", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — michigan-v-harvey--112385

```json
{
  "schema_version": "s2.v1",
  "record_id": "michigan-v-harvey--112385",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Michigan v. Harvey",
    "case_name_short": "Harvey",
    "case_name_full": "Michigan v. Harvey",
    "input_case_name": "Michigan v. Harvey",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-04-30",
    "year": 1990,
    "docket": null,
    "cluster_id": 112385,
    "lead_opinion_id": 9431937,
    "sibling_ids": [],
    "absolute_url": "/opinion/112385/michigan-v-harvey/",
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
        "cite": "494 U.S. 344",
        "volume": "494",
        "reporter": "U.S.",
        "page": "344",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 S. Ct. 1176",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "1176",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "108 L. Ed. 2d 293",
        "volume": "108",
        "reporter": "L. Ed. 2d",
        "page": "293",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 1229",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "1229",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "494 U.S. 344",
        "volume": "494",
        "reporter": "U.S.",
        "page": "344",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 S. Ct. 1176",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "1176",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "108 L. Ed. 2d 293",
        "volume": "108",
        "reporter": "L. Ed. 2d",
        "page": "293",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 1229",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "1229",
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
    "date_created": "2026-07-06T13:51:53Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:52:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:52:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:52:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:52:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — michigan-v-harvey--112385

```
<opinion type="majority">
<author id="b411-9">Chief Justice Rehnquist</author>
<p id="AC7">delivered the opinion of the Court.</p>
<p id="b411-10">In <em>Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625</a></span> (1986), the Court established a prophylactic rule that once a criminal defendant invokes his Sixth Amendment right to counsel, a subsequent waiver of that right — even if voluntary, knowing, and intelligent under traditional standards — is presumed invalid if secured pursuant to police-initiated conversation. We held that statements obtained in violation of that rule may not be admitted as substantive evidence in the prosecution’s case in chief. The question presented in this case is whether the <page-number citation-index="1" label="346">*346</page-number>prosecution may use a statement taken in violation of the <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>prophylactic rule to impeach a defendant’s false or inconsistent testimony. We hold that it may do so.</p>
<p id="b412-5">Respondent Tyris Lemont Harvey was convicted of two counts of first-degree criminal sexual conduct in connection with the rape of Audrey Sharp on June 11, 1986. Harvey was taken into custody on July 2, 1986, and on that date, he made a statement to an investigating officer. He was arraigned later on July 2, and counsel was appointed for him. More than two months later, Harvey told another police officer that he wanted to make a second statement, but did not know whether he should talk to his lawyer. Although the entire context of the discussion is not clear from the record, the officer told respondent that he did not need to speak with his attorney, because “his lawyer was going to get a copy of the statement anyway.” App. 32-33 (stipulation of prosecution). Respondent then signed a constitutional rights waiver form, on which he initialed the portions advising him of his right to remain silent, his right to have a lawyer present before and during questioning, and his right to have a lawyer appointed for him prior to any questioning. App. to Pet. for Cert. 3a-4a.<footnotemark>1</footnotemark> Asked whether he understood his constitutional rights, respondent answered affirmatively. He then gave a statement detailing his version of the events of June 11.</p>
<p id="b412-6">At a bench trial, Sharp testified that Harvey visited her home at 2:30 a.m. on the date in question and asked to use the telephone. After placing a call, Harvey confronted Sharp with a barbecue fork, and a struggle ensued. According to Sharp, respondent struck her in the face, threatened her with the fork and a pair of garden shears, and eventually threw her to the floor of her kitchen. When she ran to the living room to escape, Harvey pursued her with the weapons, <page-number citation-index="1" label="347">*347</page-number>demanded that she take off her clothes, and forced her to engage in sexual acts.</p>
<p id="b413-4">Harvey testified in his own defense and presented a conflicting account of the night’s events. He claimed that he had gone to Sharp’s home at 9 p.m. and invited her to smoke some crack cocaine, which he offered to supply in return for sexual favors. She agreed, but after smoking the cocaine, she refused to perform the favors. When respondent would not leave her house, Sharp allegedly grabbed the barbecue fork and threatened him, triggering a brief fight during which he grabbed the fork and threw it to the floor. The two then moved to the living room, where, according to Harvey, Sharp voluntarily removed her clothes. He testified, however, that the two never engaged in sexual intercourse and that he left shortly thereafter.</p>
<p id="b413-5">On cross-examination, the prosecutor used Harvey’s second statement to the police to impeach his testimony. Before doing so, the prosecutor stipulated that the statement “was not subject to proper Miranda,” App. 32, and therefore could not have been used in the case in chief. But because the statement was voluntary, the prosecutor argued that it could be used for impeachment under our decision in <em>Harris </em>v. <em>New York, </em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971). Defense counsel did not object, App. 34; App. to Pet. for Cert. 5a, and the trial court permitted the questioning. The prosecutor then impeached certain of Harvey’s statements, including his claim that he had thrown the barbecue fork to the floor, by showing that he had omitted that information from his statement to the police. App. 36-45.<footnotemark>2</footnotemark> The trial judge believed the victim’s testimony and found respondent guilty as charged.</p>
<p id="b414-4"><page-number citation-index="1" label="348">*348</page-number>The Michigan Court of Appeals reversed the conviction. The court noted that if the second statement had been taken only in violation of the rules announced in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), it could have been used to impeach Harvey’s testimony. It held, however, that the statement was inadmissible even for impeachment purposes, because it was taken “in violation of defendant’s Sixth Amendment right to counsel. See <em>e. g., Michigan v. Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">475 US 625</a></span>.” App. to Pet. for Cert. 6a-7a. Because the trial “involved a credibility contest between defendant and the victim,” the court concluded that the impeachment was not harmless beyond a reasonable doubt. <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Id.,</a></span> </em>at 7a. The Michigan Supreme Court denied leave to appeal, three justices dissenting, and we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./489/1010/">489 U. S. 1010</a></span> (1989). We now reverse.</p>
<p id="b414-5">To understand this case, it is necessary first to review briefly the Court’s jurisprudence surrounding the Sixth Amendment. The text of the Amendment provides in pertinent part that “[i]n all criminal prosecutions, the accused shall enjoy the right ... to have the Assistance of Counsel for his defence.” The essence of this right, we recognized in <em>Powell </em>v. <em>Alabama, </em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span> (1932), is the opportunity for a defendant to consult with an attorney and to have him investigate the case and prepare a defense for trial. <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#58" aria-description="Citation for case: Powell v. Alabama"><em>Id., </em>at 58, 71</a></span>. More recently, in a line of cases beginning with <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964), and extending through <em>Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">474 U. S. 159</a></span> (1985), the Court has held that once formal criminal proceedings begin, the Sixth Amendment renders inadmissible in the prosecution’s case in chief statements “deliberately elicited” from a defendant without an express waiver of the right to counsel. See also <em>United States </em>v. <em>Henry, </em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">447 U. S. 264</a></span> (1980); <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387</a></span> (1977). For the fruits of postindictment interrogations to be admissible in a prosecution’s case in chief, the State must prove a voluntary, knowing, and intelligent relinquishment of the Sixth Amendment <page-number citation-index="1" label="349">*349</page-number>right to counsel. <em>Patterson </em>v. <em>Illinois, </em><span class="citation" data-id="9431404"><a href="/opinion/112127/patterson-v-illinois/#292" aria-description="Citation for case: Patterson v. Illinois">487 U. S. 285, 292</a></span>, and n. 4 (1988); <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#404" aria-description="Citation for case: Brewer v. Williams"><em>Brewer, supra, </em>at 404</a></span>. We have recently held that when a suspect waives his right to counsel after receiving warnings equivalent to those prescribed by <em>Miranda </em>v. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona, supra,</a></span> </em>that will generally suffice to establish a knowing and intelligent waiver of the Sixth Amendment right to counsel for purposes of postindictment questioning. <em>Patterson </em>v. <em><span class="citation" data-id="9431404"><a href="/opinion/112127/patterson-v-illinois/" aria-description="Citation for case: Patterson v. Illinois">Illinois, supra.</a></span></em></p>
<p id="b415-5">In <em>Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625</a></span> (1986), the Court created a bright-line rule for deciding whether an accused who has “asserted” his Sixth Amendment right to counsel has subsequently waived that right. Transposing the reasoning of <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981), which had announced an identical “prophylactic rule” in the Fifth Amendment context, see <em>Solem </em>v. <em>Stumes, </em><span class="citation" data-id="9429516"><a href="/opinion/111112/solem-v-stumes/#644" aria-description="Citation for case: Solem v. Stumes">465 U. S. 638, 644</a></span> (1984), we decided that after a defendant requests assistance of counsel, any waiver of Sixth Amendment rights given in a discussion initiated by police is presumed invalid, and evidence obtained pursuant to such a waiver is inadmissible in the prosecution’s case in chief. <span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#636" aria-description="Citation for case: Michigan v. Jackson"><em>Jackson, supra, </em>at 636</a></span>. Thus, to help guarantee that waivers are truly voluntary, <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>established a presumption which renders invalid some waivers that would be considered voluntary, knowing, and intelligent under the traditional case-by-case inquiry called for by <em>Brewer </em>v. <em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">Williams</a></span>.</em></p>
<p id="b415-6">There is no dispute in this case that respondent had a Sixth Amendment right to counsel at the time he gave the statement at issue. The State further concedes that the police transgressed the <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>rule, because the colloquy between respondent and the investigating officer “cannot be viewed as defendant-initiated interrogation.” Tr. of Oral Arg. 52. The question, then, is whether a statement to police taken in violation of <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>can be admitted to impeach a defendant’s inconsistent trial testimony.</p>
<p id="b415-7"><em>Michigan </em>v. <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>is based on the Sixth Amendment, but its roots lie in this Court’s decisions in <em>Miranda </em>v. <em>Ari</em><page-number citation-index="1" label="350">*350</page-number><em>zona, supra, </em>and succeeding cases. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>of course, required police interrogators to advise criminal suspects of their rights under the Fifth and Fourteenth Amendments and set forth a now-familiar set of suggested instructions for that purpose. Although recognizing that the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rules would result in the exclusion of some voluntary and reliable statements, the Court imposed these “prophylactic standards” on the States, see <em>Michigan </em>v. <em>Tucker, </em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#446" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 446</a></span> (1974), to safeguard the Fifth Amendment privilege against self-incrimination. <em>Edwards </em>v. <em>Arizona </em>added a second layer of protection to the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rules, holding that “when an accused has invoked his right to have counsel present during custodial interrogation, a valid waiver of that right cannot be established by showing only that he responded to further police-initiated custodial interrogation even if he has been advised of his rights.” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484</a></span>. <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>thus established another prophylactic rule designed to prevent police from badgering a defendant into waiving his previously asserted <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. See <em>Oregon </em>v. <em>Bradshaw, </em><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1044" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S. 1039, 1044</a></span> (1983) (plurality opinion).</p>
<p id="b416-5"><em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>simply superimposed the Fifth Amendment analysis of <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>onto the Sixth Amendment. Reasoning that “the Sixth Amendment right to counsel at a postarraignment interrogation requires at least as much protection as the Fifth Amendment right to counsel at any custodial interrogation,” <span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#632" aria-description="Citation for case: Michigan v. Jackson"><em>Jackson, supra, </em>at 632</a></span>, the Court in <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>concluded that the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>protections should apply when a suspect charged with a crime requests counsel outside the context of interrogation. This rule, like <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>, </em>is based on the supposition that suspects who assert their right to counsel are unlikely to waive that right voluntarily in subsequent interrogations.</p>
<p id="b416-6">We have already decided that although statements taken in violation of only the prophylactic <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rules may not be used in the prosecution’s case in chief, they are admissible to impeach conflicting testimony by the defendant. <em>Harris </em>v. <page-number citation-index="1" label="351">*351</page-number><em>New York, </em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971); <em>Oregon </em>v. <em>Hass, </em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714</a></span> (1975). The prosecution must not be allowed to build its case against a criminal defendant with evidence acquired in contravention of constitutional guarantees and their corresponding judicially created protections. But use of statements so obtained for impeachment purposes is a different matter. If a defendant exercises his right to testify on his own behalf, he assumes a reciprocal “obligation to speak truthfully and accurately,” <em>Harris, </em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#225" aria-description="Citation for case: Harris v. New York">401 U. S., at 225</a></span>, and we have consistently rejected arguments that would allow a defendant to “ ‘turn the illegal method by which evidence in the Government’s possession was obtained to his own advantage, and provide himself with a shield against contradiction of his untruths.’” <em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">Id.,</a></span> </em>at 224 (quoting <em>Walder </em>v. <em>United States, </em><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/#65" aria-description="Citation for case: Walder v. United States">347 U. S. 62, 65</a></span> (1954)). See also <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#722" aria-description="Citation for case: Oregon v. Hass"><em>Hass, supra, </em>at 722</a></span>; <em>United States </em>v. <em>Havens, </em><span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#626" aria-description="Citation for case: United States v. Havens">446 U. S. 620, 626</a></span> (1980).</p>
<p id="b417-5">There is no reason for a different result in a <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>case, where the prophylactic rule is designed to ensure voluntary, knowing, and intelligent waivers of the Sixth Amendment right to counsel rather than the Fifth Amendment privilege against self-incrimination or “right to counsel.” We have mandated the exclusion of reliable and probative evidence for <em>all </em>purposes only when it is derived from involuntary statements. <em>New Jersey </em>v. <em>Portash, </em><span class="citation" data-id="9427490"><a href="/opinion/110038/new-jersey-v-portash/#459" aria-description="Citation for case: New Jersey v. Portash">440 U. S. 450, 459</a></span> (1979) (compelled incriminating statements inadmissible for. impeachment purposes); <em>Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#398" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 398</a></span> (1978) (same). We have never prevented use by the prosecution of relevant voluntary statements by a defendant, particularly when the violations alleged by a defendant relate only to procedural safeguards that are “not themselves rights protected by the Constitution,” <em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker, supra,</a></span> </em>at 444 <em>CMiranda </em>rules), but are instead measures designed to ensure that constitutional rights are protected. In such cases, we have decided that the “search for truth in a criminal case” outweighs the “speculative possibility” that exclusion of evidence might deter future violations of rules not compelled di<page-number citation-index="1" label="352">*352</page-number>rectly by the Constitution in the first place. <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#722" aria-description="Citation for case: Oregon v. Hass"><em>Hass, supra, </em>at 722-723</a></span>; <span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#627" aria-description="Citation for case: United States v. Havens"><em>Havens, supra, </em>at 627</a></span> (reaffirming <em>Hass). Hass </em>was decided 15 years ago, and no new information has come to our attention which should lead us to think otherwise now.</p>
<p id="b418-5">Respondent argues that there should be a different exclusionary rule for <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>violations than for transgressions of <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>and <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>The distinction, he suggests, is that the adversarial process has commenced at the time of a <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>violation, and the postarraignment interrogations thus implicate the constitutional guarantee of the Sixth Amendment itself. But nothing in the Sixth Amendment prevents a suspect charged with a crime and represented by counsel from voluntarily choosing, on his own, to speak with police in the absence of an attorney. We have already held that a defendant whose Sixth Amendment right to counsel has attached by virtue of an indictment may execute a knowing and intelligent waiver of that right in the course of a police-initiated interrogation. <em>Patterson </em>v. <em>Illinois, </em><span class="citation" data-id="9431404"><a href="/opinion/112127/patterson-v-illinois/" aria-description="Citation for case: Patterson v. Illinois">487 U. S. 285</a></span> (1988). To be sure, once a defendant obtains or even requests counsel as respondent had here, analysis of the waiver issue changes. But that change is due to the protective rule we created in <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>based on the apparent inconsistency between a request fob counsel and a later voluntary decision to proceed without assistance. See <span class="citation" data-id="9431404"><a href="/opinion/112127/patterson-v-illinois/#290" aria-description="Citation for case: Patterson v. Illinois">487 U. S., at 290, n. 3</a></span>.; cf. <em>Michigan </em>v. <em>Mosley, </em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#110" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 110, n. 2</a></span> (1975) (White, J., concurring in result).</p>
<p id="b418-6">In other cases, we have explicitly declined to hold that a defendant who has obtained counsel cannot himself waive his right to counsel. See <em>Brewer, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#405" aria-description="Citation for case: Brewer v. Williams">430 U. S., at 405-406</a></span> (“The Court of Appeals did not hold, nor do we, that under the circumstances of this case Williams <em>could not, </em>without notice to counsel, have waived his rights under the Sixth and Fourteenth Amendments. It only held, as do we, that he did not”) (emphasis in original); <em>Estelle </em>v. <em>Smith, </em><span class="citation" data-id="9428322"><a href="/opinion/110474/estelle-v-smith/#471" aria-description="Citation for case: Estelle v. Smith">451 U. S. 454, 471-472, n. 16</a></span> (1981) (“We do not hold that respondent was precluded from waiving this constitutional right [to coun<page-number citation-index="1" label="353">*353</page-number>sel]. ... No such waiver has been shown, or even alleged, here”). A defendant’s right to rely on counsel as a “medium” between the defendant and the State attaches upon the initiation of formal charges, <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#176" aria-description="Citation for case: Maine v. Moulton">474 U. S., at 176</a></span>, and respondent’s contention that a defendant cannot execute a valid waiver of the right to counsel without first speaking to an attorney is foreclosed by our decision in <em><span class="citation" data-id="9431404"><a href="/opinion/112127/patterson-v-illinois/" aria-description="Citation for case: Patterson v. Illinois">Patterson</a></span>. </em>Moreover, respondent’s view would render the prophylactic rule adopted in <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>wholly unnecessary, because even waivers given during <em>defendant-initiated </em>conversations would be <em>per se </em>involuntary or otherwise invalid, unless counsel were first notified.</p>
<p id="b419-5">Although a defendant may sometimes later regret his decision to speak with police, the Sixth Amendment does not disable a criminal defendant from exercising his free will. To hold that a defendant is inherently incapable of relinquishing his right to counsel once it is invoked would be “to imprison a man in his privileges and call it the Constitution.” <em>Adams </em>v. <em>United States ex rel. McCann, </em><span class="citation" data-id="9419274"><a href="/opinion/103735/adams-v-united-states-ex-rel-mccann/#280" aria-description="Citation for case: Adams v. United States Ex Rel. McCann">317 U. S. 269, 280</a></span> (1942). This we decline to do. Both <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>and <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>establish prophylactic rules that render some otherwise valid waivers of constitutional rights invalid when they result from police-initiated interrogation, and in neither case should “the shield provided by [the prophylactic rule] be perverted into a license to use perjury by way of a defense, free from the risk of confrontation with prior inconsistent utterances.” <em>Harris, </em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#226" aria-description="Citation for case: Harris v. New York">401 U. S., at 226</a></span>.</p>
<p id="b419-6">Respondent and <em>amici </em>assert, alternatively, that the conduct of the police officer who took Harvey’s second statement violated the “core value” of the Sixth Amendment’s constitutional guarantee, and under those circumstances, the second statement may not be used even for impeachment purposes. They contend that respondent was affirmatively misled as to his need for counsel, and his purported waiver is therefore invalid. But on the record before us, it is not possible to determine whether Harvey’s waiver was knowing and volun<page-number citation-index="1" label="354">*354</page-number>tary. The state courts developed no record on that issue, and the Michigan Court of Appeals did not rest its holding on any such determination. There was no testimony on this point before the trial court. The only statement in the trial record concerning the issue of waiver is the prosecutor’s concession that the second statement was taken in violation of respondent’s <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. But that concession is consistent with the Michigan Court of Appeals’ finding that the police violated <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span>, </em>which is, after all, only a Sixth Amendment analogue to the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>decisions. The Michigan court made no independent inquiry into whether there had been an otherwise valid waiver .of the right to counsel, and respondent’s counsel himself conceded that, putting aside the prosecutor’s concession, the record is insufficient to determine whether there was a voluntary waiver of Sixth Amendment rights. Tr. of Oral Arg. 31-32. In short, the issue was never litigated in this case.</p>
<p id="b420-5">Because respondent’s counsel did not object at trial to the use of his second statement for impeachment purposes, the State had no occasion to offer evidence to establish that Harvey gave a knowing and voluntary waiver of his right to counsel under traditional standards. On remand, the Michigan courts are free to conduct a hearing on that question. It is the State’s burden to show that a waiver is knowing and voluntary, <em>Brewer </em>v. <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#404" aria-description="Citation for case: Brewer v. Williams"><em>Williams, supra, </em>at 404</a></span>, and if all the circumstances in a particular case show that the police have engaged in a course of conduct which would render the waiver involuntary, the burden will not be satisfied. Those facts are not before us, however, and we need not consider the admissibility for impeachment purposes of a voluntary statement obtained in the absence of a knowing and voluntary waiver of the right to counsel.</p>
<p id="b420-6">The judgment of the Michigan Court of Appeals is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b420-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b412-7"> Harvey declined to initial portions of the waiver form explaining that anything he said could be used against him in court, and that he could decide at any time to exercise his rights and not answer any questions or make any statement. App. to Pet. for Cert. 4a.</p>
</footnote>
<footnote label="2">
<p id="b413-6"> Respondent also told police that another man and woman had been present in Sharp’s house on the night of the incident and that he thought the man’s name was “Michael. ” At trial, however, respondent said that he did not know the man’s name. App. 36-37. Respondent further testified that “Michael” had brought some cocaine to Sharp’s home, but his statement to police only mentioned cocaine that respondent had provided. Id., at 39.</p>
</footnote>
</opinion>
```

---
