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

## GROUP: _overhaul2/lake/cases/United States v. Mayville.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Mayville
type: case
citation: "955 F.3d 825 (2020)"
parallel_cite: ""
neutral_cite: ""
court: 10th Cir. 2020
court_level: coa
circuit: ca10
year: 2020
date_decided: 2020-04-07
docket: 19-4008
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
  opinion_url: "https://www.courtlistener.com/opinion/4742862/united-states-v-mayville/"
  cluster_id: 4742862
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Mayville
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Traffic Stops]]"
    role: Key
related:
  - "[[Traffic Stops]]"
  - "[[Rodriguez v. United States]]"
  - "[[Illinois v. Caballes]]"
  - "[[Terry Stops and Reasonable Suspicion]]"
tags:
  - case
  - fourth-amendment
  - traffic-stop
  - rodriguez
  - dog-sniff
  - prolonged-detention
  - reasonable-suspicion
  - tenth-circuit
holding: "The Tenth Circuit affirmed, holding that a nineteen-minute traffic stop that ended with a drug-dog alert did not violate Rodriguez v. United States: an officer may run a criminal-history (Triple I) check through dispatch as a negligibly burdensome safety precaution, and because the troopers diligently pursued the stop's mission and the dog sniff was contemporaneous with that pursuit — the alert coming just before the records check returned — the stop was not unreasonably prolonged, since reasonableness, not efficiency, is the touchstone of the Fourth Amendment."
---

# United States v. Mayville

*955 F.3d 825 (10th Cir. 2020)* (No. 19-4008) · U.S. Court of Appeals for the Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 4742862 → opinion 4523209 (955 F.3d 825, decided 2020-04-07, Baldock, J.); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Around 1:45 a.m., Utah Highway Patrol Trooper Tripodi stopped John Mayville's red Audi for going 71 in a 60-mph zone and saw him hunched over as if he were trying to stash something. Over roughly the next nineteen minutes, Tripodi spoke with Mayville (about six minutes), obtained his out-of-state license but no registration, and thought him confused and drowsy; he returned to his patrol car about seven minutes in, radioed dispatch to run a warrants check and an Interstate Identification Index ("Triple I") criminal-history check, and requested a narcotics dog while working on the citation. Trooper Mackleprang arrived with a dog, Hasso, around 1:59; after Mayville was patted down and stood roadside, Hasso conducted a free-air sniff and alerted at about 2:05 — less than thirty seconds before dispatch returned the records. The ensuing search found a methamphetamine pipe and two firearms, one with a silencer. Mayville pleaded guilty to drug and unregistered-silencer charges, preserving his challenge to the denial of suppression.

## Issue
Whether the troopers violated *[[Rodriguez v. United States]]* by prolonging the traffic stop beyond the time needed to complete the tasks incident to the stop's mission — in particular, whether running a Triple I criminal-history check through dispatch (rather than the in-car computer) and awaiting the dog sniff unreasonably extended the nineteen-minute detention.

## Rule
Under *[[Rodriguez v. United States|Rodriguez]]*, an officer's authority to detain ends when the tasks tied to the traffic mission "are — or reasonably should have been — completed," and ordinary inquiries plus permissible safety precautions must be completed within a reasonable time, measured by whether officers diligently pursued the stop's mission. But the inquiry is one of reasonableness, not stopwatch efficiency: "Rodriguez does not require courts to second-guess the logistical decisions of officers so long as their actions were reasonable and diligently completed within the confines of a lawful traffic stop. This is because reasonableness — rather than efficiency — is the touchstone of the Fourth Amendment." — 955 F.3d 825, slip op. at 1. ^pin-op1

## Application
A criminal-history check is a permissible, "negligibly burdensome" safety precaution incident to a traffic stop, and *[[Rodriguez v. United States|Rodriguez]]* itself approved the Tenth Circuit's officer-safety justification for such checks. Trooper Tripodi's choice to run the Triple I check through dispatch rather than his in-car computer was reasonable given Mayville's out-of-state license and vehicle, his apparent stashing, his demeanor, and his inability to produce registration — and the district court found, without [[Common Legal Terms#clear-error|clear error]], that the Triple I check did not extend the stop. Mayville's contention that the in-car computer would have been faster failed because the record never showed how long that alternative would have taken, and the Fourth Amendment does not require officers to use the least intrusive or most efficient means conceivable. Because the dog sniff and alert were contemporaneous with the troopers' reasonably diligent pursuit of the stop's mission — the alert preceding the records response — the stop was not unlawfully prolonged, and the search was valid.

## Conclusion
**Affirmed.** Judge Baldock wrote for the panel (Bacharach, Baldock, and Murphy, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Mayville* is a representative Tenth Circuit application of *[[Rodriguez v. United States|Rodriguez]]*'s **mission-and-diligence** limit on traffic-stop duration: a dog sniff that rides along with the officer's reasonable, diligent completion of records and safety tasks — and finishes before those tasks do — does not "prolong" the stop, because reasonableness, not efficiency, controls. Teach it as the diligence-side counterpart to *[[Rodriguez v. United States|Rodriguez]]*'s prohibition on adding time for an unrelated investigation.

## Appears on
- [[Traffic Stops]] — *Key*

## Sources
- [*United States v. Mayville*, 955 F.3d 825 (10th Cir. 2020)](https://www.courtlistener.com/opinion/4742862/united-states-v-mayville/) — pinpoint: slip op. at 1 (the *Rodriguez* reasonableness-not-efficiency holding; the CL opinion text carries the court's internal slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "642a56aa23924b8c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Mayville"}, "payload": {"all": [{"cite": "955 F.3d 825", "page": "825", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "955"}], "display": "955 F.3d 825", "official": {"cite": "955 F.3d 825", "page": "825", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "955"}, "official_selection_present": true, "record_id": "United States v. Mayville"}}
{"assertion_id": "2e683c02fc051802", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Mayville"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Mayville", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Mayville

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Mayville",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Mayville",
    "case_name_short": "Mayville",
    "case_name_full": "",
    "input_case_name": "United States v. Mayville",
    "court": "10th Cir. 2020",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": "2020-04-07",
    "year": 2020,
    "docket": "19-4008",
    "cluster_id": 4742862,
    "lead_opinion_id": 4523209,
    "sibling_ids": [],
    "absolute_url": "/opinion/4742862/united-states-v-mayville/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "955 F.3d 825",
      "volume": "955",
      "reporter": "F.3d",
      "page": "825",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "955 F.3d 825",
        "volume": "955",
        "reporter": "F.3d",
        "page": "825",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "955 F.3d 825",
    "official_selection": {
      "court_class": "state",
      "selected": "955 F.3d 825",
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
    "date_created": "2026-07-06T05:56:09Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:56:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:56:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:56:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:56:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-mayville--4742862",
      "to_record_id": "United States v. Mayville",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Mayville

```
                                                                                 FILED
                                                                     United States Court of Appeals
                                      PUBLISH                                Tenth Circuit

                      UNITED STATES COURT OF APPEALS                         April 7, 2020

                                                                        Christopher M. Wolpert
                            FOR THE TENTH CIRCUIT                           Clerk of Court
                        _________________________________

 UNITED STATES OF AMERICA,

       Plaintiff - Appellee,

 v.                                                         No. 19-4008
                                                  (D.C. No. 2:16-CR-00266-JNP-1)
 JOHN ELISHA MAYVILLE,                                        (D. Utah)

       Defendant - Appellant.
                      _________________________________

                     Appeal from the United States District Court
                               for the District of Utah
                          (D.C. No. 2:16-CR-00266-JNP-1)
                       _________________________________

Bretta Pirie, Assistant Federal Public Defender (Scott Keith Wilson, Federal Public
Defender, with her on the brief), Salt Lake City, Utah, for Defendant-Appellant.

Stewart M. Young, Assistant United States Attorney (John W. Huber, United States
Attorney, with him on the brief), Salt Lake City, Utah, for Plaintiff-Appellee.
                        _________________________________

Before BACHARACH, BALDOCK, and MURPHY, Circuit Judges.
                 _________________________________

BALDOCK, Circuit Judge.
                    _________________________________

      Defendant–Appellant John Elisha Mayville pleaded guilty to possession of

methamphetamine with intent to distribute in violation of 21 U.S.C. § 841(a)(1) and

possession of an unregistered firearm silencer in violation of 26 U.S.C. § 5861(d).

Exercising his right under the plea agreement, Defendant challenges the district court’s
denials of his motions to suppress evidence of drugs and firearms seized from his car

by Utah Highway Patrol troopers during a traffic stop. On appeal, Defendant argues

the troopers violated his Fourth Amendment rights described in Rodriguez v. United

States, 575 U.S. 348 (2015), because they unjustifiably prolonged the traffic stop

beyond the time needed to complete the tasks incident to the stop’s mission.

      Our jurisdiction arises under 28 U.S.C. § 1291, and we affirm. The Supreme

Court’s decision in Rodriguez constrains what law enforcement officers may do during

a routine traffic stop in the absence of additional reasonable suspicion. But Rodriguez

does not require courts to second-guess the logistical decisions of officers so long as

their actions were reasonable and diligently completed within the confines of a lawful

traffic stop. This is because reasonableness—rather than efficiency—is the touchstone

of the Fourth Amendment. Because the traffic stop here did not exceed the time

reasonably required to execute the tasks relevant to accomplishing the mission of the

stop, Defendant’s nineteen-minute roadside detention accorded with the Fourth

Amendment’s dictates. Thus, the district court did not err in denying Defendant’s

motions to suppress.

                                          I.

      Around 1:45 a.m. on May 6, 2016, Utah Highway Patrol Trooper Jason Tripodi

stopped a red Audi for traveling 71 m.p.h. in a 60-m.p.h. zone, in violation of state

law. After the Audi came to a stop, Trooper Tripodi observed the driver hunched over

in the vehicle as if he was “trying to stash something or hide something.” Trooper



                                          2
Tripodi approached the Audi and spoke with Defendant, who was the driver and sole

occupant of the vehicle, about his speeding.

      During this initial interaction, which lasted about six minutes, Defendant

informed Trooper Tripodi he was traveling to Grand Junction, Colorado, from Lake

Havasu, Arizona. Trooper Tripodi asked for Defendant’s license, registration, and

proof of insurance. While Defendant searched for these documents, Trooper Tripodi

noticed Defendant had trouble finding the requested paperwork. After several minutes,

Defendant provided his out-of-state driver’s license to Trooper Tripodi, but he was

unable to produce any registration documents for the vehicle.

      According to Trooper Tripodi, Defendant “seemed confused” and “wasn’t able

to multitask like a normal individual would be able to” during this initial interaction.

Trooper Tripodi also observed that Defendant seemed like he “was drowsy, or

something was wrong, something was up.” Based on these observations, Trooper

Tripodi asked Defendant if he “was okay” multiple times. Trooper Tripodi asked

Defendant to accompany him to the patrol car to chat while he filled out the paperwork

for the stop. Defendant declined this invitation and remained in his vehicle.

      Around 1:52 a.m., seven minutes after the stop began, Trooper Tripodi returned

to his patrol car and began filling out paperwork for the stop. He also radioed dispatch

to run a records check on Defendant, which consisted of two components. First,

Trooper Tripodi asked dispatch to run Defendant’s license and check for warrants.

Second, the trooper requested Defendant’s criminal history through the Interstate

Identification Index, commonly referred to as a Triple I check. After radioing dispatch

                                           3
for the records, but before dispatch returned the results, Trooper Tripodi requested a

narcotic detector dog.     He then continued working on the citation, including

“attempting to figure out whose vehicle it was because [Defendant] ha[d] no

registration paperwork.”

      At approximately 1:59 a.m., Trooper Scott Mackleprang arrived at the scene

with his narcotic detector dog, Hasso. At this point, Trooper Tripodi backed up his

patrol car because he anticipated possibly “run[ning] through sobriety tests or

something like that at a later point in the stop.” After briefly speaking with Trooper

Tripodi, who remained in his patrol car and continued to work on the citation, Trooper

Mackleprang asked Defendant to exit the vehicle so he could screen it with Hasso.

Because Defendant refused, Trooper Mackleprang requested Trooper Tripodi’s

assistance. Trooper Mackleprang observed that Defendant was “real slow to answer”

and had delayed reactions, “almost like a blank stare,” which caused him to suspect

Defendant was impaired. Defendant ultimately exited the vehicle, and Trooper Tripodi

patted him down for weapons.

      Trooper Tripodi then stood with Defendant on the side of the road while Trooper

Mackleprang had Hasso conduct a free-air sniff around the car. At approximately 2:05

a.m., Hasso alerted to the odor of narcotics in the vehicle. And less than thirty seconds

later, dispatch responded to Trooper Tripodi’s records request with information

indicating Defendant had a criminal record. The entirety of the traffic stop, from

Trooper Tripodi’s initial contact with Defendant to Hasso’s alert, lasted approximately

nineteen minutes.

                                           4
      The subsequent search of Defendant’s vehicle revealed a methamphetamine pipe

under the driver’s seat and two guns, one equipped with a silencer, in the engine

compartment. In the trunk, the troopers found roughly a pound of methamphetamine,

an ounce of heroin, and a scale. After discovering the guns and drugs, the troopers

placed Defendant under arrest.

      The grand jury indicted Defendant for possession of methamphetamine with

intent to distribute, possession of heroin with intent to distribute, possession of an

unregistered firearm silencer, and being a felon in possession of a firearm. Defendant

filed two motions to suppress in the district court, asserting several grounds for

suppressing the evidence seized during the traffic stop. As relevant here, he moved to

suppress evidence of the drugs and firearms as fruit of an unlawful seizure under the

Fourth Amendment. Specifically, Defendant argued Trooper Tripodi’s unreasonable

extension of the traffic stop resulted in the dog sniff and subsequent search of his

vehicle.

      After evidentiary hearings and oral arguments, the district court found the

troopers testified credibly and concluded Trooper Tripodi’s decision to run a Triple I

check through dispatch did not unconstitutionally extend the traffic stop.

Alternatively, the district court held the troopers possessed reasonable suspicion to

prolong the traffic stop to determine whether Defendant was impaired. The district

court accordingly denied Defendant’s motions to suppress.

      Defendant later entered a conditional guilty plea, reserving the right to appeal

the district court’s denials of his motions to suppress. The district court accepted the

                                           5
plea and sentenced Defendant to 126 months’ imprisonment. Exercising his right to

challenge the denials of his suppression motions, Defendant timely filed his notice of

appeal.

                                           II.

      “When reviewing the denial of a motion to suppress, we view the evidence in

the light most favorable to the government, accept the district court’s findings of fact

unless they are clearly erroneous, and review de novo the ultimate question of

reasonableness under the Fourth Amendment.” United States v. McNeal, 862 F.3d

1057, 1061 (10th Cir. 2017) (quoting United States v. Lopez, 849 F.3d 921, 925 (10th

Cir. 2017)). Defendant does not contest the legality of the initial traffic stop. Rather,

he contends the troopers’ actions—namely, Trooper Tripodi’s decision to run a Triple

I criminal-history check—were unrelated to the mission of the traffic stop and extended

its duration in violation of the Fourth Amendment. We disagree with Defendant’s

arguments.

                                           A.

      A traffic stop, even if brief and for a limited purpose, constitutes a “seizure”

under the Fourth Amendment and is subject to review for reasonableness. Whren v.

United States, 517 U.S. 806, 809–10 (1996). To be reasonable, a “traffic stop must be

justified at its inception and, in general, the officer’s actions during the stop must be

reasonably related in scope to ‘the mission of the stop itself.’” United States v. Cone,

868 F.3d 1150, 1152 (10th Cir. 2017) (quoting Rodriguez, 575 U.S. at 356). Because

Defendant does not contend the traffic stop was unjustified at its inception, our analysis

                                            6
is limited to whether the stop’s “manner of execution unreasonably infringe[d]” upon

Defendant’s Fourth Amendment rights. Illinois v. Caballes, 543 U.S. 405, 407 (2005).

      An officer’s authority to seize a driver “ends when tasks tied to the traffic

infraction are—or reasonably should have been—completed.” Rodriguez, 575 U.S. at

354. Officers may not prolong a stop beyond that point for the purpose of detecting

evidence of ordinary criminal wrongdoing unless separate reasonable suspicion exists

to justify further investigation. Id. at 354–55. Even de minimis delays caused by

unrelated inquiries violate the Fourth Amendment. Id. at 355–57.

      Defendant argues Trooper Tripodi unlawfully extended the stop because the

Triple I criminal-history check had no relation to his speeding—the traffic infraction

at issue—and is not one of the ordinary inquiries allowed under Rodriguez. But, as

Rodriguez explained, an officer’s mission during a traffic stop is both “to address the

traffic violation that warranted the stop and attend to related safety concerns.” Id. at

354 (emphasis added and citations omitted).        To be sure, this mission “includes

ordinary inquiries incident to” the traffic stop, which typically involve inspecting the

driver’s license, verifying the vehicle’s registration and insurance coverage, and

checking for any outstanding warrants against the driver.         Id. at 355.   Because,

however, “[t]raffic stops are ‘especially fraught with danger to police officers,’” id. at

356 (citation omitted), the Court has also included “negligibly burdensome” inquiries

an officer needs to make “to complete his mission safely” among permissible actions

incident to a traffic stop. Id. As Rodriguez explained, “[T]he government’s officer

safety interest stems from the mission of the stop itself.” Id.

                                            7
       This court has routinely permitted officers to conduct criminal-history checks

during traffic stops in the interest of officer safety. See, e.g., United States v. Burleson,

657 F.3d 1040, 1046 (10th Cir. 2011) (“[A]n officer may run a background check on a

motorist to check for warrants or criminal history even though the purpose of the stop

had nothing to do with the motorist’s history.”); United States v. Rice, 483 F.3d 1079,

1084 (10th Cir. 2007) (“While a traffic stop is ongoing . . . an officer has wide

discretion to take reasonable precautions to protect his safety. Obvious precautions

include running a background check on the driver . . . .” (citations omitted)). Notably,

in Rodriguez, the Court cited with approval our decision in United States v. Holt, 264

F.3d 1215, 1221–22 (10th Cir. 2001) (en banc), overturned on other grounds by

Muehler v. Mena, 544 U.S. 93 (2005), as an example of a proper inquiry during a traffic

stop. Rodriguez, 575 U.S. at 356; see also Cone, 868 F.3d at 1153 (recognizing

approval of Holt in Rodriguez and concluding an officer may reasonably ask questions

about a driver’s criminal history during a routine traffic stop). Our Holt decision, the

Court ably noted, “recogniz[ed] [an] officer safety justification for criminal record and

outstanding warrant checks.” Rodriguez, 575 U.S. at 356. Thus, an officer’s decision

to run a criminal-history check on an occupant of a vehicle after initiating a traffic stop

is justifiable as a “negligibly burdensome precaution” consistent with the important

governmental interest in officer safety.1


       1
         Several of our sister circuits have likewise concluded, post-Rodriguez, that an
officer may conduct a criminal-history check as part and parcel of the mission of a
traffic stop. See, e.g., United States v. Dion, 859 F.3d 114, 127 n.11 (1st Cir. 2017)
(“[T]he Supreme Court has characterized a criminal-record check as a ‘negligibly
                                             8
                                          B.

      Consistent with Rodriguez and circuit precedent, Trooper Tripodi was entitled

to inquire into Defendant’s criminal record during the traffic stop. But the question

remains whether the troopers’ conduct, including Trooper Tripodi’s decision to request

a Triple I check through dispatch rather than conduct the criminal-history check on the

computer in his patrol car, was reasonable under the circumstances. See United States

v. Windom, 863 F.3d 1322, 1327 (10th Cir. 2017) (“The touchstone of our analysis

under the Fourth Amendment is always ‘the reasonableness in all the circumstances of

the particular governmental invasion of a citizen’s personal security.’”) (citation

omitted). Defendant argues it was not. Again, we disagree.

      To repeat, an officer’s authority to seize a motorist “ends when tasks tied to the

traffic infraction are—or reasonably should have been—completed.” Rodriguez, 575

U.S. at 354. Thus, even ordinary inquiries incident to a traffic stop and permissible

safety precautions must be completed within a reasonable amount of time. Id. at 357.

In determining whether the duration of a traffic stop was reasonable, we consider



burdensome precaution’ that may be necessary in order to complete the mission of the
traffic stop safely.”) (quoting Rodriguez, 575 U.S. at 356)); United States v. Palmer,
820 F.3d 640, 651 (4th Cir. 2016) (“A police officer is entitled to inquire into a
motorist’s criminal record after initiating a traffic stop.”); United States v. Sanford,
806 F.3d 954, 956 (7th Cir. 2015) (“The trooper checked the occupants’ criminal
history on the computer in his car—a procedure permissible even without reasonable
suspicion.”); United States v. Frierson, 611 F. App’x 82, 85 (3d Cir. 2015)
(unpublished) (“Upon initially detaining the men, [the officer] reasonably addressed
the traffic violation that warranted the stop and attended to safety concerns. For
example, any preliminary delay in checking [the driver’s] license, registration, and
criminal history was justified as part of the stop.”).
                                           9
whether the officers diligently pursued the mission of the stop. Id. Accordingly,

officers may not undertake safety precautions for the purpose of lengthening the stop

to allow for investigation of unrelated criminal activity. Id. at 356.

      With these principles in mind, and objectively considering the totality of the

circumstances, we turn to examine Trooper Tripodi’s decision to run a Triple I check.

As explained above, an officer is permitted to run a criminal-history check as a safety

precaution during a traffic stop so long as the check does not unreasonably prolong the

stop. See id.; Holt, 264 F.3d at 1221–22. We see no reason to apply a different rule

simply because an officer elects to conduct a Triple I check through dispatch rather

than research a motorist’s criminal history on the computer in his patrol car. See United

States v. McRae, 81 F.3d 1528, 1536 n.6 (10th Cir. 1996) (indicating, in dicta, it is

reasonable for officers to run Triple I checks through dispatch as part of a routine

traffic stop); see also United States v. Hill, 852 F.3d 377, 380, 383 (4th Cir. 2017)

(holding, in the context of a twenty-minute stop, officers reasonably may search an

additional database for criminal history even though it “can be a lengthy process”).

      Defendant argues the Triple I check unlawfully extended the traffic stop because

Trooper Tripodi would have completed the stop sooner if he had confined himself to

checking records via the computer in his patrol vehicle. The problem with Defendant’s

argument is twofold. First, the district court made a factual finding that the Triple I

check did not extend the time period of the stop, and Defendant has not identified any

evidence demonstrating the court’s finding was clearly erroneous. Defendant points

to evidence showing it took less than a minute for Trooper Tripodi’s onboard computer

                                           10
to return information that showed Defendant had a valid license, his car was insured,

and the car was registered—though not to Defendant. But such a comparison is

irrelevant to our analysis. As defense counsel conceded at oral argument, nothing in

the record indicates how long it would have taken Trooper Tripodi to conduct either a

criminal-history inquiry or warrants check on the computer in his patrol car.

      Second, even if the Triple I check extended the duration of the stop, Trooper

Tripodi’s request for criminal-history records through dispatch was not unreasonable

as a matter of law. Trooper Tripodi, who the district court deemed credible, testified

that he conducted the Triple I check through dispatch because the computer in his

patrol car provides limited information, especially with respect to out-of-state drivers.

The record plainly shows Defendant provided an out-of-state license and was driving

an out-of-state vehicle. Moreover, Trooper Tripodi developed concerns based on

Defendant’s apparent stashing of something under the driver’s seat, Defendant’s

demeanor during their initial six-minute interaction, and Defendant’s inability to

provide registration paperwork for the vehicle. Given these circumstances, Trooper

Tripodi’s decision to run a Triple I check through dispatch—as opposed to limiting his

records check to the computer in his patrol car—did not unreasonably prolong the stop.

      Although Trooper Tripodi could have executed the traffic stop without running

the records check through dispatch, and instead relied exclusively on the information

available on the computer in his patrol car, his actions did not violate Defendant’s

Fourth Amendment rights.       As the Court has repeatedly admonished, the Fourth

Amendment does not require officers to use the least intrusive or most efficient means

                                           11
conceivable to effectuate a traffic stop. United States v. Sharpe, 470 U.S. 675, 687

(1985) (“The question is not simply whether some other alternative was available, but

whether the police acted unreasonably in failing to recognize or to pursue it.”). While

we can imagine other situations in which an officer’s decision to run a Triple I check

through dispatch would unreasonably prolong a traffic stop, that is not the case here.

The evidence in this case shows the troopers acted reasonably diligent in executing the

tasks incident to the traffic stop, and their actions did not unlawfully extend the stop

beyond the pursuit of the stop’s mission.2

      In sum, the district court determined dispatch responded to Trooper Tripodi’s

records request shortly after Hasso alerted to the presence of narcotics in Defendant’s

vehicle. Defendant has not shown, and we have not found, evidence in the record

demonstrating this factual finding was clearly erroneous. Because the dog sniff and

alert were contemporaneous with the troopers’ reasonably diligent pursuit of the stop’s


      2
          Approximately twelve minutes passed between the time Trooper Tripodi
returned to his patrol car after his initial interaction with Defendant and when Hasso
alerted to the odor of narcotics in the vehicle. During this period, Trooper Tripodi
radioed dispatch for records, worked on filling out paperwork for the stop, backed up
his vehicle to possibly perform sobriety tests, assisted Trooper Mackleprang after
Defendant refused to exit his vehicle, patted down Defendant for weapons, and further
questioned Defendant outside of the vehicle during the dog sniff. Before Trooper
Mackleprang arrived on the scene, Trooper Tripodi can be heard on his dash cam
asking a voice-activated google device about Lake Havasu, Arizona. Defendant argues
this shows Trooper Tripodi sat idle rather than performing the tasks incident to the
traffic stop. The district court, however, credited Trooper Tripodi’s testimony that
during this time he was also filling out paperwork for the citation and attempting to
figure out ownership of the vehicle. Defendant does not attempt to show this factual
finding was clearly erroneous. Based on the record before us, none of the trooper’s
individual actions suggest a lack of diligence in pursuing the mission of the stop.

                                             12
mission, the subsequent search of Defendant’s vehicle and discovery of evidence did

not violate his Fourth Amendment rights. The district court, therefore, properly denied

Defendant’s motions to suppress.3

                                          ***

      For the foregoing reasons, the judgment of the district court is AFFIRMED.




      3
         Because Trooper Tripodi did not unconstitutionally extend the traffic stop by
conducting the Triple I check through dispatch, we need not consider whether the
troopers possessed reasonable suspicion to prolong the stop to investigate Defendant’s
potential impairment. We also summarily dispose of Defendant’s meritless argument
that the troopers acted unreasonably in removing Defendant from his vehicle during
the traffic stop. See Maryland v. Wilson, 519 U.S. 408, 413–15 (1997) (reaffirming
rule that an officer may order a driver out of a vehicle during a traffic stop for officer
safety reasons); Holt, 264 F.3d at 1222 (explaining an officer “may order the driver
and passengers out of the vehicle in the interest of officer safety, even in the absence
of any particularized suspicion of personal danger”) (emphasis added).
                                           13

```

---

## GROUP: _overhaul2/lake/cases/United States v. Mendenhall.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Mendenhall"
type: case
citation: "446 U.S. 544 (1980)"
parallel_cite: "100 S. Ct. 1870; 64 L. Ed. 2d 497"
neutral_cite: 1980 U.S. LEXIS 102
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-06-30
docket: 78-1821
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1980-05-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Mendenhall
  varies_by_point: false
  scope_note: "The 'free to leave' test was announced in Justice Stewart's opinion (joined on the seizure point only by Justice Rehnquist) but was later adopted by the full Court and is the governing standard."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110264/united-states-v-mendenhall/"
  cluster_id: 110264
  opinion_id: 9427929
  identity_checked: true
homes:
  - page: "[[Seizure of the Person]]"
    role: "Key — Anchor"
related: ["[[Terry v. Ohio]]", "[[Florida v. Bostick]]", "[[California v. Hodari D.]]", "[[United States v. Drayton]]", "[[Schneckloth v. Bustamonte]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure-of-the-person", "free-to-leave", "consensual-encounter", "drug-courier-profile"]
holding: "The 'free to leave' benchmark: a person is seized only if, under all the circumstances, a reasonable person would not have believed himself free to leave."
lake:
  record_id: United States v. Mendenhall
  status: verified
  projected_at: 2026-07-06
---

# United States v. Mendenhall

*446 U.S. 544 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
DEA agents at the Detroit airport approached Sylvia Mendenhall in the public concourse because she fit a drug-courier profile. They identified themselves, asked to see her ticket and identification (which were in different names), and then asked her to accompany them to a nearby DEA office, where she consented to a search of her person that produced heroin. She moved to suppress, arguing she had been unlawfully seized.

## Issue
When does a police-citizen encounter become a Fourth Amendment "seizure" of the person — that is, by what standard is a person who is approached and questioned by officers deemed "seized"?

## Rule
A person is seized only when a reasonable person would not feel free to leave. "We conclude that a person has been 'seized' within the meaning of the Fourth Amendment only if, in view of all of the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave." — 446 U.S. at 554. ^pin-554

The inquiry is objective and totality-based. "Examples of circumstances that might indicate a seizure, even where the person did not attempt to leave, would be the threatening presence of several officers, the display of a weapon by an officer, some physical touching of the person of the citizen, or the use of language or tone of voice indicating that compliance with the officer's request might be compelled." — *Id.* ^pin-554a

## Application
On these facts the initial encounter was not a seizure. The agents approached Mendenhall in a public airport concourse, identified themselves, and *asked* — rather than demanded — to see her ticket and identification; they did not display weapons, touch her, or use a commanding tone. Under all those circumstances, a reasonable person would have believed she was free to leave, so no seizure occurred when she was approached and questioned. Her later agreement to accompany the agents to the office, and her consent to the search there, were voluntary. Because there was no seizure at the outset and the search was consensual, the heroin was not the product of an unlawful seizure.

## Conclusion
No Fourth Amendment seizure occurred when the agents approached and questioned Mendenhall, and her consent to the ensuing search was voluntary; the Sixth Circuit's suppression order was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The "free to leave" formulation appeared in Justice Stewart's opinion (joined on the seizure point only by Justice Rehnquist) but was **later adopted by the full Court** and is the governing test. It was refined in [[Florida v. Bostick]] and [[United States v. Drayton]] (where a person would not want to leave regardless — e.g., a bus passenger — the question is whether a reasonable person would feel free to decline the officers' requests or otherwise terminate the encounter), and in [[California v. Hodari D.]] (a show-of-authority seizure is not complete until the suspect submits).

## Appears on
- [[Seizure of the Person]] — *Key — Anchor*

## Sources
- *United States v. Mendenhall*, 446 U.S. 544 (1980) — https://www.courtlistener.com/opinion/110264/united-states-v-mendenhall/ — pinpoint: 554.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e40818204df5c7f4", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Mendenhall"}, "payload": {"all": [{"cite": "446 U.S. 544", "page": "544", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "446"}, {"cite": "100 S. Ct. 1870", "page": "1870", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "100"}, {"cite": "64 L. Ed. 2d 497", "page": "497", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "64"}, {"cite": "1980 U.S. LEXIS 102", "page": "102", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1980"}], "display": "446 U.S. 544", "official": {"cite": "446 U.S. 544", "page": "544", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "446"}, "official_selection_present": true, "record_id": "United States v. Mendenhall"}}
{"assertion_id": "7d2e5755888dac3e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-554", "record_id": "United States v. Mendenhall"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-554", "pinpoint_status": "slip-only", "quote": "? ## Rule A person is seized only when a reasonable person would not feel free to leave.", "quote_fidelity": "mismatch", "record_id": "United States v. Mendenhall", "star_marker": null}}
{"assertion_id": "c4e1e2cb60211526", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-554a", "record_id": "United States v. Mendenhall"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-554a", "pinpoint_status": "slip-only", "quote": "Examples of circumstances that might indicate a seizure, even where the person did not attempt to leave, would be the threatening presence of several officers, the display of a weapon by an officer, some physical touching of the person of the citizen, or the use of language or tone of voice indicating that compliance with the officer's request might be compelled.", "quote_fidelity": "mismatch", "record_id": "United States v. Mendenhall", "star_marker": null}}
{"assertion_id": "162e23c078f8c327", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Mendenhall"}, "payload": {"as_of_content": "1980-05-27", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Mendenhall", "scope_note": "The 'free to leave' test was announced in Justice Stewart's opinion (joined on the seizure point only by Justice Rehnquist) but was later adopted by the full Court and is the governing standard.", "varies_by_point": false}}
```

### lake record — United States v. Mendenhall

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Mendenhall",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Mendenhall",
    "case_name_short": "Mendenhall",
    "case_name_full": "United States v. Mendenhall",
    "input_case_name": "United States v. Mendenhall",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-06-30",
    "year": 1980,
    "docket": "78-1821",
    "cluster_id": 110264,
    "lead_opinion_id": 9427929,
    "sibling_ids": [
      110264,
      9427929,
      9427930,
      9427931
    ],
    "absolute_url": "/opinion/110264/united-states-v-mendenhall/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "446 U.S. 544",
      "volume": "446",
      "reporter": "U.S.",
      "page": "544",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 1870",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1870",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "64 L. Ed. 2d 497",
        "volume": "64",
        "reporter": "L. Ed. 2d",
        "page": "497",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 102",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "102",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "446 U.S. 544",
        "volume": "446",
        "reporter": "U.S.",
        "page": "544",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 1870",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1870",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "64 L. Ed. 2d 497",
        "volume": "64",
        "reporter": "L. Ed. 2d",
        "page": "497",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 102",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "102",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "446 U.S. 544",
    "official_selection": {
      "court_class": "scotus",
      "selected": "446 U.S. 544",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-554",
      "page": null,
      "quote": "? ## Rule A person is seized only when a reasonable person would not feel free to leave.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-554a",
      "page": null,
      "quote": "Examples of circumstances that might indicate a seizure, even where the person did not attempt to leave, would be the threatening presence of several officers, the display of a weapon by an officer, some physical touching of the person of the citizen, or the use of language or tone of voice indicating that compliance with the officer's request might be compelled.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1980-05-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Mendenhall",
    "varies_by_point": false,
    "scope_note": "The 'free to leave' test was announced in Justice Stewart's opinion (joined on the seizure point only by Justice Rehnquist) but was later adopted by the full Court and is the governing standard.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Wright",
          "cluster_id": 10658752,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Louisiana v. K.B.",
          "cluster_id": 10581696,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Poulson v. Commonwealth",
          "cluster_id": 10375911,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Sorenson",
          "cluster_id": 4806437,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Evelyn",
          "cluster_id": 4786331,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane1_negative"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Royer",
          "cluster_id": 110890,
          "cite": [
            "75 L. Ed. 2d 229",
            "103 S. Ct. 1319",
            "460 U.S. 491",
            "1983 U.S. LEXIS 151",
            "51 U.S.L.W. 4293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sokolow",
          "cluster_id": 112239,
          "cite": [
            "104 L. Ed. 2d 1",
            "109 S. Ct. 1581",
            "490 U.S. 1",
            "1989 U.S. LEXIS 1694",
            "57 U.S.L.W. 4401"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harmelin v. Michigan",
          "cluster_id": 112646,
          "cite": [
            "115 L. Ed. 2d 836",
            "111 S. Ct. 2680",
            "501 U.S. 957",
            "1991 U.S. LEXIS 3816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Bostick",
          "cluster_id": 112631,
          "cite": [
            "115 L. Ed. 2d 389",
            "111 S. Ct. 2382",
            "501 U.S. 429",
            "1991 U.S. LEXIS 3625",
            "59 U.S.L.W. 4708",
            "91 Daily Journal DAR 7328",
            "91 Cal. Daily Op. Serv. 4671",
            "1991 WL 105224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tennessee v. Garner",
          "cluster_id": 111397,
          "cite": [
            "85 L. Ed. 2d 1",
            "105 S. Ct. 1694",
            "471 U.S. 1",
            "1985 U.S. LEXIS 195",
            "53 U.S.L.W. 4410"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Hodari D.",
          "cluster_id": 112579,
          "cite": [
            "113 L. Ed. 2d 690",
            "111 S. Ct. 1547",
            "499 U.S. 621",
            "1991 U.S. LEXIS 2397",
            "91 Cal. Daily Op. Serv. 2893",
            "59 U.S.L.W. 4335",
            "91 Daily Journal DAR 4665"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Place",
          "cluster_id": 110979,
          "cite": [
            "77 L. Ed. 2d 110",
            "103 S. Ct. 2637",
            "462 U.S. 696",
            "1983 U.S. LEXIS 74",
            "51 U.S.L.W. 4844"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kolender v. Lawson",
          "cluster_id": 110926,
          "cite": [
            "75 L. Ed. 2d 903",
            "103 S. Ct. 1855",
            "461 U.S. 352",
            "1983 U.S. LEXIS 159",
            "51 U.S.L.W. 4532"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jacobsen",
          "cluster_id": 111143,
          "cite": [
            "80 L. Ed. 2d 85",
            "104 S. Ct. 1652",
            "466 U.S. 109",
            "1984 U.S. LEXIS 53",
            "52 U.S.L.W. 4414"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stansbury v. California",
          "cluster_id": 117843,
          "cite": [
            "128 L. Ed. 2d 293",
            "114 S. Ct. 1526",
            "511 U.S. 318",
            "1994 U.S. LEXIS 3293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ohio v. Robinette",
          "cluster_id": 118066,
          "cite": [
            "136 L. Ed. 2d 347",
            "117 S. Ct. 417",
            "519 U.S. 33",
            "1996 U.S. LEXIS 6971"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. Delgado",
          "cluster_id": 111148,
          "cite": [
            "80 L. Ed. 2d 247",
            "104 S. Ct. 1758",
            "466 U.S. 210",
            "1984 U.S. LEXIS 57",
            "52 U.S.L.W. 4436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brendlin v. California",
          "cluster_id": 145712,
          "cite": [
            "168 L. Ed. 2d 132",
            "127 S. Ct. 2400",
            "551 U.S. 249",
            "2007 U.S. LEXIS 7897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Chesternut",
          "cluster_id": 112095,
          "cite": [
            "100 L. Ed. 2d 565",
            "108 S. Ct. 1975",
            "486 U.S. 567",
            "1988 U.S. LEXIS 2582",
            "56 U.S.L.W. 4558"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dowthitt v. State",
          "cluster_id": 1777832,
          "cite": [
            "931 S.W.2d 244",
            "1996 Tex. Crim. App. LEXIS 93",
            "1996 WL 347772"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "National Treasury Employees Union v. Von Raab",
          "cluster_id": 112220,
          "cite": [
            "103 L. Ed. 2d 685",
            "109 S. Ct. 1384",
            "489 U.S. 656",
            "1989 U.S. LEXIS 6033",
            "1989 CCH OSHD 28,589",
            "4 I.E.R. Cas. (BNA) 246",
            "57 U.S.L.W. 4338",
            "49 Empl. Prac. Dec. (CCH) 38,792"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reid v. Georgia",
          "cluster_id": 110336,
          "cite": [
            "65 L. Ed. 2d 890",
            "100 S. Ct. 2752",
            "448 U.S. 438",
            "1980 U.S. LEXIS 148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Drayton",
          "cluster_id": 121153,
          "cite": [
            "153 L. Ed. 2d 242",
            "122 S. Ct. 2105",
            "536 U.S. 194",
            "2002 U.S. LEXIS 4420"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Montoya De Hernandez",
          "cluster_id": 111509,
          "cite": [
            "87 L. Ed. 2d 381",
            "105 S. Ct. 3304",
            "473 U.S. 531",
            "1985 U.S. LEXIS 120",
            "53 U.S.L.W. 5048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McGee v. Commonwealth",
          "cluster_id": 1067400,
          "cite": [
            "487 S.E.2d 259",
            "25 Va. App. 193",
            "1997 Va. App. LEXIS 444"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110264 OR 9427929 OR 9427930 OR 9427931) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTg3MDgxNjAwMDAwJnM9NDc0NjIxMCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110264+OR+9427929+OR+9427930+OR+9427931%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110264 OR 9427929 OR 9427930 OR 9427931)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01Mjkmcz0xNjcwODU1JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110264+OR+9427929+OR+9427930+OR+9427931%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110264 OR 9427929 OR 9427930 OR 9427931)",
        "reviewed": 98,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 98,
        "triage_read": 3,
        "triage_snippet_classified": 95
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110264 OR 9427929 OR 9427930 OR 9427931)",
    "indexed_citing_opinions": 3716,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110264,
        "count": 3292,
        "count_source": "search"
      },
      {
        "opinion_id": 9427929,
        "count": 497,
        "count_source": "search"
      },
      {
        "opinion_id": 9427930,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427931,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6316,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-mendenhall.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNjk1Mzcmcz0xMDU5MzEzNyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110264+OR+9427929+OR+9427930+OR+9427931%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110264,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 101075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 108153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 108330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 109422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 109776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 269987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 344429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 345757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 365570,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 2364698,
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
    "date_created": "2026-07-06T01:37:11Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:37:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:37:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:42:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:37:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Mendenhall

```
<opinion type="majority">
<author id="b604-9">Mr. Justice Stewart</author>
<p id="Adm">announced the judgment of the Court and delivered an opinion, in which Mr. Justice Rehnquist joined.<footnotemark>†</footnotemark></p>
<p id="b604-10">The respondent was brought to trial in the United States District Court for the Eastern District of Michigan on a <page-number citation-index="1" label="547">*547</page-number>charge of possessing heroin with intent to distribute it. She moved to suppress the introduction at trial of the heroin as evidence against her on the ground that it had been acquired from her through an unconstitutional search and seizure by agents of the Drug Enforcement Administration (DEA). The District Court denied the respondent’s motion, and she was convicted after a trial upon stipulated facts. The Court of Appeals reversed, finding the search of the respondent’s person to have been unlawful. We granted certiorari to consider whether any right of the respondent guaranteed by the Fourth Amendment was violated in the circumstances presented by this case. <span class="citation multiple-matches"><a href="/c/U.%20S./444/822/">444 U. S. 822</a></span>.</p>
<p id="b605-5">I</p>
<p id="b605-6">At the hearing in the trial court on the respondent’s motion to suppress, it was established how the heroin she was charged with possessing had been obtained from her. The respondent arrived at the Detroit Metropolitan Airport on a commercial airline flight from Los Angeles early in the morning on February 10, 1976. As she disembarked from the airplane, she was observed by two agents of the DEA, who were present at the airport for the purpose of detecting unlawful traffic in narcotics. After observing the respondent’s conduct, which appeared to the agents to be characteristic of persons unlawfully carrying narcotics,<footnotemark>1</footnotemark> the agents approached her as she was walking through the concourse, identified themselves as federal <page-number citation-index="1" label="548">*548</page-number>agents, and asked to see her identification and airline ticket. The respondent produced her driver’s license, which was in the name of Sylvia Mendenhall, and, in answer to a question of one of the agents, stated that -she resided at the address appearing on the license. The airline ticket was issued in the name of “Annette Ford.” When asked why the ticket bore a name different from her own, the respondent stated that she “just felt like using that name.” In response to a further question, the respondent indicated that she had been in California only two days. Agent Anderson then specifically identified himself as a federal narcotics agent and, according to his testimony, the respondent “became quite shaken, extremely nervous. She had a hard time speaking.”</p>
<p id="b606-5">After returning the airline ticket and driver’s license to her, Agent Anderson asked the respondent if she would accompany him to the airport DEA office for further questions. She did so, although the record does not indicate a verbal response to the request. The office, which was located up one flight of stairs about 50 feet from where the respondent had first been approached, consisted of a reception area adjoined by three other rooms. At the office the agent asked the respondent if she would allow a search of her person and handbag and told her that she had the right to decline the search if she desired. She responded: “Go ahead.” She then handed Agent Anderson her purse, which contained a receipt for an airline ticket that had been issued to “F. Bush” three days earlier for a flight from Pittsburgh through Chicago to Los Angeles. The agent asked whether this was the ticket that she had used for her flight to California, and the respondent stated that it was.</p>
<p id="b606-6">A female police officer then arrived to conduct the search of the respondent’s person. She asked the agents if the respondent had consented to be searched. The agents said that she had, and the respondent followed the policewoman into a private room. There the policewoman again asked the respondent if she consented to the search, and the respondent <page-number citation-index="1" label="549">*549</page-number>replied that- she did. The policewoman explained that the search would require that the respondent remove her clothing. The respondent stated that she had a plane to catch and was assured by the policewoman that if she were carrying no narcotics, there would be no problem. The respondent then began to disrobe without further comment. As the respondent removed her clothing, she took from her undergarments two small packages, one of which appeared to contain heroin, and handed both to the policewoman. The agents then arrested the respondent for possessing heroin.</p>
<p id="b607-5">It was on the basis of this evidence that the District Court denied the respondent’s motion to suppress. The court concluded that the agents’ conduct in initially approaching the respondent and asking to see her ticket and identification was a permissible investigative stop under the standards of <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span>, and <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span>, finding that this conduct was based on specific and articulable facts that justified a suspicion of criminal activity. The court also found that the respondent had not been placed under arrest or otherwise detained when she was asked to accompany the agents to the DEA office, but had accompanied the agents “ ‘voluntarily in a spirit of apparent cooperation.’ ” It was the court’s view that no arrest occurred until after the heroin had been found. Finally, the trial court found that the respondent “gave her consent to the search [in the DEA office] and . . . such consent was freely and voluntarily given.”</p>
<p id="b607-6">The Court of Appeals reversed the respondent’s subsequent conviction, stating only that “the court concludes that this case is indistinguishable from <em>United States </em>v. <em>McCaleb,” </em><span class="citation" data-id="344429"><a href="/opinion/344429/united-states-v-robert-ross-mccaleb-and-brenda-page/" aria-description="Citation for case: United States v. Robert Ross McCaleb and Brenda Page">552 F. 2d 717</a></span> (CA6 1977).<footnotemark>2</footnotemark> In <em>McCaleb </em>the Court of Appeals had suppressed heroin seized by DEA agents at the Detroit Airport in circumstances substantially similar to those in the <page-number citation-index="1" label="550">*550</page-number>present case.<footnotemark>3</footnotemark> The Court of Appeals there disapproved the Government’s reliance on the so-called “drug courier profile,” and held that the agents could not reasonably have suspected criminal activity in that case, for the reason that “the activities of the [persons] observed by DEA agents, were consistent with innocent behavior,” <span class="citation" data-id="344429"><a href="/opinion/344429/united-states-v-robert-ross-mccaleb-and-brenda-page/#720" aria-description="Citation for case: United States v. Robert Ross McCaleb and Brenda Page"><em>id., </em>at 720</a></span>. The Court of Appeals further concluded in <em>McCaleb </em>that, even if the initial approach had been permissible, asking the suspects to accompany the agents to a private room for further questioning constituted an arrest requiring probable cause. Finally, the court in <em>McCaleb </em>held that the consent to the search in that case had not been voluntarily given, principally because it was the fruit of what the court believed to have been an unconstitutional detention.</p>
<p id="b608-5">On rehearing en banc of the present case, the Court of Appeals reaffirmed its original decision, stating simply that the respondent had not validly consented to the search “within the meaning of <em>[McCaleb].” </em><span class="citation" data-id="9465699"><a href="/opinion/365570/united-states-v-sylvia-l-mendenhall-and-david-a-camacho/#707" aria-description="Citation for case: United States v. Sylvia L. Mendenhall and David A. Camacho">596 F. 2d 706, 707</a></span>.</p>
<p id="b608-6">II</p>
<p id="b608-7">The Fourth Amendment provides that “the right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated. . . .” There is no question in this case that the respondent possessed this constitutional right of personal security as she walked through the Detroit Airport, for “the Fourth Amendment protects people, not places,” <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span>. Here the Government concedes that its agents had neither a warrant nor probable cause to believe that the respondent was carrying narcotics when <page-number citation-index="1" label="551">*551</page-number>the agents conducted a search of the respondent’s person. It is the Government’s position, however, that the search was conducted pursuant to the respondent’s consent,<footnotemark>4</footnotemark> and thus was excepted from the requirements of both a warrant and probable cause. See <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span>. Evidently, the Court of Appeals concluded that the respondent’s apparent consent to the search was in fact not voluntarily given and was in any event the product of earlier official conduct violative of the Fourth Amendment. We must first consider, therefore, whether such conduct occurred, either on the concourse or in the DEA office at the airport.</p>
<p id="b609-5">A</p>
<p id="b609-6">The Fourth Amendment’s requirement that searches and seizures be founded upon an objective justification, governs all seizures of the person, “including seizures that involve only a brief detention short of traditional arrest. <em>Davis </em>v. <em>Mississippi, </em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969); <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 16-19</a></span> (1968).” <em>United States </em>v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce"><em>Brignoni-Ponce, supra, </em>at 878</a></span>.<footnotemark>5</footnotemark> Accordingly, if the respondent was “seized” when the DEA <page-number citation-index="1" label="552">*552</page-number>agents approached her on the concourse and asked questions of her, the agents’ conduct in doing so was constitutional only if they reasonably suspected the respondent of wrongdoing. But “[o]bviously, not all personal intercourse between policemen and citizens involves 'seizures’ of persons. Only when the officer, by means of physical force or show of authority, has in some way restrained the liberty of a citizen may we conclude that a 'seizure’ has occurred.” <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 19, n. 16</a></span>.</p>
<p id="b610-5">The distinction between an intrusion amounting to a “seizure” of the person and an encounter that intrudes upon no constitutionally protected interest is illustrated by the facts of <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio</a></span>, </em>which the Court recounted as follows: “Officer McFadden approached the three men, identified himself as a police officer and asked for their names. . . . When the men 'mumbled something’ in response to his inquiries, Officer McFadden grabbed petitioner Terry, spun him around so that they were facing the other two, with Terry between McFadden and the others, and patted down the outside of his clothing.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#6" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 6-7</a></span>. Obviously the officer “seized” Terry and subjected him to a “search” when he took hold of him, spun him around, and patted down the outer surfaces of his clothing, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio"><em>id., </em>at 19</a></span>. What was not determined in that case, however, was that a seizure had taken place before the officer physically restrained Terry for purposes of searching his per<page-number citation-index="1" label="553">*553</page-number>son for weapons. The Court “assume [d] that up to that point no intrusion upon constitutionally protected rights had occurred.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 19, n. 16</a></span>. The Court’s assumption appears entirely correct in view of the fact, noted in the concurring opinion of Mr. Justice White, that “[t]here is nothing in the Constitution which prevents a policeman from addressing questions to anyone on the streets,” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#34" aria-description="Citation for case: Terry v. Ohio"><em>id., </em>at 34</a></span>. Police officers enjoy “the liberty (again, possessed by every citizen) to address questions to other persons,” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#31" aria-description="Citation for case: Terry v. Ohio"><em>id., </em>at 31, 32-33</a></span> (Harlan, J., concurring), although “ordinarily the person addressed has an equal right to ignore his interrogator and walk away.” <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ibid.</a></span></em></p>
<p id="b611-5">Similarly, the Court in <em>Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span>, a case decided the same day as <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio</a></span>, </em>indicated that not every encounter between a police officer and a citizen is an intrusion requiring an objective justification. In that case, a police officer, before conducting what was later found to have been an unlawful search, approached Sibron in a restaurant and told him to come outside, which Sibron did. The Court had no occasion to decide whether there was a “seizure” of Sibron inside the restaurant antecedent to the seizure that accompanied the search. The record was “barren of any indication whether Sibron accompanied [the officer] outside in submission to a show of force or authority which left him no choice, or <em>whether he went voluntarily in a spirit of apparent cooperation </em>with the officer’s investigation.” 392 U. S., at 63 (emphasis added). Plainly, in the latter event, there was no seizure until the police officer in some way demonstrably curtailed Sibron’s liberty.</p>
<p id="b611-6">We adhere to the view that a person is “seized” only when, by means of physical force or a show of authority, his freedom of movement is restrained. Only when such restraint is imposed is there any foundation whatever for invoking constitutional safeguards. The purpose of the Fourth Amendment is not to eliminate all contact between the police and the citizenry, but “to prevent arbitrary and oppressive inter<page-number citation-index="1" label="554">*554</page-number>ference by enforcement officials with the privacy and personal security of individuals.” <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#554" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 554</a></span>. As long as the person to whom questions are put remains free to disregard the questions and walk away, there has been no intrusion upon that person’s liberty or privacy as would under the Constitution require some particularized and objective justification.</p>
<p id="b612-5">Moreover, characterizing every street encounter between a citizen and the police as a “seizure,” while not enhancing any interest secured by the Fourth Amendment, would impose wholly unrealistic restrictions upon a wide variety, of legitimate law enforcement practices. The Court has on other occasions referred to the acknowledged need for police questioning as a tool in the effective enforcement of the criminal laws. “Without such investigation, those who were innocent might be falsely accused, those who were guilty might wholly escape prosecution, and many crimes would go unsolved. In short, the security of all would be diminished. <em>Haynes </em>v. <em>Washington, </em><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#515" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503, 515</a></span>.” <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#225" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., at 225</a></span>.</p>
<p id="b612-6">We conclude that a person has been “seized” within the meaning of the Fourth Amendment only if, in view of all of the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave.<footnotemark>6</footnotemark> Examples of circumstances that might indicate a seizure, even where the person did not attempt to leave, would be the threatening presence of several officers, the display of a weapon by an officer, some physical touching of the person of the citizen, or the use of language or tone of voice indicating that compliance with the officer’s request might be compelled. See <em>Terry </em>v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio"><em>Ohio, supra, </em>at 19, n. 16</a></span>; <em>Dunaway </em>v. <page-number citation-index="1" label="555">*555</page-number><em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#207" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 207</a></span>, and n. 6; 3 W. LaFave, Search and Seizure 53-55 (1978). In the absence of some such evidence, otherwise inoffensive contact between a member of the public and the police cannot, as a matter of law, amount to a seizure of that person.</p>
<p id="b613-5">On the facts of this case, no “seizure” of the respondent occurred. The events took place in the public concourse. The agents wore no uniforms and displayed no weapons. They did not summon the respondent to their presence, but instead approached her and identified themselves as federal agents. They requested, but did not demand to see the respondent’s identification and ticket. Such conduct, without more, did not amount to an intrusion upon any constitutionally protected interest. The respondent was not seized simply by reason of the fact that the agents approached her, asked her if she would show them her ticket and identification, and posed to her a few questions. Nor was it enough to establish a seizure that the person asking the questions was a law enforcement official. See <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#31" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 31, 32-33</a></span> (Harlan, J., concurring). See also ALI, Model Code of Pre-Arraignment Procedure § 110.1 (1) and commentary, at 257-261 (1975). In short, nothing in the record suggests that the respondent had any objective reason to believe that she was not free to end the conversation in the concourse and proceed on her way, and for that reason we conclude that the agents’ initial approach to her was not a seizure.</p>
<p id="b613-6">Our conclusion that no seizure occurred is not affected the fact that the respondent was not expressly told by the agents that she was free to decline to cooperate with their inquiry, for the voluntariness of her responses does not depend upon her having been so informed. See <em>Schneckloth </em>v. <em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Bustamonte, supra.</a></span> </em>We also reject the argument that the only inference to be drawn from the fact that the respondent acted in a manner so contrary to her self-interest is that she was compelled to answer the agents’ questions. It may happen that a person makes statements to law enforcement <page-number citation-index="1" label="556">*556</page-number>officials that he later regrets, but the issue in such cases is not whether the statement was self-protective, but rather whether it was made voluntarily.</p>
<p id="b614-5">The Court’s decision last Term in <em>Brown </em>v. <em>Texas, </em><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">443 U. S. 47</a></span>, on which the respondent relies, is not apposite. It could not have been plainer under the circumstances there presented that Brown was forcibly detained by the officers. In that case, two police officers approached Brown in an alley, and asked him to identify himself and to explain his reason for being there. Brown “refused to identify himself and angrily asserted that the officers had no right to stop him,” <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#49" aria-description="Citation for case: Brown v. Texas"><em>id., </em>at 49</a></span>. Up to this point there was no seizure. But after continuing to protest the officers’ power to interrogate him, Brown was first frisked, and then arrested for violation of a state statute making it a criminal offense for a person to refuse to give his name and address to an officer “who has lawfully stopped him and requested the information.” The Court simply held in that case that because the officers had no reason to suspect Brown of wrongdoing, there was no basis for detaining him, and therefore no permissible foundation for applying the state statute in the circumstances there presented. <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#52" aria-description="Citation for case: Brown v. Texas"><em>Id., </em>at 52-53</a></span>.</p>
<p id="b614-6">The Court’s decisions involving investigatory stops of automobiles do not point in any different direction. In <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span>, the Court held that a roving patrol of law enforcement officers could stop motorists in the general area of an international border for brief inquiry into their residence status only if the officers reasonably suspected that the vehicle might contain aliens who were illegally in the country. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce"><em>Id., </em>at 881-882</a></span>. The Government did not contend in that case that the persons whose automobiles were detained were not seized. Indeed, the Government acknowledged that the occupants of a detained vehicle were required to respond to the officers’ questions and on some occasions to produce documents evidencing their eligibility to be in the United States. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#880" aria-description="Citation for case: United States v. Brignoni-Ponce"><em>Id., </em>at 880</a></span>. Moreover, stopping or diverting an automobile in transit, with the attendant opportunity for <page-number citation-index="1" label="557">*557</page-number>a visual inspection of areas of the passenger compartment not otherwise observable, is materially more intrusive than a question put to a passing pedestrian, and the fact that the former amounts to a seizure tells very little about the constitutional status of the latter. See also <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648</a></span>; <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 556-559</a></span>.</p>
<p id="b615-4">B</p>
<p id="b615-5">Although we have concluded that the initial encounter between the DEA agents and the respondent on the concourse at the Detroit Airport did not constitute an unlawful seizure, it is still arguable that the respondent’s Fourth Amendment protections were violated when she went from the concourse to the DEA office. Such a violation might in turn infect the subsequent search of the respondent’s person.</p>
<p id="b615-6">The District Court specifically found that the respondent accompanied the agents to the office <em>“ </em>'voluntarily in a spirit of apparent cooperation,’ ” quoting <em>Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#63" aria-description="Citation for case: Sibron v. New York">392 U. S., at 63</a></span>. Notwithstanding this determination by the trial court, the Court of Appeals evidently concluded that the agents’ request that the respondent accompany them converted the situation into an arrest requiring probable cause in order to be found lawful. But because the trial court’s finding was sustained by the record, the Court of Appeals was mistaken in substituting for that finding its view of the evidence. See <em>Jackson </em>v. <em>United States, </em>122 U. S. App. D. C. 324, <span class="citation" data-id="9451218"><a href="/opinion/269987/henry-w-jackson-v-united-states/" aria-description="Citation for case: Henry W. Jackson v. United States">353 F. 2d 862</a></span> (1965).</p>
<p id="b615-7">The question whether the respondent’s consent to accompany the agents was in fact voluntary or was the product of duress or coercion, express or implied, is to be determined by the totality of all the circumstances, <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#227" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., at 227</a></span>, and is a matter which the Government has the burden of proving. <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#222" aria-description="Citation for case: Schneckloth v. Bustamonte"><em>Id., </em>at 222</a></span>, citing <em>Bumper </em>v. <em>North Carolina, </em><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#548" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543, 548</a></span>. The respondent herself did not testify at the hearing. The Government’s evidence showed that the respondent was not told that she <page-number citation-index="1" label="558">*558</page-number>had to go to the office, but was simply asked if she would accompany the officers. There were neither threats nor any show of force. The respondent had been questioned only briefly, and her ticket and identification were returned to her before she was asked to accompany the officers.</p>
<p id="b616-4">On the other hand, it is argued that the incident would reasonably have appeared coercive to the respondent, who was 22 years old and had not been graduated from high school. It is additionally suggested that the respondent, a female and a Negro, may have felt unusually threatened by the officers, who were white males. While these factors were not irrelevant, see <em>Schneckloth </em>v. <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte"><em>Bustamonte, supra, </em>at 226</a></span>, neither were they decisive, and the totality of the evidence in this case was plainly adequate to support the District Court’s finding that the respondent voluntarily consented to accompany the officers to the DEA office.</p>
<p id="b616-5">C</p>
<p id="b616-6">Because the search of the respondent’s person was not preceded by an impermissible seizure of her person, it cannot be contended that her apparent consent to the subsequent search was infected by an unlawful detention. There remains to be considered whether the respondent’s consent to the search was for any other reason invalid. The District Court explicitly credited the officers’ testimony and found that the “consent was freely and voluntarily given,” citing <em>Schneckloth </em>v. <em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Bustamonte, supra.</a></span> </em>There was more than enough evidence in this case to sustain that view. First, we note that the respondent, who was 22 years old and had an llth-grade education, was plainly capable of a knowing consent. Second, it is especially significant that the respondent was twice expressly told that she was free to decline to consent to the search, and only thereafter explicitly consented to it. Although the Constitution does not require “proof of knowledge of a right to refuse as the <em>sine qua non </em>of an effective consent to a search,” <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#234" aria-description="Citation for case: Schneckloth v. Bustamonte"><em>id., </em>at 234</a></span> (footnote omitted), such knowledge <page-number citation-index="1" label="559">*559</page-number>was highly relevant to the determination that there had been consent. And, perhaps more important for present purposes, the fact that the officers themselves informed the respondent that she was free to withhold her consent substantially lessened the probability that their conduct could reasonably have appeared to her to be coercive.</p>
<p id="b617-5">Counsel for the respondent has argued that she did in fact resist the search, relying principally on the testimony that when she- was told that the search would require the removal of her clothing, she stated to the female police officer that “she had a plane to catch.” But the trial court was entitled to view the statement as simply an expression of concern that the search be conducted quickly. The respondent had twice unequivocally indicated her consent to the search, and when assured by the police officer that there would be no problem-, if nothing were turned up by the search, she began to undress without further comment.</p>
<p id="b617-6">Counsel for the respondent has also argued that because she was within the DEA office when she consented to the search, her consent may have resulted from the inherently coercive nature of those surroundings. But in view of the District Court’s finding that the respondent’s presence in the office was voluntary, the fact that she was there is little or no evidence that she was in any way coerced. And in response to the argument that the respondent would not voluntarily have consented to a search that was likely to disclose the narcotics that she carried, we repeat that the question is not whether the respondent acted in her ultimate self-interest, but whether she acted voluntarily.<footnotemark>7</footnotemark></p>
<p id="b617-7">Ill</p>
<p id="b617-8">We conclude that the District Court’s determination that the respondent consented to the search of her person “freely <page-number citation-index="1" label="560">*560</page-number>and voluntarily” was sustained by the evidence and that the Court of Appeals was, therefore, in error in setting it aside. Accordingly, the judgment of the Court of Appeals is reversed, and the case is remanded to that court for further proceedings.</p>
<p id="b618-5">
<em>It is so ordered.</em>
</p>
<footnote label="†">
<p id="b604-13">The Chief Justice, Mr. Justice Blachmun, and Mr. Justice Powell also join all but Part II-A of this opinion.</p>
</footnote>
<footnote label="1">
<p id="b605-7"> The agent testified that 'the respondent’s behavior fit the so-called “drug courier profile” — an informally compiled abstract of characteristics thought typical of persons carrying illicit drugs. In this case the agents thought it relevant that (1) the respondent was arriving on a flight from Los Angeles, a city believed by the agents to be the place of origin for much of the heroin brought to Detroit; (2) the respondent was the last person to leave the plane, “appeared to be very nervous,” and “completely scanned the whole area where [the agents] were standing”; (3) after leaving the plane the respondent proceeded past the baggage area without claiming any luggage; and (4) the respondent changed airlines for her flight out of Detroit.</p>
</footnote>
<footnote label="2">
<p id="b607-7"> The opinion of the Court of Appeals and the opinion of the District Court are both unreported.</p>
</footnote>
<footnote label="3">
<p id="b608-8"> The <em>McCaleb </em>case, however, involved a circumstance not present here. Although the persons searched in that case were advised of their right to decline to give consent to the search of their luggage, they were also informed that if they refused they would be detained while the agents sought a search warrant. <span class="citation" data-id="344429"><a href="/opinion/344429/united-states-v-robert-ross-mccaleb-and-brenda-page/#719" aria-description="Citation for case: United States v. Robert Ross McCaleb and Brenda Page">552 F. 2d, at 719</a></span>. The Court of Appeals in this case evidently considered the distinction irrelevant.</p>
</footnote>
<footnote label="4">
<p id="b609-7"> The Government has made several alternative arguments in this ease.</p>
</footnote>
<footnote label="5">
<p id="b609-8"> In the District Court and the Court of Appeals, the parties evidently assumed that the respondent was seized when she was approached on the airport concourse and was asked if she would show her identification and airline ticket. In its brief on the merits and oral argument in this Court, however, the Government has argued that no seizure occurred, and the respondent has joined the argument. While the Court ordinarily does not consider matters neither raised before nor decided by the courts below, see <em>Adickes </em>v. <em>Kress &amp; Co., </em><span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#147" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U. S. 144, 147, n. 2</a></span>, it has done so in exceptional circumstances. See <em>Youakim </em>v. <em>Miller, </em><span class="citation" data-id="109422"><a href="/opinion/109422/youakim-v-miller/#234" aria-description="Citation for case: Youakim v. Miller">425 U. S. 231, 234</a></span>; <em>Duignan </em>v. <em>United States, </em><span class="citation" data-id="101075"><a href="/opinion/101075/duignan-v-united-states/#200" aria-description="Citation for case: Duignan v. United States">274 U. S. 195, 200</a></span>. We consider the Government’s contention that there was no seizure of the respondent in this case, because the contrary assumption, embraced by the trial court and the Court of Appeals, rests on a serious misapprehension of federal constitutional law. And because the determination of the question is essential to the correct disposition of the other issues in the case, we shall treat it as “fairly comprised” by the questions presented in the petition for cer-tiorari. This Court’s Rule 23 (1) (c). See <em>Procunier </em>v. <em>Navarette, </em><span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/#559" aria-description="Citation for case: Procunier v. Navarette">434 <page-number citation-index="1" label="552">*552</page-number>U. S. 555, 559-560, n. 6</a></span>; <em>Blonder-Tongue Laboratories, Inc. </em>v. <em>University of Illinois Foundation, </em><span class="citation" data-id="108330"><a href="/opinion/108330/blonder-tongue-laboratories-inc-v-university-of-illinois-foundation/#320" aria-description="Citation for case: Blonder-Tongue Laboratories, Inc. v. University of...">402 U. S. 313, 320-321, n. 6</a></span>.</p>
<p id="AgI">The evidentiary record in the trial court is adequate to permit consideration of the contention. The material facts are not disputed. A major question throughout the controversy has been whether the respondent was at any time detained by the DEA agents. Counsel for the respondent has argued that she was arrested while proceeding through the concourse. The trial court and the Court of Appeals characterized the incident as an “investigatory stop.” But the correctness of the legal characterization of the facts appearing in the record is a matter for this Court to determine. See <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 226</a></span>; <em>Bumper </em>v. <em>North Carolina, </em><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#548" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543, 548-550</a></span>.</p>
</footnote>
<footnote label="6">
<p id="b612-7"> We agree with the District Court that the subjective intention of the DEA agent in this case to detain the respondent, had she attempted to leave, is irrelevant except insofar as that may have been conveyed to the respondent.</p>
</footnote>
<footnote label="7">
<p id="b617-9"> It is arguable that the respondent may have thought she was acting in her self-interest, by voluntarily cooperating with the officers in the hope of receiving more lenient treatment.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Mendez.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Mendez
type: case
citation: "103 F.4th 1303 (2024)"
parallel_cite: ""
neutral_cite: ""
court: 7th Cir.
court_level: coa
circuit: ca7
year: 2024
date_decided: 2024-06-10
docket: 23-1460
authority_weight: "Binding in-circuit — 7th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/9524074/united-states-v-marcos-mendez/"
  cluster_id: 9524074
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Mendez
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Border Searches]]"
    role: Key
related:
  - "[[Border Searches]]"
  - "[[United States v. Kolsuz]]"
  - "[[Riley v. California]]"
  - "[[Carpenter v. United States]]"
tags:
  - case
  - fourth-amendment
  - border-search
  - forensic-search
  - manual-search
  - cell-phone
  - digital-privacy
  - seventh-circuit
holding: "The Seventh Circuit affirmed, joining its sister circuits to hold that a border search of a cell phone or other electronic device requires neither a warrant nor probable cause, and that a brief, manual search of a traveler's phone at the border (here, scrolling the photo gallery at O'Hare) is a routine border search requiring no individualized suspicion; because that valid manual search revealed child pornography, the court did not need to decide whether the later forensic extraction required reasonable suspicion, since the agents had ample suspicion by then."
---

# United States v. Mendez

*103 F.4th 1303 (7th Cir. 2024)* (No. 23-1460) · U.S. Court of Appeals for the Seventh Circuit · **Binding in-circuit — 7th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 9524074 → opinion 9990687 (103 F.4th 1303, decided 2024-06-10, St. Eve, J.); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Just before midnight on February 20, 2016, Marcos Mendez landed at O'Hare International Airport — a functional equivalent of the border — after a trip to Ecuador, traveling alone with a personal phone, a work phone, and a work iPad. Customs and Border Protection had issued a child-pornography "lookout" for Mendez based on a 2010 arrest and 2011 conviction, a prior inspection, his return from a country classified as a child-trafficking source, and his fitting the profile of a single adult male traveling alone. CBP Officer Callison pulled Mendez aside for secondary inspection; within thirty minutes Mendez handed over his phone and passcode. Callison manually unlocked it, scrolled the camera roll, and found thousands of pornographic images including apparent child pornography, then opened a protected "iSafe" app with more. He next conducted a roughly two-hour "forensic" DOMEX extraction that revealed additional images. Officers seized the phone but released Mendez, who remotely wiped it and fled to Mexico; he was later extradited. Charged with producing, transporting, and possessing child pornography, Mendez moved to suppress; the district court denied the motion (finding reasonable suspicion under *Wanjiku*), and he pled guilty to one production count (300 months), preserving the appeal.

## Issue
Whether the border searches of Mendez's phone — the manual scroll of the photo gallery and the subsequent forensic extraction — required a warrant, probable cause, or at least reasonable suspicion in light of *[[Riley v. California]]* and *[[Carpenter v. United States]]*.

## Rule
At the border and its functional equivalents (like an international airport), the border-search exception permits routine searches without a warrant, probable cause, or any individualized suspicion. Joining the uniform view of its sister circuits, the court held that device searches at the border require neither a warrant nor probable cause, and that a brief, manual search of a phone is routine: "We therefore agree with the consensus among circuits that brief, manual searches of a traveler's electronic device are 'routine' border searches requiring no individualized suspicion." — 103 F.4th 1303, slip op. at 13. ^pin-op13

## Application
The manual search — Officer Callison scrolling the camera roll of a phone handed over at an international airport — was a routine border search requiring no individualized suspicion, so it was valid regardless of whether the CBP lookout independently supplied reasonable suspicion. *[[Riley v. California|Riley]]* ([[Search Incident to Arrest|search incident to arrest]]) and *[[Carpenter v. United States|Carpenter]]* (cell-site location data) did not displace the border-search exception for that manual search. Because the valid manual search already revealed child pornography, the court did not need to resolve whether the more intrusive **forensic** DOMEX extraction required reasonable suspicion — an issue on which the circuits split — because by the time of that forensic search the agents "had that and more" in the way of suspicion.

## Conclusion
**Affirmed.** Judge St. Eve wrote for the panel (Hamilton, Brennan, and St. Eve, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Mendez* places the Seventh Circuit within the **cross-circuit consensus** that a brief, manual device search at the border is routine and needs no suspicion, and that no border device search requires a warrant or probable cause. Critically, it **leaves open** the forensic-search standard — the live split where the Fourth Circuit's *[[United States v. Kolsuz|Kolsuz]]* and the Ninth's *[[United States v. Cano|Cano]]* require reasonable suspicion while the Eleventh's *[[United States v. Touset|Touset]]* requires none. Teach the manual/forensic distinction and never state a settled nationwide device rule.

## Appears on
- [[Border Searches]] — *Key*

## Sources
- [*United States v. Mendez*, 103 F.4th 1303 (7th Cir. 2024)](https://www.courtlistener.com/opinion/9524074/united-states-v-marcos-mendez/) — pinpoint: slip op. at 13 (routine-manual-search-requires-no-suspicion holding; the CL opinion text carries the court's internal slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ac2b41327de9de75", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Mendez"}, "payload": {"all": [{"cite": "103 F.4th 1303", "page": "1303", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "103"}], "display": "103 F.4th 1303", "official": {"cite": "103 F.4th 1303", "page": "1303", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "103"}, "official_selection_present": true, "record_id": "United States v. Mendez"}}
{"assertion_id": "2f853958c5c5c389", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Mendez"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Mendez", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Mendez

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Mendez",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Marcos Mendez",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Mendez",
    "court": "7th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca7",
    "state": null,
    "date_decided": "2024-06-10",
    "year": 2024,
    "docket": "23-1460",
    "cluster_id": 9524074,
    "lead_opinion_id": 9990687,
    "sibling_ids": [],
    "absolute_url": "/opinion/9524074/united-states-v-marcos-mendez/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "103 F.4th 1303",
      "volume": "103",
      "reporter": "F.4th",
      "page": "1303",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "103 F.4th 1303",
        "volume": "103",
        "reporter": "F.4th",
        "page": "1303",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "103 F.4th 1303",
    "official_selection": {
      "court_class": "coa",
      "selected": "103 F.4th 1303",
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
    "date_created": "2026-07-07T01:39:58Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:40:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:40:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:40:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:40:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-mendez--9524074",
      "to_record_id": "United States v. Mendez",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Mendez

```
                              In the

    United States Court of Appeals
                For the Seventh Circuit
                    ____________________
No. 23-1460
UNITED STATES OF AMERICA,
                                                  Plaintiﬀ-Appellee,
                                v.

MARCOS MENDEZ,
                                              Defendant-Appellant.
                    ____________________

        Appeal from the United States District Court for the
          Northern District of Illinois, Eastern Division.
           No. 16-cr-163 — Mary M. Rowland, Judge.
                    ____________________

    ARGUED DECEMBER 5, 2023 — DECIDED JUNE 10, 2024
               ____________________

   Before HAMILTON, BRENNAN, and ST. EVE, Circuit Judges.
    ST. EVE, Circuit Judge. Marcos Mendez was passing
through customs at O’Hare International Airport after a trip
abroad when a customs agent pulled him aside for inspection,
unlocked and scrolled through his cell phone, and found child
pornography in the photo gallery. Customs agents then
seized the phone, downloaded its contents, and discovered
additional illicit images and videos of children.
2                                                     No. 23-1460

    After the district court denied Mendez’s motion to sup-
press this evidence, Mendez pled guilty to producing child
pornography but preserved this appeal of the district court’s
suppression-motion ruling. He now argues that the searches
of his phone, in light of the Supreme Court’s decisions in Riley
v. California, 573 U.S. 373 (2014), and Carpenter v. United States,
585 U.S. 296 (2018), required a warrant, probable cause, or at
least reasonable suspicion.
    The “longstanding recognition that searches at our bor-
ders without probable cause and without a warrant are none-
theless ‘reasonable’ has a history as old as the Fourth Amend-
ment itself.” United States v. Ramsey, 431 U.S. 606, 619 (1977).
That history leads us to join the uniform view of our sister
circuits to hold that searches of electronics at the border—like
any other border search—do not require a warrant or proba-
ble cause, and that the kind of routine, manual search of the
phone initially performed here requires no individualized
suspicion. We aﬃrm.
                         I. Background
A. Factual Background
   Just shy of midnight on February 20, 2016, Marcos Mendez
landed at O’Hare International Airport following a trip to Ec-
uador. He was traveling alone. Along with his baggage, Men-
dez carried with him three electronic devices: a personal cell
phone, a work phone, and a work iPad.
    Customs and Border Protection (“CBP”) had issued a
child-pornography-related “lookout” for Mendez based on
his arrest record and prior travel history. Mendez had a 2010
arrest relating to indecent solicitation of a child and child por-
nography, leading to a 2011 conviction for endangering the
No. 23-1460                                                   3

life or health of a child. Additionally, CBP previously had in-
spected Mendez in 2014 after he returned from Mexico. Dur-
ing that inspection, he claimed to have been kidnapped,
robbed of his electronic devices, and told to leave the country.
And on this particular trip, Mendez was returning from Ecua-
dor, which CBP oﬃcers classiﬁed as a potential child-traﬃck-
ing source country. Mendez also ﬁt the proﬁle for child-por-
nography oﬀenders: a single adult male traveling alone.
    Together, this information prompted CBP Investigating
Oﬃcer Richard Callison to pull Mendez aside for secondary
inspection after his arrival at O’Hare. Within the ﬁrst thirty
minutes of the inspection, Mendez gave Callison his cell
phone and its passcode. Callison manually unlocked the
phone and navigated to its camera roll. There he found thou-
sands of pornographic images, including what appeared to be
child pornography. Using the phone’s passcode, Callison also
opened a protected application called “iSafe,” where he dis-
covered more illicit images.
    Callison then moved Mendez to a private location, where
he conducted a more extensive, “forensic” examination of
Mendez’s devices. CBP agents used a data extraction technol-
ogy called “DOMEX” (Document and Media Exploitation) to
download a copy of the devices’ photos and videos. The fo-
rensic examination took about two hours and revealed more
child pornography.
    Oﬃcers seized Mendez’s cell phone but released Mendez,
who, in the days after his arrest, remotely wiped the contents
of his phone and traveled by car into Mexico with his mother.
Meanwhile, a Homeland Security Investigations (“HSI”) team
extracted the metadata—creation dates, geolocation infor-
mation, and so on—from the ﬁles that had earlier been
4                                                 No. 23-1460

downloaded from Mendez’s cell phone. That data revealed
that several of the child pornography images were taken near
Mendez’s residence in Rosemont, Illinois.
B. Procedural Background
    A grand jury indicted Mendez on two counts of producing
child pornography, in violation of 18 U.S.C. § 2251(a), one
count of transporting child pornography, in violation of 18
U.S.C. § 2252A(a)(1), and one count of possessing child por-
nography, in violation of 18 U.S.C. § 2252A(a)(5)(B). He was
extradited to the United States in January 2020.
    Mendez moved to suppress the evidence found on his cell
phone, arguing the searches violated the Fourth Amendment
because they were unsupported by either a probable-cause
supported warrant or reasonable suspicion. After an eviden-
tiary hearing in which Oﬃcer Callison and other investigating
oﬃcers testiﬁed, the district court denied the motion. Relying
in large part on our decision in United States v. Wanjiku, 919
F.3d 472 (7th Cir. 2019), the district court held that the
searches did not violate the Fourth Amendment because cus-
toms agents had reasonable suspicion by the time they began
looking through Mendez’s phone.
   Mendez pled guilty to one count of producing child por-
nography but preserved his right to appeal the district court’s
suppression ruling. He received a 300-month sentence, fol-
lowed by a ten-year term of supervised release. We now con-
sider that preserved issue, reviewing the district court’s ﬁnd-
ings of fact for clear error and questions of law de novo. See
United States v. Ostrum, 99 F.4th 999, 1004 (7th Cir. 2024).
No. 23-1460                                                                 5

                               II. Analysis
   The Fourth Amendment commands that searches and sei-
zures be reasonable. U.S. Const. amend. IV. Ordinarily, “[i]n
the absence of a warrant, a search is reasonable only if it falls
within a speciﬁc exception to the warrant requirement.” Riley,
573 U.S. at 382.
   One such exception is the border search exception. “Con-
gress, since the beginning of our Government, ‘has granted
the Executive plenary authority to conduct routine searches
and seizures at the border, without probable cause or a war-
rant, in order to regulate the collection of duties and to pre-
vent the introduction of contraband into this country.’” 1
United States v. Flores-Montano, 541 U.S. 149, 153 (2004) (quot-
ing United States v. Montoya de Hernandez, 473 U.S. 531, 537
(1985)). The government’s unquestionable authority to search
persons and eﬀects at the border is rooted in “the long-stand-
ing right of the sovereign to protect itself by stopping and ex-
amining persons and property crossing into this country.”
Ramsey, 431 U.S. at 616; see also id. at 619 (“Historically such
broad powers have been necessary to prevent smuggling and
to prevent prohibited articles from entry.”); Flores–Montano,
541 U.S. at 152 (noting that the border exception rests on the
government interest in “preventing the entry of unwanted
persons and eﬀects”). The “Fourth Amendment balance be-
tween the interests of the Government and the privacy right


    1 We treat the customs area of O’Hare International Airport as “the

functional equivalent of an international border for the purpose of inspect-
ing persons and articles arriving on international ﬂights.” Wanjiku, 919
F.3d at 480 (citing United States v. Yang, 286 F.3d 940, 944 (7th Cir. 2002));
see also Almeida-Sanchez v. United States, 413 U.S. 266, 273 (1973).
6                                                       No. 23-1460

of the individual is … struck much more favorably to the Gov-
ernment at the border.” Montoya de Hernandez, 473 U.S. at 540.
When the government acts under its “inherent authority to
protect … its territorial integrity,” its interest is “at its zenith.”
Flores-Montano, 541 U.S. at 152–53. In contrast, a traveler’s ex-
pectation of privacy at the border is simply “less.” Montoya de
Hernandez, 473 U.S. at 539.
    Accordingly, border searches have long been exempted
from warrant and probable cause requirements, and ordinar-
ily “are reasonable simply by virtue of the fact that they occur
at the border.” Flores-Montano, 541 U.S. at 152–53 (quoting
Ramsey, 431 U.S. at 616). “Routine” searches of people and ef-
fects at the border—which have included examining the con-
tents of a person’s purse, wallet, or pockets, United States v.
Carter, 592 F.2d 402 (7th Cir. 1979), opening mail, see Ramsey,
431 U.S. at 620, and disassembling and reassembling a vehi-
cle’s fuel tank, see Flores-Montano, 541 U.S. at 155—are “per se
reasonable” and require no particularized suspicion at all.
Yang, 286 F.3d at 944 (citing Ramsey, 431 U.S. at 616); see also
Montoya de Hernandez, 473 U.S. at 538 (“Routine searches of
the persons and eﬀects of entrants are not subject to any re-
quirement of reasonable suspicion, probable cause, or war-
rant.”); United States v. Johnson, 991 F.2d 1287, 1291 (7th Cir.
1993).
    Even highly intrusive, so-called “non-routine” border
searches need only reasonable suspicion. See Montoya de Her-
nandez, 473 U.S. at 541. But the Supreme Court has recognized
this “non-routine” category only in searches of a suspect’s
person. It held, for example, that a 16-hour detention for mon-
itored bowel movement of a person suspected of “smuggling
contraband in her alimentary canal” requires reasonable
No. 23-1460                                                   7

suspicion given the personal dignity and privacy interests at
stake. Id. at 541. And in this circuit, “we have confronted bor-
der searches and seizures that we characterized as arguably
non-routine”—including pat downs, partial strip searches,
visual body cavity searches, and the dismantling of luggage—
and have applied the reasonable suspicion standard. Wanjiku,
919 F.3d at 482–83 (emphasis added); see also Yang, 286 F.3d at
944, 949; Kaniﬀ v. United States, 351 F.3d 780, 784–85 (7th Cir.
2003); Johnson, 991 F.2d at 1291–94.
    Routine or otherwise, searches at the border “never” re-
quire a warrant or probable cause. Ramsey, 431 U.S. at 619
(“There has never been any additional requirement that the
reasonableness of a border search depended on the existence
of probable cause.”). At most, border searches require reason-
able suspicion. See Wanjiku, 919 F.3d at 481; United States v.
Molina-Isidoro, 884 F.3d 287, 291 (5th Cir. 2018) (“For border
searches both routine and not, no case has required a war-
rant.”). In more than 200 years of border search precedent,
neither the Supreme Court nor we have ever found a border
search unconstitutional.
    Mendez argues that Riley and Carpenter upended that
precedent by recognizing that cell phones fundamentally dif-
fer from other types of personal eﬀects. See Riley, 573 U.S. at
393; Carpenter, 585 U.S. at 318. Yet our caselaw highlights why
neither case supports altering the long-settled rule exempting
border searches from warrant and probable cause require-
ments: Riley and Carpenter had nothing to do with the border
context. See Wanjiku, 919 F.3d at 484; United States v. Wood, 16
F.4th 529, 533 (7th Cir. 2021) (“Given the context-speciﬁc
8                                                              No. 23-1460

nature of the Fourth Amendment, Riley is not readily transfer-
able to scenarios other than the one it addressed.”). 2
     Rather, Riley involved the search incident to arrest excep-
tion and “carefully tailored its analysis to that context.” Wood,
16 F.4th at 533. What is unreasonable after arrest may be per-
fectly reasonable at customs, as Riley itself anticipated. See Ri-
ley, 573 U.S. at 401–02 (“[O]ther case-speciﬁc exceptions may
still justify a warrantless search of a particular phone.”); see
also New Jersey v. T.L.O., 469 U.S. 325, 337 (1985) (Fourth
Amendment reasonableness “depends on the context within
which a search takes place.”). A border search is


    2 Wanjiku and a later decision, United States v. Skaggs, 25 F.4th 494 (7th

Cir. 2022), resolved the identical issue of electronic device searches at cus-
toms under the Fourth Amendment’s good faith exception to the warrant
requirement. “[N]o court,” we observed in Wanjiku, “had ever required
more than reasonable suspicion for any search at the border.” 919 F.3d at
479. And because we found that law enforcement had reasonable suspi-
cion to search the defendant’s phone, “[g]iven the state of the law at the
time of the[] searches,” we concluded that law enforcement had “an ob-
jectively good faith belief that their conduct did not violate the Fourth
Amendment.” Id. at 485–86. While we left the merits of the Fourth Amend-
ment issues open in those cases, we go on to reach those merits issues here
to provide clarity to law enforcement and the public on the burgeoning
practice of electronic device searches. See Molina-Isidoro, 884 F.3d at 293
(Costa, J., specially concurring) (“Courts should resist the temptation to
frequently rest their Fourth Amendment decisions on the safe haven of the
good-faith exception, lest the courts fail to give law enforcement and the
public the guidance needed to regulate their frequent interactions.”);
United States v. Bosyk, 933 F.3d 319, 332 n.10 (4th Cir. 2019) (“[W]hen a
Fourth Amendment case presents a novel question of law whose resolu-
tion is necessary to guide future action by law enforcement oﬃcers and
magistrates, there is suﬃcient reason for [a court] to decide the violation
issue before turning to the good-faith question.” (alterations in original)
(quoting Illinois v. Gates, 462 U.S. 213, 264 (1983) (White, J., concurring))).
No. 23-1460                                                                9

fundamentally diﬀerent from a search incident to arrest, not
least because “the Fourth Amendment’s balance of reasona-
bleness is qualitatively diﬀerent at the international border,”
where the government’s interest in protecting its territorial in-
tegrity is at its peak and travelers’ expectations of privacy are
diminished. Montoya de Hernandez, 473 U.S. at 538; cf. United
States v. 12 200-Ft. Reels of Super 8MM. Film, 413 U.S. 123, 125
(1973) (“Import restrictions and searches of persons or pack-
ages at the national borders rest on diﬀerent considerations
and diﬀerent rules of constitutional law from domestic regu-
lations.”). Underlying the Court’s decision in Riley was the
fact that neither of the search incident to arrest exception’s
twin concerns—preventing harm to oﬃcers and destruction
of evidence—“ha[d] much force with respect to digital con-
tent on cell phones.” Riley, 573 U.S. at 386. Here, in contrast,
we agree with the First Circuit that “given the volume of trav-
elers passing through our nation’s borders, warrantless elec-
tronic device searches are essential to the border search ex-
ception’s purpose of ensuring that the executive branch can
adequately protect the border.” 3 Alasaad v. Mayorkas, 988 F.3d
8, 17 (1st Cir. 2021).
   While Mendez argues that cell phone searches are unteth-
ered to the border search doctrine’s justiﬁcations, this case


    3 We have twice declined to extend Riley beyond the search incident

to arrest exception: to parolee searches in Wood, 16 F.4th at 533, and to
consent searches in United States v. Thurman, 889 F.3d 356, 366 n.9 (7th Cir.
2018) (ﬁnding in the consent-search context that “Riley d[id] not aﬀect our
holding” because “[a]lthough the Court discussed the unique nature of
modern cell phones as unparalleled repositories for personal information,
it did not address the consent-based exception to the warrant require-
ment”).
10                                                            No. 23-1460

illustrates that cell phones can contain the contraband the bor-
der search doctrine means to intercept: here, digital contra-
band in the form of child pornography. See United States v.
Cano, 934 F.3d 1002, 1014 (9th Cir. 2019) (“The best example
[of digital contraband] is child pornography.”). The govern-
ment’s interest in detecting child pornography at the border
is just as strong as its interest in intercepting ﬁrearms, narcot-
ics, or any other prohibited item. 4 See United States v. Touset,
890 F.3d 1227, 1235 (11th Cir. 2018) (“‘[Digital]’ child pornog-
raphy poses the same exact ‘risk’ of unlawful entry at the bor-
der as its physical counterpart.”). That digital contraband like
child pornography can pass into the country electronically or
be accessed remotely does little to diminish the government’s
interest in preventing its physical entry into the country. See


     4 Although the scope of a search conducted under an exception to the

warrant requirement must be “commensurate with its purposes,” Arizona
v. Gant, 556 U.S. 332, 339 (2009), the Ninth Circuit is the only circuit to
cabin the border search exception to detecting contraband itself. Compare
Cano, 934 F.3d at 1019 (holding that “border oﬃcials are limited to search-
ing for contraband only”), with United States v. Levy, 803 F.3d 120, 124 (2d
Cir. 2015) (noting that CBP oﬃcers “have the authority to search and re-
view a traveler’s documents and other items at the border when they rea-
sonably suspect that the traveler is engaged in criminal activity, even if the
crime falls outside the primary scope of their oﬃcial duties.”), and United
States v. Xiang, 67 F.4th 895, 900 (8th Cir. 2023) (adopting the Second Cir-
cuit’s “more sensibl[e]” position), and Alasaad, 988 F.3d at 20 (“[T]he bor-
der search exception’s purpose is not limited to interdicting contraband;
it serves to bar entry to those ‘who may bring anything harmful into this
country.’” (emphasis in original) (quoting Montoya de Hernandez, 473 U.S.
at 544)), and United States v. Aigbekaen, 943 F.3d 713, 721 (4th Cir. 2019)
(ﬁnding the purposes of the exception to be “protecting national security,
collecting duties, blocking the entry of unwanted persons, or disrupting
eﬀorts to export or import contraband”).
No. 23-1460                                                    11

id. (“If anything, the advent of sophisticated technological
means for concealing contraband only heightens the need of
the government to search property at the border.”); United
States v. Thirty-Seven Photographs, 402 U.S. 363, 376 (1971)
(“Customs oﬃcers characteristically inspect luggage and
their power to do so is not questioned … ; it is an old practice
and is intimately associated with excluding illegal articles
from the country.”). And although it was not the case here, a
border search of a cell phone could also facilitate the doc-
trine’s goal of “reasonably requiring one entering the country
to identify himself as entitled to come in.” Carroll v. United
States, 267 U.S. 132, 154 (1925).
    No circuit court has read Riley to require more than rea-
sonable suspicion to support even the most intrusive electron-
ics search at the border. See United States v. Castillo, 70 F.4th
894, 897–98 (5th Cir. 2023) (“[W]hen it comes to manual cell
phone searches at the border, our sister circuits have uni-
formly held that Riley does not require either a warrant or rea-
sonable suspicion.”); Molina-Isidoro, 884 F.3d at 293 (5th Cir.
2018); Xiang, 67 F.4th at 900 (8th Cir. 2023) (“Riley involved a
diﬀerent Fourth Amendment exception, searches incident to
arrest. No Circuit has held that the government must obtain a
warrant to conduct a routine border search of electronic de-
vices.”); Alasaad, 988 F.3d at 17 (1st Cir. 2021) (“Riley does not
command a warrant requirement for border searches of elec-
tronic devices nor does the logic behind Riley compel us to
impose one.”); Cano, 934 F.3d at 1015 (9th Cir. 2019); Touset,
890 F.3d at 1234 (11th Cir. 2018) (“Although the Supreme
Court stressed in Riley that the search of a cell phone risks a
signiﬁcant intrusion on privacy, our [caselaw makes] clear
that Riley, which involved the search-incident-to-arrest excep-
tion, does not apply to searches at the border.”); United States
12                                                   No. 23-1460

v. Vergara, 884 F.3d 1309, 1312–13 (11th Cir. 2018) (“Border
searches have long been excepted from warrant and probable
cause requirements, and the holding of Riley does not change
this rule.”); United States v. Kolsuz, 890 F.3d 133, 147 (4th Cir.
2018). We join our sister circuits to hold that a border search
of a cell phone or other electronic device requires neither a
warrant nor probable cause.
    The question remains whether the agent’s manual search
of Mendez’s phone—scrolling through its photo gallery—was
a routine search permissible without any suspicion or a “non-
routine” search requiring reasonable suspicion. Mendez con-
tends that because electronic devices carry potentially vast
troves of sensitive and personal information, we should treat
all electronic device searches as intrusive border searches re-
quiring at least reasonable suspicion. Riley itself involved a
manual phone search and no doubt indicates that all cell
phone searches are intrusive to some degree, but the privacy
concerns such searches implicate “are nevertheless tempered
by the fact that the searches are taking place at the border.”
Alasaad, 988 F.3d at 18. Moreover, manual electronic searches
at the border are typically “brief procedure[s]”—here, around
thirty minutes—practically limited in intrusiveness by the
fact that the customs agent cannot download and peruse the
phone’s entire contents. Instead, they must physically scroll
through the device, making it less likely for an agent to tap
into the revealing nooks and crannies of the phone’s
metadata, encrypted ﬁles, or deleted contents. Flores-Montano,
541 U.S. at 155; compare United States v. Cotterman, 709 F.3d
952, 960 (9th Cir. 2013) (en banc) (pre-Riley decision ﬁnding
the legitimacy of a suspicion-less “quick look and unintru-
sive” manual laptop search “not in doubt”), with Kolsuz, 890
F.3d at 136 (requiring reasonable suspicion for a month-long,
No. 23-1460                                                  13

oﬀ-site forensic analysis that yielded a nearly 900-page report
cataloguing the phone’s data).
    We therefore agree with the consensus among circuits that
brief, manual searches of a traveler’s electronic device are
“routine” border searches requiring no individualized suspi-
cion. See Castillo, 70 F.4th at 897–98 (“[W]hen it comes to man-
ual cell phone searches at the border, our sister circuits have
uniformly held that Riley does not require either a warrant or
reasonable suspicion.”); Alasaad, 988 F.3d at 19 (“[B]asic bor-
der searches [of electronic devices] are routine searches and
need not be supported by reasonable suspicion.”); Cano, 934
F.3d at 1016 (“[M]anual searches of cell phones at the border
are reasonable without individualized suspicion.”); Touset,
890 F.3d at 1233; Kolsuz, 890 F.3d at 146 n.5 (describing United
States v. Ickes, 393 F.3d 501 (4th Cir. 2005), as “treat[ing] a
[basic] search of a computer as a routine border search, requir-
ing no individualized suspicion”).
    The only point of divergence among the circuits is whether
more intrusive, forensic electronic device searches require in-
dividualized suspicion. Compare Touset, 890 F.3d at 1231 (no
suspicion required for forensic electronics search), with Cano,
934 F.3d at 1016 (reasonable suspicion required). We need not
resolve this issue today because this case does not require it.
The valid manual search of Mendez’s phone revealed child
pornography. So, even if the extensive forensic searches that
followed required reasonable suspicion, customs agents had
that and more once they found illicit images and videos of
children on Mendez’s phone during the routine search.
                                                      AFFIRMED

```

---

## GROUP: _overhaul2/lake/cases/United States v. Mendoza.json  (`lake-record`, 1 assertions)

### content_page

```
---
title: United States v. Mendoza
type: case
citation: "No. 25-1154, slip op. (3d Cir. 2026)"
parallel_cite: ""
neutral_cite: ""
court: 3d Cir.
court_level: coa
circuit: ca3
year: 2026
date_decided: 2026-01-08
docket: 25-1154
authority_weight: "Binding in-circuit — 3d Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/10771114/united-states-v-ryan-mendoza/"
  cluster_id: 10771114
  opinion_id: null
  identity_checked: false
lake:
  record_id: United States v. Mendoza
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: Key
related:
  - "[[Standing to Challenge a Search]]"
  - "[[Katz v. United States]]"
tags:
  - case
  - fourth-amendment
  - standing
  - reasonable-expectation-of-privacy
  - hotel-room
  - checkout
  - third-circuit
holding: "A hotel guest's reasonable expectation of privacy in his room ends when his rental period lapses and possession reverts to the hotel; because police searched the room roughly five hours after the noon checkout time — after the guest had failed to check out, his keycard had been deactivated, and the room had been marked vacant — Mendoza lacked a legitimate expectation of privacy and therefore had no standing to challenge the warrantless search."
aliases:
  - United States v. Mendoza
  - "United States v. Mendoza (3d Cir. 2026)"
  - United States v. Ryan Mendoza
---

# United States v. Mendoza

*No. 25-1154, slip op. (3d Cir. 2026)* · U.S. Court of Appeals for the Third Circuit · **Binding in-circuit — 3d Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10771114 → precedential opinion 11237699 (Ambro, J.; No. 25-1154, decided Jan. 8, 2026). Rule quote string-matched to the CL opinion text 2026-07-07; slip-style pin (precedential 3d Cir. slip; no F.4th reporter cite assigned yet — S2 A3). S9 promotes. -->

## Background
Ryan Mendoza checked into a Pittsburgh hotel for a two-night stay ending February 25, with a posted noon checkout and keycards set to deactivate two hours after checkout. By noon on the departure day he had not checked out, so the hotel placed his room on a "due-out" list. A manager's check found personal items but no luggage; a later check turned up a backpack of white-powder packages, and staff called police. Officers arrived around 5:20 p.m. — some five hours after checkout — confirmed with the manager that the room was vacant and possession had reverted to the hotel, and searched it without a warrant. Mendoza, arrested that night, moved to suppress; the district court denied the motion for lack of a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]].

## Issue
Whether Mendoza retained a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the hotel room — and thus [[Standing to Challenge a Search|standing to challenge]] its search — several hours after the checkout time had passed.

## Rule
[[Standing to Challenge a Search|Fourth Amendment standing]] turns on whether the person "had 'a legitimate expectation of privacy in the invaded place.'" A guest's privacy interest in a rented room is tied to the rental period; once the period ends and control returns to the hotel, that interest dissolves. Applying this rule, the court held: "Five hours after checkout time, any expectation of privacy Mendoza had was not objectively reasonable." — slip op. at 2. ^pin-slip2

## Application
By the time officers entered, checkout had long passed, Mendoza had not extended his stay or notified the front desk, his keycard was set to deactivate, his balance would be charged, and the hotel had marked the room vacant and taken possession. Whatever expectation of privacy he might have retained briefly after noon was no longer objectively reasonable five hours later. Lacking a legitimate expectation of privacy in the room, Mendoza had no standing to contest the warrantless search, and the district court properly denied suppression.

## Conclusion
**Affirmed.** Judge Ambro wrote for the panel (Restrepo, McKee, Ambro, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Mendoza* is a clean precedential illustration of the threshold standing inquiry (*[[Standing to Challenge a Search]]*): the *[[Katz v. United States|Katz]]* reasonable-expectation-of-privacy question is answered against a guest whose rental period has expired and whose room has reverted to the hotel — no privacy interest, no standing to suppress.

## Appears on
- [[Standing to Challenge a Search]] — *Key*

## Sources
- [*United States v. Ryan Mendoza*, No. 25-1154, slip op. (3d Cir. 2026)](https://www.courtlistener.com/opinion/10771114/united-states-v-ryan-mendoza/) — pinpoint: slip op. at 2 (no reasonable expectation of privacy in a hotel room five hours after checkout). Rule quote string-matched to the CL opinion text 2026-07-07. Precedential 3d Cir. slip; no F.4th cite assigned yet (S2 A3 slip precedent).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4556e8ba912d9985", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Mendoza"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Mendoza", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Mendoza

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Mendoza",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Ryan Mendoza",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Mendoza",
    "court": "3d Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca3",
    "state": null,
    "date_decided": "2026-01-08",
    "year": 2026,
    "docket": "25-1154",
    "cluster_id": 10771114,
    "lead_opinion_id": 11237699,
    "sibling_ids": [],
    "absolute_url": "/opinion/10771114/united-states-v-ryan-mendoza/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
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
      "reason": "no_official_class_citation"
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "W9 RE-STAMP after pre-W5 re-key (prior stamp was on cluster 10131439). United States v. Ryan Mendoza, 3d Cir. PRECEDENTIAL slip No. 25-1154, decided 2026-01-08 (hotel-checkout REP). CL cluster 10771114 Published, citations[] empty (live-verified 2026-07-07); no F.4th cite assigned yet.",
      "legs": [
        {
          "source": "Court PDF",
          "url": "https://www.govinfo.gov/content/pkg/USCOURTS-ca3-25-01154/pdf/USCOURTS-ca3-25-01154-0.pdf",
          "cite": "No. 25-1154 (3d Cir.) PRECEDENTIAL, filed 2026-01-08"
        },
        {
          "source": "CourtListener",
          "url": "https://www.courtlistener.com/opinion/10771114/united-states-v-ryan-mendoza/",
          "cite": "cluster 10771114 Published, citations[] empty"
        }
      ]
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
    "date_created": "2026-07-07T18:21:27Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:21:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:21:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:21:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:21:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-mendoza--10771114",
      "to_record_id": "United States v. Mendoza",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Mendoza

```
                                       PRECEDENTIAL

       UNITED STATES COURT OF APPEALS
            FOR THE THIRD CIRCUIT
                 ____________

                     No. 25-1154
                    ____________

          UNITED STATES OF AMERICA

                           v.

                 RYAN MENDOZA,

                                               Appellant


      Appeal from the United States District Court
       for the Western District of Pennsylvania
        (District Court No. 2:21-cr-00503-001)
      District Judge: Honorable Arthur J. Schwab

     Submitted Under Third Circuit L.A.R. 34.1(a)
               on November 13, 2025

Before: RESTREPO, McKEE, and AMBRO, Circuit Judges

            (Opinion filed: January 8, 2026)
Ryan R. Smith
Suite 820
310 Grant Street
Pittsburgh, PA 15219

             Counsel for Appellant

Adam N. Hallowell
Laura S. Irwin
Office of United States Attorney
700 Grant Street
Suite 4000
Pittsburgh, PA 15219

             Counsel for Appellee



                OPINION OF THE COURT


AMBRO, Circuit Judge

       Ryan Mendoza moved to suppress evidence the
Government obtained in its search of his hotel room after
checkout time. The District Court denied his motion, holding
that he failed to show he had a reasonable expectation of
privacy in that hotel room. We agree. Five hours after
checkout time, any expectation of privacy Mendoza had was
not objectively reasonable.




                             2
                    I.      BACKGROUND

       Around 1:00 a.m. on February 24, 2021, Ryan Mendoza
checked into a Pittsburgh hotel for a two-night stay—the night
spanning February 23 to 24 and the night spanning February
24 to 25. He obtained a receipt stating that his departure date
was February 25. On the back of each guest room door, and
usually on a plaque behind the front desk, the hotel posted signs
stating that checkout time was noon. The hotel usually set
guests’ key cards to deactivate two hours after checkout time.

         The hotel permitted guests to check out either by going
to the front desk or simply by walking out of the hotel without
notifying anyone. By noon on February 25, Mendoza had not
gone to the front desk to check out. So the hotel’s system
added him to a “due-out” list. Hotel staff check rooms on the
list to ensure they have been vacated. When the hotel manager
checked Mendoza’s room around 2:00 p.m., he saw a number
of personal items but no luggage. He marked the room as a
checkout, but found the situation odd. A few hours later, the
manager returned for another check and discovered a backpack
containing wrapped packages of white powder. He told a staff
member to call the police.

        They arrived around 5:20 p.m. Hotel staff informed the
officers that they had found a bag containing drugs in the room
of a “walk-out” guest whose stay had ended at noon that day.
Police entered the hotel room without a warrant, accompanied
by the hotel manager. In the room, the officers “double-
check[ed]” with the manager that the guest had “checked out.”
Supp. App. 4, at 8:35–8:50. The manager appeared to
understand the question as asking whether the guest physically
checked out at the front desk, so the officer sought to clarify
that the room was “vacant,” the guest “ha[d] nothing to do with




                               3
this room anymore,” possession of the room had reverted to the
hotel, and the guest would not be allowed back in if he tried to
return. Id., at 8:50–9:35. The manager confirmed this
understanding. The police also asked the manager to alert them
if the guest returned.

       Around 10:00 p.m., Mendoza returned to the hotel. He
was arrested with room keycards and the receipt in his pocket.

       Mendoza moved to suppress the fruits of the hotel room
search under the Fourth Amendment, arguing he had not
vacated the room when the police searched it warrantlessly. At
the suppression hearing, the hotel manager testified that guests
could check out either by going to the front desk or by walking
out. After the designated checkout time, walk-out guests’
balances are charged to their credit cards on file, their room
keys are deactivated, and their rooms are considered vacant.

      The District Court denied Mendoza’s motion.           He
appeals.

     II.    JURISDICTION AND STANDARD OF REVIEW

       The District Court had jurisdiction under 18 U.S.C.
§ 3231, and we have jurisdiction under 28 U.S.C. § 1291. “We
review a district court’s order denying a motion to suppress
under a mixed standard of review. We review findings of fact
for clear error, but exercise plenary review over legal
determinations.” United States v. Dyer, 54 F.4th 155, 158 (3d
Cir. 2022) (citation omitted). And “[b]ecause the District
Court denied the suppression motion, we view the facts in the
light most favorable to the Government.” Id. (quoting United
States v. Garner, 961 F.3d 264, 269 (3d Cir. 2020)).




                               4
                        III.    ANALYSIS

       As an initial step in determining whether a search
violated the Fourth Amendment, we ask whether the person
claiming its protection had “a legitimate expectation of privacy
in the invaded place.” United States v. Montalvo-Flores, 81
F.4th 339, 342 (3d Cir. 2023) (quoting Rakas v. Illinois, 439
U.S. 128, 143 (1978)). This inquiry involves a “subjective”
prong—whether the defendant actually expected privacy in
that place—and an “objective” prong—whether any such
expectation was one that society is prepared to recognize as
reasonable.1 Id. (citing Katz v. United States, 389 U.S. 347,
361 (1967) (Harlan, J., concurring)). Mendoza “bears the
burden of proving each element.” Id. at 343. If he fails his
objective burden, he cannot claim Fourth Amendment relief
even if he did have a subjective expectation of privacy.

        Under the Fourth Amendment, a hotel guest’s privacy
interest in a hotel room is the same as that of a tenant in a rented
house. Stoner v. California, 376 U.S. 483, 490 (1964). But
that interest dissipates when the guest vacates the room. Abel
v. United States, 362 U.S. 217, 241 (1960). “The hotel then
ha[s] the exclusive right to its possession,” and hotel
management may consent to a search. Id.

      There is no precedential authority in our Circuit
governing whether hotel guests maintain an objectively

1
  Courts often refer to this doctrine as a Fourth Amendment
standing inquiry because it requires defendants to demonstrate
a privacy interest in a searched place before seeking relief
under the Fourth Amendment. See Montalvo-Flores, 81 F.4th
at 342 & n.4. However, this inquiry is not jurisdictional and
should not be confused with Article III standing. Id. at n.4.




                                 5
reasonable expectation of privacy in their rooms after checkout
time if they have not taken some affirmative action to check
out. However, the many circuits to have confronted the issue
unanimously hold that the expectation lapses after checkout
time. See, e.g., United States v. Parizo, 514 F.2d 52, 55 (2d
Cir. 1975); United States v. Jackson, 585 F.2d 653, 658 (4th
Cir. 1978); United States v. Ramirez, 810 F.2d 1338, 1341 (5th
Cir. 1987); United States v. Lanier, 636 F.3d 228, 232 (6th Cir.
2011); United States v. Akin, 562 F.2d 459, 464 (7th Cir. 1977);
United States v. Larson, 760 F.2d 852, 855 (8th Cir. 1985);
United States v. Dorais, 241 F.3d 1124, 1128–30 (9th Cir.
2001); United States v. Croft, 429 F.2d 884, 887 (10th Cir.
1970); United States v. Ross, 964 F.3d 1034, 1043 (11th Cir.
2020).

        That rule makes sense. Checkout time is an appropriate
marker for the end of a guest’s possession of a room and the
resumption of possession by the hotel. Once checkout time has
passed, hotel staff may—indeed, must—enter a room to clean
it and prepare it for the next guest, who might be arriving just
a short time later.2 Leftover items can be removed by a hotel
after checkout time. Keycards can be deactivated, terminating
the guest’s access to the room. And many hotels, like the one
here, do not require guests to check out affirmatively at the
front desk; instead, they simply charge the credit card on file


2
  That hotel staff may enter a room to maintain it during a
guest’s stay does not defeat the guest’s reasonable expectation
of privacy from police intrusion. See United States v. Jeffers,
342 U.S. 48, 51 (1951). But hotel staff acquire complete
discretion to enter the room after checkout time—for example,
they may reasonably ignore a “Do Not Disturb” doorhanger
left by a guest after checkout. See Ross, 964 F.3d at 1043.




                               6
after checkout time. Accordingly, guests can lose their privacy
interests in a hotel room even without taking affirmative action
to check out.

        To argue otherwise, Mendoza points to testimony from
the hotel manager that “people come in and they think they
have the room for 24 hours.” App. 71. On the basis of this
testimony, Mendoza contends it was objectively reasonable for
him to believe he had the room for a full 48 hours after
checking in for a two-night stay. That argument fails. As a
matter of societal expectation, most hotel guests understand
that the checkout time is a fixed time of day that does not
change based on the time they checked in. Travelers receive
this information in many ways, including signage, receipts, and
the typical check-in colloquy at the front desk. Here, the
manager testified that the hotel had signs about the checkout
time posted in multiple locations. And Mendoza himself
received a receipt stating that his departure date was February
25, not February 26 as it would have been if he had the room
for 48 hours.

       Because this search happened five hours after checkout
time, and there were neither communications between
Mendoza and the hotel regarding a late checkout nor any other
potentially ambiguous circumstances, it does not raise a close
question. A future case nonetheless might. Does the
reasonable expectation of privacy disappear immediately at
checkout time, or might there be a “grace period” for stragglers
who remain slightly overtime? If there should be a grace
period, does it vary based on the patterns and practices at that
particular hotel, or the hotel’s communications with that
particular guest? Circuits disagree on these questions, and we
need not weigh in here. Compare United States v. Kitchens,
114 F.3d 29, 32 (4th Cir. 1997) (allowing guest to retain




                               7
legitimate expectation of privacy after checkout time if hotel
has pattern or practice that would make the expectation
reasonable), and Lanier, 636 F.3d at 232 (same), and Dorais,
241 F.3d at 1129 (same), and United States v. Owens, 782 F.2d
146, 150 (10th Cir. 1986) (same), with Ross, 964 F.3d at 1043
n.6 (expressly rejecting such an exception in favor of “clear
Fourth Amendment rules”).

       Instead, it is sufficient to say that any subjective
expectation of privacy Mendoza had in a hotel room five hours
after checkout time was not one that society is prepared to
recognize as reasonable. Lacking objective reasonableness, his
expectation of privacy cannot support a Fourth Amendment
claim.

                *      *      *      *      *

       To demonstrate that a search violated his rights under
the Fourth Amendment, Mendoza must first show that the
place searched was one in which he maintained a legitimate
expectation of privacy. An expectation of privacy is legitimate
only if it is objectively reasonable. Mendoza’s expectation of
privacy in his former hotel room, five hours after checkout
time, was not. As such, the police’s search of that room did
not violate his Fourth Amendment rights.

      We therefore affirm the District Court’s denial of the
motion to suppress.




                              8

```

---
