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

## GROUP: _overhaul2/lake/cases/Nieves v. Bartlett.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Nieves v. Bartlett
type: case
citation: "587 U.S. 391 (2019)"
parallel_cite: 139 S. Ct. 1715
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2019
date_decided: ""
docket: 17-1174
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
  opinion_url: "https://www.courtlistener.com/opinion/9231236/nieves-v-bartlett/"
  cluster_id: 9231236
  opinion_id: null
  identity_checked: true
lake:
  record_id: Nieves v. Bartlett
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Retaliatory Arrest]]"
    role: Key
related:
  - "[[Gonzalez v. Trevino]]"
  - "[[Retaliatory Arrest]]"
tags:
  - case
  - first-amendment
  - retaliatory-arrest
  - probable-cause
  - section-1983
holding: "A First Amendment retaliatory-arrest plaintiff must generally plead and prove the absence of probable cause for the arrest, subject to a narrow exception when he presents objective evidence that otherwise similarly situated individuals not engaged in the same protected speech were not arrested."
---

# Nieves v. Bartlett

*587 U.S. 391 (2019)* (No. 17-1174) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 9231236 → opinion 9226038; quote string-matched to the CL opinion text 2026-07-07 (CL text carries S. Ct. star-pagination; U.S. pincite corroborated by Gonzalez v. Trevino, 602 U.S. 653). S9 promotes. -->

## Background
Russell Bartlett was arrested for disorderly conduct and resisting arrest during "Arctic Man," a raucous winter sports festival in Alaska, after tense encounters with two state troopers — he had declined to speak with one officer and had intervened when the other questioned a minor. Bartlett sued under 42 U.S.C. § 1983, alleging the officers arrested him in retaliation for that protected speech in violation of the First Amendment. The Ninth Circuit held that the existence of probable cause did not defeat his retaliatory-arrest claim.

## Issue
Whether probable cause defeats a First Amendment retaliatory-arrest claim under § 1983, and if so, whether any exception exists.

## Rule
As a general rule, a plaintiff bringing a retaliatory-arrest claim "must plead and prove the absence of probable cause for the arrest." 587 U.S., at 402. Because the presence of probable cause will be at issue in virtually every such case and its objective character screens out weak claims of retaliatory animus, the no-probable-cause requirement is the threshold a plaintiff must clear. The Court recognized one narrow exception: "we conclude that the no-probable-cause requirement should not apply when a plaintiff presents objective evidence that he was arrested when otherwise similarly situated individuals not engaged in the same sort of protected speech had not been." — 587 U.S. at 406. ^pin-406

## Application
Bartlett's claim failed at the threshold. Probable cause supported his arrest for disorderly conduct and resisting, and he offered no objective evidence that officers typically exercise their discretion not to arrest others engaged in similar conduct but not in protected speech. Absent that comparative showing, the general no-probable-cause bar controlled and his retaliatory-arrest claim could not proceed. The Court grounded the rule in the practical difficulty of disentangling protected speech from legitimate arrest justifications and in the analogous causation framework of *Hartman v. Moore*.

## Conclusion
The judgment of the Ninth Circuit was **reversed** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. Roberts, C.J., delivered the opinion of the Court; Justices Thomas, Gorsuch, and Ginsburg concurred in part and/or dissented in part, and Justice Sotomayor dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Nieves* remains the controlling framework for retaliatory-arrest claims; the Supreme Court construed its exception in *[[Gonzalez v. Trevino]]* (2024), rejecting a demand for narrow comparator evidence.

## Appears on
- [[Retaliatory Arrest]] — *Key*

## Sources
- [*Nieves v. Bartlett*, 587 U.S. 391 (2019)](https://www.courtlistener.com/opinion/9231236/nieves-v-bartlett/) — pinpoint: 406 (exception; Opinion of the Court). Quote string-matched to the CL opinion text (139 S. Ct. 1715, at 1727) 2026-07-07; U.S.-reporter pincite corroborated by *Gonzalez v. Trevino*, 602 U.S. 653, 658 (2024).
- [*Gonzalez v. Trevino*, 602 U.S. 653 (2024)](https://www.courtlistener.com/opinion/10600071/gonzalez-v-trevino/) — construing the *Nieves* exception.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "651d221b6213eee2", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Nieves v. Bartlett"}, "payload": {"all": [{"cite": "587 U.S. 391", "page": "391", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "587"}, {"cite": "139 S. Ct. 1715", "page": "1715", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "139"}], "display": "587 U.S. 391", "official": {"cite": "587 U.S. 391", "page": "391", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "587"}, "official_selection_present": true, "record_id": "Nieves v. Bartlett"}}
{"assertion_id": "5a805406dde9b36f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Nieves v. Bartlett"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Nieves v. Bartlett", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Nieves v. Bartlett

```json
{
  "schema_version": "s2.v1",
  "record_id": "Nieves v. Bartlett",
  "status": "under_review",
  "identity": {
    "case_name": "Nieves v. Bartlett",
    "case_name_short": "Nieves",
    "case_name_full": "Luis A. NIEVES v. Russell P. BARTLETT",
    "input_case_name": "Nieves v. Bartlett",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2019,
    "docket": "17-1174",
    "cluster_id": 9231236,
    "lead_opinion_id": 9226038,
    "sibling_ids": [],
    "absolute_url": "/opinion/9231236/nieves-v-bartlett/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "587 U.S. 391",
      "volume": "587",
      "reporter": "U.S.",
      "page": "391",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "139 S. Ct. 1715",
        "volume": "139",
        "reporter": "S. Ct.",
        "page": "1715",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "587 U.S. 391",
        "volume": "587",
        "reporter": "U.S.",
        "page": "391",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "139 S. Ct. 1715",
        "volume": "139",
        "reporter": "S. Ct.",
        "page": "1715",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "587 U.S. 391",
    "official_selection": {
      "court_class": "scotus",
      "selected": "587 U.S. 391",
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
    "date_created": "2026-07-06T12:14:24Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:14:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:14:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:14:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:14:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "nieves-v-bartlett--9231236",
      "to_record_id": "Nieves v. Bartlett",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Nieves v. Bartlett

```
<opinion type="majority">
<author id="p-7">Chief Justice ROBERTS delivered the opinion of the Court.</author>
<p id="p-8"><a class="page-label" data-citation-index="1" data-label="1720" href="#p1720" id="p1720">*1720</a>Respondent Russell Bartlett sued petitioners-two police officers-alleging that they retaliated against him for his protected First Amendment speech by arresting him for disorderly conduct and resisting arrest. The officers had probable cause to arrest Bartlett, and we now decide whether that fact defeats Bartlett's First Amendment claim as a matter of law.</p>
<p id="p-9">I</p>
<p id="p-10">A</p>
<p id="p-11">Bartlett was arrested during "Arctic Man," a weeklong winter sports festival held in the remote Hoodoo Mountains near Paxson, Alaska. Paxson is a small community that normally consists of a few dozen residents. But once a year, upwards of 10,000 people descend on the area for Arctic Man, an event known for both extreme sports and extreme alcohol consumption. The mainstays are high-speed ski and snowmobile races, bonfires, and parties. During that week, the Arctic Man campground briefly becomes one of the largest and most raucous cities in Alaska.</p>
<p id="p-12">The event poses special challenges for law enforcement. Snowmobiles, alcohol, and freezing temperatures do not always mix well, and officers spend much of the week responding to snowmobile crashes, breaking up fights, and policing underage drinking. Given the remote location of the event, Alaska flies in additional officers from around the State to provide support. Still, the number of police remains limited. Even during the busiest periods of the event, only six to eight officers are on patrol at a time.</p>
<p id="p-13">On the last night of Arctic Man 2014, Sergeant Luis Nieves and Trooper Bryce Weight arrested Bartlett. The parties dispute certain details about the arrest but agree on the general course of events, some of which were captured on video by a local news reporter.</p>
<p id="p-14">At around 1:30 a.m., Sergeant Nieves and Bartlett first crossed paths. Nieves was asking some partygoers to move their beer keg inside their RV because minors had been making off with alcohol. According to Nieves, Bartlett began belligerently yelling to the RV owners that they should not speak with the police. Nieves approached Bartlett to explain the situation, but Bartlett was highly intoxicated and yelled at him to leave. Rather than escalate the situation, Nieves left. Bartlett disputes that account. According to Bartlett, he was not drunk at that time and never yelled at Nieves. He claims it was Nieves who became aggressive when Bartlett refused to speak with him.</p>
<p id="p-15">Several minutes later, Bartlett saw Trooper Weight asking a minor whether he and his underage friends had been drinking. According to Weight, Bartlett approached in an aggressive manner, stood between Weight and the teenager, and yelled with slurred speech that Weight should not speak with the minor. Weight claims that Bartlett then stepped very close to him in a combative way, so Weight pushed him back. Sergeant Nieves saw the <a class="page-label" data-citation-index="1" data-label="1721" href="#p1721" id="p1721">*1721</a>confrontation and rushed over, arriving right after Weight pushed Bartlett. Nieves immediately initiated an arrest, and when Bartlett was slow to comply with his orders, the officers forced him to the ground and threatened to tase him.</p>
<p id="p-16">Again, Bartlett tells a different story. He denies being aggressive, and claims that he stood close to Weight only in an effort to speak over the loud background music. And he was slow to comply with Nieves's orders, not because he was resisting arrest, but because he did not want to aggravate a back injury. After Bartlett was handcuffed, he claims that Nieves said: "[B]et you wish you would have talked to me now." <extracted-citation index="0" url="https://cite.case.law/citations/?q=712%20Fed.%20Appx.%20613"><span class="citation" data-id="4213549"><a href="/opinion/4436296/russell-bartlett-v-luis-nieves/" aria-description="Citation for case: Russell Bartlett v. Luis Nieves">712 Fed. Appx. 613</a></span></extracted-citation>, 616 (C.A.9 2017).</p>
<p id="p-17">The officers took Bartlett to a holding tent, where he was charged with disorderly conduct and resisting arrest. He had sustained no injuries during the episode and was released a few hours later.</p>
<p id="p-18">B</p>
<p id="p-19">The State ultimately dismissed the criminal charges against Bartlett, and Bartlett then sued the officers under <extracted-citation index="1" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation>, which provides a cause of action for state deprivations of federal rights. As relevant here, he claimed that the officers violated his First Amendment rights by arresting him in retaliation for his speech. The protected speech, according to Bartlett, was his refusal to speak with Nieves earlier in the evening and his intervention in Weight's discussion with the underage partygoer. The officers responded that they arrested Bartlett because he interfered with an investigation and initiated a physical confrontation with Weight. The District Court granted summary judgment for the officers. The court determined that the officers had probable cause to arrest Bartlett and held that the existence of probable cause precluded Bartlett's First Amendment retaliatory arrest claim.</p>
<p id="p-20">The Ninth Circuit disagreed. <extracted-citation index="2" url="https://cite.case.law/citations/?q=712%20Fed.%20Appx.%20613"><span class="citation" data-id="4213549"><a href="/opinion/4436296/russell-bartlett-v-luis-nieves/" aria-description="Citation for case: Russell Bartlett v. Luis Nieves">712 Fed. Appx. 613</a></span></extracted-citation>. Relying on its prior decision in <em>Ford v. Yakima</em> , <extracted-citation case-ids="3662237" index="3" url="https://cite.case.law/f3d/706/1188/"><span class="citation" data-id="9502716"><a href="/opinion/820004/eddie-ford-v-city-of-yakima/" aria-description="Citation for case: Eddie Ford v. City of Yakima">706 F. 3d 1188</a></span></extracted-citation> (2013), the court held that a plaintiff can prevail on a First Amendment retaliatory arrest claim even in the face of probable cause for the arrest. According to the Ninth Circuit, Bartlett needed to show only (1) that the officers' conduct would "chill a person of ordinary firmness from future First Amendment activity," and (2) that he had advanced evidence that would "enable him ultimately to prove that the officers' desire to chill his speech was a but-for cause" of the arrest. <extracted-citation index="4" url="https://cite.case.law/citations/?q=712%20Fed.%20Appx.%20613"><span class="citation" data-id="4213549"><a href="/opinion/4436296/russell-bartlett-v-luis-nieves/#616" aria-description="Citation for case: Russell Bartlett v. Luis Nieves">712 Fed. Appx. at 616</a></span></extracted-citation> (internal quotation marks omitted). The court concluded that Bartlett had satisfied both requirements: A retaliatory arrest is sufficiently chilling, and Bartlett had presented enough evidence that his speech was a but-for cause of the arrest. The only causal evidence relied on by the court was Bartlett's affidavit alleging that Sergeant Nieves said "bet you wish you would have talked to me now." If that allegation were true, the court reasoned, a jury might conclude that the officers arrested Bartlett in retaliation for his statements earlier that night.</p>
<p id="p-21">The officers petitioned for review in this Court, and we granted certiorari. 585 U.S. ----, <extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="5" url="https://cite.case.law/s-ct/138/2709/"><span class="citation multiple-matches"><a href="/c/S.Ct./138/2709/">138 S.Ct. 2709</a></span></extracted-citation>, <extracted-citation index="6" url="https://cite.case.law/citations/?q=201%20L.%20Ed.%202d%201095"><span class="citation no-link">201 L.Ed.2d 1095</span></extracted-citation> (2018).</p>
<p id="p-22">II</p>
<p id="p-23">We are asked to resolve whether probable cause to make an arrest defeats a claim that the arrest was in retaliation for speech protected by the First Amendment. We have considered this issue twice in recent years. On the first occasion, we ultimately left the question unanswered because we decided the case on the alternative ground of qualified immunity. See <a class="page-label" data-citation-index="1" data-label="1722" href="#p1722" id="p1722">*1722</a><em>Reichle v. Howards</em> , <extracted-citation case-ids="12190092" index="7" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">566 U.S. 658</a></span></extracted-citation>, <extracted-citation case-ids="12190092" index="8" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">132 S.Ct. 2088</a></span></extracted-citation>, <extracted-citation case-ids="12190092" index="9" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">182 L.Ed.2d 985</a></span></extracted-citation> (2012). We took up the question again last Term in <em>Lozman v.Riviera Beach,</em> 585 U.S. ----, <extracted-citation case-ids="12612344" index="10" url="https://cite.case.law/s-ct/138/1945/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct. 1945</a></span></extracted-citation>, <extracted-citation case-ids="12612344" index="11" url="https://cite.case.law/s-ct/138/1945/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">201 L.Ed.2d 342</a></span></extracted-citation> (2018). <em>Lozman</em> involved unusual circumstances in which the plaintiff was arrested pursuant to an alleged "official municipal policy" of retaliation. <em><extracted-citation case-ids="12612344" index="12" url="https://cite.case.law/s-ct/138/1945/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="13" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct., at 1954</a></span></extracted-citation>. Because those facts were "far afield from the typical retaliatory arrest claim," we reserved judgment on the broader question presented and limited our holding to arrests that result from official policies of retaliation. <em><extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="14" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="15" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct., at 1953</a></span>-1954</extracted-citation>. In such cases, we held, probable cause does not categorically bar a plaintiff from suing the municipality. <em><extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="16" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">Id.,</a></span></extracted-citation></em> at ---- - ----, <extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="17" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct., at 1954</a></span>-1955</extracted-citation>. We now take up the question once again, this time in a more representative case.</p>
<p id="p-24">A</p>
<p id="p-25">"[A]s a general matter the First Amendment prohibits government officials from subjecting an individual to retaliatory actions" for engaging in protected speech. <em>Hartman v. Moore</em> , <extracted-citation case-ids="3275855" index="18" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. 250</a></span></extracted-citation>, 256, <extracted-citation case-ids="3275855" index="19" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="20" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">164 L.Ed.2d 441</a></span></extracted-citation> (2006). If an official takes adverse action against someone based on that forbidden motive, and "non-retaliatory grounds are in fact insufficient to provoke the adverse consequences," the injured person may generally seek relief by bringing a First Amendment claim. <em><extracted-citation case-ids="3275855" index="21" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Ibid.</a></span></extracted-citation></em> (citing <em>Crawford-El v. Britton</em> , <extracted-citation case-ids="11503978" index="22" url="https://cite.case.law/us/523/574/#p593"><span class="citation" data-id="9433625"><a href="/opinion/118203/crawford-el-v-britton/" aria-description="Citation for case: Crawford-El v. Britton">523 U.S. 574</a></span></extracted-citation>, 593, <extracted-citation case-ids="11503978" index="23" url="https://cite.case.law/us/523/574/#p593"><span class="citation" data-id="9433625"><a href="/opinion/118203/crawford-el-v-britton/" aria-description="Citation for case: Crawford-El v. Britton">118 S.Ct. 1584</a></span></extracted-citation>, <extracted-citation case-ids="11503978" index="24" url="https://cite.case.law/us/523/574/#p593"><span class="citation" data-id="9433625"><a href="/opinion/118203/crawford-el-v-britton/" aria-description="Citation for case: Crawford-El v. Britton">140 L.Ed.2d 759</a></span></extracted-citation> (1998) ; <em>Mt. Healthy City Bd. of Ed. v. Doyle</em> , <extracted-citation case-ids="8150" index="25" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">429 U.S. 274</a></span></extracted-citation>, 283-284, <extracted-citation case-ids="8150" index="26" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">97 S.Ct. 568</a></span></extracted-citation>, <extracted-citation case-ids="8150" index="27" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">50 L.Ed.2d 471</a></span></extracted-citation> (1977) ).</p>
<p id="p-26">To prevail on such a claim, a plaintiff must establish a "causal connection" between the government defendant's "retaliatory animus" and the plaintiff's "subsequent injury." <em>Hartman</em> , <extracted-citation case-ids="3275855" index="28" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. at 259</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="29" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>. It is not enough to show that an official acted with a retaliatory motive and that the plaintiff was injured-the motive must <em>cause</em> the injury. Specifically, it must be a "but-for" cause, meaning that the adverse action against the plaintiff would not have been taken absent the retaliatory motive. <em><extracted-citation case-ids="3275855" index="30" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="3275855" index="30" url="https://cite.case.law/us/547/250/#p256"> at 260</extracted-citation>, <extracted-citation case-ids="3275855" index="31" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation> (recognizing that although it "may be dishonorable to act with an unconstitutional motive," an official's "action colored by some degree of bad motive does not amount to a constitutional tort if that action would have been taken anyway").</p>
<p id="p-27">For example, in <em>Mt. Healthy</em> , a teacher claimed that a school district refused to rehire him in retaliation for his protected speech. We held that even if the teacher's "protected conduct played a part, substantial or otherwise, in [the] decision not to rehire," he was not entitled to reinstatement "if the same decision would have been reached" absent his protected speech. <extracted-citation case-ids="8150" index="32" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">429 U.S. at 285</a></span></extracted-citation>, <extracted-citation case-ids="8150" index="33" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">97 S.Ct. 568</a></span></extracted-citation>. Regardless of the motives of the school district, we concluded that the First Amendment "principle at stake is sufficiently vindicated if such an employee is placed in no worse a position than if he had not engaged in the [protected speech]." <em><extracted-citation case-ids="8150" index="34" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="8150" index="34" url="https://cite.case.law/us/429/274/#p283"> at 285-286</extracted-citation>, <extracted-citation case-ids="8150" index="35" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">97 S.Ct. 568</a></span></extracted-citation>.</p>
<p id="p-28">For a number of retaliation claims, establishing the causal connection between a defendant's animus and a plaintiff's injury is straightforward. Indeed, some of our cases in the public employment context "have simply taken the evidence of the motive and the discharge as sufficient for a circumstantial demonstration that the one caused the other," shifting the burden to the defendant to show he would have taken the challenged action even without the impermissible motive. <em>Hartman</em> , <extracted-citation case-ids="3275855" index="36" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. at 260</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="37" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation> (citing <em>Mt. Healthy</em> , <extracted-citation case-ids="8150" index="38" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">429 U.S. at 287</a></span></extracted-citation>, <extracted-citation case-ids="8150" index="39" url="https://cite.case.law/us/429/274/#p283"><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">97 S.Ct. 568</a></span></extracted-citation> ;</p>
<p id="p-29"><a class="page-label" data-citation-index="1" data-label="1723" href="#p1723" id="p1723">*1723</a><em>Arlington Heights v. Metropolitan Housing Development Corp.</em> , <extracted-citation case-ids="6951" index="40" url="https://cite.case.law/us/429/252/#p270"><span class="citation" data-id="9426633"><a href="/opinion/109573/village-of-arlington-heights-v-metropolitan-housing-development-corp/" aria-description="Citation for case: Village of Arlington Heights v. Metropolitan Housing...">429 U.S. 252</a></span></extracted-citation>, 270, n. 21, <extracted-citation case-ids="6951" index="41" url="https://cite.case.law/us/429/252/#p270"><span class="citation" data-id="9426633"><a href="/opinion/109573/village-of-arlington-heights-v-metropolitan-housing-development-corp/" aria-description="Citation for case: Village of Arlington Heights v. Metropolitan Housing...">97 S.Ct. 555</a></span></extracted-citation>, <extracted-citation case-ids="6951" index="42" url="https://cite.case.law/us/429/252/#p270"><span class="citation" data-id="9426633"><a href="/opinion/109573/village-of-arlington-heights-v-metropolitan-housing-development-corp/" aria-description="Citation for case: Village of Arlington Heights v. Metropolitan Housing...">50 L.Ed.2d 450</a></span></extracted-citation> (1977) ). But the consideration of causation is not so straightforward in other types of retaliation cases.</p>
<p id="p-30">In <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> , for example, we addressed retaliatory prosecution cases, where "proving the link between the defendant's retaliatory animus and the plaintiff's injury ... 'is usually more complex than it is in other retaliation cases.' " <em>Lozman</em> , 585 U.S., at ----, <extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="43" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct., at 1952</a></span>-1953</extracted-citation> (quoting <em>Hartman</em> , <extracted-citation case-ids="3275855" index="44" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. at 261</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="45" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation> ). Unlike most retaliation cases, in retaliatory prosecution cases the official with the malicious motive does not carry out the retaliatory action himself-the decision to bring charges is instead made by a prosecutor, who is generally immune from suit and whose decisions receive a presumption of regularity. <em>Lozman</em> , 585 U.S., at ---- - ----, <extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="46" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct., at 1952</a></span>-1953</extracted-citation><em>.</em> Thus, even when an officer's animus is clear, it does not necessarily show that the officer "induced the action of a prosecutor who would not have pressed charges otherwise." <em>Hartman</em> , <extracted-citation case-ids="3275855" index="47" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. at 263</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="48" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>.</p>
<p id="p-31">To account for this "problem of causation" in retaliatory prosecution claims, <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> adopted the requirement that plaintiffs plead and prove the absence of probable cause for the underlying criminal charge. <em><extracted-citation case-ids="3275855" index="49" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Ibid.</a></span></extracted-citation></em> ; see <em><extracted-citation case-ids="3275855" index="50" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">id.,</a></span></extracted-citation></em><extracted-citation case-ids="3275855" index="50" url="https://cite.case.law/us/547/250/#p256"> at 265-266</extracted-citation>, <extracted-citation case-ids="3275855" index="51" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>. As <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> explained, that showing provides a "distinct body of highly valuable circumstantial evidence" that is "apt to prove or disprove" whether retaliatory animus actually caused the injury: "Demonstrating that there was no probable cause for the underlying criminal charge will tend to reinforce the retaliation evidence and show that retaliation was the but-for basis for instigating the prosecution, while establishing the existence of probable cause will suggest that prosecution would have occurred even without a retaliatory motive." <em><extracted-citation case-ids="3275855" index="52" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="3275855" index="52" url="https://cite.case.law/us/547/250/#p256"> at 261</extracted-citation>, <extracted-citation case-ids="3275855" index="53" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>. Requiring plaintiffs to plead and prove the absence of probable cause made sense, we reasoned, because the existence of probable cause will be at issue in "practically all" retaliatory prosecution cases, has "high probative force," and thus "can be made mandatory with little or no added cost." <em><extracted-citation case-ids="3275855" index="54" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="3275855" index="54" url="https://cite.case.law/us/547/250/#p256"> at 265</extracted-citation>, <extracted-citation case-ids="3275855" index="55" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>. Moreover, imposing that burden on plaintiffs was necessary to suspend the presumption of regularity underlying the prosecutor's charging decision-a presumption we "do not lightly discard." <em><extracted-citation case-ids="3275855" index="56" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="3275855" index="56" url="https://cite.case.law/us/547/250/#p256"> at 263</extracted-citation>, <extracted-citation case-ids="3275855" index="57" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation> ; see also <em><extracted-citation case-ids="3275855" index="58" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">id.,</a></span></extracted-citation></em><extracted-citation case-ids="3275855" index="58" url="https://cite.case.law/us/547/250/#p256"> at 265</extracted-citation>, <extracted-citation case-ids="3275855" index="59" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>. Thus, <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> requires plaintiffs in retaliatory prosecution cases to show more than the subjective animus of an officer and a subsequent injury; plaintiffs must also prove as a threshold matter that the decision to press charges was objectively unreasonable because it was not supported by probable cause.</p>
<p id="p-32">B</p>
<p id="p-33">Officers Nieves and Weight argue that the same no-probable-cause requirement should apply to First Amendment retaliatory arrest claims. Their primary contention is that retaliatory arrest claims involve causal complexities akin to those we identified in <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> , and thus warrant the same requirement that plaintiffs plead and prove the absence of probable cause. Brief for Petitioners 20-30.</p>
<p id="p-34">As a general matter, we agree. As we recognized in <em><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">Reichle</a></span></em> and reaffirmed in <em>Lozman</em> , retaliatory arrest claims face some of the same challenges we identified in <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> : Like retaliatory prosecution cases, "retaliatory arrest cases also present a tenuous causal connection between the defendant's alleged animus and the plaintiff's injury." <em>Reichle</em> , <extracted-citation case-ids="12190092" index="60" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">566 U.S. at 668</a></span></extracted-citation>, <extracted-citation case-ids="12190092" index="61" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">132 S.Ct. 2088</a></span></extracted-citation>. The causal inquiry is complex <a class="page-label" data-citation-index="1" data-label="1724" href="#p1724" id="p1724">*1724</a>because protected speech is often a "wholly legitimate consideration" for officers when deciding whether to make an arrest. <em><extracted-citation case-ids="12190092" index="62" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">Ibid.</a></span></extracted-citation></em> ; <em>Lozman</em> , 585 U.S., at ----, <extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="63" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct., at 1953</a></span></extracted-citation>. Officers frequently must make "split-second judgments" when deciding whether to arrest, and the content and manner of a suspect's speech may convey vital information-for example, if he is "ready to cooperate" or rather "present[s] a continuing threat." <em><extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="64" url="https://cite.case.law/s-ct/138/2709/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">Id.</a></span></extracted-citation></em> , at ----, <extracted-citation case-ids="12614054,12614055,12614056,12614057,12614058" index="65" url="https://cite.case.law/s-ct/138/2709/">138 S.Ct., at </extracted-citation>1953 (citing <em>District of Columbiav.Wesby</em> , 583 U.S. ----, ----, <extracted-citation case-ids="12615996" index="66" url="https://cite.case.law/s-ct/138/577/#p587"><span class="citation" data-id="4238107"><a href="/opinion/4460854/district-of-columbia-v-wesby/" aria-description="Citation for case: District of Columbia v. Wesby">138 S.Ct. 577</a></span></extracted-citation>, 587-588, <extracted-citation case-ids="12615996" index="67" url="https://cite.case.law/s-ct/138/577/#p587"><span class="citation" data-id="4238107"><a href="/opinion/4460854/district-of-columbia-v-wesby/" aria-description="Citation for case: District of Columbia v. Wesby">199 L.Ed.2d 453</a></span></extracted-citation> (2018) ("suspect's untruthful and evasive answers to police questioning could support probable cause")). Indeed, that kind of assessment happened in this case. The officers testified that they perceived Bartlett to be a threat based on a combination of the content and tone of his speech, his combative posture, and his apparent intoxication.</p>
<p id="p-35">In addition, "[l]ike retaliatory prosecution cases, evidence of the presence or absence of probable cause for the arrest will be available in virtually every retaliatory arrest case." <em>Reichle,</em> <extracted-citation case-ids="12190092" index="68" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">566 U.S. at 668</a></span></extracted-citation>, <extracted-citation case-ids="12190092" index="69" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">132 S.Ct. 2088</a></span></extracted-citation>. And because probable cause speaks to the objective reasonableness of an arrest, see <em>Ashcroft v. al-Kidd</em> , <extracted-citation case-ids="5924024,12459540" index="70" url="https://cite.case.law/us/563/731/"><span class="citation" data-id="7262676"><a href="/opinion/7344719/ashcroft-v-al-kidd/" aria-description="Citation for case: Ashcroft v. al-Kidd">563 U.S. 731</a></span></extracted-citation>, 736, <extracted-citation case-ids="5924024,12459540" index="71" url="https://cite.case.law/us/563/731/"><span class="citation" data-id="7262676"><a href="/opinion/7344719/ashcroft-v-al-kidd/" aria-description="Citation for case: Ashcroft v. al-Kidd">131 S.Ct. 2074</a></span></extracted-citation>, <extracted-citation case-ids="5924024,12459540" index="72" url="https://cite.case.law/us/563/731/"><span class="citation" data-id="7262676"><a href="/opinion/7344719/ashcroft-v-al-kidd/" aria-description="Citation for case: Ashcroft v. al-Kidd">179 L.Ed.2d 1149</a></span></extracted-citation> (2011), its absence will-as in retaliatory prosecution cases-generally provide weighty evidence that the officer's animus caused the arrest, whereas the presence of probable cause will suggest the opposite.</p>
<p id="p-36">To be sure, <em><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">Reichle</a></span></em> and <em>Lozman</em> also recognized that the two claims give rise to complex causal inquiries for somewhat different reasons. Unlike retaliatory prosecution cases, retaliatory arrest cases do not implicate the presumption of prosecutorial regularity or necessarily involve multiple government actors (although this case did). <em>Reichle</em> , <extracted-citation case-ids="12190092" index="73" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">566 U.S. at 668</a></span>-669</extracted-citation>, <extracted-citation case-ids="12190092" index="74" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">132 S.Ct. 2088</a></span></extracted-citation> ; <em>Lozman</em> , 585 U.S., at ----, 138 S.Ct., at 1953-1954. But regardless of the source of the causal complexity, the ultimate problem remains the same. For both claims, it is particularly difficult to determine whether the adverse government action was caused by the officer's malice or the plaintiff's potentially criminal conduct. See <em>id.</em> , at ----, 138 S.Ct., at 1953 (referring to "the complexity of proving (or disproving) causation" in retaliatory arrest cases). Because of the "close relationship" between the two claims, <em>Reichle</em> , <extracted-citation case-ids="12190092" index="75" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">566 U.S. at 667</a></span></extracted-citation>, <extracted-citation case-ids="12190092" index="76" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">132 S.Ct. 2088</a></span></extracted-citation>, their related causal challenge should lead to the same solution: The plaintiff pressing a retaliatory arrest claim must plead and prove the absence of probable cause for the arrest.</p>
<p id="p-37">Bartlett, in defending the decision below, argues that the "causation in retaliatory-arrest cases is not inherently complex" because the "factfinder simply must determine whether the officer intended to punish the plaintiff for the plaintiff's protected speech." Brief for Respondent 36-37; see also <em>post</em> , at 1737 - 1738 (SOTOMAYOR, J., dissenting). That approach fails to account for the fact that protected speech is often a legitimate consideration when deciding whether to make an arrest, and disregards the resulting causal complexity previously recognized by this Court. See <em>Reichle</em> , <extracted-citation case-ids="12190092" index="77" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">566 U.S. at 668</a></span></extracted-citation>, <extracted-citation case-ids="12190092" index="78" url="https://cite.case.law/us/566/658/"><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">132 S.Ct. 2088</a></span></extracted-citation> ; <em>Lozman</em> , 585 U.S., at ----, 138 S.Ct., at 1953.</p>
<p id="p-38">Bartlett's approach dismisses the need for any threshold showing, moving directly to consideration of the subjective intent of the officers. In the Fourth Amendment context, however, "we have almost uniformly rejected invitations to probe subjective intent." <em>al-Kidd</em> , <extracted-citation case-ids="5924024,12459540" index="79" url="https://cite.case.law/us/563/731/"><span class="citation" data-id="7262676"><a href="/opinion/7344719/ashcroft-v-al-kidd/" aria-description="Citation for case: Ashcroft v. al-Kidd">563 U.S. at 737</a></span></extracted-citation>, <extracted-citation case-ids="5924024,12459540" index="80" url="https://cite.case.law/us/563/731/"><span class="citation multiple-matches"><a href="/c/S.Ct./131/2074/">131 S.Ct. 2074</a></span></extracted-citation> ; see also <em>Kentucky v. King</em> , <extracted-citation case-ids="5911971,12458997" index="81" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">563 U.S. 452</a></span></extracted-citation>, 464, <extracted-citation case-ids="5911971,12458997" index="82" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">131 S.Ct. 1849</a></span></extracted-citation>, <extracted-citation case-ids="5911971,12458997" index="83" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">179 L.Ed.2d 865</a></span></extracted-citation> (2011) ("Legal tests based <a class="page-label" data-citation-index="1" data-label="1725" href="#p1725" id="p1725">*1725</a>on reasonableness are generally objective, and this Court has long taken the view that evenhanded law enforcement is best achieved by the application of objective standards of conduct, rather than standards that depend upon the subjective state of mind of the officer." (internal quotation marks omitted)). Police officers conduct approximately 29,000 arrests every day-a dangerous task that requires making quick decisions in "circumstances that are tense, uncertain, and rapidly evolving." <em>Graham v. Connor</em> , <extracted-citation case-ids="605535" index="84" url="https://cite.case.law/us/490/386/#p397"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U.S. 386</a></span></extracted-citation>, 397, <extracted-citation case-ids="605535" index="85" url="https://cite.case.law/us/490/386/#p397"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">109 S.Ct. 1865</a></span></extracted-citation>, <extracted-citation case-ids="605535" index="86" url="https://cite.case.law/us/490/386/#p397"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">104 L.Ed.2d 443</a></span></extracted-citation> (1989). To ensure that officers may go about their work without undue apprehension of being sued, we generally review their conduct under objective standards of reasonableness. See <em>Atwater v. Lago Vista</em> , <extracted-citation case-ids="9301256" index="87" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">532 U.S. 318</a></span></extracted-citation>, 351, and n. 22, <extracted-citation case-ids="9301256" index="88" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">121 S.Ct. 1536</a></span></extracted-citation>, <extracted-citation case-ids="9301256" index="89" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">149 L.Ed.2d 549</a></span></extracted-citation> (2001) ; <em>Harlow v. Fitzgerald</em> , <extracted-citation case-ids="6194865" index="90" url="https://cite.case.law/us/457/800/#p814"><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">457 U.S. 800</a></span></extracted-citation>, 814-819, <extracted-citation case-ids="6194865" index="91" url="https://cite.case.law/us/457/800/#p814"><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">102 S.Ct. 2727</a></span></extracted-citation>, <extracted-citation case-ids="6194865" index="92" url="https://cite.case.law/us/457/800/#p814"><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">73 L.Ed.2d 396</a></span></extracted-citation> (1982). Thus, when reviewing an arrest, we ask "whether the circumstances, viewed objectively, justify [the challenged] action," and if so, conclude "that action was reasonable <em>whatever</em> the subjective intent motivating the relevant officials." <em>al-Kidd</em> , <span class="citation" data-id="7262676"><a href="/opinion/7344719/ashcroft-v-al-kidd/#736" aria-description="Citation for case: Ashcroft v. al-Kidd">563 U.S. at 736</a></span>, <extracted-citation case-ids="5924024,12459540" index="93" url="https://cite.case.law/us/563/731/"><span class="citation multiple-matches"><a href="/c/S.Ct./131/2074/">131 S.Ct. 2074</a></span></extracted-citation> (internal quotation marks omitted). A particular officer's state of mind is simply "irrelevant," and it provides "no basis for invalidating an arrest." <em>Devenpeck v. Alford</em> , <extracted-citation case-ids="5916678" index="94" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">543 U.S. 146</a></span></extracted-citation>, 153, 155, <extracted-citation case-ids="5916678" index="95" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">125 S.Ct. 588</a></span></extracted-citation>, <extracted-citation case-ids="5916678" index="96" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">160 L.Ed.2d 537</a></span></extracted-citation> (2004).</p>
<p id="p-39">Bartlett's purely subjective approach would undermine that precedent by allowing even doubtful retaliatory arrest suits to proceed based solely on allegations about an arresting officer's mental state. See <em>Lozman</em> , 585 U.S., at ----, 138 S.Ct., at 1953. Because a state of mind is "easy to allege and hard to disprove," <em>Crawford-El</em> , <extracted-citation case-ids="11503978" index="97" url="https://cite.case.law/us/523/574/#p593"><span class="citation" data-id="9433625"><a href="/opinion/118203/crawford-el-v-britton/" aria-description="Citation for case: Crawford-El v. Britton">523 U.S. at 585</a></span></extracted-citation>, <extracted-citation case-ids="11503978" index="98" url="https://cite.case.law/us/523/574/#p593"><span class="citation" data-id="9433625"><a href="/opinion/118203/crawford-el-v-britton/" aria-description="Citation for case: Crawford-El v. Britton">118 S.Ct. 1584</a></span></extracted-citation>, a subjective inquiry would threaten to set off "broad-ranging discovery" in which "there often is no clear end to the relevant evidence," <em>Harlow</em> , <extracted-citation case-ids="6194865" index="99" url="https://cite.case.law/us/457/800/#p814"><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">457 U.S. at 817</a></span></extracted-citation>, <extracted-citation case-ids="6194865" index="100" url="https://cite.case.law/us/457/800/#p814"><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">102 S.Ct. 2727</a></span></extracted-citation>. As a result, policing certain events like an unruly protest would pose overwhelming litigation risks. Any inartful turn of phrase or perceived slight during a legitimate arrest could land an officer in years of litigation. Bartlett's standard would thus "dampen the ardor of all but the most resolute, or the most irresponsible, in the unflinching discharge of their duties." <em>Gregoire v. Biddle</em> , <extracted-citation case-ids="1166269" index="101" url="https://cite.case.law/f2d/177/579/#p581"><span class="citation" data-id="1507366"><a href="/opinion/1507366/gregoire-v-biddle/" aria-description="Citation for case: Gregoire v. Biddle">177 F. 2d 579</a></span></extracted-citation>, 581 (C.A.2 1949) (Learned Hand, C.J.). It would also compromise evenhanded application of the law by making the constitutionality of an arrest "vary from place to place and from time to time" depending on the personal motives of individual officers. <em>Devenpeck</em> , <extracted-citation case-ids="5916678" index="102" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">543 U.S. at 154</a></span></extracted-citation>, <extracted-citation case-ids="5916678" index="103" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">125 S.Ct. 588</a></span></extracted-citation>. Yet another "predictable consequence" of such a rule is that officers would simply minimize their communication during arrests to avoid having their words scrutinized for hints of improper motive-a result that would leave everyone worse off. <em><extracted-citation case-ids="5916678" index="104" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="5916678" index="104" url="https://cite.case.law/us/543/146/#p153"> at 155</extracted-citation>, <extracted-citation case-ids="5916678" index="105" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">125 S.Ct. 588</a></span></extracted-citation>.</p>
<p id="p-40">Adopting <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> 's no-probable-cause rule in this closely related context addresses those familiar concerns. Absent such a showing, a retaliatory arrest claim fails. But if the plaintiff establishes the absence of probable cause, "then the <em><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">Mt. Healthy</a></span></em> test governs: The plaintiff must show that the retaliation was a substantial or motivating factor behind the [arrest], and, if that showing is made, the defendant can prevail only by showing that the [arrest] would have been initiated without respect to retaliation." <em>Lozman</em> , 585 U.S., at ----, 138 S.Ct., at 1952-1953 (citing <em>Hartman</em> , <extracted-citation case-ids="3275855" index="106" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. at 265</a></span>-266</extracted-citation>, <extracted-citation case-ids="3275855" index="107" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation> ).<footnotemark>1</footnotemark></p>
<p id="p-41"><a class="page-label" data-citation-index="1" data-label="1726" href="#p1726" id="p1726">*1726</a>C</p>
<p id="p-42">Our conclusion is confirmed by the common law approach to similar tort claims. When defining the contours of a claim under § 1983, we look to "common-law principles that were well settled at the time of its enactment." <em>Kalina v. Fletcher</em> , <extracted-citation case-ids="11470940" index="108" url="https://cite.case.law/us/522/118/#p123"><span class="citation" data-id="9433547"><a href="/opinion/118156/kalina-v-fletcher/" aria-description="Citation for case: Kalina v. Fletcher">522 U.S. 118</a></span></extracted-citation>, 123, <extracted-citation case-ids="11470940" index="109" url="https://cite.case.law/us/522/118/#p123"><span class="citation" data-id="9433547"><a href="/opinion/118156/kalina-v-fletcher/" aria-description="Citation for case: Kalina v. Fletcher">118 S.Ct. 502</a></span></extracted-citation>, <extracted-citation case-ids="11470940" index="110" url="https://cite.case.law/us/522/118/#p123"><span class="citation" data-id="9433547"><a href="/opinion/118156/kalina-v-fletcher/" aria-description="Citation for case: Kalina v. Fletcher">139 L.Ed.2d 471</a></span></extracted-citation> (1997) ; <em>Manuelv.Joliet</em> , 580 U.S. ----, ----, <extracted-citation case-ids="12609962" index="111" url="https://cite.case.law/s-ct/137/911/#p1920"><span class="citation" data-id="9873459"><a href="/opinion/4376986/manuel-v-city-of-joliet/" aria-description="Citation for case: Manuel v. City of Joliet">137 S.Ct. 911</a></span></extracted-citation>, 1920-1921, <extracted-citation case-ids="12609962" index="112" url="https://cite.case.law/s-ct/137/911/#p1920"><span class="citation" data-id="9873459"><a href="/opinion/4376986/manuel-v-city-of-joliet/" aria-description="Citation for case: Manuel v. City of Joliet">197 L.Ed.2d 312</a></span></extracted-citation> (2017) (common law principles "guide" the definition of claims under § 1983 ).</p>
<p id="p-43">As the parties acknowledge, when § 1983 was enacted in 1871, there was no common law tort for retaliatory arrest based on protected speech. See Brief for Petitioners 43; Brief for Respondent 20. We therefore turn to the common law torts that provide the "closest analogy" to retaliatory arrest claims. <em>Heck v. Humphrey</em> , <extracted-citation case-ids="39868" index="113" url="https://cite.case.law/us/512/477/#p484"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U.S. 477</a></span></extracted-citation>, 484, <extracted-citation case-ids="39868" index="114" url="https://cite.case.law/us/512/477/#p484"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>, <extracted-citation case-ids="39868" index="115" url="https://cite.case.law/us/512/477/#p484"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">129 L.Ed.2d 383</a></span></extracted-citation> (1994). The parties dispute whether the better analog is false imprisonment or malicious prosecution. At common law, false imprisonment arose from a "detention without legal process," whereas malicious prosecution was marked "by <em>wrongful institution</em> of legal process." <em>Wallace v. Kato</em> , <extracted-citation case-ids="3553763" index="116" url="https://cite.case.law/us/549/384/#p389"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S. 384</a></span></extracted-citation>, 389-390, <extracted-citation case-ids="3553763" index="117" url="https://cite.case.law/us/549/384/#p389"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>, <extracted-citation case-ids="3553763" index="118" url="https://cite.case.law/us/549/384/#p389"><span class="citation no-link">166 L.Ed.2d 973</span></extracted-citation> (2007).<footnotemark>2</footnotemark> Here, both claims suggest the same result: The presence of probable cause should generally defeat a First Amendment retaliatory arrest claim. See generally <em>Lozman</em> , 585 U.S., at ---- - ----, 138 S.Ct., at 1950-1951 (THOMAS, J., dissenting).</p>
<p id="p-44">Malicious prosecution required the plaintiff to show that the criminal charge against him "was unfounded, and that it was made without reasonable or probable cause, and that the defendant in making or instigating it was actuated by malice." <em>Wheeler v. Nesbitt</em> , <extracted-citation case-ids="3463673" index="119" url="https://cite.case.law/us/65/544/"><span class="citation" data-id="87431"><a href="/opinion/87431/wheeler-v-nesbitt/" aria-description="Citation for case: Wheeler v. Nesbitt">65 U.S. 544</a></span></extracted-citation>, <extracted-citation case-ids="3463673" index="120" url="https://cite.case.law/us/65/544/"><span class="citation" data-id="87431"><a href="/opinion/87431/wheeler-v-nesbitt/" aria-description="Citation for case: Wheeler v. Nesbitt">24 How. 544</a></span></extracted-citation>, 549-550, <extracted-citation case-ids="3463673" index="121" url="https://cite.case.law/us/65/544/"><span class="citation" data-id="87431"><a href="/opinion/87431/wheeler-v-nesbitt/" aria-description="Citation for case: Wheeler v. Nesbitt">16 L.Ed. 765</a></span></extracted-citation> (1861) ; see also Restatement of Torts § 653 (1938). It has long been "settled law" that malicious prosecution requires proving "the want of probable cause," and Bartlett does not argue otherwise. <em>Brown v. Selfridge</em> , <extracted-citation case-ids="3668822" index="122" url="https://cite.case.law/us/224/189/#p191"><span class="citation" data-id="97600"><a href="/opinion/97600/brown-v-selfridge/" aria-description="Citation for case: Brown v. Selfridge">224 U.S. 189</a></span></extracted-citation>, 191, <extracted-citation case-ids="3668822" index="123" url="https://cite.case.law/us/224/189/#p191"><span class="citation" data-id="97600"><a href="/opinion/97600/brown-v-selfridge/" aria-description="Citation for case: Brown v. Selfridge">32 S.Ct. 444</a></span></extracted-citation>, <extracted-citation case-ids="3668822" index="124" url="https://cite.case.law/us/224/189/#p191"><span class="citation" data-id="97600"><a href="/opinion/97600/brown-v-selfridge/" aria-description="Citation for case: Brown v. Selfridge">56 L.Ed. 727</a></span></extracted-citation> (1912) ; see also <em>Wheeler</em> , <extracted-citation case-ids="3463673" index="125" url="https://cite.case.law/us/65/544/"><span class="citation" data-id="87431"><a href="/opinion/87431/wheeler-v-nesbitt/#550" aria-description="Citation for case: Wheeler v. Nesbitt">24 How. at 550</a></span></extracted-citation> (noting that "[w]ant of reasonable and probable cause" is an "element in the action for a malicious criminal prosecution").</p>
<p id="p-45">For claims of false imprisonment, the presence of probable cause was generally a complete defense for peace officers. See T. Cooley, Law of Torts 175 (1880); 1 F. Hilliard, The Law of Torts or Private Wrongs 207-208, and n. (a) (1859). In such cases, arresting officers were protected from liability if the arrest was "privileged." At common law, peace officers were privileged to make warrantless arrests based on probable cause of the commission of a felony or certain misdemeanors. See Restatement of Torts §§ 118, 119, 121 (1934) ; see also Cooley, Law of Torts, at 175-176 (stating that peace officers who make arrests <a class="page-label" data-citation-index="1" data-label="1727" href="#p1727" id="p1727">*1727</a>based on probable cause "will be excused, even though it appear afterwards that in fact no felony had been committed"); see generally <em>Atwater</em> , <extracted-citation case-ids="9301256" index="126" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">532 U.S. at 340</a></span>-345</extracted-citation>, <extracted-citation case-ids="9301256" index="127" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">121 S.Ct. 1536</a></span></extracted-citation> (reviewing the history of warrantless arrests for misdemeanors). Although the exact scope of the privilege varied somewhat depending on the jurisdiction, the consistent rule was that officers were not liable for arrests they were privileged to make based on probable cause.</p>
<p id="p-46">D</p>
<p id="p-47">Although probable cause should generally defeat a retaliatory arrest claim, a narrow qualification is warranted for circumstances where officers have probable cause to make arrests, but typically exercise their discretion not to do so. In such cases, an unyielding requirement to show the absence of probable cause could pose "a risk that some police officers may exploit the arrest power as a means of suppressing speech." <em>Lozman</em> , 585 U.S., at ----, 138 S.Ct., at 1953-1954.</p>
<p id="p-48">When § 1983 was adopted, officers were generally privileged to make warrantless arrests for misdemeanors only in limited circumstances. See Restatement of Torts § 121, Comments <em>e</em> , <em>h</em> , at 262-263. Today, however, "statutes in all 50 States and the District of Columbia permit warrantless misdemeanor arrests" in a much wider range of situations-often whenever officers have probable cause for "even a very minor criminal offense." <em>Atwater</em> , <extracted-citation case-ids="9301256" index="128" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/#344" aria-description="Citation for case: Atwater v. City of Lago Vista">532 U.S. at 344-345</a></span>, 354</extracted-citation>, <extracted-citation case-ids="9301256" index="129" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">121 S.Ct. 1536</a></span></extracted-citation> ; see <em><extracted-citation case-ids="9301256" index="130" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">id.,</a></span></extracted-citation></em><extracted-citation case-ids="9301256" index="130" url="https://cite.case.law/us/532/318/#p351"> at 355-360</extracted-citation>, <extracted-citation case-ids="9301256" index="131" url="https://cite.case.law/us/532/318/#p351"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">121 S.Ct. 1536</a></span></extracted-citation> (listing state statutes).</p>
<p id="p-49">For example, at many intersections, jaywalking is endemic but rarely results in arrest. If an individual who has been vocally complaining about police conduct is arrested for jaywalking at such an intersection, it would seem insufficiently protective of First Amendment rights to dismiss the individual's retaliatory arrest claim on the ground that there was undoubted probable cause for the arrest. In such a case, because probable cause does little to prove or disprove the causal connection between animus and injury, applying <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> 's rule would come at the expense of <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> 's logic.</p>
<p id="p-50">For those reasons, we conclude that the no-probable-cause requirement should not apply when a plaintiff presents objective evidence that he was arrested when otherwise similarly situated individuals not engaged in the same sort of protected speech had not been. Cf. <em>United States v. Armstrong</em> , <extracted-citation case-ids="11745202" index="132" url="https://cite.case.law/us/517/456/#p465"><span class="citation" data-id="9433285"><a href="/opinion/118022/united-states-v-armstrong/" aria-description="Citation for case: United States v. Armstrong">517 U.S. 456</a></span></extracted-citation>, 465, <extracted-citation case-ids="11745202" index="133" url="https://cite.case.law/us/517/456/#p465"><span class="citation" data-id="9433285"><a href="/opinion/118022/united-states-v-armstrong/" aria-description="Citation for case: United States v. Armstrong">116 S.Ct. 1480</a></span></extracted-citation>, <extracted-citation case-ids="11745202" index="134" url="https://cite.case.law/us/517/456/#p465"><span class="citation" data-id="9433285"><a href="/opinion/118022/united-states-v-armstrong/" aria-description="Citation for case: United States v. Armstrong">134 L.Ed.2d 687</a></span></extracted-citation> (1996). That showing addresses <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> 's causal concern by helping to establish that "non-retaliatory grounds [we]re in fact insufficient to provoke the adverse consequences." <extracted-citation case-ids="3275855" index="135" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. at 256</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="136" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>. And like a probable cause analysis, it provides an objective inquiry that avoids the significant problems that would arise from reviewing police conduct under a purely subjective standard. Because this inquiry is objective, the statements and motivations of the particular arresting officer are "irrelevant" at this stage. <em>Devenpeck</em> , <extracted-citation case-ids="5916678" index="137" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">543 U.S. at 153</a></span></extracted-citation>, <extracted-citation case-ids="5916678" index="138" url="https://cite.case.law/us/543/146/#p153"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">125 S.Ct. 588</a></span></extracted-citation>. After making the required showing, the plaintiff's claim may proceed in the same manner as claims where the plaintiff has met the threshold showing of the absence of probable cause. See <em>Lozman</em> , 585 U.S., at ----, 138 S.Ct., at 1952-1953.</p>
<p id="p-51">* * *</p>
<p id="p-52">In light of the foregoing, Bartlett's retaliation claim cannot survive summary judgment. As an initial matter, the record contains insufficient evidence of retaliation on the part of Trooper Weight. The <em>only</em> evidence of retaliatory animus <a class="page-label" data-citation-index="1" data-label="1728" href="#p1728" id="p1728">*1728</a>identified by the Ninth Circuit was Bartlett's affidavit stating that Sergeant Nieves said "bet you wish you would have talked to me now." <extracted-citation index="139" url="https://cite.case.law/citations/?q=712%20Fed.%20Appx.%20613"><span class="citation" data-id="4213549"><a href="/opinion/4436296/russell-bartlett-v-luis-nieves/" aria-description="Citation for case: Russell Bartlett v. Luis Nieves">712 Fed. Appx. at 616</a></span></extracted-citation>. But that allegation about <em>Nieves</em> says nothing about what motivated <em>Weight</em> , who had no knowledge of Bartlett's prior run-in with Nieves. Cf. <em>Lozman</em> , 585 U.S., at ----, 138 S.Ct., at 1953-1954 (plaintiff "likely could not have maintained a retaliation claim against the arresting officer" when there was "no showing that the officer had any knowledge of [the plaintiff's] prior speech").</p>
<p id="p-53">In any event, Bartlett's claim against both officers cannot succeed because they had probable cause to arrest him. As the Court of Appeals explained:</p>
<blockquote id="p-54">"When Sergeant Nieves initiated Bartlett's arrest, he knew that Bartlett had been drinking, and he observed Bartlett speaking in a loud voice and standing close to Trooper Weight. He also saw Trooper Weight push Bartlett back.... [T]he test is whether the information the officer had at the time of making the arrest gave rise to probable cause. We agree with the district court that it did; a reasonable officer in Sergeant Nieves's position could have concluded that Bartlett stood close to Trooper Weight and spoke loudly in order to challenge him, provoking Trooper Weight to push him back." <extracted-citation index="140" url="https://cite.case.law/citations/?q=712%20Fed.%20Appx.%20613"><span class="citation" data-id="4213549"><a href="/opinion/4436296/russell-bartlett-v-luis-nieves/#615" aria-description="Citation for case: Russell Bartlett v. Luis Nieves">712 Fed. Appx. at 615</a></span></extracted-citation> (citations and internal quotation marks omitted).</blockquote>
<p id="p-55">Because there was probable cause to arrest Bartlett, his retaliatory arrest claim fails as a matter of law. Accordingly, the judgment of the United States Court of Appeals for the Ninth Circuit is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="p-56">It is so ordered.</p>
<p id="p-57">Justice THOMAS, concurring in part and concurring in the judgment.</p>
<p id="p-58">When <extracted-citation index="141" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation> was enacted, "the common law recognized probable cause as an important element for ensuring that arrest-based torts did not unduly interfere with the objectives of law enforcement." <em>Lozman v.Riviera Beach</em> , 585 U.S. ----, ----, <extracted-citation case-ids="12612344" index="142" url="https://cite.case.law/s-ct/138/1945/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct. 1945</a></span></extracted-citation>, 1958, <extracted-citation case-ids="12612344" index="143" url="https://cite.case.law/s-ct/138/1945/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">201 L.Ed.2d 342</a></span></extracted-citation> (2018) (THOMAS, J., dissenting). Applying that principle resolves this case: "[P]laintiffs bringing a First Amendment retaliatory-arrest claim under § 1983 should have to plead and prove a lack of probable cause." <em><extracted-citation case-ids="12612344" index="144" url="https://cite.case.law/s-ct/138/1945/">Ibid.</extracted-citation></em> The Court acknowledges as much, <em>ante,</em> at 1726 - 1727, and I join the portions of the Court's opinion adopting that rule.<footnotemark>1</footnotemark> I do not join Part II-D, however, because I do not agree that "a narrow qualification is warranted for circumstances where officers have probable cause to make arrests, but typically exercise their discretion not to do so." <em>Ante,</em> at 1727. That qualification has no basis in either the common law or our First Amendment precedents.</p>
<p id="p-59">As the Court explains, "[w]hen defining the contours of a claim under § 1983, we look to 'common-law principles that were well settled at the time of its enactment.' " <em>Ante,</em> at 1726. Because no common-law tort for retaliatory arrest in violation of the freedom of speech existed when § 1983 was enacted, we "look to the common-law torts that 'provid[e] the closest analogy' to this claim." <em>Lozman</em> , 585 U.S., at ----, 138 S.Ct., at 1957 (opinion of THOMAS, J.). Here, those torts are false imprisonment, <a class="page-label" data-citation-index="1" data-label="1729" href="#p1729" id="p1729">*1729</a>malicious arrest, and malicious prosecution. <em>Ibid.</em></p>
<p id="p-60">The existence of probable cause generally excused an officer from liability for these three torts, without regard to the treatment of similarly situated individuals. For instance, a constable who made an arrest "on reasonable grounds of belief" that a felony had been committed was "excused" from liability for false imprisonment. T. Cooley, Law of Torts 175 (1879) (Cooley); <em>Lozman</em> , <em>supra,</em> at 1721 - 1722, 138 S.Ct., at 1957-1958 (opinion of THOMAS, J.). And the absence of probable cause was central to both malicious arrest and malicious prosecution. Cooley 180-181; <em>Lozman</em> , <em>supra,</em> at 1722 - 1723, 138 S.Ct., at 1957-1958 (opinion of THOMAS, J.). As the Court puts it, "the consistent rule was that officers were not liable for arrests they were privileged to make based on probable cause." <em>Ante,</em> at 1727.</p>
<p id="p-61">Rather than adhere to this rule, the majority carves out an exception to the no-probable-cause requirement for plaintiffs who "presen[t] objective evidence" that they were "arrested when otherwise similarly situated individuals not engaged in the same sort of protected speech had not been." <em>Ante,</em> at 1727. The common law provides no support for this exception. Indeed, the majority cites not a single common-law case that supports imposing liability based on an officer's treatment of similarly situated individuals. The majority instead suggests that its exception responds to the fact that States today " 'permit warrantless misdemeanor arrests' " for many " 'minor criminal offense[s],' " whereas "[w]hen § 1983 was adopted, officers were generally privileged to make warrantless arrests for misdemeanors only in limited circumstances." <em>Ibid</em> . But discomfort with the number of warrantless arrests that are privileged today is an issue for state legislatures, not a license for this Court to fashion an exception to a previously "consistent rule." <em>Ante,</em> at 1726 - 1727.</p>
<p id="p-62">The majority's exception is also untethered from our First Amendment precedents. In <em>Hartman v. Moore</em> , <extracted-citation case-ids="3275855" index="145" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. 250</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="146" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="147" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">164 L.Ed.2d 441</a></span></extracted-citation> (2006), we expressly declined to create <em>any</em> exceptions to the rule that a plaintiff alleging retaliatory prosecution in violation of the First Amendment must plead and prove the absence of probable cause. See <em><extracted-citation case-ids="3275855" index="148" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">id.</a></span></extracted-citation></em> , at 264-266, and n. 10, <extracted-citation case-ids="3275855" index="149" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>. The majority today imports its "qualification" from our jurisprudence on selective-prosecution claims. <em>Ante</em> , at 1727 - 1728, 1729 - 1730 (citing <em>United States v. Armstrong</em> , <extracted-citation case-ids="11745202" index="150" url="https://cite.case.law/us/517/456/#p465"><span class="citation" data-id="9433285"><a href="/opinion/118022/united-states-v-armstrong/" aria-description="Citation for case: United States v. Armstrong">517 U.S. 456</a></span></extracted-citation>, 465, <extracted-citation case-ids="11745202" index="151" url="https://cite.case.law/us/517/456/#p465"><span class="citation" data-id="9433285"><a href="/opinion/118022/united-states-v-armstrong/" aria-description="Citation for case: United States v. Armstrong">116 S.Ct. 1480</a></span></extracted-citation>, <extracted-citation case-ids="11745202" index="152" url="https://cite.case.law/us/517/456/#p465"><span class="citation" data-id="9433285"><a href="/opinion/118022/united-states-v-armstrong/" aria-description="Citation for case: United States v. Armstrong">134 L.Ed.2d 687</a></span></extracted-citation> (1996) ). But "[t]he requirements for a selective-prosecution claim draw on 'ordinary equal protection standards,' " not the First Amendment. <em><extracted-citation case-ids="11745202" index="153" url="https://cite.case.law/us/517/456/#p465"><span class="citation" data-id="9433285"><a href="/opinion/118022/united-states-v-armstrong/" aria-description="Citation for case: United States v. Armstrong">Id.</a></span></extracted-citation></em> , at 465, <extracted-citation case-ids="11745202" index="154" url="https://cite.case.law/us/517/456/#p465"><span class="citation" data-id="9433285"><a href="/opinion/118022/united-states-v-armstrong/" aria-description="Citation for case: United States v. Armstrong">116 S.Ct. 1480</a></span></extracted-citation>. That jurisprudence therefore is not relevant here. Cf. <em>Whren v. United States</em> , <extracted-citation case-ids="11746960" index="155" url="https://cite.case.law/us/517/806/#p813"><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U.S. 806</a></span></extracted-citation>, 813, <extracted-citation case-ids="11746960" index="156" url="https://cite.case.law/us/517/806/#p813"><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S.Ct. 1769</a></span></extracted-citation>, <extracted-citation case-ids="11746960" index="157" url="https://cite.case.law/us/517/806/#p813"><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L.Ed.2d 89</a></span></extracted-citation> (1996) ("[T]he constitutional basis for objecting to intentionally discriminatory application of laws is the Equal Protection Clause ... ").</p>
<p id="p-63">With no guidance from the common law or relevant precedents, the majority crafts its exception as a matter of policy. But this "narrow" qualification threatens to derail our retaliation jurisprudence in several ways. For one, although the majority's stated concern is with " 'warrantless misdemeanor arrests' " for " 'very minor' " offenses like "jaywalking," <em>ante,</em> at 1727 - 1728, its exception apparently applies to <em>all</em> offenses, including serious felonies. This overbroad exception thus is likely to encourage protracted litigation about which individuals are "similarly situated," <em><extracted-citation case-ids="11746960" index="158" url="https://cite.case.law/us/517/806/#p813"><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">ibid.</a></span></extracted-citation></em> , while doing little to vindicate First Amendment rights. Moreover, the majority's rule risks chilling law enforcement officers from making arrests for fear of <a class="page-label" data-citation-index="1" data-label="1730" href="#p1730" id="p1730">*1730</a>liability, thus flouting the reasoning behind the emphasis on probable cause in arrest-based torts at common law. <em>Lozman</em> , <em>supra,</em> at 1721 - 1722, 138 S.Ct., at 1957-1958 (opinion of THOMAS, J.). In short, the majority's exception lacks the support of history, precedent, and sound policy.</p>
<p id="p-64">* * *</p>
<p id="p-65">The requirement that plaintiffs bringing First Amendment retaliatory-arrest claims plead and prove the absence of probable cause is supported by the common law and our First Amendment precedents. The majority's new exception has no basis in either. Accordingly, I join all but Part II-D of the majority opinion.</p>
<footnote label="1">
<p id="p-130">Justice SOTOMAYOR would have us extend <em><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">Mt. Healthy</a></span></em> and rely on that "tried and true" approach as the exclusive standard in the retaliatory arrest context. See <em>post</em> , at 1735 - 1737, 1742 (dissenting opinion). But not even respondent Bartlett argues for such a rule. And since our decisions in <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> and <em><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">Reichle</a></span></em> , no court of appeals has applied that approach in retaliatory arrest cases of this sort. Justice SOTOMAYOR criticizes the Court for spending "[m]uch of its opinion ... analogizing to <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> ," <em>post,</em> at 1736 - 1737, but of course <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> is our precedent most directly on point. To the extent retaliatory arrest cases raise concerns distinct from that precedent, we have departed from <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> to afford greater First Amendment protection. See <em>infra</em> , at 1741 - 1742.</p>
</footnote>
<footnote label="2">
<p id="p-131">For our purposes, we need not distinguish between the torts of false imprisonment and false arrest, which are "virtually synonymous." 35 C.J. S., False Imprisonment § 2, p. 522 (2009) ; see also <em>Wallace</em> , <extracted-citation case-ids="3553763" index="159" url="https://cite.case.law/us/549/384/#p389"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S. at 388</a></span>-389</extracted-citation>, <extracted-citation case-ids="3553763" index="160" url="https://cite.case.law/us/549/384/#p389"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>.</p>
</footnote>
<footnote label="1">
<p id="p-133">The majority implies that the Ninth Circuit does not apply <em><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">Mt. Healthy</a></span></em> . <em>Ante,</em> at 1725, n. 1 ("since ... <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> and <em><span class="citation" data-id="9500600"><a href="/opinion/801500/reichle-v-howards/" aria-description="Citation for case: Reichle v. Howards">Reichle</a></span></em> , no court of appeals has applied [the <em><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">Mt. Healthy</a></span></em> ] approach"). That is not readily apparent. Because <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> 's no-probable-cause requirement does not apply to retaliatory police action in the Ninth Circuit, such claims are handled as " 'ordinary' retaliation claim[s]," <em>Skoog v. County of Clackamas</em> , <extracted-citation case-ids="3757279" index="161" url="https://cite.case.law/f3d/469/1221/#p1234"><span class="citation" data-id="3039576"><a href="/opinion/3039576/skoog-v-county-of-clackamas/" aria-description="Citation for case: Skoog v. County of Clackamas">469 F. 3d 1221</a></span></extracted-citation>, 1234 (2006), which in the Ninth Circuit (as elsewhere) means that retaliatory motive must be the "but-for cause of the defendant's action," <em><extracted-citation case-ids="3757279" index="162" url="https://cite.case.law/f3d/469/1221/#p1234"><span class="citation" data-id="3039576"><a href="/opinion/3039576/skoog-v-county-of-clackamas/" aria-description="Citation for case: Skoog v. County of Clackamas">id.,</a></span></extracted-citation></em><extracted-citation case-ids="3757279" index="162" url="https://cite.case.law/f3d/469/1221/#p1234"> at 1232</extracted-citation>. That but-for causation requirement for retaliation claims derives from <em><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">Mt. Healthy</a></span></em> . See <em>Hartman v. Moore</em> , <extracted-citation case-ids="3275855" index="163" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. 250</a></span></extracted-citation>, 260, <extracted-citation case-ids="3275855" index="164" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="165" url="https://cite.case.law/us/547/250/#p256"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">164 L.Ed.2d 441</a></span></extracted-citation> (2006) ; <em>Crawford-El v. Britton</em> , <extracted-citation case-ids="11503978" index="166" url="https://cite.case.law/us/523/574/#p593"><span class="citation" data-id="9433625"><a href="/opinion/118203/crawford-el-v-britton/" aria-description="Citation for case: Crawford-El v. Britton">523 U.S. 574</a></span></extracted-citation>, 593, <extracted-citation case-ids="11503978" index="167" url="https://cite.case.law/us/523/574/#p593"><span class="citation" data-id="9433625"><a href="/opinion/118203/crawford-el-v-britton/" aria-description="Citation for case: Crawford-El v. Britton">118 S.Ct. 1584</a></span></extracted-citation>, <extracted-citation case-ids="11503978" index="168" url="https://cite.case.law/us/523/574/#p593"><span class="citation" data-id="9433625"><a href="/opinion/118203/crawford-el-v-britton/" aria-description="Citation for case: Crawford-El v. Britton">140 L.Ed.2d 759</a></span></extracted-citation> (1998) ; see also <em>Lacey v. Maricopa County</em> , <extracted-citation case-ids="3518590" index="169" url="https://cite.case.law/f3d/693/896/#p916"><span class="citation" data-id="9501261"><a href="/opinion/807646/michael-lacey-v-joseph-arpaio/" aria-description="Citation for case: Michael Lacey v. Joseph Arpaio">693 F. 3d 896</a></span></extracted-citation>, 916-917 (C.A.9 2012) (en banc) (retaliatory arrest plaintiff must show that deterrence of speech "was a substantial or motivating factor" and also "ultimately" be able to show " 'but-for causation' " (quoting <em><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">Hartman</a></span></em> 's discussion of <em><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">Mt. Healthy</a></span></em> )).</p>
<p id="p-134">In any event, the majority's criticism is a red herring. There is nothing novel about applying <em><span class="citation" data-id="109574"><a href="/opinion/109574/mt-healthy-city-school-district-board-of-education-v-doyle/" aria-description="Citation for case: Mt. Healthy City School District Board of Education v. Doyle">Mt. Healthy</a></span></em> in the retaliatory arrest context. <em>E.g.,</em> <em>Lozmanv.Riviera Beach</em> , 585 U.S. ----, ---- - ----, <extracted-citation case-ids="12612344" index="170" url="https://cite.case.law/s-ct/138/1945/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">138 S.Ct. 1945</a></span></extracted-citation>, 1954-1955, <extracted-citation case-ids="12612344" index="171" url="https://cite.case.law/s-ct/138/1945/"><span class="citation" data-id="4285390"><a href="/opinion/4508137/lozman-v-riviera-beach/" aria-description="Citation for case: Lozman v. Riviera Beach">201 L.Ed.2d 342</a></span></extracted-citation> (2018). The same cannot be said of the test concocted by the majority.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/North Carolina v. Butler.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "North Carolina v. Butler"
type: case
citation: "441 U.S. 369 (1979)"
parallel_cite: "99 S. Ct. 1755; 60 L. Ed. 2d 286"
neutral_cite: 1979 U.S. LEXIS 91
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-04-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1979-04-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: North Carolina v. Butler
  varies_by_point: false
  scope_note: "Implied-waiver rule; reaffirmed in Berghuis v. Thompkins; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110065/north-carolina-v-butler/"
  cluster_id: 110065
  opinion_id: 9427547
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[Berghuis v. Thompkins]]", "[[Moran v. Burbine]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "waiver", "implied-waiver"]
holding: "An express written or oral waiver is not required; a valid Miranda waiver may be inferred from the suspect's words and conduct — but…"
lake:
  record_id: North Carolina v. Butler
  status: verified
  projected_at: 2026-07-06
---

# North Carolina v. Butler

*441 U.S. 369 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After his arrest, Butler was advised of his *[[Miranda v. Arizona|Miranda]]* rights and given a waiver form. He said he understood his rights but refused to sign the waiver, stating that he would talk but would not sign any form. He then made inculpatory statements without expressly waiving and without requesting counsel.

## Issue
Whether an explicit (signed or spoken) statement of waiver is necessary for a valid *[[Miranda v. Arizona|Miranda]]* waiver, or whether waiver may be inferred from the suspect's words and conduct.

## Rule
An express waiver is not required. "An express written or oral statement of waiver of the right to remain silent or of the right to counsel is usually strong proof of the validity of that waiver, but is not inevitably either necessary or sufficient to establish waiver." — 441 U.S. at 373. ^pin-373

"The courts must presume that a defendant did not waive his rights; the prosecution's burden is great; but in at least some cases waiver can be clearly inferred from the actions and words of the person interrogated." — *Id.* ^pin-373b

## Application
Butler's refusal to sign the waiver form did not, by itself, defeat waiver. His statement that he would talk — made after he acknowledged understanding his rights and without invoking counsel — could support a finding that he waived his rights through his words and conduct. The Court rejected the North Carolina Supreme Court's [[Common Legal Terms#per-se|per se]] rule requiring an explicit waiver and [[Reading and Citing Cases#on-remand|remanded]] for a determination under the proper standard.

## Conclusion
The state court's [[Common Legal Terms#per-se|per se]] rule requiring an express waiver was rejected; reversed and [[Reading and Citing Cases#on-remand|remanded]] to assess waiver from the totality of Butler's words and conduct.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Butler*'s implied-waiver principle was reaffirmed and extended in [[Berghuis v. Thompkins]], and operates within the voluntary/knowing-and-intelligent framework of [[Moran v. Burbine]].

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *North Carolina v. Butler*, 441 U.S. 369 (1979) — https://www.courtlistener.com/opinion/110065/north-carolina-v-butler/ — pinpoint: 373.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "20da48e440683e20", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "North Carolina v. Butler"}, "payload": {"all": [{"cite": "441 U.S. 369", "page": "369", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "441"}, {"cite": "99 S. Ct. 1755", "page": "1755", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "99"}, {"cite": "60 L. Ed. 2d 286", "page": "286", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "60"}, {"cite": "1979 U.S. LEXIS 91", "page": "91", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1979"}], "display": "441 U.S. 369", "official": {"cite": "441 U.S. 369", "page": "369", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "441"}, "official_selection_present": true, "record_id": "North Carolina v. Butler"}}
{"assertion_id": "34bf784032895ee3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-373b", "record_id": "North Carolina v. Butler"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-373b", "pinpoint_status": "slip-only", "quote": "The courts must presume that a defendant did not waive his rights; the prosecution's burden is great; but in at least some cases waiver can be clearly inferred from the actions and words of the person interrogated.", "quote_fidelity": "mismatch", "record_id": "North Carolina v. Butler", "star_marker": null}}
{"assertion_id": "91e1454196b37dce", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-373", "record_id": "North Carolina v. Butler"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-373", "pinpoint_status": "slip-only", "quote": "--- # North Carolina v. Butler *441 U.S. 369 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After his arrest, Butler was advised of his *Miranda* rights and given a waiver form. He said he understood his rights but refused to sign the waiver, stating that he would talk but would not sign any form. He then made inculpatory statements without expressly waiving and without requesting counsel. ## Issue Whether an explicit (signed or spoken) statement of waiver is necessary for a valid *Miranda* waiver, or whether waiver may be inferred from the suspect's words and conduct. ## Rule An express waiver is not required.", "quote_fidelity": "mismatch", "record_id": "North Carolina v. Butler", "star_marker": null}}
{"assertion_id": "fc45231dffb5b7ed", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "North Carolina v. Butler"}, "payload": {"as_of_content": "1979-04-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "North Carolina v. Butler", "scope_note": "Implied-waiver rule; reaffirmed in Berghuis v. Thompkins; good law.", "varies_by_point": false}}
```

### lake record — North Carolina v. Butler

```json
{
  "schema_version": "s2.v1",
  "record_id": "North Carolina v. Butler",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "North Carolina v. Butler",
    "case_name_short": "",
    "case_name_full": "North Carolina v. Butler",
    "input_case_name": "North Carolina v. Butler",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-04-24",
    "year": 1979,
    "docket": null,
    "cluster_id": 110065,
    "lead_opinion_id": 9427547,
    "sibling_ids": [
      110065,
      9427547,
      9427548,
      9427549
    ],
    "absolute_url": "/opinion/110065/north-carolina-v-butler/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9021516,
        "score": 20,
        "case_name": "North Carolina v. Butler"
      },
      {
        "cluster_id": 9020876,
        "score": 20,
        "case_name": "North Carolina v. Butler"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "441 U.S. 369",
      "volume": "441",
      "reporter": "U.S.",
      "page": "369",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 1755",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1755",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 L. Ed. 2d 286",
        "volume": "60",
        "reporter": "L. Ed. 2d",
        "page": "286",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 91",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "91",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "441 U.S. 369",
        "volume": "441",
        "reporter": "U.S.",
        "page": "369",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 1755",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1755",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 L. Ed. 2d 286",
        "volume": "60",
        "reporter": "L. Ed. 2d",
        "page": "286",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 91",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "91",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "441 U.S. 369",
    "official_selection": {
      "court_class": "scotus",
      "selected": "441 U.S. 369",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-373",
      "page": null,
      "quote": "--- # North Carolina v. Butler *441 U.S. 369 (1979)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After his arrest, Butler was advised of his *Miranda* rights and given a waiver form. He said he understood his rights but refused to sign the waiver, stating that he would talk but would not sign any form. He then made inculpatory statements without expressly waiving and without requesting counsel. ## Issue Whether an explicit (signed or spoken) statement of waiver is necessary for a valid *Miranda* waiver, or whether waiver may be inferred from the suspect's words and conduct. ## Rule An express waiver is not required.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-373b",
      "page": null,
      "quote": "The courts must presume that a defendant did not waive his rights; the prosecution's burden is great; but in at least some cases waiver can be clearly inferred from the actions and words of the person interrogated.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1979-04-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "North Carolina v. Butler",
    "varies_by_point": false,
    "scope_note": "Implied-waiver rule; reaffirmed in Berghuis v. Thompkins; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Dias v. Boone",
          "cluster_id": 10680524,
          "cite": [
            "912 S.E.2d 547",
            "320 Ga. 785"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Delossantos",
          "cluster_id": 9405989,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "1A Auto, Inc. v. Director of the Office of Campaign and Political Finance",
          "cluster_id": 4533242,
          "cite": [
            "105 N.E.3d 1175",
            "480 Mass. 423"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Saldierna",
          "cluster_id": 4527726,
          "cite": [
            "817 S.E.2d 174",
            "371 N.C. 407"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jones v. Stephens",
          "cluster_id": 7317930,
          "cite": [
            "157 F. Supp. 3d 623",
            "2016 U.S. Dist. LEXIS 3888",
            "2016 WL 147919"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 2830722,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 2828358,
          "cite": [
            "413 S.C. 458",
            "776 S.E.2d 367",
            "2015 S.C. LEXIS 302"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane1_negative"
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
        "journal_ref": "North Carolina v. Butler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Garcia, Irving Magana",
          "cluster_id": 2949812,
          "cite": [
            "429 S.W.3d 604",
            "2014 WL 1375457",
            "2014 Tex. Crim. App. LEXIS 540"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Edwards v. Arizona",
          "cluster_id": 110475,
          "cite": [
            "68 L. Ed. 2d 378",
            "101 S. Ct. 1880",
            "451 U.S. 477",
            "1981 U.S. LEXIS 96"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
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
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
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
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
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
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fare v. Michael C.",
          "cluster_id": 110117,
          "cite": [
            "61 L. Ed. 2d 197",
            "99 S. Ct. 2560",
            "442 U.S. 707",
            "1979 U.S. LEXIS 133"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Bradshaw",
          "cluster_id": 110987,
          "cite": [
            "77 L. Ed. 2d 405",
            "103 S. Ct. 2830",
            "462 U.S. 1039",
            "1983 U.S. LEXIS 82",
            "51 U.S.L.W. 4940"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Clover Leaf Creamery Co.",
          "cluster_id": 110380,
          "cite": [
            "66 L. Ed. 2d 659",
            "101 S. Ct. 715",
            "449 U.S. 456",
            "1981 U.S. LEXIS 14"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Spring",
          "cluster_id": 111798,
          "cite": [
            "93 L. Ed. 2d 954",
            "107 S. Ct. 851",
            "479 U.S. 564",
            "1987 U.S. LEXIS 418",
            "55 U.S.L.W. 4162"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
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
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mays v. State",
          "cluster_id": 1523430,
          "cite": [
            "904 S.W.2d 920",
            "1995 Tex. App. LEXIS 1814",
            "1995 WL 470664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albert L. Wilson v. Edward Murray, Director of the Virginia Department of Corrections",
          "cluster_id": 480360,
          "cite": [
            "806 F.2d 1232",
            "1986 U.S. App. LEXIS 34712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beverly A. Seymour v. Diane Walker,respondent-Appellee",
          "cluster_id": 770145,
          "cite": [
            "224 F.3d 542",
            "2000 U.S. App. LEXIS 20170",
            "2000 WL 1154017"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Stephenson",
          "cluster_id": 2410270,
          "cite": [
            "878 S.W.2d 530",
            "1994 Tenn. LEXIS 143"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
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
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
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
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Bomar",
          "cluster_id": 1989353,
          "cite": [
            "826 A.2d 831",
            "573 Pa. 426",
            "2003 Pa. LEXIS 920"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
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
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
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
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garcia v. State",
          "cluster_id": 2459967,
          "cite": [
            "919 S.W.2d 370",
            "1996 Tex. Crim. App. LEXIS 35",
            "1994 WL 706957"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Juan H. v. Walter Allen III",
          "cluster_id": 790372,
          "cite": [
            "408 F.3d 1262"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holland v. State",
          "cluster_id": 1784340,
          "cite": [
            "587 So. 2d 848",
            "1991 WL 178413"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Pena",
          "cluster_id": 1229684,
          "cite": [
            "869 P.2d 932",
            "232 Utah Adv. Rep. 3",
            "1994 Utah LEXIS 6",
            "1994 WL 46544"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Watkins v. Sowders",
          "cluster_id": 110371,
          "cite": [
            "66 L. Ed. 2d 549",
            "101 S. Ct. 654",
            "449 U.S. 341",
            "1981 U.S. LEXIS 53",
            "49 U.S.L.W. 4082"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Russel William Burket v. Ronald Angelone, Director, Virginia Department of Corrections",
          "cluster_id": 768204,
          "cite": [
            "208 F.3d 172",
            "2000 U.S. App. LEXIS 5116",
            "2000 WL 309299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "North Carolina v. Butler:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110065 OR 9427547 OR 9427548 OR 9427549) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzQ0ODE2MDAwMDAwJnM9ODQ0MTU2JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110065+OR+9427547+OR+9427548+OR+9427549%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110065 OR 9427547 OR 9427548 OR 9427549)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNjEmcz0xMjQ0NzUyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110065+OR+9427547+OR+9427548+OR+9427549%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110065 OR 9427547 OR 9427548 OR 9427549)",
        "reviewed": 46,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 46,
        "triage_read": 1,
        "triage_snippet_classified": 45
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110065 OR 9427547 OR 9427548 OR 9427549)",
    "indexed_citing_opinions": 1355,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110065,
        "count": 1169,
        "count_source": "search"
      },
      {
        "opinion_id": 9427547,
        "count": 212,
        "count_source": "search"
      },
      {
        "opinion_id": 9427548,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427549,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2173,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/north-carolina-v-butler.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwNDQ4MDgmcz0xMDI3NjE4OCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110065+OR+9427547+OR+9427548+OR+9427549%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110065,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 277766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 278912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 280792,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 288244,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 294040,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 296344,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 300514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 300899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 305663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 315587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 319939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 320109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 320439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 324438,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 328787,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 339071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 340511,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1163905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1180267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1191424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1224771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1259789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1264180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1275041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1338200,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1413276,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1414808,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1424568,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1434456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1575075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1657897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1658656,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1662874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1728481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1824562,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1885915,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1891400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 1892749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 2157474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 2232976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 2327606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 2610043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110065,
        "cited_id": 2616723,
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
    "date_created": "2026-07-05T15:56:28Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:56:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:56:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:00:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:56:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — North Carolina v. Butler

```
<opinion type="majority">
<author id="b428-5">Me. Justice Stewart</author>
<p id="ATY">delivered the opinion of the Court.</p>
<p id="b428-6">In evident conflict with the present view of every other court that has considered the issue, the North Carolina Supreme Court has held that <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, requires that no statement of a person under custodial interrogation may be admitted in evidence against him unless, at the time the statement was made, he explicitly waived the right to the presence of a lawyer. We granted certiorari to consider whether this <em>per se </em>rule reflects a proper understanding of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>decision. <span class="citation multiple-matches"><a href="/c/U.%20S./439/1046/">439 U. S. 1046</a></span>.</p>
<p id="b428-7">The respondent was convicted in a North Carolina trial court of kidnaping, armed robbery, and felonious assault. The evidence at his trial showed that he and a man named Elmer Lee had robbed a gas station in Goldsboro, N. C., in December 1976, and had shot the station attendant as he was attempting to escape. The attendant was paralyzed, but survived to testify against the respondent.</p>
<p id="b428-8">The prosecution also produced evidence of incriminating statements made by the respondent shortly after his arrest by Federal Bureau of Investigation agents in the Bronx, N. Y., on the basis of a North Carolina fugitive warrant. Outside the presence of the jury, FBI Agent Martinez testified that at the time of the arrest he fully advised the respondent of the rights delineated in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>case. According to the uncontroverted testimony of Martinez, the agents then took the respondent to the FBI office in nearby New Rochelle, N. Y. There, after the agents determined that the respondent had an 11th grade education and was literate, he was given the Bureau’s “Advice of Rights” form <page-number citation-index="1" label="371">*371</page-number>which he read.<footnotemark>1</footnotemark> When asked if he understood his rights, he replied that he did. The respondent refused to sign the waiver at the bottom of the form. He was told that he need neither speak nor sign the form, but that the agents would like him to talk to them. The respondent replied: “I will talk to you but I am not signing any form.” He then made inculpatory statements.<footnotemark>2</footnotemark> Agent Martinez testified that the respondent said nothing when advised of his right to the assistance of a lawyer. At no time did the respondent request counsel or attempt to terminate the agents’ questioning.</p>
<p id="b429-5">At the conclusion of this testimony the respondent moved to suppress the evidence of his incriminating statements on the ground that he had not waived his right to the assistance of counsel at the time the statements were made. The court denied the motion, finding that</p>
<blockquote id="b429-6">“the statement made by the defendant, William Thomas Butler, to Agent David C. Martinez, was made freely and voluntarily to said agent after having been advised of his rights as required by the Miranda ruling, including his right to an attorney being present at the time of the inquiry and that the defendant, Butler, understood his <page-number citation-index="1" label="372">*372</page-number>rights; [and] that he effectively waived his rights, including the right to have an attorney present during the questioning by his indication that he was willing to answer questions, having read the rights form together with the Waiver of Rights . . . App. A-22 to A-23.</blockquote>
<p id="b430-5">The respondent’s statements were then admitted into evidence, and the jury ultimately found the respondent guilty of each offense charged.</p>
<p id="b430-6">On appeal, the North Carolina Supreme Court reversed the convictions and ordered a new trial. It found that the statements had been admitted in violation of the requirements of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>decision, noting that the respondent had refused to waive in writing his right to have counsel present and that there had not been a <em>specific </em>oral waiver. As it had in at least two earlier cases, the court read the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion as</p>
<blockquote id="b430-7">“provid [ing] in plain language that waiver of the right to counsel during interrogation will not be recognized unless such waiver is 'specifically made’ after the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings have been given.” <span class="citation" data-id="1338200"><a href="/opinion/1338200/state-v-butler/#255" aria-description="Citation for case: State v. Butler">295 N. C. 250, 255</a></span>, <span class="citation" data-id="1338200"><a href="/opinion/1338200/state-v-butler/#413" aria-description="Citation for case: State v. Butler">244 S. E. 2d 410, 413</a></span> (1978).</blockquote>
<p id="b430-8">See <em>State </em>v. <em>Blackmon, </em><span class="citation" data-id="1275041"><a href="/opinion/1275041/state-v-blackmon/#49" aria-description="Citation for case: State v. Blackmon">280 N. C. 42, 49-50</a></span>, <span class="citation" data-id="1275041"><a href="/opinion/1275041/state-v-blackmon/#127" aria-description="Citation for case: State v. Blackmon">185 S. E. 2d 123, 127-128</a></span> (1971); <em>State </em>v. <em>Thacker, </em><span class="citation" data-id="1224771"><a href="/opinion/1224771/state-v-thacker/#453" aria-description="Citation for case: State v. Thacker">281 N. C. 447, 453-454</a></span>, <span class="citation" data-id="1224771"><a href="/opinion/1224771/state-v-thacker/#149" aria-description="Citation for case: State v. Thacker">189 S. E. 2d 145, 149-150</a></span> (1972).<footnotemark>3</footnotemark></p>
<p id="b430-9">We conclude that the North Carolina Supreme Court erred in its reading of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion. There, this Court said:</p>
<blockquote id="b430-10">“If the interrogation continues without the presence of an attorney and a statement is taken, a heavy burden <page-number citation-index="1" label="373">*373</page-number>rests on the government to demonstrate that the defendant knowingly and intelligently waived his privilege against self-incrimination and his right to retained or appointed counsel.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 475</a></span>.</blockquote>
<p id="b431-4">The Court’s opinion went on to say:</p>
<blockquote id="b431-5">“An express statement that the individual is willing to make a statement and does not want an attorney followed closely by a statement could constitute a waiver. But a valid waiver will not be presumed simply from the silence of the accused after warnings are given or simply from the fact that a confession was in fact eventually obtained.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></em></blockquote>
<p id="b431-6">Thus, the Court held that an express statement can constitute a waiver, and that silence alone after such warnings cannot do so. But the Court did not hold that such an express statement is indispensable to a finding of waiver.</p>
<p id="b431-7">An express written or oral statement of waiver of the right to remain silent or of the right to counsel is usually strong proof of the validity of that waiver, but is not inevitably either necessary or sufficient to establish waiver. The question is not one of form, but rather whether the defendant in fact knowingly and voluntarily waived the rights delineated in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>case. As was unequivocally said in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>mere silence is not enough. That does not mean that the defendant’s silence, coupled with an understanding of his rights and a course of conduct indicating waiver, may never support a conclusion that a defendant has waived his rights. The courts must presume that a defendant did not waive his rights; the prosecution’s burden is great; but in at least some cases waiver can be clearly inferred from the actions and words of the person interrogated.<footnotemark>4</footnotemark></p>
<p id="b432-4"><page-number citation-index="1" label="374">*374</page-number>The Court’s opinion in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>explained the reasons for the prophylactic rules it created:</p>
<blockquote id="b432-5">“We have concluded that without proper safeguards the process of in-custody interrogation of persons suspected or accused of crime contains inherently compelling pressures which work to undermine the individual’s will to resist and to compel him to speak where he would not otherwise do so freely. In order to combat these pressures and to permit a full opportunity to exercise the privilege against self-incrimination, the accused must be adequately and effectively apprised of his rights and the exercise of those rights must be fully honored.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 467</a></span>.</blockquote>
<p id="b432-6">The <em>per se </em>rule that the North Carolina Supreme Court has found in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>does not speak to these concerns. There is no doubt that this respondent was adequately and effectively apprised of his rights. The only question is whether he waived the exercise of one of those rights, the right to the presence of a lawyer. Neither the state court nor the respondent has offered any reason why there must be a negative answer to that question in the absence of an <em>express </em>waiver. This is not the first criminal case to question whether a defendant waived his constitutional rights. It is an issue with which courts must repeatedly deal. Even when a right scr fundamental as that to counsel at trial is involved, the question of waiver must be determined on “the particular facts and circumstances surrounding that case, including the back<page-number citation-index="1" label="375">*375</page-number>ground, experience, and conduct of the accused.” <em>Johnson </em>v. <em>Zerbst, </em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 464</a></span>. See also <em>United States </em>v. <em>Washington, </em><span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#188" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 188</a></span>; <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span>; <em>Frazier </em>v. <em>Cupp, </em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#739" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 739</a></span>.</p>
<p id="b433-4">We see no reason to discard that standard and replace it with an inflexible <em>per se </em>rule in a case such as this. As stated at the outset of this opinion, it appears that every court that has considered this question has now reached the same conclusion. Ten of the eleven United States Courts of Appeals<footnotemark>5</footnotemark> and the courts of at least 17 States<footnotemark>6</footnotemark> have held that an explicit state<page-number citation-index="1" label="376">*376</page-number>ment of waiver is not invariably necessary to support a finding that the defendant waived the right to remain silent or the right to counsel guaranteed by the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>case. By creating an inflexible rule that no implicit waiver can ever suffice, the North Carolina Supreme Court has gone beyond the requirements of federal organic law. It follows that its judgment cannot stand, since a state court can neither add to nor subtract from the mandates of the United States Constitution. <em>Oregon </em>v. <em>Hass, </em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714</a></span>.<footnotemark>7</footnotemark></p>
<p id="b434-5">Accordingly, the judgment is vacated, and the case is remanded to the North Carolina Supreme Court for further proceedings not inconsistent with this opinion.</p>
<p id="b434-6">
<em>It is so ordered.</em>
</p>
<judges id="b434-7">Mr. Justice Powell took no part in the consideration or decision of this case.</judges>
<footnote label="1">
<p id="b429-7"> The parties disagree over whether the respondent was also orally advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights at the New Rochelle office. There is no dispute that he was given those warnings orally at the scene of the arrest, or that he read the “Advice of Rights” form in the New Rochelle office. This factual controversy, therefore, is not relevant to the basic issue in this case.</p>
<p id="b429-8">The dissenting opinion points out, <em>post, </em>at 378, that at oral argument the respondent’s counsel disputed the fact that the respondent is literate. But the trial court specifically found that “it had been . . . determined by Agent Martinez that the defendant has an Eleventh Grade Education and that he could read and write . . . .” App. A-21. This finding, based upon uncontroverted evidence, is binding on this Court.</p>
</footnote>
<footnote label="2">
<p id="b429-9"> The respondent admitted to the agents that he and Lee had been drinking heavily on' the day of the robbery. He acknowledged that they had decided to rob a gas station, but denied that he had actually participated in the robbery. His friend, he said, had shot the attendant.</p>
</footnote>
<footnote label="3">
<p id="b430-11"> But see <em>State </em>v. <em>Siler, </em><span class="citation" data-id="1259789"><a href="/opinion/1259789/state-v-siler/#550" aria-description="Citation for case: State v. Siler">292 N. C. 543, 550</a></span>, <span class="citation" data-id="1259789"><a href="/opinion/1259789/state-v-siler/#738" aria-description="Citation for case: State v. Siler">234 S. E. 2d 733, 738</a></span> (1977). In that case, the North Carolina Supreme Court adhered to the interpretation of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>it first expressed in <em><span class="citation" data-id="1275041"><a href="/opinion/1275041/state-v-blackmon/" aria-description="Citation for case: State v. Blackmon">Blackmon</a></span>, </em>but acknowledged that it might find waiver without an express written or oral statement if the defendant’s subsequent comments revealed that his earlier silence had been meant as a waiver. Although <em><span class="citation" data-id="1259789"><a href="/opinion/1259789/state-v-siler/" aria-description="Citation for case: State v. Siler">Siler</a></span> </em>was cited by the State Supreme Court in the present case, that portion of the <em><span class="citation" data-id="1259789"><a href="/opinion/1259789/state-v-siler/" aria-description="Citation for case: State v. Siler">Siler</a></span> </em>opinion was not discussed.</p>
</footnote>
<footnote label="4">
<p id="b431-8"> We do not today even remotely question the holding in <em>Carnley </em>v. <em>Cochran, </em><span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/" aria-description="Citation for case: Carnley v. Cochran">369 U. S. 506</a></span>, which was specificaEy approved in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 475</a></span>. In that case, decided before <em>Gideon </em>v. <em>Wainwright, </em><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>, the Court held that the defendant had a <page-number citation-index="1" label="374">*374</page-number>constitutional right to counsel under the Fourteenth Amendment. The Florida Supreme Court had presumed that his right had been waived because there was no evidence in the record that he had requested counsel. The Court refused to allow a presumption of waiver from a silent record. It said: “The record must show, or there must be an allegation and evidence which show, that an accused was offered counsel but intelligently and understandingly rejected the offer.” <span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/#516" aria-description="Citation for case: Carnley v. Cochran">369 U. S., at 516</a></span>. This statement is consistent with our decision today, which is merely that a court <em>may </em>find an intelligent and understanding rejection of counsel in situations where the defendant did not <em>expressly </em>state as much.</p>
</footnote>
<footnote label="5">
<p id="b433-5"> <em>United States </em>v. <em>Speaks, </em><span class="citation" data-id="300899"><a href="/opinion/300899/united-states-v-albert-philip-speaks/" aria-description="Citation for case: United States v. Albert Philip Speaks">453 F. 2d 966</a></span> (CA1 1972); <em>United States </em>v. <em>Boston, </em>508. F. 2d 1171 (CA2 1974); <em>United States </em>v. <em>Stuckey, </em><span class="citation" data-id="296344"><a href="/opinion/296344/united-states-v-jusse-j-stuckey/" aria-description="Citation for case: United States v. Jusse J. Stuckey">441 F. 2d 1104</a></span> (CA3 1971); <em>Blackmon </em>v. <em>Blackledge, </em><span class="citation" data-id="339071"><a href="/opinion/339071/johnny-james-blackmon-v-stanley-blackledge-warden-central-prison/" aria-description="Citation for case: Johnny James Blackmon v. Stanley Blackledge, Warden,...">541 F. 2d 1070</a></span> (CA4 1976); <em>United States </em>v. <em>Hayes, </em><span class="citation" data-id="277766"><a href="/opinion/277766/united-states-v-maynard-francis-hayes/" aria-description="Citation for case: United States v. Maynard Francis Hayes">385 F. 2d 375</a></span> (CA4 1967); <em>United States </em>v. <em>Cavallino, </em><span class="citation" data-id="320109"><a href="/opinion/320109/united-states-v-ronald-anthony-cavallino/" aria-description="Citation for case: United States v. Ronald Anthony Cavallino">498 F. 2d 1200</a></span> (CA5 1974); <em>United States </em>v. <em>Montos, </em><span class="citation" data-id="288244"><a href="/opinion/288244/united-states-v-kenneth-george-montos/" aria-description="Citation for case: United States v. Kenneth George Montos">421 F. 2d 215</a></span> (CA5 1970); <em>United States </em>v. <em>Ganter, </em><span class="citation" data-id="294040"><a href="/opinion/294040/united-states-v-steven-ganter/" aria-description="Citation for case: United States v. Steven Ganter">436 F. 2d 364</a></span> (CA7 1970); <em>United States </em>v. <em>Marchildon, </em><span class="citation" data-id="328787"><a href="/opinion/328787/united-states-v-robert-dale-marchildon/" aria-description="Citation for case: United States v. Robert Dale Marchildon">519 F. 2d 337</a></span> (CA8 1975); <em>Hughes </em>v. <em>Swenson, </em><span class="citation" data-id="300514"><a href="/opinion/300514/dennis-paul-hughes-v-harold-r-swenson-warden/" aria-description="Citation for case: Dennis Paul Hughes v. Harold R. Swenson, Warden">452 F. 2d 866</a></span> (CA8 1971); <em>United States </em>v. <em>Moreno-Lopez, </em><span class="citation" data-id="305663"><a href="/opinion/305663/united-states-v-isabel-moreno-lopez/" aria-description="Citation for case: United States v. Isabel Moreno-Lopez">466 F. 2d 1205</a></span> (CA9 1972); <em>United States </em>v. <em>Hilliker, </em><span class="citation" data-id="293991"><a href="/opinion/293991/united-states-v-gary-lee-hilliker/" aria-description="Citation for case: United States v. Gary Lee Hilliker">436 F. 2d 101</a></span> (CA9 1970); <em>Bond </em>v. <em>United States, </em><span class="citation" data-id="280792"><a href="/opinion/280792/roy-gene-bond-v-united-states/" aria-description="Citation for case: Roy Gene Bond v. United States">397 F. 2d 162</a></span> (CA10 1968) (but see <em>Sullins </em>v. <em>United States, </em><span class="citation" data-id="9453346"><a href="/opinion/278912/howard-douglas-sullins-james-floyd-williams-audrey-louise-gillingham-v/" aria-description="Citation for case: Howard Douglas Sullins, James Floyd Williams, Audrey...">389 F. 2d 985</a></span> (CA10 1968)); <em>United States </em>v. <em>Cooper, </em>163 U. S. App. D. C. 55, <span class="citation" data-id="9460787"><a href="/opinion/320439/united-states-v-donald-m-cooper/" aria-description="Citation for case: United States v. Donald M. Cooper">499 F. 2d 1060</a></span> (1974). In <em>Blackmon </em>v. <em><span class="citation" data-id="339071"><a href="/opinion/339071/johnny-james-blackmon-v-stanley-blackledge-warden-central-prison/" aria-description="Citation for case: Johnny James Blackmon v. Stanley Blackledge, Warden,...">Blackledge, supra,</a></span> </em>the Court of Appeals for the Fourth Circuit specifically rejected the North Carolina Supreme Court’s inflexible view that only express waivers of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights can be valid.</p>
<p id="b433-6">The Courts of Appeals have unanimously rejected the similar argument that refusal to sign a written waiver form precludes a finding of waiver. See <em>United States </em>v. <em><span class="citation" data-id="300899"><a href="/opinion/300899/united-states-v-albert-philip-speaks/" aria-description="Citation for case: United States v. Albert Philip Speaks">Speaks, supra;</a></span> United States </em>v. <em>Boston, supra; United States </em>v. <em><span class="citation" data-id="296344"><a href="/opinion/296344/united-states-v-jusse-j-stuckey/" aria-description="Citation for case: United States v. Jusse J. Stuckey">Stuckey, supra;</a></span> United States </em>v. <em>Thompson, </em><span class="citation" data-id="286880"><a href="/opinion/286880/united-states-v-vernon-thompson/" aria-description="Citation for case: United States v. Vernon Thompson">417 F. 2d 196</a></span> (CA4 1969); <em>United States </em>v. <em>Guzman-Guzman, </em><span class="citation" data-id="315587"><a href="/opinion/315587/united-states-v-arturo-guzman-guzman/" aria-description="Citation for case: United States v. Arturo Guzman-Guzman">488 F. 2d 965</a></span> (CA5 1974); <em>United States </em>v. <em>Caulton, </em><span class="citation" data-id="319939"><a href="/opinion/319939/united-states-v-james-raymond-caulton/" aria-description="Citation for case: United States v. James Raymond Caulton">498 F. 2d 412</a></span> (CA6 1974); <em>United States </em>v. <em>Crisp, </em><span class="citation" data-id="293647"><a href="/opinion/293647/united-states-v-donald-roy-crisp/" aria-description="Citation for case: United States v. Donald Roy Crisp">435 F. 2d 354</a></span> (CA7 1970); <em>United States </em>v. <em>Zamarripa, </em><span class="citation" data-id="340511"><a href="/opinion/340511/united-states-v-antonio-valentino-zamarripa/" aria-description="Citation for case: United States v. Antonio Valentino Zamarripa">544 F. 2d 978</a></span> (CA8 1976); <em>United States </em>v. <em><span class="citation" data-id="305663"><a href="/opinion/305663/united-states-v-isabel-moreno-lopez/" aria-description="Citation for case: United States v. Isabel Moreno-Lopez">Moreno-Lopez, supra;</a></span> Bond </em>v. <em>United States, supra; </em>and <em>United States </em>v. <em><span class="citation" data-id="9460787"><a href="/opinion/320439/united-states-v-donald-m-cooper/" aria-description="Citation for case: United States v. Donald M. Cooper">Cooper, supra.</a></span></em></p>
</footnote>
<footnote label="6">
<p id="b433-7"><em> Sullivan </em>v. <em>State, </em><span class="citation" data-id="1658656"><a href="/opinion/1658656/sullivan-v-state/" aria-description="Citation for case: Sullivan v. State">351 So. 2d 659</a></span> (Ala. Crim. App.), cert. denied, <span class="citation" data-id="1657897"><a href="/opinion/1657897/ex-parte-sullivan/" aria-description="Citation for case: Ex Parte Sullivan">351 So. 2d 665</a></span> (Ala. 1977); <em>State </em>v. <em>Pineda, </em><span class="citation" data-id="1180267"><a href="/opinion/1180267/state-v-pineda/" aria-description="Citation for case: State v. Pineda">110 Ariz. 342</a></span>, <span class="citation" data-id="1180267"><a href="/opinion/1180267/state-v-pineda/" aria-description="Citation for case: State v. Pineda">519 P. 2d 41</a></span> (1974); <em>State ex rel. Berger </em>v. <em>Superior Court, </em><span class="citation multiple-matches"><a href="/c/Ariz./109/506/">109 Ariz. 506</a></span>, <span class="citation multiple-matches"><a href="/c/P.%202d/513/935/">513 P. 2d 935</a></span> (1973); <em>People </em>v. <em>Johnson, </em><span class="citation" data-id="9624615"><a href="/opinion/1413276/people-v-johnson/" aria-description="Citation for case: People v. Johnson">70 Cal. 2d 541</a></span>, <span class="citation" data-id="9624615"><a href="/opinion/1413276/people-v-johnson/" aria-description="Citation for case: People v. Johnson">450 P. 2d 865</a></span> (1969) (reversing lower court on other grounds); <em>People </em>v. <em>Weaver, </em><span class="citation" data-id="2616723"><a href="/opinion/2616723/people-v-weaver/" aria-description="Citation for case: People v. Weaver">179 Colo. 331</a></span>, <span class="citation" data-id="2616723"><a href="/opinion/2616723/people-v-weaver/" aria-description="Citation for case: People v. Weaver">500 P. 2d 980</a></span> (1972); <page-number citation-index="1" label="376">*376</page-number><em>Reed </em>v. <em>People, </em><span class="citation" data-id="2610043"><a href="/opinion/2610043/reed-v-people/" aria-description="Citation for case: Reed v. People">171 Colo. 421</a></span>, <span class="citation" data-id="2610043"><a href="/opinion/2610043/reed-v-people/" aria-description="Citation for case: Reed v. People">467 P. 2d 809</a></span> (1970); <em>State </em>v. <em>Craig, </em><span class="citation" data-id="1824562"><a href="/opinion/1824562/state-v-craig/" aria-description="Citation for case: State v. Craig">237 So. 2d 737</a></span> (Fla. 1970); <em>Peek </em>v. <em>State, </em><span class="citation" data-id="1424568"><a href="/opinion/1424568/peek-v-state/" aria-description="Citation for case: Peek v. State">239 Ga. 422</a></span>, <span class="citation" data-id="1424568"><a href="/opinion/1424568/peek-v-state/" aria-description="Citation for case: Peek v. State">238 S. E. 2d 12</a></span> (1977); <em>People </em>v. <em>Brooks, </em><span class="citation" data-id="2157474"><a href="/opinion/2157474/people-v-brooks/" aria-description="Citation for case: People v. Brooks">51 Ill. 2d 156</a></span>, <span class="citation" data-id="2157474"><a href="/opinion/2157474/people-v-brooks/" aria-description="Citation for case: People v. Brooks">281 N. E. 2d 326</a></span> (1972); <em>State </em>v. <em>Wilson, </em><span class="citation" data-id="1163905"><a href="/opinion/1163905/state-v-wilson/" aria-description="Citation for case: State v. Wilson">215 Kan. 28</a></span>, <span class="citation" data-id="1163905"><a href="/opinion/1163905/state-v-wilson/" aria-description="Citation for case: State v. Wilson">523 P. 2d 337</a></span> (1974); <em>State </em>v. <em>Hazelton, </em><span class="citation" data-id="2359781"><a href="/opinion/2359781/state-v-hazelton/" aria-description="Citation for case: State v. Hazelton">330 A. 2d 919</a></span> (Me. 1975); <em>Miller </em>v. <em>State, </em><span class="citation" data-id="9754194"><a href="/opinion/2327606/miller-v-state/" aria-description="Citation for case: Miller v. State">251 Md. 362</a></span>, <span class="citation" data-id="9754194"><a href="/opinion/2327606/miller-v-state/" aria-description="Citation for case: Miller v. State">247 A. 2d 530</a></span> (1968); <em>Commonwealth </em>v. <em>Murray, </em><span class="citation" data-id="2232976"><a href="/opinion/2232976/commonwealth-v-murray/" aria-description="Citation for case: Commonwealth v. Murray">359 Mass. 541</a></span>, <span class="citation" data-id="2232976"><a href="/opinion/2232976/commonwealth-v-murray/" aria-description="Citation for case: Commonwealth v. Murray">269 N. E. 2d 641</a></span> (1971); <em>State </em>v. <em>Alewine, </em><span class="citation" data-id="1662874"><a href="/opinion/1662874/state-v-alewine/" aria-description="Citation for case: State v. Alewine">474 S. W. 2d 848</a></span> (Mo. 1971); <em>Burnside </em>v. <em>State, </em><span class="citation" data-id="1728481"><a href="/opinion/1728481/burnside-v-state/" aria-description="Citation for case: Burnside v. State">473 S. W. 2d 697</a></span> (Mo. 1971); <em>Shirey </em>v. <em>State, </em><span class="citation" data-id="1191424"><a href="/opinion/1191424/shirey-v-state/" aria-description="Citation for case: Shirey v. State">520 P. 2d 701</a></span> (Okla. Crim. App. 1974); <em>State </em>v. <em>Davidson, </em><span class="citation" data-id="1434456"><a href="/opinion/1434456/state-v-davidson/" aria-description="Citation for case: State v. Davidson">252 Ore. 617</a></span>, <span class="citation" data-id="1434456"><a href="/opinion/1434456/state-v-davidson/" aria-description="Citation for case: State v. Davidson">451 P. 2d 481</a></span> (1969); <em>Commonwealth </em>v. <em>Garnett, </em><span class="citation" data-id="1892749"><a href="/opinion/1892749/commonwealth-v-garnett/" aria-description="Citation for case: Commonwealth v. Garnett">458 Pa. 4</a></span>, <span class="citation" data-id="1892749"><a href="/opinion/1892749/commonwealth-v-garnett/" aria-description="Citation for case: Commonwealth v. Garnett">326 A. 2d 335</a></span> (1974); <em>Bowling </em>v. <em>State, </em><span class="citation" data-id="1575075"><a href="/opinion/1575075/bowling-v-state/" aria-description="Citation for case: Bowling v. State">458 S. W. 2d 639</a></span> (Tenn. Crim. App. 1970); <em>State </em>v. <em>Young, </em><span class="citation" data-id="1414808"><a href="/opinion/1414808/state-v-young/" aria-description="Citation for case: State v. Young">89 Wash. 2d 613</a></span>, <span class="citation" data-id="1414808"><a href="/opinion/1414808/state-v-young/" aria-description="Citation for case: State v. Young">574 P. 2d 1171</a></span> (1978). See also <em>Aaron </em>v. <em>State, </em><span class="citation" data-id="1885915"><a href="/opinion/1885915/aaron-v-state/" aria-description="Citation for case: Aaron v. State">275 A. 2d 791</a></span> (Del. 1971); <em>State </em>v. <em>Nelson, </em><span class="citation" data-id="1891400"><a href="/opinion/1891400/state-v-nelson/" aria-description="Citation for case: State v. Nelson">257 N. W. 2d 356</a></span> (Minn. 1977); <em>Land </em>v. <em>Commonwealth, </em><span class="citation" data-id="1264180"><a href="/opinion/1264180/land-v-commonwealth/" aria-description="Citation for case: Land v. Commonwealth">211 Va. 223</a></span>, <span class="citation" data-id="1264180"><a href="/opinion/1264180/land-v-commonwealth/" aria-description="Citation for case: Land v. Commonwealth">176 S. E. 2d 586</a></span> (1970) (reversing lower court on other grounds).</p>
</footnote>
<footnote label="7">
<p id="b434-11"> By the same token this Court must accept whatever construction of a state constitution is placed upon it by the highest court of the State.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Northrup v. City of Toledo Police Dept.json  (`lake-record`, 2 assertions)

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
{"assertion_id": "066ea0e436159a8f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Northrup v. City of Toledo Police Dept"}, "payload": {"all": [{"cite": "785 F.3d 1128", "page": "1128", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "785"}, {"cite": "2015 FED App. 0092P", "page": "0092P", "reporter": "FED App.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "2015"}, {"cite": "2015 U.S. App. LEXIS 7868", "page": "7868", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2015"}, {"cite": "2015 WL 2217061", "page": "2217061", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2015"}], "display": "785 F.3d 1128", "official": {"cite": "785 F.3d 1128", "page": "1128", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "785"}, "official_selection_present": true, "record_id": "Northrup v. City of Toledo Police Dept"}}
{"assertion_id": "7edceee210787167", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Northrup v. City of Toledo Police Dept"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Northrup v. City of Toledo Police Dept", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/O'Connor v. Ortega.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "O'Connor v. Ortega"
type: case
citation: "480 U.S. 709 (1987)"
parallel_cite: "107 S. Ct. 1492; 94 L. Ed. 2d 714; 1 I.E.R. Cas. (BNA) 1617; 55 U.S.L.W. 4405; 42 Empl. Prac. Dec. (CCH) 36,891"
neutral_cite: 1987 U.S. LEXIS 1507
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-03-31
docket: 85-530
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-03-31
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "O'Connor v. Ortega"
  varies_by_point: false
  scope_note: "Plurality opinion (O'Connor, J.); Scalia concurred in the judgment, supplying a fifth vote for the reasonableness standard, which is controlling. Good law; reaffirmed and applied in City of Ontario v. Quon (2010)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111851/oconnor-v-ortega/"
  cluster_id: 111851
  opinion_id: 9430897
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Anchor (workplace REP)"
related: ["[[City of Ontario v. Quon]]"]
aliases: []
tags: ["case", "fourth-amendment", "special-needs", "workplace", "public-employee", "reasonable-expectation-of-privacy"]
holding: "Public employees may have a reasonable expectation of privacy in their offices, desks, and files, subject to the operational realities of the workplace; but a public employer's work-related search — whether to retrieve work materials or to investigate work-related misconduct — is judged by reasonableness under all the circumstances, without a warrant or probable cause."
lake:
  record_id: "O'Connor v. Ortega"
  status: under_review
  projected_at: 2026-07-06
---

# O'Connor v. Ortega

*480 U.S. 709 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Dr. Ortega, a physician and administrator at a California state hospital, was placed on administrative leave while officials investigated suspected workplace misconduct (concerning resident-training and the acquisition of a computer). During the investigation, hospital officials entered and searched his office, desk, and file cabinets and seized personal items later used against him in administrative proceedings. Ortega sued under § 1983, claiming the search violated the Fourth Amendment.

## Issue
Whether a public employee has a Fourth Amendment expectation of privacy in his office, desk, and files, and what standard governs a search of those areas by his government employer for work-related purposes.

## Rule
Public employees are not stripped of Fourth Amendment protection at work, though their privacy may be reduced by workplace realities. "Individuals do not lose Fourth Amendment rights merely because they work for the government instead of a private employer. The operational realities of the workplace, however, may make *some* employees' expectations of privacy unreasonable when an intrusion is by a supervisor rather than a law enforcement official." — 480 U.S. at 717. ^pin-717

Work-related employer searches are judged by reasonableness, not warrant or probable cause: "We hold, therefore, that public employer intrusions on the constitutionally protected privacy interests of government employees for noninvestigatory, work-related purposes, as well as for investigations of work-related misconduct, should be judged by the standard of reasonableness under all the circumstances. Under this reasonableness standard, both the inception and the scope of the intrusion must be reasonable." — *Id.* at 725–726. ^pin-725

## Application
Because Dr. Ortega did not share his office and kept personal materials in his desk and files, he had a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] there. But the warrant and probable-cause requirements would be unworkable for the routine, work-related searches public employers must make, so the intrusion was instead measured by reasonableness — assessed at both inception and scope. The Court did not itself resolve whether this particular search was reasonable; it [[Reading and Citing Cases#on-remand|remanded]] for that fact-bound determination.

## Conclusion
Ortega had a Fourth Amendment privacy interest in his office, but the employer's work-related search is governed by reasonableness rather than warrant/probable cause; the case was [[Reading and Citing Cases#on-remand|remanded]] to apply that standard.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (plurality; Scalia, J., concurring in the judgment, provided the controlling fifth vote for the reasonableness standard).
- No negative treatment. *O'Connor* is the anchor for public-employee workplace privacy; its reasonableness framework was reaffirmed and applied to an employer's review of an employee's electronic messages in [[City of Ontario v. Quon]] (2010).

## Appears on
- [[Special Needs and Administrative Searches]] — *Anchor (workplace REP)*

## Sources
- *O'Connor v. Ortega*, 480 U.S. 709 (1987) — https://www.courtlistener.com/opinion/111851/oconnor-v-ortega/ — pinpoints: 717, 725–726.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8d223e86caac43f5", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "O'Connor v. Ortega"}, "payload": {"all": [{"cite": "480 U.S. 709", "page": "709", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "480"}, {"cite": "107 S. Ct. 1492", "page": "1492", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "107"}, {"cite": "94 L. Ed. 2d 714", "page": "714", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "94"}, {"cite": "1987 U.S. LEXIS 1507", "page": "1507", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1987"}, {"cite": "1 I.E.R. Cas. (BNA) 1617", "page": "1617", "reporter": "I.E.R. Cas. (BNA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "1"}, {"cite": "55 U.S.L.W. 4405", "page": "4405", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "55"}, {"cite": "42 Empl. Prac. Dec. (CCH) 36,891", "page": "36,891", "reporter": "Empl. Prac. Dec. (CCH)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "42"}], "display": "480 U.S. 709", "official": {"cite": "480 U.S. 709", "page": "709", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "480"}, "official_selection_present": true, "record_id": "O'Connor v. Ortega"}}
{"assertion_id": "7901a2e5313b72cb", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-717", "record_id": "O'Connor v. Ortega"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-717", "pinpoint_status": "slip-only", "quote": "--- # O'Connor v. Ortega *480 U.S. 709 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Dr. Ortega, a physician and administrator at a California state hospital, was placed on administrative leave while officials investigated suspected workplace misconduct (concerning resident-training and the acquisition of a computer). During the investigation, hospital officials entered and searched his office, desk, and file cabinets and seized personal items later used against him in administrative proceedings. Ortega sued under § 1983, claiming the search violated the Fourth Amendment. ## Issue Whether a public employee has a Fourth Amendment expectation of privacy in his office, desk, and files, and what standard governs a search of those areas by his government employer for work-related purposes. ## Rule Public employees are not stripped of Fourth Amendment protection at work, though their privacy may be reduced by workplace realities.", "quote_fidelity": "mismatch", "record_id": "O'Connor v. Ortega", "star_marker": null}}
{"assertion_id": "fbad6dca46abde8b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-725", "record_id": "O'Connor v. Ortega"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-725", "pinpoint_status": "slip-only", "quote": "We hold, therefore, that public employer intrusions on the constitutionally protected privacy interests of government employees for noninvestigatory, work-related purposes, as well as for investigations of work-related misconduct, should be judged by the standard of reasonableness under all the circumstances. Under this reasonableness standard, both the inception and the scope of the intrusion must be reasonable.", "quote_fidelity": "mismatch", "record_id": "O'Connor v. Ortega", "star_marker": null}}
{"assertion_id": "398be112f6e1bd9b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "O'Connor v. Ortega"}, "payload": {"as_of_content": "1987-03-31", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "O'Connor v. Ortega", "scope_note": "Plurality opinion (O'Connor, J.); Scalia concurred in the judgment, supplying a fifth vote for the reasonableness standard, which is controlling. Good law; reaffirmed and applied in City of Ontario v. Quon (2010).", "varies_by_point": false}}
```

### lake record — O'Connor v. Ortega

```json
{
  "schema_version": "s2.v1",
  "record_id": "O'Connor v. Ortega",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "O'CONNOR v. Ortega",
    "case_name_short": "O'Connor",
    "case_name_full": "O\u2019CONNOR Et Al. v. ORTEGA",
    "input_case_name": "O'Connor v. Ortega",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-03-31",
    "year": 1987,
    "docket": "85-530",
    "cluster_id": 111851,
    "lead_opinion_id": 9430897,
    "sibling_ids": [
      111851,
      9430897,
      9430898,
      9430899
    ],
    "absolute_url": "/opinion/111851/oconnor-v-ortega/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "480 U.S. 709",
      "volume": "480",
      "reporter": "U.S.",
      "page": "709",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 1492",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 714",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "714",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1 I.E.R. Cas. (BNA) 1617",
        "volume": "1",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "1617",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4405",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4405",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "42 Empl. Prac. Dec. (CCH) 36,891",
        "volume": "42",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "36,891",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 1507",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1507",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "480 U.S. 709",
        "volume": "480",
        "reporter": "U.S.",
        "page": "709",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 1492",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 714",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "714",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 1507",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1507",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1 I.E.R. Cas. (BNA) 1617",
        "volume": "1",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "1617",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4405",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4405",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "42 Empl. Prac. Dec. (CCH) 36,891",
        "volume": "42",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "36,891",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "480 U.S. 709",
    "official_selection": {
      "court_class": "scotus",
      "selected": "480 U.S. 709",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-717",
      "page": null,
      "quote": "--- # O'Connor v. Ortega *480 U.S. 709 (1987)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Dr. Ortega, a physician and administrator at a California state hospital, was placed on administrative leave while officials investigated suspected workplace misconduct (concerning resident-training and the acquisition of a computer). During the investigation, hospital officials entered and searched his office, desk, and file cabinets and seized personal items later used against him in administrative proceedings. Ortega sued under \u00a7 1983, claiming the search violated the Fourth Amendment. ## Issue Whether a public employee has a Fourth Amendment expectation of privacy in his office, desk, and files, and what standard governs a search of those areas by his government employer for work-related purposes. ## Rule Public employees are not stripped of Fourth Amendment protection at work, though their privacy may be reduced by workplace realities.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-725",
      "page": null,
      "quote": "We hold, therefore, that public employer intrusions on the constitutionally protected privacy interests of government employees for noninvestigatory, work-related purposes, as well as for investigations of work-related misconduct, should be judged by the standard of reasonableness under all the circumstances. Under this reasonableness standard, both the inception and the scope of the intrusion must be reasonable.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-03-31",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "O'Connor v. Ortega",
    "varies_by_point": false,
    "scope_note": "Plurality opinion (O'Connor, J.); Scalia concurred in the judgment, supplying a fifth vote for the reasonableness standard, which is controlling. Good law; reaffirmed and applied in City of Ontario v. Quon (2010).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Grady",
          "cluster_id": 4649078,
          "cite": [
            "831 S.E.2d 542",
            "372 N.C. 509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Pirk",
          "cluster_id": 7327733,
          "cite": [
            "282 F. Supp. 3d 585"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hitselberger",
          "cluster_id": 2659423,
          "cite": [
            "991 F. Supp. 2d 108",
            "93 Fed. R. Serv. 1076",
            "2014 WL 842465",
            "2014 U.S. Dist. LEXIS 27792"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Christine Ann Kern",
          "cluster_id": 4472227,
          "cite": [
            "831 N.W.2d 149",
            "2013 WL 2278018",
            "2013 Iowa Sup. LEXIS 61"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Southerland v. City of New York",
          "cluster_id": 8441115,
          "cite": [
            "667 F.3d 87",
            "2012 WL 310836",
            "2011 U.S. App. LEXIS 26144"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jessica Beechum v. State",
          "cluster_id": 3129045,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Martin",
          "cluster_id": 1978636,
          "cite": [
            "2008 VT 53",
            "955 A.2d 1144",
            "184 Vt. 23",
            "2008 Vt. LEXIS 56"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jeffrey Brian Ziegler",
          "cluster_id": 796647,
          "cite": [
            "474 F.3d 1184",
            "2007 U.S. App. LEXIS 1953",
            "2007 WL 222167"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane1_negative"
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
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
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
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. Wisconsin",
          "cluster_id": 111959,
          "cite": [
            "97 L. Ed. 2d 709",
            "107 S. Ct. 3164",
            "483 U.S. 868",
            "1987 U.S. LEXIS 2897",
            "55 U.S.L.W. 5156"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Francis v. Giacomelli",
          "cluster_id": 1030886,
          "cite": [
            "588 F.3d 186",
            "30 I.E.R. Cas. (BNA) 1",
            "2009 U.S. App. LEXIS 26188",
            "107 Fair Empl. Prac. Cas. (BNA) 1605",
            "2009 WL 4348830"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Engquist v. Oregon Department of Agriculture",
          "cluster_id": 145801,
          "cite": [
            "170 L. Ed. 2d 975",
            "128 S. Ct. 2146",
            "553 U.S. 591",
            "2008 U.S. LEXIS 4705",
            "27 I.E.R. Cas. (BNA) 1121",
            "76 U.S.L.W. 4367",
            "21 Fla. L. Weekly Fed. S 302",
            "91 Empl. Prac. Dec. (CCH) 43,213"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
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
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
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
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Villarreal v. State",
          "cluster_id": 2365320,
          "cite": [
            "935 S.W.2d 134",
            "1996 Tex. Crim. App. LEXIS 237",
            "1996 WL 668593"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rutan v. Republican Party of Illinois",
          "cluster_id": 112472,
          "cite": [
            "111 L. Ed. 2d 52",
            "110 S. Ct. 2729",
            "497 U.S. 62",
            "1990 U.S. LEXIS 3298"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Carter",
          "cluster_id": 118249,
          "cite": [
            "142 L. Ed. 2d 373",
            "119 S. Ct. 469",
            "525 U.S. 83",
            "1998 U.S. LEXIS 7844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
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
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
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
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Soldal v. Cook County",
          "cluster_id": 112795,
          "cite": [
            "121 L. Ed. 2d 450",
            "113 S. Ct. 538",
            "506 U.S. 56",
            "1992 U.S. LEXIS 7835",
            "92 Daily Journal DAR 16378",
            "61 U.S.L.W. 4019",
            "6 Fla. L. Weekly Fed. S 769",
            "92 Cal. Daily Op. Serv. 9794"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Burger",
          "cluster_id": 111927,
          "cite": [
            "96 L. Ed. 2d 601",
            "107 S. Ct. 2636",
            "482 U.S. 691",
            "1987 U.S. LEXIS 2725",
            "55 U.S.L.W. 4890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Greenwood",
          "cluster_id": 112067,
          "cite": [
            "100 L. Ed. 2d 30",
            "108 S. Ct. 1625",
            "486 U.S. 35",
            "1988 U.S. LEXIS 2279",
            "56 U.S.L.W. 4409"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jessie Walker v. Thomas E. Darby, Hugh L. Robinson, Jr., and Kenneth Day",
          "cluster_id": 546977,
          "cite": [
            "911 F.2d 1573",
            "5 I.E.R. Cas. (BNA) 1342",
            "1990 U.S. App. LEXIS 16510",
            "1990 WL 126642"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dubbs Ex Rel. Dubbs v. Head Start, Inc.",
          "cluster_id": 163684,
          "cite": [
            "336 F.3d 1194",
            "2003 U.S. App. LEXIS 14578",
            "2003 WL 21690533"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parviz Karim-Panahi v. Los Angeles Police Department",
          "cluster_id": 501771,
          "cite": [
            "839 F.2d 621",
            "10 Fed. R. Serv. 3d 791",
            "1988 U.S. App. LEXIS 1814",
            "46 Fair Empl. Prac. Cas. (BNA) 287"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
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
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tenenbaum v. Williams",
          "cluster_id": 7079141,
          "cite": [
            "193 F.3d 581",
            "1999 WL 822538"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Borough of Duryea v. Guarnieri",
          "cluster_id": 219105,
          "cite": [
            "180 L. Ed. 2d 408",
            "131 S. Ct. 2488",
            "564 U.S. 379",
            "2011 U.S. LEXIS 4564"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brian Sheppard v. Leon Beerman, as an Individual and in His Official Capacity as Justice of the Supreme Court of the State of New York",
          "cluster_id": 664638,
          "cite": [
            "18 F.3d 147",
            "1994 U.S. App. LEXIS 3985"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James G. Jackson v. City of Columbus, Gregory Lashutka, Thomas W. Rice, Sr.",
          "cluster_id": 766509,
          "cite": [
            "194 F.3d 737"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111851 OR 9430897 OR 9430898 OR 9430899) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTAyNjM2ODAwMDAwJnM9Nzg4NjI0JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111851+OR+9430897+OR+9430898+OR+9430899%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 8,
        "triage_snippet_classified": 192
      },
      "lane2_top_cited": {
        "query": "cites:(111851 OR 9430897 OR 9430898 OR 9430899)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTAmcz01NjA3OTU2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111851+OR+9430897+OR+9430898+OR+9430899%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111851 OR 9430897 OR 9430898 OR 9430899)",
        "reviewed": 8,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 8,
        "triage_read": 0,
        "triage_snippet_classified": 8
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111851 OR 9430897 OR 9430898 OR 9430899)",
    "indexed_citing_opinions": 694,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111851,
        "count": 635,
        "count_source": "search"
      },
      {
        "opinion_id": 9430897,
        "count": 73,
        "count_source": "search"
      },
      {
        "opinion_id": 9430898,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430899,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1072,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/o-connor-v-ortega.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc0NjkwMDYmcz01Mjk5Mzc4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111851+OR+9430897+OR+9430898+OR+9430899%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111851,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 106168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 110100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 110917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 111241,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 111788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 227140,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 268915,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 310289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 329742,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 346754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 358050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 359042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 431839,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 437463,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 453433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 1631759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 2005190,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 2263945,
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
    "date_created": "2026-07-05T16:00:58Z",
    "date_modified": "2026-07-06T08:32:27Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:01:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:01:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:05:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:01:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — O'Connor v. Ortega

```
<opinion type="majority">
<author id="b757-8">Justice O’Connor</author>
<p id="Ad0">announced the judgment of the Court and delivered an opinion in which The Chief Justice, Justice White, and Justice Powell join.</p>
<p id="b757-9">This suit under <span class="citation no-link">42 U. S. C. § 1983</span> presents two issues concerning the Fourth Amendment rights of public employees. First, we must determine whether the respondent, a public <page-number citation-index="1" label="712">*712</page-number>employee, had a reasonable expectation of privacy in his office, desk, and file cabinets at his place of work. Second, we must address the appropriate Fourth Amendment standard for a search conducted by a public employer in areas in which a public employee is found to have a reasonable expectation of privacy.</p>
<p id="b758-5">I</p>
<p id="b758-6">Dr. Magno Ortega, a physician and psychiatrist, held the position of Chief of Professional Education at Napa State Hospital (Hospital) for 17 years, until his dismissal from that position in 1981. As Chief of Professional Education, Dr.. Ortega had primary responsibility for training young physicians in psychiatric residency programs.</p>
<p id="b758-7">In July 1981, Hospital officials, including Dr. Dennis O’Connor, the Executive Director of the Hospital, became concerned about possible improprieties in Dr. Ortega’s management of the residency program. In particular, the Hospital officials were concerned with Dr. Ortega’s acquisition of an Apple II computer for use in the residency program. The officials thought that Dr. Ortega may have misled Dr. O’Con-nor into believing that the computer had been donated, when in fact the computer had been financed by the possibly coerced contributions of residents. Additionally, the Hospital officials were concerned with charges that Dr. Ortega had sexually harassed two female Hospital employees, and had taken inappropriate disciplinary action against a resident.</p>
<p id="b758-8">On July 30, 1981, Dr. O’Connor requested that Dr. Ortega take paid administrative leave during an investigation of these charges. At Dr. Ortega’s request, Dr. O’Connor agreed to allow Dr. Ortega to take two weeks’ vacation instead of administrative leave. Dr. Ortega, however, was requested to stay off Hospital grounds for the duration of the investigation. On August 14, 1981, Dr. O’Connor informed Dr. Ortega that the investigation had not yet been completed, and that he was being placed on paid administrative leave. Dr. Ortega remained on administrative leave until <page-number citation-index="1" label="713">*713</page-number>the Hospital terminated his employment on September 22, 1981.</p>
<p id="b759-5">Dr. O’Connor selected several Hospital personnel to conduct the investigation, including an accountant, a physician, and a Hospital security officer. Richard Friday, the Hospital Administrator, led this “investigative team.” At some point during the investigation, Mr. Friday made the decision to enter Dr. Ortega’s office. The specific reason for the entry into Dr. Ortega’s office is unclear from the record. The petitioners claim that the search was conducted to secure state property. Initially, petitioners contended that such a search was pursuant to a Hospital policy of conducting a routine inventory of state property in the office of a terminated employee. At the time of the search, however, the Hospital had not yet terminated Dr. Ortega’s employment; Dr. Ortega was still on administrative leave. Apparently, there was no policy of inventorying the offices of those on administrative leave. Before the search had been initiated, however, petitioners had become aware that Dr. Ortega had taken the computer to his home. Dr. Ortega contends that the purpose of the search was to secure evidence for use against him in administrative disciplinary proceedings.</p>
<p id="b759-6">The resulting search of Dr. Ortega’s office was quite thorough. The investigators entered the office a number of times and seized several items from Dr. Ortega’s desk and file cabinets, including a Valentine’s Day card, a photograph, and a book of poetry all sent to Dr. Ortega by a former resident physician. These items were later used in a proceeding before a hearing officer of the California State Personnel Board to impeach the credibility of the former resident, who testified on Dr. Ortega’s behalf. The investigators also seized billing documentation of one of Dr. Ortega’s private patients under the California Medicaid program. The investigators did not otherwise separate Dr. Ortega’s property from state property because, as one investigator testified, “[tjrying to sort State from non-State, it was too much to do, so I gave it <page-number citation-index="1" label="714">*714</page-number>up and boxed it up.” App. 62. Thus, no formal inventory of the property in the office was ever made. Instead, all the papers in Dr. Ortega’s office were merely placed in boxes, and put in storage for Dr. Ortega to retrieve.</p>
<p id="b760-5">Dr. Ortega commenced this action against petitioners in Federal District Court under <span class="citation no-link">42 U. S. C. § 1988</span>, alleging that the search of his office violated the Fourth Amendment. On cross-motions for summary judgment, the District Court granted petitioners’ motion for summary judgment. The District Court, relying on <em>Chenkin </em>v. <em>Bellevue Hospital Center, New York City Health &amp; Hospitals Corp., </em><span class="citation" data-id="2263945"><a href="/opinion/2263945/chenkin-v-bellevue-hosp-ctr-nyc-etc/" aria-description="Citation for case: Chenkin v. BELLEVUE HOSP. CTR., NYC, ETC.">479 F. Supp. 207</a></span> (SDNY 1979), concluded that the search was proper because there was a need to secure state property in the office. The Court of Appeals for the Ninth Circuit affirmed in part and reversed in part, <span class="citation multiple-matches"><a href="/c/F.%202d/764/703/">764 F. 2d 703</a></span> (1985), concluding that Dr. Ortega had a reasonable expectation of privacy in his office. While the Hospital had a procedure for office inventories, these inventories were reserved for employees who were departing or were terminated. The Court of Appeals also concluded — albeit without explanation — that the search violated the Fourth Amendment. The Court of Appeals held that the record justified a grant of partial summary judgment for Dr. Ortega on the issue of liability for an unlawful search, and it remanded the case to the District Court for a determination of damages.</p>
<p id="b760-6">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./474/1018/">474 U. S. 1018</a></span> (1985), and now reverse and remand.</p>
<p id="b760-8">h — I l-H</p>
<p id="b760-7">The strictures of the Fourth Amendment, applied to the States through the Fourteenth Amendment, have been applied to the conduct of governmental officials in various civil activities. <em>New Jersey </em>v. <em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#334" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 334-335</a></span> (1985). Thus, we have held in the past that the Fourth Amendment governs the conduct of school officials, see <em>ibid., </em>building inspectors, see <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span> (1967), and Occupational Safety and Health <page-number citation-index="1" label="715">*715</page-number>Act inspectors, see <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#312" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 312-313</a></span> (1978). As we observed in <em>T. L. 0., </em>“[b]ecause the individual’s interest in privacy and personal security ‘suffers whether the government’s motivation is to investigate violations of criminal laws or breaches of other statutory or regulatory standards,’... it would be ‘anomalous to say that the individual and his private property are fully protected by the Fourth Amendment only when the individual is suspected of criminal behavior.’” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 335</a></span> (quoting <em>Marshall </em>v. <em>Barlow’s, <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">Inc., supra,</a></span> </em>at 312-313 and <em>Camara </em>v. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#530" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><em>Municipal Court, supra, </em>at 530</a></span>). Searches and seizures by government employers or supervisors of the private property of their employees, therefore, are subject to the restraints of the Fourth Amendment.</p>
<p id="b761-5">The Fourth Amendment protects the “right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures . . . .” Our cases establish that Dr. Ortega’s Fourth Amendment rights are implicated only if the conduct of the Hospital officials at issue in this case infringed “an expectation of privacy that society is prepared to consider reasonable.” <em>United States </em>v. <em>Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 113</a></span> (1984). We have no talisman that determines in all cases those privacy expectations that society is prepared to accept as reasonable. Instead, “the Court has given weight to such factors as the intention of the Framers of the Fourth Amendment, the uses to which the individual has put a location, and our societal understanding that certain areas deserve the most scrupulous protection from government invasion.” <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#178" aria-description="Citation for case: Oliver v. United States">466 U. S. 170, 178</a></span> (1984) (citations omitted).</p>
<p id="b761-6">Because the reasonableness of an expectation of privacy, as well as the appropriate standard for a search, is understood to differ according to context, it is essential first to delineate the boundaries of the workplace context. The workplace includes those areas and items that are related to work and are generally within the employer’s control. At a hospital, for <page-number citation-index="1" label="716">*716</page-number>example, the hallways, cafeteria, offices, desks, and file cabinets, among other areas, are all part of the workplace. These areas remain part of the workplace context even if the employee has placed personal items in them, such as a photograph placed in a desk or a letter posted on an employee bulletin board.</p>
<p id="b762-5">Not everything that passes through the confines of the business address can be considered part of the workplace context, however. An employee may bring closed luggage to the office prior to leaving on a trip, or a handbag or briefcase each workday. While whatever expectation of privacy the employee has in the existence and the outward appearance of the luggage is affected by its presence in the workplace, the employee’s expectation of privacy in the <em>contents </em>of the luggage is not affected in the same way. The appropriate standard for a workplace search does not necessarily apply to a piece of closed personal luggage, a handbag, or a briefcase that happens to be within the employer’s business address.</p>
<p id="b762-6">Within the workplace context, this Court has recognized that employees may have a reasonable expectation of privacy against intrusions by police. See <em>Mancusi </em>v. <em>DeForte, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364</a></span> (1968). As with the expectation of privacy in one’s home, such an expectation in one’s place of work is “based upon societal expectations that have deep roots in the history of the Amendment.” <em>Oliver </em>v. <em>United States, supra, </em>at 178, n. 8. Thus, in <em>Mancusi </em>v. <em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">DeForte, supra,</a></span> </em>the Court held that a union employee who shared an office with other union employees had a privacy interest in the office sufficient to challenge successfully the warrantless search of that office:</p>
<blockquote id="b762-7">“It has long been settled that one has standing to object to a search of his office, as well as of his home. . . . [I]t seems clear that if DeForte had occupied a ‘private’ office in the union headquarters, and union records had been seized from a desk or a filing cabinet in that office, he would have had standing. ... In such a ‘private’ of<page-number citation-index="1" label="717">*717</page-number>fice, DeForte would have been entitled to expect that he would not be disturbed except by personal or business invitees, and that records would not be taken except with his permission or that of his union superiors.” <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#369" aria-description="Citation for case: Mancusi v. DeForte">392 U. S., at 369</a></span>.</blockquote>
<p id="b763-5">Given the societal expectations of privacy in one’s place of work expressed in both <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver</a></span> </em>and <em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">Mancusi</a></span>, </em>we reject the contention made by the Solicitor General and petitioners that public employees can never have a reasonable expectation of privacy in their place of work. Individuals do not lose Fourth Amendment rights merely because they work for the government instead of a private employer. The operational realities of the workplace, however, may make <em>some </em>employees’ expectations of privacy unreasonable when an intrusion is by a supervisor rather than a law enforcement official. Public employees’ expectations of privacy in their offices, desks, and file cabinets, like similar expectations of employees in the private sector, may be reduced by virtue of actual office practices and procedures, or by legitimate regulation. Indeed, in <em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">Mancusi</a></span> </em>itself, the Court suggested that the union employee did not have a reasonable expectation of privacy against his union supervisors. <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#369" aria-description="Citation for case: Mancusi v. DeForte">392 U. S., at 369</a></span>. The employee’s expectation of privacy must be assessed in the context of the employment relation. An office is seldom a private enclave free from entry by supervisors, other employees, and business and personal invitees. Instead, in many cases offices are continually entered by fellow employees and other visitors during the workday for conferences, consultations, and other work-related visits. Simply put, it is the nature of government offices that others — such as fellow employees, supervisors, consensual visitors, and the general public — may have frequent access to an individual’s office. We agree with Justice Scalia that “[cjonstitutional protection against <em>unreasonable </em>searches by the government does not disappear merely because the government has the right to make reasonable. intrusions in its capacity as em<page-number citation-index="1" label="718">*718</page-number>ployer,” <em>post, </em>at 731, but some government offices may be so open to fellow employees or the public that no expectation of privacy is reasonable. Cf. <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967) (“What a person knowingly exposes to the public, even in his own home or office, is not a subject of Fourth Amendment protection”). Given the great variety of work environments in the public sector, the question whether an employee has a reasonable expectation of privacy must be addressed on a case-by-case basis.</p>
<p id="b764-5">The Court of Appeals concluded that Dr. Ortega had a reasonable expectation of privacy in his office, and five Members of this Court agree with that determination. See <em>post, </em>at 731-732 (Scalia, J., concurring in judgment); <em>post, </em>at 732 (Blackmun, J., joined by Brennan, Marshall, and Stevens, JJ., dissenting). Because the record does not reveal the extent to which Hospital officials may have had work-related reasons to enter Dr. Ortega’s office, we think the Court of Appeals should have remanded the matter to the District Court for its further determination. But regardless of any legitimate right of access the Hospital staff may have had to the office as such, we recognize that the undisputed evidence suggests that Dr. Ortega had a reasonable expectation of privacy in his desk and file cabinets. The undisputed evidence discloses that Dr. Ortega did not share his desk or file cabinets with any other employees. Dr. Ortega had occupied the office for 17 years and he kept materials in his office, which included personal correspondence, medical files, correspondence from private patients unconnected to the Hospital, personal financial records, teaching aids and notes, and personal gifts and mementos. App. 14. The files on physicians in residency training were kept outside Dr. Ortega’s office. <em>Id., </em>at 21. Indeed, the only items found by the investigators were apparently personal items because, with the exception of the items seized for use in the administrative hearings, all the papers and effects found in the office were simply placed in boxes and made available to Dr. Ortega. <page-number citation-index="1" label="719">*719</page-number><em>Id., </em>at 58, 62. Finally, we note that there was no evidence that the Hospital had established any reasonable regulation or policy discouraging employees such as Dr. Ortega from storing personal papers and effects in their desks or file cabinets, id., at 44, although the absence of such a policy does not create an expectation of privacy where it would not otherwise exist.</p>
<p id="b765-5">On the basis of this undisputed evidence, we accept the conclusion of the Court of Appeals that Dr. Ortega had a reasonable expectation of privacy at least in his desk and file cabinets. See <em>Gillard </em>v. <em>Schmidt, </em><span class="citation" data-id="358050"><a href="/opinion/358050/francis-d-gillard-v-harold-f-schmidt/#829" aria-description="Citation for case: Francis D. Gillard v. Harold F. Schmidt">579 F. 2d 825, 829</a></span> (CA3 1978); <em>United States </em>v. <em>Speights, </em><span class="citation" data-id="346754"><a href="/opinion/346754/united-states-v-ronald-miller-speights/" aria-description="Citation for case: United States v. Ronald Miller Speights">557 F. 2d 362</a></span> (CA3-4977); <em>United States </em>v. <em>Blok, </em>88 U. S. App. D. C. 326, <span class="citation" data-id="227140"><a href="/opinion/227140/united-states-v-blok/" aria-description="Citation for case: United States v. Blok">188 F. 2d 1019</a></span> (1951).</p>
<p id="b765-6">Ill</p>
<p id="b765-7">Having determined that Dr. Ortega had a reasonable expectation of privacy in his office, the Court of Appeals simply concluded without discussion that the “search . . . was not a reasonable search under the fourth amendment.” 764 F. 2d, at 707. But as we have stated in <em>T. L. 0., </em>“[t]o hold that the Fourth Amendment applies to searches conducted by [public employers] is only to begin the inquiry into the standards governing such searches. . . . [W]hat is reasonable depends on the context within which a search takes place.” <em>New Jersey </em>v. <em>T. L. 0., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#337" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 337</a></span>. Thus, we must determine the appropriate standard of reasonableness applicable to the search. A determination of the standard of reasonableness applicable to a particular class of searches requires “balancing] the nature and quality of the intrusion on the individual’s Fourth Amendment interests against the importance of the governmental interests alleged to justify the intrusion.” <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place">462 U. S. 696, 703</a></span> (1983); <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#536" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 536-537</a></span>. In the case of searches conducted by a public employer, we must balance the invasion of the employees’ legitimate expectations of pri<page-number citation-index="1" label="720">*720</page-number>vacy against the government’s need for supervision, control, and the efficient operation of the workplace.</p>
<p id="b766-5">“[I]t is settled . . . that ‘except in certain carefully defined classes of cases, a search of private property without proper consent is “unreasonable” unless it has been authorized by a valid search warrant.’” <em>Mancusi </em>v. <em>DeForte, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U. S., at 370</a></span> (quoting <em>Camara </em>v. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><em>Municipal Court, supra, </em>at 528-529</a></span>). There are some circumstances, however, in which we have recognized that a warrant requirement is unsuitable. In particular, a warrant requirement is not appropriate when “the burden of obtaining a warrant is likely to frustrate the governmental purpose behind the search.” <em>Camara </em>v. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#533" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><em>Municipal Court, supra, </em>at 533</a></span>. Or, as Justice Blackmun stated in <em>T. L. 0., </em>“[o]nly in those exceptional circumstances in which special needs, beyond the normal need for law enforcement, make the warrant and probable-cause requirement impracticable.” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#351" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 351</a></span> (concurring in judgment). In <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307</a></span> (1978), for example, the Court explored the burdens a warrant requirement would impose on the Occupational Safety and Health Act regulatory scheme, and held that the warrant requirement was appropriate only after concluding that warrants would not “impose serious burdens on the inspection system or the courts, [would not] prevent inspections necessary to enforce the statute, or [would not] make them less effective.” <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#316" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 316</a></span>. In <em>New Jersey </em>v. <em>T. L. O., supra, </em>we concluded that the warrant requirement was not suitable to the school environment, because such a requirement would unduly interfere with the maintenance of the swift and informal disciplinary procedures needed in the schools.</p>
<p id="b766-6">There is surprisingly little case law on the appropriate Fourth Amendment standard of reasonableness for a public employer’s work-related search of its employee’s offices, desks, or file cabinets. Generally, however, the lower courts have held that any “work-related” search by an em<page-number citation-index="1" label="721">*721</page-number>ployer satisfies the Fourth Amendment reasonableness requirement. See <em>United States </em>v. <em>Nasser6, </em><span class="citation" data-id="9459389"><a href="/opinion/310289/united-states-v-arthur-nasser-united-states-of-america-v-richard-w/#1123" aria-description="Citation for case: United States v. Arthur Nasser, United States of America...">476 F. 2d 1111, 1123</a></span> (CA7 1973) (“work-related” searches and seizures are reasonable under the Fourth Amendment); <em>United States </em>v. <em>Collins, </em><span class="citation" data-id="268915"><a href="/opinion/268915/united-states-v-madell-collins/#868" aria-description="Citation for case: United States v. Madell Collins">349 F. 2d 863, 868</a></span> (CA2 1965) (upholding search and seizure because conducted pursuant to “the power of the Government as defendant’s employer, to supervise and investigate the performance of his duties as a Customs employee”). Others have suggested the use of a standard other than probable cause. See <em>United States </em>v. <em>Bunkers, </em><span class="citation" data-id="329742"><a href="/opinion/329742/united-states-v-jennieve-rose-bunkers/" aria-description="Citation for case: United States v. Jennieve Rose Bunkers">521 F. 2d 1217</a></span> (CA9 1975) (work-related search of a locker tested under “reasonable cause” standard); <em>United States </em>v. <span class="citation" data-id="227140"><a href="/opinion/227140/united-states-v-blok/#328" aria-description="Citation for case: United States v. Blok"><em>Blok, supra, </em>at 328</a></span>, <span class="citation" data-id="227140"><a href="/opinion/227140/united-states-v-blok/#1021" aria-description="Citation for case: United States v. Blok">188 F. 2d, at 1021</a></span> (“No doubt a search of [a desk] without her consent would have been reasonable if made by some people in some circumstances. Her official superiors might reasonably have searched the desk for official property needed for official use”). The only cases to imply that a warrant should be required involve searches that are not work related, see <em>Gillard </em>v. <span class="citation" data-id="358050"><a href="/opinion/358050/francis-d-gillard-v-harold-f-schmidt/#829" aria-description="Citation for case: Francis D. Gillard v. Harold F. Schmidt"><em>Schmidt, supra, </em>at 829, n. 1</a></span>, or searches for evidence of criminal misconduct, see <em>United States </em>v. <em>Kahan, </em><span class="citation" data-id="2005190"><a href="/opinion/2005190/united-states-v-kahan/" aria-description="Citation for case: United States v. Kahan">350 F. Supp. 784</a></span> (SDNY 1972).</p>
<p id="b767-5">The legitimate privacy interests of public employees in the private objects they bring to the workplace may be substantial. Against these privacy interests, however, must be balanced the realities of the workplace, which strongly suggest that a warrant requirement would be unworkable. While police, and even administrative enforcement personnel, conduct searches for the primary purpose of obtaining evidence for use in criminal or other enforcement proceedings, employers most frequently need to enter the offices and desks of their employees for legitimate work-related reasons wholly unrelated to illegal conduct. Employers and supervisors are focused primarily on the need to complete the government agency’s work in a prompt and efficient manner. An employer may have need for correspondence, or a file or report available only in an employee’s office while the employee is <page-number citation-index="1" label="722">*722</page-number>away from the office. Or, as is alleged to have been the case here, employers may need to safeguard or identify state property or records in an office in connection with a pending investigation into suspected employee misfeasance.</p>
<p id="b768-5">In our view, requiring an employer to obtain a warrant whenever the employer wished to enter an employee’s office, desk, or file cabinets for a work-related purpose would seriously disrupt the routine conduct of business and would be unduly burdensome. Imposing unwieldy warrant procedures in such cases upon supervisors, who would otherwise have no reason to be familiar with such procedures, is simply unreasonable. In contrast to other circumstances in which we have required warrants, supervisors in offices such as at the Hospital are hardly in the business of investigating the violation of criminal laws. Rather, work-related searches are merely incident to the primary business of the agency. Under these circumstances, the imposition of a warrant requirement would conflict with “the common-sense realization that government offices could not function if every employment decision became a constitutional matter.” <em>Connick </em>v. <em>Myers, </em><span class="citation" data-id="9429164"><a href="/opinion/110917/connick-ex-rel-parish-of-orleans-v-myers/#143" aria-description="Citation for case: Connick Ex Rel. Parish of Orleans v. Myers">461 U. S. 138, 143</a></span> (1983).</p>
<p id="b768-6">Whether probable cause is an inappropriate standard for public employer searches of their employees’ offices presents a more difficult issue. For the most part, we have required that a search be based upon probable cause, but as we noted in <em>New Jersey </em>v. <em>T. L. O., </em>“[t]he fundamental command of the Fourth Amendment is that searches and seizures be reasonable, and although ‘both the concept of probable cause and the requirement of a warrant bear on the reasonableness of a search, ... in certain limited circumstances neither is required.’” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 340</a></span> (quoting <em>Almeida-Sanchez </em>v. <em>United States, </em><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#277" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 277</a></span> (1973) (Powell, J., concurring)). Thus, “[w]here a careful balancing of governmental and private interests suggests that the public interest is best served by a Fourth Amendment standard of reasonableness that stops short of probable cause, we have not hesitated to <page-number citation-index="1" label="723">*723</page-number>adopt such a standard.” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#341" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 341</a></span>. We have concluded, for example, that the appropriate standard for administrative searches is not probable cause in its traditional meaning. Instead, an administrative warrant can be obtained if there is a showing that reasonable legislative or administrative standards for conducting an inspection are satisfied. See <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#320" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 320</a></span>; <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#538" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 538</a></span>.</p>
<p id="b769-4">As an initial matter, it is important to recognize the plethora of contexts in which employers will have an occasion to intrude to some extent on an employee’s expectation of privacy. Because the parties in this case have alleged that the search was either a noninvestigatory work-related intrusion or an investigatory search for evidence of suspected work-related employee misfeasance, we undertake to determine the appropriate Fourth Amendment standard of reasonableness <em>only </em>for these two types of employer intrusions and leave for another day inquiry into other circumstances.</p>
<p id="b769-5">The governmental interest justifying work-related intrusions by public employers is the efficient and proper operation of the workplace. Government agencies provide myriad services to the public, and the work of these agencies would suffer if employers were required to have probable cause before they entered an employee’s desk for the purpose of finding a file or piece of office correspondence. Indeed, it is difficult to give the concept of probable cause, rooted as it is in the criminal investigatory context, much meaning when the purpose of a search is to retrieve a file for work-related reasons. Similarly, the concept of probable cause has little meaning for a routine inventory conducted by public employers for the purpose of securing state property. See <em>Colorado </em>v. <em>Bertine, </em><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">479 U. S. 367</a></span> (1987); <em>Illinois </em>v. <em>Lafayette, </em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">462 U. S. 640</a></span> (1983). To ensure the efficient and proper operation of the agency, therefore, public employers must be given wide latitude to enter employee offices for work-related, noninvestigatory reasons.</p>
<p id="b770-4"><page-number citation-index="1" label="724">*724</page-number>We come to a similar conclusion for searches conducted pursuant to an investigation of work-related employee misconduct. Even when employers conduct an investigation, they have an interest substantially different from “the normal need for law enforcement.” <em>New Jersey </em>v. <em>T. L. O., supra, </em>at 351 (Blackmun, J., concurring in judgment). Public employers have an interest in ensuring that their agencies operate in an effective and efficient manner, and the work of these agencies inevitably suffers from the inefficiency, incompetence, mismanagement, or other work-related misfeasance of its employees. Indeed, in many cases, public employees are entrusted with tremendous responsibility, and the consequences of their misconduct or incompetence to both the agency and the public interest can be severe. In contrast to law enforcement officials, therefore, public employers are not enforcers of the criminal law; instead, public employers have a direct and overriding interest in ensuring that the work of the agency is conducted in a proper and efficient manner. In our view, therefore, a probable cause requirement for searches of the type at issue here would impose intolerable burdens on public employers. The delay in correcting the employee misconduct caused by the need for probable cause rather than reasonable suspicion will be translated into tangible and often irreparable damage to the agency’s work, and ultimately to the public interest. See <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#353" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 353</a></span> (“The time required for a teacher to ask the questions or make the observations that are necessary to turn reasonable grounds into probable cause is time during which the teacher, and other students, are diverted from the essential task of education”). Additionally, while law enforcement officials are expected to “schoo[l] themselves in the niceties of probable cause,” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#343" aria-description="Citation for case: New Jersey v. T. L. O."><em>id., </em>at 343</a></span>, no such expectation is generally applicable to public employers, at least when the search is not used to gather evidence of a criminal offense. It is simply unrealistic to expect supervisors in most government agencies to learn the subtleties of <page-number citation-index="1" label="725">*725</page-number>the probable cause standard. As Justice Blackmun observed in <em>T. L. 0., </em>“[a] teacher has neither the training nor the day-to-day experience in the complexities of probable cause that a law enforcement officer possesses, and is ill-equipped to make a quick judgment about the existence of probable cause.” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#353" aria-description="Citation for case: New Jersey v. T. L. O."><em>Id., </em>at 353</a></span>. We believe that this observation is an equally apt description of the public employer and supervisors at the Hospital, and we conclude that a reasonableness standard will permit regulation of the employer’s conduct “according to the dictates of reason and common sense.” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#343" aria-description="Citation for case: New Jersey v. T. L. O."><em>Id., </em>at 343</a></span>.</p>
<p id="b771-5">Balanced against the substantial government interests in the efficient and proper operation of the workplace are the privacy interests of government employees in their place of work which, while not insubstantial, are far less than those found at home or in some other contexts. As with the building inspections in <em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span>, </em>the employer intrusions at issue here “involve a relatively limited invasion” of employee privacy. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#537" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 537</a></span>. Government offices are provided to employees for the sole purpose of facilitating the work of an agency. The employee may avoid exposing personal belongings at work by simply leaving them at home.</p>
<p id="b771-6">In sum, we conclude that the “special needs, beyond the normal need for law enforcement make the . . . probable-cause requirement impracticable,” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#351" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 351</a></span> (Black-mun, J., concurring in judgment), for legitimate work-related, noninvestigatory intrusions as well as investigations of work-related misconduct. A standard of reasonableness will neither unduly burden the efforts of government employers to ensure the efficient and proper operation of the workplace, nor authorize arbitrary intrusions upon the privacy of public employees. We hold, therefore, that public employer intrusions on the constitutionally protected privacy interests of government employees for noninvestigatory, work-related purposes, as well as for investigations of work-related misconduct, should be judged by the standard of reasonableness <page-number citation-index="1" label="726">*726</page-number>under all the circumstances. Under this reasonableness standard, both the inception and the scope of the intrusion must be reasonable:</p>
<blockquote id="b772-6">“Determining the reasonableness of any search involves a twofold inquiry: first, one must consider ‘whether the . . . action was justified at its inception,’ <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#20" aria-description="Citation for case: Mancusi v. DeForte">392 U. S., at 20</a></span>; second, one must determine whether ■ the search as actually conducted ‘was reasonably related in scope to the circumstances which justified the interference in the first place,’ <em>ibid.” New Jersey </em>v. <em>T. L. O., supra, </em>at 341.</blockquote>
<p id="b772-7">Ordinarily, a search of an employee’s office by a supervisor will be “justified at its inception” when there are reasonable grounds for suspecting that the search will turn up evidence that the employee is guilty of work-related misconduct, or that the search is necessary for a noninvestigatory work-related purpose such as to retrieve a needed file. Because petitioners had an “individualized suspicion” of misconduct by Dr. Ortega, we need not decide whether individualized suspicion is an essential element of the standard of reasonableness that we adopt today. See <em>New Jersey </em>v. <em>T. L. O., supra, </em>at 342, n. 8. The search will be permissible in its scope when “the measures adopted are reasonably related to the objectives of the search and not excessively intrusive in light of . . . the nature of the [misconduct].” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#342" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 342</a></span>.</p>
<p id="b772-8">&lt;1</p>
<p id="b772-3">In the procedural posture of this case, we do not attempt to determine whether the search of Dr. Ortega’s office and the seizure of his personal belongings satisfy the standard of reasonableness we have articulated in this case. No eviden-tiary hearing was held in this case because the District Court acted on cross-motions for summary judgment, and granted petitioners summary judgment. The Court of Appeals, on the other hand, concluded that the record in this case justi-<page-number citation-index="1" label="727">*727</page-number>fled granting partial summary judgment on liability to Dr. Ortega.</p>
<p id="b773-5">We believe that both the District Court and the Court of Appeals were in error because summary judgment was inappropriate. The parties were in dispute about the actual justification for the search, and the record was inadequate for a determination on motion for summary judgment of the reasonableness of the search and seizure. Petitioners have consistently attempted to justify the search and seizure as required to secure the state property in Dr. Ortega’s office. Mr. Friday testified in a deposition that he had ordered members of the investigative team to “check Dr. Ortega’s office out in order to separate the business files from any personal files in order to ascertain what was in his office.” App. 50. He further testified that the search was initiated because he “wanted to make sure that we had our state property identified, and in order to provide Dr. Ortega with his property and get what we had out of there, in order to make sure our resident’s files were protected, and that sort of stuff.” <em>Id., </em>at 51.</p>
<p id="b773-6">In their motion for summary judgment in the District Court, petitioners alleged that this search to secure property was reasonable as “part of the established hospital policy to inventory property within offices of departing, terminated or separated employees.” Record Doc. No. 24, p. 9. The District Court apparently accepted this characterization of the search because it applied <em>Chenkin </em>v. <em>Bellevue Hospital Center, New York City Health &amp; Hospitals Corp., </em><span class="citation" data-id="2263945"><a href="/opinion/2263945/chenkin-v-bellevue-hosp-ctr-nyc-etc/" aria-description="Citation for case: Chenkin v. BELLEVUE HOSP. CTR., NYC, ETC.">479 F. Supp. 207</a></span> (SDNY 1979), a case involving a Fourth Amendment challenge to an inspection <em>policy. </em>At the time of the search, however, Dr. Ortega had not been terminated, but rather was still on administrative leave, and the record does not reflect whether the Hospital had a policy of inventorying the property of investigated employees. Respondent, moreover, has consistently rejected petitioners’ characterization of the search as motivated by a need to secure state property. <page-number citation-index="1" label="728">*728</page-number>Instead, Dr. Ortega has contended that the intrusion was an investigatory search whose purpose was simply to discover evidence that would be of use in administrative proceedings. He has pointed to the fact that no inventory was ever taken of the property in the office, and that seized evidence was eventually used in the administrative proceedings. Additionally, Dr. O’Connor stated in a deposition that one purpose of the search was “to look for contractural <em>[sic] </em>and other kinds of documents that might have been related to the issues” involved in the investigation. App. 38.</p>
<p id="b774-5">Under these circumstances, the District Court was in error in granting petitioners summary judgment. There was a dispute of fact about the character of the search, and the District Court acted under the erroneous assumption that thq search was conducted pursuant to a Hospital policy. Moreover, no findings were made as to the scope of the search that was undertaken.</p>
<p id="b774-6">The Court of Appeals concluded that Dr. Ortega was entitled to partial summary judgment on liability. It noted that the Hospital had no policy of inventorying the property of employees on administrative leave, but it did not consider whether the search was otherwise reasonable. Under the standard of reasonableness articulated in this case, however, the absence of a Hospital policy did not necessarily make the search unlawful. A search to secure state property is valid as long as petitioners had a reasonable belief that there was government property in Dr. Ortega’s office which needed to be secured, and the scope of the intrusion was itself reasonable in light of this justification. Indeed, petitioners have put forward evidence that they had such a reasonable belief; at the time of the search, petitioners knew that Dr. Ortega had removed the computer from the Hospital. The removal of the computer — together with the allegations of mismanagement of the residency program and sexual harassment— may have made the search reasonable at its inception under the standard we have put forth in this case. As with the <page-number citation-index="1" label="729">*729</page-number>District Court order, therefore, the Court of Appeals conclusion that summary judgment was appropriate cannot stand.</p>
<p id="b775-5">On remand, therefore, the District Court must determine the justification for the search and seizure, and evaluate the reasonableness of both the inception of the search and its scope.<footnotemark>*</footnotemark></p>
<p id="b775-6">Accordingly, the judgment of the Court of Appeals is reversed, and the case is remanded to that court for further proceedings consistent with this opinion.</p>
<p id="b775-7">
<em>It is so ordered.</em>
</p>
<footnote label="*">
<p id="b775-11">We have no occasion in this case to reach the issue of the appropriate standard for the evaluation of the Fourth Amendment reasonableness of the seizure of Dr. Ortega’s personal items. Neither the District Court nor the Court of Appeals addressed this issue, and the <em>amicus curiae </em>brief filed on behalf of respondent did not discuss the legality of the seizure separate from that of the search. We also have no occasion in this case to address whether qualified immunity should protect petitioners from damages liability under § 1983. See <em>Davis </em>v. <em>Scherer, </em><span class="citation" data-id="9429708"><a href="/opinion/111241/davis-v-scherer/" aria-description="Citation for case: Davis v. Scherer">468 U. S. 183</a></span> (1984); <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800</a></span> (1982). The qualified immunity issue was not raised below and was not addressed by either the District Court or the Court of Appeals. Nor do we address the proper Fourth Amendment analysis for drug and alcohol testing of employees. Finally, we do not address the appropriate standard when an employee is being investigated for criminal misconduct or breaches of other nonwork-related statutory or regulatory standards.</p>
</footnote>
</opinion>
```

---
