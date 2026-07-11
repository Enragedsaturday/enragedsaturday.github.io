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

## GROUP: _overhaul2/lake/cases/United States v. Burgess.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Burgess
type: case
citation: "576 F.3d 1078 (2009)"
parallel_cite: 80 Fed. R. Serv. 344
neutral_cite: "2009 U.S. App. LEXIS 17823; 2009 WL 2436674"
court: 10th Cir.
court_level: coa
circuit: ca10
year: 2009
date_decided: 2009-08-11
docket: 08-3072
authority_weight: "Binding in-circuit — 10th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/172511/united-states-v-burgess/"
  cluster_id: 172511
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Burgess
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Plain View Doctrine]]"
    role: Key
  - page: "[[Border Searches]]"
    role: "Related (cross-doctrine)"
related:
  - "[[Plain View Doctrine]]"
  - "[[Riley v. California]]"
  - "[[United States v. Leon]]"
tags:
  - case
  - fourth-amendment
  - plain-view
  - computer-search
  - particularity
  - scope-of-search
  - border-searches
  - tenth-circuit
holding: "A warrant to search a vehicle for evidence of drug trafficking that authorizes a search of 'computer records,' read together with its supporting affidavit, is sufficiently particular and limits the computer search to the kind of drug-trafficking evidence likely to be found on the device; officers who came upon child pornography while conducting a scope-limited forensic search of seized hard drives did not exceed the warrant, and suppression was properly denied."
aliases:
  - United States v. Burgess
  - "United States v. Burgess (10th Cir. 2009)"
---

# United States v. Burgess

*576 F.3d 1078 (10th Cir. 2009)* · U.S. Court of Appeals for the Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 172511 → majority opinion 172511 (O'Brien, J.; 576 F.3d 1078, decided Aug. 11, 2009). Re-keyed in the pre-W5 identity audit from a wrong-case namesake (99 F.4th 1175, residual-hearsay) to the intended computer-search-scope Burgess; identity re-verified on read 2026-07-07 (motor-home drug search → hard drives → particularity/scope). Rule quote string-matched to the CL opinion text (reporter star `*1091`). S9 promotes. -->

## Background
A Wyoming trooper stopped David Burgess's motor home for an expired trailer plate; a drug dog alerted, and a search turned up marijuana and cocaine. Officers saw a laptop and hard drives, seized the motor home, and obtained a warrant to search it for property and evidence showing the transportation and delivery of controlled substances, including "computer records." A forensic examiner searching the seized hard drives for drug evidence found thousands of child-pornography images. Burgess moved to suppress, arguing the warrant lacked [[Particularity|particularity]] and that the search exceeded its scope. The district court denied the motion.

## Issue
Whether a warrant authorizing the search of "computer records" for drug-trafficking evidence was sufficiently particular, and whether the forensic search of the hard drives stayed within that authorized scope.

## Rule
The [[Particularity|particularity]] requirement is heightened for computers because they "store and intermingle a huge array of one's personal papers in a single place," and a warrant that would permit "a search of all computer records without description or limitation" would not satisfy the Fourth Amendment. Read with its affidavit, however, the warrant here was adequately confined. The court held: "The search, in general, was limited to evidence of drugs and drug trafficking and, as it relates to the computer, was limited to the kind of drug and drug trafficking information likely to be found on a computer, to wit (as the warrant says): 'pay-owe sheets, address books, rolodexes' and 'personal property which would tend to show conspiracy to sell drugs.'" — 576 F.3d at 1091. ^pin-1091

## Application
The warrant's "computer records" clause, illuminated by an affidavit describing drug traffickers' habit of keeping photographs of contraband and coconspirators, cabined the digital search to drug-related material, since a word is known by the company it keeps. An examiner searching those categories on the hard drives could reasonably encounter image files; the incriminating pornography surfaced within a scope-limited search rather than an open-ended rummage through the machine. The search therefore did not transgress the warrant.

## Conclusion
**Affirmed.** Judge O'Brien wrote for the panel.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Burgess* is a leading circuit statement on the outer edge of the *[[Plain View Doctrine]]* in the digital context: because a computer intermingles vast private data, warrants must confine the search to specified crimes or material, and the reasonableness of a scope-limited forensic search — not an open-ended plain-view rummage — governs what officers may lawfully view. It also informs device searches at the border (see *[[Border Searches]]*).

## Appears on
- [[Plain View Doctrine]] — *Key*
- [[Border Searches]] — *Related (cross-doctrine)*

## Sources
- [*United States v. Burgess*, 576 F.3d 1078 (10th Cir. 2009)](https://www.courtlistener.com/opinion/172511/united-states-v-burgess/) — pinpoint: 576 F.3d at 1091 (computer-search particularity/scope; "computer records" limited by the warrant and affidavit to drug-trafficking evidence). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*1091`).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8343c0f7378c6e0b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Burgess"}, "payload": {"all": [{"cite": "576 F.3d 1078", "page": "1078", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "576"}, {"cite": "80 Fed. R. Serv. 344", "page": "344", "reporter": "Fed. R. Serv.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "80"}, {"cite": "2009 U.S. App. LEXIS 17823", "page": "17823", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2009"}, {"cite": "2009 WL 2436674", "page": "2436674", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2009"}], "display": "576 F.3d 1078", "official": {"cite": "576 F.3d 1078", "page": "1078", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "576"}, "official_selection_present": true, "record_id": "United States v. Burgess"}}
{"assertion_id": "2b3b021a1bb94e14", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Burgess"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Burgess", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Burgess

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Burgess",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Burgess",
    "case_name_short": "Burgess",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. David BURGESS, Defendant-Appellant",
    "input_case_name": "United States v. Burgess",
    "court": "10th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": "2009-08-11",
    "year": 2009,
    "docket": "08-3072",
    "cluster_id": 172511,
    "lead_opinion_id": 172511,
    "sibling_ids": [],
    "absolute_url": "/opinion/172511/united-states-v-burgess/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "576 F.3d 1078",
      "volume": "576",
      "reporter": "F.3d",
      "page": "1078",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "80 Fed. R. Serv. 344",
        "volume": "80",
        "reporter": "Fed. R. Serv.",
        "page": "344",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. App. LEXIS 17823",
        "volume": "2009",
        "reporter": "U.S. App. LEXIS",
        "page": "17823",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 WL 2436674",
        "volume": "2009",
        "reporter": "WL",
        "page": "2436674",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "576 F.3d 1078",
        "volume": "576",
        "reporter": "F.3d",
        "page": "1078",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 Fed. R. Serv. 344",
        "volume": "80",
        "reporter": "Fed. R. Serv.",
        "page": "344",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. App. LEXIS 17823",
        "volume": "2009",
        "reporter": "U.S. App. LEXIS",
        "page": "17823",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 WL 2436674",
        "volume": "2009",
        "reporter": "WL",
        "page": "2436674",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "576 F.3d 1078",
    "official_selection": {
      "court_class": "coa",
      "selected": "576 F.3d 1078",
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
    "date_created": "2026-07-07T18:13:42Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:13:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:13:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:13:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:13:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-burgess--172511",
      "to_record_id": "United States v. Burgess",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Burgess

```
                                                                     FILED
                                                          United States Court of Appeals
                                                                  Tenth Circuit

                                                                August 11, 2009
                                   PUBLISH                    Elisabeth A. Shumaker
                                                                  Clerk of Court
                   UNITED STATES COURT OF APPEALS

                                TENTH CIRCUIT


 UNITED STATES OF AMERICA,

       Plaintiff - Appellee,

 v.                                                    No. 08-8053

 DAVID BURGESS,

       Defendant - Appellant.


                 Appeal from the United States District Court
                         for the District of Wyoming
                      (D.C. No. 1:07-CR-00298-ABJ-1)


James C. Anderson, Assistant United States Attorney (Kelly H. Ranking, United
States Attorney, with him on the briefs) Cheyenne, Wyoming, for Plaintiff-
Appellee.

Norman R. Mueller (Ty Gee with him on the briefs) of Haddon, Morgan, Mueller,
Jordan, Mackey & Foreman, P.C., Denver, Colorado, for Defendant-Appellant.


Before TACHA, O’BRIEN, and McCONNELL, Circuit Judges.


O’BRIEN, Circuit Judge.



      Following a traffic stop and a canine alert, police searched David Burgess’

motor home for drugs and evidence of drug trafficking. The search led to the
discovery of a laptop computer and two external hard drives. The hard drives

contained thousands of pictures of child pornography, which Burgess moved to

suppress, arguing the warrant authorizing their search lacked sufficient

particularity and the search exceeded the scope of the warrant. The district court

denied the motion. Burgess continues to press his arguments here and also

challenges the admission of 404(b) evidence and the length of his sentence. We

affirm.

                                     I. FACTS

A. Introduction

      On July 24, 2007, Wyoming Trooper Matt Arnell observed a motor home

with Nevada license plates at a restaurant parking lot in Evanston, Wyoming. It

was towing a trailer bearing an expired Wyoming license plate. Arnell was aware

(from a prior briefing) the motor home was associated with the Hell’s Angels

motorcycle club. He verified that the trailer plate was expired but did nothing

more until the motor home was driven on to Interstate 80 heading east. As Arnell

followed the vehicle, he called for a drug canine to be brought to the area. He

then stopped the motor home to issue a citation for the expired plate. When the

driver, Shayne Waldron, stepped out, Arnell smelled the odor of burnt marijuana.

As Arnell spoke with Waldron, a passenger in the motor home, David Burgess,

joined the conversation. Burgess said he was the owner of the motor home and

both men acknowledged the trailer’s license plate was expired. Burgess explained

                                        -2-
the trailer belonged to a person who permitted them to use it and they were

traveling to another town in Wyoming to update the registration and obtain

current plates.

      As Arnell was issuing a citation for the expired plate, Deputy David Homar

and his canine, Blitz, arrived. Blitz (who had never given a false alert to the

presence of drugs) alerted at the doors of the motor home. Trooper Arnell

informed Burgess he was going to search the vehicle. Burgess said he would

rather Arnell get a warrant. Nevertheless, because of the suspicions raised by

Blitz’s alert and the smell of marijuana, Arnell entered the motor home where he

found some marijuana, a pipe, and two bags of cocaine – each containing

approximately seven grams. Arnell advised Waldron and Burgess of their rights

per the Miranda decision. 1 When Arnell said he had found marijuana, Burgess

admitted the marijuana was his. Arnell resumed the search. He noticed a laptop

computer and a Seagate hard drive in the bedroom. After approximately fifteen to

thirty minutes, Arnell left the motor home and arranged to have it towed to a

Wyoming Department of Transportation shop for further inspection.

      In the meantime, Agent Russell Schmitt, a narcotics officer with the Green

River, Wyoming, police department arranged to meet Arnell at the shop. The two

officers went to the Department of Criminal Investigations office in Evanston to


      1
          Miranda v. Arizona, 384 U.S. 436 (1966).


                                           -3-
prepare an affidavit and request for a search warrant. Paragraph 17 of the

affidavit stated in relevant part: “Based upon training and experience, your

Affiant [Schmitt] knows that persons involved in trafficking or the use of

narcotics often keep photographs of coconspirators or photographs of illegal

narcotics in their vehicle.” (R. Vol. I at 133.) Arnell and Schmitt’s team leader,

Agent Webster, reviewed the documents. Arnell and Schmitt then took the

documents to the county attorney for review and approval. Finally, they

presented the affidavit and request for a warrant to the county judge, who

incorporated the affidavit into the warrant and authorized a search for:

      The property and premises of a white, 1999, Freightliner Motorhome
      . . . [for] certain property and evidence to show the transportation
      and delivery of controlled substances, which may include but not
      limit[ed] to, cash, or proceeds from the sale of controlled substances,
      Marijuana, Cocaine, Methamphetamine, or other illegal controlled
      substances, along with associated paraphernalia to include but not
      limited to pipes, bongs, syringes, packaging material, computer
      records, scales, laboratory dishes, flasks, beakers, tubes, pie tins,
      electrical timers, containers to be used for storing , manufacturing
      and selling, chemicals used in the creation of illegal narcotics as well
      as their diluting agents, items of personal property which would tend
      to show conspiracy to sell drugs, including pay-owe sheets, address
      books, rolodexes, pagers, firearms and monies.

(Id. at 130.) The warrant authorized a search on July 24, 2007, “or within ten

days thereafter.” (Id.)

      After serving the warrant, the officers returned to the search of the motor

home. Arnell discovered a Maxtor hard drive pushed underneath the couch in the

living room. The Maxtor drive along with the laptop and the Seagate drive

                                         -4-
discovered earlier were seized and transported to Cheyenne, Wyoming, for

forensic examination. Agent Scott Hughes, special agent with the Internet Crimes

Against Children Division 2 was assigned to the case on August 1, 2007. When

Hughes went to retrieve the material from the evidence locker, the associated

paperwork was not present. Hughes immediately requested the paperwork, which

he received on August 21, 2007. After reviewing the warrant, Hughes was

concerned about the time delay (the items were seized on July 24). He contacted

a DCI staff attorney who advised he could search for evidence of controlled

substances, but if he found evidence of any other crime, he must stop and request

a new warrant to continue his search. The search of the hard drives was

commenced on September 6, 2007.

      Hughes began with the Maxtor hard drive using a program called EnCase.

The protocol is to first make a byte-for-byte copy of the hard drive. After the

contents of the original hard drive are copied, the original drive is secured and the

copied material is examined – this process ensures evidence is not corrupted.

Hughes planned to contact the investigating agent to see if there were any special

key or code words which may have been found during the investigation to

facilitate further search once the copying process was complete.

      Copying the files can take up to twelve hours but EnCase allows an


      2
         Agents from this division are trained in computer examinations and work on
cases from many different law enforcement divisions, including narcotics.

                                          -5-
investigator to “preview” files as they are being copied. (Id. at 246.) Hughes

decided to take advantage of the preview feature to look for “trophy photos,” i.e.,

pictures of a “person holding the controlled substance in front of a stack of

money,” similar to the kinds of photographs described in Paragraph 17 of

Schmitt’s affidavit. (Id.) The images are shown in a “gallery view,” an option

where multiple reduced size photos are displayed on one page. (Id.) After

viewing 200-300 digital images of personal photographs, Hughes came upon an

image depicting child sexual exploitation. He immediately closed the preview

program and secured a new warrant authorizing a search for evidence of child

sexual exploitation. He then searched all three devices, the laptop, the Seagate

hard drive and the Maxtor hard drive. While the laptop did not contain child

pornography, his search revealed approximately 166,000 images, including

movies and texts, between the two hard drives. Hughes stopped counting the

number of child pornography files when the count exceeded 1,300. His

conservative estimate was 30% to 45% of the files contained child pornography,

approximately 70,000 images. Some of the same pornographic pictures were on

both the Maxtor and the Seagate hard drives.

      A grand jury indicted Burgess for knowing transportation of child

pornography across state lines in violation of 18 U.S.C. §§ 2252A(a)(1) and

(b)(1) (Count One) and knowing possession of child pornography transported in

interstate commerce in violation of 18 U.S.C.§§ 2252A(a)(5)(B) and (b)(2)

                                         -6-
(Count Two). Both charges were based on the images found in the Maxtor hard

drive “including, but not limited to,” six specific images.

B. Pretrial Motions

       Burgess moved to suppress the evidence claiming the original search of the

Maxtor hard drive violated his rights under the Fourth Amendment. He

maintained the first warrant (authorizing a search for drug trafficking evidence)

lacked specificity and the search constituted an impermissible general search. 3

The government claimed, even if the warrant was defective, the search was

permissible under the automobile exception to the general presumption that

warrantless searches are unreasonable. The district court denied Burgess’ motion,

concluding both the seizure and the search of the computer equipment was

supported by probable cause, the seizure was valid under the automobile

exception and the search warrant was sufficient to allow a search of the computer

equipment for evidence of drug trafficking. Finally, the court held the search did

not exceed the scope of the warrant.

           Prior to trial, Burgess said he planned to defend against the charges by

testing the government’s ability to prove he knowingly possessed the images

charged in the indictment and found on the Maxtor hard drive. In response the

government filed a motion declaring its intent to introduce 78 images from the

       3
        Burgess claims the second search warrant (authorizing a search for child
pornography) was tainted by the first search, but raises no other issues with respect to the
second warrant or the resulting search.

                                            -7-
Seagate hard drive, including numerous pictures of R.C., a fourteen-year-old

female ward of Burgess’ friend, Rebecca Deshaise. Numerous pictures of R.C.

were found on both hard drives and trial testimony revealed R.C. had spent many

hours at Burgess’ home over the years.

      Some of the pictures of R.C., found only on the Seagate drive, were taken

in May, 2007, in a motel room in Winnemucca, Nevada, while Burgess attended

the Run-A-Mucca motorcycle rally. R.C. and two of her friends accompanied

Deshaise and Burgess to the rally. Among the pictures were nude and seminude

images of her (some showing her exposed genitalia), which also contained lurid

text suggesting Burgess was the photographer and/or describing inappropriate

sexual contact between R.C. and “Uncle David.” (e.g. Sealed Vol. II, Exh. 816.)

The government offered the evidence to prove motive, intent, knowledge, and

identity under Rule 404(b) of the Federal Rules of Evidence. The government’s

motion generated objections and motions in limine prompting hearings prior to

and during the trial. Eventually, the parties stipulated to the admissibility of four

of the child pornographic images charged in the indictment — those four pictures

were found on both the Maxtor and Seagate hard drives. 4 The pictures of R.C.

were not among those admitted by stipulation.

      4
        The images are clearly child pornography. They show a pre-pubescent girl
wearing nothing but a light dress pulled up over her chest: Exhibits 805-808 show the
nude child in various poses centering on her genitalia. One image shows her with an
adult male.


                                           -8-
C. Trial

       During the government’s case in chief the court admitted four pictures of

R.C. found on the Seagate drive 5 and gave a limiting instruction to the jury. 6

       5
         These exhibits include one nude image of R.C. taking a shower and several
semi-nude pictures of R.C. dressed only in a towel. The images appear with graphic and
vulgar superimposed text. For example, one image is R.C. sitting cross-legged on a bed
wearing only a short towel (genitalia exposed) with superimposed text referring to “Uncle
David”s . . . Princess.” (R. Sealed Vol. II, Exh. 816.) The nude shower image contains
the superimposed statement, “I think this is one of the sexiest pictures in my collection.”
(Id., Exh. 834.)
       6

       Ladies and gentlemen of the jury, the two charges contained in the Indictment in
       this case refer to the Maxtor hard drive. I need and wish to caution you at this
       point concerning evidence as to the Seagate hard drive.

       Evidence that an act was done or that an offense may have been committed
       by the defendant at some other time is not, of course, any evidence or proof
       whatever that at another time the defendant performed a similar act or
       committed a similar offense, including the offenses charged in this
       Indictment. Evidence of a similar act or offense may not be considered by
       the jury in determining whether the defendant actually performed the
       physical acts charged in this Indictment, nor may such evidence be
       considered for any other purpose whatever unless the jury first finds beyond
       a reasonable doubt, from other evidence in the case standing alone, that the
       defendant physically did the acts charged in the Indictment. If the jury
       should find beyond a reasonable doubt from other evidence in the case the
       defendant did the act or acts alleged in the counts under consideration, the
       jury may then consider the evidence as to an alleged earlier act of a like
       nature in determining the state of mind or intent with which the defendant
       actually did the act or acts charged in the Indictment.

       It is also offered for the purpose of identity, that it was the defendant that
       did the acts, as well as knowledge on the part of the defendant that the acts
       have been performed.

       Of course, I want to again emphasize that you will hear evidence of other
       digital images contained in the Government’s 800 series of exhibits that

                                             -9-
According to the government the superimposed text on the photographs directly

connected Burgess to the images of R.C., showed he was aware of the contents of

the Seagate drive, and, because some of the child pornography on the Seagate

Drive was identical to that on the Maxtor drive, was evidence from which the jury

could infer he had knowledge of the contents of the Maxtor drive, specifically the

pictures charged in the indictment.

       Burgess called several witnesses who testified he never acted

inappropriately around children. One of these witnesses was Deshaise, R.C.’s

legal guardian and chaperone of all three girls at the Runna-A-Mucca motorcycle

rally. Deshaise testified she was with the girls at all times in the motel room and

they were never alone with Burgess. On cross examination the government

questioned Deshaise regarding the circumstances surrounding twelve more images

of R.C. taken in the motel room in Winnemucca and also found on the Seagate

hard drive (they were in addition to the four already admitted). 7 The government

       were found on the Seagate hard drive that the Government alleges were
       possessed by the defendant. You may consider this evidence only as it
       bears on the defendant’s intent, the identity of the defendant, the
       defendant’s knowledge and the absence of a mistake, and for no other
       purpose. Of course, the fact that the defendant may have possessed these
       images does not mean that the defendant necessarily committed the act
       charged in this case.

(R. Vol. II at 615-16.)


       7
        Some of these images include the same image of R.C. contained in Exhibits 816
and 834, but with additional material. In Exhibit 832 an oval containing a much younger

                                          -10-
offered the pictures to rebut Deshaise’s testimony that the girls were adequately

chaperoned and Burgess could not have taken the pictures. The pictures were

admitted over Burgess’ objection and without explanation.

       The jury found Burgess guilty of both counts.

D. Sentencing

       The presentence report (PSR) calculated a total offense level of 37 and a

criminal history category I. 8 Burgess objected to the PSR’s use of both an

enhancement under USSG §2.2(b)(4) (vulnerable victim) and an enhancement

under USSG § 3A1.1(b)(1) (vulnerable victim) as double counting. He also

claimed an enhancement under USSG §2.2(b)(5) (use of a computer) was not

applicable because the hard drive was not a computer. Finally, he claimed he was

entitled to a two-level reduction of his offense level under USSG § 2G2.2(b)(1).

The court rejected the objection regarding use of a computer but agreed as to the

vulnerable victim enhancement and therefore reduced the total offense level to

35. 9 The court further determined Burgess was not entitled to a two point

picture of R.C. is superimposed to the side of the sexually explicit picture of R.C. The
same picture appears again in Exhibit 848 without text. Exhibit 833 is a composite of
R.C. as well as a friend, both in various states of undress; the superimposed text reads,
“Gee . . . you think this might be the reason why your daddy doesn’t want his 14-yr-old
daughter spending the night in a motel room with me.” (R. Sealed Vol. II, Exhs. 827,
832, 848.)
       8
       The November 1, 2007 Edition of the United States Sentencing Guidelines
Manual was used for sentencing.
       9
           The district court ruling on these objections is not at issue on appeal.

                                               -11-
reduction under U.S.S.G § 2G2.2(b)(1) in light of his conviction for transporting

the child pornography across state lines. It declined to sentence Burgess below

the guideline recommendation, imposing a sentence of 180 months imprisonment

on Count One and 120 months imprisonment on Count Two, the sentences to run

concurrently.

      Burgess appeals from the denial of his motion to suppress evidence, the

admission of 16 images from the Seagate hard drive and the length of his

sentence.

                                 II. DISCUSSION

A. Motion to Suppress

      1. Standard of Review

      “When reviewing the district court’s denial of a motion to suppress, we

view the evidence in the light most favorable to the government and accept the

district court’s factual findings unless they are clearly erroneous.” United States

v. Grimmett, 439 F.3d 1263, 1268 (10th Cir. 2006). “The ultimate question of

reasonableness under the Fourth Amendment is a legal conclusion that we review

de novo.” Id. Burgess claims the search of his hard drive amounted to a general

search prohibited by the Fourth Amendment and the original warrant lacked

sufficient particularity to justify the agent’s search of the images on his hard

drive. The government maintains the search was within the scope of the warrant

and, in any event, a warrant was unnecessary because the hard drives and laptop

                                         -12-
could be searched as well as seized pursuant to the automobile exception.

       2. Computer Search

              a. Automobile Exception

       The Fourth Amendment protects the “right of the people to be secure in

their persons, houses, papers, and effects, against unreasonable searches and

seizures.” “[I]t is a cardinal principle that ‘searches conducted outside the

judicial process, without prior approval by judge or magistrate, are per se

unreasonable under the Fourth Amendment--subject only to a few specifically

established and well-delineated exceptions.’” United States v. Ross, 456 U.S.

798, 825 (1982) (quoting Katz v. United States, 389 U.S. 347, 357 (1967)). One

of these specifically established exceptions is the “automobile exception” which

allows the police to “search an automobile and the containers within it where they

have probable cause to believe contraband or evidence is contained.” 10 California

v. Acevedo, 500 U.S. 565, 580 (1991).

       “The scope of a warrantless search based on probable cause is no narrower

— and no broader — than the scope of a search authorized by a warrant supported

by probable cause. Only the prior approval of the magistrate is waived; the

search otherwise is as the magistrate could authorize.” Ross, 456 U.S. at 823.

       10
           “[T]he justification to conduct such a warrantless search does not vanish once
the car has been immobilized,” Michigan v. Thomas, 458 U.S. 259, 261 (1982), and
“[t]here is no requirement that the warrantless search of a vehicle occur
contemporaneously with its lawful seizure.” United States v. Johns, 469 U.S. 478, 484
(1985).

                                           -13-
“When a legitimate search is under way, and when its purpose and its limits have

been precisely defined, nice distinctions between closets, drawers, and containers,

in the case of a home, or between glove compartments, upholstered seats, trunks,

and wrapped packages, in the case of a vehicle, must give way to the interest in

the prompt and efficient completion of the task at hand.” Id. at 821.

      Against this legal backdrop, and relying on our holding in United States v.

Andrus, 483 F.3d 711 (10th Cir. 2007), cert. denied, 128 S. Ct. 1738 (2008), the

government urges us to apply the automobile exception not only to the seizure of

the laptop and hard drives but to the search of those items as well. Andrus

involved a father’s actual or apparent authority to consent to the search of a

computer located in their shared residence but belonging to his absent adult son.

In discussion of reasonable expectations of privacy we likened a computer to a

suitcase or briefcase. Id. at 718. Because “[a] personal computer is often a

repository for private information the computer’s owner does not intend to share

with others” and “intimate information is commonly stored on computers, it

seems natural that computers should fall into the same category as suitcases,

footlockers, or other personal items that command a high degree of privacy.” Id.

(quotations omitted). The government constructs this syllogism: 1) the

expectation of privacy of computer contents has been likened to that of a suitcase

or briefcase (Andrus); 2) the automobile exception to the warrant requirement

permits, with probable cause, the search of containers found in the automobile –

                                         -14-
even locked suitcases and briefcases, Acevedo, 500 U.S. at 580; therefore 3)

police may (with probable cause, but without a warrant) search computers and

hard drives found in automobiles, Burgess’ motor home included.

       Burgess does not quarrel about the search of his motor home for drugs. 11

Rather, he contends the application of the automobile exception to search the

computer and hard drives found in his motor home would grant police “the

authority to forensically analyze and conduct a general search of any computer

found in any automobile which was subject to a valid search under the automobile

exception.” (Appellant’s Reply Br. at 2.) While a computer may be a container,

because of the amount of personal information stored within, Burgess argues it is

a virtual home. He says in this “age of the laptop computer,” such an

“extraordinary expansion” of the automobile exception would “destroy a citizen’s

expectation of privacy in his or her computer.” (Id.)

       The Supreme Court’s Fourth Amendment jurisprudence has not directly

addressed this issue. Moreover, the parties have cited no case law which either

allows or prohibits computer equipment searches under the automobile exception

and our research has failed to uncover such authority.



       11
          See United States v. Stewart, 473 F.3d 1265, 1270 (10th Cir. 2007) (“A canine
alert gives rise to probable cause to search a vehicle. This is so even when the dog alert
occurs during a warrantless sniff on the exterior of a vehicle during a lawful traffic stop
because such sniffs do not implicate the Fourth Amendment.” (citation and quotations
omitted).

                                            -15-
      At first blush, there appears no reason to treat computers differently than,

for instance, a locked briefcase in the locked trunk of an automobile. There is a

privacy expectation for a briefcase or suitcase, which may contain very personal

and confidential papers – particularly when well secured in the trunk of a car.

Yet the automobile exception subjects the briefcase to search. So why not the

computer? What is the difference between a file cabinet, suitcase or briefcase and

a computer? It might lie in the sheer range and volume of personal information

the computer may contain. United States v. Otero, 563 F.3d 1127, 1132 (10th

Cir. 2009) (“development of personal computer . . . increases . . . ability to

conduct a wide-ranging search”).

       “[A]nalogies to closed containers or file cabinets may lead courts to

‘oversimplify a complex area of Fourth Amendment doctrines and ignore the

realities of massive modern computer storage.’” United States v. Carey, 172 F.3d

1268, 1275 (10th Cir. 1999) (quoting Raphael Winick, Searches and Seizures of

Computers and Computer Data, 8 Harv. J.L. & Tech. 75, 104 (1994)); see also

United States v. Walser, 275 F.3d 981, 986 (10th Cir. 2001) (“analogies to other

physical objects . . . do not often inform the situations we now face as judges

when applying search and seizure law”); United States v. Campos, 221 F.3d 1143,

1148 (10th Cir. 2000) (“the storage capacity of computers may require law

enforcement officers to take a special approach”). In Andrus, we “tentative[ly]”

characterized a computer as a container akin to a suitcase or locked footlocker,

                                         -16-
but we did so to emphasize the high expectation of privacy for this particular type

of “container,” not to permit promiscuous searches under the automobile

exception. 483 F.3d at 718. And a notable distinction may exist between

authority to seize a computer and authority to search its contents.

      In Carey, we stated,

      Where officers come across relevant documents so intermingled with
      irrelevant documents that they cannot feasibly be sorted at the site,
      the officers may seal or hold the documents pending approval by a
      magistrate of the conditions and limitations on a further search
      through the documents. The magistrate should then require officers
      to specify in a warrant which type of files are sought.

172 F.3d at 1275. Historically, there is substantial support for the notion a

warrantless seizure is valid but a warrantless search is not.

      [I]f there is probable cause to believe [an object] contains
      contraband, the owner’s possessory interest in the container
      must yield to society’s interest in making sure that the
      contraband does not vanish during the time it would take to
      obtain a warrant. The item may be seized temporarily. It does
      not follow, however, that the container may be opened on the
      spot. Once the container is in custody, there is no risk that
      evidence will be destroyed. Some inconvenience to the officer
      is entailed by requiring him to obtain a warrant before opening
      the container, but that alone does not excuse the duty to go
      before a neutral magistrate.

Texas v. Brown, 460 U.S. 730, 749-50 (1983) (plurality) (J. Stevens, concurring).

That, of course, was the rationale underlying United States v. Chadwick, 433 U.S.

1 (1977) (search of double locked footlocker found in automobile unreasonable),

and Arkansas v. Sanders, 442 U.S. 753 (1979) (search of seized suitcase found in


                                         -17-
taxi unreasonable), but that rationale was rejected in California v. Acevedo, 500

U.S. 565, 579 (1991), in favor of a bright line rule: “We therefore interpret

Carroll as providing one rule to govern all automobile searches. The police may

search an automobile and the containers within it where they have probable cause

to believe contraband or evidence is contained.” Acevedo involved a paper bag

full of marijuana in the trunk of a car but the court saw no reason to distinguish

that sack, which would be an unlikely container of private papers, from a

briefcase, which very well might. In a concurring opinion Justice Scalia noted

anomalies in dealing with vehicle searches, saying:

      I agree with the dissent that it is anomalous for a briefcase to be
      protected by the "general requirement" of a prior warrant when it is
      being carried along the street, but for that same briefcase to become
      unprotected as soon as it is carried into an automobile. On the other
      hand, I agree with the Court that it would be anomalous for a locked
      compartment in an automobile to be unprotected by the "general
      requirement" of a prior warrant, but for an unlocked briefcase within
      the automobile to be protected. I join in the judgment of the Court
      because I think its holding is more faithful to the text and tradition of
      the Fourth Amendment, and if these anomalies in our jurisprudence
      are ever to be eliminated that is the direction in which we should
      travel.

Id. at 581.

       Practically speaking, the forensic search of a hard drive (or its equivalent,

such as a flash drive 12) will rarely be conducted at the “site” while searching an

      12
          “Flash drives” are solid state memory devices that can comfortably be carried
on a key chain. They can be used, usually thru a USB port, much like an external hard
drive. They hold tremendous amounts of data, commonly having 2 to 32 GB of memory.
One manufacturer has recently announced the release of a 256 GB flash card, which

                                         -18-
automobile, given the potential to corrupt or lose evidence. Arguably, requiring

the government to secure a warrant prior to searching the contents of a properly

seized computer is typically not overly burdensome in light of the privacy

interests at stake. However, sometimes the police may not resort to forensic

programs like EnCase. Assuming probable cause to do so, they might simply turn

the computer on and conduct a superficial search. Nothing in Acevedo suggests

either type of search (limited or on site forensic) would be impermissible without

a warrant, but seemingly well settled matters are subject to change. 13 Last term in

Arizona v. Gant, 129 S. Ct. 1710, 1722 (2009), the Court retreated from clear

language in New York v. Belton, 453 U.S. 454 (1981). Belton said, “when a

policeman has made a lawful custodial arrest of the occupant of an automobile, he

may, as a contemporaneous incident of that arrest, search the passenger

compartment of that automobile.” 453 U.S. at 460 (footnote omitted). After Gant

the rule is “Police may search a vehicle incident to a recent occupant’s arrest only

if the arrestee is within reaching distance of the passenger compartment at the



would equal or exceed the hard drive capacity of many contemporary laptop computers.
See, http://www.physorg.com/news167461888.html.
        13
           Doing so would be much like searching a cell phone for recent calls (in and
out), information contained in the address book, image files (still or digital video), audio
files (including phone messages) or other digital information. The memory cards,
available in some cell phones can, like flash drives, hold vast amounts of information,
including image and data files. See, for instance
http://www.sandisk.com/Products/Item(2537)-SDSDQ-8192-A11M-SanDisk_microSDH
C_8GB_Card_with_SD_Adapter.aspx.


                                            -19-
time of the search or it is reasonable to believe the vehicle contains evidence of

the offense of arrest.” Gant, 129 S. Ct. at 1723. In spite of clear language in

Acevedo, one might speculate whether the Supreme Court would treat laptop

computers, hard drives, flash drives or even cell phones as it has a briefcase or

give those types of devices preferred status because of their unique ability to hold

vast amounts of diverse personal information. Interesting as the issue may be, we

need not now resolve it because the search of Burgess’ hard drives was authorized

by a warrant.

             b. Validity of the Warrant

       Burgess argues the initial search warrant authorizing a search of “computer

records” and “items of personal property which would tend to show a conspiracy

to sell drugs” was overbroad. (R. Vol. I at 130.) “The Fourth Amendment

requires not only that warrants be supported by probable cause, but that they

particularly describ[e] the place to be searched, and the persons or things to be

seized.” Otero, 563 F.3d at 1131 (quotations omitted). “The modern

development of the personal computer and its ability to store and intermingle a

huge array of one’s personal papers in a single place increases law enforcement’s

ability to conduct a wide-ranging search into a person’s private affairs, and

accordingly makes the particularity requirement that much more important.” Id.

at 1132. “Because of this, our case law requires that warrants for computer

searches must affirmatively limit the search to evidence of specific federal crimes

                                          -20-
or specific types of material.” Id. (quotations omitted). However, we must keep

in mind “[a] reviewing court is to interpret search warrant affidavits in a common

sense and realistic fashion.” Grimmett, 439 F.3d at 1270.

      We agree with the district court; “the pertinent documents could have been

more artfully prepared.” (Id. at 88.) We also agree the officers had probable

cause to seize the computer equipment and could do so without a warrant under

the automobile exception. Although a closer call, we further agree the warrant to

search “contained sufficiently particularized language” creating “a nexus” with

the crime to be investigated – drug trafficking – and therefore was not overly

broad. Id. at 1271. The warrant authorized the search of Burgess’ motor home

for “certain property and evidence to show the transportation and delivery of

controlled substances, which may include but [is] not limited to” controlled

substances, paraphernalia, chemicals, and containers. (Id. at 130.) It also

authorized a search for “computer records” and for “items of personal property

which would tend to show conspiracy to sell drugs, including pay-owe sheets,

address books, rolodexes, pagers, firearms and monies.” (Id.)

      The inclusion of “computer records” amongst a host of other physical items

might seem to be an anomaly. Nevertheless, the warrant authorizes such a search

and provides context for determining its scope. The issue here relates to the

breadth of the search authorized. If the warrant is read to allow a search of all

computer records without description or limitation it would not meet the Fourth

                                         -21-
Amendment’s particularity requirement. United States v. Riccardi, 405 F.3d 852,

862 (10th Cir. 2005); 14 United States v. Leary, 846 F.2d 592, 600 (10th Cir.

1988). But “a word is known by the company it keeps.” S.D. Warren Co. v.

Maine Bd. of Envtl. Prot., 547 U.S. 370 (2006) (dealing with statutory

construction). The search, in general, was limited to evidence of drugs and drug

trafficking and, as it relates to the computer, was limited to the kind of drug and

drug trafficking information likely to be found on a computer, to wit (as the

warrant says): “pay-owe sheets, address books, rolodexes” and “personal property

which would tend to show conspiracy to sell drugs.” (Id. at 130.) The latter

could reasonably include “trophy photos.”

      Paragraph 17 of Schmitt’s affidavit explicitly included “photographs of

coconspirators or photographs of illegal narcotics” among the types of items to be

included in the requested search. (Id. at 133.) The warrant, itself, does not

      14
          In Riccardi, we held the seizure of computer equipment was permissible, but the
subsequent warrant authorizing the search “was not limited to any particular files, or to
any particular federal crime” and therefore violated the Fourth Amendment. 405 F.3d at
862. The warrant authorized the search of Riccardi’s computer:

      and all electronic and magnetic media stored therein, together with all
      storage devises [sic], internal or external to the computer or computer
      system, including but not limited to floppy disks, diskettes, hard disks,
      magnetic tapes, removable media drives, optical media such as CD-ROM,
      printers, modems, and any other electronic or magnetic devises used as a
      peripheral to the computer or computer system, and all electronic media
      stored within such devises.

Id. (emphasis added).


                                          -22-
explicitly instruct officers to look for image files on the hard drive, but the

affidavit was incorporated into the warrant and is, at least, an aid to interpretation

of the term used in the warrant – computer records.

      Our reading of the scope of the “computer records” subject to search,

narrowing it to looking for drug related evidence, comes from the text of the

warrant, with due regard to context, coupled with the specifics of the supporting

affidavit, see Grimmett, 439 F.3d at 1271; United States v. Brooks, 427 F.3d 1246

(10th Cir. 2005), and is reinforced by the executing officer’s (Hughes)

understanding of and respect for the narrow scope authorized by the search

warrant. Hughes was only looking for “trophy photos” when he came upon the

child pornography. 15

             c. Scope of Search

        Burgess claims the scope of the search violated the Fourth Amendment

under our holding in Carey, because Agent Hughes “employed none of the

      15

       “While the warrant does not explicitly instruct officers to look solely for
      those text files containing child pornography, in context-and certainly in the
      view of the officers conducting the search-the restrictions placed upon
      searches for image files also apply to the other types of files. In other
      words, although the language of the warrant may, on first glance, authorize
      a broad, unchanneled search through Brooks's document files, as a whole,
      its language more naturally instructs officers to search those files only for
      evidence related to child pornography. In this light, the warrant should
      be-and was-read by officers to implicitly place the same restriction (i.e., to
      locate child pornography) on the scope of the entire search.”

Brooks, 427 F.3d at 1252.

                                           -23-
methods suggested by this Court in Carey to avoid searching files which would

not be related to any drug offense.” (Appellant’s Reply Br. at 7.) And it is true

that Hughes began his search by previewing photographs contained in the Maxtor

hard drive.

      As in this case, the officer in Carey inadvertently discovered an image of

child pornography while searching for electronic evidence of drug activity. After

opening the first file, the officer in Carey temporarily abandoned the search for

drug evidence and proceeded to look through the hard drive for more images of

child pornography. We determined the extension of the search to locate further

evidence of child pornography exceeded the scope of the warrant authorizing a

search for evidence of drug crimes. Here Hughes immediately stopped the

preview upon seeing an instance of suspected child pornography and obtained

another warrant to search for pornography. Beyond that obvious and significant

difference between this case and Carey, it is tempting, as Burgess suggests, to

over read Carey. But the Carey holding was limited. Both the majority and the

concurring opinions were careful to warn that the case was fact intense. Carey,

172 F.3d at 1276 (“[W]e are quick to note these results are predicated only upon

the particular facts of this case, and a search of computer files based on different

facts might produce a different result.”).

      While “[o]fficers must be clear as to what it is they are seeking on the

computer and conduct the search in a way that avoids searching files of types not

                                         -24-
identified in the warrant,” Walser, 275 F.3d at 986, “a computer search may be as

extensive as reasonably required to locate the items described in the warrant”

based on probable cause. Grimmett, 439 F.3d at 1270 (quotation omitted). And

“[t]his Court has never required warrants to contain a particularized computer

search strategy.” Brooks, 427 F.3d at 1251. Carey dicta suggested methods to

constrain searches, keying on the type of files identified in the warrant, file

names, key word searches, directory structure (file organization), etc. 172 F.3d at

1276. The warrant here did not direct the search by describing file name

extensions (.doc,. wpd, .txt, .jpg, .gif, etc.), 16 file names or directory structure.

Rather the limitation on the scope of this search was explicitly constrained by

content – computer files containing evidence of drug use or trafficking. Such

files could take many forms. Pay-owe sheets could be generic text files (.txt) or

word processing documents, e.g. Microsoft Word (.doc, .docx, .dot, .dotx, etc.),

Corel WordPerfect (.wpt, .wpk, .wpd, .wp7, etc.), or other word processing

programs and, of course, there is the ubiquitous .pdf from Adobe. 17 Address


       16
         A file extension consists of one to five characters and informs a computer’s
operating system what program to utilize in order to open a particular file. There are
thousands of filename extensions.
http://www.sharpened.net/glossary/definition.php?fileextension.
       17
          Open-source applications like Abiword (.abw), KWord (.kwd), and OpenOffice
(.odt, .odm, .odf, etc.), or newer online word processors like Google Docs (which allows
you to download the document in a number of file formats) complicate the issue even
further.


                                           -25-
books or the electronic version of a rolodex might be found in Outlook (.pst) or

other Email program files or they could be in spreadsheets such as Excel (.xls,

.xlsb, .xltx, etc.), Lotus 1-2-3 (.wks, .wk4, etc.), Quattro Pro (.qpw) Quicken

(.qsd, .qdf, .qel, etc.), or OpenOffice (.ods, .ots, etc.). Or they could be database

files like Access (.accdb, .mdb, .maf, .mar, etc.) or Paradox (.db).

       It is unrealistic to expect a warrant to prospectively restrict the scope of a

search by directory, filename or extension or to attempt to structure search

methods – that process must remain dynamic. While file or directory names may

sometimes alert one to the contents (e.g., "Russian Lolitas," "meth stuff," or

"reagents"), illegal activity may not be advertised even in the privacy of one's

personal computer – it could well be coded or otherwise disguised. 18 The

directory structure might give hints as to an effective search strategy, but could

just as well be misleading and most often could not effectively, or even

reasonably, be described or limited in a warrant. Keyword searches may be

useful in locating suspect files, but not always. In this case, for instance, some of

the pictures of R.C. contained lurid text (see n.5 & 7), which, if searchable, might

lead an investigator to those images by use of keyword searches. But that text

does not appear in the filename, meaning it would not be revealed by a filename

       18
           Hughes testified to having seen computer files in other cases describe pay-owe
sheets as “auto repair bills,” marijuana as “green paint,” and cocaine as “white paint.” (R.
Vol. I at 248.) There was no evidence of deliberate concealment in this case; some of the
filenames are incriminating. See n.16. However, other file names gave little or no
indication of the file’s content. See discussion on the next page.

                                           -26-
search. And if the text was an embedded graphic (rather than embedded text) it

might not be revealed even in a word search of the entire document. Moreover

some of the pictures of R.C. ( Exhibits 830-834) had the following path: 07 301

8\8Hold\RC2007\May\252627\Towel\ and indescript filenames, such as

Img_5777_875.jpg. The path and filename of one particularly graphic image

(Exhibit 816 – lurid text superimposed) was: 07 301 8\8\Als_u621x2a.jpg. On

the other hand the path and/or filename may sometimes give an obscure hint as to

the content. For instance three of the pornographic child pictures from the

Maxtor and Seagate hard drives (Exhibits 805, 807 and 808) had this path: 07 301

8\8\Files\SG\Kp\Amateur Access\DCP\ (emphasis added). But the file names,

such as DCO01352.jpg, gave no hint as to file content

      In summary, it is folly for a search warrant to attempt to structure the

mechanics of the search and a warrant imposing such limits would unduly restrict

legitimate search objectives. One would not ordinarily expect a warrant to search

filing cabinets for evidence of drug activity to prospectively restrict the search to

"file cabinets in the basement" or to file folders labeled "Meth Lab" or

"Customers." And there is no reason to so limit computer searches. But that is

not to say methodology is irrelevant.

      A warrant may permit only the search of particularly described places and

only particularly described things may be seized. As the description of such

places and things becomes more general, the method by which the search is

                                         -27-
executed become more important – the search method must be tailored to meet

allowed ends. And those limits must be functional. For instance, unless

specifically authorized by the warrant there would be little reason for officers

searching for evidence of drug trafficking to look at tax returns (beyond verifying

the folder labeled "2002 Tax Return" actually contains tax returns and not drug

files or trophy pictures). 19

       Respect for legitimate rights to privacy in papers and effects requires an

officer executing a search warrant to first look in the most obvious places and as

it becomes necessary to progressively move from the obvious to the obscure.

That is the purpose of a search protocol which structures the search by requiring

an analysis of the file structure, next looking for suspicious file folders, then

looking for files and types of files most likely to contain the objects of the search

by doing keyword searches. But in the end, there may be no practical substitute

for actually looking in many (perhaps all) folders and sometimes at the documents

contained within those folders, and that is true whether the search is of computer

files or physical files. It is particularly true with image files.

       We have not abandoned the concerns expressed in Carey. See Otero, 563

F.3d at 1135-36; Brooks 427 F.3d at 1251-52; Riccardi, 405 F.3d at 862; Walser,

275 F.3d at 986 (agent used a clear search methodology searching records where

       19
        We recognize a unique case might justify looking at tax returns for evidence of
payments related to drug activities such as purchases of manufacturing supplies or
equipment.

                                          -28-
evidence might logically be found); Campos, 221 F.3d at 1148. The preview

technique may be problematic in other contexts but we are not prepared to

condemn it in this case. We must be guided by practical realities and several are

readily apparent. First, Hughes was not previewing all files, only image files and

his search was properly targeted – “trophy photos.” Second, had Hughes omitted

the preview and, instead, waited to do a structured search on the copied files (for

instance, by looking at the filenames of .jpg files) his search for "trophy photos"

would eventually and inevitably have led to discovery of the charged images. 20

Third, as our cases seem to require, Hughes immediately closed the gallery view

when he observed a possible criminal violation outside the scope of the warrant's

search authorization and did not renew the search until he obtained a new warrant.

Fourth, in general a structured approach may provide only the illusion of

protecting privacy interests, particularly when the search target is image files.

When a computer search for drug related evidence reveals filenames strongly


      20
         As trial evidence demonstrated some of the file names in Burgess’ hard drive
were particularly descriptive and a review of the names would have legitimately aroused
the suspicions of an agent trained in child pornography and inevitably led to the second
search warrant. See United States v. White, 326 F.3d 1135, 1138 (10th Cir. 2003) (“the
exclusionary rule is inapplicable if the evidence inevitably would have been discovered
by lawful means.”). For example, one folder named “Nastiest11yoSeries” had a
subfolder titled “Sausage” containing pornographic images of a young girl. (R. Vol. II at
574.) Another folder titled “AGE” contained subfolders titled “03,” “04,” “05,” “06,”
“07,” “08,” “09,” “10” and “11.” (Id. at 569-70.) Each subfolder folder contained images
of children the same age as described in the title engaged in sexually exploitive conduct.
One file was entitled “Lolita,” a term which Agent Hughes testified is often seen in the
investigation of child pornography. (Id. at 573-74.)

                                          -29-
suggesting pornography an officer might be required to get another warrant before

proceeding. But if the suggestive file names did not amount to probable cause he

could keep searching for drug evidence, ultimately resulting in opening most files

to make sure they were not deceptively labeled. And eventually the child

pornography would be revealed. The only difference is that it would be

discovered later, rather than earlier. That is particularly true in this case where

the search was for image files, which could be buried almost anywhere. 21 Fifth,

Burgess complains the particular methodology used in this case was overbroad,

yet he offers no alternative methodology that would protect his legitimate

interests and also permit a thorough search for evidence of drug trafficking. See

Brooks, 427 F.3d at 1251 (“[N]or has Brooks suggested how the search in this

case would have been different with a scripted search protocol.”).

      On these facts, we cannot say the Fourth Amendment was violated.




      21
          It would seem odd to require an officer who merely suspects pornography to
stop the search for evidence of drug trafficking. The concurring opinion in Carey
suggests it would not be necessary. “[I]f the record showed that Detective Lewis had
merely continued his search for drug-related evidence and, in doing so, continued to come
across evidence of child pornography, I think a different result would be required.” 172
F.3d at 1277. It would also seem odd to require the officer to attempt to obtain a
pornography warrant before confirming his suspicions about a file. Especially so in this
case because if the suspicions did not, in the view of a judge, amount to probable cause
the officer could continue his structured search for evidence of drug trafficking and
eventually return to and open the suspicious file (and multiple others) to guard against
deceptive labeling.

                                          -30-
              d. Leon Good Faith

       Even if the warrant was not sufficiently particularized to comply with the

Fourth Amendment, the evidence need not be excluded if the search qualified

under the good faith doctrine of United States v. Leon, 468 U.S. 897 (1984).

Whether the “good faith exception” to the exclusionary rule should be applied is a

question of law, subject to de novo review by this Court. 22 Leary, 846 F.2d at

606. In Leon, the Supreme Court held the purpose of the exclusionary rule is to

deter police misconduct and “suppression of evidence obtained pursuant to a

warrant should be ordered only on a case-by-case basis and only in those unusual

cases in which exclusion will further” that purpose. 468 U.S. at 918. “Where an

officer acting with objective good faith obtains a search warrant from a detached

and neutral magistrate and the executing officers act within its scope, there is

nothing to deter.” United States v. Nolan, 199 F.3d 1180, 1184 (10th Cir. 1999).

       Burgess argues the Leon exception does not apply here because the warrant

was “so facially deficient . . . the executing officers [could] not [have] reasonably

presume[d] it to be valid.” Leon, 468 U.S. at 923. It is the government’s burden

to prove “its agents’ reliance upon the warrant was objectively reasonable.”

United States v. Corral-Corral, 899 F.2d 927, 932 (10th Cir. 1990) (quotations


       22
           The parties briefed and argued the issue in the district court, which did not reach
it, and it was briefed on appeal. Thus, we may consider it. See United States v. Harrison,
566 F.3d 1254, 1256 (10th Cir. 2009) (proceeding directly to Leon analysis not decided
by the district court).

                                            -31-
omitted).

      “Just as reviewing courts give ‘great deference’ to the decisions of judicial

officers who make probable-cause determinations, police officers should be

entitled to rely upon the probable-cause determination of a neutral magistrate

when defending an attack on their good faith for either seeking or executing a

warrant.” Id. at 939.

      It is the magistrate’s responsibility to determine whether the officer’s
      allegations establish probable cause and, if so, to issue a warrant
      comporting in form with the requirements of the Fourth Amendment.
      In the ordinary case, an officer cannot be expected to question the
      magistrate’s probable-cause determination or his judgment that the
      form of the warrant is technically sufficient.

Leon, 468 U.S. at 921.

      Burgess cites to two district court cases from other circuits to demonstrate

these officers could not reasonably believe the warrant was valid. In United

States v. Clough, the warrant authorized a search of computers for “a. text

documents of any variety, including e-mail, websites, records of chat sessions,

correspondence or shipping records; and b. digital images of any variety,

including still images and videos.” 246 F. Supp. 2d 84, 87 (D. Me. 2003). As the

court found, the warrant contained no restrictions on the search, no references to

statutes, and no references to crimes or illegality. Id. Again, in United States v.

Fleetwood Mgm’t Ltd., the warrant authorized a computer search for “any and all

data from the three seized computers, including, but not limited to certain types of


                                         -32-
data relating to the Ship’s operation, engineering, maintenance, pollution control

equipment, navigational charts, and crew.” 521 F. Supp. 2d 436 (E.D. Pa. 2007)

(quotations omitted). In neither case was the search restricted in any way by the

warrant. These cases only underscore the officers’ reasonable reliance on the

language of the warrant in this case limiting the search to evidence of drug

trafficking.

      Contrary to Burgess’ assertions, Agent Hughes did not contact the agency

attorney because he was confused about the scope of his search, he emphatically

stated his concern was the delay. Hughes knew he was looking for evidence of

drug possession and distribution and that such evidence would very likely be

contained in the digital images on the hard drive. At each step of the

investigation, the officers made every effort to comply with the law. Therefore,

even if the warrant was deficient, exclusion of the evidence would not be

necessary.

               e. Timeliness of Search

      Burgess argues the forty-four day delay in searching the computer violated

the Fourth Amendment. Because this issue was not raised below, we review for

plain error. Fed. R. Crim. P. 52(b).

      To notice plain error under Rule 52(b), the error must:

          (1) be an actual error that was forfeited; (2) be plain or obvious;
          and (3) affect substantial rights, in other words, in most cases the
          error must be prejudicial, i.e., it must have affected the outcome

                                         -33-
          of the trial. . . . Given plain error that affects substantial rights, an
          appellate court should exercise its discretion and notice such error
          where it either (a) results in the conviction of one actually
          innocent, or (b) seriously affect[s] the fairness, integrity or public
          reputation of judicial proceedings.

Walser, 275 F.3d 985. “We apply the plain error rule less rigidly when reviewing

a potential constitutional error.” Id.

      Because the warrant had expired by its own terms prior to the time Agent

Hughes began his forensic search of the hard drive, Burgess maintains the search

was warrantless and violated his Fourth Amendment rights. “The Fourth

Amendment does not specify that search warrants contain expiration dates.”

United States v. Sims, 428 F.3d 945, 955 (10th Cir. 2005); see also United States

v. Johns, 469 U.S. 478, 487 (1985) (while police officers may not indefinitely

retain possession of a vehicle and its contents before they complete a valid

warrantless search, the owner of the property must prove delay in the completion

of a search was unreasonable because it adversely affected a privacy or

possessory interest). Specific time limits are imposed by the Federal Rules of

Criminal Procedure which require that a “warrant must command the officer to . .

. execute the warrant within a specified time no longer than 10 days.” Fed. R.

Crim. P. 41(e)(2)(A)(i). “The restrictions in Rule 41 not only ensure that

probable cause continues to exist, but also that it is the neutral magistrate, not the

executing officers, who determines whether probable cause continues to exist.”

United States v. Syphers, 426 F.3d 461, 469 (1st Cir. 2005) (quotation omitted).

                                           -34-
But “violations of Rule 41 alone should not lead to exclusion unless (1) there was

prejudice in the sense that the search might not have occurred or would not have

been so abrasive if the Rule had been followed, or (2) there is evidence of

intentional and deliberate disregard of a provision in the Rule.” Sims, 428 F.3d

955 (quotations omitted). The same analysis applies whether it is “a violation of

the warrant itself,” or “a violation of Rule 41 per se.” Id. There is no evidence

either of these conditions were met here.

      Burgess points us to United States v. Mitchell where the Eleventh Circuit

held an initial seizure of a hard drive was permissible, but “the detention of the

hard drive for over three weeks before a warrant was sought constitute[d] a

significant interference with Mitchell’s possessory interest.” 565 F.3d 1347, 1351

(11th Cir. 2009) (emphasis added). The court held the delay in securing a warrant

was unreasonable because the government had no compelling excuse. Id. Here,

the warrant to search was secured prior to the hard drives being seized 23 and there

is no indication the officers were not diligent in executing the search. Probable

cause to search was unaffected by the delay and the reasons to search the

computer and hard drives did not dissipate during the month and a half the items

sat in an evidence locker. Burgess has not identified any prejudice from the delay

and the only readily apparent concern is that Burgess was temporarily denied

      23
         The motorhome was seized before the search warrant was issued. In a broad
sense, then, so was the computer equipment. But neither the laptop nor the hard drives
were separately seized (or searched) until after the warrant issued.

                                          -35-
access to his property. Moreover, any delay was due to Agent Hughes’ efforts to

make sure the job was done right. Our plain error analysis ends at the first step,

suppression of the evidence from the computer equipment is not required – there

was no error.

B. Admission of Evidence

      Burgess claims the court erred in admitting sixteen digital images from the

Seagate hard drive (four images admitted in the prosecution’s case-in-chief, and

twelve images admitted for impeachment of defense witness Dechaise – these

exhibits ought not be confused with the four pictures stipulated into evidence).

Early on, the defense stipulated to the admission of four pornographic pictures of

a child (see n.4), which appeared on both the Seagate drive and the Maxtor drive

(the four images on the Maxtor drive were specifically named in the indictment).

The images at issue here were only on the Seagate drive.

      As is his right, Burgess decided to put the government to its proofs, among

them that he intentionally possessed the charged pornographic images found on

the Maxtor drive, in effect denying knowledge of those images on his hard drives.

The government offered the Seagate pictures in order to show Burgess was aware

the Seagate drive, and inferentially the Maxtor drive, contained pornographic

pictures. The file structure on both drives was highly organized, both drives

contained child pornographic images and both drives had duplicate images and

other files personal to Burgess. One could reasonably infer that Burgess was

                                        -36-
aware of the contents of both drives. But the Seagate drive had an additional tie;

it contained many pictures of R.C. that were sexually suggestive or borderline

pornographic. Some of the photos of her had other pictures and/or lewd text

superimposed upon them, suggesting Burgess had taken the photographs and/or

had superimposed the text upon them. Tying him to those pictures might,

inferentially, tie him to the charged child pornography. Burgess claims the

admission of the pictures and text, while perhaps “marginally relevant” to show

Burgess knew the child pornography was on his hard drive, were unnecessary and

unduly prejudicial because their admission encouraged the jury to speculate about

Burgess’ perverted interest in a young girl with whom he had a trusting

relationship. (Appellant’s Br. at 24.)

      We review the district court’s admission of evidence under Rules 404(b)

and 403 for abuse of discretion. United States v. Cerno, 529 F.3d 926, 933 (10th

Cir. 2008) (Rule 403), cert. denied, 129 S.Ct. 1905 (2009); United States v.

Mares, 441 F.3d 1152, 1156 (10th Cir. 2006) (Rule 404(b)). “We will not reverse

a district court’s ruling if it fall[s] within the bounds of permissible choice in the

circumstances and is not arbitrary, capricious or whimsical.” Mares, 441 F.3d at

1157 (quotations omitted).

      Federal Rule of Evidence 404(b) provides:

      Evidence of other crimes, wrongs, or acts is not admissible to prove
      the character of a person in order to show action in conformity
      therewith. It may, however, be admissible for other purposes, such

                                          -37-
      as proof of . . . intent, . . . plan, knowledge, . . . or absence of
      mistake.

We “consider four factors in weighing the admissibility of evidence under Rule

404(b): (1) whether the evidence is offered for a proper purpose, (2) its relevancy,

(3) that the probative value of the evidence is not substantially outweighed by its

prejudicial effect, and (4) a limiting instruction is given if the defendant so

requests.” Mares, 441 F.3d at 1157 “Rule 404(b) is considered to be an inclusive

rule, admitting all evidence of other crimes or acts except that which tends to

prove only criminal disposition.” United States v. Tan, 254 F.3d 1204, 1208 (10th

Cir. 2001) (quotations omitted).

      However, even if relevant and offered for a proper purpose, Rule 404(b)

evidence may still be excluded under Rule 403 if its probative value “is

substantially outweighed by the danger of unfair prejudice, confusion of the

issues, or misleading the jury. . . .” Fed. R. Evid. 403. “In determining whether

evidence is properly admitted under Rule 403, we consider (1) whether the

evidence was relevant, (2) whether it had the potential to unfairly prejudice the

defendant, and (3) whether its probative value was substantially outweighed by

the danger of unfair prejudice.” Cerno, 529 F.3d at 933. To be inadmissible

under rule 403, evidence must do more than “damage the Defendant’s position at

trial,” it must “make[] a conviction more likely because it provokes an emotional

response in the jury or otherwise tends to affect adversely the jury’s attitude


                                           -38-
toward the defendant wholly apart from its judgment as to his guilt or innocense

[sic] of the crime charged.” Tan, 254 F.3d at 1211-12 (quotations omitted).

      Burgess essentially argues the court erred in admitting the first four images

because the government already presented evidence sufficient to show knowledge,

identity and intent to possess the charged images on the Maxtor hard drive. He

points to the government’s evidence suggesting he, in effect, admitted ownership

of the hard drives. The numerous photos of Burgess and his home along with his

personal correspondence on both the Seagate and Maxtor hard drives connected

him to both drives and some of the non-pornographic photos found on the Maxtor

drive were posted on Burgess’ website. Therefore, according to Burgess, the

highly prejudicial nature of the evidence relating to R.C. which implied an

improper relationship with a minor was not “vital” to the government’s proof.

See United States v. Garot, 801 F.2d 1241, 1247 (10th Cir. 1986) (“exhibits were

vital to proof of appellants’ knowledge”). Thus, Burgess maintains the images

and text were far more prejudicial than probative and allowed the jury to convict

Burgess, not for possession and transportation, but for other uncharged crimes.

Although it may be a factor, the test is not necessarily whether the evidence is

vital to the government’s case. Vitality is often a matter of perspective. Within

limits delineated in the Federal Rules of Evidence the government is entitled to

introduce all relevant, probative evidence at its disposal. The defense cannot be

heard to complain that the government has produced too much evidence of guilt.

                                        -39-
The Rule 403 test balances the probative value of (not necessarily the need for)

the evidence against its potentially unfairly prejudicial effect. That balancing is

for the trial judge. The remaining twelve images, some with accompanying text,

were not offered until Dechaise testified that Burgess had no opportunity to take

the pictures of the girls and her suggestion that the girls took the pictures

themselves. These twelve pictures were much like the four previously admitted.

According to the government, they were admissible to rebut the testimony of

defense witnesses who testified as to the defendant’s exemplary conduct around

children. These witnesses testified they had never seen Burgess behave

inappropriately with children and could not believe the man they knew as David

Burgess would be capable of possessing vast amounts of child pornography. The

government also claims they were admissible to impeach Deshaise’s testimony –

that Burgess was not alone with the young girls and the girls were sufficiently

chaperoned during the motorcycle rally. Burgess further complains these photos

were admitted without a limiting instruction. Such an instruction, however, was

never requested.

      In United States v. Schene, we affirmed the district court’s admission of

uncharged child pornography images to show intent and knowledge. 543 F.3d

627, 643 (10th Cir. 2008). We held the evidence was relevant and proper,

specifically noting the district court gave a limiting instruction on the matter. Id.;

see also United States v. Simpson, 152 F.3d 1241, 1249 (10th Cir.1998)

                                         -40-
(affirming the district court’s decision to admit similar evidence “to prove that (1)

[the defendant’s] possession of child pornography on his computer was not a

mistake or accident, and (2) he had knowledge of the nature of the material he

was receiving.”). We agree the first four pictures were admissible to show

Burgess’ knowledge and possession. As in Schene and Simpson, the district court

here carefully reviewed the entirety of the evidence the government wished to

offer and excluded all but what the court believed necessary to government’s

case. In addition, the court gave an instruction prior to the introduction and in the

instruction package sent to the jury explaining the very limited purpose for which

it was offered and admonishing the jury to consider it for no other purpose. We

find no abuse of discretion.

      The twelve additional photos with accompanying text is a closer call. Their

value for impeachment may have been cumulative; these twelve pictures were

much the same as the four pictures previously admitted over Burgess’ objection.

But the government’s position was that Burgess took the photographs. Its

arguments in that regard were undermined by the testimony of one of R.C.’s

companions at Winnemucca; the girl said she took the pictures. So the

superimposed captions on the photographs, suggesting Burgess took or edited

them, gained new importance and some of the twelve new photos contained

captions not present in the other four.




                                          -41-
      On the other hand Burgess’ conduct with real children was not the issue in

this trial; nor was his conduct at the motorcycle rally. The government does not

explain why it was necessary to introduce twelve rather than one or two

additional images for impeachment purposes (especially given the district court’s

determination that the four stipulated images and four additional Seagate images

were sufficient to prove Burgess’ intent and lack of mistake). Nonetheless, we

“afford great deference to the district court; review of a cold record is a poor

substitute for a trial judge’s intimate familiarity with the evidence and its role in

the context of the trial as a whole.” United States v. Hubenka, 438 F.3d 1026,

1036 (10th Cir. 2006) (quotations omitted). Considering whether to admit “more

of the same” is a judgment call best made by the trial judge. It is most difficult

for us to look at a cold record and decide if eight would be sufficient or four or

two. We may have reached a different conclusion but that does not make the trial

court’s decision an abuse of discretion.

      In any event, the admission of these photographs and texts does not call

into question the jury’s guilty verdict. Any error in admitting the photographs

was harmless. “A non-constitutional error, such as a decision whether to admit or

exclude evidence, is considered harmless ‘unless a substantial right of [a] party is

affected.’” United States v. Charley, 189 F.3d 1251, 1270 (10th Cir. 1999)

(quoting Fed. R. Evid. 103(a)). An error affecting a substantial right of a party is

an error which had a “substantial influence” on the outcome or which leaves one

                                           -42-
in “grave doubt” as to whether it had such effect. United States v. Rivera, 900

F.2d 1462, 1469 (10th Cir.1990) (quoting Kotteakos v. United States, 328 U.S.

750, 765 (1946)). “[W]e review the record as a whole.” Charley, 189 F.3d at

1270. “The question is not whether, omitting the inadmissible statements, the

record contains sufficient evidence for a jury to convict the defendant,” but

whether the evidence had a substantial influence on the jury’s decision. United

States v. Tome, 61 F.3d 1446, 1455 (10th Cir. 1995).

      The jury was presented with evidence Burgess possessed thousands of

images of child pornography, among them the charged images, which were

present on both hard drives. The hard drives also contained Burgess’ personal

photos and files. All the material on both hard drives, both legal and illegal, was

organized in a singular and sophisticated fashion. Putting aside all inferences of

an improper fascination with R.C., no reasonable jury could have reached a

conclusion other than the one reached here. There can be no doubt, let alone a

grave doubt, that Burgess knowingly possessed child pornography as he traveled

from Nevada into Wyoming.

C. Sentencing

      Under Gall v. United States, the Supreme Court set the procedure for the

district court’s imposition of a sentence:

      [A] district court should begin all sentencing proceedings by
      correctly calculating the applicable Guidelines range. As a matter of
      administration and to secure nationwide consistency, the Guidelines

                                         -43-
      should be the starting point and the initial benchmark. The
      Guidelines are not the only consideration, however. Accordingly,
      after giving both parties an opportunity to argue for whatever
      sentence they deem appropriate, the district judge should then
      consider all of the § 3553(a) factors to determine whether they
      support the sentence requested by a party. In so doing, he may not
      presume that the Guidelines range is reasonable. He must make an
      individualized assessment based on the facts presented . . . . After
      settling on the appropriate sentence, he must adequately explain the
      chosen sentence to allow for meaningful appellate review and to
      promote the perception of fair sentencing.

552 U.S. 38, 128 S. Ct. 586, 596-97 (2007).

      We review a sentence for abuse of discretion. Id. at 600. We review the

court’s legal conclusions de novo and its factual findings for clear error. United

States v. Kristl, 437 F.3d 1050, 1055 (10th Cir. 2006). A sentence is procedurally

unreasonable if the district court “fail[ed] to calculate (or improperly

calculate[ed]) the Guidelines range, treat[ed] the Guidelines as mandatory,

fail[ed] to consider the § 3553(a) factors . . . or fail[ed] to adequately explain the

chosen sentence.” Gall, 552 U.S. at 597.

      1. Procedural Error

             a. USSG §2.G2(b)

      Burgess claims the district court erred as a matter of law in interpreting

USSG § 2G2.2(b)(1) to prohibit the reduction of his offense level by two points.

This section provides if a defendant is convicted of a child pornography offense

with a base offense level of 22, the court will decrease the offense level by two

points if “the defendant’s conduct was limited to (B) the receipt or solicitation of

                                          -44-
material involving the sexual exploitation of a minor; and (C) the defendant did

not intend to traffic in, or distribute such material.” USSG § 2G2.2(b)(1). The

district court determined that, because Burgess’ conduct included transportation

of child pornography, not only receipt, he did not qualify for the reduction even

though Burgess did not intend to distribute the material.

        Burgess claims the court’s interpretation is in error because it is contrary to

guideline commentary defining distribution. “Distribution” is defined as:

        [A]ny act, including possession with intent to distribute, production,
        advertisement, and transportation, related to the transfer of material
        involving the sexual exploitation of a minor.

USSG § 2G2.2(b)(1)(C), cmt. n.1 (2007). Burgess argues the definition’s

alignment of the word “transportation” with the concept of “transfer” of child

pornography demonstrates the drafters’ intention to apply the two level reduction

to defendants who transport material without intending it be transferred to anyone

else.

        The Sixth Circuit has rejected this argument in a case nearly identical to

this one. See United States v. Fore, 507 F.3d 412 (6th Cir. 2007). In Fore, it was

uncontested there was “insufficient evidence that defendant intended to

‘distribute’ the images found in his vehicle,” but the government maintained “the

simple fact that defendant’s criminal conduct . . . also involved the interstate

transportation of child pornography in violation of 18 U.S.C. § 2252(a)(1),

disqualifie[d] defendant from receiving the reduction.” Id. at 415. The court

                                          -45-
began with the plain language of the guideline, recognizing “[s]entencing

guidelines should be read as they are written.” Id. (quotations omitted). The

court stated:

      The wording of U.S.S.G. § 2G2.2(b)(1) is neither complicated nor
      ambiguous. By its express terms, this Guideline permits a two-level
      reduction in the offense level only if a defendant meets three
      requirements: (1) his base offense level must be 22, in accordance
      with subsection (b)(1)(A); (2) under subsection (b)(1)(B), his
      conduct must be “limited” in scope of the receipt or solicitation of
      material involving the sexual exploitation of a minor; “and” (3)
      under subsection (b)(1)(C), he did not intend to traffic in or
      distribute such material. Here, defendant’s undisputed base offense
      level is 22. However, defendant has not met the second requirement
      because his criminal conduct was not limited to the receipt or
      solicitation of pornographic materials, but also encompassed the
      transportation of materials involving the sexual exploitation of a
      minor in interstate commerce in violation of 18 U.S.C. § 2252(a)(1),
      an offense that is separate and distinct from, and goes beyond, the
      mere receipt or solicitation of pornography proscribed by 18 U.S.C. §
      2252(a)(4)(B). We further note that U.S.S.G. § 2G2.2(b)(1) is
      devoid of any language suggesting that the offense of transporting
      child pornography in interstate commerce otherwise qualifies for the
      two-level decrease in a defendant’s offense level.

Id. For these reasons, the court held the district court properly denied defendant’s

request for a decrease in his base offense level. We find the Sixth Circuit’s

reasoning without flaw and adopt it here. The district court did not err in denying

Burgess’ request for a reduction under USSG § 2G2.2(b)(1).

                b. Other Procedural Issues

      On appeal, Burgess claims the district court treated the guidelines as

mandatory because, at sentencing, the court stated:


                                             -46-
      I do look at the other cases that have been prosecuted before this
      Court and really have to look in this case at the guidelines for
      guidance in imposing sentence in this case and will be imposing the
      sentence within the guideline range that has been . . . established.

(R. Vol. II at 1025.) Burgess also claims the court failed to provide a sufficient

explanation of the reasons for his sentence.

      Our review of the record reveals the district court’s statement regarding its

intention to sentence within the guideline range followed a complete analysis of

the evidence in this case as it bears on the § 3553(a) factors. The court then

continued to thoroughly assess the facts relevant to Burgess’ conduct. There is no

evidence the court considered the guidelines mandatory or failed to consider the

sentence in light of the § 3553(a) factors. Indeed, the court went well beyond

what we require. See United States v. Tindale, 519 F.3d 1057, 1065 (10th Cir.

2008) (“A one-sentence explanation accompanying a within-guidelines sentence --

in the absence of the need to address specific § 3553(a) arguments brought to the

district court’s attention -- satisfies the district court’s duty to impose a

procedurally reasonable sentence.”). The sentence is procedurally reasonable.

      2. Substantive Error

      The substantive aspect of a sentence relates to the length of the sentence

and we ask “whether the length of the sentence is reasonable considering the

statutory factors delineated in . . . § 3553(a).” United States v. Hamilton, 510

F.3d 1209, 1217-18 (10th Cir. 2007), cert. denied, 128 S. Ct. 1922 (2008).


                                          -47-
Stripped to its essence, Burgess argues his sentence was too long and points to

several cases and articles criticizing the guideline recommendations as too harsh

compared to the five-year minimum allowed under the statute. While recognizing

the district court correctly calculated Burgess’ guideline range as 168 to 210

months imprisonment, he claims the court unreasonably sentenced him to 180

months because he was merely “a first-time offender prosecuted for having a

private collection of pornography with him in his travels.” (Appellant’s Br. at

43.) We are not convinced by this characterization of the crime and the relevant

conduct appropriately considered by the district court. In this case, we could, but

need not, presume the district court’s guidelines sentence was reasonable. See

United States v. Navarreata-Medina, 554 F.3d 1312, 1313 (10th Cir. 2009) (a

sentence falling within a correctly calculated advisory range is entitled to a

rebuttable presumption of reasonableness). The district court’s extensive and

reasoned consideration of the facts and law is more than evident in the record.

Burgess’ sentence is not substantively unreasonable.

      AFFIRMED.




                                         -48-

```

---

## GROUP: _overhaul2/lake/cases/United States v. Caceres.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Caceres
type: case
citation: "440 U.S. 741 (1979)"
parallel_cite: "99 S. Ct. 1465; 59 L. Ed. 2d 733"
neutral_cite: 1979 U.S. LEXIS 83
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-04-13
docket: No. 76-1309
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
  opinion_url: "https://www.courtlistener.com/opinion/110049/united-states-v-caceres/"
  cluster_id: 110049
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Caceres
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[The Exclusionary Rule]]"
    role: Anchor
related:
  - "[[The Exclusionary Rule]]"
  - "[[Stone v. Powell]]"
  - "[[United States v. Calandra]]"
  - "[[United States v. Janis]]"
  - "[[United States v. Leon]]"
tags:
  - case
  - fourth-amendment
  - exclusionary-rule
  - agency-regulations
  - consensual-monitoring
  - deterrence
holding: "Evidence obtained in violation of an executive agency's internal regulations — here, IRS rules requiring prior authorization for consensual electronic monitoring — need not be excluded from a criminal trial where the agent's conduct violated neither the Constitution nor a federal statute; because the exclusionary rule rests on deterring constitutional violations, it lends no support to suppression for a mere regulatory breach, and the Court declined to adopt any rigid rule excluding all evidence obtained through such a violation."
aliases:
  - United States v. Caceres
  - "United States v. Caceres (1979)"
---

# United States v. Caceres

*440 U.S. 741 (1979)* (No. 76-1309) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 110049 → combined opinion 110049 (Stevens, J.; 440 U.S. 741, argued Jan. 8-9, 1979, decided Apr. 2, 1979). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*755`). S9 promotes. -->

## Background
While being audited, respondent Caceres offered a bribe to IRS Agent Yee. The IRS monitored and recorded three face-to-face conversations between them using a radio transmitter concealed on Yee. IRS regulations (the IRS Manual) prohibited such "consensual electronic surveillance" unless prior authorization was obtained through several layers of agency and, in some cases, Justice Department approval. Caceres moved to suppress the recordings because the required authorizations had not been properly secured. The District Court suppressed all three; the Ninth Circuit reversed as to the third tape (authorization was adequate) but agreed that the first two, made without proper authorization, had to be excluded. The Government sought review of that exclusion.

## Issue
Whether evidence obtained in violation of an agency's own internal regulations — regulations not required by the Constitution or by statute — must be excluded from the defendant's criminal trial.

## Rule
The Court began from the premise that neither the Constitution nor any Act of Congress required prior approval for consensual monitoring; only the IRS's self-imposed regulations were violated. Because the exclusionary rule exists to deter *constitutional* violations, it had no purchase where no constitutional right was infringed: "In view of our conclusion that none of respondent's constitutional rights has been violated here, either by the actual recording or by the agency violation of its own regulations, our precedents enforcing the exclusionary rule to deter constitutional violations provide no support for the rule's application in this case." — 440 U.S. at 755. ^pin-755

## Application
The Court declined to adopt any rigid rule excluding all evidence obtained through a regulatory violation. Forcing suppression for every departure from an agency's internal rules would take from the Executive its primary responsibility to fashion remedies for its own regulations — and might perversely lead agencies to write fewer or weaker rules, leaving the public *less* protected. Nor did a case-by-case approach favor suppression here, where the violation was neither deliberate nor prejudicial and did not affect any constitutional or statutory right. It was better, the Court reasoned, to have protective regulations like the IRS Manual's and tolerate occasional lapses than to discourage agencies from adopting such rules at all.

## Conclusion
The judgment of the Court of Appeals for the Ninth Circuit was **reversed**. Stevens, J., delivered the opinion of the Court. Marshall, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], in which Brennan, J., joined.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Caceres* anchors an outer limit of the exclusionary rule: suppression is a remedy for constitutional (and some statutory) violations, not for an agency's failure to follow its own internal procedures. It belongs with the deterrence-and-cost line — *[[Stone v. Powell]]*, *[[United States v. Calandra]]*, *[[United States v. Janis]]*, and *[[United States v. Leon]]* — that ties suppression to whether excluding evidence will meaningfully deter the violation of constitutional rights.

## Appears on
- [[The Exclusionary Rule]] — *Anchor*

## Sources
- [*United States v. Caceres*, 440 U.S. 741 (1979)](https://www.courtlistener.com/opinion/110049/united-states-v-caceres/) — pinpoint: 755 (Stevens, J., for the Court; the CL opinion text carries the reporter star `*755` immediately before the quoted holding). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d2f1602f26cd7524", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Caceres"}, "payload": {"all": [{"cite": "440 U.S. 741", "page": "741", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "440"}, {"cite": "99 S. Ct. 1465", "page": "1465", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "99"}, {"cite": "59 L. Ed. 2d 733", "page": "733", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "59"}, {"cite": "1979 U.S. LEXIS 83", "page": "83", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1979"}], "display": "440 U.S. 741", "official": {"cite": "440 U.S. 741", "page": "741", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "440"}, "official_selection_present": true, "record_id": "United States v. Caceres"}}
{"assertion_id": "4cd94f7892c8c634", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Caceres"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Caceres", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Caceres

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Caceres",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Caceres",
    "case_name_short": "Caceres",
    "case_name_full": "United States v. Caceres",
    "input_case_name": "United States v. Caceres",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-04-13",
    "year": 1979,
    "docket": "No. 76-1309",
    "cluster_id": 110049,
    "lead_opinion_id": 9427514,
    "sibling_ids": [],
    "absolute_url": "/opinion/110049/united-states-v-caceres/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "440 U.S. 741",
      "volume": "440",
      "reporter": "U.S.",
      "page": "741",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 1465",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1465",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "59 L. Ed. 2d 733",
        "volume": "59",
        "reporter": "L. Ed. 2d",
        "page": "733",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 83",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "83",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "440 U.S. 741",
        "volume": "440",
        "reporter": "U.S.",
        "page": "741",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 1465",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1465",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "59 L. Ed. 2d 733",
        "volume": "59",
        "reporter": "L. Ed. 2d",
        "page": "733",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 83",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "83",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "440 U.S. 741",
    "official_selection": {
      "court_class": "scotus",
      "selected": "440 U.S. 741",
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
    "date_created": "2026-07-06T13:42:49Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:43:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:43:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:43:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:43:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-caceres--110049",
      "to_record_id": "United States v. Caceres",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Caceres

```
<opinion type="majority">
<author id="b813-5">Mr. Justice Stevens</author>
<p id="At5b">delivered the opinion of the Court.</p>
<p id="b813-6">The question we granted certiorari to decide is whether evidence obtained in violation of Internal Revenue Service (IRS) regulations may be admitted at the criminal trial of a taxpayer accused of bribing an IRS agent. <span class="citation multiple-matches"><a href="/c/U.%20S./436/943/">436 U. S. 943</a></span> (1978).</p>
<p id="b813-7">Unbeknown to respondent, three of his face-to-face conversations with IRS Agent Yee were monitored by means of a radio transmitter concealed on Yee’s person. Respondent moved to suppress tape recordings of the three conversations on the ground that the authorizations required by IRS regulations had not been secured. The District Court granted the motion. The Court of Appeals for the Ninth Circuit reversed as to the third tape; it concluded that adequate authorization had been obtained.<footnotemark>1</footnotemark> As to the first two tapes, however, the Court of Appeals agreed with the District Court both that the IRS regulations had not been followed and that exclusion of the recordings was therefore required. It is the latter conclusion that is at issue here.</p>
<p id="b813-8">The Government argues that exclusion of probative evidence in a criminal trial is an inappropriate sanction for violation of an executive department’s regulations. In this case, moreover, it argues that suppression is especially inappropriate because the violation of the regulation was neither deliberate nor prejudicial, and did not affect any constitu<page-number citation-index="1" label="744">*744</page-number>tional or statutory rights. We agree that suppression should not have been ordered in this case, and therefore reverse the judgment of the Court of Appeals.</p>
<p id="b814-5">I</p>
<p id="b814-6">Neither the Constitution nor any Act of Congress requires that official approval be secured before conversations are overheard or recorded by Government agents with the consent of one of the conversants.<footnotemark>2</footnotemark> Such “consensual electronic surveillance” between taxpayers and IRS agents is, however, prohibited by IRS regulations unless appropriate prior authorization is obtained.<footnotemark>3</footnotemark></p>
<p id="b814-7">The IRS Manual sets forth in detail the procedures to be followed in obtaining such approvals.<footnotemark>4</footnotemark> For all types of re<page-number citation-index="1" label="745">*745</page-number>quests the regulations require an explanation of the reasons for the proposal, the type of equipment to be used; the names of the persons involved, and the duration of the proposed monitoring.</p>
<p id="b815-5">Approval by as many as three different levels of authority may be required, depending on the kind of surveillance that is contemplated and the circumstances of the request. Telephone conversations may be monitored with the approval of an Assistant Regional Inspector of the Internal Security Division. Such advance approval may be requested and given verbally, although the authorization must subsequently be <page-number citation-index="1" label="746">*746</page-number>confirmed in writing. The monitoring of nontelephone conversations requires approval at the national as well as the regional level. In emergency situations, the Director, or Acting Director, Internal Security Division, or the Assistant Commissioner (Inspection) may authorize the recording. If there is at least 48 hours in which to obtain approval, a signed request must also be submitted to the Attorney General of the United States, or a designated Assistant Attorney General, by the Director or Acting Director of the Internal Security Division.</p>
<p id="b816-5">II</p>
<p id="b816-6">On March 14, 1974, Agent Yee met with respondent and his wife in connection with an audit of their 1971 income tax returns. After Mrs. Caceres left the meeting, respondent offered Yee a “personal settlement” of $500 in exchange for a favorable resolution of the audit. When he returned to the IRS office, Yee reported the offer to his superiors and prepared an affidavit describing it.<footnotemark>5</footnotemark></p>
<p id="b816-7">The record reflects no further discussion of the offer until January 1975. It does indicate, however, that one telephone conversation between Yee and respondent, on March 21, 1974, was recorded with authorization,<footnotemark>6</footnotemark> and that authority was also obtained to monitor face-to-face conversations with respondent from time to time during the period between March and September 1974.<footnotemark>7</footnotemark> Yee continued to work on the <page-number citation-index="1" label="747">*747</page-number>audit of respondent’s records throughout this period, but his meetings, until January 1975, were with Mrs. Caceres and the Cacereses’ accountant.<footnotemark>8</footnotemark></p>
<p id="b817-5">On January 27, 1975, Yee had a meeting with respondent that was not recorded. According to Yee’s affidavit,<footnotemark>9</footnotemark> the meeting proceeded in two stages. First, he discussed his calculations with respondent, Mrs. Caceres, and their accountant. When respondent and his wife asked for an additional week to check their records, Yee told them it would be necessary to sign an extension becau'se the statute of limitations would otherwise expire soon. Respondent stated that he would have to consult his attorney before signing any extension, and would call Yee with his decision later that day.</p>
<p id="b817-6">Yee then left the office to return to his car. He was followed by respondent, who revived the subject of a “personal settlement.” This time, respondent indicated that he had $500 that he would give Yee immediately, with an additional $500 to be paid when the matter was finally settled. Yee refused the offer, but at respondent’s insistence, eventually stated that he might consider it.</p>
<p id="b817-7">In subsequent conversations initiated by Agent Yee, all of which were monitored,<footnotemark>10</footnotemark> respondent indicated that he was not prepared for another meeting with Yee. .Finally, in a conversation on January 30 at 5:15 p. m., respondent agreed to a meeting the following day at 2 p. m. At 8:15 a. m. on the <page-number citation-index="1" label="748">*748</page-number>31st, the Regional Inspector in San Francisco telephoned the Director of Internal Security in Washington and obtained emergency approval for the use of electronic equipment to monitor the meeting that afternoon. On the same day, a written request for authority to monitor face-to-face conversations for a period of 30 days was initiated and, in due course, forwarded to Washington for submission to the Department of Justice.</p>
<p id="b818-5">At the meeting on the 31st, respondent gave Yee $500 and promised to give him an additional $500 when he received a notice from IRS showing his deficiency at an amount upon which he and Yee had agreed. As in all his future meetings with respondent, Yee wore a concealed radio transmitter which allowed other agents to monitor and record their conversation.</p>
<p id="b818-6">Yee next called respondent on February 5 and arranged a meeting for the next day to review the audit agreement. Because the Department of Justice had not yet acted on, or perhaps even received, the request for a 30-day authorization, the Regional Inspector again requested and obtained emergency approval to monitor the meeting with respondent. At the February 6 meeting, respondent renewed his promise to pay an additional $500 in connection with the 1971 return, and also offered Yee another $2,000 for help in settling his 1973 and 1974 returns.</p>
<p id="b818-7">On February 11, a Deputy Assistant Attorney General approved the request for authority to monitor Yee’s conversations with respondent for 30 days. The approval was received in time to cover a meeting held that day at which Yee was paid the additional $500. Because the 30-day period did not commence until February 11, however, no approval from the Department of Justice was ever obtained for the earlier monitorings of January 31 and February 6.</p>
<p id="b818-8">The District Court and the Court of Appeals both held that the two earlier meetings had not been monitored in accordance with IRS regulations, since Justice Department approval had <page-number citation-index="1" label="749">*749</page-number>not been secured. The courts recognized that such approval is not required, by the terms of the regulations, in “emergency situations” when less than 48 hours is available to secure authorization. They recognized, too, that in each instance, less than 48 hours did exist between the time the IRS initiated its request for monitoring approval and the time of the scheduled meeting with Yee. But the courts concluded that neither meeting fell within the emergency provision of the regulations because the exigencies were the product of “government-created scheduling problems.” <footnotemark>11</footnotemark></p>
<p id="b819-5">The Government does not challenge that conclusion. We are therefore presented with the question whether the tape recordings, and the testimony of the agents who monitored the January 31 and February 6 conversations, should be excluded because of the violation of the IRS regulations.</p>
<p id="b819-6">Ill</p>
<p id="b819-7">A court’s duty to enforce an agency regulation is most evident when compliance with the regulation is mandated by the Constitution or federal law. In <em>Bridges </em>v. <em>Wixon, </em><span class="citation" data-id="9419697"><a href="/opinion/104184/bridges-v-wixon/#152" aria-description="Citation for case: Bridges v. Wixon">326 U. S. 135, 152-153</a></span>, for example, this Court held invalid a deportation ordered on the basis of statements which did not comply with the Immigration Service’s rules requiring signatures and oaths, finding that the rules were designed “to afford [the alien] due process of law” by providing “safeguards against essentially unfair procedures.” <footnotemark>12</footnotemark></p>
<p id="b819-8">In this case, however, unlike <em>Bridges </em>v. <em><span class="citation" data-id="9419697"><a href="/opinion/104184/bridges-v-wixon/" aria-description="Citation for case: Bridges v. Wixon">Wixon</a></span>, </em>the agency was not required by the Constitution or by statute to adopt any particular procedures or rules before engaging in con<page-number citation-index="1" label="750">*750</page-number>sensual monitoring and recording. While Title III of the Omnibus Crime Control and Safe Streets Act of 1968, 18 IT. S. C. § 2510 <em>et seq., </em>regulates electronic surveillance conducted without the consent of either party to a conversation, federal statutes impose no restrictions on recording a conversation with the consent of one of the conversants.</p>
<p id="b820-5">Nor does the Constitution protect the privacy of individuals in respondent’s position. In <em>Lopez </em>v. <em>United States, </em><span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#439" aria-description="Citation for case: Lopez v. United States">373 U. S. 427, 439</a></span>, we held that the Fourth Amendment provided no protection to an individual against the recording of his statements by the IRS agent to whom he was speaking. In doing so, we repudiated any suggestion that the defendant had a “constitutional right to rely on possible flaws in the agent’s memory, or to challenge the agent’s credibility without being beset by corroborating evidence that is not susceptible of impeachment,” concluding instead that “the risk that petitioner took in offering a bribe to [the IRS agent] fairly included the risk that the offer would be accurately reproduced in court, whether by faultless memory or mechanical recording.” The same analysis was applied in <em>United States </em>v. <em>White, </em><span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/" aria-description="Citation for case: United States v. White">401 U. S. 745</a></span>, to consensual monitoring and recording by means of a transmitter concealed on an informant’s person, even though the defendant did not know that he was speaking with a Government agent:</p>
<blockquote id="b820-6">“Concededly a police agent who conceals his police connections may write down for official use his conversations with a defendant and testify concerning them, without a warrant authorizing his encounters with the defendant and without otherwise violating the latter’s Fourth Amendment rights. <em>Hoffa </em>v. <em>United States, </em>385 U. S., at 300-303. For constitutional purposes, no different result is required if the agent instead of immediately reporting and transcribing his conversations with defendant, either (1) simultaneously records them with electronic equipment which he is carrying on his person, <page-number citation-index="1" label="751">*751</page-number><em>Lopez </em>v. <em>United States, supra; </em>(2) or carries radio equipment which simultaneously transmits the conversations either to recording equipment located elsewhere or to other agents monitoring the transmitting frequency. <em>On Lee </em>v. <em>United States, </em>[<span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/" aria-description="Citation for case: On Lee v. United States">343 U. S. 747</a></span>]. If the conduct and revelations of an agent operating without electronic equipment do not invade the defendant’s constitutionally justifiable expectations of privacy, neither does a simultaneous recording of the same conversations made by the agent or by others from transmissions received from the agent to whom the defendant is talking and whose trustworthiness the defendant necessarily risks.” <em>United States </em>v. <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#751" aria-description="Citation for case: United States v. White"><em>White, supra, </em>at 751</a></span> (opinion of White, J.).<footnotemark>13</footnotemark></blockquote>
<p id="b821-5">Our decisions in <em><span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">Lopez</a></span> </em>and <em><span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/" aria-description="Citation for case: United States v. White">White</a></span> </em>demonstrate that the IRS was not required by the Constitution to adopt these regulations.<footnotemark>14</footnotemark> It is equally clear that the violations of agency regu<page-number citation-index="1" label="752">*752</page-number>lations disclosed by this record do not raise any constitutional questions.</p>
<p id="b822-5">It is true, of course, that respondent’s conversations were monitored without the approval of the Department of Justice, whereas the conversations of others in a similar position would, assuming the IRS generally follows its regulations, be recorded only with Justice Department approval. But this difference does not even arguably amount to a denial of equal protection. No claim is, or reasonably could be, made that if the IRS had more promptly addressed this request to the Department of Justice, it would have been denied. As a result, any inconsistency of which respondent might complain is purely one of form, with no discernible effect in this case on the action taken by the agency and its treatment of respondent.</p>
<p id="b822-6">Moreover, the failure to secure Justice Department authorization, while conceded here to be a violation of the IRS regulations, was attributable to the fact that the IRS officials responsible for administration of the relevant regulations, both in San Francisco and Washington, construed the situation as an emergency within the meaning of those regulations. Their construction of their own regulations, even if erroneous, was not obviously so. That kind of error by an executive agency in interpreting its own regulations surely does not raise any constitutional questions.</p>
<p id="b822-7">Nor is this a case in which the Due Process Clause is implicated because an individual has reasonably relied on agency <page-number citation-index="1" label="753">*753</page-number>regulations promulgated for his guidance or benefit and has suffered substantially because of their violation by the agency.<footnotemark>15</footnotemark> Respondent cannot reasonably contend that he relied on the regulation, or that its breach had any effect on his conduct. He did not know that his conversations with Yee were being recorded without proper authority.' He was, of course, prejudiced in the sense that he would be better off if all monitoring had been postponed until after the Deputy Assistant Attorney General’s approval was obtained on February 11, 1975, but precisely the same prejudice would have ensued if the approval had been issued more promptly. For the record makes it perfectly clear that a delay in processing the request, rather than any doubt about its propriety or sufficiency, was the sole reason why advance authorization was not obtained before February 11.</p>
<p id="b823-5">Finally, the Administrative Procedure Act<footnotemark>16</footnotemark> provides no grounds for judicial enforcement of the regulation violated in this case. The APA authorizes judicial review and invalidation of agency action that is arbitrary, capricious, an abuse of discretion, or not in accordance with law, as well as action <page-number citation-index="1" label="754">*754</page-number>taken “without observance of procedure required by law.” <footnotemark>17</footnotemark> Agency violations of their own regulations, whether or not also in violation of the Constitution, may well be inconsistent with the standards of agency action which the APA directs the courts .to enforce.<footnotemark>18</footnotemark> Indeed, some of our most important decisions holding agencies bound by their regulations have been in cases originally brought under the APA.<footnotemark>19</footnotemark></p>
<p id="b824-4">But this is not an APA case, and the remedy sought is not invalidation of the agency action. Rather, we are dealing with a criminal prosecution in which respondent seeks judicial enforcement of the agency regulations by means of the exclusionary rule. That rule has primarily rested on the judgment that the importance of deterring police conduct that may invade the constitutional rights of individuals throughout the community outweighs the importance of securing the conviction of the specific defendant on trial.<footnotemark>20</footnotemark> In view of our <page-number citation-index="1" label="755">*755</page-number>conclusion that none of respondent’s constitutional rights has been violated here, either by the actual recording or by the agency violation of its own regulations, our precedents enforcing the exclusionary rule to deter constitutional violations provide no support for the rule’s application in this case.<footnotemark>21</footnotemark></p>
<p id="b825-5">IY</p>
<p id="b825-6">Respondent argues that the regulations concerning electronic eavesdropping, even though not required by the Constitution or by statute, are of such importance in safeguarding the privacy of the citizenry that a rigid exclusionary rule should be applied to all evidence obtained in violation of any of their provisions. We do not doubt the importance of these rules. Nevertheless, without pausing to evaluate the Government’s challenge to our power to do so,<footnotemark>22</footnotemark> we decline to adopt any rigid rule requiring federal courts to exclude any evidence obtained as a result of a violation of these rules.</p>
<p id="b825-7">Regulations governing the conduct of criminal investigations are generally considered desirable, and may well provide more valuable protection to the public at large than the deterrence flowing from the occasional exclusion of items of evidence in criminal trials.<footnotemark>23</footnotemark> Although we do not suggest that a suppression order in this case would cause the IRS to abandon or modify its electronic surveillance regulations, we cannot ignore the possibility that a rigid application of an exclusionary rule to every regulatory violation could have a serious <page-number citation-index="1" label="756">*756</page-number>deterrent impact on the formulation of additional standards to govern prosecutorial and police procedures.<footnotemark>24</footnotemark> Here, the Executive itself has provided for internal sanctions in cases of knowing violations of the electronic-surveillance regulations<footnotemark>25</footnotemark> To go beyond that, and require exclusion in every case, would take away from the Executive Department the primary responsibility for fashioning the appropriate remedy for the violation of its regulations. But since the content, and indeed the existence, of the regulations would remain, within the Executive’s sole authority, the result might well be fewer and less protective regulations. In the long run, it is far better to have rules like those contained in the IRS Manual, and to tolerate occasional erroneous administration of the kind displayed by this record, than either to have no rules except those mandated by statute, or to have them framed in a mere precatory form.</p>
<p id="b826-5">Nor can we accept respondent’s further argument that even without a rigid rule of exclusion, his is a case in which evidence secured in violation of the agency regulation should be excluded on the basis of a more limited, individualized approach. Quite the contrary, this case exemplifies those situations in which evidence would <em>not </em>be excluded if a case-by-case approach were applied. The two conversations at issue here were recorded with the approval of the IRS officials in San Francisco and Washington. In an emergency situa<page-number citation-index="1" label="757">*757</page-number>tion, which the agents thought was present, this approval would have been sufficient. The agency action, while later found to be in violation of the regulations, nonetheless reflected a reasonable, good-faith attempt to comply in a situation in which no one questions that monitoring was appropriate and would have certainly received Justice Department authorization, had the request been received more promptly. In these circumstances, there is simply no reason why a court should exercise whatever discretion it may have to exclude evidence obtained in violation of the regulations.</p>
<p id="b827-5">The judgment of the Court of Appeals is</p>
<p id="b827-6">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b813-9"> <span class="citation" data-id="340826"><a href="/opinion/340826/united-states-v-alfredo-l-caceres/" aria-description="Citation for case: United States v. Alfredo L. Caceres">545 F. 2d 1182</a></span> (1976). The District Court suppressed evidence relating to the third conversation as well on the ground that the approval of a <em>Deputy </em>Assistant Attorney General was not sufficient to comply with the regulations. The Court of Appeals disagreed, concluding that the Attorney General’s authority to approve such monitoring could be delegated not only to Assistant Attorneys General, as provided specifically in the regulation, but also to their deputies. That conclusion is not at issue here.</p>
</footnote>
<footnote label="2">
<p id="b814-8"> See <em>United States </em>v. <em>White, </em><span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#752" aria-description="Citation for case: United States v. White">401 U. S. 745, 752</a></span> (plurality opinion); <em>Lopez </em>v. <em>United States, </em><span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">373 U. S. 427</a></span>; <span class="citation no-link">18 U. S. C. §2511</span> (2) (c); <em>infra, </em>at 749-751.</p>
</footnote>
<footnote label="3">
<p id="b814-9"> The IRS regulations were drafted to conform to the requirements of the Attorney General’s October 16, 1972, Memorandum to the Heads of Executive Departments and Agencies. The memorandum mandates Justice Department approval for all consensual monitoring of nontelephone conversations by federal departments and agencies. The only exceptions are if less than 48 hours is available to secure approval or if exigent circumstances preclude requests for advance authorization from the Justice Department; in such cases, monitoring may be instituted under the authorization of the head of the department or agency, or other officials designated by him.</p>
</footnote>
<footnote label="4">
<p id="b814-10"> Paragraph 652.22 of the IRS Manual (in effect Sept. 1975) provides in pertinent part:</p>
<p id="b814-11">“(1) The monitoring of non-telephone conversations with the consent of one party requires the advance authorization of the Attorney General or any designated Assistant Attorney General. Requests for such authority may be signed by the Director, Internal Security Division, or, in his/her absence, the Acting Director. This authority cannot be redelegated. These same officials may authorize temporary emergency monitoring when exigent circumstances preclude requesting the authorization of the Attorney General in advance. If the Director, Internal Security Division, <page-number citation-index="1" label="745">*745</page-number>cannot be reached, the Assistant Commissioner (Inspection) may grant emergency approval. This authority cannot be redelegated.</p>
<p id="A2g">“(2) Written approval of the Attorney General must be requested 48 hours prior to the use of mechanical, electronic or other devices to overhear, transmit or record a non-telephone private conversation with the permission of one party to the conversation. . . . Any requests being telefaxed into the National Office should be submitted four days prior to the anticipated equipment use. . . .</p>
<p id="ANx">“(3) [A request] must be signed and submitted by the Regional Inspector or Chief, Investigations Branch, to the Director, Internal Security Division. Such requests will contain [reason for such proposed use; type of equipment to be used; names of persons involved; proposed location of equipment; duration of proposed use (limited to 30 days from proposed beginning date); and manner or method of installation] ....</p>
<p id="AA_j">“(6) When emergency situations occur, the Director or Acting Director, Internal Security Division, or the Assistant Commissioner (Inspection) will be contacted to grant emergency approval to monitor. This emergency approval authority cannot be redelegated. . . . Emergency authorization pursuant to this exception will not be given where the requesting official has in excess of 48 hours to obtain written advance approval from the Attorney General.</p>
<p id="AJo">“(7) If, at the time the emergency approval request is submitted, it is desired that approval for use of electronic equipment be given for an extended period, this should be indicated on the [appropriate form]. The Director, in addition to reporting his authorization for emergency use to the Attorney General, will also request approval for the Use of Electronic Equipment for the duration of that period specified by the requestor.”</p>
</footnote>
<footnote label="5">
<p id="b816-8"> App. 20, 23-24, 46.</p>
</footnote>
<footnote label="6">
<p id="b816-9"> <em>Id,., </em>at 25-27, 46.</p>
</footnote>
<footnote label="7">
<p id="b816-10"> Requests for authorization to use electronic equipment to monitor nontelephone conversations are made on a form (No. 5177) that requires disclosure of the dates of previous authorizations. The form dated January 31, 1975, App. 63, is termed an extension, and reports prior authorizations dated March 25, April 24, May 24, June 27, July 23, and August 29, 1974. Under the regulations, a single authorization may cover a period of up to 30 days; the intervals between the dates of prior authorizations in this case are consistent with successive 30-day authorizations, although this has not been established by any evidence called to our attention.</p>
</footnote>
<footnote label="8">
<p id="b817-8"> Yee had one follow-up conversation with respondent later in March, which was not monitored. From that point until January 1975, he had no further contact with respondent. App. to Pet. for Cert. 16a (opinion and order of the District Court); App. 21-22,</p>
</footnote>
<footnote label="9">
<p id="b817-9"><span class="citation no-link"><em> Id., </em>at 65-67</span>.</p>
</footnote>
<footnote label="10">
<p id="b817-10"> In the District Court, respondent moved to suppress evidence relating to these telephone conversations on the grounds that the monitoring had not been properly authorized. The District Court rejected that challenge, concluding that the applicable IRS regulations had been followed with respect to these conversations. App. to Pet. for Cert. 16a-17a. That ruling is not at issue here.</p>
</footnote>
<footnote label="11">
<p id="b819-9"> 545 E. 2d, at 1187. See also App. to Pet. for Cert. 20a (opinion of District Court) (“the only 'emergency’ was created wholly by the I. R. S.”).</p>
</footnote>
<footnote label="12">
<p id="b819-10"> See also <em>United States ex rel. Bilokumsky </em>v. <em>Tod, </em><span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#155" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">263 U. S. 149, 155</a></span> (Court assumed that “one under investigation with a view to deportation is legally entitled to insist upon the observance of rules promulgated by the Secretary pursuant to law”).</p>
</footnote>
<footnote label="13">
<p id="b821-6"> Mr. Justice White further stated:</p>
<p id="b821-7">“Nor should we be too ready to erect constitutional barriers to relevant and probative evidence which is also accurate and reliable. An electronic recording will many times produce a more reliable rendition of what a defendant has said than will the unaided memory of a police agent. It may also be that with the recording in existence it is less likely that the informant will change his mind, less chance that threat or injury will suppress unfavorable evidence and less chance that cross-examination will confound the testimony. Considerations like these obviously do not favor the defendant, but we are not prepared to hold that a defendant who has no constitutional right to exclude the informer’s unaided testimony nevertheless has a Fourth Amendment privilege against a more accurate version of the events in question.” <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#753" aria-description="Citation for case: United States v. White">401 U. S., at 753</a></span>.</p>
</footnote>
<footnote label="14">
<p id="b821-8"> It does not necessarily follow, however, as a matter of either logic or law, that the agency had no duty to obey them. “Where the rights of individuals are affected, it is incumbent upon agencies to follow their own procedures. This is so even where the internal procedures are possibly more rigorous than otherwise would be required.” <em>Morton </em>v. <em>Ruiz, </em><span class="citation" data-id="108969"><a href="/opinion/108969/morton-v-ruiz/#235" aria-description="Citation for case: Morton v. Ruiz">415 U. S. 199, 235</a></span>. See, <em>e. g., United States ex rel. Accardi </em>v. <em>Shaughnessy, </em><span class="citation" data-id="9421054"><a href="/opinion/105205/united-states-ex-rel-accardi-v-shaughnessy/" aria-description="Citation for case: United States Ex Rel. Accardi v. Shaughnessy">347 U. S. 260</a></span> (holding habeas corpus relief proper where Government regulations “with the force and effect of law” governing the procedure to be foEowed in processing and passing upon an alien’s application for suspen<page-number citation-index="1" label="752">*752</page-number>sion of deportation were not followed); <em>Service </em>v. <em>Dulles, </em><span class="citation" data-id="105539"><a href="/opinion/105539/service-v-dulles/" aria-description="Citation for case: Service v. Dulles">354 U. S. 363</a></span> (invalidating Secretary of State’s dismissal of an employee where regulations requiring approval of the Deputy Undersecretary and consultation of full record were not satisfied); <em>Vitarelli </em>v. <em>Seaton, </em><span class="citation" data-id="9421811"><a href="/opinion/105892/vitarelli-v-seaton/" aria-description="Citation for case: Vitarelli v. Seaton">359 U. S. 535</a></span> (invalidating dismissal of Interior Department employee where regulations governing hearing procedures for national security dismissals were not followed). See also <em>Yellin </em>v. <em>United States, </em><span class="citation" data-id="9422642"><a href="/opinion/106654/yellin-v-united-states/" aria-description="Citation for case: Yellin v. United States">374 U. S. 109</a></span> (reversing contempt conviction where congressional committee had not complied with its rules requiring it to consider a witness’ request to be heard in executive session).</p>
</footnote>
<footnote label="15">
<p id="b823-6"> In <em>Raley </em>v. <em>Ohio, </em><span class="citation" data-id="105925"><a href="/opinion/105925/raley-v-ohio/#437" aria-description="Citation for case: Raley v. Ohio">360 U. S. 423, 437-438</a></span>, we held that due process precluded the conviction of individuals for refusing to answer questions asked by a state investigating commission which itself had erroneously provided assurances, express or implied, that the defendants had a privilege under state law to refuse to answer. And in <em>Cox </em>v. <em>Louisiana, </em><span class="citation" data-id="9422938"><a href="/opinion/106968/cox-v-louisiana/" aria-description="Citation for case: Cox v. Louisiana">379 U. S. 559</a></span>, the Court held that an individual could not be punished for demonstrating “near” a courthouse where the highest police officials of the city had advised the demonstrators that they could meet where they did without violating the statutory proscription against demonstrations “near” the courthouse. Cf. <em>Arizona Grocery Co. </em>v. <em>Atchison, T. &amp; S. F. R. Co., </em><span class="citation" data-id="101832"><a href="/opinion/101832/arizona-grocery-co-v-atchison-topeka-santa-fe-railway-co/" aria-description="Citation for case: Arizona Grocery Co. v. Atchison, Topeka &amp; Santa Fe...">284 U. S. 370</a></span> (holding invalid Interstate Commerce Commission's retroactive application of new rate); <em>Columbia Broadcasting System, Inc. </em>v. <em>United States, </em><span class="citation" data-id="9419254"><a href="/opinion/103691/columbia-broadcasting-system-inc-v-united-states/#422" aria-description="Citation for case: Columbia Broadcasting System, Inc. v. United States">316 U. S. 407, 422</a></span> (agency regulations on which individuals are “-entitled to rely” bind agency and are therefore ripe for judicial review). The underlying rationale of the foregoing cases is plainly inapplicable here.</p>
</footnote>
<footnote label="16">
<p id="b823-7"> The Act was originally passed in 1946, <span class="citation no-link">60 Stat. 237</span>, and is codified at <span class="citation no-link">5 U. S. C. § 551</span> <em>et seq. </em>and § 701 <em>et seq.</em></p>
</footnote>
<footnote label="17">
<p id="b824-5"> <span class="citation no-link">5 U. S. C. § 706</span>.</p>
</footnote>
<footnote label="18">
<p id="b824-6"> Cf. <em>Board of Curators, Univ. of Mo. </em>v. <em>Horowitz, </em><span class="citation" data-id="9427086"><a href="/opinion/109809/board-of-curators-of-the-university-of-missouri-v-horowitz/" aria-description="Citation for case: Board of Curators of the University of Missouri v. Horowitz">435 U. S. 78</a></span>, 92 n. 8; <em>Vitarelli </em>v. <span class="citation" data-id="9421811"><a href="/opinion/105892/vitarelli-v-seaton/#547" aria-description="Citation for case: Vitarelli v. Seaton"><em>Seaton, supra, </em>at 547</a></span> (Frankfurter, J., concurring in part and dissenting in part) (“This judicially evolved rule of administrative law is now firmly established and, if I may add, rightly so. He that takes the procedural sword shall perish with that sword”).</p>
<p id="b824-7">Even as a matter of administrative law, however, it seems clear that agencies are not required, at the risk of invalidation of their action, to follow all of their rules, even those properly classified as “internal.” In <em>American Farm Lines </em>v. <em>Black Ball Freight Service, </em><span class="citation" data-id="9424239"><a href="/opinion/108117/american-farm-lines-v-black-ball-freight-service/#538" aria-description="Citation for case: American Farm Lines v. Black Ball Freight Service">397 U. S. 532, 538</a></span>, for example, ICC rules requiring certain information to be included in applications had not been followed. This Court rejected the argument that the agency action was therefore invalid, concluding that the Commission was “entitled to a measure of discretion in administering its own procedural rules in such a manner as it deems necessary to resolve quickly and correctly urgent transportation problems.”</p>
</footnote>
<footnote label="19">
<p id="b824-8"> See App. in <em>Service </em>v. <em><span class="citation" data-id="105539"><a href="/opinion/105539/service-v-dulles/" aria-description="Citation for case: Service v. Dulles">Dulles</a></span>, </em>O. T. 1956, No. 407, p. 40; App. in <em>Vitarelli </em>v. <em><span class="citation" data-id="9421811"><a href="/opinion/105892/vitarelli-v-seaton/" aria-description="Citation for case: Vitarelli v. Seaton">Seaton</a></span>, </em>O. T. 1958, No. 101, p. 7. The complaints in both of these cases invoked <span class="citation no-link">5 U. S. C. § 1009</span> (1964 ed.), the then-applicable APA judicial-review provision.</p>
</footnote>
<footnote label="20">
<p id="b824-9"> See <em>Linkletter </em>v. <em>Walker, </em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#633" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 633, 636-637</a></span>; <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#656" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 656</a></span>; <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 217</a></span>.</p>
</footnote>
<footnote label="21">
<p id="b825-8"> Since no statute was violated by the recording of respondent’s conversations, this Court’s decision in <em>Miller </em>v. <em>United States, </em><span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">357 U. S. 301</a></span>, is likewise inapplicable.</p>
</footnote>
<footnote label="22">
<p id="b825-9"> The Government argues that Fed. Rule Evid. 402 and <span class="citation no-link">18 U. S. C. § 3501</span> prohibited the Court of Appeals from exercising whatever supervisory power it might otherwise have to suppress evidence of respondent’s statements to Yee. Brief for United States 42.</p>
</footnote>
<footnote label="23">
<p id="b825-10"> See Amsterdam, Perspectives on the Fourth Amendment, <span class="citation no-link">58 Minn. L. Rev. 349</span>, 416-428 (1974); McGowan, Rule-Making and the Police, <span class="citation no-link">70 Mich. L. Rev. 659</span> (1972).</p>
</footnote>
<footnote label="24">
<p id="b826-6"> See F. Cooper, Administrative Agencies and the Courts 289-290 (1951) (“[T]oo rigid an application of the doctrine prohibiting disregard of procedural rules would encourage the tendency of some agencies to proceed almost without rules. The doctrine should not be pressed so far as to induce agencies to adopt the protective device of promulgating procedural rules so vague in nature as to make it impossible to show a violation of the rules”).</p>
</footnote>
<footnote label="25">
<p id="b826-7"> See IRS Manual ¶ 652.1 (3) (in effect Sept. 1975) (“Any employee who knowingly violates or in any way knowingly countenances violation of this policy will be subject to disciplinary action and may be removed from the Service”).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Calandra.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "United States v. Calandra"
type: case
citation: "414 U.S. 338 (1974)"
parallel_cite: "94 S. Ct. 613; 38 L. Ed. 2d 561; 66 Ohio Op. 2d 320"
neutral_cite: 1974 U.S. LEXIS 145
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1974
date_decided: 1974-01-08
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1974-01-08
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Calandra
  varies_by_point: false
  scope_note: "Good law; foundational statement of the exclusionary rule as a deterrent remedy, central to later good-faith and cost-benefit cases."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108898/united-states-v-calandra/"
  cluster_id: 108898
  opinion_id: 108898
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[Mapp v. Ohio]]", "[[Herring v. United States]]", "[[Hudson v. Michigan]]", "[[Immigration & Naturalization Service v. Lopez-Mendoza]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule"]
holding: "The exclusionary rule is a judicially created deterrent remedy, not a personal constitutional right; it does not apply to grand-jury…"
lake:
  record_id: United States v. Calandra
  status: verified
  projected_at: 2026-07-06
---

# United States v. Calandra

*414 U.S. 338 (1974)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
During a search under a warrant for evidence of a bookmaking operation, agents also found and seized a card suggesting Calandra was involved in loansharking. A grand jury investigating loansharking summoned him and asked questions based on that seized evidence. Calandra refused to answer, arguing the questions were derived from an unlawful search; the lower courts agreed the search exceeded the warrant and suppressed.

## Issue
Whether a grand jury witness may refuse to answer questions on the ground that the questions are based on evidence obtained through an unlawful search and seizure — i.e., whether the exclusionary rule applies in grand jury proceedings.

## Rule
The exclusionary rule is a judicial deterrent, not a personal right of the aggrieved party: "the rule is a judicially created remedy designed to safeguard Fourth Amendment rights generally through its deterrent effect, rather than a personal constitutional right of the party aggrieved." — 414 U.S. at 348. ^pin-348

Because applying the rule to grand jury questioning would achieve little additional deterrence while unduly impeding the grand jury's investigative role, the Court declined to extend it there; a grand jury witness may not refuse to answer questions merely because they are based on illegally obtained evidence.

## Application
The Fourth Amendment wrong against Calandra — the unlawful seizure — was already complete; grand jury questions drawing on that evidence inflicted no fresh invasion of his person, house, papers, or effects. Suppressing such questions would extend the exclusionary rule's costs to the grand jury for only speculative incremental deterrence. The Court therefore held Calandra could not refuse to answer, and reversed the order suppressing the grand jury questions.

## Conclusion
The exclusionary rule does not apply to grand jury proceedings, and Calandra had to answer; the suppression order was reversed. Exclusion is a deterrence-driven judicial remedy whose reach is set by weighing its costs against its deterrent benefits, not a personal constitutional entitlement.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Calandra*'s deterrence rationale qualifies the suppression remedy of [[Mapp v. Ohio]] and anchors the cost-benefit analysis later used to narrow exclusion in [[Hudson v. Michigan]], [[Herring v. United States]], and [[Immigration & Naturalization Service v. Lopez-Mendoza]].

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Calandra*, 414 U.S. 338 (1974) — https://www.courtlistener.com/opinion/108898/united-states-v-calandra/ — pinpoint: 348.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5940ba1956ef42b4", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Calandra"}, "payload": {"all": [{"cite": "414 U.S. 338", "page": "338", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "414"}, {"cite": "94 S. Ct. 613", "page": "613", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "94"}, {"cite": "38 L. Ed. 2d 561", "page": "561", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "38"}, {"cite": "1974 U.S. LEXIS 145", "page": "145", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1974"}, {"cite": "66 Ohio Op. 2d 320", "page": "320", "reporter": "Ohio Op. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "66"}], "display": "414 U.S. 338", "official": {"cite": "414 U.S. 338", "page": "338", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "414"}, "official_selection_present": true, "record_id": "United States v. Calandra"}}
{"assertion_id": "fd5824993ecbea09", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-348", "record_id": "United States v. Calandra"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-348", "pinpoint_status": "slip-only", "quote": "--- # United States v. Calandra *414 U.S. 338 (1974)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background During a search under a warrant for evidence of a bookmaking operation, agents also found and seized a card suggesting Calandra was involved in loansharking. A grand jury investigating loansharking summoned him and asked questions based on that seized evidence. Calandra refused to answer, arguing the questions were derived from an unlawful search; the lower courts agreed the search exceeded the warrant and suppressed. ## Issue Whether a grand jury witness may refuse to answer questions on the ground that the questions are based on evidence obtained through an unlawful search and seizure — i.e., whether the exclusionary rule applies in grand jury proceedings. ## Rule The exclusionary rule is a judicial deterrent, not a personal right of the aggrieved party:", "quote_fidelity": "mismatch", "record_id": "United States v. Calandra", "star_marker": null}}
{"assertion_id": "624955926e1f5a4c", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Calandra"}, "payload": {"as_of_content": "1974-01-08", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Calandra", "scope_note": "Good law; foundational statement of the exclusionary rule as a deterrent remedy, central to later good-faith and cost-benefit cases.", "varies_by_point": false}}
```

### lake record — United States v. Calandra

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Calandra",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Calandra",
    "case_name_short": "Calandra",
    "case_name_full": "United States v. Calandra",
    "input_case_name": "United States v. Calandra",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1974-01-08",
    "year": 1974,
    "docket": null,
    "cluster_id": 108898,
    "lead_opinion_id": 108898,
    "sibling_ids": [
      108898,
      9425486,
      9425487
    ],
    "absolute_url": "/opinion/108898/united-states-v-calandra/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "414 U.S. 338",
      "volume": "414",
      "reporter": "U.S.",
      "page": "338",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "94 S. Ct. 613",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "613",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "38 L. Ed. 2d 561",
        "volume": "38",
        "reporter": "L. Ed. 2d",
        "page": "561",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "66 Ohio Op. 2d 320",
        "volume": "66",
        "reporter": "Ohio Op. 2d",
        "page": "320",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1974 U.S. LEXIS 145",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "145",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "414 U.S. 338",
        "volume": "414",
        "reporter": "U.S.",
        "page": "338",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 S. Ct. 613",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "613",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "38 L. Ed. 2d 561",
        "volume": "38",
        "reporter": "L. Ed. 2d",
        "page": "561",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1974 U.S. LEXIS 145",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "145",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "66 Ohio Op. 2d 320",
        "volume": "66",
        "reporter": "Ohio Op. 2d",
        "page": "320",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "414 U.S. 338",
    "official_selection": {
      "court_class": "scotus",
      "selected": "414 U.S. 338",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-348",
      "page": null,
      "quote": "--- # United States v. Calandra *414 U.S. 338 (1974)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background During a search under a warrant for evidence of a bookmaking operation, agents also found and seized a card suggesting Calandra was involved in loansharking. A grand jury investigating loansharking summoned him and asked questions based on that seized evidence. Calandra refused to answer, arguing the questions were derived from an unlawful search; the lower courts agreed the search exceeded the warrant and suppressed. ## Issue Whether a grand jury witness may refuse to answer questions on the ground that the questions are based on evidence obtained through an unlawful search and seizure \u2014 i.e., whether the exclusionary rule applies in grand jury proceedings. ## Rule The exclusionary rule is a judicial deterrent, not a personal right of the aggrieved party:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1974-01-08",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Calandra",
    "varies_by_point": false,
    "scope_note": "Good law; foundational statement of the exclusionary rule as a deterrent remedy, central to later good-faith and cost-benefit cases.",
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
        "journal_ref": "United States v. Calandra:lane1_negative"
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
        "journal_ref": "United States v. Calandra:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States of America v. Joseph A. Foistner",
          "cluster_id": 10698819,
          "cite": [
            "2021 DNH 050"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Christian",
          "cluster_id": 4643309,
          "cite": [
            "445 P.3d 183"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Thalken",
          "cluster_id": 4497142,
          "cite": [
            "299 Neb. 857",
            "911 N.W.2d 562"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gomez",
          "cluster_id": 8443636,
          "cite": [
            "877 F.3d 76"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Allen",
          "cluster_id": 4409967,
          "cite": [
            "864 F.3d 63",
            "2017 U.S. App. LEXIS 12942",
            "2017 WL 3040201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Long",
          "cluster_id": 4371038,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Todd Eugene Trahan",
          "cluster_id": 4311782,
          "cite": [
            "886 N.W.2d 216",
            "2016 Minn. LEXIS 660"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Illinois v. Gates",
          "cluster_id": 110959,
          "cite": [
            "76 L. Ed. 2d 527",
            "103 S. Ct. 2317",
            "462 U.S. 213",
            "1983 U.S. LEXIS 54",
            "51 U.S.L.W. 4709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane2_top_cited"
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
        "journal_ref": "United States v. Calandra:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Franks v. Delaware",
          "cluster_id": 109925,
          "cite": [
            "57 L. Ed. 2d 667",
            "98 S. Ct. 2674",
            "438 U.S. 154",
            "1978 U.S. LEXIS 127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albright v. Oliver",
          "cluster_id": 112924,
          "cite": [
            "127 L. Ed. 2d 114",
            "114 S. Ct. 807",
            "510 U.S. 266",
            "1994 U.S. LEXIS 1319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane2_top_cited"
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
        "journal_ref": "United States v. Calandra:lane2_top_cited"
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
        "journal_ref": "United States v. Calandra:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gerstein v. Pugh",
          "cluster_id": 109186,
          "cite": [
            "43 L. Ed. 2d 54",
            "95 S. Ct. 854",
            "420 U.S. 103",
            "1975 U.S. LEXIS 29",
            "19 Fed. R. Serv. 2d 1499"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stone v. Powell",
          "cluster_id": 109540,
          "cite": [
            "49 L. Ed. 2d 1067",
            "96 S. Ct. 3037",
            "428 U.S. 465",
            "1976 U.S. LEXIS 86"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane2_top_cited"
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
        "journal_ref": "United States v. Calandra:lane2_top_cited"
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
        "journal_ref": "United States v. Calandra:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nix v. Williams",
          "cluster_id": 111204,
          "cite": [
            "81 L. Ed. 2d 377",
            "104 S. Ct. 2501",
            "467 U.S. 431",
            "1984 U.S. LEXIS 101",
            "52 U.S.L.W. 4732"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brewer v. Williams",
          "cluster_id": 109624,
          "cite": [
            "51 L. Ed. 2d 424",
            "97 S. Ct. 1232",
            "430 U.S. 387",
            "1977 U.S. LEXIS 64"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane2_top_cited"
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
        "journal_ref": "United States v. Calandra:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fisher v. United States",
          "cluster_id": 109432,
          "cite": [
            "48 L. Ed. 2d 39",
            "96 S. Ct. 1569",
            "425 U.S. 391",
            "1976 U.S. LEXIS 98",
            "37 A.F.T.R.2d (RIA) 1244"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richmond Newspapers, Inc. v. Virginia",
          "cluster_id": 110339,
          "cite": [
            "65 L. Ed. 2d 973",
            "100 S. Ct. 2814",
            "448 U.S. 555",
            "1980 U.S. LEXIS 18",
            "6 Media L. Rep. (BNA) 1833"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Salvucci",
          "cluster_id": 110325,
          "cite": [
            "65 L. Ed. 2d 619",
            "100 S. Ct. 2547",
            "448 U.S. 83",
            "1980 U.S. LEXIS 141"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane2_top_cited"
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
        "journal_ref": "United States v. Calandra:lane2_top_cited"
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
        "journal_ref": "United States v. Calandra:lane2_top_cited"
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
        "journal_ref": "United States v. Calandra:lane2_top_cited"
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
        "journal_ref": "United States v. Calandra:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Janis",
          "cluster_id": 109539,
          "cite": [
            "49 L. Ed. 2d 1046",
            "96 S. Ct. 3021",
            "428 U.S. 433",
            "1976 U.S. LEXIS 162"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Tucker",
          "cluster_id": 109063,
          "cite": [
            "41 L. Ed. 2d 182",
            "94 S. Ct. 2357",
            "417 U.S. 433",
            "1974 U.S. LEXIS 71"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Hass",
          "cluster_id": 109221,
          "cite": [
            "43 L. Ed. 2d 570",
            "95 S. Ct. 1215",
            "420 U.S. 714",
            "1975 U.S. LEXIS 5"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Calandra:lane2_top_cited"
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
        "journal_ref": "United States v. Calandra:lane2_top_cited"
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
        "journal_ref": "United States v. Calandra:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108898 OR 9425486 OR 9425487) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDY4OTcyODAwMDAwJnM9ODQ0MjgyNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108898+OR+9425486+OR+9425487%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(108898 OR 9425486 OR 9425487)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03ODUmcz0xMTAzMTcmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28108898+OR+9425486+OR+9425487%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108898 OR 9425486 OR 9425487)",
        "reviewed": 53,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 53,
        "triage_read": 2,
        "triage_snippet_classified": 51
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108898 OR 9425486 OR 9425487)",
    "indexed_citing_opinions": 2242,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108898,
        "count": 2009,
        "count_source": "search"
      },
      {
        "opinion_id": 9425486,
        "count": 284,
        "count_source": "search"
      },
      {
        "opinion_id": 9425487,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3415,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-calandra.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwNDQ4MDgmcz0xMDE2MTkzMCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28108898+OR+9425486+OR+9425487%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108898,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 97290,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 99422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 101836,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 103311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 104788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 105021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 105355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 105609,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 105848,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 106441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 107874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 108340,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 108596,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 108611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 108650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 108760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 291186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 300619,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 305315,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108898,
        "cited_id": 1624691,
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
    "date_created": "2026-07-05T22:52:32Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:52:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:52:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:55:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:52:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Calandra

```
<div>
<center><b><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">414 U.S. 338</a></span> (1974)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
CALANDRA.</h1></center>
<center>No. 72-734.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 11, 1973.</center>
<center>Decided January 8, 1974.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SIXTH CIRCUIT.
<p><span class="star-pagination">*339</span> <i>Louis F. Claiborne</i> argued the cause for the United States. With him on the briefs were <i>Solicitor General Bork,</i> former <i>Solicitor General Griswold, Assistant Attorney General Petersen, Deputy Solicitor General Lacovara, Keith A. Jones, Jerome M. Feit,</i> and <i>Shirley Baccus-Lobel.</i></p>
<p><i>Robert J. Rotatori</i> argued the cause for respondent. With him on the brief were <i>Gerald S. Gold</i> and <i>Niki Z. Schwartz.</i><sup>[*]</sup></p>
<p>MR. JUSTICE POWELL delivered the opinion of the Court.</p>
<p>This case presents the question whether a witness summoned to appear and testify before a grand jury may refuse to answer questions on the ground that they are based on evidence obtained from an unlawful search and seizure. The issue is of considerable importance to the administration of criminal justice.</p>
<p></p>
<h2>
<span class="star-pagination">*340</span> I</h2>
<p>On December 11, 1970, federal agents obtained a warrant authorizing a search of respondent John Calandra's place of business, the Royal Machine &amp; Tool Co. in Cleveland, Ohio. The warrant was issued in connection with an extensive investigation of suspected illegal gambling operations. It specified that the object of the search was the discovery and seizure of bookmaking records and wagering paraphernalia. A master affidavit submitted in support of the application for the warrant contained information derived from statements by confidential informants to the Federal Bureau of Investigation (FBI), from physical surveillance conducted by FBI agents, and from court-authorized electronic surveillance.<sup>[1]</sup></p>
<p>The Royal Machine &amp; Tool Co. occupies a two-story building. The first floor consists of about 13,000 square feet, and houses industrial machinery and inventory. The second floor contains a general office area of about 1,500 square feet and a small office occupied by Calandra, president of the company, and his secretary. On December 15, 1970, federal agents executed the warrant directed at Calandra's place of business and conducted a thorough, four-hour search of the premises. The record reveals that the agents spent more than three hours searching Calandra's office and files.</p>
<p>Although the agents found no gambling paraphernalia, one discovered, among certain promissory notes, a card indicating that Dr. Walter Loveland had been making periodic payments to Calandra. The agent stated in an affidavit that he was aware that the United States Attorney's <span class="star-pagination">*341</span> office for the Northern District of Ohio was investigating possible violations of <span class="citation no-link">18 U. S. C. §§ 892</span>, 893, and 894, dealing with extortionate credit transactions, and that Dr. Loveland had been the victim of a "loansharking" enterprise then under investigation. The agent concluded that the card bearing Dr. Loveland's name was a loansharking record and therefore had it seized along with various other items, including books and records of the company, stock certificates, and address books.</p>
<p>On March 1, 1971, a special grand jury was convened in the Northern District of Ohio to investigate possible loansharking activities in violation of federal laws. The grand jury subpoenaed Calandra in order to ask him questions based on the evidence seized during the search of his place of business on December 15, 1970. Calandra appeared before the grand jury on August 17, 1971, but refused to testify, invoking his Fifth Amendment privilege against self-incrimination. The Government then requested the District Court to grant Calandra transactional immunity pursuant to <span class="citation no-link">18 U. S. C. § 2514</span>. Calandra requested and received a postponement of the hearing on the Government's application for the immunity order so that he could prepare a motion to suppress the evidence seized in the search.</p>
<p>Calandra later moved pursuant to Fed. Rule Crim. Proc. 41 (e) for suppression and return of the seized evidence on the grounds that the affidavit supporting the warrant was insufficient and that the search exceeded the scope of the warrant. On August 27, the District Court held a hearing at which Calandra stipulated that he would refuse to answer questions based on the seized materials. On October 1, the District Court entered its judgment ordering the evidence suppressed and returned to Calandra and further ordering that Calandra need not answer any of the grand jury's questions based on the <span class="star-pagination">*342</span> suppressed evidence. <span class="citation" data-id="1624691"><a href="/opinion/1624691/in-re-immunity-of-calandra/" aria-description="Citation for case: In Re Immunity of Calandra">332 F. Supp. 737</a></span> (1971). The court held that "due process . . . allows a witness to litigate the question of whether the evidence which constitutes the basis for the questions asked of him before the grand jury has been obtained in a way which violates the constitutional protection against unlawful search and seizure." <span class="citation" data-id="1624691"><a href="/opinion/1624691/in-re-immunity-of-calandra/#742" aria-description="Citation for case: In Re Immunity of Calandra"><i>Id.,</i> at 742</a></span>. The court found that the search warrant had been issued without probable cause and that the search had exceeded the scope of the warrant.</p>
<p>The Court of Appeals for the Sixth Circuit affirmed, holding that the District Court had properly entertained the suppression motion and that the exclusionary rule may be invoked by a witness before the grand jury to bar questioning based on evidence obtained in an unlawful search and seizure.<sup>[2]</sup> <span class="citation" data-id="305315"><a href="/opinion/305315/united-states-v-john-p-calandra/" aria-description="Citation for case: United States v. John P. Calandra">465 F. 2d 1218</a></span> (1972). The offer to grant Calandra immunity was deemed irrelevant. <span class="citation" data-id="305315"><a href="/opinion/305315/united-states-v-john-p-calandra/#1221" aria-description="Citation for case: United States v. John P. Calandra"><i>Id.,</i> at 1221</a></span>.</p>
<p>We granted the Government's petition for certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./410/925/">410 U. S. 925</a></span> (1973). We now reverse.</p>
<p></p>
<h2>II</h2>
<p>The institution of the grand jury is deeply rooted in Anglo-American history.<sup>[3]</sup> In England, the grand jury <span class="star-pagination">*343</span> served for centuries both as a body of accusers sworn to discover and present for trial persons suspected of criminal wrongdoing and as a protector of citizens against arbitrary and oppressive governmental action. In this country the Founders thought the grand jury so essential to basic liberties that they provided in the Fifth Amendment that federal prosecution for serious crimes can only be instituted by "a presentment or indictment of a Grand Jury." Cf. <i>Costello</i> v. <i>United States,</i> <span class="citation" data-id="9421237"><a href="/opinion/105355/costello-v-united-states/#361" aria-description="Citation for case: Costello v. United States">350 U. S. 359, 361-362</a></span> (1956). The grand jury's historic functions survive to this day. Its responsibilities continue to include both the determination whether there is probable cause to believe a crime has been committed and the protection of citizens against unfounded criminal prosecutions. <i>Branzburg</i> v. <i>Hayes,</i> <span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/#686" aria-description="Citation for case: Branzburg v. Hayes">408 U. S. 665, 686-687</a></span> (1972).</p>
<p>Traditionally the grand jury has been accorded wide latitude to inquire into violations of criminal law. No judge presides to monitor its proceedings. It deliberates in secret and may determine alone the course of its inquiry. The grand jury may compel the production of evidence or the testimony of witnesses as it considers appropriate, and its operation generally is unrestrained by the technical procedural and evidentiary rules governing the conduct of criminal trials. "It is a grand inquest, a body with powers of investigation and inquisition, the scope of whose inquiries is not to be limited narrowly by questions of propriety or forecasts of the probable result of the investigation, or by doubts whether any particular individual will be found properly subject to an accusation of crime." <i>Blair</i> v. <i>United States,</i> <span class="citation" data-id="99422"><a href="/opinion/99422/blair-v-united-states/#282" aria-description="Citation for case: Blair v. United States">250 U. S. 273, 282</a></span> (1919).</p>
<p>The scope of the grand jury's powers reflects its special role in insuring fair and effective law enforcement. A grand jury proceeding is not an adversary hearing in which the guilt or innocence of the accused is adjudicated. Rather, it is an <i>ex parte</i> investigation to determine <span class="star-pagination">*344</span> whether a crime has been committed and whether criminal proceedings should be instituted against any person. The grand jury's investigative power must be broad if its public responsibility is adequately to be discharged. <i>Branzburg</i> v. <span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/#700" aria-description="Citation for case: Branzburg v. Hayes"><i>Hayes, supra,</i> at 700</a></span>; <i>Costello</i> v. <i>United States, supra,</i> at 364.</p>
<p>In <i><span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/" aria-description="Citation for case: Branzburg v. Hayes">Branzburg</a></span>,</i> the Court had occasion to reaffirm the importance of the grand jury's role:</p>
<blockquote>"[T]he investigation of crime by the grand jury implements a fundamental governmental role of securing the safety of the person and property of the citizen . . . ." <span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/#700" aria-description="Citation for case: Branzburg v. Hayes">408 U. S., at 700</a></span>.</blockquote>
<blockquote>"The role of the grand jury as an important instrument of effective law enforcement necessarily includes an investigatory function with respect to determining whether a crime has been committed and who committed it. . . . `When the grand jury is performing its investigatory function into a general problem area . . . society's interest is best served by a thorough and extensive investigation.' <i>Wood</i> v. <i>Georgia,</i> <span class="citation" data-id="9422448"><a href="/opinion/106441/wood-v-georgia/#392" aria-description="Citation for case: Wood v. Georgia">370 U. S. 375, 392</a></span> (1962). A grand jury investigation `is not fully carried out until every available clue has been run down and all witnesses examined in every proper way to find if a crime has been committed.' <i>United States</i> v. <i>Stone,</i> <span class="citation" data-id="291186"><a href="/opinion/291186/united-states-v-samuel-stone/#140" aria-description="Citation for case: United States v. Samuel Stone">429 F. 2d 138, 140</a></span> (CA2 1970). Such an investigation may be triggered by tips, rumors, evidence proffered by the prosecutor, or the personal knowledge of the grand jurors. <i>Costello</i> v. <i>United States,</i> <span class="citation" data-id="9421237"><a href="/opinion/105355/costello-v-united-states/#362" aria-description="Citation for case: Costello v. United States">350 U. S., at 362</a></span>. It is only after the grand jury has examined the evidence that a determination of whether the proceeding will result in an indictment can be made . . . ." <i>Id.,</i> at 701-702.</blockquote>
<p>The grand jury's sources of information are widely drawn, and the validity of an indictment is not affected <span class="star-pagination">*345</span> by the character of the evidence considered. Thus, an indictment valid on its face is not subject to challenge on the ground that the grand jury acted on the basis of inadequate or incompetent evidence, <i>Costello</i> v. <i>United States, supra</i><i>; </i><i>Holt</i> v. <i>United States,</i> <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/" aria-description="Citation for case: Holt v. United States">218 U. S. 245</a></span> (1910); or even on the basis of information obtained in violation of a defendant's Fifth Amendment privilege against self-incrimination, <i>Lawn</i> v. <i>United States,</i> <span class="citation" data-id="9421531"><a href="/opinion/105609/lawn-v-united-states/" aria-description="Citation for case: Lawn v. United States">355 U. S. 339</a></span> (1958).</p>
<p>The power of a federal court to compel persons to appear and testify before a grand jury is also firmly established. <i>Kastigar</i> v. <i>United States,</i> <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441</a></span> (1972). The duty to testify has long been recognized as a basic obligation that every citizen owes his Government. <i>Blackmer</i> v. <i>United States,</i> <span class="citation" data-id="101836"><a href="/opinion/101836/blackmer-v-united-states/#438" aria-description="Citation for case: Blackmer v. United States">284 U. S. 421, 438</a></span> (1932); <i>United States</i> v. <i>Bryan,</i> <span class="citation" data-id="9420474"><a href="/opinion/104788/united-states-v-bryan/#331" aria-description="Citation for case: United States v. Bryan">339 U. S. 323, 331</a></span> (1950). In <i>Branzburg</i> v. <i><span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/" aria-description="Citation for case: Branzburg v. Hayes">Hayes, supra,</a></span></i> at 682 and 688, the Court noted that "[c]itizens generally are not constitutionally immune from grand jury subpoenas . . ." and that "the longstanding principle that `the public . . . has a right to every man's evidence' . . . is particularly applicable to grand jury proceedings." The duty to testify may on occasion be burdensome and even embarrassing. It may cause injury to a witness' social and economic status. Yet the duty to testify has been regarded as "so necessary to the administration of justice" that the witness' personal interest in privacy must yield to the public's overriding interest in full disclosure. <i>Blair</i> v. <i>United States,</i> <span class="citation" data-id="99422"><a href="/opinion/99422/blair-v-united-states/#281" aria-description="Citation for case: Blair v. United States">250 U. S., at 281</a></span>. Furthermore, a witness may not interfere with the course of the grand jury's inquiry. He "is not entitled to urge objections of incompetency or irrelevancy, such as a party might raise, for this is no concern of his." <span class="citation" data-id="99422"><a href="/opinion/99422/blair-v-united-states/#282" aria-description="Citation for case: Blair v. United States"><i>Id.,</i> at 282</a></span>. Nor is he entitled "to challenge the authority of the court or of the grand jury" or "to set limits to the investigation that the grand jury may conduct." <i><span class="citation" data-id="99422"><a href="/opinion/99422/blair-v-united-states/" aria-description="Citation for case: Blair v. United States">Ibid.</a></span></i></p>
<p><span class="star-pagination">*346</span> Of course, the grand jury's subpoena power is not unlimited.<sup>[4]</sup> It may consider incompetent evidence, but it may not itself violate a valid privilege, whether established by the Constitution, statutes, or the common law. <i>Branzburg</i> v. <i><span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/" aria-description="Citation for case: Branzburg v. Hayes">Hayes, supra</a></span></i><i>; </i><i>United States</i> v. <i><span class="citation" data-id="9420474"><a href="/opinion/104788/united-states-v-bryan/" aria-description="Citation for case: United States v. Bryan">Bryan, supra</a></span></i><i>; </i><i>Blackmer</i> v. <i>United States, supra;</i> 8 J. Wigmore, Evidence §§ 2290-2391 (McNaughton rev. ed. 1961). Although, for example, an indictment based on evidence obtained in violation of a defendant's Fifth Amendment privilege is nevertheless valid, <i>Lawn</i> v. <i>United States, supra</i><i>,</i> the grand jury may not force a witness to answer questions in violation of that constitutional guarantee. Rather, the grand jury may override a Fifth Amendment claim only if the witness is granted immunity co-extensive with the privilege against self-incrimination. <i>Kastigar</i> v. <i>United States, supra</i><i>.</i> Similarly, a grand jury may not compel a person to produce books and papers that would incriminate him. <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#633" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 633-635</a></span> (1886). Cf. <i>Couch</i> v. <i>United States,</i> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">409 U. S. 322</a></span> (1973). The grand jury is also without power to invade a legitimate privacy interest protected by the Fourth Amendment. A grand jury's subpoena <i>duces tecum</i> will be disallowed if it is "far too sweeping in its terms to be regarded as reasonable" under the Fourth Amendment. <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#76" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 76</a></span> (1906). Judicial supervision is properly exercised in such cases to prevent the wrong before it occurs.</p>
<p></p>
<h2>
<span class="star-pagination">*347</span> III</h2>
<p>In the instant case, the Court of Appeals held that the exclusionary rule of the Fourth Amendment limits the grand jury's power to compel a witness to answer questions based on evidence obtained from a prior unlawful search and seizure. The exclusionary rule was adopted to effectuate the Fourth Amendment right of all citizens "to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures . . . ." Under this rule, evidence obtained in violation of the Fourth Amendment cannot be used in a criminal proceeding against the victim of the illegal search and seizure. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914); <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961). This prohibition applies as well to the fruits of the illegally seized evidence. <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963); <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920).</p>
<p>The purpose of the exclusionary rule is not to redress the injury to the privacy of the search victim:</p>
<blockquote>"[T]he ruptured privacy of the victims' homes and effects cannot be restored. Reparation comes too late." <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#637" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 637</a></span> (1965).</blockquote>
<p>Instead, the rule's prime purpose is to deter future unlawful police conduct and thereby effectuate the guarantee of the Fourth Amendment against unreasonable searches and seizures:</p>
<blockquote>"The rule is calculated to prevent, not to repair. Its purpose is to deterto compel respect for the constitutional guaranty in the only effectively available wayby removing the incentive to disregard it." <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 217</a></span> (1960).</blockquote>
<p><span class="star-pagination">*348</span> Accord, <i>Mapp</i> v. <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#656" aria-description="Citation for case: Mapp v. Ohio"><i>Ohio, supra,</i> at 656</a></span>; <i>Tehan</i> v. <i>Shott,</i> <span class="citation" data-id="6751647"><a href="/opinion/6862154/tehan-v-united-states-ex-rel-shott/#416" aria-description="Citation for case: Tehan v. United States ex rel. Shott">382 U. S. 406, 416</a></span> (1966); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 29</a></span> (1968). In sum, the rule is a judicially created remedy designed to safeguard Fourth Amendment rights generally through its deterrent effect, rather than a personal constitutional right of the party aggrieved.<sup>[5]</sup></p>
<p>Despite its broad deterrent purpose, the exclusionary rule has never been interpreted to proscribe the use of illegally seized evidence in all proceedings or against all persons. As with any remedial device, the application of the rule has been restricted to those areas where its remedial objectives are thought most efficaciously served. The balancing process implicit in this approach is expressed in the contours of the standing requirement. Thus, standing to invoke the exclusionary rule has been confined to situations where the Government seeks to use such evidence to incriminate the victim of the unlawful search. <i>Brown</i> v. <i>United States,</i> <span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/" aria-description="Citation for case: Brown v. United States">411 U. S. 223</a></span> (1973); <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span> (1969); <i>Wong Sun</i> v. <i>United States, supra</i><i>; </i><i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960). This standing rule is premised on a recognition that the need for deterrence and hence the rationale for excluding the evidence are strongest where the Government's unlawful conduct would result in imposition of a criminal sanction on the victim of the search.<sup>[6]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*349</span> IV</h2>
<p>In deciding whether to extend the exclusionary rule to grand jury proceedings, we must weigh the potential injury to the historic role and functions of the grand jury against the potential benefits of the rule as applied in this context. It is evident that this extention of the exclusionary rule would seriously impede the grand jury. Because the grand jury does not finally adjudicate guilt or innocence, it has traditionally been allowed to pursue its investigative and accusatorial functions unimpeded by the evidentiary and procedural restrictions applicable to a criminal trial. Permitting witnesses to invoke the exclusionary rule before a grand jury would precipitate adjudication of issues hitherto reserved for the trial on the merits and would delay and disrupt grand jury proceedings. Suppression hearings would halt the orderly progress of an investigation and might necessitate extended litigation of issues only tangentially related to the grand jury's primary objective.<sup>[7]</sup> The probable <span class="star-pagination">*350</span> result would be "protracted interruption of grand jury proceedings," <i>Gelbard</i> v. <i>United States,</i> <span class="citation" data-id="9424980"><a href="/opinion/108596/gelbard-v-united-states/#70" aria-description="Citation for case: Gelbard v. United States">408 U. S. 41, 70</a></span> (1972) (WHITE, J., concurring), effectively transforming them into preliminary trials on the merits. In some cases the delay might be fatal to the enforcement of the criminal law. Just last Term we reaffirmed our disinclination to allow litigious interference with grand jury proceedings:</p>
<blockquote>"Any holding that would saddle a grand jury with minitrials and preliminary showings would assuredly impede its investigation and frustrate the public's interest in the fair and expeditious administration of the criminal laws." <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#17" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1, 17</a></span> (1973).</blockquote>
<p>Cf. <i>United States</i> v. <i>Ryan,</i> <span class="citation" data-id="108340"><a href="/opinion/108340/united-states-v-ryan/" aria-description="Citation for case: United States v. Ryan">402 U. S. 530</a></span> (1971); <i>Cobbledick</i> v. <i>United States,</i> <span class="citation" data-id="103311"><a href="/opinion/103311/cobbledick-v-united-states/" aria-description="Citation for case: Cobbledick v. United States">309 U. S. 323</a></span> (1940). In sum, we believe that allowing a grand jury witness to invoke the exclusionary rule would unduly interfere with the effective and expeditious discharge of the grand jury's duties.</p>
<p>Against this potential damage to the role and functions of the grand jury, we must weigh the benefits to be derived from this proposed extension of the exclusionary rule. Suppression of the use of illegally seized evidence against the search victim in a criminal trial is thought to be an important method of effectuating the Fourth Amendment. But it does not follow that the Fourth Amendment requires adoption of every proposal that might deter police misconduct. In <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States">394 U. S., at 174-175</a></span>, for example, this <span class="star-pagination">*351</span> Court declined to extend the exclusionary rule to one who was not the victim of the unlawful search:</p>
<blockquote>"The deterrent values of preventing the incrimination of those whose rights the police have violated have been considered sufficient to justify the suppression of probative evidence even though the case against the defendant is weakened or destroyed. We adhere to that judgment. But we are not convinced that the additional benefits of extending the exclusionary rule to other defendants would justify further encroachment upon the public interest in prosecuting those accused of crime and having them acquitted or convicted on the basis of all the evidence which exposes the truth."</blockquote>
<p>We think this observation equally applicable in the present context.</p>
<p>Any incremental deterrent effect which might be achieved by extending the rule to grand jury proceedings is uncertain at best. Whatever deterrence of police misconduct may result from the exclusion of illegally seized evidence from criminal trials, it is unrealistic to assume that application of the rule to grand jury proceedings would significantly further that goal. Such an extension would deter only police investigation consciously directed toward the discovery of evidence solely for use in a grand jury investigation. The incentive to disregard the requirement of the Fourth Amendment solely to obtain an indictment from a grand jury is substantially negated by the inadmissibility of the illegally seized evidence in a subsequent criminal prosecution of the search victim. For the most part, a prosecutor would be unlikely to request an indictment where a conviction could not be obtained. We therefore decline to embrace a view that would achieve a speculative and undoubtedly <span class="star-pagination">*352</span> minimal advance in the deterrence of police misconduct at the expense of substantially impeding the role of the grand jury.<sup>[8]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*353</span> V</h2>
<p>Respondent also argues that each and every question based on evidence obtained from an illegal search and seizure constitutes a fresh and independent violation of the witness' constitutional rights.<sup>[9]</sup> Ordinarily, of course, a witness has no right of privacy before the grand jury. Absent some recognized privilege of confidentiality, every man owes his testimony. He may invoke his Fifth Amendment privilege against compulsory self-incrimination, but he may not decline to answer on the grounds that his responses might prove embarrassing or result in an unwelcome disclosure of his personal affairs. <i>Blair</i> v. <i>United States,</i> <span class="citation" data-id="99422"><a href="/opinion/99422/blair-v-united-states/" aria-description="Citation for case: Blair v. United States">250 U. S. 273</a></span> (1919). Respondent's claim must be, therefore, not merely that the grand jury's questions invade his privacy but that, because those questions are based on illegally obtained evidence, they somehow <span class="star-pagination">*354</span> constitute distinct violations of his Fourth Amendment rights. We disagree.</p>
<p>The purpose of the Fourth Amendment is to prevent unreasonable governmental intrusions into the privacy of one's person, house, papers, or effects. The wrong condemned is the unjustified governmental invasion of these areas of an individual's life. That wrong, committed in this case, is fully accomplished by the original search without probable cause. Grand jury questions based on evidence obtained thereby involve no independent governmental invasion of one's person, house, papers, or effects, but rather the usual abridgment of personal privacy common to all grand jury questioning. Questions based on illegally obtained evidence are only a derivative use of the product of a past unlawful search and seizure. They work no new Fourth Amendment wrong. Whether such derivative use of illegally obtained evidence by a grand jury should be proscribed presents a question, not of rights, but of remedies.</p>
<p>In the usual context of a criminal trial, the defendant is entitled to the suppression of, not only the evidence obtained through an unlawful search and seizure, but also any derivative use of that evidence. The prohibition of the exclusionary rule must reach such derivative use if it is to fulfill its function of deterring police misconduct. In the context of a grand jury proceeding, we believe that the damage to that institution from the unprecedented extension of the exclusionary rule urged by respondent outweighs the benefit of any possible incremental deterrent effect. Our conclusion necessarily controls both the evidence seized during the course of an unlawful search and seizure and any question or evidence derived therefrom (the fruits of the unlawful search).<sup>[10]</sup> The same considerations of logic and policy apply to both the fruits <span class="star-pagination">*355</span> of an unlawful search and seizure and derivative use of that evidence, and we do not distinguish between them.<sup>[11]</sup></p>
<p>The judgment of the Court of Appeals is</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE BRENNAN, with whom MR. JUSTICE DOUGLAS and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>The Court holds that the exclusionary rule in search-and-seizure cases does not apply to grand jury proceedings because the principal objective of the rule is "to deter future unlawful police conduct," <i>ante,</i> at 347, and "it is unrealistic to assume that application of the rule to grand jury proceedings would significantly further that goal." <span class="star-pagination">*356</span> <i>Ante,</i> at 351. This downgrading of the exclusionary rule to a determination whether its application in a particular type of proceeding furthers deterrence of future police misconduct reflects a startling misconception, unless it is a purposeful rejection, of the historical objective and purpose of the rule.</p>
<p>The commands of the Fourth Amendment are, of course, directed solely to public officials. Necessarily, therefore, only official violations of those commands could have created the evil that threatened to make the Amendment a dead letter. But curtailment of the evil, if a consideration at all, was at best only a hoped-for effect of the exclusionary rule, not its ultimate objective. Indeed, there is no evidence that the possible deterrent effect of the rule was given any attention by the judges chiefly responsible for its formulation. Their concern as guardians of the Bill of Rights was to fashion an enforcement tool to give content and meaning to the Fourth Amendment's guarantees. They thus bore out James Madison's prediction in his address to the First Congress on June 8, 1789:</p>
<blockquote>"If they [the rights] are incorporated into the Constitution, independent tribunals of justice will <span class="star-pagination">*357</span> consider themselves in a peculiar manner the guardians of those rights; they will be an impenetrable bulwark against every assumption of power in the Legislative or Executive; they will be naturally led to resist every encroachment upon rights expressly stipulated for in the Constitution by the declaration of rights." 1 Annals of Cong. 439 (1789).</blockquote>
<p>Since, however, those judges were without power to direct or control the conduct of law enforcement officers, the enforcement tool had necessarily to be one capable of administration by judges. The exclusionary rule, if not perfect, accomplished the twin goals of enabling the judiciary to avoid the taint of partnership in official lawlessness and of assuring the peopleall potential victims of unlawful government conductthat the government would not profit from its lawless behavior, thus minimizing the risk of seriously undermining popular trust in government.</p>
<p>That these considerations, not the rule's possible deterrent effect, were uppermost in the minds of the framers of the rule clearly emerges from the decision which fashioned it:</p>
<blockquote>"The effect of the Fourth Amendment is to put the courts of the United States and Federal officials, in the exercise of their power and authority, under limitations and restraints as to the exercise of such power and authority, and to forever secure the people, their persons, houses, papers and effects against all unreasonable searches and seizures under the guise of law. . . . The tendency of those who execute the criminal laws of the country to obtain conviction by means of unlawful seizures . . . <i>should find no sanction in the judgments of the courts which are charged at all times with the support of the Constitution and to which people of all conditions</i> <span class="star-pagination">*358</span> <i>have a right to appeal for the maintenance of such fundamental rights.</i> . . .</blockquote>
<blockquote>.....</blockquote>
<blockquote>"This protection is equally extended to the action of the Government and officers of the law acting under it. . . . <i>To sanction such proceedings would be to affirm by judicial decision a manifest neglect if not an open defiance of the prohibitions of the Constitution, intended for the protection of the people against such unauthorized action.</i>" <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#391" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 391-392, 394</a></span> (1914) (emphasis added).</blockquote>
<p>Mr. Justice Brandeis and Mr. Justice Holmes added their enormous influence to these precepts in their notable dissents in <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span> (1928). Mr. Justice Brandeis said:</p>
<blockquote>"In a government of laws, existence of the government will be imperilled if it fails to observe the law scrupulously. Our Government is the potent, the omnipresent teacher. For good or for ill, it teaches the whole people by its example. Crime is contagious. If the Government becomes a law-breaker, it breeds contempt for law; it invites every man to become a law unto himself; it invites anarchy." <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#485" aria-description="Citation for case: Olmstead v. United States"><i>Id.,</i> at 485</a></span>.</blockquote>
<p>And Mr. Justice Holmes said:</p>
<blockquote>"[W]e must consider the two objects of desire, both of which we cannot have, and make up our minds which to choose. It is desirable that criminals should be detected, and to that end that all available evidence should be used. It also is desirable that the Government should not itself foster and pay for other crimes, when they are the means by which the evidence is to be obtained. . . . We have to <span class="star-pagination">*359</span> choose, and for my part I think it a less evil that some criminals should escape than that the Government should play an ignoble part.</blockquote>
<blockquote>". . . If the existing code does not permit district attorneys to have a hand in such dirty business it does not permit the judge to allow such iniquities to succeed." <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#470" aria-description="Citation for case: Olmstead v. United States"><i>Id.,</i> at 470</a></span>.</blockquote>
<p>The same principles were reiterated less than six years ago. In <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#12" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 12-13</a></span> (1968), Mr. Chief Justice Warren said for the Court:</p>
<blockquote>"The rule also serves another vital function`the imperative of judicial integrity.' <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#222" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 222</a></span> (1960). Courts which sit under our Constitution cannot and will not be made party to lawless invasions of the constitutional rights of citizens by permitting unhindered governmental use of the fruits of such invasions."</blockquote>
<p>It is true that deterrence was a prominent consideration in the determination whether <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), which applied the exclusionary rule to the States, should be given retrospective effect. <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618</a></span> (1965). But that lends no support to today's holding that the application of the exclusionary rule depends solely upon whether its invocation in a particular type of proceeding will significantly further the goal of deterrence. The emphasis upon deterrence in <i><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span></i> must be understood in the light of the crucial fact that the States had justifiably relied from 1949 to 1961 upon <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span> (1949), and consequently, that application of <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> would have required the wholesale release of innumerable convicted prisoners, few of whom could have been successfully retried. In that circumstance, <i><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span></i> held not only that retrospective application of <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> would not further the goal of deterrence but also <span class="star-pagination">*360</span> that it would not further "the administration of justice and the integrity of the judicial process." <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#637" aria-description="Citation for case: Linkletter v. Walker">381 U. S., at 637</a></span>. Cf. <i>Kaufman</i> v. <i>United States,</i> <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#229" aria-description="Citation for case: Kaufman v. United States">394 U. S. 217, 229</a></span> (1969).</p>
<p>Thus, the Court seriously errs in describing the exclusionary rule as merely "a judicially created remedy designed to safeguard Fourth Amendment rights generally through its deterrent effect . . . ." <i>Ante,</i> at 348. Rather, the exclusionary rule is "part and parcel of the Fourth Amendment's limitation upon [governmental] encroachment of individual privacy," <i>Mapp</i> v. <i>Ohio, supra,</i> at 651, and "an essential part of both the Fourth and Fourteenth Amendments," <i>id.,</i> at 657, that "gives to the individual no more than that which the Constitution guarantees him, to the police officer no less than that to which honest law enforcement is entitled, and, to the courts, that judicial integrity so necessary in the true administration of justice." <i>Id.,</i> at 660.</p>
<p>This <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> summation crystallizes the series of decisions that developed the rule and with which today's holding is plainly at war. For the first time, the Court today discounts to the point of extinction the vital function of the rule to insure that the judiciary avoid even the slightest appearance of sanctioning illegal government conduct. This rejection of "the imperative of judicial integrity," <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#222" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 222</a></span> (1960), openly invites "[t]he conviction that all government is staffed by . . . hypocrites [, a conviction] easy to instill and difficult to erase." Paulsen, The Exclusionary Rule and Misconduct by the Police, 52 J. Crim. L. C. &amp; P. S. 255, 258 (1961). When judges appear to become "accomplices in the willful disobedience of a Constitution they are sworn to uphold," <i>Elkins</i> v. <i>United States, supra,</i> at 223, we imperil the very foundation of our people's trust in their Government on which our democracy rests. See <i>On Lee</i> v. <i>United</i> <span class="star-pagination">*361</span> <i>States,</i> <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/#758" aria-description="Citation for case: On Lee v. United States">343 U. S. 747, 758-759</a></span> (1952) (Frankfurter, J., dissenting). The exclusionary rule is needed to make the Fourth Amendment something real; a guarantee that does not carry with it the exclusion of evidence obtained by its violation is a chimera. Moreover,</p>
<blockquote>"[I]nsistence on observance by law officers of traditional fair procedural requirements is, from the long point of view, best calculated to contribute to that end. However much in a particular case insistence upon such rules may appear as a technicality that inures to the benefit of a guilty person, the history of the criminal law proves that tolerance of shortcut methods in law enforcement impairs its enduring effectiveness." <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#313" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 313</a></span> (1958).</blockquote>
<p>The judges who developed the exclusionary rule were well aware that it embodied a judgment that it is better for some guilty persons to go free than for the police to behave in forbidden fashion. A similar judgment led the Court to decide in <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920), that a grand jury must be denied access to plainly relevant but illegally seized papers. In that case, after federal agents unlawfully seized papers belonging to the Silverthornes and their corporation, and presented the documents to a grand jury which had previously indicted the Silverthornes, a district court ordered the documents returned and copies that had been prepared in the interim impounded. After returning the originals, the grand jury attempted to recoup them by issuance of a subpoena <i>duces tecum.</i> Compliance with the subpoena was refused, and contempt convictions followed. In reversing the judgment of convictions, the Court, speaking through Mr. Justice Holmes, held that the Government was barred from utilizing any fruits of its forbidden act, <span class="star-pagination">*362</span> stating that "[t]he essence of a provision forbidding the acquisition of evidence in a certain way is that not merely evidence so acquired shall not be used before the Court but that it shall not be used at all." <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States"><i>Id.,</i> at 392</a></span>.</p>
<p><i>Silverthorne</i> plainly controls this case. Respondent, like plaintiffs in error in <i>Silverthorne,</i><sup>[1]</sup> seeks to avoid furnishing the grand jury with evidence that he would not have been called upon to supply but for the unlawful search and seizure. The Court would distinguish <i>Silverthorne</i> on the ground that there the plaintiffs in error had been indicted and could invoke the exclusionary rule "on the basis of their status as criminal defendants," since the Government's effort to obtain the documents was "founded on a belief that they might be useful in the criminal prosecution already authorized by the grand jury." <i>Ante,</i> at 352 n. 8. The effort was clearly not founded on any such belief. Overlooked is the fact that the grand jury's interest in again obtaining the documents in <i>Silverthorne</i> may well have been to secure information leading to further criminal charges, especially since indictments of three other individuals, as well as additional indictments of the Silverthornes, had been the consequence of initial submission of the documents to the grand jury. See Brief on Behalf of Plaintiffs in Error in No. 358, O. T. 1919, pp. 4, 18-19.<sup>[2]</sup><span class="star-pagination">*363</span> Only if <i>Silverthorne</i> is overruled can its precedential force to compel affirmance here be denied.</p>
<p>Congressional concern with the <i>Silverthorne</i> holding was clearly evidenced in enactment of <span class="citation no-link">18 U. S. C. § 2515</span>, providing that "[w]henever any wire or oral communication has been intercepted, no part of the contents of such communication <i>and no evidence derived therefrom</i> may be received in evidence in any . . . proceeding in or before <i>any</i> . . . <i>grand jury</i> . . . if the disclosure of that information would be in violation of this chapter." (Emphasis added.) In <i>Gelbard</i> v. <i>United States,</i> <span class="citation" data-id="9424980"><a href="/opinion/108596/gelbard-v-united-states/" aria-description="Citation for case: Gelbard v. United States">408 U. S. 41</a></span> (1972), we set aside the adjudication in criminal contempt of a grand jury witness who refused to comply with a court order to testify on the ground that interrogation was to be based upon information obtained from the witness' communications allegedly intercepted by federal agents by means of illegal wiretapping and electronic surveillance. Our reasons track the grounds advanced in <i>Silverthorne.</i></p>
<blockquote>"The purposes of § 2515 and Title III as a whole would be subverted were the plain command of § 2515 ignored when the victim of an illegal interception is called as a witness before a grand jury and asked questions based upon that interception. Moreover, § 2515 serves not only to protect the privacy of communications, but also to ensure that the courts do not become partners to illegal conduct: the evidentiary prohibition was enacted also `to protect the integrity of court and administrative proceedings.' Consequently, to order a grand jury witness, on pain of imprisonment, to disclose evidence that § 2515 bars in unequivocal terms is both <span class="star-pagination">*364</span> to thwart the congressional objective of protecting individual privacy by excluding such evidence and to entangle the courts in the illegal acts of Government agents." 408 U. S., at 51 (footnotes omitted).</blockquote>
<p>Similarly to allow Calandra to be subjected to questions derived from the illegal search of his office and seizure of his files is "to thwart the [Fourth and Fourteenth Amendments' protection] of . . . individual privacy . . . and to entangle the courts in the illegal acts of Government agents." <i>Ibid.</i> "And for a court, on petition of the executive department, to sentence a witness, who is [himself] the victim of the illegal [search and seizure], to jail for refusal to participate in the exploitation of that [conduct in violation of the explicit command of the Fourth Amendment] is to stand our whole system of criminal justice on its head." <i>In re Evans,</i> 146 U. S. App. D. C. 310, 323, <span class="citation" data-id="8886873"><a href="/opinion/8900071/united-states-v-violations-of-18-usc-sections-231-241-245-371-1361/#1252" aria-description="Citation for case: United States v. Violations of 18 U.S.C. Sections 231,...">452 F. 2d 1239, 1252</a></span> (1971) (Wright, J., concurring).</p>
<p>It is no answer, to suggest as the Court does, that the grand jury witnesses' Fourth Amendment rights will be sufficiently protected "by the inadmissibility of the illegally seized evidence in a subsequent criminal prosecution of the search victim." <i>Ante,</i> at 351. This, of course, is no alternative for Calandra, since he was granted transactional immunity and cannot be criminally prosecuted. But the fundamental flaw of the alternative is that to compel Calandra to testify in the first place under penalty of contempt necessarily "thwarts" his Fourth Amendment protection and "entangle[s] the courts in the illegal acts of Government agents"consequences that <i>Silverthorne</i> condemned as intolerable.</p>
<p>To be sure, the exclusionary rule does not "provide that illegally seized evidence is inadmissible against anyone for any purpose." <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#175" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 175</a></span> (1969). But clearly there is a crucial <span class="star-pagination">*365</span> distinction between withholding its cover from individuals whose Fourth Amendment rights have not been violatedas has been done in the "standing" cases, <i>Alderman</i> v. <i>United States, supra</i><i>; </i><i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960)and withdrawing its cover from persons whose Fourth Amendment rights have in fact been abridged.</p>
<p>Respondent does not seek vicariously to assert another's Fourth Amendment rights. He himself has been the victim of an illegal search and desires "to mend no one's privacy [but his] own." <i>Gelbard</i> v. <i>United States, supra,</i> at 63 (DOUGLAS, J., concurring). Respondent is told that he must look to damages to redress the concededly unconstitutional invasion of his privacy. In other words, officialdom may profit from its lawlessness if it is willing to pay a price.</p>
<p>In <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span>,</i> the Court thought it had "close[d] the only courtroom door remaining open to evidence secured by official lawlessness" in violation of Fourth Amendment rights. <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#654" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 654-655</a></span>. The door is again ajar. As a consequence, I am left with the uneasy feeling that today's decision may signal that a majority of my colleagues have positioned themselves to reopen the door still further and abandon altogether the exclusionary rule in search-and-seizure cases; for surely they cannot believe that application of the exclusionary rule at trial furthers the goal of deterrence, but that its application in grand jury proceedings will not "significantly" do so. Unless we are to shut our eyes to the evidence that crosses our desks every day, we must concede that official lawlessness has not abated and that no empirical data distinguishes trials from grand jury proceedings. I thus fear that when next we confront a case of a conviction rested on illegally seized evidence, today's decision will be invoked to sustain the conclusion in that case <span class="star-pagination">*366</span> also, that "it is unrealistic to assume" that application of the rule at trial would "significantly further" the goal of deterrencethough, if the police are presently undeterred, it is difficult to see how removal of the sanction of exclusion will induce more lawful official conduct.</p>
<p>The exclusionary rule gave life to Madison's prediction that "independent tribunals of justice . . . will be naturally led to resist every encroachment upon rights expressly stipulated for in the Constitution by the declaration of rights." 1 Annals of Cong. 439 (1789). We betray the trust upon which that prediction rested by today's long step toward abandonment of the exclusionary rule. The observations of a recent commentator highlight the grievous error of the majority's retreat:</p>
<blockquote>"If constitutional rights are to be anything more than pious pronouncements, then some measurable consequence must be attached to their violation. It would be intolerable if the guarantee against unreasonable search and seizure could be violated without practical consequence. It is likewise imperative to have a practical procedure by which courts can review alleged violations of constitutional rights and articulate the meaning of those rights. The advantage of the exclusionary ruleentirely apart from any direct deterrent effectis that it provides an occasion for judicial review, and it gives credibility to the constitutional guarantees. By demonstrating that society will attach serious consequences to the violation of constitutional rights, the exclusionary rule invokes and magnifies the moral and educative force of the law. Over the long term this may integrate some fourth amendment ideals into the value system or norms of behavior of law enforcement agencies." Oaks, Studying the <span class="star-pagination">*367</span> Exclusionary Rule in Search and Seizure, <span class="citation no-link">37 U. Chi. L. Rev. 665</span>, 756 (1970).</blockquote>
<p>See also Dellinger, Of Rights and Remedies: The Constitution as a Sword, <span class="citation no-link">85 Harv. L. Rev. 1532</span>, 1562-1563 (1972).</p>
<p>I dissent and would affirm the judgment of the Court of Appeals.</p>
<h2>NOTES</h2>
<p>[*]  <i>Melvin L. Wulf</i> and <i>Paul Halvonik</i> filed a brief for the American Civil Liberties Union as <i>amicus curiae</i> urging affirmance.</p>
<p>[1]  On the basis of the same affidavit, federal agents also obtained warrants authorizing searches of Calandra's residence and automobile. The present case involves only the search of the Royal Machine &amp; Tool Co.</p>
<p>[2]  The Court of Appeals affirmed the District Court's finding that the search of Calandra's business and seizure of his property were unlawful. <span class="citation" data-id="305315"><a href="/opinion/305315/united-states-v-john-p-calandra/" aria-description="Citation for case: United States v. John P. Calandra">465 F. 2d 1218</a></span>, 1226 n. 5. Although the Government does not agree with the court's finding, it has not sought review of this issue. In addition, the Government has not challenged the District Court's order directing return of the illegally seized property to Calandra.</p>
<p>[3]  For a discussion of the history and role of the grand jury, see <i>Costello</i> v. <i>United States,</i> <span class="citation" data-id="9421237"><a href="/opinion/105355/costello-v-united-states/#361" aria-description="Citation for case: Costello v. United States">350 U. S. 359, 361-362</a></span> (1956); <i>Blair</i> v. <i>United States,</i> <span class="citation" data-id="99422"><a href="/opinion/99422/blair-v-united-states/#279" aria-description="Citation for case: Blair v. United States">250 U. S. 273, 279-283</a></span> (1919); <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#59" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 59</a></span> (1906); 4 W. Blackstone, Commentaries *301 <i>et seq.;</i> G. Edwards. The Grand Jury 1-44 (1906); 1 F. Pollock &amp; F. Maitland, History of English Law 151 (2d ed. 1909); 1 W. Holdsworth, History of English Law 321-323 (7th rev. ed. 1956).</p>
<p>[4]  The grand jury is subject to the court's supervision in several respects. See <i>Brown</i> v. <i>United States,</i> <span class="citation" data-id="9421773"><a href="/opinion/105848/brown-v-united-states/#49" aria-description="Citation for case: Brown v. United States">359 U. S. 41, 49</a></span> (1959); Fed. Rules Crim. Proc. 6 and 17; 1 L. Orfield, Criminal Procedure Under the Federal Rules § 6:108, pp. 475-477 (1966). In particular, the grand jury must rely on the court to compel production of books, papers, documents, and the testimony of witnesses, and the court may quash or modify a subpoena on motion if compliance would be "unreasonable or oppressive." Fed. Rule Crim. Proc. 17 (c).</p>
<p>[5]  There is some disagreement as to the practical efficacy of the exclusionary rule, and as the Court noted in <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#218" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 218</a></span> (1960), relevant "[e]mpirical statistics are not available." Cf. Oaks, Studying the Exclusionary Rule in Search and Seizure, <span class="citation no-link">37 U. Chi. L. Rev. 665</span> (1970). We have no occasion in the present case to consider the extent of the rule's efficacy in criminal trials.</p>
<p>[6]  In holding that the respondent had standing to invoke the exclusionary rule in a grand jury proceeding, the Court of Appeals relied on Fed. Rule Crim. Proc. 41 (e). <span class="citation" data-id="305315"><a href="/opinion/305315/united-states-v-john-p-calandra/#1222" aria-description="Citation for case: United States v. John P. Calandra">465 F. 2d, at 1222-1224</a></span>. Rule 41 (e) provides, in relevant part, that "[a] person aggrieved by an unlawful search and seizure may move the district court . . . for the return of the property and to suppress for the use as evidence anything so obtained . . . ." It further states that "[t]he motion shall be made before trial or hearing . . . ." We have recognized that Rule 41 (e) is "no broader than the constitutional rule." <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span>, 173 n. 6 (1969); <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960). Rule 41 (e), therefore, does not constitute a statutory expansion of the exclusionary rule.
</p>
<p>The Court of Appeals also found that the Government's offer of immunity under <span class="citation no-link">18 U. S. C. § 2514</span> was irrelevant to respondent's standing to invoke the exclusionary rule. <span class="citation" data-id="305315"><a href="/opinion/305315/united-states-v-john-p-calandra/#1221" aria-description="Citation for case: United States v. John P. Calandra">465 F. 2d, at 1221</a></span>. We agree with that determination for the reasons stated in Parts III, IV, and V of this opinion.</p>
<p>[7]  The force of this argument is well illustrated by the facts of the present case. As of the date of this decision, almost two and one-half years will have elapsed since respondent was summoned to appear and testify before the grand jury. If respondent's testimony was vital to the grand jury's investigation in August 1971 of extortionate credit transactions, it is possible that this particular investigation has been completely frustrated.</p>
<p>[8]  Respondent relies primarily on <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920), which the dissent contends "plainly controls this case." <i>Post,</i> at 362. In that case, federal officers unlawfully seized certain documents belonging to the Silverthornes and their lumber company and presented them to a grand jury that had already indicted the Silverthornes and the company. A district court ordered the return of the documents but impounded photographs and copies of the originals. Later, the prosecutor caused the grand jury to issue subpoenas <i>duces tecum</i> to the Silverthornes and the company to produce the originals, and their refusal to comply led to a contempt citation. In reversing the judgment, the Court held that the subpoenas were invalid because they were based on knowledge obtained from the illegally seized evidence, citing <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914). Mr. Justice Holmes, writing for the Court, stated that the "essence of a provision forbidding the acquisition of evidence in a certain way is that not merely evidence so acquired shall not be used before the Court but that it shall not be used at all." <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S., at 392</a></span>.
</p>
<p><i>Silverthorne</i> is distinguishable from the present case in several significant respects. There, plaintiffs in error had previously been indicted by the grand jury and thus could invoke the exclusionary rule on the basis of their status as criminal defendants. Moreover, the Government's interest in recapturing the original documents was founded on a belief that they might be useful in the criminal prosecution already authorized by the grand jury. It did not appear that the grand jury needed the documents to perform its investigative or accusatorial functions. Thus, the primary consequence of the Court's decision was to exclude the evidence from the subsequent criminal trial. Finally, prior to the issuance of the grand jury subpoenas, there had been a judicial determination that the search and seizure were illegal. The claim of plaintiffs in error was not raised for the first time in a pre-indictment motion to suppress requiring interruption of grand jury proceedings.</p>
<p>By contrast, in the instant case respondent had not been indicted by the grand jury and was not a criminal defendant. Under traditional principles, he had no standing to invoke the exclusionary rule. The effect of the District Court's order was to deprive the grand jury of testimony it needed to conduct its investigation. Furthermore, respondent's motion to suppress had not been previously made and required interruption of the grand jury proceedings. In these circumstances, <i>Silverthorne</i> is certainly not controlling. To the extent that the Court's broad dictum might be construed to suggest a different result in the present case, we note that it has been substantially undermined by later cases. See Parts III and IV of this opinion.</p>
<p>[9]  At oral argument, counsel for respondent stated the contention as follows:
</p>
<p>"I submit to the Court that each question asked of the Respondent before the Grand Jury, which question was only asked because of a past violation of the Fourth Amendment, [amounts to] a new, immediate violation of the Fourth Amendment . . . . [A] question derived from a past violation, a question into the privacy of the witness amounts to another intrusion in violation of the Fourth Amendment." Tr. of Oral Arg. 17.</p>
<p>"[R]efusing to answer a question in which the question conceivably is derived from a past violation of the Fourth Amendment, gives rise to an additional or new Fourth Amendment right to resist answering that question because the question itself becomes an additional intrusion . . . ." Tr. of Oral Arg. 19-20.</p>
<p>[10]  It should be noted that, even absent the exclusionary rule, a grand jury witness may have other remedies to redress the injury to his privacy and to prevent a further invasion in the future. He may be entitled to maintain a cause of action for damages against the officers who conducted the unlawful search. <i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971). He may also seek return of the illegally seized property, and exclusion of the property and its fruits from being used as evidence against him in a criminal trial. <i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span> (1931). In these circumstances, we cannot say that such a witness is necessarily left remediless in the face of an unlawful search and seizure.</p>
<p>[11]  The dissent's reliance on <i>Gelbard</i> v. <i>United States,</i> <span class="citation" data-id="9424980"><a href="/opinion/108596/gelbard-v-united-states/" aria-description="Citation for case: Gelbard v. United States">408 U. S. 41</a></span> (1972), is misplaced. There, the Court construed <span class="citation no-link">18 U. S. C. § 2515</span>, the evidentiary prohibition of Tit. III of the Omnibus Crime Control and Safe Streets Act of 1968, <span class="citation no-link">82 Stat. 211</span>, as amended, <span class="citation no-link">18 U. S. C. §§ 2510-2520</span>. It held that § 2515 could be invoked by a grand jury witness as a defense to a contempt charge brought for refusal to answer questions based on information obtained from the witness' communications alleged to have been unlawfully intercepted through wiretapping and electronic surveillance. The Court's holding rested exclusively on an interpretation of Tit. III, which represented a congressional effort to afford special safeguards against the unique problems posed by misuse of wiretapping and electronic surveillance. There was no indication, in either <i><span class="citation" data-id="9424980"><a href="/opinion/108596/gelbard-v-united-states/" aria-description="Citation for case: Gelbard v. United States">Gelbard</a></span></i> or the legislative history, that Tit. III was regarded as a restatement of existing law with respect to grand jury proceedings. As MR. JUSTICE WHITE noted in his concurring opinion in <i><span class="citation" data-id="9424980"><a href="/opinion/108596/gelbard-v-united-states/" aria-description="Citation for case: Gelbard v. United States">Gelbard</a></span>,</i> Tit. III "unquestionably works a change in the law with respect to the rights of grand jury witnesses . . . ." 408 U. S., at 70.
</p>
<p>The dissent also voices concern that today's decision will betray " `the imperative of judicial integrity,' " sanction "illegal government conduct," and even "imperil the very foundation of our people's trust in their Government." <i>Post,</i> at 360. There is no basis for this alarm. "Illegal conduct" is hardly sanctioned, nor are the foundations of the Republic imperiled, by declining to make an unprecedented extension of the exclusionary rule to grand jury proceedings where the rule's objectives would not be effectively served and where other important and historic values would be unduly prejudiced. Cf. <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span> (1969); <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618</a></span> (1965); and cases cited <i>supra,</i> at 347-348.</p>
<p>[1]  Neither the Silverthorne Lumber Co., because it was a corporation, see <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43</a></span> (1906), nor respondent, because he was granted transactional immunity, could invoke the privilege against self-incrimination. The situations are therefore completely comparable.</p>
<p>[2]  The Court also argues that "[t]he [Silverthorne's claim] was not raised for the first time in a pre-indictment motion to suppress requiring interruption of grand jury proceedings," <i>ante,</i> at 352 n. 8, and therefore presumably its assertion occasioned no delay. However, the District Court in <i>Silverthorne</i> had granted an earlier application for return of the seized documents from the grand jury after determining that they had been obtained in violation of the Fourth Amendment. This Court made no intimation that the District Court acted improperly in considering the initial application.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Camou.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Camou
type: case
citation: "773 F.3d 932 (2014)"
parallel_cite: ""
neutral_cite: "2014 U.S. App. LEXIS 23347; 2014 WL 6980135"
court: 9th Cir. 2014
court_level: coa
circuit: ca9
year: 2014
date_decided: 2014-12-11
docket: 12-50598
authority_weight: "Binding in-circuit — 9th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/2759861/united-states-v-chad-camou/"
  cluster_id: 2759861
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Camou
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Automobile Exception]]"
    role: Key
related:
  - "[[Automobile Exception]]"
  - "[[Riley v. California]]"
  - "[[California v. Acevedo]]"
  - "[[United States v. Ross]]"
tags:
  - case
  - fourth-amendment
  - search
  - automobile-exception
  - digital-privacy
  - warrant-requirement
holding: "A cell phone found in a vehicle is not a 'container' for purposes of the automobile (vehicle) exception, so probable cause to search the vehicle does not authorize a warrantless search of the phone's data; extending Riley v. California, the search of Camou's phone — untimely as a search incident to arrest, unsupported by exigency, and outside the vehicle exception — was unconstitutional and was not saved by inevitable discovery or good faith."
---

# United States v. Camou

*773 F.3d 932 (9th Cir. 2014)* (No. 12-50598) · U.S. Court of Appeals for the Ninth Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 2759861 → opinion 2759861 (773 F.3d 932, decided 2014-12-11); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Border Patrol agents stopped Chad Camou's truck at a Highway 86 checkpoint in Westmorland, California, and found an undocumented immigrant hiding behind the front seats. At 10:40 p.m. the agents arrested Camou and seized both the truck and a cell phone from the cab. One hour and twenty minutes later, after booking and interviews, an agent searched the phone — scrolling through its call logs, then videos, then photographs — and discovered images of child pornography. Camou was charged with possession of child pornography and moved to suppress the images. The district court denied the motion, ruling the search was a valid [[Search Incident to Arrest|search incident to arrest]] and, alternatively, that the good-faith and inevitable-discovery exceptions applied. Camou entered a conditional guilty plea and appealed.

## Issue
Whether the warrantless search of Camou's cell phone — conducted an hour and twenty minutes after his arrest, on a phone taken from his truck — could be justified as a [[Search Incident to Arrest|search incident to arrest]], under the [[Exigent Circumstances and Hot Pursuit|exigency]] exception, or under the automobile (vehicle) exception.

## Rule
Under the vehicle exception, officers with probable cause may search a vehicle and any containers found in it without a warrant. But a cell phone is not such a container. Extending *[[Riley v. California|Riley]]* from the search-incident-to-arrest context, the court reasoned that the vast and qualitatively different privacy interest in a phone's data cannot be swept into a doctrine built for glove compartments, luggage, boxes, and bags, and held: "We hold, however, that cell phones are not containers for purposes of the vehicle exception." — 773 F.3d at 944. ^pin-944

## Application
None of the three exceptions fit. The search was not incident to arrest, because the hour-and-twenty-minute gap and seven intervening acts made it not roughly contemporaneous with the arrest. It was not justified by [[Exigent Circumstances and Hot Pursuit|exigency]], because the agent never claimed the data was in danger of destruction, and it was not. And it could not rest on the vehicle exception, because a phone is not a container — treating it as one would let officers sift through all of a phone's data unbounded by the [[Exigent Circumstances and Hot Pursuit|exigency]] or crime-relevance limits that cabin the other exceptions. The court also rejected the government's inevitable-discovery and good-faith arguments.

## Conclusion
**Reversed**: the warrantless search of Camou's cell phone violated the Fourth Amendment, and the images were not saved by [[Inevitable Discovery and Independent Source|inevitable discovery]] or good faith. Pregerson, J., wrote for the panel.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Camou* carries *[[Riley v. California|Riley]]* into the automobile-exception setting: a cell phone found in a car is not a "container" that probable cause to search the vehicle allows officers to open, so a warrant is required to search the phone's data even where the vehicle exception otherwise applies.

## Appears on
- [[Automobile Exception]] — *Key*

## Sources
- [*United States v. Camou*, 773 F.3d 932 (9th Cir. 2014)](https://www.courtlistener.com/opinion/2759861/united-states-v-chad-camou/) — pinpoint: 944 (cell-phone-not-a-container holding; the CL opinion text star-paginates the F.3d reporter). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e9ee2168395b82e9", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Camou"}, "payload": {"all": [{"cite": "773 F.3d 932", "page": "932", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "773"}, {"cite": "2014 U.S. App. LEXIS 23347", "page": "23347", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2014"}, {"cite": "2014 WL 6980135", "page": "6980135", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2014"}], "display": "773 F.3d 932", "official": {"cite": "773 F.3d 932", "page": "932", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "773"}, "official_selection_present": true, "record_id": "United States v. Camou"}}
{"assertion_id": "8e524bdc3be7d90b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Camou"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Camou", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Camou

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Camou",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Chad Camou",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Chad Daniel CAMOU, Defendant-Appellant",
    "input_case_name": "United States v. Camou",
    "court": "9th Cir. 2014",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": "2014-12-11",
    "year": 2014,
    "docket": "12-50598",
    "cluster_id": 2759861,
    "lead_opinion_id": 2759861,
    "sibling_ids": [],
    "absolute_url": "/opinion/2759861/united-states-v-chad-camou/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "773 F.3d 932",
      "volume": "773",
      "reporter": "F.3d",
      "page": "932",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2014 U.S. App. LEXIS 23347",
        "volume": "2014",
        "reporter": "U.S. App. LEXIS",
        "page": "23347",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 6980135",
        "volume": "2014",
        "reporter": "WL",
        "page": "6980135",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "773 F.3d 932",
        "volume": "773",
        "reporter": "F.3d",
        "page": "932",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 U.S. App. LEXIS 23347",
        "volume": "2014",
        "reporter": "U.S. App. LEXIS",
        "page": "23347",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 6980135",
        "volume": "2014",
        "reporter": "WL",
        "page": "6980135",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "773 F.3d 932",
    "official_selection": {
      "court_class": "coa",
      "selected": "773 F.3d 932",
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
    "date_created": "2026-07-06T05:50:36Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:50:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:50:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:50:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:50:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-camou--2759861",
      "to_record_id": "United States v. Camou",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Camou

```
                     FOR PUBLICATION

    UNITED STATES COURT OF APPEALS
         FOR THE NINTH CIRCUIT


 UNITED STATES OF AMERICA,                       No. 12-50598
               Plaintiff-Appellee,
                                                   D.C. No.
                    v.                        3:11-cr-05027-H-1

 CHAD DANIEL CAMOU,
            Defendant-Appellant.                   OPINION


        Appeal from the United States District Court
          for the Southern District of California
         Marilyn L. Huff, District Judge, Presiding

                    Argued May 7, 2013
                 Submitted December 3, 2014
                    Pasadena, California

                   Filed December 11, 2014

 Before: Harry Pregerson and Raymond C. Fisher, Circuit
       Judges, and James S. Gwin, District Judge.*

                  Opinion by Judge Pregerson




  *
    The Honorable James S. Gwin, District Judge for the U.S. District
Court for the Northern District of Ohio, sitting by designation.
2                   UNITED STATES V. CAMOU

                           SUMMARY**


                           Criminal Law

    The panel reversed the district court’s denial of a criminal
defendant’s motion to suppress images of child pornography
found on his cell phone during a warrantless search.

    The panel held that the warrantless search of the cell
phone at a Border Patrol checkpoint’s security offices was not
roughly contemporaneous with the defendant’s arrest and,
therefore, not a search incident to arrest, given both the
passage of one hour and twenty minutes between arrest and
search, and the seven intervening acts between arrest and
search that signaled the arrest was over.

    The panel held that the search of the cell phone is not
excused under the exigency exception to the warrant
requirement because the government failed to show exigent
circumstances that required immediate police action, and
even if the exigencies permitted a search of the phone to
prevent the loss of call data, the search’s scope was
impermissibly overbroad.

   The panel held that cell phones are not containers for
purposes of the vehicle exception to the warrant requirement,
and that the search of the defendant’s cell phone therefore
cannot be justified under that exception.




  **
     This summary constitutes no part of the opinion of the court. It has
been prepared by court staff for the convenience of the reader.
                 UNITED STATES V. CAMOU                     3

   The panel concluded that neither the inevitable-discovery
exception to the exclusionary rule, nor the good-faith
exception, applies.


                        COUNSEL

James Fife, Deputy Federal Public Defenders, San Diego,
California, for Defendant-Appellant

Alessandra P. Serano, Assistant United States Attorney, San
Diego, California, for Plaintiff-Appellee.


                         OPINION

PREGERSON, Circuit Judge:

    Chad Camou appeals the district court’s denial of his
motion to suppress images of child pornography found on his
cell phone during a warrantless search. We have jurisdiction
pursuant to 28 U.S.C. § 1291. We reverse.

    FACTUAL & PROCEDURAL BACKGROUND

I. Camou’s Arrest and the Seizure of Camou’s Cell
   Phone at 10:40 p.m.

    On August 1, 2009, United States Border Patrol agents
stopped a truck belonging to Chad Camou at a primary
inspection checkpoint on Highway 86 in Westmorland,
California. Camou was driving the truck, while his girlfriend,
Ashley Lundy, sat in the passenger seat. Agents at the
checkpoint grew suspicious when Lundy did not make eye
4                UNITED STATES V. CAMOU

contact, so they asked Camou if they could open the door to
the truck. Once they opened the door, the agents saw
Alejandro Martinez-Ramirez (Martinez-Ramirez), an
undocumented immigrant, lying on the floor behind the
truck’s front seats. Consequently, at about 10:40 p.m., agents
arrested and handcuffed Camou, Lundy, and Martinez-
Ramirez. At the same time, agents also seized Camou’s truck
and a cell phone found in the cab of the truck. Agents then
moved Camou, Lundy, and Martinez-Ramirez into the
checkpoint’s security offices for booking.

II. Agents Processed, Booked, and Interviewed Camou at
    the Security Offices

   Once at the checkpoint’s security offices, Border Patrol
agents processed and booked Camou and Lundy. At some
point during the booking process, Border Patrol Agent
Andrew Baldwin inventoried Camou’s cell phone as “seized
property and evidence.”

   Agents then began to interview Camou and Lundy.
Lundy was given Miranda warnings. It is unclear whether
Camou was given Miranda warnings or whether he said
anything to the agents at this point. Neither Camou nor
Lundy asked for an attorney.

    During Lundy’s initial interview with Border Patrol
Agent Richard Walla, Lundy waived her Miranda rights and
explained that, before she and Camou picked up Martinez-
Ramirez, Camou had received a phone call from Jessie, a.k.a.
“Mother Teresa.” “Mother Teresa” arranged for Camou to
pick up Martinez-Ramirez in Calexico, California and
transport him to either Palm Desert, California or Coachella,
California. During Lundy’s interview, Camou’s cell phone
                 UNITED STATES V. CAMOU                     5

rang several times. The caller identification screen on the
phone displayed the phone number that Lundy had identified
as belonging to “Mother Teresa.” Agents asked Camou if the
cell phone belonged to him. Camou replied, “Yes.”

    Border Patrol Agents Jason Masney and Ciudad Real
attempted to further interview Martinez-Ramirez, Camou, and
Lundy. Martinez-Ramirez told the agents that he had been in
the car for about forty minutes and that Camou had planned
to take him to Los Angeles. Camou invoked his right to
remain silent. Lundy, meanwhile, agreed to answer more
questions. She told the agents that she and Camou had been
smuggling undocumented immigrants about eight times per
month for about nine months. She explained that Camou
would receive phone calls from smugglers on his cell phone
both before and after passing the Highway 86 checkpoint.

III.   Warrantless Search of Camou’s Cell Phone at
       12:00 a.m.

    At 12:00 a.m., one hour and twenty minutes after
Camou’s arrest, Agent Walla searched Camou’s cell phone.
In his subsequent report, Agent Walla claimed he was looking
for evidence of “known smuggling organizations and
information related to the case.” Agent Walla did not assert
that the search was necessary to prevent the destruction of
evidence or to ensure his or anyone else’s safety.

    Agent Walla searched the call logs of the cell phone and
discovered several recent calls from “Mother Teresa.” Agent
Walla closed the call logs screen and opened the videos
stored on the phone’s internal memory. He saw several
videos that appeared to be taken near the Calexico, California
Port of Entry. He then closed the videos and opened the
6                UNITED STATES V. CAMOU

photographs, which were also stored on the phone’s internal
memory. He “scrolled quickly through about 170 of the
images before stopping. Of the images he viewed, about 30
to 40 were child pornography. Walla was disturbed by the
images and stopped reviewing the contents of the phone.”

    After stopping the search, Agent Walla called U.S.
Immigration and Customs Enforcement, the Imperial County
Sheriff’s Office, and the FBI to pursue child pornography
charges against Camou. Assistant United States Attorney
John Weis at the El Centro Sector Prosecutions Office did not
pursue alien smuggling charges against Camou because Weis
decided that the smuggling case against Camou “did not meet
prosecution guidelines.” Weis informed Border Patrol agents
of his decision the same day Camou’s cell phone was
searched by Agent Walla.

    Several days later, on August 5, 2009, the FBI executed
a federal warrant to search Camou’s cell phone for child
pornography. Pursuant to the warrant, the FBI found several
hundred images of child pornography on the cell phone.

IV.    District Court Proceedings

    A grand jury indicted Camou for possession of child
pornography in violation of 18 U.S.C. § 2252(a)(4)(B).
Camou moved the district court to suppress the child
pornography images found on his cell phone, arguing that the
warrantless search of his cell phone at the checkpoint’s
security offices violated his Fourth Amendment rights. The
district court denied Camou’s motion. The district court
found that the search of the phone was a lawful search
incident to arrest and, even if the search was unconstitutional,
                 UNITED STATES V. CAMOU                     7

the good faith and inevitable discovery exceptions to the
exclusionary rule were satisfied.

    Camou entered a conditional guilty plea to possession of
child pornography in violation of 18 U.S.C. § 2252(a)(4)(B).
Camou was sentenced to thirty-seven months in prison
followed by five years of supervised release. Camou is
currently serving his prison sentence. Camou appeals the
district court’s denial of his motion to suppress.

                STANDARD OF REVIEW

     We review de novo the district court’s denial of a motion
to suppress. United States v. Song Ja Cha, 597 F.3d 995, 999
(9th Cir. 2010). We review the district court’s underlying
factual findings for clear error. Id. We review de novo the
application of the good faith and inevitable discovery
exceptions to the exclusionary rule. United States v. Krupa,
658 F.3d 1174, 1179 (9th Cir. 2011).

                       DISCUSSION

    Camou argues that the warrantless search of his cell
phone was unconstitutional because the search was not
incident to arrest, and no other exceptions to the warrant
requirement apply. Camou also argues that the exclusionary
rule bars the admissibility of the images found on his phone.
We agree.

I. Search Incident to Arrest

   A search incident to a lawful arrest is an exception to the
general rule that warrantless searches violate the Fourth
Amendment. The exception allows a police officer making
8                   UNITED STATES V. CAMOU

a lawful arrest to conduct a search of the area within the
arrestee’s “immediate control,” that is, “the area from within
which [an arrestee] might gain possession of a weapon or
destructible evidence.” Chimel v. California, 395 U.S. 752,
763 (1969) (internal quotation marks omitted), abrogated on
other grounds by Arizona v. Gant, 556 U.S. 332, 344 (2009).

    The first requirement of a search incident to arrest is that
the search be limited to the arrestee’s person or areas in the
arrestee’s “immediate control” at the time of arrest. Gant,
556 U.S. at 339; Chimel, 395 U.S. at 763; United States v.
Turner, 926 F.2d 883, 887 (9th Cir. 1991). The “immediate
control” requirement ensures that a search incident to arrest
will not exceed the rule’s two original purposes of protecting
arresting officers and preventing the arrestee from destroying
evidence: “If there is no possibility that an arrestee could
reach into the area that law enforcement officers seek to
search, both justifications for the search-incident-to-arrest
exception are absent and the rule does not apply.” Gant,
556 U.S. at 339.1

    The second requirement of a search incident to arrest is
that the search be spatially and temporally incident to the
arrest. See United States v. Chadwick, 433 U.S. 1, 15 (1977),
abrogated on other grounds by California v. Acevedo,


  1
    One exception to the immediate control requirement, however, occurs
in the vehicle context. Where the search incident to arrest is of a vehicle,
the Supreme Court has held: “Although it does not follow from Chimel,
we also conclude that circumstances unique to the vehicle context justify
a search incident to lawful arrest when it is ‘reasonable to believe
evidence relevant to the crime of the arrest might be found in the
vehicle.’” Gant, 556 U.S. at 343 (emphasis added) (quoting Thornton v.
United States, 541 U.S. 615, 632 (2004) (Scalia, J., concurring in
judgment)).
                  UNITED STATES V. CAMOU                         9

500 U.S. 565, 580 (1991); United States v. Hudson, 100 F.3d
1409, 1419 (9th Cir. 1996). The Supreme Court has held that
“warrantless searches of luggage or other property seized at
the time of an arrest cannot be justified as incident to that
arrest . . . if the search is remote in time or place from the
arrest . . . .” Chadwick, 433 U.S. at 15 (emphasis added).
We have interpreted the temporal requirement to mean that
the search must be “roughly contemporaneous with the
arrest.” United States v. Smith, 389 F.3d 944, 951 (9th Cir.
2004) (per curiam).

    We have summed up the two general requirements of a
valid search incident to arrest as follows: “The determination
of the validity of a search incident to arrest in this circuit is a
two-fold inquiry: (1) was the searched item ‘within the
arrestee’s immediate control when he was arrested’; (2) did
‘events occurring after the arrest but before the search ma[k]e
the search unreasonable’?” United States v. Maddox,
614 F.3d 1046, 1048 (9th Cir. 2010) (quoting United States
v. Turner, 926 F.2d 883, 887 (9th Cir. 1992)).

     We need not decide whether the government meets the
first requirement of search incident to arrest because the
government cannot show that the second requirement—that
the search be spatially and temporally incident to the
arrest—is met.

    Agent Walla’s search of Camou’s cell phone was too far
removed in time from Camou’s arrest to be incident to that
arrest. As stated above, we have interpreted the temporal
requirement to mean that the search must be “roughly
contemporaneous with the arrest.” Smith, 389 F.3d at 951.
To determine whether this contemporaneity requirement is
met, we have stated that the focus is “upon whether the arrest
10               UNITED STATES V. CAMOU

and search are so separated in time or by intervening acts that
the latter cannot be said to have been incident to the former.”
Id. In some cases, we have “relied on the number of minutes
that passed between the arrest and the search. . . . In other
cases, we have relied on a more impressionistic sense of the
flow of events that begins with the arrest and ends with the
search.” United States v. Caseres, 533 F.3d 1064, 1073 (9th
Cir. 2008).

    In Caseres, we found that a search of the arrestee-
defendant’s car was not incident to arrest for two independent
reasons: (1) the “arrest was not spatially related to the
vehicle” because Caseres, the arrestee, was a block and a half
away from his car at the time of his arrest; and (2) “the search
. . . was too far removed in time from the arrest to be
considered as truly incidental to [the] arrest.” Id. at 1072,
1074. We noted that, while it was unclear from the record
how much time passed between arrest and search, the district
court reasonably found the search was conducted “well after”
the arrest. Id. at 1074. In holding that the search was too
temporally removed from the arrest, we reasoned that the
“arrest and the search were separated not only by substantial
time, but also by a string of intervening events that signaled
that the exigencies of the situation had dissipated.” Id. The
intervening events we noted were: police questioning of
Caseres, conversations between police, and police moving
back and forth between the site of the arrest and Caseres’s
car. Id.

    In Maddox, we similarly held that the warrantless search
of an arrestee-defendant’s car was not incident to arrest, but
in so holding we relied solely on intervening events between
the arrest and search. 614 F.3d at 1048. In Maddox, after
Maddox ignored the officer’s request to exit his car following
                    UNITED STATES V. CAMOU                             11

a stop for reckless driving, the officer seized Maddox’s key
chain and cell phone and threw them on the front seat. Id. at
1047. The officer arrested and handcuffed Maddox and
placed him in the back of the patrol car. Id. He then returned
to Maddox’s car, reached inside, and grabbed the key chain
and cell phone. Id. The key chain included a metal vial with
a screw top. Id. The officer unscrewed the metal vial’s top
and discovered methamphetamine inside. Id. We held that
the intervening event of Maddox being handcuffed and placed
in the back of a patrol car rendered the search unreasonable.
Id. at 1048–49; see also United States v. Vasey, 834 F.2d 782,
787–88 (9th Cir. 1987) (holding that the warrantless search of
Vasey’s car was not incident to arrest where the search
occurred thirty to forty-five minutes after Vasey was arrested;
Vasey was handcuffed and placed in the back of the patrol car
before the search; and officers “conducted several
conversations with Vasey” between arrest and search); United
States v. Monclavo-Cruz, 662 F.2d 1285, 1288 (9th Cir. 1981)
(holding that the warrantless search of an arrestee’s purse at
the station house, about an hour after she was arrested next to
her car, was not sufficiently contemporaneous with the arrest
to be incident to arrest).2

   Here, Agent Walla’s search of Camou’s cell phone was
not roughly contemporaneous with Camou’s arrest and,


  2
    We briefly note that, by citing to United States v. Johns, 469 U.S. 478
(1985), the government incorrectly conflates two different search and
seizure doctrines: search incident to arrest and the vehicle exception to
the warrant requirement. As Johns did not concern a search incident to
arrest, Johns’s holding allowing a three-day delay in searching seized
items does not help the government’s search incident to arrest argument.
We revisit the government’s Johns argument in the next section when
analyzing whether the vehicle exception to the warrant requirement
applies.
12               UNITED STATES V. CAMOU

therefore, was not incident to arrest. First, one hour and
twenty minutes passed between Camou’s arrest and Agent
Walla’s search of the cell phone. This delay is longer than
the thirty to forty-five minutes in Vasey and the one hour in
Monclavo-Cruz; and the searches in those two cases were
deemed not sufficiently contemporaneous with arrest.

    Second, a string of intervening acts occurred between
Camou’s arrest and the search of his cell phone that make the
one hour and twenty minute delay even more unreasonable:
(1) Camou and Lundy were restrained with handcuffs; (2)
Camou and Lundy were moved from the checkpoint area to
the security offices; (3) Camou and Lundy were processed;
(4) agents moved Camou’s cell phone from the vehicle into
the security offices, inventoried the phone as a seized item,
and moved the phone into the interview rooms; (5) Camou
and Lundy were interviewed as part of the booking process;
(6) Martinez-Ramirez was interviewed; and (7) Agents
Masney and Real interviewed Lundy for a second time and
tried to interview Camou, who invoked his right to remain
silent. These intervening acts include the same sort of
intervening acts in Caseres—police questioning the arrestee,
conversations between police, and police moving between the
site of the arrest and the site of search—as well as the
intervening acts of Maddox and Vasey—police handcuffing
the arrestee and placing him under police control. And here
we also have the additional intervening acts of police booking
the arrestee, police questioning the material witness,
Martinez-Ramirez, and police moving the item to be
searched––i.e., Camou’s cell phone––from the site of the
arrest to the security offices.

   Given both the passage of one hour and twenty minutes
between arrest and search and the seven intervening acts
                 UNITED STATES V. CAMOU                       13

between arrest and search that signaled the arrest was over,
we conclude that the search of the phone was not roughly
contemporaneous with arrest and, therefore, was not a search
incident to arrest.

II. Two Other Exceptions to the Warrant Requirement:
    the Exigency Exception & the Vehicle Exception

    Several of the government’s arguments more properly fall
under the exigency and vehicle exceptions. For the reasons
explained below, we conclude that neither of these exceptions
is met.

    A. The Exigency Exception

    Under the exigency exception, officers may make a
warrantless search if: (1) they have probable cause to believe
that the item or place to be searched contains evidence of a
crime, and (2) they are facing exigent circumstances that
require immediate police action.           See Warden, Md.
Penitentiary v. Hayden, 387 U.S. 294, 298–301 (1967)
(upholding a warrantless search where “the exigencies of the
situation made that course imperative”). We have defined
exigent circumstances as “those circumstances that would
cause a reasonable person to believe that entry [or search] . . .
was necessary to prevent physical harm to the officers or
other persons, the destruction of relevant evidence, the escape
of the suspect, or some other consequence improperly
frustrating legitimate law enforcement efforts.” United States
v. McConney, 728 F.2d 1195, 1199 (9th Cir. 1984) (en banc),
overruled on other grounds by Estate of Merchant v.
Comm’r, 947 F.2d 1390, 1392–93 (9th Cir. 1991). To be
reasonable, a search under this exception must be limited in
scope so that it is “strictly circumscribed by the exigencies
14                UNITED STATES V. CAMOU

which justify its initiation.” Mincey v. Arizona, 437 U.S. 385,
393 (1978) (internal quotation marks omitted); see also
United States v. Reyes-Bosque, 596 F.3d 1017, 1029 (9th Cir.
2010) (“In order to prove that the exigent circumstances
doctrine justified a warrantless search, the government must
[also] show that . . . the search’s scope and manner were
reasonable to meet the need.”).

     After we submitted this case, the Supreme Court granted
the petition for writ of certiorari in Riley v. California, 134 S.
Ct. 999 (2014), on January 17, 2014, to answer the following
question: “Whether evidence admitted at petitioner’s trial was
obtained in a search of petitioner’s cell phone that violated
petitioner’s Fourth Amendment rights.” We then vacated
submission of this case pending the Supreme Court’s decision
in Riley. On June 25, 2014, the Supreme Court issued its
unanimous decision in Riley v. California, 134 S. Ct. 2473
(2014), holding that “a warrant is generally required before
. . . a search [of a cell phone], even when a cell phone is
seized incident to arrest.” Id. at 2493. The Court went on,
however, to note that “other case-specific exceptions may still
justify a warrantless search of a particular phone.” Id. at
2494. Specifically, the exigency exception “could include the
need to prevent the imminent destruction of evidence in
individual cases, to pursue a fleeing suspect, and to assist
persons who are seriously injured or are threatened with
imminent injury.” Id.

    Even if there was probable cause to search Camou’s cell
phone, we conclude that the government failed to meet the
second prong of the exigency exception: exigent
circumstances that require immediate police action.
                 UNITED STATES V. CAMOU                       15

    The government argues that “the volatile nature of call
logs and other cell phone information with the passing of
time” presented an exigent circumstance. Riley forecloses
this argument. There, the Court determined that “once law
enforcement officers have secured a cell phone, there is no
longer any risk that the arrestee himself will be able to delete
incriminating data from the phone.” Riley, 134 S. Ct. at 2486.
And although “information on a cell phone may nevertheless
be vulnerable to . . . remote wiping,” there is “little reason to
believe that [this] problem is prevalent.” Id. And, “as to
remote wiping, law enforcement is not without specific
means to address the threat. Remote wiping can be fully
prevented by disconnecting the phone from the network.” Id.
at 2487. When “the police are truly confronted with a ‘now
or never’ situation—for example, circumstances suggesting
that a defendant’s phone will be the target of an imminent
remote-wipe attempt—they may be able to rely on exigent
circumstances to search the phone immediately.” Id (internal
quotation marks omitted). Here, the search of Camou’s cell
phone occurred one hour and twenty minutes after his arrest.
This was not an “imminent” “now or never situation” such
that the exigency exception would apply. Moreover, the
record does not indicate that Agent Walla believed the call
logs on Camou’s cell phone were volatile and that a search of
Camou’s phone was necessary to prevent the loss of recent
call data.

    And even if we were to assume that the exigencies of the
situation permitted a search of Camou’s cell phone to prevent
the loss of call data, the search’s scope was impermissibly
overbroad. The search in this case went beyond contacts and
call logs to include a search of hundreds of photographs and
videos stored on the phone’s internal memory. Thus, Agent
Walla exceeded the scope of any possible exigency by
16               UNITED STATES V. CAMOU

extending the search beyond the call logs to examine the
phone’s photographs and videos. See State v. Carroll,
778 N.W.2d 1, 12 (Wis. 2010) (holding that the exigency
exception justified the answering of an incoming call on the
defendant’s cell phone but did not justify a search of images
stored on the phone “because there were no exigent
circumstances at the time requiring [the officer] to review the
gallery or other data stored on the phone. That data was not
in immediate danger of disappearing before [the officer]
could obtain a warrant.”). We therefore conclude that the
search of Camou’s cell phone is not excused under the
exigency exception to the warrant requirement.

     B. The Vehicle Exception

    Another exception to the Fourth Amendment’s warrant
requirement is the vehicle exception. Carroll v. United
States, 267 U.S. 132, 153–54 (1925). Under the vehicle
exception, officers may search a vehicle and any containers
found therein without a warrant, so long as they have
probable cause. California v. Acevedo, 500 U.S. 565, 580
(1991); United States v. Ross, 456 U.S. 798, 821–22, 825
(1982). Unlike search incident to arrest, the vehicle
exception is not rooted in arrest and the Chimel rationales of
preventing arrestees from harming officers and destroying
evidence. Instead, the vehicle exception is motivated by the
supposedly lower expectation of privacy individuals have in
their vehicles as well as the mobility of vehicles, which
allows evidence contained within those vehicles to be easily
concealed from the police. Carroll, 267 U.S. at 153;
California v. Carney, 471 U.S. 386, 390–91 (1985).

   As the Supreme Court noted in Arizona v. Gant, the
permissible scope of a vehicle exception search is “broader”
                 UNITED STATES V. CAMOU                     17

than that of a search incident to arrest: “If there is probable
cause to believe a vehicle contains evidence of criminal
activity, [Ross] authorizes a search of any area of the vehicle
in which the evidence might be found. . . . Ross allows
searches for evidence relevant to offenses other than the
offense of arrest.” 556 U.S. 332, 347 (2009) (citing Ross,
456 U.S. at 820–21). Moreover, unlike searches incident to
arrest, searches of vehicles and containers pursuant to the
vehicle exception need not be conducted right away. United
States v. Johns, 469 U.S. 478, 487–88 (1985). So long as the
officers had probable cause to believe the car had evidence of
criminal activity when they seized a container from inside the
car, they may delay searching it. Id. Delays, however, must
be “reasonable in light of all the circumstances.” United
States v. Albers, 136 F.3d 670, 674 (9th Cir. 1998) (upholding
as reasonable a seven- to ten-day delay in viewing videotapes
and film seized from a houseboat).

    We assume that the agents had probable cause to believe
Camou’s truck contained evidence of criminal activity once
they saw Martinez-Ramirez lying down behind the seats of
the truck. If the vehicle exception applied in this case,
pursuant to Johns and Albers, the one hour and twenty minute
delay between the seizure of Camou’s cell phone and the
search of its contents would not invalidate the search. We
hold, however, that cell phones are not containers for
purposes of the vehicle exception.

    In New York v. Belton, the Supreme Court defined
“container” as “any object capable of holding another object”
and explained that in the vehicle context, containers
“include[] closed or open glove compartments, consoles, or
other receptacles located anywhere within the passenger
compartment, as well as luggage, boxes, bags, clothing, and
18               UNITED STATES V. CAMOU

the like.” 453 U.S. 454, 460 n.4 (1981), overruled on other
grounds by Gant, 556 U.S. at 350–51. In United States v.
Ross, the Supreme Court provided “paper bags, locked
trunks, lunch buckets, and orange crates” as examples of
containers. 456 U.S. 798, 821–22 (1982).

    Then, in Riley, the Supreme Court examined the
definition of “container” as it would apply to cell phones and
the search incident to arrest exception. The Court found:

       Treating a cell phone as a container whose
       contents may be searched incident to an arrest
       is a bit strained as an initial matter. But the
       analogy crumbles entirely when a cell phone
       is used to access data located elsewhere, at the
       tap of a screen.

134 S. Ct. 2473, 2491 (2014) (citation omitted).

    The Court then addressed the government’s proposal that
cell phone searches incident to arrest be analyzed under the
Gant standard imported from the vehicle context:

       [A] Gant standard would prove no practical
       limit at all when it comes to cell phone
       searches. In the vehicle context, Gant
       generally protects against searches for
       evidence of past crimes. In the cell phone
       context, however, it is reasonable to expect
       that incriminating information will be found
       on a phone regardless of when the crime
       occurred. . . . The sources of potential
       pertinent information are virtually unlimited,
       so applying the Gant standard to cell phones
                 UNITED STATES V. CAMOU                      19

       would in effect give police officers unbridled
       discretion to rummage at will among a
       person’s private effects.

Id. at 2492 (internal quotation marks omitted).

    Given the Court’s extensive analysis of cell phones as
“containers” and cell phone searches in the vehicle context,
we find no reason not to extend the reasoning in Riley from
the search incident to arrest exception to the vehicle
exception. Just as “[c]ell phones differ in both a quantitative
and a qualitative sense from other objects that might be kept
on an arrestee’s person,” so too do cell phones differ from
any other object officers might find in a vehicle. Id. at 2489.
Today’s cell phones are unlike any of the container examples
the Supreme Court has provided in the vehicle context.
Whereas luggage, boxes, bags, clothing, lunch buckets,
orange crates, wrapped packages, glove compartments, and
locked trunks are capable of physically “holding another
object,” see Belton, 453 U.S. at 460 n.4, “[m]odern cell
phones, as a category, implicate privacy concerns far beyond
those implicated by the search of a cigarette pack, a wallet, or
a purse,” Riley, 134 S. Ct. at 2488–89. In fact, “a cell phone
search would typically expose to the government far more
than the most exhaustive search of a house.” Id. at 2491
(emphasis in original).

    We further note that the privacy intrusion of searching a
cell phone without a warrant is of particular concern in the
vehicle exception context because the allowable scope of the
search is broader than that of an exigency search, or a search
incident to arrest.      Whereas exigency searches are
circumscribed by the specific exigency at hand and searches
incident to arrest are limited to areas within the arrestee’s
20                UNITED STATES V. CAMOU

immediate control or to evidence relevant to the crime of
arrest, vehicle exception searches allow for evidence relevant
to criminal activity broadly. If cell phones are considered
containers for purposes of the vehicle exception, officers
would often be able to sift through all of the data on cell
phones found in vehicles because they would not be
restrained by any limitations of exigency or relevance to a
specific crime.

    We therefore conclude that cell phones are non-containers
for purposes of the vehicle exception to the warrant
requirement, and the search of Camou’s cell phone cannot be
justified under that exception.

III.      Inevitable Discovery and the Good Faith
          Exceptions to the Exclusionary Rule

    The government argues that, even if the warrantless
search of Camou’s cell phone was unconstitutional, the
photographs found as a result of the search should not be
suppressed because the inevitable discovery and good faith
exceptions to the exclusionary rule are met. We disagree
with the government and find that neither exception is met.

       A. Inevitable Discovery

    The exclusionary rule allows courts to suppress evidence
obtained as a result of an unconstitutional search or seizure.
Mapp v. Ohio, 367 U.S. 643, 655 (1961); Weeks v. United
States, 232 U.S. 383, 393 (1914). But if the government can
establish by a preponderance of the evidence that the
unlawfully obtained information “ultimately or inevitably
would have been discovered by lawful means,” the
exclusionary rule will not apply. Nix v. Williams, 467 U.S.
                 UNITED STATES V. CAMOU                      21

431, 444 (1984). We have “never applied the inevitable
discovery exception so as to excuse the failure to obtain a
search warrant where the police had probable cause but
simply did not attempt to obtain a warrant.” United States v.
Young, 573 F.3d 711, 723 (9th Cir. 2009) (quoting United
States v. Mejia, 69 F.3d 309, 320 (9th Cir. 1995)). As we
reasoned in Mejia, “[i]f evidence were admitted
notwithstanding the officers’ unexcused failure to obtain a
warrant, simply because probable cause existed, then there
would never be any reason for officers to seek a warrant.”
69 F.3d at 320.

    Here, the government argues that a warrant to search
Camou’s cell phone for evidence of smuggling activity
inevitably would have been sought and approved, and
therefore that the inevitable discovery doctrine applies. This
argument fails for two independent reasons.

    First, the government has not proved by a preponderance
of the evidence that it would have applied for a warrant to
search Camou’s phone for evidence of alien smuggling
activity. In fact, the record points to the opposite conclusion:
that no search warrant would have been sought and thus that
no search warrant would have been approved. Camou was
ultimately charged only with possession of child
pornography, not with alien smuggling. Border Patrol agents
knew the day Agent Walla searched Camou’s cell phone that
Camou would not be charged with alien smuggling. The
Sector Prosecutions Office informed the agents that day that
“prosecution was declined” in the smuggling case against
Camou because the case “did not meet prosecution
guidelines.” Because the reasonable conclusion from the
record is that no search warrant would have been sought, the
22               UNITED STATES V. CAMOU

inevitable discovery exception to the exclusionary rule is not
satisfied.

    Second, and more importantly, Mejia governs this case.
By asking this court to conclude that the inevitable discovery
exception applies here because a search warrant would have
issued, the government is asking us to “excuse the failure to
obtain a search warrant where the police had probable cause
but simply did not attempt to obtain a warrant.” Mejia,
69 F.3d at 320. Under Mejia, this is impermissible and the
inevitable discovery exception to the exclusionary rule is not
satisfied.

     B. Good Faith

     When the officer executing an unconstitutional search
acted in “good faith,” or on “objectively reasonable reliance,”
the exclusionary rule does not apply. See United States v.
Leon, 468 U.S. 897, 922 (1984).               The burden of
demonstrating good faith rests with the government. United
States v. Kow, 58 F.3d 423, 428 (9th Cir. 1995). The test for
good faith is an objective one: “whether a reasonably well
trained officer would have known that the search was illegal
in light of all the circumstances.” United States v. Herring,
555 U.S. 135, 145 (2009) (internal quotation marks omitted).

    In Herring, the Supreme Court applied the good faith
exception to an officer’s arrest and search incident to arrest of
the defendant. The Court held that the officer had reasonably
relied on the county clerk’s assertion that the defendant had
an active arrest warrant. Id. at 149–50. The clerk based her
assertion on another law enforcement employee’s negligent
bookkeeping entry, which falsely indicated that the defendant
had an active arrest warrant. Id. In holding that the good
                  UNITED STATES V. CAMOU                       23

faith exception applied, the Court reasoned that “the error was
the result of isolated negligence attenuated from the arrest”
and that “an error that arises from nonrecurring and
attenuated negligence is . . . far removed from the core
concerns that led us to adopt the rule in the first place.” Id. at
138, 144. The Court further stated that “[t]o trigger the
exclusionary rule, police conduct must be sufficiently
deliberate that exclusion can meaningfully deter it, and
sufficiently culpable that such deterrence is worth the price
paid by the justice system.” Id. at 144.

    We conclude the good faith exception does not apply
here. The governing law at the time of the search made clear
that a search incident to arrest had to be contemporaneous
with the arrest. See, e.g., United States v. Hudson, 100 F.3d
1409, 1419 (9th Cir. 1996). The government has not met its
burden to prove that a reasonably well-trained officer in
Agent Walla’s position could have believed that the search of
Camou’s cell phone one hour and 20 minutes after Camou’s
arrest was lawful. The government does not advance any
arguments except that in searching the phone Agent Walla
was not acting “through ‘reckless or deliberate’ officer
misconduct,” and that Herring controls.

    But Herring is distinguishable. Herring dealt with an
officer’s reliance on a county clerk’s assertion that the
defendant had an outstanding warrant, which was in turn
based on another law enforcement employee’s negligence.
The officer was not negligent himself; the negligence was
two degrees removed from the officer and thus amounted to
“isolated negligence attenuated from the arrest.” 555 U.S. at
137. In Herring, as in its prior good faith jurisprudence, the
Supreme Court found the good faith exception was met
because the officer reasonably relied on an external source,
24                  UNITED STATES V. CAMOU

which turned out to be erroneous. Id.; see also Arizona v.
Evans, 514 U.S. 1, 14 (1995) (holding that good faith
exception was met where police reasonably relied on
erroneous information concerning an arrest warrant in a
database maintained by judicial employees); Illinois v. Krull,
480 U.S. 340, 358–60 (1987) (extending good faith exception
to searches conducted in reasonable reliance on subsequently
invalidated statutes); Leon, 468 U.S. at 922 (holding that the
officer’s reasonable reliance on a warrant later held to be
invalid met the good faith exception).

    The Supreme Court has never applied the good faith
exception to excuse an officer who was negligent himself,
and whose negligence directly led to the violation of the
defendant’s constitutional rights.3 Here, the government fails
to assert that Agent Walla relied on anyone or anything in
conducting his search of Camou’s cell phone, let alone that
any reliance was reasonable. The government instead only
asserts that by searching the phone, Agent Walla was not
acting “recklessly[,] or deliberately” misbehaving. In this
case, the good faith exception cannot apply.

                          CONCLUSION

   For the foregoing reasons, we REVERSE the district
court’s denial of Camou’s motion to suppress.

 3
   In fact, because “objectively reasonable” and “negligent” are mutually
exclusive, the only way to reconcile the “objectively reasonable reliance”
rule established in Leon with Herring is to conclude that the officer who
executed the unconstitutional search or seizure cannot have been the
negligent actor. Herring should be read as holding instead that when an
officer reasonably relies on incorrect information that was the result of
another individual’s “isolated” and “attenuated” negligence, the good faith
exception applies.

```

---
