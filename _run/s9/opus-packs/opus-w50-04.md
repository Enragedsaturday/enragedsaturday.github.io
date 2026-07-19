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

## GROUP: content/cases/State v. Weaver.md  (`case`, 5 assertions)

### content_page

```
---
title: State v. Weaver
type: case
citation: "2011 Tex. Crim. App. LEXIS 1320 (2011)"
parallel_cite: 349 S.W.3d 521
neutral_cite: 2011 WL 4715178
court: Tex. Crim. App.
court_level: state
circuit: ""
year: 2011
date_decided: 2011-09-28
docket: PD-1635-10
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
  opinion_url: "https://www.courtlistener.com/opinion/2546485/state-v-weaver/"
  cluster_id: 2546485
  opinion_id: null
  identity_checked: true
lake:
  record_id: State v. Weaver
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Curtilage]]"
    role: Key
related:
  - "[[Curtilage]]"
  - "[[Consent Searches]]"
  - "[[Illinois v. Caballes]]"
  - "[[Florida v. Jimeno]]"
tags:
  - case
  - fourth-amendment
  - search
  - curtilage
  - consent
  - dog-sniff
  - state-court
holding: "A canine sniff of a vehicle on private, non-public business premises exceeds the scope of a limited consent and is unlawful once the owner's consent to be there for a particular purpose has ended — the rule that a dog sniff is not itself a Fourth Amendment search presupposes that the officer, and therefore the dog, has a lawful right to be where the sniff occurs, so suppression was proper where officers lingered and deployed a drug dog after their consented-to search for a person came up empty."
---

# State v. Weaver

*349 S.W.3d 521 (Tex. Crim. App. 2011)* (No. PD-1635-10) · Court of Criminal Appeals of Texas · **Persuasive — state, illustrative** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 2546485 → opinion 2546485 (349 S.W.3d 521, decided 2011-09-28); Rule quote string-matched to the CL opinion text 2026-07-07. Note: lake selected the neutral cite 2011 Tex. Crim. App. LEXIS 1320 as official — flagged for S2 re-selection (S.W.3d reporter is the correct primary). S9 promotes. -->

## Background
Four Polk County narcotics officers came to Roy Weaver's welding shop looking for "Bear," a man wanted in another county, and Weaver gave them consent to "look for him." After about ten minutes the officers had not found Bear or anything suspicious, but — having heard that methamphetamine was distributed from the business — they lingered. Sergeant Smith questioned Weaver, then asked to search a van backed into the workshop bay; Weaver refused. Smith immediately had a drug dog run around the van; the dog alerted, the van was searched, and a tin box holding glass pipes and methamphetamine was found. Weaver was arrested and charged with possession. The trial court suppressed the evidence, finding the search exceeded the scope of Weaver's consent; the court of appeals affirmed over a [[Common Legal Terms#dissenting-opinion|dissent]].

## Issue
Whether a warrantless canine sniff and search of a vehicle on the owner's private, non-public business premises — conducted after his limited consent to search for a person had come up empty and after he refused consent to search the van — exceeded the scope of his consent in violation of the Fourth Amendment.

## Rule
The Court of Criminal Appeals affirmed, resolving the case on the scope of consent. It reasoned that the settled rule that a dog sniff is not itself a Fourth Amendment search presupposes that the officer, and therefore the dog, has a right to be standing where the sniff occurs — a premise absent here, on private premises where the owner's limited consent had ended. The court held: "Because we agree that the resolution of this case turns on the scope of Mr. Weaver's consent, we affirm the judgment of the trial court and that of the court of appeals." — 349 S.W.3d at 523. ^pin-523

## Application
Weaver's consent authorized only a search for "Bear"; once that search produced nothing, a reasonable person would understand the consent as exhausted. The officers then had no lawful basis — neither probable cause nor continuing consent — to remain and deploy a drug dog around the van in the private, non-public workshop bay, an area the majority found was not open to the general public. Because the dog and officers lacked any right to be where they were when the sniff occurred, the *Caballes/Place* rule that a canine sniff is not a search did not apply, and the resulting search fell outside Weaver's consent.

## Conclusion
The suppression order was **affirmed**. Cochran, J., wrote for the majority (Meyers, Price, Womack, Johnson, Alcala, JJ.). Keller, P.J., and Keasler, J., dissented, arguing the dog sniff was not a search and that under *State v. Elias* the case should be [[Reading and Citing Cases#on-remand|remanded]] for a finding on whether the parking area was public or private.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Weaver* marks the private-premises limit on suspicionless canine sniffs: because the dog-sniff-is-not-a-search rule of *[[Illinois v. Caballes|Caballes]]* and *[[United States v. Place|Place]]* presupposes the officer's lawful presence, it does not reach a sniff conducted on private, non-public business [[Curtilage|curtilage]] after the owner's limited consent has ended.

## Appears on
- [[Curtilage]] — *Key*

## Sources
- [*State v. Weaver*, 349 S.W.3d 521 (Tex. Crim. App. 2011)](https://www.courtlistener.com/opinion/2546485/state-v-weaver/) — pinpoint: 523 (scope-of-consent holding; the CL opinion text star-paginates the S.W.3d reporter). Parallel neutral cite 2011 Tex. Crim. App. LEXIS 1320. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "49306b9d916bcc7b", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "2011 Tex. Crim. App. LEXIS 1320 (2011)", "court": "Tex. Crim. App.", "neutral_cite": "2011 WL 4715178", "official_citation_present": true, "parallel_cite": "349 S.W.3d 521", "title": "State v. Weaver", "year": "2011"}}
{"assertion_id": "4607e3a651f53c42", "dimension": "support", "kind": "home_role", "locator": {"home": "Curtilage"}, "payload": {"home": "Curtilage", "role": "Key", "title": "State v. Weaver"}}
{"assertion_id": "a2904755cb6cdc11", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A canine sniff of a vehicle on private, non-public business premises exceeds the scope of a limited consent and is unlawful once the owner's consent to be there for a particular purpose has ended — the rule that a dog sniff is not itself a Fourth Amendment search presupposes that the officer, and therefore the dog, has a lawful right to be where the sniff occurs, so suppression was proper where officers lingered and deployed a drug dog after their consented-to search for a person came up empty.", "title": "State v. Weaver"}}
{"assertion_id": "d80d3487ac16fc0b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "State v. Weaver", "varies_by_point": "false"}}
{"assertion_id": "f443261870ad38b2", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Persuasive — state, illustrative", "title": "State v. Weaver"}}
```

### lake record — State v. Weaver

```json
{
  "schema_version": "s2.v1",
  "record_id": "State v. Weaver",
  "status": "under_review",
  "identity": {
    "case_name": "State v. Weaver",
    "case_name_short": "Weaver",
    "case_name_full": "The STATE of Texas v. Roy Andrew WEAVER, Appellee",
    "input_case_name": "State v. Weaver",
    "court": "Tex. Crim. App.",
    "court_id": null,
    "court_level": "state",
    "circuit": null,
    "state": "Texas",
    "date_decided": "2011-09-28",
    "year": 2011,
    "docket": "PD-1635-10",
    "cluster_id": 2546485,
    "lead_opinion_id": 9784480,
    "sibling_ids": [],
    "absolute_url": "/opinion/2546485/state-v-weaver/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "2011 Tex. Crim. App. LEXIS 1320",
      "volume": "2011",
      "reporter": "Tex. Crim. App. LEXIS",
      "page": "1320",
      "type": 2,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "349 S.W.3d 521",
        "volume": "349",
        "reporter": "S.W.3d",
        "page": "521",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2011 WL 4715178",
        "volume": "2011",
        "reporter": "WL",
        "page": "4715178",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "349 S.W.3d 521",
        "volume": "349",
        "reporter": "S.W.3d",
        "page": "521",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 Tex. Crim. App. LEXIS 1320",
        "volume": "2011",
        "reporter": "Tex. Crim. App. LEXIS",
        "page": "1320",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 WL 4715178",
        "volume": "2011",
        "reporter": "WL",
        "page": "4715178",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "2011 Tex. Crim. App. LEXIS 1320",
    "official_selection": {
      "court_class": "state",
      "selected": "2011 Tex. Crim. App. LEXIS 1320",
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
    "date_created": "2026-07-07T01:38:37Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:38:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:38:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:38:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:38:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "state-v-weaver--2546485",
      "to_record_id": "State v. Weaver",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — State v. Weaver

```
<opinion type="majority">
<p id="b543-15">
<em>OPINION</em>
</p>
<author id="b543-16">COCHRAN, J.,</author>
<p id="A3_">delivered the opinion of the Court</p>
<judges id="Av7a">in which MEYERS, PRICE, WOMACK, JOHNSON and ALCALA, JJ., joined.</judges>
<p id="b543-17">Four police officers came to Mr. Weaver’s welding shop looking for a person wanted in another county. Mr. Weaver gave the officers consent to search for that person. The officers, over Mr. Weaver’s objection, ended up searching a van on his property and finding drugs in it. The trial judge granted Mr. Weaver’s motion to suppress because he found that the search of the van exceeded the scope of Mr. Weaver’s consent. The court of appeals, over a dissent, affirmed. We granted review in light of the justices’ disagreement. Because we agree that the resolution of this case turns on the scope of Mr. Weaver’s consent, we affirm the judgment of the trial court and that of the court of appeals.</p>
<p id="b543-18">I.</p>
<p id="b543-19">Roy Andrew Weaver owned a welding shop in Polk County.<footnotemark>1</footnotemark> There was a front office and a workshop in the rear. At the back on one side of the workshop was an open bay door with a van backed into it. Also parked in the back yard were several “broken down” vehicles, a boat, and “some other items.” One day, while the shop was open, four Polk County narcotics officers came looking for Jerry Barksdale (“Bear”), who worked or “hung out” at the shop. Bear was wanted in another county for organized crime. When the officers arrived, they saw Bear’s car parked out in front of the shop. The officers asked Mr. Weaver if they “could look around for the <page-number citation-index="1" label="524">*524</page-number>guy,” and he gave them “consent to look for him.”</p>
<p id="b544-4">The officers looked around for about ten minutes, but Bear was not at the shop nor inside the van that was backed up in the workshop bay door. Nonetheless, because the narcotics officers had received information “that there was also methamphetamine being used and distributed from the business,” they lingered in the shop.</p>
<p id="b544-5">Sergeant Smith “just began talking to Mr. Weaver. We were standing just inside the shop. I asked him if he had any illegal guns, knives, narcotics, anything like that. He advised no. He — well, he did tell me he had some guns inside the office.” Mr. Weaver showed Sgt. Smith the licensed guns in his office. After they came out of the office, Sgt. Smith then asked “who the van belonged to.” Mr. Weaver said that it was his dad’s van but that he drove it. When Sgt. Smith asked if he could search the van, Mr. Weaver refused consent.</p>
<p id="b544-6">As soon as Mr. Weaver refused consent, Sgt. Smith told Lieutenant Lowrie to retrieve his drug-dog from the patrol car and run the dog around the van parked in the bay door of the workshop. The dog showed “odor response” to the passenger door. The van was searched, and a tin box that contained glass pipes and some methamphetamine was found on the floorboard between the door and the passenger’s seat. Mr. Weaver was arrested and charged with possession of methamphetamine. He filed a motion to suppress which the trial judge, after hearing testimony from Sgt. Smith and Lt. Lowrie, granted. The judge entered findings of fact, including the following:</p>
<blockquote id="b544-7">3. The defendant gave the officers permission to search his shop for Barks-dale ....</blockquote>
<blockquote id="b544-9">4. A van was located beside the defendant’s shop on property owned by the defendant. Officers looked through the van windows and did not see Barksdale or any contraband.</blockquote>
<blockquote id="pAai">[[Image here]]</blockquote>
<blockquote id="b544-10">6. The officers asked the defendant for permission to search the van. The defendant refused permission and the officers used a drug canine to walk outside of the van.</blockquote>
<p id="b544-11">Based upon his factual findings, the trial judge concluded,</p>
<blockquote id="b544-12">The officers exceeded the scope of their search after they did not find Barksdale and they did not have enough cause to conduct the canine search on the van which they did not see being operated.</blockquote>
<p id="AObk">The State appealed, arguing that the officers and Mr. Weaver had a consensual interaction that never became a detention until the canine alert provided probable cause to arrest Mr. Weaver. Mr. Weaver responded that the consensual encounter became an unlawful detention before the dog sniff. The court of appeals affirmed the trial court’s ruling and held,</p>
<blockquote id="b544-13">In this case, the evidence shows that when the officers’ search for “Bear” ended, they had not observed anything suspicious. Because the trial judge could have determined that Weaver’s consent to search for “Bear” had ended, the trial court could reasonably find that the officers, without establishing probable cause, were not entitled to search for other purposes unrelated to that of their initial search. Under the facts of this case, we conclude the trial court did not abuse its discretion in granting Weaver’s motion to suppress. The trial court’s ruling is affirmed.<footnotemark>2</footnotemark></blockquote>
<p id="b544-14">Justice Gaultney dissented. He framed the issue as “whether the canine sniff of <page-number citation-index="1" label="525">*525</page-number>the exterior of the van while the officers were talking with Weaver was an impermissible ‘search’ for Fourth Amendment purposes.”<footnotemark>3</footnotemark> He concluded, “In this case the officers were on the business premises legally with the consent of the owner. They had not been asked to leave. Although the owner refused consent to a search of the van, the canine sniff of the exterior of the van, made while officers were questioning Weaver, was not a ‘search’ for Fourth Amendment purposes.” <footnotemark>4</footnotemark></p>
<p id="b545-5">The State Prosecuting Attorney (SPA) filed a petition for discretionary review, asking: “May police conduct a dog sniff of the exterior of an unoccupied vehicle in the parking lot of a business without the permission of the owner of the business?” We granted review in light of the justices’ disagreement on a material question of law.<footnotemark>5</footnotemark></p>
<p id="b545-6">II.</p>
<p id="b545-7">
<em>A. Standard of Review.</em>
</p>
<p id="b545-8">When reviewing the ruling on a suppression motion, the trial judge’s determination of facts — if supported by the record — is afforded almost total deference.<footnotemark>6</footnotemark> Regardless of whether the judge granted or denied the motion, appellate courts view the evidence in the light most favorable to the trial judge’s ruling.<footnotemark>7</footnotemark> The prevailing party is afforded the strongest legitimate view of the evidence and all reasonable inferences that may be drawn from that evidence.<footnotemark>8</footnotemark> We review a trial court’s application of the law of search and seizure to the facts <em>de novo.</em><footnotemark><em>9</em></footnotemark><em> </em>“We will sustain the trial judge’s ruling if that ruling is ‘reasonably supported by the record and is correct on any theory of law applicable to the case.’ ”<footnotemark>10</footnotemark></p>
<p id="b545-16">
<em>B. The Scope of Consent Under the Fourth Amendment.</em>
</p>
<p id="b545-17">The Fourth Amendment protects individuals against unreasonable searches and seizures.<footnotemark>11</footnotemark> Reasonableness is the touchstone of the Fourth Amendment.<footnotemark>12</footnotemark> And, “except in certain carefully defined classes of cases, a search of private property without proper consent is ‘unreasonable’ unless it has been authorized by a valid search warrant.”<footnotemark>13</footnotemark> The Supreme Court has “long approved consensual searches because it is no doubt reasonable for the police to conduct a search once <page-number citation-index="1" label="526">*526</page-number>they have been permitted to do so.”<footnotemark>14</footnotemark> Although consent must be positive, it may be given orally or by action, or it may be shown by circumstantial evidence.<footnotemark>15</footnotemark> The validity of an alleged consent to search is a question of fact to be determined from the totality of the circumstances.<footnotemark>16</footnotemark> Under Texas law, the State must prove voluntary consent by clear and convincing evidence.<footnotemark>17</footnotemark></p>
<p id="b546-4">The scope of a search is usually defined by its expressed object.<footnotemark>18</footnotemark> A person is free to limit the scope of the consent that he gives.<footnotemark>19</footnotemark> If police rely on consent as the basis for a warrantless search, “they have no more authority than they have apparently been given by the consent.”<footnotemark>20</footnotemark> It is therefore “important to take account of any express or implied limitations or qualifications attending that consent which establish the permissible scope of the search in terms of such matters as time, duration, area, or intensity.”<footnotemark>21</footnotemark> On the other hand, a person’s silence in the face of an officer’s further actions may imply consent to that further action.<footnotemark>22</footnotemark> The “standard for measuring the scope of a suspect’s consent under the Fourth Amendment is that of ‘objective’ reasonableness — what would the typical reasonable person have understood by the exchange between the officer and the suspect?” <footnotemark>23</footnotemark> Therefore, a court reviewing the totality of the circumstances of a particular police-citizen interaction does so without regard for the subjective thoughts or intents of either the officer or the citizen.<footnotemark>24</footnotemark> Still, in Texas, the “clear and convincing” burden “requires the prosecution to show the consent given was positive and unequivocal and there must not be duress or coercion, actual or implied.”<footnotemark>25</footnotemark></p>
<p id="b546-14">
<em>C. Business and Commercial Premises are Protected Areas.</em>
</p>
<p id="b546-15">The occupant of a business establishment enjoys the same constitutional <page-number citation-index="1" label="527">*527</page-number>right to be free from unreasonable searches as does the occupant of a private residence.<footnotemark>26</footnotemark> But “business and commercial premises are not as private as residential premises,” and “consequently there are various police investigative procedures which may be directed at such premises without the police conduct constituting a Fourth Amendment search.”<footnotemark>27</footnotemark> Police, although motivated by an investigative purpose, are as free as the general public to enter premises “open to the public,” when they are open to the public.<footnotemark>28</footnotemark> Officers are then entitled to note objects in plain view,<footnotemark>29</footnotemark> or examine merchandise as a customer would.<footnotemark>30</footnotemark> For “actions not to constitute a Fourth Amendment search, the officer must remain in that portion of the premises which is open to the public.”<footnotemark>31</footnotemark></p>
<p id="AaB">III.</p>
<p id="b547-10">The SPA asserts that the motion to suppress was granted based on incorrect conclusions of law rather than any fact-findings that were unfavorable to the State. These conclusions were incorrect, argues the SPA, because 1) the officers did not need permission to be in “the parking lot” when they initiated the dog sniff; 2) neither Mr. Weaver nor the van were seized in order to conduct the dog sniff; 3) the dog sniff was not a search; and 4) the dog’s positive alert justified the search. The Supreme Court has made it clear that a dog sniff is not a search,<footnotemark>32</footnotemark> and it is generally accepted that a positive alert by a certified drug dog is usually enough, by itself, to give officers probable cause to <page-number citation-index="1" label="528">*528</page-number>search.<footnotemark>33</footnotemark> We agree with the SPA that neither Mr. Weaver nor the van were seized in order to conduct the dog sniff.</p>
<p id="b548-4">But, as discussed below, the SPA assumes a fact that is not in evidence: that the van was parked in a parking lot “open to the public.”<footnotemark>34</footnotemark> Viewing the evidence in the light most favorable to the trial judge’s ruling, this area was not part of the “public” area of his welding shop. Therefore, the officers needed permission to be where they were when they initiated the dog sniff, but they did not have it.<footnotemark>35</footnotemark></p>
<p id="b548-5"><em>A. Affording appellee the “strongest legitimate view of the evidence, </em>” <em>the van was not parked in a parking lot open to the public.</em></p>
<p id="b548-6">The SPA’s position is apparent in the way it framed the issue for review: “May police conduct a dog sniff of the exterior of an unoccupied vehicle in the parking lot of a business without the permission of the owner of the business?” Surely the answer to that question, on its face, is yes. A public parking lot is public regardless of whether a nearby business is open or not.</p>
<p id="b548-11">In <em>Illinois v. </em>Caballes,<footnotemark>36</footnotemark> the Supreme Court held that the use of a narcotics-detection dog to sniff around the exteri- or of a motorist’s vehicle during a lawful traffic stop did not violate the Fourth Amendment because it revealed no information other than the location of a substance that the individual had no right to possess.<footnotemark>37</footnotemark> In keeping with Justice Ginsburg’s prophecy that <em>Caballes </em>“clears the way for suspicionless, dog-accompanied drug sweeps of parked cars along sidewalks and in parking lots,”<footnotemark>38</footnotemark> it has done just that. Federal and state courts alike have used <em>Caballes </em>to uphold dog sniffs in the public parking lots of gas stations, hotels, restaurants, and high schools.<footnotemark>39</footnotemark> But in <em>Caballes, </em>Justice Stevens empha<page-number citation-index="1" label="529">*529</page-number>sized that the police cannot prolong a traffic stop beyond the time reasonably required to accomplish its purpose simply to give them time to bring in a drug dog.<footnotemark>40</footnotemark> As our courts of appeals have recognized, officers initiating a dog sniff must have the right to be where they are at the time they initiate a dog sniff.<footnotemark>41</footnotemark></p>
<p id="b549-5">It is the <em>Caballes </em>line of cases that the SPA relies on here. The problem in this case is that no one, except the prosecutor, characterized the place the van was parked as a “parking lot.” Lt. Lowrie said that the truck was parked in a “sall[y] port.”</p>
<blockquote id="AJe2">Q. Where was the van parked? '</blockquote>
<blockquote id="b549-6">A. It was the — I guess it would be the north side of the building back up to the big sall[y] port<footnotemark>42</footnotemark> on the building.</blockquote>
<blockquote id="AyVM">Q. Is it, like, a parking lot or a parking area?</blockquote>
<blockquote id="b549-11">A. It’s a big, bay door. I guess you would say it’s kind of like a loading/unloading for the business area.</blockquote>
<p id="b549-12">The State argued to the trial court that “The vehicle ... was located on a parking lot that was in — in a business that was open for public use or open to the public. So the fact that the officers decided to run the canine, even though maybe they didn’t see or smell something, they didn’t have to have any type of reasonable suspicion to do that.” The SPA argues similarly: “While on the premises of a business open to the public, police are permitted to conduct a dog sniff of vehicles parked in the <page-number citation-index="1" label="530">*530</page-number>parking area.... The unoccupied van was parked in the parking lot[.]”<footnotemark>43</footnotemark></p>
<p id="b550-4">But the trial court did not find that the van was parked in a public parking lot. Rather, it found the van “was located beside the defendant’s shop on property owned by the defendant.” The prevailing party is afforded the strongest legitimate view of the evidence and all reasonable inferences that may be drawn from that evidence. The facts here support the trial court’s implicit finding that the van was not parked on any part of the business premises open to the public or in a public “parking lot.”<footnotemark>44</footnotemark> From the evidence in this record, the trial judge could have found otherwise, but he did not do so. We are obliged to give almost total deference to his implied factual findings.<footnotemark>45</footnotemark> Therefore, unless the officers had Mr. Weaver’s consent to be standing beside the van at the loading dock, they were no longer entitled to be in the non-public portion of the welding workshop at the time they conducted the dog sniff.<footnotemark>46</footnotemark></p>
<p id="b550-11">
<em>B. Affording Mr. Weaver the “strongest legitimate view of the evidence," the officers did not have continued consent to be on the premises at the time they ran the dog sniff</em>
</p>
<p id="b550-12">The SPA asserts that the officers — who had lawfully entered the premises — were “under no obligation to leave unless asked” and that there “was no evidence or fact finding that the officers were ever asked to stop their investigation or leave the premises.”<footnotemark>47</footnotemark> But the relevant question here is as follows: What would the typical reasonable person have under<page-number citation-index="1" label="531">*531</page-number>stood by the exchange between the officers and Mr. Weaver?<footnotemark>48</footnotemark> Mr. Weaver gave oral consent to search his welding shop for “Bear,” voluntarily showed the officers his registered guns,<footnotemark>49</footnotemark> and then unequivocally refused to consent to a search of the van backed up in the loading dock of his shop.</p>
<p id="b551-5">We recently addressed the scope of a consent to search under the Fourth Amendment in <em>Valtierra v. State.</em><footnotemark><em>50</em></footnotemark><em> </em>There, the trial court and the court of appeals agreed that Heriberto Valtierra consented to have police officers enter his apartment to talk to Erica, a 13-year-old runaway. The question before us was whether Heriberto’s consent extended to the officer’s act of walking down the open hallway to knock on the bathroom door where Erica was said to be taking a shower. We held that it was objectively reasonable for the officer to conclude that Heriberto’s general consent to come inside the apartment to talk to Erica included consent to walk down the open hallway to knock on the bathroom door.<footnotemark>51</footnotemark> Thus, the officer was lawfully present in the hallway when he observed, through an open bedroom door, two men making furtive gestures and throwing items under the bed.<footnotemark>52</footnotemark></p>
<p id="b551-6">This case is like <em>Valtierra </em>in that the officers here obtained oral consent to enter the premises to look for a specific individual. This case is also unlike <em>Valtierra, </em>because here the officers had finished looking for the specific individual and had achieved the ostensible purpose of their entry. And here, unlike in <em>Valtierra, </em>Mr. Weaver unequivocally said “No,” to a further search of his van.</p>
<p id="b551-11">The legal question is, what would “the typical reasonable person have understood by the exchange between the officer and the suspect?” We think that it was objectively unreasonable for the officers to conclude that Mr. Weaver’s act of objecting to the van search indicated, by clear and convincing evidence, his consent for the officers to remain standing beside his van while one officer went back out to the patrol car and retrieved a drug dog to run around his van.<footnotemark>53</footnotemark> A typical reasonable person would have understood — from Mr. Weaver’s refusal of consent to search the van — that he had had enough. It would be unreasonable for that typical person, having heard an unequivocal “No,” to think that he had “positive and unequivocal” consent, not only to remain standing beside the van on the non-public premises, but also to retrieve yet another unwelcome intruder. There is certainly no indication in the record that Mr. Weaver consented for the officers to bring the drug dog from the patrol car to the van parked at his loading dock. From these facts, the trial <page-number citation-index="1" label="532">*532</page-number>judge could have concluded that the consent to search for “Bear” was lawful at its inception, but that it had been completed. The officers had completed their stated mission. Thus, when Mr. Weaver unequivocally said “No” to any further search of his van, the officers violated the Fourth Amendment by remaining on his private business premises and bringing in a drug dog without legal authorization. Therefore, the trial judge could have justifiably concluded that the “nonconsensual” use of the drug dog and the subsequent discovery of contraband were the product of an unconstitutional search on private premises.</p>
<p id="b552-4">The record, viewed in the light most favorable to the trial judge’s ruling, supports an implicit fact finding that the van was parked in a protected, non-public area of the business premises rather than in a parking lot open to the public. And the record also supports the trial judge’s legal conclusion that the officers had worn out their welcome and lingered beyond the scope of Mr. Weaver’s consent before the initiation of the dog sniff. We recognize that this ease is a close call — but it is in the “close call” cases that the need for giving discretion to the trial judge and deferring to his factual findings is greatest, especially when the State must prove positive consent by clear and convincing evidence. We therefore affirm the court of appeals’s judgment that upheld the trial judge’s ruling.</p>
<judges id="b552-5">KELLER, P.J., filed a dissenting opinion in which KEASLER and HERVEY, JJ., joined.</judges>
<p id="AjE">KEASLER, J., filed a dissenting opinion in which KELLER, P.J., and HERVEY, J., joined.</p>
<footnote label="1">
<p id="AA_">. The shop is located at 203 Gray Drive in Livingston.</p>
</footnote>
<footnote label="2">
<p id="b544-8">. <em>State v. Weaver, </em><span class="citation no-link">2010 WL 3518743</span>, *4, 2010 Tex.App. LEXIS 7425, *9 (Tex.App.-Beaumont Sept. 8, 2010) (not designated for publication)</p>
</footnote>
<footnote label="3">
<p id="b545-9">. <em>Id. </em>at *4, 2010 Tex.App. LEXIS 7425, at *10-11 (Gaultney, J., dissenting).</p>
</footnote>
<footnote label="4">
<p id="b545-10">. <em>Id. </em>at *5, 2010 Tex.App. LEXIS 7425, at *11-12 (citing <em>City of Indianapolis v. Edmond, </em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#40" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U.S. 32, 40</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S.Ct. 447</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L.Ed.2d 333</a></span> (2000); <em>Illinois v. Caballes, </em><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/#410" aria-description="Citation for case: Illinois v. Caballes">543 U.S. 405, 410</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">160 L.Ed.2d 842</a></span> (2005); <em>United States v. Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place">462 U.S. 696, 707</a></span>, <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">103 S.Ct. 2637</a></span>, <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">77 L.Ed.2d 110</a></span> (1983)).</p>
</footnote>
<footnote label="5">
<p id="b545-12">. Tex.R.App. P. 66.3(e).</p>
</footnote>
<footnote label="6">
<p id="b545-13">. <em>State v. Woodard, </em><span class="citation" data-id="9783836"><a href="/opinion/2540788/state-v-woodard/#410" aria-description="Citation for case: State v. Woodard">341 S.W.3d 404, 410</a></span> (Tex.Crim.App.2011) (citing <em>Guzman v. State, </em><span class="citation" data-id="9863199"><a href="/opinion/2449770/guzman-v-state/#89" aria-description="Citation for case: Guzman v. State">955 S.W.2d 85, 89</a></span> (Tex.Crim.App.1997)).</p>
</footnote>
<footnote label="7">
<p id="b545-14">. <span class="citation" data-id="9863199"><a href="/opinion/2449770/guzman-v-state/" aria-description="Citation for case: Guzman v. State">Id.</a></span> (citing State <em>v. Garcia-Cantu, </em><span class="citation" data-id="9680128"><a href="/opinion/1769810/state-v-garcia-cantu/#241" aria-description="Citation for case: State v. Garcia-Cantu">253 S.W.3d 236, 241</a></span> (Tex.Crim.App.2008); <em>Gutierrez v. State, </em><span class="citation" data-id="9643603"><a href="/opinion/1508583/gutierrez-v-state/#687" aria-description="Citation for case: Gutierrez v. State">221 S.W.3d 680, 687</a></span> (Tex.Crim.App.2007)).</p>
</footnote>
<footnote label="8">
<p id="b545-18">. <em><span class="citation" data-id="9643603"><a href="/opinion/1508583/gutierrez-v-state/" aria-description="Citation for case: Gutierrez v. State">Id.</a></span> </em>(citing <em>Garcia-Cantu, </em><span class="citation" data-id="9680128"><a href="/opinion/1769810/state-v-garcia-cantu/#241" aria-description="Citation for case: State v. Garcia-Cantu">253 S.W.3d at 241</a></span>).</p>
</footnote>
<footnote label="9">
<p id="b545-19">. <em>Valtierra v. State, </em><span class="citation" data-id="1370428"><a href="/opinion/1370428/valtierra-v-state/#447" aria-description="Citation for case: Valtierra v. State">310 S.W.3d 442, 447</a></span> (Tex.Crim.App.2010); <em>Wiede v. State, </em><span class="citation" data-id="1404049"><a href="/opinion/1404049/wiede-v-state/#25" aria-description="Citation for case: Wiede v. State">214 S.W.3d 17, 25</a></span> (Tex.Crim.App.2007).</p>
</footnote>
<footnote label="10">
<p id="b545-20">. <em>Valtierra, </em><span class="citation" data-id="1370428"><a href="/opinion/1370428/valtierra-v-state/" aria-description="Citation for case: Valtierra v. State">310 S.W.3d at 447</a></span>-48 (quoting <em>State v. Dixon, </em><span class="citation" data-id="9620856"><a href="/opinion/1400629/state-v-dixon/#590" aria-description="Citation for case: State v. Dixon">206 S.W.3d 587, 590</a></span> (Tex.Crim.App.2006)).</p>
</footnote>
<footnote label="11">
<p id="b545-21">. U.S. Const, amend. IV.</p>
</footnote>
<footnote label="12">
<p id="b545-22">. <em>Florida v. Jimeno, </em><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#250" aria-description="Citation for case: Florida v. Jimeno">500 U.S. 248, 250</a></span>, <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">111 S.Ct. 1801</a></span>, <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">114 L.Ed.2d 297</a></span> (1991).</p>
</footnote>
<footnote label="13">
<p id="b545-23">. <em>Camara v. Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U.S. 523, 528-29</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">87 S.Ct. 1727</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">18 L.Ed.2d 930</a></span> (1967).</p>
</footnote>
<footnote label="14">
<p id="b546-5">. <em>Jimeno, </em><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#250" aria-description="Citation for case: Florida v. Jimeno">500 U.S. at 250-51</a></span>, <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">111 S.Ct. 1801</a></span>.</p>
</footnote>
<footnote label="15">
<p id="b546-6">. <em>Valtierra, </em><span class="citation" data-id="1370428"><a href="/opinion/1370428/valtierra-v-state/#448" aria-description="Citation for case: Valtierra v. State">310 S.W.3d at 448</a></span>; <em>Johnson v. State, </em><span class="citation" data-id="9729074"><a href="/opinion/2165895/johnson-v-state/" aria-description="Citation for case: Johnson v. State">226 S.W.3d 439</a></span>, 446 n. 27 (Tex.Crim.App.2007); <em>Gallups v. State, </em><span class="citation" data-id="9655220"><a href="/opinion/1577308/gallups-v-state/#201" aria-description="Citation for case: Gallups v. State">151 S.W.3d 196, 201</a></span> (Tex.Crim.App.2004).</p>
</footnote>
<footnote label="16">
<p id="b546-7">. <em>Valtierra, </em><span class="citation" data-id="1370428"><a href="/opinion/1370428/valtierra-v-state/#448" aria-description="Citation for case: Valtierra v. State">310 S.W.3d at 448</a></span>; <em>Ohio v. Robinette, </em><span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/#39" aria-description="Citation for case: Ohio v. Robinette">519 U.S. 33, 39-40</a></span>, <span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/" aria-description="Citation for case: Ohio v. Robinette">117 S.Ct. 417</a></span>, <span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/" aria-description="Citation for case: Ohio v. Robinette">136 L.Ed.2d 347</a></span> (1996); <em>Gallups, </em><span class="citation" data-id="9655220"><a href="/opinion/1577308/gallups-v-state/#200" aria-description="Citation for case: Gallups v. State">151 S.W.3d at 200-01</a></span>; <em>Guevara v. State, </em><span class="citation" data-id="2188747"><a href="/opinion/2188747/guevara-v-state/#582" aria-description="Citation for case: Guevara v. State">97 S.W.3d 579, 582</a></span> (Tex.Crim.App.2003).</p>
</footnote>
<footnote label="17">
<p id="b546-8">. <em>Valtierra, </em><span class="citation" data-id="1370428"><a href="/opinion/1370428/valtierra-v-state/#448" aria-description="Citation for case: Valtierra v. State">310 S.W.3d at 448</a></span>; <em>Reasor v. State, </em><span class="citation" data-id="1580731"><a href="/opinion/1580731/reasor-v-state/#817" aria-description="Citation for case: Reasor v. State">12 S.W.3d 813, 817</a></span> (Tex.Crim.App.2000); <em>Meeks v. State, 692 </em>S.W.2d 504, 509 (Tex.Crim.App.1985).</p>
</footnote>
<footnote label="18">
<p id="b546-9">. <em>Jimeno, </em><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#251" aria-description="Citation for case: Florida v. Jimeno">500 U.S. at 251</a></span>, <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">111 S.Ct. 1801</a></span>.</p>
</footnote>
<footnote label="19">
<p id="b546-10">. <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#252" aria-description="Citation for case: Florida v. Jimeno"><em>Id. </em>at 252</a></span>, <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">111 S.Ct. 1801</a></span> ("A suspect may of course delimit as he chooses the scope of the search to which he consents.”).</p>
</footnote>
<footnote label="20">
<p id="b546-11">. 4 Wayne R. LaFave, Search and Seizure § 8.1© at 19 (4th ed.2004).</p>
</footnote>
<footnote label="21">
<p id="b546-12">. <em>Id.</em></p>
</footnote>
<footnote label="22">
<p id="b546-16">. <em>Valtierra, </em><span class="citation" data-id="1370428"><a href="/opinion/1370428/valtierra-v-state/#449" aria-description="Citation for case: Valtierra v. State">310 S.W.3d at 449</a></span>. <em>Accord United States v. Starr, </em><span class="citation" data-id="1235169"><a href="/opinion/1235169/united-states-v-starr/#996" aria-description="Citation for case: United States v. Starr">533 F.3d 985, 996</a></span> (8th Cir.2008) ("Starr was present during the officers' full search of his home, but remained silent and made no attempt to impede their efforts or to express his concern that they were exceeding the scope of his consent. Given these facts, we conclude that a reasonable person would have believed that the officers had authority to conduct a full search of Starr’s home including his closet and a roll of film; therefore, this warrantless search did not violate the Fourth Amendment because it was authorized by Starr's consent.”).</p>
</footnote>
<footnote label="23">
<p id="b546-17">. <em>Florida v. Jimeno, </em><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#251" aria-description="Citation for case: Florida v. Jimeno">500 U.S. at 251</a></span>, <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">111 S.Ct. 1801</a></span>.</p>
</footnote>
<footnote label="24">
<p id="b546-18">. <em>Meekins v. State, </em><span class="citation" data-id="9784155"><a href="/opinion/2544137/meekins-v-state/#459" aria-description="Citation for case: Meekins v. State">340 S.W.3d 454, 459</a></span> (Tex.Crim.App.2011) (citing <em>Maryland </em>v. <em>Macon, </em><span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/#470" aria-description="Citation for case: Maryland v. MacOn">472 U.S. 463, 470-71</a></span>, <span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/" aria-description="Citation for case: Maryland v. MacOn">105 S.Ct. 2778</a></span>, <span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/" aria-description="Citation for case: Maryland v. MacOn">86 L.Ed.2d 370</a></span> (1985); <em>Scott v. United States, </em><span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#136" aria-description="Citation for case: Scott v. United States">436 U.S. 128, 136</a></span>, <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/" aria-description="Citation for case: Scott v. United States">98 S.Ct. 1717</a></span>, <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/" aria-description="Citation for case: Scott v. United States">56 L.Ed.2d <em>168 </em></a></span>(1978)).</p>
</footnote>
<footnote label="25">
<p id="b546-19">. <em>Meeks </em>v. <em>State, </em><span class="citation" data-id="1782139"><a href="/opinion/1782139/mccullough-v-state/#509" aria-description="Citation for case: McCullough v. State">692 S.W.2d 504, 509</a></span> (Tex.Crim.App.1985).</p>
</footnote>
<footnote label="26">
<p id="b547-4">. <em>See v. Seattle, </em><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/#543" aria-description="Citation for case: See v. City of Seattle">387 U.S. 541, 543</a></span>, <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">87 S.Ct. 1737</a></span>, <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">18 L.Ed.2d 943</a></span> (1967) ("The businessman, like the occupant of a residence, has a constitutional right to go about his business free from unreasonable official entries upon his private commercial property."); <em>Oliver v. United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U.S. 170</a></span>, 178 n. 8, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">104 S.Ct. 1735</a></span>, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">80 L.Ed.2d 214</a></span> (1984) ("The Fourth Amendment’s protection of offices and commercial buildings, in which there may be legitimate expectations of privacy, is based upon societal expectations that have deep roots in the history of the Amendment.”).</p>
</footnote>
<footnote label="27">
<p id="b547-5">. 1 LaFave, <em>supra </em>note 20, § 2.4(b) at 627.</p>
</footnote>
<footnote label="28">
<p id="b547-6">. <em>Maryland v. Macon, </em><span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/#470" aria-description="Citation for case: Maryland v. MacOn">472 U.S. 463, 470</a></span>, <span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/" aria-description="Citation for case: Maryland v. MacOn">105 S.Ct. 2778</a></span>, <span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/" aria-description="Citation for case: Maryland v. MacOn">86 L.Ed.2d 370</a></span> (1985).</p>
</footnote>
<footnote label="29">
<p id="b547-7">. <em>United States v. Morton, </em><span class="citation" data-id="664091"><a href="/opinion/664091/united-states-v-phillip-daniel-morton/#913" aria-description="Citation for case: United States v. Phillip Daniel Morton">17 F.3d 911, 913</a></span> (6th Cir.1994) (discovery and seizure of the gun did not violate the Fourth Amendment; testimony fairly established that the auto shop was open to the public for business, so the officers lawfully entered the shop, and, when the defendant stood up, an officer saw, in plain view, a gun in defendant's back pocket).</p>
</footnote>
<footnote label="30">
<p id="b547-8">. <em>Lo-Ji Sales, Inc. v. New York, </em><span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/#329" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York">442 U.S. 319, 329</a></span>, <span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York">99 S.Ct. 2319</a></span>, <span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York">60 L.Ed.2d 920</a></span> (1979) (Fourth Amendment violated by sweeping search of "adult” bookstore; officers viewed films “without the payment a member of the public would be required to make,” and viewed magazines and books "not ... as a customer would ordinarily see them” by removing cellophane wrappers).</p>
</footnote>
<footnote label="31">
<p id="b547-12">. 1 LaFave, <em>supra </em>note 20 § 2.4(b) at 630. Courts have held that searches of private offices, airline baggage rooms, employee break rooms, employee locker rooms, private dressing rooms of entertainers, etc. are not sustainable on the theory of "store premises open to the public.” <em>Id. </em>(collecting cases).</p>
</footnote>
<footnote label="32">
<p id="b547-13">. <em>Illinois v. Caballes, </em><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/#409" aria-description="Citation for case: Illinois v. Caballes">543 U.S. 405, 409</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">160 L.Ed.2d 842</a></span> (2005) (holding that a canine sniff of an automobile need not be justified by reasonable articulable suspicion of drug activity); <em>City of Indianapolis v. Edmond, </em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#40" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U.S. 32, 40</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S.Ct. 447</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L.Ed.2d 333</a></span> (2000) (recognizing that a canine sniff of an automobile is not a search); <em>United States v. Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#706" aria-description="Citation for case: United States v. Place">462 U.S. 696, 706-07</a></span>, <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">103 S.Ct. 2637</a></span>, <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">77 L.Ed.2d 110</a></span> (1983) (holding that a canine sniff of luggage does not constitute a search). These holdings are based on the legal theory that a canine sniff by a well-trained narcotics-detection dog is not Fourth Amendment search because it reveals no information other than the location of a substance that no individual has a legitimate privacy interest in. They are all premised, however, upon a finding that the officer — and therefore the dog — have a right to be standing where they are at the time of the canine sniff.</p>
</footnote>
<footnote label="33">
<p id="b548-7">. <em>United States v. Parada, </em><span class="citation" data-id="172578"><a href="/opinion/172578/united-states-v-parada/#1282" aria-description="Citation for case: United States v. Parada">577 F.3d 1275, 1282</a></span> (10th Cir.2009).</p>
</footnote>
<footnote label="34">
<p id="b548-8">. It has been suggested that this Court should remand this case to the trial judge to enter a specific finding on a disputed fact that is dispositive to the appeal. <em>See State v. Elias, </em><span class="citation" data-id="9783708"><a href="/opinion/2539936/state-v-elias/#676" aria-description="Citation for case: State v. Elias">339 S.W.3d 667, 676</a></span> (Tex.Crim.App.2011). But here, unlike the situation in <em><span class="citation" data-id="9783708"><a href="/opinion/2539936/state-v-elias/" aria-description="Citation for case: State v. Elias">Elias</a></span>, </em>there is no disputed fact issue. There is no evidence in this record that the van backed into the workshop bay door was located in a "parking lot” or an area that was open to the general public. The State <em>argues </em>that the van was located in a public parking lot, but there is no evidence from any witness in the record that supports that argument. We need not remand this case for the trial judge to enter a finding on a fact that, based on the record, is not in dispute.</p>
</footnote>
<footnote label="35">
<p id="b548-9">. <em>Weaver, </em><span class="citation no-link">2010 WL 3518743</span>, at <em>*4, </em>2010 Tex.App. LEXIS 7425, at *9 ("Because the trial judge could have determined that Weaver's consent to search for ‘Bear’ had ended, the trial court could reasonably find that the officers, without establishing probable cause, were not entitled to search for other purposes unrelated to that of their initial search.”).</p>
</footnote>
<footnote label="36">
<p id="b548-12">. <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">543 U.S. 405</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">160 L.Ed.2d 842</a></span> (2005).</p>
</footnote>
<footnote label="37">
<p id="b548-13">. <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/#409" aria-description="Citation for case: Illinois v. Caballes"><em>Id. </em>at 409</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span>.</p>
</footnote>
<footnote label="38">
<p id="b548-14">. <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/#422" aria-description="Citation for case: Illinois v. Caballes"><em>Id. </em>at 422</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span> (Ginsburg, J„ dissenting) ("Today’s decision ... clears the way for suspicionless, dog-accompanied drug sweeps of parked cars along sidewalks and in parking lots.”).</p>
</footnote>
<footnote label="39">
<p id="b548-15">. <em>United States v. Dyson, </em><span class="citation" data-id="215072"><a href="/opinion/215072/united-states-v-dyson/" aria-description="Citation for case: United States v. Dyson">639 F.3d 230</a></span>-33 (6th Cir.2011) (dog sniff of an unoccupied, parked Maxima at gas station “does not in itself require reasonable suspicion”); <em>United States v. Perez, </em><span class="citation" data-id="793575"><a href="/opinion/793575/united-states-v-jaime-perez-04-5440-walter-rhodes-05-5373/" aria-description="Citation for case: United States v. Jaime Perez (04-5440) Walter Rhodes...">440 F.3d 363</a></span> (6th Cir.2006) (dog sniff of unoccupied Tahoe, which sat in the parking lot of the hotel and was not stopped, detained or moved, was not a search or seizure; no reasonable suspicion is required when using a drug-sniffing dog); <em>United States v. Engles, </em><span class="citation" data-id="797344"><a href="/opinion/797344/united-states-v-michael-delevan-engles/#1245" aria-description="Citation for case: United States v. Michael Delevan Engles">481 F.3d 1243, 1245</a></span> (10th Cir.2007) (dog sniff of the exterior of a vehicle parked in a restaurant parking lot does not require reasonable suspicion because it is not a Fourth Amendment intrusion); <em>State v. Hobbs, </em><span class="citation" data-id="9504938"><a href="/opinion/852203/state-v-hobbs/#1286" aria-description="Citation for case: State v. Hobbs">933 N.E.2d 1281, 1286-87</a></span> (Ind.2010) (dog sniff of car in Pizza Hut lot, conducted <page-number citation-index="1" label="529">*529</page-number>under circumstances in which Hobbs was not unconstitutionally seized, not Fourth Amendment violation); <em>Dowty v. State, </em><span class="citation" data-id="9691174"><a href="/opinion/1877908/dowty-v-state/" aria-description="Citation for case: Dowty v. State">363 Ark. 1</a></span>, <span class="citation" data-id="9691174"><a href="/opinion/1877908/dowty-v-state/#854" aria-description="Citation for case: Dowty v. State">210 S.W.3d 850, 854-55</a></span> (2005) (dog sniff of Grand Am and Suburban at a Western Siz-zlin parking lot not Fourth Amendment search); <em>Myers </em>v. <em>State, </em><span class="citation" data-id="9505227"><a href="/opinion/852725/myers-v-state/#1159" aria-description="Citation for case: Myers v. State">839 N.E.2d 1154, 1159</a></span> (Ind.2005) (high-school-student defendant’s car was subject to the narcotics dog-sniff test absent reasonable particularized suspicion, as it was parked and unoccupied and the defendant was in school).</p>
</footnote>
<footnote label="40">
<p id="b549-8">. <em>Caballes, </em><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/#407" aria-description="Citation for case: Illinois v. Caballes">543 U.S. at 407-08</a></span>, <span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span> ("A seizure that is justified solely by the interest in issuing a warning ticket to the driver can become unlawful if it is prolonged beyond the time reasonably required to complete that mission. In an earlier case involving a dog sniff that occurred during an unreasonably prolonged traffic stop, the Illinois Supreme Court held that use of the dog and the subsequent discovery of contraband were the product of an unconstitutional seizure. We may assume that a similar result would be warranted in this case if the dog sniff had been conducted while respondent was being unlawfully detained.”) (citation omitted).</p>
</footnote>
<footnote label="41">
<p id="b549-9">. <em>See Branch v. State, </em><span class="citation" data-id="2291162"><a href="/opinion/2291162/branch-v-state/#901" aria-description="Citation for case: Branch v. State">335 S.W.3d 893, 901</a></span> (Tex.App.-Austin 2011, no pet.) ("Given the evidence regarding the initial traffic stop and the arrival of the drug-detection dog, all of which shows that the dog arrived within eight minutes of the traffic stop and before Wing-field finished conducting normal procedures for a traffic stop, we conclude that the record supports an implied finding by the trial court that the time it took for the dog to arrive did not prolong the initial stop beyond the time reasonably required to complete the mission of the stop."); <em>Johnson v. State, </em><span class="citation" data-id="2271814"><a href="/opinion/2271814/johnson-v-state/#562" aria-description="Citation for case: Johnson v. State">323 S.W.3d 561, 562-63</a></span> (Tex.App.-Eastland 2010, pet. ref’d) (Fourth Amendment does not requires reasonable suspicion to justify using a drug-detection dog to sniff a vehicle during a legitimate traffic stop; while one officer was running a check on appellant’s driver’s license, another officer had his drug-detection dog conduct an open-air search around the vehicle, and the dog alerted on the driver’s door).</p>
</footnote>
<footnote label="42">
<p id="b549-14">. Sally port may have been an unfortunate choice of words. It literally means "1. in fortification, a postern gate, or a passage under ground from the inner to the outer works, to afford free egress to troops in making a sally, closed by massive gates when not in use. 2. a large port on each quarter of a fire ship, for the escape of the men into boats when the train is fired; also, a large port in an ironclad.” Webster’s New Twentieth Century Dictionary Unabridged 1599 (2nd ed.1983). What the officer undoubtedly meant to say was that the van was backed into a loading-dock bay at the rear of the welding workshop.</p>
</footnote>
<footnote label="43">
<p id="b550-5">. SPA's Brief at 4, 7.</p>
</footnote>
<footnote label="44">
<p id="b550-6">. The record indicates that the parking lot for the welding shop was at the front of the shop where "Bear’s” car was parked. Furthermore, it is unlikely that Mr. Weaver would be storing his "broke down” vehicles, boat, and other items in a public parking lot, and Lt. Lowrie testified that those items were out in "the back” area with the van. It is also unlikely that the general public would have access to the workshop area and loading dock of a welding shop as welding operations involve both significant fire hazards and risks due to the use and movement of heavy equipment.</p>
</footnote>
<footnote label="45">
<p id="b550-7">. <em>State </em>v. <em>Woodard, </em><span class="citation" data-id="9783836"><a href="/opinion/2540788/state-v-woodard/#410" aria-description="Citation for case: State v. Woodard">341 S.W.3d 404, 410</a></span> (Tex.Crim.App.2011).</p>
</footnote>
<footnote label="46">
<p id="b550-8">. <em>Cf. Buchanan v. State, </em><span class="citation" data-id="1466758"><a href="/opinion/1466758/buchanan-v-state/#774" aria-description="Citation for case: Buchanan v. State">129 S.W.3d 767, 774</a></span> (Tex.App.-Amarillo 2004, pet. ref'd). In that case, the trial court denied a motion to suppress, but made no findings. The court of appeals, viewing the facts in the light most favorable to the prevailing party as it was required to do, found that appellant had no legitimate expectation of privacy in the dirt driveway entrance to a business run behind his house:</p>
<blockquote id="b550-9">The time of day, the presence of no one outside the fence with whom the officers could speak, the large open gate, the presence of a well-defined dirt driveway leading through the gate to a building behind the empty house, appellant’s operation (behind the gate) of a business involving vehicles owned by third parties, the reasonable inference not only that third parties passed through the gates to obtain appellant's mechanical services but also that they were authorized to do so during normal business hours, the lack of any evidence illustrating that only appellant or certain designated individuals could drive their cars through the gate, the presence of a third party actually working on his vehicle inside the fenced lot, and the officers confining themselves to the well-defined dirt driveway are indicia upon which a trial court could reasonably find that appellant had no legitimate expectation of privacy in the dirt driveway behind the fence and that which could be perceived from it. Thus, no search occurred when the officers passed through the gate while utilizing that path and smelled the ether. Nor can we say that the trial court abused its discretion in refusing to find that the entry violated appellant’s constitutional rights.</blockquote>
<p id="b550-14"><span class="citation" data-id="1466758"><a href="/opinion/1466758/buchanan-v-state/#774" aria-description="Citation for case: Buchanan v. State"><em>Id. </em>at 774</a></span>.</p>
</footnote>
<footnote label="47">
<p id="b550-15">. SPA’s Brief at 7.</p>
</footnote>
<footnote label="48">
<p id="b551-7">. <em>Florida v. Jimeno, </em><span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#251" aria-description="Citation for case: Florida v. Jimeno">500 U.S. 248, 251</a></span>, <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">111 S.Ct. 1801</a></span>, <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">114 L.Ed.2d 297</a></span> (1991).</p>
</footnote>
<footnote label="49">
<p id="b551-8">. <em>See State v. Bagby, </em><span class="citation" data-id="2170730"><a href="/opinion/2170730/state-v-bagby/#450" aria-description="Citation for case: State v. Bagby">119 S.W.3d 446, 450</a></span> (Tex.App.-Tyler 2003, no pet.) (officer's entry into appellee's shed was expressly limited in scope by appellee to officer’s inspection of the firearms to determine if they had been recently discharged; continuation of search of shed after inspection was finished — resulting in discovery of methamphetamine — violated scope of consent).</p>
</footnote>
<footnote label="50">
<p id="b551-9">. <span class="citation" data-id="1370428"><a href="/opinion/1370428/valtierra-v-state/#451" aria-description="Citation for case: Valtierra v. State">310 S.W.3d 442, 451-52</a></span> (Tex.Crim.App.2010).</p>
</footnote>
<footnote label="51">
<p id="b551-14">
<em>.Id.</em>
</p>
</footnote>
<footnote label="52">
<p id="b551-12">. <em><span class="citation" data-id="1370428"><a href="/opinion/1370428/valtierra-v-state/" aria-description="Citation for case: Valtierra v. State">Id.</a></span></em></p>
</footnote>
<footnote label="53">
<p id="b551-13">. <em>Accord Baldwin v. State, </em><span class="citation" data-id="9627668"><a href="/opinion/1427878/baldwin-v-state/#372" aria-description="Citation for case: Baldwin v. State">278 S.W.3d 367, 372</a></span> (Tex.Crim.App.2009) ("Deputy Smith believed that appellant's answer to a question regarding the location of his identification constituted permission to retrieve that identification. We find this belief to be <em>objectively unreasonable. </em>Appellant’s response was simply an answer to the officer’s question (after being handcuffed) and not a consent for the officer to search his person.”) (emphasis added).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/State v. Wint.md  (`case`, 5 assertions)

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
{"assertion_id": "15aa03918603c894", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "236 N.J. 174 (2018)", "court": "N.J. 2018", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "198 A.3d 963", "title": "State v. Wint", "year": "2018"}}
{"assertion_id": "579e1acaee6cbba4", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A suspect's six months of continuous pre-indictment custody is not a 'break in custody' under Maryland v. Shatzer, so the Edwards bar on police-initiated reinterrogation after an invocation of counsel remained in force; because none of the three exceptions — counsel provided, defendant-initiated communication, or a break in custody — applied, a later Mirandized waiver could not validate the interrogation and the incriminating statements had to be suppressed.", "title": "State v. Wint"}}
{"assertion_id": "5f544054545f78b4", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key", "title": "State v. Wint"}}
{"assertion_id": "0e4e3832ccddfb98", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Persuasive — state, illustrative", "title": "State v. Wint"}}
{"assertion_id": "59138d73197ff689", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "State v. Wint", "varies_by_point": "false"}}
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

## GROUP: content/cases/Steele v. United States.md  (`case`, 5 assertions)

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
{"assertion_id": "82fd1c8ccb08940e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "267 U.S. 498 (1925)", "court": "U.S. Supreme Court", "neutral_cite": "1925 U.S. LEXIS 386", "official_citation_present": true, "parallel_cite": "45 S. Ct. 414; 69 L. Ed. 757", "title": "Steele v. United States", "year": "1925"}}
{"assertion_id": "0031ea198ddd1c6a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A warrant satisfies the Fourth Amendment's particularity-of-place requirement if its description is such that the executing officer can, with reasonable effort, ascertain and identify the place intended to be searched.", "title": "Steele v. United States"}}
{"assertion_id": "943e11a240bc5d02", "dimension": "support", "kind": "home_role", "locator": {"home": "Particularity"}, "payload": {"home": "Particularity", "role": "Progeny", "title": "Steele v. United States"}}
{"assertion_id": "05d59aa192460345", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1925-04-13", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Steele v. United States", "field_i_validity": "good_law", "scope_note": "Controlling and canonical: the particularity-of-place requirement is satisfied if an officer can, with reasonable effort, ascertain and identify the place intended.", "title": "Steele v. United States", "varies_by_point": "false"}}
{"assertion_id": "dbf181fb7bd1eb22", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Steele v. United States"}}
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

## GROUP: content/cases/Stoner v. California.md  (`case`, 5 assertions)

### content_page

```
---
title: "Stoner v. California"
type: case
citation: "376 U.S. 483 (1964)"
parallel_cite: "84 S. Ct. 889; 11 L. Ed. 2d 856"
neutral_cite: 1964 U.S. LEXIS 1579
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1964
date_decided: 1964-05-18
docket: 209
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1964-03-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Stoner v. California
  varies_by_point: false
  scope_note: "Good law. Later apparent-authority doctrine (Illinois v. Rodriguez) permits searches on an officer's reasonable belief in a consenter's authority, but a hotel clerk still lacks authority to consent to a current guest's room; Stoner remains good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106777/stoner-v-california/"
  cluster_id: 106777
  opinion_id: 106777
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Progeny (third-party consent / apparent authority)"
related: ["[[Chapman v. United States (1961)]]", "[[Illinois v. Rodriguez]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent", "third-party-consent", "apparent-authority", "hotel"]
holding: "A hotel desk clerk cannot give valid third-party consent to a police search of a current guest's room; a guest retains Fourth Amendment protection that only the guest may waive, and unrealistic notions of 'apparent authority' do not validate the search."
lake:
  record_id: Stoner v. California
  status: verified
  projected_at: 2026-07-06
---

# Stoner v. California

*376 U.S. 483 (1964)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating an armed robbery, police traced the petitioner to the Mayfair Hotel. Without a warrant, they asked the night clerk for Stoner's room and, on the clerk's statement that Stoner was out and his offer of "permission," had the clerk unlock Room 404 and let them in ("Be my guest"). Officers searched the room and seized eyeglasses, a jacket, and a pistol used at trial to convict Stoner of robbery.

## Issue
Whether a hotel desk clerk's consent can authorize a warrantless police search of a guest's rented room consistent with the Fourth Amendment.

## Rule
No. A hotel guest enjoys full Fourth Amendment protection in the room. "No less than a tenant of a house, or the occupant of a room in a boarding house, … a guest in a hotel room is entitled to constitutional protection against unreasonable searches and seizures. That protection would disappear if it were left to depend upon the unfettered discretion of an employee of the hotel." — 376 U.S. at 490. ^pin-490

That protection is the guest's alone to waive, and cannot be conjured from agency law: "the rights protected by the Fourth Amendment are not to be eroded by strained applications of the law of agency or by unrealistic doctrines of 'apparent authority.'" — *Id.* at 488. ^pin-488

The right "only the petitioner could waive by word or deed, either directly or through an agent," and there was "nothing in the record to indicate that the police had any basis whatsoever to believe that the night clerk had been authorized by the petitioner" to permit a search. — *Id.* at 489. ^pin-489

## Application
The clerk "clearly and unambiguously consented," but the consent was legally irrelevant: the constitutional right was Stoner's, not the clerk's or the hotel's. A guest impliedly permits maids or repairmen to enter for their duties, but not police to conduct a criminal search; and the police had no basis to think the clerk was the guest's authorized agent. The warrantless search therefore violated the Fourth Amendment.

## Conclusion
The hotel clerk could not consent to the search of Stoner's room; the search was unlawful and the conviction was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The later apparent-authority rule of [[Illinois v. Rodriguez]] (1990) validates a search where officers reasonably (if mistakenly) believe the consenter has authority — but a hotel clerk has neither actual nor reasonably-[[Consent Searches|apparent authority]] over a current guest's room, so *Stoner* remains good law and is taught alongside [[Chapman v. United States (1961)]] (landlord) as the core third-party-consent limit.

## Appears on
- [[Consent Searches]] — *Progeny ([[Consent Searches|third-party consent]] / [[Consent Searches|apparent authority]])*

## Sources
- *Stoner v. California*, 376 U.S. 483 (1964) — https://www.courtlistener.com/opinion/106777/stoner-v-california/ — pinpoints: 488, 489, 490.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d435c1dbcccf1235", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "376 U.S. 483 (1964)", "court": "U.S. Supreme Court", "neutral_cite": "1964 U.S. LEXIS 1579", "official_citation_present": true, "parallel_cite": "84 S. Ct. 889; 11 L. Ed. 2d 856", "title": "Stoner v. California", "year": "1964"}}
{"assertion_id": "0e0fbc19b50a9521", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A hotel desk clerk cannot give valid third-party consent to a police search of a current guest's room; a guest retains Fourth Amendment protection that only the guest may waive, and unrealistic notions of 'apparent authority' do not validate the search.", "title": "Stoner v. California"}}
{"assertion_id": "cabdde6ecf1222dd", "dimension": "support", "kind": "home_role", "locator": {"home": "Consent Searches"}, "payload": {"home": "Consent Searches", "role": "Progeny (third-party consent / apparent authority)", "title": "Stoner v. California"}}
{"assertion_id": "68ccd25f85f3c687", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1964-03-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Stoner v. California", "field_i_validity": "good_law", "scope_note": "Good law. Later apparent-authority doctrine (Illinois v. Rodriguez) permits searches on an officer's reasonable belief in a consenter's authority, but a hotel clerk still lacks authority to consent to a current guest's room; Stoner remains good law.", "title": "Stoner v. California", "varies_by_point": "false"}}
{"assertion_id": "73e3016711c919cf", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Stoner v. California"}}
```

### lake record — Stoner v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Stoner v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Stoner v. California",
    "case_name_short": "Stoner",
    "case_name_full": "Stoner v. California",
    "input_case_name": "Stoner v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1964-05-18",
    "year": 1964,
    "docket": "209",
    "cluster_id": 106777,
    "lead_opinion_id": 106777,
    "sibling_ids": [
      106777,
      9422755,
      9422756
    ],
    "absolute_url": "/opinion/106777/stoner-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "376 U.S. 483",
      "volume": "376",
      "reporter": "U.S.",
      "page": "483",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "84 S. Ct. 889",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "889",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "11 L. Ed. 2d 856",
        "volume": "11",
        "reporter": "L. Ed. 2d",
        "page": "856",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1964 U.S. LEXIS 1579",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "1579",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "376 U.S. 483",
        "volume": "376",
        "reporter": "U.S.",
        "page": "483",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 S. Ct. 889",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "889",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "11 L. Ed. 2d 856",
        "volume": "11",
        "reporter": "L. Ed. 2d",
        "page": "856",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1964 U.S. LEXIS 1579",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "1579",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "376 U.S. 483",
    "official_selection": {
      "court_class": "scotus",
      "selected": "376 U.S. 483",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-490",
      "page": null,
      "quote": "). Officers searched the room and seized eyeglasses, a jacket, and a pistol used at trial to convict Stoner of robbery. ## Issue Whether a hotel desk clerk's consent can authorize a warrantless police search of a guest's rented room consistent with the Fourth Amendment. ## Rule No. A hotel guest enjoys full Fourth Amendment protection in the room.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-488",
      "page": null,
      "quote": "the rights protected by the Fourth Amendment are not to be eroded by strained applications of the law of agency or by unrealistic doctrines of 'apparent authority.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-489",
      "page": null,
      "quote": "only the petitioner could waive by word or deed, either directly or through an agent,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1964-03-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Stoner v. California",
    "varies_by_point": false,
    "scope_note": "Good law. Later apparent-authority doctrine (Illinois v. Rodriguez) permits searches on an officer's reasonable belief in a consenter's authority, but a hotel clerk still lacks authority to consent to a current guest's room; Stoner remains good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Gatto",
          "cluster_id": 10133498,
          "cite": [
            "304 Or. App. 210",
            "466 P.3d 981"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Owens",
          "cluster_id": 4425178,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Hillary Lee Tyler",
          "cluster_id": 2820149,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Hillary Lee Tyler",
          "cluster_id": 2812907,
          "cite": [
            "867 N.W.2d 136",
            "2015 Iowa Sup. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Joshua Daniel Fleming",
          "cluster_id": 4472496,
          "cite": [
            "790 N.W.2d 560",
            "2010 Iowa Sup. LEXIS 110"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kareem Jamal Currence",
          "cluster_id": 794165,
          "cite": [
            "446 F.3d 554",
            "2006 U.S. App. LEXIS 11090",
            "2006 WL 1172337"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gibson",
          "cluster_id": 3975410,
          "cite": [
            "164 Ohio App. 3d 558",
            "2005 Ohio 6380",
            "843 N.E.2d 224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Piedad Barajas-Avalos, AKA Opinion Piedad Barajas-Avaslos",
          "cluster_id": 785295,
          "cite": [
            "359 F.3d 1204",
            "2004 U.S. App. LEXIS 4569",
            "2004 D.A.R. 3084"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Katz v. United States",
          "cluster_id": 107564,
          "cite": [
            "19 L. Ed. 2d 576",
            "88 S. Ct. 507",
            "389 U.S. 347",
            "1967 U.S. LEXIS 2"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
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
        "journal_ref": "Stoner v. California:lane2_top_cited"
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
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gilbert v. California",
          "cluster_id": 107487,
          "cite": [
            "18 L. Ed. 2d 1178",
            "87 S. Ct. 1951",
            "388 U.S. 263",
            "1967 U.S. LEXIS 1086"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Matlock",
          "cluster_id": 108967,
          "cite": [
            "39 L. Ed. 2d 242",
            "94 S. Ct. 988",
            "415 U.S. 164",
            "1974 U.S. LEXIS 8"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Camara v. Municipal Court of City and County of San Francisco",
          "cluster_id": 107473,
          "cite": [
            "18 L. Ed. 2d 930",
            "87 S. Ct. 1727",
            "387 U.S. 523",
            "1967 U.S. LEXIS 1254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
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
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Opperman",
          "cluster_id": 109537,
          "cite": [
            "49 L. Ed. 2d 1000",
            "96 S. Ct. 3092",
            "428 U.S. 364",
            "1976 U.S. LEXIS 15"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warden, Maryland Penitentiary v. Hayden",
          "cluster_id": 107465,
          "cite": [
            "18 L. Ed. 2d 782",
            "87 S. Ct. 1642",
            "387 U.S. 294",
            "1967 U.S. LEXIS 2753"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Linkletter v. Walker",
          "cluster_id": 107084,
          "cite": [
            "14 L. Ed. 2d 601",
            "85 S. Ct. 1731",
            "381 U.S. 618",
            "1965 U.S. LEXIS 2283",
            "5 Ohio Misc. 49",
            "33 Ohio Op. 2d 118"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Rodriguez",
          "cluster_id": 112475,
          "cite": [
            "111 L. Ed. 2d 148",
            "110 S. Ct. 2793",
            "497 U.S. 177",
            "1990 U.S. LEXIS 3295",
            "58 U.S.L.W. 4892"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Carney",
          "cluster_id": 111423,
          "cite": [
            "85 L. Ed. 2d 406",
            "105 S. Ct. 2066",
            "471 U.S. 386",
            "1985 U.S. LEXIS 8",
            "53 U.S.L.W. 4521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Desist v. United States",
          "cluster_id": 107875,
          "cite": [
            "22 L. Ed. 2d 248",
            "89 S. Ct. 1030",
            "394 U.S. 244",
            "1969 U.S. LEXIS 2159"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
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
        "journal_ref": "Stoner v. California:lane2_top_cited"
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
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Greenwood",
          "cluster_id": 112067,
          "cite": [
            "100 L. Ed. 2d 30",
            "108 S. Ct. 1625",
            "486 U.S. 35",
            "1988 U.S. LEXIS 2279",
            "56 U.S.L.W. 4409"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vale v. Louisiana",
          "cluster_id": 108183,
          "cite": [
            "26 L. Ed. 2d 409",
            "90 S. Ct. 1969",
            "399 U.S. 30",
            "1970 U.S. LEXIS 18"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Johnson",
          "cluster_id": 110754,
          "cite": [
            "73 L. Ed. 2d 202",
            "102 S. Ct. 2579",
            "457 U.S. 537",
            "1982 U.S. LEXIS 134",
            "50 U.S.L.W. 4742"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Edwards",
          "cluster_id": 108995,
          "cite": [
            "39 L. Ed. 2d 771",
            "94 S. Ct. 1234",
            "415 U.S. 800",
            "1974 U.S. LEXIS 120"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jenkins",
          "cluster_id": 1195356,
          "cite": [
            "997 P.2d 1044",
            "95 Cal. Rptr. 2d 377",
            "22 Cal. 4th 900"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mancusi v. DeForte",
          "cluster_id": 107745,
          "cite": [
            "20 L. Ed. 2d 1154",
            "88 S. Ct. 2120",
            "392 U.S. 364",
            "1968 U.S. LEXIS 3075",
            "68 L.R.R.M. (BNA) 2449"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maxwell v. State",
          "cluster_id": 2105782,
          "cite": [
            "73 S.W.3d 278",
            "2002 Tex. Crim. App. LEXIS 84",
            "2002 WL 562264"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Peltier",
          "cluster_id": 109302,
          "cite": [
            "45 L. Ed. 2d 374",
            "95 S. Ct. 2313",
            "422 U.S. 531",
            "1975 U.S. LEXIS 155"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "G. M. Leasing Corp. v. United States",
          "cluster_id": 109579,
          "cite": [
            "50 L. Ed. 2d 530",
            "97 S. Ct. 619",
            "429 U.S. 338",
            "1977 U.S. LEXIS 33",
            "39 A.F.T.R.2d (RIA) 475"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ross",
          "cluster_id": 1060457,
          "cite": [
            "49 S.W.3d 833",
            "2001 Tenn. LEXIS 563",
            "2001 WL 760100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106777 OR 9422755 OR 9422756) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDQ3NjAwMDAwMDAwJnM9MTI5ODU1MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106777+OR+9422755+OR+9422756%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(106777 OR 9422755 OR 9422756)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDAmcz0xMTc0OTc0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106777+OR+9422755+OR+9422756%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106777 OR 9422755 OR 9422756)",
        "reviewed": 11,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 11,
        "triage_read": 0,
        "triage_snippet_classified": 11
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106777 OR 9422755 OR 9422756)",
    "indexed_citing_opinions": 1038,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106777,
        "count": 963,
        "count_source": "search"
      },
      {
        "opinion_id": 9422755,
        "count": 93,
        "count_source": "search"
      },
      {
        "opinion_id": 9422756,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1576,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/stoner-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc3MzAzODUmcz02NDY0MzQ2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106777+OR+9422755+OR+9422756%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106777,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 104713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 106699,
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
    "date_created": "2026-07-05T21:03:18Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:03:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:03:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:06:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:03:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Stoner v. California

```
<div>
<center><b><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">376 U.S. 483</a></span> (1964)</b></center>
<center><h1>STONER<br>
v.<br>
CALIFORNIA.</h1></center>
<center>No. 209.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 25, 1964.</center>
<center>Decided March 23, 1964.</center>
CERTIORARI TO THE DISTRICT COURT OF APPEAL OF CALIFORNIA, SECOND APPELLATE DISTRICT.
<p><i>William H. Dempsey, Jr.,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./375/805/">375 U. S. 805</a></span>, argued the cause and filed briefs for petitioner.</p>
<p><i>Arlo E. Smith,</i> Chief Assistant Attorney General of California, argued the cause for respondent. With him on the brief were <i>Stanley Mosk,</i> Attorney General of California, and <i>Albert W. Harris, Jr.</i> and <i>Michael J. Phelan,</i> Deputy Attorneys General.</p>
<p><i>A. L. Wirin, Fred Okrand</i> and <i>Paul Cooksey</i> filed a brief for the American Civil Liberties Union of Southern California, as <i>amicus curiae,</i> urging reversal.</p>
<p><span class="star-pagination">*484</span> MR. JUSTICE STEWART delivered the opinion of the Court.</p>
<p>The petitioner was convicted of armed robbery after a jury trial in the Superior Court of Los Angeles County, California. At the trial several articles which had been found by police officers in a search of the petitioner's hotel room during his absence were admitted into evidence over his objection. A District Court of Appeal of California affirmed the conviction,<sup>[1]</sup> and the Supreme Court of California denied further review.<sup>[2]</sup> We granted certiorari, limiting review "to the question of whether evidence was admitted which had been obtained by an unlawful search and seizure." <span class="citation multiple-matches"><a href="/c/U.%20S./374/826/">374 U. S. 826</a></span>. For the reasons which follow, we conclude that the petitioner's conviction must be set aside.</p>
<p>The essential facts are not in dispute. On the night of October 25, 1960, the Budget Town Food Market in Monrovia, California, was robbed by two men, one of whom was described by eyewitnesses as carrying a gun and wearing horn-rimmed glasses and a grey jacket. Soon after the robbery a checkbook belonging to the petitioner was found in an adjacent parking lot and turned over to the police. Two of the stubs in the checkbook indicated that checks had been drawn to the order of the Mayfair Hotel in Pomona, California. Pursuing this lead, the officers learned from the Police Department of Pomona that the petitioner had a previous criminal record, and they obtained from the Pomona police a photograph of the petitioner. They showed the photograph to the two eyewitnesses to the robbery, who both stated that the picture looked like the man who had carried the gun. On the basis of this information the officers went to the Mayfair Hotel in Pomona at about 10 <span class="star-pagination">*485</span> o'clock on the night of October 27. They had neither search nor arrest warrants. There then transpired the following events, as later recounted by one of the officers:</p>
<blockquote>"We approached the desk, the night clerk, and asked him if there was a party by the name of Joey L. Stoner living at the hotel. He checked his records and stated `Yes, there is.' And we asked him what room he was in. He stated he was in Room 404 but he was out at this time.</blockquote>
<blockquote>"We asked him how he knew that he was out. He stated that the hotel regulations required that the key to the room would be placed in the mail box each time they left the hotel. The key was in the mail box, that he therefore knew he was out of the room.</blockquote>
<blockquote>"We asked him if he would give us permission to enter the room, explaining our reasons for this.</blockquote>
<blockquote>"Q. What reasons did you explain to the clerk?</blockquote>
<blockquote>"A. We explained that we were there to make an arrest of a man who had possibly committed a robbery in the City of Monrovia, and that we were concerned about the fact that he had a weapon. He stated `In this case, I will be more than happy to give you permission and I will take you directly to the room.'</blockquote>
<blockquote>"Q. Is that what the clerk told you?</blockquote>
<blockquote>"A. Yes, sir.</blockquote>
<blockquote>"Q. What else happened?</blockquote>
<blockquote>"A. We left one detective in the lobby, and Detective Oliver, Officer Collins, and myself, along with the night clerk, got on the elevator and proceeded to the fourth floor, and went to Room 404. The night clerk placed a key in the lock, unlocked the door, and says, `Be my guest.' "</blockquote>
<p>The officers entered and made a thorough search of the room and its contents. They found a pair of hornrimmed <span class="star-pagination">*486</span> glasses and a grey jacket in the room, and a .45-caliber automatic pistol with a clip and several cartridges in the bottom of a bureau drawer. The petitioner was arrested two days later in Las Vegas, Nevada. He waived extradition and was returned to California for trial on the charge of armed robbery. The gun, the cartridges and clip, the horn-rimmed glasses, and the grey jacket were all used as evidence against him at his trial.</p>
<p>The search of the petitioner's room by the police officers was conducted without a warrant of any kind, and it therefore "can survive constitutional inhibition only upon a showing that the surrounding facts brought it within one of the exceptions to the rule that a search must rest upon a search warrant. <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499</a></span>; <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span>." <i>Rios</i> v. <i>United States,</i> <span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/#261" aria-description="Citation for case: Rios v. United States">364 U. S. 253, 261</a></span>. The District Court of Appeal thought the search was justified as an incident to a lawful arrest.<sup>[3]</sup> But a search can be incident to an arrest only if it is substantially contemporaneous with the arrest and is confined to the immediate vicinity of the arrest. <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span>.<sup>[4]</sup><span class="star-pagination">*487</span> Whatever room for leeway there may be in these concepts,<sup>[5]</sup> it is clear that the search of the petitioner's hotel room in Pomona, California, on October 27 was not incident to his arrest in Las Vegas, Nevada, on October 29. The search was completely unrelated to the arrest, both as to time and as to place. See <i>Preston</i> v. <i>United States,</i> decided this day, <i>ante,</i> p. 364.</p>
<p>In this Court the respondent has recognized that the reasoning of the California District Court of Appeal cannot be reconciled with our decision in <i><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">Agnello</a></span>,</i> nor, indeed, with the most recent California decisions.<sup>[6]</sup> Accordingly, the respondent has made no argument that the search can be justified as an incident to the petitioner's arrest. Instead, the argument is made that the search of the hotel room, although conducted without the petitioner's consent, was lawful because it was conducted <span class="star-pagination">*488</span> with the consent of the hotel clerk. We find this argument unpersuasive.</p>
<p>Even if it be assumed that a state law which gave a hotel proprietor blanket authority to authorize the police to search the rooms of the hotel's guests could survive constitutional challenge, there is no intimation in the California cases cited by the respondent that California has any such law.<sup>[7]</sup> Nor is there any substance to the claim that the search was reasonable because the police, relying upon the night clerk's expressions of consent, had a reasonable basis for the belief that the clerk had authority to consent to the search. Our decisions make clear that the rights protected by the Fourth Amendment are not to be eroded by strained applications of the law of agency or by unrealistic doctrines of "apparent authority." As this Court has said,</p>
<blockquote>"it is unnecessary and ill-advised to import into the law surrounding the constitutional right to be free from unreasonable searches and seizures subtle distinctions, developed and refined by the common law in evolving the body of private property law which, more than almost any other branch of law, has been shaped by distinctions whose validity is largely historical.. . . [W]e ought not to bow to them in the fair administration of the criminal law. To do so would not comport with our justly proud claim of the procedural protections accorded to those charged with crime." <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#266" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 266-267</a></span>.</blockquote>
<p><span class="star-pagination">*489</span> It is important to bear in mind that it was the petitioner's constitutional right which was at stake here, and not the night clerk's nor the hotel's. It was a right, therefore, which only the petitioner could waive by word or deed, either directly or through an agent. It is true that the night clerk clearly and unambiguously consented to the search. But there is nothing in the record to indicate that the police had any basis whatsoever to believe that the night clerk had been authorized by the petitioner to permit the police to search the petitioner's room.</p>
<p>At least twice this Court has explicitly refused to permit an otherwise unlawful police search of a hotel room to rest upon consent of the hotel proprietor. <i>Lustig</i> v. <i>United States,</i> <span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/" aria-description="Citation for case: Lustig v. United States">338 U. S. 74</a></span>; <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span>. In <i><span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/" aria-description="Citation for case: Lustig v. United States">Lustig</a></span></i> the manager of a hotel allowed police to enter and search a room without a warrant in the occupant's absence, and the search was held unconstitutional. In <i><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Jeffers</a></span></i> the assistant manager allowed a similar search, and that search was likewise held unconstitutional.</p>
<p>It is true, as was said in <i><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Jeffers</a></span>,</i> that when a person engages a hotel room he undoubtedly gives "implied or express permission" to "such persons as maids, janitors or repairmen" to enter his room "in the performance of their duties." <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S., at 51</a></span>. But the conduct of the night clerk and the police in the present case was of an entirely different order. In a closely analogous situation the Court has held that a search by police officers of a house occupied by a tenant invaded the tenant's constitutional right, even though the search was authorized by the owner of the house, who presumably had not only apparent but actual authority to enter the house for some purposes, such as to "view waste." <i>Chapman</i> v. <i>United States,</i> <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span>. The Court pointed out that the officers' purpose in entering was not to view waste but to search for distilling equipment, and concluded that to uphold such a search without a warrant would leave <span class="star-pagination">*490</span> tenants' homes secure only in the discretion of their landlords.</p>
<p>No less than a tenant of a house, or the occupant of a room in a boarding house, <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>, a guest in a hotel room is entitled to constitutional protection against unreasonable searches and seizures. <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>. That protection would disappear if it were left to depend upon the unfettered discretion of an employee of the hotel. It follows that this search without a warrant was unlawful. Since evidence obtained through the search was admitted at the trial, the judgment must be reversed. <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>.<sup>[8]</sup></p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE HARLAN, concurring in part and dissenting in part.</p>
<p>I entirely agree with the Court's opinion, except as to its disposition of the case. I would remand the case to the California District Court of Appeal so that it may consider whether or not admission of the illegally seized evidence was harmless error. <i>Fahy</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422676"><a href="/opinion/106699/fahy-v-connecticut/" aria-description="Citation for case: Fahy v. Connecticut">375 U. S. 85</a></span>, does not require or justify the course which the Court takes. In <i><span class="citation" data-id="9422676"><a href="/opinion/106699/fahy-v-connecticut/" aria-description="Citation for case: Fahy v. Connecticut">Fahy</a></span>,</i> Connecticut at least had had the opportunity to decide the question of harmless error with respect to the illegally seized evidence there involved; <span class="star-pagination">*491</span> here California has had no such opportunity.<sup>[*]</sup> For this Court to decide that question as an original matter is, in my opinion, incompatible with proper federal-state relations.</p>
<p>Accordingly, I would vacate the judgment below and remand the case to the California courts for further appropriate proceedings.</p>
<h2>NOTES</h2>
<p>[1]  <span class="citation" data-id="2213895"><a href="/opinion/2213895/people-v-stoner/" aria-description="Citation for case: People v. Stoner">205 Cal. App. 2d 108</a></span>, <span class="citation" data-id="2213895"><a href="/opinion/2213895/people-v-stoner/" aria-description="Citation for case: People v. Stoner">22 Cal. Rptr. 718</a></span>.</p>
<p>[2]  <span class="citation" data-id="2213895"><a href="/opinion/2213895/people-v-stoner/#116" aria-description="Citation for case: People v. Stoner">205 Cal. App. 2d, at 116</a></span>.</p>
<p>[3]  The court reasoned that the officers had probable cause to arrest the petitioner prior to their entry into the hotel room; that they were not obliged to accept as true the night clerk's statement that the petitioner was not in his room; that "it may be reasonably inferred that they entered his room for the purpose of making an arrest," that their observation of the glasses in plain sight reasonably led them to a further search; and that in the circumstances the arrest and the search and seizure were "part of the same transaction." <span class="citation" data-id="2213895"><a href="/opinion/2213895/people-v-stoner/#113" aria-description="Citation for case: People v. Stoner">205 Cal. App. 2d 108, 113</a></span>, <span class="citation" data-id="2213895"><a href="/opinion/2213895/people-v-stoner/#722" aria-description="Citation for case: People v. Stoner">22 Cal. Rptr. 718, 722</a></span>.</p>
<p>[4]  "The right without a search warrant contemporaneously to search persons lawfully arrested while committing crime and to search the place where the arrest is made in order to find and seize things connected with the crime as its fruits or as the means by which it was committed, as well as weapons and other things to effect an escape from custody, is not to be doubted. See <i>Carroll</i> v. <i>United States.</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 158</a></span>; <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span>. . . . But the right does not extend to other places." <i>Id.,</i> at 30. See also <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#42" aria-description="Citation for case: Ker v. California">374 U. S. 23, 42, n. 13</a></span>; <i>Lustig</i> v. <i>United States,</i> <span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/#79" aria-description="Citation for case: Lustig v. United States">338 U. S. 74, 79-80</a></span>.</p>
<p>[5]  Although some members of this Court have expressed the view that the statement in <i><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">Agnello</a></span></i> defining the permissible bounds of a search incident to arrest went too far, see, <i>e. g., </i><i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#155" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 155, 183, 195</a></span> (dissenting opinions); <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#68" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 68</a></span> (dissenting opinion), the <i><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">Agnello</a></span></i> holding as to what may <i>not</i> be searcheda house substantially removed geographically from the place of arrest at a time not substantially contemporaneous with the arresthas never been questioned in this Court.</p>
<p>[6]  "[T]he search cannot be justified as incident to the arrest `for it was at a distance from the place thereof and was not contemporaneous therewith.' (Castaneda v. Superior Court, 59 A. C. 456, 459, <span class="citation" data-id="9559447"><a href="/opinion/1198462/castaneda-v-superior-court/#3" aria-description="Citation for case: Castaneda v. Superior Court">30 Cal. Rptr. 1, 3</a></span>, <span class="citation" data-id="9559447"><a href="/opinion/1198462/castaneda-v-superior-court/#643" aria-description="Citation for case: Castaneda v. Superior Court">380 P. 2d 641, 643</a></span>; Tompkins v. Superior Court, 59 A. C. 75, 77, <span class="citation" data-id="9533071"><a href="/opinion/1126066/tompkins-v-superior-court/" aria-description="Citation for case: Tompkins v. Superior Court">27 Cal. Rptr. 889</a></span>, <span class="citation" data-id="9533071"><a href="/opinion/1126066/tompkins-v-superior-court/" aria-description="Citation for case: Tompkins v. Superior Court">378 P. 2d 113</a></span>; People v. Gorg, <span class="citation" data-id="1359720"><a href="/opinion/1359720/people-v-gorg/#781" aria-description="Citation for case: People v. Gorg">45 Cal. 2d 776, 781</a></span>, <span class="citation" data-id="1359720"><a href="/opinion/1359720/people-v-gorg/" aria-description="Citation for case: People v. Gorg">291 P. 2d 469</a></span>.)" <i>People</i> v. <i>King,</i> <span class="citation" data-id="9791441"><a href="/opinion/2609262/people-v-king/#311" aria-description="Citation for case: People v. King">60 Cal. 2d 308, 311</a></span>, <span class="citation" data-id="9791441"><a href="/opinion/2609262/people-v-king/#826" aria-description="Citation for case: People v. King">32 Cal. Rptr. 825, 826</a></span>, <span class="citation" data-id="9791441"><a href="/opinion/2609262/people-v-king/#155" aria-description="Citation for case: People v. King">384 P. 2d 153, 155</a></span>.</p>
<p>[7]  See <i>Roberts</i> v. <i>Casey,</i> <span class="citation" data-id="1111698"><a href="/opinion/1111698/roberts-v-casey/" aria-description="Citation for case: Roberts v. Casey">36 Cal. App. 2d Supp. 767</a></span>, <span class="citation" data-id="1111698"><a href="/opinion/1111698/roberts-v-casey/" aria-description="Citation for case: Roberts v. Casey">93 P. 2d 654</a></span>; <i>Fox</i> v. <i>Windemere Hotel Apt. Co.,</i> <span class="citation" data-id="3293015"><a href="/opinion/3294337/fox-v-windemere-hotel-apartment-co/" aria-description="Citation for case: Fox v. Windemere Hotel Apartment Co.">30 Cal. App. 162</a></span>, <span class="citation" data-id="3293015"><a href="/opinion/3294337/fox-v-windemere-hotel-apartment-co/" aria-description="Citation for case: Fox v. Windemere Hotel Apartment Co.">157 P. 820</a></span>; <i>People</i> v. <i>Vaughan,</i> <span class="citation" data-id="1209992"><a href="/opinion/1209992/people-v-vaughan/" aria-description="Citation for case: People v. Vaughan">65 Cal. App. 2d Supp. 844</a></span>; <span class="citation" data-id="1209992"><a href="/opinion/1209992/people-v-vaughan/" aria-description="Citation for case: People v. Vaughan">150 P. 2d 964</a></span>. "The mere fact that a person is a hotel manager does not import an authority to permit the police to enter and search the rooms of her guests." <i>People</i> v. <i>Burke,</i> <span class="citation" data-id="2207511"><a href="/opinion/2207511/people-v-burke/#160" aria-description="Citation for case: People v. Burke">208 Cal. App. 2d 149, 160</a></span>, <span class="citation" data-id="2207511"><a href="/opinion/2207511/people-v-burke/#919" aria-description="Citation for case: People v. Burke">24 Cal. Rptr. 912, 919</a></span>.</p>
<p>[8]  The respondent has argued that the case should be remanded to let the California District Court of Appeal decide whether the admission of this evidence was harmless error. But the conviction depended in large part upon the jury's resolution of the question of the credibility of witnesses, and that determination must almost certainly have been influenced by the incriminating nature of the physical evidence illegally seized and erroneously admitted. There is thus at least "a reasonable possibility that the evidence complained of might have contributed to the conviction." <i>Fahy</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422676"><a href="/opinion/106699/fahy-v-connecticut/#86" aria-description="Citation for case: Fahy v. Connecticut">375 U. S. 85, 86</a></span>.</p>
<p>[*]  The evidence against the accused included a confession of the crime charged. This Court refused to review the claim, contained in the petition for certiorari, that this confession had been involuntarily made. <span class="citation multiple-matches"><a href="/c/U.%20S./374/826/">374 U. S. 826</a></span>, <i>ante,</i> p. 484.</p>

</div>
```

---
