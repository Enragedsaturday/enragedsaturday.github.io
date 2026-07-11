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

## GROUP: _overhaul2/lake/cases/United States v. Massenburg.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Massenburg
type: case
citation: "654 F.3d 480 (2011)"
parallel_cite: ""
neutral_cite: "2011 U.S. App. LEXIS 16849; 2011 WL 3559897"
court: 4th Cir. 2011
court_level: coa
circuit: ca4
year: 2011
date_decided: 2011-08-15
docket: 10-4209
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
  opinion_url: "https://www.courtlistener.com/opinion/223188/united-states-v-massenburg/"
  cluster_id: 223188
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Massenburg
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Collective Knowledge and the Fellow-Officer Rule]]"
    role: Key
related:
  - "[[Collective Knowledge and the Fellow-Officer Rule]]"
  - "[[Terry Stops and Reasonable Suspicion]]"
  - "[[United States v. Hensley]]"
  - "[[Reasonable Suspicion]]"
tags:
  - case
  - fourth-amendment
  - collective-knowledge
  - fellow-officer-rule
  - terry-stop
  - reasonable-suspicion
  - frisk
  - fourth-circuit
holding: "The Fourth Circuit reversed the denial of suppression, holding that the nonconsensual frisk of Massenburg was not supported by reasonable suspicion and — critically for the collective-knowledge doctrine — that Officer Fries's uncommunicated observation of a 'bulge' could not be imputed to the frisking officer: the collective-knowledge (fellow-officer) doctrine substitutes an instructing officer's knowledge for the acting officer's only where the information was communicated, and does not permit after-the-fact aggregation of uncommunicated facts among officers."
---

# United States v. Massenburg

*654 F.3d 480 (4th Cir. 2011)* (No. 10-4209) · U.S. Court of Appeals for the Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 223188 → majority opinion 223188 (654 F.3d 480, decided 2011-08-15, Davis, J.); Rule quote star-matched to the F.3d reporter pagination in the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Responding to an anonymous tip that shots were fired in a high-crime Richmond neighborhood, officers encountered four young men — including Tyerail Massenburg — about four blocks from the reported gunfire. The men were cooperative and not evasive: one reported hearing shots two blocks away, and at least two consented to pat-downs. Massenburg stopped with the group but refused to consent to a frisk. Officer Gaines, thinking him "nervous" and "reluctant," and noting that Massenburg stood a foot or two off from the shoulder-to-shoulder others and did not make eye contact, frisked him without consent, recovering a firearm and marijuana. Notably, a second officer, Fries, had earlier seen "a small bulge" in Massenburg's jacket pocket but "didn't alert" Gaines — and Gaines never saw any signal from Fries and never cited the bulge as a basis for his suspicion. Charged under 18 U.S.C. § 922(g)(3) and 21 U.S.C. § 844, Massenburg moved to suppress; the district court denied the motion, and he entered a conditional guilty plea.

## Issue
Whether the nonconsensual frisk was supported by reasonable suspicion, and whether Officer Fries's uncommunicated observation of a bulge in Massenburg's pocket could be imputed to the frisking officer under the collective-knowledge (fellow-officer) doctrine to supply the suspicion the acting officer otherwise lacked.

## Rule
An officer must have reasonable, articulable suspicion of criminal activity before conducting a frisk, and a suspect's refusal to consent cannot itself justify a nonconsensual search. The collective-knowledge doctrine operates only "vertically," on communicated alerts or instructions: "the collective-knowledge doctrine simply directs us to substitute the knowledge of the *instructing officer or officers* for the knowledge of the *acting officer;* it does not permit us to aggregate bits and pieces of information from among myriad officers, nor does it apply outside the context of communicated alerts or instructions." — 654 F.3d at 493. ^pin-493

## Application
The individualized facts — standing a foot or two apart, declining eye contact, and reluctance to consent — did not add up to reasonable suspicion, and refusing consent could not be spun into it. The Government's fallback was to impute Officer Fries's observation of the "bulge" to Gaines, but Fries never communicated it and Gaines never saw a signal or relied on it. That is "horizontal" aggregation of uncommunicated facts, which the court declined to allow: no Supreme Court or Fourth Circuit case had ever extended the collective-knowledge doctrine beyond the context of information or instructions communicated vertically to acting officers, because after-the-fact aggregation would make a search's legality turn on hindsight and would deprive officers of any way to know *ex ante* whether a search is lawful. Fries's unshared observation therefore could not supply the missing suspicion.

## Conclusion
**[[Reading and Citing Cases#vacated|Vacated]], reversed, and [[Reading and Citing Cases#on-remand|remanded]].** Judge Davis wrote for the panel (Davis, Motz, and Keenan, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Massenburg* is a leading Fourth Circuit statement cabining the **collective-knowledge / fellow-officer** rule to its **vertical**, communicated form: an instructing officer's knowledge may be imputed to the acting officer only when it was actually conveyed, and courts may not retroactively pool officers' uncommunicated observations to manufacture reasonable suspicion or probable cause. Teach it alongside the *[[Whiteley v. Warden|Whiteley]]*/*[[United States v. Hensley|Hensley]]* line and the vertical-versus-horizontal distinction.

## Appears on
- [[Collective Knowledge and the Fellow-Officer Rule]] — *Key*

## Sources
- [*United States v. Massenburg*, 654 F.3d 480 (4th Cir. 2011)](https://www.courtlistener.com/opinion/223188/united-states-v-massenburg/) — pinpoint: 493 (vertical-only / no-horizontal-aggregation holding; the CL opinion text star-paginates the F.3d reporter). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f032b25cb2ae8055", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Massenburg"}, "payload": {"all": [{"cite": "654 F.3d 480", "page": "480", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "654"}, {"cite": "2011 U.S. App. LEXIS 16849", "page": "16849", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2011"}, {"cite": "2011 WL 3559897", "page": "3559897", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2011"}], "display": "654 F.3d 480", "official": {"cite": "654 F.3d 480", "page": "480", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "654"}, "official_selection_present": true, "record_id": "United States v. Massenburg"}}
{"assertion_id": "a2f3ca6e69802ce6", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Massenburg"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Massenburg", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Massenburg

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Massenburg",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Massenburg",
    "case_name_short": "Massenburg",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Tyerail D. MASSENBURG, Defendant-Appellant",
    "input_case_name": "United States v. Massenburg",
    "court": "4th Cir. 2011",
    "court_id": "ca4",
    "court_level": "coa",
    "circuit": "ca4",
    "state": null,
    "date_decided": "2011-08-15",
    "year": 2011,
    "docket": "10-4209",
    "cluster_id": 223188,
    "lead_opinion_id": 223188,
    "sibling_ids": [],
    "absolute_url": "/opinion/223188/united-states-v-massenburg/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "654 F.3d 480",
      "volume": "654",
      "reporter": "F.3d",
      "page": "480",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2011 U.S. App. LEXIS 16849",
        "volume": "2011",
        "reporter": "U.S. App. LEXIS",
        "page": "16849",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 WL 3559897",
        "volume": "2011",
        "reporter": "WL",
        "page": "3559897",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "654 F.3d 480",
        "volume": "654",
        "reporter": "F.3d",
        "page": "480",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 U.S. App. LEXIS 16849",
        "volume": "2011",
        "reporter": "U.S. App. LEXIS",
        "page": "16849",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 WL 3559897",
        "volume": "2011",
        "reporter": "WL",
        "page": "3559897",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "654 F.3d 480",
    "official_selection": {
      "court_class": "coa",
      "selected": "654 F.3d 480",
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
    "date_created": "2026-07-06T05:55:49Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:55:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:55:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:55:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:55:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-massenburg--223188",
      "to_record_id": "United States v. Massenburg",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Massenburg

```
                       PUBLISHED


UNITED STATES COURT OF APPEALS
             FOR THE FOURTH CIRCUIT


UNITED STATES OF AMERICA,             
                Plaintiff-Appellee,
               v.                          No. 10-4209
TYERAIL D. MASSENBURG,
             Defendant-Appellant.
                                      
       Appeal from the United States District Court
     for the Eastern District of Virginia, at Richmond.
        Richard L. Williams, Senior District Judge.
                  (3:09-cr-00276-RLW-1)

                  Argued: May 13, 2011

                 Decided: August 15, 2011

  Before MOTZ, DAVIS, and KEENAN, Circuit Judges.



Vacated, reversed, and remanded by published opinion. Judge
Davis wrote the opinion, in which Judge Motz and Judge
Keenan joined.


                        COUNSEL

ARGUED: Caroline Swift Platt, OFFICE OF THE FED-
ERAL PUBLIC DEFENDER, Alexandria, Virginia, for
Appellant. Michael Arlen Jagels, OFFICE OF THE UNITED
STATES ATTORNEY, Richmond, Virginia, for Appellee.
2                UNITED STATES v. MASSENBURG
ON BRIEF: Michael S. Nachmanoff, Federal Public
Defender, Alexandria, Virginia, Carolyn V. Grady, Assistant
Federal Public Defender, OFFICE OF THE FEDERAL PUB-
LIC DEFENDER, Richmond, Virginia, for Appellant. Neil H.
MacBride, United States Attorney, Alexandria, Virginia, for
Appellee.


                         OPINION

DAVIS, Circuit Judge:

   In this appeal from a judgment of sentence, we are once
again called on to determine whether evidence seized during
a street encounter between law enforcement and citizens was
properly admitted into evidence during a subsequent criminal
prosecution. We conclude that the seizure of the evidence did
not comport with settled Fourth Amendment principles, and
we therefore reverse the district court’s denial of appellant’s
motion to suppress and remand for further proceedings.

   Responding one night to an anonymous tip that shots were
fired in a high-crime neighborhood, Richmond police encoun-
tered four young men, including appellant Tyerail Massen-
burg, four blocks from the reported gunfire. When an officer
approached them in a marked police car, the men were not
evasive; they continued walking forward, toward the car, and
voluntarily paused to speak with the officer upon the officer’s
request. In fact, they were cooperative: one of the men
reported that he had heard shots fired from a passing car two
blocks away and handed over his identification when asked;
and at least two of the men consented to voluntary pat-downs.
Appellant Massenburg stopped with his friends, but he
refused to consent to a frisk. As the officer interacting with
Massenburg testified, he first thought Massenburg nervous
when he began asking him to consent to a pat-down and
Massenburg was "real reluctant to give consent." J.A. 48.
                 UNITED STATES v. MASSENBURG                  3
Based on the fact that appellant stood a foot or two away from
the other men, who were shoulder-to-shoulder, and did not
make eye contact as the officer renewed his requests for a
consensual search, the officer undertook a nonconsensual
search. The search produced a firearm and some marijuana,
the subjects of the suppression motion at issue here.

   Charged with one count of possession of a firearm by a
drug user under 18 U.S.C. § 922(g)(3) and one count of pos-
session of marijuana under 21 U.S.C. § 844, Massenburg
moved to suppress the gun and drugs on the ground that the
officer’s frisk was unlawful. The district court denied that
motion, and Massenburg entered a conditional guilty plea,
reserving his right to appeal the suppression ruling.

   Before an officer can stop and frisk a citizen, she must have
"reasonable and articulable suspicion that the person seized is
engaged in criminal activity." Reid v. Georgia, 448 U.S. 438,
440 (1980). We recently warned against the Government’s
proffering "whatever facts are present, no matter how inno-
cent, as indicia of suspicious activity" and noted that we were
"deeply troubled by the way in which the Government
attempts to spin . . . mundane acts into a web of deception."
United States v. Foster, 634 F.3d 243, 248 (4th Cir. 2011).
This concern is only heightened when the "mundane acts"
emerge from the refusal to consent to a voluntary search. If
the important limitations on the "stop and frisk" regime
crafted by Terry v. Ohio, 392 U.S. 1 (1968), are not to
become dead letters, refusing to consent to a search cannot
itself justify a nonconsensual search.

                               I.

                              A.

  On the night of March 28, 2009, at 10:33 p.m., Richmond
City Police received an anonymous tip that shots had just
been fired. The caller reported eight shots fired "possibly" two
4                UNITED STATES v. MASSENBURG
blocks south of 14th and Hull Streets, a high-crime area in
which "drug activity as well as random gunfire" were
"usual[ ]." J.A. 46, 77. The caller said nothing more; in partic-
ular, he or she included no description of a suspect.

  Officers Stephen Gaines and Eric Fries responded to the
call and arrived at 14th and Hull at 10:48 p.m. They split up
and patrolled the area in marked police cars. Fries soon saw
four young black men, including appellant Massenburg, walk-
ing north at the corner of East 17th Street and Stockton Street,
four blocks west and two south of the intersection of 14th and
Hull and thus four blocks from the alleged origin of the shots.
They were walking in the direction of Fries’s marked car and
did not stop or change course when they saw it.

   Fries approached in his vehicle and asked, "hey guys, can
you stop for a second?" J.A. 31. The men stopped to talk with
him. Fries asked if they had heard gunfire, and one man
reported hearing shots fired from a vehicle on Maury Street,
two blocks south of their present location. Gaines arrived, the
two officers exited their vehicles, and they began taking the
men’s names. Fries then asked if they had weapons on them
and if they would consent to a pat-down. The four men were
now "all basically lined up in a row on the sidewalk," with the
man who reported hearing gunfire on Maury Street on the left
end of the line and Massenburg on the right. J.A. 32. Accord-
ing to Gaines, the three left-most men were "pretty much
shoulder-to-shoulder, and [Massenburg] was kind of offset
from the group" by a "foot or two," "give or take." J.A. 57.

   The man on the left consented to Fries’s request for a pat-
down, as did the man nearest him. Gaines began at the other
end of the line, asking Massenburg if he would consent to a
frisk. Gaines testified that Massenburg, in reply to the request,
"was kind of hesitant and stand-offish, and kind of real reluc-
tant to give consent to a pat down or a search of his person."
J.A. 48. Instead, "[h]e stated he did not have anything. You
don’t need to check me. Stood back and kind of air-patted
                 UNITED STATES v. MASSENBURG                   5
himself down, stating, trying to show he didn’t have any-
thing." J.A. 48. At this point Gaines insisted and patted
Massenburg down without his consent.

   Officer Fries testified that he had seen "a small bulge in the
left jacket pocket of Mr. Massenburg" prior to Officer
Gaines’s frisk, but he "didn’t alert" Gaines to it. J.A. 32, 42.
Officer Gaines, asked multiple times about the basis for his
suspicion of Massenburg, never indicated in his testimony
that he saw a sign or signal from Fries.

   During the frisk of Massenburg, Gaines felt the handle of
a firearm on Massenburg’s waist band (not in the jacket), and
Massenburg fled before Gaines could grab it. Gaines pursued
and directed him to drop the firearm, which Massenburg did,
dropping it on the grass. Massenburg ran another 250 feet
before Gaines caught up and arrested him. In addition to the
firearm, police recovered a small amount of marijuana on
Massenburg’s person.

                               B.

   Massenburg was charged with one count of possession of
a firearm by a drug user, in violation of 18 U.S.C.
§ 922(g)(3), and one count of possession of marijuana, in vio-
lation of 21 U.S.C. § 844. He filed a motion to suppress the
firearm and marijuana, arguing that Gaines lacked the reason-
able, particularized suspicion that he was engaged in criminal
activity necessary to authorize a nonconsensual frisk under
the Fourth and Fourteenth Amendments.

   At the suppression hearing, the Government presented few
objective bases for particularized suspicion of Massenburg. It
was only able to point to the following: (1) Massenburg and
his three friends were walking four blocks from the location
of the shots reported by the tipster, the only people the
responding officers encountered in the vicinity; and (2) sev-
eral observations made by Gaines of Massenburg’s allegedly
6                UNITED STATES v. MASSENBURG
"nervous behavior." In particular: (a) Massenburg was stand-
ing a foot or two from the other three men, who were
"shoulder-to-shoulder," J.A. 57; (b) he did not make eye con-
tact with Gaines as Gaines asked him to consent to a frisk;
and (c) he did not consent. Gaines’s testimony on these points
is instructive.

   Officer Gaines testified that "it wasn’t until actually I made
contact with him that I noticed nervous behavior from him."
J.A. 48. He elaborated:

       A: . . . We questioned if anybody had any weap-
    ons on them. The individuals besides Massenburg
    stated, we don’t have anything, you can check us.
    And Tyerail [Massenburg] was kind of hesitant and
    stand-offish, and kind of real reluctant to give con-
    sent to a pat down or a search of his person.

       ...

       Q: You indicated that Mr. Massenburg, you said,
    was acting nervously. What gave you that impres-
    sion?

       A: Like, I said, he was standing off from the three
    in the group from being questioned. He was reluc-
    tant, didn’t show any eye contact. Looked down.
    Once he stood back and stated, "I don’t need to get
    a pat-down." That kind of raised my suspicion a little
    further. And we were more persistent to find out
    whether he had weapons on his person.

J.A. 48-50. On cross-examination, Massenburg’s attorney
attempted to clarify Gaines’s ostensible particularized suspi-
cion concerning Massenburg.

    Q: And during your conversation with him, he
    wouldn’t look you in the eye?
                   UNITED STATES v. MASSENBURG               7
    A:   Correct.

    Q: And he just kept on saying, I don’t need to be
    patted down?

    A:   Yes.

    Q:   That made you more persistent?

    A:   It did.

    Q:   Because he didn’t want to be patted down?

    A: Correct. As I said, the others made statements
    when asked if they had weapons. Said, you can
    check me. And he was the only one to be reluctant.

    Q: You had no new information to know he was
    armed and dangerous but for the fact he didn’t want
    to be patted down?

    A: I mean the nature of the call and nature of [the]
    area.

    Q: You had no new information, did you, Officer,
    other than his repeated statements that he didn’t want
    to be patted down?

    A:   Besides the statements, the area of the call.

    Q: Right. Nothing new other than the area of the
    call?

    A:   Nothing, ma’am.

J.A. 57-59.
8                  UNITED STATES v. MASSENBURG
   The district court denied Massenburg’s suppression motion,
holding that the search was lawful. It found that reasonable
suspicion existed on the basis of six factors: (1) "a vague
report of shots fired"; (2) the four men were encountered
"roughly two blocks from the location of the reported shoot-
ing incident"1 and were the only people in the area; (3) this
was a "high-drug, high-crime area"; (4) Massenburg was "act-
ing nervously, looked down and refused to make eye contact
and stood off from the group"; (5) Massenburg "continued to
act strangely by making a series of two furtive move-
ments"—that is, he "took a step back away from Officer
Gaines, and he then began pantomiming a self pat-down
search"; (6) Gaines’s actions were informed by a "year’s
worth of practical experience serving as a law enforcement
officer." J.A. 73-75.

   After the denial of his suppression motion, Massenburg
entered a conditional guilty plea, reserving his right to appeal
the court’s ruling. Judgment was entered and he was sen-
tenced to 18 months in prison. He brought this timely appeal
challenging the suppression ruling. We exercise jurisdiction
pursuant to 28 U.S.C. § 1291.

                                  II.

  We review the district court’s legal conclusions de novo
and its factual findings for clear error. See United States v.
Day, 591 F.3d 679, 682 (4th Cir. 2010).

  To comport with the Fourth Amendment, even a "brief"
investigatory detention "must be supported at least by a rea-
sonable and articulable suspicion that the person seized is
    1
   The district court appears to have confused the location given by the
anonymous caller, which was four blocks from the encounter with
Massenburg, and the location reported by one of Massenburg’s compan-
ions, who acknowledged hearing shots fired from a passing car roughly
two blocks away.
                  UNITED STATES v. MASSENBURG                     9
engaged in criminal activity." Reid v. Georgia, 448 U.S. at
440; see United States v. Foster, 634 F.3d 243, 246 (4th Cir.
2011). Considering the totality of the circumstances, we are
to determine whether there was a sufficient objective, particu-
larized basis for suspecting the person seized of criminal
activity. United States v. Arvizu, 534 U.S. 266, 273 (2002).
Evidence that would support only "a mere ‘hunch’ is insuffi-
cient," though a reasonable basis need not establish probable
cause and may well "fall[ ] considerably short of satisfying a
preponderance of the evidence standard." Id. at 274 (quoting
Terry, 392 U.S. at 27); cf. United States v. Digiovanni, ___
F.3d ___, ___ (4th Cir. 2011) ("The reasonable suspicion
standard is an objective one, so we examine the facts within
the knowledge of [the officer] to determine the presence or
nonexistence of reasonable suspicion.").

   This quantum of suspicion is likewise required prior to a
frisk when the officer’s initial encounter with the citizen is
voluntary. See United States v. Burton, 228 F.3d 524, 528 (4th
Cir. 2000) ("[D]uring [initially consensual] police-citizen
encounters, an officer is not entitled, without additional justi-
fication, to conduct a protective search. To conduct such a
protective search, an officer must first have reasonable suspi-
cion supported by articulable facts that criminal activity may
be afoot."); see also Terry, 392 U.S. at 32-33 (Harlan, J., con-
curring) ("[I]f the frisk is justified in order to protect the offi-
cer during an encounter with a citizen, the officer must first
have constitutional grounds to insist on an encounter, to make
a forcible stop. . . . If and when a policeman has a right . . .
to disarm such a person for his own protection, he must first
have a right not to avoid him but to be in his presence. That
right must be more than the liberty . . . to address questions
to other persons, for ordinarily the person addressed has an
equal right to ignore his interrogator and walk away; he cer-
tainly need not submit to a frisk for the questioner’s protec-
tion.") (emphasis added). Thus we can assume without
deciding that Officer Fries’s initial conversation with Massen-
burg and his companions was consensual and that the Fourth
10               UNITED STATES v. MASSENBURG
Amendment was first implicated by Officer Gaines’s frisk of
Massenburg.

   We emphasize that the Constitution requires "a particular-
ized and objective basis for suspecting the particular person
stopped of criminal activity." United States v. Griffin, 589
F.3d 148, 152 (4th Cir. 2009) (quoting United States v. Cor-
tez, 449 U.S. 411, 417-18 (1981)) (emphases added). As the
Supreme Court noted in Cortez, "Chief Justice Warren, speak-
ing for the Court in Terry v. Ohio, said that, "[t]his demand
for specificity in the information upon which police action is
predicated is the central teaching of this Court’s Fourth
Amendment jurisprudence." Cortez, 449 U.S. at 418 (quoting
Terry, 392 U.S. at 21 n. 18 (emphasis added by Cortez)).
Indeed, as our late friend and colleague Judge Michael
reminded us in the 2010 Madison Lecture at New York Uni-
versity, "The Fourth Amendment owes its existence to furious
opposition in the American colonies to British search and sei-
zure practices . . . . Th[e] controversy [over the use of general
warrants] left citizens of the new American states with a deep-
dyed fear of discretionary searches permitted by general war-
rants and writs of assistance." The Honorable M. Blane
Michael, Reading the Fourth Amendment: Guidance from the
Mischief that Gave it Birth, 85 N.Y.U. L. Rev. 905, 907, 911-
12 (2010). Cf. Arizona v. Gant, 556 U.S. 332, ___, 129 S. Ct.
1710, 1720 (2009) (noting "the central concern underlying the
Fourth Amendment" is "the concern about giving police offi-
cers unbridled discretion to rummage at will among a per-
son’s private effects"); Delaware v. Prouse, 440 U.S. 648,
661 (1979) (holding unconstitutional a discretionary, suspi-
cionless stop for a "spot check" of a motorist’s license and
registration, emphasizing that "[t]his kind of standardless and
unconstrained discretion is the evil the Court has discerned
when in previous cases it has insisted that the discretion of the
official in the field be circumscribed").

                              III.

   On the facts of this case, there is precious little to sustain
the district court’s holding that Officer Gaines had reasonable,
                 UNITED STATES v. MASSENBURG                   11
particularized suspicion of Massenburg such that a noncon-
sensual frisk was lawful under the Fourth Amendment.
Among the six factors the district court cited in support of its
ruling is Officer Gaines’s one "year’s worth of practical expe-
rience serving as a law enforcement officer," which of course
is wholly unrelated to appellant. J.A. 74. The first three fac-
tors it listed—that the officers were responding to a "vague
report of shots fired," J.A. 73, that Massenburg was found in
the general vicinity (four blocks) of the reported site of the
gunfire, and that this encounter occurred in a high-crime
area—also do little to create particularized suspicion.

                               A.

   As the district court noted, the officers were responding to
"a vague report of shots fired." J.A. 73. This report was not
only "vague"—indicating only that eight shots were "possi-
bly" fired two blocks south of a certain intersection, J.A.
77—it was also anonymous. Reliance on an anonymous tip
may be reasonable where, "suitably corroborated, [it] exhibits
sufficient indicia of reliability." Florida v. J.L., 529 U.S. 266,
270 (2000). Yet here corroboration did not exist until one of
Massenburg’s       companions        reported     hearing    shots
fired—which cannot be said to increase reasonable suspicion
of the companion’s own party, especially since he also
reported that the shots were fired from a moving car (by
unknown parties) several blocks away. Like the tip of illegal
gun possession held unreliable in J.L., the tip here "provided
no predictive information and therefore left the police without
means to test the informant’s knowledge or credibility." Id. at
271. The tipster here disclosed her basis of knowledge—she
heard the shots herself—but little else. Though that disclosure
"enhance[s] the tip’s reliability," United States v. Perkins, 363
F.3d 317, 322 (4th Cir. 2004), we have held that even a
"nearly contemporaneous report" of a drug transaction the tip-
ster reportedly saw was unreliable in the absence of "[s]ome
corroboration," since "a fraudulent tipster can fabricate her
basis of knowledge," United States v. Reaves, 512 F.3d 123,
12                  UNITED STATES v. MASSENBURG
127-28 (4th Cir. 2008). Cf. Perkins 363 F.3d at 322, 327-28
(anonymous tip held sufficiently reliable where contempora-
neous viewing was corroborated by presence of a known drug
user in front of a known drug house and where tipster, though
she did not explicitly identify herself, was reasonably
assumed to be a known, reliable informant).2

   Furthermore, the poor match between the vague tip and the
individuals encountered substantially undermines reliance on
the tip for reasonable particularized suspicion of Massenburg.
The tip contained no physical description of the perpetrators
or any other outward identifying features; the only link
between the tip and Massenburg’s group was the group’s
rough proximity to the alleged site of the gunfire. The tipster
reported hearing shots two blocks south of the intersection of
Hull and 14th Streets; Massenburg and his friends were
encountered four blocks west of that intersection.
  2
    Though the threat of harassment that occupied the Court in J.L. may
seem substantially lessened here, where the tipster provided no physical
description or any other identifying information concerning the allegedly
armed person(s), this threat always exists in cases where the information
given by an anonymous tip is sufficiently specific to identify individuals.
See J.L., 529 U.S. at 272 (warning that an "automatic firearm exception
to our established reliability analysis would . . . enable any person seeking
to harass another to set in motion an intrusive, embarrassing police search
of the targeted person"). Since, for this issue to arise, individuals must
have been singled out on the basis of an anonymous tip, the possibility of
targeted harassment always exists, no matter how generic the tip itself may
appear. Just as the anonymous tipster in J.L. likely knew that there was
only one "young black male . . . wearing a plaid shirt" at the indicated bus
stop, id. at 268, the tipster here might well have known that the streets in
the indicated area were empty except for Massenburg and his friends.
   We also note that in Reaves, where we held an anonymous tip unreli-
able, the threat of harassment also appeared minimal. There the tipster,
who notified police after she saw what appeared to be a drug deal and
guided police as she followed the car of the alleged drug dealer for several
blocks, ceased pursuit when it came time to turn onto another street to
reach the market, where she was traveling on an errand. Reaves, 512 F.3d
at 125.
                  UNITED STATES v. MASSENBURG                    13
   Thus, while the district court appears to have heavily relied
on the fact that Massenburg and his companions were the only
people encountered as Officers Fries and Gaines responded to
the tip, this provides little basis for reasonable, particularized
suspicion of Massenburg. As J.L. and its progeny indicate,
when a tip lacks sufficient indicia of reliability, presence in
the area identified by the tip does not generate reasonable sus-
picion. Here, Massenburg was not even present at the site of
the alleged gunfire—he was encountered four blocks away.
Cf. United States v. Moore, 817 F.2d 1105, 1106 (4th Cir.
1987) (finding reasonable suspicion where only individual in
the vicinity was found "30 to 40 yards" from the entrance to
a building burglarized two to three minutes before, "moving
away from the scene of the crime"). To the extent that the tip,
together with Massenburg’s location, did identify his group
with particularity, J.L. and Reaves teach that an anonymous
tip, absent some corroboration or sufficient other indicia of
reliability, is not itself a reasonable basis for suspicion justify-
ing a nonconsensual frisk.

    The fact that this was a "high-drug, high-crime area" adds
little to the anonymous tip. J.A. 74. This counts among the
totality of the circumstances we consider, but it does little to
support the claimed particularized suspicion as to Massen-
burg. "An individual’s presence in an area of expected crimi-
nal activity, standing alone, is not enough to support a
reasonable, particularized suspicion that the person is commit-
ting a crime." Illinois v. Wardlow, 528 U.S. 119, 124 (2000);
see Brown v. Texas, 443 U.S. 47, 52 (1979). This is true
because "presence in a high crime neighborhood is a fact too
generic and susceptible to innocent explanation to satisfy the
reasonable suspicion inquiry." Wardlow, 528 U.S. at 139 (Ste-
vens, J., concurring in part and dissenting in part).

   As the officers testified, the city police "usually get com-
plaints . . . [for] random gunfire" in this area. J.A. 46. That
such incidents are common may make it more reasonable for
otherwise innocent behavior to appear suspicious to officers
14               UNITED STATES v. MASSENBURG
on the beat; but where a tip has already indicated that shots
were fired, the level of such crime in the neighborhood does
not provide an additional reasonable basis for suspicion of
particular individuals. That the tip concerned a common inci-
dent in a high-crime neighborhood does little to bolster its
reliability and less to create particularized suspicion. While
we appreciate the danger posed by firearms in our cities, the
Supreme Court has rejected "an automatic firearm exception
to our established reliability analysis." J.L., 529 U.S. at 272.
Like any other anonymous tip, a tip concerning firearms must
present certain indicia of reliability before it can provide a
basis for reasonable, particularized suspicion.

   To hold otherwise would be to authorize general searches
of persons on the street not unlike those conducted of old by
the crown against the colonists. Allowing officers to stop and
frisk any individuals in the neighborhood after even the most
generic of anonymous tips would be tantamount to permitting
a regime of general searches of virtually any individual resid-
ing in or found in high-crime neighborhoods, where "com-
plaints" of "random gunfire" in the night are all too "usual[ ]."
J.A. 46. James Otis famously decried general searches as "in-
struments of slavery . . . and villainy," which "place[ ] the lib-
erty of every man in the hands of every petty officer,"
warning against abuses by "[e]very man prompted by
revenge, ill humor, or wantonness." Timothy Lynch, In
Defense of the Exclusionary Rule, 23 Harv. J. L. & Pub. P.
711, 722 (2000) (quoting James Otis, Speech on the Writs of
Assistance (1761)). The Fourth Amendment, and the courts’
Fourth Amendment jurisprudence, is aimed at this evil. With-
out reasonable particularized suspicion of wrongdoing, such
searches and seizures offend the Constitution.

                               B.

   Reasonable suspicion determinations are made according to
the totality of the circumstances, and in light of the
above—Massenburg’s presence in a high-crime neighborhood
                 UNITED STATES v. MASSENBURG                  15
shortly after an (unreliable) tip concerning random gunfire in
the general vicinity—we give Officer Gaines a good deal of
leeway in his interpretation of Massenburg’s behavior. Yet, as
we recently reminded the Government in Foster, it cannot
simply proffer "whatever facts are present, no matter how
innocent, as indicia of suspicious activity." 634 F.3d at 248.
We expressed serious concerns there about "the way in which
the Government attempts to spin . . . mundane acts into a web
of deception," id.; these concerns are amplified when these
"mundane acts" are incident to the refusal to consent to a vol-
untary search.

   Officer Gaines made clear in his testimony that "it wasn’t
until actually I made contact with [Massenburg] that I noticed
nervous behavior from him." J.A. 48. His "blow-by-blow"
account of the encounter—which is not contradicted by Fries
or any other evidence—indicates that this "nervous behavior"
was his characterization of Massenburg’s repeated refusal to
consent to a voluntary pat-down: "We questioned if anybody
had any weapons on them. The individuals besides Massen-
burg stated, we don’t have anything, you can check us. And
Tyerail [Massenburg] was kind of hesitant and stand-offish,
and kind of real reluctant to give consent to a pat down or a
search of his person." J.A. 48. Gaines reiterated this when
asked a second time to describe Massenburg’s nervous behav-
ior:

    Like, I said, he was standing off from the three in the
    group from being questioned [sic]. He was reluctant,
    didn’t show any eye contact. Looked down. Once he
    stood back and stated, "I don’t need to get a pat-
    down. That kind of raised my suspicion a little fur-
    ther. And we were more persistent to find out
    whether he had weapons on his person.

J.A. 49-50 (emphases added). On cross-examination, Gaines
again explained that Massenburg "was the only one to be
reluctant" and admitted, when asked if it was true he had "no
16               UNITED STATES v. MASSENBURG
new information to know [Massenburg] was armed and dan-
gerous but for the fact he didn’t want to be patted down," that
there was "[n]othing" except Massenburg’s "statements" (he
"kept on saying, I don’t need to be patted down") and "the
area of the call." J.A. 57-59.

   The evidence Gaines cites for Massenburg’s nervousness is
slight: Massenburg was standing a foot or two from the other
three, who were lined up shoulder-to-shoulder, and "[l]ooked
down" or failed to make eye contact as Gaines repeatedly
asked him if he would consent to a search. The district court
accepted the Government’s characterization and deemed
Massenburg’s lack of eye contact "nervous behavior," yet as
Judge Gregory noted in United States v. Foreman, the Gov-
ernment often argues just the reverse: that it is suspicious
when "an individual looks or stares back at [officers]." 369
F.3d 776, 787 n.1 (4th Cir. 2004) (Gregory, J., concurring in
part and dissenting in part) (collecting cases); see also United
States v. McFarley, 991 F.2d 1188, 1192 (4th Cir. 1993) (not-
ing, in support of reasonable suspicion, that appellant and his
companion "each canvassed the terminal area, obtaining eye
contact with Officer Faulkenberry"). Given the complex real-
ity of citizen-police relationships in many cities, a young
man’s keeping his eyes down during a police encounter seems
just as likely to be a show of respect and an attempt to avoid
confrontation. Cf. State v. Scott, 412 So. 2d 988, 989 (La.
1982) ("Nervousness on the part of a black laborer when con-
fronted by an armed uniformed police officer does not seem
so unusual as to indicate guilt or criminal proclivity.")

   It is, of course, highly relevant when suspects "engage[ ] in
evasive behavior or act[ ] nervously." United States v. Mayo,
361 F.3d 802, 806 (4th Cir. 2004). Yet Massenburg did not
attempt to evade the officers—in fact, he and his companions
stopped to speak with Officer Fries, and one volunteered
information about recent gunfire. And looking down as an
officer persists in requesting consent to a search is a far cry
from the "unusually nervous behavior" we cited in United
                 UNITED STATES v. MASSENBURG                17
States v. Mayo, which included "shaking hands, heavy breath-
ing, and providing inconsistent answers." 861 F.3d at 806 (cit-
ing to United States v. McFarley, 991 F.2d 1188, 1192 (4th
Cir. 1993)). As the Tenth Circuit explained in United States
v. Salzano,

    [I]t is common for most people to exhibit signs of
    nervousness when confronted by a law enforcement
    officer whether or not the person is currently
    engaged in criminal activity. Thus, absent signs of
    nervousness beyond the norm, we will discount the
    detaining officer’s reliance on the detainee’s ner-
    vousness as a basis for reasonable suspicion.

158 F.3d 1107, 1113 (10th Cir. 1998) (internal quotation
marks and citations omitted). See also State v. Lee, 658
N.W.2d 669, 678-79 (Neb. 2003) ("[N]ervousness is of lim-
ited value" to reasonable suspicion analyses as "it is common
knowledge that most citizens whether innocent or guilty,
when confronted by a law enforcement officer who asks them
potentially incriminating questions are likely to exhibit some
signs of nervousness.").

   Indeed, the Supreme Court of Wyoming has applied this
commonsense principle to a situation much like this one,
where an officer was asking a motorist for consent to search
his car and, upon the motorist’s refusal, continued to ask him
"whether there was some reason he did not want the officer
looking in the vehicle." Damato v. State, 64 P.3d 700, 709
(Wyo. 2003). Reasoning that "[r]ealistically, few citizens
would not have become uncomfortable to some degree with
these questions," the court discounted as a "factor of no sig-
nificance" far more extreme signs of nervousness, including
the motorist’s "sweating heavily although it was a chilly day,
his carotid artery pulsating hard and fast, and an inability to
keep eye contact." Id.

  And as a reasonable response to continued police question-
ing, looking down is a good deal more innocent than the
18                 UNITED STATES v. MASSENBURG
defendant’s actions in United States v. Sprinkle, where the
defendant "put his head down and his hand up to his face as
if to avoid recognition" as an officer passed the car and then
"drove away as soon as the officers walked by." 106 F.3d 613,
617 (4th Cir. 1997). In Sprinkle we found no reasonable sus-
picion existed, even though the officers knew the defendant
to have been recently released from prison following narcotics
convictions, defendant was in a neighborhood known for drug
trafficking, and his evasive behavior was preceded by some-
one else’s entering the car and making gestures consistent
with a covert exchange ("huddling" with the two men’s hands
"close[ ] together" as if to pass something). Id. at 615-16.
When we have held that behavior far more extreme, by a
known narcotics dealer, in a high-crime area does not create
reasonable suspicion, it is difficult to imagine that Massen-
burg’s keeping his eyes down as he is asked repeatedly to
consent to a voluntary search would suffice.

   Indeed, we are especially conscious here of the fact that
Massenburg’s looking down was incident to his repeated
refusal to consent to a voluntary search. It cannot be doubted
that "a refusal to cooperate [with a police request to conduct
a voluntary search], without more, does not furnish the mini-
mal level of objective justification needed for a detention or
seizure." Florida v. Bostick, 501 U.S. 429, 437 (1991); see
also Mayo, 361 F.3d at 806 ("A suspect’s refusal to cooperate
with police, without more, does not satisfy Terry stop require-
ments."). If the ordinary response of the innocent upon being
asked to consent to a search—some mild nervous-
ness—sufficed to create reasonable suspicion, then Terry’s
reasonable suspicion requirement would become meaningless:
officers could ask a citizen for permission to conduct a volun-
tary search, and, if denied, they could use the citizen’s denial
as evidence of criminal activity and perform the search any-
way. Though, as an analytic matter, nervousness can be sepa-
rated from the denial of consent itself,3 to attempt to extricate
  3
   Indeed, the suggestion in Bostick that the refusal to cooperate may go
even some of the way toward establishing reasonable suspicion is best
read to refer to these sorts of indicators. See Bostick, 501 U.S. at 437.
                 UNITED STATES v. MASSENBURG                   19
the very mildest indicators of nervousness—such as a failure
to maintain eye contact during the refusal, as the officer
becomes "more persistent," J.A. 50—from the denial itself is
too nice a matter. Virtually any denial will be accompanied by
these mild reactions to the request, and thus virtually any
denial would go much of the way toward authorizing a non-
consensual search. This cannot be the case.

   As for the district court’s characterization of Massenburg’s
"self-pat down" as "[f]urtive movements," J.A. 74, it recalls
the Government’s suggestion in Foster that a man’s "sud-
den[ly]" "pop[ping] up" in a car with "his arms going hay-
wire" was suspicious. Foster, 634 F.3d at 247. There we
warned against "using whatever facts are present, no matter
how innocent, as indicia of suspicious activity," and reminded
the Government that it "must do more than simply label a
behavior as ‘suspicious’ to make it so": "The Government
must also be able to either articulate why a particular behavior
is suspicious or logically demonstrate, given the surrounding
circumstances, that the behavior is likely to be indicative of
some more sinister activity than may appear at first glance."
Id. at 248. No such demonstration has been forthcoming.
Massenburg’s "self-pat down" was interpreted as such by
Officer Gaines, and as an obvious attempt to satisfy him with-
out consenting to a frisk, it provided little basis, if any, as a
matter of constitutional analysis, for a reasonable suspicion of
wrongdoing.

   Genuinely suspicious behavior, occurring in a high-crime
neighborhood after a tip concerning gunfire, would certainly
justify a Terry stop and almost certainly a frisk of the
detainee. Where that tip is unreliable, the question becomes
closer. But where the accompanying behavior—the only sub-
stantial basis for particularized suspicion—is simply a mild
reaction to repeated requests to relinquish one’s constitutional
right to be free from unreasonable searches, it is clear that rea-
sonable, particularized suspicion of criminal activity does not
exist.
20                  UNITED STATES v. MASSENBURG
                                   IV.

    The Government suggests that under the collective-
knowledge doctrine (also called the "fellow officer" rule)
Officer Fries’s observation of a bulge in Massenburg’s jacket
pocket should be imputed to Officer Gaines, though, as the
Government concedes, Fries never "inform[ed]" Gaines about
it. Br. of Appellee, at 16 n.1.4 Because this novel application
of the doctrine would stretch it well beyond its purpose, we
decline to do so.

   The collective-knowledge doctrine, as enunciated by the
Supreme Court, holds that when an officer acts on an instruc-
tion from another officer, the act is justified if the instructing
officer had sufficient information to justify taking such action
herself; in this very limited sense, the instructing officer’s
knowledge is imputed to the acting officer. In Whiteley v.
Warden, the Supreme Court recognized in dicta that "officers
called upon to aid other officers in executing arrest warrants
are entitled to assume that the officers requesting aid" had
probable cause to support the issue of the warrant. 401 U.S.
560, 568 (1971). The Court applied this principle in United
States v. Hensley, holding that where officers stopped defen-
dant "in objective reliance" on a flyer from another depart-
ment that explained that defendant was wanted in connection
with an aggravated robbery and requested that other police
   4
     During cross-examination, Fries said that after seeing the bulge he
"made a movement towards him [Gaines? Massenburg?], but that is a
hand gesture, maybe," "[a]t best." J.A. 43. There was no serious conten-
tion by Fries that he communicated his observation to Gaines, see J.A. 32;
he admitted he "didn’t alert" Gaines. J.A. 43. The Government has con-
ceded this point: it relegates discussion of the bulge to a footnote, where
it admits that "before [Fries] could inform Officer Gaines, Gaines began
performing a pat-down of Massenburg." Br. of Appellee, at 16 n.1. More
importantly, Officer Gaines made no mention in his testimony of seeing
a sign or signal from Fries. Accordingly, we conclude that Fries’s observa-
tion of the "bulge" was not communicated to Gaines at the time he under-
took his search.
                 UNITED STATES v. MASSENBURG                  21
departments "pick up and hold" him, the stop was justified if
and only if the officers who issued the request had reasonable,
particularized suspicion sufficient to justify their own stop:

    We conclude that, if a flyer or bulletin has been
    issued on the basis of articulable facts supporting a
    reasonable suspicion that the wanted person has
    committed an offense, then reliance on that flyer or
    bulletin justifies a stop . . . . If the flyer has been
    issued in the absence of a reasonable suspicion, then
    a stop in the objective reliance upon it violates the
    Fourth Amendment.

469 U.S. 221, 223, 232 (1985) (internal citations omitted).

   We have applied the collective-knowledge doctrine often,
both before and after Whiteley and Hensley, and our case law
likewise establishes that the doctrine has a limited domain:
officers acting on the information and instructions of other
officers. In United States v. Pitt, federal police agent Wurms
learned through an informant that a large quantity of heroin
was being driven from New York City to Washington, D.C.
382 F.2d 322 (4th Cir. 1967). Agent Wurms informed fellow
agents, including Agent Worden, and instructed Baltimore
City police to intercept the car. Pitt was arrested by Agent
Worden, with the assistance of city police. Rejecting Pitt’s
claim that Worden lacked personal knowledge of the facts
constituting probable cause, we noted that "[p]robable cause
. . . can rest upon the collective knowledge of the police,
rather than solely on that of the officer who actually makes
the arrest." Id. at 324. Though this shorthand reference to the
collective-knowledge doctrine might be misleading out of
context, we went on in the next sentence to explain that "[i]t
was enough that Agent Wurms reported to Agent Worden the
substance of his telephone conversation with the informant."
Id.

  In our discussion of the doctrine in United States v. Laugh-
man, we made its limitations explicit:
22               UNITED STATES v. MASSENBURG
        The law seems to be clear that so long as the offi-
     cer who orders an arrest or search has knowledge of
     facts establishing probable cause, it is not necessary
     for the officers actually making the arrest or con-
     ducting the search to be personally aware of those
     facts.

        [N.3] When a superior officer orders another offi-
     cer to make an arrest, it is proper to consider the
     superior’s knowledge in determining whether there
     was probable cause. Likewise, when a group of
     agents in close communication with one another
     determines that it is proper to arrest an individual,
     the knowledge of the group that made the decision
     may be considered in determining probable cause,
     not just the knowledge of the individual officer who
     physically effected the arrest. [collecting cases]

618 F.2d 1067, 1072-73 & n.3 (4th Cir. 1980) (emphasis
added). Again, the collective-knowledge doctrine simply
directs us to substitute the knowledge of the instructing offi-
cer or officers for the knowledge of the acting officer; it does
not permit us to aggregate bits and pieces of information from
among myriad officers, nor does it apply outside the context
of communicated alerts or instructions. See 2 Wayne R.
LaFave, Search and Seizure § 3.5(b) (4th ed. 2004) ("[U]nder
the Whiteley rule (or, as it is sometimes termed, the ‘fellow
officer’ rule) police are in a limited sense ‘entitled to act’
upon the strength of a communication through official chan-
nels directing or requesting that an arrest be made."); cf.
United States v. Wells, 98 F.3d 808, 810 (4th Cir. 1996)
("[A]lthough the agent who actually seized the weapon pursu-
ant to the supervising agent’s instructions had no personal
knowledge that Wells was a convicted felon, it is sufficient
that the agents collectively had probable cause to believe the
weapon was evidence of a crime at the time of the seizure.")
(emphasis added); United States v. Gaither, 527 F.2d 456,
458 (4th Cir. 1975) (quoting Pitt to support application of
                 UNITED STATES v. MASSENBURG                   23
collective-knowledge doctrine where arresting officer was
"acting on" a "‘flash’ bulletin" issued by FBI agents who had
just observed a bank robbery).

   The Government would have us recognize a far more
expansive rule, which would look to the aggregated knowl-
edge of all officers involved to determine if reasonable suspi-
cion or probable cause existed. Under this proposed rule, it
would be irrelevant that no officer had sufficient information
to justify a search or seizure. It would be irrelevant that no
officer believed any other officer had pertinent information,
and thus that the acting officer undertook a search or seizure
she should have believed to be illegal. Indeed, as this aggrega-
tion rule is only required when the information at issue has
not been communicated to other officers (as the "aggregation"
it concerns is judicial, after-the-fact aggregation, not an acting
officer’s reliance on instructions or information conveyed by
another officer), this would be the paradigmatic case. Were
we to adopt this rule, the legality of the search would depend
solely on whether, after the fact, it turns out that the disparate
pieces of information held by different officers added up to
reasonable suspicion or probable cause.

   The Tenth Circuit has helpfully distinguished "‘vertical’
collective knowledge relationships in which [one] officer’s
conclusion [i]s conveyed" to others who effect the seizure
from a "‘horizontal’ collective knowledge relationship in
which the knowledge of several officers must be aggregated
to create probable cause." United States v. Rodriguez-
Rodriguez, 550 F.3d 1223, 1228 n.5 (10th Cir. 2008). No case
from the Supreme Court or from our own court has ever
expanded the collective-knowledge doctrine beyond the con-
text of information or instructions communicated
("vertically") to acting officers. Some of our sister courts have
authorized "horizontal" aggregation of uncommunicated
information. See United States v. Ramirez, 473 F.3d 1027,
1032-33 (9th Cir. 2007) (collecting cases). Because we
believe that this expansive aggregation rule strays from the
24               UNITED STATES v. MASSENBURG
purposes of the collective-knowledge doctrine recognized by
the Supreme Court and promotes none of the proper ends of
law enforcement, we decline to follow them.

   The rationale behind the Supreme Court’s collective-
knowledge doctrine is, as the Court noted in Hensley, "a mat-
ter of common sense: [the rule] minimizes the volume of
information concerning suspects that must be transmitted to
other jurisdictions [or officers] and enables police . . . to act
promptly in reliance on information from another jurisdiction
[or officer]." Hensley, 469 U.S. at 231. Thus, law enforcement
efficiency and responsiveness would be increased: Police
department search-and-seizure training would soon reflect
Hensley’s rule, and officers would learn that they need not
relay the information justifying an alert when issuing one nor
wait for such information upon hearing one.

   The Government’s proposed aggregation rule serves no
such ends. Because it jettisons the present requirement of
communication between an instructing and an acting officer,
officers would have no way of knowing before a search or
seizure whether the aggregation rule would make it legal, or
even how likely that is. The officer deciding whether or not
to perform a given search will simply know that she lacks
cause; in ordinary circumstances, she will have no way of
estimating the likelihood that her fellow officers hold enough
uncommunicated information to justify the search. And as an
officer will never know ex ante when the aggregation rule
might apply, the rule does not allow for useful shortcuts when
an officer knows an action to be legal, as Hensley did. Per-
haps an officer who knows she lacks cause for a search will
be more likely to roll the dice and conduct the search anyway,
in the hopes that uncommunicated information existed. But as
this would only create an incentive for officers to conduct
searches and seizures they believe are likely illegal, it would
be directly contrary to the purposes of longstanding Fourth
Amendment jurisprudence.
                   UNITED STATES v. MASSENBURG                       25
   As the Supreme Court recently reaffirmed in Davis v.
United States, the exclusionary rule’s "sole purpose . . . is to
deter future Fourth Amendment violations." ___ U.S. ___,
___, 131 S. Ct. 2419, 2426 (2011). It targets police action that
"exhibit[s] deliberate, reckless, or grossly negligent disregard
for Fourth Amendment rights"—in these cases the "deterrent
value of exclusion is strong and tends to outweigh the result-
ing costs." Id. at 2427 (internal quotation marks omitted). As
the Government’s proposed aggregation rule would do noth-
ing but redeem searches or seizures that the acting officers
should have believed at the time to be unlawful, it would
serve only to erode that deterrence. The Davis Court further
broadened the "good-faith" exception to the exclusionary rule,
recognizing that "when the police act with an objectively rea-
sonable good-faith belief that their conduct is lawful . . . the
deterrence rationale loses much of its force." Id. at 2427-28.
The Government’s proposed aggregation rule would per-
versely reward officers acting in bad faith according to the
result of an after-the-fact aggregation inquiry that is simply
academic.

   Though we have studied our sister circuits’ cases adopting
an aggregation rule, we can find no convincing defense of it.5
Most courts to have adopted the rule appear to have done so
simply on the grounds that officers working closely together
are "a team," United States v. Terry, 400 F.3d 575, 581 (8th
Cir. 2005); United States v. Edwards, 885 F.2d 377, 383 (7th
Cir. 1989), or, as one court put it, "on the theory that officers
working closely together during a stop or an arrest can be
treated as a single organism," United States v. Shareef, 100
F.3d 1491, 1504 & n.6 (10th Cir. 1996) (considering this
rationale after rejecting a general aggregation rule). But why?
We must frame the question in terms of deterrence, and for
the purposes of deterrence we look to each individual offi-
cer’s decision-making process as she considers executing a
  5
   For collections of these cases, see Ramirez, 473 F.3d at 1032-33, and
Bailey v. Newland, 263 F.3d 1022, 1031-32 (9th Cir. 2001).
26                   UNITED STATES v. MASSENBURG
search or effecting a seizure. Where officers working closely
together have not communicated pertinent information, the
acting officer weighs the costs and benefits of performing the
search in total ignorance of the existence of that informa-
tion—it is not known to her, so it cannot enter into the calcu-
lus. Therefore, for purposes of the exclusionary rule, that
additional information must be irrelevant.6

   Furthermore, if the "team" or "single organism" theory
should apply when the information at issue is incriminating,
should it not apply when the information is exculpatory? Yet,
we held in United States v. Holmes that the collective-
knowledge doctrine does not impute uncommunicated excul-
patory knowledge to fellow officers in similar circumstances.
376 F.3d 270, 277 n.3 (4th Cir. 2004). Likewise, though most
courts to allow aggregation have required "some degree of
communication" among the officers, Terry, 400 F.3d at 581,
see also Ramirez, 473 F.3d at 1032-33, it is not clear why. If
the Fourth Amendment is satisfied when, unbeknownst to the
officer conducting a search, a fellow officer on the scene has
the information necessary to justify it, why should the analy-
sis change when the other officer is not on the scene? Yet we
recently held in United States v. Blauvelt that information
held by others in the "law enforcement community at large"
is not imputed to members of a particular investigative team.
638 F.3d 281, 289 (4th Cir. 2011). Cf. People v. Hazelhurst,
662 P.2d 1081, 1087 (Colo. 1983) ("The fellow officer rule,
however, is not a means of creating probable cause by using
  6
    It is true that in the "vertical" collective-knowledge context the acting
officer is ignorant of the actual information held by the instructing officer.
But there the instruction itself communicates to the acting officer that the
instructing officer believes that she has sufficient information to justify the
action; after Hensley, police procedure can have the acting officer defer to
the instructing officer. Thus, the only officer making a reasonable suspi-
cion or probable cause determination is the instructing officer, and she will
be deterred by potential application of the exclusionary rule from ordering
an illegal search in the same way that an officer executing her own search
would be.
                 UNITED STATES v. MASSENBURG                  27
post hoc combinations of information available to the police.
The rule does not permit the police to cull its archives in
hopes of justifying an arrest which is not supported by proba-
ble cause.")

   Because we believe the aggregation rule runs contrary to
the Supreme Court’s Fourth Amendment jurisprudence,
would seriously erode the efficacy of the exclusionary rule’s
deterrent purposes, and serves none of the legitimate ends of
law enforcement, we reject it. We do not impute Officer
Fries’s observation of a "bulge" in Massenburg’s jacket
pocket to Officer Gaines, and thus, for the reasons stated
above, we hold that Gaines lacked the reasonable suspicion
needed to conduct a lawful nonconsensual frisk. Accordingly,
the district court erred when it failed to suppress the fruits of
that unlawful search.

                               V.

   For the reasons set forth herein, the judgment is vacated,
the district court’s order denying the motion to suppress is
reversed, and the case is remanded for further proceedings
consistent with this opinion.

                 VACATED, REVERSED, AND REMANDED

```

---

## GROUP: _overhaul2/lake/cases/United States v. Mathis.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Mathis"
type: case
citation: "767 F.3d 1264 (2014)"
parallel_cite: ""
neutral_cite: "2014 U.S. App. LEXIS 18297; 2014 WL 4724697"
court: "U.S. Court of Appeals, Eleventh Circuit"
court_level: coa
circuit: 11th
year: 2014
date_decided: 2014-09-24
docket: ""
authority_weight: "Binding in-circuit — 11th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: null
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Mathis
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2736649/united-states-v-arnold-maurice-mathis/"
  cluster_id: 2736649
  opinion_id: 2736649
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Leon]]", "[[Massachusetts v. Sheppard]]", "[[United States v. Jackson]]", "[[Riley v. California]]"]
aliases: ["United States v. Mathis (11th Cir. 2014)", "United States v. Arnold Maurice Mathis"]
tags: ["case", "fourth-amendment", "exclusionary-rule", "good-faith-exception", "leon", "phone-search", "eleventh-circuit"]
holding: "Even assuming the search warrant lacked probable cause, the Leon good-faith exception applied: the detective had an objectively…"
lake:
  record_id: United States v. Mathis
  status: verified
  projected_at: 2026-07-06
---

# United States v. Mathis

*767 F.3d 1264 (11th Cir. 2014)* · U.S. Court of Appeals, Eleventh Circuit · **Binding in-circuit — 11th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Detective Vizcarrondo obtained a warrant to search Arnold Mathis's smartphone, and the search produced incriminating evidence. Mathis moved to suppress, arguing the affidavit failed to establish probable cause to search the phone. The district court denied the motion; Mathis was convicted and appealed.

## Issue
Whether, even assuming the warrant to search Mathis's phone was not supported by probable cause, the [[United States v. Leon]] [[The Good-Faith Exception|good-faith exception]] barred suppression of the evidence obtained from the phone.

## Rule
Yes. Where officers obtain and execute a warrant in objectively reasonable, good-faith reliance, the *[[United States v. Leon|Leon]]* [[The Good-Faith Exception|good-faith exception]] applies even if the warrant turns out to lack probable cause. "Alternatively, even if the search warrant was not supported by probable cause, evidence obtained from the search of Mathis's phone was not subject to suppression under the good faith exception to the exclusionary rule." — 767 F.3d at 1276. ^pin-1276

The standard is objective good faith, judged by whether any of the *[[United States v. Leon|Leon]]* exceptions applies: "Because the officers engaged in 'objectively reasonable law enforcement activity and . . . acted in good faith when obtaining [the] search warrant . . . the *Leon* good faith exception applies.'" — *Id.* at 1277. ^pin-1277

## Application
On these facts good faith saved the phone evidence. Nothing showed that Detective Vizcarrondo "was dishonest or reckless in preparing her affidavit or that she could not have harbored an objectively reasonable belief in the existence of probable cause," so the *[[Franks v. Delaware|Franks]]* exception did not apply, and the affidavit was not so lacking in indicia of probable cause as to make reliance unreasonable. Because the officers acted in objectively reasonable, good-faith reliance on the warrant a magistrate had issued, the evidence from the phone search was admissible regardless of whether the warrant ultimately established probable cause — the court did not need to resolve the probable-cause question to affirm.

## Conclusion
Even assuming the warrant lacked probable cause, the *[[United States v. Leon|Leon]]* [[The Good-Faith Exception|good-faith exception]] applied and the phone evidence was admissible; the denial of suppression was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 11th Cir.**
- No negative subsequent treatment identified. The decision applies [[United States v. Leon]] / [[Massachusetts v. Sheppard]] objective good-faith reliance to a phone-search warrant, paralleling [[United States v. Jackson]] (8th Cir.); the underlying warrant requirement for cell phones is governed by [[Riley v. California]].

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Mathis*, 767 F.3d 1264 (11th Cir. 2014) — https://www.courtlistener.com/opinion/2736649/united-states-v-arnold-maurice-mathis/ — pinpoints: 1276, 1277.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "523b7ba125089681", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Mathis"}, "payload": {"all": [{"cite": "767 F.3d 1264", "page": "1264", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "767"}, {"cite": "2014 U.S. App. LEXIS 18297", "page": "18297", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2014"}, {"cite": "2014 WL 4724697", "page": "4724697", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2014"}], "display": "767 F.3d 1264", "official": {"cite": "767 F.3d 1264", "page": "1264", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "767"}, "official_selection_present": true, "record_id": "United States v. Mathis"}}
{"assertion_id": "8f1d86043a35c3a3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1277", "record_id": "United States v. Mathis"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1277", "pinpoint_status": "slip-only", "quote": "Because the officers engaged in 'objectively reasonable law enforcement activity and . . . acted in good faith when obtaining [the] search warrant . . . the *Leon* good faith exception applies.'", "quote_fidelity": "mismatch", "record_id": "United States v. Mathis", "star_marker": null}}
{"assertion_id": "eaaa4bfde80d9e7b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1276", "record_id": "United States v. Mathis"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1276", "pinpoint_status": "slip-only", "quote": "--- # United States v. Mathis *767 F.3d 1264 (11th Cir. 2014)* · U.S. Court of Appeals, Eleventh Circuit · **Binding in-circuit — 11th Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Detective Vizcarrondo obtained a warrant to search Arnold Mathis's smartphone, and the search produced incriminating evidence. Mathis moved to suppress, arguing the affidavit failed to establish probable cause to search the phone. The district court denied the motion; Mathis was convicted and appealed. ## Issue Whether, even assuming the warrant to search Mathis's phone was not supported by probable cause, the [[United States v. Leon]] good-faith exception barred suppression of the evidence obtained from the phone. ## Rule Yes. Where officers obtain and execute a warrant in objectively reasonable, good-faith reliance, the *Leon* good-faith exception applies even if the warrant turns out to lack probable cause.", "quote_fidelity": "mismatch", "record_id": "United States v. Mathis", "star_marker": null}}
{"assertion_id": "fec20d67e0d0c461", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Mathis"}, "payload": {"as_of_content": null, "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Mathis", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Mathis

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Mathis",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Arnold Maurice Mathis",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Arnold Maurice MATHIS, Defendant-Appellant",
    "input_case_name": "United States v. Mathis",
    "court": "U.S. Court of Appeals, Eleventh Circuit",
    "court_id": "ca11",
    "court_level": "coa",
    "circuit": "11th",
    "state": null,
    "date_decided": "2014-09-24",
    "year": 2014,
    "docket": null,
    "cluster_id": 2736649,
    "lead_opinion_id": 2736649,
    "sibling_ids": [
      2736649
    ],
    "absolute_url": "/opinion/2736649/united-states-v-arnold-maurice-mathis/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "767 F.3d 1264",
      "volume": "767",
      "reporter": "F.3d",
      "page": "1264",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2014 U.S. App. LEXIS 18297",
        "volume": "2014",
        "reporter": "U.S. App. LEXIS",
        "page": "18297",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 4724697",
        "volume": "2014",
        "reporter": "WL",
        "page": "4724697",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "767 F.3d 1264",
        "volume": "767",
        "reporter": "F.3d",
        "page": "1264",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 U.S. App. LEXIS 18297",
        "volume": "2014",
        "reporter": "U.S. App. LEXIS",
        "page": "18297",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 4724697",
        "volume": "2014",
        "reporter": "WL",
        "page": "4724697",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "767 F.3d 1264",
    "official_selection": {
      "court_class": "coa",
      "selected": "767 F.3d 1264",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1276",
      "page": null,
      "quote": "--- # United States v. Mathis *767 F.3d 1264 (11th Cir. 2014)* \u00b7 U.S. Court of Appeals, Eleventh Circuit \u00b7 **Binding in-circuit \u2014 11th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Detective Vizcarrondo obtained a warrant to search Arnold Mathis's smartphone, and the search produced incriminating evidence. Mathis moved to suppress, arguing the affidavit failed to establish probable cause to search the phone. The district court denied the motion; Mathis was convicted and appealed. ## Issue Whether, even assuming the warrant to search Mathis's phone was not supported by probable cause, the [[United States v. Leon]] good-faith exception barred suppression of the evidence obtained from the phone. ## Rule Yes. Where officers obtain and execute a warrant in objectively reasonable, good-faith reliance, the *Leon* good-faith exception applies even if the warrant turns out to lack probable cause.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1277",
      "page": null,
      "quote": "Because the officers engaged in 'objectively reasonable law enforcement activity and . . . acted in good faith when obtaining [the] search warrant . . . the *Leon* good faith exception applies.'",
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
    "composite_basis_ref": "United States v. Mathis",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Wilson",
          "cluster_id": 10680152,
          "cite": [
            "884 S.E.2d 298",
            "315 Ga. 613"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mathis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. LEDBETTER (And Vice Versa)",
          "cluster_id": 10680366,
          "cite": [
            "899 S.E.2d 222",
            "318 Ga. 457"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mathis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Federal Trade Commission v. Steven J. Dorfman",
          "cluster_id": 9371119,
          "cite": [
            "58 F.4th 1322"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mathis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Randal Wise",
          "cluster_id": 10382388,
          "cite": [
            "134 F.4th 745"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mathis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Washington v. Zachary James Fairley",
          "cluster_id": 4727836,
          "cite": [
            "457 P.3d 1150"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mathis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dusty J. Cowan v. State of Alaska",
          "cluster_id": 10161720,
          "cite": [
            "559 P.3d 627"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mathis:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2736649) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca11)",
        "reviewed": 1,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 1,
        "triage_read": 0,
        "triage_snippet_classified": 1
      },
      "lane2_top_cited": {
        "query": "cites:(2736649)",
        "reviewed": 6,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 6,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(2736649)",
        "reviewed": 3,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 3,
        "triage_read": 0,
        "triage_snippet_classified": 3
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2736649)",
    "indexed_citing_opinions": 6,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2736649,
        "count": 6,
        "count_source": "search"
      }
    ],
    "citation_count": 53,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-mathis.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 6,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2736649,
        "cited_id": 1990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 75800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 75908,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 76294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 76840,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 77529,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 78058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 78534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 109925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 118188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 118381,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 134724,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 145922,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 147511,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 204288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 392842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 396175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 608150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 622315,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 626752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 657263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 670638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 677467,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 772987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 790000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 903985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2736649,
        "cited_id": 1840522,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "CU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T01:29:48Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:30:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:30:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:32:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:30:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Mathis

```
           Case: 13-13109   Date Filed: 09/24/2014   Page: 1 of 42


                                                                     [PUBLISH]



            IN THE UNITED STATES COURT OF APPEALS

                     FOR THE ELEVENTH CIRCUIT
                       ________________________

                             No. 13-13109
                       ________________________

               D.C. Docket No. 8:12-cr-00457-SCB-MAP-1



UNITED STATES OF AMERICA,

                                                               Plaintiff-Appellee,

                                   versus

ARNOLD MAURICE MATHIS,

                                                          Defendant-Appellant.

                       ________________________

                Appeal from the United States District Court
                    for the Middle District of Florida
                      ________________________

                            (September 24, 2014)



Before HULL, MARCUS and BLACK, Circuit Judges.

PER CURIAM:
              Case: 13-13109     Date Filed: 09/24/2014    Page: 2 of 42


      Arnold Maurice Mathis, a registered sex offender, enticed a minor to engage

in sexual activity in 2004. Seven years later, in 2011, he attempted to convince a

minor to take sexually explicit pictures and send them to him via text message, and

he actually succeeded in convincing a different minor to do so. Based on this

conduct, a jury convicted Mathis of several child exploitation offenses and the

district court sentenced him to a 480-month total term of imprisonment. On

appeal, Mathis raises numerous challenges to his convictions and sentences, which

we address in turn. After a thorough review of the record and consideration of the

parties’ briefs, and with the benefit of oral argument, we affirm Mathis’s

convictions and sentences. However, we remand to the district court for the

limited purpose of correcting a scrivener’s error in the judgment.

                                 I. BACKGROUND

A. Mathis’s Sexual Abuse of Jarvis J. and Subsequent Arrest

      In 2004, Mathis, who was approximately 34 years old, approached Jarvis J.

after a high school basketball game. Jarvis was 14 years old at the time. Mathis

introduced himself as Pastor Maurice and gave Jarvis approximately $20 to

purchase items at the concession stand. Mathis also told Jarvis that he was willing

to act as a father figure or mentor and that he could assist Jarvis financially by

helping him purchase shoes and clothes. Mathis gave Jarvis his cell phone number

and told Jarvis to call him the next day.


                                            2
              Case: 13-13109    Date Filed: 09/24/2014   Page: 3 of 42


      At some point the following week, Jarvis met Mathis and Mathis gave him a

pair of shoes, a shirt, and $100 to purchase a prepaid cell phone. Jarvis

subsequently purchased a cell phone, phone card, and minutes for the phone.

Jarvis used the phone to talk to Mathis, and the two met a few days after Jarvis

bought the phone. On that occasion, after going to a fast food restaurant, Mathis

took Jarvis to Mathis’s house where Mathis eventually goaded Jarvis into showing

him his penis. Mathis then performed oral sex on Jarvis. Mathis told Jarvis not to

tell anyone about the encounter and promised that he would give Jarvis money and

take care of him. Mathis took Jarvis to an ATM and gave him money.

      Following the incident at Mathis’s house, Jarvis used his cell phone to talk

to Mathis on a daily basis. During his conversations with Jarvis, Mathis became

more explicit and told Jarvis that he wanted to engage in sexual conduct with him.

Mathis eventually met Jarvis again and, after having a meal, Mathis took Jarvis to

Mathis’s house. Mathis performed oral sex on Jarvis and instructed him to

perform anal sex on Mathis. Jarvis complied with Mathis’s instructions.

      Sometime thereafter, Mathis talked to Jarvis on the phone about traveling to

Orlando to go bowling. When Mathis arrived to pick up Jarvis, Jarvis observed

another man in the car with Mathis as well as a boy around Jarvis’s own age. The

group drove to Orlando, but instead of going bowling, they went to a diner and




                                          3
              Case: 13-13109     Date Filed: 09/24/2014   Page: 4 of 42


then a hotel. At the hotel, Mathis performed oral sex on Jarvis and had Jarvis

perform anal sex on him while the other boy performed anal sex on the other man.

      Subsequently, Mathis took Jarvis to a townhouse in Lakeland and tried to

perform oral sex on him, but Jarvis resisted. Jarvis did not tell anyone about his

experiences with Mathis until December 2011, nearly seven years later. At that

time, Jarvis ran into the other man who had gone with him and Mathis to Orlando.

After arguing with the man in a store, Jarvis talked to his pastor and then went to

the Polk County Sheriff’s Office. At the sheriff’s office, Jarvis told Sergeant

James Evans and Detective Zoe Vizcarrondo about his experiences with Mathis.

Detective Vizcarrondo asked Jarvis to make a recorded phone call to Mathis.

During the call, Mathis acknowledged that he had engaged in sexual conduct with

Jarvis.

      A few hours after Jarvis’s recorded call with Mathis, law enforcement

officers arrested Mathis. During the arrest, officers seized Mathis’s cell phone,

which was a Sprint smartphone.

B. The Search of Mathis’s Smartphone

      After Mathis was arrested, Detective Vizcarrondo obtained a search warrant

for the contents of his cell phone. In support of her application for a search

warrant, Detective Vizcarrondo submitted an affidavit which provided in pertinent

part that the victim in the case, Jarvis, was 21 years old and that when he was


                                          4
              Case: 13-13109     Date Filed: 09/24/2014   Page: 5 of 42


between the ages of 14 and 15, Mathis sexually abused him. The affidavit

explained that, according to Jarvis, Mathis continuously called him from Mathis’s

cell phone and that Mathis would also communicate with him via text message.

Detective Vizcarrondo stated that Mathis had maintained the same phone number

since the time of the crimes, and that a forensic examination of the phone would

reveal a log of the recorded phone call between Jarvis and Mathis. In addition,

Detective Vizcarrondo averred that, based on her knowledge, experience, and

training in child sexual abuse investigations,

      [T]here are certain characteristics common to many individuals
      involved in the communication made between the suspect and victim
      of such investigations. These suspects sometimes possess and
      maintain “soft copies” of such communication in the privacy and
      security of their personal cell phones and retain these items for many
      years. They often conceal such correspondence and often maintain
      lists of names, addresses, and telephone numbers of individuals with
      whom they have been in contact with and who share the same
      interests in encounters, sexual in nature, with children.

      Glenn Hayes, a computer forensics examiner with the Polk County Sheriff’s

Office, initially examined Mathis’s cell phone on December 22, 2011. During the

initial examination of Mathis’s phone, Hayes was able to retrieve contact lists,

phone logs, and text messages, but could not retrieve multimedia messages—i.e.,

text messages to which a file was attached. Hayes examined the phone a second

time on August 1, 2012. During the second examination, Hayes was able to

retrieve all of the same data as before in addition to multimedia messages. Based


                                          5
              Case: 13-13109     Date Filed: 09/24/2014   Page: 6 of 42


on information obtained from Mathis’s cell phone, law enforcement officers

believed that he had either persuaded or attempted to persuade two other minors—

Jerel A. and Harold J.—to send him sexually explicit pictures of themselves.

C. The Indictment

      A grand jury returned a second superseding indictment charging Mathis with

(1) knowingly employing, using, persuading, inducing, enticing, and coercing

Jerel A., a minor, to engage in sexually explicit conduct for the purpose of

producing a visual depiction of such conduct, and attempting to do so, in violation

of 18 U.S.C. § 2251(a) (Count One); (2) knowingly attempting to employ, use,

persuade, induce, entice and coerce Harold J., a minor, to engage in sexually

explicit conduct for the purpose of producing a visual depiction of such conduct, in

violation of 18 U.S.C. § 2251(a) (Count Two); (3) knowingly persuading,

inducing, and enticing Jarvis J., a minor, to engage in sexual activity, and

attempting to do so, in violation of 18 U.S.C. § 2422(b) (Count Three); and

(4) committing the offenses in Counts One through Three while he was required to

register as a sex offender under the laws of Florida, in violation of 18 U.S.C.

§ 2260A (Count Four).

D. Mathis’s Motion to Suppress

      Prior to trial, Mathis moved to suppress the evidence obtained from the

search of his cell phone. Mathis argued Detective Vizcarrondo’s affidavit in


                                          6
              Case: 13-13109    Date Filed: 09/24/2014    Page: 7 of 42


support of the search warrant was misleading because it indicated Mathis used his

cell phone to commit crimes against Jarvis J., even though the events giving rise to

the charge occurred in 2004, when Mathis had a different cell phone. Mathis

further maintained the search warrant was not supported by probable cause to

believe evidence of an offense committed seven years prior to the search would be

found on Mathis’s current smartphone; that the information on which the warrant

was based was stale; and that once law enforcement officials determined the

smartphone did not contain text messages from before 2011, any further search

exceeded the scope of the warrant.

      At a suppression hearing held before a magistrate judge, Sergeant Evans

testified that when he spoke with Jarvis J. at the Polk County Sheriff’s Office in

December 2011, Jarvis stated that, in 2004 and 2005, Mathis would communicate

with him on the phone, in person, and via text message. Sergeant Evans stated that

he knew Mathis did not have the same cell phone in 2011 as he did in 2004.

Nevertheless, based on his training and experience, Sergeant Evans believed

evidence of a crime committed in 2004 could be present on a cell phone in 2011.

For instance, the phone could contain soft copies of information, digital images

and media could be placed on a phone from an external source, and digital media

could be transferred from one phone to another with a media card. Sergeant Evans

further testified that, in his experience, individuals who sexually abuse minors


                                          7
             Case: 13-13109     Date Filed: 09/24/2014   Page: 8 of 42


generally maintain soft copies of evidence on their cell phones. Sergeant Evans

acknowledged there was no indication that Mathis took photographs of Jarvis with

his cell phone or that any text messages between Mathis and Jarvis were sexual in

nature.

      Adam Sharp, an expert in data recovery and the forensic analysis of

computers and cell phones, testified it was highly improbable that text messages

sent from a phone in 2004 would be present on a smartphone in 2011. Sharp

explained that cell phones in 2004 could hold approximately one hundred text

messages and that once the phone’s capacity was reached, old text messages would

be cleared when new text messages were received. Furthermore, it was not

generally possible to transfer information from one cell phone to another if an

individual changed cell phone carriers. In addition, data was stored differently in

2004 than in 2011, and various other factors would have made it improbable that a

text message from a cell phone in 2004 would be transferred to subsequent cell

phones.

      The magistrate judge issued a report and recommendation (R&R),

concluding Mathis’s motion to suppress should be denied because Detective

Vizcarrondo did not recklessly mislead the state court judge who issued the search

warrant, and because law enforcement acted in good faith reliance on the warrant




                                          8
               Case: 13-13109   Date Filed: 09/24/2014     Page: 9 of 42


when searching Mathis’s cell phone. Over Mathis’s objections, the district court

adopted the magistrate judge’s R&R and denied the motion to suppress.

E. The Trial

      At trial, Jarvis J. testified and recounted his interactions with Mathis in

detail. In addition, the Government introduced a copy of Mathis’s 1995 judgment

from the Circuit Court for Leon County, which showed that he entered a plea of

nolo contendere to lewd and lascivious assault on a child, in violation of § 800.04

of the Florida Statutes. The Government also introduced a judgment from

February 21, 1997, establishing that Mathis was sentenced to 48 months’

imprisonment for violating his probation on his § 800.04 offense.

      While Hayes was testifying at trial, Mathis renewed his motion to suppress,

arguing for the first time that the second search of his cell phone in August 2012

was not authorized by the search warrant. In response, the Government elicited

testimony from Hayes, who explained that during the December 2011 examination,

the device he used to remove information from Mathis’s cell phone was not able to

extract multimedia messages from the phone. However, the device was

subsequently updated numerous times before Hayes examined the phone again in

August 2012. After the device was updated, Hayes was able to retrieve everything

from Mathis’s phone, including multimedia messages. The district court denied

the renewed motion to suppress. The court explained that law enforcement officers


                                          9
             Case: 13-13109      Date Filed: 09/24/2014    Page: 10 of 42


had not acted in bad faith in waiting approximately eight months before searching

the phone a second time and, regardless, Mathis was not prejudiced by the delay.

      During the third day of trial, the Assistant United States Attorney (AUSA)

advised the district court that earlier that morning she was in the elevator with

Sergeant Evans when a juror stepped into the elevator as the doors were closing.

Before the AUSA noticed the juror, the AUSA told Sergeant Evans that she had

been at work until 2:00 a.m., to which Sergeant Evans responded, “[t]hat sucks.”

      Michelle Gonzalez, a special agent with the Federal Bureau of Investigation

(FBI), testified that, based on their birth certificates, Jerel A. and Harold J. turned

16 years old in 2011, and that Jarvis J. was 14 years old in 2004.

      Rashaad J. testified that he was friends with Harold J. Rashaad first met

Mathis in the summer of 2011, when Rashaad was 17 years old. Rashaad met

Mathis through Harold. Rashaad testified he took three pictures of Harold shirtless

for Harold to send to Mathis, and that he saw Harold send one of the pictures to

Mathis. Rashaad also saw Harold send a pornographic picture to Mathis that he

got from the Internet.

      At the beginning of the fourth day of trial, the AUSA informed the district

court that while Agent Gonzalez was at a coffee shop, a juror possibly overheard

the special agent say “they need to get him” during a conversation on her cell

phone. The district court indicated it did not think there was a problem.


                                           10
             Case: 13-13109     Date Filed: 09/24/2014   Page: 11 of 42


      Harold J. was called as a witness. He testified that he first met Mathis after

a basketball game. Mathis told Harold that he wanted to get to know him and then

began sending Harold text messages. Mathis indicated he was trying to act like a

father figure and told Harold to let him know if he needed anything. For instance,

on May 24, 2011, Mathis sent Harold a text message saying “I’m good people I

promise you can trust me even if you do things wrong” as well as a message

stating in part, “[w]hen I meet you I saw something about you and took interest in

you . . . . Let’s keep in touch so I can do things for you.” Mathis also sent Harold a

text message on May 24, 2011, stating “[l]et me help you. No one will know what

I’m doing unless you tell them. This coming from my heart cause I see good in

you. . . . You will have money in your pocket and lots of nice cloth[e]s and shoes

for next year.”

      On May 31, 2011, in response to a text message from Mathis, Harold sent

Mathis a text message stating he was 15 years old. Mathis continued sending text

messages to Harold encouraging Harold to trust him and professing that he had

strong feelings for Harold. On several occasions, Mathis asked Harold to send him

pictures, and Harold complied by sending pictures of himself in athletic wear and

casual clothing. Mathis also sent Harold text messages asking Harold about his

sexual activity and discussing Harold’s physique.




                                          11
             Case: 13-13109     Date Filed: 09/24/2014   Page: 12 of 42


      On July 16, 2011, Mathis sent Harold a text message asking Harold to send

him a picture of himself shirtless. Harold ignored the text message and Mathis sent

Harold text messages several days later again asking for pictures of Harold without

a shirt. Harold ultimately sent Mathis three pictures of himself in which he was

not wearing a shirt. Mathis subsequently sent Harold text messages asking Harold

to send him pictures of his genitalia. In response, Harold sent Mathis pictures of

male genitalia he obtained from the Internet. After Harold sent one of the pictures,

Mathis sent Harold text messages asking Harold to let him see and touch Harold’s

genitalia.

      Gary Scevola, a senior investigator with the U.S. Marshal Service, testified

that he obtained certified copies of Mathis’s sex offender registration forms from

the Florida Department of Law Enforcement, and the Government introduced the

forms into evidence.

      After Scevola testified, the Government recalled Agent Gonzalez. Agent

Gonzalez testified that as part of her investigation she reviewed text messages

between Mathis and Jerel A. After Mathis objected to the introduction of Jerel’s

text messages as impermissible hearsay, the district court instructed the jurors that

they could not consider Jerel’s text messages for the truth of the matter asserted.

The court further instructed the jurors that they could nevertheless consider

Mathis’s text messages for the truth of the matter asserted. Mathis also objected to


                                          12
             Case: 13-13109     Date Filed: 09/24/2014    Page: 13 of 42


the introduction of the text messages on Confrontation Clause grounds. Over

Mathis’s objections, Agent Gonzalez testified that on May 2, 2011, Jerel sent a text

message to Mathis stating “[h]ey this jerel..this my number,” to which Mathis

replied, “[o]k did you have enough money” and “[o]k well you will get some more.

Also text me tonite when you by yourself want to talk to you, and know I care

about you.” Mathis then sent Jerel text messages expressing affection and

promising to provide for him, as well as messages asking Jerel to send him

pictures. Jerel complied and sent Mathis several pictures of himself. Mathis also

repeatedly sent Jerel text messages discussing the size of Jerel’s genitalia and

Jerel’s sexual activity. Mathis sent Jerel text messages asking Jerel to trust him,

such as the following message on May 8, 2011: “Jerel you got it real good and

don’t realize it. You need to let your guards down and let me be close to you.”

       Eventually, Mathis sent Jerel text messages asking him for pictures of his

genitalia. On June 29, 2011, Jerel sent Mathis a text message containing a picture

of his genitalia. Mathis responded by sending Jerel text messages asking to touch

Jerel’s genitalia. On September 11, 2011, Mathis again sent text messages to Jerel

asking for pictures of Jerel’s genitalia. In response, Jerel sent Mathis a text

message containing a picture of his genitalia. On cross-examination, Agent

Gonzalez acknowledged that Jerel had been present in the courthouse the previous

day.


                                          13
             Case: 13-13109     Date Filed: 09/24/2014     Page: 14 of 42


      After the Government rested its case-in-chief, Mathis moved for a judgment

of acquittal, which the district court denied. Mathis then introduced two exhibits

into evidence and rested his case without renewing his motion for a judgment of

acquittal. Mathis did not testify.

      On the fifth and final day of trial, the district court instructed the jury and

then the parties delivered their closing arguments. During the Government’s

closing argument, the AUSA stated “[i]n 2004 the defendant was 34. Jarvis J. was

14. Jarvis J. told you the defendant, Pastor Maurice, molested him and he

assaulted him. It’s a violation of Florida law. The same statute as defendant’s

1995 conviction.” Mathis objected to the statement and moved for a mistrial. The

district court denied the motion but offered to instruct the jury regarding the

AUSA’s statement. Mathis declined to ask for an instruction.

      When the proceedings resumed following a break between the parties’

closing arguments, defense counsel informed the court that, during the break,

Mathis’s aunt overheard one juror say to another juror, “oh, I just love her.” The

district court stated it did not know to whom or what the comment was referring

and that a cautionary instruction was not warranted. The jury ultimately convicted

Mathis on each count.




                                          14
             Case: 13-13109     Date Filed: 09/24/2014    Page: 15 of 42


F. The Presentence Investigation Report

      In preparing Mathis’s Presentence Investigation Report (PSI), the probation

officer calculated a combined adjusted offense level of 41 as to Counts One

through Three, based in part on a two-level enhancement under U.S.S.G.

§ 2G2.1(b)(6) for Mathis’s use of a computer or interactive computer service to

persuade, induce, entice, coerce, or facilitate the travel of a minor to engage in

sexually explicit conduct. Mathis had a criminal history category of V pursuant to

U.S.S.G. § 4B1.5(a)(2) because he had sustained a prior conviction for a sex

offense. Based on his combined adjusted offense level of 41 and criminal history

category of V, Mathis’s advisory guidelines range on Counts One through Three

was 360 months to life imprisonment, with a consecutive 10-year statutory

mandatory minimum term of imprisonment on Count Four. Mathis was also

subject to statutorily enhanced penalties on Counts One and Two under 18 U.S.C.

§ 2251(e) based on his 1995 conviction. Mathis objected to the PSI’s factual

allegations as well as the enhancements under U.S.S.G. § 2G2.1(b)(6) and 18

U.S.C. § 2251(e).

G. The Sentencing Hearing

      During his sentencing hearing, Mathis reiterated his objection to the

§ 2G2.1(b)(6) enhancement, arguing that he did not use “the computer

components” of his smartphone in committing the offenses in Counts One and


                                          15
             Case: 13-13109     Date Filed: 09/24/2014   Page: 16 of 42


Two, in which he was charged with persuading Jerel A. and attempting to persuade

Harold J. to produce child pornography. Instead, Mathis simply sent text messages

and requested pictures, which he could have done with a basic cell phone. The

district court overruled the objection and found the two-level enhancement applied

because Mathis used a smartphone which had Internet and email capabilities and,

further, Mathis sent and received multimedia messages.

      Relying on Alleyne v. United States, 133 S. Ct. 2151 (2013), Mathis objected

to his sentence being enhanced based on the facts underlying his prior conviction.

Mathis also objected to the statutory enhancements under 18 U.S.C. § 2251(e),

contending that his 1995 conviction was not a qualifying predicate offense because

the statute under which he was convicted did not require contact as an element of

the offense. The district court overruled the objection, finding that the § 2251(e)

enhancements applied because the statute was not limited to prior convictions

involving sexual contact. After ruling on various other objections, the district

court calculated that Mathis had a total offense level of 41 and criminal history

category of V, yielding a guidelines range of 360 months to life imprisonment,

with a mandatory consecutive 10-year sentence on Count Four. The district court

sentenced Mathis to 480 months’ imprisonment, comprised of concurrent terms of

360 months’ imprisonment on Counts One, Two, and Three, and a consecutive

120-month term of imprisonment on Count Four. This appeal followed.


                                         16
               Case: 13-13109       Date Filed: 09/24/2014       Page: 17 of 42


                                      II. DISCUSSION

       Mathis raises a host of issues on appeal related to his trial, convictions, and

total sentence. Specifically, Mathis contends that (1) the district court erred by

denying his motion to suppress and renewed motion to suppress; (2) the

introduction of Jerel A.’s text messages at trial violated his Confrontation Clause

rights; (3) insufficient evidence supported each of his convictions; (4) the district

court erred by denying his motion for a mistrial based on the AUSA’s statements

during closing argument; (5) the district court should have interrogated the jurors

or given them an instruction following the two instances of inadvertent juror

contact and after Mathis’s aunt overheard a comment between two jurors; (6) the

cumulative effect of the alleged trial errors warrants reversal; (7) the district court

erred in applying a two-level sentencing enhancement under U.S.S.G.

§ 2G2.1(b)(6); 1 and (8) the district court erred by enhancing his sentences pursuant

to 18 U.S.C. § 2251(e). We conclude none of the issues raised by Mathis have

merit, and we therefore affirm his convictions and sentences.

A. Motions to Suppress

       Mathis contends the search of his phone violated his Fourth Amendment

rights because the affidavit submitted in support of the search warrant was


       1
         Mathis also argued in his initial brief that the district court erred by applying an
enhancement under U.S.S.G. § 2G2.1(b)(3), but he explicitly abandoned that argument in his
reply brief and we do not address it.
                                               17
              Case: 13-13109     Date Filed: 09/24/2014     Page: 18 of 42


misleading and thus the warrant was not obtained in good faith. He also argues the

second examination of his phone exceeded the scope and timeframe of the search

warrant.

      In considering the district court’s denial of a motion to suppress, we review

the district court’s factual findings for clear error, construing the facts in the light

most favorable to the prevailing party, but review the district court’s application of

law to the facts de novo. United States v. Ransfer, 749 F.3d 914, 921 (11th Cir.

2014). We also review de novo “whether a search warrant affidavit established

probable cause” and we “give due weight to inferences drawn from [the] facts by

resident judges and local law enforcement officers.” United States v. Bush, 727

F.3d 1308, 1315 n.3 (11th Cir. 2013) (internal quotation marks omitted).

      1. The Search Warrant

      Mathis argues the affidavit Detective Vizcarrondo submitted in support of

her application for a search warrant was misleading because (1) the affidavit did

not explicitly state that Mathis’s cell phone was a 2011 smartphone and was not

the same phone Mathis used in 2004, and (2) the affidavit failed to state that Jarvis

never alleged his phone and text message conversations with Mathis were sexual in




                                            18
               Case: 13-13109        Date Filed: 09/24/2014        Page: 19 of 42


nature. Mathis further maintains it was improbable that evidence of a crime

committed in 2004 would be present on a cell phone in 2011. 2

       Mathis’s arguments are unavailing. It is well established that affidavits

submitted in support of search warrants are presumptively valid. Franks v.

Delaware, 438 U.S. 154, 171, 98 S. Ct. 2674, 2684 (1978) (“There is, of course, a

presumption of validity with respect to the affidavit supporting the search

warrant.”); United States v. Lebowitz, 676 F.3d 1000, 1010 (11th Cir. 2012)

(“Affidavits supporting warrants are presumptively valid.”). Thus, “intentional or

reckless omissions will invalidate a warrant only if inclusion of the omitted facts

would have prevented a finding of probable cause.” Lebowitz, 676 F.3d at 1010

(internal quotation marks and alteration omitted).

       Inclusion of the omitted facts would not have prevented a finding of

probable cause. 3 Even if the affidavit had stated that Mathis possessed a different


       2
          At oral argument, counsel argued the information contained in the affidavit was stale.
As counsel noted, she made passing reference to that argument in her opening brief when she
stated “the application was overly-broad in an apparent attempt to avoid the appearance of
staleness and in order to attempt to obtain evidence of other crimes unrelated to J.J.’s
allegations.” That terse statement did not sufficiently raise the issue. See United States v. King,
751 F.3d 1268, 1277 (11th Cir. 2014); Sapuppo v. Allstate Floridian Ins. Co., 739 F.3d 678, 681
(11th Cir. 2014) (“We have long held that an appellant abandons a claim when he either makes
only passing references to it or raises it in a perfunctory manner without supporting arguments
and authority.”). Even if we were to consider the argument, it lacks merit. The affidavit was
based on information from Jarvis’s recorded phone call to Mathis in December 2011.
       3
          It is well settled that “[c]ourts reviewing the legitimacy of search warrants should not
interpret supporting affidavits in a hypertechnical manner; rather, a realistic and commonsense
approach should be employed.” United States v. Miller, 24 F.3d 1357, 1361 (11th Cir. 1994).
Having employed a commonsense approach in reviewing the search warrant in this case, we
                                                 19
               Case: 13-13109       Date Filed: 09/24/2014      Page: 20 of 42


phone in 2011 than the phone he used to contact Jarvis in 2004, and that Jarvis

never claimed his cell phone and text message communications with Mathis were

sexual in nature, the affidavit provided probable cause sufficient to support the

issuance of a warrant. See United States v. Gibson, 708 F.3d 1256, 1278 (11th Cir.

2013) (“To obtain a warrant, police must establish probable cause to conclude that

there is a fair probability that contraband or evidence of a crime will be found in a

particular place.” (internal quotation marks omitted)). We have explained that “an

affidavit should establish a connection between the defendant and the property to

be searched and a link between the property and any criminal activity.” Id.

(internal quotation marks and brackets omitted).

       Detective Vizcarrondo’s affidavit established a connection between Mathis

and the phone to be searched. The affidavit explained that Jarvis made a recorded

phone call to Mathis’s phone number on December 17, 2011, that Mathis did not

maintain a home phone and appeared to exclusively use his cell phone to

communicate with others, and that Mathis had maintained the same phone number

since 2004.

       The affidavit also established a connection between Mathis’s cell phone and

criminal activity. Specifically, the affidavit explained Jarvis had told law




conclude Detective Vizcarrondo did not intentionally or recklessly omit information from the
affidavit she submitted to the state court judge who issued the warrant.
                                              20
               Case: 13-13109       Date Filed: 09/24/2014      Page: 21 of 42


enforcement officers that, during the period in time when Mathis sexually abused

him, Mathis continuously called him from Mathis’s cell phone and that the two

would communicate via text messages. Contrary to Mathis’s contentions, the fact

that Mathis may not have made sexually explicit comments to Jarvis on the phone

or in text messages did not mean evidence of wrongdoing would not be found on

his phone. See United States v. Tinkle, 655 F.2d 617, 621 (5th Cir. Unit A Sept.

1981) (“The currency of probable cause is probability, not legal certainty; it may

exist even though the evidence before the officer is insufficient to convict.”). 4 As

the Supreme Court has stated, “innocent behavior frequently will provide the basis

for a showing of probable cause,” and the relevant inquiry in making a

determination of probable cause “is not whether particular conduct is ‘innocent’ or

‘guilty,’ but the degree of suspicion that attaches to particular types of

non-criminal acts.” Illinois v. Gates, 462 U.S. 213, 243 n.13, 103 S. Ct. 2317,

2335 n.13 (1983). The affidavit, moreover, explained that, based on her

knowledge, experience, and training, Detective Vizcarrondo knew that individuals

who sexually abuse children sometimes maintain copies of communications with

their victims “in the privacy and security of their personal cell phones and retain

these items for many years.” See Riley v. California, 573 U.S. __, __, 134 S. Ct.


       4
          In Bonner v. City of Prichard, 661 F.2d 1206, 1209 (11th Cir. 1981) (en banc), this
Court adopted as binding precedent all decisions of the former Fifth Circuit handed down prior
to the close of business on September 30, 1981.
                                               21
                Case: 13-13109        Date Filed: 09/24/2014        Page: 22 of 42


2473, 2492 (2014) (“In the cell phone context . . . it is reasonable to expect that

incriminating information will be found on a phone regardless of when the crime

occurred.”).

       Alternatively, even if the search warrant was not supported by probable

cause, evidence obtained from the search of Mathis’s phone was not subject to

suppression under the good faith exception to the exclusionary rule. See United

States v. Martin, 297 F.3d 1308, 1313 (11th Cir. 2002) (explaining that “United

States v. Leon, 468 U.S. 897, 922, 104 S. Ct. 3405, 3420 (1984), stands for the

principle that courts generally should not render inadmissible evidence obtained by

police officers acting in reasonable reliance upon a search warrant that is

ultimately found to be unsupported by probable cause”).5 The record contains no

indication Detective Vizcarrondo was dishonest or reckless in preparing her

affidavit or that she could not have harbored an objectively reasonable belief in the

existence of probable cause. Because the officers engaged in “objectively

reasonable law enforcement activity and . . . acted in good faith when obtaining
       5
          Mathis does not argue in his initial brief that any exception to the good faith rule applies
in this case. He does not contend that (1) Detective Vizcarrondo included information in the
affidavit that she knew was false or would have known was false except for her reckless
disregard for the truth; (2) the issuing judge wholly abandoned his judicial role; (3) the affidavit
was so lacking in indicia of probable cause that official belief in its existence was unreasonable;
or (4) the warrant was so facially deficient that the executing officers could not reasonably
presume it was valid. See Martin, 297 F.3d at 1313. Accordingly, Mathis has abandoned any
argument regarding the exceptions to the good faith rule. See United States v. McKinley, 732
F.3d 1291, 1295 n.1 (11th Cir. 2013). In the alternative, even if the issue was sufficiently raised,
Mathis has not demonstrated that any exception to the good faith rule applies and we conclude
the issue lacks merit.


                                                 22
               Case: 13-13109        Date Filed: 09/24/2014        Page: 23 of 42


[the] search warrant . . . the Leon good faith exception applies.” Id. (internal

quotation marks omitted).

       2. The August 2012 Examination 6

       Mathis also contests the validity of the second examination of his

smartphone, which occurred on August 1, 2012. Before the district court, Mathis

argued in his renewed motion to suppress that the multimedia messages obtained

during the August 2012 examination were not in plain view during the December

2011 examination and there was no authorization for the August 2012 examination

because no new search warrant had been obtained.

       On appeal, Mathis contends evidence obtained from his smartphone on

August 1, 2012, should have been suppressed because the examination occurred

well after the expiration of the 10-day period provided in the warrant. Mathis

devotes only two paragraphs of his sixty-one page opening brief to this issue. In

those two paragraphs, Mathis mostly repeats the facts underlying his claim and his

actual argument boils down to three sentences. First, he argues “[t]he district court

erred in not granting Mathis’s motion to suppress at trial where the evidence was

obtained outside the scope and time frame of the search warrant.” Second, he

       6
          Although Mathis arguably waived his challenge to the August 2012 examination
because he did not raise it in his motion to suppress prior to trial, see United States v. Ford, 34
F.3d 992, 994 n.2 (11th Cir. 1994) (concluding a party’s failure to raise a suppression argument
prior to trial resulted in a waiver of the issue); Fed. R. Crim. P. 12(b)(3), (e), the district court
considered and rejected the issue on the merits and we will therefore address it, see United States
v. Lall, 607 F.3d 1277, 1290 (11th Cir. 2010).

                                                 23
               Case: 13-13109        Date Filed: 09/24/2014        Page: 24 of 42


asserts “[e]vidence seized while the police are acting outside the boundaries of the

warrant is subject to suppression.” Third, Mathis contends that “[o]nly during a

search conducted eight mo[n]ths [after the initial search], outside the scope of the

search warrant[,] was Hayes able to determine who sent the MMS messages.”

Mathis does not argue the eight month delay was itself unreasonable or that he was

prejudiced by the delay. In support of his arguments, Mathis cites only a single

Fourth Circuit opinion from 1994 for the proposition that, if officers seize items

which are not enumerated in a search warrant, those items are subject to

suppression.7

       Although Mathis contends the second examination of his phone violated his

constitutional rights, we have held that “[t]he Fourth Amendment does not specify

that search warrants contain expiration dates,” and that a search conducted after a

warrant’s expiration date does not necessarily require suppression of the evidence.

United States v. Gerber, 994 F.2d 1556, 1559-60 (11th Cir. 1993); see also

Herring v. United States, 555 U.S. 135, 144, 135 S. Ct. 695, 702 (2009) (“To

trigger the exclusionary rule, police conduct must be sufficiently deliberate that



       7
          Mathis has waived any arguments that he raises only in his reply brief because those
arguments are too late. United States v. Lopez, 649 F.3d 1222, 1246 (11th Cir. 2011); United
States v. Evans, 473 F.3d 1115, 1120 (11th Cir. 2006) (“Arguments raised for the first time in a
reply brief are not properly before a reviewing court.” (internal quotation marks and alteration
omitted)). In addition, the record does not support Mathis’s contention in his reply brief that the
Government searched his smartphone month after month for eight months. Instead, the record
establishes that Mathis’s smartphone was examined only twice.
                                                24
                Case: 13-13109      Date Filed: 09/24/2014      Page: 25 of 42


exclusion can meaningfully deter it, and sufficiently culpable that such deterrence

is worth the price paid by the justice system.”).

           We need not decide this issue, however, because even if the August 2012

examination violated Mathis’s Fourth Amendment rights, any error in admitting

the evidence at trial was harmless. See United States v. Rhind, 289 F.3d 690, 694

(11th Cir. 2002). The record demonstrates that officers obtained Mathis’s SMS

messages, i.e., plain text messages, during the initial examination of his cell phone,

but could not recover his multimedia messages, i.e., text messages containing

pictures or videos. The initial search was conducted within the ten-day period

provided in the warrant and, as discussed above, was valid. Mathis’s plain text

messages, even without the multimedia messages and accompanying pictures,

provided overwhelming evidence of Mathis’s guilt on Counts One and Two.

Accordingly, any error in admitting the multimedia messages was harmless. 8 See

id. (concluding a Fourth Amendment violation was harmless because evidence of

the defendants’ guilt was overwhelming).

B. The Confrontation Clause

       Mathis argues that the admission of Jerel A.’s text messages at trial violated

his rights under the Confrontation Clause. Mathis contends he was prohibited from


       8
        Counsel agreed at oral argument that any error in the introduction of the multimedia
messages obtained from the August 2012 examination was harmless in light of the plain text
messages retrieved during the December 2011 examination.
                                              25
             Case: 13-13109    Date Filed: 09/24/2014    Page: 26 of 42


cross-examining and impeaching Jerel’s testimony, while the Government was

allowed to introduce favorable evidence in the form of Jerel’s text messages. “We

review a preserved Confrontation Clause claim de novo,” United States v. Curbelo,

726 F.3d 1260, 1271-72 (11th Cir. 2013), and also review de novo “the question of

whether hearsay statements are testimonial for purposes of the Confrontation

Clause,” United States v. Caraballo, 595 F.3d 1214, 1226 (11th Cir. 2010)

(internal quotation marks omitted).

      Mathis’s arguments lack merit. The Confrontation Clause bars the

admission of a witness’s testimonial statements when the witness did not appear at

trial unless the witness was unavailable and the defendant had a prior opportunity

to examine him. Caraballo, 595 F.3d at 1227; see also Crawford v. Washington,

541 U.S. 36, 53-54, 124 S. Ct. 1354, 1365 (2004). Mathis does not argue on

appeal that Jerel’s text messages were testimonial and he has “therefore abandoned

an issue on which he had to prevail in order to obtain reversal.” United States v.

King, 751 F.3d 1268, 1277 (11th Cir. 2014). Regardless, any argument that Jerel’s

text messages were testimonial would be unavailing. We have explained that:

      [F]ormal statements to government officers are generally testimonial
      as are affidavits, custodial examinations, prior testimony that the
      defendant was unable to cross-examine, or similar pretrial statements
      that declarants would reasonably expect to be used prosecutorially.
      Similarly, extrajudicial statements contained in formalized testimonial
      materials, such as affidavits, depositions, prior testimony, or
      confessions, and statements that were made under circumstances
      which would lead an objective witness reasonably to believe that the
                                         26
               Case: 13-13109      Date Filed: 09/24/2014      Page: 27 of 42


        statement would be available for use at a later trial, fall within the core
        class of testimony.

Caraballo, 595 F.3d at 1228 (brackets and alterations omitted). Jerel’s text

messages were not formal statements to government officers, they were not made

during a custodial examination, and they did not constitute an affidavit, prior

testimony, or pretrial statements that he would reasonably expect to be used

prosecutorially. Jerel’s text messages were not formalized testimonial materials,

and they were not made under circumstances that would lead an objective witness

reasonably to believe that they would be available for use at a later trial. See id.

Far from amounting to “the functional equivalent of in-court testimony,” Curbelo,

726 F.3d at 1272 (internal quotation marks omitted), Jerel’s text messages were

informal, haphazard communications sent at all hours and from locations such as

his house, the bus stop, and his school. Jerel’s text messages were not testimonial

statements and Mathis’s right of confrontation was not violated by their admission

at trial.

C. Sufficiency of the Evidence

     Mathis argues that insufficient evidence supported each of his convictions. 9

As to Count One—which charged Mathis with persuading, inducing, enticing, or

        9
         While we ordinarily “review challenges to the sufficiency of the evidence de novo, and
ask whether a reasonable jury could have found the defendant guilty beyond a reasonable doubt,”
when a defendant “fails to renew his motion for judgment of acquittal at the end of all of the
evidence, we review the defendant’s challenge to the sufficiency of the evidence for a manifest
miscarriage of justice.” United States v. House, 684 F.3d 1173, 1196 (11th Cir. 2012) (internal
                                              27
               Case: 13-13109       Date Filed: 09/24/2014       Page: 28 of 42


coercing Jerel A. to engage in sexually explicit conduct for the purpose of

producing a visual depiction of such conduct—Mathis reiterates his Confrontation

Clause arguments and then asserts without elaboration that there was no proof

beyond a reasonable doubt that Jerel produced a sexually explicit visual depiction.

We have already determined that Mathis’s Confrontation Clause arguments lack

merit and we conclude the evidence was more than sufficient to support Mathis’s

conviction on Count One.

       At trial, the Government introduced evidence that Jerel was a minor in 2011

and that Mathis persuaded, induced, enticed, or coerced Jerel to take pictures of his

genitalia and then send them to Mathis in text messages. Specifically, Mathis

asked Jerel for pictures of Jerel’s genitalia in May, June, and September of 2011,

Mathis offered to pay Jerel for a picture of Jerel’s genitalia, and he directed Jerel to

take sexually explicit pictures. For instance, on June 29, 2011, Mathis sent Jerel a

text message stating “I want my picture and it better be hard and I hope you trust

me cause I have been there for you.” Similarly, on September 11, 2011, Mathis

asked Jerel to send him a text message with a picture of his genitalia, stating “[o]k



quotation marks omitted). Although Mathis introduced two exhibits into evidence during his
case-in-chief and then failed to renew his motion for a judgment of acquittal, we need not decide
whether to review his arguments only for a manifest miscarriage of justice because his
sufficiency challenges fail regardless of the standard applied. See United States v. Houser, 754
F.3d 1335, 1349 (11th Cir. 2014) (“Regardless of the standard applied . . . [the defendant’s]
sufficiency challenge fails.”).

                                               28
             Case: 13-13109     Date Filed: 09/24/2014    Page: 29 of 42


just send a good one I want to see how long it is,” and, after receiving a picture,

Mathis sent Jerel a text message saying “[c]an you hold it up please.” The

Government also introduced into evidence two pictures of male genitalia Jerel sent

to Mathis, at least one of which was an image of male genitalia in an aroused state.

The evidence adduced at trial was sufficient for a jury to conclude Mathis

persuaded Jerel to produce and send him a visual depiction of sexually explicit

conduct. See United States v. Grzybowicz, 747 F.3d 1296, 1305-07 (11th Cir.

2014).

      The evidence was also sufficient to support Mathis’s conviction on Count

Two, which charged him with attempting to persuade, induce, entice, or coerce

Harold J. to engage in sexually explicit conduct for the purpose of producing a

visual depiction of such conduct. On appeal, Mathis argues only that his

conviction cannot stand because Harold did not, in fact, produce a visual depiction

of sexually explicit conduct. Mathis’s argument fails to recognize that he was

convicted in Count Two of attempted production of child pornography rather than

actual production. The evidence presented at trial, moreover, demonstrated that

Mathis intentionally attempted to persuade Harold, who was a minor in 2011, to

produce child pornography. Harold testified that Mathis repeatedly sent him text

messages exhorting Harold to trust him. Harold also explained that, on several

occasions, Mathis asked Harold to send him text messages with pictures of


                                          29
             Case: 13-13109      Date Filed: 09/24/2014    Page: 30 of 42


Harold’s genitalia. According to Harold, on one occasion Mathis sent him text

messages offering to pay him $500 in exchange for such a picture and, on another

occasion, Mathis promised to take Harold to Tampa in exchange for Harold taking

and sending a picture of his genitalia. In addition, the Government introduced

copies of the text messages between Mathis and Harold in which Mathis asked

Harold for pictures of his genitalia. A reasonable jury could have found that

Mathis took a substantial step toward persuading, inducing, or enticing Harold to

produce child pornography and that he attempted to produce child pornography.

See United States v. Lee, 603 F.3d 904, 918 (11th Cir. 2010).

      Mathis next contends insufficient evidence supported his conviction on

Count Three because he was charged with enticing and attempting to entice Jarvis

to engage in sexual activity on a cellular phone and that no evidence proved sexual

activity took place on the phone or that Mathis used a phone to commit the offense.

Mathis again misconceives the offense for which he was convicted. Count Three

charged him with using a facility of interstate commerce to knowingly persuade,

induce, or entice Jarvis J., a minor, to engage in illegal sexual activity, in violation

of 18 U.S.C. § 2422(b). Section 2422(b) does not require that the sexual activity

have occurred on the facility of interstate commerce, in this case a cell phone. See

18 U.S.C. § 2422(b).




                                           30
                 Case: 13-13109       Date Filed: 09/24/2014       Page: 31 of 42


         Regardless, Mathis’s argument is contradicted by the record. Jarvis testified

that, after their first sexual interaction, Mathis talked to him on his cell phone in a

sexually explicit manner and that Mathis was more comfortable “talking about

planning it with [him].” Jarvis’s extensive testimony at trial provided sufficient

evidence for the jury to conclude Mathis used his cell phone to induce or entice

Jarvis to engage in sexual activity and his conviction on Count Three must stand.

         Mathis’s conviction on Count Four was also supported by sufficient

evidence. Count Four charged Mathis with violating 18 U.S.C. § 2260A by

committing the offenses charged in Counts One through Three while he was

required to register as a sex offender under Florida law. 10 The Government

introduced a copy of a judgment demonstrating that, on February 22, 1995, Mathis

was convicted of lewd or lascivious assault on a child, in violation of § 800.04 of

the Florida Statutes. 11 Accordingly, Florida law required Mathis to register as a

sex offender if he was released from his sentence for that conviction on or after

10
     Section 2260A provides:

         Whoever, being required by Federal or other law to register as a sex offender,
         commits a felony offense involving a minor under section 1201, 1466A, 1470,
         1591, 2241, 2242, 2243, 2244, 2245, 2251, 2251A, 2260, 2421, 2422, 2423, or
         2425, shall be sentenced to a term of imprisonment of 10 years in addition to the
         imprisonment imposed for the offense under that provision. The sentence
         imposed under this section shall be consecutive to any sentence imposed for the
         offense under that provision.

18 U.S.C. § 2260A.
         11
         Mathis was sentenced to a 52-month term of imprisonment, but his sentence was
suspended and he was placed on a 2-year term of probation.
                                                 31
               Case: 13-13109     Date Filed: 09/24/2014   Page: 32 of 42


October 1, 1997. See Fla. Stat. § 943.0435; Miller v. State, 971 So. 2d 951, 954

(Fla. 5th DCA 2007). Mathis maintains no evidence was introduced at trial

proving when he was released from custody for his § 800.04 offense. Thus, no

evidence was presented that he was required to register as a sex offender under

Florida law.

      Contrary to his contentions, the Government presented sufficient evidence

from which a reasonable jury could have found he was required to register as a sex

offender. The Government introduced a copy of a judgment from February 21,

1997, adjudicating Mathis guilty of violating the term of probation to which he was

sentenced for his § 800.04 conviction. Mathis was sentenced to a 48-month term

of imprisonment for his probation violation and was given credit for 174 days of

time served. Accordingly, the jury could have found Mathis was to be incarcerated

for 1,286 days, placing his release date well beyond October 1, 1997. Such a

finding was supported by copies of Mathis’s sex offender registration forms, which

indicated he registered as a sex offender with the State of Florida in January 1999

due to his § 800.04 conviction.

D. Motion for a Mistrial

      Mathis argues the district court erred by denying his motion for a mistrial

based on the AUSA’s statement during closing argument that Mathis’s conduct in

2004 was a violation of § 800.04, the same statute under which Mathis was


                                           32
              Case: 13-13109     Date Filed: 09/24/2014     Page: 33 of 42


convicted in 1995. We review the denial of a motion for a mistrial for abuse of

discretion. United States v. Garcia, 405 F.3d 1260, 1272 (11th Cir. 2005). An

improper closing argument will justify a new trial only if it was “both improper

and prejudicial to a substantial right of the defendant.” Id. (internal quotation

marks omitted).

      In the context of the entire trial, the AUSA’s comment did not prejudice

Mathis’s substantial rights. See United States v. Hasner, 340 F.3d 1261, 1275

(11th Cir. 2003) (“Prosecutorial misconduct is a basis for reversing an appellant’s

conviction only if, in the context of the entire trial in light of any curative

instruction, the misconduct may have prejudiced the substantial rights of the

accused.” (internal quotation marks omitted)). The jury was provided a copy of the

indictment which clearly revealed the same information referenced by the AUSA,

namely that Mathis’s conduct in 2004 was illegal under § 800.04 of the Florida

Statutes, and that Mathis had previously violated § 800.04. Additionally, the

evidence that Mathis enticed or induced Jarvis to engage in sexual activity was

overwhelming and included Jarvis’s testimony at trial as well as Jarvis’s recorded

conversation with Mathis in which Mathis acknowledged sexually abusing Jarvis

when he was a minor. Thus, no reasonable probability existed that, but for the

remark, the outcome of the trial would have been different. The district court did

not abuse its discretion by denying Mathis’s motion for a mistrial. See United


                                           33
             Case: 13-13109      Date Filed: 09/24/2014    Page: 34 of 42


States v. Capers, 708 F.3d 1286, 1308-09 (11th Cir. 2013) (“A defendant’s

substantial rights are prejudiced if there is a reasonable probability that, but for the

improper remarks, the outcome of the trial would have been different.” (internal

quotation marks omitted)).

E. Juror Encounters

      Mathis next argues that three occurrences during the course of the trial

involving jurors could have affected the impartiality of the jury and rendered his

trial unfair. First, Mathis contends the juror who potentially overheard the AUSA

tell Sergeant Evans that she worked late into the night could have felt sympathy for

the AUSA and, by extension, the Government’s case. Second, Mathis maintains

the jury could have been influenced or affected by the fact that a juror potentially

overheard Agent Gonzalez in a coffee shop say into her cell phone “we need to get

him.” Third, Mathis argues that the two jurors whom Mathis’s aunt overheard

saying “oh, I just love her” could have been expressing a preference for the

Government and bias toward the defense.

      We presume that the jury was impartial, and neither Mathis’s speculation

nor the record establishes that the jurors in the elevator and the coffee shop

actually overheard the statements of which he complains, or that any of the jurors

were biased against him. See United States v. Siegelman, 640 F.3d 1159, 1182

(11th Cir. 2011). Mathis has failed to make a colorable showing that the jury was


                                           34
              Case: 13-13109    Date Filed: 09/24/2014   Page: 35 of 42


exposed to extraneous information, see id., and the district court did not err by

declining to interrogate each member of the jury in response to such fleeting,

innocuous events. Furthermore, the district court instructed the jurors that their

decision had to be based on the evidence presented during trial and that they

should not be influenced in any way by sympathy or prejudice against the

defendant or the Government. The district court also instructed the jurors that they

should not discuss the case among themselves until the court gave them the case to

decide. We presume the jury followed the district court’s instructions, and Mathis

has provided us with no basis for disregarding that presumption. See United States

v. Stone, 9 F.3d 934, 938 (11th Cir. 1993) (“Few tenets are more fundamental to

our jury trial system than the presumption that juries obey the court’s

instructions.”).

F. Cumulative Error

      Mathis argues that the cumulative effect of the alleged errors at trial

deprived him of a fair trial. Mathis, however, has not demonstrated cumulative

error warranting a new trial. See Grzybowicz, 747 F.3d at 1311; Capers, 708 F.3d

at 1299 (explaining a defendant’s substantial rights must be affected to warrant

relief under the cumulative error doctrine).

G. The § 2G2.1(b)(6) Enhancement




                                          35
             Case: 13-13109      Date Filed: 09/24/2014    Page: 36 of 42


      Turning to his 480-month total sentence, Mathis argues the district court

erred by applying a two-level enhancement under U.S.S.G. § 2G2.1(b)(6), which

applies if the defendant, for the purpose of producing sexually explicit material,

used “a computer or an interactive computer service to . . . persuade, induce,

entice, coerce, or facilitate the travel of, a minor to engage in sexually explicit

conduct, or to otherwise solicit participation by a minor in such conduct.”

According to Mathis, the enhancement applies only when a defendant used the

Internet in the commission of the offense and not simply because a phone with

Internet capabilities was used. We disagree.

      Section 2G2.1(b)(6) provides:

      If, for the purpose of producing sexually explicit material or for the
      purpose of transmitting such material live, the offense
      involved . . . the use of a computer or an interactive computer service
      to (i) persuade, induce, entice, coerce, or facilitate the travel of, a
      minor to engage in sexually explicit conduct, or to otherwise solicit
      participation by a minor in such conduct; or (ii) solicit participation
      with a minor in sexually explicit conduct, increase by 2 levels.

U.S.S.G. § 2G2.1(b)(6). The guidelines commentary instructs that the word

“computer” has “the meaning given that term in 18 U.S.C. § 1030(e)(1).” U.S.S.G.

§ 2G2.1 cmt. (n.1). 18 U.S.C. § 1030(e)(1), in turn, defines a computer as:

      an electronic, magnetic, optical, electrochemical, or other high speed
      data processing device performing logical, arithmetic, or storage
      functions, and includes any data storage facility or communications
      facility directly related to or operating in conjunction with such
      device, but such term does not include an automated typewriter or
      typesetter, a portable hand held calculator, or other similar device.
                                           36
             Case: 13-13109     Date Filed: 09/24/2014    Page: 37 of 42




18 U.S.C. § 1030(e)(1).

      It is an issue of first impression in this Circuit whether a cell phone is a

“computer” within the meaning of § 1030(e)(1). The Eighth Circuit, however, has

decided the issue. See United States v. Kramer, 631 F.3d 900, 902-04 (8th Cir.

2011). As that court has noted, the language of § 1030(e)(1) is broad and

encompasses any device that uses a data processor. Id. at 902. We agree with the

Eighth Circuit’s observation that “each time an electronic processor performs any

task—from powering on, to receiving keypad input, to displaying information—it

performs logical, arithmetic, or storage functions. These functions are the essence

of its operation.” Id. at 903. Nothing in the statutory definition of a computer

requires that the device have a connection to the Internet or Internet capabilities.

Id. We will not rewrite the statutory definition to exclude Mathis’s use of a

smartphone to call and send text messages to his minor victims—activities that

undoubtedly employed an electronic or high speed data processing device

performing logical, arithmetic, and storage functions. The Seventh Circuit has

explained in discussing the scope of § 1030, “[a]s more devices come to have

built-in intelligence, the effective scope of the statute grows. This might prompt

Congress to amend the statute but does not authorize the judiciary to give the

existing version less coverage than its language portends.” United States v. Mitra,



                                          37
               Case: 13-13109       Date Filed: 09/24/2014       Page: 38 of 42


405 F.3d 492, 495 (7th Cir. 2005). 12 We therefore hold that a defendant’s use of a

cell phone to call and send text messages constitutes the use of a computer, as that

term is defined in 18 U.S.C. § 1030(e)(1), and warrants imposition of an

enhancement under U.S.S.G. § 2G2.1(b)(6).

       In the alternative, even if the enhancement was not warranted, any error was

harmless. As calculated by the district court, Mathis had a combined total offense

level of 41 and a criminal history category of V, yielding a guidelines range of 360

months to life imprisonment. Without the § 2G2.1(b)(6) enhancement, Mathis’s

offense level of 39 and criminal history category of V would have still yielded a

guidelines range of 360 months to life imprisonment. See U.S.S.G. Ch. 5 pt. A,

sentencing table. Given that Mathis’s guidelines range was the same with or

without the enhancement, any potential error in applying the enhancement does not

warrant reversal. See United States v. Campa, 529 F.3d 980, 1013 (11th Cir. 2008)

(“A sentencing error, under the Guidelines, is harmless if a court considers the

proceedings in their entirety and determines that the error did not affect the

sentence or had but very slight effect.” (internal quotation marks omitted)).

H. The § 2251(e) Enhancement



       12
           We do not mean to say that every use of a device with a data processor necessarily
warrants imposition of an enhancement under § 2G2.1(b)(6). The guidelines commentary
specifies that the enhancement “is intended to apply only to the use of a computer . . . to
communicate directly with a minor,” as Mathis did in this case. U.S.S.G. § 2G2.1 cmt. (n.4).
                                               38
             Case: 13-13109     Date Filed: 09/24/2014    Page: 39 of 42


      Mathis raises several challenges to the district court’s imposition of a

sentencing enhancement under 18 U.S.C. § 2251(e). Specifically, Mathis contends

the enhancement was inapplicable because the Florida statute under which he was

convicted in 1995, i.e, § 800.04, did not require actual touching or contact with a

minor. Mathis also argues that imposition of an enhanced sentence violated his

Sixth Amendment rights.

      We review de novo the interpretation of a statute, United States v. McQueen,

727 F.3d 1144, 1151 (11th Cir. 2013), as well as preserved claims of error under

Alleyne and Apprendi v. New Jersey, 530 U.S. 466, 120 S. Ct. 2348 (2000), see

King, 751 F.3d at 1279. Section 2251 criminalizes the sexual exploitation of

minors and provides for a sentence of not less than 15 years’ or more than 30

years’ imprisonment. 18 U.S.C. § 2251(a), (e). However, if a defendant “has one

prior conviction . . . under the laws of any State relating to aggravated sexual

abuse, sexual abuse, [or] abusive sexual contact involving a minor or ward,” the

defendant is subject to a 25-year mandatory minimum and 50-year statutory

maximum sentence. Id. § 2251(e).

      1. Actual Touching or Contact

      Mathis asserts that for an enhancement to apply under § 2251(e), a prior

state conviction must have required sexual contact, not merely sexual conduct. He

maintains that because he was convicted of lewd or lascivious assault on a minor,


                                          39
               Case: 13-13109         Date Filed: 09/24/2014        Page: 40 of 42


and assault can be committed without actual touching, his conviction under

§ 800.04 of the Florida Statutes was not a qualifying offense.13

       Mathis’s argument is unavailing. His reading of § 2251(e) ignores the plain

text of the statute, which provides for an enhanced sentencing range if the

defendant has previously been convicted under a state law relating to sexual abuse

of a minor. See 18 U.S.C. § 2251(e). We have interpreted the phrase “relating to”

broadly in the context of child exploitation offenses, and have held that a

defendant’s prior conviction under Georgia law for discussing illicit sexual acts

with a minor warranted an enhancement under § 2251(e). See United States v.

McGarity, 669 F.3d 1218, 1262-63 (11th Cir. 2012). We have also held that the

plain meaning of the phrase “sexual abuse of a minor” includes “acts that involve

physical contact between the perpetrator and the victim as well as acts that do not.”

United States v. Padilla-Reyes, 247 F.3d 1158, 1163 (11th Cir. 2001). Mathis

cannot avoid our clear pronouncement that “the phrase ‘sexual abuse of a minor’

means a perpetrator’s physical or nonphysical misuse or maltreatment of a minor

for a purpose associated with sexual gratification.” Id. Mathis’s prior state

conviction under § 800.04 for lewd or lascivious assault on a child related to the



       13
           At the time of Mathis’s offense, § 800.04 provided in pertinent part that “[a] person
who . . . [h]andles, fondles, or assaults any child under the age of 16 years in a lewd, lascivious,
or indecent manner . . . without committing the crime of sexual battery, commits a felony of the
second degree.” Fla. Stat. § 800.04(1) (1994).
                                                 40
             Case: 13-13109     Date Filed: 09/24/2014    Page: 41 of 42


sexual abuse of a minor and the district court did not err by enhancing his sentence

under § 2251(e).

      2. The Sixth Amendment

      Finally, to preserve the issue, Mathis argues that the Supreme Court’s

decision in Almendarez-Torres v. United States, 523 U.S. 224, 118 S. Ct. 1219

(1998), does not apply to this case and the district court’s imposition of a statutory

sentencing enhancement violated his Sixth Amendment rights. Mathis’s argument

is squarely foreclosed by Circuit precedent, see King, 751 F.3d at 1280 (rejecting

the argument that Alleyne is inconsistent with Almendarez-Torres); United States v.

Shelton, 400 F.3d 1325, 1329 (11th Cir. 2005) (explaining that the Supreme

Court’s holding in Almendarez-Torres was left undisturbed by Apprendi), and we

adhere to the Supreme Court’s holding in Almendarez-Torres that “the

Government need not allege in its indictment and need not prove beyond a

reasonable doubt that a defendant had prior convictions for a district court to use

those convictions for purposes of enhancing a sentence,” King, 751 F.3d at 1280

(internal quotation marks and brackets omitted).

                                III. CONCLUSION

      For the foregoing reasons, we affirm Mathis’s convictions and sentences.

However, we note the judgment states Mathis was convicted on Count Two of




                                          41
               Case: 13-13109       Date Filed: 09/24/2014      Page: 42 of 42


production and attempted production of child pornography. 14 We remand to the

district court for the limited purpose of correcting the judgment to reflect that

Mathis was convicted on Count Two only of attempted production of child

pornography. See United States v. Reeves, 742 F.3d 487, 507 n.12 (11th Cir. 2014)

(“We may sua sponte raise the issue of clerical errors in a judgment and remand

with instructions that the district court correct them.”).

       AFFIRMED and REMANDED.




       14
         During the sentencing hearing, the district court judge imposed Mathis’s sentence on
each count by count number. Count Two charged Mathis with attempted production of child
pornography and the typographical error occurred in the clerical entry of “Nature of Offense.”
                                               42

```

---

## GROUP: _overhaul2/lake/cases/United States v. Matlock.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Matlock"
type: case
citation: "415 U.S. 164 (1974)"
parallel_cite: "94 S. Ct. 988; 39 L. Ed. 2d 242"
neutral_cite: 1974 U.S. LEXIS 8
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1974
date_decided: 1974-02-20
docket: 72-1355
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1974-02-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Matlock
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108967/united-states-v-matlock/"
  cluster_id: 108967
  opinion_id: 9425606
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Key — Anchor"
related: ["[[Illinois v. Rodriguez]]", "[[Georgia v. Randolph]]", "[[Fernandez v. California]]", "[[Schneckloth v. Bustamonte]]", "[[Frazier v. Cupp]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent-search", "third-party-consent", "common-authority", "joint-access"]
holding: "COMMON AUTHORITY: consent of one who possesses common authority over premises or effects is valid against an absent, nonconsenting…"
lake:
  record_id: United States v. Matlock
  status: verified
  projected_at: 2026-07-09
---

# United States v. Matlock

*415 U.S. 164 (1974)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Matlock was arrested in the front yard of a house where he lived with Mrs. Gayle Graff and her family. Officers did not ask Matlock for consent; instead Mrs. Graff consented to a search of the house, including the east bedroom she said she jointly occupied with him. In a diaper bag in the bedroom closet, officers found $4,995 in cash — evidence of a bank robbery. At the [[Common Legal Terms#suppression-hearing|suppression hearing]] the District Court excluded, as hearsay, Mrs. Graff's out-of-court statements that she and Matlock shared the bedroom, and suppressed the money.

## Issue
Whether a third party's voluntary consent to search shared premises is valid against an absent, nonconsenting co-occupant, and what the Government must show about that party's authority over the premises.

## Rule
A co-occupant with common authority may consent for the absent one. "The consent of one who possesses common authority over premises or effects is valid as against the absent, nonconsenting person with whom that authority is shared." — 415 U.S. at 170. ^pin-170

The prosecution "may show that permission to search was obtained from a third party who possessed common authority over or other sufficient relationship to the premises or effects sought to be inspected." — [*Id.* at 171](https://www.courtlistener.com/opinion/108967/united-states-v-matlock/#:~:text=may%20show%20that%20permission%20to). ^pin-171

Common authority is not a property concept; it rests on shared use: it "rests rather on mutual use of the property by persons generally having joint access or control for most purposes, so that it is reasonable to recognize that any of the co-inhabitants has the right to permit the inspection in his own right and that the others have assumed the risk that one of their number might permit the common area to be searched." — [*Id.* at 171](https://www.courtlistener.com/opinion/108967/united-states-v-matlock/#:~:text=rests%20rather%20on%20mutual%20use) n.7. ^pin-171a

## Application
On these facts the validity of the consent turned on whether Mrs. Graff had common authority over the east bedroom, and the District Court had wrongly kept out the evidence bearing on that question. The excluded statements and other proof tended to show that she and Matlock jointly occupied and used the bedroom; if she did share mutual use with joint access or control, her consent was valid against the absent Matlock, who had assumed the risk that a co-occupant might permit a search of the common area. Because the suppression rested on the erroneous exclusion of that evidence (including Mrs. Graff's admissions and her statements as relevant to her authority), the Court reversed and [[Reading and Citing Cases#on-remand|remanded]] for the lower courts to decide, on the full record, whether the Government had carried its burden of proving common authority.

## Conclusion
[[Consent Searches|Third-party consent]] by a co-occupant with common authority is valid against an absent co-occupant; the suppression order was reversed and the case [[Reading and Citing Cases#on-remand|remanded]] to determine whether Mrs. Graff possessed common authority over the bedroom.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Matlock* is the anchor for [[Consent Searches|third-party consent]]: [[Illinois v. Rodriguez]] extends it to officers' reasonable mistakes about *apparent* authority; [[Georgia v. Randolph]] carves out the *physically present, expressly objecting* co-occupant; and [[Fernandez v. California]] limits *[[Georgia v. Randolph|Randolph]]* to a present objector.

## Appears on
- [[Consent Searches]] — *Key — Anchor*

## Sources
- *United States v. Matlock*, 415 U.S. 164 (1974) — https://www.courtlistener.com/opinion/108967/united-states-v-matlock/ — pinpoints: 170, 171, 171 n.7.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8bcc9efbff4169c0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Matlock"}, "payload": {"all": [{"cite": "415 U.S. 164", "page": "164", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "415"}, {"cite": "94 S. Ct. 988", "page": "988", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "94"}, {"cite": "39 L. Ed. 2d 242", "page": "242", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "39"}, {"cite": "1974 U.S. LEXIS 8", "page": "8", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1974"}], "display": "415 U.S. 164", "official": {"cite": "415 U.S. 164", "page": "164", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "415"}, "official_selection_present": true, "record_id": "United States v. Matlock"}}
{"assertion_id": "7437f773d186f8b3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-170", "record_id": "United States v. Matlock"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-170", "pinpoint_status": "slip-only", "quote": "--- # United States v. Matlock *415 U.S. 164 (1974)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Matlock was arrested in the front yard of a house where he lived with Mrs. Gayle Graff and her family. Officers did not ask Matlock for consent; instead Mrs. Graff consented to a search of the house, including the east bedroom she said she jointly occupied with him. In a diaper bag in the bedroom closet, officers found $4,995 in cash — evidence of a bank robbery. At the suppression hearing the District Court excluded, as hearsay, Mrs. Graff's out-of-court statements that she and Matlock shared the bedroom, and suppressed the money. ## Issue Whether a third party's voluntary consent to search shared premises is valid against an absent, nonconsenting co-occupant, and what the Government must show about that party's authority over the premises. ## Rule A co-occupant with common authority may consent for the absent one.", "quote_fidelity": "mismatch", "record_id": "United States v. Matlock", "star_marker": null}}
{"assertion_id": "a025d7b426c942f9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-171a", "record_id": "United States v. Matlock"}, "payload": {"fragment": "#:~:text=rests%20rather%20on%20mutual%20use", "page": null, "pin_id": "pin-171a", "pinpoint_status": "star-verified", "quote": "rests rather on mutual use of the property by persons generally having joint access or control for most purposes, so that it is reasonable to recognize that any of the co-inhabitants has the right to permit the inspection in his own right and that the others have assumed the risk that one of their number might permit the common area to be searched.", "quote_fidelity": "matched", "record_id": "United States v. Matlock", "star_marker": "170"}}
{"assertion_id": "e87e3d04275f3c2a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-171", "record_id": "United States v. Matlock"}, "payload": {"fragment": "#:~:text=may%20show%20that%20permission%20to", "page": null, "pin_id": "pin-171", "pinpoint_status": "star-verified", "quote": "may show that permission to search was obtained from a third party who possessed common authority over or other sufficient relationship to the premises or effects sought to be inspected.", "quote_fidelity": "matched", "record_id": "United States v. Matlock", "star_marker": "171"}}
{"assertion_id": "94995bfa15e8a0f4", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Matlock"}, "payload": {"as_of_content": "1974-02-20", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Matlock", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Matlock

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Matlock",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Matlock",
    "case_name_short": "Matlock",
    "case_name_full": "United States v. Matlock",
    "input_case_name": "United States v. Matlock",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1974-02-20",
    "year": 1974,
    "docket": "72-1355",
    "cluster_id": 108967,
    "lead_opinion_id": 9425606,
    "sibling_ids": [
      108967,
      9425606,
      9425607,
      9425608
    ],
    "absolute_url": "/opinion/108967/united-states-v-matlock/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "415 U.S. 164",
      "volume": "415",
      "reporter": "U.S.",
      "page": "164",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "94 S. Ct. 988",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "988",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "39 L. Ed. 2d 242",
        "volume": "39",
        "reporter": "L. Ed. 2d",
        "page": "242",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1974 U.S. LEXIS 8",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "8",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "415 U.S. 164",
        "volume": "415",
        "reporter": "U.S.",
        "page": "164",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 S. Ct. 988",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "988",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "39 L. Ed. 2d 242",
        "volume": "39",
        "reporter": "L. Ed. 2d",
        "page": "242",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1974 U.S. LEXIS 8",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "8",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "415 U.S. 164",
    "official_selection": {
      "court_class": "scotus",
      "selected": "415 U.S. 164",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-170",
      "page": null,
      "quote": "--- # United States v. Matlock *415 U.S. 164 (1974)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Matlock was arrested in the front yard of a house where he lived with Mrs. Gayle Graff and her family. Officers did not ask Matlock for consent; instead Mrs. Graff consented to a search of the house, including the east bedroom she said she jointly occupied with him. In a diaper bag in the bedroom closet, officers found $4,995 in cash \u2014 evidence of a bank robbery. At the suppression hearing the District Court excluded, as hearsay, Mrs. Graff's out-of-court statements that she and Matlock shared the bedroom, and suppressed the money. ## Issue Whether a third party's voluntary consent to search shared premises is valid against an absent, nonconsenting co-occupant, and what the Government must show about that party's authority over the premises. ## Rule A co-occupant with common authority may consent for the absent one.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-171",
      "page": null,
      "quote": "may show that permission to search was obtained from a third party who possessed common authority over or other sufficient relationship to the premises or effects sought to be inspected.",
      "star_marker": "171",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 10811,
      "fragment": "#:~:text=may%20show%20that%20permission%20to",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-171a",
      "page": null,
      "quote": "rests rather on mutual use of the property by persons generally having joint access or control for most purposes, so that it is reasonable to recognize that any of the co-inhabitants has the right to permit the inspection in his own right and that the others have assumed the risk that one of their number might permit the common area to be searched.",
      "star_marker": "170",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 32667,
      "fragment": "#:~:text=rests%20rather%20on%20mutual%20use",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1974-02-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Matlock",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "United States v. Matlock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. H. K. D. S. (A163158)",
          "cluster_id": 10133573,
          "cite": [
            "305 Or. App. 86",
            "469 P.3d 770"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jones",
          "cluster_id": 4517594,
          "cite": [
            "193 A.3d 957"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Washington v. Amanda Marie Torres",
          "cluster_id": 4389851,
          "cite": [
            "198 Wash. App. 864",
            "397 P.3d 900"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thomas Rigterink v. State of Florida",
          "cluster_id": 3196514,
          "cite": [
            "193 So. 3d 846",
            "41 Fla. L. Weekly Supp. 177",
            "2016 WL 1592714",
            "2016 Fla. LEXIS 835"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Glenda Smith v. City of Wyoming",
          "cluster_id": 3194781,
          "cite": [
            "821 F.3d 697",
            "2016 FED App. 0094P",
            "2016 U.S. App. LEXIS 6833",
            "2016 WL 1533998"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "CIAN PRIDGEN v. UNITED STATES.",
          "cluster_id": 3192171,
          "cite": [
            "134 A.3d 297",
            "2016 D.C. App. LEXIS 91",
            "2016 WL 1392012"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane1_negative"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nixon",
          "cluster_id": 109101,
          "cite": [
            "41 L. Ed. 2d 1039",
            "94 S. Ct. 3090",
            "418 U.S. 683",
            "1974 U.S. LEXIS 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raddatz",
          "cluster_id": 110315,
          "cite": [
            "65 L. Ed. 2d 424",
            "100 S. Ct. 2406",
            "447 U.S. 667",
            "1980 U.S. LEXIS 49"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bourjaily v. United States",
          "cluster_id": 111938,
          "cite": [
            "97 L. Ed. 2d 144",
            "107 S. Ct. 2775",
            "483 U.S. 171",
            "1987 U.S. LEXIS 2874",
            "22 Fed. R. Serv. 1105",
            "55 U.S.L.W. 4962"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patrick v. State",
          "cluster_id": 1713584,
          "cite": [
            "906 S.W.2d 481",
            "1995 WL 379872"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Orange Jell Beechum",
          "cluster_id": 358983,
          "cite": [
            "582 F.2d 898",
            "1978 U.S. App. LEXIS 8198",
            "3 Fed. R. Serv. 1185"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Medina v. California",
          "cluster_id": 112775,
          "cite": [
            "120 L. Ed. 2d 353",
            "112 S. Ct. 2572",
            "505 U.S. 437",
            "1992 U.S. LEXIS 3696"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karo",
          "cluster_id": 111257,
          "cite": [
            "82 L. Ed. 2d 530",
            "104 S. Ct. 3296",
            "468 U.S. 705",
            "1984 U.S. LEXIS 148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Balentine v. State",
          "cluster_id": 1662103,
          "cite": [
            "71 S.W.3d 763",
            "2002 WL 496960"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Frye",
          "cluster_id": 5607916,
          "cite": [
            "18 Cal. 4th 894",
            "98 Cal. Daily Op. Serv. 5949",
            "959 P.2d 183",
            "98 Daily Journal DAR 8259",
            "77 Cal. Rptr. 2d 25",
            "1998 Cal. LEXIS 4688"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Valtierra v. State",
          "cluster_id": 1370428,
          "cite": [
            "310 S.W.3d 442",
            "2010 Tex. Crim. App. LEXIS 828",
            "2010 WL 1850384"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oles v. State",
          "cluster_id": 1762668,
          "cite": [
            "993 S.W.2d 103",
            "1999 Tex. Crim. App. LEXIS 53",
            "1999 WL 330266"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Montoya",
          "cluster_id": 1202376,
          "cite": [
            "753 P.2d 729",
            "12 Brief Times Rptr. 482",
            "1988 Colo. LEXIS 39",
            "1988 WL 25119"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bruce A. Campbell v. United States District Court for the Northern District of California",
          "cluster_id": 320998,
          "cite": [
            "501 F.2d 196"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Stone",
          "cluster_id": 4958214,
          "cite": [
            "2021 COA 104"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ford v. State",
          "cluster_id": 2187417,
          "cite": [
            "305 S.W.3d 530",
            "2009 Tex. Crim. App. LEXIS 1440",
            "2009 WL 3365661"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Donald James and David Anthony Butler, United States of America v. Henry Smith and Kenneth Wayne Whitmore",
          "cluster_id": 362801,
          "cite": [
            "590 F.2d 575",
            "1979 U.S. App. LEXIS 17005",
            "3 Fed. R. Serv. 785"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hill v. National Collegiate Athletic Assn.",
          "cluster_id": 1235436,
          "cite": [
            "865 P.2d 633",
            "7 Cal. 4th 1",
            "26 Cal. Rptr. 2d 834",
            "94 Cal. Daily Op. Serv. 681",
            "94 Daily Journal DAR 1141",
            "9 I.E.R. Cas. (BNA) 716",
            "1994 Cal. LEXIS 9"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108967 OR 9425606 OR 9425607 OR 9425608) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDQxNjcwNDAwMDAwJnM9Mjg5ODIxNiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108967+OR+9425606+OR+9425607+OR+9425608%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(108967 OR 9425606 OR 9425607 OR 9425608)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMzAmcz0yMDk0NzcyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108967+OR+9425606+OR+9425607+OR+9425608%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108967 OR 9425606 OR 9425607 OR 9425608)",
        "reviewed": 60,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 60,
        "triage_read": 0,
        "triage_snippet_classified": 60
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108967 OR 9425606 OR 9425607 OR 9425608)",
    "indexed_citing_opinions": 2399,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108967,
        "count": 2188,
        "count_source": "search"
      },
      {
        "opinion_id": 9425606,
        "count": 255,
        "count_source": "search"
      },
      {
        "opinion_id": 9425607,
        "count": 1,
        "count_source": "search"
      },
      {
        "opinion_id": 9425608,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3649,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-matlock.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxNzE1NDImcz0xMDMxNjc5MSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28108967+OR+9425606+OR+9425607+OR+9425608%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108967,
        "cited_id": 97847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 104184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 107394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 108212,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 108429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 233305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 264623,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 267102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 268073,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 276553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 278916,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 288276,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 292123,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 292716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 298539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 303962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 310284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 1359720,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 1656389,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 1976399,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 2059444,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 3868069,
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
    "date_created": "2026-07-06T01:32:24Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:33:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:33:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:37:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:33:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Matlock

```
<opinion type="majority">
<author id="b233-11">MR. Justice White</author>
<p id="A8b">delivered the opinion of the Court.</p>
<p id="b233-12">In <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973), the Court reaffirmed the principle that the search of property, without warrant and without probable cause, <page-number citation-index="1" label="166">*166</page-number>but with proper consent voluntarily given, is valid under the Fourth Amendment. The question now before us is whether the evidence presented by the United States with respect to the voluntary consent of a third party to search the living quarters of the respondent was legally sufficient to render the seized materials admissible in evidence at the respondent's criminal trial.</p>
<p id="b234-5">I</p>
<p id="b234-6">Respondent Matlock was indicted in February 1971 for the robbery of a federally insured bank in Wisconsin, in violation of <span class="citation no-link">18 U. S. C. § 2113</span>. A week later, he filed a motion to suppress evidence seized by law enforcement officers from a home in the town of Pardeeville, Wisconsin, in which he had been living. Suppression hearings followed. As found by the District Court, the facts were that respondent was arrested in the yard in front of the Pardeeville home on November 12, 1970. The home was leased from the owner by Mr. and Mrs. Marshall. Living in the home were Mrs. Marshall, several of her children, including her daughter Mrs. Gayle Graff, Gayle's three-year-old son, and respondent. Although the officers were aware at the time of the arrest that respondent lived in the house, they did not ask him which room he occupied or whether he would consent to a search. Three of the arresting officers went to the door of the house and were admitted by Mrs. Graff, who was dressed in a robe and was holding her son in her arms. The officers told her they were looking for money and a gun and asked if they could search the house. Although denied by Mrs. Graff at the suppression hearings, it was found that she consented voluntarily to the search of the house, including the east bedroom on the second floor which she said was jointly occupied by Matlock and herself. The east bedroom was searched and the evidence at issue here, $4,995 in cash, was found in a diaper <page-number citation-index="1" label="167">*167</page-number>bag in the only closet in the room.<footnotemark>1</footnotemark> The issue came to be whether Mrs. Graff's relationship to the east bedroom was sufficient to make her consent to the search valid against respondent Matlock.</p>
<p id="b235-5">The District Court ruled that before the seized evidence could be admitted at trial the Government'had to prove, first, that it reasonably appeared to the searching officers “just prior to the search, that facts exist which will render the consenter’s consent binding on the putative defendant,” and, second, that “just prior to the search, facts do exist which render the consenter’s consent binding on the putative defendant.” There was no requirement that express permission from respondent to Mrs. Graff to allow the officers to search be shown; it was sufficient to show her authority to consent in her own right, by reason of her relationship to the premises. The first requirement was held satisfied because of respondent’s presence in the yard of the house at the time of his arrest, because of Gayle Graff’s residence in the house for some time and her presence in the house just prior to the search, and because of her statement to the officers that she and ‘ the respondent occupied the east bedroom.<footnotemark>2</footnotemark></p>
<p id="b235-6">The District Court concluded, however, that the Government had failed to satisfy the second requirement and <page-number citation-index="1" label="168">*168</page-number>had not satisfactorily proved Mrs. Graff's actual authority to consent to the search. To arrive at this result, the District Court held that although Gayle Graff’s statements to the officers that she and the respondent occupied the east bedroom were admissible to prove the good-faith belief of the officers, they were nevertheless extrajudicial statements inadmissible to prove the truth of the facts therein averred. The same was true of Mrs. Graff’s additional statements to the officers later on November 12 that she and the respondent had been sleeping together in the east bedroom regularly, including the early morning of November 12, and that she and respondent shared the use of a dresser in the room. There was also testimony that both Gayle Graff and respondent, at various times and places and to various persons, had made statements that they were wife and husband. These statements were deemed inadmissible to prove that respondent and Gayle Graff were married, which they were not, or that they were sleeping together .as a husband and wife might be expected to do. Having excluded these declarations, the District Court then concluded that the remaining evidence was insufficient to prove “to a reasonable certainty, by the greater weight of the credible evidence, that at the time of the search, and for some period of reasonable length theretofore, Gayle Graff and the defendant were living together in the east bedroom.” The remaining evidence, briefly stated, was that Mrs. Graff and respondent had lived together in a one-bedroom apartment in Florida from April to August 1970; that they lived at the Marshall home in Pardeeville from August to November 12, 1970; that they were several times seen going up or down stairs in the house together; and that the east bedroom, which respondent was shown to have rented from Mr. and Mrs. Marshall, contained evidence that it was also lived in by <page-number citation-index="1" label="169">*169</page-number>a man and a woman.<footnotemark>3</footnotemark> The District Court thought these items of evidence created an “inference” or at least a “mild inference” that respondent and Gayle Graff at times slept together in the east bedroom, but it deemed them insufficient to satisfy the Government’s burden of proof. The District Court also rejected the Government’s claim that it was required to prove only that at the time of the search the officers could reasonably have concluded that Gayle Graff’s relationship to the east bedroom was sufficient to make her consent binding on respondent.</p>
<p id="b237-5">The Court of Appeals affirmed the judgment of the District Court in all respects. <span class="citation" data-id="310284"><a href="/opinion/310284/united-states-v-william-earl-matlock/" aria-description="Citation for case: United States v. William Earl Matlock">476 F. 2d 1083</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./412/917/">412 U. S. 917</a></span>, and now reverse the Court of Appeals.</p>
<p id="b237-6">II</p>
<p id="b237-7">It has been assumed by the parties and the courts below that the voluntary consent of any joint occupant of a residence to search the premises jointly occupied is valid against the co-occupant, permitting evidence discovered in the search to be used against him at a criminal trial. This basic proposition was accepted by the Seventh Circuit in this case, <span class="citation" data-id="310284"><a href="/opinion/310284/united-states-v-william-earl-matlock/#1086" aria-description="Citation for case: United States v. William Earl Matlock">476 F. 2d, at 1086</a></span>, as it had been in prior cases,<footnotemark>4</footnotemark> and has generally been ap<page-number citation-index="1" label="170">*170</page-number>plied in similar circumstances by other courts of appeals,<footnotemark>5</footnotemark> and various state courts.<footnotemark>6</footnotemark> This Court left open, in <em>Amos </em>v. <em>United States, </em><span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/#317" aria-description="Citation for case: Amos v. United States">255 U. S. 313, 317</a></span> (1921), the question whether a wife’s permission to search the residence in which she lived with her husband could “waive his constitutional rights,” but more recent authority here clearly indicates that the consent of one who possesses common authority over premises or effects is valid as against the absent, nonconsenting person with whom that authority is shared. In <em>Frazier </em>v. <em>Cupp, </em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#740" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 740</a></span> (1969), the Court “dismissed rather quickly” the contention that the consent of the petitioner’s cousin to the search of a duffel bag, which was being used jointly by both men and had been left in the cousin’s home, would not justify the seizure of petitioner’s cloth<page-number citation-index="1" label="171">*171</page-number>ing found inside; joint use of the bag rendered the cousin’s authority to consent to its search clear. Indeed, the Court was unwilling to engage in the “metaphysical subtleties” raised by Frazier’s claim that his cousin only had permission to use one compartment within the bag. By allowing the cousin the use of the bag, and by leaving it in his house, Frazier was held to have assumed the risk that his cousin would allow someone else to look inside. <em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/" aria-description="Citation for case: Frazier v. Cupp">Ibid.</a></span> </em>More generally, in <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#245" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., at 245-246</a></span>, we noted that our prior recognition of the constitutional validity of “third party consent” searches in cases like <em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/" aria-description="Citation for case: Frazier v. Cupp">Frazier</a></span> </em>and <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#487" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 487-490</a></span> (1971), supported the view that a consent search is fundamentally different in nature from the waiver of a trial right. These cases at least make clear that when the prosecution seeks to justify a warrantless search by proof of voluntary consent, it is not limited to proof that consent was given by the defendant, but may show that permission to search was obtained from a third party who possessed common authority over or other sufficient relationship to the premises or effects sought to be inspected.<footnotemark>7</footnotemark> The <page-number citation-index="1" label="172">*172</page-number>issue now before us is whether the Government made the requisite showing in this case.</p>
<p id="b240-4">Ill</p>
<p id="b240-5">The District Court excluded from evidence at the suppression hearings, as inadmissible hearsay, the out-of-court statements of Mrs. Graff with respect to her and respondent’s joint occupancy and use of the east bedroom, as well as the evidence that both respondent and Mrs. Graff at various times and to various persons had represented themselves as husband and wife. The Court of Appeals affirmed the ruling. Both courts were in error.</p>
<p id="b240-6">As an initial matter we fail to understand why, on any approach to the case, the out-of-court representations of respondent himself that he and Gayle Graff were husband and wife were considered to be inadmissible against him. Whether or not Mrs. Graff’s statements were hearsay, the respondent’s own out-of-court admissions would surmount all objections based on the hearsay rule both at the suppression hearings and at the trial itself, and would be admissible for whatever inferences the trial judge could reasonably draw concerning joint occupancy of the east bedroom. See 4 J. Wigmore, Evidence § 1048 (J. Chadbourn rev. 1972); C. McCormick, Evidence § 262 (2d ed. 1972).<footnotemark>8</footnotemark></p>
<p id="b240-7">As for Mrs. Graff’s statements to the searching officers, it should be recalled that the rules of evidence normally applicable in criminal trials do not operate with full force at hearings before the judge to determine the admissi<page-number citation-index="1" label="173">*173</page-number>bility of evidence.<footnotemark>9</footnotemark> In <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949), it was objected that hearsay had been used at the hearing on a challenge to the admissibility of evidence seized when a car was searched and that other evidence used at the hearing was held inadmissible at the trial itself. The Court sustained the trial court’s rulings. It distinguished between the rules applicable to proceedings to determine probable cause for arrest and search and those governing the criminal trial itself— “There is a large difference between the two things to be proved, as well as between the tribunals which determine them, and therefore a like difference in the <em>quanta </em>and modes of proof required to establish them.” <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#173" aria-description="Citation for case: Brinegar v. United States"><em>Id., </em>at 173</a></span>. That certain evidence was admitted in preliminary proceedings but excluded at the trial — and the Court thought both rulings proper- — was thought merely to “illustrate the difference in standards and latitude allowed in passing upon the distinct issues of probable cause and guilt.” <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#174" aria-description="Citation for case: Brinegar v. United States"><em>Id., </em>at 174</a></span>.</p>
<p id="b241-5">That the same rules of evidence governing criminal jury trials are not generally thought to govern hearings before a judge to determine evidentiary questions was confirmed on November 20, 1972, when the Court transmitted to Congress the proposed Federal Rules of Evidence. Rule 104 (a) provides that preliminary questions concerning admissibility are matters for <page-number citation-index="1" label="174">*174</page-number>the judge and that in performing this function he is not bound by the Rules of Evidence except those with respect to privileges.<footnotemark>10</footnotemark> Essentially the same language on the scope of the proposed Rules is repeated in Rule 1101 (d)(1).<footnotemark>11</footnotemark> The Rules in this respect reflect the general views of various authorities on evidence. 5 J. Wigmore, Evidence § 1385 (3d ed. 1940); C. McCormick, Evidence §53, p. 122 n. 91 (2d ed. 1972). See also Maguire &amp; Epstein, Rules of Evidence in Preliminary Controversies as to Admissibility, 36 Yale L. J. 1101 (1927).</p>
<p id="b242-5">Search warrants are repeatedly issued on <em>ex parte </em>affidavits containing out-of-court statements of identified and unidentified persons. <em>United States </em>v. <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 108</a></span> (1965). An arrest and search without a warrant were involved in <em>McCray </em>v. <em>Illinois, </em><span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300</a></span> (1967). At the initial suppression hearing, the police proved probable cause for the arrest by testifying to the out-of-court statements of an unidentified informer. The Government would have been obligated to produce the informer and to put him on the stand had it wanted to use his testimony at defendant's trial, but we sustained the use of his out-of-court statements at the suppression hearing, as well as the Govern-<page-number citation-index="1" label="175">*175</page-number>merit’s refusal to identify him. In the course of the opinion, we specifically rejected the claim that defendant’s right to confrontation under the Sixth Amendment and Due Process Clause of the Fourteenth Amendment had in any way been violated. We also made clear that there was no contrary rule governing proceedings in the federal courts.</p>
<p id="b243-5">There is, therefore, much to be said for the proposition that in proceedings where the judge himself is considering the admissibility of evidence, the exclusionary rules, aside from rules of privilege, should not be applicable; and the judge should receive the evidence and give it such weight as his judgment and experience counsel.<footnotemark>12</footnotemark> However that may be, certainly there should be no automatic rule against the reception of hearsay evidence in such proceedings, and it seems equally clear to us that the trial judge should not have excluded Mrs. Graff’s statements in the circumstances present here.</p>
<p id="b243-6">In the first place, the court was quite satisfied that the statements had in fact been made. Second, there is nothing in the record to raise serious doubts about the truthfulness of the statements themselves. Mrs. Graff harbored no hostility or bias against respondent that might call her statements into question. Indeed, she testified on his behalf at the suppression hearings. Mrs. Graff responded to inquiry at the time of the search that she and respondent occupied the east bedroom together. A few minutes later, having led the officers to the bedroom, she stated that she and respondent shared the one dresser in the room and that the woman’s clothing in the <page-number citation-index="1" label="176">*176</page-number>room was hers. Later the same day, she stated to the officers that she and respondent had slept together regularly in the room, including the early morning of that very day. These statements were consistent with one another. They were also corroborated by other evidence received at the suppression hearings: Mrs. Graff and respondent had lived together in Florida for several months immediately prior to coming to Wisconsin, where they lived in the house in question and where they were seen going upstairs together in the evening; respondent was the tenant of the east bedroom and that room bore every evidence that it was also occupied by a woman; respondent indicated in prior statements to various people that he and Mrs. Graff were husband and wife. Under these circumstances there was no apparent reason for the judge to distrust the evidence and to exclude Mrs. Graff’s declarations from his own consideration for whatever they might be worth in resolving, one way or another, the issues raised at the suppression hearings.</p>
<p id="b244-5">If there is remaining doubt about the matter, it should be dispelled by another consideration: cohabitation out of wedlock would not seem to be a relationship that one would falsely confess. Respondent and Gayle Graff were not married, and cohabitation out of wedlock is a crime in the State of Wisconsin.<footnotemark>13</footnotemark> Mrs. Graff’s statements were against her penal interest and they carried their own indicia of reliability. This was sufficient in itself, we think, to warrant admitting them to evidence for consideration by the trial judge. This <page-number citation-index="1" label="177">*177</page-number>is the case even if they would be inadmissible hearsay at respondent's trial either because statements against penal interest are to be excluded under <em>Donnelly </em>v. <em>United States, </em><span class="citation" data-id="97847"><a href="/opinion/97847/donnelly-v-united-states/#272" aria-description="Citation for case: Donnelly v. United States">228 U. S. 243, 272-277</a></span> (1913), or because, if Rule 804 (b) (4) of the proposed Federal Rules of Evidence becomes the law, such declarations would be admissible only if the declarant is unavailable at the time of the trial.</p>
<p id="b245-5">Finally, we note that Mrs. Graff was a witness for the respondent at the suppression hearings. As such, she was available for cross-examination,-and the risk of prejudice, if there was any, from the use of hearsay was reduced. Indeed, she entirely denied that she either gave consent or made the November 12 statements to the officers that the District Court excluded from evidence. When asked whether in fact she and respondent had lived together, she claimed her privilege against self-incrimination and declined to answer.</p>
<p id="b245-6">IV</p>
<p id="b245-7">It appears to us, given the admissibility of Mrs. Graff’s and respondent’s out-of-court statements, that the Government sustained its burden of proving by the preponderance of the evidence that Mrs. Graff’s voluntary consent to search the east bedroom was legally sufficient to warrant admitting into evidence the $4,995 found in the diaper bag.<footnotemark>14</footnotemark> But we prefer that the District Court <page-number citation-index="1" label="178">*178</page-number>first reconsider the sufficiency of the evidence in the light of this decision and opinion. The judgment of the Court of Appeals is reversed and the case is remanded to the Court of Appeals with directions to remand the case to the District Court for further proceedings consistent with this opinion.</p>
<p id="b246-5">
<em>So ordered.</em>
</p>
<footnote label="1">
<p id="b235-7"> There were other seizures in the house and the east bedroom on November 12, but none of them is at issue here.</p>
</footnote>
<footnote label="2">
<p id="b235-8"> Mrs. Graff was not advised that she had a right to refuse to consent to the search. The District Court expressed no view as to whether the absence of such advice would render her consent invalid, since it found that her consent, however voluntary, would not bind the respondent with regard to the search of his room. <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973), has since made clear, of course, that it is not essential for the prosecution to show that the consenter knew of the right to refuse consent in order to establish that the consent was voluntary.</p>
</footnote>
<footnote label="3">
<p id="b237-8"> When the officers searched the east bedroom, two pillows were on the double bed, which had been slept in, men’s and women's clothes were in the closet, and men’s and women’s clothes were also in separate drawers of the dresser.</p>
</footnote>
<footnote label="4">
<p id="b237-9"><em> E. g., United States </em>v. <em>Stone, </em><span class="citation" data-id="9459007"><a href="/opinion/307293/united-states-v-ervin-w-stone/#173" aria-description="Citation for case: United States v. Ervin W. Stone">471 F. 2d 170, 173</a></span> (1972), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./411/931/">411 U. S. 931</a></span> (1973); <em>United States </em>v. <em>Wixom, </em><span class="citation" data-id="296244"><a href="/opinion/296244/united-states-v-roswell-william-wixom/#624" aria-description="Citation for case: United States v. Roswell William Wixom">441 F. 2d 623, 624-625</a></span> (1971); <em>United States </em>v. <em>Airdo, </em><span class="citation" data-id="276553"><a href="/opinion/276553/united-states-v-dominic-daniel-alrdo/#106" aria-description="Citation for case: United States v. Dominic Daniel Alrdo">380 F. 2d 103, 106-107</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./389/913/">389 U. S. 913</a></span> (1967). Each of these cases cited with approval <em>United States </em>v. <em>Sferas, </em><span class="citation" data-id="233305"><a href="/opinion/233305/united-states-v-sferas-two-cases-united-states-v-skally/#74" aria-description="Citation for case: United States v. Sferas (Two Cases). United States v. Skally">210 F. 2d 69, 74</a></span> (CA7), cert. denied <em>sub nom. Skally </em>v. <em>United States, </em><span class="citation" data-id="8925459"><a href="/opinion/8935196/skally-v-united-states/" aria-description="Citation for case: Skally v. United States">347 U. S. 935</a></span> (1954), which expressed the rule "that where two persons have equal rights <page-number citation-index="1" label="170">*170</page-number>to the use or occupation of premises, either may give consent to a search, and the evidence thus disclosed can be used against either.”</p>
</footnote>
<footnote label="5">
<p id="AKp"><em> E. g., United States </em>v. <em>Ellis, </em><span class="citation" data-id="303962"><a href="/opinion/303962/united-states-v-robert-w-ellis/#967" aria-description="Citation for case: United States v. Robert W. Ellis">461 F. 2d 962, 967-968</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./409/866/">409 U. S. 866</a></span> (1972); <em>United States </em>v. <em>Cataldo, </em><span class="citation" data-id="292716"><a href="/opinion/292716/united-states-v-joseph-cataldo-and-james-lucakos-aka-james-lucas-tn/#40" aria-description="Citation for case: United States v. Joseph Cataldo and James Lucakos, A/K/A...">433 F. 2d 38, 40</a></span> (CA2 1970), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./401/977/">401 U. S. 977</a></span> (1971); <em>United States ex rel. Cabey </em>v. <em>Mazurkiewicz, </em><span class="citation" data-id="9456020"><a href="/opinion/292123/united-states-of-america-ex-rel-william-cabey-h-2519-v-joseph/#842" aria-description="Citation for case: United States of America Ex Rel. William Cabey H-2519 v....">431 F. 2d 839, 842-843</a></span> (CA3 1970); <em>United States </em>v. <em>Thompson, </em><span class="citation" data-id="288276"><a href="/opinion/288276/united-states-v-john-thompson/#375" aria-description="Citation for case: United States v. John Thompson">421 F. 2d 373, 375-376</a></span> (CA5), vacated on other grounds, <span class="citation" data-id="108212"><a href="/opinion/108212/thompson-v-united-states/" aria-description="Citation for case: Thompson v. United States">400 U. S. 17</a></span> (1970); <em>Gurleski </em>v. <em>United States, </em><span class="citation" data-id="9454142"><a href="/opinion/282906/michael-joseph-gurleski-and-dorothy-villafranca-v-united-states-of/#260" aria-description="Citation for case: Michael Joseph Gurleski and Dorothy Villafranca v. United...">405 F. 2d 253, 260-262</a></span> (CA5 1968), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./395/981/">395 U. S. 981</a></span> (1969); <em>Wright </em>v. <em>United States, </em><span class="citation" data-id="278916"><a href="/opinion/278916/lynn-edward-wright-v-united-states/#998" aria-description="Citation for case: Lynn Edward Wright v. United States">389 F. 2d 996, 998-999</a></span> (CA8 1968); <em>Roberts </em>v. <em>United States, </em><span class="citation" data-id="264623"><a href="/opinion/264623/raymond-ralph-roberts-v-united-states/#894" aria-description="Citation for case: Raymond Ralph Roberts v. United States">332 F. 2d 892, 894-898</a></span> (CA8 1964), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./380/980/">380 U. S. 980</a></span> (1965); <em>United States </em>v. <em>Wilson, </em><span class="citation" data-id="298539"><a href="/opinion/298539/united-states-v-raymond-craig-wilson-united-states-of-america-v-wilbert/#5" aria-description="Citation for case: United States v. Raymond Craig Wilson, United States of...">447 F. 2d 1, 5-6</a></span> (CA9 1971); <em>Nelson </em>v. <em>California, </em><span class="citation" data-id="268073"><a href="/opinion/268073/chester-nelson-v-people-of-the-state-of-california-robert-a-heinze/#77" aria-description="Citation for case: Chester Nelson v. People of the State of California,...">346 F. 2d 73, 77</a></span> (CA9), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./382/964/">382 U. S. 964</a></span> (1965); <em>Burge </em>v. <em>United States, </em><span class="citation" data-id="9450504"><a href="/opinion/267102/richard-w-burge-v-united-states/#413" aria-description="Citation for case: Richard W. Burge v. United States">342 F. 2d 408, 413</a></span> (CA9), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./382/829/">382 U. S. 829</a></span> (1965).</p>
</footnote>
<footnote label="6">
<p id="b238-8"><em> E. g., People </em>v. <em>Howard, </em><span class="citation" data-id="1377086"><a href="/opinion/1377086/people-v-howard/#651" aria-description="Citation for case: People v. Howard">166 Cal. App. 2d 638, 651</a></span>, <span class="citation" data-id="1377086"><a href="/opinion/1377086/people-v-howard/#114" aria-description="Citation for case: People v. Howard">334 P. 2d 105, 114</a></span> (1958); <em>People </em>v. <em>Gorg, </em><span class="citation" data-id="1359720"><a href="/opinion/1359720/people-v-gorg/#783" aria-description="Citation for case: People v. Gorg">45 Cal. 2d 776, 783</a></span>, <span class="citation" data-id="1359720"><a href="/opinion/1359720/people-v-gorg/#473" aria-description="Citation for case: People v. Gorg">291 P. 2d 469, 473</a></span> (1955); <em>People </em>v. <em>Haskell, </em><span class="citation" data-id="1976399"><a href="/opinion/1976399/the-people-v-haskell/#28" aria-description="Citation for case: The PEOPLE v. Haskell">41 Ill. 2d 25, 28-29</a></span>, <span class="citation" data-id="1976399"><a href="/opinion/1976399/the-people-v-haskell/#432" aria-description="Citation for case: The PEOPLE v. Haskell">241 N. E. 2d 430, 432</a></span> (1968); <em>People </em>v. <em>Walker, </em><span class="citation" data-id="2059444"><a href="/opinion/2059444/the-people-v-walker/#27" aria-description="Citation for case: The People v. Walker">34 Ill. 2d 23, 27-28</a></span>, <span class="citation" data-id="2059444"><a href="/opinion/2059444/the-people-v-walker/#555" aria-description="Citation for case: The People v. Walker">213 N. E. 2d 552, 555</a></span> (1966); <em>Commonwealth ex rel. Cabey </em>v. <em>Rundle, </em><span class="citation" data-id="6259595"><a href="/opinion/6389909/commonwealth-ex-rel-cabey-v-rundle/" aria-description="Citation for case: Commonwealth ex rel. Cabey v. Rundle">432 Pa. 466</a></span>, <span class="citation" data-id="6259595"><a href="/opinion/6389909/commonwealth-ex-rel-cabey-v-rundle/" aria-description="Citation for case: Commonwealth ex rel. Cabey v. Rundle">248 A. 2d 197</a></span> (1968); <em>State </em>v. <em>Cairo, </em>74 R. I. 377, 385-386, <span class="citation" data-id="3868069"><a href="/opinion/4108204/state-v-cairo/#845" aria-description="Citation for case: State v. Cairo">60 A. 2d 841, 845</a></span> (1948); <em>Burge </em>v. <em>State, </em><span class="citation" data-id="1656389"><a href="/opinion/1656389/burge-v-state/#722" aria-description="Citation for case: Burge v. State">443 S. W. 2d 720, 722-723</a></span> (Ct. Crim. App. Tex.), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./396/934/">396 U. S. 934</a></span> (1969).</p>
</footnote>
<footnote label="7">
<p id="b239-5"> Common authority is, of course, not to be implied from the mere property interest a third party has in the property. The authority which justifies the third-party consent does not rest upon the law of property, with its attendant historical and legal refinements, see <em>Chapman </em>v. <em>United States, </em><span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span> (1961) (landlord could not validly consent to the search of a house he had rented to another), <em>Stoner </em>v. <em>California, </em><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">376 U. S. 483</a></span> (1964) (night hotel clerk could not validly consent to search of customer’s room) but rests rather on mutual use of the property by persons generally having joint access or control for most purposes, so that it is reasonable to recognize that any of the co-inhabitants has the right to permit the inspection in his own right and that the others have assumed the risk that one of their number might permit the common area to be searched.</p>
</footnote>
<footnote label="8">
<p id="b240-8"> Rule 801 (d) (2) (A) of the proposed Federal Rules of Evidence, approved by the Court on November 20, 1972, and transmitted to Congress, expressly provides that a party’s own statements offered against him at trial are not hearsay.</p>
</footnote>
<footnote label="9">
<p id="b241-6"> <em>Bridges </em>v. <em>Wixon, </em>326 U, S. 135, 153-154 (1945), upon which respondent and the Court of Appeals relied, involved the use of hearsay as substantive evidence bearing on the question of Bridges' membership in the Communist Party, a charge upon which a deportation order had been based. In addition to the fact that the use of unsworn, unsigned statements violated the rules of the Board of Immigration Appeals, the evidence was admitted to prove charges which directly jeopardized “the liberty of an individual,” <em>id., </em>at 154, and not for the purpose of determining a preliminary question of admissibility, as in this case.</p>
</footnote>
<footnote label="10">
<p id="b242-6"> Rule 104 (a) provides:</p>
<p id="b242-7">“(a) Questions of admissibility generally. Preliminary questions concerning the qualification of a person to be a witness, the existence of a privilege, or the admissibility of evidence shall be determined by the judge, subject to the provisions of subdivision (b). In making his determination he is not bound by the rules of evidence except those with respect to privileges.”</p>
</footnote>
<footnote label="11">
<p id="b242-8"> Rule 1101 (d)(1) provides:</p>
<p id="b242-9">“Rules inapplicable. The rules (other than those with respect to privileges) do not apply in the following situations:</p>
<p id="b242-10">“(1) <em>Preliminary questions of fact. </em>The determination of questions of fact preliminary to admissibility of evidence when the issue is to be determined by the judge under Rule 104 (a).”</p>
</footnote>
<footnote label="12">
<p id="b243-7"> “Should the exclusionary law of evidence, 'the child of the jury system’ in Thayer’s phrase, be applied to this hearing before the judge? Sound sense backs the view that it should not, and that the judge should be empowered to hear any relevant evidence, such as affidavits or other reliable hearsay.” C. McCormick, Evidence §53, p. 122 n. 91 (2d ed. 1972).</p>
</footnote>
<footnote label="13">
<p id="b244-6"> <span class="citation no-link">Wis. Stat. § 944.20</span> (1971) provides:</p>
<p id="b244-7">'‘Whoever does any of the following may be fined not more than $500 or imprisoned not more than one year in county jail or both: ... (3) Openly cohabits and associates with a person he knows is not his spouse under circumstances that imply sexual intercourse.”</p>
</footnote>
<footnote label="14">
<p id="b245-8"> Accordingly, we do not reach another major contention of the United States in bringing this case here: that the Government in any event had only to satisfy the District Court that the searching officers reasonably believed that Mrs. Graff had sufficient authority over the premises to consent to the search.</p>
<p id="b245-9">The Government also contends that the Court of Appeals imposed an unduly strict standard of proof on the Government by ruling that its case must be proved “to a reasonable certainty, by the great weight of the credible evidence.” But the District Court required only that the proof be by the <em>greater </em>weight of the evidence and the <page-number citation-index="1" label="178">*178</page-number>Court of Appeals merely affirmed the District Court's judgment. There was an inadvertence in articulating the applicable burden of proof, but it seems to have been occasioned by a similar inadvertence by the Government in presenting its case. In any event, the controlling burden of proof at suppression hearings should impose no greater burden than proof by a preponderance of the evidence. See <em>Lego </em>v. <em>Twomey, </em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#488" aria-description="Citation for case: Lego v. Twomey">404 U. S. 477, 488-489</a></span> (1972). We do not understand the Government to contend that the standard employed by the District Court was in error, and we have no occasion to consider whether it was.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. May-Shaw.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. May-Shaw
type: case
citation: "955 F.3d 563 (2020)"
parallel_cite: ""
neutral_cite: ""
court: 6th Cir. 2020
court_level: coa
circuit: ca6
year: 2020
date_decided: 2020-04-08
docket: 18-1821
authority_weight: "Binding in-circuit — 6th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4743325/united-states-v-christopher-may-shaw/"
  cluster_id: 4743325
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. May-Shaw
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Curtilage]]"
    role: Key
related:
  - "[[Curtilage]]"
  - "[[United States v. Dunn]]"
  - "[[Florida v. Jardines]]"
  - "[[Collins v. Virginia]]"
tags:
  - case
  - fourth-amendment
  - curtilage
  - dunn-factors
  - dog-sniff
  - pole-camera
  - apartment
  - sixth-circuit
holding: "The Sixth Circuit affirmed, holding that a covered carport in a communal apartment parking lot — where May-Shaw regularly parked but had no right to exclude others, and which was easily viewable from a public street — was not within the curtilage of his apartment under the Dunn factors, so a drug-dog sniff of his car parked there was not a Fourth Amendment search; nor did the twenty-three-day pole-camera surveillance of the lot violate any reasonable expectation of privacy."
---

# United States v. May-Shaw

*955 F.3d 563 (6th Cir. 2020)* (No. 18-1821) · U.S. Court of Appeals for the Sixth Circuit · **Binding in-circuit — 6th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 4743325 → opinion 4523672 (955 F.3d 563, decided 2020-04-08, Bush, J.); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Grand Rapids police investigated Christopher May-Shaw for drug trafficking after anonymous tips and a check revealing prior felony convictions. With the complex owner's permission, they surveilled the exterior of his apartment building and the communal parking lot — first from cameras in a van moved around the lot, and from January 26, 2016, a camera affixed to a telephone pole on Norman Drive that recorded continuously for twenty-three days. May-Shaw parked his BMW under a covered carport in the communal lot, easily viewable from the public street. After watching suspected drug transactions, officers had a K-9 sniff the BMW parked under the carport; the dog alerted, and the officers obtained a warrant for the apartment and vehicles that turned up cash, wrappers, and cocaine. The district court denied suppression, and May-Shaw entered a conditional guilty plea to conspiracy to distribute cocaine (144 months), preserving the appeal.

## Issue
Whether the covered carport in the communal parking lot was within the [[Curtilage|curtilage]] of May-Shaw's apartment — so that the warrantless drug-dog sniff of his car parked there was an unconstitutional search under *[[Florida v. Jardines]]* — and whether the twenty-three-day pole-camera surveillance of the lot violated his [[Reasonable Expectation of Privacy|reasonable expectation of privacy]].

## Rule
A warrantless dog sniff of a home's [[Curtilage|curtilage]] is a search under *[[Florida v. Jardines|Jardines]]*, but whether ground is [[Curtilage|curtilage]] is resolved with reference to the four *[[United States v. Dunn|Dunn]]* factors — proximity to the home, enclosure, the nature of the area's use, and the steps taken to shield it from observation — with the burden on the defendant to show the area is intimately linked to the home. Applying those factors, the court held: "May-Shaw has failed to establish that the carport constituted the curtilage of his apartment; the drug dog sniff therefore did not constitute a search." — 955 F.3d 563, slip op. at 12. ^pin-op12

## Application
None of the *[[United States v. Dunn|Dunn]]* factors carried May-Shaw's burden. Proximity: the carport was closest to his apartment but not as close as structures previously found to be [[Curtilage|curtilage]], and proximity alone is not determinative. Enclosure: the carport had a roof and two side walls but sat in a communal lot, not within an enclosure around the residence. Use: regularly parking there arguably favored him, but he had no legal right to exclude others from the communal carport. Protection from observation: unlike the petitioner in *[[Collins v. Virginia|Collins]]* (who covered his vehicle), May-Shaw did little to protect the area from the view of passersby, and officers could see into the carport from a pole camera across the street. Because the carport was not [[Curtilage|curtilage]], the dog sniff was not a search — and the pole-camera surveillance captured only what was publicly visible, so it did not violate any [[Reasonable Expectation of Privacy|reasonable expectation of privacy]]. The court therefore did not reach the independent-source or good-faith questions.

## Conclusion
**Affirmed.** Judge Bush wrote for the panel (Merritt, Clay, and Bush, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *May-Shaw* is a useful *[[United States v. Dunn|Dunn]]*-factors application at the **[[Curtilage|curtilage]] / open-view boundary**: a partially enclosed but **communal** carport that the resident cannot exclude others from, and that is plainly visible from a public street, falls outside the [[Curtilage|curtilage]] — so a dog sniff there is not a search, and *[[Collins v. Virginia|Collins]]* (a walled-off driveway the owner shielded) does not compel the opposite result.

## Appears on
- [[Curtilage]] — *Key*

## Sources
- [*United States v. May-Shaw*, 955 F.3d 563 (6th Cir. 2020)](https://www.courtlistener.com/opinion/4743325/united-states-v-christopher-may-shaw/) — pinpoint: slip op. at 12 (carport-not-curtilage / dog-sniff-not-a-search holding; the CL opinion text carries the court's internal slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "df308f019703607e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. May-Shaw"}, "payload": {"all": [{"cite": "955 F.3d 563", "page": "563", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "955"}], "display": "955 F.3d 563", "official": {"cite": "955 F.3d 563", "page": "563", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "955"}, "official_selection_present": true, "record_id": "United States v. May-Shaw"}}
{"assertion_id": "8350ede997259178", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. May-Shaw"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. May-Shaw", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. May-Shaw

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. May-Shaw",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Christopher May-Shaw",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. May-Shaw",
    "court": "6th Cir. 2020",
    "court_id": "ca6",
    "court_level": "coa",
    "circuit": "ca6",
    "state": null,
    "date_decided": "2020-04-08",
    "year": 2020,
    "docket": "18-1821",
    "cluster_id": 4743325,
    "lead_opinion_id": 4523672,
    "sibling_ids": [],
    "absolute_url": "/opinion/4743325/united-states-v-christopher-may-shaw/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "955 F.3d 563",
      "volume": "955",
      "reporter": "F.3d",
      "page": "563",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "955 F.3d 563",
        "volume": "955",
        "reporter": "F.3d",
        "page": "563",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "955 F.3d 563",
    "official_selection": {
      "court_class": "state",
      "selected": "955 F.3d 563",
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
    "date_created": "2026-07-06T05:55:59Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:56:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:56:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:56:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:56:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-may-shaw--4743325",
      "to_record_id": "United States v. May-Shaw",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. May-Shaw

```
                                RECOMMENDED FOR PUBLICATION
                                Pursuant to Sixth Circuit I.O.P. 32.1(b)
                                       File Name: 20a0109p.06

                    UNITED STATES COURT OF APPEALS
                                   FOR THE SIXTH CIRCUIT



 UNITED STATES OF AMERICA,                                   ┐
                                    Plaintiff-Appellee,      │
                                                             │
                                                              >        No. 18-1821
        v.                                                   │
                                                             │
                                                             │
 CHRISTOPHER PAYTON MAY-SHAW,                                │
                           Defendant-Appellant.              │
                                                             ┘

                          Appeal from the United States District Court
                     for the Western District of Michigan at Grand Rapids.
                   No. 1:17-cr-00057-1—Paul Lewis Maloney, District Judge.

                                   Argued: January 28, 2020

                                Decided and Filed: April 8, 2020

                     Before: MERRITT, CLAY, and BUSH, Circuit Judges.

                                      _________________

                                            COUNSEL

ARGUED: Patrick J. Hanley, Covington, Kentucky, for Appellant. Tonya R. Long, UNITED
STATES ATTORNEY’S OFFICE, Grand Rapids, Michigan, for Appellee. ON BRIEF: Patrick
J. Hanley, Covington, Kentucky, for Appellant. Sally J. Berens, UNITED STATES
ATTORNEY’S OFFICE, Grand Rapids, Michigan, for Appellee.           Christopher Payton
May-Shaw, Sandstone, Minnesota, pro se.
                                      _________________

                                             OPINION
                                      _________________

       JOHN K. BUSH, Circuit Judge. Christopher May-Shaw was sentenced to 144 months in
prison after he entered a conditional guilty plea to a charge of conspiracy to distribute cocaine.
 No. 18-1821                       United States v. May-Shaw                              Page 2


The conviction arose from police surveillance of a parking lot near his apartment building and a
covered carport next to that building, where May-Shaw parked his BMW, one of his several
vehicles. The surveillance lasted for twenty-three days and used a camera affixed to a telephone
pole on a public street and cameras in a surveillance van parked in the parking lot. After
witnessing May-Shaw engage in several suspected drug deals, the police used a drug-detecting
dog to sniff the BMW. The dog indicated the presence of narcotics in the vehicle. Based on the
dog sniff and the surveillance, the officers obtained a search warrant for May-Shaw’s apartment
and all of his vehicles. The search found evidence of drug distribution, including cash, wrappers,
and cocaine. The district court denied his motion under the Fourth Amendment to suppress the
evidence from his apartment and vehicles. May-Shaw then entered a conditional guilty plea for
conspiracy to distribute cocaine, but he preserved the right to appeal the denial of his motion to
suppress.

       As explained below, May-Shaw did not have a reasonable expectation of privacy in the
carport such that police surveillance constituted a search in violation of the Fourth Amendment.
Nor was the carport within the curtilage of his apartment such that the dog sniff was
unconstitutional. Therefore, we AFFIRM the district court’s denial of May-Shaw’s motion to
suppress.

                                                I.

       In December 2015, the City of Grand Rapids Police Department began investigating
May-Shaw for suspected involvement in drug trafficking. The Department had received tips
from Silent Observer—an organization that receives anonymous information from the public—
describing vehicles May-Shaw was using to transport drugs and a specific bag where he kept
drugs, money, and a gun. A criminal history check on May-Shaw revealed that he had one
felony firearm conviction and two felony drug convictions. Based on all of this information, the
Grand Rapids police decided to conduct surveillance of the exterior of May-Shaw’s apartment
building and the parking lot of the apartment complex.

       The apartment where May-Shaw lived is one of several units in the complex, which itself
abuts a communal parking lot. In the parking lot are covered carports, the interiors of which are
 No. 18-1821                        United States v. May-Shaw                             Page 3


easily viewable from a public vantage point on Norman Drive, a road outside of the parking lot.
May-Shaw often parked his vehicles under a covered carport close to the entrance to his
apartment building.    Nothing in the record indicates whether the carport was specifically
assigned to him, or if he had just consistently parked there.

       The carport is next to a parking lot that is accessible only from Norman Drive, and that
entrance affords almost complete visibility of the lot and adjacent apartment complex. The
owner of the complex gave police permission to conduct physical and video surveillance of the
lot. They had a good view, for only a line of trees obstructs the parking lot from public view on
the road, and there was no foliage obstructing the view in February 2016, when the surveillance
occurred.

       Most of the stakeout, lasting several weeks, was done from a van using remotely operated
cameras. Officers would park the van in the lot, moving its location every day or two. Through
this method, police observed May-Shaw loading and unloading drugs and cash from his BMW
and engaging in what officers believed to be drug deals in the parking lot.

       In addition to their surveillance from the van, on January 26, 2016, police installed a
camera on a telephone pole on Norman Drive. Officer Mesman, the principal investigator in
May-Shaw’s case, testified as to the specifics of the pole camera. According to Mesman, the
camera was affixed to the pole approximately twenty feet from the ground, and could pan from
side to side and up and down. The camera, which recorded continuously for twenty-three days,
could produce video as well as still shots. Though officers did not monitor the footage
continuously in real time, they reviewed the footage they missed by watching the recorded video.

       The pole-camera and van-camera footage captured May-Shaw engaging in what the
officers suspected were drug transactions in the parking lot. They based this conclusion on
observations of May-Shaw making brief contact with people inside their vehicles, during which
time he and the person in the car exchanged something. Also, on several occasions May-Shaw
retrieved what appeared to be evidence of drug distribution from his vehicles. For example, on
February 17, 2016, officers observed him lean into the front passenger side of one of his vehicles
and remove cash and a bag of suspected drugs, hide the items under his jacket, and carry them
 No. 18-1821                         United States v. May-Shaw                            Page 4


inside the apartment. The next day, officers watched May-Shaw reach into the back of his car
and remove a large stack of cash, which he also took inside the apartment. Soon thereafter, the
officers saw him put another two bags, which they also suspected contained drugs and cash, in
the trunk of his BMW.

       After witnessing such suspected drug transactions, the officers called in a K-9 unit for a
drug-detecting dog sniff of the BMW, where the officers had just seen May-Shaw stash the bags.
When the dog circled the BMW, which was parked directly under the carport, it alerted the
officers to the odor of narcotics.

       Based on the surveillance and dog sniff, the officers sought a search warrant. The police
relied primarily on the footage from the pole camera and the surveillance van, which showed
different angles of the same conduct described earlier. A state magistrate judge authorized a
search warrant for the apartment and three vehicles connected to May-Shaw. The apartment
search resulted in seizure of almost $2,000 in cash, a gun, drug paraphernalia and packaging
material, and nearly a pound of marijuana. In their search of the BMW, police found a kilogram
of cocaine, some fentanyl, and over $200,000 in cash. The search of one of May-Shaw’s other
vehicles, a Chevrolet Tahoe, turned up another $486 in cash. Neither May-Shaw nor his third
car was present when the police conducted the search. May-Shaw was arrested some months
later in Brooklyn, New York.

       A federal grand jury in the U.S. District Court for the Western District of Michigan
returned a superseding indictment charging May-Shaw with conspiracy to distribute and possess
with intent to distribute cocaine, possession with intent to distribute cocaine, and maintaining
drug-involved premises, in violation of 21 U.S.C. §§ 846, 841(b)(1)(A) and 856.

       May-Shaw moved the district court to suppress the evidence seized pursuant to the search
warrant, arguing that the warrantless surveillance through the pole camera and the warrantless
sniff by the drug-detecting dog of the BMW constituted unconstitutional warrantless searches.
The district court denied the motion, holding that (1) May-Shaw had no reasonable expectation
of privacy in the parking lot; (2) the area surveilled by the pole camera was not constitutionally
protected curtilage of the apartment; (3) the dog sniff was permitted under the Fourth
 No. 18-1821                         United States v. May-Shaw                              Page 5


Amendment; and (4) even if the dog sniff was unconstitutional, the remainder of the information
in the warrant affidavit was sufficient to support probable cause for the search warrant.

       May-Shaw entered a conditional guilty plea to the conspiracy count, preserving the right
to appeal the denial of the motion to suppress. He was sentenced to 144 months in prison. He
filed this timely appeal.

                                                II.

       When reviewing a district court’s decision on a motion to suppress, we use a mixed
standard of review, reviewing findings of fact for clear error and conclusions of law de novo.
United States v. Hines, 885 F.3d 919, 924 (6th Cir. 2018). Evidence should be viewed in the
light most favorable to the district court’s conclusions. United States v. McCraney, 674 F.3d
614, 616–17 (6th Cir. 2012). “[A] denial of a motion to suppress will be affirmed on appeal if
the district court’s conclusion can be justified for any reason.” United States v. Moorehead,
912 F.3d 963, 966 (6th Cir. 2019) (alteration in original) (quoting United States v. Pasquarille,
20 F.3d 682, 685 (6th Cir. 1994)).

       May-Shaw’s motion to suppress invokes the Fourth Amendment, which protects “[t]he
right of the people to be secure in their persons, houses, papers, and effects, against unreasonable
searches and seizures.”     U.S. Const. amend. IV.        May-Shaw maintains that his Fourth
Amendment rights were violated when the police conducted warrantless surveillance of the
carport outside of his apartment, and when they used a drug-detecting dog to sniff his car that
was parked in that carport. We address each argument in turn.

                                                A.

       May-Shaw argues that the district court erred in finding that the long-term surveillance of
the carport did not constitute a search. Under Fourth Amendment jurisprudence, there are two
ways in which government action may constitute a search. First, when the government gains
information by physically intruding into a constitutionally protected area—namely, “persons,
houses, papers, and effects,” U.S. Const. amend. IV—“‘a search within the original meaning of
the Fourth Amendment’ has ‘undoubtedly occurred.’” Morgan v. Fairfield Cty., 903 F.3d 553,
 No. 18-1821                       United States v. May-Shaw                               Page 6


561 (6th Cir. 2018) (quoting Florida v. Jardines, 569 U.S. 1, 5 (2013)). Second, as articulated
by the Supreme Court, a search occurs when “a government official invades an area in which ‘a
person has a constitutionally protected reasonable expectation of privacy.’” Taylor v. City of
Saginaw, 922 F.3d 328, 332 (6th Cir. 2019) (quoting Katz v. United States, 389 U.S. 347, 360
(1967) (Harlan, J., concurring)). Under the latter framework, there are two requirements for a
government intrusion to constitute a Fourth Amendment search: first, a person must exhibit “an
actual (subjective) expectation of privacy” in the place or thing searched; second, the expectation
is one “that society is prepared to recognize as ‘reasonable.’” Katz, 389 U.S. at 361.

       Because the officers’ use of the pole camera did not involve any sort of physical intrusion
into a constitutionally protected area, May-Shaw must show that he had a reasonable expectation
of privacy in the carport. Cobbling together dicta from several Fourth Amendment cases, he
argues that, although police may permissibly observe the curtilage of a home for a short period
of time, for example with an aerial flyover, see California v. Ciraolo, 476 U.S. 207, 213 (1986),
long-term video surveillance of a home’s curtilage is problematic under the Fourth Amendment,
see United States v. Anderson-Bagshaw, 509 F. App’x 396, 405 (6th Cir. 2012). There is at least
some support for that proposition, as this court and five Justices of the Supreme Court have
noted concerns about the problems with long-term warrantless surveillance. See id.; see also
United States v. Jones, 565 U.S. 400, 415, 429–30 (2012) (Sotomayor, J., concurring and Alito,
J., concurring).

       Although this argument may be compelling in theory, as applied here, it is foreclosed by
this circuit’s case law, which has consistently held that this type of warrantless surveillance does
not violate the Fourth Amendment. For example, in United States v. Houston, we held that
affixing a video camera to the top of a utility pole to record the defendant’s front porch over a
ten-week period did not violate the defendant’s Fourth Amendment rights because “agents only
observed what [the defendant] made public to any person traveling on the roads” surrounding his
home. 813 F.3d 282, 288 (6th Cir. 2016). We rejected the defendant’s claim that the length of
the period of monitoring made the surveillance constitutionally unreasonable, reasoning that it is
the possibility—not the practicability—that the police could have themselves sat atop the utility
pole and observed the same view for every waking moment of a ten-week period that is critical.
 No. 18-1821                             United States v. May-Shaw                                        Page 7


Id. at 289–90. That reasoning was applied in United States v. Powell, in which we held that the
warrantless surveillance of three buildings through the installation of video cameras on three
public utility poles, for periods of up to 90 days each, did not violate the defendants’ Fourth
Amendment rights. 847 F.3d 760, 773 (6th Cir. 2017). And, even assuming that May-Shaw is
correct that the carport constitutes the curtilage of his apartment—an argument that we find
unpersuasive, for reasons discussed below—that is of no consequence to the constitutional
analysis of the video surveillance. We held in Houston that warrantless video surveillance of the
defendant’s front porch, which is unquestionably within the curtilage of his home, did not violate
his reasonable expectation of privacy because the camera “captured only views that were plainly
visible to any member of the public who drove down the roads bordering” his home. Houston,
813 F.3d at 288.

        May-Shaw contends that the pole camera did not provide the same vantage point that was
readily accessible from the street.1 The district court, however, held that the area surveilled by
the pole camera was readily accessible from a public vantage point. This is a factual finding that
is reviewed for clear error. Officer Mesman testified that the vantage point from the pole camera
was the same as the vantage point from the street, and nothing in the record contradicts that
assertion. Therefore, the district court’s factual finding that the pole camera recorded the same
view enjoyed by an individual standing on Norman Avenue was not clearly erroneous.

        Furthermore, the surveillance footage and photos here did not “generate[] a precise,
comprehensive record of [May-Shaw’s] public movements that reflects a wealth of detail about
[his] familial, political, professional, religious, and sexual associations,” Jones, 565 U.S. at 415


        1The     parties dispute which camera or cameras recorded the illicit activity. May-Shaw claims that the
footage was captured by the pole camera, whereas the government maintains that the incriminating footage came
from the cameras in the van. Though the officers did not keep a log of which images came from each camera, a
comparison of two sets of photos available at R. 60-2, PageID 236–37 clearly indicates that the close-up images
showing May-Shaw engaged in suspected drug transactions did not come from the more remote camera affixed to
the telephone pole. May-Shaw does not point to anything other than the lack of a log to suggest that the images did
not come from the surveillance van cameras. Appellant Br. at 13. If the images were in fact recorded from the
surveillance van rather than from the pole camera, then this is a simple case of police surveillance from a publicly
accessible area, in which the police had permission to conduct the surveillance. This does not raise the same Fourth
Amendment concerns. See United States v. Gooch, 499 F.3d 596, 602–03 (6th Cir. 2007) (noting that an individual
does not have a reasonable expectation of privacy in an openly accessible parking lot, and so police surveillance in
that lot did not constitute a search).
 No. 18-1821                       United States v. May-Shaw                              Page 8


(Sotomayor, J., concurring), which could raise significant Fourth Amendment concerns. Rather,
the footage and photos only revealed what May-Shaw did in a public space—the parking lot.
They captured images of May-Shaw moving things from his car to his apartment. The video
showed when he arrived and left the apartment. In other words, the cameras observed only what
“was possible for any member of the public to have observed . . . during the surveillance period.”
Houston, 813 F.3d at 290.

       May-Shaw has not demonstrated that when the government surveilled the carport for
twenty-three days, it violated his reasonable expectation of privacy and thus conducted an
unconstitutional search. We find no error in the district court’s judgment that the pole-camera
surveillance did not violate May-Shaw’s Fourth Amendment rights.

                                               B.

       May-Shaw also argues that the district court should have granted his motion to suppress
because the use of the drug-detecting dog to sniff his BMW while it was parked in the carport
constituted an unlawful search under the Fourth Amendment. This argument hinges on one
issue: whether the carport where the vehicle was parked constitutes the curtilage of the
apartment.

       As relevant here, the Fourth Amendment protects the people from “unreasonable
searches” of “their . . . houses.” And, as a general rule, the curtilage of a home is protected by
the Fourth Amendment. See United States v. Dunn, 480 U.S. 294, 300 (1987); see also Jardines,
569 U.S. at 6 (noting that the area “immediately surrounding and associated with the home” is
“part of the home itself for Fourth Amendment purposes” (quoting Oliver v. United States, 466
U.S. 170, 180 (1984))). That rule is well-rooted in history. “At the founding, curtilage was
considered part of the ‘hous[e]’ itself.” Collins v. Virginia, 138 S. Ct. 1663, 1676 (2018)
(Thomas, J., concurring) (alteration in original) (quoting 4 W. Blackstone, Commentaries on the
Laws of England 225 (1769) (“[T]he capital house protects and privileges all its branches and
appurtenants, if within the curtilage.”)). “The protection afforded the curtilage is essentially a
protection of families and personal privacy in an area intimately linked to the home, both
 No. 18-1821                       United States v. May-Shaw                               Page 9


physically and psychologically, where privacy expectations are most heightened.” Id. at 1670
(majority opinion) (quoting Ciraolo, 476 U.S. at 212–213).

       Although it is well-settled that the warrantless search of a home’s curtilage with a drug-
sniffing dog violates the Fourth Amendment, Jardines, 569 U.S. at 11–12, what constitutes
curtilage for purposes of the Fourth Amendment generally, and in the present case in particular,
are harder questions. If the carport was within the curtilage of May-Shaw’s apartment, then the
dog sniff constituted an unconstitutional warrantless search under Jardines, but if the carport was
not within the curtilage, then the sniff was not a search, and therefore was not constitutionally
problematic. See United States v. Perez, 440 F.3d 363, 375 (6th Cir. 2006) (holding that using a
drug-sniffing dog on a car parked in a hotel parking lot, which was not stopped, detained, or
moved, did not constitute a search).

       Courts have identified four factors as guideposts to determining whether an area falls
within a home’s curtilage: (1) the proximity of the area to the home, (2) whether the area is
within an enclosure around the home, (3) how that area is used, and (4) what the owner has done
to protect the area from observation from passersby. Morgan, 903 F.3d at 561 (citing Dunn, 480
U.S. at 301). These factors are not to be applied mechanically; rather, they are “useful analytical
tools only to the degree that, in any given case, they bear upon the centrally relevant
consideration—whether the area in question is so intimately tied to the home itself that it should
be placed under the home’s ‘umbrella’ of Fourth Amendment protection.” Dunn, 480 U.S. at
301. In the application of the factors, the onus is on May-Shaw: he “bears the burden of
establishing that the challenged search violated his Fourth Amendment rights.” United States v.
Coleman, 923 F.3d 450, 455 (6th Cir. 2019) (quoting United States v. Witherspoon, 467 F.
App’x 486, 490 (6th Cir. 2012)).

       The Supreme Court recently held that an enclosed driveway abutting a house constituted
the curtilage of the home. Collins, 138 S. Ct. at 1670–71. In Collins, police searched a
motorcycle that was covered by a tarp and was parked in a section of a driveway that was
partitioned off by two brick walls and a wall of the house itself. Id. at 1670. “A visitor
endeavoring to reach the front door of the house would have to walk partway up the driveway,
but would turn off before entering the enclosure and instead proceed up a set of steps leading to
 No. 18-1821                          United States v. May-Shaw                           Page 10


the front porch.” Id. at 1671. The Court held that the driveway enclosure “constitute[d] ‘an area
adjacent to the home and “to which the activity of home life extends,”’ and so is properly
considered curtilage.” Id. (quoting Jardines, 569 U.S. at 7).

       May-Shaw argues that Collins is dispositive here, and that because the carport was
partially enclosed, it constitutes the curtilage of the apartment. But Collins does not mandate
that result. At least three cases in this circuit cut against May-Shaw’s position.

       First, there is Coleman, mentioned above. There, we found that the defendant’s car was
not within the curtilage of his condo when it was parked in his condominium complex’s
driveway, reasoning in part that the driveway was communal and other condo residents
frequently walked past cars parked in front of the condo units. 923 F.3d at 456–57; see also
United States v. Jones, 893 F.3d 66, 72 (2d Cir. 2018) (“[Collins] has no effect on [the
defendant’s] appeal, which fails because the driveway in which [the defendant’s] vehicle was
parked was the shared driveway of tenants in two multi-family buildings and was not within the
curtilage of [his] private home.”).

       In addition, two Sixth Circuit cases decided prior to Collins—United States v. Galaviz,
645 F.3d 347 (6th Cir. 2011), and United States v. Estes, 343 F. App’x 97 (6th Cir. 2009)—are
instructive. Those cases involved unenclosed driveways that were adjacent to a home, and
abutted a sidewalk or alley, with no steps taken by the resident to obstruct the view of passersby.
Galaviz, 645 F.3d at 356; Estes, 343 F. App’x at 101. In both cases, we held that officers did not
intrude upon the curtilage by entering the driveway. In Galaviz we found that although the
driveway was adjacent to the house, it was not enclosed by any barrier, and the portion where
cars were parked was directly adjacent to a public sidewalk. Galaviz, 645 F.3d at 356. And in
Estes, the driveway was not curtilage because it was not enclosed, the defendant had not taken
any steps to protect it from observation by passersby, and it was used as a point of entry to the
defendant’s residence. Estes, 343 F. App’x at 101.

       May-Shaw directs the court’s attention to several cases—one from the Sixth Circuit, and
three from district courts within our circuit—in an attempt to establish a broad rule that a carport
is always within the curtilage of a home. See Appellant Br. at 26. But each of the cases he cites
 No. 18-1821                       United States v. May-Shaw                              Page 11


is factually distinct. As the first case he cites for that proposition states, “[e]very curtilage
determination is distinctive and stands or falls on its own unique set of facts.” Daughenbaugh v.
City of Tiffin, 150 F.3d 594, 598 (6th Cir. 1998) (alteration in original) (quoting United States v.
Reilly, 76 F.3d 1271, 1276 (2d Cir. 1996))).

       In Daughenbaugh, as May-Shaw notes, our court held that a detached garage was within
the curtilage of a home. Id. at 601. But there, the garage was “within natural boundaries
demarcated by the river and the heavy tree coverage . . . [and] the backyard and garage [were]
not readily visible from the street.” Id. at 599. We considered these natural boundaries to be
compelling evidence that the garage was within the curtilage of the home. Id. Furthermore, the
garage was set far back from the road, and a large tree prevented neighbors, those parked in the
driveway, and those on the street from viewing the interior of the garage. Id. at 600. Important
to the court’s calculus was that the “contents [of the garage] were only visible after a person
entered the backyard and approached the garage.” Id.

       Here, although the carport where May-Shaw parked his vehicles was the closest in
proximity to his apartment, it was not as close to the residence as other structures found to be
curtilage have been. But in any event, that factor is not determinative “without reference to the
additional Dunn factors.” Daughenbaugh, 150 F.3d at 599. In Collins, Coleman, Galaviz, and
Estes, the areas at issue were all driveways that, unlike the carport here, directly abutted homes
or condominiums. And even in those cases where the driveway was connected to the home, the
courts each held that the driveway was not curtilage.

       The second factor—whether the area is an enclosure around the home—also cuts against
May-Shaw. Here, although the area was enclosed, at least to the extent that the carport had a
roof and two side walls, it was not in an enclosure around the residence as was the walled-off
driveway in Collins, nor was it enclosed within natural boundaries of the property like the
detached garage in Daughenbaugh.

       The third factor, which relates to May-Shaw’s use of the carport, arguably weighs in his
favor because, by regularly parking his car in the carport, he contends it was sufficiently
“associated with the activities and privacies of domestic life” to ostensibly support a finding that
 No. 18-1821                        United States v. May-Shaw                              Page 12


it was within the curtilage of his apartment. Dunn, 480 U.S. at 303. However, there is no
evidence that May-Shaw had any legal right to exclude others from the carport.

       Furthermore, May-Shaw did little to protect the area from the view of passersby, and so
the fourth factor weighs against him. With respect to this last consideration, May-Shaw’s case
falls somewhere in between Collins and Coleman. Like the driveway in Collins, the carport here
was partially enclosed, which cuts at least somewhat in his favor. But, like in Coleman, May-
Shaw took no additional steps to protect the area from passersby. He did not, as did the
petitioner in Collins, cover his vehicle to shield it from view from his neighbors. See 138 S. Ct.
at 1668. And because officers could see into the carport from a camera affixed to a utility pole
across a street, it is apparent that May-Shaw did not take significant steps to protect the area from
observation.

       The burden is on May-Shaw to establish that the carport is “intimately linked to the
home, both physically and psychologically, where privacy expectations are most heightened.”
Collins, 138 S. Ct. at 1670 (quoting Ciraolo, 476 U.S. at 212–13). He has not done so. May-
Shaw has failed to establish that the carport constituted the curtilage of his apartment; the drug
dog sniff therefore did not constitute a search. See Perez, 440 F.3d at 375. Because we hold that
neither the pole-camera surveillance nor the dog sniff constituted a search, we need not decide
whether the evidence would have been admissible under the independent-source doctrine or the
good-faith exception.

                                                III.

       May-Shaw has not shown that (1) police surveillance from the pole camera violated his
reasonable expectation of privacy; or (2) the dog sniff constituted an unconstitutional search.
Therefore, we AFFIRM the district court’s denial of his motion to suppress.

```

---
