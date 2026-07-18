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

## GROUP: content/cases/United States v. Meyer.md  (`case`, 6 assertions)

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
{"assertion_id": "ec3fd3909a2daef3", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "19 F.4th 1028 (2021)", "court": "8th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Meyer", "year": "2021"}}
{"assertion_id": "216911f84a27a6a7", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A 'knock and talk' — approaching a home and knocking to ask questions — is a valid investigative technique, and where a suspect's evasive answers during such an encounter give officers an objectively reasonable basis to believe he will destroy digital evidence if left alone, the resulting exigency justifies a warrantless entry and seizure, provided the officers did not manufacture the exigency by threatening to violate the Fourth Amendment.", "title": "United States v. Meyer"}}
{"assertion_id": "8d462c453fbb13e4", "dimension": "support", "kind": "home_role", "locator": {"home": "Exigent Circumstances and Hot Pursuit"}, "payload": {"home": "Exigent Circumstances and Hot Pursuit", "role": "Related (cross-doctrine)", "title": "United States v. Meyer"}}
{"assertion_id": "de469a456a2a8b82", "dimension": "support", "kind": "home_role", "locator": {"home": "Knock and Talk"}, "payload": {"home": "Knock and Talk", "role": "Key", "title": "United States v. Meyer"}}
{"assertion_id": "0b985bd3d5bb61c3", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Meyer", "varies_by_point": "false"}}
{"assertion_id": "20d811f9c2d5540c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 8th Cir.", "title": "United States v. Meyer"}}
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

## GROUP: content/cases/United States v. Moore-Bush.md  (`case`, 8 assertions)

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
{"assertion_id": "28876c63217b8101", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "36 F.4th 320 (2022)", "court": "1st Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Moore-Bush", "year": "2022"}}
{"assertion_id": "35b9111922cacf93", "dimension": "support", "kind": "home_role", "locator": {"home": "Third-Party Doctrine & CSLI"}, "payload": {"home": "Third-Party Doctrine & CSLI", "role": "Related (cross-doctrine)", "title": "United States v. Moore-Bush"}}
{"assertion_id": "787b727857d87ba1", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Related (cross-doctrine)", "title": "United States v. Moore-Bush"}}
{"assertion_id": "7ada7692c4d58ba1", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Sitting en banc, the First Circuit unanimously reversed the suppression of evidence from eight months of continuous, warrantless pole-camera surveillance of a home's front curtilage and remanded with instructions to deny suppression — but the court divided evenly on the merits: three judges concluded the prolonged aggregate surveillance was a Fourth Amendment search, and three concluded it was not, so the decision established no binding circuit rule on whether such surveillance is a search.", "title": "United States v. Moore-Bush"}}
{"assertion_id": "a9b8cf5b208f22b4", "dimension": "support", "kind": "home_role", "locator": {"home": "Curtilage"}, "payload": {"home": "Curtilage", "role": "Related (cross-doctrine)", "title": "United States v. Moore-Bush"}}
{"assertion_id": "d3ebdfb09b20ff72", "dimension": "support", "kind": "home_role", "locator": {"home": "Fourth Amendment Framework"}, "payload": {"home": "Fourth Amendment Framework", "role": "Key", "title": "United States v. Moore-Bush"}}
{"assertion_id": "754b9f4486e127bc", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 1st Cir.", "title": "United States v. Moore-Bush"}}
{"assertion_id": "eee729ff37ea625e", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Moore-Bush", "varies_by_point": "false"}}
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

## GROUP: content/cases/United States v. Morley.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Morley"
type: case
citation: "99 F.4th 1328 (2024)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, Eleventh Circuit"
court_level: coa
circuit: 11th
year: 2024
date_decided: 2024-04-30
docket: 22-12988
authority_weight: "Binding in-circuit — 11th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2024-04-30
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Morley
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/9498175/united-states-v-derrick-alfondso-morley/"
  cluster_id: 9498175
  opinion_id: 9964788
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Recent development (role-based)"
related: ["[[Carroll v. United States]]", "[[United States v. Ross]]", "[[California v. Carney]]"]
aliases: ["United States v. Morley (11th Cir. 2024)"]
tags: ["case", "fourth-amendment", "automobile-exception", "vehicle-search", "probable-cause", "eleventh-circuit"]
holding: "Recites the modern two-element formulation of the automobile exception: a warrantless vehicle search is permitted if (1) the vehicle is…"
lake:
  record_id: United States v. Morley
  status: verified
  projected_at: 2026-07-09
---

# United States v. Morley

*99 F.4th 1328 (11th Cir. 2024)* · U.S. Court of Appeals, Eleventh Circuit · **Binding in-circuit — 11th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Morley was convicted of drug offenses arising from a controlled transaction. At an associate's direction, a cooperating individual (Fred) retrieved a briefcase containing cocaine from the passenger seat of Morley's car without a warrant. Morley moved to suppress the cocaine as the fruit of an unlawful search. The district court denied the motion, finding that the automobile exception (and apparent-authority consent) justified the warrantless search; Morley was convicted and appealed.

## Issue
Whether the warrantless retrieval of the briefcase from the passenger compartment of Morley's car was justified under the automobile exception to the Fourth Amendment's warrant requirement.

## Rule
The automobile exception permits a warrantless vehicle search on two elements. The court restated the circuit's formulation: "The automobile exception allows law enforcement to conduct a warrantless search of a vehicle if (1) the vehicle is readily mobile and (2) law enforcement has probable cause to search it." — *United States v. Morley*, 99 F.4th 1328 (11th Cir. 2024) (slip op., at 15). ^pin-op15

The first element is satisfied by mere operability: "All that is necessary to satisfy the first element is that the automobile is operational." — [*Id.*](https://www.courtlistener.com/opinion/9498175/united-states-v-derrick-alfondso-morley/#:~:text=All%20that%20is%20necessary%20to) ^pin-op15a

## Application
Both elements were satisfied here. Morley drove the car to the scene and did not dispute that it was readily mobile, so the first element was met. As to probable cause, Morley's associate had negotiated an $84,000 drug deal, Morley arrived and parked close to the associate's and the cooperating individual's cars, and the associate then directed the cooperating individual to retrieve the drugs from the passenger seat of Morley's car — facts the court held were more than enough to establish probable cause to search. Because both elements were met, law enforcement was authorized to conduct the warrantless search of Morley's car.

## Conclusion
Both elements of the automobile exception were satisfied, so the warrantless search of Morley's car was constitutionally permissible; the Eleventh Circuit affirmed the denial of Morley's suppression motion.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 11th Cir.**
- No negative treatment. *Morley* is a recent published Eleventh Circuit decision restating the circuit's two-element automobile-exception test (ready mobility + probable cause) and applying it to a vehicle driven to the scene of a drug transaction.

## Appears on
- [[Automobile Exception]] — *Recent development (role-based)*

## Sources
- *United States v. Morley*, 99 F.4th 1328 (11th Cir. 2024) — https://www.courtlistener.com/opinion/9498175/united-states-v-derrick-alfondso-morley/ — pinpoints given as slip-opinion pages (CourtListener carries the slip opinion; cluster 9498175 → opinion 9964788).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7b954e5146033080", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "99 F.4th 1328 (2024)", "court": "U.S. Court of Appeals, Eleventh Circuit", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Morley", "year": "2024"}}
{"assertion_id": "42b65ea5c8ca15d0", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Recites the modern two-element formulation of the automobile exception: a warrantless vehicle search is permitted if (1) the vehicle is…", "title": "United States v. Morley"}}
{"assertion_id": "dca00d9164caf39b", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Recent development (role-based)", "title": "United States v. Morley"}}
{"assertion_id": "74c4f72160884aa7", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 11th Cir.", "title": "United States v. Morley"}}
{"assertion_id": "930be2e5797450cd", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2024-04-30", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Morley", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Morley", "varies_by_point": "false"}}
```

### lake record — United States v. Morley

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Morley",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Derrick Alfondso Morley",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Morley",
    "court": "U.S. Court of Appeals, Eleventh Circuit",
    "court_id": "ca11",
    "court_level": "coa",
    "circuit": "11th",
    "state": null,
    "date_decided": "2024-04-30",
    "year": 2024,
    "docket": "22-12988",
    "cluster_id": 9498175,
    "lead_opinion_id": 9964788,
    "sibling_ids": [
      9964788
    ],
    "absolute_url": "/opinion/9498175/united-states-v-derrick-alfondso-morley/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "99 F.4th 1328",
      "volume": "99",
      "reporter": "F.4th",
      "page": "1328",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "99 F.4th 1328",
        "volume": "99",
        "reporter": "F.4th",
        "page": "1328",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "99 F.4th 1328",
    "official_selection": {
      "court_class": "coa",
      "selected": "99 F.4th 1328",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op15",
      "page": null,
      "quote": "--- # United States v. Morley *99 F.4th 1328 (11th Cir. 2024)* \u00b7 U.S. Court of Appeals, Eleventh Circuit \u00b7 **Binding in-circuit \u2014 11th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Morley was convicted of drug offenses arising from a controlled transaction. At an associate's direction, a cooperating individual (Fred) retrieved a briefcase containing cocaine from the passenger seat of Morley's car without a warrant. Morley moved to suppress the cocaine as the fruit of an unlawful search. The district court denied the motion, finding that the automobile exception (and apparent-authority consent) justified the warrantless search; Morley was convicted and appealed. ## Issue Whether the warrantless retrieval of the briefcase from the passenger compartment of Morley's car was justified under the automobile exception to the Fourth Amendment's warrant requirement. ## Rule The automobile exception permits a warrantless vehicle search on two elements. The court restated the circuit's formulation:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op15a",
      "page": null,
      "quote": "All that is necessary to satisfy the first element is that the automobile is operational.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 22722,
      "fragment": "#:~:text=All%20that%20is%20necessary%20to",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2024-04-30",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Morley",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Lawrence Alexander",
          "cluster_id": 10814315,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Morley:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(9964788) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca11)",
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
        "query": "cites:(9964788)",
        "reviewed": 1,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(9964788)",
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
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(9964788)",
    "indexed_citing_opinions": 1,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 9964788,
        "count": 1,
        "count_source": "search"
      }
    ],
    "citation_count": 10,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-morley.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 1,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 9964788,
        "cited_id": 70414,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 72529,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 76193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 77108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 77161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 77608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 78102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 78192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 78506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 216166,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 453288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 458882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 499145,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 551365,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 568540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 657263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 676156,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 679522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 770221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 773384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 820615,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 2648815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 2766686,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 4184984,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 4234128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 4283480,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 4301605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 4703255,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 9323286,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 9427680,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 9433305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9964788,
        "cited_id": 9477172,
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
    "date_created": "2026-07-06T01:51:28Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:51:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:51:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:52:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:51:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Morley

```
USCA11 Case: 22-12988    Document: 50-1      Date Filed: 04/30/2024   Page: 1 of 30




                                                            [PUBLISH]
                                    In the
                 United States Court of Appeals
                         For the Eleventh Circuit

                           ____________________

                                 No. 22-12988
                           ____________________

        UNITED STATES OF AMERICA,
                                                       Plaintiﬀ-Appellee,
        versus
        DERRICK ALFONDSO MORLEY,


                                                    Defendant-Appellant.


                           ____________________

                  Appeal from the United States District Court
                      for the Southern District of Florida
                     D.C. Docket No. 1:21-cr-20519-DPG-2
                           ____________________
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024     Page: 2 of 30




        2                       Opinion of the Court                22-12988

        Before WILSON, LUCK, and LAGOA, Circuit Judges.
        LAGOA, Circuit Judge:
                A jury convicted Derrick Morley of conspiracy to possess
        with intent to distribute five hundred grams or more of cocaine, in
        violation of 21 U.S.C. § 846, and possession with intent to distribute
        five hundred grams or more of cocaine, in violation of 21 U.S.C.
        § 841(a)(1). For each count, Morley was sentenced to a term of 60
        months’ imprisonment, to be served concurrently. Morley now
        appeals his convictions and sentence, arguing that: (1) the district
        court erred in denying his motion to suppress evidence that was
        the fruit of an unlawful search; (2) the trial evidence was insuffi-
        cient to support his convictions; (3) the district court erred in
        providing a deliberate ignorance jury instruction; and (4) the dis-
        trict court erred in denying him a safety valve sentence reduction
        under 18 U.S.C. § 3553(f). After carefully considering the parties’
        arguments and with the benefit of oral argument, we affirm Mor-
        ley’s convictions and sentence.
             I.     FACTUAL & PROCEDURAL BACKGROUND
               We begin with the government’s trial evidence as to two
        separate cocaine deals that led to Morley’s arrest. The first deal
        took place on August 6, 2021, when Morley’s associate and code-
        fendant, Valentino Edgecombe, sold half a kilogram of cocaine to
        a paid FBI confidential informant (“Fred”). The FBI learned, in
        early August 2021, that Edgecombe, a Bahamian national, had been
        in South Florida “looking to try to get off some dope.” Based on
        this information, Fred, at the FBI’s direction, arranged to meet
USCA11 Case: 22-12988       Document: 50-1      Date Filed: 04/30/2024      Page: 3 of 30




        22-12988                Opinion of the Court                          3

        Edgecombe in the parking lot of a Miami shopping mall, outside of
        a Bass Pro Shops. With law enforcement officers surveilling, Fred
        bought half a kilogram of cocaine from Edgecombe for $14,000.
                Following the first cocaine deal, Fred tried to negotiate a big-
        ger deal for six kilograms of cocaine. On September 22, 2021, on a
        recorded phone call, Fred told Edgecombe that he had the money
        ready to buy more cocaine. About ten minutes later, on a second
        recorded phone call, Edgecombe offered to send Fred “straight to
        the person” with the cocaine. Edgecombe explained, however,
        that the person would only relinquish the cocaine if Edgecombe
        first cleared his debt, which he’d previously said he owed to “the
        guy who was holding the dope.”
               About an hour after the second recorded phone call, law en-
        forcement observed Edgecombe meet up with Morley in the park-
        ing lot of a Fort Lauderdale hotel where Edgecombe was staying.
        Morley arrived in a maroon BMW, which law enforcement later
        confirmed that he owned. Morley parked near Edgecombe, en-
        tered Edgecombe’s car, and they drove off together. Expecting a
        deal to occur, law enforcement tracked Edgecombe and Morley
        from the hotel, first to a car parts store and then to a Sam’s Club.
        However, no deal took place that day.
               Instead, the second deal happened six days later on Septem-
        ber 28, 2021. The day prior, in a recorded phone call, Edgecombe
        again told Fred that he had to take him straight to his cocaine
        source to clear his debt and make the deal. Fred agreed to pay
        $28,000 per kilogram of cocaine, and the two decided they would
USCA11 Case: 22-12988      Document: 50-1     Date Filed: 04/30/2024     Page: 4 of 30




        4                      Opinion of the Court                22-12988

        meet up the next day and go together to the cocaine source. On
        the morning of the deal, Edgecombe sent a WhatsApp message to
        Fred indicating that he could sell him three kilograms of cocaine.
               Later that evening, before meeting Edgecombe, Fred met
        with law enforcement to prepare for a “controlled evidence pur-
        chase arrest operation.” Law enforcement gave Fred a hat
        equipped with a covert videorecording device and a backpack con-
        taining money for the deal. Law enforcement also told Fred to per-
        suade Edgecombe to meet him in “a specific part” of a parking lot
        of a Home Depot rather than going with Edgecombe to his source.
               Fred arrived at the Home Depot and, to coax Edgecombe
        into meeting him there, told Edgecombe that his car battery “was
        dead” and that his key “won’t crank.” Edgecombe ultimately
        agreed over the phone to meet Fred at the Home Depot to com-
        plete the deal. So, Fred sent a text message to Edgecombe with the
        address of the Home Depot.
               Edgecombe arrived at the Home Depot at around 8:30 p.m.
        and parked his car next to Fred’s car. Fred asked whether
        Edgecombe had the cocaine with him, and Edgecombe responded,
        “Yeah someone is right there” and promised “[i]t’s coming.”
        Edgecombe then tried to persuade Fred to get in the car with him,
        but Fred refused, stating “I can’t get in the car with you. I got too
        much money. I don’t got no gun.” Fred told Edgecombe to “tell
        [his] peoples” he can only get in Edgecombe’s car if he sees the co-
        caine first.
USCA11 Case: 22-12988      Document: 50-1     Date Filed: 04/30/2024     Page: 5 of 30




        22-12988               Opinion of the Court                        5

               Minutes later, Morley arrived in his maroon BMW and
        “trolled through the parking lot.” He parked his car, got out, and
        quickly walked toward a nearby Wendy’s restaurant. Edgecombe
        instructed Fred to “[g]o get it” from Morley’s passenger seat. Fred
        retrieved a “small briefcase” from Morley’s car and brought it to
        his car, confirming that it contained three kilograms of cocaine.
                  In the meantime, Morley tried to enter the Wendy’s, but the
        door was locked, so he paced back and forth outside. All the while,
        Morley kept looking back toward the Home Depot parking lot:
        “[H]e just kept looking over his shoulder and then he walked into
        . . . [t]he driveway area of Wendy’s, and he just kind of lingered in
        the area kind of like looking at the BMW, just watching it.” After
        several minutes, Morley walked across the street to help a family
        with a broken-down car.
              After Fred gave Edgecombe $84,000 for the cocaine, law en-
        forcement arrested Edgecombe. Law enforcement then arrested
        Morley across the street.
               Incident to his arrest, agents seized Morley’s cellphone, got
        a search warrant, and accessed his phone. The search revealed ex-
        tensive communications between Morley and Edgecombe leading
        up to the second cocaine deal, as well as evidence that Morley had
        acted on that communication. For instance, Morley and
        Edgecombe called each other fifteen times on the night of Septem-
        ber 28. Edgecombe also sent the address of the Home Depot to
        Morley in a text message, which came two minutes after Fred had
        sent the same address to Edgecombe. Data from Morley’s phone
USCA11 Case: 22-12988     Document: 50-1     Date Filed: 04/30/2024   Page: 6 of 30




        6                     Opinion of the Court               22-12988

        showed that he looked up directions from his home in Fort Lauder-
        dale to the Home Depot two minutes after Edgecombe had sent
        him the address.
               Edgecombe and Morley had also communicated in the lead-
        up to the first cocaine deal. On August 3, 2021, Edgecombe texted
        Morley, “i want you ride with me to deal with something also make
        yourself available” and “whenever i call you i want ride with me.”
        Then, on the day of the first deal, Edgecombe sent Morley a mes-
        sage with the address of the same Bass Pro Shops where Fred met
        Edgecombe.
             A grand jury returned a three-count indictment charging
        Morley with conspiring to possess with intent to distribute five
        hundred grams or more of cocaine in violation of 21 U.S.C. § 846
        (Count 1) and possessing with intent to distribute five hundred
        grams or more of cocaine in violation of 21 U.S.C. § 841(a)(1)
        (Count 3).
               Morley moved to suppress the cocaine that Fred, at
        Edgecombe’s direction, took from Morley’s vehicle without a war-
        rant. The government opposed Morley’s suppression motion. The
        government argued that the automobile exception to the Fourth
        Amendment’s warrant requirement applied because there was a
        fair probability that Fred would find contraband in Morley’s car.
        The government noted that Fred and Edgecombe “had negotiated
        an $84,000 drug deal, and Edgecombe—who had previously sold
        [Fred] half a kilogram of cocaine—told [Fred] where to find the
        drugs.” Thus, the government concluded, Fred reasonably
USCA11 Case: 22-12988       Document: 50-1       Date Filed: 04/30/2024     Page: 7 of 30




        22-12988                Opinion of the Court                           7

        believed he would find drugs in Morley’s car. In any event, the
        government added, the consent exception applied because Fred
        reasonably believed Edgecombe had the authority to direct him to
        search Morley’s car. Morley argued that neither of the two rele-
        vant exceptions to the Fourth Amendment’s warrant requirement
        applied to Fred’s search of his car.
                The district court held an evidentiary hearing at which Mi-
        ami-Dade Detective and FBI Organized Crime Task Force Officer
        Wendell Johnson testified. After hearing the officer’s testimony,
        the district court denied Morley’s motion. First, the district court
        found that there was probable cause to believe Morley’s car con-
        tained contraband or evidence of a crime because Edgecombe and
        Fred “picked specific remote locations” for their drug deals, and
        “it’s really hard to believe that . . . [Morley] pulled up in close prox-
        imity” by happenstance. And second, the district court found that
        apparent authority existed under the circumstances because “the
        drugs were retrieved exactly where Mr. Edgecombe said that they
        would be.”
               Morley proceeded to a four-day jury trial. The govern-
        ment’s proposed jury instructions included the pattern instruction
        on deliberate ignorance. At the charge conference, Morley ob-
        jected to the government’s proposed deliberate ignorance instruc-
        tion. He contended that the record did not support the instruction
        because “[t]here ha[d] been no proof of any evidence in reference
        to fingerprints or . . . DNA” and “the testimony on exactly where
        the bag was located and how it was taken out of the car is extremely
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024     Page: 8 of 30




        8                      Opinion of the Court                 22-12988

        wishy-washy.” In response, the government argued that deliberate
        ignorance was “an alternative proof,” which was “consistent with
        the evidence that Edgecombe had him drive a bag to the Home
        Depot, and he never made any attempt to ask Edgecombe what
        was in that bag, despite the multiple calls they had.” The district
        court deferred ruling on Morley’s objection.
                After the close of the evidence, the district court decided to
        give the jury instruction because the evidence “equally could be
        consistent with actual knowledge or deliberate ignorance.” The
        district court pointed to Morley’s actions, like walking away from
        the car, and the way the drugs were packaged. The instruction
        mirrored the government’s proposed instruction.
               During trial, Morley twice moved for a judgment of acquit-
        tal under Federal Rule of Criminal Procedure 29(a). The district
        court denied both of his motions. The jury ultimately found him
        guilty as charged in the indictment. Afterward, Morley moved for
        a judgment of acquittal notwithstanding the verdict under Rule
        29(c). The district court denied his motion in a paperless order.
               Before sentencing, the United States Probation Office pre-
        pared a Presentence Investigation Report (“PSI”) using the 2021
        Sentencing Guidelines Manual. The PSI held Morley accountable
        for 3.518 kilograms of cocaine (about half a kilogram for the August
        6 deal and three kilograms for the September 28 deal), resulting in
        a total offense level of 28. It also assessed three criminal history
        points based on Morley’s prior 37-month sentence for conspiracy
        to import 100 kilograms or more of marijuana. With three criminal
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024      Page: 9 of 30




        22-12988               Opinion of the Court                          9

        history points, Morley fell into criminal history category II. To-
        gether, Morley’s total offense level and criminal history category
        produced a guideline range of 87 to 108 months’ imprisonment.
               Through his trial attorney, Morley filed several objections to
        the PSI’s description of his offense conduct. Despite the jury’s ver-
        dict, Morley maintained his innocence and “denied all knowledge”
        of Edgecombe’s sale of cocaine to Fred. In support, Morley at-
        tached a post-trial polygraph examination report, which claimed
        Morley “was truthful” in denying his knowledge of the conspiracy
        and the cocaine. Morley attached the full version of the polygraph
        examiner’s report to a motion for a downward variance filed a cou-
        ple of weeks later.
                A new attorney later entered his appearance to represent
        Morley for sentencing. Through his sentencing attorney, Morley
        filed additional objections to the PSI in which, among other things,
        he argued for a base offense level of 26, because the evidence only
        supported his responsibility for the September 28 deal, and a role
        reduction under U.S.S.G. § 3B1.2. Morley also moved to continue
        his sentencing hearing because his sentencing attorney, unlike his
        trial attorney, believed that he might qualify for relief from the
        mandatory minimum sentence under 18 U.S.C. § 3553(f). Known
        as the safety valve, that statute allows the district court to impose
        a sentence below the mandatory minimum sentence for drug
        crimes if the defendant meets five criteria. § 3553(f)(1)–(5). Two
        of the statutory criteria are relevant here. First, under § 3553(f)(1),
        the district court must find that:
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024      Page: 10 of 30




        10                      Opinion of the Court                  22-12988

               (1) the defendant does not have—
                  (A) more than 4 criminal history points, ex-
                  cluding any criminal history points resulting
                  from a 1-point offense, as determined under
                  the sentencing guidelines;
                  (B) a prior 3-point offense, as determined un-
                  der the sentencing guidelines; and
                  (C) a prior 2-point offense, as determined un-
                  der the sentencing guidelines[.]
               Second, under § 3553(f)(5), the district court must find that
        the defendant truthfully provided to the government “all infor-
        mation and evidence the defendant has concerning the offense or
        offenses that were part of the same course of conduct or of a com-
        mon scheme or plan.”
               As for § 3553(f)(1), Morley argued that his prior three-point
        offense for conspiracy to import marijuana did not preclude him
        from relief because the safety valve’s criminal- history-point provi-
        sion is “conjunctive.” The safety valve, he argued, only excludes
        defendants who have all three things: (A) more than four criminal
        history points, excluding any points from one-point offenses, (B) a
        prior three-point offense, and (C) a prior two-point violent offense.
        And because he did not have more than four criminal history points
        or a prior two-point violent offense, he could qualify for relief if the
        court gave him time to submit a truthful statement to the govern-
        ment.
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024     Page: 11 of 30




        22-12988               Opinion of the Court                         11

                After the district court continued Morley’s sentencing hear-
        ing, he submitted a written safety valve statement in an attempt to
        comply with § 3553(f)(5). In his statement, Morley again claimed
        he did not know he had delivered cocaine to a drug deal. He ex-
        plained that, when he arrived at the Home Depot, he “walked to a
        nearby Wendy’s for something to eat” and left his car unlocked
        “because the locks did not work (as shown in the trial) in an at-
        tempt to buy some food.” He pointed to his post-arrest statements
        and the polygraph test for corroboration of his lack of knowledge.
        But in the end, he admitted, whether it “was naïve, stupid or com-
        pletely negligent,” he “did bring the bag which contained cocaine
        in this case to the parking lot of the Home Depot,” and he accepted
        full responsibility for it.
               At sentencing, the district court granted two of Morley’s ob-
        jections to the PSI’s offense-level calculation. First, it found Morley
        responsible for 3, rather than 3.518, kilograms of cocaine, which
        reduced his base offense level to 26 under U.S.S.G. § 2D1.1(c)(7).
        Second, it awarded Morley a two-level minor role reduction under
        U.S.S.G. § 3B1.2, producing a new total offense level of 24.
                The district court then found Morley did not qualify for
        safety-valve relief both because of his criminal history and his fail-
        ure to truthfully provide the government with all the information
        he had concerning his offenses. As to his criminal history, the dis-
        trict court interpreted § 3553(f)(1) as “disjunctive,” meaning a de-
        fendant must not have any of (1) more than four criminal history
        points, (2) a prior three-point offense, or (3) a prior two-point
USCA11 Case: 22-12988         Document: 50-1   Date Filed: 04/30/2024     Page: 12 of 30




        12                       Opinion of the Court                22-12988

        violent offense to qualify for relief. And because Morley had a prior
        three-point offense, the court found that he was not safety-valve
        eligible. As to his statement, the district court agreed with Morley’s
        contention that the government’s “belief regarding truthfulness”
        and noted that “perhaps” even “the jury’s findings” did not prevent
        it from finding his statement truthful. Still, the district court disa-
        greed that Morley provided a truthful and complete statement un-
        der § 3553(f)(5), particularly considering the government’s “strong
        circumstantial case.”
               The district court found that Morley’s total offense level of
        24 and his criminal history category of II produced a guideline
        range of 57 to 71 months. Because the mandatory minimum sen-
        tence for his offenses was 60 months, however, the district court
        calculated the guideline range as 60 to 71 months. The govern-
        ment advocated for a 65-month term of imprisonment, citing Mor-
        ley’s prior 37-month sentence for his federal drug conviction and
        the need to promote deterrence, respect for the law, “and send a
        message that the defendant should not be dealing with drugs.”
        Morley asked for the mandatory minimum sentence of 60 months.
        Before the district court imposed its sentence, it allowed Morley to
        provide a statement.
              The district court sentenced Morley to two concurrent
        terms of 60 months’ imprisonment on both counts, the mandatory
        minimum sentence for each count under § 841(b)(1)(B)(ii). This
        timely appeal followed.
                        II.      STANDARDS OF REVIEW
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024      Page: 13 of 30




        22-12988                Opinion of the Court                         13

               A district court’s denial of a motion to suppress evidence is
        reviewed under a mixed standard. United States v. Jiminez, 224 F.3d
        1243, 1247 (11th Cir. 2000). We review the district court’s findings
        of fact under the clearly erroneous standard and its application of
        law to those facts de novo. Id. We also give “due weight” to the
        inferences that the district court and law enforcement officers draw
        from the facts. Ornelas v. United States, 517 U.S. 690, 699 (1996).
        When considering a ruling on a motion to suppress, we must con-
        strue all facts in the light most favorable to the party prevailing in
        the district court. United States v. Behety, 32 F.3d 503, 510 (11th Cir.
        1994).
                “We review de novo a [d]istrict [c]ourt’s denial of judgment
        of acquittal on sufficiency of evidence grounds, considering the ev-
        idence in the light most favorable to the [g]overnment, and draw-
        ing all reasonable inferences and credibility choices in the [g]overn-
        ment’s favor.” United States v. Capers, 708 F.3d 1286, 1296 (11th Cir.
        2013) (emphasis omitted). We must affirm if “after viewing the ev-
        idence in the light most favorable to the prosecution, any rational
        trier of fact could have found the essential elements of the crime[s]
        beyond a reasonable doubt.” United States v. Hernandez, 433 F.3d
        1328, 1335 (11th Cir. 2005) (emphasis omitted) (quoting Jackson v.
        Virginia, 443 U.S. 307, 319 (1979)).
               We also review de novo whether the circumstances of a par-
        ticular case rendered it appropriate to instruct the jury on deliber-
        ate ignorance. United States v. Stone, 9 F.3d 934, 937 (11th Cir. 1993).
        But our review of jury instructions is deferential, and we will
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024     Page: 14 of 30




        14                     Opinion of the Court                  22-12988

        reverse only “if we are left with a substantial and eradicable doubt
        as to whether the jury was properly guided in its deliberations.”
        United States v. Crabtree, 878 F.3d 1274, 1289 (11th Cir. 2018) (quot-
        ing United States v. Steed, 548 F.3d 961, 977 (11th Cir. 2008)).
                                 III.   ANALYSIS
                On appeal, Morley argues that: (1) the district court erred in
        denying his motion to suppress the evidence of the briefcase as the
        fruit of an unlawful search; (2) the evidence at trial was insufficient
        to support his convictions; (3) the district court erred in providing
        a deliberate ignorance jury instruction; and (4) the district court
        erred in denying him a safety valve sentence reduction. We ad-
        dress each of his challenges in turn.
                             A. The Motion to Suppress
                Morley argues that Fred’s retrieval of the briefcase from the
        passenger seat of Morley’s car was an unconstitutional search in
        violation of the Fourth Amendment. It is undisputed that Fred’s
        actions amounted to a warrantless search that implicated the
        Fourth Amendment’s protections. We must determine, however,
        whether any exception to the Fourth Amendment’s warrant re-
        quirement rendered the search constitutionally permissible. The
        district court specifically found that two exceptions applied: the au-
        tomobile exception and the consent exception by way of apparent
        authority.
              As an initial matter, Morley mischaracterizes the automobile
        and apparent authority doctrines as requirements that must be met
        for a valid search. Those doctrines, however, are separate
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024     Page: 15 of 30




        22-12988               Opinion of the Court                         15

        exceptions to the Fourth Amendment’s warrant requirement, and
        either of which may provide an independent basis for us to affirm
        the denial of Morley’s suppression motion. Here, we conclude that
        the district court did not abuse its discretion in finding that the au-
        tomobile exception applied.
                The automobile exception allows law enforcement to con-
        duct a warrantless search of a vehicle if (1) the vehicle is readily
        mobile and (2) law enforcement has probable cause to search it.
        United States v. Lindsey, 482 F.3d 1285, 1293 (11th Cir. 2007). All
        that is necessary to satisfy the first element is that the automobile
        is operational. United States v. Watts, 329 F.3d 1282, 1286 (11th Cir.
        2003). In United States v. Nixon, 918 F.2d 895 (11th Cir. 1990), this
        Court explained that “ready mobility” is “inherent in all automo-
        biles that reasonably appear to be capable of functioning.” Id. at
        903 (emphasis in original); see also United States v. Alexander, 835
        F.2d 1406, 1409 (11th Cir. 1988) (stating that the vehicle need not
        be moving at the moment when police obtain probable cause to
        search and that the ability of a vehicle to become mobile is suffi-
        cient). That requirement is met here because Morley drove the car
        to the scene, nor does Morley challenge that his vehicle was readily
        mobile. See Sapuppo v. Allstate Floridian Ins. Co., 739 F.3d 678, 680
        (11th Cir. 2014) (noting that a party abandons an issue by not rais-
        ing it on appeal).
              Turning to the second element, probable cause exists when,
        “under the totality of the circumstances, there is a fair probability
        that contraband or evidence of a crime will be found in the
USCA11 Case: 22-12988     Document: 50-1     Date Filed: 04/30/2024    Page: 16 of 30




        16                    Opinion of the Court                22-12988

        vehicle.” Lindsey, 482 F.3d at 1293 (citation omitted). For example,
        in United States v. Lanzon, 639 F.3d 1293 (11th Cir. 2011), we held
        that the district court did not err in denying Lanzon’s motion to
        suppress because officers had probable cause to search Lanzon’s
        truck pursuant to the automobile exception. Id. at 1300. In that
        case, Lanzon participated in instant message conversations with an
        undercover agent posing as “Tom.” Id. Lanzon described to
        “Tom” his intent to have sex with a minor, and he agreed to meet
        “Tom” and the minor at a specific time and place and to bring col-
        ored condoms with him. Id. After driving his truck to the desig-
        nated meeting place at the agreed-upon time, Lanzon approached
        the officers who were posing as “Tom” and the minor and said,
        “Tom, Tom.” Id. Lanzon was then arrested, and a search of his
        person yielded no condoms. Id. The officers sought Lanzon’s con-
        sent to search his truck, but he refused. Id. at 1297. The officers
        then searched the truck anyway—using Lanzon’s keys to open it—
        and found the colored condoms, along with flavored lubricant and
        a receipt for the purchase of those items. Id. During his criminal
        proceedings, Lanzon filed to suppress the evidence seized from his
        truck, which the district court denied. Id. at 1299. On appeal, we
        held that, under the totality of the circumstances, there was a fair
        probability that evidence of a crime would be found in Lanzon’s
        vehicle. Id. at 1300.
               The facts and circumstances known to law enforcement
        here are similar to those in Lanzon. As in Lanzon, law enforcement
        here, via a confidential informant, engaged in conversations with
        Edgecombe that led to an agreement to meet at a specific time and
USCA11 Case: 22-12988     Document: 50-1      Date Filed: 04/30/2024     Page: 17 of 30




        22-12988               Opinion of the Court                        17

        place for an illicit act. The only significant difference here is the
        involvement of a third party, Morley. But Morley arrived at the
        designated meeting place at the agreed upon time, minutes after
        Edgecombe had texted him to come, and after Edgecombe told
        Fred that the cocaine was on its way. When Morley arrived, it was
        clear that Edgecombe recognized him. Indeed, Edgecombe explic-
        itly directed Fred to retrieve the cocaine from Morley’s car. There
        was more than a reasonable probability that Fred would find con-
        traband in the exact place that Edgecombe told him to look.
               Morley’s argument against probable cause relies heavily on
        one unpublished case, United States v. Smith, 596 F. App’x 804 (11th
        Cir. 2015), in which this Court affirmed a district court’s finding
        that probable cause existed. Id. at 807. In Smith, this Court held
        that a police officer’s credible belief that “he smelled marijuana
        coming from the car” of the defendant, whom he had just arrested
        for marijuana possession, sufficed to show probable cause to con-
        duct a warrantless search of the vehicle. Id. Morley’s argument
        largely consists of a recitation of the facts in Smith in an effort to
        distinguish it from the facts here. But there are multiple problems
        with Morley’s approach. For starters, Morley fails to explain how
        an unpublished case in which this Court found that law enforce-
        ment acted reasonably establishes that law enforcement acted un-
        reasonably here. Additionally, unlike the officer in Smith, Fred did
        not have to logically deduce that there might be contraband in the
        car based on smell or any other subjective factor. Fred searched
        Morley’s car after Edgecombe first told Fred that the cocaine was
        on its way and then specifically directed him to “[g]o get” the
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024     Page: 18 of 30




        18                     Opinion of the Court                  22-12988

        cocaine from Morley’s passenger seat. Thus, the probability that
        Fred would find contraband in Morley’s car was no less than it was
        in Smith.
               Morley also misconstrues both the standard of review and
        the legal test for probable cause. Regarding the standard of review,
        he argues that it “is not improbable that no reasonable fact finder
        could accept” an alternative explanation. Our review, however,
        does not ask whether there is some possible alternative explanation
        that a reasonable factfinder could have accepted. Rather, we re-
        view the district court’s findings of fact only for clear error, and we
        must give due weight to the inferences that the district court and
        law enforcement officers draw from those facts. Ornelas, 517 U.S.
        at 699. And when considering a ruling on a motion to suppress, we
        must construe all facts in the light most favorable to the party pre-
        vailing in the district court—here, the government. See Behety, 32
        F.3d at 510.
                As to the proper legal test, Morley argues that he was merely
        used by Edgecombe as a pawn to unwittingly facilitate the Septem-
        ber 28 deal. This conclusion, he contends, is supported by the fact
        that Edgecombe unilaterally involved an innocent decoy for the
        prior August 6 drug deal. But Morley’s knowledge, or lack thereof,
        is irrelevant to the probable cause inquiry. Instead, it is “the facts
        and circumstances within [law enforcement’s] knowledge” that
        matter. Rankin v. Evans, 133 F.3d 1425, 1435 (11th Cir. 1998) (quot-
        ing Williamson v. Mills, 65 F.3d 155, 158 (11th Cir. 1995)). Even if
        Morley were “unwittingly duped” into bringing the cocaine to the
USCA11 Case: 22-12988     Document: 50-1     Date Filed: 04/30/2024   Page: 19 of 30




        22-12988              Opinion of the Court                      19

        deal, his supposed lack of knowledge has no bearing on law en-
        forcement’s knowledge as to the probability that Morley’s car con-
        tained cocaine.
               Under the totality of the circumstances, the facts and cir-
        cumstances that were known to law enforcement at the relevant
        time supported a fair probability that cocaine would be found in
        Morley’s vehicle. Edgecombe had previously sold Fred half a kilo-
        gram of cocaine, and Fred and Edgecombe had no other relation-
        ship besides that of customer and drug dealer. Turning to the night
        of September 28, Fred and Edgecombe had negotiated an $84,000
        drug deal, and Edgecombe made it clear to Fred that he was not
        working alone. Edgecombe consistently asked Fred to go straight
        to “the guy who was holding the dope.” And on the night of the
        deal, Edgecombe asked Fred to drive with him to a different loca-
        tion to get the cocaine from another person. After Fred refused,
        Edgecombe told Fred that his associate was bringing it to them at
        the Home Depot. Shortly afterward, Morley arrived, and parked
        his vehicle close to Edgecombe and Fred’s cars. Edgecombe then
        directed Fred to retrieve the drugs from the passenger seat of Mor-
        ley’s car. This was more than enough to establish probable cause
        under the automobile exception.
                Because both elements of the automobile exception were
        satisfied, law enforcement was authorized to conduct a warrantless
        search of Morley’s car. Watts, 329 F.3d at 1286. We therefore af-
        firm the district court’s denial of Morley’s motion to suppress.
USCA11 Case: 22-12988        Document: 50-1   Date Filed: 04/30/2024     Page: 20 of 30




        20                      Opinion of the Court                22-12988

                        B.      Sufficiency of the Evidence
                Morley next challenges the sufficiency of the evidence sup-
        porting his convictions for conspiracy to possess with intent to dis-
        tribute cocaine in violation of 21 U.S.C. § 846 and possession of co-
        caine with intent to distribute in violation of 21 U.S.C. § 841(a)(1).
        Morley argues that the evidence here was solely circumstantial and
        that it was insufficient for a reasonable jury to find him guilty be-
        yond a reasonable doubt. Specifically, Morley argues that the pros-
        ecution failed to prove that he was a willing participant in the con-
        spiracy and that he knew that the briefcase contained cocaine.
                Both of the offenses for which Morley was convicted have a
        guilty knowledge element. The conspiracy charge under § 846 re-
        quired the government to prove: (1) the existence of an illegal
        agreement between two or more people to distribute cocaine; (2)
        that Morley knew of the agreement and its goal; and (3) that Mor-
        ley knowingly joined or participated in the agreement. See United
        States v. Brown, 587 F.3d 1082, 1089 (11th Cir. 2009). And the sub-
        stantive possession charge under § 841(a)(1) required the govern-
        ment to prove that Morley knowingly possessed cocaine and in-
        tended to distribute it. United States v. Mercer, 541 F.3d 1070, 1076
        (11th Cir. 2008). Because guilty knowledge can rarely be estab-
        lished directly, however, “a jury may infer knowledge and criminal
        intent from circumstantial evidence alone.” United States v. Duenas,
        891 F.3d 1330, 1334 (11th Cir. 2018).
             Morley argues that the circumstantial evidence here is not
        enough to support an inference of knowledge. He contends that
USCA11 Case: 22-12988     Document: 50-1      Date Filed: 04/30/2024     Page: 21 of 30




        22-12988               Opinion of the Court                        21

        this is a case of “guilt by association,” and that close association
        with a co-conspirator or mere presence at the scene of the crime is
        insufficient evidence to prove knowing participation in a conspir-
        acy. Morley is correct that “[n]either association with a co-con-
        spirator nor presence at the scene of a crime, standing alone, will
        support a finding of specific knowledge.” Id. (citing United States v.
        Louis, 861 F.3d 1330, 1333 (11th Cir. 2017)). But “presence none-
        theless is a probative factor which the jury may consider in deter-
        mining whether a defendant was a knowing and intentional partic-
        ipant in a criminal scheme.” United States v. Miranda, 425 F.3d 953,
        959 (11th Cir. 2005) (quoting United States v. McDowell, 250 F.3d
        1354, 1365 (11th Cir. 2001)).
                Relying mainly on our decision in United States v. Sullivan,
        763 F.2d 1215 (11th Cir. 1985), Morley argues that his association
        with Edgecombe along with his presence at the scene is insufficient
        to support his convictions. In Sullivan, six codefendants were con-
        victed of conspiring to import marijuana from Columbia and dis-
        tribute it in the United States. Id. at 1216. The plan was to fly the
        marijuana to Florida, and then at the airport landing strip, to of-
        fload that marijuana into vans. Id. at 1216–17. Those vans would
        then deliver the marijuana to other drivers who would be waiting
        at a nearby hotel and would keep distributing the marijuana. Id.
        All six codefendants appealed the sufficiency of the evidence sup-
        porting their conspiracy convictions, but this Court found that only
        one codefendant, Martos, raised a legitimate challenge. Id. at 1218.
USCA11 Case: 22-12988     Document: 50-1      Date Filed: 04/30/2024    Page: 22 of 30




        22                     Opinion of the Court                22-12988

               This Court summarized the evidence related to Martos as
        follows. Drug Enforcement Administration agents saw Martos in
        a hotel parking lot near a red van. Id. at 1219. A codefendant, Mar-
        tinez, arrived in a blue van and walked over to Martos. Id. Martos
        and Martinez then walked over to two other codefendants, and all
        four walked around the parking lot for about five minutes. Id.
        Martos and Martinez went to the blue van and one of them, though
        it was never established who, removed a small bag from the van.
        Id. The two then went into the hotel lounge. Id. All four of them
        were later arrested, including Martos. Id. When Martos was ar-
        rested, he was with Martinez who was carrying the small handbag,
        which was found to contain a pistol. Id. There was no marijuana
        found at the scene of arrest because the plan was for other conspira-
        tors to offload the marijuana from the planes and transport it to the
        hotel to meet separate drivers who would distribute it to various
        other points. Id. at 1217. Therefore, though the police knew that
        some alleged conspirators would be drivers in the hotel parking lot
        awaiting other conspirators delivering marijuana from the airport,
        there was no evidence as to who the drivers at the hotel would be.
        Id.
               We reversed Martos’s conviction because there was no evi-
        dence that Martos knew of the existence of the conspiracy or that
        he knew that the van was intended to transport marijuana. Id. His
        conviction, rather, was seemingly based only “on his presence at
        the scene in the [hotel] parking lot.” Id. He was never “observed
        doing anything from which the jury could draw an inference that
        he was a member of the conspiracy.” Id.
USCA11 Case: 22-12988     Document: 50-1      Date Filed: 04/30/2024     Page: 23 of 30




        22-12988               Opinion of the Court                        23

               Morley contends that this case is similar to Martos’s in Sulli-
        van because there was no evidence that Morley knew Edgecombe
        was planning to sell cocaine on August 6 or September 22 or that
        Morley knew Edgecombe’s briefcase contained cocaine that
        Edgecombe would instruct Fred to retrieve from Morley’s car. In-
        stead, Morley argues, he merely believed that he was meeting his
        friend, Edgecombe, after they scheduled a meeting at Home Depot
        for Morley to return the case left in his car. Morley points out that
        neither his DNA nor latent fingerprints were found on the cocaine
        or briefcase, so there was insufficient proof that he knew that he
        was transporting cocaine.
                The circumstantial evidence here, however, is far greater
        than it was in Sullivan and was more than sufficient for the jury to
        infer Morley’s knowledge. For starters, no marijuana was recov-
        ered at the scene of arrest in Sullivan, so it was much more attenu-
        ated to impute, to Martos, knowledge of a conspiracy to distribute
        drugs that Martos never physically possessed. In this case, it is un-
        disputed that Morley was in physical possession of the three kilo-
        grams of cocaine and that he transported the cocaine to the scene
        of the drug deal at the time it was supposed to occur. The only
        issue is whether a reasonable jury could have inferred that Morley
        knowingly agreed to do so despite his contention that he was an
        unsuspecting pawn. While knowledge requirements may vary
        widely based on the individual facts of each case, a jury can infer
        knowledge using certain guideposts, such as whether “a defendant
        was instrumental to a plan’s success, had ample opportunities to
        discover the critical fact, and was in frequent contact with someone
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024     Page: 24 of 30




        24                     Opinion of the Court                  22-12988

        who knew that fact.” United States v. Colston, 4 F.4th 1179, 1190
        (11th Cir. 2021). Viewed in the light most favorable to the verdict,
        a reasonable jury could have found that Morley knew of the plan
        to deliver cocaine to a drug deal.
                Morley played an instrumental role in the plan’s success.
        Edgecombe relied on Morley to deliver $84,000 worth of cocaine
        to a drug deal that Edgecombe had been discussing with Fred for
        over a month. And a prudent drug dealer is not likely to entrust
        the delivery of costly amounts of drugs to unwitting participants.
        In fact, we have repeatedly held that because “‘a prudent smuggler
        is not likely to suffer the presence of unaffiliated bystanders,’ when
        the orchestrator of a conspiracy vests substantial trust in an associ-
        ate to contribute to the scheme, a jury may infer the associate’s
        knowing participation.” Duenas, 891 F.3d at 1334 (quoting United
        States v. Cruz-Valdez, 773 F.2d 1541, 1547 (11th Cir. 1985) (en banc)).
        The deal’s success depended on Morley delivering the cocaine. He
        did so, arriving at the designated meeting site, at the designated
        meeting time, minutes after Edgecombe directed him to show up.
               Morley’s communications with Edgecombe further support
        the inference of knowledge. On the day of the drug deal, Morley
        was in consistent contact with Edgecombe, who had brokered the
        cocaine deal with Fred. Morley’s phone records showed that he
        and Edgecombe called each other fifteen times, including multiple
        phone calls after Edgecombe had sent Morley the Home Depot ad-
        dress. The communications leading up to the September 28 deal
        suggested Morley’s knowledge, too. On September 22, Fred and
USCA11 Case: 22-12988     Document: 50-1      Date Filed: 04/30/2024     Page: 25 of 30




        22-12988               Opinion of the Court                        25

        Edgecombe had a conversation at 10:01 a.m. about a deal for six
        kilograms of cocaine. During that call, Edgecombe told Fred that
        “it still isn’t really in place yet.” Fred explained that he wanted to
        know when it would be ready because he had “business” in Or-
        lando. After that call, Edgecombe and Morley spoke twice on the
        phone, once at 10:06 a.m. and again at 10:13 a.m. A minute after
        Edgecombe’s second call with Morley, Edgecombe called Fred
        again and told him he would send him “straight” and “directly” to
        the person with the cocaine.
                On the day of the August 6 deal, Edgecombe shared with
        Morley the address of the Bass Pro Shops. In addition, a few days
        before the August 6 drug deal, Edgecombe sent Morley two cryptic
        text messages: “I want you ride with me to deal with something
        also make yourself available,” and “whenever i call you i want ride
        with me.” In Duenas, we found similar messages to be a relevant
        indicator of the defendant’s knowledge. 891 F.3d at 1335. Specifi-
        cally, the defendant in Duenas texted his girlfriend two days before
        the transaction “that he was ‘going to do a special work,’ which he
        suggested would be lucrative for him.” Id. His girlfriend “re-
        sponded, ‘Good luck. God protect you and guide you,’” which this
        Court found to be an indicator of the defendant’s “knowing as-
        sumption of a palpable risk.” Id. The August 6 messages here are
        similar to those in Duenas. Edgecombe urging Morley to make
        himself available to ride with Edgecombe to deal with something
        whenever Edgecombe called, a few days before the first drug deal,
        could support an inference of Morley’s knowledge of the circum-
        stances. When paired with the communications leading up to, and
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024     Page: 26 of 30




        26                     Opinion of the Court                  22-12988

        on the date of, the September 28 drug deal, the frequency and the
        timing of the calls suggested Morley was a knowing participant.
               Despite Morley’s arguments to the contrary, the circum-
        stantial evidence here went far beyond Morley’s mere presence at
        the scene or his close association with Edgecombe. Morley showed
        up at the designated meeting site, at the designated meeting time,
        minutes after Edgecombe directed him to come. He was entrusted
        with delivering the cocaine, so he was instrumental to the deal. His
        communications with Edgecombe, a knowing participant, were
        frequent and suspiciously timed. In totality, a jury could reasona-
        bly infer Morley’s knowing involvement in the cocaine conspiracy
        on these facts. The trial evidence was thus sufficient to support his
        convictions, and we affirm as to this issue.
                     C.     Deliberate Ignorance Instruction
               Morley also challenges the district court’s decision to pro-
        vide a jury instruction on deliberate ignorance. The district court
        instructed the jury on both actual knowledge and deliberate igno-
        rance because the evidence “equally could be consistent with ac-
        tual knowledge or deliberate ignorance.” The district court
        pointed to Morley’s actions, such as his walking away from the car,
        and the way the drugs were packaged.
                A deliberate ignorance instruction is appropriate when the
        facts “support the inference that the defendant was aware of a high
        probability of the existence of the fact in question and purposely
        contrived to avoid learning all of the facts in order to have a defense
        in the event of a subsequent prosecution.” United States v. Rivera,
USCA11 Case: 22-12988     Document: 50-1     Date Filed: 04/30/2024    Page: 27 of 30




        22-12988              Opinion of the Court                       27

        944 F.2d 1563, 1571 (11th Cir. 1991) (quoting United States v. Al-
        varado, 838 F.2d 311, 314 (9th Cir. 1987)). We have cautioned the
        district courts against instructing juries on deliberate ignorance
        when the evidence only points to either actual knowledge or no
        knowledge on the part of the defendant. Stone, 9 F.3d at 937 (citing
        Rivera, 944 F.2d at 1570–71). But it is not error “when the evidence
        could support both actual knowledge or deliberate ignorance and
        the jury was instructed on both.” United States v. Maitre, 898 F.3d
        1151, 1157 (11th Cir. 2018).
                Morley argues that the evidence only supported an actual-
        knowledge theory and points to our decision in United States v. Pe-
        rez-Tosta, 36 F.3d 1552 (11th Cir. 1994) for support. There, the de-
        fendant had driven a “cocaine-laden” truck to a house and “was
        present while seventy kilograms of cocaine were taken off the truck
        and placed in the bedroom of the house.” Id. at 1565. Because the
        only inference a jury could draw from this evidence was that the
        defendant’s presence during such a large movement of cocaine
        meant that he “had to have been aware of it,” we held that the dis-
        trict court erroneously gave a deliberate ignorance instruction. Id.
               But the facts here are different from Perez-Tosta. Unlike the
        defendant in Perez-Tosta, Morley attempted to distance himself
        from the deal as it took place. Morley received a text message from
        Edgecombe with the address of the Home Depot and, within
        minutes, left his house and drove there with a briefcase containing
        three kilograms of cocaine on his passenger seat. When Morley
        arrived, however, he did not attempt to find Edgecombe. Instead,
USCA11 Case: 22-12988      Document: 50-1      Date Filed: 04/30/2024      Page: 28 of 30




        28                      Opinion of the Court                  22-12988

        he quickly exited his vehicle and walked across the street to a
        Wendy’s restaurant. After realizing that the Wendy’s was closed,
        Morley paced around outside and eventually made his way across
        the street to help a family with car troubles. Consequently, Morley
        was not present when Fred retrieved the three kilograms of cocaine
        from Morley’s car, or when Fred gave Edgecombe the $84,000 for
        that cocaine. These facts supported the alternative inference that
        Morley was aware of a high probability that he had delivered co-
        caine to a drug deal and had been trying to avoid learning all the
        facts in order to have a defense in a subsequent prosecution. Mor-
        ley’s actions therefore warranted the deliberate ignorance instruc-
        tion.
                In any event, the district court instructed the jury that it
        could convict if Morley had actual knowledge or deliberate igno-
        rance. If, as Morley contends, there was insufficient evidence that
        he was deliberately ignorant of the contents of the briefcase, then
        our precedent is clear that the jury must have convicted on the al-
        ternative theory—actual knowledge. See Colston, 4 F.4th at 1192
        (citing Stone, 9 F.3d at 938). Thus, even if the district court erred in
        giving the deliberate ignorance instruction, it was harmless. See id.
        In any event, Morley’s challenge to the jury instruction fails.
                          D.      Safety Valve Reduction
              Finally, Morley argues that the district court erred in its de-
        termination that he was ineligible for a safety valve sentence reduc-
        tion under the First Step Act. See 18 U.S.C. § 3553(f). The district
        court denied Morley a safety valve reduction on two grounds: (1)
USCA11 Case: 22-12988        Document: 50-1        Date Filed: 04/30/2024        Page: 29 of 30




        22-12988                  Opinion of the Court                              29

        Morley did not satisfy § 3553(f)(1) because he had a prior 3-point
        offense and (2) Morley did not satisfy § 3553(f)(5) because his safety
        valve statement was insufficiently truthful and complete. 1 In light
        of the Supreme Court’s recent decision in Pulsifer v. United States,
        144 S. Ct. 718 (2024), the district court’s first basis for denying safety
        valve relief was correct.
                At the time of sentencing, there were competing interpreta-
        tions as to whether § 3553(f)(1) was conjunctive or disjunctive. Af-
        ter noting that the issue was “still not settled by the Eleventh Cir-
        cuit,” the district court landed on the disjunctive side of the debate
        and based its first ground for denying safety valve relief on that
        finding. Shortly after Morley was sentenced, this Court released its
        en banc decision in United States v. Garcon, 54 F.4th 1274 (11th Cir.
        2022) (en banc), abrogated by Pulsifer, 144 S. Ct. 718. Vacating a prior
        panel decision that reached the opposite conclusion, our en banc
        Court determined that § 3553(f)(1) was “conjunctive” such that de-
        fendants were only disqualified from safety valve relief due to prior
        convictions if they had all of the criminal history features under
        subsection (f)(1). Id. at 1276.
                On appeal, Morley argued that Garcon invalidated the dis-
        trict court’s first basis for denying safety valve relief and, as to the
        second basis, that the district court clearly erred in finding that he
        failed to satisfy § 3553(f)(5). The government conceded that, after

        1 The relevant statutory provisions, along with the conjunctive versus disjunc-

        tive interpretative divide, are detailed in the Factual & Procedural Back-
        ground.
USCA11 Case: 22-12988      Document: 50-1       Date Filed: 04/30/2024      Page: 30 of 30




        30                      Opinion of the Court                   22-12988

        Garcon, the district court’s first basis for denying safety valve relief
        would have been incorrect. However, the government argued that
        we should affirm on the district court’s alternative rationale that
        Morley’s safety-valve statement was insufficient under § 3553(f)(5).
        Therefore, the only issue that we would have needed to consider
        is whether the district court erred in its § 3553(f)(5) determination.
        We only needed to reach that argument, however, if Morley was
        otherwise eligible for the safety valve reduction. But the Supreme
        Court’s recent decision in Pulsifer expressly abrogated our decision
        in Garcon and held that a defendant who has any of the three crim-
        inal-history components under § 3553(f)(1) is disqualified from
        safety valve sentencing relief. 144 S. Ct. at 737.
               It is undisputed in this appeal that Morley fails to satisfy §
        3553(f)(1)(B) because he has a prior three-point offense—conspir-
        acy to import 100 kilograms or more of marijuana. Therefore,
        Morley is ineligible for the safety valve reduction in light of Pulsifer.
        We thus affirm the district court’s denial of Morley’s request for a
        reduced sentence.
                                 IV.     CONCLUSION
                 For these reasons, we affirm Morley’s convictions and sen-
        tence.
                 AFFIRMED.

```

---

## GROUP: content/cases/United States v. Morton.md  (`case`, 4 assertions)

### content_page

```
---
title: "United States v. Morton"
type: case
citation: ""
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, Fifth Circuit"
court_level: coa
circuit: 5th
year: 2022
date_decided: 2022-08-23
docket: 19-10842
authority_weight: "Binding in-circuit — 5th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2022-08-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Morton
  varies_by_point: false
  scope_note: "En banc; resolved on the good-faith exception."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/7859188/united-states-v-morton/"
  cluster_id: 7859188
  opinion_id: 7803054
  identity_checked: false
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Recent development (role-based)"
related: ["[[Riley v. California]]", "[[Carpenter v. United States]]", "[[United States v. Leon]]"]
aliases: ["United States v. Morton (5th Cir. 2022)", "United States v. Morton (en banc)"]
tags: ["case", "fourth-amendment", "plain-view", "digital-searches", "cell-phone", "good-faith-exception", "fifth-circuit"]
holding: "En banc 5th Circuit (resolving on good-faith grounds) discusses the digital general-warrant problem and flags, in concurrence, that the…"
lake:
  record_id: United States v. Morton
  status: under_review
  projected_at: 2026-07-09
---

# United States v. Morton

*46 F.4th 331 (5th Cir. 2022)* · U.S. Court of Appeals, Fifth Circuit (en banc) · **Binding in-circuit — 5th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating Morton, officers obtained warrants to search his cell phones in a drug case. While executing the warrants on the phones' photographs, they found images that appeared to be child pornography. Morton moved to suppress the images, arguing the affidavits did not establish probable cause to search his photographs. Sitting [[Reading and Citing Cases#en-banc|en banc]], the Fifth Circuit resolved the case on the [[The Good-Faith Exception|good-faith exception]] to the exclusionary rule.

## Issue
Whether the images recovered from Morton's phones must be suppressed, or whether the officers' good-faith reliance on the issuing judge's warrants brought the evidence within the [[The Good-Faith Exception|good-faith exception]].

## Rule
The [[Reading and Citing Cases#en-banc|en banc]] court resolved the case on good faith and expressly declined to reach the underlying Fourth Amendment question: "We do not decide if the state judge should have authorized full searches of the phones based on these affidavits. We decide only that the officers acted in good faith when relying on the judge's decision to issue the warrants." — *United States v. Morton*, 46 F.4th 331 (5th Cir. 2022) (en banc) (slip op., at 13). ^pin-op13

Judges concurring in the judgment wrote separately to flag the unresolved digital-search problem the majority left open — that the [[Plain View Doctrine|plain-view doctrine]] may need adaptation for data outside a warrant's scope: it "would be unsurprising if the Court, again acknowledging the need to adapt rules constructed for the physical world to the reality of the digital world, recognized an exception to another longstanding Fourth Amendment doctrine, this time plain view." — *Id.* (slip op., at [16](https://www.courtlistener.com/opinion/7859188/united-states-v-morton/#:~:text=would%20be%20unsurprising%20if%20the)) (opinion concurring in the judgment). ^pin-op16

## Application
The [[Reading and Citing Cases#en-banc|en banc]] court concluded that the warrant affidavits were borderline rather than bare bones, so the officers' reliance on the judge's warrants was objectively reasonable and the [[The Good-Faith Exception|good-faith exception]] applied. The court therefore affirmed admission of the images without deciding whether the warrants in fact established probable cause to search Morton's photographs. The separate opinion concurring in the judgment used the case to identify — but not resolve — whether the [[Plain View Doctrine|plain-view doctrine]] should be limited for nonresponsive digital data, the reason this decision is tracked on the plain-view page.

## Conclusion
Sitting [[Reading and Citing Cases#en-banc|en banc]], the Fifth Circuit held the [[The Good-Faith Exception|good-faith exception]] applied and affirmed the denial of suppression; it expressly declined to decide whether the warrants were overbroad as to the phones' photographs.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 5th Cir.** (en banc).
- No negative treatment. *Morton*'s holding rests on the [[The Good-Faith Exception|good-faith exception]] ([[United States v. Leon]]); its relevance to the [[Plain View Doctrine|plain-view doctrine]] lies in the separate opinion flagging the open digital-search question after [[Riley v. California]] and [[Carpenter v. United States]].

## Appears on
- [[Plain View Doctrine]] — *Recent development (role-based)*

## Sources
- *United States v. Morton*, 46 F.4th 331 (5th Cir. 2022) (en banc) — https://www.courtlistener.com/opinion/7859188/united-states-v-morton/ — pinpoints given as slip-opinion pages (CourtListener carries the slip opinion; cluster 7859188 → opinion 7803054).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d32b6687453eb4c6", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "En banc 5th Circuit (resolving on good-faith grounds) discusses the digital general-warrant problem and flags, in concurrence, that the…", "title": "United States v. Morton"}}
{"assertion_id": "e4a45cbfa350a5f5", "dimension": "support", "kind": "home_role", "locator": {"home": "Plain View Doctrine"}, "payload": {"home": "Plain View Doctrine", "role": "Recent development (role-based)", "title": "United States v. Morton"}}
{"assertion_id": "51fba81d8130ba99", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2022-08-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Morton", "field_i_validity": "good_law", "scope_note": "En banc; resolved on the good-faith exception.", "title": "United States v. Morton", "varies_by_point": "false"}}
{"assertion_id": "d62a6775576f0d98", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 5th Cir.", "title": "United States v. Morton"}}
```

### lake record — United States v. Morton

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Morton",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Morton",
    "case_name_short": "Morton",
    "case_name_full": "",
    "input_case_name": "United States v. Morton",
    "court": "U.S. Court of Appeals, Fifth Circuit",
    "court_id": "ca5",
    "court_level": "coa",
    "circuit": "5th",
    "state": null,
    "date_decided": "2022-08-23",
    "year": 2022,
    "docket": "19-10842",
    "cluster_id": 7859188,
    "lead_opinion_id": 7803054,
    "sibling_ids": [
      7803054
    ],
    "absolute_url": "/opinion/7859188/united-states-v-morton/",
    "identity_method": "name+docket",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
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
  "pinpoints": [
    {
      "id": "pin-op13",
      "page": null,
      "quote": "--- # United States v. Morton *46 F.4th 331 (5th Cir. 2022)* \u00b7 U.S. Court of Appeals, Fifth Circuit (en banc) \u00b7 **Binding in-circuit \u2014 5th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigating Morton, officers obtained warrants to search his cell phones in a drug case. While executing the warrants on the phones' photographs, they found images that appeared to be child pornography. Morton moved to suppress the images, arguing the affidavits did not establish probable cause to search his photographs. Sitting en banc, the Fifth Circuit resolved the case on the good-faith exception to the exclusionary rule. ## Issue Whether the images recovered from Morton's phones must be suppressed, or whether the officers' good-faith reliance on the issuing judge's warrants brought the evidence within the good-faith exception. ## Rule The en banc court resolved the case on good faith and expressly declined to reach the underlying Fourth Amendment question:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op16",
      "page": null,
      "quote": "would be unsurprising if the Court, again acknowledging the need to adapt rules constructed for the physical world to the reality of the digital world, recognized an exception to another longstanding Fourth Amendment doctrine, this time plain view.",
      "star_marker": "11",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 30555,
      "fragment": "#:~:text=would%20be%20unsurprising%20if%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2022-08-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Morton",
    "varies_by_point": false,
    "scope_note": "En banc; resolved on the good-faith exception.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(7803054) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca5)",
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
        "query": "cites:(7803054)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(7803054)",
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
    "complete_query": "cites:(7803054)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 7803054,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-morton.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 7803054,
        "cited_id": 6544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 8255,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 46216,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 47945,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 50941,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 145918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 172511,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 183984,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 450602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 480195,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 595515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 765254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 802237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 1189236,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 2310827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 2673989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 4251099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 4287285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 4649311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 4693288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 4699658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 6454865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 6534035,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 7263677,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9417418,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9421690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9422845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9422971,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9423434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9423895,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9424493,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9426173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9428782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9429232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9429766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9434104,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9434949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9469573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9498985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9499327,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9876158,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 7803054,
        "cited_id": 9889044,
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
    "date_created": "2026-07-06T01:52:16Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: no_official_class_citation",
      "legacy treatment migrated: good -> good_law",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:53:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:53:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T13:39:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:53:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Morton

```
Case: 19-10842        Document: 00516443952             Page: 1      Date Filed: 08/23/2022




               United States Court of Appeals
                    for the Fifth Circuit                                         United States Court of Appeals
                                                                                           Fifth Circuit

                                                                                         FILED
                                                                                   August 22, 2022
                                        No. 19-10842
                                                                                    Lyle W. Cayce
                                                                                         Clerk
   United States of America,

                                                                      Plaintiff—Appellee,

                                            versus

   Brian Matthew Morton,

                                                                  Defendant—Appellant.


                     Appeal from the United States District Court
                         for the Northern District of Texas
                               USDC No. 4:19-CR-17-1


   Before Richman, Chief Judge, and Jolly, Jones, Smith, Stewart,
   Dennis, Elrod, Southwick, Haynes, Graves, Higginson,
   Costa, Willett, Ho, Duncan, Engelhardt, Oldham and
   Wilson, Circuit Judges.*
   Gregg Costa, Circuit Judge, joined by Richman, Chief Judge, and
   Jones, Smith, Stewart, Southwick, Haynes, Ho, Duncan,
   Engelhardt, Oldham, and Wilson, Circuit Judges:
           State troopers arrested Brian Morton after finding drugs in his car
   during a traffic stop. Morton also had three cellphones in the car. A state


           *
             Judge Jolly chooses not to dissent or to join Judge Graves’s dissent. He chooses
   to stand by the initial panel opinion.
Case: 19-10842      Document: 00516443952           Page: 2   Date Filed: 08/23/2022




                                     No. 19-10842


   judge later signed warrants authorizing searches of the phones for evidence
   of drug crime. The warrants allowed law enforcement to look at photos on
   the phones. When doing so, troopers discovered photos that appeared to be
   child pornography. This discovery led to a second set of search warrants.
   The ensuing forensic examination of the phones revealed almost 20,000
   images of child pornography. This federal prosecution for receipt of child
   pornography followed.
          Even though search warrants authorized everything law enforcement
   did when searching the cell phones, Morton argues the evidence discovered
   during those searches should be suppressed. We disagree because law
   enforcement is usually entitled to rely on warrants, and none of the
   exceptions that undermine good-faith reliance on a judge’s authorization
   applies.
                                          I
          Shortly after midnight, state trooper Burt Blue pulled over Morton’s
   van on Interstate 20 about fifty miles west of Fort Worth. After approaching
   the driver’s side door, Blue smelled marijuana. Morton eventually admitted
   he had marijuana in the van. Blue then searched Morton and found an Advil
   bottle in his right pocket. The bottle contained several different colored pills
   that Morton admitted were ecstasy. Morton was arrested.
          Blue and another trooper searched the van. Inside a plastic container
   wrapped in tape they discovered two plastic bags, one of which contained a
   small amount of marijuana. They also found a glass pipe with marijuana. In
   addition to the drug evidence, the troopers discovered approximately 100
   pairs of women’s underwear, a number of sex toys, and lubricant. A backpack
   with children’s school supplies was also inside the van. A lollipop was inside
   a cupholder. Based on what they found in the van, the troopers were
   concerned Morton was a sexual predator.




                                          2
Case: 19-10842      Document: 00516443952           Page: 3   Date Filed: 08/23/2022




                                     No. 19-10842


          The troopers also seized three cellphones during the search of the van.
   A few days after Morton’s arrest, Blue applied for search warrants for the
   three phones. The search warrants sought evidence of drug possession and
   dealing.
          In the affidavits he submitted in support of the warrants, Blue
   recounted the traffic stop and the drug evidence discovered in the van and on
   Morton. He also explained why, based on his experience, he believed it likely
   that the cellphones contained evidence of illegal drug activity. People often
   communicate via cellphone to arrange drug transactions. And “criminals
   often take photographs of co-conspirators as well as illicit drugs and currency
   derived from the sale of illicit drugs.”
          A state district judge concluded that probable cause existed for the
   searches and signed the three warrants. Each warrant allowed troopers to
   search for various items on the phones including “photographs, digital
   images, or multimedia files in furtherance of narcotics trafficking or
   possession.”
          While searching the phones, Blue and a Department of Public Safety
   agent saw images they believed were child pornography. They stopped
   searching and sought new warrants seeking evidence of child pornography.
   The same state district judge issued the new warrants. The forensic search
   of the phones that followed located 19,270 images of child pornography on
   the three phones.
          A federal grand jury charged Morton with receipt of child
   pornography. Morton moved to suppress the pornographic images found on
   the phones. He argued that probable cause did not support the initial
   warrants allowing the phone searches. The good-faith doctrine did not apply,
   he continued, because the affidavits were too “general in nature” to tie the
   phones to drug activity. He also briefly contended that the search of the




                                          3
Case: 19-10842     Document: 00516443952            Page: 4    Date Filed: 08/23/2022




                                     No. 19-10842


   phone for drug evidence was pretextual because the troopers were really
   concerned that Morton might have committed sex crimes.
          The district court refused to suppress the evidence. It concluded that
   the good-faith exception to the suppression rule applied.
          After losing his suppression motion, Morton entered a conditional
   guilty plea that allowed him to challenge the searches on appeal.
          Morton’s appeal initially succeeded. A panel of our court concluded
   that, although the “affidavits successfully establish probable cause to search
   Morton’s contacts, call logs, and text messages for evidence of drug
   possession,” United States v. Morton, 984 F.3d 421, 427 (5th Cir. 2021), they
   do not establish probable cause “that the photographs on Morton’s phones
   would contain evidence pertinent to [that] crime,” id. at 428. The panel also
   held that the good-faith exception did not apply because reasonable officers
   should “have been aware that searching the digital images on Morton’s
   phone—allegedly for drug-trafficking-related evidence—was unsupported
   by probable cause.” Id. at 430.
          Our full court vacated that decision and agreed to hear this case en
   banc. See United States v. Morton, 996 F.3d 754 (5th Cir. 2021).
                                          II
          Riley v. California, one of the recent Supreme Court cases applying the
   Fourth Amendment to modern technology, held that the search of a
   cellphone incident to arrest requires a warrant. 574 U.S. 373 (2014). Morton
   and supporting amici view this case as a follow-on that allows us to flesh out
   when probable cause exists to believe that certain applications on a cellphone
   contain incriminating evidence. They argue that Riley’s warrant requirement
   will be a mere formality if officers can search an entire phone based on




                                          4
Case: 19-10842        Document: 00516443952              Page: 5      Date Filed: 08/23/2022




                                         No. 19-10842


   nothing more than the fact that criminals sometimes use phones to conduct
   their illicit activity.
           Despite the invitation to treat this as another difficult case addressing
   how “the degree of privacy secured to citizens by the Fourth Amendment”
   is affected “by the advance of modern technology,” Kyllo v. United States,
   533 U.S. 27, 33–34 (2001), a longstanding rule resolves the case: Evidence
   should not be suppressed when law enforcement obtained it in good-faith
   reliance on a warrant. See United States v. Leon, 468 U.S. 897 (1984).1
           The good-faith rule flows from two central features of modern Fourth
   Amendment jurisprudence: the warrant requirement and the suppression
   remedy. The Supreme Court has held that a warrant is generally required for
   certain searches, most notably searches of the home and most recently
   searches of cellphones incident to arrest. See Riley, 574 U.S. at 403; Brigham
   City v. Stuart, 547 U.S. 398, 403 (2006) (noting that “searches and seizures
   inside a home without a warrant are presumptively unreasonable” (internal
   quotation omitted)). Behind the warrant requirement is the idea that the
   “inferences which reasonable men draw from evidence” to decide if probable
   cause exists should “be drawn by a neutral and detached magistrate instead
   of being judged by the officer engaged in the often competitive enterprise of
   ferreting out crime.” Johnson v. United States, 333 U.S. 10, 14 (1948)
   (Jackson, J.). Although obtaining a warrant from that neutral judge may



           1
             We recognize that it will “stunt the development of Fourth Amendment law” if
   courts too often avoid the underlying constitutional question and deny suppression motions
   based on the good-faith rule. See Davis v. United States, 564 U.S. 229, 245–46 (2011)
   (summarizing this argument the defendant advanced); cf. Pearson v. Callahan, 555 U.S. 223
   236 (2009) (giving courts discretion to rule only on the “clearly established” inquiry for
   qualified immunity but recognizing that deciding the underlying constitutional question is
   “often beneficial”). In this instance, however, we conclude that the good-faith rule offers
   the most appropriate resolution by the full court.




                                               5
Case: 19-10842      Document: 00516443952           Page: 6    Date Filed: 08/23/2022




                                     No. 19-10842


   burden law enforcement before it conducts the search, the police obtain a
   benefit after the search. When a court reviews an after-the-fact challenge to
   the search, “the resolution of doubtful or marginal cases . . . should be largely
   determined by the preference to be accorded to warrants.” United States v.
   Ventresca, 380 U.S. 102, 109 (1965). As a result, “[s]earches pursuant to a
   warrant will rarely require any deep inquiry into reasonableness.” Leon, 468
   U.S. at 922 (quoting Illinois v. Gates, 462 U.S. 213, 267 (1983) (White, J.,
   concurring in judgment)).
          To this unwillingness to second guess the magistrate who authorized
   the warrant, the exclusionary rule adds another component. As a judicially-
   created remedy rather than a constitutional requirement, the exclusionary
   rule is justified by the deterrent effect of suppressing evidence when it was
   obtained unlawfully. Id. at 906. A key consideration in deciding when
   suppression will deter is whether “law enforcement officers have acted in
   objective good faith.” Id. at 908. The need to punish police conduct and
   thus deter future violations via suppression “assumes that the police have
   engaged in willful, or at the very least negligent, conduct.” Id. at 919 (quoting
   United States v. Peltier, 422 U.S. 531, 539 (1975)). The exclusionary rule is
   not aimed at “punish[ing] the errors of judges and magistrates” who issue
   warrants. Id. at 916.
          Deference to the judge issuing the warrant and the exclusionary rule’s
   focus on deterring police misconduct results in the good-faith exception to
   the suppression remedy: A “‘warrant issued by a magistrate normally
   suffices to establish’ that a law enforcement officer has ‘acted in good faith
   in conducting a search.’” Id. at 922 (quoting United States v. Ross, 456 U.S.
   798, 832 n.32 (1982)).
          Normally, but not always.        The Supreme Court identified four
   situations when “a reasonably well trained officer would have known that the




                                          6
Case: 19-10842         Document: 00516443952               Page: 7      Date Filed: 08/23/2022




                                          No. 19-10842


   search was illegal despite the magistrate’s authorization.” Id. at 922 n.23.
   Reliance on a warrant is unreasonable when: 1) the magistrate issued it based
   on information the affiant knew was false or should have known was false but
   for reckless disregard of the truth; 2) the magistrate wholly abandoned the
   judicial role; 3) the warrant is based on an affidavit so lacking in probable
   cause as to render belief in its existence unreasonable; and 4) the warrant is
   facially deficient in particularizing the place to be searched or things to be
   seized. Id. at 923; see also United States v. Triplett, 684 F.3d 500, 504 (5th Cir.
   2012).
                                                III
            Morton principally tries to defeat good faith by invoking the third
   exception, which involves what are commonly known as “bare bones”
   affidavits.2 “‘Bare bones’ affidavits contain wholly conclusory statements,
   which lack the facts and circumstances from which a magistrate can
   independently determine probable cause.” United States v. Satterwhite, 980
   F.2d 317, 321 (5th Cir. 1992).




            2
             Morton also invokes the first exception that applies when law enforcement
   misleads the magistrate with false information in the affidavit. We succinctly address this
   argument because the full court is unanimous in rejecting it and Morton may not have
   adequately raised it in district court.
           The alleged falsehood is keeping from the magistrate that the affiant’s motive was
   not obtaining evidence of drug crime but investigating suspicions that Morton was a sexual
   predator. In other words, Morton is arguing that the reason for obtaining the warrant was
   pretextual. Even if Morton could prove this motive, it would not matter. The Supreme
   Court has repeatedly held that the Fourth Amendment inquiry, including the existence of
   probable cause, is objective. See, e.g., Brigham City, 547 U.S. at 404–05 (2006); Whren v.
   United States, 517 U.S. 806, 813 (1996); see also United States v. McKinnon, 681 F.3d 203,
   210 (5th Cir. 2012) (explaining that the officer’s motive in searching a vehicle did not
   matter). It is telling that Morton’s primary authority on this issue is a vacated opinion. See
   United States v. Pope, 452 F.3d 338, vacated by 467 F.3d 912 (5th Cir. 2006).




                                                 7
Case: 19-10842      Document: 00516443952            Page: 8   Date Filed: 08/23/2022




                                     No. 19-10842


          A look at some bare-bones affidavits from Supreme Court cases shows
   just how bare they are. One affidavit, from the Prohibition Era, said nothing
   more than that the agent “has cause to suspect and does believe that certain
   merchandise . . . has otherwise been brought into the United States contrary
   to law, and that said merchandise is now deposited and contained within”
   the defendant’s home. Nathanson v. United States, 290 U.S. 41, 44 (1933).
   Another affidavit, this one supporting an arrest warrant, said only that, on a
   certain day, the defendant “did receive, conceal, etc., narcotic drugs, to-wit:
   heroin hydrochloride with knowledge of unlawful importation” and that the
   affiant “believes” certain people “are material witnesses in relation to this
   charge.” Giordenello v. United States, 357 U.S. 480, 481 (1958). Similarly,
   the allegations supporting an arrest warrant were bare bones when the only
   information was that “defendants did then and there unlawfully break and
   enter a locked and sealed building.” Whiteley v. Warden, 401 U.S. 560, 563
   (1971). Lastly, Houston police officers obtained a search warrant based only
   on their statement that they “received reliable information from a credible
   person and do believe that [drugs] are being kept at the above described
   premises for the purpose of sale and use contrary to the provisions of the
   law.” Aguilar v. Texas, 378 U.S. 108, 109 (1964). These affidavits do not
   detail any facts, they allege only conclusions.
          Also consider affidavits we have found to be bare-boned. In what we
   described as a “textbook example of a facially invalid, ‘barebones’ affidavit,”
   the officer listed just the defendant’s “biographical and contact information”
   and then stated “nothing more than the charged offense, accompanied by a
   conclusory statement” that the defendant committed that crime. Spencer v.
   Staton, 489 F.3d 658, 661–62 (5th Cir. 2007), withdrawn in part on reh’g (July
   26, 2007). In another case, an officer obtained a warrant to search a motel
   room based on an affidavit stating nothing more than that the officer
   “received information from a confidential informant” who was known to him




                                          8
Case: 19-10842      Document: 00516443952           Page: 9    Date Filed: 08/23/2022




                                     No. 19-10842


   and who had “provided information in the past that ha[d] led to arrest and
   convictions.” United States v. Barrington, 806 F.2d 529, 531 (5th Cir. 1986).
   As these cases illustrate, bare-bones affidavits contain “wholly conclusory”
   statements such as “the affiant ‘has cause to suspect and does believe’ or
   ‘[has] received reliable information from a credible person and [does]
   believe.’” United States v. Pope, 467 F.3d 912, 920 (5th Cir. 2006) (internal
   quotations omitted).
          The affidavits used to search Morton’s phones are not of this genre;
   they have some meat on the bones. Each is over three pages and fully details
   the facts surrounding Morton’s arrest and the discovery of drugs and his
   phones. They explain where the marijuana and glass pipe were discovered,
   the number (16) and location of the ecstasy pills, and the affiant’s knowledge
   that cellphones are used for receipt and delivery of illegal narcotics. In
   support of the request to search for photos on the phones, the affiant explains
   he “knows through training and experience that criminals often take
   photographs of co-conspirators as well as illicit drugs and currency derived
   the sale of illicit drugs.” Whatever one might conclude in hindsight about
   the strength of the evidence it recounts, the affidavit is not “wholly
   conclusory.” Satterwhite, 980 F.2d at 321.
          The affidavits, then, put all the relevant “facts and circumstances”
   before the state judge, allowing him to “independently determine” if the
   notoriously fuzzy probable-cause standard had been met. See id.; see also
   Gates, 462 U.S. at 232 (“[P]robable cause is a fluid concept—turning on the
   assessment of probabilities in particular factual contexts—not readily, or
   even usefully, reduced to a neat set of legal rules.”). In other words, the judge
   made a judgment call. Judgment calls in close cases are precisely when the
   good-faith rule prevents suppression based on after-the-fact reassessment of
   a probable-cause determination. Leon, 468 U.S. at 914 (“Reasonable minds
   frequently may differ on the question whether a particular affidavit



                                          9
Case: 19-10842        Document: 00516443952              Page: 10       Date Filed: 08/23/2022




                                          No. 19-10842


   establishes probable cause, and we have thus concluded that the preference
   for warrants is most appropriately effectuated by according ‘great deference’
   to a magistrate’s determination.” (quoting Spinelli v. United States, 393 U.S.
   410, 419 (1969))).
           Although he invokes the bare-bones exception, Morton does not
   confront the caselaw showing it applies to affidavits that are wholly
   conclusory. He instead mostly challenges the probable-cause determination
   assessment itself, contending that the facts “merely establish[ed] probable
   cause for a user-quantity drug possession arrest and not probable cause to
   search the entire communication and photographic contents of [his]
   phones.” Drug possessors, he points out, are less likely to use phones for
   drug activity than are dealers. He contends it would gut Riley if the linking of
   criminal activity to cellphones can be based on nothing more than an officer’s
   experience that certain offenders often use cellphones in connection with
   their crimes. But this is not such a case. Morton had multiple phones in his
   car along with the drugs, which our court and others have recognized can
   indicate that the phones are being used for criminal activity.3 See United
   States v. Bams, 858 F.3d 937, 945 (5th Cir. 2017); United States v. Lindsay, 3
   F.4th 32, 40 (1st Cir. 2021); United States v. Peterson, 2019 WL 1793138, at
   *11–12 (E.D. Va. Apr. 24, 2019); see also United States v. Eggerson, 999 F.3d
   1121, 1127 (8th Cir. 2021) (“It would be unreasonable and impractical to
   demand that judges evaluating probable cause must turn a blind eye to the
   virtual certainty that drug dealers use cell phones.”).




           3
            The concurring opinion points out that the affidavits did not identify the existence
   of three phones as a reason why the troopers suspected Morton of dealing drugs. But
   together the affidavits placed the fact of Morton’s multiple phones before the state judge,
   who is charged with making an objective evaluation of probable cause.




                                                10
Case: 19-10842        Document: 00516443952           Page: 11    Date Filed: 08/23/2022




                                       No. 19-10842


          It is a close call whether the evidence recounted in the affidavits
   established probable cause for drug trafficking as opposed to drug possession.
   And if the evidence indicated only possession, then it is another close call
   whether there was probable cause to believe that evidence of drug possession
   would be found on the phones. But as we have emphasized, on close calls
   second guessing the issuing judge is not a basis for excluding evidence.
          Viewed in their entirety, the affidavits supporting the warrants are far
   from bare bones. It thus was reasonable to rely on the warrants and search
   the phones.
          For most of this case, Morton’s argument was the one we have just
   addressed: that searching any part of his phones was unjustified because the
   affidavits establish probable cause only for drug possession and not the
   trafficking that is more logically tied to phones. But even the panel originally
   hearing this appeal did not accept that argument despite holding that the
   photos should have been suppressed. The panel recognized probable cause
   existed to “search Morton’s contacts, call logs, and text messages” on his
   phone, just not the photos. 984 F.3d at 427–28; id. at 431 (concluding that
   “the magistrate did not have a substantial basis for determining that probable
   cause existed to extend the search to the photographs on the cellphones”).
   Morton now runs with this theory that good-faith should be “analyzed
   separately” for each area to be searched. Because he did not make this claim
   in the district court or in his original appellate brief, it is forfeited, and we are
   not deciding it.
          Even if we could consider Morton’s new argument advocating a
   piecemeal analysis, it would not change our holding that the good-faith rule
   applies. At least one other court has taken the approach of the original panel
   in this case and analyzed whether an affidavit is bare bones for particular
   items to be searched. See Burns v. United States, 235 A.3d 758, 774 (D.C.




                                            11
Case: 19-10842     Document: 00516443952            Page: 12   Date Filed: 08/23/2022




                                     No. 19-10842


   2020) (“The affidavits were thus classic ‘bare bones’ statements as to
   everything on Mr. Burns’s phones for which Detective Littlejohn made a
   claim of probable cause beyond three narrow categories of data for which the
   affidavits made proper factual showings.”). Our precedent takes a different
   approach. When a defendant moved to suppress evidence obtained under a
   warrant that authorized the seizure of “twenty-six categories of evidence,
   primarily written and electronic documents,” our good-faith inquiry did not
   parse probable cause for each category. See United States v. Cherna, 184 F.3d
   403, 406 (5th Cir. 1999). We instead focused on whether the affidavit as a
   whole was bare bones, while “keep[ing] in mind that it is more difficult to
   demonstrate probable cause for an ‘all records’ search of a residence than for
   other searches.” Id. at 409. That is, the scope of a warrant may influence
   whether it is bare bones. An affidavit that is not bare bones for a limited
   search could be bare when supporting a broader search. Keeping the focus
   on the entirety of the affidavit as Cherna does is the traditional bare-bones
   inquiry, see, e.g, Leon, 468 U.S. at 926 (referring to a “‘bare bones’ affidavit”
   not parts of an affidavit), and consistent with the ultimate question whether
   an officer would know the affidavit is “so lacking in probable cause as to
   render belief in its existence unreasonable” despite a judge’s finding that
   probable cause existed, id. at 923.
          Viewing the entire affidavit against the broad phone search it
   authorized, it is borderline rather than bare bones. And even if our caselaw
   allowed a photographs-only inquiry and Morton preserved that argument, we
   would still not characterize the evidence supporting that request as “wholly
   conclusory.” Cf. United States v. Burgess, 576 F.3d 1078 (10th Cir. 2009)
   (recognizing that it was reasonable to search a computer for “trophy photos”
   of drug activity based on not much more evidence than exists here).
          The officers relied in good faith on the warrants the state judge issued.
   On finding images that appeared to be child pornography, they went back to



                                          12
Case: 19-10842       Document: 00516443952              Page: 13      Date Filed: 08/23/2022




                                         No. 19-10842


   the judge for additional warrants (Morton does not challenge how the
   searches were conducted).           We see no unreasonable law enforcement
   conduct that warrants suppression of the evidence the searches discovered.
                                             ***
           We do not decide if the state judge should have authorized full
   searches of the phones based on these affidavits. We decide only that the
   officers acted in good faith when relying on the judge’s decision to issue the
   warrants. This ruling hardly nullifies Riley as Morton, amici, and the dissent
   suggest. Before Riley, police could have searched Morton’s phones on the
   spot after arresting him. See United States v. Finley, 477 F.3d 250, 259–60
   (5th Cir. 2007), overruled by Riley, 573 U.S. at 373. Because of Riley, the
   officers had to obtain warrants. For better or worse, the warrant requirement
   and good-faith rule make the judge presented with the warrant application
   the central guardian of Fourth Amendment rights.4 That has long been true
   when officers seek to search a home; Riley makes it true for searches of
   cellphones incident to arrest.
           The judgment is AFFIRMED.




           4
            The role of the judge who must authorize a warrant is absent from the dissent’s
   recounting of how officers might be able to search cellphones after “find[ing] evidence of
   small quantities of illicit drugs for personal use during an automobile stop.” Dissenting
   Op. 4–5.




                                              13
Case: 19-10842        Document: 00516443952         Page: 14    Date Filed: 08/23/2022




                                     No. 19-10842


   Stephen A. Higginson, Circuit Judge, with whom Elrod and
   Willett, Circuit Judges, join, and with whom Ho and Wilson, Circuit
   Judges, join as to Part II, concurring in the judgment:
          I agree with the majority that the affidavit supporting the warrants in
   this case was “borderline rather than bare bones,” and, therefore, that the
   good faith exception applies. United States v. Satterwhite, 980 F.2d 317, 321
   (5th Cir. 1992).
                                           I.
          Because we can decide this case on the good faith exception, the
   majority opinion appropriately declines to address whether there was
   probable cause to search Morton’s cell phone. I write separately to address
   the majority’s response to Morton’s argument that a finding of probable
   cause here would conflict with the reasoning, though not necessarily the
   holding, of Riley v. California, 573 U.S. 373 (2014), in which the Supreme
   Court held that police officers must obtain a warrant before searching the
   contents of an arrestee’s cell phone, rather than conducting a search of the
   cell phone incident to arrest.
          The only facts in the affidavit to support probable cause for a search
   of Morton’s cell phone were that: (1) he possessed a user-quantity of drugs,
   (2) he simultaneously possessed a cell phone, and (3) the officer “kn[ew]
   through training and experience” that individuals, including those
   possessing illicit drugs, use their cell phones to communicate. If these three
   facts are sufficient to support probable cause for the search here, then any
   time an officer finds drugs (or other contraband for that matter) on a person
   or in a vehicle, there is probable cause to search the entire contents of a nearby
   cell phone.
          Of course, Riley requires that officers first get a warrant, 573 U.S. at
   403, but if the fact that the arrestee was carrying a cell phone at the time of




                                          14
Case: 19-10842        Document: 00516443952              Page: 15       Date Filed: 08/23/2022




                                          No. 19-10842


   arrest is sufficient to support probable cause for a search, then the warrant
   requirement is merely a paperwork requirement. It cannot be that Riley’s
   holding is so hollow.1
                                               II.
           The heightened privacy interest that Riley recognized an arrestee has
   in the contents of their cell phone stems in part from the quantitative and
   qualitative differences between the data stored on a cell phone and any
   “other objects that might be kept on an arrestee’s person.” Id. at 393. Cell
   phones contain an enormous amount of personal information dating back
   months or years, including data that has no physical equivalent, like browser
   history or geolocation information. Id. at 394-96. Therein lies the problem
   with a cell phone search premised solely on the simultaneous possession of
   drugs and a phone. It is not merely the lack of probable cause that evidence
   of drug possession or trafficking would be found on the phone, but also that
   with such a meager showing, officers would gain unfettered access to all of
   “the privacies of life.” Id. at 403 (quoting Boyd v. United States, 116 U.S. 616,
   630 (1886)).
           The original panel opinion in this case presented one potential
   solution to this problem by requiring probable cause for each category of data
   to be searched. United States v. Morton, 984 F.3d 421, 425-26 (5th Cir. 2021).
   This approach runs into practical problems, including the fact that



           1
             The majority’s response to the contention that “it would gut Riley if the linking
   of criminal activity to cellphones can be based on nothing more than an officer’s experience
   that certain offenders often use cellphones in connection with their crimes” is that, here,
   there was something more—namely, the presence of multiple cellphones. It is true that we
   have recognized that the presence of multiple phones in a car—when combined with other
   strong evidence—can support a conviction for drug trafficking, United States v. Bams, 858
   F.3d 937, 945 (5th Cir. 2017). But the affidavits here did not mention that multiple phones
   were found in the car, let alone rely on that fact to support probable cause.




                                               15
Case: 19-10842     Document: 00516443952            Page: 16    Date Filed: 08/23/2022




                                     No. 19-10842


   “criminals can—and often do—hide, mislabel, or manipulate files to conceal
   criminal activity.” United States v. Stabile, 633 F.3d 219, 237 (3d Cir. 2011).
          Another approach, proposed by a leading Fourth Amendment
   scholar, would impose “use restrictions” on data that is outside the scope of
   the warrant, possibly by limiting application of the plain view doctrine in the
   context of digital searches. See Orin S. Kerr, Executing Warrants for Digital
   Evidence: The Case for Use Restrictions on Nonresponsive Data, 48 Tex. Tech
   L. Rev. 1, 9, 19-20 (2015). At least one state supreme court has adopted a
   use restriction approach, see State v. Mansor, 421 P.3d 323, 344 (Or. 2018),
   and another has suggested that it might do so in the future, Preventative Med.
   Assocs. v. Commonwealth, 992 N.E.2d 257, 274 (Mass. 2013). After Riley and
   Carpenter v. United States, 138 S. Ct. 2206, 2220 (2018), in which the
   Supreme Court held that the third-party doctrine does not apply to cell-site
   location information, it would be unsurprising if the Court, again
   acknowledging the need to adapt rules constructed for the physical world to
   the reality of the digital world, recognized an exception to another
   longstanding Fourth Amendment doctrine, this time plain view. See Kerr,
   supra, at 20; see generally Kyllo v. United States, 533 U.S. 27, 33-34 (2001).
          And there may be still other solutions that have yet to be identified.
   State courts face these dilemmas much more often than we do, and their
   continued innovation in this area—along with the valuable insights of Fourth
   Amendment scholars and those with the necessary technological expertise—
   will undoubtedly aid the lower federal courts and the Supreme Court in
   reaching a solution that protects privacy and the Framers’ conception of
   reasonableness. To my eye, that conception is unlikely to approve plain view
   full access to, and use of, what the Supreme Court has observed is more
   private information than would be contained in an entire home, where plain
   view access has obvious and significant limits. Riley, 573 U.S. at 396-97.




                                          16
Case: 19-10842     Document: 00516443952           Page: 17    Date Filed: 08/23/2022




                                    No. 19-10842


   James E. Graves, Jr., Circuit Judge, joined by Dennis, Circuit Judge,
   dissenting:
          Despite cautionary case law from this court that we “should resist the
   temptation to frequently rest [our] Fourth Amendment decisions on the safe
   haven of the good-faith exception, lest [we] fail to give law enforcement and
   the public the guidance needed to regulate their frequent interactions,” the
   majority avoids dealing with the “close call” question of probable cause.
   United States v. Molina-Isidoro, 884 F.3d 287, 293 (5th Cir. 2018) (Costa, J.,
   specially concurring). We should not fall into this “inflexible practice” that
   the Supreme Court warned against in Leon “of always deciding whether the
   officers’ conduct manifested objective good faith before turning to the
   question whether the Fourth Amendment has been violated.” United States
   v. Leon, 468 U.S. 897, 923 (1984). In failing to analyze this case for probable
   cause, the majority condones the government’s extensive and intrusive
   search of cell phones and its failure to provide any explanation of how those
   particular phones relate to the charged crime. In essence, it insulates officers
   from having to connect the dots between their general knowledge and
   experience—as detailed in a probable cause affidavit—and the basis for that
   specific search warrant. See United States v. Pope, 467 F.3d 912, 920 (5th Cir.
   2006) (disavowing affidavits based on an officer’s general suspicions or
   beliefs as “bare bones”). I dissent.
          First, this case must be viewed against the proper backdrop. Searching
   a cellphone is much more invasive than a self-contained search of a pocket,
   compartment, or bag. As Learned Hand noted, it is “a totally different thing
   to search a man’s pockets and use against him what they contain, from
   ransacking his house for everything which may incriminate him.” Riley v.
   California, 573 U.S. 373, 396 (2014) (citation omitted). “A phone not only
   contains in digital form many sensitive records previously found in the home;
   it also contains a broad array of private information never found in a home in



                                          17
Case: 19-10842     Document: 00516443952            Page: 18   Date Filed: 08/23/2022




                                     No. 19-10842


   any form—unless the phone is.” Id. at 396-97. Here, law enforcement
   conducted a traffic stop that produced evidence of a marginal offense. Then,
   they used this evidence as an excuse to gain unfettered access to a device
   saturated with personal, private information.
          Probable cause exists when “there is a fair probability that contraband
   or evidence of a crime will be found in a particular place.” Illinois v. Gates,
   462 U.S. 213, 238 (1983). We require a “nexus between the [place] to be
   searched and the evidence sought.” United States v. Freeman, 685 F.2d 942,
   949 (5th Cir. 1982) (collecting cases). Here, Morton was charged with simple
   possession based on 16 ecstasy pills, a small bag of marijuana, and a glass pipe.
   Trooper Blue’s affidavit stated that he believed Morton’s phones contained
   evidence of possession of ecstasy and marijuana “and other criminal
   activity.” Notably, Trooper Blue’s affidavit indicates that he already had
   firsthand evidence of Morton’s possession offense. One, he found the drugs
   on Morton. And two, Morton “admitted to . . . the possession of marijuana
   and [e]cstasy.” Morton did not have a large quantity of drugs, a large sum of
   cash, or anything else that would have indicated he was anything more than
   an admitted drug possessor, not a drug dealer.
          However, in an attempt to gain access to Morton’s phones, Trooper
   Blue made sweeping generalizations about “other criminal activity” and cell
   phone use, yet not once did he mention why such evidence could or would
   be on Morton’s phone. Nor did he connect his suspicions to Morton’s simple
   possession offense. Not even in passing. He instead hinged his affidavit on
   general conclusions about cellphones and criminals. As the Supreme Court
   has noted, “[i]t would be a particularly inexperienced or unimaginative law
   enforcement officer who could not come up with several reasons to suppose
   evidence of just about any crime could be found on a cell phone.” Riley, 573
   U.S. at 399. However, such speculation cannot be used to allow “police
   officers unbridled discretion to rummage at will among a person’s private



                                          18
Case: 19-10842     Document: 00516443952            Page: 19   Date Filed: 08/23/2022




                                     No. 19-10842


   effects.” Id. (citation omitted). Trooper Blue’s generalizations lack a nexus
   to the crime of simple possession, and there was no probable cause for the
   warrant to issue.
          For this same reason, the good faith exception does not apply. This
   court has repeatedly held that a nexus is necessary to claim the protection of
   the good faith exception. See, e.g., United States v. Garcia, 27 F.3d 1009, 1014
   (5th Cir. 1994) (noting in the discussion on the officer’s good faith reliance
   that “[t]he affidavit must tend to show some nexus between the [area] to be
   searched and the evidence sought.”); United States v. Brown, 567 F. App’x
   272, 284 (5th Cir. 2014) (unpublished) (including the lack of nexus “between
   [defendant’s] trafficking activities and his residence” among the deficiencies
   in the warrant’s supporting affidavit); United States v. Triplett, 684 F.3d 500,
   506–07 (5th Cir. 2012); United States v. Fields, 72 F.3d 1200, 1214 (5th Cir.
   1996); United States v. Gant, 759 F.2d 484, 488 (5th Cir. 1985); cf. Warden,
   Md. Penitentiary v. Hayden, 387 U.S. 294, 307 (1967) (indicating in the
   context of a seizure of “mere evidence” that “[t]here must, of course, be a
   nexus . . . between the item to be seized and criminal behavior.”).
          Where the affiant claims—without explaining why—he “has cause to
   suspect and does believe” or—without explaining how—he “[has] received
   reliable information from a credible person and [does] believe” that the
   search will result in the discovery of illegal activity, we deem such affidavits
   “bare bones.” Pope, 467 F.3d at 920 (internal quotations omitted). And the
   root issue with “bare bones” affidavits is that they do not explain how or why
   the affiant’s attested knowledge and the specific facts connect.
          Under Leon, the Supreme Court noted that the critical inquiry in this
   analysis is whether the affidavit “provide[s] evidence sufficient to”—at a
   minimum—“create disagreement among thoughtful and competent judges
   as to the existence of probable cause.” 468 U.S. at 926; see also U.S. v. Bosyk,




                                          19
Case: 19-10842      Document: 00516443952            Page: 20    Date Filed: 08/23/2022




                                      No. 19-10842


   933 F.3d 319, 333 (4th Cir. 2019); U.S. v. Davis, 530 F.3d 1069, 1083 n.3 (9th
   Cir. 2008); U.S. v. Luong, 470 F.3d 898, 903 (9th Cir. 2006). Cramming facts
   into a supporting affidavit does not make reliance on the resulting warrant
   more objectively reasonable unless those facts are probative as to probable
   cause. But the majority departs from this approach and exalts quantity over
   quality. For instance, the majority lauds the fact that the supporting affidavit
   in this case was “over three pages” long; specified the locations where the
   marijuana, ecstasy, and glass pipe were found; and stated the quantity of
   ecstasy pills recovered (namely, sixteen). Ante, at 9. But the search of
   Defendant’s phone was justified only on the basis that people who sell drugs,
   and other “criminals,” might have inculpatory photographs on their phones.
   And none of these facts indicate that Morton sold drugs or otherwise
   possessed them for anything other than personal use.
          In short, Trooper Blue makes sweeping generalizations about criminal
   activity and cell phone use, yet not once does he mention why such evidence
   could or would be on Morton’s phone or how it relates to simple possession.
   No reasonable officer could have perceived the facts alleged in the supporting
   affidavit to be “indicia of probable cause” to support a search of Defendant’s
   phone. Leon, 468 U.S. at 923.
          Lastly, I fear that the incentive for law enforcement to imitate Trooper
   Blue’s conduct in this case will be both strong and widespread. It is routine
   for officers to find evidence of small quantities of illicit drugs for personal use
   during an automobile stop. If the officer then wishes to gain access to such
   person’s phone—and, with it, “[t]he sum of [his or her] private life,” Riley,
   573 U.S. at 394—the majority’s approach imposes virtually no costs against
   doing so. All the officer needs to do is state what drugs they found, where
   they found it, and provide boilerplate language about how “cellphones are
   used for receipt and delivery of illegal narcotics.” Ante, at 9. The officer can




                                           20
Case: 19-10842     Document: 00516443952           Page: 21   Date Filed: 08/23/2022




                                    No. 19-10842


   then take refuge in the majority’s holding that he is protected by the good
   faith exception. This is unjust, unfair, and unconstitutional.
          I respectfully dissent.




                                         21

```

---
