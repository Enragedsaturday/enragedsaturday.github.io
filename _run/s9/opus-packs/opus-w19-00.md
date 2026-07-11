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

## GROUP: _overhaul2/lake/cases/United States v. Payne.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Payne
type: case
citation: "99 F.4th 495 (2024)"
parallel_cite: ""
neutral_cite: ""
court: 9th Cir. 2024
court_level: coa
circuit: ca9
year: 2024
date_decided: 2024-04-17
docket: 22-50262
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
  opinion_url: "https://www.courtlistener.com/opinion/9494371/united-states-v-jeremy-payne/"
  cluster_id: 9494371
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Payne
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: Key
related:
  - "[[Special Needs and Administrative Searches]]"
  - "[[Samson v. California]]"
  - "[[Riley v. California]]"
  - "[[United States v. Knights]]"
tags:
  - case
  - fourth-amendment
  - fifth-amendment
  - parole-search
  - suspicionless-search
  - cell-phone
  - biometric-unlock
  - ninth-circuit
holding: "A California parolee is subject to a valid suspicionless search condition, and because parole searches require no probable cause as to the place or thing searched, CHP officers who stopped Payne for a traffic violation and, learning he was a parolee, searched his cell phone acted reasonably; the court declined to extend Riley — a search-incident-to-arrest case — to parole searches of a cell phone, and separately held that compelling Payne to unlock the phone with his thumbprint did not violate the Fifth Amendment because the act was non-testimonial."
aliases:
  - United States v. Payne
  - "United States v. Payne (9th Cir. 2024)"
---

# United States v. Payne

*99 F.4th 495 (9th Cir. 2024)* (No. 22-50262) · U.S. Court of Appeals for the Ninth Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 9494371 → lead opinion 9960984 (99 F.4th 495, decided 2024-04-17); Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — CL text is slip-paginated). S9 promotes. -->

## Background
California Highway Patrol officers stopped Jeremy Payne for a vehicle-code window-tint violation. During the stop they learned he was a California parolee subject to a search condition. After finding nothing illegal on his person or in the car, an officer searched Payne's cell phone — compelling him to unlock it by grabbing his thumb and pressing it to the sensor while Payne was handcuffed in the back of a patrol vehicle — and reviewed his photos, videos, and maps, uncovering evidence. Payne moved to suppress, arguing the phone search was an unreasonable parole search and that compelling the biometric unlock violated his Fifth Amendment privilege. The district court denied the motion.

## Issue
Whether the suspicionless search of a parolee's cell phone under a parole search condition was reasonable under the Fourth Amendment (and whether *[[Riley v. California|Riley]]* required otherwise), and whether compelling the parolee to unlock the phone with his fingerprint violated the Fifth Amendment.

## Rule
Parolees have a severely diminished expectation of privacy, and a search conducted pursuant to a valid parole search condition need not rest on individualized suspicion or probable cause. As the panel put it: "Parole searches, on the other hand, require no such probable cause determination as to the place or thing being searched." — 99 F.4th 495, slip op. at 20. ^pin-op20

## Application
Because Payne's statutorily mandated parole search condition independently authorized the search, and the officers displayed no arbitrary, capricious, or harassing conduct, the search of his phone was reasonable under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]. The court rejected Payne's reliance on *[[Riley v. California|Riley]]*: that decision barred warrantless cell-phone [[Search Incident to Arrest|searches incident to arrest]], but the court had already declined to extend *[[Riley v. California|Riley]]*'s reasoning to parole searches, and it declined again here — a parole search of a phone is governed by the parolee's diminished privacy interests, not by *[[Riley v. California|Riley]]*. On the Fifth Amendment, the court held that compelling Payne to press his thumb to the sensor was not testimonial: like a blood draw or a booking fingerprint, the act required no cognitive assertion and merely provided access, so it did not compel Payne to be a witness against himself.

## Conclusion
**Affirmed.** The Ninth Circuit rejected both the Fourth Amendment parole-search challenge and the Fifth Amendment compelled-unlock challenge and upheld the denial of suppression.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Payne* applies the *[[Samson v. California|Samson]]* diminished-privacy rationale to a **cell-phone** parole search: suspicionless parole searches need no probable cause, and *[[Riley v. California|Riley]]* — a search-incident-to-arrest rule — does not govern them. Its distinct **Fifth Amendment** holding (compelled biometric unlock is non-testimonial) belongs to the self-incrimination materials; here, teach the parole/administrative-search rationale and the boundary between *[[Riley v. California|Riley]]* and suspicionless supervision searches.

## Appears on
- [[Special Needs and Administrative Searches]] — *Key*

## Sources
- [*United States v. Payne*, 99 F.4th 495 (9th Cir. 2024)](https://www.courtlistener.com/opinion/9494371/united-states-v-jeremy-payne/) — pinpoint: slip op. at 20 (parole searches require no probable cause; *Riley* not extended to parole phone searches; the CL opinion text carries slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7e7c4710b2ae5eec", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Payne"}, "payload": {"all": [{"cite": "99 F.4th 495", "page": "495", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "99"}], "display": "99 F.4th 495", "official": {"cite": "99 F.4th 495", "page": "495", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "99"}, "official_selection_present": true, "record_id": "United States v. Payne"}}
{"assertion_id": "28278bc60338c485", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Payne"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Payne", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Payne

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Payne",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Jeremy Payne",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Payne",
    "court": "9th Cir. 2024",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": "2024-04-17",
    "year": 2024,
    "docket": "22-50262",
    "cluster_id": 9494371,
    "lead_opinion_id": 9960984,
    "sibling_ids": [],
    "absolute_url": "/opinion/9494371/united-states-v-jeremy-payne/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "99 F.4th 495",
      "volume": "99",
      "reporter": "F.4th",
      "page": "495",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "99 F.4th 495",
        "volume": "99",
        "reporter": "F.4th",
        "page": "495",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "99 F.4th 495",
    "official_selection": {
      "court_class": "state",
      "selected": "99 F.4th 495",
      "reason": "selected_rank_3"
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
    "date_created": "2026-07-06T05:57:18Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:57:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:57:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:57:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:57:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-payne--9494371",
      "to_record_id": "United States v. Payne",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Payne

```
                     FOR PUBLICATION

     UNITED STATES COURT OF APPEALS
          FOR THE NINTH CIRCUIT

UNITED STATES OF AMERICA,                          No. 22-50262

                 Plaintiff-Appellee,             D.C. No. 5:22-cr-
                                                   00054-PA-1
    v.

JEREMY TRAVIS PAYNE, AKA                             OPINION
Jeramey Travis Payne,

                 Defendant-Appellant.

         Appeal from the United States District Court
            for the Central District of California
          Percy Anderson, District Judge, Presiding

           Argued and Submitted February 14, 2024
                    Pasadena, California

                       Filed April 17, 2024

    Before: Richard C. Tallman and Consuelo M. Callahan,
     Circuit Judges, and Robert S. Lasnik, * District Judge.

                   Opinion by Judge Tallman

*
 The Honorable Robert S. Lasnik, United States District Judge for the
Western District of Washington, sitting by designation.
2                          USA V. PAYNE


                          SUMMARY **


                          Criminal Law

   The panel affirmed the district court’s denial of Jeremy
Travis Payne’s motion to suppress evidence.
    Payne, a California parolee, was arrested and charged
with possession with intent to distribute fentanyl,
fluorofentanyl, and cocaine. After the district court denied
his motion to suppress evidence of these crimes that
California Highway Patrol officers had recovered from a
house in Palm Desert, California, he entered a conditional
guilty plea to possession of fentanyl with intent to distribute.
    The panel held that the CHP officers did not violate the
Fourth Amendment in their search, during a traffic stop, of
Payne’s cell phone, made possible by the officers’ forced use
of his thumb to unlock the device. The panel held that,
despite the language of a special search condition of Payne’s
parole, requiring him to surrender any electronic device and
provide a pass key or code, but not requiring him to provide
a biometric identifier to unlock the device, the search was
authorized under a general search condition, mandated by
California law, allowing the suspicionless search of any
property under Payne’s control. The panel concluded that
any ambiguity created by the special condition, when
factored into the totality of the circumstances, did not
increase Payne’s expectation of privacy in his cell phone to
render the search unreasonable under the Fourth
Amendment. The panel further held that the search of the

**
  This summary constitutes no part of the opinion of the court. It has
been prepared by court staff for the convenience of the reader.
                        USA V. PAYNE                        3


cell phone was not unreasonable on a theory that it violated
California’s prohibition against arbitrary, capricious, or
harassing searches. In addition, the search of Payne’s
photos, videos, and maps on his cell phone did not run afoul
of Riley v. California, which held that officers cannot search
the contents of an individual’s cell phone incident to their
arrest, because Riley does not apply to parole searches of a
cell phone.
     The panel held that the CHP officers did not violate
Payne’s Fifth Amendment privilege against self-
incrimination when they compelled him to unlock his cell
phone using his fingerprint. Payne established that the
communication       at    issue     was    compelled       and
incriminating. The panel held, however, that the compelled
use of a biometric to unlock an electronic device was not
testimonial because it required no cognitive exertion, placing
it in the same category as a blood draw or a fingerprint taken
at booking, and merely provided the CHP with access to a
source of potential information. Accordingly, the Fifth
Amendment did not apply.
    The panel held that there was sufficient probable cause
to support issuance of a search warrant without regard to
observations CHP officers made during a challenged
protective sweep of the Palm Desert House.
4                       USA V. PAYNE


                         COUNSEL

Caroline S. Platt (argued), Assistant Federal Public
Defender; Cuauhtemoc Ortega, Federal Public Defender;
Federal Public Defender’s Office, Los Angeles, for
Defendant-Appellant.
Haoxiaohan H. Cai (argued), Assistant United States
Attorney, General Crimes Section; Bram M. Alden,
Assistant United States Attorney, Chief, Criminal Appeals
Section; E. Martin Estrada, United States Attorney; United
States Department of Justice, Office of the United States
Attorney, Los Angeles, California, for Plaintiff-Appellee.


                         OPINION

TALLMAN, Circuit Judge:

    Appellant Jeremy Travis Payne was a California parolee
when he was arrested and charged with three counts of
possession with intent to distribute fentanyl, fluorofentanyl,
and cocaine. After the district court denied Payne’s motion
to suppress evidence of these crimes recovered from a home
in Palm Desert, California, Payne entered a conditional
guilty plea to possession of fentanyl with intent to distribute
at least 40 grams in violation of 21 U.S.C. § 841(a)(1),
(b)(1)(B)(vi). On appeal, Payne challenges the district
court’s denial of his motion to suppress, arguing that
California Highway Patrol (“CHP”) officers violated his
Fourth and Fifth Amendment rights.
                            USA V. PAYNE                              5


                                   I
    In November 2018, Payne was arrested for assault with
a deadly weapon on a peace officer, in violation of Cal. Penal
Code § 245(c).      He was sentenced to three years
imprisonment and later released on parole. On September
23, 2020, Payne signed a one-page “Notice and Conditions
of Parole” document and a separate, three-page “Special
Conditions of Parole” document. Pursuant to Cal. Penal
Code § 3067(b)(3) and 15 Cal. Code Regs. § 2511(b)(4),
Payne’s Notice and Conditions of Parole included the
following condition (“general search condition”) 1:

        You, your residence, and any property under
        your control are subject to search or seizure
        by a probation officer, an agent or officer of
        the California Department of Corrections and
        Rehabilitation, or any other peace officer, at
        any time of the day or night, with or without
        a search warrant, with or without cause.

Payne’s Special Conditions of Parole included a more
detailed condition (“special search condition”) concerning
electronic devices:

        You shall surrender any digital/electronic
        device and provide a pass key/code to unlock
        the device to any law enforcement officer for
        inspection other than what is visible on the
        display screen.        This includes any

1
 This general search condition is “mandated as a term of every parolee’s
release” in the State of California. People v. Delrio, 259 Cal. Rptr. 3d
301, 305 (Ct. App. 2020); see People v. Schmitz, 288 P.3d 1259, 1264–
65 (Cal. 2012).
6                       USA V. PAYNE


       digital/electronic device in your vicinity.
       Failure to comply can result in your arrest
       pending further investigation and/or
       confiscation of any device pending
       investigation.

    On November 3, 2021, CHP officers Coddington and
Garcia—who were both assigned to the Coachella Valley
Violent Crime Gang Taskforce—were patrolling an area in
Desert Hot Springs, California. They saw a gold Nissan with
what they perceived to be unlawfully tinted front windows
and initiated a traffic stop for a suspected violation of Cal.
Veh. Code § 26708. Officer Coddington approached the
vehicle and asked the driver, Payne, to provide his driver’s
license, vehicle registration, and proof of insurance. Officer
Coddington later reported that Payne was “extremely
nervous,” “trembling as he fumbled for the documents,”
“sweating profusely,” and “stammering when he spoke.”
Payne informed the officers that he was on California parole.
After confirming Payne’s California parole status with
Riverside County Sheriff’s Dispatch, Officer Coddington
asked Payne and his female passenger to get out of the car.
Payne was handcuffed and eventually detained in the back
of a squad car.
    Officers searched Payne’s person pursuant to his parole
conditions and found in his pockets $1,270 cash and a key
ring with several keys, including a key to a BMW. After
searching the vehicle, Officer Coddington asked Payne if he
had a phone. Payne responded that “his phone was in the
driver’s door panel and was green in color.” The phone was
where Payne said it would be. Officer Coddington retrieved
it and asked Payne to provide the passcode. Despite
confirming that he had a phone, and informing officers of its
                            USA V. PAYNE                              7


location and color, Payne changed his story and began
denying ownership, stating “the phone was not his and he
did not have the password.”
    At this juncture, CHP officers would have been justified
under Payne’s special search condition in either
“confiscati[ng] . . . [the] device” or “arrest[ing] Payne
pending further investigation.” Instead, Officer Coddington
forcibly grabbed Payne’s thumb and used it to unlock the
phone via a built-in biometric unlocking feature. 2 Once
unlocked, Officer Coddington opened the phone’s settings
and confirmed that Payne’s full name was listed in the
owner’s information section. Next, he began looking
through the device’s stored media and found two important
videos.
    The first video was recorded on the phone the same day,
November 3, 2021, just three hours before the traffic stop. It
showed the inside of a room with what Officer Coddington
believed to be “a large amount of U.S. currency, several bags
of blue pills (suspected to be fentanyl), and a gold-colored
money counting machine.” An individual, who Officer
Coddington presumed was Payne, could be heard on the
video referring to the room as his “office.” The second video
was taken outside of a residence with a gray-brick wall
around the front. Again, an individual, who Officer
Coddington presumed was Payne, could be heard saying
“life is good in Palm Desert” and “I got the Beamer out


2
 Whether Officer Coddington forcibly used Payne’s thumb to unlock the
phone or Payne “reluctantly unlocked the cell phone using his thumb
print” was disputed before the district court. For the purposes of this
appeal, however, the government—both in its answering brief and during
oral argument—accepted the defendant’s version of the facts, i.e., “that
defendant’s thumbprint was compelled.”
8                        USA V. PAYNE


front,” referring to a parked BMW vehicle shown in the
video.
    Finally, Officer Coddington opened the maps application
on Payne’s cell phone, which showed a pin dropped to a
parked vehicle on a street called El Cortez Way in Palm
Desert, California, about twenty-five miles away. Despite
what Officer Coddington found on the phone concerning the
parked car in Palm Desert, Payne insisted that he resided
with his mother at her home in Indio, California; Payne’s
female passenger told officers the same thing in a later
interview. Based on what CHP officers found on Payne’s
person and phone, they drove Payne to the location of the
parked car on El Cortez Way.
    When the officers arrived, they saw a silver BMW
parked in front of a house. The car was registered to Payne
and the BMW key recovered from Payne’s person unlocked
it. Before obtaining a warrant, Officer Coddington walked
to the front door of what was marked Unit B and unlocked
the door with one of the keys from Payne’s keyring. Officers
entered the home and conducted what they reported as a
“security sweep” to “make sure there was no one inside the
residence who could possibly come out of the residence and
harm [the officers].” During this initial search of the home,
officers observed in plain sight several bags of blue pills they
suspected of being fentanyl and a money-counting machine,
consistent with what they had earlier observed in the first
video on Payne’s cell phone.
     Officer Coddington then wrote a search warrant
application for the house on El Cortez Way. The application
listed all the information that Officer Coddington had
learned from his search of Payne’s cell phone. The
application also attested that Officer Coddington:
                        USA V. PAYNE                       9


(1) observed a BMW outside of Payne’s residence that the
key recovered from Payne’s person unlocked; (2) confirmed
the BMW was registered to Payne; (3) accessed Unit B with
another key on Payne’s keyring; and (4) saw several bags of
blue pills (suspected to be fentanyl) and a gold money-
counting machine during the initial sweep of the residence.
Two hours later, a Riverside County Superior Court judge
authorized the search warrant.
    The search of El Cortez Way under the authority of that
warrant was more thorough. Officers found several
documents, including pieces of mail, bearing Payne’s full
name. They also discovered a “white powdery substance”
throughout the home and a total of 104.3 grams of blue pills
marked “M/30.” The pills and powder were later confirmed
to be fentanyl, fluorofentanyl, and cocaine. In addition to
the drugs, officers recovered a total of $13,992 in cash, a
digital scale, the gold money-counting machine, and six cell
phones. Payne was arrested following the second search.
    On February 23, 2022, a federal grand jury returned an
indictment charging Payne with: (1) possession with intent
to distribute a mixture and substance containing fentanyl in
violation of 21 U.S.C. § 841(a)(1), (b)(1)(B)(vi);
(2) possession with intent to distribute fluorofentanyl in
violation of 21 U.S.C. § 841(a)(1), (b)(1)(C); and
(3) possession with intent to distribute cocaine in violation
of 21 U.S.C. § 841(a)(1), (b)(1)(C). Payne filed a motion to
suppress the evidence seized from the house on El Cortez
Way on April 25, 2022. He primarily argued that the
searches of his phone and the house on El Cortez Way
violated his Fourth and Fifth Amendment rights.
   The district court denied Payne’s motion in an oral ruling
on May 24, 2022. The court found that the search of Payne’s
10                      USA V. PAYNE


cell phone was reasonable under the Fourth Amendment
given that Payne was on parole in California and subject to
California’s standard search conditions that covered his
electronic devices. Further, the court determined that the
compelled use of Payne’s thumb to access the phone was a
nontestimonial act, placing it outside of Payne’s Fifth
Amendment privilege against self-incrimination. The court
found no separate Fourth Amendment violation for the first,
warrantless search of the house on El Cortez Way for two
reasons. First, because the search was justified under
Payne’s parole conditions and, second, because the search
warrant officers later obtained would have still been valid
after excising the information included in the warrant
application from the protective sweep of the home.
    Payne was sentenced on November 7, 2022, to 144
months in prison. After the district court entered final
judgment, Payne filed a timely notice of appeal. We have
jurisdiction under 28 U.S.C. § 1291.
                             II
    We begin with Payne’s Fourth Amendment challenges
to the CHP officers’ search of his cell phone. Given Payne
raises his Fourth Amendment claim in the context of a
challenge to the district court’s denial of his motion to
suppress, we review the denial of that motion de novo and
the district court’s factual findings for clear error. United
States v. Sullivan, 797 F.3d 623, 632–33 (9th Cir. 2015).
    The general suspicionless search condition in Payne’s
Notice and Conditions of Parole is mandated by California
law. See Cal. Penal Code § 3067(b)(3); 15 Cal. Code Regs.
§ 2511(b)(4). The California Supreme Court held the
condition was reasonable under the Fourth Amendment, in
large part because parolees, who enjoy only “conditional
                        USA V. PAYNE                        11


freedom,” have a significantly diminished expectation of
privacy, while the government has a strong interest in
assessing parolees’ rehabilitation and reentry while
simultaneously protecting the public. People v. Reyes, 968
P.2d 445, 450–51 (Cal. 1998); People v. Bryant, 491 P.3d
1046, 1054 (Cal. 2021) (“[A] warrantless search of a
parolee’s property or residence . . . is per se reasonable.”);
see also United States v. Johnson, 875 F.3d 1265, 1275 (9th
Cir. 2017). The Supreme Court of the United States agreed,
upholding suspicionless searches of parolees based on the
totality of the circumstances provided they are not “arbitrary,
capricious, or harassing.” Samson v. California, 547 U.S.
843, 856–57 (2006). In the years since Samson, we have
made clear that suspicionless parolee searches that
“compl[y] with the terms of a valid search condition will
usually be deemed reasonable under the Fourth
Amendment.” United States v. Cervantes, 859 F.3d 1175,
1183 (9th Cir. 2017).
    Our more recent cases have articulated the narrow set of
constraints that apply to law enforcement officers
conducting suspicionless parole searches. First, the officer
conducting the parole search must have probable cause to
believe “that the individual to be searched is on active
parole, and an applicable parole condition authorizes the
search or seizure at issue.” United States v. Estrella, 69
F.4th 958, 972 (9th Cir. 2023). Second, those searches
cannot be “arbitrary, capricious, or harassing.” Id. (internal
quotations and citations omitted); Reyes, 968 P.2d at 450;
see Cal. Penal Code § 3067(d) (“It is not the intent of the
Legislature to authorize law enforcement officers to conduct
searches for the sole purpose of harassment.”).
   Payne raises two distinct, yet inexorably entwined,
arguments: (1) that the officers on scene during the traffic
12                          USA V. PAYNE


stop used “unreasonable means” to unlock his phone
considering the language of his special search condition;3
and (2) that the search was arbitrary, capricious, or
harassing.
                                  A
    Payne’s unreasonable means argument most closely
implicates the principle, from Estrella, that officers must
have probable cause to believe an individual is on parole and
subject to an applicable parole condition that authorizes the
search at issue. 69 F.4th at 972. Here, the search at issue is
of Payne’s phone, made possible by the forced use of
Payne’s thumb to unlock the device. Payne posits the
question of whether CHP officers complied with the precise
terms of his parole conditions when they searched his cell
phone as a threshold one. In other words, he argues that the
parole search exception to the warrant requirement cannot
apply when officers do not follow the precise terms or
commands of a parole condition. He points to the language
in special parole condition number sixty-four for support,
which compelled Payne to surrender his cell phone to any
law enforcement officer for inspection and “provide [the]
pass key/code to unlock the device.” It further states that
“[f]ailure to comply can result in your arrest pending further
investigation and/or confiscation of any device pending

3
  Invoking Fed. R. Crim. P. 12, the government argues that Payne
forfeited his “unreasonable means” argument because he failed to
squarely present it in his motion to suppress. However, Payne’s
argument centers on the precise language of his parole conditions, which
was presented to and analyzed by the district court during the
suppression hearing. See United States v. Magdirila, 962 F.3d 1152,
1155–57 (9th Cir. 2020). Because Payne’s argument does not rely on
new facts or wholly distinct legal theories, we decline to deem it
forfeited.
                         USA V. PAYNE                        13


investigation.” Relying on the condition’s plain language,
Payne argues that the officers could not use his thumb to
unlock his phone when he refused to provide the numerical
passcode—their only recourse was to confiscate the device
or arrest him pending investigation, as outlined in the special
search condition.
    Textually, Payne’s unreasonable means argument has
certain cogency. The special search condition did not
require Payne to provide a biometric identifier to unlock any
electronic devices in his vicinity and it did include an express
enforcement provision. However, Payne’s argument suffers
from two fatal flaws. First, it ignores the more general,
statutorily mandated search condition included in his—and
every California parolee’s—Notice of Conditions of Parole.
Second, Payne’s proposed approach decouples the analysis
from the “totality of the circumstances” and
“reasonableness” inquiries that form the foundation of our
Fourth Amendment jurisprudence, including in the parolee
search context. See, e.g., Brigham City, Utah v. Stuart, 547
U.S. 398, 403 (2006); United States v. Knights, 534 U.S.
112, 118 (2001).
    While Payne’s special search condition addresses
electronic devices specifically, his general search condition,
mandated by California law, states that “any property under
[Payne’s] control are subject to search or seizure by . . . any
other peace officer, at any time of the day or night, with or
without a search warrant, with or without cause.” We have
before held that California’s statutory framework governing
the suspicionless search of parolees authorizes officers to
conduct warrantless searches of parolees’ cell phones. See
Johnson, 875 F.3d at 1275. The language of California’s
general search condition, written into all California parole
notices, is abundantly clear, putting parolees like Payne on
14                      USA V. PAYNE


notice that their person, home, phone, and other belongings
may be searched at any time without cause or a warrant. This
“clear and unambiguous search condition” serves to
“significantly diminish[] [parolees’] reasonable expectation
of privacy.” Samson, 547 U.S. at 852. Thus, under the
general search condition of Payne’s parole, he did not have
an “expectation of privacy that society would recognize as
legitimate” in the contents of his cell phone. Id. The
question then becomes whether the inclusion of the special
search condition in any way alters that reality.
    In applying Supreme Court precedent governing
warrantless parolee and probationer searches, we have
acknowledged that officers are generally required to conduct
these searches pursuant to valid search conditions. In United
States v. Caseres, we held that warrantless parole searches
do not withstand scrutiny when officers are unaware that
§ 3067, or a similar parole search statute or condition,
applies. 533 F.3d 1064, 1076 (9th Cir. 2008). Caseres drew
on well-founded concerns that officers could seek to use
broad parole search conditions—discovered to apply only
after a warrantless search took place—to retroactively justify
their actions. See id.; Samson, 547 U.S. at 856 n.5 (“[A]n
officer would not act reasonably in conducting a
suspicionless search absent knowledge that the person
stopped for the search is a parolee.”); Moreno v. Baca, 431
F.3d 633, 641 (9th Cir. 2005) (“[P]olice officers cannot
retroactively justify a suspicionless search and arrest on the
basis of an after-the-fact discovery of . . . a parole
condition.”); Fitzgerald v. City of Los Angeles, 485 F. Supp.
2d 1137, 1143 (C.D. Cal. 2007) (“[A]dvance knowledge of
a parolee’s status is critical to the constitutionality of a
suspicionless search of a parolee.”). These cases, on which
Caseres relied, did not hold that officers must have
                        USA V. PAYNE                       15


knowledge of the exact language of a parole condition.
Rather, they focused on whether the searching officers had
knowledge of a parolee’s status.
    In Estrella, we refined the prior knowledge language
from Caseres to mean that an officer must have both:
(1) “probable cause to believe that an individual is on active
parole before conducting a suspicionless search,” and
(2) probable cause to believe that “an applicable parole
condition authorizes the search . . . at issue.” 69 F.4th at
971–72. We opted for this standard, in lieu of an “actual
knowledge” standard, on the basis that the Fourth
Amendment “calls for reasonable determinations, and does
not demand certainty.” Id. at 968 (citing Hill v. California,
401 U.S. 797, 804 (1971)).
    Our decisions in Caseres and Estrella do not support
Payne’s proposition that the officers were compelled to
follow the special search condition to the letter or that the
special search condition served to override the general
search condition. Instead, they support the government’s
position that the general search condition authorized the
search of Payne’s cell phone. If we were to accept Payne’s
proposition, it would impose an impractical burden on
officers in the field to study a parolee’s specific parole
conditions before conducting the investigations they deem
necessary based on the circumstances with which they are
confronted. See Estrella, 69 F.4th at 968 (noting that
officers cannot be expected to possess “‘up-to-the-minute’
information of a parolee’s status before proceeding with a
routine compliance check”).
   Here, having confirmed Payne’s California parole status
with the Riverside County Sheriff’s dispatch, Officer
Coddington was on notice of Payne’s general search
16                      USA V. PAYNE


condition, which subjected all “property under [Payne’s]
control” to “search or seizure . . . at any time of the day or
night, with or without a search warrant, with or without
cause.” As a California officer, dealing with a California
parolee, he reasonably believed that §§ 3067(b)(3) and
2511(b)(4) authorized him to search Payne, his vehicle, and
his belongings, including his cell phone. The search was
thus independently justified under Payne’s general search
condition.
    That Payne was also subject to a special electronic
device search condition, of which Officer Coddington was
also aware, does not place the search of Payne’s cell phone
outside of the realm of reasonableness, even considering the
way Officer Coddington accessed its contents. In Delrio, the
California Court of Appeal considered the interplay between
California’s mandatory search conditions and other various
special conditions to which a parolee may be subjected. See
People v. Delrio, 259 Cal. Rptr. 3d 301, 304–09 (Ct. App.
2020). There, the court found that special conditions of
California parole, like special condition sixty-four in
Payne’s case, “do not appear intended to set restrictions on
the searches and seizures authorized by Penal Code section
3067, subdivision (b)(3), or to elevate a parolee’s
expectations of privacy.” Id. at 308. Instead, the court saw
the terms as interposing additional penalties for possible
parole violations. Id. (“When such special conditions are
selected, the parolee’s failure to adhere may give rise to
parole violation charges . . . .”). We agree.
   As Payne would have it, CHP officers’ only recourse for
Payne’s refusal to provide his numerical passcode would
have been the two options textually set forth in his special
parole condition: “arrest pending further investigation
and/or confiscation of any device pending investigation.”
                        USA V. PAYNE                        17


Payne argues that any officer conduct outside of those
measures would be per se unreasonable. But so drastically
limiting the range of permissible officer conduct based on
whether a parolee is subject to a special search condition
would lead to bizarre results. Nor do parole search
conditions have the strict textual force that Payne suggests
they should. See People v. Schmitz, 288 P.3d 1259, 1273
(Cal. 2012) (noting that the scope of a parole search is not
“strictly tied to the literal wording of the notification given
to the parolee upon release”); Delrio, 259 Cal. Rptr. 3d at
309 (“[T]he officers who performed the parole search of
defendant were not required to first ascertain and parse the
language of the [parole] form”).
    Law enforcement officers in the field can proceed with a
search under a parolee’s general search condition, assuming
that search is reasonable.        After all, the California
Department of Corrections and Rehabilitation defines
special conditions of parole as “rules imposed in addition to
the general conditions of parole,” not in place of those
general conditions. Parole Conditions, Cal. Dep’t of Corrs.
&       Rehab.,       https://www.cdcr.ca.gov/parole/parole-
conditions/ (last visited Apr. 10, 2024) (emphasis added).
These special conditions are imposed based on a parolee’s
particular offense and criminal history—i.e., aggravating
factors—and are designed as a further means by which the
department can “discourage criminal behavior.” Id. It
would thus make little sense to hold that Payne’s special
search condition materially raised his expectation of
privacy, providing him with a way to shield the contents of
his phone from officer inspection by refusing to provide his
passcode.
   At best, the special condition of Payne’s parole created
some minimal ambiguity concerning the reach of his parole
18                      USA V. PAYNE


conditions in the aggregate. In reviewing suspicionless
searches of parolees, the Supreme Court of the United States,
the Ninth Circuit, and the Supreme Court of California have
often analyzed parole conditions, their clarity, and officers’
knowledge of their express terms as factors to consider in a
comprehensive reasonableness analysis. For example, in
Samson, the Supreme Court of the United States found the
clear expression of a parole search condition as “salient,” but
still examined the search under the “totality of the
circumstances.” Samson, 547 U.S. at 852; see also Knights,
534 U.S. at 118; Johnson, 875 F.3d at 1275; People v.
Sanders, 73 P.3d 496, 506–07 (Cal. 2003). This totality of
the circumstances approach is sound, especially considering
that a parole search is an exception to the warrant
requirement, well-situated in broader Fourth Amendment
jurisprudence. See, e.g., Griffin v. Wisconsin, 483 U.S. 868,
873 (1987). With that approach in mind, we assess “on the
one hand, the degree to which [the search] intrudes upon an
individual’s privacy and, on the other, the degree to which it
is needed for the promotion of legitimate governmental
interests.” Knights, 534 U.S. at 119 (quoting Wyoming v.
Houghton, 526 U.S. 295, 300 (1999)).
    Payne’s parole status alone subjected him to a
significantly diminished expectation of privacy.        See
Johnson, 875 F.3d at 1275. With respect to his cell phone,
Payne signed and acknowledged multiple explicit parole
search conditions that required him to surrender any device
in his vicinity for search without cause. To the extent that
Payne’s special search condition created an ambiguity over
how far his general search condition could sweep, that
ambiguity may have marginally increased Payne’s
expectation of privacy in his cell phone. But any increase
based on these facts is de minimis. Payne knew he was on
                        USA V. PAYNE                       19


parole. He knew that, based on his parole conditions, all his
belongings could be searched at any time, including the
contents of his cell phone. Officer Coddington’s use of
means not specifically contemplated by Payne’s special
search condition to access a device over which Payne had no
significant privacy interest does not appear to have been
unreasonable.
    The reasonableness of the search is compounded when
Payne’s diminished privacy interest is weighed against the
government’s interest in supervising parolees. “[A] State’s
interests in reducing recidivism and thereby promoting
reintegration and positive citizenship among probationers
and parolees warrant privacy intrusions that would not
otherwise be tolerated under the Fourth Amendment.”
Samson, 547 U.S. at 853. The Supreme Court has described
this government interest as “overwhelming” based on
parolees increased propensity “to commit future criminal
offenses.” Id. (quoting Pennsylvania Bd. of Prob. & Parole
v. Scott, 524 U.S. 357, 365 (1998)). Here, the State’s already
significant interest was even greater based on Officer
Coddington’s knowledge of Payne’s assault with a deadly
weapon charge, Payne’s extreme nervousness during the
traffic stop, and Payne’s possession of over $1,000 in cash.
    Accordingly, we hold that the inclusion of Payne’s
special search condition did not vitiate the force of his
statutorily mandated general search condition, which
independently authorized the search at issue in this case.
Moreover, we hold that any ambiguity created by the
inclusion of the special condition, when factored into the
totality of the circumstances, did not increase Payne’s
expectation of privacy in his cell phone to render the search
unreasonable under the Fourth Amendment.
20                       USA V. PAYNE


                               B
    In addition to his unreasonable means argument, Payne
claims that the search of his cell phone violated California’s
prohibition against arbitrary, capricious, or harassing parole
searches.     Suspicionless parole searches that violate
California’s prohibition against arbitrary, capricious, or
harassing searches are constitutionally unreasonable.
Cervantes, 859 F.3d at 1183. This prohibition, however, is
“decidedly narrow” and only applies to situations where, for
example, a search “is based merely on a whim or caprice or
when there is no reasonable claim of a legitimate law
enforcement purpose.” Estrella, 69 F.4th at 972 (quoting
People v. Cervantes, 127 Cal. Rptr. 2d 468, 471 (Ct. App.
2002), as modified (Dec. 23, 2002)).
    Payne argues that “[o]nce the officers found nothing
illegal on [his] person or in his vehicle, that should have been
the end of the matter,” but he does not cite to any authority
suggesting that an officer’s failure to abandon their
investigation under these circumstances rises to the level of
a violation of the arbitrary, capricious, or harassing standard.
Instead, he cites cases involving the automobile exception
for the proposition that officers had no reason to search the
contents of Payne’s phone for evidence of his window tint
violation. Those cases, however, are inapposite because
officers must have probable cause to conduct a search under
the automobile exception to the warrant requirement. Parole
searches, on the other hand, require no such probable cause
determination as to the place or thing being searched.
   Finally, Payne claims that the officers’ search of his
photos, videos, and maps ran afoul of the Supreme Court’s
decision in Riley v. California, which held that officers could
not search the contents of an individual’s cell phone as
                             USA V. PAYNE                               21


incident to their arrest. 573 U.S. 373, 401 (2014). However,
we clearly rejected the argument that Riley applies to parole
searches of a cell phone in Johnson. 875 F.3d at 1273–75.
We therefore decline to extend Riley’s reasoning to the facts
of this case.
    The CHP officers who legitimately stopped Payne did so
based on their independent suspicion that Payne had violated
California’s Vehicle Code. They proceeded with their
investigation logically and appropriately after learning
Payne was a California parolee and observing his behavior.
Having failed to present any evidence that the CHP officers
who stopped Payne and eventually searched his cell phone
demonstrated any “arbitrary or oppressive conduct,” Reyes,
968 P.2d at 451 (citations omitted), we hold that the search
of Payne’s cell phone was reasonable. 4
                                   III
    Next, we consider Payne’s argument that CHP officers
violated his Fifth Amendment privilege against self-
incrimination when they compelled him to unlock his cell
phone using his fingerprint. Again, we review the district
court’s denial of Payne’s motion to suppress de novo, and its
factual findings for clear error. Sullivan, 797 F.3d at 632–
33.
    Ratified in 1791, the Fifth Amendment provides that
“[n]o person shall be . . . compelled in any criminal case to
be a witness against himself.” U.S. Const. amend. V. While


4
  To the extent that determination required the court to apply facts to law
in a way that was “essentially factual,” we discern no clear error in the
court’s conclusion. United States v. Franklin, 18 F.4th 1105, 1115 (9th
Cir. 2021) (quoting United States v. Hinkson, 585 F.3d 1247, 1259–60
(9th Cir. 2009) (en banc)).
22                      USA V. PAYNE


the precise scope of the privilege has, and continues to be,
subject to great debate, what has emerged is a three-prong
analysis, with each prong representing a standalone inquiry.
For a criminal defendant to benefit from the Fifth
Amendment privilege, there must be a “communication” at
issue that is: (1) compelled; (2) incriminating; and
(3) testimonial. See Hiibel v. Sixth Jud. Dist. Ct. of Nev.,
Humboldt Cnty., 542 U.S. 177, 189 (2004). The government
all but concedes that Payne has established the compelled
and incriminating prongs of the analysis, so we address them
only briefly.
    The district court implicitly found that CHP officers
compelled Payne to use his thumb to open the device, despite
Officer Coddington’s attestation that Payne reluctantly
opened the device on his own. For the purposes of this
appeal, the government has accepted Payne’s version of
events. Payne averred that, after he refused to give officers
his passcode, one of them “grabbed [his] thumb and
unlocked the phone.” This transpired while Payne was
handcuffed and in the back of a patrol vehicle. Compulsion
is present for Fifth Amendment purposes when,
“considering the totality of the circumstances, the free will
of the witness was overborne.” United States v. Anderson,
79 F.3d 1522, 1526 (9th Cir. 1996) (quoting United States v.
Washington, 431 U.S. 181, 188 (1977)). Based on Payne’s
version of events, the use of his thumb to unlock his phone
was compelled. He was physically restrained, in the back of
a squad car, and had already refused to provide officers with
the passcode to unlock the phone. Based on this resistance,
CHP officers took matters into their own hands, physically
selecting one of Payne’s thumbs to unlock the device.
    The use of Payne’s thumb to unlock his device was also
“incriminating.” This prong of the Fifth Amendment
                        USA V. PAYNE                        23


analysis has been interpreted to encompass “any disclosures
which the witness reasonably believes could be used in a
criminal prosecution or could lead to other evidence that
might be so used.” Kastigar v. United States, 406 U.S. 441,
445 (1972). Here, Payne could have reasonably concluded
that giving up his thumbprint, and thereby access to the vast
trove of personal information contained on his cell phone,
would lead to evidence that could be used against him in a
criminal prosecution. Indeed, that is exactly what happened.
    The more difficult question is whether the compelled use
of Payne’s thumb to unlock his phone was testimonial. To
date, neither the Supreme Court nor any of our sister circuits
have addressed whether the compelled use of a biometric to
unlock an electronic device is testimonial. Testimonial
communications are those that, “explicitly or implicitly,
relate a factual assertion or disclose information.” Doe v.
United States, 487 U.S. 201, 210 (1988). Of course, there
are no explicit communications on this record. Payne said
nothing when CHP officers used his thumb to unlock his
phone. His Fifth Amendment claim thus rests entirely on
whether the use of his thumb implicitly related certain facts
to officers such that he can avail himself of the privilege
against self-incrimination. This argument implicates two
lines of Supreme Court precedent: the physical trait cases
and the act of production doctrine.
    Compelled physical acts—i.e., those that require an
individual to serve as a “donor”—are not testimonial. The
physical trait cases have addressed circumstances where an
individual is compelled to: don a particular piece of clothing,
Holt v. United States, 218 U.S. 245, 252–53 (1910); stand in
a lineup, United States v. Wade, 388 U.S. 218, 223 (1967);
provide a handwriting or voice exemplar, Gilbert v.
California, 388 U.S. 263, 266–67 (1967) (handwriting
24                       USA V. PAYNE


exemplar); Wade, 388 U.S. at 222–23 (1967) (voice
exemplar); submit to fingerprinting, Wade, 388 U.S. at 223;
or have their blood drawn for DUI testing, Schmerber v.
California, 384 U.S. 757, 761 (1966). Each case reached the
same conclusion: not testimonial. In Schmerber, for
example, the Court recognized that history and lower court
precedent made clear that the privilege against self-
incrimination was designed to ward off “situations in which
the State seeks to . . . obtain[] the evidence against an
accused through the cruel, simple expedient of compelling it
from his own mouth.” Schmerber, 384 U.S. at 763 (internal
quotation marks omitted). Because the “[p]etitioner’s
testimonial capacities were in no way implicated” and his
“participation, except as a donor, was irrelevant to the results
of the test,” the Court held that the compelled blood draw
was not testimonial under the Fifth Amendment. Id. at 765.
    On its face, the use of Payne’s thumb to unlock his phone
appears no different from a blood draw or fingerprinting at
booking. These actions do not involve the testimonial
capacities of the accused and instead only compel an
individual to provide law enforcement with access to an
immutable physical characteristic. See Wade, 388 U.S. at
222–23. The next step of the investigation depends on the
“independent labor of [the state’s] officers.” Estelle v.
Smith, 451 U.S. 454, 462 (1981) (quoting Culombe v.
Connecticut, 367 U.S. 568, 581–82 (1961)). But Payne
maintains that the use of his thumb to unlock his phone is
fundamentally different from the compelled acts in past
physical trait cases, including the fingerprinting discussed in
Schmerber and Wade. See Schmerber, 384 U.S. at 764;
Wade, 388 U.S. at 223. According to Payne, this is because
of what the compelled use of his biometric implicitly
                              USA V. PAYNE                               25


communicated. He looks to the act of production doctrine
for support.
    Under the act of production doctrine, a purely physical
act may nonetheless be testimonial because of what it
communicates “wholly aside from the contents” of the thing
produced. Fisher v. United States, 425 U.S. 391, 410 (1976).
Although act of production cases have dealt exclusively with
responses to document subpoenas, their reasoning applies to
other situations. 5 The Supreme Court has reasoned that
producing a trove of documents in response to a subpoena
may implicitly communicate “the existence of the papers
demanded and their possession or control by the
[individual],” as well as the individual’s “belief that the
papers are those described in the subpoena.” Id. (citing
Curcio v. United States, 354 U.S. 118, 125 (1957)).
    The act of production doctrine’s triggering point
becomes clearer upon close reading of the Supreme Court’s
decisions in Doe, 487 U.S. 201, and United States v.
Hubbell, 530 U.S. 27 (2000). In Doe, the government
compelled an individual to “sign 12 forms consenting to
disclosure of any bank records respectively relating to 12
foreign bank accounts over which the Government knew or
suspected that Doe had control.” 487 U.S. at 203. However,
the consent forms did not force Doe to himself collect and

5
   The government suggests the doctrine only applies to subpoena
responses, arguing that there is “no basis to extend that doctrine to the
act of biometric unlock.” We are not so sure. The Supreme Court has
stated in its act of production jurisprudence that “[t]he difficult question
whether a compelled communication is testimonial for purposes of
applying the Fifth Amendment often depends on the facts and
circumstances of the particular case.” Doe, 487 U.S. at 214–15; see also
Fisher, 425 U.S. at 410 (noting questions of whether “tacit averments”
are testimonial “do not lend themselves to categorical answers”).
26                         USA V. PAYNE


turn over any documents. The Court held that this was not a
testimonial production, reasoning that the signing of the
forms related no information about existence, control, or
authenticity of the records that the bank could ultimately be
forced to produce. Id. at 215–16. For these reasons, the
consent forms were more akin to producing “a handwriting
sample or voice exemplar” because the act was not
“compelled to obtain ‘any knowledge [the suspect] might
have.’” Id. at 217 (quoting Wade, 388 U.S. at 222). 6 The
forms only provided the government with “access to a
potential source of evidence,” but locating the evidence itself
required “the independent labor of its officers.” Id. at 215
(internal quotation marks omitted and emphasis added).
    Hubbell, on the other hand, involved a “subpoena duces
tecum calling for the production of 11 categories of
documents.” Hubbell, 530 U.S. at 31. The suspect
eventually “produced 13,120 pages of documents and
records and responded to a series of questions that
established that those were all of the documents in his
custody or control that were responsive to the commands in
the subpoena.” Id. The Court held that this act of production
was of a fundamentally different kind than that at issue in
Doe because it was “unquestionably necessary for
respondent to make extensive use of ‘the contents of his own
mind’ in identifying the hundreds of documents responsive
to the requests in the subpoena.” Id. at 43. The “assembly
of those documents was like telling an inquisitor the

6
  Justice Stevens dissented from the majority opinion in Doe but
introduced an analogy that was central to his majority opinion in
Hubbell. He wrote that a defendant “may in some cases be forced to
surrender a key to a strongbox containing incriminating documents, but
I do not believe he can be compelled to reveal the combination to his
wall safe.” Doe, 487 U.S. at 219 (Stevens, J. dissenting).
                        USA V. PAYNE                       27


combination to a wall safe, not like being forced to surrender
the key to a strongbox.” Id. (citing Doe, 487 U.S. at 210
n.9). Thus, the dividing line between Doe and Hubbell
centers on the mental process involved in a compelled act,
and an inquiry into whether that act implicitly communicates
the existence, control, or authenticity of potential evidence.
     District courts applying Doe and Hubbell have arrived at
different conclusions on the biometric unlock question.
Payne relies heavily on a Northern District of California case
that held forced biometric unlocks violate the Fifth
Amendment. In re Residence in Oakland, Cal., 354 F. Supp.
3d 1010 (N.D. Cal. 2019) [hereinafter Oakland]. There, a
magistrate judge determined the act of production doctrine
applied for two primary reasons. First, because compelling
an individual to unlock a device with a biometric identifier
is the functional equivalent of compelling that person to turn
over their alphanumeric passcode, an act that is generally
accepted to be protected by the Fifth Amendment because it
requires an individual to divulge the contents of his mind.
Id. at 1015–16 (“[I]f a person cannot be compelled to
provide a passcode because it is a testimonial
communication, a person cannot be compelled to provide
one’s finger, thumb, iris, face, or other biometric feature to
unlock that same device.”). Second, because the act
instantly concedes “that the phone was in the possession and
control of the suspect, and authenticates ownership or access
to the phone and all of its digital contents.” Id. at 1016.
Other district courts have come to similar conclusions. See,
e.g., United States v. Wright, 431 F. Supp. 3d 1175, 1187–
88 (D. Nev. 2020); In re Single-Family Home & Attached
Garage, No. 17 M 85, 2017 WL 4563870, at *7 (N.D. Ill.
Feb. 21, 2017).
28                          USA V. PAYNE


     Still other district courts have come to the opposite
result. Addressing the Oakland court’s reasoning, these
cases assert that whether a passcode and a fingerprint unlock
are functional equivalents is an observation with no legal
significance to the Fifth Amendment analysis. See In re
Search Warrant No. 5165, 470 F. Supp. 3d 715, 734 (E.D.
Ky. 2020) (“The Court stands by the unambiguous
distinction in both the law and common sense between
something intangibly held in the most sacred of places—
one’s own mind—and an immutable physical
characteristic.”). Moreover, responding to the argument that
“if the device unlocks, then the incriminating inference is
that the person had possession or control of the device,”
these courts note that such a line of analysis improperly
conflates the incrimination prong with the testimonial prong.
See In re Search Warrant Application for [redacted text],
279 F. Supp. 3d 800, 805 (N.D. Ill. 2017). They ultimately
conclude that biometric unlock cases are no different than
other physical trait cases, like subjecting an individual to
fingerprinting or drawing a person’s blood, because the acts
at issue “do not themselves communicate anything.” Id. 7
    In Payne’s case, the Fifth Amendment question
stemming from the compelled use of his thumb to unlock his
phone bears striking resemblance to Justice Steven’s key vs.
combination analogy. While providing law enforcement
officers with a combination to a safe or passcode to a phone
would require an individual to divulge the “contents of his

7
  State courts are equally split on the issue. Compare, e.g., State v.
Pittman, 479 P.3d 1028, 1040–43 (Or. 2021) (unlocking phone using
biometrics is testimonial), with State v. Diamond, 905 N.W.2d 870, 874–
78 (Minn. 2018) (unlocking phone using biometrics is not testimonial);
People v. Ramirez, 316 Cal. Rptr. 3d 520, 544–50 (Ct. App. 2023)
(same).
                        USA V. PAYNE                        29


own mind,” turning over a key to a safe or a thumb to unlock
a phone requires no such mental process. Hubbell, 530 U.S.
at 43. To say that a passcode and a biometric are equivalents
and thus cannot receive different treatment under the law is
a syllogistic fallacy. The logic goes: biometrics are the
equivalent of or a substitute for a passcode and passcodes are
protected under the Fifth Amendment, so, biometrics are
also protected under the Fifth Amendment. The flaw lies in
the fact that the Supreme Court has framed the question
around whether a particular action requires a defendant to
divulge the contents of his mind, not whether two actions
yield the same result. See Hubbell, 530 U.S. at 43. The
functional equivalent argument attempts to make an end run
around this central piece of the Fifth Amendment inquiry.
When Officer Coddington used Payne’s thumb to unlock his
phone—which he could have accomplished even if Payne
had been unconscious—he did not intrude on the contents of
Payne’s mind.
    While we find the fact that there was no “cognitive
exertion” on Payne’s part most determinative, In re Search
of [redacted] Washington, D.C., 317 F. Supp. 3d 523, 538
(D.D.C. 2018), the relative level of existence, control, and
authentication established through a biometric unlock
compared to a comprehensive response to a subpoena is also
instructive. See Hubbell, 530 U.S. at 43. Payne concedes
that “the use of biometrics to open an electronic device is
akin to providing a physical key to a safe,” but argues it is
nonetheless a testimonial act because it “simultaneously
confirm[s] ownership and authentication of its contents.”
However, Payne was never compelled to acknowledge the
existence of any incriminating information. He merely had
to provide access to a source of potential information, just as
was the case in Doe and Schmerber. See Doe, 487 U.S. at
30                      USA V. PAYNE


215; Schmerber, 384 U.S. at 765. The officers were left to
identify any incriminating evidence through their own
investigation. This is decidedly unlike Hubbell, where the
subpoena respondent was implicitly conceding the
“existence, authenticity, and custody” of specific documents
that prosecutors could use in building its case against the
respondent. Hubbell, 530 U.S. at 41–42.
    One can imagine how Payne’s case might alternatively
fit more neatly in the Hubbell framework. For example, had
officers somehow compelled Payne to cull through the
information in his phone and produce any photos or videos
that demonstrated his participation in fentanyl trafficking,
there may have been a testimonial act of production.
Turning over those photos or videos would implicitly
concede that Payne had such videos, that they depicted what
the officers were looking for, and that they related to his
specific activities. Obviously, that is not the case here.
     The Supreme Court has also observed that implicit
authentication is the “prevailing justification” for extending
Fifth Amendment protection to acts of documentary
production because responding to a subpoena may be akin to
requiring a suspect to “implicitly testif[y] that the evidence
he brings forth is in fact the evidence demanded.” Fisher,
425 U.S. at 412 n.12 (internal quotations omitted) (quoting
Couch v. United States, 409 U.S. 322, 346 (1973) (Marshall,
J., dissenting)). But “[t]he fact that an individual is able to
unlock a phone with a physical characteristic does not
automatically make each individual set of data, such as
photos, videos . . . immediately authentic.” In re Search
Warrant Application for the Cellular Telephone in United
States v. Barrera, 415 F. Supp. 3d 832, 841 (N.D. Ill. 2019).
Authentication is not established in the same way here
compared to a response to a subpoena where the respondent
                        USA V. PAYNE                      31


is essentially stating the “item is what the proponent claims
it is.” Id. (quoting Fed. R. Evid. 901(a)). Phones like
Payne’s “can often be programmed to use multiple
individuals’ biometrics.” In re Search Warrant No. 5165,
470 F. Supp. 3d at 733. While the fact that Payne’s thumb
unlocked the phone proved to be incriminating, it alone
certainly did not serve to authenticate all the phone’s
contents.
    To the extent Payne relies on the Oakland court’s
attempt to distinguish biometric unlocks from “requiring a
suspect to submit to fingerprinting” because it immediately
results in access to more physical evidence and “there is no
comparison . . . required to confirm a positive match,” this
line of analysis conflates what is incriminating with what is
testimonial. Oakland, 354 F. Supp. 3d at 1016; see Doe, 487
U.S. at 210 (“[C]ertain acts, though incriminating, are not
within the privilege.”). All physical trait cases have dealt
with compelled acts eventually leading to incriminating
evidence that can be used in a suspect’s prosecution. See In
re Search Warrant Application for [redacted text], 279 F.
Supp. 3d at 805 (noting the “distinction—between whether
an act is testimonial versus whether the act is
incriminating—explains why physical characteristics, like
fingerprints, blood samples, handwriting, and so on are not
protected by the privilege even though they often are highly
incriminating”). The compelled use of an individual’s
thumb to unlock a device shares many of the same
incriminating inferences as comparing a suspect’s
thumbprint to a thumbprint lifted from a murder weapon.
The time it takes to make the connection, or the amount of
incriminating information that flows from the
nontestimonial act, is of little consequence.
32                          USA V. PAYNE


    Accordingly, we hold that the compelled use of Payne’s
thumb to unlock his phone (which he had already identified
for the officers) required no cognitive exertion, placing it
firmly in the same category as a blood draw or fingerprint
taken at booking. The act itself merely provided CHP with
access to a source of potential information, much like the
consent directive in Doe. The considerations regarding
existence, control, and authentication that were present in
Hubbell are absent or, at a minimum, significantly less
compelling in this case. Accordingly, under the current
binding Supreme Court framework, the use of Payne’s
thumb to unlock his phone was not a testimonial act and the
Fifth Amendment does not apply. 8
    We would be remiss not to mention that Fifth
Amendment questions like this one are highly fact dependent
and the line between what is testimonial and what is not is
particularly fine. Our opinion should not be read to extend
to all instances where a biometric is used to unlock an
electronic device. Indeed, the outcome on the testimonial
prong may have been different had Officer Coddington
required Payne to independently select the finger that he
placed on the phone. See In re Search Warrant Application
for [redacted text], 279 F. Supp. 3d at 804 (discussing how

8
  Payne argues that the Supreme Court’s decision in Riley supports a
different result because there the Court recognized that modern
technological advances like the use of smart phones may require
reexamination of certain privacy principles. 573 U.S. at 403. But Riley
analyzed cell phone searches under the Fourth Amendment, which calls
for a reasonableness analysis. See In re Search Warrant Application for
[redacted text], 279 F. Supp. 3d at 806. The Fifth Amendment demands
no such reasonableness inquiry. The narrow question before us is
whether the compelled use of Payne’s thumb is testimonial. Existing
Supreme Court precedent provides the necessary tools to answer that
question.
                        USA V. PAYNE                        33


a suspect would be required to engage in some thought
process if the government compels them to “decide which
finger (or fingers) to apply” to a sensor). And if that were
the case, we may have had to grapple with the so-called
foregone conclusion doctrine. See Fisher, 425 U.S. at 411.
We mention these possibilities not to opine on the right result
in those future cases, but only to demonstrate the complex
nature of the inquiry.
                              IV
    Having determined that the search of Payne’s cell phone
did not violate the Fourth or Fifth Amendment, Payne’s
argument that the evidence seized from El Cortez Way must
be suppressed as “fruit of the poisonous tree” fails.
    Next, Payne contends that the pre-warrant search of the
house on El Cortez Way independently violated his Fourth
Amendment rights. The government offers three possible
reasons why either the pre-warrant search was legal, or the
constitutionality of the pre-warrant search is immaterial to
the outcome of this case. First, it claims the search was valid
pursuant to Payne’s parole conditions. Second, it claims that
the search warrant CHP officers eventually obtained was
valid notwithstanding the constitutionality of the pre-
warrant search. Third, it claims that even if the search
warrant was invalid, the good faith exception to the
exclusionary rule applies. We agree with the government’s
second argument and, thus, do not address its first or third.
    We review the district court’s denial of Payne’s motion
to suppress de novo and can affirm on any basis the record
supports. United States v. Ruiz, 428 F.3d 877, 880 (9th Cir.
2005).
34                      USA V. PAYNE


    When a search warrant application includes “illegally
obtained information,” a reviewing court must determine
whether the warrant was supported by probable cause after
“properly purg[ing] the affidavit of the offending facts.”
United States v. Bishop, 264 F.3d 919, 924 (9th Cir. 2001).
Here, the district court held that “when you eliminate the
facts uncovered during the sweep, the warrant contained
probable cause.” In his reply brief, Payne expressly
conceded that he “agrees with the government . . . that the
information from his phone likely would have been
sufficient for probable cause even without the information
garnered during the illegal protective sweep.” We agree.
    Assuming without deciding that the pre-warrant sweep
of El Cortez Way violated Payne’s Fourth Amendment
rights, whether the warrant CHP officers obtained was
supported by probable cause —i.e., a “probability or
substantial chance of criminal activity”—depends on the
facts included in the warrant application that CHP officers
knew before the sweep. District of Columbia v. Wesby, 583
U.S. 48, 57 (2018). These included: (1) Payne was
extremely nervous, sweating profusely, and fumbling for his
documents when he was initially pulled over; (2) Payne
confirmed that he was on parole; (3) a search of Payne’s cell
phone showed a video depicting a large amount of cash, a
money-counting machine, and several bags of what officers
suspected to be fentanyl; (4) a separate video from Payne’s
phone showed the outside of the home on El Cortez Way;
(5) the map application on Payne’s phone showed a pin to a
parked vehicle outside a residence on El Cortez Way; and
(6) upon driving to the location on El Cortez Way, Officer
Coddington observed a silver BMW, confirmed it was
registered to Payne, and was able to unlock the vehicle using
the key seized from Payne’s person.
                        USA V. PAYNE                        35


    As Payne acknowledges in his reply brief, these facts go
well beyond establishing probable cause to believe that a
search of the house would uncover evidence of criminal drug
possession and trafficking. Thus, the search warrant was
valid even after excising the facts included in the application
from the pre-warrant protective sweep. The district court
rightfully denied Payne’s motion to suppress.
                       CONCLUSION
   We AFFIRM the denial of Payne’s motion to suppress.

```

---

## GROUP: _overhaul2/lake/cases/United States v. Payner.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Payner"
type: case
citation: "447 U.S. 727 (1980)"
parallel_cite: "100 S. Ct. 2439; 65 L. Ed. 2d 468"
neutral_cite: 1980 U.S. LEXIS 136
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-08-11
docket: 78-1729
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1980-06-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Payner
  varies_by_point: false
  scope_note: A federal court may not use its supervisory power to evade the Fourth Amendment standing rules. Good law.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110317/united-states-v-payner/"
  cluster_id: 110317
  opinion_id: 9428014
  identity_checked: true
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: "Key — Progeny"
related: ["[[Rakas v. Illinois]]", "[[Alderman v. United States]]", "[[Elkins v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "standing", "exclusionary-rule", "supervisory-power", "third-party"]
holding: "A federal court may not invoke its supervisory power to suppress evidence obtained through the deliberate violation of a third party's Fourth Amendment rights at the instance of a defendant whose own rights were not violated; the supervisory power cannot circumvent the standing requirement."
lake:
  record_id: United States v. Payner
  status: verified
  projected_at: 2026-07-09
---

# United States v. Payner

*447 U.S. 727 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In the IRS "briefcase caper," agents arranged for an informant to steal a Bahamian banker's briefcase and photograph its documents, which led to evidence that Payner had falsified his tax return. The District Court found that the Government had deliberately and flagrantly violated the banker's (a third party's) Fourth Amendment rights, but it acknowledged that Payner himself lacked standing because his own rights were not invaded. It nonetheless suppressed the evidence under the federal courts' supervisory power, and the Sixth Circuit affirmed.

## Issue
Whether a federal court may invoke its supervisory power to suppress evidence obtained through the Government's deliberate violation of a third party's Fourth Amendment rights, at the instance of a defendant whose own rights were not violated and who therefore lacks standing.

## Rule
No. "We conclude that the supervisory power does not authorize a federal court to suppress otherwise admissible evidence on the ground that it was seized unlawfully from a third party not before the court. Our Fourth Amendment decisions have established beyond any doubt that the interest in deterring illegal searches does not justify the exclusion of tainted evidence at the instance of a party who was not the victim of the challenged practices." — 447 U.S. at 735 (citing *Rakas v. Illinois*, 439 U.S. 128, 137, and *Alderman v. United States*, 394 U.S. 165, 174–175). ^pin-735

The label does not matter: "The values assigned to the competing interests do not change because a court has elected to analyze the question under the supervisory power instead of the Fourth Amendment." — [*Id.* at 736](https://www.courtlistener.com/opinion/110317/united-states-v-payner/#:~:text=The%20values%20assigned%20to%20the). ^pin-736

## Application
However egregious the IRS conduct, Payner was not the victim of the unlawful search — it invaded the banker's rights, not his — so he had no standing, and the same deterrence-versus-cost balance the standing rule already strikes governed. The District Court's contrary weighing "amounts to a substitution of individual judgment for the controlling decisions of this Court." To let a court suppress on that basis "would confer on the judiciary discretionary power to disregard the considered limitations of the law it is charged with enforcing." — [*Id.* at 737](https://www.courtlistener.com/opinion/110317/united-states-v-payner/#:~:text=amounts%20to%20a%20substitution%20of). ^pin-737

## Conclusion
The supervisory power "does not extend so far"; the suppression order was reversed. A defendant who lacks [[Standing to Challenge a Search|Fourth Amendment standing]] cannot obtain exclusion through the supervisory power.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Payner* enforces the personal-rights standing rule of [[Alderman v. United States]] and [[Rakas v. Illinois]], holding the supervisory power cannot be used to evade it; it draws on the restrained-supervisory-power and deterrence rationale of [[Elkins v. United States]].

## Appears on
- [[Standing to Challenge a Search]] — *Key — Progeny*

## Sources
- *United States v. Payner*, 447 U.S. 727 (1980) — https://www.courtlistener.com/opinion/110317/united-states-v-payner/ — pinpoints: 735, 736, 737.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "11a42d5d0dc42423", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Payner"}, "payload": {"all": [{"cite": "447 U.S. 727", "page": "727", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "447"}, {"cite": "100 S. Ct. 2439", "page": "2439", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "100"}, {"cite": "65 L. Ed. 2d 468", "page": "468", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "65"}, {"cite": "1980 U.S. LEXIS 136", "page": "136", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1980"}], "display": "447 U.S. 727", "official": {"cite": "447 U.S. 727", "page": "727", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "447"}, "official_selection_present": true, "record_id": "United States v. Payner"}}
{"assertion_id": "322dd6c545e986ab", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-737", "record_id": "United States v. Payner"}, "payload": {"fragment": "#:~:text=amounts%20to%20a%20substitution%20of", "page": null, "pin_id": "pin-737", "pinpoint_status": "star-verified", "quote": "amounts to a substitution of individual judgment for the controlling decisions of this Court.", "quote_fidelity": "matched", "record_id": "United States v. Payner", "star_marker": "737"}}
{"assertion_id": "3463263067857ba7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-736", "record_id": "United States v. Payner"}, "payload": {"fragment": "#:~:text=The%20values%20assigned%20to%20the", "page": null, "pin_id": "pin-736", "pinpoint_status": "star-verified", "quote": "The values assigned to the competing interests do not change because a court has elected to analyze the question under the supervisory power instead of the Fourth Amendment.", "quote_fidelity": "matched", "record_id": "United States v. Payner", "star_marker": "736"}}
{"assertion_id": "e348268924c9396f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-735", "record_id": "United States v. Payner"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-735", "pinpoint_status": "slip-only", "quote": "agents arranged for an informant to steal a Bahamian banker's briefcase and photograph its documents, which led to evidence that Payner had falsified his tax return. The District Court found that the Government had deliberately and flagrantly violated the banker's (a third party's) Fourth Amendment rights, but it acknowledged that Payner himself lacked standing because his own rights were not invaded. It nonetheless suppressed the evidence under the federal courts' supervisory power, and the Sixth Circuit affirmed. ## Issue Whether a federal court may invoke its supervisory power to suppress evidence obtained through the Government's deliberate violation of a third party's Fourth Amendment rights, at the instance of a defendant whose own rights were not violated and who therefore lacks standing. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "United States v. Payner", "star_marker": null}}
{"assertion_id": "46d546b43741f6de", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Payner"}, "payload": {"as_of_content": "1980-06-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Payner", "scope_note": "A federal court may not use its supervisory power to evade the Fourth Amendment standing rules. Good law.", "varies_by_point": false}}
```

### lake record — United States v. Payner

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Payner",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Payner",
    "case_name_short": "Payner",
    "case_name_full": "United States v. Payner",
    "input_case_name": "United States v. Payner",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-08-11",
    "year": 1980,
    "docket": "78-1729",
    "cluster_id": 110317,
    "lead_opinion_id": 9428014,
    "sibling_ids": [
      110317,
      9428014,
      9428015
    ],
    "absolute_url": "/opinion/110317/united-states-v-payner/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "447 U.S. 727",
      "volume": "447",
      "reporter": "U.S.",
      "page": "727",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 2439",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2439",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 468",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "468",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 136",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "136",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "447 U.S. 727",
        "volume": "447",
        "reporter": "U.S.",
        "page": "727",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 2439",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2439",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 468",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "468",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 136",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "136",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "447 U.S. 727",
    "official_selection": {
      "court_class": "scotus",
      "selected": "447 U.S. 727",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-735",
      "page": null,
      "quote": "agents arranged for an informant to steal a Bahamian banker's briefcase and photograph its documents, which led to evidence that Payner had falsified his tax return. The District Court found that the Government had deliberately and flagrantly violated the banker's (a third party's) Fourth Amendment rights, but it acknowledged that Payner himself lacked standing because his own rights were not invaded. It nonetheless suppressed the evidence under the federal courts' supervisory power, and the Sixth Circuit affirmed. ## Issue Whether a federal court may invoke its supervisory power to suppress evidence obtained through the Government's deliberate violation of a third party's Fourth Amendment rights, at the instance of a defendant whose own rights were not violated and who therefore lacks standing. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-736",
      "page": null,
      "quote": "The values assigned to the competing interests do not change because a court has elected to analyze the question under the supervisory power instead of the Fourth Amendment.",
      "star_marker": "736",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 18359,
      "fragment": "#:~:text=The%20values%20assigned%20to%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-737",
      "page": null,
      "quote": "amounts to a substitution of individual judgment for the controlling decisions of this Court.",
      "star_marker": "737",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 19214,
      "fragment": "#:~:text=amounts%20to%20a%20substitution%20of",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1980-06-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Payner",
    "varies_by_point": false,
    "scope_note": "A federal court may not use its supervisory power to evade the Fourth Amendment standing rules. Good law.",
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
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Willie Walker, Jr. v. United States",
          "cluster_id": 4592520,
          "cite": [
            "201 A.3d 586"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Delaine and Malisa Fitzpat",
          "cluster_id": 889950,
          "cite": [
            "2012 MT 300",
            "367 Mont. 385",
            "291 P.3d 1106",
            "2012 Mont. LEXIS 368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Jordan Heath Dentler",
          "cluster_id": 4472853,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Teague",
          "cluster_id": 202526,
          "cite": [
            "469 F.3d 205",
            "2006 U.S. App. LEXIS 29293",
            "2006 WL 3423378"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Southerland, Vince",
          "cluster_id": 186774,
          "cite": [
            "373 U.S. App. D.C. 305",
            "466 F.3d 1083",
            "2006 U.S. App. LEXIS 26978",
            "2006 WL 3069122"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Clemmons v. Wolfe",
          "cluster_id": 3013934,
          "cite": [
            "377 F.3d 322",
            "2004 U.S. App. LEXIS 15613",
            "2004 WL 1689682"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Triumph Capital Group, Inc.",
          "cluster_id": 8751433,
          "cite": [
            "211 F.R.D. 31",
            "2002 U.S. Dist. LEXIS 21615",
            "2002 WL 31487754"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Badgett",
          "cluster_id": 1265814,
          "cite": [
            "895 P.2d 877",
            "10 Cal. 4th 330",
            "41 Cal. Rptr. 2d 635",
            "95 Cal. Daily Op. Serv. 4314",
            "95 Daily Journal DAR 7407",
            "1995 Cal. LEXIS 3320"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Richard A. Horn",
          "cluster_id": 674595,
          "cite": [
            "29 F.3d 754",
            "29 Fed. R. Serv. 3d 1525",
            "1994 U.S. App. LEXIS 18687",
            "1994 WL 378486"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. McMillan",
          "cluster_id": 3944785,
          "cite": [
            "631 N.E.2d 660",
            "91 Ohio App. 3d 1",
            "1993 Ohio App. LEXIS 4413"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thomas v. Arn",
          "cluster_id": 111545,
          "cite": [
            "88 L. Ed. 2d 435",
            "106 S. Ct. 466",
            "474 U.S. 140",
            "1985 U.S. LEXIS 146"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
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
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Powers v. Ohio",
          "cluster_id": 112570,
          "cite": [
            "113 L. Ed. 2d 411",
            "111 S. Ct. 1364",
            "499 U.S. 400",
            "1991 U.S. LEXIS 1857",
            "59 U.S.L.W. 4268",
            "91 Daily Journal DAR 3732",
            "91 Cal. Daily Op. Serv. 2259"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hasting",
          "cluster_id": 110933,
          "cite": [
            "76 L. Ed. 2d 96",
            "103 S. Ct. 1974",
            "461 U.S. 499",
            "1983 U.S. LEXIS 31",
            "51 U.S.L.W. 4572"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
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
        "journal_ref": "United States v. Payner:lane2_top_cited"
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
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bank of Nova Scotia v. United States",
          "cluster_id": 112125,
          "cite": [
            "101 L. Ed. 2d 228",
            "108 S. Ct. 2369",
            "487 U.S. 250",
            "1988 U.S. LEXIS 2866",
            "56 U.S.L.W. 4714",
            "62 A.F.T.R.2d (RIA) 5738"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Young v. United States Ex Rel. Vuitton Et Fils S. A.",
          "cluster_id": 111893,
          "cite": [
            "95 L. Ed. 2d 740",
            "107 S. Ct. 2124",
            "481 U.S. 787",
            "1987 U.S. LEXIS 2261",
            "2 U.S.P.Q. 2d (BNA) 1809",
            "55 U.S.L.W. 4676"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Edmunds",
          "cluster_id": 2316698,
          "cite": [
            "586 A.2d 887",
            "526 Pa. 374",
            "1991 Pa. LEXIS 28"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Williams",
          "cluster_id": 112730,
          "cite": [
            "118 L. Ed. 2d 352",
            "112 S. Ct. 1735",
            "504 U.S. 36",
            "1992 U.S. LEXIS 2688"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lance W.",
          "cluster_id": 1421847,
          "cite": [
            "694 P.2d 744",
            "37 Cal. 3d 873",
            "210 Cal. Rptr. 631",
            "1985 Cal. LEXIS 241"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania Bd. of Probation and Parole v. Scott",
          "cluster_id": 118235,
          "cite": [
            "141 L. Ed. 2d 344",
            "118 S. Ct. 2014",
            "524 U.S. 357",
            "1998 U.S. LEXIS 4037"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "G. Heileman Brewing Co., Inc. v. Joseph Oat Corporation",
          "cluster_id": 520636,
          "cite": [
            "871 F.2d 648",
            "13 Fed. R. Serv. 3d 8",
            "1989 U.S. App. LEXIS 4563",
            "1989 WL 30098"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parks v. Commonwealth",
          "cluster_id": 1315235,
          "cite": [
            "270 S.E.2d 755",
            "221 Va. 492",
            "1980 Va. LEXIS 269"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Voigt",
          "cluster_id": 722380,
          "cite": [
            "89 F.3d 1050",
            "78 A.F.T.R.2d (RIA) 5577",
            "1996 U.S. App. LEXIS 16287",
            "1996 WL 380609"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lonchar v. Thomas",
          "cluster_id": 118015,
          "cite": [
            "134 L. Ed. 2d 440",
            "116 S. Ct. 1293",
            "517 U.S. 314",
            "1996 U.S. LEXIS 2167"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Roy L. Williams, Thomas F. O'malley, Andrew G. Massa, Joseph Lombardo",
          "cluster_id": 437518,
          "cite": [
            "737 F.2d 594"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gaetano Modica",
          "cluster_id": 396890,
          "cite": [
            "663 F.2d 1173",
            "1981 U.S. App. LEXIS 16444"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Guillermo Novo Sampol, United States of America v. Alvin Ross Diaz, United States of America v. Ignacio Novo Sampol",
          "cluster_id": 384944,
          "cite": [
            "636 F.2d 621",
            "204 U.S. App. D.C. 349"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, in No. 81-1020 v. Jannotti, Harry P. United States of America, in No. 81-1021 v. Schwartz, George X",
          "cluster_id": 401021,
          "cite": [
            "673 F.2d 578",
            "1982 WL 602723"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States Department of Labor v. Triplett",
          "cluster_id": 112399,
          "cite": [
            "108 L. Ed. 2d 701",
            "110 S. Ct. 1428",
            "494 U.S. 715",
            "1990 U.S. LEXIS 1666"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin Eugene Wright",
          "cluster_id": 663707,
          "cite": [
            "16 F.3d 1429",
            "1994 U.S. App. LEXIS 2361",
            "1994 WL 38983"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hutchins",
          "cluster_id": 1394982,
          "cite": [
            "279 S.E.2d 788",
            "303 N.C. 321",
            "1981 N.C. LEXIS 1186"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110317 OR 9428014 OR 9428015) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03NDkwODgwMDAwMDAmcz0zOTQ0Nzg1JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110317+OR+9428014+OR+9428015%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(110317 OR 9428014 OR 9428015)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzkmcz04OTc4OTU5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110317+OR+9428014+OR+9428015%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110317 OR 9428014 OR 9428015)",
        "reviewed": 11,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 11,
        "triage_read": 1,
        "triage_snippet_classified": 10
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110317 OR 9428014 OR 9428015)",
    "indexed_citing_opinions": 540,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110317,
        "count": 482,
        "count_source": "search"
      },
      {
        "opinion_id": 9428014,
        "count": 66,
        "count_source": "search"
      },
      {
        "opinion_id": 9428015,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 785,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-payner.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjYxNzY5ODgmcz00NTg3NTY5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110317+OR+9428014+OR+9428015%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110317,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 104603,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 105343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 105421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 106881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 107567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 107874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 108602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 108760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 108768,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 109005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 109437,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 109816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 110049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 341778,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 362527,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 1087965,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 1417027,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
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
    "date_created": "2026-07-06T02:12:06Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:12:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:12:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:17:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:12:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Payner

```
<opinion type="majority">
<author id="b770-10">Mr. Justice Powell</author>
<p id="Atf">delivered the opinion of the Court.</p>
<p id="b770-11">The question is whether the District Court properly suppressed the fruits of an unlawful search that did not invade the respondent’s Fourth Amendment rights.</p>
<p id="b770-12">I</p>
<p id="b770-13">Respondent Jack Payner was indicted in September 1976 on a charge of falsifying his 1972 federal income tax return in violation of <span class="citation no-link">18 U. S. C. § 1001</span>.<footnotemark>1</footnotemark> The indictment alleged that respondent denied maintaining a foreign bank account at a time when he knew that he had such an account at the Castle Bank and Trust Company of Nassau, Bahama Islands. The Government’s case rested heavily on a loan guarantee agreement dated April 28, 1972, in which respondent pledged <page-number citation-index="1" label="729">*729</page-number>the funds in his Castle Bank account as security for a $100,000 loan.</p>
<p id="b771-5">Respondent waived his right to jury trial and moved to suppress the guarantee agreement. With the consent of the parties, the United States District Court for the • Northern District of Ohio took evidence on the motion at a hearing consolidated with the trial on the merits. The court found respondent guilty as charged on the basis of all the evidence. The court also found, however, that the Government discovered the guarantee agreement by exploiting a flagrantly illegal search that occurred on January 15, 1973. The court therefore suppressed “all evidence introduced in the case by the Government with the exception of Jack Payner’s 1972 tax return . . . and the related testimony.” <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#136" aria-description="Citation for case: United States v. Payner">434 F. Supp. 113, 136</a></span> (1977). As the tax return alone was insufficient to demonstrate knowing falsification, the District Court set aside respondent’s conviction.<footnotemark>2</footnotemark></p>
<p id="b771-6">The events leading up to the 1973 search are not in dispute. In 1965, the Internal Revenue Service launched an investigation into the financial activities of American citizens in the Bahamas. The project, known as “Operation Trade Winds,” was headquartered in Jacksonville, Fla. Suspicion focused on the Castle Bank in 1972, when investigators learned that a suspected narcotics trafficker had an account there. Special Agent Richard Jaffe of the Jacksonville office asked Norman Casper, a private investigator and occasional informant, to learn what he could about the Castle Bank and its depositors. To that end, Casper cultivated his friendship with Castle <page-number citation-index="1" label="730">*730</page-number>Bank vice president Michael Wolstencroft. Casper introduced Wolstencroft to Sybol Kennedy, a private investigator and former employee. When Casper discovered that the banker intended to spend a few days in Miami in January 1973, he devised a scheme to gain access to the bank records he knew Wolstencroft would be carrying in his briefcase. Agent Jaffe approved the basic outline of the plan.</p>
<p id="b772-5">Wolstencroft arrived in Miami on January 15 and went directly to Kennedy’s apartment. At about 7:30 p. m., the two left for dinner at a Key Biscayne restaurant. Shortly thereafter, Casper entered the apartment using a key supplied by Kennedy. He removed the briefcase and delivered it to Jaffe.' While the agent supervised the copying of approximately 400 documents taken from the briefcase, a “lookout” observed Kennedy and Wolstencroft at dinner. The observer notified Casper when the pair left the restaurant, and the briefcase was replaced. The documents photographed that evening included papers evidencing a close working relationship between the Castle Bank and the Bank of Perrine, Fla. Subpoenas issued to the Bank of Perrine ultimately uncovered the loan guarantee agreement at issue in this case.</p>
<p id="b772-6">The District Court found that the United States, acting through Jaffe, “knowingly and willfully participated in the unlawful seizure of Michael Wolstencroft’s briefcase....” <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#120" aria-description="Citation for case: United States v. Payner"><em>Id., </em>at 120</a></span>. According to that court, “the Government affirmatively counsels its agents that the Fourth Amendment standing limitation permits them to purposefully conduct an unconstitutional search and seizure of one individual in order to obtain evidence against third parties. . . .” <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#132" aria-description="Citation for case: United States v. Payner"><em>Id., </em>at 132-133</a></span>. The District Court also found that the documents seized from Wolstencroft provided the leads that ultimately led to the discovery of the critical loan guarantee agreement. <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#123" aria-description="Citation for case: United States v. Payner"><em>Id., </em>at 123</a></span>.<footnotemark>3</footnotemark> Although the search did not impinge upon the <page-number citation-index="1" label="731">*731</page-number>respondent's Fourth Amendment rights, the District Court believed that the Due Process Clause of the Fifth Amendment and the inherent supervisory power of the federal courts required it to exclude evidence tainted by the Government’s “knowing and purposeful <em>bad faith hostility </em>to any person’s fundamental constitutional rights.” <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#129" aria-description="Citation for case: United States v. Payner"><em>Id., </em>at 129</a></span>; see <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#133" aria-description="Citation for case: United States v. Payner"><em>id., </em>at 133, 134-135</a></span>.</p>
<p id="b773-5">The Court of Appeals for the Sixth Circuit affirmed in a brief order endorsing the District Court’s use of its supervisory power. <span class="citation" data-id="362527"><a href="/opinion/362527/united-states-v-jack-payner/" aria-description="Citation for case: United States v. Jack Payner">590 F. 2d 206</a></span> (1979) <em>(per curiam). </em>The Court of Appeals did not decide the due process question. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./444/822/">444 U. S. 822</a></span> (1979), and we now reverse.</p>
<p id="b773-6">II</p>
<p id="b773-7">This Court discussed the doctrine of “standing to invoke the [Fourth Amendment] exclusionary rule” in some detail last Term. <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#138" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 138</a></span> (1978). We reaffirmed the established rule that a court may not exclude evidence under the Fourth Amendment unless it finds that an unlawful search or seizure violated the defendant’s own constitutional rights. <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#133" aria-description="Citation for case: Rakas v. Illinois"><em>Id., </em>at 133-140</a></span>. See, <em>e. g., Brown </em>v. <em>United States, </em><span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/#229" aria-description="Citation for case: Brown v. United States">411 U. S. 223, 229-230</a></span> (1973); <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#171" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 171-172</a></span> (1969); <em>Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#389" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 389</a></span> (1968). And the defendant’s Fourth Amendment rights are violated only when the challenged conduct invaded <em>his </em>legitimate expectation of privacy rather than that of a third party. <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 143</a></span>; <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#149" aria-description="Citation for case: Rakas v. Illinois"><em>id., </em>at 149-152</a></span> (Powell, J., concurring) ; <em>Combs </em>v. <em>United States, </em><span class="citation" data-id="108602"><a href="/opinion/108602/combs-v-united-states/#227" aria-description="Citation for case: Combs v. United States">408 U. S. 224, 227</a></span> (1972); <em>Mancusi </em>v. <em>DeForte, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#368" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364, 368</a></span> (1968).</p>
<p id="b773-8">The foregoing authorities establish, as the District Court recognized, that respondent lacks standing under the Fourth <page-number citation-index="1" label="732">*732</page-number>Amendment to suppress the documents illegally seized from Wolstencroft. <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#126" aria-description="Citation for case: United States v. Payner">434 F. Supp., at 126</a></span>. The Court of Appeals did not disturb the District Court’s conclusion that “Jack Payner possessed no privacy interest in the Castle Bank documents that were seized from Wolstencroft.” <em>Ibid.; </em>see <span class="citation" data-id="362527"><a href="/opinion/362527/united-states-v-jack-payner/#207" aria-description="Citation for case: United States v. Jack Payner">590 F. 2d, at 207</a></span>. Nor do we. <em>United States </em>v. <em>Miller, </em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">425 U. S. 435</a></span> (1976), established that a depositor has no expectation of privacy and thus no “protectable Fourth Amendment interest” in copies of checks and deposit slips retained by his bank. <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#437" aria-description="Citation for case: United States v. Miller"><em>Id., </em>at 437</a></span>; see <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#442" aria-description="Citation for case: United States v. Miller"><em>id., </em>at 442</a></span>. Nothing in the record supports a contrary conclusion in this case.<footnotemark>4</footnotemark></p>
<p id="b775-4"><page-number citation-index="1" label="733">*733</page-number>The District Court and the Court of Appeals believed, however, that a federal court should use its supervisory power to suppress evidence tainted by gross illegalities that did not infringe the defendant’s constitutional rights. The United States contends that this approach- — as applied in this case— upsets the careful balance of interests embodied in the Fourth Amendment decisions of this Court. In the Government’s view, such an extension of the supervisory power would enable federal courts to exercise a standardless discretion in their application of the exclusionary rule to enforce the Fourth Amendment. We agree with the Government.</p>
<p id="b775-5">Ill</p>
<p id="b775-6">We certainly can understand the District Court’s commendable desire to deter deliberate intrusions into the privacy of persons who are unlikely to become defendants in a criminal prosecution. See <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#135" aria-description="Citation for case: United States v. Payner">434 F. Supp., at 135</a></span>. No court should condone the unconstitutional and possibly criminal behavior of those who planned and executed this “briefcase caper.” <footnotemark>5</footnotemark> <page-number citation-index="1" label="734">*734</page-number>Indeed, the decisions of this Court are replete with denunciations of willfully lawless activities undertaken in the name of law enforcement. <em>E. g., Jackson </em>v. <em>Denno, </em><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#386" aria-description="Citation for case: Jackson v. Denno">378 U. S. 368, 386</a></span> (1964); see <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#485" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 485</a></span> (1928) (Brandéis, J., dissenting). But our cases also show that these unexceptional principles do not command the exclusion of evidence in every case of illegality. Instead, they must be weighed against the considerable harm that would flow from indiscriminate application of an exclusionary rule.</p>
<p id="b776-5">Thus, the exclusionary rule “has been restricted to those areas where its remedial objectives are most efficaciously served.” <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 348</a></span> (1974). The Court has acknowledged that the suppression of probative but tainted evidence exacts a costly toll upon the ability of courts to ascertain the truth in a criminal case. <em>E. g., Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#137" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 137-138</a></span>; <em>United States </em>v. <em>Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#275" aria-description="Citation for case: United States v. Ceccolini">435 U. S. 268, 275-279</a></span> (1978); <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#489" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 489-491</a></span> (1976); see <em>Michigan </em>v. <em>Tucker, </em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#450" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 450-451</a></span> (1974).<footnotemark>6</footnotemark> Our cases have consistently recognized that unbending application of the exclusionary sanction to enforce ideals of governmental rectitude would impede unacceptably the truth-finding functions of judge and jury. <em>E. g., Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#485" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 485-489</a></span>; <em>United States </em>v. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>. After all, it is the defendant, and not the constable, who stands trial.</p>
<p id="b776-6">The same societal interests are at risk when a criminal defendant invokes the supervisory power to suppress evidence seized in violation of a third party’s constitutional rights. The supervisory power is applied with some caution even <page-number citation-index="1" label="735">*735</page-number>when the defendant asserts a violation of his own rights.<footnotemark>7</footnotemark> In <em>United States </em>v. <em>Caceres, </em><span class="citation" data-id="9427514"><a href="/opinion/110049/united-states-v-caceres/#754" aria-description="Citation for case: United States v. Caceres">440 U. S. 741, 754-757</a></span> (1979), we refused to exclude all evidence tainted by violations of an executive department’s rules. And in <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#216" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 216</a></span> (1960), the Court called for a restrained application of the supervisory power.</p>
<blockquote id="b777-5">“[A]ny apparent limitation upon the process of discovering truth in a federal trial ought to be imposed only upon the basis of considerations which outweigh the genera] need for untrammeled disclosure of competent and relevant evidence in a court of justice.” <em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">Ibid.</a></span></em></blockquote>
<p id="b777-6">See also <em>Nardone </em>v. <em>United States, </em><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#340" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 340</a></span> (1939).</p>
<p id="b777-7">We conclude that the supervisory power does not authorize a federal court to suppress otherwise admissible evidence on the ground that it was seized unlawfully from a third party not before the court. Our Fourth Amendment decisions have established beyond any doubt that the interest in deterring illegal searches does not justify the exclusion of tainted evidence at the instance of a party who was not the victim of the challenged practices. <em>Rakas </em>v. <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#137" aria-description="Citation for case: Rakas v. Illinois"><em>Illinois, supra, </em>at 137</a></span>; <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States">394 U. S., at 174-175</a></span>.<footnotemark>8</footnotemark> <page-number citation-index="1" label="736">*736</page-number>The values assigned to the competing interests do not change because a court has elected to analyze the question under the supervisory power instead of the Fourth Amendment. In either case, the need to deter the underlying conduct and the detrimental impact of excluding the evidence remain precisely the same.</p>
<p id="b778-5">The District Court erred, therefore, when it concluded that <page-number citation-index="1" label="737">*737</page-number>“society’s interest in deterring [bad faith] conduct by exclusion outweigh [s] society’s interest in furnishing the trier of fact with all relevant evidence.” <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#135" aria-description="Citation for case: United States v. Payner">434 F. Supp., at 135</a></span>. This reasoning, which the Court of Appeals affirmed, amounts to a substitution of individual judgment for the controlling decisions of this Court.<footnotemark>9</footnotemark> Were we to accept this use of the supervisory power, we would confer on the judiciary discretionary power to disregard the considered limitations of the law it is charged with enforcing. We hold that the supervisory power does not extend so far.</p>
<p id="b779-5">The judgment of the Court of Appeals is</p>
<p id="b779-6">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b770-14"> Title <span class="citation no-link">18 U. S. C. § 1001</span> provides in relevant part:</p>
<blockquote id="b770-15">“Whoever, in any matter within the jurisdiction of any department or agency of the United States knowingly and willfully . . . makes any false, fictitious or fraudulent statements or representations, . . . shall be fined not more than $10,000 or imprisoned not more than five years, or both.”</blockquote>
</footnote>
<footnote label="2">
<p id="b771-7"> The unusual sequence of rulings was a byproduct of the consolidated hearing conducted by the District Court. The court initially failed to enter judgment on the merits. At the close of the evidence, it simply granted respondent’s motion to suppress. After the Court of Appeals for the Sixth Circuit dismissed the Government’s appeal for want of jurisdiction, the District Court vacated the order granting the motion to suppress and entered a verdict of guilty. The court then reinstated its suppression order and set aside the verdict. Respondent does not challenge these procedures.</p>
</footnote>
<footnote label="3">
<p id="b772-7"> The United States argued in the District Court and the Court of Appeals that the guarantee agreement was discovered through an independent investigation untainted by the briefcase search. The Government also <page-number citation-index="1" label="731">*731</page-number>denied that its agents willfully encouraged Casper’s illegal behavior. For purposes of this opinion, we need not question the District Court’s contrary findings on either point.</p>
</footnote>
<footnote label="4">
<p id="b774-5"><em> </em>We are not persuaded by respondent’s suggestion that the Bahamian law of bank secrecy creates an expectation of privacy not present in <em>United States </em>v. <em>Miller, </em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">425 U. S. 435</a></span> (1976). At the outset, it is not clear that secret information regarding this respondent’s account played any role in the investigation that led to the discovery of the critical loan guarantee agreement. See <em>swpra, </em>at 730. Even if the causal link were established, however, respondent’s claim lacks merit. He cites a provision, 1909 Bah. Acts, ch. 4, that is no longer in effect. Bank secrecy is now safeguarded by § 19 of the Banks Act, Bah. Islands Rev. Laws, ch. 96 (1965), as added, 1965 Bah. Acts, No. 65, which provides in relevant part:</p>
<blockquote id="b774-8">“(1) Except for the purpose of the performance of his duties or the exercise of his functions under this Act or when lawfully required to do so by any court of competent jurisdiction within the Colony or under the provisions of any law, no person shall disclose any information relating to the affairs of . . . the customer of a bank which he has acquired in the performance of his duties or the exercise of his functions under this Act.” See also the Banks and Trust Companies Regulation Act, 1965 Bah. Acts, No. 64, § 10, as amended, 1968 Bah. Acts, No. 34, 1969 Bah. Acts, No. 20, 1971 Bah. Acts, No. 15. The statute is hardly a blanket guarantee of privacy. Its application is limited; it is hedged with exceptions; and we have been directed to no authority construing its terms. Moreover, American depositors know that their own country requires them to report relationships with foreign financial institutions. <span class="citation no-link">31 U. S. C. §1121</span>; <span class="citation no-link">31 CFR §103.24</span> (1979). See generally <em>California Bankers Assn. </em>v. <em>Shultz, </em><span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#59" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S. 21, 59-63, 71-76</a></span> (1974). We conclude that respondent lacked a reasonable expectation of privacy in the Castle Bank records that documented his account.</blockquote>
</footnote>
<footnote label="5">
<p id="b775-7"> “The security of persons and property remains a fundamental value which law enforcement officers must respect. Nor should those who flout the rules escape unscathed.” <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#175" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 175</a></span> (1969). We note that in 1976 Congress investigated the improprieties revealed in this record. See Oversight Hearings into the Operations of the IRS before a Subcommittee of the House Committee on Government Operations (Operation Tradewinds, Project Haven, and Narcotics Traffickers Tax Program), 94th Cong., 1st Sess. (1975). As a result, the Commissioner of Internal Revenue “called off” Operation Trade Winds. Tr. of Oral Arg. 35. The Commissioner also adopted guidelines that require agents to instruct informants on the requirements of the law and to report known illegalities to a supervisory officer, who is in turn directed to notify appropriate state authorities. IR Manual §§ 9373.3 (3), 9373.4 (Manual Transmittal 9-21, Dec. 27, 1977). Although these measures appear on their face to be less positive than one might expect from an agency charged with upholding the law, they do indicate disapproval of the practices found to have been implemented in this case. We cannot assume that similar lawless conduct, if brought to the attention of <page-number citation-index="1" label="734">*734</page-number>responsible officials, would not be dealt with appropriately. To require in addition the suppression of highly probative evidence in a trial against a third party would penalize society unnecessarily.</p>
</footnote>
<footnote label="6">
<p id="b776-10"> See also <em>Kaufman </em>v. <em>United States, </em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#237" aria-description="Citation for case: Kaufman v. United States">394 U. S. 217, 237-238</a></span> (1969) (Black, J., dissenting); Oaks, Studying the Exclusionary Rule in Search and Seizure, <span class="citation no-link">37 U. Chi. L. Rev. 665</span>, 736-746, 755-756 (1970).</p>
</footnote>
<footnote label="7">
<p id="b777-8"> Federal courts may use their supervisory power in some circumstances to exclude evidence taken from the <em>defendant </em>by “willful disobedience of law.” <em>McNabb </em>v. <em>United States, </em><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#345" aria-description="Citation for case: McNabb v. United States">318 U. S. 332, 345</a></span> (1943); see <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#223" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 223</a></span> (1960); <em>Rea </em>v. <em>United States, </em><span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/#216" aria-description="Citation for case: Rea v. United States">350 U. S. 214, 216-217</a></span> (1956); cf. <em>Hampton </em>v. <em>United States, </em><span class="citation" data-id="9426380"><a href="/opinion/109437/hampton-v-united-states/#495" aria-description="Citation for case: Hampton v. United States">425 U. S. 484, 495</a></span> (1976) (Powell, J., concurring in judgment). This Court has never held, however, that the supervisory power authorizes suppression of evidence obtained from third parties in violation of Constitution, statute, or rule. The supervisory power merely permits federal courts to supervise “the administration of criminal justice” among the parties before the bar. <em>McNabb </em>v. <em>United States, supra, </em>at 340.</p>
</footnote>
<footnote label="8">
<p id="b777-9"> “The deterrent values of preventing the incrimination of those whose rights the police have violated have been considered sufficient to justify the suppression of probative evidence even though the case against the defendant is weakened or destroyed. We adhere to that judgment. But <page-number citation-index="1" label="736">*736</page-number>we are not convinced that the additional benefits of extending the exclusionary rule to other defendants would justify further encroachment upon the public interest in prosecuting those accused of crime and having them acquitted or convicted on the basis of all the evidence which exposes the truth.” <em>Alderman </em>v. <em>United States, </em>394 U. S., at 174-175. See also <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#488" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 488-489</a></span> (1976); <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 348</a></span> (1974).</p>
<p id="AaX4">The dissent, <em>post, </em>at 746, urges that the balance of interests under the supervisory power differs from that considered in <em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">Alderman</a></span> </em>and like cases, because the supervisory power focuses upon the “need to protect the integrity of the federal courts.” Although the District Court in this case relied upon a deterrent rationale, we agree that the supervisory power serves the “twofold” purpose of deterring illegality and protecting judicial integrity. See <em>post, </em>at 744. As the dissent recognizes, however, the Fourth Amendment exclusionary rule serves precisely the same purposes. <em>Ibid., </em>citing, <em>inter alia, Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#218" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 218</a></span> (1979), and <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#659" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 659-660</a></span> (1961). Thus, the Fourth Amendment exclusionary rule, like the supervisory power, is applied in part “to protect the integrity of the <em>court, </em>rather than to vindicate the constitutional rights of the defendant. . . .” <em>Post, </em>at 747; see generally <em>Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 486</a></span>; <em>United States </em>v. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>.</p>
<p id="AxV">In this case, where the illegal conduct did not violate the respondent’s rights, the interest in preserving judicial integrity and in deterring such conduct is outweighed by the societal interest in presenting probative evidence to the trier to fact. See the first paragraph, <em>supra; </em>see also, <em>e. g., Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#485" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 485-486</a></span>. None of the cases cited by the dissent, <em>post, </em>at 7444745, supports a contrary view, since none of those cases involved criminal defendants who were not themselves the victims of the challenged practices. Thus, our decision today does not limit the traditional scope of the supervisory power in any way; nor does it render that power “superfluous.” <em>Post, </em>at 748. We merely reject its use as a substitute for established Fourth Amendment doctrine.</p>
</footnote>
<footnote label="9">
<p id="b779-10"> The same difficulty attends respondent’s claim to the protections of the Due Process Clause of the Fifth Amendment. The Court of Appeals expressly declined to consider the Due Process Clause. But even if we assume that the unlawful briefcase search was so outrageous as to offend fundamental “ ‘canons of decency and fairness/ ” <em>Rochin </em>v. <em>California, </em><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#169" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 169</a></span> (1952), quoting <em>Malinshi </em>v. <em>New York, </em><span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#417" aria-description="Citation for case: Malinski v. New York">324 U. S. 401, 417</a></span> (1945) (opinion of Frankfurter, J.), the fact remains that “[t]he limitations of the Due Process Clause . . . come into play only when the Government activity in question violates some protected right of the <em>defendant,” Hampton </em>v. <em>United States, supra, </em>at 490 (plurality opinion).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Perez-Rodriguez.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Perez-Rodriguez
type: case
citation: "13 F.4th 1 (2021)"
parallel_cite: ""
neutral_cite: ""
court: 1st Cir. 2021
court_level: coa
circuit: ca1
year: 2021
date_decided: 2021-09-02
docket: 19-1538P
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
  opinion_url: "https://www.courtlistener.com/opinion/5067201/united-states-v-perez-rodriguez/"
  cluster_id: 5067201
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Perez-Rodriguez
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Entrapment]]"
    role: Key
related:
  - "[[Entrapment]]"
  - "[[Jacobson v. United States]]"
  - "[[Sherman v. United States]]"
tags:
  - case
  - entrapment
  - inducement
  - predisposition
  - jury-instruction
  - plain-error
  - first-circuit
holding: "The entrapment defense has two prongs — improper government inducement and the defendant's lack of predisposition — and a defendant who makes a modest production showing on both is entitled to have the jury instructed on entrapment; where an undercover agent posing on a dating app steered a target toward a sexual encounter with a fictitious minor, the district court's refusal to give the entrapment instruction was plain error, and the conviction was vacated and remanded for a new trial."
aliases:
  - United States v. Perez-Rodriguez
  - "United States v. Pérez-Rodríguez"
  - "United States v. Perez-Rodriguez (1st Cir. 2021)"
---

# United States v. Perez-Rodriguez

*13 F.4th 1 (1st Cir. 2021)* (No. 19-1538P) · U.S. Court of Appeals for the First Circuit · **Binding in-circuit — 1st Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 5067201 → lead opinion 4882594 (13 F.4th 1, decided 2021-09-02); Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — CL text is slip-paginated). S9 promotes. -->

## Background
A Homeland Security Investigations agent ran a sting on an adults-only dating application, posing as a gay adult man. After Pérez-Rodríguez contacted the persona, the agent offered to arrange a sexual encounter with the agent's fictitious minor "boyfriend," an invented eleven-year-old. Pérez was charged with attempted enticement of a minor under 18 U.S.C. § 2422(b). He requested a jury instruction on entrapment, which the district court denied, and a jury convicted him. On appeal he challenged both the sufficiency of the evidence and the refusal to instruct on entrapment.

## Issue
Whether the district court erred in refusing to instruct the jury on entrapment, given the evidence of the government's inducement and the question of Pérez's predisposition.

## Rule
Entrapment shields a defendant who was not otherwise disposed to commit the crime but was induced to do so by the government, and a defendant is entitled to the instruction on a modest production showing as to each element. As the panel stated: "The defense has two prongs: (1) improper government inducement and (2) the defendant's lack of predisposition to commit the offense charged." — 13 F.4th 1, slip op. at 21. ^pin-op21

## Application
Although the court found the evidence sufficient to convict, it held that Pérez had made the modest showing needed to put entrapment to the jury. The agent had not merely furnished an ordinary opportunity to offend; posing as an adult romantic interest and then steering the exchange toward a fabricated child supplied evidence of improper inducement, and the record did not so conclusively establish predisposition as to withhold the question from the jury. Because the two prongs draw on overlapping facts and the evidence had to be viewed in the light most favorable to the defendant, the refusal to instruct deprived Pérez of his primary defense. Reviewing for plain error — because the objection was not renewed after the charge — the court found the error clear, prejudicial, and one that undermined the fairness of the proceeding.

## Conclusion
The conviction was **[[Reading and Citing Cases#vacated|vacated]]** and the case **[[Reading and Citing Cases#on-remand|remanded]] for a new trial**: the district court committed plain error in failing to instruct the jury on entrapment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Perez-Rodriguez* is a clean statement of the **two-prong** entrapment framework from *[[Jacobson v. United States|Jacobson]]* and *[[Sherman v. United States|Sherman]]* — improper inducement plus lack of predisposition — and of the **modest burden of production** that entitles a defendant to the instruction. Teach it for the inducement/predisposition split and for the rule that ambiguous entrapment evidence goes to the jury.

## Appears on
- [[Entrapment]] — *Key*

## Sources
- [*United States v. Perez-Rodriguez*, 13 F.4th 1 (1st Cir. 2021)](https://www.courtlistener.com/opinion/5067201/united-states-v-perez-rodriguez/) — pinpoint: slip op. at 21 (two-prong entrapment framework and burden of production; the CL opinion text carries slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "eb7d716ea4bdaa59", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Perez-Rodriguez"}, "payload": {"all": [{"cite": "13 F.4th 1", "page": "1", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "13"}], "display": "13 F.4th 1", "official": {"cite": "13 F.4th 1", "page": "1", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "13"}, "official_selection_present": true, "record_id": "United States v. Perez-Rodriguez"}}
{"assertion_id": "07ecdaea13e97d5e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Perez-Rodriguez"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Perez-Rodriguez", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Perez-Rodriguez

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Perez-Rodriguez",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Perez-Rodriguez",
    "case_name_short": "Perez-Rodriguez",
    "case_name_full": "",
    "input_case_name": "United States v. Perez-Rodriguez",
    "court": "1st Cir. 2021",
    "court_id": "ca1",
    "court_level": "coa",
    "circuit": "ca1",
    "state": null,
    "date_decided": "2021-09-02",
    "year": 2021,
    "docket": "19-1538P",
    "cluster_id": 5067201,
    "lead_opinion_id": 4882594,
    "sibling_ids": [],
    "absolute_url": "/opinion/5067201/united-states-v-perez-rodriguez/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "13 F.4th 1",
      "volume": "13",
      "reporter": "F.4th",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "13 F.4th 1",
        "volume": "13",
        "reporter": "F.4th",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "13 F.4th 1",
    "official_selection": {
      "court_class": "state",
      "selected": "13 F.4th 1",
      "reason": "selected_rank_3"
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
    "date_created": "2026-07-06T05:57:38Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:57:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:57:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:57:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:57:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-perez-rodriguez--5067201",
      "to_record_id": "United States v. Perez-Rodriguez",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Perez-Rodriguez

```
          United States Court of Appeals
                     For the First Circuit


No. 19-1538

                    UNITED STATES OF AMERICA,

                            Appellee,

                               v.

                     RAFAEL PÉREZ-RODRÍGUEZ,

                      Defendant, Appellant.


          APPEAL FROM THE UNITED STATES DISTRICT COURT
                FOR THE DISTRICT OF PUERTO RICO

     [Hon. Pedro A. Delgado-Hernández, U.S. District Judge]


                             Before

           Kayatta, Lipez, and Barron, Circuit Judges.


     Linda A. Backiel for appellant.
     Julia Meconiates, Assistant United States Attorney, with whom
W. Stephen Muldrow, United States Attorney, and Mariana E. Bauzá-
Almonte, Assistant United States Attorney, were on brief, for
appellee.


                        September 2, 2021
            LIPEZ,        Circuit     Judge.         Rafael    Pérez-Rodríguez      was

convicted by a jury of attempted enticement of a minor for unlawful

sexual activity in violation of 18 U.S.C. § 2422(b).                            He was

apprehended through a sting operation in which a government agent

created a profile on an adults-only dating application posing as

a gay adult man, and, after being contacted by Pérez, then offered

to arrange a sexual encounter with his minor "boyfriend."                          Pérez

appeals    on       several     grounds,     including      insufficiency     of    the

evidence and the denial of a jury instruction on the entrapment

defense.     While we find Pérez's challenge to the sufficiency of

the   evidence        meritless,     we   conclude     that    the   district    court

committed       plain        error   in    failing     to     give   the   entrapment

instruction.          We therefore vacate the conviction and remand for a

new trial.

                                            I.

            In 2015, Ryan Seig, a special agent with the child

exploitation unit of Homeland Security Investigations ("HSI"),

conducted       a    sting     operation    using     the     geosocial    networking

application Grindr.            Agent Seig testified that the purpose of the

application is "to talk and usually meet with someone else who

shares your interests."               On cross-examination, he added "it's

social networking among homosexuals."                 Grindr describes itself as

"the largest social networking app for gay, bi, trans, and queer

people."            About,    Grindr,     https://www.grindr.com/about/            (last


                                             - 2 -
visited August 25, 2021).         Grindr allows users to create profiles

and to exchange messages with other users with profiles in their

geographic area.     Per Agent Seig's testimony, "[a] profile is a

small blurb about what you are looking for, possibly what you look

like, and sort of a general description of who you are and what

you want."     Grindr requires users to be eighteen years of age or

older and does not allow individuals to use the platform to seek

sexual encounters with minors.

          Agent Seig created a Grindr profile under the name "Dave

W."   He wrote in his profile, "Looking for young fun or to share

my young fun."    He testified that he chose this text as a "veiled"

reference to a sexual encounter with a minor, explaining that

"someone who was familiar with the way pedophiles communicate on

the internet could read this and know what it meant."           The profile

also described "Dave W." as "Muscular, White, Single."

          On     December   30,    2015,   the   Dave   undercover   profile

received a message from a profile with the name "Mirando," a

profile created by Pérez.         Dave and "Mirando" exchanged messages

on Grindr, and then moved to text messaging.            The precise language

of the messages is crucial to this case.1          Thus, we reproduce key

parts of the exchange in full.        The conversation began as follows:




      1The messages were primarily in Spanish. We draw from the
certified English translations that were admitted into evidence.


                                       - 3 -
Pérez: Hello what are you doing?

Dave: Hey what's up

Pérez: Let's see you

Dave: Cool, do you like really young guys?

Pérez: Yes
       Age?
       I started at 8

Dave: Me? 35, but my boyfriend is young

Pérez: Hahhaha Okk
       How old is he?
       What does your boyfriend like?

Dave: He likes everything :)
      He is very young, what age do you like?

Pérez: The younger the better
       I don't discriminate
       I started at 8 hehehhe
       So you tell me
       What does he like to do?
       We are close, we can come up with some fun
       From there up I do it all

Dave: Do you understand English? I speak only a little
      Spanish
      My boyfriend is 11 years old. Do you want to play
      with him?

Pérez: Mmmm yessss
       Where is he?
       I speak little only a little English?
       Share pics??
       You tell me when and where???
       Do you prefer to call?
       Yes, I want to play

Dave:   We live in[] San Juan.
        We're free next week.




                        - 4 -
          Pérez: Ok
                 Have whatsapp?
                 Send me pics?
                 Can you now?

          Dave: Yes I'm busy with a party

          Pérez: Ok, but you are close
                 Can you get away?
                 Can you*

          Dave: Last night, no haha :)
                Do you want anal with him or oral?

          Pérez: Everything
                 I want the 3 of us to play
                 You for a while and me for a while.   You like?

          Dave:   Me too
                  Yes

          Pérez: Send me something to see you playing with him
                 I like taboo

          Dave:   Me too :)

          Pérez: Have a pic?
                 Are you with him at the party

          Dave: I don't want to send a pic because I won't know
                who you are until we meet
                Yes, he is here
                You can take pics if this happens. Just no faces
                I don't have whatsapp
                But I can text

          Pérez: Text is better

Pérez then sent two photos of himself to "Dave," and Dave provided

Pérez with a telephone number.

          The next day, December 31, Pérez sent Dave a text message

to continue the conversation.    He again expressed sexual interest

in "Dave's" minor "boyfriend."     Dave messaged, "we're going to


                                  - 5 -
have a lot of fun, friend. :) . . . Him you and I[.]"          Pérez

requested pictures of "Dave."       Pérez asked Dave questions about

his relationship with the minor.     ("How did you get him?" and "How

long have you had him?").

             On January 1, Pérez messaged Dave and said, "Happy New

Year."   He again said, "I want your boyfriend."      Pérez and Dave

discussed their availability for a meeting that week.           They

exchanged messages about what Pérez wants to do during the sexual

encounter.     Pérez asked several questions about how Dave met the

minor, what the minor's parents think, and whether "Dave's" family

knows about the minor.    "Dave's" answers included "He's my friend"

and "I am a 'good influence.'"

             On January 2, Dave initiated the conversation.       He

writes, "Just saying hi.        Very busy with family!     Happy new

year ;)[.]"     The following day, Dave and Pérez discussed meeting.

             Pérez: Let's see each other tomorrow to get to know you

             Dave: Ok, what time can you do it?

             Pérez: Write me when you wake up
                    I get up early
                    Where should we meet?

             Dave: Are we using your house or mine for the threesome?

             Pérez: Yes. I live alone. But if it's at home, then it
                    should be in the afternoon
                    But I want to see you before to get to know you
                    and see what you want to do so that I'm
                    comfortable

             Dave: I understand.   Me too.


                                    - 6 -
             Pérez: Ok

             Dave: Where is a good place for us all to meet?

             Pérez: Where should we meet

             Dave: We can meet and then go to your house for sex with
                   all of us?
                   I can meet anywhere. It doesn't matter. We'll
                   talk in the morning when you know more concerning
                   your schedule

             Pérez: Yes
                    Depends on what we talk about and we'll go
                    I am free. Write to me tomorrow.

Pérez then requested a picture of Dave again.           He asked Dave

several more questions about his relationship with the minor. Dave

said that the minor is "excited, happy" about the planned sexual

encounter.     They agreed to meet at Guaynabo Plaza.    Pérez stated

"first I see you" and asked "Can you come alone?"       Dave replied,

"I can leave him at my place and you can follow me there, ok?"

Pérez responded, "Yes."

             The following morning, Monday, January 4, Dave started

the conversation again, initiating this exchange:

             Dave: Can you meet at 3?

             Pérez: Ok

             Dave: Cool

             Pérez: Ok

             Dave: I spoke with him and he's excited :)
                   He's worrie[d] about what clothes to bring
                   LOL
                   What parking do you want to meet in?
                   Are you busy?


                                   - 7 -
Pérez: Hahahhahha
       Go to Guaynabo Plaza and I'll tell you where
       we'll meet
       Remember that I want to talk to you first. I
       need to feel safe.

Dave: Yes, me too, it's a good idea.
      I am also scared.

Pérez: That's why I want to see you by yourself.
       I would like to know you first.

Dave: Yes, he will be at my house

Pérez: Ok

Dave: Waiting with the XBOX and beers LOL

Pérez: What are you like, physically?
      Mmmmm
      I like beer
      He doesn't get in trouble for drinking?

Dave: Like in my profile.
      5'9" or 5'10". Brown hair.

Pérez: Gym body?

Dave: Yes, I lift weights 4-5 days a week
      I am not fat

Pérez: And what's he like?

Dave: Skinny, like a young guy.     He is Boricua, with
      short hair.

Pérez: Ok

Dave: He likes soccer jerseys?
      He's very intelligent and friendly

Pérez: Let's see one another now to talk and be horny
       about what we're going to do.




                      - 8 -
The two men eventually agreed to meet at the Martinez Nadal train

station at 4 p.m.

          At the appointed time, Agent Seig drove to the station

and parked his vehicle in the parking lot.   Seig had informed other

members of his unit about the meeting, and several additional HSI

agents were also waiting in the parking lot.    Pérez drove into the

parking lot, pulled up alongside Agent Seig's vehicle, and got out

of his car.    HSI agents immediately arrested him.

          On January 27, 2016, a grand jury returned an indictment

charging Pérez with one count of attempted enticement of a minor

in violation of 18 U.S.C. § 2422(b).    Prior to commencement of the

jury trial, the parties submitted proposed jury instructions.

Pérez filed a separate ex parte request for an entrapment jury

instruction.

          A two-day jury trial was held beginning on May 15, 2017.

The   government's   case   primarily   consisted   of   Agent   Seig's

testimony and the transcripts of the Grindr and text messages.2

Pérez did not present any witnesses.3 At the close of the evidence,




      2The government also presented testimony from two other HSI
agents present at the arrest.     An AT&T security manager also
explained how he confirmed that the phone which sent the messages
belonged to Pérez.

      3Pérez attempted to present character witnesses, but the
court excluded the testimony as impermissible under the Federal
Rules of Evidence because there was no pertinent character trait
associated with the crime charged.


                                   - 9 -
Pérez moved for acquittal under Rule 29. The district court denied

the motion.          The parties participated in a charging conference,

which was not recorded.            Nevertheless, the record indicates that

Pérez renewed his request for an entrapment jury instruction at

that conference because the district court denied the entrapment

instruction in a docket entry, stating, "The ruling is based on

the arguments presented by the government and defendant's response

during the charging conference in connection with predisposition.

In the end, the evidence presented at trial did not justify an

entrapment instruction."              Before instructing the jury, the court

asked       the     parties   if   there      were    "any     objections      to   the

instructions."         Pérez did not raise any objections at that time.

After       charging    the   jury,    the   district    court    did    not    invite

objections from the parties.               Pérez did not raise any objection.

The jury deliberated for less than one hour and returned a guilty

verdict.          On May 14, 2019, Pérez was sentenced to 151 months of

incarceration.

               Pérez    timely     filed     this    appeal.      In    addition    to

challenging the sufficiency of the evidence, he asserts that the

district court erred in rejecting his request for an entrapment

instruction.4



      Pérez raises four additional claims of error: (1) inadequate
        4

questioning during voir dire, (2) violations of the Jones Act, see
48 U.S.C. § 864 (requiring that all trial proceedings in the



                                             - 10 -
                                  II.

            We review de novo the district court's denial of Pérez's

properly preserved claim that the evidence presented at trial was

insufficient to support the jury's verdict.        See United States v.

Tanco-Baez, 942 F.3d 7, 15 (1st Cir. 2019).             In evaluating a

sufficiency of the evidence claim, "we examine the evidence, both

direct and circumstantial, in the light most favorable to the

prosecution   and   decide   whether    that   evidence,   including   all

plausible   inferences   drawn   therefrom,    would   allow   a   rational

factfinder to conclude beyond a reasonable doubt that the defendant

committed the charged count or crime." United States v. Velázquez-

Aponte, 940 F.3d 785, 798 (1st Cir. 2019) (quoting United States

v. Díaz-Rosado, 857 F.3d 116, 120–21 (1st Cir. 2017)).

A. The Elements of the Offense

            Pérez was found guilty of violating 18 U.S.C. § 2422(b),

which provides:

            Whoever, using the mail or any facility or
            means of interstate or foreign commerce, or
            within the special maritime and territorial
            jurisdiction of the United States knowingly
            persuades, induces, entices, or coerces any
            individual who has not attained the age of 18


District of Puerto Rico be conducted in English), and the Court
Reporter Act, see 28 U.S.C. § 753(b) (requiring federal court
proceedings to be recorded verbatim), (3) improper opinion
testimony, and (4) improper exclusion of a character witness.
Except for some observations on the voir dire process, we do not
address the other issues raised given our conclusion that Pérez's
conviction must be vacated on the basis of the court's failure to
give an entrapment instruction.


                                   - 11 -
            years, to engage in prostitution or any sexual
            activity for which any person can be charged
            with a criminal offense, or attempts to do so,
            shall be fined under this title and imprisoned
            not less than 10 years or for life.

To support a conviction under the attempt portion of the statute,

the government must show that the defendant attempted to "(1) use

a facility of interstate commerce (2) to knowingly persuade,

induce, entice, or coerce (3) an individual under the age of 18

(4) to engage in illegal sexual activity."5       United States v. Berk,

652 F.3d 132, 138 (1st Cir. 2011) (quoting United States v.

Gravenhorst, 190 F. App'x 1, 3 (1st Cir. 2006) (per curiam)).

            To prove an attempt, the government must establish both

a   specific   intent   to   commit   the   substantive   offense   and   a

substantial step toward its commission.         Id. at 140.   Hence, for

conviction under § 2422, the specific intent required is the intent

to persuade, induce, entice, or coerce a minor into engaging in

illegal sexual activity.      We have interpreted this requirement as

broadly requiring an intent "to achieve a mental state -- a minor's

assent -- regardless of the accused's intentions vis-à-vis the

actual consummation of sexual activities with the minor."           United

States v. Dwinells, 508 F.3d 63, 71 (1st Cir. 2007) (emphasis

omitted).


      5Here, the government argued, the illegal sexual activity
was sexual assault under Puerto Rico law. See P.R. Laws Ann. tit.
33, § 5191(a) (defining sexual assault to include sex with someone
under age sixteen).


                                      - 12 -
            A substantial step toward commission of an offense is

"less than what is necessary to complete the substantive crime,

but more than 'mere preparation.'"      Berk, 652 F.3d at 140 (quoting

United States v. Piesak, 521 F.3d 41, 44 (1st Cir. 2008)).             This

requirement    serves   to   "distinguish   between   those   who   express

criminal aims without doing much to act on them and others who

have proved themselves dangerous by taking a substantial step down

a path of conduct reasonably calculated to end in the substantive

offense."     United States v. Doyon, 194 F.3d 207, 211 (1st Cir.

1999).   We have found that a variety of actions, including actions

short of meeting the minor in person, can constitute a substantial

step toward a § 2422(b) offense.       See United States v. Rang, 919

F.3d 113, 121 (1st Cir. 2019) (defendant reserved hotel room and

sought consent from the minor's mother for a "sleepover" with the

minor); Berk, 652 F.3d at 140 (defendant offered to help a woman

find housing in exchange for sex with her daughter and sent the

woman leads about homes for rent); Gravenhorst, 190 F. App'x at 4

(defendant sent minors sexually explicit messages and proposed

meeting in person).     But see Berk, 652 F.3d at 140-41 (noting that

"explicit sexual talk alone" does not constitute a substantial

step toward a § 2422(b) offense (citing United States v. Gladish,

536 F.3d 646, 652 (7th Cir. 2008))).         Direct communication with a

minor, real or fictitious, is not required.           A person can commit

a § 2422(b) offense by communicating with an adult who acts as an


                                    - 13 -
"intermediary" between the defendant and a minor.    See Berk, 652

F.3d at 140.

B. The Sufficiency of the Evidence Against Pérez

           On the first element, intent, Pérez argues that the

government failed to provide enough evidence to allow a jury to

conclude that he intended to persuade, induce, entice, or coerce

a minor.    He asserts: "There was no reason to do that [i.e.,

persuade, induce, entice, or coerce] here because the agent offered

[a minor] he presented as already ready, willing, and experienced,

'lik[ing] everything.'"   In his view, the evidence, at most, could

allow the jury to conclude that Pérez communicated with an adult

with the intention of "bringing about a meeting at which prohibited

conduct was supposed to, or likely to occur."

           Pérez's focus on the fictitious minor's supposed sexual

experience and willing participation is seriously misplaced.     A

child who has previously been sexually abused or is otherwise

depicted as "experienced" can still be a victim of persuasion,

inducement, enticement, or coercion.   See United States v. Hinkel,

837 F.3d 111, 116 (1st Cir. 2016) (upholding a § 2422(b) conviction

where the minor was described as "15 but experienced").      And a

child's expression that he "like[s] it" and wants to engage in

illegal sexual activity does not mean that persuasion, inducement,

enticement, or coercion could not possibly play a role.        See

Dwinells, 508 F.3d at 67 (upholding a § 2422(b) conviction where


                                 - 14 -
law enforcement agents posing as minors responded positively to

the defendant's sexual advances, including one fictitious minor

who "assured him that she would consent" to sexual activity in

person).   To suggest otherwise is to misunderstand the nature of

child sexual abuse.   See United States v. Gonyer, 761 F.3d 157,

167 (1st Cir. 2014) (describing the process of a sexual predator

"grooming" a child to form an emotional connection which would

lead the child to be persuaded to engage in sexual activity);

United States v. Brand, 467 F.3d 179, 203 (2d Cir. 2006) ("Child

sexual abuse is often effectuated following a period of 'grooming'

and the sexualization of the relationship." (quoting Sana Loue,

Legal and Epidemiological Aspects of Child Maltreatment, 19 J.

Legal Med. 471, 479 (1998))).

           It was reasonable for the jury to believe that the

fictitious eleven-year-old boy Dave "offered" to Pérez would not

participate in the planned sexual encounter absent persuasion,

inducement, coercion, or enticement -- at a minimum, "implicit

coaxing or encouragement."    See United States v. Montijo-Maysonet,

974 F.3d 34, 42 (1st Cir. 2020) ("[T]he four verbs Congress

used -- including 'entice' and 'induce' -- plainly reach implicit

coaxing or encouragement designed to 'achieve . . . the minor's

assent' to unlawful sex[.]" (second omission in original) (quoting

Dwinells, 508 F.3d at 71)).    And it was reasonable for the jury to

conclude that Pérez must have been cognizant of that reality and


                                  - 15 -
was relying on Dave to affect his "boyfriend's" mental state such

that the minor would participate.          Although Agent Seig's text

messages can be read to imply that Dave had already groomed the

minor for the sexual activity, the jury could reasonably infer

that Pérez intended to use Dave as an intermediary to "entice"

(meaning "to draw on by arousing hope or desire: allure, attract,"

id.) the minor into participating in illegal sexual activity with

Pérez on January 4, 2016.

          On    the   second    element,    substantial   step,     Pérez

emphasizes that he never communicated directly with a minor.          Such

communication is not required to establish a substantial step

towards commission of a § 2422(b) offense.      In Berk, we recognized

that "a defendant can be convicted [of a § 2422(b) offense] even

if the relevant communications are with an intermediary."             652

F.3d at 140.    Berk involved communications between the defendant

and parents of minor children, but we did not state that only

parents could serve as intermediaries in the commission of a

§ 2422(b) offense.    See id.   Indeed, the rationale for relying on

a sexual predator's use of intermediaries extends to any adult

with sufficient influence or control over a minor.           As explained

by the Third Circuit, in an opinion cited in Berk,           § 2422(b) is

"part of an overall policy to aggressively combat computer-related

sex   crimes   against   children[]   [and]   [i]t   would     be   wholly

inconsistent with the purpose and policy of the statute to allow


                                   - 16 -
sexual predators to use adult intermediaries to shield themselves

from prosecution."       United States v. Nestor, 574 F.3d 159, 162 (3d

Cir. 2009); see also Montijo-Maysonet, 974 F.3d at 42 ("Congress

. . . meant to cast a broad net (consistent with the Constitution)

to catch predators who use the Internet to lure children into

sexual encounters." (citing H.R. Rep. 105-557, at 21 (1998), as

reprinted in 1998 U.S.C.C.A.N. 678, 678–79)).

             The "broad net" plainly must cover a defendant who

attempted    to    use     any   intermediary    adult   perceived    to    have

sufficient    sway    to    "lead   a   child    to   participate    in   sexual

activity."     See United States v. Douglas, 626 F.3d 161, 164 (2d

Cir. 2010). The defendant's understanding of the nature and degree

of the adult's control over the minor is a question of fact for

the jury.    Here, the jury could reasonably infer that an adult man

whose "boyfriend" is a minor, and who confidently invites another

man to have sex with the child, would have been viewed by the

defendant as      someone with the power        to elicit the minor's assent

to illegal sexual activity.6

             Pérez   similarly      argues   a    lack   of   evidence     of   a

substantial step because the evidence showed he arrived at the




     6 Pérez mischaracterizes the evidence by describing Dave as
"a part-time tutor" to the minor. While Dave did mention that the
minor was his student, he more importantly described him as his
"boyfriend" and a person with whom he had an ongoing sexual
relationship for six months.


                                        - 17 -
parking lot to meet Dave, not the minor. We agree with the district

court that "the act of traveling to meet an intermediary . . . has

been held sufficient to establish a 'substantial step.'"            United

States v. Pérez-Rodríguez, No. 16-041 2016, WL 7442650, at *2

(D.P.R. Dec. 27, 2016) (citing Berk, 652 F.3d at 140).             Drawing

all inferences in favor of the government, a rational jury could

find that Pérez's communications with Dave and his subsequent

arrival   at   the   meeting   he   arranged   with   Dave   constituted   a

substantial step to persuade, induce, entice, or coerce a minor.

Thus, there was sufficient evidence to convict and the motion for

acquittal was properly denied.

                                    III.

           The district court declined to instruct the jury as to

the elements of Pérez's primary defense, entrapment, because, in

its view, the record did not contain sufficient evidence to warrant

the instruction.      Pérez argues that this omission denied him a

fair trial.

A. Standard of Review

           Preserved objections to the denial of a requested jury

instruction are subject to plenary review. United States v. Joost,

92 F.3d 7, 12 (1st Cir. 1996).        If, however, the defendant fails

to preserve his claim of entitlement to a jury instruction, the

claim is forfeited, and we review the district court's decision

under the plain error standard of Rule 52(b) of the Federal Rules


                                      - 18 -
of Criminal Procedure.            United States v. Baltas, 236 F.3d 27, 36

(1st Cir. 2001).          It has been the longstanding rule of this circuit

to treat a challenge to jury instructions as forfeited if the

defendant fails to object to the instructions after the judge has

charged the jury, regardless of whether he previously brought the

matter to the judge's attention.               United States v. Wilkinson, 926

F.2d 22, 26 (1st Cir. 1991) ("As we have repeatedly held, . . .

[a] party may not claim error in the judge's charge to the jury

unless that party 'objects' after the judge gives the charge but

before the 'jury retires . . . .'" (quoting Fed. R. Crim. P. 30)),

overruled on other grounds by Bailey v. United States, 516 U.S.

137, 149 (1995).          Though Pérez requested an entrapment instruction

before the trial and argued for it at a charging conference, he

did   not   lodge     a    post-charge    objection    to   the    denial   of   the

instruction.7         Thus, Pérez's claim is subject to plain error

review.

            To meet the heavy burden of establishing plain error, an

appellant must show "(1) that an error occurred (2) which was clear

or    obvious   and       which   not   only   (3)   affected     the   defendant's

substantial rights, but also (4) seriously impaired the fairness,



       Pérez also failed to make an objection when the judge invited
       7

objections on the record directly before instructing the jury.
Even if Pérez had made such an objection, his claim would still be
subject to plain error review under our precedent because he did
not renew it after the instruction, and we hold parties strictly
to that timing. See Wilkinson, 926 F.2d at 26.


                                           - 19 -
integrity, or public reputation of judicial proceedings."                United

States v. Duarte, 246 F.3d 56, 60 (1st Cir. 2001).                   The first

prong, "error," consists of "[d]eviation from a legal rule."

United States v. Olano, 507 U.S. 725, 732-33 (1993).                 The second

prong requires that the error identified in the first prong is not

"open to doubt or question," though an appellant can meet this

requirement even in the "absence of a decision directly on point."

United States v. Morales, 801 F.3d 1, 10 (1st Cir. 2015).8                    To

establish the third prong, the appellant must show that "it is

reasonably probable that the . . . error affected the result of

the proceedings."        United States v. Latorre-Cacho, 874 F.3d 299,

303 (1st Cir. 2017).            Our analysis under the fourth prong is

guided by our fundamental concern with "the public legitimacy of

our    justice    system[,]     [which]   relies   on   procedures    that   are

'neutral, accurate, consistent, trustworthy, and fair.'"               Rosales-

Mireles v. United States, 138 S. Ct. 1897, 1908 (2018) (quoting

Josh       Bowers &   Paul H.    Robinson,    Perceptions of Fairness and




       We note that, in our circuit, the second prong is sometimes
       8

described as "clear and obvious error," e.g., United States v.
Scott, 877 F.3d 42, 49 (1st Cir. 2017), while in other opinions it
is phrased as "clear or obvious error," e.g., United States v.
Aquino-Florenciani, 894 F.3d 4, 7 (1st Cir. 2018). As far as we
can tell, there is no substantive difference between the two
usages. In fact, we are unaware of any decision suggesting that
the words "clear" and "obvious" have different meanings. We will
use the "clear or obvious" formulation here, which appears to be
the more frequent usage.


                                          - 20 -
Justice: The Shared Aims and Occasional Conflicts of Legitimacy

and Moral Credibility, 47 Wake Forest L. Rev. 211, 215–16 (2012)).

            The plain error standard is a difficult burden for any

appellant to meet.      See United States v. Gelin, 712 F.3d 612, 620

(1st Cir. 2013) ("This multi-factor analysis makes the road to

success   under   the    plain      error       standard     rather    steep;   hence,

reversal constitutes a remedy that is granted sparingly.").                        It is

a particularly challenging standard to meet in the context of an

unpreserved objection to jury instructions.                   See United States v.

Paniagua–Ramos, 251 F.3d 242, 246 (1st Cir. 2001) ("[T]he plain

error hurdle, high in all events, nowhere looms larger than in the

context of alleged instructional errors.").                   Nonetheless, on rare

occasions, the severity of an error in instructing the jury does

rise to the level of plain error and requires vacatur of the

conviction.    See, e.g., Latorre-Cacho, 874 F.3d at 310; United

States v. Delgado-Marrero, 744 F.3d 167, 189 (1st Cir. 2014).

B. The Entrapment Defense

            Entrapment       provides       a    defense      if    law   enforcement

officers "originate a criminal design, implant in an innocent

person's mind the disposition to commit a criminal act, and then

induce    commission    of    the    crime       so   that    the     Government    may

prosecute."    Jacobson v. United States, 503 U.S. 540, 548 (1992);

see United States v. Teleguz, 492 F.3d 80, 84 (1st Cir. 2007)

("Congress could not have intended that its statutes were to be


                                            - 21 -
enforced by tempting innocent persons into violations." (quoting

Sherman v. United States, 356 U.S. 369, 372 (1958)).                     The defense

has two prongs: (1) improper government inducement and (2) the

defendant's lack of predisposition to commit the offense charged.

Id.

             1. Improper Inducement

             Improper inducement, also referred to as "government

overreaching,"     occurs    when   law     enforcement        agents     engage    in

conduct "of the type that would cause a person not otherwise

predisposed to commit a crime to do so."                Hinkel, 837 F.3d at 117.

The mere creation of an "opportunity to commit a crime" through a

"sting" operation does not, in and of itself, constitute improper

inducement.    United States v. Gendron, 18 F.3d 955, 961 (1st Cir.

1994)   (quoting   Jacobson,       503    U.S.     at    550).      Rather,     "[a]n

'inducement' consists of an 'opportunity' plus something else --

typically, excessive pressure by the government upon the defendant

or the government's taking advantage of an alternative, non-

criminal type of motive."           Id.     "Plus" factors that may tip a

government    operation     from    a     permissible      sting       operation   to

improper     inducement     include,      for    example,        intimidation      and

threats,     "dogged   insistence,"         playing       on     the    defendant's

sympathies, and "repeated suggestions."                 Id. (collecting cases).

"[E]ven very subtle governmental pressure, if skillfully applied,

can amount to inducement."          United States v. Poehlman, 217 F.3d


                                          - 22 -
692, 701 (9th Cir. 2000).        The judgment of whether government

conduct has crossed the line from valid law enforcement tactic to

improper inducement is often a difficult factfinding question for

the jury because "the facts [may] fall somewhere in a middle ground

between what is plainly proper and what is plainly improper."

United States v. Acosta, 67 F.3d 334, 338 (1st Cir. 1995); see

also id. ("To assume that we are dealing with a sharp boundary

rather than a spectrum is an illusion.").

             2. Lack of Predisposition

             The second element of the entrapment defense turns on

whether the "defendant was disposed to commit the criminal act

prior to first being approached by Government agents."          Jacobson,

503   U.S.   at   549.   Our   decision   in   Gendron   sets   forth   our

understanding of this element as follows:

             The right way to ask the question, it seems to
             us, is to abstract from -- to assume away --
             the present circumstances insofar as they
             reveal government overreaching. That is to
             say, we should ask how the defendant likely
             would have reacted to an ordinary opportunity
             to commit the crime. By using the word
             "ordinary," we mean an opportunity that lacked
             those special features of the government's
             conduct that made of it an "inducement," or an
             "overreaching."      Was     the     defendant
             "predisposed" to respond affirmatively to a
             proper, not to an improper, lure?

Gendron, 18 F.3d at 962 (citation omitted).         The purpose of this

predisposition inquiry is to determine whether the defendant is

"someone who would likely commit the crime under the circumstances


                                    - 23 -
and for the reasons normally associated with that crime, and who

therefore poses the sort of threat to society that the statute

seeks to control, and which the government, through the 'sting,'

seeks to stop."       Id. at 963.          The "critical time"       for the

predisposition analysis is the time "in advance of the government's

initial intervention."       United States v. Gifford, 17 F.3d 462, 469

(1st Cir. 1994); see also United States v. Gamache, 156 F.3d 1, 12

(1st Cir. 1998) ("[T]he concept of predisposition has a definite

temporal reference: 'the inquiry must focus on a defendant's

predisposition     before     contact    with    government   officers    or

agents.'" (quoting United States v. Brown, 43 F.3d 618, 627 (11th

Cir. 1995)); Poehlman, 217 F.3d at 703 ("Quite obviously, by the

time a defendant actually commits the crime, he will have become

disposed to do so.    However, the relevant time frame for assessing

a defendant's disposition comes before he has any contact with

government     agents,      which   is    doubtless    why    it's    called

predisposition.").       While evidence of the defendant's response to

the government's inducement may be relevant to the predisposition

inquiry, that evidence must be evaluated in terms of what it

reveals about the defendant's readiness to commit the crime before

the government contacted him.       See Gifford, 17 F.3d at 469.

             We have advised trial courts that the following factors

may be useful in evaluating the evidence of predisposition or lack

thereof:


                                        - 24 -
          (1) the character or reputation of the
          defendant; (2) whether the initial suggestion
          of criminal activity was made by the
          Government; (3) whether the defendant was
          engaged in the criminal activity for profit;
          (4) whether the defendant showed reluctance to
          commit the offense, which was overcome by the
          governmental persuasion; and (5) the nature of
          the inducement or persuasion offered by the
          Government.

Gamache, 156 F.3d at 9–10.     The second, fourth, and fifth of these

factors are also relevant to the improper inducement analysis.

Thus, while improper inducement and lack of predisposition are two

separate prongs, the same factual evidence will often be relevant

to both prongs.

          3. The Defendant's Burden of Production

          A   defendant   is   entitled   to   a   jury   instruction   on

entrapment if he meets a modest burden of production on the two

prongs of the defense.     United States v. Rodriguez, 858 F.2d 809,

814 (1st Cir. 1988).      This rule is in keeping with the "general

proposition [that] a defendant is entitled to an instruction as to

any recognized defense for which there exists evidence sufficient

for a reasonable jury to find in his favor."          Mathews v. United

States, 485 U.S. 58, 63 (1988).

          In analyzing whether the defendant has met his burden,

the court must construe the evidence in the light most favorable

to the defendant.    Rodriguez, 858 F.2d at 813.           An entrapment

instruction is required if the evidence, viewed in this charitable



                                   - 25 -
fashion, "furnishes an arguable basis for application of the

proposed rule of law."    Id. at 814 (quoting United States v. Coady,

809 F.2d 119, 121 (1st Cir. 1987)).            In other words, the record

must contain evidence that makes the entrapment theory "plausible"

or "superficially reasonable."         Gamache, 156 F.3d at 9.        As we

have previously emphasized, "[t]his is not a very high standard to

meet."   Id.

          A defendant does not need to introduce his own evidence

to meet this burden.     Rodriguez, 858 F.2d at 813.        He may rely on

"evidence adduced during the government's case" or "any probative

material in the record."       Id.    The proof may be "circumstantial

rather than direct."     Id.    If there are factual disputes in the

record, the court is not permitted to "weigh the evidence, make

credibility determinations, or resolve conflicts in the proof."

Gamache, 156 F.3d at 9. If the parties argue competing inferences,

the court must draw all reasonable inferences in favor of the

defendant's entrapment theory.        Id.   Ultimately, if "a reasonable

jury could view the evidence as establishing that defendant was

entrapped . . . [the defendant] [i]s entitled to an entrapment

instruction."     Teleguz,     492   F.3d   at   84.   Determining   whether

government conduct has crossed the line into improper inducement

or whether a person was predisposed to commit an offense are

delicate questions of fact for the jury to sort out.           See Acosta,

67 F.3d at 338.    Thus, a judge should not hesitate to send the


                                      - 26 -
question to the jury if there is even ambiguous evidence of

entrapment.

           Once   the   defendant   meets   his    burden   of    production,

entrapment becomes a question of fact for the jury.              Id.    At that

stage,   the   government   bears   the   burden    of   proving       beyond   a

reasonable doubt either that there was no improper inducement or

that the defendant was predisposed to commit the offense.               Id.     If

"a rational jury could decide either way, its verdict will not be

disturbed."    Id.

                                    IV.

           Consistent with our earlier explanation of the plain

error standard, Pérez is entitled to relief if he is able to

demonstrate that: (1) the district court erred in failing to give

an entrapment instruction; (2) his entitlement to that instruction

was clear or obvious; (3) the omission affected his substantial

rights; and (4) it undermined the fundamental fairness of the

trial.   See Duarte, 246 F.3d at 60.

A.   Error

           The district court denied Pérez's requested entrapment

instruction for failure to meet his burden of production on the

lack of predisposition prong, without addressing whether Pérez had

met his burden of production on the improper inducement prong.

Because the defendant is required to meet the burden of production

on both prongs, a court may deny an entrapment instruction based


                                    - 27 -
on a failure to show evidence on one prong or the other, without

discussing both.    See, e.g., United States v. Rivera-Ruperto, 846

F.3d 417, 431 (1st Cir. 2017); United States v. Sánchez-Berríos,

424 F.3d 65, 77 (1st Cir. 2005).           Because we disagree with the

district court's assessment of the evidence on predisposition, we

must consider both prongs.        If the defendant failed to meet his

burden of production on the improper inducement prong, an error by

the judge in the assessment of the predisposition prong would be

harmless.

            We   also    repeat     that      improper     inducement      and

predisposition     are   analytically        linked   in     that     improper

inducement, and the defendant's responses to it, are part of the

evidence courts should consider in deciding whether the defendant

met his burden of production on the lack of predisposition prong.

Gamache, 156 F.3d at 9–10; see Joost, 92 F.3d at 13-14 ("As for

the absence of predisposition prong, much of what we have pointed

to [in the improper inducement analysis] is relevant.").                    In

evaluating the question of whether the defendant was predisposed,

the factfinder must "abstract from -- . . . assume away -- the

present     circumstances   insofar     as     they      reveal     government

overreaching."     Gendron, 18 F.3d at 962 (emphasis omitted).              If

there was no improper inducement, we already have our answer as to

how the defendant would respond to "an ordinary opportunity to

commit the crime" and any further analysis of predisposition is


                                    - 28 -
unnecessary.    Id. (emphasis omitted).           But if there was improper

inducement, the nature of that inducement and the defendant's

responses to it are relevant to the predisposition analysis to the

extent that they allow inferences about the defendant's state of

mind prior to the government's intervention.            Rodriguez, 858 F.2d

at 816 (considering evidence of the defendant's responses to

improper inducement because "later events often may shed light on

earlier motivations").

           1.   Improper Inducement

           Agent Seig created a Grindr profile appearing to belong

to an adult named "Dave W."               The profile described Dave as

"[m]uscular, [w]hite, [s]ingle."            Pérez sent a message to that

profile, presumably believing he was speaking with that adult man.

Dave quickly turned the conversation towards sexual activity with

a minor by offering to arrange a sexual encounter with his eleven-

year-old "boyfriend."       Dave said that both he and the minor would

be part of the encounter, stating it would be "him you and I" and

describing the encounter as a "threesome."            This type of "bundling

of licit and illicit sex into a package deal" can constitute a

"plus factor" for purposes of establishing improper inducement.

Hinkel,   837   F.3d   at   118;   see    also    Gendron,   18   F.3d   at   961

(describing "the government's taking advantage of an alternative,

non-criminal type of motive" as a "typical[]" example of an

inducement plus factor).


                                         - 29 -
            Agent Seig, writing as Dave, represented from the start

that the eleven-year-old minor was his "boyfriend" -- a term which

suggests    the legally impossible notion that         the minor was a

consenting participant in a sexual and romantic relationship with

Dave.   Agent Seig repeatedly stated that this imagined encounter

would be a positive experience for the minor.             Such repeated

suggestions "downplay[ing] the harm" caused by child sexual abuse,

or otherwise justifying it, can constitute a "plus factor" which

a jury may rely on to find improper inducement.          See Hinkel, 837

F.3d at 118 (stating that the defendant presented evidence of

"clever and sophisticated inducement" where the law enforcement

agent "on numerous occasions, downplayed the harm that could be

expected to flow from the commission of the crime by describing

how 'amazing' the encounter would be, how 'excited' 'Samantha'

was, and how 'Lisa' 'appreciate[d]' how 'honest and caring' Hinkel

had been in his messages"); Gamache, 156 F.3d at 11 (stating that

the   law   enforcement   agent's   repeated   "justifications   for   the

illicit activity (intergenerational sex) by describing 'herself'

as glad that Gamache was 'liberal' like her, expressing that she,

as the mother of the children, strongly approved of the illegal

activity, and explaining that she had engaged in this conduct as

a child and found it beneficial" constituted evidence of improper

inducement); see also Jacobson, 503 U.S. at 540 (describing the

government's     improper     inducement       as   including    repeated


                                     - 30 -
"suggesti[ons] that petitioner ought to be allowed to do what he

had been solicited to do," i.e., purchase child pornography).

            Hence, the record contained evidence that would allow a

jury to find      two significant "plus" factors in Agent Seig's

communications with Pérez: first, Seig's linking the opportunity

for adult sexual activity, a lawful objective of Grindr users,

with the unlawful sexual activity involving a minor -- establishing

a kind of prerequisite for the adult activity; second, Seig's

repeated suggestions that the illegal conduct was not harmful, but

actually beneficial, to the minor.        Thus, a reasonable jury could

have found improper inducement -- a necessary precondition for a

defendant    to     meet   his   burden   of   production   on   lack   of

predisposition.

            2.    Lack of Predisposition

            Pérez met his burden of production on the lack of

predisposition prong if the record would permit a reasonable

inference by the jurors that, before his interaction with Agent

Seig, Pérez was not predisposed to commit the crime of enticing a

minor to commit unlawful sexual activity.        See Gendron, 18 F.3d at

962.   The five factors identified in Gamache guide our analysis.

See 156 F.3d at 9-10.

            As to the first factor, the character or reputation of

the    defendant,    the   evidence    might   include   prior   criminal

convictions for similar offenses or a history of sexual interest


                                      - 31 -
in minors.      Tellingly, the record contains no such evidence.                   See

id. at 12 ("[T]here was no evidence presented that Gamache had

engaged in similar activities independent of this sting operation.

The jury could have relied on this evidence to find a lack of

predisposition . . . ."); see also Hinkel, 837 F.3d at 118 (stating

that the defendant produced sufficient evidence to "clearly" meet

his prima facie burden of a lack of predisposition because, inter

alia, "the government had not uncovered any evidence suggesting

that he had other underage victims").               The absence of any kind of

negative    character       evidence    relating     to    sexual    activity     with

minors     is   one   point     in     favor   of    allowing       the   entrapment

instruction.

             There    are    two     statements     from   Pérez     early   in   the

conversation with Dave that "I started at 8."                   As noted earlier,

the exchange begins as follows:

             Pérez: Hello what are you doing?

             Dave: Hey what's up

             Pérez: Let's see you

             Dave: Cool, do you like really young guys?


             Pérez: Yes
                    Age?
                    I started at 8

             Dave: Me? 35, but my boyfriend is young

             Pérez: Hahhaha Okk
                    How old is he?


                                          - 32 -
                 What does your boyfriend like?

          Dave: He likes everything :)
                He is very young, what age do you like?

          Pérez: The younger the better
                 I don't discriminate
                 I started at 8 hehehhe
                 So you tell me
                 What does he like to do?
                 We are close, we can come up with some fun
                 From there up I do it all

          Dave: Do you understand English? I speak only a little
                Spanish
                My boyfriend is 11 years old. Do you want to play
                with him?

          Pérez: Mmmm yessss
                 Where is he?
                 I speak little only a little English?
                 Share pics??
                 You tell me when and where???
                 Do you prefer to call?
                 Yes, I want to play


          The dissent states that, "in context," the exchange

plainly reflects a "stark pre-dispositional admission by Pérez."

In fact, however, the dissent ignores the context of Pérez's

statements that "I started at 8."   Both statements are made before

the notion of sex with a minor entered the conversation ("My

boyfriend is 11 years old.   Do you want to play with him?").    Until

Dave   talks   about   his    eleven-year-old     "boyfriend,"    the

conversation, which took place on a dating app for adults, can be

read as discussing sex with young adults.       When Dave refers to

himself as thirty-five, he could be saying that he is thirty-five



                                 - 33 -
years old, or that he started having his sexual experiences at age

thirty-five.     Clearly, he (i.e., Agent Seig, posing as Dave) is

not saying that his partners in his sexual experiences are thirty-

five.     It thus remains unclear, when Pérez reiterates that he

"started at 8," whether he is referring to the beginning of his

own sexual experiences or the age of boys with whom he has had

sex.

            The dissent similarly ignores the context when Pérez

says, "the younger the better."          Here, too, he makes the statement

before Dave made any reference to his "boyfriend" being underage.

Thus, it is hardly clear that Pérez is admitting to having an

interest in children rather than meaning that he is interested in

younger    adults.      The    latter      interpretation    is    plausible,

particularly in light of Dave's reference to "really young guys,"

(the word "guys" tending to imply adults), and the fact that Pérez

made the comments on an adults-only dating app.              As for Pérez's

apparent eagerness when he discovers that Dave's "boyfriend" is

only eleven, we have said in our case law that " eagerness alone

. . . is not sufficient to remove the predisposition question from

the jury's purview."     Gamache, 156 F.3d at 12.

            Hence, the text is ambiguous enough that a jury, not a

judge, needed to determine its meaning.               See id. at 9 ("[T]he

court's function is to examine the evidence on the record and to

draw    those   inferences    as   can   reasonably   be   drawn   therefrom,


                                         - 34 -
determining whether the proof, taken in the light most favorable

to the defense can plausibly support the theory of the defense.").

Thus,       for   the   purpose   of     evaluating   the   evidence   on   the

predisposition prong, the "I started at 8" statements do not

provide evidence of a history of sexual interest in minors.

              On the second factor, the initial suggestion of criminal

activity, it is indisputable that the government first suggested

the sexual abuse of a minor.              In fact, as we have noted, Pérez

encountered law enforcement on a forum intended to be used only by

adults.9      The jury could reasonably draw the inference from Pérez's

use of Grindr that, before his conversation with "Dave," he was

interested in sex with other adult men, not children.             Indeed, the

expert psychologist who testified at sentencing drew this same

inference, stating: "A pedophile will not be using, my personal

clinical opinion, I don't think they will use Grindr because he

will be easily identified."            Although Agent Seig testified that he

designed his profile to contain "veiled" references which would be

understood as suggesting sexual abuse of a minor "by someone who

was versed in communicating in the realm of pedophiles," we must

interpret the evidence in the manner most charitable to Pérez.




      Agent Seig testified that profiles explicitly seeking sexual
        9

encounters with minors "would be removed from the social network,
because many people would report that and then the owners of the
network would remove it."


                                          - 35 -
Here, there is no basis for concluding on this record that Pérez

understood these veiled references.

             The third factor -- whether the defendant engaged in the

criminal activity for profit -- is not relevant here, but we note

that monetary profit was not at issue.

             As for the fourth factor, "whether the defendant showed

reluctance to commit the offense," the transcripts show that Pérez

insisted on meeting Dave without the minor's presence.      Taken in

the light most favorable to Pérez, as it must be at this stage,

this insistence can be read as a sign of some reluctance to commit

the crime.     Pérez made clear that any subsequent meeting with the

minor would depend on how the meeting with Dave went, and it is a

reasonable inference from the messages that Pérez had not made up

his mind about actually meeting the child.        A jury could also

conclude from Pérez's insistence on meeting with Dave alone, his

repeated statements that he wanted to get to know Dave first, and

his clear interest in Dave, that Pérez was hesitant about moving

beyond the realm of fantasy with a minor and was motivated by a

desire to "be horny" with an adult in whom he was sexually

interested.      Although a jury could also conclude that Pérez

intended to proceed directly to a meeting with the minor after

seeing Dave and ensuring he was not a law enforcement officer,

that plausible inference is not sufficient to take the entrapment

defense from the jury.      See Gamache, 156 F.3d at 10 (explaining


                                   - 36 -
that whether the government disputes the defendant's version of

the facts is "irrelevant to the question of whether it raises an

issue of entrapment to be put before the jury"); Rodriguez, 858

F.2d   at   815    (explaining   that    it    is   sufficient      that   "[the

defendant's] version, whether or not it strikes us as particularly

credible,    is    neither   thoroughly       implausible    nor    constructed

entirely of gauzy generalities").

            The fifth factor, "the nature of the inducement or

persuasion offered by the Government," brings us back to the

improper inducement analysis.           From the very beginning of the

conversation, Pérez expressed his interest in "Dave," an adult

man.   Before either party said anything about a minor, Pérez said

to Dave, "Let's see you," likely meaning that he wanted to see a

picture of "Dave."        Later in the conversation, Pérez asked Dave

for pictures again and for a physical description of his body.                 A

juror could reasonably infer that Pérez was primarily motivated by

sexual interest in "Dave," not the minor.             Pérez also asked Dave

questions about how he "got" his "boyfriend."               Drawing inferences

in favor of Pérez, these questions suggest that he asked them

because he had not ever thought about or tried to entice a minor

into sex before, and would not do so without the encouragement of

the government agent and repeated statements "downplaying the

harm,"   Hinkel,    837   F.3d   at   118,    or,   even    more   offensively,

normalizing the sexual behavior with the minor.


                                        - 37 -
          To be sure, there are different inferences one could

draw from the communications between Pérez and Dave.        But, in

determining whether the defendant has met his burden of production,

we are required to draw all inferences in favor of the defendant.

The evidence relevant to the factors listed in Gamache provides at

least some evidence of lack of predisposition.    Thus, the record

met Pérez's modest burden of production, and the district court

erred by denying the entrapment instruction.

B.   Clear or Obvious Error

          1.   Relevant First Circuit Precedent

          Prior to Pérez's trial in May 2017, our court had decided

two significant cases addressing the circumstances in which a

defendant is entitled to jury instructions on the entrapment

defense in the context of child sexual abuse sting operations:

Hinkel, 837 F.3d at 111, and Gamache, 156 F.3d at 1.   Because these

cases reveal the clarity of the district court's error, we describe

their facts in some detail.

          a.   Hinkel

          Hinkel was convicted of attempted enticement of a minor

in violation of § 2422(b) -- the precise offense at issue here --

after email correspondence with a law enforcement agent posing as

"Lisa," the thirty-eight-year-old mother of a fictitious fifteen-

year-old girl, "Samantha."    Hinkel, 837 F.3d at 116.       Hinkel

contacted "Lisa" based on a personal ad posted to an "online


                                - 38 -
message      board    .    .   .    frequented        by     those   seeking     adult    sex

partners."      Id. at 115.             The ad stated, "mom with daughter looking

for taboo relationship."                  Id. at 116.        Hinkel responded with an

email containing "graphic descriptions of sexual acts that he

imagined engaging in with 'Lisa' and her daughter."                               Id.     The

government agent posing as "Lisa" promptly told Hinkel that her

daughter was "15 but experienced," to which Hinkel responded,

"Sounds very naughty!              I am concerned about her age since legally

she should be 16 or older."                 Id.      The agent answered "she[']s not

[16 or older] so i guess this conversation is over."                            Id.    Hinkel

immediately replied, "Nope..... It is not over! I want to talk

more!   I'm    very       intrigued        by   it    all.    Such   taboo   and      naughty

play!!!!"      Id.

              For the next month, Hinkel continued to correspond with

Lisa    in    "lurid      detail"         about    his     desire    to   have    sex    with

"Samantha,"      though            he     occasionally        expressed      "conflicting

feelings." Id. at 116-17. Lisa reassured Hinkel, writing "i think

you will love her...and i appreciate the way you describe our

situation."      Id. at 117.              Hinkel also exchanged sexually graphic

emails with Samantha directly.                    Id.      Hinkel and Lisa made plans

for Hinkel to visit and have sex with Samantha.                           Id.    Lisa told

him that the planned encounter would be "such an amazing experience

for us to have together." Id. When Hinkel arrived at the appointed

time and place, he was arrested and subsequently charged and


                                                  - 39 -
convicted of a § 2422(b) offense. Id. At his trial, the government

introduced evidence of "five cartoons, which consist of detailed

anime drawings of adults and minors engaged in sex acts" that law

enforcement had found on Hinkel's computer.    Id. at 122.

          Hinkel's primary defense at his trial was entrapment,

and -- unlike here -- the district court instructed the jury on

the elements of that defense.   Id.    On appeal, Hinkel claimed the

government's evidence was insufficient to overcome the entrapment

defense. Id. We rejected that challenge because it was reasonable

for the jury to find that entrapment had not occurred.       Id. at

120.   Of importance here, however, is our explicit consideration

of whether Hinkel had satisfied his burden of production even

though the district court had instructed the jury on entrapment.

Id. at 118.    Hence, although the posture of Hinkel was different,

its discussion of the facts that clearly met the threshold for an

entrapment instruction is directly applicable here.

          b.   Gamache

          Following a postal service correspondence with a law

enforcement agent posing as a mother of three young children,

Gamache was convicted of travel with intent to engage in illicit

sexual conduct with a minor in violation of 18 U.S.C. § 2423(b),

and an attempt to use a minor to produce sexually explicit images

in violation of 18 U.S.C. § 2251(a).    Gamache, 156 F.3d at 2.   The

agent had published a personal ad in an adult magazine which read,


                                 - 40 -
in part, "female, 31; Single mom, two girls, one boy, seeks male

as partner and mentor, seeks fun, enjoys travel and photography."

Id. at 3.     Gamache responded with interest in the adult female

author of the advertisement.    Id.

            The   agent,   posing     as     "Frances,"     steered   the

correspondence toward sex with her three minor children, ages

twelve, ten, and eight.    Id. at 4.       Frances wrote that she wanted

to "introduc[e] an adult male to further [her] children's sexual

education and experiences."    Id.     Gamache responded that he was

"not shocked" and that he would be "honored" to be chosen as the

adult man to have sex with Frances's children.        Id.    Over several

months of continuing correspondence, Frances described sexual

activities she wanted Gamache to engage in with her children, and

Gamache replied in kind, sharing his own ideas and desires.           Id.

at 4-7.   He also sent a letter to the children describing sexual

activities he planned to engage in with them. Id. at 7. Throughout

the correspondence, Frances referenced a "kind" uncle who "taught

[her] about sex when [she] was very young, and wanting the same

type of experience for [her] children."         Id. at 4-5 (alterations

in original).     She told Gamache the children were "very excited

about meeting" him, and they arranged for Gamache to meet "Frances"

and her children at a motel.   Id. at 5-7.       When Gamache arrived at

the motel, he was arrested.    Id. at 7.




                                    - 41 -
          Gamache   requested   an     entrapment     instruction   at   his

trial, and the court rejected his request. Id. at 3. His objection

was properly preserved and subject to plenary review.            Id. at 9.

We held that Gamache had met his burden of production on both

prongs of the entrapment defense and that the court erred in

failing to give the instruction.          Id. at 12.      We vacated the

conviction and remanded for a new trial.

          c. Common Principles in Hinkel and Gamache

          Our review of Hinkel and Gamache reveals that, at the

time the district court rejected Pérez's request for an entrapment

instruction,   we   had   previously    held   that    certain   facts    in

combination -- present in both of those cases -- entitled a

defendant to an entrapment instruction.

          In both cases, the government originated the criminal

design and invited the defendants to participate by placing an

ambiguous advertisement in an adults-only forum; then, when the

defendants responded to the advertisements, the government offered

to arrange a sexual encounter involving a minor.         Hinkel, 837 F.3d

at 116; Gamache, 156 F.3d at 10.       In both cases, we noted that the

government agents used the tactic of "bundling . . . licit and

illicit sex into a package deal," meaning that they offered a

sexual encounter that would include both legal sex with an adult

and illegal sex with a minor.     Hinkel, 837 F.3d at 118; see also

Gamache, 156 F.3d at 10.    A key component of the government agent's


                                     - 42 -
strategy in both cases was "downplay[ing] the harm" that would

flow from the crime through repeated statements portraying sex

with a minor as normal or even beneficial.             Hinkel, 837 F.3d at

116; see Gamache, 156 F.3d at 10-11.        In both cases, the defendants

manifested some hesitancy to commit the offense, though most of

their   communications     expressed       eagerness    to   do   so,      and,

ultimately, both defendants showed up for a meeting with the minor.

Finally, in both cases, there was no evidence of the defendants'

prior sexual activity with minors.             Hinkel, 837 F.3d at 116;

Gamache, 156 F.3d at 10.

             Not surprisingly, given these similarities, we cited

Gamache as apt precedent in stating that the defendant met his

burden of production in Hinkel.         The cases, of course, are not

identical.       Gamache   involved    a    more   prolonged      period     of

correspondence and, arguably, more severe government manipulation.

Despite those differences, however, when all inferences are drawn

in favor of the defendant, the record in each case told, in

essence, the same story: a defendant without any known prior sexual

contact with minors moved from his initial, lawful inquiry about

adult sex to what a jury could find was an attempt to commit an

offense involving sexual exploitation of a minor, prompted by

encouragement from the government that a reasonable juror could

deem improper inducement.




                                      - 43 -
             2.   Comparing Pérez's Case with Hinkel and Gamache

             a. Initiation by the Government Agent

             Like the law enforcement agents in Hinkel and Gamache,

Agent Seig purported to be an adult using a forum for adults

seeking adult sexual partners, and alluded to the possibility of

a relationship with a younger person without specifying the nature

of the relationship or the age of the young person.      See Hinkel,

837 F.3d at 116; Gamache, 156 F.3d at 10.     Pérez took the bait and

contacted the agent.     Like Hinkel and Gamache, his initial message

did not include any reference to sex with a minor.         He wrote,

"Hello what are you doing?" and then "Let's see you."      It was the

government agent who turned the conversation to sex with minors,

asking if Pérez "liked really young guys," and then, when he

responded affirmatively, making the offer of sex with a minor: "My

boyfriend is 11 years old.      Do you want to play with him?"     When

Pérez again responded affirmatively, Agent Seig made that offer

more explicit, asking what sex act Pérez wanted to engage in with

the minor.    While Pérez expressed enthusiastic interest, "[i]t was

the Government that first mentioned the 'child[]' as [a] sex

object[]; it was the Government that first used sexually explicit

language involving the 'child[]'; [and] it was the Government that

escalated the subject of sex with [the] child[]."       Gamache, 156

F.3d at 10.




                                   - 44 -
          b. Government's Bundling of Licit and Illicit Sex

          Agent Seig's sting operation relied on precisely the

same tactic we described in Hinkel and Gamache: the "bundling of

licit and illicit sex into a package deal." Hinkel, 837 F.3d at

118; see also Gamache 156 F.3d at 10.      Pérez reached out to Dave

-- described as a "[m]uscular, [w]hite, [s]ingle" adult man -- on

an adult dating application.     He clearly remained interested in

the adult throughout the conversation, including asking for photos

just of Dave when Dave would not send photos of the minor.        These

circumstances permit a plausible inference that Pérez was not

predisposed to sexually abuse a child, but, rather, was motivated

by interest in sex with Dave.   See Gamache, 156 F.3d at 10 (noting

a plausible argument that "all of [Gamache's] correspondence about

sex with minors was a ruse to have sex with 'Frances,' who was his

target from the time that he answered the ad").

          c.   Government   Agent's   Statements   Normalizing   Sexual

     Abuse

          Dave's comments repeatedly portraying sex with a minor

as normal or even beneficial resemble those made by the agents in

Hinkel and Gamache.   See Hinkel, 837 F.3d at 118 (stating that the

agent "downplayed the harm that could be expected to flow from the

commission of the crime by describing how 'amazing' the encounter

would be"); Gamache, 156 F.3d at 11 ("[T]he government agent

provided justifications for the illicit activity         [by]    . . .


                                  - 45 -
expressing that she, as the mother of the children, strongly

approved of the illegal activity, and explaining that she had

engaged in this conduct as a child and found it beneficial to

her."). The government's perverse statements that the minors would

enjoy and benefit from sexual exploitation were important because

such suggestions have the potential to influence the mind of a

person who is not predisposed to abuse children and convince him

that sex with a minor is acceptable. See Gamache, 156 F.3d at 11

("These solicitations suggested that Gamache ought to be allowed

to engage in the illicit activity . . . .").

          d. Defendant's Reluctance to Commit the Offense

          As in Hinkel and Gamache, some of Pérez's actions could

be interpreted as reluctance to commit the offense.   He repeatedly

insisted on meeting with Dave alone, without the minor's presence.

That demand could be interpreted as an indication that he was

reluctant to go through with meeting the minor, despite his many

statements of enthusiasm about doing so.

          To be sure, Pérez's plausible expression of reluctance

differed from the more explicit statements in Hinkel and Gamache.

Still, there was no outright rejection of the criminal conduct in

either of those cases.   Hinkel briefly indicated hesitation when

"Lisa" told him that her daughter was fifteen, but clearly overcame

his reluctance just moments later, stating in response to an

obvious exit opportunity, "Nope..... It is not over! I want to


                                - 46 -
talk more! I'm very intrigued by it all.      Such taboo and naughty

play!!!!"10    See Hinkel, 837 F.3d at 116.   Hinkel subsequently did

arrange and show up at a meeting with the fictitious fifteen-year-

old. Id. at 117.     Gamache initially resisted Frances's suggestion

that he bring a video camera, but he stated his hesitance was based

on technological ignorance, not any moral opposition to creating

child pornography.     See Gamache, 156 F.3d at 12.      In the end,

Gamache did show up for a meeting with the children and brought a

video camera with him.

             e. Defendant's Eagerness to Commit the Offense

             Aside from his insistence on meeting Dave separately

prior to meeting the minor, Pérez's responses to Dave's suggestions

of sexual activity with an eleven-year-old boy were decidedly not

reluctant.    His immediate response to Dave's offer of sex with his

"boyfriend" was "yes," and he made explicit statements about the

sex acts he wanted to engage in with the boy.11    Gamache and Hinkel


     10In an apparent attempt to suggest that Hinkel was reluctant
to engage in sex with a minor in a way that Pérez was not, the
dissent ignores this quick abandonment of any hesitation in its
characterization of Hinkel's response to the prospect of sex with
a minor.

     11The dissent focuses on this immediate affirmative response,
suggesting that Pérez's enthusiasm made the necessity of an
entrapment instruction in this case unclear, and, thus, its
omission was not plain error. But our precedent has been clear on
this point: "[E]agerness alone . . . is not sufficient to remove
the predisposition question from the jury's purview."     Gamache,
156 F.3d at 12. Similarly, the dissent emphasizes that Pérez went



                                  - 47 -
expressed similar reactions to law enforcement agents' criminal

suggestions.        See    Hinkel,      837    F.3d     at   118    (describing          the

defendant's    response        as    "eager[]");      Gamache,      156    F.3d     at   11

(describing the defendant's response as "enthusiastic").                              Both

Hinkel and Gamache gave graphic descriptions of the sex acts they

wanted to engage in with minors.                 See Hinkel, 837 F.3d at 116

(stating that "Hinkel corresponded frequently and in lurid detail

with 'Lisa' and her fictitious daughter 'Samantha'" and that he

"describ[ed] his own sexual desires in detail"); Gamache, 156 F.3d

at   6   (describing       a    letter    from        Gamache      to     Frances     that

"explain[ed], at length and in detail, how he will carry about the

sexual 'education' of 'Frances'' 'children'").

            Our holdings in Hinkel and Gamache make clear that a

defendant     can   meet       his    burden     of     production        on   lack      of

predisposition even if he responded eagerly or enthusiastically to

the proposed criminal conduct.                As we have noted, in Gamache we

explained, "[W]hile 'ready commission of the criminal act can



to meet with Dave just five days after the first message. This
time frame may be another display of eagerness, certainly worthy
of the jury's consideration, but it did not warrant withholding
the entrapment instruction from the jury when other evidence in
the record supported a finding of a lack of predisposition. The
dissent also overlooks the fact that Pérez was arrested, not at a
planned meeting with the minor, but rather, at a meeting with Dave.
Read in the light most favorable to Pérez, he was prepared to meet
with the adult intermediary alone, but had not clearly agreed to
meet with the minor. By contrast, Hinkel and Gamache were arrested
at planned meetings with minors.     See Hinkel, 837 F.3d at 116;
Gamache, 156 F.3d at 7.


                                          - 48 -
itself adequately evince an individual's predisposition' and thus

provide sufficient evidence to support a jury's finding that the

defendant was predisposed to commit the offense, eagerness alone,

when coupled with the 'extra elements' present in this sting

operation, is not sufficient to remove the predisposition question

from the jury's purview."          156 F.3d at 12 (citation omitted)

(quoting   Gifford,    17   F.3d   at    469);   see   also    id.    at   11-12

("[W]illingness to commit the crime, although clearly relevant to

the jury's inquiry, is not sufficient by itself to mandate a

finding that he was predisposed."); Rodriguez, 858 F.2d at 816

("Although a jury might well find that Rodriguez's wiliness, and

the level of experience and enthusiasm which he subsequently

exhibited,     were   inconsistent       with    the   claim     of    initial

unreadiness, such a finding would not be inevitable.").

             f. Prior Sexual Interest in Children

             As Pérez notes, the trial record contained "absolutely

no evidence that, aside from this virtual conversation, Mr. Pérez

had engaged, tried to engage, or would have considered engaging in

sex with a minor."12    In Gamache, we emphasized the importance of

the absence of evidence of prior similar conduct in meeting the

defendant's burden of production on lack of predisposition. See


     12 As noted    above in Section IV.A.2., the meaning of Pérez's
statements that    "I started at 8" is ambiguous. If all inferences
are drawn in his   favor, those statements do not constitute evidence
of prior sexual    interest in children.


                                        - 49 -
Gamache, 156 F.3d at 12 ("[T]here was no evidence presented that

Gamache had engaged in similar activities independent of this sting

operation.    The jury could have relied on this evidence to find a

lack of predisposition . . . .").

             Of course, to address the burden of production on the

predisposition issue, a defendant could introduce some evidence of

positive relationships with children, though Gamache makes clear

that the defendant need not introduce such evidence to meet that

burden.   See id.     Indeed, Hinkel offered evidence that he "had

raised two adult children and had not been accused of having an

inappropriate relationship with either of them."       Hinkel, 837 F.3d

at 118.      However, in Hinkel, there was contrary evidence that

Hinkel had sexual interest in children before the contact with the

government, in the form of cartoon images of adult sexual conduct

with children recovered from his computer.        Id. at 122.      Hinkel

challenged the admission of that evidence on appeal.              Id.   In

rejecting that claim, we recognized that the images were "probative

of   Hinkel's    predisposition"   and   may   tend   to   show   "sexual

inclination towards children."       Id. (quoting United States v.

Chambers, 642 F.3d 588, 595–96 (7th Cir. 2011)).       Still, even with

the record containing evidence of Hinkel's sexual inclination

towards children, we agreed with the district court that Hinkel

had provided enough evidence of lack of predisposition to mount a




                                   - 50 -
"credible entrapment case." Id. at 118.                 Again, there was no such

evidence of Pérez's prior sexual interest in children.

            3.      Conclusion

            As we have described, this case is strikingly similar to

Hinkel and Gamache.          Agent Seig used the same tactics we saw in

those cases -- placing an ambiguous lure on an adults-only forum,

inviting the defendant who responded to the lure to engage in a

"bundled"    sexual     encounter    with     an    adult     and    a    child,    and

repeatedly insisting that this sexual abuse was beneficial to the

child.      Pérez    responded     similarly       to   Hinkel      and   Gamache   --

enthusiastic     interest        coupled     with       a   weak     expression     of

reluctance.      And as in Gamache, the record at Pérez's trial

contained no evidence of any sexual interest in children prior to

the government's intervention.

            In Hinkel, we stated that the facts "clearly" met the

defendant's "'modest' burden of making a prima facie showing that

there is some evidence both elements [of the entrapment defense]

are satisfied."        Hinkel, 837 F.3d at 117; see also id. at 118

(stating that the evidence at Hinkel's trial supported "a credible

entrapment case").       In Gamache, we concluded that "appellant met

the dual burdens required for an instruction on entrapment, because

the   evidence      raises   a   reasonable     doubt       that    the   Government

improperly induced a citizen to commit crimes that he was not

predisposed to commit, yet crimes for which he was charged and


                                           - 51 -
convicted."   Gamache, 156 F.3d at 12.    The district court ignored

our precedents when it decided a trial record containing strikingly

similar core facts did not warrant an entrapment instruction

because the defendant did not meet his burden of production on the

predisposition prong of the defense.

          Tellingly, the government's brief on appeal does not

even mention Hinkel or Gamache, much less attempt to distinguish

those cases from the circumstances present here.    The government's

primary argument is that Pérez cannot meet his burden on lack of

predisposition because he "jumped at the opportunity to 'play'

with the 11-year-old boyfriend."         That position is obviously

foreclosed by our case law, and, if it influenced the district

court's decision to deny the entrapment instruction, it should not

have.

          The dissent claims that comparing this case to Hinkel

and Gamache is like "saying apples and oranges are 'clearly and

obviously' the same because they both grow on trees in orchards."

To be sure, there are distinctions among the three cases, but all

three involve a mix of evidence -- some favorable to the entrapment

defense, some tending to disprove entrapment.     Each case involved

statements reflecting eagerness and others reflecting reluctance.

Although those statements appeared in conversations which played

out across different time frames featuring different modes of

communication, and the specific facts of the cases do not perfectly


                                - 52 -
align, there is the significant overlap in the categories of facts

that we have described.   The district court's failure to see that

overlap between this case on the one hand, and Hinkel and Gamache

on the other -- cases in which we stated the predisposition issue

needed to go to the jury -- was a clear error.    Although there are

many varieties of apples, they are apples all the same.

C.   Substantial Rights

          Next, we ask whether the clear or obvious error affected

the defendant's substantial rights.       By refusing to give an

entrapment instruction, the court denied Pérez an opportunity to

have the jury consider his primary defense.     See United States v.

Benavidez, 558 F.2d 308, 309 (5th Cir. 1977).    As we have discussed

at length, Pérez's entrapment defense, reviewed in the light most

favorable to him, as required by law, was plausible.     There was a

reasonable probability that a rational jury could credit the

defense, even in the face of the government's attempt to disprove

the entrapment defense beyond a reasonable doubt.         See United

States v. Benjamin, 252 F.3d 1, 9 (1st Cir. 2001) (stating that to

determine whether an error affected the defendant's substantial

rights, the court "must determine 'whether the record contains

evidence that could rationally lead to a contrary finding with

respect to the omitted [jury instruction]'" (quoting Neder v.

United States, 527 U.S. 1, 19 (1999))).   Thus, Pérez's substantial

rights were affected.


                                - 53 -
D.   Fundamental Fairness

            Finally,   we    ask   whether     this   error   is   one   that

"impugn[ed] the fairness, integrity, or public reputation of the

criminal proceeding as a whole."         United States v. Padilla, 415

F.3d 211, 221 (1st Cir. 2005). Our analysis under this final prong

of plain error review is "flexible . . . and depends significantly

on the nature of the error, its context, and the facts of the

case."     United States v. Gandia-Maysonet, 227 F.3d 1, 6 (1st Cir.

2000).

            Entrapment is a judicially created defense reflecting a

recognition that "[m]anifestly, [the law enforcement] function

does not include the manufacturing of crime."            Sherman, 356 U.S.

at 369 (citing Sorrells v. United States, 287 U.S. 435, 443

(1932)).      Given the importance of the defense,            erroneous or

confusing jury instructions regarding entrapment compromise the

fairness of a trial.        E.g., United States v. Kopstein, 759 F.3d

168, 182 (2d Cir. 2014) (holding that misleading jury instructions

regarding    entrapment,    the    defendant's   "only   viable    defense,"

created so much confusion as to "call into question the fairness

and integrity of [the defendant's] conviction" (quoting United

States v. Rossomando, 144 F.3d 197, 201 (2d Cir. 1998))); United

States v. Burt, 143 F.3d 1215, 1219 (9th Cir. 1998); United States

v. Duran, 133 F.3d 1324, 1335 (10th Cir. 1998); Here, we did not

have an instruction that was problematic because it was confusing.


                                      - 54 -
Rather, we had a complete failure to instruct the jury on the

defendant's primary defense.       See Benavidez, 558 F.2d at 310.

Because   of   the   court's   refusal   to   give    Pérez's   requested

instruction, "the jury was not in a position to fairly evaluate

the defendant's case," see id., as it did not know that the

government was required to prove beyond a reasonable doubt that

either no improper inducement took place, or that Pérez was

predisposed to commit the offense.       It is fundamentally unfair to

allow a jury to convict without instructing it on the law relevant

to a plausible entrapment theory that was "fairly raised" at trial.

Id.

          This is not the common plain error case where the failure

of a defendant to properly preserve an objection for de novo review

means that the trial court never had an opportunity to rule on the

matter at issue.     Pérez requested an entrapment instruction before

trial and renewed his request at a charging conference shortly

before the jury instructions were delivered.         Although these steps

did not preserve Pérez's challenge under our circuit's law --

because he did not renew his objection after the court charged the

jury -- the fact remains that the court was fully advised that

Pérez sought the instruction, and objected to its denial, because

he intended to rely, and did in fact rely, on entrapment as a




                                   - 55 -
defense.13 Yet, the court denied the request in a single conclusory

sentence, providing no explanation for its determination that

Pérez had not met his burden of production on the predisposition

prong of the defense.14

             Pérez is now serving a sentence of 151 months' (twelve

and a half years') imprisonment based on the outcome of a trial at

which the court summarily and improperly excluded his primary

defense.     Under these circumstances, the trial court's clear or

obvious error in refusing to present Pérez's entrapment defense to

the   jury   affected   his   substantial   rights   and   undermined   the

fundamental fairness of his trial.       To correct that error, we must

remand for a new trial.

                                    V.

             Given that we are remanding for a new trial, we choose

to comment on one aspect of any new trial: the voir dire process.




       As noted above, Pérez also failed to object on the record
      13

when the judge invited objections immediately before instructing
the jury.   Despite this omission, the trial record makes clear
that the district court was aware of Pérez's objection.

       To the extent that it might be relevant to the fourth prong
      14

analysis, we note that the retrial in this case will not require
a victim to endure a second trial. Obviously, there was no actual
victim of child sexual abuse in this attempt case.      Cf. United
States v. Colon-Nales, 464 F.3d 21, 29 (1st Cir. 2006) ("Given the
unchallenged nature of the evidence in this case . . . the greater
threat to the 'fairness, integrity and public reputation of
judicial proceedings' would be to send this back for trial . . .
thereby requiring the carjacking and rape victim to testify
twice.")


                                     - 56 -
See, e.g., United States v. Gonzalez-Maldonado, 115 F.3d 9, 13

(1st Cir. 1997) ("In order to give as much guidance as possible to

the district court, we also discuss some of the other claims that

are likely to resurface if there is a new trial.").     Pérez insists

that there was error in the district court's handling of the voir

dire.   We do not go that far.     But the briefing has convinced us

that the court would be well-advised to explore the issue of anti-

gay bias more thoroughly than it did in the voir dire process

reflected in the record.

           The court devoted only one question to the topic of anti-

gay bias, asking the panel: "Do you feel that you would not be

able to render a fair and impartial verdict based on the evidence

and my instructions if the defendant were homosexual or gay?"       On

remand, the court should carefully consider Pérez's argument that

this single self-assessment question "was inadequate to permit

discovery of stereotypical and pejorative notions rooted in an

extremely relevant bias."        As Pérez notes, this case raises

particular concerns about anti-gay bias not only because the

defendant is gay, but because of the graphic sexual nature of the

evidence   and   the   repugnant     but    unfortunately   widespread

prejudicial belief that gay men are likely to sexually abuse




                                   - 57 -
children.15     Questions probing prospective jurors' actual bias

against gay men -- rather than their self-assessment of their

ability to be impartial at a criminal trial where the defendant is

gay -- would be more useful in identifying jurors who could not be

fair and impartial in dealing with the difficult facts of this

case.

             Vacated and remanded.

                    - Concurring Opinion Follows -




       See Perry v. Schwarzenegger, 704 F. Supp. 2d 921, 983 (N.D.
        15

Cal. 2010) ("[S]tereotypes imagine gay men and lesbians as . . .
child molesters who recruit young children into homosexuality. No
evidence supports these stereotypes."), aff'd sub nom. Perry v.
Brown, 671 F.3d 1052 (9th Cir. 2012); Luke A. Boso, Dignity,
Inequality, and Stereotypes, 92 Wash. L. Rev. 1119, 1142-43 (2017)
(discussing manifestations of the false stereotype that gay men
are likely to be pedophiles).


                                     - 58 -
            LIPEZ, Circuit Judge, concurring.      I write separately to

urge our court in a future en banc proceeding to abandon the rigid

and outdated interpretation of Rule 30(d) of the Federal Rules of

Criminal Procedure that we had to apply in this case.          We are the

only circuit that -- without regard for the specificity or timing

of a party's initial objection to jury instructions -- deems that

objection forfeited if it is not repeated after the court instructs

the jury.    See United States v. Roberson, 459 F.3d 39, 45 (1st

Cir. 2006). That preservation requirement serves no useful purpose

in   the   administration    of   justice,   and   it   is   premised   on

practicalities that no longer exist.

            To be clear, I do not raise this issue because of any

reservations about the strength of the majority's plain error

analysis in this case.      Rather, I am concerned about the impact of

our existing rule on criminal defendants who cannot meet that

exacting standard in other instances where it is inappropriately

applied.    Pérez's case provides a helpful illustration of why the

rule requiring a pointless post-charge objection is misguided.

            Before his trial commenced, Pérez filed an ex parte

request for an entrapment jury instruction.             At the close of

evidence in the two-day trial, the parties participated in an

unrecorded charging conference.        Even without a record of the

conference, it is clear from the district court's docket entry

that Pérez renewed his request for an entrapment jury instruction.


                                    - 59 -
The district court denied the instruction, stating: "The ruling is

based on the arguments presented by the government and defendant's

response    during   the   charging    conference   in    connection     with

predisposition."16    Following the conference, the attorneys gave

their closing arguments and the court then proceeded to charge the

jury. It did not invite objections from the parties, and Pérez did

not raise an objection.

            Under our court's interpretation of Rule 30(d), Pérez

forfeited   his   claim    that   he   was   entitled    to   an   entrapment

instruction, subjecting that claim to plain-error review.                 See

Fed. R. Crim. P. 52(b).     In other words, our law faulted Pérez for

failing to reiterate an objection that had just been rejected at

the charging conference.      See United States v. Meadows, 571 F.3d

131, 146 (1st Cir. 2009) ("Objections registered during pre-charge

hearings    are   insufficient    to   preserve   the    issue."     (quoting

Roberson, 459 F.3d at 45)).

              Rule 30(d) does not require that interpretation.             It

states: "A party who objects to any portion of the instructions or

to a failure to give a requested instruction must inform the court


     16 Before instructing the jury, the court asked the parties
if there were objections to the instructions. Pérez did not object
at that time, but that lack of objection would not matter because
our precedent requires the objection to be made after the jury is
instructed.   See Roberson, 459 F.3d at 45.     Even if Pérez had
objected when invited to do so by the judge, his claim would still
be considered forfeited and subject to plain error review on
appeal. Id.


                                       - 60 -
of the specific objection and the grounds for objection before the

jury retires to deliberate." By its terms, then, the rule requires

only   that    the   party's   objection   be   specific,   explained,   and

presented before the jury deliberates.             Pérez satisfied each of

those requirements.

              Our rule insisting on a post-charge objection under Rule

30(d) has its origins in a decades-old, out-of-circuit precedent

-- authored by one of our First Circuit colleagues sitting by

designation -- that involved the similar requirement in civil cases

to timely raise instructional challenges.           See Fed. R. Civ. P. 51.

In that 1966 case, Judge Aldrich observed that "[t]he duty imposed

upon counsel of 'stating distinctly the matter to which he objects

and the grounds of his objection' cannot normally be performed

until the charge has been heard in its entirety."              Dunn v. St.

Louis-San Francisco Ry. Co., 370 F.2d 681, 684 (10th Cir. 1966)

(Aldrich,      J.    sitting   by   designation)    (quoting   then-current

language of Fed. R. Civ. P. 51).        Based on that view -- i.e., that

specificity will likely be infeasible before counsel hears the

instructions as given -- the panel in Dunn concluded that an

instructional objection ordinarily will be deemed preserved only

if it is voiced after the court charges the jury. See id.                 We

subsequently adopted that post-charge preservation rule in our

circuit, including for criminal cases governed by Rule 30(d).            See

United States v. Leach, 427 F.2d 1107, 1113 (1st Cir. 1970) (citing


                                       - 61 -
Dunn     as   precedent   for     concluding    that   a   claim       for   a   jury

instruction was forfeited where counsel requested the instruction

but did not renew his objection after the instructions were

delivered).       While Dunn allowed for limited exceptions to the

requirement that objections be made after the jury charge, see 370

F.2d at 684, the First Circuit requires a post-charge objection in

all criminal cases.17       See United States v. Coady, 809 F.2d 119,

123 (1st Cir. 1987) (rejecting an argument that a claim regarding

jury     instructions     could    be   preserved      through     a    pre-charge

objection, stating, "[t]hat counsel may have discoursed upon the

nature of his theory at some time prior to the giving of the charge

will not excuse noncompliance with the express mandates of Rule

30").

              The Dunn rationale for requiring a post-charge objection

in most cases may have been apt when it was articulated more than

a half-century ago.       The judges of that era did not routinely give

lawyers       advance   copies    of    their   proposed    instructions         for

discussion and debate at charging conferences. Indeed, even during




        In a civil proceeding, the trial court has been required
        17

since 2003 to "inform the parties of its proposed instructions and
proposed action on the requests [for instructions] before
instructing the jury and before final jury arguments," Fed. R.
Civ. P. 51(b)(1) (emphasis added), and it "must give the parties
an opportunity to object on the record and out of the jury's
hearing before the instructions and arguments are delivered," id.
at (b)(2). The rule states that an objection is timely if made
"at the opportunity provided under Rule 51(b)(2)."


                                         - 62 -
my tenure as a Maine state trial judge two decades later -- in the

late    1980s     and    early    1990s    --    most   judges     did     not    preview

instructions with counsel in their entirety before delivering

them.    Hence, the general practice supported the assumption that

parties ordinarily could not object with the specificity required

by   Rules   51    and    30(d)    until    they    heard    the    instructions         as

delivered.

             That is simply not the current reality. Today, attorneys

are well-positioned to make specific objections to assist the judge

in correcting errors before he or she charges the jury.                                  The

court's ability to distribute proposed instructions in advance and

to easily revise them on the computer means that the attorney's

obligation to object with specificity can now be -- and ordinarily

is -- performed before "the charge has been heard in its entirety."

Dunn, 370 F.2d at 684.           My experience as an appellate judge reading

trial records tells me that, as a result of this current practice,

surprises    in    the    instructions      as     given    are    rare.         Thus,   by

maintaining our rule, we impose the harsh consequence of plain-

error review without justification.

             We are an outlier in requiring a post-charge objection

in criminal cases under all circumstances.                    Every other circuit

that has considered the sufficiency of a pre-charge objection

employs a more flexible approach, in which a pre-charge objection

is evaluated for its adequacy in meeting Rule 30(d)'s requirements


                                           - 63 -
to provide the trial court with specific notice of an asserted

instructional error.     See United States v. Grote, 961 F.3d 105,

115 (2d Cir. 2020) (an objection prior to jury charge is not

forfeited if "taking further exception under the circumstances

would have been futile" (quoting United States v. Rosemond, 841

F.3d 95, 107 (2d Cir. 2016));     United States v. Russell, 134 F.3d

171, 178 (3d Cir. 1998) ("[T]he crux of Rule 30 is that the district

court be given notice of potential errors in the jury instructions,

not that a party be 'required to adhere to any formalities of

language and style to preserve his objection on the record.'"

(quoting United States v. O'Neill, 116 F.3d 245, 247 (7th Cir.

1997)); United States v. Hollinger, 553 F.2d 535, 543 (7th Cir.

1977) ("[S]pecific and distinct objections voiced in an earlier

instructions conference held in the presence of a court reporter

will be considered timely under [Rule 30(d)] . . . . [W]e shall

henceforth   allow     counsel   to     incorporate   [objections]   by

reference."); United States v. Kessi, 868 F.2d 1097, 1102 (9th

Cir. 1989) (parties need not object following the instructions if

doing so would be a "pointless formality"); United States v.

Kottwitz, 614 F.3d 1241, 1270 (11th Cir. 2010) (objection is

preserved so long as it is "sufficient to give the district court

the chance to correct errors before the case goes to the jury"),

opinion withdrawn in part on denial of reh'g on other grounds, 627

F.3d 1383 (11th Cir. 2010); see also United States v. McDonnell,


                                      - 64 -
792 F.3d 478, 504 & n.15 (4th Cir. 2015) (noting that the appellant

objected at a pre-charge conference and should have repeated his

objection     after   the   instructions   were   delivered,    but   still

applying harmless error review, rather than plain error), vacated

on other grounds, 136 S. Ct. 2355 (2016);18 United States v.

Bornfield, 184 F.3d 1144, 1146 (10th Cir. 1999) (stating that a

party is "obligated to object on the record before the jury retired

to preserve his objection for appellate review" and acknowledging

that    the   objection     might   properly   occur   at   a   pre-charge

conference).

                  That flexible approach not only fulfills the notice

purpose of Rule 30(d), but it also aligns with our forfeiture

doctrine more broadly.       Issues not raised in the trial court are

deemed forfeited, and subject to plain error review on appeal, to

prevent a party from wasting judicial resources and undermining

finality by "sandbagging" the court. See Puckett v. United States,

556 U.S. 129, 134 (2009) ("[T]he contemporaneous-objection rule



        Indeed, on further review, the Supreme Court also applied
       18

a harmless error analysis and vacated the conviction on the ground
that an error in the jury instructions was not harmless.       See
McDonnell, 136 S. Ct. at 2375. The Supreme Court did not comment
on the timing requirements of Rule 30(d) or explicitly affirm a
flexible application of the rule.      Although McDonnell is not
binding intervening precedent that would require us to abandon our
current rule, see United States v. Walker-Couvertier, 860 F.3d 1,
8 (1st Cir. 2017), it does give tacit approval to review for
harmless error rather than plain error when an appellant objected
at a pre-charge conference but not after the instructions were
delivered.


                                      - 65 -
prevents a litigant from 'sandbagging' the court -- remaining

silent about his objection and belatedly raising the error only if

the case does not conclude in his favor."); United States v.

Correa-Osorio, 784 F.3d 11, 22 (1st Cir. 2015) (stating that the

plain   error   rule   "(hopefully)   deters   unsavory   sandbagging   by

lawyers (i.e., their keeping mum about an error, pocketing it for

later just in case the jury does not acquit) and gives judges the

chance to fix things without the need for appeals and new trials").

Our obsolete interpretation of Rule 30(d) does nothing to prevent

"sandbagging." Where, as in this case, a defendant files a written

request for an instruction, and argues for that request at a

charging conference, he is not "sandbagging" when he raises that

same issue on appeal.        He has clearly brought the issue to the

trial court's attention and given the court an opportunity to

correct the instructions.

           Indeed, from a practical standpoint, an objection made

during a charging conference, before the instructions have been

delivered, should be preferred to a post-charge objection.              The

earlier notice provides more timely opportunity for the court to

correct   any    errors.      See   Hollinger,   553   F.2d   at   542-43

("Ordinarily, trial judges will derive considerable benefit from

a serious exchange of views by opposing counsel regarding the

proper formulation of the applicable rules of law before they must

charge the jury.").        In addition, when a request regarding jury


                                      - 66 -
instructions has been discussed in detail at a charging conference,

and the court has ruled, there is no advantage to anyone for

lawyers to persist with the same objection.                To the contrary, such

persistence can be awkward for counsel and off-putting for the

court.    See United States v. Toribio-Lugo, 376 F.3d 33, 41 (1st

Cir. 2004) ("To do her job, a lawyer must be forceful, but she

also must handle her relationship with the presiding judge with

care."); United States v. Kelinson, 205 F.2d 600, 601-02 (2d Cir.

1953)    ("[Rule   30(d)]   does   not    require      a   lawyer     to    become   a

chattering magpie.").

            Importantly, I am not suggesting that a party's failure

to lodge an objection after the court has delivered the jury charge

should    never    result   in   forfeiture       of   the    claim    on    appeal.

Inevitably, some pre-charge objections will be insufficiently

specific,    or    inadequately    explained,      and      will    therefore    not

fulfill the notice objective of Rule 30(d).                  But Rule 30(d) does

not require us to demand pointless repetition of objections that

were distinctly raised and decisively denied.

            In short, our court's outdated, inflexible approach to

Rule 30(d) neither advances the purpose of the rule nor serves the

interests of justice and, hence, it poses an unjustifiable barrier

to plenary appellate review of fully preserved objections.                           We

should replace our outmoded instructional-error doctrine with the

flexible approach that -- for good reason -- is now the prevailing


                                         - 67 -
view.   In    other     words,   like   our   sister    circuits,      we   should

recognize    that   a    pre-charge     objection      may    preserve      a   jury

instruction   issue     for   appellate   review    if       the   objection    was

sufficiently specific to give the trial court notice of the claimed

error and repetition of the objection post-charge would be a futile

exercise.

                      - Concurring Opinion Follows -




                                        - 68 -
           BARRON, Circuit Judge, concurring.   I share the concern

that Judge Lipez expresses about the way that our precedent

currently requires us to construe Rule 30(d) of the Federal Rules

of Criminal Procedure.     The text of the rule, his concurrence

points out, does not compel the rigid procedure for preserving

objections to jury instructions that our case law requires.   There

may often be benefits to voicing objections to instructions after

the charge to the jury has been given.    But, they are not manifest

in every case.    Indeed, the case at hand exemplifies the point.

The sole ground that the District Court gave at the charging

conference for denying the requested instruction here was that the

evidence developed at trial had failed to provide a factual basis

for giving it.   Nothing about the charge itself could have called

that ruling into question.   Yet, our precedent still requires that

we treat this defendant's failure to seek reconsideration of that

ruling as if it were a failure to have requested the instruction

at all.   See United States v. Baltas, 236 F.3d 27 (1st Cir. 2001).

                  - Dissenting Opinion Follows -




                                 - 69 -
             KAYATTA, Circuit Judge, dissenting.

             The   majority's     analysis    hinges        crucially    on   the

assertion that, as to the matter of predisposition, this case is

so   like    Hinkel   and   Gamache   that   the    need    for   an   entrapment

instruction was "clear or obvious."             Respectfully, I cannot see

how this is so in this case.

             Here is what Hinkel said when he first learned that a

15-year-old was involved:        "Sounds very naughty.            I am concerned

about her age since legally she should be 16 or older."                   It then

took a month before the continued enticement ripened into a planned

meeting. Here, by contrast, is what Pérez said upon first learning

that an eleven-year-old was involved:              "Mmmm yes."      Within three

days Pérez was messaging, "I want your boyfriend."                     And within

five days from the first message, the meet was on.

             There is more.     Hinkel offered affirmative evidence that

he had never sought a relationship with someone not of legal age.

Pérez offered no such evidence. Rather, when the agent asked Pérez

at the outset of their communications "what age do you like?,"

Pérez replied, "The younger the better.             I don't discriminate.       I

started at 8.      Hehehe.    So you tell me."        And when asked "do you

like really young guys?," he replied:               "Yes.     Age?      I started

at 8."      So while Hinkel was saying he never even looked for sex

with a minor, Pérez was highlighting a nondiscriminatory track




                                       - 70 -
record.    And he was clearly saying in context that eight years old

was not too young.

            Gamache is even further removed.               The defendant in

Gamache    initially    expressed       interest     solely    in    an     adult

relationship.     Only after "the Government's insistence and artful

manipulation" over the course of eight months did he become ready

to meet the supposed victims, and even then he was saying "this

will be a new experience for me."            United States v. Gamache, 156

F.3d 1, 6, 10 (1st Cir. 1998).         Pérez, conversely, expressed eager

interest immediately.     And unlike Hinkel and Gamache, he offered

no evidence suggesting a lack of predisposition.

            The   majority's        effort   to    avoid   the      stark      pre-

dispositional     admission    by    Pérez   at   the   very   outset     of   his

exchanges with the agent warrants particular scrutiny.                  Ignoring

Pérez's express assurance that he likes them the "younger the

better," all the majority can do is claim that there is some

ambiguity about what the agent meant when he subsequently referred

to his own age.     And the majority's claim that it is not obvious

what Pérez was saying is twice-flawed:            It certainly seems obvious

he was indeed saying he likes them "the younger the better;" and,

in any event, I do not see how it was possibly plain error for the

trial court to have read Pérez's statement exactly as I do, i.e.,

as a frank, un-coaxed profession of the precise predisposition at

issue.    And since there is zero contrary evidence, I simply cannot


                                        - 71 -
see how it was also plain error to conclude that Pérez failed to

generate a sufficient claim of entrapment to get to a jury.                     See

Gamache, 156 F.3d at 9 ("The defendant carries the initial burden

of producing some evidence of both the Government's improper

inducement, and the defendant's lack of predisposition to commit

the alleged offense, so as to 'raise a reasonable doubt as to

whether he was an unwavering innocent rather than an unwavering

criminal.'" (quoting United States v. Joost, 92 F.3d 7, 12 (1st

Cir. 1996)) (second emphasis added)); see also id. ("[T]he court's

function is to examine the evidence on the record and to draw those

inferences    as    can   reasonably    be    drawn   therefrom,       determining

whether the proof, taken in the light most favorable to the defense

can plausibly support the theory of the defense." (first emphasis

added)).

             The bottom line is that the majority significantly errs

in   comparing     Hinkel    and   Gamache    to   this    case   by   noting   the

similarities     while      ignoring   or    downplaying    the   very   material

differences.       The resulting reasoning is like saying apples and

oranges are clearly and obviously the same because they both grow




                                        - 72 -
on trees in orchards.    I would rule that it was not clear or

obvious that an entrapment instruction was required in this case.19




     19  I do agree, however, with my colleague's concurrences that
we should revisit our rule on preserving objections to jury
instructions. As ably explained, our rule is not derived from the
text of Rule 30(d), no longer fits practice, and is apt to produce
unfair results. I also agree with Part V of the majority opinion.


                                - 73 -

```

---

## GROUP: _overhaul2/lake/cases/United States v. Perez.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Perez
type: case
citation: "89 F.4th 247 (2023)"
parallel_cite: ""
neutral_cite: ""
court: 1st Cir.
court_level: coa
circuit: ca1
year: 2023
date_decided: 2023-12-28
docket: 22-1121
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
  opinion_url: "https://www.courtlistener.com/opinion/9456060/united-states-v-perez/"
  cluster_id: 9456060
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Perez
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[SIA Vehicles]]"
    role: "Lower-court development (role-based)"
related:
  - "[[SIA Vehicles]]"
  - "[[Arizona v. Gant]]"
  - "[[Riley v. California]]"
  - "[[Chimel v. California]]"
tags:
  - case
  - fourth-amendment
  - search-incident-to-arrest
  - grabbing-area
  - container-search
  - backpack
  - first-circuit
holding: "The search-incident-to-arrest exception permits a warrantless search of an arrestee's nearby container, and the First Circuit's decision in United States v. Eatherton — upholding such a search of a bag within an arrestee's reach — retains controlling force notwithstanding the Supreme Court's intervening decisions in Gant and Riley, so the warrantless search of Perez's backpack incident to his arrest did not violate the Fourth Amendment and his conviction was affirmed."
aliases:
  - United States v. Perez
  - "United States v. Perez (1st Cir. 2023)"
---

# United States v. Perez

*89 F.4th 247 (1st Cir. 2023)* (No. 22-1121) · U.S. Court of Appeals for the First Circuit · **Binding in-circuit — 1st Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 9456060 → lead opinion 9913885 (Barron, C.J.; 89 F.4th 247, decided 2023-12-28); Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — CL text is slip-paginated). S9 promotes. -->

## Background
Gilbert Perez was convicted of a federal drug offense in the District of Maine after the district court denied his motion to suppress the fruits of a warrantless search of his backpack, which officers searched incident to his arrest. The district court rested its ruling on *United States v. Eatherton*, a First Circuit decision upholding a similar warrantless search of a bag within an arrestee's reach under the search-incident-to-arrest exception. On appeal, Perez argued that intervening Supreme Court decisions — *[[Arizona v. Gant]]* and *[[Riley v. California]]* — had stripped *Eatherton* of its controlling force.

## Issue
Whether the First Circuit's search-incident-to-arrest rule permitting the warrantless search of an arrestee's nearby bag, as applied in *Eatherton*, survives the Supreme Court's decisions in *[[Arizona v. Gant|Gant]]* and *[[Riley v. California|Riley]]*.

## Rule
The search-incident-to-arrest exception allows officers, without a warrant, to search the arrestee's person and the area within his immediate control, including containers such as a bag found there; *Eatherton* applied that rule to an arrestee's nearby bag, and the panel held it remains good law after *[[Arizona v. Gant|Gant]]* and *[[Riley v. California|Riley]]*: "Because we conclude that *Eatherton* controls here, we need not evaluate the search of Perez's backpack under *Maldonaldo-Espinosa*." — 89 F.4th 247, slip op. at 17. ^pin-op17

## Application
Perez's core contention was that *[[Arizona v. Gant|Gant]]* (which cabined vehicle [[Search Incident to Arrest|searches incident to arrest]] to circumstances where the arrestee can access the passenger compartment or the vehicle may contain evidence of the offense) and *[[Riley v. California|Riley]]* (which required a warrant to search a cell phone seized incident to arrest) had eroded *Eatherton*'s allowance for a warrantless search of an arrestee's bag. The court disagreed: *[[Arizona v. Gant|Gant]]* addressed the distinct automobile context, and *[[Riley v. California|Riley]]* turned on the unique privacy interests in the vast digital contents of a modern cell phone, not on physical containers generally. Neither displaced *Eatherton*'s rule for a bag within an arrestee's grabbing area. Because *Eatherton* controlled, the panel did not need to reach the government's alternative ground, and the warrantless backpack search was lawful.

## Conclusion
**Affirmed.** Chief Judge Barron wrote for the panel (Barron, C.J., Howard, and Montecalvo, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Perez* is a useful post-*[[Riley v. California|Riley]]* boundary marker for **[[Search Incident to Arrest|search incident to arrest]]**: it confirms that the *[[Chimel v. California|Chimel]]* grabbing-area rule still authorizes the warrantless search of an arrestee's nearby **physical container**, and that *[[Arizona v. Gant|Gant]]* (vehicles) and *[[Riley v. California|Riley]]* (cell phones) did not silently overrule that allowance. Teach it to keep students from over-reading *[[Riley v. California|Riley]]* into a general container rule.

## Appears on
- [[SIA Vehicles]] — *Lower-court development (role-based)*

## Sources
- [*United States v. Perez*, 89 F.4th 247 (1st Cir. 2023)](https://www.courtlistener.com/opinion/9456060/united-states-v-perez/) — pinpoint: slip op. at 17 (*Eatherton*'s search-incident-to-arrest rule for an arrestee's bag survives *Gant* and *Riley*; the CL opinion text carries slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "29337d6ee4b04327", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Perez"}, "payload": {"all": [{"cite": "89 F.4th 247", "page": "247", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "89"}], "display": "89 F.4th 247", "official": {"cite": "89 F.4th 247", "page": "247", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "89"}, "official_selection_present": true, "record_id": "United States v. Perez"}}
{"assertion_id": "b536a6299b87318a", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Perez"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Perez", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Perez

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Perez",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Perez",
    "case_name_short": "Perez",
    "case_name_full": "",
    "input_case_name": "United States v. Perez",
    "court": "1st Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca1",
    "state": null,
    "date_decided": "2023-12-28",
    "year": 2023,
    "docket": "22-1121",
    "cluster_id": 9456060,
    "lead_opinion_id": 9913885,
    "sibling_ids": [],
    "absolute_url": "/opinion/9456060/united-states-v-perez/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "89 F.4th 247",
      "volume": "89",
      "reporter": "F.4th",
      "page": "247",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "89 F.4th 247",
        "volume": "89",
        "reporter": "F.4th",
        "page": "247",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "89 F.4th 247",
    "official_selection": {
      "court_class": "coa",
      "selected": "89 F.4th 247",
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
    "date_created": "2026-07-07T01:40:20Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:40:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:40:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:40:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:40:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-perez--9456060",
      "to_record_id": "United States v. Perez",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Perez

```
          United States Court of Appeals
                      For the First Circuit

No. 22-1121

                          UNITED STATES,

                            Appellee,

                                v.

                          GILBERT PEREZ,

                      Defendant, Appellant.


          APPEAL FROM THE UNITED STATES DISTRICT COURT
                    FOR THE DISTRICT OF MAINE

          [Hon. D. Brock Hornby, U.S. District Judge]


                              Before

                       Barron, Chief Judge,
              Howard and Montecalvo, Circuit Judges.


     Jamesa J. Drake, with whom Drake Law LLC was on brief, for
appellant.
     Brian S. Kleinbord, Assistant United States Attorney, with
whom Darcie N. McElwee, United States Attorney, was on brief, for
appellee.



                        December 28, 2023
          BARRON, Chief Judge.      Gilbert Perez seeks to vacate his

federal drug conviction on the ground that the United States

District Court for the District of Maine wrongly denied his motion

to suppress the fruits of a warrantless search of his backpack.

The District Court rested the denial on our decision in United

States v. Eatherton, 519 F.2d 603 (1st Cir. 1975), which upheld a

similar warrantless search under the search-incident-to-arrest

exception to the warrant requirement of the Fourth Amendment to

the U.S. Constitution, id. at 609-11.        Because we reject Perez's

contention that intervening decisions of the Supreme Court of the

United States have stripped Eatherton of controlling force, we

affirm the judgment of conviction.

                                    I.

          When   reviewing   the    denial   of   a   motion   to   suppress

evidence, "'we recite the facts as found by the district court,

consistent with record support,' including the testimony from the

motion hearing."   United States v. Tom, 988 F.3d 95, 97 (1st Cir.

2021) (quoting United States v. Soares, 521 F.3d 117, 118 (1st

Cir. 2008) (cleaned up)). Massachusetts State Trooper Jason Conant

was conducting a patrol on the evening of August 30, 2019, when he

saw a pickup truck with Maine license plates stop in a McDonald's




                                   - 2 -
parking lot in Lawrence, Massachusetts.            The driver was later

identified as Perez.

            Perez exited the truck, donned a backpack, and walked

towards a residential area near the parking lot.             Conant became

suspicious of the out-of-state truck, as well as Perez's behavior,

and alerted other state troopers in the area to watch for Perez.

            Minutes after Perez left the parking lot, a second

Massachusetts state trooper, Shawn McIntyre, saw Perez exiting a

taxi on a nearby street.       McIntyre watched Perez start to walk in

the direction of the McDonald's where the truck was parked.

            McIntyre stopped the taxi and saw large quantities of

cash at the feet of the taxi's passenger.          McIntyre then radioed

Conant, informing him of the cash and the suspicion that Perez had

participated in a drug transaction with the taxi's passenger.

            Perez,    still   wearing   the   backpack,   returned   to   the

McDonald's parking lot.       Conant pulled his (unmarked) car into the

parking lot and exited the car.          Roughly simultaneously, Conant

began to yell "state police," and Perez began to run from the

parking lot.    Conant gave chase.

            About twenty yards from the parking lot, Perez tripped

and fell.   Conant caught up to Perez after his fall and pinned him

to the ground.       A third state trooper, Ryan Dolan, pulled up in a

patrol car.




                                   - 3 -
          Conant removed the backpack from Perez as Dolan was

handcuffing Perez's hands behind his back.         Dolan then sat Perez

on the pavement.

          After Perez was handcuffed, Conant placed the backpack

on Dolan's car and opened and searched the backpack.           Perez was

not in reaching distance of the backpack when the search of the

backpack took place.

          Conant discovered fentanyl and cocaine in the backpack.

Perez was then searched and formally arrested.

          Perez was indicted on March 12, 2020, on a federal

drug-related charge.       He moved to suppress the drugs, contending

that the backpack's search violated the Fourth Amendment.1

          The government opposed the motion on the ground that the

search was constitutional under Eatherton.         The government also

argued that, in any event, the search was conducted in good-faith

reliance on Eatherton.      See Davis v. United States, 564 U.S. 229,

232   (2011)    (holding    that   "[police]   searches    conducted   in

objectively reasonable reliance on binding appellate precedent are

not subject to the exclusionary rule").

          The    District    Court   denied    Perez's    motion   without

reaching the good-faith issue.       See United States v. Perez, Crim.

No. 2:20-CR-39-DBH-01, 2021 WL 2953671 (D. Me. July 14, 2021).


      1Perez challenged several other aspects of his arrest in the
District Court but raises none of those issues on appeal.


                                   - 4 -
The District Court found that "[t]he police had probable cause to

arrest Perez when they handcuffed him," and it "treat[ed] [the

police] as having effectively arrested him then," although the

District Court also found that it was only later that Perez was

"formally" arrested.   Id. at *2.     The District Court separately

found, moreover, that Perez's handcuffing occurred "as" Conan

"ripped the backpack off" of Perez.        Id.   With that factual

predicate in place, the District Court reasoned that the search of

the backpack was lawful because, when there is probable cause for

an arrest, Eatherton allows for the warrantless "search [of] a

container found on a person being arrested," id. at *3, and our

Court had not "'unmistakably' cast Eatherton 'into disrepute,'"

id. at *4 (quoting Eulitt ex rel. Eulitt v. Me., Dep’t of Educ.,

386 F.3d 344, 349 (1st Cir. 2004)).

          Perez entered a conditional guilty plea, which preserved

his right to appeal his conviction based on the District Court's

Eatherton-based denial of his motion to suppress.     He then filed

this timely appeal.    We review the District Court's "factual

findings for 'clear error'" and its "legal conclusions . . . de

novo."   United States v. Rodríguez-Pacheco, 948 F.3d 1, 6 (1st

Cir. 2020) (quoting United States v. Camacho, 661 F.3d 718, 723-

24 (1st Cir. 2011)).




                              - 5 -
                                       II.

             The Fourth Amendment protects "[t]he right of the people

to be secure in their persons, houses, papers, and effects, against

unreasonable       searches      and    seizures"       by    providing      that

"no Warrants shall issue, but upon probable cause."                   U.S. Const.

amend. IV.    Our focus is on the exception to the Fourth Amendment's

warrant requirement for a search incident to an arrest. See United

States v. Robinson, 414 U.S. 218 (1973).

             Perez does not dispute that the exception covers his

backpack's search if Eatherton remains good law.              He contends only

that   Eatherton    does   not    because      of   either   United    States   v.

Chadwick, 433 U.S. 1 (1977), or Arizona v. Gant, 556 U.S. 332

(2009), or both together.

             Under the law of the circuit doctrine, newly constituted

panels must follow the rulings of preceding panels that are

"directly (or even closely) on point," United States v. Guzman,

419 F.3d 27, 31 (1st Cir. 2005), "even where the succeeding panel

disagrees with the prior one," United States v. Guerrero, 19 F.4th

547, 552 (1st. Cir 2021).         The doctrine recognizes an exception,

however, when "[a]n existing panel decision [is] undermined by

controlling authority, subsequently announced, such as an opinion

of the Supreme Court, an en banc opinion of the circuit court, or

a statutory overruling," Williams v. Ashland Eng'g Co., 45 F.3d

588, 592 (1st Cir. 1995), or when an "authority that postdates the


                                       - 6 -
original decision, although not directly controlling, nevertheless

offers a sound reason for believing that the former panel, in light

of fresh developments, would change its collective mind," United

States v. Barbosa, 896 F.3d 60, 74 (1st Cir. 2018) (quoting

Williams, 45 F.3d at 592).

            The latter exception is very limited, as it applies only

when the new authority "provides a clear and convincing basis" to

conclude    that    the   prior   panel    would    have   changed   its   mind.

Guerrero, 19 F.4th at 552.          For that reason, we have described

cases that trigger this exception as "hen's-teeth-rare."               San Juan

Cable LLC v. P.R. Tel. Co., 612 F.3d 25, 33 (1st Cir. 2010).

            We    begin   by   reviewing   Eatherton       and   describing   its

rationale.       We then explain why we conclude that Eatherton still

controls.

                                      A.

            The defendant in Eatherton was Gilbert Eatherton.                 519

F.2d. at 605.        A suspected bank robber, he was walking down a

street while carrying a briefcase when agents of the Federal Bureau

of Investigation ("FBI") spotted him.              Id. at 609.

            The FBI agents called for Eatherton to come to their

car, and he did so.        Id.    When he was "close to the vehicle the

agents told him he was under arrest [and] instructed him to drop

the briefcase and [lie] spread eagle on the ground."                    Id.    He

complied with the commands, and the FBI agents "thoroughly frisked"


                                    - 7 -
him, handcuffed him, and placed him in the back of their vehicle.

Id.    The FBI agents then picked up the briefcase, opened it, and

found a loaded gun and three brown ski masks, all of which were

later admitted as evidence at trial.     Id.

           Eatherton did not dispute that there was probable cause

to arrest him, and he "concede[d] that the agents could have seized

the briefcase consonant with the [F]ourth [A]mendment."      Id. at

610.   But he argued that the agents "should have obtained a search

warrant before investigating [the briefcase's] contents," and

that, because the agents did not, the search of his briefcase

violated the Fourth Amendment.    Id. He thus argued that the fruits

of the search of the briefcase had to be suppressed because that

search could not be justified merely by the fact of his arrest and

the right to search his person that his arrest entailed.    Id.

           Eatherton relied chiefly on the Supreme Court's decision

in Chimel v. California, 395 U.S. 752 (1969).      There, the Court

held that the bare fact that an arrest occurred inside a home did

not justify a warrantless search of the entirety of the premises.

Id. at 763. The Court also held that although a warrantless search

of the area of the home within the "immediate control" of the

arrestee was reasonable if justified "by the need to seize weapons

and other things which might be used to assault an officer or

effect an escape" or "by the need to prevent the destruction of

evidence of the crime," these "justifications are absent where a


                                 - 8 -
search is remote in time or place from the arrest."      Id. at 764

(quoting Preston v. United States, 376 U.S. 364, 367 (1964)).

           Eatherton argued based on Chimel that the briefcase's

search violated the Fourth Amendment because "any urgency to

inspect the interior of the briefcase was completely removed once

he had been subdued and the [brief]case removed from his possession

and beyond his possible reach."    Eatherton, 519 F.2d at 610.   But,

although the Eatherton panel acknowledged that there was "some

logical cogency" to the contention, id., the panel held that the

search of the briefcase's interior was reasonable.

           The Eatherton panel first pointed out that Chimel had

cited "with apparent approval Draper v. United States, in which a

search virtually identical to that at issue [in Eatherton] was

upheld."   Id. (citation omitted).       Draper involved a criminal

defendant who had evidence admitted against him at his trial that

was obtained from the warrantless search of a bag that he was

carrying when he was arrested.    358 U.S. 307, 310 (1959).

           The Eatherton panel next explained that other courts of

appeals "had little apparent difficulty" rejecting Chimel-based

arguments for prohibiting warrantless "searches identical to that

contested" by Eatherton.   519 F.2d at 610.     Notably, in each of

those cases, as in Draper, the warrantlessly-searched container

was similar in size to the briefcase in Eatherton.       See United

States v. Maynard, 439 F.2d 1086, 1087 (9th Cir. 1971) (rejecting


                                 - 9 -
the argument that a warrantless search of a suitcase the defendant

was carrying when arrested was unconstitutional because the search

was "incident to the lawful arrest of its carrier"); United States

v. Mehciz, 437 F.2d 145, 146-48 (9th Cir. 1971) (relying on Draper

to reject the contention that Chimel governed a warrantless search

of a suitcase carried at the time of arrest); United States ex

rel. Muhammad v. Mancusi, 432 F.2d 1046, 1047-48 (2d Cir. 1970)

(rejecting     as   "frivolous"   a   Chimel-based   challenge   to   the

post-arrest search at a police station of a briefcase in the

"immediate possession" of the defendant at the time of the arrest

when the defendant conceded that the search "would have been proper

if [it] had been conducted at the time [and place] of his arrest").

          The Eatherton panel then addressed three Supreme Court

decisions that post-dated both Chimel and the other circuits'

rulings that had upheld searches like the search of Eatherton's

briefcase: Robinson, 414 U.S. at 218; Gustafson v. Florida, 414

U.S. 260 (1973); and United States v. Edwards, 415 U.S. 800 (1974).

The Eatherton panel explained that this trio showed that the

Chimel-based challenge could not "be sustained."         Eatherton, 519

F.2d at 610.

          In Robinson, the Court held that the warrantless search

of a "crumpled up cigarette package" found in the "breast pocket

of the heavy coat [the arrestee] was wearing" at the time of his

arrest did not violate the Fourth Amendment, even though the


                                  - 10 -
arresting   officer    had   neither    "any     subjective   fear   of   the

[arrestee]" or any "susp[icion] that the [arrestee] was armed."

414 U.S. at 222-23, 236.         The Court explained that because the

"custodial arrest of a suspect based on probable cause is a

reasonable intrusion under the Fourth Amendment[,]" a search "of

the person" of an arrestee incident to that arrest is per se

reasonable.    Id. at 235.     Robinson thus rejected the contention

that a more limited pat-down -- such as the limited frisk permitted

in Terry v. Ohio, 392 U.S. 1 (1968) -- was all that was allowed

for a search incident to the arrest.             See Robinson, 414 U.S. at

235.   And the Court then explained that "[h]aving in the course of

a lawful search come upon the crumpled package of cigarettes, [the

officer who had conducted the search of the arrestee's person] was

entitled to inspect [the package,] and when his inspection revealed

the heroin capsules, he was entitled to seize them as 'fruits,

instrumentalities, or contraband' probative of criminal conduct."

Id. at 236 (quoting Harris v. United States, 331 U.S. 145, 154-55

(1947)).

            Robinson    relied     on      the     rationales    for      the

search-incident-to-arrest exception to the warrant requirement to

justify the ruling that the warrantless search of the cigarette

package was reasonable.      Those rationales are rooted in a concern

for officer safety, the governmental interest in the preservation

of evidence, and the diminished privacy interest of an arrestee


                                  - 11 -
due to the dominion over their person effected by the arrest

itself.     See   Robinson,    414    U.S.     at     226;    see     also    Riley   v.

California, 573 U.S. 373, 386 (2014) ("Robinson regarded any

privacy   interests     retained     by   an   individual           after    arrest   as

significantly diminished by the fact of the arrest itself.").

            In Gustafson, which was decided the same day as Robinson,

the Court went a step further than it had in Robinson.                         It held

that a warrantless search of a cigarette box found in the "front

coat pocket of the coat [the arrestee] was wearing" during a search

of the arrestee's person at the time of his arrest, 414 U.S. at

262, was per se reasonable under Robinson even though the search

of the cigarette box occurred after the arrestee had been placed

"in the back seat of the squad car," id. at 262 n.2, and even

though    there   was   no   "subjective       fear    of     the    [arrestee]"      or

"susp[icion] that the [arrestee] was armed," id. at 266.

            The defendant in Eatherton tried to distinguish Robinson

and Gustafson based on the relatively large size of his briefcase

and the fact that it was not concealed in his pocket but held in

his hand at the time of the arrest.                   But the Eatherton panel

concluded that "[t]he line which [Eatherton] attempts to draw

placing the briefcase beyond the search of his 'person' which

Robinson and Gustafson expressly approve is one requiring gossamer

distinctions."     Eatherton, 519 F.2d at 610.               And Eatherton went on

to state that "[t]here is no indication that the result in those


                                     - 12 -
cases would have been any different had the cigarette packages

been in the defendants' hands rather than in their pockets or if

they had been dropped to the ground in response to [a] police

command." Id. Moreover, Eatherton explained, "[w]hile a briefcase

may be a different order of container than a cigarette box, it is

not easy to rest a principled articulation of the reach of the

[F]ourth [A]mendment upon the distinction."               Id.

           The Eatherton panel also noted that the defendant's

argument was "not unlike" Justice Marshall's in "his dissent to

Gustafson and Robinson."        Id.     The Eatherton panel then cited to

the portion of that dissent that relied on Chimel to dispute the

majority's     decision   to   uphold    the   warrantless       search   of   the

container in that case.        Id. (citing Robinson, 414 U.S. at 256-58

(Marshall, J., dissenting)).          While the argument advanced in that

portion   of    Justice   Marshall's      dissent    "may       have   analytical

appeal," the Eatherton panel concluded, the view set forth there

"does not presently represent the law."             Id.

           The Eatherton panel wound up its analysis by invoking

Edwards, which was decided the year after Robinson and Gustafson.

The Court held in Edwards that the Fourth Amendment permitted the

warrantless search of clothing that an arrestee was wearing at the

time of his arrest even though the search of the clothing occurred

the day after the arrest and while the arrestee was in jail.

Edwards, 415 U.S. at 808-09.            Edwards reasoned that "the legal


                                      - 13 -
arrest of a person" reduces the arrestee's expectation of privacy

in items "in his immediate possession, including his clothing."

Id. at 805, 808 (emphasis added) (quoting United States v. DeLeo,

422 F.2d 487, 493 (1st Cir. 1970)).

             The Eatherton panel observed that the Court in Edwards,

"after noting that the courts of appeals have generally permitted

searches of both 'the person and the property in his immediate

possession,'" stated that "it is difficult to perceive what is

unreasonable about the police examining and holding as evidence

those personal effects of the accused that they already have in

their lawful custody as the result of a lawful arrest." Eatherton,

519 F.2d at 610 (first quoting Edwards, 415 U.S. at 803; then

quoting Edwards, 415 U.S. at 806).       The search in Edwards had been

made   "in    the     station   house   after   an   arrest,"   Eatherton

acknowledged.       But Eatherton explained that there was no reason to

"doubt that [those observations from Edwards] apply equally to

searches in the field immediately incident to the arrest."            Id.

Eatherton thus held that, as the defendant in the case before it

had "conceded the agents properly seized the briefcase as . . .

incident to his arrest . . . any expectation of privacy which he

held with regard to the briefcase was taken out of 'the realm of

protection from police interest in weapons, means of escape, and

evidence.'"    Id. at 610-11 (quoting Edwards, 415 U.S. at 808-09).




                                   - 14 -
                                        B.

               As this extended review of Eatherton reveals, the panel

in that case did more than determine that the rule set forth in

Robinson, Gustafson, and Edwards rather than the rule set forth in

Chimel controlled the briefcase's search.              The panel also made

clear that it based that determination on the considered judgment

that, for purposes of the rule laid down in Robinson and Gustafson,

a search of a container (at least of the "order" of a briefcase,

see Eatherton, 519 F.2d at 610) in the hands of an arrestee at the

time of the arrest was no different from a search of a container

in the pocket of an arrestee at that time.2            As Eatherton put it,

a "line which [would] plac[e] the briefcase beyond the search of

[the] 'person' which Robinson and Gustafson expressly approve is

one requiring gossamer distinctions."             519 F.2d at 610.    And, to

that       point,   the   Eatherton   panel    explained   that,   although   a

briefcase was of "a different order of container from a cigarette

box," it would not be "easy" to make any such distinction for the




       2We understand Eatherton's statement that "[t]here is no
indication that the result in [Robinson and Gustafson] would have
been any different had the cigarette packages been . . . dropped
to the ground in response to police command," 519 F.2d at 610, to
mean only that the determination of whether an item is "of the
person" of the arrestee or in the arrestee's "area of immediate
control" is unaffected by post-arrest, police-ordered conduct.
After all, at the same time that the FBI agents told Eatherton to
drop the briefcase, they also told him he was under arrest. Id.
at 609.


                                      - 15 -
relevant Fourth Amendment purposes in a "principled" manner.                 Id.

Eatherton then reasoned that, as a result, Edwards required the

conclusion that the briefcase's search was reasonable, given that

Edwards concluded that the search of the personal property found

on the person of the arrestee in that case was reasonable.                   In

that regard, Eatherton concluded based on Edwards that because

"the   agents   properly   seized    the     briefcase   . . .    incident   to

[Eatherton's] arrest. . . . any expectation of privacy which he

held with regard to the briefcase was taken out of 'the realm of

protection from police interest in weapons, means of escape, and

evidence.'"     Id. at 610-11 (quoting Edwards, 415 U.S. at 808-09).

           Perez   does    not   suggest     that   there   is   any   relevant

difference between his backpack and the briefcase in Eatherton or

that the backpack was not on his back when the District Court found

that he was arrested, notwithstanding that the District Court found

that he was "formally" arrested only thereafter.             He thus accepts

that his appeal lacks merit if Eatherton controls.                     His sole

contention, therefore, is that Eatherton does not control due to

post-Eatherton developments.

                                      C.

           The post-Eatherton developments that Perez has in mind

are two Supreme Court precedents: Chadwick and Gant.              He contends

that, whether separately or together, they undermine (even if they

do not overrule) Eatherton's holding that a briefcase in the hands


                                    - 16 -
of an arrestee at the time of arrest is no different from the

cigarette containers involved in Robinson and Gustafson.                   But we

cannot agree -- even if we account for post-Chadwick and post-Gant

out-of-circuit precedent that is at odds with Eatherton.                  Thus, we

conclude that Eatherton remains binding on us as a panel.3

                                           1.

               We start with Perez's arguments about Chadwick, which

was decided two years after               Eatherton.       Perez contends that

Chadwick       is    a    significant       intervening     precedent     because

Eatherton's rationale depended on the determination that there was

"no indication" that the result in either Robinson or Gustafson

"would have been any different had the cigarette packages been in

the defendants' hands rather than in their pockets or if they had

been       dropped   to   the   ground    in    response   to   police   command."

Eatherton, 519 F.2d at 610.              Yet, Perez asserts, Chadwick shows

that is not so.



       Neither Perez nor the government addresses whether, even if
       3

Eatherton does not control the outcome of this case, it is
controlled by our post-Chadwick ruling in United States v.
Maldonaldo-Espinosa, 968 F.2d 101, 104 (1st Cir. 1992) (rejecting
an argument that the search of a bag "on the table next to [the
handcuffed defendant] and within reach" could be justified only by
an exigency because "government agents, when arresting a person,
may constitutionally search an arrested person's nearby . . . bag,
without a warrant . . . whether or not [the agents] have reason to
fear that the carry-on bag contains a weapon, another threat to
their safety, or destructible evidence"). Because we conclude that
Eatherton controls here, we need not evaluate the search of Perez's
backpack under Maldonaldo-Espinosa.


                                         - 17 -
           The Supreme Court held in Chadwick that the warrantless

search of an arrestee's      "double-locked,    200-pound footlocker"

violated the Fourth Amendment when the search of that container

was conducted beyond "the area from within which [the arrestees]

might gain possession of a weapon or destructible evidence,"

Chadwick, 433 U.S. at 5 (quoting Chimel, 395 U.S. at 763), and was

not "justified by any other exigency," id. at 15.         But nothing in

Chadwick   disturbs    either    Robinson's    ruling     upholding    the

warrantless search of a cigarette container in the pocket of an

arrestee at the time of the lawful arrest or Gustafson's ruling

upholding such a search even when it is performed after the

cigarette container has been removed from the arrestee's immediate

area of control.

           In   that   regard,   Chadwick     expressly    states     that,

"[u]nlike searches of the person [under] United States v. Robinson

[and] United States v. Edwards, searches of possessions within an

arrestee's immediate control cannot be justified by any reduced

expectations of privacy caused by the arrest."            433 U.S. at 16

n.10 (emphasis added) (citations omitted).        We do not read that

passage, in expressly reaffirming Robinson and Edwards, to be

silently rejecting the parts of their holdings that blessed the

searches of the personal property in those cases that was found on

the person of the defendants.      Nor do we read that passage, in

reaffirming those two cases without mentioning Gustafson, to be


                                 - 18 -
silently    rejecting      Gustafson's     extension    of   Robinson's    rule

regarding a search of personal property on the person of the

arrestee at the time of the arrest to cover the search of such

property even after that property was no longer in the arrestee's

area of immediate control.

            Moreover, nothing in Chadwick purports to address how to

treat a container that an arrestee has in hand at the time of

arrest relative to a container that an arrestee has in a pocket at

that time.      In fact, Chadwick had no reason to address that

question because the arrestee was not holding the container in

Chadwick.    Nor, for that same reason, did Chadwick have reason to

address whether the arrestee's dropping of such a container in

response to a police command upon arrest would change the calculus.

So, not surprisingly, Chadwick does not purport to address that

scenario either.

            True, Chadwick does state that "[o]nce law enforcement

officers have reduced luggage or other personal property not

immediately associated with the person of the arrestee to their

exclusive control, and there is no longer any danger that the

arrestee might gain access to the property to seize a weapon or

destroy evidence, a search of the property is no longer an incident

of the arrest."         433 U.S. at 15 (emphasis added).             But the

emphasized    language     shows   that    Chadwick's   "immediate   area    of

control"     rule   does    not    apply   to   "personal    property     . . .


                                     - 19 -
immediately associated with the person of the arrestee," id., and

so merely operates in parallel to the holdings in                           Robinson,

Gustafson, and Edwards.          Thus, because Chadwick does not address

what, if any, personal property carried or worn by the arrestee at

the time of the arrest beyond the cigarette packages in Robinson

and Gustafson and the clothing in Edwards constitutes "personal

property     . . . immediately         associated   with   the      person    of   the

arrestee," Chadwick does not address whether a held briefcase like

the one in Eatherton is to be treated the way that the personal

property in those three cases was.           As a result, Chadwick gives no

"indication that the result in [Robinson and Gustafson] would have

been   any    different    had    the    cigarette     packages      been     in   the

defendants' hands rather than in their pockets or if they had been

dropped to the ground in response to police command."                    Eatherton,

519 F.2d at 610.

             Simply     put,   Eatherton     was    concerned       about     drawing

distinctions     between       types    of   containers       in    an   arrestee's

"immediate     possession,"      Eatherton,      519   F.2d    at    610     (quoting

Edwards, 415 at 803), at the time of arrest -- a problem that is

hardly trivial given the range of containers people may carry

beyond cigarette packages, from holsters to purses to backpacks.

But, as      Chadwick    had no reason to address that line-drawing

problem, it cannot offer any insight into how to resolve that




                                        - 20 -
problem.    We thus do not see how Chadwick undermines Eatherton's

rationale for upholding the search of the briefcase in Eatherton.

                                 2.

           Perez does argue that Gant undermines Eatherton even if

Chadwick does not.   But here, too, we disagree.

           Gant relied on Chimel in holding that courts had wrongly

interpreted New York v. Belton, 453 U.S. 454 (1981), to have held

that all personal property in an automobile was categorically

searchable incident to an occupant's arrest.       Gant, 556 U.S. at

348-52.    Perez contends that it follows from Gant that the search

of his backpack is no different from the car search in that case.

           But, Gant, like Chadwick, said nothing about whether the

rule of Robinson (as applied in Gustafson and Edwards) governs a

container that an arrestee is carrying at the time of the arrest

(or that is dropped in response to police command at that time).

Indeed, Gant did not address carried personal property at all,

because it concerned only whether a car may be searched incident

to a lawful arrest of an occupant of the car.       Thus, Gant is no

different from Chadwick in the relevant respect, and so provides

no basis for our concluding that Eatherton has been stripped of

its controlling force.     For, like Chadwick, Gant has literally

nothing to say about where the line should be drawn in searches




                               - 21 -
incident to arrest when it comes to things an arrestee carries at

the time of the arrest.4

                                      D.

               The dissent appears to accept that neither Chadwick nor

Gant       directly   overrules   Eatherton.     The   dissent    nonetheless

contends that we still can be confident that if the panel in

Eatherton knew what we do in consequence of Chadwick and Gant,

that panel would have abandoned its hard line about the difficulty

of drawing hard lines.        As the dissent sees it, the panel in that

event would have "centered its analysis around 'immediate control'

rather than shoehorning the search of a closed container into being

'of the [arrestee's] person.'"             Dissent at 49.   But we see no

"clear and convincing" case for that conclusion.                 Guerrero, 19

F.4th at 552.

               Chadwick does make clear that no per se rule establishes

that "luggage" within the "immediate area of control" of an



       Perez does at points argue that, under Gant, the location
       4

of a container "relative to the arrestee at the time of arrest is
irrelevant" when determining whether the container can be searched
without a warrant, because all such searches should be evaluated
based on the container's location at the time of its search. But,
as Gustafson and Edwards show, the application of Robinson's
categorical rule depends, as to at least some personal property,
on the property's location at the time of the arrest and not at
the time of the search.      And, as we have explained, there is
nothing in Gant that undermines Robinson, Gustafson, or Edwards.
We thus do not see how Perez's time-of-the-search contention,
insofar as it is meant to address all containers, can be reconciled
with Robinson as it was applied in Gustafson and Edwards.


                                    - 22 -
arrestee at the time of the arrest may be warrantlessly searched.

See Chadwick, 433 U.S. at 16 n.10.          Thus, Chadwick does prompt the

question of why it would be per se reasonable to search a briefcase

that is held (or dropped upon police command) by an arrestee at

the time of the arrest.

             But Chadwick applied the "immediate control" test to a

container that was not carried by the arrestee at the time of the

arrest.      By contrast, the Eatherton panel was addressing only how

to treat a container that an arrestee was carrying at that time,

so the Eatherton panel did not purport to suggest that the Robinson

rule would apply to nearby containers not carried by the arrestee

at the time of the arrest.        As a result, Chadwick fails to provide

a clear and convincing reason for us to conclude that the Eatherton

panel would have reversed course had it known about Chadwick.

             That is especially so given that Chadwick, in a passage

that   the    dissent     mentions    but   otherwise    ignores,   expressly

distinguishes       searches     of    personal    property     "immediately

associated" with the person of the arrestee (like the personal

property     at   issue   in   Robinson,    Gustafson,   and   Edwards)   from

searches of personal property of the arrestee that is merely within

the "immediate control" of the arrestee.          Id. at 15.    For, because

of that distinction, Chadwick did not address whether principled

lines could be drawn in this context between types of containers

that are carried by the arrestee at the time of arrest -- whether


                                      - 23 -
those types of containers are cigarette packs, wallets, purses,

fanny packs, holsters, or briefcases.                      Yet Eatherton's clearly

expressed concern was that such lines could not be drawn.                              See

Eatherton, 519 F.2d at 610.

              Gant   similarly     offers        no    relevant    insight     into    the

proper way to resolve the line-drawing problem that troubled the

Eatherton      panel.        Because      Gant     addresses      only    searches      of

automobiles, it says nothing about what distinctions might be

tenable when it comes to containers that an arrestee is carrying

at the time of the arrest.

              We thus fail to see how we could be confident that

Chadwick or Gant -- or even the two taken together -- would have

led the Eatherton panel to "center" its analysis of the briefcase

on the "immediate control" question.                   Were the panel to have done

so, it would have been forced to draw the very distinctions between

the   types    of    carried    containers         that    it    concluded     were    too

"gossamer" to make.          Eatherton, 519 F.2d at 610.                But not a word

in either Chadwick or Gant would give the Eatherton panel reason

to    think   that,     contrary     to    the        panel's   initial    assessment,

distinctions of substance as to such containers could be made in

a "principled" manner.          See id.

              Of course, the dissent is right that, in the wake of

Chadwick      and    Gant,   other     circuits         have    drawn    the   kinds   of

distinctions that Eatherton refused to make.                    See United States v.


                                          - 24 -
Knapp, 917 F.3d 1161, 1168 (10th Cir. 2019) (holding that the

search of a purse was governed by the Chimel standard because the

purse   "was    not   concealed   under   or     within   [the    defendant's]

clothing" and "was easily capable of separation from her person");

United States v. Shakir, 616 F.3d 315, 321 (3rd Cir. 2010) ("[A]

search is permissible incident to a suspect's arrest when, under

all the circumstances, there remains a reasonable possibility that

the arrestee could access a weapon or destructible evidence in the

container or area being searched.").         But post-Eatherton precedent

is not uniformly at odds with Eatherton, as even the dissent

acknowledges     in   describing    how     other      circuits   reacted   to

Chadwick -- at least prior to Gant.          See Dissent at 39.

           Indeed, some circuits after Chadwick but before Gant

appeared   to   follow   Eatherton's      lead    in   categorizing   certain

carried items as "of the person."           Two months after Chadwick was

decided, for example, the Fourth Circuit assumed that warrantless

searches of objects carried in an arrestee's hands were permissible

as searches "of the person incidental to an arrest." United States

v. Wyatt, 561 F.2d 1388, 1391 (4th Cir. 1977) (search of a notebook

that arrestee retrieved from his car after being arrested).                 And

four years later, in United States v. Graham, the Seventh Circuit

explained that a "shoulder purse carried by a person at the time

he is stopped lies within the scope of a warrant authorizing the

search of his person."      638 F.2d 1111, 1114 (7th Cir. 1981).


                                   - 25 -
             Although the question in Graham was whether the purse

was "of the person" for purposes of a search warrant authorizing

a search of the person, and there was no issue of a warrantless

search incident to an arrest, the Seventh Circuit's reasoning

nevertheless aligns neatly with Eatherton's.         As the Seventh

Circuit explained, "[c]ontainers . . . while appended to the body,

are so closely associated with the person that they are identified

with and included within the concept of one's person.           To hold

differently would be to narrow the scope of a search of one's

person to a point at which it would have little meaning."           Id.

And almost two decades later, the Eighth Circuit followed the

Seventh Circuit's lead and explained that a purse, for purposes of

the       search-incident-to-arrest   exception,   was     an    object

"immediately associated" with one's person, even though the purse

in that case was also within the arrestee's area of "immediate

control."      Curd v. City Court, 141 F.3d 839, 843-44 (8th Cir.

1998).     Indeed, the Eighth Circuit agreed "with the general view"

of other courts that "concluded that a purse, like a wallet, is an

object 'immediately associated' with the person."        Id. (citations

omitted).5


      5To be sure, four months later, the Eighth Circuit approved
a backpack search because "the search of his person and backpack
was lawful as a search incident to arrest," seemingly
distinguishing "person" from "backpack" and citing a case for the
idea that possessions within "immediate control" can be searched.
United States v. Oakley, 153 F.3d 696, 698 (8th Cir. 1998).


                                 - 26 -
            Thus, to the extent that post-Chadwick precedents from

sister circuits may shed light on what the Eatherton panel would

have done with the benefit of them, we do not see how the pre-Gant

precedents of that ilk do. Even though some of those post-Chadwick

but   pre-Gant   precedents   adopt    the   dissent's    position,    these

precedents are, as a group, too varied to justify application of

the second exception to the law-of-the-circuit doctrine.

            The dissent does also cite to post-Gant sister-circuit

cases that extend Gant to non-vehicle contexts.          See, e.g., United

States v. Davis, 997 F.3d 191, 193 (4th Cir. 2021) ("Gant applies

beyond the automobile context to the search of a backpack.");

United States v. Knapp, 917 F.3d 1161, 1168 (10th Cir. 2019)

("[A]lthough     Gant   specifically    addressed   the    search     of   an

automobile, its principles apply more broadly."); United States v.

Cook, 808 F.3d 1195, 1199 n.1 (9th Cir. 2015) ("We do not read

Gant's holding as limited only to automobile searches because the

Court tethered its rational to the concerns articulated in Chimel,

which involved a search of an arrestee's home."); Shakir, 616 F.3d

at 318 ("[T]he Government contends that the rule of Gant applies

only to vehicle searches.       We do not read Gant so narrowly.").

But these out-of-circuit cases also fail to show what is required

to justify applying the second exception to the law-of-the-circuit

doctrine.




                                 - 27 -
             Even after Gant, the Supreme Court recognized in Riley

v. California that "[l]ower courts applying Robinson and Chimel

. . . have approved searches of a variety of personal items carried

by an arrestee" and cited to a case where the D.C. Circuit upheld

the search of a purse incident to the arrest of its owner.             573

U.S. 373, 392-93 (2014) (citing, inter alia, United States v. Lee,

501   F.2d   890,   892   (D.C.   Cir.   1974)).   And   Riley   repeatedly

described Gant as a case involving automobile searches without in

any way suggesting that Gant had worked a reformation of Robinson's

rule for searches of at least some personal property on the person

of the arrestee at the time of the arrest.           See 573 U.S. at 398

("But Gant relied on 'circumstances unique to the vehicle context'"

(quoting Gant, 556 U.S. at 343)); id. at 385 ("Gant added . . . an

independent exception for a warrantless search of a vehicle's

passenger compartment . . . . That exception stems not from Chimel

. . . but from 'circumstances unique to the vehicle context.'"

(quoting Gant, 556 U.S. at 343)).         Thus, the post-Gant cases from

sister circuits do not show in a clear and convincing way that the

Eatherton panel -- with the benefit of Gant -- would have ruled

the same way that those circuits had.

             We note, too, that Riley made its observation about how

other circuits had applied Robinson post-Chadwick while addressing

whether the rule of Robinson extends to the search of the data on

an arrestee's carried cellphone.         Riley, 573 U.S. at 392-93.   Yet,


                                    - 28 -
in doing so, the Court both expressly reaffirmed that Robinson

survived Chadwick as to at least some personal property on the

person of the arrestee at the time of arrest, id. at 384, 394, and

highlighted the fact that Chadwick expressly exempted from its

"immediate control" test "personal property . . . immediately

associated with the person of the arrestee[,]" id. at 384 (first

alteration in original) (quoting Chadwick, 433 U.S. at 15).

           Finally, although Riley carefully explained that the

officer-safety,     evidence-collection,       and     diminished-privacy

rationales for Robinson's rule did not apply to a cell phone's

data, the Court said nothing in doing so that "clear[ly] and

convincing[ly]"    indicates,    Guerrero,    19     F.4th   at   552,   that

Robinson's rule has no application to a container that is of the

same "order" as a briefcase, Eatherton, 519 F.2d at 610.                 Riley

does   suggest   that,   based   on   those   rationales,     a   200-pound

double-locked storage trunk may fall outside Robinson's rule even

if the arrestee happens to be dragging the trunk along behind him.

See Riley, 573 U.S. at 394.      But Eatherton did not itself suggest

otherwise.   Rather, Eatherton held only that a briefcase that the

arrestee was carrying at the time of the arrest fell within

Robinson's rule because the distinction between such a container

when held in hand and a cigarette package when carried in a pocket

was "gossamer" and because it was "not easy to rest a principled




                                 - 29 -
articulation of the reach of the [F]ourth [A]mendment upon the

distinction."       Eatherton, 519 F.2d at 610.

            We note, too, that Riley's comment about the potential

exclusion of the dragged trunk from Robinson's rule was based on

the   notion      that   "[m]ost      people     cannot   lug     around"     a    trunk

containing "every piece of mail . . . every picture . . . or every

book or article they have read" and on the observation that "nor

would they have any reason to attempt to do so."                    Id. at 393-94.

Yet, of course, most people can carry a briefcase and often have

reason to do so.         Indeed, Perez himself does not argue that Riley

is the case that would have led the Eatherton panel to rule other

than it did, as he contends only that Riley merely excluded digital

content from Robinson's rule.

                                           E.

            We close by addressing what may be our key point of

disagreement with our dissenting colleague -- the proper scope of

the second exception to the law-of-the-circuit doctrine.                          As we

see   it,   the    whole   point      of   the   doctrine    is    to   ensure      that

individual     panels      of   our    court      do   not   --    in   an    ad     hoc

way -- second-guess prior circuit precedents just because the

panels are convinced that those precedents are wrong.                        Thus, the

determination of whether a prior panel decision binds a future

panel cannot depend on whether there are sound reasons to conclude

that the prior panel got it wrong.                Yet, the post-Eatherton body


                                       - 30 -
of precedent that the dissent invokes shows, in our view, that

there are merely reasons of that sort when it comes to Eatherton,

as that body of caselaw fails to provide "a clear and convincing

basis to believe that the [Eatherton] panel would have decided the

issue differently."       Guerrero, 19 F.4th at 552.

            A comparison of this case with Guerrero -- which is our

most     recent    case   to   find   the   second   exception   to   the

law-of-the-circuit doctrine to be satisfied -- underscores the

point.    In finding the second exception to the doctrine applicable

there, we relied on an unbroken string of intervening Supreme Court

precedents.       Id. at 555-57.   Those precedents, we explained, each

had made sweeping statements that contradicted the very rationale

that the prior panel had relied on in ruling that a warrantless

search had to be subjectively and not just objectively aimed at

addressing an exigency to be lawful.         See id., 19 F.4th at 554.

And while we acknowledged that none of those precedents directly

overruled the prior panel decision, we pointed out that one of

them rejected the application of a subjective test with respect to

a home search, notwithstanding that the prior panel had applied

that test to a search of an automobile.       See id. at 555-56 (citing

Maryland v. Buie, 494 U.S. 325 (1990)).         We thus explained that,

given the heightened privacy interests at stake in home searches,

it would be most strange to conclude that the prior panel would

stick with its position that a subjective test had to be used for


                                   - 31 -
a search of a car if that panel had the benefit of the intervening

Supreme Court precedent.     See id. at 557.

          Here, by contrast, the relevant intervening Supreme

Court precedents are Chadwick and Gant -- neither of which even

addresses a search of personal property carried by an arrestee at

the time of the arrest, let alone whether and how to distinguish

between types of such personal property, at least as between

briefcases and cigarette packages.     We thus do not see how we could

reason from either of those precedents to the determination that

there is a clear and convincing basis on which to conclude that

the Eatherton panel would have decided differently with the benefit

of knowing what we now do.    And the fact that sister circuits have

relied on Chadwick and Gant to chart a different course than

Eatherton cannot provide the required clarity, as the second

exception to the law-of-the-circuit doctrine does not apply just

because several other circuits have chosen not to follow one of

our prior rulings.

          Accordingly,       we     conclude    that,    under    the

law-of-the-circuit doctrine, the en banc process supplies the

proper means for our Court to reconsider Eatherton in light of all

that has transpired in its wake.      Through that process, the Court

as a whole rather than this single panel can examine Eatherton and

the question of whether Eatherton's line-drawing concern justifies

its decision to treat an openly carried container like a briefcase


                                  - 32 -
the way that the Supreme Court treated the cigarette containers in

Robinson and Gustafson and the clothing in Edwards.   And so, until

then, the rule laid down in Eatherton controls this case about the

things we carry, as Perez makes no argument that Eatherton can be

distinguished on the facts.6

                                III.

          For the reasons set out above, the District Court's

judgment of conviction is affirmed.



                   -Dissenting Opinion Follows-




     6 We do recognize that a determination that a Fourth Amendment
precedent of our court remains binding may well bear on whether
the good-faith exception to the warrant requirement applies. See
Davis, 564 U.S. at 232 ("[P]olice . . . searches conducted in
objectively reasonable reliance on binding appellate precedent are
not subject to the exclusionary rule.").      But, given the vital
role that the law-of-the-circuit doctrine plays in ensuring the
orderly process of lower court adjudication, that fact provides no
reason for us to be less strict in applying the law-of-the-circuit
doctrine than we have long been.


                               - 33 -
              MONTECALVO, Circuit Judge, dissenting.            I view United

States v. Eatherton, 519 F.2d 603 (1st Cir. 1975), differently

than the majority, particularly as to how the exception to the

law-of-the-circuit      doctrine   applies      here.       Further,    applying

modern Supreme Court precedent, I would find that the search of

Perez's backpack violated his Fourth-Amendment rights.                   I would

also find that the good-faith exception is not applicable here.

Accordingly, and for the reasons that follow, I would reverse the

decision of the district court on Perez's motion to suppress and

vacate the judgment of conviction.

                   I. The Law-of-the-Circuit Doctrine

              This appeal arises from the denial of a motion to

suppress the warrantless search of the backpack Perez was wearing

at the time of his arrest.         As the majority notes, that search

should   be    viewed   through   the   scope   of   "the    basic     rule   that

'searches conducted outside the judicial process, without prior

approval by judge or magistrate are per se unreasonable under the

Fourth Amendment -- subject only to a few specifically established

and well-delineated exceptions.'"         Arizona v. Gant, 556 U.S. 332,

338 (2009) (quoting Katz v. United States, 389 U.S. 347, 357

(2009)).      One such exception is that of the search incident to

arrest. Id. There are two grounding principles to that exception:

(1) to protect officer safety and (2) to preserve evidence.                   Id.




                                   - 34 -
             The     development     of       this   exception    has    evolved   over

decades of caselaw, both in the Supreme Court and this Circuit.

To that end, as to our prior decisions, we are bound by the

law-of-the-circuit doctrine.              United States v. Barbosa, 896 F.3d

60, 74 (1st Cir. 2018).              However, there are exceptions to that

doctrine, as it is "neither a straightjacket nor an immutable

rule."      Id. (quoting Carpenters Local Union No. 26 v. U.S. Fid. &

Guar. Co., 215 F.3d 136, 142 (1st Cir. 2000)).                      One exception is

"when the holding of a previous panel is contradicted by subsequent

controlling authority, such as a decision by the Supreme Court, an

en   banc    decision     of   the    originating        court,     or   a    statutory

overruling."       Id.    Another exception exists "when 'authority that

postdates      the       original     decision,          although       not    directly

controlling, nevertheless offers a sound reason for believing that

the former panel, in light of fresh developments, would change its

collective mind.'"         Id. (quoting Williams v. Ashland Eng'g Co., 45

F.3d 588, 592 (1st Cir. 1995)).

             The majority's opinion rests on a case decided by a panel

of   this    court    nearly   half       a    century    ago:    United      States   v.

Eatherton, 519 F.2d 603 (1st Cir. 1975).                         Admittedly, should

Eatherton remain good law, it is controlling here.                         In my view,

however, the second exception to the law-of-the-circuit doctrine,

delineated above, is applicable under these circumstances.                             In

light of the major developments to the search-incident-to-arrest


                                          - 35 -
exception    postdating   Eatherton,      including       modern     binding      and

persuasive precedent on the propriety of warrantless searches

incident to arrest, I think that the Eatherton panel would have

come to a different conclusion.           To justify this conclusion, an

analysis    of   Eatherton     itself    and     a   brief    history      of     the

developments following Eatherton's publication is necessary.

                                A. Eatherton

            As described in the majority opinion, Eatherton involved

the warrantless search of a briefcase that the arrestee was holding

when first approached by law enforcement.               519 F.2d at 609.        After

the arrestee was frisked and placed in the back of a police

vehicle, the officers searched the briefcase, and the contents

were later admitted at trial.           Id.    The defendant challenged the

search of his briefcase as violative of his Fourth-Amendment

rights.    Id. at 609-10.

            The Eatherton panel noted that the appellant's strongest

support for his Fourth-Amendment challenge laid in Chimel v.

California, 395 U.S. 752 (1962); however, the panel recognized

that Chimel cited with approval to Draper v. United States, 358

U.S. 307 (1959), a case involving a "virtually identical" search

to the one at issue in Eatherton.         519 F.2d at 610.         The Eatherton

panel then cited to a number of cases from our sister circuits

that,     applying   Chimel,    upheld        similar     searches    of    closed

containers carried by the arrestee. 519 F.2d at 610 (citing United


                                   - 36 -
States v. Maynard, 439 F.2d 1086 (9th Cir. 1971); United States v.

Mehciz, 437 F.2d 145 (9th Cir. 1971), cert. denied, 402 U.S. 974

(1971); United States ex rel. Muhammad v. Mancusi, 432 F.2d 1046

(2d Cir. 1970), cert. denied, 402 U.S. 911 (1971)).                Lastly, the

Eatherton    panel    noted   that    the     Supreme   Court's    then-recent

decisions in United States v. Robinson, 414 U.S. 218 (1973);

Gustafson v. Florida, 414 U.S. 260 (1973); and United States v.

Edwards, 415 U.S. 800 (1974), offered further guidance on the

Fourth-Amendment issue.       519 F.2d at 610.

            Relying on this case law, the Eatherton panel determined

that differentiating between the cigarette packages in Robinson

and Gustafson and the briefcase in Eatherton "requir[ed] gossamer

distinctions."       Id. at 610.     The panel further held that "[w]hile

a briefcase may be a different order of container from a cigarette

box, it is not easy to rest a principled articulation of the reach

of the [F]ourth [A]mendment upon the distinction."                Id.   Relying

on Edwards, the Eatherton panel emphasized that once the briefcase

was "properly seized" as "incident to [the defendant's] arrest"

any expectation of privacy the defendant held was diminished.              Id.

at 610-11.

                                B. Chadwick

            After Eatherton, the Supreme Court decided United States

v. Chadwick, 433 U.S. 1 (1977).          In Chadwick, the Court examined

the search of a 200-pound footlocker stowed in the trunk of the


                                     - 37 -
defendant's car at the time of arrest.           433 U.S. at 3-4.       Officers

subsequently seized the footlocker, transported it to a federal

building, and then, an hour and a half later and without a warrant,

searched the footlocker.       Id. at 4.      The officers had no reason to

believe     the   footlocker    held    inherently       dangerous     items   or

contained evidence that could lose value over time. Id. Examining

the nature of the footlocker, the Court noted that "[l]uggage

contents are not open to public view . . . nor is luggage subject

to regular inspections and official scrutiny on a continuing

basis."    Id. at 13.   "[L]uggage is [also] intended as a repository

of personal effects."     Id.

            Chadwick    reiterated     that     "[t]he     potential     dangers

lurking in all custodial arrests make warrantless searches of items

within the 'immediate control' area reasonable without requiring

the arresting officer to calculate the probability that weapons or

destructible evidence may be involved."            433 U.S. at 14-15.          But

Chadwick    importantly   clarified     that    "warrantless     searches       of

luggage or other property seized at the time of an arrest cannot

be justified as incident to that arrest either if the search is

remote in time or place from the arrest . . . or no exigency

exists."     Id. at 15 (cleaned up).          Finally, the Chadwick Court

concluded    that   "[o]nce    law   enforcement     officers   have     reduced

luggage or other personal property not immediately associated with

the person of the arrestee to their exclusive control, and there


                                     - 38 -
is no longer any danger that the arrestee might gain access to the

property to seize a weapon or destroy evidence, a search of that

property is no longer an incident of the arrest."        Id.   Put another

way, "when no exigency is shown to support the need for an

immediate search, the Warrant Clause places the line at the point

where the property to be searched comes under the exclusive

dominion of police authority."      Id.

                      C. Cases Postdating Chadwick

             After Chadwick, several of our sister circuits addressed

situations involving items that an arrestee was holding or carrying

at the time of arrest and questioned the breadth of Chadwick,

reaching mixed results.       See United States v. Han, 74 F.3d 537,

543   (4th    Cir.   1996)   (finding   that,   after   Chadwick,   "[t]he

determinative question appears to be whether the time and distance

between elimination of the danger and performance of the search

were reasonable" and holding that "when a container is within the

immediate control of a suspect at the beginning of an encounter

with law enforcement officers; and when the officers search the

container at the scene of the arrest; the Fourth Amendment does

not prohibit a reasonable delay . . . between the elimination of

danger and the search"); see also United States v. Garcia, 605

F.2d 349, 356-57 (7th Cir. 1979) (noting the "less than uniform"

application of Chadwick across the circuits).




                                  - 39 -
            In United States v. Calandrella, 605 F.2d 236 (6th Cir.

1979), cert. denied, 444 U.S. 991 (1979), the            Sixth Circuit

examined a briefcase seized from the person at the time of arrest.

That court, examining Chadwick, noted that "the primary [F]ourth

[A]mendment interest [is] in the privacy of the contents of [a

container], not in the simple possession of the receptacle."          Id.

at 249. Therefore, the defendant had an increased privacy interest

in the briefcase, like the footlocker in Chadwick, the "very

purpose [for which] is to transport papers and other items of an

inherently personal, private nature."       Id. (internal quotations

omitted).     Ultimately, the Calandrella court found that under

Chadwick, "once the agents had seized the item and reduced it to

their exclusive control there was no further danger that the

defendant     would   secure   therefrom   either   a   weapon   or   an

instrumentality of escape, or would destroy evidence contained in

the briefcase."       Id. at 249, 251-52 (expressly overturning its

prior line of cases upholding searches of suitcases "even after

the item has been seized and the suspect subdued" and citing to

courts that had made similar decisions prior to Chadwick, including

Eatherton).

            Several other circuits also recognized the applicability

of Chadwick to cases involving carried containers.          See United

States v. Berry, 571 F.2d 2, 3 (7th Cir. 1978) (holding that "until

Chadwick, there was no reason for law enforcement officials to


                                 - 40 -
believe that attache cases were not among those personal effects

which, under [Robinson], could be seized as part of a 'full search

of the person' incident to a lawful arrest, and which, under

[Edwards], could be searched several hours after the suspect had

been taken into custody"); see also United States v. Stewart, 595

F.2d 500, 503 (9th Cir. 1979) (finding that if Chadwick was

applicable, "it would require suppression of the contents of the

attache case"); United States v. Myers, 308 F.3d 251, 273 (3d Cir.

2002) (examining the search of a "school bag" under the immediate

control analysis and citing Chadwick's rationale).

                                D. Gant

           Later, in Arizona v. Gant, 556 U.S. 332 (2009), the Court

revisited the search-incident-to-arrest exception.     The Court once

again emphasized that the limitation on that exception "ensures

that the scope of a search incident to arrest is commensurate with

its purposes of protecting arresting officers and safeguarding any

evidence of the offense of arrest that an arrestee might conceal

or destroy."    Id. at 339.    Relying on the principles articulated

in Chimel, the Court reiterated that "[i]f there is no possibility

that an arrestee could reach into [an] area that law enforcement

officers   seek      to   search,   both   justifications   for   the

search-incident-to-arrest exception are absent and the rule does

not apply."    Id.




                                - 41 -
                          E. Cases Postdating Gant

              The   decision     in   Gant   has   been    instrumental     in   the

understanding and application of the Fourth Amendment and the

search-incident-to-arrest doctrine.                After Gant, circuit courts

applied that precedent and the immediate control analysis to

containers outside of the vehicle context.                 See United States v.

Shakir, 616 F.3d 315, 318 (3d Cir. 2010), cert. denied, 562 U.S.

1116 (2010) (examining the search of a gym bag under the "narrowed"

scope    of   the   search-incident-to-arrest            doctrine   under      Gant);

United   States     v.   Cook,    808   F.3d     1195,    1199   (9th   Cir.   2015)

(applying the immediate control analysis to a backpack); United

States v. Davis, 997 F.3d 191, 193 (4th Cir. 2021) (holding that

"Gant applies beyond the automobile context to the search of a

backpack"); United States v. Knapp, 917 F.3d 1161, 1168-70 (10th

Cir. 2019) (considering whether the search of an arrestee's purse

was justified under Chimel and Gant); see also United States v.

Hill, 818 F.3d 289, 295 (7th Cir. 2016) (applying immediate control

analysis to bag); United States v. Matthews, 532 Fed. Appx. 211,

217-19 (3d Cir. 2013) (finding that the search of a backpack could

not be justified under the immediate control analysis of the

search-incident-to-arrest doctrine); cf. United States v. Perdoma,

621 F.3d 745, 750-51 (8th Cir. 2010), cert. denied, 563 U.S. 992

(2011) (upholding the warrantless search of a "small bag" where

"the search of the bag occurred in close proximity to where [the


                                        - 42 -
arrestee] was restrained" and the arrestee had already run from

officers once; but holding that a closer application of Gant was

not necessary under the circumstances).        Many of these cases are

instructive as to how Gant must be applied to cases involving

carried containers.

          In   Shakir,   the   Third    Circuit    was   faced    with     the

warrantless search of a gym bag initially held by an arrestee.

616 F.3d at 316.    The defendant there argued that the search of

his bag was in violation of his Fourth-Amendment rights because he

was already handcuffed at the time of the search and could not

have accessed the bag.    Id. at 317.      In response, the government

cited several cases upholding searches conducted while an arrestee

was handcuffed.    Id.   However, the Third Circuit noted that the

government relied solely on pre-Gant cases.        Id. at 318.    The court

emphasized "Gant as refocusing [its] attention on a suspect's

ability (or inability) to access weapons or destroy evidence at

the time a search incident to arrest is conducted."              Id.     Thus,

the Shakir court was "left to consider, under Gant and other

relevant precedents, whether [the defendant] retained sufficient

potential access to his bag to justify a warrantless search."              Id.

at 319.

          In   considering     that    question,   our   sister        circuit

"underst[ood] Gant to stand for the proposition that police cannot

search a location or item when there is no reasonable possibility


                                 - 43 -
that the suspect might access it."           Id. at 320.      In accordance

with that principle, it held that "a search is permissible incident

to a suspect's arrest when, under all the circumstances, there

remains a reasonable possibility that the arrestee could access a

weapon or destructible evidence in the container or area being

searched."   Id. at 321.    Applying this legal standard to the facts

there, the Third Circuit concluded that the search was justified

because there was a "sufficient possibility" that the arrestee

could have gained access to the bag.          Id.     The court found this

even though the arrestee was handcuffed because the bag was at his

feet, he was in a public area surrounded by approximately twenty

bystanders, and there was at least one suspected confederate in

the area.    Id. at 316, 321.

            The   Ninth   Circuit    confronted     similar   questions   in

assessing the validity of a warrantless backpack search in Cook.

808 F.3d at 1199-1200.     There, the arrestee was wearing a backpack

at the time the officers approached him.          Id. at 1197.    While the

arrestee was handcuffed on the ground, but within one to two

minutes of his arrest, officers picked up the arrestee's backpack,

which was right next to the arrestee, and conducted a twenty- or

thirty-second cursory search.         Id.    The officers then took the

arrestee to a more secluded area several blocks away and performed

a more thorough search of the backpack.             Id.   The arrestee only

challenged the validity of the first cursory search of his backpack


                                    - 44 -
immediately following his arrest.       Id. at 1198.       Relying on Gant,

our sister circuit found that "[t]he brief and limited nature of

the [initial] search, its immediacy to the time of arrest, and the

location of the backpack ensured that the search was 'commensurate

with   its     purposes    of   protecting     arresting        officers   and

safeguarding any evidence of the offense of arrest that [the

arrestee] might conceal or destroy.'"         Id. at 1200 (quoting Gant,

556 U.S. at 339).

             In Davis, the Fourth Circuit examined the history of the

search-incident-to-arrest       exception    and   how   Gant    altered   its

understanding of that exception.       997 F.3d at 195-200.         The Davis

court found that Gant's first holding, "that police can 'search a

vehicle incident to a recent occupant's arrest only when the

arrestee is unsecured and within reaching distance of the passenger

compartment at the time of the search'" -- a holding derived from

Chimel -- applies outside of the automobile context.               Id. at 197

(quoting Gant, 556 U.S. at 343).

             After establishing Gant's applicability outside of the

automobile search context, the Fourth Circuit analyzed whether the

warrantless search of a backpack was permissible under Gant.               Id.

at 198.   In Davis, the arrestee fled from officers while carrying

his backpack but ultimately became bogged down in a swamp with

knee-high water.     Id.   An officer drew his weapon and ordered the

arrestee out of the swamp.      Id.   The arrestee complied and dropped


                                  - 45 -
his backpack on the ground; he then laid down and was handcuffed.

Id.    Two other officers arrived at the scene, and the officers

searched the backpack that was not within the arrestee's reaching

distance.     Id.

             The Fourth Circuit then held that the warrantless search

of the backpack was unlawful, reasoning that there was "no doubt

that [the arrestee] was secured and not within reaching distance

of his backpack when [the officer] unzipped and searched it."                   Id.

At    the   time    of   the    search,    the   arrestee   was   face   down   and

handcuffed, he was outnumbered by officers three to one, and the

events had occurred in a residential area with no other people

present; the court thus had "no difficulty" in determining that

the arrestee was secured.            Id.   The court also emphasized that the

arrestee was not within reaching distance of the backpack at the

time of the search.            Id.

             F. The Impact of Modern Authority on Eatherton

             In examining the above cases carefully, I agree with the

majority that we do not have a Supreme Court opinion that is

"directly on point contradicting our precedent" in Eatherton.

United States v. Wurie, 867 F.3d 28, 34 (1st Cir. 2017).                 However,

I remain convinced that the "less common exception" to the law-

of-the-circuit       doctrine        forecloses    our   present    reliance     on

Eatherton.         The    authorities      discussed     above,    "although    not

directly controlling, offer[] a sound reason for believing that


                                        - 46 -
the [Eatherton] panel would change its collective mind."    Id.   "A

Supreme Court opinion need not be directly on point to undermine

one of our opinions."    United States v. Holloway, 630 F.3d 252,

258 (1st Cir. 2011).    Further, a decision of the Supreme Court

"can extend through its logic beyond the specific facts of its

case."   Id. (quoting Los Angeles Cnty. v. Humphries, 562 U.S. 29,

38 (2010)).

          Unlike the district court, who must apply our "precedent

unless it has unmistakably been cast into disrepute by supervening

authority," the exceptions to the law-of-the-circuit doctrine

provide us with "modest" flexibility in the application of our own

precedents.   Eulitt ex rel. Eulitt v. Me. Dep't of Educ., 386 F.3d

344, 349 (1st Cir. 2004), abrogated on other grounds by Carson as

next friend of O.C. v. Makin, 596 U.S. 767 (2022).     The majority

decision stresses that the second exception to the law-of-the-

circuit doctrine "cannot depend on whether there are sound reasons

to conclude that the prior panel got it wrong."   However, the scope

of the exception applied here is not based on whether I believe

there are sound reasons to conclude that the Eatherton panel was

wrong, but rather whether there are sound reasons for believing

that the Eatherton panel would have changed its collective mind.

And this "sound reason" standard has been reiterated by this court.

See e.g., Lewis, 963 F.3d at 23; United States v. López, 890 F.3d

332, 340 (1st Cir. 2018); Wurie, 867 F.3d at 34.


                              - 47 -
          Given that scope, in my view, had the Eatherton panel

had the benefit of both Chadwick and Gant, that panel would have

changed its collective mind as to its interpretation of the

search-incident-to-arrest doctrine.         As our sister circuits have

concluded,   Chadwick   and,    perhaps     even    more   so,    Gant    have

unquestionably     altered        our       understanding         of      the

search-incident-to-arrest      doctrine    and     "provide   a   clear   and

convincing basis" to determine that the Eatherton panel too would

have come to a different conclusion on the issue.             See Guerrero,

19 F.4th at 552.

          Chadwick made a nuanced distinction between the reduced

expectation of privacy an arrestee has of their person as compared

to possessions within their immediate control at the time of

arrest.   433 U.S. at 16 n.10.      Further, Chadwick's analysis did

not hinge on whether the possession was held by the arrestee or

was elsewhere in their vicinity.        Instead, Chadwick focused on the

nature of containers as "repositor[ies] of personal effects."7 Id.


     7 Indeed, the Supreme Court seems to agree that the result in
Chadwick would not have been different had the arrestee been
"drag[ging] [the trunk] behind them." Riley v. California, 573
U.S. 373, 394 (2014) (acknowledging the difference between the
trunk in Chadwick -- which could hold a large number of personal
items and required a warrant to search -- and "a container the
size of [a] cigarette package" at issue in Robinson). In my view,
Riley lends support for the very line-drawing about different
carried containers that Eatherton believed it was unable to make.
The majority appears to suggest that Riley distinguishes between
personal property that is difficult to carry, either due to its
size or weight, and personal property that is commonly carried,


                                 - 48 -
at 13.     Thus, although the Eatherton panel was understandably

influenced by the then-recent cases of Edwards, Robinson, and

Gustafson when assessing an arrestee's privacy interests, Chadwick

would    have   provided   the   additional   context   that   "possessions

within an arrestee's immediate control cannot be justified by any

reduced expectations of privacy caused by the arrest."            433 U.S.

at 16 n.10 (emphasis added).

            Given this understanding and Gant's refined framework

for "immediate control" searches, the Eatherton panel would have

centered    its   analysis   around   "immediate   control"    rather   than

shoehorning the search of a closed container into being "of the

person."    Specifically, I believe this modern authority would have

led the Eatherton panel to the conclusion, under Chadwick and Gant,

that searches of visible containers held or carried by an arrestee

-- like the briefcase in Eatherton -- must be treated as "immediate



such as a briefcase. See Majority at 30. I do not think this was
the Riley Court's intent. Riley notes that "[m]ost people cannot
lug around every piece of mail they have received for the past
several months, every picture they have taken, or every book or
article they have read -- nor would they have any reason to attempt
to do so." Id. at 393-94. But, the Riley Court then states that
the only way for a person to carry personal property like that
(prior to the existence of cell phones) would be to "drag behind
them a trunk of the sort held to require a search warrant in
Chadwick."    Id. at 394.     In my view, the Riley Court was
differentiating between certain containers that may be receptacles
for other personal property and small containers like those the
size of a cigarette package, while emphasizing that a container
like the trunk in Chadwick would have required a search warrant
just as a cell phone would. Id. at 394.


                                   - 49 -
control" searches.          See Knapp, 917 F.3d at 1167 (limiting Robinson

searches      to   "searches        of   an    arrestee's       clothing,       including

containers concealed under or within her clothing" and holding

that "visible containers in an arrestee's hand . . . are best

considered to be within the area of an arrestee's immediate

control").

              Further,      the    parties      here     have      not   identified    any

post-Gant      published      circuit         opinions      that    adopted     the   same

approach taken in Eatherton.              Indeed, we have found the opposite:

circuits    that     once    took    an    Eatherton-like           approach     to   cases

involving carried containers now applying the "immediate control"

analysis in similar circumstances.                  Cf. United States v. Lewis,

963 F.3d 16, 24 (1st Cir. 2020) (adhering to the law-of-the-circuit

doctrine where three sister circuits retained allegiance to this

Circuit's reasoning despite a recent Supreme Court decision);

Sanchez v. United States, 740 F.3d 47, 57 (1st Cir. 2014) (finding

that just two circuits' decisions contrary to our precedent "hardly

paint a picture of a rush to the exit so as to allow us to overrule

our   own     controlling         precedent").         In    short,      the    continued

application of Eatherton simply "runs counter to the strong modern

trend in the caselaw."             United States v. Guerrero, 19 F.4th 547,

557 (1st Cir. 2021).

              Accordingly, I find "that the gloss added by the Supreme

Court"   to    the   search-incident-to-arrest                exception        requires   a


                                          - 50 -
different approach than that taken by the Eatherton panel.            United

States v. Rodriguez, 527 F.3d 221, 225 (1st Cir. 2008).              Had the

Eatherton panel had the benefit of viewing that case "through the

prism of" Chadwick and Gant, I believe that they would have come

to a different result.       Id. at 226; see Guerrero, 19 F.4th at 559

("The bottom line [] is that given the Supreme Court cases in vogue

after [our prior decision], we believe [that] panel would (if it

had the chance) reverse its view of the . . . issue 180 degrees.").

           For these reasons, I would find that Eatherton is no

longer the law of the circuit. Instead, the appropriate rule under

Chadwick   and   Gant   is   that   the   searches   of   visible,    closed

containers held or carried by an arrestee should be analyzed as

"immediate control" searches.

                   II. Fourth-Amendment Violation

           Because I would hold that Eatherton is no longer the law

of the circuit and that the search of the backpack here should be

treated as an immediate control search, the next step is to

determine whether the search was nonetheless justified under the

circumstances presented.      Appropriate factors to be considered in

that inquiry are: "(1) whether the arrestee is handcuffed; (2) the

relative number of arrestees and officers present; (3) the relative

positions of the arrestees, officers, and the place to be searched;

. . . (4) the ease or difficulty with which the arrestee could

gain access to the searched area"; and (5) "the degree to which


                                    - 51 -
arresting officers have separated an article from an arrestee at

the time of the search."     Knapp, 917 F.3d at 1168-69.

          The district court made the necessary factual findings

to support a conclusion that the search of Perez's backpack was

violative of his Fourth-Amendment rights. The district court found

that "Perez was secured in handcuffs on the ground under [one

officer's] supervision as [another officer] was searching the

backpack on the hood or roof of [one of the officer's] vehicle,

not within reaching distance of Perez, so destruction of evidence

or access to weapons was not at stake."8       Accordingly, I would find

that under the immediate control analysis, the search of Perez's

backpack was in contravention with the warrant requirement of the

Fourth    Amendment    and      did      not      fall    within    the

search-incident-to-arrest exception.

                           III. Good Faith

          Finding that the search of Perez's backpack violated the

Fourth Amendment, however, is not the end of the inquiry.           The



     8 The government has argued before us that the backpack was
near Perez at the time of the search and that "there was a
reasonable possibility that he could access the bag," and the
search was therefore justified under the immediate control
analysis. However, it has not pointed us to any support to find
that the district court's determinations regarding Perez's
inability to reach the backpack at the time of the search were
clearly erroneous. See United States v. Oquendo-Rivas, 750 F.3d
12, 16 (1st Cir. 2014) ("We assess questions of fact . . . for
clear error."). I also do not surmise any support in the record
to find a clear error in the district court's factual findings.


                                - 52 -
Fourth Amendment "says nothing about suppressing evidence obtained

in violation of [its] command."    Davis v. United States, 564 U.S.

229, 236 (2011).    I must thus determine if the exclusionary rule

is applicable here.    "The rule's sole purpose . . . is to deter

future Fourth[-]Amendment violations" and not to redress prior

violations.   Id. at 236-37.      "Our cases have thus limited the

rule's operation to situations in which this purpose is 'thought

most efficaciously served.'"   Id. at 237 (quoting United States v.

Calandra, 414 U.S. 338, 348 (1974)).

          "When the police exhibit 'deliberate,' 'reckless,' or

'grossly negligent' disregard for Fourth[-]Amendment rights, the

deterrent value of exclusion is strong and tends to outweigh the

resulting costs."   Id. at 238 (quoting Herring v. United States,

555 U.S. 135, 144 (2009)).     On the other hand, "when the police

act with an objectively reasonable good-faith belief that their

conduct is lawful . . . or when their conduct involves only simple,

isolated negligence[,] . . . the deterrence rationale loses much

of its force, and exclusion cannot pay its way."      Id. (internal

quotations omitted).   "The government bears the burden of showing

that its officers acted with objective good faith."   United States

v. Sheehan, 70 F.4th 36, 51 (1st Cir. 2023) (quoting United States

v. Brunette, 256 F.3d 14, 17 (1st Cir. 2001)).

          The good-faith exception may be triggered "when the

police conduct a search in objectively reasonable reliance on


                               - 53 -
binding    judicial   precedent."      Davis,    564   U.S.   at   239.   But

importantly, this "exception is available only where the police

rely on precedent that is clear and well-settled."             United States

v. Sparks, 711 F.3d 58, 64 (1st Cir. 2013) (cleaned up).             "[W]here

judicial    precedent   does   not    clearly    authorize     a   particular

practice, suppression has deterrent value because it creates an

'incentive to err on the side of constitutional behavior.'" United

States v. Bain, 874 F.3d 1, 20 (1st Cir. 2017) (quoting Sparks,

711 F.3d at 64).

            Had this case fallen within the first exception to the

law-of-the-circuit doctrine -- where "the holding of a previous

panel is contradicted by subsequent controlling authority" -- the

good-faith exception would plainly not apply.             See Barbosa, 896

F.3d at 74.     For example, imagine a scenario where, post-Gant,

officers searched a vehicle incident to a recent occupant's arrest

after the occupant was secured and not within reaching distance of

the passenger compartment and without probable cause that the

vehicle contained evidence of the offense of arrest.               Regardless

of whether prior circuit law allowed this practice, that search

would be unlawful post-Gant, and the officers could not rely on

good faith.

            Admittedly,    when      the     second    exception     to   the

law-of-the-circuit doctrine applies, as I believe it does here,

there is a much closer question as to whether the good-faith


                                    - 54 -
exception applies.        Ultimately, given the deterrent value of

enforcing a regime where officers err on the side of constitutional

conduct in the face of unclear or eroded precedent, I would not

permit good faith to bar exclusion in this case.

            First and foremost, for the same reasons that I find the

second exception to the law-of-the-circuit doctrine applies here,

I am of the view that Eatherton was not the kind of "clear and

well-settled" precedent that officers could reasonably rely on.

See Sparks, 711 F.3d at 64. At the very minimum, Gant -- a landmark

case in our Fourth-Amendment jurisprudence -- called into question

the continued vitality of Eatherton.              It would be untenable to

require that Supreme Court holdings address virtually identical

factual   scenarios     before    we    consider       our    circuit     precedent

undermined and reject application of the good-faith exception.

Such a requirement would be contrary to the requirement that the

precedent   officers    rely     upon   "be    unequivocal"      when     shielding

unlawfully obtained evidence from exclusion.                 Sparks, 711 F.3d at

64.

            Second,    this   conclusion       aptly   aligns     with    the   very

purpose of the exclusionary rule: to deter future Fourth-Amendment

violations.     Davis, 564 U.S. at 236-37.                   If we do not strip

precedent     that    falls    within    the     second       exception    to   the

law-of-the-circuit doctrine of its weight as forcefully as we do

in cases under the first exception, officers would be encouraged


                                    - 55 -
to adhere to shaky precedent (no matter how potentially abrogated)

until those cases are formally and explicitly overruled.                     Because

suppression is intended to create the "incentive to err on the

side     of   constitutional        behavior,"     I     think   the    appropriate

conclusion is that when opinions authored by the Supreme Court,

particularly landmark cases like Gant, call into question our prior

precedent,      officers     must    conform     their    conduct      to   the   more

protective reading of the Fourth Amendment laid out by the Supreme

Court.    See Bain, 874 F.3d at 20 (quoting Sparks, 711 F.3d at 64).

              Finally, this is not a case where "the police engage[d]

in conduct that complie[d] with existing precedent, and the law

later change[d]."       United States v. Baez, 744 F.3d 30, 33 (1st

Cir. 2014).      Gant was decided a decade before the search at issue

here occurred, and Chadwick's guidance on closed containers has

been binding precedent for over forty years.                Cf. Sparks, 711 F.3d

at 67 (finding good faith applied where the applicable Supreme

Court    case   came   out    three    years     after    the    search     at    issue

occurred); United States v. Moore-Bush, 36 F.4th 320, 359 (1st

Cir. 2022) (mem.) (Barron, C.J., concurring) (concurring opinion

finding that good faith applied when the applicable Supreme Court

decision was published over one year after the search began).

Given my view of the impact of these cases on Eatherton, the

officers were required to follow the logic supplied by Gant and

Chadwick.


                                       - 56 -
           For these reasons, I would conclude that the good-faith

exception is not available under the circumstances and suppression

is the proper outcome to deter future Fourth-Amendment violations.

                              IV. Conclusion

           For the above stated reasons, I would abrogate Eatherton

to the extent it is inconsistent with this analysis, reverse the

district court's decision on the motion to suppress, vacate the

judgment   of   conviction,    and   remand    for   further   proceedings

consistent with this opinion.




                                 - 57 -

```

---
