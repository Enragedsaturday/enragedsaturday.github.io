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

## GROUP: content/cases/LaDuke v. Nelson.md  (`case`, 5 assertions)

### content_page

```
---
title: LaDuke v. Nelson
type: case
citation: "762 F.2d 1318 (1985)"
parallel_cite: 53 U.S.L.W. 2625
neutral_cite: 1985 U.S. App. LEXIS 19963
court: 9th Cir.
court_level: coa
circuit: ca9
year: 1985
date_decided: 1985-06-10
docket: 83-3608
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
  opinion_url: "https://www.courtlistener.com/opinion/452994/charles-laduke-v-alan-c-nelson-etc/"
  cluster_id: 452994
  opinion_id: null
  identity_checked: true
lake:
  record_id: LaDuke v. Nelson
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Tents]]"
    role: Key
related:
  - "[[Tents]]"
tags:
  - case
  - fourth-amendment
  - curtilage
  - dwelling
  - migrant-housing
  - warrantless-entry
  - injunction
holding: "Migrant farmworkers' dwellings retain their occupants' reasonable expectations of privacy, so the INS may not conduct warrantless 'area control' entries of farm housing to search or arrest absent consent or probable cause; the Ninth Circuit affirmed a class injunction barring the practice as a Fourth Amendment violation."
---

# LaDuke v. Nelson

*762 F.2d 1318 (9th Cir. 1985)* (No. 83-3608) · U.S. Court of Appeals for the Ninth Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 452994 → opinion 452994 (762 F.2d 1318, decided 1985-06-10); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
A class of migrant and seasonal farmworkers in Washington's Spokane Sector challenged the Immigration and Naturalization Service's "area control operations" — sweeps in which agents entered farm labor camps and the workers' dwellings, and stopped and interrogated residents, without warrants or individualized suspicion. The district court found the practices unconstitutional and issued a class-wide injunction; the INS appealed, contesting standing, the seizure findings, and the scope of the injunction.

## Issue
Whether the INS's warrantless entries into migrant farmworker dwellings and its suspicionless detentive stops of residents violate the Fourth Amendment, and whether the district court's injunction was proper.

## Rule
The Ninth Circuit affirmed. It held that the humble, often temporary dwellings of migrant farmworkers are fully protected by the Fourth Amendment and that the injunction's first component — barring warrantless entries of farm dwellings to search or arrest absent clear consent or probable cause — was sound: "we think the plain language of the first component provides ample flexibility for INS searches while preserving class members' reasonable expectations of privacy." — 762 F.2d at 1331. The court agreed that the INS "farm checks, as described by the witnesses, run afoul of the Fourth Amendment." — *Id.* at 1332.

## Application
The injunction had three parts: no warrantless entries of farm dwellings to search or arrest absent consent or probable cause; no warrantless arrests or searches of residents without probable cause; and no detentive stops without articulable suspicion of both alienage and unlawful presence. The court sustained each, rejecting the INS's overbreadth arguments and stressing that the modest character of migrant housing does not diminish its occupants' constitutional protection; the injunction still left ample room for consensual encounters and legitimate, warrant-based enforcement.

## Conclusion
The judgment and injunction were **affirmed** (with a modification to the fee award); the INS's area-control entries and suspicionless stops violated the Fourth Amendment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *LaDuke* stands for the proposition that a dwelling's protection does not depend on its permanence or grandeur: temporary and makeshift homes — farmworker cabins, shacks, and tents — remain within the Fourth Amendment's shelter against warrantless government entry.

## Appears on
- [[Tents]] — *Key*

## Sources
- [*LaDuke v. Nelson*, 762 F.2d 1318 (9th Cir. 1985)](https://www.courtlistener.com/opinion/452994/charles-laduke-v-alan-c-nelson-etc/) — pinpoint: 1331–1332 (holding on warrantless farm-dwelling entries and the affirmed injunction); Rule quotes string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "21cc643e61362310", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "762 F.2d 1318 (1985)", "court": "9th Cir.", "neutral_cite": "1985 U.S. App. LEXIS 19963", "official_citation_present": true, "parallel_cite": "53 U.S.L.W. 2625", "title": "LaDuke v. Nelson", "year": "1985"}}
{"assertion_id": "141cd874f9760348", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Migrant farmworkers' dwellings retain their occupants' reasonable expectations of privacy, so the INS may not conduct warrantless 'area control' entries of farm housing to search or arrest absent consent or probable cause; the Ninth Circuit affirmed a class injunction barring the practice as a Fourth Amendment violation.", "title": "LaDuke v. Nelson"}}
{"assertion_id": "34f13dd0845b5f14", "dimension": "support", "kind": "home_role", "locator": {"home": "Tents"}, "payload": {"home": "Tents", "role": "Key", "title": "LaDuke v. Nelson"}}
{"assertion_id": "470a17b777bc1982", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 9th Cir.", "title": "LaDuke v. Nelson"}}
{"assertion_id": "687bc13d9dc0d0b4", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "LaDuke v. Nelson", "varies_by_point": "false"}}
```

### lake record — LaDuke v. Nelson

```json
{
  "schema_version": "s2.v1",
  "record_id": "LaDuke v. Nelson",
  "status": "under_review",
  "identity": {
    "case_name": "Charles Laduke v. Alan C. Nelson, Etc.",
    "case_name_short": "",
    "case_name_full": "Charles LaDUKE, Et Al., Plaintiffs/Appellees, v. Alan C. NELSON, Etc., Et Al., Defendants/Appellants",
    "input_case_name": "LaDuke v. Nelson",
    "court": "9th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": "1985-06-10",
    "year": 1985,
    "docket": "83-3608",
    "cluster_id": 452994,
    "lead_opinion_id": 452994,
    "sibling_ids": [],
    "absolute_url": "/opinion/452994/charles-laduke-v-alan-c-nelson-etc/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "762 F.2d 1318",
      "volume": "762",
      "reporter": "F.2d",
      "page": "1318",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "53 U.S.L.W. 2625",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "2625",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. App. LEXIS 19963",
        "volume": "1985",
        "reporter": "U.S. App. LEXIS",
        "page": "19963",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "762 F.2d 1318",
        "volume": "762",
        "reporter": "F.2d",
        "page": "1318",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. App. LEXIS 19963",
        "volume": "1985",
        "reporter": "U.S. App. LEXIS",
        "page": "19963",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 2625",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "2625",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "762 F.2d 1318",
    "official_selection": {
      "court_class": "coa",
      "selected": "762 F.2d 1318",
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
    "date_created": "2026-07-07T01:37:21Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:37:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:37:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:37:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:37:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "laduke-v-nelson--452994",
      "to_record_id": "LaDuke v. Nelson",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — LaDuke v. Nelson

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b1417-10">
  FERGUSON, Circuit Judge:
 </author>
<p id="b1417-11">
  The Immigration and Naturalization Service (“INS”) appeals from an injunction issued by the district court prohibiting the INS from conducting farm and ranch checks of migrant farm housing without a warrant, probable cause, or articulable suspicion.
  <em>
   See LaDuke v. Nelson,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. 158</a></span> (E.D.Wash.1982). The INS also appeals the award of fees under the Equal Access to Justice Act. We affirm.
 </p>
<p id="b1417-12">
  I.
 </p>
<p id="b1417-13">
  The plaintiffs, residents of migrant farm dwellings in the INS region known as the Spokane Sector, covering the states of Washington, Idaho and Montana, brought suit in 1977 alleging that the defendant’s practice of initiating and executing searches of migrant farm housing violated their Fourth Amendment rights. The district court certified the plaintiffs as a class in 1979 under Federal Rule of Civil Procedure 23(b)(2). In 1981 the district court refined the plaintiff class to include all persons who have resided or will reside in particularly described farm housing within the Sector.
 </p>
<p id="b1417-14">
  The district court found that the INS engaged in a “standard pattern” of searches within farm labor housing communities in the Sector. The court found that the INS initiated these warrantless searches without articulable suspicion or probable cause.
  <em>
   LaDuke,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/#161" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 161</a></span>;
  <em>
   see
  </em>
  note 12
  <em>
   infra.
  </em>
  The armed Border Patrol agents periodically cordoned off migrant housing during early morning or late evening hours, surrounded the residences in emergency vehicles with flashing lights, approached the homes with flashlights, and stationed officers at all doors and windows. The agents would then conduct house-to-house searches either without consent or with the alleged “knowing” consent of the occupants.
 </p>
<p id="b1417-15">
  The district court found that under these circumstances the occupants were not free to leave and, consequently, a seizure had taken place. The court further found that any consent obtained was involuntary given the substantial show of official force. The court also found that the seizures took place without probable cause, reasonable belief, or articulable suspicion that illegal aliens were present. The court enjoined the defendants and those acting in concert with them from engaging in similar unconstitutional farm check practices.
 </p>
<p id="b1417-16">
  II.
 </p>
<p id="b1417-17">
  The standard of review over the district court’s grant of a permanent injunction must, of course, be segmented according to the component functions performed by the district court.
  <em>
   See United States v. McConney,
  </em>
  <span class="citation" data-id="9471865"><a href="/opinion/431931/united-states-v-winston-bryant-mcconney/" aria-description="Citation for case: United States v. Winston Bryant McConney">728 F.2d 1195</a></span> (9th Cir.) (en banc),
  <em>
   cert. denied,
  </em>
  — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./105/101/">105 S.Ct. 101</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/83/46/">83 L.Ed.2d 46</a></span> (1984). Accordingly, the district court’s findings of fact are reviewed under the clearly erroneous standard. Fed.R.Civ.P. 52(a). A district court’s findings on the voluntariness of consent to search are reviewed under the clearly erroneous standard.
  <em>
   United States v. Caicedo-Guarnizo,
  </em>
  <span class="citation" data-id="429241"><a href="/opinion/429241/united-states-v-jose-orlando-caicedo-guarnizo/#1423" aria-description="Citation for case: United States v. Jose Orlando Caicedo-Guarnizo">723 F.2d 1420, 1423</a></span> (9th Cir.1984). The district court’s
  <span citation-index="1" class="star-pagination" label="1322"> 
   *1322
   </span>
  finding that the ranch checks are not based on articulable suspicion is also reviewed under the clearly erroneous standard.
  <em>
   United States v. Garcia-Nunez,
  </em>
  <span class="citation" data-id="9470736"><a href="/opinion/419810/united-states-v-agustin-garcia-nunez-united-states-of-america-v-charles/#561" aria-description="Citation for case: United States v. Agustin Garcia-Nunez, United States of...">709 F.2d 559, 561</a></span> (9th Cir.1983).
  <em>
   Cf. United States v. Cortez,
  </em>
  <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#416" aria-description="Citation for case: United States v. Cortez">449 U.S. 411, 416</a></span>, <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#694" aria-description="Citation for case: United States v. Cortez">101 S.Ct. 690, 694</a></span>, <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">66 L.Ed.2d 621</a></span> (1981).
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  Because the court’s jurisdiction is dependent on Article III standing, this issue is subject to de novo review. Finally, the district court’s determinations on questions of law and on mixed questions of facts and law implicating constitutional rights are reviewed de novo.
  <em>
   United States v. McConney,
  </em>
  <span class="citation" data-id="9471865"><a href="/opinion/431931/united-states-v-winston-bryant-mcconney/#1203" aria-description="Citation for case: United States v. Winston Bryant McConney">728 F.2d at 1203</a></span>.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b1418-4">
  III.
 </p>
<p id="b1418-5">
  This opinion will focus on the major arguments
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  raised by the INS in the following sequence:
 </p>
<blockquote id="b1418-6">
  (A) Do the plaintiffs have Article III standing to seek an injunction?
 </blockquote>
<blockquote id="b1418-10">
  (B) Did the district court err in its decision on the merits of plaintiffs’ Fourth Amendment claim?
 </blockquote>
<blockquote id="b1418-11">
  (C) Did the district court err in finding the essential prerequisites for an injunction met and, if not, is the issued injunction overbroad?
 </blockquote>
<blockquote id="b1418-12">
  (D) Was the class properly certified under Fed.R.Civ.P. 23(b)(2)?
 </blockquote>
<blockquote id="b1418-13">
  (E) Was the award of attorney fees and costs appropriate under the Equal Access to Justice Act?
 </blockquote>
<p id="b1418-14">
  A.
 </p>
<p id="b1418-15">
  The INS has challenged the plaintiffs’ standing to bring suit for injunctive relief under Article III of the Constitution. The “case or controversy” standing requirement serves to limit federal jurisdiction to those cases in which an adversarial
  <span citation-index="1" class="star-pagination" label="1323"> 
   *1323
   </span>
  setting is guaranteed by the parties’ “personal stake” in the outcome of the litigation.
  <em>
   Warth v. Seldin,
  </em>
  <span class="citation" data-id="9426170"><a href="/opinion/109301/warth-v-seldin/#498" aria-description="Citation for case: Warth v. Seldin">422 U.S. 490, 498</a></span>, <span class="citation" data-id="9426170"><a href="/opinion/109301/warth-v-seldin/#2204" aria-description="Citation for case: Warth v. Seldin">95 S.Ct. 2197, 2204</a></span>, <span class="citation" data-id="9426170"><a href="/opinion/109301/warth-v-seldin/" aria-description="Citation for case: Warth v. Seldin">45 L.Ed.2d 343</a></span> (1975). The Supreme Court has also extended the standing inquiry beyond this Article III based minimum to include judicially imposed “prudential limitations” on the appropriate exercise of federal judicial power.
  <em>
   Allen v. Wright,
  </em>
  — U.S. -, <span class="citation" data-id="9429754"><a href="/opinion/111258/allen-v-wright/#3324" aria-description="Citation for case: Allen v. Wright">104 S.Ct. 3315, 3324-25</a></span>, <span class="citation" data-id="9429754"><a href="/opinion/111258/allen-v-wright/" aria-description="Citation for case: Allen v. Wright">82 L.Ed.2d 556</a></span> (1984);
  <em>
   Warth v. Seldin,
  </em>
  <span class="citation" data-id="9426170"><a href="/opinion/109301/warth-v-seldin/#499" aria-description="Citation for case: Warth v. Seldin">422 U.S. at 499-500</a></span>, <span class="citation" data-id="9426170"><a href="/opinion/109301/warth-v-seldin/#2205" aria-description="Citation for case: Warth v. Seldin">95 S.Ct. at 2205</a></span>. The “irreducible minimum” demanded of a proper plaintiff by Article Ill’s constitutional demands, however, requires that a plaintiff show he has “personally ... suffered some actual or threatened injury as a result of the putatively illegal conduct of the defendant,” that can be “fairly” traced to the defendant’s challenged conduct, and which “is likely to be redressed by a favorable decision.”
  <em>
   Valley Forge Christian College v. Americans United for Separation of Church and State, Inc.,
  </em>
  <span class="citation" data-id="9428574"><a href="/opinion/110599/valley-forge-christian-college-v-americans-united-for-separation-of-church/#472" aria-description="Citation for case: Valley Forge Christian College v. Americans United for...">454 U.S. 464, 472</a></span>,<span class="citation" data-id="9428574"><a href="/opinion/110599/valley-forge-christian-college-v-americans-united-for-separation-of-church/#758" aria-description="Citation for case: Valley Forge Christian College v. Americans United for...">102 S.Ct. 752, 758</a></span>, <span class="citation" data-id="9428574"><a href="/opinion/110599/valley-forge-christian-college-v-americans-united-for-separation-of-church/" aria-description="Citation for case: Valley Forge Christian College v. Americans United for...">70 L.Ed.2d 700</a></span> (1982).
 </p>
<p id="b1419-7">
  Added to this core constitutional standing test are judicially created prudential limitations, including: a general prohibition on “raising another person’s legal rights”,
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  a preference for the resolution of “generalized grievances” in the representative branches,
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  and the “requirement that a plaintiff’s complaint fall within the zone of interests protected” by the pertinent law.
  <em>
   Allen v. Wright,
  </em>
  — U.S. -, <span class="citation" data-id="9429754"><a href="/opinion/111258/allen-v-wright/#3324" aria-description="Citation for case: Allen v. Wright">104 S.Ct. 3315, 3324-25</a></span>, <span class="citation" data-id="9429754"><a href="/opinion/111258/allen-v-wright/" aria-description="Citation for case: Allen v. Wright">82 L.Ed.2d 556</a></span> (1984). Finally, the Supreme Court has indicated that, at least when injunctive relief is sought, litigants must adduce a “credible threat” of recurrent injury.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
<em>
   Kolender v. Lawson,
  </em>
  <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">461 U.S. 352</a></span>, <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">103 S.Ct. 1855</a></span>, 1857 n. 3, <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">75 L.Ed.2d 903</a></span> (1983);
  <em>
   Los Angeles v. Lyons,
  </em>
  <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">461 U.S. 95</a></span>, <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">103 S.Ct. 1660</a></span>, <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">75 L.Ed.2d 675</a></span> (1983). We first address the significance of
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  to plaintiffs’ standing to seek injunctive relief.
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
</p>
<p id="b1419-13">
  In
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>,
  </em>
  the plaintiff brought suit under <span class="citation no-link">42 U.S.C. § 1983</span> for damages and declaratory and injunctive relief against the City of Los Angeles and four of its police officers. The plaintiff had previously been subjected to an allegedly unprovoked and unjustified “chokehold” by a police officer in the course of a routine stop for a traffic violation. The Supreme Court reversed the Ninth Circuit’s affirmance of a preliminary injunction in three discrete holdings. First, the Court held that Lyons lacked standing under the case or controversy clause of Article III to seek injunctive relief and consequently the lower courts lacked jurisdiction over his injunctive claim.
  <span class="citation no-link"><em>
   Id.
  </em>
  at 101</span>, 103 S.Ct. at 1664. Second, the Court held that the plaintiff had not met the standards for issuance of injunctive relief.
  <em>
   Id.
  </em>
  at 109, 103 S.Ct. at 1668. Third, the Court held that the jurisprudential concerns of “equity, comity, and federalism” sharply constrict federal judicial oversight of “state law enforcement authorities,”
  <em>
   id.
  </em>
<span citation-index="1" class="star-pagination" label="1324"> 
   *1324
   </span>
  at 112, 103 S.Ct. at 1670, thereby making injunctive relief inappropriate.
 </p>
<p id="b1420-4">
  As the Supreme Court summarized: “Lyons’ standing to seek the injunction requested depended on whether he was likely to suffer future injury from the use of the chokeholds by police officers.” 461 U.S. at 105, 103 S.Ct. at 1667. Relying heavily on
  <em>
   O’Shea v. Littleton,
  </em>
  <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">414 U.S. 488</a></span>, <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">94 S.Ct. 669</a></span>, <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">38 L.Ed.2d 674</a></span> (1974) and
  <em>
   Rizzo v. Goode,
  </em>
  <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">423 U.S. 362</a></span>, <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">96 S.Ct. 598</a></span>, <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">46 L.Ed.2d 561</a></span> (1976), the Court held that Lyons did not face “a real and immediate threat of again being illegally choked.”
  <em>
   Id.
  </em>
  461 U.S. at 110, 103 S.Ct. at 1669. Finding the plaintiff’s allegation of future injury speculative,
  <em>
   id.
  </em>
  at 108, 103 S.Ct. at 1668, Court held that the objective “reality of the threat of repeated injury,”
  <em>
   id.
  </em>
  at 107 n. 8, 103 S.Ct. at 1668 n. 8, was beyond reasonable belief given the remote probability that Lyons would once again violate the law and incite an unjustifiable response by Los Angeles police. Finally, the Court found probative the fact that the district court had made “no finding that Lyons faced a real and immediate threat of again being illegally choked.”
  <em>
   Id.
  </em>
  at 110, 103 S.Ct. at 1669.
 </p>
<p id="b1420-5">
  At a minimum,
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  requires that the “personal stake” showing necessary under Article III in cases involving injunctive relief includes an essential showing of the likelihood of similar injury in the future. At least for Lyons, past injury was insufficient, standing alone, to afford him a “personal stake” in the prospective relief provided by an injunction.
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
  Four fundamental differences between
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  and this case demonstrate why the plaintiff class has a sufficient “personal stake” under Article III to warrant the prospective relief only an injunction can provide.
 </p>
<p id="b1420-6">
  The first difference between
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  and this case lies in the respective district court findings on the likelihood of recurrent injury. The district court in
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  made no finding of likely recurrence,
  <em>
   Lyons,
  </em>
  <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">461 U.S. at 110</a></span> n. 9, 103 S.Ct. at 1669 n. 9, while the district court in this case made a specific finding of likely recurrence.
  <em>
   LaDuke,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/#164" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 164</a></span>. Second, the district court in this case explicitly found that the defendants engaged in a standard pattern of officially sanctioned officer behavior, <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/#160" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 160</a></span>, violative of the plaintiffs’ constitutional rights. Conversely, the
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  opinion expressly noted the absence of any written or oral pronouncements by the Los Angeles Police Department sanctioning the unjustifiable application of the chokehold and pointed to the absence of "any [record] evidence showing a pattern of police behavior” suggestive of an unconstitutional application of the chokehold.
  <em>
   Id.
  </em>
  461 U.S. at 110 n. 9, 103 S.Ct. at 1669 n. 9. The Supreme Court has repeatedly upheld the appropriateness of federal injunctive relief to combat a “pattern” of illicit law enforcement behavior.
  <em>
   See Allee v. Medrano,
  </em>
  <span class="citation" data-id="9425720"><a href="/opinion/109031/allee-v-medrano/#812" aria-description="Citation for case: Allee v. Medrano">416 U.S. 802, 812</a></span>, <span class="citation" data-id="9425720"><a href="/opinion/109031/allee-v-medrano/#2198" aria-description="Citation for case: Allee v. Medrano">94 S.Ct. 2191, 2198</a></span>, <span class="citation" data-id="9425720"><a href="/opinion/109031/allee-v-medrano/" aria-description="Citation for case: Allee v. Medrano">40 L.Ed.2d 566</a></span> (1974);
  <em>
   Hague v. CIO,
  </em>
  <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">307 U.S. 496</a></span>, <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">59 S.Ct. 954</a></span>, <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">83 L.Ed. 1423</a></span> (1939);
  <em>
   see also INS v. Delgado,
  </em>
  — U.S. -, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">104 S.Ct. 1758</a></span>, 1763 n. 4, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">80 L.Ed.2d 247</a></span> (1984);
  <em>
   Rizzo v. Goode,
  </em>
  <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/#375" aria-description="Citation for case: Rizzo v. Goode">423 U.S. 362, 375</a></span>, <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/#606" aria-description="Citation for case: Rizzo v. Goode">96 S.Ct. 598, 606</a></span>, <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">46 L.Ed.2d 561</a></span> (1976) (distinguishing
  <em>
   Allee
  </em>
  and
  <em>
   Hague
  </em>
  as involving patterns of misbehavior, not isolated incidents).
 </p>
<p id="b1420-13">
  A third distinguishing feature that separates the present case from
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  is the absence of the prudential limitations circumscribing federal court intervention in state law enforcement matters.
  <em>
   Lyons, Rizzo,
  </em>
  and
  <em>
   <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">O’Shea</a></span>
  </em>
  all involved attempts by plaintiffs to entangle federal courts in the operations of state law enforcement and criminal justice institutions.
  <em>
   See City of Los Angeles v. Lyons,
  </em>
  <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">461 U.S. 95</a></span>, <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">103 S.Ct. 1660</a></span>, <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">75 L.Ed.2d 675</a></span> (1983) (city law enforcement practices);
  <em>
   Rizzo v. Goode,
  </em>
  <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">423 U.S. 362</a></span>, <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">96 S.Ct. 598</a></span>, <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">46 L.Ed.2d 561</a></span> (1976) (same);
  <em>
   O’Shea v. Littleton,
  </em>
  <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">414 U.S. 488</a></span>, <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">94 S.Ct. 669</a></span>, <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">38 L.Ed.2d 674</a></span> (1974) (county criminal justice system).
  <span citation-index="1" class="star-pagination" label="1325"> 
   *1325
   </span>
  Obviously, none of the considerations inherent in the judicial concept of “Our Federalism,”
  <em>
   Younger v. Harris,
  </em>
  <span class="citation" data-id="9424435"><a href="/opinion/108263/younger-v-harris/#44" aria-description="Citation for case: Younger v. Harris">401 U.S. 37, 44</a></span>, <span class="citation" data-id="9424435"><a href="/opinion/108263/younger-v-harris/#751" aria-description="Citation for case: Younger v. Harris">91 S.Ct. 746, 751</a></span>, <span class="citation" data-id="9424435"><a href="/opinion/108263/younger-v-harris/" aria-description="Citation for case: Younger v. Harris">27 L.Ed.2d 669</a></span> (1971), are implicated in constitutional challenges to executive branch behavior in federal courts. This court cannot rely on a state judiciary to correct the unconstitutional practices of federal officials.
  <em>
   Cf Los Angeles v. Lyons,
  </em>
  461 U.S. at 113, <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/#1671" aria-description="Citation for case: City of Los Angeles v. Lyons">103 S.Ct. at 1671</a></span> (comity counsels in favor of permitting state judiciary systems to oversee state law enforcement practices). Accordingly, the comity considerations which influenced the Supreme Court’s decisions in
  <em>
   O’Shea, Rizzo
  </em>
  and
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  are inapplicable in this case.
 </p>
<p id="b1421-5">
  Enforcement of the nation’s immigration laws has been delegated by Congress to the Executive Branch.
  <em>
   See United States v. Valenzuela-Bernal,
  </em>
  <span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/#864" aria-description="Citation for case: United States v. Valenzuela-Bernal">458 U.S. 858, 864</a></span>, <span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/#3444" aria-description="Citation for case: United States v. Valenzuela-Bernal">102 S.Ct. 3440, 3444</a></span>, <span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/" aria-description="Citation for case: United States v. Valenzuela-Bernal">73 L.Ed.2d 1193</a></span> (1982). Nonetheless, the federal judiciary has been vested with the ultimate authority to determine the constitutionality of the actions of the other branches of the federal government.
  <a class="footnote" href="#fn9" id="fn9_ref">
   9
  </a>
  While the co-equal branches of the federal government are entitled to “the widest latitude in the dispatch of [their] own internal affairs,”
  <em>
   Rizzo,
  </em>
  <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/#379" aria-description="Citation for case: Rizzo v. Goode">423 U.S. at 379</a></span>, <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">96 S.Ct. at 608</a></span> (quoting
  <em>
   Cafeteria Workers v. McElroy,
  </em>
  <span class="citation" data-id="9422292"><a href="/opinion/106290/cafeteria-restaurant-workers-union-local-473-v-mcelroy/" aria-description="Citation for case: Cafeteria &amp; Restaurant Workers Union, Local 473 v. McElroy">367 U.S. 886</a></span>, <span class="citation" data-id="9422292"><a href="/opinion/106290/cafeteria-restaurant-workers-union-local-473-v-mcelroy/" aria-description="Citation for case: Cafeteria &amp; Restaurant Workers Union, Local 473 v. McElroy">81 S.Ct. 1743</a></span>, <span class="citation" data-id="9422292"><a href="/opinion/106290/cafeteria-restaurant-workers-union-local-473-v-mcelroy/" aria-description="Citation for case: Cafeteria &amp; Restaurant Workers Union, Local 473 v. McElroy">6 L.Ed.2d 1230</a></span> (1961)), the executive branch has no discretion with which to violate constitutional rights.
  <em>
   Accord Illinois Migrant Council v. Pilliod,
  </em>
  <span class="citation" data-id="9463025"><a href="/opinion/338582/illinois-migrant-council-etc-v-alva-l-pilliod-etc/#1068" aria-description="Citation for case: Illinois Migrant Council, Etc. v. Alva L. Pilliod, Etc.">540 F.2d 1062, 1068</a></span> (7th Cir.1976),
  <em>
   modified en banc,
  </em>
  <span class="citation" data-id="342479"><a href="/opinion/342479/illinois-migrant-council-etc-v-alva-l-pilliod-etc/" aria-description="Citation for case: Illinois Migrant Council, Etc. v. Alva L. Pilliod, Etc.">548 F.2d 715</a></span> (1977).
 </p>
<p id="b1421-6">
  The fourth and final feature which distinguishes this case from
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
  </em>
  and O’Shea
  <a class="footnote" href="#fn10" id="fn10_ref">
   10
  </a>
  is the fact that the plaintiffs constitute a certified class under Federal Rule of Civil Procedure 23(b)(2). For standing purposes, this court’s inquiry must focus on the standing of the
  <em>
   class
  </em>
  to seek equitable relief.
  <em>
   See Sosna v. Iowa,
  </em>
  <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/#399" aria-description="Citation for case: Sosna v. Iowa">419 U.S. 393, 399</a></span>, <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/#557" aria-description="Citation for case: Sosna v. Iowa">95 S.Ct. 553, 557</a></span>, <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/" aria-description="Citation for case: Sosna v. Iowa">42 L.Ed.2d 532</a></span> (1975) ("When the District Court certified the propriety of the class action, the class of unnamed persons described in the certification acquired a legal status separate from the interest asserted by appellant.”). Standing, however, is a jurisdictional element that must be satisfied prior to class certification. While the fact of certification will preserve a class’s standing even after the named individual representatives have lost the required “personal stake,”
  <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/#399" aria-description="Citation for case: Sosna v. Iowa"><em>
   see id.
  </em>
  at 399</a></span>, 95 S.Ct. at 557, certification is not sufficient in itself to bestow standing, on individuals or a class who lacked the requisite personal stake at the outset. The Supreme Court has held that, under the analogous doctrine of mootness, the “personal-stake requirement relating] to the first purpose of the ease-or-controversy doctrine” is met in class actions simply by class certification notwithstanding the subsequent loss of a “personal stake” by the class representative.
  <em>
   United States Parole Commission v. Geraghty,
  </em>
  <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#400" aria-description="Citation for case: United States Parole Commission v. Geraghty">445 U.S. 388, 400</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#1210" aria-description="Citation for case: United States Parole Commission v. Geraghty">100 S.Ct. 1202, 1210</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/" aria-description="Citation for case: United States Parole Commission v. Geraghty">63 L.Ed.2d 479</a></span> (1980). The
  <em>
   <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/" aria-description="Citation for case: United States Parole Commission v. Geraghty">Geraghty</a></span>
  </em>
  court, noting it was following precedent which had eroded the “strict, formalistic perception of Article III,”
  <em>
   <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/" aria-description="Citation for case: United States Parole Commission v. Geraghty">id.</a></span>
  </em>
  at 404 n. 11, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/" aria-description="Citation for case: United States Parole Commission v. Geraghty">100 S.Ct. at 1213</a></span> n. 11, applied a “flexible” approach in concluding the personal stake necessary to satisfy Article Ill’s case or controversy requirement is satisfied by the class representative’s cognizable interest in the certification decision.
  <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#404" aria-description="Citation for case: United States Parole Commission v. Geraghty"><em>
   Id.
  </em>
  at 404</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#1212" aria-description="Citation for case: United States Parole Commission v. Geraghty">100 S.Ct. at 1212</a></span>. This “personal stake” in the certification decision survives the mootness of the named plaintiffs’ claims.
  <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#403" aria-description="Citation for case: United States Parole Commission v. Geraghty"><em>
   Id.
  </em>
  at 403</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#1212" aria-description="Citation for case: United States Parole Commission v. Geraghty">100 S.Ct. at 1212</a></span>.
 </p>
<p id="b1422-3">
<span citation-index="1" class="star-pagination" label="1326"> 
   *1326
   </span>
  Although mootness and standing are separate justiciability requirements, they share the component of a necessary “personal interest” in the outcome of the litigation.
  <em>
   See Geraghty,
  </em>
  <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#397" aria-description="Citation for case: United States Parole Commission v. Geraghty">445 U.S. at 397</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#1209" aria-description="Citation for case: United States Parole Commission v. Geraghty">100 S.Ct. at 1209</a></span>. “The requisite personal interest that must exist at the commencement of the litigation (standing) must continue throughout its existence (mootness).”
  <em>
   Geraghty,
  </em>
  <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#397" aria-description="Citation for case: United States Parole Commission v. Geraghty">445 U.S. at 397</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/" aria-description="Citation for case: United States Parole Commission v. Geraghty">100 S.Ct. at 1209</a></span> (quoting Monaghan,
  <em>
   Constitutional Adjudication: The Who and When,
  </em>
  <span class="citation no-link">82 Yale L.J. 1363</span>, 1384 (1973)). Of course, as class representatives, by definition, the named plaintiffs can prosecute only the class claims. Accordingly, the standing inquiry on the merits of plaintiffs’ case is directed to whether the class has standing — the necessary personal interest — to raise their constitutional claim for injunctive relief. The evidence presented at trial reveals that the plaintiff class faces a credible threat of recurring injury.
 </p>
<p id="b1422-4">
  Each of the four distinguishing features described above supports the conclusion that the class has standing under Article III as interpreted by
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>.
  </em>
  The systematic pattern finding of the district court, the official INS policy for the conduct of ranch checks, and the district court’s finding of likely recurrence all reinforce the reality and immediacy of the plaintiffs’ constitutional claims. Unlike Lyons, the members of plaintiff class do not have to induce a police encounter before the possibility of injury can occur.
  <em>
   See Lewis v. Tully,
  </em>
  <span class="citation" data-id="8800747"><a href="/opinion/8816245/lewis-v-tully/" aria-description="Citation for case: Lewis v. Tully">99 F.R.D. 632</a></span> (N.D.Ill.1983). The class members are subject to constitutional injury based on the completely innocent behavior of residing in migrant farm housing. Their grievances are general only to the residents of farm housing in the Spokane Sector. Members of the class have repeatedly suffered personal injuries in the past that can fairly be traced to the INS’s standard ranch and farm practices. Class members have been and will continue to be aggrieved by the defendants’ unconstitutional pattern of conduct in contravention of the Fourth Amendment. The equitable relief sought by the plaintiff class is both efficacious and responsive to the individual interests of class members and the certified class.
 </p>
<p id="b1422-7">
  B.
 </p>
<p id="b1422-8">
  The district court found that the defendants’ pattern of conduct violated the plaintiffs’ Fourth Amendment rights under either of two separate holdings. The district court first held that the methods employed by the Border Patrol — “sealing] off roads or paths leading out of the housing area” if possible, and “stationpng] officers at all doors and windows” of the dwellings to prevent egress — constituted a “seizure” of the occupants such that “a reasonable person would have believed that he was not free to leave.”
  <em>
   LaDuke,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/#162" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 162-63</a></span>. Because the seizure thus preceded the alleged consent, the question of consent is immaterial to the finding of a Fourth Amendment violation. In the alternative, the district court concluded that under the INS’s standard farm check practice the consent given by the farm occupants was not voluntary.
 </p>
<p id="b1422-9">
  In response, the INS argues that the consent given by the occupants was voluntary and, citing
  <em>
   INS v. Delgado,
  </em>
  — U.S. --, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">104 S.Ct. 1758</a></span>, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">80 L.Ed.2d 247</a></span> (1984), contests the district court’s conclusion that a “seizure” occurs in the course of their farm and ranch checks. Other than its contention, raised unsuccessfully in the district court, that farm housing searches are identical to factory worksite sweeps, the INS has not explained why it requires its agents to obtain a warrant for urban residential searches but not for rural residential searches.
  <a class="footnote" href="#fn11" id="fn11_ref">
   11
  </a>
</p>
<p id="b1423-4">
<span citation-index="1" class="star-pagination" label="1327"> 
   *1327
   </span>
  In fashioning the injunction, the district court followed the law of this and every other circuit which has addressed the issue by requiring the INS to adduce articulable suspicion of both alienage and unlawful presence prior to the initiation of detentive stops.
  <em>
   See, e.g., Benitez-Mendez v. INS,
  </em>
  <span class="citation" data-id="418799"><a href="/opinion/418799/eleuterio-benitez-mendez-v-immigration-and-naturalization-service/#1100" aria-description="Citation for case: Eleuterio Benitez-Mendez v. Immigration and...">707 F.2d 1107, 1100</a></span> (9th Cir.1983),
  <em>
   amended
  </em>
  <span class="citation" data-id="444456"><a href="/opinion/444456/eleuterio-benitez-mendez-v-immigration-and-naturalization-service/" aria-description="Citation for case: Eleuterio Benitez-Mendez v. Immigration and...">748 F.2d 539</a></span> (9th Cir.1984) (clarifying that a seizure had taken place);
  <em>
   International Ladies Garment Workers Union v. Sureck,
  </em>
  <span class="citation" data-id="8915362"><a href="/opinion/8925775/international-ladies-garment-workers-union-v-sureck/#638" aria-description="Citation for case: International Ladies&#x27; Garment Workers&#x27; Union v. Sureck">681 F.2d 624, 638</a></span> (9th Cir.1982),
  <em>
   rev’d on other grounds sub nom. INS v. Delgado,
  </em>
  — U.S.-, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">104 S.Ct. 1758</a></span>, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">80 L.Ed.2d 247</a></span> (1984).
  <em>
   Accord Illinois Migrant Council v. Pilliod,
  </em>
  <span class="citation" data-id="9463025"><a href="/opinion/338582/illinois-migrant-council-etc-v-alva-l-pilliod-etc/#1070" aria-description="Citation for case: Illinois Migrant Council, Etc. v. Alva L. Pilliod, Etc.">540 F.2d 1062, 1070</a></span> (7th Cir.1976),
  <em>
   modified on reh’g en banc,
  </em>
  <span class="citation" data-id="342479"><a href="/opinion/342479/illinois-migrant-council-etc-v-alva-l-pilliod-etc/" aria-description="Citation for case: Illinois Migrant Council, Etc. v. Alva L. Pilliod, Etc.">548 F.2d 715</a></span> (1977);
  <em>
   Ojeda-Vinales v. INS,
  </em>
  <span class="citation" data-id="330250"><a href="/opinion/330250/jose-gil-ojeda-vinales-v-the-immigration-and-naturalization-service/#287" aria-description="Citation for case: Jose Gil Ojeda-Vinales v. The Immigration and...">523 F.2d 286, 287</a></span> (2d Cir.1975) (following
  <em>
   Au Yi
  </em>
  Lau);
  <em>
   Au Yi Lau v. INS,
  </em>
  <span class="citation multiple-matches"><a href="/c/F.2d/445/217/">445 F.2d 217</a></span>, 223 (D.C.Cir.),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./404/864/">404 U.S. 864</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./92/64/">92 S.Ct. 64</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/30/108/">30 L.Ed.2d 108</a></span> (1971);
  <em>
   Ramirez v. Webb,
  </em>
  <span class="citation" data-id="1897912"><a href="/opinion/1897912/ramirez-v-webb/#1282" aria-description="Citation for case: Ramirez v. Webb">599 F.Supp. 1278, 1282</a></span> (W.D.Mich.1984). Consistent with the statutory language of <span class="citation no-link">8 U.S.C. § 1357</span>(a)(1), however, the district court’s injunction does permit nondetentive interrogations based solely on alienage.
  <em>
   LaDuke,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/#165" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 165</a></span>.
  <em>
   Accord Illinois Migrant Council v. Pilliod,
  </em>
  <span class="citation" data-id="342479"><a href="/opinion/342479/illinois-migrant-council-etc-v-alva-l-pilliod-etc/" aria-description="Citation for case: Illinois Migrant Council, Etc. v. Alva L. Pilliod, Etc.">548 F.2d 715</a></span> (7th Cir.1977) (en banc).
  <em>
   But see Marquez v. Kiley,
  </em>
  <span class="citation" data-id="1430125"><a href="/opinion/1430125/marquez-v-kiley/" aria-description="Citation for case: Marquez v. Kiley">436 F.Supp. 100</a></span> (S.D.N.Y.1977) (Fourth Amendment bars both detentive and nondetentive INS interrogations based solely on alien-age).
 </p>
<p id="b1423-12">
  1.
 </p>
<p id="b1423-13">
  The district court’s conclusion that the INS farm and ranch check practices result in the seizure of an entire farm housing community is predicated on the facts as the district court found them. On this record we cannot say that these facts are clearly erroneous.
  <a class="footnote" href="#fn12" id="fn12_ref">
   12
  </a>
  Nonetheless, the seizure conclusion is a mixed question of law and fact subject to de novo review on these facts. The district court concluded: “when uniformed officers surround residences with emergency vehicles with flashing lights, approach the houses with flashlights, awaken the occupants, and station officers at all doors and windows, it borders on the incredulous to conclude that people such as the members of the class in this action would feel free to walk away.” This conclusion is reinforced by the further factual finding that residents who exited the housing “were apprehended, detained, and interrogated.”
 </p>
<p id="b1423-14">
  The record in this case contains incidents in which Border Patrol agents forcibly intruded, either physically or with a flash
  <span citation-index="1" class="star-pagination" label="1328"> 
   *1328
   </span>
  light, into the housing units.
  <a class="footnote" href="#fn13" id="fn13_ref">
   13
  </a>
  Looking at the entire record, especially the findings that the access roads were sealed, the means of egress from the individual units were surrounded and those who left were seized, we affirm the district court’s conclusion that a seizure of the entire unit is routinely accomplished. Moreover, the Supreme Court’s opinion in
  <em>
   INS v. Delgado
  </em>
  only strengthens the validity of the district court’s seizure conclusion.
 </p>
<p id="b1424-4">
  In
  <em>
   INS v. Delgado,
  </em>
  — U.S. -, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">104 S.Ct. 1758</a></span>, <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">80 L.Ed.2d 247</a></span> (1984), the Supreme Court held that INS worksite interrogations conducted pursuant to warrants do not violate the Fourth Amendment. The
  <em>
   <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>
  </em>
  opinion rejected a contrary holding by this circuit wherein we had held that such factory surveys resulted in a seizure of the workforce. The Court also reversed our alternate holding that employee questioning must be based on particularized suspicion.
 </p>
<p id="b1424-6">
  In dismissing the seizure-of-the-workforce theory the Supreme Court discounted the plaintiff’s evidence that employees were not free to leave the factory.
  <a class="footnote" href="#fn14" id="fn14_ref">
   14
  </a>
  The Court then held that: “if mere questioning does not constitute a seizure when it occurs inside the factory, it is no more a seizure when it occurs at the exits.” If INS agents were lawfully conducting questioning, pursuant to a warrant, inside the workplace, then similar conduct is permissible at points of egress.
 </p>
<p id="b1424-7">
  On the issue of particularized suspicion of illegal alienage, the Supreme Court found that none of the individual encounters rose to the level of a detentive interrogation.
  <em>
   Id.
  </em>
  104 S.Ct. at 1764. According to the Court, the brief encounters only amounted to “questioning” that did not involve any reasonable apprehension of, or actual detention by the INS agents. Under the “seizure” test articulated in
  <em>
   Delgado: “Unless the circumstances of the encounter are so intimidating
  </em>
  as to demonstrate that a reasonable person would have believed he was not free to leave if he had not responded, one cannot say that the questioning resulted in a detention under the Fourth Amendment.”
  <em>
   Id.
  </em>
  at 1763 (emphasis added).
 </p>
<p id="b1424-10">
  Two material distinctions between
  <em>
   <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>
  </em>
  and the present case are noteworthy. First, unlike
  <em>
   <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>,
  </em>
  the INS agents do not obtain any form of warrant for ranch and farm checks. As the district court found, the INS agents base their decision to check on a random basis without any current articulable suspicion that particular units will contain illegal aliens. Also unlike
  <em>
   <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>,
  </em>
  the INS systematically fails to obtain the consent of the owner of the farm housing. A second distinction between the factory surveys in
  <em>
   <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>
  </em>
  and farm checks is the materially different forum in which these searches take place— the workplace versus the home. Although the INS persists in contending that farm housing is part and parcel of the workplace and should be treated similarly, the simple truth is that the INS itself has recognized that they are dissimilar. If the INS truly thought that the occupants of farm housing were living at the workplace then the INS would be obliged to seek the consent of the employer — not the occupant — to obtain access. The measure of protection
  <span citation-index="1" class="star-pagination" label="1329"> 
   *1329
   </span>
  accorded the home under the Fourth Amendment is .qualitatively different from that afforded the workplace under
  <em>
   <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>.
  </em>
  “[T]he employers’ expectation of privacy in the plant setting ... certainly is far less than the traditional expectation of privacy in one’s residence.”
  <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#1767" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><em>
   Id.
  </em>
  at 1767</a></span> (Powell, J., concurring). Significantly, the
  <em>
   <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>
  </em>
  opinion’s reliance on the permissibility of questioning within the open interior of the workplace to justify questioning at the workplace exits is clearly inapplicable to the home setting.
 </p>
<p id="b1425-5">
  2.
 </p>
<p id="b1425-6">
  In the alternative, the district court held that under the circumstances of these farm checks, any consent given by the occupants was not voluntary. The government has the burden of proving voluntary consent.
  <em>
   Schneckloth,
  </em>
  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#248" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218 at 248</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#2058" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041 at 2058</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L.Ed.2d 854</a></span> (1973) (state must show voluntariness “when the subject of a search is not in custody”). On appeal, we can reverse the district court’s consent finding “only if in viewing the evidence in the light most favorable to the [plaintiffs],” the finding is clearly erroneous.
  <a class="footnote" href="#fn15" id="fn15_ref">
   15
  </a>
</p>
<p id="b1425-7">
  The district court listed the following factors as supportive of its finding that, under the standard practices applicable to ranch and farm checks, any consent given by the occupants was not voluntary: the uniform failure of the agents to advise the occupants of the right to refuse; the inherent fear that the residents of the camp have of uniformed officers because of their Mexican heritage; the limited lingual and educational background of the housing occupants; the early morning or late evening hours of the checks; and the occupant’s knowledge of the “power which INS has in dealing with them” as opposed to the average citizen.
  <em>
   LaDuke,
  </em>
  460 F.Supp. at 163 (citing
  <em>
   Marquez v. Kiley,
  </em>
  <span class="citation" data-id="1430125"><a href="/opinion/1430125/marquez-v-kiley/#113" aria-description="Citation for case: Marquez v. Kiley">436 F.Supp. 100, 113-14</a></span> (S.D.N.Y.1977)). Citing the show of official force and the vulnerable nature of the migrant workforce, the district court found that the government had not met its burden in showing voluntary consent to search. When placed against the court’s other factual findings and the record as a whole, the district court’s factual finding of involuntary consent when the occupants are confronted with the standard pattern of conduct in a ranch check is not clearly erroneous.
  <a class="footnote" href="#fn16" id="fn16_ref">
   16
  </a>
</p>
<p id="b1425-11">
  Courts have referred to identical or similar factors as probative on the factual question of the voluntariness of consent to search.
  <em>
   See, e.g., Schneckloth v. Bustamonte,
  </em>
  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L.Ed.2d 854</a></span> (1973) (“traditional definition of voluntariness we accept today has always taken into account evidence of minimal schooling”; failure to inform of right to refuse consent probative on voluntariness);
  <em>
   United States v. Mayes,
  </em>
  <span class="citation" data-id="344431"><a href="/opinion/344431/united-states-v-theodore-howard-mayes/" aria-description="Citation for case: United States v. Theodore Howard Mayes">552 F.2d 729</a></span> (6th Cir.1977) (minimal schooling);
  <em>
   United States v. O’Looney,
  </em>
  <span class="citation" data-id="9463220"><a href="/opinion/340099/united-states-v-michael-olooney/#388" aria-description="Citation for case: United States v. Michael O&#x27;LOOney">544 F.2d 385, 388</a></span> (9th Cir.) (business sophistication),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./429/1023/">429 U.S. 1023</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./97/642/">97 S.Ct. 642</a></span>, <span class="citation no-link">50 L.Ed.2d 625</span> (1976);
  <em>
   United States v. Rodriguez,
  </em>
  <span class="citation" data-id="331358"><a href="/opinion/331358/united-states-v-eduardo-rodriguez/#1315" aria-description="Citation for case: United States v. Eduardo Rodriguez">525 F.2d 1313, 1315-16</a></span> (10th Cir.1975) (lack of fluency in English);
  <em>
   United States v. Marshall,
  </em>
  <span class="citation" data-id="315664"><a href="/opinion/315664/united-states-v-robert-marshall-united-states-of-america-v-dennis/#1187" aria-description="Citation for case: United States v. Robert Marshall, United States of...">488 F.2d 1169, 1187-89</a></span> (9th Cir.1973) (show of force by armed officers; display of authority);
  <em>
   Harless v. Turner,
  </em>
  <span class="citation" data-id="302265"><a href="/opinion/302265/george-franklin-harless-v-john-w-turner-warden-utah-state-prison/#1338" aria-description="Citation for case: George Franklin Harless v. John W. Turner, Warden, Utah...">456 F.2d 1337, 1338</a></span> (10th Cir.1972) (defendant awakened by numerous officers at early morning hour);
  <em>
   Marquez v. Kiley,
  </em>
  <span class="citation" data-id="1430125"><a href="/opinion/1430125/marquez-v-kiley/#113" aria-description="Citation for case: Marquez v. Kiley">436 F.Supp. 100, 113-14</a></span> (S.D.N.Y.1977). The district court’s finding of involuntary consent also finds support on this record in that the INS did not meet its evidentiary burden to prove consent; the record demonstrates “no more than acquiescence to a claim of lawful authority.”
  <em>
   Bumper v. North Carolina,
  </em>
  <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#548" aria-description="Citation for case: Bumper v. North Carolina">391 U.S. 543, 548-49</a></span>, <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#1792" aria-description="Citation for case: Bumper v. North Carolina">88 S.Ct. 1788, 1792</a></span>, <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">20 L.Ed.2d 797</a></span> (1968);
  <em>
   cf. Gomez v. Turner,
  </em>
  <span class="citation" data-id="400070"><a href="/opinion/400070/manuel-gomez-v-maurice-t-turner-jr-chief-of-police/#141" aria-description="Citation for case: Manuel Gomez v. Maurice T. Turner, Jr., Chief of Police">672 F.2d 134, 141</a></span> (D.C.Cir.1982) (“ ‘seizure’ occurs when a police officer, by force or show of authority, restrains the liberty of a citizen”). The atmo
  <span citation-index="1" class="star-pagination" label="1330"> 
   *1330
   </span>
  sphere surrounding the INS’s standard farm check practices depicts a substantial show of official force. The tenor of the injunction reveals that it is aimed at preventing involuntary consent prompted by shows of force or claims of lawful authority.
  <em>
   LaDuke,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/#165" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 165</a></span>.
 </p>
<p id="b1426-4">
  C.
 </p>
<p id="b1426-5">
  The government challenges both the appropriateness of injunctive relief and the breadth of the injunction issued. We affirm the issuance of an injunction and reject the INS’s overbreadth arguments as raised in the district court.
 </p>
<p id="b1426-6">
  1.
 </p>
<p id="b1426-7">
  The district court correctly stated the basic prerequisites for issuance of a permanent injunction as “the likelihood of substantial and immediate irreparable injury and the inadequacy of remedies at law.”
  <em>
   LaDuke,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 162</a></span> (citing
  <em>
   O’Shea,
  </em>
  <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/#502" aria-description="Citation for case: O&#x27;Shea v. Littleton">414 U.S. at 502</a></span>, 94 S.Ct. at 679). The district court then found that plaintiffs had prevailed on the merits and the balance of the equities favored injunctive relief.
  <em>
   La-Duke,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/#162" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 162</a></span>. The court then determined “what form of [equitable] relief is appropriate.”
  <em>
   <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/" aria-description="Citation for case: LaDuke v. Nelson">Id.</a></span>
  </em>
  Twenty days after issuance
  <em>
   of the
  </em>
  original injunction, the district court amended the injunction, an act clearly within its jurisdiction,
  <em>
   Safe Flight Instrument Corp. v. United Control Corp.,
  </em>
  <span class="citation" data-id="8906441"><a href="/opinion/8918072/safe-flight-instrument-corp-v-united-control-corp/#1343" aria-description="Citation for case: Safe Flight Instrument Corp. v. United Control Corp.">576 F.2d 1340, 1343</a></span> (9th Cir.1978), to clarify that the injunction “is not intended to prohibit clearly consensual entries such as those made for the purpose of gathering an arrested alien’s belongings.”
  <em>
   LaDuke,
  </em>
  <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/" aria-description="Citation for case: LaDuke v. Nelson">560 F.Supp. at 165</a></span> n. 1.
 </p>
<p id="b1426-8">
  From the preceding discussion of the merits of plaintiffs’ case, the district court’s conclusion on the appropriateness of injunctive relief is sound. From the previous discussion on the plaintiffs’ standing, it should be evident that plaintiffs face a “likelihood of substantial and immediate irreparable injury.”
  <em>
   <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>,
  </em>
  461 U.S. at Ill, 103 S.Ct. at 1670 (quoting
  <em>
   <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">O’Shea</a></span>,
  </em>
  at 502, 94 S.Ct. at 679). The likelihood that class members will suffer prospective injury is buttressed not only by the defendants’ past conduct but also by the defendants’ avowed future intent.
 </p>
<p id="b1426-13">
  The district court’s conclusion that the remedies at law are inadequate is also sound. As the Supreme Court stated in rejecting the application of the exclusionary rule in deportation hearings, the deterrent value of the rule “is undermined by the availability of alternative remedies for institutional practices by the INS” in contravention of the Fourth Amendment.
  <em>
   INS v. Lopez-Mendoza,
  </em>
  — U.S.-, <span class="citation" data-id="9429772"><a href="/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/#3488" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Lopez-Mendoza">104 S.Ct. 3479, 3488</a></span>, <span class="citation" data-id="9429772"><a href="/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Lopez-Mendoza">82 L.Ed.2d 778</a></span> (1984). In particular, “[T]he possibility of declaratory relief against the agency thus offers a means for challenging the validity of INS practices, when standing requirements for bringing such an action can be met.”
  <em>
   Id.
  </em>
  104 S.Ct. at 3488.
 </p>
<p id="b1426-16">
  The only other remedy at law available to the class is an action for damages.
  <a class="footnote" href="#fn17" id="fn17_ref">
   17
  </a>
  For various reasons the district court found that damages were not available to the individual class representatives. The plaintiffs have not appealed this ruling nor has the INS asserted that damages constituted an adequate alternative remedy at law for plaintiffs individually or as a class. The high likelihood that the violations will recur absent issuance of an injunction counsels in favor of equitable rather than legal relief. In addition, the district court certified this suit as a class under Rule 23(b)(2), which literally permits only class applications for injunctive or declaratory relief.
  <a class="footnote" href="#fn18" id="fn18_ref">
   18
  </a>
<em>
   See
  </em>
  Fed. R.Civ.P. 23(b)(2).
 </p>
<p id="b1426-17">
  2.
 </p>
<p id="b1426-18">
  The INS further contends that the injunction is overbroad. We reject those challenges to the breadth of the injunction unsuccessfully raised in the district court. We decline to express any opinion on any overbreadth claim not originally addressed
  <span citation-index="1" class="star-pagination" label="1331"> 
   *1331
   </span>
  to the district court. Given the district court’s extensive experience with the facts and litigants, sound principles of judicial administration indicate that any further challenges to the scope of the injunction be directed initially to the jurisdiction of the district court.
 </p>
<p id="b1427-5">
  The amended injunction has three separate components barring: (a) warrantless entries of farm dwellings to search or arrest unless the officers have “clear[] consent” or probable cause; (b) warrantless arrests or searches of migrant farm housing residents unless based on probable cause; and (c) “stopping, detaining, and interrogating [class members] by force, threats of force or a command based upon official authority” absent a warrant, probable cause, or reasonable suspicion based on articulable fact that the person is an alien illegally within the United States. The injunction does expressly permit, however, the nondetentive interrogation of suspected aliens concerning their lawful presence in the United States.
  <em>
   <span class="citation" data-id="1481919"><a href="/opinion/1481919/laduke-v-nelson/" aria-description="Citation for case: LaDuke v. Nelson">LaDuke</a></span>,
  </em>
  560 P.Supp. at 165.
 </p>
<p id="b1427-6">
  According to the INS, the first component of the injunction is overbroad because it allegedly bars consensual searches. This argument was previously made in the district court after the issuance of the original injunction, and any ambiguity on this matter was clarified by the amended injunction. Under the amended injunction, clearly consensual searches are expressly permitted. The first component of the injunction is directed to farm housing entries. If anything, this component’s • simple language overstates the bounds of the INS’s authority to enter housing units with or without a warrant. In sum, however, we think the plain language of the first component provides ample flexibility for INS searches while preserving class members’ reasonable expectations of privacy.
 </p>
<p id="b1427-7">
  The INS finds the second component of the injunction legally “unremarkable” but claims it would cast a chill on officer performance because they are not fully conversant in the legal standards for searches and seizures. We sympathize with the INS’s educational task in keeping its officers abreast of the developments in the fast-moving world of the Fourth Amendment. When the Chief Patrol Agent for the Spokane Sector testified in the district court, however, he stated that house-to-house searches of farm dwellings would not be permitted under INS policy without individualized suspicion as to each searched dwelling. The testimony of his agents, on the other hand, indicated that house-to-house searches without information as to specific dwellings was a standard practice. Consequently, we cannot affix the entire blame for the educational difficulties of the INS solely on the prolix language of the numerous judicial interpretations of the Fourth Amendment. We find the plain language of the injunction’s second component sufficiently clear to convey the Fourth Amendment’s core commands to all who wish to listen.
 </p>
<p id="b1427-9">
  The third injunctive proscription is challenged by the INS because it bars detentive stops without articulable suspicion of both alienage and illegal presence in the United States. For reasons previously explained, in this nonborder context the Fourth Amendment requires at least articulable suspicion of both alienage and unlawful presence for a detentive stop. The government’s overbreadth claim completely ignores the language of the injunction’s third component, which permits nondetentive interrogations as to illegal presence based solely on reasonable belief of alienage.
 </p>
<p id="b1427-10">
  Lest there remain any dotibts, the amended injunction as it-.currently stands does not infringe upon the legitimate use of law enforcement practices within the migrant worker farm housing community in the Spokane Sector. As the district court stated in the course of the trial, none of the parties disputed the legitimate enforcement needs of the INS within this community. As the district court found, however, the use of ranch checks by the INS in the Spokane Sector cannot be viewed as casual encounters between residents and law enforcement. We agree with the district court’s conclusion that
  <span citation-index="1" class="star-pagination" label="1332"> 
   *1332
   </span>
  farm checks, as described by the witnesses, run afoul of the Fourth Amendment.
 </p>
<p id="b1428-4">
  D.
 </p>
<p id="b1428-5">
  The bulk of the INS’s certification contentions are merely adjuncts to the INS’s challenges to class standing. Nonetheless, assuming that the propriety of the district court’s certification decision has been placed at issue by the government on appeal, the district court did not abuse its discretion in certifying the plaintiff class.
  <em>
   See Moore v. Hughes Helicopters, Inc.,
  </em>
  <span class="citation" data-id="419216"><a href="/opinion/419216/tommie-y-moore-plaintiff-appellant-v-hughes-helicopters-inc-a/#479" aria-description="Citation for case: Tommie Y. MOORE, Plaintiff-Appellant, v. HUGHES...">708 F.2d 475, 479</a></span> (9th Cir.1983) (standard of review for class certification is “abuse of discretion or impermissible legal criteria”).
 </p>
<p id="b1428-6">
  Rule 23(a) sets forth the four minimum requirements of (a) numerosity (b) commonality (c) typicality, and (d) adequate representation. Fed.R.Civ.P. 23(a). Only commonality and typicality have been questioned by the INS. The position of the INS is without merit. Plainly, the constitutionality of the INS ranch check technique as it affects the defined class is a “question of law or fact common to the class.”
  <em>
   <span class="citation" data-id="419216"><a href="/opinion/419216/tommie-y-moore-plaintiff-appellant-v-hughes-helicopters-inc-a/" aria-description="Citation for case: Tommie Y. MOORE, Plaintiff-Appellant, v. HUGHES...">Id.</a></span>
  </em>
</p>
<p id="b1428-7">
<em>
   Of
  </em>
  course, if material variations exist as to the law or facts involved with individual class member injuries, then the commonality requirement would not be met.
  <em>
   In re Hotel Telephone Charges, <span class="citation" data-id="320513"><a href="/opinion/320513/in-re-hotel-telephone-charges/#89" aria-description="Citation for case: In Re HOTEL TELEPHONE CHARGES">500 F.2d 86, 89</a></span>
  </em>
  (9th Cir.1974). The district court’s ultimate factual finding of a uniform pattern of INS conduct, upon which the court premised its legal conclusions, reinforces the court’s pri- or conclusion that there are no material differences among individual class grievances. Accordingly, the district court can hardly be held to have abused its discretion in finding commonality for class claims.
 </p>
<p id="b1428-8">
  Similarly, the typicality of the class representative’s claims was vigorously litigated in the district court and the district court did not abuse its discretion in finding that the named plaintiffs’ claims are typical of those raised by the class as to the propriety of injunctive relief. The minor differences in the manner in which the representative’s Fourth Amendment rights were violated
  <a class="footnote" href="#fn19" id="fn19_ref">
   19
  </a>
  does not render their claims atypical of those of the class. We agree that the representatives’ claims fairly encompass the Fourth Amendment claims of the remaining class members.
 </p>
<p id="b1428-11">
  Finally,
  <em>
   citing Betts v. Reliable Collection Agency, Ltd.,
  </em>
  <span class="citation" data-id="8913981"><a href="/opinion/8924619/betts-v-reliable-collection-agency-ltd/#1005" aria-description="Citation for case: Betts v. Reliable Collection Agency, Ltd.">659 F.2d 1000, 1005</a></span> (9th Cir.1981) (after certification court may divide class into subclasses), the INS contends that the class certified by the district court is actually composed of discrete subclasses which require separate treatment by the court. We reject the INS’s attempt to raise the subclass issue for the first time on appeal. The district court did not abuse its discretion in failing to address sua sponte the possibility of subclasses under Federal Rule of Civil Procedure 23(c)(4)(B) when the subclass proponent fails to request such a procedure,
  <em>
   see United States Parole Commission v. Geraghty, 445 U.S.
  </em>
  388, 408, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#1214" aria-description="Citation for case: United States Parole Commission v. Geraghty">100 S.Ct. 1202, 1214</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/" aria-description="Citation for case: United States Parole Commission v. Geraghty">63 L.Ed.2d 479</a></span> (1980), and no obvious basis for subclass creation, such as conflicting interests within the class, is apparent on the record.
 </p>
<p id="b1428-12">
  E.
 </p>
<p id="b1428-13">
  After two days of hearings the district court awarded plaintiffs’ counsel approximately $300,000 in attorney fees and costs under the Equal Access to Justice Act (“EAJA”), <span class="citation no-link">28 U.S.C. § 2412</span>. The fee application of the various counsel for plaintiff class was premised on the availability of fees under either § 2412(b) or § 2412(d)(1)(A). The distrit court held plaintiffs’ counsel entitled to fees under both provisions. The district court then rigorously analyzed the various fee applications, awarded reasonable hourly fees of $100 to Mr. Fox and $125 for Mr. Ginsberg, and applied a 20% multiplier based on the risk that the attorneys’ work on such a protracted case would go uncompensated.
 </p>
<p id="b1429-4">
<span citation-index="1" class="star-pagination" label="1333"> 
   *1333
   </span>
  The government now challenges both statutory bases of entitlement under the EAJA found by the court below. The standard of review applied in this circuit to a district court’s ruling on attorney fees is abuse of discretion.
  <em>
   Foster v. Tourtellotte,
  </em>
  <span class="citation" data-id="8916719"><a href="/opinion/8926932/foster-v-tourtellotte/#1110" aria-description="Citation for case: Foster v. Tourtellotte">704 F.2d 1109, 1110-11</a></span> (9th Cir.). Nonetheless, issues regarding the proper interpretation of the EAJA are subject to
  <em>
   de novo
  </em>
  review.
  <em>
   Lauritzen v. Lehman,
  </em>
  <span class="citation" data-id="8922565"><a href="/opinion/8932408/lauritzen-v-lehman/#553" aria-description="Citation for case: Lauritzen v. Lehman">736 F.2d 550, 553</a></span> (9th Cir.1984).
 </p>
<p id="b1429-5">
  The district court rejected plaintiffs’ claim to fees under § 2412(b) which had been raised under a “common law benefit” theory. The district court’s alternative finding of fee entitlement under the analogous “statute” prong of § 2412(b) is no longer consistent with Ninth Circuit precedent.
  <em>
   See Lauritzen v. Lehman,
  </em>
  <span class="citation" data-id="8922565"><a href="/opinion/8932408/lauritzen-v-lehman/#553" aria-description="Citation for case: Lauritzen v. Lehman">736 F.2d 550, 553-59</a></span> (9th Cir.1984).
 </p>
<p id="b1429-6">
  The district court’s separate ruling on entitlement under <span class="citation no-link">28 U.S.C. § 2412</span>(d)(1)(A), however, did not constitute an abuse of discretion. The court’s finding that plaintiffs were prevailing parties
  <a class="footnote" href="#fn20" id="fn20_ref">
   20
  </a>
  has not been challenged on appeal. The INS largely contests the district court’s finding that the government’s position was not “substantially justified.”
  <a class="footnote" href="#fn21" id="fn21_ref">
   21
  </a>
</p>
<p id="b1429-7">
  Following
  <em>
   Rawlings v. Heckler,
  </em>
  <span class="citation" data-id="8918963"><a href="/opinion/8928923/rawlings-v-heckler/" aria-description="Citation for case: Rawlings v. Heckler">725 F.2d 1192</a></span> (9th Cir.1984), the district court found the government’s position lacked a reasonable basis in law and fact because the law regarding the need for articulable suspicion was clear, the defendants failed to follow both the law and their own policies, and the INS needlessly protracted the litigation by denying routine INS practices. The district court, having a unique perspective earned from tireless effort in this protracted litigation, did not abuse its discretion in finding an absence of substantial justification.
 </p>
<p id="b1429-8">
  Finally, the INS charges that the hourly fee award ($100 and $125) to class counsel unreasonably exceeded the normal fee of $75 per hour under the EAJA. The EAJA authorizes exceeding the $75 “cap” on attorney fees based on either a cost of living increase or a “special factor, such as the limited availability of qualified attorneys for the proceedings.” 28 .U.S.C. § 2412(d)(2)(A)(ii). The court did not abuse its discretion in finding a special factor existed for breaching the $75 cap based on expert testimony.
  <em>
   Accord Action on Smoking and Health v. CAB,
  </em>
  <span class="citation" data-id="429382"><a href="/opinion/429382/action-on-smoking-and-health-v-civil-aeronautics-board-action-on-smoking/#219" aria-description="Citation for case: Action on Smoking and Health v. Civil Aeronautics Board,...">724 F.2d 211, 219</a></span> (D.C.Cir.1984). The court relied on a concurring opinion in
  <em>
   Blum v. Stenson,
  </em>
  — U.S. -, <span class="citation" data-id="9429529"><a href="/opinion/111123/blum-v-stenson/" aria-description="Citation for case: Blum v. Stenson">104 S.Ct. 1541</a></span>, <span class="citation" data-id="9429529"><a href="/opinion/111123/blum-v-stenson/" aria-description="Citation for case: Blum v. Stenson">79 L.Ed.2d 891</a></span> (1984), to support the position that the inordinate risk of no fee award was sufficient to justify a multiplier. The contingent nature of fee awards under the EAJA has been held a “special factor” permitting a multiplier.
  <em>
   Action on Smoking and Health v. CAB,
  </em>
  <span class="citation" data-id="429382"><a href="/opinion/429382/action-on-smoking-and-health-v-civil-aeronautics-board-action-on-smoking/" aria-description="Citation for case: Action on Smoking and Health v. Civil Aeronautics Board,...">724 F.2d 211</a></span>-218 (D.C.Cir.1984) (citing
  <em>
   Copeland v. Marshall,
  </em>
  <span class="citation" data-id="9467613"><a href="/opinion/387362/dolores-j-copeland-individually-and-on-behalf-of-the-class-of-all-others/#905" aria-description="Citation for case: Dolores J. Copeland, Individually and on Behalf of the...">641 F.2d 880, 905-08</a></span> (D.C.Cir.1980) (en banc));
  <em>
   Coleman v. Block,
  </em>
  <span class="citation" data-id="1869791"><a href="/opinion/1869791/coleman-v-block/#1421" aria-description="Citation for case: Coleman v. Block">589 F.Supp. 1411, 1421</a></span> (D.N.Dak.1984);
  <em>
   Local 3-98, Int. Woodworkers of America v. Donovan,
  </em>
  <span class="citation" data-id="1450572"><a href="/opinion/1450572/local-3-98-international-woodworkers-of-america-v-donovan/#717" aria-description="Citation for case: Local 3-98, International Woodworkers of America v. Donovan">580 F.Supp. 714, 717</a></span> (N.D.Cal.1984). Consequently, the district court properly took this special factor into account in adjusting the plaintiffs’ attorney fees.
 </p>
<p id="b1429-13">
  IV.
 </p>
<p id="b1429-14">
  We affirm the district court’s issuance of an amended injunction and the award of fees and costs.
 </p>





















<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b1418-7">
   . We note that
   <em>
    United States v. Maybusher,
   </em>
   <span class="citation" data-id="436162"><a href="/opinion/436162/united-states-v-frank-j-maybusher/" aria-description="Citation for case: United States v. Frank J. Maybusher">735 F.2d 366</a></span>, 371 n. 1 (9th Cir.1984), holds that we exercise de novo review over district court determinations on the mixed question of fact and law regarding the presence of articulable facts justifying a detentive stop. Rather than reconcile the conflicting signals we have received from our past precedent, we have carefully reviewed the evidence and found the district court’s finding of no articulable suspicion correct under both de novo and the clearly erroneous standards.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b1418-8">
   . Similarly, we recognize that some post
   <em>
    -McConney
   </em>
   case law suggests that a Fourth Amendment "seizure” conclusion is reviewable under the clearly erroneous standard.
   <em>
    See United States v. Moreno,
   </em>
   <span class="citation" data-id="9472553"><a href="/opinion/440411/united-states-v-vidal-moreno/#537" aria-description="Citation for case: United States v. Vidal Moreno">742 F.2d 532, 537</a></span> (9th Cir.1984) (Wallace, J., concurring). Reviewed under either standard, we reach the same conclusion as the district court.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b1418-9">
   . The INS offers a general contention that because some class representatives, Charles La-Duke, for example, are not currently engaged in farm labor or residing in farm dwellings, they are not proper class representatives and therefore they lack standing to bring this suit. Although immaterial, plaintiffs assert that the class representatives will continue to reside in migrant worker housing. The INS argument as to the mootness of class representative claims was correctly rejected by the district court. The class was originally certified by Judge McNichols on October 13, 1981. When the district court redefined the class, largely to narrow the definition of the affected dwellings, it found the class representatives still remaining in the case were representative as of the original certification date.
  </p>
<p id="b1418-17">
   The district court based its 1981 finding that the class representatives would still represent the class on two alternate grounds. First, the court found the representatives’ individual circumstances within the class action rule for constitutional violations "capable of repetition, yet evading review" pronounced in
   <em>
    Sosna v. Iowa,
   </em>
   <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/#399" aria-description="Citation for case: Sosna v. Iowa">419 U.S. 393, 399-400</a></span>, <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/#557" aria-description="Citation for case: Sosna v. Iowa">95 S.Ct. 553, 557</a></span>, <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/" aria-description="Citation for case: Sosna v. Iowa">42 L.Ed.2d 532</a></span> (1975). In the alternative, the district court followed Ninth Circuit precedent which permits class representatives to prosecute class claims even though their individual claims become moot after certification.
   <em>
    Kuahulu v. Employers Insurance of Wausau,
   </em>
   <span class="citation" data-id="346935"><a href="/opinion/346935/bernard-kuahulu-for-himself-and-for-all-others-similarly-situated-v/" aria-description="Citation for case: Bernard Kuahulu, for Himself and for All Others Similarly...">557 F.2d 1334</a></span> (9th Cir.1977).
  </p>
<p id="b1418-18">
   The basis for allowing class representatives to continue despite mooted individual claims lies in the notion that, upon certification, the class acquires an independent legal status,
   <em>
    Kuahulu,
   </em>
   <span class="citation" data-id="346935"><a href="/opinion/346935/bernard-kuahulu-for-himself-and-for-all-others-similarly-situated-v/#1336" aria-description="Citation for case: Bernard Kuahulu, for Himself and for All Others Similarly...">557 F.2d at 1336</a></span>, for which the representative acts in a role "analogous to the private attorney general.”
   <em>
    United States Parole Commission v. Geraghty,
   </em>
   <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#403" aria-description="Citation for case: United States Parole Commission v. Geraghty">445 U.S. 388, 403</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/#1212" aria-description="Citation for case: United States Parole Commission v. Geraghty">100 S.Ct. 1202, 1212</a></span>, <span class="citation" data-id="9427834"><a href="/opinion/110228/united-states-parole-commission-v-geraghty/" aria-description="Citation for case: United States Parole Commission v. Geraghty">63 L.Ed.2d 479</a></span> (1980). Given the transience of the migrant labor force,
   <em>
    see also Ger-stein v. Pugh,
   </em>
   <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U.S. 103</a></span>, 111 n. 11, <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span>, 861 n. 11, <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">43 L.Ed.2d 54</a></span> (1975) ("constant existence of a class of persons suffering the deprivation is certain”), and the district court’s finding that the representatives would continue to press the class claims with diligence, both of the district court’s alternative grounds for rejecting the INS’s mootness challenge to the class representatives’ status are correct.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b1419-8">
   . This prudential standing limit has not been directly raised by the INS. Plaintiff class members are not attempting to assert the rights of nonparties to this litigation. Rather, they press and seek vindication of their personal rights. Moreover, in the context of this class action we find the “underlying justifications” for this prudential limitation absent.
   <em>
    See Singleton v. Wulff,
   </em>
   <span class="citation" data-id="9426552"><a href="/opinion/109530/singleton-v-wulff/#114" aria-description="Citation for case: Singleton v. Wulff">428 U.S. 106, 114</a></span>, <span class="citation" data-id="9426552"><a href="/opinion/109530/singleton-v-wulff/#2874" aria-description="Citation for case: Singleton v. Wulff">96 S.Ct. 2868, 2874</a></span>, <span class="citation" data-id="9426552"><a href="/opinion/109530/singleton-v-wulff/" aria-description="Citation for case: Singleton v. Wulff">49 L.Ed.2d 826</a></span> (1976) (Blackmun, J.).
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b1419-9">
   .
   <em>
    See generally
   </em>
   Note,
   <em>
    The Generalized Grievance Restriction: Prudential Restraint or Constitutional Mandate,
   </em>
   70 Geo.L.J. 1157 (1982) (discussing contours of the generalized grievance standing rule as a prudential limit).
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b1419-10">
   . We reserve ruling on whether remedial standing under
   <em>
    <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
   </em>
   is a prudential or constitutional standing limitation because the characterization would have no effect on the disposition of this case.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b1419-15">
   . We would prefer, however, to follow the Supreme Court’s post
   <em>
    -Lyons
   </em>
   standing analysis in
   <em>
    Kolender v. Lawson,
   </em>
   <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">461 U.S. 352</a></span>, <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">103 S.Ct. 1855</a></span>, <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">75 L.Ed.2d 903</a></span> (1983), and simply determine whether there is a "credible threat” that the plaintiffs will again be subject to ranch checks.
   <em>
    Id.
   </em>
   103 S.Ct. at 1857 n. 3.
   <em>
    <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">Kolender</a></span>
   </em>
   involved a facial challenge to a California identification statute under which plaintiff had repeatedly been arrested.
   <em>
    <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">Kolender</a></span>
   </em>
   also sought injunctive relief. Nonetheless, we think
   <em>
    <span class="citation" data-id="9429162"><a href="/opinion/110916/city-of-los-angeles-v-lyons/" aria-description="Citation for case: City of Los Angeles v. Lyons">Lyons</a></span>
   </em>
   "cannot be so easily confined to [its] facts,” 461 U.S. at 108-09, 103 S.Ct. at 1668, and therefore will give careful attention to its teachings.
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b1420-7">
   . Obviously, proof of past injury, especially of a repetitive character, is not immaterial to the issue of likely recurrence.
   <em>
    See Kolender v. Lawson,
   </em>
   <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">461 U.S. 352</a></span>, 355 n. 3, <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">103 S.Ct. 1855</a></span>, 1857 n. 3, <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">75 L.Ed.2d 903</a></span> (1983);
   <em>
    Lewis v. Tally,
   </em>
   <span class="citation" data-id="8800747"><a href="/opinion/8816245/lewis-v-tully/#641" aria-description="Citation for case: Lewis v. Tully">99 F.R.D. 632, 641</a></span> (N.D.Ill.1983).
  </p>
</div><div class="footnote" id="fn9" label="9">
<a class="footnote" href="#fn9_ref">
   9
  </a>
<p id="b1421-7">
   . As the Court made clear in
   <em>
    Almeida-Sanchez,
   </em>
   the statutory authority bestowed on the INS must comply with the Constitution and courts should narrowly construe the INS’s statutory search and seizure authority consistent with Fourth Amendment precedent.
   <em>
    Almeida-Sanchez,
   </em>
   <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#272" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U.S. 266 at 272</a></span>, <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#2539" aria-description="Citation for case: Almeida-Sanchez v. United States">93 S.Ct. 2535 at 2539</a></span>, <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">37 L.Ed.2d 596</a></span> (1973).
  </p>
</div><div class="footnote" id="fn10" label="10">
<a class="footnote" href="#fn10_ref">
   10
  </a>
<p id="b1421-9">
   .
   <em>
    See O’Shea v. Littleton,
   </em>
   <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/" aria-description="Citation for case: O&#x27;Shea v. Littleton">414 U.S. at 494</a></span> n. 3, 94 S.Ct. at 675 n. 3. Although
   <em>
    <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">Rizzo</a></span>
   </em>
   did involve a class action, the Court declined to address the relevance of this fact.
   <em>
    Rizzo,
   </em>
   432 U.S. at 373, <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/#605" aria-description="Citation for case: Rizzo v. Goode">96 S.Ct. at 605</a></span>. The
   <em>
    <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">Rizzo</a></span>
   </em>
   opinion found no “pattern” of police misconduct sufficient to justify the detailed affirmative injunction ordered by the lower courts to rectify the undifferentiated allegations of police abuse.
   <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/#374" aria-description="Citation for case: Rizzo v. Goode"><em>
    Id.
   </em>
   at 374</a></span>, 96 S.Ct. at 605.
  </p>
</div><div class="footnote" id="fn11" label="11">
<a class="footnote" href="#fn11_ref">
   11
  </a>
<p id="b1422-5">
   . These ranch checks are not border area searches and the INS has not contended that these area control operations are conducted under its border control authority. Moreover, the Fourth Amendment does not permit the INS to differentiate on a per se basis in the privacy accorded different stocks of housing. Without question, the Fourth Amendment was intended to protect the resident’s, not the INS’s, expectation of privacy.
  </p>
<p id="b1422-13">
   The poorest man may in his cottage bid defiance to all the forces of the Crown. It may be
   <span citation-index="1" class="star-pagination" label="1327"> 
    *1327
    </span>
   frail; its roof may shake; the wind may blow through it; the storm may enter; the rain may enter; but the King of England cannot enter — all his force dares not cross the threshold of the ruined tenement!
  </p>
<p id="A6y">
<em>
    Miller
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#307" aria-description="Citation for case: Miller v. United States">357 U.S. 301, 307</a></span>, <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#1195" aria-description="Citation for case: Miller v. United States">78 S.Ct. 1190, 1195</a></span>, <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">2 L.Ed.2d 1332</a></span> (1958) (expressing principle articulated by William Pitt).
  </p>
</div><div class="footnote" id="fn12" label="12">
<a class="footnote" href="#fn12_ref">
   12
  </a>
<p id="b1423-9">
   . The INS does challenge the finding that the ranch checks are conducted without any individualized suspicion as to the presence of illegal aliens in the checked units. The district court’s finding to the contrary is amply supported in the record through the testimony of the INS Border Patrol agents.
  </p>
<p id="b1423-10">
   As the district court recognized, the Border Patrol Agents themselves presented conflicting evidence on the amount of information they obtained prior to initiating farm and ranch checks. For example, Agent Turner testified he never had any specific information in advance that identified a particular suspect or dwelling for a ranch check since at least 1974. Others indicated that they relied on notoriety or the "reputation” of a particular camp. Supervising Agent Minyard echoed these comments, noting that he normally did not refer to records of prior apprehensions in determining whether to initiate a check, and conceding that any information the Sector offices might receive from complaining witnesses was systematically destroyed and unavailable even after this suit was filed. He admitted that the decision to initiate ranch checks was sometimes based on no specific information and sometimes just on proximity to a migrant worker housing unit. Even in those situations where agents claimed to be acting on prior anonymous tips, the tips often were vague references to geographic areas or farm locations. Finally, the agents testified that it was INS policy to conduct complete sweeps of all community residences, with or without information as to specific residences. For example, Agent Minyard, on whom many of the other agents relied exclusively for information to commence a check, testified that a sole factor in approaching a particular residence was whether the lights were on.
  </p>
</div><div class="footnote" id="fn13" label="13">
<a class="footnote" href="#fn13_ref">
   13
  </a>
<p id="b1424-8">
   . For example, one agent testified that his "customary procedure" for obtaining consent was to grasp the belt of the person responding to the door. In another incident, class member Sally Wilson testified that on one occasion she was awakened by the flashlight of an agent, standing in her bedroom doorway, who then attempted to pull the blanket off her bed to ascertain if she was alone. In another episode, Ms. Wilson was making a pie in her kitchen when INS agents fanned around her residence, stationed themselves at all windows and doors, and peered into her home. As she was staring at the face of an agent looking through the window, the agent yelled that everything was okay because it was an “American family.” These and other incidents demonstrate that the atmosphere surrounding these early morning or nocturnal visitations is indeed intimidating to those residing in the farm housing units.
  </p>
</div><div class="footnote" id="fn14" label="14">
<a class="footnote" href="#fn14_ref">
   14
  </a>
<p id="b1424-12">
   .
   <em>
    See
   </em>
   104 S.Ct. at 1764 n. 6. The Court was only able to find one piece of evidence, contained in a deposition, that agents attempted to restrain a worker from leaving the factory. According to the Court, this was "an ambiguous, isolated event.”
  </p>
</div><div class="footnote" id="fn15" label="15">
<a class="footnote" href="#fn15_ref">
   15
  </a>
<p id="b1425-8">
   .
   <em>
    Id.
   </em>
   at 227, 93 S.Ct. at 2047;
   <em>
    United States v. Cawley,
   </em>
   <span class="citation" data-id="9467110"><a href="/opinion/382245/united-states-v-ralph-collins-cawley/#1349" aria-description="Citation for case: United States v. Ralph Collins Cawley">630 F.2d 1345, 1349</a></span> (9th Cir.1980).
  </p>
</div><div class="footnote" id="fn16" label="16">
<a class="footnote" href="#fn16_ref">
   16
  </a>
<p id="b1425-12">
   . While the district court’s link between Mexican culture and an inherent fear of uniformed officers is a questionable stereotype, it was not the sole basis for the court’s decision.
  </p>
</div><div class="footnote" id="fn17" label="17">
<a class="footnote" href="#fn17_ref">
   17
  </a>
<p id="b1426-9">
   . We do not mean to suggest that injunctive relief is limited to those situations in which the exclusionary rule is unavailable.
  </p>
</div><div class="footnote" id="fn18" label="18">
<a class="footnote" href="#fn18_ref">
   18
  </a>
<p id="b1426-19">
   . The complaint sought certification under Rule 23(b)(1)(A) but the court did not certify such a class.
  </p>
</div><div class="footnote" id="fn19" label="19">
<a class="footnote" href="#fn19_ref">
   19
  </a>
<p id="b1428-9">
   . LaDuke's privacy was violated by a flashlight search of his tent and a physical trespass while the Garcias’ privacy was violated only through trespass. Other class members suffered similar violations of their Fourth Amendment rights.
   <em>
    Cf.
   </em>
   Deposition of Ramon Castillo (unauthorized physical entry by agents, lights shined through windows).
  </p>
</div><div class="footnote" id="fn20" label="20">
<a class="footnote" href="#fn20_ref">
   20
  </a>
<p id="b1429-9">
   . The district court rejected INS arguments that the dismissal of some defendants, denial of a preliminary injunction, failure to settle the case, and limited nature of the injunction issued operated to deprive plaintiffs of prevailing party status.
  </p>
</div><div class="footnote" id="fn21" label="21">
<a class="footnote" href="#fn21_ref">
   21
  </a>
<p id="b1429-16">
   . The court also found no "special circumstances” rendered an award unjust and the INS has not contested this finding.
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Lefkowitz v. Turley.md  (`case`, 5 assertions)

### content_page

```
---
title: "Lefkowitz v. Turley"
type: case
citation: "414 U.S. 70 (1973)"
parallel_cite: "94 S. Ct. 316; 38 L. Ed. 2d 274"
neutral_cite: 1973 U.S. LEXIS 132
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1973
date_decided: 1973-11-19
docket: 72-331
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1973-11-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Lefkowitz v. Turley
  varies_by_point: false
  scope_note: "Good law; extends the Garrity/Gardner principle to independent contractors and fixes the rule that the State must grant immunity rather than demand a waiver."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108882/lefkowitz-v-turley/"
  cluster_id: 108882
  opinion_id: 108882
  identity_checked: true
homes:
  - page: "[[Public-Employee Compelled Statements (Garrity)]]"
    role: "Key — Progeny / Refinement"
related: ["[[Garrity v. New Jersey]]", "[[Gardner v. Broderick]]", "[[Kalkines v. United States]]"]
aliases: []
tags: ["case", "fifth-amendment", "self-incrimination", "public-employee", "garrity", "immunity", "contractors"]
holding: "A State may not compel a person (employee or contractor) to choose between waiving Fifth Amendment immunity and losing state employment or contracts; it may compel testimony about official functions only by granting use-and-derivative-use immunity, never by insisting on a waiver."
lake:
  record_id: Lefkowitz v. Turley
  status: verified
  projected_at: 2026-07-06
---

# Lefkowitz v. Turley

*414 U.S. 70 (1973)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
New York statutes provided that any person doing business with the State who, when called before a grand jury, refused to waive immunity or to answer questions about his state contracts would have his existing contracts cancelled and be disqualified from public contracting for five years. Two architects who performed state work were subpoenaed before a grand jury, refused to waive immunity, and sued to enjoin the statutes as violating the Fifth Amendment. A three-judge district court held the statutes unconstitutional, and the New York Attorney General appealed.

## Issue
Whether a State may, consistent with the Fifth Amendment, require a contractor (or public employee) either to waive his privilege against self-incrimination and testify or to forfeit his existing state contracts and be disqualified from future state work.

## Rule
The State may compel duty-related answers, but only under immunity: "[G]iven adequate immunity, the State may plainly insist that employees either answer questions under oath about the performance of their job or suffer the loss of employment." — 414 U.S. at 84. ^pin-84

What it may not do is demand a waiver: "[T]he State may not insist that appellees waive their Fifth Amendment privilege against self-incrimination and consent to the use of the fruits of the interrogation in any later proceedings brought against them. Rather, the State must recognize what our cases hold: that answers elicited upon the threat of the loss of employment are compelled and inadmissible in evidence. Hence, if answers are to be required in such circumstances States must offer to the witness whatever immunity is required to supplant the privilege and may not insist that the employee or contractor waive such immunity." — *Id.* at 84–85. ^pin-84a

## Application
The New York statutes confronted the architects with the very choice the Fifth Amendment forbids: waive immunity (exposing their testimony and its fruits to criminal use) or lose their contracts and be barred from state work for five years. The State could have compelled their testimony about their state contracts by granting use-and-derivative-use immunity, but instead it demanded a waiver of the privilege as the price of keeping their livelihood. Because answers extracted under that threat are compelled and inadmissible, conditioning contracts on a waiver violated the Fifth Amendment.

## Conclusion
The statutes were unconstitutional, and the judgment was affirmed. *Lefkowitz* confirms that a government may compel testimony about official functions only by supplying immunity, and may never penalize a person for refusing to surrender the privilege itself.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Lefkowitz* is good law; it extends [[Garrity v. New Jersey]] and [[Gardner v. Broderick]] beyond employees to independent contractors and states the controlling immunity-not-waiver rule that the federal [[Kalkines v. United States]] warning implements.

## Appears on
- [[Public-Employee Compelled Statements (Garrity)]] — *Key — Progeny / Refinement*

## Sources
- *Lefkowitz v. Turley*, 414 U.S. 70 (1973) — https://www.courtlistener.com/opinion/108882/lefkowitz-v-turley/ — pinpoints: 84–85.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "78bf7ddd185972df", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "414 U.S. 70 (1973)", "court": "U.S. Supreme Court", "neutral_cite": "1973 U.S. LEXIS 132", "official_citation_present": true, "parallel_cite": "94 S. Ct. 316; 38 L. Ed. 2d 274", "title": "Lefkowitz v. Turley", "year": "1973"}}
{"assertion_id": "24061a259198029f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A State may not compel a person (employee or contractor) to choose between waiving Fifth Amendment immunity and losing state employment or contracts; it may compel testimony about official functions only by granting use-and-derivative-use immunity, never by insisting on a waiver.", "title": "Lefkowitz v. Turley"}}
{"assertion_id": "d5693042522c825e", "dimension": "support", "kind": "home_role", "locator": {"home": "Public-Employee Compelled Statements (Garrity)"}, "payload": {"home": "Public-Employee Compelled Statements (Garrity)", "role": "Key — Progeny / Refinement", "title": "Lefkowitz v. Turley"}}
{"assertion_id": "0bb29d36b447d265", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Lefkowitz v. Turley"}}
{"assertion_id": "276c477944fdbe85", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1973-11-19", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Lefkowitz v. Turley", "field_i_validity": "good_law", "scope_note": "Good law; extends the Garrity/Gardner principle to independent contractors and fixes the rule that the State must grant immunity rather than demand a waiver.", "title": "Lefkowitz v. Turley", "varies_by_point": "false"}}
```

### lake record — Lefkowitz v. Turley

```json
{
  "schema_version": "s2.v1",
  "record_id": "Lefkowitz v. Turley",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Lefkowitz v. Turley",
    "case_name_short": "Lefkowitz",
    "case_name_full": "LEFKOWITZ, ATTORNEY GENERAL OF NEW YORK, Et Al. v. TURLEY Et Al.",
    "input_case_name": "Lefkowitz v. Turley",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1973-11-19",
    "year": 1973,
    "docket": "72-331",
    "cluster_id": 108882,
    "lead_opinion_id": 108882,
    "sibling_ids": [
      108882
    ],
    "absolute_url": "/opinion/108882/lefkowitz-v-turley/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8991929,
        "score": 20,
        "case_name": "Lefkowitz v. Turley"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "414 U.S. 70",
      "volume": "414",
      "reporter": "U.S.",
      "page": "70",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "94 S. Ct. 316",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "316",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "38 L. Ed. 2d 274",
        "volume": "38",
        "reporter": "L. Ed. 2d",
        "page": "274",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1973 U.S. LEXIS 132",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "132",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "414 U.S. 70",
        "volume": "414",
        "reporter": "U.S.",
        "page": "70",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 S. Ct. 316",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "316",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "38 L. Ed. 2d 274",
        "volume": "38",
        "reporter": "L. Ed. 2d",
        "page": "274",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. LEXIS 132",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "132",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "414 U.S. 70",
    "official_selection": {
      "court_class": "scotus",
      "selected": "414 U.S. 70",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-84",
      "page": null,
      "quote": "--- # Lefkowitz v. Turley *414 U.S. 70 (1973)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background New York statutes provided that any person doing business with the State who, when called before a grand jury, refused to waive immunity or to answer questions about his state contracts would have his existing contracts cancelled and be disqualified from public contracting for five years. Two architects who performed state work were subpoenaed before a grand jury, refused to waive immunity, and sued to enjoin the statutes as violating the Fifth Amendment. A three-judge district court held the statutes unconstitutional, and the New York Attorney General appealed. ## Issue Whether a State may, consistent with the Fifth Amendment, require a contractor (or public employee) either to waive his privilege against self-incrimination and testify or to forfeit his existing state contracts and be disqualified from future state work. ## Rule The State may compel duty-related answers, but only under immunity:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-84a",
      "page": null,
      "quote": "[T]he State may not insist that appellees waive their Fifth Amendment privilege against self-incrimination and consent to the use of the fruits of the interrogation in any later proceedings brought against them. Rather, the State must recognize what our cases hold: that answers elicited upon the threat of the loss of employment are compelled and inadmissible in evidence. Hence, if answers are to be required in such circumstances States must offer to the witness whatever immunity is required to supplant the privilege and may not insist that the employee or contractor waive such immunity.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1973-11-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Lefkowitz v. Turley",
    "varies_by_point": false,
    "scope_note": "Good law; extends the Garrity/Gardner principle to independent contractors and fixes the rule that the State must grant immunity rather than demand a waiver.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Gideon",
          "cluster_id": 4632199,
          "cite": [
            "2019 Ohio 2482",
            "130 N.E.3d 357"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Heffington v. Moser",
          "cluster_id": 4531554,
          "cite": [
            "192 A.3d 900",
            "238 Md. App. 509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gregory Wayne Powell",
          "cluster_id": 4348676,
          "cite": [
            "161 Idaho 774",
            "391 P.3d 659",
            "2017 WL 587254",
            "2017 Ida. App. LEXIS 17"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People in re L.K",
          "cluster_id": 4247631,
          "cite": [
            "2016 COA 112",
            "410 P.3d 664"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Von Behren",
          "cluster_id": 3202148,
          "cite": [
            "822 F.3d 1139",
            "2016 U.S. App. LEXIS 8567",
            "2016 WL 2641270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jesus J. Pena v. State",
          "cluster_id": 3199326,
          "cite": [
            "508 S.W.3d 599",
            "2016 WL 1702219",
            "2016 Tex. App. LEXIS 4360"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Turner",
          "cluster_id": 2723970,
          "cite": [
            "300 Kan. 662",
            "333 P.3d 155",
            "2014 Kan. LEXIS 499"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Brent Vreeland",
          "cluster_id": 803377,
          "cite": [
            "684 F.3d 653",
            "2012 WL 2477578",
            "2012 U.S. App. LEXIS 13307"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ex Parte Dangelo",
          "cluster_id": 2537141,
          "cite": [
            "339 S.W.3d 143",
            "2010 WL 5118650"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Spielbauer v. County of Santa Clara",
          "cluster_id": 5608087,
          "cite": [
            "45 Cal. 4th 704",
            "199 P.3d 1125",
            "88 Cal. Rptr. 3d 590",
            "28 I.E.R. Cas. (BNA) 1254",
            "2009 Cal. LEXIS 1010"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Aguilera v. Baca",
          "cluster_id": 1390016,
          "cite": [
            "510 F.3d 1161",
            "27 I.E.R. Cas. (BNA) 31",
            "2007 U.S. App. LEXIS 29804",
            "2007 WL 4531990"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cleveland Board of Education v. Loudermill",
          "cluster_id": 111372,
          "cite": [
            "84 L. Ed. 2d 494",
            "105 S. Ct. 1487",
            "470 U.S. 532",
            "1985 U.S. LEXIS 68",
            "1 I.E.R. Cas. (BNA) 424",
            "53 U.S.L.W. 4306",
            "118 L.R.R.M. (BNA) 3041"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
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
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baxter v. Palmigiano",
          "cluster_id": 109429,
          "cite": [
            "47 L. Ed. 2d 810",
            "96 S. Ct. 1551",
            "425 U.S. 308",
            "1976 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arnett v. Kennedy",
          "cluster_id": 109008,
          "cite": [
            "40 L. Ed. 2d 15",
            "94 S. Ct. 1633",
            "416 U.S. 134",
            "1974 U.S. LEXIS 125"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
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
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
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
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
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
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chavez v. Martinez",
          "cluster_id": 127927,
          "cite": [
            "155 L. Ed. 2d 984",
            "123 S. Ct. 1994",
            "538 U.S. 760",
            "2003 U.S. LEXIS 4274"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maness v. Meyers",
          "cluster_id": 109130,
          "cite": [
            "42 L. Ed. 2d 574",
            "95 S. Ct. 584",
            "419 U.S. 449",
            "1975 U.S. LEXIS 20"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of Comm'rs, Wabaunsee Cty. v. Umbehr",
          "cluster_id": 118059,
          "cite": [
            "135 L. Ed. 2d 843",
            "116 S. Ct. 2342",
            "518 U.S. 668",
            "1996 U.S. LEXIS 4262",
            "10 Fla. L. Weekly Fed. S 124",
            "64 U.S.L.W. 4682",
            "96 Cal. Daily Op. Serv. 4821",
            "11 I.E.R. Cas. (BNA) 1393",
            "96 Daily Journal DAR 7732"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilkie v. Robbins",
          "cluster_id": 145705,
          "cite": [
            "168 L. Ed. 2d 389",
            "127 S. Ct. 2588",
            "551 U.S. 537",
            "2007 U.S. LEXIS 8513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lefkowitz v. Cunningham",
          "cluster_id": 109683,
          "cite": [
            "53 L. Ed. 2d 1",
            "97 S. Ct. 2132",
            "431 U.S. 801",
            "1977 U.S. LEXIS 19"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Allen v. Illinois",
          "cluster_id": 111745,
          "cite": [
            "92 L. Ed. 2d 296",
            "106 S. Ct. 2988",
            "478 U.S. 364",
            "1986 U.S. LEXIS 130",
            "54 U.S.L.W. 4966"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garner v. United States",
          "cluster_id": 109400,
          "cite": [
            "47 L. Ed. 2d 370",
            "96 S. Ct. 1178",
            "424 U.S. 648",
            "1976 U.S. LEXIS 138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mandujano",
          "cluster_id": 109442,
          "cite": [
            "48 L. Ed. 2d 212",
            "96 S. Ct. 1768",
            "425 U.S. 564",
            "1976 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Selective Service System v. Minnesota Public Interest Research Group",
          "cluster_id": 111260,
          "cite": [
            "82 L. Ed. 2d 632",
            "104 S. Ct. 3348",
            "468 U.S. 841",
            "1984 U.S. LEXIS 151",
            "52 U.S.L.W. 5140"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'Hare Truck Service, Inc. v. City of Northlake",
          "cluster_id": 118060,
          "cite": [
            "135 L. Ed. 2d 874",
            "116 S. Ct. 2353",
            "518 U.S. 712",
            "1996 U.S. LEXIS 4263",
            "64 U.S.L.W. 4694",
            "10 Fla. L. Weekly Fed. S 115",
            "11 I.E.R. Cas. (BNA) 1377",
            "96 Cal. Daily Op. Serv. 4812",
            "96 Daily Journal DAR 7746"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Asplin v. Mueller",
          "cluster_id": 1389666,
          "cite": [
            "687 P.2d 1329",
            "1984 Colo. App. LEXIS 1157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heller v. District of Columbia",
          "cluster_id": 614652,
          "cite": [
            "670 F.3d 1244",
            "399 U.S. App. D.C. 314",
            "2011 U.S. App. LEXIS 20130",
            "2011 WL 4551558"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sonya Evette Singleton, National Association of Criminal Defense Lawyers, Amicus Curiae",
          "cluster_id": 760928,
          "cite": [
            "165 F.3d 1297",
            "1999 Colo. J. C.A.R. 590",
            "1999 U.S. App. LEXIS 222",
            "1999 WL 6469"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salinas v. Texas",
          "cluster_id": 903977,
          "cite": [
            "186 L. Ed. 2d 376",
            "133 S. Ct. 2174",
            "2013 U.S. LEXIS 4697",
            "570 U.S. 178",
            "81 U.S.L.W. 4467",
            "24 Fla. L. Weekly Fed. S 294",
            "2013 WL 2922119"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillip Fantone v. Fred Latini",
          "cluster_id": 2779958,
          "cite": [
            "780 F.3d 184",
            "2015 U.S. App. LEXIS 2470",
            "2015 WL 669290"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Avant v. Clifford",
          "cluster_id": 1549504,
          "cite": [
            "341 A.2d 629",
            "67 N.J. 496",
            "1975 N.J. LEXIS 205"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karl P. Zinn",
          "cluster_id": 76088,
          "cite": [
            "321 F.3d 1084",
            "2003 WL 328925"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Richard Aichele",
          "cluster_id": 566407,
          "cite": [
            "941 F.2d 761",
            "91 Cal. Daily Op. Serv. 6180",
            "91 Daily Journal DAR 9211",
            "1991 U.S. App. LEXIS 16620",
            "1991 WL 138118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lefkowitz v. Turley:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108882) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDUzOTkzNjAwMDAwJnM9MTI3ODkxJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108882%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 11,
        "triage_snippet_classified": 189
      },
      "lane2_top_cited": {
        "query": "cites:(108882)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzUmcz03MzIyMiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28108882%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108882)",
        "reviewed": 22,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 22,
        "triage_read": 0,
        "triage_snippet_classified": 22
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108882)",
    "indexed_citing_opinions": 663,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108882,
        "count": 663,
        "count_source": "search"
      }
    ],
    "citation_count": 1103,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/lefkowitz-v-turley.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgwNTQxMjMmcz05MzY3NTAyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108882%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108882,
        "cited_id": 85566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 100474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 105095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 105363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 106075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 107248,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 107336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 107738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 107739,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 108238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 2339910,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108882,
        "cited_id": 2499246,
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
    "date_created": "2026-07-05T10:47:20Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:47:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:47:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:51:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:47:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Lefkowitz v. Turley

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b223-13">
  Mr. Justice White
 </author>
<p id="Aos">
  delivered the opinion of the Court.
 </p>
<p id="b223-14">
  New York General Municipal Law §§ 103-a and 103-b and New York Public Authorities Law §§ 2601 and 2602 require public contracts to provide that if a contractor refuses to waive immunity or to answer questions when called to testify concerning his contracts with the State or any of its subdivisions, his existing contracts may be canceled and he shall be disqualified from further transactions with the State for five years.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  In addition to
  <span citation-index="1" class="star-pagination" label="72"> 
   *72
   </span>
  specifying these contract terms, the statutes require disqualification from contracting with public authorities upon failure of any person to waive immunity or to
  <span citation-index="1" class="star-pagination" label="73"> 
   *73
   </span>
  answer questions with respect to his transactions with the State or its subdivisions. The issue in this case is whether these sections are consistent with the Four
  <span citation-index="1" class="star-pagination" label="74"> 
   *74
   </span>
  teenth Amendment insofar as it makes applicable to the States the Fifth Amendment privilege against compelled self-incrimination.
 </p>
<p id="b227-4">
<span citation-index="1" class="star-pagination" label="75"> 
   *75
   </span>
  I
 </p>
<p id="b227-5">
  Appellees are two architects licensed by the State of New York. They were summoned to testify before a grand jury investigating various charges of conspiracy,
  <span citation-index="1" class="star-pagination" label="76"> 
   *76
   </span>
  bribery, and larceny. They were asked, but refused, to sign waivers of immunity, the effect of which would have been to waive their right not to be compelled in a criminal case to be a witness against themselves. They were then excused and the District Attorney, as directed by law, notified various contracting authorities of appellees’ conduct and called attention to the applicable disqualification statutes. Appellees thereupon brought this action alleging that their existing contracts and future contracting privileges were threatened and asserted that the pertinent statutory provisions were violative of the constitutional privilege against compelled self-incrimination. A three-judge District Court was convened and declared the four statutory provision's at issue unconstitutional under the Fourteenth and Fifth Amendments, <span class="citation" data-id="2339910"><a href="/opinion/2339910/turley-v-lefkowitz/" aria-description="Citation for case: Turley v. Lefkowitz">342 F. Supp. 544</a></span> (WDNY 1972). We noted probable jurisdiction, <span class="citation multiple-matches"><a href="/c/U.%20S./410/924/">410 U. S. 924</a></span> (1973). The State appealed pursuant to <span class="citation no-link">28 U. S. C. § 1253</span>. We affirm the judgment of the District Court.
 </p>
<p id="b229-8">
<span citation-index="1" class="star-pagination" label="77"> 
   *77
   </span>
  ) — i
 </p>
<p id="b229-3">
  The Fifth Amendment provides that no person shall be compelled in any criminal case to be a witness against himself.” The Amendment not only protects the individual against being involuntarily called as a witness against himself in a criminal prosecution but also privileges him not to answer official questions put to him in any other proceeding, civil or criminal, formal or informal, where the answers might incriminate him in future criminal proceedings.
  <em>
   McCarthy
  </em>
  v.
  <em>
   Arndstein,
  </em>
  <span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/#40" aria-description="Citation for case: McCarthy v. Arndstein">266 U. S. 34, 40</a></span> (1924), squarely held that
 </p>
<blockquote id="b229-4">
  “[t]he privilege is not ordinarily dependent upon the nature of the proceeding in which the testimony is sought or is to be used. It applies alike to civil and criminal proceedings, wherever the answer might tend to subject to criminal responsibility him who gives it. The privilege protects a mere witness as fully as it does one who is also a party defendant.”
 </blockquote>
<p id="b229-5">
  In this respect,
  <em>
   McCarthy
  </em>
  v.
  <em>
   <span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/" aria-description="Citation for case: McCarthy v. Arndstein">Arndstein</a></span>
  </em>
  reflected the settled view in this Court. The object of the Amendment “was to insure that a person should not be compelled, when acting as a witness in any investigation, to give testimony which might tend to show that he himself had committed a crime.”
  <em>
   Counselman
  </em>
  v.
  <em>
   Hitchcock,
  </em>
  <span class="citation no-link">142 U. S. 647</span>, 562 (1892). See also
  <em>
   Bram
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="94789"><a href="/opinion/94789/hall-v-united-states/#542" aria-description="Citation for case: Hall v. United States">168 U. S. 632, 542-543</a></span> (1897);
  <em>
   Brown
  </em>
  v.
  <em>
   Walker,
  </em>
  <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/" aria-description="Citation for case: Brown v. Walker">161 U. S. 591</a></span> (1896);
  <em>
   Boyd
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#634" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 634, 637-638</a></span> (1886);
  <em>
   United States
  </em>
  v.
  <em>
   Saline Bank,
  </em>
  <span class="citation" data-id="85566"><a href="/opinion/85566/the-united-states-v-the-saline-bank-of-virginia-john-webster-and-others/" aria-description="Citation for case: The United States v. The Saline Bank of Virginia, John...">1 Pet. 100</a></span> (1828). This is the rule that is now applicable to the States.
  <em>
   Malloy
  </em>
  v.
  <em>
   Hogan,
  </em>
  <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964). “It must be considered irrelevant that the petitioner was a witness in a statutory inquiry and not a defendant in a criminal prosecution, for it has long been settled that the privilege protects witnesses in similar federal inquiries.”
  <span citation-index="1" class="star-pagination" label="78"> 
   *78
   </span>
<span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#11" aria-description="Citation for case: Malloy v. Hogan"><em>
   Id.,
  </em>
  at 11</a></span>. In any of these contexts, therefore, a witness protected by the privilege may rightfully refuse to answer unless and until he is protected at least against the use of his compelled answers and evidence derived therefrom in any subsequent criminal case in which he is a defendant.
  <em>
   Kastigar
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441</a></span> (1972). Absent such protection, if he is nevertheless compelled to answer, his answers are inadmissible against him in a later criminal prosecution.
  <em>
   Bram
  </em>
  v.
  <em>
   United States, supra; Boyd
  </em>
  v.
  <em>
   United States, supra.
  </em>
</p>
<p id="b230-5">
  Against this background, there is no room for urging that the Fifth Amendment privilege is inapplicable simply because the issue arises, as it does here, in the context of official inquiries into the job performance of a public contractor. Surely, the ordinary rule is that the privilege is available to witnesses called before grand juries as these appellee architects were.
  <em>
   Hale
  </em>
  v.
  <em>
   Henkel,
  </em>
  <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#66" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 66</a></span> (1906).
 </p>
<p id="b230-6">
  It is- true that the State has a strong, legitimate interest in maintaining the integrity of its civil service and of its transactions with independent contractors furnishing a wide range of goods and services; and New York would have it that this interest is sufficiently strong to override the privilege. The suggestion is that the State should be able to interrogate employees and contractors about their job performance without regard to the Fifth Amendment, to discharge those who refuse to answer or to waive the privilege by waiving the immunity to which they would otherwise be entitled, and to use any incriminating answers obtained in subsequent criminal prosecutions. But claims of overriding interests are not unusual in Fifth Amendment litigation and they have not fared well.
 </p>
<p id="b230-7">
  In
  <em>
   McCarthy
  </em>
  v.
  <em>
   <span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/" aria-description="Citation for case: McCarthy v. Arndstein">Arndstein, supra,</a></span>
  </em>
  the United States insisted that because of the strong public interest in marshaling and distributing assets of bankrupts, the
  <span citation-index="1" class="star-pagination" label="79"> 
   *79
   </span>
  Fifth Amendment should not protect a bankrupt during the official examinations mandated by the Bankruptcy Act. That position did not prevail. The bankrupt’s testimony could be had, but only if he were afforded sufficient immunity to supplant the privilege. And long before
  <em>
   McCarthy
  </em>
  v.
  <em>
   <span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/" aria-description="Citation for case: McCarthy v. Arndstein">Arndstein</a></span>,
  </em>
  the Court recognized that without the compelled testimony of knowledgeable and perhaps implicated witnesses, the enforcement of the transportation laws “would become impossible,” but nevertheless proceeded on a basis that witnesses must be granted adequate immunity if their evidence was to be compelled.
  <em>
   Brown
  </em>
  v.
  <em>
   Walker,
  </em>
  <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#610" aria-description="Citation for case: Brown v. Walker">161 U. S., at 610</a></span>. Similarly, the enforcement of the antitrust laws against private corporations was at stake in
  <em>
   Hale
  </em>
  v.
  <em>
   <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/" aria-description="Citation for case: Hale v. Henkel">Henkel, supra,</a></span>
  </em>
  but immunity was essential to command the testimony of individual witnesses. Also, it would be difficult to overestimate the importance of the interest of the States in the enforcement of their ordinary criminal laws; but the price for incriminating answers from third-party witnesses is sufficient immunity to satisfy the imperatives of the Fifth Amendment privilege against compelled self-incrimination. Finally, in almost the very context here involved, this Court has only recently held that employees of the State do not forfeit their constitutional privilege and that they may be compelled to respond to questions about the performance of their duties but only if their answers cannot be used against them in subsequent criminal prosecutions.
  <em>
   Garrity
  </em>
  v.
  <em>
   New Jersey,
  </em>
  <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">385 U. S. 493</a></span> (1967);
  <em>
   Gardner
  </em>
  v.
  <em>
   Broderick,
  </em>
  <span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">392 U. S. 273</a></span> (1968);
  <em>
   Sanitation Men
  </em>
  v.
  <em>
   Sanitation Comm’r,
  </em>
  <span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">392 U. S. 280</a></span> (1968).
 </p>
<p id="b231-5">
  Ill
 </p>
<p id="b231-6">
  In
  <em>
   Garrity
  </em>
  v.
  <em>
   <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">New Jersey</a></span>,
  </em>
  certain police officers were summoned to an inquiry being conducted by the Attorney General concerning the fixing of traffic tickets.
  <span citation-index="1" class="star-pagination" label="80"> 
   *80
   </span>
  They were asked questions following warnings that if they did not answer they would be removed from office and that anything they said might be used against them in any criminal proceeding. No immunity of any kind was offered or available under state law. The questions were answered and the answers later used over their objections, in their prosecutions for conspiracy. The Court held that “the protection of the individual under the Fourteenth Amendment against coerced statements prohibits use in subsequent criminal proceedings of statements obtained under threat of removal from office, and that it extends to all, whether they are policemen or other members of our body politic.” <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/#500" aria-description="Citation for case: Garrity v. New Jersey">385 U. S., at 500</a></span>. The Court also held that in the context of threats of removal from office the act of responding to interrogation was not voluntary and was not an effective waiver of the privilege against self-incrimination, the Court conceding, however, that there might be other situations “where one who is anxious to make a clean breast of the whole affair volunteers the information.”
  <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/#499" aria-description="Citation for case: Garrity v. New Jersey"><em>
   Id.,
  </em>
  at 499</a></span>.
 </p>
<p id="b232-5">
  The issue in
  <em>
   Gardner
  </em>
  v.
  <em>
   <span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">Broderick, supra,</a></span>
  </em>
  was whether the State might discharge a police officer who, after he was summoned before a grand jury to testify about the performance of his official duties and was advised of his right against compulsory self-incrimination, then refused to waive that right as requested by the State. Conceding that appellant could be discharged for refusing to answer questions about the performance of his official duties, if not required to waive immunity, the Court held that the officer could not be terminated, as he was, for refusing to waive his constitutional privilege. Although under
  <em>
   <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Garrity</a></span>
  </em>
  any waiver executed may have been invalid and any answers elicited inadmissible in evidence, the State did not purport to recognize as much and instead
  <span citation-index="1" class="star-pagination" label="81"> 
   *81
   </span>
  attempted to coerce a waiver on the penalty of loss of employment. The “testimony was demanded before the grand jury in part so that it might be used to prosecute him, and not solely for the purpose of securing an accounting of his performance of his public trust.” 392 U. S., at 279. Hence, the State’s statutory provision requiring his dismissal for his refusal to waive immunity could not stand.
 </p>
<p id="b233-4">
  The companion case,
  <em>
   Sanitation Men
  </em>
  v.
  <em>
   Sanitation Comm’r, supra,
  </em>
  was to the same effect. Here again, public employees were officially interrogated and advised that refusal to answer and sign waivers of immunity would lead to dismissal. Here again, the Court held that the State presented the employees with “a choice between surrendering their constitutional rights or their jobs,” 392 U. S., at 284, although clearly they would “subject themselves to dismissal if they refuse to account for their performance of their public trust, after proper proceedings, which do not involve an attempt to coerce them to relinquish their constitutional rights.”
  <em>
   Id.,
  </em>
  at 285.
 </p>
<p id="b233-5">
  These cases, and their predecessors, ultimately rest on a reconciliation of the well-recognized policies behind the privilege of self-incrimination,
  <em>
   Murphy
  </em>
  v.
  <em>
   Waterfront Comm’n,
  </em>
  <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#55" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 55</a></span> (1964), and the need of the State, as well as the Federal Government, to obtain information “to assure the effective functioning of government,”
  <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#93" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor"><em>
   id.,
  </em>
  at 93</a></span> (White, J., concurring). Immunity is required if there is to be “rational accommodation between the imperatives of the privilege and the legitimate demands of government to compel citizens to testify.”
  <em>
   Kastigar
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#446" aria-description="Citation for case: Kastigar v. United States">406 U. S., at 446</a></span>. It is in this sense that immunity
  <span citation-index="1" class="star-pagination" label="82"> 
   *82
   </span>
  statutes have “become part of our constitutional fabric.”
  <em>
   Ullmann
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421245"><a href="/opinion/105363/ullmann-v-united-states/#438" aria-description="Citation for case: Ullmann v. United States">350 U. S. 422, 438</a></span> (1956).
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b234-5">
  We agree with the District Court that
  <em>
   Garrity, Gardner,
  </em>
  and
  <em>
   <span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">Sanitation Men</a></span>
  </em>
  control the issue now before us. The State sought to interrogate appellees about their transactions with the State and to require them to furnish possibly incriminating testimony by demanding that they waive their immunity and by disqualifying them as public contractors when they refused. It seems to us that the State intended to accomplish what
  <em>
   <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Garrity</a></span>
  </em>
  specifically prohibited — to compel testimony that had not been immunized. The waiver sought by the State, under threat of loss of contracts, would have been no less compelled than a direct request for the testimony without resort to the waiver device. A waiver secured under threat of substantial economic sanction cannot be
  <span citation-index="1" class="star-pagination" label="83"> 
   *83
   </span>
  termed voluntary. As already noted,
  <em>
   Oarrity
  </em>
  specifically rejected the claim of an effective waiver when the policemen in that case, in the face of possible discharge, proceeded to answer the questions put to them. <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/#498" aria-description="Citation for case: Garrity v. New Jersey">385 U. S., at 498</a></span>. The same holding is implicit in both
  <em>
   <span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">Gardner</a></span>
  </em>
  and
  <em>
   <span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">Sanitation Men</a></span>.
  </em>
</p>
<p id="b235-5">
  The State nevertheless asserts that whatever may be true of state employees, a different rule is applicable to public contractors such as architects. Because independent contractors may not depend entirely on transactions with the State for their livelihood, it is suggested that disqualification from contracting with official agencies for a period of five years is neither compulsion within the meaning of the Fifth Amendment nor a forbidden penalty for refusing to answer questions put to them about their job performance. But we agree with the District Court that “the plaintiffs’ disqualification from public contracting for five years as a penalty for asserting a constitutional privilege is violative of their Fifth Amendment rights.” <span class="citation" data-id="2339910"><a href="/opinion/2339910/turley-v-lefkowitz/#549" aria-description="Citation for case: Turley v. Lefkowitz">342 F. Supp., at 549</a></span>. We fail to see a difference of constitutional magnitude between the threat of job loss to an employee of the State, and a threat of loss of contracts to a contractor.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b235-6">
  If the argument is that the cost to a contractor is small in comparison to the cost to an employee of losing his job, the premise must be that it is harder for a state employee to find employment in the private sector, than it is for an architect. An architect lives off his contracting fees as surely as a state employee lives off his salary, and fees and salaries may be equally hard to come by in the private sector after sanctions have been taken by
  <span citation-index="1" class="star-pagination" label="84"> 
   *84
   </span>
  the State. In some sense the plight of the architect may be worse, for under the New York statutes it may be that any firm that employs him thereafter will also be subject to contract cancellation and disqualification.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  A significant infringement of constitutional rights cannot be justified by the speculative ability of those affected to cover the damage.
 </p>
<p id="b236-5">
  IV
 </p>
<p id="b236-6">
  We should make clear, however, what we have said before. Although due regard for the Fifth Amendment forbids the State to compel incriminating answers from its employees and contractors that may be used against them in criminal proceedings, the Constitution permits that very testimony to be compelled if neither it nor its fruits are available for such use.
  <em>
   Kastigar
  </em>
  v.
  <em>
   United States, supra.
  </em>
  Furthermore, the accommodation between the interest of the State and the Fifth Amendment requires that the State have means at its disposal to secure testimony if immunity is supplied and testimony is still refused. This is recognized by the power of the courts to. compel testimony, after a grant of immunity, by use of civil contempt and coerced imprisonment.
  <em>
   Shillitani
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="107248"><a href="/opinion/107248/shillitani-v-united-states/" aria-description="Citation for case: Shillitani v. United States">384 U. S. 364</a></span> (1966). Also, given adequate immunity, the State may plainly insist that employees either answer questions under oath about the performance of their job or suffer the loss of employment. By like token, the State may insist that the architects involved in this case either respond to relevant inquiries about the performance of their contracts or suffer cancellation of current relationships and disqualification from contracting with public agencies for an appropriate time in the future. But the State may not insist that appellees
  <span citation-index="1" class="star-pagination" label="85"> 
   *85
   </span>
  waive their Fifth Amendment privilege against self-incrimination and consent to the use of the fruits of the interrogation in any later proceedings brought against them. Rather, the State must recognize what our cases hold: that answers elicited upon the threat of the loss of employment are compelled and inadmissible in evidence. Hence, if answers are to be required in such circumstances States must offer to the witness whatever immunity is required to supplant the privilege and may not insist that the employee or contractor waive such immunity.
 </p>
<p id="b237-6">
  ~ ,
  <em>
   Affirmed.
  </em>
</p>
<author id="b237-7">
  Mr. Justice Brennan,
 </author>
<p id="Amjp">
  with whom Mr. Justice Douglas and Mr. Justice Marshall join.
 </p>
<p id="b237-8">
  I join the Court’s opinion in all respects but one. It is my view that immunity which permits testimony to be compelled “if neither it nor its fruits are available for . . . use” in criminal proceedings does not satisfy the privilege against self-incrimination. “I believe that the Fifth Amendment’s privilege against self-incrimination requires that any jurisdiction that compels a man to incriminate himself grant him absolute immunity under its laws from prosecution for any transaction revealed in that testimony.”
  <em>
   Piccirillo
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="9424403"><a href="/opinion/108238/piccirillo-v-new-york/#562" aria-description="Citation for case: Piccirillo v. New York">400 U. S. 548, 562</a></span> (1971) (Brennan, J., dissenting.)
 </p>




<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b223-15">
   N. Y. Gen. Munic. Law §§ 103-a and 103-b (Supp. 1973-1974) provide:
  </p>
<blockquote id="b223-16">
   Section 103-a. Ground for cancellation of contract by municipal corporations and fire districts:
  </blockquote>
<blockquote id="b223-17">
<em>
    “A
   </em>
   clause shall be inserted in all specifications or contracts made or awarded by a municipal corporation or any public department, agency or official thereof on or after the first day of July, nineteen
   <span citation-index="1" class="star-pagination" label="72"> 
    *72
    </span>
   hundred fifty-nine or by a fire district or any agency or official thereof on or after the first day of September, nineteen hundred sixty, for work or services performed or to be performed, or goods sold or to be sold, to provide that upon the refusal of a person, when called before a grand jury, head of a state department, temporary state commission or other state agency, . . . head of a city department, or other city agency, which is empowered to compel the attendance of witnesses and examine them under oath, to testify in an investigation concerning any transaction or contract had with the state, any political subdivision thereof, a public authority or with any public department, agency or official of the state or of any political subdivision thereof or of a public authority, to sign a waiver of immunity against subsequent criminal prosecution or to answer any relevant question concerning such transaction or contract,
  </blockquote>
<blockquote id="b224-6">
   “(a) such person, and any firm, partnership or corporation of which he is a member, partner, director or officer shall be disqualified from thereafter selling to or submitting bids to or receiving awards from or entering into any contracts with any municipal corporation, or firé district, or any public department, agency or official thereof, for goods, work or services, for a period of five years after such refusal, and to provide also that
  </blockquote>
<blockquote id="b224-7">
   “(b) any and all contracts made with any municipal corporation or any public department, agency or official thereof on or after the first day of July, nineteen hundred fifty-nine or with any fire district or any agency or official thereof on or after the first day of September, nineteen hundred sixty, by such person, and by any firm, partnership, or corporation of which he is a member, partner, director or officer may be cancelled or terminated by the municipal corporation or fire district without incurring any penalty or damages on account of such cancellation or termination, but any monies owing by the municipal corporation or fire district for goods delivered or work done prior to the cancellation or termination shall be paid.
  </blockquote>
<blockquote id="b224-8">
   “The provisions of this section as in force and effect prior to the first day of September, nineteen hundred sixty, shall apply to specifications or contracts made or awarded by a municipal corpora
   <span citation-index="1" class="star-pagination" label="73"> 
    *73
    </span>
   tion on or after .the first day of July, nineteen hundred fifty-nine, but prior to the first day of September, nineteen hundred sixty.”
  </blockquote>
<p id="b225-6">
   Section 103-b. Disqualification to contract with municipal corporations and fire districts:
  </p>
<blockquote id="b225-7">
   “Any person, who, when called before a grand jury, head of a state department, temporary state commission or other state agency, . . . head of a city department or other city agency, which is empowered to compel the attendance of witnesses and examine them under oath, to testify in an investigation concerning any transaction or contract had with the state, any political subdivision thereof, a public authority, or with a public department, agency or official of the state or of any political subdivision thereof or of a public authority, refuses to sign a waiver of immunity against subsequent criminal prosecution or to answer any relevant question concerning such transaction or contract, and any firm, partnership or corporation of which he is a member, partner, director or officer shall be disqualified from thereafter selling to or submitting bids to or receiving awards from or entering into any contracts with any municipal corporation or fire district, or with any public department, agency or official thereof, for goods, work or services, for a period of five years after such refusal or until a disqualification shall be removed pursuant to the provisions of section one hundred three-c of this article.
  </blockquote>
<blockquote id="b225-8">
   “It shall be the duty of the officer conducting the investigation before the grand jury, the head of a state department, the chairman of the temporary state commission or other state agency,... . the head of a city department or other city agency before which the refusal occurs to send notice of such refusal, together with the names of any firm, partnership, or corporation of which the person so refusing is known to be a member, partner, officer or director, to the commissioner of transportation of the state of New York and the appropriate departments, agencies and officials of the state, political subdivisions thereof or public authorities with whom the person so refusing and any firm, partnership or corporation of which he is a member, partner, director or officer, is known to have a contract. However, when such refusal occurs before a body other than a grand jury, notice of refusal shall not be sent for a period of ten days after such refusal occurs. Prior to the expiration of
   <span citation-index="1" class="star-pagination" label="74"> 
    *74
    </span>
   this ten day period, any person, firm, partnership or corporation which has become liable to the cancellation or termination of a contract or disqualification to contract on account of such refusal may commence a special proceeding at a special term of the supreme court, held within the judicial district in which the refusal occurred, for an order determining whether the questions in response to which the refusal occurred were relevant and material to the inquiry. Upon the commencement of such proceeding, the sending of such notice of refusal to answer shall be subject to order of the court in which the proceeding was brought in a manner and on such terms as the court may deem just. If a proceeding is not brought within ten days, notice of refusal shall thereupon be sent as provided herein.”
  </blockquote>
<p id="b226-6">
   N. Y. Pub. Auth. Law §§2601 and 2602 (Supp. 1973-1974) provide:
  </p>
<p id="b226-7">
   Section 2601. Ground for cancellation of contract by public authority:
  </p>
<blockquote id="b226-8">
   “A clause shall be inserted in all specifications or contracts hereafter made or awarded by any public authority or by any official of any public authority created by the state or any political subdivision, for work or services performed or to be performed or goods sold or to be sold, to provide that upon the refusal by a person, when called before a grand jury, head of a state department, temporary state commission or other state agency,... head of a city department, or other city agency, which is empowered to compel the attendance of witnesses and examine them under oath, to testify in an investigation concerning any transaction or contract had with the state, any political subdivision thereof, a public authority or with any. public department, agency or official of the state or of any political subdivision thereof or of a public authority, to sign a waiver of immunity against subsequent criminal prosecution or to answer any relevant question concerning such transaction or contract,
  </blockquote>
<blockquote id="b226-9">
   “(a) such person, and any firm, partnership or corporation of which he is a member, partner, director or officer shall be disqualified from thereafter selling to or submitting bids to or receiving awards from or entering into any contracts with any public authority or official thereof, for goods, work or services, for a period of five years after such refusal, and to provide also that
  </blockquote>
<blockquote id="b226-10">
   “(b) any and all contracts made with any public authority or
   <span citation-index="1" class="star-pagination" label="75"> 
    *75
    </span>
   official thereof, since the effective date of this law, by such person and by any firm, partnership or corporation of which he is a member, partner, director or officer may be cancelled or terminated by the public authority without incurring any penalty or damages on account of such cancellation or termination, but any monies owing by the public authority for goods delivered or work done prior to the cancellation or termination shall be paid.”
  </blockquote>
<p id="b227-7">
   Section 2602. Disqualification to contract with public authority:
  </p>
<blockquote id="b227-8">
   “Any person, who, when called before a grand jury, head of a state department, temporary state commission or other state agency, . . . head of a city department, or other city agency, which is empowered to compel the attendance of witnesses and examine them under oath, to testify in an investigation concerning any transaction or contract had with the state, any political subdivision thereof, a public authority or with a public department, agency or official of the state or of any political subdivision thereof or of a public authority, refuses to sign a waiver of immunity against subsequent criminal prosecution or to answer any relevant questions concerning such transaction or contract, and any firm, partnership or corporation, of which he is a member, partner, director, or officer shall be disqualified from thereafter selling to or submitting bids to or receiving awards from or entering into any contracts with any public authority or any official of any public authority created by the state or any political subdivision, for goods, work or services, for a period of five years after such refusal or until a disqualification shall be removed pursuant to the provisions of section twenty-six hundred three of this title.
  </blockquote>
<blockquote id="b227-9">
   “It shall be the duty of the officer conducting the investigation before the grand jury, the head of a state department, the chairman of the temporary state commission or other state agency,... the head of a city department or other city agency before which the refusal occurs to send notice of such refusal, together with the names of any firm, partnership or corporation of which the person so refusing is known to be a member, partner, officer or director, to the commissioner of transportation of the state of New York, or the commissioner of general services as the case may be, and the appropriate
   <span citation-index="1" class="star-pagination" label="76"> 
    *76
    </span>
   departments, agencies and officials of the state, political subdivisions thereof or public authorities with whom the persons [sic] so refusing and any firm, partnership or corporation of which he is a member, partner, director or officer, is known to have a contract. However, when such refusal occurs before a body other than a grand jury, notice of refusal shall not be sent for a period of ten days after such refusal occurs. Prior to the expiration of this ten day period, any person, firm, partnership or corporation which has become liable to the. cancellation or termination of a contract or disqualification to contract on account of such refusal may commence a special proceeding at a special term of the supreme court, held within the judicial district in which the refusal occurred, for an order determining whether the questions in response to which the refusal occurred were relevant and material to the inquiry. Upon the commencement of such proceeding, the sending of such notice of refusal to answer shall be subject to order of the court in which the proceeding was brought in a manner and on such terms as the court may deem just. If a proceeding is not brought within ten days, notice of refusal shall thereupon be sent as provided herein.”
  </blockquote>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b234-6">
   In
   <em>
    Orloff
   </em>
   v.
   <em>
    Willoughby,
   </em>
   <span class="citation" data-id="9420889"><a href="/opinion/105095/orloff-v-willoughby/" aria-description="Citation for case: Orloff v. Willoughby">345 U. S. 83</a></span> (1953), a doctor inducted into the Army was denied a commission as an officer after refusing to divulge whether he was a Communist, as required by a loyalty certificate prescribed for commissioned officers. Instead he asserted his “Federal constitutional privilege” when called upon to answer the question. In holding that the Government was justified in refusing the commission because of the failure to answer, the Court had no occasion to consider whether Orloff would have been exposed to criminal prosecution if he had stated that he was a member of the Communist Party. The case differs significantly from the one before us since the State here asks the architects to affirmatively expose themselves to criminal prosecution by waiving their privilege against self-in crimination, or from
   <em>
    <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Garrity</a></span>,
   </em>
   where the threat of criminal prosecution was apparent both from the nature of the proceeding, and the absence of applicable state immunity statutes.
  </p>
<p id="b234-7">
<em>
    Kimm
   </em>
   v.
   <em>
    Rosenberg,
   </em>
   <span class="citation" data-id="9422018"><a href="/opinion/106075/kimm-v-rosenberg/" aria-description="Citation for case: Kimm v. Rosenberg">363 U. S. 405</a></span> (1960), is also inapposite. The Court there held that an alien whose deportation had been ordered was ineligible for a discretionary order permitting his voluntary departure, because he had failed to establish that he was not affiliated with the Communist Party. .Petitioner’s imminent departure from the country, whether it was voluntary or compelled, obviously made the threat of criminal prosecution on the basis of his answer remote.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b235-7">
   As
   <em>
    <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Garrity</a></span>
   </em>
   succinctly put it: “The option to lose their means of livelihood or to pay the penalty of self-incrimination is the antithesis of free choice to speak out or to remain silent.” <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/#497" aria-description="Citation for case: Garrity v. New Jersey">385 U. S. 493, 497</a></span> (1967).
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b236-7">
   The contract disqualifications apply not only to the person who refuses to waive immunity but also to “any firm, partnership or corporation of which he is a member, partner, director or officer . . . .”
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Lego v. Twomey.md  (`case`, 5 assertions)

### content_page

```
---
title: "Lego v. Twomey"
type: case
citation: "404 U.S. 477 (1972)"
parallel_cite: "92 S. Ct. 619; 30 L. Ed. 2d 618"
neutral_cite: 1972 U.S. LEXIS 100
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1972
date_decided: 1972-01-12
docket: 70-5037
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1972-01-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Lego v. Twomey
  varies_by_point: false
  scope_note: "Good law; the federal constitutional floor for proving confession voluntariness is a preponderance of the evidence. Reaffirmed and extended to Miranda-waiver proof in Colorado v. Connelly."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108429/lego-v-twomey/"
  cluster_id: 108429
  opinion_id: 108429
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Colorado v. Connelly]]", "[[Rogers v. Richmond]]", "[[Brown v. Mississippi]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "fourteenth-amendment", "confessions", "voluntariness", "due-process", "burden-of-proof"]
holding: "The prosecution need prove the voluntariness of a confession only by a preponderance of the evidence, not beyond a reasonable doubt; and a defendant whose voluntariness claim the judge has decided is not entitled to have the jury redetermine voluntariness. States may adopt a higher standard."
lake:
  record_id: Lego v. Twomey
  status: verified
  projected_at: 2026-07-06
---

# Lego v. Twomey

*404 U.S. 477 (1972)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Lego was convicted of armed robbery on evidence that included his confession, which he claimed the police had beaten out of him. At a pretrial [[Common Legal Terms#suppression-hearing|suppression hearing]] the trial judge — applying the then-prevailing practice — found the confession voluntary by a [[Common Legal Terms#preponderance-of-the-evidence|preponderance of the evidence]] and admitted it. Lego argued that the Constitution required the prosecution to prove voluntariness [[Common Legal Terms#beyond-a-reasonable-doubt|beyond a reasonable doubt]], and that he was entitled to have the jury decide voluntariness anew. He sought federal [[Common Legal Terms#habeas-corpus|habeas corpus]] (Twomey was the prison warden).

## Issue
Whether the prosecution must prove a confession's voluntariness [[Common Legal Terms#beyond-a-reasonable-doubt|beyond a reasonable doubt]], and whether a defendant is entitled to have the jury redetermine voluntariness after the judge has ruled it admissible.

## Rule
A [[Common Legal Terms#preponderance-of-the-evidence|preponderance of the evidence]] is the constitutional floor. "[W]hen a confession challenged as involuntary is sought to be used against a criminal defendant at his trial, he is entitled to a reliable and clear-cut determination that the confession was in fact voluntarily rendered. Thus, the prosecution must prove at least by a preponderance of the evidence that the confession was voluntary. Of course, the States are free, pursuant to their own law, to adopt a higher standard." — 404 U.S. at 489. ^pin-489

The Court also held that, the judge having reliably determined voluntariness, the defendant has no constitutional right to have the jury pass on the claim a second time.

## Application
The trial judge had found Lego's confession voluntary under the preponderance standard, and that determination was constitutionally sufficient. *In re Winship*'s beyond-a-reasonable-doubt requirement governs proof of guilt, not the preliminary admissibility question of voluntariness, so the higher standard was not required. And because a judge's reliable voluntariness ruling adequately protects the defendant's rights, Lego was not entitled to relitigate voluntariness before the jury. His [[Common Legal Terms#habeas-corpus|habeas]] petition therefore failed.

## Conclusion
The prosecution need prove voluntariness only by a [[Common Legal Terms#preponderance-of-the-evidence|preponderance of the evidence]], and the defendant has no right to a second, jury determination of voluntariness; the judgment denying [[Common Legal Terms#habeas-corpus|habeas]] relief was affirmed. States remain free to impose a higher burden.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Lego* sets the burden of proof for the voluntariness inquiry developed in the due-process line ([[Brown v. Mississippi]], [[Rogers v. Richmond]]) and for the *Jackson v. Denno* requirement of a separate judicial voluntariness determination. The Court extended the same preponderance standard to proof of a [[Miranda v. Arizona]] waiver and to voluntariness generally in [[Colorado v. Connelly]].

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Lego v. Twomey*, 404 U.S. 477 (1972) — https://www.courtlistener.com/opinion/108429/lego-v-twomey/ — pinpoint: 489.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7b28a9b1736c71d6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "404 U.S. 477 (1972)", "court": "U.S. Supreme Court", "neutral_cite": "1972 U.S. LEXIS 100", "official_citation_present": true, "parallel_cite": "92 S. Ct. 619; 30 L. Ed. 2d 618", "title": "Lego v. Twomey", "year": "1972"}}
{"assertion_id": "4bb5db4553497634", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key — Progeny / Refinement", "title": "Lego v. Twomey"}}
{"assertion_id": "aea070ff8b45e52a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The prosecution need prove the voluntariness of a confession only by a preponderance of the evidence, not beyond a reasonable doubt; and a defendant whose voluntariness claim the judge has decided is not entitled to have the jury redetermine voluntariness. States may adopt a higher standard.", "title": "Lego v. Twomey"}}
{"assertion_id": "9ecc02b6dd98a525", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Lego v. Twomey"}}
{"assertion_id": "d713c8716bd038e1", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1972-01-12", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Lego v. Twomey", "field_i_validity": "good_law", "scope_note": "Good law; the federal constitutional floor for proving confession voluntariness is a preponderance of the evidence. Reaffirmed and extended to Miranda-waiver proof in Colorado v. Connelly.", "title": "Lego v. Twomey", "varies_by_point": "false"}}
```

### lake record — Lego v. Twomey

```json
{
  "schema_version": "s2.v1",
  "record_id": "Lego v. Twomey",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Lego v. Twomey",
    "case_name_short": "Lego",
    "case_name_full": "Lego v. Twomey, Warden",
    "input_case_name": "Lego v. Twomey",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1972-01-12",
    "year": 1972,
    "docket": "70-5037",
    "cluster_id": 108429,
    "lead_opinion_id": 108429,
    "sibling_ids": [
      108429,
      9424726,
      9424727
    ],
    "absolute_url": "/opinion/108429/lego-v-twomey/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8991183,
        "score": 20,
        "case_name": "Lego v. Twomey"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "404 U.S. 477",
      "volume": "404",
      "reporter": "U.S.",
      "page": "477",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "92 S. Ct. 619",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "30 L. Ed. 2d 618",
        "volume": "30",
        "reporter": "L. Ed. 2d",
        "page": "618",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1972 U.S. LEXIS 100",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "100",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "404 U.S. 477",
        "volume": "404",
        "reporter": "U.S.",
        "page": "477",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 S. Ct. 619",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "30 L. Ed. 2d 618",
        "volume": "30",
        "reporter": "L. Ed. 2d",
        "page": "618",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1972 U.S. LEXIS 100",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "100",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "404 U.S. 477",
    "official_selection": {
      "court_class": "scotus",
      "selected": "404 U.S. 477",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-489",
      "page": null,
      "quote": "--- # Lego v. Twomey *404 U.S. 477 (1972)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Lego was convicted of armed robbery on evidence that included his confession, which he claimed the police had beaten out of him. At a pretrial suppression hearing the trial judge \u2014 applying the then-prevailing practice \u2014 found the confession voluntary by a preponderance of the evidence and admitted it. Lego argued that the Constitution required the prosecution to prove voluntariness beyond a reasonable doubt, and that he was entitled to have the jury decide voluntariness anew. He sought federal habeas corpus (Twomey was the prison warden). ## Issue Whether the prosecution must prove a confession's voluntariness beyond a reasonable doubt, and whether a defendant is entitled to have the jury redetermine voluntariness after the judge has ruled it admissible. ## Rule A preponderance of the evidence is the constitutional floor.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1972-01-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Lego v. Twomey",
    "varies_by_point": false,
    "scope_note": "Good law; the federal constitutional floor for proving confession voluntariness is a preponderance of the evidence. Reaffirmed and extended to Miranda-waiver proof in Colorado v. Connelly.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Capote v. State",
          "cluster_id": 10680228,
          "cite": [
            "908 S.E.2d 540",
            "320 Ga. 191"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kasey A. Smith",
          "cluster_id": 4442984,
          "cite": [
            "162 Idaho 878",
            "406 P.3d 890"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re Thomas S. Sharrow",
          "cluster_id": 4489413,
          "cite": [
            "175 A.3d 1236",
            "2017 VT 69"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jalonte Little v. United States",
          "cluster_id": 3153940,
          "cite": [
            "125 A.3d 1119",
            "2015 D.C. App. LEXIS 526"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Feliz",
          "cluster_id": 2817827,
          "cite": [
            "794 F.3d 123",
            "2015 U.S. App. LEXIS 12303",
            "2015 WL 4322298"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "CHARLES S. TURNER,CHRISTOPHER D. TURNER,RUSSELL L. OVERTON, LEVY ROUSE, CLIFTON E. YARBOROUGH, KELVIN D. SMITH, & TIMOTHY CATLETT",
          "cluster_id": 2807493,
          "cite": [
            "116 A.3d 894",
            "2015 D.C. App. LEXIS 262"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Greineder",
          "cluster_id": 6580608,
          "cite": [
            "464 Mass. 580",
            "984 N.E.2d 804",
            "2013 WL 951135",
            "2013 Mass. LEXIS 46"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Allen Murdock",
          "cluster_id": 622650,
          "cite": [
            "399 U.S. App. D.C. 153",
            "667 F.3d 1302",
            "2012 WL 414459",
            "2012 U.S. App. LEXIS 2599"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jelks, 17-08-18 (11-10-2008)",
          "cluster_id": 4009442,
          "cite": [
            "2008 Ohio 5828"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Burnette",
          "cluster_id": 2519721,
          "cite": [
            "535 F. Supp. 2d 772",
            "2007 WL 4911523"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Banford, L-05-1334 (7-27-2007)",
          "cluster_id": 3978076,
          "cite": [
            "2007 Ohio 3821"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kenneth Wayne Simpson v. State",
          "cluster_id": 2933337,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Miller",
          "cluster_id": 6588574,
          "cite": [
            "68 Mass. App. Ct. 835",
            "865 N.E.2d 825",
            "2007 Mass. App. LEXIS 495"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rojas Tapia",
          "cluster_id": 202140,
          "cite": [
            "446 F.3d 1",
            "2006 U.S. App. LEXIS 8803",
            "2006 WL 923990"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tashiri Wayne Williams",
          "cluster_id": 793121,
          "cite": [
            "435 F.3d 1148",
            "2006 U.S. App. LEXIS 2235",
            "2006 WL 213852"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jackson v. Virginia",
          "cluster_id": 110138,
          "cite": [
            "61 L. Ed. 2d 560",
            "99 S. Ct. 2781",
            "443 U.S. 307",
            "1979 U.S. LEXIS 10"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. Sykes",
          "cluster_id": 109717,
          "cite": [
            "53 L. Ed. 2d 594",
            "97 S. Ct. 2497",
            "433 U.S. 72",
            "1977 U.S. LEXIS 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Fulminante",
          "cluster_id": 112566,
          "cite": [
            "113 L. Ed. 2d 302",
            "111 S. Ct. 1246",
            "499 U.S. 279",
            "1991 U.S. LEXIS 1854"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
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
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Matlock",
          "cluster_id": 108967,
          "cite": [
            "39 L. Ed. 2d 242",
            "94 S. Ct. 988",
            "415 U.S. 164",
            "1974 U.S. LEXIS 8"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mullaney v. Wilbur",
          "cluster_id": 109265,
          "cite": [
            "44 L. Ed. 2d 508",
            "95 S. Ct. 1881",
            "421 U.S. 684",
            "1975 U.S. LEXIS 70"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
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
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
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
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patterson v. New York",
          "cluster_id": 109698,
          "cite": [
            "53 L. Ed. 2d 281",
            "97 S. Ct. 2319",
            "432 U.S. 197",
            "1977 U.S. LEXIS 120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Mathiason",
          "cluster_id": 109587,
          "cite": [
            "50 L. Ed. 2d 714",
            "97 S. Ct. 711",
            "429 U.S. 492",
            "1977 U.S. LEXIS 38"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crane v. Kentucky",
          "cluster_id": 111687,
          "cite": [
            "90 L. Ed. 2d 636",
            "106 S. Ct. 2142",
            "476 U.S. 683",
            "1986 U.S. LEXIS 89",
            "54 U.S.L.W. 4598"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
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
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Mosley",
          "cluster_id": 109336,
          "cite": [
            "46 L. Ed. 2d 313",
            "96 S. Ct. 321",
            "423 U.S. 96",
            "1975 U.S. LEXIS 100"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wright v. West",
          "cluster_id": 112771,
          "cite": [
            "120 L. Ed. 2d 225",
            "112 S. Ct. 2482",
            "505 U.S. 277",
            "1992 U.S. LEXIS 3689"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. Seibert",
          "cluster_id": 137002,
          "cite": [
            "159 L. Ed. 2d 643",
            "124 S. Ct. 2601",
            "542 U.S. 600",
            "2004 U.S. LEXIS 4578"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schneble v. Florida",
          "cluster_id": 108488,
          "cite": [
            "31 L. Ed. 2d 340",
            "92 S. Ct. 1056",
            "405 U.S. 427",
            "1972 U.S. LEXIS 77"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
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
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
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
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alvarado v. State",
          "cluster_id": 1676536,
          "cite": [
            "912 S.W.2d 199",
            "1995 Tex. Crim. App. LEXIS 116",
            "1995 WL 675552"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gimmy v. People",
          "cluster_id": 1231296,
          "cite": [
            "645 P.2d 262",
            "1982 Colo. LEXIS 568"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Guidry v. State",
          "cluster_id": 2342370,
          "cite": [
            "9 S.W.3d 133",
            "1999 Tex. Crim. App. LEXIS 145",
            "1999 WL 1144826"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
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
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Prim",
          "cluster_id": 2050056,
          "cite": [
            "289 N.E.2d 601",
            "53 Ill. 2d 62",
            "1972 Ill. LEXIS 262"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Guerra",
          "cluster_id": 2633286,
          "cite": [
            "129 P.3d 321",
            "40 Cal. Rptr. 3d 118",
            "37 Cal. 4th 1067",
            "2006 Cal. Daily Op. Serv. 1802",
            "2006 Daily Journal DAR 2547",
            "2006 Cal. LEXIS 2872"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
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
        "journal_ref": "Lego v. Twomey:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108429 OR 9424726 OR 9424727) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTE3NzU2ODAwMDAwJnM9MzEzNTIyOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108429+OR+9424726+OR+9424727%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 15,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 15,
        "triage_snippet_classified": 185
      },
      "lane2_top_cited": {
        "query": "cites:(108429 OR 9424726 OR 9424727)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMTkmcz0xMjQ0NzY5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108429+OR+9424726+OR+9424727%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108429 OR 9424726 OR 9424727)",
        "reviewed": 18,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 18,
        "triage_read": 1,
        "triage_snippet_classified": 17
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108429 OR 9424726 OR 9424727)",
    "indexed_citing_opinions": 1278,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108429,
        "count": 1139,
        "count_source": "search"
      },
      {
        "opinion_id": 9424726,
        "count": 170,
        "count_source": "search"
      },
      {
        "opinion_id": 9424727,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1930,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/lego-v-twomey.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc4MjM2MDYmcz02NjIxMzYxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108429+OR+9424726+OR+9424727%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108429,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 104997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 105149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 105751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 106544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 106881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 107419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 107650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 107685,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 107736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 107893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 108111,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 108231,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 269702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 286166,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1207372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1402028,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1409161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1419387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1515039,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1534970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1568872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1586369,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1645241,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1795610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1798836,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1940977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 1992878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 2000298,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 2047659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 2128885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 2199240,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 2225068,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 2374676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 2499246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 2619842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108429,
        "cited_id": 3420642,
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
    "date_created": "2026-07-05T10:51:42Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:53:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:53:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:56:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:53:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Lego v. Twomey

```
<div>
<center><b><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/" aria-description="Citation for case: Lego v. Twomey">404 U.S. 477</a></span> (1972)</b></center>
<center><h1>LEGO<br>
v.<br>
TWOMEY, WARDEN.</h1></center>
<center>No. 70-5037.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 11, 1971</center>
<center>Decided January 12, 1972</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SEVENTH CIRCUIT.
<p><span class="star-pagination">*478</span> <i>Nathan Lewin,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./402/928/">402 U. S. 928</a></span>, argued the cause and filed a brief for petitioner.</p>
<p><i>James B. Zagel,</i> Assistant Attorney General of Illinois, argued the cause for respondent. With him on the brief were <i>William J. Scott,</i> Attorney General, <i>Joel M. Flaum,</i> First Assistant Attorney General, and <i>Warren K. Smoot,</i> Assistant Attorney General.</p>
<p>MR. JUSTICE WHITE delivered the opinion of the Court.</p>
<p>In 1964 this Court held that a criminal defendant who challenges the voluntariness of a confession made to officials and sought to be used against him at his trial has a due process right to a reliable determination that the confession was in fact voluntarily given and not the outcome of coercion which the Constitution forbids. <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">378 U. S. 368</a></span>. While our decision made plain that only voluntary confessions may be admitted at the trial of guilt or innocence, we did not then announce, or even suggest, that the factfinder at a coercion hearing need judge voluntariness with reference to an especially severe standard of proof. Nevertheless, <span class="star-pagination">*479</span> since <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span>,</i> state and federal courts have addressed themselves to the issue with a considerable variety of opinions.<sup>[1]</sup> We granted certiorari in this case to resolve the question. <span class="citation multiple-matches"><a href="/c/U.%20S./401/992/">401 U. S. 992</a></span> (1971).</p>
<p><span class="star-pagination">*480</span> Petitioner Lego was convicted of armed robbery in 1961 after a jury trial in Superior Court, Cook County, Illinois. The court sentenced him to prison for 25 to 50 years. The evidence introduced against Lego at trial included a confession he had made to police after arrest and while in custody at the station house. Prior to trial Lego sought to have the confession suppressed. He did not deny making it but did challenge that he had done so voluntarily. The trial judge conducted a hearing, out of the presence of the jury, at which Lego testified that police had beaten him about the head and neck with a gun butt. His explanation of this treatment was that the local police chief, a neighbor and former classmate of the robbery victim, had sought revenge upon him. Lego introduced into evidence a photograph that had been taken of him at the county jail on the day after his arrest. The photograph showed that petitioner's face had been swollen and had traces of blood on it. Lego admitted that his face had been scratched in a scuffle with the robbery victim but maintained that the encounter did not explain the condition shown in the photograph. The police chief and four officers also testified. They denied either beating or threatening petitioner and disclaimed knowledge that any other officer had done so. The trial judge resolved this credibility problem in favor of the police and ruled the confession admissible.<sup>[2]</sup> At trial, Lego testified in his own behalf. Although he did not dispute the truth of the confession directly, he did tell his version of the events that had transpired at the <span class="star-pagination">*481</span> police station. The trial judge instructed the jury as to the prosecution's burden of proving guilt. He did not instruct that the jury was required to find the confession voluntary before it could be used in judging guilt or innocence.<sup>[3]</sup> On direct appeal the Illinois Supreme Court affirmed the conviction. <i>People</i> v. <i>Lego,</i> <span class="citation" data-id="2199240"><a href="/opinion/2199240/the-people-v-lego/" aria-description="Citation for case: The PEOPLE v. Lego">32 Ill. 2d 76</a></span>, <span class="citation" data-id="2199240"><a href="/opinion/2199240/the-people-v-lego/" aria-description="Citation for case: The PEOPLE v. Lego">203 N. E. 2d 875</a></span> (1965).</p>
<p>Four years later petitioner challenged his conviction by seeking a writ of habeas corpus in the United States District Court for the Northern District of Illinois. He maintained that the trial judge should have found the confession voluntary beyond a reasonable doubt before admitting it into evidence. Although the judge had made no mention of the standard he used, Illinois law provided that a confession challenged as involuntary could be admitted into evidence if, at a hearing outside the presence of the jury, the judge found it voluntary by a preponderance of the evidence.<sup>[4]</sup> In the alternative petitioner argued that the voluntariness question should also have been submitted to the jury for its separate consideration. <span class="star-pagination">*482</span> After first denying the writ for failure to exhaust state remedies, the District Court granted a rehearing motion, concluded that Lego had no state remedy then available to him and denied relief on the merits. <i>United States ex rel. Lego</i> v. <i>Pate,</i> <span class="citation" data-id="1568872"><a href="/opinion/1568872/united-states-ex-rel-lego-v-pate/" aria-description="Citation for case: United States Ex Rel. Lego v. Pate">308 F. Supp. 38</a></span> (1970).<sup>[5]</sup> The Court of Appeals for the Seventh Circuit affirmed.<sup>[6]</sup></p>
<p></p>
<h2>I</h2>
<p>Petitioner challenges the judgment of the Court of Appeals on three grounds. The first is that he was not proved guilty beyond a reasonable doubt as required by <i>In re Winship,</i> <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">397 U. S. 358</a></span> (1970), because the confession used against him at his trial had been proved voluntary only by a preponderance of the evidence. Implicit in the claim is an assumption that a voluntariness hearing is designed to enhance the reliability of jury verdicts. To judge whether that is so we must return to <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">378 U. S. 368</a></span> (1964).</p>
<p>In New York prior to <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span>,</i> juries most often determined the voluntariness of confessions and hence whether confessions could be used in deciding guilt or innocence. Trial judges were required to make an initial determination and could exclude a confession, but only if it could not under any circumstances be deemed voluntary.<sup>[7]</sup> When voluntariness was fairly debatable, either because a dispute of fact existed or because reasonable men could have drawn differing inferences from undisputed facts, the question whether the confession violated due process was for the jury. This meant the confession <span class="star-pagination">*483</span> was introduced at the trial itself. If evidence challenging its voluntariness were adduced, the jury was instructed first to pass upon voluntariness and, if it found the confession involuntary, ignore it in determining guilt. If, on the other hand, the confession were found to be voluntary, the jury was then free to consider its truth or falsity and give the confession an appropriate weight in judging guilt or innocence.</p>
<p>We concluded that the New York procedure was constitutionally defective because at no point along the way did a criminal defendant receive a clear-cut determination that the confession used against him was in fact voluntary. The trial judge was not entitled to exclude a confession merely because he himself would have found it involuntary, and, while we recognized that the jury was empowered to perform that function, we doubted it could do so reliably. Precisely because confessions of guilt, whether coerced or freely given, may be truthful and potent evidence, we did not believe a jury could be called upon to ignore the probative value of a truthful but coerced confession; it was also likely, we thought, that in judging voluntariness itself the jury would be influenced by the reliability of a confession it considered an accurate account of the facts. "It is now axiomatic," we said,</p>
<blockquote>"that a defendant in a criminal case is deprived of due process of law if his conviction is founded, in whole or in part, upon an involuntary confession, without regard for the truth or falsity of the confession, <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534</a></span>, and even though there is ample evidence aside from the confession to support the conviction. <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span>; <i>Stroble</i> v. <i>California,</i> <span class="citation" data-id="9420722"><a href="/opinion/104997/stroble-v-california/" aria-description="Citation for case: Stroble v. California">343 U. S. 181</a></span>; <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span>. Equally clear is the defendant's constitutional right at some stage in the proceedings to object to the use of the confession <span class="star-pagination">*484</span> and to have a fair hearing and a reliable determination on the issue of voluntariness, a determination uninfluenced by the truth or falsity of the confession. <i>Rogers</i> v. <i><span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">Richmond, supra</a></span></i><i>.</i>"<sup>[8]</sup></blockquote>
<p>We did not think it necessary, or even appropriate, in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> to announce that prosecutors would be required to meet a particular burden of proof in a <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> hearing held before the trial judge.<sup>[9]</sup> Indeed, the then-established duty to determine voluntariness had not been framed in terms of a burden of proof,<sup>[10]</sup> nor has it been since <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> was decided.<sup>[11]</sup> We could fairly assume then, as we can now, that a judge would admit into evidence only those confessions that he reliably found, at least by a preponderance of the evidence, had been made voluntarily.</p>
<p>We noted in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> that there may be a relationship between the involuntariness of a confession and its unreliability.<sup>[12]</sup> But our decision was not based in the <span class="star-pagination">*485</span> slightest on the fear that juries might misjudge the accuracy of confessions and arrive at erroneous determinations of guilt or innocence. That case was not aimed at reducing the possibility of convicting innocent men.</p>
<p>Quite the contrary, we feared that the reliability and truthfulness of even coerced confessions could impermissibly influence a jury's judgment as to voluntariness. The use of coerced confessions, whether true or false, is forbidden because the method used to extract them offends constitutional principles. <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#540" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 540-541</a></span> (1961).<sup>[13]</sup> The procedure we established in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> was designed to safeguard the right of an individual, entirely apart from his guilt or innocence, not to be compelled to condemn himself by his own utterances. Nothing in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> questioned the province or capacity of juries to assess the truthfulness of confessions. Nothing in that opinion took from the jury any evidence relating to the accuracy or weight of confessions admitted into evidence. A defendant has <span class="star-pagination">*486</span> been as free since <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> as he was before to familiarize a jury with circumstances that attend the taking of his confession, including facts bearing upon its weight and voluntariness.<sup>[14]</sup> In like measure, of course, juries have been at liberty to disregard confessions that are insufficiently corroborated or otherwise deemed unworthy of belief.</p>
<p>Since the purpose that a voluntariness hearing is designed to serve has nothing whatever to do with improving the reliability of jury verdicts, we cannot accept the charge that judging the admissibility of a confession by a preponderance of the evidence undermines the mandate of <i>In re Winship,</i> <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">397 U. S. 358</a></span> (1970). Our decision in <i><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span></i> was not concerned with standards for determining the admissibility of evidence or with the prosecution's burden of proof at a suppression hearing when evidence is challenged on constitutional grounds. <i><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span></i> went no further than to confirm the fundamental right that protects "the accused against conviction except upon proof beyond a reasonable doubt of every fact necessary to constitute the crime with which he is charged." <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#364" aria-description="Citation for case: In Re WINSHIP"><i>Id.,</i> at 364</a></span>. A high standard of proof is <span class="star-pagination">*487</span> necessary, we said, to ensure against unjust convictions by giving substance to the presumption of innocence. <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#363" aria-description="Citation for case: In Re WINSHIP"><i>Id.,</i> at 363</a></span>. A guilty verdict is not rendered less reliable or less consonant with <i><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span></i> simply because the admissibility of a confession is determined by a less stringent standard. Petitioner does not maintain that either his confession or its voluntariness is an element of the crime with which he was charged. He does not challenge the constitutionality of the standard by which the jury was instructed to decide his guilt or innocence; nor does he question the sufficiency of the evidence that reached the jury to satisfy the proper standard of proof. Petitioner's rights under <i><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span></i> have not been violated.<sup>[15]</sup></p>
<p></p>
<h2>II</h2>
<p>Even conceding that <i><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span></i> is inapplicable because the purpose of a voluntariness hearing is not to implement the presumption of innocence, petitioner presses for reversal on the alternative ground that evidence offered against a defendant at a criminal trial and challenged on constitutional grounds must be determined admissible beyond a reasonable doubt in order to give adequate protection to those values that exclusionary rules are designed to serve. <i>Jackson</i> v. <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Denno, supra</a></span></i><i>,</i> an offspring of <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936), requires judicial rulings on voluntariness prior to admitting confessions. <i>Miranda</i> v. <i>Arizona,</i> 384 <span class="star-pagination">*488</span> U. S. 436 (1966), excludes confessions flowing from custodial interrogations unless adequate warnings were administered and a waiver was obtained. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), and <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), make impermissible the introduction of evidence obtained in violation of a defendant's Fourth Amendment rights. In each instance, and without regard to its probative value, evidence is kept from the trier of guilt or innocence for reasons wholly apart from enhancing the reliability of verdicts. These independent values, it is urged, themselves require a stricter standard of proof in judging admissibility.</p>
<p>The argument is straightforward and has appeal. But we are unconvinced that merely emphasizing the importance of the values served by exclusionary rules is itself sufficient demonstration that the Constitution also requires admissibility to be proved beyond reasonable doubt.<sup>[16]</sup> Evidence obtained in violation of the Fourth Amendment has been excluded from federal criminal trials for many years. <i>Weeks</i> v. <i>United States, supra</i><i>.</i> The same is true of coerced confessions offered in either federal or state trials. <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">168 U. S. 532</a></span> (1897); <i>Brown</i> v. <i><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Mississippi, supra</a></span></i><i>.</i> But, from our experience over this period of time no substantial evidence has accumulated that federal rights have suffered from determining admissibility by a preponderance of the evidence. Petitioner offers nothing to suggest that admissibility rulings have been unreliable or otherwise wanting in quality because not based on some higher standard. Without good cause, we are unwilling to expand currently applicable exclusionary rules by erecting additional barriers to placing truthful and probative evidence <span class="star-pagination">*489</span> before state juries and by revising the standards applicable in collateral proceedings. Sound reason for moving further in this direction has not been offered here nor do we discern any at the present time. This is particularly true since the exclusionary rules are very much aimed at deterring lawless conduct by police and prosecution and it is very doubtful that escalating the prosecution's burden of proof in Fourth and Fifth Amendment suppression hearings would be sufficiently productive in this respect to outweigh the public interest in placing probative evidence before juries for the purpose of arriving at truthful decisions about guilt or innocence.</p>
<p>To reiterate what we said in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span>:</i> when a confession challenged as involuntary is sought to be used against a criminal defendant at his trial, he is entitled to a reliable and clear-cut determination that the confession was in fact voluntarily rendered. Thus, the prosecution must prove at least by a preponderance of the evidence that the confession was voluntary. Of course, the States are free, pursuant to their own law, to adopt a higher standard. They may indeed differ as to the appropriate resolution of the values they find at stake.<sup>[17]</sup></p>
<p></p>
<h2>III</h2>
<p>We also reject petitioner's final contention that, even though the trial judge ruled on his coercion claim, he was entitled to have the jury decide the claim anew. To the extent this argument asserts that the judge's determination was insufficiently reliable, it is no more persuasive than petitioner's other contentions. To the extent the position assumes that a jury is better suited than a judge to determine voluntariness, it questions the basic assumptions of <i>Jackson</i> v. <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Denno</a></span></i><i>;</i> it also ignores <span class="star-pagination">*490</span> that <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> neither raised any question about the constitutional validity of the so-called orthodox rule for judging the admissibility of confessions nor even suggested that the Constitution requires submission of voluntariness claims to a jury as well as a judge. Finally, <i>Duncan</i> v. <i>Louisiana,</i> <span class="citation" data-id="9423691"><a href="/opinion/107685/duncan-v-louisiana/" aria-description="Citation for case: Duncan v. Louisiana">391 U. S. 145</a></span> (1968), which made the Sixth Amendment right to trial by jury applicable to the States, did not purport to change the normal rule that the admissibility of evidence is a question for the court rather than the jury. Nor did that decision require that both judge and jury pass upon the admissibility of evidence when constitutional grounds are asserted for excluding it. We are not disposed to impose as a constitutional requirement a procedure we have found wanting merely to afford petitioner a second forum for litigating his claim.</p>
<p>The decision of the Court of Appeals is</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE POWELL and MR. JUSTICE REHNQUIST took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE BRENNAN, with whom MR. JUSTICE DOUGLAS and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>When the prosecution, state or federal, seeks to put in evidence an allegedly involuntary confession, its admissibility is determined by the command of the Fifth Amendment that "[n]o person . . . shall be compelled in any criminal case to be a witness against himself." <i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#740" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737, 740</a></span> (1966); <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#7" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 7-8</a></span> (1964); <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#542" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 542-543</a></span> (1897). This right against compulsory self-incrimination is the "essential mainstay" of our system of criminal prosecution, <i>Malloy</i> v. <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#7" aria-description="Citation for case: Malloy v. Hogan"><i>Hogan, supra,</i> at 7</a></span>, "a system in which the State must establish guilt by evidence independently <span class="star-pagination">*491</span> and freely secured and may not by coercion prove its charge against an accused out of his own mouth," <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#541" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 541</a></span> (1961). What is thereby protected from governmental invasion is, quite simply, "the right of a person to remain silent unless he chooses to speak in the unfettered exercise of his own will." <i>Malloy</i> v. <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#8" aria-description="Citation for case: Malloy v. Hogan"><i>Hogan, supra,</i> at 8</a></span>. Hence, a confession is involuntary and inadmissible unless it is "the product of a rational intellect and a free will." <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#208" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 208</a></span> (1960); see <i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/#440" aria-description="Citation for case: Reck v. Pate">367 U. S. 433, 440</a></span> (1961).</p>
<p>Ideally, of course, a defendant's compelled utterance would never be admitted into evidence against him. As we said in <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#376" aria-description="Citation for case: Jackson v. Denno">378 U. S. 368, 376</a></span> (1964), it is "axiomatic" that a criminal conviction cannot stand if it "is founded, in whole or in part, upon an involuntary confession . . . even though there is ample evidence aside from the confession to support the conviction." Yet I doubt that informed observers of the criminal process would deny that at least some compelled utterances slip through, even assuming scrupulous adherence to constitutional standards and the most rigorous procedural protections. <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> was an attempt to move that reality somewhat closer to the ideal. We there rejected the New York rule because it "did not afford a reliable determination of the voluntariness of the confession offered in evidence at the trial" and consequently "did not adequately protect [a defendant's] right to be free of a conviction based upon a coerced confession." <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#377" aria-description="Citation for case: Jackson v. Denno"><i>Id.,</i> at 377</a></span>. As the Court today points out, "[t]he procedure we established in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> was designed to safeguard the right of an individual, entirely apart from his guilt or innocence, not to be compelled to condemn himself by his own utterances." <i>Ante,</i> at 485.</p>
<p>There is no need to dwell upon the importance our American concept of justice attaches to preserving the <span class="star-pagination">*492</span> integrity of the constitutional privilege. Both the rule that automatically reverses a conviction when an involuntary confession was admitted at trial and the procedure established in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> for determining whether a confession was voluntary are means to further the end that no utterance of a defendant not the product of his own free choice will be used against him. The Court today reaffirms what we held in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span>:</i> "[W]hen a confession challenged as involuntary is sought to be used against a criminal defendant at his trial, he is entitled to a reliable and clear-cut determination that the confession was in fact voluntarily rendered." <i>Ante,</i> at 489. But the Court goes on to hold that it follows from <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> that "the prosecution must prove at least by a preponderance of the evidence that the confession was voluntary." <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Ibid.</a></span></i> I disagree. In my view, the rationale of <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> requires the conclusion that the preponderance standard does not provide sufficient protection against the danger that involuntary confessions will be employed in criminal trials.</p>
<p>A <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> hearing normally presents the factfinder with conflicting testimony from the defendant and law enforcement officers about what occurred during the officers' interrogation of the defendant. The factfinder's resolution of this conflict is often, as a practical matter, the final resolution of the voluntariness issue. <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#390" aria-description="Citation for case: Jackson v. Denno"><i>Jackson, supra,</i> at 390-391</a></span>. This case is a typical example. Petitioner testified that he confessed because the police had beaten him; the police testified that there was no beating. As the Court notes, "[t]he trial judge resolved this credibility problem in favor of the police and ruled the confession admissible." <i>Ante,</i> at 480. When the question before the factfinder is whether to believe one or the other of two self-serving accounts of what has happened, it is apparent that the standard of persuasion will in many instances be of controlling significance. <span class="star-pagination">*493</span> See <i>Speiser</i> v. <i>Randall,</i> <span class="citation" data-id="9421696"><a href="/opinion/105751/speiser-v-randall/#525" aria-description="Citation for case: Speiser v. Randall">357 U. S. 513, 525-526</a></span> (1958). Although the Court suggests "that federal rights have [not] suffered from determining admissibility by a preponderance of the evidence" and that there has been no showing "that admissibility rulings have been unreliable. . . because not based on some higher standard," <i>ante,</i> at 488, I do not think it can be denied, given the factual nature of the ordinary voluntariness determination, that permitting a lower standard of proof will necessarily result in the admission of more involuntary confessions than would be admitted were the prosecution required to meet a higher standard. The converse, of course, is also true. Requiring the higher standard means that some voluntary confessions will be excluded as involuntary even though they would have been found voluntary under the lower standard.</p>
<p>The standard of proof required for a criminal conviction presents a similar situation, yet we have held that guilt must be established by proof beyond a reasonable doubt. <i>In re Winship,</i> <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#361" aria-description="Citation for case: In Re WINSHIP">397 U. S. 358, 361-364</a></span> (1970); see <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#370" aria-description="Citation for case: In Re WINSHIP"><i>id.,</i> at 370-372</a></span> (Harlan, J., concurring.) Permitting proof by a preponderance of the evidence would necessarily result in the conviction of more defendants who are in fact innocent. Conversely, imposing the burden of proof beyond a reasonable doubt means that more defendants who are in fact guilty are found innocent. It seems to me that the same considerations that demand the reasonable-doubt standard when guilt or innocence is at stake also demand that standard when the question is the admissibility of an allegedly involuntary confession.</p>
<p>We permit proof by a preponderance of the evidence in civil litigation because "we view it as no more serious in general for there to be an erroneous verdict in the defendant's favor than for there to be an erroneous verdict in the plaintiff's favor." <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#371" aria-description="Citation for case: In Re WINSHIP"><i>Id.,</i> at 371</a></span> (Harlan, J., concurring). We do not take that view in criminal cases. <span class="star-pagination">*494</span> We said in <i><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span></i> that the reasonable-doubt standard "is a prime instrument for reducing the risk of convictions resting on factual error. The standard provides concrete substance for the presumption of innocence . . . ." <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#363" aria-description="Citation for case: In Re WINSHIP"><i>Id.,</i> at 363</a></span>. As Mr. Justice Harlan put it in his concurring opinion, the requirement of proof beyond a reasonable doubt is "bottomed on a fundamental value determination of our society that it is far worse to convict an innocent man than to let a guilty man go free." <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#372" aria-description="Citation for case: In Re WINSHIP"><i>Id.,</i> at 372</a></span>.</p>
<p>If we permit the prosecution to prove by a preponderance of the evidence that a confession was voluntary, then, to paraphrase Mr. Justice Harlan, we must be prepared to justify the view that it is no more serious in general to admit involuntary confessions than it is to exclude voluntary confessions. I am not prepared to justify that view. Compelled self-incrimination is so alien to the American sense of justice that I see no way that such a view could ever be justified. If we are to provide "concrete substance" for the command of the Fifth Amendment that no person shall be compelled to condemn himself, we must insist, as we do at the trial of guilt or innocence, that the prosecution prove that the defendant's confession was voluntary beyond a reasonable doubt.<sup>[*]</sup> In my judgment, to paraphrase Mr. Justice <span class="star-pagination">*495</span> Harlan again, the command of the Fifth Amendment reflects the determination of our society that it is worse to permit involuntary self-condemnation than it is to deprive a jury of probative evidence. Just as we do not convict when there is a reasonable doubt of guilt, we should not permit the prosecution to introduce into evidence a defendant's confession when there is a reasonable doubt that it was the product of his free and rational choice.</p>
<p>I add only that the absolute bar against the admission of a defendant's compelled utterance at his criminal trial is fundamentally an expression of the American commitment to the moral worth of the individual. What we said in <i><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span></i> bears repeating here. "[U]se of the reasonable-doubt standard is indispensable to command the respect and confidence of the community in applications of the criminal law. It is critical that the moral force of the criminal law not be diluted by a standard of proof that leaves people in doubt whether innocent men are being condemned." <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#364" aria-description="Citation for case: In Re WINSHIP"><i>Id.,</i> at 364</a></span>. I believe that it is just as critical to our system of criminal justice that when a person's words are used against him, no reasonable doubt remains that he spoke of his own free will.</p>
<h2>NOTES</h2>
<p>[1]  State courts that have considered the question since <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> have adopted a variety of standards, most of them founded upon state law. Many have sanctioned a standard of proof less strict than beyond a reasonable doubt, including proof of voluntariness by a preponderance of the evidence or to the satisfaction of the court or proof of voluntariness in fact. <i>E. g., </i><i>Duncan</i> v. <i>State,</i> <span class="citation" data-id="9656485"><a href="/opinion/1586369/duncan-v-state/" aria-description="Citation for case: Duncan v. State">278 Ala. 145</a></span>, <span class="citation" data-id="9656485"><a href="/opinion/1586369/duncan-v-state/" aria-description="Citation for case: Duncan v. State">176 So. 2d 840</a></span> (1965); <i>State</i> v. <i>Dillon,</i> <span class="citation" data-id="1402028"><a href="/opinion/1402028/state-v-dillon/" aria-description="Citation for case: State v. Dillon">93 Idaho 698</a></span>, <span class="citation" data-id="1402028"><a href="/opinion/1402028/state-v-dillon/" aria-description="Citation for case: State v. Dillon">471 P. 2d 553</a></span> (1970), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./401/942/">401 U. S. 942</a></span> (1971); <i>People</i> v. <i>Harper,</i> <span class="citation" data-id="9884438"><a href="/opinion/2047659/the-people-v-harper/" aria-description="Citation for case: The PEOPLE v. Harper">36 Ill. 2d 398</a></span>, <span class="citation" data-id="9884438"><a href="/opinion/2047659/the-people-v-harper/" aria-description="Citation for case: The PEOPLE v. Harper">223 N. E. 2d 841</a></span> (1967); <i>State</i> v. <i>Milow,</i> <span class="citation" data-id="1409161"><a href="/opinion/1409161/state-v-milow/" aria-description="Citation for case: State v. Milow">199 Kan. 576</a></span>, <span class="citation" data-id="1409161"><a href="/opinion/1409161/state-v-milow/" aria-description="Citation for case: State v. Milow">433 P. 2d 538</a></span> (1967); <i>Barnhart</i> v. <i>State,</i> <span class="citation" data-id="1515039"><a href="/opinion/1515039/barnhart-v-state/" aria-description="Citation for case: Barnhart v. State">5 Md. App. 222</a></span>, <span class="citation" data-id="1515039"><a href="/opinion/1515039/barnhart-v-state/" aria-description="Citation for case: Barnhart v. State">246 A. 2d 280</a></span> (1968); <i>Commonwealth</i> v. <i>White,</i> <span class="citation" data-id="2225068"><a href="/opinion/2225068/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">353 Mass. 409</a></span>, <span class="citation" data-id="2225068"><a href="/opinion/2225068/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">232 N. E. 2d 335</a></span> (1967); <i>State</i> v. <i>Nolan,</i> <span class="citation" data-id="1795610"><a href="/opinion/1795610/state-v-nolan/" aria-description="Citation for case: State v. Nolan">423 S. W. 2d 815</a></span> (Mo. 1968); <i>State</i> v. <i>White,</i> <span class="citation" data-id="8025470"><a href="/opinion/8067290/state-v-white/" aria-description="Citation for case: State v. White">146 Mont. 226</a></span>, <span class="citation" data-id="8025470"><a href="/opinion/8067290/state-v-white/" aria-description="Citation for case: State v. White">405 P. 2d 761</a></span> (1965), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./384/1023/">384 U. S. 1023</a></span> (1966); <i>State</i> v. <i>Brewton,</i> <span class="citation" data-id="9794916"><a href="/opinion/2619842/state-v-brewton/" aria-description="Citation for case: State v. Brewton">238 Ore. 590</a></span>, <span class="citation" data-id="9794916"><a href="/opinion/2619842/state-v-brewton/" aria-description="Citation for case: State v. Brewton">395 P. 2d 874</a></span> (1964); <i>Commonwealth ex rel. Butler</i> v. <i>Rundle,</i> <span class="citation" data-id="1992878"><a href="/opinion/1992878/commonwealth-ex-rel-butler-v-rundle/" aria-description="Citation for case: Commonwealth Ex Rel. Butler v. Rundle">429 Pa. 141</a></span>, <span class="citation" data-id="1992878"><a href="/opinion/1992878/commonwealth-ex-rel-butler-v-rundle/" aria-description="Citation for case: Commonwealth Ex Rel. Butler v. Rundle">239 A. 2d 426</a></span> (1968); <i>Monts</i> v. <i>State,</i> <span class="citation" data-id="2374676"><a href="/opinion/2374676/monts-v-state/" aria-description="Citation for case: Monts v. State">218 Tenn. 31</a></span>, <span class="citation" data-id="2374676"><a href="/opinion/2374676/monts-v-state/" aria-description="Citation for case: Monts v. State">400 S. W. 2d 722</a></span> (1966); <i>State</i> v. <i>Davis,</i> <span class="citation" data-id="9562176"><a href="/opinion/1207372/state-v-davis/" aria-description="Citation for case: State v. Davis">73 Wash. 2d 271</a></span>, <span class="citation" data-id="9562176"><a href="/opinion/1207372/state-v-davis/" aria-description="Citation for case: State v. Davis">438 P. 2d 185</a></span> (1968).
</p>
<p>Other States, using state law or not specifying a basis, require proof beyond a reasonable doubt. <i>E. g., </i><i>State</i> v. <i>Ragsdale,</i> <span class="citation" data-id="1940977"><a href="/opinion/1940977/state-v-ragsdale/" aria-description="Citation for case: State v. Ragsdale">249 La. 420</a></span>, <span class="citation" data-id="1940977"><a href="/opinion/1940977/state-v-ragsdale/" aria-description="Citation for case: State v. Ragsdale">187 So. 2d 427</a></span> (1966), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./385/1029/">385 U. S. 1029</a></span> (1967); <i>State</i> v. <i>Keiser,</i> <span class="citation" data-id="1645241"><a href="/opinion/1645241/state-v-keiser/" aria-description="Citation for case: State v. Keiser">274 Minn. 265</a></span>, <span class="citation" data-id="1645241"><a href="/opinion/1645241/state-v-keiser/" aria-description="Citation for case: State v. Keiser">143 N. W. 2d 75</a></span> (1966); <i>State</i> v. <i>Yough,</i> 49 N. J. 587, <span class="citation" data-id="1534970"><a href="/opinion/1534970/state-v-yough/" aria-description="Citation for case: State v. Yough">231 A. 2d 598</a></span> (1967); <i>People</i> v. <i>Huntley,</i> 15 N. Y. 2d 72, <span class="citation" data-id="5521571"><a href="/opinion/5674048/people-v-huntley/" aria-description="Citation for case: People v. Huntley">204 N. E. 2d 179</a></span> (1965); <i>State</i> v. <i>Thundershield,</i> 83 S. D. 414, <span class="citation" data-id="9722826"><a href="/opinion/2128885/state-v-thundershield/" aria-description="Citation for case: State v. Thundershield">160 N. W. 2d 408</a></span> (1968); <i>State ex rel. Goodchild</i> v. <i>Burke,</i> <span class="citation" data-id="1798836"><a href="/opinion/1798836/state-ex-rel-goodchild-v-burke/" aria-description="Citation for case: State Ex Rel. Goodchild v. Burke">27 Wis. 2d 244</a></span>, <span class="citation" data-id="1798836"><a href="/opinion/1798836/state-ex-rel-goodchild-v-burke/" aria-description="Citation for case: State Ex Rel. Goodchild v. Burke">133 N. W. 2d 753</a></span> (1965), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./384/1017/">384 U. S. 1017</a></span> (1966).</p>
<p>Two federal courts have held as an exercise of supervisory power that voluntariness must be proved beyond a reasonable doubt. <i>Ralph</i> v. <i>Warden,</i> <span class="citation" data-id="9456545"><a href="/opinion/294988/william-ralph-v-warden-maryland-penitentiary/#793" aria-description="Citation for case: William Ralph v. Warden, Maryland Penitentiary">438 F. 2d 786, 793</a></span> (CA4 1970), clarifying <i>United States</i> v. <i>Inman,</i> <span class="citation" data-id="269702"><a href="/opinion/269702/united-states-v-richard-floyd-inman/" aria-description="Citation for case: United States v. Richard Floyd Inman">352 F. 2d 954</a></span> (CA4 1965); <i>Pea</i> v. <i>United States,</i> 130 U. S. App. D. C. 66, <span class="citation" data-id="9453787"><a href="/opinion/280914/emanuel-pea-jr-v-united-states/" aria-description="Citation for case: Emanuel Pea, Jr. v. United States">397 F. 2d 627</a></span> (1967); cf. <i>United States</i> v. <i>Schipani,</i> <span class="citation" data-id="1419387"><a href="/opinion/1419387/united-states-v-schipani/" aria-description="Citation for case: United States v. Schipani">289 F. Supp. 43</a></span> (EDNY 1968), aff'd, <span class="citation" data-id="286166"><a href="/opinion/286166/united-states-v-joseph-f-schipani/" aria-description="Citation for case: United States v. Joseph F. Schipani">414 F. 2d 1262</a></span> (CA2 1969), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./397/922/">397 U. S. 922</a></span> (1970), requiring the Government to prove beyond a reasonable doubt that certain evidence was not tainted by violation of the Fourth Amendment.</p>
<p>[2]  In ruling the confession admissible, the judge stated:
</p>
<p>"The petitioner has admitted under oath he had a struggle with the complaining witness over the gun; he was wounded, obtained a facial wound. The Officers testified he was bloody at the time he was arrested.</p>
<p>"I don't believe the defendant's testimony at all that he was beaten up by the Police. The condition he is in is well explained by the defendant himself."</p>
<p>[3]  Illinois followed what we described in <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">378 U. S. 368</a></span> (1964), as "the orthodox rule, under which the judge himself solely and finally determines the voluntariness of the confession . . . ." <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#378" aria-description="Citation for case: Jackson v. Denno"><i>Id.,</i> at 378</a></span>. While the procedures of all the States could not be neatly classified, we noted that some followed the Massachusetts procedure whereby the judge himself first resolves evidentiary conflicts and determines whether a confession is in fact voluntary. If he is unable so to conclude, the confession may not be admitted into evidence. If judged voluntary and therefore admissible, the jury must also determine the coercion issue and is instructed to ignore a confession it finds involuntary. <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Id.,</a></span></i> at 378 n. 8. Other States had adopted the New York procedure at issue in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span>.</i> Our decision in <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> cast no doubt upon the orthodox and Massachusetts procedures but did call into question the practice of every State that did not clearly follow one of these procedures. A thorough tabulation of what States did in the wake of <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> appears in 3 J. Wigmore, Evidence 585-593 (J. Chadbourn rev. 1970).</p>
<p>[4]  <i>People</i> v. <i>Wagoner,</i> <span class="citation" data-id="2000298"><a href="/opinion/2000298/the-people-v-wagoner/" aria-description="Citation for case: The PEOPLE v. Wagoner">8 Ill. 2d 188</a></span>, <span class="citation" data-id="2000298"><a href="/opinion/2000298/the-people-v-wagoner/" aria-description="Citation for case: The PEOPLE v. Wagoner">133 N. E. 2d 24</a></span> (1956); <i>People</i> v. <i>Thomlison,</i> <span class="citation" data-id="3420642"><a href="/opinion/3423792/the-people-v-thomlison/" aria-description="Citation for case: The People v. Thomlison">400 Ill. 555</a></span>, <span class="citation" data-id="3420642"><a href="/opinion/3423792/the-people-v-thomlison/" aria-description="Citation for case: The People v. Thomlison">81 N. E. 2d 434</a></span> (1948).</p>
<p>[5]  Respondent makes no contention here that petitioner either waived the right to adjudicate his federal claims or deliberately bypassed state procedures for testing those claims. Cf. <i>Fay</i> v. <i>Noia,</i> <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#439" aria-description="Citation for case: Fay v. Noia">372 U. S. 391, 439</a></span> (1963).</p>
<p>[6]  The Seventh Circuit's affirmance is unreported. <i>United States ex rel. Lego</i> v. <i>Pate,</i> No. 18313 (CA7 Oct. 8, 1970).</p>
<p>[7]  A more thorough description of the New York procedure is found in <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#377" aria-description="Citation for case: Jackson v. Denno">378 U. S., at 377-391</a></span>.</p>
<p>[8]  <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#376" aria-description="Citation for case: Jackson v. Denno">378 U. S., at 376-377</a></span>.</p>
<p>[9]  "Judge" is used here and throughout the opinion to mean a factfinder, whether trial judge or jury, at a voluntariness hearing. The proscription against permitting the jury that passes upon guilt or innocence to judge voluntariness in the same proceeding does not preclude the States from impaneling a separate jury to determine voluntariness. <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">378 U. S., at 391</a></span> n. 19.</p>
<p>[10]  See, <i>e. g., </i><i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span> (1963); <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span> (1959); <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span> (1958).</p>
<p>[11]  See, <i>e. g., </i><i>Frazier</i> v. <i>Cupp,</i> <span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731</a></span> (1969); <i>Boulden</i> v. <i>Holman,</i> <span class="citation" data-id="9423981"><a href="/opinion/107893/boulden-v-holman/" aria-description="Citation for case: Boulden v. Holman">394 U. S. 478</a></span> (1969); <i>Harrison</i> v. <i>United States,</i> <span class="citation" data-id="9423779"><a href="/opinion/107736/harrison-v-united-states/" aria-description="Citation for case: Harrison v. United States">392 U. S. 219</a></span> (1968); <i>Greenwald</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9423651"><a href="/opinion/107650/greenwald-v-wisconsin/" aria-description="Citation for case: Greenwald v. Wisconsin">390 U. S. 519</a></span> (1968); <i>Clewis</i> v. <i>Texas,</i> <span class="citation" data-id="107419"><a href="/opinion/107419/clewis-v-texas/" aria-description="Citation for case: Clewis v. Texas">386 U. S. 707</a></span> (1967); <i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737</a></span> (1966); cf. <i>Procunier</i> v. <i>Atchley,</i> <span class="citation" data-id="108231"><a href="/opinion/108231/procunier-v-atchley/" aria-description="Citation for case: Procunier v. Atchley">400 U. S. 446</a></span> (1971).</p>
<p>[12]  We noted that coerced confessions are forbidden in part because of their "probable unreliability." <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#385" aria-description="Citation for case: Jackson v. Denno">378 U. S., at 385-386</a></span>. However, it had been settled when this Court decided <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Jackson</a></span></i> that the exclusion of unreliable confessions is not the purpose that a voluntariness hearing is designed to serve. <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534</a></span> (1961). The sole issue in such a hearing is whether a confession was coerced. Whether it be true or false is irrelevant; indeed, such an inquiry is forbidden. The judge may not take into consideration evidence that would indicate that the confession, though compelled, is reliable, even highly so. <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#545" aria-description="Citation for case: Rogers v. Richmond"><i>Id.,</i> at 545</a></span>. As difficult as such tasks may be to accomplish, the judge is also duty-bound to ignore implications of reliability in facts relevant to coercion and to shut from his mind any internal evidence of authenticity that a confession itself may bear.</p>
<p>[13]  In <i>Jackson,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#377" aria-description="Citation for case: Jackson v. Denno">378 U. S., at 377-391</a></span>, we traced the genesis of the view that due process forbids the use of coerced confessions, whether or not reliable. The Court had departed from that view in <i>Stein</i> v. <i>New York,</i> <span class="citation" data-id="9420977"><a href="/opinion/105149/stein-v-new-york/" aria-description="Citation for case: Stein v. New York">346 U. S. 156</a></span> (1953), whose premise was that a confession is excludable because of its inherent untrustworthiness. The <i><span class="citation" data-id="9420977"><a href="/opinion/105149/stein-v-new-york/" aria-description="Citation for case: Stein v. New York">Stein</a></span></i> premise was repudiated in <i>Rogers</i> v. <i><span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">Richmond</a></span></i> and <i><span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">Rogers</a></span></i> was reaffirmed in <i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#739" aria-description="Citation for case: Davis v. North Carolina">384 U. S., at 739</a></span>, and <i>Johnson</i> v. <i>New Jersey,</i> <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719</a></span>, 729 n. 9 (1966). That case continues to serve as the basis for evaluating coercion claims. See cases cited in n. 11, <i>supra.</i></p>
<p>[14]  This is the course that petitioner pursued. Cf. <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">378 U. S., at 386</a></span> n. 13. Although <span class="citation no-link">18 U. S. C. § 3501</span> (a) is inapplicable here, it is relevant to note the provisions of that section:
</p>
<p>"(a) In any criminal prosecution brought by the United States or by the District of Columbia, a confession, as defined in subsection (e) hereof, shall be admissible in evidence if it is voluntarily given. Before such confession is received in evidence, the trial judge shall, out of the presence of the jury, determine any issue as to voluntariness. If the trial judge determines that the confession was voluntarily made it shall be admitted in evidence and the trial judge shall permit the jury to hear relevant evidence on the issue of voluntariness and shall instruct the jury to give such weight to the confession as the jury feels it deserves under all the circumstances."</p>
<p>[15]  Nothing is to be gained from restating the constitutional rule as requiring proof of guilt beyond a reasonable doubt on the basis of constitutionally obtained evidence and then arguing that rights under <i><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span></i> are diluted unless admissibility is governed by a high standard. Transparently, this assumes the question at issue, which is whether a confession is admissible if found voluntary by a preponderance of the evidence. <i>United States</i> v. <i>Schipani, supra,</i> n. 1, followed this unsatisfactory course in a Fourth Amendment case but stopped short of basing the decision on the Constitution.</p>
<p>[16]  It is no more persuasive to impose the stricter standard of proof as an exercise of supervisory power than as a constitutional rule. Cf. <i>Ralph</i> v. <span class="citation" data-id="9456545"><a href="/opinion/294988/william-ralph-v-warden-maryland-penitentiary/#1" aria-description="Citation for case: William Ralph v. Warden, Maryland Penitentiary"><i>Warden, supra,</i> n. 1</a></span>, clarifying <i>United States</i> v. <span class="citation" data-id="269702"><a href="/opinion/269702/united-states-v-richard-floyd-inman/#1" aria-description="Citation for case: United States v. Richard Floyd Inman"><i>Inman, supra,</i> n. 1</a></span>; <i>Pea</i> v. <i>United States, supra,</i> n. 1.</p>
<p>[17]  See cases cited in n. 1, <i>supra.</i></p>
<p>[*]  My view that the reasonable-doubt standard must be imposed upon the prosecution does not depend upon whether that standard would be more effective than some lower standard in deterring police misconduct. When a defendant challenges his confession as involuntary, "the constitutional inquiry is not whether the conduct of state officers in obtaining the confession was shocking, but whether the confession was `free and voluntary . . . .' " <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#7" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 7</a></span> (1964). It is true that the defendant will frequently allege police misconduct, as petitioner did here. Nevertheless, as we said in <i>Townsend</i> v. <i>Sain,</i> <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/#308" aria-description="Citation for case: Townsend v. Sain">372 U. S. 293, 308</a></span> (1963), "[a]ny questioning by police officers which <i>in fact</i> produces a confession which is not the product of a free intellect renders that confession inadmissible." (Emphasis in original.)</p>

</div>
```

---

## GROUP: content/cases/Lewis v. United States (1966).md  (`case`, 6 assertions)

### content_page

```
---
title: "Lewis v. United States (1966)"
type: case
citation: "385 U.S. 206 (1966)"
parallel_cite: "87 S. Ct. 424; 17 L. Ed. 2d 312"
neutral_cite: 1966 U.S. LEXIS 3
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1966
date_decided: 1966-12-12
docket: 36
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1966-12-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "Lewis v. United States (1966)"
  varies_by_point: false
  scope_note: "Good law; part of the settled misplaced-trust / false-friend line (Hoffa, Lopez, On Lee, later United States v. White) holding that undercover dealing with a willing party is no Fourth Amendment search."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107312/lewis-v-united-states/"
  cluster_id: 107312
  opinion_id: 9423294
  identity_checked: true
homes:
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (undercover entry / misplaced trust)"
  - page: "[[Consent Searches]]"
    role: "Related"
related: ["[[Gouled v. United States]]"]
aliases: ["Lewis v. United States"]
tags: ["case", "fourth-amendment", "search-threshold", "undercover", "misplaced-trust", "consent", "home"]
holding: "When an occupant converts his home into a commercial center and invites an undercover agent in to transact illegal business, the agent's entry and purchase are no Fourth Amendment search; the agent may not, however, exceed the invitation to conduct a general search."
lake:
  record_id: "Lewis v. United States (1966)"
  status: verified
  projected_at: 2026-07-10
---

# Lewis v. United States (1966)

*385 U.S. 206 (1966)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

> **Disambiguation:** This is *Lewis v. United States*, 385 U.S. 206 (1966) (undercover entry / misplaced trust). Distinct from later same-named cases (e.g., 445 U.S. 55 (1980), felon-in-possession; 518 U.S. 322 (1996), petty-offense jury right), which are not part of this corpus. A bare `[[Lewis v. United States]]` link resolves here.

## Background
A federal narcotics agent, posing as a willing buyer, telephoned Lewis and was twice invited to Lewis's home to purchase marihuana. At each visit Lewis sold the agent narcotics; on the second sale he threw in an extra bag for a prospective "regular customer." The agent saw, heard, and took nothing beyond what Lewis exposed and handed over as part of the drug sale. Lewis moved to suppress, arguing the agent's deception-procured entry into his home was an unconstitutional search.

## Issue
Whether a government agent's entry into a home by the occupant's invitation, achieved by concealing his identity, to buy contraband as part of the occupant's illegal business constitutes a Fourth Amendment search.

## Rule
No search occurs. "[W]hen … the home is converted into a commercial center to which outsiders are invited for purposes of transacting unlawful business, that business is entitled to no greater sanctity than if it were carried on in a store, a garage, a car, or on the street. A government agent, in the same manner as a private person, may accept an invitation to do business and may enter upon the premises for the very purposes contemplated by the occupant." — 385 U.S. at 211. ^pin-211

The rule has a limit: it "does not mean that, whenever entry is obtained by invitation and the locus is characterized as a place of business, an agent is authorized to conduct a general search for incriminating materials" — the agent may not exceed the scope of the invitation. — [*Id.*](https://www.courtlistener.com/opinion/107312/lewis-v-united-states/#:~:text=does%20not%20mean%20that%2C%20whenever) (citing *Gouled*). ^pin-211b

## Application
"During neither of his visits to petitioner's home did the agent see, hear, or take anything that was not contemplated, and in fact intended, by petitioner as a necessary part of his illegal business." — 385 U.S. at 210. ^pin-210

Lewis chose the location and willingly admitted the agent to make the sale he sought, so there was no governmental intrusion on protected privacy and nothing was taken beyond the marihuana voluntarily transferred. The agent did no more than buy the wares offered, so no Fourth Amendment search occurred.

## Conclusion
The undercover purchase in the home was not a Fourth Amendment search; the conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Lewis* is a settled member of the misplaced-trust / false-friend line — a person who deals with someone who turns out to be an undercover agent assumes the risk of that misplaced trust — alongside *[[Hoffa v. United States]]*, *Lopez v. United States*, and later affirmed in *United States v. White*. Its limit (no general search beyond the invitation) traces to [[Gouled v. United States]].

## Appears on
- [[Reasonable Expectation of Privacy]] — *Related (undercover entry / misplaced trust)*
- [[Consent Searches]] — *Related*

## Sources
- *Lewis v. United States*, 385 U.S. 206 (1966) — https://www.courtlistener.com/opinion/107312/lewis-v-united-states/ — pinpoints: 210, 211.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "25589f64e7fb4de2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "385 U.S. 206 (1966)", "court": "U.S. Supreme Court", "neutral_cite": "1966 U.S. LEXIS 3", "official_citation_present": true, "parallel_cite": "87 S. Ct. 424; 17 L. Ed. 2d 312", "title": "Lewis v. United States (1966)", "year": "1966"}}
{"assertion_id": "79efba74fde139a5", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Related (undercover entry / misplaced trust)", "title": "Lewis v. United States (1966)"}}
{"assertion_id": "dced19efd85da0e1", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "When an occupant converts his home into a commercial center and invites an undercover agent in to transact illegal business, the agent's entry and purchase are no Fourth Amendment search; the agent may not, however, exceed the invitation to conduct a general search.", "title": "Lewis v. United States (1966)"}}
{"assertion_id": "e6dbade55da67e86", "dimension": "support", "kind": "home_role", "locator": {"home": "Consent Searches"}, "payload": {"home": "Consent Searches", "role": "Related", "title": "Lewis v. United States (1966)"}}
{"assertion_id": "5c7ff0e8f7e5357d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1966-12-12", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Lewis v. United States (1966)", "field_i_validity": "good_law", "scope_note": "Good law; part of the settled misplaced-trust / false-friend line (Hoffa, Lopez, On Lee, later United States v. White) holding that undercover dealing with a willing party is no Fourth Amendment search.", "title": "Lewis v. United States (1966)", "varies_by_point": "false"}}
{"assertion_id": "d00982f60be171f3", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Lewis v. United States (1966)"}}
```

### lake record — Lewis v. United States (1966)

```json
{
  "schema_version": "s2.v1",
  "record_id": "Lewis v. United States (1966)",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Lewis v. United States",
    "case_name_short": "Lewis",
    "case_name_full": "Lewis v. United States",
    "input_case_name": "Lewis v. United States (1966)",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1966-12-12",
    "year": 1966,
    "docket": "36",
    "cluster_id": 107312,
    "lead_opinion_id": 9423294,
    "sibling_ids": [
      107312,
      9423294,
      9423295
    ],
    "absolute_url": "/opinion/107312/lewis-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8965963,
        "score": 20,
        "case_name": "Marine National Exchanges Bank v. Government of the Virgin Islands"
      },
      {
        "cluster_id": 8965961,
        "score": 20,
        "case_name": "McFaddin Express, Inc. v. Adley Corp."
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "385 U.S. 206",
      "volume": "385",
      "reporter": "U.S.",
      "page": "206",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 424",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "424",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 312",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "312",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1966 U.S. LEXIS 3",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "3",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "385 U.S. 206",
        "volume": "385",
        "reporter": "U.S.",
        "page": "206",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 424",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "424",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 312",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "312",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1966 U.S. LEXIS 3",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "3",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "385 U.S. 206",
    "official_selection": {
      "court_class": "scotus",
      "selected": "385 U.S. 206",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-211",
      "page": null,
      "quote": "The agent saw, heard, and took nothing beyond what Lewis exposed and handed over as part of the drug sale. Lewis moved to suppress, arguing the agent's deception-procured entry into his home was an unconstitutional search. ## Issue Whether a government agent's entry into a home by the occupant's invitation, achieved by concealing his identity, to buy contraband as part of the occupant's illegal business constitutes a Fourth Amendment search. ## Rule No search occurs.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-211b",
      "page": null,
      "quote": "does not mean that, whenever entry is obtained by invitation and the locus is characterized as a place of business, an agent is authorized to conduct a general search for incriminating materials",
      "star_marker": "211",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 8982,
      "fragment": "#:~:text=does%20not%20mean%20that%2C%20whenever",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-210",
      "page": null,
      "quote": "During neither of his visits to petitioner's home did the agent see, hear, or take anything that was not contemplated, and in fact intended, by petitioner as a necessary part of his illegal business.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1966-12-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Lewis v. United States (1966)",
    "varies_by_point": false,
    "scope_note": "Good law; part of the settled misplaced-trust / false-friend line (Hoffa, Lopez, On Lee, later United States v. White) holding that undercover dealing with a willing party is no Fourth Amendment search.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Perry G. Blocker",
          "cluster_id": 733272,
          "cite": [
            "104 F.3d 720",
            "1997 U.S. App. LEXIS 712",
            "1997 WL 14762"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tidswell",
          "cluster_id": 8707842,
          "cite": [
            "753 F. Supp. 1001",
            "1990 U.S. Dist. LEXIS 17789",
            "1990 WL 251821"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jones v. Berry",
          "cluster_id": 8928076,
          "cite": [
            "722 F.2d 443"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Auletta",
          "cluster_id": 5994618,
          "cite": [
            "88 A.D.2d 867",
            "452 N.Y.S.2d 32",
            "1982 N.Y. App. Div. LEXIS 17187"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Barry Dean Michael, A/K/A Mike Thompson, A/K/A Mike Johnson, Defendant",
          "cluster_id": 389127,
          "cite": [
            "645 F.2d 252",
            "1981 U.S. App. LEXIS 13417"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rovinsky v. State",
          "cluster_id": 1501764,
          "cite": [
            "605 S.W.2d 578",
            "1980 Tex. Crim. App. LEXIS 1335"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pedro Amezquita v. Rafael Hernandez Colon",
          "cluster_id": 328469,
          "cite": [
            "518 F.2d 8",
            "1975 U.S. App. LEXIS 5616"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Patterson v. State",
          "cluster_id": 1371382,
          "cite": [
            "212 S.E.2d 858",
            "133 Ga. App. 742",
            "1975 Ga. App. LEXIS 2268"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "W. Thomas Holmes v. Waldon v. Burr, Sheriff of Pima County, Arizona",
          "cluster_id": 314071,
          "cite": [
            "486 F.2d 55"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Piazzola v. Watkins",
          "cluster_id": 8898665,
          "cite": [
            "442 F.2d 284"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Grady Monroe Holsen v. United States",
          "cluster_id": 292305,
          "cite": [
            "432 F.2d 47",
            "1970 U.S. App. LEXIS 7135"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Garland William Boggus",
          "cluster_id": 284907,
          "cite": [
            "411 F.2d 110"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Katz v. United States",
          "cluster_id": 107564,
          "cite": [
            "19 L. Ed. 2d 576",
            "88 S. Ct. 507",
            "389 U.S. 347",
            "1967 U.S. LEXIS 2"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coolidge v. New Hampshire",
          "cluster_id": 108377,
          "cite": [
            "29 L. Ed. 2d 564",
            "91 S. Ct. 2022",
            "403 U.S. 443",
            "1971 U.S. LEXIS 25"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCray v. Illinois",
          "cluster_id": 107394,
          "cite": [
            "18 L. Ed. 2d 62",
            "87 S. Ct. 1056",
            "386 U.S. 300",
            "1967 U.S. LEXIS 1983"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Club Retro, L.L.C. v. Hilton",
          "cluster_id": 1459439,
          "cite": [
            "568 F.3d 181",
            "2009 U.S. App. LEXIS 9864",
            "2006 WL 6245546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "White v. Davis",
          "cluster_id": 1235711,
          "cite": [
            "533 P.2d 222",
            "13 Cal. 3d 757",
            "120 Cal. Rptr. 94",
            "1975 Cal. LEXIS 208"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vincent Martino, John Torrioni, Policardo Despaigne, A/K/A \"Paulie,\" Odell Miller, A/K/A \"Pluggy,\" John Radice, and John Perry",
          "cluster_id": 397139,
          "cite": [
            "664 F.2d 860",
            "1981 U.S. App. LEXIS 16278"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Aguilar",
          "cluster_id": 8980450,
          "cite": [
            "883 F.2d 662"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Turner",
          "cluster_id": 8910590,
          "cite": [
            "528 F.2d 143"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Larry Knohl",
          "cluster_id": 276382,
          "cite": [
            "379 F.2d 427",
            "1967 U.S. App. LEXIS 5888"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hardin",
          "cluster_id": 1427400,
          "cite": [
            "539 F.3d 404",
            "2008 U.S. App. LEXIS 18135",
            "2008 WL 3891265"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Texeira",
          "cluster_id": 1409339,
          "cite": [
            "433 P.2d 593",
            "50 Haw. 138",
            "1967 Haw. LEXIS 75"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bosley v. State",
          "cluster_id": 2411414,
          "cite": [
            "414 S.W.2d 468",
            "1967 Tex. Crim. App. LEXIS 1072"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "A. A. Dietemann v. Time, Inc., a New York Corporation",
          "cluster_id": 299367,
          "cite": [
            "449 F.2d 245",
            "1 Media L. Rep. (BNA) 2417",
            "1971 U.S. App. LEXIS 8409"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David T. Lace, Roger R. Ducharme, Gary D. Butts, Patricia Eckman, and Glenn Pollack",
          "cluster_id": 398901,
          "cite": [
            "669 F.2d 46",
            "1982 U.S. App. LEXIS 22855"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dennis Roy Choate",
          "cluster_id": 355886,
          "cite": [
            "576 F.2d 165"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Theofel v. Farey-Jones",
          "cluster_id": 8438109,
          "cite": [
            "359 F.3d 1066"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Wyatt",
          "cluster_id": 1389377,
          "cite": [
            "687 P.2d 544",
            "67 Haw. 293",
            "1984 Haw. LEXIS 120"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carmine G. Desapio",
          "cluster_id": 293630,
          "cite": [
            "435 F.2d 272",
            "1970 U.S. App. LEXIS 6389"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William Ross Phillips",
          "cluster_id": 319783,
          "cite": [
            "497 F.2d 1131"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James A. White",
          "cluster_id": 283034,
          "cite": [
            "405 F.2d 838"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Arthur Fera",
          "cluster_id": 375495,
          "cite": [
            "616 F.2d 590",
            "1980 U.S. App. LEXIS 20064"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Charles B. Bradley, Jr.",
          "cluster_id": 301708,
          "cite": [
            "455 F.2d 1181"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Curtis Keith Glassel",
          "cluster_id": 315375,
          "cite": [
            "488 F.2d 143",
            "1973 U.S. App. LEXIS 6619"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Lewis v. United States (1966):lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107312 OR 9423294 OR 9423295) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 167,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 12,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 167,
        "triage_read": 15,
        "triage_snippet_classified": 152
      },
      "lane2_top_cited": {
        "query": "cites:(107312 OR 9423294 OR 9423295)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NyZzPTEwOTE0NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107312+OR+9423294+OR+9423295%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107312 OR 9423294 OR 9423295)",
        "reviewed": 6,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 6,
        "triage_read": 0,
        "triage_snippet_classified": 6
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107312 OR 9423294 OR 9423295)",
    "indexed_citing_opinions": 236,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107312,
        "count": 145,
        "count_source": "search"
      },
      {
        "opinion_id": 9423294,
        "count": 100,
        "count_source": "search"
      },
      {
        "opinion_id": 9423295,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 885,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/lewis-v-united-states-1966.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjI0OTIyMTEmcz0yNTI1NzQ5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107312+OR+9423294+OR+9423295%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107312,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 94127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 94440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 101997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 105681,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107312,
        "cited_id": 269666,
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
    "date_created": "2026-07-05T12:44:19Z",
    "date_modified": "2026-07-10T00:12:42Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T12:45:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T12:45:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T12:50:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T12:45:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Lewis v. United States (1966)

```
<opinion type="majority">
<author id="b310-15">Mr. Chief Justice Warren</author>
<p id="A82">delivered the opinion of the Court.</p>
<p id="b310-16">The question for resolution here is whether the Fourth Amendment was violated when a federal narcotics agent, <page-number citation-index="1" label="207">*207</page-number>by misrepresenting his identity and stating his willingness to purchase narcotics, was invited into petitioner’s home where an unlawful narcotics transaction was consummated and the narcotics were thereafter introduced at petitioner’s criminal trial over his objection. We hold that under the facts of this case it was not. Those facts are not disputed and may be briefly stated as follows:</p>
<p id="b311-5">On December 3, 1964, Edward Cass, an undercover federal narcotics agent, telephoned petitioner’s home to inquire about the possibility of purchasing marihuana. Cass, who previously had not met or dealt with petitioner, falsely identified himself as one “Jimmy the Pollack <em>[sic]” </em>and stated that a mutual friend had told him petitioner might be able to supply marihuana. In response, petitioner said, “Yes. I believe, Jimmy, I can take care of you,” and then directed Cass to his home where, it was indicated, a sale of marihuana would occur. Cass drove to petitioner’s home, knocked on the door, identified himself as “Jim,” and was admitted. After discussing the possibility of regular future dealings at a discounted price, petitioner led Cass to a package located on the front porch of his home. Cass gave petitioner $50, took the package, and left the premises. The package contained five bags of marihuana.<footnotemark>1</footnotemark> On December 17, 1964, a similar transaction took place, beginning with a phone conversation in which Cass identified himself as “Jimmy the Pollack” and ending with an invited visit, by Cass to petitioner’s home where a second sale of marihuana occurred. Once again, Cass paid petitioner <page-number citation-index="1" label="208">*208</page-number>$50, but this time he received in return a package containing six bags of marihuana.<footnotemark>2</footnotemark></p>
<p id="b312-6">Petitioner was arrested on April 27, 1965, and charged by a two-count indictment with violations of the narcotics laws relating to transfers of marihuana. <span class="citation no-link">26 U. S. C. § 4742</span> (a). A pretrial motion to suppress as evidence the marihuana and the conversations between petitioner and the agent was denied, and they were introduced at the trial. The District Court, sitting without a jury, convicted petitioner on both counts and imposed concurrent five-year penitentiary sentences. The Court of Appeals for the First Circuit affirmed, <span class="citation" data-id="269666"><a href="/opinion/269666/duke-lee-lewis-aka-lee-d-lewis-v-united-states/" aria-description="Citation for case: Duke Lee Lewis, A/k/a/ Lee D. Lewis v. United States">352 F. 2d 799</a></span>, and we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./382/1024/">382 U. S. 1024</a></span>.</p>
<p id="b312-7">Petitioner does not argue that he was entrapped, as he could not on the facts of this case;<footnotemark>3</footnotemark> nor does he contend that a search of his home was made or that anything other than the purchased narcotics was taken away. His only contentions are that, in the absence of a warrant, any official intrusion upon the privacy of a home constitutes a Fourth Amendment violation and that the fact the suspect invited the intrusion cannot be held a waiver when the invitation was induced by fraud and deception.</p>
<p id="b312-8">Both petitioner and the Government recognize the necessity for some undercover police activity and both concede that the particular circumstances of each case govern the admissibility of evidence obtained by stratagem or deception.<footnotemark>4</footnotemark> Indeed, it has long been acknowl<page-number citation-index="1" label="209">*209</page-number>edged by the decisions of this Court, see <em>Grimm </em>v. <em>United States, </em><span class="citation" data-id="94127"><a href="/opinion/94127/grimm-v-united-states/#610" aria-description="Citation for case: Grimm v. United States">156 U. S. 604, 610</a></span> (1895), and <em>Andrews </em>v. <em>United States, </em><span class="citation" data-id="94440"><a href="/opinion/94440/andrews-v-united-states/#423" aria-description="Citation for case: Andrews v. United States">162 U. S. 420, 423</a></span> (1896),<footnotemark>5</footnotemark> that, in the detection of many types of crime, the Government is entitled to use decoys and to conceal the identity of its agents. The various protections of the Bill of Rights, of course, provide checks upon such official deception for the protection of the individual. See, <em>e. g., Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964); <em>Trupiano </em>v. <em>United States, </em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span> (1948).</p>
<p id="b313-5">Petitioner argues that the Government overstepped the constitutional bounds in this case and places principal reliance on <em>Gouled </em>v. <em>United States, </em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span> (1921). But a short statement of that case will demonstrate how misplaced his reliance is. There, a business acquaintance of the petitioner, acting under orders of federal officers, obtained entry into the petitioner’s office by falsely representing that he intended only to pay a social visit. In the petitioner’s absence, however, the <page-number citation-index="1" label="210">*210</page-number>intruder secretly ransacked the office and seized certain private papers of an incriminating nature. This Court had no difficulty concluding that the Fourth Amendment had been violated by the secret and general ransacking, notwithstanding that the initial intrusion was occasioned by a fraudulently obtained invitation rather than by force or stealth.</p>
<p id="b314-4">In the instant case, on the other hand, the petitioner invited the undercover agent to his home for the specific purpose of executing a felonious sale of narcotics. Petitioner’s only concern was whether the agent was a willing purchaser who could pay the agreed price. Indeed, in order to convince the agent that his patronage at petitioner’s home was desired, petitioner told him that, if he became a regular customer there, he would in the future receive an extra bag of marihuana at no additional cost; and in fact petitioner did hand over an extra bag at a second sale which was consummated at the same place and in precisely the same manner. During neither of his visits to petitioner’s home did the agent see, hear, or take anything that was not contemplated, and in fact intended, by petitioner as a necessary part of his illegal business. Were we to hold the deceptions of the agent in this case constitutionally prohibited, we would come near to a rule that the use of undercover agents in any manner is virtually unconstitutional <em>per se. </em>Such a rule would, for example, severely hamper the Government in ferreting out those organized criminal activities that are characterized by covert dealings with victims who either cannot or do not protest.<footnotemark>6</footnotemark> A prime example is provided by the narcotics traffic.</p>
<p id="b315-4"><page-number citation-index="1" label="211">*211</page-number>The fact that the undercover agent entered petitioner’s home does not compel a different conclusion. Without question, the home is accorded the full range of Fourth Amendment protections. See Amos v. <em>United States, </em><span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span> (1921); <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#151" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 151, n. 15</a></span> (1947). But when, as here, the home is converted into a commercial center to which outsiders are invited for purposes of transacting unlawful business, that business is entitled to no greater sanctity than if it were carried on in a store, a garage, a car, or on the street. A government agent, in the same manner as a private person, may accept an invitation to do business and may enter upon the premises for the very purposes contemplated by the occupant. Of course, this does not mean that, whenever entry is obtained by invitation and the locus is characterized as a place of business, an agent is authorized to conduct a general search for incriminating materials; a citation to the <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>case, <em>supra, </em>is sufficient to dispose of that contention.</p>
<p id="b315-5">Finally, petitioner also relies on <em>Rios </em>v. <em>United States, </em><span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/" aria-description="Citation for case: Rios v. United States">364 U. S. 253</a></span> (1960); <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960); <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span> (1948); and <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (1948). But those cases all dealt with the exclusion of evidence that had been forcibly seized against the suspects’ desires and without the authorization conferred by search warrants. A reading of them will readily demonstrate that they are inapposite to the facts of this case; <page-number citation-index="1" label="212">*212</page-number>and, in this area, each case must be judged on its own particular facts. Nor is <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961), in point; for there, the conduct proscribed was that of eavesdroppers, unknown and unwanted intruders who furtively listened to conversations occurring in the privacy of a house. The instant case involves no such problem; it has been well summarized by the Government at the conclusion of its brief as follows:</p>
<blockquote id="b316-4">“In short, this case involves the exercise of no governmental power to intrude upon protected premises; the visitor was invited and willingly admitted by the suspect. It concerns no design on the part of a government agent to observe or hear what was happening in the privacy of a home; the suspect chose the location where the transaction took place. It presents no question of the invasion of the privacy of a dwelling; the only statements repeated were those that were willingly made to the agent and the only things taken were the packets of marihuana voluntarily transferred to him. The pretense resulted in no breach of privacy; it merely encouraged the suspect to say things which he was willing and anxious to say to anyone who would be interested in purchasing marihuana.”</blockquote>
<p id="b316-5">Further elaboration is not necessary. The judgment is</p>
<p id="b316-6">
<em>Affirmed.</em>
</p>
<p id="b316-7">[For opinion of Douglas, J., dissenting, see <em>post, </em>p. 340.]</p>
<footnote label="1">
<p id="b311-6"> In the illegal narcotics trade, an average “bag” of marihuana contains approximately five grams of marihuana. The five bags transferred to the agent by petitioner, however, contained a quantity of marihuana measuring 31.16 grams.</p>
</footnote>
<footnote label="2">
<p id="b312-9"> The six bags transferred in this second transaction contained 40.34 grams of marihuana.</p>
</footnote>
<footnote label="3">
<p id="b312-10"> Compare <em>Sherman </em>v. <em>United States, </em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">356 U. S. 369</a></span> (1958), and <em>Sorrells </em>v. <em>United States, </em><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435</a></span> (1932). See generally Mikell, The Doctrine of Entrapment in the Federal Courts, <span class="citation no-link">90 U. Pa. L. <em>Rev. </em>245</span> (1942).</p>
</footnote>
<footnote label="4">
<p id="b312-11"> In oral argument before this Court, counsel for petitioner conceded that information obtained by the agent in the course of his <page-number citation-index="1" label="209">*209</page-number>general undercover investigation, together with the subject matter of the first telephone conversation between the agent and petitioner, provided probable cause for believing that a narcotics offense would be committed in petitioner’s home and, therefore, would have supported the issuance of a search warrant. According to counsel, the agent’s misrepresentations would not have vitiated a magistrate’s determination of probable cause. Counsel further suggested that, if the agent had arrested petitioner at the latter’s home and then had conducted a search incidental to the arrest, no constitutional problems would be presented.</p>
</footnote>
<footnote label="5">
<p id="b313-10"> Former Chief Justice Hughes commented as follows upon the use of official deception in combating criminal activity:</p>
<blockquote id="b313-11">“Artifice and stratagem may be employed to catch those engaged in criminal enterprises. . . . The appropriate object of this permitted activity, frequently essential to the enforcement of the law, is to reveal the criminal design; to expose the illicit traffic, the prohibited publication, the fraudulent use of the mails, the illegal conspiracy, or other offenses, and thus to disclose the would-be violators of the law.” <em>Sorrells </em>v. <em>United States, </em><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#441" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435, 441-442</a></span> (1932).</blockquote>
</footnote>
<footnote label="6">
<p id="b314-5"> “Particularly, in the enforcement of vice, liquor or narcotics laws, it is all but impossible to obtain evidence for prosecution save by the use of decoys. There are rarely complaining witnesses. The participants in the crime enjoy themselves. Misrepresentation by a police officer or agent concerning the identity of the purchaser of <page-number citation-index="1" label="211">*211</page-number>illegal narcotics is a practical necessity. . . . Therefore, the law must attempt to distinguish between those deceits and persuasions which are permissible and those which are not.” Model Penal Code §2.10, comment, p. 16 (Tent. Draft No. 9, 1959).</p>
<p id="b315-7">See also Donnelly, Judicial Control of Informants, Spies, Stool Pigeons and Agent Provocateurs, 60 Yale L. J. 1091, 1094 (1951); Note, <span class="citation no-link">73 Harv. L. Rev. 1333</span>, 1338-1339 (1960).</p>
</footnote>
</opinion>
```

---
