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

## GROUP: _overhaul2/lake/cases/United States v. Reddick.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Reddick
type: case
citation: "900 F.3d 636 (2018)"
parallel_cite: ""
neutral_cite: ""
court: 5th Cir.
court_level: coa
circuit: ca5
year: 2018
date_decided: 2018-08-17
docket: 17-41116
authority_weight: "Binding in-circuit — 5th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4527853/united-states-v-henry-reddick/"
  cluster_id: 4527853
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Reddick
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Private and Foreign Searches]]"
    role: "Key — hash-match split (5th Cir.)"
related:
  - "[[Fourth Amendment Framework]]"
  - "[[United States v. Jacobsen]]"
  - "[[Carpenter v. United States]]"
  - "[[Riley v. California]]"
tags:
  - case
  - fourth-amendment
  - private-search-doctrine
  - hash-value
  - child-pornography
  - digital-privacy
  - fifth-circuit
holding: "Under the private-search doctrine, the government does not conduct a Fourth Amendment search when it merely receives and reviews the results of a search already performed by a private party, so where a private company hash-matched Reddick's uploaded files to known child-pornography images and reported them, the officer's warrantless viewing of the flagged images exposed nothing beyond what the private search had already revealed and did not violate the Fourth Amendment."
aliases:
  - United States v. Reddick
  - "United States v. Reddick (5th Cir. 2018)"
---

# United States v. Reddick

*900 F.3d 636 (5th Cir. 2018)* (No. 17-41116) · U.S. Court of Appeals for the Fifth Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4527853 → lead opinion 4305106 (Ho, J.; 900 F.3d 636, decided 2018-08-17); Rule quote string-matched to the CL opinion text 2026-07-07 (reporter page-label *637). S9 promotes. -->

## Background
Henry Reddick uploaded files to Microsoft's cloud-storage service. Microsoft's automated systems computed the "hash values" of those files — short, distinctive alphanumeric identifiers derived from a file's contents — and compared them against a database of hash values of known child-pornography images. When the values matched, Microsoft reported the files to the National Center for Missing and Exploited Children, which forwarded the report to law enforcement. Detective Ilse then opened and viewed the flagged image files without first obtaining a warrant, confirmed they were child pornography, and that evidence supported the ensuing prosecution. Reddick moved to suppress, arguing the warrantless viewing was an unlawful search; the district court denied the motion, and he appealed.

## Issue
Whether a law-enforcement officer conducts a Fourth Amendment search when, without a warrant, he opens and views digital files whose hash values a private party has already matched against known child-pornography images and reported to authorities.

## Rule
The Fourth Amendment restrains only government action, so when a private party has already searched an item the government does not conduct a new search by examining what that private search already exposed — it acquires no information as to which the owner's expectation of privacy remained intact. Applying that private-search doctrine, the panel held: "Under the private search doctrine, the Fourth Amendment is not implicated where the government does not conduct the search itself, but only receives and utilizes information uncovered by a search conducted by a private party." — 900 F.3d at 637. ^pin-637

## Application
Microsoft's automated hash-value comparison had already identified Reddick's files as matching known child pornography and had frustrated whatever expectation of privacy he retained in them before any officer became involved — a hash match identifies a file with near-certainty. When Detective Ilse opened the files, he learned nothing that the private hash-match had not already established, so his viewing worked no additional intrusion on any privacy interest that survived, and the Fourth Amendment was not implicated. The court therefore affirmed on this broader private-search ground rather than the narrower rationale the district court had invoked.

## Conclusion
**Affirmed.** James C. Ho, Circuit Judge, wrote for the panel.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Reddick* applies the *[[United States v. Jacobsen|Jacobsen]]* private-search doctrine to automated hash-value matching: because a private company's hash comparison exposes a file's status before any officer looks, the officer's confirmatory viewing adds nothing the Fourth Amendment protects. Note the live cross-circuit tension over how far the doctrine reaches when no human at the private company ever viewed the specific file — the Ninth Circuit has diverged on that point — so teach *Reddick* as the Fifth Circuit's confirmatory-viewing rule, not a settled national standard.

## Appears on
- [[Private and Foreign Searches]] — *Key — hash-match split (5th Cir.)*

## Sources
- [*United States v. Reddick*, 900 F.3d 636 (5th Cir. 2018)](https://www.courtlistener.com/opinion/4527853/united-states-v-henry-reddick/) — pinpoint: 637 (private-search-doctrine holding; Ho, J.; the CL opinion text carries the reporter page-label *637). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0d0e127be61c7fa2", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Reddick"}, "payload": {"all": [{"cite": "900 F.3d 636", "page": "636", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "900"}], "display": "900 F.3d 636", "official": {"cite": "900 F.3d 636", "page": "636", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "900"}, "official_selection_present": true, "record_id": "United States v. Reddick"}}
{"assertion_id": "725782814889d891", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Reddick"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Reddick", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Reddick

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Reddick",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Henry Reddick",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee v. Henry Franklin REDDICK, Defendant-Appellant",
    "input_case_name": "United States v. Reddick",
    "court": "5th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca5",
    "state": null,
    "date_decided": "2018-08-17",
    "year": 2018,
    "docket": "17-41116",
    "cluster_id": 4527853,
    "lead_opinion_id": 4305106,
    "sibling_ids": [],
    "absolute_url": "/opinion/4527853/united-states-v-henry-reddick/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "900 F.3d 636",
      "volume": "900",
      "reporter": "F.3d",
      "page": "636",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "900 F.3d 636",
        "volume": "900",
        "reporter": "F.3d",
        "page": "636",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "900 F.3d 636",
    "official_selection": {
      "court_class": "coa",
      "selected": "900 F.3d 636",
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
    "date_created": "2026-07-07T01:40:32Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:40:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:40:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:40:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:40:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-reddick--4527853",
      "to_record_id": "United States v. Reddick",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Reddick

```
     Case: 17-41116    Document: 00514605839        Page: 1   Date Filed: 08/17/2018




        IN THE UNITED STATES COURT OF APPEALS
                 FOR THE FIFTH CIRCUIT
                                                                     United States Court of Appeals
                                                                              Fifth Circuit


                                    No. 17-41116
                                                                            FILED
                                                                      August 17, 2018
                                                                       Lyle W. Cayce
UNITED STATES OF AMERICA,                                                   Clerk

             Plaintiff - Appellee

v.

HENRY FRANKLIN REDDICK,

             Defendant - Appellant




                Appeal from the United States District Court
                     for the Southern District of Texas


Before KING, SOUTHWICK, and HO, Circuit Judges.
JAMES C. HO, Circuit Judge:
      Private businesses and police investigators rely regularly on “hash
values” to fight the online distribution of child pornography. Hash values are
short, distinctive identifiers that enable computer users to quickly compare the
contents of one file to another. They allow investigators to identify suspect
material from enormous masses of online data, through the use of specialized
software programs—and to do so rapidly and automatically, without the need
for human searchers.
      Hash values have thus become a powerful tool for combating the online
distribution of unlawful aberrant content.         The question in this appeal is
whether and when the use of hash values by law enforcement is consistent with
    Case: 17-41116    Document: 00514605839     Page: 2   Date Filed: 08/17/2018



                                 No. 17-41116
the Fourth Amendment. For the Fourth Amendment concerns not efficiency,
but the liberty of the people “to be secure in their persons, houses, papers, and
effects, against unreasonable searches and seizures.” There is no precedent in
our circuit concerning the validity of these investigative tools under the Fourth
Amendment, and to our knowledge no other circuit has confronted the precise
question before us.   This case therefore presents an opportunity to apply
established Fourth Amendment principles in this new context.
      One touchstone of our Fourth Amendment jurisprudence is that the
Constitution secures the right of the people against unreasonable searches and
seizures conducted by the government—not searches and seizures conducted
by private parties. Under the private search doctrine, the Fourth Amendment
is not implicated where the government does not conduct the search itself, but
only receives and utilizes information uncovered by a search conducted by a
private party.
      The private search doctrine decides this case.        A private company
determined that the hash values of files uploaded by Mr. Reddick corresponded
to the hash values of known child pornography images. The company then
passed this information on to law enforcement. This qualifies as a “private
search” for Fourth Amendment purposes. And the government’s subsequent
law enforcement actions in reviewing the images did not effect an intrusion on
Mr. Reddick’s privacy that he did not already experience as a result of the
private search. Accordingly, we affirm the judgment of the district court.
                                       I.
      In technical terms, a hash value is “an algorithmic calculation that yields
an alphanumeric value for a file.” United States v. Stevenson, 727 F.3d 826,
828 (8th Cir. 2013). More simply, a hash value is a string of characters
obtained by processing the contents of a given computer file and assigning a
sequence of numbers and letters that correspond to the file’s contents. In the
                                       2
    Case: 17-41116    Document: 00514605839     Page: 3   Date Filed: 08/17/2018



                                 No. 17-41116
words of one commentator, “[t]he concept behind hashing is quite elegant: take
a large amount of data, such as a file or all the bits on a hard drive, and use a
complex mathematical algorithm to generate a relatively compact numerical
identifier (the hash value) unique to that data.” Richard P. Salgado, Fourth
Amendment Search and the Power of the Hash, 119 Harv. L. Rev. F. 38, 38
(2005).
      Hash values are regularly used to compare the contents of two files
against each other.    “If two nonidentical files are inputted into the hash
program, the computer will output different results. If the two identical files
are inputted, however, the hash function will generate identical output.” Orin
S. Kerr, Searches and Seizures in a Digital World, 119 Harv. L. Rev. 531, 541
(2005). Hash values have been used to fight child pornography distribution,
by comparing the hash values of suspect files against a list of the hash values
of known child pornography images currently in circulation. This process
allows potential child pornography images to be identified rapidly, without the
need to involve human investigators at every stage.
                                       II.
      Henry Reddick uploaded digital image files to Microsoft SkyDrive, a
cloud hosting service.     SkyDrive uses a program called PhotoDNA to
automatically scan the hash values of user-uploaded files and compare them
against the hash values of known images of child pornography.             When
PhotoDNA detects a match between the hash value of a user-uploaded file and
a known child pornography hash value, it creates a “CyberTip” and sends the
file—along with the uploader’s IP address information—to the National Center
for Missing and Exploited Children (NCMEC).
      In early 2015, Microsoft sent CyberTips to NCMEC based on the hash
values of files that Reddick had uploaded to SkyDrive. Based on location data
derived from the IP address information accompanying the files, NCMEC
                                       3
    Case: 17-41116      Document: 00514605839     Page: 4    Date Filed: 08/17/2018



                                  No. 17-41116
subsequently forwarded the CyberTips to the Corpus Christi Police
Department.     Upon receiving the CyberTips, police detective Michael Ilse
opened each of the suspect files and confirmed that each contained child
pornography. Shortly thereafter, Detective Ilse applied for and received a
warrant to search Reddick’s home and seize his computer and related
materials. This search uncovered additional evidence of child pornography in
Reddick’s possession.
      Reddick was indicted for possession of child pornography in violation of
18 U.S.C. § 2252(a)(2) and (b)(1). Following his indictment, Reddick initially
pled not guilty and moved to suppress all the evidence of child pornography.
He alleged that Detective Ilse’s warrantless opening of the files associated with
the CyberTips was an unlawful search. He further claimed that any evidence
of child pornography found in his home should be suppressed under the
exclusionary rule, since the initial review of the suspect files was improper.
      The district court denied his motion. Reddick subsequently pled guilty,
while retaining the right to appeal the denial of his suppression motion. In
denying Reddick’s motion, the district court “assume[d] without deciding that
Officer Ilse’s viewing of the file images . . . invaded a constitutional expectation
of privacy, exceeded the scope of Microsoft Skydrive’s hash value search, and
did not fall into any exception to the warrant requirement.”            The court
nevertheless concluded that “the evidence here support[ed] the good faith
exception to the exclusionary rule.”         Accordingly, the court found no
justification to suppress the evidence of child pornography found in Reddick’s
home.
      As a general rule, “[w]e may affirm the district court’s ruling on a motion
to suppress ‘based on any rationale supported by the record.’” United States v.
Wise, 877 F.3d 209, 215 (5th Cir. 2017) (citation omitted). Consistent with this
rule, we affirm the denial of the motion to suppress on a ground broader than
                                         4
     Case: 17-41116       Document: 00514605839          Page: 5     Date Filed: 08/17/2018



                                       No. 17-41116
the one invoked by the district court—namely, that under the private search
doctrine, Officer Ilse’s viewing of the file images did not violate the Fourth
Amendment.
                                             III.
       Under the private search doctrine, “the critical inquiry under the Fourth
Amendment is whether the authorities obtained information with respect to
which the defendant’s expectation of privacy has not already been frustrated.”
United States v. Runyan, 275 F.3d 449, 461 (5th Cir. 2001). The question
presented here, then, is whether, by the time Detective Ilse viewed the suspect
image files, Reddick’s expectation of privacy in his computer files had already
been thwarted by a private third party. 1
       The Supreme Court’s decision in United States v. Jacobsen, 466 U.S. 109
(1984), guides our analysis.          In Jacobsen, employees of Federal Express
observed that one of its packages had been damaged in transit. They opened
the package and discovered a white powder.                  In response, the employees
contacted the Drug Enforcement Administration.                     DEA agents conducted
chemical field tests on the white powder and determined that the power was
cocaine. The government then used the test results to obtain a warrant and
arrest the package’s intended recipients, who subsequently challenged the
government’s actions as unconstitutional.
       The Court held that the agents’ actions did not violate the Fourth
Amendment. “Once frustration of the original expectation of privacy occurs,
the Fourth Amendment does not prohibit governmental use of the now-
nonprivate information.” Id. at 117. Any expectation of privacy the recipients


       1  We assume without deciding that Reddick indeed had a legitimate expectation of
privacy in the computer files at issue. As the district court correctly noted, “the most useful
evidence on which to make the determination” of whether Reddick’s expectation of privacy
was reasonable—“the end user agreement governing Reddick’s use of Microsoft Skydrive”—
is not in the record.
                                              5
    Case: 17-41116    Document: 00514605839     Page: 6   Date Filed: 08/17/2018



                                No. 17-41116
might have had in the package’s contents was abrogated when the Federal
Express employees opened and searched the package and discovered the white
powder. The government’s subsequent use of that information—its test to
discern the powder’s chemical composition—infringed no expectation of
privacy that had not already been infringed.
      So too here.   When Reddick uploaded files to SkyDrive, Microsoft’s
PhotoDNA program automatically reviewed the hash values of those files and
compared them against an existing database of known child pornography hash
values. In other words, his “package” (that is, his set of computer files) was
inspected and deemed suspicious by a private actor. Accordingly, whatever
expectation of privacy Reddick might have had in the hash values of his files
was frustrated by Microsoft’s private search.
      When Detective Ilse first received Reddick’s files, he already knew that
their hash values matched the hash values of child pornography images known
to NCMEC. As our court has previously noted, hash value comparison “allows
law enforcement to identify child pornography with almost absolute certainty,”
since hash values are “specific to the makeup of a particular image’s data.”
United States v. Larman, 547 F. App’x 475, 477 (5th Cir. 2013) (unpublished).
See also United States v. Sosa-Pintor, 2018 WL 3409657, at *1 (5th Cir. July
11, 2018) (unpublished) (describing a file’s hash value as its “unique digital
fingerprint”).
      Accordingly, when Detective Ilse opened the files, there was no
“significant expansion of the search that had been conducted previously by a
private party” sufficient to constitute “a separate search.” Walter v. United
States, 447 U.S. 649, 657 (1980). His visual review of the suspect images—a
step which merely dispelled any residual doubt about the contents of the files—
was akin to the government agents’ decision to conduct chemical tests on the
white powder in Jacobsen. “A chemical test that merely discloses whether or
                                      6
    Case: 17-41116   Document: 00514605839     Page: 7   Date Filed: 08/17/2018



                                No. 17-41116
not a particular substance is cocaine does not compromise any legitimate
interest in privacy.” 466 U.S. at 123. This principle readily applies here—
opening the file merely confirmed that the flagged file was indeed child
pornography, as suspected. As in Jacobsen, “the suspicious nature of the
material made it virtually certain that the substance tested was in fact
contraband.” Id. at 125.
      Significantly, there is no allegation that Detective Ilse conducted a
search of any of Mr. Reddick’s files other than those flagged as child
pornography.   Contrast a Tenth Circuit decision authored by then-Judge
Gorsuch. See United States v. Ackerman, 831 F.3d 1292 (10th Cir. 2016). In
Ackerman, an investigator conducted a search of an email and three
attachments whose hash values did not correspond to known child
pornography images. 831 F.3d at 1306. The Tenth Circuit reversed the district
court’s denial of a motion to suppress accordingly. Id. at 1309. Here, by
contrast, Detective Ilse reviewed only those files whose hash values
corresponded to the hash values of known child pornography images, as
ascertained by the PhotoDNA program. So his review did not sweep in any
“(presumptively) private correspondence that could have contained much
besides potential contraband.” Id. at 1307.
                                    ***
      The exact issues presented by this case may be novel. But the governing
constitutional principles set forth by the Supreme Court are not.          The
government effectively learned nothing from Detective Ilse’s viewing of the
files that it had not already learned from the private search. Accordingly,
under the private search doctrine, the government did not violate Reddick’s
Fourth Amendment rights. We affirm the judgment of the district court.




                                      7

```

---

## GROUP: _overhaul2/lake/cases/United States v. Rideau.json  (`lake-record`, 6 assertions)

### content_page

```
---
title: "United States v. Rideau"
type: case
citation: "969 F.2d 1572 (1992)"
parallel_cite: ""
neutral_cite: "1992 U.S. App. LEXIS 18693; 1992 WL 195842"
court: "U.S. Court of Appeals, 5th Circuit"
court_level: coa
circuit: 5th
year: 1992
date_decided: 1992-08-14
docket: ""
authority_weight: "Binding in-circuit — 5th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 1992-08-14
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Rideau
  varies_by_point: false
  scope_note: "Good law; en banc. Public-welfare/community-caretaking function applied to an impaired person in the roadway."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/587275/united-states-v-izeal-rideau-jr/"
  cluster_id: 587275
  opinion_id: 587275
  identity_checked: false
homes:
  - page: "[[Community Caretaking]]"
    role: "Key — Progeny"
related: ["[[United States v. Garner]]", "[[Cady v. Dombrowski]]", "[[Terry v. Ohio]]", "[[Adams v. Williams]]", "[[Caniglia v. Strom]]"]
aliases: ["United States v. Izeal Rideau, Jr.", "United States v. Rideau (5th Cir. 1992)"]
tags: ["case", "fourth-amendment", "community-caretaking", "public-welfare", "investigative-detention", "persons-in-public", "fifth-circuit"]
holding: "Police serve a public-welfare/community-caretaking function by removing apparently intoxicated people from the public streets, and an officer is warranted in stopping to check on the condition of an impaired person standing in the roadway; on these facts the en banc court held the stop and protective patdown reasonable under the Fourth Amendment."
lake:
  record_id: United States v. Rideau
  status: under_review
  projected_at: 2026-07-09
---

# United States v. Rideau

*969 F.2d 1572 (5th Cir. 1992) (en banc)* · U.S. Court of Appeals, 5th Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Around 10:30 p.m. in a high-crime area of Beaumont, Texas, Officer Ellison saw a man wearing dark clothing standing in the road. Ellison flashed his bright lights to encourage the man to leave the street; the man turned, stepped toward the shoulder, and stumbled, leading Ellison to suspect he was drunk. Ellison pulled over and approached to investigate and check on him. When Ellison asked the man's name, he appeared nervous, did not answer, and began to back away; Ellison closed the gap and patted the man's outer pants pocket, where he felt a firearm. The man — Izeal Rideau, a convicted felon — was arrested and charged with being a felon in possession (18 U.S.C. § 922(g)(1)). A panel had reversed his conviction, and the Fifth Circuit reheard the case [[Reading and Citing Cases#en-banc|en banc]].

## Issue
Whether an officer acted reasonably under the Fourth Amendment in stopping an apparently intoxicated man standing in a roadway at night to check on his condition, and then conducting a limited protective patdown when the man backed away.

## Rule
Police actions in caring for an impaired person on the public streets serve a recognized public-welfare/community-caretaking function. "Police have long served the public welfare by removing intoxicated people from the public streets, where they pose a hazard to themselves and others." — 969 F.2d at 1574 (citing *Powell v. Texas* and *Cady v. Dombrowski*'s "community caretaking functions"). ^pin-1574

Accordingly, "Officer Ellison was warranted in stopping to investigate the situation and check on the man's condition." — [*Id.*](https://www.courtlistener.com/opinion/587275/united-states-v-izeal-rideau-jr/#:~:text=Officer%20Ellison%20was%20warranted%20in) ^pin-1574a

A lawful detention is not a license to frisk, but the protective patdown here was supported by specific and articulable facts: "A reasonably prudent man in Ellison's situation could have believed that his safety and that of his partner was in danger." — [*Id.*](https://www.courtlistener.com/opinion/587275/united-states-v-izeal-rideau-jr/#:~:text=A%20reasonably%20prudent%20man%20in%20Ellison%27s) ^pin-1574b

The court added that "police officers must have specific and articulable facts indicating that their safety is in danger to justify a patdown." — 969 F.2d at 1576. ^pin-1576

## Application
Ellison was justified in stopping because Rideau, apparently intoxicated and standing in the roadway at night, presented both a possible public-intoxication offense and a public-welfare concern that warranted checking on his condition. The subsequent patdown was supported by specific and articulable facts: after the lawful detention, in a high-crime area where weapons were common, Rideau backed away when asked his name — conduct a reasonably prudent officer could read as gaining room to draw a weapon. The single, spontaneous touch of the front pants pocket was a limited and tailored response to that safety concern.

## Conclusion
The [[Reading and Citing Cases#en-banc|en banc]] court held the officer's actions reasonable under the Fourth Amendment and affirmed the denial of suppression and the conviction, reversing the panel.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 5th Cir.** (en banc).
- *Rideau* is a leading progeny illustration of the public-welfare/community-caretaking function applied to a **person** (not a vehicle): it grounds the caretaking stop in [[Cady v. Dombrowski]] and is cited by [[United States v. Garner]] (10th Cir.) for extending a caretaking detention based on an apparently impaired person's behavior.
- [[Caniglia v. Strom]] (2021) barred a *freestanding* community-caretaking entry into the **home**; that home-limited holding does not disturb *Rideau*'s rule for an impaired person in public.

## Appears on
- [[Community Caretaking]] — *Key — Progeny*

## Sources
- *United States v. Rideau*, 969 F.2d 1572 (5th Cir. 1992) (en banc) — https://www.courtlistener.com/opinion/587275/united-states-v-izeal-rideau-jr/ — pinpoints: 1574, 1576.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "df68d26f7416959c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Rideau"}, "payload": {"all": [{"cite": "969 F.2d 1572", "page": "1572", "reporter": "F.2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "969"}, {"cite": "1992 U.S. App. LEXIS 18693", "page": "18693", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1992"}, {"cite": "1992 WL 195842", "page": "195842", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "1992"}], "display": "969 F.2d 1572", "official": {"cite": "969 F.2d 1572", "page": "1572", "reporter": "F.2d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "969"}, "official_selection_present": true, "record_id": "United States v. Rideau"}}
{"assertion_id": "1f257266d9fe8e5f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1574b", "record_id": "United States v. Rideau"}, "payload": {"fragment": "#:~:text=A%20reasonably%20prudent%20man%20in%20Ellison%27s", "page": null, "pin_id": "pin-1574b", "pinpoint_status": "slip-only", "quote": "A reasonably prudent man in Ellison's situation could have believed that his safety and that of his partner was in danger.", "quote_fidelity": "matched", "record_id": "United States v. Rideau", "star_marker": null}}
{"assertion_id": "5a93ef5b99f8ac3c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1576", "record_id": "United States v. Rideau"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1576", "pinpoint_status": "slip-only", "quote": "police officers must have specific and articulable facts indicating that their safety is in danger to justify a patdown.", "quote_fidelity": "matched", "record_id": "United States v. Rideau", "star_marker": null}}
{"assertion_id": "6a6030212e6c9543", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1574a", "record_id": "United States v. Rideau"}, "payload": {"fragment": "#:~:text=Officer%20Ellison%20was%20warranted%20in", "page": null, "pin_id": "pin-1574a", "pinpoint_status": "slip-only", "quote": "Officer Ellison was warranted in stopping to investigate the situation and check on the man's condition.", "quote_fidelity": "matched", "record_id": "United States v. Rideau", "star_marker": null}}
{"assertion_id": "6d3b3bfd9172305e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1574", "record_id": "United States v. Rideau"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1574", "pinpoint_status": "slip-only", "quote": "--- # United States v. Rideau *969 F.2d 1572 (5th Cir. 1992) (en banc)* · U.S. Court of Appeals, 5th Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Around 10:30 p.m. in a high-crime area of Beaumont, Texas, Officer Ellison saw a man wearing dark clothing standing in the road. Ellison flashed his bright lights to encourage the man to leave the street; the man turned, stepped toward the shoulder, and stumbled, leading Ellison to suspect he was drunk. Ellison pulled over and approached to investigate and check on him. When Ellison asked the man's name, he appeared nervous, did not answer, and began to back away; Ellison closed the gap and patted the man's outer pants pocket, where he felt a firearm. The man — Izeal Rideau, a convicted felon — was arrested and charged with being a felon in possession (18 U.S.C. § 922(g)(1)). A panel had reversed his conviction, and the Fifth Circuit reheard the case en banc. ## Issue Whether an officer acted reasonably under the Fourth Amendment in stopping an apparently intoxicated man standing in a roadway at night to check on his condition, and then conducting a limited protective patdown when the man backed away. ## Rule Police actions in caring for an impaired person on the public streets serve a recognized public-welfare/community-caretaking function.", "quote_fidelity": "mismatch", "record_id": "United States v. Rideau", "star_marker": null}}
{"assertion_id": "d062fd7ec8ca842e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Rideau"}, "payload": {"as_of_content": "1992-08-14", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Rideau", "scope_note": "Good law; en banc. Public-welfare/community-caretaking function applied to an impaired person in the roadway.", "varies_by_point": false}}
```

### lake record — United States v. Rideau

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Rideau",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Izeal Rideau, Jr.",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Izeal RIDEAU, Jr., Defendant-Appellant",
    "input_case_name": "United States v. Rideau",
    "court": "U.S. Court of Appeals, 5th Circuit",
    "court_id": "ca5",
    "court_level": "coa",
    "circuit": "5th",
    "state": null,
    "date_decided": "1992-08-14",
    "year": 1992,
    "docket": null,
    "cluster_id": 587275,
    "lead_opinion_id": 587275,
    "sibling_ids": [
      587275,
      9483168,
      9483169
    ],
    "absolute_url": "/opinion/587275/united-states-v-izeal-rideau-jr/",
    "identity_method": "pending",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 572438,
        "score": 20,
        "case_name": "United States v. Izeal Rideau, Jr."
      }
    ],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "969 F.2d 1572",
      "volume": "969",
      "reporter": "F.2d",
      "page": "1572",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1992 U.S. App. LEXIS 18693",
        "volume": "1992",
        "reporter": "U.S. App. LEXIS",
        "page": "18693",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1992 WL 195842",
        "volume": "1992",
        "reporter": "WL",
        "page": "195842",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "969 F.2d 1572",
        "volume": "969",
        "reporter": "F.2d",
        "page": "1572",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1992 U.S. App. LEXIS 18693",
        "volume": "1992",
        "reporter": "U.S. App. LEXIS",
        "page": "18693",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1992 WL 195842",
        "volume": "1992",
        "reporter": "WL",
        "page": "195842",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "969 F.2d 1572",
    "official_selection": {
      "court_class": "coa",
      "selected": "969 F.2d 1572",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1574",
      "page": null,
      "quote": "--- # United States v. Rideau *969 F.2d 1572 (5th Cir. 1992) (en banc)* \u00b7 U.S. Court of Appeals, 5th Circuit \u00b7 **Binding in-circuit \u2014 5th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Around 10:30 p.m. in a high-crime area of Beaumont, Texas, Officer Ellison saw a man wearing dark clothing standing in the road. Ellison flashed his bright lights to encourage the man to leave the street; the man turned, stepped toward the shoulder, and stumbled, leading Ellison to suspect he was drunk. Ellison pulled over and approached to investigate and check on him. When Ellison asked the man's name, he appeared nervous, did not answer, and began to back away; Ellison closed the gap and patted the man's outer pants pocket, where he felt a firearm. The man \u2014 Izeal Rideau, a convicted felon \u2014 was arrested and charged with being a felon in possession (18 U.S.C. \u00a7 922(g)(1)). A panel had reversed his conviction, and the Fifth Circuit reheard the case en banc. ## Issue Whether an officer acted reasonably under the Fourth Amendment in stopping an apparently intoxicated man standing in a roadway at night to check on his condition, and then conducting a limited protective patdown when the man backed away. ## Rule Police actions in caring for an impaired person on the public streets serve a recognized public-welfare/community-caretaking function.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1574a",
      "page": null,
      "quote": "Officer Ellison was warranted in stopping to investigate the situation and check on the man's condition.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 13804,
      "fragment": "#:~:text=Officer%20Ellison%20was%20warranted%20in",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-1574b",
      "page": null,
      "quote": "A reasonably prudent man in Ellison's situation could have believed that his safety and that of his partner was in danger.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 14107,
      "fragment": "#:~:text=A%20reasonably%20prudent%20man%20in%20Ellison%27s",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-1576",
      "page": null,
      "quote": "police officers must have specific and articulable facts indicating that their safety is in danger to justify a patdown.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 23241
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1992-08-14",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Rideau",
    "varies_by_point": false,
    "scope_note": "Good law; en banc. Public-welfare/community-caretaking function applied to an impaired person in the roadway.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Lionel Alexander v. City of Round Rock",
          "cluster_id": 4384027,
          "cite": [
            "854 F.3d 298",
            "2017 U.S. App. LEXIS 6692",
            "2017 WL 1393702"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tosh Toussaint",
          "cluster_id": 4259133,
          "cite": [
            "838 F.3d 503",
            "2016 U.S. App. LEXIS 17357",
            "2016 WL 5314862"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Marcus Wadley",
          "cluster_id": 717593,
          "cite": [
            "83 F.3d 108",
            "1996 WL 226785"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Rene Ponce",
          "cluster_id": 656578,
          "cite": [
            "8 F.3d 989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Earl Sanders",
          "cluster_id": 607884,
          "cite": [
            "994 F.2d 200",
            "1993 U.S. App. LEXIS 14818",
            "1993 WL 211684"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Peterson v. City of Fort Worth, Tex.",
          "cluster_id": 69197,
          "cite": [
            "588 F.3d 838",
            "2009 U.S. App. LEXIS 25183",
            "2009 WL 3818826"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wright v. State",
          "cluster_id": 1870455,
          "cite": [
            "7 S.W.3d 148",
            "1999 Tex. Crim. App. LEXIS 146",
            "1999 WL 1178566"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 2087727,
          "cite": [
            "745 A.2d 856",
            "1999 Del. LEXIS 445",
            "1999 WL 1259008"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michelletti",
          "cluster_id": 6205,
          "cite": [
            "13 F.3d 838",
            "1994 U.S. App. LEXIS 1229",
            "1994 WL 19106"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Shiffermiller",
          "cluster_id": 4592777,
          "cite": [
            "302 Neb. 245",
            "922 N.W.2d 763"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bradley Lee Winters v. Robert Adams and Craig Prahm",
          "cluster_id": 773752,
          "cite": [
            "254 F.3d 758",
            "2001 U.S. App. LEXIS 14157",
            "2001 WL 704426"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lizette Vargas v. City of Philadelphia",
          "cluster_id": 2794598,
          "cite": [
            "783 F.3d 962",
            "2015 U.S. App. LEXIS 6331",
            "2015 WL 1741504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Macias v. Raul A. (Unknown), Badge No. 153",
          "cluster_id": 6480,
          "cite": [
            "23 F.3d 94",
            "1994 U.S. App. LEXIS 14792",
            "1994 WL 232885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Klare v. State",
          "cluster_id": 2335254,
          "cite": [
            "76 S.W.3d 68",
            "2002 WL 369940"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Roch",
          "cluster_id": 5959,
          "cite": [
            "5 F.3d 894",
            "1993 U.S. App. LEXIS 27282",
            "1993 WL 413854"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Guy",
          "cluster_id": 1251064,
          "cite": [
            "492 N.W.2d 311",
            "172 Wis. 2d 86",
            "1992 Wisc. LEXIS 763"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Jeffrey Dana Kurth",
          "cluster_id": 4472335,
          "cite": [
            "813 N.W.2d 270",
            "2012 WL 1648253",
            "2012 Iowa Sup. LEXIS 47"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Regon Hill",
          "cluster_id": 2676368,
          "cite": [
            "752 F.3d 1029",
            "2014 WL 2219064",
            "2014 U.S. App. LEXIS 9960"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Terry Lee Coffman",
          "cluster_id": 4509998,
          "cite": [
            "914 N.W.2d 240"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth D. Evans",
          "cluster_id": 607901,
          "cite": [
            "994 F.2d 317",
            "1993 WL 143866"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fontenot v. Cormier",
          "cluster_id": 7279,
          "cite": [
            "56 F.3d 669",
            "1995 U.S. App. LEXIS 15158",
            "1995 WL 366232"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Eleanor Keller v. Attala County",
          "cluster_id": 4728903,
          "cite": [
            "952 F.3d 216"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alvarez",
          "cluster_id": 6043,
          "cite": [
            "6 F.3d 287",
            "1993 WL 426048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. State",
          "cluster_id": 1448073,
          "cite": [
            "854 P.2d 688",
            "1993 Wyo. LEXIS 105",
            "1993 WL 195796"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alvarez",
          "cluster_id": 6623468,
          "cite": [
            "40 F.4th 339"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salazar v. State",
          "cluster_id": 1528589,
          "cite": [
            "893 S.W.2d 138",
            "1995 Tex. App. LEXIS 65",
            "1995 WL 19359"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas",
          "cluster_id": 4883758,
          "cite": [
            "997 F.3d 603"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(587275 OR 9483168 OR 9483169) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca5)",
        "reviewed": 21,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 5,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 21,
        "triage_read": 5,
        "triage_snippet_classified": 16
      },
      "lane2_top_cited": {
        "query": "cites:(587275 OR 9483168 OR 9483169)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00JnM9NDYxNjUxNyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28587275+OR+9483168+OR+9483169%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(587275 OR 9483168 OR 9483169)",
        "reviewed": 2,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 2,
        "triage_read": 0,
        "triage_snippet_classified": 2
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(587275 OR 9483168 OR 9483169)",
    "indexed_citing_opinions": 69,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 587275,
        "count": 47,
        "count_source": "search"
      },
      {
        "opinion_id": 9483168,
        "count": 26,
        "count_source": "search"
      },
      {
        "opinion_id": 9483169,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 157,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-rideau.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU4OTQ3Nzkmcz00NTA5OTk4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28587275+OR+9483168+OR+9483169%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 587275,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 107750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 111477,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 112239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 112384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 1122661,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 1187451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 532013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 545167,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 1141153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 2290134,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 8994043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9090740,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9423233,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9423752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9424935,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9427853,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9431933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9475728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9531694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9552492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 532013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 551302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 557811,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 572438,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9423752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9424935,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9425411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9427002,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9427183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9430099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9431641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9431933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9475728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9842054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9883102,
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
    "date_created": "2026-07-06T02:28:43Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:29:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:29:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:32:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:29:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Rideau

```
<p class="case_cite"><span class="citation" data-id="9483168"><a href="/opinion/587275/united-states-v-izeal-rideau-jr/" aria-description="Citation for case: United States v. Izeal Rideau, Jr.">969 F.2d 1572</a></span></p>
    <p class="parties">UNITED STATES of America, Plaintiff-Appellee,<br>v.<br>Izeal RIDEAU, Jr., Defendant-Appellant.</p>
    <p class="docket">No. 91-4172.</p>
    <p class="court">United States Court of Appeals,<br>Fifth Circuit.</p>
    <p class="date">Aug. 14, 1992.</p>
    <div class="prelims">
      <p class="indent">Donald E. Sample, Beaumont, Tex.  (Court-appointed), for defendant-appellant.</p>
      <p class="indent">Paul Naman, Kerry M. Klintworth, Asst. U.S. Attys., Bob Wortham, U.S. Atty., Beaumont, Tex., for plaintiff-appellee.</p>
      <p class="indent">Appeal from the United States District Court for the Eastern District of Texas.</p>
      <p class="indent">Before POLITZ, Chief Judge, GOLDBERG, KING, GARWOOD, JOLLY, HIGGINBOTHAM, DAVIS, JONES, SMITH, DUHE, WIENER, BARKSDALE, EMILIO M. GARZA, DeMOSS, Circuit Judges.</p>
      <p class="indent">PATRICK E. HIGGINBOTHAM, Circuit Judge:</p>
    </div>
    <div class="num" id="p1">
      <span class="num">1</span>
      <p class="indent">This case requires us to consider the reasonableness of a police officer's actions in an encounter with a person he suspected was intoxicated, standing in the road, at night, in a high crime area.   A panel of this court held that the officer violated the Fourth Amendment when he reached out and touched the pants pocket of the individual and discovered a gun.   We granted rehearing en banc, and now hold that the officer's actions were reasonable under the Fourth Amendment.</p>
    </div>
    <p>I.</p>
    <div class="num" id="p2">
      <span class="num">2</span>
      <p class="indent">At about 10:30 one night in July of 1989,<a class="footnote" href="#fn1" id="fn1_ref">1</a> police officer Jimmy Ellison and his partner were driving toward the intersection of Bonham Street and Martin Luther King Boulevard, a high crime area in Beaumont, Texas, where people often carried weapons and transacted drug deals on the street, and where public drunkenness was a recurrent problem.   As he drove up Bonham Street, officer Ellison saw a man wearing dark clothing standing in the road.   Ellison flashed his bright lights to see the man better and to encourage him to get out of the street.   The man turned to step out of the roadway and stumbled as he moved toward the shoulder.   Ellison suspected that he was drunk.   He pulled over, got out of his car, and approached the man to investigate.   Ellison asked the man his name.   He seemed nervous.   When the man did not answer but instead began to back away, Ellison immediately closed the gap and reached out to pat the man's outer clothing.   Ellison's quick move was to see if he had any weapons that could harm him or his partner.   The first place he touched was the man's right front pants pocket, where he felt a firearm.   He shouted "gun" to his partner and grabbed the man's arm.   Ellison and his partner then put the man up against the patrol car, removed the gun from his pocket, handcuffed him and placed him under arrest.</p>
    </div>
    <div class="num" id="p3">
      <span class="num">3</span>
      <p class="indent">The man was later identified as Izeal Rideau, previously convicted of robbery and burglary in Texas state court.   Rideau was charged with possession of a firearm by a convicted felon, in violation of <span class="citation no-link">18 U.S.C. &#167; 922</span>(g)(1).   Before his trial, he moved to suppress the gun, arguing that Ellison violated his Fourth Amendment rights when he stopped him and patted his pants pocket.   The district court denied the motion to suppress, and a jury convicted Rideau.   A panel of this court reversed Rideau's conviction on appeal, however, finding that although the officers were justified in detaining Rideau, they had failed to provide specific and articulable facts to justify a patdown, and thereby violated the Fourth Amendment's prohibition on unreasonable searches and seizures, <span class="citation" data-id="572438"><a href="/opinion/572438/united-states-v-izeal-rideau-jr/" aria-description="Citation for case: United States v. Izeal Rideau, Jr.">949 F.2d 718</a></span>.   We granted rehearing en banc to consider the issue further.</p>
    </div>
    <p>II.</p>
    <div class="num" id="p4">
      <span class="num">4</span>
      <p class="indent">In Terry v. Ohio, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968), the Supreme Court explained the limits that the Fourth Amendment imposes on the conduct of police officers on the beat.   First, it recognized that effective crime prevention and detection requires that officers be allowed to detain individuals briefly on the street even though there is no probable cause to arrest them.   To justify such brief detentions, the officers must have a reasonable suspicion that criminal activity is afoot.   The showing required to demonstrate "reasonable suspicion" is considerably less than that which is necessary to prove probable cause.   In this context, the Fourth Amendment requires only some minimal level of objective justification for the officer's actions, measured in light of the totality of the circumstances.   See United States v. Sokolow, <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#6" aria-description="Citation for case: United States v. Sokolow">490 U.S. 1, 6-8</a></span>, <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#1585" aria-description="Citation for case: United States v. Sokolow">109 S.Ct. 1581, 1585</a></span>, <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">104 L.Ed.2d 1</a></span> (1989).</p>
    </div>
    <div class="num" id="p5">
      <span class="num">5</span>
      <p class="indent">Second, the Court recognized that law enforcement officers need to protect themselves and the public at large from violence that may ensue in the course of such encounters.   It therefore held that if police officers are justified in believing that the individuals whose suspicious behavior they are investigating at close range are armed and presently dangerous to the officers or to others, they may conduct a limited protective search for concealed weapons.  Terry, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 24</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#1881" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. at 1881</a></span>;  Adams v. Williams, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U.S. 143, 146</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#1923" aria-description="Citation for case: Adams v. Williams">92 S.Ct. 1921, 1923</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">32 L.Ed.2d 612</a></span> (1972).   An officer need not be certain that an individual is armed;  the issue is whether a reasonably prudent man could believe, based on "specific and articulable facts," that his safety or that of others is in danger.  <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">Id.</a></span> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 27</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#1883" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. at 1883</a></span>;  Maryland v. Buie, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#332" aria-description="Citation for case: Maryland v. Buie">494 U.S. 325, 332</a></span>, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#1097" aria-description="Citation for case: Maryland v. Buie">110 S.Ct. 1093, 1097</a></span>, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">108 L.Ed.2d 276</a></span> (1990).</p>
    </div>
    <div class="num" id="p6">
      <span class="num">6</span>
      <p class="indent">In assessing the reasonableness of an officer's actions, "it is imperative that the facts be judged against an objective standard:  would the facts available to the officer at the moment of the seizure or the search 'warrant a man of reasonable caution in the belief' that the action taken was appropriate?".  Terry, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 22</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#1880" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. at 1880</a></span> (citations omitted).   The officer's state of mind, or his stated justification for his actions, is not the focus of our inquiry.   See Maryland v. Macon, <span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/#470" aria-description="Citation for case: Maryland v. MacOn">472 U.S. 463, 470-71</a></span>, <span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/#2782" aria-description="Citation for case: Maryland v. MacOn">105 S.Ct. 2778, 2782-83</a></span>, <span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/" aria-description="Citation for case: Maryland v. MacOn">86 L.Ed.2d 370</a></span> (1985);  Scott v. United States, <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#138" aria-description="Citation for case: Scott v. United States">436 U.S. 128, 138-39</a></span>, <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#1723" aria-description="Citation for case: Scott v. United States">98 S.Ct. 1717, 1723-24</a></span>, <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/" aria-description="Citation for case: Scott v. United States">56 L.Ed.2d 168</a></span> (1978);  United States v. Colin, <span class="citation" data-id="557811"><a href="/opinion/557811/united-states-v-antonio-h-colin/#678" aria-description="Citation for case: United States v. Antonio H. Colin">928 F.2d 676, 678</a></span> (5th Cir.1991).   As long as all the facts and circumstances, viewed objectively, support the officer's decisions, the Fourth Amendment is satisfied.   We must attempt to put ourselves in the shoes of a reasonable police officer as he or she approaches a given situation and assesses the likelihood of danger in a particular context.</p>
    </div>
    <div class="num" id="p7">
      <span class="num">7</span>
      <p class="indent">There is no serious question that Ellison had reasonable suspicion to detain Rideau.   Rideau had been standing in the roadway at night in a high crime area, where public drunkenness was common, and stumbled out of the road only when Ellison flashed his lights at him.   Ellison had reason to believe that Rideau was drunk.   Since public intoxication is a criminal offense under Texas law, see Tex.  Penal Code &#167; 42.08 (Vernon's 1991), the officers had adequate grounds for a stop.   In any event, Terry recognizes that "[e]ncounters are initiated by the police for a wide variety of purposes, some of which are wholly unrelated to a desire to prosecute for crime."  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#13" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 13</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#1876" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. at 1876</a></span>.   Police have long served the public welfare by removing intoxicated people from the public streets, where they pose a hazard to themselves and others.   See Powell v. Texas, <span class="citation" data-id="9883102"><a href="/opinion/107750/powell-v-texas/" aria-description="Citation for case: Powell v. Texas">392 U.S. 514</a></span>, <span class="citation" data-id="9883102"><a href="/opinion/107750/powell-v-texas/" aria-description="Citation for case: Powell v. Texas">88 S.Ct. 2145</a></span>, <span class="citation" data-id="9883102"><a href="/opinion/107750/powell-v-texas/" aria-description="Citation for case: Powell v. Texas">20 L.Ed.2d 1254</a></span> (1968);  see also Cady v. Dombrowski, <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski">413 U.S. 433, 441</a></span>, <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#2528" aria-description="Citation for case: Cady v. Dombrowski">93 S.Ct. 2523, 2528</a></span>, <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">37 L.Ed.2d 706</a></span> (1973) (describing "community caretaking functions" that police officers serve).   Officer Ellison was warranted in stopping to investigate the situation and check on the man's condition.</p>
    </div>
    <div class="num" id="p8">
      <span class="num">8</span>
      <p class="indent">We also find that Ellison's decision to reach out and pat Rideau's pocket rested on specific and articulable facts.   A reasonably prudent man in Ellison's situation could have believed that his safety and that of his partner was in danger.   Ellison already had some reason to believe that Rideau might be intoxicated or perhaps injured.   When approached and asked his name, Rideau did not respond but appeared nervous and, critically, backed away.   It was not unreasonable under the circumstances for Ellison to have feared that Rideau was moving back to give himself time and space to draw a weapon.   It was not then unreasonable for Ellison simply to touch Rideau's front pants pocket to determine whether he had a gun.</p>
    </div>
    <div class="num" id="p9">
      <span class="num">9</span>
      <p class="indent">Rideau's specific moves took place after a detention, at night, in a high crime area where the carrying of weapons is common.   These are articulable facts upon which a police officer may legitimately rely in justifying his actions.   See Adams v. Williams, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U.S. 143</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">92 S.Ct. 1921</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">32 L.Ed.2d 612</a></span> (1972);  United States v. Laing, <span class="citation" data-id="532013"><a href="/opinion/532013/united-states-v-kenroy-laing-aka-junior-roy-laing-united-states-of/#286" aria-description="Citation for case: United States v. Kenroy Laing, A/K/A Junior Roy Laing,...">889 F.2d 281, 286</a></span> (D.C.Cir.1989);  United States v. Trullo, <span class="citation" data-id="9475728"><a href="/opinion/481633/united-states-v-john-f-trullo/#111" aria-description="Citation for case: United States v. John F. Trullo">809 F.2d 108, 111</a></span> (1st Cir.1987).   Stripped from their context, the backward steps offer no threat, but to a police officer in Ellison's situation, they become very significant in the matrix of the general facts.   Stated abstractly, specific actions may be construed as more or less hostile depending on the setting in which they occur.   Of course, that an individual is in a high crime neighborhood at night is not in and of itself enough to support an officer's decision to stop or frisk him.  Brown v. Texas, <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#52" aria-description="Citation for case: Brown v. Texas">443 U.S. 47, 52</a></span>, <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#2641" aria-description="Citation for case: Brown v. Texas">99 S.Ct. 2637, 2641</a></span>, <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">61 L.Ed.2d 357</a></span> (1979).   But when someone engages in suspicious activity in a high crime area, where weapons and violence abound, police officers must be particularly cautious in approaching and questioning him.   Trained, experienced officers like Ellison may perceive danger where an untrained observer would not.  <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Id.</a></span> at 52 n. 2, <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">99 S.Ct. at 2641</a></span> n. 2.   We are unwilling to tie the hands of police officers operating in potentially dangerous situations by precluding them from taking reasonable steps to ensure their safety when they have legitimately detained an individual.</p>
    </div>
    <div class="num" id="p10">
      <span class="num">10</span>
      <p class="indent">We do not suggest that the police have a right to frisk anyone on the street at night in a high crime neighborhood.   There was no such rousting here.   First, as we have observed, the detention was proper, beyond cavil.   That is, only persons meeting the requirements of a Terry stop can be detained, and this detention did not rest solely on Rideau's presence in a bad part of town.   Second, after Rideau was lawfully detained, he responded to the request of the officer by backing away--a move which in this specific context was reasonably seen as threatening.   Ellison could reasonably believe that Rideau was gaining room to use a weapon.   Rideau had no legitimate right to be free of the minor invasion of his liberty that came in response to this behavior.   On these facts, there is no basis for concluding that the officer's concerns for his safety were unreasonable.   We reject the suggestion that Rideau's movement could not reasonably be seen as threatening because it at best presented a risk of flight.   The suggestion ironically discloses the emptiness of Rideau's asserted liberty interest.   The officer could have grabbed Rideau to keep him from fleeing.   It is perverse to suggest that he could not touch him to protect himself against the drawing of a weapon.</p>
    </div>
    <div class="num" id="p11">
      <span class="num">11</span>
      <p class="indent">The scope of Ellison's "frisk" of Rideau is a relevant factor for us to consider.  "The touchstone of our analysis under the Fourth Amendment is always 'the reasonableness in all the circumstances of the particular governmental invasion of a citizen's personal security.' "  Pennsylvania v. Mimms, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#109" aria-description="Citation for case: Pennsylvania v. Mimms">434 U.S. 106, 109</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#332" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330, 332</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">54 L.Ed.2d 331</a></span> (1977) (quoting Terry );  see also Michigan v. Long, <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1045" aria-description="Citation for case: Michigan v. Long">463 U.S. 1032, 1045-46</a></span>, <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#3479" aria-description="Citation for case: Michigan v. Long">103 S.Ct. 3469, 3479</a></span>, <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">77 L.Ed.2d 1201</a></span> (1983).   Reaching out to touch Rideau's pocket was a limited and tailored response to Ellison's fears for his safety, and served to validate his concerns.   Its very spontaneity equally validates the objective reasonableness of the practical balance of safety and liberty.   This was not the intrusive exploration of a detainee's body that the Court envisioned in Terry.<a class="footnote" href="#fn2" id="fn2_ref">2</a> Rideau was not put up against a wall or across a car and subjected to a shake down.   As we have observed, Ellison could have grabbed Rideau in a more invasive manner to prevent him from fleeing.   Thus the minimal intrusion involved in this encounter is another factor supporting officer Ellison's decision.</p>
    </div>
    <div class="num" id="p12">
      <span class="num">12</span>
      <p class="indent">The dissent accuses us of taking "significant liberties with both the facts and the law."   It is settled that in reviewing this denial of a motion to suppress, we view the evidence taken both at the suppression hearing and at trial in the light most favorable to the ruling.  United States v. Simmons, <span class="citation" data-id="551302"><a href="/opinion/551302/united-states-v-robert-simmons/#479" aria-description="Citation for case: United States v. Robert Simmons">918 F.2d 476, 479</a></span> (5th Cir.1990).   The dissent turns the standard upside down, searching for any inference contrary to the district court's ruling, proceeding as if this ruling, by a veteran of thirty-six years on the trial bench, did not exist.   At trial, Rideau told a very different story about the street encounter, and the district judge simply did not believe him.   He denied walking away from the police officers, denied tripping or stumbling, and even denied that the gun was found in the frisk.   His story was that the police officers found a cocaine pipe in his sock and while on the "... way from putting me in the back of the vehicle ... that's when I throwed the gun on the ground."   The dissent refers to our statement that Rideau "began to back away" as "at best misleading."   The arresting officer used these exact words in his testimony, and we are required to give credence to them.   Curiously, Judge Smith, in writing the panel opinion described the facts as follows:  "Ellison got out of the car and asked Rideau to identify himself.   Rideau began to back away."</p>
    </div>
    <div class="num" id="p13">
      <span class="num">13</span>
      <p class="indent">We do not depart from the rule that police officers must have specific and articulable facts indicating that their safety is in danger to justify a patdown.   Nor do we assert that a lawful detention is a license to frisk.   We simply look to the reality that the setting in which the police officer acts may reasonably and significantly affect his decisional calculus.   A reasonably prudent man in officer Ellison's position could believe that he was in danger as he approached Rideau.   The minimally intrusive action that he took to ensure his safety and that of his partner was not a violation of Rideau's constitutional rights.   The Fourth Amendment does not require police to allow a suspect to draw first.   This is East Texas, but it is 1992.</p>
    </div>
    <div class="num" id="p14">
      <span class="num">14</span>
      <p class="indent">AFFIRMED.</p>
    </div>
    <div class="num" id="p15">
      <span class="num">15</span>
      <p class="indent">JERRY E. SMITH, Circuit Judge, with whom POLITZ, Chief Judge, GOLDBERG, DUHE and WIENER, Circuit Judges, join, dissenting:</p>
    </div>
    <div class="num" id="p16">
      <span class="num">16</span>
      <p class="indent">The en banc majority takes limited but significant liberties with both the facts and the law.   More importantly, the court today comes dangerously close to declaring that persons in "bad parts of town" enjoy second-class status in regard to the Fourth Amendment.   Accordingly, I respectfully dissent from its well-intentioned view.</p>
    </div>
    <p>I.</p>
    <div class="num" id="p17">
      <span class="num">17</span>
      <p class="indent">In some important particulars, the facts in the record bear only a superficial resemblance to those set forth in the opinion for the en banc court.   The pertinent portions of the record are brief and are reprinted in the two footnotes that follow.   The first is from the transcript of the suppression hearing,<a class="footnote" href="#fn1-1" id="fn1-1_ref">1</a> and the second recounts the relevant portions of the trial before the jury.<a class="footnote" href="#fn2-1" id="fn2-1_ref">2</a></p>
    </div>
    <div class="num" id="p18">
      <span class="num">18</span>
      <p class="indent">As the transcript reveals, there is more to the facts than the majority has disclosed. Importantly, the majority opinion, as well as the government's oral argument, emphasizes Officer Ellison's suspicion that the defendant, Izeal Rideau, was drunk.   In fact, at the suppression hearing (at the close of which the district court denied the motion to suppress the fruits of the search), absolutely no mention was made of intoxication.   Instead, at that hearing Ellison, when asked at what point he decided to detain Rideau and talk to him, said, "After observing him stumble, as he moved out of the street."</p>
    </div>
    <div class="num" id="p19">
      <span class="num">19</span>
      <p class="indent">Even if the mention of stumbling<a class="footnote" href="#fn3-1" id="fn3-1_ref">3</a> could be understood as a proxy for intoxication,<a class="footnote" href="#fn4" id="fn4_ref">4</a> Ellison used it as justification only for the stop, not for the frisk.   But at issue here is the patdown, for, as the majority says and the panel held, there is no dispute that the officers had justification to detain Rideau, at least briefly, under Terry v. Ohio, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968).</p>
    </div>
    <div class="num" id="p20">
      <span class="num">20</span>
      <p class="indent">Intoxication was never mentioned until the trial on the merits, when Ellison finally said that he at first thought Rideau might be drunk.<a class="footnote" href="#fn5" id="fn5_ref">5</a>  He acknowledged that the only reason he stopped Rideau was that he saw him trip, "[c]ompounded with standing in the roadway."</p>
    </div>
    <div class="num" id="p21">
      <span class="num">21</span>
      <p class="indent">There is no suggestion that, once Rideau had stepped the six or seven feet to the edge of the road, he was a threat to himself or others.   He did exactly what Ellison wanted him to do--leave the roadway.   At that point his actions were those of a reasonable person and could be viewed, if anything, as cooperative.   Without more, there were no articulable facts to justify a search.</p>
    </div>
    <div class="num" id="p22">
      <span class="num">22</span>
      <p class="indent">The only justification offered by the majority is that Rideau "began to back away" as Ellison got out of his patrol car and walked toward him.   This is, at best, misleading.   Ellison's plain testimony is that Rideau only took "a couple of steps backwards"--hardly the makings of a hasty retreat to gain room to draw a weapon.</p>
    </div>
    <div class="num" id="p23">
      <span class="num">23</span>
      <p class="indent">In fact, the theory that Rideau intended, or appeared, to move back to give himself room to draw a gun is wholly the invention of the majority.<a class="footnote" href="#fn6" id="fn6_ref">6</a>  Officer Ellison's explanation is critically different.   At the suppression hearing, without mentioning any fear that Rideau was retreating in order to produce a gun, Ellison simply states, in conclusionary terms, that "concerned for my safety, due to the area, time of night and his apparent nervousness, I reached out to pat his outer clothing for officer safety."</p>
    </div>
    <div class="num" id="p24">
      <span class="num">24</span>
      <p class="indent">At the jury trial, Ellison's testimony was even more telling.   It is obvious that his suspicion of Rideau was a product of Rideau's condition and circumstance, not--as the majority opines--a result of any action taken by the defendant.   The search of Rideau, importantly, was conducted because of the general conditions in the neighborhood and not because of any articulable suspicion regarding Rideau.</p>
    </div>
    <div class="num" id="p25">
      <span class="num">25</span>
      <p class="indent">Thus, asked "what's the purpose of you patting somebody down in that area?", Ellison's explanation was as follows:</p>
    </div>
    <div class="num" id="p26">
      <span class="num">26</span>
      <p>The purpose of that is, a lot of times you have an area such as this, it is a high crime area, the officer is always concerned for his safety and any other citizens that could be nearby.   You pat down a person's outer clothing to determine if he's got any kind of weapons or knives, guns, et cetera, that could be quickly accessible to him before you could have a chance to get control of him, if he did try to go for them.  [Emphasis added.]</p>
    </div>
    <div class="num" id="p27">
      <span class="num">27</span>
      <p class="indent">Remarkably, what Ellison unwittingly describes is akin to a general warrant<a class="footnote" href="#fn7" id="fn7_ref">7</a> or to an indiscriminate dragnet-like procedure whereby all persons detained in a "bad part of town" are subject to search, not for anything they have done, but for the general purpose of ensuring the officer's safety or finding evidence of criminal activity.   In other words, Ellison frisked Rideau not because Rideau did anything (i.e., stepped backward) to arouse individualized suspicion but because he was there, in a bad part of town, and, like anyone else in that area that night, might have had a weapon.</p>
    </div>
    <div class="num" id="p28">
      <span class="num">28</span>
      <p class="indent">Thus, the search of Rideau was conducted not because he had started to draw a weapon--or because a reasonable officer in Ellison's situation objectively might have believed as much.   Instead, the patdown was effected to make sure that the officers would not be harmed if Rideau should decide to go for a gun--a gun the officers had no reason to believe he even had.   Unfortunately, however, for those who accept the dangers inherent in law enforcement work, the Fourth Amendment does not provide officers with that hefty an insurance policy.</p>
    </div>
    <div class="num" id="p29">
      <span class="num">29</span>
      <p class="indent">I must take issue, therefore, with the majority's assertion that "[i]t was not unreasonable under the circumstances for Ellison to have feared that Rideau was moving back to give himself time and space to draw a weapon."   Maj. op. at 1575.   Nothing that Rideau did showed that he--any more than anyone else in that area that night--was likely to endanger the police or the public.   Again, the Constitution requires specific and articulable facts.   An amorphous fear for one's safety, and the desire to take extra steps to guarantee that safety, are not enough.</p>
    </div>
    <div class="num" id="p30">
      <span class="num">30</span>
      <p class="indent">In this regard, one must examine in some depth the details of Rideau's movements at the instant in question.   It is undisputed that he took only "a couple of steps backwards," a critical detail the majority fails to note.   First, a movement of two steps, without more,<a class="footnote" href="#fn8" id="fn8_ref">8</a> is not enough to indicate that a suspect is trying to buy space in which to pull a gun, and no reasonable person could think as much.   Second, there is no reasonable ground for concluding that that specific action was more threatening than any other action Rideau could have taken.</p>
    </div>
    <div class="num" id="p31">
      <span class="num">31</span>
      <p class="indent">By the government's own acknowledgement, and the majority's rationale, Rideau is caught in a classic "Catch 22."   That is, once the officers exited their vehicle and began walking toward him, there is nothing he could have done to save himself from a frisk.   The action he took--stepping back a couple of paces--has been fantasized by the majority into a hastily conceived plot to draw a gun and fire on the officers.   But, as the government seemed to admit in oral argument, any other action, by that point, also would have been viewed as "suspicious."</p>
    </div>
    <div class="num" id="p32">
      <span class="num">32</span>
      <p class="indent">For example, if Rideau had stepped forward, Ellison most certainly would have viewed it as threatening.   Had the defendant stepped to the right or left, it would have been interpreted as nervousness or an attempt to flee.   If Rideau had remained stiffly frozen in place, it would have been viewed, presumably, as a show of guilt or of abnormal behavior caused by drugs or alcohol.</p>
    </div>
    <div class="num" id="p33">
      <span class="num">33</span>
      <p class="indent">Perhaps if Rideau had graduated from charm school and had been taught how to look "cool and collected" in the face of approaching uniformed officers, he could have managed to avoid the patdown.   Otherwise, he was doomed to the intrusion that in fact occurred.   Government counsel candidly admitted as much, at oral argument, by stating that Rideau was subject to search as soon as he was seen standing in the street, then tripping;  in other words, Ellison did not even have to rely upon fear of his safety as an excuse for the frisk.</p>
    </div>
    <div class="num" id="p34">
      <span class="num">34</span>
      <p class="indent">The Fourth Amendment proscribes only those searches that are unreasonable.   But it defies reason to base a justification for a search upon actions that any similarly-situated person would have taken.   The meat of the Terry analysis is that a search is unreasonable if it is based not upon the individualized and unusual actions taken by the suspect but upon actions any reasonable person would or might have taken under the circumstances.</p>
    </div>
    <div class="num" id="p35">
      <span class="num">35</span>
      <p class="indent">Indeed, one can surmise that many totally innocent citizens, upon seeing the approach of two uniformed officers, would take "a couple of steps" backward and would be surprised to learn that that normal reaction could subject them to a search of their person and the consequent invasion of privacy.   This underscores the fact that Rideau was searched not because of anything he did but because of his status--a person in a "bad part of town" where, presumably, people do not belong late at night, on the street, unless they are "up to no good."   By that measure, almost any person in the vicinity of Martin Luther King Boulevard and Bonham Street that night could have been stopped and frisked.</p>
    </div>
    <div class="num" id="p36">
      <span class="num">36</span>
      <p class="indent">The only "fact" that distinguishes Rideau from other such persons is that he was seen to stumble in the street while avoiding an oncoming car.   But, as the panel held, that action alone reasonably subjected him only to a stop--a brief inquiry by the officers to check on his condition--and not to a search<a class="footnote" href="#fn9" id="fn9_ref">9</a> of his person.   This is why what was done to Rideau is tantamount to a general warrant, a dragnet, and why what happened to Rideau is precisely what the Constitution forbids.</p>
    </div>
    <p>II.</p>
    <div class="num" id="p37">
      <span class="num">37</span>
      <p class="indent">The majority mentions only in passing, and fails to discuss, the most significant Supreme Court authority regarding this case.   In Maryland v. Buie, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">494 U.S. 325</a></span>, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">110 S.Ct. 1093</a></span>, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">108 L.Ed.2d 276</a></span> (1990), the Court summarizes the law as it has developed since the seminal case of Terry v. Ohio, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968).   The Court reminds us that Terry authorizes only "a limited patdown for weapons where a reasonably prudent officer would be warranted in the belief, based on 'specific and articulable facts,' ... and not on a mere 'inchoate and unparticularized suspicion or "hunch," ... that he is dealing with an armed and dangerous individual.' "  Buie, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#332" aria-description="Citation for case: Maryland v. Buie">494 U.S. at 332</a></span>, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#1097" aria-description="Citation for case: Maryland v. Buie">110 S.Ct. at 1097</a></span> (emphasis added) (quoting Terry, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 21, 27</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#1880" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. at 1880, 1883</a></span>).</p>
    </div>
    <div class="num" id="p38">
      <span class="num">38</span>
      <p class="indent">The majority concludes that "[a] reasonably prudent man in Ellison's situation could have believed that his safety and that of his partner was [sic] in danger."   Maj. op. at 1574.   But the Court in Buie--a recent restatement of Terry--words it in a way that requires much more:  The officer must reasonably believe "that he is dealing with an armed and dangerous individual."  Buie, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#332" aria-description="Citation for case: Maryland v. Buie">494 U.S. at 332</a></span>, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">110 S.Ct. at 1097</a></span> (quoting Terry, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 27</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#1883" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. at 1883</a></span>).   Significantly, this is phrased in the conjunctive:  The suspect must be both armed and dangerous.</p>
    </div>
    <div class="num" id="p39">
      <span class="num">39</span>
      <p class="indent">It is true that Rideau proved to be armed, but hindsight will not justify a search.   As I have stated, the fact of tripping slightly in the street, coupled with his taking two steps backward, gave the officers no reasonable belief that he was armed.   Moreover, absolutely nothing in this record supports a reasonable conclusion that, at the moment he was searched, Rideau was also "dangerous," to either the officers or others.</p>
    </div>
    <div class="num" id="p40">
      <span class="num">40</span>
      <p class="indent">The majority also misreads the law regarding "specific and articulable facts."   Emphatically, the Supreme Court in Buie has reiterated its warning in Terry that the officer's belief<a class="footnote" href="#fn10" id="fn10_ref">10</a> that the suspect is "armed and dangerous" may not be based upon only "a mere inchoate and unparticularized suspicion or 'hunch.' "  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Id.</a></span> (first internal quotation marks omitted).<a class="footnote" href="#fn11" id="fn11_ref">11</a></p>
    </div>
    <div class="num" id="p41">
      <span class="num">41</span>
      <p class="indent">Yet, such an impermissible "hunch" is the very most that Ellison seems to be describing when he states, "The purpose of [the patdown] is, a lot of times you have an area such as this, it is a high crime area, the officer is always concerned for his safety...."  In fact, this statement seems not even to describe a hunch but rather a general practice of searching all suspects in high-crime areas, even without individualized suspicion.   The only other factor that Ellison relied upon was Rideau's "apparent nervousness," but there is nothing about such a trait that would indicate to a reasonable officer that a person is armed and dangerous.<a class="footnote" href="#fn12" id="fn12_ref">12</a></p>
    </div>
    <div class="num" id="p42">
      <span class="num">42</span>
      <p class="indent">This is the heart of the instant case.   The essential question for the en banc court today is whether an officer may use the general conditions in a particular part of town as justification for a search, where the suspect is guilty of no culpable conduct but merely reacts as any reasonable person would under the circumstances.<a class="footnote" href="#fn13" id="fn13_ref">13</a></p>
    </div>
    <div class="num" id="p43">
      <span class="num">43</span>
      <p class="indent">In Buie, the Court addresses this question specifically:</p>
    </div>
    <div class="num" id="p44">
      <span class="num">44</span>
      <p>[D]espite the danger that inheres in on-the-street encounters and the need for police to act quickly for their own safety, ... [e]ven in high crime areas, where the possibility that any given individual is armed is significant, Terry requires reasonable, individualized suspicion before a frisk of weapons can be conducted.</p>
    </div>
    <div class="num" id="p45">
      <span class="num">45</span>
      <p class="indent"><span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">Id.</a></span> <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">494 U.S. at 334</a></span> n. 2, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">110 S.Ct. at 1098</a></span> n. 2.</p>
    </div>
    <div class="num" id="p46">
      <span class="num">46</span>
      <p class="indent">The majority does not attend to this important passage from Buie.   It sets forth, as the only articulable facts upon which it relies, that the officers had reason to believe Rideau was intoxicated or injured;  that when approached, Rideau "did not respond but appeared nervous and, critically, backed away";  and that "Rideau's specific moves took place after a detention, at night, in a high crime area where the carrying of weapons is common."   Maj. op. at 1574-1575.<a class="footnote" href="#fn14" id="fn14_ref">14</a></p>
    </div>
    <div class="num" id="p47">
      <span class="num">47</span>
      <p class="indent">The majority takes pains to state that "[o]f course, that an individual is in a high crime neighborhood at night is not in and of itself enough to support an officer's decision to stop or frisk him."   Id. at 1575.<a class="footnote" href="#fn15" id="fn15_ref">15</a>  So, it is only what the majority terms Rideau's "suspicious activity," id., that the majority adds to the equation to tip the scales in favor of the frisk.   But it is a challenge to the imagination to say that Rideau's actions were "suspicious," and certainly there was nothing about them that gave rise to a reasonable suspicion that he was armed and dangerous.</p>
    </div>
    <div class="num" id="p48">
      <span class="num">48</span>
      <p class="indent">Thus, the majority in this case has installed the very rule it attempts to deny:  that, practically speaking, any person in a high-crime area (or "bad part of town") late at night is subject to a frisk.   Such a maxim could make the directive to "round up the usual suspects" the order of the day.</p>
    </div>
    <p>III.</p>
    <div class="num" id="p49">
      <span class="num">49</span>
      <p class="indent">The majority expresses a concern that I share regarding officer safety--a problem important enough to warrant separate discussion.   In Buie, Terry, and elsewhere, the Supreme Court has provided that a search can be reasonable under some circumstances when effected to ensure safety in the field, when spur-of-the-moment encounters reasonably raise the specter of danger to an officer or to others.   It is also plain, however, that such concerns do not automatically trump the Fourth Amendment.</p>
    </div>
    <div class="num" id="p50">
      <span class="num">50</span>
      <p class="indent">The safety of police officers undoubtedly would be enhanced if, when entering a high-crime area for a legitimate purpose, they could briefly and effectively search all persons in the area for weapons.   The salutary interest of law enforcement would be served by such a rule, but it would come at the unacceptable expense of intrusions upon innocent members of the public as to whom there is no reasonable suspicion of wrongdoing.   Our Bill of Rights does not permit such intrusions.</p>
    </div>
    <div class="num" id="p51">
      <span class="num">51</span>
      <p class="indent">The majority, Maj. op. at 1576, reminds us that this is 1992, presumably referring to the growing problem of drugs and crime in our inner cities and to the consequent dangers that confront well-meaning law enforcement personnel who enter there to do their jobs.   But only two years ago, in 1990, the Supreme Court reminded us that the proscription of unreasonable searches is alive and well despite the obvious peril to officers that can be presented by limiting their ability to conduct street searches.   The Court's words are poignant, so I quote them again:</p>
    </div>
    <div class="num" id="p52">
      <span class="num">52</span>
      <p>[D]espite the danger that inheres in on-the-street encounters and the need for police to act quickly for their own safety, the Court in Terry did not adopt a bright-line rule authorizing frisks for weapons in all confrontational encounters.   Even in high crime areas, where the possibility that any given individual is armed is significant, Terry requires reasonable, individualized suspicion before a frisk for weapons can be conducted.</p>
    </div>
    <div class="num" id="p53">
      <span class="num">53</span>
      <p class="indent">Buie, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">494 U.S. at 334</a></span> n. 2, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">110 S.Ct. at 1098</a></span> n. 2 (emphasis added).</p>
    </div>
    <div class="num" id="p54">
      <span class="num">54</span>
      <p class="indent">We must remember, too, that this is not an all-or-nothing matter.   By imposing limits on searches, the Constitution and the Supreme Court have not left the police unprotected.   The requirement of individualized suspicion merely ensures that officers receive greater protection in those instances in which they are most likely to be in danger.   That is the essence of the requirement that searches be "reasonable."</p>
    </div>
    <div class="num" id="p55">
      <span class="num">55</span>
      <p class="indent">Like the rule of Miranda v. Arizona, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U.S. 436</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L.Ed.2d 694</a></span> (1966), the lesson of Buie and Terry makes law enforcement more difficult.   Much as police officers must learn to administer the warnings required by the Court in Miranda, they likewise must be aware of the constraints upon searches in the street and must accept their jobs with that understanding.<a class="footnote" href="#fn16" id="fn16_ref">16</a></p>
    </div>
    <div class="num" id="p56">
      <span class="num">56</span>
      <p class="indent">This is no criticism of Officer Ellison.   He is accused of no wrongdoing or malice, and his actions are subject to reasonably differing legal interpretations that today divide our en banc court.   The search he conducted on defendant Rideau was in accordance with proper procedure as he understood it and was in the interest of law enforcement.   The majority has put its stamp of approval on his conduct;  concluding that he crossed the constitutional line, I disagree.</p>
    </div>
    <p>IV.</p>
    <div class="num" id="p57">
      <span class="num">57</span>
      <p class="indent">Finally, I wish to comment upon the status of this case as an en banc rehearing.   Interestingly, the government never requested either en banc or panel rehearing in this matter.   Nor, as often is its practice, did it even seek an extension of time in which to suggest rehearing en banc, in order to seek permission from the Solicitor General.</p>
    </div>
    <div class="num" id="p58">
      <span class="num">58</span>
      <p class="indent">Presumably, this is because the Department of Justice and the interests it represents perceived no jurisprudential danger from the panel's conclusion that the fruits of the instant search should be suppressed.   This case was routine, made no new law, and should not have been reviewed en banc.   The panel opinion posed no threat to officer safety, and the government's reaction to it showed as much.<a class="footnote" href="#fn17" id="fn17_ref">17</a></p>
    </div>
    <div class="num" id="p59">
      <span class="num">59</span>
      <p class="indent">By taking the case en banc and fashioning today's ruling, the court has run afoul of the Constitution and Supreme Court precedent and has rendered the Fourth Amendment essentially meaningless in an entire category of ordinary street encounters.   Despite the good intention of the majority to protect our officers on the street, I respectfully dissent.</p>
    </div>
    <div class="footnotes">
      <div class="footnote" id="fn1">
        <a class="footnote" href="#fn1_ref">1</a>
        <p> Defendant testified that the encounter occurred between 3:30 and 4:30 a.m.   The arresting officer placed the time at 10:30 p.m</p>
      </div>
      <div class="footnote" id="fn2">
        <a class="footnote" href="#fn2_ref">2</a>
        <p> The Court described a frisk in Terry as follows:  " 'The officer must feel with sensitive fingers every portion of the prisoner's body.   A thorough search must be made of the prisoner's arms and armpits, waistline and back, the groin and area about the testicles, and entire surface of the legs down to the feet.' "  392 U.S. at 17 n. 13, 88 S.Ct. at 1877 n. 13 (citation omitted)</p>
      </div>
      <div class="footnote" id="fn1-1">
        <a class="footnote" href="#fn1-1_ref">1</a>
        <p> The pertinent portion of the transcript of the suppression hearing is as follows:</p>
        <p>Direct examination of defendant Rideau (by his attorney):</p>
        <p>Q. At the time of the arrest where were you standing?</p>
        <p>A. On the street corner.</p>
        <p>Q. You were at the corner of Martin Luther King Boulevard and Bonham Street?</p>
        <p>A. Yes.</p>
        <p>Q. Was there anyone with you?</p>
        <p>A. No, sir.</p>
        <p>Q. Were you just standing on the street corner at that time?</p>
        <p>A. Standing on the street corner, on the side of the street.</p>
        <p>Q. Did the officers approach you in a marked vehicle?</p>
        <p>A. They came in a white--black-and-white car with the siren on top.</p>
        <p>Q. And did you walk away from them at all?</p>
        <p>A. No.</p>
        <p>Q. Did you remain standing at that position?</p>
        <p>A. Yes.</p>
        <p>Q. Had you been in the street at any time where you had tripped or stumbled?</p>
        <p>A. No.</p>
        <p>Q. After the officers approached you, did they place their hands on you?</p>
        <p>A. Yes.</p>
        <p>Cross-examination of defendant Rideau (by government counsel):</p>
        <p>Q. What time of day was this, Mr. Rideau?</p>
        <p>A. I guess it was 3:30, 4:30 in the morning.</p>
        <p>Q. Would you agree with me that at least back on July of '89 that was a[ ] high crime area?</p>
        <p>A. Not really.</p>
        <p>Q. You thought that was a very safe place to go?</p>
        <p>A. People live up there.</p>
        <p>Q. I realize that.   But there are lots of drug dealings going down in that area;  is that correct?</p>
        <p>A. Not at that time.</p>
        <p>Q. I don't mean right at that minute;  I mean that time in 1989 in July?</p>
        <p>A. Yes.</p>
        <p>Q. It has improved now.   But at that point, it was not a place that you want your children to be walking around late at night?</p>
        <p>A. No.</p>
        <p>Q. You do not live in that area;  is that correct?</p>
        <p>A. Yes.</p>
        <p>Q. You were, in fact, living in Liberty?</p>
        <p>A. Yes.</p>
        <p>Q. Isn't it a fact, that you were wearing warm up pants, dark warm up pants?</p>
        <p>A. Yes.</p>
        <p>Q. And what kind of a shirt were you wearing?   Do you remember?</p>
        <p>A. No.</p>
        <p>Q. Dark in color, however?</p>
        <p>A. I think so.</p>
        <p>Q. Isn't it a fact, that when the officers were driving along the street, that you were in fact in the street area?</p>
        <p>A. No.</p>
        <p>Q. Isn't it a fact, that they flashed their headlights to get you to move out of the street?</p>
        <p>A. No.</p>
        <p>Q. They didn't do that at all?</p>
        <p>A. No.</p>
        <p>Q. Isn't it a fact, Mr. Rideau, that the officers pulled over and, without too much discussion, they patted the outside of your clothing?</p>
        <p>A. Yes.</p>
        <p>Direct examination of Officer Ellison (by government counsel):</p>
        <p>Q. Were you in the area of Bonham and Martin Luther King at about 10:30 p.m. on that day?</p>
        <p>A. Yes, ma'am.</p>
        <p>Q. Did you happen to observe someone standing in the roadway of that area wearing dark clothing?</p>
        <p>A. I did.</p>
        <p>Q. What type of area is that, high crime, high crime area, that sort of thing?</p>
        <p>A. Yes, ma'am, it is.   There's a high crime area, drug trafficking, street deals, that type of thing.</p>
        <p>Q. In your experience have you found people in that area also carry weapons?</p>
        <p>A. Yes, ma'am.</p>
        <p>Q. When you observed this person in the roadway with the dark clothing on, what action did you take?</p>
        <p>A. When I saw the person standing there in dark clothing, I flashed my bright lights to see him better and make sure it was a person and if it was, hopefully, he would step out of the roadway.</p>
        <p>Q. And did this person, in fact, step out of the roadway?</p>
        <p>A. Yes, ma'am.</p>
        <p>Q. Did you observe him make that move?</p>
        <p>A. Yes, ma'am.   As he stepped out of the roadway towards the shoulder, he began to stumble somewhat.</p>
        <p>Q. So did you stop to check on his condition?</p>
        <p>A. Yes, ma'am, I did.</p>
        <p>Q. And when got out [sic] of your patrol car, which I assume you did, what action did you take?</p>
        <p>A. I stepped out of the patrol car and approached him and asked him his name.   And as I approached him, he began to back up from me, back away.</p>
        <p>Q. So what did you do then?</p>
        <p>A. At that time, concerned for my safety due to the area, time of night and his apparent nervousness, I reached out to pat his outer clothing for officer safety.</p>
        <p>Q. Did you actual [sic] reach into a pocket or reach into his clothing?</p>
        <p>A. No, ma'am, I did not.</p>
        <p>Q. Specifically, what did you do?</p>
        <p>A. I patted down his outer clothing, his outer pockets, normally [sic] pat down the outer pockets of any jacket or shirt, and his pants.</p>
        <p>Q. And in this particular case, exactly what did you pat?</p>
        <p>A. The first thing that I reached out [sic] was his right front pant's [sic] pocket.</p>
        <p>Q. And what, if anything, did you notice when you touched that outer pocket?</p>
        <p>A. When I touched that outer pocket, I felt what appeared to be a small firearm in the pocket?  [sic]</p>
        <p>Q. And what you did [sic] do then?</p>
        <p>A. At that time I secured him and called out "gun" to my partner.   And then my partner secured the other arm and I reached in and found it to be a small firearm and pulled it out of the pocket.</p>
        <p>Cross-examination of Officer Ellison (by Rideau's counsel):</p>
        <p>Q. And is there a street light at the corner of Martin Luther King and Bonham?</p>
        <p>A. There's a street light near that corner.</p>
        <p>Q. And how is the road surfaced?</p>
        <p>A. It's asphalt.</p>
        <p>Q. Does it have a curb and gutter or does it just have a shoulder?</p>
        <p>A. Just a shoulder, no curb and gutter.</p>
        <p>Q. At the time that you exited your vehicle, where was the Defendant?</p>
        <p>A. He was standing on the shoulder of the roadway.   I don't recall that there's a street light on that corner.</p>
        <p>Q. Now, at the time that you saw him move from the street, had you already flashed your lights?</p>
        <p>A. I flashed the bright lights at him as we were approaching in traffic.</p>
        <p>Q. And was he looking at you when you flashed the bright lights?</p>
        <p>A. Yes, sir.</p>
        <p>Q. Then after that you saw him removed from the street?</p>
        <p>A. Right.</p>
        <p>Q. Now, you're not pretending that it's a crime for a person to stumble are you?</p>
        <p>A. No, sir.</p>
        <p>Q. ... [A]t what point in time did you determine that you were going to stop the Defendant and talk to him?</p>
        <p>A. After observing him stumble, as he moved out of the street.</p>
        <p>Q. Is there any other thing that made you determine that you were going to stop and talk to him?</p>
        <p>A. No, sir.</p>
      </div>
      <div class="footnote" id="fn2-1">
        <a class="footnote" href="#fn2-1_ref">2</a>
        <p> The significant testimony from the trial regarding the search is as follows:</p>
        <p>Direct testimony of Officer Ellison (by government counsel):</p>
        <p>Q. And how long have you been a police officer?</p>
        <p>A. Approximately six and a half years.</p>
        <p>Q. Tell us about that area.   What's in that vicinity, is it a residential, stores, factories, what?</p>
        <p>A. There is a small residential area that is similar to a project type area, there's a night club located about a block away from there.   Other than that, it's mainly commercial.</p>
        <p>Q. And back on July the 6th 1989, what type of a crime area was it?</p>
        <p>A. At that time, this area was an area with numerous drug type offenses:  street buys of cocaine, lots of drunkenness, weapons, drugs and so forth.</p>
        <p>Q. You've experienced all or any of those in your experience as a patrol officer there?</p>
        <p>A. Yes, ma'am.</p>
        <p>Q. You would claim it to be a high crime area?</p>
        <p>A. Yes, ma'am.</p>
        <p>Q. What, if anything, did you observe?</p>
        <p>A. We observed a black male standing in the intersection of Bonham and M.L.K.</p>
        <p>Q. What type of clothing did he have on, do you recall?</p>
        <p>A. He had on dark clothing, is all we could tell from the distance.</p>
        <p>Q. I take it [sic] was hard to see him then?</p>
        <p>A. Yes, ma'am.</p>
        <p>Q. What, if anything, did you do when you observed this man in the street there ...?</p>
        <p>A. I just flicked the bright lights to see if it was someone standing in the road, and then turned them off.</p>
        <p>Q. What action, if anything, did the man take then?</p>
        <p>A. When he saw the bright lights, he had turned towards us, and began to step out of the roadway towards the shoulder.   He was near the corner.   And when he did, he stumbled or tripped or something.</p>
        <p>Q. You don't know if he tripped over anything, but you obviously noticed the stumbling and staggering?</p>
        <p>A. Right.</p>
        <p>Q. At the point that you observed him to stumble or stagger, was he still facing your patrol unit?</p>
        <p>A. He had turned to step out of the roadway, as he--he saw us and then turned to step out of the roadway, and that was the time that he stumbled.</p>
        <p>Q. What did you think when you saw this stumbling?</p>
        <p>A. I thought that he may be intoxicated.</p>
        <p>Q. So what did you do?</p>
        <p>A. We passed through the intersection and stopped right there at the corner where he was standing.</p>
        <p>Q. He didn't try to run away or anything?</p>
        <p>A. No, ma'am.</p>
        <p>Q. Did he, in fact, get out of the roadway?</p>
        <p>A. Yes, ma'am.   He had already stepped out of the roadway and was standing on the shoulder at the corner.</p>
        <p>Q. And after pulling up to the vehicle, did you turn your siren on or anything like that?</p>
        <p>A. No, ma'am.   We just simply pulled over to the shoulder.</p>
        <p>Q. And did you get out of the vehicle then?</p>
        <p>A. Yes, ma'am.</p>
        <p>Q. Did your partner also get out?</p>
        <p>A. Yes, ma'am.</p>
        <p>Q. What did you do when you got out of your vehicle yourself?</p>
        <p>A. I was on the driver's side and my side of the vehicle was closest to him, I stepped out of the vehicle into the roadway and asked him who he was as I walked up to him.</p>
        <p>Q. I take it this is a very--this is happening very quickly then?</p>
        <p>A. Yes, ma'am.   Just enough time to exit the vehicle and step a few feet towards him.</p>
        <p>Q. Okay.   What, if anything, did you observe as you were approaching him?</p>
        <p>A. He began to back up as I spoke to him and approached him a little bit, he took a couple of steps backwards.</p>
        <p>Q. And so what did you do?</p>
        <p>A. At that time I reached out to pat down his outer clothing for any weapons or anything that could harm me or my partner.</p>
        <p>Q. Explain that a little better for us.   What was the purpose of reaching out and patting somebody when you haven't even struck up a conversation yet?</p>
        <p>A. Well, due to the high crime area, the time of the night--</p>
        <p>Q. Once again, what's the purpose of you [sic] patting somebody down in that area?</p>
        <p>A. The purpose of that is, a lot of times you have an area such as this, it is a high crime area, the officer is always concerned for his safety and any other citizens that could be nearby.   You pat down a person's outer clothing to determine if he's got any kind of weapons or knives, guns, et cetera, that could be quickly accessible to him before you could have a chance to get control of him, if he did try to go for them.</p>
        <p>Q. You don't put them up against the wall, across your car?</p>
        <p>A. No, ma'am.   It's simple just to reach and pat of [sic] his outer pockets.   There's no body search or anything like that.   It's simply a pat down....  The first place that I patted him was his right front pant's [sic] pocket....  I felt an object in there that was consistent with a firearm....  At that time I squeezed the--I still didn't reach into the pocket, I just grabbed it as to get control of it, and grabbed his arm and called out "gun" to my partner, who then grabbed his other arm and we placed him up against the patrol car....</p>
        <p>Q. What was the offense that you did, in fact, arrest him for?</p>
        <p>A. Unlawfully carrying a weapon.</p>
        <p>Cross-examination of Officer Ellison (by Rideau's counsel):</p>
        <p>Q. Mr. Ellison, how far from the side of the roadway did you observe the Defendant?</p>
        <p>A. Probably six to seven feet, approximately.</p>
        <p>Q. Was he standing or moving towards the side of the roadway?</p>
        <p>A. He was just standing.</p>
        <p>Q. At the time that you flashed your bright lights, was he facing the vehicle?</p>
        <p>A. I don't recall if he was facing the vehicle at the time that I turned the brights on.   He had turned after I had the brights on;  I could see him then, I could see his face.</p>
        <p>Q. Did he fall all the way to the ground?</p>
        <p>A. No, sir.</p>
        <p>Q. More like a trip as he was walking to the side of the street?</p>
        <p>A. Yes, sir.</p>
        <p>Q. Now, as you were on patrol, did you stop everyone that night that you saw who tripped?</p>
        <p>A. I don't recall doing that, no.</p>
        <p>Q. Is it correct that the only reason that you stopped this man was because you saw him trip?</p>
        <p>A. Saw him trip, thinking that he may be intoxicated, yes.</p>
        <p>Q. But the trip is the only thing that you had suspicion about?</p>
        <p>A. Compounded with standing in the roadway.</p>
        <p>Q. By the time you got up to him, where was he?</p>
        <p>A. He was standing on the shoulder in the southwest corner of those two streets.</p>
      </div>
      <div class="footnote" id="fn3-1">
        <a class="footnote" href="#fn3-1_ref">3</a>
        <p> The term "stumble" must be viewed in light of the entire record, for at another point Ellison answered "Yes" to the question whether Rideau's miscue was "[m]ore like a trip as he was walking to the side of the street."</p>
      </div>
      <div class="footnote" id="fn4">
        <a class="footnote" href="#fn4_ref">4</a>
        <p> The stumbling cannot fairly be read as a surrogate for inebriation, for although, as the majority opinion states, public intoxication is a crime, Ellison answered "No" to the question, "Now, you're not pretending that it's a crime for a person to stumble are you?"</p>
      </div>
      <div class="footnote" id="fn5">
        <a class="footnote" href="#fn5_ref">5</a>
        <p> In fact, Rideau was arrested not for public intoxication but for unlawful possession of a weapon</p>
      </div>
      <div class="footnote" id="fn6">
        <a class="footnote" href="#fn6_ref">6</a>
        <p> Thus, the majority opines that "Ellison's quick move was to see if [Rideau] had any weapons that could harm him or his partner."   Op. at 1573.   Nothing supports this claim except the majority's ipse dixit</p>
      </div>
      <div class="footnote" id="fn7">
        <a class="footnote" href="#fn7_ref">7</a>
        <p> "[I]ndiscriminate searches and seizures conducted under the authority of 'general warrants' were the immediate evils that motivated the framing and adoption of the Fourth Amendment."  Payton v. New York, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York">445 U.S. 573, 583</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1378" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371, 1378</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980) (footnote omitted).   See generally JACOB W. LANDYNSKI, SEARCH AND SEIZURE AND THE SUPREME COURT 19-42 (1966)</p>
      </div>
      <div class="footnote" id="fn8">
        <a class="footnote" href="#fn8_ref">8</a>
        <p> "More" might include, for example, "furtive hand movements," a fact relied upon in a case cited by the majority, United States v. Laing, <span class="citation" data-id="532013"><a href="/opinion/532013/united-states-v-kenroy-laing-aka-junior-roy-laing-united-states-of/#286" aria-description="Citation for case: United States v. Kenroy Laing, A/K/A Junior Roy Laing,...">889 F.2d 281, 286</a></span> (D.C.Cir.1989), cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./494/1008/">494 U.S. 1008</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./110/1306/">110 S.Ct. 1306</a></span>, <span class="citation no-link">108 L.Ed.2d 482</span>, and cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./494/1069/">494 U.S. 1069</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./110/1790/">110 S.Ct. 1790</a></span>, <span class="citation" data-id="9090740"><a href="/opinion/9096492/thai-do-hoang-v-kansas/" aria-description="Citation for case: Thai Do Hoang v. Kansas">108 L.Ed.2d 792</a></span> (1990), or a bulge in the suspect's pocket, as in  United States v. Trullo, <span class="citation" data-id="9475728"><a href="/opinion/481633/united-states-v-john-f-trullo/#113" aria-description="Citation for case: United States v. John F. Trullo">809 F.2d 108, 113</a></span> (1st Cir.), cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./482/916/">482 U.S. 916</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./107/3191/">107 S.Ct. 3191</a></span>, <span class="citation no-link">96 L.Ed.2d 679</span> (1987), another case the majority cites</p>
      </div>
      <div class="footnote" id="fn9">
        <a class="footnote" href="#fn9_ref">9</a>
        <p> The majority describes the search euphemistically.   Thus, in its introduction, the majority states that Ellison "reached out and touched the pants pocket of the individual and discovered a gun."   Maj. op. at 1573.   Similarly, the majority refers to "Ellison's decision to reach out and pat Rideau's pocket," <span class="citation no-link">id. at 1574</span>, and says that the officer "simply [touched] Rideau's front pants pocket," <span class="citation no-link">id. at 1575</span>, and "[r]each[ed] out to touch Rideau's pocket," <span class="citation no-link">id. at 1575</span>.   The phrase "reach out and touch" should be left to long-distance telephone commercials:  The frank truth is that Rideau was searched</p>
        <p>The fact that the frisk in this case did not involve the anatomical exploration that the majority finds it necessary to describe graphically in quoting from Terry v. Ohio, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, 17 n. 13, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, 1877 n. 13, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968), see Maj. op. at 1575 n. 2, makes it no less an intrusion governed by the Fourth Amendment.   What the majority terms "a limited and tailored response," id. at 1575, is the same "frisk for weapons" that the Supreme Court recently has reminded us " 'constitutes a severe, though brief, intrusion upon cherished personal security.' "  Maryland v. Buie, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#332" aria-description="Citation for case: Maryland v. Buie">494 U.S. 325, 332</a></span>, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#1097" aria-description="Citation for case: Maryland v. Buie">110 S.Ct. 1093, 1097</a></span>, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">108 L.Ed.2d 276</a></span> (1990) (quoting Terry, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 24-25</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#1882" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. at 1882</a></span>).</p>
      </div>
      <div class="footnote" id="fn10">
        <a class="footnote" href="#fn10_ref">10</a>
        <p> The majority properly notes that we judge an officer's actions against an objective standard;  Ellison's state of mind is not directly at issue, though his factual observations are</p>
      </div>
      <div class="footnote" id="fn11">
        <a class="footnote" href="#fn11_ref">11</a>
        <p> The majority does not mention this critical passage</p>
      </div>
      <div class="footnote" id="fn12">
        <a class="footnote" href="#fn12_ref">12</a>
        <p> In Brown v. Texas, <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#52" aria-description="Citation for case: Brown v. Texas">443 U.S. 47, 52</a></span>, <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#2641" aria-description="Citation for case: Brown v. Texas">99 S.Ct. 2637, 2641</a></span>, <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">61 L.Ed.2d 357</a></span> (1979), the Court said the fact that the defendant "looked suspicious" was not enough:</p>
        <p>Officer Venegas testified ... that the situation in the alley "looked suspicious," but he was unable to point to any facts supporting that conclusion....  The fact that appellant was in a neighborhood frequented by drug users, standing alone, is not a basis for concluding that appellant himself was engaged in criminal conduct.   In short, the appellant's activity was no different from the activity of other pedestrians in that neighborhood.</p>
        <p>(Footnote omitted.)</p>
        <p>Similarly,</p>
        <p>it has properly been held that the "hesitancy of a car to pass a police cruiser and a glance at the police officer by a passenger," a "startled look at the sight of a police officer," appearing nervous when a police car passed, looking away from police activity in the vicinity, pointing toward police, or quickening one's pace upon seeing the police are not, standing alone, sufficient basis for an investigative stop.</p>
      </div>
      <div class="footnote">
        <a class="footnote">3</a>
        <p> WAYNE R. LAFAVE, SEARCH AND SEIZURE &#167; 9.3(c), at 450-51 (2d ed. 1987) (footnotes omitted).   Accord United States v. Carter, <span class="citation" data-id="2290134"><a href="/opinion/2290134/united-states-v-carter/#27" aria-description="Citation for case: United States v. Carter">369 F.Supp. 26, 27-30</a></span> (E.D.Mo.1974) (no justification for stop where occupants of car "appeared [to officer] to be nervous" and "appeared surprised and disturbed at the presence of the police officer")</p>
        <p>"Nervousness in the presence of a police officer does not furnish a reasonable basis for a detention...."  People v. Loewen, <span class="citation" data-id="9531694"><a href="/opinion/1122661/people-v-loewen/" aria-description="Citation for case: People v. Loewen">35 Cal.3d 117</a></span>, <span class="citation" data-id="9531694"><a href="/opinion/1122661/people-v-loewen/#851" aria-description="Citation for case: People v. Loewen">196 Cal.Rptr. 846, 851</a></span>, <span class="citation" data-id="9531694"><a href="/opinion/1122661/people-v-loewen/#441" aria-description="Citation for case: People v. Loewen">672 P.2d 436, 441</a></span> (1983).  "Nervousness on the part of a black laborer when confronted by an armed uniformed officer does not seem so unusual as to indicate guilt or criminal proclivity."  State v. Scott, <span class="citation" data-id="1141153"><a href="/opinion/1141153/state-v-scott/#989" aria-description="Citation for case: State v. Scott">412 So.2d 988, 989</a></span> (La.1982).</p>
      </div>
      <div class="footnote" id="fn13">
        <a class="footnote" href="#fn13_ref">13</a>
        <p> "The 'high crime area' factor is not an 'activity' of an individual.   Many citizens ... are forced to live in areas that have 'high crime' rates or they come to these areas to shop, work, play, transact business, or visit relatives or friends.   The spectrum of legitimate human behavior occurs every day in so-called high crime areas."  People v. Bower, <span class="citation" data-id="9552492"><a href="/opinion/1187451/people-v-bower/" aria-description="Citation for case: People v. Bower">24 Cal.3d 638</a></span>, <span class="citation" data-id="9552492"><a href="/opinion/1187451/people-v-bower/#860" aria-description="Citation for case: People v. Bower">156 Cal.Rptr. 856, 860</a></span>, <span class="citation" data-id="9552492"><a href="/opinion/1187451/people-v-bower/#119" aria-description="Citation for case: People v. Bower">597 P.2d 115, 119</a></span> (1979)</p>
      </div>
      <div class="footnote" id="fn14">
        <a class="footnote" href="#fn14_ref">14</a>
        <p> The majority avers that "[t]hese [i.e., Rideau's specific moves taking place after a detention, at night, in a high crime area where weapons were common] are articulable facts upon which a police officer may legitimately rely in justifying his actions."   Maj. op. at 1575.   While these are permissible factors, the majority mentions only one Supreme Court case--Adams v. Williams, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U.S. 143</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">92 S.Ct. 1921</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">32 L.Ed.2d 612</a></span> (1972)--in support</p>
        <p>Williams is inapposite, though, as a review of the instant record shows how vapid the present facts are in comparison to those in Williams.   There, an officer was on patrol in a high-crime area when a known informant told him that the defendant was nearby in a car, carrying narcotics and a gun.   The officer proceeded to reach into the defendant's vehicle and remove the weapon from his waistband.   The Court concluded that "[w]hile properly investigating the activity of a person who was reported to be carrying narcotics and a concealed weapon and who was sitting alone in a car in a high-crime area at 2:15 in the morning, [the officer] had ample reason to fear for his safety."  <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#147" aria-description="Citation for case: Adams v. Williams">Id. at 147-48</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#1924" aria-description="Citation for case: Adams v. Williams">92 S.Ct. at 1924</a></span> (footnote omitted).   The Court even emphasized that its case was "stronger ... than obtains in the case of an anonymous telephone tip," <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">id. at 146</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#1923" aria-description="Citation for case: Adams v. Williams">92 S.Ct. at 1923</a></span>, thus suggesting that an anonymous tip might not have been enough to justify the search, even in a high-crime area.</p>
        <p>The Court reiterated the Terry rule as follows:  "[T]he policeman making a reasonable investigatory stop should not be denied the opportunity to protect himself from attack by a hostile suspect.  'When an officer is justified in believing that the individual whose suspicious behavior he is investigating at close range is armed and presently dangerous ...,' he may conduct a limited protective search for concealed weapons."  <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">Id.</a></span> (emphasis added) (quoting Terry, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 24</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#1881" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. at 1881</a></span>).   Rideau was not "hostile," and his actions were not "suspicious."</p>
      </div>
      <div class="footnote" id="fn15">
        <a class="footnote" href="#fn15_ref">15</a>
        <p> "The [majority] doth protest too much, methinks."   WILLIAM SHAKESPEARE, HAMLET act III, sc. ii, ln. 242.   The majority belabors its disclaimer, as though repetition can make it so.   E.g., "Of course, that an individual is in a high crime neighborhood at night is not in and of itself enough to support an officer's decision to stop or frisk him," Maj. op. at 1575;  "[w]e do not suggest that the police have a right to frisk anyone on the street at night in a high crime neighborhood," id. at 1575;  "[w]e do not depart from the rule that police officers must have specific and articulable facts indicating that their safety is in danger to justify a patdown.   Nor do we assert that a lawful detention is a license to frisk," id. at 1576.   The unfortunate fact is that by allowing an innocent action, such as taking two steps backward, to turn a situation in which no search is permitted into one in which a search is justified, the majority in effect has adopted the rule it purports to eschew:  that being in the wrong part of town at the wrong time of day deprives one of significant Fourth Amendment protections</p>
      </div>
      <div class="footnote" id="fn16">
        <a class="footnote" href="#fn16_ref">16</a>
        <p> Today's holding enhances an officer's opportunity to use general terms such as "nervousness" and "suspicious behavior" as pretexts to conduct searches of persons who the officer has no reason to believe has done anything wrong.   The requirement of "specific and articulable facts" should encompass more than the routine use of such generalities</p>
      </div>
      <div class="footnote" id="fn17">
        <a class="footnote" href="#fn17_ref">17</a>
        <p> I do not mean to posit that this court should never consider cases en banc when no party has suggested it.   In fact, we have done so twice recently in cases implicating the Fourth Amendment.   I.e., United States v. Pierre, <span class="citation" data-id="8994043"><a href="/opinion/9001504/united-states-v-pierre/" aria-description="Citation for case: United States v. Pierre">943 F.2d 6</a></span> (5th Cir.1991) (sua sponte granting rehearing en banc);  United States v. DeLeon-Reyna, <span class="citation" data-id="545167"><a href="/opinion/545167/united-states-v-mario-de-leon-reyna/" aria-description="Citation for case: United States v. Mario De Leon-Reyna">908 F.2d 1229</a></span> (5th Cir.1990) (same).   But we should take an extra look when the agency charged with enforcing the laws of the United States, and not known for its timidity in Fourth Amendment cases, decides that a case it has lost is not worthy of en banc review</p>
      </div>
    </div>
    
```

---

## GROUP: _overhaul2/lake/cases/United States v. Robinson (4th Cir. en banc).json  (`lake-record`, 2 assertions)

### content_page

```
---
title: "United States v. Robinson (4th Cir. en banc)"
type: case
citation: "846 F.3d 694 (2017)"
parallel_cite: ""
neutral_cite: "2017 WL 280727; 2017 U.S. App. LEXIS 1134"
court: "U.S. Court of Appeals, 4th Cir. (en banc)"
court_level: coa
circuit: ca4
year: 2017
date_decided: ""
docket: No. 14-4902
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
  opinion_url: "https://www.courtlistener.com/opinion/4340460/united-states-v-shaquille-robinson/"
  cluster_id: 4340460
  opinion_id: null
  identity_checked: true
lake:
  record_id: "United States v. Robinson (4th Cir. en banc)"
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: Illustrates a circuit split
related:
  - "[[Terry Stops and Reasonable Suspicion]]"
  - "[[Terry v. Ohio]]"
  - "[[Northrup v. City of Toledo Police Dept]]"
  - "[[United States v. Black]]"
  - "[[Adams v. Williams]]"
tags:
  - case
  - fourth-amendment
  - terry-stop
  - frisk
  - reasonable-suspicion
  - armed-and-dangerous
  - circuit-split
holding: "An officer who makes a lawful traffic stop and who reasonably suspects that one of the vehicle's occupants is armed may frisk that person for weapons without separately establishing that the person is dangerous, even where state law would allow the person to carry a concealed firearm; the danger justifying a protective frisk arises from the combination of a forced police encounter and the presence of a weapon, not from any illegality in the weapon's possession."
aliases:
  - "United States v. Robinson (4th Cir. en banc)"
  - "United States v. Robinson (4th Cir. 2017)"
  - United States v. Shaquille Robinson
---

# United States v. Robinson (4th Cir. en banc)

*846 F.3d 694 (4th Cir. 2017)* · U.S. Court of Appeals for the Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4340460 → en banc majority opinion 9871494 (Niemeyer, Circuit Judge, for the en banc court; 846 F.3d 694, decided Jan. 23, 2017). Caption disambiguated (worklist): the 4th Cir. en banc United States v. Shaquille Robinson, distinct from the SCOTUS search-incident United States v. Robinson (1973). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*696`). Frontier-split row (role: Illustrates a circuit split): in-circuit binding, persuasive elsewhere; the split posture is named in Treatment (LINT-21). S9 promotes. -->

## Background
Acting on an anonymous tip that a man in a Toyota Camry had loaded a firearm and concealed it in his pocket in a high-crime 7-Eleven parking lot in Ranson, West Virginia, police stopped the car for a seatbelt violation. Reasonably believing the passenger, Shaquille Robinson, was armed, an officer frisked him and found the gun; because Robinson was a felon, he was arrested for illegal possession of a firearm. Robinson moved to suppress, arguing the officers had no articulable basis to think he was *dangerous* — since West Virginia allows people to obtain permits to carry concealed firearms, being armed did not make him a threat. The district court denied suppression; Robinson pleaded guilty conditionally, a panel reversed, and the Fourth Circuit reheard the case [[Reading and Citing Cases#en-banc|en banc]].

## Issue
Whether an officer who lawfully stops a person and reasonably believes that person is armed may conduct a protective frisk, or whether — in a jurisdiction that permits carrying a concealed firearm — the officer must additionally have reasonable suspicion that the person is dangerous.

## Rule
The [[Reading and Citing Cases#en-banc|en banc]] court held that reasonable suspicion the stopped person is armed is enough; lawful eligibility to carry the weapon does not dissolve the risk. It held: "We reject Robinson's argument and affirm, concluding that an officer who makes a lawful traffic stop and who has a reasonable suspicion that one of the automobile's occupants is armed may frisk that individual for the officer's protection and the safety of everyone on the scene." — 846 F.3d at 696. ^pin-696

## Application
Reasoning from *[[Terry v. Ohio|Terry]]*, *[[Pennsylvania v. Mimms]]*, and *[[Adams v. Williams]]*, the court explained that the danger justifying a frisk arises from the combination of a forced police encounter and the presence of a weapon — not from any illegality in possessing it. It was therefore inconsequential that Robinson was a passenger, or that he might have been entitled to a concealed-carry permit: an officer forced into close quarters with an armed person need not "take unnecessary risks" by assuming the weapon poses no threat. The frisk was reasonable, and suppression was properly denied.

## Conclusion
The denial of Robinson's suppression motion was **affirmed**. Niemeyer, Circuit Judge, wrote for the [[Reading and Citing Cases#en-banc|en banc]] majority (ten judges joining). Wynn, J., concurred in the judgment; Harris, J., dissented, joined by Gregory, C.J., and Motz and Davis, JJ.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion.

**Illustrates a circuit split (in-circuit rule).** *Robinson* is the Fourth Circuit's [[Reading and Citing Cases#en-banc|en banc]] answer — binding there, persuasive only elsewhere — that a lawfully stopped person reasonably believed to be *armed* may be frisked without a separate showing of *dangerousness*, even in a right-to-carry jurisdiction. That reading divides the courts: the [[Common Legal Terms#dissenting-opinion|dissent]] and other authorities treat *[[Terry v. Ohio|Terry]]*'s "armed *and* dangerous" formula as requiring an independent basis to believe the person is dangerous, so that lawful gun possession alone cannot justify a frisk. It sits on the opposite side of the split from *[[Northrup v. City of Toledo Police Dept]]* (6th Cir.) and the reasoning of *[[United States v. Black]]*, which hold that lawful firearm possession, standing alone, does not supply the suspicion of dangerousness the Fourth Amendment requires. Teach *Robinson* as one pole of that split, not a nationally settled rule.

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Illustrates a circuit split*

## Sources
- [*United States v. Robinson*, 846 F.3d 694 (4th Cir. 2017) (en banc)](https://www.courtlistener.com/opinion/4340460/united-states-v-shaquille-robinson/) — pinpoint: 696 (Niemeyer, J., for the en banc court; the CL opinion text carries the reporter star `*696` immediately before the paragraph containing the quoted holding). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "928b1b78c616c746", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Robinson (4th Cir. en banc)"}, "payload": {"all": [{"cite": "846 F.3d 694", "page": "694", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "846"}, {"cite": "2017 WL 280727", "page": "280727", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2017"}, {"cite": "2017 U.S. App. LEXIS 1134", "page": "1134", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2017"}], "display": "846 F.3d 694", "official": {"cite": "846 F.3d 694", "page": "694", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "846"}, "official_selection_present": true, "record_id": "United States v. Robinson (4th Cir. en banc)"}}
{"assertion_id": "7adf3189b1f0061a", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Robinson (4th Cir. en banc)"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Robinson (4th Cir. en banc)", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Robinson (4th Cir. en banc)

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Robinson (4th Cir. en banc)",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Shaquille Robinson",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Shaquille Montel ROBINSON, Defendant-Appellant",
    "input_case_name": "United States v. Robinson (4th Cir. en banc)",
    "court": "U.S. Court of Appeals, 4th Cir. (en banc)",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca4",
    "state": null,
    "date_decided": null,
    "year": 2017,
    "docket": "No. 14-4902",
    "cluster_id": 4340460,
    "lead_opinion_id": 9871494,
    "sibling_ids": [],
    "absolute_url": "/opinion/4340460/united-states-v-shaquille-robinson/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": false,
    "alternates": [],
    "reason_code": "caption_mismatch_accepted_by_case_name"
  },
  "citations": {
    "official": {
      "cite": "846 F.3d 694",
      "volume": "846",
      "reporter": "F.3d",
      "page": "694",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2017 WL 280727",
        "volume": "2017",
        "reporter": "WL",
        "page": "280727",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 U.S. App. LEXIS 1134",
        "volume": "2017",
        "reporter": "U.S. App. LEXIS",
        "page": "1134",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "846 F.3d 694",
        "volume": "846",
        "reporter": "F.3d",
        "page": "694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 WL 280727",
        "volume": "2017",
        "reporter": "WL",
        "page": "280727",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 U.S. App. LEXIS 1134",
        "volume": "2017",
        "reporter": "U.S. App. LEXIS",
        "page": "1134",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "846 F.3d 694",
    "official_selection": {
      "court_class": "coa",
      "selected": "846 F.3d 694",
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
    "date_created": "2026-07-06T13:41:21Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [
      "input caption does not match CL canonical caption",
      "frontier identity accepted by case_name rung despite caption mismatch"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:41:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:41:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-robinson-4th-cir-en-banc--4340460",
      "to_record_id": "United States v. Robinson (4th Cir. en banc)",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Robinson (4th Cir. en banc)

```
<opinion type="majority">
<p id="b717-10">Affirmed by published opinion. Judge NIEMEYER wrote the majority opinion, in which Judge WILKINSON, Judge TRAXLER, Judge KING, Judge SHEDD, Judge DUNCAN, Judge AGEE, Judge KEENAN, Judge DIAZ, Judge FLOYD, and Judge THACKER joined. Judge WYNN wrote a separate opinion concurring in the judgment. Judge HARRIS wrote a dissenting opinion, in which Chief Judge GREGORY, Judge MOTZ, and Senior Judge DAVTS joined.</p>
<p id="b717-12">ON REHEARING EN BANC</p>
<author id="b717-13">NIEMEYER, Circuit Judge:</author>
<p id="b717-14">This appeal presents the question of whether a law enforcement officer is justified, in frisking a person whom the officer has lawfully stopped and whom the officer reasonably believes to be armed, regardless of whether the person may legally be entitled to carry the firearm. Stated otherwise, the question is whether the risk of danger to a law enforcement officer created by the forced stop of a person who is armed is eliminated by the fact that state law authorizes persons to obtain a permit to carry a concealed firearm.</p>
<p id="b717-15">After receiving a tip that a man in a parking lot well known for drug-trafficking activity had just loaded a firearm and then concealed it in his pocket before getting into a car as a passenger, Ranson, West Virginia police stopped the ear after observing that its occupants were not wearing seatbelts. Reasonably believing that the car’s passenger, • Shaquille Robinson, was armed, the police frisked him and uncovered the firearm, leading to his arrest for the possession of a firearm by a felon. .</p>
<p id="b717-16">During his prosecution, Robinson filed a motion to suppress the evidence recovered as a result of the frisk, contending that the frisk violated . his Fourth Amendment rights. The' officers, he argued, had no articulable facts demonstrating that he was dangerous since, as far as the officers knew, the State could have issued him a permit to earry a concealed firearm. After the district court denied the motion to suppress, Robinson pleaded guilty to the illegal possession of a firearm, reserving <page-number citation-index="1" label="696">*696</page-number>the right to appeal the denial of his motion to suppress.</p>
<p id="b718-4">On appeal, Robinson contends again that the information that police received from the tip described seemingly innocent conduct and that his conduct at the time of the traffic stop also provided no basis for officers to reach the conclusion that he was dangerous. He argues, “Under the logic of the district court, in any state where carrying a firearm is a perfectly legal activity, every citizen could be dangerous, and subject to a <em>Terry </em>frisk and pat down.”</p>
<p id="b718-5">We reject Robinson’s argument and affirm, concluding that an officer who makes a lawful traffic stop and who has a reasonable suspicion that one of the automobile’s occupants is armed may frisk that individual for the officer’s protection and the safety of everyone on the scene. <em>See Pennsylvania v. Mimms, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#112" aria-description="Citation for case: Pennsylvania v. Mimms">434 U.S. 106, 112</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">54 L.Ed.2d 331</a></span> (1977) (per curiam). The Fourth Amendment does not “require ... police officers [to] take unnecessary risks in the performance of their duties.” <em>Terry v. Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#23" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1, 23</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968). And it is inconsequential that the person thought to be armed was a passenger. <em>See Maryland v. Wilson, </em><span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#414" aria-description="Citation for case: Maryland v. Wilson">519 U.S. 408, 414</a></span>, <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">117 S.Ct. 882</a></span>, <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">137 L.Ed.2d 41</a></span> (1997). It is also inconsequential that the passenger may have had a permit to carry the concealed firearm. The danger justifying a protective frisk arises from the combination of a forced police encounter and the presence of a weapon, not from any illegality of the weapon’s possession. <em>See Adams v. Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U.S. 143, 146</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">92 S.Ct. 1921</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">32 L.Ed.2d 612</a></span> (1972); <em>Michigan v. Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U.S. 1032</a></span>, 1052 n.16, <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">103 S.Ct. 3469</a></span>, <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">77 L.Ed.2d 1201</a></span> (1983).</p>
<p id="b718-6">I</p>
<p id="b718-7">The material facts in this case are not disputed. At about 3:55 p.m. on March 24, 2014, an unidentified man called the Ran-son, West Virginia Police Department and told Officer Crystal Tharp that he had just “witnessed a black male in a bluish greenish Toyota Camry load a firearm [and] conceal it in his pocket” while in the parking lot of the 7-Eleven on North Mildred Street. The caller advised Officer Tharp that the Camry was being driven by a white woman and had “just left” the parking lot, traveling south on North Mildred Street.</p>
<p id="b718-9">The 7-Eleven on North Mildred Street is adjacent to the Apple Tree Garden Apartments, and the area constitutes the highest crime area in Ranson. One officer who testified said that in his short one and a half years as a state trooper, he had experience with at least 20 incidents of drug trafficking in the 7-Eleven parking lot. Another officer testified that “when [she] was doing drug work[,] ... [she] dropped an informant off to buy drugs” at the 7-Eleven parking lot and observed “three other people waiting for drugs in that parking lot.” She added that she had personally received “numerous complaints” of people running between the parking lot and the apartment complex, making drug transactions. Another officer testified that “[a]nytime you hear Apple Tree or 7-Elev-en, your radar goes up a notch.” Accordingly, when the Ranson Police Department received the tip about someone loading a gun in the 7-Eleven parking lot, its officers’ “radar [went] up a notch,” and the officers went “on heightened alert.”</p>
<p id="b718-10">While still on the telephone with the caller, Officer Tharp relayed the information to Officer Kendall Hudson and Captain Robbie Roberts. Hudson immediately left the station to respond to the call, and Roberts left soon thereafter to provide backup.</p>
<p id="b719-4"><page-number citation-index="1" label="697">*697</page-number>When Officer Hudson turned onto North Mildred Street a short time later, he observed a blue-green Toyota Camry being driven by a white woman with a black male passenger. Noticing that they were not wearing seatbelts, Hudson effected a traffic stop approximately seven blocks, or three-quarters of a mile, south of the 7-Eleven. He estimated that the traffic stop took place two to three minutes after the call had been received at the station.</p>
<p id="b719-5">After calling in the stop, Officer Hudson approached the driver’s side of the vehicle with his weapon drawn but carried below his waist and asked the driver for her license, registration, and proof of insurance. He also asked the male passenger, the defendant Robinson, for his identification but quickly realized that doing so was “probably not a good idea” because “[t]his guy might have a gun[,] [and] I’m asking him to get into his pocket to get his I.D.” Instead, Officer Hudson asked Robinson to step out of the vehicle.</p>
<p id="b719-6">At this point, Captain Roberts arrived and opened the front passenger door. As Robinson was exiting the vehicle, Captain Roberts asked him if he had any weapons on him. Instead of responding verbally, Robinson “gave [Roberts] a weird look” or, more specifically, an “‘oh, crap’ look[].” Roberts took the look to mean, “I don’t want to lie to you, but I’m not going to tell you anything [either].” At this point, Captain Roberts directed Robinson to put his hands on top of the car and performed a frisk for weapons, recovering a loaded gun from the front pocket of Robinson’s pants. After conducting the frisk, Roberts recognized Robinson, recalled that he had previously been convicted of a felony, and arrested him.</p>
<p id="b719-7">After Robinson was charged with the illegal possession of a firearm by a felon, in violation of <span class="citation no-link">18 U.S.C. § 922</span>(g)(1), he filed a motion to suppress the evidence of the firearm and ammunition seized during the frisk, arguing that the frisk violated his Fourth Amendment rights.</p>
<p id="b719-9">The district court denied the motion, concluding that the officers possessed reasonable suspicion to believe that Robinson was armed and dangerous. Relying on <em>Navarette v. California, </em>— U.S. —, <span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">134 S.Ct. 1683</a></span>, <span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">188 L.Ed.2d 680</a></span> (2014), the court concluded that the anonymous caller’s eyewitness knowledge and the contemporaneous nature of the report indicated that the tip was sufficiently reliable to contribute to the officers’ reasonable suspicion. The court explained that the “anonymous tip that [Robinson] [had] recently loaded a firearm and concealed it on his person in a public parking lot in a high-crime area,” as well as Robinson’s “weird look and failure to verbally respond to the inquiry whether he was armed,” gave rise to a reasonable suspicion that Robinson was armed and dangerous.</p>
<p id="b719-11">Robinson thereafter pleaded guilty to the firearm possession charge, reserving his right to appeal the district court’s denial of his suppression motion, and the district court sentenced him to 37 months’ imprisonment. Robinson appealed the denial of his motion to suppress, and a panel of this court reversed the district court’s decision denying Robinson’s motion to suppress and vacated his conviction and sentence. <em>United States v. Robinson, </em><span class="citation" data-id="9821731"><a href="/opinion/3179638/united-states-v-shaquille-robinson/#213" aria-description="Citation for case: United States v. Shaquille Robinson">814 F.3d 201, 213</a></span> (4th Cir. 2016). By order dated April 25, 2016, we granted the government’s petition for rehearing <em>en banc, </em>which vacated the panel’s judgment and opinion. <em>See </em>4th Cir. Local R. 35(c).</p>
<p id="b719-12">II</p>
<p id="b719-13">Robinson’s appeal is defined as much by what he concedes as by what he challenges. Robinson rightfully acknowledges that the Ranson police had the right to <page-number citation-index="1" label="698">*698</page-number>stop the vehicle in which he was a passenger after observing a traffic violation, <em>see Whren v. United States, </em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#819" aria-description="Citation for case: Whren v. United States">517 U.S. 806, 819</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S.Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L.Ed.2d 89</a></span> (1996), and also that they had the authority to direct him to exit the vehicle during the valid traffic stop, <em>see Wilson, </em><span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#415" aria-description="Citation for case: Maryland v. Wilson">519 U.S. at 415</a></span>, <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">117 S.Ct. 882</a></span>. He also correctly concedes that the anonymous tip received by the Ranson Police Department was sufficiently reliable to justify the officers’ reliance on it. <em>See Navarette, </em><span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/#1688" aria-description="Citation for case: Prado Navarette v. California">134 S.Ct. at 1688-89</a></span> (concluding that an anonymous 911 call “bore adequate indicia of reliability for the officer to credit the caller’s account” in large part because, like here, the caller “claimed eyewitness knowledge of the alleged [conduct]” and the call was a “contemporaneous report” that was “made under the stress of excitement caused by a startling event”). Finally, and most importantly, Robinson does not contest the district court’s conclusion that the police had reasonable suspicion to believe that he was armed.</p>
<p id="b720-6">Robinson’s argument focuses on whether the officers could reasonably have suspected that he was dangerous. He argues that while the officers may well have had good reason to suspect that he was carrying a loaded concealed firearm, they lacked objective facts indicating <em>that he was also dangerous, </em>so as to justify a frisk for weapons, since an officer must reasonably suspect that the person being frisked is both armed <em>and </em>dangerous. <em>See Terry, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 27</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>. Robinson notes that at the time of the frisk, West Virginia residents could lawfully carry a concealed firearm if they had received a license from the State. <em>See </em><span class="citation no-link">W. Va. Code § 61-7-3</span> to -4 (2014). And, because the police did not know whether or not he possessed such a license, the tip that a suspect matching his description was carrying a loaded firearm concealed in his pocket was, he argues, a report of <em>innocent behavior </em>that was not sufficient to indicate that he posed a danger to others. Moreover, he argues, his behavior during the stop did not create suspicion—“he was compliant, cooperative, [and] not displaying signs of nervousness.” In these circumstances, he concludes, the officer’s frisk was not justified by any reasonable suspicion that he was <em>dangerous.</em></p>
<p id="AlV">Robinson’s argument presumes that the legal possession of a firearm cannot pose a danger to police officers during a forced stop, and it collapses the requirements for making a stop with the requirements for conducting a frisk. It thus fails at several levels when considered under the Supreme Court’s “stop-and-frisk” jurisprudence. First, Robinson confuses the standard for making stops—which requires a reasonable suspicion <em>that a crime or other infraction has been or is being </em>committed—with the standard for conducting a frisk—which requires both a lawful investigatory stop and a reasonable suspicion <em>that the person stopped is armed and dangerous. See Arizona v. Johnson, </em><span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/#326" aria-description="Citation for case: Arizona v. Johnson">555 U.S. 323, 326-27</a></span>, <span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">129 S.Ct. 781</a></span>, <span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">172 L.Ed.2d 694</a></span> (2009). Second, he fails to recognize that traffic stops alone are inherently dangerous for police officers. Third, he also fails to recognize that traffic stops of persons who are armed, whether legally or illegally, pose yet a greater safety risk to police officers. And fourth, he argues illogically that when a person forcefully stopped may be <em>legally </em>permitted to possess a firearm, any risk of danger to police officers posed by the firearm is eliminated.</p>
<p id="b720-9">We begin by noting that the Supreme Court has repeatedly recognized that whenever police officers use their authority to effect a stop, they subject themselves to a risk of harm. This holds true whether the temporary detention is a traditional, <page-number citation-index="1" label="699">*699</page-number>“on-the-street” <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop to investigate an officer’s reasonable suspicion “that the person apprehended is committing or has committed a criminal offense,” <em>Johnson, </em><span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/#326" aria-description="Citation for case: Arizona v. Johnson">555 U.S. at 326</a></span>, <span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">129 S.Ct. 781</a></span>, or a stop of a motor vehicle and all of its occupants to enforce a jurisdiction’s traffic laws, <span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/#327" aria-description="Citation for case: Arizona v. Johnson"><em>id. </em>at 327</a></span>,<span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">129 S.Ct. 781</a></span>. The. Supreme Court has explained that “the risk of a violent encounter in a traffic-stop setting ‘stems not from the ordinary reaction of a motorist stopped for a speeding violation, but from the fact that evidence of a more serious crime might be uncovered during the stop.’” <span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/#331" aria-description="Citation for case: Arizona v. Johnson"><em>Id. </em>at 331</a></span>, <span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">129 S.Ct. 781</a></span> (quoting <em>Wilson, </em><span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#414" aria-description="Citation for case: Maryland v. Wilson">519 U.S. at 414</a></span>, <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">117 S.Ct. 882</a></span>); <em>see also Mimms, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#110" aria-description="Citation for case: Pennsylvania v. Mimms">434 U.S. at 110</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330</a></span> (rejecting “the argument that traffic violations necessarily involve less danger to officers than other types of confrontations”). Indeed, the Court has concluded that traffic stops are “especially fraught with danger to police officers.” <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1047" aria-description="Citation for case: Michigan v. Long">463 U.S. at 1047</a></span>, <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">103 S.Ct. 3469</a></span>. And the Court has also observed that when the stop involves one or more passengers, that fact “increases the possible sources of harm to the officer,” <em>Wilson, </em><span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#413" aria-description="Citation for case: Maryland v. Wilson">519 U.S. at 413</a></span>, <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">117 S.Ct. 882</a></span>, as “the motivation of a passenger to employ violence ... is every bit as great as that of the driver,” <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#414" aria-description="Citation for case: Maryland v. Wilson"><em>id. </em>at 414</a></span>,<span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">117 S.Ct. 882</a></span>.</p>
<p id="b721-4">In <em><span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">Wilson</a></span>, </em>the Court observed that “[i]n 1994 alone, there were 5,762 officer assaults and 11 officers killed during traffic pursuits and stops,” <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#413" aria-description="Citation for case: Maryland v. Wilson">519 U.S. at 413</a></span>, <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">117 S.Ct. 882</a></span>, prompting the Court to conclude that the public interest in police officer safety during traffic stops is “both legitimate and weighty,” <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#412" aria-description="Citation for case: Maryland v. Wilson"><em>id. </em>at 412</a></span>, <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">117 S.Ct. 882</a></span> (quoting <em>Mimms, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#110" aria-description="Citation for case: Pennsylvania v. Mimms">434 U.S. at 110</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330</a></span>). And more recent statistics, unfortunately, remain as grim. Of the 51 law enforcement officers feloniously killed in the line of duty in 2014, 9 officers (or 18%) were fatally injured during traffic pursuits or stops. FBI, <em>Officers Feloniously Killed, in </em>Uniform Crime Reports: Law Enforcement Officers Killed and Assaulted, 2014.</p>
<p id="b721-7">To be clear, the general risk that is inherent during a traffic stop does not, without more, justify a frisk of the automobile’s occupants. But the risk inherent in all .traffic stops is heightened exponentially when.the person who has been stopped—a person whose propensities are unknown— is “armed with - a weapon that could unexpectedly and fatally be used against” the officer in a matter of seconds. <em>Terry, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#23" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 23</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>. As such, when the officer reasonably suspects that the person he has stopped is armed, the officer is “warranted in the belief that his safety ... [is] in danger,” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><em>id. </em>at 27</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, thus justifying a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>frisk.</p>
<p id="b721-8">In <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>Officer McFadden “seized” Terry on the street and subjected him to a “search” without probable cause to believe that he had committed or was committing a crime or that he was armed, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 19</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>. The Court was thus confronted with two distinct constitutional issues: <em>first, </em>whether a person could be stopped (seized) on suspicion of criminal conduct that fell short of probable cause; and <em>second, </em>whether the officer could conduct a protective frisk or “pat down” for weapons (search) during the stop. The Court .readily concluded that Terry’s seizure was “reasonable” under the Fourth Amendment because the officer reasonably believed that criminal conduct was afoot. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio"><em>Id. </em>at 22-23</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>. The Court then turned its attention to the legality of the frisk, stating, “We are now concerned with more than the governmental interest in investigating crime; in addition, there is the more immediate interest of the police officer in taking steps to assure himself that the person with whom he is dealing is not armed with a weapon that could-unexpectedly and fatally be used against him.” <page-number citation-index="1" label="700">*700</page-number><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#23" aria-description="Citation for case: Terry v. Ohio"><em>Id. </em>at 23</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>. The <em>concern—i.e., </em>the danger—was thus found in <em>the presence of a weapon during a forced police encounter. </em>Indeed, the Court said as much, noting in approving Officer McFadden’s frisk of Terry that “a reasonably prudent man would have been warranted in believing petitioner was armed <em>and thus presented a threat to the officer’s safety.” Id. </em>at 28, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span> (emphasis added). In this manner, the Court adopted the now well-known standard that an officer can frisk a validly stopped person if the officer reasonably believes that the person is “armed and dangerous.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><em>Id. </em>at 27</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>; <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#32" aria-description="Citation for case: Terry v. Ohio"><em>see also id. </em>at 32</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span> (Harlan, J., concurring) (explaining that because a “frisk is justified in order to protect the officer during an encounter with a citizen, the officer must first have constitutional grounds to insist on an encounter, to make a forcible stop”).</p>
<p id="b722-4">The Supreme Court applied <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>to circumstances analogous to those before us in <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span>, </em>where an officer, after making a routine traffic stop, “noticed a large bulge” under the defendant’s jacket and therefore conducted a frisk. <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#107" aria-description="Citation for case: Pennsylvania v. Mimms">434 U.S. at 107</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330</a></span>. Holding that the frisk was clearly justified, the <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span> </em>Court explained that “[t]he bulge in the jacket permitted the officer to conclude that Mimms was armed <em>and thus posed a serious and present danger to the safety of the officer,” </em>adding that “[i]n these circumstances, any man of ‘reasonable caution’ would likely have conducted the ‘pat down.’ ” <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#112" aria-description="Citation for case: Pennsylvania v. Mimms"><em>Id. </em>at 112</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330</a></span> (emphasis added). The only evidence of Mimms’ dangerousness was the bulge indicating that he was armed. <em>See <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">id.</a></span> </em>It was thus Mimms’ status of being armed during a forced police encounter (the traffic stop) that posed the danger justifying the frisk, and we have previously relied on <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span> </em>for that precise principle. <em>See United States v. Baker, </em><span class="citation" data-id="714150"><a href="/opinion/714150/united-states-v-anthony-marcellus-baker/#137" aria-description="Citation for case: United States v. Anthony Marcellus Baker">78 F.3d 135, 137</a></span> (4th Cir. 1996) (citing <em>Mimms, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#112" aria-description="Citation for case: Pennsylvania v. Mimms">434 U.S. at 112</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330</a></span>) (“Based on the inordinate risk of danger to law enforcement officers during traffic stops, observing a bulge that could be made by a weapon in a suspect’s clothing reasonably warrants a belief that the suspect is potentially dangerous, even if the suspect was stopped only for a minor violation”).</p>
<p id="b722-6">In short, established Supreme Court law imposes two requirements for conducting a frisk, but no more than two: <em>first, </em>that the officer have conducted a lawful stop, which includes both a traditional <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop as well as a traffic stop; and <em>second, </em>that during the valid but forced encounter, the officer reasonably suspect that the person is <em>armed and therefore dangerous. </em>In both Terry. and <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span>, </em>the Court deliberately linked “armed” and “dangerous,” recognizing that the frisks in those cases were lawful because the stops were valid and the officer reasonably believed that the person stopped “was armed <em>and thus” </em>dangerous. <em>Terry, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#28" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 28</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span> (emphasis added); <em>Mimms, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#112" aria-description="Citation for case: Pennsylvania v. Mimms">434 U.S. at 112</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330</a></span> (emphasis added). The use of “and thus” recognizes that the risk of danger is created simply because the person, who was forcibly stopped, is armed.</p>
<p id="b722-7">In this case, both requirements—a lawful stop and a reasonable suspicion that Robinson was armed—were satisfied, thus justifying Captain Roberts’ frisk under the Fourth Amendment as a matter of law.</p>
<p id="b722-8">Robinson argues that <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span> </em>is distinguishable because the frisk there took place in a jurisdiction that made it a crime to carry a concealed deadly weapon. West Virginia, on the other hand, generally permits its citizens to carry firearms. From this distinction, Robinson argues that when the person forcibly stopped may be <em>legally </em>permitted to possess a firearm, the <page-number citation-index="1" label="701">*701</page-number>risk of danger posed by the firearm is eliminated. This argument, however, fails under the Supreme Court’s express recognition that the legality of the frisk does not depend on the illegality of the firearm’s possession. Indeed, the Court has twice explained that “[t]he purpose of this limited search <em>[ie., </em>the frisk] is not to discover evidence of crime, but to allow the officer to pursue his investigation without fear of violence, and thus the frisk for weapons might be equally necessary and reasonable, <em>whether or not carrying a concealed weapon violated any applicable state law” Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U.S. at 146</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">92 S.Ct. 1921</a></span> (emphasis added); <em>see also Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U.S. at 1052</a></span> n.16, <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">103 S.Ct. 3469</a></span> (“[W]e have expressly rejected the view that the validity of a <em>Temj </em>search <em>[ie., </em>a frisk] depends on whether the weapon is possessed in accordance with state law”). Robinson’s position directly conflicts with these observations.</p>
<p id="b723-5">Notwithstandipg the Supreme Court’s statements, Robinson’s position also fails as a matter of logic to recognize that the risk inherent in a forced stop of a person who is armed exists even when the firearm is legally possessed. The presumptive lawfulness of an individual’s gun possession in a particular State does next to nothing to negate the reasonable concern an officer has for his own safety when forcing an encounter with an individual who is armed with a gun and whose propensities are unknown. <em>See United States v. Rodriguez, </em><span class="citation" data-id="2647900"><a href="/opinion/2647900/united-states-v-rodriguez/#491" aria-description="Citation for case: United States v. Rodriguez">739 F.3d 481, 491</a></span> (10th Cir. 2013) (concluding that “an officer making a lawful investigatory stop [must have] the ability to protect himself from an armed suspect whose propensities are unknown” and therefore rejecting the defendant’s argument that the officer “had no reason to believe he was dangerous” even though the officer had seen a handgun tucked into the waistband of his pants).</p>
<p id="A_1">Accordingly, we conclude that given Robinson’s concession that he was lawfully stopped and that the police officers had reasonable suspicion to believe that he was armed, the officers were, as a matter of law, justified in frisking him and, in doing so, did not violate Robinson’s Fourth Amendment rights.</p>
<p id="b723-7">Ill</p>
<p id="b723-8">While the lawful traffic stop of Robinson and the reasonable suspicion that he was armed justified the frisk in this case, the officers had knowledge of additional facts that increased the level of their suspicion that Robinson was dangerous.</p>
<p id="b723-9">First, the reliable tip in this case was not just that an individual matching Robinson’s description possessed a firearm. Rather, the caller reported that he had observed an individual “load a firearm [and] conceal it in his pocket” while in the parking lot of the 7-Eleven on North Mildred Street, a location that the officers knew to be a popular spot for drug-trafficking activity. Four officers testified about the high level of drug-trafficking and other criminal activity in that particular parking lot, prompting one to explain, “[a]nytime you hear ... 7-Eleven, your radar goes up a notch.” Knowing that the 7-Eleven parking lot was frequently used as a site for drug trafficking, a reasonable officer could legitimately suspect that an individual who was seen both loading and concealing a firearm in that very parking lot may well have been doing so in connection with drug-trafficking activity, making his possession of a firearm even more dangerous. <em>See United States v. Lomax, </em><span class="citation" data-id="778011"><a href="/opinion/778011/united-states-v-clarence-j-lomax/#705" aria-description="Citation for case: United States v. Clarence J. Lomax">293 F.3d 701, 705</a></span> (4th Cir. 2002) (recognizing the “numerous ways in which a firearm might further or advance drug trafficking”).</p>
<p id="b723-10">Second, when Captain Roberts asked Robinson, as he was getting out of the car, <page-number citation-index="1" label="702">*702</page-number>whether he was carrying any firearms, Robinson failed to respond verbally and instead gave the officer an ‘“oh, crap’ look[],” which Roberts took to mean, “I don’t want to lie to you, but I’m not going to tell you anything [either].” Surely, Robinson’s evasive response further heightened Captain Roberts’ legitimate concern as to the dangerousness of the situation.</p>
<p id="b724-4">While not necessary to the conclusion in this case, these facts can only confirm Captain Roberts’ reasonable suspicion that Robinson was dangerous and therefore should be frisked for the protection of the officer and all others present. Indeed, in light of all of the circumstances known to Captain Roberts, he would unquestionably have been criticized for not conducting a frisk if, after having failed to do so, something untoward had happened.</p>
<p id="pAjI">[[Image here]]</p>
<p id="b724-5">The judgment of the district court is accordingly</p>
<p id="AJ3b">
<em>AFFIRMED.</em>
</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Robinson.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "United States v. Robinson"
type: case
citation: "414 U.S. 218 (1973)"
parallel_cite: "94 S. Ct. 467; 38 L. Ed. 2d 427; 66 Ohio Op. 2d 202"
neutral_cite: 1973 U.S. LEXIS 21
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1973
date_decided: 1973-12-11
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1973-12-11
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Robinson
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108893/united-states-v-robinson/"
  cluster_id: 108893
  opinion_id: 9425474
  identity_checked: true
homes:
  - page: "[[SIA Persons]]"
    role: "Key — Anchor"
related: ["[[Chimel v. California]]", "[[Arizona v. Gant]]", "[[Riley v. California]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "full-custody-arrest", "bright-line-rule"]
holding: "A lawful custodial arrest categorically authorizes a full search of the arrestee's person; the search needs no additional justification…"
lake:
  record_id: United States v. Robinson
  status: verified
  projected_at: 2026-07-06
---

# United States v. Robinson

*414 U.S. 218 (1973)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An officer lawfully arrested Robinson on a full-custody basis for operating a motor vehicle after revocation of his driver's license. Searching Robinson incident to the arrest, the officer felt an object in Robinson's coat pocket, removed a crumpled cigarette package, opened it, and found heroin capsules. Robinson moved to suppress, arguing the search went beyond what was needed to protect the officer or to preserve evidence of the license offense.

## Issue
Whether, incident to a lawful custodial arrest, an officer may conduct a full search of the arrestee's person without additional justification — even with no particular reason to believe the search will produce weapons or evidence of the crime of arrest.

## Rule
Yes. "A custodial arrest of a suspect based on probable cause is a reasonable intrusion under the Fourth Amendment; that intrusion being lawful, a search incident to the arrest requires no additional justification. It is the fact of the lawful arrest which establishes the authority to search, and we hold that in the case of a lawful custodial arrest a full search of the person is not only an exception to the warrant requirement of the Fourth Amendment, but is also a 'reasonable' search under that Amendment." — 414 U.S. at 235. ^pin-235

The authority to search the person is automatic upon a lawful custodial arrest; it does not depend on a case-by-case judgment that weapons or evidence would in fact be found in the particular situation.

## Application
The officer made a lawful full-custody arrest of Robinson for driving after revocation of his license. Searching him incident to that arrest, the officer found a crumpled cigarette package, opened it, and discovered heroin. Because the arrest was lawful and custodial, the full search of Robinson's person — including opening the cigarette package — required no further justification and was reasonable; that the search was unlikely to yield weapons or evidence of the license offense was immaterial.

## Conclusion
The search of Robinson's person and the seizure of the heroin were valid as incident to a lawful custodial arrest; the Supreme Court reversed the Court of Appeals.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Robinson* states the [[Common Legal Terms#bright-line-rule|bright-line rule]] for searches of the person incident to a custodial arrest. [[Riley v. California]] later declined to extend that automatic-search authority to the **digital contents of a cell phone** (those require a warrant), and [[Arizona v. Gant]] cabined vehicle [[Search Incident to Arrest|searches incident to arrest]] — but neither disturbs *Robinson*'s rule for a full search of the arrestee's person and physical effects.

## Appears on
- [[SIA Persons]] — *Key — Anchor*

## Sources
- *United States v. Robinson*, 414 U.S. 218 (1973) — https://www.courtlistener.com/opinion/108893/united-states-v-robinson/ — pinpoint: 235 (parallel 94 S. Ct. 467).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6a833943ef450ae0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Robinson"}, "payload": {"all": [{"cite": "414 U.S. 218", "page": "218", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "414"}, {"cite": "94 S. Ct. 467", "page": "467", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "94"}, {"cite": "38 L. Ed. 2d 427", "page": "427", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "38"}, {"cite": "1973 U.S. LEXIS 21", "page": "21", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1973"}, {"cite": "66 Ohio Op. 2d 202", "page": "202", "reporter": "Ohio Op. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "66"}], "display": "414 U.S. 218", "official": {"cite": "414 U.S. 218", "page": "218", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "414"}, "official_selection_present": true, "record_id": "United States v. Robinson"}}
{"assertion_id": "595c7404e13e9aba", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-235", "record_id": "United States v. Robinson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-235", "pinpoint_status": "slip-only", "quote": "--- # United States v. Robinson *414 U.S. 218 (1973)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An officer lawfully arrested Robinson on a full-custody basis for operating a motor vehicle after revocation of his driver's license. Searching Robinson incident to the arrest, the officer felt an object in Robinson's coat pocket, removed a crumpled cigarette package, opened it, and found heroin capsules. Robinson moved to suppress, arguing the search went beyond what was needed to protect the officer or to preserve evidence of the license offense. ## Issue Whether, incident to a lawful custodial arrest, an officer may conduct a full search of the arrestee's person without additional justification — even with no particular reason to believe the search will produce weapons or evidence of the crime of arrest. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "United States v. Robinson", "star_marker": null}}
{"assertion_id": "4a029504203c3615", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Robinson"}, "payload": {"as_of_content": "1973-12-11", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Robinson", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Robinson

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Robinson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Robinson",
    "case_name_short": "Robinson",
    "case_name_full": "United States v. Robinson",
    "input_case_name": "United States v. Robinson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1973-12-11",
    "year": 1973,
    "docket": null,
    "cluster_id": 108893,
    "lead_opinion_id": 9425474,
    "sibling_ids": [
      108893,
      9425474,
      9425475,
      9425476
    ],
    "absolute_url": "/opinion/108893/united-states-v-robinson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "414 U.S. 218",
      "volume": "414",
      "reporter": "U.S.",
      "page": "218",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "94 S. Ct. 467",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "467",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "38 L. Ed. 2d 427",
        "volume": "38",
        "reporter": "L. Ed. 2d",
        "page": "427",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "66 Ohio Op. 2d 202",
        "volume": "66",
        "reporter": "Ohio Op. 2d",
        "page": "202",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1973 U.S. LEXIS 21",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "21",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "414 U.S. 218",
        "volume": "414",
        "reporter": "U.S.",
        "page": "218",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 S. Ct. 467",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "467",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "38 L. Ed. 2d 427",
        "volume": "38",
        "reporter": "L. Ed. 2d",
        "page": "427",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. LEXIS 21",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "21",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "66 Ohio Op. 2d 202",
        "volume": "66",
        "reporter": "Ohio Op. 2d",
        "page": "202",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "414 U.S. 218",
    "official_selection": {
      "court_class": "scotus",
      "selected": "414 U.S. 218",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-235",
      "page": null,
      "quote": "--- # United States v. Robinson *414 U.S. 218 (1973)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An officer lawfully arrested Robinson on a full-custody basis for operating a motor vehicle after revocation of his driver's license. Searching Robinson incident to the arrest, the officer felt an object in Robinson's coat pocket, removed a crumpled cigarette package, opened it, and found heroin capsules. Robinson moved to suppress, arguing the search went beyond what was needed to protect the officer or to preserve evidence of the license offense. ## Issue Whether, incident to a lawful custodial arrest, an officer may conduct a full search of the arrestee's person without additional justification \u2014 even with no particular reason to believe the search will produce weapons or evidence of the crime of arrest. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1973-12-11",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Robinson",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "United States v. Robinson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Indiana v. Justin Crager",
          "cluster_id": 4547157,
          "cite": [
            "113 N.E.3d 657"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brandon Pegg v. Grant Herrnberger",
          "cluster_id": 4335908,
          "cite": [
            "845 F.3d 112",
            "2017 WL 35722",
            "2017 U.S. App. LEXIS 109"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Ryan Mark Thompson",
          "cluster_id": 4311783,
          "cite": [
            "886 N.W.2d 224",
            "2016 Minn. LEXIS 656"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tony Williams",
          "cluster_id": 4257975,
          "cite": [
            "837 F.3d 1016",
            "2016 U.S. App. LEXIS 17150",
            "2016 WL 5030343"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Graham v. Connor",
          "cluster_id": 112257,
          "cite": [
            "104 L. Ed. 2d 443",
            "109 S. Ct. 1865",
            "490 U.S. 386",
            "1989 U.S. LEXIS 2467",
            "57 U.S.L.W. 4513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hudson v. Palmer",
          "cluster_id": 111252,
          "cite": [
            "82 L. Ed. 2d 393",
            "104 S. Ct. 3194",
            "468 U.S. 517",
            "1984 U.S. LEXIS 143",
            "52 U.S.L.W. 5052"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whren v. United States",
          "cluster_id": 118036,
          "cite": [
            "135 L. Ed. 2d 89",
            "116 S. Ct. 1769",
            "517 U.S. 806",
            "1996 U.S. LEXIS 3720"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rakas v. Illinois",
          "cluster_id": 109953,
          "cite": [
            "58 L. Ed. 2d 387",
            "99 S. Ct. 421",
            "439 U.S. 128",
            "1978 U.S. LEXIS 2452"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Berkemer v. McCarty",
          "cluster_id": 111249,
          "cite": [
            "82 L. Ed. 2d 317",
            "104 S. Ct. 3138",
            "468 U.S. 420",
            "1984 U.S. LEXIS 140",
            "52 U.S.L.W. 5023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Illinois",
          "cluster_id": 109304,
          "cite": [
            "45 L. Ed. 2d 416",
            "95 S. Ct. 2254",
            "422 U.S. 590",
            "1975 U.S. LEXIS 82"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mincey v. Arizona",
          "cluster_id": 109905,
          "cite": [
            "57 L. Ed. 2d 290",
            "98 S. Ct. 2408",
            "437 U.S. 385",
            "1978 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Long",
          "cluster_id": 111020,
          "cite": [
            "77 L. Ed. 2d 1201",
            "103 S. Ct. 3469",
            "463 U.S. 1032",
            "1983 U.S. LEXIS 7",
            "51 U.S.L.W. 5231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Mimms",
          "cluster_id": 109751,
          "cite": [
            "54 L. Ed. 2d 331",
            "98 S. Ct. 330",
            "434 U.S. 106",
            "1977 U.S. LEXIS 157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Brown",
          "cluster_id": 110901,
          "cite": [
            "75 L. Ed. 2d 502",
            "103 S. Ct. 1535",
            "460 U.S. 730",
            "1983 U.S. LEXIS 143",
            "51 U.S.L.W. 4361"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Gant",
          "cluster_id": 145887,
          "cite": [
            "173 L. Ed. 2d 485",
            "129 S. Ct. 1710",
            "556 U.S. 332",
            "2009 U.S. LEXIS 3120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chadwick",
          "cluster_id": 109714,
          "cite": [
            "53 L. Ed. 2d 538",
            "97 S. Ct. 2476",
            "433 U.S. 1",
            "1977 U.S. LEXIS 133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oliver v. United States",
          "cluster_id": 111146,
          "cite": [
            "80 L. Ed. 2d 214",
            "104 S. Ct. 1735",
            "466 U.S. 170",
            "1984 U.S. LEXIS 55",
            "52 U.S.L.W. 4425"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Bertine",
          "cluster_id": 111788,
          "cite": [
            "93 L. Ed. 2d 739",
            "107 S. Ct. 738",
            "479 U.S. 367",
            "1987 U.S. LEXIS 286",
            "55 U.S.L.W. 4105"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. DeFillippo",
          "cluster_id": 110127,
          "cite": [
            "61 L. Ed. 2d 343",
            "99 S. Ct. 2627",
            "443 U.S. 31",
            "1979 U.S. LEXIS 135"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. United States",
          "cluster_id": 109860,
          "cite": [
            "56 L. Ed. 2d 168",
            "98 S. Ct. 1717",
            "436 U.S. 128",
            "1978 U.S. LEXIS 89"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. McNeely",
          "cluster_id": 858288,
          "cite": [
            "185 L. Ed. 2d 696",
            "133 S. Ct. 1552",
            "569 U.S. 141",
            "2013 U.S. LEXIS 3160",
            "81 U.S.L.W. 4250",
            "24 Fla. L. Weekly Fed. S 150",
            "2013 WL 1628934"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arkansas v. Sanders",
          "cluster_id": 110119,
          "cite": [
            "61 L. Ed. 2d 235",
            "99 S. Ct. 2586",
            "442 U.S. 753",
            "1979 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Quarles",
          "cluster_id": 111214,
          "cite": [
            "81 L. Ed. 2d 550",
            "104 S. Ct. 2626",
            "467 U.S. 649",
            "1984 U.S. LEXIS 111",
            "52 U.S.L.W. 4790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
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
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Atwater v. City of Lago Vista",
          "cluster_id": 2620702,
          "cite": [
            "149 L. Ed. 2d 549",
            "121 S. Ct. 1536",
            "532 U.S. 318",
            "2001 U.S. LEXIS 3366",
            "2001 Daily Journal DAR 3953",
            "2001 Colo. J. C.A.R. 2069",
            "14 Fla. L. Weekly Fed. S 193",
            "69 U.S.L.W. 4262",
            "2001 Cal. Daily Op. Serv. 3203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Santana",
          "cluster_id": 109504,
          "cite": [
            "49 L. Ed. 2d 300",
            "96 S. Ct. 2406",
            "427 U.S. 38",
            "1976 U.S. LEXIS 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Robinson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108893 OR 9425474 OR 9425475 OR 9425476) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDUyNTU2ODAwMDAwJnM9MzE2ODkyOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108893+OR+9425474+OR+9425475+OR+9425476%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 5,
        "triage_snippet_classified": 195
      },
      "lane2_top_cited": {
        "query": "cites:(108893 OR 9425474 OR 9425475 OR 9425476)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00ODAmcz02MDY2ODkmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28108893+OR+9425474+OR+9425475+OR+9425476%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108893 OR 9425474 OR 9425475 OR 9425476)",
        "reviewed": 56,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 56,
        "triage_read": 0,
        "triage_snippet_classified": 56
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108893 OR 9425474 OR 9425475 OR 9425476)",
    "indexed_citing_opinions": 2137,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108893,
        "count": 1919,
        "count_source": "search"
      },
      {
        "opinion_id": 9425474,
        "count": 268,
        "count_source": "search"
      },
      {
        "opinion_id": 9425475,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425476,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3541,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-robinson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxMDIwMjQmcz0xMDI4NjMwNiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28108893+OR+9425474+OR+9425475+OR+9425476%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108893,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 250962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 279289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 284470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 298864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 307722,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 308053,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 1141467,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 1170737,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 1211726,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 1604308,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 1821304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 1922425,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 1992458,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108893,
        "cited_id": 3579530,
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
    "date_created": "2026-07-06T02:32:43Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:33:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:33:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:35:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:33:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Robinson

```
<opinion type="majority">
<author id="b371-10">Mr. Justice Rehnquist</author>
<p id="Aif">delivered the opinion of the Court.</p>
<p id="b371-12">Respondent Robinson was convicted in United States District Court for the District of Columbia of the possession and facilitation of concealment of heroin in violation of <span class="citation no-link">26 U. S. C. § 4704</span> (a) (1964 ed.), and <span class="citation no-link">21 U. S. C. § 174</span> (1964 ed.). He was sentenced to concurrent terms of imprisonment for these offenses. On his appeal to the Court of Appeals for the District of Columbia Cir<page-number citation-index="1" label="220">*220</page-number>cuit, that court first remanded the case to the District Court for an evidentiary hearing concerning the scope of the search of respondent’s person which had occurred at the time of his arrest. 145 U. S. App. D. C. 46, <span class="citation" data-id="9457297"><a href="/opinion/298864/united-states-v-willie-robinson-jr/" aria-description="Citation for case: United States v. Willie Robinson, Jr.">447 F. 2d 1215</a></span> (1971). The District Court made findings of fact and conclusions of law adverse to respondent, and he again appealed. This time the Court of Appeals en banc reversed the judgment of conviction, holding that the heroin introduced in evidence against respondent had been obtained as a result of a search which violated the Fourth Amendment to the United States Constitution. 153 U. S. App. D. C. 114, <span class="citation" data-id="9459062"><a href="/opinion/307722/united-states-v-willie-robinson-jr/" aria-description="Citation for case: United States v. Willie Robinson, Jr.">471 F. 2d 1082</a></span> (1972). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./410/982/">410 U. S. 982</a></span> (1973), and set the case for argument together with <em>Gustafson </em>v. <em>Florida, </em>No. 71-1669, <em>post, </em>p. 260, also decided today.</p>
<p id="b372-5">On April 23, 1968, at approximately 11 p. m., Officer Richard Jenks, a 15-year veteran of the District of Columbia Metropolitan Police Department, observed the respondent driving a 1965 Cadillac near the intersection of 8th and C Streets, N. E., in the District of Columbia. Jenks, as a result of previous investigation following a check of respondent’s operator’s permit four days earlier, determined there was reason to believe that respondent was operating a motor vehicle after the revocation of his operator’s permit. This is an offense defined by statute in the District of Columbia which carries a mandatory minimum jail term, a mandatory minimum fine, or both. D. C. Code Ann. § 40-302 (d) (1967).</p>
<p id="b372-6">Jenks signaled respondent to stop the automobile, which respondent did, and all three of the occupants emerged from the car. At that point Jenks informed respondent that he was under arrest for “operating after revocation and obtaining a permit by misrepresentation.” It was assumed by the Court of Appeals, and is conceded by the respondent here, that Jenks had <page-number citation-index="1" label="221">*221</page-number>probable cause to arrest respondent, and that he effected a full-custody arrest.<footnotemark>1</footnotemark></p>
<p id="b373-5">In accordance with procedures prescribed in police department instructions,<footnotemark>2</footnotemark> Jenks then began to search <page-number citation-index="1" label="222">*222</page-number>respondent. He explained at a subsequent hearing that he was “face-to-face” with the respondent, and “placed [his] hands on [the respondent], my right-hand to his <page-number citation-index="1" label="223">*223</page-number>left breast like this (demonstrating) and proceeded to pat him down thus [with the right hand].” During this patdown, Jenks felt an object in the left breast pocket of the heavy coat respondent was wearing, but testified that he “couldn't tell what it was” and also that he “couldn’t actually tell the size of it.” Jenks then reached into the pocket and pulled out the object, which turned out to be a “crumpled up cigarette package.” Jenks testified that at this point he still did not know what was in the package:</p>
<blockquote id="b375-5">“As I felt the package I could feel objects in the package but I couldn’t tell what they were. ... I knew they weren’t cigarettes.”</blockquote>
<p id="b375-6">The officer then opened the cigarette pack and found 14 gelatin capsules of white powder which .he thought to be, and which later analysis proved to be, heroin. Jenks then continued his search of respondent to completion, feeling around his waist and trouser legs, and examining the remaining pockets. The heroin seized from the respondent was admitted into evidence at the trial which resulted in his conviction in the District Court.</p>
<p id="b375-7">The opinion for the plurality judges of the Court of Appeals, written by Judge Wright, the concurring opinion of Chief Judge Bazelon, and the dissenting opinion of Judge Wilkey, concurred in by three judges, gave careful and comprehensive treatment to the authority of a police officer to search the person of one <page-number citation-index="1" label="224">*224</page-number>who has been validly arrested and taken into custody. We conclude that the search conducted by Jenks in this case did not offend the limits imposed by the Fourth Amendment, and we therefore reverse the judgment of the Court of Appeals.</p>
<p id="b376-5">I</p>
<p id="b376-6">It is well settled that a search incident to a lawful arrest is a traditional exception to the warrant requirement of the Fourth Amendment. This general exception has historically been formulated into two distinct propositions. The first is that a search may be made of the <em>person </em>of the arrestee by virtue of the lawful arrest. The second is that a search may be made of the area within the control of the arrestee.</p>
<p id="b376-7">Examination of this Court’s decisions shows that these two propositions have been treated quite differently. The validity of the search of a person incident to a lawful arrest has been regarded as settled from its first enunciation, and has remained virtually unchallenged until the present case. The validity of the second proposition, while likewise conceded in principle, has been subject to differing interpretations as to the extent of the area which may be searched.</p>
<p id="b376-8">Because the rule requiring exclusion of evidence obtained in violation of the Fourth Amendment was first enunciated in <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), it is understandable that virtually all of this Court’s search-and-seizure law has been developed since that time. In <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>, </em>the Court made clear its recognition of the validity of a search incident to a lawful arrest:</p>
<blockquote id="b376-9">“What then is the present case? Before answering that inquiry specifically, it may be well by a process of exclusion to state what it is not. It is not an assertion of the right on the part of the <page-number citation-index="1" label="225">*225</page-number>Government, always recognized under English and American law, to search the person of the accused when legally arrested to discover and seize the fruits or evidences of crime. This right has been uniformly maintained in many cases. 1 Bishop on Criminal Procedure, §211; Wharton, Crim. Plead, and Practice, 8th ed., § 60; <em>Dillon </em>v. <em>O’Brien and Davis, </em>16 Cox C. C. 245.” <em>Id., </em>at 392.</blockquote>
<p id="b377-5"><em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span> (1925), decided 11 years after <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>, </em>repeats the categorical recognition of the validity of a search incident to lawful arrest:</p>
<blockquote id="b377-6">“The right without a search warrant contemporaneously to search persons lawfully arrested while committing crime and to search the place where the arrest is made in order to find and seize things connected with the crime as its fruits or as the means by which it was committed, as well as weapons and other things to effect an escape from custody, is not to be doubted.” <em>Id., </em>at 30.</blockquote>
<p id="b377-7">Throughout the series of cases in which the Court has addressed the second proposition relating to a search incident to a lawful arrest — the permissible area beyond the person of the arrestee which such a search may cover — no doubt has been expressed as to the unqualified authority of the arresting authority to search the person of the arrestee. <em>E. g., Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925); <em>Marron </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span> (1927); <em>Go-Bart Co. </em>v. <em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span> (1931); <em>United States </em>v. <em>Lefkowitz, </em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452</a></span> (1932); <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span> (1947); <em>Trupiano </em>v. <em>United States, </em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span> (1948); <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span> (1950); <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span> (1964); <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969). In <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>, </em>where the Court overruled <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>and <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>as to the area <page-number citation-index="1" label="226">*226</page-number>of permissible search incident to a lawful arrest, full recognition was again given to the authority to search the person of the arrestee:</p>
<blockquote id="b378-5">“When an arrest is made, it is reasonable for the arresting officer to search the person arrested in order to remove any weapons that the latter might seek to use in order to resist arrest or effect his escape. Otherwise, the officer's safety might well be endangered, and the arrest itself frustrated. In addition, it is entirely reasonable for the arresting officer to search for and seize any evidence on the arrestee’s person in order to prevent its concealment or destruction.” <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California">395 U. S., at 762-763</a></span>.</blockquote>
<p id="b378-6">Three years after the decision in <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel, supra,</a></span> </em>we upheld the validity of a search in which heroin had been taken from the person of the defendant after his arrest on a weapons charge, in <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span> (1972), saying:</p>
<blockquote id="b378-7">“Under the circumstances surrounding Williams’ possession of the gun seized by Sgt. Connolly, the arrest on the weapons charge was supported by probable cause, and the search of his person and of the car incident to that arrest was lawful.” <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#149" aria-description="Citation for case: Adams v. Williams"><em>Id., </em>at 149</a></span>.</blockquote>
<p id="b378-8">Last Term in <em>Cupp </em>v. <em>Murphy, </em><span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#295" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291, 295</a></span> (1973), we again reaffirmed the traditional statement of the authority to search incident to a valid arrest.</p>
<p id="b378-9">Thus the broadly stated rule, and the reasons for it, have been repeatedly affirmed in the decisions of this Court since <em>Weeks </em>v. <em>United States, supra, </em>nearly 60 years ago. Since the statements in the cases speak not simply in terms of an exception to the warrant requirement, but in terms of an affirmative authority to search, they clearly imply that such searches also meet the Fourth Amendment’s requirement of reasonableness.</p>
<p id="b379-4"><page-number citation-index="1" label="227">*227</page-number>II</p>
<p id="b379-5">In its decision of this case, the Court of Appeals decided that even after a police officer lawfully places a suspect under arrest for the purpose of taking him into custody, he may not ordinarily proceed to fully search the prisoner. He must, instead, conduct a limited frisk of the outer clothing and remove such weapons that he may, as a result of that limited frisk, reasonably believe and ascertain that the suspect has in his possession. While recognizing that <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), dealt with a permissible “frisk” incident to an investigative stop based on less than probable cause to arrest, the Court of Appeals felt that the principles of that case should be carried over to this probable-cause arrest for driving while one’s license is revoked. Since there would be no further evidence of such a crime to be obtained in a search of the arrestee, the court held that only a search for weapons could be justified.</p>
<p id="b379-6"><em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra,</a></span> </em>did not involve an arrest for probable cause, and it made quite clear that the “protective frisk” for weapons which it approved might be conducted without probable cause. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 21-22, 24-25</a></span>. This Court’s opinion explicitly recognized that there is a “distinction in purpose, character, and extent between a search incident to an arrest and a limited search for weapons.”</p>
<blockquote id="b379-7">“The former, although justified in part by the acknowledged necessity to protect the arresting officer from assault with a concealed weapon, <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964), is also justified on other grounds, <em>ibid., </em>and can therefore involve a relatively extensive exploration of the person. A search for weapons in the absence of probable cause to arrest, however, must, like any other search, be strictly circumscribed by the exigen<page-number citation-index="1" label="228">*228</page-number>cies which justify its initiation. <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#310" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 310</a></span> (1967) (Mr. Justice Fortas, concurring). Thus it must be limited to that which is necessary for the discovery of weapons which might be used to harm the officer or others nearby, and may realistically be characterized as something less than a ‘full’ search, even though it remains a serious intrusion.</blockquote>
<blockquote id="b380-5">"... An arrest is a wholly different kind of intrusion upon individual freedom from a limited search for weapons, and the interests each is designed to serve are likewise quite different. An arrest is the initial stage of a criminal prosecution. It is intended to vindicate society’s interest in having its laws obeyed, and it is inevitably accompanied by future interference with the individual’s freedom of movement, whether or not trial or conviction ultimately follows. The protective search for weapons, on the other hand, constitutes a brief, though far from inconsiderable, intrusion upon the sanctity of the person.” <em>Id., </em>at 25-26 (footnote omitted).</blockquote>
<p id="b380-6"><em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>therefore, affords no basis to carry over to a probable-cause arrest the limitations this Court placed on a stop-and-frisk search permissible without probable cause.</p>
<p id="b380-7">The Court of Appeals also relied on language in <em>Peters </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#66" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 66</a></span> (1968), a companion case to <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>. </em>There the Court held that the police officer had authority to search Peters because he had probable cause to arrest him, and went on to say:</p>
<blockquote id="b380-8">“[T]he incident search was obviously justified 'by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the <page-number citation-index="1" label="229">*229</page-number>destruction of evidence of the crime.’ <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964). Moreover, it was reasonably limited in scope by these purposes. Officer Lasky did not engage in an unrestrained and thorough-going examination of Peters and his personal effects.” <em>Id., </em>at 67.</blockquote>
<p id="b381-5">It is, of course, possible to read the second sentence from this quotation as imposing a novel limitation on the established doctrine set forth in the first sentence. It is also possible to read it as did Mr. Justice Harlan in his opinion concurring in the result:</p>
<blockquote id="b381-6">“The second possible source of confusion is the Court’s statement that 'Officer Lasky did not engage in an unrestrained and thorough-going examination of Peters and his personal effects.’ [392 U. S.], at 67. Since the Court found probable cause to arrest Peters, and since an officer arresting on probable cause is entitled to make a very full incident search, I assume that this is merely a factual observation. As a factual matter, I agree with it.” <em>Id., </em>at 77 (footnote omitted).</blockquote>
<p id="b381-7">We do not believe that the Court in <em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">Peters</a></span> </em>intended in one unexplained and unelaborated sentence to impose a novel and far-reaching limitation on the authority to search the person of an arrestee incident to his lawful arrest. While the language from <em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">Peters</a></span> </em>was quoted with approval in <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#764" aria-description="Citation for case: Chimel v. California">395 U. S., at 764</a></span>, it is preceded by a full exposition of the traditional and unqualified authority of the arresting officer to search the arrestee’s person. <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California"><em>Id., </em>at 763</a></span>. We do not believe that either <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>or <em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">Peters</a></span>, </em>when considered in the light of the previously discussed statements of this Court, justified the sort of limitation upon that authority which the Court of Appeals fashioned in this case.</p>
<p id="b382-4"><page-number citation-index="1" label="230">*230</page-number>Ill</p>
<p id="b382-5">Virtually all of the statements of this Court affirming the existence of an unqualified authority to search incident to a lawful arrest are dicta. We would not, therefore, be foreclosed by principles of <em>stare decisis </em>from further examination into history and practice in order to see- whether the sort of qualifications imposed by the Court of Appeals in this case were in fact intended by the Framers of the Fourth Amendment or recognized in cases decided prior to <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>. </em>Unfortunately such authorities as exist are sparse. Such common-law treatises as Blackstone’s Commentaries and Holmes’ Common Law are simply silent on the subject. Pollock and Maitland, in their History of English Law, describe the law of arrest as “rough and rude” before the time of Edward I, but do not address the authority to search incident to arrest. 2 F. Pollock &amp; F. Maitland, The History of English Law <em>582 </em>(2d ed. 1909).</p>
<p id="b382-6">The issue was apparently litigated in the English courts in <em>Dillon </em>v. <em>O’Brien, </em>16 Cox C. C. 245 (Exch. Ireland, 1887), cited in <em>Weeks </em>v. <em>United States, supra, </em>There Baron Palles said:</p>
<blockquote id="b382-7">“But the interest of the State in the person charged being brought to trial in due course necessarily extends, as well -to the preservation of material evidence of his guilt or innocence, as to his custody for the purpose of trial. His custody is of no value if the law is powerless to prevent the abstraction or destruction of this evidence, without which a trial would be no more than an empty form. But if there be a right to production or preservation of this evidence, I cannot see how it can be enforced otherwise than by capture.” 16 Cox C. C., at 250.</blockquote>
<p id="b383-3"><page-number citation-index="1" label="231">*231</page-number><em>Spalding </em>v. <em>Preston, </em><span class="citation" data-id="6573992"><a href="/opinion/6694075/spalding-v-preston/" aria-description="Citation for case: Spalding v. Preston">21 Vt. 9</a></span> (1848), represents an early holding in this country that evidence may be seized from one who is lawfully arrested. In <em>Closson </em>v. <em>Morrison, </em>47 N. H. 482 (1867), the Court made the following statement:</p>
<blockquote id="b383-4">“[W]e think that an officer would also be justified in taking from a person whom he had arrested for crime, any deadly weapon he might find upon him, such as a revolver, a dirk, a knife, a sword cane, a slung shot, or a club, though it had not been used or intended to be used in the commission of the offence for which the prisoner had been arrested, and even though no threats of violence towards the officer had been made. A due regard for his own safety on the part of the officer, and also for the public safety, would justify a sufficient search to ascertain if such weapons were carried about the person of the prisoner, or were in his possession, and if found, to seize and hold them until the prisoner should be discharged, or until they could be otherwise properly disposed of. <em>Spalding </em>v. <em>Preston, </em><span class="citation" data-id="6573992"><a href="/opinion/6694075/spalding-v-preston/#16" aria-description="Citation for case: Spalding v. Preston">21 Vt. 9, 16</a></span>.</blockquote>
<blockquote id="b383-5">“So we think it might be with money or other articles of value, found upon the prisoner, by means of which, if left in his possession, he might procure his escape, or obtain tools, or implements, or weapons with which to effect his escape. We think the officer arresting a man for crime, not only may, but frequently should, make such searches and seizures; that in many cases they might be reasonable and proper, and courts would hold him harmless for so doing, when he acts in good faith, and from a regard to his own or the public safety, or the security of his prisoner.” <em>Id., </em>at 484-485.</blockquote>
<p id="b384-4"><page-number citation-index="1" label="232">*232</page-number>Similarly, in <em>Holker </em>v. <em>Hennessey, </em><span class="citation" data-id="8012666"><a href="/opinion/8055583/holker-v-hennessey/" aria-description="Citation for case: Holker v. Hennessey">141 Mo. 527</a></span>, <span class="citation" data-id="8012666"><a href="/opinion/8055583/holker-v-hennessey/" aria-description="Citation for case: Holker v. Hennessey">42 S. W. 1090</a></span> (1897), the Supreme Court of Missouri said:</p>
<blockquote id="b384-5">"Generally speaking, in the absence of a statute, an officer has no right to take any property from the person of the prisoner except such as may afford evidence of the crime charged, or means'of identifying the criminal, or may be helpful in making an escape.” <span class="citation" data-id="8012666"><a href="/opinion/8055583/holker-v-hennessey/#539" aria-description="Citation for case: Holker v. Hennessey"><em>Id., </em>at 539</a></span>, <span class="citation" data-id="8012666"><a href="/opinion/8055583/holker-v-hennessey/#1093" aria-description="Citation for case: Holker v. Hennessey">42 S. W., at 1093</a></span>.</blockquote>
<p id="b384-6">Then Associate Judge Cardozo of the New York Court of Appeals summarized his understanding of the historical basis for the authority to search incident to arrest in these words:</p>
<blockquote id="b384-7">“The basic principle is this: Search of the person is unlawful when the seizure of the body is a trespass, and the purpose of the search is to discover grounds as yet unknown for arrest or accusation [citation omitted]. Search of the person becomes lawful when grounds for arrest and accusation have been discovered, and the law is in the act of subjecting the body of the accused to its physical dominion.</blockquote>
<blockquote id="b384-8">“The distinction may seem subtle, but in truth it is founded in shrewd appreciation of the necessities of government. We are not to strain an immunity to the point at which human nature rebels against honoring it in conduct. The peace officer empowered to arrest must be empowered to disarm. If he may disarm, he may search, lest a. weapon be concealed. The search being lawful, he retains what he finds if connected with the crime.” <em>People </em>v. <em>Chiagles, </em><span class="citation" data-id="3579530"><a href="/opinion/3598271/people-v-chiagles/#197" aria-description="Citation for case: People v. . Chiagles">237 N. Y. 193, 197</a></span>, <span class="citation" data-id="3579530"><a href="/opinion/3598271/people-v-chiagles/#584" aria-description="Citation for case: People v. . Chiagles">142 N. E. 583, 584</a></span> (1923).</blockquote>
<p id="b384-10">While these earlier authorities are sketchy, they tend to support the broad statement of the authority to <page-number citation-index="1" label="233">*233</page-number>search incident to arrest found in the successive decisions of this Court, rather than the restrictive one which was applied by the Court of Appeals in this case. The scarcity of case law before <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>is doubtless due in part to the fact that the exclusionary rule there enunciated had been first adopted only 11 years earlier in Iowa; but it would seem to be also due in part to the fact that the issue was regarded as well settled.<footnotemark>3</footnotemark></p>
<p id="b385-4">The Court of Appeals in effect determined that the <em>only </em>reason supporting the authority for a <em>full </em>search incident to lawful arrest was the possibility of discovery of evidence or fruits.<footnotemark>4</footnotemark> Concluding that there could be no evidence or fruits in the case of an offense such as that with which respondent was charged, it held that any protective search would have to be limited by the conditions laid down in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>for a search upon less than probable cause to arrest. Quite apart from the fact that <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>clearly recognized the distinction between the two types of searches, and that a different rule governed one than governed the other, we find additional reason to disagree with the Court of Appeals.</p>
<p id="b386-4"><page-number citation-index="1" label="234">*234</page-number>The justification or reason for the authority to search incident to a lawful arrest rests quite as much on the need to disarm the suspect in order to take him into custody as it does on the need to preserve evidence on his person for later use at trial. <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span> (1925); <em>Abel </em>v. <em>United States, </em><span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span> (1960). The standards traditionally governing a search incident to lawful arrest are not, therefore, commuted to the stricter <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>standards by the absence of probable fruits or further evidence of the particular crime for which the arrest is made.</p>
<p id="b386-5">Nor are we inclined, on the basis of what seems to us to be a rather speculative judgment, to qualify the breadth of the general authority to search incident to a lawful custodial arrest on an assumption that persons arrested for the offense of driving while their licenses have been revoked are less likely to possess dangerous weapons than are those arrested for other crimes.<footnotemark>5</footnotemark> It is scarcely open to doubt that the danger to an officer is far greater in the case of the extended exposure which <page-number citation-index="1" label="235">*235</page-number>follows the taking of a suspect into custody and transporting him to the police station than in the case of the relatively fleeting contact resulting from the typical <em>Terry-type </em>stop. This is an adequate basis for treating all custodial arrests alike for purposes of search justification.</p>
<p id="b387-5">But quite apart from these distinctions, our more fundamental disagreement with the Court of Appeals arises from its suggestion that there must be litigated in each case the issue of whether or not there was present one of the reasons supporting the authority for a search of the person incident to a lawful arrest. We do not think the long line of authorities of this Court dating back to <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>, </em>or what we can glean from the history of practice in this country and in England, requires such a case-by-case adjudication. A police officer's determination as to how and where to search the person of a suspect whom he has arrested is necessarily a quick <em>ad hoc </em>judgment which the Fourth Amendment does not require to be broken down in each instance into an analysis of each step in the search. The authority to search the person incident to a lawful custodial arrest, while based upon the need to disarm and to discover evidence, does not depend on what a court may later decide was the probability in a particular arrest situation that weapons or evidence would in fact be found upon the person of the suspect. A custodial arrest of a suspect based on probable cause is a reasonable intrusion under the Fourth Amendment; that intrusion being lawful, a search incident to the arrest requires no additional justification. It is the fact of the lawful arrest which establishes the authority to search, and we hold that in the case of a lawful custodial arrest a full search of the person is not only an exception to the warrant requirement of the Fourth Amendment, but is also a “reasonable” search under that Amendment.</p>
<p id="b388-4"><page-number citation-index="1" label="236">*236</page-number>IV</p>
<p id="b388-5">The search of respondent’s person conducted by Officer Jenks in this case and the seizure from him of the heroin, were permissible under established Fourth Amendment law. While thorough, the search partook of none of the extreme or patently abusive characteristics which were held to violate the Due Process Clause of the Fourteenth Amendment in <em>Rochin </em>v. <em>California, </em><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952). Since it is the fact of custodial arrest which gives rise to the authority to search,<footnotemark>6</footnotemark> it is of no moment that Jenks did not indicate any subjective fear of the respondent or that he did not himself suspect that respondent was armed.<footnotemark>7</footnotemark> Having in the course of a lawful search come upon the crumpled package of cigarettes, he was entitled to inspect it; and when his inspection revealed the heroin capsules, he was entitled to seize them as “fruits, instrumentalities, or contraband” probative of criminal conduct. <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#154" aria-description="Citation for case: Harris v. United States">331 U. S., at 154-155</a></span>; <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#299" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 299, 307</a></span> (1967); <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#149" aria-description="Citation for case: Adams v. Williams">407 U. S., at 149</a></span>. <page-number citation-index="1" label="237">*237</page-number>The judgment of the Court of Appeals holding otherwise is</p>
<p id="b389-5">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b373-6"> The Court of Appeals noted that there was a difference in the presentation of the facts in the various proceedings that were conducted in the District Court. Counsel for respondent on appeal stressed that respondent had a record of two prior narcotics convictions, and suggested that Officer Jenks may have been aware of that record through his investigation of criminal records, while Jenks was cheeking out the discrepancies in the birthdates on the operator’s permit and on the Selective Service card that had been given to him for examination when he had confronted the respondent on the previous occasion. Respondent argued below that Jenks may have used the subsequent traffic violation arrest as a mere pretext for a narcotics search which would not have been allowed by a neutral magistrate had Jenks sought a warrant. The Court of Appeals found that Jenks had denied he had any such motive, and for the purposes of its opinion accepted the Government’s version of that factual question, since even accepting that version it still found the search involved to be unconstitutional. 153 U. S. App. D. C. 114, 120 n. 3, <span class="citation" data-id="9459062"><a href="/opinion/307722/united-states-v-willie-robinson-jr/" aria-description="Citation for case: United States v. Willie Robinson, Jr.">471 F. 2d 1082</a></span>, 1088 n. 3. We think it is sufficient for purposes of our decision that respondent was lawfully arrested for an offense, and that Jenks’ placing him in custody following that arrest was not a departure from established police department practice. See n. 2, <em>infra. </em>We leave for another day questions which would arise on facts different from these.</p>
</footnote>
<footnote label="2">
<p id="b373-7"> The Government introduced testimony at the evidentiary hearing upon the original remand by the Court of Appeals as to certain standard operating procedures of the Metropolitan Police Department. Sergeant Dennis C. Donaldson, a Metropolitan Police Department Training Division instructor, testified that when a police officer makes "a full custody arrest,” which he defined as one where an officer “would arrest a subject and subsequently transport him to a police facility for booking,” the officer is trained to make a full “field type search”:</p>
<blockquote id="b373-8">“Q. Would you describe the physical acts the officer is instructed to perform with respect to this field search in a full custody arrest situation?</blockquote>
<blockquote id="b373-9">“A. (Sgt. Donaldson). Basically, it is a thorough search of the <page-number citation-index="1" label="222">*222</page-number>individual. We would expect in a field search that the officer completely search the individual and inspect areas such as behind the collar, underneath the collar, the waistband of the trousers, the cuffs, the socks and shoes. Those are the areas we would ask a complete thorough search of.</blockquote>
<blockquote id="b374-6">“Q. What are the instructions in a field type search situation when an officer feels something on the outside of the garment?</blockquote>
<blockquote id="b374-7">“A. If it is a full custody arrest and he is conducting a field search, we expect him to remove anything and examine it to determine exactly what it is.</blockquote>
<blockquote id="b374-8">“THE COURT: That is a full custody arrest. What is the last part of it?</blockquote>
<blockquote id="b374-9">“THE WITNESS: In conducting a field search, which is done any time there is a full custody arrest, we expect the officer to examine anything he might find on the subject.</blockquote>
<blockquote id="b374-10">“THE COURT: Would he do the same thing in a pat-down search?</blockquote>
<blockquote id="b374-11">“THE WITNESS: If he could determine in his pat-down or frisk by squeezing that it was not, in fact, a weapon that could be used against him, then we don’t instruct him to go further.</blockquote>
<blockquote id="b374-12">“THE COURT: But in a field search, even though he may feel something that he believes is not a weapon, is he instructed, to take it out?</blockquote>
<blockquote id="b374-13">“THE WITNESS: Yes, sir.”</blockquote>
<p id="b374-14">Sergeant Donaldson testified that officers are instructed to examine the “contents of all of the pockets” of the arrestee in the course of the field search. It was stated that these standard operating procedures were initiated bjr the police department “ [primarily, for [the officer’s] own safety and, secondly, for the safety of the individual he has placed under arrest and, thirdly, to search for evidence of the crime.” While the officer is instructed to make a full field search of the person of the individual he arrests, he is instructed, and police department regulations provide, that in the case of a full-custody arrest for driving after revocation, "areas beyond [the arrestee’s] immediate control should not be searched because there is no probable cause to believe that the vehicle contains fruits, instrumentalities, contraband or evidence of the offense of driving after revocation.” Those regulations also provide that in the case <page-number citation-index="1" label="223">*223</page-number>of some traffic offenses, including the crime of operating a motor vehicle after revocation of an operator’s permit, the officer shall make a summary arrest of the violator and take the violator, in custody, to the station house for booking. D. C. Metropolitan Police Department General Order No. 3, series 1959 (Apr. 24, 1959).</p>
<p id="b375-9">Such operating procedures are not, of course, determinative of the constitutional issues presented by this case.</p>
</footnote>
<footnote label="3">
<p id="b385-5"> See T. Taylor, Two Studies in Constitutional Interpretation 44-45 (1969).</p>
<p id="b385-6">Taylor suggests that there “is little reason to doubt that search of an arrestee’s person and premises is as old as the institution of arrest itself.” <em>Id., </em>at 28. “Neither in the reported cases nor the legal literature is there any indication that search of the person of an arrestee, or the premises in which he was taken, was ever challenged in England until the end of the nineteenth century . . . [and] the English courts gave the point short shrift.” <em>Id., </em>at 29.</p>
</footnote>
<footnote label="4">
<p id="b385-7"> Where the arrest is made for a crime for which it is reasonable to believe that evidence exists, the Court of Appeals recognizes that “warrantless intrusion into the pockets of the arrestee to discover such evidence is reasonable under the 'search incident’ exception.” 153 U. S. App. D. C., at 127, <span class="citation" data-id="9459062"><a href="/opinion/307722/united-states-v-willie-robinson-jr/#1095" aria-description="Citation for case: United States v. Willie Robinson, Jr.">471 F. 2d, at 1095</a></span>. The court then states that the officer may use this “reasonable [evidentiary] intrusion” to simultaneously look for weapons. <em><span class="citation" data-id="9459062"><a href="/opinion/307722/united-states-v-willie-robinson-jr/" aria-description="Citation for case: United States v. Willie Robinson, Jr.">Ibid.</a></span></em></p>
</footnote>
<footnote label="5">
<p id="b386-6"> Such an assumption appears at least questionable in light of the available statistical data concerning assaults on police officers who are in the course of making arrests. The danger to the police officer flows from the fact of the arrest, and its attendant proximity, stress, and uncertainty, and not from the grounds for arrest. One study concludes that approximately 30% of the shootings of police officers occur when an officer stops a person in an automobile. Bristow, Police Officer <em>Shootings </em>— A Tactical Evaluation, 54 J. Crim. L. C. &amp; P. S. 93 (1963), cited in <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#148" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 148</a></span> (1972). The Government in its brief notes that the Uniform Crime Reports, prepared by the Federal Bureau of Investigation, indicate that a significant percentage of murders of police officers occurs when the officers are making traffic stops. Brief for the United States 23. Those reports indicate that during January-March 1973, 35 police officers were murdered; 11 of those officers were killed while engaged in making traffic stops. <em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">Ibid.</a></span></em></p>
</footnote>
<footnote label="6">
<p id="b388-6"> The opinion of the Court of Appeals also discussed its understanding of the law where the police officer makes what the court characterized as “a routine traffic stop,” <em>i. e., </em>where the officer would simply issue a notice of violation and allow the offender to proceed. Since in this case the officer did make a full-custody arrest of the violator, we do not reach the question discussed by the Court of Appeals.</p>
</footnote>
<footnote label="7">
<p id="b388-7"> The United States concedes that “in searching respondent, [Officer Jenks] was not motivated by a feeling of imminent danger and was not specifically looking for weapons.” Brief for the United States 34. Officer Jenks testified, “I just searched him [Robinson], I didn't think about what I was looking for. I just searched him.” As previously noted, Officer Jenks also testified that upon removing the cigarette package from the respondent’s custody, he was still unsure what was in the package, but that he knew it was not cigarettes.</p>
</footnote>
</opinion>
```

---
