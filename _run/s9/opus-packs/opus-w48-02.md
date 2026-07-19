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

## GROUP: content/cases/Northrup v. City of Toledo Police Dept.md  (`case`, 5 assertions)

### content_page

```
---
title: Northrup v. City of Toledo Police Dept
type: case
citation: "785 F.3d 1128 (2015)"
parallel_cite: 2015 FED App. 0092P
neutral_cite: "2015 U.S. App. LEXIS 7868; 2015 WL 2217061"
court: "U.S. Court of Appeals, 6th Cir."
court_level: coa
circuit: ca6
year: 2015
date_decided: ""
docket: No. 14-4050
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
  opinion_url: "https://www.courtlistener.com/opinion/2800431/shawn-northrup-v-city-of-toledo-police-dept/"
  cluster_id: 2800431
  opinion_id: null
  identity_checked: true
lake:
  record_id: Northrup v. City of Toledo Police Dept
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: Illustrates a circuit split
related:
  - "[[Terry Stops and Reasonable Suspicion]]"
  - "[[Terry v. Ohio]]"
tags:
  - case
  - fourth-amendment
  - terry-stop
  - reasonable-suspicion
  - open-carry
  - qualified-immunity
  - sixth-circuit
  - circuit-split
holding: "Where state law permits the open carry of firearms, the mere fact that a person is openly and lawfully carrying a holstered handgun — reported by a 911 caller — does not, without more, give an officer reasonable suspicion of criminality or dangerousness to justify stopping, disarming, and detaining him; doing so violates clearly established Fourth Amendment law."
aliases:
  - Northrup v. City of Toledo Police Dept.
  - Northrup v. City of Toledo Police Department
  - "Northrup v. City of Toledo (6th Cir. 2015)"
---

# Northrup v. City of Toledo Police Dept

*785 F.3d 1128 (2015)* (No. 14-4050) · U.S. Court of Appeals for the Sixth Circuit · **Binding in-circuit — 6th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 2800431 → opinion 2800431 (Sutton, J., for the panel; 785 F.3d 1128, decided May 13, 2015). frontier-split row (role: illustrates a circuit split) — in-circuit rule, persuasive elsewhere; split framing named in Treatment (LINT-21 binding-language: binding only in the 6th Cir.). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*1133`, between `*1132` and `*1134`). S9 promotes. -->

## Background
Shawn Northrup was walking his dog in his Ohio neighborhood with a handgun holstered at his side — conduct Ohio's open-carry law permits. A passing motorcyclist objected and called 911 to report a man carrying a handgun in the open. Officer David Bright responded, stopped Northrup, took his gun, handcuffed him, held him in a patrol car for about half an hour, and cited him for failure to disclose personal information. Northrup sued the officers and the City under § 1983. The district court denied the officers [[Qualified Immunity|qualified immunity]] on the Fourth Amendment claim, and they took an interlocutory appeal.

## Issue
Whether openly carrying a firearm where state law permits it — reported by a 911 caller — gives an officer reasonable suspicion to stop, disarm, and detain the carrier.

## Rule
Because Ohio law permitted Northrup to carry openly, the panel held that his doing so supplied no basis to seize him: "And it has long been clearly established that an officer needs evidence of criminality or dangerousness before he may detain and disarm a law-abiding citizen." — 785 F.3d at 1133. ^pin-1133

## Application
Ohio permits open carry, and does not even require gun owners to carry or produce a license; Northrup was doing exactly what the law allowed, and the officer — unlike the dispatcher or the complaining motorcyclist — is charged with knowing the open-carry statute. A 911 report describing a man openly carrying a handgun therefore reported lawful conduct and did not create reasonable suspicion of a crime, and the officer knew nothing of the earlier verbal dispute. Lacking any reason to suspect criminality or dangerousness, Officer Bright violated clearly established Fourth Amendment law by stopping, disarming, and detaining Northrup — so [[Qualified Immunity|qualified immunity]] was unavailable.

## Conclusion
The denial of [[Qualified Immunity|qualified immunity]] was **affirmed**. Sutton, J., wrote for the panel.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. This is a **circuit-split** entry and must be taught as such. *Northrup* — with the Fourth Circuit's *[[United States v. Black]]* — holds that the lawful open (or otherwise legal) carry of a firearm, standing alone, does not create reasonable suspicion for a *[[Terry v. Ohio|Terry]]* stop. That rule is **binding only in the Sixth Circuit** and persuasive elsewhere; other courts have found reasonable suspicion where firearm possession is combined with additional suspicious circumstances or a specific report of *unlawful* carrying, and the courts are not uniform on how much a bare gun report contributes to reasonable suspicion. Teach *Northrup* as the in-circuit rule that illustrates the split, not a settled national standard.

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Illustrates a circuit split*

## Sources
- [*Northrup v. City of Toledo Police Dept.*, 785 F.3d 1128 (6th Cir. 2015)](https://www.courtlistener.com/opinion/2800431/northrup-v-city-of-toledo-police-dept/) — pinpoint: 1133 (Sutton, J., for the panel; the CL opinion text carries the reporter star `*1133`, with the quoted sentence falling between `*1132` and `*1134`). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e239b170b8f36bb8", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "785 F.3d 1128 (2015)", "court": "U.S. Court of Appeals, 6th Cir.", "neutral_cite": "2015 U.S. App. LEXIS 7868; 2015 WL 2217061", "official_citation_present": true, "parallel_cite": "2015 FED App. 0092P", "title": "Northrup v. City of Toledo Police Dept", "year": "2015"}}
{"assertion_id": "5fde9fc989ade267", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Where state law permits the open carry of firearms, the mere fact that a person is openly and lawfully carrying a holstered handgun — reported by a 911 caller — does not, without more, give an officer reasonable suspicion of criminality or dangerousness to justify stopping, disarming, and detaining him; doing so violates clearly established Fourth Amendment law.", "title": "Northrup v. City of Toledo Police Dept"}}
{"assertion_id": "a4c235a84fe6b0de", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Illustrates a circuit split", "title": "Northrup v. City of Toledo Police Dept"}}
{"assertion_id": "1a1e616d2790ca12", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Northrup v. City of Toledo Police Dept", "varies_by_point": "false"}}
{"assertion_id": "35b754ebda9ad93d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 6th Cir.", "title": "Northrup v. City of Toledo Police Dept"}}
```

### lake record — Northrup v. City of Toledo Police Dept

```json
{
  "schema_version": "s2.v1",
  "record_id": "Northrup v. City of Toledo Police Dept",
  "status": "under_review",
  "identity": {
    "case_name": "Shawn Northrup v. City of Toledo Police Dep't",
    "case_name_short": "",
    "case_name_full": "Shawn NORTHRUP, Plaintiff-Appellee, v. CITY OF TOLEDO POLICE DEPARTMENT; David R. Bright; Daniel Ray, Defendants-Appellants",
    "input_case_name": "Northrup v. City of Toledo Police Dept",
    "court": "U.S. Court of Appeals, 6th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca6",
    "state": null,
    "date_decided": null,
    "year": 2015,
    "docket": "No. 14-4050",
    "cluster_id": 2800431,
    "lead_opinion_id": 2800431,
    "sibling_ids": [],
    "absolute_url": "/opinion/2800431/shawn-northrup-v-city-of-toledo-police-dept/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "785 F.3d 1128",
      "volume": "785",
      "reporter": "F.3d",
      "page": "1128",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "2015 FED App. 0092P",
        "volume": "2015",
        "reporter": "FED App.",
        "page": "0092P",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2015 U.S. App. LEXIS 7868",
        "volume": "2015",
        "reporter": "U.S. App. LEXIS",
        "page": "7868",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 WL 2217061",
        "volume": "2015",
        "reporter": "WL",
        "page": "2217061",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "785 F.3d 1128",
        "volume": "785",
        "reporter": "F.3d",
        "page": "1128",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 FED App. 0092P",
        "volume": "2015",
        "reporter": "FED App.",
        "page": "0092P",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 U.S. App. LEXIS 7868",
        "volume": "2015",
        "reporter": "U.S. App. LEXIS",
        "page": "7868",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 WL 2217061",
        "volume": "2015",
        "reporter": "WL",
        "page": "2217061",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "785 F.3d 1128",
    "official_selection": {
      "court_class": "coa",
      "selected": "785 F.3d 1128",
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
    "date_created": "2026-07-06T13:13:08Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:13:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:13:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:13:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:13:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "northrup-v-city-of-toledo-police-dept--2800431",
      "to_record_id": "Northrup v. City of Toledo Police Dept",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Northrup v. City of Toledo Police Dept

```
                            RECOMMENDED FOR FULL-TEXT PUBLICATION
                                Pursuant to Sixth Circuit I.O.P. 32.1(b)
                                       File Name: 15a0092p.06

                      UNITED STATES COURT OF APPEALS
                                    FOR THE SIXTH CIRCUIT
                                      _________________


 SHAWN NORTHRUP,                                          ┐
                                    Plaintiff-Appellee,   │
                                                          │
                                                          │       No. 14-4050
          v.                                              │
                                                           >
                                                          │
 CITY OF TOLEDO POLICE DEPARTMENT; DAVID R.               │
 BRIGHT; DANIEL RAY,                                      │
                        Defendants-Appellants.            │
                                                          ┘
                            Appeal from the United States District Court
                             for the Northern District of Ohio at Toledo.
                     No. 3:12-cv-01544—Jeffrey James Helmick, District Judge.
                                 Decided and Filed: May 13, 2015

                     Before: GILMAN, ROGERS, and SUTTON, Circuit Judges.

                                       _________________

                                           COUNSEL

ON BRIEF: John T. Madigan, CITY OF TOLEDO DEPARTMENT OF LAW, Toledo, Ohio,
for Appellants. Daniel T. Ellis, LYDY & MOAN, LTD., Sylvania, Ohio, for Appellee.

                                       _________________

                                            OPINION
                                      _________________

       SUTTON, Circuit Judge. On a midsummer evening, Shawn and Denise Northrup went
for a neighborhood walk with their daughter, grandson, and dog. Apparently in a happy-go-
lucky mood, Shawn wore a t-shirt reading, “This Is The Shirt I Wear When I Don’t Care.” R. 28
at 7–8.        Shawn carried a cell phone, which he holstered on his hip—next to a black
semiautomatic handgun.




                                                 1
No. 14-4050             Northrup v. City of Toledo Police Dep’t, et al.                   Page 2

       A passing motorcyclist stopped to complain about Shawn’s visible firearm. The stranger,
Alan Rose, yelled, “[Y]ou can’t walk around with a gun like that!” But “[O]pen carry is legal in
Ohio!” Denise responded.       Id. at 28.   As the Northrups walked away, Denise and Rose
exchanged increasingly unprintable words until he was out of view (and earshot).

       Rose called 911, reporting that “a guy walking down the street” with his dog was
“carrying a gun out in the open.” R. 39 at 22–23. When asked what type of gun the guy was
carrying, Rose replied, “A handgun, and he’s telling me it’s legal to carry out in the open.” Id. at
23. That’s right, the dispatcher responded, it’s legal “[i]f you have a CCW”—a concealed-carry
weapon permit. “I’ll get a crew out though.” Id. The legality of Northrup’s behavior threw
Rose for a loop, prompting him to add: “I’m not going to call a crew out if it’s legal to carry a
gun out in the open.” Id.

       Despite Rose’s change of heart, the dispatcher sent an officer to the scene anyway. “I’m
not an officer,” she worried. Id. She dispatched Officer David Bright with the message that
someone was “walking his dog on Rochelle [Road] carrying a handgun out in the open.” R. 26
at 35, 115. Ten minutes later, Bright spotted the Northrups, their dog, and the “gun on [Shawn’s]
hip.” Id. at 36. He got out of his vehicle, said “excuse me, sir,” and asked Shawn to hand the
dog’s leash to his wife, which Shawn did. Id. at 37.

       At that point, according to Officer Bright, Shawn pulled out his cell phone, then “moved
his hands back toward his weapon”—where his cell phone had been—“in what [Officer Bright]
believed to be furtive movement.” Id. Bright asked Shawn to turn around with his hands over
his head. Id. at 38. Rather than comply, Shawn “kept asking” why Bright was there. Id. And
rather than answer, Bright “walked up and unsnapped and temporarily took possession of his
firearm.” Id.

       Shawn adds these details. Before Officer Bright emerged from his car, Shawn began
holding his phone (and leash and arms) out in front of him to record the interaction. Bright
walked up with “his hand on his firearm,” announced that if Shawn “go[es] for the weapon, he’s
going to shoot,” and refused to answer any of Shawn’s questions, such as: “[W]hat was going
on?” “[A]m I free to go?” “[A]m I under arrest here?” R. 28 at 33–35. After Bright disarmed
Shawn and explained he was responding to a call, Bright demanded Shawn’s driver’s license and
No. 14-4050             Northrup v. City of Toledo Police Dep’t, et al.                   Page 3

concealed-carry permit. Shawn gave Bright his license, but Denise told Bright to look up the
permit himself, prompting Bright to threaten to “arrest [Shawn] for inducing panic right now.”
Id. at 36.

        At that point, Bright placed Shawn in handcuffs and put him in the squad car. Bright
suspected Shawn had committed the Ohio offense of “inducing panic.” R. 26 at 47; see Ohio
Rev. Code § 2917.31. After Bright looked up Shawn’s driver’s license, he discovered that
Shawn had a concealed-carry permit—making the family walk (dog, cellphone, gun, and all)
legal. After about a half hour and after another officer (Sergeant Daniel Ray) arrived, Officer
Bright released Shawn with a citation for “failure to disclose personal information.” Ohio Rev.
Code § 2921.29(A)(1). The police later dropped that charge.

        Shawn Northrup sued Officer Bright, Sergeant Ray, and other members of the Toledo
Police Department in federal court, alleging violations of his rights under the First, Second,
Fourth (and Fourteenth) Amendments as well as state law.            The district court granted the
officers’ summary judgment motion in part, rejecting Northrup’s First and Second Amendment
claims as a matter of law. But it permitted his Fourth Amendment and state-law claims against
Bright and Ray to go to trial. The officers filed this interlocutory appeal.

        Officer Bright claims that he had a “reasonable suspicion” that Northrup was engaged in
criminal activity based on two undisputed facts: (1) Northrup was visibly carrying a gun on his
holster, and (2) Bright was responding to a 911 call. That reasonable suspicion, Bright claims,
justified his disarmament, detention, and citation of Northrup. Before addressing whether he is
right, we should mention a few guiding principles.

        Qualified immunity protects the officers from this lawsuit if either of two things is true:
The officers did not violate Northrup’s Fourth Amendment rights, or any such rights were not
clearly established at the time of the search. Summary judgment is appropriate if no material
fact dispute clouds the officers’ defense and if they are entitled to judgment as a matter of law.
And the nonmovant—here Northrup—gets the benefit of all reasonable inferences in the record.

        The Fourth Amendment protects “the people” from “unreasonable searches and
seizures.” U.S. Const. amend. IV. The guarantee does not prevent the police from initiating
No. 14-4050              Northrup v. City of Toledo Police Dep’t, et al.                 Page 4

“consensual encounter[s]” with individuals—from approaching them on public streets and in
other public places and asking them questions. United States v. Drayton, 536 U.S. 194, 200–01
(2002). But it does prevent the police from stopping and frisking individuals in the absence of
“reasonable suspicion” that the individual has committed, or is about to commit, a crime. Terry
v. Ohio, 392 U.S. 1, 21, 27 (1968). More than an “inchoate and unparticularized suspicion or
‘hunch’” is needed to stop and frisk an individual; the officer must identify “specific and
articulable facts” of criminality. Id. at 27.

        The facts of Terry make the abstract more concrete. A Cleveland police officer noticed
two young men pacing outside a store and closely scrutinizing it. Id. at 5–6. Afraid the two men
might be planning an armed robbery—“casing” the joint in the Court’s words—the officer
approached the men, identified himself as a police officer, and asked what they were doing. Id.
at 6–7. The men were evasive, leading the officer to spin one of the men around and pat down
his clothing to check if he was armed. Id. He was. The officer found a concealed—and illegal
to possess at the time—handgun. Id. When the Supreme Court considered the men’s argument
that this “stop and frisk” amounted to an unreasonable search and seizure, Chief Justice Warren
wrote for eight Justices that police officers may reasonably intrude into a pedestrian’s personal
security if they can “point to specific and articulable facts which, taken together with rational
inferences from those facts, reasonably warrant that intrusion.” Id. at 21.

        In today’s case, Officer Bright relies on two “specific and articulable facts”: Northrup’s
open possession of a firearm and the 911 call about what Northrup was doing. The Fourth
Amendment no doubt permitted Bright to approach Northrup and to ask him questions. But that
is not what he did. He relied on these facts to stop Northrup, disarm him, and handcuff him.
Ohio law permits the open carry of firearms, Ohio Rev. Code § 9.68(C)(1), and thus permitted
Northrup to do exactly what he was doing. While the dispatcher and motorcyclist may not have
known the details of Ohio’s open-carry firearm law, the police officer had no basis for such
uncertainty. If it is appropriate to presume that citizens know the parameters of the criminal
laws, it is surely appropriate to expect the same of law enforcement officers—at least with regard
to unambiguous statutes. Heien v. North Carolina, 135 S. Ct. 530, 540 (2014).
No. 14-4050             Northrup v. City of Toledo Police Dep’t, et al.                   Page 5

        Clearly established law required Bright to point to evidence that Northrup may have been
“armed and dangerous.” Sibron v. New York, 392 U.S. 40, 64 (1968) (emphasis added). Yet all
he ever saw was that Northrup was armed—and legally so. To allow stops in this setting “would
effectively eliminate Fourth Amendment protections for lawfully armed persons.” United States
v. King, 990 F.2d 1552, 1559 (10th Cir. 1993); accord United States v. Ubiles, 224 F.3d 213, 218
(3d Cir. 2000); United States v. Black, 707 F.3d 531, 540 (4th Cir. 2013); United States v. Roch,
5 F.3d 894, 899 (5th Cir. 1993).

        This requirement and the impropriety of Officer Bright’s demands are particularly acute
in a State like Ohio. Not only has the State made open carry of a firearm legal, but it also does
not require gun owners to produce or even carry their licenses for inquiring officers. See Ohio
Rev. Code §§ 9.68(C)(1), 2923.12; Mike DeWine, Ohio Att’y Gen., Ohio’s Concealed Carry
Laws and License Application 15 (2015) (“Ohio’s concealed carry laws do not regulate ‘open’
carry of firearms. If you openly carry, use caution. The open carry of firearms is a legal activity
in Ohio.”); R. 26 at 121 (“If an officer engages in a conversation with a person who is carrying a
gun openly, but otherwise is not committing a crime, the person cannot be required to produce
identification.”).

        What about the verbal dispute between the Northrups and the motorcyclist? Doesn’t that
justify Bright’s suspicion that the Northrups were engaged in criminal activity? No, for at least
two reasons. There is no evidence that Bright knew about the dispute: All that the dispatcher
told him was there was a man “walking his dog on Rochelle [Road] carrying a handgun out in
the open.” R. 26 at 35, 115. Even if Bright had known about the argument, the statute that he
suspected Northrup of violating—“inducing panic”—does not cover what happened. Under
Ohio law, “inducing panic” applies to circulating a false warning of an impending “catastrophe,”
threatening to commit an “offense of violence,” or committing an offense with “reckless
disregard of the likelihood” that it will cause “serious public inconvenience or alarm,” Ohio Rev.
Code § 2917.31. Carrying a handgun out in the open is not an “offense” in Ohio and thus does
not fall within any of these proscribed activities.

        What about the possibility that Northrup was carrying a firearm not covered by the Ohio
law? Had Northrup been carrying a gun that looked like an assault rifle or some other illicit
No. 14-4050             Northrup v. City of Toledo Police Dep’t, et al.                   Page 6

firearm, that might have justified the officer’s conduct. See Embody v. Ward, 695 F.3d 577,
580–81 (6th Cir. 2012). But there is no evidence that this was the case, and Bright indeed does
not even make this argument.

       What about the possibility that Northrup was not licensed to carry a gun or that he was a
felon prohibited from possessing a gun? Where it is lawful to possess a firearm, unlawful
possession “is not the default status.” Black, 707 F.3d at 540; Ubiles, 224 F.3d at 217. There is
no “automatic firearm exception” to the Terry rule. Florida v. J.L., 529 U.S. 266, 272 (2000). In
Ublies, the Third Circuit showed why. There, police responded to an anonymous tip that Ubiles
was carrying a gun while attending a crowded street festival in the Virgin Islands—which on its
face was a legal activity. 224 F.3d at 214. The police nevertheless detained Ubiles even though
they were unaware of “any articulable facts suggesting that the gun Ubiles possessed was
defaced or unlicensed, [or] that Ubiles posed a safety risk.” Id. at 218. In rejecting the officers’
argument that Ubiles’s possession might have been illegal, the court treated the situation as “no
different” from a setting in which the officers suspected “that Ubiles possessed a wallet, a
perfectly legal act in the Virgin Islands, and the authorities stopped him for this reason. Though
a search of that wallet may have revealed counterfeit bills—the possession of which is a crime
under United States law—the officers would have had no justification to stop Ubiles based
merely on information that he possessed a wallet.” Id. (citation omitted).

       Officer Bright adds that he faced a difficult choice: “[R]espond to the communities’ fear
and the appearance of the gunman by performing an investigatory stop, or do nothing while
Northrup continued walking down Rochelle and hope that he was not about to start shooting.”
Appellant’s Br. 16. Law enforcement, to be sure, is not an easy job, and it often puts officers to
difficult choices.   But this was not one of them.        The argument indeed presents a false
dichotomy. Nothing in the Fourth Amendment prohibited Officer Bright from responding to the
call and ascertaining through a consensual encounter whether Northrup appeared dangerous.
Until any such suspicion emerged, however, Bright’s hope that Northrup “was not about to start
shooting” remains another word for the trust that Ohioans have placed in their State’s approach
to gun licensure and gun possession.
No. 14-4050            Northrup v. City of Toledo Police Dep’t, et al.                   Page 7

       What about Officer Bright’s perception that Northrup made a “furtive movement” toward
the gun during the encounter? Officer Bright was not the only witness to this encounter,
however. Northrup claims that he put both of his hands in front of him as soon as the officer
approached—with one holding the cell phone and the other holding the dog leash. R. 28 at 33–
35. Only the officer claims that Northrup made a furtive movement after he put both hands in
front of him.   On this record, only a jury may decide whether Northrup made any such
movement and whether it justified the officer’s conduct.

       While open-carry laws may put police officers (and some motorcyclists) in awkward
situations from time to time, the Ohio legislature has decided its citizens may be entrusted with
firearms on public streets. Ohio Rev. Code §§ 9.68, 2923.125. The Toledo Police Department
has no authority to disregard this decision—not to mention the protections of the Fourth
Amendment—by detaining every “gunman” who lawfully possesses a firearm. See Ohioans for
Concealed Carry, Inc. v. Clyde, 896 N.E.2d 967, 976 (Ohio 2008) (holding that Ohio’s statewide
handgun policy preempts contrary exercises of a local government’s police power). And it has
long been clearly established that an officer needs evidence of criminality or dangerousness
before he may detain and disarm a law-abiding citizen. We thus affirm the district court’s
conclusion that, after reading the factual inferences in the record in Northrup’s favor, Officer
Bright could not reasonably suspect that Northrup needed to be disarmed.

       Officer Bright’s other arguments on appeal rise and fall with his reasonable suspicion
defense. If Bright had no reason to stop and frisk Northrup, he violated clearly established law
in handcuffing—fully seizing—Northrup in his squad car for thirty minutes. Smoak v. Hall,
460 F.3d 768, 781 (6th Cir. 2006). Officer Bright, quite wisely, no longer defends the theory
raised below that he had probable cause to arrest Northrup. And a jury, as the district court also
correctly concluded, is the appropriate body to determine whether he acted with malice in seizing
Northrup and thus whether he committed a state tort.

       Unlike Officer Bright, Sergeant Ray is entitled to qualified immunity.           “[W]here
individual police officers, acting in good faith and in reliance on the reports of other officers,
have a sufficient factual basis for believing that they are in compliance with the law, qualified
immunity is warranted, notwithstanding the fact that an action may be illegal when viewed under
No. 14-4050            Northrup v. City of Toledo Police Dep’t, et al.                  Page 8

the totality of the circumstances.” Humphrey v. Mabry, 482 F.3d 840, 847 (6th Cir. 2007).
Sergeant Ray did not arrive until after Northrup was handcuffed in the back of Officer Bright’s
police car. Ray was then told Bright’s account of events, including of Northrup’s “furtive
movement” toward his gun and his failure to produce identification when initially requested. R.
26 at 63; R. 29 at 23; R. 38-2 at 3. With this information in hand, Ray contacted the Toledo
Police Department detective’s bureau to help determine the proper charge. A detective advised
Ray to cite Northrup for failure to disclose personal information, Ohio Rev. Code § 2921.29,
which Ray and Bright then did.

       Northrup has a claim against Sergeant Ray only if we infer that Officer Bright, in his
initial conversation apprising Ray of recent events, confessed to an illegal seizure. There is no
basis in the record for such an inference. During his deposition, Northrup stated that he did not
overhear the conversation between Bright and Ray, R. 28 at 38, and Northrup’s wife does not
mention the content of that conversation in her affidavit, R. 38-3 at 4–5. Accordingly, Ray
should receive qualified immunity.

       For these reasons, we affirm in part and reverse in part and remand for further
proceedings.

```

---

## GROUP: content/cases/Ohio v. Robinette.md  (`case`, 5 assertions)

### content_page

```
---
title: "Ohio v. Robinette"
type: case
citation: "519 U.S. 33 (1996)"
parallel_cite: "117 S. Ct. 417; 136 L. Ed. 2d 347"
neutral_cite: 1996 U.S. LEXIS 6971
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1996
date_decided: 1996-11-18
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1996-11-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Ohio v. Robinette
  varies_by_point: false
  scope_note: "No 'free to go' advisory required for voluntary consent; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118066/ohio-v-robinette/"
  cluster_id: 118066
  opinion_id: 118066
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Schneckloth v. Bustamonte]]", "[[Florida v. Bostick]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent-search", "voluntariness", "traffic-stop"]
holding: "No-warning rule: officers need not tell a lawfully stopped motorist he is 'free to go' for his subsequent consent to search to be voluntary."
lake:
  record_id: Ohio v. Robinette
  status: verified
  projected_at: 2026-07-06
---

# Ohio v. Robinette

*519 U.S. 33 (1996)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A deputy stopped Robinette for speeding, ran his license, returned it, and told him he was getting a warning. The deputy then asked whether Robinette was carrying any contraband and for consent to search his car. Robinette consented, and the deputy found drugs. The Ohio Supreme Court held the consent invalid because the deputy had not first told Robinette he was free to go.

## Issue
Whether the Fourth Amendment requires officers to tell a lawfully detained motorist that he is "free to go" before a consent to search obtained during the encounter can be voluntary.

## Rule
No. Just as the Court has not required a detailed warning before an ordinary consent search, "so too would it be unrealistic to require police officers to always inform detainees that they are free to go before a consent to search may be deemed voluntary." — 519 U.S. at 39–40. ^pin-39

"The Fourth Amendment test for a valid consent to search is that the consent be voluntary, and '[v]oluntariness is a question of fact to be determined from all the circumstances.'" — *Id.* at 40. ^pin-40

## Application
The absence of a "free to go" advisory did not by itself render Robinette's consent involuntary; whether his consent was voluntary had to be determined from all the circumstances of the encounter. The Court rejected the Ohio Supreme Court's [[Common Legal Terms#per-se|per se]] rule and [[Reading and Citing Cases#on-remand|remanded]] for application of the totality-of-the-circumstances standard.

## Conclusion
No "free to go" warning is constitutionally required; the [[Common Legal Terms#per-se|per se]] rule was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Robinette* applies the totality-of-the-circumstances voluntariness standard of [[Schneckloth v. Bustamonte]] and parallels [[Florida v. Bostick]]'s rejection of bright-line advisory requirements.

## Appears on
- [[Consent Searches]] — *Key — Progeny / Refinement*

## Sources
- *Ohio v. Robinette*, 519 U.S. 33 (1996) — https://www.courtlistener.com/opinion/118066/ohio-v-robinette/ — pinpoints: 39–40, 40.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0e754c391823b005", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "519 U.S. 33 (1996)", "court": "U.S. Supreme Court", "neutral_cite": "1996 U.S. LEXIS 6971", "official_citation_present": true, "parallel_cite": "117 S. Ct. 417; 136 L. Ed. 2d 347", "title": "Ohio v. Robinette", "year": "1996"}}
{"assertion_id": "386f02c507a31044", "dimension": "support", "kind": "home_role", "locator": {"home": "Consent Searches"}, "payload": {"home": "Consent Searches", "role": "Key — Progeny / Refinement", "title": "Ohio v. Robinette"}}
{"assertion_id": "d80632d55afffad1", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "No-warning rule: officers need not tell a lawfully stopped motorist he is 'free to go' for his subsequent consent to search to be voluntary.", "title": "Ohio v. Robinette"}}
{"assertion_id": "25dab56abdcba24e", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Ohio v. Robinette"}}
{"assertion_id": "dabf3809a67d6cc2", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1996-11-18", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Ohio v. Robinette", "field_i_validity": "good_law", "scope_note": "No 'free to go' advisory required for voluntary consent; good law.", "title": "Ohio v. Robinette", "varies_by_point": "false"}}
```

### lake record — Ohio v. Robinette

```json
{
  "schema_version": "s2.v1",
  "record_id": "Ohio v. Robinette",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Ohio v. Robinette",
    "case_name_short": "Robinette",
    "case_name_full": "Ohio v. Robinette",
    "input_case_name": "Ohio v. Robinette",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1996-11-18",
    "year": 1996,
    "docket": null,
    "cluster_id": 118066,
    "lead_opinion_id": 118066,
    "sibling_ids": [
      118066,
      9433390,
      9433391,
      9433392
    ],
    "absolute_url": "/opinion/118066/ohio-v-robinette/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9161388,
        "score": 20,
        "case_name": "Ohio v. Robinette"
      },
      {
        "cluster_id": 9161387,
        "score": 20,
        "case_name": "Ohio v. Robinette"
      },
      {
        "cluster_id": 9159470,
        "score": 20,
        "case_name": "Ohio v. Robinette"
      },
      {
        "cluster_id": 9159469,
        "score": 20,
        "case_name": "Ohio v. Robinette"
      },
      {
        "cluster_id": 9274301,
        "score": 20,
        "case_name": "Ohio v. Robinette"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "519 U.S. 33",
      "volume": "519",
      "reporter": "U.S.",
      "page": "33",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "117 S. Ct. 417",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "417",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "136 L. Ed. 2d 347",
        "volume": "136",
        "reporter": "L. Ed. 2d",
        "page": "347",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1996 U.S. LEXIS 6971",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "6971",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "519 U.S. 33",
        "volume": "519",
        "reporter": "U.S.",
        "page": "33",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "117 S. Ct. 417",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "417",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "136 L. Ed. 2d 347",
        "volume": "136",
        "reporter": "L. Ed. 2d",
        "page": "347",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1996 U.S. LEXIS 6971",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "6971",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "519 U.S. 33",
    "official_selection": {
      "court_class": "scotus",
      "selected": "519 U.S. 33",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-39",
      "page": null,
      "quote": "before a consent to search obtained during the encounter can be voluntary. ## Rule No. Just as the Court has not required a detailed warning before an ordinary consent search,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-40",
      "page": null,
      "quote": "The Fourth Amendment test for a valid consent to search is that the consent be voluntary, and '[v]oluntariness is a question of fact to be determined from all the circumstances.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1996-11-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Ohio v. Robinette",
    "varies_by_point": false,
    "scope_note": "No 'free to go' advisory required for voluntary consent; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Marlon Juan Lall v. the State of Texas",
          "cluster_id": 10046849,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Privette",
          "cluster_id": 9387170,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Villagran",
          "cluster_id": 4422358,
          "cite": [
            "477 Mass. 711",
            "81 N.E.3d 310"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Connor William Clar Steffens",
          "cluster_id": 4332280,
          "cite": [
            "889 N.W.2d 691",
            "2016 Iowa App. LEXIS 1316",
            "2016 WL 7393893"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dickson",
          "cluster_id": 4244499,
          "cite": [
            "141 A.3d 810",
            "322 Conn. 410",
            "2016 Conn. LEXIS 236"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Carmouche v. State",
          "cluster_id": 1463452,
          "cite": [
            "10 S.W.3d 323",
            "2000 Tex. Crim. App. LEXIS 8",
            "2000 WL 60020"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Layne",
          "cluster_id": 118289,
          "cite": [
            "143 L. Ed. 2d 818",
            "119 S. Ct. 1692",
            "526 U.S. 603",
            "1999 U.S. LEXIS 3633"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baldwin v. Reese",
          "cluster_id": 134723,
          "cite": [
            "158 L. Ed. 2d 64",
            "124 S. Ct. 1347",
            "541 U.S. 27",
            "2004 U.S. LEXIS 1835"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rodriguez v. United States",
          "cluster_id": 2795278,
          "cite": [
            "575 U.S. 348",
            "135 S. Ct. 1609",
            "191 L. Ed. 2d 492",
            "2015 U.S. LEXIS 2807",
            "83 U.S.L.W. 4241",
            "25 Fla. L. Weekly Fed. S 191"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
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
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 2336338,
          "cite": [
            "68 S.W.3d 644",
            "2002 Tex. Crim. App. LEXIS 17",
            "2002 WL 122735"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Knights",
          "cluster_id": 118468,
          "cite": [
            "151 L. Ed. 2d 497",
            "122 S. Ct. 587",
            "534 U.S. 112",
            "2001 U.S. LEXIS 10950"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
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
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Genesis HealthCare Corp. v. Symczyk",
          "cluster_id": 858086,
          "cite": [
            "185 L. Ed. 2d 636",
            "133 S. Ct. 1523",
            "569 U.S. 66",
            "2013 U.S. LEXIS 3157",
            "24 Fla. L. Weekly Fed. S 133",
            "81 U.S.L.W. 4229",
            "20 Wage & Hour Cas.2d (BNA) 801",
            "2013 WL 1567370"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. State",
          "cluster_id": 2419717,
          "cite": [
            "947 S.W.2d 240",
            "1997 Tex. Crim. App. LEXIS 43",
            "1997 WL 292676"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
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
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
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
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. United States",
          "cluster_id": 118309,
          "cite": [
            "144 L. Ed. 2d 370",
            "119 S. Ct. 2090",
            "527 U.S. 373",
            "1999 U.S. LEXIS 4201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kothe v. State",
          "cluster_id": 1504839,
          "cite": [
            "152 S.W.3d 54",
            "2004 Tex. Crim. App. LEXIS 1749",
            "2004 WL 2347781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Yeargan",
          "cluster_id": 1060948,
          "cite": [
            "958 S.W.2d 626",
            "1997 Tenn. LEXIS 574",
            "1997 WL 724993"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
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
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
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
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thornton v. United States",
          "cluster_id": 134746,
          "cite": [
            "158 L. Ed. 2d 905",
            "124 S. Ct. 2127",
            "541 U.S. 615",
            "2004 U.S. LEXIS 3681"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
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
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gutierrez v. State",
          "cluster_id": 1508583,
          "cite": [
            "221 S.W.3d 680",
            "2007 Tex. Crim. App. LEXIS 500",
            "2007 WL 1217343"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Granite Rock Co. v. International Brotherhood of Teamsters",
          "cluster_id": 149288,
          "cite": [
            "177 L. Ed. 2d 567",
            "130 S. Ct. 2847",
            "561 U.S. 287",
            "2010 U.S. LEXIS 5255",
            "22 Fla. L. Weekly Fed. S 593",
            "78 U.S.L.W. 4712",
            "188 L.R.R.M. (BNA) 2897"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gomez",
          "cluster_id": 2613548,
          "cite": [
            "932 P.2d 1",
            "122 N.M. 777",
            "1997 NMSC 006"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Grubbs",
          "cluster_id": 145670,
          "cite": [
            "164 L. Ed. 2d 195",
            "126 S. Ct. 1494",
            "547 U.S. 90",
            "2006 U.S. LEXIS 2496"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Strickler",
          "cluster_id": 2156861,
          "cite": [
            "757 A.2d 884",
            "563 Pa. 47",
            "2000 Pa. LEXIS 2114"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark A. Lee v. City of Chicago",
          "cluster_id": 782110,
          "cite": [
            "330 F.3d 456",
            "2003 U.S. App. LEXIS 10254",
            "2003 WL 21196550"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118066 OR 9433390 OR 9433391 OR 9433392) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDY0NjUyODAwMDAwJnM9MzIwODE1MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118066+OR+9433390+OR+9433391+OR+9433392%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118066 OR 9433390 OR 9433391 OR 9433392)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNTImcz00NDcyMzkyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28118066+OR+9433390+OR+9433391+OR+9433392%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118066 OR 9433390 OR 9433391 OR 9433392)",
        "reviewed": 45,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 45,
        "triage_read": 1,
        "triage_snippet_classified": 44
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118066 OR 9433390 OR 9433391 OR 9433392)",
    "indexed_citing_opinions": 1352,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118066,
        "count": 1211,
        "count_source": "search"
      },
      {
        "opinion_id": 9433390,
        "count": 175,
        "count_source": "search"
      },
      {
        "opinion_id": 9433391,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433392,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2025,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/ohio-v-robinette.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4NTE5OTkmcz05NTY3NjgzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118066+OR+9433390+OR+9433391+OR+9433392%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118066,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 109424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 109611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 109730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 110168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 110380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 110636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 111093,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 111221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 111378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 112595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 112631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 117905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 3755951,
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
    "date_created": "2026-07-05T16:05:25Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:05:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:05:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:08:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:05:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Ohio v. Robinette

```
<div>
<center><b><span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/" aria-description="Citation for case: Ohio v. Robinette">519 U.S. 33</a></span> (1996)</b></center>
<center><h1>OHIO<br>
v.<br>
ROBINETTE</h1></center>
<center>No. 95-891.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued October 8, 1996.</center>
<center>Decided November 18, 1996.</center>
CERTIORARI TO THE SUPREME COURT OF OHIO
<p><span class="star-pagination">*35</span> Rehnquist, C. J., delivered the opinion of the Court, in which O'Connor, Scalia, Kennedy, Souter, Thomas, and Breyer, JJ., joined. Ginsburg, J.,filed an opinion concurring in the judgment, <i>post,</i> p. 40. Stevens, J., filed a dissenting opinion, <i>post,</i> p. 45.</p>
<p><i>Carley J. Ingram</i> argued the cause for petitioner. With her on the briefs was <i>Mathias H. Heck, Jr.</i> </p>
<p><i>Irving L. Gornstein</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. On the brief were <i>Solicitor General Days, Acting Assistant Attorney General Keeney, Deputy Solicitor General Dreeben, Paul A. Engelmayer,</i> and <i>Joseph C. Wyderko.</i> </p>
<p><i>James D. Ruppert</i> argued the cause and filed a brief for respondent.<sup>[*]</sup></p>
<p><span class="star-pagination">*35</span> Chief Justice Rehnquist delivered the opinion of the Court.</p>
<p>We are here presented with the question whether the Fourth Amendment requires that a lawfully seized defendant must be advised that he is "free to go" before his consent to search will be recognized as voluntary. We hold that it does not.</p>
<p>This case arose on a stretch of Interstate 70 north of Dayton, Ohio, where the posted speed limit was 45 miles per hour because of construction. Respondent Robert D. Robinette was clocked at 69 miles per hour as he drove his car along this stretch of road, and was stopped by Deputy Roger Newsome of the Montgomery County Sheriff's Office. Newsome asked for and was handed Robinette's driver's license, and he ran a computer check which indicated that Robinette had no previous violations. Newsome then asked Robinette to step out of his car, turned on his mounted video camera, issued a verbal warning to Robinette, and returned his license.</p>
<p>At this point, Newsome asked, "One question before you get gone: [A]re you carrying any illegal contraband in your <span class="star-pagination">*36</span> car? Any weapons of any kind, drugs, anything like that?" App. to Brief for Respondent 2 (internal quotation marks omitted). Robinette answered "no" to these questions, after which Deputy Newsome asked if he could search the car. Robinette consented. In the car, Deputy Newsome discovered a small amount of marijuana and, in a film container, a pill which was later determined to be methylenedioxymethamphetamine (MDMA). Robinette was then arrested and charged with knowing possession of a controlled substance, MDMA, in violation of <span class="citation no-link">Ohio Rev. Code Ann. § 2925.11</span>(A) (1993).</p>
<p>Before trial, Robinette unsuccessfully sought to suppress this evidence. He then pleaded "no contest," and was found guilty. On appeal, the Ohio Court of Appeals reversed, ruling that the search resulted from an unlawful detention. The Supreme Court of Ohio, by a divided vote, affirmed. <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/" aria-description="Citation for case: State v. Robinette">73 Ohio St. 3d 650</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/" aria-description="Citation for case: State v. Robinette">653 N. E. 2d 695</a></span> (1995). In its opinion, that court established a bright-line prerequisite for consensual interrogation under these circumstances:</p>
<blockquote>"The right, guaranteed by the federal and Ohio Constitutions, to be secure in one's person and property requires that citizens stopped for traffic offenses be clearly informed by the detaining officer when they are free to go after a valid detention, before an officer attempts to engage in a consensual interrogation. Any attempt at consensual interrogation must be preceded by the phrase `At this time you legally are free to go' or by words of similar import." <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#650" aria-description="Citation for case: State v. Robinette"><i>Id.,</i> at 650-651</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#696" aria-description="Citation for case: State v. Robinette">653 N. E. 2d, at 696</a></span>.</blockquote>
<p>We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./516/1157/">516 U. S. 1157</a></span> (1996), to review this <i>per se</i> rule, and we now reverse.</p>
<p>We must first consider whether we have jurisdiction to review the Ohio Supreme Court's decision. Respondent contends that we lack such jurisdiction because the Ohio decision rested upon the Ohio Constitution, in addition to the <span class="star-pagination">*37</span> Federal Constitution. Under <i>Michigan</i> v.<i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983),when "a state court decision fairly appears to rest primarily on federal law, or to be interwoven with the federal law, and when the adequacy and independence of any possible state law ground is not clear from the face of the opinion, we will accept as the most reasonable explanation that the state court decided the case the way it did because it believed that federal law required it to do so."<sup>[*]</sup><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long"><i>Id.,</i> at 1040-1041</a></span>. Although the opinion below mentions Art. I, § 14, of the Ohio Constitution in passing (a section which reads identically to the Fourth Amendment), the opinion clearly relies on federal law nevertheless. Indeed, the only cases it discusses or even cites are federal cases, except for one state case which itself applies the Federal Constitution.</p>
<p>Our jurisdiction is not defeated by the fact that these citations appear in the body of the opinion, while, under Ohio law, "[the] Supreme Court speaks as a court only through the syllabi of its cases." See <i>Ohio</i> v. <i>Gallagher,</i> <span class="citation" data-id="9426357"><a href="/opinion/109424/ohio-v-gallagher/#259" aria-description="Citation for case: Ohio v. Gallagher">425 U. S. 257, 259</a></span> (1976). When the syllabus, as here, speaks only in general terms of "the federal and Ohio Constitutions," it is permissible for us to turn to the body of the opinion to discern the grounds for decision. <i>Zacchini</i> v. <i>Scripps-Howard Broadcasting Co.</i> , <span class="citation" data-id="9426968"><a href="/opinion/109730/zacchini-v-scripps-howard-broadcasting-co/#566" aria-description="Citation for case: Zacchini v. Scripps-Howard Broadcasting Co.">433 U. S. 562, 566</a></span> (1977).</p>
<p>Respondent Robinette also contends that we may not reach the question presented in the petition because the Supreme Court of Ohio also held, as set out in the syllabus paragraph (1):</p>
<blockquote>"When the motivation behind a police officer's continued detention of a person stopped for a traffic violation is not related to the purpose of the original, constitutional stop, and when that continued detention is not based on any articulable facts giving rise to a suspicion of some <span class="star-pagination">*38</span> separate illegal activity justifying an extension of the detention, the continued detention constitutes an illegal seizure." <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#650" aria-description="Citation for case: State v. Robinette">73 Ohio St. 3d, at 650</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#696" aria-description="Citation for case: State v. Robinette">653 N. E. 2d, at 696</a></span>.</blockquote>
<p>In reliance on this ground, the Supreme Court of Ohio held that when Newsome returned to Robinette's car and asked him to get out of the car, after he had determined in his own mind not to give Robinette a ticket, the detention then became unlawful.</p>
<p>Respondent failed to make any such argument in his brief in opposition to certiorari. See this Court's Rule 15.2. We believe the issue as to the continuing legality of the detention is a "predicate to an intelligent resolution" of the question presented, and therefore "fairly included therein." This Court's Rule 14.1(a); <i>Vance</i> v. <i>Terrazas,</i> <span class="citation" data-id="9427734"><a href="/opinion/110168/vance-v-terrazas/" aria-description="Citation for case: Vance v. Terrazas">444 U. S. 252</a></span>, 258 259, n. 5 (1980). The parties have briefed this issue, and we proceed to decide it.</p>
<p>We think that under our recent decision in <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U. S. 806</a></span> (1996) (decided after the Supreme Court of Ohio decided the present case), the subjective intentions of the officer did not make the continued detention of respondent illegal under the Fourth Amendment. As we made clear in <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span>,</i> "`the fact that [an] officer does not have the state of mind which is hypothecated by the reasons which provide the legal justification for the officer's action does not invalidate the action taken as long as the circumstances, viewed objectively, justify that action.'. . . Subjective intentions play no role in ordinary, probablecause Fourth Amendment analysis." <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Id.,</a></span></i> at 813 (quoting <i>Scott</i> v. <i>United States,</i> <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#138" aria-description="Citation for case: Scott v. United States">436 U. S. 128, 138</a></span> (1978)). And there is no question that, in light of the admitted probable cause to stop Robinette for speeding, Deputy Newsome was objectively justified in asking Robinette to get out of the car, subjective thoughts notwithstanding. See <i>Pennsylvania</i> v. <i>Mimms,</i> <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#111" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 111, n. 6</a></span> (1977) ("We hold .. . that once a motor vehicle has been lawfully detained for a traffic violation, the police officers may order the driver to get out <span class="star-pagination">*39</span> of the vehicle without violating the Fourth Amendment's proscription of unreasonable searches and seizures").</p>
<p>We now turn to the merits of the question presented. We have long held that the "touchstone of the Fourth Amendment is reasonableness." <i>Florida</i> v. <i>Jimeno,</i> <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#250" aria-description="Citation for case: Florida v. Jimeno">500 U. S. 248, 250</a></span> (1991). Reasonableness, in turn, is measured in objective terms by examining the totality of the circumstances.</p>
<p>In applying this test we have consistently eschewed bright-line rules, instead emphasizing the fact-specific nature of the reasonableness inquiry. Thus, in <i>Florida</i> v. <i>Royer,</i>  <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U. S. 491</a></span> (1983), we expressly disavowed any "litmuspaper test" or single "sentence or . . . paragraph . . . rule," in recognition of the "endless variations in the facts and circumstances" implicating the Fourth Amendment. <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#506" aria-description="Citation for case: Florida v. Royer"><i>Id.,</i> at 506</a></span>. Then, in <i>Michigan</i> v. <i>Chesternut,</i> <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/" aria-description="Citation for case: Michigan v. Chesternut">486 U. S. 567</a></span> (1988), when both parties urged "bright-line rule[s] applicable to all investigatory pursuits," we rejected both proposed rules as contrary to our "traditional contextual approach." <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#572" aria-description="Citation for case: Michigan v. Chesternut"><i>Id.,</i> at 572-573</a></span>. And again, in <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429</a></span> (1991), when the Florida Supreme Court adopted a <i>per se</i>  rule that questioning aboard a bus always constitutes a seizure, we reversed, reiterating that the proper inquiry necessitates a consideration of "all the circumstances surrounding the encounter." <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#439" aria-description="Citation for case: Florida v. Bostick"><i>Id.,</i> at 439</a></span>.</p>
<p>We have previously rejected a <i>per se</i> rule very similar to that adopted by the Supreme Court of Ohio in determining the validity of a consent to search. In <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973), it was argued that such a consent could not be valid unless the defendant knew that he had a right to refuse the request. We rejected this argument: "While knowledge of the right to refuse consent is one factor to be taken into account, the government need not establish such knowledge as the <i>sine qua non</i> of an effective consent." <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#227" aria-description="Citation for case: Schneckloth v. Bustamonte"><i>Id.,</i> at 227</a></span>. And just as it "would be thoroughly impractical to impose on the normal consent search the detailed requirements of an effective warning," <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#231" aria-description="Citation for case: Schneckloth v. Bustamonte"><i>id.,</i> at 231</a></span>, so too would it be <span class="star-pagination">*40</span> unrealistic to require police officers to always inform detainees that they are free to go before a consent to search may be deemed voluntary.</p>
<p>The Fourth Amendment test for a valid consent to search is that the consent be voluntary, and "[v]oluntariness is a question of fact to be determined from all the circumstances," <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#248" aria-description="Citation for case: Schneckloth v. Bustamonte"><i>id.,</i> at 248-249</a></span>. The Supreme Court of Ohio having held otherwise, its judgment is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i> </p>
<p>Justice Ginsburg, concurring in the judgment.</p>
<p>Robert Robinette's traffic stop for a speeding violation on an interstate highway in Ohio served as prelude to a search of his automobile for illegal drugs. Robinette's experience was not uncommon in Ohio. As the Ohio Supreme Court related, the sheriff's deputy who detained Robinette for speeding and then asked Robinette for permission to search his vehicle "was on drug interdiction patrol at the time." <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#651" aria-description="Citation for case: State v. Robinette">73 Ohio St. 3d 650, 651</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#696" aria-description="Citation for case: State v. Robinette">653 N. E. 2d 695, 696</a></span> (1995). The deputy testified in Robinette's case that he routinely requested permission to search automobiles he stopped for traffic violations. <i><span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/" aria-description="Citation for case: State v. Robinette">Ibid.</a></span></i> According to the deputy's testimony in another prosecution, he requested consent to search in 786 traffic stops in 1992, the year of Robinette's arrest. <i>State</i>  v. <i>Retherford,</i> <span class="citation" data-id="3755951"><a href="/opinion/4001886/state-v-retherford/#594" aria-description="Citation for case: State v. Retherford">93 Ohio App. 3d 586, 594, n. 3</a></span>, <span class="citation" data-id="3755951"><a href="/opinion/4001886/state-v-retherford/#503" aria-description="Citation for case: State v. Retherford">639 N. E. 2d 498, 503, n. 3</a></span>, dism'd, <span class="citation" data-id="6770179"><a href="/opinion/6877572/cleveland-bar-assn-v-young/" aria-description="Citation for case: Cleveland Bar Ass&#x27;n v. Young">69 Ohio St. 3d 1488</a></span>, <span class="citation no-link">635 N. E. 2d 43</span> (1994).</p>
<p>From their unique vantage point, Ohio's courts observed that traffic stops in the State were regularly giving way to contraband searches, characterized as consensual, even when officers had no reason to suspect illegal activity. One Ohio appellate court noted: "[H]undreds, and perhaps thousands of Ohio citizens are being routinely delayed in their travels and asked to relinquish to uniformed police officers their <span class="star-pagination">*41</span> right to privacy in their automobiles and luggage, sometimes for no better reason than to provide an officer the opportunity to `practice' his drug interdiction technique." <span class="citation" data-id="3755951"><a href="/opinion/4001886/state-v-retherford/#594" aria-description="Citation for case: State v. Retherford">93 Ohio App. 3d, at 594</a></span>, <span class="citation" data-id="3755951"><a href="/opinion/4001886/state-v-retherford/#503" aria-description="Citation for case: State v. Retherford">639 N. E. 2d, at 503</a></span> (footnote omitted).</p>
<p>Against this background, the Ohio Supreme Court determined, and announced in Robinette's case, that the federal and state constitutional rights of Ohio citizens to be secure in their persons and property called for the protection of a clear-cut instruction to the State's police officers: An officer wishing to engage in consensual interrogation of a motorist at the conclusion of a traffic stop must first tell the motorist that he or she is free to go. The Ohio Supreme Court described the need for its first-tell-then-ask rule this way:</p>
<blockquote>"The transition between detention and a consensual exchange can be so seamless that the untrained eye may not notice that it has occurred. . . .</blockquote>
<p>. . . . .</p>
<blockquote>"Most people believe that they are validly in a police officer's custody as long as the officer continues to interrogate them. The police officer retains the upper hand and the accouterments of authority. That the officer lacks legal license to continue to detain them is unknown to most citizens, and a reasonable person would not feel free to walk away as the officer continues to address him.</blockquote>
<p>. . . . .</p>
<blockquote>"While the legality of consensual encounters between police and citizens should be preserved, we do not believe that this legality should be used by police officers to turn a routine traffic stop into a fishing expedition for unrelated criminal activity. The Fourth Amendment to the federal Constitution and Section 14, Article I of the Ohio Constitution exist to protect citizens against such an unreasonable interference with their liberty." <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#654" aria-description="Citation for case: State v. Robinette">73 Ohio St. 3d, at 654-655</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#698" aria-description="Citation for case: State v. Robinette">653 N. E. 2d, at 698-699</a></span>.</blockquote>
<p><span class="star-pagination">*42</span> Today's opinion reversing the decision of the Ohio Supreme Court does not pass judgment on the wisdom of the first-tell-then-ask rule. This Court's opinion simply clarifies that the Ohio Supreme Court's instruction to police officers in Ohio is not, under this Court's controlling jurisprudence, the command of the Federal Constitution. See <i>ante,</i> at 39 40. The Ohio Supreme Court invoked both the Federal Constitution and the Ohio Constitution without clearly indicating whether state law, standing alone, independently justified the court's rule. The ambiguity in the Ohio Supreme Court's decision renders this Court's exercise of jurisdiction proper under <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1040-1042</a></span> (1983), and this Court's decision on the merits is consistent with the Court's "totality of the circumstances" Fourth Amendment precedents, see <i>ante,</i> at 39. I therefore concur in the Court's judgment.</p>
<p>I write separately, however, because it seems to me improbable that the Ohio Supreme Court understood its firsttell-then-ask rule to be the Federal Constitution's mandate for the Nation as a whole. "[A] State is free <i>as a matter of its own law</i> to impose greater restrictions on police activity than those this Court holds to be necessary upon federal constitutional standards." <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#719" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714, 719</a></span> (1975).<sup>[*]</sup> But ordinarily, when a state high court grounds a rule of criminal procedure in the Federal Constitution, the <span class="star-pagination">*43</span> court thereby signals its view that the Nation's Constitution would require the rule in all 50 States. Given this Court's decisions in consent-to-search cases such as <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973), and <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429</a></span> (1991), however, I suspect that the Ohio Supreme Court may not have homed in on the implication ordinarily to be drawn from a state court's reliance on the Federal Constitution. In other words, I question whether the Ohio court thought of the strict rule it announced as a rule for the governance of police conduct not only in Miami County, Ohio, but also in Miami, Florida.</p>
<p>The first-tell-then-ask rule seems to be a prophylactic measure not so much extracted from the text of any constitutional provision as crafted by the Ohio Supreme Court to reduce the number of violations of textually guaranteed rights. In <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), this Court announced a similarly motivated rule as a minimal national requirement without suggesting that the text of the Federal Constitution required the precise measures the Court's opinion set forth. See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 467</a></span> ("[T]he Constitution [does not] necessarily requir[e] adherence to any particular solution" to the problems associated with custodial interrogations.); see also <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#306" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 306</a></span> (1985) ("The <i>Miranda</i> exclusionary rule . . . sweeps more broadly than the Fifth Amendment itself."). Although all parts of the United States fall within this Court's domain, the Ohio Supreme Court is not similarly situated. That court can declare prophylactic rules governing the conduct of officials in Ohio, but it cannot command the police forces of sister States. The very ease with which the Court today disposes of the federal leg of the Ohio Supreme Court's decision strengthens my impression that the Ohio Supreme Court saw its rule as a measure made for Ohio, designed to reinforce in that State the right of the people to be secure against unreasonable searches and seizures.</p>
<p><span class="star-pagination">*44</span> The Ohio Supreme Court's syllabus and opinion, however, were ambiguous. Under <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span>,</i> the existence of ambiguity regarding the federal- or state-law basis of a state-court decision will trigger this Court's jurisdiction. <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i> governs even when, all things considered, the more plausible reading of the state court's decision may be that the state court did not regard the Federal Constitution alone as a sufficient basis for its ruling. Compare <i>Arizona</i> v. <i>Evans,</i> <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#7" aria-description="Citation for case: Arizona v. Evans">514 U. S. 1, 7-9</a></span> (1995), with <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#31" aria-description="Citation for case: Arizona v. Evans"><i>id.,</i> at 31-33</a></span> (Ginsburg, J., dissenting).</p>
<p>It is incumbent on a state court, therefore, when it determines that its State's laws call for protection more complete than the Federal Constitution demands, to be clear about its ultimate reliance on state law. Similarly, a state court announcing a new legal rule arguably derived from both federal and state law can definitively render state law an adequate and independent ground for its decision by a simple declaration to that effect. A recent Montana Supreme Court opinion on the scope of an individual's privilege against self-incrimination includes such a declaration:</p>
<blockquote>"While we have devoted considerable time to a lengthy discussion of the application of the Fifth Amendment to the United States Constitution, it is to be noted that this holding is also based separately and independently on [the defendant's] right to remain silent pursuant to Article II, Section 25 of the Montana Constitution." <i>State</i>  v. <i>Fuller,</i> <span class="citation" data-id="9509960"><a href="/opinion/884042/state-v-fuller/#167" aria-description="Citation for case: State v. Fuller">276 Mont. 155, 167</a></span>, <span class="citation" data-id="9509960"><a href="/opinion/884042/state-v-fuller/#816" aria-description="Citation for case: State v. Fuller">915 P. 2d 809, 816</a></span>, cert. denied, <i>post,</i> p. 930.</blockquote>
<p>An explanation of this order meets the Court's instruction in <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i> that "[i]f the state court decision indicates clearly and expressly that it is alternatively based on bona fide separate, adequate, and independent grounds, [this Court] will not undertake to review the decision." <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1041" aria-description="Citation for case: Michigan v. Long">463 U. S., at 1041</a></span>.</p>
<p>On remand, the Ohio Supreme Court may choose to clarify that its instructions to law enforcement officers in Ohio find <span class="star-pagination">*45</span> adequate and independent support in state law, and that in issuing these instructions, the court endeavored to state dispositively only the law applicable in Ohio. See <i>Evans,</i> <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#30" aria-description="Citation for case: Arizona v. Evans">514 U. S., at 30-34</a></span> (Ginsburg, J., dissenting). To avoid misunderstanding, the Ohio Supreme Court must itself speak with the clarity it sought to require of its State's police officers. The efficacy of its endeavor to safeguard the liberties of Ohioans without disarming the State's police can then be tested in the precise way Our Federalism was designed to work. See, <i>e. g.,</i> Kaye, State Courts at the Dawn of a New Century: Common Law Courts Reading Statutes and Constitutions, 70 N. Y. U. L. Rev. 1, 11-18 (1995); Linde, First Things First: Rediscovering the States' Bills of Rights, <span class="citation no-link">9 U. Balt. L. Rev. 379</span>, 392-396 (1980).</p>
<p>Justice Stevens, dissenting.</p>
<p>The Court's holding today is narrow: The Federal Constitution does not require that a lawfully seized person be advised that he is "free to go" before his consent to search will be recognized as voluntary. I agree with that holding. Given the Court's reading of the opinion of the Supreme Court of Ohio, I also agree that it is appropriate for the Court to limit its review to answering the sole question presented in the State's certiorari petition.<sup>[1]</sup> As I read the state-court opinion, however, the prophylactic rule announced in the second syllabus was intended as a guide to the decision of future cases rather than an explanation of the decision in this case. I would therefore affirm the judgment of the Supreme Court of Ohio because it correctly held that respondent's consent to the search of his vehicle was the product of an unlawful detention. Moreover, it is important <span class="star-pagination">*46</span> to emphasize that nothing in the Federal Constitutionor in this Court's opinionprevents a State from requiring its law enforcement officers to give detained motorists the advice mandated by the Ohio court.</p>
<p></p>
<h2>I</h2>
<p>The relevant facts are undisputed.<sup>[2]</sup> Officer Newsome stopped respondent because he was speeding. Neither at the time of the stop nor at any later time prior to the search of respondent's vehicle did the officer have any basis for believing that there were drugs in the car. After ordering respondent to get out of his car, issuing a warning, and returning his driver's license, Newsome took no further action related to the speeding violation. He did, however, state: "One question before you get gone: are you carrying any illegal contraband in your car? Any weapons of any kind, drugs, anything like that?" Thereafter, he obtained respondent's consent to search the car.</p>
<p>These facts give rise to two questions of law: whether respondent was still being detained when the "one question" was asked, and, if so, whether that detention was unlawful. In my opinion the Ohio Appellate Court and the Ohio Supreme Court correctly answered both of those questions.</p>
<p>The Ohio Supreme Court correctly relied upon <i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544</a></span> (1980),<sup>[3]</sup> which stated that "a person has been `seized' within the meaning of the Fourth Amendment . . . if, in view of all of the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave." <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall"><i>Id.,</i> at 554</a></span> (opinion of Stewart, J.); see <i>Michigan</i> v. <i>Chesternut,</i> <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#573" aria-description="Citation for case: Michigan v. Chesternut">486 U. S. 567, 573</a></span> (1988) (noting that "[t]he Court has since embraced this test"). See also <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#435" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429, 435-436</a></span> (1991) (applying variant of this approach). The Ohio Court <span class="star-pagination">*47</span> of Appeals applied a similar analysis. See App. to Pet. for Cert. 17-18.</p>
<p>Several circumstances support the Ohio courts' conclusion that a reasonable motorist in respondent's shoes would have believed that he had an obligation to answer the "one question" and that he could not simply walk away from the officer, get back in his car, and drive away. The question itself sought an answer "<i>before</i> you get gone." In addition, the facts that respondent had been detained, had received no advice that he was free to leave, and was then standing in front of a television camera in response to an official command are all inconsistent with an assumption that he could reasonably believe that he had no duty to respond. The Ohio Supreme Court was surely correct in stating: "Most people believe that they are validly in a police officer's custody as long as the officer continues to interrogate them. The police officer retains the upper hand and the accouterments of authority. That the officer lacks legal license to continue to detain them is unknown to most citizens, and a reasonable person would not feel free to walk away as the officer continues to address him." <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#655" aria-description="Citation for case: State v. Robinette">73 Ohio St. 3d, at 655</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#698" aria-description="Citation for case: State v. Robinette">653 N. E. 2d, at 698</a></span>.<sup>[4]</sup></p>
<p>Moreover, as an objective matter it is fair to presume that most drivers who have been stopped for speeding are in a hurry to get to their destinations; such drivers have no interest in prolonging the delay occasioned by the stop just to engage in idle conversation with an officer, much less to allow <span class="star-pagination">*48</span> a potentially lengthy search.<sup>[5]</sup> I also assume that motoristseven those who are not carrying contrabandhave an interest in preserving the privacy of their vehicles and possessions from the prying eyes of a curious stranger. The fact that this particular officer successfully used a similar method of obtaining consent to search roughly 786 times in one year, <i>State</i> v. <i>Retherford,</i> <span class="citation" data-id="3755951"><a href="/opinion/4001886/state-v-retherford/" aria-description="Citation for case: State v. Retherford">93 Ohio App. 3d 586</a></span>, 591 592, <span class="citation" data-id="3755951"><a href="/opinion/4001886/state-v-retherford/#502" aria-description="Citation for case: State v. Retherford">639 N. E. 2d 498, 502</a></span>, dism'd, <span class="citation" data-id="6770179"><a href="/opinion/6877572/cleveland-bar-assn-v-young/" aria-description="Citation for case: Cleveland Bar Ass&#x27;n v. Young">69 Ohio St. 3d 1488</a></span>, <span class="citation no-link">635 N. E. 2d 43</span> (1994), indicates that motorists generally respond in a manner that is contrary to their self-interest. Repeated decisions by ordinary citizens to surrender that interest cannot satisfactorily be explained on any hypothesis other than an assumption that they believed they had a legal duty to do so.</p>
<p>The Ohio Supreme Court was therefore entirely correct to presume in the first syllabus preceding its opinion that a "continued detention" was at issue here. <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#650" aria-description="Citation for case: State v. Robinette">73 Ohio St. 3d, at 650</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#696" aria-description="Citation for case: State v. Robinette">653 N. E. 2d, at 696</a></span>.<sup>[6]</sup> The Ohio Court of Appeals reached a similar conclusion. In response to the State's contention <span class="star-pagination">*49</span> that Robinette "was free to go" at the time consent was sought, that court heldafter reviewing the record that "a reasonable person in Robinette's position would not believe that the investigative stop had been concluded, and that he or she was free to go,so long as the police officer was continuing to ask investigative questions." App. to Pet. for Cert. 17-18. As I read the Ohio opinions, these determinations were independent of the bright-line rule criticized by the majority.<sup>[7]</sup> I see no reason to disturb them.</p>
<p>In the first syllabus, the Ohio Supreme Court also answered the question whether the officer's continued detention of respondent was lawful or unlawful. See <i>ante,</i> at 37 38. Although there is a possible ambiguity in the use of the word "motivation" in the Ohio Supreme Court's explanation of why the traffic officer's continued detention of respondent was an illegal seizure, the first syllabus otherwise was a correct statement of the relevant federal rule as well as the relevant Ohio rule. As this Court points out in its opinion, as a matter of federal law the subjective motivation of the officer does not determine the legality of a detention. Because I assume that the learned judges sitting on the Ohio Supreme Court were well aware of this proposition, we should construe the syllabus generously by replacing the ambiguous term "motivation behind" with the term "justification for" in order to make the syllabus unambiguously state the correct rule of federal law. So amended, the controlling proposition of federal law reads:</p>
<blockquote>"When the [justification for] a police officer's continued detention of a person stopped for a traffic violation is <span class="star-pagination">*50</span> not related to the purpose of the original, constitutional stop, and when that continued detention is not based on any articulable facts giving rise to a suspicion of some separate illegal activity justifying an extension of the detention, the continued detention constitutes an illegal seizure." <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#650" aria-description="Citation for case: State v. Robinette">73 Ohio St. 3d, at 650</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#696" aria-description="Citation for case: State v. Robinette">653 N. E. 2d, at 696</a></span>.</blockquote>
<p>Notwithstanding that the subjective motivation for the officer's decision to stop respondent related to drug interdiction, the legality of the stop depended entirely on the fact that respondent was speeding. Of course, "[a]s a general matter, the decision to stop an automobile is reasonable where the police have probable cause to believe that a traffic violation has occurred." <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#810" aria-description="Citation for case: Whren v. United States">517 U. S. 806, 810</a></span> (1996). As noted above, however, by the time Robinette was asked for consent to search his automobile, the lawful traffic stop had come to an end; Robinette had been given his warning, and the speeding violation provided no further justification for detention. The continued detention was therefore only justifiable, if at all, on some other grounds.<sup>[8]</sup></p>
<p>At no time prior to the search of respondent's vehicle did any articulable facts give rise to a reasonable suspicion of some separate illegal activity that would justify further detention. See <i>United States</i> v. <i>Sharpe,</i> <span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#682" aria-description="Citation for case: United States v. Sharpe">470 U. S. 675, 682</a></span> (1985); <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span>, 881 882 (1975); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 21</a></span> (1968). As an objective matter, it inexorably follows that when the officer had completed his task of either arresting or reprimanding the driver of the speeding car, his continued detention of that <span class="star-pagination">*51</span> person constituted an illegal seizure. This holding by the Ohio Supreme Court is entirely consistent with federal law.<sup>[9]</sup></p>
<p>The proper disposition follows as an application of wellsettled law. We held in <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U. S. 491</a></span> (1983), that a consent obtained during an illegal detention is ordinarily ineffective to justify an otherwise invalid search.<sup>[10]</sup> See also <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#433" aria-description="Citation for case: Florida v. Bostick">501 U. S., at 433-434</a></span> (noting that if consent was given during the course of an unlawful seizure, the results of the search "must be suppressed as tainted fruit"); <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#218" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 218-219</a></span> (1979); <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#601" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590, 601-602</a></span> (1975). Cf. <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963). Because Robinette's consent to the search was the product of an unlawful detention, "the consent was tainted by the illegality and was ineffective to justify the search." <i><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span>,</i> 460 U. S., at 507 508 (plurality opinion). I would therefore affirm the judgment below.</p>
<p></p>
<h2>II</h2>
<p>A point correctly raised by Justice Ginsburg merits emphasis. The Court's opinion today does not address either the wisdom of the rule announced in the second syllabus preceding <span class="star-pagination">*52</span> the Ohio Supreme Court's opinion or the validity of that rule as a matter of Ohio law. Nevertheless the risk that the narrowness of the Court's holding may not be fully understood prompts these additional words.</p>
<p>There is no rule of federal law that precludes Ohio from requiring its police officers to give its citizens warnings that will help them to understand whether a valid traffic stop has come to an end, and will help judges to decide whether a reasonable person would have felt free to leave under the circumstances at issue in any given case.<sup>[11]</sup> Nor, as I have previously observed, is there anything "in the Federal Constitution that prohibits a State from giving lawmaking power to its courts." <i>Minnesota</i> v. <i>Clover Leaf Creamery Co.,</i> <span class="citation" data-id="9428137"><a href="/opinion/110380/minnesota-v-clover-leaf-creamery-co/#479" aria-description="Citation for case: Minnesota v. Clover Leaf Creamery Co.">449 U. S. 456, 479</a></span>, and n. 3 (1981) (dissenting opinion). Thus, as far as we are concerned, whether Ohio acts through one branch of its government or another, it has the same power to enforce a warning rule as other States that may adopt such rules by executive action.<sup>[12]</sup></p>
<p><span class="star-pagination">*53</span> Moreover, while I recognize that warning rules provide benefits to the law enforcement profession and the courts, as well as to the public, I agree that it is not our function to pass judgment on the wisdom of such rules. Accordingly, while I have concluded that the judgment of the Supreme Court of Ohio should be affirmed, and thus dissent from this Court's disposition of the case, I am in full accord with its conclusion that the Federal Constitution neither mandates nor prohibits the warnings prescribed by the Ohio Court. Whether such a practice should be followed in Ohio is a matter for Ohio lawmakers to decide.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the State of Alabama et al. by <i>Betty D. Montgomery,</i> Attorney General of Ohio<i>, Jeffrey S. Sutton,</i> State Solicitor, and <i>Simon B. Karas,</i> and by the Attorneys General for their respective States as follows: <i>Jeff Sessions</i> of Alabama, <i>Daniel E. Lungren</i> of California, <i>Gale A. Norton</i> of Colorado, <i>M. Jane Brady</i> of Delaware, <i>Robert Butterworth</i> of Florida, <i>Margery S. Bronster</i>  of Hawaii, <i>Alan G. Lance</i> of Idaho, <i>Jim Ryan</i> of Illinois, <i>Carla J. Stovall</i>  of Kansas, <i>A. B. Chandler III</i> of Kentucky, <i>Richard P. Ieyoub</i> of Louisiana, <i>Andrew Ketterer</i> of Maine, <i>J. Joseph Curran, Jr.,</i> of Maryland, <i>Scott Harshbarger</i> of Massachusetts, <i>Frank J. Kelley</i> of Michigan, <i>Hubert H. Humphrey III</i> of Minnesota, <i>Mike Moore</i> of Mississippi, <i>Joseph P. Mazurek</i> of Montana, <i>Don Stenberg</i> of Nebraska, <i>Frankie Sue Del Papa</i>  of Nevada, <i>Jeffrey R. Howard</i> of New Hampshire, <i>Deborah T. Poritz</i> of New Jersey, <i>Dennis C. Vacco</i> of New York, <i>Michael F. Easley</i> of North Carolina, <i>W. A. Drew Edmondson</i> of Oklahoma, <i>Theodore Kulongoski</i> of Oregon, <i>Thomas W. Corbett, Jr.,</i> of Pennsylvania, <i>Jeffrey B. Pine</i> of Rhode Island, <i>Mark Bennett</i> of South Dakota, <i>Charles W. Bursen</i> of Tennessee, <i>Dan Morales</i> of Texas, <i>Jeffrey L. Amestoy</i> of Vermont, <i>James S. Gilmore III</i> of Virginia, <i>Darrell V. McGraw, Jr.,</i> of West Virginia, <i>James E. Doyle</i>  of Wisconsin, and <i>William U. Hill</i> of Wyoming; and for Americans for Effective Law Enforcement, Inc., by <i>Fred E. Inbau, Wayne W. Schmidt, James P. Manak,</i> and <i>Bernard J. Farber.</i>
</p>
<p><i>Tracey Maclin, Steven R. Shapiro,</i> and <i>Jeffrey M. Gamso</i> filed a brief for the American Civil Liberties Union et al. as <i>amici curiae</i> urging affirmance.</p>
<p>Briefs of <i>amicus curiae</i> were filed for the National Association of Criminal Defense Lawyers by <i>Sheryl Gordon McCloud;</i> and for the Ohio Association of Criminal Defense Lawyers by <i>W. Andrew Hasselbach.</i> </p>
<p>[*]   Respondent and his <i>amici</i> ask us to take this opportunity to depart from <i>Michigan</i> v. <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i><i>.</i> We are no more persuaded by this argument now than we were two Terms ago, see <i>Arizona</i> v.<span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/" aria-description="Citation for case: Arizona v. Evans"><i>Evans,</i></a></span> 514 U. S.1 (1995), and we again reaffirm the <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i> presumption.</p>
<p>[*]   Formerly, the Ohio Supreme Court was "reluctant to use the Ohio Constitution to extend greater protection to the rights and civil libertiesof Ohio citizens" and had usually not taken advantage of opportunities to "us[e] the Ohio Constitution as an independent source of constitutional rights." <i>Arnold</i> v.<i>Cleveland,</i> <span class="citation" data-id="6768465"><a href="/opinion/6876050/arnold-v-city-of-cleveland/#42" aria-description="Citation for case: Arnold v. City of Cleveland">67 Ohio St. 3d 35, 42,n. 8</a></span>,<span class="citation" data-id="6768465"><a href="/opinion/6876050/arnold-v-city-of-cleveland/#168" aria-description="Citation for case: Arnold v. City of Cleveland">616 N. E. 2d 163, 168, n. 8</a></span> (1993). Recently, however, the state high court declared: "The Ohio Constitution is a document of independent force. .. .As long as state courts provide at least as much protection as the United States Supreme Court has provided in its interpretation of the federal Bill of Rights, state courts are unrestricted in according greater civil liberties and protections to individuals and groups." <span class="citation" data-id="6768465"><a href="/opinion/6876050/arnold-v-city-of-cleveland/#35" aria-description="Citation for case: Arnold v. City of Cleveland"><i>Id.,</i> at 35</a></span>, <span class="citation" data-id="6768465"><a href="/opinion/6876050/arnold-v-city-of-cleveland/#164" aria-description="Citation for case: Arnold v. City of Cleveland">616 N. E. 2d, at 164</a></span> (syllabus).</p>
<p>[1]  "Whether the Fourth Amendment to the United States Constitution requires police officers to inform motorists, lawfully stopped for traffic violations, that the legal detention has concluded before any subsequent interrogation or search will be found to be consensual?" Pet. for Cert. i.</p>
<p>[2]  This is in part because crucial portions of the exchange were videotaped; this recording is a part of the record.</p>
<p>[3]  See <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#654" aria-description="Citation for case: State v. Robinette">73 Ohio St. 3d 650, 654</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#698" aria-description="Citation for case: State v. Robinette">653 N. E. 2d 695, 698</a></span> (1995).</p>
<p>[4]  A learned commentator has expressed agreement on this point.See 4 W. LaFave, Search and Seizure § 9.3(a),p.112 (3ded. 1996 and Supp. 1997) ("Given the fact that [defendant] quite clearly had been seized when his car was pulled over, the return of the credentials hardly manifests a change in status when it was immediately followed by interrogation concerning other criminal activity");see also <i>ibid.</i> (approving of Ohio Supreme Court's analysisin this case). We have indicated as much ourselves in the past. See <i>Berkemer</i> v.<i>McCarty,</i> 468U. S.420, 436(1984) ("Certainly few motorists would feel free either to disobey a directive to pullover or to leave the scene of a traffic stop without being told they might do so").</p>
<p>[5]  Though this search does not appear to have been particularly intrusive, that may not always be so. See Brief for American Civil Liberties Union et al. as <i>Amici Curiae</i> 28-29. Indeed, our holding in <i>Florida</i> v. <i>Jimeno,</i>  <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">500 U. S. 248</a></span> (1991), allowing police to open closed containers in the context of an automobile consent search where the "consent would reasonably be understood to extend to a particular container," <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#252" aria-description="Citation for case: Florida v. Jimeno"><i>id.,</i> at 252</a></span>, ensures that many motorists will wind up "consenting" to a far broader search than they might have imagined. See <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#254" aria-description="Citation for case: Florida v. Jimeno"><i>id.,</i> at 254-255</a></span> ("only objection that the police could have to" a rule requiring police to seek consent to search containers as well as the automobile itself "is that it would prevent them from exploiting the ignorance of a citizen who simply did not anticipate that his consent to search the car would be understood to authorize the police to rummage through his packages") (Marshall, J., dissenting).</p>
<p>[6]  It is ordinarily the syllabus that precedes an Ohio Supreme Court opinion, rather than the opinion itself, that states the law of the case. <i>Cassidy</i>  v. <i>Glossip,</i> <span class="citation" data-id="6753896"><a href="/opinion/6864181/cassidy-v-glossip/#24" aria-description="Citation for case: Cassidy v. Glossip">12 Ohio St. 2d 17, 24</a></span>, <span class="citation" data-id="6753896"><a href="/opinion/6864181/cassidy-v-glossip/#68" aria-description="Citation for case: Cassidy v. Glossip">231 N. E. 2d 64, 68</a></span> (1967); see <i>Migra</i> v. <i>Warren City School Dist. Bd. of Ed.,</i> <span class="citation" data-id="9429481"><a href="/opinion/111093/migra-v-warren-city-school-district-board-of-education/#86" aria-description="Citation for case: Migra v. Warren City School District Board of Education">465 U. S. 75, 86, n. 8</a></span> (1984); <i>Ohio</i> v. <i>Gallagher,</i> <span class="citation" data-id="9426357"><a href="/opinion/109424/ohio-v-gallagher/#259" aria-description="Citation for case: Ohio v. Gallagher">425 U. S. 257, 259</a></span> (1976).</p>
<p>[7]  Indeed, the first paragraph of the Ohio Supreme Court's opinion clearly indicates that the bright-line rule was meant to apply only in <i>future</i> cases. The Ohio Supreme Court first explained:"We find that the search was invalid since it was the product of an unlawful seizure."<span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#652" aria-description="Citation for case: State v. Robinette">73 Ohio St.3d, at 652</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#697" aria-description="Citation for case: State v. Robinette">653 N. E. 2d, at 697</a></span>.Only then did the court proceed to point out that it would "also use this case to establish a bright-line test . . . ."<i><span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/" aria-description="Citation for case: State v. Robinette">Ibid.</a></span></i> </p>
<p>[8]  Cf. <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 500</a></span> (1983) (plurality opinion) ("[A]n investigative detention must be temporary and last no longer than is necessary to effectuate the purpose of the stop"); <i>United States</i> v. <i>BrignoniPonce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 881</a></span> (1975) ("stop and inquiry must be `reasonably related in scope to the justification for their initiation' " (quoting <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 29</a></span> (1968)).</p>
<p>[9]  Since "this Court reviews judgments, not opinions," <i>Chevron U. S. A. Inc.</i> v. <i>Natural Resources Defense Council, Inc.,</i> <span class="citation" data-id="111221"><a href="/opinion/111221/chevron-u-s-a-inc-v-natural-resources-defense-council-inc/#842" aria-description="Citation for case: Chevron U. S. A. Inc. v. Natural Resources Defense...">467 U. S. 837, 842</a></span> (1984), the Ohio Supreme Court's holding that Robinette's continued seizure was illegal on these grounds provides a sufficient basis for affirming its judgment.</p>
<p>[10]  Writing for a plurality of the Court, Justice White explained that "statements given during a period of illegal detention are inadmissible even though voluntarily given if they are the product of the illegal detention and not the result of an independent act of free will." <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#501" aria-description="Citation for case: Florida v. Royer">460 U. S., at 501</a></span>. The defendant in <i><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span></i> had been "illegally detained when he consented to the search." <i><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Id.</a></span></i> , at 507. As a result, the plurality agreed that "the consent was tainted by the illegality and was ineffective to justify the search." <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#507" aria-description="Citation for case: Florida v. Royer"><i>Id.,</i> at 507-508</a></span>. Concurring in the result, Justice Brennan agreed with this much of the plurality's decision, diverging on other grounds. See <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#509" aria-description="Citation for case: Florida v. Royer"><i>id.,</i> at 509</a></span>. Justice Brennan's agreement on that narrow principle represents the holding of the Court. See <i>Marks</i> v. <i>United States,</i> <span class="citation" data-id="9004890"><a href="/opinion/9011945/marks-v-united-states/#193" aria-description="Citation for case: Marks v. United States">430 U. S. 188, 193</a></span> (1977).</p>
<p>[11]  Indeed, we indicated in <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#437" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429, 437</a></span> (1991), that the fact a defendant had been explicitly advised that he could refuse to give consent was relevant to the question whether he was seized at the time consent was sought. And, in other cases, we have stressed the importance of similar advice as a circumstance supporting the conclusion that a consent to search was voluntary. See <i>Schneckloth</i> v. <i>Bustamonte,</i>  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#227" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 227</a></span> (1973); <i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544</a></span>, 558 559 (1980). Cf. <i>Washington</i> v. <i>Chrisman,</i> <span class="citation" data-id="9428641"><a href="/opinion/110636/washington-v-chrisman/#9" aria-description="Citation for case: Washington v. Chrisman">455 U. S. 1, 9</a></span> (1982) (consent to search was voluntary where defendant "consented, in writing, . . . after being advised that his consent must be voluntary and that he had an absolute right to refuse consent").</p>
<p>[12]  As we are informed by a brief <i>amicus curiae</i> filed by Americans For Effective Law Enforcement, Inc.: "Such a warning may be good police practice, and indeed <i>amicus</i> knows that many law enforcement agencies among our constituents have routinely incorporated a warning into their Fourth Amendment consent forms that they use in the field, but it is precisely thata <i>practice</i> and <i>not a constitutional imperative.</i> An officer who includes such a warning in his request for consent undoubtedly presents a stronger case for a finding of voluntariness in a suppression hearing, and we would not suggest that such agencies and officers do otherwise. We know, too, that instructors in many police training programs of leading universities and management institutes routinely recommend such warnings as a sound practice, likely to bolster the voluntariness of a consent to search. [We ourselves] conduc[t] law enforcement training programs at the national level and many of our own speakers have made this very point." Brief for Americans For Effective Law Enforcement, Inc., as <i>Amicus Curiae</i> 7.</p>

</div>
```

---

## GROUP: content/cases/Oregon v. Bradshaw.md  (`case`, 5 assertions)

### content_page

```
---
title: "Oregon v. Bradshaw"
type: case
citation: "462 U.S. 1039 (1983)"
parallel_cite: "103 S. Ct. 2830; 77 L. Ed. 2d 405; 51 U.S.L.W. 4940"
neutral_cite: 1983 U.S. LEXIS 82
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-06-23
docket: 81-1857
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1983-06-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Oregon v. Bradshaw
  varies_by_point: false
  scope_note: "Plurality; the two-step Edwards initiation/waiver framework it states is settled and good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110987/oregon-v-bradshaw/"
  cluster_id: 110987
  opinion_id: 9429286
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny"
related: ["[[Edwards v. Arizona]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "invocation", "edwards", "initiation"]
holding: "After invoking counsel, a suspect 'initiates' further communication under Edwards only by a statement evincing a desire to open a generalized discussion about the investigation (not a routine request); even then, any resulting statement is admissible only if the suspect also validly waived counsel under the totality of the circumstances."
lake:
  record_id: Oregon v. Bradshaw
  status: verified
  projected_at: 2026-07-06
---

# Oregon v. Bradshaw

*462 U.S. 1039 (1983)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After being arrested and given [[Miranda and Custodial Interrogation|Miranda warnings]], Bradshaw invoked his right to counsel and questioning stopped. Sometime later, while being transferred, he asked an officer, "Well, what is going to happen to me now?" The officer reminded him he need not talk, and a conversation followed; Bradshaw later took a polygraph and made incriminating statements. The issue was whether *Bradshaw* — not the police — had reopened communication under *[[Edwards v. Arizona]]*.

## Issue
After a suspect invokes the right to counsel, what does it mean for the suspect to "initiate" further communication so that interrogation may resume — and what else must the State show before the resulting statements are admissible?

## Rule
*[[Edwards v. Arizona|Edwards]]* bars further interrogation after an invocation of counsel unless the accused himself "initiates" further communication. A routine inquiry does not count: "There are some inquiries, such as a request for a drink of water or a request to use a telephone, that are so routine that they cannot be fairly said to represent a desire on the part of an accused to open up a more generalized discussion relating directly or indirectly to the investigation." — 462 U.S. at 1045 (plurality opinion). ^pin-1045

Initiation requires a statement that "evinced a willingness and a desire for a generalized discussion about the investigation." — *Id.* at 1045–46. ^pin-1046

Initiation is only the **first** step: the second is whether, under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], the accused then knowingly and intelligently waived the right to counsel he had previously invoked.

## Application
Bradshaw's question — "Well, what is going to happen to me now?" — was not a routine request about the mechanics of custody; it evinced a desire to discuss the investigation, so it "initiated" further communication. With that step satisfied, the plurality concluded that on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] Bradshaw thereafter validly waived his right to counsel, so the later statements were admissible.

## Conclusion
Bradshaw initiated the renewed dialogue and validly waived counsel; the statements were admissible. The Oregon Court of Appeals' suppression was reversed. *Bradshaw* fixes the two-step *[[Edwards v. Arizona|Edwards]]* analysis: (1) did the accused initiate? (2) was there a valid waiver under the totality?

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Although a plurality, the two-step initiation-then-waiver framework stated here is the settled application of [[Edwards v. Arizona]] and remains good law.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny*

## Sources
- *Oregon v. Bradshaw*, 462 U.S. 1039 (1983) — https://www.courtlistener.com/opinion/110987/oregon-v-bradshaw/ — pinpoints: 1045, 1046 (plurality opinion).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "02ab6ccd5e2f558c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "462 U.S. 1039 (1983)", "court": "U.S. Supreme Court", "neutral_cite": "1983 U.S. LEXIS 82", "official_citation_present": true, "parallel_cite": "103 S. Ct. 2830; 77 L. Ed. 2d 405; 51 U.S.L.W. 4940", "title": "Oregon v. Bradshaw", "year": "1983"}}
{"assertion_id": "861df3c8e7bd5c74", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "After invoking counsel, a suspect 'initiates' further communication under Edwards only by a statement evincing a desire to open a generalized discussion about the investigation (not a routine request); even then, any resulting statement is admissible only if the suspect also validly waived counsel under the totality of the circumstances.", "title": "Oregon v. Bradshaw"}}
{"assertion_id": "9a384204515ca8a3", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Progeny", "title": "Oregon v. Bradshaw"}}
{"assertion_id": "04867cf1db056174", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Oregon v. Bradshaw"}}
{"assertion_id": "8ed9573cd27c1de4", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1983-06-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Oregon v. Bradshaw", "field_i_validity": "good_law", "scope_note": "Plurality; the two-step Edwards initiation/waiver framework it states is settled and good law.", "title": "Oregon v. Bradshaw", "varies_by_point": "false"}}
```

### lake record — Oregon v. Bradshaw

```json
{
  "schema_version": "s2.v1",
  "record_id": "Oregon v. Bradshaw",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Oregon v. Bradshaw",
    "case_name_short": "Bradshaw",
    "case_name_full": "Oregon v. Bradshaw",
    "input_case_name": "Oregon v. Bradshaw",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-06-23",
    "year": 1983,
    "docket": "81-1857",
    "cluster_id": 110987,
    "lead_opinion_id": 9429286,
    "sibling_ids": [
      110987,
      9429286,
      9429287,
      9429288
    ],
    "absolute_url": "/opinion/110987/oregon-v-bradshaw/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "462 U.S. 1039",
      "volume": "462",
      "reporter": "U.S.",
      "page": "1039",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 2830",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2830",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 2d 405",
        "volume": "77",
        "reporter": "L. Ed. 2d",
        "page": "405",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4940",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4940",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 82",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "82",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "462 U.S. 1039",
        "volume": "462",
        "reporter": "U.S.",
        "page": "1039",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 2830",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2830",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 2d 405",
        "volume": "77",
        "reporter": "L. Ed. 2d",
        "page": "405",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 82",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "82",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4940",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4940",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "462 U.S. 1039",
    "official_selection": {
      "court_class": "scotus",
      "selected": "462 U.S. 1039",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1045",
      "page": null,
      "quote": "further communication so that interrogation may resume \u2014 and what else must the State show before the resulting statements are admissible? ## Rule *Edwards* bars further interrogation after an invocation of counsel unless the accused himself",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1046",
      "page": null,
      "quote": "evinced a willingness and a desire for a generalized discussion about the investigation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1983-06-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Oregon v. Bradshaw",
    "varies_by_point": false,
    "scope_note": "Plurality; the two-step Edwards initiation/waiver framework it states is settled and good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Gonzalez",
          "cluster_id": 4892536,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Colon",
          "cluster_id": 4671866,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rowland v. State",
          "cluster_id": 10367127,
          "cite": [
            "306 Ga. 59"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Boyd",
          "cluster_id": 4259208,
          "cite": [
            "360 Or. 302",
            "380 P.3d 941",
            "2016 Ore. LEXIS 612"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth, Aplt v. Hill, E.",
          "cluster_id": 2754405,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Letkowski",
          "cluster_id": 6589954,
          "cite": [
            "83 Mass. App. Ct. 847",
            "991 N.E.2d 1106",
            "2013 WL 3242668",
            "2013 Mass. App. LEXIS 114"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gonzalez",
          "cluster_id": 2319916,
          "cite": [
            "25 A.3d 648",
            "302 Conn. 287",
            "2011 Conn. LEXIS 355",
            "2011 WL 3802478"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pecina v. State",
          "cluster_id": 2292956,
          "cite": [
            "326 S.W.3d 249",
            "2010 Tex. App. LEXIS 5631",
            "2010 WL 2825663"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Martinez v. State",
          "cluster_id": 1450662,
          "cite": [
            "275 S.W.3d 29",
            "2008 WL 2840151"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
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
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moran v. Burbine",
          "cluster_id": 111614,
          "cite": [
            "89 L. Ed. 2d 410",
            "106 S. Ct. 1135",
            "475 U.S. 412",
            "1986 U.S. LEXIS 32",
            "54 U.S.L.W. 4265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
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
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Jackson",
          "cluster_id": 111622,
          "cite": [
            "89 L. Ed. 2d 631",
            "106 S. Ct. 1404",
            "475 U.S. 625",
            "1986 U.S. LEXIS 91",
            "54 U.S.L.W. 4334"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Illinois",
          "cluster_id": 111288,
          "cite": [
            "83 L. Ed. 2d 488",
            "105 S. Ct. 490",
            "469 U.S. 91",
            "1984 U.S. LEXIS 167",
            "53 U.S.L.W. 3430"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Waidla",
          "cluster_id": 1316339,
          "cite": [
            "996 P.2d 46",
            "94 Cal. Rptr. 2d 396",
            "22 Cal. 4th 690",
            "22 Cal. 690",
            "2000 Daily Journal DAR 3605",
            "2000 Cal. Daily Op. Serv. 2687",
            "2000 Cal. LEXIS 2229"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Roberson",
          "cluster_id": 112100,
          "cite": [
            "100 L. Ed. 2d 704",
            "108 S. Ct. 2093",
            "486 U.S. 675",
            "1988 U.S. LEXIS 2726",
            "56 U.S.L.W. 4590"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnick v. Mississippi",
          "cluster_id": 112513,
          "cite": [
            "112 L. Ed. 2d 489",
            "111 S. Ct. 486",
            "498 U.S. 146",
            "1990 U.S. LEXIS 6118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradford",
          "cluster_id": 1239150,
          "cite": [
            "15 Cal. 4th 1229",
            "939 P.2d 259",
            "97 Daily Journal DAR 9003",
            "97 Cal. Daily Op. Serv. 5537",
            "65 Cal. Rptr. 2d 145",
            "1997 Cal. LEXIS 3699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Harvey",
          "cluster_id": 112385,
          "cite": [
            "108 L. Ed. 2d 293",
            "110 S. Ct. 1176",
            "494 U.S. 344",
            "1990 U.S. LEXIS 1229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neal v. State",
          "cluster_id": 1869722,
          "cite": [
            "451 So. 2d 743"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Shatzer",
          "cluster_id": 1734,
          "cite": [
            "175 L. Ed. 2d 1045",
            "130 S. Ct. 1213",
            "559 U.S. 98",
            "2010 U.S. LEXIS 1899"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Solem v. Stumes",
          "cluster_id": 111112,
          "cite": [
            "79 L. Ed. 2d 579",
            "104 S. Ct. 1338",
            "465 U.S. 638",
            "1984 U.S. LEXIS 36",
            "52 U.S.L.W. 4307"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Connecticut v. Barrett",
          "cluster_id": 111796,
          "cite": [
            "93 L. Ed. 2d 920",
            "107 S. Ct. 828",
            "479 U.S. 523",
            "1987 U.S. LEXIS 419",
            "55 U.S.L.W. 4151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Memro",
          "cluster_id": 1375029,
          "cite": [
            "905 P.2d 1305",
            "11 Cal. 4th 786",
            "47 Cal. Rptr. 2d 219",
            "95 Daily Journal DAR 15919",
            "95 Cal. Daily Op. Serv. 9091",
            "1995 Cal. LEXIS 6793"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mickey",
          "cluster_id": 1226896,
          "cite": [
            "818 P.2d 84",
            "54 Cal. 3d 612",
            "286 Cal. Rptr. 801",
            "91 Daily Journal DAR 13544",
            "91 Cal. Daily Op. Serv. 8732",
            "1991 Cal. LEXIS 4664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. State",
          "cluster_id": 2382336,
          "cite": [
            "504 A.2d 1096",
            "1986 Del. LEXIS 1040"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Powell",
          "cluster_id": 2690788,
          "cite": [
            "2012 Ohio 2577",
            "132 Ohio St. 3d 233"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradford",
          "cluster_id": 1407706,
          "cite": [
            "14 Cal. 4th 1005",
            "929 P.2d 544",
            "97 Daily Journal DAR 899",
            "97 Cal. Daily Op. Serv. 520",
            "60 Cal. Rptr. 2d 225",
            "1997 Cal. LEXIS 9"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Marshall",
          "cluster_id": 1425683,
          "cite": [
            "790 P.2d 676",
            "50 Cal. 3d 907",
            "269 Cal. Rptr. 269",
            "1990 Cal. LEXIS 1959"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Davis",
          "cluster_id": 1801680,
          "cite": [
            "46 Cal. 4th 539",
            "208 P.3d 78",
            "94 Cal. Rptr. 3d 322",
            "2009 Cal. LEXIS 4707"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jones",
          "cluster_id": 2689817,
          "cite": [
            "2000 Ohio 187",
            "90 Ohio St. 3d 403",
            "739 N.E.2d 300"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Etheridge v. State",
          "cluster_id": 2372478,
          "cite": [
            "903 S.W.2d 1",
            "1994 Tex. Crim. App. LEXIS 83",
            "1994 WL 273325"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Green",
          "cluster_id": 1730571,
          "cite": [
            "655 So. 2d 272",
            "1995 WL 312446"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cruz",
          "cluster_id": 2584939,
          "cite": [
            "44 Cal. 4th 636",
            "187 P.3d 970",
            "80 Cal. Rptr. 3d 126",
            "2008 Cal. LEXIS 9079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110987 OR 9429286 OR 9429287 OR 9429288) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjE2NzcxMjAwMDAwJnM9Mjg3OTQ0MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110987+OR+9429286+OR+9429287+OR+9429288%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110987 OR 9429286 OR 9429287 OR 9429288)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTEmcz0xNTIwMzA5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110987+OR+9429286+OR+9429287+OR+9429288%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110987 OR 9429286 OR 9429287 OR 9429288)",
        "reviewed": 28,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 28,
        "triage_read": 0,
        "triage_snippet_classified": 28
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110987 OR 9429286 OR 9429287 OR 9429288)",
    "indexed_citing_opinions": 824,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110987,
        "count": 732,
        "count_source": "search"
      },
      {
        "opinion_id": 9429286,
        "count": 101,
        "count_source": "search"
      },
      {
        "opinion_id": 9429287,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429288,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1351,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/oregon-v-bradshaw.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1NzE5ODQmcz05NDUwOTMxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110987+OR+9429286+OR+9429287+OR+9429288%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110987,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 110065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 110809,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 392817,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 403900,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 406019,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 409288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 1115589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 1159238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 1356056,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 1363682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 1385367,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 1767568,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 1771028,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 1962224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 2075223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 2144643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 2280262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 2362374,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 2385822,
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
    "date_created": "2026-07-05T16:16:17Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:16:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:16:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:20:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:16:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Oregon v. Bradshaw

```
<opinion type="majority">
<author id="b1086-11">Justice Rehnquist</author>
<p id="AotR">announced the judgment of the Court and delivered an opinion, in which The Chief Justice, Justice White, and Justice O’Connor joined.</p>
<p id="b1086-12">After a bench trial in an Oregon trial court, respondent James Edward Bradshaw was convicted of the offenses of <page-number citation-index="1" label="1041">*1041</page-number>first-degree manslaughter, driving while under the influence of intoxicants, and driving while his license was revoked. The Oregon Court of Appeals reversed his conviction, holding that an inquiry he made of a police officer at the time he was in custody did not “initiate” a conversation with the officer, and that therefore statements by the respondent growing out of that conversation should have been excluded from evidence under <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981). We granted certiorari to review this determination. <span class="citation multiple-matches"><a href="/c/U.%20S./459/966/">459 U. S. 966</a></span> (1982).</p>
<p id="b1087-5">In September 1980, Oregon police were investigating the death of one Lowell Reynolds in Tillamook County. Reynolds’ body had been found in his wrecked pickup truck, in which he appeared to have been a passenger at the time the vehicle left the roadway, struck a tree and an embankment, and finally came to rest on its side in a shallow creek. Reynolds had died from traumatic injury, coupled with asphyxia by drowning. During the investigation of Reynolds’ death, respondent was asked to accompany a police officer to the Rockaway Police Station for questioning.</p>
<p id="b1087-6">Once at the station, respondent was advised of his rights as required by <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Respondent then repeated to the police his earlier account of the events of the evening of Reynolds’ death, admitting that he had provided Reynolds and others with liquor for a party at Reynolds’ house, but denying involvement in the traffic accident that apparently killed Reynolds. Respondent suggested that Reynolds might have met with foul play at the hands of the assailant whom respondent alleged had struck him at the party.</p>
<p id="b1087-7">At this point, respondent was placed under arrest for furnishing liquor to Reynolds, a minor, and again advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. A police officer then told respondent the officer’s theory of how the traffic accident that killed Reynolds occurred; a theory which placed respondent behind the wheel of the vehicle. Respondent again denied his involvement, and said “I do want an attorney before it goes very <page-number citation-index="1" label="1042">*1042</page-number>much further.” App. 72. The officer immediately terminated the conversation.</p>
<p id="b1088-5">Sometime later respondent was transferred from the Rock-away Police Station to the Tillamook County Jail, a distance of some 10 or 15 miles. Either just before, or during, his trip from Rockaway to Tillamook, respondent inquired of a police officer, “Well, what is going to happen to me now?” The officer answered by saying: “You do not have to talk to me. You have requested an attorney and I don’t want you talking to me unless you so desire because anything you say — because—since you have requested an attorney, you know, it has to be at your own free will.” <em>Id., </em>at 16. See <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/#951" aria-description="Citation for case: State v. Bradshaw">54 Ore. App. 949, 951</a></span>, <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/#1011" aria-description="Citation for case: State v. Bradshaw">636 P. 2d 1011, 1011-1012</a></span> (1981). Respondent said he understood. There followed a discussion between respondent and the officer concerning where respondent was being taken and the offense with which he would be charged. The officer suggested that respondent might help himself by taking a polygraph examination. Respondent agreed to take such an examination, saying that he was willing to do whatever he could to clear up the matter.</p>
<p id="b1088-6">The next day, following another reading to respondent of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, and respondent’s signing a written waiver of those rights, the polygraph was administered. At its conclusion, the examiner told respondent that he did not believe respondent was telling the truth. Respondent then recanted his earlier story, admitting that he had been at the wheel of the vehicle in which Reynolds was killed, that he had consumed a considerable amount of alcohol, and that he had passed out at the wheel before the vehicle left the roadway and came to rest in the creek.</p>
<p id="b1088-7">Respondent was charged with first-degree manslaughter, driving while under the influence of intoxicants, and driving while his license was revoked. His motion to suppress the statements described above was denied, and he was found guilty after a bench trial. The Oregon Court of Appeals, relying on our decision in <em>Edwards </em>v. <em>Arizona, supra, </em>re<page-number citation-index="1" label="1043">*1043</page-number>versed, concluding that the statements had been obtained in violation of respondent’s Fifth Amendment rights. <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/" aria-description="Citation for case: State v. Bradshaw">54 Ore. App. 949</a></span>, <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/" aria-description="Citation for case: State v. Bradshaw">636 P. 2d 1011</a></span> (1981). We now conclude that the Oregon Court of Appeals misapplied our decision in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>.</em></p>
<p id="b1089-5">In <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>the defendant had voluntarily submitted to questioning but later stated that he wished an attorney before the discussions continued. The following day detectives accosted the defendant in the county jail, and when he refused to speak with them he was told that “he had” to talk. We held that subsequent incriminating statements made without his attorney present violated the rights secured to the defendant by the Fifth and Fourteenth Amendments to the United States Constitution. In our opinion, we stated:</p>
<blockquote id="b1089-6">“[Although we have held that after initially being advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, the accused may himself validly waive his rights and respond to interrogation, see <em>North Carolina </em>v. <em>Butler, </em>[<span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#372" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369, 372-376</a></span> (1979)], the Court has strongly indicated that additional safeguards are necessary when the accused asks for counsel; and we now hold that when an accused has invoked his right to have counsel present during custodial interrogation, a valid waiver of that right cannot be established by showing only that he responded to further police-initiated custodial interrogation even if he has been advised of his rights. We further hold that <em>an accused, such as [the defendant], having expressed his desire to deal with the police only through counsel, is not subject to further interrogation by the authorities until counsel has been made available to him, unless the accused himself initiates further communication, exchanges, or conversations with the </em>police.” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484-485</a></span> (footnote omitted) (emphasis added).</blockquote>
<p id="b1089-7">Respondent’s question in the present case, “Well, what is going to happen to me now?”, admittedly was asked prior to <page-number citation-index="1" label="1044">*1044</page-number>respondent’s being “subjected] to further interrogation by the authorities.” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona"><em>Id., </em>at 484</a></span>. The Oregon Court of Appeals stated that it did not “construe defendant’s question about what was going to happen to him to have been a waiver of his right to counsel, invoked only minutes before. . ..” <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/#953" aria-description="Citation for case: State v. Bradshaw">54 Ore. App., at 953</a></span>, <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/#1013" aria-description="Citation for case: State v. Bradshaw">636 P. 2d, at 1013</a></span>. The Court of Appeals, after quoting relevant language from <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>, </em>concluded that “under the reasoning enunciated in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>, </em>defendant did not make a valid waiver of his Fifth Amendment rights, and his statements were inadmissible.” <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Ibid.</a></span></em></p>
<p id="b1090-5">We think the Oregon Court of Appeals misapprehended the test laid down in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>. </em>We did not there hold that the “initiation” of a conversation by a defendant such as respondent would amount to a waiver of a previously invoked right to counsel; we held that after the right to counsel had been asserted by an accused, further interrogation of the accused should not take place “unless the accused himself initiates further communication, exchanges, or conversations with the police.” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#485" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 485</a></span>. This was in effect a prophylactic rule, designed to protect an accused in police custody from being badgered by police officers in the manner in which the defendant in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>was. We recently restated the requirement in <em>Wyrick </em>v. <em>Fields, </em><span class="citation" data-id="9428961"><a href="/opinion/110809/wyrick-v-fields/#46" aria-description="Citation for case: Wyrick v. Fields">459 U. S. 42, 46</a></span> (1982) <em>(per curiam), </em>to be that before a suspect in custody can be subjected to further interrogation after he requests an attorney there must be a showing that the “suspect himself initiates dialogue with the authorities.”</p>
<p id="b1090-6">But even if a conversation taking place after the accused has “expressed his desire to deal with the police only through counsel,” is initiated by the accused, where reinterrogation follows, the burden remains upon the prosecution to show that subsequent events indicated a waiver of the Fifth Amendment right to have counsel present during the interrogation. This is made clear in the following footnote to our <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>opinion:</p>
<blockquote id="b1090-7">“If, as frequently would occur in the course of a meeting initiated by the accused, the conversation is not <page-number citation-index="1" label="1045">*1045</page-number>wholly one-sided, it is likely that the officers will say or do something that clearly would be ‘interrogation.’ In that event, the question would be whether a valid waiver of the right to counsel and the right to silence had occurred, that is, <em>whether the purported waiver was knowing and intelligent and found to be so under the totality of the circumstances, </em>including the necessary fact that the accused, not the police, reopened the dialogue with the authorities.” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#486" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 486, n. 9</a></span> (emphasis added).</blockquote>
<p id="b1091-5">This rule was reaffirmed earlier this Term in <em>Wyrick </em>v. <em><span class="citation" data-id="9428961"><a href="/opinion/110809/wyrick-v-fields/" aria-description="Citation for case: Wyrick v. Fields">Fields, supra.</a></span></em></p>
<p id="b1091-6">Thus, the Oregon Court of Appeals was wrong in thinking that an “initiation” of a conversation or discussion by an accused not only satisfied the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule, but <em>ex proprio vigore </em>sufficed to show a waiver of the previously asserted right to counsel. The inquiries are separate, and clarity of application is not gained by melding them together.</p>
<p id="b1091-7">There can be no doubt in this case that in asking, “Well, what is going to happen to me now?”, respondent “initiated” further conversation in the ordinary dictionary sense of that word. While we doubt that it would be desirable to build a superstructure of legal refinements around the word “initiate” in this context, there are undoubtedly situations where a bare inquiry by either a defendant or by a police officer should not be held to “initiate” any conversation or dialogue. There are some inquiries, such as a request for a drink of water or a request to use a telephone, that are so routine that they cannot be fairly said to represent a desire on the part of an accused to open up a more generalized discussion relating directly or indirectly to the investigation. Such inquiries or statements, by either an accused or a police officer, relating to routine incidents of the custodial relationship, will not generally “initiate” a conversation in the sense in which that word was used in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>.</em></p>
<p id="b1091-8">Although ambiguous, the respondent’s question in this case as to what was going to happen to him evinced a willingness <page-number citation-index="1" label="1046">*1046</page-number>and a desire for a generalized discussion about the investigation; it was not merely a necessary inquiry arising out of the incidents of the custodial relationship. It could reasonably have been interpreted by the officer as relating generally to the investigation. That the police officer so understood it is apparent from the fact that he immediately reminded the accused that “[y]ou do not have to talk to me,” and only after the accused told him that he “understood” did they have a generalized conversation. <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/#951" aria-description="Citation for case: State v. Bradshaw">54 Ore. App., at 951</a></span>, <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/#1011" aria-description="Citation for case: State v. Bradshaw">636 P. 2d, at 1011-1012</a></span>. On these facts we believe that there was not a violation of the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule.</p>
<p id="b1092-5">Since there was no violation of the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule in this case, the next inquiry was “whether a valid waiver of the right to counsel and the right to silence had occurred, that is, whether the purported waiver was knowing and intelligent and found to be so under the totality of the circumstances, including the necessary fact that the accused, not the police, reopened the dialogue with the authorities.” <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#486" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 486, n. 9</a></span>. As we have said many times before, this determination depends upon “‘the particular facts and circumstances surrounding [the] case, including the background, experience, and conduct of the accused.’” <em>North Carolina </em>v. <em>Butler, </em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#374" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369, 374-375</a></span> (1979) (quoting <em>Johnson </em>v. <em>Zerbst, </em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 464</a></span> (1938)). See also <em>Edwards </em>v. <em>Arizona, supra, </em>at 482-483.</p>
<p id="b1092-6">The state trial court made this inquiry and, in the words of the Oregon Court of Appeals, “found that the police made no threats, promises or inducements to talk, that defendant was properly advised of his rights and understood them and that within a short time after requesting an attorney he changed his mind without any impropriety on the part of the police. The court held that the statements made to the polygraph examiner were voluntary and the result of a knowing waiver of his right to remain silent.” <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/#952" aria-description="Citation for case: State v. Bradshaw">54 Ore. App., at 952</a></span>, <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/#1012" aria-description="Citation for case: State v. Bradshaw">636 P. 2d, at 1012</a></span>.</p>
<p id="b1092-7">We have no reason to dispute these conclusions, based as they are upon the trial court’s firsthand observation of the <page-number citation-index="1" label="1047">*1047</page-number>witnesses to the events involved. The judgment of the Oregon Court of Appeals is therefore reversed, and the cause is remanded for further proceedings.</p>
<p id="b1093-5">
<em>It is so ordered.</em>
</p>
</opinion>
```

---

## GROUP: content/cases/Oregon v. Mathiason.md  (`case`, 5 assertions)

### content_page

```
---
title: "Oregon v. Mathiason"
type: case
citation: "429 U.S. 492 (1977)"
parallel_cite: "97 S. Ct. 711; 50 L. Ed. 2d 714"
neutral_cite: 1977 U.S. LEXIS 38
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-01-25
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1977-01-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Oregon v. Mathiason
  varies_by_point: false
  scope_note: "Per curiam; voluntary station-house interview is not custody; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109587/oregon-v-mathiason/"
  cluster_id: 109587
  opinion_id: 109587
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[California v. Beheler]]", "[[Stansbury v. California]]", "[[Howes v. Fields]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "custody", "station-house"]
holding: "A suspect who comes voluntarily to the station, is told he is not under arrest, and is free to leave is NOT in custody for Miranda —…"
lake:
  record_id: Oregon v. Mathiason
  status: verified
  projected_at: 2026-07-06
---

# Oregon v. Mathiason

*429 U.S. 492 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A parolee, Mathiason, came voluntarily to a state police office after an officer left a note asking him to call. The officer told him he was not under arrest, falsely said that his fingerprints had been found at a burglary scene, and questioned him behind a closed door. Mathiason confessed and then left the office freely. ([[Common Legal Terms#per-curiam|Per curiam]].)

## Issue
Whether a suspect questioned at a police station — who came voluntarily, was told he was not under arrest, and was free to leave — is "in custody" for *[[Miranda v. Arizona|Miranda]]* purposes.

## Rule
*[[Miranda v. Arizona|Miranda]]* applies only to custodial interrogation; a station-house setting or a "coercive environment" does not by itself trigger it. "[P]olice officers are not required to administer *Miranda* warnings to everyone whom they question. Nor is the requirement of warnings to be imposed simply because the questioning takes place in the station house, or because the questioned person is one whom the police suspect." — 429 U.S. at 495. ^pin-495

"*Miranda* warnings are required only where there has been such a restriction on a person's freedom as to render him 'in custody.'" — *Id.* ^pin-495b

## Application
Mathiason came to the station voluntarily, was told he was not under arrest, was questioned briefly, and left without hindrance; he was therefore not in custody. The officer's false statement that fingerprints had been found did not convert the noncustodial interview into custodial interrogation. Because Mathiason was not in custody, no *[[Miranda v. Arizona|Miranda]]* warnings were required and his confession was admissible.

## Conclusion
Mathiason was not in custody; *[[Miranda v. Arizona|Miranda]]* did not apply and the confession was admissible. The Oregon Supreme Court's judgment was reversed. *([[Common Legal Terms#per-curiam|Per curiam]].)*

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Mathiason* applies [[Miranda v. Arizona]]'s custody threshold and was reaffirmed in [[California v. Beheler]]; the custody inquiry is objective ([[Stansbury v. California]]) and turns on a formal-arrest-or-equivalent restraint on freedom of movement ([[Howes v. Fields]]).

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Oregon v. Mathiason*, 429 U.S. 492 (1977) (per curiam) — https://www.courtlistener.com/opinion/109587/oregon-v-mathiason/ — pinpoint: 495.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4438f67352db7d54", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "429 U.S. 492 (1977)", "court": "U.S. Supreme Court", "neutral_cite": "1977 U.S. LEXIS 38", "official_citation_present": true, "parallel_cite": "97 S. Ct. 711; 50 L. Ed. 2d 714", "title": "Oregon v. Mathiason", "year": "1977"}}
{"assertion_id": "9b4dd9c72041512c", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A suspect who comes voluntarily to the station, is told he is not under arrest, and is free to leave is NOT in custody for Miranda —…", "title": "Oregon v. Mathiason"}}
{"assertion_id": "e7843f15776a9030", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Progeny / Refinement", "title": "Oregon v. Mathiason"}}
{"assertion_id": "6aa14eae079f183a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Oregon v. Mathiason"}}
{"assertion_id": "6ecc91c9dd591a75", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1977-01-25", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Oregon v. Mathiason", "field_i_validity": "good_law", "scope_note": "Per curiam; voluntary station-house interview is not custody; good law.", "title": "Oregon v. Mathiason", "varies_by_point": "false"}}
```

### lake record — Oregon v. Mathiason

```json
{
  "schema_version": "s2.v1",
  "record_id": "Oregon v. Mathiason",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Oregon v. Mathiason",
    "case_name_short": "Mathiason",
    "case_name_full": "Oregon v. Mathiason",
    "input_case_name": "Oregon v. Mathiason",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-01-25",
    "year": 1977,
    "docket": null,
    "cluster_id": 109587,
    "lead_opinion_id": 109587,
    "sibling_ids": [
      109587,
      9426651,
      9426652,
      9426653
    ],
    "absolute_url": "/opinion/109587/oregon-v-mathiason/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "429 U.S. 492",
      "volume": "429",
      "reporter": "U.S.",
      "page": "492",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "97 S. Ct. 711",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "711",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 L. Ed. 2d 714",
        "volume": "50",
        "reporter": "L. Ed. 2d",
        "page": "714",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 38",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "38",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "429 U.S. 492",
        "volume": "429",
        "reporter": "U.S.",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 711",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "711",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 L. Ed. 2d 714",
        "volume": "50",
        "reporter": "L. Ed. 2d",
        "page": "714",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 38",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "38",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "429 U.S. 492",
    "official_selection": {
      "court_class": "scotus",
      "selected": "429 U.S. 492",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-495",
      "page": null,
      "quote": "for *Miranda* purposes. ## Rule *Miranda* applies only to custodial interrogation; a station-house setting or a",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-495b",
      "page": null,
      "quote": "*Miranda* warnings are required only where there has been such a restriction on a person's freedom as to render him 'in custody.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1977-01-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Oregon v. Mathiason",
    "varies_by_point": false,
    "scope_note": "Per curiam; voluntary station-house interview is not custody; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Butler v. State",
          "cluster_id": 8244686,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Butler v. State",
          "cluster_id": 8242363,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Butler v. State",
          "cluster_id": 7861363,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Welch",
          "cluster_id": 4883662,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Barksdale",
          "cluster_id": 4867083,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Mattox",
          "cluster_id": 4478290,
          "cite": [
            "2018 Ohio 992",
            "108 N.E.3d 1139"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. MacDonald",
          "cluster_id": 5309859,
          "cite": [
            "2017 UT App 124",
            "402 P.3d 91",
            "844 Utah Adv. Rep. 90",
            "2017 WL 3224516",
            "2017 Utah App. LEXIS 124"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Soto",
          "cluster_id": 4401346,
          "cite": [
            "2017 Ohio 4348",
            "93 N.E.3d 204"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Parlier",
          "cluster_id": 4373268,
          "cite": [
            "797 S.E.2d 340",
            "2017 WL 899978",
            "2017 N.C. App. LEXIS 136"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Portillo",
          "cluster_id": 3210008,
          "cite": [
            "787 S.E.2d 822",
            "247 N.C. App. 834",
            "2016 N.C. App. LEXIS 619"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Manson v. Brathwaite",
          "cluster_id": 109693,
          "cite": [
            "53 L. Ed. 2d 140",
            "97 S. Ct. 2243",
            "432 U.S. 98",
            "1977 U.S. LEXIS 116"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
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
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dunaway v. New York",
          "cluster_id": 110096,
          "cite": [
            "60 L. Ed. 2d 824",
            "99 S. Ct. 2248",
            "442 U.S. 200",
            "1979 U.S. LEXIS 126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Yarborough v. Alvarado",
          "cluster_id": 134748,
          "cite": [
            "158 L. Ed. 2d 938",
            "124 S. Ct. 2140",
            "541 U.S. 652",
            "2004 U.S. LEXIS 3843"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
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
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
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
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Beheler",
          "cluster_id": 111023,
          "cite": [
            "77 L. Ed. 2d 1275",
            "103 S. Ct. 3517",
            "463 U.S. 1121",
            "1983 U.S. LEXIS 114",
            "51 U.S.L.W. 3934"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson v. Keohane",
          "cluster_id": 117982,
          "cite": [
            "133 L. Ed. 2d 383",
            "116 S. Ct. 457",
            "516 U.S. 99",
            "1995 U.S. LEXIS 8315",
            "95 Cal. Daily Op. Serv. 8968"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Murphy",
          "cluster_id": 111105,
          "cite": [
            "79 L. Ed. 2d 409",
            "104 S. Ct. 1136",
            "465 U.S. 420",
            "1984 U.S. LEXIS 33",
            "52 U.S.L.W. 4246"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
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
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
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
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Green",
          "cluster_id": 1407600,
          "cite": [
            "616 P.2d 628",
            "94 Wash. 2d 216",
            "1980 Wash. LEXIS 1360"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McKune v. Lile",
          "cluster_id": 121146,
          "cite": [
            "153 L. Ed. 2d 47",
            "122 S. Ct. 2017",
            "536 U.S. 24",
            "2002 U.S. LEXIS 4206"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Minjarez",
          "cluster_id": 2623400,
          "cite": [
            "81 P.3d 348",
            "2003 WL 22938909"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Perkins",
          "cluster_id": 112452,
          "cite": [
            "110 L. Ed. 2d 243",
            "110 S. Ct. 2394",
            "496 U.S. 292",
            "1990 U.S. LEXIS 2885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Howes v. Fields",
          "cluster_id": 623144,
          "cite": [
            "182 L. Ed. 2d 17",
            "132 S. Ct. 1181",
            "565 U.S. 499",
            "2012 U.S. LEXIS 1077",
            "2012 WL 538280"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeffers v. United States",
          "cluster_id": 109694,
          "cite": [
            "53 L. Ed. 2d 168",
            "97 S. Ct. 2207",
            "432 U.S. 137",
            "1977 U.S. LEXIS 20"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hankerson v. North Carolina",
          "cluster_id": 109699,
          "cite": [
            "53 L. Ed. 2d 306",
            "97 S. Ct. 2339",
            "432 U.S. 233",
            "1977 U.S. LEXIS 121"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estrada v. State",
          "cluster_id": 1890229,
          "cite": [
            "313 S.W.3d 274",
            "2010 Tex. Crim. App. LEXIS 722",
            "2010 WL 2382555"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Freddie Sevier v. Kenneth Turner",
          "cluster_id": 440363,
          "cite": [
            "742 F.2d 262"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "J. D. B. v. North Carolina",
          "cluster_id": 218925,
          "cite": [
            "180 L. Ed. 2d 310",
            "131 S. Ct. 2394",
            "564 U.S. 261",
            "2011 U.S. LEXIS 4557",
            "22 Fla. L. Weekly Fed. S 1135",
            "79 U.S.L.W. 4504"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 1728885,
          "cite": [
            "868 S.W.2d 561",
            "1993 Tenn. LEXIS 410"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chambers v. State",
          "cluster_id": 2378796,
          "cite": [
            "866 S.W.2d 9",
            "1993 Tex. Crim. App. LEXIS 166",
            "1993 WL 431505"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herrera v. State",
          "cluster_id": 1872663,
          "cite": [
            "241 S.W.3d 520",
            "2007 Tex. Crim. App. LEXIS 1675",
            "2007 WL 4146707"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Linton",
          "cluster_id": 944931,
          "cite": [
            "56 Cal. 4th 1146",
            "302 P.3d 927",
            "158 Cal. Rptr. 3d 521",
            "2013 WL 3214690",
            "2013 Cal. LEXIS 5338"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109587 OR 9426651 OR 9426652 OR 9426653) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDYzMDk3NjAwMDAwJnM9MzIwNDg0NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109587+OR+9426651+OR+9426652+OR+9426653%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 10,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 10,
        "triage_snippet_classified": 190
      },
      "lane2_top_cited": {
        "query": "cites:(109587 OR 9426651 OR 9426652 OR 9426653)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNjkmcz0xNzQ1NjQxJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109587+OR+9426651+OR+9426652+OR+9426653%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109587 OR 9426651 OR 9426652 OR 9426653)",
        "reviewed": 38,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 38,
        "triage_read": 0,
        "triage_snippet_classified": 38
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109587 OR 9426651 OR 9426652 OR 9426653)",
    "indexed_citing_opinions": 1709,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109587,
        "count": 1538,
        "count_source": "search"
      },
      {
        "opinion_id": 9426651,
        "count": 200,
        "count_source": "search"
      },
      {
        "opinion_id": 9426652,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426653,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2680,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/oregon-v-mathiason.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MzM5MzYmcz0xMDAzODI1MiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109587+OR+9426651+OR+9426652+OR+9426653%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109587,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 107676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 108429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 109429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 109430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 283849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 1289115,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 1390996,
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
    "date_created": "2026-07-05T16:22:38Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:22:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:22:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:25:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:22:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Oregon v. Mathiason

```
<div>
<center><b><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">429 U.S. 492</a></span> (1977)</b></center>
<center><h1>OREGON<br>
v.<br>
MATHIASON.</h1></center>
<center>No. 76-201.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Decided January 25, 1977.</center>
ON PETITION FOR WRIT OF CERTIORARI TO THE SUPREME COURT OF OREGON.
<p>PER CURIAM.</p>
<p>Respondent Carl Mathiason was convicted of first-degree burglary after a bench trial in which his confession was critical to the State's case. At trial he moved to suppress the confession as the fruit of questioning by the police not preceded by the warnings required in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). The trial court refused to exclude the confession because it found that Mathiason was not in custody at the time of the confession.</p>
<p>The Oregon Court of Appeals affirmed respondent's conviction, but on his petition for review in the Supreme Court of Oregon that court by a divided vote reversed the conviction. It found that although Mathiason had not been arrested or otherwise formally detained, "the interrogation took place in a `coercive environment' " of the sort to which <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was intended to apply. The court conceded that its holding was contrary to decisions in other jurisdictions, and referred in particular to <i>People</i> v. <i>Yukl,</i> 25 N. Y. 2d 585, <span class="citation" data-id="5525196"><a href="/opinion/5677336/people-v-yukl/" aria-description="Citation for case: People v. Yukl">256 N. E. 2d 172</a></span> (1969). The State of Oregon has <span class="star-pagination">*493</span> petitioned for certiorari to review the judgment of the Supreme Court of Oregon. We think that court has read <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> too broadly, and we therefore reverse its judgment.</p>
<p>The Supreme Court of Oregon described the factual situation surrounding the confession as follows:</p>
<blockquote>"An officer of the State Police investigated a theft at a residence near Pendleton. He asked the lady of the house which had been burglarized if she suspected anyone. She replied that the defendant was the only one she could think of. The defendant was a parolee and a `close associate' of her son. The officer tried to contact defendant on three or four occasions with no success. Finally, about 25 days after the burglary, the officer left his card at defendant's apartment with a note asking him to call because `I'd like to discuss something with you.' The next afternoon the defendant did call. The officer asked where it would be convenient to meet. The defendant had no preference; so the officer asked if the defendant could meet him at the state patrol office in about an hour and a half, about 5:00 p. m. The patrol office was about two blocks from defendant's apartment. The building housed several state agencies.</blockquote>
<blockquote>"The officer met defendant in the hallway, shook hands and took him into an office. The defendant was told he was not under arrest. The door was closed. The two sat across a desk. The police radio in another room could be heard. The officer told defendant he wanted to talk to him about a burglary and that his truthfulness would possibly be considered by the district attorney or judge. The officer further advised that the police believed defendant was involved in the burglary and [falsely stated that] defendant's fingerprints were found at the scene. The defendant sat for a few minutes and then said he had taken the property. This occurred within five minutes after defendant had come to the office. The <span class="star-pagination">*494</span> officer then advised defendant of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights and took a taped confession.</blockquote>
<blockquote>"At the end of the taped conversation the officer told defendant he was not arresting him at this time; he was released to go about his job and return to his family. The officer said he was referring the case to the district attorney for him to determine whether criminal charges would be brought. It was 5:30 p. m. when the defendant left the office.</blockquote>
<blockquote>"The officer gave all the testimony relevant to this issue. The defendant did not take the stand either at the hearing on the motion to suppress or at the trial." <span class="citation" data-id="9616436"><a href="/opinion/1390996/state-v-mathiason/#3" aria-description="Citation for case: State v. Mathiason">275 Ore. 1, 3-4</a></span>, <span class="citation" data-id="9616436"><a href="/opinion/1390996/state-v-mathiason/#674" aria-description="Citation for case: State v. Mathiason">549 P. 2d 673, 674</a></span> (1976).</blockquote>
<p>The Supreme Court of Oregon reasoned from these facts that:</p>
<blockquote>"We hold the interrogation took place in a `coercive environment.' The parties were in the offices of the State Police; they were alone behind closed doors; the officer informed the defendant he was a suspect in a theft and the authorities had evidence incriminating him in the crime; and the defendant was a parolee under supervision. We are of the opinion that this evidence is not overcome by the evidence that the defendant came to the office in response to a request and was told he was not under arrest." <span class="citation" data-id="9616436"><a href="/opinion/1390996/state-v-mathiason/#5" aria-description="Citation for case: State v. Mathiason"><i>Id.,</i> at 5</a></span>, <span class="citation" data-id="9616436"><a href="/opinion/1390996/state-v-mathiason/#675" aria-description="Citation for case: State v. Mathiason">549 P. 2d, at 675</a></span>.</blockquote>
<p>Our decision in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> set forth rules of police procedure applicable to "custodial interrogation." "By custodial interrogation, we mean questioning initiated by law enforcement officers after a person has been taken into custody or otherwise deprived of his freedom of action in any significant way." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444</a></span>. Subsequently we have found the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> principle applicable to questioning which takes place in a prison setting during a suspect's term of imprisonment on a separate offense, <i>Mathis</i> v. <i>United States,</i> <span class="citation" data-id="9423682"><a href="/opinion/107676/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">391 U. S. 1</a></span> (1968), and to questioning taking place in a <span class="star-pagination">*495</span> suspect's home, after he has been arrested and is no longer free to go where he pleases, <i>Orozco</i> v. <i>Texas,</i> <span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">394 U. S. 324</a></span> (1969).</p>
<p>In the present case, however, there is no indication that the questioning took place in a context where respondent's freedom to depart was restricted in any way. He came voluntarily to the police station, where he was immediately informed that he was not under arrest. At the close of a 1/2-hour interview respondent did in fact leave the police station without hindrance. It is clear from these facts that Mathiason was not in custody "or otherwise deprived of his freedom of action in any significant way."</p>
<p>Such a noncustodial situation is not converted to one in which <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> applies simply because a reviewing court concludes that, even in the absence of any formal arrest or restraint on freedom of movement, the questioning took place in a "coercive environment." Any interview of one suspected of a crime by a police officer will have coercive aspects to it, simply by virtue of the fact that the police officer is part of a law enforcement system which may ultimately cause the suspect to be charged with a crime. But police officers are not required to administer <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings to everyone whom they question. Nor is the requirement of warnings to be imposed simply because the questioning takes place in the station house, or because the questioned person is one whom the police suspect. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are required only where there has been such a restriction on a person's freedom as to render him "in custody." It was <i>that</i> sort of coercive environment to which <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> by its terms was made applicable, and to which it is limited.</p>
<p>The officer's false statement about having discovered Mathiason's fingerprints at the scene was found by the Supreme Court of Oregon to be another circumstance contributing to the coercive environment which makes the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rationale applicable. Whatever relevance this fact <span class="star-pagination">*496</span> may have to other issues in the case, it has nothing to do with whether respondent was in custody for purposes of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule.</p>
<p>The petition for certiorari is granted, the judgment of the Oregon Supreme Court is reversed, and the case is remanded for proceedings not inconsistent with this opinion.</p>
<p><i>So ordered.</i></p>
<p>MR. JUSTICE BRENNAN would grant the writ but dissents from the summary disposition and would set the case for oral argument.</p>
<p>MR. JUSTICE MARSHALL, dissenting.</p>
<p>The respondent in this case was interrogated behind closed doors at police headquarters in connection with a burglary investigation. He had been named by the victim of the burglary as a suspect, and was told by the police that they believed he was involved. He was falsely informed that his fingerprints had been found at the scene, and in effect was advised that by cooperating with the police he could help himself. Not until after he had confessed was he given the warnings set forth in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966).</p>
<p>The Court today holds that for constitutional purposes all this is irrelevant because respondent had not " `been taken into custody or otherwise deprived of his freedom of action in any significant way.' " <i>Ante,</i> at 494, quoting <i>Miranda</i> v. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><i>Arizona, supra,</i> at 444</a></span>. I do not believe that such a determination is possible on the record before us. It is true that respondent was not formally placed under arrest, but surely formalities alone cannot control. At the very least, if respondent entertained an objectively reasonable belief that he was not free to leave during the questioning, then he was "deprived of his freedom of action in a significant way."<sup>[1]</sup><span class="star-pagination">*497</span> Plainly the respondent could have so believed, after being told by the police that they thought he was involved in a burglary and that his fingerprints had been found at the scene. Yet the majority is content to note that "there is no indication that . . . respondent's freedom to depart was restricted in any way," <i>ante,</i> at 495, as if a silent record (and no state-court findings) means that the State has sustained its burden, see <i>Lego</i> v. <i>Twomey,</i> <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#489" aria-description="Citation for case: Lego v. Twomey">404 U. S. 477, 489</a></span> (1972), of demonstrating that respondent received his constitutional due.<sup>[2]</sup></p>
<p>More fundamentally, however, I cannot agree with the Court's conclusion that if respondent were not in custody no warnings were required. I recognize that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is limited to custodial interrogations, but that is because, as we noted last Term, the facts in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> cases raised only this "narrow issue." <i>Beckwith</i> v. <i>United States,</i> <span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/#345" aria-description="Citation for case: Beckwith v. United States">425 U. S. 341, 345</a></span> (1976). The rationale of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> however, is not so easily cabined.</p>
<p><i>Miranda</i> requires warnings to "combat" a situation in which there are "inherently compelling pressures which work to undermine the individual's will to resist and to compel <span class="star-pagination">*498</span> him to speak where he would not otherwise do so freely." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 467</a></span>. It is of course true, as the Court notes, that "[a]ny interview of one suspected of a crime by a police officer will have coercive aspects to it." <i>Ante,</i> at 495. But it does not follow that because police "are not required to administer <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings to everyone whom they question," <i>ibid.,</i> that they need not administer warnings to <i>anyone,</i> unless the factual setting of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> cases is replicated. Rather, faithfulness to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires us to distinguish situations that resemble the "coercive aspects" of custodial interrogation from those that more nearly resemble "[g]eneral on-the-scene questioning . . . or other general questioning of citizens in the fact-finding process" which <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> states usually can take place without warnings. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#477" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 477</a></span>.</p>
<p>In my view, even if respondent were not in custody, the coercive elements in the instant case were so pervasive as to require <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>-type warnings.<sup>[3]</sup> Respondent was interrogated in "privacy" and in "unfamiliar surroundings," factors on which <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> places great stress. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#449" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 449-450</a></span>; see also <i>Beckwith</i> v. <i>United States, supra,</i> at 346 n. 7. The investigation had focused on respondent. And respondent was subjected to some of the "deceptive stratagems," <i>Miranda</i> v. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#455" aria-description="Citation for case: Miranda v. Arizona"><i>Arizona, supra,</i> at 455</a></span>, which called forth the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> decision. I therefore agree with the Oregon Supreme Court that to excuse the absence of warnings given these facts is "contrary to the rationale expressed in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i>" <span class="citation" data-id="9616436"><a href="/opinion/1390996/state-v-mathiason/#5" aria-description="Citation for case: State v. Mathiason">275 Ore. 1, 5</a></span>, <span class="citation" data-id="9616436"><a href="/opinion/1390996/state-v-mathiason/#675" aria-description="Citation for case: State v. Mathiason">549 P. 2d 673, 675</a></span> (1976).<sup>[4]</sup></p>
<p><span class="star-pagination">*499</span> The privilege against self-incrimination "has always been `as broad as the mischief against which it seeks to guard.' " <i>Miranda</i> v. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#459" aria-description="Citation for case: Miranda v. Arizona"><i>Arizona, supra,</i> at 459-460</a></span>, quoting <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#562" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 562</a></span> (1892). Today's decision means, however, that the Fifth Amendment privilege does not provide full protection against mischiefs equivalent to, but different from, custodial interrogation.<sup>[5]</sup> See also <i>Beckwith</i> v. <i>United States, supra</i><i>.</i> It is therefore important to note that the state courts remain free, in interpreting state constitutions, to guard against the evil clearly identified by this case.<sup>[6]</sup></p>
<p>I respectfully dissent.</p>
<p>MR. JUSTICE STEVENS, dissenting.</p>
<p>In my opinion the issues presented by this case are too important to be decided summarily. Of particular importance <span class="star-pagination">*500</span> is the fact that the respondent was on parole at the time of his interrogation in the police station. This fact lends support to inconsistent conclusions.</p>
<p>On the one hand, the State surely has greater power to question a parolee about his activities than to question someone else. Moreover, as a practical matter, it seems unlikely that a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning would have much effect on a parolee's choice between silence and responding to police interrogation. Arguably, therefore, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are entirely inappropriate in the parole context.</p>
<p>On the other hand, a parolee is technically in legal custody continuously until his sentence has been served. Therefore, if a formalistic analysis of the custody question is to determine when the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning is necessary, a parolee should always be warned. Moreover, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> teaches that even if a suspect is not in custody, warnings are necessary if he is "otherwise deprived of his freedom of action in any significant way." If a parolee being questioned in a police station is not described by that language, today's decision qualifies that part of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to some extent. I believe we would have a better understanding of the extent of that qualification, and therefore of the situations in which warnings must be given to a suspect who is not technically in custody, if we had the benefit of full argument and plenary consideration.</p>
<p>I therefore respectfully dissent from the Court's summary disposition.</p>
<h2>NOTES</h2>
<p>[1]  See, <i>e. g., </i><i>United States</i> v. <i>Hall,</i> <span class="citation" data-id="288311"><a href="/opinion/288311/united-states-v-glenn-w-hall/#544" aria-description="Citation for case: United States v. Glenn W. Hall">421 F. 2d 540, 544-545</a></span> (CA2 1969) (Friendly, J.); <i>Lowe</i> v. <i>United States,</i> <span class="citation" data-id="283849"><a href="/opinion/283849/arnold-lowe-v-united-states/" aria-description="Citation for case: Arnold Lowe v. United States">407 F. 2d 1391</a></span> (CA9 1969); <i>People</i> v. <i>Arnold,</i> <span class="citation" data-id="9853164"><a href="/opinion/1289115/people-v-arnold/" aria-description="Citation for case: People v. Arnold">66 Cal. 2d 438</a></span>, <span class="citation" data-id="9853164"><a href="/opinion/1289115/people-v-arnold/" aria-description="Citation for case: People v. Arnold">426 P. 2d 515</a></span> (1967); <i>People</i> v. <i>Rodney P.,</i> 21 N. Y. 2d 1, <span class="citation" data-id="9787785"><a href="/opinion/2590535/people-v-rodney-panonymous/" aria-description="Citation for case: People v. Rodney P.(Anonymous)">233 N. E. 2d 255</a></span> (1967). See also cases collected in Annot., 31 A. L. R. 3d 565, 581-583 (1970 and Supp. 1976).
</p>
<p>It has been noted that as a logical matter, a person who honestly but unreasonably believes he is in custody is subject to the same coercive pressures as one whose belief is reasonable; this suggests that such persons also are entitled to warnings. See, <i>e. g.,</i> LaFave, "Street Encounters" and the Constitution: Terry, Sibron, Peters, and Beyond, <span class="citation no-link">67 Mich. L. Rev. 39</span>, 105 (1968); Smith, The Threshold Question in Applying Miranda: What Constitutes Custodial Interrogation?, 25 S. C. L. Rev. 699, 711-714 (1974).</p>
<p>[2]  The Court's action is particularly inappropriate because the record of this case has not been transmitted to us, and thus our knowledge of the facts is limited to the information contained in the petition and in the opinions of the state courts.</p>
<p>[3]  I do not rule out the possibility that lesser warnings would suffice when a suspect is not in custody but is subjected to a highly coercive atmosphere. See, <i>e. g., </i><i>Beckwith</i> v. <i>United States,</i> <span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/#348" aria-description="Citation for case: Beckwith v. United States">425 U. S. 341, 348-349</a></span> (1976) (MARSHALL, J., concurring in judgment); ALI, Model Code of Pre-Arraignment Procedure § 110.1 (2) (Approved Draft 1975) (suspects interrogated at police station must be advised of their right to leave and right to consult with counsel, relatives, or friends).</p>
<p>[4]  See also Graham, What is "Custodial Interrogation?": California's Anticipatory Application of <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona</a></span>,</i> <span class="citation no-link">14 UCLA L. Rev. 59</span>, 81-82 (1966); Smith, <i>supra,</i> n. 1, at 732, 735.</p>
<p>[5]  I trust today's decision does not suggest that police officers can circumvent <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> by deliberately postponing the official "arrest" and the giving of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings until the necessary incriminating statements have been obtained.</p>
<p>[6]  See, <i>e. g., </i><i>South Dakota</i> v. <i>Opperman,</i> <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#384" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 384</a></span> (1976) (MARSHALL, J., dissenting); <i>Baxter</i> v. <i>Palmigiano,</i> <span class="citation" data-id="9426363"><a href="/opinion/109429/baxter-v-palmigiano/#324" aria-description="Citation for case: Baxter v. Palmigiano">425 U. S. 308, 324, 338-339</a></span> (1976) (BRENNAN, J., dissenting); <i>Michigan</i> v. <i>Mosley,</i> <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#120" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 120-121</a></span> (1975) (BRENNAN, J., dissenting); Wilkes, The New Federalism in Criminal Procedure: State Court Evasion of the Burger Court, 62 Ky. L. J. 421 (1974); Wilkes, More on the New Federalism in Criminal Procedure, 63 Ky. L. J. 873 (1975).
</p>
<p>In <i><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span>,</i> this Court reversed a decision of the South Dakota Supreme Court holding that routine inventory searches of impounded automobiles, made without probable cause or consent, violated the Fourth Amendment. The case was remanded, like this one, "for further proceedings not inconsistent with [the] opinion." <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#376" aria-description="Citation for case: South Dakota v. Opperman">428 U. S., at 376</a></span>. On remand, the South Dakota Supreme Court held that such searches violated a nearly identical provision of the State Constitution, and that therefore the seized evidence should have been suppressed. <i>State</i> v. <i>Opperman,</i> 89 S. D., <span class="citation" data-id="9573888"><a href="/opinion/1311789/state-v-opperman/" aria-description="Citation for case: State v. Opperman">228 N. W. 2d 152</a></span> (1976).</p>

</div>
```

---
