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

## GROUP: _overhaul2/lake/cases/Alasaad v. Wolf.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Alasaad v. Wolf
type: case
citation: "988 F.3d 8 (2021)"
parallel_cite: ""
neutral_cite: ""
court: 1st Cir. 2021
court_level: coa
circuit: ca1
year: 2021
date_decided: 2021-02-09
docket: 20-1077P
authority_weight: "Binding in-circuit — 1st Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4855246/alasaad-v-wolf/"
  cluster_id: 4855246
  opinion_id: null
  identity_checked: false
lake:
  record_id: Alasaad v. Wolf
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Border Searches]]"
    role: Key
related:
  - "[[Border Searches]]"
  - "[[Riley v. California]]"
  - "[[United States v. Montoya de Hernandez]]"
tags:
  - case
  - fourth-amendment
  - border-search
  - digital-privacy
  - electronic-devices
  - reasonable-suspicion
holding: "Border searches of electronic devices — basic or advanced — require neither a warrant nor probable cause, and basic device searches are routine searches that need no reasonable suspicion; the CBP and ICE device-search policies are constitutional."
aliases:
  - Alasaad v. Mayorkas
---

# Alasaad v. Wolf

*988 F.3d 8 (1st Cir. 2021)* (No. 20-1077P) · U.S. Court of Appeals for the First Circuit · **Binding in-circuit — 1st Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 4855246 → lead opinion 4659025 (988 F.3d 8, decided 2021-02-09); Rule quote string-matched to the CL opinion text 2026-07-07. CL text is slip-paginated (no 988 F.3d star pagination), so the pin is slip-style per S2 A3. S9 promotes. -->

## Background
Eleven travelers (ten U.S. citizens and one lawful permanent resident) whose smartphones and laptops were searched at U.S. ports of entry sued the Department of Homeland Security, challenging the CBP and ICE policies governing border searches of electronic devices. Those policies permit suspicionless "basic" (manual) searches and allow "advanced" (forensic) searches on reasonable suspicion. A district court held both types of searches non-routine and required reasonable suspicion that a device contains contraband; the government and the plaintiffs cross-appealed.

## Issue
Whether the Fourth Amendment requires a warrant, probable cause, or reasonable suspicion before border officers may conduct basic or advanced searches of a traveler's electronic devices.

## Rule
Joining the Ninth and Eleventh Circuits, the First Circuit held that the border-search exception governs and imposes no warrant or probable-cause requirement on device searches: "We too hold that neither a warrant nor probable cause is required for a border search of electronic devices." — slip op. at 16. It further held that basic device searches are routine and need no reasonable suspicion, and it rejected the argument that *[[Riley v. California|Riley]]*'s warrant rule for [[Search Incident to Arrest|searches incident to arrest]] carries over to the border.

## Application
The court reasoned that the government's interest is at its zenith at the border and a traveler's privacy expectation at its nadir, so *[[Riley v. California|Riley]]*'s search-incident-to-arrest logic does not transplant to the border context. It declined to limit device searches to hunting for digital contraband, and — because the challenged policies already required reasonable suspicion for advanced searches — it did not decide the minimum showing the Constitution demands for a forensic search, resolving only that the policies as written were constitutional.

## Conclusion
The First Circuit **reversed in part**, holding that the CBP and ICE policies do not violate the Fourth or First Amendments and rejecting the district court's contraband-only limitation.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Alasaad* is a leading circuit statement that the border-search exception reaches electronic devices without a warrant or probable cause, deepening a circuit consensus (with the Ninth and Eleventh Circuits) while leaving open the precise suspicion standard for advanced forensic searches — the open question *[[Riley v. California|Riley]]* pressed but did not resolve at the border.

## Appears on
- [[Border Searches]] — *Key*

## Sources
- [*Alasaad v. Wolf*, 988 F.3d 8 (1st Cir. 2021)](https://www.courtlistener.com/opinion/4855246/alasaad-v-wolf/) — pinpoint: slip op. at 16 (holding on warrant/probable cause); the CL opinion text carries the slip-opinion page numbers rather than 988 F.3d star pagination, so the pin is slip-style per S2 A3. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2486696e7b4ed51a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Alasaad v. Wolf"}, "payload": {"all": [{"cite": "988 F.3d 8", "page": "8", "reporter": "F.3d", "selected_official": true, "source": "web-dual-leg", "type": 1, "volume": "988"}], "display": "988 F.3d 8", "official": {"cite": "988 F.3d 8", "page": "8", "reporter": "F.3d", "selected_official": true, "source": "web-dual-leg", "type": 1, "volume": "988"}, "official_selection_present": true, "record_id": "Alasaad v. Wolf"}}
{"assertion_id": "3a2a5e266557343a", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Alasaad v. Wolf"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Alasaad v. Wolf", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Alasaad v. Wolf

```json
{
  "schema_version": "s2.v1",
  "record_id": "Alasaad v. Wolf",
  "status": "under_review",
  "identity": {
    "case_name": "Alasaad v. Wolf",
    "case_name_short": "Alasaad",
    "case_name_full": "",
    "input_case_name": "Alasaad v. Wolf",
    "court": "1st Cir. 2021",
    "court_id": "ca1",
    "court_level": "coa",
    "circuit": "ca1",
    "state": null,
    "date_decided": "2021-02-09",
    "year": 2021,
    "docket": "20-1077P",
    "cluster_id": 4855246,
    "lead_opinion_id": 4659025,
    "sibling_ids": [],
    "absolute_url": "/opinion/4855246/alasaad-v-wolf/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "988 F.3d 8",
      "volume": "988",
      "reporter": "F.3d",
      "page": "8",
      "type": 1,
      "selected_official": true,
      "source": "web-dual-leg"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "988 F.3d 8",
        "volume": "988",
        "reporter": "F.3d",
        "page": "8",
        "type": 1,
        "selected_official": true,
        "source": "web-dual-leg"
      }
    ],
    "display": "988 F.3d 8",
    "official_selection": {
      "court_class": "coa",
      "selected": "988 F.3d 8",
      "reason": "web-dual-leg"
    },
    "web_legs": [
      {
        "source": "Google Scholar",
        "url": "https://scholar.google.com/scholar_case?case=9076179695157864510",
        "cite": "988 F.3d 8",
        "checked_date": "2026-07-07"
      },
      {
        "source": "vLex",
        "url": "https://case-law.vlex.com/vid/alasaad-v-mayorkas-20-885676844",
        "cite": "988 F.3d 8",
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
    "date_created": "2026-07-06T05:02:27Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:02:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:02:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:02:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:02:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "alasaad-v-wolf--4855246",
      "to_record_id": "Alasaad v. Wolf",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Alasaad v. Wolf

```
           United States Court of Appeals
                       For the First Circuit


Nos. 20-1077
     20-1081

    GHASSAN ALASAAD; NADIA ALASAAD; SUHAIB ALLABABIDI; SIDD
  BIKKANNAVAR; JEREMIE DUPIN; AARON GACH; ISMAIL ABDEL-RASOUL,
   a/k/a Isma'il Kushkush; DIANE MAYE ZORRI; ZAINAB MERCHANT;
             MOHAMMED AKRAM SHIBLY; MATTHEW WRIGHT,

               Plaintiffs, Appellees/Cross-Appellants,

                                 v.

ALEJANDRO MAYORKAS, Secretary of the U.S. Department of Homeland
Security, in his official capacity;* TROY MILLER, Senior Official
  Performing the Duties of the Commissioner of U.S. Customs and
  Border Protection, in his official capacity;** TAE D. JOHNSON,
  Senior Official Performing the Duties of the Director of U.S.
Immigration and Customs Enforcement, in his official capacity,***

               Defendants, Appellants/Cross-Appellees.



     *    Pursuant to Fed. R. App. P. 43(c)(2), Secretary of the
U.S. Department of Homeland Security Alejandro Mayorkas has been
substituted for former Acting Secretary of the U.S. Department of
Homeland Security Chad F. Wolf as appellant/cross-appellee.
     **   Pursuant to Fed. R. App. P. 43(c)(2), Senior Official
Performing the Duties of the Commissioner of U.S. Customs and
Border Protection Troy Miller has been substituted for former Chief
Operating Officer and Senior Official Performing the Duties of the
Commissioner of U.S. Customs and Border Protection Mark A. Morgan
as appellant/cross-appellee.
     ***  Pursuant to Fed. R. App. P. 43(c)(2), Senior Official
Performing the Duties of the Director of U.S. Immigration and
Customs Enforcement Tae D. Johnson has been substituted for former
Senior Official Performing the Duties of the Director of U.S.
Immigration   and   Customs   Enforcement    Tony   H.   Pham   as
appellant/cross-appellee.
            APPEALS FROM THE UNITED STATES DISTRICT COURT
                  FOR THE DISTRICT OF MASSACHUSETTS

            [Hon. Denise J. Casper, U.S. District Judge]


                                 Before

                  Lynch and Selya, Circuit Judges,
                  and Laplante,**** District Judge.


     Joshua Paul Waldman, Appellate Staff, Civil Division U.S.
Department of Justice, with whom Joseph H. Hunt, Assistant Attorney
General, Scott R. McIntosh, Appellate Staff, Civil Division U.S.
Department of Justice, and Andrew E. Lelling, United States
Attorney, were on briefs, for appellants/cross-appellees.
     Esha Bhandari, with whom Adam Schwartz, Sophia Cope, Saira
Hussain, Electronic Frontier Foundation, Hugh Handeyside, Nathan
Freed Wessler, American Civil Liberties Union Foundation, Matthew
R. Segal, Jessie J. Rossman, and American Civil Liberties Union
Foundation   of   Massachusetts,   Inc.   were   on   briefs,   for
appellees/cross-appellants.
     Caroline M. DeCell, Stephanie Krent, Bruce D. Brown, Katie
Townsend, Gabriel Rottman, Caitlin Vogus, and Linda Moon on brief
for the Knight First Amendment Institute at Columbia University,
the Reporters Committee for Freedom of the Press, and 12 Media
Organizations, amici curiae.
     Kurt Wimmer, Rafael Reyneri, Calvin Cohen, Frank Broomell,
and Covington & Burling LLP on brief for the Center for Democracy
& Technology, the Brennan Center for Justice, R Street Institute,
and Techfreedom, amici curiae.
     Michael J. Iacopino, Michael Price, and Mukund Rathi on brief
for National Association of Criminal Defense Lawyers, amicus
curiae.
     Christopher T. Bavitz and Cyberlaw Clinic, Harvard Law
School, on brief for Harvard Immigration and Refugee Clinic, amicus
curiae.
     Meghan Koushik, Mark C. Fleming, Wilmer Cutler Pickering Hale
and Dorr LLP, Glenn Katon, and Hammad Alam on brief for Asian
Americans Advancing Justice, Asian Law Caucus, et al., amici
curiae.
     Elizabeth B. Wydra, Brianne J. Gorod, Brian R. Frazelle, and


     **** Of    the   District    of   New   Hampshire,   sitting   by
designation.
Dayna J. Zolle on brief for Constitutional Accountability Center,
amicus curiae.
     Jennifer Pinsof, David A. Schulz, Media Freedom & Information
Access Clinic, Yale Law School Abrams Institute, Elizabeth A.
Ritvo, Joshua P. Dunn, and Brown Rudnick LLP on brief for Floyd
Abrams, Jack M. Balkin, Hannah Bloch-Webah, Kiel Brennan-Marquez,
Ryan Calo, Danielle Keats Citron, Julie E. Cohen, Catherine Crump,
Mary Anne Franks, Woodrow Hartzog, Heidi Kitrosser, Gregory
Magarian, Neil M. Richards, Scott Skinner-Thompson, Daniel J.
Solove, Amie Stepanovich, Katherine J. Strandburg, and Ari Ezra
Waldman, amici curiae.


                        February 9, 2021
            LYNCH, Circuit Judge.       Plaintiffs bring a civil action

seeking   to    enjoin   current    policies   which      govern    searches    of

electronic devices at this country's borders.                They argue that

these    border   search   policies     violate     the    Fourth    and   First

Amendments both facially and as applied.            The policies each allow

border agents to perform "basic" searches of electronic devices

without reasonable suspicion and "advanced" searches only with

reasonable suspicion.      In these cross-appeals we conclude that the

challenged border search policies, both on their face and as

applied to the two plaintiffs who were subject to these policies,

are    within   permissible    constitutional       grounds.        We   find   no

violations of either the Fourth Amendment or the First Amendment.

While this court apparently is the first circuit court to address

these questions in a civil action, several of our sister circuits

have    addressed    similar       questions   in    criminal       proceedings

prosecuted by the United States.         We join the Eleventh Circuit in

holding that advanced searches of electronic devices at the border

do not require a warrant or probable cause.                 United States v.

Vergara, 884 F.3d 1309, 1311-12 (11th Cir. 2018).                  We also join

the Ninth and Eleventh Circuits in holding that basic border

searches of electronic devices are routine searches that may be

performed without reasonable suspicion.             United States v. Cano,

934 F.3d 1002, 1016 (9th Cir. 2019), petition for cert. filed (Jan.

29, 2021) (No. 20-1043); United States v. Touset, 890 F.3d 1227,


                                     - 4 -
1233 (11th Cir. 2018). We also hold the district court erroneously

narrowed the scope of permissible searches of such equipment at

the border.1

                                   I. Facts

               The material facts are not in dispute.          We supplement

our   description     of     the   facts     with    the   district   court's

comprehensive statement of facts. Alasaad v. Nielsen, 419 F. Supp.

3d 142, 148-50 (D. Mass. 2019); Alasaad v. Nielsen, No. 17-cv-

11730-DJC, 2018 WL 2170323 at *1-2 (D. Mass. May 9, 2018).

A. Agency Policies

           Two policies promulgated by U.S. Customs and Border

Protection ("CBP") and U.S. Immigration and Customs Enforcement

("ICE") are at issue in this case.

           The first policy is CBP Directive No. 3340-049A, Border

Search    of    Electronic    Devices      (2018),     https://www.cbp.gov/

sites/default/files/assets/documents/2018-Jan/CBP-Directive-

3340-049A-Border-Search-of-Electronic-Media-Compliant.pdf                (the

"CBP Policy").      The CBP Policy "provide[s] guidance and standard

operating procedures for searching, reviewing, retaining, and

sharing information contained in . . . mobile phones . . . and any

other communication, electronic, or digital devices . . . to ensure

compliance with customs, immigration, and other laws that CBP is


      1   We acknowledge with appreciation the assistance of the
amici curiae in this case.


                                    - 5 -
authorized to enforce and administer."       CBP Policy at 1.2     The CBP

Policy defines an "electronic device" as "[a]ny device that may

contain information in an electronic or digital form, such as

computers, tablets, disks, drives, tapes, mobile phones and other

communication devices, cameras, music and other media players."

Id. at 2.     The CBP Policy does not address CBP's authority to

search electronic devices with a warrant, consent, or in response

to exigent circumstances.        Id.

            The   CBP   Policy    distinguishes     between   "basic"    and

"advanced" searches.3      It defines an "advanced search" as "any

search in which an Officer connects external equipment, through a

wired or wireless connection, to an electronic device not merely

to gain access to the device, but to review, copy, and/or analyze

its contents."    Id. at 5.      Advanced searches require "supervisory

approval" and under the CBP Policy may only be performed "[i]n

instances in which there is reasonable suspicion of activity in

violation of the laws enforced or administered by CBP, or in which

there is a national security concern."        Id.     A "basic search" is

any non-advanced search.      Id. at 4.    The CBP Policy states that a

basic search may be performed "with or without suspicion."              Id.


     2    The policy is mandatory.    CBP Policy at 1 ("All CBP
Officers . . . shall adhere to the policy." (emphasis added)).
     3    "Advanced" searches are sometimes referred to as
"forensic" searches.    Though the terms are not precisely co-
extensive, any difference is immaterial here.


                                   - 6 -
            For both basic and advanced searches, the CBP Policy

only allows officers to search "information that is resident upon

the device," and devices must be disconnected from the internet

before a search is performed.           Id.

            In addition, the CBP Policy states that "[a]n Officer

may detain electronic devices . . . for a brief, reasonable period

of time to perform a thorough border search."                 Id. at 7.

            The second policy is Immigration and Customs Enforcement

Directive No. 7-6.1, Border Searches of Electronic Devices (2009),

https://hdhs.gov/xlibrary/assets/ice_border_search_electronic_

devices.pdf,      ("ICE     Directive")         as    superseded     in    part    by

Immigration and Customs Enforcement Broadcast: Legal Update --

Border Search of Electronic Devices (2018) ("ICE Broadcast"),

(together "ICE Policy" and, together with the CBP Policy, the

"Policies").      The ICE Policy governs ICE's searches of electronic

devices    at    the    border    "to   ensure       compliance     with   customs,

immigration, and other laws enforced by ICE."                 ICE Directive at 1.

The policy defines an "electronic device" as "any item that may

contain information, such as computers, disks, drives, tapes,

mobile phones and other communication devices, cameras, music

players,   and    any     other   electronic         or   digital   devices."     ICE

Directive at 2. The policy allows for suspicionless basic searches

but states that as of May 11, 2018, ICE agents "should no longer

perform advanced border searches of electronic devices without


                                        - 7 -
reasonable suspicion."      ICE Broadcast.         The ICE Policy also allows

agents to detain electronic devices for a "reasonable time given

the facts and circumstances of the particular search."                           ICE

Directive at 4.

            Plaintiffs     do     not    argue   there   are      any    meaningful

differences between the two agencies' policies.

B. The Searches of Plaintiffs' Electronic Devices

            Plaintiffs     are     ten    U.S.    citizens     and      one   lawful

permanent resident.      Each states that CBP or ICE officers searched

his or her electronic devices on one or more occasion.

            Only plaintiffs Zainab Merchant and Suhaib Allababidi

allege that they were searched after CBP issued its revised 2018

policy and ICE published its              advanced search         policy.      These

searches were basic searches.            These two plaintiffs do not allege

that   their   devices    were     retained      pursuant    to    the    Policies.

Accordingly, no factual information has been presented to us as to

any detention under these policies.

                          II. Procedural History

            Plaintiffs filed suit on September 13, 2017 -- before

the effective date of the challenged Policies -- alleging that CBP

and ICE violated the Fourth and First Amendments by performing

various types of searches of electronic devices without warrants

and    violated   the    Fourth    Amendment      by   retaining        plaintiffs'




                                        - 8 -
electronic devices for an extended period absent probable cause.4

The plaintiffs sought declaratory and injunctive relief, including

expungement of "all information gathered from, or copies made of,

the contents of Plaintiffs' electronic devices."

           On   May   9,   2018,   the     district   court   denied   the

government's motion to dismiss.       Alasaad, 2018 WL 2170323 at *24.

           After discovery, the parties filed cross-motions for

summary judgment.     The district court granted in part and denied

in part plaintiffs' motion for summary judgment and denied the

government's motion for summary judgment.         Alasaad, 419 F. Supp.

3d at 174.      The district court also held that plaintiffs had

standing to seek declaratory and injunctive relief as well as

expungement of their data from CBP and ICE databases.         Id. at 151-

54.5

           As to the merits of the Fourth Amendment challenges, the

district court first held that basic and advanced searches are




       4  No plaintiff in this case asserts that his or her
electronic device passcodes or passwords were entitled to
additional constitutional protections.
          A petition for a writ of certiorari is pending before
the Supreme Court in Andrews v. New Jersey as to whether the Fifth
Amendment protects an individual from being compelled to disclose
the passcodes to his or her electronic devices when doing so may
expose the individual to criminal prosecution. Petition for Writ
of Certiorari, Andrews v. New Jersey, (No. 20-937).
       5  The government does not challenge plaintiffs' standing
on appeal.


                                   - 9 -
both "non-routine" searches, and thus that both types of searches

required reasonable suspicion.6    Id. at 163, 165.     The court

concluded that the basic search component of the Policies violated

the Fourth Amendment.   Id. at 165, 168.

          As to the scope of both basic and advanced searches

permitted under the Policies, the court found two constitutional

violations.   It reasoned that because the border search exception

is premised on the government's paramount interest in "stopping

contraband at the border," "the reasonable suspicion that is

required . . . is . . . that the electronic devices contain[]

contraband [itself]," rather than (a) evidence of contraband or

(b) evidence or information regarding other crimes enforced at the

border.   Id. at 166.   Thus, the Policies were unconstitutional

because they did not restrict agents to searches for contraband

contained in the devices themselves and allowed border searches as

to evidence of all crimes CBP or ICE are authorized to enforce.7

CBP Policy at 1, 5; ICE Directive at 1, 2.


     6    The district court noted that a "cursory search of an
electronic device -- e.g., a brief look reserved to determining
whether a device is owned by the person carrying it across the
border, confirming that it is operational and that it contains
data . . . [would] not require a heightened showing of cause."
Alasaad, 419 F. Supp. 3d at 163.
     7    ICE and CBP are authorized to enforce a broad spectrum
of laws.    See, e.g., 6 U.S.C. § 211(c)(5) (requiring CBP to
"detect, respond to, and interdict terrorists, drug smugglers and
traffickers, human smugglers and traffickers, and other persons
who may undermine the security of the United States"); id.
§ 211(c)(11) (requiring CBP to "enforce and administer the laws


                              - 10 -
           As to the long-term detention of plaintiffs' electronic

devices, the district court held that devices detained based on

reasonable suspicion could be retained only for a "reasonable

period that allows for an investigatory search for contraband."

Alasaad, 419 F. Supp. 3d at 170.

           The district court granted declaratory relief stating

that

           the CBP and ICE policies for "basic" and
           "advanced" searches . . . violate the Fourth
           Amendment to the extent that the policies do
           not require reasonable suspicion that the
           devices contain contraband for both such
           classes of non-cursory searches and/or seizure
           of electronic devices; and that the non-
           cursory    searches   and/or    seizures    of
           Plaintiffs' electronic devices, without such
           reasonable suspicion, violated the Fourth
           Amendment.

Id. at 173.

           The district court declined to grant broad injunctive

relief based on its finding of constitutional violations.   Id. at

174.   It did enjoin the government from searching or detaining any

of plaintiffs' electronic devices at the border absent "reasonable

suspicion that the device contains contraband," and from detaining




relating to agricultural import"); 31 U.S.C. §§ 5316-17
(authorizing warrantless border searches to enforce limitations on
transferring $10,000 or more out of the United States); 19 C.F.R.
§ 12.39 (authorizing CBP to enforce law restricting the importation
of "articles involving unfair methods of competition").


                               - 11 -
plaintiffs'    electronic    devices    for   "longer   than   a   reasonable

period."

            The   district   court     denied   plaintiffs'    request   for

expungement.      Id. at 171-73.

            As to the First Amendment claim, the district court did

not analyze that claim independently from the Fourth Amendment

claim.     It denied plaintiffs' claim for relief, saying "to the

extent that [the First Amendment claim] seeks some further ruling

or relief based upon Plaintiffs' invocation of First Amendment

rights, not otherwise granted as to [plaintiffs' Fourth Amendment

claim]," it would deny plaintiffs' motion for summary judgment.

Id. at 170.

            The government filed a timely notice of appeal, and

plaintiffs cross-appealed.

                              III. Analysis

            We review a grant of summary judgment de novo. Henderson

v. Mass. Bay Transp. Auth., 977 F.3d 20, 29 (1st Cir. 2020).

"Cross-motions for summary judgement do not alter the basic . . .

standard, but rather simply require us to determine whether either

of the parties deserves judgment as a matter of law on facts that

are not disputed."      Adria Int'l. Grp., Inc. v. Ferre Dev., Inc.,

241 F.3d 103, 107 (1st Cir. 2001).

            We begin with plaintiffs' Fourth Amendment claims before

moving to their First Amendment claim and request for expungement.


                                   - 12 -
A. The Level of Suspicion            Required     for      Border    Searches   of
Electronic Devices

          Plaintiffs argue that all electronic device searches at

the border require a warrant, or in the alternative that such

searches require reasonable suspicion that the device contains

contraband.     Plaintiffs do not contest that the Policies require

ICE and CBP to have reasonable suspicion to perform an advanced

border search.       We address the arguments in turn.

1. Border Searches of Electronic Devices Do Not Require a Warrant

          The Fourth Amendment forbids "unreasonable searches and

seizures."    U.S. Const. amend. IV.          "In the absence of a warrant,

a search is reasonable only if it falls within a specific exception

to the warrant requirement."         Riley v. California, 573 U.S. 373,

382 (2014).    Otherwise,

          [a]bsent more precise guidance from the
          founding era, we generally determine whether
          to exempt a given type of search from the
          warrant requirement "by assessing, on the one
          hand, the degree to which it intrudes upon an
          individual's privacy and, on the other, the
          degree to which it is needed for the promotion
          of legitimate governmental interests."

Id. at 385 (quoting Wyoming v. Houghton, 526 U.S. 295, 300 (1999)).

          One     such     exception     to     the     warrant      requirement,

recognized    from    early   in   our   history,     is    the     border   search

exception.    See Boyd v. United States, 116 U.S. 616, 623 (1886);

Carroll v. United States, 267 U.S. 132, 153-54 (1925).                          The

exception is grounded in the government's "inherent authority to


                                    - 13 -
protect, and a paramount interest in protecting, its territorial

integrity."   United States v. Flores-Montano, 541 U.S. 149, 153

(2004).   Further, "the expectation of privacy [is] less at the

border than in the interior . . . [and] the Fourth Amendment

balance between the interests of the Government and the privacy

right of the individual is also struck much more favorably to the

Government at the border."    United States v. Montoya de Hernandez,

473 U.S. 531, 539-40 (1985).

          Plaintiffs rely on Riley v. California to argue that the

border search warrant exception does not encompass the search of

electronic devices because such searches do little to advance the

underlying purposes of the border search exception -- which they

say are limited to interdicting contraband and preventing the entry

of inadmissible persons.8

          This   argument    rests   on   a   misapprehension   of   the

applicability here of the Supreme Court's holding in Riley.          In

Riley, the Supreme Court held that the search incident to arrest

exception to the warrant requirement did not extend to searches of

cellphones.   573 U.S. at 403.       In doing so, it reasoned that

individuals have a heightened privacy interest in their electronic

devices due to the vast quantity of data that may be stored on



     8    For reasons articulated later in this opinion, we reject
plaintiffs' narrow view of the purposes of the border search
exception.


                                - 14 -
such devices, and that the government's interest in searching an

arrestee's cellphone during an arrest was limited because such

searches do not meaningfully advance the search incident to arrest

exception's purposes of protecting officers and preventing the

destruction of evidence.    Id.    at 386, 388-91.       Thus, the balance

of interests did not support extending the search incident to

arrest exception.    Id. at 386.

          Contrary   to   plaintiffs'      assertions,    Riley   does   not

command a warrant requirement for border searches of electronic

devices nor does the logic behind Riley compel us to impose one.

As recently explained by this circuit, Riley "d[id] not either

create or suggest a categorical rule to the effect that the

government must always secure a warrant before accessing the

contents of [an electronic device]."          United States v. Rivera-

Morales, 961 F.3d 1, 14 (1st Cir. 2020).         Nor does Riley by its

own terms apply to border searches, which are entirely separate

from the search incident to arrest searches discussed in Riley.

The search incident to arrest warrant exception is premised on

protecting officers and preventing evidence destruction, rather

than on addressing border crime.      Riley, 573 U.S. at 384-86.

          Further, given the volume of travelers passing through

our nation's borders, warrantless electronic device searches are

essential to the border search exception's purpose of ensuring

that the executive branch can adequately protect the border.             See


                                  - 15 -
Montoya   de   Hernandez,   473    U.S.   at   544    (stating   that   border

officials are "charged . . . with protecting this Nation from

entrants who may bring anything harmful into this country").                A

warrant requirement -- and the delays it would incur -- would

hamstring the agencies' efforts to prevent border-related crime

and protect this country from national security threats.

           Every circuit that has faced this question has agreed

that Riley does not mandate a warrant requirement for border

searches of electronic devices, whether basic or advanced.                The

Eleventh Circuit held that "[b]order searches have long been

excepted from warrant and probable cause requirements, and the

holding of Riley does not change this rule."            Vergara, 884 F.3d at

1312-13. The Fourth Circuit held after Riley that "law enforcement

officers may conduct a warrantless forensic search of a cell phone

under the border search exception where the officers possess

sufficient     individualized     suspicion    of    transnational   criminal

activity."     United States v. Aigbekaen, 943 F.3d 713, 719 n.4 (4th

Cir. 2019).9    The Ninth Circuit, noting that even "post-Riley, no

court has required more than reasonable suspicion to justify even

an intrusive border search," held that both basic and advanced




     9    The Fourth Circuit did not decide whether an advanced
search must be supported by probable cause. Aigbekaen, 943 F.3d
at 720 & n.5.


                                   - 16 -
border searches may be performed without a warrant or probable

cause.   Cano, 934 F.3d at 1015-16.

            We too hold that neither a warrant nor probable cause is

required for a border search of electronic devices.

2. Basic Searches May Be Performed Without Reasonable Suspicion

            Agents may perform "routine" searches at the border

without reasonable suspicion.    Montoya de Hernandez, 473 U.S. at

538, 541. Under this circuit's law, certain "non-routine" searches

must be grounded on reasonable suspicion. United States v. Molina-

Gómez, 781 F.3d 13, 19 (1st Cir. 2015); United States v. Braks,

842 F.2d 509, 513-14 (1st Cir. 1988).    Whether a border search is

routine or non-routine depends on an assessment of the facts of

the case.    Braks, 842 F.2d at 512 (holding that request to female

at border to lift skirt was routine search); Molina-Gómez, 781

F.3d at 19 (holding that the search of a laptop and PlayStation,

whether routine or non-routine, was justified because reasonable

suspicion existed); United States v. Robles, 45 F.3d 1, 5 (1st

Cir. 1995) (holding, where the government conceded that drilling

into metal cylinder was non-routine search, that the search was

justified by reasonable suspicion).      Subjecting individuals to

strip searches or body-cavity searches are examples of non-routine

searches.    Molina-Gómez, 781 F.3d at 19.

            Plaintiffs argue that because electronic devices may

contain a trove of sensitive personal information, basic border


                                - 17 -
searches of electronic devices are non-routine searches requiring

at least reasonable suspicion.                While, as noted above, Riley's

warrant requirement in the search incident to arrest context does

not    extend   to    border    searches,      Riley    recognized    that   modern

electronic devices "implicate privacy concerns far beyond those

implicated by the search of a cigarette pack, a wallet, or a purse"

and "differ in both a quantitative and qualitative sense from other

objects that might be kept on [a traveler’s] person."                 573 U.S. at

393.    These privacy concerns, however significant or novel, are

nevertheless tempered by the fact that the searches are taking

place at the border, where the "Government’s interest in preventing

the entry of unwanted persons and effects is at its zenith,"

Flores-Montano, 541 U.S. at 152, and the "Fourth Amendment balance

of    interests      leans    heavily    to    the     Government,"   Montoya    de

Hernandez, 473 U.S. at 544.          Electronic device searches do not fit

neatly into other categories of property searches, but the bottom

line is that basic border searches of electronic devices do not

involve an intrusive search of a person, like the search the

Supreme Court held to be non-routine in Montoya de Hernandez.                   473

U.S. at 541 & n.4.           Basic border searches also require an officer

to manually traverse the contents of the traveler's electronic

device, limiting in practice the quantity of information available

during a basic search.            The CBP Policy only allows searches of

data resident on the device.            CBP Policy at 4.      And a basic border


                                        - 18 -
search does not allow government officials to view deleted or

encrypted files.10

          We thus agree with the holdings of the Ninth and Eleventh

circuits that basic border searches are routine searches and need

not be supported by reasonable suspicion.     Cano, 934 F.3d at 1016;

Touset, 890 F.3d at 1233; see also United States v. Kolsuz, 890

F.3d 133, 146 n.5 (4th Cir. 2018) (stating that United States v.

Ickes, 393 F.3d 501 (4th Cir. 2005) "treated a [basic] search of

a computer as a routine border search, requiring no individualized

suspicion for the search").

B. The Scope   of    Searches   Permitted   under   the   Border   Search
Exception

          Plaintiffs next argue that border searches of electronic

devices "must be limited to searches for contraband."               This

argument is premised on plaintiffs' assertions that the border

search exception (a) extends only to searches aimed at preventing

the importation of contraband or entry of inadmissible persons

and (b) covers only searches for contraband itself, rather than




     10   Plaintiffs argue that because a basic border search can
take place over an extended period, "the policies place no limit
on the scope of a basic search." This claim is not supported by
the record.   As laid out in the complaint, basic searches are
limited to "allocated space physically resident on an electronic
device that is accessible using the native operating system of the
device."   And the agencies must process the entry of over one
million travelers per day, further restricting the practical
limits of a basic search.


                                - 19 -
for evidence of border-related crimes or contraband.    The argument

fails and its premises are incorrect.

          In non-border contexts the Supreme Court has held that

warrantless searches "must be limited in scope to that which is

justified by the particular purposes served by the exception."

Florida v. Royer, 460 U.S. 491, 500 (1983) (plurality opinion);

see also Riley, 573 U.S. at 386.    Riley did not purport to extend

this rule to the border search context.      Even assuming arguendo

that the analysis used in Riley applies here, such an analysis

would only require that warrantless border searches be tethered to

"the longstanding right of the sovereign to protect itself by

stopping and examining persons and property crossing into this

country."11   Flores-Montano, 541 U.S. at 152 (quoting United States

v. Ramsey, 431 U.S. 606, 616 (1977)).    Further, the Supreme Court

has repeatedly said that routine searches "are reasonable simply

by virtue of the fact that they occur at the border."    Id. at 152-

53 (quoting Ramsey, 431 U.S. at 616).       This is so because the

government's interest in preventing crime at international borders

"is at its zenith," see id., and it follows that a search for

evidence of either contraband or a cross-border crime furthers the

purposes of the border search exception to the warrant requirement.



     11   Plaintiffs do not challenge any specific law enforced by
CBP or ICE as having no relationship to the border search
exception's broad purposes.


                               - 20 -
           As for advanced searches, we cannot reasonably conclude

that the "substantive limitations imposed by the Constitution" on

the border search exception prevent Congress from giving border

agencies authority to search for information or items other than

contraband.   Ramsey, 431 U.S. at 620; see also Kolsuz, 890 F.3d at

152 (Wilkinson, J., concurring in the judgment) ("[T]here is a

longstanding historical practice in border searches of deferring

to the legislative and executive branches.").             To the contrary,

Montoya de Hernandez makes clear that the border search exception's

purpose is not limited to interdicting contraband; it serves to

bar entry to those "who may bring anything harmful into this

country" and then gives as examples "whether that be communicable

diseases, narcotics, or explosives."      473 U.S. at 544.

           Congress   is   better   situated   than   the    judiciary    to

identify the harms that threaten us at the border.12           Kolsuz, 890

F.3d at 152 (Wilkinson, J, concurring in the judgment) ("[Riley

does not] begin to answer the question of who should strike the

balance   between   privacy   and   security   at   the    border   of   the



     12   As explained by Judge Wilkinson, "[w]e have no idea of
the dangers we are courting" at the border. Kolsuz, 890 F.3d at
152 (Wilkinson, J., concurring in the judgment).    He notes the
risk that "[p]orous borders are uniquely tempting to those intent
upon inflicting the vivid horrors of mass casualties" and "the
danger of highly classified technical information being smuggled
out of this country only to go into the hands of foreign nations
who do not wish us well and who seek to build their armaments to
an ever more perilous state." Id.


                                - 21 -
country."); see also Riley, 573 U.S. at 408 (Alito, J., concurring

in part and concurring in the judgment) (stating with respect to

the reasonableness of warrantless searches of mobile phones that

"[l]egislatures . . . are in a better position than we are to

assess and respond to the changes that have already occurred and

those that almost certainly will take place in the future").                In

weighing the competing policy considerations, Congress or the

Executive may choose to strike a different balance as to border

searches of electronic devices and may choose to grant greater

protection than required by the Constitution.

            As   to   plaintiffs'     distinction    between   evidence     of

contraband and contraband itself, the border search exception is

not limited to searches for contraband itself rather than evidence

of contraband or a border-related crime.            Searching for evidence

is vital to achieving the border search exception's purposes of

controlling "who and what may enter the country."               Ramsey, 431

U.S. at 620; see also Aigbekaen, 943 F.3d at 721 (holding that the

purposes of the border search exception are "protecting national

security,   collecting    duties,     blocking   the   entry   of     unwanted

persons, [and] disrupting efforts to export or import contraband"

(emphasis added)); United States v. Gurr, 471 F.3d 144, 149 (D.C.

Cir. 2006) (holding in the context of the border search exception

that   "[t]he    distinction   that    [plaintiff]     would   draw    between




                                    - 22 -
contraband and documentary evidence of a crime is without legal

basis").13

             We acknowledge that our holdings on both of these points

are contrary to the Ninth Circuit's holdings in United States v.

Cano. 934 F.3d at 1018 (holding that the border search exception

"is restricted in scope to searches for contraband").           We cannot

agree with its narrow view of the border search exception because

Cano fails to appreciate the full range of justifications for the

border search exception beyond the prevention of contraband itself

entering the country.        Advanced border searches of electronic

devices   may   be   used   to   search   for   contraband,   evidence   of

contraband, or for evidence of activity in violation of the laws

enforced or administered by CBP or ICE.




     13   Plaintiffs cite Boyd, 116 U.S. 616, for the proposition
that the border search exception does not extend to searching for
evidence of border-related crimes. But the Supreme Court rejected
in Warden, Md. Penitentiary v. Hayden the distinction articulated
in Boyd between searches for "mere evidence" and searches for
"instrumentalities, fruits of crime, or contraband."       387 U.S.
294, 301 (1967). Plaintiffs argue that Hayden only rejected this
distinction in relation to searches authorized by a warrant rather
than warrantless searches, but we conclude that Hayden should be
more broadly applied. See United States v. Molina-Isidoro, 884
F.3d 287, 297 n.7 (5th Cir. 2018) (Costa, J., specially concurring)
("Hayden is viewed as a broad rejection of the 'mere
evidence'/instrumentality distinction" (citing Wayne LaFave,
Search & Seizure, A Treatise on the Fourth Amendment § 4.1(c))).
But see id. ("[T]here are reasons to believe the [mere
evidence/instrumentality] distinction still matters when it comes
to border searches.").


                                   - 23 -
C. Device Detention

            Plaintiffs further argue that the CBP and ICE Policies

violate    the    Fourth    Amendment       because    they    do   not   impose   an

"effective       limit     on     [the]    duration"      of   electronic    device

detentions.14     Plaintiffs' argument is in the abstract as they have

not presented any facts concerning the actual retention of devices

pursuant to the policies at issue.

            The CBP Policy permits an officer to "detain electronic

devices or copies of information contained therein, for a brief,

reasonable period of time to perform a thorough border search."

CBP Policy at 7.           Supervisory approval is required to detain

devices after the device owners "departure from the port or other

location of detention."           Id.     The ICE Policy permits the detention

of "electronic devices, or copies of information therefrom [for]

a   reasonable     time    given     the    facts   and    circumstances     of    the

particular search."             ICE Directive at 4.        Both Policies require

supervisory approval to extend a device detention beyond an initial

span of time -- five days under the CBP Policy and thirty days

under the ICE policy.            CBP Policy at 7; ICE Directive at 5.




      14  Because we conclude that no reasonable suspicion is
required for a basic border search of an electronic device, we
need not reach plaintiffs' contention that the Policies are
deficient in allowing the agencies to detain devices without
reasonable suspicion.


                                          - 24 -
             The nature of plaintiffs' challenge is unclear.                The

Policies permit detention for only a reasonable period, which is

the constitutional test.        See Montoya de Hernandez, 473 U.S. at

544.    If the argument is that "reasonable" must be replaced with

hard time limits, the Supreme Court has rejected that proposition.

Id.    at   543.   If    the   argument   is   that   the   judgment   as   to

reasonableness should not be left in the first instance to the

agent who conducts the search, that misreads the Policies.                  The

CBP Policy requires a supervisor's permission to detain a device

after its owner leaves the border, a higher level of supervisory

approval to extend a detention for longer than five days, and a

third level of approval to extend a detention beyond fifteen days.

CBP Policy at 7.        What is reasonable is surely fact specific and

future as applied attacks are not foreclosed should there be

abuses.15

D. First Amendment

             Plaintiffs next argue that under the First Amendment,

government searches of electronic devices at the border require a

warrant, or at least reasonable suspicion.              They contend that

because electronic devices may contain sensitive personal data,

the threat of warrantless or suspicionless border searches will


       15 Plaintiffs do not develop the argument that any
individual detention of any plaintiff's electronic device was
unreasonable, but instead say that several particularly long
detentions demonstrate that the Policies are facially deficient.


                                   - 25 -
impermissibly   chill   speech.16    They   further   argue   that   such

searches unduly interfere with the First Amendment freedoms to

"'engage in association' . . . without government scrutiny, . . .

speak anonymously, . . . receive unpopular ideas, confidentially

and without government scrutiny, . . . read books and watch movies

privately . . . [and] gather and publish newsworthy information

absent government scrutiny."

           Because   plaintiffs     seek    relief    "beyond   [their]

particular circumstances," "they must 'satisfy [the] standards for

a facial challenge to the extent of that reach.'"        Proj. Veritas

Action Fund v. Rollins, 982 F.3d 813, 826 (1st Cir. 2020) (emphasis

omitted) (quoting John Doe No. 1 v. Reed, 561 U.S. 186, 194

(2010)).   Thus, plaintiffs must show that "a substantial number of

[the ICE and CBP Policies'] applications are unconstitutional,




     16   Plaintiffs purport to rely on United States v. Ramsey,
431 U.S. 606 (1977), but misunderstand the case.       In Ramsey,
plaintiffs argued that the search of international mail was a
violation of the First Amendment. The applicable law allowed the
search of international mail only where there was "'reasonable
cause to believe' that customs laws [were] being violated prior to
the opening of envelopes" and a regulation forbade the "reading of
correspondence absent a search warrant."     Id. at 623 (emphasis
added). The Supreme Court held that under those circumstances,
the opening of international mail did not "impermissibly chill[]
the exercise of free speech." Id. at 624.

          The court explicitly reserved and did not decide the
question of whether the search of international mail, "in the
absence of the regulatory restrictions" would chill speech and, if
it did, "whether the appropriate response would be to apply the
full panoply of Fourth Amendment requirements." Id. at 624 n.18.


                                - 26 -
judged in relation to the statute's plainly legitimate sweep."

United States v. Stevens, 559 U.S. 460, 473 (2010) (quoting Wash.

State Grange v. Wash. State Republican Party, 552 U.S. 442, 449 n.6

(2008)).

           The First Amendment provides protections -- independent

of the Fourth Amendment -- against the compelled disclosure of

expressive information.    See Buckley v. Valeo, 424 U.S. 1, 64

(1976); Tabbaa v. Chertoff, 509 F.3d 89, 102 n.4 (2d Cir. 2007)

(analyzing First Amendment challenge to targeted border searches

independently of Fourth Amendment); Ramsey, 431 U.S. at 623-24.

Neither this circuit nor the Supreme Court has specified the

appropriate standard to assess alleged government intrusions on

First Amendment rights at the border.     See Ramsey, 431 U.S. at

623-24 (refusing to "consider the constitutional reach of the First

Amendment in this area"); see also Tabbaa, 509 F.3d at 102 n.5

("It may also be true that the First Amendment's balance of

interests is qualitatively different where, as here, the action

being challenged is the government's attempt to exercise its broad

authority to control who and what enters the country.").

           Under any standard plaintiffs have not shown that the

content-neutral border search Policies facially violate the First

Amendment.   See Ramsey, 431 U.S. at 623 ("More fundamentally,

however, the existing system of border searches has not been shown

to invade protected First Amendment rights, and hence there is no


                              - 27 -
reason to think that the potential presence of correspondence makes

the otherwise constitutionally reasonable search 'unreasonable.'"

(footnote omitted)).      The Policies have a plainly legitimate sweep

and serve the government's paramount interests in protecting the

border.17

            Nor,   as   plaintiffs   contend,   does   the   presence   of

expressive material on electronic devices "trigger[] a warrant

requirement."      A    higher level of suspicion is not generally

required to search potentially expressive materials.         See New York

v. P.J. Video, Inc., 475 U.S. 868, 875 (1986); United States v.

Brunette, 256 F.3d 14, 16 (1st Cir. 2001) (holding the probable

cause standard "is no different where First Amendment concerns may

be at issue"); see also Ickes, 393 F.3d at 507 (refusing to apply

a different standard to border searches of expressive material);

United States v. Arnold, 533 F.3d 1003, 1010 (9th Cir. 2008)

(same).

            As explained by the Ninth Circuit in Arnold, providing

a different standard for "expressive material" at the border would


     17   Plaintiffs do not present the issue of whether the First
Amendment would require a different outcome if CBP and ICE were
targeting journalists or using border searches to pierce attorney-
client privilege. Two plaintiffs are journalists, but they do not
contend that they were searched by CBP for this reason.        See
Alasaad, 419 F. Supp. 3d at 169. This decision does not foreclose
a future as      applied First Amendment challenge in such
circumstances. See Ortiz-Graulau v. United States, 756 F.3d 12,
21 (1st Cir. 2014) (noting that this court may leave open "the
possibility of a future as-applied challenge").


                                 - 28 -
           (1) protect terrorist communications "which
           are inherently 'expressive'"; (2) create an
           unworkable standard for government agents who
           "would have to decide -- on their feet -- which
           expressive material is covered by the First
           Amendment"; and (3) contravene the weight of
           Supreme Court precedent refusing to subject
           government action to greater scrutiny with
           respect to the Fourth Amendment when an
           alleged First Amendment interest is also at
           stake.

533 F.3d at 1010 (quoting Ickes, 393 F.3d at 506).      Plaintiffs'

First Amendment challenge fails.

E. Expungement

           Plaintiffs argue they are entitled to expungement of any

data obtained in violation of the Constitution.        The district

court's refusal to grant the equitable remedy of expungement is

reviewed only for abuse of discretion.      Reyes v. DEA, 834 F.2d

1093, 1098-99 (1st Cir. 1987).

           There was no abuse of discretion here.      The district

court adequately justified its conclusions that expungement was

not warranted.   And contrary to plaintiffs' assertions, it was not

error for the district court to analogize to caselaw regarding the

suppression of evidence.

                           IV. Conclusion

           We affirm in part, reverse in part, vacate in part, and

remand for the entry of a revised judgment consistent with this

opinion.   No costs imposed.




                               - 29 -

```

---

## GROUP: _overhaul2/lake/cases/Barnes v. Felix.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Barnes v. Felix"
type: case
citation: "605 U.S. 73 (2025)"
parallel_cite: ""
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2025
date_decided: 2025-05-15
docket: 23-1239
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2025-05-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Barnes v. Felix
  varies_by_point: false
  scope_note: "Good law (2025, unanimous): excessive-force reasonableness is judged on the totality of the circumstances with no 'moment of threat' time limit. Slip opinion subject to formal revision."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10776852/barnes-v-felix/"
  cluster_id: 10776852
  opinion_id: 11243439
  identity_checked: true
homes:
  - page: "[[Use of Force]]"
    role: "Key — Progeny / Refinement"
related: ["[[Graham v. Connor]]", "[[Tennessee v. Garner]]", "[[Plumhoff v. Rickard]]"]
aliases: []
tags: ["case", "use-of-force", "deadly-force", "totality-of-circumstances", "moment-of-threat", "section-1983"]
holding: "Excessive-force reasonableness under the Fourth Amendment is judged on the totality of the circumstances, which has no time limit; the 'moment of threat' rule that ignores the events leading up to the use of force is rejected."
lake:
  record_id: Barnes v. Felix
  status: verified
  projected_at: 2026-07-06
---

# Barnes v. Felix

*605 U.S. 73 (2025)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officer Roberto Felix, Jr. pulled over Ashtian Barnes near Houston for outstanding toll violations. After questioning at the window, Felix ordered Barnes out of the car; Barnes instead turned the ignition back on, and as the car began to move, Felix jumped onto the doorsill and — with no visibility into the car — fired two shots inside, fatally wounding Barnes. About five seconds elapsed from when the car started moving to when it stopped; only two seconds passed between Felix stepping onto the doorsill and his first shot. Barnes's mother sued under § 1983 for excessive force. Applying the Fifth Circuit's "moment-of-threat" rule, the district court and Fifth Circuit looked only at the two seconds before the shooting and granted Felix summary judgment.

## Issue
Whether a court evaluating an excessive-force claim may apply a "moment-of-threat" rule that confines the inquiry to the circumstances at the precise instant force was used, ignoring the events leading up to it.

## Rule
No — the inquiry is the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], with no time limit. "Today, we reject that approach as improperly narrowing the requisite Fourth Amendment analysis. To assess whether an officer acted reasonably in using force, a court must consider all the relevant circumstances, including facts and events leading up to the climactic moment." — 605 U.S. 73 (slip op., at 1). ^pin-73

The *[[Graham v. Connor]]* reasonableness test, assessed from the perspective of a reasonable officer on the scene, requires looking at the whole encounter: "A court deciding a use-of-force case cannot review the totality of the circumstances if it has put on chronological blinders." — *Id.* (slip op., at 7). ^pin-73b

## Application
By limiting their view to the two seconds when Felix clung to the moving car, the lower courts could not consider the reasons for the stop or the earlier interactions — including Felix's own decision to jump onto the doorsill — and so could not assess whether those final two seconds would look different within a longer timeframe. As *[[Plumhoff v. Rickard]]* illustrates, earlier events may show why a reasonable officer would perceive later conduct as threatening (or not). Because the Fifth Circuit's rule precluded that context, the Court [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]] for analysis under the full [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]. The Court expressly did not decide whether Felix's use of force was reasonable, nor whether or how an officer's own "creation of a dangerous situation" factors in.

## Conclusion
[[Reading and Citing Cases#vacated|Vacated]] and [[Reading and Citing Cases#on-remand|remanded]] (unanimous). Excessive-force reasonableness must be assessed on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], including the events leading up to the use of force; the "moment-of-threat" rule is incompatible with that standard.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- A 2025 decision applying [[Graham v. Connor]] and [[Tennessee v. Garner]]; it confirms the totality approach already reflected in [[Plumhoff v. Rickard]] and abrogates the Fifth Circuit's "moment-of-threat" doctrine. Justice Kavanaugh's [[Common Legal Terms#concurring-opinion|concurrence]] (joined by Thomas, Alito, and Barrett) addressed the dangers of traffic-stop flight; the Court left [[Qualified Immunity|qualified immunity]] and the "officer-created danger" question for another day. No negative treatment.

## Appears on
- [[Use of Force]] — *Key — Progeny / Refinement*
- [[Section 1983 Liability and Qualified Immunity]] — *Related (cross-doctrine)*

## Sources
- *Barnes v. Felix*, 605 U.S. 73 (2025) — https://www.courtlistener.com/opinion/10584846/barnes-v-felix/ — pinpoints: slip op., at 1, 7 (CL stores the slip opinion "605 U. S. ____ (2025)," subject to formal revision; pins keyed to the official case-start page 73).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5a07a5ee4209c02f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Barnes v. Felix"}, "payload": {"all": [{"cite": "605 U.S. 73", "page": "73", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "605"}], "display": "605 U.S. 73", "official": {"cite": "605 U.S. 73", "page": "73", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "605"}, "official_selection_present": true, "record_id": "Barnes v. Felix"}}
{"assertion_id": "96c441ba7a83030c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-73", "record_id": "Barnes v. Felix"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-73", "pinpoint_status": "slip-only", "quote": "rule that confines the inquiry to the circumstances at the precise instant force was used, ignoring the events leading up to it. ## Rule No — the inquiry is the totality of the circumstances, with no time limit.", "quote_fidelity": "mismatch", "record_id": "Barnes v. Felix", "star_marker": null}}
{"assertion_id": "b00833b82290e9b4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-73b", "record_id": "Barnes v. Felix"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-73b", "pinpoint_status": "slip-only", "quote": "A court deciding a use-of-force case cannot review the totality of the circumstances if it has put on chronological blinders.", "quote_fidelity": "mismatch", "record_id": "Barnes v. Felix", "star_marker": null}}
{"assertion_id": "3e5ae8df7456f9db", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Barnes v. Felix"}, "payload": {"as_of_content": "2025-05-15", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Barnes v. Felix", "scope_note": "Good law (2025, unanimous): excessive-force reasonableness is judged on the totality of the circumstances with no 'moment of threat' time limit. Slip opinion subject to formal revision.", "varies_by_point": false}}
```

### lake record — Barnes v. Felix

```json
{
  "schema_version": "s2.v1",
  "record_id": "Barnes v. Felix",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Barnes v. Felix",
    "case_name_short": "Barnes",
    "case_name_full": "",
    "input_case_name": "Barnes v. Felix",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2025-05-15",
    "year": 2025,
    "docket": "23-1239",
    "cluster_id": 10776852,
    "lead_opinion_id": 11243439,
    "sibling_ids": [
      11243439
    ],
    "absolute_url": "/opinion/10776852/barnes-v-felix/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 10584846,
        "score": 110,
        "case_name": "Barnes v. Felix"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "605 U.S. 73",
      "volume": "605",
      "reporter": "U.S.",
      "page": "73",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "605 U.S. 73",
        "volume": "605",
        "reporter": "U.S.",
        "page": "73",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "605 U.S. 73",
    "official_selection": {
      "court_class": "scotus",
      "selected": "605 U.S. 73",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-73",
      "page": null,
      "quote": "rule that confines the inquiry to the circumstances at the precise instant force was used, ignoring the events leading up to it. ## Rule No \u2014 the inquiry is the totality of the circumstances, with no time limit.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-73b",
      "page": null,
      "quote": "A court deciding a use-of-force case cannot review the totality of the circumstances if it has put on chronological blinders.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2025-05-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Barnes v. Felix",
    "varies_by_point": false,
    "scope_note": "Good law (2025, unanimous): excessive-force reasonableness is judged on the totality of the circumstances with no 'moment of threat' time limit. Slip opinion subject to formal revision.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(11243439) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 0,
        "triage_read": 0,
        "triage_snippet_classified": 0
      },
      "lane2_top_cited": {
        "query": "cites:(11243439)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(11243439)",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 0,
        "triage_read": 0,
        "triage_snippet_classified": 0
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(11243439)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 11243439,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/barnes-v-felix.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 11243439,
        "cited_id": 508475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243439,
        "cited_id": 2656509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243439,
        "cited_id": 2675750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243439,
        "cited_id": 4172499,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243439,
        "cited_id": 4697833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243439,
        "cited_id": 9425474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243439,
        "cited_id": 9427002,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243439,
        "cited_id": 9429990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243439,
        "cited_id": 9431666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243439,
        "cited_id": 9434949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243439,
        "cited_id": 9435077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243439,
        "cited_id": 9485101,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243439,
        "cited_id": 9485643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243439,
        "cited_id": 9808641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243439,
        "cited_id": 9842054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243439,
        "cited_id": 9926212,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11243439,
        "cited_id": 11051434,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "C",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-04T19:26:45Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T19:27:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T19:27:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:27:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T19:27:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Barnes v. Felix

```
                   PRELIMINARY PRINT

              Volume 605 U. S. Part 1
                               Pages 73–90




       OFFICIAL REPORTS
                                     OF


   THE SUPREME COURT
                                May 15, 2025


Page Proof Pending Publication


                    REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D. C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
                        OCTOBER TERM, 2024                             73

                                Syllabus


BARNES, individually and as representative of the
 ESTATE OF BARNES, DECEASED v. FELIX et al.
certiorari to the united states court of appeals for
                  the fth circuit
     No. 23–1239. Argued January 22, 2025—Decided May 15, 2025
Respondent Roberto Felix, Jr., a law enforcement offcer, pulled over Ash-
 tian Barnes for suspected toll violations. Felix ordered Barnes to exit
 the vehicle, but Barnes began to drive away. As the car began to move
 forward, Felix jumped onto its doorsill and fred two shots inside.
 Barnes was fatally hit but managed to stop the car. About fve seconds
 elapsed between when the car started moving and when it stopped.
 Two seconds passed between the moment Felix stepped on the doorsill
 and the moment he fred his frst shot.
    Barnes's mother sued Felix on Barnes's behalf, alleging that Felix
 violated Barnes's Fourth Amendment right against excessive force.
 The District Court granted summary judgment to Felix, applying the
 Fifth Circuit's “moment-of-threat” rule. The Court of Appeals af-
Page Proof Pending Publication
 frmed, explaining that the moment-of-threat rule requires asking only
 whether an offcer was “in danger at the moment of the threat that
 resulted in [his] use of deadly force.” 91 F. 4th 393, 397. Under the
 rule, events “leading up to the shooting” are “not relevant.” Ibid.
 Here, the “precise moment of the threat” was the “two seconds” when
 Felix was clinging to a moving car. Id., at 397–398. Because Felix
 could then have reasonably believed his life in danger, the panel held,
 the shooting was lawful. Id., at 398.
Held: A claim that a law enforcement offcer used excessive force during
 a stop or arrest is analyzed under the Fourth Amendment, which re-
 quires that the force deployed be objectively reasonable from “the per-
 spective of a reasonable offcer on the scene.” Graham v. Connor, 490
 U. S. 386, 396. The inquiry into the reasonableness of police force re-
 quires analyzing the “totality of the circumstances.” County of Los
 Angeles v. Mendez, 581 U. S. 420, 427–428; Tennessee v. Garner, 471 U. S.
 1, 9. That analysis demands “careful attention to the facts and circum-
 stances” relating to the incident. Graham, 490 U. S., at 396.
    Most notable here, the “totality of the circumstances” inquiry has no
 time limit. While the situation at the precise time of the shooting will
 often matter most, earlier facts and circumstances may bear on how a
 reasonable offcer would have understood and responded to later ones.
 Prior events may show why a reasonable offcer would perceive other-
74                         BARNES v. FELIX

                                 Syllabus

  wise ambiguous conduct as threatening, or instead as innocuous.
  Plumhoff v. Rickard, 572 U. S. 765, well illustrates this point. There,
  an offcer's use of deadly force was justifed “at the moment” partly
  because of what had transpired in the preceding period. Id., at 777.
     The moment-of-threat rule applied below prevents that sort of atten-
  tion to context, and thus conficts with this Court's instruction to ana-
  lyze the totality of the circumstances. By limiting their view to the
  two seconds before the shooting, the lower courts could not take into
  account anything preceding that fnal moment. So, for example, they
  could not consider the reasons for the stop or the earlier interactions
  between the suspect and offcer. And because of that limit, they could
  not address whether the fnal two seconds of the encounter would look
  different if set within a longer timeframe. A rule like that, which pre-
  cludes consideration of prior events in assessing a police shooting, is not
  reconcilable with the fact-dependent and context-sensitive approach this
  Court has prescribed. A court deciding a use-of-force case cannot re-
  view the totality of the circumstances if it has put on chronological
  blinders.
     The Court does not address a separate question about whether or
  how an offcer's own “creation of a dangerous situation” factors into the
  reasonableness analysis. The courts below never confronted that issue,
Page Proof Pending Publication
  and it was not the basis of the petition for certiorari. Pp. 79–84.
91 F. 4th 393, vacated and remanded.

   Kagan, J., delivered the opinion for a unanimous Court. Kavanaugh,
J., fled a concurring opinion, in which Thomas, Alito, and Barrett, JJ.,
joined, post, p. 84.

  Nathaniel A. G. Zelinsky argued the cause for petitioner.
With him on the briefs were Katherine B. Wellington, Neal
Kumar Katyal, and Adam W. Fomby.
  Zoe A. Jacoby argued the cause for the United States as
amicus curiae supporting vacatur and remand. With her
on the brief were Solicitor General Prelogar, Assistant At-
torney General Clarke, Principal Deputy Assistant Attor-
neys General Argentieri and Boynton, Deputy Solicitor
General Feigin, Thomas Booth, and Teresa Kwong.
  Charles L. McCloud argued the cause for respondents.
With him on the brief were Lisa S. Blatt, Peter S. Jorgensen,
                       Cite as: 605 U. S. 73 (2025)                     75

                                 Counsel

Erin M. Sielaff, and Judith Ramsey Saldana. Lanora C.
Pettit, Principal Deputy Solicitor General of Texas, argued
the cause for Texas et al. as amici curiae supporting re-
spondent Felix.*

   *Briefs of amici curiae urging reversal were fled for the Cato Institute
et al. by Clark M. Neily III, Matthew P. Cavedon, and Michael Z. Fox;
for the Constitutional Accountability Center by Elizabeth B. Wydra, Bri-
anne J. Gorod, David H. Gans, and Brian R. Frazelle; for Current and
Former Law Enforcement Officials by Elizabeth C. Rinehart, Barry
Friedman, Aaron Scherzer, and Josh Parker; for the Due Process Insti-
tute et al. by Douglas E. Litvack and Shana-Tara O'Toole; for the Giffords
Law Center to Prevent Gun Violence et al. by Maureen P. Alger, Emily
J. Born, Douglas N. Letter, Shira Lauren Feldman, Kristen A. Johnson,
Amanda Liverzani, Esther Sanchez-Gomez, and Leigh Rome; for the In-
stitute for American Policing Reform by Chantale Fiebig, Joshua M.
Wesneski, Stephanie Adamakos, and Steven Reiss; for the National Police
Accountability Project by Dana E. Foster; for the National Urban League
et al. by Rachel A. Chung, Janai S. Nelson, Kevin E. Jason, Jin Hee Lee,
and Melissa C. Cassel; for The Rutherford Institute by Angela M. Liu,
Page Proof Pending Publication
John W. Whitehead, and Christopher J. Merken; for the Southern Border
Communities Coalition by Delia Addo-Yobo and Roxanna Altholz; for the
Southern Poverty Law Center by Arthur Ago and Krista A. Dolan; and
for the Texas Civil Rights Project by Daniel N. Guisbond. Raff Melkon-
ian fled a brief for the Color of Change as amicus curiae urging vacatur.
   Briefs of amici curiae urging affrmance were fled for the State of
Texas et al. by Ken Paxton, Attorney General of Texas, Brent Webster,
First Assistant Attorney General, Aaron L. Nielson, Solicitor General,
Lanora C. Pettit, Principal Deputy Solicitor General, Kateland R. Jack-
son, Assistant Solicitor General, and Brendan A. Fugere, Assistant Attor-
ney General, and by the Attorneys General for their respective States as
follows: Steve Marshall of Alabama, Tim Griffn of Arkansas, Chris Carr
of Georgia, Theodore E. Rokita of Indiana, Brenna Bird of Iowa, Liz Mur-
rill of Louisiana, Lynn Fitch of Mississippi, Austin Knudsen of Montana,
Michael T. Hilgers of Nebraska, Drew Wrigley of North Dakota, Alan
Wilson of South Carolina, Marty Jackley of South Dakota, Jonathan Skr-
metti of Tennessee, and Jason Miyares of Virginia; for the Los Angeles
County Police Chiefs' Association by J. Scott Tiedemann and David A.
Urban; for the National Fraternal Order of Police by Larry H. James; for
the National Police Association et al. by Jeffrey C. Hendrickson and Rob-
ert S. Lafferrandre; for the Peace Offcers Research Association of Califor-
76                         BARNES v. FELIX

                           Opinion of the Court

     Justice Kagan delivered the opinion of the Court.
  A police offcer's use of deadly force violates the Fourth
Amendment when it is not “objectively reasonable.” Gra-
ham v. Connor, 490 U. S. 386, 397 (1989). And that inquiry
into reasonableness, we have held, requires assessing the
“totality of the circumstances.” Id., at 396 (quoting Tennes-
see v. Garner, 471 U. S. 1, 9 (1985)).
  The question here is whether that framework permits
courts, in evaluating a police shooting (or other use of force),
to apply the so-called moment-of-threat rule used in the
courts below. Under that rule, a court looks only to the cir-
cumstances existing at the precise time an offcer perceived
the threat inducing him to shoot. Today, we reject that
approach as improperly narrowing the requisite Fourth
Amendment analysis. To assess whether an offcer acted
reasonably in using force, a court must consider all the rele-
vant circumstances, including facts and events leading up to
Page Proof Pending Publication
the climactic moment.
                                I
  On the afternoon of April 28, 2016, Roberto Felix, Jr., a
law enforcement offcer patrolling a highway outside Hous-
ton, received a radio alert about an automobile on the road
with outstanding toll violations. Felix soon spotted the car,
a Toyota Corolla, and turned on his emergency lights to initi-
ate a traffc stop. The driver, Ashtian Barnes, pulled over
to the highway's shoulder.

nia et al. by Timothy K. Talbot, Michael A. Morguess, and David E. Mas-
tagni; and for the Texas Municipal League Intergovernmental Risk Pool
et al. by Laura O'Leary and Francisco J. Valenzuela.
   Briefs of amici curiae were fled for the California State Sheriffs' Asso-
ciation et al. by James R. Touchstone and Scott Wm. Davenport; for the
National Sheriffs' Association by Gregory C. Champagne and Maurice E.
Bostick; for Restore the Fourth, Inc., by Mahesha P. Subbaraman; for the
Wisconsin Coalition of Law Enforcement et al. by Remzy D. Bitar; and
for Seth W. Stoughton by J. Carl Cecere.
                   Cite as: 605 U. S. 73 (2025)             77

                      Opinion of the Court

   Parking his own car just behind, Felix walked to the Co-
rolla's driver-side door and asked Barnes for his license and
proof of insurance. Barnes replied that he did not have his
license with him, and that the car was a rental in his girl-
friend's name. As he spoke, Barnes rummaged through
some papers inside the car, causing Felix to tell him several
times to stop “digging around.” Felix also commented that
he smelled marijuana, and asked if there was anything in the
car he should know about. Barnes responded that he might
have some identifcation in the trunk. So Felix told him to
open the trunk from his seat. Barnes did so, while also
turning off the ignition. All that happened (as a dashcam
recording of the incident shows) in less than two minutes.
   Then things began moving even faster. With his right
hand resting on his holster, Felix told Barnes to get out of
the car. Barnes opened the door but did not exit; instead,
he turned the ignition back on. Felix unholstered his gun
Page Proof Pending Publication
and, as the car began to move forward, jumped onto its door-
sill. He twice shouted, “Don't fucking move.” And with no
visibility into the car (because his head was above the roof),
he fred two quick shots inside. Barnes was hit, but man-
aged to stop the car. Felix then radioed for back-up. By
the time it arrived, Barnes was dead. All told, about fve
seconds elapsed between when the car started moving and
when it stopped. And within that period, two seconds
passed between the moment Felix stepped on the doorsill
and the moment he fred his frst shot.
   Barnes's mother, Janice Barnes, sued Felix on her son's
behalf. The suit, brought under 42 U. S. C. § 1983, alleged
that Felix had violated Ashtian Barnes's Fourth Amendment
rights by using excessive force against him.
   The District Court granted summary judgment to Felix.
The court explained that to prevail on her claim, Mrs. Barnes
needed to show that Felix's use of force was “objectively un-
reasonable.” 532 F. Supp. 3d 463, 468 (SD Tex. 2021). In
78                    BARNES v. FELIX

                      Opinion of the Court

the usual excessive-force case, the court noted, the inquiry
into reasonableness would involve considering a variety of
circumstances. See id., at 468–469. But when an offcer
has used deadly force, the court continued, “the Fifth Circuit
has developed a much narrower approach.” Id., at 469.
Then, a court could ask only about the situation existing “at
the moment of the threat” that sparked the fatal shooting.
Ibid. (quoting Rockwell v. Brown, 664 F. 3d 985, 991 (CA5
2011); emphasis in original). The District Court identifed
that moment as “the two seconds before Felix fred his frst
shot,” when he was standing on the doorsill of a moving vehi-
cle. 532 F. Supp. 3d, at 471. At that moment, the court
found, an offcer could reasonably think himself “at risk of
serious harm.” Id., at 472. And under the Fifth Circuit's
rule, that fact alone concluded the analysis. The court ex-
plained that it could not consider “what had transpired up
until” those last two seconds, including Felix's decision to
Page Proof Pending Publication
jump onto the sill. Id., at 471. Although a “more robust
examination” might have aided in assessing the reasonable-
ness of the shooting, the court was “duty bound” by “Circuit
precedent” to “limit[ its] focus” to the “exact moment Felix
was hanging onto Barnes's” moving car. Id., at 472.
   The Court of Appeals affrmed, explaining that it too was
“[b]ound” by “this Circuit's moment of threat doctrine.” 91
F. 4th 393, 394, 397 (2024). Under that rule, the panel
agreed, the “inquiry is confned to whether the offcer[ ]” was
“in danger at the moment of the threat that resulted in [his]
use of deadly force.” Id., at 397. Any prior events “leading
up to the shooting,” including actions the offcer took, were
simply “not relevant.” Ibid. (quoting Harris v. Serpas, 745
F. 3d 767, 772 (CA5 2014)). And here, as the District Court
found, the “precise moment of the threat” was the “two sec-
onds” when Felix was clinging to a moving car. 91 F. 4th,
at 397–398. Because Felix could then have reasonably be-
lieved his life in danger, the panel concluded, his decision to
                   Cite as: 605 U. S. 73 (2025)             79

                      Opinion of the Court

shoot “did not violate Barnes's constitutional rights.” Id.,
at 398.
   In a concurring opinion, Judge Higginbotham (who also
authored the panel opinion) expressed “concern” with the
Fif th Circuit's moment-of-threat doctrine. Ibid. He
thought that rule inconsistent with this Court's directive to
assess the reasonableness of an offcer's use of force, includ-
ing deadly force, by “look[ing] to the totality of circum-
stances.” Id., at 399. Under the totality approach, Judge
Higginbotham wrote, a court could consider not just the
“precise millisecond” when an offcer deploys force, but ev-
erything that “ha[d] transpired up until” that time. Ibid.
And with that wider focus, Judge Higginbotham would have
found that Felix's shooting of Barnes was unreasonable.
See id., at 401.
   We granted certiorari to address whether, in resolving
Fourth Amendment excessive-force claims, courts may apply
Page Proof Pending Publication
the moment-of-threat rule just described. See 603 U. S. 949
(2024). We hold they may not because that rule con-
stricts the proper inquiry into the “ totality of the
circumstances.”
                             II
  A claim that a law enforcement offcer used excessive force
during a stop or arrest is “analyzed under the Fourth
Amendment.” Graham, 490 U. S., at 395; see Amdt. 4
(applying to “seizures” of “persons”). The “touchstone of
the Fourth Amendment is `reasonableness,' ” as measured in
objective terms. Brigham City v. Stuart, 547 U. S. 398, 403
(2006). So the question in a case like this one, as this Court
has often held, is whether the force deployed was justifed
from “the perspective of a reasonable offcer on the scene,”
taking due account of both the individual interests and the
governmental interests at stake. Graham, 490 U. S., at 396;
County of Los Angeles v. Mendez, 581 U. S. 420, 428 (2017).
80                     BARNES v. FELIX

                      Opinion of the Court

   That inquiry into the reasonableness of police force re-
quires analyzing the “totality of the circumstances.” Id., at
427–428; Garner, 471 U. S., at 9. There is no “easy-to-apply
legal test” or “on/off switch” in this context. Scott v.
Harris, 550 U. S. 372, 382–383 (2007). Rather, the Fourth
Amendment requires, as we once put it, that a court “slosh
[its] way through” a “factbound morass.” Id., at 383. Or
said more prosaically, deciding whether a use of force was
objectively reasonable demands “careful attention to the
facts and circumstances” relating to the incident, as then
known to the offcer. Graham, 490 U. S., at 396. For exam-
ple, the “severity of the crime” prompting the stop can carry
weight in the analysis. See ibid.; Garner, 471 U. S., at 11.
So too can actions the offcer took during the stop, such as
giving warnings or otherwise trying to control the encoun-
ter. See id., at 12; Kingsley v. Hendrickson, 576 U. S. 389,
397 (2015). And the stopped person's conduct is always rele-
Page Proof Pending Publication
vant because it indicates the nature and level of the threat
he poses, either to the offcer or to others. See ibid.; Gra-
ham, 490 U. S., at 396.
   Most notable here, the “totality of the circumstances” in-
quiry into a use of force has no time limit. Of course, the
situation at the precise time of the shooting will often be
what matters most; it is, after all, the offcer's choice in that
moment that is under review. But earlier facts and circum-
stances may bear on how a reasonable offcer would have
understood and responded to later ones. Or as the Federal
Government puts the point, those later, “in-the-moment”
facts “cannot be hermetically sealed off from the context in
which they arose.” Brief for United States as Amicus Cu-
riae 14. Taking account of that context may beneft either
party in an excessive-force case. Prior events may show,
for example, why a reasonable offcer would have perceived
otherwise ambiguous conduct of a suspect as threatening.
Or instead they may show why such an offcer would have
perceived the same conduct as innocuous. The history of
                   Cite as: 605 U. S. 73 (2025)              81

                      Opinion of the Court

the interaction, as well as other past circumstances known
to the offcer, thus may inform the reasonableness of the use
of force.
   The Court's decision in Plumhoff v. Rickard, 572 U. S. 765
(2014), well illustrates the point. The excessive-force claim
there concerned the fatal shooting of a driver at the end of
a “dangerous car chase” lasting more than fve minutes. Id.,
at 768. The driver had sped away from a traffc stop on a
well-used road, and tried to outrun as many as six police
cruisers at speeds sometimes exceeding 100 miles per hour.
Eventually, the feeing car ran into one of the cruisers and
came “to a near standstill.” Id., at 776. The driver,
though, still tried to escape, pumping the gas in a way that
sent his wheels “spinning” and then putting the car into re-
verse. Ibid. At that point, one of the offcers fred several
shots into the car. In a suit brought against the offcer, the
driver's daughter contended that those shots were taken
Page Proof Pending Publication
when the chase was “already over.” Id., at 777. But this
Court rejected that claim based on everything that had hap-
pened during the incident—the driver's “outrageously reck-
less” behavior over the prior “fve minutes,” as well as his
last-second efforts to again take fight. Id., at 776. Given
all of those events, the Court explained, a reasonable offcer
would have concluded that the driver was “intent on resum-
ing” his getaway and, if allowed to do so, would “again pose
a deadly threat for others.” Id., at 777. In short, the
shooting was justifed “at the moment” it occurred partly
because of what had transpired in the preceding period.
Ibid.
   The moment-of-threat rule applied in the courts below pre-
vents that sort of attention to context, and thus conficts with
this Court's instruction to analyze the totality of the circum-
stances. Recall that the District Court and Fifth Circuit
limited their view to the two seconds before the shooting,
after Felix had stepped onto the doorsill of Barnes's car. See
supra, at 78–79. Those courts believed that, under Fifth
82                    BARNES v. FELIX

                      Opinion of the Court

Circuit precedent, they could not take into account anything
preceding that fnal moment. See 532 F. Supp. 3d, at 471
(excluding analysis of “what had transpired up until the
shooting itself ”); 91 F. 4th, at 397 (agreeing that “actions
leading up to the shooting are not relevant”). So, for exam-
ple, they could not consider the reasons for the stop or the
earlier conduct of, and interactions between, the suspect and
offcer. And because of that limit, they could not address
whether the fnal two seconds of the encounter would look
different if set within a longer timeframe. It is as though
the Court in Plumhoff could consider only the instant when
the chased car was at a “near standstill,” and not the earlier
time when it zigzagged down a busy roadway at speed. 572
U. S., at 776. To be sure, historical facts will not often mat-
ter as much as they did there to the reasonableness analysis.
See supra, at 81. And some of those facts may not be rele-
vant at all. But no rule that precludes consideration of
Page Proof Pending Publication
prior events in assessing a police shooting is reconcilable
with the fact-dependent and context-sensitive approach we
have prescribed. A court deciding a use-of-force case can-
not review the totality of the circumstances if it has put on
chronological blinders.
   That point is so evident that not even Felix quarrels with
it; his defense of the decisions below instead relies on taking
a different view of their meaning and of the question they
raise. First, the agreement with what we have said: Yes,
Felix acknowledges, prior events are not “off limits” in the
reasonableness inquiry, for they may “inform the perspective
of the reasonable offcer.” Tr. of Oral Arg. 79; Brief for Re-
spondent 2. Just so. But now the divergence: According to
Felix, the courts below acted consistently with that all-times-
considered principle. The Fifth Circuit's moment-of-threat
doctrine, Felix argues, in fact allows courts to assess many
pre-shooting facts and circumstances—and courts applying it
often do so. See id., at 20 (citing other Fifth Circuit deci-
sions). All that the doctrine bars is a single kind of in-
                    Cite as: 605 U. S. 73 (2025)               83

                       Opinion of the Court

quiry—into whether an offcer's earlier error itself “created
the need for deadly force.” Id., at 21; see Tr. of Oral Arg.
53. And on that issue, Felix submits, the Fifth Circuit is
right: “[A]n offcer doesn't lose his right to defend himself
just because” he previously “made a mistake.” Ibid.
   But whatever might be said of Fifth Circuit law generally,
the decisions below applied a rule about timing. As shown
above, both lower courts took pains to explain that, in evalu-
ating the shooting's reasonableness, they could look only to
a two-second snippet of the encounter. See supra, at 78–79.
And because that was the reasoning in the case before us,
that is the reasoning we must address. It could make no
difference to our decision here if the Fifth Circuit in other
cases eschewed a strict time limit, as Felix claims. And
anyway, we are not sure Felix correctly describes the overall
state of Fifth Circuit law. Consider Harris v. Serpas—a
Fifth Circuit decision relied on below. See 91 F. 4th, at 397.
Page Proof Pending Publication
The court there noted the plaintiffs' recital of several histori-
cal facts—actions of both the suspect and the offcer in the
period prior to the shooting. See 745 F. 3d, at 772. And
the court recognized that this Court's decisions directed an
inquiry into the “the `totality of the circumstances.' ” Ibid.
(quoting Graham, 490 U. S., at 396). But then came the fol-
lowing: “This [Circuit], however, has narrowed that test” in
deadly force cases, holding that the inquiry there is “confned
to whether the [offcer] was in danger at the moment of the
threat that resulted in the [offcer's] shooting.” Ibid. (alter-
ations in original). The problem with the statement is ap-
parent. As we have explained, a court cannot thus “narrow”
the totality-of-the-circumstances inquiry, to focus on only a
single moment. It must look too, in this and all excessive-
force cases, at any relevant events coming before.
   We do not address here the different question Felix raises
about use-of-force cases: whether or how an offcer's own “cre-
ation of a dangerous situation” factors into the reasonableness
analysis. Brief for Respondent 22; see supra, at 82–83.
84                    BARNES v. FELIX

                   Kavanaugh, J., concurring

As in another of our recent Fourth Amendment cases, that
issue is not properly before us. See Mendez, 581 U. S., at
429, n. The courts below never confronted the issue, pre-
cisely because their inquiry was so time-bound. In looking
at only the two seconds before the shot, they excluded from
view any actions of the offcer that allegedly created the dan-
ger necessitating deadly force. See supra, at 78–79. So, to
use the obvious example, the courts below did not address
the relevance, if any, of Felix stepping onto the doorsill of
Barnes's car. And because they never considered that issue,
it was not the basis of the petition for certiorari. The
question presented to us was one of timing alone: whether
to look only at the encounter's fnal two seconds, or also to
consider earlier events serving to put those seconds in
context.
    With that matter resolved, we return everything else to
the courts below. It is for them now to consider the reason-
ableness of the shooting, using the lengthier timeframe we
Page Proof Pending Publication
have prescribed.
   Accordingly, we vacate the judgment of the Court of Ap-
peals and remand the case for further proceedings consistent
with this opinion.
                                              It is so ordered.

  Justice Kavanaugh, with whom Justice Thomas, Jus-
tice Alito, and Justice Barrett join, concurring.
   I join the Court's opinion. I agree that the offcer's ac-
tions during the traffc stop in this case should be assessed
based on the totality of the circumstances. I write sepa-
rately to add a few points about the dangers of traffc stops
for police offcers, particularly when as here the driver pulls
away in the midst of the stop.
   Even for routine traffic violations, traffic stops are
“fraught with danger to police offcers.” Michigan v. Long,
463 U. S. 1032, 1047 (1983). An “inordinate risk confront[s]
an offcer as he approaches a person seated in an automo-
                       Cite as: 605 U. S. 73 (2025)                     85

                       Kavanaugh, J., concurring

bile.” Pennsylvania v. Mimms, 434 U. S. 106, 110 (1977)
(per curiam). That is in part because offcers operate at a
“tactical disadvantage” when “approaching an unknown ve-
hicle, with limited visibility and unpredictable threats.”
Brief for National Fraternal Order of Police as Amicus Cu-
riae 4. As this Court noted nearly 50 years ago, “a signif-
cant percentage of murders of police offcers occurs when the
offcers are making traffc stops.” Mimms, 434 U. S., at 110
(quoting United States v. Robinson, 414 U. S. 218, 234, n. 5
(1973)). Traffc stops remain highly dangerous today. See
Dept. of Justice, Federal Bureau of Investigation, Law En-
forcement Offcers Killed and Assaulted, 2023 (2024) (Table
27). On April 8, 2023, two offcers were shot and killed at
an intersection in Cameron, Wisconsin, after stopping a car
for a warrant and welfare check on the driver.1 On Decem-
ber 8, 2024, an offcer was shot and killed after he pulled
over a pickup truck with expired license plates in a Super 8
motel parking lot in Terrell, Texas. See Brief for State of
Page Proof Pending Publication
Texas et al. as Amici Curiae 1, and n. 4. The list goes on
and on.2
   Offcers cannot let their guard down and assume that any
particular traffc stop will be safe—even if a driver is pulled
over for nothing more than a speeding violation, a broken
taillight, or the like. The driver may be drunk, on drugs,
armed, or some combination thereof. Or the driver may
have committed (or may be about to commit) a serious crime.
“People detained for minor offenses” such as ordinary traffc
violations “can turn out to be the most devious and danger-
  1
    See Offcer Down Memorial Page, Police Offcer Emily Ann Breidenbach,
https://www.odmp.org/officer/26693-police-officer-emily-ann-breidenbach;
Offcer Down Memorial Page, Police Offcer Hunter Timothy Scheel, https://
www.odmp.org/offcer/26694-police-offcer-hunter-timothy-scheel.
  2
    To be sure, offcers sometimes use excessive force during traffc stops.
When that happens, offcers of course should be held to account for their
actions. See Brief for Current and Former Law Enforcement Offcials as
Amici Curiae 22; Brief for California State Sheriffs' Association et al. as
Amici Curiae 10.
86                     BARNES v. FELIX

                    Kavanaugh, J., concurring

ous criminals.” Florence v. Board of Chosen Freeholders of
County of Burlington, 566 U. S. 318, 334 (2012). Timothy
McVeigh, the man responsible for the 1995 Oklahoma City
bombing, was stopped for a missing license plate, which ulti-
mately led to his apprehension for the bombing. See ibid.
Likewise, serial killer Ted Bundy was pulled over based on
a stolen-vehicle alert in Pensacola, Florida. When informed
that he was under arrest, Bundy kicked the offcer's legs out
from under him, and the two struggled over the offcer's gun
before the offcer was able to subdue and arrest Bundy. See
Bundy v. Dugger, 850 F. 2d 1402, 1422 (CA11 1988); see
also Brief for State of Texas et al. as Amici Curiae 11–12,
and n. 12.
   So even though most traffc stops end without incident,
traffc stops are nonetheless inherently risky for police off-
cers. And when, as in this case, the driver suddenly pulls
away in the midst of a stop, the risks multiply. A driver
Page Proof Pending Publication
speeding away from a traffc stop could easily endanger by-
standers and other drivers—especially if the feeing driver
is under the infuence of alcohol or drugs, as might well be
the case when a driver fees. Moreover, the very “fact that
a suspect fees when suspected of a minor offense,” such as
speeding or a failure to pay tolls, “could well be indicative of
a larger danger.” Lange v. California, 594 U. S. 295, 331
(2021) (Roberts, C. J., concurring in judgment). Fleeing
from the traffc stop could suggest that the driver is prepar-
ing to commit or has committed a more serious crime—and
is attempting to evade detection or arrest. The driver may
have illegal drugs or an illegal gun in the car. Or the driver
may be unlawfully in the country and fear removal if appre-
hended. He might have a warrant out for his arrest. He
could have an abducted child in the car. See Tr. of Oral Arg.
18. Or as the tragic 2025 New Year's terrorist attack in
New Orleans illustrates, the driver might intend to use the
car as a weapon. See id., at 24.
                   Cite as: 605 U. S. 73 (2025)             87

                   Kavanaugh, J., concurring

   The possibilities are many. But the key point is a com-
monsense one: A driver who speeds away from a traffc stop
can pose signifcant dangers to both the offcer and the sur-
rounding community.
   The question when a driver fees, therefore, is not merely
whether the underlying traffc violation “presents risks to
public safety”—it is also “whether fight,” and what that
fight might indicate or enable, “does so.” Lange, 594 U. S.,
at 331 (Roberts, C. J., concurring in judgment). In those
circumstances, in other words, it is not only the “severity of
the crime” that prompted the stop that is relevant to the
“totality of the circumstances” inquiry. Graham v. Connor,
490 U. S. 386, 396 (1989) (quotation marks omitted). The
Fourth Amendment analysis must also take account of the
suspect's attempt “to evade” the offcer “by fight.” Ibid.
   What should the offcer do when a driver fees from a traf-
fc stop? There are no easy or risk-free answers. Every
Page Proof Pending Publication
feasible option poses some potential danger to the offcer, the
driver, or the public at large—and often to all three. And
an offcer in that situation must make a split-second choice
among those various dangerous options.
   First, the offcer could simply let the driver go. But be-
cause the feeing driver might be a threat to the community,
letting the driver go may exacerbate the dangers, rather
than mitigate them. Encouraging offcers to stand back and
allow drivers to take off would also create “perverse incen-
tives” for those who are stopped by the police. Scott v. Har-
ris, 550 U. S. 372, 385 (2007). If doing nothing in response
to a feeing driver became a known and regular practice
among police offcers, that would presumably embolden some
drivers who otherwise might have thought twice about tak-
ing off.
   Of course, the offcer could let the driver go in the moment
but then attempt to catch the driver by, for example, track-
ing the car's license plate or reviewing surveillance footage.
See Tr. of Oral Arg. 8. But after letting the driver go, the
88                        BARNES v. FELIX

                       Kavanaugh, J., concurring

police may not be able to later track down the car or the
driver of the car. Even if the police are able to do so, the
escaped driver may pose a serious risk to the public in the
interim. And given that the driver has already shown a
propensity to evade law enforcement by feeing a traffc stop,
attempting to execute an arrest upon fnding the driver could
itself be dangerous for the police and others.
   Second, the offcer could get back in his police car and give
chase, or could radio other offcers to pursue the driver. But
a high-speed chase likewise can be exceptionally dangerous
to the offcer, the driver, and others on the road. “Vehicular
pursuits” are “often catastrophic.” Lange, 594 U. S., at 324
(Roberts, C. J., concurring in judgment). Many real-world
examples demonstrate as much. Plumhoff v. Rickard in-
volved a “ `dangerous car chase' ” in which the driver “tried
to outrun as many as six police cruisers at speeds sometimes
exceeding 100 miles per hour,” ending in the “fatal shooting”
of the driver. Ante, at 81 (quoting 572 U. S. 765, 768 (2014)).
Page Proof Pending Publication
In Scott v. Harris, multiple police cars “with blue lights
fashing and sirens blaring” chased the driver “for nearly 10
miles” while “he ignored their warning to stop,” culminating
in an offcer ramming the driver off the road. 550 U. S., at
384. Moreover, a recent study concluded that a signifcant
percentage of those killed in police chases are not the feeing
drivers but rather are passengers or bystanders. From
2017 through 2022, more than 500 bystanders were report-
edly killed as a result of police chases.3
   Third, the offcer might try to shoot out the tires of the
feeing car, or otherwise try to hinder the car's movement,
in order to bring it to a stop. But shooting at a car, espe-
cially its tires, can be “dangerous” and is often “ineffective.” 4

  3
    See S. Neilson, J. Gollan, & J. Haseman, First-of-Its-Kind Database:
Majority of People Killed in Police Chases Aren't the Fleeing Drivers, San
Francisco Chronicle (Feb. 2024).
  4
    Los Angeles County Sheriff's Dept., Field Operations Support Services
Newsletter: 15–14 – Shooting at Vehicle Tires (2025).
                   Cite as: 605 U. S. 73 (2025)              89

                   Kavanaugh, J., concurring

Even if the offcer manages to hit the tires, the driver could
lose control and crash into others on the road. That course
of action also poses the risk of the offcer accidentally shoot-
ing the driver or innocent passengers.
   Fourth, as happened here, the offcer could attempt to stop
the feeing driver at the outset by jumping on or reaching
into the car. The dangerousness of that option is readily
apparent. Perhaps the driver will hit the brakes once he
realizes an offcer is clinging to the car or attempting to
reach through the window. But if the driver does not slow
down, then the offcer may suffer serious and perhaps fatal
injuries. The offcer could try to fre his weapon to incapaci-
tate the driver and bring the car safely to a stop. But the
car may be just as likely to go careening into traffc, thereby
threatening the safety of the offcer, other drivers, passen-
gers, pedestrians, and more.
   I could go on. The point here is that when a driver
Page Proof Pending Publication
abruptly pulls away during a traffc stop, an offcer has no
particularly good or safe options. None of the options avail-
able to the offcer avoids danger to the community, and all
of them require life-or-death decisions that must be made
in a few seconds in highly stressful and unpredictable
circumstances.
   Of course, when an offcer uses force against a feeing
driver, the judiciary still must assess any resulting Fourth
Amendment claim under the standard of objective reason-
ableness. Under this Court's precedents, that inquiry in-
volves “a careful balancing of `the nature and quality of the
intrusion on the individual's Fourth Amendment interests'
against the countervailing governmental interests at stake.”
Graham, 490 U. S., at 396 (quoting Tennessee v. Garner, 471
U. S. 1, 8 (1985)). In conducting that analysis, judges should
keep in mind that it is one thing to dissect and scrutinize an
offcer's actions with the “20/20 vision of hindsight,” “in the
peace of a judge's chambers.” Graham, 490 U. S., at 396
(quotation marks omitted). It is quite another to make
90                    BARNES v. FELIX

                   Kavanaugh, J., concurring

“split-second judgments” on the ground, “in circumstances
that are tense, uncertain, and rapidly evolving.” Id., at 397.
In analyzing the reasonableness of an offcer's conduct at a
traffc stop, particularly traffc stops where the driver has
suddenly pulled away, courts must appreciate the extraordi-
nary dangers and risks facing police offcers and the commu-
nity at large.




Page Proof Pending Publication
                            Reporter’s Note

  The attached opinion has been revised to refect the usual publication
and citation style of the United States Reports. The revised pagination
makes available the offcial United States Reports citation in advance of
publication. The syllabus has been prepared by the Reporter of Decisions
for the convenience of the reader and constitutes no part of the opinion of
Page Proof Pending Publication
the Court. A list of counsel who argued or fled briefs in this case, and
who were members of the bar of this Court at the time this case was
argued, has been inserted following the syllabus. Other revisions may
include adjustments to formatting, captions, citation form, and any errant
punctuation. The following additional edits were made:

p. 73, line 18 from bottom: “the” is inserted before “threat”
p. 73, line 11 from bottom: “at” is changed to “on”

```

---

## GROUP: _overhaul2/lake/cases/Brownback v. King.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Brownback v. King
type: case
citation: "592 U.S. 209 (2021)"
parallel_cite: "209 L. Ed. 2d 33; 141 S. Ct. 740"
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2021
date_decided: ""
docket: 19-546
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
  opinion_url: "https://www.courtlistener.com/opinion/4858987/brownback-v-king/"
  cluster_id: 4858987
  opinion_id: null
  identity_checked: true
lake:
  record_id: Brownback v. King
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Suing Federal Officers]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Bivens v. Six Unknown Named Agents]]"
tags:
  - case
  - ftca
  - bivens
  - judgment-bar
  - federal-officer-liability
  - section-1983
holding: "A district court's Rule 12(b)(6) dismissal of a plaintiff's FTCA claims — even one that simultaneously deprives the court of subject-matter jurisdiction — is a judgment 'on the merits' that can trigger the FTCA judgment bar in 28 U.S.C. § 2676; whether that bar reaches Bivens claims brought in the same suit was left open on remand."
---

# Brownback v. King

*592 U.S. 209 (2021)* (No. 19-546) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4858987 → opinion 4662766; quote string-matched to the CL opinion text 2026-07-07 (CL carries the slip opinion, 592 U.S. ___; pin cited slip-style per S2 A3). S9 promotes. -->

## Background
James King, a college student, was mistakenly identified as a fugitive and violently seized and beaten by members of a joint FBI–Grand Rapids fugitive task force. He sued the United States under the Federal Tort Claims Act and sued the officers directly under *[[Bivens v. Six Unknown Named Agents|Bivens]]*. The District Court dismissed the FTCA claims under Rule 12(b)(6) — reasoning that King could not establish all six elements of an FTCA claim, which in its view also deprived the court of subject-matter jurisdiction — and dismissed the *[[Bivens v. Six Unknown Named Agents|Bivens]]* claims on [[Qualified Immunity|qualified immunity]]. King appealed only the *[[Bivens v. Six Unknown Named Agents|Bivens]]* dismissal. The Sixth Circuit held that the FTCA dismissal did not trigger the FTCA's judgment bar (because it was "jurisdictional") and reversed the qualified-immunity ruling.

## Issue
Whether a district court's Rule 12(b)(6) dismissal of a plaintiff's FTCA claims — framed as a lack of subject-matter jurisdiction — is a judgment "on the merits" that can trigger the FTCA's judgment bar, 28 U.S.C. § 2676, and thereby block the plaintiff's parallel *[[Bivens v. Six Unknown Named Agents|Bivens]]* claims.

## Rule
The FTCA's judgment bar, § 2676, provides that "[t]he judgment in an action under section 1346(b)" bars "any action by the claimant, by reason of the same subject matter, against the employee of the government whose act or omission gave rise to the claim." Drafted against the backdrop of res judicata, the bar requires a judgment "on the merits." A single order can be both jurisdictional and on the merits where the FTCA's merits elements and jurisdictional elements entirely overlap. The Court held: "We disagree and hold that the District Court's order also went to the merits of the claim and thus could trigger the judgment bar." — 592 U.S. 209 (slip op., at 1). ^pin-1

## Application
The District Court had "passed on the substance" of King's FTCA claims and found them implausible under Rule 12(b)(6); that the same ruling also determined the court lacked jurisdiction did not strip it of merits effect, because King's failure to plausibly allege an element that was both a merits element and a jurisdictional element resolved the claim on its substance. The Court reversed the Sixth Circuit's contrary holding, but expressly declined to decide King's alternative argument — pressed in Justice Sotomayor's [[Common Legal Terms#concurring-opinion|concurrence]] — that the judgment bar may not apply to claims dismissed in the *same* lawsuit, leaving that and King's other arguments for the Sixth Circuit [[Reading and Citing Cases#on-remand|on remand]].

## Conclusion
The judgment of the Sixth Circuit was **reversed** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. Thomas, J., delivered the opinion for a unanimous Court; Sotomayor, J., filed a [[Common Legal Terms#concurring-opinion|concurring opinion]] questioning whether the judgment bar reaches claims resolved within the same suit.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Brownback* is a procedural decision about the interaction of the FTCA and *[[Bivens v. Six Unknown Named Agents|Bivens]]* remedies against federal officers; it holds only that an FTCA merits dismissal *can* trigger the § 2676 judgment bar, leaving the same-suit question open [[Reading and Citing Cases#on-remand|on remand]].

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Brownback v. King*, 592 U.S. 209 (2021)](https://www.courtlistener.com/opinion/4858987/brownback-v-king/) — pinpoint: slip op., at 1 (Opinion of the Court, holding); quote string-matched to the CL slip-opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d1a4bcd0ac203cbb", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Brownback v. King"}, "payload": {"all": [{"cite": "592 U.S. 209", "page": "209", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "592"}, {"cite": "209 L. Ed. 2d 33", "page": "33", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "209"}, {"cite": "141 S. Ct. 740", "page": "740", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "141"}], "display": "592 U.S. 209", "official": {"cite": "592 U.S. 209", "page": "209", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "592"}, "official_selection_present": true, "record_id": "Brownback v. King"}}
{"assertion_id": "70600aa42974552c", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Brownback v. King"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Brownback v. King", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Brownback v. King

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brownback v. King",
  "status": "under_review",
  "identity": {
    "case_name": "Brownback v. King",
    "case_name_short": "Brownback",
    "case_name_full": "",
    "input_case_name": "Brownback v. King",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2021,
    "docket": "19-546",
    "cluster_id": 4858987,
    "lead_opinion_id": 4662766,
    "sibling_ids": [],
    "absolute_url": "/opinion/4858987/brownback-v-king/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "592 U.S. 209",
      "volume": "592",
      "reporter": "U.S.",
      "page": "209",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "209 L. Ed. 2d 33",
        "volume": "209",
        "reporter": "L. Ed. 2d",
        "page": "33",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 740",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "740",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "592 U.S. 209",
        "volume": "592",
        "reporter": "U.S.",
        "page": "209",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "209 L. Ed. 2d 33",
        "volume": "209",
        "reporter": "L. Ed. 2d",
        "page": "33",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 740",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "740",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "592 U.S. 209",
    "official_selection": {
      "court_class": "scotus",
      "selected": "592 U.S. 209",
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
    "date_created": "2026-07-06T12:09:57Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:10:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:10:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:10:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:10:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "brownback-v-king--4858987",
      "to_record_id": "Brownback v. King",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Brownback v. King

```
(Slip Opinion)              OCTOBER TERM, 2020                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                     BROWNBACK ET AL. v. KING

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE SIXTH CIRCUIT

 No. 19–546.      Argued November 9, 2020—Decided February 25, 2021
The Federal Tort Claims Act (FTCA) allows a plaintiff to bring certain
  state-law tort claims against the United States for torts committed by
  federal employees acting within the scope of their employment, pro-
  vided that the plaintiff alleges six statutory elements of an actionable
  claim. See 28 U. S. C. §1346(b). Another provision, known as the judg-
  ment bar, provides that “[t]he judgment in an action under section
  1346(b)” shall bar “any action by the claimant” involving the same sub-
  ject matter against the federal employee whose act gave rise to the
  claim. §2676. Respondent James King sued the United States under
  the FTCA after a violent encounter with Todd Allen and Douglas
  Brownback, members of a federal task force. He also sued the officers
  individually under the implied cause of action recognized by Bivens v.
  Six Unknown Fed. Narcotics Agents, 403 U. S. 388. The District Court
  dismissed his FTCA claims, holding that the Government was immune
  because the officers were entitled to qualified immunity under Michi-
  gan law, or in the alternative, that King failed to state a valid claim
  under Federal Rule of Civil Procedure 12(b)(6). The court also dis-
  missed King’s Bivens claims, ruling that the officers were entitled to
  federal qualified immunity. King appealed only the dismissal of his
  Bivens claims. The Sixth Circuit found that the District Court’s dis-
  missal of King’s FTCA claims did not trigger the judgment bar to block
  his Bivens claims.
Held: The District Court’s order was a judgment on the merits of the
 FTCA claims that can trigger the judgment bar. Pp. 5–10.
    (a) Similar to common-law claim preclusion, the judgment bar re-
 quires a final judgment “ ‘on the merits,’ ” Semtek Int’l Inc. v. Lockheed
 Martin Corp., 531 U. S. 497, 502. Here, the District Court’s summary
2                         BROWNBACK v. KING

                                  Syllabus

    judgment ruling dismissing King’s FTCA claims hinged on a quintes-
    sential merits decision: whether the undisputed facts established all
    the elements of King’s FTCA claims. See Arbaugh v. Y & H Corp., 546
    U. S. 500, 510–511. The court’s alternative Rule 12(b)(6) holding also
    passed on the substance of King’s FTCA claims, as a 12(b)(6) ruling
    concerns the merits. Id., at 506–507. Pp. 5–7.
       (b) In passing on King’s FTCA claims, the District Court also deter-
    mined that it lacked subject-matter jurisdiction over those claims. In
    most cases, a plaintiff’s failure to state a claim under Rule 12(b)(6)
    does not deprive a federal court of subject-matter jurisdiction. See
    Steel Co. v. Citizens for Better Environment, 523 U. S. 83, 89. Here,
    however, in the unique context of the FTCA, all elements of a merito-
    rious claim are also jurisdictional. Thus, even though a plaintiff need
    not prove a §1346(b)(1) jurisdictional element for a court to maintain
    subject-matter jurisdiction over his claim, see FDIC v. Meyer, 510 U. S.
    471, 477, because King’s FTCA claims failed to survive a Rule 12(b)(6)
    motion to dismiss, the court also was deprived of subject-matter juris-
    diction. Generally, a court may not issue a ruling on the merits when
    it lacks subject-matter jurisdiction, see Steel Co., 523 U. S., at 101–
    102, but where, as here, pleading a claim and pleading jurisdiction en-
    tirely overlap, a ruling that the court lacks subject-matter jurisdiction
    may simultaneously be a judgment on the merits that can trigger the
    judgment bar. Pp. 7–9.
917 F. 3d. 409, reversed.

   THOMAS, J., delivered the opinion for a unanimous Court. SOTOMAYOR,
J., filed a concurring opinion.
                        Cite as: 592 U. S. ____ (2021)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 19–546
                                    _________________


  DOUGLAS BROWNBACK, ET AL., PETITIONERS v.
              JAMES KING
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE SIXTH CIRCUIT
                               [February 25, 2021]

  JUSTICE THOMAS delivered the opinion of the Court.
  The Federal Tort Claims Act (FTCA) allows a plaintiff to
bring certain state-law tort suits against the Federal Gov-
ernment. 28 U. S. C. §2674; see also §1346(b). It also in-
cludes a provision, known as the judgment bar, which pre-
cludes “any action by the [plaintiff], by reason of the same
subject matter, against the employee of the government
whose act or omission gave rise to the claim” if a court en-
ters “[t]he judgment in an action under section 1346(b).”
§2676. The Sixth Circuit held that the District Court’s or-
der dismissing the plaintiff’s FTCA claims did not trigger
the judgment bar because the plaintiff’s failure to establish
all elements of his FTCA claims had deprived the court of
subject-matter jurisdiction. We disagree and hold that the
District Court’s order also went to the merits of the claim
and thus could trigger the judgment bar.
                             I
                            A
  The FTCA streamlined litigation for parties injured by
federal employees acting within the scope of their employ-
ment. Before 1946, a plaintiff could sue a federal employee
2                       BROWNBACK v. KING

                         Opinion of the Court

directly for damages, but sovereign immunity barred suits
against the United States, even if a similarly situated pri-
vate employer would be liable under principles of vicarious
liability. Pfander & Aggarwal, Bivens, the Judgment Bar,
and the Perils of Dynamic Textualism, 8 U. St. Thomas
L. J. 417, 424–425 (2011); see also Philadelphia Co. v. Stim-
son, 223 U. S. 605, 619–620 (1912). Despite that immunity,
the Government often would provide counsel to defendant
employees or indemnify them. Pfander, 8 U. St. Thomas
L. J., at 425. In addition, Congress passed private bills that
awarded compensation to persons injured by Government
employees. Id., at 424, n. 39. But by the 1940s, Congress
was considering hundreds of such private bills each year.
Ibid.1 “Critics worried about the speed and fairness with
which Congress disposed of these claims.” Id., at 426.
   “In 1946, Congress passed the FTCA, which waived the
sovereign immunity of the United States for certain torts
committed by federal employees” acting within the scope of
their employment. FDIC v. Meyer, 510 U. S. 471, 475–476
(1994). The Act in effect ended the private bill system by
transferring most tort claims to the federal courts. See
Pfander, 8 U. St. Thomas. L. J., at 424, n. 39. Plaintiffs
were (and are) required to bring claims under the FTCA in
federal district court. Federal courts have jurisdiction over
these claims if they are “actionable under §1346(b).” Meyer,
510 U. S., at 477. A claim is actionable if it alleges the six
elements of §1346(b), which are that the claim be:
        “[1] against the United States, [2] for money
        damages, . . . [3] for injury or loss of property,
        or personal injury or death [4] caused by the
        negligent or wrongful act or omission of any
        employee of the Government [5] while acting
        within the scope of his office or employment,
——————
 1 In 1939 and 1940 the 76th Congress considered 1,763 private bills, of

which 315 became law. Pfander, 8 U. St. Thomas L. J., at 424, n. 39.
                  Cite as: 592 U. S. ____ (2021)             3

                      Opinion of the Court

       [6] under circumstances where the United
       States, if a private person, would be liable to
       the claimant in accordance with the law of
       the place where the act or omission oc-
       curred.” Ibid. (quoting §1346(b)).
   While waiving sovereign immunity so parties can sue the
United States directly for harms caused by its employees,
the FTCA made it more difficult to sue the employees them-
selves by adding a judgment bar provision. That provision
states: “The judgment in an action under section 1346(b) of
this title shall constitute a complete bar to any action by the
claimant, by reason of the same subject matter, against the
employee of the government whose act or omission gave rise
to the claim.” §2676. “[O]nce a plaintiff receives a judgment
(favorable or not) in an FTCA suit,” the bar is triggered, and
“he generally cannot proceed with a suit against an individ-
ual employee based on the same underlying facts.” Sim-
mons v. Himmelreich, 578 U. S. 621, 625 (2016). The Act
thus opened a new path to relief (suits against the United
States) while narrowing the earlier one (suits against em-
ployees).
                             B
  This case involves a violent encounter between respond-
ent James King and officers Todd Allen and Douglas
Brownback, members of a federal task force, who mistook
King for a fugitive. King sued the United States under the
FTCA, alleging that the officers committed six torts under
Michigan law. He also sued the officers individually under
the implied cause of action recognized by Bivens v. Six Un-
known Fed. Narcotics Agents, 403 U. S. 388 (1971), alleging
four violations of his Fourth Amendment rights. The de-
fendants moved to dismiss under Federal Rule of Civil Pro-
cedure 12(b)(1) for lack of subject-matter jurisdiction and
under Rule 12(b)(6) for failure to state a claim. In the al-
ternative, they moved for summary judgment.
4                       BROWNBACK v. KING

                          Opinion of the Court

   The District Court dismissed King’s claims. As to his
FTCA claims, the court granted the Government’s sum-
mary judgment motion.2 It found that the undisputed facts
showed that the officers did not act with malice. The offic-
ers thus would have been entitled to state qualified immun-
ity had Michigan tort claims been brought against them.
See Odom v. Wayne County, 482 Mich. 459, 473–474, 760
N. W. 2d 217, 224–225 (2008). The court, following its own
precedent, ruled that the Government was immune because
it retains the benefit of state-law immunities available to
its employees. The court also ruled in the alternative that
King’s FTCA claims failed under Rule 12(b)(6) because his
complaint did not present enough facts to state a plausible
claim to relief for any of his six tort claims. The court dis-
missed King’s Bivens claims as well, ruling that the defend-
ants were entitled to federal qualified immunity. King ap-
pealed only the dismissal of his Bivens claims.
   As a threshold question, the Sixth Circuit assessed
whether the dismissal of King’s FTCA claims triggered the
judgment bar and thus blocked the parallel Bivens claims.
See King v. United States, 917 F. 3d 409, 418–421 (2019).
It did not, according to the Sixth Circuit, because “the dis-
trict court dismissed [King]’s FTCA claim[s] for lack of sub-
ject-matter jurisdiction” when it determined that he had
not stated a viable claim and thus “did not reach the mer-
its.” Id., at 419; but see Unus v. Kane, 565 F. 3d 103, 121–
122 (CA4 2009) (holding that summary judgment on the
plaintiffs’ FTCA claims triggered judgment bar with re-
spect to Bivens claims). The Sixth Circuit then held that
the defendant officers were not entitled to qualified immun-
ity and reversed the District Court.
——————
  2 Like the Sixth Circuit, we construe the District Court’s primary rul-

ing on the FTCA claims as a grant of summary judgment for the defend-
ants because its ruling relied on the parties “ ‘Joint Statement of
Facts . . . unless otherwise indicated.’ ” King v. United States, 917 F. 3d
409, 416, n. 1 (CA6 2019) (quoting ECF Doc. 91, p. 1).
                        Cite as: 592 U. S. ____ (2021)                           5

                             Opinion of the Court

  We granted certiorari, 589 U. S. ___ (2020), and now
reverse.
                               II
                               A
   The judgment bar provides that “[t]he judgment in an ac-
tion under section 1346(b)” shall bar “any action by the
claimant” involving the same subject matter against the
employee of the Federal Government whose act gave rise to
the claim. §2676. Here, the District Court entered a “Judg-
ment . . . in favor of Defendants and against Plaintiff.” ECF
Doc. 92. The parties agree that, at a minimum, this judg-
ment must have been a final judgment on the merits to trig-
ger the bar, given that the “provision functions in much the
same way as [the common-law doctrine of claim preclu-
sion].” Simmons, 578 U. S., at 630, n. 5 (internal quotation
marks omitted).3 We agree.4


——————
   3 The terms res judicata and claim preclusion often are used inter-

changeably. See Lucky Brand Dungarees, Inc. v. Marcel Fashions Group,
Inc., 590 U. S. ___, ___ (2020) (slip op., at 6). But res judicata “comprises
two distinct doctrines.” Ibid. The first is issue preclusion, also known as
collateral estoppel. Ibid. It precludes a party from relitigating an issue
actually decided in a prior case and necessary to the judgment. Ibid. The
second doctrine is claim preclusion, sometimes itself called res judicata.
Ibid. Claim preclusion prevents parties from relitigating the same
“claim” or “ ‘cause of action,’ ” even if certain issues were not litigated in
the prior action. Ibid. Suits involve the same “claim” or “ ‘ cause of ac-
tion ’ ” if the later suit “ ‘ “aris[es] from the same transaction” ’ ” or involves
a “ ‘common nucleus of operative facts.’ ” Ibid.
   4 King argues, among other things, that the judgment bar does not ap-

ply to a dismissal of claims raised in the same lawsuit because common-
law claim preclusion ordinarily “is not appropriate within a single law-
suit.” 18 C. Wright, A. Miller, & E. Cooper, Federal Practice and Proce-
dure §4401 (3d ed. Supp. 2020). The Sixth Circuit did not address those
arguments, and “we are a court of review, not of first view.” Cutter v.
Wilkinson, 544 U. S. 709, 718, n. 7 (2005). We leave it to the Sixth Cir-
cuit to address King’s alternative arguments on remand.
6                       BROWNBACK v. KING

                          Opinion of the Court

                                B
   This Court has explained that the judgment bar was
drafted against the backdrop doctrine of res judicata. See
ibid.5 To “trigge[r ] the doctrine of res judicata or claim pre-
clusion” a judgment must be “ ‘on the merits.’ ” Semtek Int’l
Inc. v. Lockheed Martin Corp., 531 U. S. 497, 502 (2001).
Under that doctrine as it existed in 1946, a judgment is “on
the merits” if the underlying decision “actually passes di-
rectly on the substance of a particular claim before the
court.” Id., at 501–502 (cleaned up).6 Thus, to determine if
the District Court’s decision is claim preclusive, we must
determine if it passed directly on the substance of King’s
FTCA claims. We conclude that it did.
   The District Court’s summary judgment ruling hinged on
a quintessential merits decision: whether the undisputed
facts established all the elements of King’s FTCA claims.
See Arbaugh v. Y & H Corp., 546 U. S. 500, 510–511 (2006).
The court noted that one element of an FTCA claim is that
the plaintiff establish that the Government employee would
be liable under state law. The court then explained that
Michigan law provides qualified immunity for Government
employees who commit intentional torts but act in subjec-
tive good faith. See Odom, 482 Mich., at 461, 481–482, 760
N. W. 2d, at 218, 229. And it concluded that, because the
undisputed facts here showed that the officers would have
——————
  5 The parties disagree about how much the judgment bar expanded on

common-law preclusion, but those disagreements are not relevant to our
decision. See n. 4, supra.
  6 We use the term “on the merits” as it was used in 1946, to mean a

decision that passed on the substance of a particular claim. “[O]ver the
years the meaning of the term ‘judgment on the merits’ ‘has gradually
undergone change’ ” and now encompasses some judgments “that do not
pass upon the substantive merits of a claim and hence do not (in many
jurisdictions) entail claim-preclusive effect.” Semtek, 531 U. S., at 502.
Regardless, the FTCA judgment in this case is an “on the merits” deci-
sion that passes on the “substance” of King’s FTCA claims under the
1946 meaning or present day meaning of those terms.
                     Cite as: 592 U. S. ____ (2021)                     7

                          Opinion of the Court

been entitled to immunity from King’s tort claims, the
United States, by extension, was not liable under the
FTCA.7
   The court’s alternative Rule 12(b)(6) holding also passed
on the substance of King’s FTCA claims. The District Court
ruled that the FTCA count in King’s complaint did not state
a claim, because even assuming the complaint’s veracity,
the officers used reasonable force, had probable cause to de-
tain King, and otherwise acted within their authority. “If
the judgment determines that the plaintiff has no cause of
action” based “on rules of substantive law,” then “it is on
the merits.” Restatement of Judgments §49, Comment a, p.
193 (1942). A ruling under Rule 12(b)(6) concerns the mer-
its. Cf. Arbaugh, 546 U. S., at 506–507. The District Court
evaluated King’s six FTCA claims under Rule 12(b)(6) and
ruled that they failed for reasons of substantive law.
                                 C
   The one complication in this case is that it involves over-
lapping questions about sovereign immunity and subject-
matter jurisdiction. In such cases, the “merits and jurisdic-
tion will sometimes come intertwined,” and a court can de-
cide “all . . . of the merits issues” in resolving a jurisdic-
tional question, or vice versa. Bolivarian Republic of
Venezuela v. Helmerich & Payne Int’l Drilling Co., 581 U. S.
___, ___ (2017) (slip op., at 7). That occurred here. The Dis-
trict Court passed on the substance of King’s FTCA claims
and found them implausible. In doing so, the District Court
also determined that it lacked jurisdiction. But an on-the-
merits judgment can still trigger the judgment bar, even if
that determination necessarily deprives the court of sub-
ject-matter jurisdiction.
——————
  7 We express no view on the availability of state-law immunities in this

context. Compare Medina v. United States, 259 F. 3d 220, 225, n. 2 (CA4
2001), with Villafranca v. United States, 587 F. 3d 257, 263, and n. 6
(CA5 2009).
8                    BROWNBACK v. KING

                       Opinion of the Court

   The District Court did lack subject-matter jurisdiction
over King’s FTCA claims. In most cases, a plaintiff’s failure
to state a claim under Rule 12(b)(6) does not deprive a fed-
eral court of subject-matter jurisdiction. See Steel Co. v.
Citizens for Better Environment, 523 U. S. 83, 89 (1998).
“Dismissal for lack of subject-matter jurisdiction . . . is
proper only when the claim is so . . . ‘completely devoid of
merit as not to involve a federal controversy.’ ” Ibid. How-
ever, a plaintiff must plausibly allege all jurisdictional ele-
ments. See, e.g., Dart Cherokee Basin Operating Co. v. Ow-
ens, 574 U. S. 81, 89 (2014). And in the unique context of
the FTCA, all elements of a meritorious claim are also ju-
risdictional. Meyer, 510 U. S., at 477. So even though a
plaintiff need not prove a §1346(b)(1) jurisdictional element
for a court to maintain subject-matter jurisdiction over his
claim, see ibid., a plaintiff must plausibly allege all six
FTCA elements not only to state a claim upon which relief
can be granted but also for a court to have subject-matter
jurisdiction over the claim. That means a plaintiff must
plausibly allege that “the United States, if a private person,
would be liable to the claimant” under state law both to sur-
vive a merits determination under Rule 12(b)(6) and to es-
tablish subject-matter jurisdiction. §1346(b)(1). Because
King’s tort claims failed to survive a Rule 12(b)(6) motion to
dismiss, the United States necessarily retained sovereign
immunity, also depriving the court of subject-matter juris-
diction.
   Ordinarily, a court cannot issue a ruling on the merits
“when it has no jurisdiction” because “to do so is, by very
definition, for a court to act ultra vires.” Steel Co., 523 U. S.,
at 101–102. But where, as here, pleading a claim and
pleading jurisdiction entirely overlap, a ruling that the
court lacks subject-matter jurisdiction may simultaneously
be a judgment on the merits that triggers the judgment
                      Cite as: 592 U. S. ____ (2021)                       9

                           Opinion of the Court

bar.8 A dismissal for lack of jurisdiction is still a “judg-
ment.” See Restatement of Judgments §49, Comment a, at
193–194 (discussing “judgment . . . based on the lack of ju-
risdiction”). And even though the District Court’s ruling in
effect deprived the court of jurisdiction, the District Court
necessarily passed on the substance of King’s FTCA claims.
See Part II–B, supra. Under the common law, judgments
were preclusive with respect to issues decided as long as the
court had the power to decide the issue. See Restatement
of Judgments §49, Comment b, at 195–196. Because “a fed-
eral court always has jurisdiction to determine its own ju-
risdiction,” United States v. Ruiz, 536 U. S. 622, 628 (2002),
a federal court can decide an element of an FTCA claim on
the merits if that element is also jurisdictional. The Dis-
trict Court did just that with its Rule 12(b)(6) decision.9
                        *    *      *
  We conclude that the District Court’s order was a judg-
ment on the merits of the FTCA claims that can trigger the
judgment bar. The judgment of the United States Court of
Appeals for the Sixth Circuit is reversed.

                                                        It is so ordered.
——————
   8 In cases such as this one where a plaintiff fails to plausibly allege an

element that is both a merit element of a claim and a jurisdictional ele-
ment, the district court may dismiss the claim under Rule 12(b)(1) or
Rule 12(b)(6). Or both. The label does not change the lack of subject-
matter jurisdiction, and the claim fails on the merits because it does not
state a claim upon which relief can be granted. However, in other cases
that overlap between merits and jurisdiction may not exist. In those
cases, the court might lack subject-matter jurisdiction for non-merits
reasons, in which case it must dismiss the case under just Rule 12(b)(1).
   9 The District Court did not have the power to issue its summary judg-

ment ruling because that decision was not necessary for the court “to
determine its own jurisdiction.” Ruiz, 536 U. S., at 628. The court should
have assessed whether King’s FTCA claims plausibly alleged the six el-
ements of §1346(b)(1) as a threshold matter, and then dismissed those
claims for lack of subject-matter jurisdiction once it concluded they were
not plausibly alleged. See Steel Co. v. Citizens for Better Environment,
523 U. S. 83, 94–95 (1998).
                  Cite as: 592 U. S. ____ (2021)            1

                   SOTOMAYOR, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 19–546
                          _________________


  DOUGLAS BROWNBACK, ET AL., PETITIONERS v.
              JAMES KING
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE SIXTH CIRCUIT
                      [February 25, 2021]

  JUSTICE SOTOMAYOR, concurring.
  I join the Court’s opinion because I agree that the District
Court dismissed King’s Federal Tort Claims Act (FTCA)
claims on the merits. Importantly, the Court does not today
decide whether an order resolving the merits of an FTCA
claim precludes other claims arising out of the same subject
matter in the same suit. Although the parties briefed the
issue, it was not the basis of the lower court’s decision. See
ante, at 5, n. 4. I write separately to emphasize that, while
many lower courts have uncritically held that the FTCA’s
judgment bar applies to claims brought in the same action,
there are reasons to question that conclusion. This issue
merits far closer consideration than it has thus far received.
  King argues that the judgment bar merely “supplements
common-law claim preclusion by closing a narrow gap,” pre-
venting plaintiffs from bringing duplicative litigation
against first the United States and then its employees.
Simmons v. Himmelreich, 578 U. S. 621, 630, n. 5 (2016);
see also ibid. (“At the time that the FTCA was passed, com-
mon-law claim preclusion would have barred a plaintiff
from suing the United States after having sued an em-
ployee but not vice versa”). On petitioners’ view, however,
the judgment bar provides that any order resolving an
FTCA claim automatically precludes separate claims
2                    BROWNBACK v. KING

                    SOTOMAYOR, J., concurring

brought in the same action and arising from the same com-
mon nucleus of facts. This is a significant departure from
the normal operation of common-law claim preclusion,
which applies only in separate or subsequent suits follow-
ing a final judgment. See, e.g., G. & C. Merriam Co. v. Saal-
field¸ 241 U. S. 22, 29 (1916) (“Obviously, the rule for deci-
sion applies only when the subsequent action has been
brought”).
    King raises a number of reasons to doubt petitioners’
reading. Looking first to the text, the FTCA’s judgment bar
is triggered by “[t]he judgment in an action under section
1346(b).” 28 U. S. C. §2676. A “judgment” is “[a] court’s
final determination of the rights and obligations of the par-
ties in a case.” Black’s Law Dictionary 1007 (11th ed. 2019);
see also 1 H. Black, Law of Judgments §1, p. 2, n. l (1891)
(“ ‘A judgment is the final consideration and determination
of a court . . . upon the matters submitted to it’ ”). Decisions
disposing of only some of the claims in a lawsuit are not
“judgments.”
    Similarly, once the judgment bar is triggered, it precludes
“any action by the claimant.” §2676. An “action” refers to
the whole of the lawsuit. See Black’s Law Dictionary, at 37
(defining “action” as a “civil or criminal judicial proceed-
ing”); Black’s Law Dictionary 43 (3d ed. 1933) (“The terms
‘action’ and ‘suit’ are now nearly, if not entirely, synony-
mous”). Individual demands for relief within a lawsuit, by
contrast, are “claims.” See Black’s Law Dictionary, at 311
(2019) (defining a “claim” as “the part of a complaint in a
civil action specifying what relief the plaintiff asks for”);
Black’s Law Dictionary, at 333 (1933) (defining a “claim” as
“any demand held or asserted as of right” or “cause of
action”).
    Thus, giving the judgment bar’s two key terms their tra-
ditional meanings, “the judgment in an action under section
1346(b)” that triggers the bar is the final order resolving
every claim in a lawsuit that includes FTCA claims. When
                      Cite as: 592 U. S. ____ (2021)                     3

                       SOTOMAYOR, J., concurring

triggered, the judgment bar precludes later “action[s],” not
claims in the same suit. So read, the statutory judgment
bar “functions in much the same way” as claim preclusion,
“with both rules depending on a prior judgment as a condi-
tion precedent.” Will v. Hallock, 546 U. S. 345, 354 (2006).1
   Turning next to the FTCA’s purpose and effect, under
King’s reading, the judgment bar also serves the same, fa-
miliar functions as claim preclusion: “avoiding duplicative
litigation” by barring repetitive suits against employees
without “reflecting a policy that a defendant should be scot
free of any liability.” Ibid. Petitioners’ interpretation, by
contrast, appears inefficient. Precluding claims brought in
the same suit incentivizes plaintiffs to bring separate suits,
first against federal employees directly and second against
the United States under the FTCA. See Sterling v. United
States, 85 F. 3d 1225, 1228–1229 (CA7 1996) (holding that
judgment in a prior direct action did not preclude a later
FTCA suit against the United States).2
   Petitioners’ interpretation also produces seemingly un-
fair results by precluding potentially meritorious claims
when a plaintiff’s FTCA claims fail for unrelated reasons.
Here, for example, King’s constitutional claims require only
——————
  1 Nearby §2672 could further support this interpretation. That section

provides that an administrative settlement with the United States “shall
constitute a complete release of any claim against the United States and
against the employee of the government” who committed the tort. Unlike
the judgment bar, §2672 uses unambiguous language (“release of any
claim”) to ensure that settlements with the United States both preclude
future litigation and resolve pending claims against federal employees.
Had Congress intended to give both provisions the same effect, “it pre-
sumably would have done so expressly.” Russello v. United States, 464
U. S. 16, 23 (1983).
  2 Some courts have held that precluding claims in the same action pre-

vents plaintiffs from recovering for the same injury from both the United
States and the federal employee. The law, however, already bars double
recovery for the same injury. See, e.g., Zenith Radio Corp. v. Hazeltine
Research, Inc., 401 U. S. 321, 348 (1971) (“[T]he law . . . does not permit
a plaintiff to recover double payment”).
4                   BROWNBACK v. KING

                   SOTOMAYOR, J., concurring

a showing that the officers’ behavior was objectively unrea-
sonable, while the District Court held that the state torts
underlying King’s FTCA claims require subjective bad
faith. If petitioners are right, King’s failure to show bad
faith, which is irrelevant to his constitutional claims,
means a jury will never decide whether the officers violated
King’s constitutional rights when they stopped, searched,
and hospitalized him.
   There are, of course, counterarguments. On the text, pe-
titioners point out that it would be strange to refer to the
entire lawsuit as “an action under section 1346(b)” even af-
ter the Court has decided all the claims brought under the
FTCA. Better, they argue, to read “judgment in an action
under section 1346(b)” to mean any order resolving all the
FTCA claims in the suit. They urge further that claims in
the same suit should be among the covered actions because
the bar precludes “any action,” rather than “subsequent” ac-
tions, which is the typical formulation of claim preclusion.
As to the judgment bar’s purpose, petitioners contend that
the FTCA gives tort claimants a choice that comes with a
cost: They can sue the United States and access its deeper
pockets, but, if they do, then the outcome of the FTCA
claims resolves the entire controversy. This preserves fed-
eral resources while allowing tort claimants to decide
whether to bring FTCA claims at all.
   There are naturally counterarguments to those counter-
arguments, and so on, but further elaboration here is un-
necessary. As the Court points out, “ ‘we are a court of re-
view, not of first view.’ ” Ante, at 5, n. 4 (quoting Cutter v.
Wilkinson, 544 U. S. 709, 718, n. 7 (2005)). While lower
courts have largely taken petitioners’ view of the judgment
bar, few have explained how its text or purpose compels
that result. In my view, this question deserves much closer
analysis and, where appropriate, reconsideration.

```

---
