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

## GROUP: _overhaul2/lake/cases/united-states-v-chatrie--10881683.json  (`lake-record`, 1 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7f56612abf04debf", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-chatrie--10881683"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-chatrie--10881683", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-chatrie--10881683

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-chatrie--10881683",
  "stub": true,
  "status": "folded-alias",
  "identity": {
    "case_name": "Chatrie v. United States",
    "case_name_short": "Chatrie",
    "case_name_full": "",
    "input_case_name": "United States v. Chatrie",
    "court": "4th Cir. en banc, 136 F.4th 100",
    "court_id": null,
    "court_level": null,
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": null,
    "docket": null,
    "cluster_id": 10881683,
    "lead_opinion_id": null,
    "sibling_ids": [],
    "absolute_url": "/opinion/10881683/chatrie-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": false,
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
      "court_class": "state",
      "selected": null,
      "reason": "no_official_class_citation"
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
    "date_created": "2026-07-06T05:51:46Z",
    "date_modified": "2026-07-07T01:43:35Z",
    "warnings": [
      "folded-alias: subsumed into Chatrie v. United States (packet-A Group-2); see _manifest.json folded_into + journal s6-dedupe-pointer"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:51:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:51:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:51:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:51:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

---

## GROUP: _overhaul2/lake/cases/united-states-v-cook--3165557.json  (`lake-record`, 1 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8e152f1d14025160", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-cook--3165557"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-cook--3165557", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-cook--3165557

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-cook--3165557",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "United States v. Oshan Cook",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Cook",
    "court": "U.S. Court of Appeals, 9th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": null,
    "year": 2015,
    "docket": null,
    "cluster_id": 3165557,
    "lead_opinion_id": 3165557,
    "sibling_ids": [],
    "absolute_url": "/opinion/3165557/united-states-v-oshan-cook/",
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
    "date_created": "2026-07-06T13:14:06Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:14:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:14:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:14:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:14:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — united-states-v-cook--3165557

```
                    FOR PUBLICATION

     UNITED STATES COURT OF APPEALS
          FOR THE NINTH CIRCUIT


 UNITED STATES OF AMERICA,                       No. 13-10233
                  Plaintiff-Appellee,
                                                    D.C. No.
                     v.                          3:10-cr-00376-
                                                     JSW-3
 OSHAN COOK,
                   Defendant-Appellant.          ORDER AND
                                                  AMENDED
                                                   OPINION

        Appeal from the United States District Court
           for the Northern District of California
         Jeffrey S. White, District Judge, Presiding

                   Argued and Submitted
        January 13, 2015—San Francisco, California

                  Filed August 13, 2015
                Amended December 24, 2015

  Before: Richard R. Clifton and Jacqueline H. Nguyen,
 Circuit Judges and Jed S. Rakoff, * Senior District Judge.


 *
   The Honorable Jed S. Rakoff, Senior District Judge for the U.S.
District Court for the Southern District of New York, sitting by
designation.
2                    UNITED STATES V. COOK

                             Order;
                    Opinion by Judge Nguyen


                          SUMMARY **


                          Criminal Law

    Affirming convictions for conspiracy to possess with
intent to distribute MDMA and possession with intent to
distribute MDMA and LSD, the panel held that a search of
the defendant’s backpack did not violate his Fourth
Amendment rights.

     The panel held that the district court did not err in
denying the defendant’s motion to suppress evidence seized
from his backpack because the brief, cursory search of the
backpack for weapons was incident to a lawful arrest. In
addition, the district court did not abuse its discretion in
failing to hold an evidentiary hearing on the motion to
suppress.

    The panel also held that any Confrontation Clause
violation in allowing law enforcement agents to testify about
an identification of the defendant as the drug supplier was
harmless.




    **
    This summary constitutes no part of the opinion of the court. It has
been prepared by court staff for the convenience of the reader.
                  UNITED STATES V. COOK                      3

                         COUNSEL

David J. Pullman, San Rafael, California, for Defendant-
Appellant.

Owen P. Martikan (argued), Assistant United States
Attorney; Melinda Haag, United States Attorney; Barbara J.
Valliere, Chief, Appellate Division, United States
Attorney’s Office, San Francisco, California, for Plaintiff-
Appellee.


                          ORDER
    The opinion filed on August 13, 2015 and published at
797 F.3d 713 is hereby withdrawn and replaced by the
amended opinion filed concurrently with this order. With
these amendments, Judges Clifton, Nguyen, and Rakoff
have voted to deny the petition for panel rehearing, Judges
Clifton and Nguyen have voted to deny the petition for
rehearing en banc, and Judge Rakoff has so recommended.
The full court has been advised of the petition for rehearing
en banc, and no judge requested a vote on whether to rehear
the matter en banc. Fed. R. App. P. 35. The petitions for
panel rehearing and rehearing en banc are denied. No
further petitions for panel rehearing or rehearing en banc will
be entertained.



                         OPINION
NGUYEN, Circuit Judge:
    Oshan Cook appeals his convictions for conspiracy to
possess with intent to distribute MDMA (also known as
ecstasy or Molly) and possession with intent to distribute
4                UNITED STATES V. COOK

MDMA and LSD. Cook mainly challenges the denial of his
motions to suppress the evidence seized from his backpack,
arguing that the search violated his Fourth Amendment
rights. We conclude, however, that the brief, cursory search
of Cook’s backpack for weapons was valid incident to a
lawful arrest, and thus the district court properly denied
Cook’s motions. Because we also reject Cook’s remaining
challenges, we affirm.
                             I
                             A
    Working with an informant, undercover agents from the
Drug Enforcement Administration arranged to buy MDMA
from Yuri Lambert and James Edmonds. On the morning of
April 22, 2010, about thirty minutes before the scheduled
sale, agents were surveilling Lambert’s house on 63rd Street
in Oakland, California, when they saw Cook carrying a
backpack into the house. The agents concluded that Cook
likely dropped something off while inside the house because,
when he left a short time later, his backpack appeared less
full and lighter. About fifteen minutes after Cook left the
house, Lambert and Edmonds also came out of the same
house and headed to the location where the drug deal was to
take place. After Edmonds showed undercover Special
Agent Jay Dial the MDMA that he intended to sell, both
Lambert and Edmonds were arrested. During a post-arrest
interview, Edmonds identified Cook as his supplier, and said
that he had been dealing drugs with Cook “on and off for
five years.”
   The agents then took Edmonds back to Lambert’s house
on 63rd Street, where they found two firearms. At the
agents’ direction, Edmonds placed a monitored call to Cook.
When Edmonds told Cook that the sale had gone through,
Cook responded, “Hallelujah. Okay, I’ll see you soon.”
                 UNITED STATES V. COOK                     5

About fifteen minutes later, Cook arrived at the 63rd Street
residence, and when he got out of his car, he wore the same
backpack that the agents had observed on him during their
surveillance. As Cook approached the front porch, the
agents ordered him to the ground at gunpoint. While they
were placing handcuffs on him, Task Force Officer Robert
Knight came onto the scene. By this time, a crowd had
gathered, and even though there were six law enforcement
agents at the scene—three near Cook and three by Cook’s
car—they were concerned that additional, unidentified
coconspirators or others might interfere if they continued to
attract attention. Thus, the agents wanted to move
immediately out of the area.
    While Cook was still on the ground and within one or
two minutes of his arrest, Officer Knight picked up the
backpack, which was right next to Cook, and conducted a
twenty or thirty-second cursory search for weapons or
contraband. Finding no weapons, the agents quickly moved
Cook and the backpack to a more secluded restaurant
parking lot a few blocks away. There, Officer Knight and
Special Agent Dial did a more thorough search of the
backpack. During this second search, they found ziplock
bags containing MDMA, LSD, marijuana, two mobile
phones, and a laptop. The purity level of the MDMA found
in Cook’s backpack matched that of the MDMA seized from
Edmonds at the drug buy.
                             B
    Cook was indicted for conspiracy to possess with intent
to distribute MDMA, possession with intent to distribute
MDMA, and possession with intent to distribute more than
10 grams of LSD, in violation of 21 U.S.C. §§ 846,
841(a)(1), 841(b)(1)(C), 841(b)(1)(A)(v).
6                 UNITED STATES V. COOK

    Prior to trial, on September 9, 2011, Cook filed a motion
to suppress the evidence from his backpack. In support of
his motion, Cook submitted a declaration, stating that during
the few minutes that he was face down on the ground, he did
not see anyone open or search his backpack. In opposition,
the government submitted a declaration from Officer Knight,
stating that, while Cook was still on the ground, he
“immediately conducted a quick search of [the backpack] to
make sure that there were no destructive devices or other
items that might pose an immediate danger.” The
government also argued in its opposition papers that because
Cook was face down on the ground, he “was in no position
to have personal knowledge of when and how the search was
completed.” Cook filed a reply brief, but rather than dispute
that the initial search occurred, he conceded “that he [did]
not know when the search occurred.” Instead, Cook’s reply
brief focused only on his legal arguments for suppression of
the evidence.
    On November 2, 2011, the district court issued a written
order stating that it was inclined to deny the motion, but
asking Cook to respond to the following questions: “Is the
Court correct that Defendant believes the motion can be
resolved without an evidentiary hearing? If not, what facts
does Defendant contend are in dispute?” The next day,
during a hearing on Cook’s motion, the court invited him to
answer the questions it had posed. Cook did not ask for an
evidentiary hearing, failed to dispute that the first search
occurred, and failed to identify any particular factual dispute.
Instead, he raised a new challenge that there was no probable
cause to arrest him. The court continued the hearing and
allowed Cook to file a supplemental brief addressing
probable cause. Cook later did so, but still did not identify a
factual dispute. On December 22, 2011, the district court
denied Cook’s motion without an evidentiary hearing.
                  UNITED STATES V. COOK                      7

    After Cook’s first trial ended in a mistrial, on August 30,
2012, he renewed his motion to suppress and, for the first
time, claimed that the initial search of his backpack did not
occur at all. Cook argued that inconsistencies between
Officer Knight’s and Special Agent Dial’s trial testimony
showed that the initial search was a “post-hoc invention.”
The district court, without holding an evidentiary hearing,
denied Cook’s motion. The court explained that it had the
opportunity during the trial to assess the credibility of the
testifying agents, and there was “no basis to discredit”
Officer Knight’s testimony that the first search occurred.
    Following a second trial, the jury convicted Cook on
November 1, 2012 of conspiracy to possess with intent to
distribute and possession with intent to distribute illegal
narcotics. On March 6, 2013, Cook again renewed his
motion to suppress. This time, he focused on Special Agent
Dial’s admission that his testimony during the first trial was
incorrect. Special Agent Dial had testified that he was
present at the first search of Cook’s backpack, when in fact
he was only there during the second, more thorough search.
The district court again denied an evidentiary hearing,
because it concluded that it already had a sufficient basis to
evaluate the witnesses’ credibility, having heard their
testimony at two trials. It found that there was “no basis to
discredit [Special Agent Dial’s] testimony that he simply
made a mistake about his participation in the initial search of
Cook’s backpack.” The court denied Cook’s motion. This
appeal followed.
                              II
    Cook argues that the first search violated his rights under
the Fourth Amendment. The government counters that the
search was incident to a lawful arrest, and thus fell within
that exception to the warrant requirement. As an initial
8                 UNITED STATES V. COOK

matter, although the evidence Cook seeks to suppress was
found during the second search of his backpack, which
occurred at a nearby restaurant parking lot, Cook only
challenges the first search that occurred at the scene of his
arrest. This is because Cook recognizes that if that search
was valid, then the second warrantless search was permitted
“so long as [his backpack] remain[ed] in the legitimate
uninterrupted possession of the police.” United States v.
Burnette, 698 F.2d 1038, 1049 (9th Cir. 1983). We review
a denial of a motion to suppress evidence de novo. United
States v. Maddox, 614 F.3d 1046, 1048 (9th Cir. 2010).
                              A
    A search incident to a lawful arrest is a well-established
exception to the Fourth Amendment’s warrant requirement.
See Arizona v. Gant, 556 U.S. 332, 338 (2009). This
exception allows an officer to search “the arrestee’s person
and the area ‘within his immediate control,’” defined as “the
area from within which he might gain possession of a
weapon or destructible evidence.” Chimel v. California, 395
U.S. 752, 763 (1969). As the Supreme Court explained in
Gant, the “immediate control” requirement “ensures that the
scope of a search incident to arrest is commensurate with its
purposes of protecting arresting officers and safeguarding
any evidence of the offense of arrest that an arrestee might
conceal or destroy.” 556 U.S. at 339. The Court in Gant
held that the officers’ search of Gant’s car was unreasonable
because, prior to the search, Gant and two other arrestees
were already handcuffed and locked inside separate police
                     UNITED STATES V. COOK                            9

cars. Thus, “Gant clearly was not within reaching distance
of his car at the time of the search.” Id. at 344. 1
    In evaluating the reasonableness of a search incident to
arrest, we have examined not only whether the area searched
was within the arrestee’s “immediate control,” but also
whether any event occurred after the arrest that rendered the
search unreasonable. Maddox, 614 F.3d at 1048. While
“[t]here is no fixed outer limit for the number of minutes that
may pass between an arrest and a valid, warrantless search,”
United States v. McLaughlin, 170 F.3d 889, 892 (9th Cir.
1999), we have said that the search must be “spatially and
temporally incident to the arrest,” United States v. Camou,
773 F.3d 932, 937 (9th Cir. 2014). See also United States v.
Smith, 389 F.3d 944, 951 (9th Cir. 2004) (per curiam)
(interpreting the temporal requirement to mean that the
search must be “roughly contemporaneous with the arrest”);
United States v. Monclavo-Cruz, 662 F.2d 1285, 1288 (9th
Cir. 1981) (holding that the search of the purse of an arrestee
“more than an hour after her arrest at the station house” was
not valid incident to arrest).
                                  B
    Cook argues that the initial search of his backpack was
not valid incident to arrest because he was handcuffed at the
time of the search, and thus there was no reasonable concern
for officer safety or evidence destruction.
    We agree that Cook’s position at the time of the search—
face down on the ground with his hands cuffed behind his


 1
    We do not read Gant’s holding as limited only to automobile searches
because the Court tethered its rationale to the concerns articulated in
Chimel, which involved a search of an arrestee’s home. Gant, 556 U.S.
at 342-43. Neither party in this case contends otherwise.
10                UNITED STATES V. COOK

back—is a highly relevant fact in determining whether the
search was justified. Yet Cook’s argument ignores other
countervailing facts that we must also consider. The search,
both quick and cursory, was “spatially and temporally
incident to the arrest.” Camou, 773 F.3d at 937. It occurred
immediately after Officer Knight arrived on the scene, as
Cook was being taken into custody. Cook’s backpack was
right next to him. And, within twenty to thirty seconds, as
soon as Officer Knight determined that the backpack
contained no weapons, he immediately stopped the search.
The brief and limited nature of the search, its immediacy to
the time of arrest, and the location of the backpack ensured
that the search was “commensurate with its purposes of
protecting arresting officers and safeguarding any evidence
of the offense of arrest that [Cook] might conceal or
destroy.” Gant, 556 U.S. at 339.
    Cook relies heavily on Gant, but the circumstances here
are entirely different. Unlike Gant, who was arrested for
driving on a suspended license, Cook was arrested for
serious felony drug offenses. Significantly, Gant was locked
inside a patrol car, while Cook’s backpack was easily within
“reaching distance.” Id. at 344. The fact that Cook was
already handcuffed is significant, but not dispositive. See
United States v. Sanders, 994 F.2d 200, 209 (5th Cir. 1993)
(stating that “[a]lbeit difficult, it is by no means impossible
for a handcuffed person to obtain and use a weapon
concealed on his person or within lunge reach, and . . . like
any mechanical device, handcuffs can and do fail on
occasion”). We cannot say here that there was no reasonable
possibility that Cook could break free and reach for a
backpack next to him. Gant, 556 U.S. at 339.
    Moreover, contrary to Cook’s claim, the agents’ safety
concerns were objectively reasonable. The agents had
reason to believe that Cook used the same backpack earlier
                  UNITED STATES V. COOK                      11

in the day to transport drugs, and they had already recovered
two firearms from the house associated with Cook’s co-
conspirator. That Cook’s arrest took place in front of the
same house, and a crowd had gathered nearby, heightened
the agents’ reasonable fear that a bystander or additional
unidentified co-conspirator might intervene. Under the
totality of the circumstances, we conclude that the search of
Cook’s backpack was reasonable and valid incident to arrest.
See United States v. Robinson, 414 U.S. 218, 235 (1973)
(stating that an officer’s decision to search incident to arrest
“is necessarily a quick and ad hoc judgment” that need not
“be broken down in each instance into analysis of each step
of the search”). Therefore, the district court properly denied
his motions.
    We note that under similar facts, our sister circuit
reached the same conclusion, in a case cited by both parties.
In United States v. Shakir, the Third Circuit found that a
search of a duffel bag, which Shakir had dropped at his feet
when he was arrested, was reasonable. 616 F.3d 315, 321
(3d Cir. 2010). Shakir’s hands were already cuffed, and two
officers were holding his arms, when another officer bent
down and searched the bag. Id. at 317. The Third Circuit
considered the circumstances of the arrest and search,
including the location of the arrest in a hotel lobby with
many people around, the fact that Shakir’s duffel bag was
right at his feet, and the officers’ concern that accomplices
were nearby. Id. at 319. Upholding the search, the Shakir
court concluded that “there remained a sufficient possibility
that Shakir could access a weapon in his bag.” Id. at 321.
Much of the same analysis, as we discussed, applies here.
As Cook points out, there are factual differences in his case.
For example, Shakir was standing up, and his large size
made it initially difficult to handcuff him, whereas Cook’s
build is slight and he was face down on the ground. None of
12                 UNITED STATES V. COOK

the factual distinctions relied on by Cook, however, are
sufficient to alter our analysis.
                              III
    We next turn to Cook’s claim that the district court
abused its discretion in failing to hold an evidentiary hearing
to determine whether the initial search of his backpack
actually occurred.
     “An evidentiary hearing on a motion to suppress need be
held only when the moving papers allege facts with
sufficient definiteness, clarity, and specificity to enable the
trial court to conclude that contested issues of fact exist.”
United States v. Howell, 231 F.3d 615, 620 (9th Cir. 2000);
see also United States v. Batiste, 868 F.2d 1089, 1093 (9th
Cir. 1989) (stating that the district court was not required to
hold an evidentiary hearing on the defendant’s motion to
suppress where the defendant failed to dispute any material
fact in the government’s proffer). We review the district
court’s denial of an evidentiary hearing for abuse of
discretion. See United States v. Hoang, 486 F.3d 1156, 1163
(9th Cir. 2007).
     Cook’s first motion to suppress failed to raise a material
factual dispute. The district court nevertheless invited Cook
to clarify by directing him to confirm that “the motion can
be resolved without an evidentiary hearing” and to identify
facts that Cook “contend[s] are in dispute.” In response,
Cook neither asked for an evidentiary hearing nor identified
a single disputed fact. He instead focused on a new legal
argument that his arrest was not supported by probable
cause. In short, because Cook failed to “allege facts with
sufficient definiteness, clarity, and specificity to enable the
trial court to conclude that contested issues of fact exist,” the
court did not abuse its discretion in failing to hold an
evidentiary hearing. Howell, 231 F.3d at 620.
                   UNITED STATES V. COOK                        13

     Cook now contends that he in fact identified a factual
dispute by arguing below that Officer Knight’s first search
was “manufactured for the purpose of legitimatizing an
otherwise unlawful search.”            What Cook fails to
acknowledge, however, is that he raised this claim only after
his first trial. By that point, the district court had already
heard trial testimony from the law enforcement witnesses—
Officer Knight and Special Agent Dial—who Cook would
have called in support of his motion. Because Cook had
already cross-examined these witnesses’ accounts of the first
search, the district court could use “[t]estimony at trial . . . to
sustain the denial of a motion to suppress evidence.” United
States v. Sanford, 673 F.2d 1070, 1072 (9th Cir. 1982). This
is especially true where, as here, Cook never proffered in his
renewed motions that, at an evidentiary hearing, he would
testify to an alternate version of the moments after his arrest.
United States v. Hernandez-Acuna, 498 F.3d 942, 945 (9th
Cir. 2007) (holding that even though “trials serve a different
function from evidentiary hearings,” a district court could
dispense with an evidentiary hearing on a motion to suppress
in light of the defendant’s opportunity to cross-examine at
trial the only witnesses who would have testified at a
suppression hearing before the court). As the district court
stated, it had the opportunity to observe the demeanor of the
witnesses, and to assess their testimony and credibility
during two trials. Thus, the district court did not abuse its
discretion in determining that no evidentiary hearing was
necessary.
                               IV
    Finally, Cook argues that his rights under the Sixth
Amendment’s Confrontation Clause were violated because
the agents were allowed to testify about Edmonds’s
identification of him as the supplier, even though Edmonds
was not a trial witness. We need not decide whether the
14               UNITED STATES V. COOK

district court erred because, even if it did, any error was
harmless. The evidence implicating Cook in the conspiracy
as the supplier was compelling. Shortly before the drug buy,
the agents saw Cook appear to drop something off from his
backpack at Lambert’s house. After Edmonds was arrested,
he placed a monitored phone call to Cook, who expressed
his satisfaction that the deal had gone through. Cook then
came to Lambert’s house with the same backpack that he had
carried earlier, and the backpack contained MDMA of the
same purity as the MDMA that Edmonds had offered to the
agents.      Thus, any error in admitting Edmonds’s
identification of Cook as his supplier was “harmless beyond
a reasonable doubt.” United States v. Morales, 720 F.3d
1194, 1199 (9th Cir. 2013).
                            ***
    The district court properly denied Cook’s motions to
suppress because the search of his backpack was valid
incident to arrest. We further conclude that the district
court’s failure to hold an evidentiary hearing was not an
abuse of discretion, and any error in the court’s evidentiary
rulings was harmless beyond a reasonable doubt.
     AFFIRMED.

```

---

## GROUP: _overhaul2/lake/cases/united-states-v-cruz--10662743.json  (`lake-record`, 1 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6f4f5eb34ea2f63e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-cruz--10662743"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-cruz--10662743", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-cruz--10662743

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-cruz--10662743",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "United States v. Negron-Cruz",
    "case_name_short": "Negron-Cruz",
    "case_name_full": "",
    "input_case_name": "United States v. Cruz",
    "court": "1st Cir. 2025",
    "court_id": "ca1",
    "court_level": "coa",
    "circuit": "ca1",
    "state": null,
    "date_decided": "2025-08-28",
    "year": 2025,
    "docket": "23-1976",
    "cluster_id": 10662743,
    "lead_opinion_id": 11129330,
    "sibling_ids": [],
    "absolute_url": "/opinion/10662743/united-states-v-negron-cruz/",
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
      "court_class": "state",
      "selected": null,
      "reason": "no_official_class_citation"
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
    "date_created": "2026-07-06T05:52:42Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:52:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:52:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:52:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:52:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — united-states-v-cruz--10662743

```
          United States Court of Appeals
                      For the First Circuit


No. 23-1976

                    UNITED STATES OF AMERICA,

                            Appellee,

                                v.

                      ALEXIS D. NEGRÓN-CRUZ,

                      Defendant, Appellant.


          APPEAL FROM THE UNITED STATES DISTRICT COURT
                FOR THE DISTRICT OF PUERTO RICO

         [Hon. Francisco A. Besosa, U.S. District Judge]


                              Before

                   Gelpí, Lipez, and Rikelman,
                         Circuit Judges.


     Kevin E. Lerman, Assistant Federal Public Defender, with whom
Rachel   Brill,   Federal   Public   Defender,   and   Franco   L.
Pérez-Redondo, Assistant Federal Public Defender, were on brief,
for appellant.

     Tory D. Roberts, Assistant U.S. Attorney, with whom W. Stephen
Muldrow, U.S. Attorney, Mariana E. Bauzá-Almonte, Assistant U.S.
Attorney, and Gregory B. Conner, Assistant U.S. Attorney, were on
brief, for appellee.


                         August 28, 2025
            RIKELMAN,     Circuit    Judge.        Alexis       Negrón-Cruz     was

sentenced to ten years in prison and 25 years of supervised release

after   pleading   guilty      to   one   count    of    possession      of   child

pornography.     Since Negrón finished his prison term, the district

court has revoked his supervised release three times.

            In this appeal, Negrón challenges the second revocation

("Second Revocation"). He argues that we should reverse the Second

Revocation judgment and vacate his sentence because the district

court improperly considered ex parte statements from his probation

officer.     Alternatively, he asks that we vacate two conditions of

his supervised release that, taken together, allow him to access

the   internet   only    via   devices    with    court-approved        monitoring

software.     In his view, these conditions are unconstitutional and

unlawfully    delegate    judicial    authority     to    the    U.S.   Probation

Office. On the record here, we find no legal error and accordingly

affirm the Second Revocation judgment and sentence in full.

                               I.    BACKGROUND

            Negrón pleaded guilty to one count of possession of child

pornography in 2013.      The underlying facts involved Negrón sharing

a video, in an online chatroom, of himself having sex with an

individual who he claimed was a minor.              Subsequently, he shared

additional videos of minors as young as five being sexually abused

by others and attempted to arrange sex with an eight-year-old girl

and a woman he believed was her mother.                   The district court


                                     - 2 -
sentenced him to ten years in prison and 25 years of supervised

release.   Negrón began serving his supervised release term in

December 2019. One of the supervised release conditions prohibited

Negrón   from   possessing      any   "device    with    internet    accessing

capability" without prior approval of a probation officer.

                           A.    First Revocation

           In   February    2022,     Negrón's   supervised       release   was

revoked ("First Revocation").          The district court determined that

Negrón "had access[ed] . . . the internet without approval of the

probation officer," among other violations.             Negrón, who had been

detained pending his revocation proceedings, was sentenced to time

served and a new supervised release term of 25 years.

           Because   Negrón       had    violated       an    internet-related

condition, the district court also imposed a new set of supervised

release conditions governing internet access.                Special Conditions

31 and 32, at issue in this appeal, read in relevant part:

           31.    [Mr. Negrón] shall consent to the
           installation of systems that will enable the
           Probation Officer or his or her designee to
           monitor and filter any internet accessing and
           data storage device, owned or controlled by
           [him].    Mr. Negrón shall consent to, and
           cooperate with, unannounced examinations on
           any equipment owned or controlled by him,
           which may result in retrieval and copying of
           all data from the device and any internal or
           external peripherals and may involve removal
           [of] the equipment to conduct a more thorough
           inspection. . . . Mr. Negrón shall contribute
           to the cost of the monitoring service based on
           his ability to pay.


                                      - 3 -
          32. He shall not possess or use a computer,
          cellular telephone, or any other device with
          internet accessing capability, at any time or
          place other than those with systems that will
          enable the Probation Officer or his or her
          designee to monitor and filter any internet
          accessing.

Negrón began serving his new supervised release term under the

modified conditions immediately.

                      B.     Second Revocation

          After Negrón was released to a homeless shelter in

February 2022 and a few days into his new supervised release term,

Negrón informed the Probation Office that he had acquired a

smartphone.    Officer     Taisa    Mojica,   his   probation   officer,

conferred with her supervisors, and then agreed that Negrón could

keep the smartphone "until he could secure employment to cover the

monitoring cost."

          In March 2022, Officer Mojica learned that Negrón had

secured a second smartphone.         Negrón's primary smartphone was

seized for forensic examination and, a few days later, so was his

second smartphone.   Negrón received his primary smartphone back at

some point thereafter, but it seems that his second smartphone was

never returned to him.

          Six months later in September 2022, when Negrón was

seeking to re-establish a relationship with one of his daughters,

Officer Mojica reminded Negrón that the Probation Office needed to

install the monitoring system on his primary smartphone.          Negrón


                                   - 4 -
had been employed in the months since February 2022 but nonetheless

stated that he was unable to pay for the monitoring software.

Officer Mojica responded that Negrón should then secure a phone

incapable of connecting to the internet.                The next day, Negrón

said   that    he   would   switch   over    to   a   cellular   plan   for   his

smartphone that would no longer include internet.                Officer Mojica

rejected   Negrón's     proposal,    since    his     smartphone   could   still

connect to the internet even without a data plan.            By early October

2022, Negrón still had not followed Officer Mojica's instruction,

so she told him to hand over his smartphone.              He complied but did

not provide the passcode, asserting that the phone had been factory

reset.

              Negrón switched jobs in October but did not inform

Officer Mojica of his change in employment until mid-November.

Officer Mojica met with Negrón to address the matter, and Negrón

argued that he did not inform her earlier because he had handed

over his smartphone.        Officer Mojica once again instructed Negrón

to secure a basic phone incapable of connecting to the internet

because he was unable to pay for the monitoring software.               Officer

Mojica and Negrón then agreed that he would provide paystubs and

a formal letter indicating the change in employment, and he did so

in late November.

              Officer Mojica and Negrón met again two months later in

January 2023, and Negrón provided her with his latest paystub.                He


                                     - 5 -
also admitted that he had kept an iPad from his prior employer,

had   an   unauthorized    smartphone   with   internet    access      in   his

possession, and had applied for a job with Uber.                   Probation

officers visited his home in early February to confiscate the

devices, but Negrón refused to relinquish the iPad and deleted his

smartphone contacts before giving up his phone.

            Later   that   month,    Officer   Mojica     filed    a     motion

requesting that the district court issue an arrest warrant charging

Negrón with violating the terms of his supervised release.                After

the warrant was issued, the court ordered that Negrón be detained

pending his preliminary revocation hearing.

            Negrón's preliminary revocation hearing took place on

March 6, 2023, and Officer Mojica was the only witness.                     The

magistrate judge found probable cause for all but one of the

alleged    violations   but   nonetheless   permitted     Negrón    to    leave

detention that day, subject to the same conditions of supervised

release plus two additions: Negrón had to wear an electronic

monitoring device and submit to home detention.

            The next day, Officer Mojica discovered that Negrón had

activated the SIM card from his original smartphone.                She then

seized the smartphone for a forensic examination and initially

instructed Negrón, as she had before, to get a phone incapable of

connecting to the internet in the meantime.        But after concluding

that finding a phone without internet access is functionally


                                    - 6 -
impossible (because even flip phones might have internet access),

she instructed Negrón to get a flip phone instead.

           Twenty days after his smartphone was seized, on March

27, 2023, Negrón returned to the Probation Office to retrieve the

phone, with the monitoring software finally installed.             During his

interactions    with     the   probation     officers   that   afternoon,    he

mentioned that he was continuing to deliver for Uber Eats and for

his own online small business.            It then became clear that Negrón

had obtained yet another backup smartphone. In response to Officer

Mojica's questions, Negrón explained that he had acquired the

backup phone because he could not wait until the officers returned

his original smartphone.        At the end of this March 27 meeting, the

Probation Office returned Negrón's original smartphone to him with

the monitoring software installed and seized the newly discovered

backup smartphone.

           Officer Mojica filed a motion requesting another arrest

warrant later that day.         The warrant was issued, and Negrón was

again detained.      On April 13, the magistrate judge held another

preliminary revocation hearing, which focused on Negrón's alleged

violations of his supervised release conditions since March 6.

This   time,   Officer     Mojica   and    Officer   Guillermo   Montañez,    a

supervisor     for   the   Probation      Office,    both   testified.      The

magistrate judge again found probable cause to conclude that Negrón




                                     - 7 -
had violated his supervised release conditions and ordered Negrón

detained pending his final revocation hearing.

           The district court held the final revocation hearing in

November    2023.         During    his    allocution,        Negrón     expressed

significant      frustration      about   how   the   Probation        Office   had

enforced his supervised release conditions.                    He concluded by

stating that "while [Officer] Mojica" and two other officers "are

working at the [P]robation [O]ffice, you can leave me in jail."

The   district    court    took    judicial     notice   of    the     preliminary

revocation hearing on March 6.             It then ruled that Negrón had

violated Special Conditions 31 and 32, among other conditions,1

and revoked the supervised release term that was imposed as part

of the First Revocation.          The court sentenced Negrón anew to time

served and 270 months (22 years and six months) of supervised

release, with the same supervised release conditions that were

imposed    following      the     First   Revocation,     including        Special

Conditions 31 and 32.

                           C.      Third Revocation

           In December 2024, while appellate briefing in this case



      1The district court also concluded that Negrón violated
Standard Conditions 4, 6, 7, and 13. Condition 4 requires Negrón
to answer the Probation Office's questions truthfully; Condition
6 permits the Probation Office to meet Negrón anywhere at any time;
Condition 7 requires regular employment in a lawful occupation;
and Condition 13 requires Negrón to follow the Probation Office's
instructions. These conditions are not challenged on appeal.


                                      - 8 -
was   underway,   the   district   court   revoked   Negrón's   supervised

release for a third time ("Third Revocation").        It determined that

Negrón had again violated Special Condition 31, as well as other

standard and special conditions.       The court sentenced him to two

years in prison and 268 months (22 years and four months) of

supervised release.       Negrón has separately appealed the Third

Revocation to this court.      See United States v. Negrón-Cruz, No.

25-1017 (1st Cir. docketed Jan. 8, 2025).

                            II.    DISCUSSION

           We have jurisdiction to hear Negrón's appeal from the

Second Revocation under 28 U.S.C. § 1291 and 18 U.S.C. § 3742(a).2


      2Given our "obligation to inquire sua sponte into our
jurisdiction" in every case, Doyle v. Huntress, Inc., 419 F.3d 3,
6 (1st Cir. 2005), we also consider whether the Third Revocation
moots this appeal from the Second Revocation. We conclude that it
does not.
     "[A] case is moot when the court cannot give any effectual
relief to the potentially prevailing party."     ACLU of Mass. v.
U.S. Conf. of Cath. Bishops, 705 F.3d 44, 52 (1st Cir. 2013)
(quotation marks and citation omitted). "An appeal from an order
revoking supervised release is ordinarily moot if the sentence is
completed before the appeal is decided."        United States v.
Mazzillo, 373 F.3d 181, 182 (1st Cir. 2004) (per curiam).      But
such an appeal is not moot if the defendant is still serving his
supervised release term. See United States v. Reyes-Barreto, 24
F.4th 82, 86 (1st Cir. 2022). In such cases, a defendant still
"has a stake in the outcome of [an] appeal" because he "could seek
equitable relief by way of a motion to modify the terms of his
supervised release" or "file a motion to terminate his supervised
release early." Id. at 85-86 (citing 18 U.S.C. § 3583(e)(1)-(2)).
     The reasoning of Reyes-Barreto applies here. In determining
a sentence for the Third Revocation, the district court relied in
part on Negrón's "pattern of recurrent noncompliance" with his



                                   - 9 -
           As we previewed above, Negrón focuses on two primary

arguments.       First,    he        requests    that    we   reverse      the   Second

Revocation judgment and vacate his sentence.                     In his view, the

district court improperly considered ex parte statements from

Officer Mojica during his revocation proceedings, in violation of

due process and Federal Rule of Criminal Procedure 32.1.                         Second,

he   challenges     the    district           court's    imposition       of     Special

Conditions   31     and    32.          Those    conditions,         he   argues,    are

unconstitutional     and       amount     to     impermissible        delegations      of

judicial authority to the Probation Office.

                      A.        Ex Parte Communications

           Negrón    asks       that     we    reverse   the    Second      Revocation

judgment   and    vacate       his    sentence    because      the    district      court

impermissibly relied in part on ex parte statements from Officer

Mojica during the final revocation hearing.                          We disagree and

conclude that the district court's actions do not warrant reversal.

Before we explain our reasoning, we recap the relevant proceedings

before the district court and sketch out the legal framework.

                          1.     Relevant Proceedings

           We begin with the proceedings that form the backdrop of

Negrón's ex parte communication challenge.                    Officer Mojica filed


supervised release conditions.  Thus, if we were to vacate the
Second Revocation, Negrón could seek equitable relief to reduce
the supervised release term imposed as part of the Third
Revocation. See 18 U.S.C. § 3583(e)(1)-(2).


                                        - 10 -
two motions with the district court after the March 6, 2023

preliminary revocation hearing -- first, an informative motion

filed on March 10, and second, a motion for an arrest warrant filed

on   March    27   --   alleging   additional   violations   of   Negrón's

conditions since March 6.

             Two factual allegations in those motions are critical

for our purposes.       In the first motion, Officer Mojica claimed:

             [O]n January 19, 2023, [Officer Mojica] met
             with   Mr.   Negrón-Cruz . . . . During   the
             intervention, Mr. Negrón-Cruz stated that he
             applied for a job "with Uber." . . . On March
             9, 2023, [Officer Mojica] became aware that
             Mr. Negrón-Cruz is or has been employed by
             Uber.

She asserted that Negrón's conduct violated Standard Condition 7,

which requires timely notice of any change in employment.            In the

second motion, Officer Mojica claimed:

             On March 27, 2023, . . . . Mr. Negrón-Cruz
             . . . admitted to having a backup cellphone.
             When advised that he could not have had a
             back-up   phone    without    the   officer's
             authorization, he responded that he cannot
             wait until the officer decides to install the
             required monitoring software.

The unauthorized possession of the phone, she alleged, was a

violation     of   Negrón's   supervised    released   conditions.     The

district court issued the arrest warrant, and Negrón was detained.

             The preliminary revocation hearing that focused on these

particular allegations was held in April 2023.           At the hearing,

Officers Mojica and Montañez testified that the Probation Office



                                   - 11 -
found and seized Negrón's unauthorized backup smartphone.   Negrón,

for his part, did not introduce any evidence to the contrary or

even dispute that account.    His counsel argued instead that the

phone restrictions were "Byzantine" and trapped Negrón in a cycle

of recurring revocation.    Further, the government did not elicit

any testimony or introduce other evidence at the hearing to support

the allegation that Negrón failed to report his employment with

Uber.    The magistrate judge ultimately found "probable cause that

the defendant violated his conditions of supervised release as

alleged in . . . [the] motions filed by Probation."

           The case then proceeded to the final revocation hearing

in November 2023, during which the district court had the following

exchange with defense counsel:

           THE COURT:     I have been speaking with
           [Officer] Mojica about what to do today with
           Mr. Negrón, and we both agreed that the best
           thing to do would be to give him time served.
           Is that okay with you, Mr. McCutcheon?

           MR. MCCUTCHEON: Judge, it's fine for me. I
           would probably have to lodge objections, just
           because he would ask me to do that, to the
           conditions of supervised release.3

The court then took judicial notice of the transcript of the March

2023 preliminary revocation hearing, making no mention of the April



     3 The district court also asked Officer Mojica whether the
"supervised release terms" that she had suggested imposing "were
the same that were imposed before," to which she replied "yes"
(minus a drug condition not relevant to this appeal).


                               - 12 -
2023 preliminary revocation hearing.    (Nor could it, given that

the transcript for the April hearing was not ready until two months

after the November final revocation hearing took place.)

          The district court ultimately concluded that Negrón

violated his supervised release conditions, including Standard

Condition 7 and Special Condition 32.   Then, before imposing its

sentence, the court recited its findings of fact.    It determined

that:

          On January 19, 2023, Mr. Negrón lied to his
          probation officer, [Officer] Mojica, . . .
          when he stated that he had applied [for] a job
          with Uber when in fact information provide[d]
          by the Government confirmed that Mr. Negrón
          had already had an active delivery account
          with Uber since January 4, 2023.

The court also found:

          [O]n March 27, 2023, . . . Mr. Negrón admitted
          to having a cell phone. When advised that he
          could not have a backup phone without the
          officer's authorization, he responded that he
          could not wait until the officer decided to
          install the required monitoring software.
          This behavior constitute[s] violations of
          standard condition number 4 and special
          condition number 32 . . . .

At the end of the hearing, Negrón objected to the court's factual

findings on ex-parte-communication grounds.

          The district court then imposed a prison term of time

served and a renewed supervised release term of 270 months, which

was necessary in its view "[t]o reflect the seriousness of Mr.

Negrón's noncompliant behavior and to protect the public."



                              - 13 -
                            2.    Legal Overview

            The sweep of information that a sentencing court may

consider is "broad in scope," but it is not unlimited.                United

States v. Reyes-Correa, 81 F.4th 1, 7 (1st Cir. 2023) (quoting

Pepper v. United States, 562 U.S. 476, 489 (2011)).               The Due

Process Clause of the Fifth Amendment to the U.S. Constitution

guarantees that "[n]o person shall be deprived of life, liberty,

or property, without due process of law."          U.S. Const. amend. V.

And Federal Rule of Criminal Procedure 32.1 requires that a

defendant   subject   to    revocation   proceedings   "is   entitled"    to

"disclosure of the evidence against the person" and "an opportunity

to appear, present evidence, and question any adverse witness,"

subject to an exception not applicable here.           Fed. R. Crim. P.

32.1(b)(2)(B)-(C).         Together,   these   provisions    ensure   basic

fairness to a defendant in revocation proceedings, including by

requiring that the "defendant be apprised of the information to be

relied on in sentencing and [have] an opportunity to challenge and

rebut such information."         Reyes-Correa, 81 F.4th at 8 (citation

omitted).

            Some ex parte communications between a probation officer

and a district court are lawful.            "[A]s the sentencing court

prepares for the revocation and sentencing hearing, '[e]x parte

communication between the probation officer and the court is

usually permissible where the court is merely seeking advice or


                                   - 14 -
analysis, . . . and the probation officer and the court may consult

privately about certain issues incident to criminal sentencing.'"

Id. (second alteration and omission in original) (quoting United

States v. Marrero-Pérez, 914 F.3d 20, 25 (1st Cir. 2019)).            That

is in part because a "probation officer is simply an extension of

the court itself," and "a sentencing court's communications with

the   probation   officer   are   fundamentally    different   from   its

communications with third parties."        United States v. Bramley, 847

F.3d 1, 6 (1st Cir. 2017).

           When a sentencing court is not merely seeking advice and

analysis, however, its reliance on an ex parte communication from

a probation officer can be reversible error if the communication

conveys "new information" that is "significant."       Reyes-Correa, 81

F.4th at 8 (quoting United States v. Ramos-Carreras, 59 F.4th 1,

5 (1st Cir. 2023)).    Information is "new" when it is "not already

found in the district court's record," and it is "significant"

when it is "'materially relied on' by the district court in

determining a sentence."    Id. (quoting Ramos-Carreras, 59 F.4th at

5).   Thus, new and significant facts relayed solely through ex

parte communications "cannot be relied upon by the sentencing court

unless and until they are disclosed to the parties and subjected

to whatever adversarial testing may be appropriate."       Bramley, 847

F.3d at 7.




                                  - 15 -
                               3.     Analysis

           We now turn to Negrón's challenge here.            Negrón argues

that the district court's remark that it "[had] been speaking with

[Officer] Mojica about what to do today with Mr. Negrón" and that

they had "both agreed that the best thing to do would be to give

him time served" was evidence of an ex parte conversation.                That

conversation alone, of course, would not necessarily amount to

error if it merely concerned "advice or analysis" about the length

of Negrón's prison term.       Reyes-Correa, 81 F.4th at 8.      But Negrón

points to two facts -- first, his possession of a backup smartphone

on March 27, and second, his employment history with Uber -- that

he alleges were conveyed in the district court's meeting with

Officer Mojica and that he claims warrant closer scrutiny.

           The parties agree that Negrón timely objected to the use

of these facts in sentencing, so our review is for abuse of

discretion.   See id. at 7.         But Negrón's objection to these ex

parte   communications   did    not   immediately    follow   each   of    the

district court's factual findings, so the court did not clarify

how it reached these particular conclusions.            Cf. Bramley, 847

F.3d at 5 (reasoning that "timely objection[s]" can "shed light on

the nature of the conversations").           In any event, we review what

is in the record (and what is not) to assess how the court arrived

at its findings, noting that "the district judge had to learn the

allegations from somewhere."        Ramos-Carreras, 59 F.4th at 6.


                                    - 16 -
             First, we consider the district court's determination

that Negrón admitted to having an unauthorized smartphone on March

27, 2023.      The district court did not abuse its discretion by

relying on this fact because, even if it surfaced in an ex parte

communication, the information was not "new."               Reyes-Correa, 81

F.4th at 8.      To be sure, the fact was highlighted at the April

preliminary revocation hearing, which had yet to be transcribed,

so we assume favorably to Negrón that the district court indeed

learned about it during an ex parte conversation.               But even so,

the Probation Office's March 27 motion for an arrest warrant

alleged that Negrón possessed an unauthorized smartphone on that

day.    And we have previously held that the "explicit mention" of

information in an arrest warrant motion makes it "difficult to

characterize        [the     information]       as   'new   information'     or

extra-record evidence."           Id. at 8-9.    Nor did Negrón ever dispute

that he possessed the unauthorized smartphone, even when given a

chance to do so at the April preliminary revocation hearing.               When

a defendant has not contested a fact supposedly conveyed in an ex

parte communication, his argument "that he was unprepared for [that

fact]   to   play    a     role   in   his   ultimate   sentencing"   is   less

persuasive.     Id. at 8.

             Second, we evaluate the district court's conclusion that

Negrón "lied" to Officer Mojica on January 19, 2023, about his

employment with Uber because he "already had an active delivery


                                       - 17 -
account with Uber since January 4, 2023."                This finding appears to

refer to "new" and "significant" facts shared in an ex parte

communication, so it was an abuse of discretion for the district

court to rely on those facts.            Cf. Ramos-Carreras, 59 F.4th at 7

(holding that, under the plain error standard, a district court's

recital of "extraneous non-record avowals without identifying the

source   or    providing      notice    to    [the    defendant]"       in   a   final

revocation hearing was "clear error").                   From our review of the

record, there was no allegation or evidence of Negrón lying to

Officer Mojica on January 19 or of Negrón's employment history

with Uber prior to that date, making the conveyed information

"new."     Id.       And although the district court never expressly

explained which supervised release conditions Negrón's "lie[]"

violated, it recited its finding that he lied among the list of

other violations, leaving us to think that the court "materially

relied on" these facts when determining his sentence.                    Id.     Thus,

the district court's reliance on these facts was unlawful.

              That   error,    however,      was     harmless.      A    procedural

sentencing "error is harmless if 'the error did not affect the

district      court's      selection         of    the     sentence      imposed.'"

Reyes-Correa, 81 F.4th at 9 (quoting Williams v. United States,

503 U.S. 193, 203 (1992)).         Here, the district court recited two

other instances when Negrón had lied to a probation officer and

one other instance when he had failed to give timely notice of a


                                       - 18 -
change in employment, all of which are unchallenged on appeal.           So

even without the alleged misrepresentation on January 19, Negrón

would nonetheless have violated the same conditions of supervised

release.    And Negrón offers no basis to conclude that, without

this particular finding, the court would have imposed a different

sentence.    Thus, we determine that the district court's reliance

on an ex parte communication about the supposed lie was "unlikely"

to "influence[] the sentence."4        Reyes-Correa, 81 F.4th at 9.

            Finally, Negrón argues that the district court should

not have consulted Officer Mojica at all.            In his view, Officer

Mojica had an improper interest in the outcome of the case and

undermined the appearance of justice in the revocation proceedings

simply   because   she   had    been   Negrón's    supervising   probation

officer.     But   Officer     Mojica's   supervisory   authority   is   an

extension of the district court's powers, see Bramley, 847 F.3d at

6, so her participation in the revocation proceedings, standing

alone, cannot be the basis for error.             Indeed, Negrón does not


     4 Negrón also contends that the district court's reliance on
facts learned ex parte is a structural error, not subject to
harmless error analysis, and requires reversal. The Supreme Court
"has classified an error as structural in only a very limited class
of cases." United States v. Rivera-Rodriguez, 617 F.3d 581, 604
(1st Cir. 2010). And Negrón offers no authority to suggest that
ex parte communications with a probation officer before a
revocation hearing result in structural error. His only citation
in support is to Tumey v. Ohio, which involved a judge with a
financial interest in the outcome of a trial and therefore is
clearly inapposite. See 273 U.S. 510, 535 (1927). Thus, we reject
this argument based on the briefing before us.


                                   - 19 -
cite to any precedent that supports the notion that her mere

involvement      in     the    proceedings,        without    any    allegations   of

misconduct or legal error, would be problematic. Cf. Reyes-Correa,

81 F.4th at 8-10 (making no issue of the fact that the probation

officer who allegedly engaged in ex parte communication was the

officer supervising the defendant).                 Thus, with no other developed

argument by Negrón for disturbing the district court's ruling, we

affirm the Second Revocation judgment and sentence.

                      B.      Special Conditions 31 and 32

            Now    we      turn     to   Negrón's    prospective      challenges    to

Special Conditions 31 and 32.                   In his view, these conditions

violate    his    First       and   Fifth     Amendment     rights    and   unlawfully

delegate judicial power to the Probation Office.5

            Negrón objected to Special Conditions 31 and 32 at the

final    revocation        hearing,      so   we   review    the    district   court's

imposition of these special conditions for abuse of discretion.

See United States v. Perazza-Mercado, 553 F.3d 65, 69 (1st Cir.

2009).    Under that umbrella standard, "we inspect fact findings



     5 In the conclusion of his appellate brief, Negrón requests
that we vacate only Special Condition 31. But, at other points in
his brief, he challenges the "complex of conditions" that limit
his internet access. And Special Condition 31's requirement that
Negrón use monitoring software cannot be enforced without the ban
on unauthorized devices mandated by Special Condition 32. Thus,
for purposes of our analysis, we assume that Negrón intends to
challenge both special conditions to the extent they restrict his
constitutional rights.


                                          - 20 -
for clear error, legal issues de novo[,] . . . and judgment calls

with some deference."   United States v. McCullock, 991 F.3d 313,

317 (1st Cir. 2021).6

                        1.    Ability to Pay

          We begin with Negrón's first constitutional challenge.

Negrón argues that Special Condition 31 is unlawful because the

Probation Office enforces it in a manner that requires him to pay

the   internet   monitoring   fee   regardless   of   his   financial

circumstances.   That supposed policy, he maintains, violates the

Fifth Amendment's equal protection guarantee.

          We disagree that Special Condition 31 violates Negrón's

equal protection rights based on the arguments before us.         The

Fifth Amendment limits a district court's power to revoke an


      6Relying on United States v. Eaglin, Negrón urges us to
"conduct a more searching review" of the factors governing special
conditions restricting internet access, which pose "heightened
constitutional concerns." 913 F.3d 88, 95 (2d Cir. 2019).
     Eaglin's standard, however, is not the law of our circuit.
We have applied the abuse of discretion standard in each of our
cases analyzing supervised release conditions restricting internet
access.    See Perazza-Mercado, 553 F.3d at 69; United States v.
Stergios, 659 F.3d 127, 133 (1st Cir. 2011); United States v.
Ramos, 763 F.3d 45, 58 (1st Cir. 2014); United States v. Hinkel,
837   F.3d   111,   125  (1st   Cir.  2016);   United  States   v.
Aquino-Florenciani, 894 F.3d 4, 6 (1st Cir. 2018); United States
v. Windle, 35 F.4th 62, 67 (1st Cir. 2022).       And we have not
applied a more rigorous standard when evaluating special
conditions posing other types of constitutional concerns.     See,
e.g., United States v. Millette, 121 F.4th 946, 953-54 (1st Cir.
2024) (special condition that impaired defendant's "constitutional
interest in parenting his daughter"); United States v. Del
Valle-Cruz, 785 F.3d 48, 58 (1st Cir. 2015) (similar).


                               - 21 -
indigent   defendant's    supervised    release   based     solely   on   the

nonpayment of fines.     See Bearden v. Georgia, 461 U.S. 660, 672-73

(1983); see also United States v. Merric, 166 F.3d 406, 411 (1st

Cir. 1999) ("Obviously, a court could not properly make it a

condition of probation or supervised release that a penniless

defendant make immediate payments, nor can we imagine sending [a]

defendant back to jail where he had done his best to comply with

an installment schedule.").       But revocation on nonpayment grounds

is permitted if a defendant "willfully refuse[s] to pay" or does

not "make sufficient bona fide efforts to seek employment or borrow

money in order to pay."      Bearden, 461 U.S. at 668.

            To begin, Special Condition 31 is not unconstitutional

on   its   face.      Because   the   special   condition    requires     the

software-monitoring fee to be assessed based on Negrón's "ability

to pay," it does not require revocation solely on the basis of

nonpayment.     Thus, it does not violate equal protection.7              See

Merric, 166 F.3d at 411; see also United States v. Santarpio, 560

F.2d 448, 455–56 (1st Cir. 1977) (upholding special condition

requiring payment to government so long as it is "enforced with

proper regard to the question of the defendant's ability to pay").

            Negrón also advances an as-applied challenge to Special

Condition 31.      He argues that the Probation Office knew full well


      7The government does not contest the application of Bearden
to Special Condition 31.


                                  - 22 -
that he was indigent and that he never             "materially withheld

information" about his income, raising important points for his

ongoing supervision.      The Probation Office cannot, consistent with

Negrón's constitutional rights, require him to pay the monitoring

fee if he is financially unable to do so.          See Bearden, 461 U.S.

at 672-73.     Indeed, it cannot enforce the payment requirement

"without a finding that the funds are available."           United States

v. Chorney, 63 F.3d 78, 83 (1st Cir. 1995) (quoting Santarpio, 560

F.2d at 455) (requiring such a finding for supervised release

conditions    directing    defendants   to   pay   the   costs   of    their

court-appointed counsel).      Similarly, the Probation Office cannot

prohibit Negrón from using internet-capable devices unless it

first determines that he has available funds to offset some of the

costs of monitoring those devices but nevertheless has willfully

refused to pay any portion of those costs.

            But Negrón's as-applied challenge is ultimately unripe.

Negrón does not contend that we should vacate the Second Revocation

because the Probation Office enforced Special Condition 31 in a

manner that violated his equal protection rights. And the paystubs

that Negrón provided to Officer Mojica in November 2022 and January

2023 are not in the record, nor did Negrón present a developed

argument to the district court or to us about why his income as

reflected on those paystubs would prohibit him from covering any

of   the   software   monitoring   costs.    Rather,     Negrón's     counsel


                                   - 23 -
expressly stated at oral argument before us that his constitutional

challenges to this condition are prospective.      He requested that

we strike the condition as drafted and "provide guidance" to the

district court and the Probation Office on how to craft and enforce

any similar condition in the future.     Yet our court has held that

we cannot consider prospective challenges to supervised release

conditions   that   rely   on   the   "unusually   inappropriate   or

ineffective way" that the condition may be implemented.       United

States v. Medina, 779 F.3d 55, 67 (1st Cir. 2015); see also United

States v. Hood, 920 F.3d 87, 94 (1st Cir. 2019); United States v.

Sebastian, 612 F.3d 47, 52 (1st Cir. 2010); United States v. York,

357 F.3d 14, 25 (1st Cir. 2004).      Unlike facial challenges, such

as-applied challenges "depend on the particular way in which" the

Probation Office "may choose" to enforce the special condition.

Medina, 779 F.3d at 67; see also Hood, 920 F.3d at 94 (explaining

that an as-applied challenge, "unlike [a] facial challenge, . . .

necessarily depends on future factual contingencies").      Thus, we

conclude that Negrón's as-applied equal protection challenge is

"not ripe for our review," Hood, 920 F.3d at 94, and that Special

Condition 31 does not violate equal protection on its face.

          Nevertheless, we repeat that, under our precedent, the

Probation Office cannot require Negrón to pay for monitoring

without a finding that he has the financial ability to do so, nor




                                - 24 -
can it ban Negrón from using the internet altogether without

determining that he has willfully refused to pay what he can.

                     2.   Access to the Internet

          Next, Negrón contends that Special Conditions 31 and 32

stand "to periodically cut off internet access for time periods so

excessive [that] they violate the First Amendment."   In his view,

the Probation Office "gave no explanation for why there was a

twenty[-]day delay in the installation of the software" where the

process "takes only one hour," and that gap in access resulted in

an "excessive and unjustified" restriction of his First Amendment

rights.   Based on the specific arguments before us, we conclude

that there has been no First Amendment violation.

          To evaluate a constitutional challenge to a condition of

supervised release, we must analyze whether the condition indeed

"intrudes upon a constitutionally protected right."   United States

v. Smith, 436 F.3d 307, 311 (1st Cir. 2006).   And even if it does,

we will vacate a condition only if we determine that, "on a given

set of facts, a particular restriction" on a defendant's liberty

"is clearly unnecessary."    Id. at 310 (quoting United States v.

Brown, 235 F.3d 2, 7 (1st Cir. 2000)) (upholding special condition

restricting the fundamental right to associate with a close family

member); see also United States v. Marino, 833 F.3d 1, 12 (1st

Cir. 2016) (same).




                               - 25 -
          To begin, there is, of course, a constitutional right at

stake.   The First Amendment's free speech guarantee protects

Negrón's right to access the internet.              See Packingham v. North

Carolina, 582 U.S. 98, 107 (2017) (holding that a state law barring

sex   offenders   from       accessing     social     media   websites     was

"unprecedented    in   the    scope   of    First     Amendment   speech   it

burden[ed]"); Berge v. Sch. Comm. of Gloucester, 107 F.4th 33, 40

(1st Cir. 2024) (noting that the First Amendment's "protections

apply to the 'vast democratic forums of the internet'" (quoting

Packingham, 582 U.S. at 104)); see also United States v. Eaglin,

913 F.3d 88, 96 (2d Cir. 2019) (reading Packingham to hold that

there is "a First Amendment right to access the Internet"); United

States v. Ellis, 984 F.3d 1092, 1105 (4th Cir. 2021) (holding that

"an internet ban implicates fundamental rights").

          Further, as the government concedes, Special Conditions

31 and 32 restrict Negrón's First Amendment rights.               See Smith,

436 F.3d at 310 (concluding that the condition there "impinge[d]

upon" a "constitutionally protected" right).              These conditions

require that Negrón access the internet only on devices that are

equipped with monitoring software.          See United States v. Windle,

35 F.4th 62, 68 (1st Cir. 2022) (evaluating whether a monitoring

condition was clearly unnecessary to deter the defendant from

future crime).




                                  - 26 -
              That said, we cannot conclude that Special Conditions 31

and 32 violate the First Amendment based on the arguments presented

by Negrón here.         According to Negrón, "the present complex of

conditions impose[s] a virtually total ban on internet access at

any time."      To be clear, our circuit has repeatedly held that a

total   ban    on     internet    access   is   the   kind    of   "broad-brush,

untailored approach to sculpting the conditions of supervised

release" that results in "'a greater deprivation of liberty than

is reasonably necessary' to achieve the penal goals Congress has

identified."        United States v. Hinkel, 837 F.3d 111, 125 (1st Cir.

2016) (quoting 18 U.S.C. § 3583(d)(2)); see also United States v.

Ramos, 763 F.3d 45, 61-62 (1st Cir. 2014); Perazza-Mercado, 553

F.3d at 69-70.

              But Special Conditions 31 and 32 impose a monitoring

requirement, which "is not a complete or partial ban" on internet

access.       Windle, 35 F.4th at 68            (emphasis added)      (upholding

imposition of monitoring condition for defendant convicted of

internet fraud); cf. also United States v. Aquino-Florenciani, 894

F.3d 4, 7 (1st Cir. 2018) (rejecting "total ban" argument where

defendant, who was convicted of child pornography offenses, was

permitted to use devices "subject to approval from his probation

officer   and        electronic    monitoring").          Rather,     monitoring

conditions      are    "narrowly     tailored     tools      for   reaching   the

appropriate balance between monitoring an offender in order to


                                     - 27 -
protect the public, while still allowing him some reasonable

internet access."     Ramos, 763 F.3d at 61-63 (striking a total

internet ban on a defendant convicted of a child pornography

offense not involving the internet, but leaving the monitoring

condition in place); see also Perazza-Mercado, 553 F.3d at 73-74

(striking a total ban on home internet use by defendant convicted

of sex offense not involving the internet, but noting that courts

can   "fashion   precise   restrictions"    on    internet      usage   like

monitoring-software requirements).8      Thus, on their face, Special

Conditions 31 and 32 do not run afoul of the First Amendment.

          Negrón next contends that Special Conditions 31 and 32,

as applied, stand "to periodically cut off internet access for

time periods so excessive [that] they violate the First Amendment."

He complains that the Probation Office "gave no explanation for

why there was a twenty[-]day delay in the installation of the

software" in March 2023, where the process "takes only one hour."

He further claims that this substantial gap in internet access

resulted in an "excessive and unjustified" restriction of his First

Amendment rights.

          Twenty    days   without   internet    access   is,    indeed,   a

substantial restriction by the government on an individual's First



      8Unlike the defendants in these cases, Negrón does not
challenge Special Conditions 31 and 32 as not reasonably related
to the statutory sentencing factors. See 18 U.S.C. § 3583(d)(1).


                                - 28 -
Amendment rights.           But, again, Negrón confirmed at oral argument

that his constitutional challenges to the monitoring requirement

are purely prospective.          And the question of whether the Probation

Office's manner of enforcing a generally permitted monitoring

requirement is "clearly unnecessary" is heavily fact-dependent.

See Hood, 920 F.3d at 94; Medina, 779 F.3d at 67; Sebastian, 612

F.3d at 52; York, 357 F.3d at 25.              For example, the government

contends that the 20-day delay reflects the time it took to conduct

a forensic examination of Negrón's phone on top of installing the

monitoring software.           And the record does not reflect what is a

reasonable time period for such a forensic examination.                Thus, we

also must dismiss Negrón's as-applied First Amendment challenge as

unripe and affirm Special Conditions 31 and 32 as otherwise

facially constitutional.

                       3.    Delegation of Judicial Power

               We now turn to Negrón's final challenge.         He argues that

Special Conditions 31 and 32 unlawfully delegate the core judicial

power to decide "whether or not his internet will be monitored."

               Article III of the U.S. Constitution prohibits "federal

courts from delegating to nonjudicial officers (such as probation)

their     core    judicial     function,    including     the   imposition   of

conditions        of    supervised       release."        United    States   v.

Morales-Cortijo, 65 F.4th 30, 35 (1st Cir. 2023).                  To determine

whether    a     special     condition   infringes   on   the   core   judicial


                                      - 29 -
function, "we distinguish between delegations that merely task the

probation officer with performing ministerial acts or support

services and those that permit the officer to decide the nature or

extent of the punishment itself."          Id. at 36 (citation modified)

(quoting United States v. Mike, 632 F.3d 686, 695 (10th Cir.

2011)).    If we conclude that a special condition amounts to an

unlawful     delegation,   then   we    vacate   the   relevant   special

condition.     See United States v. Sepulveda-Contreras, 466 F.3d

166, 173 (1st Cir. 2006).

           Negrón makes two delegation arguments, but we conclude

that neither ultimately prevails.           First, he contends that the

Probation Office's power to "[de]activate and reactivate" Special

Conditions 31 and 32 regardless of his "ability to pay the fee"

reflected "an unreasonable delegation of authority" and "virtually

unlimited discretion." Negrón is correct that the Probation Office

suspended the monitoring-software requirement in February 2022,

when Negrón was newly released from prison and homeless.          At that

time, Officer Mojica told him that he could use a smartphone

without monitoring software "until he could secure employment to

cover the monitoring cost."            The Probation Office's actions,

however well-intentioned, were clearly inconsistent with Special

Condition 32.     But even so, Special Condition 32 itself did not

authorize the Probation Office to determine if and when such

monitoring software would be required, so we see no basis to


                                  - 30 -
invalidate     that   condition.      See,   e.g.,    id.   (vacating   the

drug-testing provision giving rise to the unauthorized action).

          Second,     Negrón   argues   that   the    Probation   Office's

imposition of a 44-paragraph contract governing internet usage,

titled the "Computer & Internet Management Program" (CIMP), is an

unlawful expansion of his punishment.        Generally, CIMPs assist the

Probation Office with "mandat[ing] compliance" with a defendant's

conditions of supervised release.       United States v. Stergios, 659

F.3d 127, 134 (1st Cir. 2011) (quoting Sebastian, 612 F.3d at 52).

And although certain provisions of a CIMP could theoretically

exceed the Probation Office's delegated authority, Negrón fails to

identify any provisions that do so here.9            In any event, Negrón

never signed the CIMP at issue in this case, so the CIMP was never

enforced against him.       Thus, his challenge depends on "future

factual contingencies" -- like how the CIMP would be enforced, or

which provisions would be invoked -- that render it "not ripe for

our review."    Hood, 920 F.3d at 94.




     9  Negrón mentions in passing that the CIMP unlawfully
restricts him to one internet-connected device. The CIMP appears
contradictory on that point, with one provision stating that Negrón
"shall only possess Internet-capable devices approved by the
Probation Officer" and another stating that Negrón "shall not use
any other Internet-capable device than the one you have been
authorized to use." As we explain, Negrón may file a motion to
clarify his supervised release conditions under 18 U.S.C.
§ 3583(e)(2) if he is unable to agree on the scope of the
conditions with the Probation Office.


                                   - 31 -
            And    we   note    that    Negrón      has   recourse   "should     the

probation officer abuse the discretion delegated to her."                  United

States v. Mercado, 777 F.3d 532, 537 (1st Cir. 2015).                 A district

court may modify, enlarge, or reduce a supervised release condition

under 18 U.S.C. § 3583(e)(2).                Thus, Negrón can always request

relief    from    the   district      court    if   the   Probation   Office     is

"attempting unreasonably or unnecessarily" to enforce a particular

condition.        Mercado,     777    F.3d    at   537.    Such   relief   may   be

appropriate if further disputes arise concerning Negrón's "ability

to pay" the monitoring software fee; Negrón is slated to serve 22

years and four months of supervised release following his current

prison term, which may result in a substantial cost for the

monitoring software.

                               III.     CONCLUSION

            For all these reasons, we affirm the Second Revocation

judgment and sentence.10



     10Negrón also makes two procedural requests on appeal, which
we deny.   First, he asks that we reverse the district court's
supposed denial of his motion to access his mental health report.
But the district court never decided that motion.      Rather, in
response to the motion, it indicated in a docket entry "[n]oted."
So with no order to review, we lack appellate jurisdiction to go
any further.   See United States v. Kouri-Perez, 187 F.3d 1, 13
(1st Cir. 1999).
     Second, Negrón requests that we remand the case to a different
district judge. Because there was no reversible error, we decline
to do so. See United States v. Castillo-Torres, 8 F.4th 68, 73
(1st Cir. 2021).


                                       - 32 -

```

---

## GROUP: _overhaul2/lake/cases/united-states-v-cunningham--166076.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a154d90a4a4084d0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "united-states-v-cunningham--166076"}, "payload": {"all": [{"cite": "413 F.3d 1199", "page": "1199", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "413"}, {"cite": "2005 U.S. App. LEXIS 13145", "page": "13145", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2005"}, {"cite": "2005 WL 1541074", "page": "1541074", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2005"}], "display": "413 F.3d 1199", "official": {"cite": "413 F.3d 1199", "page": "1199", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "413"}, "official_selection_present": true, "record_id": "united-states-v-cunningham--166076"}}
{"assertion_id": "0b89969498023804", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-cunningham--166076"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-cunningham--166076", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-cunningham--166076

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-cunningham--166076",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "United States v. Cunningham",
    "case_name_short": "Cunningham",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. William CUNNINGHAM, Defendant-Appellant",
    "input_case_name": "United States v. Cunningham",
    "court": "U.S. Court of Appeals, 10th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": null,
    "year": 2005,
    "docket": null,
    "cluster_id": 166076,
    "lead_opinion_id": 166076,
    "sibling_ids": [],
    "absolute_url": "/opinion/166076/united-states-v-cunningham/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "413 F.3d 1199",
      "volume": "413",
      "reporter": "F.3d",
      "page": "1199",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2005 U.S. App. LEXIS 13145",
        "volume": "2005",
        "reporter": "U.S. App. LEXIS",
        "page": "13145",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2005 WL 1541074",
        "volume": "2005",
        "reporter": "WL",
        "page": "1541074",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "413 F.3d 1199",
        "volume": "413",
        "reporter": "F.3d",
        "page": "1199",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2005 U.S. App. LEXIS 13145",
        "volume": "2005",
        "reporter": "U.S. App. LEXIS",
        "page": "13145",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2005 WL 1541074",
        "volume": "2005",
        "reporter": "WL",
        "page": "1541074",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "413 F.3d 1199",
    "official_selection": {
      "court_class": "coa",
      "selected": "413 F.3d 1199",
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
    "date_created": "2026-07-06T13:43:39Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:43:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:43:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:43:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:43:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — united-states-v-cunningham--166076

```
                                                                       F I L E D
                                                                United States Court of Appeals
                                                                        Tenth Circuit

                                                                        July 1, 2005
                                  PUBLISH
                                                                     PATRICK FISHER
                                                                            Clerk
              UNITED STATES COURT OF APPEALS
                       TENTH CIRCUIT



 UNITED STATES OF AMERICA,

       Plaintiff-Appellee,

 v.                                                    No. 04-3026

 WILLIAM CUNNINGHAM,

       Defendant-Appellant.


                 Appeal from the United States District Court
                          for the District of Kansas
                        (D.C. No. 03-CR-20073-GTV)


Patrick J. Berrigan, of Watson & Dameron, LLP, Kansas City, Missouri,
appearing for the Defendant-Appellant.

Leon J. Patton, Assistant U.S. Attorney (Eric F. Melgren, United States Attorney,
with him on the briefs), Kansas City, Kansas, appearing for the Plaintiff-
Appellee.


Before SEYMOUR, Circuit Judge, McWILLIAMS, Senior Circuit Judge, and
KELLY, Circuit Judge.


SEYMOUR, Circuit Judge.
      Mr. William Cunningham conditionally pled guilty to one count of making,

possessing, and uttering counterfeit securities (checks), in violation of 18 U.S.C.

§§ 2 and 513(a). He appeals the denial of his motion to suppress, contending the

district court erred in finding that his consent to a search of his home by law

enforcement officers was voluntary. We affirm on the alternative basis of the

inevitable discovery doctrine.



                                          I

      From November 2002 through January 2003, law enforcement officers were

investigating a counterfeit check-writing ring in the Kansas City metropolitan

area. On January 28, 2003, four suspects in the ring were arrested as they tried to

pass counterfeit checks at banks in Overland Park, Kansas and Kansas City,

Missouri. Information obtained from these suspects led law enforcement to

believe they should focus their investigation on the 1100 block of East 76th

Terrace in Kansas City, Missouri. Specifically, one of the suspects identified the

residence at 1179 East 76th Terrace as the house from which their check

“supplier,” James Hughes, had gone to obtain the counterfeit checks. Another

suspect reported that Hughes had actually acquired the checks from the

neighboring house at 1175 East 76th Terrace. The two remaining suspects were

unsure whether Hughes had derived the checks from either address. Police noted


                                         -2-
that the homes share a common driveway.

      Based on this information, Police Detective Kevin Duncan prepared an

affidavit for a search warrant for the residence located at 1175 East 76th Terrace

and presented it to the Assistant United States Attorney (AUSA). According to

Detective Duncan, during the meeting with the AUSA,

      We came to the agreement that at this time it wouldn’t be best to proceed
      with the search warrant based on the possibility that we would go into the
      wrong address. Obviously, that was a concern to everyone, and we decided
      to go ahead and continue surveillance and now concentrate on that area
      including those two houses . . . .

Aplt. App. at 82-83. In other words, although probable cause existed to believe

that the supplier had obtained the checks from either 1175 or 1179 East 76th

Terrace, the police pursued a policy of additional surveillance in order to

specifically determine which of the two houses was the source of the criminal

activity. The officers set up surveillance of the residences on the evening of

January 29, 2003. That night they observed a red Chevrolet Lumina parked at

1179 East 76 Terrace. The vehicle matched the description of a car belonging to

Tikko Parish, an individual previously identified by other suspects as someone

who had frequently accompanied Hughes. As the car left the residence, officers

stopped it and discovered both Hughes and Parish inside.

      Police also stopped a black pickup truck in the area, which was being

driven by Mr. Cunningham. He informed them he resided at 1179 East 76th


                                         -3-
Terrace. Mr. Cunningham was arrested on unrelated charges of driving with a

suspended driver’s license and transported to jail. Although Mr. Cunningham had

not been implicated in the check-writing ring, the black pickup truck he drove

matched the description of one identified earlier in the investigation.

      Subsequent to the traffic stops, officers decided to knock at the door of

1175 East 76th Terrace. The residents, a family of three, permitted the officers to

enter and look around their home. They spoke freely with the police and pointed

out that the gray Blazer parked in the shared driveway – which matched the

description of a vehicle earlier identified with Hughes – belonged to 1179 East

76th Terrace. Once the officers were satisfied that Hughes had not obtained the

checks from 1175 East 76th Terrace, they decided to attempt to make contact with

someone at 1179 East 76th Terrace.

      As police knocked at the door of 1179 East 76th Terrace, Detective Linny

Cunningham, a twenty-five year veteran of the Kansas City, Missouri, Police

Department, arrived on the scene. Mrs. Cunningham recognized one of the

officers present as Sergeant Roy Orth, a fellow member of her police department.

Although Sergeant Orth was superior in rank to Mrs. Cunningham, he had no

supervisory authority over her. Mrs. Cunningham identified herself as the owner

of the house and reported that although she did not live at the location, her

twenty-nine year old son, William Cunningham, had resided there for five years.


                                         -4-
Sergeant Orth indicated that the officers needed to get inside the house. He

declined Mrs. Cunningham’s offer to let them in, however, due to her inability to

legally consent to a search of the home.

      In the meantime, police released Mr. Cunningham from jail on a bond and

transported him to 1179 East 76th Terrace for the purpose of obtaining his

consent to search the house. When Mr. Cunningham arrived, the officers

implored him to give consent to a search of his residence. They indicated that

they were conducting an ongoing investigation and would obtain a search warrant

should he refuse to provide consent. Nevertheless, Mr. Cunningham repeatedly

refused to give permission to search. Even after his mother spoke to him, he

continued to resist signing the consent form. Eventually, Mrs. Cunningham told

her son “I got the feeling that I was in trouble now with the PD because with Orth

there and he’s expecting me to get [the consent form] signed for him.” Id. at 192.

She also informed her son that should he decide not to sign the consent form, the

police were going to get a warrant and “they were going to go in there and they

are going to tear up your house. Hopefully they won’t do anything to the dogs

inside of the house.” Id. at 203. As Mrs. Cunningham spoke to her son, “he was

sad, and he started sobbing.” Id. at 192.

      According to Mr. Cunningham’s testimony, his mother said:

      [T]hey are going to get in your house; they are going to tear your doors
      down. Your dogs are in there. You’ve got a pit bull, you know . . . . They

                                            -5-
      are going to destroy your house. They are going to tear your doors off the
      hinges. Your dogs are going to get shot. Just let them in.

Id. at 217-18. Mr. Cunningham testified he was concerned that he had already

embarrassed his mother and did not wish to get her into trouble. He spoke with

her for five to ten minutes and “it was just upsetting.” Id. at 219. At the

conclusion of their conversation and approximately twenty minutes after his

arrival on the scene, Mr. Cunningham finally consented to the search of his home.

      During the search, the police observed numerous items of evidentiary value

including check stock paper, a shredder, and a computer with latex gloves nearby.

The officers did not seize any evidence at the time. Instead, they secured the

premises and revised their prior affidavit for a search warrant to include the new

information that had focused them on 1179 East 76th Terrace, as well as the

evidence they had seen at Mr. Cunningham’s residence. A magistrate judge

signed a search warrant and the police then seized the incriminating items.

      Mr. Cunningham filed a motion to suppress the evidence obtained from his

home, arguing that his mother had coerced his consent. The district court,

however, found that the consent was valid and voluntary, stating:

      I find that this may have been a very awkward situation for Mrs.
      Cunningham, the defendant’s mother, but I think whether she was a mother
      or an officer or how she was acting is not really the point here because I
      think the totality of the evidence – and even if the representations that she
      made, if she made them to the defendant as a police officer, would still in
      this court’s opinion fall short of coercion such as to render the consent
      other than voluntary. That finding, of course, is tempered by the fact that

                                         -6-
      this was his mother telling him to sign this, and as I’ve said, even though it
      is an awkward situation for her, I find nevertheless that her actions did not
      rise to coercion.

Id. at 233. The court found that the officers had eliminated 1175 East 76th

Terrace as a possibility before they obtained the warrant for Mr. Cunningham’s

home and there was thus probable cause for the warrant. Consequently, the court

denied the motion to suppress.



                                         II

      On appeal, Mr. Cunningham contends the totality of the circumstances

amounted to duress and coercion that rendered his consent to search his home

involuntary. He points to the following facts to bolster this contention. He

initially and repeatedly refused to consent to the search while supervising officers

at the scene implored his mother, a police detective, to convince him to change

his mind. His dogs and personal property in the house were threatened with

destruction should he not cooperate. He also was convinced his mother’s

employment would be jeopardized if he refused to consent. We need not decide

whether Mr. Cunningham’s consent was voluntary, however, because we conclude

the inevitable discovery doctrine clearly applies here and supports the denial of

Mr. Cunningham’s motion to suppress.

      While we review the district court’s factual determinations for clear error,


                                         -7-
our review of an ultimate Fourth Amendment question is de novo. United States

v. Souza, 223 F.3d 1197, 1201 (10th Cir. 2000). When a search violates the

Fourth Amendment, the exclusionary rule normally dictates that evidence

obtained as a result of that search be suppressed. See Nix v. Williams, 467 U.S.

431, 442-43 (1984). The inevitable discovery doctrine provides an exception to

the exclusionary rule, see id. at 444, 448; United States v. Romero, 692 F.2d 699,

704 (10th Cir. 1982), and permits evidence to be admitted “if an independent,

lawful police investigation inevitably would have discovered it.” United States v.

Owens, 782 F.2d 146, 152 (10th Cir. 1986). The government possesses the

burden of proving by a preponderance of the evidence that the evidence at issue

would have been discovered without the Fourth Amendment violation. Souza,

223 F.3d at 1203 (citation omitted).

      In Souza, we set forth the standard for considering whether the inevitable

discovery doctrine applies to a warrantless search. Id. at 1205. We addressed

whether evidence found from the warrantless search of a package in a United

Parcel Service (UPS) facility was admissible under the doctrine. See id. at 1199,

1201. Probable cause existed for the presence of narcotics in the package,

including a positive alert by a narcotics dog. Id. at 1200. After a law

enforcement officer had contacted his office and expressed his intent to procure a

search warrant for the package, but before the warrant was obtained, a UPS


                                         -8-
employee opened the package, assisted in part by an officer. Id. Reviewing

Tenth Circuit case law regarding inevitable discovery, we noted that our

precedents had involved application of the doctrine in conjunction with another

exception to the warrant requirement, such as an inventory search or a search

incident to arrest. Id. at 1203. The facts in Souza, however, did not fit within any

of the other warrant requirement exceptions. Id. Nonetheless, we held it

permissible for a court to apply the inevitable discovery doctrine

      when it has a high level of confidence that the warrant in fact would
      have been issued and that the specific evidence in question would
      have been obtained by lawful means. Inevitable discovery analysis
      thus requires the court to examine each of the contingencies involved
      that would have had to have been resolved favorably to the
      government in order for the evidence to have been discovered legally
      and to assess the probability of the contingencies having occurred.

Id. at 1205. To assist this determination, we adopted the factors set forth by the

Second Circuit to assess warrantless search situations:

      1) the extent to which the warrant process has been completed at the
      time those seeking the warrant learn of the search; 2) the strength of
      the showing of probable cause at the time the search occurred; 3)
      whether a warrant ultimately was obtained, albeit after the illegal
      entry; and 4) evidence that law enforcement agents “jumped the gun”
      because they lacked confidence in their showing of probable cause
      and wanted to force the issue by creating a fait accompli.

Id. at 1204 (citing United States v. Cabassa, 62 F.3d 470, 473-74 & n.2 (2d Cir.




                                         -9-
1995)) (internal quotations and citations omitted). 1

      We concluded in Souza that the steps taken by law enforcement officers

satisfied the approach laid out in Cabassa. Id. at 1205. These included a law

enforcement officer alerting his office that he would be coming back to prepare a

warrant for the package, and ensuring an affidavit form would be ready when he

arrived back at the station. Moreover, the package was specifically placed apart

from others for the purpose of obtaining a warrant. Id. We also noted that

extremely strong probable cause existed to believe contraband was in the package

at the time of the illegal search, officers ultimately did obtain a search warrant,

and there were no doubts regarding whether the officers would actually obtain the

narcotics because the package had been secured by them. Id. at 1205-06. As a

result, we determined that “but for [the UPS employee] opening the package, [law

enforcement officers] would have obtained a warrant and the evidence would



      1
        The requirement set forth in United States v. Souza, 223 F.3d 1197, 1204-
05 (10th Cir. 2000), that the police have taken steps to obtain a warrant prior to
the illegal search may arguably be read to conflict with our earlier case, United
States v. Larsen, 127 F.3d 984 (10th Cir. 1997). In Larsen, we held that the
inevitable discovery doctrine does not require there to be a separate investigation
ongoing at the time of the constitutional violation. Id. at 986. We are not
persuaded there is an actual conflict, however. Larsen addressed a scenario
involving two unrelated and separate investigations. The circumstances in Souza
and the current case involve one line of investigation that would have led
inevitably to the obtaining of a search warrant by independent lawful means but
was halted prematurely by a search subsequently contended to be illegal.


                                         -10-
have been discovered.” Id. We observed that “exclusion of the evidence ‘would

put the police in a worse position than they would have been in absent any error

or violation.’” Id. (quoting Nix, 467 U.S. at 443).

      The present case squares with Souza. Here, the officers took substantial

steps to obtain a warrant before the contested search occurred. The record

demonstrates that they had focused their investigation on 1175 and 1179 East 76th

Terrace, and had drafted an affidavit to support a search warrant for one of these

homes. As a result of their conversation with the AUSA, the officers decided that

further surveillance on the two homes was necessary before they specifically

selected one to search, and they proceeded to conduct that surveillance

immediately. The officers’ actions clearly indicate they took steps to obtain a

search warrant and that they intended to obtain the warrant for either 1175 or

1179 East 76th Terrace as soon as possible.

      The officers also possessed strong probable cause for their search of 1179

East 76th Terrace by the time Mr. Cunningham arrived at the home. Prior to that

time, they had acquired background information about the alleged check-writing

ring, narrowed their investigation to one residential block, and focused on the two

homes sharing a common driveway. The officers’ surveillance had uncovered the

following additional information: a red car containing two individuals identified

earlier in the investigation arrived, parked briefly, and then pulled out from


                                         -11-
behind 1179 East 76th Terrace; a black pickup truck previously observed in the

investigation was stopped containing Mr. Cunningham, who said that he lived at

1179 East 76th Terrace; the residents of 1175 East 76th Terrace told officers that

the home next door had been receiving all of the traffic that evening, and the

officers ruled out 1175 East 76th Terrace as the location visited by the alleged

check supplier; and a gray Blazer previously observed in the investigation was

seen parked by 1179 East 76th Terrace. The government thus had sufficient

probable cause for a search of 1179 East 76th Terrace at the time of Mr.

Cunningham’s disputed consent to search his home.

      Moreover, the officers ultimately did obtain a warrant, albeit based in part

on information retrieved from inside Mr. Cunningham’s home. There is also no

evidence the officers “jumped the gun” due to a lack of confidence about

probable cause and out of a desire to force the issue. Id. at 1204. Instead, the

record indicates that the search occurred at the time it did because of the

coincidental arrival of Mrs. Cunningham. Her presence on the scene led to a

series of events that culminated in her son’s release from jail, his return home,

and his consent to search. As a result, we are satisfied the government has

demonstrated that, as in Souza, but for Mrs. Cunningham’s arrival at 1179 East

76th Terrace on the evening of the search, the officers would have obtained a

search warrant and the evidence in question would have been found. Id. at 1205.


                                         -12-
      Our case is unlike the scenario in Owens, 782 F.2d at 151-53, where we

declined to apply the inevitable discovery doctrine to the search of a motel room.

In that case, police arrested the room’s occupant, entered the room, and then

opened and searched a drawer as well as a closed bag inside that drawer,

ultimately discovering illegal drugs. Id. at 148-49. Although marijuana, white

powder, and drug paraphernalia were also in plain view and the police had full

control over the room, they made no attempt to seek a warrant. Id. at 149.

Declining to apply the inevitable discovery doctrine, we concluded that the illegal

searches of the drawer and bag tainted the only police investigation that was

ongoing. Thus, there did not exist any prior and independent investigation that

would have inevitably led to discovery of the concealed illegal drugs. Id. at 152.

We also disagreed with the government that the motel’s routine cleaning service

would have inevitably revealed the concealed drugs. Id. at 152-53. We observed

that the police’s complete failure to comply with the warrant requirement

although they had repeated opportunities to do so, “exemplif[ied] the very type of

official conduct the exclusionary rule is intended to deter.” Id. at 152. As

discussed above, the officers’ actions in the present controversy do not create the

same problem.

      We conclude by repeating our observation in Souza that “[i]n most cases,

the failure of the police to secure a warrant will probably be fatal.” 223 F.3d at


                                         -13-
1206. We apply the inevitable discovery doctrine in this case only because we are

convinced that without Mr. Cunningham’s disputed consent, the warrant to search

his house would have been issued and the incriminating evidence would have

been discovered.



                                       III

      For the foregoing reasons, we AFFIRM the decision of the district court

denying Mr. Cunningham’s motion to suppress.




                                       -14-

```

---
