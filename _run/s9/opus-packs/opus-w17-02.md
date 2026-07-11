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

## GROUP: _overhaul2/lake/cases/United States v. Kolsuz.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Kolsuz
type: case
citation: "890 F.3d 133 (2018)"
parallel_cite: ""
neutral_cite: ""
court: 4th Cir. 2018
court_level: coa
circuit: ca4
year: 2018
date_decided: 2018-05-18
docket: 16-4687
authority_weight: "Binding in-circuit — 4th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4499413/united-states-v-hamza-kolsuz/"
  cluster_id: 4499413
  opinion_id: null
  identity_checked: false
lake:
  record_id: United States v. Kolsuz
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Border Searches]]"
    role: Key
related:
  - "[[Border Searches]]"
  - "[[Riley v. California]]"
  - "[[United States v. Aigbekaen]]"
  - "[[United States v. Montoya de Hernandez]]"
tags:
  - case
  - fourth-amendment
  - border-search
  - forensic-search
  - cell-phone
  - digital-privacy
  - reasonable-suspicion
  - good-faith-exception
  - fourth-circuit
holding: "The Fourth Circuit held that a month-long off-site forensic examination of a smartphone seized at an international airport is a border search, but that under Riley it is a nonroutine border search requiring at least individualized suspicion — while expressly reserving whether reasonable suspicion suffices or a probable-cause warrant is required — and affirmed the denial of suppression under the good-faith exception because the agents reasonably relied on precedent holding that no warrant was required."
---

# United States v. Kolsuz

*890 F.3d 133 (4th Cir. 2018)* (No. 16-4687) · U.S. Court of Appeals for the Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 4499413 → opinion 4276666 (890 F.3d 133, decided 2018-05-09, amended 2018-05-18); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Hamza Kolsuz was detained at Washington Dulles International Airport while trying to board a flight to Turkey after customs agents found firearms parts in his luggage. Agents arrested him, seized his smartphone, and subjected it to a **month-long, off-site forensic analysis** that produced a nearly 900-page report cataloguing the phone's data. The district court denied Kolsuz's motion to suppress, applying the Fourth Amendment's border-search exception and holding that the forensic examination was a **nonroutine** border search justified by reasonable suspicion. Kolsuz was convicted of attempting to smuggle firearms out of the country and a related conspiracy count, and appealed the suppression ruling.

## Issue
Whether the off-site forensic analysis of Kolsuz's smartphone was a border search at all once he and the phone were in custody, and, if so, whether under *[[Riley v. California]]* the weighty privacy interest in smartphone data requires more than reasonable suspicion — a warrant based on probable cause — to conduct a forensic border search of a phone.

## Rule
At the border or its functional equivalent, agents may conduct **routine** searches without a warrant or any individualized suspicion, but **nonroutine, highly intrusive** searches require individualized suspicion. Reading that framework together with *[[Riley v. California|Riley]]*'s recognition that digital devices hold a uniquely vast and private trove of data, the court classified a forensic phone search as nonroutine: "We also agree with the district court that under *Riley*, the forensic examination of Kolsuz's phone must be considered a nonroutine border search, requiring some measure of individualized suspicion." — 890 F.3d 133, slip op. at 4. ^pin-op4

## Application
The forensic analysis remained a **border search** despite the temporal and spatial distance between the off-site examination and Kolsuz's airport interception — the justification for the border exception was broad enough to reach it. And under *[[Riley v. California|Riley]]*, that forensic examination was **nonroutine**, requiring individualized suspicion rather than qualifying as a suspicionless routine inspection. The court expressly declined to decide **what** that standard must be — reasonable suspicion, as the district court held, or a probable-cause warrant, as Kolsuz urged — because the question was not outcome-determinative: the agents reasonably relied on precedent holding that no warrant was required, so under the [[The Good-Faith Exception|good-faith exception]] suppression would be inappropriate even if the court disagreed on the standard.

## Conclusion
**Affirmed.** Judge Harris wrote for the court, joined by Judge Motz; Judge Wilkinson concurred in the judgment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Kolsuz* is the Fourth Circuit's foundational digital-border-search holding: forensic device searches at the border are **nonroutine** and demand at least individualized suspicion under *[[Riley v. California|Riley]]*, though the court reserved whether reasonable suspicion or a warrant is required. The circuit soon supplied the missing piece in *[[United States v. Aigbekaen|Aigbekaen]]* (2019), which added a **border-nexus** limit. Frame *Kolsuz* within the unresolved circuit split over forensic device searches (Ninth and Fourth Circuits requiring suspicion; Eleventh requiring none) — never as a settled nationwide device rule.

## Appears on
- [[Border Searches]] — *Key*

## Sources
- [*United States v. Kolsuz*, 890 F.3d 133 (4th Cir. 2018)](https://www.courtlistener.com/opinion/4499413/united-states-v-hamza-kolsuz/) — pinpoint: slip op. at 4 (forensic-device-search-is-nonroutine holding; the CL opinion text is slip-paginated, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "68ab4d1d4b4a1714", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Kolsuz"}, "payload": {"all": [{"cite": "890 F.3d 133", "page": "133", "reporter": "F.3d", "selected_official": true, "source": "web-dual-leg", "type": 1, "volume": "890"}], "display": "890 F.3d 133", "official": {"cite": "890 F.3d 133", "page": "133", "reporter": "F.3d", "selected_official": true, "source": "web-dual-leg", "type": 1, "volume": "890"}, "official_selection_present": true, "record_id": "United States v. Kolsuz"}}
{"assertion_id": "a264e562ab0e45c1", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Kolsuz"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Kolsuz", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Kolsuz

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Kolsuz",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Hamza Kolsuz",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Kolsuz",
    "court": "4th Cir. 2018",
    "court_id": "ca4",
    "court_level": "coa",
    "circuit": "ca4",
    "state": null,
    "date_decided": "2018-05-18",
    "year": 2018,
    "docket": "16-4687",
    "cluster_id": 4499413,
    "lead_opinion_id": 4276666,
    "sibling_ids": [],
    "absolute_url": "/opinion/4499413/united-states-v-hamza-kolsuz/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "890 F.3d 133",
      "volume": "890",
      "reporter": "F.3d",
      "page": "133",
      "type": 1,
      "selected_official": true,
      "source": "web-dual-leg"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "890 F.3d 133",
        "volume": "890",
        "reporter": "F.3d",
        "page": "133",
        "type": 1,
        "selected_official": true,
        "source": "web-dual-leg"
      }
    ],
    "display": "890 F.3d 133",
    "official_selection": {
      "court_class": "coa",
      "selected": "890 F.3d 133",
      "reason": "web-dual-leg"
    },
    "web_legs": [
      {
        "source": "Google Scholar",
        "url": "https://scholar.google.com/scholar_case?case=150597407311153261",
        "cite": "890 F.3d 133",
        "checked_date": "2026-07-07"
      },
      {
        "source": "FindLaw",
        "url": "https://caselaw.findlaw.com/us-4th-circuit/1895857.html",
        "cite": "890 F.3d 133",
        "checked_date": "2026-07-07"
      }
    ]
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
    "date_created": "2026-07-06T05:54:09Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:54:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:54:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:54:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:54:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-kolsuz--4499413",
      "to_record_id": "United States v. Kolsuz",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Kolsuz

```
                                     PUBLISHED

                      UNITED STATES COURT OF APPEALS
                          FOR THE FOURTH CIRCUIT


                                      No. 16-4687


UNITED STATES OF AMERICA,

                    Plaintiff-Appellee,

      v.

HAMZA KOLSUZ,

                    Defendant-Appellant.


Appeal from the United States District Court for the Eastern District of Virginia, at
Alexandria. T.S. Ellis, III, District Judge. (1:16-cr-00053-TSE)


Argued: October 26, 2017                                        Decided: May 9, 2018
                               Amended: May 18, 2018


Before WILKINSON, MOTZ, and HARRIS, Circuit Judges.


Affirmed by published opinion. Judge Harris wrote the opinion, in which Judge Motz
joined. Judge Wilkinson wrote a separate opinion concurring in the judgment.


ARGUED: Todd M. Richman, OFFICE OF THE FEDERAL PUBLIC DEFENDER,
Alexandria, Virginia, for Appellant. Jeffrey Michael Smith, National Security Division,
UNITED STATES DEPARTMENT OF JUSTICE, Washington, D.C., for Appellee.
Esha Bhandari, AMERICAN CIVIL LIBERTIES UNION, New York, New York, for
Amici American Civil Liberties Union, ACLU of Virginia, ACLU of Maryland, ACLU
of North Carolina, ACLU of South Carolina, and ACLU of West Virginia. ON BRIEF:
Geremy C. Kamens, Federal Public Defender, OFFICE OF THE FEDERAL PUBLIC
DEFENDER, Alexandria, Virginia, for Appellant. Dana Boente, United States Attorney,
Mary B. McCord, Acting Assistant Attorney General for National Security, Heather
Alpino, UNITED STATES DEPARTMENT OF JUSTICE, Washington, D.C., for
Appellee.      Hope R. Amezquita, AMERICAN CIVIL LIBERTIES UNION
FOUNDATION OF VIRGINIA, Richmond, Virginia, Nathan Freed Wessler, Vera
Eidelman, AMERICAN CIVIL LIBERTIES UNION FOUNDATION, New York, New
York, for Amici American Civil Liberties Union, ACLU of Virginia, ACLU of
Maryland, ACLU of North Carolina, ACLU of South Carolina, and ACLU of West
Virginia. Curt Levey, THE COMMITTEE FOR JUSTICE, Washington, D.C., Erica L.
Marshall, CAUSE OF ACTION INSTITUTE, Washington, D.C., for Amici Cause of
Action Institute, The Committee for Justice, and Floor64, Inc. Sophia Cope, Adam
Schwartz, ELECTRONIC FRONTIER FOUNDATION, San Francisco, California, for
Amici Electronic Frontier Foundation, Asian Americans Advancing Justice-Asian Law
Caucus, Council on American-Islamic Relations (CAIR), CAIR California, CAIR
Florida, CAIR Missouri, CAIR New York, CAIR Ohio, CAIR Dallas/Fort Worth, and
The National Association of Criminal Defense Lawyers. Michael Price, BRENNAN
CENTER FOR JUSTICE AT NYU SCHOOL OF LAW, New York, New York, for
Amicus Brennan Center for Justice.




                                       2
PAMELA HARRIS, Circuit Judge:

      Hamza Kolsuz was detained at Washington Dulles International Airport while

attempting to board a flight to Turkey because federal customs agents found firearms

parts in his luggage. After arresting Kolsuz, the agents took possession of his smartphone

and subjected it to a month-long, off-site forensic analysis, yielding a nearly 900-page

report cataloguing the phone’s data.     The district court denied Kolsuz’s motion to

suppress, applying the Fourth Amendment’s border search exception and holding that the

forensic examination was a nonroutine border search justified by reasonable suspicion.

Kolsuz ultimately was convicted of attempting to smuggle firearms out of the country

and an associated conspiracy charge.

      Kolsuz now challenges the denial of his suppression motion. First, he argues that

the forensic analysis of his phone should not have been treated as a border search at all.

According to Kolsuz, once both he and his phone were in government custody, the

government interest in preventing contraband from crossing the border was no longer

implicated, so the border exception should no longer apply. Second, relying chiefly on

Riley v. California, 134 S. Ct. 2473 (2014) (holding that search incident to arrest

exception does not apply to searches of cell phones), Kolsuz urges that the privacy

interest in smartphone data is so weighty that even under the border exception, a forensic

search of a phone requires more than reasonable suspicion, and instead may be conducted

only with a warrant based on probable cause.

      We agree with the district court that the forensic analysis of Kolsuz’s phone is

properly categorized as a border search.        Despite the temporal and spatial distance

                                            3
between the off-site analysis of the phone and Kolsuz’s attempted departure at the airport,

the justification for the border exception is broad enough to reach the search in this case.

We also agree with the district court that under Riley, the forensic examination of

Kolsuz’s phone must be considered a nonroutine border search, requiring some measure

of individualized suspicion. What precisely that standard should be – whether reasonable

suspicion is enough, as the district court concluded, or whether there must be a warrant

based on probable cause, as Kolsuz suggests – is a question we need not resolve:

Because the agents who conducted the search reasonably relied on precedent holding that

no warrant was required, suppression of the report would be inappropriate even if we

disagreed. Accordingly, we affirm the judgment of the district court.



                                             I.

                                            A.

       We begin with the Fourth Amendment principles that govern this case. As a

general rule, the Fourth Amendment requires that law enforcement searches be

accompanied by a warrant based on probable cause. Arizona v. Gant, 556 U.S. 332, 338

(2009). But there are exceptions, and one such exception typically covers our nation’s

borders. At a border – or at a border’s “functional equivalent,” like the international

airport at which Kolsuz was intercepted – government agents may conduct “routine”

searches and seizures of persons and property without a warrant or any individualized

suspicion. Almeida-Sanchez v. United States, 413 U.S. 266, 272–73 (1973); United

States v. Montoya de Hernandez, 473 U.S. 531, 538 (1985). The Supreme Court has

                                             4
described the border exception as “grounded in the recognized right of the sovereign to

control, subject to substantive limitations imposed by the Constitution, who and what

may enter the country.” United States v. Ramsey, 431 U.S. 606, 620 (1977); see United

States v. Flores-Montano, 541 U.S. 149, 152 (2004) (border exception rests on

government interest in “preventing the entry of unwanted persons and effects”). Routine

searches and seizures at the border therefore are exempted from standard Fourth

Amendment requirements so that the government can “prevent the introduction of

contraband” into the country and bar entry by those who would bring harm across the

border, “whether that be communicable diseases, narcotics, or explosives.” Montoya de

Hernandez, 473 U.S. at 537, 544.

      In this case, the search in question was initiated when Kolsuz attempted to exit the

country, not to enter. But we have long held that the rationales underlying the border

exception extend to exit as well as entry searches. See United States v. Oriakhi, 57 F.3d

1290, 1296–97 (4th Cir. 1995). The “fundamental principles of national sovereignty”

that are the basis for the border search exception, we have explained, apply equally to

government efforts to “protect[] and monitor[] exports from the country” as they do to

efforts to control imports. Id. at 1296, 1297. Thus, with respect to exit searches, the

border search exception is justified by the government’s power to regulate the export of

currency and other goods. Id. at 1297. And that power surely extends to controls on the

exports of dangerous weapons, like the firearms parts at issue here. See, e.g., United

States v. Boumelhem, 339 F.3d 414, 422–23 (6th Cir. 2003) (applying border exception to

exit search of shipping container believed to hold smuggled firearms).

                                            5
       Even at the border, however, the government’s authority is not without limits. The

“ultimate touchstone” of the Fourth Amendment, Riley, 134 S. Ct. at 2482, remains

“reasonableness.” See Montoya de Hernandez, 473 U.S. at 538. While suspicionless

border searches generally are “reasonable simply by virtue of the fact that they occur at

the border,” Ramsey, 431 U.S. at 616, the Supreme Court also has recognized a category

of “nonroutine” border searches that are constitutionally reasonable only if based on

individualized suspicion. See Montoya de Hernandez, 473 U.S. at 541 (holding that

overnight detention for monitored bowel movement followed by rectal examination is

“beyond the scope of a routine customs search” and permissible under the border

exception only with reasonable suspicion). Such nonroutine border searches, the Court

has suggested, include “highly intrusive searches” that implicate especially significant

“dignity and privacy interests,” as well as destructive searches of property and searches

carried out in “particularly offensive” manners. Flores-Montano, 541 U.S. at 152, 154 &

n.2.

                                           B.

       In January 2016, Turkish citizen Hamza Kolsuz entered the United States in

Miami, Florida, on a tourist visa. By that time, Kolsuz already was well known to

government authorities. In December 2012, agents had discovered 163 firearms parts in

his luggage when Kolsuz checked in for a flight to Turkey at John F. Kennedy

International Airport in New York. The parts were listed on the United States Munitions

List (“USML”), subjecting them to export controls and a license requirement under the

Arms Export Control Act, 22 U.S.C. § 2778(b)(2). See 22 C.F.R. §§ 120.2, 121.1 (setting

                                           6
out USML, and defining “defense articles and defense services” subject to control under

the Act). Agents explained the licensing requirements to Kolsuz and his companions,

and ultimately seized the weapons parts. Just one month later, in January 2013, the

process more or less repeated itself: Kolsuz arrived at JFK Airport for a flight to Turkey;

a search of his checked luggage revealed firearms parts; and a licensing determination

disclosed that although the parts were listed on the USML, Kolsuz had not obtained the

requisite export license.

       When Kolsuz reentered the country on January 25, 2016, the authorities were

ready for him. On February 1, 2016, Charles Reich, a Special Agent with United States

Customs and Border Protection (“CBP”) in New York, reached out to CBP officers on

duty at Washington Dulles International Airport (“Dulles”) to let them know that Kolsuz,

who had been stopped before while attempting to smuggle firearms parts out of the

country, would be traveling from Dulles to Turkey the following day. Agent Reich urged

the officers to search Kolsuz’s luggage for firearms parts, and followed up with an email

containing additional information and a list of questions to ask Kolsuz about his

associates and activities.

       On February 2, 2016, Kolsuz began his return trip by checking in at Miami

International Airport for a series of flights that would take him through Dulles and on to

Turkey. When Kolsuz and his luggage reached Dulles, CBP officers Lauren Colgan and




                                            7
Jonathan Budd conducted an outbound customs examination of his two checked bags. 1

Once again, they found multiple firearms parts: 18 handgun barrels, 22 9mm handgun

magazines, four .45 caliber handgun magazines, and one .22 caliber conversion kit.

Colgan and Budd, thanks to their training, immediately recognized that the barrels and

conversion kit were listed on the USML and thus could not be removed from the country

without a license. And when Kolsuz was stopped on the jetway as he attempted to board

his flight to Turkey, he admitted that he was in possession of firearms parts for which he

did not have a federal license.

       After transporting Kolsuz to a secondary inspection area, the officers conducted

what would be the first of two searches of Kolsuz’s iPhone 6 Plus. This search – often

referred to as a “manual” search – involved using the iPhone’s touch screen, which was

not password protected, to scroll through Kolsuz’s recent calls and text messages. The

officers also confirmed through a records search that Kolsuz had no export license or

pending application for a license. After an interview with a number of CBP officers,

Kolsuz was arrested.

       At that point, CBP Special Agent Adam Coppolo initiated the second search of

Kolsuz’s phone, this one commonly known as a “forensic” search.             Coppolo first

transported the phone approximately four miles from Dulles to the Homeland Security


       1
         Kolsuz never has suggested that this standard customs search of his checked
luggage presents any constitutional problem. Nor could he: It is long established that a
search of luggage taken from or bound for an overseas flight is a routine border search
that may be conducted on a suspicionless basis. See Montoya de Hernandez, 473 U.S. at
538; see also, e.g., United States v. Ezeiruaku, 936 F.2d 136, 140–41 (3d Cir. 1991).

                                            8
Investigations office in Sterling, Virginia. There, Computer Forensic Agent Michael Del

Vacchio attached the phone to a Cellebrite Physical Analyzer, which extracts data from

electronic devices, and conducted an advanced logical file system extraction. The phone

remained in airplane mode throughout, so the forensic examination did not reach data

stored remotely – or “in the cloud” – and was instead limited to data stored on the phone

itself. Even so, the data extraction process lasted for a full month, and yielded an 896-

page report that included Kolsuz’s personal contact lists, emails, messenger

conversations, photographs, videos, calendar, web browsing history, and call logs, along

with a history of Kolsuz’s physical location down to precise GPS coordinates.

                                                C.

      Kolsuz was indicted on three counts: (i) attempting to export firearms parts on the

USML without a license, in violation of the Arms Export Control Act, 22 U.S.C. §§

2278(b) and (c); (ii) attempting to smuggle goods from the United States in violation of

18 U.S.C. § 554(a); and (iii) conspiracy to commit those offenses, in violation of 18

U.S.C. § 371.

      Before trial, Kolsuz filed a motion to suppress the report generated by the forensic

examination of his phone, arguing primarily that the border exception did not apply to the

search. According to Kolsuz, a forensic search of a phone that occurs miles away from

an airport and for a month after an attempted departure does not constitute a “border

search.” Moreover, Kolsuz contended, the rationales justifying the border exception were

not implicated in this case, because at the time of the search there was no prospect that

either he or his phone – both securely in government custody – would be crossing the

                                            9
border. Instead, Kolsuz argued, the forensic search should be treated as a search incident

to his arrest, and under Riley v. California, cell phones may be searched incident to arrest

only with a warrant based on probable cause.

       In a comprehensively reasoned opinion, the district court denied Kolsuz’s

suppression motion. United States v. Kolsuz, 185 F. Supp. 3d 843, 860 (E.D. Va. 2016).

The court held first that the forensic search of Kolsuz’s phone was properly evaluated as

a border search. That Kolsuz had been arrested, the district court explained, did not

transform the forensic examination into a search incident to arrest or render the border

exception inapplicable; both the Fourth Circuit and other courts have held that a border

search may be conducted after a traveler is arrested and no longer in a position to cross

the border. Id. at 851 (citing United States v. Ickes, 393 F.3d 501, 507 (4th Cir. 2005)).

Similarly, the court found, it is well established that a search initiated at the border may

fall under the border exception even if it ultimately is conducted off-site and over a long

period of time. Id. at 851–52.

       Now applying the border exception, the district court went on to consider whether

the forensic search of Kolsuz’s smartphone was a routine border search, subject to no

Fourth Amendment requirements, or whether, as Kolsuz urged, it was a nonroutine

search that required some degree of individualized suspicion. The court acknowledged

that in Ickes, the Fourth Circuit treated as routine a border inspection of a computer’s

contents, accessed manually “in the same way a typical user would” and without any

“sophisticated forensic analysis.” Id. at 853 (citing Ickes, 393 F.3d at 502–03). But that

decision, the court determined, “does not address whether more sophisticated forensic

                                            10
searches” also may be classified as routine, id. at 854, particularly in light of the Supreme

Court’s subsequent decision in Riley and its emphasis on the significant privacy interests

in the digital contents of phones.

       The court concluded that while the manual search of Kolsuz’s iPhone at the airport

was a routine border search, 2 the off-site forensic analysis of the phone’s data qualified as

a nonroutine search. After Riley, the court found, a forensic search of a phone no longer

can be analogized to an ordinary search of luggage or some other container at the border,

given the breadth and sensitivity of the private information that may be uncovered. It is

“difficult to conceive of a property search more invasive or intrusive than a sophisticated,

digital search of a cell phone,” the court concluded, which might be compared to a “body

cavity search” of a phone. Id. at 856 (quoting United States v. Saboonchi, 990 F. Supp.

2d 536, 569 (D. Md. 2014)).

       As a nonroutine border search, the court went on to hold, the forensic analysis of

Kolsuz’s phone required particularized suspicion, in the form of the familiar reasonable

suspicion standard. The court rejected the more demanding requirement of a warrant

based on probable cause, noting that no reported case has held a border search to that

standard. Instead, courts consistently have deemed reasonable suspicion sufficient to


       2
         Although the district court addressed this initial search in the course of its
reasoning, Kolsuz’s suppression motion is limited to the subsequent forensic
examination. On appeal, Kolsuz expressly disclaims any challenge to the manual search
of his phone at Dulles, which in any event did not reveal information used against him at
trial.




                                             11
justify even the most intrusive of nonroutine border searches, including body cavity and

alimentary canal searches.     Because the government in this case had “more than

reasonable suspicion” that a forensic examination of Kolsuz’s phone would reveal

evidence of both past and ongoing attempts to export firearms parts illegally, the court

concluded, the forensic search was reasonable under the Fourth Amendment. Id. at 859,

860.

       The parties consented to a bench trial, and the district court found Kolsuz guilty of

all three counts against him. In finding that Kolsuz acted with the requisite willfulness,

the court relied in part on messages Kolsuz exchanged with a co-conspirator, obtained

from the forensic search of Kolsuz’s phone. 3 The court ultimately entered judgment only

on the Arms Export Control Act and conspiracy counts against Kolsuz, dismissing the

smuggling charge on the government’s motion. Kolsuz was sentenced to 30 months in

prison and three years of supervised release, and this timely appeal followed.



                                                 II.

       Kolsuz’s appeal is a narrow one, and we begin by clarifying what is and is not in

front of us today. First, Kolsuz does not challenge the manual search of his smartphone,

undertaken on-site at the airport as he tried to depart for Turkey. We thus have no


       3
         The court also adopted an independent willful blindness theory, under which it
was “unnecessary to rely” on the messages recovered from Kolsuz’s phone. J.A. 243
n.34. As the government recognizes, however, that theory does not apply to the
conspiracy charge of which Kolsuz was convicted, and thus does not provide an
alternative basis for affirming the district court judgment in full.

                                            12
occasion to consider application of the border exception to manual searches of electronic

devices, conducted at the border and roughly contemporaneously with an attempted

crossing.   Cf. United States v. Molina-Isidoro, 884 F.3d 287, 289 (5th Cir. 2018)

(sustaining manual search of phone at border under good-faith exception to Fourth

Amendment exclusionary rule).

      Nor does Kolsuz challenge the seizure of his phone, either initially at the airport or

later at the Homeland Security Investigations office where it was forensically examined.

The Fourth Amendment protects property as well as privacy, see Flores-Montano, 541

U.S. at 154, and a seizure reasonable at its inception must remain reasonable in scope and

duration to satisfy the Fourth Amendment, see Montoya de Hernandez, 473 U.S. at 541–

42. But perhaps because he was in custody while the government undertook its month-

long forensic analysis, Kolsuz has not asserted any impairment of a possessory interest in

his phone. Accordingly, we do not address whether and under what circumstances an

extended confiscation of a traveler’s phone – quite apart from any search undertaken –

might constitute an unreasonable seizure of property for Fourth Amendment purposes.

Cf. Saboonchi, 990 F. Supp. 2d at 569 (noting that forensic searches of digital devices

may deprive individuals of their possessions for periods of days or weeks).

      That leaves the question that is raised by this appeal: whether the forensic search

of Kolsuz’s phone, and the associated invasion of Kolsuz’s privacy, was justified under

the border search exception. In considering the district court’s denial of Kolsuz’s motion

to suppress, we review that court’s legal conclusions de novo and its factual findings for

clear error, considering the evidence in the light most favorable to the government. See

                                            13
United States v. Palmer, 820 F.3d 640, 648 (4th Cir. 2016). For the reasons given below,

we affirm.

                                            A.

       Kolsuz’s primary argument is that the forensic analysis of his phone was not

subject to the border search exception at all. Once he was arrested and his phone seized

and transported miles from the airport, Kolsuz contends, the government interest that

underlies the border search exception – preventing contraband from crossing a border –

was no longer at issue, and the border exception was therefore inapplicable. Rather,

standard Fourth Amendment rules governed the forensic search, and required a warrant

based on probable cause because the search was incident to Kolsuz’s arrest. See Riley,

134 S. Ct. at 2485, 2493–94 (holding that the search incident exception does not apply to

cell phones, which generally may be searched incident to arrest only with probable cause

and a warrant). We cannot agree.

       First, as the district court explained, the border exception is not rendered

inapplicable because a search initiated at a border ultimately is conducted at some

physical or temporal remove. See Kolsuz, 185 F. Supp. 3d at 851–52 (“as several courts

have held, an off-site forensic search of an electronic device over a long period of time is

nonetheless a border search”); see also, e.g., United States v. Cotterman, 709 F.3d 952,

961–62 (9th Cir. 2013) (en banc) (applying border exception to forensic examination of

laptop computer conducted miles from and days after attempted border crossing);

Saboonchi, 990 F. Supp. 2d at 548–49, 561 (applying border exception to forensic search

of cell phones conducted several hundred miles from border crossing). Indeed, after

                                            14
pressing this point before the district court, Kolsuz concedes it on appeal, agreeing that

the location and timing of the search in this case are consistent with the border search

exception.

       Nor, as the district court determined, does the fact of Kolsuz’s arrest transform the

examination of his phone into a search incident to arrest, triggering Riley and calling for a

search warrant based on probable cause. In Ickes, our court applied the border search

exception to approve a manual search of computer data that occurred only after the

defendant had been arrested, obviating any threat of an imminent border crossing. See

393 F.3d at 503; see also, e.g., United States v. Ramos, 190 F. Supp. 3d 992, 998–1000

(S.D. Cal. 2016) (rejecting argument that arrest renders border exception inapplicable by

making it impossible for defendant or contraband to cross border). Kolsuz attempts to

distinguish Ickes on the ground that it involved an entry search rather than the exit search

at issue here, but for these purposes, it makes no difference: As we have explained,

where the relevant governmental interests are present, the border search exception

extends equally to entry and exit searches, see Oriakhi, 57 F.3d at 1296–97, and any rule

carving out post-arrest searches from that doctrine would apply equally in both contexts,

as well.

       In its strongest form, Kolsuz’s argument combines all of these factors – his arrest

as he sought to depart the country, the phone in government custody miles from the

border, the month-long gap between the action at the airport and the end of the search –

and argues that taken together, they show that the search in this case is entirely

“untethered” from any justification behind the border exception. The rationale allowing

                                             15
outgoing border searches, as Kolsuz describes it, is limited to intercepting contraband as

it crosses the national border. Here, with the phone as well as the firearms parts seized

by the government and Kolsuz under arrest, there was no contraband poised to exit the

country and thus no nexus to that rationale. When that is the case, Kolsuz argues, the

border search exception does not apply, because the concerns underlying a warrant

exception “define the boundaries of the exception.” See Gant, 566 U.S. at 339.

       Kolsuz’s foundational premise is correct: As a general rule, the scope of a warrant

exception should be defined by its justifications. See Riley, 134 S. Ct. at 2484–88 (asking

whether “application of the search incident to arrest doctrine to this particular category of

effects would untether the rule from the justifications underlying the [search incident to

arrest] exception”). As a result, where the government interests underlying a Fourth

Amendment exception are not implicated by a certain type of search, and where the

individual’s privacy interests outweigh any ancillary governmental interests, the

government must obtain a warrant based on probable cause. See id. At some point, in

other words, even a search initiated at the border could become so attenuated from the

rationale for the border search exception that it no longer would fall under that exception.

See Molina-Isidoro, 884 F.3d at 295–97 (Costa, J., concurring) (questioning whether

search for evidence as opposed to contraband is consistent with justifications for border

search exception).

       But this is not that case. On the facts here, the link between the search of Kolsuz’s

phone and the interest that justifies border searches was sufficient to trigger the border

exception on any account of a “nexus” requirement. Government agents forensically

                                             16
searched Kolsuz’s phone because they had reason to believe – and good reason to

believe, in the form of two suitcases filled with firearms parts – that Kolsuz was

attempting to export firearms illegally and without a license. See Kolsuz, 185 F. Supp. 3d

at 859–60. That is a transnational offense that goes to the heart of the border search

exception, which rests in part on “the sovereign interest of protecting and monitoring

exports from the country.” See Oriakhi, 57 F.3d at 1297; see also Boumelhem, 339 F.3d

at 423 (holding that exit search for firearms implicates “significant government interests”

not only in controlling exports but also in national security). This is not a case, in other

words, in which the government invokes the border exception on behalf of its generalized

interest in law enforcement and combatting crime. Cf. United States v. Vergara, 884

F.3d 1309, 1317 (11th Cir. 2018) (Jill Pryor, J., dissenting) (relying on “general law

enforcement justification” to approve evidentiary border searches would “untether the

[border search exception] from its justifications”). Here, there is a direct link between the

predicate for the search and the rationale for the border exception.

       Moreover, as the district court explained, the agents who searched Kolsuz’s phone

reasonably believed that their search would reveal not only evidence of the export

violation they already had detected, but also “information related to other ongoing

attempts to export illegally various firearms parts.” Kolsuz, 185 F. Supp. 3d at 860. The

government emphasizes that finding – not contested by Kolsuz – in its argument before

us, and properly so. The justification behind the border search exception is broad enough

to accommodate not only the direct interception of contraband as it crosses the border,

but also the prevention and disruption of ongoing efforts to export contraband illegally,

                                             17
through searches initiated at the border. See, e.g., Ramos, 190 F. Supp. 3d at 999

(approving post-arrest “investigatory” border search of cell phone for information about

larger smuggling organization and “more contraband entering into the country at that

time”); United States v. Mendez, 240 F. Supp. 3d 1005, 1007–10 (D. Ariz. 2017)

(approving post-arrest border search of cell phone for evidence of additional contraband

entering country); cf. United States v. Kim, 103 F. Supp. 3d 32, 44, 46, 59 (D.D.C. 2015)

(holding unreasonable forensic search of laptop at border where search was expected to

reveal evidence of past but not ongoing criminal activity).

       In the circumstances presented here, we agree with the government’s bottom line:

Because the forensic search of Kolsuz’s phone was conducted at least in part to uncover

information about an ongoing transnational crime – in particular, information about

additional illegal firearms exports already underway, by freight or in the custody of a

coconspirator, see Kolsuz, 185 F. Supp. 3d at 860 – it “fits within the core of the

rationale” underlying the border search exception. Brief of United States at 19–20.

                                            B.

       Most of Kolsuz’s appeal is devoted to his argument against application of the

border exception. But Kolsuz has a fallback position, as well: Even under the border

exception, Kolsuz contends, the forensic search of his phone constituted a nonroutine

border search “unsupported by the type of reasonable suspicion required to justify” such

searches. Defendant’s Brief at 31. Again, we disagree.




                                            18
                                             1.

       Like the district court, we begin by considering the first premise of Kolsuz’s

argument: that the forensic search of his cell-phone data qualifies as a nonroutine border

search, requiring some level of particularized suspicion. We agree with the district court

that particularly in light of the Supreme Court’s decision in Riley, a forensic border

search of a phone must be treated as nonroutine, permissible only on a showing of

individualized suspicion. See Kolsuz, 185 F. Supp. 3d at 852–58.

       As described above, the Supreme Court has held that even at the border,

individualized suspicion is necessary to justify certain “highly intrusive searches,” in

light of the significance of the individual “dignity and privacy interests” infringed.

Flores-Montano, 541 U.S. at 152. Beyond that general guidance, the Court has not

delineated precisely what makes a search nonroutine. Compare id. at 155 (removal and

disassembly of car’s gas tank does not qualify as nonroutine border search) with Montoya

de Hernandez, 473 U.S. at 541–42 (16-hour detention for monitored bowel movement

pending rectal examination is nonroutine). But as the district court ably explains, in

deciding whether a search rises to the level of nonroutine, courts have focused primarily

on how deeply it intrudes into a person’s privacy. Kolsuz, 185 F. Supp. 3d at 853. Under

that approach, border searches of luggage, outer clothing, and personal effects

consistently are treated as routine, while searches that are most invasive of privacy – strip

searches, alimentary-canal searches, x-rays, and the like – are deemed nonroutine and

permitted only with reasonable suspicion. See id. at 853 & n.14 (citing cases).



                                             19
       By that metric, even before the Supreme Court issued its 2014 decision in Riley,

there was a convincing case for categorizing forensic searches of digital devices as

nonroutine. See Cotterman, 709 F.3d at 963–68 (holding that forensic examination of

computer is nonroutine border search requiring reasonable suspicion); Saboonchi, 990 F.

Supp. 2d at 549–60 (same as to smartphones and flash drives). First is the matter of

scale: The sheer quantity of data stored on smartphones and other digital devices dwarfs

the amount of personal information that can be carried over a border – and thus subjected

to a routine border search – in luggage or a car. “The average 400-gigabyte laptop hard

drive can store over 200 million pages. . . . Even a car full of packed suitcases with

sensitive documents cannot hold a candle to the sheer, and ever-increasing, capacity of

digital storage.” Cotterman, 709 F.3d at 964. Subjected to comprehensive forensic

analysis, a digital device can reveal an unparalleled breadth of private information.

       The uniquely sensitive nature of that information matters, as well. Smartphones

and laptops “contain the most intimate details of our lives: financial records, confidential

business documents, medical records and private emails,” id., and also may provide

access to data stored remotely, id. at 965. 4 The report generated by the month-long

logical file system extraction of data from Kolsuz’s phone is a case in point, revealing

896 pages’ worth of sensitive data including personal contacts, photographs, web


       4
          The forensic search of Kolsuz’s phone, which remained in airplane mode
throughout, did not extend to information stored remotely (“in the cloud”), nor to residual
data of files that had been deleted by Kolsuz. Kolsuz, 185 F. Supp. 3d at 849 & n.8. Like
the district court, however, we decline “to distinguish an extensive forensic search of a
cell phone from a very extensive forensic search of a cell phone.” Id. at 857.

                                            20
browsing history, and a “history of [Kolsuz’s] physical location down to precise GPS

coordinates,” J.A. 94 – the kind of information that, analyzed cumulatively, “generates a

precise, comprehensive record of a person’s public movements that reflects a wealth of

detail about her familial, political, professional, religious and sexual associations.” See

United States v. Jones, 565 U.S. 400, 415 (2012) (Sotomayor, J., concurring). And

finally, while an international traveler can mitigate the intrusion occasioned by a routine

luggage search by leaving behind her diaries, photographs, and other especially personal

effects, the same is not true, at least practically speaking, when it comes to smartphones

and digital devices. Portable electronic devices are ubiquitous – for many, the most

reliable means of contact when abroad – and it is neither “realistic nor reasonable to

expect the average traveler to leave his digital devices at home when traveling.”

Saboonchi, 990 F. Supp. 2d at 556.

       And then came Riley, in which the Supreme Court confirmed every particular of

that assessment. Riley holds that the search incident to arrest exception, which allows for

automatic searches of personal effects in the possession of an arrestee, does not apply to

manual searches of cell phones. 134 S. Ct. at 2493–94. The key to Riley’s reasoning is

its express refusal to treat such phones as just another form of container, like the wallets,

bags, address books, and diaries covered by the search incident exception. See id. at

2488–90.    Instead, Riley insists, cell phones are fundamentally different “in both a

quantitative and a qualitative sense” from other objects traditionally subject to

government searches. Id. at 2489. And that is so, Riley explains, for precisely the

reasons already identified by cases treating border searches of digital devices as

                                             21
nonroutine: the “immense storage capacity” of cell phones, putting a vastly larger array

of information at risk of exposure, id.; the special sensitivity of the kinds of information

that may be stored on a phone, such as browsing history and historical location data, id. at

2490; and, finally, the “element of pervasiveness that characterizes cell phones,” id.,

making them an “insistent part of daily life,” id. at 2484.

       After Riley, we think it is clear that a forensic search of a digital phone must be

treated as a nonroutine border search, requiring some form of individualized suspicion.

See Kolsuz, 185 F. Supp. 3d at 858; see also United States v. Saboonchi, 48 F. Supp. 3d

815, 819 (D. Md. 2014) (“Saboonchi II”) (discussing ways in which Riley confirms prior

holding that border searches of digital devices are nonroutine). Indeed, the impact of

Riley is plain enough that the government’s brief does not seriously contest this point,

focusing instead on the argument (which we next address) that nonroutine or not, the

search of Kolsuz’s phone was justified under the border exception. 5 We also note that

shortly after argument in this case, the Department of Homeland Security adopted a

policy that treats forensic searches of digital devices as nonroutine border searches,

insofar as such searches now may be conducted only with reasonable suspicion of

       5
         The government does note that in Ickes, 393 F.3d at 505–07, our court treated a
search of a computer as a routine border search, requiring no individualized suspicion for
the search. But as the district court explained, Ickes approved a manual, on-site
inspection of computer contents that would be accessible to any user, and did not address
the use of the sophisticated forensic search methods at issue here. Kolsuz, 185 F. Supp.
3d at 853–54; see also Saboonchi, 990 F. Supp. 2d at 546 (distinguishing Ickes on same
ground). Because Kolsuz does not challenge the initial manual search of his phone at
Dulles, we have no occasion here to consider whether Riley calls into question the
permissibility of suspicionless manual searches of digital devices at the border.


                                             22
activity that violates the customs laws or in cases raising national security concerns. U.S.

Customs and Border Prot., CBP Directive No. 3340-049A, Border Search of Electronic

Devices 5 (2018). That the agency has chosen to adopt these requirements, of course,

does not establish that they are constitutionally mandated. Cf. Ickes, 393 F.3d at 507

(distinguishing between agency practice and constitutional requirements). But it does

suggest, as courts have anticipated, that the distinction between manual and forensic

searches is a perfectly manageable one, see Cotterman, 709 F.3d at 967 (categorizing

forensic searches as nonroutine requires only “that officers make a commonsense

differentiation between a manual review of files on an electronic device and application

of computer software to analyze a hard drive”), and that treating forensic phone searches

as nonroutine need not interfere unduly with the agency’s protective mission at the

border, see Saboonchi, 990 F. Supp. 2d at 570. 6

                                             2.

       That the forensic analysis of Kolsuz’s phone data qualifies as a nonroutine border

search does not resolve this case. Nonroutine searches are permitted under the border


       6
         The new policy does not use the “routine” and “nonroutine” terminology of
Supreme Court case law, distinguishing instead between “basic” and “advanced”
searches. But the import is the same. “Basic” searches (like those we term “manual”) are
examinations of an electronic device that do not entail the use of external equipment or
software and may be conducted without suspicion. “Advanced” searches (like “forensic”
searches) involve the connection of external equipment to a device – such as the
Cellebrite Physical Analyzer used on Kolsuz’s phone – in order to review, copy, or
analyze its contents, and are subject to the restrictions noted above. See U.S. Customs
and Border Prot., CBP Directive No. 3340-049A, Border Search of Electronic Devices 4–
5 (2018); Molina-Isidoro, 884 F.3d at 294 & n.2 (Costa, J., concurring).


                                            23
exception, so long as they are accompanied by the appropriate level of individualized

suspicion. See Montoya de Hernandez, 473 U.S. at 540–41 & n.4.

      The district court concluded that under the border exception, the “highest level of

Fourth Amendment protection available” is the reasonable suspicion standard, which was

met in this case. 7 Kolsuz, 185 F. Supp. 3d at 858–59. As the district court explained,

courts consistently have required only reasonable suspicion even when reviewing the

most intrusive of nonroutine border searches and seizures – like, for instance, the one at

issue in Montoya de Hernandez, in which the Supreme Court held that with reasonable

suspicion, the government could detain a traveler thought to be smuggling contraband in

her alimentary canal for 16 hours while it monitored her bowel movements and sought a

court order for a rectal examination. Id. at 852–53, 858–59.

      Of course, certain searches conducted under exceptions to the warrant requirement

may require more than reasonable suspicion. See, e.g., California v. Carney, 471 U.S.

386, 393–95 (1985) (holding that automobile exception to the Fourth Amendment

permits a warrantless search of a motor home if based on probable cause). Perhaps the

      7
         Kolsuz also argues that even if the search of his phone could be justified by
reasonable suspicion, what would be required is reasonable suspicion that contraband, as
opposed to evidence, would be found on the device. Otherwise, according to Kolsuz, the
search would be “untethered” from the constitutional justification for border searches:
the interception of contraband as it crosses the border. If this argument sounds familiar,
that is because it is a reformulation of Kolsuz’s threshold argument against any
application of the border exception to this case, addressed above. And for essentially the
reasons already given, we cannot agree. The district court found – and Kolsuz does not
dispute – that the agents here had reason to believe that their search of Kolsuz’s phone
would reveal not only evidence of past export-control violations, but also evidence of
ongoing efforts to smuggle firearms over the border. Kolsuz, 185 F. Supp. 3d at 860.
That is enough to “tether” the search to the rationale behind the border exception.

                                           24
same is true of some nonroutine border searches, as Kolsuz argues, but we need not

resolve that question here. As the government reminds us, even if a search is judged to

be constitutionally flawed in some way, its fruits need not be suppressed if the agents

acted “in reasonable reliance on binding precedent.” Davis v. United States, 564 U.S.

229, 241 (2011); see United States v. Baker, 719 F.3d 313, 320–21 (4th Cir. 2013)

(describing Davis). In such circumstances, suppression can do little to deter police

misconduct, and the “social costs” of suppression – the exclusion from trial of reliable

evidence bearing on guilt or innocence – outweigh any deterrence benefits. Davis, 564

U.S. at 237–38.

      At the time the CBP officers conducted their forensic search of Kolsuz’s phone,

there was at least some case law indicating that reasonable suspicion might be required.

See Kolsuz, 185 F. Supp. 3d at 855–58 (discussing cases). But there was no case

suggesting that even more would be necessary – for a forensic search of a phone at the

border or, indeed, for any border search, no matter how nonroutine or invasive. And that

remains the case today: Even as Riley has become familiar law, there are no cases

requiring more than reasonable suspicion for forensic cell phone searches at the border.

But see Vergara, 884 F.3d at 1313–19 (Jill Pryor, J., dissenting) (after Riley, forensic

search of phone is not subject to border search exception and therefore requires warrant

based on probable cause).

      Under these circumstances, we think it was reasonable for the CBP officers who

conducted the forensic analysis of Kolsuz’s phone to rely on the established and uniform

body of precedent allowing warrantless border searches of digital devices that are based

                                          25
on at least reasonable suspicion. See Molina-Isidoro, 884 F.3d at 293 (applying good-

faith exception to warrantless manual search of phone at border). Under Davis’s “good-

faith” exception to the Fourth Amendment exclusionary rule, that reasonable reliance by

itself is enough to bar suppression of the evidence generated by the search. See Baker,

719 F.3d at 321. Accordingly, we need not – and will not – reach the issue of whether

more than reasonable suspicion is required for a search of this nature in affirming the

judgment of the district court.     See Molina-Isidoro, 884 F.3d at 294 (Costa, J.,

concurring) (reliance on good-faith exception particularly appropriate in area of rapid

legal and technological change).



                                           III.

      For the reasons given above, the judgment of the district court is

                                                                           AFFIRMED




                                           26
WILKINSON, Circuit Judge, concurring in the judgment:

       I thank the majority for its thoughtful opinion. While I agree with much of what is

said, my point of departure is quite basic. The majority appears to leave the legislative

and executive branches shivering in the cold. Those branches have a critical role to play

in defining the standards for a border search, and they are much better equipped than we

are to appreciate both the privacy interests at stake and the magnitude of the practical

risks involved.

       The standard of reasonableness in the particular context of a border search should

be principally a legislative question, not a judicial one. Congress should decide that

standard. Courts should apply it. This is a separation of powers approach that makes use

of the respective capabilities of all three branches of government, not just one.

       The infirmity of a constitutional rule in the unique context of a border search is

clear. Such a rule claims for courts the sole prerogative to set standards in an area where

legislative inquiry would be invaluable and where the executive maintains a strong

sovereign interest. Diminishing the other two branches flirts with real-life dangers. The

whole enterprise calls for the greatest caution and circumspection, not premature

declarations of constitutional rules.

       If individualized suspicion is to be required in order to conduct what the majority

asserts is a “nonroutine border search,” Maj. Op. at 4, then Congress must say so. And in

all events, there was plainly reasonable suspicion to conduct the search here. The

majority should have stopped right there. Assuming without deciding that reasonable

suspicion was even required, it is present here in triplicate.

                                              27
       Instead my colleagues wander from what Article III indisputably envisions as the

core role of courts: simply to decide a case or controversy. The majority turns

prescriptive, but the pronouncement here is too abstract and floats too far above the

realities at the border.

       Lethal capabilities are advancing at a rapid pace. Detection of destructive devices

is becoming more difficult. Nation states, terrorist bands, and individual arms merchants

see profit and prestige and power in joining the arms race. Might we wish to hear in a

manner more probing than appellate briefs and oral argument exactly what are the

dimensions of the threats we face? What makes us think the elective branches would

downgrade the significant privacy interests the majority rightly identifies? Might the

other two branches, if given a fair chance, have something to say? And do not Articles I

and II, which set forth the legislative and executive roles in matters of grave international

import, give them the right to say it? Who are we to propound the idea that democratic

bodies, where Fourth Amendment reasonableness is concerned, have nothing to

contribute?

       Alarmist? Hyperbolic? Perhaps. But if we so limit the role of our coordinate

branches with a constitutional ruling, how shall we ever know?

                                             I.

       The majority fairly recounts the facts here, and they are straightforward and

incriminating. Before his arrest at Dulles airport, Customs and Border Protection (CBP)

agents had twice stopped Kolsuz, a Turkish national, at JFK airport for carrying

contraband firearms parts proscribed by statute. See 22 U.S.C. § 2278. On both

                                             28
occasions, Kolsuz failed to produce the license required to export those parts. Both times,

CBP agents informed Kolsuz that he needed a license to export those items.

       Kolsuz reentered the United States on January 25, 2016, on a tourist visa. He again

purchased numerous gun parts. Law enforcement officials who were familiar with

Kolsuz’s previous attempts to export contraband firearms asked CBP to search Kolsuz’s

bags when he tried to return to Turkey. When Kolsuz arrived at Dulles, CBP searched his

bags. The inspection revealed eighteen handgun barrels, twenty-two 9 mm handgun

magazines, four .45 caliber handgun magazines, and one .22 caliber Glock conversion

kit. All of these firearms parts are restricted items on the U.S. Munitions List. At no time

did Kolsuz have permission to export them. Based on Kolsuz’s previous attempts to bring

firearm parts out of the country, CBP had ample reason to suspect that Kolsuz might

again try to export firearms.

       Following the search of Kolsuz’s bags, CBP officers interrogated Kolsuz and

performed a cursory inspection of his iPhone. At the end of the interrogation, Kolsuz was

arrested and his iPhone seized. At that point, his iPhone was transported to Sterling,

Virginia, where federal law enforcement conducted an “advanced logical file system

extraction” of the iPhone. This extraction, as the majority notes, generated an 896-page

report on the information contained in the phone.

                                            II.

       This was plainly a border search. See Maj. Op. at 18. Assuming reasonable

suspicion of Kolsuz’s criminal activity is somehow required, it clearly existed here. We

need go no further. Rather than deciding the case on solid and suitably limited grounds,

                                            29
the majority goes on to prescribe a constitutional standard whose rationale would label a

great many cell phone searches undertaken at the border as “nonroutine” and forbidden

absent prior individualized suspicion.

       While the majority purports not to reach the question of the justification required

for the manual search of Kolsuz’s cell phone at Dulles airport, see Maj. Op. at 22 n.5, the

rhetorical thrust of its opinion as concerns cell phones and smartphones may be read by

many courts to require individualized suspicion for border searches of all cell phones

period. Or if the majority intends a less sweeping standard, the slipperiness of the

distinction between intrusive and less intrusive cell phone searches and between those

that are routine and those that are nonroutine will lead, I fear, to difficulties in application

down the road. While the majority’s constitutional venture may be correct, it also may

well not be. Again, we are not the ones to set the standard.

       We are, each of us, in over our heads. We have no idea of the dangers we are

courting. JFK and Dulles are quintessential border posts. See Almeida-Sanchez v. United

States, 413 U.S. 266, 273 (1973). Thousands of international travelers go through them

every day. Yet the majority hardly grapples with how law enforcement is expected to

ascertain individualized suspicion when dealing with such numbers. The privacy interest,

while weighty, is the only side of a precarious balance that seems to concern the majority,

and this in the application of the Fourth Amendment, which articulates reasonableness

and hence balance as a standard. See Katz v. United States, 389 U.S. 347, 360 (1967).

       One would hope that rather than charging unnecessarily ahead, the majority would

recognize the need for congressional input, which the enunciation of constitutional

                                              30
standards makes more difficult. Constitutional standards are preemptive. They sweep all

other pieces off the board. Judicially promulgated constitutional standards say essentially,

“That’s that. The Constitution is the highest law, and the judiciary shall be its sole

guardian.”

       Empirical questions lie at the heart of the tension between privacy and security

interests at the border. How many people travel through international airports every day?

What screening techniques and investigative resources does government have available?

What materials are being smuggled in and out, and by whom? What practical obstacles

exist to individualized findings? What, in other words, is the magnitude of danger courted

by progressive step-ups of search requirements?

       The limited glimpse from a single case does no more than beg the question: What

is the reality of it all? This is why any Fourth Amendment standard is best designed here

through the more adaptable legislative process and the wider lens of legislative hearings.

See Riley v. California, 134 S. Ct. 2473, 2497-98 (2014) (Alito, J., concurring in the

judgment) (“Legislatures, elected by the people, are in a better position than we are to

assess and respond to the changes that have already occurred and those that almost

certainly will take place in the future.”). For “[a]s new technologies continue to appear in

the marketplace and outpace existing surveillance law, the primary job of evaluating their

impact on privacy rights and of updating the law must remain with the branch of

government designed to make such policy choices, the legislature.” In re Askin, 47 F.3d

100, 106 (4th Cir. 1995).



                                            31
       The majority contends that the “Department of Homeland Security adopted a

policy that treats forensic searches of digital devices as nonroutine border searches.” Maj.

Op. at 22. I think the document is more complex than this, but in all events, it proves my

point—that in this narrow area agency policy born of actual and ongoing experience is

more adaptable than a freeze-frame constitutional ruling.

       Courts too often assume Congress is desensitized to the need for privacy

protections. This does lawmakers a disservice. Congress has long sought to strike a

balance between privacy and security in the context of digital searches. See, e.g., USA

Freedom Act of 2015, Pub. L. No. 114-23, 129 Stat. 268 (limiting government

surveillance of telephone records); 18 U.S.C. §§ 2510-22 (2012) (limiting the

government’s ability to monitor electronic communications); Orin S. Kerr, The Effect of

Legislation on Fourth Amendment Protection, 115 Mich. L. Rev. 1117, 1120 (2017)

(observing “the recent enactment of more and stronger statutory privacy laws” by federal

and state legislatures in the past five years). And, though of course not directly relevant in

the context of a federal border search, states have historically also protected Fourth

Amendment privacy rights. See Kerr, 115 Mich. L. Rev. at 1120 (documenting state

statutes limiting the use of digital searches).

       It is sometimes said in non-border search cases that the judiciary does no more

than provide “a floor” which Congress can exceed at its discretion. See, e.g., Kelsey v.

Cty. of Schoharie, 567 F.3d 54, 64 (2d Cir. 2009); Graves v. Mahoning Cty., 821 F.3d

772, 778 (6th Cir. 2016). But the so-called floor in this case is not some innocuous

minimum, but a hugely consequential policy judgment that certain categories of border

                                              32
searches will require individualized suspicion. The fact that Congress has not thus far

seen fit to adopt a court’s preferred standard gives us no license to act preemptively with

an unnecessary constitutional disquisition. The dangers of this notion are underscored by

the majority’s reservation here of the question whether probable cause or a warrant may

be required for some unspecified categories of border searches in the future. See Maj. Op.

at 24-25. This does not sound like any sort of “floor” at all.

       The dangers of judicial standard-setting in an area as sensitive as border searches

is thus apparent. Here the legislative process would be informed by numerous

representatives of the executive branch, who can lend their practical insights and

experience to the inquiry. The executive’s role has always been thought especially

important in an area such as border searches, where it has long been held to have a

uniquely sovereign interest. The border search exception to the Fourth Amendment’s

warrant requirement is based on the “longstanding right of the sovereign to protect itself

by stopping and examining persons and property crossing into this country.” United

States v. Ramsey, 431 U.S. 606, 616 (1977). As the Supreme Court has explained, “[t]he

Government’s interest in preventing the entry of unwanted persons and effects is at its

zenith at the international border.” See United States v. Flores-Montano, 541 U.S. 149,

152 (2004). That interest is so powerful that border searches “are reasonable simply by

virtue of the fact that they occur at the border.” Ramsey, 431 U.S. at 616.

       The role of courts is thus not to blanket the field of border searches by preempting

constitutionally the contributions that the other two branches of our government are

constitutionally empowered and uniquely positioned to make. Marbury v. Madison did of

                                             33
course say that it is “emphatically the province and duty of the judicial department to say

what the law is.” 5 U.S. (1 Cranch) 137, 177 (1803). But that is a very different

proposition from holding that constitutional interpretation must be solely a judicial

function. Indeed “the general architecture of [the Constitution] would seem to imply a

basic coequality among the three departments. . . . [I]t nowhere explicitly raises the Court

above coordinate legislative and executive departments.” Akhil Reed Amar, Architecture,

77 Ind. L.J. 671, 692-93 (2002). This is not a new idea. James Madison wrote that “none

of [the three branches of government] ought to possess, directly or indirectly, an

overruling influence over the others in the administration of their respective powers.” The

Federalist No. 48 (James Madison). But it is precisely that “overruling influence” the

majority asserts in its unnecessary constitutional exercise today.

                                            III.

       The general search that all of us must undergo at airports attests to the difficulties

of ensuring airborne security through individualized suspicion. Our new world has

brought inconvenience and intrusions on an indiscriminate basis, which none of us

welcome, but which most of us undergo in the interest of assuring a larger common good.

Our old world of relative security and relative privacy, if indeed it ever existed, is now

gone with the wind. It is painful to dream of retrieving what is ours no longer.

       The Supreme Court has often noted how technology endangers privacy. As it

observed in Riley, “[m]odern cell phones, as a category, implicate privacy concerns far

beyond those implicated by the search of a cigarette pack, a wallet, or a purse.” 134 S. Ct.

at 2488-89. But Riley involved the warrantless search of a cell phone following an

                                             34
ordinary roadside arrest after a traffic violation. The defendant was not at the border. The

setting here is far different from Riley.

       Nor does the privacy interest recognized in Riley begin to answer the question of

who should strike the balance between privacy and security at the border of the country,

the point most freighted with security threats and the point at which a nation asserts and

affirms its very right to nationhood.

       Porous borders are uniquely tempting to those intent upon inflicting the vivid

horrors of mass casualties. Then too, there is the danger of highly classified technical

information being smuggled out of this country only to go into the hands of foreign

nations who do not wish us well and who seek to build their armaments to an ever more

perilous state.

       It is no secret that rapid technological advances have enhanced the ability of

criminal syndicates and terrorist networks to execute transnational schemes through the

coordination now made possible by instantaneous communications. To give criminal

enterprises the advantage of technological advancements and at the same time impair

access of law enforcement to those same developments risks recalibrating the Fourth

Amendment balance in a manner that does not comport with reasonableness. Cell phones

may prove essential to revealing the scope of a conspiracy; who is involved; what

weapons and devices the conspirators possess; what the purpose and plans and timing of

the plotted criminal acts may be; and where indeed those who would carry out these acts

may be located.



                                            35
       But to stop there is to halve the equation. The majority is right to emphasize that

searches of cell phones and the like can reveal a trove of data unconnected to any

criminal offense. The intrusion upon personal privacy is undoubtedly severe. One may of

course say that international travelers are on notice that border inspections may be

uniquely intrusive, and that travelers can prepare for that prospect by not taking a full

load of personal data abroad, where additional dangers of theft and inadvertent loss may

also await. But the fact that we can pack our digital suitcase with the same care that we

pack personal belongings in traditional luggage still does not nullify the reality that these

sorts of searches look into our lives in a way that is deeply uncomfortable, especially

when government itself becomes the agent of intrusion. But the ultimate question here is

not whether there is a balance to be struck between what are highly significant privacy

and security interests. It is what branch of government is best suited to make that

determination. In this case, where there is a longstanding historical practice in border

searches of deferring to the legislative and executive branches, the majority should have

shown a modest measure of restraint simply by deciding the case. Our role in this narrow

area is more the application of standards than the creation of them. In reaching to

formulate a constitutional rule, the majority has turned the whole thing on its head.

       We are ruling in a vacuum. We are building a doctrinal house without foundation.

The majority opinion provides little context or background or real-life picture of Dulles

Airport. It leaves little role for the legislative branch. At what point the domestic

conveniences of cell phone use should ripen into transnational entitlements is primarily

for the political branches to determine. The elected branches are also best able to gauge at

                                             36
what point the creeping constitutionalization of border searches reflects the cultural

habits and practices of an elite group of transnational Americans at the risk of

endangerment that knows no class bounds.

       It is ill advised to ignore the role of the political branches in addressing a

phenomenon that may fall short of the formal warfare contemplated in Articles I and II,

but still retains major features of international conflict. To reach beyond the Article III

function is to court grave dangers which we may perceive as remote and hypothetical

until one day, very suddenly, they are not. Not that any one case or any one appellate

court will likely bring down havoc on our heads. In our shielded circumstances, we may

never know or be apprised of many effects of our decisions. Still it is uncomfortable to

guess. I have nothing but respect for my friends in the majority. But taken cumulatively,

rulings slowly constitutionalizing border searches are taking chances with the safety and

lives of our fellow Americans. And this, as a judge, I cannot do.




                                            37

```

---

## GROUP: _overhaul2/lake/cases/United States v. Leary.json  (`lake-record`, 6 assertions)

### content_page

```
---
title: "United States v. Leary"
type: case
citation: "846 F.2d 592 (1988)"
parallel_cite: ""
neutral_cite: "1988 U.S. App. LEXIS 5755; 1988 WL 39811"
court: "U.S. Court of Appeals, Tenth Circuit"
court_level: coa
circuit: 10th
year: 1988
date_decided: 1988-05-02
docket: ""
authority_weight: "Binding in-circuit — 10th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: null
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Leary
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/505922/united-states-v-richard-j-leary-and-fl-kleinberg-co/"
  cluster_id: 505922
  opinion_id: 505922
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Leon]]", "[[Massachusetts v. Sheppard]]", "[[Coolidge v. New Hampshire]]", "[[Groh v. Ramirez]]"]
aliases: ["United States v. Leary (10th Cir. 1988)", "United States v. Richard J. Leary"]
tags: ["case", "fourth-amendment", "exclusionary-rule", "particularity", "general-warrant", "overbreadth", "good-faith-exception", "tenth-circuit"]
holding: "A facially overbroad / general warrant (authorizing seizure of records 'relating to' violations of the export laws, offering no…"
lake:
  record_id: United States v. Leary
  status: verified
  projected_at: 2026-07-09
---

# United States v. Leary

*846 F.2d 592 (10th Cir. 1988)* · U.S. Court of Appeals, Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Customs agents investigating suspected violations of the federal export laws by F.L. Kleinberg & Co. (and Richard Leary) obtained a warrant authorizing seizure of business records "relating to" violations of the export laws, with no further limitation. Executing it, the agents seized broad swaths of documents, including records concerning transactions, countries, and commodities not mentioned in the affidavit and unrelated to the suspected deal. The district court suppressed the evidence as the product of an overbroad warrant; the government appealed.

## Issue
(1) Whether a warrant authorizing seizure of records "relating to" violations of the export laws satisfies the Fourth Amendment's [[Particularity|particularity]] requirement; and (2) whether the [[United States v. Leon]] [[The Good-Faith Exception|good-faith exception]] saves evidence seized under such a facially overbroad warrant.

## Rule
No to both. The [[Particularity|particularity]] requirement bars general, exploratory rummaging: it "ensures that a search is confined in scope to particularly described evidence relating to a specific crime for which there is demonstrated probable cause." — 846 F.2d at 600 (quoting *Voss v. Bergsgaard*). ^pin-600

A warrant that fails to cabin the executing officer's discretion is an unconstitutional general warrant: "A warrant that directs an officer to seize records 'relating to' violations of the federal export laws offers no such guidelines. The officers were left to their own discretion." — *Id.* at 609. ^pin-609

The Leon [[The Good-Faith Exception|good-faith exception]] does not save such a warrant: "We find the warrant so facially deficient in its description of the items to be seized that the executing officers could not reasonably rely on it." — [*Id.* at 609](https://www.courtlistener.com/opinion/505922/united-states-v-richard-j-leary-and-fl-kleinberg-co/#:~:text=We%20find%20the%20warrant%20so). ^pin-609a

"Accordingly, we hold that the 'good faith' exception is inapplicable in these circumstances and affirm the district court's decision to suppress all of the evidence from the Kleinberg warrant." — *Id.* at 610. ^pin-610

## Application
On these facts the warrant was an unconstitutional general warrant and good faith could not rescue it. The "relating to" language gave the agents no criteria to distinguish seizable from non-seizable records, and the record showed they used the warrant's breadth (not any affidavit specificity) to seize documents far beyond the suspected transaction — "[t]here is no portion of the Kleinberg warrant that adequately defines the items to be seized," so the affidavit could not cure it and severance was impossible. Good faith was unavailable because a reasonably well-trained officer "should know that a warrant must provide guidelines for determining what evidence may be seized," and a warrant this facially deficient could not be reasonably presumed valid — placing it within *[[United States v. Leon|Leon]]*'s own exception for warrants "so facially deficient . . . that the executing officers cannot reasonably presume it to be valid." The Court did not reach the separate probable-cause defect.

## Conclusion
The warrant was facially overbroad and the *[[United States v. Leon|Leon]]* [[The Good-Faith Exception|good-faith exception]] did not apply; the district court's suppression of all evidence seized under it was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 10th Cir.**
- No negative subsequent treatment identified. *Leary* applies the [[Particularity|particularity]] rule of [[Coolidge v. New Hampshire]] and marks the boundary of [[United States v. Leon]] / [[Massachusetts v. Sheppard]] good-faith: a facially overbroad general warrant cannot support objectively reasonable reliance.

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Leary*, 846 F.2d 592 (10th Cir. 1988) — https://www.courtlistener.com/opinion/505922/united-states-v-richard-j-leary-and-fl-kleinberg-co/ — pinpoints: 600, 609, 610.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5908f017c89cb709", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Leary"}, "payload": {"all": [{"cite": "846 F.2d 592", "page": "592", "reporter": "F.2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "846"}, {"cite": "1988 U.S. App. LEXIS 5755", "page": "5755", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1988"}, {"cite": "1988 WL 39811", "page": "39811", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "1988"}], "display": "846 F.2d 592", "official": {"cite": "846 F.2d 592", "page": "592", "reporter": "F.2d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "846"}, "official_selection_present": true, "record_id": "United States v. Leary"}}
{"assertion_id": "2914c83409640b97", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-610", "record_id": "United States v. Leary"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-610", "pinpoint_status": "slip-only", "quote": "Accordingly, we hold that the 'good faith' exception is inapplicable in these circumstances and affirm the district court's decision to suppress all of the evidence from the Kleinberg warrant.", "quote_fidelity": "mismatch", "record_id": "United States v. Leary", "star_marker": null}}
{"assertion_id": "3ba308a3cb38de4c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-609a", "record_id": "United States v. Leary"}, "payload": {"fragment": "#:~:text=We%20find%20the%20warrant%20so", "page": null, "pin_id": "pin-609a", "pinpoint_status": "star-verified", "quote": "We find the warrant so facially deficient in its description of the items to be seized that the executing officers could not reasonably rely on it.", "quote_fidelity": "matched", "record_id": "United States v. Leary", "star_marker": "609"}}
{"assertion_id": "4a16c86c4b1d51c5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-600", "record_id": "United States v. Leary"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-600", "pinpoint_status": "slip-only", "quote": "violations of the export laws satisfies the Fourth Amendment's particularity requirement; and (2) whether the [[United States v. Leon]] good-faith exception saves evidence seized under such a facially overbroad warrant. ## Rule No to both. The particularity requirement bars general, exploratory rummaging: it", "quote_fidelity": "mismatch", "record_id": "United States v. Leary", "star_marker": null}}
{"assertion_id": "a90b29935ae806ff", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-609", "record_id": "United States v. Leary"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-609", "pinpoint_status": "slip-only", "quote": "A warrant that directs an officer to seize records 'relating to' violations of the federal export laws offers no such guidelines. The officers were left to their own discretion.", "quote_fidelity": "mismatch", "record_id": "United States v. Leary", "star_marker": null}}
{"assertion_id": "a59b2d7cf5e3c503", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Leary"}, "payload": {"as_of_content": null, "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Leary", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Leary

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Leary",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Richard J. Leary, and F.L. Kleinberg & Co.",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellant, v. Richard J. LEARY, and F.L. Kleinberg & Co., Defendants-Appellees",
    "input_case_name": "United States v. Leary",
    "court": "U.S. Court of Appeals, Tenth Circuit",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "10th",
    "state": null,
    "date_decided": "1988-05-02",
    "year": 1988,
    "docket": null,
    "cluster_id": 505922,
    "lead_opinion_id": 505922,
    "sibling_ids": [
      505922
    ],
    "absolute_url": "/opinion/505922/united-states-v-richard-j-leary-and-fl-kleinberg-co/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "846 F.2d 592",
      "volume": "846",
      "reporter": "F.2d",
      "page": "592",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1988 U.S. App. LEXIS 5755",
        "volume": "1988",
        "reporter": "U.S. App. LEXIS",
        "page": "5755",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 WL 39811",
        "volume": "1988",
        "reporter": "WL",
        "page": "39811",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "846 F.2d 592",
        "volume": "846",
        "reporter": "F.2d",
        "page": "592",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 U.S. App. LEXIS 5755",
        "volume": "1988",
        "reporter": "U.S. App. LEXIS",
        "page": "5755",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 WL 39811",
        "volume": "1988",
        "reporter": "WL",
        "page": "39811",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "846 F.2d 592",
    "official_selection": {
      "court_class": "coa",
      "selected": "846 F.2d 592",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-600",
      "page": null,
      "quote": "violations of the export laws satisfies the Fourth Amendment's particularity requirement; and (2) whether the [[United States v. Leon]] good-faith exception saves evidence seized under such a facially overbroad warrant. ## Rule No to both. The particularity requirement bars general, exploratory rummaging: it",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-609",
      "page": null,
      "quote": "A warrant that directs an officer to seize records 'relating to' violations of the federal export laws offers no such guidelines. The officers were left to their own discretion.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-609a",
      "page": null,
      "quote": "We find the warrant so facially deficient in its description of the items to be seized that the executing officers could not reasonably rely on it.",
      "star_marker": "609",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 90650,
      "fragment": "#:~:text=We%20find%20the%20warrant%20so",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-610",
      "page": null,
      "quote": "Accordingly, we hold that the 'good faith' exception is inapplicable in these circumstances and affirm the district court's decision to suppress all of the evidence from the Kleinberg warrant.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": null,
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Leary",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Cooper",
          "cluster_id": 223162,
          "cite": [
            "654 F.3d 1104",
            "108 A.F.T.R.2d (RIA) 5815",
            "2011 U.S. App. LEXIS 16825",
            "2011 WL 3559929"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
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
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Ray Erwin",
          "cluster_id": 523285,
          "cite": [
            "875 F.2d 268",
            "1989 U.S. App. LEXIS 6543",
            "1989 WL 51352"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re Grand Jury Subpoenas Dated December 10, 1987. Does I Through IV v. United States",
          "cluster_id": 556527,
          "cite": [
            "926 F.2d 847",
            "91 Daily Journal DAR 1973",
            "91 Cal. Daily Op. Serv. 1168",
            "1991 U.S. App. LEXIS 2243"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thao Dinh Le",
          "cluster_id": 157748,
          "cite": [
            "173 F.3d 1258",
            "1999 Colo. J. C.A.R. 2740",
            "1999 U.S. App. LEXIS 5794",
            "1999 WL 176192"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Daniel Scott Gahagan (87-1991), Michael John Gahagan (87-1993), Susan Soper (87-1992)",
          "cluster_id": 517440,
          "cite": [
            "865 F.2d 1490"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tanell Rashaad Curry, T/n Tanell R. Curry",
          "cluster_id": 546301,
          "cite": [
            "911 F.2d 72",
            "1990 U.S. App. LEXIS 13423",
            "1990 WL 111468"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Galpin",
          "cluster_id": 931473,
          "cite": [
            "720 F.3d 436",
            "2013 WL 3185299"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mark James Dahlman",
          "cluster_id": 660281,
          "cite": [
            "13 F.3d 1391",
            "1993 U.S. App. LEXIS 33363",
            "1993 WL 527367"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Burke",
          "cluster_id": 184136,
          "cite": [
            "633 F.3d 984",
            "2011 U.S. App. LEXIS 2082",
            "2011 WL 310520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael McMonagle v. Northeast Women's Center, Inc",
          "cluster_id": 112364,
          "cite": [
            "493 U.S. 901",
            "110 S. Ct. 261",
            "58 U.S.L.W. 3237",
            "107 L. Ed. 2d 210",
            "1989 U.S. LEXIS 4670"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Parker D. Langston, United States of America v. Huey Lee Francis, United States of America v. Enoch McIlroy United States of America v. William McIlroy United States of America v. James McIlroy United States of America v. Speck Aron Ross",
          "cluster_id": 587373,
          "cite": [
            "970 F.2d 692",
            "1992 U.S. App. LEXIS 15017"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joaquin Emilio Mesa-Rincon, United States of America v. Peter Scott Stoppe",
          "cluster_id": 546962,
          "cite": [
            "911 F.2d 1433",
            "1990 U.S. App. LEXIS 14187",
            "1990 WL 117972"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mark A. Harris",
          "cluster_id": 541818,
          "cite": [
            "903 F.2d 770",
            "30 Fed. R. Serv. 586",
            "1990 U.S. App. LEXIS 7973",
            "1990 WL 62995"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James S. Anderson",
          "cluster_id": 757710,
          "cite": [
            "154 F.3d 1225",
            "1998 Colo. J. C.A.R. 5134",
            "1998 U.S. App. LEXIS 22547",
            "98 CJ C.A.R. 5134"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Guidry",
          "cluster_id": 159006,
          "cite": [
            "199 F.3d 1150",
            "2000 Colo. J. C.A.R. 16",
            "84 A.F.T.R.2d (RIA) 7443",
            "1999 U.S. App. LEXIS 33145"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Arthur Theodore Towne Dane Joseph Treiber",
          "cluster_id": 610668,
          "cite": [
            "997 F.2d 537",
            "93 Cal. Daily Op. Serv. 4520",
            "93 Daily Journal DAR 7722",
            "1993 U.S. App. LEXIS 14481",
            "1993 WL 210527"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. SDI Future Health, Inc.",
          "cluster_id": 1459636,
          "cite": [
            "568 F.3d 684",
            "103 A.F.T.R.2d (RIA) 2436",
            "2009 U.S. App. LEXIS 13003",
            "2009 WL 1508763"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Roccaforte",
          "cluster_id": 1274940,
          "cite": [
            "919 P.2d 799",
            "20 Brief Times Rptr. 997",
            "1996 Colo. LEXIS 209",
            "1996 WL 342294"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Center Art Galleries--Hawaii, Inc. William D. Mett v. United States",
          "cluster_id": 523623,
          "cite": [
            "875 F.2d 747",
            "1989 U.S. App. LEXIS 6983",
            "1989 WL 51355"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. Gracey",
          "cluster_id": 154737,
          "cite": [
            "111 F.3d 1472",
            "1997 WL 192018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Herrera",
          "cluster_id": 167373,
          "cite": [
            "444 F.3d 1238",
            "2006 U.S. App. LEXIS 9830",
            "2006 WL 1017642"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re the Matter of the Search of Kitty's East, 735 E. Colfax Avenue, Denver, Colorado. Kitty's East v. United States",
          "cluster_id": 543204,
          "cite": [
            "905 F.2d 1367",
            "1990 U.S. App. LEXIS 9064",
            "1990 WL 74065"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ezra Griffith",
          "cluster_id": 4419946,
          "cite": [
            "867 F.3d 1265",
            "2017 WL 3568288",
            "2017 U.S. App. LEXIS 15636"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Angevine",
          "cluster_id": 162077,
          "cite": [
            "281 F.3d 1130",
            "2002 U.S. App. LEXIS 2746",
            "2002 WL 254138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leary:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(505922) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca10)",
        "reviewed": 23,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 23,
        "triage_read": 0,
        "triage_snippet_classified": 23
      },
      "lane2_top_cited": {
        "query": "cites:(505922)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNCZzPTE1ODkwNjEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28505922%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(505922)",
        "reviewed": 13,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 13,
        "triage_read": 0,
        "triage_snippet_classified": 13
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(505922)",
    "indexed_citing_opinions": 121,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 505922,
        "count": 121,
        "count_source": "search"
      }
    ],
    "citation_count": 230,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-leary.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU0OTI2Njgmcz00NDExNjU3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28505922%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 505922,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 105594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 109522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 110325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 111066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 111252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 111263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 111927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 304369,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 324061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 346767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 350518,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 355493,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 362453,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 371945,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 373913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 374752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 376886,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 380192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 387515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 392049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 393709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 394830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 397225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 405042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 406519,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 408050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 412106,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 424091,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 434740,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 440371,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 442866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 444625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 445307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 450796,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 451731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 451751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 451967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 453574,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 458765,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 458774,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 458949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 458952,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 461301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 461431,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 461601,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 463621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 467613,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 471869,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 472649,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 474531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 474635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 475515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 475840,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 478417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 479836,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 480985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 484648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 484709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 487817,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 492430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 493275,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 493687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 495037,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 498743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 501767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 502477,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 503533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 1392737,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 1394599,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 1482053,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 1519992,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 1577597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 1875700,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 1876547,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 2149373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 505922,
        "cited_id": 2595045,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "RU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T01:16:56Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:17:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:17:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:20:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:17:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Leary (truncated)

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b690-7">
  STEPHEN H. ANDERSON, Circuit Judge.
 </author>
<p id="b690-8">
  The government appeals from the district court’s decision granting defendants’ motion to suppress evidence seized under a search warrant. We affirm the district court, holding that the defendants’ fourth amendment rights were infringed, that the search warrant was facially overbroad and invalid, and that the evidence seized should be suppressed.
 </p>
<p id="b690-9">
  I. Background
 </p>
<p id="b690-10">
  This appeal stems from the execution of a search warrant at the offices of the F.L. Kleinberg Company (“Kleinberg”) in Boulder, Colorado on August 23, 1984. Klein-berg and Richard J. Leary, a vice-president at Kleinberg, were subsequently indicted for conspiring to violate the Export Administration Act. 50 U.S.C.App. § 2410. Kleinberg and Leary, as defendants, moved to suppress the fruits of the search of the Kleinberg offices. The district court granted that motion and the government appeals pursuant to <span class="citation no-link">18 U.S.C. § 3731</span>.
 </p>
<p id="b690-11">
  The search warrant was obtained by federal customs agent John Juhasz on the basis of his affidavit alleging violations of the Arms Export Control Act, <span class="citation no-link">22 U.S.C. § 2778</span>, and the Export Administration Act. The affidavit recites in detail the purchase and attempted export of a Micro-tel Precision Attenuation Measurement Receiver
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  by Kleinberg in 1984. In short, the affidavit alleges that Kleinberg did not have the proper license to export this particular piece of equipment and that Kleinberg was attempting to illegally export the receiver to the People’s Republic of China via a series of “front” companies in Hong Kong. The affidavit addresses only this single transaction and the companies
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  involved in that transaction. No other companies, countries, or commodities are mentioned in the affidavit or alleged to be part of any illegal export scheme.
 </p>
<p id="b690-16">
  Based on the affidavit, a warrant was issued to search the Kleinberg offices and seize the following property:
 </p>
<blockquote id="Avh">
  Correspondence, Telex messages, contracts, invoices, purchase orders, shipping documents, payment records, export documents, packing slips, technical data, recorded notations, and other records and communications relating to the purchase, sale and illegal exportation of materials in violation of the Arms Export Control Act, 22 U.S.C. 2778, and the Export Administration Act of 1979, 50 U.S. C.App. 2410.
 </blockquote>
<p id="b690-17">
  The warrant was executed on August 23, 1984 by Agent Juhasz and six other Customs officers. Twenty boxes of business records were seized including references to sales and sales contacts throughout the world, telexes to Australia and South Africa, information from applicants for employment with Kleinberg, Leary’s application with Shearson American Express for per
  <span citation-index="1" class="star-pagination" label="595"> 
   *595
   </span>
  sonal financial planning, Leary’s life insurance policy, and correspondence relating to other businesses for which Leary acted as sales representative.
 </p>
<p id="b691-4">
  After the indictment, Kleinberg and Leary moved to suppress all of the evidence seized in the search. The district court granted that motion, finding first that the affidavit was not supported by probable cause,
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  and second, that the warrant did not sufficiently specify the evidence to be seized. The court also found that the “good faith” exception to the exclusionary rule adopted by the United States Supreme Court in
  <em>
   United States v. Leon,
  </em>
  <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U.S. 897</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">82 L.Ed.2d 677</a></span> (1984) was inapplicable.
 </p>
<p id="b691-5">
  On appeal, the government argues (1) Leary and Kleinberg have no standing to raise a fourth amendment claim; (2) the warrant was sufficiently particular in specifying the items to be seized; (3) the warrant was supported by probable cause; and (4) even if the warrant is found upon review to be invalid, reliance on the warrant was “objectively reasonable” and the evidence should not be suppressed under the reasoning of
  <em>
   <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>.
  </em>
</p>
<p id="b691-6">
  II. Standing
 </p>
<p id="b691-7">
  In
  <em>
   Rakas v. Illinois,
  </em>
  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U.S. 128</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. 421</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">58 L.Ed.2d 387</a></span> (1978) the Supreme Court abandoned a separate analysis of “standing” for claims of violations of the fourth amendment in favor of an analysis focusing on the “substantive question of whether or not the proponent of the motion to suppress has had his own Fourth Amendment rights infringed by the search and seizure which he seeks to challenge.”
  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#133" aria-description="Citation for case: Rakas v. Illinois"><em>
   Id.
  </em>
  at 133</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#425" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. at 425</a></span>.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
<em>
   See Rawlings v. Kentucky,
  </em>
  <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/#104" aria-description="Citation for case: Rawlings v. Kentucky">448 U.S. 98, 104</a></span>, <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/#2561" aria-description="Citation for case: Rawlings v. Kentucky">100 S.Ct. 2556, 2561</a></span>, <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">65 L.Ed.2d 633</a></span> (1980);
  <em>
   United States v. Hansen,
  </em>
  <span class="citation" data-id="392049"><a href="/opinion/392049/united-states-v-gary-e-hansen-daniel-e-means-aka-daniel-e-johnson/" aria-description="Citation for case: United States v. Gary E. Hansen, Daniel E. Means, AKA...">652 F.2d 1374</a></span>, 1379 n. 2 (10th Cir.1981). “Whether a person has standing to contest a search on fourth amendment grounds turns on whether the person had a legitimate expectation of privacy in the area searched, not merely in the items seized.”
  <em>
   United States v. Skowronski,
  </em>
  <span class="citation" data-id="493687"><a href="/opinion/493687/united-states-v-william-michael-skowronski/#1418" aria-description="Citation for case: United States v. William Michael Skowronski">827 F.2d 1414, 1418</a></span> (10th Cir.1987) (citing
  <em>
   United States v. Salvucci,
  </em>
  <span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/#93" aria-description="Citation for case: United States v. Salvucci">448 U.S. 83, 93</a></span>, <span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/#2554" aria-description="Citation for case: United States v. Salvucci">100 S.Ct. 2547, 2554</a></span>, <span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">65 L.Ed.2d 619</a></span> (1980)). Determining whether a legitimate or justifiable expectation of privacy exists, in turn, involves two inquiries. First, the claimant must show a subjective expectation of privacy in the area searched, and second, that expectation must be one that “society is prepared to recognize as ‘reasonable.’ ”
  <em>
   Hudson v. Palmer,
  </em>
  <span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/#525" aria-description="Citation for case: Hudson v. Palmer">468 U.S. 517, 525</a></span>, <span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/#3199" aria-description="Citation for case: Hudson v. Palmer">104 S.Ct. 3194, 3199</a></span>, <span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/" aria-description="Citation for case: Hudson v. Palmer">82 L.Ed.2d 393</a></span> (1984) (quoting in part
  <em>
   Katz v. United States,
  </em>
  <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U.S. 347, 361</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#516" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507, 516</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L.Ed.2d 576</a></span> (1967) (Harlan, J., concurring));
  <em>
   see also United States v. Owens,
  </em>
  <span class="citation" data-id="463621"><a href="/opinion/463621/united-states-v-merle-ellis-owens/#150" aria-description="Citation for case: United States v. Merle Ellis Owens">782 F.2d 146, 150</a></span> (10th Cir.1986). The “ultimate question” is “whether one’s claim to privacy from government intrusion is reasonable in light of all the surrounding circumstances.”
  <em>
   Rakas,
  </em>
  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#152" aria-description="Citation for case: Rakas v. Illinois">439 U.S. at 152</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#435" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. at 435</a></span> (Powell, J., concurring). Finally, standing is a legal question, and “[wjhere the facts are not in dispute, this court may review the question of standing de novo.”
  <em>
   United States v. Kuespert,
  </em>
  <span class="citation" data-id="458765"><a href="/opinion/458765/united-states-v-lee-a-kuespert/#1067" aria-description="Citation for case: United States v. Lee A. Kuespert">773 F.2d 1066, 1067</a></span> (9th Cir.1985).
 </p>
<p id="b691-14">
  There is no doubt that a corporate officer or employee may assert a reasonable or legitimate expectation of privacy in his corporate office.
  <em>
   Cf. Mancusi v. DeForte,
  </em>
  <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#369" aria-description="Citation for case: Mancusi v. DeForte">392 U.S. 364, 369</a></span>, <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#2124" aria-description="Citation for case: Mancusi v. DeForte">88 S.Ct. 2120, 2124</a></span>, <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">20 L.Ed.2d 1154</a></span> (1968) (“It has long been settled that one has standing to object to a search of his office, as well as of his home.”);
  <em>
   United States v. Lefkowitz,
  </em>
  <span class="citation" data-id="1519992"><a href="/opinion/1519992/united-states-v-lefkowitz/#230" aria-description="Citation for case: United States v. Lefkowitz">464 F.Supp. 227, 230</a></span> (C.D.Cal.1979) (corporate officers
  <span citation-index="1" class="star-pagination" label="596"> 
   *596
   </span>
  had sufficient privacy interest in corporate office suite),
  <em>
   aff'd,
  </em>
  <span class="citation" data-id="376886"><a href="/opinion/376886/united-states-v-albert-m-lefkowitz/" aria-description="Citation for case: United States v. Albert M. Lefkowitz">618 F.2d 1313</a></span> (9th Cir.),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./449/824/">449 U.S. 824</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./101/86/">101 S.Ct. 86</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/66/27/">66 L.Ed.2d 27</a></span> (1980);
  <em>
   see also
  </em>
  4 W. LaFave,
  <em>
   Search and Seizure
  </em>
  § 11.3(d) (2d ed. 1987) [hereinafter LaFave]. Similarly, “it seems clear that a corporate defendant has standing with respect to searches of corporate premises and seizure of corporate records ”
  <em>
   Id.
  </em>
  at 316.
  <em>
   See G.M. Leasing Corp. v. United States,
  </em>
  <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#353" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U.S. 338, 353</a></span>, <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#629" aria-description="Citation for case: G. M. Leasing Corp. v. United States">97 S.Ct. 619, 629</a></span>, <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/" aria-description="Citation for case: G. M. Leasing Corp. v. United States">50 L.Ed.2d 530</a></span> (1977);
  <em>
   Auster Oil &amp; Gas, Inc. v. Stream,
  </em>
  <span class="citation" data-id="8956372"><a href="/opinion/8965067/auster-oil-gas-inc-v-stream/" aria-description="Citation for case: Auster Oil &amp; Gas, Inc. v. Stream">835 F.2d 597</a></span> (5th Cir.1988). In addition, except in rare circumstances, a warrant is as necessary to support a search of commercial premises as private premises.
  <em>
   See Blackie’s House of Beef, Inc. v. Castillo,
  </em>
  <span class="citation" data-id="394830"><a href="/opinion/394830/blackies-house-of-beef-inc-v-leonel-j-castillo-commissioner-of-the/" aria-description="Citation for case: Blackie&#x27;s House of Beef, Inc. v. Leonel J. Castillo,...">659 F.2d 1211</a></span>, 1216 n. 5 (D.C.Cir.1981) (citing
  <em>
   Marshall v. Barlow’s, Inc.,
  </em>
  <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U.S. 307</a></span>, <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">98 S.Ct. 1816</a></span>, <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">56 L.Ed.2d 305</a></span> (1978)),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./455/940/">455 U.S. 940</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./102/1432/">102 S.Ct. 1432</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/71/651/">71 L.Ed.2d 651</a></span> (1982).
 </p>
<p id="b692-4">
  Normally, our inquiry would end here. The government argues, however, that Leary and Kleinberg lack the requisite expectation of privacy in their offices and records because of the regulatory scheme imposed upon exporters by the federal government and the company’s “open door” policy toward government inspectors. For purposes of clarity, we repeat the government’s argument in some detail:
 </p>
<blockquote id="b692-5">
  [T]he government would concede that if it were not for the regulatory scheme requiring that the defendants make, keep and produce the seized records to the government upon request, and the company’s open door policy, both defendants would be able to assert a privacy interest in the seized records under
  <em>
   Rakas v. Illinois,
  </em>
  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U.S. 128</a></span> [<span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. 421</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">58 L.Ed.2d 387</a></span>] (1978).
 </blockquote>
<blockquote id="b692-6">
  The standing argument asserted by the government is limited to the very unusual facts of this case_ [T]he defendants operated in a highly regulated industry where the law required them to make, keep and produce all documents relating in any way to an export. Furthermore, company policy was that the government could come, scheduled or unscheduled and ask for any file or information it needed. Thus, the government’s argument is that any privacy interest in the required records was waived by the company and Mr. Leary.
 </blockquote>
<blockquote id="b692-9">
  Mr. Leary must have known that under these circumstances any company record could be turned over to the government upon request at any time, whether he was present or not, without the government being required to resort to legal process.
 </blockquote>
<blockquote id="b692-10">
  The company’s position is somewhat different, because it could have revoked the policy at any time. But it did not. At the conclusion of the search the President, Frederick L. Kleinberg, invited the agents back to examine any remaining records at a later time.
 </blockquote>
<p id="b692-11">
  Reply Brief of Appellant at 3-5 (citations omitted).
 </p>
<p id="b692-12">
  We find the government’s argument inherently misleading, as it attempts to concede an expectation of privacy with one hand and remove it with the other. Moreover, the argument confuses the law relating to searches or inspections of “regulated” industries with simple recordkeeping requirements.
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  Nevertheless, we will analyze the government’s position in detail. The government’s standing argument consists of two related questions: First, do the regulatory requirements imposed on exporters licensed by the government and Kleinberg’s “open door” policy constitute “circumstances” that render Leary and Kleinberg’s expectation of privacy unreasonable?
  <em>
   See Rakas,
  </em>
  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#152" aria-description="Citation for case: Rakas v. Illinois">439 U.S. at 152</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#435" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. at 435</a></span> (Powell, J., concurring). Second, have Leary and Kleinberg “waived”
  <span citation-index="1" class="star-pagination" label="597"> 
   *597
   </span>
  their fourth amendment rights by participating in a regulated business and by adopting an “open door” policy, inviting government agents to inspect their business records? We address these questions in turn.
 </p>
<p id="b693-4">
  Federal regulations implementing the nation’s export control laws impose comprehensive recordkeeping requirements on exporters. It is clear, however, that licensed exporters retain their fourth amendment rights. The key provision is <span class="citation no-link">15 C.F.R. § 387.13</span>(f)(1) (1987):
 </p>
<blockquote id="b693-5">
  Persons within the United States may be requested to produce records which are required to be kept by any provision of the Export Administration Regulations or by any order, and to make them available for inspection and copying by any authorized agent, official or employee of the International Trade Administration, the U.S. Customs Service, or the U.S. Government, without any charge or expense to such agent, official or employee. The [government] encourage[s] voluntary cooperation with such requests. When voluntary cooperation is not forthcoming, the Office of Export Enforcement and the Office of Antiboycott Compliance are authorized to issue subpoenas for books, records and other writings. In instances where a person does not comply with a subpoena, the Department of Commerce may petition a district court to have the subpoena enforced.
 </blockquote>
<p id="A-K">
  The district court properly analyzed the effect of these requirements:
 </p>
<blockquote id="b693-6">
  The Department of Commerce could have requested inspection and copying of records relating to export at any time, and if the company refused to allow voluntary inspection, the government could have subpoenaed the records. This required procedure affords the protection of judicial review before records can be seized without permission.... The fact that a warrant is required for a full-scale criminal search and seizure of records required to be kept recognizes the fourth amendment’s protection of privacy even in these circumstances and restrictions on the government’s power to intrude on that privacy.
 </blockquote>
<p id="b693-11">
  Mem. Opinion at 4.
  <em>
   Cf. United States v. Molt,
  </em>
  <span class="citation" data-id="2149373"><a href="/opinion/2149373/united-states-v-molt/" aria-description="Citation for case: United States v. Molt">444 F.Supp. 491</a></span> (E.D.Pa.),
  <em>
   aff'd,
  </em>
  <span class="citation" data-id="9465383"><a href="/opinion/362453/united-states-v-henry-a-molt-jr/" aria-description="Citation for case: United States v. Henry A. Molt, Jr">589 F.2d 1247</a></span> (3d Cir.1978);
  <em>
   see also Railway Labor Executives’ Ass’n v. Burnley,
  </em>
  <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#584" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley">839 F.2d 575, 584</a></span> (9th Cir.1988) (“When no ... plan [authorizing warrantless inspections] is built into the legislation regulating a specific industry, the [Supreme] Court has required a warrant as a condition of a reasonable search.”);
  <em>
   Serpas v. Schmidt,
  </em>
  <span class="citation" data-id="9476620"><a href="/opinion/493275/don-serpas-raymond-johnson-and-carl-waters-individually-and-on-behalf-of/#28" aria-description="Citation for case: Don Serpas, Raymond Johnson and Carl Waters, Individually...">827 F.2d 23, 28</a></span> (7th Cir.1987) (“[A] history of pervasive regulation of an industry is not by itself enough to render the warrant requirement superfluous_ [T]he Supreme Court has sanctioned warrantless searches of commercial premises in certain industries subject to longstanding governmental oversight.... [however] [i]n each of these cases, ... Congress expressly authorized the terms and conditions of searches on specified premises.”),
  <em>
   cert. denied,
  </em>
  — U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./108/1075/">108 S.Ct. 1075</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/99/234/">99 L.Ed.2d 234</a></span> (1988). Neither the export regulations nor the export statutes authorize a warrantless search and seizure of business records,
  <em>
   see
  </em>
  <span class="citation no-link">22 U.S.C. § 2778</span>(e); 50 U.S.C.App. § 2411; Brief of Appellant at 14, yet the government would have us hold that the regulatory scheme negates the licensed exporter’s right to challenge an invalid warrant. In other words, the government concedes that it must obtain a warrant but argues that it need not obtain a valid warrant. We refuse to adopt this reasoning.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
</p>
<p id="b694-3">
<span citation-index="1" class="star-pagination" label="598"> 
   *598
   </span>
  Similarly, the company’s “open door” policy does not negate the defendants’ expectation of privacy. There is a distinction of constitutional significance between the company’s policy, which invited government agents to “visit ... and ask for any file or information they want or need,” and a thorough search of the offices and seizure and removal of twenty boxes of files, including personal records and documents unrelated to the company’s regulated export activities. Leary and Kleinberg retained control over the premises and records and had the authority to restrict the government’s access by the terms of the policy. In sum, we find a reasonable expectation of privacy in these circumstances.
 </p>
<p id="b694-4">
  For substantially the same reasons, we reject the government’s argument that Leary and Kleinberg either waived their fourth amendment rights or consented to the search. When evaluating fourth amendment rights, there is no clear distinction between “consent” to a search and a “waiver” of one’s privacy interest. The government, however, attempts to draw a distinction in this case, that is, that Leary and Kleinberg either “consented” to the August 23 search, or evidenced an ongoing consent to be searched at any time (a “waiver”).
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  Despite the government’s effort to cast this inquiry as one of waiver, the proper analysis focuses on consent. In fact, the Supreme Court has expressly rejected the use of “waiver” analysis in fourth amendment cases in favor of a “voluntary consent” test.
  <em>
   See Schneckloth v. Bustamonte,
  </em>
  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#235" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218, 235-46</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#2052" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041, 2052-57</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L.Ed.2d 854</a></span> (1973). Thus, to determine whether, by granting any ongoing consent, Leary and Kleinberg effectively “waived” their fourth amendment rights, our analysis is guided by the law developed for analyzing “consent” searches.
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
</p>
<p id="b694-9">
  Initially, we reject any suggestion that Leary and Kleinberg specifically consented to the August 23, 1984 search. When a government agent claims authority to search under a warrant, “he announces in effect that the occupant has no right to resist the search. The situation is instinct with coercion — albeit colorably lawful coercion. Where there is coercion there cannot be consent.”
  <em>
   Bumper v. North Carolina,
  </em>
  <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#550" aria-description="Citation for case: Bumper v. North Carolina">391 U.S. 543, 550</a></span>, <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#1792" aria-description="Citation for case: Bumper v. North Carolina">88 S.Ct. 1788, 1792</a></span>, <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">20 L.Ed.2d 797</a></span> (1968). In fact, the Supreme Court has stated that: “A search conducted in reliance upon a warrant cannot later be justified on the basis of consent if it turns out that the warrant was invalid.”
  <em>
   Bumper,
  </em>
  <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#549" aria-description="Citation for case: Bumper v. North Carolina">391 U.S. at 549</a></span>, <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#1792" aria-description="Citation for case: Bumper v. North Carolina">88 S.Ct. at 1792</a></span>.
  <a class="footnote" href="#fn9" id="fn9_ref">
   9
  </a>
</p>
<p id="b695-3">
<span citation-index="1" class="star-pagination" label="599"> 
   *599
   </span>
  Similarly, we find no evidence that Leary and Kleinberg granted an ongoing consent to searches by Customs officers. We recently addressed the question of consent in detail, recognizing that the Supreme Court requires that “consent to a Fourth Amendment search must be voluntary
  <em>
   in fact
  </em>
  and free of coercion under the totality of the circumstances....”
  <em>
   United States v. Carson,
  </em>
  <span class="citation" data-id="9475015"><a href="/opinion/471869/united-states-v-george-l-carson/#1150" aria-description="Citation for case: United States v. George L. Carson">793 F.2d 1141, 1150</a></span> (10th Cir.) (citing
  <em>
   Schneckloth,
  </em>
  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#248" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. at 248-49</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#2058" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. at 2058-59</a></span>) (emphasis in original),
  <em>
   cert. denied,
  </em>
  — U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./107/315/">107 S.Ct. 315</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.%202d/93/289/">93 L.Ed. 2d 289</a></span> (1986). In addition, we have noted that consent “is a question of fact to be determined from the totality of all the circumstances [and] [t]he Government has the burden of proving that consent was given freely and voluntarily.”
  <em>
   United States v. Recalde,
  </em>
  <span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1453" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d 1448, 1453</a></span> (10th Cir.1985) (citations omitted).
  <a class="footnote" href="#fn10" id="fn10_ref">
   10
  </a>
</p>
<p id="b695-5">
  There is no evidence that Kleinberg and Leary granted an ongoing consent to the search of their offices or records by participating in a regulated activity. The federal recordkeeping regulations leave exporters with a substantial privacy interest. Government agents may be required to resort to judicial process to obtain desired records. Absent a statutory scheme authorizing warrantless searches, there is no waiver of constitutional rights in the mere fact that Leary and Kleinberg chose to participate in an activity regulated and licensed by the government.
  <em>
   See Marshall v. Barlow’s Inc.,
  </em>
  <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#312" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U.S. 307, 312-14, 323-24</a></span>, <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#1820" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">98 S.Ct. 1816, 1820-21, 1826</a></span>, <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">56 L.Ed.2d 305</a></span> (1978).
 </p>
<p id="b695-6">
  Nor do we find any ongoing consent in the company’s “open door” policy. As we noted earlier, Kleinberg did not invite the government to rummage through company files and carry out any documents that the agents found interesting. Equally important is the fact that “[w]hen the basis for a search or seizure is consent, the government must conform to the limitations placed upon the right granted to search, seize or retain the papers or effects.”
  <em>
   Mason v. Pulliam,
  </em>
  <span class="citation" data-id="9463909"><a href="/opinion/346767/harve-d-mason-and-pat-j-mason-v-ralph-j-pulliam-special/#429" aria-description="Citation for case: Harve D. Mason and Pat J. Mason v. Ralph J. Pulliam...">557 F.2d 426, 429</a></span> (5th Cir.1977);
  <em>
   see also United States v. Gay,
  </em>
  <span class="citation" data-id="458949"><a href="/opinion/458949/united-states-v-thomas-norman-gay/#377" aria-description="Citation for case: United States v. Thomas Norman Gay">774 F.2d 368, 377</a></span> (10th Cir.1985) (“The scope of a consent search is limited by the breadth of the actual consent itself.”);
  <em>
   United States v. Milian-Rodriguez,
  </em>
  <span class="citation" data-id="450796"><a href="/opinion/450796/united-states-v-ramon-milian-rodriguez/#1563" aria-description="Citation for case: United States v. Ramon Milian-Rodriguez">759 F.2d 1558, 1563</a></span> (11th Cir.) (“the government may not use consent to a search which was initially described as narrow as license to conduct a general search”),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./474/845/">474 U.S. 845</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./106/135/">106 S.Ct. 135</a></span>, <span class="citation" data-id="9049585"><a href="/opinion/9056060/kabanuk-v-minnesota/" aria-description="Citation for case: Kabanuk v. Minnesota">88 L.Ed.2d 112</a></span> (1985). Even if Kleinberg’s policy can be characterized as an ongoing consent to government searches, the government exceeded the scope of that consent in two respects. First, Kleinberg invited government agents to inspect and copy records, not seize them. Second, Kleinberg’s invitation extended only to those documents related to regulated export activities. The government searched and seized records dealing with Leary’s personal and financial affairs and business activities unrelated to exports.
 </p>
<p id="b695-10">
  In addition, we find a compelling policy reason to reject the government’s argument. As the regulations indicate, the government encourages voluntary cooperation with requests for export documents and information. Yet the government urges us to find that Kleinberg’s voluntary cooperation has resulted in a waiver of fourth amendment rights.
  <a class="footnote" href="#fn11" id="fn11_ref">
   11
  </a>
  This interpre
  <span citation-index="1" class="star-pagination" label="600"> 
   *600
   </span>
  tation of the law would deliver a serious blow to the government’s “voluntary cooperation” efforts and discourage “open door” policies in the export industry.
 </p>
<p id="b696-4">
  Accordingly, we find no consent or “waiver” and conclude that both Leary and Kleinberg have had their fourth amendment rights infringed by this search and seizure and may seek suppression of the evidence. We proceed to review the adequacy of the search warrant.
 </p>
<p id="b696-5">
  III. Particularity
 </p>
<p id="b696-6">
  The fourth amendment requires that warrants “particularly describ[e] ... the persons or things to be seized.” U.S. Const, amend. IV. This requirement prevents a “general, exploratory rummaging in a person’s belongings,”
  <em>
   Coolidge v. New Hampshire,
  </em>
  <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#467" aria-description="Citation for case: Coolidge v. New Hampshire">403 U.S. 443, 467</a></span>, <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#2038" aria-description="Citation for case: Coolidge v. New Hampshire">91 S.Ct. 2022, 2038</a></span>, <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">29 L.Ed.2d 564</a></span> (1971) and “ ‘makes general searches ... impossible and prevents the seizure of one thing under a warrant describing another. As to what is be taken, nothing is left to the discretion of the officer executing the warrant.’ ”
  <em>
   Stanford v. Texas,
  </em>
  <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas">379 U.S. 476, 485</a></span>, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#511" aria-description="Citation for case: Stanford v. Texas">85 S.Ct. 506, 511</a></span>, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">13 L.Ed.2d 431</a></span> (1965) (quoting Ma
  <em>
   rron v. United States, 275
  </em>
  U.S. 192, 196, <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#76" aria-description="Citation for case: Marron v. United States">48 S.Ct. 74, 76</a></span>, <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">72 L.Ed. 231</a></span> (1927)).
  <em>
   See Andresen v. Maryland,
  </em>
  <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#480" aria-description="Citation for case: Andresen v. Maryland">427 U.S. 463, 480</a></span>, <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#2748" aria-description="Citation for case: Andresen v. Maryland">96 S.Ct. 2737, 2748</a></span>, <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">49 L.Ed.2d 627</a></span> (1976);
  <em>
   United States v. Medlin,
  </em>
  <span class="citation" data-id="503533"><a href="/opinion/503533/united-states-v-arvle-edgar-medlin/#1199" aria-description="Citation for case: United States v. Arvle Edgar Medlin">842 F.2d 1194, 1199</a></span> (10th Cir.1988);
  <em>
   Voss v. Bergsgaard,
  </em>
  <span class="citation" data-id="8935318"><a href="/opinion/8944758/voss-v-bergsgaard/#404" aria-description="Citation for case: Voss v. Bergsgaard">774 F.2d 402, 404</a></span> (10th Cir.1985). “The particularity requirement [also] ensures that a search is confined in scope to particularly described evidence relating to a specific crime for which there is demonstrated probable cause.”
  <em>
   Voss,
  </em>
  <span class="citation" data-id="8935318"><a href="/opinion/8944758/voss-v-bergsgaard/#404" aria-description="Citation for case: Voss v. Bergsgaard">774 F.2d at 404</a></span>.
 </p>
<p id="b696-7">
  The test applied to the description of the items to be seized is a practical one. “ ‘A description is sufficiently particular when it enables the searcher to reasonably ascertain and identify the things authorized to be seized.’ ”
  <em>
   United States v. Wolfenbarger,
  </em>
  <span class="citation" data-id="412106"><a href="/opinion/412106/united-states-v-john-q-wolfenbarger/#752" aria-description="Citation for case: United States v. John Q. Wolfenbarger">696 F.2d 750, 752</a></span> (10th Cir.1982) (quoting
  <em>
   United States v. Wuagneux,
  </em>
  <span class="citation" data-id="406519"><a href="/opinion/406519/united-states-v-george-wuagneux/#1348" aria-description="Citation for case: United States v. George Wuagneux">683 F.2d 1343, 1348</a></span> (11th Cir.1982)).
  <a class="footnote" href="#fn12" id="fn12_ref">
   12
  </a>
  Even a warrant that describes the items to be seized in broad or generic terms may be valid “when the description is as specific as the circumstances and the nature of the activity under investigation permit.”
  <em>
   United States v. Santarelli,
  </em>
  <span class="citation" data-id="461431"><a href="/opinion/461431/united-states-v-dominic-santarelli/#614" aria-description="Citation for case: United States v. Dominic Santarelli">778 F.2d 609, 614</a></span> (11th Cir.1985);
  <em>
   see United States v. Strand,
  </em>
  <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/#453" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers">761 F.2d 449, 453</a></span> (8th Cir.1985) (“degree of specificity required necessarily depends upon the circumstances of each particular case”). However, the fourth amendment requires that the government describe the items to be seized with as much specificity as the government’s knowledge and circumstances allow, and “warrants are conclusively invalidated by their substantial failure to specify as nearly as possible the distinguishing characteristics of the goods to be seized.”
  <em>
   United States v. Fuccillo,
  </em>
  <span class="citation" data-id="480985"><a href="/opinion/480985/united-states-v-carl-a-fuccillo/#176" aria-description="Citation for case: United States v. Carl A. Fuccillo">808 F.2d 173, 176</a></span> (1st Cir.),
  <em>
   cert. denied,
  </em>
  — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./107/2481/">107 S.Ct. 2481</a></span>, <span class="citation no-link">96 L.Ed.2d 374</span> (1987).
 </p>
<p id="b696-13">
  The district court found the Kleinberg warrant overbroad. That legal conclusion is subject to
  <em>
   de novo
  </em>
  review on appeal.
  <em>
   See United States v. Fannin,
  </em>
  <span class="citation" data-id="487817"><a href="/opinion/487817/united-states-v-john-fannin/#1381" aria-description="Citation for case: United States v. John Fannin">817 F.2d 1379, 1381</a></span> (9th Cir.1987);
  <em>
   United States v. Spilotro,
  </em>
  <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/#963" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and...">800 F.2d 959, 963</a></span> (9th Cir.1986). Therefore, our task is to determine if the language of the Kleinberg warrant is sufficiently particular to achieve the requirements of the fourth amendment.
 </p>
<p id="b696-14">
  The warrant under scrutiny here included only two limitations. First, the documents to be seized had to fall within a long list of business records typical of the documents kept by an export company. Second, those documents had to relate to
  <span citation-index="1" class="star-pagination" label="601"> 
   *601
   </span>
  “the purchase, sale and illegal exportation of materials in violation of the” federal export laws. In this context — the search of the offices of an export company — these limitations provide no limitation at all. The warrant authorizes, and the customs agents conducted, a general search of the Kleinberg offices.
  <a class="footnote" href="#fn13" id="fn13_ref">
   13
  </a>
</p>
<p id="b697-4">
  A.
  <em>
   The warrant is facially overbroad.
  </em>
</p>
<p id="b697-5">
  The Kleinberg warrant suffers from three flaws. First, it authorizes a general search in conjunction with a federal crime and is overbroad on its face. In Foss
  <em>
   v. Bergsgaard,
  </em>
  <span class="citation" data-id="8935318"><a href="/opinion/8944758/voss-v-bergsgaard/" aria-description="Citation for case: Voss v. Bergsgaard">774 F.2d 402</a></span> (10th Cir.1985), we invalidated a similar warrant. The warrant in Foss authorized government agents to seize documents and records “[a]ll of which are evidence of violations of Title <span class="citation no-link">18, United States Code, Section 371</span>.”
  <span class="citation no-link"><em>
   Id.
  </em>
  at 405</span>. We concluded that “[e]ven if the reference to Section 371 [the federal conspiracy statute] is construed as a limitation, it does not constitute a constitutionally adequate particularization of the items to be seized.”
  <em>
   <span class="citation no-link">Id.</span>
  </em>
<a class="footnote" href="#fn14" id="fn14_ref">
<em>
    14
   </em>
</a>
</p>
<p id="b697-10">
  The government argues that
  <em>
   <span class="citation" data-id="8935318"><a href="/opinion/8944758/voss-v-bergsgaard/" aria-description="Citation for case: Voss v. Bergsgaard">Voss</a></span>
  </em>
  does not apply here because the export statutes describe a much narrower range of criminal activity. We disagree. While some federal statutes may be narrow enough to meet the fourth amendment’s requirement, the two statutes cited by the Kleinberg warrant cover a broad range of activity and the reference to those statutes does not sufficiently limit the scope of the warrant.
  <a class="footnote" href="#fn15" id="fn15_ref">
   15
  </a>
</p>
<p id="b697-11">
  Moreover, a series of decisions from other circuits have held that reference to a broad federal statute is not a sufficient limitation on a search warrant. For example, in
  <em>
   Roche v. United States,
  </em>
  <span class="citation" data-id="373913"><a href="/opinion/373913/united-states-v-john-c-roche/#7" aria-description="Citation for case: United States v. John C. Roche">614 F.2d 6, 7</a></span> (1st Cir.1980) the warrant authorized the seizure of books, records and documents “which are evidence, fruits, and instrumen-talities of the violation of Title <span class="citation no-link">18, United States Code Section 1341</span> [mail fraud].” The court found this limitation to be “no
  <span citation-index="1" class="star-pagination" label="602"> 
   *602
   </span>
  limitation at all.”
  <span class="citation no-link"><em>
   Id.
  </em>
  at 8</span>. The Ninth Circuit has consistently applied the same rule. In
  <em>
   United States v. Cardwell,
  </em>
  <span class="citation" data-id="405042"><a href="/opinion/405042/united-states-v-james-b-cardwell-united-states-of-america-v-marvin/#77" aria-description="Citation for case: United States v. James B. Cardwell, United States of...">680 F.2d 75, 77</a></span> (9th Cir.1982), “[t]he only limitation on the search and seizure of appellants’ business papers was the requirement that they be the instrumentality or evidence of violation of the general tax evasion statute, <span class="citation no-link">26 U.S.C. § 7201</span>. That is not enough.” The court’s reasoning in
  <em>
   Card-well
  </em>
  is equally applicable here:
 </p>
<blockquote id="b698-4">
  “ ‘[Limiting’ the search to only records that are evidence of the violation of a certain statute is generally not enough.... If items that are illegal, fraudulent, or evidence of illegality are sought, the warrant must contain some guidelines to aid the determination of what may or may not be seized.”
 </blockquote>
<p id="b698-5">
<span class="citation no-link"><em>
   Id.
  </em>
  at 78</span>. Where the warrant provides no such guidelines, it is impermissibly over-broad on its face.
  <em>
   See also Rickert v. Sweeney,
  </em>
  <span class="citation" data-id="8949178"><a href="/opinion/8958115/rickert-v-sweeney/#909" aria-description="Citation for case: Rickert v. Sweeney">813 F.2d 907, 909</a></span> (8th Cir.1987) (warrant limited only by references to the general conspiracy statute and general tax evasion statute did “not limit the search in any substantive manner”);
  <em>
   United States v. Spilotro,
  </em>
  <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/#965" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and...">800 F.2d 959, 965</a></span> (9th Cir.1986) (“effort to limit discretion solely by reference to criminal statutes was inadequate”);
  <em>
   United States v. Abrams,
  </em>
  <span class="citation" data-id="9842939"><a href="/opinion/374752/united-states-v-maurice-abrams/#542" aria-description="Citation for case: United States v. Maurice Abrams">615 F.2d 541, 542-43</a></span> (1st Cir.1980) (warrant limited only by reference to records and federal fraud statute is overbroad); In re
  <em>
   Lafayette Academy,
  </em>
  <span class="citation" data-id="9466280"><a href="/opinion/371945/in-the-matter-of-the-application-of-lafayette-academy-inc-appeal-of/#3" aria-description="Citation for case: In the Matter of the Application of Lafayette Academy,...">610 F.2d 1, 3</a></span> (1st Cir.1979) (over-broad warrant allowed “seizure of most every sort of book or paper ... limited only by the qualification that the seized item be evidence of violations of ... ‘18 U.S.C. 286, 287, 371, 1001 and 1014.’ ”).
 </p>
<p id="b698-9">
  We agree with the reasoning of these courts. As an irreducible minimum, a proper warrant must allow the executing officers to distinguish between items that may and may not be seized.
  <a class="footnote" href="#fn16" id="fn16_ref">
   16
  </a>
<em>
   See
  </em>
  2 La-Fave, § 4.6(a), at 235-36. The Kleinberg warrant does not provide that guidance. An unadorned reference to a broad federal statute does not sufficiently limit the scope of a search warrant. Absent other limiting factors, such a warrant does not comply with the requirements of the fourth amendment.
  <a class="footnote" href="#fn17" id="fn17_ref">
   17
  </a>
<em>
   See Andresen v. Maryland,
  </em>
  <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#480" aria-description="Citation for case: Andresen v. Maryland">427 U.S. 463, 480-82</a></span>, <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#2748" aria-description="Citation for case: Andresen v. Maryland">96 S.Ct. 2737, 2748-49</a></span>, <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">49 L.Ed.2d 627</a></span> (1976).
 </p>
<p id="b698-10">
  Nor did the list of business records to be seized provide any meaningful limitation on the Kleinberg search. The warrant encompassed virtually every document that one might expect to find in a modem export company’s office. Again, the fourth amendment requires more.
  <em>
   See Id.; see also In re Grand Jury Proceedings (Young),
  </em>
  <span class="citation" data-id="9471119"><a href="/opinion/424091/in-re-grand-jury-proceedings-appeal-of-robert-e-young/#498" aria-description="Citation for case: In Re Grand Jury Proceedings. Appeal of Robert E. Young">716 F.2d 493, 498</a></span> (8th Cir.1983) (“laundry list of various type of records is insufficient to save the search warrant”);
  <em>
   Roberts v. United States,
  </em>
  <span class="citation" data-id="1394599"><a href="/opinion/1394599/roberts-v-united-states/#934" aria-description="Citation for case: Roberts v. United States">656 F.Supp. 929, 934</a></span> (S.D.N.Y.1987) (“By listing every type
  <span citation-index="1" class="star-pagination" label="603"> 
   *603
   </span>
  of record that could conceivably be found in an office, the warrant effectively authorized the inspectors to cart away anything that they could find on the premises.”);
  <em>
   cf. Cardwell,
  </em>
  <span class="citation" data-id="405042"><a href="/opinion/405042/united-states-v-james-b-cardwell-united-states-of-america-v-marvin/#78" aria-description="Citation for case: United States v. James B. Cardwell, United States of...">680 F.2d at 78</a></span>;
  <em>
   Abrams,
  </em>
  <span class="citation" data-id="9842939"><a href="/opinion/374752/united-states-v-maurice-abrams/#543" aria-description="Citation for case: United States v. Maurice Abrams">615 F.2d at 543</a></span>;
  <em>
   Roche,
  </em>
  <span class="citation" data-id="373913"><a href="/opinion/373913/united-states-v-john-c-roche/#7" aria-description="Citation for case: United States v. John C. Roche">614 F.2d at 7</a></span>;
  <em>
   Lafayette Academy,
  </em>
  <span class="citation" data-id="9466280"><a href="/opinion/371945/in-the-matter-of-the-application-of-lafayette-academy-inc-appeal-of/#5" aria-description="Citation for case: In the Matter of the Application of Lafayette Academy,...">610 F.2d at 5</a></span>.
 </p>
<p id="b699-4">
  We recognize that some lower courts have found similar warrants to be sufficiently particular. The government relies on
  <em>
   United States v. Moller-Butcher,
  </em>
  <span class="citation" data-id="1482053"><a href="/opinion/1482053/united-states-v-moller-butcher/#557" aria-description="Citation for case: United States v. Moller-Butcher">560 F.Supp. 550, 557</a></span> (D.Mass.1983) where the district court found a warrant seeking “records which are required under the Export Administration Act, <span class="citation no-link">15 C.F.R. § 387.13</span>, by all businesses sending electronic equipment outside the United States” to be sufficiently particular. The district court in
  <em>
   United States v. Gregg,
  </em>
  <span class="citation" data-id="1577597"><a href="/opinion/1577597/united-states-v-gregg/#966" aria-description="Citation for case: United States v. Gregg">629 F.Supp. 958, 966-67</a></span> (W.D.No.1986),
  <em>
   aff'd
  </em>
  <span class="citation" data-id="495037"><a href="/opinion/495037/united-states-v-werner-ernst-gregg-and-roswitha-gregg/" aria-description="Citation for case: United States v. Werner Ernst Gregg and Roswitha Gregg">829 F.2d 1430</a></span> (8th Cir.1987), approved a similar warrant. We are unpersuaded by these decisions. Neither court clearly explained why the warrant in question is sufficient; the analysis is brief and concluso-ry.
  <a class="footnote" href="#fn18" id="fn18_ref">
   18
  </a>
  Moreover, there are distinguishing features that limit the value of these decisions in our present inquiry.
  <a class="footnote" href="#fn19" id="fn19_ref">
   19
  </a>
</p>
<p id="b699-5">
  The government also argues that the facial overbreadth of the warrant is not fatal because any doubts about what was to be seized “could be resolved by resort to the affidavit which was a part of the warrant and which the agents had with them at the location of the search.” Brief of Appellant at 38. We disagree. It is true that the particularity of an affidavit may cure an overbroad warrant, but only “where the affidavit and the search warrant ... can be reasonably said to constitute one document. Two requirements must be satisfied to reach this result: first, the affidavit and search warrant must be physically connected so that they constitute one document; and second, the search warrant must expressly refer to the affidavit and incorporate it by reference using suitable words of reference.” 2 LaFave, § 4.6(a), at 241 (quoting
  <em>
   Bloom v. State,
  </em>
  <span class="citation" data-id="1876547"><a href="/opinion/1876547/bloom-v-state/" aria-description="Citation for case: Bloom v. State">283 So.2d 134</a></span> (Fla.App.1973));
  <em>
   see <span class="citation" data-id="1876547"><a href="/opinion/1876547/bloom-v-state/" aria-description="Citation for case: Bloom v. State">Id.</a></span>
  </em>
  cases cited at n. 28; 3 C. Wright,
  <em>
   Federal Practice and Procedure
  </em>
  § 670, at 723 (2d ed. 1982);
  <em>
   United States v. Medlin,
  </em>
  <span class="citation" data-id="474635"><a href="/opinion/474635/united-states-v-arvle-edgar-medlin/" aria-description="Citation for case: United States v. Arvle Edgar Medlin">798 F.2d 407</a></span>, 410 n. 1 (10th Cir.1986) (“When an affidavit is
  <em>
   attached
  </em>
  to a warrant and incorporated by reference into the warrant, it can be used to cure a lack of particularity.”);
  <a class="footnote" href="#fn20" id="fn20_ref">
   20
  </a>
<em>
   United States v. Hayes,
  </em>
  <span class="citation" data-id="9475068"><a href="/opinion/472649/united-states-v-jude-r-hayes/#1354" aria-description="Citation for case: United States v. Jude R. Hayes">794 F.2d 1348, 1354</a></span> (9th Cir.1986),
  <em>
   cert. denied,
  </em>
  — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./107/1289/">107 S.Ct. 1289</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/94/146/">94 L.Ed.2d 146</a></span> (1987) (affidavits did not accompany warrant);
  <em>
   United States v. Strand,
  </em>
  <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/#453" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers">761 F.2d 449, 453</a></span> (8th Cir.1985) (affidavit accompanied warrant but was not incorporated).
 </p>
<p id="b699-11">
  The Kleinberg warrant did not incorporate the affidavit; there is no reference to the affidavit on the face of the warrant. In addition, there is no clear evidence in the record to support the government’s assertion that the affidavit “was a part of the warrant.” Finally, and perhaps most importantly, the search itself was not limited by the affidavit. If the affidavit was available to the agents searching the Kleinberg
  <span citation-index="1" class="star-pagination" label="604"> 
   *604
   </span>
  offices, it certainly was not used to limit the search.
  <a class="footnote" href="#fn21" id="fn21_ref">
   21
  </a>
  The agents seized documents related to transactions, countries and commodities not mentioned in the affidavit. In fact, the agents seized documents unrelated to Kleinberg’s export business.
  <a class="footnote" href="#fn22" id="fn22_ref">
   22
  </a>
  Even if the technical requirements for incorporation were met, it would be improper to allow the affidavit to cure the lack of particularity in the warrant where the government agents relied on the breadth of the warrant, not the specificity of the affidavit, to define the scope of the search.
  <em>
   Cf. United States v. Spilotro,
  </em>
  <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/#967" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and...">800 F.2d 959, 967</a></span> (9th Cir.1986) (“government’s argument that the agents were somehow constructively guided by the affidavit in executing the warrants is unpersuasive”);
  <em>
   Lafayette Academy,
  </em>
  <span class="citation" data-id="9466280"><a href="/opinion/371945/in-the-matter-of-the-application-of-lafayette-academy-inc-appeal-of/#5" aria-description="Citation for case: In the Matter of the Application of Lafayette Academy,...">610 F.2d at 5</a></span> (“[S]elf-restraint on the part of the ... executing officers does not erase the fact that under the broadly worded warrant appellees were subject to a greater exercise of power than that which may have actually transpired and for which probable cause had been established. The particularity requirement is a check to just this sort of risk.” (citations omitted)).
 </p>
<p id="b700-4">
  B.
  <em>
   Information was available to make the warrant more particular.
  </em>
</p>
<p id="b700-5">
  In addition to being overbroad on its face, the Kleinberg warrant is flawed because information was available to the government to make the description of the items to be seized much more particular. Admittedly, a general description is not always invalid.
 </p>
<blockquote id="b700-9">
  “Courts tend to tolerate a greater degree of ambiguity [in the warrant’s description] where law enforcement agents have done the best that could reasonably be expected under the circumstances, have acquired all the descriptive facts which a reasonable investigation could be expected to cover, and have insured that all those facts were included in the warrant.”
 </blockquote>
<p id="b700-10">
<em>
   United States v. Young,
  </em>
  <span class="citation" data-id="8925220"><a href="/opinion/8934968/united-states-v-young/#759" aria-description="Citation for case: United States v. Young">745 F.2d 733, 759</a></span> (2d Cir.1984),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./470/1084/">470 U.S. 1084</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./105/1842/">105 S.Ct. 1842</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/85/142/">85 L.Ed.2d 142</a></span> (1985). In this case, however, the government’s argument that the warrant was “as specific as the circumstances and the nature of the activity under investigation permit” is untenable. Agent Juhasz’ affidavit in support of the warrant was very specific, alleging the attempted illegal export of a specific product to the People’s Republic of China via a series of specific companies in Hong Kong. Yet none of this information was reflected in the warrant. The warrant could have been limited to documents related to the Micro-tel transaction, to the companies suspected of participating in the illegal export, to the countries involved in the route of the export, Hong Kong and China, or to a specific period of time coincident to the suspect transaction. Yet the government chose to include none of these limiting factors. As the Ninth Circuit found in
  <em>
   <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and...">Spilotro</a></span>,
  </em>
</p>
<blockquote id="b701-3">
<span citation-index="1" class="star-pagination" label="605"> 
   *605
   </span>
  “[T]he government could have narrowed most of the descriptions in the warrants either by describing in greater detail the items one commonly expects to find on premises used for the criminal activities in question, or at the very least, by describing the criminal activities themselves rather than simply referring to the statute believed to have been violated. As the warrants stand, however, they authorize wholesale seizures of entire categories of items not generally evidence of criminal activity, and provide no guidelines to distinguish items used lawfully from those the government had probable cause to seize.”
 </blockquote>
<p id="b701-4">
<em>
   Spilotro,
  </em>
  <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/#964" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and...">800 F.2d at 964</a></span>;
  <em>
   see also United States v. Fuccillo,
  </em>
  <span class="citation" data-id="480985"><a href="/opinion/480985/united-states-v-carl-a-fuccillo/#176" aria-description="Citation for case: United States v. Carl A. Fuccillo">808 F.2d 173, 176</a></span> (1st Cir.) (“ ‘In light of the information available to the agents which could have served to narrow the scope of the warrant and protect the defendants’ personal rights, the warrant was inadequate.’ ”) (quoting
  <em>
   United States v. Klein,
  </em>
  <span class="citation" data-id="9464268"><a href="/opinion/350518/united-states-v-allan-michael-klein/#190" aria-description="Citation for case: United States v. Allan Michael Klein">565 F.2d 183, 190</a></span> (1st Cir.1977)),
  <em>
   cert. denied,
  </em>
  — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./107/2481/">107 S.Ct. 2481</a></span>, <span class="citation no-link">96 L.Ed.2d 374</span> (1987);
  <em>
   United States v. Cook,
  </em>
  <span class="citation" data-id="393709"><a href="/opinion/393709/united-states-v-lee-cook-and-jackie-b-kirk/#733" aria-description="Citation for case: United States v. Lee Cook and Jackie B. Kirk">657 F.2d 730, 733</a></span> (5th Cir. Unit A Sept.1981) (“Failure to employ the specificity available will invalidate a general description in a warrant.”).
 </p>
<p id="b701-7">
  C.
  <em>
   The scope of the warrant exceeded the probable cause.
  </em>
</p>
<p id="b701-8">
  The final factor leading us to conclude that the Kleinberg warrant was impermissibly overbroad is that even if we assume that Agent Juhasz’ affidavit established probable cause to issue a search warrant, the scope of the warrant far exceeded the probable cause to support it. The fourth amendment requires not only that the warrant sufficiently specify the evidence to be seized, but also that the scope of the warrant be limited to the specific areas and things for which there is probable cause to search.
  <em>
   Maryland v. Garrison,
  </em>
  <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/" aria-description="Citation for case: Maryland v. Garrison">480 U.S. 79</a></span>, <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#1017" aria-description="Citation for case: Maryland v. Garrison">107 S.Ct. 1013, 1017</a></span>, <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/" aria-description="Citation for case: Maryland v. Garrison">94 L.Ed.2d 72</a></span> (1987). “An otherwise unobjectionable description of the objects to be seized is defective if it is broader than can be justified by the probable cause upon which the warrant is based.” 2 LaFave, § 4.6(a), at 236;
  <em>
   see United States v. Bentley,
  </em>
  <span class="citation" data-id="492430"><a href="/opinion/492430/united-states-v-david-bentley-richard-degen-allen-yung-and-walter/#1110" aria-description="Citation for case: United States v. David Bentley, Richard Degen, Allen...">825 F.2d 1104, 1110</a></span> (7th Cir.) (“When the probable cause covers fewer documents in a system of files, the warrant must ... tell the officers how to separate the documents to be seized from others.”),
  <em>
   cert. denied,
  </em>
  — U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./108/240/">108 S.Ct. 240</a></span>, <span class="citation no-link">98 L.Ed.2d 198</span> (1987);
  <em>
   Rickert v. Sweeney,
  </em>
  <span class="citation" data-id="8949178"><a href="/opinion/8958115/rickert-v-sweeney/#909" aria-description="Citation for case: Rickert v. Sweeney">813 F.2d 907, 909</a></span> (8th Cir.1987) (“Although probable cause existed to search the records of one particular project, the warrant failed to so limit the search.”);
  <em>
   Spilo-tro,
  </em>
  <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/#967" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and...">800 F.2d at 967</a></span> (list of criminal statutes in warrant went beyond probable cause in affidavit);
  <em>
   Voss,
  </em>
  <span class="citation" data-id="8935318"><a href="/opinion/8944758/voss-v-bergsgaard/#408" aria-description="Citation for case: Voss v. Bergsgaard">774 F.2d at 408</a></span> (Logan, J., concurring) (“The breadth of a warrant must be justified by the breadth of the probable cause.”);
  <em>
   cf. VonderAhe v. Howland,
  </em>
  <span class="citation" data-id="9461326"><a href="/opinion/324061/donn-vonderahe-and-barbara-vonderahe-v-roy-h-howland/#369" aria-description="Citation for case: Donn Vonderahe and Barbara Vonderahe v. Roy H. Howland">508 F.2d 364, 369</a></span> (9th Cir.1974) (“[Ajlthough there may have been ‘probable cause’ to search for and seize [records of a certain type and date] there was no probable cause shown for a seizure of all the ... books and records, or ... personal and private papers.”) In other words, a search warrant is also impermissibly over-broad if it authorizes the search and seizure of evidence that is not supported by probable cause. A generous reading of the affidavit may disclose probable cause for a search of the Kleinberg offices limited to documentary evidence of transactions related to the Micro-tel receiver or to shipments to Hong Kong, but in no event is there probable cause to support a general search for evidence of violations of the export laws. The government asserts that the affidavit “describ[ed] a systematic scheme for committing a specific narrow export offense.” Reply Brief of Appellant at 15. That is not accurate; the affidavit includes only a general reference to the export of electronic equipment to the People’s Republic of China through Hong Kong, and references no Kleinberg transactions apart from the export of the Micro-tel receiver.
 </p>
<p id="b701-13">
  In summary, we find the Kleinberg warrant overbroad in every respect.
  <a class="footnote" href="#fn23" id="fn23_ref">
   23
  </a>
  The
  <span citation-index="1" class="star-pagination" label="606"> 
   *606
   </span>
  warrant contains no limitation on the scope of the search, it is not as particular as the circumstances would allow or require and it extends far beyond the scope of the supporting affidavit. The warrant is invalid and we must determine if the evidence seized should be suppressed.
 </p>
<p id="b702-4">
  IY. Exclusion
 </p>
<p id="b702-5">
  Our conclusion that the Kleinberg warrant was invalid does not necessarily mean that the evidence seized under the warrant must be suppressed. The government argues that we should apply the “good faith” exception
  <a class="footnote" href="#fn24" id="fn24_ref">
   24
  </a>
  to the exclusionary rule created in
  <em>
   United States v. Leon,
  </em>
  <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U.S. 897</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">82 L.Ed.2d 677</a></span> (1984) and reverse the district court’s decision.
  <a class="footnote" href="#fn25" id="fn25_ref">
   25
  </a>
  The district court found the good faith exception inapplicable, but we note that whether the “good faith” exception to the exclusionary rule should be applied is a question of law, subject to
  <em>
   de novo
  </em>
  review by this court.
  <a class="footnote" href="#fn26" id="fn26_ref">
   26
  </a>
<em>
   See United States v. Mi-
  </em>
<span citation-index="1" class="star-pagination" label="607"> 
   *607
   </span>
<em>
   chaelian,
  </em>
  <span class="citation" data-id="478417"><a href="/opinion/478417/united-states-v-ara-michaelian/#1046" aria-description="Citation for case: United States v. Ara Michaelian">803 F.2d 1042, 1046</a></span> (9th Cir.1986);
  <em>
   United States v. Maggitt,
  </em>
  <span class="citation" data-id="461601"><a href="/opinion/461601/united-states-v-willie-b-maggitt-aka-willie-b-madgett/#1034" aria-description="Citation for case: United States v. Willie B. Maggitt, A/K/A Willie B. Madgett">778 F.2d 1029, 1034-35</a></span> (5th Cir.1985),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./476/1184/">476 U.S. 1184</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./106/2920/">106 S.Ct. 2920</a></span>, <span class="citation" data-id="9054533"><a href="/opinion/9060924/keplinger-v-united-states/" aria-description="Citation for case: Keplinger v. United States">91 L.Ed.2d 548</a></span> (1986).
 </p>
<p id="b703-4">
  In
  <em>
   <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>,
  </em>
  the Supreme Court modified the fourth amendment exclusionary rule to provide that evidence seized under a warrant later found to be invalid may be admissible if the executing officers acted in good faith and in reasonable reliance on the warrant.
  <em>
   United States v. Medlin,
  </em>
  <span class="citation" data-id="474635"><a href="/opinion/474635/united-states-v-arvle-edgar-medlin/#409" aria-description="Citation for case: United States v. Arvle Edgar Medlin">798 F.2d 407, 409</a></span> (10th Cir.1986);
  <em>
   see generally
  </em>
  1 LaFave § 1.3. The
  <em>
   <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>
  </em>
  Court applied the “good faith” exception to admit the evidence from a search warrant subsequently invalidated by a lack of probable cause. In
  <em>
   Massachusetts v. Sheppard,
  </em>
  <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#988" aria-description="Citation for case: Massachusetts v. Sheppard">468 U.S. 981, 988</a></span>, <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#3427" aria-description="Citation for case: Massachusetts v. Sheppard">104 S.Ct. 3424, 3427</a></span>, <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">82 L.Ed.2d 737</a></span> (1984) the Court held that the same exception could also be applied to warrants that violate the fourth amendment’s particularity requirement.
 </p>
<p id="b703-5">
  Of course,
  <em>
   <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>
  </em>
  does not mean that evidence obtained under an invalid warrant should never be suppressed. “The Court mandated that the exclusionary rule be invoked only in those ‘unusual’ cases in which its purposes would be served, i.e., in which it would deter police misconduct.”
  <em>
   Medlin,
  </em>
  <span class="citation" data-id="474635"><a href="/opinion/474635/united-states-v-arvle-edgar-medlin/#409" aria-description="Citation for case: United States v. Arvle Edgar Medlin">798 F.2d at 409</a></span>. The Court also identified certain circumstances where suppression remains an appropriate remedy, including where the warrant is “so facially
  <em>
   deficient
  </em>
  — i.e., in failing to particularize the place to be searched or the things to be seized — that the executing officers cannot reasonably presume it to be valid.”
  <em>
   Leon,
  </em>
  <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#923" aria-description="Citation for case: United States v. Leon">468 U.S. at 923</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#3420" aria-description="Citation for case: United States v. Leon">104 S.Ct. at 3420</a></span> (citations omitted).
  <a class="footnote" href="#fn27" id="fn27_ref">
   27
  </a>
  In determining whether the exception should be applied, the “good-faith inquiry is confined to the objectively ascertainable question whether a reasonably well trained officer would have known that the search was illegal despite the magistrate’s authorization.”
  <em>
   Leon,
  </em>
  <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U.S. at 922</a></span> n. 23, 104 S.Ct. at 3420 n. 23. To answer this “objectively ascertainable question,” we are to consider “all of the circumstances,”
  <em>
   id.
  </em>
  and assume that the executing “officers have a reasonable knowledge of what the law prohibits.”
  <em>
   Id.
  </em>
  at 919 n. 20, 104 S.Ct. at 3419 n. 20. Accordingly, under
  <em>
   <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>
  </em>
  and
  <em>
   <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard</a></span>,
  </em>
  even though we have previously determined the Kleinberg warrant to be facially invalid, we must also review the text of the warrant and the circumstances of the search to ascertain whether the agents might have “reasonably presume[d] it to be valid.”
  <em>
   Leon,
  </em>
  <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#923" aria-description="Citation for case: United States v. Leon">468 U.S. at 923</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#3420" aria-description="Citation for case: United States v. Leon">104 S.Ct. at 3420</a></span>.
 </p>
<p id="b703-10">
  The application of the “good faith” exception to an overbroad warrant has not yet been directly addressed by this court. However, there is guidance from other courts of appeals. This question has been most frequently considered by the Ninth Circuit. In
  <em>
   United States v. Crozier, 111
  </em>
  F.2d 1376, 1379 (9th Cir.1985) the government executed a warrant “that did not describe any particular property to be seized; it merely authorized the seizure of ‘Material evidence of violation 21 USC 841, 846.’ ” The court found the warrant facially over-broad and held that the agent could not reasonably rely on it.
  <span class="citation no-link"><em>
   Id.
  </em>
  at 1381</span>. “In contrast to the detective in
  <em>
   Sheppard,”
  </em>
  and similar to the customs agents here, the Ninth Circuit found that the agent “did not take ‘every step that could reasonably be expected of him.’”
  <em>
   <span class="citation no-link">Id.</span>
  </em>
  at 1382 (citing
  <em>
   Sheppard,
  </em>
  <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#989" aria-description="Citation for case: Massachusetts v. Sheppard">468 U.S. at 989</a></span>, <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#3428" aria-description="Citation for case: Massachusetts v. Sheppard">104 S.Ct. at 3428</a></span>). Specifically, the agent in
  <em>
   Crozier
  </em>
  failed to make the warrant as particular as the information available would allow and
  <span citation-index="1" class="star-pagination" label="608"> 
   *608
   </span>
  “obtained no specific assurance from the magistrate that the overbroad warrant was acceptable.”
  <em>
   <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Id.</a></span>
  </em>
</p>
<p id="b704-4">
  The Ninth Circuit reached the same conclusion in
  <em>
   United States v. Spilotro,
  </em>
  <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and...">800 F.2d 959</a></span> (9th Cir.1986). In
  <em>
   <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and...">Spilotro</a></span>,
  </em>
  the warrant authorized the search and seizure of property and records which were “evidence of violations” of a list of federal criminal statutes.
  <span class="citation" data-id="9475343"><a href="/opinion/475840/united-states-v-john-spilotro-herbert-blitzstein-and-joseph-c-blasko/#961" aria-description="Citation for case: United States v. John Spilotro Herbert Blitzstein and..."><em>
   Id.
  </em>
  at 961</a></span>. The court relied on
  <em>
   Crozier
  </em>
  to find that the “good faith” exception was inapplicable to a facially overbroad warrant.
  <em>
   See also United States v. Washington,
  </em>
  <span class="citation" data-id="474531"><a href="/opinion/474531/united-states-v-ralph-h-washington/#1473" aria-description="Citation for case: United States v. Ralph H. Washington">797 F.2d 1461, 1473</a></span> (9th Cir.1986) (“the overbroad sections of the ... warrant are so facially deficient that any evidence obtained in reliance upon either of them must be suppressed”);
  <em>
   cf. United States v. Michaelian,
  </em>
  <span class="citation" data-id="478417"><a href="/opinion/478417/united-states-v-ara-michaelian/#1047" aria-description="Citation for case: United States v. Ara Michaelian">803 F.2d 1042, 1047</a></span> (9th Cir.1986) (warrants did not “approximate the degree of facial deficiency which would preclude objective reasonable reliance”).
 </p>
<p id="b704-5">
  The First Circuit has adopted similar reasoning. In
  <em>
   United States v. Fuccillo,
  </em>
  <span class="citation" data-id="480985"><a href="/opinion/480985/united-states-v-carl-a-fuccillo/#176" aria-description="Citation for case: United States v. Carl A. Fuccillo">808 F.2d 173,176-77</a></span> (1st Cir.),
  <em>
   cert. denied,
  </em>
  — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./107/2481/">107 S.Ct. 2481</a></span>, <span class="citation no-link">96 L.Ed.2d 374</span> (1987), the court invalidated warrants that inadequately described the stolen goods to be seized. As in this case, the court found that the “executing agents ... had no ‘physical criteria or detailed description in the warrant to enable them to determine what they might lawfully seize.’ ”
  <em>
   <span class="citation no-link">Id.</span>
  </em>
  at 177 (quoting
  <em>
   Montilla Records of Puerto Rico v. Morales,
  </em>
  <span class="citation" data-id="9464772"><a href="/opinion/355493/application-of-montilla-records-of-puerto-rico-inc-v-the-honorable-julio/#326" aria-description="Citation for case: Application of Montilla Records of Puerto Rico, Inc. v....">575 F.2d 324, 326-27</a></span> (1st Cir.1978)).
  <em>
   <span class="citation" data-id="480985"><a href="/opinion/480985/united-states-v-carl-a-fuccillo/" aria-description="Citation for case: United States v. Carl A. Fuccillo">Fuccillo</a></span>
  </em>
  also determined that the “good faith” exception was inapplicable, but focused on a different aspect of
  <em>
   <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>.
  </em>
  The warrant in
  <em>
   <span class="citation" data-id="480985"><a href="/opinion/480985/united-states-v-carl-a-fuccillo/" aria-description="Citation for case: United States v. Carl A. Fuccillo">Fuccillo</a></span>
  </em>
  authorized the FBI to seize cartons of women’s clothing and records related to those cartons. However, in executing the warrant, “the agents seized, in addition to the authorized cartons of
  <em>
   women’s
  </em>
  clothing, racks of clothing, empty boxes, and most disturbingly, two racks of
  <em>
   men’s
  </em>
  clothing. The
  <em>
   entire contents
  </em>
  of [a] warehouse were seized.”
  <span class="citation" data-id="480985"><a href="/opinion/480985/united-states-v-carl-a-fuccillo/#177" aria-description="Citation for case: United States v. Carl A. Fuccillo"><em>
   Id.
  </em>
  at 177-78</a></span> (emphasis in original). The court found the “good faith” exception inapplicable for three reasons. First, the agents exceeded the scope of the warrant. Second, the “agents were reckless in not including in the affidavit information which was known or easily accessible to them.”
  <span class="citation" data-id="480985"><a href="/opinion/480985/united-states-v-carl-a-fuccillo/#178" aria-description="Citation for case: United States v. Carl A. Fuccillo"><em>
   Id.
  </em>
  at 178</a></span>. Finally, the warrant was “ ‘so facially deficient... that the executing officers cannot reasonably presume it to be valid.’ ”
  <em>
   <span class="citation" data-id="480985"><a href="/opinion/480985/united-states-v-carl-a-fuccillo/" aria-description="Citation for case: United States v. Carl A. Fuccillo">Id.</a></span>
  </em>
  at 178 (quoting
  <em>
   Leon,
  </em>
  <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#923" aria-description="Citation for case: United States v. Leon">468 U.S. at 923</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#3420" aria-description="Citation for case: United States v. Leon">104 S.Ct. at 3420</a></span>).
  <em>
   Cf. United States v. Diaz,
  </em>
  <span class="citation" data-id="502477"><a href="/opinion/502477/united-states-v-leoncio-l-diaz-aka-leonel-diaz/#6" aria-description="Citation for case: United States v. Leoncio L. Diaz, A/K/A Leonel Diaz">841 F.2d 1, 6</a></span> (1st Cir.1988) (“[W[hile the warrant was overbroad ..., it was not so facially deficient that [the Agent] could not have reasonably and in good faith believed that it adequately authorized the search he undertook.”).
  <a class="footnote" href="#fn28" id="fn28_ref">
   28
  </a>
  The findings in
  <em>
   Fucillo
  </em>
  parallel our analysis of the Kleinberg warrant and search.
 </p>
<p id="b704-10">
  We are also in accord with the Eighth Circuit’s analysis of the “good faith” exception in
  <em>
   United States v. Strand,
  </em>
  <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers">761 F.2d 449</a></span> (8th Cir.1985). The warrant in
  <em>
   <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers">Strand</a></span>
  </em>
  authorized the search of an apartment for “stolen mail which is evidence of and the fruits of the crime of theft from the mail.”
  <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/#452" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers"><em>
   Id.
  </em>
  at 452</a></span>. The postal inspectors executing the warrant found stolen mail, but also seized certain household items that matched items that had been reported missing. The court held that the “warrant authorized a search only for ‘stolen mail,’ and that it did not describe the other items to be seized with sufficient particularity to be valid under the Fourth Amendment.”
  <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/#453" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers"><em>
   Id.
  </em>
  at 453-54</a></span>. The court then considered whether the evidence was admissible under the “good faith” exception, concluding that there was no “objectively reasonable basis for the postal inspectors to have believed that the warrant authorized the seizure of [the household] items” and that the exception did not apply.
  <a class="footnote" href="#fn29" id="fn29_ref">
   29
  </a>
<span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/#456" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers"><em>
   Id.
  </em>
  at 456</a></span>. Again, the court’s reasoning is applicable to the Klein-berg warrant and search. First, the
  <em>
   <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers">Strand</a></span>
  </em>
  court noted that the “seizure of ordinary household goods ... went far beyond the seizure expressly authorized by
  <span citation-index="1" class="star-pagination" label="609"> 
   *609
   </span>
  the
  <em>
   warrant_” <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers">Id.</a></span>
  </em>
  Second, the “seizure of household items ... not only went beyond the seizure contemplated by the warrant, but also went far beyond the seizure contemplated by the affidavit.”
  <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/#457" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers"><em>
   Id.
  </em>
  at 457</a></span>. Thus, the postal inspectors could not “reasonably believe” they had the authority to seize the household items. The court also found “no showing of any good reason for the lack of more particularized descriptions.”
  <em>
   <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers">Id.</a></span>
  </em>
</p>
<p id="b705-5">
  We have found only one appellate decision that reaches a contrary conclusion.
  <a class="footnote" href="#fn30" id="fn30_ref">
   30
  </a>
  In
  <em>
   United States v. Buck,
  </em>
  <span class="citation" data-id="484648"><a href="/opinion/484648/united-states-v-marilyn-buck/" aria-description="Citation for case: United States v. Marilyn Buck">813 F.2d 588</a></span> (2d Cir.),
  <em>
   cert. denied,
  </em>
  — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./108/167/">108 S.Ct. 167</a></span>, <span class="citation no-link">98 L.Ed.2d 121</span> (1987) police officers were investigating the robbery of an armored car. Witnesses identified a car leaving the scene with several gunmen. Working through the night, the police traced the car to an apartment and sought a telephone warrant to search the apartment. The judge placed the officer under oath, elicited details of the crime and investigation and then verbally authorized a warrant “to seize any papers, things or property of any kind relating to previously described crime.”
  <span class="citation no-link"><em>
   Id.
  </em>
  at 590</span>. The court found the language of the warrant impermissibly broad, but found no police misconduct: “While it can safely be said that the police here performed reasonably under the circumstances and collected all the ‘descriptive facts’ they could ... they clearly did not insure that all known facts were included in the warrant. The warrant only described the crimes — and gave no limitation whatsoever on the kind of evidence sought.”
  <span class="citation no-link"><em>
   Id.
  </em>
  at 591-92</span>. The court found the evidence admissible under
  <em>
   <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>
  </em>
  and
  <em>
   <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard</a></span>
  </em>
  because “the officers made considerable efforts to comply with the dictates of the Fourth Amendment.”
  <em>
   Id.
  </em>
  at 592. The court reasoned that the evidence should not be suppressed because “the law was unsettled as to how particular the description of the articles to be seized must be” and under those circumstances, “a reasonably well-trained police officer could not be expected to know that the warrant” violated the fourth amendment.
  <em>
   Id.
  </em>
  at 593.
 </p>
<p id="b705-9">
  Obviously,
  <em>
   <span class="citation" data-id="484648"><a href="/opinion/484648/united-states-v-marilyn-buck/" aria-description="Citation for case: United States v. Marilyn Buck">Buck</a></span>
  </em>
  presents a different factual situation than we face here. Moreover, we are not expecting the agents to anticipate legal determinations or resolve ambiguities in the law. A reasonably well-trained officer should know that a warrant must provide guidelines for determining what evidence may be seized.
  <a class="footnote" href="#fn31" id="fn31_ref">
   31
  </a>
  A warrant that directs an officer to seize records “relating to” violations of the federal export laws offers no such guidelines. The officers were left to their own discretion.
 </p>
<p id="b705-10">
  We conclude that the government may not rely on the “good faith” exception in this case and that all evidence seized under the Kleinberg warrant should be suppressed. We find the warrant so facially deficient in its description of the items to be seized that the executing officers could not reasonably rely on it. That conclusion
  <span citation-index="1" class="star-pagination" label="610"> 
   *610
   </span>
  is reinforced by the government’s conduct and the circumstances of the search. This is one of those “unusual” cases where suppression of the evidence is appropriate to deter government misconduct. As we said in
  <em>
   United States v. Owens,
  </em>
  <span class="citation" data-id="463621"><a href="/opinion/463621/united-states-v-merle-ellis-owens/#152" aria-description="Citation for case: United States v. Merle Ellis Owens">782 F.2d 146, 152</a></span> (10th Cir.1986), the search here “exemplifies the very type of official conduct the exclusionary rule is intended to deter.”
  <a class="footnote" href="#fn32" id="fn32_ref">
   32
  </a>
  Accordingly, we hold that the “good faith” exception is inapplicable in these circumstances and affirm the district court’s decision to suppress all of the evidence from the Kleinberg warrant.
 </p>
<p id="b706-4">
  V. Probable Cause
 </p>
<p id="b706-5">
  Because we have decided to suppress the evidence based on the warrant’s over-breadth, there is no need to review the district court’s decision that the warrant was not supported by probable cause.
 </p>
<p id="b706-6">
  The district court’s decision granting defendants’ motion to suppress is AFFIRMED.
 </p>
































<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b690-13">
   . The Micro-tel receiver is a "device used to measure or test the basic output of electronic parts." Brief of Appellees at 2 (citing R. Vol. Ill at 202).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b690-14">
   . The affidavit specifically mentions six companies involved in the Micro-tel transaction: Kleinberg; Micro-tel Corporation, a Maryland manufacturer; Union Air Transport, Kleinberg’s shipping agent in California; Hong Kong Computer Company, the purchaser in Hong Kong; Dataventures International, Ltd., another Hong Kong company which was supposed to purchase the receiver from Hong Kong Computer; and Tak Sing Company of Hong Kong, the final purchaser of the receiver in Hong Kong.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b691-10">
   . According to the district court:
  </p>
<blockquote id="b691-11">
   The evidence shows that the magistrate was led to believe a crime had been committed by the defendants when Agent Juhasz could not himself have believed that the facts he set forth in his affidavit constituted a crime. The affidavit on its face fails to establish probable cause that any crime had been committed if the relevant statutes and facts are examined.
  </blockquote>
<p id="b691-12">
   Mem.Opinion at 5-6.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b691-15">
   . Nevertheless, fourth amendment claims are still commonly analyzed in terms of "standing."
   <em>
    See
   </em>
   3 C. Wright,
   <em>
    Federal Practice and Procedure
   </em>
   § 674 (2d ed. 1982);
   <em>
    see, e.g., United States v. Salvucci,
   </em>
   <span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">448 U.S. 83</a></span>, 87 n. 4, <span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">100 S.Ct. 2547</a></span>, 2551 n. 4, <span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/" aria-description="Citation for case: United States v. Salvucci">65 L.Ed.2d 619</a></span> (1980);
   <em>
    United States v. Skowronski,
   </em>
   <span class="citation" data-id="493687"><a href="/opinion/493687/united-states-v-william-michael-skowronski/#1417" aria-description="Citation for case: United States v. William Michael Skowronski">827 F.2d 1414, 1417-18</a></span> (10th Cir.1987);
   <em>
    United States v. Salazar,
   </em>
   <span class="citation" data-id="479836"><a href="/opinion/479836/united-states-v-edgar-salazar/#1396" aria-description="Citation for case: United States v. Edgar Salazar">805 F.2d 1394, 1396</a></span> (9th Cir.1986);
   <em>
    United States v. Gerena,
   </em>
   <span class="citation" data-id="1392737"><a href="/opinion/1392737/united-states-v-gerena/#1232" aria-description="Citation for case: United States v. Gerena">662 F.Supp. 1218, 1232-40</a></span> (D.Conn.1987).
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b692-7">
   . The government suggests that the defendants’ fourth amendment rights are somehow limited by the reasoning of
   <em>
    Shapiro v. United States,
   </em>
   <span class="citation" data-id="9420211"><a href="/opinion/104585/shapiro-v-united-states/" aria-description="Citation for case: Shapiro v. United States">335 U.S. 1</a></span>, <span class="citation" data-id="9420211"><a href="/opinion/104585/shapiro-v-united-states/" aria-description="Citation for case: Shapiro v. United States">68 S.Ct. 1375</a></span>, <span class="citation no-link">92 L.Ed. 1787</span> (1970) and
   <em>
    Peterman
   </em>
   v.
   <em>
    Coleman,
   </em>
   <span class="citation" data-id="453574"><a href="/opinion/453574/frank-peterman-bruce-horne-v-gerry-coleman-in-his-official-capacity-as/" aria-description="Citation for case: Frank Peterman, Bruce Horne v. Gerry Coleman, in His...">764 F.2d 1416</a></span> (11th Cir.1985). A careful review of those cases demonstrates that they are inapplicable here. Both decisions conclude that the government may impose recordkeeping and inspection requirements on certain businesses without violating the fourth amendment. The validity of the recordkeeping and inspection requirements imposed upon licensed exporters are not at issue.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b693-7">
   . Of course “[a]n expectation of privacy in commercial premises, ... is different from, and indeed less than, a similar expectation in an individual's home. This expectation is particularly attenuated in commercial property employed in ‘closely regulated’ industries."
   <em>
    New York v. Burger,
   </em>
   — U.S. -, <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#2642" aria-description="Citation for case: New York v. Burger">107 S.Ct. 2636, 2642</a></span>, <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/" aria-description="Citation for case: New York v. Burger">96 L.Ed.2d 601</a></span> (1987) (citations omitted). Nevertheless, we reject the government's argument that the nature of the Kleinberg business diminishes the defendants’ expectation of privacy. The reduced expectation of privacy in commercial premises is important in two respects, neither of which is relevant to our disposition of this case. First, the reduced expectation of privacy may justify a statutory authorization of warrantless inspections or searches.
   <em>
    See Id,
   </em>
   at 2643-44. The government concedes that a warrant was required to search the Kleinberg offices. Second, the nature of the premises may "affect the type of evidence that constitutes
   <span citation-index="1" class="star-pagination" label="598"> 
    *598
    </span>
   probable cause to obtain a search warrant in the particular case.”
   <em>
    Blackie’s House of Beef,
   </em>
   <span class="citation" data-id="394830"><a href="/opinion/394830/blackies-house-of-beef-inc-v-leonel-j-castillo-commissioner-of-the/" aria-description="Citation for case: Blackie&#x27;s House of Beef, Inc. v. Leonel J. Castillo,...">659 F.2d at 1216</a></span> n. 5. We find no need to reach the question of probable cause.
   <em>
    See infra
   </em>
   at 610.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b694-6">
   . For an example of ongoing consent treated as a waiver, see
   <em>
    American Postal Workers Union v. United States Postal Service,
   </em>
   <span class="citation" data-id="2595045"><a href="/opinion/2595045/american-postal-workers-union-v-united-states-postal-service/#501" aria-description="Citation for case: American Postal Workers Union v. United States Postal...">671 F.Supp. 497, 501-02</a></span> (S.D.Ohio 1987) (Where "postal regulations, express terms of locker assignment agreements and collective bargaining agreements providefd] for nonconsensual inspection of employee lockers by post office personnel," postal employees "expressly waived any Fourth Amendment rights they might otherwise have in their assigned lockers.”).
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b694-7">
   . We believe that
   <em>
    <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span>
   </em>
   demands that we review the government's "waiver” argument as a question of consent.
   <em>
    See Schneckloth,
   </em>
   <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#246" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. at 246</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#2057" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. at 2057</a></span>. We also find the Court’s quotation from Justice Black instructive: " “Waiver’ is a vague term used for a great variety of purposes, good and bad, in the law.,”
   <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#235" aria-description="Citation for case: Schneckloth v. Bustamonte"><em>
    Id.
   </em>
   at 235</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. at 2052</a></span> (quoting
   <em>
    Green
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9421521"><a href="/opinion/105594/green-v-united-states/#191" aria-description="Citation for case: Green v. United States">355 U.S. 184, 191</a></span>, <span class="citation" data-id="9421521"><a href="/opinion/105594/green-v-united-states/#226" aria-description="Citation for case: Green v. United States">78 S.Ct. 221, 226</a></span>, <span class="citation" data-id="9421521"><a href="/opinion/105594/green-v-united-states/" aria-description="Citation for case: Green v. United States">2 L.Ed.2d 199</a></span> (1957)).
  </p>
</div><div class="footnote" id="fn9" label="9">
<a class="footnote" href="#fn9_ref">
   9
  </a>
<p id="b694-10">
   .The Court’s language in
   <em>
    <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">Bumper</a></span>
   </em>
   has not been applied literally in all cases.
   <em>
    See Comeaux v. Henderson,
   </em>
   <span class="citation" data-id="304369"><a href="/opinion/304369/claude-comeaux-v-c-murray-henderson-warden/#1346" aria-description="Citation for case: Claude Comeaux v. C. Murray Henderson, Warden">462 F.2d 1345, 1346</a></span> (5th Cir.1972) ("not every consent to a search is automatically vitiated simply because a tainted warrant is immediately or remotely involved”);
   <em>
    United States v. Stine,
   </em>
   <span class="citation" data-id="1875700"><a href="/opinion/1875700/united-states-v-stine/#370" aria-description="Citation for case: United States v. Stine">458 F.Supp. 366, 370</a></span> (E.D.Pa.1978) (“In a proper case, a voluntary consent may break the chain of causation between an illegal search warrant and a subsequent search.").
  </p>
<p id="b694-11">
   At the same time, it is clear that the reasoning of
   <em>
    <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">Bumper</a></span>
   </em>
   applies in a commercial context and is relevant here. Professor LaFave has noted "if the businessman admits [a government] inspector only after being told that the inspector has a right to conduct a warrantless inspection, this is not consent but merely an acquiescence to a claim of lawful authority no different than that in
   <em>
    Bumper
   </em>
   v.
   <em>
    <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">North Carolina</a></span>.
   </em>
   If the inspector makes such a claim, then ... ‘the legality of the search depends not on consent but on the authority of a valid statute.’ ’’ 3 LaFave, § 10.2(b), at 637 (quoting in part
   <em>
    United States
   </em>
   v.
   <em>
    Biswell,
   </em>
   <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U.S. 311</a></span>, <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">92 S.Ct. 1593</a></span>, <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">32 L.Ed.2d 87</a></span> (1972)). As we have noted, the export statutes
   <span citation-index="1" class="star-pagination" label="599"> 
    *599
    </span>
   and regulations do not authorize warrantless inspections.
  </p>
</div><div class="footnote" id="fn10" label="10">
<a class="footnote" href="#fn10_ref">
   10
  </a>
<p id="b695-8">
   . In reviewing the district court’s decision on the question of consent, we rely on the lower court’s factual findings unless they are clearly erroneous.
   <em>
    See United States v. Lopez,
   </em>
   <span class="citation" data-id="461084"><a href="/opinion/461084/united-states-v-augustin-alonso-lopez/#548" aria-description="Citation for case: United States v. Augustin Alonso Lopez">777 F.2d 543, 548</a></span> (10th Cir.1985);
   <em>
    Recalde,
   </em>
   <span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1453" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d at 1453</a></span>. However, the question of consent or waiver was not raised in the same fashion below; while the district court found that the defendants had standing to assert their fourth amendment claims, there was no explicit finding on the question of consent. Accordingly, we review the record to answer this question. Because the facts are essentially undisputed, there is no reason to remand for factual determinations.
   <em>
    See <span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/" aria-description="Citation for case: United States v. Miguel Angel Recalde">Id.</a></span>
   </em>
   at 1453 n. 4;
   <em>
    cf. United States v. Skowronski,
   </em>
   <span class="citation" data-id="493687"><a href="/opinion/493687/united-states-v-william-michael-skowronski/" aria-description="Citation for case: United States v. William Michael Skowronski">827 F.2d 1414</a></span>, 1417 n. 2 (10th Cir.1987);
   <em>
    United States v. Hansen,
   </em>
   <span class="citation" data-id="392049"><a href="/opinion/392049/united-states-v-gary-e-hansen-daniel-e-means-aka-daniel-e-johnson/#1383" aria-description="Citation for case: United States v. Gary E. Hansen, Daniel E. Means, AKA...">652 F.2d 1374, 1383</a></span> (10th Cir.1981).
  </p>
</div><div class="footnote" id="fn11" label="11">
<a class="footnote" href="#fn11_ref">
   11
  </a>
<p id="b695-12">
   . Furthermore, the government asks that we adopt this reasoning in a case where the government
   <em>
    did not rely
   </em>
   on the policy of voluntary cooperation but entered the premises with a search warrant.
   <em>
    See Bumper v. North Carolina,
   </em>
<span citation-index="1" class="star-pagination" label="600"> 
    *600
    </span>
   <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">391 U.S. 543</a></span>, <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">88 S.Ct. 1788</a></span>, <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">20 L.Ed.2d 797</a></span> (1968).
  </p>
</div><div class="footnote" id="fn12" label="12">
<a class="footnote" href="#fn12_ref">
   12
  </a>
<p id="b696-9">
   . Thus, the direction in
   <em>
    <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">Stanford</a></span>
   </em>
   that "nothing is left to the discretion of the officer” has been interpreted in a variety of "practical" ways.
   <em>
    See, e.g., United States v. Strand,
   </em>
   <span class="citation" data-id="9473426"><a href="/opinion/451751/united-states-v-anna-m-strand-aka-anna-rogers/#453" aria-description="Citation for case: United States v. Anna M. Strand, A/K/A Anna Rogers">761 F.2d 449, 453</a></span> (8th Cir.1985) ("The constitutional standard for particularity of description in a search warrant is that the language be sufficiently definite to enable the searcher reasonably to ascertain and identify the things authorized to be seized.");
   <em>
    see also
   </em>
   2 LaFave, § 4.6(a); 3 C. Wright,
   <em>
    Federal Practice and Procedure
   </em>
   § 670, at 720-22 (2d ed. 1982). The common theme of all descriptions of the particularity standard is that the warrant must allow the executing officer to distinguish between items that may and may not be seized.
  </p>
</div><div class="footnote" id="fn13" label="13">
<a class="footnote" href="#fn13_ref">
   13
  </a>
<p id="b697-6">
   .The government cites a number of cases where warrants for business records have been held sufficiently particular to meet the requirements of the fourth amendment. We have reviewed these cases and find that they do not support the government’s claim, as the warrants in question were more particular than the one we review here, or the warrants were as particular as the information available would allow.
   <em>
    See, e.g., Andresen v. Maryland,
   </em>
   <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#481" aria-description="Citation for case: Andresen v. Maryland">427 U.S. 463, 481-82</a></span>, <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#2749" aria-description="Citation for case: Andresen v. Maryland">96 S.Ct. 2737, 2749</a></span>, <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">49 L.Ed.2d 627</a></span> (1976) (documents limited to a specific transaction);
   <em>
    United States v. Lamport,
   </em>
   <span class="citation" data-id="467613"><a href="/opinion/467613/united-states-v-frederick-e-lamport-jr/#476" aria-description="Citation for case: United States v. Frederick E. Lamport, Jr.">787 F.2d 474, 476</a></span> (10th Cir.) (more specific warrant),
   <em>
    cert. denied,
   </em>
   — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./107/166/">107 S.Ct. 166</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/93/104/">93 L.Ed.2d 104</a></span> (1986);
   <em>
    Marvin v. United States,
   </em>
   <span class="citation" data-id="434740"><a href="/opinion/434740/dr-jack-l-marvin-patricia-marvin-v-united-states/#673" aria-description="Citation for case: Dr. Jack L. Marvin, Patricia Marvin v. United States">732 F.2d 669, 673-74</a></span> (8th Cir.1984) (records to be seized limited by type and date);
   <em>
    United States v. Wuagneux,
   </em>
   <span class="citation" data-id="406519"><a href="/opinion/406519/united-states-v-george-wuagneux/" aria-description="Citation for case: United States v. George Wuagneux">683 F.2d 1343</a></span>, 1350 n. 5 (11th Cir.1982) (more specific warrant),
   <em>
    cert. denied,
   </em>
   <span class="citation multiple-matches"><a href="/c/U.S./464/814/">464 U.S. 814</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./104/69/">104 S.Ct. 69</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/78/83/">78 L.Ed.2d 83</a></span> (1983);
   <em>
    United States
   </em>
   v.
   <em>
    Timpani,
   </em>
   <span class="citation" data-id="397225"><a href="/opinion/397225/united-states-v-joseph-a-timpani/#4" aria-description="Citation for case: United States v. Joseph A. Timpani">665 F.2d 1, 4-5</a></span> (1st Cir.1981) ("it is difficult to see how the search warrant could have been made significantly more precise");
   <em>
    United States v. Dennis,
   </em>
   <span class="citation" data-id="380192"><a href="/opinion/380192/united-states-v-willie-h-dennis/#792" aria-description="Citation for case: United States v. Willie H. Dennis">625 F.2d 782, 792</a></span> (8th Cir.1980) (warrant as specific as circumstances would allow). None of the decisions cited by the government allow a general description where the information was readily available to significantly narrow the search. The government argues that
   <em>
    <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">Andresen</a></span>
   </em>
   authorizes the seizure of general business records, but the warrant in
   <em>
    <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">Andresen</a></span>
   </em>
   was limited to a specific transaction.
   <em>
    See
   </em>
   In re
   <em>
    Grand Jury Proceedings (Young),
   </em>
   <span class="citation" data-id="9471119"><a href="/opinion/424091/in-re-grand-jury-proceedings-appeal-of-robert-e-young/" aria-description="Citation for case: In Re Grand Jury Proceedings. Appeal of Robert E. Young">716 F.2d 493</a></span>, 498 n. 7 (8th Cir.1983);
   <em>
    United States v. Roche,
   </em>
   <span class="citation" data-id="373913"><a href="/opinion/373913/united-states-v-john-c-roche/" aria-description="Citation for case: United States v. John C. Roche">614 F.2d 6</a></span>, 7 n. 2 (1st Cir.1980). If the Kleinberg warrant had been explicitly limited to documents related to the Micro-tel transaction it would be comparable to the warrant in
   <em>
    <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">Andresen</a></span>.
   </em>
</p>
</div><div class="footnote" id="fn14" label="14">
<a class="footnote" href="#fn14_ref">
   14
  </a>
<p id="b697-13">
   .
   <em>
    <span class="citation" data-id="8935318"><a href="/opinion/8944758/voss-v-bergsgaard/" aria-description="Citation for case: Voss v. Bergsgaard">Voss</a></span>
   </em>
   differs from the current case in two respects. First, the search in
   <em>
    <span class="citation" data-id="8935318"><a href="/opinion/8944758/voss-v-bergsgaard/" aria-description="Citation for case: Voss v. Bergsgaard">Voss</a></span>
   </em>
   implicated first amendment concerns that are not present here. Second, the conspiracy statute is arguably broader than the export statutes cited in the Kleinberg warrant. However, neither distinction is reason to depart from our holding. The first amendment concerns were not central to the decision but merely made the "warrants’ overbreadth ... even more egregious."
   <em>
    Voss,
   </em>
   <span class="citation" data-id="8935318"><a href="/opinion/8944758/voss-v-bergsgaard/#405" aria-description="Citation for case: Voss v. Bergsgaard">774 F.2d at 405</a></span>. Similarly, the differences in the statutes cited are not significant.
  </p>
</div><div class="footnote" id="fn15" label="15">
<a class="footnote" href="#fn15_ref">
   15
  </a>
<p id="b697-14">
   . We emphasize that it is not the mere reference to the statute that makes the Kleinberg warrant overbroad, it is the
   <em>
    absence of any limiting features.
   </em>
   In other words, the warrant is limited neither by the list of records to be seized, nor by the reference to the export statutes. If the warrant were narrower in either respect, or if it included some other limitation, we might find it valid. For example, this court found the warrant in
   <em>
    United States v. Lamport,
   </em>
   <span class="citation" data-id="467613"><a href="/opinion/467613/united-states-v-frederick-e-lamport-jr/#476" aria-description="Citation for case: United States v. Frederick E. Lamport, Jr.">787 F.2d 474, 476</a></span> (10th Cir.),
   <em>
    cert. denied,
   </em>
   — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./107/166/">107 S.Ct. 166</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/93/104/">93 L.Ed.2d 104</a></span> (1986), sufficiently specific where the statutory reference (to the mail fraud statute) was limited by a list of specific items (medical records limited by patients and dates).
  </p>
</div><div class="footnote" id="fn16" label="16">
<a class="footnote" href="#fn16_ref">
   16
  </a>
<p id="b698-6">
   . The government argues that the "agents based their decisions on the guidelines set forth in the warrant which they testified was sufficiently descriptive.” Brief of Appellant at 39. But the government’s citations to the record of the suppression hearing do not support that assertion. The record clearly indicates that the agents relied on Agent Juhasz' instructions.
   <em>
    See, e.g.,
   </em>
   R. Vol. Ill at 31-32, 45-47. The only acknowledged guidance from the face of the warrant by the agents is that they "were looking for records reflecting possible violations of the Export Administration Act, ...”
   <em>
    Id.
   </em>
   at 30.
  </p>
</div><div class="footnote" id="fn17" label="17">
<a class="footnote" href="#fn17_ref">
   17
  </a>
<p id="b698-7">
   . In
   <em>
    United States v. Sawyer, 799
   </em>
   F.2d 1494 (11th Cir.1986) the Elev

[...TRUNCATED 29024 of 149024 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/United States v. Lee.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Lee
type: case
citation: "274 U.S. 559 (1927)"
parallel_cite: "47 S. Ct. 746; 71 L. Ed. 1202"
neutral_cite: 1927 U.S. LEXIS 52
court: U.S.
court_level: scotus
circuit: ca6
year: 1927
date_decided: 1927-05-31
docket: 540
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
  opinion_url: "https://www.courtlistener.com/opinion/101118/united-states-v-lee/"
  cluster_id: 101118
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Lee
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Fourth Amendment Recalibration]]"
    role: Key
related:
  - "[[Fourth Amendment Recalibration]]"
  - "[[Kyllo v. United States]]"
  - "[[Hester v. United States]]"
  - "[[Carroll v. United States]]"
tags:
  - case
  - fourth-amendment
  - search
  - sense-enhancement
  - open-view
  - prohibition
  - coast-guard
  - scotus
holding: "The Supreme Court held that a Coast Guard officer's use of a searchlight to illuminate the deck of a suspected rum-runner on the high seas was not a Fourth Amendment search — it merely revealed what was already in open view, comparable to using a marine glass or field glass — and, more broadly, that the Coast Guard could board, search, and seize an American vessel and arrest those aboard on the high seas beyond the twelve-mile limit on probable cause of a revenue-law violation; the Court of Appeals' contrary judgment was reversed."
---

# United States v. Lee

*274 U.S. 559 (1927)* (No. 540) · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 101118 → opinion 101118 (274 U.S. 559, decided 1927-05-31); Rule quote star-matched to the U.S. Reports pagination in the CL opinion text 2026-07-07. S9 promotes. -->

## Background
In February 1925, during Prohibition, the boatswain of a Coast Guard patrol boat followed a motor boat registered to Lee out of Gloucester harbor and, after losing her in a fog, found her about twenty-four miles from land in a region commonly spoken of as Rum Row, lying alongside the schooner *L'Homme* with seventy-one cases of grain alcohol aboard. The boatswain "put a searchlight on her," ordered the three men to raise their hands, boarded, found the alcohol, arrested Lee and his associates, and took the boat and liquor to Boston. Lee was convicted of conspiring to violate the Tariff Act of 1922 and the National Prohibition Act. The Court of Appeals [[Reading and Citing Cases#vacated|vacated]] the conviction, holding that the Coast Guard could not search American vessels on the high seas more than twelve miles out and that the evidence was the fruit of an illegal search under *[[Weeks v. United States|Weeks]]*.

## Issue
Whether the Coast Guard's boarding, search, and seizure of an American vessel on the high seas beyond the twelve-mile limit — and in particular the boatswain's use of a searchlight to observe the vessel's deck — violated the Fourth Amendment, so that the resulting evidence had to be excluded.

## Rule
The Coast Guard may seize an American vessel on the high seas beyond the twelve-mile limit, and board and search it and arrest those aboard, when there is probable cause to believe the revenue laws are being violated — authority the Court analogized to the warrantless automobile search upheld in *[[Carroll v. United States|Carroll]]*. And illuminating what is already exposed to view is not a search: because no exploration below decks or under hatches was shown and the liquor was on deck, discovered before boarding, the boatswain's use of a searchlight worked no Fourth Amendment intrusion — "Such use of a searchlight is comparable to the use of a marine glass or a field glass. It is not prohibited by the Constitution." — 274 U.S. at 563. ^pin-563

## Application
There was probable cause to believe Lee's vessel was violating the revenue laws — a registered motor boat meeting a schooner on Rum Row with seventy-one cases of alcohol aboard — so the search and seizure of the vessel and the arrest of those aboard were lawful, and the deputy surveyor's later examination of the cases in Boston was independently authorized. As to the searchlight, the Court treated it as mere observation of what was in open view: it revealed only the deck and what lay upon it, no different in kind from using a field glass, and so fell outside the Fourth Amendment. A later trespass, if any, did not render inadmissible knowledge already lawfully obtained.

## Conclusion
**Reversed** — the Court of Appeals' judgment vacating the conviction was set aside, the evidence having been lawfully obtained. Justice Brandeis delivered the opinion of the Court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Lee*'s enduring contribution to the Fourth Amendment's recalibration arc is the **sense-enhancement seed**: illuminating what is already exposed with a searchlight — like a field or marine glass — is not a search. That open-view/enhanced-observation line runs forward to *[[Kyllo v. United States|Kyllo]]*, which draws the boundary at technology "not in general public use" used to reveal the interior of a home. Read *Lee* on the "expands government power" side of the timeline, a Prohibition-era decision fitting the Amendment to new maritime enforcement.

## Appears on
- [[Fourth Amendment Recalibration]] — *Key*

## Sources
- [*United States v. Lee*, 274 U.S. 559 (1927)](https://www.courtlistener.com/opinion/101118/united-states-v-lee/) — pinpoint: 563 (searchlight-is-not-a-search holding; the CL opinion text carries U.S. Reports star pagination, so the pin is reporter-style). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6f036bb79ee4560b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Lee"}, "payload": {"all": [{"cite": "274 U.S. 559", "page": "559", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "274"}, {"cite": "47 S. Ct. 746", "page": "746", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "47"}, {"cite": "71 L. Ed. 1202", "page": "1202", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "71"}, {"cite": "1927 U.S. LEXIS 52", "page": "52", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1927"}], "display": "274 U.S. 559", "official": {"cite": "274 U.S. 559", "page": "559", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "274"}, "official_selection_present": true, "record_id": "United States v. Lee"}}
{"assertion_id": "a17e1ba14c727542", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Lee"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Lee", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Lee

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Lee",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Lee",
    "case_name_short": "",
    "case_name_full": "United States v. Lee",
    "input_case_name": "United States v. Lee",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": "ca6",
    "state": null,
    "date_decided": "1927-05-31",
    "year": 1927,
    "docket": "540",
    "cluster_id": 101118,
    "lead_opinion_id": 101118,
    "sibling_ids": [],
    "absolute_url": "/opinion/101118/united-states-v-lee/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "274 U.S. 559",
      "volume": "274",
      "reporter": "U.S.",
      "page": "559",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "47 S. Ct. 746",
        "volume": "47",
        "reporter": "S. Ct.",
        "page": "746",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "71 L. Ed. 1202",
        "volume": "71",
        "reporter": "L. Ed.",
        "page": "1202",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1927 U.S. LEXIS 52",
        "volume": "1927",
        "reporter": "U.S. LEXIS",
        "page": "52",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "274 U.S. 559",
        "volume": "274",
        "reporter": "U.S.",
        "page": "559",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "47 S. Ct. 746",
        "volume": "47",
        "reporter": "S. Ct.",
        "page": "746",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "71 L. Ed. 1202",
        "volume": "71",
        "reporter": "L. Ed.",
        "page": "1202",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1927 U.S. LEXIS 52",
        "volume": "1927",
        "reporter": "U.S. LEXIS",
        "page": "52",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "274 U.S. 559",
    "official_selection": {
      "court_class": "scotus",
      "selected": "274 U.S. 559",
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
    "date_created": "2026-07-07T18:18:50Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:18:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:18:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:18:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:18:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-lee--101118",
      "to_record_id": "United States v. Lee",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Lee

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b618-5">
  Mr. Justice Brandéis
 </author>
<p id="A7V">
  delivered the opinion of the Court.
 </p>
<p id="AqW">
  In the federal court for Massachusetts, Lee and two others, all apparently American citizens, were indicted for conspiring within the United States to violate §§ 591 and 593 of the Tariff Act of 1922, c. 356, <span class="citation no-link">42 Stat. 858</span>, 981, 982, and § 3 of the National Prohibition Act, October 28, 1919, c. 85, Title II, <span class="citation no-link">41 Stat. 305</span>, 308. The defendants pleaded not guilty. Lee and one other were convicted. Lee sued out a writ of error. The Court of Appeals (one judge dissenting) vacated the judgment on the ground that evidence had been admitted which was obtained by an illegal search. and seizure. 14 F. (2d) 400. This Court granted a writ of certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./273/686/">273 U. S. 686</a></span>.
 </p>
<p id="b618-7">
  On the afternoon of February 16, 1925, the. boatswain of a Coast Guard patrol boat saw a motor boat of the numbered type proceed in a southeasterly direction from Gloucester harbor. He followed her at a distance of 500 yards, lost sight of her after sundown, apparently in a fog, at a point about 20 miles east of Boston Light, and discovered her later alongside the schooner
  <em>
   L’Homme
  </em>
  in a region commonly spoken of as Rum Row, at a point 24 miles from land. On board the motor boat were Lee, two associates, and 71 cases of grain alcohol. The boatswain arrested thé three men, seized the motor boat, and took her with them and the liquor to Boston. There this indictment was found. It does not appear that the Government instituted proceedihgs to forfeit; either the motor boat or the. liquor. The motor boat, which had a length of about 30 feet-,- was registered in Lee’s name.
 </p>
<p id="b618-8">
  The boatswain testified that when he discovered the motor boat alongside the
  <em>
   L’Homme:
  </em>
</p>
<blockquote id="A7v-">
<span citation-index="1" class="star-pagination" label="561"> 
   *561
   </span>
  “ I put a searchlight on her and told those aboard the motor boat to put. up their hands. In the boat I found the three defendants, McNeil, Yieria, and Lee. I hooked the boat over and found a number of cansí of alcohol on board it. I searched the defendants for weapons and found none. I put two of my men on board the motor boat and took the boat and the defendants to Boston.”
 </blockquote>
<p id="Aei">
  The liquor does not appear to have been put in evidence. The deputy surveyor of the port testified that, upon the motor boat’s arrival in Boston, he examined the cases on board and found that they contained alcohol, 95 degrees proof.; and that Lee, when interrogated, said: “ I ran the engine, and the first thing I knew I was alongside a schooner. I did not see any cases on our boat until captured by the revenue cutter.” The testimony of the deputy surveyor as to what he found on the, motor boat, and that of the boatswain as to what he found upon his examination of the motor boat at the time of his command to those on board to throw up their hands, was admitted over Lee’s objection and subject to exception duly made.
 </p>
<p id="b619-6">
  . The Court of Appeals, expressing disagreement with the conclusion reached in
  <em>
   The Underwriter,
  </em>
  13 F. (2d) 433, held that the Coast Guard is not authorized to visit and search American vessels on the high seas more than twelve miles from the coast; that the seizure there made was without authority; that it was illegal, since it did not appear that the Government had ratified it by the institution of legal proceedings to enforce ^e forfeiture; that the search and seizure having been illegal, knowledge gained as a result of the illegal search could not be put ^ evidence,
  <em>
   Weeks
  </em>
  v.
  <em>
   United States,
  </em>
  232 U. S.. 383; and that the testimony of the deputy surveyor and of the boatswain was wrongly admitted.
 </p>
<p id="b620-4">
<span citation-index="1" class="star-pagination" label="562"> 
   *562
   </span>
  The Government contends that the Coast Guard has authority to visit, search and seize an American vessel on the high seas beyond the twelve-mile limit when probable cause exists to believe that our law is being violated; that it has authority also to arrest persons on such vessel who there is reason to believe are engaged in committing a felony; that here probable cause was shown that the crime, a felony, was being committed; that if any search, within the meaning of the Constitution, was made of the motor boat before she reached port, it was valid as an incident of a lawful arrest of persons who the officer had reasonable cause to believe were engaged in committing a felony; that the constitutional prohibition against search and seizure without a warrant is not applicable to this small motor boat which does not appear to have been used as a place of residence; and that it does not appear that any search was, in fact, made before the motor boat was examined in Boston by the deputy surveyor, within the territorial limits of the - United States, where search is clearly valid.
 </p>
<p id="b620-5">
  In the main the contentions of the Government are in our opinion well founded. Officers of the Coast Guard .are authorized, by virtue of Revised Statutes, § 3072, to seize on the high seas beyond the twelve-mile limit an American vessel subject to forfeiture for violation of any law respecting the revenue.
  <em>
   Maul
  </em>
  v.
  <em>
   United States [The
  </em>
  Underwriter],
  <em>
   ante,
  </em>
  p. 501. From that power it is fairly to be inferred that, they are likewise authorized to board and search such vessels when there is probable cause to believe them subject to seizure for violation of revenue laws, and to arrest persons thereon engaged in such violation. Compare
  <em>
   Ford
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="101041"><a href="/opinion/101041/ford-v-united-states/#609" aria-description="Citation for case: Ford v. United States">273 U. S. 593, 609-616</a></span>. The authority asserted is not as broad as the belligerent right to visit and search even without probable
  <span citation-index="1" class="star-pagination" label="563"> 
   *563
   </span>
  cause. Compare.
  <em>
   The Marianna Flora,
  </em>
  <span class="citation" data-id="85480"><a href="/opinion/85480/the-marianna-flora/#42" aria-description="Citation for case: The Marianna Flora">11 Wheat. 1, 42</a></span>. In the case at bar, there was probable cause to believe that our revenue laws were being violated by an American vessel and the persons thereon, in such manner as to render the vessel subject to forfeiture. Under such circumstances, search and seizure of the vessel, and arrest of the persons thereon, by the Coast Guard on the high seas is lawful, as like search and seizure, of an automobile, and arrest of the persons therein, by - prohibition officers on land is lawful. Compare
  <em>
   Carroll
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 149</a></span>. As the Coast Guard was authorized to seize the motor boat, the search of her by the deputy surveyor within the territory of the United States was, in any event, authorized under § 581 of the Tariff Act of 1922. The failure of the Government to institute thereafter proceedings for forfeiture of the motor boat and the liquor did not, by retroaction, render illegal either the seizure or the search.
 </p>
<p id="b621-6">
  Moreover search, if any, of the motor boat at sea did not violate the Constitution, for it was made by the boatswain as an incident of a lawful arrest.
  <em>
   Agnello
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span>. But no search on the high seas is shown. The testimony of the boatswain shows that he used a searchlight. It is not shown that there was any exploration below decks or under hatches. For aught that appears, the cases of liquor were on deck and, like the defendants, were discovered before the motor boat was boarded. Such use of a searchlight is comparable to the use of a marine glass or a field glass. It is not prohibited by the Constitution. Compare
  <em>
   Hester
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span>. A later trespass by the officers, if any, did not render inadmissible in evidence knowledge legally, obtained.
  <em>
   McGuire
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100989"><a href="/opinion/100989/mcguire-v-united-states/" aria-description="Citation for case: McGuire v. United States">273 U. S. 95</a></span>.
 </p>
<p id="b621-7">
<em>
   Reversed.
  </em>
</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Leon.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Leon"
type: case
citation: "468 U.S. 897 (1984)"
parallel_cite: "104 S. Ct. 3405; 82 L. Ed. 2d 677"
neutral_cite: 1984 U.S. LEXIS 153
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-09-18
docket: 82-1771
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-07-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Leon
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111262/united-states-v-leon/"
  cluster_id: 111262
  opinion_id: 9429766
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Anchor"
  - page: "[[Franks Challenges]]"
    role: "Related (cross-doctrine)"
related: ["[[Massachusetts v. Sheppard]]", "[[Herring v. United States]]", "[[Davis v. United States (2011)|Davis v. United States]]", "[[Franks v. Delaware]]", "[[Illinois v. Gates]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "good-faith-exception", "search-warrant", "deterrence"]
holding: "Good-faith exception: evidence obtained by officers in objectively reasonable reliance on a search warrant later found unsupported by…"
lake:
  record_id: United States v. Leon
  status: verified
  projected_at: 2026-07-09
---

# United States v. Leon

*468 U.S. 897 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Acting on a confidential informant's tip of unproven reliability, Burbank police conducted surveillance and investigation, then obtained a facially valid search warrant from a state judge; the searches produced large quantities of drugs. The District Court held the affidavit insufficient to establish probable cause but recognized that the officers had acted in good faith, and granted suppression; the Ninth Circuit affirmed.

## Issue
Whether the Fourth Amendment exclusionary rule should be modified so as not to bar the prosecution's use, in its case-in-chief, of evidence obtained by officers acting in objectively reasonable reliance on a search warrant issued by a detached and neutral magistrate but ultimately found to be unsupported by probable cause.

## Rule
The exclusionary rule does not bar such evidence. Because the rule's purpose is to deter police misconduct, and suppressing evidence obtained on a warrant deters the magistrate's error rather than the officer's, the Court held: "We conclude that the marginal or nonexistent benefits produced by suppressing evidence obtained in objectively reasonable reliance on a subsequently invalidated search warrant cannot justify the substantial costs of exclusion." — 468 U.S. at 922. ^pin-922

Good faith is measured objectively, and the exception does **not** apply in four situations: (1) where "the magistrate or judge in issuing a warrant was misled by information in an affidavit that the affiant knew was false or would have known was false except for his reckless disregard of the truth" ([[Franks v. Delaware]]); (2) where "the issuing magistrate wholly abandoned his judicial role"; (3) where the affidavit is "so lacking in indicia of probable cause as to render official belief in its existence entirely unreasonable"; and (4) where a warrant is so facially deficient — in failing to particularize the place or things — "that the executing officers cannot reasonably presume it to be valid." — [*Id.* at 923](https://www.courtlistener.com/opinion/111262/united-states-v-leon/#:~:text=the%20magistrate%20or%20judge%20in). ^pin-923

## Application
On these facts the evidence was admissible. The officers obtained a warrant from a neutral magistrate and executed it within its terms; whatever the affidavit's shortcomings on probable cause, their reliance on the judge's determination was objectively reasonable. None of the four disqualifying circumstances was present — there was no *[[Franks v. Delaware|Franks]]* falsehood, the magistrate did not abandon his judicial role, the affidavit was not so bare as to make belief in probable cause entirely unreasonable, and the warrant was not facially deficient. Excluding the evidence would punish the officers for the magistrate's error and yield no appreciable deterrent benefit, so suppression was unwarranted.

## Conclusion
Evidence seized in objectively reasonable reliance on a later-invalidated warrant need not be suppressed; the Ninth Circuit's judgment affirming suppression was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Leon* establishes the [[The Good-Faith Exception|good-faith exception]], extended the same day to a [[Particularity|particularity]] defect in [[Massachusetts v. Sheppard]], to a statute later held unconstitutional in [[Illinois v. Krull]], and to police recordkeeping errors in [[Herring v. United States]] and binding-precedent reliance in [[Davis v. United States (2011)|Davis v. United States]]; its limits track the four enumerated exceptions.

## Appears on
- [[The Exclusionary Rule]] — *Key — Anchor*
- [[Franks Challenges]] — *Related (cross-doctrine)*

## Sources
- *United States v. Leon*, 468 U.S. 897 (1984) — https://www.courtlistener.com/opinion/111262/united-states-v-leon/ — pinpoints: 922, 923.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e34b5c48810c6979", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Leon"}, "payload": {"all": [{"cite": "468 U.S. 897", "page": "897", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "468"}, {"cite": "104 S. Ct. 3405", "page": "3405", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "104"}, {"cite": "82 L. Ed. 2d 677", "page": "677", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "82"}, {"cite": "1984 U.S. LEXIS 153", "page": "153", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1984"}], "display": "468 U.S. 897", "official": {"cite": "468 U.S. 897", "page": "897", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "468"}, "official_selection_present": true, "record_id": "United States v. Leon"}}
{"assertion_id": "341f1de8eddb4e49", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-923", "record_id": "United States v. Leon"}, "payload": {"fragment": "#:~:text=the%20magistrate%20or%20judge%20in", "page": null, "pin_id": "pin-923", "pinpoint_status": "star-verified", "quote": "the magistrate or judge in issuing a warrant was misled by information in an affidavit that the affiant knew was false or would have known was false except for his reckless disregard of the truth", "quote_fidelity": "matched", "record_id": "United States v. Leon", "star_marker": "923"}}
{"assertion_id": "fdcdd54e0045d295", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-922", "record_id": "United States v. Leon"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-922", "pinpoint_status": "slip-only", "quote": "--- # United States v. Leon *468 U.S. 897 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting on a confidential informant's tip of unproven reliability, Burbank police conducted surveillance and investigation, then obtained a facially valid search warrant from a state judge; the searches produced large quantities of drugs. The District Court held the affidavit insufficient to establish probable cause but recognized that the officers had acted in good faith, and granted suppression; the Ninth Circuit affirmed. ## Issue Whether the Fourth Amendment exclusionary rule should be modified so as not to bar the prosecution's use, in its case-in-chief, of evidence obtained by officers acting in objectively reasonable reliance on a search warrant issued by a detached and neutral magistrate but ultimately found to be unsupported by probable cause. ## Rule The exclusionary rule does not bar such evidence. Because the rule's purpose is to deter police misconduct, and suppressing evidence obtained on a warrant deters the magistrate's error rather than the officer's, the Court held:", "quote_fidelity": "mismatch", "record_id": "United States v. Leon", "star_marker": null}}
{"assertion_id": "b874911dc347777f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Leon"}, "payload": {"as_of_content": "1984-07-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Leon", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Leon

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Leon",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Leon",
    "case_name_short": "Leon",
    "case_name_full": "UNITED STATES v. LEON Et Al.",
    "input_case_name": "United States v. Leon",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-09-18",
    "year": 1984,
    "docket": "82-1771",
    "cluster_id": 111262,
    "lead_opinion_id": 9429766,
    "sibling_ids": [
      111262,
      9429766,
      9429767,
      9429768,
      9429769
    ],
    "absolute_url": "/opinion/111262/united-states-v-leon/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "468 U.S. 897",
      "volume": "468",
      "reporter": "U.S.",
      "page": "897",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 3405",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3405",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 677",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "677",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 153",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "153",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "468 U.S. 897",
        "volume": "468",
        "reporter": "U.S.",
        "page": "897",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 3405",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3405",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 677",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "677",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 153",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "153",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "468 U.S. 897",
    "official_selection": {
      "court_class": "scotus",
      "selected": "468 U.S. 897",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-922",
      "page": null,
      "quote": "--- # United States v. Leon *468 U.S. 897 (1984)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting on a confidential informant's tip of unproven reliability, Burbank police conducted surveillance and investigation, then obtained a facially valid search warrant from a state judge; the searches produced large quantities of drugs. The District Court held the affidavit insufficient to establish probable cause but recognized that the officers had acted in good faith, and granted suppression; the Ninth Circuit affirmed. ## Issue Whether the Fourth Amendment exclusionary rule should be modified so as not to bar the prosecution's use, in its case-in-chief, of evidence obtained by officers acting in objectively reasonable reliance on a search warrant issued by a detached and neutral magistrate but ultimately found to be unsupported by probable cause. ## Rule The exclusionary rule does not bar such evidence. Because the rule's purpose is to deter police misconduct, and suppressing evidence obtained on a warrant deters the magistrate's error rather than the officer's, the Court held:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-923",
      "page": null,
      "quote": "the magistrate or judge in issuing a warrant was misled by information in an affidavit that the affiant knew was false or would have known was false except for his reckless disregard of the truth",
      "star_marker": "923",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 48236,
      "fragment": "#:~:text=the%20magistrate%20or%20judge%20in",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-07-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Leon",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 10705828,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Raenard Romalle Douglas",
          "cluster_id": 10129058,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Batson v. Kentucky",
          "cluster_id": 111662,
          "cite": [
            "90 L. Ed. 2d 69",
            "106 S. Ct. 1712",
            "476 U.S. 79",
            "1986 U.S. LEXIS 150",
            "54 U.S.L.W. 4425"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pearson v. Callahan",
          "cluster_id": 145918,
          "cite": [
            "172 L. Ed. 2d 565",
            "129 S. Ct. 808",
            "555 U.S. 223",
            "2009 U.S. LEXIS 591"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
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
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray v. Carrier",
          "cluster_id": 111727,
          "cite": [
            "91 L. Ed. 2d 397",
            "106 S. Ct. 2639",
            "477 U.S. 478",
            "1986 U.S. LEXIS 66",
            "54 U.S.L.W. 4820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ornelas v. United States",
          "cluster_id": 118030,
          "cite": [
            "134 L. Ed. 2d 911",
            "116 S. Ct. 1657",
            "517 U.S. 690",
            "1996 U.S. LEXIS 3391"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
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
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyles v. Whitley",
          "cluster_id": 117923,
          "cite": [
            "131 L. Ed. 2d 490",
            "115 S. Ct. 1555",
            "514 U.S. 419",
            "1995 U.S. LEXIS 2845"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
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
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. Witt",
          "cluster_id": 111303,
          "cite": [
            "83 L. Ed. 2d 841",
            "105 S. Ct. 844",
            "469 U.S. 412",
            "1985 U.S. LEXIS 43",
            "53 U.S.L.W. 4108"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kimmelman v. Morrison",
          "cluster_id": 111724,
          "cite": [
            "91 L. Ed. 2d 305",
            "106 S. Ct. 2574",
            "477 U.S. 365",
            "1986 U.S. LEXIS 63",
            "54 U.S.L.W. 4789"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sharpe",
          "cluster_id": 111378,
          "cite": [
            "84 L. Ed. 2d 605",
            "105 S. Ct. 1568",
            "470 U.S. 675",
            "1985 U.S. LEXIS 74",
            "53 U.S.L.W. 4346"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Elstad",
          "cluster_id": 111364,
          "cite": [
            "84 L. Ed. 2d 222",
            "105 S. Ct. 1285",
            "470 U.S. 298",
            "1985 U.S. LEXIS 60",
            "53 U.S.L.W. 4244"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 117863,
          "cite": [
            "129 L. Ed. 2d 362",
            "114 S. Ct. 2350",
            "512 U.S. 452",
            "1994 U.S. LEXIS 4827"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
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
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jett v. Dallas Independent School District",
          "cluster_id": 112313,
          "cite": [
            "105 L. Ed. 2d 598",
            "109 S. Ct. 2702",
            "491 U.S. 701",
            "1989 U.S. LEXIS 3130",
            "57 U.S.L.W. 4858",
            "50 Fair Empl. Prac. Cas. (BNA) 27",
            "50 Empl. Prac. Dec. (CCH) 39,070"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McDonald v. City of Chicago",
          "cluster_id": 149702,
          "cite": [
            "177 L. Ed. 2d 894",
            "130 S. Ct. 3020",
            "561 U.S. 742",
            "2010 U.S. LEXIS 5523",
            "22 Fla. L. Weekly Fed. S 619",
            "78 U.S.L.W. 4844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davidson v. Cannon",
          "cluster_id": 111556,
          "cite": [
            "88 L. Ed. 2d 677",
            "106 S. Ct. 668",
            "474 U.S. 344",
            "1986 U.S. LEXIS 44",
            "54 U.S.L.W. 4095"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vasquez v. Hillery",
          "cluster_id": 111552,
          "cite": [
            "88 L. Ed. 2d 598",
            "106 S. Ct. 617",
            "474 U.S. 254",
            "1986 U.S. LEXIS 40",
            "54 U.S.L.W. 4068"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wright v. West",
          "cluster_id": 112771,
          "cite": [
            "120 L. Ed. 2d 225",
            "112 S. Ct. 2482",
            "505 U.S. 277",
            "1992 U.S. LEXIS 3689"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herring v. United States",
          "cluster_id": 145922,
          "cite": [
            "172 L. Ed. 2d 496",
            "129 S. Ct. 695",
            "555 U.S. 135",
            "2009 U.S. LEXIS 581"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. Seibert",
          "cluster_id": 137002,
          "cite": [
            "159 L. Ed. 2d 643",
            "124 S. Ct. 2601",
            "542 U.S. 600",
            "2004 U.S. LEXIS 4578"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 218926,
          "cite": [
            "180 L. Ed. 2d 285",
            "131 S. Ct. 2419",
            "564 U.S. 229",
            "2011 U.S. LEXIS 4560"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brower Ex Rel. Estate of Caldwell v. County of Inyo",
          "cluster_id": 112218,
          "cite": [
            "103 L. Ed. 2d 628",
            "109 S. Ct. 1378",
            "489 U.S. 593",
            "1989 U.S. LEXIS 1569",
            "57 U.S.L.W. 4321"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mickens v. Taylor",
          "cluster_id": 118492,
          "cite": [
            "152 L. Ed. 2d 291",
            "122 S. Ct. 1237",
            "535 U.S. 162",
            "2002 U.S. LEXIS 2146"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray v. United States",
          "cluster_id": 112136,
          "cite": [
            "101 L. Ed. 2d 472",
            "108 S. Ct. 2529",
            "487 U.S. 533",
            "1988 U.S. LEXIS 2881",
            "56 U.S.L.W. 4801"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111262 OR 9429766 OR 9429767 OR 9429768 OR 9429769) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjgwMjIwODAwMDAwJnM9OTM4ODM0MSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111262+OR+9429766+OR+9429767+OR+9429768+OR+9429769%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 2,
        "triage_snippet_classified": 198
      },
      "lane2_top_cited": {
        "query": "cites:(111262 OR 9429766 OR 9429767 OR 9429768 OR 9429769)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03NzYmcz0yMzE2Njk4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111262+OR+9429766+OR+9429767+OR+9429768+OR+9429769%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111262 OR 9429766 OR 9429767 OR 9429768 OR 9429769)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzAzNzIxNjAwMDAwJnM9OTQ1NTgxNiZ0PW8mZD0yMDI2LTA3LTA2JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111262+OR+9429766+OR+9429767+OR+9429768+OR+9429769%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 2,
        "triage_snippet_classified": 198
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111262 OR 9429766 OR 9429767 OR 9429768 OR 9429769)",
    "indexed_citing_opinions": 5262,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111262,
        "count": 4543,
        "count_source": "search"
      },
      {
        "opinion_id": 9429766,
        "count": 808,
        "count_source": "search"
      },
      {
        "opinion_id": 9429767,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429768,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429769,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 9241,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-leon.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk1MTI1OCZzPTEwNjYyNTI5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111262+OR+9429766+OR+9429767+OR+9429768+OR+9429769%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111262,
        "cited_id": 85272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 100621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 100949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 105242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106287,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107577,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108379,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109303,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 111172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 294030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 296213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 333763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 339292,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 378896,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 1237532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 2058560,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 2620876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 3580565,
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
    "date_created": "2026-07-06T01:20:53Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:21:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:21:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:24:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:21:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Leon

```
<opinion type="majority">
<author id="b942-4"><page-number citation-index="1" label="900">*900</page-number>Justice White</author>
<p id="AaUZ">delivered the opinion of the Court.</p>
<p id="b942-5">This ease presents the question whether the Fourth Amendment exclusionary rule should be modified so as not to bar the use in the prosecution’s case in chief of evidence obtained by officers acting in reasonable reliance on a search warrant issued by a detached and neutral magistrate but ultimately found to be unsupported by probable cause. To resolve this question, we must consider once again the tension between the sometimes competing goals of, on the one hand, deterring official misconduct and removing inducements to unreasonable invasions of privacy and, on the other, establishing procedures under which criminal defendants are “ac<page-number citation-index="1" label="901">*901</page-number>quitted or convicted on the basis of all the evidence which exposes the truth.” <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#175" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 175</a></span> (1969).</p>
<p id="b943-5">I</p>
<p id="b943-6">In August 1981, a confidential informant of unproven reliability informed an officer of the Burbank Police Department that two persons known to him as “Armando” and “Patsy” were selling large quantities of cocaine and methaqualone from their residence at 620 Price Drive in Burbank, Cal. The informant also indicated that he had witnessed a sale of methaqualone by “Patsy” at the residence approximately five months earlier and had observed at that time a shoebox containing a large amount of cash that belonged to “Patsy.” He further declared that “Armando” and “Patsy” generally kept only small quantities of drugs at their residence and stored the remainder at another location in Burbank.</p>
<p id="b943-7">On the basis of this information, the Burbank police initiated an extensive investigation focusing first on the Price Drive residence and later on two other residences as well. Cars parked at the Price Drive residence were determined to belong to respondents Armando Sanchez, who had previously been arrested for possession of marihuana, and Patsy Stewart, who had no criminal record. During the course of the investigation, officers observed an automobile belonging to respondent Ricardo Del Castillo, who had previously been arrested for possession of 50 pounds of marihuana, arrive at the Price Drive residence. The driver of that car entered the house, exited shortly thereafter carrying a small paper sack, and drove away. A check of Del Castillo’s probation records led the officers to respondent Alberto Leon, whose telephone number Del Castillo had listed as his employer’s. Leon had been arrested in 1980 on drug charges, and a companion had informed the police at that time that Leon was heavily involved in the importation of drugs into this country. Before the current investigation began, the Burbank officers had <page-number citation-index="1" label="902">*902</page-number>learned that an informant had told a Glendale police officer that Leon stored a large quantity of methaqualone at his residence in Glendale. During the course of this investigation, the Burbank officers learned that Leon was living at 716 South Sunset Canyon in Burbank.</p>
<p id="b944-5">Subsequently, the officers observed several persons, at least one of whom had prior drug involvement, arriving at the Price Drive residence and leaving with small packages; observed a variety of other material activity at the two residences as well as at a condominium at 7902 Via Magdalena; and witnessed a variety of relevant activity involving respondents’ automobiles. The officers also observed respondents Sanchez and Stewart board separate flights for Miami. The pair later returned to Los Angeles together, consented to a search of their luggage that revealed only a small amount of marihuana, and left the airport. Based on these and other observations summarized in the affidavit, App. 34, Officer Cyril Rombach of the Burbank Police Department, an experienced and well-trained narcotics investigator, prepared an application for a warrant to search 620 Price Drive, 716 South Sunset Canyon, 7902 Via Magdalena, and automobiles registered to each of the respondents for an extensive list of items believed to be related to respondents’ drug-trafficking activities. Officer Rombach’s extensive application was reviewed by several Deputy District Attorneys.</p>
<p id="b944-6">A facially valid search warrant was issued in September 1981 by a State Superior Court Judge. The ensuing searches produced large quantities of drugs at the Via Magdalena and Sunset Canyon addresses and a small quantity at the Price Drive residence. Other evidence was discovered at each of the residences and in Stewart’s and Del Castillo’s automobiles. Respondents were indicted by a grand jury in the District Court for the Central District of California and charged with conspiracy to possess and distribute cocaine and a variety of substantive counts.</p>
<p id="b945-4"><page-number citation-index="1" label="903">*903</page-number>The respondents then filed motions to suppress the evidence seized pursuant to the warrant.<footnotemark>1</footnotemark> The District Court held an evidentiary hearing and, while recognizing that the case was a close one, see <em>id., </em>at 131, granted the motions to suppress in part. It concluded that the affidavit was insufficient to establish probable cause,<footnotemark>2</footnotemark> but did not suppress all of the evidence as to all of the respondents because none of the respondents had standing to challenge all of the searches.<footnotemark>3</footnotemark> In <page-number citation-index="1" label="904">*904</page-number>response to a request from the Government, the court made clear that Officer Rombach had acted in good faith, but it rejected the Government’s suggestion that the Fourth Amendment exclusionary rule should not apply where evidence is seized in reasonable, good-faith reliance on a search warrant.<footnotemark>4</footnotemark></p>
<p id="b946-5">The District Court denied the Government’s motion for reconsideration, id., at 147, and a divided panel of the Court of Appeals for the Ninth Circuit affirmed, judgt. order reported at <span class="citation multiple-matches"><a href="/c/F.%202d/701/187/">701 F. 2d 187</a></span> (1983). The Court of Appeals first concluded that Officer Rombach’s affidavit could not establish probable cause to search the Price Drive residence. To the extent that the affidavit set forth facts demonstrating the basis of the informant’s knowledge of criminal activity, the information included was fatally stale. The affidavit, moreover, failed to establish the informant’s credibility. Accordingly, the Court of Appeals concluded that the information provided by the informant was inadequate under both prongs of the two-part test established in <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), and <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969).<footnotemark>5</footnotemark> The officers’ independent investigation neither cured the staleness nor corroborated the details of the informant’s declarations. The Court of Appeals then considered whether the affidavit formed a proper basis for the <page-number citation-index="1" label="905">*905</page-number>search of the Sunset Canyon residence. In its view, the affidavit included no facts indicating the basis for the informants’ statements concerning respondent Leon’s criminal activities and was devoid of information establishing the informants’ reliability. Because these deficiencies had not been cured by the police investigation, the District Court properly suppressed the fruits of the search. The Court of Appeals refused the Government’s invitation to recognize a good-faith exception to the Fourth Amendment exclusionary rule. App. to Pet. for Cert. 4a.</p>
<p id="b947-5">The Government’s petition for certiorari expressly declined to seek review of the lower courts’ determinations that the search warrant was unsupported by probable cause and presented only the question “[w]hether the Fourth Amendment exclusionary rule should be modified so as not to bar the admission of evidence seized in reasonable, good-faith reliance on a search warrant that is subsequently held to be defective.” We granted certiorari to consider the propriety of such a modification. <span class="citation multiple-matches"><a href="/c/U.%20S./463/1206/">463 U. S. 1206</a></span> (1983). Although it undoubtedly is within our power to consider the question whether probable cause existed under the “totality of the circumstances” test announced last Term in <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213</a></span> (1983), that question has not been briefed or argued; and it is also within our authority, which we choose to exercise, to take the case as it comes to us, accepting the Court of Appeals’ conclusion that probable cause was lacking under the prevailing legal standards. See this Court’s Rule 21.1(a).</p>
<p id="b947-6">We have concluded that, in the Fourth Amendment context, the exclusionary rule can be modified somewhat without jeopardizing its ability to perform its intended functions. Accordingly, we reverse the judgment of the Court of Appeals.</p>
<p id="b947-7">II</p>
<p id="b947-8">Language in opinions of this Court and of individual Justices has sometimes implied that the exclusionary rule is a necessary corollary of the Fourth Amendment, <em>Mapp </em>v. <page-number citation-index="1" label="906">*906</page-number><em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#651" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 651, 655-657</a></span> (1961); <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#462" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 462-463</a></span> (1928), or that the rule is required by the conjunction of the Fourth and Fifth Amendments. <em>Mapp </em>v. <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#661" aria-description="Citation for case: Mapp v. Ohio"><em>Ohio, supra, </em>at 661-662</a></span> (Black, J., concurring); <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33-34</a></span> (1925). These implications need not detain us long. The Fifth Amendment theory has not withstood critical analysis or the test of time, see <em>Andresen </em>v. <em>Maryland, </em><span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">427 U. S. 463</a></span> (1976), and the Fourth Amendment “has never been interpreted to proscribe the introduction of illegally seized evidence in all proceedings or against all persons.” <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 486</a></span> (1976).</p>
<p id="b948-5">A</p>
<p id="b948-6">The Fourth Amendment contains no provision expressly precluding the use of evidence obtained in violation of its commands, and an examination of its origin and purposes makes clear that the use of fruits of a past unlawful search or seizure “work[s] no new Fourth Amendment wrong.” <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#354" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 354</a></span> (1974). The wrong condemned by the Amendment is “fully accomplished” by the unlawful search or seizure itself, <em>ibid., </em>and the exclusionary rule is neither intended nor able to “cure the invasion of the defendant’s rights which he has already suffered.” <em>Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#540" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 540</a></span> (White, J., dissenting). The rule thus operates as “a judicially created remedy designed to safeguard Fourth Amendment rights generally through its deterrent effect, rather than a personal constitutional right of the party aggrieved.” <em>United States </em>v. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>.</p>
<p id="b948-7">Whether the exclusionary sanction is appropriately imposed in a particular case, our decisions make clear, is “an issue separate from the question whether the Fourth Amendment rights of the party seeking to invoke the rule were violated by police conduct.” <em>Illinois </em>v. <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#223" aria-description="Citation for case: Illinois v. Gates"><em>Gates, supra, </em>at 223</a></span>. Only the former question is currently before us, and it must <page-number citation-index="1" label="907">*907</page-number>be resolved by weighing the costs and benefits of preventing the use in the prosecution’s case in chief of inherently trustworthy tangible evidence obtained in reliance on a search warrant issued by a detached and neutral magistrate that ultimately is found to be defective.</p>
<p id="b949-5">The substantial social costs exacted by the exclusionary rule for the vindication of Fourth Amendment rights have long been a source of concern. “Our cases have consistently recognized that unbending application of the exclusionary sanction to enforce ideals of governmental rectitude would impede unacceptably the truth-finding functions of judge and jury.” <em>United States </em>v. <em>Payner, </em><span class="citation" data-id="9428014"><a href="/opinion/110317/united-states-v-payner/#734" aria-description="Citation for case: United States v. Payner">447 U. S. 727, 734</a></span> (1980). An objectionable collateral consequence of this interference with the criminal justice system’s truth-finding function is that some guilty defendants may go free or receive reduced sentences as a result of favorable plea bargains.<footnotemark>6</footnotemark> Particu<page-number citation-index="1" label="908">*908</page-number>larly when law enforcement officers have acted in objective good faith or their transgressions have been minor, the magnitude of the benefit conferred on such guilty defendants offends basic concepts of the criminal justice system. <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#490" aria-description="Citation for case: Stone v. Powell">428 U. S., at 490</a></span>. Indiscriminate application of the exclusionary rule, therefore, may well “generate] disrespect for the law and administration of justice.” <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#491" aria-description="Citation for case: Stone v. Powell">Id., at 491</a></span>. Accordingly, “[a]s with any remedial device, the application of the rule has been restricted to those areas where its remedial objectives are thought most efficaciously served.” <em>United States </em>v. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>; see <em>Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 486-487</a></span>; <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#447" aria-description="Citation for case: United States v. Janis">428 U. S. 433, 447</a></span> (1976).</p>
<p id="b950-5">B</p>
<p id="b950-6">Close attention to those remedial objectives has characterized our recent decisions concerning the scope of the Fourth Amendment exclusionary rule. The Court has, to be sure, not seriously questioned, “in the absence of a more efficacious sanction, the continued application of the rule to suppress ev<page-number citation-index="1" label="909">*909</page-number>idence from the [prosecution’s] case where a Fourth Amendment violation has been substantial and deliberate. ...” <em>Franks </em>v. <em>Delaware, </em><span class="citation" data-id="9427321"><a href="/opinion/109925/franks-v-delaware/#171" aria-description="Citation for case: Franks v. Delaware">438 U. S. 154, 171</a></span> (1978); <em>Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#492" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 492</a></span>. Nevertheless, the balancing approach that has evolved in various contexts — including criminal trials — “forcefully suggests] that the exclusionary rule be more generally modified to permit the introduction of evidence obtained in the reasonable good-faith belief that a search or seizure was in accord with the Fourth Amendment.” <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#255" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 255</a></span> (WHITE, J., concurring in judgment).</p>
<p id="b951-5">In <em>Stone </em>v. <em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Powell, supra,</a></span> </em>the Court emphasized the costs of the exclusionary rule, expressed its view that limiting the circumstances under which Fourth Amendment claims could be raised in federal habeas corpus proceedings would not reduce the rule’s deterrent effect, <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#489" aria-description="Citation for case: Stone v. Powell"><em>id., </em>at 489-495</a></span>, and held that a state prisoner who has been afforded a full and fair opportunity to litigate a Fourth Amendment claim may not obtain federal habeas relief on the ground that unlawfully obtained evidence had been introduced at his trial. Cf. <em>Rose </em>v. <em>Mitchell, </em><span class="citation" data-id="9427696"><a href="/opinion/110143/rose-v-mitchell/#560" aria-description="Citation for case: Rose v. Mitchell">443 U. S. 545, 560-563</a></span> (1979). Proposed extensions of the exclusionary rule to proceedings other than the criminal trial itself have been evaluated and rejected under the same analytic approach. In <em>United States </em>v. <em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">Calandra</a></span>, </em>for example, we declined to allow grand jury witnesses to refuse to answer questions based on evidence obtained from an unlawful search or seizure since “[a]ny incremental deterrent effect which might be achieved by extending the rule to grand jury proceedings is uncertain at best.” <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S., at 348</a></span>. Similarly, in <em>United States </em>v. <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis, supra,</a></span> </em>we permitted the use in federal civil proceedings of evidence illegally seized by state officials since the likelihood of deterring police misconduct through such an extension of the exclusionary rule was insufficient to outweigh its substantial social costs. In so doing, we declared that, “[i]f . . . the exclusionary rule does not result in appreciable deterrence, then, clearly, its use in the instant situation is unwarranted.” <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#454" aria-description="Citation for case: United States v. Janis"><em>Id., </em>at 454</a></span>.</p>
<p id="b952-4"><page-number citation-index="1" label="910">*910</page-number>As cases considering the use of unlawfully obtained evidence in criminal trials themselves make clear, it does not follow from the emphasis on the exclusionary rule’s deterrent value that “anything which deters illegal searches is thereby commanded by the Fourth Amendment.” <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States">394 U. S., at 174</a></span>. In determining whether persons aggrieved solely by the introduction of damaging evidence unlawfully obtained from their co-conspirators or codefendants could seek suppression, for example, we found that the additional benefits of such an extension of the exclusionary rule would not outweigh its costs. <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States"><em>Id., </em>at 174-175</a></span>. Standing to invoke the rule has thus been limited to cases in which the prosecution seeks to use the fruits of an illegal search or seizure against the victim of police misconduct. <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978); <em>Brown </em>v. <em>United States, </em><span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/" aria-description="Citation for case: Brown v. United States">411 U. S. 223</a></span> (1973); <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#491" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 491-492</a></span> (1963). Cf. <em>United States </em>v. <em>Payner, </em><span class="citation" data-id="9428014"><a href="/opinion/110317/united-states-v-payner/" aria-description="Citation for case: United States v. Payner">447 U. S. 727</a></span> (1980).</p>
<p id="b952-5">Even defendants with standing to challenge the introduction in their criminal trials of unlawfully obtained evidence cannot prevent every conceivable use of such evidence. Evidence obtained in violation of the Fourth Amendment and inadmissible in the prosecution’s case in chief may be used to impeach a defendant’s direct testimony. <em>Walder </em>v. <em>United States, </em><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span> (1954). See also <em>Oregon </em>v. <em>Hass, </em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714</a></span> (1975); <em>Harris </em>v. <em>New York, </em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971). A similar assessment of the “incremental furthering” of the ends of the exclusionary rule led us to conclude in <em>United States </em>v. <em>Havens, </em><span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#627" aria-description="Citation for case: United States v. Havens">446 U. S. 620, 627</a></span> (1980), that evidence inadmissible in the prosecution’s case in chief or otherwise as substantive evidence of guilt may be used to impeach statements made by a defendant in response to “proper cross-examination reasonably suggested by the defendant’s direct examination.” <span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#627" aria-description="Citation for case: United States v. Havens"><em>Id., </em>at 627-628</a></span>.</p>
<p id="b952-6">When considering the use of evidence obtained in violation of the Fourth Amendment in the prosecution’s case in chief, moreover, we have declined to adopt a <em>per se </em>or “but for” rule <page-number citation-index="1" label="911">*911</page-number>that would render inadmissible any evidence that came to light through a chain of causation that began with an illegal arrest. <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975); <em>Wong Sun </em>v. <em>United States, supra, </em>at 487-488. We also have held that a witness’ testimony may be admitted even when his identity was discovered in an unconstitutional search. <em>United States </em>v. <em>Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">435 U. S. 268</a></span> (1978). The perception underlying these decisions — that the connection between police misconduct and evidence of crime may be sufficiently attenuated to permit the use of that evidence at trial — is a product of considerations relating to the exclusionary rule and the constitutional principles it is designed to protect. <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#217" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 217-218</a></span> (1979); <em>United States </em>v. <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#279" aria-description="Citation for case: United States v. Ceccolini"><em>Ceccolini, supra, </em>at 279</a></span>.<footnotemark>7</footnotemark> In short, the “dissipation of the taint” concept that the Court has applied in deciding whether exclusion is appropriate in a particular case “attempts to mark the point at which the detrimental consequences of illegal police action become so attenuated that the deterrent effect of the exclusionary rule no longer justifies its cost.” <em>Brown </em>v. <em>Illinois, supra, </em>at 609 (Powell, J., concurring in part). Not surprisingly in view of this purpose, an assessment of the flagrancy of the police misconduct constitutes an important step in the calculus. <em>Dunaway </em>v. <em>New York, supra, </em>at 218; <em>Brown </em>v. <em>Illinois, supra, </em>at 603-604.</p>
<p id="b953-5">The same attention to the purposes underlying the exclusionary rule also has characterized decisions not involving the scope of the rule itself. We have not required suppression of the fruits of a search incident to an arrest made in good-faith reliance on a substantive criminal statute that subsequently <page-number citation-index="1" label="912">*912</page-number>is declared unconstitutional. <em>Michigan </em>v. <em>DeFillippo, </em><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">443 U. S. 31</a></span> (1979).<footnotemark>8</footnotemark> Similarly, although the Court has been unwilling to conclude that new Fourth Amendment principles are always to have only prospective effect, <em>United States </em>v. <em>Johnson, </em><span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/#560" aria-description="Citation for case: United States v. Johnson">457 U. S. 537, 560</a></span> (1982),<footnotemark>9</footnotemark> no Fourth Amendment decision marking a “clear break with the past” has been applied retroactively. See <em>United States </em>v. <em>Peltier, </em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/" aria-description="Citation for case: United States v. Peltier">422 U. S. 531</a></span> (1975); <em>Desist </em>v. <em>United States, </em><span class="citation" data-id="9423951"><a href="/opinion/107875/desist-v-united-states/" aria-description="Citation for case: Desist v. United States">394 U. S. 244</a></span> (1969); <em>Linkletter </em>v. <em>Walker, </em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618</a></span> (1965).<footnotemark>10</footnotemark> The propriety <page-number citation-index="1" label="913">*913</page-number>of retroactive application of a newly announced Fourth Amendment principle, moreover, has been assessed largely in terms of the contribution retroactivity might make to the deterrence of police misconduct. <em>United States </em>v. <span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/#560" aria-description="Citation for case: United States v. Johnson"><em>Johnson, supra, </em>at 560-561</a></span>; <em>United States </em>v. <span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#536" aria-description="Citation for case: United States v. Peltier"><em>Peltier, supra, </em>at 536-539, 542</a></span>.</p>
<p id="b955-9">As yet, we have not recognized any form of good-faith exception to the Fourth Amendment exclusionary rule.<footnotemark>11</footnotemark> But the balancing approach that has evolved during the years of experience with the rule provides strong support for the modification currently urged upon us. As we discuss below, our evaluation of the costs and benefits of suppressing reliable physical evidence seized by officers reasonably relying on a warrant issued by a detached and neutral magistrate leads to the conclusion that such evidence should be admissible in the prosecution’s case in chief.</p>
<p id="b955-10">HH HH</p>
<p id="b955-3">A</p>
<p id="b955-4">Because a search warrant “provides the detached scrutiny of a neutral magistrate, which is a more reliable safeguard <page-number citation-index="1" label="914">*914</page-number>against improper searches than the hurried judgment of a law enforcement officer ‘engaged in the often competitive enterprise of ferreting out crime,’ ” <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#9" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 9</a></span> (1977) (quoting <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948)), we have expressed a strong preference for warrants and declared that “in a doubtful or marginal case a search under a warrant may be sustainable where without one it would fall.” <em>United States </em>v. <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#106" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 106</a></span> (1965). See <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#111" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 111</a></span>. Reasonable minds frequently may differ on the question whether a particular affidavit establishes probable cause, and we have thus concluded that the preference for warrants is most appropriately effectuated by according “great deference” to a magistrate’s determination. <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#419" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 419</a></span>. See <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#236" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 236</a></span>; <em>United States </em>v. <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca"><em>Ventresca, supra, </em>at 108-109</a></span>.</p>
<p id="b956-5">Deference to the magistrate, however, is not boundless. It is clear, first, that the deference accorded to a magistrate’s finding of probable cause does not preclude inquiry into the knowing or reckless falsity of the affidavit on which that determination was based. <em>Franks </em>v. <em>Delaware, </em><span class="citation" data-id="9427321"><a href="/opinion/109925/franks-v-delaware/" aria-description="Citation for case: Franks v. Delaware">438 U. S. 154</a></span> (1978).<footnotemark>12</footnotemark> Second, the courts must also insist that the magistrate purport to “perform his ‘neutral and detached’ function and not serve merely as a rubber stamp for the police.” <em>Aguilar </em>v. <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#111" aria-description="Citation for case: Aguilar v. Texas"><em>Texas, supra, </em>at 111</a></span>. See <em>Illinois </em>v. <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#239" aria-description="Citation for case: Illinois v. Gates"><em>Gates, supra, </em>at 239</a></span>. A magistrate failing to “manifest that neutrality and detachment demanded of a judicial officer when presented with a warrant application” and who acts instead as “an adjunct law enforcement officer” cannot provide valid authorization for an otherwise unconstitutional search. <em>Lo-Ji Sales, Inc. </em>v. <em>New York, </em><span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/#326" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York">442 U. S. 319, 326-327</a></span> (1979).</p>
<p id="b957-4"><page-number citation-index="1" label="915">*915</page-number>Third, reviewing courts will not defer to a warrant based on an affidavit that does not “provide the magistrate with a substantial basis for determining the existence of probable cause.” <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#239" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 239</a></span>. “Sufficient information must be presented to the magistrate to allow that official to determine probable cause; his action cannot be a mere ratification of the bare conclusions of others.” <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Ibid.</a></span> </em>See <em>Aguilar </em>v. <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#114" aria-description="Citation for case: Aguilar v. Texas"><em>Texas, supra, </em>at 114-115</a></span>; <em>Giordenello </em>v. <em>United States, 357 </em>U. S. 480 (1958); <em>Nathanson </em>v. <em>United States, </em><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span> (1933).<footnotemark>13</footnotemark> Even if the warrant application was supported by more than a “bare bones” affidavit, a reviewing court may properly conclude that, notwithstanding the deference that magistrates deserve, the warrant was invalid because the magistrate’s probable-cause determination reflected an improper analysis of the totality of the circumstances, <em>Illinois </em>v. <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#238" aria-description="Citation for case: Illinois v. Gates"><em>Gates, supra, </em>at 238-239</a></span>, or because the form of the warrant was improper in some respect.</p>
<p id="b957-5">Only in the first of these three situations, however, has the Court set forth a rationale for suppressing evidence obtained pursuant to a search warrant; in the other areas, it has simply excluded such evidence without considering whether <page-number citation-index="1" label="916">*916</page-number>Fourth Amendment interests will be advanced. To the extent that proponents of exclusion rely on its behavioral effects on judges and magistrates in these areas, their reliance is misplaced. First, the exclusionary rule is designed to deter police misconduct rather than to punish the errors of judges and magistrates. Second, there exists no evidence suggesting that judges and magistrates are inclined to ignore or subvert the Fourth Amendment or that lawlessness among these actors requires application of the extreme sanction of exclusion.<footnotemark>14</footnotemark></p>
<p id="b958-5">Third, and most important, we discern no basis, and are offered none, for believing that exclusion of evidence seized pursuant to a warrant will have a significant deterrent effect on the issuing judge or magistrate.<footnotemark>15</footnotemark> Many of the factors <page-number citation-index="1" label="917">*917</page-number>that indicate that the exclusionary rule cannot provide an effective “special” or “general” deterrent for individual offending law enforcement officers<footnotemark>16</footnotemark> apply as well to judges or magistrates. And, to the extent that the rule is thought to operate as a “systemic” deterrent on a wider audience,<footnotemark>17</footnotemark> it clearly can have no such effect on individuals empowered to issue search warrants. Judges and magistrates are not adjuncts to the law enforcement team; as neutral judicial officers, they have no stake in the outcome of particular criminal prosecutions. The threat of exclusion thus cannot be expected significantly to deter them. Imposition of the exclusionary sanction is not necessary meaningfully to inform judicial officers of their errors, and we cannot conclude that admitting evidence obtained pursuant to a warrant while at the same time declaring that the warrant was somehow defective will in any way reduce judicial officers’ professional incentives to comply with the Fourth Amendment, encourage them to repeat their mistakes, or lead to the granting of all colorable warrant requests.<footnotemark>18</footnotemark></p>
<p id="b960-4"><page-number citation-index="1" label="918">*918</page-number>B</p>
<p id="b960-5">If exclusion of evidence obtained pursuant to a subsequently invalidated warrant is to have any deterrent effect, therefore, it must alter the behavior of individual law enforcement officers or the policies of their departments. One could argue that applying the exclusionary rule in cases where the police failed to demonstrate probable cause in the warrant application deters future inadequate presentations or “magistrate shopping” and thus promotes the ends of the Fourth Amendment. Suppressing evidence obtained pursuant to a technically defective warrant supported by probable cause also might encourage officers to scrutinize more closely the form of the warrant and to point out suspected judicial errors. We find such arguments speculative and conclude that suppression of evidence obtained pursuant to a warrant should be ordered only on a case-by-case basis and only in those unusual cases in which exclusion will further the purposes of the exclusionary rule.<footnotemark>19</footnotemark></p>
<p id="b960-6">We have frequently questioned whether the exclusionary rule can have any deterrent effect when the offending officers acted in the objectively reasonable belief that their conduct did not violate the Fourth Amendment. “No empirical researcher, proponent or opponent of the rule, has yet been able to establish with any assurance whether the rule has a deterrent effect. . . .” <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#452" aria-description="Citation for case: United States v. Janis">428 U. S., at 452, n. 22</a></span>. But even assuming that the rule effectively <page-number citation-index="1" label="919">*919</page-number>deters some police misconduct and provides incentives for the law enforcement profession as a whole to conduct itself in accord with the Fourth Amendment, it cannot be expected, and should not be applied, to deter objectively reasonable law enforcement activity.</p>
<p id="b961-5">As we observed in <em>Michigan </em>v. <em>Tucker, </em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#447" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 447</a></span> (1974), and reiterated in <em>United States </em>v. <em>Peltier, </em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/" aria-description="Citation for case: United States v. Peltier">422 U. S., at 539</a></span>:</p>
<blockquote id="b961-6">“The deterrent purpose of the exclusionary rule necessarily assumes that the police have engaged in willful, or at the very least negligent, conduct which has deprived the defendant of some right. By refusing to admit evidence gained as a result of such conduct, the courts hope to instill in those particular investigating officers, or in their future counterparts, a greater degree of care toward the rights of an accused. Where the official action was pursued in complete good faith, however, the deterrence rationale loses much of its force.”</blockquote>
<p id="b961-7">The <em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/" aria-description="Citation for case: United States v. Peltier">Peltier</a></span> </em>Court continued, <em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/" aria-description="Citation for case: United States v. Peltier">id.,</a></span> </em>at 542:</p>
<blockquote id="b961-8">“If the purpose of the exclusionary rule is to deter unlawful police conduct, then evidence obtained from a search should be suppressed only if it can be said that the law enforcement officer had knowledge, or may properly be charged with knowledge, that the search was unconstitutional under the Fourth Amendment.”</blockquote>
<p id="b961-9">See also <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#260" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 260-261</a></span> (White, J., concurring in judgment); <em>United States </em>v. <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#459" aria-description="Citation for case: United States v. Janis"><em>Janis, supra, </em>at 459</a></span>; <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#610" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 610-611</a></span> (Powell, J., concurring in part).<footnotemark>20</footnotemark> In short, where the officer’s conduct is objectively reasonable,</p>
<blockquote id="b962-4"><page-number citation-index="1" label="920">*920</page-number>“excluding the evidence will not further the ends of the exclusionary rule in any appreciable way; for it is painfully apparent that. . . the officer is acting as a reasonable officer would and should act in similar circumstances. Excluding the evidence can in no way affect his future conduct unless it is to make him less willing to do his duty.” <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#539" aria-description="Citation for case: Stone v. Powell">428 U. S., at 539-540</a></span> (White, J., dissenting).</blockquote>
<p id="b962-5">This is particularly true, we believe, when an officer acting with objective good faith has obtained a search warrant from a judge or magistrate and acted within its scope.<footnotemark>21</footnotemark> In most <page-number citation-index="1" label="921">*921</page-number>such cases, there is no police illegality and thus nothing to deter. It is the magistrate’s responsibility to determine whether the officer’s allegations establish probable cause and, if so, to issue a warrant comporting in form with the requirements of the Fourth Amendment. In the ordinary case, an officer cannot be expected to question the magistrate’s probable-cause determination or his judgment that the form of the warrant is technically sufficient. “[Ojnce the warrant issues, there is literally nothing more the policeman can do in seeking to comply with the law.” <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#498" aria-description="Citation for case: Stone v. Powell"><em>Id., </em>at 498</a></span> (Burger, C. J., concurring). Penalizing the officer for the magistrate’s error, rather than his own, cannot logically contribute to the deterrence of Fourth Amendment violations.<footnotemark>22</footnotemark></p>
<p id="b964-4"><page-number citation-index="1" label="922">*922</page-number>c</p>
<p id="b964-5">We conclude that the marginal or nonexistent benefits produced by suppressing evidence obtained in objectively reasonable reliance on a subsequently invalidated search warrant cannot justify the substantial costs of exclusion. We do not suggest, however, that exclusion is always inappropriate in cases where an officer has obtained a warrant and abided by its terms. “[Searches pursuant to a warrant will rarely require any deep inquiry into reasonableness,” <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#267" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 267</a></span> (White, J., concurring in judgment), for “a warrant issued by a magistrate normally suffices to establish” that a law enforcement officer has “acted in good faith in conducting the search.” <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#823" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 823, n. 32</a></span> (1982). Nevertheless, the officer’s reliance on the magistrate’s probable-cause determination and on the technical sufficiency of the warrant he issues must be objectively reasonable, cf. <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#815" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 815-819</a></span> (1982),<footnotemark>23</footnotemark> and it is clear that in some eircum-<page-number citation-index="1" label="923">*923</page-number>stances the officer<footnotemark>24</footnotemark> will have no reasonable grounds for believing that the warrant was properly issued.</p>
<p id="b965-5">Suppression therefore remains an appropriate remedy if the magistrate or judge in issuing a warrant was misled by information in an affidavit that the affiant knew was false or would have known was false except for his reckless disregard of the truth. <em>Franks </em>v. <em>Delaware, </em><span class="citation" data-id="9427321"><a href="/opinion/109925/franks-v-delaware/" aria-description="Citation for case: Franks v. Delaware">438 U. S. 154</a></span> (1978). The exception we recognize today will also not apply in cases where the issuing magistrate wholly abandoned his judicial role in the manner condemned in <em>Lo-Ji Sales, Inc. </em>v. <em>New York, </em><span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York">442 U. S. 319</a></span> (1979); in such circumstances, no reasonably well trained officer should rely on the warrant. Nor would an officer manifest objective good faith in relying on a warrant based on an affidavit “so lacking in indicia of probable cause as to render official belief in its existence entirely unreasonable.” <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#610" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 610-611</a></span> (Powell, J., concurring in part); see <em>Illinois </em>v. <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#263" aria-description="Citation for case: Illinois v. Gates"><em>Gates, supra, </em>at 263-264</a></span> (White, J., concurring in judgment). Finally, depending on the circumstances of the particular case, a warrant may be so facially <em>deficient </em>— i. <em>e., </em>in failing to particularize the place to be searched or the things to be seized— that the executing officers cannot reasonably presume it to be valid. Cf. <em>Massachusetts </em>v. <em>Sheppard, post, </em>at 988-991.</p>
<p id="b965-6">In so limiting the suppression remedy, we leave untouched the probable-cause standard and the various requirements for a valid warrant. Other objections to the modification of <page-number citation-index="1" label="924">*924</page-number>the Fourth Amendment exclusionary rule we consider to be insubstantial. The good-faith exception for searches conducted pursuant to warrants is not intended to signal our unwillingness strictly to enforce the requirements of the Fourth Amendment, and we do not believe that it will have this effect. As we have already suggested, the good-faith exception, turning as it does on objective reasonableness, should not be difficult to apply in practice. When officers have acted pursuant to a warrant, the prosecution should ordinarily be able to establish objective good faith without a substantial expenditure of judicial time.</p>
<p id="b966-5">Nor are we persuaded that application of a good-faith exception to searches conducted pursuant to warrants will preclude review of the constitutionality of the search or seizure, deny needed guidance from the courts, or freeze Fourth Amendment law in its present state.<footnotemark>25</footnotemark> There is no need for courts to adopt the inflexible practice of always deciding whether the officers’ conduct manifested objective good faith before turning to the question whether the Fourth Amendment has been violated. Defendants seeking suppression of the fruits of allegedly unconstitutional searches or seizures undoubtedly raise live controversies which Art. Ill empowers federal courts to adjudicate. As cases addressing questions of good-faith immunity under <span class="citation no-link">42 U. S. C. § 1983</span>, compare <em>O’Connor </em>v. Donaldson, <span class="citation" data-id="9842006"><a href="/opinion/109303/oconnor-v-donaldson/" aria-description="Citation for case: O&#x27;Connor v. Donaldson">422 U. S. 563</a></span> (1975), with <em>Procunier </em>v. <em>Navarette, </em><span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/#566" aria-description="Citation for case: Procunier v. Navarette">434 U. S. 555, 566, n. 14</a></span> (1978), and cases involving the harmless-error doctrine, compare <em>Milton </em>v. <em>Wainwright, </em><span class="citation" data-id="9424959"><a href="/opinion/108585/milton-v-wainwright/#372" aria-description="Citation for case: Milton v. Wainwright">407 U. S. 371, 372</a></span> (1972), with <em>Coleman </em>v. <em>Alabama, </em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970), make clear, courts have consid<page-number citation-index="1" label="925">*925</page-number>erable discretion in conforming their decisionmaking processes to the exigencies of particular cases.</p>
<p id="b967-5">If the resolution of a particular Fourth Amendment question is necessary to guide future action by law enforcement officers and magistrates, nothing will prevent reviewing courts from deciding that question before turning to the good-faith issue.<footnotemark>26</footnotemark> Indeed, it frequently will be difficult to determine whether the officers acted reasonably without resolving the Fourth Amendment issue. Even if the Fourth Amendment question is not one of broad import, reviewing courts could decide in particular cases that magistrates under their supervision need to be informed of their errors and so evaluate the officers’ good faith only after finding a violation. In other circumstances, those courts could reject suppression motions posing no important Fourth Amendment questions by turning immediately to a consideration of the officers’ good faith. We have no reason to believe that our Fourth Amendment jurisprudence would suffer by allowing reviewing courts to exercise an informed discretion in making this choice.</p>
<p id="b967-8">I<em>V</em></p>
<p id="b967-6">When the principles we have enunciated today are applied to the facts of this case, it is apparent that the judgment of the Court of Appeals cannot stand. The Court of Appeals applied the prevailing legal standards to Officer Rombach’s warrant application and concluded that the application could not support the magistrate’s probable-cause determination. In so doing, the court clearly informed the magistrate that he <page-number citation-index="1" label="926">*926</page-number>had erred in issuing the challenged warrant. This aspect of the court’s judgment is not under attack in this proceeding.</p>
<p id="b968-5">Having determined that the warrant should not have issued, the Court of Appeals understandably declined to adopt a modification of the Fourth Amendment exclusionary rule that this Court had not previously sanctioned. Although the modification finds strong support in our previous cases, the Court of Appeals’ commendable self-restraint is not to be criticized. We have now reexamined the purposes of the exclusionary rule and the propriety of its application in cases where officers have relied on a subsequently invalidated search warrant. Our conclusion is that the rule’s purposes will only rarely be served by applying it in such circumstances.</p>
<p id="b968-6">In the absence of an allegation that the magistrate abandoned his detached and neutral role, suppression is appropriate only if the officers were dishonest or reckless in preparing their affidavit or could not have harbored an objectively reasonable belief in the existence of probable cause. Only respondent Leon has contended that no reasonably well trained police officer could have believed that there existed probable cause to search his house; significantly, the other respondents advance no comparable argument. Officer Rombach’s application for a warrant clearly was supported by much more than a “bare bones” affidavit. The affidavit related the results of an extensive investigation and, as the opinions of the divided panel of the Court of Appeals make clear, provided evidence sufficient to create disagreement among thoughtful and competent judges as to the existence of probable cause. Under these circumstances, the officers’ reliance on the magistrate’s determination of probable cause was objectively reasonable, and application of the extreme sanction of exclusion is inappropriate.</p>
<p id="b968-7">Accordingly, the judgment of the Court of Appeals is</p>
<p id="b968-8">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b945-5"> Respondent Leon moved to suppress the evidence found on his person at the time of his arrest and the evidence seized from his residence at 716 South Sunset Canyon. Respondent Stewart’s motion covered the fruits of searches of her residence at 620 Price Drive and the condominium at 7902 Via Magdalena and statements she made during the search of her residence. Respondent Sanchez sought to suppress the evidence discovered during the search of his residence at 620 Price Drive and statements he made shortly thereafter. He also joined Stewart’s motion to suppress evidence seized from the condominium. Respondent Del Castillo apparently sought to suppress all of the evidence seized in the searches. App. 78-80. The respondents also moved to suppress evidence seized in the searches of their automobiles.</p>
</footnote>
<footnote label="2">
<p id="b945-6"> “I just cannot find this warrant sufficient for a showing of probable cause.</p>
<blockquote id="b945-7">“There is no question of the reliability and credibility of the informant as not being established.</blockquote>
<blockquote id="b945-8">“Some details given tended to corroborate, maybe, the reliability of [the informant’s] information about the previous transaction, but if it is not a stale transaction, it comes awfully close to it; and all the other material I think is as consistent with innocence as it is with guilt.</blockquote>
<blockquote id="b945-9">“So I just do not think this affidavit can withstand the test. I find, then, that there is no probable cause in this case for the issuance of the search warrant. . . .” <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#127" aria-description="Citation for case: Coleman v. Alabama"><em>Id., </em>at 127</a></span>.</blockquote>
</footnote>
<footnote label="3">
<p id="b945-10"> The District Court concluded that Sanchez and Stewart had standing to challenge the search of 620 Price Drive; that Leon had standing to contest the legality of the search of 716 South Sunset Canyon; that none of the respondents had established a legitimate expectation of privacy in the condominium at 7902 Via Magdalena; and that Stewart and Del Castillo each had standing to challenge the searches of their automobiles. The <page-number citation-index="1" label="904">*904</page-number>Government indicated that it did not intend to introduce evidence seized from the other respondents’ vehicles. <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#127" aria-description="Citation for case: Coleman v. Alabama"><em>Id., </em>at 127-129</a></span>. Finally, the court suppressed statements given by Sanchez and Stewart. <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#129" aria-description="Citation for case: Coleman v. Alabama"><em>Id., </em>at 129-130</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b946-9"><em> “On </em>the issue of good faith, obviously that is not the law of the Circuit, and I am not going to apply that law.</p>
<blockquote id="b946-10">“I will say certainly in my view, there is not any question about good faith. [Officer Rombach] went to a Superior Court judge and got a warrant; obviously laid a meticulous trail. Had surveilled for a long period of time, and I believe his testimony — and I think he said he consulted with three Deputy District Attorneys before proceeding himself, and I certainly have no doubt about the fact that that is true.” <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#140" aria-description="Citation for case: Coleman v. Alabama"><em>Id., </em>at 140</a></span>.</blockquote>
</footnote>
<footnote label="5">
<p id="b946-11"> In <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213</a></span> (1983), decided last Term, the Court abandoned the two-pronged <em>Aguilar-Spinelli </em>test for determining whether an informant’s tip suffices to establish probable cause for the issuance of a warrant and substituted in its place a “totality of the circumstances” approach.</p>
</footnote>
<footnote label="6">
<p id="b949-6"> Researchers have only recently begun to study extensively the effects of the exclusionary rule on the disposition of felony arrests. One study suggests that the rule results in the nonprosecution or nonconviction of between 0.6% and 2.35% of individuals arrested for felonies. Davies, A Hard Look at What We Know (and Still Need to Learn) About the “Costs” of the Exclusionary Rule: The NIJ Study and Other Studies of “Lost” Arrests, 1988 A. B. F. Res. J. 611, 621. The estimates are higher for particular crimes the prosecution of which depends heavily on physical evidence. Thus, the cumulative loss due to nonproseeution or noneonviction of individuals arrested on felony drug charges is probably in the range of 2.8% to 7.1%. <em>Id., </em>at 680. Davies’ analysis of California data suggests that screening by police and prosecutors results in the release because of illegal searches or seizures of as many as 1.4% of all felony arrestees, id., at 650, that 0.9% of felony arrestees are released, because of illegal searches or seizures, at the preliminary hearing or after trial, <em>id., </em>at 653, and that roughly 0.05% of all felony arrestees benefit from reversals on appeal because of illegal searches. <em>Id., </em>at 654. See also K. Brosi, A Cross-City Comparison of Felony Case Processing 16, 18-19 (1979); U. S. General Accounting Office, Report of the Comptroller General of the United States, Impact of the Exclusionary Rule on Federal Criminal Prosecutions 10-11, 14 (1979); F. Feeney, F. Dill, &amp; A. Weir, Arrests Without Convictions: How Often They Occur and Why 203-206 (National Institute of Justice <page-number citation-index="1" label="908">*908</page-number>1983); National Institute of Justice, The Effects of the Exclusionary Rule: A Study in California 1-2 (1982); Nardulli, The Societal Cost of the Exclusionary Rule: An Empirical Assessment, 1983 A. B. F. Res. J. 585, 600. The exclusionary rule also has been found to affect the plea-bargaining process. S. Schlesinger, Exclusionary Injustice: The Problem of Illegally Obtained Evidence 63 (1977). But see Davies, <em>supra, </em>at 668-669; Nardulli, <em>supra, </em>at 604-606.</p>
<p id="b950-8">Many of these researchers have concluded that the impact of the exclusionary rule is insubstantial, but the small percentages with which they deal mask a large absolute number of felons who are released because the cases against them were based in part on illegal searches or seizures. “[A]ny rule of evidence that denies the jury access to clearly probative and reliable evidence must bear a heavy burden of justification, and must be carefully limited to the circumstances in which it will pay its way by deterring official unlawlessness.” <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#257" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 257-258</a></span> (White, J., concurring in judgment). Because we find that the rule can have no substantial deterrent effect in the sorts of situations under consideration in this case, see <em>infra, </em>at 916-921, we conclude that it cannot pay its way in those situations.</p>
</footnote>
<footnote label="7">
<p id="b953-6"> <em>“Brown’s, </em>focus on ‘the causal connection between the illegality and the confession’ reflected the two policies behind the use of the exclusionary rule to effectuate the Fourth Amendment. Where there is a close causal connection between the illegal seizure and the confession, not only is exclusion of the evidence more likely to deter similar police misconduct in the future, but use of the evidence is more likely to compromise the integrity of the courts.” <em>Dunaway </em>v. <em>New York, </em>442 U. S., at 217-218 (citation omitted).</p>
</footnote>
<footnote label="8">
<p id="b954-5"> We have held, however, that the exclusionary rule requires suppression of evidence obtained in searches carried out pursuant to statutes, not yet declared unconstitutional, purporting to authorize searches and seizures without probable cause or search warrants. See, <em>e. g., Ybarra </em>v. <em>Illinois, </em><span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85</a></span> (1979); <em>Torres </em>v. <em>Puerto Rico, </em><span class="citation" data-id="9795098"><a href="/opinion/2620876/torres-v-puerto-rico/" aria-description="Citation for case: Torres v. Puerto Rico">442 U. S. 465</a></span> (1979); <em>Almeida-Sanchez </em>v. <em>United States, </em><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973); <em>Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span> (1968); <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967). “Those decisions involved statutes which, by their own terms, authorized searches under circumstances which did not satisfy the traditional warrant and probable-cause requirements of the Fourth Amendment.” <em>Michigan </em>v. <em>DeFillippo, </em><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/#39" aria-description="Citation for case: Michigan v. DeFillippo">443 U. S., at 39</a></span>. The substantive Fourth Amendment principles announced in those eases are fully consistent with our holding here.</p>
</footnote>
<footnote label="9">
<p id="AARi"> The Court held in <em>United States </em>v. <em>Johnson, </em>that a construction of the sFourth Amendment that did not constitute a “clear break with the past” is to be applied to all convictions not yet final when the decision was handed down. The limited holding, see 457 U. S., at 562, turned in part on the Court’s judgment that “[fjailure to accord <em>any </em>retroactive effect to Fourth Amendment rulings would ‘encourage police or other courts to disregard the plain purport of our decisions and to adopt a let’s-wait-until-it’s-decided approach.’” <em>Id., </em>at 561 (emphasis in original) (quoting <em>Desist </em>v. <em>United States, </em><span class="citation" data-id="9423951"><a href="/opinion/107875/desist-v-united-states/#277" aria-description="Citation for case: Desist v. United States">394 U. S. 244, 277</a></span> (1969) (Fortas, J., dissenting)). Contrary to respondents’ assertions, nothing in <em>Johnson </em>precludes adoption of a good-faith exception tailored to situations in which the police have reasonably relied on a warrant issued by a detached and neutral magistrate but later found to be defective.</p>
</footnote>
<footnote label="10">
<p id="b954-7"> Our retroactivity decisions have, for the most part, turned on our assessments of “(a) the purpose to be served by the new standards, (b) the extent of the reliance by law enforcement authorities on the old standards, and (c) the effect on the administration of justice of a retroactive application of the new standards.” <em>Stovall </em>v. <em>Denno, </em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#297" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293, 297</a></span> (1967). As we observed earlier this Term:</p>
<blockquote id="b955-5"><page-number citation-index="1" label="913">*913</page-number>“In considering the reliance factor, this Court’s cases have looked primarily to whether law enforcement authorities and state courts have justifiably relied on a prior rule of law said to be different from that announced by the decision whose retroactivity is at issue. Unjustified ‘reliance’ is no bar to retroactivity. This inquiry is often phrased in terms of whether the new decision was foreshadowed by earlier cases or was a ‘clear break with the past.’” <em>Solem </em>v. <em>Stumes, </em><span class="citation" data-id="9429516"><a href="/opinion/111112/solem-v-stumes/#645" aria-description="Citation for case: Solem v. Stumes">465 U. S. 638, 645-646</a></span> (1984).</blockquote>
</footnote>
<footnote label="11">
<p id="b955-6">Members of the Court have, however, urged reconsideration of the scope of the exclusionary rule. See, <em>e. g., Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#496" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 496</a></span> (1976) (Burgee, C. J., concurring); <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#536" aria-description="Citation for case: Stone v. Powell"><em>id., </em>at 536</a></span> (White, J., dissenting); <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#254" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 254-267</a></span> (White, J., concurring in judgment); <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#609" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590, 609-612</a></span> (1975) (Powell, J., concurring in part); <em>Schneckloth </em>v. <em>Bustamante, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#261" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 261-271</a></span> (1973) (Powell, J., concurring); <em>California </em>v. <em>Minjares, </em><span class="citation multiple-matches"><a href="/c/U.%20S./443/916/">443 U. S. 916</a></span> (1979) (Rehnquist, J., dissenting from denial of stay). One Court of Appeals, no doubt influenced by these individual urgings, has adopted a form of good-faith exception to the exclusionary rule. <em>United States </em>v. <em>Williams, </em><span class="citation" data-id="378896"><a href="/opinion/378896/united-states-v-jo-ann-williams/" aria-description="Citation for case: United States v. Jo Ann Williams">622 F. 2d 830</a></span> (CA5 1980) (en banc), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/1127/">449 U. S. 1127</a></span> (1981).</p>
</footnote>
<footnote label="12">
<p id="b956-6"> Indeed, <em>“it </em>would be an unthinkable imposition upon [the magistrate’s] authority if a warrant affidavit, revealed after the fact to contain a deliberately or recklessly false statement, were to stand beyond impeachment.” <span class="citation" data-id="9427321"><a href="/opinion/109925/franks-v-delaware/#165" aria-description="Citation for case: Franks v. Delaware">438 U. S., at 165</a></span>.</p>
</footnote>
<footnote label="13">
<p id="b957-6"> See also <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span> (1964), in which the Court concluded that “the record . . . does not contain a single objective fact to support a belief by the officers that the petitioner was engaged in criminal activity at the time they arrested him.” <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#95" aria-description="Citation for case: Beck v. Ohio"><em>Id., </em>at 95</a></span>. Although the Court was willing to assume that the arresting officers acted in good faith, it concluded:</p>
<blockquote id="b957-7">“‘[G]ood faith on the part of the arresting officers is not enough.’ <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#102" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 102</a></span>. If subjective good faith alone were the test, the protections of the Fourth Amendment would evaporate, and the people would be ‘secure in their persons, houses, papers, and effects,’ only in the discretion of the police.” <em>Id., </em>at 97.</blockquote>
<p id="b957-8">We adhere to this view and emphasize that nothing in this opinion is intended to suggest a lowering of the probable-cause standard. On the contrary, we deal here only with the remedy to be applied to a concededly unconstitutional search.</p>
</footnote>
<footnote label="14">
<p id="b958-6">Although there are assertions that some magistrates become rubber stamps for the police and others may be unable effectively to screen police conduct, see, <em>e.g.,2 </em>W. LaFave, Search and Seizure §4.1 (1978); Kamisar, Does (Did) (Should) The Exclusionary Rule Rest on a “Principled Basis” Rather than an “Empirical Proposition”?, <span class="citation no-link">16 Creighton L. Rev. 565</span>, 569-571 (1983); Schroeder, Deterring Fourth Amendment Violations: Alternatives to the Exclusionary Rule, 69 Geo. L. J. 1361, 1412 (1981), we are not convinced that this is a problem of major proportions. See L. Tiffany, D. McIntyre, &amp; D. Rotenberg, Detection of Crime 119 (1967); Israel, Criminal Procedure, the Burger Court, and the Legacy of the Warren Court, <span class="citation no-link">75 Mich. L. Rev. 1319</span>, 1414, n. 396 (1977); P. Johnson, New Approaches to Enforcing the Fourth Amendment 8-10 (Working Paper, Sept. 1978), quoted in Y. Kamisar, W. LaFave, &amp; J. Israel, Modern Criminal Procedure 229-230 (5th ed. 1980); R. Van Duizend, L. Sutton, &amp; C. Carter, The Search Warrant Process, eh. 7 (Review Draft, National Center for State Courts, 1983).</p>
</footnote>
<footnote label="15">
<p id="b958-7"> As the Supreme Judicial Court of Massachusetts recognized in <em>Commonwealth </em>v. <em>Sheppard, </em><span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#506" aria-description="Citation for case: Commonwealth v. Sheppard">387 Mass. 488, 506</a></span>, <span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#735" aria-description="Citation for case: Commonwealth v. Sheppard">441 N. E. 2d 725, 735</a></span> (1982):</p>
<blockquote id="b958-8">“The exclusionary rule may not be well tailored to deterring judicial misconduct. If applied to judicial misconduct, the rule would be just as costly as it is when it is applied to police misconduct, but it may be ill-fitted to the job-created motivations of judges. . . . [IJdeally a judge is impartial as to whether a particular piece of evidence is admitted or a particular defendant convicted. Hence, in the abstract, suppression of a particular piece of evidence may not be as effective a disincentive to a neutral judge as it would be to the police. It may be that a ruling by an appellate court that a <page-number citation-index="1" label="917">*917</page-number>search warrant was unconstitutional would be sufficient to deter similar conduct in the future by magistrates.”</blockquote>
<p id="b959-6">But see <em>United States </em>v. <em>Karathanos, </em><span class="citation" data-id="9462518"><a href="/opinion/333763/united-states-v-steve-karathanos-and-john-karathanos/#33" aria-description="Citation for case: United States v. Steve Karathanos and John Karathanos">531 F. 2d 26, 33-34</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./428/910/">428 U. S. 910</a></span> (1976).</p>
</footnote>
<footnote label="16">
<p id="b959-7"> See, e. <em>g., Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#498" aria-description="Citation for case: Stone v. Powell">428 U. S., at 498</a></span> (Burger, C. J., concurring); Oaks, Studying the Exclusionary Rule in Search and Seizure, <span class="citation no-link">37 U. Chi. L. Rev. 665</span>, 709-710 (1970).</p>
</footnote>
<footnote label="17">
<p id="b959-8">See, <em>e. g., Dunaway </em>v. <em>New York, </em><span class="citation multiple-matches"><a href="/c/U.%20S./442/220/">442 U. S. 220</a></span>, 221 (1979) (Stevens, J., concurring); Mertens &amp; Wasserstrom, The Good Faith Exception to the Exclusionary Rule: Deregulating the Police and Derailing the Law, 70 Geo. L. J. 365, 399-401 (1981).</p>
</footnote>
<footnote label="18">
<p id="b959-9"> Limiting the application of the exclusionary sanction may well increase the care with which magistrates scrutinize warrant applications. We doubt that magistrates are more desirous of avoiding the exclusion of evidence obtained pursuant to warrants they have issued than of avoiding invasions of privacy.</p>
<p id="b959-10">Federal magistrates, moreover, are subject to the direct supervision of district courts. They may be removed for “incompeteney, misconduct, neglect of duty, or physical or mental disability.” <span class="citation no-link">28 U. S. C. §631</span>(i). If a magistrate serves merely as a “rubber stamp” for the police or is <page-number citation-index="1" label="918">*918</page-number>unable to exercise mature judgment, closer supervision or removal provides a more effective remedy than the exclusionary rule.</p>
</footnote>
<footnote label="19">
<p id="b960-8"> Our discussion of the deterrent effect of excluding evidence obtained in reasonable reliance on a subsequently invalidated warrant assumes, of course, that the officers properly executed the warrant and searched only those places and for those objects that it was reasonable to believe were covered by the warrant. Cf. <em>Massachusetts </em>v. <em>Sheppard, post, </em>at 989, n. 6 (“[I]t was not unreasonable for the police in this case to rely on the judge’s assurances that the warrant authorized the search they had requested”).</p>
</footnote>
<footnote label="20">
<p id="b961-10"> We emphasize that the standard of reasonableness we adopt is an objective one. Many objections to a good-faith exception assume that the exception will turn on the subjective good faith of individual officers. “Grounding the modification in objective reasonableness, however, retains <page-number citation-index="1" label="920">*920</page-number>the value of the exclusionary rule as an incentive for the law enforcement profession as a whole to conduct themselves in accord with the Fourth Amendment.” <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#261" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 261, n. 15</a></span> (White, J., concurring in judgment); see <em>Dunaway </em>v. <em>New York, </em>442 U. S., at 221 (Stevens, J., concurring). The objective standard we adopt, moreover, requires officers to have a reasonable knowledge of what the law prohibits. <em>United States </em>v. <em>Peltier, </em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#542" aria-description="Citation for case: United States v. Peltier">422 U. S. 531, 542</a></span> (1975). As Professor Jerold Israel has observed:</p>
<blockquote id="b962-7">“The key to the [exclusionary] rule’s effectiveness as a deterrent lies, I believe, in the impetus it has provided to police training programs that make officers aware of the limits imposed by the fourth amendment and emphasize the need to operate within those limits. [An objective good-faith exception] is not likely to result in the elimination of such programs, which are now viewed as an important aspect of police professionalism. Neither is it likely to alter the tenor of those programs; the possibility that illegally obtained evidence may be admitted in borderline cases is unlikely to encourage police instructors to pay less attention to fourth amendment limitations. Finally, [it] should not encourage officers to pay less attention to what they are taught, as the requirement that the officer act in ‘good faith’ is inconsistent with closing one’s mind to the possibility of illegality.” Israel, <em>supra </em>n. 14, at 1412-1413 (footnotes omitted).</blockquote>
</footnote>
<footnote label="21">
<p id="b962-8"> According <em>to </em>the Attorney General’s Task Force on Violent Crime, Final Report (1981), the situation in which an officer relies on a duly authorized warrant</p>
<blockquote id="b962-9">“is a particularly compelling example of good faith. A warrant is a judicial mandate to an officer to conduct a search or make an arrest, and the officer has a sworn duty to carry out its provisions. Accordingly, we believe that <page-number citation-index="1" label="921">*921</page-number>there should be a rule which states that evidence obtained pursuant to and within the scope of a warrant is prima facie the result of good faith on the part of the officer seizing the evidence.” <em>Id., </em>at 55.</blockquote>
</footnote>
<footnote label="22">
<p id="b963-6"> To the extent that Justice Stevens’ conclusions concerning the integrity of the courts, <em>post, </em>at 976-978, rest on a foundation other than his judgment, which we reject, concerning the effects of our decision on the deterrence of police illegality, we find his argument unpersuasive. “Judicial integrity clearly does not mean that the courts must never admit evidence obtained in violation of the Fourth Amendment.” <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#458" aria-description="Citation for case: United States v. Janis">428 U. S. 433, 458, n. 35</a></span> (1976). “While courts, of course, must ever be concerned with preserving the integrity of the judicial process, this concern has limited force as a justification for the exclusion of highly probative evidence.” <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#485" aria-description="Citation for case: Stone v. Powell">428 U. S., at 485</a></span>. Our cases establish that the question whether the use of illegally obtained evidence in judicial proceedings represents judicial participation in a Fourth Amendment violation and offends the integrity of the courts</p>
<blockquote id="b963-7">“is essentially the same as the inquiry into whether exclusion would serve a deterrent purpose. . . . The analysis showing that exclusion in this case has no demonstrated deterrent effect and is unlikely to have any significant such effect shows, by the same reasoning, that the admission of the evidence is unlikely to encourage violations of the Fourth Amendment.” <em>United States </em>v. <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#459" aria-description="Citation for case: United States v. Janis"><em>Janis, supra, </em>at 459, n. 35</a></span>.</blockquote>
<p id="b963-8">Absent unusual circumstances, when a Fourth Amendment violation has occurred because the police have reasonably relied on a warrant issued by a detached and neutral magistrate but ultimately found to be defective, “the <page-number citation-index="1" label="922">*922</page-number>integrity of the courts is not implicated.” <em>Illinois </em>v. <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#259" aria-description="Citation for case: Illinois v. Gates"><em>Gates, supra, </em>at 259, n. 14</a></span> (White, J., concurring in judgment). See <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#485" aria-description="Citation for case: Stone v. Powell">428 U. S., at 485, n. 23</a></span>; <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#540" aria-description="Citation for case: Stone v. Powell"><em>id., </em>at 540</a></span> (White, J., dissenting); <em>United States </em>v. <em>Peltier, </em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#536" aria-description="Citation for case: United States v. Peltier">422 U. S. 531, 536-539</a></span> (1975).</p>
</footnote>
<footnote label="23">
<p id="b964-7"> In <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span>, </em>we eliminated the subjective component of the qualified immunity public officials enjoy in suits seeking damages for alleged deprivations of constitutional rights. The situations are not perfectly analogous, but we also eschew inquiries into the subjective beliefs of law enforcement officers who seize evidence pursuant to a subsequently invalidated warrant. Although we have suggested that, “[o]n occasion, the motive with which the officer conducts an illegal search may have some relevance in determining the propriety of applying the exclusionary rule,” <em>Scott </em>v. <em>United States, </em><span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#139" aria-description="Citation for case: Scott v. United States">436 U. S. 128, 139, n. 13</a></span> (1978), we believe that “sending state and federal courts on an expedition into the minds of police officers would produce a grave and fruitless misallocation of judicial resources.” <em>Massachusetts </em>v. <em>Painten, </em><span class="citation" data-id="9423573"><a href="/opinion/107577/massachusetts-v-painten/#565" aria-description="Citation for case: Massachusetts v. Painten">389 U. S. 560, 565</a></span> (1968) (White, J., dissenting). Accordingly, our good-faith inquiry is confined to the objectively ascertainable question whether a reasonably well trained officer would have known that the search was illegal despite the magistrate’s authorization. In making this determination, all of the circumstances— <page-number citation-index="1" label="923">*923</page-number>including whether the warrant application had previously been rejected by a different magistrate — may be considered.</p>
</footnote>
<footnote label="24">
<p id="b965-8"> References to “officer” throughout this opinion should not be read too narrowly. It is necessary to consider the objective reasonableness, not only of the officers who eventually executed a warrant, but also of the officers who originally obtained it or who provided information material to the probable-cause determination. Nothing in our opinion suggests, for example, that an officer could obtain a warrant on the basis of a “bare bones” affidavit and then rely on colleagues who are ignorant of the circumstances under which the warrant was obtained to conduct the search. See <em>Whiteley </em>v. <em>Warden, </em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#568" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560, 568</a></span> (1971).</p>
</footnote>
<footnote label="25">
<p id="b966-6"> The argument that defendants will lose their incentive to litigate meritorious Fourth Amendment claims as a result of the good-faith exception we adopt today is unpersuasive. Although the exception might discourage presentation of insubstantial suppression motions, the magnitude of the benefit conferred on defendants by a successful motion makes it unlikely that litigation of colorable claims will be substantially diminished.</p>
</footnote>
<footnote label="26">
<p id="b967-7"> It has been suggested, in fact, that “the recognition of a ‘penumbral zone,’ within which an inadvertent mistake would not call for exclusion, . . . will make it less tempting forjudges to bend fourth amendment standards to avoid releasing a possibly dangerous criminal because of a minor and unintentional miscalculation by the police.” Sehroeder, <em>supra </em>n. 14, at 1420-1421 (footnote omitted); see Ashdown, Good Faith, the Exclusionary Remedy, and Rule-Oriented Adjudication in the Criminal Process, <span class="citation no-link">24 Wm. &amp; Mary L. Rev. 335</span>, 383-384 (1983).</p>
</footnote>
</opinion>
```

---
