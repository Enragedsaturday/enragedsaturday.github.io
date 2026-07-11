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

## GROUP: _overhaul2/lake/cases/kastigar-v-united-states--108541.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6611f86a4e2e16b4", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "kastigar-v-united-states--108541"}, "payload": {"all": [{"cite": "406 U.S. 441", "page": "441", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "406"}, {"cite": "92 S. Ct. 1653", "page": "1653", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "92"}, {"cite": "32 L. Ed. 2d 212", "page": "212", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "32"}, {"cite": "1972 U.S. LEXIS 57", "page": "57", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1972"}], "display": null, "official": null, "official_selection_present": false, "record_id": "kastigar-v-united-states--108541"}}
{"assertion_id": "05d8cf7d83921762", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "kastigar-v-united-states--108541"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "kastigar-v-united-states--108541", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — kastigar-v-united-states--108541

```json
{
  "schema_version": "s2.v1",
  "record_id": "kastigar-v-united-states--108541",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Kastigar v. United States",
    "case_name_short": "Kastigar",
    "case_name_full": "KASTIGAR Et Al. v. UNITED STATES",
    "input_case_name": "Kastigar v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1972-06-26",
    "year": 1972,
    "docket": null,
    "cluster_id": 108541,
    "lead_opinion_id": 9424889,
    "sibling_ids": [],
    "absolute_url": "/opinion/108541/kastigar-v-united-states/",
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
        "cite": "406 U.S. 441",
        "volume": "406",
        "reporter": "U.S.",
        "page": "441",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 S. Ct. 1653",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "1653",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "32 L. Ed. 2d 212",
        "volume": "32",
        "reporter": "L. Ed. 2d",
        "page": "212",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1972 U.S. LEXIS 57",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "57",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "406 U.S. 441",
        "volume": "406",
        "reporter": "U.S.",
        "page": "441",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 S. Ct. 1653",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "1653",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "32 L. Ed. 2d 212",
        "volume": "32",
        "reporter": "L. Ed. 2d",
        "page": "212",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1972 U.S. LEXIS 57",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "57",
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
    "date_created": "2026-07-06T13:48:11Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:48:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:48:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:48:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:48:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — kastigar-v-united-states--108541

```
<opinion type="majority">
<author id="b506-4"><page-number citation-index="1" label="442">*442</page-number>Mr. Justice Powell delivered the opinion of the Court.</author>
<p id="b506-5">This case presents the question whether the United States Government may compel testimony from an unwilling witness, who invokes the Fifth Amendment privilege against compulsory self-incrimination, by conferring on the witness immunity from use of the compelled testimony in subsequent criminal proceedings, as well as immunity from use of evidence derived from the testimony.</p>
<p id="b506-6">Petitioners were subpoenaed to appear before a United States grand jury in the Central District of California on February 4, 1971. The Government believed that petitioners were likely to assert their Fifth Amendment privilege. Prior to the scheduled appearances, the Government applied to the District Court for an order directing petitioners to answer questions and produce evidence before the grand jury under a grant of immunity conferred pursuant to <span class="citation no-link">18 U. S. C. §§ 6002-6003</span>. Petitioners opposed issuance of the order, contending primarily that the scope of the immunity provided by the statute was not coextensive with the scope of the privilege against self-incrimination, and therefore was not sufficient to supplant the privilege and compel their testimony. The District Court rejected this contention, and ordered petitioners to appear before the grand jury and answer its questions under the grant of immunity.</p>
<p id="b506-7">Petitioners appeared but refused to answer questions, asserting their privilege against compulsory self-incrimination. They were brought before the District Court, and each persisted in his refusal to answer the grand jury’s questions, notwithstanding the grant of immunity. The court found both in contempt, and committed them to the custody of the Attorney General until either they answered the grand jury’s questions or the term of the grand jury expired.<footnotemark>1</footnotemark> The Court of <page-number citation-index="1" label="443">*443</page-number>Appeals for the Ninth Circuit affirmed. <em>Stewart </em>v. <em>United States, </em><span class="citation" data-id="295861"><a href="/opinion/295861/michael-gorean-stewart-v-united-states-of-america-charles-joseph-kastigar/" aria-description="Citation for case: Michael Gorean Stewart v. United States of America,...">440 F. 2d 954</a></span> (CA9 1971). This Court granted certiorari to resolve the important question whether testimony may be compelled by granting immunity from the use of compelled testimony and evidence derived therefrom (“use and derivative use” immunity), or whether it is necessary to grant immunity from prosecution for offenses to which compelled testimony relates (“transactional” immunity). <span class="citation multiple-matches"><a href="/c/U.%20S./402/971/">402 U. S. 971</a></span> (1971).</p>
<p id="b507-5">I</p>
<p id="b507-6">The power of government to compel persons to testify in court or before grand juries and other governmental agencies is firmly established in Anglo-American jurisprudence.<footnotemark>2</footnotemark> The power with respect to courts was established by statute in England as early as 1562,<footnotemark>3</footnotemark> and Lord Bacon observed in 1612 that all subjects owed the King their “knowledge and discovery.” <footnotemark>4</footnotemark> While it is not clear when grand juries first resorted to compulsory process to secure, the attendance and testimony of witnesses, the general common-law principle that “the public has a right to every man’s evidence” was considered an “indubitable certainty” that “cannot be denied” by 1742.<footnotemark>5</footnotemark> The power to compel testimony, and the corresponding duty to testify, are recognized in the Sixth Amend<page-number citation-index="1" label="444">*444</page-number>ment requirements that an accused be confronted with the witnesses against him, and have compulsory process for obtaining witnesses in his favor. The first Congress recognized the testimonial duty in the Judiciary Act of 1789, which provided for compulsory attendance of witnesses in the federal courts.<footnotemark>6</footnotemark> Mr. Justice White noted the importance of this essential power of government in his concurring opinion in <em>Murphy </em>v. <em>Waterfront Comm’n, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#93" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 93-94</a></span> (1964):</p>
<blockquote id="b508-5">“Among the necessary and most important of the powers of the States as well as the Federal Government to assure the effective functioning of government in an ordered society is the broad power to compel residents to testify in court or before grand juries or agencies. See <em>Blair </em>v. <em>United States, </em><span class="citation" data-id="99422"><a href="/opinion/99422/blair-v-united-states/" aria-description="Citation for case: Blair v. United States">250 U. S. 273</a></span>. Such testimony constitutes one of the Government’s primary sources of information.”</blockquote>
<p id="b508-6">But the power to compel testimony is not absolute. There are a number of exemptions from the testimonial duty,<footnotemark>7</footnotemark> the most important of which is the Fifth Amendment privilege against compulsory self-incrimination. The privilege reflects a complex of our fundamental values and aspirations,<footnotemark>8</footnotemark> and marks an important advance in the development of our liberty.<footnotemark>9</footnotemark> It can be asserted in any proceeding, civil or criminal, administrative or judicial, investigatory or adjudicatory;<footnotemark>10</footnotemark> and it <page-number citation-index="1" label="445">*445</page-number>protects against any disclosures that the witness reasonably believes could be used in a criminal prosecution or could lead to other evidence that might be so used.<footnotemark>11</footnotemark> This Court has been zealous to safeguard the values that underlie the privilege.<footnotemark>12</footnotemark></p>
<p id="b509-5">Immunity statutes, which have historical roots deep in Anglo-American jurisprudence,<footnotemark>13</footnotemark> are not incompatible <page-number citation-index="1" label="446">*446</page-number>with these values. Rather, they seek a rational accommodation between the imperatives of the privilege and the legitimate demands of government to compel citizens to testify. The existence of these statutes reflects the importance of testimony, and the fact that many offenses are of such a character that the only persons capable of giving useful testimony are those implicated in the crime. Indeed, their origins were in the context of such offenses,<footnotemark>14</footnotemark> <page-number citation-index="1" label="447">*447</page-number>and their primary use has been to investigate such offenses.<footnotemark>15</footnotemark> Congress included immunity statutes in many of the regulatory measures adopted in the first half of this century.<footnotemark>10</footnotemark> Indeed, prior to the enactment of the statute under consideration in this case, there were in force over 50 federal immunity statutes.<footnotemark>17</footnotemark> In addition, every State in the Union, as well as the District of Columbia and Puerto Rico, has one or more such statutes.<footnotemark>18</footnotemark> The commentators,<footnotemark>19</footnotemark> and this Court on several occasions,<footnotemark>20</footnotemark> have characterized immunity statutes as essential to the effective enforcement of various criminal statutes. As Mr. Justice Frankfurter observed, speaking for the Court in <em>Ullmann </em>v. <em>United States, </em><span class="citation" data-id="9421245"><a href="/opinion/105363/ullmann-v-united-states/" aria-description="Citation for case: Ullmann v. United States">350 U. S. 422</a></span> (1956), such statutes have “become part of our constitutional fabric.” <footnotemark>21</footnotemark> <span class="citation" data-id="9421245"><a href="/opinion/105363/ullmann-v-united-states/#438" aria-description="Citation for case: Ullmann v. United States"><em>Id., </em>at 438</a></span>.</p>
<p id="b512-4"><page-number citation-index="1" label="448">*448</page-number>II</p>
<p id="b512-5">Petitioners contend, first, that the Fifth Amendment's privilege against compulsory self-incrimination, which is that “[n]o person . . . shall be compelled in any criminal case to be a witness against himself," deprives Congress of power to enact laws that compel self-incrimination, even if complete immunity from prosecution is granted prior to the compulsion of the incriminatory testimony. In other words, petitioners assert that no immunity statute, however drawn, can afford a lawful basis for compelling incriminatory testimony. They ask us to reconsider and overrule <em>Brown </em>v. <em>Walker, </em><span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/" aria-description="Citation for case: Brown v. Walker">161 U. S. 591</a></span> (1896), and <em>Ullmann </em>v. <em>United States, supra, </em>decisions that uphold the constitutionality of immunity statutes.<footnotemark>22</footnotemark> We find no merit to this contention and reaffirm the decisions in <em><span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/" aria-description="Citation for case: Brown v. Walker">Brown</a></span> </em>and <em><span class="citation" data-id="9421245"><a href="/opinion/105363/ullmann-v-united-states/" aria-description="Citation for case: Ullmann v. United States">Ullmann</a></span>.</em></p>
<p id="b512-6">III</p>
<p id="b512-7">Petitioners' second contention is that the scope of immunity provided by the federal witness immunity statute, <span class="citation no-link">18 U. S. C. § 6002</span>, is not coextensive with the scope of the Fifth Amendment privilege against compulsory self-incrimination, and therefore is not sufficient to supplant the privilege and compel testimony over a claim of the privilege. The statute provides that when a witness is compelled by district court order to testify over a claim of the privilege:</p>
<blockquote id="b512-8">“the witness may not refuse to comply with the order on the basis of his privilege against self-incrimination; but no testimony or other information compelled under the order (or any information <page-number citation-index="1" label="449">*449</page-number>directly or indirectly derived from such testimony or other information) may be used against the witness in any criminal case, except a prosecution for perjury, giving a false statement, or otherwise failing to comply with the order.” <footnotemark><em>23</em></footnotemark><em> </em><span class="citation no-link">18 U. S. C. § 6002</span>.</blockquote>
<p id="b513-5">The constitutional inquiry, rooted in logic and history, as well as in the decisions of this Court, is whether the immunity granted under this statute is coextensive with the scope of the privilege.<footnotemark>24</footnotemark> If so, petitioners’ refusals to answer based on the privilege were unjustified, and the judgments of contempt were proper, for the grant of immunity has removed the dangers against which the privilege protects. <em>Brown </em>v. <em><span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/" aria-description="Citation for case: Brown v. Walker">Walker, supra.</a></span> </em>If, on the other hand, the immunity granted is not as comprehensive as the protection afforded by the privilege, petitioners were justified in refusing to answer, and the judgments of contempt must be vacated. <em>McCarthy </em>v. <em>Arndstein, </em><span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/#42" aria-description="Citation for case: McCarthy v. Arndstein">266 U. S. 34, 42</a></span> (1924).</p>
<p id="b513-6">Petitioners draw a distinction between statutes that provide transactional immunity and those that provide, as does the statute before us, immunity from use and derivative use.<footnotemark>25</footnotemark> They contend that a statute must at a minimum grant full transactional immunity in order to be coextensive with the scope of the privilege. In support of this contention, they rely on <em>Counselman </em>v. Hitchcock, <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547</a></span> (1892), the first case in which this Court considered a constitutional challenge to an immunity statute. The statute, a re-enactment of the Immunity Act of 1868,<footnotemark>26</footnotemark> provided that no “evidence obtained from a party or witness by means of a judicial <page-number citation-index="1" label="450">*450</page-number>proceeding . . . shall be given in evidence, or in any manner used against him ... in any court of the United States . . . .”<footnotemark>27</footnotemark> Notwithstanding a grant of immunity and order to testify under the revised 1868 Act, the witness, asserting his privilege against compulsory self-incrimination, refused to testify before a federal grand jury. He was consequently adjudged in contempt of court.<footnotemark>28</footnotemark> On appeal, this Court construed the statute as affording a witness protection only against the use of the specific testimony compelled from him under the grant of immunity. This construction meant that the statute “could not, and would not, prevent the use of his testimony to search out other testimony to be used in evidence against him.” <footnotemark>29</footnotemark> Since the revised 1868 Act, as construed by the Court, would permit the use against the immunized witness of evidence derived from his compelled testimony, it did not protect the witness to the same extent that a claim of the privilege would protect him. Accordingly, under the principle that a grant of immunity cannot supplant the privilege, and is not sufficient to compel testimony over a claim of the privilege, unless the scope of the grant of immunity is coextensive with the scope of the privilege,<footnotemark>30</footnotemark> the witness’ refusal to testify was held proper. In the course of its opinion, the Court made the following statement, on which petitioners heavily rely:</p>
<blockquote id="b514-5">“We are clearly of opinion that no statute which leaves the party or witness subject to prosecution <page-number citation-index="1" label="451">*451</page-number>after he answers the criminating question put to him, can have the effect of supplanting the privilege conferred by the Constitution of the United States. [The immunity statute under consideration] does not supply a complete protection from all the perils against which the constitutional prohibition was designed to guard, and is not a full substitute for that prohibition. In view of the constitutional provision, a statutory enactment, to be valid, must afford absolute immunity against future prosecution for the offence to which the question relates.” <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#585" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S., at 585-586</a></span>.</blockquote>
<p id="b515-5">Sixteen days after the <em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/" aria-description="Citation for case: Counselman v. Hitchcock">Counselman</a></span> </em>decision, a new immunity bill was introduced by Senator Cullom,<footnotemark>31</footnotemark> who urged that enforcement of the Interstate Commerce Act would be impossible in the absence of an effective immunity statute.<footnotemark>32</footnotemark> The bill, which became the Compulsory Testimony Act of 1893,<footnotemark>33</footnotemark> was drafted specifically to meet the broad language in <em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/" aria-description="Citation for case: Counselman v. Hitchcock">Counselman</a></span> </em>set forth above.<footnotemark>34</footnotemark> The new Act removed the privilege against self-incrimination in hearings before the Interstate Commerce Commission and provided that:</p>
<blockquote id="b515-6">“no person shall be prosecuted or subjected to any penalty or forfeiture for or on account of any transaction, matter or thing, concerning which he may testify, or produce evidence, documentary or otherwise -” Act of Feb. 11, 1893, <span class="citation no-link">27 Stat. 444</span>.</blockquote>
<p id="b516-4"><page-number citation-index="1" label="452">*452</page-number>This transactional immunity statute became the basic form for the numerous federal immunity statutes<footnotemark>35</footnotemark> until 1970, when, after re-examining applicable constitutional principles and the adequacy of existing law, Congress enacted the statute here under consideration.<footnotemark>36</footnotemark> The new statute, which does not “afford [the] absolute immunity against future prosecution” referred to in <em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/" aria-description="Citation for case: Counselman v. Hitchcock">Counselman</a></span>, </em>was drafted to meet what Congress judged to be the conceptual basis of <em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/" aria-description="Citation for case: Counselman v. Hitchcock">Counselman</a></span>, </em>as elaborated in subsequent decisions of the Court, namely, that immunity from the <page-number citation-index="1" label="453">*453</page-number>use of compelled testimony and evidence derived therefrom is coextensive with the scope of the privilege.<footnotemark>37</footnotemark></p>
<p id="b517-5">The statute’s explicit proscription of the use in any criminal case of “testimony or other information compelled under the order (or any information directly or indirectly derived from such testimony or other information)” is consonant with Fifth Amendment standards. We hold that such immunity from use and derivative use is coextensive with the scope of the privilege against self-incrimination, and therefore is sufficient to compel testimony over a claim of the privilege. While a grant of immunity must afford protection commensurate with that afforded by the privilege, it need not be broader. Transactional immunity, which accords full immunity from prosecution for the offense to which the compelled testimony relates, affords the witness considerably broader protection than does the Fifth Amendment privilege. The privilege has never been construed to mean that one who invokes it cannot subsequently be prosecuted. Its sole concern is to afford protection against being “forced to give testimony leading to the infliction of 'penalties affixed to . . . criminal acts.’ ”<footnotemark>38</footnotemark> Immunity from the use of compelled testimony, as well as evidence derived directly and indirectly therefrom, affords this protection. It prohibits the prosecutorial authorities from using the compelled testimony in <em>any </em>respect, and it therefore insures that the testimony cannot lead to the infliction of criminal penalties on the witness.</p>
<p id="b517-6">Our holding is consistent with the conceptual basis of <em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/" aria-description="Citation for case: Counselman v. Hitchcock">Counselman</a></span>. </em>The <em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/" aria-description="Citation for case: Counselman v. Hitchcock">Counselman</a></span> </em>statute, as construed by the Court, was plainly deficient in its 'failure to <page-number citation-index="1" label="454">*454</page-number>prohibit the use against the immunized witness of evidence derived from his compelled testimony. The Court repeatedly emphasized this deficiency, noting that the statute:</p>
<blockquote id="b518-5">“could not, and would not, prevent the use of his testimony to search out other testimony to be used in evidence against him or his property, in a criminal proceeding . . <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#564" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S., at 564</a></span>;</blockquote>
<p id="b518-6">that it:</p>
<blockquote id="b518-7">“could not prevent the obtaining and the use of witnesses and evidence which should be attributable directly to the testimony he might give under compulsion, and on which he might be convicted, when otherwise, and if he had refused to answer, he could not possibly have been convicted,” <em>ibid.;</em></blockquote>
<p id="b518-8">and that it:</p>
<blockquote id="b518-9">“affords no protection against that use of compelled testimony which consists in gaining therefrom a knowledge of the details of a crime, and of sources of information which may supply other means of convicting the witness or party.” <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#586" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S., at 586</a></span>.</blockquote>
<p id="b518-10">The basis of the Court's decision was recognized in <em>Ullmann </em>v. <em>United States, </em><span class="citation" data-id="9421245"><a href="/opinion/105363/ullmann-v-united-states/" aria-description="Citation for case: Ullmann v. United States">350 U. S. 422</a></span> (1956), in which the Court reiterated that the <em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/" aria-description="Citation for case: Counselman v. Hitchcock">Counselman</a></span> </em>statute was insufficient:</p>
<blockquote id="b518-11">“because the immunity granted was incomplete, in that it merely forbade the use of the testimony given and failed to protect a witness from future prosecution <em>based on knowledge and sources of information obtained from the compelled testimony Id., </em>at 437. (Emphasis supplied.)</blockquote>
<p id="b518-12">See also <em>Arndstein </em>v. <em>McCarthy, </em><span class="citation" data-id="8144042"><a href="/opinion/8182123/arndstein-v-mccarthy/#73" aria-description="Citation for case: Arndstein v. McCarthy">254 U. S. 71, 73</a></span> (1920). The broad language in <em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/" aria-description="Citation for case: Counselman v. Hitchcock">Counselman</a></span> </em>relied upon by peti<page-number citation-index="1" label="455">*455</page-number>tioners was unnecessary to the Court’s decision, and cannot be considered binding authority.<footnotemark>39</footnotemark></p>
<p id="b519-5">In <em>Murphy </em>v. <em>Waterfront Comm’n, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52</a></span> (1964), the Court carefully considered immunity from use of compelled testimony and evidence derived therefrom. The <em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">Murphy</a></span> </em>petitioners were subpoenaed to testify at a hearing conducted by the Waterfront Commission of New York Harbor. After refusing to answer certain questions on the ground that the answers might tend to incriminate them, petitioners were granted im<page-number citation-index="1" label="456">*456</page-number>munity from prosecution under the laws of New Jersey and New York.<footnotemark>40</footnotemark> They continued to refuse to testify, however, on the ground that their answers might tend to incriminate them under federal law, to which the immunity did not purport to extend. They were adjudged in civil contempt, and that judgment was affirmed by the New Jersey Supreme Court.<footnotemark>41</footnotemark></p>
<p id="b520-5">The issue before the Court in <em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">Murphy</a></span> </em>was whether New Jersey and New York could compel the witnesses, whom these States had immunized from prosecution under their laws, to give testimony that might then be used to convict them of a federal crime. Since New Jersey and New York had not purported to confer immunity from federal prosecution, the Court was faced with the question what limitations the Fifth Amendment privilege imposed on the prosecutorial powers of the Federal Government, a nonimmunizing sovereign. After undertaking an examination of the policies and purposes of the privilege, the Court overturned the rule that one jurisdiction within our federal structure may compel a witness to give testimony which could be used to convict him of a crime in another jurisdiction.<footnotemark>42</footnotemark> The Court held that the privilege protects state witnesses against incrimination under federal as well as state law, and federal witnesses against incrim<page-number citation-index="1" label="457">*457</page-number>ination under state as well as federal law. Applying this principle to the state immunity legislation before it, the Court held the constitutional rule to be that:</p>
<blockquote id="AHD">“[A] state witness may not be compelled to give testimony which may be incriminating under federal law unless the compelled testimony and its fruits cannot be used in any manner by federal officials in connection with a criminal prosecution against him. We conclude, moreover, that in order to implement this constitutional rule and accommodate the interests of the State and Federal Governments in investigating and prosecuting crime, the Federal Government must be prohibited from making any such use of compelled testimony and its fruits.” <footnotemark>43</footnotemark> <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#79" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S., at 79</a></span>.</blockquote>
<p id="b521-5">The Court emphasized that this rule left the state witness and the Federal Government, against which the witness had immunity only from the <em>me </em>of the compelled testimony and evidence derived therefrom, “in substantially the same position as if the witness had claimed his privilege in the absence of a state grant of immunity.” <em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">Ibid.</a></span></em></p>
<p id="b521-6">It is true that in <em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">Murphy</a></span> </em>the Court was not presented with the precise question presented by this case, whether a jurisdiction seeking to compel testimony may do so by granting only use and derivative-use immunity, for New Jersey and New York had granted petitioners transactional immunity. The Court heretofore has not <page-number citation-index="1" label="458">*458</page-number>squarely confronted this question,<footnotemark>44</footnotemark> because <em>post-Coun-selman </em>immunity statutes reaching the Court either have followed the pattern of the 1893 Act in providing transactional immunity,<footnotemark>45</footnotemark> or have been found deficient for failure to prohibit the use of all evidence derived from compelled testimony.<footnotemark>46</footnotemark> But both the reasoning of the Court in <em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">Murphy</a></span> </em>and the result reached compel the conclusion that use and derivative-use immunity is constitutionally sufficient to compel testimony over a claim of the privilege. Since the privilege is fully applicable and its scope is the same whether invoked in a state or in a federal jurisdiction,<footnotemark>47</footnotemark> the <em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">Murphy</a></span> </em>conclusion that a prohibition on use and derivative use secures a witness’ Fifth Amendment privilege against infringement by the Federal Government demonstrates that immunity from use and derivative use is coextensive with the scope of the privilege. As the <em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">Murphy</a></span> </em>Court noted, immunity from use and derivative use “leaves the witness and the Federal Government in substantially the same position <page-number citation-index="1" label="459">*459</page-number>as if the witness had claimed his privilege”<footnotemark>48</footnotemark> in the absence of a grant of immunity. The <em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">Murphy</a></span> </em>Court was concerned solely with the danger of incrimination under federal law, and held that immunity from use and derivative use was sufficient to displace the danger. This protection coextensive with the privilege is the degree of protection that the Constitution requires, and is all that the Constitution requires even against the jurisdiction compelling testimony by granting immunity.<footnotemark>49</footnotemark></p>
<p id="b523-5">IV</p>
<p id="b523-6">Although an analysis of prior decisions and the purpose of the Fifth Amendment privilege indicates that use and derivative-use immunity is coextensive with the privilege, we must consider additional arguments advanced by petitioners against the sufficiency of such immunity. We start from the premise, repeatedly affirmed by this Court, that an appropriately broad immunity grant is compatible with the Constitution.</p>
<p id="b523-7">Petitioners argue that use and derivative-use immunity will not adequately protect a witness from various possible incriminating uses of the compelled testimony: for example, the prosecutor or other law enforcement officials may obtain leads, names of witnesses, or other information not otherwise available that might result in a prosecution. It will be difficult and perhaps impossible, the argument goes, to identify, by testimony or cross-examination, the subtle ways in which the compelled testimony may disadvantage a witness, especially in the jurisdiction granting the immunity.</p>
<p id="b523-8">This argument presupposes that the statute’s pro<page-number citation-index="1" label="460">*460</page-number>hibition will prove impossible to enforce. The statute provides a sweeping proscription of any use, direct or indirect, of the compelled testimony and any information derived therefrom:</p>
<blockquote id="b524-5">“[N]o testimony or other information compelled under the order (or any information directly or indirectly derived from such testimony or other information) may be used against the witness in any criminal case <em>. . . </em><span class="citation no-link">18 U. S. C. § 6002</span>.</blockquote>
<p id="b524-6">This total prohibition on use provides a comprehensive safeguard, barring the use of compelled testimony as an “investigatory lead,” <footnotemark>50</footnotemark> and also barring the use of any evidence obtained by focusing investigation on a witness as a result of his compelled disclosures.</p>
<p id="b524-7">A person accorded this immunity under <span class="citation no-link">18 U. S. C. § 6002</span>, and subsequently prosecuted, is not dependent for the preservation of his rights upon the integrity and good faith of the prosecuting authorities. As stated in <em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">Murphy</a></span>:</em></p>
<blockquote id="b524-8">“Once a defendant demonstrates that he has testified, under a state grant of immunity, to matters related to the federal prosecution, the federal authorities have the burden of showing that their evidence is not tainted by establishing that they had an independent, legitimate source for the disputed evidence.” <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S., at 79</a></span> n. 18.</blockquote>
<p id="b524-9">This burden of proof, which we reaffirm as appropriate, is not limited to a negation of taint; rather, it imposes on the prosecution the affirmative duty to prove that the evidence it proposes to use is derived from a legitimate source wholly independent of the compelled testimony.</p>
<p id="b525-4"><page-number citation-index="1" label="461">*461</page-number>This is very substantial protection,<footnotemark>51</footnotemark> commensurate with that resulting from invoking the privilege itself. The privilege assures that a citizen is not compelled to incriminate himself by his own testimony. It usually operates to allow a citizen to remain silent when asked a question requiring an incriminatory answer. This statute, which operates after a witness has given incriminatory testimony, affords the same protection by assuring that the compelled testimony can in no way lead to the infliction of criminal penalties. The statute, like the Fifth Amendment, grants neither pardon nor amnesty. Both the statute and the Fifth Amendment allow the government to prosecute using evidence from legitimate independent sources.</p>
<p id="b525-5">The statutory proscription is analogous to the Fifth Amendment requirement in cases of coerced confessions.<footnotemark>52</footnotemark> A coerced confession, as revealing of leads as testimony given in exchange for immunity,<footnotemark>53</footnotemark> is inadmissible in a criminal trial, but it does not bar prosecution.<footnotemark>54</footnotemark> Moreover, a defendant against whom incriminating evidence has been obtained through a grant of immunity may be in a stronger position at trial than a defendant who asserts a Fifth Amendment coerced-confession claim. One raising a claim under this statute need only show that he testified under a grant of immunity in order to shift to the government the heavy burden of proving that all of the evidence it proposes to use was derived from <page-number citation-index="1" label="462">*462</page-number>legitimate independent sources.<footnotemark>55</footnotemark> On the other hand, a defendant raising a eoerced-confession claim under the Fifth Amendment must first prevail in a voluntariness hearing before his confession and evidence derived from it become inadmissible.<footnotemark>56</footnotemark></p>
<p id="b526-5">There can be no justification in reason or policy for holding that the Constitution requires an amnesty grant where, acting pursuant to statute and accompanying safeguards, testimony is compelled in exchange for immunity from use and derivative use when no such amnesty is required where the government, acting without colorable right, coerces a defendant into incriminating himself.</p>
<p id="b526-6">We conclude that the immunity provided by <span class="citation no-link">18 U. S. C. § 6002</span> leaves the witness and the prosecutorial authorities in substantially the same position as if the witness had claimed the Fifth Amendment privilege. The immunity therefore is coextensive with the privilege and suffices to supplant it. The judgment of the Court of Appeals for the Ninth Circuit accordingly is</p>
<p id="b526-7">
<em>Affirmed.</em>
</p>
<p id="b526-8">Mr. Justice Brennan and Mr. Justice Rehnquist took no part in the consideration or decision of this case.</p>
<footnote label="1">
<p id="b506-8"> The contempt order was issued pursuant to <span class="citation no-link">28 U. S. C. § 1826</span>.</p>
</footnote>
<footnote label="2">
<p id="b507-7"> For a concise history of testimonial compulsion prior to the adoption of our Constitution, see 8 J. Wigmore, Evidence § 2190 (J. McNaughton rev. 1961). See <em>Ullmann </em>v. <em>United States, </em><span class="citation" data-id="9421245"><a href="/opinion/105363/ullmann-v-united-states/" aria-description="Citation for case: Ullmann v. United States">350 U. S. 422</a></span>, 439 n. 15 (1956); <em>Blair </em>v. <em>United States, </em><span class="citation" data-id="99422"><a href="/opinion/99422/blair-v-united-states/" aria-description="Citation for case: Blair v. United States">250 U. S. 273</a></span> (1919).</p>
</footnote>
<footnote label="3">
<p id="b507-8"> Statute of Elizabeth, 5 Eliz. 1, c. 9, § 12 (1562).</p>
</footnote>
<footnote label="4">
<p id="b507-9"> <em>Countess of Shrewsbury’s Case, </em>2 How. St. Tr. 769, 778 (1612).</p>
</footnote>
<footnote label="5">
<p id="b507-10"> See the parliamentary debate on the Bill to Indemnify Evidence, particularly the remarks of the Duke of Argyle and Lord Chancellor Hardwicke, reported in 12 T. Hansard, Parliamentary History of England 675, 693 (1812). See also <em>Piemonte </em>v. <em>United States, </em><span class="citation" data-id="9422272"><a href="/opinion/106283/piemonte-v-united-states/" aria-description="Citation for case: Piemonte v. United States">367 U. S. 556</a></span>, 559 n. 2 (1961); <em>Ullmann </em>v. <em>United States, supra, </em>at 439 n. 15; <em>Brown </em>v. <em>Walker, </em><span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#600" aria-description="Citation for case: Brown v. Walker">161 U. S. 591, 600</a></span> (1896).</p>
</footnote>
<footnote label="6">
<p id="b508-7"> <span class="citation no-link">1 Stat. 73</span>, 88-89.</p>
</footnote>
<footnote label="7">
<p id="b508-8"> See <em>Blair </em>v. <em>United States, supra, </em>at 281; 8 Wigmore, <em>supra, </em>n. 2, §§ 2192, 2197.</p>
</footnote>
<footnote label="8">
<p id="b508-9"> See <em>Murphy </em>v. <em>Waterfront Comm’n, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#55" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 55</a></span> (1964).</p>
</footnote>
<footnote label="9">
<p id="b508-10"> See <em>Ullmann </em>v. <em>United States, </em><span class="citation" data-id="9421245"><a href="/opinion/105363/ullmann-v-united-states/#426" aria-description="Citation for case: Ullmann v. United States">350 U. S., at 426</a></span>; E. Griswold, The Fifth Amendment Today 7 (1955).</p>
</footnote>
<footnote label="10">
<p id="b508-11"> <em>Murphy </em>v. <em>Waterfront Comm’n, supra, </em>at 94 (White, J., concurring); <em>McCarthy </em>v. <em>Arndstein, </em><span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/#40" aria-description="Citation for case: McCarthy v. Arndstein">266 U. S. 34, 40</a></span> (1924); <em>United States </em>v. <em>Saline Bank, </em><span class="citation" data-id="85566"><a href="/opinion/85566/the-united-states-v-the-saline-bank-of-virginia-john-webster-and-others/" aria-description="Citation for case: The United States v. The Saline Bank of Virginia, John...">1 Pet. 100</a></span> (1828); cf. <em>Gardner </em>v. <em>Broderick, </em><span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">392 U. S. 273</a></span> (1968).</p>
</footnote>
<footnote label="11">
<p id="b509-6"><em> Hoffman </em>v. <em>United States, </em><span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/#486" aria-description="Citation for case: Hoffman v. United States">341 U. S. 479, 486</a></span> (1951); <em>Blau </em>v. <em>United States, </em><span class="citation" data-id="104833"><a href="/opinion/104833/blau-v-united-states/" aria-description="Citation for case: Blau v. United States">340 U. S. 159</a></span> (1950); <em>Mason </em>v. <em>United States, </em><span class="citation" data-id="98977"><a href="/opinion/98977/mason-v-united-states/#365" aria-description="Citation for case: Mason v. United States">244 U. S. 362, 365</a></span> (1917).</p>
</footnote>
<footnote label="12">
<p id="b509-7"> See, <em>e. g., Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#443" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 443-444</a></span> (1966); <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 635</a></span> (1886).</p>
</footnote>
<footnote label="13">
<p id="b509-8"> Soon after the privilege against compulsory self-incrimination became firmly established in law, it was recognized that the privilege did not apply when immunity, or “indemnity,” in the English usage, had been granted. See L. Levy, Origins of the Fifth Amendment 328, 495 (1968). Parliament enacted an immunity statute in 1710 directed against illegal gambling, 9 Anne, c. 14, §§ 3-4, which became the model for an identical immunity statute enacted in 1774 by the Colonial Legislature of New York. Law of Mar. 9, 1774, c. 1651, 5 Colonial Laws of New York 621, 623 (1894). These statutes provided that the loser could sue the winner, who was compelled to answer the loser’s charges. After the winner responded and returned his ill-gotten gains, he was “acquitted, indemnified [immunized] and discharged from any further or other Punishment, Forfeiture or Penalty, which he . . . may have incurred by the playing for, and winning such Money . . . .” 9 Anne, c. 14, § 4 (1710); Law of Mar. 9, 1774, c. 1651, 5 Colonial Laws of New York, at 623.</p>
<p id="b509-9">Another notable instance of the early use of immunity legislation is the 1725 impeachment trial of Lord Chancellor Macclesfield. The Lord Chancellor was accused by the House of Commons of the sale of public offices and appointments. In order to compel the testimony of Masters in Chancery who had allegedly purchased their offices from the Lord Chancellor, and who could incriminate themselves by so testifying, Parliament enacted a statute granting immunity to persons then holding office as Masters in Chancery. <em>Lord Chancellor Macclesfield’s Trial, </em>16 How. St. Tr. 767, 1147 (1725). See 8 Wigmore, <em>supra, </em>n. 2, § 2281, at 492. See also <em>Bishop Atter-bury’s Trial, </em>16 How. St. Tr. 323, 604-605 (1723). The legislatures <page-number citation-index="1" label="446">*446</page-number>in colonial Pennsylvania and New York enacted immunity legislation in the 18th century. See, e. <em>g., </em>Resolution of Jan. 6, 1758, in Votes and Proceedings of the House of Representatives of the Province of Pennsylvania (1682-1776), 6 Pennsylvania Archives (8th series) 4679 (C. Hoban ed. 1935); Law of Mar. 24, 1772, c. 1542, 5 Colonial Laws of New York 351, 353-354; Law of Mar. 9, 1774, c. 1651, <em>id., </em>at 621, 623; Law of Mar. 9, 1774, c. 1655, <em>id., </em>at 639, 641-642. See generally L. Levy, Origins of the Fifth Amendment 359, 384-385, 389, 402-403 (1968). Federal immunity statutes have existed since 1857. Act of Jan. 24, 1857, <span class="citation no-link">11 Stat. 155</span>. For a history of the various federal immunity statutes, see Comment, The Federal Witness Immunity Acts in Theory and Practice: Treading the Constitutional Tightrope, 72 Yale L. J. 1568 (1963); Wendel, Compulsory Immunity Legislation and the Fifth Amendment Privilege: New Developments and New Confusion, 10 St. Louis U. L. Rev. 327 (1966); and National Commission on Reform of Federal Criminal Laws, Working Papers, 1406-1411 (1970).</p>
</footnote>
<footnote label="14">
<p id="b510-6"> See, <em>e. g., </em>Resolution of Jan. 6, 1758, n. 13, <em>supra, </em>6 Pennsylvania Archives (8th series) 4679 (C. Hoban ed. 1935); Law of Mar. 24, 1772, c. 1542, 5 Colonial Laws of New York 351, 354; Law of Mar. 9, 1774, c. 1655, <em>id., </em>at 639, 642. <em>Bishop Atter-bury’s Trial, supra, </em>for which the House of Commons passed immunity legislation, was a prosecution for treasonable conspiracy. See <em>id., </em>at 604-605; 8 Wigmore, <em>supra, </em>n. 2, §2281, at 492 n. 2. <em>Lord Chancellor Macclesfield’s Trial, supra, </em>for which Parliament passed immunity legislation, was a prosecution for political bribery involving the sale of public offices and appointments. See <em>id., </em>at 1147. The first federal immunity statute was enacted to facilitate an investigation of charges of corruption and vote buying in the House of Representatives. See Comment, n. 13, <em>supra, </em>72 Yale L. J., at 1571.</p>
</footnote>
<footnote label="15">
<p id="b511-5"> See 8 Wigmore, <em>supra, </em>n. 2, § 2281, at 492. Mr. Justice White noted in his concurring opinion in <em>Murphy </em>v. <em>Waterfront Comm’n, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#92" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S., at 92</a></span>, that immunity statutes “have for more than a century been resorted to for the investigation of many offenses, chiefly those whose proof and punishment were otherwise impracticable, such as political bribery, extortion, gambling, consumer frauds, liquor violations, commercial larceny, and various forms of racketeering.” <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#94" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor"><em>Id., </em>at 94-95</a></span>. See n. 14, <em>supra.</em></p>
</footnote>
<footnote label="10">
<p id="b511-6"> See Comment, n. 13, <em>supra, </em>72 Yale L. J., at 1576.</p>
</footnote>
<footnote label="17">
<p id="b511-7"> For a listing of these statutes, see National Commission on Reform of Federal Criminal Laws, Working Papers, 1444-1445 (1970).</p>
</footnote>
<footnote label="18">
<p id="b511-8"> For a listing of these statutes, see 8 Wigmore, <em>supra, </em>n. 2, § 2281, at 495 n. 11.</p>
</footnote>
<footnote label="19">
<p id="b511-9"> See, <em>e. g., </em>8 J. Wigmore, Evidence § 2281, at 501 (3d ed. 1940); 8 Wigmore, <em>supra, </em>n. 2, § 2281, at 496.</p>
</footnote>
<footnote label="20">
<p id="b511-10"> See <em>Hale </em>v. <em>Henkel, </em><span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#70" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 70</a></span> (1906); <em>Brown </em>v. <em>Walker, </em><span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#610" aria-description="Citation for case: Brown v. Walker">161 U. S., at 610</a></span>.</p>
</footnote>
<footnote label="21">
<p id="b511-11"> This statement was made with specific reference to the Compulsory Testimony Act of 1893, <span class="citation no-link">27 Stat. 443</span>, the model for almost all federal immunity statutes prior to the enactment of the statute under consideration in this case. See <em>Murphy </em>v. <em>Waterfront Comm’n, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#95" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S., at 95</a></span> (White, J., concurring).</p>
</footnote>
<footnote label="22">
<p id="b512-9"> Accord, <em>Gardner </em>v. <em>Broderick, </em><span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/#276" aria-description="Citation for case: Gardner v. Broderick">392 U. S., at 276</a></span>; <em>Murphy </em>v. <em>Waterfront Comm’n, supra; McCarthy </em>v. <em>Arndstein, </em><span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/#42" aria-description="Citation for case: McCarthy v. Arndstein">266 U. S., at 42</a></span> (Brandéis, J.); <em>Heilce </em>v. <em>United States, </em><span class="citation" data-id="97764"><a href="/opinion/97764/heike-v-united-states/#142" aria-description="Citation for case: Heike v. United States">227 U. S. 131, 142</a></span> (1913) (Holmes, J.).</p>
</footnote>
<footnote label="23">
<p id="b513-7"> Eor other provisions of the 1970 Act relative to immunity of witnesses, see <span class="citation no-link">18 U. S. C. §§ 6001-6005</span>.</p>
</footnote>
<footnote label="24">
<p id="b513-8"> See, <em>e. g., Murphy </em>v. <em>Waterfront Comm’n, supra, </em>at 54, 78; <em>Counselman </em>v. <em>Hitchcock, </em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#585" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 585</a></span> (1892).</p>
</footnote>
<footnote label="25">
<p id="b513-9"> See <em>Piccirillo </em>v. <em>New York, </em><span class="citation" data-id="9424403"><a href="/opinion/108238/piccirillo-v-new-york/" aria-description="Citation for case: Piccirillo v. New York">400 U. S. 548</a></span> (1971).</p>
</footnote>
<footnote label="26">
<p id="b513-10"> <span class="citation no-link">15 Stat. 37</span>.</p>
</footnote>
<footnote label="27">
<p id="b514-6"> See <em>Counselman </em>v. <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#560" aria-description="Citation for case: Counselman v. Hitchcock"><em>Hitchcock, supra, </em>at 560</a></span>.</p>
</footnote>
<footnote label="28">
<p id="b514-7"> <em>In re Counselman, </em><span class="citation" data-id="9305828"><a href="/opinion/9310678/in-re-counselman/" aria-description="Citation for case: In re Counselman">44 F. 268</a></span> (CCND Ill. 1890).</p>
</footnote>
<footnote label="29">
<p id="b514-8"> <em>Counselman </em>v. <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#564" aria-description="Citation for case: Counselman v. Hitchcock"><em>Hitchcock, supra, </em>at 564</a></span>.</p>
</footnote>
<footnote label="30">
<p id="b514-9"> Precisely, the Court held “that legislation cannot abridge a constitutional privilege, and that it cannot replace or supply [sic] one, at least unless it is so broad as to have the same extent in scope and effect.” <em>Id,., </em>at 585. See <em>Murphy </em>v. <em>Waterfront Comm’n, supra, </em>at 54, 78.</p>
</footnote>
<footnote label="31">
<p id="b515-7"> <em>Counselman </em>was decided Jan. 11, 1892. Senator Cullom introduced the new bill on Jan. 27, 1892. 23 Cong. Rec. 573.</p>
</footnote>
<footnote label="32">
<p id="b515-8"> 23 Cong. Rec. 6333.</p>
</footnote>
<footnote label="33">
<p id="b515-9"> Act of Feb. 11, 1893, <span class="citation no-link">27 Stat. 443</span>, repealed by the Organized Crime Control Act of 1970, <span class="citation no-link">Pub. L. No. 91-452, § 245</span>, <span class="citation no-link">84 Stat. 931</span>.</p>
</footnote>
<footnote label="34">
<p id="b515-10"> See the remarks of Senator Cullom, 23 Cong. Rec. 573, 6333, and Congressman Wise, who introduced the bill in the House. 24 Cong. Rec. 503. See <em>Shapiro </em>v. <em>United States, </em><span class="citation" data-id="9420211"><a href="/opinion/104585/shapiro-v-united-states/" aria-description="Citation for case: Shapiro v. United States">335 U. S. 1</a></span>, 28-29 and n. 36 (1948).</p>
</footnote>
<footnote label="35">
<p id="b516-5"> <em>Ullmann </em>v. <em>United States, </em><span class="citation" data-id="9421245"><a href="/opinion/105363/ullmann-v-united-states/#438" aria-description="Citation for case: Ullmann v. United States">350 U. S., at 438</a></span>; <em>Shapiro </em>v. <em>United States, supra, </em>at 6. There was one minor exception. See <em>Piccirillo </em>v. <em>New York, </em><span class="citation" data-id="9424403"><a href="/opinion/108238/piccirillo-v-new-york/" aria-description="Citation for case: Piccirillo v. New York">400 U. S., at 571</a></span> and n. 11 (Brennan, J., dissenting); <em>Arndstein </em>v. <em>McCarthy, </em><span class="citation" data-id="8144042"><a href="/opinion/8182123/arndstein-v-mccarthy/#73" aria-description="Citation for case: Arndstein v. McCarthy">254 U. S. 71, 73</a></span> (1920).</p>
</footnote>
<footnote label="36">
<p id="b516-6"> The statute is a product of careful study and consideration by the National Commission on Reform of Federal Criminal Laws, as well as by Congress. The Commission recommended legislation to reform the federal immunity laws. The recommendation served as the model for this statute. In commenting on its proposal in a special report to the President, the Commission said:</p>
<blockquote id="b516-7">“We are satisfied that our substitution of immunity from use for immunity from prosecution meets constitutional requirements for overcoming the claim of privilege. Immunity from use is the only consequence flowing from a violation of the individual’s constitutional right to be protected from unreasonable searches and seizures, his constitutional right to counsel, and his constitutional right not to be coerced into confessing. The proposed immunity is thus of the same scope as that frequently, even though unintentionally, conferred as the result of constitutional violations by law enforcement officers.” Second Interim Report of the National Commission on Reform of Federal Criminal Laws, Mar. 17, 1969, Working Papers of the Commission, 1446 (1970).</blockquote>
<p id="b516-8">The Commission’s recommendation was based in large part on a comprehensive study of immunity and the relevant decisions of this Court prepared for the Commission by Prof. Robert G. Dixon, Jr., of the George Washington University Law Center, and transmitted to the President with the recommendations of the Commission. See National Commission on Reform of Federal Criminal Laws, Working Papers, 1405-1444 (1970).</p>
</footnote>
<footnote label="37">
<p id="b517-7"> See S. Rep. No. 91-617, pp. 51-56, 145 (1969); H. R. Rep. No. 91-1549, p. 42 (1970).</p>
</footnote>
<footnote label="38">
<p id="b517-8"> <em>Ullmann </em>v. <em>United States, </em><span class="citation" data-id="9421245"><a href="/opinion/105363/ullmann-v-united-states/#438" aria-description="Citation for case: Ullmann v. United States">350 U. S., at 438-439</a></span>, quoting <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#634" aria-description="Citation for case: Boyd v. United States">116 U. S., at 634</a></span>. See <em>Knapp </em>v. <em>Schweitzer, </em>357, U. S. 371, 380 (1958).</p>
</footnote>
<footnote label="39">
<p id="b519-6"> Cf. The Supreme Court, 1963 Term, <span class="citation no-link">78 Harv. L. Rev. 179</span>, 230 (1964). Language similar to the <em>Counselman </em>dictum can be found in <em>Brown </em>v. <em>Walker, </em><span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#594" aria-description="Citation for case: Brown v. Walker">161 U. S., at 594-595</a></span>, and <em>Hále </em>v. <em>Henkel, </em><span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#67" aria-description="Citation for case: Hale v. Henkel">201 U. S., at 67</a></span>. <em><span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/" aria-description="Citation for case: Brown v. Walker">Brown</a></span> </em>and <em><span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/" aria-description="Citation for case: Hale v. Henkel">Hale</a></span>, </em>however, involved statutes that were clearly sufficient to supplant the privilege against self-incrimination, as they provided full immunity from prosecution “for or on account of any transaction, matter or thing, concerning which he may testify, or produce evidence <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#594" aria-description="Citation for case: Brown v. Walker">161 U. S., at 594</a></span>; <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#66" aria-description="Citation for case: Hale v. Henkel">201 U. S., at 66</a></span>. The same is true of <em>Smith </em>v. <em>United States, </em><span class="citation" data-id="104675"><a href="/opinion/104675/smith-v-united-states/#141" aria-description="Citation for case: Smith v. United States">337 U. S. 137, 141, 146</a></span> (1949), and <em>United States </em>v. <em>Monia, </em><span class="citation" data-id="9419281"><a href="/opinion/103748/united-states-v-monia/#425" aria-description="Citation for case: United States v. Monia">317 U. S. 424, 425, 428</a></span> (1943). In <em>Albertson </em>v. <em>Subversive Activities Control Board, </em><span class="citation" data-id="9423096"><a href="/opinion/107110/albertson-v-subversive-activities-control-board/" aria-description="Citation for case: Albertson v. Subversive Activities Control Board">382 U. S. 70</a></span> (1965), some of the <em>Counselman </em>language urged upon us by petitioners was again quoted. But <em><span class="citation" data-id="9423096"><a href="/opinion/107110/albertson-v-subversive-activities-control-board/" aria-description="Citation for case: Albertson v. Subversive Activities Control Board">Albertson</a></span>, </em>like <em>Counselman, </em>involved an immunity statute that was held insufficient for failure to prohibit the use of evidence derived from compelled admissions and the use of compelled admissions as an “investigatory lead.” <em>Id., </em>at 80.</p>
<p id="b519-8">In <em>Adams </em>v. <em>Maryland, </em><span class="citation" data-id="9421044"><a href="/opinion/105197/adams-v-maryland/#182" aria-description="Citation for case: Adams v. Maryland">347 U. S. 179, 182</a></span> (1954), and in <em>United States </em>v. <em>Murdock, </em><span class="citation" data-id="101804"><a href="/opinion/101804/united-states-v-murdock/#149" aria-description="Citation for case: United States v. Murdock">284 U. S. 141, 149</a></span> (1931), the <em>Counselman </em>dictum was referred to as the principle of <em>Counselman. </em>The references were in the context of ancillary points not essential to the decisions of the Court. The <em><span class="citation" data-id="9421044"><a href="/opinion/105197/adams-v-maryland/" aria-description="Citation for case: Adams v. Maryland">Adams</a></span> </em>Court did note, however, that the Fifth Amendment privilege prohibits the “use” of compelled self-incriminatory testimony. <span class="citation" data-id="9421044"><a href="/opinion/105197/adams-v-maryland/#181" aria-description="Citation for case: Adams v. Maryland">347 U. S., at 181</a></span>. In any event, the Court in <em>Ullmann </em>v. <em>United States, </em><span class="citation" data-id="9421245"><a href="/opinion/105363/ullmann-v-united-states/#436" aria-description="Citation for case: Ullmann v. United States">350 U. S., at 436-437</a></span>, recognized that the rationale of <em>Counselman </em>was that the <em>Counselman </em>statute was insufficient for failure to prohibit the use of evidence derived from compelled testimony. See also <em>Arndstein </em>v. <em>McCarthy, </em><span class="citation" data-id="8144042"><a href="/opinion/8182123/arndstein-v-mccarthy/#73" aria-description="Citation for case: Arndstein v. McCarthy">254 U. S., at 73</a></span>.</p>
</footnote>
<footnote label="40">
<p id="b520-6"> The Waterfront Commission of New York Harbor is a bistate body established under an interstate compact approved by Congress. <span class="citation no-link">67 Stat. 541</span>.</p>
</footnote>
<footnote label="41">
<p id="b520-7"> <em>In re Waterfront Comm’n of N. Y. Harbor, </em>39 N. J. 436, <span class="citation" data-id="1513654"><a href="/opinion/1513654/in-re-application-of-waterfront-comn-of-ny-harbor/" aria-description="Citation for case: In Re Application of Waterfront Com&#x27;n of Ny Harbor">189 A. 2d 36</a></span> (1963).</p>
</footnote>
<footnote label="42">
<p id="b520-8"> Reconsideration of the rule that the Fifth Amendment privilege does not protect a witness in one jurisdiction against being compelled to give testimony that could be used to convict him in another jurisdiction was made necessary by the decision in <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964), in which the Court held the Fifth Amendment privilege applicable to the States through the Fourteenth Amendment. <em>Murphy </em>v. <em>Waterfront Comm’n, </em>378 U. S., at 57.</p>
</footnote>
<footnote label="43">
<p id="b521-7"> At this point the Court added the following note: “Once a defendant demonstrates that he has testified, under a state grant of immunity, to matters related to the federal prosecution, the federal authorities have the burden of showing that their evidence is not tainted by establishing that they had an independent, legitimate source for the disputed evidence.” <em>Id., </em>at 79 n. 18. If transactional immunity had been deemed to be the “constitutional rule” there could be no federal prosecution.</p>
</footnote>
<footnote label="44">
<p id="b522-5"> See, <em>e. g., California </em>v. <em>Byers, </em><span class="citation" data-id="9424566"><a href="/opinion/108335/california-v-byers/" aria-description="Citation for case: California v. Byers">402 U. S. 424</a></span>, 442 n. 3 (1971) (Harlan, J., concurring in judgment); <em>United States </em>v. <em>Freed, </em><span class="citation" data-id="9424498"><a href="/opinion/108299/united-states-v-freed/" aria-description="Citation for case: United States v. Freed">401 U. S. 601</a></span>, 606 n. 11 (1971); <em>Piccirillo </em>v. <em>New York, </em><span class="citation" data-id="9424403"><a href="/opinion/108238/piccirillo-v-new-york/" aria-description="Citation for case: Piccirillo v. New York">400 U. S. 548</a></span> (1971); <em>Stevens </em>v. <em>Marks, </em><span class="citation" data-id="9423156"><a href="/opinion/107173/stevens-v-marks/" aria-description="Citation for case: Stevens v. Marks">383 U. S. 234</a></span>, 24&lt;R245 (1966).</p>
</footnote>
<footnote label="45">
<p id="b522-6"> <em>E. g., Murphy </em>v. <em>Waterfront Comm’n, swpra; Ullmann </em>v. <em>United States, supra; Smith </em>v. <em>United States, </em>337 IT. S. 137 (1949); <em>United States </em>v. <em>Monia, </em><span class="citation" data-id="9419281"><a href="/opinion/103748/united-states-v-monia/" aria-description="Citation for case: United States v. Monia">317 U. S. 424</a></span> (1943); <em>Hale </em>v. <em><span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/" aria-description="Citation for case: Hale v. Henkel">Henkel</a></span>, </em>201 IT. S. 43 (1906); <em>Jack </em>v. <em>Kansas, </em><span class="citation" data-id="96350"><a href="/opinion/96350/jack-v-kansas/" aria-description="Citation for case: Jack v. Kansas">199 U. S. 372</a></span> (1905); <em>Brown </em>v. <em><span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/" aria-description="Citation for case: Brown v. Walker">Walker</a></span>, </em>161 IT. S. 591 (1896). See also n. 35, <em>supra.</em></p>
</footnote>
<footnote label="46">
<p id="b522-7"><em> E. g., Albertson </em>v. <em><span class="citation" data-id="9423096"><a href="/opinion/107110/albertson-v-subversive-activities-control-board/" aria-description="Citation for case: Albertson v. Subversive Activities Control Board">Subversive Activities Control Board</a></span>, </em>382 IT. S., at 80; <em>Arndstein </em>v. <em>McCarthy, </em>254 IT. S., at 73.</p>
</footnote>
<footnote label="47">
<p id="b522-8"> In <em>Malloy </em>v. <em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Hogan</a></span>, </em>378 IT. S., at 10-11, the Court held that the same standards would determine the extent or scope of the privilege in state and in federal proceedings, because the same substantive guarantee of the Bill of Rights is involved. The <em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">Murphy</a></span> </em>Court emphasized that the scope of the privilege is the same in state and in federal proceedings. <em>Murphy </em>v. <em>Waterfront Comm’n, </em>378 U. S., at 79.</p>
</footnote>
<footnote label="48">
<p id="b523-9"> <em>Ibid.</em></p>
</footnote>
<footnote label="49">
<p id="b523-10"> As the Court noted in <em>Gardner </em>v. <em>Broderick, </em><span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/#276" aria-description="Citation for case: Gardner v. Broderick">392 U. S., at 276</a></span>, “[a]nswers may be compelled regardless of the privilege if there is immunity from federal and state use of the compelled testimony or its fruits in connection with a criminal prosecution against the person testifying.”</p>
</footnote>
<footnote label="50">
<p id="b524-10"> See, <em>e. g., Albertson </em>v. <em>Subversive Activities Control Board, </em><span class="citation" data-id="9423096"><a href="/opinion/107110/albertson-v-subversive-activities-control-board/#80" aria-description="Citation for case: Albertson v. Subversive Activities Control Board">382 U. S., at 80</a></span>.</p>
</footnote>
<footnote label="51">
<p id="b525-6"> See <em>Murphy </em>v. <em>Waterfront Comm’n, </em>378 U. S., at 102-104 (White, J., concurring).</p>
</footnote>
<footnote label="52">
<p id="b525-7"> <em>Adams </em>v. <em>Maryland, </em><span class="citation" data-id="9421044"><a href="/opinion/105197/adams-v-maryland/#181" aria-description="Citation for case: Adams v. Maryland">347 U. S., at 181</a></span>; <em>Bram </em>v. <em>United States, </em><span class="citation" data-id="94789"><a href="/opinion/94789/hall-v-united-states/#542" aria-description="Citation for case: Hall v. United States">168 U. S. 632, 542</a></span> (1897).</p>
</footnote>
<footnote label="53">
<p id="b525-8"> As Mr. Justice White, concurring in <em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">Murphy</a></span>, </em>pointed out:</p>
<blockquote id="b525-9"><em>“A </em>coerced confession is as revealing of leads as testimony given in exchange for immunity and indeed is excluded in part because it is compelled incrimination in violation of the privilege. <em>Malloy </em>v. <em>Hogan, </em>[<span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#7" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 7-8</a></span>]; <em>Spano </em>v. <em>New York, </em><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span>; <em>Bram </em>v. <em>United States, </em><span class="citation multiple-matches"><a href="/c/U.%20S./168/532/">168 U. S. 532</a></span>.” 378 U. S., at 103.</blockquote>
</footnote>
<footnote label="54">
<p id="b525-10"> <em>Jackson </em>v. <em>Denno, </em><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">378 U. S. 368</a></span> (1964).</p>
</footnote>
<footnote label="55">
<p id="b526-12"> See <em>supra, </em>at 460; Brief for the United States 37; Cf. <em>Chapman </em>v. <em>Calijornia, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967).</p>
</footnote>
<footnote label="56">
<p id="b526-13"> <em>Jackson </em>v. <em><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Denno, supra.</a></span></em></p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/kentucky-v-graham--111500.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "896f7efe0a421647", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "kentucky-v-graham--111500"}, "payload": {"all": [{"cite": "473 U.S. 159", "page": "159", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "473"}, {"cite": "105 S. Ct. 3099", "page": "3099", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "105"}, {"cite": "87 L. Ed. 2d 114", "page": "114", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "87"}, {"cite": "1985 U.S. LEXIS 86", "page": "86", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1985"}, {"cite": "53 U.S.L.W. 4966", "page": "4966", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "53"}], "display": null, "official": null, "official_selection_present": false, "record_id": "kentucky-v-graham--111500"}}
{"assertion_id": "62081f93ebd42169", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "kentucky-v-graham--111500"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "kentucky-v-graham--111500", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — kentucky-v-graham--111500

```json
{
  "schema_version": "s2.v1",
  "record_id": "kentucky-v-graham--111500",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Kentucky v. Graham",
    "case_name_short": "Graham",
    "case_name_full": "KENTUCKY, Dba BUREAU OF STATE POLICE v. GRAHAM Et Al.",
    "input_case_name": "Kentucky v. Graham",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-06-28",
    "year": 1985,
    "docket": null,
    "cluster_id": 111500,
    "lead_opinion_id": 111500,
    "sibling_ids": [],
    "absolute_url": "/opinion/111500/kentucky-v-graham/",
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
        "cite": "473 U.S. 159",
        "volume": "473",
        "reporter": "U.S.",
        "page": "159",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 3099",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "3099",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 L. Ed. 2d 114",
        "volume": "87",
        "reporter": "L. Ed. 2d",
        "page": "114",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4966",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4966",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 86",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "86",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "473 U.S. 159",
        "volume": "473",
        "reporter": "U.S.",
        "page": "159",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 3099",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "3099",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 L. Ed. 2d 114",
        "volume": "87",
        "reporter": "L. Ed. 2d",
        "page": "114",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 86",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "86",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4966",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4966",
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
    "date_created": "2026-07-06T13:54:27Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:54:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:54:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:54:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:54:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — kentucky-v-graham--111500

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="AW_s">
<span citation-index="1" class="star-pagination" label="161"> 
   *161
   </span>
  Justice Marshall
 </author>
<p id="A2Ib">
  delivered the opinion of the Court.
 </p>
<p id="Agkg">
  The question presented is whether <span class="citation no-link">42 U. S. C. §1988</span> allows attorney’s fees to be recovered from a governmental entity when a plaintiff sues governmental employees only in their personal capacities and prevails.
 </p>
<p id="Ag3v">
  I
 </p>
<p id="Aju">
  On November 7, 1979, a Kentucky state trooper was murdered. Suspicion quickly focused on Clyde Graham, whose stepmother’s car was found near the site of the slaying and whose driver’s license and billfold were discovered in nearby bushes. That evening, 30 to 40 city, county, and state police officers converged on the house of Graham’s father in Elizabethtown, Kentucky. Without a warrant, the police entered the home twice and eventually arrested all the occupants, who are the six respondents here. Graham was not among them.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  According to respondents, they were severely beaten, terrorized, illegally searched, and falsely arrested. Kenneth Brandenburgh, the Commissioner of the State Police and the highest ranking law enforcement officer in Kentucky, allegedly was directly involved in carrying out at least one of the raids. An investigation by the Kentucky Attorney General’s office later concluded that the police had used excessive force and that a “complete breakdown” in police discipline had created an “uncontrolled” situation. App. to Brief for Respondents 21-22.
 </p>
<p id="AU0F">
  Alleging a deprivation of a number of federal rights, respondents filed suit in Federal District Court.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  Their com
  <span citation-index="1" class="star-pagination" label="162"> 
   *162
   </span>
  plaint sought only money damages and named as defendants various local and state law enforcement officers, the city of Elizabethtown, and Hardin County, Kentucky. Also made defendants were Commissioner Brandenburgh, “individually and as Commissioner of the Bureau of State Police,” and the Commonwealth of Kentucky. The Commonwealth was sued, not for damages on the merits, but only for attorney’s fees should the plaintiffs eventually prevail.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  Shortly after the complaint was filed, the District Court, relying on the Eleventh Amendment, dismissed the Commonwealth as a party. Based on its Attorney General’s report, the Commonwealth refused to defend any of the individual defendants, including Commissioner Brandenburgh, or to pay their litigation expenses.
 </p>
<p id="b200-5">
  On the second day of trial, the case was settled for $60,000.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  The settlement agreement, embodied in a court order dismissing the case, barred respondents from seeking attorney’s fees from any of the individual defendants but specifically preserved respondents’ right to seek fees and court costs from the Commonwealth. Respondents then moved, pursuant to <span class="citation no-link">42 U. S. C. § 1988</span>, that the Commonwealth pay their costs and attorney’s fees. At a hearing on this motion, the Commonwealth argued that the fee request had to be
  <span citation-index="1" class="star-pagination" label="163"> 
   *163
   </span>
  denied as a matter of law, both because the Commonwealth had been dismissed as a party and because the Eleventh Amendment, in any event, barred such an award. Rejecting these arguments, the District Court ordered the Commonwealth to pay $58,521 in fees and more than $6,000 in costs and expenses.
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  In a short
  <em>
   per curiam
  </em>
  opinion relying solely on this Court’s decision in
  <em>
   Hutto
  </em>
  v.
  <em>
   Finney,
  </em>
  <span class="citation" data-id="9427304"><a href="/opinion/109919/hutto-v-finney/" aria-description="Citation for case: Hutto v. Finney">437 U. S. 678</a></span> (1978), the Court of Appeals for the Sixth Circuit affirmed.
  <em>
   Graham
  </em>
  v.
  <em>
   Wilson,
  </em>
  <span class="citation" data-id="441338"><a href="/opinion/441338/graham-v-wilson/" aria-description="Citation for case: Graham v. Wilson">742 F. 2d 1455</a></span> (1984).
 </p>
<p id="AvB4">
  We granted certiorari to address the proposition, rejected by at least two Courts of Appeals,
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
  that fees can be recovered from a governmental entity when a plaintiff prevails in a suit against government employees in their personal capacities. <span class="citation multiple-matches"><a href="/c/U.%20S./469/1156/">469 U. S. 1156</a></span> (1985). We now reverse.
 </p>
<p id="AKK">
  H — I I
 </p>
<p id="Amr">
  This case requires us to unravel once again the distinctions between personal- and official-capacity suits, see
  <em>
   Brandon
  </em>
  v.
  <em>
   Holt,
  </em>
  <span class="citation" data-id="9429823"><a href="/opinion/111304/brandon-v-holt/" aria-description="Citation for case: Brandon v. Holt">469 U. S. 464</a></span> (1985), this time in the context of fee awards under <span class="citation no-link">42 U. S. C. § 1988</span>. The relevant portion of § 1988, enacted as the Civil Rights Attorney’s Fees Awards Act of 1976, <span class="citation no-link">90 Stat. 2641</span>, provides:
 </p>
<blockquote id="Asoq">
  “In any action or proceeding to enforce a provision of sections 1981, 1982, 1983, 1985, and 1986 of this title, title IX of <span class="citation no-link">Public Law 92-318, </span>or title VI of the Civil Rights Act of 1964, the court, in its discretion, may allow
  <em>
   the prevailing party,
  </em>
  other than the United States, a reasonable attorney’s fee as part of the costs” (emphasis added).
 </blockquote>
<p id="b202-4">
<span citation-index="1" class="star-pagination" label="164"> 
   *164
   </span>
  If a plaintiff prevails in a suit covered by § 1988, fees should be awarded as costs “unless special circumstances would render such an award unjust.” S. Rep. No. 94-1011, p. 4 (1976); see
  <em>
   Supreme Court of Virginia
  </em>
  v.
  <em>
   Consumers Union of United States, Inc.,
  </em>
  <span class="citation" data-id="110273"><a href="/opinion/110273/supreme-court-of-virginia-v-consumers-union-of-the-united-states-inc/#737" aria-description="Citation for case: Supreme Court of Virginia v. Consumers Union of the...">446 U. S. 719, 737</a></span> (1980). Section 1988 does not in so many words define the parties who must bear these costs. Nonetheless, it is clear that the logical place to look for recovery of fees is to the losing party — the party legally responsible for relief on the merits. That is the party who must pay the costs of the litigation, see generally Fed. Rule Civ. Proc. 54(d),
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  and it is clearly the party who should also bear fee liability under § 1988.
 </p>
<p id="b202-5">
  We recognized as much in
  <em>
   Supreme Court of <span class="citation" data-id="110273"><a href="/opinion/110273/supreme-court-of-virginia-v-consumers-union-of-the-united-states-inc/" aria-description="Citation for case: Supreme Court of Virginia v. Consumers Union of the...">Virginia, supra.</a></span>
  </em>
  There a three-judge District Court had found the Virginia Supreme Court and its chief justice in his official capacity liable for promulgating, and refusing to amend, a State Bar Code that violated the First Amendment. The District Court also awarded fees against these defendants pursuant to § 1988. We held that absolute legislative immunity shielded these defendants for acts taken in their legislative capacity. We then vacated the fee award, stating that we found nothing “in the legislative history of the Act to suggest that Congress intended to permit an award of attorney’s fees to be premised on acts for which defendants would enjoy absolute legislative immunity.” <span class="citation" data-id="110273"><a href="/opinion/110273/supreme-court-of-virginia-v-consumers-union-of-the-united-states-inc/#738" aria-description="Citation for case: Supreme Court of Virginia v. Consumers Union of the...">446 U. S., at 738</a></span>.
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
<span citation-index="1" class="star-pagination" label="165"> 
   *165
   </span>
  Thus, liability on the merits and responsibility for fees go hand in hand; where a defendant has not been prevailed against, either because of legal immunity or on the merits, § 1988 does not authorize a fee award against that defendant.
  <a class="footnote" href="#fn9" id="fn9_ref">
   9
  </a>
  Cf.
  <em>
   Pulliam
  </em>
  v.
  <em>
   Allen,
  </em>
  <span class="citation" data-id="9429586"><a href="/opinion/111166/pulliam-v-allen/#543" aria-description="Citation for case: Pulliam v. Allen">466 U. S. 522, 543-544</a></span> (1984) (state judge liable for injunctive and declaratory relief under § 1988 also liable for fees under § 1988).
 </p>
<p id="b203-5">
  A
 </p>
<p id="b203-6">
  Proper application of this principle in damages actions against public officials requires careful adherence to the distinction between personal- and official-capacity suits.
  <a class="footnote" href="#fn10" id="fn10_ref">
   10
  </a>
  Because this distinction apparently continues to confuse lawyers and confound lower courts, we attempt to define it more clearly through concrete examples of the practical and doctrinal differences between personal- and official-capacity actions.
 </p>
<p id="b203-7">
  Personal-capacity suits seek to impose personal liability upon a government official for actions he takes under color of state law. See,
  <em>
   e. g., Scheuer
  </em>
  v.
  <em>
   Rhodes,
  </em>
  <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#237" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232, 237-238</a></span> (1974). Official-capacity suits, in contrast, “generally represent only another way of pleading an action against an entity of which an officer is an agent.”
  <em>
   Monell
  </em>
  v.
  <em>
   New York City Dept. of Social Services,
  </em>
  <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#690" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658, 690</a></span>, n. 55
  <span citation-index="1" class="star-pagination" label="166"> 
   *166
   </span>
  (1978). As long as the government entity receives notice and an opportunity to respond, an official-capacity suit is, in all respects other than name, to be treated as a suit against the entity.
  <em>
   Brandon,
  </em>
  <span class="citation" data-id="9429823"><a href="/opinion/111304/brandon-v-holt/#471" aria-description="Citation for case: Brandon v. Holt">469 U. S., at 471-472</a></span>. It is
  <em>
   not
  </em>
  a suit against the official personally, for the real party in interest is the entity. Thus, while an award of damages against an official in his personal capacity can be executed only against the official’s personal assets, a plaintiff seeking to recover on a damages judgment in an official-capacity suit must look to the government entity itself.
  <a class="footnote" href="#fn11" id="fn11_ref">
   11
  </a>
</p>
<p id="b204-5">
  On the merits, to establish
  <em>
   personal
  </em>
  liability in a § 1983 action, it is enough to show that the official, acting under color of state law, caused the deprivation of a federal right. See,
  <em>
   e. g., Monroe
  </em>
  v.
  <em>
   Pape,
  </em>
  <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167</a></span> (1961). More is required in an official-capacity action, however, for a governmental entity is liable under § 1983 only when the entity itself is a “ ‘moving force’ ” behind the deprivation,
  <em>
   Polk County
  </em>
  v.
  <em>
   Dodson,
  </em>
  <span class="citation" data-id="9428551"><a href="/opinion/110589/polk-county-v-dodson/#326" aria-description="Citation for case: Polk County v. Dodson">454 U. S. 312, 326</a></span> (1981) (quoting
  <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs."><em>
   Monell, supra,
  </em>
  at 694</a></span>); thus, in an official-capacity suit the entity’s “policy or custom” must have played a part in the violation of federal law.
  <em>
   <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell, supra;</a></span> Oklahoma City
  </em>
  v.
  <em>
   Tuttle,
  </em>
  <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#817" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S. 808, 817-818</a></span> (1985);
  <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#827" aria-description="Citation for case: City of Oklahoma v. Tuttle"><em>
   id.,
  </em>
  at 827-828</a></span> (Brennan, J., concurring in judgment).
  <a class="footnote" href="#fn12" id="fn12_ref">
   12
  </a>
  When it comes to defenses to liability, an official in a personal-capacity action may, depending on his position, be able to assert personal immunity defenses, such
  <span citation-index="1" class="star-pagination" label="167"> 
   *167
   </span>
  as objectively reasonable reliance on existing law. See
  <em>
   Imbler
  </em>
  v.
  <em>
   Pachtman,
  </em>
  <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409</a></span> (1976) (absolute immunity);
  <em>
   Pierson
  </em>
  v.
  <em>
   Ray,
  </em>
  <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547</a></span> (1967) (same);
  <em>
   Harlow
  </em>
  v.
  <em>
   Fitzgerald,
  </em>
  <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800</a></span> (1982) (qualified immunity);
  <em>
   Wood
  </em>
  v.
  <em>
   Strickland,
  </em>
  <span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308</a></span> (1975) (same). In an official-capacity action, these defenses are unavailable.
  <em>
   Owen
  </em>
  v.
  <em>
   City of Independence,
  </em>
  <span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/" aria-description="Citation for case: Owen v. City of Independence">445 U. S. 622</a></span> (1980); see also
  <em>
   Brandon
  </em>
  v.
  <em>
   Holt,
  </em>
  <span class="citation" data-id="9429823"><a href="/opinion/111304/brandon-v-holt/" aria-description="Citation for case: Brandon v. Holt">469 U. S. 464</a></span> (1985).
  <a class="footnote" href="#fn13" id="fn13_ref">
   13
  </a>
  The only immunities that can be claimed in an official-capacity action are forms of sovereign immunity that the entity,
  <em>
   qua
  </em>
  entity, may possess, such as the Eleventh Amendment. While not exhaustive, this list illustrates the basic distinction between personal- and official-capacity actions.
  <a class="footnote" href="#fn14" id="fn14_ref">
   14
  </a>
</p>
<p id="b205-4">
  With this distinction in mind, it is clear that a suit against a government official in his or her personal capacity cannot lead to imposition of fee liability upon the governmental entity. A victory in a personal-capacity action is a victory against the individual defendant, rather than against the
  <span citation-index="1" class="star-pagination" label="168"> 
   *168
   </span>
  entity that employs him. Indeed, unless a distinct cause of action is asserted against the entity itself, the entity is not even a party to a personal-capacity lawsuit and has no opportunity to present a defense. That a plaintiff has prevailed against one party does not entitle him to fees from another party, let alone from a nonparty. Cf.
  <em>
   Hensley
  </em>
  v.
  <em>
   Eckerhart,
  </em>
  <span class="citation" data-id="9429188"><a href="/opinion/110929/hensley-v-eckerhart/" aria-description="Citation for case: Hensley v. Eckerhart">461 U. S. 424</a></span> (1983). Yet that would be the result were we to hold that fees can be recovered from a governmental entity following victory in a personal-capacity action against government officials.
 </p>
<p id="b206-5">
  B
 </p>
<p id="b206-6">
  Such a result also would be inconsistent with the statement in
  <em>
   <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell, supra,</a></span>
  </em>
  that a municipality cannot be made liable under <span class="citation no-link">42 U. S. C. §1983</span> on a
  <em>
   respondeat superior
  </em>
  basis. Nothing in the history of § 1988, a statute designed to make effective the remedies created in § 1983 and similar statutes, suggests that fee liability, unlike merits liability,
  <em>
   was
  </em>
  intended to be imposed on a
  <em>
   respondeat superior
  </em>
  basis. On the contrary, just as Congress rejected making § 1983 a “mutual insurance” scheme, <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 694</a></span>, Congress sought to avoid making § 1988 a “‘relief fund for lawyers.’”
  <span class="citation" data-id="9429188"><a href="/opinion/110929/hensley-v-eckerhart/#446" aria-description="Citation for case: Hensley v. Eckerhart"><em>
   Hensley, supra,
  </em>
  at 446</a></span> (opinion of Brennan, J.) (quoting 122 Cong. Rec. 33314 (1976) (remarks of Sen. Kennedy)). Section 1988 does not guarantee that lawyers will recover fees anytime their clients sue a government official in his personal capacity, with the governmental entity as ultimate insurer. Instead, fee liability runs with merits liability; if federal law does not make the government substantively liable on a
  <em>
   respondeat superior
  </em>
  basis, the government similarly is not liable for fees on that basis under §1988. Section 1988 simply does not create fee liability where merits liability is nonexistent.
 </p>
<p id="b206-7">
  Ill
 </p>
<p id="b206-8">
  We conclude that this case was necessarily litigated as a personal-capacity action and that the Court of Appeals therefore erred in awarding fees against the Commonwealth of
  <span citation-index="1" class="star-pagination" label="169"> 
   *169
   </span>
  Kentucky.
  <a class="footnote" href="#fn15" id="fn15_ref">
   15
  </a>
  In asserting the contrary, respondents point out that the complaint expressly named Commissioner Bran-denburgh in both his “individual” and “official” capacities and that the Commonwealth of Kentucky was named as a defendant for the limited purposes of a fee award. Nonetheless, given Eleventh Amendment doctrine, there can be no doubt that this damages action did not seek to impose monetary liability on the Commonwealth.
  <a class="footnote" href="#fn16" id="fn16_ref">
   16
  </a>
</p>
<p id="b207-4">
  The Court has held that, absent waiver by the State or valid congressional override, the Eleventh Amendment bars a damages action against a State in federal court.
  <a class="footnote" href="#fn17" id="fn17_ref">
   17
  </a>
  See,
  <em>
   e. g., Ford Motor Co.
  </em>
  v.
  <em>
   Department of Treasury of Indiana,
  </em>
  <span class="citation" data-id="104057"><a href="/opinion/104057/ford-motor-co-v-department-of-treasury/#464" aria-description="Citation for case: Ford Motor Co. v. Department of Treasury">323 U. S. 459, 464</a></span> (1945). This bar remains in effect when state officials are sued for damages in their official capacity.
  <em>
   Cory
  </em>
  v.
  <em>
   White,
  </em>
  <span class="citation" data-id="9428807"><a href="/opinion/110734/cory-v-white/#90" aria-description="Citation for case: Cory v. White">457 U. S. 85, 90</a></span> (1982);
  <em>
   Edelman
  </em>
  v.
  <em>
   Jordan,
  </em>
  <span class="citation" data-id="9425645"><a href="/opinion/108990/edelman-v-jordan/#663" aria-description="Citation for case: Edelman v. Jordan">415 U. S. 651, 663</a></span> (1974). That is so because, as discussed above, “a judgment against a public servant ‘in his official capacity’ imposes liability on the entity that he represents . . . .”
  <span class="citation" data-id="9429823"><a href="/opinion/111304/brandon-v-holt/#471" aria-description="Citation for case: Brandon v. Holt"><em>
   Brandon, supra,
  </em>
  at 471</a></span>.
  <a class="footnote" href="#fn18" id="fn18_ref">
   18
  </a>
</p>
<p id="Adn">
<span citation-index="1" class="star-pagination" label="170"> 
   *170
   </span>
  Given this understanding of the law, an official-capacity action for damages could not have been maintained against Commissioner Brandenburgh in federal court.
  <a class="footnote" href="#fn19" id="fn19_ref">
   19
  </a>
  Although respondents fail to acknowledge this point, they freely concede that money damages were never sought from the Commonwealth and could not have been awarded against it;
  <a class="footnote" href="#fn20" id="fn20_ref">
   20
  </a>
  respondents cannot reach this same end simply by suing state officials in their official capacity. Nor did respondents’ action on the merits become a suit against Kentucky when the Commonwealth was named a defendant on the limited issue of fee liability. There is no cause of action against a defendant for fees absent that defendant’s liability for relief on the merits. See
  <em>
   swpra,
  </em>
  at 167-168. Naming the Commonwealth for fees did not create, out of whole cloth, the cause of action on the merits necessary to support this fee request. Thus, no claim for merits relief capable of being asserted in federal court was asserted against the Commonwealth of Kentucky. In the absence of such a claim, the fee award against the Commonwealth must be reversed.
 </p>
<p id="Ajn">
  &lt;1
 </p>
<p id="ACC">
  Despite the Court of Appeals’ contrary view, the result we reach today is fully consistent with
  <em>
   Hutto
  </em>
  v.
  <em>
   Finney,
  </em>
  <span class="citation" data-id="9427304"><a href="/opinion/109919/hutto-v-finney/" aria-description="Citation for case: Hutto v. Finney">437 U. S. 678</a></span> (1978).
  <em>
   <span class="citation" data-id="9427304"><a href="/opinion/109919/hutto-v-finney/" aria-description="Citation for case: Hutto v. Finney">Hutto</a></span>
  </em>
  holds only that, when a State in a § 1983 action has been prevailed against for relief on the merits, either because the State was a proper party defendant or because state officials properly were sued in their official capacity, fees may also be available from the State under § 1988.
  <em>
   <span class="citation" data-id="9427304"><a href="/opinion/109919/hutto-v-finney/" aria-description="Citation for case: Hutto v. Finney">Hutto</a></span>
  </em>
  does not alter the basic philosophy of
  <span citation-index="1" class="star-pagination" label="171"> 
   *171
   </span>
  §1988, namely, that fee and merits liability run together. As a result,
  <em>
   <span class="citation" data-id="9427304"><a href="/opinion/109919/hutto-v-finney/" aria-description="Citation for case: Hutto v. Finney">Hutto</a></span>
  </em>
  neither holds nor suggests that fees are available from a governmental entity simply because a government official has been prevailed against in his or her personal capacity.
 </p>
<p id="b209-4">
  Respondents vigorously protest that this holding will “effectively destro[y]” § 1988 in cases such as this one. Brief for Respondents 19. This fear is overstated. Fees are unavailable only where a governmental entity cannot be held liable on the merits; today we simply apply the fee-shifting provisions of §1988 against a pre-existing background of substantive liability rules.
 </p>
<p id="b209-5">
  V
 </p>
<p id="b209-6">
  Only in an official-capacity action is a plaintiff who prevails entitled to look for relief, both on the merits and for fees, to the governmental entity. Because the Court’s Eleventh Amendment decisions required this case to be litigated as a personal-capacity action, the award of fees against the Commonwealth of Kentucky must be reversed.
 </p>
<p id="b209-7">
<em>
   It is so ordered.
  </em>
</p>




















<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="A-K">
   Clyde Graham was killed by a Kentucky state trooper a month later at a motel in Illinois.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="AnB">
   Respondents asserted causes of action under <span class="citation no-link">42 U. S. C. §§ 1983</span>, 1985, 1986, and 1988, as well as the Fourth, Fifth, Sixth, Eleventh, and Fourteenth Amendments. Complaint ¶ 13. Because the case was settled, there has been no need below to separate out or distinguish any of these purported causes of action. Before this Court, the parties briefed and argued the case as if it had been brought simply as a § 1983 action and we, accordingly,
   <span citation-index="1" class="star-pagination" label="162"> 
    *162
    </span>
   analyze it the same way. Our discussion throughout is therefore not meant to express any view on suits brought under any provision of federal law other than § 1983.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b200-8">
   The complaint states:
  </p>
<blockquote id="b200-9">
   “Pursuant to the provisions of <span class="citation no-link">42 U. S. C. Sec. 1988</span>, the Commonwealth of Kentucky, d/b/a Bureau of State Police is liable for the payment of reasonable attorney fees incurred in this action.” Complaint ¶ 4(D).
  </blockquote>
<p id="AxJ">
   According to respondents, “[paragraph 4(D). . . states the sole basis for including the Commonwealth as a named party.” Brief for Respondents 14.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b200-10">
   Five thousand dollars came from the city and $10,000 from the county. The remaining $45,000 was to be paid by Commissioner Brandenburgh, both personally and as agent for the “Kentucky State Police Legal Fund.” The latter was not a named defendant but presumably represented the interests of the individual officers sued.
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="ANn">
   Petitioner did not appeal from the award of costs and expenses, and we therefore have no occasion to consider the appropriateness of these portions of the award.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="Afr">
<em>
    Berry
   </em>
   v.
   <em>
    McLemore,
   </em>
   <span class="citation" data-id="399169"><a href="/opinion/399169/earl-berry-v-jimmy-mclemore/" aria-description="Citation for case: Earl Berry v. Jimmy McLemore">670 F. 2d 30</a></span> (CA5 1982) (municipal officials);
   <em>
    Morrison
   </em>
   v.
   <em>
    Fox,
   </em>
   <span class="citation" data-id="394861"><a href="/opinion/394861/morrison-v-fox/" aria-description="Citation for case: Morrison v. Fox">660 F. 2d 87</a></span> (CA3 1981) (same). At least one Court of Appeals appears to have reached the same result as that of the lower court in this case. See
   <em>
    Glover
   </em>
   v.
   <em>
    Alabama Department of Corrections,
   </em>
   <span class="citation" data-id="447580"><a href="/opinion/447580/willie-james-glover-v-alabama-department-of-corrections/" aria-description="Citation for case: Willie James Glover v. Alabama Department of Corrections">753 F. 2d 1569</a></span> (CA11 1985).
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b202-6">
   See 6 J. Moore, W. Taggart, &amp; J. Wicker, Moore’s Federal Practice § 54.70[1], p. 1301 (1985) (“Costs” are awarded “against the losing party and as an incident of the judgment”); 10 C. Wright, A. Miller, &amp; M. Kane, Federal Practice and Procedure §2666, p. 173 (1983) (“‘Costs’ refers to those charges that one party has incurred and is permitted to have reimbursed by his opponent as part of the judgment in the action”).
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b202-7">
   We did hold that the court and its chief justice in his official capacity could be enjoined from
   <em>
    enforcing
   </em>
   the State Bar Code and suggested that fees could be recovered from these defendants in their enforcement roles. Because the fee award had clearly been made against the defendants in their legislative roles, however, the award had to be vacated and the case remanded for further proceedings. That fees could be awarded against
   <span citation-index="1" class="star-pagination" label="165"> 
    *165
    </span>
   the Virginia Supreme Court and its chief justice pursuant to an injunction against enforcement of the Code further illustrates that fee liability is tied to liability on the merits.
  </p>
</div><div class="footnote" id="fn9" label="9">
<a class="footnote" href="#fn9_ref">
   9
  </a>
<p id="b203-11">
   The rules are somewhat different with respect to prevailing defendants. Prevailing defendants generally are entitled to costs, see Fed. Rule Civ. Proc. 54(d), but are entitled to fees only where the suit was vexatious, frivolous, or brought to harass or embarrass the defendant. See
   <em>
    Hensley
   </em>
   v.
   <em>
    Eckerhart,
   </em>
   <span class="citation" data-id="9429188"><a href="/opinion/110929/hensley-v-eckerhart/#429" aria-description="Citation for case: Hensley v. Eckerhart">461 U. S. 424, 429, n. 2</a></span> (1983).
  </p>
<p id="b203-12">
   We express no view as to the nature or degree of success necessary to make a plaintiff a prevailing party. See
   <em>
    Maher
   </em>
   v.
   <em>
    Gagne,
   </em>
   <span class="citation" data-id="9428042"><a href="/opinion/110327/maher-v-gagne/" aria-description="Citation for case: Maher v. Gagne">448 U. S. 122</a></span> (1980).
  </p>
</div><div class="footnote" id="fn10" label="10">
<a class="footnote" href="#fn10_ref">
   10
  </a>
<p id="b203-13">
   Personal-capacity actions are sometimes referred to as individual-capacity actions.
  </p>
</div><div class="footnote" id="fn11" label="11">
<a class="footnote" href="#fn11_ref">
   11
  </a>
<p id="b204-6">
   Should the offical die pending final resolution of a personal-capacity action, the plaintiff would have to pursue his action against the decedent’s estate. In an official-capacity action in federal court, death or replacement of the named official will result in automatic substitution of the official’s successor in office. See Fed. Rule Civ. Proc. 25(d)(1); Fed. Rule App. Proc. 43(c)(1); this Court’s Rule 40.3.
  </p>
</div><div class="footnote" id="fn12" label="12">
<a class="footnote" href="#fn12_ref">
   12
  </a>
<p id="b204-7">
   See
   <em>
    Monell,
   </em>
   <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 694</a></span> (“[A] local government may not be sued under § 1983 for an injury inflicted solely by its employees or agents. Instead, it is when execution of a government’s policy or custom, whether made by its lawmakers or by those whose edicts or acts may fairly be said to represent official policy, inflicts the injury that the government as an entity is responsible under § 1983”).
  </p>
</div><div class="footnote" id="fn13" label="13">
<a class="footnote" href="#fn13_ref">
   13
  </a>
<p id="b205-5">
   In addition, punitive damages are not available under § 1983 from a municipality,
   <em>
    Newport
   </em>
   v.
   <em>
    Fact Concerts, Inc.,
   </em>
   <span class="citation" data-id="9428471"><a href="/opinion/110553/city-of-newport-v-fact-concerts-inc/" aria-description="Citation for case: City of Newport v. Fact Concerts, Inc.">453 U. S. 247</a></span> (1981), but are available in a suit against an official personally, see
   <em>
    Smith
   </em>
   v.
   <em>
    Wade,
   </em>
   <span class="citation" data-id="9429159"><a href="/opinion/110915/smith-v-wade/" aria-description="Citation for case: Smith v. Wade">461 U. S. 30</a></span> (1983).
  </p>
</div><div class="footnote" id="fn14" label="14">
<a class="footnote" href="#fn14_ref">
   14
  </a>
<p id="b205-6">
   There is no longer a need to bring official-capacity actions against local government officials, for under
   <em>
    <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell, supra,</a></span>
   </em>
   local government units can be sued directly for damages and injunctive or declaratory relief. See,
   <em>
    e. g., Memphis Police Dept.
   </em>
   v.
   <em>
    Garner,
   </em>
   <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985) (decided with
   <em>
    Tennessee
   </em>
   v. Gamer) (damages action against municipality). Unless a State has waived its Eleventh Amendment immunity or Congress has overridden it, however, a State cannot be sued directly in its own name regardless of the relief sought.
   <em>
    Alabama
   </em>
   v.
   <em>
    Pugh,
   </em>
   <span class="citation" data-id="9427360"><a href="/opinion/109940/alabama-v-pugh/" aria-description="Citation for case: Alabama v. Pugh">438 U. S. 781</a></span> (1978)
   <em>
    (per curiam).
   </em>
   Thus, implementation of state policy or custom may be reached in federal court only because official-capacity actions for prospective relief are not treated as actions against the State. See
   <em>
    Ex parte Young,
   </em>
   <span class="citation" data-id="9418117"><a href="/opinion/96819/ex-parte-young/" aria-description="Citation for case: Ex Parte Young">209 U. S. 123</a></span> (1908).
  </p>
<p id="b205-7">
   In many cases, the complaint will not clearly specify whether officials are sued personally, in their official capacity, or both. “The course of proceedings” in such eases typically will indicate the nature of the liability sought to be imposed.
   <em>
    Brandon
   </em>
   v.
   <em>
    Holt,
   </em>
   <span class="citation" data-id="9429823"><a href="/opinion/111304/brandon-v-holt/#469" aria-description="Citation for case: Brandon v. Holt">469 U. S. 464, 469</a></span> (1985).
  </p>
</div><div class="footnote" id="fn15" label="15">
<a class="footnote" href="#fn15_ref">
   15
  </a>
<p id="b207-5">
   The city and county were sued directly as entities, but that aspect of the case is not before us.
  </p>
</div><div class="footnote" id="fn16" label="16">
<a class="footnote" href="#fn16_ref">
   16
  </a>
<p id="b207-6">
   See also n. 3,
   <em>
    supra.
   </em>
</p>
</div><div class="footnote" id="fn17" label="17">
<a class="footnote" href="#fn17_ref">
   17
  </a>
<p id="b207-7">
   The Court has held that § 1983 was not intended to abrogate a State’s Eleventh Amendment immunity.
   <em>
    Quern
   </em>
   v.
   <em>
    Jordan,
   </em>
   <span class="citation" data-id="9427476"><a href="/opinion/110031/quern-v-jordan/" aria-description="Citation for case: Quern v. Jordan">440 U. S. 332</a></span> (1979);
   <em>
    Edelman
   </em>
   v.
   <em>
    Jordan,
   </em>
   <span class="citation" data-id="9425645"><a href="/opinion/108990/edelman-v-jordan/" aria-description="Citation for case: Edelman v. Jordan">415 U. S. 651</a></span> (1974). Because this action comes to us as if it arose solely under § 1983, see n. 2,
   <em>
    supra,
   </em>
   we cannot conclude that federal law authorized an official-capacity action for damages against Commissioner Brandenburgh to be brought in federal court.
  </p>
<p id="b207-8">
   As to legislative waiver of immunity, petitioners assert that the Commonwealth of Kentucky has not waived its Eleventh Amendment immunity. This contention is not disputed, and we therefore accept it for purposes of this case.
  </p>
</div><div class="footnote" id="fn18" label="18">
<a class="footnote" href="#fn18_ref">
   18
  </a>
<p id="b207-9">
   In an injunctive or declaratory action grounded on federal law, the State’s immunity
   <em>
    can
   </em>
   be overcome by naming state officials as defendants. See
   <em>
    Pennhurst State School &amp; Hospital
   </em>
   v.
   <em>
    Halderman,
   </em>
   <span class="citation" data-id="9429483"><a href="/opinion/111094/pennhurst-state-school-and-hospital-v-halderman/" aria-description="Citation for case: Pennhurst State School and Hospital v. Halderman">465 U. S. 89</a></span> (1984); see also
   <em>
    Ex parte <span class="citation" data-id="9418117"><a href="/opinion/96819/ex-parte-young/" aria-description="Citation for case: Ex Parte Young">Young, supra.</a></span>
   </em>
   Monetary relief that is “ancillary” to in-junctive relief also is not barred by the Eleventh Amendment.
   <em>
    Edelman
   </em>
   v.
   <em>
    Jordan, supra,
   </em>
   at 667-668.
  </p>
</div><div class="footnote" id="fn19" label="19">
<a class="footnote" href="#fn19_ref">
   19
  </a>
<p id="AIV">
   No argument has been made that the Commonwealth waived its Eleventh Amendment immunity by failing specifically to seek dismissal of that portion of the damages action that named Commissioner Brandenburgh in his official capacity. Nor is the Commonwealth alleged to have done so by allowing him to enter the settlement agreement; the Commonwealth did not even have notice of the settlement negotiations.
  </p>
</div><div class="footnote" id="fn20" label="20">
<a class="footnote" href="#fn20_ref">
   20
  </a>
<p id="AbR">
   Brief for Respondents 17; Tr. of Oral Arg. 18.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/killian-v-united-states--106310.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8efe3089d2229f65", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "killian-v-united-states--106310"}, "payload": {"all": [{"cite": "368 U.S. 231", "page": "231", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "368"}, {"cite": "82 S. Ct. 302", "page": "302", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "82"}, {"cite": "7 L. Ed. 2d 256", "page": "256", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "7"}, {"cite": "1961 U.S. LEXIS 1931", "page": "1931", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1961"}], "display": null, "official": null, "official_selection_present": false, "record_id": "killian-v-united-states--106310"}}
{"assertion_id": "190388e3438e4334", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "killian-v-united-states--106310"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "killian-v-united-states--106310", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — killian-v-united-states--106310

```json
{
  "schema_version": "s2.v1",
  "record_id": "killian-v-united-states--106310",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Killian v. United States",
    "case_name_short": "Killian",
    "case_name_full": "Killian v. United States",
    "input_case_name": "Killian v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1962-01-22",
    "year": 1962,
    "docket": null,
    "cluster_id": 106310,
    "lead_opinion_id": 9422314,
    "sibling_ids": [],
    "absolute_url": "/opinion/106310/killian-v-united-states/",
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
        "cite": "368 U.S. 231",
        "volume": "368",
        "reporter": "U.S.",
        "page": "231",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 S. Ct. 302",
        "volume": "82",
        "reporter": "S. Ct.",
        "page": "302",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "7 L. Ed. 2d 256",
        "volume": "7",
        "reporter": "L. Ed. 2d",
        "page": "256",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1961 U.S. LEXIS 1931",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "1931",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "368 U.S. 231",
        "volume": "368",
        "reporter": "U.S.",
        "page": "231",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 S. Ct. 302",
        "volume": "82",
        "reporter": "S. Ct.",
        "page": "302",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "7 L. Ed. 2d 256",
        "volume": "7",
        "reporter": "L. Ed. 2d",
        "page": "256",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1961 U.S. LEXIS 1931",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "1931",
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
    "date_created": "2026-07-06T13:49:22Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:51:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:51:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:51:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:51:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — killian-v-united-states--106310

```
<opinion type="majority">
<author id="b322-6">Mr. Justice Whittaker</author>
<p id="AkI">delivered the opinion of the Court.</p>
<p id="b322-7">For the purpose of enabling a labor union of which he was then an officer to comply with § 9 (h) of the National Labor Relations Act, as amended, <span class="citation no-link">29 U. S. C. § 169</span> (h), and hence to use the processes of the National Labor Relations Board,<footnotemark>1</footnotemark> petitioner made on Decembér 9, and caused to be filed with the Board on December 11, 1952, an affidavit reciting, <em>inter alia, “I </em>am not a member of the Communist Party or affiliated with such Party.” Upon receipt of that affidavit and like ones of all other officers of the union, the Board advised the union that it had complied with § 9 (h) and could make use of the Board’s processes.</p>
<p id="b322-8">In November 1955, an indictment in two counts was returned against petitioner in the United States District Court for the Northern District of Illinois. The first <page-number citation-index="1" label="235">*235</page-number>count charged that, in violation of <span class="citation no-link">18 U. S. C. § 1001</span>,<footnotemark>2</footnotemark> petitioner had falsely sworn, in the affidavit, that he was not a member of the Communist Party, and the second charged that, in violation of the same statute, he had also falsely sworn in that affidavit that he was not affiliated' with the Communist Party. A jury trial was had which resulted in a verdict of guilty on both counts, and the court sentenced petitioner to imprisonment. On appeal, the United States Court of Appeals for the Seventh Circuit originally affirmed, but, before the motion for rehearing was ruled, this Court’s decision in <em>Jencks </em>v. <em>United States, </em><span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/" aria-description="Citation for case: Jencks v. United States">353 U. S. 657</a></span>, came down, and, on the authority of that case, the court granted the motion for rehearing, reversed the judgment and remanded the case for a new trial. <em>United States </em>v. <em>Killian, </em><span class="citation" data-id="9445686"><a href="/opinion/242683/the-united-states-of-america-v-john-joseph-killian/#82" aria-description="Citation for case: The United States of America v. John Joseph Killian">246 F. 2d 77, 82</a></span>. A new trial was had. It also resulted in a verdict of guilty on both counts, and petitioner was sentenced to imprisonment for five years on Count I, and for three years on Count II, the sentences to run concurrently. On appeal, the United States Court of Appeals for the Seventh Circuit affirmed, <em>United States </em>v. <em>Killian, </em><span class="citation" data-id="250299"><a href="/opinion/250299/united-states-v-john-joseph-killian/" aria-description="Citation for case: United States v. John Joseph Killian">275 F. 2d 561</a></span>, and we granted certiorari limited to two questions, namely, (1) whether production of statements submitted by Government informer witnesses for their expenses, and the receipts executed by them for the payments, is required by <span class="citation no-link">18 U. S. C. § 3500</span> when the Government offers at the trial to produce a list of the dates and .amounts of the <page-number citation-index="1" label="236">*236</page-number>payments, and (2) whether the instructions to the jury properly defined membership in and affiliation with the Communist Party. <span class="citation multiple-matches"><a href="/c/U.%20S./365/810/">365 U. S. 810</a></span>.</p>
<p id="b324-5">The Government introduced evidence tending to show that petitioner was a member and active in the affairs of the Communist Party from 1949 through August 1953, but, inasmuch as there is not before us any question concerning the sufficiency of the evidence to make a sub-missible case for the jury, it is not necessary to review the evidence in detail.</p>
<p id="b324-6">I. The Document Production Questions.</p>
<p id="b324-7">Intelligent understanding of the document production questions presented requires a brief statement of their basis. They arose in connection with the testimony of Government witnesses Sullivan and Ondrejka.</p>
<p id="b324-8">On direct examination, Sullivan testified that he joined the Communist Party in 1948 at the request of the Federal Bureau of Investigation, and in October 1949 transferred his membership from Cincinnati, Ohio, to Madison, Wisconsin, where, by secret means, he made contact with local leaders of the Communist Party and became active in its affairs. In those activities, he met petitioner in December 1949. Petitioner was then the section organizer for the Party in Madison. Thereafter, Sullivan attended a number of secret Communist Party group meetings in Madison in 1949 and 1950 at which petitioner was present and acted as the spokesman and leader. Sullivan testified that he gave written reports to the F. B. I. respecting Party meetings and activities soon after they occurred.</p>
<p id="b324-9">At the close of Sullivan’s direct testimony, petitioner moved for production, for use in cross-examination, of all statements given by the witness to the F. B. I. relating to his direct testimony. The narrative statements were produced to the judge, <em>in camera, </em>who, after excising the <page-number citation-index="1" label="237">*237</page-number>parts that did not relate to the witness' direct testimony, handed them to petitioner’s counsel. On cross-examination, Sullivan testified that he was paid stipulated monthly amounts for his services, and was reimbursed for his expenses incurred in Communist Party activities, by the F. B. I., and that when he received the money he signed a receipt for it. His connection with the F. B. I. terminated in 1952.</p>
<p id="b325-5">After completing the cross-examination of the witness, petitioner again moved for production of all statements made by the witness to the F. B. I., without excision. The Government objected to the motion on the grounds that it had produced all of the witness’ statements that related to his direct testimony, and that there was no showing that the witness had given any other statements to the Government that related to his direct testimony. Thereupon, the court denied petitioner’s motion. Petitioner then moved to strike the testimony of the witness, and that motion, too, was denied.</p>
<p id="b325-6">On direct examination, Ondrejka testified that he joined the Communist Party at the request of the F. B. I. in October 1949 and remained a member of the Party until November 1953. He met petitioner at a Communist Party meeting in Milwaukee, Wisconsin, in January 1951, and thereafter attended many secret Communist Party meetings in Milwaukee where petitioner was present and active, and alsi &gt; participated with petitioner in numerous Party activities, until August 1953, and knew petitioner to be a member of the Communist Party throughout that period. Ondrejka testified that he gave written reports to the F. B. I. respecting Party meetings and activities soon after they occurred.</p>
<p id="b325-7">At the conclusion of Ondrejka’s direct testimony, petitioner moved for production, for use in cross-examination, of all statements given by the witness to the F. B. I. The court ordered the Government to produce to the judge, <page-number citation-index="1" label="238">*238</page-number><em>in camera, </em>“all statements that in any way affect the direct examination of the witness.” Accordingly, all of the narrative statements given by the witness to the Government relating to his direct testimony were produced to the judge, who, after excising such parts as did not relate to the witness’ direct testimony, delivered them to petitioner’s counsel. Petitioner then moved for production of all statements relating to the testimony of the witness, without excision. That motion was denied.</p>
<p id="b326-6">On cross-examination, Ondrejka testified that he was paid stipulated monthly amounts in cash for his services by the F. B. I., and, in addition, was reimbursed by the F. B. I. for his expenses, such as Communist Party dues, literature, contributions and travel, which he orally reported to an F. B. I. agent, who made notes thereof and later reimbursed him in cash. The court sustained the Government’s objection to a question asking whether Ondrejka signed receipts for the moneys paid to him in reimbursement for his expenses.</p>
<p id="b326-7">Petitioner then moved for production of all statements given by the witness to the F. B. I., whether written by the witness or by an F. B. I. agent as the result of interviews with the witness, which related to the witness’ testimony on cross-examination, including particularly reports by the witness of his reimbursable expenses and the receipts which he signed evidencing reimbursement for those expenses. The Government opposed production of the documents on the ground that they did not relate to the direct testimony of the witness. It further objected to producing Ondrejka’s reports of expenses, and the receipts he had signed when reimbursed for those expenses, on the grounds that they were administrative records of the F. B. I. and were immaterial and irrelevant, but the Government offered to produce a list showing the dates and amounts of the payments and whether they were for services or expenses. Petitioner refused to <page-number citation-index="1" label="239">*239</page-number>receive that proffered list. Thereupon, the court denied the motion. Petitioner then moved to strike all of Ondrejka’s testimony, and that motion, too, was denied.</p>
<p id="b327-5">Petitioner contends that his general demands for “all statements,” as well as his specific demand for the reports and receipts made by Ondrejka, encompassed, and the trial court erred to his prejudice in denying his motion to require the Government to produce, (1) the notes made by the F. B. I. agents covering Ondrejka’s oral reports of expenses and (2) the receipts signed by Sullivan and Ondrejka for moneys paid to them in reimbursement for expenses. He supports these contentions with an elaborate argument which we need not delineate because the Solicitor General now concedes that the F. B. I. notes of Ondrejka’s oral reports may have been “statements” within the meaning of <span class="citation no-link">18 U. S. C. §3500</span> (e)(2),<footnotemark>3</footnotemark> and he flatly concedes that the receipts signed by Sullivan and Ondrejka were “statements” within the meaning of § 3500.</p>
<p id="b327-6">However, the Solicitor General contends that on the actual facts — many of which are not incorporated in the record before us — petitioner is not entitled to, and that we should not on this incomplete and imperfect record order, a new trial, because the true facts are that the F. B. I. agents’ notes covering Ondrejka’s oral reports of expenses were not in existence at the time of the trial, and the receipts signed by Sullivan and Ondrejka do not “relate to” their direct testimony as required by § 3500, or, if it may be said that any of them do “relate to” their direct testimony, that the same information, in much <page-number citation-index="1" label="240">*240</page-number>greater detail, was given to petitioner in the witnesses’ narrative statements that were produced and delivered to his counsel at the trial, and hence if there was any error it was harmless.</p>
<p id="b328-5">More specifically, the Solicitor General tells us in his brief that, although the nature of the Government’s objections in the courts below implied that the agents’ notes were in existence, his interrogation of the F. B. I. agents has disclosed that, after they incorporated the data contained in their notes of Ondrejka’s oral reports into the receipts to be signed by him, the agents destroyed the notes in accord with their normal practice, and hence those notes were not in existence at the time of either of petitioner’s trials. Although the receipts are not contained in the record before us, the Solicitor General says that there are 124 of them and that a careful examination of them reveals that none of Sullivan’s receipts contains any itemization whatever of the nature of the reimbursed expenses, and thus they do not "relate to” anything mentioned in his direct testimony. With respect to Ondrejka’s receipts, the Solicitor General says that, although the Government inadvertently represented to the District Court and the Court of Appeals that the list, proffered to petitioner at the trial and showing the dates and amounts of payments made to Ondrejka, gave all of the information that was contained in the receipts, his examination has disclosed that nine of Ondrejka’s receipts do contain some itemization of the nature of his reimbursed expenses, but that only two of the nine can be said to “relate to” anything mentioned by Ondrejka on his direct examination, and that the same information, in greater detail, was contained in Ondrejka’s narrative statements that were produced and delivered to petitioner’s counsel at the trial. .</p>
<p id="b328-6">For these reasons, the Solicitor General contends that, viewed upon the now known and readily available actual <page-number citation-index="1" label="241">*241</page-number>facts, no error, at least no prejudicial error, resulted from the nonproduction of the F. B. I. notes and the Sullivan and Ondrejka receipts at the trial. However, the Solicitor General recognizes that petitioner is not bound to accept his statement that the F. B. I. notes of Ondrejka’s oral reports of expenses were destroyed in accord with normal practice long prior to the trial, and that petitioner is entitled to an opportunity to examine the F. B. I. agents and other responsible Government officials on these matters which, of course, can be done only in the District Court. He recognizes, too, that his contentions with respect to the receipts signed by Sullivan and Ondrejka necessarily involve a detailed examination and comparison of the lengthy direct testimony of Sullivan and Ondrejka, the 124 receipts, the list showing the dates and amounts of payments to Ondrejka that was proffered to petitioner by the Government at the trial, and the numerous narrative statements by Sullivan and Ondrejka that were produced and delivered to petitioner at the trial, and he submits that this cannot appropriately be done in this Court, especially since neither the receipts nor the proffered list is contained in the present record, but can properly be done only in the District Court. He therefore asks us to vacate the judgment and remand the case to the District Court to hear these issues and to determine whether a new trial should be ordered or the judgment should be reinstated with the right in the petitioner, of course, to appeal from any such judgment to the Court of Appeals.</p>
<p id="b329-5">In opposition, petitioner argues that the claimed destruction of the agents’ notes admits the destruction of evidence that may have been helpful to him and deprives him of his rights under § 3500 and to due process of law, and therefore the judgment should be reversed. Alternatively, he argues that only he and his counsel could determine the uses that might have been made of <page-number citation-index="1" label="242">*242</page-number>the receipts had they been produced, and he concludes that it would not be possible for the District Court, on remand, to find that the failure to produce the receipts was nonprejudicial or harmless error, and that therefore he is entitled to a new trial.</p>
<p id="b330-6">As to petitioner’s contention that the claimed destruction of the agents’ notes admits the destruction of evidence, deprives him of legal rights and requires reversal of the judgment, it seems appropriate to observe that almost everything is evidence of something, but that does not mean that nothing can ever safely be destroyed. If the agents’ notes of Ondrejka's oral reports of expenses were made only for the purpose of transferring the data thereon to the receipts to be signed by Ondrejka, and if, after having served that purpose, they were destroyed by the agents in good faith and in accord with their normal practice, it would be clear that their destruction did not constitute an impermissible destruction of evidence nor deprive petitioner of any right. Those are the factual representations made by the Solicitor General. Whether they are true can be determined only upon a hearing in the District Court.</p>
<p id="b330-7">It is entirely clear that petitioner would not be entitled to a new trial because of the nonproduction of the agents’ notes if those notes were so destroyed and not in existence at the time of the trial. It is equally clear that, notwithstanding the fact that the Sullivan and Ondrejka receipts were “statements” within the meaning of § 3500 and were demanded under that section, petitioner would not be entitled to a new trial because of the nonproduction of those receipts if in truth they do not relate to the direct testimony of those witnesses inasmuch as § 3500 (c) requires “the court [to] excise the portions of [the] statement which do not relate to the subject matter of the testimony of the witness.” The Solicitor General represents that 115 of the 124 receipts signed by Sullivan and <page-number citation-index="1" label="243">*243</page-number>Ondrejka do not contain any itemization of the nature of the reimbursed expenses nor relate to the direct testimony of those witnesses. If those representations are true, petitioner would not be entitled to a new trial because of the nonproduction of those 115 receipts. Inasmuch as the receipts are not contained in the record before us, whether the Solicitor General’s representations are true can be determined only upon a hearing in the District Court.</p>
<p id="b331-5">But the Solicitor General finds that two of Ondrejka’s receipts may be said to relate to Ondrejka’s direct testimony. However, he says that the same information as they contain and much more on the same subjects was contained in Ondrejka’s narrative statements that were produced and delivered to petitioner at the trial, and therefore petitioner could not have been prejudiced by the nonproduction of those two receipts and is not entitled to a new trial on that account. It is true, as petitioner argues, that only the defense is in position to determine the precise uses that may be made of demanded documents, <em>Jencks </em>v. <em>United States, </em><span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/#668" aria-description="Citation for case: Jencks v. United States">353 U. S. 657, 668</a></span>, but that is not to say that the harmless error rule is never applicable in respect to the nonproduction of demanded documents. Upon very similar facts, we recently approved a holding that nonproduction of demanded documents was harmless error. <em>Rosenberg </em>v. <em>United States, </em><span class="citation" data-id="9421847"><a href="/opinion/105921/rosenberg-v-united-states/" aria-description="Citation for case: Rosenberg v. United States">360 U. S. 367</a></span>. We there said: “Since the same information that would have been afforded had the document been given to defendant was already in the possession of the defense by way of the witness’ admissions while testifying, it would deny reason to entertain the belief that defendant could have been prejudiced by not having had opportunity to inspect the letter.” <span class="citation" data-id="9421847"><a href="/opinion/105921/rosenberg-v-united-states/#371" aria-description="Citation for case: Rosenberg v. United States">360 U. S., at 371</a></span>.</p>
<p id="b331-6">While, as we said in the <em><span class="citation" data-id="9421847"><a href="/opinion/105921/rosenberg-v-united-states/" aria-description="Citation for case: Rosenberg v. United States">Rosenberg</a></span> </em>case, <em>supra, </em>a “court should not confidently guess what defendant’s attorney <page-number citation-index="1" label="244">*244</page-number>might have found useful for impeachment purposes in withheld documents to which the defense is entitled . . . , when the very same information was possessed by defendant’s counsel as would have been available were error not committed [a court properly can find that] it would offend common sense and the fair administration of justice to order a new trial.” <span class="citation" data-id="9421847"><a href="/opinion/105921/rosenberg-v-united-states/#371" aria-description="Citation for case: Rosenberg v. United States">360 U. S., at 371</a></span>.</p>
<p id="b332-6">If it is true, as the Solicitor General represents, that the information contained on the two Ondrejka receipts had already been given to petitioner in Ondrejka’s narrative statements covering the same subjects, it is clear that the District Court properly could find that the error in failing to produce those two receipts was harmless.</p>
<p id="b332-7">Accordingly, we vacate the judgment and remand the cause to the District Court for a hearing confined to the issues raised by the Solicitor General’s representations as stated in this opinion. The District Court shall make findings of fact on those issues. If the District Court finds that the Solicitor General’s representations are true in all material respects, it shall enter a new final judgment based upon the record as supplemented by its findings, thereby preserving to petitioner the right to appeal to the Court of Appeals. If, on the other hand, the District Court finds that the Solicitor General’s representations are untrue in any material respect, it shall grant petitioner a new trial.</p>
<p id="b332-8">II. The Instructions to the Jury.</p>
<p id="b332-9">Whether the District Court, on remand, grants or denies a new trial, it is obvious that petitioner’s contentions respecting the court’s instructions to the jury will not be mooted<footnotemark>4</footnotemark> and it seems necessary to decide them.</p>
<p id="b333-4"><page-number citation-index="1" label="245">*245</page-number>Because of the nature of some of petitioner’s contentions respecting the instructions, it seems appropriate to make clear just what was the charge upon which petitioner was convicted. He was not charged with criminality for being a member of or affiliated with the Communist Party, nor for participation in any criminal activities of or for the Communist Party. He was not charged with advocating or teaching the overthrow of the Government as was the case in <em>Yates </em>v. <em>United States, </em><span class="citation" data-id="9421479"><a href="/opinion/105537/yates-v-united-states/" aria-description="Citation for case: Yates v. United States">354 U. S. 298</a></span>, or with knowing membership in an organization advocating the overthrow of the Government by force and violence as in <em>Scales </em>v. <em>United States, </em><span class="citation" data-id="9422242"><a href="/opinion/106268/scales-v-united-states/" aria-description="Citation for case: Scales v. United States">367 U. S. 203</a></span>, and <em>Noto </em>v. <em>United States, </em><span class="citation" data-id="9422246"><a href="/opinion/106269/noto-v-united-states/" aria-description="Citation for case: Noto v. United States">367 U. S. 290</a></span>. The charge was that, to enable a labor union of which he was an officer to comply with § 9 (h) of the National Labor Relations Act and thus be permitted to use the processes of the Labor' Board, petitioner, on December 11, 1952, knowingly made and caused to be transmitted to the Labor Board a false affidavit, saying he was not then a member of or affiliated with the Communist Party when in fact he was both a member of and affiliated with the Communist Party, and that those acts were made criminal and punishable by <span class="citation no-link">18 U. S. C. § 1001</span>.</p>
<p id="b333-5">Nothing in § 9 (h) or elsewhere in the National Labor Relations Act makes or purports to make criminal either membership in or affiliation with the Communist Party, <em>American Communications Assn. </em>v. <em>Douds, </em><span class="citation" data-id="9420478"><a href="/opinion/104790/american-communications-assn-v-douds/#402" aria-description="Citation for case: American Communications Assn. v. Douds">339 U. S. 382, 402</a></span>, but § 1001 provides that “Whoever, in any matter within the jurisdiction of any department or <page-number citation-index="1" label="246">*246</page-number>agency of the United States knowingly and willfully falsifies ... a material fact ... or makes or uses any false writing or document knowing the same to contain any false . . . statement . . . shall be fined not more than $10,000 or imprisoned not more than five years, or both.” Petitioner was charged with and convicted for violating that statute — of knowingly making and transmitting to the Labor Board on December 11, 1952, an affidavit falsely swearing that he was not a member of or affiliated with the Communist Party — not for being a member of or affiliated with the Communist Party, nor for participating in any activities, lawful or unlawful, of the Communist Party, although, of course, determination of whether the affidavit was true or false requires a determination of whether petitioner was a member of or affiliated with the Communist Party on December 11, 1952. Neither is there any question here about the fact that the evidence was sufficient to make a submissible case for the jury and to support its verdict — notwithstanding petitioner’s tangential implications to the contrary. The questions here are simply whether the court’s instructions to the jury properly defined <em>membership </em>in and <em>affiliation </em>with the Communist Party.</p>
<p id="b334-6"><em>Membership. </em>Petitioner first contends that the instruction respecting membership<footnotemark>5</footnotemark> should have defined “mem<page-number citation-index="1" label="247">*247</page-number>bership” as, and required a finding of, “a definite objective factual phenomenon” or a “specific formal act of joining” rather than, as was done, in the subjective terms of a state of mind. If petitioner is right in this contention it would follow, despite the fact the question is foreclosed against him here, that the evidence did not make a submissible case for the jury on Count I of the indictment and his motion for a directed verdict of acquittal on that count should have been granted, for there was no evidence of “a definite objective factual phenomenon [of joining]” or of “a specific formal act of joining.” Indeed, the very nature of the case — claimed membership in an underground or secretly operating organization whose member<page-number citation-index="1" label="248">*248</page-number>ship records, if any, are not available to the Government— precludes the possibility of such evidence, and, if the rule were as petitioner contends, false affidavits of non-Communist Party membership could be made and sub<page-number citation-index="1" label="249">*249</page-number>mitted to the Labor Board with impunity. Membership in such a secretly operating organization is, to all but the organization and its member or members, necessarily subjective, and, although it must be proved by evidence of objective facts and circumstances having a rational tendency to show, and from which the jury may rationally and logically infer, the ultimate subjective fact of membership, it is, in the very nature of such a case, necessary that the court's instructions define membership in such an organization in subjective terms or not at all.</p>
<p id="b337-5">A similar question arising under § 9 (h) was presented in <em>Jencks </em>v. <em>United </em>States, <span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/" aria-description="Citation for case: Jencks v. United States">353 U. S. 657</a></span>, but the Court’s opinion, turning on the document production question, did not reach it. However, Mr. Justice Burton’s separate concurring opinion, joined by Mr. Justice Harlan, <span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/#672" aria-description="Citation for case: Jencks v. United States">353 U. S., at 672</a></span>, and, on the question here considered, also by Mr. Justice Frankfurter, <span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/#672" aria-description="Citation for case: Jencks v. United States">353 U. S., at 672</a></span>, did reach the question. It found the membership defining instruction given in that case to be deficient because it “failed to emphasize to the jury the essential element of membership in an organized group — the desire of an individual to belong to the organization and a recognition by the organization that it considers him as a member.” <page-number citation-index="1" label="250">*250</page-number><span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/#679" aria-description="Citation for case: Jencks v. United States">353 U. S., at 679</a></span>. In the instant case, the District Court’s instruction to the jury defined membership to the jury in almost precisely that language (see note 5, sixth paragraph) . Similar instructions in cases arising under § 9(h) have been held proper by every United States Court of Appeals that has passed upon the question. <em>Fisher </em>v. <em>United States, </em><span class="citation" data-id="238900"><a href="/opinion/238900/avalo-allison-fisher-v-united-states/#107" aria-description="Citation for case: Avalo Allison Fisher v. United States">231 F. 2d 99, 107</a></span> (C. A. 9th Cir.);<footnotemark>6</footnotemark> <em>Lohman </em>v. <em>United States, </em><span class="citation" data-id="244159"><a href="/opinion/244159/walter-c-lohman-jr-v-united-states/#954" aria-description="Citation for case: Walter C. Lohman, Jr. v. United States">251 F. 2d 951, 954</a></span> (C. A. 6th Cir.);<footnotemark>7</footnotemark> <em>Lohman </em>v. <em>United States, </em><span class="citation" data-id="247868"><a href="/opinion/247868/walter-c-lohman-jr-v-united-states/" aria-description="Citation for case: Walter C. Lohman, Jr. v. United States">266 F. 2d 3</a></span> (C. A. 6th Cir.); <footnotemark>8</footnotemark> <em>Travis </em>v. <em>United States, </em><span class="citation" data-id="9446962"><a href="/opinion/248843/maurice-e-travis-v-united-states/#942" aria-description="Citation for case: Maurice E. Travis v. United States">269 F. 2d 928, 942-943</a></span> (C. A. 10th Cir.).<footnotemark>9</footnotemark> From these consistent holdings and <page-number citation-index="1" label="251">*251</page-number>upon principle, it seems clear that the instruction’s definition of. membership was not erroneous under Count I of the indictment.</p>
<p id="b339-5">Petitioner next contends that the court’s instruction failed to tell the jury precisely what objective circumstances would be sufficient to justify a finding of membership, and that the criteria which it told the jury they might consider in determining the question of membership were too indefinite to give the jury the necessary guidance. Although the ultimate fact of membership in such a case is almost necessarily a subjective one, it may be proved, as we have said, by objective facts and circumstances having a rational tendency to show, and from which the jury rationally and logically may find, the ultimate fact of membership. But, for the purpose of confining the jury’s considerations to the relevant evidence, it was proper for the court to outline the objective acts, shown in the evidence, which they might consider in determining the ultimate subjective fact of membership. Here, the court’s instruction, after telling the jury that intent is a state of mind and can only be determined by what an individual says and does, went on to say that in determining the issue as to whether the defendant was or was not a member of the Communist Party at the time alleged in the indictment the jury might take into consideration, as circumstances bearing on that question, the acts and statements of the defendant (see note 5, sixth paragraph), and in this connection they might take into consideration whether the defendant did the things set forth in the 12 numbered paragraphs that followed, which, <page-number citation-index="1" label="252">*252</page-number>it said, were some of the indicia of Communist Party membership (see note 5, eighth paragraph).</p>
<p id="b340-5">While the criteria specified in the numbered paragraphs of the challenged instruction were in substance 12 of the 14 criteria specified by Congress in § 5 of the Communist Control Act of 1954 (<span class="citation no-link">50 U. S. C. § 844</span>) to be considered by a jury in determining Communist Party membership under that Act, it is unnecessary for us to determine in this case whether that section applies, by force of law, to prosecutions under <span class="citation no-link">18 U. S. C. § 1001</span> for making a false affidavit to the Labor Board in purported compliance with § 9 (h) of the National Labor Relations Act, for it is obvious that those 12 criteria rationally tend to show, and were sufficient to enable a jury rationally and logically to find, the ultimate fact of membership, though subjective, and hence it was proper, independently of and wholly apart from § 5 of the Communist Control Act of 1954, to tell the jury, as this instruction did, that they might consider those criteria in determining whether the defendant was or was not a member of the Communist Party on the date charged in the indictment.</p>
<p id="b340-6">Similar criteria were contained in the membership instruction given in the <em><span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/" aria-description="Citation for case: Jencks v. United States">Jencks</a></span> </em>case, <em>supra,</em><footnotemark><em>10</em></footnotemark><em> </em>and the opinion of Mr. Justice Burton did not find any error in that aspect of the instruction. Very similar instructions telling the jury that they might consider such or similar criteria in determining the ultimate subjective fact of membership within the meaning of § 9 (h) have been consistently and uniformly approved, <em>Hupman </em>v. <em>United States, </em><span class="citation" data-id="235762"><a href="/opinion/235762/everest-melvin-hupman-also-known-as-melvin-e-hupman-v-united-states/" aria-description="Citation for case: Everest Melvin Hupman, Also Known as Melvin E. Hupman v....">219 F. 2d 243</a></span> (C. A. 6th Cir.);<footnotemark>11</footnotemark> <em>Fisher </em>v. <em>United States, </em><span class="citation" data-id="238900"><a href="/opinion/238900/avalo-allison-fisher-v-united-states/#107" aria-description="Citation for case: Avalo Allison Fisher v. United States">231 F. <page-number citation-index="1" label="253">*253</page-number>2d 99, 107</a></span> (C. A. 9th Cir.).<footnotemark>12</footnotemark> In <em>Travis </em>v. <em>United States, </em><span class="citation" data-id="9445762"><a href="/opinion/242924/maurice-e-travis-v-united-states/#135" aria-description="Citation for case: Maurice E. Travis v. United States">247 F. 2d 130, 135</a></span>, the United States Court of Appeals for the Tenth Circuit reversed because the membership instruction failed to specify and require the jury to consider such criteria in determining the question of membership. On retrial, the jury was instructed to consider virtually the same criteria of membership as was the jury in the instant case. The defendants were again convicted, and, on appeal, the Court of Appeals specifically approved the instruction. <em>Travis </em>v. <em>United States, </em><span class="citation" data-id="9446962"><a href="/opinion/248843/maurice-e-travis-v-united-states/#942" aria-description="Citation for case: Maurice E. Travis v. United States">269 F. 2d 928, 942-943</a></span>.</p>
<p id="b341-5">We think there is no merit in petitioner’s contention that the instruction failed adequately to state the objective circumstances that might be considered by the jury in determining membership or that the criteria submitted were too indefinite to give the jury the necessary guidance.</p>
<p id="b341-6">Nor is there any merit in petitioner’s contention that those criteria allowed a finding of membership on a date other than that charged in the indictment. That contention fails to consider the whole charge, particularly the vital fact that the court repeatedly emphasized to the jury that the issue for them to determine was whether petitioner was or was not a member of the Communist Party on the date that he executed and transmitted the affidavit.</p>
<p id="b341-7">Petitioner, and the <em>amici curiae, </em>contend that § 5 of the Communist Control Act of 1954 (<span class="citation no-link">50 U. S. C. § 844</span>) is constitutionally invalid in that it violates the First Amendment of the Constitution and denies due process because it permits a jury to base its finding of membership upon statements and acts that are protected by the First Amendment. They then argue that because the chal<page-number citation-index="1" label="254">*254</page-number>lenged instruction substantially adopted 12 of the 14 criteria mentioned in that section this instruction, too, was violative of the First Amendment and denied due process. We have no occasion here to consider the constitutionality of § 5 of the Communist Control Act of 1954 because, as we have said, the indicia which the challenged instruction told the jury to consider as circumstances bearing upon the issue of membership did rationally tend to show, and were sufficient, if believed, to enable the jury rationally and logically to find, the ultimate subjective fact of membership, wholly apart from' and independently of § 5 of the Communist Control Act of 1954. To petitioner’s argument that the submitted criteria permitted the jury to find membership from statements and acts that were wholly innocent in themselves or even protected by the First Amendment, it is enough to recall that nothing in § 9 (h) or elsewhere in the National Labor Relations Act makes or purports to make criminal either membership in or affiliation with the Communist Party, <em>American Communications Assn. </em>v. <em><span class="citation" data-id="9420478"><a href="/opinion/104790/american-communications-assn-v-douds/" aria-description="Citation for case: American Communications Assn. v. Douds">Douds, supra,</a></span> </em><span class="citation" data-id="9420478"><a href="/opinion/104790/american-communications-assn-v-douds/#402" aria-description="Citation for case: American Communications Assn. v. Douds">339 U. S., at 402</a></span>, and that petitioner was not charged with criminality for being a member of or affiliated with the Communist Party, nor with participating in any criminal activities of or for the Communist Party, but only with having made and submitted to the Government an affidavit falsely swearing that he was not a member of or affiliated with the Communist Party in violation of <span class="citation no-link">18 U. S. C. § 1001</span>. It would be strange doctrine, indeed, to say that membership in the Communist Party — when, as here, a lawful status — cannot be proved by evidence of lawful acts and statements, but only by evidence of unlawful acts and statements.</p>
<p id="b342-5"><em>Affiliation. </em>We think the court’s instruction defining affiliation<footnotemark>13</footnotemark> was correct under Count II of the indictment <page-number citation-index="1" label="255">*255</page-number>and in accord with all the precedents. A far less complete and definitive instruction on affiliation was given by the trial court in <em>Jencks </em>v. <em>United States, supra, </em>and was challenged in this Court. That instruction merely quoted dictionary definitions and then stated that “[a]filiation . . . means something less than membership but more than sympathy. Affiliation with the Communist Party may be proved by either circumstantial or direct evidence, or both.” See <span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/#679" aria-description="Citation for case: Jencks v. United States">353 U. S., at 679</a></span>. The Court’s opinion, turning on the document production problem, did not reach that question. However the opinion of Mr. Justice Burton did reach the question. It did not find the instruction erroneous insofar as it went, but found it to be deficient because “It did not require a continuing course of conduct ‘on a fairly permanent basis’ ‘that could not be abruptly ended without giving at least reasonable cause for the charge of a breach of good faith,’ ” and thus “allowed the jury to convict petitioner on the basis of <page-number citation-index="1" label="256">*256</page-number>acts of intermittent cooperation.” <span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/#679" aria-description="Citation for case: Jencks v. United States">353 U. S., at 679-680</a></span>. The instruction given in this case contained not only the definition given in the <em><span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/" aria-description="Citation for case: Jencks v. United States">Jencks</a></span> </em>case (see note 13, paragraph one) but went on to embody almost exactly the expanded definition prescribed by Mr. Justice Burton (see note 13, paragraph two). The opinions of the Courts of Appeals have uniformly approved that definition. In <em>Bryson </em>v. <em>United States, </em><span class="citation" data-id="240757"><a href="/opinion/240757/hugh-bryson-v-united-states/#664" aria-description="Citation for case: Hugh Bryson v. United States">238 F. 2d 657, 664</a></span>, the United States Court of Appeals for the Ninth Circuit found an identical instruction to be “full and complete” and said that it “adequately informed the jury of the meaning of the term [affiliated with] and provided an adequate standard for evaluating the evidence.” In <em>Lohman </em>v. <em>United States, </em><span class="citation" data-id="244159"><a href="/opinion/244159/walter-c-lohman-jr-v-united-states/#954" aria-description="Citation for case: Walter C. Lohman, Jr. v. United States">251 F. 2d 951, 954</a></span>, the United States Court of Appeals for the Sixth Circuit, speaking through Judge, now Mr. Justice, Stewart, specifically approved the definition of “affiliated with” prescribed by Mr. Justice Burton’s opinion in the <em><span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/" aria-description="Citation for case: Jencks v. United States">Jencks</a></span> </em>case; and in <em>Travis </em>v. <em>United States, </em><span class="citation" data-id="9445762"><a href="/opinion/242924/maurice-e-travis-v-united-states/#135" aria-description="Citation for case: Maurice E. Travis v. United States">247 F. 2d 130, 135</a></span>, the United States Court of Appeals for the Tenth Circuit approved an almost identical instruction.<footnotemark>14</footnotemark></p>
<p id="b344-5">Petitioner contends that one may not be “affiliated with” the Communist Party, within the meaning of §9 (h), by any direct relationship with the Party, but only by being a member of another organization that is affiliated with the Party, and that the instruction was erroneous for failure so to advise the jury. If petitioner is right in this contention it would follow, despite the fact the question is foreclosed against him here, that the evidence did not make a submissible case for the jury on Count II of the indictment and his motion for a directed verdict of acquittal on that count should have been granted, for there was no evidence that petitioner was <page-number citation-index="1" label="257">*257</page-number>affiliated with the Communist Party through membership in some other organization. It is true that one may be “affiliated with” the Communist Party through membership in an organization that is affiliated with the Communist Party, <em>American Communications Assn. </em>v. <em><span class="citation" data-id="9420478"><a href="/opinion/104790/american-communications-assn-v-douds/" aria-description="Citation for case: American Communications Assn. v. Douds">Douds, supra,</a></span> </em><span class="citation" data-id="9420478"><a href="/opinion/104790/american-communications-assn-v-douds/#406" aria-description="Citation for case: American Communications Assn. v. Douds">339 U. S., at 406, 421, 450</a></span>, but that is not to say one may not do so directly, and every decision that has considered the meaning of “affiliated with,” as used in § 9 (h), has held that one may be directly affiliated with the Communist Party. See Mr. Justice Burton's separate concurring opinion in <em>Jencks </em>v. <em>United States, supra, </em><span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/#672" aria-description="Citation for case: Jencks v. United States">353 U. S., at 672, 679</a></span>; and <em>Bryson </em>v. <em>United States, supra, </em><span class="citation" data-id="240757"><a href="/opinion/240757/hugh-bryson-v-united-states/#664" aria-description="Citation for case: Hugh Bryson v. United States">238 F. 2d, at 664</a></span>; <em>Lohman </em>v. <em>United States, supra, </em><span class="citation" data-id="244159"><a href="/opinion/244159/walter-c-lohman-jr-v-united-states/#954" aria-description="Citation for case: Walter C. Lohman, Jr. v. United States">251 F. 2d, at 954</a></span>; <em>Travis </em>v. <em>United States, supra, </em><span class="citation" data-id="9446962"><a href="/opinion/248843/maurice-e-travis-v-united-states/#942" aria-description="Citation for case: Maurice E. Travis v. United States">269 F. 2d, at 942</a></span>.</p>
<p id="b345-5">In a manner similar to his attack upon the court’s instruction defining membership, petitioner contends that the instruction in question erroneously defined the phrase “affiliated with” only in subjective terms and without objective criteria. However, just as with regard to membership, affiliation, in relation to Count II in this case, is necessarily subjective. But the ultimate fact of affiliation, though subjective, may be proved by evidence of objective facts and circumstances having a rational tendency to show, and from which the jury may rationally and logically find, the ultimate fact of affiliation. It cannot be disputed here that there was such evidence at the trial. The court’s instruction told the jury that “[wjhether or not the defendant was affiliated with the Communist party ... is a question of fact which you are to determine from all the evidence in the case,” and that their determination should be based on the “statements made or acts done by the accused, and all other facts and circumstances in evidence . . . .” We think that instruction was adequate.</p>
<p id="b345-6">Petitioner argues that because the first paragraph of the instruction stated that affiliation “means a relation<page-number citation-index="1" label="258">*258</page-number>ship short of and less than membership in the Communist Party, but more than that of mere sympathy for the aims and objectives of the Communist Party,” and the third paragraph of the instruction stated that “affiliation . . . means a relationship which is equivalent or equal to that of membership in all but name,” it was contradictory and confusing. We agree that the third paragraph appears inconsistent with the first. However, it is evident that the erroneous third paragraph could not have prejudiced petitioner for it, though inconsistent with the correct first paragraph, exacted a higher standard of proof of affiliation than the law required.</p>
<p id="b346-6">Petitioner, quite understandably, would require instructions as specific as mathematical formulas. But such specificity often is impossible. The phrases “member of” and “affiliated with,” especially when applied to the relationship between persons and organizations that conceal their connection, cannot be defined in absolute terms. The most that is possible, and hence all that can be expected, is that the trial court shall give the jury a fair statement of the <em>issues </em>— i. <em>e., </em>whether petitioner was a member of or affiliated with the Communist Party on the date of his affidavit — give a reasonable definition of the terms and outline the various criteria, shown in the evidence, which the jury may consider in determining the ultimate issues. We believe thát the instructions in this case, which are consistent with all the judicial precedents under § 9 (h), adequately met those tests.</p>
<p id="b346-7">Accordingly, the judgment is vacated and the case is remanded to the District Court for further proceedings consistent with this opinion.</p>
<p id="b346-8">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b322-9"> Section 9 (h), <span class="citation no-link">29 U. S. C. § 159</span> (h), provided in pertinent part that “No investigation shall be made by the Board of any question affecting commerce concerning the representation of employees, raised by a labor organization under subsection (c) of this section, and no complaint shall be issued pursuant to a charge made by a labor organization under subsection (b) of section 160 of this title, unless there is on file with the Board an affidavit executed contemporaneously or within the preceding twelve-month period by each officer of such labor organization . . . that he is not a member of the Communist Party or affiliated with such party . . . .” This section was repealed by <span class="citation no-link">Pub. L. 86-257, </span>86th Cong., 1st Sess., § 201 (d), <span class="citation no-link">73 Stat. 519</span>, 525.</p>
</footnote>
<footnote label="2">
<p id="b323-5"> <span class="citation no-link">18 U. S. C. § 1001</span> provides:</p>
<blockquote id="b323-6">“Whoever, in any matter within the jurisdiction of any department or agency of the United States knowingly and willfully falsifies, conceals or covers up by any trick, scheme, or device a material fact, or makes any false, fictitious or fraudulent statements or representations, or makes or uses any false writing or document knowing the same to contain any false, fictitious or fraudulent statement or entry, shall be fined not more than $10,000 or imprisoned not more than five years, or both.”</blockquote>
</footnote>
<footnote label="3">
<p id="b327-7"> The Solicitor General concedes that the F. B. I. notes of Ondrejka’s oral reports may have come within the meaning of “statement" as defined by <span class="citation no-link">18 U. S. C. §3500</span> (e)(2), namely, “a stenographic . . . recording . . . which is a substantially verbatim recital of an oral statement made by said witness to an agent of the Government and recorded contemporaneously with the making of such oral statement."</p>
</footnote>
<footnote label="4">
<p id="b332-10"> These instruction questions are not likely to be mooted on remand, because if a new trial is granted it is probable, since the Court of Appeals has already approved them, the District Court would give <page-number citation-index="1" label="245">*245</page-number>the same or similar instructions to the jury on the new trial, and, if petitioner should be convicted, the same question would likely be brought here again. If we then disapproved the instructions, a fourth trial would be necessary. If, on the other hand, the District Court denies a new trial and enters a new judgment, it is likely that the Court of Appeals would again approve these instructions and that the same questions would be brought here again.</p>
</footnote>
<footnote label="5">
<p id="b334-7"> The instruction respecting membership was as follows:</p>
<blockquote id="b334-8">“The crucial issue of fact in this case is whether on December 11, 1952, John Joseph Killian was or was not then a member of the Communist Party or affiliated with such Party.</blockquote>
<blockquote id="b334-9">“The affidavit does not call upon any person to state whether or not in the past he has ever been a member of the Communist Party or affiliated with it. A person who has been at some time in the past a member of the Communist Party or affiliated with that Party but who has terminated such membership or affiliation prior to the making of the affidavit would be entitled to sign the affidavit under oath without violating the law.</blockquote>
<blockquote id="b334-10">“Since the affidavit speaks in the present tense only, the fundamental issue of fact for you to decide is whether or not at the time <page-number citation-index="1" label="247">*247</page-number>alleged in the indictment the defendant knowingly and willfully used an affidavit which was false and which he knew to be false at that time.</blockquote>
<blockquote id="b335-6">“Whether or not the defendant was a member of the Communist party at the time alleged in the indictment- is a question of fact which you are to determine from all of the evidence in the case. In determining this question you must bear in mind that the burden of proof rests on the Government to prove the defendant guilty beyond a reasonable doubt. Membership or lack of membership in the Communist Party may be established by direct as well as circumstantial evidence.</blockquote>
<blockquote id="b335-7">“Membership in the Communist Party, the same as membership in any other organization, constitutes the state of being one of those persons who belong to or comprise the Communist Party. It connotes a status of mutuality between the individual and the organization. That is to say, there must be present the desire on the part of the individual to belong to the Communist Party and a recognition by that Party that it considers him as a member.</blockquote>
<blockquote id="ANB">“Intent is a state of mind and can only be determined by what an individual says and what he does. In determining the issue as to whether the defendant was or was not a member of the Communist Party at the time alleged in the indictment you may take into consideration the acts and statements of this defendant, as disclosed by the evidence, bearing in mind that individual and unrelated isolated acts of the defendant showing cooperation with the Communist Party or isolated statements of the defendant showing sympathy with the-<page-number citation-index="1" label="248">*248</page-number>Communist Party are not in themselves conclusive evidence of membership but are circumstances which you may take into consideration along with all the other evidence in this case.</blockquote>
<blockquote id="b336-5">“In determining whether or not the defendant was a member of the Communist Party at the time alleged in the indictment you may take into consideration whether the defendant:</blockquote>
<blockquote id="b336-6">“1. Paid dues or made any financial contributions to the Communist Party or collected any funds on its behalf;</blockquote>
<blockquote id="b336-7">“2. Attended Communist Party meetings, classes, conferences, or any other type of Communist Party gathering;</blockquote>
<blockquote id="b336-8">“3. Had made himself subject to the discipline of the Communist Party in any form whatsoever;</blockquote>
<blockquote id="b336-9">“4. Participated in any recruiting activities on behalf of the Communist Party;</blockquote>
<blockquote id="b336-10">“5. Has executed orders, plans or directives of any kind of the Communist Party;</blockquote>
<blockquote id="b336-11">“6. Has acted as an agent, messenger, correspondent, organizer, or in any other capacity in behalf of the Communist Party;</blockquote>
<blockquote id="b336-12">“7. Has been accepted to his knowledge as an officer or member of the Communist Party, or as one to be called upon for services by other officers or members of the Communist Party;</blockquote>
<blockquote id="b336-13">“8. Has conferred with officers or other members of the Communist Party in behalf of any plan or enterprise of the Communist Party;</blockquote>
<blockquote id="b336-14">“9. Has spoken or in any other way communicated orders, directives or plans of the Communist Party;</blockquote>
<blockquote id="b336-15">“10. Has advised, counseled, or in any other way imparted information, suggestions, or recommendations, to officers or members of the Communist Party, or to anyone else, in behalf of the Communist Party;</blockquote>
<blockquote id="b336-16">“11. Has indicated by word, action, conduct, writing, or in any other way, a willingness to carry out in any manner and to any degree the plans, objectives or designs of the Communist Party;</blockquote>
<blockquote id="b336-17">“12. Has in any other way participated in the activities, planning or actions of the Communist Party;</blockquote>
<blockquote id="b336-18">“These are some of the indicia of Communist Party membership but you are not limited solely to those I have enumerated. As sole <page-number citation-index="1" label="249">*249</page-number>arbiters of the facts, it is your duty to consider all the evidence, either direct or circumstantial, which bears upon the question of whether or not the defendant was a member of the Communist Party on the date alleged in the indictment.</blockquote>
<blockquote id="b337-7">“In determining this question, you must bear in mind that the burden of proof rests upon the Government to prove the defendant guilty beyond a reasonable doubt. If you find that the Government has sustained this burden by proving beyond a reasonable doubt that the defendant was a member of the Communist Party on December 11, 1952, as alleged in the indictment, and if you find, also, that the Government has proved beyond a reasonable doubt the other essential elements of the offense charged in the first count of the indictment, as I have outlined them to you, then you must find the defendant guilty as to the first count.”</blockquote>
</footnote>
<footnote label="6">
<p id="b338-6"> In <em>Fisher </em>v. <em>United States, supra, </em>the Court of Appeals for the Ninth Circuit said: “Membership is composed of a desire on the part of the person in question to belong to an organization and acceptance by the organization. Moreover, certain actions are usually required such as paying dues, attending meetings and doing some of the work of the group.” <span class="citation" data-id="238900"><a href="/opinion/238900/avalo-allison-fisher-v-united-states/#107" aria-description="Citation for case: Avalo Allison Fisher v. United States">231 F. 2d, at 107</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b338-12"> In <em>Lohman </em>v. <em>United States, supra, </em>the Court of Appeals for the Sixth Circuit, speaking through Judge, now Mr. Justice, Stewart, said: “Membership should be so defined as to emphasize to the jury the necessity of finding that the appellant desired to belong to the Communist Party, and that the Communist Party recognized that it considered him as a member. <em>Jencks </em>v. <em>United States, </em>353 U. S. at pages 657, 679, <span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/#1019" aria-description="Citation for case: Jencks v. United States">77 S. Ct. 1007, 1019</a></span> (concurring opinion); <em>Fisher </em>v. <em>United States, </em>9 Cir., 1956, <span class="citation" data-id="238900"><a href="/opinion/238900/avalo-allison-fisher-v-united-states/#106" aria-description="Citation for case: Avalo Allison Fisher v. United States">231 F. 2d 99, 106-107</a></span>; <em>Travis </em>v. <em>United States, </em>10 Cir., 1957, <span class="citation" data-id="9445762"><a href="/opinion/242924/maurice-e-travis-v-united-states/#135" aria-description="Citation for case: Maurice E. Travis v. United States">247 F. 2d 130, 135-136</a></span>. . . ."</p>
</footnote>
<footnote label="8">
<p id="b338-13"> On retrial of the <em>Lohman </em>case, <em>supra, </em>the trial court defined membership for the jury as directed by the Court of Appeals on the first appeal (see note 7) and the defendant was again convicted. On appeal, the Court of Appeals for the Sixth Circuit reapproved that instruction. <em>Lohman </em>v. <em>United States, </em><span class="citation" data-id="247868"><a href="/opinion/247868/walter-c-lohman-jr-v-united-states/#4" aria-description="Citation for case: Walter C. Lohman, Jr. v. United States">266 F. 2d, at 4</a></span>.</p>
</footnote>
<footnote label="9">
<p id="b338-14"> In <em>Travis </em>v. <em>United States, supra, </em>the Court of Appeals for the Tenth Circuit said of the membership instruction, precisely like the one here, that “The instructions were meaningful and clear. They included 11 of the 14 indicia of membership outlined by Congress in Section 5 of the Communist Control Act of 1954 (50 U. S. C. A. § 844) and emphasized the primary element of membership as suggested by Mr. Justice Burton in <em>Jencks </em>v. <em>United States, </em><span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/" aria-description="Citation for case: Jencks v. United States">353 U. S. 657</a></span>, <span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/#1019" aria-description="Citation for case: Jencks v. United States">77 S. Ct. 1007, 1019</a></span>, <span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/" aria-description="Citation for case: Jencks v. United States">1 L. Ed. 2d 1103</a></span>, that there must be present ‘the <page-number citation-index="1" label="251">*251</page-number>desire of an individual to belong to the organization and a recognition by the organization that it considers him as a member.’ This adequately outlined the kind of acts that could be considered evidence of membership and included the idea of the continuing reciprocal relationship necessary for that status.” <span class="citation" data-id="9446962"><a href="/opinion/248843/maurice-e-travis-v-united-states/#942" aria-description="Citation for case: Maurice E. Travis v. United States">269 F. 2d, at 942-943</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b340-7"> Compare the <em><span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/" aria-description="Citation for case: Jencks v. United States">Jencks</a></span> </em>instruction, <span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/#679" aria-description="Citation for case: Jencks v. United States">353 U. S., at 679</a></span>, with the 12 numbered paragraphs in note 5.</p>
</footnote>
<footnote label="11">
<p id="b340-8"> In <em>Hupman </em>v. <em>United States, supra, </em>the Court of Appeals for the Sixth Circuit said that a very similar instruction was “fair [and] substantially covered the crucial questions of law, with a careful analysis of the elements of the offense charged.” <span class="citation" data-id="235762"><a href="/opinion/235762/everest-melvin-hupman-also-known-as-melvin-e-hupman-v-united-states/#249" aria-description="Citation for case: Everest Melvin Hupman, Also Known as Melvin E. Hupman v....">219 F. 2d, at 249</a></span>.</p>
</footnote>
<footnote label="12">
<p id="b341-8"> In <em>Fisher </em>v. <em>United States, supra, </em>the Court of Appeals for the Ninth Circuit, in dealing with a similar question, said: “The jury should have been reminded of the components of the term membership rather than be supplied with synonyms.” <span class="citation" data-id="238900"><a href="/opinion/238900/avalo-allison-fisher-v-united-states/#107" aria-description="Citation for case: Avalo Allison Fisher v. United States">231 F. 2d, at 107</a></span>.</p>
</footnote>
<footnote label="13">
<p id="b342-6"> The instruction respecting affiliation was as follows:</p>
<blockquote id="b342-7">“The verb ‘affiliated,’ as used in the Second Count of the indictment, means a relationship short of and less than membership in the <page-number citation-index="1" label="255">*255</page-number>Communist Party, but more than that of mere sympathy for the aims and objectives of the Communist Party.</blockquote>
<blockquote id="b343-6">“A person may be found to be ‘affiliated’ with an organization, even though not a member, when there is shown to be a close working alliance or association between him and the organization, together with a mutual understanding or recognition that the organization can rely and depend upon him to cooperate with it, and to work for its benefit, for an indefinite future period upon a fairly permanent basis.</blockquote>
<blockquote id="b343-7">“Briefly stated, affiliation as charged in the Second Count of the indictment, means a relationship which is equivalent or equal to that of membership in all but name.</blockquote>
<blockquote id="b343-8">“Whether or not the defendant was affiliated with the Communist Party at the time alleged in the indictment is a question of fact which you are to determine from all the evidence in the ease. Affiliation or lack of affiliation in the Communist Party may be established by direct as well as circumstantial evidence.</blockquote>
<blockquote id="b343-9">“In determining the issue as to whether the defendant was or was not affiliated with the Communist Party at the time alleged in the indictment, you may take into consideration any statements made or acts done by the accused, and all other facts and circumstances in evidence which may aid determination of the issue.”</blockquote>
</footnote>
<footnote label="14">
<p id="b344-6"> Compare <em>United States ex rel. Kettunen </em>v. <em>Reimer, </em><span class="citation" data-id="1501275"><a href="/opinion/1501275/united-states-ex-rel-kettunen-v-reimer/" aria-description="Citation for case: United States Ex Rel. Kettunen v. Reimer">79 F. 2d 315</a></span> (C. A. 2d Cir.), and <em>Bridges </em>v. <em>Wixon, </em><span class="citation" data-id="9419697"><a href="/opinion/104184/bridges-v-wixon/" aria-description="Citation for case: Bridges v. Wixon">326 U. S. 135</a></span>, defining the term affiliation but as used in the deportation statutes.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/lee-art-theatre-inc-v-virginia--107755.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "afb1c34fa4887e90", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "lee-art-theatre-inc-v-virginia--107755"}, "payload": {"all": [{"cite": "392 U.S. 636", "page": "636", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "392"}, {"cite": "88 S. Ct. 2103", "page": "2103", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "88"}, {"cite": "20 L. Ed. 2d 1313", "page": "1313", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "20"}, {"cite": "1968 U.S. LEXIS 1145", "page": "1145", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1968"}], "display": null, "official": null, "official_selection_present": false, "record_id": "lee-art-theatre-inc-v-virginia--107755"}}
{"assertion_id": "9d073c653da40647", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "lee-art-theatre-inc-v-virginia--107755"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "lee-art-theatre-inc-v-virginia--107755", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — lee-art-theatre-inc-v-virginia--107755

```json
{
  "schema_version": "s2.v1",
  "record_id": "lee-art-theatre-inc-v-virginia--107755",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Lee Art Theatre, Inc. v. Virginia",
    "case_name_short": "Lee Art",
    "case_name_full": "Lee Art Theatre, Inc. v. Virginia",
    "input_case_name": "Lee Art Theatre, Inc. v. Virginia",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-06-17",
    "year": 1968,
    "docket": "No. 997",
    "cluster_id": 107755,
    "lead_opinion_id": 9423825,
    "sibling_ids": [],
    "absolute_url": "/opinion/107755/lee-art-theatre-inc-v-virginia/",
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
        "cite": "392 U.S. 636",
        "volume": "392",
        "reporter": "U.S.",
        "page": "636",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 2103",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "2103",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 1313",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "1313",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 1145",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1145",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "392 U.S. 636",
        "volume": "392",
        "reporter": "U.S.",
        "page": "636",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 2103",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "2103",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 1313",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "1313",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 1145",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1145",
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
    "date_created": "2026-07-06T13:44:10Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:44:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:44:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:44:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:44:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — lee-art-theatre-inc-v-virginia--107755

```
<opinion type="majority">
<author id="b678-10">Per Curiam.</author>
<p id="b678-11">The petition for a writ of certiorari is granted. Petitioner, operator of a motion picture theatre in Richmond, Virginia, was convicted in the Hustings Court of Richmond of possessing and exhibiting lewd and obscene motion pictures in violation of Title 18.1-228 of the Code of Virginia. The Supreme Court of Appeals of Virginia refused a writ of error.</p>
<p id="b678-12">The films in question were admitted in evidence over objection that they had been unconstitutionally seized. The seizure was under the authority of a warrant issued by a justice of the peace on the basis of an affidavit of a police officer which stated only the titles of the motion pictures and that the officer had determined from personal observation of them and of the billboard in front of the theatre that the films were obscene.</p>
<p id="b679-4"><page-number citation-index="1" label="637">*637</page-number>The admission of the films in evidence requires reversal of petitioner’s conviction. A seizure of allegedly obscene books on the authority of a warrant “issued on the strength of the conclusory assertions of a single police officer, without any scrutiny by the judge of any materials considered . . . obscene,” was held to be an unconstitutional seizure in <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#731" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717, 731-732</a></span>. It is true that a judge may read a copy of a book in courtroom or chambers but not as easily arrange to see a motion picture there. However, we need not decide in this case whether the justice of the peace should have viewed the motion picture before issuing the warrant. The procedure under which the warrant issued solely upon the conclusory assertions of the police officer without any inquiry by the justice of the peace into the factual basis for the officer’s conclusions was not a procedure “designed to focus searchingly on the question of obscenity,” <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#732" aria-description="Citation for case: Marcus v. Search Warrant of Property"><em>id., </em>at 732</a></span>, and therefore fell short of constitutional requirements demanding necessary sensitivity to freedom of expression. See <em>Freedman </em>v. <em>Maryland, </em><span class="citation" data-id="9422964"><a href="/opinion/106987/freedman-v-maryland/#58" aria-description="Citation for case: Freedman v. Maryland">380 U. S. 51, 58-59</a></span>.</p>
<p id="b679-5">The judgment of the Supreme Court of Appeals of Virginia is reversed and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b679-6">
<em>It is so ordered.</em>
</p>
<judges id="b679-7">Mr. Justice Black, Mr. Justice Douglas, and Mr. Justice Stewart base their concurrence in the judgment of reversal upon <em>Redrup </em>v. <em>New York, </em><span class="citation" data-id="9423403"><a href="/opinion/107426/redrup-v-new-york/" aria-description="Citation for case: Redrup v. New York">386 U. S. 767</a></span>.</judges>
</opinion>
```

---
