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

## GROUP: content/cases/United States v. Young.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Young
type: case
citation: "964 F.3d 938 (2020)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, 10th Cir."
court_level: coa
circuit: ca10
year: 2020
date_decided: 2020-07-07
docket: 18-6221
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
  opinion_url: "https://www.courtlistener.com/opinion/4766220/united-states-v-young/"
  cluster_id: 4766220
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Young
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: Key
related:
  - "[[Due-Process Voluntariness of Confessions]]"
  - "[[Colorado v. Connelly]]"
  - "[[Miranda v. Arizona]]"
tags:
  - case
  - fifth-amendment
  - due-process
  - voluntariness
  - coerced-confession
  - police-deception
  - promises-of-leniency
  - tenth-circuit
holding: "A confession is involuntary under the Due Process Clause when, under the totality of the circumstances, the defendant's capacity for self-determination is critically impaired by coercive police conduct; where an agent materially misrepresented the sentence the defendant faced, falsely promised to speak to a federal judge about his cooperation, and dangled leniency, and the defendant's ordinary personal characteristics could not withstand that pressure, the resulting confession was involuntary and had to be suppressed."
aliases:
  - United States v. Young
  - "United States v. Young (10th Cir. 2020)"
---

# United States v. Young

*964 F.3d 938 (10th Cir. 2020)* (No. 18-6221) · U.S. Court of Appeals for the Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4766220 → lead opinion 4546567 (964 F.3d 938, decided 2020-07-07); Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — CL text is slip-paginated). S9 promotes. -->

## Background
During a custodial interrogation, federal Agent Brown obtained a confession from Young. The district court found — and the government did not challenge on appeal — that Brown made false representations to Young about the sentence he faced, misstating how the drug quantity would drive his exposure; falsely told Young he would speak to a federal judge about Young's cooperation and how Young could "buy down" his sentence; and made promises of leniency. Young, who was forty-three years old with a GED and only prior state-system experience, was visibly shocked to learn he faced federal charges. He confessed, and the district court admitted the statements.

## Issue
Whether Young's confession was voluntary under the Due Process Clause, given the interrogating agent's misrepresentations of the sentence and false promises of leniency.

## Rule
Voluntariness is judged under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], and a confession must be suppressed when coercive government conduct overbears the suspect's will; an officer's material misrepresentation of the penalties a suspect faces, coupled with false promises of leniency, weighs heavily toward coercion. Applying that standard, the court held: "Under the totality of the circumstances, we conclude that Young's capacity for self-determination was critically impaired, rendering his confession involuntary." — 964 F.3d 938, slip op. at 15. ^pin-op15

## Application
The court first agreed that Agent Brown's conduct was coercive: misrepresenting the sentence Young faced, falsely promising to intercede with a federal judge, and offering leniency were the kind of deceptions that render a confession involuntary. It then asked whether Young's personal characteristics let him withstand that coercion, and found they did not — he was of ordinary age and education, showed no unusual resilience, and his prior experience was confined to the state system, doing nothing to inoculate him against a federal officer's misrepresentations about federal exposure and cooperation. Weighing the coercive conduct against Young's characteristics under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], the court concluded his will was overborne and his confession was not the product of a rational, free choice.

## Conclusion
The Tenth Circuit **reversed** the district court, **[[Reading and Citing Cases#vacated|vacated]]** the judgment against Young, and **[[Reading and Citing Cases#on-remand|remanded]]** for further proceedings, holding the confession involuntary.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Young* is a clean modern **due-process voluntariness** application: it is not a *[[Miranda v. Arizona|Miranda]]* case but a coercion case, holding that an officer's **misrepresentation of sentencing exposure** plus **false promises of leniency** can overbear an ordinary suspect's will. Read against *[[Colorado v. Connelly|Connelly]]*'s requirement of state action / coercive police conduct, *Young* illustrates the totality inquiry when the coercion is psychological rather than physical.

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key*

## Sources
- [*United States v. Young*, 964 F.3d 938 (10th Cir. 2020)](https://www.courtlistener.com/opinion/4766220/united-states-v-young/) — pinpoint: slip op. at 15 (confession involuntary under the totality of the circumstances; the CL opinion text carries slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "aa37a6f65e00395a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "964 F.3d 938 (2020)", "court": "U.S. Court of Appeals, 10th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Young", "year": "2020"}}
{"assertion_id": "3a78222e08939da4", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key", "title": "United States v. Young"}}
{"assertion_id": "3de061167f1e6f68", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A confession is involuntary under the Due Process Clause when, under the totality of the circumstances, the defendant's capacity for self-determination is critically impaired by coercive police conduct; where an agent materially misrepresented the sentence the defendant faced, falsely promised to speak to a federal judge about his cooperation, and dangled leniency, and the defendant's ordinary personal characteristics could not withstand that pressure, the resulting confession was involuntary and had to be suppressed.", "title": "United States v. Young"}}
{"assertion_id": "9407d93cdc42d6b6", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Young", "varies_by_point": "false"}}
{"assertion_id": "bd8e54a6a59014cc", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 10th Cir.", "title": "United States v. Young"}}
```

### lake record — United States v. Young

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Young",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Young",
    "case_name_short": "Young",
    "case_name_full": "",
    "input_case_name": "United States v. Young",
    "court": "U.S. Court of Appeals, 10th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": "2020-07-07",
    "year": 2020,
    "docket": "18-6221",
    "cluster_id": 4766220,
    "lead_opinion_id": 4546567,
    "sibling_ids": [],
    "absolute_url": "/opinion/4766220/united-states-v-young/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "964 F.3d 938",
      "volume": "964",
      "reporter": "F.3d",
      "page": "938",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "964 F.3d 938",
        "volume": "964",
        "reporter": "F.3d",
        "page": "938",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "964 F.3d 938",
    "official_selection": {
      "court_class": "coa",
      "selected": "964 F.3d 938",
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
    "date_created": "2026-07-07T13:48:58Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:49:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:49:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:49:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:49:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-young--4766220",
      "to_record_id": "United States v. Young",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Young

```
                                                                               FILED
                                                                   United States Court of Appeals
                                     PUBLISH                               Tenth Circuit

                     UNITED STATES COURT OF APPEALS                        July 7, 2020
                                                                      Christopher M. Wolpert
                           FOR THE TENTH CIRCUIT                          Clerk of Court
                       _________________________________

 UNITED STATES OF AMERICA,

      Plaintiff - Appellee,

 v.                                                        No. 18-6221

 SHANE THOMAS YOUNG,

      Defendant - Appellant.
                     _________________________________

                    Appeal from the United States District Court
                       for the Western District of Oklahoma
                          (D.C. No. 5:18-CR-00096-HE-1)
                      _________________________________

Howard Pincus, Assistant Federal Public Defender, Denver, Colorado (Virginia Grady,
Federal Public Defender, Denver, Colorado with him on the briefs) for Defendant-
Appellant.

Steven Creager, Assistant United States Attorney, Oklahoma City, Oklahoma (Timothy
Downing, United States Attorney, and Nicholas Patterson, Assistant United States
Attorney, with him on the brief) for Plaintiff-Appellee.
                        _________________________________

Before LUCERO, KELLY, and PHILLIPS, Circuit Judges.
                  _________________________________

LUCERO, Circuit Judge.
                    _________________________________

      Defendant Shane Young appeals the district court’s denial of his motion to

suppress a confession. He argues the confession was involuntary because the law

enforcement officer who interrogated him deceived him about having access to the
federal judge on the case. Exercising jurisdiction under 28 U.S.C. § 1291, we reverse

and remand to the district court.

                                           I

      In the early morning hours of March 16, 2018, a Woodward County Sheriff’s

Office deputy observed Young’s vehicle swerving on the roadway and signaled for

Young to stop his car. Young continued to drive, ultimately pulling into a nearby

residential property, stopping his car, and fleeing on foot. The deputy pursued, tasing

and arresting Young. After the arrest, the deputy retraced Young’s path and found a

small headphones case containing about four grams 1 of a mixture or substance

containing methamphetamine. Young was released later that day.

      In the late afternoon of March 16, officers returned to the area and found a

black bag containing about 93 grams of a mixture or substance containing

methamphetamine near where Young stopped his car. A resident of the property

stated that he did not recognize the bag the deputies had found in his yard and had

not observed anyone walking around the property earlier that day. Later that night,

the deputy rearrested and interviewed Young. Young admitted to possessing the

smaller quantity of methamphetamine but denied that the larger quantity was his. He

then cut off questioning and revoked his consent to speak.




      1
       The record alternately states the quantity in the headphones case was 3.5
grams and 4 grams. The amount does not affect the outcome of this appeal.

                                          2
      Four days later, while still held in the county jail, Young was interrogated by

Federal Bureau of Investigations Special Agent Kent Brown and a state narcotics

agent. 2 Agent Brown advised Young of his Miranda rights, which he waived. At the

beginning of the interrogation, Young informed the agents that he was concerned

about who would pick up his pregnant fiancée on her release from rehab the next day

and worried about how criminal charges would affect his ability to raise his new

baby. He told the agents he was sick to his stomach and wanted to “roll over and

die.” Agent Brown told Young that he tried to help people in trouble if they were

trying to “do what’s right and get on the right path,” and that after their conversation

he would do his best to try and help.

      Agent Brown then told Young he had gone to Oklahoma City the prior

afternoon to meet with the Assistant United States Attorney and brief the prosecutor

about Young’s arrest. He said the prosecutor had met with the judge. Agent Brown

then showed Young a federal warrant for his arrest. Young was visibly shocked.

Agent Brown told Young he wanted to proceed from the “bad news” that Young was

facing federal charges “to the good news.” He urged Young to trust him and told him

that “from this moment on, I’m on your side.” Young queried, “Is any of this going



      2
        A video recording of the interrogation was introduced at the suppression
hearing. There are no allegations that the footage has been doctored or altered, so we
may rely on this video evidence. See Scott v. Harris, 550 U.S. 372, 381 (2007)
(holding appellate court “should have viewed the facts in the light depicted by the
videotape”); cf. Carabajal v. City of Cheyenne, Wyo., 847 F.3d 1203, 1207 (10th Cir.
2017) (“[W]e cannot ignore clear, contrary video evidence in the record depicting the
events as they occurred.”).
                                           3
to help me?” Agent Brown responded, “Yes, absolutely,” and pivoted again to the

“good news,” telling Young that he was on his side and that Young had to trust him.

      Agent Brown continued, describing his trip to Oklahoma City the previous day

to obtain the federal warrant and telling Young that he had spoken with the judge

who had reviewed the case. He said the judge had looked at Young’s criminal

record. Agent Brown emphasized that he was “not bullshitting” and repeatedly told

Young to trust him. Then, he told Young that with the smaller amount of

methamphetamine, the judge was willing to charge “anywhere from five to ten

years.” Agent Brown said that Young had two options and that he could “physically

buy down the amount of time you see in a federal prison,” with the difference

depending on Young’s “willingness to own to the information.” He continued,

“every time you answer a question truthfully, it ticks time off that record, it ticks

time off how much you’re going to actually see.” He also repeatedly told Young that

he would go back to the judge and tell him what Young said at the interview,

invoking his supposed relationship with the judge numerous times. Agent Brown

reiterated yet again that Young needed to trust him, and he asked Young about the

bag with the larger quantity of drugs in it, suggesting that Young could explain that

he threw the bags in different directions as he ran from the car.

      In response, Young wondered aloud whether he should have a lawyer present.

Then, he said, “I want to help myself out, man, but at the same time I feel like I’m

buying the farm.” Following Agent Brown’s earlier suggestion, Young admitted that



                                            4
after he exited his vehicle, he lost his grip on the containers of methamphetamine,

and they flew in different directions as he was running away.

      After his confession, Young was charged with possession with intent to

distribute approximately 97 grams of a mixture or substance containing a detectable

amount of methamphetamine. He moved to suppress his confession as involuntary.

The district court held a suppression hearing, at which Agent Brown testified that his

“number of mentions” of having spoken with the judge were all “error[s] in

specificity of speech” and that his intent was to say “prosecutor.” Agent Brown also

stated that at the time of Young’s interview, although he had spoken about the case to

the federal magistrate judge who signed Young’s warrant, they had not discussed

potential charges. Agent Brown further testified that he did not know the actual

sentencing range for the offenses for which Young was charged and that when he

used the five- to ten-year figure, he was providing a tangible number to explain to

Young that “cooperation can pay dividends.”

      Although the court found Agent Brown made false representations and

improper promises of leniency that were “coercive in nature under the

circumstances,” it ultimately concluded Young’s confession was not involuntary and

denied his motion to suppress. Young pled guilty and was sentenced to 188 months’

imprisonment and five years’ supervised release. He timely appealed.

                                          II

      “When a party challenges a district court’s ruling on a motion to suppress a

confession, we review its conclusions of law de novo and its factual findings for clear

                                          5
error. We consider the evidence in the light most favorable to the district court’s

determination.” United States v. Pettigrew, 468 F.3d 626, 633 (10th Cir. 2006)

(citation omitted). Thus, “when reviewing the denial of a motion to suppress, an

appellate court must consider the evidence adduced at the suppression hearing . . . in

the light most favorable to the Government.” United States v. Rodebaugh, 798 F.3d

1281, 1290 (10th Cir. 2015) (alteration and quotation omitted).

      “[C]onvictions following the admission into evidence of confessions which are

involuntary, i.e., the product of coercion, either physical or psychological, cannot

stand.” Rogers v. Richmond, 365 U.S. 534, 540 (1961). “To be admiss[i]ble, a

confession must be made freely and voluntarily; it must not be extracted by threats in

violation of due process or obtained by compulsion or inducement of any sort.”

Griffin v. Strong, 983 F.2d 1540, 1542 (10th Cir. 1993). Voluntariness is determined

under the totality of the circumstances, and no single factor is determinative. See

United States v. Lopez, 437 F.3d 1059, 1063 (10th Cir. 2006).

      The district court found that Agent Brown made false representations to Young

when he stated that he was “on your side” and that he had discussions with the judge

about Young’s charges and sentence. It also found Agent Brown’s statement that

Young could “buy down” his time by answering questions truthfully was a promise

of leniency. Its findings that there were false representations and promises of

leniency are factual findings subject to clear error review. See id. at 1062, 1064.

The government does not challenge these findings on appeal.



                                           6
      We review de novo the legal conclusion that Young’s statement was voluntary.

Id. at 1062. The government bears the burden of showing voluntariness by a

preponderance of the evidence. Id. at 1063. “The central consideration in

determining whether a confession has been coerced always involves this question:

did the governmental conduct complained of bring about a confession not freely self-

determined?” Griffin, 983 F.2d at 1543 (quotations omitted). Put another way, the

issue is whether the confession is “the product of an essentially free and

unconstrained choice by its maker.” United States v. Perdue, 8 F.3d 1455, 1466

(10th Cir. 1993) (quotation omitted). If not, “if his will has been overborne and his

capacity for self-determination critically impaired, the use of his confession offends

due process.” Id. (quotation omitted). The inquiry is based on the totality of the

circumstances and requires consideration of “both the characteristics of the accused

and the details of the interrogation.” United States v. Toles, 297 F.3d 959, 966 (10th

Cir. 2002). This test “does not favor any one of these factors over the others—it is a

case-specific inquiry where the importance of any given factor can vary in each

situation.” Sharp v. Rohling, 793 F.3d 1216, 1233 (10th Cir. 2015).

      “[C]oercive police activity is a necessary predicate to the finding that a

confession is not ‘voluntary.’” Colorado v. Connelly, 479 U.S. 157, 167 (1986).

Accordingly, we first address Agent Brown’s conduct—his misrepresentations and

promises of leniency. We then turn to other factors that may contribute to

involuntariness, including the defendant’s mental condition. See id. at 164 (“[A]s

interrogators have turned to more subtle forms of psychological persuasion, courts

                                           7
have found the mental condition of the defendant a more significant factor in the

‘voluntariness’ calculus.”); United States v. Erving L., 147 F.3d 1240, 1249-50 (10th

Cir. 1998) (defendant’s personal characteristics relevant if officers’ conduct

coercive).

                                           A

      Promises of leniency are “relevant to determining whether a confession was

involuntary and, depending on the totality of the circumstances, may render a

confession coerced.” Clanton v. Cooper, 129 F.3d 1147, 1159 (10th Cir. 1997),

overruled on other grounds by Becker v. Kroll, 494 F.3d 904 (10th Cir. 2007).

Similarly, an officer’s deceptions or misrepresentations may, but do not necessarily,

render a confession coerced. See Lopez, 437 F.3d at 1065.

      During the interrogation, Agent Brown told Young that he was facing a

sentence of five to ten years’ imprisonment and that the length of the sentence

depended primarily on Young’s cooperation. He also told Young he could

“physically buy down the amount of time you see in a federal prison.” These were

misrepresentations. Possession with intent to distribute 97 grams of a mixture or

substance containing methamphetamine carries a minimum sentence of five years and

a maximum sentence of forty years. 21 U.S.C. § 841(b)(1)(B). In contrast,

possession with intent to distribute four grams of a mixture or substance containing

methamphetamine carries a maximum sentence of 20 years and no mandatory

minimum. § 841(b)(1)(C). The latter may also be prosecuted as simple possession,

with a maximum sentence of one, two, or three years depending on the defendant’s

                                           8
prior criminal history. 21 U.S.C. § 844(a). Similarly, under the Sentencing

Guidelines, possession of 97 grams of a mixture or substance containing

methamphetamine corresponds to a much longer sentence than possession of four

grams, contrary to Agent Brown’s misrepresentations.

       Although we do not require a law enforcement officer to inform a suspect of

the penalties for all the charges he may face, if he misrepresents these penalties, then

that deception affects our evaluation of the voluntariness of any resulting statements.

In this interrogation, Agent Brown misrepresented the law to Young, a factor that

weighs in favor of concluding his actions were coercive. See Clanton, 129 F.3d at

1158 (“[C]ourts are much less likely to tolerate misrepresentations of law.”).

       Although “the fact that an officer promises to make a defendant’s cooperation

known to prosecutors will not produce a coerced confession,” Lopez, 437 F.3d at

1064, Agent Brown did not merely inform Young that cooperation would be viewed

favorably by the prosecutor. Instead, Agent Brown repeatedly told Young he had

spoken with a federal judge who had reviewed the case. He emphasized to Young

that he would tell the judge whether Young had cooperated and that cooperation

would “physically buy down the amount of time you see in a federal prison.” He

said, “every time you answer a question truthfully, it ticks time off that record, . . .

that’s the way it works.” But that is not the way the federal system works. Agents

do not provide information directly to federal judges for use in determining the

charges or sentences suspects face.



                                             9
      At the suppression hearing, Agent Brown tried to walk back his statements

about talking to the “judge,” testifying that he had meant to refer to the prosecutor. 3

But we do not consider what Agent Brown intended to say. Rather, we view the

coercive nature of assertions from the standpoint of the defendant. See United States

v. Walton, 10 F.3d 1024, 1029 (3d Cir. 1993); United States v. Shears, 762 F.2d 397,

402 (4th Cir. 1985) (evaluating “the defendant’s perception of what government

agents have promised”).

      Turning to Agent Brown’s promises of leniency, we have held that “a promise

of leniency is relevant to determining whether a confession was involuntary and,

depending on the totality of the circumstances, may render a confession coerced.”

Clanton, 129 F.3d at 1159; see also Griffin, 983 F.2d at 1543 (“Where a promise of

leniency has been made in exchange for a statement, an inculpatory statement would

be the product of inducement, and thus not an act of free will.” (quotations omitted));

cf. United States v. Nguyen, 155 F.3d 1219, 1223 (10th Cir. 1998) (holding statement

that prosecutor will be informed of defendant’s cooperation does not, without more,

constitute a promise of leniency). In this case, Agent Brown told Young he could




      3
        The district court did not explicitly rule on whether it credited Agent
Brown’s explanation. It ultimately determined that even if credited, the explanation
did “not change the coercive nature of the assertions when viewed from the
standpoint of the defendant.”

                                           10
“physically buy down” the length of the sentence and that each truthful response

would “tick[] time off” his sentence. 4

      We faced a similar situation in Lopez. In that case, law enforcement officers

wrote the words “mistake,” “murder,” “6,” and “60” on slips of paper to show the

defendant he would receive a six-year sentence if he cooperated and a sixty-year

sentence if he did not. 437 F.3d at 1064. We held this was not a permissible “limited

assurance,” but rather an improper promise of leniency “of the sort that may . . .

critically impair a defendant’s capacity for self-determination.” Id. at 1065. The

government contends that Lopez is distinguishable because it involved a quid pro quo

promise of leniency, arguing that Agent Brown’s improper promises were not as

specific as the agents’ promises in Lopez. We are not persuaded.

      In Lopez, we held the defendant’s confession was involuntary because of the

officers’ promise of leniency, combined with their misrepresentation or exaggeration

of the evidence against the defendant. Id. at 1064-65. The government argues, and

Young does not contest, that Agent Brown did not misrepresent or exaggerate the

evidence against him. But like the officers in Lopez, Agent Brown made inaccurate

representations about the sentence Young faced and promised leniency if Young

incriminated himself. Critically, Agent Brown also made improper representations




      4
        Although Agent Brown did tell Young he made no promises as to a particular
sentence or disposition, he did not explicitly say so until after Young incriminated
himself.

                                          11
about his purported access to a federal judge—misconduct as coercive as the officers’

misrepresentation or exaggeration of the evidence in Lopez.

      The government points out that just four days before Agent Brown’s

interrogation, 5 Young stopped the sheriff’s deputy’s interrogation by revoking his

consent to speak. The government argues that this shows that Young generally knew

he could stop an interrogation. In contrast, about eleven minutes into Agent Brown’s

questioning, Young confessed. By that time, Young had been confronted with a

federal arrest warrant and told that federal charges had been filed against him. But

the main difference between the two interrogations is that before the second, Agent

Brown misrepresented the law and made false promises of leniency, including a

particularly troubling false promise of access to the federal judiciary. 6 Young’s

awareness that he could stop the interrogation did little to mitigate the coercive

nature of Agent Brown’s actions.

      We acknowledge that some aspects of the interrogation were not coercive. In

Sharp, we noted that we should consider “whether the suspect was advised of his or



      5
        Agent Brown erroneously testified that the first interrogation occurred the
day prior to his. The district court repeated this error. The first interrogation
occurred on March 16, 2018, whereas Agent Brown’s interrogation was on March 20.
      6
         The government points out other differences between the interviews: it states
that Young seemed more willing to confess at the beginning of the second interview,
that Agent Brown developed a rapport with Young, and that Agent Brown confirmed
that he had seen the dashboard camera video and offered to explain why the agents
were asking about Young’s possession of the container with 93 grams. But in our
view, the key difference was Agent Brown’s misrepresentations and promises of
leniency.
                                           12
her constitutional rights, the length of his or her detention, the nature of the

questioning, and any physical punishment such as deprivation of food or sleep.” 793

F.3d at 1233. None of these forms of coercion occurred in this case, and admittedly,

several factors weigh against concluding the interrogation was coercive. The

questioning was friendly and short: Young confessed within minutes of the

beginning of the interrogation. Cf. Lopez, 437 F.3d at 1062, 1065 (implying

interrogations lasting thirty minutes or one hour are short). Young was fully advised

of his constitutional rights 7 and knew that he could stop the interrogation, as

demonstrated by his stopping of the deputy’s questioning four days earlier. And well

into the interrogation, he asked the agents whether he should wait for his lawyer to be

present and declined to consent to a search of his phone.

       But these factors are not dispositive. Cf. United States v. Bustillos-Munoz,

235 F.3d 505, 517 n.8 (10th Cir. 2000) (“A suspect cannot be subjected to invalid

coercion to obtain a confession just because he earlier was given a valid Miranda

warning.”). Our inquiry is based on the totality of the circumstances. Considering

all of the evidence, we agree with the district court that Agent Brown’s conduct was



       7
         Notably, before the Miranda warning, the state narcotics agent elicited what
could be construed as an incriminating statement. After Young was brought into the
interrogation room but before he received a Miranda warning, Agent Brown left the
room. Young asked the state officer if the agents were going to get him out of jail,
and the officer responded that it would depend on Agent Brown. After a brief
silence, the officer asked Young if he had anything else “going on,” and Young
responded that he had been “working selling dope.” Because Young did not argue at
the district court or on appeal that this pre-warning questioning contributed to the
involuntariness of his confession, we do not consider it.
                                            13
coercive in nature, particularly in light of his misrepresentation of the sentence

Young faced, his false statement that he would speak to a federal judge about

Young’s cooperation, and his promises of leniency.

                                           B

      Because we agree that Agent Brown’s conduct was coercive, we turn to

Young’s personal characteristics to answer the ultimate question: whether Young’s

statements were voluntary. See Lopez, 437 F.3d at 1064. There is no evidence in the

record to indicate that Young was “unusually susceptible to coercion because of age,

lack of education, or intelligence.” Toles, 297 F.3d at 966 (quotation omitted).

Young was 43 years old and had completed a GED. And nothing in the record

suggests that he has limited intelligence. See Lopez, 437 F.3d at 1060 (age and

education did not weigh in favor of involuntariness for 33-year old defendant who

finished eleventh grade); Toles, 297 F.3d at 966.

      The district court correctly noted that Young had prior experience with the

criminal justice system. Although that is relevant to our analysis of voluntariness,

see id., Young’s prior experience was solely in the state system. This prior

experience did not necessarily make him less susceptible to believing promises of

leniency and misrepresentations by a federal law enforcement officer explaining his

access to a federal judge and how Young could “buy down” his sentence. And

Young was visibly shocked when Agent Brown told him he faced federal charges.

      Young’s personal characteristics are not dispositive, and they do not convince

us that Young could withstand the coercion created by Agent Brown’s legal

                                           14
misrepresentations and promises of leniency. See Lopez, 437 F.3d. at 1066

(concluding coerced confession was involuntary even though defendant’s personal

characteristics did not suggest unusual susceptibility to coercion). Under the totality

of the circumstances, we conclude that Young’s capacity for self-determination was

critically impaired, rendering his confession involuntary.

                                          III

      For the foregoing reasons, we REVERSE the decision of the district court,

VACATE the judgment entered against Young, and REMAND for proceedings

consistent with this decision.




                                          15

```

---

## GROUP: content/cases/Uzuegbunam v. Preczewski.md  (`case`, 5 assertions)

### content_page

```
---
title: Uzuegbunam v. Preczewski
type: case
citation: "592 U.S. 279 (2021)"
parallel_cite: "141 S. Ct. 792; 209 L. Ed. 2d 94"
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2021
date_decided: ""
docket: 19-968
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
  opinion_url: "https://www.courtlistener.com/opinion/4861817/uzuegbunam-v-preczewski/"
  cluster_id: 4861817
  opinion_id: null
  identity_checked: true
lake:
  record_id: Uzuegbunam v. Preczewski
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
tags:
  - case
  - section-1983
  - standing
  - nominal-damages
  - first-amendment
holding: "A plaintiff's request for nominal damages satisfies Article III's redressability requirement where his claim rests on a completed violation of a legal right, so a suit for a past constitutional injury is not moot merely because only nominal damages remain."
---

# Uzuegbunam v. Preczewski

*592 U.S. 279 (2021)* (No. 19-968) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4861817 → opinion 4665596; quote string-matched to the CL slip-opinion text 2026-07-07 (CL carries the slip opinion "592 U. S. ____ (2021)"; U.S.-reporter page equality not asserted per S2 A3). S9 promotes. -->

## Background
Chike Uzuegbunam, a student at Georgia Gwinnett College, was stopped by campus officials from distributing religious literature and later from speaking even within a designated "free speech zone," after officials invoked policies restricting on-campus speech. He and fellow student Joseph Bradford sued college officials under the First Amendment, seeking injunctive relief and nominal damages. The officials discontinued the challenged policies, which mooted the request for injunctive relief, and then argued that the students' remaining request for nominal damages could not by itself sustain standing. The Eleventh Circuit agreed and dismissed the case.

## Issue
Whether a plaintiff who seeks only nominal damages for a completed violation of a constitutional right retains Article III standing to pursue the suit.

## Rule
Article III standing requires a remedy likely to redress the plaintiff's injury. Looking to the forms of relief available at common law, the Court explained that a party whose rights were invaded could always recover nominal damages without proving actual damage, and that nominal damages are "not purely symbolic" but constitute relief on the merits. It therefore held: "Because nominal damages were available at common law in analogous circumstances, we conclude that a request for nominal damages satisfies the redressability element of standing where a plaintiff's claim is based on a completed violation of a legal right." — 592 U.S. 279 (slip op., at 11). ^pin-op

## Application
Uzuegbunam experienced a completed violation of his constitutional rights when the officials enforced the speech policies against him, and nominal damages can redress that past injury even though he did not or could not quantify the harm in economic terms. Redressability was thus satisfied. The Court did not decide whether Bradford, who self-censored rather than being directly enjoined, had likewise suffered a past, completed injury, leaving that question for the District Court.

## Conclusion
The judgment of the Eleventh Circuit was **reversed** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. Thomas, J., delivered the opinion of the Court, joined by Breyer, Alito, Sotomayor, Kagan, Gorsuch, Kavanaugh, and Barrett, JJ.; Kavanaugh, J., filed a [[Common Legal Terms#concurring-opinion|concurring opinion]]; Roberts, C.J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Uzuegbunam* is a standing decision that keeps § 1983 and other constitutional-tort suits for completed violations alive when only nominal damages remain, so a defendant cannot moot accountability by discontinuing the challenged conduct after the injury.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Uzuegbunam v. Preczewski*, 592 U.S. 279 (2021)](https://www.courtlistener.com/opinion/4861817/uzuegbunam-v-preczewski/) — pinpoint: slip op., at 11 (Opinion of the Court, Part III, holding; Thomas, J.). CL carries the slip opinion ("592 U. S. ____ (2021)"; cluster 4861817 → opinion 4665596); slip-only per S2 A3 — quote string-matched to the CL opinion text 2026-07-07, U.S.-reporter page equality not asserted.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "674dd9798fd6d97f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "592 U.S. 279 (2021)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "141 S. Ct. 792; 209 L. Ed. 2d 94", "title": "Uzuegbunam v. Preczewski", "year": "2021"}}
{"assertion_id": "0ffbd0bed7b1aa0d", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Recent development", "title": "Uzuegbunam v. Preczewski"}}
{"assertion_id": "dae902f79361b4de", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A plaintiff's request for nominal damages satisfies Article III's redressability requirement where his claim rests on a completed violation of a legal right, so a suit for a past constitutional injury is not moot merely because only nominal damages remain.", "title": "Uzuegbunam v. Preczewski"}}
{"assertion_id": "3f9441492dc28972", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Uzuegbunam v. Preczewski"}}
{"assertion_id": "49b53fe71a62e4d5", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Uzuegbunam v. Preczewski", "varies_by_point": "false"}}
```

### lake record — Uzuegbunam v. Preczewski

```json
{
  "schema_version": "s2.v1",
  "record_id": "Uzuegbunam v. Preczewski",
  "status": "under_review",
  "identity": {
    "case_name": "Uzuegbunam v. Preczewski",
    "case_name_short": "Uzuegbunam",
    "case_name_full": "",
    "input_case_name": "Uzuegbunam v. Preczewski",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2021,
    "docket": "19-968",
    "cluster_id": 4861817,
    "lead_opinion_id": 4665596,
    "sibling_ids": [],
    "absolute_url": "/opinion/4861817/uzuegbunam-v-preczewski/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "592 U.S. 279",
      "volume": "592",
      "reporter": "U.S.",
      "page": "279",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "141 S. Ct. 792",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "792",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "209 L. Ed. 2d 94",
        "volume": "209",
        "reporter": "L. Ed. 2d",
        "page": "94",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "592 U.S. 279",
        "volume": "592",
        "reporter": "U.S.",
        "page": "279",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 792",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "792",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "209 L. Ed. 2d 94",
        "volume": "209",
        "reporter": "L. Ed. 2d",
        "page": "94",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "592 U.S. 279",
    "official_selection": {
      "court_class": "scotus",
      "selected": "592 U.S. 279",
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
    "date_created": "2026-07-06T12:10:07Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:10:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:10:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:10:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:10:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "uzuegbunam-v-preczewski--4861817",
      "to_record_id": "Uzuegbunam v. Preczewski",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Uzuegbunam v. Preczewski

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

        UZUEGBUNAM ET AL. v. PRECZEWSKI ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                THE ELEVENTH CIRCUIT

    No. 19–968.      Argued January 12, 2021—Decided March 8, 2021
Petitioners are former students of Georgia Gwinnett College who wished
  to exercise their religion by sharing their faith on campus while en-
  rolled there. In 2016, Chike Uzuegbunam talked with interested stu-
  dents and handed out religious literature on campus grounds. Uzueg-
  bunam stopped after a campus police officer informed him that campus
  policy prohibited distributing written religious materials outside areas
  designated for that purpose. A college official later explained to Uzueg-
  bunam that he could speak about his religion or distribute materials
  only in two designated speech areas on campus, and even then only
  after securing a permit. But when Uzuegbunam obtained the required
  permit and tried to speak in a free speech zone, a campus police officer
  again asked him to stop, this time saying that people had complained
  about his speech. Campus policy at that time prohibited using the free
  speech zone to say anything that “disturbs the peace and/or comfort of
  person(s).” The officer told Uzuegbunam that his speech violated cam-
  pus policy because it had led to complaints, and the officer threatened
  Uzuegbunam with disciplinary action if he continued. Uzuegbunam
  again complied with the order to stop speaking. Another student who
  shares Uzuegbunam’s faith, Joseph Bradford, decided not to speak
  about religion because of these events. Both Uzuegbunam and Brad-
  ford sued certain college officials charged with enforcement of the col-
  lege’s speech policies, arguing that these policies violated the First
  Amendment. As relevant here, the students sought injunctive relief
  and nominal damages. The college officials ultimately chose to discon-
  tinue the challenged policies rather than to defend them, and they
  sought dismissal on the ground that the policy change left the students
  without standing to sue. The parties agreed that the policy change
  rendered the students’ request for injunctive relief moot, but disputed
2                   UZUEGBUNAM v. PRECZEWSKI

                                  Syllabus

    whether the students had standing to maintain the suit based on their
    remaining claim for nominal damages. The Eleventh Circuit held that
    while a request for nominal damages can sometimes save a case from
    mootness, such as where a person pleads but fails to prove an amount
    of compensatory damages, the students’ plea for nominal damages
    alone could not by itself establish standing.
Held: A request for nominal damages satisfies the redressability element
 necessary for Article III standing where a plaintiff’s claim is based on
 a completed violation of a legal right. Pp. 3–12.
    (a) To establish Article III standing, the Constitution requires a
 plaintiff to identify an injury in fact that is fairly traceable to the chal-
 lenged conduct and to seek a remedy likely to redress that injury.
 Spokeo, Inc. v. Robins, 578 U. S. 330, 338. The dispute here concerns
 whether the remedy Uzuegbunam sought—nominal damages—can re-
 dress the completed constitutional violation that he alleges occurred
 when campus officials enforced the speech policies against him. The
 Court looks to the forms of relief awarded at common law to determine
 whether nominal damages can redress a past injury. The prevailing
 rule at common law was that a party whose rights are invaded can
 always recover nominal damages without furnishing evidence of actual
 damage. By permitting plaintiffs to pursue nominal damages when-
 ever they suffered a personal legal injury, the common law avoided the
 oddity of privileging small economic rights over important, but not eas-
 ily quantifiable, nonpecuniary rights. Pp. 3–8.
    (b) The common law did not require a plea for compensatory dam-
 ages as a prerequisite to an award of nominal damages. Nominal dam-
 ages are not purely symbolic. They are instead the damages awarded
 by default until the plaintiff establishes entitlement to some other
 form of damages. A single dollar often will not provide full redress,
 but the partial remedy satisfies the redressability requirement.
 Church of Scientology of Cal. v. United States, 506 U. S. 9, 13. Re-
 spondents’ argument that a plea for compensatory damages is neces-
 sary to confer jurisdiction also does not square with established prin-
 ciples of standing. And unlike an award of attorney’s fees and costs
 which may be the byproduct of a successful suit, an award of nominal
 damages constitutes relief on the merits. Pp. 8–11.
    (c) A request for redress in the form of nominal damages does not
 guarantee entry to court. In addition to redressability, the plaintiff
 must establish the other elements of standing and satisfy all other rel-
 evant requirements, such as pleading a cognizable cause of action.
 Uzuegbunam experienced a completed violation of his constitutional
 rights when respondents enforced their speech policies against him.
 Nominal damages can redress Uzuegbunam’s injury even if he cannot
 or chooses not to quantify that harm in economic terms. The Court
                      Cite as: 592 U. S. ____ (2021)                     3

                                 Syllabus

  does not decide whether Bradford can pursue nominal damages and
  leaves for the District Court to determine whether Bradford has estab-
  lished a past, completed injury. Pp. 11–12.

781 Fed. Appx. 824, reversed and remanded.

  THOMAS, J., delivered the opinion of the Court, in which BREYER, ALITO,
SOTOMAYOR, KAGAN, GORSUCH, KAVANAUGH, and BARRETT, JJ., joined.
KAVANAUGH, J., filed a concurring opinion. ROBERTS, C. J., filed a dissent-
ing opinion.
                        Cite as: 592 U. S. ____ (2021)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 19–968
                                    _________________


    CHIKE UZUEGBUNAM, ET AL., PETITIONERS v.
         STANLEY C. PRECZEWSKI, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
          APPEALS FOR THE ELEVENTH CIRCUIT
                                  [March 8, 2021]

   JUSTICE THOMAS delivered the opinion of the Court.
   At all stages of litigation, a plaintiff must maintain a per-
sonal interest in the dispute. The doctrine of standing gen-
erally assesses whether that interest exists at the outset,
while the doctrine of mootness considers whether it exists
throughout the proceedings. To demonstrate standing, the
plaintiff must not only establish an injury that is fairly
traceable to the challenged conduct but must also seek a
remedy that redresses that injury. And if in the course of
litigation a court finds that it can no longer provide a plain-
tiff with any effectual relief, the case generally is moot.
This case asks whether an award of nominal damages by
itself can redress a past injury. We hold that it can.
                             I
  According to the complaint, Chike Uzuegbunam is an
evangelical Christian who believes that an important part
of exercising his religion includes sharing his faith. In
2016, Uzuegbunam decided to share his faith at Georgia
Gwinnett College, a public college where he was enrolled as
a student. At an outdoor plaza on campus near the library
2               UZUEGBUNAM v. PRECZEWSKI

                      Opinion of the Court

where students often gather, Uzuegbunam engaged in con-
versations with interested students and handed out reli-
gious literature.
   A campus police officer soon informed Uzuegbunam that
campus policy prohibited distributing written religious ma-
terials in that area and told him to stop. Uzuegbunam com-
plied with the officer’s order. To learn more about this pol-
icy, he then visited the college’s Director of the Office of
Student Integrity, who was directly responsible for promul-
gating and enforcing the policy. When asked if Uzueg-
bunam could continue speaking about his religion if he
stopped distributing materials, the official said no. The of-
ficial explained that Uzuegbunam could speak about his re-
ligion or distribute materials only in two designated “free
speech expression areas,” which together make up just
0.0015 percent of campus. And he could do so only after
securing the necessary permit. Uzuegbunam then applied
for and received a permit to use the free speech zone.
   Twenty minutes after Uzuegbunam began speaking on
the day allowed by his permit, another campus police officer
again told him to stop, this time saying that people had
complained about his speech. Campus policy prohibited us-
ing the free speech zone to say anything that “disturbs the
peace and/or comfort of person(s).” App. to Pet. for Cert.
151(a). The officer told Uzuegbunam that his speech vio-
lated this policy because it had led to complaints. The of-
ficer threatened Uzuegbunam with disciplinary action if he
continued. Uzuegbunam again complied with the order to
stop speaking. Another student who shares Uzuegbunam’s
faith, Joseph Bradford, decided not to speak about religion
because of these events.
   Both students sued a number of college officials in charge
of enforcing the college’s speech policies, arguing that those
policies violated the First Amendment. As relevant here,
they sought nominal damages and injunctive relief. Re-
spondents initially attempted to defend the policy, stating
                  Cite as: 592 U. S. ____ (2021)              3

                      Opinion of the Court

that Uzuegbunam’s discussion of his religion “arguably rose
to the level of ‘fighting words.’ ” Id., at 155(a). But the col-
lege officials quickly abandoned that strategy and instead
decided to get rid of the challenged policies. They then
moved to dismiss, arguing that the suit was moot, because
of the policy change. The students agreed that injunctive
relief was no longer available, but they disagreed that the
case was moot. They contended that their case was still live
because they had also sought nominal damages. The Dis-
trict Court dismissed the case, holding that the students’
claim for nominal damages was insufficient by itself to es-
tablish standing.
   The Eleventh Circuit affirmed. 781 Fed. Appx. 824
(2019). It stated that a request for nominal damages can
save a case from mootness in certain circumstances, such
as where a person pleads but fails to prove an amount of
compensatory damages. But, because the students did not
request compensatory damages, their plea for nominal
damages could not by itself establish standing.
   We granted certiorari to consider whether a plaintiff who
sues over a completed injury and establishes the first two
elements of standing (injury and traceability) can establish
the third by requesting only nominal damages. 591 U. S.
___ (2020). We now reverse.
                               II
   To satisfy the “ ‘irreducible constitutional minimum’ ” of
Article III standing, a plaintiff must not only establish
(1) an injury in fact (2) that is fairly traceable to the chal-
lenged conduct, but he must also seek (3) a remedy that is
likely to redress that injury. Spokeo, Inc. v. Robins, 578
U. S. 330, 338 (2016); see also Gill v. Whitford, 585 U. S.
___, ___–___ (2018) (slip op., at 13–14). There is no dispute
that Uzuegbunam has established the first two elements.
The only question is whether the remedy he sought—nom-
inal damages—can redress the constitutional violation that
4               UZUEGBUNAM v. PRECZEWSKI

                      Opinion of the Court

Uzuegbunam alleges occurred when campus officials en-
forced the speech policies against him.
                                A
   In determining whether nominal damages can redress a
past injury, we look to the forms of relief awarded at com-
mon law. “Article III’s restriction of the judicial power to
‘Cases’ and ‘Controversies’ is properly understood to mean
‘cases and controversies of the sort traditionally amenable
to, and resolved by, the judicial process.’ ” Vermont Agency
of Natural Resources v. United States ex rel. Stevens, 529
U. S. 765, 774 (2000) (quoting Steel Co. v. Citizens for Better
Environment, 523 U. S. 83, 102 (1998)); cf. Memphis Com-
munity School Dist. v. Stachura, 477 U. S. 299, 306 (1986)
(relief for “§1983 plaintiffs . . . is ordinarily determined ac-
cording to principles derived from the common law of
torts”). The parties here agree that courts at common law
routinely awarded nominal damages. They, instead, dis-
pute what kinds of harms those damages could redress.
   Both sides agree that nominal damages historically could
provide prospective relief. The award of nominal damages
was one way for plaintiffs at common law to “obtain a form
of declaratory relief in a legal system with no general de-
claratory judgment act.” D. Laycock & R. Hasen, Modern
American Remedies 636 (5th ed. 2019). For example, a tres-
pass to land or water rights might raise a prospective threat
to a property right by creating the foundation for a future
claim of adverse possession or prescriptive easement.
Blanchard v. Baker, 8 Me. 253, 268 (1832) (“If an unlawful
diversion [of water] is suffered for twenty years, it ripens
into a right, which cannot be controverted”). By obtaining
a declaration of trespass, a property owner could “vindicate
his right by action” and protect against those future
threats. Ibid. Courts at common law would not declare
property boundaries in the abstract, “but the suit for nomi-
nal damages allowed them to do so indirectly.” Laycock,
                  Cite as: 592 U. S. ____ (2021)             5

                      Opinion of the Court

supra, at 636.
  The parties disagree, however, about whether nominal
damages alone could provide retrospective relief. Stressing
the declaratory function, respondents argue that nominal
damages by themselves redressed only continuing or
threatened injury, not past injury.
  But cases at common law paint a different picture. Early
courts required the plaintiff to prove actual monetary dam-
ages in every case: “[I]njuria & damnum [injury and dam-
age] are the two grounds for the having [of] all actions, and
without these, no action lieth.” Cable v. Rogers, 3 Bulst.
311, 312, 81 Eng. Rep. 259 (K. B. 1625). Later courts, how-
ever, reasoned that every legal injury necessarily causes
damage, so they awarded nominal damages absent evi-
dence of other damages (such as compensatory, statutory,
or punitive damages), and they did so where there was no
apparent continuing or threatened injury for nominal dam-
ages to redress. See, e.g., Barker v. Green, 2 Bing. 317, 130
Eng. Rep. 327 (C. P. 1824) (nominal damages awarded for
1-day delay in arrest because “if there was a breach of duty
the law would presume some damage”); Hatch v. Lewis, 2
F. & F. 467, 479, 485–486, 175 Eng. Rep. 1145, 1150, 1153
(N. P. 1861) (ineffective assistance by criminal defense at-
torney that does not prejudice the client); Dods v. Evans, 15
C. B. N. S. 621, 624, 627, 143 Eng. Rep. 929, 930–931 (C. P.
1864) (breach of contract); Marzetti v. Williams, 1 B. & Ad.
415, 417–418, 423–428, 109 Eng. Rep. 842, 843, 845–847
(K. B. 1830) (bank’s 1-day delay in paying on a check); id.,
at 424, 109 Eng. Rep., at 845 (recognizing that breach of
contract could create a continuing injury but determining
that the fact of breach of contract by itself justified nominal
damages).
  The latter approach was followed both before and after
ratification of the Constitution. An early case about voting
rights effectively illustrates this common-law understand-
ing. Faced with a suit pleading denial of the right to vote,
6               UZUEGBUNAM v. PRECZEWSKI

                       Opinion of the Court

the court rejected the plaintiff ’s claim because, among
other reasons, the plaintiff had not established actual dam-
ages. Ashby v. White, 2 Raym. Ld. 938, 941–943, 948, 92
Eng. Rep. 126, 129, 130, 133 (K. B. 1703). Dissenting, Lord
Holt argued that the common law inferred damages when-
ever a legal right was violated. Observing that the law rec-
ognized “not merely pecuniary” injury but also “personal in-
jury,” Lord Holt stated that “every injury imports a
damage” and that a plaintiff could always obtain damages
even if he “does not lose a penny by reason of the [viola-
tion].” Id., at 955, 92 Eng. Rep., at 137. Although Lord Holt
was in the minority, the House of Lords overturned the ma-
jority decision, thus validating Lord Holt’s position, 3 Salk.
17, 91 Eng. Rep. 665 (K. B. 1703), and this principle “laid
down . . . by Lord Holt” was followed “in many subsequent
cases,” Embrey v. Owen, 6 Exch. 353, 368, 155 Eng. Rep.
579, 585 (1851).
   The dissent correctly notes that English courts differed in
some respects from courts under our system, but Lord
Holt’s position also prevailed in courts on this side of the
Atlantic. Applying what he called Lord Holt’s “incontro-
vertible” reasoning, Justice Story explained that a prevail-
ing plaintiff “is entitled to a verdict for nominal damages”
whenever “no other [kind of damages] be proved.” Webb v.
Portland Mfg. Co., 29 F. Cas. 506, 508–509 (No. 17,322) (CC
Me. 1838). Because the common law recognized that “every
violation imports damage,” Justice Story reasoned that
“[t]he law tolerates no farther inquiry than whether there
has been the violation of a right.” Ibid. Justice Story also
made clear that this logic applied to both retrospective and
prospective relief. Id., at 507 (stating that nominal dam-
ages are available “wherever there is a wrong” and that, “[a]
fortiori, this doctrine applies where there is not only a vio-
lation of a right of the plaintiff, but the act of the defendant,
if continued, may become the foundation, by lapse of time,
of an adverse right”).
                  Cite as: 592 U. S. ____ (2021)             7

                      Opinion of the Court

   The dissent discounts Justice Story’s statement, saying
that he took a potentially contradictory position elsewhere
and asserted that both actual damages and a violation of a
legal right are required. Post, at 7–8 (opinion of ROBERTS,
C. J.). But in the same source the dissent cites, Justice
Story said that nominal damages are “presumed” “[w]here
the breach of duty is clear.” Commentaries on the Law of
Agency §217, p. 211 (1839). Justice Story adopted the same
position a few years later. Whipple v. Cumberland Mfg. Co.,
29 F. Cas. 934, 936 (No. 17,516) (CC Me. 1843) (stating that
it is “well-known and well-settled” that “wherever a wrong
is done to a right,” at minimum “nominal damages will be
given”). And other jurists declared that “[t]he principle that
every injury legally imports damage, was decisively settled,
in the case of Ashby.” Parker v. Griswold, 17 Conn. *288,
*304–*306 (1845) (citing many cases on both sides of the
Atlantic, including Webb and Marzetti). This history is
hardly one of “indeterminate sources.” Post, at 8.
   Admittedly, the rule allowing nominal damages for a vio-
lation of any legal right, though “decisively settled,” Parker,
17 Conn., at *304, was not universally followed—as is true
for most common-law doctrines. And some courts only fol-
lowed the rule in part, recognizing the availability of nomi-
nal damages but holding that the improper denial of nomi-
nal damages could be harmless error. Yet, even among
these courts, many adopted the rule in full whenever a per-
son proved that there was a violation of an “important
right.” E.g., Hecht v. Harrison, 5 Wyo. 279, 290, 40 P. 306,
309–310 (1895); accord, Reid v. Johnson, 132 Ind. 416, 419,
31 N. E. 1107, 1108 (1892) (“substantial right”). Nonethe-
less, the prevailing rule, “well established” at common law,
was “that a party whose rights are invaded can always re-
cover nominal damages without furnishing any evidence of
actual damage.” 1 T. Sedgwick, Measure of Damages 71,
n. a (7th ed. 1880); see also id., at 72 (citing Lord Holt’s
opinion in Ashby).
8              UZUEGBUNAM v. PRECZEWSKI

                     Opinion of the Court

   That this rule developed at common law is unsurprising
in the light of the noneconomic rights that individuals had
at that time. A contrary rule would have meant, in many
cases, that there was no remedy at all for those rights, such
as due process or voting rights, that were not readily reduc-
ible to monetary valuation. See D. Dobbs, Law of Remedies
§3.3(2) (3d ed. 2018) (nominal damages are often awarded
for a right “not economic in character and for which no sub-
stantial non-pecuniary award is available”); see also Carey
v. Piphus, 435 U. S. 247, 266–267 (1978) (awarding nominal
damages for a violation of procedural due process). By per-
mitting plaintiffs to pursue nominal damages whenever
they suffered a personal legal injury, the common law
avoided the oddity of privileging small-dollar economic
rights over important, but not easily quantifiable, nonpecu-
niary rights.
                              B
   Respondents and the dissent attempt to discount this his-
torical line of cases by contending that something other
than nominal damages provided redressability. They argue
instead that courts could award nominal damages only
when a plaintiff pleaded compensatory damages but failed
to prove a specific amount. In those circumstances, they
say, the plea for compensatory damages is what satisfied
the redressability requirement, and courts awarded nomi-
nal damages merely as a technical matter. We do not agree.
   To begin with, the cases themselves did not require a plea
for compensatory damages as a condition for receiving nom-
inal damages. Lord Holt spoke in categorical terms:
“[E]very injury imports a damage,” so a plaintiff who proved
a legal violation could always obtain some form of damages
because he “must of necessity have a means to vindicate
and maintain [the right].” Ashby, 2 Raym. Ld., at 953–955,
92 Eng. Rep., at 136–137. Justice Story’s language was no
less definitive: “The law tolerates no farther inquiry than
                  Cite as: 592 U. S. ____ (2021)            9

                      Opinion of the Court

whether there has been the violation of a right.” Webb, 29
F. Cas., at 508. When a right is violated, that violation “im-
ports damage in the nature of it” and “the party injured is
entitled to a verdict for nominal damages.” Id., at 508.
   Respondents and the dissent thus get the relationship be-
tween nominal damages and compensatory damages back-
wards. Nominal damages are not a consolation prize for the
plaintiff who pleads, but fails to prove, compensatory dam-
ages. They are instead the damages awarded by default
until the plaintiff establishes entitlement to some other
form of damages, such as compensatory or statutory dam-
ages. See, e.g., Dods, 15 C. B. N. S., at 621, 627, 143
Eng. Rep., at 929, 931 (prevailing plaintiff entitled to nom-
inal damages as a matter of law even where jury neglected
to find them); see also Stachura, 477 U. S., at 308 (rejecting
the argument that courts could presume, without proof,
damages greater than nominal).
   The argument that a claim for compensatory damages is
a prerequisite for an award of nominal damages also rests
on the flawed premise that nominal damages are purely
symbolic, a mere judicial token that provides no actual ben-
efit to the plaintiff. That contention is not without some
support. See, e.g., Stanton v. New York & Eastern R. Co.,
59 Conn. 272, 282, 22 A. 300, 303 (1890) (“Nominal damages
mean no damages at all. They exist only in name, and not
in amount”); but cf. ibid. (still recognizing that nominal
damages are appropriate when a right is violated). But this
view is against the weight of the history discussed above,
and we have already expressly rejected it. Despite being
small, nominal damages are certainly concrete. The dissent
says that “an award of nominal damages does not change [a
plaintiff’s] status or condition at all.” Post, at 3. But we
have already held that a person who is awarded nominal
damages receives “relief on the merits of his claim” and
“may demand payment for nominal damages no less than
10              UZUEGBUNAM v. PRECZEWSKI

                      Opinion of the Court

he may demand payment for millions of dollars in compen-
satory damages.” Farrar v. Hobby, 506 U. S. 103, 111, 113
(1992). Because nominal damages are in fact damages paid
to the plaintiff, they “affec[t] the behavior of the defendant
towards the plaintiff ” and thus independently provide re-
dress. Hewitt v. Helms, 482 U. S. 755, 761 (1987) (emphasis
deleted); accord, Mission Product Holdings, Inc. v. Temp-
nology, LLC, 587 U. S. ___, ___ (2019) (slip op., at 6) (“If
there is any chance of money changing hands, [the] suit re-
mains live”). True, a single dollar often cannot provide full
redress, but the ability “to effectuate a partial remedy” sat-
isfies the redressability requirement. Church of Scientology
of Cal. v. United States, 506 U. S. 9, 13 (1992).
   The next difficulty faced by respondents and the dissent
is their inability to square their argument with established
principles of standing. Because redressability is an “ ‘irre-
ducible’ ” component of standing, Spokeo, 578 U. S., at 338,
no federal court has jurisdiction to enter a judgment unless
it provides a remedy that can redress the plaintiff ’s injury.
Yet early courts routinely awarded nominal damages alone.
Certainly, no one seems to think that those judgments were
without legal effect. Those nominal damages necessarily
must have provided redress. Respondents contend that a
request for compensatory damages at the pleading stage
was what provided the basis for nominal damages at the
judgment stage. But a plaintiff must maintain a personal
interest in the dispute at every stage of litigation, including
when judgment is entered, Lujan v. Defenders of Wildlife,
504 U. S. 555, 561 (1992), and must do so “separately for
each form of relief sought,” Friends of the Earth, Inc. v.
Laidlaw Environmental Services (TOC), Inc., 528 U. S. 167,
185 (2000). As soon as a plea for compensatory damages
fails at the factfinding stage of litigation, that plea can no
longer support jurisdiction for a favorable judgment. The
dissent’s contrary assertion is unaccompanied by any cita-
tion.
                  Cite as: 592 U. S. ____ (2021)             11

                      Opinion of the Court

  Likewise, any analogy to attorney’s fees and costs fails.
A request for attorney’s fees or costs cannot establish stand-
ing because those awards are merely a “byproduct” of a suit
that already succeeded, not a form of redressability. Steel
Co., 523 U. S., at 107; see also Lewis v. Continental Bank
Corp., 494 U. S. 472, 480 (1990). In contrast, nominal dam-
ages are redress, not a byproduct.
                                III
   Because nominal damages were available at common law
in analogous circumstances, we conclude that a request for
nominal damages satisfies the redressability element of
standing where a plaintiff’s claim is based on a completed
violation of a legal right.
   The dissent worries that after today the Judiciary will be
required to weigh in on legal questions “whenever a plain-
tiff asks for a dollar.” Post, at 9. But petitioners still would
have satisfied redressability if instead of one dollar in nom-
inal damages they sought one dollar in compensation for a
wasted bus fare to travel to the free speech zone. The dis-
sent “would place a higher value on Article III” than a dol-
lar. Post, at 1; but see Sprint Communications Co. v. APCC
Services, Inc., 554 U. S. 269, 305 (2008) (ROBERTS, C. J., dis-
senting) (“Article III is worth a dollar”). But Congress abol-
ished the statutory amount-in-controversy requirement for
federal-question jurisdiction in 1980. Federal Question Ju-
risdictional Amendments Act, 94 Stat. 2369. And we have
never held that one applies as a matter of constitutional
law.
   This is not to say that a request for nominal damages
guarantees entry to court. Our holding concerns only re-
dressability. It remains for the plaintiff to establish the
other elements of standing (such as a particularized injury);
plead a cognizable cause of action, Planck v. Anderson, 5
T. R. 37, 41, 101 Eng. Rep. 21, 23 (K. B. 1792) (“if no [actual]
damage be sustained, the creditor has no cause of action”
12                UZUEGBUNAM v. PRECZEWSKI

                         Opinion of the Court

for some claims); and meet all other relevant requirements.
We hold only that, for the purpose of Article III standing,
nominal damages provide the necessary redress for a com-
pleted violation of a legal right.
  Applying this principle here is straightforward. For pur-
poses of this appeal, it is undisputed that Uzuegbunam ex-
perienced a completed violation of his constitutional rights
when respondents enforced their speech policies against
him. Because “every violation [of a right] imports damage,”
Webb, 29 F. Cas., at 509, nominal damages can redress
Uzuegbunam’s injury even if he cannot or chooses not to
quantify that harm in economic terms.*
  The judgment of the Court of Appeals is reversed, and the
case is remanded for further proceedings consistent with
this opinion.
                                             It is so ordered.




——————
  *We do not decide whether Bradford can pursue nominal damages.
Nominal damages go only to redressability and are unavailable where a
plaintiff has failed to establish a past, completed injury. The District
Court should determine in the first instance whether the enforcement
against Uzuegbunam also violated Bradford’s constitutional rights.
                 Cite as: 592 U. S. ____ (2021)            1

                   KAVANAUGH, J., concurring

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 19–968
                         _________________


   CHIKE UZUEGBUNAM, ET AL., PETITIONERS v.
        STANLEY C. PRECZEWSKI, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
          APPEALS FOR THE ELEVENTH CIRCUIT
                        [March 8, 2021]

   JUSTICE KAVANAUGH, concurring.
   I agree with the Court that, as a matter of history and
precedent, a plaintiff’s request for nominal damages can
satisfy the redressability requirement for Article III stand-
ing and can keep an otherwise moot case alive. I write sep-
arately simply to note that I agree with THE CHIEF JUSTICE
and the Solicitor General that a defendant should be able
to accept the entry of a judgment for nominal damages
against it and thereby end the litigation without a resolu-
tion of the merits. Post, at 11 (ROBERTS, C. J., dissenting);
Brief for United States as Amicus Curiae 29–30.
                 Cite as: 592 U. S. ____ (2021)            1

                   ROBERTS, C. J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 19–968
                         _________________


   CHIKE UZUEGBUNAM, ET AL., PETITIONERS v.
        STANLEY C. PRECZEWSKI, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
          APPEALS FOR THE ELEVENTH CIRCUIT
                        [March 8, 2021]

   CHIEF JUSTICE ROBERTS, dissenting.
   Petitioners Chike Uzuegbunam and Joseph Bradford
want to challenge the constitutionality of speech re-
strictions at Georgia Gwinnett College. There are just a few
problems: Uzuegbunam and Bradford are no longer stu-
dents at the college. The challenged restrictions no longer
exist. And the petitioners have not alleged actual damages.
The case is therefore moot because a federal court cannot
grant Uzuegbunam and Bradford “any effectual relief what-
ever.” Chafin v. Chafin, 568 U. S. 165, 172 (2013) (internal
quotation marks omitted).
   The Court resists this conclusion, holding that the peti-
tioners can keep pressing their claims because they have
asked for “nominal damages.” In the Court’s view, nominal
damages can save a case from mootness because any
amount of money—no matter how trivial—“can redress a
past injury.” Ante, at 1. But an award of nominal damages
does not alleviate the harms suffered by a plaintiff, and is
not intended to. If nominal damages can preserve a live
controversy, then federal courts will be required to give ad-
visory opinions whenever a plaintiff tacks on a request for
a dollar. Because I would place a higher value on Article
III, I respectfully dissent.
2               UZUEGBUNAM v. PRECZEWSKI

                    ROBERTS, C. J., dissenting

                               I
   In urging the ratification of the Constitution, Alexander
Hamilton famously wrote that “the judiciary, from the na-
ture of its functions, will always be the least dangerous” of
“the different departments of power.” The Federalist
No. 78, p. 465 (C. Rossiter ed. 1961). This was so, Hamilton
explained, because the Judiciary “will be least in a capacity
to annoy or injure” “the political rights of the Constitution.”
Ibid. Whereas “[t]he executive not only dispenses the hon-
ors but holds the sword of the community,” and “[t]he legis-
lature not only commands the purse but prescribes the
rules by which the duties and rights of every citizen are to
be regulated,” the Judiciary “may truly be said to have nei-
ther FORCE nor WILL but merely judgment.” Ibid.
   But that power of judgment can nonetheless bind the Ex-
ecutive and Legislature—and the States. It is modest only
if confined to its proper sphere. As John Marshall empha-
sized during his one term in the House of Representatives,
“[i]f the judicial power extended to every question under the
constitution” or “to every question under the laws and trea-
ties of the United States,” then “[t]he division of power
[among the branches of Government] could exist no longer,
and the other departments would be swallowed up by the
judiciary.” 4 Papers of John Marshall 95 (C. Cullen ed.
1984) (quoted in DaimlerChrysler Corp. v. Cuno, 547 U. S.
332, 341 (2006)). To maintain adequate separation between
the Judiciary, on the one hand, and the political branches
and the States, on the other, Article III of the Constitution
authorizes federal courts to decide only “Cases” and
“Controversies”—that is, “cases of a Judiciary nature.”
2 Records of the Federal Convention of 1787, p. 430
(M. Farrand ed. 1966) (J. Madison).
   The case-or-controversy requirement imposes fundamen-
tal restrictions on who can invoke federal jurisdiction and
what types of disputes federal courts can resolve. As perti-
nent here, “when it is impossible for a court to grant any
                  Cite as: 592 U. S. ____ (2021)              3

                    ROBERTS, C. J., dissenting

effectual relief whatever to the prevailing party,” Chafin,
568 U. S., at 172 (internal quotation marks omitted), the
case is moot, and the court has no power to decide it, see
Spencer v. Kemna, 523 U. S. 1, 18 (1998). To decide a moot
case would be to give an advisory opinion, in violation of
“the oldest and most consistent thread in the federal law
of justiciability.” Flast v. Cohen, 392 U. S. 83, 96 (1968)
(internal quotation marks omitted).
   By insisting that judges be able to provide meaningful re-
dress to litigants, Article III ensures that federal courts ex-
ercise their authority only “as a necessity in the determina-
tion of real, earnest and vital controversy between
individuals.” Chicago & Grand Trunk R. Co. v. Wellman,
143 U. S. 339, 345 (1892); see Valley Forge Christian Col-
lege v. Americans United for Separation of Church and
State, Inc., 454 U. S. 464, 471 (1982) (“The constitutional
power of federal courts cannot be defined, and indeed has
no substance, without reference to the necessity ‘to adjudge
the legal rights of litigants in actual controversies.’ ” (quot-
ing Liverpool, New York & Philadelphia S. S. Co. v. Com-
missioners of Emigration, 113 U. S. 33, 39 (1885))). When
plaintiffs like Uzuegbunam and Bradford allege neither ac-
tual damages nor the prospect of future injury, an award of
nominal damages does not change their status or condition
at all. Such an award instead represents a judicial deter-
mination that the plaintiffs’ interpretation of the law is
correct—nothing more. The court in such a case is acting
not as an Article III court, but as a moot court, deciding
cases “in the rarified atmosphere of a debating society.”
Director, Office of Workers’ Compensation Programs v.
Perini North River Associates, 459 U. S. 297, 305 (1983)
(internal quotation marks omitted).
                           II
  The Court sees no problem with turning judges into ad-
vice columnists. In its view, the common law and (to a
4               UZUEGBUNAM v. PRECZEWSKI

                    ROBERTS, C. J., dissenting

lesser extent) our cases require that federal courts open
their doors to any plaintiff who asks for a dollar. I part
ways with the Court regarding both the framework it ap-
plies and the result it reaches.
   Begin with the framework. The Court’s initial premise is
that we must “look to the forms of relief awarded at common
law” in order to decide “whether nominal damages can re-
dress a past injury.” Ante, at 4. Because the Court finds
that “nominal damages were available at common law in
analogous circumstances” to the ones before us, it “con-
clude[s] that a request for nominal damages satisfies the
redressability element of standing where a plaintiff ’s claim
is based on a completed violation of a legal right.” Ante, at
11.
   Any lessons that we learn from the common law, how-
ever, must be tempered by differences in constitutional de-
sign. The structure and function of 18th-century English
courts were in many respects irreconcilable with “the role
assigned to the judiciary in a tripartite allocation of power.”
Flast, 392 U. S., at 95. Perhaps most saliently, in England
“all jurisdictions of courts [were] either mediately or imme-
diately derived from the crown,” 1 W. Blackstone, Commen-
taries on the Laws of England 257 (1765), an organizational
principle the Framers explicitly rejected by separating the
Executive from the Judiciary. This difference in organiza-
tion yielded a difference in operation. To give just one ex-
ample, “English judicial practice with which early Ameri-
cans were familiar had long permitted the Crown to solicit
advisory opinions from judges.” R. Fallon, J. Manning, D.
Meltzer, & D. Shapiro, Hart and Wechsler’s The Federal
Courts and the Federal System 52 (7th ed. 2015). We would
not look to such practice for guidance today if a plaintiff
came into court arguing that advisory opinions were in fact
an appropriate form of Article III redress. We would know
that they are not. We likewise should know that a bare re-
quest for nominal damages is not justiciable because the
                  Cite as: 592 U. S. ____ (2021)            5

                   ROBERTS, C. J., dissenting

plaintiff cannot “benefit in a tangible way from the court’s
intervention.” Steel Co. v. Citizens for Better Environment,
523 U. S. 83, 103, n. 5 (1998) (internal quotation marks
omitted).
   We should of course consult founding-era decisions when
discerning the boundaries of our jurisdiction, for the Fram-
ers sought to limit the judicial power to “Cases” and “Con-
troversies,” as those terms were understood at the time.
See Coleman v. Miller, 307 U. S. 433, 460 (1939) (opinion of
Frankfurter, J.). No question. But that does not mean that
the requirements of Article III are “satisfied merely because
a party requests a court of the United States to declare its
legal rights, and has couched that request for forms of relief
historically associated with courts of law in terms that have
a familiar ring to those trained in the legal process.” Valley
Forge, 454 U. S., at 471. A focus on common law analogues
cannot obscure the significance of the establishment of an
independent Judiciary—a “remarkable transformation”
from a system with courts operating as “appendages of
crown power.” Gordon S. Wood, The Origins of Judicial Re-
view, 22 Suffolk U. L. Rev. 1293, 1304 (1988). That trans-
formation carries with it the need to cabin the jurisdiction
of the Judiciary to ensure it does not trespass on the prov-
ince of the political branches.
   It is in any event entirely unclear whether common law
courts would have awarded nominal damages in a case like
the one before us. There is no dispute that “nominal dam-
ages historically could provide prospective relief,” because
such awards allowed “plaintiffs at common law to ‘obtain a
form of declaratory relief in a legal system with no general
declaratory judgment act.’ ” Ante, at 4 (quoting D. Laycock
& R. Hasen, Modern American Remedies 636 (5th ed. 2019);
emphasis added); see Borchard, The Declaratory Judgment—
A Needed Procedural Reform, 28 Yale L. J. 1, 25–29 (1918)
(describing the development of declaratory judgments in
England in the second half of the 19th century). Yet the
6               UZUEGBUNAM v. PRECZEWSKI

                   ROBERTS, C. J., dissenting

petitioners in this case no longer seek prospective relief.
Although they initially asked for a declaratory judgment
and a preliminary injunction, they abandoned those re-
quests once the college rescinded the challenged policies.
   The Court is correct to note that plaintiffs at common law
often received nominal damages for past violations of their
rights. Those awards, however, were generally limited to
situations in which prevailing plaintiffs tried and failed to
prove actual damages. See 1 D. Dobbs, Law of Remedies
§3.3(2), p. 296 (2d ed. 1993) (describing nominal damages
awards as “a rescue operation”). Notwithstanding the
Court’s protestations to the contrary, nominal damages in
such cases were in fact a “consolation prize,” ante, at 9,
awarded as a hook to allow prevailing plaintiffs to at least
recover attorney’s fees and costs. See W. Hale, Handbook
on the Law of Damages 30–31 (1896) (“The importance of
the right to recover nominal damages often consists in its
effect on costs.”); 1 T. Sedgwick, Measure of Damages §96,
p. 164 (9th ed. 1912) (“[T]hey are a mere peg to hang costs
on.” (internal quotation marks omitted)). The petitioners in
this case have asked to recover their fees and costs, but they
never sought actual damages, so the common law provides
little relevant support.
   On this last point, the Court acknowledges in several
places that the historical record is mixed as to whether legal
violations were actionable at all without a showing of com-
pensable harm. See ante, at 5, 7. And the Court does not
cite any case in which plaintiffs sought only nominal dam-
ages for purely retrospective injuries. The Court instead
relies on several decisions that contained live damages
claims, see Barker v. Green, 2 Bing. 317, 130 Eng. Rep. 327
(C. P. 1824) (“actual damage was the gist of the action”);
Hatch v. Lewis, 2 F. & F. 467, 469, 175 Eng. Rep. 1145, 1146
(N. P. 1861) (defendants’ ineffective assistance allegedly
caused plaintiff to be “deprived of the profits and emolu-
ments he might otherwise have obtained”); Dods v. Evans,
                  Cite as: 592 U. S. ____ (2021)            7

                   ROBERTS, C. J., dissenting

15 C. B. N. S. 621, 143 Eng. Rep. 929 (C. P. 1864) (action for
damages), or involved prospective harm to the plaintiff ’s
reputation, see Marzetti v. Williams, 1 B. & Ad. 415, 420,
109 Eng. Rep. 842, 844 (K. B. 1830) (bank’s failure to timely
pay “was injurious to the character of the plaintiff in his
trade”); see also C. Addison, Law of Torts 46–47 (1860) (def-
amation actionable without proof of damage).
   The Court also appeals to “categorical” and “definitive”
statements by Lord Chief Justice Holt and Justice Story,
that “every injury imports a damage,” Ashby v. White, 2
Raym. Ld. 938, 955, 92 Eng. Rep. 126, 137 (K. B. 1703), and
that “[t]he law tolerates no farther inquiry than whether
there has been the violation of a right,” Webb v. Portland
Mfg. Co., 29 F. Cas. 506, 508 (No. 17,322) (CC Me. 1838).
Ante, at 8–9. These statements, however, bear less weight
than the Court suggests. Lord Holt was alone in dissent in
Ashby (no shame there), and although his opinion has been
cited favorably by subsequent cases and commentary, his
colleagues disagreed with him. The Court writes that “the
House of Lords overturned the majority decision, thus vali-
dating Lord Holt’s position,” ante, at 6, but the House of
Lords likely paid scant attention to Lord Holt’s analysis. It
appears instead that the majority decision was reversed as
collateral damage in a Whig-Tory political dispute, and “lit-
tle weight was given to reasoning or eloquence.” 2 J. Camp-
bell, Lives of the Chief Justices of England 160 (1849).
(Ashby had tried to vote for a Whig candidate, and his ballot
had been rejected as part of a Tory election-rigging scheme.
Id., at 156–157.) Regardless, the House of Lords held that
Ashby “should recover his damages assessed by the jury” at
trial, suggesting that the fact of injury alone did not “im-
port” them. Ashby v. White, 1 Bro. P. C. 62, 64, 1 Eng. Rep.
417, 418 (1703).
   Justice Story is no more helpful to the Court—despite the
supposedly “definitive” nature of his statement in Webb—
as he took the position elsewhere in his writings that a legal
8               UZUEGBUNAM v. PRECZEWSKI

                   ROBERTS, C. J., dissenting

violation alone was not sufficient to ground a lawsuit. See
Commentaries on the Law of Agency §236, p. 200 (1839)
(“[T]he rule applies, that though it is a wrong, it is without
any damage; and, to maintain an action, both must concur;
for damnum absque injuria, and injuria absque damno, are
equally objections to any recovery.”). Perhaps Justice
Story’s conflicting statements can be reconciled, see ante, at
7; Hessick, Standing, Injury in Fact, and Private Rights, 93
Cornell L. Rev. 275, 283, n. 38 (2008), but neither his com-
mentary nor Lord Holt’s dissent provides firm footing for
the position that a plaintiff could seek nominal damages
without alleging actual damages or prospective harm.
   At bottom, the Court relies on a handful of indeterminate
sources to justify a radical expansion of the judicial power.
The Court acknowledges that “the rule allowing nominal
damages for a violation of any legal right . . . was not uni-
versally followed,” ante, at 7, but even this concession un-
derstates the equivocal nature of the historical record. I
would require more before bursting the bounds of Article
III.
   The Court spends little time trying to reconcile its analy-
sis with modern justiciability principles. It cites in passing
our decisions in Carey v. Piphus, 435 U. S. 247 (1978), Mem-
phis Community School Dist. v. Stachura, 477 U. S. 299
(1986), and Farrar v. Hobby, 506 U. S. 103 (1992), but those
cases made no mention of Article III, and none involved a
standalone claim for nominal damages. The Court also con-
tends that nominal damages must provide redress because
courts would otherwise lack jurisdiction to award them,
even where a plaintiff tries and fails to prove actual dam-
ages. See ante, at 10. But a claim for actual damages pre-
serves a live controversy, see Memphis Light, Gas & Water
Div. v. Craft, 436 U. S. 1, 8–9 (1978), and a court does not
lose jurisdiction just because that claim ultimately fails.
   Finally, the Court argues that nominal damages provide
Article III relief because they “affec[t] the behavior of the
                  Cite as: 592 U. S. ____ (2021)              9

                    ROBERTS, C. J., dissenting

defendant towards the plaintiff ” by requiring “money
changing hands.” Ante, at 10 (internal quotation marks
omitted). If this were the standard, then the prospect of
attorney’s fees and costs would confer standing at the be-
ginning of a lawsuit and prevent mootness throughout—a
proposition we have squarely rejected. See Lewis v. Conti-
nental Bank Corp., 494 U. S. 472, 480 (1990). The Court
posits that “nominal damages are redress,” whereas fees
and costs “are merely a byproduct of a suit that already suc-
ceeded.” Ante, at 11 (internal quotation marks omitted).
This classification just begs the question of what qualifies
as redress. To satisfy Article III, redress must alleviate the
plaintiff ’s alleged injury in some way, either by compensat-
ing the plaintiff for a past loss or by preventing an ongoing
or future harm. Nominal damages do not serve these ends
where a plaintiff alleges only a completed violation of his
rights. They are not intended to approximate the value of
tangible or intangible harms, or the deterrent effect re-
quired to prevent future misconduct. And they are not cal-
culated with reference to either of these purposes. Because
such an award performs no remedial function—and because
“[r]elief that does not remedy the injury suffered cannot
bootstrap a plaintiff into federal court,” Steel Co., 523 U. S.,
at 107—nominal damages cannot preserve a live contro-
versy where a case is otherwise moot.
                              III
  Today’s decision risks a major expansion of the judicial
role. Until now, we have said that federal courts can review
the legality of policies and actions only as a necessary inci-
dent to resolving real disputes. Going forward, the Judici-
ary will be required to perform this function whenever a
plaintiff asks for a dollar. For those who want to know if
their rights have been violated, the least dangerous branch
will become the least expensive source of legal advice.
  In an effort to downplay these consequences, the Court
10              UZUEGBUNAM v. PRECZEWSKI

                    ROBERTS, C. J., dissenting

argues that plaintiffs who seek nominal damages will often
be able to seek actual damages as well. In this case, for
example, the Court notes that Uzuegbunam and Bradford
“would have satisfied redressability if instead of one dollar
in nominal damages they sought one dollar in compensation
for a wasted bus fare to travel to the free speech zone.”
Ante, at 11. Maybe they would have, and maybe they
should have. The Court is mistaken, however, to equate a
small amount of actual damages with the token award of
nominal damages. The former redresses a compensable
harm and satisfies Article III, while the latter is a legal fic-
tion with “no existence in point of quantity.” J. Mayne, Law
of Damages 27 (1856) (internal quotation marks omitted);
see Dobbs, Law of Remedies §3.3(2), at 294 (“Nominal dam-
ages are damages in name only . . . .”).
   The Court also insists that not every “request for nominal
damages guarantees entry to court.” Ante, at 11. Yet its
holding admits of no limiting principle. As then-Judge
McConnell remarked in an insightful concurrence on the is-
sue before us, “[i]t is hard to conceive of a case in which a
plaintiff would be unable to append a claim for nominal
damages, and thus insulate the case from the possibility of
mootness.” Utah Animal Rights Coalition v. Salt Lake City
Corp., 371 F. 3d 1248, 1266 (CA10 2004). The Court today
reinforces this point by emphasizing that “every violation of
a right imports damage,” ante, at 12 (emphasis added; al-
terations and internal quotation marks omitted)—even
though we have definitively and recently held that a plain-
tiff must allege a concrete injury even where his rights have
been violated, see Thole v. U. S. Bank N. A., 590 U. S. ___,
___ (2020) (slip op., at 5) (“This Court has rejected the ar-
gument that ‘a plaintiff automatically satisfies the injury-
in-fact requirement whenever a statute grants a person a
statutory right and purports to authorize that person to sue
to vindicate that right.’ ” (quoting Spokeo, Inc. v. Robins,
578 U. S. 330, 341 (2016))).
                  Cite as: 592 U. S. ____ (2021)           11

                   ROBERTS, C. J., dissenting

   The best that can be said for the Court’s sweeping excep-
tion to the case-or-controversy requirement is that it may
itself admit of a sweeping exception: Where a plaintiff asks
only for a dollar, the defendant should be able to end the
case by giving him a dollar, without the court needing to
pass on the merits of the plaintiff ’s claims. Although we
recently reserved the question whether a defendant can
moot a case by depositing the full amount requested by the
plaintiff, Campbell-Ewald Co. v. Gomez, 577 U. S. 153, 166
(2016), our cases have long suggested that he can, see, e.g.,
California v. San Pablo & Tulare R. Co., 149 U. S. 308, 313–
314 (1893). The United States agrees, arguing in its brief
in “support” of the petitioners that “the defendant should be
able to end the litigation without a resolution of the consti-
tutional merits, simply by accepting the entry of judgment
for nominal damages against him.” Brief for United States
as Amicus Curiae 29. The defendant can even file an offer
of judgment for one dollar, rendering the plaintiff liable for
any subsequent costs if he receives only nominal damages.
See Fed. Rule Civ. Proc. 68(d). This is a welcome caveat,
and it may ultimately save federal courts from issuing
reams of advisory opinions. But it also highlights the flim-
siness of the Court’s view of the separation of powers. The
scope of our jurisdiction should not depend on whether the
defendant decides to fork over a buck.
                        *     *    *
  Five years after Hamilton wrote Federalist No. 78, Secre-
tary of State Thomas Jefferson sent a letter on behalf of
President George Washington to Chief Justice John Jay
and the Associate Justices of the Supreme Court, asking for
advice about the Nation’s rights and obligations regarding
the ongoing war in Europe. Washington’s request must
have struck him as reasonable enough, since English sover-
eigns regularly sought advice from their courts. Yet the
12             UZUEGBUNAM v. PRECZEWSKI

                   ROBERTS, C. J., dissenting

Justices declined the entreaty, citing “the lines of separa-
tion drawn by the Constitution between the three depart-
ments of the government.” 3 Correspondence and Public
Papers of John Jay 488 (H. Johnston ed. 1891). For over
two centuries, the Correspondence of the Justices has stood
as a reminder that federal courts cannot give answers
simply because someone asks.
   The Judiciary is authorized “to say what the law is” only
because “[t]hose who apply [a] rule to particular cases, must
of necessity expound and interpret the rule.” Marbury v.
Madison, 1 Cranch 137, 177 (1803) (emphasis added). To-
day’s decision abandons that principle. When a plaintiff
brings a nominal damages claim in the absence of past dam-
ages or future harm, it is not “necessary to give an opinion
upon a question of law.” San Pablo, 149 U. S., at 314. It is
instead a “gratuitous” exercise of the judicial power, Simon
v. Eastern Ky. Welfare Rights Organization, 426 U. S. 26,
38 (1976), and expanding that power encroaches on the po-
litical branches and the States. Perhaps defendants will
wise up and moot such claims by paying a dollar, but it is
difficult to see that outcome as a victory for Article III.
Rather than encourage litigants to fight over farthings,
I would affirm the judgment of the Court of
Appeals.

```

---

## GROUP: content/cases/Vega v. Tekoh.md  (`case`, 6 assertions)

### content_page

```
---
title: "Vega v. Tekoh"
type: case
citation: "597 U.S. 134 (2022)"
parallel_cite: "213 L. Ed. 2d 479; 142 S. Ct. 2095"
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2022
date_decided: 2022-06-23
docket: 21-499
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2022-06-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Vega v. Tekoh
  varies_by_point: false
  scope_note: "Recent controlling decision; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/6480695/vega-v-tekoh/"
  cluster_id: 6480695
  opinion_id: 6352828
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny"
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Key — Progeny"
related: ["[[Chavez v. Martinez]]", "[[Dickerson v. United States]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "section-1983", "qualified-immunity"]
holding: "A violation of the Miranda rules is not itself a violation of the Fifth Amendment and does not provide a basis for a § 1983 damages claim against the officer who took an un-Mirandized statement."
lake:
  record_id: Vega v. Tekoh
  status: verified
  projected_at: 2026-07-06
---

# Vega v. Tekoh

*597 U.S. 134 (2022)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Deputy Vega questioned Terence Tekoh at his workplace about a reported sexual assault without giving [[Miranda and Custodial Interrogation|Miranda warnings]]; Tekoh wrote an apologetic statement that was admitted at his criminal trial. The jury acquitted. Tekoh then sued Vega under 42 U.S.C. § 1983, claiming the admission of his un-Mirandized statement violated his Fifth Amendment rights. The Ninth Circuit held that using an un-Mirandized statement at a criminal trial can support a § 1983 claim.

## Issue
Whether a plaintiff may sue a police officer under § 1983 based on the admission at a criminal trial of a statement obtained without [[Miranda and Custodial Interrogation|Miranda warnings]] — i.e., whether a *[[Miranda v. Arizona|Miranda]]* violation is a deprivation of a right "secured by the Constitution and laws" for § 1983 purposes.

## Rule
No. "A violation of the *Miranda* rules does not provide a basis for a § 1983 claim." — 597 U.S. at 134 (Held). ^pin-134

*[[Miranda v. Arizona|Miranda]]* imposed a set of *prophylactic* rules to protect the Fifth Amendment privilege; those rules are not themselves the constitutional right, so their breach is not, by itself, a constitutional deprivation. The Court declined to treat the *[[Miranda v. Arizona|Miranda]]* rules as federal "law" creating a § 1983 cause of action because the benefits would be slight and the costs substantial, and "*Miranda* and its progeny provide sufficient protection for the Fifth Amendment right against compelled self-incrimination."

Concluding: "Because a violation of *Miranda* is not itself a violation of the Fifth Amendment, and because we see no justification for expanding *Miranda* to confer a right to sue under § 1983, the judgment of the Court of Appeals is reversed." — *Id.* (Alito, J., for the Court) (concluding paragraph). ^pin-134a

## Application
Tekoh's § 1983 theory rested entirely on the admission of his un-Mirandized statement. Because a *[[Miranda v. Arizona|Miranda]]* violation is not equivalent to a Fifth Amendment violation, that admission — even assuming it was error — did not deprive Tekoh of a right secured by the Constitution and laws within the meaning of § 1983. The proper remedy for a *[[Miranda v. Arizona|Miranda]]* violation is suppression of the statement in the criminal case, not a § 1983 damages action against the interrogating officer.

## Conclusion
A *[[Miranda v. Arizona|Miranda]]* violation is not itself a constitutional violation and cannot ground a § 1983 suit. The Ninth Circuit's judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Vega* extends the logic of [[Chavez v. Martinez]] (the Self-Incrimination Clause is a trial right) and reaffirms that *[[Miranda v. Arizona|Miranda]]*'s rules, though constitutionally based (see [[Dickerson v. United States]]), are prophylactic and do not by themselves create § 1983 liability.

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny*
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny*

## Sources
- *Vega v. Tekoh*, 597 U.S. 134 (2022) — https://www.courtlistener.com/opinion/6480695/vega-v-tekoh/ — pinpoints: 134 (Held); conclusion at end of opinion (Alito, J.). (CourtListener's copy is the slip opinion; official U.S. Reports internal pagination shown as "597 U.S. ____".)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "cab58951dcc90347", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "597 U.S. 134 (2022)", "court": "U.S. Supreme Court", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "213 L. Ed. 2d 479; 142 S. Ct. 2095", "title": "Vega v. Tekoh", "year": "2022"}}
{"assertion_id": "1c95dc8a785f9f7a", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Key — Progeny", "title": "Vega v. Tekoh"}}
{"assertion_id": "5907f53b24d8a4eb", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A violation of the Miranda rules is not itself a violation of the Fifth Amendment and does not provide a basis for a § 1983 damages claim against the officer who took an un-Mirandized statement.", "title": "Vega v. Tekoh"}}
{"assertion_id": "a368dd5d09441970", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Progeny", "title": "Vega v. Tekoh"}}
{"assertion_id": "3d7be0c71c4953da", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Vega v. Tekoh"}}
{"assertion_id": "d563388dcd5b42f6", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2022-06-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Vega v. Tekoh", "field_i_validity": "good_law", "scope_note": "Recent controlling decision; good law.", "title": "Vega v. Tekoh", "varies_by_point": "false"}}
```

### lake record — Vega v. Tekoh

```json
{
  "schema_version": "s2.v1",
  "record_id": "Vega v. Tekoh",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Vega v. Tekoh",
    "case_name_short": "Vega",
    "case_name_full": "",
    "input_case_name": "Vega v. Tekoh",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2022-06-23",
    "year": 2022,
    "docket": "21-499",
    "cluster_id": 6480695,
    "lead_opinion_id": 6352828,
    "sibling_ids": [
      6352828
    ],
    "absolute_url": "/opinion/6480695/vega-v-tekoh/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "597 U.S. 134",
      "volume": "597",
      "reporter": "U.S.",
      "page": "134",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "213 L. Ed. 2d 479",
        "volume": "213",
        "reporter": "L. Ed. 2d",
        "page": "479",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "142 S. Ct. 2095",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "2095",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "597 U.S. 134",
        "volume": "597",
        "reporter": "U.S.",
        "page": "134",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "213 L. Ed. 2d 479",
        "volume": "213",
        "reporter": "L. Ed. 2d",
        "page": "479",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "142 S. Ct. 2095",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "2095",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "597 U.S. 134",
    "official_selection": {
      "court_class": "scotus",
      "selected": "597 U.S. 134",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-134",
      "page": null,
      "quote": "for \u00a7 1983 purposes. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-134a",
      "page": null,
      "quote": "Concluding:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2022-06-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Vega v. Tekoh",
    "varies_by_point": false,
    "scope_note": "Recent controlling decision; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Ronald Fosnight v. Robert Jones",
          "cluster_id": 7441273,
          "cite": [
            "41 F.4th 916"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dwayne Holloway v. City of Milwaukee",
          "cluster_id": 7855045,
          "cite": [
            "43 F.4th 760"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Logan",
          "cluster_id": 9486489,
          "cite": [
            "2024 IL 129054"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Waukegan Potawatomi Casino, LLC v. City of Waukegan",
          "cluster_id": 10333614,
          "cite": [
            "128 F.4th 871"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Midland County",
          "cluster_id": 10116259,
          "cite": [
            "116 F.4th 384"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terence Tekoh v. County of Los Angeles",
          "cluster_id": 9418187,
          "cite": [
            "75 F.4th 1264"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Coulter",
          "cluster_id": 6624576,
          "cite": [
            "41 F.4th 451"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Travis Lester",
          "cluster_id": 9494065,
          "cite": [
            "98 F.4th 768"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aaron Salter v. City of Detroit, Mich.",
          "cluster_id": 10361064,
          "cite": [
            "133 F.4th 527"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Schaefer",
          "cluster_id": 10311854,
          "cite": [
            "563 P.3d 424",
            "2025 UT App 4"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dale E. Holloway, Jr. v. Governor, State of New Hampshire, et al.",
          "cluster_id": 10695608,
          "cite": [
            "2022 DNH 097"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Eric Blackmon v. Gregory Jones",
          "cluster_id": 10360714,
          "cite": [
            "132 F.4th 522"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zuniga De La Cruz v. Garland",
          "cluster_id": 9441968,
          "cite": [
            "86 F.4th 1236"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Willey v. Springfield Twp.",
          "cluster_id": 10862344,
          "cite": [
            "2026 Ohio 1842"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O.W. v. Marie Carr",
          "cluster_id": 10840933,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin Loren Daniels",
          "cluster_id": 10770631,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rajeri Curry",
          "cluster_id": 10710491,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warren v. State",
          "cluster_id": 10679805,
          "cite": [
            "878 S.E.2d 438",
            "314 Ga. 598"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brandon Paul Janssen v. State of Florida",
          "cluster_id": 10661543,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Florida v. Thomas Michael Pastor, Jr.",
          "cluster_id": 10658570,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "M.A. v. J.H.M.",
          "cluster_id": 10592887,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zachary Joseph Penna v. State of Florida",
          "cluster_id": 10419663,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Arizona v. Giovani Fuster Melendez",
          "cluster_id": 10367639,
          "cite": [
            "565 P.3d 1034"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garrett Dale Reeves v. the State of Texas",
          "cluster_id": 10333815,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(6352828) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 25,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 25,
        "triage_read": 0,
        "triage_snippet_classified": 25
      },
      "lane2_top_cited": {
        "query": "cites:(6352828)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0wJnM9MTA2NjE1NDMmdD1vJmQ9MjAyNi0wNy0wNiZwPTI%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%286352828%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(6352828)",
        "reviewed": 25,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 25,
        "triage_read": 0,
        "triage_snippet_classified": 25
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(6352828)",
    "indexed_citing_opinions": 32,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 6352828,
        "count": 32,
        "count_source": "search"
      }
    ],
    "citation_count": 154,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/vega-v-tekoh.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1MjUyODMmcz05NDM4NDI4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%286352828%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 6352828,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 108882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 110268,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 4651954,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 4692581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 7263680,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 8985601,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9413177,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9417767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9419051,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9422515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9422839,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9423233,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9423964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9424454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9425260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9425753,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9426178,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9426459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9426587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9427279,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9427404,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9427547,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9427972,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9429007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9429504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9429664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9429930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9430786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9431349,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9431819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9431937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9432192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9432264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9432329,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9432778,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9432786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9433017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9433019,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9433228,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9433893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9433984,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9434450,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9434686,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9434762,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9435335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9485375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9842134,
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
    "date_created": "2026-07-06T03:47:05Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:47:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:47:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:50:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:47:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Vega v. Tekoh

```
(Slip Opinion)              OCTOBER TERM, 2021                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                               VEGA v. TEKOH

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE NINTH CIRCUIT

       No. 21–499.      Argued April 20, 2022—Decided June 23, 2022
The case arose out of the interrogation of respondent, Terence Tekoh, by
  petitioner, Los Angeles County Sheriff ’s Deputy Carlos Vega. Deputy
  Vega questioned Tekoh at the medical center where Tekoh worked re-
  garding the reported sexual assault of a patient. Vega did not inform
  Tekoh of his rights under Miranda v. Arizona, 384 U. S. 436. Tekoh
  eventually provided a written statement apologizing for inappropri-
  ately touching the patient’s genitals. Tekoh was prosecuted for unlaw-
  ful sexual penetration. His written statement was admitted against
  him at trial. After the jury returned a verdict of not guilty, Tekoh sued
  Vega under 42 U. S. C. §1983, seeking damages for alleged violations
  of his constitutional rights. The Ninth Circuit held that the use of an
  un-Mirandized statement against a defendant in a criminal proceed-
  ing violates the Fifth Amendment and may support a §1983 claim
  against the officer who obtained the statement.
Held: A violation of the Miranda rules does not provide a basis for a
 §1983 claim. Pp. 4–16.
    (a) Section 1983 provides a cause of action against any person acting
 under color of state law who “subjects” a person “to the deprivation of
 any rights, privileges, or immunities secured by the Constitution and
 laws.” Tekoh argues that a violation of Miranda constitutes a violation
 of the Fifth Amendment right against compelled self-incrimination.
 That is wrong. Pp. 4–13.
    (1) In Miranda, the Court concluded that additional procedural pro-
 tections were necessary to prevent the violation of the Fifth Amend-
 ment right against self-incrimination when suspects who are in cus-
 tody are interrogated by the police. Miranda imposed a set of
 prophylactic rules requiring that custodial interrogation be preceded
2                             VEGA v. TEKOH

                                  Syllabus

    by now-familiar warnings and disallowing the use of statements ob-
    tained in violation of these new rules by the prosecution in its case-in-
    chief. 384 U. S., at 444, 479. Miranda did not hold that a violation of
    the rules it established necessarily constitute a Fifth Amendment vio-
    lation. That makes sense, as an un-Mirandized suspect in custody may
    make self-incriminating statements without any hint of compulsion.
    The Miranda Court stated that the Constitution did not itself require
    “adherence to any particular solution for the inherent compulsions of
    the interrogation process” and that its decision “in no way create[d] a
    constitutional straitjacket.” Id., at 467. Since Miranda, the Court has
    repeatedly described Miranda rules as “prophylactic.” Pp. 4–7.
       (2) After Miranda, the Court engaged in the process of charting the
    dimensions of these new prophylactic rules, and, in doing so, weighed
    the benefits and costs of any clarification of the prophylactic rules’
    scope. See Maryland v. Shatzer, 559 U. S. 98, 106. Some post-Mi-
    randa decisions found that the balance of interests justified re-
    strictions that would not have been possible if Miranda described the
    Fifth Amendment right as opposed to a set of rules designed to protect
    that right. For example, in Harris v. New York, 401 U. S. 222, 224–
    226, the Court held that a statement obtained in violation of Miranda
    could be used to impeach the testimony of a defendant, even though an
    involuntary statement obtained in violation of the Fifth Amendment
    could not have been employed in this way. In Michigan v. Tucker, 417
    U. S. 443, 450–452, n. 26, the Court held that the “fruits” of an un-
    Mirandized statement can be admitted. In doing so, the Court distin-
    guished police conduct that “abridge[s] [a person’s] constitutional priv-
    ilege against compulsory self-incrimination” from conduct that “de-
    part[s] only from the prophylactic standards later laid down by this
    Court in Miranda to safeguard that privilege.” 417 U. S., at 445–446.
    Similarly, in Oregon v. Elstad, 470 U. S. 298, the Court, following the
    reasoning in Tucker, refused to exclude a signed confession and em-
    phasized that an officer’s error “in administering the prophylactic Mi-
    randa procedures . . . should not breed the same irremediable conse-
    quences as police infringement of the Fifth Amendment itself.” Id., at
    309.
       While many of the Court’s decisions imposed limits on Miranda’s
    prophylactic rules, other decisions found that the balance of interests
    called for expansion. For example, in Doyle v. Ohio, 426 U. S. 610, the
    Court held that silence following a Miranda warning cannot be used
    to impeach. The Court acknowledged that Miranda warnings are
    “prophylactic,” 426 U. S., at 617, but it found that allowing the use of
    post-warning silence would undermine the warnings’ implicit promise
    that silence would not be used to convict. Id., at 618. Likewise, in
    Withrow v. Williams, 507 U. S. 680, the Court rejected an attempt to
                    Cite as: 597 U. S. ____ (2022)                      3

                               Syllabus

restrict Miranda’s application in collateral proceedings based on the
reasoning in Stone v. Powell, 428 U. S. 465 (1976). Once again ac-
knowledging that Miranda adopted prophylactic rules, the Court bal-
anced the competing interests and found that the costs of adopting a
Stone-like rule outweighed any benefits. In sum, the Court’s post-Mi-
randa cases acknowledge the prophylactic nature of the Miranda rules
and engage in cost-benefit analysis to define their scope. Pp. 7–11.
    (3) The Court’s decision in Dickerson v. United States, 530 U. S. 428,
did not upset the firmly established prior understanding of Miranda
as a prophylactic decision. Dickerson involved a federal statute, 18
U. S. C. §3501, that effectively overruled Miranda by making the ad-
missibility of a statement given during custodial interrogation turn
solely on whether it was made voluntarily. 530 U. S., at 431–432. The
Court held that Congress could not abrogate Miranda by statute be-
cause Miranda was a “constitutional decision” that adopted a “consti-
tutional rule,” 530 U. S., at 438–439, and the Court noted that these
rules could not have been made applicable to the States if they did not
have that status, see ibid. At the same time, the Court made it clear
that it was not equating a violation of the Miranda rules with an out-
right Fifth Amendment violation. Instead, the Dickerson Court de-
scribed the Miranda rules as “constitutionally based” with “constitu-
tional underpinnings,” 530 U. S., at 440, and n. 5. Those formulations
obviously avoided saying that a Miranda violation is the same as a
violation of the Fifth Amendment right. Miranda was a “constitutional
decision” and it adopted a “constitutional rule” in the sense that the
decision was based on the Court’s judgment about what is required to
safeguard that constitutional right. And when the Court adopts a con-
stitutional prophylactic rule of this nature, Dickerson concluded, the
rule has the status of a “La[w] of the United States” that is binding on
the States under the Supremacy Clause (as Miranda implicitly held,
since three of the four decisions it reversed came from state court, 384
U. S., at 491–494, 497–499), and the rule cannot be altered by ordinary
legislation. Dickerson thus asserted a bold and controversial claim—
that this Court has the authority to create constitutionally based
prophylactic rules that bind both federal and state courts—but Dick-
erson cannot be understood any other way consistent with the Court’s
prior decisions. Subsequent cases confirm that Dickerson did not up-
end the Court’s understanding of the Miranda rules as prophylactic.
In sum, a violation of Miranda does not necessarily constitute a viola-
tion of the Constitution, and therefore such a violation does not consti-
tute “the deprivation of [a] right . . . secured by the Constitution” for
purposes of §1983. Pp. 11–13.
    (b) A §1983 claim may also be based on “the deprivation of any rights
. . . secured by the . . . laws.” But the argument that Miranda rules
4                             VEGA v. TEKOH

                                  Syllabus

    constitute federal “law” that can provide the ground for a §1983 claim
    cannot succeed unless Tekoh can persuade the Court that this “law”
    should be expanded to include the right to sue for damages under
    §1983. “A judicially crafted” prophylactic rule should apply “only
    where its benefits outweigh its costs,” Shatzer, 559 U. S., at 106. Here,
    while the benefits of permitting the assertion of Miranda claims under
    §1983 would be slight, the costs would be substantial. For example,
    allowing a claim like Tekoh’s would disserve “judicial economy,” Park-
    lane Hosiery Co. v. Shore, 439 U. S. 322, 326, by requiring a federal
    judge or jury to adjudicate a factual question (whether Tekoh was in
    custody when questioned) that had already been decided by a state
    court. Allowing §1983 suits based on Miranda claims could also pre-
    sent many procedural issues. Miranda and its progeny provide suffi-
    cient protection for the Fifth Amendment right against compelled self-
    incrimination. Pp. 13–16.
985 F. 3d 713, reversed and remanded.

   ALITO, J., delivered the opinion of the Court, in which ROBERTS, C. J.,
and THOMAS, GORSUCH, KAVANAUGH, and BARRETT, JJ., joined. KAGAN,
J., filed a dissenting opinion, in which BREYER and SOTOMAYOR, JJ.,
joined.
                        Cite as: 597 U. S. ____ (2022)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 21–499
                                    _________________


 CARLOS VEGA, PETITIONER v. TERENCE B. TEKOH
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE NINTH CIRCUIT
                                  [June 23, 2022]

   JUSTICE ALITO delivered the opinion of the Court.
   This case presents the question whether a plaintiff may
sue a police officer under Rev. Stat. §1979, 42 U. S. C.
§1983, based on the allegedly improper admission of an “un-
Mirandized”1 statement in a criminal prosecution. The case
arose out of the interrogation of respondent, Terence Tekoh,
by petitioner, Los Angeles County Sheriff ’s Deputy Carlos
Vega. Deputy Vega questioned Tekoh at his place of em-
ployment and did not give him a Miranda warning. Tekoh
was prosecuted, and his confession was admitted into evi-
dence, but the jury returned a verdict of not guilty. Tekoh
then sued Vega under §1983, and the United States Court
of Appeals for the Ninth Circuit held that the use of Tekoh’s
un-Mirandized statement provided a valid basis for a §1983
claim against Vega. We now reject this extension of our
Miranda case law.
                             I
  In March 2014, Tekoh was working as a certified nursing
assistant at a Los Angeles medical center. When a female
patient accused him of sexually assaulting her, the hospital
——————
 1 See Miranda v. Arizona, 384 U. S. 436 (1966).
2                      VEGA v. TEKOH

                     Opinion of the Court

staff reported the accusation to the Los Angeles County
Sheriff ’s Department, and Deputy Vega responded. Vega
questioned Tekoh at length in the hospital, and Tekoh even-
tually provided a written statement apologizing for inap-
propriately touching the patient’s genitals. The parties dis-
pute whether Vega used coercive investigatory techniques
to extract the statement, but it is undisputed that he never
informed Tekoh of his rights under Miranda v. Arizona, 384
U. S. 436 (1966), which held that during a custodial inter-
rogation police officers must inform a suspect that “he has
the right to remain silent, that anything he says can be used
against him in a court of law, that he has the right to the
presence of an attorney, and that if he cannot afford an at-
torney one will be appointed for him prior to any question-
ing.” Id., at 479.
   Tekoh was arrested and charged in California state court
with unlawful sexual penetration. At Tekoh’s first trial, the
judge held that Miranda had not been violated because
Tekoh was not in custody when he provided the statement,
but the trial resulted in a mistrial. When Tekoh was re-
tried, a second judge again denied his request to exclude the
confession. This trial resulted in acquittal, and Tekoh then
brought this action under 42 U. S. C. §1983 against Vega
and several other defendants seeking damages for alleged
violations of his constitutional rights, including his Fifth
Amendment right against compelled self-incrimination.
   When this §1983 case was first tried, the jury returned a
verdict in favor of Vega, but the judge concluded that he had
given an improper jury instruction and thus granted a new
trial. Before the second trial, Tekoh asked the court to in-
struct the jury that it was required to find that Vega vio-
lated the Fifth Amendment right against compelled self-
incrimination if it determined that he took a statement
from Tekoh in violation of Miranda and that the statement
was then improperly used against Tekoh at his criminal
trial. The District Court declined, reasoning that Miranda
                 Cite as: 597 U. S. ____ (2022)            3

                     Opinion of the Court

established a prophylactic rule and that such a rule could
not alone provide a ground for §1983 liability. Instead, the
jury was asked to decide whether Tekoh’s Fifth Amendment
right had been violated. The court instructed the jury to
determine, based on “the totality of all the surrounding cir-
cumstances,” whether Tekoh’s statement had been “im-
properly coerced or compelled,” and the court explained
that “[a] confession is improperly coerced or compelled . . .
if a police officer uses physical or psychological force or
threats not permitted by law to undermine a person’s abil-
ity to exercise his or her free will.” App. to Pet. for Cert.
119a. The jury found in Vega’s favor, and Tekoh appealed.
   A Ninth Circuit panel reversed, holding that the “use of
an un-Mirandized statement against a defendant in a crim-
inal proceeding violates the Fifth Amendment and may
support a §1983 claim” against the officer who obtained the
statement. Tekoh v. County of Los Angeles, 985 F. 3d 713,
722 (2021). The panel acknowledged that this Court has
repeatedly said that Miranda adopted prophylactic rules
designed to protect against constitutional violations and
that the decision did not hold that the contravention of
those rules necessarily constitutes a constitutional viola-
tion. See 985 F. 3d, at 719–720. But the panel thought that
our decision in Dickerson v. United States, 530 U. S. 428
(2000), “made clear that the right of a criminal defendant
against having an un-Mirandized statement introduced in
the prosecution’s case in chief is indeed a right secured by
the Constitution.” 985 F. 3d, at 720. Therefore the panel
concluded that Tekoh could establish a violation of his Fifth
Amendment right against compelled self-incrimination
simply by showing that Miranda had been violated. See
985 F. 3d, at 720. The panel thus remanded the case for a
new trial.
   Vega’s petition for rehearing en banc was denied, but
Judge Bumatay, joined by six other judges, filed a dissent
4                       VEGA v. TEKOH

                      Opinion of the Court

from the denial of rehearing. Tekoh v. County of Los Ange-
les, 997 F. 3d 1260, 1261, 1264–1272 (CA9 2021). We then
granted certiorari. 595 U. S. ___ (2022).
                               II
   Section 1983 provides a cause of action against any per-
son acting under color of state law who “subjects” a person
or “causes [a person] to be subjected . . . to the deprivation
of any rights, privileges, or immunities secured by the Con-
stitution and laws.” The question we must decide is
whether a violation of the Miranda rules provides a basis
for a claim under §1983. We hold that it does not.
                               A
   If a Miranda violation were tantamount to a violation of
the Fifth Amendment, our answer would of course be differ-
ent. The Fifth Amendment, made applicable to the States
by the Fourteenth Amendment, Malloy v. Hogan, 378 U. S.
1, 6 (1964), provides that “[n]o person . . . shall be compelled
in any criminal case to be a witness against himself.” This
Clause “permits a person to refuse to testify against himself
at a criminal trial in which he is a defendant” and “also
‘privileges him not to answer official questions put to him
in any other proceeding, civil or criminal, formal or infor-
mal, where the answers might incriminate him in future
criminal proceedings.’ ” Minnesota v. Murphy, 465 U. S.
420, 426 (1984) (quoting Lefkowitz v. Turley, 414 U. S. 70,
77 (1973)). In addition, the right bars the introduction
against a criminal defendant of out-of-court statements ob-
tained by compulsion. See, e.g., Bram v. United States, 168
U. S. 532, 565 (1897); Miranda, 384 U. S., at 466; Michigan
v. Tucker, 417 U. S. 433, 440–442 (1974).
   In Miranda, the Court concluded that additional proce-
dural protections were necessary to prevent the violation of
this important right when suspects who are in custody are
interrogated by the police. To afford this protection, the
                 Cite as: 597 U. S. ____ (2022)            5

                     Opinion of the Court

Court required that custodial interrogation be preceded by
the now-familiar warnings mentioned above, and it directed
that statements obtained in violation of these new rules
may not be used by the prosecution in its case-in-chief. 384
U. S., at 444, 479.
  In this case, the Ninth Circuit held—and Tekoh now ar-
gues, Brief for Respondent 20—that a violation of Miranda
constitutes a violation of the Fifth Amendment right
against compelled self-incrimination, but that is wrong.
Miranda itself and our subsequent cases make clear that
Miranda imposed a set of prophylactic rules. Those rules,
to be sure, are “constitutionally based,” Dickerson, 530
U. S., at 440, but they are prophylactic rules nonetheless.
                              B
  Miranda itself was clear on this point. Miranda did not
hold that a violation of the rules it established necessarily
constitute a Fifth Amendment violation, and it is difficult
to see how it could have held otherwise. For one thing, it is
easy to imagine many situations in which an un-
Mirandized suspect in custody may make self-
incriminating statements without any hint of compulsion.
In addition, the warnings that the Court required included
components, such as notification of the right to have re-
tained or appointed counsel present during questioning,
that do not concern self-incrimination per se but are instead
plainly designed to safeguard that right. And the same is
true of Miranda’s detailed rules about the waiver of the
right to remain silent and the right to an attorney. 384
U. S., at 474–479.
  At no point in the opinion did the Court state that a vio-
lation of its new rules constituted a violation of the Fifth
Amendment right against compelled self-incrimination. In-
stead, it claimed only that those rules were needed to safe-
guard that right during custodial interrogation. See id., at
439 (describing its rules as “procedures which assure that
6                      VEGA v. TEKOH

                     Opinion of the Court

the individual is accorded his privilege under the Fifth
Amendment”); id., at 444 (describing rules as “procedural
safeguards”); id., at 457 (“appropriate safeguards”); id., at
458 (“adequate protective devices”); id., at 467 (“safe-
guards”).
   In accordance with this understanding of the nature of
the rules it imposed, the Miranda Court stated quite clearly
that the Constitution did not itself require “adherence to
any particular solution for the inherent compulsions of the
interrogation process” and that its decision “in no way cre-
ate[d] a constitutional straitjacket.” Ibid. The opinion
added that its new rules might not be needed if Congress or
the States adopted “other procedures which are at least as
effective,” ibid., and the opinion suggested that there might
not have been any actual Fifth Amendment violations in
the four cases that were before the Court. See id., at 457
(“In these cases, we might not find the defendants’ state-
ments to have been involuntary in traditional terms”). The
Court could not have said any of these things if a violation
of the Miranda rules necessarily constituted a violation of
the Fifth Amendment.
   Since Miranda, the Court has repeatedly described the
rules it adopted as “prophylactic.” See Howes v. Fields, 565
U. S. 499, 507 (2012); J. D. B. v. North Carolina, 564 U. S.
261, 269 (2011); Maryland v. Shatzer, 559 U. S. 98, 103
(2010); Montejo v. Louisiana, 556 U. S. 778, 794 (2009); Da-
vis v. United States, 512 U. S. 452, 458 (1994); Brecht v.
Abrahamson, 507 U. S. 619, 629 (1993); Withrow v. Wil-
liams, 507 U. S. 680, 691 (1993); McNeil v. Wisconsin, 501
U. S. 171, 176 (1991); Michigan v. Harvey, 494 U. S. 344,
350 (1990); Duckworth v. Eagan, 492 U. S. 195, 203 (1989);
Arizona v. Roberson, 486 U. S. 675, 681 (1988); Connecticut
v. Barrett, 479 U. S. 523, 528 (1987); Oregon v. Elstad, 470
U. S. 298, 309 (1985); New York v. Quarles, 467 U. S. 649,
654 (1984); South Dakota v. Neville, 459 U. S. 553, 564, n.
15 (1983); United States v. Henry, 447 U. S. 264, 274 (1980);
                      Cite as: 597 U. S. ____ (2022)                     7

                          Opinion of the Court

North Carolina v. Butler, 441 U. S. 369, 374 (1979); Brown
v. Illinois, 422 U. S. 590, 600 (1975); Michigan v. Tucker,
417 U. S., at 439; and Michigan v. Payne, 412 U. S. 47, 53
(1973).2
                               C
   After Miranda was handed down, the Court engaged in
the process of charting the dimensions of these new prophy-
lactic rules. As we would later spell out, this process en-
tailed a weighing of the benefits and costs of any clarifica-
tion of the rules’ scope. See Shatzer, 559 U. S., at 106 (“A
judicially crafted rule is ‘justified only by reference to its
prophylactic purpose,’ . . . and applies only where its bene-
fits outweigh its costs”).
   Some post-Miranda decisions found that the balance of
interests justified restrictions that would not have been
possible if Miranda represented an explanation of the
meaning of the Fifth Amendment right as opposed to a set
of rules designed to protect that right. For example, in Har-
ris v. New York, 401 U. S. 222, 224–226 (1971), the Court
held that a statement obtained in violation of Miranda
could be used to impeach the testimony of a defendant, even
though an involuntary statement obtained in violation of
the Fifth Amendment could not have been employed in this
way. See Mincey v. Arizona, 437 U. S. 385, 398 (1978)

——————
   2 Tekoh cites Orozco v. Texas, 394 U. S. 324 (1969), which characterized

the admission of an unwarned statement in the prosecutor’s case-in-chief
as a “flat violation of the Self-Incrimination Clause of the Fifth Amend-
ment as construed in Miranda.” Id., at 326 (emphasis added); Brief for
Respondent 21, 29. But the Court made this assertion in a three-para-
graph opinion without any additional analysis, and did not purport to go
beyond Miranda, which, as we have explained, does not support the prop-
osition that a Miranda violation equates to a Fifth Amendment violation.
See Orozco, 394 U. S., at 327 (“We do not . . . expand or extend to the
slightest extent our Miranda decision”). Likewise, the decision predates
the subsequent case law defining the scope of the Miranda rules. See
infra, this page and 8–11.
8                      VEGA v. TEKOH

                      Opinion of the Court

(“[A]ny criminal trial use against a defendant of his invol-
untary statement is a denial of due process of law” (empha-
sis deleted)). Engaging in the process we described in
Shatzer, the Harris Court considered the benefits of forbid-
ding impeachment but dismissed “the speculative possibil-
ity” that this would discourage “impermissible police con-
duct,” and on the other side of the scale, it feared that
barring impeachment would turn Miranda into “a license
to use perjury by way of a defense.” 401 U. S., at 225–226.
   A similar analysis was used in Michigan v. Tucker, 417
U. S. 443, 450–452, n. 26 (1974), where the Court held that
the “fruits” of an un-Mirandized statement can be admit-
ted. The Court noted that “the ‘fruits’ of police conduct
which actually infringe[s]” a defendant’s constitutional
rights must be suppressed. Id., at 445; see also Wong Sun
v. United States, 371 U. S. 471 (1963) (applying the rule in
the context of a Fourth Amendment violation). But the
Court distinguished police conduct that “abridge[s] [a per-
son’s] constitutional privilege against compulsory self-
incrimination” from conduct that “depart[s] only from the
prophylactic standards later laid down by this Court in Mi-
randa to safeguard that privilege.” 417 U. S., at 445–446.
Because there had been only a Miranda violation in that
case, the Wong Sun rule of automatic exclusion was found
to be inapplicable. See 417 U. S., at 445–446. Instead, the
Court asked whether the Miranda rules’ prophylactic pur-
poses justified the exclusion of the fruits of the violation,
and after “balancing the interests involved,” it held that ex-
clusion was not required. 417 U. S., at 447–452.
   In New York v. Quarles, 467 U. S. 649, 654–657 (1984),
the Court held that statements obtained in violation of Mi-
randa need not be suppressed when the questioning is con-
ducted to address an ongoing “public safety” concern. The
Court reasoned that Miranda warnings are “ ‘not them-
selves rights protected by the Constitution’ ” and that “the
need for answers to questions in a situation posing a threat
                      Cite as: 597 U. S. ____ (2022)                      9

                           Opinion of the Court

to the public safety outweigh[ed] the need for the prophy-
lactic rule.” 467 U. S., at 654, 657.
   Finally, in Elstad, 470 U. S. 298, the Court again distin-
guished between a constitutional violation and a violation
of Miranda. In that case, a suspect in custody was initially
questioned without receiving a Miranda warning, and the
statements made at that time were suppressed. 470 U. S.,
at 301–302. But the suspect was later given Miranda warn-
ings, chose to waive his Miranda rights, and signed a writ-
ten confession. 470 U. S., at 301. Asked to decide whether
this confession was admissible, the Court followed the rea-
soning in Tucker and again held that the fruit-of-the-
poisonous-tree rule that applies to constitutional violations
does not apply to violations of Miranda. 470 U. S., at 306–
309, 318. The Court refused to exclude the signed confes-
sion and emphasized that an officer’s error “in administer-
ing the prophylactic Miranda procedures . . . should not
breed the same irremediable consequences as police in-
fringement of the Fifth Amendment itself.” 3 Id., at 309.



——————
   3 Two other decisions fall into this same category, but in both there was

no opinion of the Court. In Chavez v. Martinez, 538 U. S. 760 (2003), the
suspect gave an un-Mirandized statement while in custody but was
never charged with a crime. The Court held that the suspect could not
bring a 42 U. S. C. §1983 claim against the officer who questioned him,
and Justice Souter, who cast the necessary fifth vote on the issue,
reached that conclusion based on “a realistic assessment of costs and
risks” of “expand[ing] protection of the privilege against compelled self-
incrimination to the point of the civil liability” at issue. 538 U. S., at
778–779 (opinion concurring in judgment).
   In United States v. Patane, 542 U. S. 630 (2004), the Court once again
held that Miranda does not require the suppression of the fruits of a un-
Mirandized statement made during custodial questioning, and two of the
five Justices in the majority engaged in the same type of balancing that
was used in Michigan v. Tucker, 417 U. S. 433 (1974), and Elstad. See
Patane, 542 U. S., at 644–645 (Kennedy, J., concurring in judgment); see
also id., at 641–644 (plurality opinion).
10                     VEGA v. TEKOH

                     Opinion of the Court

  It is hard to see how these decisions could stand if a vio-
lation of Miranda constituted a violation of the Fifth
Amendment.
                              D
   While these decisions imposed limits on Miranda’s
prophylactic rules, other decisions found that the balance of
interests called for expansion. In Doyle v. Ohio, 426 U. S.
610, 617–619 (1976), the Court held that silence following a
Miranda warning cannot be used to impeach. The Court
acknowledged that Miranda warnings are “prophylactic,”
426 U. S., at 617, and it recognized the prosecution’s need
to test a defendant’s exculpatory story through cross-
examination, id., at 616–618. But it found that allowing
the use of post-warning silence would undermine the warn-
ings’ implicit promise that silence would not be used to con-
vict. Id., at 618.
   Similarly, in Roberson, 486 U. S., at 682, the Court held
that a suspect’s post-warning request for counsel with re-
spect to one offense barred later interrogation without
counsel regarding a different offense. Describing the Mi-
randa rules as “prophylactic protections,” 486 U. S., at 681,
the Court concluded that both law enforcement and crimi-
nal defendants would benefit from a bright-line, id., at 681–
682.
   Finally, in Withrow v. Williams, 507 U. S. 680, the Court
rejected an attempt to restrict Miranda’s application in col-
lateral proceedings based on the reasoning in Stone v. Pow-
ell, 428 U. S. 465 (1976). In Stone, the Court had held that
a defendant who has had a full and fair opportunity to seek
suppression of evidence allegedly seized in violation of the
Fourth Amendment may not obtain federal habeas relief on
that ground, id., at 494–495, and in Withrow, a state prison
warden argued that a similar rule should apply to a habeas
petitioner who had been given an opportunity to litigate a
Miranda claim at trial, see 507 U. S., at 688–690. Once
                  Cite as: 597 U. S. ____ (2022)           11

                      Opinion of the Court

again acknowledging that Miranda adopted prophylactic
rules, the Court balanced the competing interests and
found that the costs of adopting the warden’s argument out-
weighed any benefits. On the cost side, the Court noted
that enforcing Miranda “safeguards ‘a fundamental trial
right” and furthers “the correct ascertainment of guilt” at
trial. 507 U. S., at 691–692. And on the other side, the
Court found that the adoption of a Stone-like rule “would
not significantly benefit the federal courts in their exercise
of habeas jurisdiction, or advance the cause of federalism in
any substantial way.” 507 U. S., at 693.
   Thus, all the post-Miranda cases we have discussed
acknowledged the prophylactic nature of the Miranda rules
and engaged in cost-benefit analysis to define the scope of
these prophylactic rules.
                              E
   Contrary to the decision below and Tekoh’s argument
here, see Brief for Respondent 24, our decision in Dickerson,
530 U. S. 428, did not upset the firmly established prior un-
derstanding of Miranda as a prophylactic decision. Dicker-
son involved a federal statute, 18 U. S. C. §3501, that effec-
tively overruled Miranda by making the admissibility of a
statement given during custodial interrogation turn solely
on whether it was made voluntarily. 530 U. S., at 431–432.
The Court held that Congress could not abrogate Miranda
by statute because Miranda was a “constitutional decision”
that adopted a “constitutional rule,” 530 U. S., at 438–439,
and the Court noted that these rules could not have been
made applicable to the States if it did not have that status,
see ibid.
   At the same time, however, the Court made it clear that
it was not equating a violation of the Miranda rules with
an outright Fifth Amendment violation. For one thing, it
reiterated Miranda’s observation that “the Constitution
would not preclude legislative solutions that differed from
12                          VEGA v. TEKOH

                           Opinion of the Court

the prescribed Miranda warnings but which were ‘at least
as effective in apprising accused persons’ ” of their rights.
530 U. S., at 440 (quoting Miranda, 384 U. S., at 467).
  Even more to the point, the Court rejected the dissent’s
argument that §3501 could not be held unconstitutional un-
less “Miranda warnings are required by the Constitution,
in the sense that nothing else will suffice to satisfy consti-
tutional requirements.” 530 U. S., at 442. The Court’s an-
swer, in substance, was that the Miranda rules, though not
an explication of the meaning of the Fifth Amendment
right, are rules that are necessary to protect that right (at
least until a better alternative is found and adopted). See
530 U. S., at 441–443. Thus, in the words of the Dickerson
Court, the Miranda rules are “constitutionally based” and
have “constitutional underpinnings.” 530 U. S., at 440, and
n. 5. But the obvious point of these formulations was to
avoid saying that a Miranda violation is the same as a vio-
lation of the Fifth Amendment right.
  What all this boils down to is basically as follows. The
Miranda rules are prophylactic rules that the Court found
to be necessary to protect the Fifth Amendment right
against compelled self-incrimination. In that sense, Mi-
randa was a “constitutional decision” and it adopted a “con-
stitutional rule” because the decision was based on the
Court’s judgment about what is required to safeguard that
constitutional right. And when the Court adopts a consti-
tutional prophylactic rule of this nature, Dickerson con-
cluded, the rule has the status of a “La[w] of the United
States” that is binding on the States under the Supremacy
Clause 4 (as Miranda implicitly held, since three of the four
decisions it reversed came from state court, 384 U. S., at
491–494, 497–499), and the rule cannot be altered by ordi-
nary legislation.

——————
 4 U. S. Const., Art. VI, §2.
                     Cite as: 597 U. S. ____ (2022)                    13

                          Opinion of the Court

  This was a bold and controversial claim of authority,5 but
we do not think that Dickerson can be understood any other
way without (1) taking the insupportable position that a
Miranda violation is tantamount to a violation of the Fifth
Amendment, (2) calling into question the prior decisions
that were predicated on the proposition that a Miranda vi-
olation is not the same as a constitutional violation, and (3)
excising from the United States Reports a mountain of
statements describing the Miranda rules as prophylactic.
  Subsequent cases confirm that Dickerson did not upend
the Court’s understanding of the Miranda rules as prophy-
lactic. See, e.g., supra, at 6–7 (collecting post-Dickerson
cases).
  In sum, a violation of Miranda does not necessarily con-
stitute a violation of the Constitution, and therefore such a
violation does not constitute “the deprivation of [a] right . . .
secured by the Constitution.” 42 U. S. C. §1983.
                              III
  This conclusion does not necessarily dictate reversal be-
cause a §1983 claim may also be based on “the deprivation
of any rights, privileges, or immunities secured by the . . .
laws.” (Emphasis added.) It may thus be argued that the
Miranda rules constitute federal “law” and that an abridg-
ment of those rules can therefore provide the ground for a


——————
   5 Whether this Court has the authority to create constitutionally based

prophylactic rules that bind both federal and state courts has been the
subject of debate among jurists and commentators. See, e.g., Dickerson,
530 U. S., at 445–446, 457–461 (Scalia, J., joined by THOMAS, J., dissent-
ing); D. Strauss, The Ubiquity of Prophylactic Rules, 55 U. Chi. L. Rev.
190 (1988); J. Grano, Prophylactic Rules in Criminal Procedure: A Ques-
tion of Article III Legitimacy, 80 Nw. U. L. Rev. 100 (1985); H. Mona-
ghan, Foreword: Constitutional Common Law, 89 Harv. L. Rev. 1 (1975).
But that is what the Court did in Miranda, and we do not disturb that
decision in any way. Rather, we accept it on its own terms, and for the
purpose of deciding this case, we follow its rationale.
14                           VEGA v. TEKOH

                           Opinion of the Court

§1983 claim. But whatever else may be said about this ar-
gument,6 it cannot succeed unless Tekoh can persuade us
that this “law” should be expanded to include the right to
sue for damages under §1983.
   As we have noted, “[a] judicially crafted” prophylactic
rule should apply “only where its benefits outweigh its
costs,” Shatzer, 559 U. S., at 106, and here, while the bene-
fits of permitting the assertion of Miranda claims under
§1983 would be slight, the costs would be substantial.
   Miranda rests on a pragmatic judgment about what is
needed to stop the violation at trial of the Fifth Amendment
right against compelled self-incrimination. That prophy-
lactic purpose is served by the suppression at trial of state-


——————
   6 “[Section] 1983 does not provide an avenue for relief every time a state

actor violates a federal law.” Rancho Palos Verdes v. Abrams, 544 U. S.
113, 119 (2005). If a §1983 plaintiff demonstrates that the federal stat-
ute “creates an individually enforceable right in the class of beneficiaries
to which he belongs,” this gives rise to “ ‘a rebuttable presumption that
the right is enforceable under §1983,’ ” and “[t]he defendant may defeat
this presumption by demonstrating that Congress did not intend that
remedy for a newly created right.” Id., at 120 (quoting Blessing v. Free-
stone, 520 U. S. 329, 341 (1997)). In this case, the “law” that could confer
the right in question is not a statute but judicially created prophylactic
rules. It could be argued that a judicially created prophylactic rule can-
not be the basis for a §1983 suit, but we need not decide that question
because, assuming that such rules can provide the basis for a §1983
claim, we would be led back to a question that is very much like the one
discussed supra, at 7–11, namely, whether the benefits of allowing such
a claim outweigh the costs.
   The dissent, by contrast, would apparently hold that a prophylactic
rule crafted by the Judiciary to protect a constitutional right, unlike a
statute that confers a personal right, is always cognizable under §1983.
There is no sound reason to give this preferred status to such prophylac-
tic rules. The dissent contends that the Miranda rules merit this special
treatment because they are “secured by” the Constitution, see post, at 5–
6, but in fact, as we have shown, those rules differ from the right secured
by the Fifth Amendment and are instead secured for prophylactic rea-
sons by decisions of this Court.
                  Cite as: 597 U. S. ____ (2022)           15

                      Opinion of the Court

ments obtained in violation of Miranda and by the applica-
tion of that decision in other recognized contexts. Allowing
the victim of a Miranda violation to sue a police officer for
damages under §1983 would have little additional deter-
rent value, and permitting such claims would cause many
problems.
   Allowing a claim like Tekoh’s would disserve “judicial
economy,” Parklane Hosiery Co. v. Shore, 439 U. S. 322, 326
(1979), by requiring a federal judge or jury to adjudicate a
factual question (whether Tekoh was in custody when ques-
tioned) that had already been decided by a state court. This
re-adjudication would not only be wasteful; it would under-
cut the “ ‘strong judicial policy against the creation of two
conflicting resolutions’ ” based on the same set of facts.
Heck v. Humphrey, 512 U. S. 477, 484 (1994). And it could
produce “unnecessary friction” between the federal and
state court systems by requiring the federal court enter-
taining the §1983 claim to pass judgment on legal and fac-
tual issues already settled in state court. See Preiser v. Ro-
driguez, 411 U. S. 475, 490–491 (1973).
   Allowing §1983 suits based on Miranda claims could also
present many procedural issues, such as whether a federal
court considering a §1983 claim would owe any deference to
a trial court’s factual findings; whether forfeiture and plain
error rules carry over from the criminal trial; whether
harmless-error rules apply; and whether civil damages are
available in instances where the unwarned statement had
no impact on the outcome of the criminal case.
   We therefore refuse to extend Miranda in the way Tekoh
requests. Miranda, Dickerson, and the other cases in that
line provide sufficient protection for the Fifth Amendment
right against compelled self-incrimination. “The identifica-
tion of a Miranda violation and its consequences . . . ought
to be determined at trial.” Chavez v. Martinez, 538 U. S.
760, 790 (2003) (Kennedy, J., concurring in part and dis-
senting in part). And except in unusual circumstances, the
16                     VEGA v. TEKOH

                     Opinion of the Court

“exclusion of unwarned statements” should be “a complete
and sufficient remedy.” Ibid.
                       *    *     *
  Because a violation of Miranda is not itself a violation of
the Fifth Amendment, and because we see no justification
for expanding Miranda to confer a right to sue under §1983,
the judgment of the Court of Appeals is reversed, and the
case is remanded for further proceedings consistent with
this opinion.
                                            It is so ordered.
                  Cite as: 597 U. S. ____ (2022)             1

                      KAGAN, J., dissenting

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 21–499
                          _________________


CARLOS VEGA, PETITIONER v. TERENCE B. TEKOH
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE NINTH CIRCUIT
                         [June 23, 2022]

   JUSTICE KAGAN, with whom JUSTICE BREYER and
JUSTICE SOTOMAYOR join, dissenting.
   The Court’s decision in Miranda v. Arizona, 384 U. S. 436
(1966), affords well-known protections to suspects who are
interrogated by police while in custody. Those protections
derive from the Constitution: Dickerson v. United States
tells us in no uncertain terms that Miranda is a “constitu-
tional rule.” 530 U. S. 428, 444 (2000). And that rule grants
a corresponding right: If police fail to provide the Miranda
warnings to a suspect before interrogating him, then he is
generally entitled to have any resulting confession excluded
from his trial. See 384 U. S., at 478–479. From those facts,
only one conclusion can follow—that Miranda’s protections
are a “right[ ]” “secured by the Constitution” under the fed-
eral civil rights statute. Rev. Stat. §1979, 42 U. S. C. §1983.
Yet the Court today says otherwise. It holds that Miranda
is not a constitutional right enforceable through a §1983
suit. And so it prevents individuals from obtaining any re-
dress when police violate their rights under Miranda. I re-
spectfully dissent.
   Miranda responded to problems stemming from the in-
terrogation of suspects “incommunicado” and “in a police-
dominated atmosphere.” Miranda, 384 U. S., at 445. In
such an environment, Miranda said, there are “pressures”
which may “compel [a suspect] to speak where he would not
otherwise do so freely.” Id., at 467. And so Miranda found
2                       VEGA v. TEKOH

                      KAGAN, J., dissenting

a “necessity for procedures which assure that the individual
is accorded his” Fifth Amendment privilege “not to be com-
pelled to incriminate himself.” Id., at 439. Miranda set out
protocols (including the now-familiar warnings) that would
safeguard the constitutional privilege against self-incrimi-
nation. See id., at 478–479. And Miranda held that if po-
lice failed to follow those requirements (without substitut-
ing equally effective ones), the prosecution could not use at
trial a statement obtained from the interrogation. See id.,
at 479.
   The question in this case is whether Miranda’s protec-
tions are a “right[ ]” that is “secured by the Constitution”
within the meaning of §1983. If the answer is yes, then a
person may sue a state actor who deprives him of the right.
In past cases, the Court has given a broad construction to
§1983’s broad language. See, e.g., Dennis v. Higgins, 498
U. S. 439, 443 (1991). Under §1983 (as elsewhere), a
“right[ ]” is anything that creates specific “obligations bind-
ing on [a] governmental unit” that an individual may ask
the judiciary to enforce. Id., at 449; see id., at 447, and n. 7.
And the phrase “secured by the Constitution” also has a ca-
pacious meaning. It refers to any right that is “protect[ed]
or ma[de] certain” by the country’s foundational charter.
Hague v. Committee for Industrial Organization, 307 U. S.
496, 527 (1939) (opinion of Stone, J.) (internal quotation
marks omitted).
   Begin with whether Miranda is “secured by the Constitu-
tion.” We know that it is, because the Court’s decision in
Dickerson says so. Dickerson tells us again and again that
Miranda is a “constitutional rule.” 530 U. S., at 444. It is
a “constitutional decision” that sets forth “ ‘concrete consti-
tutional guidelines.’ ” Id., at 432, 435 (quoting Miranda,
384 U. S., at 442). Miranda “is constitutionally based”; or
again, it has a “constitutional basis.” 530 U. S., at 439, n. 3,
440. It is “of constitutional origin”; it has “constitutional
underpinnings.” Id., at 439, n. 3, 440, n. 5. And—one
                      Cite as: 597 U. S. ____ (2022)                     3

                          KAGAN, J., dissenting

more—Miranda sets a “constitutional minimum.” 530
U. S., at 442. Over and over, Dickerson labels Miranda a
rule stemming from the Constitution.
   Dickerson also makes plain that Miranda has all the sub-
stance of a constitutional rule—including that it cannot be
“abrogate[d]” by any “legislation.” Miranda, 384 U. S., at
491; see Dickerson, 530 U. S., at 437. In Dickerson, the
Court considered a federal statute whose obvious purpose
was to override Miranda. Dickerson held that Miranda is
a “constitutional decision” that cannot be “overruled by”
any “Act of Congress.” 530 U. S., at 432. To be sure, Con-
gress may devise “legislative solutions that differ[ ] from the
prescribed Miranda warnings,” but only if those solutions
are “ ‘at least as effective.’ ” Id., at 440 (quoting Miranda,
384 U. S., at 467). Dickerson therefore instructs (as noted
above) that Miranda sets a “constitutional minimum.” 530
U. S., at 442. No statute may provide lesser protection than
that baseline.*
   And Dickerson makes clear that the constitutional sub-
stance of Miranda does not end there. Rules arising from
“the United States Constitution” are applicable in state-
court proceedings, but non-constitutional rules are not. See
530 U. S., at 438 (explaining that the Court “do[es] not hold
a supervisory power over the courts of the several States”).
Too, constitutional rules are enforceable in federal-court
habeas proceedings, where a prisoner is entitled to claim he
“is in custody in violation of the Constitution.” 28 U. S. C.
——————
   *Other constitutional rules, like Miranda, leave room for States to ex-
periment with procedures, so long as the procedures satisfy the constitu-
tionally mandated baseline. See County of Riverside v. McLaughlin, 500
U. S. 44, 58 (1991) (States may adopt different procedures for providing
probable-cause determinations for persons arrested without a warrant,
so long as those determinations are made promptly); Smith v. Robbins,
528 U. S. 259, 276–277 (2000) (States may adopt different procedures to
ensure effective appellate review for indigent defendants’ claims, “so long
as [the State] reasonably ensures that an indigent’s appeal will be re-
solved in a way that is related to the merit of that appeal”).
4                      VEGA v. TEKOH

                     KAGAN, J., dissenting

§2254(a). Miranda checks both boxes. The Court has “con-
sistently applied Miranda’s rule to prosecutions arising in
state courts.” Dickerson, 530 U. S., at 438. And prisoners
may claim Miranda violations in federal-court habeas pro-
ceedings. See 530 U. S., at 439, n. 3; Thompson v. Keohane,
516 U. S. 99, 107, n. 5 (1995). So Dickerson is unequivocal:
Miranda is set in constitutional stone.
   Miranda’s constitutional rule gives suspects a correlative
“right[ ].” §1983. Under Miranda, a suspect typically has a
right to be tried without the prosecutor using his un-
Mirandized statement. And we know how that right oper-
ates in the real world. Suppose a defendant standing trial
was able to show the court that he gave an un-Mirandized
confession during a custodial interrogation. The court
would have no choice but to exclude it from the prosecutor’s
case. As one judge below put it: “Miranda indisputably cre-
ates individual legal rights that are judicially enforceable.
(Any prosecutor who doubts this can try to introduce an un-
Mirandized confession and then watch what happens.)”
Tekoh v. County of Los Angeles, 997 F. 3d 1260, 1263 (CA9
2021) (Miller, J., concurring in denial of rehearing en banc).
   The majority basically agrees with everything I’ve just
explained.     It concurs that, per Dickerson, Miranda
“adopted a ‘constitutional rule.’ ” Ante, at 11 (quoting Dick-
erson, 530 U. S., at 439); see ante, at 12. How could it not?
That Miranda is a constitutional rule is what Dickerson
said (and said and said). The majority also agrees that Mi-
randa “directed that statements obtained in violation of
[its] rules may not be used by the prosecution in its case-in-
chief ”—which is simply another way of saying that Mi-
randa grants suspects a right to the exclusion of those
statements from the prosecutor’s case. Ante, at 5.
   So how does the majority hold that a violation of Miranda
is not a “deprivation of [a] right[ ]” “secured by the Consti-
tution”? §1983. How does it agree with my premises, but
                 Cite as: 597 U. S. ____ (2022)            5

                     KAGAN, J., dissenting

not my conclusion? The majority’s argument is that “a vio-
lation of Miranda does not necessarily constitute a violation
of the Constitution,” because Miranda’s rules are “prophy-
lactic.” Ante, at 13. The idea is that the Fifth Amendment
prohibits the use only of statements obtained by compul-
sion, whereas Miranda excludes non-compelled statements
too. See ante, at 4–5. That is why, the majority says, the
Court has been able to recognize exceptions permitting cer-
tain uses of un-Mirandized statements at trial (when it
could not do so for compelled statements). See ante, at 7–9.
   But none of that helps the majority’s case. Let’s assume,
as the majority says, that Miranda extends beyond—in or-
der to safeguard—the Fifth Amendment’s core guarantee.
Still, Miranda is enforceable through §1983. It remains a
constitutional rule, as Dickerson held (and the majority
agrees). And it grants the defendant a legally enforceable
entitlement—in a word, a right—to have his confession ex-
cluded. So, to refer back to the language of §1983, Miranda
grants a “right[ ]” “secured by the Constitution.” Whether
that right to have evidence excluded safeguards a yet
deeper constitutional commitment makes no difference to
§1983. The majority has no response to that point—except
to repeat what our argument assumes already. See ante, at
14, n. 6 (describing Miranda as prophylactic).
   Compare the majority’s holding today to a prior decision,
in which the Court “rejected [an] attempt[ ] to limit the
types of constitutional rights that are encompassed within ”
§1983. Dennis, 498 U. S., at 445. There, the Court held
that a plaintiff could sue under §1983 for a violation of the
so-called dormant Commerce Clause, which safeguards in-
terstate commerce. To the Court, it did not matter that the
Commerce Clause might be viewed as “merely allocat[ing]
power between the Federal and State Governments” over
interstate commerce, rather than as “confer[ring] ‘rights.’ ”
Id., at 447. Nor did it matter that the dormant Commerce
Clause’s protection is only “implied” by the constitutional
6                      VEGA v. TEKOH

                     KAGAN, J., dissenting

text. Ibid., n. 7. The dormant Commerce Clause, the Court
said, still provides a “right”—in the “ordinary” sense of be-
ing “ ‘[a] legally enforceable claim of one person against an-
other.’ ” Ibid. (quoting Black’s Law Dictionary 1324 (6th ed.
1990)). That describes Miranda to a tee. And if a right im-
plied from Congress’s constitutional authority over inter-
state commerce is enforceable under §1983, how could it be
that Miranda—which the Court has found necessary to
safeguard the personal protections of the Fifth Amend-
ment—is not also enforceable? The majority again has no
answer.
                         *     *    *
  Today, the Court strips individuals of the ability to seek
a remedy for violations of the right recognized in Miranda.
The majority observes that defendants may still seek “the
suppression at trial of statements obtained” in violation of
Miranda’s procedures. Ante, at 14–15. But sometimes,
such a statement will not be suppressed. And sometimes,
as a result, a defendant will be wrongly convicted and spend
years in prison. He may succeed, on appeal or in habeas, in
getting the conviction reversed. But then, what remedy
does he have for all the harm he has suffered? The point of
§1983 is to provide such redress—because a remedy “is a
vital component of any scheme for vindicating cherished
constitutional guarantees.” Gomez v. Toledo, 446 U. S. 635,
639 (1980). The majority here, as elsewhere, injures the
right by denying the remedy. See, e.g., Egbert v. Boule, 596
U. S. ___ (2022). I respectfully dissent.

```

---

## GROUP: content/cases/Wright v. City of Euclid.md  (`case`, 5 assertions)

### content_page

```
---
title: "Wright v. City of Euclid"
type: case
citation: "962 F.3d 852 (2020)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, Sixth Circuit"
court_level: coa
circuit: 6th
year: 2020
date_decided: 2020-06-18
docket: 19-3452
authority_weight: "Binding in-circuit — 6th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2020-06-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Wright v. City of Euclid
  varies_by_point: false
  scope_note: "Published Sixth Circuit decision; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4762133/lamar-wright-v-city-of-euclid/"
  cluster_id: 4762133
  opinion_id: 4542480
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Recent development (role-based)"
related: ["[[Graham v. Connor]]", "[[Monell v. Department of Social Services]]", "[[Pearson v. Callahan]]"]
aliases: ["Lamar Wright v. City of Euclid", "Wright v. Euclid"]
tags: ["case", "section-1983", "qualified-immunity", "excessive-force", "false-arrest", "municipal-liability", "sixth-circuit"]
holding: "The Sixth Circuit REVERSED summary judgment / denial of qualified immunity on multiple Fourth Amendment § 1983 claims: excessive force…"
lake:
  record_id: Wright v. City of Euclid
  status: verified
  projected_at: 2026-07-06
---

# Wright v. City of Euclid

*962 F.3d 852 (6th Cir. 2020)* · U.S. Court of Appeals, Sixth Circuit · **Binding in-circuit — 6th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Plainclothes Euclid, Ohio officers in an unmarked car, suspecting a drug deal, stopped Lamar Wright. According to Wright, within moments — without his fleeing or actively resisting — Officer Flagg drew a weapon and tased him and Officer Williams brandished a firearm and pepper-sprayed him; Wright, who wore a colostomy bag, was pulled from his SUV. He was arrested, his arrest designated drug-related (subjecting him to more invasive searches), and held roughly four hours past posting bond for a body scan that found no drugs; the charges were later dropped. Wright sued the officers and the City under § 1983. The district court granted summary judgment to the defendants on qualified-immunity and Monell grounds.

## Issue
Whether genuine disputes of material fact precluded summary judgment — and whether [[Qualified Immunity|qualified immunity]] shielded the officers — on Wright's Fourth Amendment claims for excessive force, false arrest, and extended detention, and whether the City could face Monell municipal liability.

## Rule
[[Qualified Immunity|Qualified immunity]] is overcome where, taking the plaintiff's version of the facts as true, a jury could find a violation of a clearly established right. On excessive force: "It was clearly established as of November 4, 2016 that drawing a weapon on a suspect who was not fleeing or posing a safety risk and tasering a suspect who was not actively resisting arrest constituted excessive force." — *Wright v. City of Euclid*, 962 F.3d 852 (6th Cir. 2020) (slip op., at 17). ^pin-op17

On false arrest: "the right to be free from arrest without probable cause is a 'quintessential example[] of [a] "clearly established" constitutional right.'" — *Id.* (slip op., at 23). ^pin-op23

On municipal liability: "Wright has produced enough evidence such that a reasonable jury could find that the City's custom surrounding use of force is so settled so as to have the force of law and that it was the moving force behind violations of Wright's constitutional rights." — *Id.* (slip op., at 33). ^pin-op33

## Application
On these facts, taking Wright's account as true (as required at summary judgment), a reasonable jury could find that Flagg and Williams used excessive force by drawing weapons and deploying a taser and pepper spray against a suspect who was neither fleeing nor actively resisting, and that the officers lacked probable cause to arrest him. Because both rights were clearly established by November 2016, the officers were not entitled to [[Qualified Immunity|qualified immunity]] on those claims, and the extended detention (derivative of the arrest) failed for the same reason. Wright's evidence about the Euclid department's use-of-force training and culture, including offensive training materials, also permitted a jury to find a municipal custom that was the moving force behind the violations. The court reversed the grants of summary judgment on these claims.

## Conclusion
Genuine fact disputes precluded summary judgment, and the rights at issue were clearly established, so the officers were not entitled to [[Qualified Immunity|qualified immunity]]; the City could face [[Section 1983 Liability and Qualified Immunity|Monell liability]]. The Sixth Circuit reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 6th Cir.**
- No negative treatment. *Wright* applies the excessive-force standard of [[Graham v. Connor]], the clearly-established/qualified-immunity framework reflected in [[Pearson v. Callahan]], and the municipal-liability "policy or custom" rule of [[Monell v. Department of Social Services]].

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development (role-based)*

## Sources
- *Wright v. City of Euclid*, 962 F.3d 852 (6th Cir. 2020) — https://www.courtlistener.com/opinion/4762133/lamar-wright-v-city-of-euclid/ — pinpoints given as slip-opinion pages (slip op., at 17, 23, 33); CourtListener carries the slip opinion, paginated by slip page (cluster 4762133 → opinion 4542480).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2b23dc3ff023c2ca", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "962 F.3d 852 (2020)", "court": "U.S. Court of Appeals, Sixth Circuit", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Wright v. City of Euclid", "year": "2020"}}
{"assertion_id": "0259211247f58c4b", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Recent development (role-based)", "title": "Wright v. City of Euclid"}}
{"assertion_id": "029f34eb909a3b4b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Sixth Circuit REVERSED summary judgment / denial of qualified immunity on multiple Fourth Amendment § 1983 claims: excessive force…", "title": "Wright v. City of Euclid"}}
{"assertion_id": "691d3381e9776a26", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2020-06-18", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Wright v. City of Euclid", "field_i_validity": "good_law", "scope_note": "Published Sixth Circuit decision; good law.", "title": "Wright v. City of Euclid", "varies_by_point": "false"}}
{"assertion_id": "ac8c0e37818c658d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 6th Cir.", "title": "Wright v. City of Euclid"}}
```

### lake record — Wright v. City of Euclid

```json
{
  "schema_version": "s2.v1",
  "record_id": "Wright v. City of Euclid",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Lamar Wright v. City of Euclid",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "Wright v. City of Euclid",
    "court": "U.S. Court of Appeals, Sixth Circuit",
    "court_id": "ca6",
    "court_level": "coa",
    "circuit": "6th",
    "state": null,
    "date_decided": "2020-06-18",
    "year": 2020,
    "docket": "19-3452",
    "cluster_id": 4762133,
    "lead_opinion_id": 4542480,
    "sibling_ids": [
      4542480
    ],
    "absolute_url": "/opinion/4762133/lamar-wright-v-city-of-euclid/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "962 F.3d 852",
      "volume": "962",
      "reporter": "F.3d",
      "page": "852",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "962 F.3d 852",
        "volume": "962",
        "reporter": "F.3d",
        "page": "852",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "962 F.3d 852",
    "official_selection": {
      "court_class": "coa",
      "selected": "962 F.3d 852",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op17",
      "page": null,
      "quote": "--- # Wright v. City of Euclid *962 F.3d 852 (6th Cir. 2020)* \u00b7 U.S. Court of Appeals, Sixth Circuit \u00b7 **Binding in-circuit \u2014 6th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Plainclothes Euclid, Ohio officers in an unmarked car, suspecting a drug deal, stopped Lamar Wright. According to Wright, within moments \u2014 without his fleeing or actively resisting \u2014 Officer Flagg drew a weapon and tased him and Officer Williams brandished a firearm and pepper-sprayed him; Wright, who wore a colostomy bag, was pulled from his SUV. He was arrested, his arrest designated drug-related (subjecting him to more invasive searches), and held roughly four hours past posting bond for a body scan that found no drugs; the charges were later dropped. Wright sued the officers and the City under \u00a7 1983. The district court granted summary judgment to the defendants on qualified-immunity and Monell grounds. ## Issue Whether genuine disputes of material fact precluded summary judgment \u2014 and whether qualified immunity shielded the officers \u2014 on Wright's Fourth Amendment claims for excessive force, false arrest, and extended detention, and whether the City could face Monell municipal liability. ## Rule Qualified immunity is overcome where, taking the plaintiff's version of the facts as true, a jury could find a violation of a clearly established right. On excessive force:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op23",
      "page": null,
      "quote": "the right to be free from arrest without probable cause is a 'quintessential example[] of [a]",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op33",
      "page": null,
      "quote": "Wright has produced enough evidence such that a reasonable jury could find that the City's custom surrounding use of force is so settled so as to have the force of law and that it was the moving force behind violations of Wright's constitutional rights.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2020-06-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Wright v. City of Euclid",
    "varies_by_point": false,
    "scope_note": "Published Sixth Circuit decision; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Pearlie Gambrel v. Knox Cnty., Ky.",
          "cluster_id": 6347889,
          "cite": [
            "25 F.4th 391"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salvatore Palma, Jr. v. Matthew Johns",
          "cluster_id": 6445970,
          "cite": [
            "27 F.4th 419"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tucker v. City of Shreveport",
          "cluster_id": 4884106,
          "cite": [
            "998 F.3d 165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Shumate v. City of Adrian, Mich.",
          "cluster_id": 7855599,
          "cite": [
            "44 F.4th 427"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lutfi Saalim v. Walmart, Inc.",
          "cluster_id": 9490587,
          "cite": [
            "97 F.4th 995"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wendy Browning v. Edmonson Cnty., Ky.",
          "cluster_id": 5298175,
          "cite": [
            "18 F.4th 516"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kamel Chaney-Snell v. Andrew Young",
          "cluster_id": 9493618,
          "cite": [
            "98 F.4th 699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Timothy Raimey v. City of Niles, Ohio",
          "cluster_id": 9419576,
          "cite": [
            "77 F.4th 441"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "LaChance v. Town of Charlton",
          "cluster_id": 4860892,
          "cite": [
            "990 F.3d 14"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chana Wiley v. City of Columbus",
          "cluster_id": 6474125,
          "cite": [
            "36 F.4th 661"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Howard Linden v. City of Southfield, Mich.",
          "cluster_id": 9416052,
          "cite": [
            "75 F.4th 597"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joseph Meadows v. City of Walker, Mich.",
          "cluster_id": 7857927,
          "cite": [
            "46 F.4th 416"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whitney Hodges v. City of Grand Rapids, Mich.",
          "cluster_id": 10595782,
          "cite": [
            "139 F.4th 495"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sean Hart v. City of Grand Rapids, Mich.",
          "cluster_id": 10584953,
          "cite": [
            "138 F.4th 409"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Linda Moser v. Etowah Police Dep't",
          "cluster_id": 6447900,
          "cite": [
            "27 F.4th 1148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Clemons v. John Couch",
          "cluster_id": 4898166,
          "cite": [
            "3 F.4th 897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jones",
          "cluster_id": 6479950,
          "cite": [
            "2022 Ohio 2122"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cory Driscoll v. Montgomery Cnty. Bd. of Comm'rs",
          "cluster_id": 10847360,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Louis Alford v. Brandon Deffendoll",
          "cluster_id": 10778906,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ashly Romero v. City of Lansing, Mich.",
          "cluster_id": 10738319,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reuben Jelani Adams v. Lexington-Fayette Urban Cnty. Gov't",
          "cluster_id": 10700490,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael Chrestman v. Metro Gov't of Nashville & Davidson Cnty., Tenn.",
          "cluster_id": 10672549,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wright v. City of Euclid:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4542480) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca6)",
        "reviewed": 16,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 16,
        "triage_read": 0,
        "triage_snippet_classified": 16
      },
      "lane2_top_cited": {
        "query": "cites:(4542480)",
        "reviewed": 22,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 22,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(4542480)",
        "reviewed": 11,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 11,
        "triage_read": 0,
        "triage_snippet_classified": 11
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4542480)",
    "indexed_citing_opinions": 22,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4542480,
        "count": 22,
        "count_source": "search"
      }
    ],
    "citation_count": 217,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/wright-v-city-of-euclid.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU3OTQxMiZzPTEwNzc4OTA2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%284542480%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4542480,
        "cited_id": 2092,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 178987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 196191,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 220504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 478767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 533819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 675736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 746760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 774301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 781854,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 792929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 794492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 796462,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 797071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 797998,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 804467,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 807291,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 807347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 856354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 857543,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 1192312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 1207949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 1238362,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 1462051,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 2641010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 2658128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 2760321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 2783172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 2787500,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 2805007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 2809264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 2981244,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 3178832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 3192192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 3194675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 3711678,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 3739859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 3747697,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 3763766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4027018,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4155276,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4193066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4216889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4237060,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4263410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4398647,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4405225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4422863,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4431725,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 4486948,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 6762733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 6771749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 6951820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 7081890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9422887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9424277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9425988,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9427232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9430379,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9430387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9430599,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9431589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9431666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9434318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9475403,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9498217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9498341,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9501733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9501893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9520246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9842136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9848411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9873459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4542480,
        "cited_id": 9877396,
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
    "date_created": "2026-07-06T04:46:06Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:46:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:46:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:48:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:46:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Wright v. City of Euclid

```
                               RECOMMENDED FOR PUBLICATION
                               Pursuant to Sixth Circuit I.O.P. 32.1(b)
                                      File Name: 20a0185p.06

                   UNITED STATES COURT OF APPEALS
                                 FOR THE SIXTH CIRCUIT



 LAMAR WRIGHT,                                              ┐
                                  Plaintiff-Appellant,      │
                                                            │
                                                             >        No. 19-3452
        v.                                                  │
                                                            │
                                                            │
 CITY OF EUCLID, OHIO; KYLE FLAGG; VASHON                   │
 WILLIAMS,                                                  │
                         Defendants-Appellees.              │
                                                            ┘

                         Appeal from the United States District Court
                        for the Northern District of Ohio at Cleveland.
                    No. 1:17-cv-02503—Donald C. Nugent, District Judge.

                                  Argued: January 28, 2020

                              Decided and Filed: June 18, 2020

                                      _________________

                                           COUNSEL

ARGUED: Jacqueline C. Greene, FRIEDMAN & GILBERT, Cleveland, Ohio, for Appellant.
Frank H. Scialdone, MAZANEC, RASKIN AND RYDER CO., L.P.A., Cleveland, Ohio, for
Appellees. ON BRIEF: Jacqueline C. Greene, Sarah Gelsomino, Terry H. Gilbert,
FRIEDMAN & GILBERT, Cleveland, Ohio, for Appellant. Frank H. Scialdone, James A.
Climer, John D. Pinzone, MAZANEC, RASKIN AND RYDER CO., L.P.A., Cleveland, Ohio,
for Appellees.
                                     _________________

                                            OPINION
                                     _________________

       JOHN K. BUSH, Circuit Judge. This appeal involves a Chris Rock video and a cartoon,
but it is no laughing matter. In fact, this case raises a gravely important issue—police use of
 No. 19-3452                       Wright v. City of Euclid, et al.                        Page 2


force—that has dominated the nation’s attention in recent weeks. Lamar Wright, an African
American man, brought claims under 42 U.S.C. § 1983 of unconstitutional excessive force, false
arrest, malicious prosecution, and municipal liability, along with state-law claims, relating to the
actions of certain police officers and other officials employed by the City of Euclid, Ohio.

       The police officers, in plain clothes, approached Wright’s parked SUV with weapons
drawn. Thinking he was about to be robbed, Wright tried to back up the vehicle to get away.
A flash of a badge made him realize that the men he thought were about rob him were the police.
Wright stopped the SUV, and the officers pulled open the driver’s side door. Wright had no
weapon, and the officers holstered theirs. Nonetheless, they simultaneously deployed a taser
against him and pepper-sprayed him at point-blank range, all while he remained seated in the
vehicle. Wright had trouble getting out of the SUV because of a colostomy bag stapled to the
right side of his abdomen. He was recovering from a medical operation for diverticulitis. The
police aggravated the staples from his surgery, causing bleeding from around the bag.

       The officers then arrested Wright even though there was arguably no probable cause for
the arrest. The officers designated Wright’s arrest as arising from a drug investigation, even
though they found no drugs on him. This designation resulted in Wright’s being detained for
more than nine hours and subjected to an intrusive body scan for drugs well after the officers
knew of Wright’s medical condition. The scan revealed no drugs, and no drug-related charges
were ever brought against him.

       The district court granted summary judgment to the officers on the basis of qualified
immunity, and to the City based on Monell v. Department of Social Services, 436 U.S. 658, 690
(1978). As explained below, we disagree with the district court’s qualified immunity analysis.
With respect to the Monell claim, the evidence against the City includes the Chris Rock video,
played as part of its use-of-force training for officers, in which the comedian makes remarks
about Rodney King and police misconduct that are highly inappropriate for law-enforcement
instruction. The proof also includes an offensive cartoon in the City’s police-training manual
that portrays an officer in riot gear beating a prone and unarmed civilian with a club, with the
caption “protecting and serving the poop out of you.” R. 23 at PageID 808. Based on this
 No. 19-3452                       Wright v. City of Euclid, et al.                         Page 3


evidence and more, we find that Wright has introduced sufficient evidence of municipal policy to
satisfy Monell.

       For the reasons set forth below, we AFFIRM in part and REVERSE in part the district
court’s judgment, and REMAND for further proceedings consistent with this opinion.

                                                 I.

A.     Wright’s Stop, Arrest and Experience in Custody

       On November 4, 2016, at around 6:00 p.m., Lamar Wright pulled an SUV onto a
residential driveway off of 207th Street in Euclid, Ohio. After Wright rolled down his window,
conversation ensued with a friend who stood outside the residence. The friend never came over
to the SUV, and Wright never exited the vehicle. Their visit lasted for about a minute.

       Unbeknownst to Wright and his friend, plain-clothed Officers Kyle Flagg and Vashon
Williams, in an unmarked vehicle, were surveilling the friend’s home based on reports of illegal
drug activity in the area and at that residence in particular. The officers identified Wright’s
vehicle as a rented Ford Edge SUV. Based on the short amount of time Wright spent at the
house, the officers suspected that he may have been involved in a drug transaction.

       After Wright pulled out of the driveway, Flagg and Williams followed him. He turned
right onto Recher Avenue and then left onto East 212th Street. The officers maintain that at both
turns, Wright failed to use his turn signal, but there is no dash-cam footage or other evidence to
confirm the officers’ word. Wright insists that he did use his turn signal in both instances.

       The situation escalated after Wright pulled into a second driveway to answer a text
message from his girlfriend. While Wright texted in the SUV, the officers exited their vehicle,
drawing their guns as they approached the SUV. One of the men caught Wright’s eye when he
glanced up from his texting. In his side mirror, Wright could see this man dressed in dark
clothing with a gun pointed at the SUV. Believing that he was about to be robbed, Wright
dropped his cellphone in the center console and threw the car into reverse. Glancing to his left,
he saw another armed man, but this time he noticed a badge. Wright heard the men yell: “Shut
the car off!” and “Open the door!” Now realizing that the men were police officers, he put the
 No. 19-3452                        Wright v. City of Euclid, et al.                         Page 4


car in park and put his hands up. These events are corroborated by the body-cam footage.
At this point, Flagg stood beside the driver’s side door while Williams was next to the front
passenger door. Both officers holstered their guns.

       Next, Flagg yanked the driver’s side door open and demanded that Wright shut off the
vehicle. Wright complied and then raised his hands once more. Flagg grabbed Wright’s left
wrist, twisting his arm behind his back. The officer then attempted to gain control of Wright’s
right arm in order to handcuff him behind his back while he remained seated in the vehicle.
Flagg was unsuccessful in his efforts.       As Flagg continued to twist the left arm, Wright
repeatedly exclaimed that the officer was hurting him, to which Flagg responded, “let me see
your hand,” apparently referring to Wright’s right hand.

       Flagg then tried to pull Wright from the vehicle, but the latter had difficulty getting out.
As noted, Wright had recently undergone surgery for diverticulitis, which required staples in his
stomach and a colostomy bag attached to his abdomen. Though the officers apparently could not
see the bag and staples, these items prevented Wright from easily moving from his seat. Wright
placed his right hand on the center console of the car to better situate his torso to exit the car. By
this point Williams had moved over to stand behind Flagg on the driver’s side. Williams
responded to Wright’s hand movement by reaching around Flagg to pepper-spray Wright at
point-blank range.    Flagg simultaneously deployed his taser into Wright’s abdomen.             The
besieged detainee finally managed to exit the car with his hands up. He then was forced face
down on the ground, where he explained to officers that he had a “shit bag” on. Officer Williams
next handcuffed Wright while he was on the ground.

       Wright was bleeding from the staples that attached the colostomy bag to his abdomen.
The bag was now visible to Williams, who would testify that he “was kind of leery of getting
some sort of biohazard on [him].” R. 24 at PageID 938. The officers had Wright sit on the trunk
of his car while they called an ambulance. As the body cam continued to record, Flagg made
various arguably self-serving statements, including that “[Wright] was reaching like he had a
f***ing gun,” and that Flagg had been afraid that Wright was going to shoot him. Wright did not
have a gun, nor did he have any drugs or other contraband. The officers conceded that they did
not have probable cause to arrest Wright until after they believed he was resisting, and that they
 No. 19-3452                         Wright v. City of Euclid, et al.                     Page 5


had not seen Wright engage in any illegal activity prior to the arrest apart from his alleged
failures to use his turn signal. They arrested Wright for the misdemeanors of obstructing official
business and resisting arrest.

       After Wright’s arrest, a hospital doctor treated him for bleeding in his abdomen because
of the stress placed on the staples around his colostomy bag. Wright refused to submit to an x-
ray because of his recent surgery. The officers responded by demanding a CT scan of Wright’s
abdomen, but the doctors refused to perform the scan after consulting with the hospital’s legal
department. Wright was then discharged from the hospital and taken to the Euclid jail.

       At his 10:45 p.m. booking, Wright was charged with the two misdemeanors for which he
was arrested (obstructing official business and resisting arrest), along with two other offenses
(criminal trespass and failure to use a turn signal). Despite the fact that Wright had no drugs
when he was arrested and was not charged with any drug-related offenses, the officers
designated Wright’s arrest as stemming from a drug investigation. Flagg acknowledged that he
knew that this designation would result in Wright’s being subjected to additional, more thorough
searches.

       Wright posted bond between 11:00 p.m. and midnight, but he still was not released from
police custody. As Wright was attempting to leave the Euclid jail, a corrections officer told him
that he would be taken to the Cuyahoga County jail for a full body scan to see if he was hiding
drugs in his abdomen. Shortly after 1:00 a.m., he arrived at this next facility, where jail staff
searched him using a body scanner. The search turned up nothing. Wright finally was released
from custody at 3:55 a.m.

       Over seven months later, all the charges against Wright were dropped. Neither Flagg nor
Williams was investigated or disciplined for his encounter with Wright, and their use of force
was approved by their supervisors.

B.     The City of Euclid’s Practices and Customs

       Wright argues that his injury is directly attributable to the City’s policy or custom of
indifference to use of force. Euclid police officers undergo “defensive tactics training” that
 No. 19-3452                       Wright v. City of Euclid, et al.                       Page 6


purportedly trains officers in methods to defend themselves or defuse a situation.           Flagg
maintains he used “defensive tactics” in subduing Wright.

       This training contains a link to a YouTube video of a Chris Rock comedy skit entitled
“How not to get your ass kicked by the police!” The video shows numerous clips of multiple
police officers beating African-American suspects. During the video, Rock says things such as:

       “People in the black community . . . often wonder that we might be a victim of
       police brutality, so as a public service the Chris Rock Show proudly presents: this
       educational video.”
       “Have you ever been face-to-face with a police officer and wondered: is he about
       to kick my ass? Well wonder no more. If you follow these easy tips, you’ll be
       fine.”
       “We all know what happened to Rodney King, but Rodney wouldn’t have got his
       ass kicked if he had just followed this simple tip. When you see flashing police
       lights in your mirror, stop immediately. Everybody knows, if the police have to
       come and get you, they’re bringing an ass kicking with ‘em.”
       “If you have to give a friend a ride, get a white friend. A white friend can be the
       difference between a ticket and a bullet in the ass.”

InsaneNutter, Chris Rock-How not to get your ass kicked by the police! (Feb. 2, 2007),
https://www.youtube.com/watch?v=uj0mtxXEGE8 [https://perma.cc/NU2W-MGLN].

       Sergeant Murowsky conducts the use-of-force trainings and reviews all incidents of
officer-involved force. He stated that he thought the video was humorous and that it related to
things that Euclid police officers have experienced.        The City’s use-of-force training also
includes a PowerPoint presentation, the first page of which displays a stick figure cartoon
portraying a police officer in riot gear beating a prone and unarmed civilian with a club with the
caption “protecting and serving the poop out of you.” R. 23 at PageID 808.
 No. 19-3452                        Wright v. City of Euclid, et al.                        Page 7




        Sergeant Murowsky testified that he did not believe that the graphic conveys that the
Euclid Police Department “beat[s] the hell out of people,” R. 25 at PageID 1200, but he didn’t
know what other message could possibly be taken away from the image.

        Finally, the use-of-force training contains a meme that depicts two officers with their
guns drawn and aimed at something. It is captioned “Bed bug! Bed bug on my shoe!” Sergeant
Murowsky testified that he believed the image conveyed that the officers were overreacting to
and escalating a situation.

        When the Euclid Police Department receives allegations of excessive force, Sergeant
Murowsky reviews the relevant incident report to determine whether the use of force was
appropriate. Murowsky approved the use of force against Wright, as he had done numerous
times with respect to other incident reports. In fact, he testified that he had never heard of a use-
of-force incident by another Euclid officer that he deemed inappropriate. Likewise, Chief Meyer
testified that he had never found merit to any civilian complaint concerning use of force, false
arrest, or illegal searches.
 No. 19-3452                        Wright v. City of Euclid, et al.                         Page 8


C.     Proceedings Below

       Wright brought suit in the U.S. District Court for the Northern District of Ohio against
the City of Euclid and Officers Flagg and Williams, alleging counts under 42 U.S.C. § 1983 of
excessive force, false arrest, malicious prosecution, failure to intervene, extended detention, and
the City’s municipal liability, along with claims under Ohio law for malicious prosecution and
intentional infliction of emotional distress. After the close of discovery, the district court granted
summary judgment to the officers and the City. Wright v. City of Euclid, No. 1:17 CV 2503,
2019 WL 2009453, at *12 (N.D. Ohio May 7, 2019). Wright filed a timely appeal.

                                                 II.

       We review a district court’s grant of summary judgment de novo. Jackson v. City of
Cleveland, 925 F.3d 793, 806 (6th Cir. 2019) (internal quotations omitted). Summary judgment
is appropriate when “no genuine dispute as to any material fact” exists and the moving party “is
entitled to judgment as a matter of law.” Fed. R. Civ. P. 56(a). “A genuine dispute of material
fact exists ‘if the evidence is such that a reasonable jury could return a verdict for the nonmoving
party.’” Peffer v. Stephens, 880 F.3d 256, 262 (6th Cir. 2018) (quoting Anderson v. Liberty
Lobby, Inc., 477 U.S. 242, 248 (1986)). At the summary judgment stage, “the evidence is
construed and all reasonable inferences are drawn in favor of the nonmoving party.” Burgess v.
Fischer, 735 F.3d 462, 471 (6th Cir. 2013) (citing Hawkis v. Anheuser-Busch, Inc., 517 F.3d
321, 332 (6th Cir. 2008)).

       Wright raises several arguments on appeal. First, he argues that the district court erred in
granting summary judgment on qualified immunity grounds to Flagg and Williams for his
excessive-force and failure-to-intervene claims based on brandishing their firearms and using a
taser and pepper spray when he was not actively resisting arrest. Second, he argues that the
district court erred in granting the officers qualified immunity on his false-arrest and extended-
detention claims. Third, he claims that the district court erred in granting qualified immunity to
the officers on his federal malicious-prosecution claim. Fourth, he argues that the district court
erred in holding that the officers were entitled to statutory immunity for his state-law claims.
Fifth, he argues that the district court erred in granting the officers summary judgment on his
 No. 19-3452                       Wright v. City of Euclid, et al.                        Page 9


state-law claims of malicious prosecution and intentional infliction of emotional distress. Sixth,
and finally, he argues that the district court erred in granting summary judgment to the City of
Euclid under Monell.

       Most of Wright’s arguments hinge on whether Flagg and Williams are immune from suit
through qualified immunity or statutory immunity under Ohio law. We analyze whether an
officer is entitled to qualified immunity using two steps: (1) whether the defendant violated a
constitutional right; and (2) whether that constitutional right was clearly established at the time
of the alleged violation. Fazica v. Jordan, 926 F.3d 283, 289 (6th Cir. 2019). A similar inquiry
applies to statutory immunity under Ohio law. See Hopper v. Phil Plummer, 887 F.3d 744, 759
(6th Cir. 2018).

A.     Excessive Force

       Wright first argues that the district court erred in granting qualified immunity to Flagg
and Williams on his excessive-force claims. He maintains that the officers used excessive force
in brandishing their firearms as they approached his vehicle, that Flagg used excessive force in
deploying his taser, and that Williams used excessive force in using pepper spray, all while
(Wright claims) he was not resisting arrest.

       “When more than one officer is involved, the court must consider each officer’s
entitlement to qualified immunity separately.” Smith v. City of Troy, 874 F.3d 938, 944 (6th Cir.
2017) (per curiam). And when, as here, a plaintiff claims that excessive force was used multiple
times, “the court must segment the incident into its constituent parts and consider the officer’s
entitlement to qualified immunity at each step along the way.” Id.

       1.      Officer Flagg

               a.      Constitutional Violation

       Wright argues that Flagg “used far more force than necessary to effect an arrest,”
Appellant’s Br. at 42, when he approached Wright’s SUV with his gun drawn and later deployed
his taser on Wright while the latter sat in the driver’s seat of the vehicle. When making an arrest
or investigatory stop, the police have “the right to use some degree of physical coercion or threat
 No. 19-3452                       Wright v. City of Euclid, et al.                       Page 10


thereof to effect it.” Graham v. Connor, 490 U.S. 386, 396 (1989). In determining whether the
use of force in effecting an arrest is excessive in violation of the Fourth Amendment, we must
determine “whether the officers’ actions [were] ‘objectively reasonable’ in light of the facts and
circumstances confronting them, without regard to their underlying intent or motivation.” Id. at
397. This inquiry assesses “reasonableness at the moment” of the use of force, as “judged from
the perspective of a reasonable officer on the scene, rather than with the 20/20 vision of
hindsight.” Goodwin v. City of Painesville, 781 F.3d 314, 321 (6th Cir. 2015) (quoting Graham,
490 U.S. at 396).

       The bottom-line inquiry is “whether the totality of the circumstances justifies a particular
level of force.”    Coffey v. Carroll, 933 F.3d 577, 588 (6th Cir. 2019) (citing Mitchell v.
Schlabach, 864 F.3d 416, 421 (6th Cir. 2017)). Three factors from Graham guide this analysis:
“[1] the severity of the crime at issue, [2] whether the suspect poses an immediate threat to the
safety of the officers or others, and [3] whether he is actively resisting arrest or attempting to
evade arrest by flight.” Shreve v. Jessamine Cty. Fiscal Court, 453 F.3d 681, 687 (6th Cir. 2006)
(quoting Graham, 490 U.S. at 396). Balancing these factors, and viewing the record in the light
most favorable to Wright, a reasonable juror could conclude that Flagg used excessive force both
when he brandished his firearm and when he deployed his taser.

       As to the firearm, we have held that a police officer may approach a suspect with a
weapon drawn during a Terry stop when the officer reasonably fears for his safety. United States
v. Hardnett, 804 F.2d 353, 357 (6th Cir. 1986); see also United States v. Heath, 259 F.3d 522,
530 (6th Cir. 2001) (“[When the] surrounding circumstances give rise to a justifiable fear for
personal safety, a seizure effectuated with weapons drawn may properly be considered an
investigative stop.” (alteration in original) (quoting Hardnett, 804 F.2d at 357)). Moreover, we
have held that when a suspect is reasonably suspected of carrying drugs, an officer is “entitled to
rely on [his] experience and training in concluding that weapons are frequently used in drug
transactions.” Heath, 259 F.3d at 530. In Heath, the officers surveilled the defendant four times
over the course of a month and observed conduct that they believed was consistent with drug
activity, including stopping at locations under investigation for drug activity, checking for tails,
and associating with “a large-scale drug trafficker.” Id. at 525. The police had identified the
 No. 19-3452                        Wright v. City of Euclid, et al.                      Page 11


defendant and knew that he had three misdemeanor convictions and one felony drug conviction.
Id. at 524. They also obtained information from a confidential informant that the defendant was
trafficking in large quantities of cocaine. Id. In those circumstances, we held that it was
reasonable for the officers to approach the defendant’s vehicle with their guns drawn when
conducting a Terry stop after seeing him leave a building with a known large-scale drug
trafficker while carrying a bag. Id. at 530.

       Relying on Heath’s “drug activity = guns” premise, the district court in this case held as a
matter of law that Flagg and Williams were justified in drawing their weapons for protection
upon approaching Wright’s vehicle. See Appellant’s Br. at 44; see also Wright, 2019 WL
2009453, at *6 (“Thus, the officers in this case, having an objective reason to believe that
Mr. Wright may have been involved in drug activity, also had a reasonable belief that he may be
in possession of a weapon.”). The facts in this case, however, can be distinguished from Heath.
Unlike the defendant officers in Heath, the officers here had very little, if any, reason to think
that the detainee was involved in drug activity. Flagg and Williams had observed Wright pull
into a driveway at his friend’s house and speak to his friend for about one minute to exchange
greetings. According to Wright, he did not pull all the way up the driveway. While conversing,
Wright stayed in his car and the friend stayed on the porch. According to the officers, they were
surveilling the residence “based upon multiple arrests and complaints regarding drug activity.”
However, according to Wright, the prior complaints for the residence were all stale, only three of
the six complaints pertained to drugs, and none of the complaints pertained to him. Flagg and
Williams also admit that they did not see Wright engage in any criminal activity, drug-related or
otherwise, while stopped at the residence.

       Nevertheless, based only on Wright’s brief stop at the residence, the officers decided to
conduct a traffic stop with weapons drawn. These circumstances are very different from those in
Heath where the officers had a justifiable fear for their safety given that the defendant, whom
they had identified and surveilled for a month, was a large-scale drug dealer and likely to be
carrying a weapon. Flagg and Williams at most had a suspicion that Wright had briefly visited
with a suspected drug dealer, but given that the officers had not identified Wright himself as a
drug dealer or sought any corroboration of their suspicions of criminal activity, there is a genuine
 No. 19-3452                        Wright v. City of Euclid, et al.                     Page 12


dispute as to whether the officers were justified in brandishing their firearms upon approach.
Thus, a jury must determine whether their decision to do so was unconstitutionally excessive.
See, e.g., Croom v. Balkwill, 645 F.3d 1240, 1252 n.17 (11th Cir. 2011) (“An officer’s decision
to point a gun at an unarmed civilian who objectively poses no threat to the officer or the public
can certainly sustain a claim of excessive force.” (collecting cases)).

       Second, as to Flagg’s use of his taser, we hold that this too must be submitted to a jury to
determine whether the use of force was excessive. The tasering occurred when Flagg had, at
most, reasonable suspicion—not probable cause—to detain him for the officers’ drug
investigation. See Ciminillo v. Streicher, 434 F.3d 461, 467 (6th Cir. 2006) (noting that “the fact
that a plaintiff in a § 1983 suit had committed no crime clearly weighed against a finding of
reasonableness”). Therefore, at no point before Flagg began to seize Wright did Flagg have
probable cause to arrest him. The first Graham factor, relating to the severity of the suspected
crime, thus cuts against a finding of justified use of force because there was no probable cause
that he had committed any crime at all before the tasering occurred.

       “Of course, the use of force can be reasonable, even when the crime at issue is innocuous.
To determine whether this is so, we turn to the [second and third] Graham factors.” Thomas v.
Plummer, 489 F. App’x 116, 126 (6th Cir. 2012). Construing the record in the light most
favorable to Wright, the second Graham factor—the immediate safety threat posed by the
suspect to police and others—weighs in his favor as well. When Flagg deployed his taser,
Wright was doing his best to comply with the officers’ commands despite his recent surgery and
difficulty in exiting the SUV. After Flagg and Williams had holstered their weapons, Flagg
opened the driver’s side door and Wright put his hands up. Flagg then demanded Wright turn off
the engine, an order with which Wright complied, followed immediately by putting his hands up
again. When Wright was unable to comply with Flagg’s commands because of his stomach
staples and colostomy bag, the encounter turned violent. Wright was not armed. According to
Flagg, he thought Wright was reaching for a weapon in the center console and considered that
movement to be an act of resisting arrest. Wright, however, disputes that his hand movement
was threatening to the extent that he moved his hand at all. Although these two versions of
events are not inconsistent with each other—that is, Flagg could have reasonably believed
 No. 19-3452                       Wright v. City of Euclid, et al.                       Page 13


Wright was reaching for a gun when in reality he was trying to comply with orders—a
reasonable jury could find, based on the totality of the circumstances, that a reasonable officer
would not believe that Wright posed an immediate threat to their safety.

       Finally, the third Graham factor, which hinges on whether Wright was “actively” or
“passively” resisting arrest, weighs in his favor as well when the facts are construed in his favor.
See Goodwin v. City of Painesville, 781 F.3d 314, 323 (6th Cir. 2015) (noting that while active
resistance to an officer’s command can justify use of a taser, passive resistance—or no resistance
at all—does not justify such use of force) (citing Hagans v. Franklin Cty. Sheriff’s Office,
695 F.3d 505, 509 (6th Cir. 2012)). Flagg maintains that when he opened the driver’s side door,
he grabbed Wright’s left wrist and began to bring his left arm under control. Flagg claims that
when Wright pushed down on the center console, Flagg lost control of Wright’s arm, which
Flagg described as an act of resistance. A reasonable juror, however, could accept Wright’s
account that he was not resisting, but rather was simply having difficulty maneuvering while
seated in the vehicle and in Officer Flagg’s forced hold.

       Even if Flagg is correct that Wright’s act of pushing down on the center console
constituted some resistance, if the resistance was merely “passive,” then the use of a taser was
unreasonable. See Goodwin, 781 F.3d at 323. The tasering of Wright was justified only if he
engaged in resistance that was “active,” which “can take the form of ‘verbal hostility’ or a
‘deliberate act of defiance.’” Id. at 323 (quoting Eldridge v. City of Warren, 533 F. App’x 529,
534–35 (6th Cir. 2013)).

       We recognized this principle in Smith v. City of Troy, where the plaintiff was tased while
experiencing an epileptic seizure. 874 F.3d at 942. In that case, when officers arrived at the
scene, the plaintiff was standing outside his car clinging to a fence, which led the officers
mistakenly to believe that he had been driving under the influence. Id. In an attempt to return
the plaintiff to his car, an officer tried to pry the plaintiff’s fingers from the fence. Id. The
plaintiff responded by pulling his arm away from the officer, at which point the officer forced the
plaintiff to the ground and wrestled with him until a second officer arrived and deployed his
taser. Id. The district court granted the officers qualified immunity, holding that “the officers
used measured force in response to [the plaintiff’s] defiance of their orders and reaching where
 No. 19-3452                       Wright v. City of Euclid, et al.                      Page 14


the officers could not see his hands.” Id. at 943. We reversed, holding that “[a] reasonable juror
could conclude that, in pulling his arm away, [the plaintiff’s] resistance was minimal and that
[the force used] was excessive.” Id. at 945.

        Similarly, the facts regarding Wright’s arm movement would allow a reasonable juror to
find that his resistance was minimal to the extent that it constituted resistance at all. Wright
maintains that he reached down towards the center console in order to assist the officers in
removing him from the SUV because his mobility was limited as a result of his surgery,
colostomy bag, and staples in his stomach. However, Flagg claims that he was not aware of
Wright’s medical problems until after he had deployed his taser. The reasonableness of force is
predicated solely on the knowledge of officers in the moments before the force is used. Graham,
490 U.S. at 396–97. Therefore, if the officers did not know of Wright’s recent surgery, the
colostomy bag or the stomach staples, those facts would bear no weight in the reasonableness
calculus. But, even if the officers had no knowledge of any of these facts, there are other facts
that, when construed in Wright’s favor, could support a reasonable juror’s finding that Wright
did not actively resist. In a split-second reaction, Wright pushed down on the center console in
an attempt to maneuver his torso into a better position to get out of the car. Construing the
record in the light most favorable to Wright, his act of purported resistance is close enough to
that of the plaintiff in Smith to present a question of fact for a jury to decide whether Wright in
fact actively resisted arrest.

        That this issue presents a jury question is confirmed by our consideration of the officer’s
actions “in light of testimony regarding the training that [the officer] received.” Griffith v.
Coburn, 473 F.3d 650, 657 (6th Cir. 2007). Wright presented expert testimony from Roy Taylor,
a police officer and expert on police-involved use of force, who testified that the level of force
used was unreasonable. In his affidavit, Taylor noted that the Model Policy on Electronic
Control Weapons of the International Association of Chiefs of Police (of which the Euclid police
chief is a member), the TASER training manual, and the Euclid Police Department’s use-of-
force continuum, each outline circumstances in which use of a taser is appropriate. According to
Taylor, “[n]one of the circumstances . . . were present when Officer Flagg deployed his taser
 No. 19-3452                        Wright v. City of Euclid, et al.                      Page 15


against Lamar Wright. Officer Flagg used a greater level of force than other officers would have
used if facing the same, or similar circumstances.” R. 31-6 at PageID 1415.

         Finally, and significantly, at no point before Flagg deployed his taser was Wright under
arrest for any offense. As we noted in Smith, “the mere failure of a citizen—not arrested for any
crime—to follow the officer’s commands does not give a law enforcement official authority to
put the citizen in handcuffs.” 874 F.3d at 945. By the same logic, an officer may not tase a
citizen not under arrest merely for failure to follow the officer’s orders when the officer has no
reasonable fear for his or her safety. Whether the tasering in this instance was constitutionally
permissible must be decided by the jury, given the genuine factual disputes described above
concerning the circumstances of Wright’s encounter with the officers.

                b.      Clearly Established Right

         We now must decide whether, accepting Wright’s version of the facts, Flagg’s drawing
of his weapon and use of the taser violated a constitutional right that was “clearly established at
the time of the alleged violation.” Campbell v. City of Springboro, 700 F.3d 779, 786 (6th Cir.
2012).    For this prong of the qualified immunity analysis, we are “not to define clearly
established law at a high level of generality.” Ashcroft v. al-Kidd, 563 U.S. 731, 742 (2011).

         The district court held that it was “unaware of any controlling cases that have established
a constitutional violation occurred when non-lethal force was used to obtain control over the
suspect who reasonably appeared to pose a safety risk to officers.” Wright, 2019 WL 2009453,
at *7. In so holding, the district court examined the issue of whether the law was clearly
established using too specific of a level of generality. See al-Kidd, 563 U.S. at 742. The district
court also incorrectly framed the issue based upon Flagg’s version of the facts by assuming that
Wright did in fact “reasonably appear[] to pose a safety risk” to the officer. Given that this was a
summary judgment ruling, the district court instead should have considered whether the law was
clearly established using Wright’s version of the facts. Wright contends that he had done
nothing prior to his encounter with police to justify the officers’ brandishing of their firearms.
He also maintains that he had a right not to be tased when, during the course of an investigatory
detention, he inadvertently broke away from the officer’s grip, but presented no threat to others,
 No. 19-3452                       Wright v. City of Euclid, et al.                       Page 16


and did not actively resist arrest. For the reasons discussed below, we hold that, viewing the
facts in Wright’s favor, Flagg’s drawing of his firearm and use of his taser violated Wright’s
constitutional rights that were clearly established as of the date of the encounter, November 4,
2016.

        We reach this conclusion by examining “whether the contours of” the plaintiff’s
constitutional rights “were sufficiently defined to give a reasonable officer fair warning that the
conduct at issue was unconstitutional.” Brown v. Chapman, 814 F.3d 447, 461 (6th Cir. 2016).
“This is not to say that an official action is protected by qualified immunity unless the very
action in question has previously been held unlawful, . . . but it is to say that in light of pre-
existing law the unlawfulness must be apparent.” Hope v. Pelzer, 536 U.S. 730, 739 (2002)
(quoting Anderson v. Creighton, 482 U.S. 635, 640 (1987)). “In determining whether a right was
clearly established, we look first to decisions of the Supreme Court, then to our own
precedents, and then to decisions of other courts of appeal, and we ask whether these precedents
‘placed the . . . constitutional question beyond debate.’” Hearring v. Sliwowski, 712 F.3d 275,
280 (6th Cir. 2013) (quoting al-Kidd, 563 U.S. at 741).

        With respect to an officer’s use of a firearm, we have recognized that “pointing a firearm
at an individual and making a demand of that individual . . . communicates the implicit threat
that if the individual does not comply with the . . . demands, the [one pointing the firearm] will
shoot the individual.” Vanderhoef v. Dixon, 938 F.3d 271, 277 (6th Cir. 2019) (quoting United
States v. Bolden, 479 F.3d 455, 461 (6th Cir. 2007)). We have also recognized that pointing a
gun at an individual can constitute excessive force under the Fourth Amendment. See Binay v.
Bettendorf, 601 F.3d 640, 650 (6th Cir. 2010). We have addressed a similar scenario before. In
Davis v. Bergeon, 187 F.3d 635, 1999 WL 591448 (6th Cir. 1999) (table), we concluded that
pointing or displaying a firearm could constitute excessive force in the following circumstances:

        [The detective] was not in the process of an arrest, but inspecting the ladies’
        restroom. [The plaintiff] was attempting to enter the men’s restroom to use the
        facilities and was not suspected of any wrongdoing at that point in time. [The
        detective], dressed in plainclothes, allegedly did not identify herself, pointed her
        weapon at [the plaintiff] and ordered him to get on the floor.
 No. 19-3452                        Wright v. City of Euclid, et al.                       Page 17


Id. at *5. We concluded that those facts sufficed to allow a jury to find that the officer had
violated the plaintiff’s clearly established Fourth Amendment rights. Id. at *5–6; see also Saad
v. City of Dearborn, No. 10-12635, 2011 WL 3112517, at *5 (E.D. Mich. July 26, 2011), aff’d
sub nom. Saad v. Krause, 472 F. App’x 403 (6th Cir. 2012) (per curiam) (noting that that the
Sixth Circuit has “held that pointing a gun at an unarmed suspect who is not fleeing or posing a
risk to police officers may be an objectively unreasonable use of force” (citing Binay, 601 F.3d at
650)). Based on this authority, it was clearly established as of the time of Wright’s encounter
with the officers that brandishing a firearm without a justifiable fear that Wright was fleeing or
dangerous was unreasonable and constituted excessive force.

       In conducting the analysis as it pertains to use of the taser, two lines of cases emerge.
The first holds that there is no clearly established right not to be tased when a suspect is actively
resisting arrest. See, e.g., Hagans v. Franklin Cty. Sheriff’s Office, 695 F.3d 505, 509–10 (6th
Cir. 2012) (noting that, as of 2007, a suspect who refused to be handcuffed and actively resisted
arrest did not have a clearly established right not to be tased). The second line of authority holds
that there is a clearly established right not to be tased when the suspect is not actively resisting
arrest. See Brown, 814 F.3d at 462 (holding that “as of December 31, 2010, it was clearly
established that tasering a non-threatening suspect who was not actively resisting arrest
constituted excessive force”); Coffey, 933 F.3d at 589 (“Drawing the line at a suspect’s active
resistance defines the right at a level of particularity appropriate for a claim pursued under
§ 1983.”); Smith, 874 F.3d at 945 (“It was well-established [in 2014] that a non-violent, non-
resisting, or only passively resisting suspect who is not under arrest has a right to be free from an
officer’s use of force.”). Assuming Wright’s version of the facts to be true, this case falls neatly
within the second category of cases.

       To summarize, a reasonable jury could find that Flagg’s actions constituted unreasonable
and constituted excessive force. It was clearly established as of November 4, 2016 that drawing
a weapon on a suspect who was not fleeing or posing a safety risk and tasering a suspect who
was not actively resisting arrest constituted excessive force. Therefore, we REVERSE the
district court’s grant of summary judgment on qualified immunity grounds to Flagg as to the
excessive-force claims.
 No. 19-3452                         Wright v. City of Euclid, et al.                      Page 18


         2.     Officer Williams

                a.      Violation of a Constitutional Right

         Wright’s excessive-force claim against Williams, based on his brandishing of a firearm
and use of the pepper spray, largely mirrors the claim against Flagg based on his similar use of a
firearm and tasing, and therefore the analysis is largely the same. The discussion of the Graham
factors as they relate to Williams is identical to the analysis of those factors as they concern
Flagg. The severity of the crime, whether Wright was a threat to the police, and whether Wright
actively resisted arrest all present questions of fact that should be decided by a jury.

         In Adams v. Metiva, 31 F.3d 375 (6th Cir. 1994), we held that summary judgment was
inappropriate for an excessive-force claim brought against police officers for the use of pepper
spray, when it remained genuinely disputed whether the plaintiff had committed a crime,
whether he posed a threat, and whether he was resisting arrest. Id. at 385–86; see also Vaughn v.
City of Lebanon, 18 F. App’x 252, 266–68 (6th Cir. 2001). Here, as discussed, it remains
genuinely disputed whether Wright had committed a crime, whether he posed a threat to officers,
and whether he was actively resisting arrest. See, e.g., Grawey v. Drury, 567 F.3d 302, 311 (6th
Cir. 2009) (“An officer has used excessive force when he pepper sprays a suspect who has not
been told she is under arrest and is not resisting arrest.”).

         The body-cam footage shows that while Flagg was attempting to gain control of Wright’s
right arm, Williams reached into the car with the can of pepper spray and sprayed Wright within
inches of his face. Wright’s expert opined that the use of pepper spray at this close distance was
unreasonably dangerous and violated nationally-accepted standards and protocols, which dictate
that pepper spray “should not be used on someone closer than three feet from the canister’s
nozzle.” R. 31-6 at PageID 1416. Further, this expert noted that the Euclid Police Department’s
use-of-force continuum indicates that pepper spray should be used only when an individual is
wrestling with or pushing an officer, not when the suspect is pulling away from an officer. This
testimony supports Wright’s argument that Williams acted unreasonably in his use of the pepper
spray.
 No. 19-3452                        Wright v. City of Euclid, et al.                        Page 19


        Furthermore, the evaluation of the reasonableness of officers’ use of force “considers the
effects of their actions, as any inquiry into a violation of the Fourth Amendment requires a
careful balancing of ‘the nature and quality of the intrusion on the individual’s Fourth
Amendment interests’ against the countervailing governmental interests at stake.”             Brown,
814 F.3d at 459 (quoting Graham, 490 U.S. at 396). As Wright’s expert opined, use of pepper
spray at such a close proximity risks significant injury, which is not present if the officer uses the
spray at a safe distance. This testimony and the other proof present a jury question as to whether
Williams’s use of the pepper spray constituted excessive force in violation of Wright’s
constitutional rights.

                b.       Clearly Established Right

        For reasons similar to those discussed above as they relate to Flagg’s use of his taser, we
hold that the right to be free from being pepper sprayed when a suspect is not actively resisting
arrest was also clearly established at the time of the encounter in question. See, e.g., Coffey, 933
F.3d at 589 (6th Cir. 2019) (“Drawing the line at a suspect’s active resistance defines the right at
a level of particularity appropriate for a claim pursued under § 1983.”); Smith, 874 F.3d at 945
(“It was well-established [in 2014] that a non-violent, non-resisting, or only passively resisting
suspect who is not under arrest has a right to be free from an officer’s use of force.”).

        Wright has produced evidence that would allow a reasonable juror to conclude that he
had not committed a serious crime, or any crime at all; that he was not a danger to the officers or
the public; and that he was not resisting arrest. Although the officers tell a different story, it
should be up to the jury to determine whose story is more credible. Therefore, we REVERSE as
to the excessive-force claim against Williams for deploying his pepper spray, as well as for
brandishing his firearm.

B.      Failure to Intervene

        Wright further claims that both Flagg and Williams failed to intervene to protect him
from alleged excessive force committed by the other. In order to establish such a claim, Wright
must prove that “the officer observed or had reason to know that the excessive force would be or
was being used and that the officer had both the opportunity and the means to prevent the harm
 No. 19-3452                        Wright v. City of Euclid, et al.                      Page 20


from occurring.” Smith, 874 F.3d at 945–46 (citing Turner v. Scott, 119 F.3d 425, 429 (6th Cir.
1997)). Wright maintains that because the officers were “practically on top of each other” when
they used the allegedly excessive force of the taser and pepper spray, Appellant’s Br. at 49, each
officer had the opportunity to prevent the other from using force.          However, we are not
persuaded that the evidence would allow a reasonable juror to find a constitutional violation as to
either of these failure-to-intervene claims.

       In Smith, we held that when one officer was “occupied trying to gain control of [the
plaintiff’s] arms while [the other officer] was deploying his taser,” no reasonable juror could find
that the officer had the opportunity and the means to prevent the excessive force. 874 F.3d at
946. So too here. Although Wright is correct that the officers were in close proximity to each
other, the body-cam footage from both Flagg and Williams shows that when Williams used
pepper spray on Wright, Flagg was struggling with Wright in an attempt to remove him from the
car. Like the officer in Smith, at the time Williams used his pepper spray, Flagg was preoccupied
with attempting to detain Wright. The body-cam footage shows Flagg grappling with Wright’s
arms when Williams reached into the car to deploy the pepper spray. This all happened within a
span of approximately ten seconds. Therefore, similar to the court’s holding in Smith, we hold
that no reasonable juror could find that Flagg had the opportunity and means to prevent Williams
from using pepper spray. See id.

       Likewise, no reasonable juror could find a constitutional violation in Williams’s failure to
prevent Flagg’s use of his taser. The body cam footage shows that Flagg tased Wright for
approximately five seconds during which time Williams reached around Flagg to pepper spray
Wright. The use of force happened almost simultaneously. Wright has failed to demonstrate
“that the incident lasted long enough for [Williams] to both perceive what was going on” with
Flagg’s tasering “and intercede to stop it.” Burgess, 735 F.3d at 475.

       Therefore, we AFFIRM the district court’s grant of summary judgment to Flagg and
Williams with respect to the failure-to-intervene claims.
 No. 19-3452                        Wright v. City of Euclid, et al.                      Page 21


C.     Fourth Amendment False Arrest

       Wright also maintains that the district court erred in granting summary judgment to the
officers on his Fourth Amendment false-arrest claim. For Wright to succeed on this claim, he
must prove that the police lacked probable cause to arrest him. Burley v. Gagacki, 834 F.3d 606,
613–14 (6th Cir. 2016). “An officer possesses probable cause when, at the moment the officer
seeks the arrest, ‘the facts and circumstances within the officer’s knowledge and of which [he]
had reasonably trustworthy information are sufficient to warrant a prudent man in believing that
the plaintiff had committed or was committing an offense.’” Wesley v. Campbell, 779 F.3d 421,
429 (6th Cir. 2015) (alterations omitted) (quoting Beck v. Ohio, 379 U.S. 89, 91 (1964)). “If
probable cause exists to arrest the suspect for any of the charged offenses, then the false arrest
claim must fail.” Fineout v. Kostanko, 780 F. App’x 317, 328 (6th Cir. 2019) (citing Lyons v.
City of Xenia, 417 F.3d 565, 573 (6th Cir. 2005)).

       Wright was charged for failure to use his turn signal, resisting arrest, obstructing official
business, and criminal trespass. However, for purposes of summary judgment, the officers
maintain that their bases for probable cause to arrest were Wright’s resisting arrest and his
obstruction of official business. We therefore address below whether probable cause existed for
the arrest based on these latter charges only.

       1.      Obstructing Official Business

       The officers contend that they arrested Wright, in part, “because he was … obstruct[ing]
official business.” Appellees’ Br. at 40. Under Ohio law, one is guilty of obstructing official
business if he, “without privilege to do so and with purpose to prevent, obstruct, or delay the
performance by a public official of any authorized act within the public official’s official
capacity, shall do any act that hampers or impedes a public official in the performance of the
public official’s lawful duties.” Ohio Rev. Code § 2921.31. With respect to the element of
“purpose to obstruct,” “[a] person acts purposely when it is his specific intention to cause a
certain result.” City of N. Ridgeville v. Reichbaum, 677 N.E.2d 1245, 1249 (Ohio 1996) (quoting
Ohio Rev. Code § 2901.22(A)). The statute also requires an affirmative act that interrupts police
business; “[a] person may not be convicted of the offense simply by doing nothing.” Lyons,
 No. 19-3452                        Wright v. City of Euclid, et al.                        Page 22


415 F.3d at 573 (citing State v. McCrone, 580 N.E.2d 468, 470–71 (Ohio 1989)). The act must
actually hamper or impede the officer in the performance of his duties, and “there must be some
substantial stoppage of the officer’s progress.” State v. Wellman, 879 N.E.2d 215, 219 (Ohio
2007) (quoting State v. Stephens, 387 N.E.2d 252, 253 (Ohio 1978)).

       On several occasions we have examined the Ohio statute that prohibits obstruction of
official business. The affirmative-act requirement requires more than a failure to comply with an
officer’s request. See Jones v. City of Elyria, 947 F.3d 905, 915 (6th Cir. 2020) (citing Patrizi v.
Huff, 690 F.3d 459, 464 (6th Cir. 2012)). Also, when a suspect pulls her hand away from the
police but otherwise complies with orders, she has not engaged in an affirmative act giving
officers probable cause to arrest for obstruction of official business. Smith v. City of Wyoming,
821 F.3d 697, 716 (6th Cir. 2016). Based on this standard, a reasonable juror could find that
Wright’s actions did not involve any affirmative act that obstructed police business. Wright
maintains that he was doing his best to comply, and the act of moving his arm was really an
attempt to maneuver his torso in the car so as to allow Flagg to remove him from the car—
despite the fact that the seizure was unlawful.

       Certainly, Wright’s and the officers’ respective versions of events are not necessarily
inconsistent. Wright could have earnestly believed that he was trying to help Flagg remove him
from the car, and Flagg could have simultaneously believed that Wright was trying to interfere
with his arrest. But viewing the facts in the light most favorable to Wright, a reasonable jury
could find that he did not engage in an affirmative act such as to give rise to probable cause that
he was obstructing official business.

       2.      Resisting Arrest

       In his deposition, Flagg conceded that he did not have probable cause to arrest Wright
until he started “resisting.” This puts the cart before the horse. When an underlying arrest is for
resisting arrest and nothing more, “the officers could not, as a matter of law, have probable cause
to arrest [Wright] where the underlying arrest was not lawful.” Osberry v. Slusher, 750 F. App’x
385, 395 (6th Cir. 2018); see Ohio Rev. Code § 2921.33(A) (“No person, recklessly or by force,
shall resist or interfere with a lawful arrest . . . .”) (emphasis added); see also Hoover v. Garfield
 No. 19-3452                          Wright v. City of Euclid, et al.                   Page 23


Heights Mun. Court, 802 F.2d 168, 174 (6th Cir. 1986) (“[W]e conclude that [Ohio Rev. Code]
§ 2921.33 indeed forbids only resisting a lawful arrest and does not prohibit resisting an unlawful
arrest.”). Because a reasonable jury could find that Flagg and Williams did not have probable
cause to arrest Wright prior to his alleged resistance, they are not entitled to summary judgment
that the arrest was justified. See Osberry, 750 F. App’x at 395.

                                              * * * * *

       If the jury finds that the officers lacked probable cause that Wright had engaged in any
illegal activity, then it would be clearly established that the officers falsely arrested him, in
violation of his Fourth Amendment rights. Indeed, the right to be free from arrest without
probable cause is a “quintessential example[] of [a] ‘clearly established’ constitutional right.”
Jones, 947 F.3d at 915. Wright has presented sufficient evidence for a reasonable jury to find no
probable cause—and no qualified immunity—for the arrest.

       Therefore we REVERSE the district court’s grant of summary judgment to Flagg and
Williams on the false-arrest claim.

D.     Extended Detention

       Wright also brought a claim for a violation of the Fourth Amendment based on his
extended detention after he posted bond. This claim is, in essence, derivative of his false-arrest
claim—that is, his detention was unreasonably extended without probable cause. The Fourth
Amendment “establishes the minimum constitutional ‘standards and procedures’ not just for
arrest but also the ensuing ‘detention.’” Manuel v. City of Joliet, 137 S. Ct. 911, 917 (2017)
(quoting Gerstein v. Pugh, 420 U.S. 103, 111 (1975)).

       1.      Constitutional Violation

       Before being taken into custody, Wright was hospitalized for his injuries from his
encounter with Flagg and Williams.          Both officers stayed in the hospital with Wright for
approximately four hours. Wright alleges that, during that time, the officers sought a CT scan of
Wright because they thought he was hiding drugs in his abdomen. At one point, hospital staff
took Wright to get an X-ray, but he refused to consent because of radiation concerns. According
 No. 19-3452                       Wright v. City of Euclid, et al.                    Page 24


to Wright, his refusal to be X-rayed infuriated Flagg and Williams, along with other unnamed
officers who were present at the hospital. The officers were so angry, according to Wright, that
they told him they were going to charge him because he would not be X-rayed.

       Upon discharge from the hospital, Wright was indeed arrested and taken to the Euclid
City Jail. Wright was booked at this facility at 10:49 p.m. His cousin arrived and posted bond
for Wright sometime between 11:00 p.m. and midnight. However, Wright was not then released.
Instead, after Wright posted bond, an officer told him that he had to be taken downtown to
undergo a body scan to see if he was hiding drugs in his body.

       At approximately 1:00 a.m., Wright was transferred from the Euclid City Jail to the
downtown Cuyahoga County Jail. When he arrived at this next facility, the staff asked him if he
had ingested any drugs or was hiding any drugs in his body. The jail staff informed him that his
bond had been paid, and he would be released once they had performed a body scan. County jail
staff then subjected Wright to a full-body scan.        The scan revealed that Wright was not
sequestering any drugs. Wright was finally released from custody at 3:55 a.m., approximately
four hours after he posted bond, and almost ten hours after Flagg and Williams detained him.

       Under Ohio law, when a defendant posts bail bond, he should be released from custody.
See Ohio Rev. Code § 2713.13 (“The bond, when accepted, shall be returned to the clerk’s
office, and the defendant shall be discharged.”). The approximate four-hour delay in his release
was caused by the designation of his arrest as drug-related. At the time the drug designation
occurred, both Wright and his SUV had been searched, and no drugs or other contraband had
been found. Nor were drugs or other contraband found on him when he was searched (again) by
officials at the jail. He was never charged with any drug-related offense.

       The Fourth Amendment protects “[t]he right of the people to be secure in their
persons . . . against unreasonable searches and seizures.” U.S. Const. amend. IV. As the text
indicates, and the Supreme Court has repeatedly affirmed, “the ultimate touchstone of the Fourth
Amendment is ‘reasonableness.’” Heien v. North Carolina, 574 U.S. 54, 60 (2014) (quoting
Riley v. California, 573 U.S. 373, 381)). Nothing happened from the time that Wright was
detained in his SUV to the time he posted bond to give officers probable cause to believe that
 No. 19-3452                        Wright v. City of Euclid, et al.                       Page 25


Wright was hiding drugs in his body. Despite the officers’ having no information that would
give them probable cause, Wright was seized for four hours after he should have been free to go.
A jury could find that this detention violated Wright’s right to be free from unreasonable
seizures.

         2.      Clearly Established Right

         Because the extended-detention claim, in essence, is derivative of Wright’s false-arrest
claim, the law was likewise clearly established that officers could not seize him without probable
cause.      As we stated above, the right to be free from arrest without probable cause is a
“quintessential example[] of [a] ‘clearly established’ constitutional right.” Jones, 947 F.3d at
915. Wright has presented sufficient evidence for a reasonable jury to find no probable cause—
and no qualified immunity—for the extended detention. Therefore, we REVERSE the district
court’s grant of summary judgment on Wright’s extended-detention claim.

E.       Fourth-Amendment Malicious Prosecution

         Wright next argues that the district court erred in granting summary judgment on his
claim of malicious prosecution in violation of the Fourth Amendment.             The Sixth Circuit
“recognizes a separate constitutionally cognizable claim of malicious prosecution under the
Fourth Amendment, which encompasses wrongful investigation, prosecution, conviction, and
incarceration.” Sykes v. Anderson, 625 F.3d 294, 308 (6th Cir. 2010) (cleaned up) (quoting
Barnes v. Wright, 449 F.3d 709, 715–16 (6th Cir. 2006)).

         To succeed on this claim, Wright must prove four things: (1) that a criminal prosecution
was initiated against him and that the defendant “made, influenced, or participated in the
decision to prosecute,” id. (alterations omitted) (quoting Fox v. Desoto, 489 F.3d 227, 237 (6th
Cir. 2007)); (2) that there was a lack of probable cause for the criminal prosecution; (3) that, as a
consequence of a legal proceeding, he suffered a deprivation of liberty apart from the initial
seizure; and (4) that the criminal proceeding was resolved in his favor, id. at 308–09; see also
Fox, 489 F.3d at 237.
 No. 19-3452                        Wright v. City of Euclid, et al.                      Page 26


          1.     The Officer Influenced or Participated in the Decision to Prosecute

          At minimum, “whether an officer influenced or participated in the decision to prosecute
hinges on the degree of the officer’s involvement and the nature of the officer’s actions.” Sykes,
625 F.3d at 311 n. 9; see Malley v. Briggs, 475 U.S. 335, 344–45 n. 7 (1986) (internal quotation
omitted) (construing § 1983 “against the background of tort liability,” in which people are
responsible for the “natural consequences” of their acts).

          Although Wright need not show that the officers influenced or participated with malice,
“there must be some element of blameworthiness or culpability in the participation,” that is,
“truthful participation in the prosecution is not actionable.” Johnson v. Moseley, 790 F.3d 649,
655 (6th Cir. 2015) (citing Sykes, 625 F.3d at 314). The most clear-cut way for a plaintiff to
satisfy this prong is to show that the officer gave false testimony before a grand jury. See Webb
v. United States, 789 F.3d 647, 663 (6th Cir. 2015). But an officer can also influence or
participate in the decision to prosecute by falsely prompting or urging a prosecutor’s decision to
bring charges in the first place. See id. at 666.

          Wright maintains that because Flagg conceded in his deposition that “by signing the
tickets he initiated prosecution against Lamar Wright,” the first prong of his malicious
prosecution claim is met. The “tickets,” or “traffic citations” as Flagg called them, were the
official citations that appear to have been filed in Euclid Municipal Court that charged Wright
with traffic violations, resisting arrest, obstructing official business, and criminal trespass. The
district court noted that Wright “makes general allegations that the officers fabricated evidence,
but points to no evidence of fabrication or falsification.” Wright, 2019 WL 2009453, at *9.
However, because the officers designated Wright’s arrest to be the result of a drug investigation,
despite knowing that Wright had no drugs when he was arrested and he was not arrested for any
drug-related offenses, a reasonable juror could find that Flagg and Williams engaged in
misrepresentation such that they were culpable in their involvement with Wright’s prosecution.
Cf. Jones, 947 F.3d at 918–19 (holding that filing a narrative report that falsely accuses a
defendant of resisting arrest establishes sufficient culpability for a federal malicious prosecution
claim).
 No. 19-3452                        Wright v. City of Euclid, et al.                       Page 27


       At the time of the designation, the officers knew two things of which they were unaware
when they pulled Wright over. First, they knew that Wright had a serious medical condition that
prevented him from exiting the vehicle. Second, they knew that Wright was not possessing any
drugs when they arrested him. These facts are sufficient for a reasonable juror to find the
officers made a false statement that Wright’s arrest was drug related, thereby establishing their
requisite involvement in his prosecution for a claim that it was malicious.

       2.      Lack of Probable Cause for the Prosecution

       For the same reasons set forth above regarding Wright’s false-arrest claim, a reasonable
jury could likewise find that there was a lack of probable cause to prosecute Wright.

       3.      Deprivation of Liberty

       We have recognized that an “initial arrest alone is an insufficient deprivation of liberty”
to support a claim for malicious prosecution. Noonan v. Cty. of Oakland, 683 F. App’x 455, 463
(6th Cir. 2017). Something more is required, and this circuit has held that “service with a
summons to appear at trial or some other court proceeding does not rise to the level of a
constitutional deprivation.” Id. at 463 (internal quotation marks and citation omitted).

       Wright argues that he suffered a deprivation of liberty beyond the initial seizure because
he was confined in the jail and in the hospital for many hours after the initial seizure but before
being released. That is enough to present a jury question under our caselaw. In Miller v.
Maddox, the plaintiff had suffered a deprivation of liberty apart from the initial seizure when she
remained detained for an extra forty-five minutes, paid a fee to be released, and was required to
participate in a pretrial release program. 866 F.3d 386, 393 (6th Cir. 2017).

       Here, Wright was booked into the Euclid jail at around 10:49 p.m., and he posted a
$905.00 bond between 11:00 p.m. and midnight. After he posted bond, Wright was not allowed
to leave. Rather, he was transported to the Cuyahoga County jail at around 1:00 a.m. He was
then required to undergo a full body scan as a result of the “drug investigation” that was noted on
his record. Wright was finally released at approximately 3:55 a.m. These facts would allow a
reasonable jury to find that Wright suffered a deprivation of liberty beyond the initial seizure.
 No. 19-3452                        Wright v. City of Euclid, et al.                      Page 28


       4.      Criminal Proceeding Resolved in his Favor

       The district court did not explicitly address this element of the action, but it is obviously
satisfied. The prosecution was terminated in Wright’s favor when the prosecutor dropped all
charges against him. See Ash v. Ash, 651 N.E.2d 945, 947–48 (Ohio 1995) (“[A]n unconditional,
unilateral dismissal of criminal charges or an abandonment of a prosecution by the prosecutor or
the complaining witness that results in the discharge of the accused generally constitutes a
termination in favor of the accused.”).

                                               * * * * *

       The right to be free from malicious prosecution is clearly established, but “the right is a
narrow one.” Coffey, 933 F.3d at 590 (citing Johnson, 790 F.3d at 649). “A police officer
violates a suspect’s clearly established right to freedom from malicious prosecution under the
Fourth Amendment ‘only when his deliberate or reckless falsehood results in arrest and
prosecution without probable cause.’” Johnson, 790 F.3d at 655 (quoting Newman v. Twp. of
Hamburg, 773 F.3d 769, 772 (6th Cir. 2014)). The officers’ designation of Wright’s arrest as
drug-related, given their knowledge of the circumstances of his arrest, including his medical
condition, is sufficient proof for a reasonable jury to find that the officers engaged in at least
reckless falsehood that resulted in his wrongful detention and intrusive search. Because Wright
has produced enough evidence such that a jury could find in his favor on the federal malicious-
prosecution claim, we REVERSE the district court’s grant of qualified immunity on this count.

F.     State-Law Claims

       In addition to his claims brought under § 1983, Wright brought state-law claims,
including malicious prosecution and intentional infliction of emotional distress. The district
court held that the officers were entitled to immunity under the Ohio statute that grants immunity
to municipal employees acting within the scope of their employment. For the reasons that
follow, we disagree with the district court.
 No. 19-3452                       Wright v. City of Euclid, et al.                     Page 29


       1.      State-Law Immunity

       The district court granted summary judgment to the officers and the City on Wright’s
state-law claims based on Ohio statutory immunity. Ohio Revised Code Chapter 2744 grants
immunity to political subdivisions and to employees of political subdivisions for actions arising
within the course or scope of their employment. The City is immune from suit for damages
unless one of several exceptions applies. Wright has not presented an argument as to why the
City should be liable for his state-law claims, so this argument is forfeited. See McPherson v.
Kelsey, 125 F.3d 989, 995 (6th Cir. 1997) (“[I]ssues adverted to in a perfunctory manner,
unaccompanied by some effort at developed argumentation, are deemed waived. It is not
sufficient for a party to mention a possible argument in the most skeletal way, leaving the court
to . . . put flesh on its bones.” (quoting Citizens Awareness Network, Inc. v. United States
Nuclear Regulatory Comm’n, 59 F.3d 284, 293–94 (1st Cir. 1995))).

       As to Flagg and Williams, Ohio law grants immunity from civil suits to employees of
political subdivisions unless:

       (a) the employee’s acts or omissions were manifestly outside the scope of their
           employment or official responsibilities;
       (b) the employee’s acts or omissions were with malicious purpose, in bad faith, or in a
           wanton or reckless manner; [or]
       (c) civil liability is expressly imposed by a section of the Revised Code.

Ohio Rev. Code § 2744.03(A)(6)(a)–(c). Because the officers’ conduct was within the scope of
their employment and because civil liability is not expressly imposed by another section of the
Ohio Revised Code, Wright must show that their acts were “with malicious purpose, in bad faith,
or in a wanton or reckless manner.” Id. § 2744.03(A)(6)(b).

       “When federal qualified immunity and Ohio state-law immunity under [Ohio Rev. Code]
§ 2744.03(A)(6) rest on the same questions of material fact, we may review the state-law
immunity defense ‘through the lens of federal qualified immunity analysis.’” Hopper v.
Plummer, 887 F.3d 744, 759 (6th Cir. 2018) (quoting Chappell v. City of Cleveland, 585 F.3d
901, 907 n.1 (6th Cir. 2009)). The officers’ state-law statutory-immunity defense therefore
“stands or falls with their federal qualified immunity defense.” Id. at 760; cf. Martin v. City of
 No. 19-3452                       Wright v. City of Euclid, et al.                     Page 30


Broadview Heights, 712 F.3d 951, 963 (6th Cir. 2013) (holding that “[a]s resolution of the state-
law immunity issue is heavily dependent on the same disputed material facts as the excessive
force determination under § 1983, the district court properly denied summary judgment to the
officers on the estate’s state-law claims”). For the reasons discussed above regarding qualified
immunity, we hold that the district court erred in granting statutory immunity to Flagg and
Williams.

       2.      State-Law Malicious Prosecution

       To sustain an action for malicious prosecution under Ohio law, Wright must establish:
(1) malice in instituting or continuing the prosecution; (2) lack of probable cause; and
(3) termination of the prosecution in his favor. Ash v. Ash, 651 N.E.2d 945, 947 (Ohio 1995).
Unlike Wright’s federal malicious-prosecution claim, his Ohio state law claim requires a
showing of malice. “Ohio law defines ‘malice’ as ‘an improper purpose, or any purpose other
than the legitimate interest of bringing an offender to justice.’” Harris v. Bornhorst, 513 F.3d
503, 521 (6th Cir. 2008) (quoting Criss v. Springfield Twp., 564 N.E.2d 440, 443 (Ohio 1990));
accord, e.g., Harris v. United States, 422 F.3d 322, 327 (6th Cir. 2005). Moreover, under Ohio
law, the absence of probable cause to seize a person raises an inference of malice. See, e.g.,
Melanowski v. Judy, 131 N.E. 360, 361 (Ohio 1921) (“If want of probable cause be proven, the
legal inference may be drawn that the proceedings were actuated by malice.”); Criss, 564 N.E.2d
at 443 (“If the basis for prosecution cannot be shown, those who made the decision will appear to
have acted with no basis—that is maliciously.”); accord, e.g., Bornhorst, 513 F.3d at 521;
Thacker v. City of Columbus, 328 F.3d 244, 261 (6th Cir. 2003).

       As explained above, Wright has demonstrated a genuine factual dispute as to whether
Officers Flagg and Williams lacked probable cause to arrest him. He has also demonstrated a
triable issue regarding whether Officers Flagg and Williams wrongfully, and perhaps even
willfully, designated his arrest as stemming from a drug investigation in order to detain him,
cause him to undergo a full body scan, and potentially justify their past actions. Under our case
law, this constitutes an “improper purpose” sufficient to overcome Defendants’ motion for
summary judgment. See, e.g., Jones, 947 F.3d at 921 (holding that “a reasonable jury could infer
malice on behalf of all three officers” where “the jury could find that all three officers lied in
 No. 19-3452                       Wright v. City of Euclid, et al.                       Page 31


ways that were material to the eventual decision to prosecute Jones, for the purpose of justifying
their own prior actions”).

       Therefore, we REVERSE the district court’s grant of summary judgment on the state law
malicious prosecution claim.

       3.      Intentional Infliction of Emotional Distress

       Though Wright dedicates some portion of his briefing to arguing that the district court
erred in granting summary judgment to the officers on his intentional-infliction-of-emotional-
distress claim, his argument is little more than a bare recitation of the elements of the cause of
action, and for that reason is forfeited. See United States v. Fowler, 819 F.3d 298, 309 (6th Cir.
2016) (“It is not sufficient for a party to mention a possible argument in [a] skeletal way, leaving
the court to put flesh on its bones.” (quoting El-Moussa v. Holder, 569 F.3d 250, 257 (6th Cir.
2009)). We therefore we AFFIRM the district court’s grant of summary judgment on this claim.

G.     Municipal Liability under 42 U.S.C. § 1983

       We now reach Wright’s Monell claim. Wright argues that the City is liable under § 1983
for its inadequate policy on use of force by police; ratification of use of excessive force by the
chief of police; failure to adequately train or supervise its officers on use of force; and a custom
of tolerance or inaction towards excessive force. The district court granted the City summary
judgment on this claim for want of a constitutional violation.

       The § 1983 cause of action may be exercised only against a “person who . . . causes to be
subjected, any citizen of the United States or other person within the jurisdiction thereof to the
deprivation of any rights, privileges, or immunities secured by the Constitution and laws.” 42
U.S.C. § 1983. Although “person” has been given a wide meaning under § 1983, Monell v.
Dep’t of Soc. Servs., 436 U.S. 658, 690 (1978), when the person is a municipality, liability
attaches only under a narrow set of circumstances. “A municipality may not be held liable under
§ 1983 on a respondeat superior theory—in other words, ‘solely because it employs a
tortfeasor.’” D’Ambrosio v. Marino, 747 F.3d 378, 388–89 (6th Cir. 2014) (quoting Monell,
436 U.S. at 691).    Instead, a plaintiff must show that “through its deliberate conduct, the
 No. 19-3452                        Wright v. City of Euclid, et al.                        Page 32


municipality was the ‘moving force’ behind the injury alleged.” Alman v. Reed, 703 F.3d 887,
903 (6th Cir. 2013) (quoting Bd. of Cty. Comm’rs v. Brown, 520 U.S. 397, 404 (1997)).
A plaintiff does this by showing that the municipality had a “policy or custom” that caused the
violation of his rights. Monell, 436 U.S. at 694.

       There are four methods of proving a municipality’s illegal policy or custom: the plaintiff
may prove “(1) the existence of an illegal official policy or legislative enactment; (2) that an
official with final decision making authority ratified illegal actions; (3) the existence of a policy
of inadequate training or supervision; or (4) the existence of a custom of tolerance or
acquiescence of federal rights violations.” Jackson v. City of Cleveland, 925 F.3d 793, 828 (6th
Cir. 2019) (citing Burgess, 735 F.3d at 478). Wright argues that he can establish municipal
liability under three of the four methods: (1) a custom of tolerance or acquiescence of federal
rights violations; (2) inadequate training and supervision; and (3) ratification of illegal actions by
an official with final decision-making authority.

       1.      Illegal Official Policy

       “[T]o satisfy the Monell requirements a plaintiff must identify the policy, connect the
policy to the city itself, and show that the particular injury was incurred because of the execution
of that policy.” Jackson, 925 F.3d at 829 (internal quotation omitted). Wright argues that the
Euclid Police Department has a custom of permitting or acquiescing to the use of excessive
force, which directly caused his injury. “[A] city may be liable under Monell for a policy of
permitting constitutional violations regardless of whether the policy is written.” Id. at 830; see
Monell, 436 U.S. at 691 (“Congress included customs and usages [in § 1983] . . . . Although not
authorized by written law, such practices . . . could well be so permanent and well settled as to
constitute a ‘custom or usage’ with the force of law.” (quoting Adickes v. S.H. Kress & Co., 398
U.S. 144, 167–68 (1970))). When proceeding under the first theory of Monell liability, Wright
must show that there were “formal rules or understandings—often but not always committed to
writing—that [were] intended to, and [did], establish fixed plans of action to be followed under
similar circumstances consistently and over time.” Pembaur v. City of Cincinnati, 475 U.S. 469,
480–81 (1986).
 No. 19-3452                       Wright v. City of Euclid, et al.                      Page 33


       Wright points to the Euclid Police department training on use of force to support his
argument that the City has a custom of allowing excessive force. First, there is the link in the
training materials to the YouTube video of the Chris Rock comedy sketch discussed earlier. As
noted, it is entitled “How not to get your ass kicked by the police!”. It includes numerous
vignettes depicting police officers beating African-American suspects, with commentary from
Rock about Rodney King and other matters as also described earlier.

       The evidence further includes, as also noted, a slide from the same training titled
“Defensive Tactics Training.” The slide includes a cartoon in which a stick figure police officer
in riot gear is shown beating a prone and unarmed civilian with a club with the caption
“protecting and serving the poop out of you.” R. 23 at PageID 808. Again, as noted, Murowsky
testified that he did not believe that the image conveys that the Euclid Police Department
“beat[s] the hell out of people,” R. 25 at PageID 1200, but that he didn’t know what other
message could possibly be taken away from the image.

       Finally, the use-of-force training contains a meme that depicts two officers with their
guns drawn and aimed at something.         It is captioned “Bed bug! Bed bug on my shoe!”.
Murowsky testified that he believed the image conveyed that the officers were overreacting to
and escalating a situation.

       Wright has produced enough evidence such that a reasonable jury could find that the
City’s custom surrounding use of force is so settled so as to have the force of law and that it was
the moving force behind violations of Wright’s constitutional rights. We therefore REVERSE
the district court’s grant of summary judgment on the issue of municipal liability under § 1983.

       2.      Failure to Train or Supervise

       “When determining whether a municipality has adequately trained its employees, ‘the
focus must be on adequacy of the training program in relation to the tasks the particular officers
must perform.” Jackson, 925 F.3d at 834 (quoting City of Canton v. Harris, 489 U.S. 378, 390
(1989)). A failure-to-supervise claim requires a showing of “prior instances of unconstitutional
conduct demonstrating that the municipality had ignored a history of abuse and was clearly on
 No. 19-3452                              Wright v. City of Euclid, et al.                                  Page 34


notice that the training in this particular area was deficient and likely to cause injury.” Burgess,
735 F.3d at 478.

         It is undisputed that Euclid police officers received some form of training on the proper
use of force, but a reasonable juror could find that this training is deficient. The Euclid Police
Department’s training policy and procedures mandate that “[t]he department will establish and
maintain a training committee.” However, no such training committee apparently has ever
existed.

         The City’s training seems to consist initially of simply reading the use-of-force policy to
the officers at rollcall until “it is believed that all the officers have heard it,” R. 31-7 at PageID
1508, which is then followed up with a one-or-two-page quiz that may or may not be given to
officers. The City also engages in some sort of practical training exercise in which officers are
given scenarios in which they may use force. But according to Murowsky, who implemented
these scenario-based trainings, the scenarios never changed, and the officers’ performances were
never evaluated.        And recall that this training also included the graphic and comedy skit
discussed above.1

         A reasonable jury could find that the City’s excessive-force training regimen and
practices gave rise to a culture that encouraged, permitted, or acquiesced to the use of
unconstitutional excessive force, and that, as a result, such force was used on Wright. Therefore,
we REVERSE the district court’s grant of summary judgment on Wright’s Monell claim based
on failure to train or supervise. See Jackson, 925 F.3d at 836–37 (holding that a single instance
of unconstitutional conduct can give rise to a failure-to-train claim when the natural consequence
of the municipality’s training regimen is that officials will violate constitutional rights); accord
Canton, 489 U.S. at 390 (“[I]t may happen that in the light of the duties assigned to specific
officers or employees the need for more or different training is so obvious . . . that the



         1
          Wright directs our attention to three other instances of police force by Euclid police officers to support the
notion that the police department “has a track record of excessive force and ongoing failure to take seriously the
need to properly . . . train officers on use of force.” Appellant’s Br. at 66. Those three instances of use of force,
while certainly troubling in their own right, cannot establish that the Euclid Police Department had a track record of
excessive force at the time of Wright’s constitutional injury because they all occurred after the incident with Wright.
 No. 19-3452                        Wright v. City of Euclid, et al.                      Page 35


policymakers of the city can reasonably be said to have been deliberately indifferent to the
need.”).

       3.       Ratification by Decision-Maker

       Wright argues that Chief Meyer’s failure to investigate numerous claims of excessive
force amounts to ratification of unconstitutional acts by a final decision-maker. A plaintiff can
establish municipal liability by showing that the municipality ratifies the unconstitutional acts of
its employees by failing to meaningfully investigate and punish allegations of unconstitutional
conduct. Leach v. Shelby Cty. Sheriff, 891 F.2d 1241, 1247–48 (6th Cir. 1990). Wright points us
to Chief Meyer’s lack of investigation and discipline in the other high-profile use-of-force cases
involving Euclid police officers, but those instances occurred after Wright’s encounter with
Flagg and Williams and cannot show that Meyer’s failure to investigate and punish the officers
involved in those uses of force led in any way to Wright’s injuries. However, Murowsky
testified that he had never heard of a use of force incident by a Euclid officer that seemed
inappropriate to him. That too moves the needle so that a reasonable jury could decide that use
of excessive force is ratified by the department. A reasonable jury could likewise find that
Meyer and Murowsky’s seeming failure to ever meaningfully investigate excessive force
complaints rises to the level of a ratification of use of force by a policymaker.

                                                  IV.

       It is very troubling that the City of Euclid’s law-enforcement training included jokes
about Rodney King—who was tased and beaten in one of the most infamous police encounters in
history—and a cartoon with a message that twists the mission of police. The offensive statements
and depictions in the training contradict the ethical duty of law enforcement officer “to serve the
community; to safeguard lives and property; to protect the innocent against deception, the weak
against oppression or intimidation and the peaceful against violence or disorder; and to respect
the constitutional rights of all to liberty, equality, and justice.” Law Enforcement Code of Ethics,
International   Association    of   Chiefs   of    Police,   https://www.theiacp.org/resources/law-
enforcement-code-of-ethics.
 No. 19-3452                      Wright v. City of Euclid, et al.                     Page 36


       There is enough evidence to present jury questions that preclude summary judgment on
the Monell claims under 42 U.S.C. § 1983. Likewise, the evidence regarding Wright’s encounter
with the police present jury questions that preclude summary judgment on the excessive-force,
false-arrest, extended-detention, and federal malicious-prosecution claims under § 1983 as well.
Accordingly, for the reasons stated above, we AFFIRM in part, REVERSE in part, and
REMAND to the district court for further proceedings.

```

---
