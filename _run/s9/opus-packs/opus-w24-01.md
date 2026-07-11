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

## GROUP: _overhaul2/lake/cases/new-york-v-p-j-video-inc--111635.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0c450e6699075052", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "new-york-v-p-j-video-inc--111635"}, "payload": {"all": [{"cite": "475 U.S. 868", "page": "868", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "475"}, {"cite": "106 S. Ct. 1610", "page": "1610", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "106"}, {"cite": "89 L. Ed. 2d 871", "page": "871", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "89"}, {"cite": "1986 U.S. LEXIS 104", "page": "104", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1986"}, {"cite": "54 U.S.L.W. 4396", "page": "4396", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "54"}], "display": null, "official": null, "official_selection_present": false, "record_id": "new-york-v-p-j-video-inc--111635"}}
{"assertion_id": "1d34a568459a06f7", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "new-york-v-p-j-video-inc--111635"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "new-york-v-p-j-video-inc--111635", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — new-york-v-p-j-video-inc--111635

```json
{
  "schema_version": "s2.v1",
  "record_id": "new-york-v-p-j-video-inc--111635",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "New York v. P. J. Video, Inc.",
    "case_name_short": "",
    "case_name_full": "NEW YORK v. P. J. VIDEO, INC., Dba NETWORK VIDEO, Et Al.",
    "input_case_name": "New York v. P. J. Video, Inc.",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-04-22",
    "year": 1986,
    "docket": "No. 85-363",
    "cluster_id": 111635,
    "lead_opinion_id": 9430437,
    "sibling_ids": [],
    "absolute_url": "/opinion/111635/new-york-v-p-j-video-inc/",
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
        "cite": "475 U.S. 868",
        "volume": "475",
        "reporter": "U.S.",
        "page": "868",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 1610",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1610",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 871",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "871",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4396",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4396",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 104",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "104",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "475 U.S. 868",
        "volume": "475",
        "reporter": "U.S.",
        "page": "868",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 1610",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1610",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 871",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "871",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 104",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "104",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4396",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4396",
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
    "date_created": "2026-07-06T13:44:32Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:44:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:44:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:44:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:44:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — new-york-v-p-j-video-inc--111635

```
<opinion type="majority">
<author id="b951-7">Justice Rehnquist</author>
<p id="A73">delivered the opinion of the Court.</p>
<p id="b951-8">This case concerns the proper standard for issuance of a warrant authorizing the seizure of materials presumptively protected by the First Amendment. Respondents P. J. Video, Inc., and James Erhardt were charged in the village of Depew, New York, Justice Court with six counts of obscenity in the third degree under § 235.05(1) of the New York Penal Law.<footnotemark>1</footnotemark> Respondents moved to suppress five videocassette movies that had been seized from respondents’ store, and that formed the basis for the obscenity charges <page-number citation-index="1" label="870">*870</page-number>against respondents, on the ground that the warrant authorizing the seizure was issued without probable cause to believe that the movies were obscene. The Justice Court granted the motion and dismissed the informations under which respondents were charged, and both the County Court of Erie County and the New York Court of Appeals affirmed. 65 N. Y. 2d 566, <span class="citation no-link">483 N. E. 2d 1120</span> (1985). We granted certiorari to resolve the conflict between the decision of the New York Court of Appeals in the instant case and the decisions in <em>Sequoia Books, Inc. </em>v. <em>McDonald, </em><span class="citation" data-id="8918957"><a href="/opinion/8928917/sequoia-books-inc-v-mcdonald/" aria-description="Citation for case: Sequoia Books, Inc. v. McDonald">725 F. 2d 1091</a></span> (CA7 1984), and <em>United States </em>v. <em>Pryba, </em>163 U. S. App. D. C. 389, <span class="citation" data-id="321241"><a href="/opinion/321241/united-states-v-dennis-e-pryba/" aria-description="Citation for case: United States v. Dennis E. Pryba">502 F. 2d 391</a></span> (1974), cert. denied, <span class="citation" data-id="8993957"><a href="/opinion/9001432/allred-v-north-carolina/" aria-description="Citation for case: Allred v. North Carolina">419 U. S. 1127</a></span> (1975). <span class="citation multiple-matches"><a href="/c/U.%20S./474/918/">474 U. S. 918</a></span> (1985). We now reverse the judgment of the Court of Appeals.</p>
<p id="b952-6">The obscenity charges against respondents arose out of an investigation by the Erie County District Attorney’s Office. Investigator David J. Groblewski was assigned to review 10 videocassette movies that had been rented from respondents’ store by a member of the Erie County Sheriff’s Department.<footnotemark>2</footnotemark> Groblewski viewed the movies in their entirety, and executed affidavits summarizing the theme of, and conduct depicted in, each film. The affidavits were attached to an application filed by the village of Depew Police Department for a warrant to search respondents’ store.</p>
<p id="b952-7">A justice of the New York Supreme Court issued the warrant, authorizing the search of the store and the seizure of the movies. The warrant was executed the next day and, according to a sworn, itemized inventory statement, the police seized 1 or 2 copies of each of the 10 movies. A total of 13 videocassettes were seized. The justice who had issued the warrant ordered that the videocassettes be temporarily <page-number citation-index="1" label="871">*871</page-number>retained by the police as evidence for trial. See N. Y. Crim. Proc. Law §§690.05-690.55 (McKinney 1984).</p>
<p id="b953-5">Respondents ultimately were charged in the village of Depew Justice Court with violating the New York obscenity laws with respect to only 5 of the 10 movies. The affidavits describing these five movies appear in full in the Appendix to this opinion.<footnotemark>3</footnotemark> Respondents moved for suppression of the seized videocassettes, alleging that the warrant authorizing their seizure was not supported by probable cause because the issuing justice had not personally viewed the movies. The Justice Court granted the motion and dismissed the in-formations under which respondents were charged, and on the State’s appeal the County Court of Erie County affirmed.</p>
<p id="b953-6">The New York Court of Appeals likewise affirmed, although on a different theory than that of the Justice Court. According to the Court of Appeals, “there is a higher standard for evaluation of a warrant application seeking to seize such things as books and films, as distinguished from one seeking to seize weapons or drugs, for example <em>(Roaden </em>v. <em>Kentucky, </em>[<span class="citation" data-id="9425416"><a href="/opinion/108854/roaden-v-kentucky/" aria-description="Citation for case: Roaden v. Kentucky">413 U. S. 496</a></span>], 504 [1973]; <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#730" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717, 730-731</a></span> [1961]). In applying the [Fourth] Amendment to such items, the court must act with ‘scrupulous exactitude’ <em>(Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481-485</a></span> [1965]; <em>see also, Maryland </em>v. <em>Macon, </em><span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/" aria-description="Citation for case: Maryland v. MacOn">472 U. S. 463</a></span> [1985]).” 65 N. Y. 2d, at 569-570, 483 N. E. 2d, at 1123 (footnote omitted). Using this “higher” probable-cause standard to review the affidavits submitted in support of the warrant application, the Court of Appeals stated:</p>
<blockquote id="b953-7">“Many of the scenes described contain explicit sexual activity, patently offensive by any constitutional standard, but the allegations of the affidavits do not indicate whether they constitute all, most or a few of the scenes <page-number citation-index="1" label="872">*872</page-number>presented in the films. . . . The descriptions of the action are not supplemented by references to the narrative or dialogue of the films and the affiant attempted to describe the ‘character’ or ‘theme’ of the movies by settings having nothing to do with the plot .... He made no attempt to reveal the story line (or lack of one) of the films or demonstrate that their ‘predominant appeal’ was to prurient interest. In short, none of the affidavits permit an inference that the scenes described are more than a catalog of offensive parts of the whole.” <em>Id., </em>at 570-571, 483 N. E. 2d, at 1124.</blockquote>
<p id="b954-5">The Court of Appeals concluded that the affidavits did not contain sufficient information to permit the issuing justice, “applying contemporary community standards, to judge the films as a whole and determine that they are within the statutory definitions of obscenity and thus are not entitled to constitutional protection.” <em>Id., </em>at 572, 483 N. E. 2d, at 1124 (footnote omitted). One judge dissented, arguing that the affidavits contained enough information for the issuing justice “to reasonably believe that the video movies were obscene as legislatively defined.” <em>Id., </em>at 573, 483 N. E. 2d, at 1125 (Jasen, J., dissenting).<footnotemark>4</footnotemark></p>
<p id="b955-4"><page-number citation-index="1" label="873">*873</page-number>We have long recognized that the seizure of films or books on the basis of their content implicates First Amendment concerns not raised by other kinds of seizures. For this reason, we have required that certain special conditions be met before such seizures may be carried out. In <em>Roaden </em>v. <em>Kentucky, </em><span class="citation" data-id="9425416"><a href="/opinion/108854/roaden-v-kentucky/" aria-description="Citation for case: Roaden v. Kentucky">413 U. S. 496</a></span> (1973), for example, we held that the police may not rely on the “exigency” exception to the Fourth Amendment’s warrant requirement in conducting a seizure of allegedly obscene materials, under circumstances where such a seizure would effectively constitute a “prior restraint.” In <em>A Quantity of Books </em>v. <em>Kansas, </em><span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">378 U. S. 205</a></span> (1964), and <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717</a></span> (1961), we had gone a step farther, ruling that the large-scale seizure of books or films constituting a “prior restraint” must be preceded by an adversary hearing on the question of obscenity. In <em>Heller </em>v. <em>New York, </em><span class="citation" data-id="9425413"><a href="/opinion/108853/heller-v-new-york/" aria-description="Citation for case: Heller v. New York">413 U. S. 483</a></span> (1973), we emphasized that, even where a seizure of allegedly obscene materials would not constitute a “prior restraint,” but instead would merely preserve evidence for trial, the seizure must be made pursuant to a warrant and there must be an opportunity for a prompt postseizure judicial determination of obscenity. And in <em>Lee Art Theatre, Inc. </em>v. <em>Virginia, </em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">392 U. S. 636</a></span> (1968), we held that a warrant authorizing the seizure of materials presumptively protected by the First Amendment may not issue based solely on the conclusory allegations of a police officer that the sought-after materials are obscene, but instead must be supported by affidavits setting forth specific facts in order <page-number citation-index="1" label="874">*874</page-number>that the issuing magistrate may “focus searchingly on the question of obscenity.” <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#732" aria-description="Citation for case: Marcus v. Search Warrant of Property"><em>Marcus, supra, </em>at 732</a></span>; see also <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#486" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 486</a></span> (1965).<footnotemark>5</footnotemark></p>
<p id="b956-5">The New York Court of Appeals construed our prior decisions in this area as standing for the additional proposition that an application for a warrant authorizing the seizure of books or films must be evaluated under a “higher” standard of probable cause than that used in other areas of Fourth Amendment law. But we have never held or said that such a “higher” standard is required by the First Amendment. In <em><span class="citation" data-id="9425413"><a href="/opinion/108853/heller-v-new-york/" aria-description="Citation for case: Heller v. New York">Heller</a></span>, </em>we said:</p>
<blockquote id="b956-6">“[S]eizing films to destroy them or to block their distribution or exhibition is a very different matter from seizing a single copy of a film for the <em>bona fide </em>purpose of preserving it as evidence in a criminal proceeding, particularly where, as here, there is no showing or pretrial claim that the seizure of the copy prevented continuing exhibition of the film. If such a seizure is pursuant to a warrant, <em>issued after a determination of probable cause by a neutral magistrate, </em>and, following the seizure, a prompt judicial determination of the obscenity issue in an adversary proceeding is available at the request of any interested party,' the seizure is constitutionally permissible. . . .</blockquote>
<blockquote id="b956-7"><em>“The necessity for a prior judicial determination of probable cause </em>will protect against gross abuses . . . .” 413 U. S., at 492-493 (emphasis added; footnotes omitted).</blockquote>
<p id="b957-4"><page-number citation-index="1" label="875">*875</page-number>We think that this passage from <em><span class="citation" data-id="9425413"><a href="/opinion/108853/heller-v-new-york/" aria-description="Citation for case: Heller v. New York">Heller</a></span>, </em>emphasizing the requirement that the magistrate determine probable cause as a means of safeguarding First Amendment interests, and eschewing any suggestion that the standard of probable cause in the First Amendment area is different than in other contexts, suggests that we saw no need for the latter requirement. In our view, the longstanding special protections described above, and enunciated in cases such as <em>Roaden, A Quantity of Books, Marcus, Heller, </em>and <em>Lee Art Theatre, </em>are adequate to ensure that First Amendment interests will not be impaired by the issuance and execution of warrants authorizing the seizure of books or films. We think, and accordingly hold, that an application for a warrant authorizing the seizure of materials presumptively protected by the First Amendment should be evaluated under the same standard of probable cause used to review warrant applications generally.<footnotemark>6</footnotemark></p>
<p id="b958-4"><page-number citation-index="1" label="876">*876</page-number>That standard was recently set forth by this Court in <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213</a></span> (1983):</p>
<blockquote id="b958-5">“‘[T]he term “probable cause,” . . . means less than evidence which would justify condemnation .... It imports a seizure made under circumstances which warrant suspicion.’ <em>[Locke </em>v. <em>United States, </em><span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/#348" aria-description="Citation for case: Locke v. United States">7 Cranch 339, 348</a></span> (1813).] . . . Finely tuned standards such as proof beyond a reasonable doubt or by a preponderance of the evidence, useful in formal trials, have no place in the magistrate’s decision.</blockquote>
<blockquote id="pArA">[[Image here]]</blockquote>
<blockquote id="b958-6">“The task of the issuing magistrate is simply to make a practical, common-sense decision whether, given all the circumstances set forth in the affidavit before him, . . . there is a fair probability that contraband or evidence of a crime will be found in a particular place. And the duty of a reviewing court is simply to ensure that the magistrate had a ‘substantial basis for. . . concluding,]’ <em>[Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#271" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 271</a></span> (1960),] that probable cause existed.” <em>Id., </em>at 235, 238-239.</blockquote>
<p id="b958-7">Applying the <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Gates</a></span> </em>standard to the affidavits in the instant case, we think it clear beyond peradventure that the warrant was supported by probable cause to believe that the five films at issue were obscene under New York law. Respondents concede that the affidavits describing the five films adequately established probable cause with respect to the second of the three elements of obscenity under the statute, namely, that the movies depicted “in a patently offensive manner” the various kinds of sexual conduct specified in the statute. See N. Y. Penal Law §235.00(l)(b) (McKinney 1980). Our review of the affidavits convinces us that the issuing justice also was given more than enough information to conclude that there was a “fair probability” that the movies satisfied <page-number citation-index="1" label="877">*877</page-number>the first and third elements of the statutory definition, namely, that the “predominant appeal [of the movies] is to the prurient interest in sex,” and that the movies “lac[k] serious literary, artistic, political, and scientific value.” See N. Y. Penal Law §§235.00(l)(a), (c) (McKinney 1980). As Judge Jasen of the Court of Appeals noted in his dissent in the present case:</p>
<blockquote id="b959-5">“Each of the affidavits describing the films clearly state at the outset that ‘the <em>content </em>and character of the above mentioned video movie is as follows.’ Inasmuch as the magistrate was reviewing affidavits describing movies which were advertised by defendants as ‘adult cassette movies,’ it was reasonable for him to believe that the affidavits faithfully and accurately described the substance of each movie as a whole. Each affidavit describes the numerous acts of deviate sexual intercourse and the objectification of women occurring in each film which the majority concede to be offensive. Each film is of relatively short duration. Manifestly, the acts described in each movie consume a substantial time span. Thus, the magistrate may reasonably have concluded that the described, successive acts of deviate sexual intercourse pervaded each film. When the title of each movie is considered together with its plot and setting, its general theme and serious value, if any, may reasonably be discerned. The films were described in each of the five nonconclusory affidavits in such a fashion as to permit the magistrate to focus searchingly on the issue of obscenity. Under these circumstances, there was a reasonable basis for the magistrate to authorize the seizure of the films in question.” 65 N. Y. 2d, at 580, 483 N. E. 2d, at 1130 (emphasis in original).</blockquote>
<p id="b959-6">We believe that the analysis and conclusion expressed by the dissenting judge are completely consistent with our statement in <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Gates</a></span> </em>that “probable cause requires only a prob<page-number citation-index="1" label="878">*878</page-number>ability or substantial chance of criminal activity, not an actual showing of such activity.” <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#244" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 244, n. 13</a></span>. We hold that, evaluated under the correct standard of probable cause, the warrant was properly issued and the videocassettes of the five movies should not have been suppressed. The judgment of the New York Court of Appeals is accordingly reversed, and the cause remanded to that court for further proceedings not inconsistent with this opinion.</p>
<p id="b960-5">
<em>It is so ordered.</em>
</p>
<p id="b960-6">APPENDIX TO OPINION OF THE COURT</p>
<p id="A6_Q">
<em>AFFIDAVIT</em>
</p>
<blockquote id="b960-7">STATE OF NEW YORK ) COUNTY OF ERIE ) SS: CITY OF BUFFALO )</blockquote>
<blockquote id="b960-10">DAVID J. GROBLEWSKI, being duly sworn, deposes and says:</blockquote>
<blockquote id="b960-11">I am presently a Confidential Criminal Investigator assigned to the Erie County District Attorney’s Office and prior to this, a member of the New York State Police for approximately 25 years.</blockquote>
<blockquote id="b960-12">On September 26th, 1983 I viewed the video tape movie “CALIFORNIA VALLEY GIRLS,” which was rented on September 20th, 1983, from Network Video, 5868 Transit Road, Depew, New York. This movie was rented by Detective Sergeant Vincent Costanza, a member of the Erie County Sheriff’s Department. This movie was viewed in my office starting at 12:00 Noon and lasted until 1:33 P.M.</blockquote>
<blockquote id="b960-13">The content and character of the above mentioned video movie is as follows: Six white females, approximately 18 to 25 years of age, are unemployed and attempt to make a living by <page-number citation-index="1" label="879">*879</page-number>becoming prostitutes. The first scene is a bedroom scene where two females are involved in love making, fondling and cunnilingus. The second scene depicts a white male and a white female having intercourse in the back of a van. The third scene is a house scene where six girls, all white females are introduced to the art of love making. One male, approximately 35 years of age, is teaching the girls the art of fellatio with each one of them performing this act on him. The next scene is a bedroom scene in a home where a husband and wife, a white male and a white female, alone with a girl, a white female, perform various sexual acts which include intercourse, fellatio, anal intercourse and cunnilingus. The movie ends with some lesbianism where the wife performs cunnilingus on the girl while she performs fellatio on the husband and they engage in intercourse and anal intercourse.</blockquote>
<blockquote id="b961-5">[Signature] David J. Groblewski Confidential Criminal Investigator</blockquote>
<blockquote id="b961-9">Subscribed and sworn to before me this [21] day of November, 1983.</blockquote>
<blockquote id="b961-10">[Signature] Notary Public</blockquote>
<p id="b961-12">
<em>AFFIDAVIT</em>
</p>
<blockquote id="b961-13">STATE OF NEW YORK ) COUNTY OF ERIE ) SS: CITY OF BUFFALO )</blockquote>
<blockquote id="b961-16">DAVID J. GROBLEWSKI, being duly sworn, deposes and says:</blockquote>
<blockquote id="b961-17">I am presently a Confidential Criminal Investigator assigned to the Erie County District Attorney’s Office and <page-number citation-index="1" label="880">*880</page-number>prior to this, a member of the New York State Police for approximately 25 years.</blockquote>
<blockquote id="b962-5">On September 23rd, 1983, I viewed the video tape movie “TABOO II,” which was rented on September 20th, 1983, from Network Video, 5868 Transit Road, Depew, New York. This movie was rented by Detective Sergeant Vincent Costanza, a member of the Erie County Sheriff’s Department. This movie was viewed in my office starting at 9:00 A.M. and with several interruptions lasted until 12:12 P.M.</blockquote>
<blockquote id="b962-6">The content and character of the above mentioned video movie: The theme of the movie is a middle-class neighborhood where a home is the place where all the sexual acts are performed. The movie starts with a brother and sister, a white male and white female, fondling each other. The second scene is another house scene where a white male and white female are giving a rubdown to a white female. The sexual acts that follow include cunnilingus and fellatio. There is also intercourse and the scene closes with the male placing his penis between the girl’s breasts and ejaculating into and over her mouth. In another scene there is some incestuous type activity between the brother and the sister where again fellatio and intercourse are performed. At one point during the movie the mother enters the bedroom and observes the two performing the sexual acts and becomes depressed about the situation. In a later scene the son and his mother are on a couch where they become involved in sexual acts of intercourse and fellatio. The movie closes with the mother and father asleep in their bedroom at which time the daughter enters and sleeps next to her father, where they perform incestuous acts of intercourse, and she performs fellatio on her father.</blockquote>
<blockquote id="b962-7">[Signature]</blockquote>
<blockquote id="b962-8">Subscribed and sworn to before me this [21] day of November, 1983</blockquote>
<blockquote id="b962-9">[Signature] Notary Public</blockquote>
<p id="b963-3">
<page-number citation-index="1" label="881">*881</page-number>
<em>AFFIDAVIT</em>
</p>
<blockquote id="b963-4">STATE OF NEW YORK ) COUNTY OF ERIE ) SS: CITY OF BUFFALO )</blockquote>
<blockquote id="b963-7">DAVID J. GROBLEWSKI, being duly sworn, deposes and says:</blockquote>
<blockquote id="b963-8">I am presently a Confidential Criminal Investigator assigned to the Erie County District Attorney’s Office and prior to this, a member of the New York State Police for approximately 25 years.</blockquote>
<blockquote id="b963-9">On September 29th, 1983, I viewed the video tape movie “TABOO,” which was rented on September 27th, 1983 from Network Video, 5868 Transit Road, Depew, New York. This movie was rented by Detective Sergeant Vincent Costanza, a member of the Erie County Sheriff’s Department. This movie was viewed in my office starting at 11:00 A.M. and lasted until 11:55 A.M. and watched again commencing at 1:42 P.M. and lasting until 2:23 P.M.</blockquote>
<blockquote id="b963-10">The content and character of the above mentioned video movie is as follows: The first scene is a bedroom scene where two white females and one white male perform various acts of fellatio, cunnilingus and intercourse. The second scene is a house party scene where many white males and white females are involved in various acts of intercourse, fellatio and cunnilingus. There is also a scene where females perform acts of cunnilingus on each other. The movie portrays at one point a bedroom scene with a white male, the son, laying in bed naked, at which time his mother, a white female enters the room. She makes love to him and incestuous acts of intercourse, placing of the penis between her breasts, ejaculation and cunnilingus are performed.</blockquote>
<blockquote id="b963-11">[Signature] David J. Groblewski Confidential Criminal Investigator</blockquote>
<blockquote id="b964-3"><page-number citation-index="1" label="882">*882</page-number>Subscribed and sworn to before me this [21] day of November, 1983</blockquote>
<blockquote id="b964-4">[Signature] Notary Public</blockquote>
<p id="b964-6">
<em>AFFIDAVIT</em>
</p>
<blockquote id="b964-7">STATE OF NEW YORK ) COUNTY OF ERIE ) SS: CITY OF BUFFALO )</blockquote>
<blockquote id="b964-10">DAVID J. GROBLEWSKI, being duly sworn, deposes and says:</blockquote>
<blockquote id="b964-11">I am presently a Confidential Criminal Investigator assigned to the Erie County District Attorney’s Office and prior to this, a member of the New York State Police for approximately 25 years.</blockquote>
<blockquote id="b964-12">On September 28th, 1983, Detective Sergeant Vincent Costanza, a Member of the Erie County Sheriff’s Department and I viewed the video tape movie “ALL AMERICAN GIRLS,” which was rented on September 27th, 1983 from Network Video, 5868 Transit Road, Depew, New York. This movie was viewed in my office starting at 11:35 A.M., and lasted until 1:00 P.M.</blockquote>
<blockquote id="b964-13">The content and character of the above mentioned video movie is as follows: The theme of the movie is a home of one of the six girls, all white females who had previously attended high school and were meeting for a reunion. The first scene is two girls in a room performing acts of lesbianism, namely cunnilingus on each other. They are met by a white male and they perform acts of fellatio on him, have intercourse and all leave the room. Throughout the movie the girls reminisce about their high school days with each one depicting her sexual acts with her male partner. The sex<page-number citation-index="1" label="883">*883</page-number>ual acts which followed included intercourse, fellatio and eunnilingus.</blockquote>
<blockquote id="b965-5">[Signature] David J. Groblewski Confidential Criminal Investigator</blockquote>
<blockquote id="b965-7">Subscribed and sworn to before me this [21] day of November, 1983</blockquote>
<blockquote id="b965-8">[Signature] Notary Public</blockquote>
<p id="b965-10">
<em>AFFIDAVIT</em>
</p>
<blockquote id="b965-11">STATE OF NEW YORK ) COUNTY OF ERIE ) SS: CITY OF BUFFALO )</blockquote>
<blockquote id="b965-14">DAVID J. GROBLEWSKI, being duly sworn, deposes and says:</blockquote>
<blockquote id="b965-15">I am presently a Confidential Criminal Investigator assigned to the Erie County District Attorney’s Office and prior to this, a member of the New York State Police for approximately 25 years.</blockquote>
<blockquote id="b965-16">On October 3rd, 1983, Detective Sergeant Vincent Costanza, a member of the Erie County Sheriff’s Department and I viewed the video tape movie “DEBBIE DOES DALLAS,” which was rented on September 30th, 1983, by Vincent Costanza from Network Video, 5868 Transit Road, Depew, New York. This movie was viewed in my office starting at 2:50 P.M. and lasted until 4:23 P.M.</blockquote>
<blockquote id="b965-17">The content and character of the above mentioned video movie is as follows: The theme of the movie is a girl moving out west for a change of atmosphere. The first scene is a jail scene where a white female is in jail after she had been put there by the so-called Sheriff, a white male, and she performs fellatio on him. The two then perform intercourse, at which <page-number citation-index="1" label="884">*884</page-number>time he removes his pants and ejaculates over her buttocks. The second scene is the ranch, a so-called house of ill repute, a bedroom scene in which a white male and a white female are involved in various sexual acts including fellatio, cunnilingus and intercourse. At the end of the scene the male ejaculates in and over the female’s mouth. The third scene, a bathroom scene, depicts some lesbianism involving three girls. They participate in love making, foreplay and performing cunnilingus on each other. Throughout, the movie depicts some lesbianism along with sexual acts of intercourse, fellatio and cunnilingus.</blockquote>
<blockquote id="b966-5">[Signature] David J. Groblewski Confidential Criminal Investigator</blockquote>
<blockquote id="b966-7">Subscribed and sworn to before me this [21] day of November, 1983</blockquote>
<blockquote id="b966-8">[Signature] Notary Public</blockquote>
<footnote label="1">
<p id="b951-10"> Section 235.05(1) (McKinney Supp. 1986) provides:</p>
<blockquote id="b951-11">“A person is guilty of obscenity in the third degree when, knowing its content and character, he:</blockquote>
<blockquote id="b951-12">“1. Promotes, or possesses with intent to promote, any obscene material. . . .”</blockquote>
<blockquote id="b951-13">“Obscenity in the third degree is a class A misdemeanor.”</blockquote>
<p id="b951-14">The statutory definition of “obscenity,” which is derived from <em>Miller </em>v. <em>California, </em><span class="citation" data-id="9425379"><a href="/opinion/108838/miller-v-california/" aria-description="Citation for case: Miller v. California">413 U. S. 15</a></span> (1973), appears at § 235.00(1) (McKinney 1980):</p>
<blockquote id="A4F">“. . . Any material or performance is ‘obscene’ if (a) the average person, applying contemporary community standards, would find that considered as a whole, its predominant appeal is to the prurient interest in sex, and (b) it depicts or describes in a patently offensive manner, actual or simulated: sexual intercourse, sodomy, sexual bestiality, masturbation, sadism, masochism, excretion or lewd exhibition of the genitals, and (c) considered as a whole, it lacks serious literary, artistic, political, and scientific value. Predominant appeal shall be judged with reference to ordinary adults unless it appears from the character of the material or the circumstances of its dissemination to be designed for children or other specially susceptible audiences.”</blockquote>
</footnote>
<footnote label="2">
<p id="b952-8"> The 10 movies were entitled “California Valley Girls,” “Taboo II,” “Taboo,” “All American Girls,” “Debbie Does Dallas,” “Body Magic,” “Deep Throat,” “Every Which Way She Can,” “Filthy Rich,” and “Little Girls Blue.”</p>
</footnote>
<footnote label="3">
<p id="b953-8"> The five movies that formed the basis for the obscenity charges against respondents were “California Valley Girls,” “Taboo II,” “Taboo,” “All American Girls,” and “Debbie Does Dallas.”</p>
</footnote>
<footnote label="4">
<p id="b954-6"> Respondents argue that the decision of the New York Court of Appeals rested on adequate and independent state grounds, namely, provisions of the New York Constitution and various state-court decisions, and that we therefore lack jurisdiction to review that decision. We disagree. As we explained in <em>Caldwell </em>v. <em>Mississippi, </em><span class="citation" data-id="111471"><a href="/opinion/111471/caldwell-v-mississippi/" aria-description="Citation for case: Caldwell v. Mississippi">472 U. S. 320</a></span> (1985):</p>
<blockquote id="b954-7">“[W]e will not assume that a state-court decision rests on adequate and independent state grounds when the ‘state court decision fairly appears to rest primarily on federal law, or to be interwoven with the federal law, and when the adequacy and independence of any possible state law ground is not clear from the face of the opinion.”’ <span class="citation" data-id="111471"><a href="/opinion/111471/caldwell-v-mississippi/#327" aria-description="Citation for case: Caldwell v. Mississippi"><em>Id., </em>at 327</a></span>, quoting <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1040-1041</a></span> (1983).</blockquote>
<p id="b954-8">Here, the New York Court of Appeals cited the New York Constitution only once,'near the beginning of its opinion, and in the same parenthetical also cited the Fourth Amendment to the United States Constitution. Moreover, the Court of Appeals repeatedly referred to the “First Amend<page-number citation-index="1" label="873">*873</page-number>ment” and “Fourth Amendment” during its discussion of the merits of the case, strongly indicating that it believed that its decision was governed by federal law. Finally, although the Court of Appeals cited several state-court decisions, the only citations appended to the crucial language quoted in the text were to the federal decisions in <em>Roaden </em>v. <em>Kentucky, </em><span class="citation" data-id="9425416"><a href="/opinion/108854/roaden-v-kentucky/" aria-description="Citation for case: Roaden v. Kentucky">413 U. S. 496</a></span> (1973), <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717</a></span> (1961), <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476</a></span> (1966), and <em>Maryland </em>v. <em>Macon, </em><span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/" aria-description="Citation for case: Maryland v. MacOn">472 U. S. 463</a></span> (1985). We conclude, in the absence of a “plain statement” to the contrary, that the decision of the Court of Appeals was premised on federal, not state, law.</p>
</footnote>
<footnote label="5">
<p id="b956-8"> Contrary to the position apparently taken by the Justice Court in the instant case, we have never held that a magistrate must personally view allegedly obscene films prior to issuing a warrant authorizing their seizure. See <em>Lee Art Theatre, Inc. </em>v. <em>Virginia, </em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/#637" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">392 U. S., at 637</a></span>. On the contrary, we think that a reasonably specific affidavit describing the content of a film generally provides an adequate basis for the magistrate to determine whether there is probable cause to believe that the film is obscene, and whether a warrant authorizing the seizure of the film should issue.</p>
</footnote>
<footnote label="6">
<p id="b957-5"> Respondents contend that the seizure in the instant case was not limited to only one copy of each film, but instead extended to all copies of the films that the police were able to find during their search of respondents’ store. According to respondents, the seizure had the effect of severely restricting public access to the films, and thereby constituted a “prior restraint.” Respondents therefore argue that this case is properly governed not by <em>Heller </em>v. <em>New York, </em><span class="citation" data-id="9425413"><a href="/opinion/108853/heller-v-new-york/" aria-description="Citation for case: Heller v. New York">413 U. S. 483</a></span> (1973), but by <em>Roaden </em>v. <em><span class="citation" data-id="9425416"><a href="/opinion/108854/roaden-v-kentucky/" aria-description="Citation for case: Roaden v. Kentucky">Kentucky, supra,</a></span> </em>where this Court stated that the seizure of an allegedly obscene film, under circumstances where the seizure “brought to an abrupt halt an orderly and presumptively legitimate . . . exhibition” of the film, “calls for a higher hurdle in the evaluation of reasonableness.” <span class="citation" data-id="9425416"><a href="/opinion/108854/roaden-v-kentucky/#504" aria-description="Citation for case: Roaden v. Kentucky"><em>Id., </em>at 504</a></span>.</p>
<p id="b957-6">We reject this contention. Our reference in <em><span class="citation" data-id="9425416"><a href="/opinion/108854/roaden-v-kentucky/" aria-description="Citation for case: Roaden v. Kentucky">Roaden</a></span> </em>to a “higher hurdle ... of reasonableness” was not intended to establish a “higher” standard of probable cause for the issuance of a warrant to seize books or films, but instead related to the more basic requirement, imposed by that decision, that the police not rely on the “exigency” exception to the Fourth Amendment warrant requirement, but instead obtain a warrant from a magistrate who has ‘“foeus[ed] searchingly on the question of obscenity.’” <span class="citation" data-id="9425416"><a href="/opinion/108854/roaden-v-kentucky/#506" aria-description="Citation for case: Roaden v. Kentucky"><em>Id., </em>at 506</a></span>, quoting <em>Marcus </em>v. <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#732" aria-description="Citation for case: Marcus v. Search Warrant of Property"><em>Search Warrant, supra, </em>at 732</a></span>.</p>
<p id="b957-7">We also note that the burden is on the defendant to make a pretrial showing of a “substantial restraint” if he wishes to escape the rule of <em><span class="citation" data-id="9425413"><a href="/opinion/108853/heller-v-new-york/" aria-description="Citation for case: Heller v. New York">Heller, supra,</a></span> </em>that a mere seizure to preserve evidence does not impose on <page-number citation-index="1" label="876">*876</page-number>the State a duty to conduct an adversary hearing of the sort described in <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus, supra.</a></span> </em>Respondents made no such pretrial showing in this case.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/o-brien-v-united-states--107396.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "822b75c17ac84838", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "o-brien-v-united-states--107396"}, "payload": {"all": [{"cite": "386 U.S. 345", "page": "345", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "386"}, {"cite": "87 S. Ct. 1158", "page": "1158", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "87"}, {"cite": "18 L. Ed. 2d 94", "page": "94", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "18"}, {"cite": "1967 U.S. LEXIS 1984", "page": "1984", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1967"}], "display": null, "official": null, "official_selection_present": false, "record_id": "o-brien-v-united-states--107396"}}
{"assertion_id": "88a71594f4eafea1", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "o-brien-v-united-states--107396"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "o-brien-v-united-states--107396", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — o-brien-v-united-states--107396

```json
{
  "schema_version": "s2.v1",
  "record_id": "o-brien-v-united-states--107396",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "O'BRIEN v. United States",
    "case_name_short": "O'BRIEN",
    "case_name_full": "O\u2019BRIEN Et Al. v. UNITED STATES",
    "input_case_name": "O'Brien v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-03-20",
    "year": 1967,
    "docket": null,
    "cluster_id": 107396,
    "lead_opinion_id": 9423374,
    "sibling_ids": [],
    "absolute_url": "/opinion/107396/obrien-v-united-states/",
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
        "cite": "386 U.S. 345",
        "volume": "386",
        "reporter": "U.S.",
        "page": "345",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 1158",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1158",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 94",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "94",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 1984",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1984",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "386 U.S. 345",
        "volume": "386",
        "reporter": "U.S.",
        "page": "345",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 1158",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1158",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 94",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "94",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 1984",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1984",
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
    "date_created": "2026-07-06T13:52:15Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:52:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:52:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:52:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:52:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — o-brien-v-united-states--107396

```
<opinion type="majority">
<author id="b423-11">■ Per Curiam.</author>
<p id="b423-12">The petition for a writ of certiorari is granted, judgment vacated and the case is remanded to the United States District Court for the Eastern District of Michigan for a new trial should the Government seek to prosecute petitioners anew. <em>Black </em>v. <em>United States, </em><span class="citation" data-id="9423273"><a href="/opinion/107287/black-v-united-states/" aria-description="Citation for case: Black v. United States">385 U. S. 26</a></span>.</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/people-v-seymour--10018335.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4361cd456dc8dc63", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "people-v-seymour--10018335"}, "payload": {"all": [{"cite": "526 P.3d 954", "page": "954", "reporter": "P.3d", "selected_official": false, "source": "cluster.citations[]", "type": 3, "volume": "526"}], "display": null, "official": null, "official_selection_present": false, "record_id": "people-v-seymour--10018335"}}
{"assertion_id": "33d48c313375de48", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "people-v-seymour--10018335"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "people-v-seymour--10018335", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — people-v-seymour--10018335

```json
{
  "schema_version": "s2.v1",
  "record_id": "people-v-seymour--10018335",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "In re: The PEOPLE of the State of Colorado v. Gavin SEYMOUR",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "People v. Seymour",
    "court": "Colo. 2023",
    "court_id": "colo",
    "court_level": "state",
    "circuit": null,
    "state": "co",
    "date_decided": "2023-01-17",
    "year": 2023,
    "docket": "2023 CO 53",
    "cluster_id": 10018335,
    "lead_opinion_id": 10484936,
    "sibling_ids": [],
    "absolute_url": "/opinion/10018335/in-re-the-people-of-the-state-of-colorado-v-gavin-seymour/",
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
        "cite": "526 P.3d 954",
        "volume": "526",
        "reporter": "P.3d",
        "page": "954",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "526 P.3d 954",
        "volume": "526",
        "reporter": "P.3d",
        "page": "954",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "other",
      "selected": null,
      "reason": "unlisted_reporter:P.3d"
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
    "date_created": "2026-07-06T13:12:33Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:12:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:12:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:12:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:12:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — people-v-seymour--10018335

```
<div><div class="content"><div class="html-children"><div><header><center><b></b><p><span class="citation no-link">526 P.3d 954</span>  (Mem)</p><p>In re: The PEOPLE of the State of Colorado, Plaintiff,<br>v.<br>Gavin SEYMOUR, Defendant.</p><p>Supreme Court Case No: 2023SA12<br></p><p>Supreme Court of Colorado.</p><p>Date Filed: January 17, 2023</p></center></header><br><p>ORDER AND RULE TO SHOW CAUSE</p><p>Upon consideration of the Petition for Rule to Show Cause Pursuant to C.A.R. 21 filed in the above entitled action and matter, and being sufficiently advised in the premises,</p><p>IT IS ORDERED that a Rule to Show Cause issue out of this court. Therefore, Respondents, The People of the State of Colorado and Denver District Court are directed to answer, in writing, on or before February 14, 2023, why the relief requested in the petition should not be granted.</p><p>IT IS FURTHER ORDERED that Petitioner, Gavin Seymour, has 21 days from receipt of the answer within which to reply.</p><p>Pursuant to C.A.R. 21(f)(2), all further proceedings are stayed until further order of this court.</p></div></div></div></div>
```

---

## GROUP: _overhaul2/lake/cases/reichle-v-howards--801500.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f4978367f53094a7", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "reichle-v-howards--801500"}, "payload": {"all": [{"cite": "132 S. Ct. 2088", "page": "2088", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "132"}, {"cite": "182 L. Ed. 2d 985", "page": "985", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "182"}, {"cite": "2012 U.S. LEXIS 4132", "page": "4132", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2012"}, {"cite": "566 U.S. 658", "page": "658", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "566"}], "display": null, "official": null, "official_selection_present": false, "record_id": "reichle-v-howards--801500"}}
{"assertion_id": "53c973e2d5d438aa", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "reichle-v-howards--801500"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "reichle-v-howards--801500", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — reichle-v-howards--801500

```json
{
  "schema_version": "s2.v1",
  "record_id": "reichle-v-howards--801500",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Reichle v. Howards",
    "case_name_short": "Reichle",
    "case_name_full": "REICHLE Et Al. v. HOWARDS",
    "input_case_name": "Reichle v. Howards",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2012-06-04",
    "year": 2012,
    "docket": "No. 11-262",
    "cluster_id": 801500,
    "lead_opinion_id": 9500600,
    "sibling_ids": [],
    "absolute_url": "/opinion/801500/reichle-v-howards/",
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
        "cite": "132 S. Ct. 2088",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "2088",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "182 L. Ed. 2d 985",
        "volume": "182",
        "reporter": "L. Ed. 2d",
        "page": "985",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "566 U.S. 658",
        "volume": "566",
        "reporter": "U.S.",
        "page": "658",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2012 U.S. LEXIS 4132",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "4132",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "132 S. Ct. 2088",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "2088",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "182 L. Ed. 2d 985",
        "volume": "182",
        "reporter": "L. Ed. 2d",
        "page": "985",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 U.S. LEXIS 4132",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "4132",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "566 U.S. 658",
        "volume": "566",
        "reporter": "U.S.",
        "page": "658",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "other",
      "selected": null,
      "reason": "unlisted_reporter:S. Ct."
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
    "date_created": "2026-07-06T13:17:51Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:18:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:18:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:18:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:18:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — reichle-v-howards--801500

```
<opinion type="majority">
<author id="b740-6">Justice Thomas</author>
<p id="AAf-">delivered the opinion of the Court.</p>
<p id="b740-7">This case requires us to decide whether two federal law enforcement agents are immune from suit for allegedly arresting a suspect in retaliation for his political speech, when the agents had probable cause to arrest the suspect for committing a federal crime.</p>
<p id="b740-8">I</p>
<p id="b740-9">On June 16, 2006, Vice President Richard Cheney visited a shopping mall in Beaver Creek, Colorado. A Secret Service protective detail accompanied the Vice President. Petitioners Gus Reichle and Dan Doyle were members of that detail.</p>
<p id="b740-10">Respondent Steven Howards was also at the mall. He was. engaged in a cell phone conversation when he noticed the Vice President greeting members of the public. Agent Doyle overheard Howards say, during this conversation, “ ‘I’m going to ask [the Vice President] how many kids he’s killed today.’” Brief for Petitioners 4. Agent Doyle told two other agents what he had heard, and the three of them began monitoring Howards more closely.</p>
<p id="b740-11">Agent Doyle watched Howards enter the line to meet the Vice President. When Howards approached the Vice Presi<page-number citation-index="1" label="661">*661</page-number>dent, he told him that his “ ‘policies in Iraq are disgusting.’ ” <em>Ibid. </em>The Vice President simply thanked Howards and moved along, but Howards touched the Vice President’s shoulder as the Vice President departed.<footnotemark>1</footnotemark> Howards then walked away.</p>
<p id="b741-5">Several agents observed Howards’ encounter with the Vice President. The agents determined that Agent Reichle, who coordinated the protective intelligence team responsible for interviewing individuals suspected of violating the law, should question Howards. Agent Reichle had not personally heard Howards’ comments or seen his contact with the Vice President, but Agent Doyle briefed Agent Reichle on what had happened.</p>
<p id="b741-6">Agent Reichle approached Howards, presented his badge and identified himself, and asked to speak with him. How-ards refused and attempted to walk away. At that point, Agent Reichle stepped in front of Howards and asked if he had assaulted the Vice President. Pointing his finger at Agent Reichle, Howards denied assaulting the Vice President and told Agent Reichle, “if you don’t want other people sharing their opinions, you should have him [the Vice President] avoid public places.” <em>Howards </em>v. <em>McLaughlin, </em><span class="citation" data-id="9441235"><a href="/opinion/212271/howards-v-mclaughlin/#1137" aria-description="Citation for case: Howards v. McLaughlin">634 F. 3d 1131,1137</a></span> (CA10 2011) (internal quotation marks omitted). During this exchange, Agent Reichle also asked How-ards whether he had touched the Vice President. Howards falsely denied doing so. After confirming that Agent Doyle had indeed seen Howards touch the Vice President, Reichle arrested Howards.</p>
<p id="b741-7">The Secret Service transferred Howards to the custody of the local sheriff’s department. Howards was' charged by local officials with harassment in violation of state law. The charge was eventually dismissed.</p>
<p id="AAv"><page-number citation-index="1" label="662">*662</page-number>I — i H-1</p>
<p id="AkGs">Howards brought this action in the United States District Court for the District of Colorado under Rev. Stat. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>, and <em>Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971).<footnotemark>2</footnotemark> Howards alleged that he was arrested and searched without probable cause, in violation of the Fourth Amendment. Howards also alleged that he was arrested in retaliation for criticizing the Vice President, in violation of the First Amendment.</p>
<p id="AHV">Petitioners Reichle and Doyle moved for summary judgment on the ground that they were entitled to qualified immunity. The District Court denied the motion. See App. to Pet. for Cert. 46-61. On interlocutory appeal, a divided panel of the United States Court of Appeals for the Tenth Circuit affirmed in part and reversed in part. <span class="citation" data-id="9441235"><a href="/opinion/212271/howards-v-mclaughlin/" aria-description="Citation for case: Howards v. McLaughlin">634 F. 3d 1131</a></span>.</p>
<p id="Al2A">The Court of Appeals held that petitioners enjoyed qualified immunity with respect to Howards’ Fourth Amendment claim. The court concluded that petitioners had probable cause to arrest Howards for making a materially false statement to a federal official in violation of <span class="citation no-link">18 U. S. C. § 1001</span> because he falsely denied touching the Vice President. <span class="citation" data-id="9441235"><a href="/opinion/212271/howards-v-mclaughlin/#1142" aria-description="Citation for case: Howards v. McLaughlin">634 F. 3d, at 1142</a></span>. Thus, the court concluded that neither How-ards’ arrest nor search incident to the arrest violated the Fourth Amendment.<footnotemark>3</footnotemark> <span class="citation" data-id="9441235"><a href="/opinion/212271/howards-v-mclaughlin/#1142" aria-description="Citation for case: Howards v. McLaughlin"><em>Id., </em>at 1142-1143</a></span>.</p>
<p id="AX5">However, the Court of Appeals denied petitioners qualified immunity from Howards’ First Amendment claim. The court first determined that Howards had established a material factual dispute regarding whether petitioners were substantially motivated by Howards’ speech when they arrested <page-number citation-index="1" label="663">*663</page-number>him. <span class="citation" data-id="9441235"><a href="/opinion/212271/howards-v-mclaughlin/#1144" aria-description="Citation for case: Howards v. McLaughlin"><em>Id., </em>at 1144-1145</a></span>. The court then rejected petitioners’ argument that, under this Court’s decision in <em>Hartman </em>v. <span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore"><em>Moore, 547 </em>U. S. 250</a></span> (2006), probable cause to arrest defeats a First Amendment claim of retaliatory arrest. The court concluded that <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>established such a rule only for retaliatory prosecution claims and, therefore, did not upset prior Tenth Circuit precedent clearly establishing that a retaliatory <em>arrest </em>violates the First Amendment even if supported by probable cause. <span class="citation" data-id="9441235"><a href="/opinion/212271/howards-v-mclaughlin/#1148" aria-description="Citation for case: Howards v. McLaughlin">634 F. 3d, at 1148</a></span>.</p>
<p id="b743-5">Judge Paul Kelly dissented from the court’s denial of qualified immunity. He would have held that when Howards was arrested, it was not clearly established that an arrest supported by probable cause could violate the First Amendment. In Judge Kelly’s view, <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>called into serious question the Tenth Circuit’s prior precedent on retaliatory arrests. <span class="citation" data-id="9441235"><a href="/opinion/212271/howards-v-mclaughlin/#1151" aria-description="Citation for case: Howards v. McLaughlin">634 F. 3d, at 1151</a></span>. He noted that other Circuits had applied <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>to retaliatory arrests and that there was a “strong argument” in favor of doing so. <span class="citation" data-id="9441235"><a href="/opinion/212271/howards-v-mclaughlin/#1151" aria-description="Citation for case: Howards v. McLaughlin">634 F. 3d, at 1151-1152</a></span>.</p>
<p id="b743-6">We granted certiorari on two questions: whether a First Amendment retaliatory arrest claim may lie despite the presence of probable cause to support the arrest, and whether clearly established law at the time of Howards’ arrest so held. See <span class="citation multiple-matches"><a href="/c/U.%20S./565/1078/">565 U. S. 1078</a></span> (2011). If the answer to either question is “no,” then the agents are entitled to qualified immunity. We elect to address only the second question. We conclude that, at the time of Howards’ arrest, it was not clearly established that an arrest supported by probable cause could violate the First Amendment. We, therefore, reverse the judgment of the Court of Appeals denying petitioners qualified immunity.<footnotemark>4</footnotemark></p>
<p id="ARTF"><page-number citation-index="1" label="664">*664</page-number>III</p>
<p id="AGNO">Qualified immunity shields government officials from civil damages liability unless the official violated a statutory or constitutional right that was clearly established at the time of the challenged conduct. See <em>Ashcroft </em>v. <em>al-Kidd, </em><span class="citation" data-id="7262676"><a href="/opinion/7344719/ashcroft-v-al-kidd/#735" aria-description="Citation for case: Ashcroft v. al-Kidd">563 U. S. 731, 735</a></span> (2011). In <em>Pearson </em>v. <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/#236" aria-description="Citation for case: Pearson v. Callahan"><em>Callahan, 555 </em>U. S. 223, 236</a></span> (2009), we held that courts may grant qualified immunity on the ground that a purported right was not “clearly established” by prior case law, without resolving the often more difficult question whether the purported right exists at all. <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/#227" aria-description="Citation for case: Pearson v. Callahan"><em>Id., </em>at 227</a></span>. This approach comports with our usual reluctance to decide constitutional questions unnecessarily. <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/#241" aria-description="Citation for case: Pearson v. Callahan"><em>Id., </em>at 241</a></span>; see also <em>Camreta </em>v. <em>Greene, </em><span class="citation" data-id="7262672"><a href="/opinion/7344718/camreta-v-greene/#705" aria-description="Citation for case: Camreta v. Greene">563 U. S. 692, 705-706</a></span> (2011); <em>al-Kidd, </em><span class="citation" data-id="7262676"><a href="/opinion/7344719/ashcroft-v-al-kidd/#735" aria-description="Citation for case: Ashcroft v. al-Kidd">563 U. S., at 735</a></span>.</p>
<p id="Axtb">To be clearly established, a right must be sufficiently, clear “that every 'reasonable official would-[have understood] that what he is doing violates that right/ ” <em><span class="citation" data-id="7262676"><a href="/opinion/7344719/ashcroft-v-al-kidd/" aria-description="Citation for case: Ashcroft v. al-Kidd">Id.,</a></span> </em>at 741 (quoting <em>Anderson </em>v. <em>Creighton, </em><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#640" aria-description="Citation for case: Anderson v. Creighton">483 U. S. 635, 640</a></span> (1987)). In other words, “existing precedent must have placed the statutory or constitutional question beyond debate.” <span class="citation" data-id="7262676"><a href="/opinion/7344719/ashcroft-v-al-kidd/#741" aria-description="Citation for case: Ashcroft v. al-Kidd"><em>al-Kidd, supra, </em>at 741</a></span>. This “clearly established” standard protects the balance between vindication of constitutional rights and government officials’ effective performance of their duties by ensuring that officials can “ ‘reasonably . . . anticipate when their conduct may give rise to liability for damages.’ ” <em><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">Anderson, supra,</a></span> </em>at 639 (quoting <em>Davis </em>v. <em>Scherer, </em><span class="citation" data-id="9429708"><a href="/opinion/111241/davis-v-scherer/#195" aria-description="Citation for case: Davis v. Scherer">468 U. S. 183, 195</a></span> (1984)).</p>
<p id="ATT">The “clearly established” standard is not satisfied here. This Court has never recognized a First Amendment right to be free from a retaliatory arrest that is supported by <page-number citation-index="1" label="665">*665</page-number>probable cause; nor was such a right otherwise clearly established at the time of Howards’ arrest.</p>
<p id="b745-5">A</p>
<p id="b745-6">■ ■ Howards contends that our cases have “ ‘settled’ ” the rule that, “ ‘as a general matterf,] the First Amendment prohibits government officials from subjecting an individual to retaliatory actions’ ” for his speech. See Brief for Respondent 39 (quoting <span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/#256" aria-description="Citation for case: Hartman v. Moore"><em>Hartman, supra, </em>at 256</a></span>). But we have previously explained that the right allegedly violated must be established, “ ‘not as a broad general proposition,’ ” <em>Brosseau </em>v. <em>Haugen, </em><span class="citation" data-id="9434715"><a href="/opinion/137736/brosseau-v-haugen/#198" aria-description="Citation for case: Brosseau v. Haugen">543 U. S. 194, 198</a></span> (2004) <em>(per curiam), </em>but in a “particularized” sense so that the “contours” of the right are clear to a reasonable official, <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#640" aria-description="Citation for case: Anderson v. Creighton"><em>Anderson, supra, </em>at 640</a></span>. Here, the right in question is not the general right to be free from retaliation for one’s speech, but the more specific right to be free from a retaliatory arrest that is otherwise supported by probable cause. This Court has never held that there is such a right.<footnotemark>5</footnotemark></p>
<p id="b745-7">B</p>
<p id="b745-8">We next consider Tenth Circuit precedent. Assuming, <em>arguendo, </em>that controlling Court of Appeals’ authority could be a dispositive source of clearly established law in the cir<page-number citation-index="1" label="666">*666</page-number>cumstances of this case, the Tenth Circuit’s cases do not satisfy the “clearly established” standard here.</p>
<p id="b746-5">Relying on <em>DeLoach </em>v. <em>Bevers, </em><span class="citation" data-id="553431"><a href="/opinion/553431/camille-deloach-v-mitzi-bevers/" aria-description="Citation for case: Camille Deloach v. Mitzi Bevers">922 F. 2d 618</a></span> (1990), and <em>Poole </em>v. <em>County of Otero, </em><span class="citation" data-id="161553"><a href="/opinion/161553/poole-v-county-of-otero/" aria-description="Citation for case: Poole v. County of Otero">271 F. 3d 955</a></span> (2001), the Court of Appeals concluded that, at the time of Howards’ arrest, its precedent had clearly established the unlawfulness of an arrest in retaliation for the exercise of First Amendment rights, irrespective of probable cause. In <em><span class="citation" data-id="553431"><a href="/opinion/553431/camille-deloach-v-mitzi-bevers/" aria-description="Citation for case: Camille Deloach v. Mitzi Bevers">DeLoach</a></span>, </em>a case involving both a retaliatory arrest and a retaliatory prosecution, the court held that “[a]n act taken in retaliation for the exercise of a constitutionally protected right is actionable under § 1983 even if the act, when taken for a different reason, would have been proper.” <span class="citation" data-id="553431"><a href="/opinion/553431/camille-deloach-v-mitzi-bevers/#620" aria-description="Citation for case: Camille Deloach v. Mitzi Bevers">922 F. 2d, at 620</a></span> (internal quotation marks omitted). In <em><span class="citation" data-id="161553"><a href="/opinion/161553/poole-v-county-of-otero/" aria-description="Citation for case: Poole v. County of Otero">Poole</a></span>, </em>a subsequent retaliatory prosecution case, the court relied on <em><span class="citation" data-id="553431"><a href="/opinion/553431/camille-deloach-v-mitzi-bevers/" aria-description="Citation for case: Camille Deloach v. Mitzi Bevers">DeLoach</a></span> </em>for the proposition that a plaintiff’s illegal conduct is “not relevant to his First Amendment claim.” <span class="citation" data-id="161553"><a href="/opinion/161553/poole-v-county-of-otero/#961" aria-description="Citation for case: Poole v. County of Otero">271 F. 3d, at 961</a></span>.</p>
<p id="b746-6">The Court of Appeals acknowledged that <em><span class="citation" data-id="161553"><a href="/opinion/161553/poole-v-county-of-otero/" aria-description="Citation for case: Poole v. County of Otero">Poole</a></span> </em>was abrogated by this Court’s subsequent decision in <em>Hartman </em>v. <em>Moore, </em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U. S. 250</a></span>, which held that a plaintiff cannot state a claim of retaliatory prosecution in violation of the First Amendment if the charges were supported by probable cause. But the Court of Appeals determined that <em>Hartman’s </em>no-probable-cause requirement did not extend to claims of retaliatory arrest and therefore did not disturb its prior precedent in <em><span class="citation" data-id="553431"><a href="/opinion/553431/camille-deloach-v-mitzi-bevers/" aria-description="Citation for case: Camille Deloach v. Mitzi Bevers">DeLoach</a></span>. </em>Accordingly, the court concluded, “when Mr. Howards was arrested it was clearly established that an arrest made in retaliation of an individual’s First Amendment rights is unlawful, even if the arrest is supported by probable cause.” <span class="citation" data-id="9441235"><a href="/opinion/212271/howards-v-mclaughlin/#1148" aria-description="Citation for case: Howards v. McLaughlin">634 F. 3d, at 1148</a></span>.</p>
<p id="b746-7">We disagree. At the time of Howards’ arrest, <em>Hartman’s </em>impact on the Tenth Circuit’s precedent governing retaliatory arrests was far from clear. Although the facts of <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>involved only a retaliatory prosecution, reasonable officers could have questioned whether the rule of <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>also applied to arrests.</p>
<p id="b747-4"><page-number citation-index="1" label="667">*667</page-number><em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>was decided against a legal backdrop that treated retaliatory arrest and prosecution claims similarly. <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>resolved a split among the Courts of Appeals about the relevance of probable cause in retaliatory prosecution suits, but some of the conflicting Court of Appeals cases involved both an arrest and a prosecution that were alleged to be retaliation for the exercise of First Amendment rights. See <span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/#255" aria-description="Citation for case: Hartman v. Moore">547 U. S., at 255-256, 259</a></span>, n. 6 (citing <em>Mozzochi </em>v. <em>Borden, </em><span class="citation" data-id="580301"><a href="/opinion/580301/charles-mozzochi-v-richard-s-borden-jr-paul-j-gibbons-richard-s/" aria-description="Citation for case: Charles Mozzochi v. Richard S. Borden, Jr., Paul J....">959 F. 2d 1174</a></span> (CA2 1992); <em>Singer </em>v. <em>Fulton Cty. Sheriff, </em><span class="citation multiple-matches"><a href="/c/F.%203d/63/110/">63 F. 3d 110</a></span> (CA2 1995); <em>Keenan </em>v. <em>Tejeda, </em><span class="citation" data-id="27242"><a href="/opinion/27242/keenan-v-tejeda/" aria-description="Citation for case: Keenan v. Tejeda">290 F. 3d 252</a></span> (CA5 2002); <em>Wood </em>v. <em>Kesler, </em><span class="citation" data-id="76122"><a href="/opinion/76122/melvin-alan-wood-v-michael-kesler-individually-and-in-his-capacity-as-an/" aria-description="Citation for case: Melvin Alan Wood v. Michael Kesler, individually and in...">323 F. 3d 872</a></span> (CA11 2003)). Those cases made no distinction between claims of retaliatory arrest and claims of retaliatory prosecution when considering the relevance of probable cause. See <span class="citation" data-id="580301"><a href="/opinion/580301/charles-mozzochi-v-richard-s-borden-jr-paul-j-gibbons-richard-s/#1179" aria-description="Citation for case: Charles Mozzochi v. Richard S. Borden, Jr., Paul J...."><em>Mozzochi, supra, </em>at 1179-1180</a></span>; <em>Singer, supra, </em>at 120; <span class="citation" data-id="27242"><a href="/opinion/27242/keenan-v-tejeda/#260" aria-description="Citation for case: Keenan v. Tejeda"><em>Keenan, supra, </em>at 260</a></span>; <span class="citation" data-id="76122"><a href="/opinion/76122/melvin-alan-wood-v-michael-kesler-individually-and-in-his-capacity-as-an/#883" aria-description="Citation for case: Melvin Alan Wood v. Michael Kesler, individually and in..."><em>Wood, supra, </em>at 883</a></span>. Indeed, the close relationship between retaliatory arrest and prosecution claims is well demonstrated by the Tenth Circuit’s own decision in <em>DeLoach. DeLoach, </em>too, involved allegations of both retaliatory arrest and retaliatory prosecution, and the Tenth Circuit analyzed the two claims as one. <span class="citation" data-id="553431"><a href="/opinion/553431/camille-deloach-v-mitzi-bevers/#620" aria-description="Citation for case: Camille Deloach v. Mitzi Bevers">922 F. 2d, at 620-621</a></span>.</p>
<p id="b747-5">A reasonable official also could have interpreted <em>Hartman's </em>rationale to apply to retaliatory arrests. <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>first observed that, in retaliatory prosecution cases, evidence showing whether there was probable cause for the charges would always be “available and apt to prove or disprove retaliatory causation.” <span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/#261" aria-description="Citation for case: Hartman v. Moore">547 U. S., at 261</a></span>. In this Court’s view, the presence of probable cause, while not a “guarantee” that retaliatory motive did not cause the prosecution, still precluded any prima facie inference that retaliatory motive was the but-for cause of the plaintiff’s injury. <span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/#265" aria-description="Citation for case: Hartman v. Moore"><em>Id., </em>at 265</a></span>. This was especially true because, as <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>next emphasized, retaliatory prosecution claims involve particularly attenuated causation between the defendant’s alleged retaliatory animus and the plaintiff’s injury. <span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/#259" aria-description="Citation for case: Hartman v. Moore"><em>Id., </em>at 259-261</a></span>. In <page-number citation-index="1" label="668">*668</page-number>a retaliatory prosecution case, the key defendant is typically not the prosecutor who made the charging decision that injured the plaintiff, because prosecutors enjoy absolute immunity for their decisions to prosecute. Rather, the key defendant is the person who allegedly prompted the prosecutor’s decision. Thus, the intervening decision of the third-party prosecutor widens the causal gap between the defendant’s animus and the plaintiff’s injury. <span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/#261" aria-description="Citation for case: Hartman v. Moore"><em>Id., </em>at 261-263</a></span>.</p>
<p id="b748-5">Like retaliatory prosecution cases, evidence of the presence or absence of probable cause for the arrest will be available in virtually every retaliatory arrest case. Such evidence could be thought similarly fatal to a plaintiff’s claim that animus caused his arrest, given that retaliatory arrest cases also present a tenuous causal connection between the defendant’s alleged animus and the plaintiff’s injury. An officer might bear animus toward the content of a suspect’s speech. But the officer may decide to arrest the suspect because his speech provides evidence of a crime or suggests a potential threat. See, <em>e. g., Wayte </em>v. <em>United States, </em><span class="citation" data-id="9429952"><a href="/opinion/111375/wayte-v-united-states/#612" aria-description="Citation for case: Wayte v. United States">470 U. S. 598, 612-613</a></span> (1985) (noting that letters of protest writ- , ten to the Selective Service, in which the author expressed disagreement with the draft, “provided strong, perhaps conclusive evidence of the nonregistrant’s intent not to comply — one of the elements of the offense” of willful failure to register for the draft). Like retaliatory prosecution cases, then, the connection between alleged animus and injury may be weakened in the arrest context by a police officer’s wholly legitimate consideration of speech.</p>
<p id="b748-6">To be sure, we do not suggest that Hartman’s rule in fact extends to arrests. Nor do we suggest that every aspect of <em>Hartman’s </em>rationale could apply to retaliatory arrests. <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>concluded that the causal connection in retaliatory prosecution cases is attenuated because those cases necessarily involve the animus of one person and the injurious action of another, <span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/#262" aria-description="Citation for case: Hartman v. Moore">547 U. S., at 262</a></span>, but in many retaliatory arrest <page-number citation-index="1" label="669">*669</page-number>cases, it is the officer bearing the alleged animus who makes the injurious arrest. Moreover, <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>noted that, in retaliatory prosecution cases, the causal connection between the defendant’s animus and the prosecutor’s decision is further weakened by the, “presumption of regularity accorded to prosecutorial decisionmaking.” <span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/#263" aria-description="Citation for case: Hartman v. Moore"><em>Id., </em>at 263</a></span>. That presumption does hot apply here. Nonetheless, the fact remains that, for qualified immunity purposes, at the time of Howards’ arrest it was at least arguable that Hartman’s rule extended to retaliatory arrests.<footnotemark>6</footnotemark></p>
<p id="b749-5">Decisions from other Federal Courts of Appeals in the wake of <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>support this assessment. Shortly before Howards’ arrest, the Sixth Circuit held that <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>required a plaintiff alleging a retaliatory arrest to show that the defendant officer lacked probable cause. See <em>Barnes </em>v. <em>Wright, </em><span class="citation" data-id="794492"><a href="/opinion/794492/wilbur-barnes-v-tony-wright/#720" aria-description="Citation for case: Wilbur Barnes v. Tony Wright">449 F. 3d 709, 720</a></span> (2006) (reasoning that the <em>Hartman </em>“rule sweeps broadly”). That court’s treatment of <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>confirms that the inapplicability of <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>to arrests would not have been clear to a reasonable officer when Howards was arrested. Moreover, since Howards’ arrest, additional Courts of Appeals have concluded that <em>Hartman’s </em>no-probable-cause requirement extends to retaliatory arrests. See, <em>e. g., MeCabe </em>v. <em>Parker, </em><span class="citation" data-id="149785"><a href="/opinion/149785/mccabe-v-parker/#1075" aria-description="Citation for case: McCabe v. Parker">608 F. 3d 1068, 1075</a></span> (CA8 2010); <em>Phillips </em>v. <em>Irvin, </em><span class="citation" data-id="51745"><a href="/opinion/51745/william-joseph-phillips-v-officer-b-e-irvin/#929" aria-description="Citation for case: William Joseph Phillips v. Officer B. E. Irvin">222 Fed. Appx. 928, 929</a></span> (CA11 2007) <em>(per curiam). </em>As we have previously observed, “[i]f <page-number citation-index="1" label="670">*670</page-number>judges thus disagree on a constitutional question, it is unfair to subject police to money damages for picking the losing side of the controversy.” <em>Wilson </em>v. <em>Layne, </em><span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/#618" aria-description="Citation for case: Wilson v. Layne">526 U. S. 603, 618</a></span> (1999).<footnotemark>7</footnotemark></p>
<p id="b750-5">* * *</p>
<p id="b750-6"><em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>injected uncertainty into the law governing retaliatory arrests, particularly in light of <em>Hartman’s </em>rationale and the close relationship between retaliatory arrest and prosecution claims. This uncertainty was only confirmed by subsequent appellate decisions that disagreed over whether the reasoning in <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>applied similarly to retaliatory arrests. Accordingly, when Howards was arrested it was not clearly established that an arrest supported by probable cause could give rise to a First Amendment violation. Petitioners Reichle and Doyle are thus entitled to qualified immunity.</p>
<p id="b750-7">The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b750-8">
<em>It is so ordered.</em>
</p>
<p id="b750-9">Justice Kagan took no part in the consideration or decision of this case.</p>
<footnote label="1">
<p id="b741-8"> The parties dispute the manner of the touch. Howards described it as an openhanded pat, while several Secret Service agents described it as a forceful push. This dispute does not affect our analysis.</p>
</footnote>
<footnote label="2">
<p id="AiOP"> Howards named several Secret Service agents as defendants, but only Agents Reichle and Doyle are petitioners here. We address only those parts of the lower courts’ decisions that involve petitioners Reichle and Doyle.</p>
</footnote>
<footnote label="3">
<p id="AVzb"> Howards does not challenge the Court of Appeals’ probable-cause determination.</p>
</footnote>
<footnote label="4">
<p id="b743-7"> This Court has recognized an implied cause of action for damages against federal officials for Fourth Amendment violations. See <em>Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971). We have never held that <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span> </em>extends to First Amendment claims. See <em>Ashcroft </em>v. <em>Iqbal, </em><span class="citation" data-id="9435339"><a href="/opinion/145875/ashcroft-v-iqbal/#675" aria-description="Citation for case: Ashcroft v. Iqbal">556 U. S. 662, 675</a></span> (2009) (assuming without deciding that a <page-number citation-index="1" label="664">*664</page-number>First Amendment free exercise claim is actionable under Bivens); <em>Bush v. Lucas, </em><span class="citation" data-id="9429240"><a href="/opinion/110965/bush-v-lucas/#368" aria-description="Citation for case: Bush v. Lucas">462 U. S. 367, 368</a></span> (1983) (refusing to extend <em>Bivens </em>to a First Amendment speech claim involving federal employment). We need not (and do not) decide here whether <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span> </em>extends to First Amendment retaliatory arrest claims.</p>
</footnote>
<footnote label="5">
<p id="b745-9"> The Court of Appeals’ reliance on <em>Whren </em>v. <em>United States, </em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U. S. 806</a></span> (1996), was misplaced. There, we held that a traffic stop supported by probable cause did not violate the Fourth Amendment regardless of the officer’s actual motivations, but we explained that the Equal Protection Clause would prohibit an officer from selectively enforcing the traffic laws based on race. <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#813" aria-description="Citation for case: Whren v. United States"><em>Id., </em>at 813</a></span>. Citing <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span>, </em>the Court of Appeals noted that “[i]t is well established that an act which is lawful under the Fourth Amendment may still violate other provisions of the Constitution.” <em>Howards </em>v. <em>McLaughlin, </em><span class="citation" data-id="9441235"><a href="/opinion/212271/howards-v-mclaughlin/#1149" aria-description="Citation for case: Howards v. McLaughlin">634 F. 3d 1131, 1149, n. 15</a></span> (CA10 2011). But, again, we do not define clearly established law at such a “high level of generality.” <em>Ashcroft </em>v. <em>al-Kidd, </em><span class="citation" data-id="7262676"><a href="/opinion/7344719/ashcroft-v-al-kidd/#742" aria-description="Citation for case: Ashcroft v. al-Kidd">563 U. S. 731, 742</a></span> (2011). Whren’s discussion of the Fourteenth Amendment does not indicate, much less “clearly establish,” that an arrest supported by probable cause could none-, theless violate the First Amendment.</p>
</footnote>
<footnote label="6">
<p id="b749-6"> Howards argues that petitioners violated his clearly established First Amendment right even if <em>Hartman’s </em>rule applies equally to retaliatory arrests. According to Howards, <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>did not hold that a prosecution violates the First Amendment only when it is unsupported by probable cause. Rather, Howards argues, <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>made probable cause relevant only to a plaintiff’s ability to recover damages for a First Amendment violation. See Brief for Respondent 37-41. We need not resolve whether <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>is best read as defining the scope of the First Amendment right or as simply establishing a prerequisite for recovery. Nor need we decide whether that distinction matters. It suffices, for qualified immunity purposes, that the answer would not have been clear to a reasonable official when Howards was arrested.</p>
</footnote>
<footnote label="7">
<p id="b750-12"> Indeed, the Tenth Circuit itself has applied <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span> </em>outside the context of retaliatory prosecution. See <em>McBeth </em>v. <em>Himes, </em><span class="citation" data-id="811048"><a href="/opinion/811048/united-states-v-daniel-miller/#719" aria-description="Citation for case: United States v. Daniel Miller">698 F. 3d 708, 719</a></span> (2010) (requiring the absence of probable cause in the context of a claim alleging that government officials suspended a business license in retaliation for the exercise of First Amendment rights).</p>
</footnote>
</opinion>
```

---
