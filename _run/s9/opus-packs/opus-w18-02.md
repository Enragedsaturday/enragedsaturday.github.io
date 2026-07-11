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

## GROUP: _overhaul2/lake/cases/United States v. Meyer.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Meyer
type: case
citation: "19 F.4th 1028 (2021)"
parallel_cite: ""
neutral_cite: ""
court: 8th Cir.
court_level: coa
circuit: ca8
year: 2021
date_decided: 2021-12-02
docket: 20-2958
authority_weight: "Binding in-circuit — 8th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/5302394/united-states-v-william-meyer/"
  cluster_id: 5302394
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Meyer
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Knock and Talk]]"
    role: Key
  - page: "[[Exigent Circumstances and Hot Pursuit]]"
    role: "Related (cross-doctrine)"
related:
  - "[[Knock and Talk]]"
  - "[[Exigent Circumstances and Hot Pursuit]]"
  - "[[Kentucky v. King]]"
  - "[[Riley v. California]]"
tags:
  - case
  - fourth-amendment
  - knock-and-talk
  - exigent-circumstances
  - destruction-of-evidence
  - warrantless-entry
  - eighth-circuit
holding: "A 'knock and talk' — approaching a home and knocking to ask questions — is a valid investigative technique, and where a suspect's evasive answers during such an encounter give officers an objectively reasonable basis to believe he will destroy digital evidence if left alone, the resulting exigency justifies a warrantless entry and seizure, provided the officers did not manufacture the exigency by threatening to violate the Fourth Amendment."
aliases:
  - United States v. Meyer
  - "United States v. Meyer (8th Cir. 2021)"
---

# United States v. Meyer

*19 F.4th 1028 (8th Cir. 2021)* (No. 20-2958) · U.S. Court of Appeals for the Eighth Circuit · **Binding in-circuit — 8th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 5302394 → lead opinion 5130956 (Stras, J.; 19 F.4th 1028, decided 2021-12-02); Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — CL text is slip-paginated). S9 promotes. -->

## Background
As part of "Operation Dark Room," federal agents traced financial ties between William Meyer and individuals in the Philippines who were livestreaming the sexual abuse of children. Two agents went to Meyer's home and knocked; the conversation moved to the agents' car. Meyer made increasingly suspicious admissions — including personal and financial ties to those involved — and acknowledged using a computer and cellphone to contact them. When asked to hand over the devices, he first offered to do so later, after he could "check [his] email and stuff," then refused because his house was "a mess," and ultimately went back inside alone despite the agents' request that he wait. Concerned that he would erase the devices, an agent called a prosecutor, was told an [[Exigent Circumstances and Hot Pursuit|exigency]] existed, and the agents re-knocked, entered without a warrant, and seized two computers, a cellphone, and a hard drive; a warrant issued afterward, and the search revealed child pornography. Meyer's suppression motion was denied, and he entered a conditional guilty plea.

## Issue
Whether a warrantless entry into a home is justified by [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] when a suspect's evasive conduct during a [[Knock and Talk|knock-and-talk]] gives officers reason to believe he will destroy digital evidence, and whether the officers impermissibly created that [[Exigent Circumstances and Hot Pursuit|exigency]].

## Rule
The [[Knock and Talk|knock-and-talk]] is a lawful, consensual investigative technique that does not itself implicate the Fourth Amendment, and officers who lawfully develop a reasonable fear that evidence will be imminently destroyed may enter without a warrant — so long as they did not create the [[Exigent Circumstances and Hot Pursuit|exigency]] by threatening to act unlawfully. As the panel explained: "Knocking on a suspect's door to ask questions, a so-called 'knock and talk,' has long been a valid investigative technique". — 19 F.4th 1028, slip op. at 6. ^pin-op6

## Application
Meyer's own answers — professing constant need for a computer he was willing to surrender only later, citing a messy house, and insisting on time alone with his devices before going back inside — gave the agents an objectively reasonable basis to conclude he intended to be alone with the devices to erase their contents, data that can be deleted at the touch of a button. That supplied a genuine [[Exigent Circumstances and Hot Pursuit|exigency]]: it was now or never. And the agents did not manufacture the [[Exigent Circumstances and Hot Pursuit|exigency]]; a [[Knock and Talk|knock-and-talk]] is a valid technique, and Meyer did more than merely stand on his rights and decline entry — his suspicious conduct, not any threat by the agents to violate the Fourth Amendment, produced the risk of destruction. The warrantless entry and seizure were therefore reasonable.

## Conclusion
**Affirmed.** Judge Stras wrote for the panel (Gruender, Benton, and Stras, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Meyer* sits at the junction of the **[[Knock and Talk|knock-and-talk]]** and **exigent-circumstances** doctrines: it reaffirms that a [[Knock and Talk|knock-and-talk]] is a valid, consensual technique, and applies *[[Kentucky v. King|Kentucky v. King]]*'s rule that police may not rely on an [[Exigent Circumstances and Hot Pursuit|exigency]] they created by threatening to violate the Fourth Amendment — holding these agents did not, because the suspect's own evasive conduct generated the risk that digital evidence would be destroyed. Teach it for the destruction-of-evidence [[Exigent Circumstances and Hot Pursuit|exigency]] in the digital context and the police-created-[[Exigent Circumstances and Hot Pursuit|exigency]] limit.

## Appears on
- [[Knock and Talk]] — *Key*
- [[Exigent Circumstances and Hot Pursuit]] — *Related (cross-doctrine)*

## Sources
- [*United States v. Meyer*, 19 F.4th 1028 (8th Cir. 2021)](https://www.courtlistener.com/opinion/5302394/united-states-v-william-meyer/) — pinpoint: slip op. at 6 (knock-and-talk validity, en route to the destruction-of-evidence exigency holding; the CL opinion text carries slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d966cf794c66a047", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Meyer"}, "payload": {"all": [{"cite": "19 F.4th 1028", "page": "1028", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "19"}], "display": "19 F.4th 1028", "official": {"cite": "19 F.4th 1028", "page": "1028", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "19"}, "official_selection_present": true, "record_id": "United States v. Meyer"}}
{"assertion_id": "a07ba7952fb20fc3", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Meyer"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Meyer", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Meyer

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Meyer",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. William Meyer",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Meyer",
    "court": "8th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca8",
    "state": null,
    "date_decided": "2021-12-02",
    "year": 2021,
    "docket": "20-2958",
    "cluster_id": 5302394,
    "lead_opinion_id": 5130956,
    "sibling_ids": [],
    "absolute_url": "/opinion/5302394/united-states-v-william-meyer/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "19 F.4th 1028",
      "volume": "19",
      "reporter": "F.4th",
      "page": "1028",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "19 F.4th 1028",
        "volume": "19",
        "reporter": "F.4th",
        "page": "1028",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "19 F.4th 1028",
    "official_selection": {
      "court_class": "coa",
      "selected": "19 F.4th 1028",
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
    "date_created": "2026-07-07T01:40:09Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:40:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:40:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:40:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:40:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-meyer--5302394",
      "to_record_id": "United States v. Meyer",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Meyer

```
                 United States Court of Appeals
                            For the Eighth Circuit
                        ___________________________

                                No. 20-2958
                        ___________________________

                            United States of America

                                      Plaintiff - Appellee

                                        v.

                                 William Meyer

                                   Defendant - Appellant
                                 ____________

                     Appeal from United States District Court
                 for the Northern District of Iowa - Cedar Rapids
                                  ____________

                            Submitted: June 17, 2021
                            Filed: December 2, 2021
                                 ____________

Before GRUENDER, BENTON, and STRAS, Circuit Judges.
                          ____________

STRAS, Circuit Judge.

       While talking with William Meyer outside his home, federal agents grew
worried that, if he went back inside, he would destroy evidence. Rather than take
that risk, they entered his home without a warrant and took two computers, a
cellphone, and a hard drive. The main question in this case is whether their actions
violated the Fourth Amendment. We agree with the district court 1 that they did not.

                                          I.

       As part of an investigation named “Operation Dark Room,” federal agents
discovered financial ties between Meyer and individuals in the Philippines who were
livestreaming sex acts involving children. To gather more information, two agents
decided to visit Meyer at his home and knock on his door. During the course of the
conversation, which took place in the agents’ car, Meyer revealed a number of facts
that aroused suspicion, including that he had personal and financial ties to the
individuals involved in the abuse. When he further admitted that he used a computer
and cellphone to contact them, the agents asked if he would be willing to turn those
devices over for an examination.

       Rather than categorically refusing, Meyer said he was willing to hand them
over later, after he had a chance to “check [his] email and stuff.” Once the agents
expressed concern that a delay would give him a chance to erase what was on them,
Meyer still refused to consent, this time because his house was “a mess” and “not . . .
in any condition to entertain people.” So after further discussion, he went back
inside.

      At that point, the agents sprang into action. Worried that Meyer would destroy
evidence if they waited any longer, one of the agents called a prosecutor for advice
on whether “an exigent circumstance existed.” When he was told that it did, the
agents again knocked on Meyer’s door; searched his home for electronic devices;
and seized two computers, a cellphone, and a hard drive. One of the agents then
successfully applied for a search warrant.



      1
        The Honorable C.J. Williams, United States District Judge for the Northern
District of Iowa.

                                         -2-
     The search revealed a hoard of child pornography. The hard drive, for
example, contained videos of minors performing sex acts on Skype, with Meyer
shown watching in the corner of the screen. It also contained a number of lewd
messages between Meyer and a minor girl, as well as evidence that he had sent
money in exchange for the videos.

      The evidence spelled trouble for Meyer, who moved to suppress everything
the agents found. The district court denied the motion; accepted his conditional plea
to one count of sexual exploitation of children, see 18 U.S.C. § 2251(a), (e); and
sentenced him to 30 years in prison. On appeal, he challenges both the denial of his
motion and the length of his sentence.

                                          II.

        The default rule for entering a home to search and retrieve evidence is to get
a warrant first. See Brigham City v. Stuart, 547 U.S. 398, 403 (2006). But when
there is “a sufficient basis” to suspect that incriminating evidence will be destroyed,
United States v. Ramirez, 676 F.3d 755, 760 (8th Cir. 2012), exigent circumstances
exist, and the presence of probable cause allows officers to enter and search the home
without one. The lone exception is when the officers themselves have created the
exigency by “engaging or threatening to engage in conduct that violates the Fourth
Amendment.” Kentucky v. King, 563 U.S. 452, 462 (2011).

      Meyer challenges the warrantless entry into his home at every step in this
analysis. First, he claims that there was no probable cause. Second, he denies the
existence of an exigency. And third, even if an exigency existed, he claims the
agents created it. Each of these “challenges fall[s] into [the legal-question] category,
so our review is de novo.” United States v. James, 3 F.4th 1102, 1104 (8th Cir.
2021).




                                          -3-
                                           A.

      On these facts, probable cause is not a close call. It “exists when[ever] . . . a
reasonable person could believe [that] there is a fair probability that . . . evidence of
a crime w[ill] be found” in the place to be searched. Kleinholz v. United States, 339
F.3d 674, 676 (8th Cir. 2003) (per curiam) (quotation marks omitted).

      By the time the agents decided to enter Meyer’s home, they had probable
cause. See Kaley v. United States, 571 U.S. 320, 338 (2014) (explaining that
probable cause “is not a high bar”). They knew that he: (1) had ties to the individuals
who were livestreaming the abuse; (2) had stayed with them when he visited the
Philippines; (3) had paid thousands to them and one of the minor victims; and (4)
did not tell his wife about some of the money he sent, despite claiming that the
payments were tied to his humanitarian work. It was not much of a leap from there
to conclude that there was a “fair probability” that he was involved. See United
States v. Horne, 4 F.3d 579, 589 (8th Cir. 1993) (explaining that officers have
“substantial latitude” to draw “inferences” from what they know).

       The same goes for the possibility that there would be incriminating evidence
on Meyer’s devices. See United States v. Tellez, 217 F.3d 547, 550 (8th Cir. 2000)
(explaining that there must be “a nexus between the [illegal activity] and the place
to be searched”). Meyer had already admitted to the agents that he used a computer
and cellphone to communicate with the abusers and had stayed in regular contact
with them. The agents also knew that his Skype username was “prettyvirginfilipino”
and that the profile he used was a variant of the first name of one of the minor
victims. Given that Meyer had already admitted that the devices were in his home,
there was at least “a fair probability” that the agents would find “evidence of a crime”
inside. Kleinholz, 339 F.3d at 676.

      Just because Meyer had an innocent explanation for some of these facts did
not mean the officers had to believe him. As the Supreme Court has put it, “probable
cause does not require [officers] to rule out a suspect’s innocent explanation for


                                          -4-
suspicious facts.” District of Columbia v. Wesby, 138 S. Ct. 577, 588 (2018). And
here, the “circumstances” were suspicious enough that the agents could have
reasonably concluded there was a “substantial chance” that Meyer was involved in
“criminal activity,” not charitable work. Id. at 586.

                                          B.

       Though a closer call, the agents also faced an exigency: they had a “sufficient
basis” to reasonably believe that Meyer would “imminently destroy evidence.”
Ramirez, 676 F.3d at 760; see also United States v. Knobeloch, 746 F.2d 1366, 1367
(8th Cir. 1984). Meyer’s suspicious answers, including his insistence that he have
time alone with his devices before the agents could see them, is what led to a sense
of urgency, a “now[-]or[-]never” scenario. Riley v. California, 573 U.S. 373, 391
(2014) (quoting Missouri v. McNeely, 569 U.S. 141, 153 (2013)); see also United
States v. Cisneros-Gutierrez, 598 F.3d 997, 1004 (8th Cir. 2010) (observing that a
suspect’s “conduct” can create the exigency).

       Consider what Meyer said and did. When asked whether he would allow an
examination of his computer, he initially said no because he used it “all the time.”
Then, despite his professed need for it, he offered to let the agents examine it later,
after he “check[ed] [his] email and stuff.”

       From there, Meyer’s responses only became more suspicious. When the
agents suggested that they accompany him inside and look at the devices together,
his attention shifted to the tidiness of his house. His “house [was] a mess,” he said,
so he would need “a few minutes to clean up.” And then, rather than remaining
outside as requested while one of the agents made a call, Meyer instead went inside.

       Knowing that data can be deleted at the touch of a button, the agents decided
that they needed to act fast. See Riley, 573 U.S. at 391. Given Meyer’s insistence
that he have an opportunity to be alone with his devices first, they reasonably
concluded that he was hiding something. And if they were to wait to conduct the


                                         -5-
search, as he had suggested, the something that he did not want them to see would
be gone. 2 So the agents reasonably determined that it was “now or never”:
“search . . . immediately,” or forever lose their chance. See Riley, 573 U.S. at 391
(quotation marks omitted).

                                          C.

      It should also be clear by now that the agents did not create the exigency “by
engaging or threatening to engage in conduct that violates the Fourth Amendment.”
King, 563 U.S. at 462. Knocking on a suspect’s door to ask questions, a so-called
“knock and talk,” has long been a valid investigative technique, see United States v.
Spotted Elk, 548 F.3d 641, 655 (8th Cir. 2008), so Meyer’s argument focuses on
what happened next.

                                          1.

       After the agents knocked on his door, Meyer insisted on speaking with them
outside, so the conversation took place in the agents’ car. Toward the end, one of
the agents told Meyer that, “if I suspect that something’s going on, . . . I can’t just
let people go in and have an opportunity to . . . destroy potential evidence.” Then,
after the possibility of getting a warrant came up and Meyer suggested that they
come back later, the same agent said, “I’m not gonna tell you when I want it. I’ll
come over, I’ll knock on the door, and we’ll . . . go from there.” According to
Meyer, these two statements created the exigency by planting the idea of destroying


      2
        Meyer did more than just “stand on [his] constitutional rights.” King, 563
U.S. at 470; cf. Ramirez, 676 F.3d at 762–64 (concluding that there were no exigent
circumstances when the suspect merely declined to let the officers enter and then
shut the door on them). Rather, he gave suspicious answers that led the agents to
reasonably conclude that he wanted time alone with the devices for a reason he could
not say out loud: to destroy evidence. See United States v. Leveringston, 397 F.3d
1112, 1116 (8th Cir. 2005) (noting that officers may draw reasonable inferences
when evaluating whether exigent circumstances exist).

                                         -6-
evidence in his mind and threatening to take his property at any time, with or without
a warrant.

      The most obvious problem with Meyer’s theory is timing. By that point,
Meyer had already made a number of suspicious comments, including offering
multiple excuses for his refusal to cooperate. For the agents to have caused the
exigency, they must have “manufacture[d]” or “create[d]” it. Ramirez, 676 F.3d at
761 n.3 (quotation marks omitted). They could not have manufactured or created an
exigency that already existed.

       Nor did either statement threaten to violate Meyer’s Fourth Amendment
rights. See King, 563 U.S. at 462. The first was just a response to his attempts to
persuade the agents to return for the devices. And the second merely explained that,
if the agents were to come back with a warrant, the search would not, as the district
court put it, “be scheduled at [his] convenience.”

                                          2.

       Nothing else the agents did that day created an exigency either. Meyer
suggests that they spoke it into existence by raising the possibility that he would
destroy evidence. But hypothesizing about what Meyer might do is not the same as
threatening to engage in conduct that would violate his constitutional rights. See id.
at 462. Besides, the agents were only saying out loud what they reasonably
suspected was true based on what he had already said. His responses, in other words,
are what created the exigency.

      For similar reasons, the agents did not have to “act” like “members of the
general public” when they spoke to him. Just because asking tough questions and
closely scrutinizing the answers could lead a suspect to destroy evidence does not
mean that someone else created the exigency. See United States v. Newman, 472
F.3d 233, 238–39 (5th Cir. 2006) (explaining that officers did “not manufacture an
exigency by employing a legitimate investigative tactic”). Rather, the agents in this


                                         -7-
case would have needed to do something more: “engag[e] or threaten[] to engage in
conduct that violate[d] the Fourth Amendment.” King, 563 U.S. at 462.

                                     *      *      *

       Long story short: probable cause existed, the exigency was real, and it was
not of the agents’ making. So even though the search was warrantless, it did not
violate the Fourth Amendment.

                                           III.

       Nor do we need to remand for resentencing, even though the district court
mistakenly told Meyer that he had “to persuade the court to vary downward.” Meyer
did not object at the time, so our review is for plain error. See United States v. Pirani,
406 F.3d 543, 549 (8th Cir. 2005) (en banc). Even assuming this statement was
erroneous and that any error was plain, it did not affect Meyer’s substantial rights.
See United States v. Henson, 550 F.3d 739, 740 (8th Cir. 2008) (explaining that
treating the advisory range as presumptive is “significant procedural error,” but
holding that the error may still be harmless (quoting Gall v. United States, 552 U.S.
38, 51 (2007)).

       The remainder of the record makes clear that this statement did not play a role
in the district court’s analysis. The court stated, for example, that it had “considered
all the [statutory sentencing] factors,” including Meyer’s “horrendous, egregious
victimization of vulnerable victims,” in an effort to “arriv[e] at a sentence that [was]
sufficient but not greater than necessary to achieve the goals of sentencing.” See 18
U.S.C. § 3553(a). It then went on to explain that there was no reason to vary
downward because “the aggravating factors . . . vastly outweigh[ed] the mitigating
factors.” Given these other comments, we conclude that, even if the court erred,
there is no “reasonable probability” that it affected Meyer’s sentence. United States
v. Cottrell, 853 F.3d 459, 463 (8th Cir. 2017).



                                           -8-
                                 IV.

We accordingly affirm the judgment of the district court.
               ______________________________




                                 -9-

```

---

## GROUP: _overhaul2/lake/cases/United States v. Miller.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Miller"
type: case
citation: "425 U.S. 435 (1976)"
parallel_cite: "96 S. Ct. 1619; 48 L. Ed. 2d 71; 37 A.F.T.R.2d (RIA) 1261"
neutral_cite: 1976 U.S. LEXIS 148
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-04-21
docket: 74-1179
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-04-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Miller
  varies_by_point: false
  scope_note: "Foundational third-party-doctrine case (bank records); remains good law. Carpenter v. United States (2018) declined to extend the third-party doctrine to cell-site location information but expressly did not overrule Miller."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109433/united-states-v-miller/"
  cluster_id: 109433
  opinion_id: 9426375
  identity_checked: true
homes:
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Key — Anchor"
related: ["[[Smith v. Maryland]]", "[[Carpenter v. United States]]", "[[Katz v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "third-party-doctrine", "bank-records", "standing"]
holding: "No legitimate expectation of privacy in bank records (checks, deposit slips) voluntarily conveyed to a bank; a depositor assumes the risk the bank will disclose them to the government (third-party doctrine)."
lake:
  record_id: United States v. Miller
  status: verified
  projected_at: 2026-07-09
---

# United States v. Miller

*425 U.S. 435 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
During an investigation into untaxed-whiskey offenses, federal agents obtained Miller's bank records — microfilmed checks, deposit slips, and financial statements — from two banks through grand-jury subpoenas. Miller moved to suppress the records, arguing the government's acquisition of his financial records from the banks was an unreasonable search and seizure of materials in which he had a Fourth Amendment interest.

## Issue
Whether a bank depositor has a Fourth Amendment-protected expectation of privacy in financial records (cancelled checks, deposit slips, and statements) maintained by his bank, so that the government's acquisition of them constitutes a search or seizure as to the depositor.

## Rule
No. The records are the bank's business records, and the depositor has no legitimate expectation of privacy in information he conveys to the bank. "All of the documents obtained, including financial statements and deposit slips, contain only information voluntarily conveyed to the banks and exposed to their employees in the ordinary course of business." — 425 U.S. at 442. ^pin-442

That voluntary exposure forfeits any Fourth Amendment claim: "The depositor takes the risk, in revealing his affairs to another, that the information will be conveyed by that person to the Government." — [*Id.* at 443](https://www.courtlistener.com/opinion/109433/united-states-v-miller/#:~:text=The%20depositor%20takes%20the%20risk%2C). ^pin-443

## Application
The checks were not confidential communications but negotiable instruments used in commercial transactions, and the statements and deposit slips contained only information Miller had voluntarily handed to his banks and exposed to their employees in the ordinary course of business. Because the records were not Miller's private papers and he had assumed the risk the banks would disclose them, he had no legitimate expectation of privacy and no Fourth Amendment interest the government's acquisition could invade.

## Conclusion
Miller had no protectable Fourth Amendment interest in the bank records; obtaining them worked no search or seizure as to him. With [[Smith v. Maryland]] (dialed numbers), *Miller* is a pillar of the third-party doctrine the Court later confronted for digital data in [[Carpenter v. United States]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Miller* remains good law. [[Carpenter v. United States]] (2018) declined to extend the third-party doctrine to historical cell-site location information, but **expressly declined to overrule** *Miller* or [[Smith v. Maryland]]; the bank-records holding stands. (The result also prompted the statutory Right to Financial Privacy Act, a non-constitutional check.)

## Appears on
- [[Third-Party Doctrine & CSLI]] — *Key — Anchor*

## Sources
- *United States v. Miller*, 425 U.S. 435 (1976) — https://www.courtlistener.com/opinion/109433/united-states-v-miller/ — pinpoints: 442, 443.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "cebe4181b0310c17", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Miller"}, "payload": {"all": [{"cite": "425 U.S. 435", "page": "435", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "425"}, {"cite": "96 S. Ct. 1619", "page": "1619", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "96"}, {"cite": "48 L. Ed. 2d 71", "page": "71", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "48"}, {"cite": "1976 U.S. LEXIS 148", "page": "148", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1976"}, {"cite": "37 A.F.T.R.2d (RIA) 1261", "page": "1261", "reporter": "A.F.T.R.2d (RIA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "37"}], "display": "425 U.S. 435", "official": {"cite": "425 U.S. 435", "page": "435", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "425"}, "official_selection_present": true, "record_id": "United States v. Miller"}}
{"assertion_id": "575533c3c66c09d4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-442", "record_id": "United States v. Miller"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-442", "pinpoint_status": "slip-only", "quote": "--- # United States v. Miller *425 U.S. 435 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background During an investigation into untaxed-whiskey offenses, federal agents obtained Miller's bank records — microfilmed checks, deposit slips, and financial statements — from two banks through grand-jury subpoenas. Miller moved to suppress the records, arguing the government's acquisition of his financial records from the banks was an unreasonable search and seizure of materials in which he had a Fourth Amendment interest. ## Issue Whether a bank depositor has a Fourth Amendment-protected expectation of privacy in financial records (cancelled checks, deposit slips, and statements) maintained by his bank, so that the government's acquisition of them constitutes a search or seizure as to the depositor. ## Rule No. The records are the bank's business records, and the depositor has no legitimate expectation of privacy in information he conveys to the bank.", "quote_fidelity": "mismatch", "record_id": "United States v. Miller", "star_marker": null}}
{"assertion_id": "abb3fa3c4f84b539", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-443", "record_id": "United States v. Miller"}, "payload": {"fragment": "#:~:text=The%20depositor%20takes%20the%20risk%2C", "page": null, "pin_id": "pin-443", "pinpoint_status": "star-verified", "quote": "The depositor takes the risk, in revealing his affairs to another, that the information will be conveyed by that person to the Government.", "quote_fidelity": "matched", "record_id": "United States v. Miller", "star_marker": "443"}}
{"assertion_id": "9802e5b1273d202e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Miller"}, "payload": {"as_of_content": "1976-04-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Miller", "scope_note": "Foundational third-party-doctrine case (bank records); remains good law. Carpenter v. United States (2018) declined to extend the third-party doctrine to cell-site location information but expressly did not overrule Miller.", "varies_by_point": false}}
```

### lake record — United States v. Miller

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Miller",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Miller",
    "case_name_short": "",
    "case_name_full": "United States v. Miller",
    "input_case_name": "United States v. Miller",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-04-21",
    "year": 1976,
    "docket": "74-1179",
    "cluster_id": 109433,
    "lead_opinion_id": 9426375,
    "sibling_ids": [
      109433,
      9426375,
      9426376,
      9426377
    ],
    "absolute_url": "/opinion/109433/united-states-v-miller/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "425 U.S. 435",
      "volume": "425",
      "reporter": "U.S.",
      "page": "435",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 1619",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "1619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "48 L. Ed. 2d 71",
        "volume": "48",
        "reporter": "L. Ed. 2d",
        "page": "71",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 A.F.T.R.2d (RIA) 1261",
        "volume": "37",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1261",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 148",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "148",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "425 U.S. 435",
        "volume": "425",
        "reporter": "U.S.",
        "page": "435",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 1619",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "1619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "48 L. Ed. 2d 71",
        "volume": "48",
        "reporter": "L. Ed. 2d",
        "page": "71",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 148",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "148",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 A.F.T.R.2d (RIA) 1261",
        "volume": "37",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1261",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "425 U.S. 435",
    "official_selection": {
      "court_class": "scotus",
      "selected": "425 U.S. 435",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-442",
      "page": null,
      "quote": "--- # United States v. Miller *425 U.S. 435 (1976)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background During an investigation into untaxed-whiskey offenses, federal agents obtained Miller's bank records \u2014 microfilmed checks, deposit slips, and financial statements \u2014 from two banks through grand-jury subpoenas. Miller moved to suppress the records, arguing the government's acquisition of his financial records from the banks was an unreasonable search and seizure of materials in which he had a Fourth Amendment interest. ## Issue Whether a bank depositor has a Fourth Amendment-protected expectation of privacy in financial records (cancelled checks, deposit slips, and statements) maintained by his bank, so that the government's acquisition of them constitutes a search or seizure as to the depositor. ## Rule No. The records are the bank's business records, and the depositor has no legitimate expectation of privacy in information he conveys to the bank.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-443",
      "page": null,
      "quote": "The depositor takes the risk, in revealing his affairs to another, that the information will be conveyed by that person to the Government.",
      "star_marker": "443",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15418,
      "fragment": "#:~:text=The%20depositor%20takes%20the%20risk%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-04-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Miller",
    "varies_by_point": false,
    "scope_note": "Foundational third-party-doctrine case (bank records); remains good law. Carpenter v. United States (2018) declined to extend the third-party doctrine to cell-site location information but expressly did not overrule Miller.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Lepage",
          "cluster_id": 9503197,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hoffman",
          "cluster_id": 10135310,
          "cite": [
            "321 Or. App. 330",
            "515 P.3d 912"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ajemian v. Yahoo!, Inc.",
          "cluster_id": 4434746,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Fulgiam",
          "cluster_id": 4389223,
          "cite": [
            "477 Mass. 20",
            "73 N.E.3d 798"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Zodhiates",
          "cluster_id": 7318729,
          "cite": [
            "166 F. Supp. 3d 328",
            "2016 U.S. Dist. LEXIS 55748",
            "2016 WL 1594558"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri v. Sandra G. Plunkett",
          "cluster_id": 2827918,
          "cite": [
            "473 S.W.3d 166",
            "2015 Mo. App. LEXIS 827"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jon Thomas Ford v. State",
          "cluster_id": 2719207,
          "cite": [
            "444 S.W.3d 171",
            "2014 Tex. App. LEXIS 9159",
            "2014 WL 4099731"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Augustine",
          "cluster_id": 6580805,
          "cite": [
            "467 Mass. 230",
            "4 N.E.3d 846",
            "2014 WL 901649",
            "2014 Mass. LEXIS 30"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Leotis B. Branigh, III",
          "cluster_id": 1034108,
          "cite": [
            "155 Idaho 404",
            "313 P.3d 732",
            "2013 WL 3718751",
            "2013 Ida. App. LEXIS 63"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane1_negative"
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
        "journal_ref": "United States v. Miller:lane2_top_cited"
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
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Maryland",
          "cluster_id": 110118,
          "cite": [
            "61 L. Ed. 2d 220",
            "99 S. Ct. 2577",
            "442 U.S. 735",
            "1979 U.S. LEXIS 134"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Martinez-Fuerte",
          "cluster_id": 109541,
          "cite": [
            "49 L. Ed. 2d 1116",
            "96 S. Ct. 3074",
            "428 U.S. 543",
            "1976 U.S. LEXIS 87"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nixon v. Administrator of General Services",
          "cluster_id": 109729,
          "cite": [
            "53 L. Ed. 2d 867",
            "97 S. Ct. 2777",
            "433 U.S. 425",
            "1977 U.S. LEXIS 24",
            "2 Media L. Rep. (BNA) 2025"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Andresen v. Maryland",
          "cluster_id": 109522,
          "cite": [
            "49 L. Ed. 2d 627",
            "96 S. Ct. 2737",
            "427 U.S. 463",
            "1976 U.S. LEXIS 78"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Ciraolo",
          "cluster_id": 111666,
          "cite": [
            "90 L. Ed. 2d 210",
            "106 S. Ct. 1809",
            "476 U.S. 207",
            "1986 U.S. LEXIS 154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
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
        "journal_ref": "United States v. Miller:lane2_top_cited"
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
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 622304,
          "cite": [
            "181 L. Ed. 2d 911",
            "132 S. Ct. 945",
            "565 U.S. 400",
            "2012 U.S. LEXIS 1063"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
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
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Payner",
          "cluster_id": 110317,
          "cite": [
            "65 L. Ed. 2d 468",
            "100 S. Ct. 2439",
            "447 U.S. 727",
            "1980 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
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
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Campbell",
          "cluster_id": 4463634,
          "cite": [
            "2018 COA 5",
            "425 P.3d 1163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ferguson v. City of Charleston",
          "cluster_id": 118414,
          "cite": [
            "149 L. Ed. 2d 205",
            "121 S. Ct. 1281",
            "532 U.S. 67",
            "2001 U.S. LEXIS 2460",
            "2001 Daily Journal DAR 2839",
            "2001 Colo. J. C.A.R. 1427",
            "14 Fla. L. Weekly Fed. S 152",
            "69 U.S.L.W. 4184"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Kennedy",
          "cluster_id": 1142841,
          "cite": [
            "666 P.2d 1316",
            "295 Or. 260",
            "1983 Ore. LEXIS 1311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Warshak",
          "cluster_id": 181032,
          "cite": [
            "631 F.3d 266",
            "2010 U.S. App. LEXIS 25415",
            "2010 WL 5071766"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Moore",
          "cluster_id": 1147295,
          "cite": [
            "782 P.2d 91",
            "109 N.M. 119"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hunt",
          "cluster_id": 2285004,
          "cite": [
            "450 A.2d 952",
            "91 N.J. 338",
            "1982 N.J. LEXIS 2189"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hardy",
          "cluster_id": 1494781,
          "cite": [
            "963 S.W.2d 516",
            "1997 WL 716775"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Sell",
          "cluster_id": 1462347,
          "cite": [
            "470 A.2d 457",
            "504 Pa. 46",
            "1983 Pa. LEXIS 792"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cecil Dwayne Evans, Arnold Gene Tate, and Charles Edward Gent, Jr.",
          "cluster_id": 354019,
          "cite": [
            "572 F.2d 455"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hempele",
          "cluster_id": 1435469,
          "cite": [
            "576 A.2d 793",
            "120 N.J. 182",
            "1990 N.J. LEXIS 92"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. DeJohn",
          "cluster_id": 2055341,
          "cite": [
            "403 A.2d 1283",
            "486 Pa. 32",
            "1979 Pa. LEXIS 572"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Miller:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109433 OR 9426375 OR 9426376 OR 9426377) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjc5MjM4NDAwMDAwJnM9MTUwODEyJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109433+OR+9426375+OR+9426376+OR+9426377%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 12,
        "triage_snippet_classified": 188
      },
      "lane2_top_cited": {
        "query": "cites:(109433 OR 9426375 OR 9426376 OR 9426377)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTQmcz0yNDQ2ODgyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109433+OR+9426375+OR+9426376+OR+9426377%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109433 OR 9426375 OR 9426376 OR 9426377)",
        "reviewed": 29,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 29,
        "triage_read": 1,
        "triage_snippet_classified": 28
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109433 OR 9426375 OR 9426376 OR 9426377)",
    "indexed_citing_opinions": 766,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109433,
        "count": 639,
        "count_source": "search"
      },
      {
        "opinion_id": 9426375,
        "count": 148,
        "count_source": "search"
      },
      {
        "opinion_id": 9426376,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426377,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1198,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-miller.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5OTgyNzQmcz0xMDEyNDY0MCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109433+OR+9426375+OR+9426376+OR+9426377%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109433,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 104239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 108236,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 108650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 109005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 109257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 109380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 109402,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 320663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 1172381,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109433,
        "cited_id": 2301022,
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
    "date_created": "2026-07-06T01:42:56Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:43:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:43:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:47:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:43:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Miller

```
<opinion type="majority">
<author id="b506-9">Mr. Justice Powell</author>
<p id="AvQ">delivered the opinion of the Court.</p>
<p id="b506-10">Respondent was convicted of possessing an unregistered still, carrying on the business of a distiller without giving bond and with intent to defraud the Government of whiskey tax, possessing 175 gallons of whiskey upon which no taxes had been paid, and conspiring to defraud the United States of tax revenues. <span class="citation no-link">26 U. S. C. §§ 5179</span>, 5205, 5601 <em>et seq.; </em><span class="citation no-link">18 U. S. C. § 371</span>. Prior to trial respondent moved to suppress copies of checks and other bank records obtained by means of allegedly defective subpoenas <em>duces tecum </em>served upon two banks at which he had accounts. The records had been maintained by the banks in compliance with the requirements of the Bank Secrecy Act of 1970, <span class="citation no-link">84 Stat. 1114</span>, 12 U. S. C. § 1829b (d).</p>
<p id="b507-4"><page-number citation-index="1" label="437">*437</page-number>The District Court overruled respondent’s motion to suppress, and the evidence was admitted. The Court of Appeals for the Fifth Circuit reversed on the ground that a depositor’s Fourth Amendment rights are violated when bank records maintained pursuant to the Bank Secrecy Act are obtained by means of a defective subpoena. It held that any evidence so obtained must be suppressed. Since we find that respondent had no pro-tectable Fourth Amendment interest in the subpoenaed documents, we reverse the decision below.</p>
<p id="b507-5">I</p>
<p id="b507-6">On December 18, 1972, in response to an informant’s tip, a deputy sheriff from Houston County, Ga., stopped a van-type truck occupied by two of respondent’s alleged co-conspirators. The truck contained distillery apparatus and raw material. On January 9, 1973, a fire broke out in a Kathleen, Ga., warehouse rented to respondent. During the blaze firemen and sheriff department officials discovered a 7,500-gallon-eapacity distillery, 175 gallons of non-tax-paid whiskey, and related paraphernalia.</p>
<p id="b507-7">Two weeks later agents from the Treasury Department’s Alcohol, Tobacco and Firearms Bureau presented grand jury subpoenas issued in blank by the clerk of the District Court, and completed by the United States Attorney’s office, to the presidents of the Citizens &amp; Southern National Bank of Warner Robins and the Bank of Byron, where respondent maintained accounts. The subpoenas required the two presidents to appear on January 24, 1973, and to produce</p>
<blockquote id="b507-8">“all records of accounts, <em>i. e., </em>savings, checking, loan or otherwise, in the name of Mr. Mitch Miller [respondent], 3859 Mathis Street, Macon, Ga. and/or Mitch Miller Associates, 100 Executive <page-number citation-index="1" label="438">*438</page-number>Terrace, Warner Robins, Ga., from October 1, 1972, through the present date [January 22, 1973, in the case of the Bank of Byron, and January 23, 1973, in the case of the Citizens &amp; Southern National Bank of Warner Robins]</blockquote>
<p id="b508-5">The banks did not advise respondent that the subpoenas had been served but ordered their employees to make the records available and to provide copies .of any documents the agents desired. At the Bank of Byron, an agent was shown microfilm records of the relevant account and provided with copies of one deposit slip and one or two checks. At the Citizens &amp; Southern National Bank microfilm records also were shown to the agent, and he was given copies-of the records of respondent's account during the applicable period. These included all checks, deposit slips, two financial statements, and three monthly statements. The bank presidents were then told that it would not be necessary to appear in person before the grand jury.</p>
<p id="b508-6">The grand jury met on February 12, 1973, 19 days after the return date on the subpoenas. Respondent and four others were indicted. The overt acts alleged to have been committed in furtherance of the conspiracy included three financial transactions — the rental by respondent of the van-type truck, the purchase by respondent of radio equipment, and the purchase by respondent of a quantity of sheet metal and metal pipe. The record does not indicate whether any of the bank records were in fact presented to the grand jury. They were used in the investigation and provided “one or two" investigatory leads. Copies of the checks also were introduced at trial to establish the overt acts described above.</p>
<p id="b508-7">In his motion to suppress, denied by the District Court, respondent contended that the bank documents were illegally seized. It was urged that the subpoenas were <page-number citation-index="1" label="439">*439</page-number>defective because they were issued by the United States Attorney rather than a court, no return was made to a court, and the subpoenas were returnable on a date when the grand jury was not in session. The Court of Appeals reversed. <span class="citation" data-id="320663"><a href="/opinion/320663/united-states-v-mitchell-miller-susan-mcduffie-weeks-and-john-henry/" aria-description="Citation for case: United States v. Mitchell Miller, Susan McDuffie Weeks,...">500 F. 2d 751</a></span> (1974). Citing the prohibition in <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#622" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 622</a></span> (1886), against “compulsory production of a man’s private papers to establish a criminal charge against him,” the court held that the Government had improperly circumvented <em>Boyd’s </em>protections of respondent’s Fourth Amendment right against “unreasonable searches and seizures” by “first requiring a third party bank to copy all of its depositors’ personal checks and then, with an improper invocation of legal process, calling upon the bank to allow inspection and reproduction of those copies.” <span class="citation" data-id="320663"><a href="/opinion/320663/united-states-v-mitchell-miller-susan-mcduffie-weeks-and-john-henry/#757" aria-description="Citation for case: United States v. Mitchell Miller, Susan McDuffie Weeks,...">500 F. 2d, at 757</a></span>. The court acknowledged that the recordkeeping requirements of the Bank Secrecy Act had been held to be constitutional on their face in <em>California Bankers Assn. </em>v. <em>Shultz, </em><span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S. 21</a></span> (1974), but noted that access to the records was to be controlled by “existing legal process.” See <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#52" aria-description="Citation for case: California Bankers Assn. v. Shultz"><em>id., </em>at 52</a></span>. The subpoenas issued here were found not to constitute adequate “legal process.” The fact that the bank officers cooperated voluntarily was found to be irrelevant, for “he whose rights are threatened by the improper disclosure here was a bank depositor, not a bank official.” <span class="citation" data-id="320663"><a href="/opinion/320663/united-states-v-mitchell-miller-susan-mcduffie-weeks-and-john-henry/#758" aria-description="Citation for case: United States v. Mitchell Miller, Susan McDuffie Weeks,...">500 F. 2d, at 758</a></span>.</p>
<p id="b509-5">The Government contends that the Court of Appeals erred in three respects: (i) in finding that respondent had the Fourth Amendment interest necessary to entitle him to challenge the validity of the subpoenas <em>duces tecum </em>through his motion to suppress; (ii) in holding that the subpoenas were defective; and (iii) in determining that suppression of the evidence obtained was the appropriate remedy if a constitutional violation did take place.</p>
<p id="b510-4"><page-number citation-index="1" label="440">*440</page-number>We find that there was no intrusion into any area in which respondent had a protected Fourth Amendment interest and that the District Court therefore correctly denied respondent’s motion to suppress. Because we reverse the decision of the Court of Appeals on that ground alone, we do not reach the Government’s latter two contentions.</p>
<p id="b510-5">II</p>
<p id="b510-6">In <em>Hoffa </em>v. <em>United States, </em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#301" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 301-302</a></span> (1966), the Court said that “no interest legitimately protected by the Fourth Amendment” is implicated by governmental investigative activities unless there is an intrusion into a zone of privacy, into “the security a man relies upon when he places himself or his property within a constitutionally protected area.” The Court of Appeals, as noted above, assumed that respondent had the necessary Fourth Amendment interest, pointing to the language in <em>Boyd </em>v. <em>United States, supra, at </em>622, which describes that Amendment’s protection against the “compulsory production of a man’s private papers.”<footnotemark>1</footnotemark> We think that the Court of Appeals erred in finding the subpoenaed documents to fall within a protected zone of privacy.</p>
<p id="b510-7">On their face, the documents subpoenaed here are not respondent’s “private papers.” Unlike the claimant in <em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>, </em>respondent can assert neither ownership nor possession. Instead, these are the business records of the banks. As we said in <em>California Bankers Assn. </em>v. <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#48" aria-description="Citation for case: California Bankers Assn. v. Shultz"><em>Shultz, supra, </em>at 48-49</a></span>, “[blanks are . . . not . . . neutrals in transactions involving negotiable instruments, but parties to the instruments with a substantial stake in their continued availability and acceptance.” The records of re<page-number citation-index="1" label="441">*441</page-number>spondent’s accounts, like “all of the records [which are required to be kept pursuant to the Bank Secrecy Act,] pertain to transactions to which the bank was itself a party.” <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#52" aria-description="Citation for case: California Bankers Assn. v. Shultz"><em>Id., </em>at 52</a></span>.</p>
<p id="b511-4">Respondent argues, however, that the Bank Secrecy Act introduces a factor that makes the subpoena in this case the functional equivalent of a search and seizure of the depositor’s “private papers.” We have held, in <em>California Bankers Assn. </em>v. <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#54" aria-description="Citation for case: California Bankers Assn. v. Shultz"><em>Shultz, supra, </em>at 54</a></span>, that the mere maintenance of records pursuant to the requirements of the Act “invade [s] no Fourth Amendment right of any depositor.” But respondent contends that the combination of the recordkeeping requirements of the Act and the issuance of a subpoena<footnotemark>2</footnotemark> to obtain those records permits the Government to circumvent the requirements of the Fourth Amendment by allowing it to obtain a depositor’s private records without complying with the legal requirements that would be applicable had it proceeded against him directly.<footnotemark>3</footnotemark> Therefore, we must address the question whether the compulsion embodied in the Bank Secrecy Act as exercised in this case creates a Fourth Amendment interest in the depositor where none existed before. This question was expressly re<page-number citation-index="1" label="442">*442</page-number>served in <em>California Bankers Assn., supra, </em>at 53-54, and n. 24.</p>
<p id="b512-5">Respondent urges that he has a Fourth Amendment interest in the records kept by the banks because they are merely copies of personal records that were made available to the banks for a limited purpose and in which he has a reasonable expectation of privacy. He relies on this Court’s statement in <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 353</a></span> (1967), quoting <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#304" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 304</a></span> (1967), that “we have . . . departed from the narrow view” that “ 'property interests control the right of the Government to search and seize,’ ” and that a “search and seizure” become unreasonable when the Government’s activities violate “the privacy upon which [a person] justifiably reliefs].” But in <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>the Court also stressed that “[w]hat a person knowingly exposes to the public ... is not a subject of Fourth Amendment protection.” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S., at 351</a></span>. We must examine the nature of the particular documents sought to be protected in order to determine whether there is a legitimate “expectation of privacy” concerning their contents. Cf. <em>Couch </em>v. <em>United States, </em><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#335" aria-description="Citation for case: Couch v. United States">409 U. S. 322, 335</a></span> (1973).</p>
<p id="b512-6">Even if we direct our attention to the original checks and deposit slips, rather than to the microfilm copies actually viewed and obtained by means of the subpoena, we perceive no legitimate “expectation of privacy” in their contents. The checks are not confidential communications but negotiable instruments to be used in commercial transactions. All of the documents obtained, including financial statements and deposit slips, contain only information voluntarily conveyed to the banks and exposed to their employees in the ordinary course of business. The lack of any legitimate expectation of privacy concerning the information kept in bank records was assumed by Congress in enacting the Bank Secrecy Act, the expressed purpose of which is to require records <page-number citation-index="1" label="443">*443</page-number>to be maintained because they “have a high degree of usefulness in criminal, tax, and regulatory investigations and proceedings.” 12 U. S. C. § 1829b (a) (1). Cf. <em>Couch </em>v. <em>United States, supra, </em>at 335.</p>
<p id="b513-5">The depositor takes the risk, in revealing his affairs to another, that the information will be conveyed by that person to the Government. <em>United States </em>v. <em>White, </em><span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#751" aria-description="Citation for case: United States v. White">401 U. S. 745, 751-752</a></span> (1971). This Court has held repeatedly that the Fourth Amendment does not prohibit the obtaining of information revealed to a third party and conveyed by him to Government authorities, even if the information is revealed on the assumption that it will be used only for a limited purpose and the confidence placed in the third party will not be betrayed. <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#752" aria-description="Citation for case: United States v. White"><em>Id., </em>at 752</a></span>; <em>Hoffa </em>v. <em>United States, </em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#302" aria-description="Citation for case: Hoffa v. United States">385 U. S., at 302</a></span>; <em>Lopez </em>v. <em>United States, </em><span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">373 U. S. 427</a></span> (1963).<footnotemark>4</footnotemark></p>
<p id="b513-6">This analysis is not changed by the mandate of the Bank Secrecy Act that records of depositors' transactions be maintained by banks. In <em>California Bankers Assn. </em>v. <em>Shultz, </em><span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#52" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S., at 52-53</a></span>, we rejected the contention that banks, when keeping records of their depositors' transactions pursuant to the Act, are acting solely as agents of the Government. But, even if the banks could be said to have been acting solely as Government agents in transcribing the necessary information and complying without protest<footnotemark>5</footnotemark> with the requirements of the subpoenas, there would be no intrusion upon the depositors' Fourth Amendment rights. See <em>Osborn </em>v. <em>United States, </em><span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/" aria-description="Citation for case: Osborn v. United States">385 U. S. 323</a></span> (1966); <em>Lewis </em>v. <em>United States, </em><span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/" aria-description="Citation for case: Lewis v. United States">385 U. S. 206</a></span> (1966).</p>
<p id="b514-4"><page-number citation-index="1" label="444">*444</page-number>Ill</p>
<p id="b514-5">Since no Fourth Amendment interests of the depositor are implicated here, this case is governed by the general rule that the issuance of a subpoena to a third party to obtain the records of that party does not violate the rights of a defendant, even if a criminal prosecution is contemplated at the time the subpoena is issued. <em>California Bankers Assn. </em>v. <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#53" aria-description="Citation for case: California Bankers Assn. v. Shultz"><em>Shultz, supra, </em>at 53</a></span>; <em>Donaldson </em>v. <em>United States, </em><span class="citation" data-id="9424399"><a href="/opinion/108236/donaldson-v-united-states/#537" aria-description="Citation for case: Donaldson v. United States">400 U. S. 517, 537</a></span> (1971) (Douglas, J., concurring). Under these principles, it was firmly settled, before the passage of the Bank Secrecy Act, that an Internal Revenue Service summons directed to a third-party bank does not violate the Fourth Amendment rights of a depositor under investigation. See <em>First National Bank of Mobile </em>v. <em>United States, </em><span class="citation multiple-matches"><a href="/c/U.%20S./267/576/">267 U. S. 576</a></span> (1925), aff’g <span class="citation" data-id="8833975"><a href="/opinion/8848641/united-states-v-first-nat-bank/" aria-description="Citation for case: United States v. First Nat. Bank">295 F. 142</a></span> (SD Ala. 1924). See also <em>California Bankers Assn. </em>v. <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#53" aria-description="Citation for case: California Bankers Assn. v. Shultz"><em>Shultz, supra, </em>at 53</a></span>; <em>Donaldson </em>v. <em>United States, supra, </em>at 522.</p>
<p id="b514-6">Many banks traditionally kept permanent records of their depositors’ accounts, although not all banks did so and the practice was declining in recent years. By requiring that such records be kept by all banks, the Bank Secrecy Act is not a novel means designed to circumvent established Fourth Amendment rights. It is merely an attempt to facilitate the use of a proper and longstanding law enforcement technique by insuring that records are available when they are needed.<footnotemark>6</footnotemark></p>
<p id="b515-4"><page-number citation-index="1" label="445">*445</page-number>We hold that the District Court correctly denied respondent’s motion to suppress, since he possessed no Fourth Amendment interest that could be vindicated by a challenge to the subpoenas.</p>
<p id="b515-5">IV</p>
<p id="b515-6">Respondent contends not only that the subpoenas <em>duces tecum </em>directed against the banks infringed his Fourth Amendment rights, but that a subpoena issued to a bank to obtain records maintained pursuant to the Act is subject to more stringent Fourth Amendment requirements than is the ordinary subpoena. In making this assertion he relies on our statement in <em>California Bankers Assn., supra, </em>at 52, that access to the records maintained by banks under the Act is to be controlled by "existing legal process.” <footnotemark>7</footnotemark></p>
<p id="b515-7">In <em>Oklahoma Press Pub. Co. </em>v. <em>Walling, </em><span class="citation" data-id="9419755"><a href="/opinion/104239/oklahoma-press-publishing-co-v-walling/#208" aria-description="Citation for case: Oklahoma Press Publishing Co. v. Walling">327 U. S. 186, 208</a></span> (1946), the Court said that “the Fourth [Amendment], if applicable [to subpoenas for the production of business records and papers], at the most guards against abuse only by way of too much indefiniteness or breadth in the things required to be 'particularly described,’ if also the inquiry is one the demanding <page-number citation-index="1" label="446">*446</page-number>agency is authorized by law to make and the materials specified are relevant.” See also <em>United States </em>v. <em>Dionisio, </em><span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#11" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1, 11-12</a></span> (1973). Respondent, citing <em>United States </em>v. <em>United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297</a></span> (1972), in which we discussed the application of the warrant requirements of the Fourth Amendment to domestic security surveillance through electronic eavesdropping, suggests that greater judicial scrutiny, equivalent to that required for a search warrant, is necessary when a subpoena is to be used to obtain bank records of a depositor’s account. But in <em>California Bankers Assn., </em><span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#52" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S., at 52</a></span>, we emphasized only that access to the records was to be in accordance with “existing legal process.” There was no indication that a new rule was to be devised, or that the traditional distinction between a search warrant and a subpoena would not be recognized.<footnotemark>8</footnotemark></p>
<p id="b516-5">In any event, for the reasons stated above, we hold that respondent lacks the requisite Fourth Amendment interest to challenge the validity of the subpoenas.<footnotemark>9</footnotemark></p>
<p id="b516-6">V</p>
<p id="b516-7">The judgment of the Court of Appeals is reversed. The court deferred decision on whether the trial court had improperly overruled respondent’s motion to suppress <page-number citation-index="1" label="447">*447</page-number>distillery apparatus and raw material seized from a rented truck. We remand for disposition of that issue.</p>
<p id="b517-5">
<em>So ordered.</em>
</p>
<footnote label="1">
<p id="b510-8"> The Fourth Amendment implications of <em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span> </em>as it applies to subpoenas <em>duces tecum </em>have been undercut by more recent cases. <em>Fisher </em>v. <em>United States, ante, at </em>407-409. <em>See infra, </em>at 445-446.</p>
</footnote>
<footnote label="2">
<p id="b511-5"> Respondent appears to contend that a depositor’s Fourth Amendment interest comes into play only when a <em>defective </em>subpoena is used to obtain records kept pursuant to the Act. We see no reason why the existence of a Fourth Amendment interest turns on whether the subpoena is defective. Therefore, we do not limit our consideration to the situation in which there is an alleged defect in the subpoena served on the bank.</p>
</footnote>
<footnote label="3">
<p id="b511-6"> It is not clear whether respondent refers to attempts to obtain private documents through a subpoena issued directly to the depositor or through a search pursuant to a warrant. The question whether personal business records may be seized pursuant to a valid warrant is before this Court in No. 74-1646, <em>Andresen </em>v. <em>Maryland, </em>cert. granted, <span class="citation multiple-matches"><a href="/c/U.%20S./423/822/">423 U. S. 822</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b513-7"> We do not address here the question of evidentiary privileges, such as that protecting communications between an attorney and his client. Cf. <em>Fisher </em>v. <em>United States, ante, </em>at 403-405.</p>
</footnote>
<footnote label="5">
<p id="b513-8"> Nor did the banks notify respondent, a neglect without legal consequences here, however unattractive it may be.</p>
</footnote>
<footnote label="6">
<p id="b514-7"> Respondent does not contend that the subpoenas infringed upon his First Amendment rights. There was no blanket reporting requirement of the sort we addressed in <em>Buckley </em>v. <em>Valeo, </em><span class="citation" data-id="109380"><a href="/opinion/109380/buckley-v-valeo/#60" aria-description="Citation for case: Buckley v. Valeo">424 U. S. 1, 60-84</a></span> (1976), nor any allegation of an improper inquiry into protected associational activities of the sort presented in <em>Eastland </em>v. <em>United States Servicemen’s Fund, </em><span class="citation" data-id="9426086"><a href="/opinion/109257/eastland-v-united-states-servicemens-fund/" aria-description="Citation for case: Eastland v. United States Servicemen&#x27;s Fund">421 U. S. 491</a></span> (1975).</p>
<p id="APj">We are not confronted with a situation in which the Government, through “unreviewed executive discretion,” has made a wide-ranging <page-number citation-index="1" label="445">*445</page-number>inquiry that unnecessarily "touch[es] upon intimate areas of an individual’s personal affairs.” <em>California Bankers </em>Assn. v. <em>Shultz, </em><span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#78" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S., at 78-79</a></span> (Powell, J., concurring). Here the Government has exercised its powers through narrowly directed subpoenas <em>duces tecum </em>subject to the legal restraints attendant to such process. See Part IV, <em>infra.</em></p>
</footnote>
<footnote label="7">
<p id="b515-14"> This case differs from <em>Burrows </em>v. <em>Superior Court, 13 </em>Cal. 3d 238, <span class="citation" data-id="1172381"><a href="/opinion/1172381/burrows-v-superior-court/" aria-description="Citation for case: Burrows v. Superior Court">529 P. 2d 590</a></span> (1974), relied on by Mr. Justice Brennan in dissent, in that the bank records of respondent’s accounts were furnished in response to “compulsion by legal process” in the form of subpoenas <em>duces tecum. </em>The court in <em><span class="citation" data-id="1172381"><a href="/opinion/1172381/burrows-v-superior-court/" aria-description="Citation for case: Burrows v. Superior Court">Burrows</a></span> </em>found it “significant . . . that the bank [in that case) provided the statements to the police in response to an informal oral request for information.” <span class="citation" data-id="1172381"><a href="/opinion/1172381/burrows-v-superior-court/#243" aria-description="Citation for case: Burrows v. Superior Court"><em>Id., </em>at 243</a></span>, <span class="citation" data-id="1172381"><a href="/opinion/1172381/burrows-v-superior-court/#593" aria-description="Citation for case: Burrows v. Superior Court">529 P. 2d, at 593</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b516-8"> A subpoena <em>duces tecum </em>issued to obtain records is subject to nó more stringent Fourth Amendment requirements than is the ordinary subpoena. A search warrant, in contrast, is issuable only pursuant to prior judicial approval and authorizes Government officers to seize evidence without requiring enforcement through the courts. See <em>United States </em>v. <em>Dionisio, </em><span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#9" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1, 9-10</a></span> (1973).</p>
</footnote>
<footnote label="9">
<p id="b516-9"> There is no occasion for us to address whether the subpoenas complied with the requirements outlined in <em>Oklahoma Press Pub. Co. </em>v. <em>Walling, </em><span class="citation" data-id="9419755"><a href="/opinion/104239/oklahoma-press-publishing-co-v-walling/" aria-description="Citation for case: Oklahoma Press Publishing Co. v. Walling">327 U. S. 186</a></span> (1946). The banks upon which they were served did not contest their validity.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Montoya de Hernandez.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Montoya de Hernandez"
type: case
citation: "473 U.S. 531 (1985)"
parallel_cite: "105 S. Ct. 3304; 87 L. Ed. 2d 381; 53 U.S.L.W. 5048"
neutral_cite: 1985 U.S. LEXIS 120
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-07-01
docket: 84-755
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-07-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Montoya de Hernandez
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111509/united-states-v-montoya-de-hernandez/"
  cluster_id: 111509
  opinion_id: 9430181
  identity_checked: true
homes:
  - page: "[[Border Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Flores-Montano]]", "[[United States v. Martinez-Fuerte]]", "[[Almeida-Sanchez v. United States]]", "[[Terry v. Ohio]]", "[[United States v. Cortez]]"]
aliases: ["United States v. Rosa Elvira Montoya de Hernandez"]
tags: ["case", "fourth-amendment", "border-searches", "reasonable-suspicion", "alimentary-canal-smuggling", "detention"]
holding: "The prolonged detention of a suspected alimentary-canal (balloon) smuggler at the border is reasonable when customs officers have…"
lake:
  record_id: United States v. Montoya de Hernandez
  status: verified
  projected_at: 2026-07-06
---

# United States v. Montoya de Hernandez

*473 U.S. 531 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Rosa Elvira Montoya de Hernandez arrived at Los Angeles International Airport on a flight from Bogotá, Colombia. Customs inspectors found her travel story implausible — frequent short trips, about $5,000 cash but no checks or credit cards, no hotel reservations, and minimal luggage — and a strip search revealed a firm fullness in her abdomen and two pairs of underpants lined with a paper towel. Suspecting she was a "balloon swallower," inspectors detained her for roughly 16 hours awaiting a monitored bowel movement after she declined an x-ray; a court order eventually authorized an examination that produced 88 cocaine-filled balloons from her alimentary canal. The Ninth Circuit reversed her conviction, requiring a "clear indication" of smuggling.

## Issue
What level of suspicion justifies detaining an incoming international traveler at the border, beyond a routine customs search, on suspicion of alimentary-canal smuggling — and whether the prolonged detention here was reasonable.

## Rule
Reasonable suspicion governs such nonroutine border detentions of persons. "We hold that the detention of a traveler at the border, beyond the scope of a routine customs search and inspection, is justified at its inception if customs agents, considering all the facts surrounding the traveler and her trip, reasonably suspect that the traveler is smuggling contraband in her alimentary canal." — 473 U.S. at 541. ^pin-541

Officials must have a "particularized and objective basis for suspecting the particular person" of such smuggling, not an "inchoate and unparticularized suspicion or 'hunch.'"

The detention may last as long as is reasonably necessary to confirm or dispel the suspicion: "in the presence of articulable suspicion of smuggling in her alimentary canal, the customs officers were not required by the Fourth Amendment to pass respondent and her 88 cocaine-filled balloons into the interior. Her detention for the period of time necessary to either verify or dispel the suspicion was not unreasonable." — *Id.* at 544. ^pin-544

## Application
On these facts the inspectors had reasonable suspicion and the detention was reasonable. Montoya's implausible itinerary, her cash without ordinary financial instruments, the absence of luggage and reservations, the firm abdominal fullness, and Inspector Talamantes's experience apprehending dozens of balloon swallowers on that very flight supplied a particularized, objective basis to suspect alimentary-canal smuggling — far more than a hunch. Because such smuggling gives no external signs and cannot be detected by a frisk or strip search, the officers were not obliged to let her pass into the country; detaining her until her bodily processes could verify or dispel the suspicion was reasonable, and the length and discomfort of the detention "resulted solely from the method by which she chose to" smuggle and her refusal of the x-ray alternative.

## Conclusion
Reasonable suspicion justified the nonroutine border detention, and its duration was reasonable; the Ninth Circuit's reversal of the conviction was itself reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Montoya de Hernandez* sets the reasonable-suspicion standard for nonroutine border *detentions of persons*; [[United States v. Flores-Montano]] later confined that "routine vs. non-routine" analysis to person searches and held it inapplicable to *vehicle* searches at the border. It draws the reasonable-suspicion standard from the [[Terry v. Ohio]] / [[United States v. Cortez]] line.

## Appears on
- [[Border Searches]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Montoya de Hernandez*, 473 U.S. 531 (1985) — https://www.courtlistener.com/opinion/111509/united-states-v-montoya-de-hernandez/ — pinpoints: 541, 544.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0b0a9b0d83474895", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Montoya de Hernandez"}, "payload": {"all": [{"cite": "473 U.S. 531", "page": "531", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "473"}, {"cite": "105 S. Ct. 3304", "page": "3304", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "105"}, {"cite": "87 L. Ed. 2d 381", "page": "381", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "87"}, {"cite": "1985 U.S. LEXIS 120", "page": "120", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1985"}, {"cite": "53 U.S.L.W. 5048", "page": "5048", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "53"}], "display": "473 U.S. 531", "official": {"cite": "473 U.S. 531", "page": "531", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "473"}, "official_selection_present": true, "record_id": "United States v. Montoya de Hernandez"}}
{"assertion_id": "2f16801c6fce78a6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-544", "record_id": "United States v. Montoya de Hernandez"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-544", "pinpoint_status": "slip-only", "quote": "The detention may last as long as is reasonably necessary to confirm or dispel the suspicion:", "quote_fidelity": "mismatch", "record_id": "United States v. Montoya de Hernandez", "star_marker": null}}
{"assertion_id": "b38591e79540d046", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-541", "record_id": "United States v. Montoya de Hernandez"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-541", "pinpoint_status": "slip-only", "quote": "of smuggling. ## Issue What level of suspicion justifies detaining an incoming international traveler at the border, beyond a routine customs search, on suspicion of alimentary-canal smuggling — and whether the prolonged detention here was reasonable. ## Rule Reasonable suspicion governs such nonroutine border detentions of persons.", "quote_fidelity": "mismatch", "record_id": "United States v. Montoya de Hernandez", "star_marker": null}}
{"assertion_id": "73d1b7201664af05", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Montoya de Hernandez"}, "payload": {"as_of_content": "1985-07-01", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Montoya de Hernandez", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Montoya de Hernandez

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Montoya de Hernandez",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Montoya De Hernandez",
    "case_name_short": "Hernandez",
    "case_name_full": "UNITED STATES v. MONTOYA De HERNANDEZ",
    "input_case_name": "United States v. Montoya de Hernandez",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-07-01",
    "year": 1985,
    "docket": "84-755",
    "cluster_id": 111509,
    "lead_opinion_id": 9430181,
    "sibling_ids": [
      111509,
      9430181,
      9430182,
      9430183
    ],
    "absolute_url": "/opinion/111509/united-states-v-montoya-de-hernandez/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "473 U.S. 531",
      "volume": "473",
      "reporter": "U.S.",
      "page": "531",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 3304",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "3304",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 L. Ed. 2d 381",
        "volume": "87",
        "reporter": "L. Ed. 2d",
        "page": "381",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 5048",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "5048",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 120",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "120",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "473 U.S. 531",
        "volume": "473",
        "reporter": "U.S.",
        "page": "531",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 3304",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "3304",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 L. Ed. 2d 381",
        "volume": "87",
        "reporter": "L. Ed. 2d",
        "page": "381",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 120",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "120",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 5048",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "5048",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "473 U.S. 531",
    "official_selection": {
      "court_class": "scotus",
      "selected": "473 U.S. 531",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-541",
      "page": null,
      "quote": "of smuggling. ## Issue What level of suspicion justifies detaining an incoming international traveler at the border, beyond a routine customs search, on suspicion of alimentary-canal smuggling \u2014 and whether the prolonged detention here was reasonable. ## Rule Reasonable suspicion governs such nonroutine border detentions of persons.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-544",
      "page": null,
      "quote": "The detention may last as long as is reasonably necessary to confirm or dispel the suspicion:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-07-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Montoya de Hernandez",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Banks",
          "cluster_id": 6658146,
          "cite": [
            "434 P.3d 361",
            "364 Or. 332"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Martinez",
          "cluster_id": 4574288,
          "cite": [
            "910 F.3d 1309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Caballero",
          "cluster_id": 7319742,
          "cite": [
            "178 F. Supp. 3d 1008",
            "2016 U.S. Dist. LEXIS 51132",
            "2016 WL 1546731"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Levy",
          "cluster_id": 8442407,
          "cite": [
            "803 F.3d 120",
            "2015 U.S. App. LEXIS 17154",
            "2015 WL 5692332"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cotterman",
          "cluster_id": 213651,
          "cite": [
            "637 F.3d 1068",
            "2011 U.S. App. LEXIS 6483",
            "2011 WL 1137302"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Stefan Irving",
          "cluster_id": 794720,
          "cite": [
            "452 F.3d 110",
            "2006 U.S. App. LEXIS 16077",
            "2006 WL 1735582"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Figg v. Schroeder",
          "cluster_id": 2967701,
          "cite": [
            "312 F.3d 625",
            "2002 WL 31689413"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane1_negative"
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
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ashcroft v. al-Kidd",
          "cluster_id": 217703,
          "cite": [
            "179 L. Ed. 2d 1149",
            "131 S. Ct. 2074",
            "563 U.S. 731",
            "2011 U.S. LEXIS 4021"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Skinner v. Railway Labor Executives' Assn.",
          "cluster_id": 112219,
          "cite": [
            "103 L. Ed. 2d 639",
            "109 S. Ct. 1402",
            "489 U.S. 602",
            "1989 U.S. LEXIS 1568",
            "4 I.E.R. Cas. (BNA) 224",
            "1989 CCH OSHD 28,476",
            "57 U.S.L.W. 4324",
            "13 OSHC (BNA) 2065",
            "130 L.R.R.M. (BNA) 2857",
            "49 Empl. Prac. Dec. (CCH) 38,791"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vernonia School District 47J v. Acton",
          "cluster_id": 117964,
          "cite": [
            "132 L. Ed. 2d 564",
            "115 S. Ct. 2386",
            "515 U.S. 646",
            "1995 U.S. LEXIS 4275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Acevedo",
          "cluster_id": 112608,
          "cite": [
            "114 L. Ed. 2d 619",
            "111 S. Ct. 1982",
            "500 U.S. 565",
            "1991 U.S. LEXIS 3016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Indianapolis v. Edmond",
          "cluster_id": 118391,
          "cite": [
            "148 L. Ed. 2d 333",
            "121 S. Ct. 447",
            "531 U.S. 32",
            "2000 U.S. LEXIS 8084",
            "69 U.S.L.W. 4009",
            "14 Fla. L. Weekly Fed. S 9",
            "2000 Colo. J. C.A.R. 6401",
            "2000 Cal. Daily Op. Serv. 9549"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
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
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County of Allegheny v. American Civil Liberties Union",
          "cluster_id": 112331,
          "cite": [
            "106 L. Ed. 2d 472",
            "109 S. Ct. 3086",
            "492 U.S. 573",
            "1989 U.S. LEXIS 3468",
            "57 U.S.L.W. 5045"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Verdugo-Urquidez",
          "cluster_id": 112382,
          "cite": [
            "108 L. Ed. 2d 222",
            "110 S. Ct. 1056",
            "494 U.S. 259",
            "1990 U.S. LEXIS 1175",
            "1990 WL 16772"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henry v. Purnell",
          "cluster_id": 220962,
          "cite": [
            "652 F.3d 524",
            "2011 U.S. App. LEXIS 14391",
            "2011 WL 2725816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McCullough",
          "cluster_id": 2594742,
          "cite": [
            "6 P.3d 774",
            "2000 Colo. J. C.A.R. 3950",
            "2000 Colo. LEXIS 817",
            "2000 WL 870824"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Oody",
          "cluster_id": 1740610,
          "cite": [
            "823 S.W.2d 554",
            "1991 Tenn. Crim. App. LEXIS 405"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McGee v. State",
          "cluster_id": 1960022,
          "cite": [
            "105 S.W.3d 609",
            "2003 Tex. Crim. App. LEXIS 75",
            "2003 WL 1918091"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fuller v. M.G. Jewelry",
          "cluster_id": 9003626,
          "cite": [
            "950 F.2d 1437",
            "1991 WL 258850"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gonzalez v. City of Schenectady",
          "cluster_id": 1038554,
          "cite": [
            "728 F.3d 149",
            "2013 U.S. App. LEXIS 17943",
            "2013 WL 4528864"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Manuel Melendez-Garcia",
          "cluster_id": 673526,
          "cite": [
            "28 F.3d 1046",
            "1994 U.S. App. LEXIS 16309",
            "1994 WL 313268"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. $191,910.00 in U.S. Currency, Bruce R. Morgan, Claimant-Appellee",
          "cluster_id": 663161,
          "cite": [
            "16 F.3d 1051",
            "94 Daily Journal DAR 2139",
            "94 Cal. Daily Op. Serv. 1214",
            "1994 U.S. App. LEXIS 2681",
            "1994 WL 46744"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rita Ann Cardenas and Shamsideen Abiodun Lawal",
          "cluster_id": 657339,
          "cite": [
            "9 F.3d 1139"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Terry King and Valerie Jean Burdex",
          "cluster_id": 604813,
          "cite": [
            "990 F.2d 1552",
            "1993 U.S. App. LEXIS 6056"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Acosta-Colon",
          "cluster_id": 198134,
          "cite": [
            "157 F.3d 9",
            "1998 U.S. App. LEXIS 24862",
            "1998 WL 671324"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Zapata",
          "cluster_id": 195255,
          "cite": [
            "18 F.3d 971",
            "1994 WL 86216"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Flores-Montano",
          "cluster_id": 134729,
          "cite": [
            "158 L. Ed. 2d 311",
            "124 S. Ct. 1582",
            "541 U.S. 149",
            "2004 U.S. LEXIS 2548",
            "72 U.S.L.W. 4263",
            "17 Fla. L. Weekly Fed. S 207"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stuart Romm",
          "cluster_id": 795139,
          "cite": [
            "455 F.3d 990",
            "2006 U.S. App. LEXIS 18474",
            "2006 WL 2042827"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Betty Lester v. City of Chicago, Officer Daniel Leahy, Officer Ernest Cain, and Sergeant John McNulty",
          "cluster_id": 495261,
          "cite": [
            "830 F.2d 706",
            "1987 U.S. App. LEXIS 14017",
            "56 U.S.L.W. 2203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Montoya de Hernandez:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111509 OR 9430181 OR 9430182 OR 9430183) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDM4ODczNjAwMDAwJnM9Mjk2NzcwMSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111509+OR+9430181+OR+9430182+OR+9430183%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(111509 OR 9430181 OR 9430182 OR 9430183)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjImcz04OTQzODQzJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111509+OR+9430181+OR+9430182+OR+9430183%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111509 OR 9430181 OR 9430182 OR 9430183)",
        "reviewed": 15,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 15,
        "triage_read": 0,
        "triage_snippet_classified": 15
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111509 OR 9430181 OR 9430182 OR 9430183)",
    "indexed_citing_opinions": 607,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111509,
        "count": 527,
        "count_source": "search"
      },
      {
        "opinion_id": 9430181,
        "count": 94,
        "count_source": "search"
      },
      {
        "opinion_id": 9430182,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430183,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 983,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-montoya-de-hernandez.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgwNDQyMTUmcz05MzI5MDUzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111509+OR+9430181+OR+9430182+OR+9430183%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111509,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 94479,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 108841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110501,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 111378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 111380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 111382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 272334,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 283495,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 285139,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 311366,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 402585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 408227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 419999,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 421712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 421842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 427199,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 428603,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 429241,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 432317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 432318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 432319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 432320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 432321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 432322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 433838,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111509,
        "cited_id": 436008,
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
    "date_created": "2026-07-06T01:47:04Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:47:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:47:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:51:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:47:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Montoya de Hernandez

```
<opinion type="majority">
<author id="b570-10">Justice Rehnquist</author>
<p id="A3j">delivered the opinion of the Court.</p>
<p id="b570-11">Respondent Rosa Elvira Montoya de Hernandez was detained by customs officials upon her arrival at the Los Ange-les Airport on a flight from Bogota, Colombia. She was found to be smuggling 88 cocaine-filled balloons in her alimen<page-number citation-index="1" label="533">*533</page-number>tary canal, and was convicted after a bench trial of various federal narcotics offenses. A divided panel of the United States Court of Appeals for the Ninth Circuit reversed her convictions, holding that her detention violated the Fourth Amendment to the United States Constitution because the customs inspectors did not have a “clear indication” of alimentary canal smuggling at the time she was detained. <span class="citation" data-id="9472040"><a href="/opinion/433838/united-states-v-rosa-elvira-montoya-de-hernandez/" aria-description="Citation for case: United States v. Rosa Elvira Montoya De Hernandez">731 F. 2d 1369</a></span> (1984). Because of a conflict in the decisions of the Courts of Appeals on this question and the importance of its resolution to the enforcement of customs laws, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./469/1188/">469 U. S. 1188</a></span>. We now reverse.</p>
<p id="b571-5">Respondent arrived at Los Angeles International Airport shortly after midnight, March 5, 1983, on Avianca Flight 080, a direct 10-hour flight from Bogota, Colombia. Her visa was in order so she was passed through Immigration and proceeded to the customs desk. At the customs desk she encountered Customs Inspector Talamantes, who reviewed her documents and noticed from her passport that she had made at least eight recent trips to either Miami or Los Angeles. Talamantes referred respondent to a secondary customs desk for further questioning. At this desk Talamantes and another inspector asked respondent general questions concerning herself and the purpose of her trip. Respondent revealed that she spoke no English and had no family or friends in the United States. She explained in Spanish that she had come to the United States to purchase goods for her husband’s store in Bogota. The customs inspectors recognized Bogota as a “source city” for narcotics. Respondent possessed $5,000 in cash, mostly $50 bills, but had no billfold. She indicated to the inspectors that she had no appointments with merchandise vendors, but planned to ride around Los Angeles in taxicabs visiting retail stores such as J. C. Penney and K-Mart in order to buy goods for her husband’s store with the $5,000.</p>
<p id="b571-6">Respondent admitted that she had no hotel reservations, but stated that she planned to stay at a Holiday Inn. Respondent could not recall how her airline ticket was pur<page-number citation-index="1" label="534">*534</page-number>chased. When the inspectors opened respondent’s one small valise they found about four changes of “cold weather” clothing. Respondent had no shoes other than the high-heeled pair she was wearing. Although respondent possessed no checks, waybills, credit cards, or letters of credit, she did produce a Colombian business card and a number of old receipts, waybills, and fabric swatches displayed in a photo album.</p>
<p id="b572-5">At this point Talamantes and the other inspector suspected that respondent was a “balloon swallower,” one who attempts to smuggle narcotics into this country hidden in her alimentary canal. Over the years Inspector Talamantes had apprehended dozens of alimentary canal smugglers arriving on Avianca Flight 080. See App. 42; <em>United States </em>v. <em>Mendez-Jimenez, </em><span class="citation" data-id="419999"><a href="/opinion/419999/united-states-v-luis-alfonso-mendez-jimenez/#1301" aria-description="Citation for case: United States v. Luis Alfonso Mendez-Jimenez">709 F. 2d 1300, 1301</a></span> (CA9 1983).</p>
<p id="b572-6">The inspectors requested a female customs inspector to take respondent to a private area and conduct a patdown and strip search. During the search the female inspector felt respondent’s abdomen area and noticed a firm fullness, as if respondent were wearing a girdle. The search revealed no contraband, but the inspector noticed that respondent was wearing two pairs of elastic underpants with a paper towel lining the crotch area.</p>
<p id="b572-7">When respondent returned to the customs area and the female inspector reported her discoveries, the inspector in charge told respondent that he suspected she was smuggling drugs in her alimentary canal. Respondent agreed to the inspector’s request that she be x-rayed at a hospital but in answer to the inspector’s query stated that she was pregnant. She agreed to a pregnancy test before the x ray. Respondent withdrew the consent for an x ray when she learned that she would have to be handcuffed en route to the hospital. The inspector then gave respondent the option of returning to Colombia on the next available flight, agreeing to an x ray, or remaining in detention until she produced a monitored bowel movement that would confirm or rebut the inspectors’ <page-number citation-index="1" label="535">*535</page-number>suspicions. Respondent chose the first option and was placed in a customs office under observation. She was told that if she went to the toilet she would have to use a wastebasket in the women’s restroom, in order that female customs inspectors could inspect her stool for balloons or capsules carrying narcotics. The inspectors refused respondent’s request to place a telephone call.</p>
<p id="b573-5">Respondent sat in the customs office, under observation, for the remainder of the night. During the night customs officials attempted to place respondent on a Mexican airline that was flying to Bogota via Mexico City in the morning. The airline refused to transport respondent because she lacked a Mexican visa necessary to land in Mexico City. • Respondent was not permitted to leave, and was informed that she would be detained until she agreed to an x ray or her bowels moved. She remained detained in the customs office under observation, for most of the time curled up in a chair leaning to one side. She refused all offers of food and drink, and refused to use the toilet facilities. The Court of Appeals noted that she exhibited symptoms of discomfort consistent with “heroic efforts to resist the usual calls of nature.” <span class="citation" data-id="9472040"><a href="/opinion/433838/united-states-v-rosa-elvira-montoya-de-hernandez/#1371" aria-description="Citation for case: United States v. Rosa Elvira Montoya De Hernandez">731 F. 2d, at 1371</a></span>.</p>
<p id="b573-6">At the shift change at 4:00 o’clock the next afternoon, almost 16 hours after her flight had landed, respondent still had not defecated or urinated or partaken of food or drink. At that time customs officials sought a court order authorizing a pregnancy test, an x ray, and a rectal examination. The Federal Magistrate issued an order just before midnight that evening, which authorized a rectal examination and involuntary x ray, provided that the physician in charge considered respondent’s claim of pregnancy. Respondent was taken to a hospital and given a pregnancy test, which later turned out to be negative. Before the results of the pregnancy test were known, a physician conducted a rectal examination and removed from respondent’s rectum a balloon containing a foreign substance. Respondent was then placed <page-number citation-index="1" label="536">*536</page-number>formally under arrest. By 4:10 a. m. respondent had passed 6 similar balloons; over the next four days she passed 88 balloons containing a total of 528 grams of 80% pure cocaine hydrochloride.</p>
<p id="b574-5">After a suppression hearing the District Court admitted the cocaine in evidence against respondent. She was convicted of possession of cocaine with intent to distribute, <span class="citation no-link">21 U. S. C. § 841</span>(a)(1), and unlawful importation of cocaine, <span class="citation no-link">21 U. S. C. §§ 952</span>(a), 960(a).</p>
<p id="b574-6">A divided panel of the United States Court of Appeals for the Ninth Circuit reversed respondent’s convictions. The court noted that customs inspectors had a “justifiably high level of official skepticism” about respondent’s good motives, but the inspectors decided to let nature take its course rather than seek an immediate magistrate’s warrant for an x ray. <span class="citation" data-id="9472040"><a href="/opinion/433838/united-states-v-rosa-elvira-montoya-de-hernandez/#1372" aria-description="Citation for case: United States v. Rosa Elvira Montoya De Hernandez">731 F. 2d, at 1372</a></span>. Such a magistrate’s warrant required a “clear indication” or “plain suggestion” that the traveler was an alimentary canal smuggler under previous decisions of the Court of Appeals. See <em>United States </em>v. <em>Quintero-Castro, </em><span class="citation" data-id="8916798"><a href="/opinion/8927001/united-states-v-quintero-castro/" aria-description="Citation for case: United States v. Quintero-Castro">705 F. 2d 1099</a></span> (CA9 1983); <em>United States </em>v. <em>Mendez-Jimenez, </em><span class="citation" data-id="419999"><a href="/opinion/419999/united-states-v-luis-alfonso-mendez-jimenez/#1302" aria-description="Citation for case: United States v. Luis Alfonso Mendez-Jimenez">709 F. 2d 1300, 1302</a></span> (CA9 1983); but cf. <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#370" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 370, n. 5</a></span> (1976). The court applied this required level of suspicion to respondent’s case. The court questioned the “humanity” of the inspectors’ decision to hold respondent until her bowels moved, knowing that she would suffer “many hours of humiliating discomfort” if she chose not to submit to the x-ray examination. The court concluded that under a “clear indication” standard “the evidence available to the customs officers when they decided to hold [respondent] for continued observation was insufficient to support the 16-hour detention.” <span class="citation" data-id="9472040"><a href="/opinion/433838/united-states-v-rosa-elvira-montoya-de-hernandez/#1373" aria-description="Citation for case: United States v. Rosa Elvira Montoya De Hernandez">731 F. 2d, at 1373</a></span>.</p>
<p id="b574-7">The Government contends that the customs inspectors reasonably suspected that respondent was an alimentary canal smuggler, and this suspicion was sufficient to justify the detention. In support of the judgment below respondent <page-number citation-index="1" label="537">*537</page-number>argues, <em>inter alia, </em>that reasonable suspicion would not support respondent’s detention, and in any event the inspectors did not reasonably suspect that respondent was carrying narcotics internally.</p>
<p id="b575-5">The Fourth Amendment commands that searches and seizures be reasonable. What is reasonable depends upon all of the circumstances surrounding the search or seizure and the nature of the search or seizure itself. <em>New Jersey </em>v. T. <em>L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#337" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 337-342</a></span> (1985). The permissibility of a particular law enforcement practice is judged by “balancing its intrusion on the individual’s Fourth Amendment interests against its promotion of legitimate governmental interests.” <em>United States </em>v. <em>Villamonte-Marquez, </em><span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/#588" aria-description="Citation for case: United States v. Villamonte-Marquez">462 U. S. 579, 588</a></span> (1983); <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979); <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967).</p>
<p id="b575-7">Here the seizure of respondent took place at the international border. Since the founding of our Republic, Congress has granted the Executive plenary authority to conduct routine searches and seizures at the border, without probable cause or a warrant, in order to regulate the collection of duties and to prevent the introduction of contraband into this country. See <em>United States </em>v. <em>Ramsey, </em><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#616" aria-description="Citation for case: United States v. Ramsey">431 U. S. 606, 616-617</a></span> (1977), citing Act of July 31, 1789, ch. 5, <span class="citation no-link">1 Stat. 29</span>. This Court has long recognized Congress’ power to police entrants at the border. See <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#623" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 623</a></span> (1886). As we stated recently:</p>
<blockquote id="b575-9">“‘Import restrictions and searches of persons or packages at the national border rest on different considerations and different rules of constitutional law from domestic regulations. The Constitution gives Congress broad comprehensive powers “[t]o regulate Commerce with foreign Nations,” Art. I, §8, cl. 3. Historically such broad powers have been necessary to prevent smuggling and to prevent prohibited articles from <page-number citation-index="1" label="538">*538</page-number>entry.’” <span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#618" aria-description="Citation for case: United States v. Ramsey"><em>Ramsey, supra, </em>at 618-619</a></span>, quoting <em>United States </em>v. <em>12 200-Ft. Reels of Film, </em><span class="citation" data-id="9425385"><a href="/opinion/108841/united-states-v-12-200-ft-reels-of-super-8mm-film/#125" aria-description="Citation for case: United States v. 12 200-Ft. Reels of Super 8MM. Film">413 U. S. 123, 125</a></span> (1973).</blockquote>
<p id="b576-5">Consistently, therefore, with Congress’ power to protect the Nation by stopping and examining persons entering this country, the Fourth Amendment’s balance of reasonableness is qualitatively different at the international border than in the interior. Routine searches of the persons and effects of entrants are not subject to any requirement of reasonable suspicion, probable cause, or warrant,<footnotemark>1</footnotemark> and first-class mail may be opened without a warrant on less than probable cause, <em><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">Ramsey, supra.</a></span> </em>Automotive travelers may be stopped at fixed checkpoints near the border -without individualized suspicion even if the stop is based largely on ethnicity, <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#562" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 562-563</a></span> (1976), and boats on inland waters with ready access to the sea may be hailed and boarded with no suspicion whatever. <em>United States </em>v. <em><span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/" aria-description="Citation for case: United States v. Villamonte-Marquez">Villamonte-Marquez, supra.</a></span></em></p>
<p id="b576-6">These cases reflect longstanding concern for the protection of the integrity of the border. This concern is, if anything, heightened by the veritable national crisis in law enforcement caused by smuggling of illicit narcotics, see <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#561" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 561</a></span> (1980) (Powell, J., concurring), and in particular by the increasing utilization of alimentary canal smuggling. This desperate practice appears to be a relatively recent addition to the smugglers’ repertoire of deceptive practices, and it also appears to be exceedingly dif<page-number citation-index="1" label="539">*539</page-number>ficult to detect.<footnotemark>2</footnotemark> Congress had recognized these difficulties. Title <span class="citation no-link">19 U. S. C. § 1582</span> provides that “all persons coming into the United States from foreign countries shall be liable to detention and search authorized . . . [by customs regulations].” Customs agents may “stop, search, and examine” any “vehicle, beast or person” upon which an officer suspects there is contraband or “merchandise which is subject to duty.” §482; see also §§ 1467, 1481; <span class="citation no-link">19 CFR §§ 162.6</span>, 162.7 (1984).</p>
<p id="b577-5">Balanced against the sovereign’s interests at the border are the Fourth Amendment rights of respondent. Having presented herself at the border for admission, and having subjected herself to the criminal enforcement powers of the Federal Government, <span class="citation no-link">19 U. S. C. § 482</span>, respondent was entitled to be free from unreasonable search and seizure. But not only is the expectation of privacy less at the border than in the interior, see, <em>e. g., Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#154" aria-description="Citation for case: Carroll v. United States">267 U. S. <page-number citation-index="1" label="540">*540</page-number>132, 154</a></span> (1925); cf. <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#515" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 515</a></span> (1983) (Blackmun, J., dissenting), the Fourth Amendment balance between the interests of the Government and the privacy right of the individual is also struck much more favorably to the Government at the border. <em>Supra, </em>at 538.</p>
<p id="b578-4">We have not previously decided what level of suspicion would justify a seizure of an incoming traveler for purposes other than a routine border search. Cf. <em>Ramsey, </em><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#618" aria-description="Citation for case: United States v. Ramsey">431 U. S., at 618, n. 13</a></span>. The Court of Appeals held that the initial detention of respondent was permissible only if the inspectors possessed a “clear indication” of alimentary canal smuggling. <span class="citation" data-id="9472040"><a href="/opinion/433838/united-states-v-rosa-elvira-montoya-de-hernandez/#1372" aria-description="Citation for case: United States v. Rosa Elvira Montoya De Hernandez">731 F. 2d, at 1372</a></span>, citing <em>United States </em>v. <em>Quintero-Castro, </em><span class="citation" data-id="8916798"><a href="/opinion/8927001/united-states-v-quintero-castro/" aria-description="Citation for case: United States v. Quintero-Castro">705 F. 2d 1099</a></span> (CA9 1983); cf. <em>United States </em>v. <em>Mendez-Jimenez, </em><span class="citation" data-id="419999"><a href="/opinion/419999/united-states-v-luis-alfonso-mendez-jimenez/" aria-description="Citation for case: United States v. Luis Alfonso Mendez-Jimenez">709 F. 2d 1300</a></span> (CA9 1983). This “clear indication” language comes from our opinion in <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966), but we think that the Court of Appeals misapprehended the significance of that phrase in the context in which it was used in Schmerber.<footnotemark>3</footnotemark> The Court of Appeals viewed “clear indication” as an intermediate standard between “reasonable suspicion” and “probable cause.” See <span class="citation" data-id="419999"><a href="/opinion/419999/united-states-v-luis-alfonso-mendez-jimenez/#1302" aria-description="Citation for case: United States v. Luis Alfonso Mendez-Jimenez"><em>Mendez-Jimenez, supra, </em>at 1302</a></span>. But we think that the words in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>were used to indicate the necessity for particularized suspicion that the evidence sought might be found within the body of the individual, rather than as enunciating still a third Fourth Amendment threshold between “reasonable suspicion” and “probable cause.”</p>
<p id="b578-5">No other court, including this one, has ever adopted <em>Schmerber1 </em>s “clear indication” language as a Fourth Amendment standard. See, <em>e. g., Winston </em>v. <em>Lee, </em><span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/#759" aria-description="Citation for case: Winston v. Lee">470 U. S. 753, <page-number citation-index="1" label="541">*541</page-number>759-763</a></span> (1985) (surgical removal of bullet for evidence). Indeed, another Court of Appeals, faced with facts almost identical to this case, has adopted a less strict standard based upon reasonable suspicion. See <em>United States </em>v. <em>Mosquera-Ramirez, </em><span class="citation" data-id="9471932"><a href="/opinion/432318/united-states-v-luis-fernando-mosquera-ramirez/#1355" aria-description="Citation for case: United States v. Luis Fernando Mosquera-Ramirez">729 F. 2d 1352, 1355</a></span> (CA11 1984). We do not think that the Fourth Amendment’s emphasis upon reasonableness is consistent with the creation of a third verbal standard in addition to “reasonable suspicion” and “probable cause”; we are dealing with a constitutional requirement of reasonableness, not <em>mens rea, </em>see <em>United States </em>v. <em>Bailey, </em><span class="citation" data-id="9427750"><a href="/opinion/110175/united-states-v-bailey/#403" aria-description="Citation for case: United States v. Bailey">444 U. S. 394, 403-406</a></span> (1980), and subtle verbal gradations may obscure rather than elucidate the meaning of the provision in question.</p>
<p id="b579-5">We hold that the detention of a traveler at the border, beyond the scope of a routine customs search and inspection, is justified at its inception if customs agents, considering all the facts surrounding the traveler and her trip, reasonably suspect that the traveler is smuggling contraband in her alimentary canal.<footnotemark>4</footnotemark></p>
<p id="b579-6">The “reasonable suspicion” standard has been applied in a number of contexts and effects a needed balance between private and public interests when law enforcement officials must make a limited intrusion on less than probable cause. It thus fits well into the situations involving alimentary canal smuggling at the border: this type of smuggling gives no external signs and inspectors will rarely possess probable cause to arrest or search, yet governmental interests in stopping smuggling at the border are high indeed. Under this standard officials at the border must have a “particularized and objective basis for suspecting the particular person” of ali<page-number citation-index="1" label="542">*542</page-number>mentary canal smuggling. <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 417</a></span> (1981); <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#418" aria-description="Citation for case: United States v. Cortez"><em>id., </em>at 418</a></span>, citing <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 21, n. 18</a></span> (1968).</p>
<p id="b580-5">The facts, and their rational inferences, known to customs inspectors in this case clearly supported a reasonable suspicion that respondent was an alimentary canal smuggler. We need not belabor the facts, including respondent’s implausible story, that supported this suspicion, see <em>supra, </em>at 533-536. The trained customs inspectors had encountered many alimentary canal smugglers and certainly had more than an “inchoate and unparticularized suspicion or ‘hunch,’” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><em>Terry, supra, </em>at 27</a></span>, that respondent was smuggling narcotics in her alimentary canal. The inspectors’ suspicion was a “‘common-sense conclusio[n] about human behavior’ upon which ‘practical people,’ — including government officials, are entitled to rely.” <em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#346" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 346</a></span>, citing <em>United States </em>v. <em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">Cortez, supra.</a></span></em></p>
<p id="b580-6">The final issue in this case is whether the detention of respondent was reasonably related in scope to the circumstances which justified it initially. In this regard we have cautioned that courts should not indulge in “unrealistic second-guessing,” <em>United States </em>v. <em>Sharpe, </em><span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#686" aria-description="Citation for case: United States v. Sharpe">470 U. S. 675, 686</a></span> (1985), and we have noted that “creative judge[s], engaged in <em>post hoc </em>evaluations of police conduct can almost always imagine some alternative means by which the objectives of the police might have been accomplished.” <span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#686" aria-description="Citation for case: United States v. Sharpe"><em>Id., </em>at 686-687</a></span>. But “[t]he fact that the protection of the public might, in the abstract, have been accomplished by ‘less intrusive’ means does not, in itself, render the search unreasonable.” <span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#687" aria-description="Citation for case: United States v. Sharpe"><em>Id., </em>at 687</a></span>, citing <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#447" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 447</a></span> (1973). Authorities must be allowed “to graduate their response to the demands of any particular situation.” <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place">462 U. S. 696, 709, n. 10</a></span> (1983). Here, respondent was detained incommunicado for almost 16 hours before inspectors sought a warrant; the warrant then took a number of hours to procure, through no apparent fault <page-number citation-index="1" label="543">*543</page-number>of the inspectors. This length of time undoubtedly exceeds any other detention we have approved under reasonable suspicion. But we have also consistently rejected hard-and-fast time limits, <em><span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/" aria-description="Citation for case: United States v. Sharpe">Sharpe, supra;</a></span> Place, supra, </em>at 709, n. 10. Instead, “common sense and ordinary human experience must govern over rigid criteria.” <span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#685" aria-description="Citation for case: United States v. Sharpe"><em>Sharpe, supra, </em>at 685</a></span>.</p>
<p id="b581-5">The rudimentary knowledge of the human body which judges possess in common with the rest of humankind tells us that alimentary canal smuggling cannot be detected in the amount of time in which other illegal activity may be investigated through brief Terry-type stops. It presents few, if any external signs; a quick frisk will not do, nor will even a strip search. In the case of respondent the inspectors had available, as an alternative to simply awaiting her bowel movement, an x ray. They offered her the alternative of submitting herself to that procedure. But when she refused that alternative, the customs inspectors were left with only two practical alternatives: detain her for such time as necessary to confirm their suspicions, a detention which would last much longer than the typical <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop, or turn her loose into the interior carrying the reasonably suspected contraband drugs.</p>
<p id="b581-6">The inspectors in this case followed this former procedure. They no doubt expected that respondent, having recently disembarked from a 10-hour direct flight with a full and stiff abdomen, would produce a bowel movement without extended delay. - But her visible efforts to resist the call of nature, which the court below labeled “heroic,” disappointed this expectation and in turn caused her humiliation and discomfort. Our prior cases have refused to charge police with delays in investigatory detention attributable to the suspect’s evasive actions, see <em>Sharpe, </em><span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#687" aria-description="Citation for case: United States v. Sharpe">470 U. S., at 687-688</a></span>; <span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#697" aria-description="Citation for case: United States v. Sharpe"><em>id., </em>at 697</a></span> (Marshall, J., concurring in judgment), and that principle applies here as well. Respondent alone was responsible for much of the duration and discomfort of the seizure.</p>
<p id="b582-4"><page-number citation-index="1" label="544">*544</page-number>Under these circumstances, we conclude that the detention in this case was not unreasonably long. It occurred at the international border, where the Fourth Amendment balance of interests leans heavily to the Government. At the border, customs officials have more than merely an investigative law enforcement role. They are also charged, along with immigration officials, with protecting this Nation from entrants who may bring anything harmful into this country, whether that be communicable diseases, narcotics, or explosives. See <span class="citation no-link">8 U. S. C. §§ 1182</span>(a)(23), 1182(a)(6), 1222; <span class="citation no-link">19 CFR §§ 162.4-162.7</span> (1984). See also <span class="citation no-link">19 U. S. C. §482</span>; <span class="citation no-link">8 U. S. C. § 1103</span>(a). In this regard the detention of a suspected alimentary canal smuggler at the border is analogous to the detention of a suspected tuberculosis carrier at the border: both are detained until their bodily processes dispel the suspicion that they will introduce a harmful agent into this country. Cf. <span class="citation no-link">8 U. S. C. § 1222</span>; 42 CFR pt. 34 (1984); <span class="citation no-link">19 U. S. C. §§482</span>, 1582.</p>
<p id="b582-5">Respondent’s detention was long, uncomfortable, indeed, humiliating; but both its length and its discomfort resulted solely from the method by which she chose to smuggle illicit drugs into this country. In <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span> (1972), another Terry-stop case, we said that “[t]he Fourth Amendment does not require a policeman who lacks the precise level of information necessary for probable cause to arrest to simply shrug his shoulders and allow a crime to occur or a criminal to escape.” <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#145" aria-description="Citation for case: Adams v. Williams"><em>Id., </em>at 145</a></span>. Here, by analogy, in the presence of articulable suspicion of smuggling in her alimentary canal, the customs officers were not required by the Fourth Amendment to pass respondent and her 88 cocaine-filled balloons into the interior. Her detention for the period of time necessary to either verify or dispel the suspicion was not unreasonable. The judgment of the Court of Appeals is therefore</p>
<p id="b582-6">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b576-7"> See <em>United States </em>v. <em>Ramsey, </em><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#616" aria-description="Citation for case: United States v. Ramsey">431 U. S., at 616-619</a></span>; <em>Almeida-Sanchez </em>v. <em>United States, </em><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#272" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 272-273</a></span> (1973); <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#288" aria-description="Citation for case: Almeida-Sanchez v. United States"><em>id., </em>at 288</a></span> (White, J., dissenting). As the Court stated in <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#154" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 154</a></span> (1925):</p>
<blockquote id="b576-8">“Travellers may be so stopped in crossing an international boundary because of national self protection reasonably requiring one entering the country to identify himself as entitled to come in and his belongings as effects which may be lawfully brought in.”</blockquote>
</footnote>
<footnote label="2">
<p id="b577-6"> See <em>United States </em>v. <em>DeMontoya, </em><span class="citation" data-id="9471940"><a href="/opinion/432322/united-states-v-celina-nohemy-giraldo-de-montoya/" aria-description="Citation for case: United States v. Celina Nohemy Giraldo De Montoya">729 F. 2d 1369</a></span> (CA11 1984) (required surgery; swallowed 100 cocaine-filled condoms); <em>United States </em>v. <em>Pino, </em><span class="citation" data-id="9471934"><a href="/opinion/432319/united-states-v-gabriel-antonio-pino/" aria-description="Citation for case: United States v. Gabriel Antonio Pino">729 F. 2d 1357</a></span> (CA11 1984) (required surgery; 120 cocaine-filled pellets); <em>United States </em>v. <em>Mejia, </em><span class="citation" data-id="427199"><a href="/opinion/427199/united-states-v-german-mejia/" aria-description="Citation for case: United States v. German Mejia">720 F. 2d 1378</a></span> (CA5 1983) (75 balloons); <em>United States </em>v. <em>Couch, </em><span class="citation" data-id="408227"><a href="/opinion/408227/united-states-v-joseph-mark-couch/#605" aria-description="Citation for case: United States v. Joseph Mark Couch">688 F. 2d 599, 605</a></span> (CA9 1982) (36 capsules); <em>United States </em>v. <em>Quintero-Castro, </em><span class="citation" data-id="8916798"><a href="/opinion/8927001/united-states-v-quintero-castro/" aria-description="Citation for case: United States v. Quintero-Castro">705 F. 2d 1099</a></span> (CA9 1983) (120 balloons); <em>United States </em>v. <em>Saldarriaga-Marin, </em><span class="citation" data-id="436008"><a href="/opinion/436008/united-states-v-gloria-saldarriaga-marin-marina-hoyos-gomez-del-soccorro/" aria-description="Citation for case: United States v. Gloria Saldarriaga-Marin, Marina Hoyos...">734 F. 2d 1425</a></span> (CA11 1984); <em>United States </em>v. <em>Vega-Barvo, </em><span class="citation" data-id="9471930"><a href="/opinion/432317/united-states-v-maria-vega-barvo/" aria-description="Citation for case: United States v. Maria Vega-Barvo">729 F. 2d 1341</a></span> (CA11 1984) (135 condoms); <em>United States </em>v. <em>Mendez-Jimenez, </em><span class="citation" data-id="419999"><a href="/opinion/419999/united-states-v-luis-alfonso-mendez-jimenez/" aria-description="Citation for case: United States v. Luis Alfonso Mendez-Jimenez">709 F. 2d 1300</a></span> (CA9 1983) (102 balloons); <em>United States </em>v. <em>Mosquera-Ramirez, </em><span class="citation" data-id="9471932"><a href="/opinion/432318/united-states-v-luis-fernando-mosquera-ramirez/" aria-description="Citation for case: United States v. Luis Fernando Mosquera-Ramirez">729 F. 2d 1352</a></span> (CA11 1984) (95 condoms); <em>United States </em>v. <em>Castrillon, </em><span class="citation" data-id="424734"><a href="/opinion/424734/united-states-v-oscar-alfonso-castrillon/" aria-description="Citation for case: United States v. Oscar Alfonso Castrillon">716 F. 2d 1279</a></span> (CA9 1983) (83 balloons); <em>United States </em>v. <em>Castaneda-Castaneda, </em><span class="citation" data-id="9471936"><a href="/opinion/432320/united-states-v-jose-jaime-castaneda-castaneda-and-betulia-jara-de/" aria-description="Citation for case: United States v. Jose Jaime Castaneda-Castaneda and...">729 F. 2d 1360</a></span> (CA11 1984) (2 smugglers; 201 balloons); <em>United States </em>v. <em>Caicedo-Guamizo, </em><span class="citation" data-id="429241"><a href="/opinion/429241/united-states-v-jose-orlando-caicedo-guarnizo/" aria-description="Citation for case: United States v. Jose Orlando Caicedo-Guarnizo">723 F. 2d 1420</a></span> (CA9 1984) (85 balloons); <em>United States </em>v. <em>Henao-Castano, </em><span class="citation" data-id="9471938"><a href="/opinion/432321/united-states-v-rodrigo-henao-castano/" aria-description="Citation for case: United States v. Rodrigo Henao-Castano">729 F. 2d 1364</a></span> (CA11 1984) (85 condoms); <em>United States </em>v. <em>Ek, </em><span class="citation" data-id="9469126"><a href="/opinion/402585/united-states-v-robert-karl-ek/" aria-description="Citation for case: United States v. Robert Karl Ek">676 F. 2d 379</a></span> (CA9 1982) (30 capsules); <em>United States </em>v. <em>Padilla, </em><span class="citation" data-id="8919792"><a href="/opinion/8929700/united-states-v-padilla/" aria-description="Citation for case: United States v. Padilla">729 F. 2d 1367</a></span> (CA11 1984) (115 condoms); <em>United States </em>v. <em>Gomez-Diaz, </em><span class="citation" data-id="421842"><a href="/opinion/421842/united-states-v-jamie-alberto-gomez-diaz/" aria-description="Citation for case: United States v. Jamie Alberto Gomez-Diaz">712 F. 2d 949</a></span> (CA5 1983) (69 balloons); <em>United States </em>v. <em>D’Allerman, </em><span class="citation" data-id="421712"><a href="/opinion/421712/united-states-v-constanza-dallerman-aka-reyna-maria-murcia/" aria-description="Citation for case: United States v. Constanza D&#x27;allerman, A/K/A Reyna Maria...">712 F. 2d 100</a></span> (CA5 1983) (80 balloons); <em>United States </em>v. <em>Contento-Pachon, </em><span class="citation" data-id="9471547"><a href="/opinion/428603/united-states-v-juan-manuel-contento-pachon/" aria-description="Citation for case: United States v. Juan Manuel Contento-Pachon">723 F. 2d 691</a></span> (CA9 1984) (129 balloons).</p>
</footnote>
<footnote label="3">
<p id="b578-6"> In that ease we stated:</p>
<blockquote id="b578-7">“The interests in human dignity and privacy which the Fourth Amendment protects forbid any such intrusion [beyond the body’s surface] on the mere chance that desired evidence might be obtained. In the absence of a clear indication that in fact such evidence will be found, these fundamental human interests require law officers to suffer the risk that such evidence may disappear unless there is an immediate search.” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#769" aria-description="Citation for case: Schmerber v. California">384 U. S., at 769-770</a></span>.</blockquote>
</footnote>
<footnote label="4">
<p id="b579-7"> It is also important to note what we do <em>not </em>hold. Because the issues are not presented today we suggest no view on what level of suspicion, if any, is required for nonroutine border searches such as strip, body-cavity, or involuntary x-ray searches. Both parties would have us decide the issue of whether aliens possess lesser Fourth Amendment rights at the border; that question was not raised in either court below and we do not consider it today.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Moore-Bush.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Moore-Bush
type: case
citation: "36 F.4th 320 (2022)"
parallel_cite: ""
neutral_cite: ""
court: 1st Cir.
court_level: coa
circuit: ca1
year: 2022
date_decided: 2022-06-09
docket: 19-1582
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
  opinion_url: "https://www.courtlistener.com/opinion/6476395/united-states-v-moore-bush/"
  cluster_id: 6476395
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Moore-Bush
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Fourth Amendment Framework]]"
    role: Key
  - page: "[[Curtilage]]"
    role: "Related (cross-doctrine)"
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Related (cross-doctrine)"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
related:
  - "[[Fourth Amendment Framework]]"
  - "[[Curtilage]]"
  - "[[Third-Party Doctrine & CSLI]]"
  - "[[Two Definitions of Search]]"
  - "[[Carpenter v. United States]]"
  - "[[Katz v. United States]]"
tags:
  - case
  - fourth-amendment
  - pole-camera
  - long-term-surveillance
  - curtilage
  - reasonable-expectation-of-privacy
  - mosaic-theory
  - first-circuit
  - en-banc
holding: "Sitting en banc, the First Circuit unanimously reversed the suppression of evidence from eight months of continuous, warrantless pole-camera surveillance of a home's front curtilage and remanded with instructions to deny suppression — but the court divided evenly on the merits: three judges concluded the prolonged aggregate surveillance was a Fourth Amendment search, and three concluded it was not, so the decision established no binding circuit rule on whether such surveillance is a search."
aliases:
  - United States v. Moore-Bush
  - "United States v. Moore-Bush (1st Cir. 2022) (en banc)"
---

# United States v. Moore-Bush

*36 F.4th 320 (1st Cir. 2022) (en banc)* (No. 19-1582) · U.S. Court of Appeals for the First Circuit · **Binding in-circuit — 1st Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 6476395 → lead opinion 6348506 (en banc per curiam; 36 F.4th 320, decided 2022-06-09; equally divided on the merits). Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — CL text is slip-paginated). S9 promotes. -->

## Background
Investigating Nia Moore-Bush and Daphne Moore, ATF agents installed a digital video camera near the top of a utility pole across the public street from the Hadley Street residence and used it, without a warrant, to surveil the home continuously — day and night — for about eight months. The camera could zoom to capture facial expressions, clothing details, small objects in a person's hands, and license plates of cars in the private driveway, producing what the defendants described as a live-action log of everyone who came and went from the front [[Curtilage|curtilage]] over that period. The defendants moved to suppress the pole-camera record and its fruits. The district court granted suppression, concluding that the circuit's prior decision upholding such surveillance (*Bucci*) was no longer binding after *[[Carpenter v. United States]]*. The government appealed, and the First Circuit reheard the case [[Reading and Citing Cases#en-banc|en banc]].

## Issue
Whether eight months of continuous, warrantless pole-camera surveillance of the [[Curtilage|curtilage]] of a home is a Fourth Amendment search — and whether, in any event, the evidence had to be suppressed.

## Rule
The full court agreed on the disposition but not on the constitutional question. As the [[Reading and Citing Cases#en-banc|en banc]] court stated [[Common Legal Terms#per-curiam|per curiam]]: "The district court order granting Daphne Moore and Nia Moore-Bush's motions to suppress is unanimously reversed by the en banc court. We remand with instructions to deny the motions to suppress." — 36 F.4th 320, slip op. at 3. ^pin-op3

## Application
Though unanimous in the result, the six judges split evenly on the Fourth Amendment merits, and neither view commanded a majority. One trio (Barron, C.J., with Thompson and Kayatta, JJ.) concluded that the prolonged, aggregate surveillance of the [[Curtilage|curtilage]] *was* a search — reasoning, in the spirit of *[[Carpenter v. United States|Carpenter]]*, that continuously recording the whole of a household's comings and goings for eight months invades a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] that no one activity, viewed alone, would carry — yet agreed that suppression was unwarranted. The other trio (Lynch, J., with Howard and Gelpí, JJ.) concluded that no search occurred, treating the earlier *Bucci* decision as controlling and unshaken by *[[Carpenter v. United States|Carpenter]]*. Because the court divided three-to-three on whether a search took place, its opinions establish no binding circuit rule on that question; what the decision holds is only that, on this record, the evidence should not be suppressed and the motions must be denied.

## Conclusion
The district court's suppression order was **unanimously reversed** and the case **[[Reading and Citing Cases#on-remand|remanded]] with instructions to deny** the motions to suppress. The [[Reading and Citing Cases#en-banc|en banc]] court fractured evenly on whether the surveillance was a search, so the case resolves the parties' dispute without settling that question for the circuit.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Moore-Bush* is best taught as an **open question**, not a settled rule: an [[Reading and Citing Cases#en-banc|en banc]] court split evenly on whether *[[Carpenter v. United States|Carpenter]]*'s aggregation reasoning extends long-term **pole-camera** surveillance of a home's **[[Curtilage|curtilage]]** into "search" territory. Present both [[Common Legal Terms#concurring-opinion|concurrences]] as competing frameworks — the *[[Carpenter v. United States|Carpenter]]*/mosaic view (a search) versus the *[[Katz v. United States|Katz]]*/public-exposure view (no search) — and stress that, because neither drew a majority, the surveillance-is-a-search question remains unresolved in the First Circuit.

## Appears on
- [[Fourth Amendment Framework]] — *Key*
- [[Curtilage]] — *Related (cross-doctrine)*
- [[Third-Party Doctrine & CSLI]] — *Related (cross-doctrine)*
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*

## Sources
- [*United States v. Moore-Bush*, 36 F.4th 320 (1st Cir. 2022) (en banc)](https://www.courtlistener.com/opinion/6476395/united-states-v-moore-bush/) — pinpoint: slip op. at 3 (per curiam disposition — unanimous reversal, court equally divided on whether the surveillance was a search; the CL opinion text carries slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0c4ca09320798530", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Moore-Bush"}, "payload": {"all": [{"cite": "36 F.4th 320", "page": "320", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "36"}], "display": "36 F.4th 320", "official": {"cite": "36 F.4th 320", "page": "320", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "36"}, "official_selection_present": true, "record_id": "United States v. Moore-Bush"}}
{"assertion_id": "918889bd819d8e5a", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Moore-Bush"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Moore-Bush", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Moore-Bush

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Moore-Bush",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Moore-Bush",
    "case_name_short": "Moore-Bush",
    "case_name_full": "",
    "input_case_name": "United States v. Moore-Bush",
    "court": "1st Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca1",
    "state": null,
    "date_decided": "2022-06-09",
    "year": 2022,
    "docket": "19-1582",
    "cluster_id": 6476395,
    "lead_opinion_id": 6348506,
    "sibling_ids": [],
    "absolute_url": "/opinion/6476395/united-states-v-moore-bush/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "36 F.4th 320",
      "volume": "36",
      "reporter": "F.4th",
      "page": "320",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "36 F.4th 320",
        "volume": "36",
        "reporter": "F.4th",
        "page": "320",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "36 F.4th 320",
    "official_selection": {
      "court_class": "coa",
      "selected": "36 F.4th 320",
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
    "date_created": "2026-07-07T18:20:05Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:20:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:20:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:20:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:20:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-moore-bush--6476395",
      "to_record_id": "United States v. Moore-Bush",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Moore-Bush (truncated)

```
          United States Court of Appeals
                     For the First Circuit


Nos. 19-1582
     19-1625
                         UNITED STATES,

                           Appellant,

                               v.

               NIA MOORE-BUSH, a/k/a Nia Dinzey,

                      Defendant, Appellee.


Nos. 19-1583
     19-1626
                         UNITED STATES,

                           Appellant,

                               v.

                         DAPHNE MOORE,

                      Defendant, Appellee.



         APPEALS FROM THE UNITED STATES DISTRICT COURT
               FOR THE DISTRICT OF MASSACHUSETTS

          [Hon. William G. Young, U.S. District Judge]


                             Before

                      Barron, Chief Judge,
  Lynch, Howard, Thompson, Kayatta, and Gelpí, Circuit Judges.


    Randall E. Kromm, Assistant United States Attorney, with whom
Andrew E. Lelling, United States Attorney, was on brief, for
appellant.
     Judith H. Mizner, Assistant Federal Public Defender, for
appellee Nia Moore-Bush, a/k/a Nia Dinzey.
     Linda J. Thompson, with whom John M. Thompson and Thompson &
Thompson, P.C. were on brief, for appellee Daphne Moore.
     Matthew R. Segal, with whom Jessie J. Rossman, Nathan Freed
Wessler, Brett Max Kaufman, Andrew Crocker, Samir Jain, Gregory T.
Nojeim, and Mana Azarmi were on brief, for amici curiae American
Civil Liberties Union, American Civil Liberties Union of
Massachussetts, Center for Democracy & Technology, and Electronic
Frontier Foundation in support of defendant-appellees.
     Bruce D. Brown, with whom Katie Townsend, Gabriel Rottman,
and Mailyn Fidler were on brief, for amici curiae Reporters
Committee for Freedom of the Press and Eight Media Organizations
in support of defendant-appellees.

                      ____________________

                         Opinion En Banc


                           June 9, 2022
                         AMENDED OPINION




      The full version of this opinion was filed on May 27,
2022,and remains on file, under seal, in the Clerk's Office.
         Per curiam.   The district court order granting Daphne

Moore and Nia Moore-Bush's motions to suppress is unanimously

reversed by the en banc court.     We remand with instructions to

deny the motions to suppress.




                 - Concurring Opinions Follow -




                                - 3 -
                BARRON,    Chief     Judge,       THOMPSON        and    KAYATTA,    Circuit

Judges, concurring.         The Fourth Amendment to the U.S. Constitution

"seeks     to    secure    'the      privacies        of    life'      against   'arbitrary

power,'" Carpenter v. United States, 138 S. Ct. 2206, 2214 (2018)

(quoting Boyd v. United States, 116 U.S. 616, 630 (1886)), by

"plac[ing]       obstacles      in    the       way   of    a    too    permeating      police

surveillance," id. (quoting United States v. Di Re, 332 U.S. 581,

595 (1948)).         It is with that "Founding-era understanding[] in

mind," id., that we must determine in these consolidated appeals

whether the Fourth Amendment places any limits on the use by law

enforcement of the kind of surveillance -- unimagined in 1789 --

that   it       engaged    in   here:       the       continuous        and   surreptitious

recording, day and night for eight months, of all the activities

in   the    front    curtilage       of     a    private        residence     visible    to   a

remotely-controlled digital video camera affixed to a utility pole

across the street from that residence.

                The Fourth Amendment issue concerning the use of such

surveillance arises here in connection with the criminal cases

that the federal government brought in the United States District

Court for the District of Massachusetts against Nia Moore-Bush and

her mother, Daphne Moore, on federal drug- and gun-related charges.

Each defendant moved in the District Court to suppress on Fourth

Amendment grounds all evidence derived from the digital compendium

created     through       the   long-term         use      of    the    video    pole-camera

                                            - 4 -
surveillance of the front curtilage of the defendants' residence.

The government opposed the motions on the ground that no Fourth

Amendment "search" had been conducted.                 The District Court then

granted the defendants' motions to suppress.

           As we will explain, we conclude -- unlike our colleagues

-- that the government did conduct a Fourth Amendment "search"

when it accessed the digital video record that law enforcement had

created   over    the    course      of    the     eight    months    in    question,

notwithstanding the government's contention that the record itself

is merely a compendium of images of what had been exposed to public

view.     As we also will explain, however, we agree with our

colleagues     that     the    District       Court's       order     granting    the

defendants' motions to suppress must be reversed.

           We come to that latter conclusion because the relevant

controlling precedent from our circuit that was in place at the

time that the government drew upon the pole-camera surveillance

was United States v. Bucci, 582 F.3d 108 (1st Cir. 2009).                         And,

there, a panel of this court                 had   held that the use by law

enforcement of uncannily similar pole-camera surveillance did not

constitute a search within the meaning of the Fourth Amendment and

so raised no Fourth Amendment concerns.                    Id. at 116-17.        Thus,

while we conclude -- unlike our colleagues -- that subsequent

developments      in    Fourth      Amendment      jurisprudence       support     the

overruling   of    Bucci      and   the     conclusion      that     the   government

                                          - 5 -
conducted a search here, we also conclude that, under the "good

faith" exception to the Fourth Amendment's warrant requirement,

see Davis v. United States, 564 U.S. 229, 238-41 (2011), the

government was entitled to rely on Bucci in acting as it did,

Bucci, 582 F.3d at 116.       Cf. United States v. Campbell, 26 F.4th

860, 873, 887-88 (11th Cir. 2022) (en banc) (applying the good-

faith exception even though it had not been raised by the parties

in their initial briefings).

            The result is that our court is unanimous in holding

that the District Court's order granting the motions to suppress

must be reversed. Our court's rationale for that holding, however,

is most decidedly not.

            The three of us who join this separate opinion would

reverse   the   District   Court's   order   granting     the   defendants'

motions to suppress based solely on the "good faith" exception to

the Fourth Amendment's warrant requirement.        We reject, however,

our colleagues' view that the accessing by law enforcement in a

criminal case of the record created by the kind of suspicionless,

long-term   digital   video   surveillance   at   issue    here   does   not

constitute a Fourth Amendment search.

            Mindful of the brave new world that the routine use of

such all-encompassing, long-term video surveillance of the front

curtilage of a home could bring about, we are convinced that the

government does conduct a search within the meaning of the Fourth

                                  - 6 -
Amendment when it accesses the record that it creates through

surveillance of that kind and thus that law enforcement, in doing

so, must comply with that Amendment's limitations.          For, in accord

with post-Bucci precedents from the Supreme Court of the United

States that recognize the effect that the pace of technological

change can have on long assumed expectations of privacy, we are

convinced that no other conclusion would be faithful to the balance

that the Fourth Amendment strikes between the right to be "secure"

in one's home and the need for public order.1

                                     I.

                                     A.

             The following facts -- including the characteristics of

the   pole   camera   and   the   recording   that   it   produced   --   are

undisputed on appeal.        The federal Bureau of Alcohol, Tobacco,

Firearms and Explosives ("ATF") began investigating Moore-Bush in

January 2017, for the unlicensed sale of firearms.2           ATF began to


      1Although we conclude that the motions to suppress must be
denied pursuant to the good-faith exception to the warrant
requirement, we conclude that it would not be appropriate to rely
solely on that ground to resolve this case.        The question of
Bucci's status in this circuit going forward is an important one.
Cf. Pearson v. Callahan, 555 U.S. 223, 236 (2009) (allowing "courts
of appeals . . . to exercise their sound discretion in deciding
which of the two prongs of the qualified immunity analysis should
be addressed first," including whether the constitutionality of
the officer's conduct should be analyzed first).
      Our colleagues discuss in some detail the circumstances that
      2

caused law enforcement to begin to investigate Moore-Bush. Those
details are not pertinent to this analysis, however, because the


                                    - 7 -
have   concerns   during    the    investigation     that    Moore-Bush   was

trafficking in narcotics.

             About a month into the ATF investigation, Moore-Bush

moved in with her mother, Moore, who lived at 120 Hadley Street in

Springfield, Massachusetts.        ATF agents claimed that they came to

suspect that Moore-Bush -- though not, at that point, her mother

-- was using the Hadley Street residence as the site for illegal

firearms and narcotics transactions.

             The location of the home made it difficult for law

enforcement to undertake the physical surveillance of it.             So, on

or around May 17, 2017, ATF agents, without seeking a warrant,

surreptitiously installed a digital video camera near the top of

a utility pole across the public street from the residence.

             The District Court found -- based on the defendants'

undisputed contentions -- that the digital, video pole camera was

"hid[den] . . . out of sight of its targets."               It further found

that   law    enforcement   used     the    camera   to     "surreptitiously

surveil[]" the Hadley Street residence.




government does not assert that its use of the pole camera to
create the compendium at issue was supported by any quantum of
suspicion.   We thus must assess the constitutionality of the
government's use of this surveillance on the understanding that it
had no reasonable basis to suspect wrongdoing by the defendants at
the relevant time.


                                    - 8 -
            ATF agents were able to view a live-stream of what the

camera recorded through a password-protected website.              The agents

also could, remotely, pan, tilt, and zoom3 the camera to better

focus on individuals or objects of interest.

            When not zoomed, the camera had within its view roughly

half of the front structure of the 120 Hadley Street residence,

including   its   side   entrance    and    a   gardening   plot   near   that

entrance, the whole of the home's private driveway, the front of

the home's garage, much of the home's front lawn, and the vast

majority of the walkway leading from the home's private driveway

up to the home's front door (although not the front door itself).4

The camera also had within its view a portion of the public street




     3 The camera's zoom feature enabled a significant level of
magnification. Although the record does not disclose the camera's
precise capability on that dimension, the government in filings
below "analogized [that] feature to a law enforcement agent using
binoculars." Images in the record reflect that, by zooming, the
camera was able to accurately capture facial expressions, details
on clothing, small objects in a person's hands (such as keys or a
cigarette), and the license plate numbers of cars parked in the
residence's private driveway.
     4 The government represented to the District Court at the
suppression hearing on May 13, 2019, that the pole camera did not
have "a full clear view of the entire exterior of the home" as
there was "one tree that partially obfuscate[d] the view of the
pole camera." The government then explained in a subsequent filing
that, at least during the winter, "there was no obstruction -- the
leaves had fallen and the view was clear." In this respect, we
note that the pole camera was in place surveilling the home from
May 2017 until January 2018.

                                    - 9 -
that ran parallel to the front of the house and perpendicular to

the private driveway.

            Because of the positioning of the camera, it was not

able to peer into the home's interior.     However, images in the

record taken from the footage captured by the camera indicate that

the camera could discern the presence of a person looking out the

front windows of the house and see inside the front of the garage

when its door was up.

            The camera recorded in color, but it did not record

audio.     The camera's footage was digitally stored and could be

retrieved and re-watched at any time.

            The camera could and did operate at night, but the

resulting footage was lower in quality.     For example, when the

camera recorded in the dark, it became more difficult -- although

not impossible -- for the camera accurately to depict license plate

numbers.

            The camera recorded the Hadley Street residence for

approximately eight months without interruption.       It captured

numerous comings, goings, and occurrences in the front curtilage

of the residence -- from the mundane (such as persons going to and

from the residence, parking, smoking cigarettes, or taking out the

trash) to the potentially incriminating.     The resulting record

included all these movements and interactions.      The government

does not represent that law enforcement officers were continuously

                               - 10 -
watching    the    livestream      of    the     video    while    the    camera      was

recording.

                                          B.

            A federal grand jury indicted Moore-Bush on January 11,

2018, for conspiracy to distribute and possess with intent to

distribute heroin and cocaine base in violation of 21 U.S.C.

§§ 841(a)(1),      846.        Moore-Bush      was     also   subject     to     a   drug

forfeiture allegation under 21 U.S.C. § 853. Four other defendants

(but not Moore) were named in that indictment.

            Moore-Bush was arrested the following day.                         The pole

camera was removed soon after Moore-Bush's arrest, which occurred

about eight months after the camera began recording.

            Nearly a year after Moore-Bush's arrest, on December 20,

2018, a grand jury returned a superseding indictment that charged

Moore-Bush and, for the first time, her mother, Moore.                                 The

superseding       indictment     charged       Moore-Bush      with,     among       other

crimes,    conspiracy     to    distribute       and     possess   with    intent       to

distribute heroin, cocaine, and cocaine base in violation of 21

U.S.C.     §§ 841(a)(1),        846     (Count    One);       distribution       and/or

possession    with     intent     to     distribute       various      narcotics        in

violation of 21 U.S.C. § 841(a)(1) and 18 U.S.C. § 2 (Counts Two

through Six); conspiracy to deal firearms without a license in

violation of 18 U.S.C. § 371 (Count Twenty); and dealing firearms

without a license in violation of 18 U.S.C. § 922(a)(1)(A) (Counts

                                        - 11 -
Twenty-One and Twenty-Two).5     The superseding indictment also

charged Moore with, among other crimes, conspiracy to distribute

and possess with intent to distribute heroin, cocaine, and cocaine

base in violation of 21 U.S.C. §§ 841(a)(1), 846 (Count One); and

distribution and possession with intent to distribute heroin,

cocaine, and cocaine base in violation of 21 U.S.C. § 841(a)(1)

(Count Three).6

          On April 22, 2019, Moore moved to suppress the record

created by the pole camera and all "fruits" of it.      Moore-Bush

filed a similar suppression motion on May 2, 2019.     Each motion

argued that law enforcement had engaged in a warrantless search

within the meaning of the Fourth Amendment that was unreasonable

based on "the prolonged, covert use of a hidden pole camera to

. . . record the activities associated with" the Hadley Street

residence for a period of eight months.




     5 Moore-Bush was also charged with conspiracy to launder money
in violation of 18 U.S.C. § 1956(h) (Counts Seven and Eight); money
laundering in violation of 18 U.S.C. §§ 2, 1956(a)(1) (Counts
Eleven and Fourteen through Nineteen); and aiding and abetting the
possession of a firearm by a felon, in violation of 18 U.S.C. §§ 2,
922(g)(1) (Count Twenty-Three). She faced a drug forfeiture charge
as well.
     6 Moore was also charged with money laundering and money
laundering conspiracy in violation of 18 U.S.C. § 1956(a)(1), (h)
(Counts Eight and Fourteen through Nineteen); and making false
statements to federal agents in violation of 18 U.S.C. § 1001
(Count Twenty-Four). She also faced a drug forfeiture charge.

                               - 12 -
           The government did not contend that this surveillance

was supported by either probable cause or reasonable suspicion to

believe that a crime had been committed, let alone that it was

authorized by a warrant.      Rather, the government contended that

the defendants' suppression motions must be rejected because,

under this circuit's decision in Bucci, which applied Katz v.

United States, 389 U.S. 345 (1967), the "images captured by the

pole camera [did not] violate[] the [d]efendant[s'] objectively

reasonable expectation of privacy in the view of" the curtilage of

their home and so no Fourth Amendment search had occurred.            The

government thus contended that it could use, in the defendants'

criminal cases, any digital video footage or still images captured

by the pole camera over the eight-month span in which it was in

operation, including any images that the camera had captured "from

November 2017 through January 2018."

           In Bucci, a panel of this court addressed a motion to

suppress   that   concerned   evidence    produced   by   a   government-

installed digital video pole camera that had been pointed for eight

months at the front of the defendant's home as part of a criminal

investigation.    582 F.3d at 116.       Bucci in a brief paragraph of

analysis rejected the defendant's motion to suppress.            It held

that the surveillance     conducted via the pole camera          did not

interfere with any subjective expectation of privacy on the part

of the defendant because the defendant had taken no measures to

                                - 13 -
hide the activities that occurred in his home's curtilage from

public    view.   Id.   at   116.   Bucci   also   observed   that   the

surveillance did not interfere with any objectively reasonable

expectation of privacy on the part of the defendant, because the

images captured by the camera were solely of conduct that had

occurred in public view.     Id. at 117.

            Notwithstanding Bucci, the District Court on June 3,

2019, granted both defendants' motions to suppress the digital

record created by the pole camera and any of the record's fruits.7

The District Court concluded in so ruling that Bucci was no longer

binding precedent because it conflicted with a subsequent Supreme

Court precedent, Carpenter v. United States, 138 S. Ct. 2206

(2018).    See United States v. Moore-Bush, 381 F. Supp. 3d 139,

144-45 (D. Mass. 2019).

            Carpenter followed United States v. Jones, 565 U.S. 400

(2012), which was itself decided three years after Bucci.            The

Supreme Court determined in Jones that the "installation of a GPS

tracking device on a target's vehicle" to "monitor the vehicle's

movements" for twenty-eight days "constitut[ed] a search . . .

within the meaning of the Fourth Amendment."       Jones, 565 U.S. at

404-05.    The majority opinion in Jones based that conclusion on

the common-law trespassory test for determining whether a Fourth


     7 The order was amended the following day in ways that are
not relevant to the issues before us.

                                - 14 -
Amendment search had occurred because the GPS-tracking device had

been affixed by law enforcement to the target's vehicle without

the vehicle owner's knowledge or permission.               Id. at 405-06, 409,

411.    Five Justices across two concurrences, however, also found

in that case that a Fourth Amendment search had occurred under the

"reasonable expectation of privacy" test from Katz because "longer

term GPS monitoring . . . impinges on expectations of privacy"

that one reasonably has in the entirety of one's movements -- even

when made in public -- over a substantial period.                    Id. at 430

(Alito, J., concurring in the judgment joined by three Justices);

see also id. at 415 (Sotomayor, J., concurring).

           Carpenter presented the Court with a somewhat similar

question to the one presented in Jones, as it, too, raised a

question     about   whether    the    use    of     warrantless,     long-term

electronic    surveillance     comported      with   the    Fourth   Amendment.

Specifically,    the   issue    in    Carpenter      concerned   whether    the

government had conducted a search within the meaning of the Fourth

Amendment when it "accessed" -- without a warrant -- seven days'

worth of historical cell-site location information ("CSLI") from

a wireless carrier by requesting that the wireless carrier provide

that information.      See Carpenter, 138 S. Ct. at 2212, 2217 n.3,

2219.

           The Court concluded in Carpenter that, under Katz, the

government had conducted a search by "access[ing]" through the

                                     - 15 -
request to the wireless carrier that amount of CSLI both because

"an individual maintains a legitimate expectation of privacy in

the record of his physical movements as captured through CSLI" --

even if those movements take place in public -- and because the

"access[ing]" of that amount of the defendant's historical CSLI

from the wireless carrier "contravene[d] that expectation."            Id.

at 2217, 2219.    The Court reached that conclusion even though the

government had received from the wireless carrier only two days'

worth of the total of the seven days' worth of the historical CSLI

that the government had requested from the wireless carrier.            See

id. at 2212.

          The District Court "read[] Carpenter . . . to cabin --

if not repudiate -- th[e] principle" that Bucci's reasoning had

rested on: that, as a categorical matter, "[a]n individual does

not have an expectation of privacy in items or places he exposes

to the public."       Moore-Bush, 381 F. Supp. 3d at 144 (third

alteration in original) (quoting Bucci, 582 F.3d at 116-17).

Having concluded that, after Carpenter, Bucci was not binding on

that point, the District Court then held that a Fourth Amendment

search had occurred here.     Id. at 148-49.

          The District Court explained that the defendants had

"exhibited   an   actual,   subjective    expectation   of   privacy   that

society recognizes as objectively reasonable" in the "aggregate"

of what was visible to the pole camera over the eight months that

                                 - 16 -
the camera was recording.     Moore-Bush, 381 F. Supp. 3d at 143.

The District Court also analogized the digital record accessed by

the government here to the twenty-eight days' worth of GPS data

that the government in Jones had obtained from the GPS tracker

that the government had installed on the defendant's vehicle in

that case and the seven days' worth of the historical CSLI that

the government had accessed from the wireless carrier in Carpenter.

Id. Moreover, as the government did not argue that it had complied

with the Fourth Amendment insofar as a search within the meaning

of that Amendment had occurred, the District Court granted the

defendants' motions to suppress the digital record that had been

created from the pole-camera surveillance and any evidence derived

from it.   Id. at 149-50.

           The government filed a motion for reconsideration on

June 5, 2019.   The government argued in that motion for the first

time that even if a search had occurred the good-faith exception

recognized in Davis "applies here and precludes suppression of the

government's pole camera evidence" due to Bucci having been on the

books at the relevant time.   The District Court denied the motion.

           The government, relying on 18 U.S.C. § 3731, timely

appealed the District Court's order that granted the defendants'

motions to suppress, as well as the District Court's order that

denied the motion for reconsideration.    The government's appeals



                               - 17 -
of those orders were consolidated for purposes of briefing and

argument.

            A panel of this court reversed the order of the District

Court that granted the defendants' motions to suppress.         The panel

concluded that the District Court transgressed both Bucci -- which

the panel concluded remained binding on the "search" point in this

circuit even after Jones and Carpenter -- and Carpenter, given the

limitations on that ruling that the panel determined that the

Supreme Court had placed on it.      United States v. Moore-Bush, 963

F.3d 29, 31 (1st Cir. 2020), reh'g en banc granted, vacated, 982

F.3d 50 (1st Cir. 2020).

            The opinion concurring in the result agreed that Bucci

was binding on the panel and the District Court under the law-of-

the-circuit doctrine.     See id. at 48-49 (Barron, J., concurring in

the result). The opinion concurring in the result expressed doubt,

however, as to whether Bucci had correctly applied the Supreme

Court's     Fourth   Amendment   precedents   tracing    back   to   Katz,

especially given the recent guidance that Carpenter had provided.

See id. at 53-56.     The concurring opinion thus concluded that "the

proper course for our Court is to use this case to give Bucci fresh

consideration en banc, so that we may determine for ourselves

whether the result that it requires [the panel to reach] is one

the Supreme Court's decisions . . . prohibit."          Id. at 58.



                                  - 18 -
          The defendants filed petitions for rehearing en banc,

which were granted, and the panel's ruling reversing the District

Court's order granting the defendants' suppression motions was

vacated. United States v. Moore-Bush, 982 F.3d 50 (1st Cir. 2020).

We   consider in what follows       both    the District Court's    order

granting the defendants' motions to suppress, reviewing "findings

of fact for clear error and the application of the law to those

facts de novo," United States v. Crespo-Ríos, 645 F.3d 37, 41 (1st

Cir. 2011) (quoting United States v. Siciliano, 578 F.3d 61, 67

(1st Cir. 2009)); see also United States v. Orth, 873 F.3d 349,

353 (1st Cir. 2017), and the District Court's order denying the

government's motion to reconsider, reviewing for an abuse of

discretion, see United States v. Siciliano, 578 F.3d 61, 72 (1st

Cir. 2009).

                                II.

          The Fourth Amendment provides for "[t]he right of the

people to be secure in their persons, houses, papers, and effects,

against   unreasonable   searches     and    seizures."   U.S.     Const.

amend. IV.    That Amendment further provides that a search is

"presumptively unreasonable" in the absence of a warrant supported

by probable cause.   See United States v. Karo, 468 U.S. 705, 715

(1984).

          The Supreme Court has, as we have indicated, set forth

two tests to assess whether government conduct constitutes a

                               - 19 -
"search" within the meaning of the Fourth Amendment.                The parties

agree that the first test -- "the common-law trespassory test,"

Jones, 565 U.S. at 409 -- is not relevant here because it applies

only   when    the    government     "obtains   information    by   physically

intruding on a constitutionally protected area."              Id. at 405, 406

n.3. Our focus, therefore, is on the second test, which is derived

from Katz.      Under that test, as explicated in Carpenter, "[w]hen

an individual 'seeks' to preserve something as 'private,' and his

expectation of privacy is            'one'   that society is prepared to

recognize as 'reasonable,'" a government action that "contravenes

that expectation" "generally qualifies as a search."                Carpenter,

138 S. Ct. at 2213, 2217 (quoting Smith v. Maryland, 442 U.S. 735,

740 (1979)).

              Thus, we first must determine whether Moore-Bush and

Moore each manifested an expectation of privacy in what each seeks

to   preserve    as   private   --    namely,   "the   totality     of   [their]

movements and activities and associations with family members and

visitors in the front [curtilage] of" their home that was visible

to the pole camera during the eight-month-long period that it

recorded.     As we will explain, we conclude that the District Court




                                      - 20 -
supportably   found   that   the   defendants    did      manifest   such   an

expectation of privacy.8

          Having so concluded, we next must determine whether such

an expectation is one that society is prepared to accept as

reasonable.   As we will explain, we conclude that the District

Court correctly held that it is.

          Because we conclude that the defendants have shown what

they must with respect to the "expectation of privacy" portion of

the Katz inquiry, we then must address whether the government's

"accessing"   of   the   record    at   issue   --   to    use   Carpenter's

terminology -- "contravened" that expectation. As we will explain,

we conclude that the accessing of that record did.

          We emphasize that the government advances no argument to

the en banc court -- nor, for that matter, did it advance any

argument below -- that, even though it had not obtained a warrant

that authorized its use of this surveillance, its use of such

surveillance still comported with the Fourth Amendment because


     8  We note neither party disputes that the quantum of
information at issue in this case is inclusive of not only each
defendant's own visible activity in the defendants' front
curtilage but also of what is effectively a live-action log of all
visitors to their home during the eight-month period in which the
pole camera operated. We note, too, that the government does not
dispute that if the defendants are fairly deemed to have a
subjective expectation of privacy in such information that society
is prepared to accept as reasonable, then it is an expectation of
privacy that the Fourth Amendment -- given its protection of
"houses" -- protects, insofar as that expectation is contravened
by the government.

                                   - 21 -
some       quantum   of    suspicion   supported     the    surveillance   and    an

exception       to   the    warrant    requirement       applied.     Rather,    the

government relies solely on the contention that its use of the

pole camera -- and, implicitly, the accessing of the record created

by it -- was not a "search" because the camera captured only what

was already exposed to public view, such that the government did

not need any level of suspicion whatsoever, let alone a warrant,

to undertake such surveillance and access the record created by

it. Thus, because we conclude that a search did occur, we conclude

--   unlike      our      colleagues   --   that   the     Fourth   Amendment    was

violated.9

               Nevertheless, as we will explain in the concluding part

of this opinion, we still conclude that the District Court's order

granting the defendants' suppression motions must be reversed.

And, that is because we conclude that the good-faith exception to

the warrant requirement that is set forth in Davis requires that

result, given that Bucci was the law of this circuit at the

relevant time.



       We note that although our colleagues contend that either
       9

probable cause or reasonable suspicion supported the use of the
pole-camera surveillance at issue, Concur. Op. at 105, they do not
explain why the presence of reasonable suspicion or probable cause
would on its own render the use of pole-camera surveillance of the
kind that was used here constitutional, given that the Fourth
Amendment ordinarily requires there to be both probable cause and
a warrant    before law enforcement can conduct         a search
constitutionally.

                                        - 22 -
                                         III.

               We start with the "expectation of privacy" portion of

the Katz inquiry.          That portion requires us to determine -- at

least arguably -- two distinct things:                  whether Moore-Bush and

Moore    can    show     that   they   "exhibited      an   actual,      subjective,

expectation of privacy" in the aggregate of what the pole camera

captured, and whether they can show that "society is prepared to

recognize        [that     subjective          expectation]     as       objectively

reasonable."      United States v. Rheault, 561 F.3d 55, 59 (1st Cir.

2009) (citing Smith, 442 U.S. at 740).               We address each component

of this portion of the Katz inquiry in turn.

                                          A.

               The District Court found with respect to the subjective

expectation of privacy portion of the Katz inquiry that Moore-Bush

and   Moore     did    show     that   they    had   "manifested     a    subjective

expectation of privacy through the relevant actions that they

took."    Moore-Bush, 381 F. Supp. 3d at 143.                 The District Court

explained that it inferred "from [Moore-Bush and Moore's] choice

of neighborhood and home within it that they did not subjectively

expect to be surreptitiously surveilled with meticulous precision

each and every time they or a visitor came or went from their home"

and that a digital and easily searchable video record of eight

months of those movements would be compiled.                  Id. at 144.



                                        - 23 -
               The government does not challenge the District Court's

findings       regarding     the    characteristics        of     the    defendants'

neighborhood and home, see id. at 143.                  The government also does

not    contend    that    the     record     suggests   that    the     occupants   of

120 Hadley      Street     invited,     in   any   affirmative     way,    long-term

surveillance of the home by a digital video camera. The government

does not even suggest that the defendants were aware that video

cameras of any kind were trained on the Hadley Street property for

any period of time and yet took no steps to shield the curtilage

of the residence from that form of surveillance.                      Cf. Shafer v.

City of Boulder, 896 F. Supp. 2d 915, 930 (D. Nev. 2012).

               The government focuses solely on what the defendants

failed to do despite their lack of awareness that any digital

surveillance      was    being     conducted:      "erect[]     fences    or   plant[]

hedges to obscure the view from the street." The government relies

heavily in doing so on Bucci, which observed that the defendant in

that    case     had    "failed    to   establish . . . a         subjective . . .

expectation of privacy in the front of his home" because there

were "no fences, gates or shrubbery located [out] front . . . that

obstruct[ed] the view of the driveway or the garage from the

street."       Bucci, 582 F.3d at 116-17.

               Bucci did not grapple, however, with the contention that

is front and center here -- that the claimed expectation of privacy

is only in the totality of what transpired within the area of the

                                        - 24 -
property at issue over the months in question and not in any

discrete occurrences that, one by one, happened to take place there

during that time. Instead, Bucci appeared to treat the defendant's

claimed expectation of privacy in that case as if it were no

different from a defendant's claimed expectation of privacy in a

discrete activity that occurs in the curtilage of a residence and

may be seen from the street by any passerby at the moment of its

occurrence.    See id.

           The government is right that Bucci relied in this part

of its analysis on the Supreme Court's decision in California v.

Ciraolo.   See Bucci, 582 F.3d at 117-18.    So, we must consider

whether that precedent itself compels us to credit the government's

contention regarding the subjective expectation of privacy portion

of the Katz inquiry even though Bucci does not.       But, Ciraolo,

too, is distinguishable from this case.

           In Ciraolo, the Supreme Court did point to the fact that

the defendant there had erected a fence in finding that he had

established that he had a subjective expectation in keeping private

what he sought to hide from view -- his backyard agriculture

activity, or, more pointedly, his marijuana plants.    Ciraolo, 476

U.S. at 211.   The Court did so, moreover, even though such "normal

precautions" against "casual, accidental observation" would have

provided little protection to the defendant from the type of

surveillance that the government used there: photography from a

                               - 25 -
low-flying plane.     Id. at 211-12 (quoting Rawlings v. Kentucky,

448 U.S. 98, 105 (1980)).

          Ciraolo thus does suggest, by negative implication, that

because a casual observer could have noticed an unobstructed plot

of marijuana plants by just walking by the defendant's home, a

defendant's failure to erect a fence or hedges to protect such a

plot from being casually observed in that manner would signal a

willingness on the part of that defendant to permit any passerby

to observe it.   And, that is so, Ciraolo indicates, even if a mere

passerby happened to have a vantage point -- whether from a utility

truck or a double-decker bus, id. at 211 -- that was high enough

to permit a view of the plot that no fence or hedges would be high

enough to block.

          We   have   not   yet   encountered,   however,   the   "casual,

accidental observ[er]," id. at 212 -- whether viewing from on the

ground or on high -- who could take in all that occurs in a home's

curtilage over the course of eight months and recall it perfectly

and at a moment's notice.     Thus, we see little sense in inferring

that the defendants here lacked, as a subjective matter, their

claimed expectation of privacy simply because they failed to take

measures that would at most protect against casual observation of

the curtilage of their residence when casual observation of the

curtilage -- from whatever vantage -- would in no way undermine

that claimed expectation, given that the expectation inheres in

                                  - 26 -
the aggregate of activity in question.10       The government thus errs

in arguing that Ciraolo shows that the failure of the defendants

in this case to put up a fence or similar barrier around the front

of   the   Hadley   Street   home    necessarily   precludes   them   from

establishing that they had the subjective expectation of privacy

that they claim.

            We do note, moreover, that it is possible that the

inquiry into a defendant's subjective expectation of privacy in

the whole of what transpires over a very long time in the front of

one's home, when each discrete activity in that totality is itself

exposed to public view, is a corollary of whether that claimed

expectation of privacy in the aggregate of what transpires there



      10Our colleagues contend that even if no "casual" observer
witnesses and records the whole of what occurs in the curtilage of
a home, a nosy neighbor might.     Concur. Op. at 118, 122.    Our
colleagues go on to contend, for that reason, that the failure of
Moore-Bush and Moore to take precautions to avoid being seen by
neighbors suggests that they lacked a subjective expectation of
privacy with respect to the aggregate of those movements. Concur.
Op. at 112-13.
     Perhaps a nosy neighbor could become familiar with some of
the daily rituals of those who live nearby. And, perhaps -- if
particularly dedicated -- that neighbor could even log those
observations as our colleagues suggest.      But, it dramatically
undersells the hypothesized neighbor's distinctive character to
describe that neighbor as merely "nosy," given the unrelenting and
all-encompassing kind of surveillance that is at issue. Thus, we
do not see how the awareness of neighbors -- including even of
those neighbors one might wish would move to a different block --
suffices to undermine the District Court's finding that these
defendants manifested their subjective expectation of privacy in
what they claim to wish to keep from public view.

                                    - 27 -
is   objectively     reasonable.          We    can    see    how    the   objective

reasonableness of an expectation that such activities are not being

catalogued in a manner that would make the compendium of them

accessible to an observer upon command might bear on whether a

defendant's failure to protect against a casual observer's viewing

each activity one by one supports an inference that the defendant

is in fact, as a subjective matter, willing to permit such an

easily searchable catalogue of the activities in the aggregate to

be compiled.       Cf. Hudson v. Palmer, 468 U.S. 517, 525 n.7 (1984)

(characterizing      the    Katz   test    as       primarily      being   about    the

objective inquiry and stating that "[t]he Court[] [has] refus[ed]

to   adopt     a     test    of    'subjective            expectation'"         because

"constitutional rights are generally not defined by the subjective

intent of those asserting the rights" (quoting Smith, 442 U.S. at

740-41   n.5));     Smith,   442   U.S.        at   741    n.5     (explaining     that

"[s]ituations can be imagined, of course," such as those in which

"an individual's subjective expectations ha[ve] been 'conditioned'

by influences alien to well-recognized Fourth Amendment freedoms,"

"in which Katz['s] two-pronged inquiry would provide an inadequate

index    of   Fourth    Amendment     protection"            and    that   in     those

"circumstances[,] . . . subjective expectations obviously could

play no meaningful role in ascertaining what the scope of Fourth

Amendment protection was" and instead when "determining whether a

'legitimate expectation of privacy' existed in such cases, a

                                    - 28 -
normative inquiry would be proper").          We can especially see the

sense in so concluding to the extent that combining the subjective

and objective components of the "expectation of privacy" inquiry

would help to avoid the Fourth Amendment being held to mean one

thing for those living in a quiet neighborhood of single-family

homes and another for those living in a neighborhood of apartments

or attached houses.

           To that same point, there is no Supreme Court precedent

of which we are aware that clearly indicates that the subjective

and objective inquiries in this context are properly understood to

be wholly distinct.     The only cases from the Court to address an

even arguably analogous claimed expectation of privacy are Jones

and   Carpenter.     And,    neither   case   addresses   the   subjective

expectation of privacy component of the Katz inquiry, as Jones did

not rely on the Katz test, Jones, 565 U.S. at 407-08, and Carpenter

addressed only the objective component of the "expectation of

privacy" portion of the Katz inquiry, Carpenter, 138 S. Ct. at

2217-19.

           But,    insofar   as   an   independent   inquiry    into   the

subjective expectation of privacy is required, we conclude, for

reasons that we have explained, the District Court did not err in

finding that the defendants here have made the requisite showing.

And, we emphasize, this conclusion accords with Carpenter, even if

it is not, strictly speaking, compelled by it.

                                  - 29 -
          True,   Carpenter   did      not   address   the   subjective

expectation of privacy component of the Katz inquiry.          But, we

decline to conclude that, after Carpenter, a court could find in

a case involving the same facts as were involved there that no

search had occurred simply based on the defendant's failure to

have taken countermeasures that at most would have protected his

public movements from being subjected to casual observation.11

Nor, we note, does the government suggest that Carpenter may be

read to permit such an outcome.

                                  B.

          We move on, then, to the defendants' contention that

their subjective expectation of privacy in what they seek to shield

from the view of others is also an "expectation . . . that society

is prepared to accept as reasonable."        Carpenter, 138 S. Ct. at

2213 (quoting Smith, 442 U.S. at 740).       Our focus in undertaking

this portion of the Katz inquiry, we emphasize, is not on whether

these defendants have a reasonable expectation of privacy in each

discrete activity -- considered on its own and at the time that it

occurred -- that was visible to the pole camera over the course of


     11 We thus disagree with our colleagues that the defendants
here were required to build a fence or otherwise "take . . . steps
to prevent observation" of "many" but "not all" of the activities
in the front curtilage of their home. To require as much of the
defendants here would be analogous to requiring the defendant in
Carpenter to have manifested a subjective expectation of privacy
by traveling around town in a disguise, and we do not understand
Carpenter to permit that requirement to be imposed.

                              - 30 -
the many months that it was up and running.             The expectation of

privacy that Moore-Bush and Moore each claims inheres solely in

what they characterize as "the totality of [their] movements and

activities and associations with family members and visitors in

the front [curtilage] of [their] home" that was recorded by the

pole camera. In other words, they assert an expectation of privacy

in the whole of the activities in that locale -- taken as a whole

-- that were visible to the pole camera during the lengthy period

of time in question, just as the expectation of privacy that the

defendant in Carpenter -- and the defendant in Jones, for that

matter -- claimed was in an aggregate of the movements taken in

public over a relatively long period of time and not in each of

those movements individually at the moment of its occurrence.

            Moreover, Moore-Bush and Moore acknowledge, as they must

-- and as both Bucci and our colleagues emphasize -- that the Court

has made clear that, in general, "[w]hat a person knowingly exposes

to   the   public . . .   is   not   a   subject   of    Fourth   Amendment

protection."    Katz, 389 U.S. at 351.        They rightly point out,

however, that Katz itself noted -- in a passage from that case

that neither Bucci nor our colleagues invoke -- that "what [a

person] seeks to preserve as private, even in an area accessible

to the public, may be constitutionally protected."                Id.   The

defendants also rightly emphasize that Carpenter invoked just that

passage in Katz both to explain that "[a] person does not surrender

                                 - 31 -
all Fourth Amendment protection by venturing into the public

sphere,"   Carpenter,   138   S.   Ct.    at   2217,   and   to   support   the

conclusion that "individuals have a reasonable expectation of

privacy in the whole of their physical movements," even if those

movements take place in public view, id.

           Thus, a critical question here -- though an affirmative

answer to it is not itself dispositive of whether a search occurred

-- concerns whether Carpenter's reasons for concluding that the

claimed expectation of privacy in the whole of the movements that

was at issue in that case was objectively reasonable justify our

reaching the same conclusion with respect to the similar, but still

distinct, claimed expectation of privacy that we confront in this

case.   As we will next explain, we conclude that those reasons do.

                                     1.

           Carpenter acknowledged that a person generally "has no

reasonable expectation of privacy in his movements from one place

to another" because such movements are "voluntarily conveyed to

anyone who want[s] to look."        Id. at 2215 (quoting United States

v. Knotts, 460 U.S. 276, 281 (1983)).                  But, the Court then

explained, this general point does not dictate whether society is

prepared to accept as reasonable a claimed expectation of privacy

in the whole of "every single movement of an individual[] . . .

for a very long period."      Id. at 2217 (quoting Jones, 565 U.S. at

430 (Alito, J., concurring in the judgment)).            In fact, Carpenter

                                   - 32 -
explained, based on the concurring opinions in Jones, "[a] majority

of this Court has already recognized that individuals have a

reasonable expectation in the whole of their public movements."

Id. (citing Jones, 565 U.S. at 430 (Alito, J., concurring in the

judgment joined by three Justices) and Jones, 565 U.S. at 415

(Sotomayor, J., concurring)).

          Carpenter    elaborated   that    its   recognition   of    the

reasonableness   of   this   expectation   of   privacy   reflected   the

limited state of surveillance technology for most of our history.

"Prior to the digital age," the Court observed, "law enforcement

might have pursued a suspect for a brief stretch, but doing so

'for any extended period of time was difficult and costly and

therefore rarely undertaken.'"       Id. (emphasis added) (quoting

Jones, 565 U.S. at 429 (Alito, J., concurring in the judgment)).

Carpenter noted in this regard that it was almost inconceivable

until relatively recently that the government would, other than at

most rarely, have the resources to "tail[] [a suspect] every moment

of every day for five years," which was a reference to the amount

of time that the wireless carrier for the defendant in Carpenter

stored the CSLI that it collected from its customers.       Id. at 2218.

          Thus, Carpenter     concluded,   expressly drawing on the

similar reasoning of the concurring Justices in Jones, "society's

expectation has been that law enforcement agents and others would

not -- and, indeed, in the main, simply could not -- secretly

                                - 33 -
monitor and catalogue every single movement of an individual's car

for a very long period."   Id. at 2217 (quoting Jones, 565 U.S. at

430 (Alito, J., concurring in the judgment)).   That being so, the

Court concluded in Carpenter, it was reasonable for a person to

expect that no such tracking was occurring as he moved about in

public over a lengthy period and thus to expect that those public

movements were, taken as a whole, private in consequence of the

practical anonymity with respect to the whole of them that follows

from the reality that virtually no one has a feasible means of

piercing it.   Id.

                                2.

          In arguing that neither Carpenter nor Jones supports the

defendants here with respect to this portion of the Katz inquiry,

the government contends that neither of those two precedents is

analogous to this case because each addresses a claimed expectation

of privacy in the whole of a person's physical movements over a

long stretch of time while that person is moving about from one

place to another.    See id. at 2214; Jones, 565 U.S. at 402.   By

contrast, the government emphasizes, as do our colleagues, Concur.

Op. at 114, that the claimed expectation of privacy here is only

in what occurred over a lengthy stretch of time at a single locale

-- the defendants' Hadley Street home.    The government contends

that while society may be prepared to accept as reasonable one's

expectation of privacy in the whole of one's public movements from

                              - 34 -
place to place over a substantial stretch of time, society is not

prepared to accept as reasonable one's expectation of privacy in

the whole of what one exposes to public view during such a period

in a single place.    We cannot agree -- at least given the place

that we are talking about here.

                                  a.

          The government attempts to support its contention about

what society is prepared to accept as reasonable in part by

pointing to documented instances in which teams of law enforcement

officers have diligently watched a single place of interest for a

period of time that has ranged from three weeks12 to three months.13

That recent history fails to show, though, that one reasonably

would expect such lengthy stakeouts of the home to be undertaken

more than "rarely."   Carpenter, 138 S. Ct. at 2217 (quoting Jones,

565 U.S. at 429 (Alito, J., concurring in the judgment)).      And,

under Carpenter, evidence of such infrequent surveillance does

nothing to undermine the reasonableness of a claimed expectation

of privacy in the whole of what transpires in a publicly visible

manner over a sustained expanse of time in a single place, at least

insofar as what does transpire there over that expanse of time


     12See, e.g., United States v. Gramlich, 551 F.2d 1359, 1362
(5th Cir. 1977) (surveilling the property for three weeks).
     13See, e.g., United States v. Jimenez, 5 F.3d 1494, No. 92-
1997, 1993 WL 391395, at *1 (5th Cir. Sept. 21, 1993) (unpublished
table decision) (surveilling the property for three months).

                               - 35 -
reveals the "privacies of life" when considered in the aggregate.

Id. (quoting Riley v. California, 573 U.S. 373, 403 (2014)).

             Consistent with this understanding, Carpenter concluded

that one reasonably leaves one's home without expecting a perfect

form of surveillance to be conducted over a long period of time,

even though "tailing" for non-trivial periods of time has always

been possible.           See id. at 2218; see also Jones, 565 U.S. at 416

(Sotomayor, J., concurring) (explaining that the Court should "not

regard as dispositive the fact that the government might obtain

the    fruits       of    GPS   monitoring     through        lawful   conventional

surveillances techniques").              That is so, Carpenter explained,

because     the     time,    labor,    and    expense    of    carrying   out    such

surveillance in a pre-digital age rendered it at most a rare

practice, such that one could not reasonably be expected by our

society (given that it is a free one) to govern one's actions in

traveling about town as if a tail were always already underway.

138 S. Ct. at 2217; cf. United States v. Tuggle, 4 F.4th 505, 526

(7th Cir. 2021), cert. denied, 142 S. Ct. 1107 (2022) ("We . . .

close the door on the notion that surveillance accomplished through

technological        means      is    constitutional      simply       because    the

government could theoretically accomplish the same surveillance

--    no   matter    how    laborious    --    through   some     nontechnological

means.").



                                        - 36 -
            True, no tailing need be conducted here to capture what

these defendants seek to keep private; a single-point stakeout

would suffice.        But, the government provides us with no reason to

conclude that "[p]rior to the digital age," Carpenter, 138 S. Ct.

at 2215, it would have been appreciably less difficult to conduct

a stakeout that could effectively and perfectly capture all that

visibly occurs in front of a person's home over the course of

months -- and in a manner that makes all of the information

collected readily retrievable at a moment's notice -- than it would

have been to conduct roving surveillance of perfect precision of

all of one's movements outside the home over the course of a week

(using Carpenter's own measure) or a month (using the measure of

the majority of the Justices in Jones).14               Indeed, we must take

account of not merely the practical limits of manpower and expense

that -- in the pre-digital era -- would have made such lengthy,

24/7 surveillance of anyone in any place a most rare occurrence.

See Tuggle, 4 F.4th at 526 ("To assume that the government would,

or even could, allocate thousands of hours of labor and thousands

of   dollars     to   station   agents   atop   three    telephone   poles   to

constantly monitor [the defendant]'s home for eighteen months

defies     the   reasonable     limits    of    human    nature   and   finite


       We recognize that Carpenter did also refer to the fact that
      14

wireless carriers retain CSLI for five years. But, we do not see
any material difference for purposes of the inquiry that Katz
requires between that period and the eight-month period before us.

                                    - 37 -
resources.").      We also must take account of the practical limits

in that earlier era of conducting such an enduring, undetected

watch of a home.

              Accordingly,   we    conclude        that    the    same   real-world

constraints that contributed to the sense of privacy that the Court

has recognized one reasonably had for most of our nation's history

in the totality of the picture -- though not in each brushstroke

-- painted by the whole of one's movements while traveling in

public also contributed to that same sense in the full portrait of

all that visibly occurs for many months in the curtilage of one's

own   home.      Cf.    Jones,    565   U.S.   at     415-16      (Sotomayor,    J.,

concurring) ("[B]ecause GPS monitoring is cheap in comparison to

conventional surveillance techniques, . . . it evades the ordinary

checks that constrain abusive law enforcement practices: 'limited

police resources and community hostility.'" (quoting Illinois v.

Lidster, 540 U.S. 419, 426 (2004))); id. at 429 (Alito, J.,

concurring in the judgment) ("Devices like the [GPS device] . . .

make long-term monitoring relatively easy and cheap.").                         This

understanding,     we   further    note,     comports      with    the   protection

afforded   by    the    common    law   in   response       to    developments    in

surveillance     technology      through     the    tort    of    intrusion     upon

seclusion.     See, e.g., Nader v. Gen. Motors Corp., 255 N.E.2d 765,

771 (N.Y. 1970) (explaining that the mere fact that something

occurs in public does not necessarily indicate a willingness to

                                     - 38 -
reveal that action to others and distinguishing between what could

be seen by a "casual observer" and what could be seen by a person

conducting "overzealous" surveillance); cf. Restatement (Second)

of Torts § 652B (1977) (explaining that the tort of intrusion upon

seclusion   protects    against   intrusion        "upon   the   solitude   or

seclusion of another or his private affairs or concerns"); Samuel

D. Warren & Louis D. Brandeis, The Right to Privacy, 4 Harv. L.

Rev. 193, 195, 206 (1890) (arguing that "existing law affords a

principle which may be invoked to protect the privacy of the

individual from invasion by" then-"[r]ecent innovations" such as

a "modern device for recording or reproducing scenes or sounds").

                                    b.

            The government also suggests that Carpenter and Jones,

with   respect   to   this   portion    of   the    Katz   inquiry,   may   be

distinguished from this case on the ground that the depth of

information revealed by one's movements in a single place over a

long period pales in comparison to            the depth of information

revealed over such an expansive period by "a person's movements

from one location to another."         But, although what the defendants

seek to keep private may have occurred in only one place, it did

not occur in just any place.

            As Moore-Bush and Moore point out, "[a]t the very core'

of the Fourth Amendment 'stands the right of man to retreat into

his own home and there be free from governmental intrusion.'"

                                  - 39 -
Kyllo v. United States, 533 U.S. 27, 31 (2001) (quoting Silverman

v. United States, 365 U.S. 505, 511 (1961)).              The curtilage is

"intimately     linked    to        the   home,    both       physically     and

psychologically," which matters precisely because the home is

"where privacy expectations are most heightened."                Ciraolo, 476

U.S. at 213.    The importance of the home to the Fourth Amendment

is reflected in the text of the Amendment itself, which guarantees

the "right of the people to be secure in their persons, houses,

papers, and effects, against unreasonable searches and seizures,"

U.S. Const. amend. IV (emphasis added), and the curtilage of a

residence has long been understood to "harbor[] the 'intimate

activity associated with the sanctity of a man's home and the

privacies of life,'" United States v. Dunn, 480 U.S. 294, 300

(1987)    (quoting   Oliver    v.    United   States,   466    U.S.   170,   180

(1984)).15


     15Our colleagues suggest that the home only carries special
importance under the Fourth Amendment when courts apply the common-
law trespass test to determine if a search occurred. Concur. Op.
at 120-21. But, in Kyllo v. United States, 533 U.S. 27 (2001),
the Court held -- relying on the Katz test -- that the use of a
device that drew upon heat radiating from a home constituted a
search, even though no physical trespass occurred, in part because
of what the use of the device revealed about what was occurring
inside the home and because "the interior of homes . . . [is] the
prototypical . . . area of protected privacy . . . with roots deep
in the common law," id. at 34. In so concluding, the Court did
the very thing our colleagues accuse us of doing -- "hybridiz[ing]
two threads of Fourth Amendment doctrine," the Katz reasonable
expectation of privacy test and the common-law trespass test.
Concur. Op. at 120-21. We thus see no reason why we may not take


                                     - 40 -
          Not surprisingly, then, the government concedes that the

whole of what was visible to the pole camera here, precisely

because of where the camera was pointed, reveals "information about

a person's life, including, potentially, 'familial, political,

professional,     religious,   and    sexual   associations.'"       See

Carpenter, 138 S. Ct. at 2217.       And, while it is true that one has

no reasonable expectation of privacy in the discrete moments of

intimacy that may occur in the front of one's home -- from a

parting kiss to a teary reunion to those moments most likely to

cause shame -- because of what a passerby may see through casual

observation, it does not follow that the same is true with respect

to an aggregation of those moments over many months.

          No casual observer who is merely passing by can observe

(let alone instantly recall and present for others to observe) the

aggregate of the months of moments between relatives, spouses,

partners, and friends that uniquely occur in front of one's home.

Thus, we do not see why the rarity (at least in the pre-digital

world)   of     sustained   surveillance    and   the   "frailties   of

recollection," id. at 2218, cannot combine to give one a reasonable

sense of security that such intimate moments -- as a whole -- will

be lost to time in the same way that Carpenter recognized one can


account of the special status that the home has under the Fourth
Amendment in determining whether the defendants here had a
reasonable expectation of privacy in the whole of the activities
that occurred in the curtilage of their home.

                                - 41 -
have that one's less intimate movements from place to place beyond

the home will be, see id. at 2217 ("[S]ociety's expectation [is]

that law enforcement agents and others would not . . . secretly

monitor and catalogue every single movement of an individual's car

for a very long period." (quoting Jones, 565 U.S. 430 (Alito, J.,

concurring in the judgment))).   That being so, it follows that the

sum total of all visible activities that take place in a location

that by its nature is "associated with the sanctity of a man's

home and the privacies of life," Ciraolo, 476 U.S. at 212 (quoting

Oliver, 466 U.S. at 180), can be even more revealing than the sum

total of one's movements while out and about, given the nature of

what transpires in front of the home.

          Moreover, the exposure of the aggregate of all visible

activities occurring over a substantial period in front of one's

home may disclose -- by revealing patterns of movements and visits

over time -- what the exposure of each discrete activity in and of

itself cannot.   See Commonwealth v. Mora, 150 N.E.3d 297, 311

(Mass. 2020) ("Prolonged and targeted video surveillance of a

home . . . reveals how a person looks and behaves, with whom the

residents of the home meet, and how they interact with others.").

True, a nosy neighbor, as our colleagues emphasize, Concur. Op. at

116-18, 122, could also observe the patterns of the goings-on in

front of a nearby home over a prolonged period.   But, again it is

worth emphasizing, as we did in our discussion of the defendants'

                             - 42 -
subjective expectation of privacy, that it is the rarest of nosy

neighbors -- if any there be -- who would be able to observe all

the visible activity in the curtilage of the home across the

street, including the license plate of every car that stopped by,

the face of every visitor, and any other activity that occurred at

all times of the day for a period of eight months.   After all, the

claimed expectation of privacy here is not in a discrete activity

or even discrete pattern of activities -- it is in the whole of

the movements, visible to the pole camera, that occur in the

curtilage of a home.16


     16 Our colleagues suggest that the nosy neighbor could augment
his observational abilities by recording the goings on with a video
camera.   Concur. Op. at 122.    But, courts have long found such
video recording of neighbors to be patently unreasonable -- so
much so that such activity can be tortious. See, e.g., Wolfson v.
Lewis, 924 F. Supp. 1413 (E.D. Pa. 1996) (explaining that the
nonstop "videotaping and recording" of the plaintiffs' home made
them "prisoners" in their own home and amounted to "hounding" that
constituted an "invasion of privacy" sufficient to support finding
that the filming was a tort); Gianoli v. Pfleiderer, 563 N.W.2d
562, 568 (Wis. App. 1997) (finding that near constant surveillance
of the plaintiffs' residence constituted "extreme and outrageous
conduct" giving rise to the tort of intrusion upon seclusion);
Jones v. Hirschberger, No. B135112, 2002 WL 853858 (Cal App. May
6, 2002) (finding that a trier of fact could conclude that
neighbors' videotaping of the plaintiffs' backyard was tortious);
Mangelluzzi v. Morley, 40 N.E.3d 588 (Ohio Ct. App. 2015) (same);
see also Polay v. McMahon, 10 N.E.3d 1122, 1127 (Mass. 2014)
("[E]ven where an individual's conduct is observable by the public,
the individual still may possess a reasonable expectation of
privacy against the use of electronic surveillance that monitors
and records such conduct for a continuous and extended duration.").
     To the extent that our colleagues suggest that a person cannot
have an objective expectation of privacy in the whole of the
activities that occur in the front curtilage of the person's home


                              - 43 -
           Thus, for this reason, too, the claimed expectation of

privacy here is not fairly characterized as inhering in a mere

"sliver" of a person's publicly visible life, Tuggle, 4 F.4th at

524, any more than the sum total of one's movements beyond the

home may be deemed to be.      Indeed, it is not evident that our

public movements from place to place could reveal that the place

where we live is the site where a disfavored political group is

holding weekly meetings or where a cleric is holding a worship

service.    But, that type of information is at risk of being

disclosed when the "aggregate" of our publicly visible activity

consists of all that transpires over months in the front curtilage

of our home.

                                     3.

           The   government   does     nonetheless   insist   that   pre-

Carpenter rulings -- none of which Carpenter purported to overrule,

see Carpenter, 138 S. Ct. at 2220 ("Our decision today is a narrow

one.   We do not express a view on matters not before us.") --

require the conclusion that there is no reasonable expectation of



because "many of those movements, even if not all, can and will be
observed by the same people," Concur. Op. at 119, we do not see
how that assertion can be squared with Carpenter itself.         A
person's movements in public may be observed by others, and the
same person may even observe many of them. But, the fact that
others may have a window into some -- but not all -- of a person's
movements in public does not, as Carpenter explained, render a
person's expectation of privacy in the whole of their movements in
public objectively unreasonable.

                                - 44 -
privacy in what the defendants claim.                    Once again, we are not

persuaded.

               The government points here, for example, to Ciraolo, in

which the Court rejected the defendant's argument that "because

his yard was in the curtilage of his home, no government aerial

observation [was] permissible under the Fourth Amendment."                          476

U.S. at 212.       But, Ciraolo did not dispute that the "home is, for

most purposes, a place where he expects privacy."                        Id. at 215

(quoting Katz, 389 U.S. at 361 (Harlan, J., concurring)).                    Rather,

it explained that the owner of the curtilage was reasonably on

notice    of    the   possible     exposure      to     the   "casual,     accidental

observ[er]"      of   what   was   sought    to    be    kept    private    there   --

especially "[i]n an age where private and commercial flight in

public airways is routine."             Id. at 212, 215; see also id. at 213

("The Fourth Amendment protection of the home has never been

extended to require law enforcement officers to shield their eyes

when passing by a home on public thoroughfares." (emphasis added)).

Ciraolo thus did not in any way suggest that the owner was

similarly on notice of the possible exposure of all that was

visible in the curtilage of the home over a substantial period --

recorded in a perfect visual compendium that is both endlessly re-

playable and easily sifted through for the telling detail.

               The same is true of Florida v. Riley, 488 U.S. 445

(1989),    which      concerned    an    officer      who     "circled   twice   over

                                        - 45 -
respondent's property in a helicopter" and used his "naked eye" to

look through a greenhouse to discover illicit substances.                   Id. at

448 (plurality opinion).           There, in determining that no Fourth

Amendment search occurred, the Court observed merely that "[a]s a

general proposition, the police may see what may be seen 'from a

public vantage point where [they have] a right to be.'"                     Id. at

449 (emphasis added and second alteration in original) (quoting

Ciraolo, 476 U.S. at 213); see also id. at 451 ("Any member of the

public could legally have been flying over [the defendant]'s

property    in    a    helicopter . . . and      could    have   observed    [his]

greenhouse.").         Thus, again, the Court did not suggest that the

same conclusion would follow if the question concerned one's

expectation of privacy in all that visibly occurred in one's front

curtilage over a long period of time.

            The government also points us to the Court's pre-Jones

precedent, United States v. Knotts, 460 U.S. 276 (1983), which

concerned the use of an electronic beeper to monitor the movement

of a car on a public roadway.            The Court unanimously held in that

case that the electronic "monitoring of [a] beeper" to track a

vehicle as it traveled from a store in Minnesota to a cabin in

Wisconsin "was [not] a 'search' . . . within the contemplation of

the Fourth Amendment," id. at 279,                285, because      "[a] person

traveling    in       an   automobile    on   public     thoroughfares   has    no

reasonable expectation of privacy in his movements from one place

                                        - 46 -
to another," id. at 281.     But, Knotts expressly cautioned that the

Court was not "determin[ing] whether" technological advances that

enabled longer-term tracking of those movements would similarly be

permissible:   If "twenty-four hour surveillance of any citizen of

this country will be possible, without judicial knowledge or

supervision," "there will be time enough then to determine whether

different constitutional principles may be applicable."               Id. at

283-84.   So, Knotts, too,        fails to      support the government's

contention.

          Finally, the government points to Kyllo.                There, the

Court explained that, since the advent of the Katz test, it had

yet to call into question the "lawfulness of warrantless visual

surveillance   of   a   home,"   Kyllo,   533   U.S.   at   32,   noted   that

traditionally "our Fourth Amendment jurisprudence was tied to

common-law trespass," id. at 31, and pointed out that, under that

trespass-based test, "[v]isual surveillance was unquestionably

lawful because 'the eye cannot by the laws of England be guilty of

a trespass,'" id. at 31-32 (quoting Boyd, 116 U.S. at 628)).              But,

while the government argues that Kyllo reflects a determination

that all "warrantless visual surveillance of a home" is lawful,

id. at 32, the Court in the passages quoted above was explaining

only that it had yet to confront a form of "visual surveillance"

that was a search under the Fourth Amendment, id. at 32, while



                                  - 47 -
appearing to contemplate that there may be a need for future

"refine[ments]" to the Katz test down the road, id. at 34.

           Nor   did    Kyllo   have      reason    to   address    long-term

electronic visual surveillance of a home's curtilage.               Its focus

was on the capacity of technology to enhance visual surveillance

in the short term:      a policeman in that case had used a thermal-

imaging device for "a few minutes" from outside the home to

determine the heat levels within the defendant's home.             Id. at 30.

In fact, when discussing the lack of judicial questioning of the

constitutional propriety of "warrantless visual surveillance of a

home," id. at 32, Kyllo referred only to Ciraolo, which, as we

have seen, involved only short-term police surveillance of a home

(which   there   was   unenhanced    by   digital    technology),    and   Dow

Chemical Co. v. United States, 476 U.S. 227 (1986), which also

concerned only short-term observation of a "commercial property,"

id. at 237; see also id. at 237-38, 238 n.5 (holding that no search

occurred when government regulators engaged in one days' worth of

aerial   surveillance     "of   a    2,000-acre     outdoor   manufacturing

facility" using camera technology by which "human vision [wa]s

enhanced somewhat" although not to the point that "any identifiable

human faces or secret documents [were] captured in such a fashion

as to implicate more serious privacy concerns").

           Moreover, the subject of the surveillance in Kyllo --

"heat radiating from the external surface of the house," 533 U.S.

                                    - 48 -
at 35 -- was itself exposed to public "view" in a sense.     Indeed,

that was how a thermal imaging device operating outside the home

could enable such heat to be "seen."         But, that fact did not

preclude the Court from concluding in Kyllo that a resident of a

heat-emitting home has a reasonable expectation of privacy in the

record of the thermal radiation -- at least when the source of the

heat is a home.    See id. at 34.       Kyllo's holding thus in some

respects lends support to -- though we do not suggest that it

requires -- the conclusion that a person can have a reasonable

expectation of privacy in what visibly occurs in the curtilage of

his home even though it is exposed to the public.

          In sum, none of the pre-Carpenter decisions of the Court

that the government relies on rejected claims to privacy in the

aggregate of the activities that occur in front of one's home over

a long period of time.   Nor did any of those precedents purport to

suggest that one reasonably expects to be subjected to the kind of

intensive, long-term surveillance that could expose to a member of

the observing public the whole of what visibly transpires in the

front of one's home over many months in any practically likely

scenario.17   Accordingly, we reject the government's contention


     17The remaining Supreme Court cases cited by the government
to support its contention that "law enforcement may observe what
a person exposes to public view" are similarly inapposite. These
cases all involve discrete incidents in which a person revealed
information to the public rather than the compendium of activity


                               - 49 -
that the Supreme Court's pre-Carpenter caselaw requires us to find

that   the    defendants   here     assert   no   objectively    reasonable

expectation of privacy.

             In so doing, we part ways with our colleagues who,

persuaded by the government's canvassing of the pre-Carpenter

caselaw, would conclude that there is no reasonable expectation of

privacy in what the defendants here seek to shield simply because

each discrete activity that took place in the front curtilage of

the Hadley Street home was exposed to public view.              It is worth

emphasizing,    though,    before   moving   to   the   next   part   of   the

analysis, how sweeping a conclusion that appears to be.

             By seeming to hold that a person can have no reasonable

expectation of privacy in the whole of the activities in the front

curtilage of a home simply because each activity is exposed to

public view, our colleagues appear to be willing to close the door

to a Fourth Amendment claim that could stem from the government

accessing a database containing continuous video footage of every

home in a neighborhood, or for that matter, in the United States

as a whole.      In light of the Supreme Court's warning that "as

'[s]ubtler and more far-reaching means of invading privacy have

become available to the [g]overnment,'" courts are "obligated


at issue here. See, e.g., California v. Greenwood, 486 U.S. 35,
37, 41 (1988); New York v. Class, 475 U.S. 106, 107, 114 (1986);
United States v. Dionisio, 410 U.S. 1, 3, 14 (1973); United States
v. Mara, 410 U.S. 19, 21 (1973).

                                    - 50 -
. . . to ensure that the 'progress of science' does not erode

Fourth   Amendment      protections,"       Carpenter,    138    U.S.     at      2220

(quoting Olmstead v. United States, 277 U.S. 438, 473-74 (1928)

(Brandeis,     J.,    dissenting)),    we    are    not   as    willing      as   our

colleagues to preclude categorically such Fourth Amendment claims.

                                      IV.

           Our conclusions to this point do not, however, suffice

to   support    the    conclusion     that    the    surveillance       at     issue

constituted a search. We still must address whether the government

"contravene[d]" the objectively reasonable expectation of privacy

that the defendants possessed, such that the government engaged in

a search by accessing a record of that surveillance.                    Carpenter,

138 S. Ct. at 2217.      The portion of the Katz inquiry that concerns

what contravenes a reasonable expectation of privacy is a necessary

one for us to undertake because "[t]he obtaining of information is

not alone a search unless it is achieved by . . . a trespass or

invasion of privacy." Jones, 565 U.S. at 408 n.5 (emphasis added).

           In opposing the defendants' motions to suppress in the

District Court, the government did not distinguish between the

portions of the Katz inquiry that concern the expectation of

privacy and the portions that concern contravention.                It was only

in the motion to reconsider that the government filed after the

District Court's ruling finding that a search had occurred that

the government developed an argument that focused on the means of

                                    - 51 -
the surveillance rather than the public exposure of what was

subject to that surveillance.        The government contended in that

motion that "[t]here was no unique or new technology used in the

investigation   that    implicated     the     concerns        of   Carpenter,"

(capitalization altered), because the surveillance at issue merely

involved the use of a digital camera.          Then, both in its briefing

to the panel on appeal and in its briefing to our full court in

connection with the rehearing en banc, the government augmented

that contention by emphasizing other attributes of the means of

surveillance to support the contention that the defendants could

not satisfy the contravention portion of the Katz test.

          In addressing the assertions about contravention that

the government now makes, we must keep in mind a point related to

the one that we made in connection with our discussion of the

antecedent   portions   of   the   Katz     test   --   that    the   means   of

surveillance that the government used here did not permit merely

the observation from afar of the curtilage of the Hadley Street

residence.   Nor did those means involve merely the use of a digital

camera such that they permitted what transpired there simply to be

recorded digitally.     Rather, those means involved the long term,

remote use of a digital video camera affixed to a utility pole and

thus permitted the government to acquire an instantly searchable,

perfectly accurate, and thus irrefutable digital compendium of the

whole of what visibly occurred over a period of the government's

                                   - 52 -
choosing (and thus seemingly without limit as to duration) that

ended up lasting eight months.           Moreover, those means enabled the

government to access that record for a criminal investigatory

purpose   in   a   manner   that   was    not   only   cheap   and   remarkably

efficient but also impossible for the target of the surveillance

to evade through precautions that one may be expected to take in

response to the possibility of "casual, accidental observation,"

Ciraolo, 476 U.S. at 212.

           Notably, the government makes no contention otherwise in

arguing that, even still, this means of surveillance did not

contravene the defendants' claimed expectation of privacy in the

aggregate of what transpired in the curtilage of the Hadley Street

residence that was visible to the camera over the course of many

months or, at least, did not do so in any way that would render

this means of surveillance a search.            And, we note, the government

presses for us to credit this means-of-surveillance-based ground

for ruling that no search occurred even if we were to accept what

the government vigorously disputes: that the defendants' claimed

expectation of privacy in that aggregate is one that society is

prepared to accept as reasonable.             We decline to do so.

                                         A.

           To get our bearings, it helps to start our analysis of

the "contravention" portion of the inquiry by reviewing what

Carpenter had to say about why "the [g]overnment's acquisition of

                                    - 53 -
the cell-site records" contravened                 the defendant's reasonable

expectation    in    the   whole    of    his    movements      in   that    case   and

therefore constituted a search.                Carpenter, 138 S. Ct. at 2223.

Carpenter, after all, is the only case in which the Court has

addressed    the    contravention        portion    of    the    Katz   inquiry     in

connection    with    a    contention     that     the    long-term,        electronic

surveillance of an individual's publicly visible movements is not

a search.     It is thus a singularly instructive guide to us here,

despite the distinct factual context in which the issue arose

there.

            It is also worth noting in this regard that the Court,

in considering whether the surveillance at issue in Carpenter

"contravened" the defendant's reasonable expectation of privacy,

conducted that inquiry at the point at which the government

"accessed" the CSLI.         Carpenter, 138 S. Ct. at 2219.                 Thus, the

Court did not consider whether or how the government ultimately

utilized the seven days' worth of CSLI that it "accessed."                      Id. at

2217 n.3.

            Carpenter recognized that it was confronting a "new

phenomenon"    brought      on     by    the     advent    of    once       unimagined

surveillance technology.           Id. at 2216.      It recognized, too, that

it needed to "tread carefully . . . to ensure that [it] d[id] not

'embarrass the future.'"            Id. at 2220 (quoting Nw. Airlines,

Inc. v. Minnesota, 322 U.S. 292, 300 (1944)).                   But, it also noted

                                        - 54 -
that, as we have already mentioned, it was "obligated -- as

'[s]ubtler and more far-reaching means of invading privacy have

become available to the        [g]overnment'   -- to ensure that the

'progress    of    science'    does   not   erode   Fourth   Amendment

protections."     Id. at 2223 (first alteration in original) (quoting

Olmstead, 277 U.S. at 473-74 (Brandeis, J., dissenting)).

            Applying those principles, Carpenter concluded that "the

progress of science has afforded law enforcement a powerful new

tool to carry out its important responsibilities [but which also]

risk[s] [g]overnment encroachment of the sort the Framers, 'after

consulting the lessons of history,' drafted the Fourth Amendment

to prevent."    Id. (quoting Di Re, 332 U.S. at 595).   And, in coming

to that conclusion, we note, the Court carefully examined the

precise new surveillance tool before it in combination with the

way in which that tool was employed in the case at hand, "tak[ing]

account of more sophisticated" versions of that tool "already in

use or in development."       Id. at 2218 (quoting Kyllo, 533 U.S. at

36). Moreover, the Court pointed to various aspects of that tool's

features that, at least in combination, demonstrated that the tool

posed a concerning risk to the constitutional balance, at least

when used to acquire the quantum of information covering the

expanse of time that was there at issue.

            Carpenter emphasized, in this connection, "the deeply

revealing nature of CSLI."       Id. at 2223.    Here, the Court drew

                                  - 55 -
upon its own explanation of why the movements tracked by the CSLI

that the government accessed from the defendant's wireless carrier

over   the   period   in    question    revealed   in   the   aggregate   the

"privacies of life."       Id. at 2217 (quoting Riley, 573 U.S. at 403).

The Court pointed out in this regard that the CSLI that the

government accessed provided an "intimate window into a person's

life," id. at 2217, due to the "depth, breadth, and comprehensive

reach" of such CSLI, id. at 2223.               As the Court explained,

"[m]apping a cell phone's location over the course of [several

months] provides [the government with] an all-encompassing record

of the holder's whereabouts" that is akin to "achiev[ing] near

perfect surveillance, as if [the government] had attached an ankle

monitor to the phone's user."          Id. at 2217-18 (quoting Jones, 565

U.S. at 415 (Sotomayor, J., concurring)).

             Notably, the Court also drew support for this aspect of

its analysis from the reasoning of the five concurring Justices in

Jones, as they had emphasized the comprehensive nature of the

information that the GPS device at issue there had permitted the

government to acquire in finding that the government's decision to

use that device to collect twenty-eight days' worth of GPS data

regarding the defendant "impinge[d] on" the defendant's reasonable

expectation of privacy.         id. (quoting Jones, 565 U.S. at 430

(Alito, J., concurring in the judgment)); see also Jones, 565 U.S.

at 415 (Sotomayor, J., concurring) ("GPS monitoring generates a

                                   - 56 -
precise, comprehensive record of a person's public movements that

reflects   a   wealth    of   detail     about     [a   person's]   . . .

associations. . . .     The government can store such records and

efficiently mine them for information years into the future.");

Jones, 565 U.S. at 428-29 (Alito, J., concurring in the judgment

joined by three Justices) (describing various new technologies

that engage in "constant monitoring" and are thus able to track a

person's "daily movements").       Indeed, the Court in Carpenter

pointed out that the tracking effectuated by the collection of the

CSLI "partakes of many of the qualities of the GPS monitoring we

considered in Jones," as the Court explained that "cell phone

location information," too, is "detailed" and "encyclopedic."

Carpenter, 138 S. Ct. at 2216.

           Carpenter emphasized, as well, the relative ease with

which this new surveillance tool afforded the government access to

an intimate and comprehensive window into a target's life.             By

requesting CSLI from a wireless carrier, the Court explained, "the

[g]overnment can access [a] deep repository of historical location

information at practically no expense."          Id. at 2218.   The Court

further noted that the "repository" of CSLI, once accessed by the

government from a wireless carrier, is not "limited by . . . the

frailties of recollection" and that, as a result, it "gives police

access to a category of information otherwise unknowable."            Id.

In addition, the Court noted that CSLI is "effortlessly compiled."

                                - 57 -
Id. at 2216.     And, in doing so, the Court once again mirrored the

language from the Jones concurrences.             Id. at 2218.

           Finally, in determining that the government's accessing

of the seven days' worth of CSLI from the defendant's wireless

carrier contravened the defendant's               reasonable expectation of

privacy and so constituted a search, Carpenter emphasized a feature

of that CSLI that arguably differentiated it from the GPS-tracker

information that the government had acquired through its own real-

time    tracking      of     the   defendant's    movements      in    Jones:     the

information had a "retrospective quality."               Id.   The Court pointed

out that "because location information is continually logged for

all of the 400 million devices in the United States -- not just

those   belonging      to     persons    who   might    happen   to    come     under

investigation -- this newfound tracking capacity runs against

everyone."      Id.    Thus, the Court noted, "[w]hoever the suspect

turns out to be, he has effectively been tailed every moment of

every day for five years" with no reasonable ability to take

countermeasures to avoid that surveillance as a "cell phone [is]

'almost a feature of human anatomy.'"             Id. at 2218, 2219 (quoting

Riley, 573 U.S. at 386).                In other words, this surveillance

technology      was        especially     threatening     to     the    reasonable

expectation of privacy in the whole of one's movements in public

because    of   "the        inescapable    and   automatic       nature   of      its

collection."     Id. at 2217.

                                        - 58 -
            Consistent    with   the    Court's     stated   concern        about

ensuring that new technological enhancements to law enforcement's

surveillance capacity do not "erode" the basic protection that the

Fourth Amendment guarantees,         the Court also      made a point of

comparing these features of this means of pursuing a criminal

investigation with less souped-up ones.             Id. at 2223.     In this

regard, the Court, again mirroring the language of the                       five

concurring Justices in Jones, explained that the accessing of

historical CSLI by the government is "remarkably easy, cheap, and

efficient compared to traditional investigative tools" because the

government by doing so acquires a capacity to easily mine "the

exhaustive    chronicle    of    location   information"     that      is    not

comparable to the capacity it has when relying on "traditional,

investigative tools."       Id. at 2217-18 ("[L]ike GPS monitoring,

cell phone tracking is remarkably easy, cheap, and efficient

compared to traditional investigative tools."); see also Jones,

565 U.S. at 415-16 (Sotomayor, J., concurring) ("[B]ecause GPS

monitoring is cheap in comparison to conventional surveillance

techniques, . . . it evades the ordinary checks that constrain

abusive law enforcement practices."); Jones, 565 U.S. at 429

(Alito, J., concurring in the judgment) ("Devices like the [GPS

device] . . .   make     long-term     monitoring    relatively     easy      and

cheap.").



                                   - 59 -
                 The Court was careful, moreover, to caveat that the

concerns         presented    by     unconventional,      aggregative      electronic

surveillance -- like the accessing of the historical CSLI at issue

in   Carpenter       --   did      not   apply   to   "conventional      surveillance

techniques and tools, such as security cameras."                         Id. at 2220.

And, the Court similarly explained that it was withholding judgment

about      how    "business     records,"        other   than   CSLI,    "that    might

incidentally         reveal        location      information"      fit     into     the

conventional-discrete/unconventional-aggregative                   dichotomy       that

it described.         Id.18

                                            B.

                 There is no doubt, as our colleagues point out, that the

factual context presented here differs in certain respects from

the one that the Court confronted in Carpenter and that it does so

in ways that have some bearing on the contravention portion of the

Katz inquiry. Most notably, the Court had to address there whether

the so-called third-party doctrine provided a reason to conclude

that the government's accessing of the seven days' worth of the

defendant's historical CSLI did not contravene the expectation of

privacy that the Court had recognized that the defendant had in


      18It is possible that it is not useful to disentangle the
"contravention" and the "objective" portions of the "expectation
of privacy" component of the Katz inquiry from one another. But,
we read Carpenter to suggest that it is useful to consider the
contravention portion of the inquiry separately, and so do so. As
far as we can tell, nothing of substance turns on that choice here.

                                          - 60 -
what that tranche of CSLI contained.        See id. at 2216-17.     After

all, in Carpenter, the government had accessed information that it

had not created through its own surveillance; it had accessed

information that it had requested from a third-party to which that

collection of information had already been disclosed.          Thus, the

disclosure to that third-party could be thought to have destroyed

whatever privacy expectation the defendant might otherwise have

possessed.   Id.    The Court thus identified the various features of

the surveillance canvassed above at least in part to justify not

extending the third-party doctrine to the case at hand, despite

the fact that the doctrine had been held to apply to, for example,

bank records, which are themselves quite revealing, see United

States v. Miller, 425 U.S. 435, 443 (1976).

          We, of course, have no such issue regarding the third-

party doctrine to address.     The government here accessed a digital

compendium that it created on its own and that was not disclosed

in advance to any other party.          In that respect, the case for

concluding   that    the   government     contravened   the   defendants'

reasonable    expectation      of   privacy      is     seemingly    more

straightforward than it was for concluding similarly with the

respect to the reasonable expectation of privacy of the defendant

in Carpenter itself.

          At the same time, Carpenter, by its own terms, is not

limited to situations in which the third-party doctrine is in play,

                                 - 61 -
despite what our colleagues suggest.                      Carpenter, 138 S. Ct. at

2217.       Concur. Op. at 113-14.                  Indeed, in the paragraph of

Carpenter that describes how the decision is a "limited one," the

Court      expressly       does   not     limit     its    decision    to    only    those

situations in which the third-party doctrine is implicated.                              Id.

at 2220; see also id. at 2217 ("Whether the [g]overnment employs

its own surveillance technology as in Jones or leverages the

technology      of     a    wireless      carrier,        we   hold   that . . . [t]he

location information obtained from Carpenter's wireless carriers

was the product of a search.").

              It    follows,      then,      that     Carpenter's     analysis      of   the

contravention issue also bears on whether a means of electronic

surveillance utilized by the government itself is a means that

"contravenes" a reasonable expectation of privacy.                          The question

for   us    here,    therefore,         is    how     Carpenter's     analysis      of   the

contravention question bears on our analysis of that question,

even though the third-party doctrine is not at issue.

              In addressing that question, we must be cautious about

responding to this means of surveillance in a manner that would

"embarrass the future," id. at 2220 (quoting Nw. Airlines, 322

U.S. at 300), by needlessly stripping government of a potentially

useful surveillance tool insofar as that tool -- even if newfangled

-- does not threaten to erode the vital protections that the Fourth

Amendment provides any more than longstanding but somewhat-updated

                                             - 62 -
versions of more pedestrian, surveillance techniques would.                               At

the same time, though, we must not lose sight of the fact that the

Fourth Amendment was drafted with the "central aim of . . .

'plac[ing]      obstacles    in    the      way    of    a    too     permeating   police

surveillance,'" id. at 2214 (quoting Di Re, 332 U.S. at 595), and

that courts must "assure [] preservation of that degree of privacy

against government that existed when the Fourth Amendment was

adopted" in assessing evolving technologies that threaten that

degree of privacy, id. (alteration in original) (quoting Kyllo,

533 U.S. at 34).

               Moreover, we must attend to the fact that Carpenter, as

we have pointed out, explained that it was a "narrow ruling" that

did not apply to "conventional surveillance techniques."                           Id. at

2220.    And, we must also take account of the fact that Carpenter's

caveat on that score accords with Carpenter's observation that

government conduct that "contravenes" a reasonable expectation of

privacy    "generally"      --     and      thus    not       necessarily     always      --

constitutes a search.         Id. at 2213 (emphasis added).

               With those considerations in mind, we conclude, as we

will next explain, that many of the same reasons that Carpenter

relied    on    to   find   that      the    government         had    contravened       the

reasonable      expectation      of   privacy       at       issue    there   --   and    so

conducted a search -- equally support the conclusion that the

government did the same in this case.                     For, while the databases

                                         - 63 -
that the government accessed in the two cases are not identical,

the differences between them are not of a kind that warrants an

outcome   here   opposite    to   Carpenter's   with   respect   to   the

contravention issue.

                                    1.

           For starters, there is little doubt that the record

generated over the months-long expanse of time by the digital pole

camera in this case is "deeply revealing" of the "privacies of

life."    Carpenter, 138 S. Ct. at 2217, 2223 (quoting Riley, 573

U.S. at 403).    Like the seven days' worth of the historical CSLI

accessed by the government in Carpenter, the digital videologue

that was created here provides an "intimate window into [the

defendants'] li[ves]."      Id. at 2217.

           That is so, in part, due to the "depth, breadth, and

comprehensive" reach of the pole camera's gaze, id. at 2223,

trained as it was on the front curtilage of the Hadley Street

property over eight months and capable as it was of retaining in

full -- and in readily searchable form -- all that it espied for

as long as it looked.       Indeed, while the camera at issue here

records live images, the CSLI at issue in Carpenter merely reveals

a dot on a map for a single person.

           That is also so, because, as we explained in connection

with the reasonable expectation of privacy portion of the inquiry,

the focus of the pole camera's recording -- the front curtilage of

                                  - 64 -
the defendants' residence -- implicates the home, which is "[a]t

the very core of the Fourth Amendment."         Kyllo, 533 U.S. at 31

(internal quotation marks omitted).       Every person has the right to

"retreat into [and enjoy] his own home and there be free from

unreasonable governmental intrusion."         Jardines, 569 U.S. at 6

(quoting Silverman, 365 U.S. at 511).         And, for good reason, as

our home (curtilage included) is often the center of our lives: it

is where we always return to, where our friends, family, and

associates visit, where we receive packages and mail, and where we

spend a good deal of time.     Observing the movements in front of a

home for months, therefore, can reveal quite a lot about a person

--   at   the   very   least   "familial,    political,   professional,

religious, and sexual associations," Carpenter, 138 S. Ct. at 2217

(quoting Jones, 565 U.S. at 415 (Sotomayor, J., concurring)) --

and perhaps to a greater extent than even a substantial swath of

one's historical CSLI.

           There is similarly little doubt that, like the type of

surveillance at issue in Carpenter, the type of surveillance at

issue here is "easy, cheap, and efficient" relative to its pre-

digital substitute.    Id. at 2217-18.      The government can initiate

the surveillance -- and then carry it through to completion -- for

a pittance relative to what a traditional stakeout would cost in




                                 - 65 -
terms of time and expense, to say nothing of the reduction in the

risk of detection that this means of surveillance makes possible.19

          The   digital   pole   camera   recording   here,   given   the

substantial expanse of time that the digital record encompasses,

is also an unusually efficient tool of surveillance in another



     19 Our colleagues suggest that the long-term use of a pole
camera is not "easy, cheap, and efficient" because such
surveillance is "not cost-free." Concur. Op. at 113. True, the
use of a pole camera comes with a cost (as does the use of a GPS
tracker and the receipt and review of CSLI). But, there is no
basis on this record for concluding that the cost is a great one,
as our colleagues themselves also point out by emphasizing how
inexpensive cameras are for the everyday consumer.
     Our colleagues do suggest that while it may be inexpensive to
use a single pole camera to create a searchable record, replicating
that surveillance by "[p]lacing and maintaining . . . millions of
pole cameras" to compile a database of "years of video" is not.
Concur. Op. at 113 n.39. But, our colleagues do not explain why
the ease with which the government can replicate the surveillance
is the relevant comparator for purposes of determining whether a
surveillance technique is cheap. Indeed, Carpenter's reliance on
the Jones concurrences in explaining why CSLI is "easy, cheap, and
efficient" relative to past, conventional technologies suggests
the opposite.    Carpenter, 138 S. Ct. at 2217-18.      As we have
described, in Jones, the concurrences were concerned with the
resource constraints that make tailing a single individual for a
long period impractical -- at no point did the concurrences in
Jones consider whether it would be "easy, cheap, and efficient" to
use a GPS tracker tail every person in the United States for every
hour of every day. See Jones, 565 U.S. at 415-16 (Sotomayor, J.,
concurring); id. at 429 (Alito, J., concurring in the judgment).
     In any event, the relevant question after Carpenter is not
whether a technology is cost-free. It is whether the efficiencies
afforded by the surveillance tool give rise to the substantial
risk that what had been at best a most rare prospect of
surveillance will become more routine and thereby upend the balance
between security in the private realm and order that the Fourth
Amendment strikes. We see no reason to doubt that the efficiencies
of this tool are of that sort.

                                 - 66 -
way:   it is easily searchable -- especially when, considering the

"more sophisticated [versions of this technology] that are already

in use or in development," id. at 2218-19 (quoting Kyllo, 533 U.S.

at 36), the ability to utilize facial recognition and other forms

of visual search technologies is factored into the searchability

of this record.   See also Riley, 573 U.S. at 381, 385 (considering

the appropriateness of extending the search-incident-to-arrest

doctrine to "modern cell phones" with "smart" features even though

the phone at issue in one of the two cases on appeal was a "flip

phone" with none of those "smart" features).   The ease with which

a voluminous digital record may be mined to yield otherwise hidden

information, when combined with the capacity for that record to be

stored (given cloud-based computing), makes it distinct from its

analog analogues.    One need only imagine the officer tasked with

reviewing month three of a collection of eight months of VHS tapes

-- assuming that she could retrieve them in a timely fashion from

the warehouse -- to see how distinct the digital repository before

us is.

            Finally, the accessing by the government of the pole

camera-generated, digital video record here is also similar to the

accessing by the government of the CSLI in Carpenter in the third

way that Carpenter identified as salient to the contravention

inquiry:    the means of evading the creation of the record are not

feasible.   As the Court recognized in Carpenter, CSLI is generated

                               - 67 -
"several times a minute" "[e]ach time the phone connects to a cells

site" -- "even if the owner is not using one of the phone's

features."   Carpenter, 138 S. Ct. at 2211.         The only way to avoid

generating CSLI is to not use a cell phone, which the Court

recognized was simply not a feasible precaution for a person

functioning in today's society.      Id. at 2218.

           Evading the pole-camera surveillance here -- contrary to

our colleagues' suggestion -- demands no less unreasonable efforts

to thwart it.     Nor is a homeowner likely to be placed on notice

that the government is surveilling the property via pole camera,

because, by definition, such surveillance is clandestine. In fact,

a homeowner need not be on notice of even his own illegal activity

to be subjected to this type of watch.          By the government's own

theory, no level of suspicion is needed to utilize a pole camera.

           To be sure, a well-constructed fence or craftily planted

hedgerows may enable the homeowner to block the gaze of a hidden

camera   placed   at   street   level,   to   the   extent   financial   and

regulatory constraints make either countermeasure realistic.             But,

the saying, "show me a wall and I'll show you a ladder" comes to

mind.    We must assume that the government would choose to place

the camera at a height sufficient to surmount whatever vertical

barrier would obstruct its view.         Thus, the only countermeasures

certain to work -- never leaving the house or enclosing the

curtilage to make it effectively part of the inside of the house

                                  - 68 -
-- are at least as unreasonable to expect a person to take as

leaving home without a cell phone.

           That said, the comparison to the government's accessing

of the CSLI in Carpenter is not a perfect one.          CSLI is created by

wireless carriers as part of the provision of cell-phone service.

As a result, any law-enforcement accessing of historical CSLI from

a wireless carrier has a "retrospective quality." For this reason,

in accessing the CSLI at issue in Carpenter, the Court emphasized,

the government was able to overcome the "dearth of records and the

frailties of recollection" and was limited instead only by "the

retention policies of the wireless carriers."       Id.

           The accessing of that trove of historical data was in

that respect more concerning than even the government's use of

CSLI to track a person's movements in real time.               Id. at 2220.

The   accessing   of   the   historical   CSLI   gave    the    government,

instantly, information that the government did not even know that

it needed and so would never have collected on its own.

           By contrast, because the government set up the pole

camera in this case, it follows, as our colleagues emphasize, that

the government must have had some reason to have done so.           Concur.

Op. at 113-14.    In that sense, the accessing of the record of the

"privacies of life," id. at 2214 (quoting Boyd, 116 U.S. at 630),

follows a decision by the government to make the record in real

time in a way that the accessing of the historical CSLI from the

                                 - 69 -
wireless carrier in Carpenter did not.          See also Tuggle, 4 F.4th

at 525 ("The government had to decide ex ante to collect the video

footage by installing the cameras.").

             But, we do not understand Carpenter to suggest that the

creation of a searchable digital record that perfectly accounts

for the whole of the movements of a person over a long period of

time contravenes a reasonable expectation of privacy -- and thereby

effects a search -- only when that record was created before the

government wished to have it.         Cf. Carpenter, 138 S. Ct. at 2217

("Whether the [g]overnment employs its own surveillance technology

. . . or leverages the technology of a wireless carrier, we hold

that an individual maintains a legitimate expectation of privacy

in the record of his physical movements.").          Indeed, it is hard to

understand why it would be less destructive of the "degree of

privacy" that existed at the time of the Founding, id. at 2214, to

have   the    government   directly    engage   in   scooping   up   visual

information about all that occurs in front of a residence over a

long period of time than to have the government selectively request

that information from a private actor who had undertaken its own

collection effort to amass a wealth of data, id. at 2218.

             We recognize that democratic pressures may, of their own

force, constrain the widespread use of this means of surveillance.

But, the risk that this form of surveillance, given how cheap,

easy, and efficient it is, would upset the Framers' balance if

                                 - 70 -
permitted to be deployed unrestrained by the Fourth Amendment is

clear enough.   There appears to be little in the nature of the

technology itself that would stop the government from choosing to

replicate the form of surveillance at issue here widely.   Nor does

the government give us reason to have confidence that limits either

practical or legal are sure to restrain its use.        Indeed, it

asserts that it need not have even a modicum of suspicion to engage

in the surveillance at issue here.20

          The concern, then, is real that, in time, this form of

surveillance could become a means by which the "society" to which

we look for guidance in determining what "expectations of privacy"

are worthy of constitutional concern would become a society that

would no longer afford privacy the kind of protection that the

Fourth Amendment has long been understood to provide it.        See

Tuggle, 4 F.4th at 527-28 (explaining that "if current technologies

are any indication, . . . technological growth will predictably

have an inverse and inimical relationship with individual privacy

from government intrusion, presenting serious concerns for Fourth


     20 Our colleagues propose a constraint of their own:      They
suggest that "creat[ing] anything approaching cellular service
providers' databases" for pole-camera footage "would entail such
an enormous expenditure of scarce resources as to ensure that would
never happen." Concur. Op. at 113 n.39. But, we are hesitant to
so casually dismiss as impossible the notion that the government
may not be surgical in the use of pole-camera surveillance in the
future, as the government has collected and analyzed immense
amounts of information in the recent past, see, e.g., Am. C.L.
Union v. Clapper, 785 F.3d 787, 796-97 (2d Cir. 2015).

                              - 71 -
Amendment protections" because "once society sparks the promethean

fire -- shifting its expectations in response to technological

development -- the government receives license . . . to act with

greater constitutional impunity").         For, while pole cameras are

not currently in use today by law enforcement to monitor the front

of every home, or even every home in a neighborhood, see, e.g.,

Paul Mozur & Aaron Krolik, A Surveillance Net Blankets China's

Cities, Giving Police Vast Powers, N.Y. Times (Dec. 17, 2019),

https://www.nytimes.com/2019/12/17/technology/

china-surveillance.html,       Carpenter   emphasized   that   courts   are

"obligated -- as '[s]ubtler and more far-reaching means of invading

privacy have become available to the [g]overnment' -- to ensure

that the 'progress of science' does not erode Fourth Amendment

protections," Carpenter, 138 S. Ct. at 2223 (first alteration in

original) (quoting Olmstead, 277 U.S. at 473-74 (Brandeis, J.,

dissenting)).

          Moreover, even though the government created the digital

record at issue in this case, the accessing of it by the government

still shares many of the features that Carpenter pointed to in

expressing   concern   about    the   "retrospective    quality"   of   the

government's accessing of historical CSLI.          Id. at 2218.        The

government claims that it can set up an unmanned digital video

pole camera for law enforcement purposes without a warrant or even

any constitutionally required showing of a predicate in front of

                                  - 72 -
any   --   and   by    extension   all     --   homes   and    let   the   camera

continuously record for eight months.               And, Carpenter indicates

that the    point at which we consider whether the pole-camera

surveillance "contravened" a reasonable expectation of privacy is

the point at which the government "accesses"                   -- rather than

produces -- the record.        Id. at 2219.         Therefore, the resulting

pole-camera-generated record, if of sufficient duration, is like

historical CSLI in that it also can give the government the ability

both to "travel back in time" with little expense to witness with

perfect precision activities that turn out to be of any focused

interest to law enforcement only upon reflection and to do so

"effortlessly" in a way that precursor methods of home surveillance

practically could not.       Id. at 2216, 2218.

                                       C.

            Notwithstanding        these        similarities     between     the

surveillance means used in this case and the means at issue in

Carpenter, the government

[...TRUNCATED 98597 of 218597 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
