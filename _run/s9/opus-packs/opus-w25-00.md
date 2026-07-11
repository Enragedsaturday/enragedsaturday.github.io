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

## GROUP: _overhaul2/lake/cases/united-states-v-holcomb--10670143.json  (`lake-record`, 1 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ceedb0baab96a3b7", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-holcomb--10670143"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-holcomb--10670143", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-holcomb--10670143

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-holcomb--10670143",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "United States v. Holcomb",
    "case_name_short": "Holcomb",
    "case_name_full": "",
    "input_case_name": "United States v. Holcomb",
    "court": "9th Cir. 2025",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": "2025-09-11",
    "year": 2025,
    "docket": "23-469",
    "cluster_id": 10670143,
    "lead_opinion_id": 11136730,
    "sibling_ids": [],
    "absolute_url": "/opinion/10670143/united-states-v-holcomb/",
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
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "9th Cir. order 2025-09-11 WITHDREW the 2025-03-27 opinion (had appeared at 132 F.4th 1118) and marked it non-citable; no superseding published cite exists now.",
      "legs": [
        {
          "source": "Court PDF",
          "url": "https://cdn.ca9.uscourts.gov/datastore/opinions/2025/09/11/23-469.pdf",
          "cite": "No. 23-469 order withdrawing 132 F.4th 1118, non-precedential"
        },
        {
          "source": "Official court",
          "url": "https://fourthamendment.com/?p=60612",
          "cite": "CA9 Holcomb opinion flagged withdrawn"
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
    "date_created": "2026-07-06T05:53:50Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:53:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:53:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:53:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:53:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — united-states-v-holcomb--10670143

```
                              FOR PUBLICATION                             FILED
                    UNITED STATES COURT OF APPEALS                        SEP 11 2025
                                                                      MOLLY C. DWYER, CLERK
                                                                        U.S. COURT OF APPEALS
                           FOR THE NINTH CIRCUIT

UNITED STATES OF AMERICA,                       No. 23-469
                                                D.C. No.
             Plaintiff - Appellee,              2:21-cr-00075-RSL-1
                                                Western District of Washington,
 v.
                                                Seattle
JOHN HOLCOMB,                                   ORDER

             Defendant - Appellant.

Before: GRABER and SUNG, Circuit Judges, and RAKOFF, District Judge.*

      The Opinion filed March 27, 2025, and appearing at 132 F.4th 1118 (9th Cir.

2025), is withdrawn. It may not be cited as precedent by or to this court or any

district court of the Ninth Circuit. The court will file a new opinion in due course.

Because the court’s opinion is withdrawn, the petition for rehearing en banc is

DENIED as moot. Once a new opinion is filed, further petitions for rehearing and

rehearing en banc may be filed.




      *
            The Honorable Jed S. Rakoff, United States District Judge for the
Southern District of New York, sitting by designation.

```

---

## GROUP: _overhaul2/lake/cases/united-states-v-kennedy--700649.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "49d3b2440522c943", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "united-states-v-kennedy--700649"}, "payload": {"all": [{"cite": "61 F.3d 494", "page": "494", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "61"}, {"cite": "1995 WL 461520", "page": "461520", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "1995"}], "display": "61 F.3d 494", "official": {"cite": "61 F.3d 494", "page": "494", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "61"}, "official_selection_present": true, "record_id": "united-states-v-kennedy--700649"}}
{"assertion_id": "acd57ac505a93df3", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-kennedy--700649"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-kennedy--700649", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-kennedy--700649

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-kennedy--700649",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "United States v. Arre Kennedy",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Arre KENNEDY, Defendant-Appellant",
    "input_case_name": "United States v. Kennedy",
    "court": "U.S. Court of Appeals, 6th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca6",
    "state": null,
    "date_decided": null,
    "year": 1995,
    "docket": null,
    "cluster_id": 700649,
    "lead_opinion_id": 700649,
    "sibling_ids": [],
    "absolute_url": "/opinion/700649/united-states-v-arre-kennedy/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "61 F.3d 494",
      "volume": "61",
      "reporter": "F.3d",
      "page": "494",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1995 WL 461520",
        "volume": "1995",
        "reporter": "WL",
        "page": "461520",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "61 F.3d 494",
        "volume": "61",
        "reporter": "F.3d",
        "page": "494",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1995 WL 461520",
        "volume": "1995",
        "reporter": "WL",
        "page": "461520",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "61 F.3d 494",
    "official_selection": {
      "court_class": "coa",
      "selected": "61 F.3d 494",
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
    "date_created": "2026-07-06T13:43:29Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:43:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:43:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:43:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:43:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — united-states-v-kennedy--700649

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b599-24">
  TODD, District Judge.
 </author>
<p id="b599-25">
  Defendant appeals his conviction following a conditional plea of guilty to a charge of conspiracy to distribute and to possess with the intent to distribute cocaine in violation of <span class="citation no-link">21 U.S.C. §§ 841</span>(a)(1) and 846. On appeal, the only issue is whether cocaine seized in a warrantless search of defendant’s suitcase was admissible under the inevitable discovery exception to the exclusionary rule. For the reasons set forth below, we AFFIRM the judgment of the district court.
 </p>
<p id="b599-26">
  I.
 </p>
<p id="b599-27">
  A.
 </p>
<p id="b599-28">
  On July 25,1993, defendant Arre Kennedy flew from Detroit, Michigan, to Miami, Florida, on Northwest Airlines flight 991. Defendant checked two locked pieces of luggage, a blue suitcase and a black suitcase. North
  <span citation-index="1" class="star-pagination" label="496"> 
   *496
   </span>
  west mistakenly labeled defendant’s suitcases with tags bearing the name of Wesley Kennedy, a Northwest passenger unrelated to defendant. As a result, defendant’s suitcases were misrouted and sent to National Airport in Washington, D.C. At National Airport, Wesley Kennedy, who had flown from Detroit to Washington, discovered that his own bag was missing and reported the problem to Northwest employee, Deborah Hawkins-Garner. Hawkins-Garner showed defendant’s two suitcases, each of which had a tag bearing the initials A-W-K, to Wesley Kennedy who informed her that the suitcases were not his.
 </p>
<p id="b600-4">
  Northwest’s policy regarding lost luggage was to open the suitcase to check for identification and, if there was no identification, to inventory the contents. Pursuant to that policy, Hawkins-Garner decided to open the suitcases to see if they contained any identification. She was unable to open the black suitcase because it had a combination lock. However, she was able to open the blue suitcase since it had a lock that could be opened with a Northwest key. The blue suitcase contained $176,000, which was promptly reported to the Metropolitan Washington Airport Authority Police Department.
 </p>
<p id="b600-5">
  Officer Simon Mantel answered the call and was later joined by Sergeant Arthur Taplett. Sergeant Taplett was suspicious of the contents of the black suitcase because a strong odor of perfume was emanating from it. Because of a concern that the suitcase might contain explosives, Sergeant Taplett had it x-rayed, which revealed a number of dense, rectangular-shaped objects with an almost metallic appearance, although approximately one-fourth of the contents was indiscernible. Officer Mantel remained with the suitcases while Sergeant Taplett began making arrangements to move the suitcases to the airport police station.
 </p>
<p id="b600-6">
  At that point, Hawkins-Garner decided to go ahead and open the black suitcase. After receiving permission from her supervisor to open the bag, she obtained a hammer and a screwdriver and asked Officer Mantel to open it for her. He advised Sergeant Taplett on the radio that Hawkins-Garner had asked him to open the black suitcase and asked if there was a problem with that. Sergeant Taplett replied that Officer Mantel could open the suitcase if Northwest wanted it opened. Officer Mantel then used the hammer and screwdriver to force open the lock on the suitcase. Inside were a number of rectangular-shaped packages "wrapped in brown duct tape. Officer Mantel did not try to open the packages.
 </p>
<p id="b600-8">
  In response to an earlier phone call from another airport police sergeant, Special Agent Ed Curley of the Drug Enforcement Administration (“DEA”) arrived. He suspected that the suitcase contained drugs based on the packaging and the presence of the perfume odor. Agents conducted a field test on the contents of one of the packages and established that it contained cocaine. It was determined that the suitcase contained 17 kilograms of cocaine and 77 grams of cocaine base.
 </p>
<p id="b600-9">
  Shortly thereafter, Northwest in Washington, D.C., was notified that defendant had arrived in Miami and was looking for his suitcases. DEA agents arranged for a controlled delivery of the suitcases to defendant. The next day, defendant and his son picked up the suitcases in Miami. As they were leaving, agents arrested Defendant after he admitted that the suitcases belonged to him. Defendant confessed that he had been trafficking drugs from Miami to Detroit for several months. A consensual search of defendant’s home produced an additional $225,000 in cash.
 </p>
<p id="b600-10">
  B.
 </p>
<p id="b600-11">
  On August 26, 1993, a federal grand jury-returned a two-count indictment against defendant charging him with conspiracy to distribute and to possess with the intent to distribute cocaine in violation of <span class="citation no-link">21 U.S.C. §§ 841</span>(a)(1) and 846 and with possession of cocaine with intent to distribute in violation of <span class="citation no-link">21 U.S.C. § 841</span>(a)(1).
 </p>
<p id="b600-12">
  Defendant moved to suppress the cocaine seized from his black suitcase and all the evidence that resulted therefrom. The district court held an evidentiary hearing and denied the motion based on the inevitable discovery exception to the exclusionary rule.
 </p>
<p id="b601-3">
<span citation-index="1" class="star-pagination" label="497"> 
   *497
   </span>
  On May 13, 1994, defendant entered a conditional plea of guilty to conspiracy to distribute cocaine, reserving his right to appeal the denial of his motion to suppress pursuant to Rule 11(a)(2) of the Federal Rules of Criminal Procedure. The government agreed to dismiss the possession count at sentencing. On August 26, 1994, the district court sentenced defendant to the statutory mandatory minimum of 120 months imprisonment, five years of supervised release, a fine of $5000, and a special assessment of $50. The district court granted defendant bond pending appeal. This timely appeal followed.
 </p>
<p id="b601-4">
  II.
 </p>
<p id="b601-5">
  Defendant contends that the district court erred in denying his motion to suppress because the government failed to establish that the cocaine inevitably would have been discovered by lawful means. “[T]his court reviews a district court’s decision on a motion to suppress under two complementary standards.”
  <em>
   United States v. Leake,
  </em>
  <span class="citation" data-id="611584"><a href="/opinion/611584/united-states-v-charles-v-leake/#1362" aria-description="Citation for case: United States v. Charles v. Leake">998 F.2d 1359, 1362</a></span> (6th Cir.1993). “A district court’s factual findings made in consideration of a motion to suppress evidence are to be upheld unless they are clearly erroneous. However, the district court’s conclusions of law are subject to de novo review on appeal. The reviewing court is to review the evidence ‘in the light most likely to support the district court’s decision.’ ”
  <em>
   United States v. Williams,
  </em>
  <span class="citation" data-id="582715"><a href="/opinion/582715/united-states-v-raymond-williams-91-1025-kevin-t-wilson/#1221" aria-description="Citation for case: United States v. Raymond Williams (91-1025), Kevin T....">962 F.2d 1218, 1221</a></span> (6th Cir.) (citations omitted),
  <em>
   cert. denied,
  </em>
  — U.S. —, <span class="citation multiple-matches"><a href="/c/S.Ct./113/264/">113 S.Ct. 264</a></span>, <span class="citation no-link">121 L.Ed.2d 194</span> (1992). Mixed questions of law and fact are reviewed de novo.
  <em>
   United States v. Clark,
  </em>
  <span class="citation" data-id="597446"><a href="/opinion/597446/united-states-v-tyrez-clark/#968" aria-description="Citation for case: United States v. Tyrez Clark">982 F.2d 965, 968</a></span> (6th Cir.1993). Because we believe the applicability of the inevitable discovery exception to this case is a mixed question, we shall review the district court’s decision de novo.
  <em>
   See United States v. Boatwright,
  </em>
  <span class="citation" data-id="490618"><a href="/opinion/490618/united-states-v-rickie-lee-boatwright/" aria-description="Citation for case: United States v. Rickie Lee Boatwright">822 F.2d 862</a></span> (9th Cir.1987) (panel implicitly reviewed the application of the inevitable discovery doctrine de novo by its extensive review of the facts and the doctrine itself).
 </p>
<p id="b601-7">
  The exclusionary rule prohibits the admission of evidence seized in searches and seizures that are deemed unreasonable under the Fourth Amendment, as well as derivative evidence acquired as a result of an unlawful search.
  <em>
   Wong Sun v. United States,
  </em>
  <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#484" aria-description="Citation for case: Wong Sun v. United States">371 U.S. 471, 484-85</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#416" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407, 416</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">9 L.Ed.2d 441</a></span> (1963). The inevitable discovery doctrine, an exception to the exclusionary rule, allows unlawfully obtained evidence to be admitted at trial if the government can prove by a preponderance that the evidence inevitably would have been acquired through lawful means.
  <em>
   Nix v. Williams,
  </em>
  <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#444" aria-description="Citation for case: Nix v. Williams">467 U.S. 431, 444</a></span>, <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#2509" aria-description="Citation for case: Nix v. Williams">104 S.Ct. 2501, 2509</a></span>, <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">81 L.Ed.2d 377</a></span> (1984). In approving the inevitable discovery exception, the Supreme Court reasoned that “[i]f the prosecution can establish by a preponderance of the evidence that the information ultimately or inevitably would have been discovered by lawful means ... then the deterrence rationale has so little basis that the evidence should be received.”
  <em>
   <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">Id.</a></span>
  </em>
</p>
<blockquote id="A27M">
  Fairness can be assured by placing the State and the accused in the same positions they would have been in had the impermissible conduct not taken place. However, if the government can prove that the evidence would have been obtained inevitably and, therefore, would have been admitted regardless of any overreaching by the police, there is no rational basis to keep that evidence from the jury in order to ensure the fairness of the trial proceedings. In that situation the State has gained no advantage at trial and the defendant has suffered no prejudice. Indeed, suppression of the evidence would operate to undermine the adversary system by putting the State in a worse position than it would have occupied without any police misconduct.
 </blockquote>
<p id="b601-9">
<span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#447" aria-description="Citation for case: Nix v. Williams"><em>
   Id.
  </em>
  at 447</a></span>, <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#2511" aria-description="Citation for case: Nix v. Williams">104 S.Ct. at 2511</a></span>. Therefore, when “the evidence in question would inevitably have been discovered without reference to the police error or misconduct, there is no nexus sufficient to provide a taint and the evidence is admissible.”
  <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#448" aria-description="Citation for case: Nix v. Williams"><em>
   Id.
  </em>
  at 448</a></span>, <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#2511" aria-description="Citation for case: Nix v. Williams">104 S.Ct. at 2511</a></span>.
 </p>
<p id="b601-10">
  For the inevitable discovery exception to apply, it must be demonstrated that the evidence inevitably would have been acquired through lawful means had the government misconduct not occurred.
  <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#444" aria-description="Citation for case: Nix v. Williams"><em>
   Id.
  </em>
  at 444</a></span>, <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#2509" aria-description="Citation for case: Nix v. Williams">104 S.Ct. at 2509</a></span>;
  <em>
   see Murray v. United States,
  </em>
  <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#539" aria-description="Citation for case: Murray v. United States">487 U.S. 533, 539</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#2534" aria-description="Citation for case: Murray v. United States">108 S.Ct. 2529, 2534</a></span>, 101
  <span citation-index="1" class="star-pagination" label="498"> 
   *498
   </span>
  L.Ed.2d 472 (1988). Proof of inevitable discovery “involves no speculative elements but focuses on demonstrated historical facts capable of ready verification or impeachment and does not require a departure from the usual burden of proof at suppression hearings.”
  <em>
   Nix,
  </em>
  <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">467 U.S. at 444</a></span> n. 5, <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">104 S.Ct. at 2509</a></span> n. 5. “The exception requires the district court to determine, viewing affairs as they existed at the instant before the unlawful search, what would have happened had the unlawful search never occurred.”
  <em>
   United States v, Eng,
  </em>
  <span class="citation multiple-matches"><a href="/c/F.2d/971/854/">971 F.2d 854</a></span>, 861 (2d Cir.1992), ce
  <em>
   rt. denied,
  </em>
  — U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./114/693/">114 S.Ct. 693</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/126/660/">126 L.Ed.2d 660</a></span> (1994). With these general principles in mind, we turn to defendant’s arguments on appeal.
 </p>
<p id="b602-5">
  Defendant acknowledges that the inevitable discovery exception applies when, at the time of the unlawful search, there was a separate independent line of investigation underway or there are compelling facts indicating that the disputed evidence would have inevitably been discovered, such as proof that the evidence would have been found in an inventory search that would inevitably follow seizure of a car.
  <em>
   See United States v. Johnson,
  </em>
  <span class="citation" data-id="9486670"><a href="/opinion/668574/united-states-v-lee-erwin-johnson/#684" aria-description="Citation for case: United States v. Lee Erwin Johnson">22 F.3d 674, 684</a></span> (6th Cir.1994) and
  <em>
   United States v. Buchanan,
  </em>
  <span class="citation" data-id="542344"><a href="/opinion/542344/united-states-v-david-buchanan/#356" aria-description="Citation for case: United States v. David Buchanan">904 F.2d 349, 356-57</a></span> (6th Cir.1990). Defendant argues that his motion to suppress should have been granted because, at the time of the search, there was no independent investigation underway nor are there historical facts demonstrating that a private search was inevitable.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
</p>
<p id="b602-6">
  Whether an independent line of investigation is required for the inevitable discovery exception to apply is a question that has divided the circuits. Some circuits have refused to apply the inevitable discovery exception absent an independent line of investigation.
  <em>
   See, e.g., United States v. Owens,
  </em>
  <span class="citation" data-id="463621"><a href="/opinion/463621/united-states-v-merle-ellis-owens/#152" aria-description="Citation for case: United States v. Merle Ellis Owens">782 F.2d 146, 152-53</a></span> (10th Cir.1986) (refusing to apply the inevitable discovery exception because at the time the evidence was illegally discovered, there was no independent, untainted investigation that inevitably would have uncovered the same evidence);
  <em>
   United States v. Cherry,
  </em>
  <span class="citation" data-id="450747"><a href="/opinion/450747/united-states-v-james-thomas-cherry/#1205" aria-description="Citation for case: United States v. James Thomas Cherry">759 F.2d 1196, 1205-06</a></span> (5th Cir.1985) (holding that “[i]n order for the [inevitable discovery] exception to apply, the prosecution must demonstrate both a reasonable possibility that the evidence would have been discovered in the absence of police misconduct and that the government was actively pursuing a substantial alternate line of investigation at the time of the constitutional violation”),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./479/1056/">479 U.S. 1056</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./107/932/">107 S.Ct. 932</a></span>, <span class="citation no-link">93 L.Ed.2d 983</span> (1987);
  <em>
   United States v. Satterfield,
  </em>
  <span class="citation" data-id="8924377"><a href="/opinion/8934150/united-states-v-satterfield/#846" aria-description="Citation for case: United States v. Satterfield">743 F.2d 827, 846</a></span> (11th Cir.1984) (stating that “if evidence is obtained by illegal conduct, the illegality can be cured only if the police possessed and were pursuing a lawful means of discovery at the time the illegality occurred”),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./471/1117/">471 U.S. 1117</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./105/2362/">105 S.Ct. 2362</a></span>, <span class="citation" data-id="9047582"><a href="/opinion/9054077/presbytery-of-elijah-parish-lovejoy-v-jaeggi/" aria-description="Citation for case: Presbytery of Elijah Parish Lovejoy v. Jaeggi">86 L.Ed.2d 262</a></span> (1985).
 </p>
<p id="b602-11">
  Other circuits, however, have rejected this requirement.
  <em>
   See, e.g., United States v. Thomas,
  </em>
  <span class="citation" data-id="577024"><a href="/opinion/577024/united-states-v-craig-lawrence-thomas/#210" aria-description="Citation for case: United States v. Craig Lawrence Thomas">955 F.2d 207, 210-11</a></span> (4th Cir.1992) (rejecting the requirement that there be an alternative line of investigation for the inevitable discovery exception to apply),
  <em>
   cert. denied,
  </em>
  — U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./115/98/">115 S.Ct. 98</a></span>, <span class="citation no-link">130 L.Ed.2d 47</span> (1994);
  <em>
   United States v. Ramirez-Sandoval,
  </em>
  <span class="citation" data-id="521934"><a href="/opinion/521934/united-states-v-jesus-ramirez-sandoval/#1399" aria-description="Citation for case: United States v. Jesus Ramirez-Sandoval">872 F.2d 1392, 1399</a></span> (9th Cir.1989) (holding that the inevitable discovery exception does not require that the tainted evidence be obtained from a previously initiated, independent investigation);
  <em>
   United States v. Fitzharris,
  </em>
  <span class="citation" data-id="383555"><a href="/opinion/383555/united-states-v-cyril-b-fitzharris-archie-edwin-whatley-and-arturo/#421" aria-description="Citation for case: United States v. Cyril B. Fitzharris, Archie Edwin...">633 F.2d 416, 421</a></span> (5th Cir.1980) (allowing the admission of evidence that was initially obtained through an illegal search when a valid warrant was subsequently obtained on the ground that the evidence inevitably would have been discovered under the warrant),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./451/988/">451 U.S. 988</a></span>, <span class="citation no-link">101 S.Ct. 2825</span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/68/847/">68 L.Ed.2d 847</a></span> (1981). Although this court has considered this issue at least twice, it has never addressed it directly.
  <em>
   See United States v. Johnson,
  </em>
  <span class="citation" data-id="9486670"><a href="/opinion/668574/united-states-v-lee-erwin-johnson/#684" aria-description="Citation for case: United States v. Lee Erwin Johnson">22 F.3d 674, 684</a></span> (6th Cir.1994) and
  <em>
   United States v. Buchanan,
  </em>
  <span class="citation" data-id="542344"><a href="/opinion/542344/united-states-v-david-buchanan/#356" aria-description="Citation for case: United States v. David Buchanan">904 F.2d 349, 356-57</a></span> (6th Cir.1990).
 </p>
<p id="b602-13">
<em>
   <span class="citation" data-id="542344"><a href="/opinion/542344/united-states-v-david-buchanan/" aria-description="Citation for case: United States v. David Buchanan">Buchanan</a></span>
  </em>
  involved the admissibility of evidence seized by drug enforcement agents during a warrantless search of the defendant’s residence.
  <em>
   Buchanan,
  </em>
  <span class="citation" data-id="542344"><a href="/opinion/542344/united-states-v-david-buchanan/#350" aria-description="Citation for case: United States v. David Buchanan">904 F.2d at 350</a></span>. The government, relying on
  <em>
   United
  </em>
<span citation-index="1" class="star-pagination" label="499"> 
   *499
   </span>
<em>
   States v. Webb,
  </em>
  <span class="citation" data-id="473689"><a href="/opinion/473689/united-states-v-keith-bryan-webb/#62" aria-description="Citation for case: United States v. Keith Bryan Webb">796 F.2d 60, 62</a></span> (5th Cir.1986), ce
  <em>
   rt. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./479/1038/">479 U.S. 1038</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./107/894/">107 S.Ct. 894</a></span>, <span class="citation no-link">93 L.Ed.2d 846</span> (1987), argued that the inevitable discovery exception permits admission of the evidence if the government can satisfy the following three-part test:
 </p>
<blockquote id="b603-4">
  (1) a reasonable probability that the evidence in question would have been discovered by lawful means but for the police misconduct; (2) that the police possessed the leads making the discovery inevitable at the time of the misconduct; and (3) that the police were actively pursuing [an] alternate line of investigation prior to the misconduct.
 </blockquote>
<p id="b603-5">
<span class="citation no-link"><em>
   Id.
  </em>
  at 356</span>.
 </p>
<p id="b603-6">
  Because the agents were not pursuing an alternate line of investigation, this court rejected the government’s claim that the three-part test was satisfied. “[P]rior to initiating the warrant application for the [defendant’s] residence, the agents made an illegal entry into the home which ‘tainted the only ... investigation that was ongoing.’ ”
  <em>
   <span class="citation no-link">Id.</span>
  </em>
  at 357 (quoting
  <em>
   United States v. Owens,
  </em>
  <span class="citation" data-id="463621"><a href="/opinion/463621/united-states-v-merle-ellis-owens/#152" aria-description="Citation for case: United States v. Merle Ellis Owens">782 F.2d 146, 152</a></span> (10th Cir.1986)).
  <em>
   <span class="citation" data-id="542344"><a href="/opinion/542344/united-states-v-david-buchanan/" aria-description="Citation for case: United States v. David Buchanan">Buchanan</a></span>
  </em>
  did not adopt the three-part test advanced by the government as a necessary requirement to the application of the inevitable discovery exception. Instead, it simply rejected the government’s argument that the inevitable discovery exception permitted admission of the evidence under the three-part test.
  <span class="citation" data-id="542344"><a href="/opinion/542344/united-states-v-david-buchanan/#356" aria-description="Citation for case: United States v. David Buchanan"><em>
   Id.
  </em>
  at 356-57</a></span>.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b603-7">
<em>
   United States v. Johnson,
  </em>
  <span class="citation" data-id="9486670"><a href="/opinion/668574/united-states-v-lee-erwin-johnson/" aria-description="Citation for case: United States v. Lee Erwin Johnson">22 F.3d 674</a></span> (6th Cir.1994), clarifies the point.
  <em>
   <span class="citation" data-id="9486670"><a href="/opinion/668574/united-states-v-lee-erwin-johnson/" aria-description="Citation for case: United States v. Lee Erwin Johnson">Johnson</a></span>,
  </em>
  which involved the admissibility of guns seized by police during a warrantless search of the defendant’s apartment, did not fit
  <em>
   <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">Nix</a></span>
  </em>
  because “there was no other independent line of investigation or compelling facts illustrating that the guns would have inevitably been discovered.”
  <em>
   Id.
  </em>
  at 684. This court quoted with approval
  <em>
   United States v. Boatwright,
  </em>
  <span class="citation" data-id="490618"><a href="/opinion/490618/united-states-v-rickie-lee-boatwright/" aria-description="Citation for case: United States v. Rickie Lee Boatwright">822 F.2d 862</a></span> (9th Cir.1987), which held that the inevitable discovery exception does not require that the tainted evidence be obtained from a previously initiated, independent investigation:
 </p>
<blockquote id="b603-11">
  “There will be instances where, based on the historical facts, inevitability is demonstrated in such a compelling way that operation of the exclusionary rule is a mechanical and entirely unrealistic bar, preventing the trier of fact from learning what would have come to light in any case. In such cases, the inevitable discovery doctrine will permit introduction of the evidence whether or not two independent investigations were in progress.”
 </blockquote>
<p id="b603-12">
<em>
   Johnson,
  </em>
  <span class="citation" data-id="9486670"><a href="/opinion/668574/united-states-v-lee-erwin-johnson/" aria-description="Citation for case: United States v. Lee Erwin Johnson">22 F.3d at 684</a></span> (quoting
  <em>
   Boatwright,
  </em>
  <span class="citation" data-id="490618"><a href="/opinion/490618/united-states-v-rickie-lee-boatwright/#864" aria-description="Citation for case: United States v. Rickie Lee Boatwright">822 F.2d at 864</a></span>).
 </p>
<p id="b603-13">
  These cases lead to the conclusion that the inevitable discovery exception to the exclusionary rule applies when the government can demonstrate
  <em>
   either
  </em>
  the existence of an independent, untainted investigation that inevitably would have uncovered the same evidence
  <em>
   or
  </em>
  other compelling facts establishing that the disputed evidence inevitably would have been discovered. Therefore, we hold that an alternate, independent line of investigation is not required for the inevitable dis
  <span citation-index="1" class="star-pagination" label="500"> 
   *500
   </span>
  covery exception to apply. We now turn to the facts of this case.
 </p>
<p id="b604-3">
  It is undisputed that there was no independent line of investigation underway at the time of the warrantless search of the black suitcase by the airport police. Therefore, we must determine whether the district court erred in finding that there were compelling facts establishing that the disputed evidence inevitably would have been discovered in any event.
 </p>
<p id="b604-4">
  In denying the motion to suppress, the district court stated:
 </p>
<blockquote id="b604-5">
  The police misconduct in this case was the warrantless search of the black suitcase, thus the Court must consider what would have happened had the illegal search not occurred. Had the police acted lawfully, once the bag was seized and it was determined that it posed no danger of exploding, they would have sought a search warrant. The government concedes that under the facts of this case, it is unlikely that a search warrant would have been issued ... If the police had been unable to secure a warrant, they would have been required to return the suitcase to Northwest Airlines unopened. Northwest would then have opened the suitcase, pursuant to its lost luggage policy, in an effort to locate its owner.
 </blockquote>
<p id="b604-6">
  J.A. 21. The district court then determined that “[t]he proper application of the inevitable discovery rule can only lead to the conclusion that, absent the illegal retention ... of the suitcase, the airport police would have returned the suitcase to Northwest, which would have searched it.” J.A. 22. The court concluded that, because an identification search by Northwest would have been a search by a private entity, the Fourth Amendment would not have been violated. Therefore, the district court ruled that the cocaine discovered in the search and the evidence derived therefrom were admissible under the inevitable discovery exception.
 </p>
<p id="b604-7">
  In
  <em>
   United States v. Ramirez-Sandoval,
  </em>
  <span class="citation" data-id="521934"><a href="/opinion/521934/united-states-v-jesus-ramirez-sandoval/#1399" aria-description="Citation for case: United States v. Jesus Ramirez-Sandoval">872 F.2d 1392, 1399</a></span> (9th Cir.1989), the Ninth Circuit held that the government can meet its burden of showing that the tainted evidence inevitably would have been discovered through lawful means “by establishing that, by following routine procedures, the police would inevitably have uncovered the evidence.” In that case, the court cited two cases involving evidence that inevitably would have been discovered pursuant to a standard procedure.
  <em>
   See United States v. Martinez-Gallegos,
  </em>
  <span class="citation" data-id="480631"><a href="/opinion/480631/united-states-v-manuel-martinez-gallegos/#870" aria-description="Citation for case: United States v. Manuel Martinez-Gallegos">807 F.2d 868, 870</a></span> (9th Cir.1987) (information inevitably would have been obtained as next step by consulting defendant’s immigration file even absent unwarned statements);
  <em>
   United States v. Andrade,
  </em>
  <span class="citation" data-id="9474578"><a href="/opinion/465419/united-states-v-jose-francisco-andrade/#1433" aria-description="Citation for case: United States v. Jose Francisco Andrade">784 F.2d 1431, 1433</a></span> (9th Cir.1986) (evidence inevitably would have been discovered by following routine booking procedure and inventory). The Second, Fourth, and Fifth Circuits agree.
  <em>
   See United States v. Seals,
  </em>
  <span class="citation" data-id="601810"><a href="/opinion/601810/united-states-v-joseph-noel-seals/#1107" aria-description="Citation for case: United States v. Joseph Noel Seals">987 F.2d 1102, 1107-08</a></span> (6th Cir.) (applying the inevitable discovery exception to evidence obtained in the illegal search of a vehicle when the officer had already decided to impound the vehicle and police department inventory procedures required the inventory of impounded vehicles),
  <em>
   cert. denied,
  </em>
  — U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./114/166/">114 S.Ct. 166</a></span>, <span class="citation no-link">126 L.Ed.2d 116</span> (1993);
  <em>
   United States v. Perea,
  </em>
  <span class="citation" data-id="600741"><a href="/opinion/600741/united-states-v-ruben-perea/#644" aria-description="Citation for case: United States v. Ruben Perea">986 F.2d 633, 644</a></span> (2d Cir.1993) (holding that the contents of a bag that was illegally searched would be admissible if the items inevitably would have been discovered during a valid inventory search);
  <em>
   United States v. George,
  </em>
  <span class="citation" data-id="588130"><a href="/opinion/588130/united-states-v-cyrus-jonathan-george/#1121" aria-description="Citation for case: United States v. Cyrus Jonathan George">971 F.2d 1113, 1121-22</a></span> (4th Cir.1992) (concluding that evidence found during a search incident to an invalid arrest would be admissible if it inevitably would have been discovered pursuant to a standard inventory search of a lawfully impounded vehicle).
 </p>
<p id="b604-11">
  We believe that the existence of a routine procedure such as Northwest’s policy regarding lost luggage satisfies the requirement that there be compelling facts illustrating that the disputed evidence inevitably would have been discovered.
 </p>
<p id="b604-12">
  Prior to the intervention of the airport police, Hawkins-Garner had already decided to open the suitcases pursuant to Northwest’s policy of opening lost luggage. Even after the airport police arrived, Hawkins-Garner still thought she should open the suitcase because she considered it to be in Northwest’s custody. Hawkins-Garner testified that she would have opened the suitcase herself or had another employee to do so if Officer Mantel had not opened it for her. Therefore, it is clear that, pursuant to Northwest’s lost luggage policy, Hawkins-Garner
  <span citation-index="1" class="star-pagination" label="501"> 
   *501
   </span>
  would have opened the black suitcase and discovered the evidence in a private search had the airport police not become involved. Because a private search was inevitable, the cocaine is admissible pursuant to the inevitable discovery exception to the exclusionary rule.
 </p>
<p id="b605-4">
  Our conclusion is bolstered by
  <em>
   United States v. Hernandez-Cano,
  </em>
  <span class="citation" data-id="481088"><a href="/opinion/481088/united-states-v-genaro-rafael-hernandez-cano/" aria-description="Citation for case: United States v. Genaro Rafael Hernandez-Cano">808 F.2d 779</a></span> (11th Cir.),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./482/918/">482 U.S. 918</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./107/3194/">107 S.Ct. 3194</a></span>, <span class="citation" data-id="9063025"><a href="/opinion/9069308/easley-v-petsock/" aria-description="Citation for case: Easley v. Petsock">96 L.Ed.2d 682</a></span> (1987), in which an x-ray of the defendant’s cany-on bag revealed a large mass. The defendant voluntarily opened the bag wide enough for an airport security officer to observe a large bundle that appeared to be a white powder which could have been an explosive. When the defendant refused to permit further inspection, he was told that he could not pass through the security checkpoint.
  <span class="citation" data-id="9063025"><a href="/opinion/9069308/easley-v-petsock/#780" aria-description="Citation for case: Easley v. Petsock"><em>
   Id.
  </em>
  at 780</a></span>. The defendant then transferred the bundle from his carry-on bag to his checked luggage. As he passed the airport security officer, he stated that he had thrown away the bundle.
 </p>
<p id="b605-5">
  When Fleck, a ticket agent supervisor, was made aware of what had transpired, she became concerned about the safety of the aircraft. She went to the baggage area accompanied by Singleton, a police officer.
  <span class="citation" data-id="9063025"><a href="/opinion/9069308/easley-v-petsock/#781" aria-description="Citation for case: Easley v. Petsock"><em>
   Id.
  </em>
  at 781</a></span>. Fleck opened one of the defendant’s suitcases and began to search it by reaching in and feeling around its edges. Singleton, who had been looking over Fleck’s shoulder, reached inside the suitcase and pulled out a large bundle which was later determined to be cocaine.
  <span class="citation" data-id="9063025"><a href="/opinion/9069308/easley-v-petsock/#782" aria-description="Citation for case: Easley v. Petsock"><em>
   Id.
  </em>
  at 782</a></span>. Fleck testified that had Singleton not reached his hand into the suitcase, it was entirely reasonable to assume that she would have completed her search and discovered the cocaine.
  <em>
   <span class="citation" data-id="9063025"><a href="/opinion/9069308/easley-v-petsock/" aria-description="Citation for case: Easley v. Petsock">Id.</a></span>
  </em>
  The district court suppressed the cocaine, but the Eleventh Circuit reversed on the basis of the inevitable discovery exception. The court reasoned that, had Singleton not intervened in the search, Fleck inevitably would have discovered the cocaine.
  <span class="citation" data-id="9063025"><a href="/opinion/9069308/easley-v-petsock/#783" aria-description="Citation for case: Easley v. Petsock"><em>
   Id.
  </em>
  at 783</a></span>.
 </p>
<p id="b605-6">
  This case is factually analogous to
  <em>
   Heman-dez-Cano.
  </em>
  Here, Hawkins-Garner undertook a private search of the two suitcases for purposes entirely independent of the airport police. As in
  <em>
   Hemandez-Cano,
  </em>
  the private search was interrupted by police involvement. If the police had not become involved, Hawkins-Garner would have completed the private search which would have revealed the cocaine. Therefore, as in
  <em>
   Hemandez-Cano,
  </em>
  application of the inevitable discovery exception is appropriate.
 </p>
<p id="b605-9">
  Defendant argues that the police would not have relinquished control of the suitcase to Northwest, and, thus, Hawkins-Garner would not have had the opportunity to open the suitcase. Assuming
  <em>
   arguendo
  </em>
  that defendant is correct and the airport police and/or DEA had kept the suitcase, the result would have been the same. The law enforcement officers would have applied for a search warrant. If a warrant had issued, the officers would have conducted a search pursuant to that warrant; if a warrant had not issued, Northwest would have conducted a private search after the suitcase had been returned. In either case, a search inevitably would have been conducted, and the cocaine would have been discovered.
 </p>
<p id="b605-10">
  For the foregoing reasons, we agree that the inevitable discovery exception to the exclusionary rule was properly applied by the district court in denying defendant’s motion to suppress. The judgment of the district court is AFFIRMED.
 </p>


<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b602-7">
   . The government has conceded that the search which actually occurred was not a private search pursuant to this court's holding in
   <em>
    United States v. Grant,
   </em>
   <span class="citation" data-id="9481099"><a href="/opinion/552385/united-states-v-harold-evan-grant/#388" aria-description="Citation for case: United States v. Harold Evan Grant">920 F.2d 376, 388</a></span> (6th Cir.1990). Ap-pellee's Brief at 11, n. 3.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b603-8">
   . In
   <em>
    <span class="citation" data-id="542344"><a href="/opinion/542344/united-states-v-david-buchanan/" aria-description="Citation for case: United States v. David Buchanan">Buchanan</a></span>,
   </em>
   this court relied in part on the reasoning in
   <em>
    United States v. Griffin,
   </em>
   <span class="citation" data-id="321384"><a href="/opinion/321384/united-states-v-thomas-griffin-and-catherine-tucker/#961" aria-description="Citation for case: United States v. Thomas Griffin and Catherine Tucker">502 F.2d 959, 961</a></span> (6th Cir.) (per curiam),
   <em>
    cert. denied,
   </em>
   <span class="citation multiple-matches"><a href="/c/U.S./419/1050/">419 U.S. 1050</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./95/626/">95 S.Ct. 626</a></span>, <span class="citation no-link">42 L.Ed.2d 645</span> (1974), which held that "police who believe they have probable cause to search cannot enter a home without a warrant merely because they plan subsequently to get one.”
   <em>
    Griffin,
   </em>
   <span class="citation" data-id="321384"><a href="/opinion/321384/united-states-v-thomas-griffin-and-catherine-tucker/#961" aria-description="Citation for case: United States v. Thomas Griffin and Catherine Tucker">502 F.2d at 961</a></span>. In
   <em>
    <span class="citation" data-id="321384"><a href="/opinion/321384/united-states-v-thomas-griffin-and-catherine-tucker/" aria-description="Citation for case: United States v. Thomas Griffin and Catherine Tucker">Griffin</a></span>
   </em>
   the inevitable discovery exception was not applied because the police intentionally took a shortcut in an attempt to bypass the Fourth Amendment warrant requirement — in effect, the police conducted an illegal search to determine whether it would be worthwhile to obtain a search warrant.
   <em>
    <span class="citation" data-id="321384"><a href="/opinion/321384/united-states-v-thomas-griffin-and-catherine-tucker/" aria-description="Citation for case: United States v. Thomas Griffin and Catherine Tucker">Id.</a></span>
   </em>
</p>
<p id="b603-9">
   Under
   <em>
    Murray v. United States,
   </em>
   <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/" aria-description="Citation for case: Murray v. United States">487 U.S. 533</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/" aria-description="Citation for case: Murray v. United States">108 S.Ct. 2529</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/" aria-description="Citation for case: Murray v. United States">101 L.Ed.2d 472</a></span> (1988), the holding in
   <em>
    <span class="citation" data-id="321384"><a href="/opinion/321384/united-states-v-thomas-griffin-and-catherine-tucker/" aria-description="Citation for case: United States v. Thomas Griffin and Catherine Tucker">Griffin</a></span>
   </em>
   must be narrowly applied.
   <em>
    Murray
   </em>
   held that the Fourth Amendment does not require suppression of evidence initially discovered during a police officer's illegal search if that evidence is also discovered during a later search pursuant to a valid warrant that was obtained independently of the illegal search. Therefore, although we adhere to the position that intentional shortcuts to the warrant requirement cannot be tolerated, we limit its application under
   <em>
    Murray
   </em>
   to facts similar to those in
   <em>
    Griffin. See United States v. Straughter,
   </em>
   <span class="citation" data-id="573108"><a href="/opinion/573108/united-states-v-charles-h-straughter-genell-brown-ladonna-thornton/#1231" aria-description="Citation for case: United States v. Charles H. Straughter, Genell Brown,...">950 F.2d 1223, 1231</a></span> (6th Cir.1991) (recognizing that “the Fourth Amendment does not require the suppression of evidence initially discovered during an illegal entry if that evidence is seized during a later search pursuant to a warrant that is not based on evidence obtained during the illegal entry”),
   <em>
    cert. denied,
   </em>
   <span class="citation multiple-matches"><a href="/c/U.S./503/976/">503 U.S. 976</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./112/1601/">112 S.Ct. 1601</a></span>, <span class="citation no-link">118 L.Ed.2d 315</span> (1992).
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/united-states-v-knapp--4596482.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c27d9aeaa2523cc4", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "united-states-v-knapp--4596482"}, "payload": {"all": [{"cite": "917 F.3d 1161", "page": "1161", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "917"}], "display": "917 F.3d 1161", "official": {"cite": "917 F.3d 1161", "page": "1161", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "917"}, "official_selection_present": true, "record_id": "united-states-v-knapp--4596482"}}
{"assertion_id": "d7d72a8b257b5687", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-knapp--4596482"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-knapp--4596482", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-knapp--4596482

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-knapp--4596482",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "United States v. Knapp",
    "case_name_short": "Knapp",
    "case_name_full": "UNITED STATES of America, Plaintiff - Appellee, v. Stacy Jo KNAPP, A/K/A Stacy Jo Rafay, A/K/A Stacey Jo Knapp, Defendant - Appellant.",
    "input_case_name": "United States v. Knapp",
    "court": "U.S. Court of Appeals, 10th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": null,
    "year": 2019,
    "docket": null,
    "cluster_id": 4596482,
    "lead_opinion_id": 4373735,
    "sibling_ids": [],
    "absolute_url": "/opinion/4596482/united-states-v-knapp/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "917 F.3d 1161",
      "volume": "917",
      "reporter": "F.3d",
      "page": "1161",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "917 F.3d 1161",
        "volume": "917",
        "reporter": "F.3d",
        "page": "1161",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "917 F.3d 1161",
    "official_selection": {
      "court_class": "coa",
      "selected": "917 F.3d 1161",
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
    "date_created": "2026-07-06T13:13:53Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:14:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:14:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:14:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:14:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — united-states-v-knapp--4596482

```
                                                                                  FILED
                                                                      United States Court of Appeals
                                       PUBLISH                                Tenth Circuit

                      UNITED STATES COURT OF APPEALS                          March 5, 2019

                                                                            Elisabeth A. Shumaker
                            FOR THE TENTH CIRCUIT                               Clerk of Court
                        _________________________________

 UNITED STATES OF AMERICA,

       Plaintiff - Appellee,

 v.                                                           No. 18-8031

 STACY JO KNAPP, a/k/a Stacy Jo Rafay,
 a/k/a Stacey Jo Knapp,

       Defendant - Appellant.
                      _________________________________

                     Appeal from the United States District Court
                             for the District of Wyoming
                         (D.C. No. 2:17-CR-00207-SWS-1)
                       _________________________________

Josh Lee, Assistant Federal Public Defender (Virginia L. Grady, Federal Public
Defender, with him on the briefs), Denver, Colorado, for Appellant.

Nicole M. Romine, Assistant United States Attorney (Mark A. Klaassen, United States
Attorney, with her on the brief), Cheyenne, Wyoming, for Appellee.
                        _________________________________

Before HOLMES, McKAY, and KELLY, Circuit Judges.
                  _________________________________

KELLY, Circuit Judge.
                        _________________________________

      Defendant-Appellant Stacy Knapp entered a conditional plea of guilty to being a

felon in possession of a firearm, 18 U.S.C. §§ 922(g)(1) & 924(a)(2), and she was

sentenced to 36 months’ imprisonment and three years’ supervised release. The
conditional plea allowed her to appeal the district court’s denial of her motion to

suppress, and in the event it is successful, to withdraw her guilty plea. Fed. R. Crim. P.

11(a)(2). Exercising jurisdiction under 28 U.S.C. § 1291, we reverse and remand.



                                        Background

       The parties do not dispute the material facts found by the district court. Ms.

Knapp called the police to report a theft at a grocery store in Gillette, Wyoming. 3 R.

18–19. Officers responded to the call, apprehended the theft suspect, and took a

statement from Ms. Knapp in the grocery store. Id. at 19. During their investigation

officers gave police dispatch Ms. Knapp’s name. Id. Dispatchers discovered that Ms.

Knapp had an outstanding warrant for her arrest and informed Officer Zachary Parker.

Id. at 19–20. By then Ms. Knapp had already left the grocery store, so Officer Parker

went to the grocery store parking lot to find Ms. Knapp. Id. at 20.

       Officer Parker found Ms. Knapp in the driver’s seat of a parked pickup truck

outside the store. Id. He instructed her that she could not leave because he had to arrest

her. Id. at 21. Ms. Knapp exited the truck and followed Officer Parker back into the

grocery store. Id. Ms. Knapp voluntarily retrieved her purse from the seat of the truck

when she followed Officer Parker back to the grocery store. Id. at 21–22. Because the

officers were still concluding their theft investigation, Officer Parker asked Ms. Knapp to

sit on a chair outside a bank office located within the store. Id. at 23.

       Once Ms. Knapp sat down, Officer Parker moved her purse, which was closed by

a zipper, a few chairs away from her. Id. at 24. Ms. Knapp then asked her friend who

                                              2
was also present to take her purse, so she would not have to take it to jail. Id. at 25. This

raised the officers’ suspicions. Id. at 70–71. When her friend — who was originally

willing to take her purse — declined, after being warned by Officer Jacob Foutch that

taking it could be illegal, she tried to have her boyfriend take it or leave it in the truck she

had been driving. Id. at 25–26, 41, 67–68. However, Officer Parker refused to let her

leave her purse in the truck. Id. at 26, 70–71. Officer Parker then asked for her consent

to search the purse but she refused. Id. at 41–42. The officers then placed Ms. Knapp in

handcuffs behind her back, and Officer Foutch led her outside while Officer Parker

carried the purse. Id. at 42–43; 1 Supp. R., Ex. C (Subpoena 17-06882 File 4, Body Cam

Video of Officer Jake Foutch), at 29:30–30:00.

         The officers and Ms. Knapp walked to Officer Parker’s patrol vehicle, and Ms.

Knapp stood in front of the hood facing Officer Foutch. 3 R. 43. Officer Parker placed

the purse on the hood of his patrol car. Id. at 28. At that time, Ms. Knapp stood near the

bumper of the patrol car, the purse was on the hood near the windshield (about three to

four feet from Ms. Knapp), and Ms. Knapp stood handcuffed facing away from the car

and toward Officer Foutch. Id. at 28, 43, 56–57. Ms. Knapp’s friend was on the opposite

side of the patrol vehicle. Id. at 28. Next, after Officer Foutch threatened that she would

be guilty of a felony for bringing drugs to a detention center, Ms. Knapp told him she was

carrying a pistol in her purse. 1 R. 50, 55. At that point the officers searched the purse

and found her pistol. When they searched the purse, three officers were present. See 3

R. 29.



                                               3
       Ms. Knapp was charged with one count of unlawfully possessing a firearm after a

felony conviction in violation of 18 U.S.C. §§ 922(g)(1) and 924(a)(2). 1 R. 10. She

moved to suppress the firearm on Fourth Amendment grounds, arguing that the search

was unreasonable and that her statement acknowledging the presence of the firearm was

inadmissible derivative evidence. Id. at 12–17. The government argued that the search

was proper under the search incident to arrest and inevitable discovery exceptions. Id. at

18–24; 3 R. 87–89. Without reaching the inevitable discovery issue, the district court

concluded that the search incident to arrest exception applied and consequently denied

the motion to suppress. 1 R. 163.

       The district court, noting that the case presented a “difficult choice,” 3 R. 107,

held that the search satisfied both the spatial and temporal proximity requirements

essential for a search incident to arrest. 1 R. 160, 162. The district court reasoned that

Ms. Knapp’s purse was approximately three feet away from her when it was searched,

and thus she could have gained access. Id. at 160. It reasoned that any delay between the

arrest and the search (some 12 to 13 minutes) was necessitated by the officers conducting

a theft investigation and allowing Ms. Knapp to make arrangements for her truck; there

were no other intervening events separating the arrest from the search. Id. at 162.

       On appeal, Ms. Knapp argues that (1) the search of her purse was not truly

incident to her arrest given intervening events, and (2) the search incident to arrest

exception does not apply because (a) the police chose to put Ms. Knapp in proximity with

her purse, and (b) Ms. Knapp could not have accessed the purse’s contents at the time of

the search. The government responds that given a lawful arrest, Ms. Knapp’s first

                                              4
argument is in essence an attack on the district court’s contrary factual finding. The

government further responds that law enforcement did not artificially create the

circumstances justifying a search of the purse incident to arrest, and law enforcement

properly searched the purse incident to an arrest because the purse was on her person at

the time of the arrest.1



                                         Discussion

       This court reviews de novo whether a search or seizure was reasonable under the

Fourth Amendment. United States v. Sanders, 796 F.3d 1241, 1243–44 (10th Cir. 2015).

It reviews the district court’s factual findings for clear error, and when reviewing the

denial of a motion to suppress, it views the evidence in the light most favorable to the

government. United States v. Serrato, 742 F.3d 461, 470 (10th Cir. 2014).

       The Fourth Amendment provides that “[t]he right of the people to be secure in

their persons, houses, papers, and effects, against unreasonable searches and seizures,

shall not be violated.” In general, warrantless searches are per se unreasonable. Katz v.

United States, 389 U.S. 347, 357 (1967). The warrantless search rule, however, is subject

to several exceptions. One exception allows arresting officers to “search the person of

the accused when legally arrested.” Weeks v. United States, 232 U.S. 383, 392 (1914).




1
  Although the government briefed the inevitable discovery issue, see Aplee. Br. at 22–
24, it has since conceded that this issue is not ripe for consideration on appeal because it
involves disputed factual questions that must be resolved by the district court in the first
instance. Oral Arg. at 25:15–50. We accordingly do not consider this issue on appeal,
although we note that this argument may be raised again on remand.
                                              5
Case law has developed to allow not only the search of the arrestee’s person, but also the

area within the arrestee’s “immediate control.” Chimel v. California, 395 U.S. 752, 763

(1969). This authority is justified by the need to disarm the suspect and preserve

evidence. United States v. Robinson, 414 U.S. 218, 234 (1973).

       Whether a search is “of the person” or of the area within the arrestee’s “immediate

control” — that is, “the area from within which he might gain possession of a weapon or

destructible evidence” — is a critical distinction.2 Chimel, 395 U.S. at 763. In United

States v. Robinson, the Court held that a search of an arrestee’s person incident to arrest

need not be justified on a case-by-case basis. Robinson, 414 U.S. at 235. Although the

Court did not address whether areas within the arrestee’s immediate control are also

categorically subject to warrantless searches incident to arrest, it noted that searches of

the arrestee’s person and searches of the area within the arrestee’s immediate control are

“two distinct propositions” that “have been treated quite differently.” Id. at 224. The

Court later reinforced this distinction, albeit in dicta, by noting that arrests create a

reduced expectation of privacy in an arrestee’s person, but not in possessions within her

immediate control. United States v. Chadwick, 433 U.S. 1, 16 n.10 (1977), abrogated on

other grounds by California v. Acevedo, 500 U.S. 565 (1991); see also United States v.

Riley, — U.S. —, 134 S. Ct. 2473, 2483 (2014) (justifying the rule in Robinson by

balancing the arrestee’s expectation of privacy in her person with the need to prevent


2
  Other circuits have aptly referred to this area of immediate control as the arrestee’s
“grab area.” See, e.g., United States v. Gandia, 424 F.3d 255, 261 (2d Cir. 2005); United
States v. Ortiz, 146 F.3d 25, 28 (1st Cir. 1998); United States v. Hudson, 100 F.3d 1409,
1420 (9th Cir. 1996).
                                               6
harm to the officers and destruction of evidence). It thus stands to reason that searches of

areas within an arrestee’s immediate control must be justified on a case-by-case basis by

the need to disarm or to preserve evidence. See United States v. Morgan, 636 F.2d 1561,

1578 n.2, 1579 (10th Cir. 1991) (Seymour, J., dissenting); cf. United States v. Pacheco,

884 F.3d 1031, 1043 n.9 (10th Cir. 2018) (noting that Robinson authorizes only a

“limited search of items found during [a] pat-down” incident to a lawful arrest).

       Because the validity of Ms. Knapp’s arrest is not at issue, this appeal turns on (1)

whether the search of her purse was one of her person for the purposes of Robinson, and

(2) if the search was not of her person, whether the search was nevertheless justified

because it was within “the area from within which [she] might [have] gain[ed] possession

of a weapon or destructible evidence.” Chimel, 395 U.S. at 763.

A.     The Search of Ms. Knapp’s Purse Was Not One “Of Her Person”

       Ms. Knapp presents two arguments why the search of her purse was not one “of

her person” at the time of her arrest. See Aplt. Br. at 11–18. First, she argues that the

government is wrong on the facts because she was not carrying her purse when she was

told she was under arrest; rather, it was sitting somewhere within the truck, and she had

to “collect” it from the truck to bring it into the store. Aplt. Reply Br. at 11. The district

court did not make a specific factual finding comparing the exact time of the arrest with

when Ms. Knapp grabbed her purse. It simply noted, “[Ms. Knapp] brought her purse

with her into the grocery store.” 1 R. 155.

       Even if Ms. Knapp was carrying her purse at the time of her arrest, she argues that

the arresting officers’ search was not one “of her person.” Aplt. Reply Br. at 12–18.

                                               7
Whether the search of a purse (or similar item) carried by an arrestee but not within her

clothing is one “of the person” is a question of first impression in this circuit. Indeed, the

Supreme Court has not clearly demarcated where the person ends and the “grab area”

begins. However, we must resolve the question now before us, and we hold that the

better view is that a carried purse does not qualify as “of the person.” We reach this

conclusion for several reasons.

       First, the animating reasons supporting arresting officers’ “unqualified authority”

to search an arrestee’s person are less salient in the context of visible, handheld

containers such as purses. Robinson, 414 U.S. at 225. Robinson was based in part on the

notion that a lawful arrest empowers an officer to disarm, and if “he ma[y] disarm, he

may search, lest a weapon be concealed.” Id. at 232 (quoting People v. Chiagles, 142

N.E. 583, 584 (1923) (Cardozo, J.)). Although Justice Marshall disagreed in his dissent

in Robinson with the Court’s grant of unqualified authority to search an arrestee’s person,

he acknowledged that more thorough searches of arrestees may be necessitated by the

risk that an arrestee in “prolonged proximity” to officers could harm them with a

concealed weapon. Robinson, 414 U.S. at 253–54 (Marshall, J., dissenting). Because of

an arrestee’s ability to always access weapons concealed in her clothing or pockets, an

officer must necessarily search those areas because it would be impractical (not to

mention demeaning) to separate the arrestee from her clothing.3 See United States v.


3
  It is for this reason that we decline to follow those courts construing the arrestee’s
“person” to include any containers in the arrestee’s “actual” or “physical” possession at
the time of arrest. See, e.g., People v. Cregan, 10 N.E.3d 1196, 1207 (Ill. 2014) (a

                                              8
Edwards, 415 U.S. 800, 803 (1974) (holding that a delay in searching an arrestee’s

clothing for evidence at the stationhouse was reasonable because officers could not have

deprived him of his clothing until substitute clothing was available). In addition, the

holding in Robinson relied on an arrestee’s diminished privacy interest in her person by

way of her arrest such that a pat-down and inspection of containers found within her

clothing “constitute[] only minor additional intrusions.” Riley, 134 S. Ct. at 2484.

Containers held in an arrestee’s hand and not concealed on her body or within her

clothing do not implicate such concerns to the same degree.

       Second, given that handheld containers such as purses are easily dispossessed,

classifying such containers as potentially part of an arrestee’s person would necessitate

unworkable determinations about what the arrestee was holding at the exact time of her

arrest. Although under Robinson the bounds of an arrestee’s person are determined

“[w]hen an arrest is made,” Robinson, 414 U.S. at 226 (quoting Chimel, 395 U.S. at 762–

63)), searches of an arrestee’s person should not depend on an exact time of arrest. Such

a rule would be unworkable in cases like this; it would require arresting officers to

determine or remember exactly when a person obtained or shed the object at issue and

compare that to the exact moment when the officer placed her under arrest. And, because

an arrestee can dispossess a handheld container simply by releasing it from her hand,

more confusion than clarity would result from such a requirement. The Fourth


wheeled bag was on an arrestee’s person because he was gripping its handle at the time of
arrest); State v. Byrd, 310 P.3d 793, 794, 798 (Wash. 2013) (a search of a purse on an
arrestee’s lap constituted a search of her person).

                                             9
Amendment is meant to guide law enforcement conduct and thus needs to be readily

determinable by officers in the field. See Davis v. United States, 564 U.S. 229, 233

(2011). A rule requiring precise timing would frustrate that goal.

       Third, a holding to the contrary would erode the distinction between the arrestee’s

person and the area within her immediate control. The government urges the definition

of an arrestee’s person includes a “container that has a close association with the person,”

Aplee. Br. at 17, a definition likely originating from the Court’s description of the

Robinson exception applying to “personal property . . . immediately associated with the

person of the arrestee.” Riley, 134 S. Ct. at 2484 (emphasis added) (quoting Chadwick,

433 U.S. at 15). To the extent the government suggests a construction that includes more

than the arrestee’s immediate person, worn clothing, or containers concealed within her

clothing, we decline to adopt it. Certainly, officers would have clear guidance from a

rule allowing them to search any container that an arrestee was or may have been

touching around the time of arrest. But such a rule risks expanding Robinson’s limited

exception to grant unqualified authority to search an arrestee’s grab area. The better

formulation, we believe, would be to limit Robinson to searches of an arrestee’s clothing,

including containers concealed under or within her clothing. Accordingly, visible

containers in an arrestee’s hand such as Ms. Knapp’s purse are best considered to be

within the area of an arrestee’s immediate control — thus governed by Chimel — the

search of which must be justified in each case. Accord United States v. Monclavo-Cruz,

662 F.2d 1285, 1287–88 (9th Cir. 1981); State v. Carrawell, 481 S.W.3d 833, 840–41

(Mo. 2016) (en banc).

                                             10
       We also decline to construe the phrase “immediately associated with the person”

as calling for an examination of the container’s function vis-à-vis the arrestee. Reading

Chimel, Robinson, and their progeny together, searches incident to arrest are governed by

a container’s location relative to the arrestee and the degree to which it can be accessed

by or separated from the arrestee, rather than the manner in which it is typically used.

Compare Edwards, 415 U.S. at 804–805 (the impracticality and indignity of removing an

arrestee’s clothing to preserve evidence supports characterizing worn clothing as “of the

person” under Robinson), with New York v. Belton, 453 U.S. 454, 460 n.4 (1981)

(providing as examples of containers possibly within an arrestee’s reach luggage, boxes,

bags, and even clothing). The comparison of purses to items of similar use, such as

wallets, is therefore misleading.4 See Aplee. Br. at 14 (citing United States v. Van Dam,

37 F. App’x 461, 463–64 (10th Cir. 2011)). Because Ms. Knapp’s purse, which was not

concealed under or within her clothing, was easily capable of separation from her person,

we hold that the arresting officers had no authority to search its contents pursuant to

Robinson.




4
  Although the Court in Riley held that cellular phones “implicate privacy concerns far
beyond those implicated by the search of a cigarette pack, a wallet, or a purse,” and it
noted that lower courts have approved searches of purses incident to arrest, it did not
endorse the searches of purses under Robinson, nor did it equate a purse to a wallet.
Riley, 134 S. Ct. at 2488–89. Instead, the comparison supported its narrower holding that
cellular phones must be exempt from Robinson searches because of the sheer quantity of
personal information they contain. Id.
                                             11
B.     The Search of Ms. Knapp’s Purse Was Not Justified Under the
       Circumstances

       We next turn to whether the search of Ms. Knapp’s purse was nevertheless

justified by either the need to preserve evidence or the need to disarm Ms. Knapp. This

question depends on whether the purse was within the area the arresting officers could

“reasonably have believed . . . [the arrestee] could have accessed . . . at the time of the

search.” Arizona v. Gant, 556 U.S. 332, 344 (2009) (emphasis added).

       At the outset, we note that although Gant specifically addressed the search of an

automobile, its principles apply more broadly. The Court held such searches are justified

either by the “twin rationales of Chimel” or by an arresting officer’s reasonable belief

that the vehicle contains evidence of the crime precipitating the arrest. 556 U.S. at 342–

43 (quoting Thornton v. United States, 541 U.S. 615, 624 (2004) (O’Connor, J.,

concurring in part)). As the Third Circuit observed, Gant meant to keep searches incident

to arrest tethered to the Chimel justifications, and Chimel did not involve a vehicle

search. United States v. Shakir, 616 F.3d 315, 318 (3d Cir. 2010) (involving a gym bag);

see also United States v. Cook, 808 F.3d 1195, 1199–1200 (9th Cir. 2015) (applying Gant

to the search of a backpack). The Court also held that the second justification — the need

to search a vehicle for evidence — but not the first, is “unique to the vehicle context.” Id.

at 343. We therefore join the Third Circuit in interpreting Gant as focusing attention on

the arrestee’s ability to access weapons or destroy evidence at the time of the search,

rather than the time of the arrest, regardless of whether the search involved a vehicle. Id.




                                              12
       Applying Gant and Chimel, it was unreasonable to believe Ms. Knapp could have

gained possession of a weapon or destructible evidence within her purse at the time of the

search.5 We look to the following factors to determine whether an area searched is within

an arrestee’s grab area under Chimel: (1) whether the arrestee is handcuffed; (2) the

relative number of arrestees and officers present; (3) the relative positions of the

arrestees, officers, and the place to be searched; and (4) the ease or difficulty with which

the arrestee could gain access to the searched area. United States v. Parra, 2 F.3d 1058,

1066 (10th Cir. 1993). Certainly, officers’ “exclusive control” of an arrestee’s article is

not dispositive of the permissibility of the search. See Belton, 453 U.S. at 461 n.5.

However, the degree to which arresting officers have separated an article from an arrestee

at the time of the search is an important consideration. See Gant, 556 U.S. at 343

(searches of an arrestee’s vehicle are permissible “only when the arrestee is unsecured

and within reaching distance of the passenger compartment at the time of the search”).

Here, not only were Ms. Knapp’s hands cuffed behind her back, Officer Foutch was next

to her, and two other officers were nearby. Moreover, the purse was closed and three to

four feet behind her, and officers had maintained exclusive possession of it since placing

her in handcuffs. We have similarly rejected a search where the defendant was

handcuffed behind his back and could therefore not reach the inside of his bureau



5
  Because we hold that it was unreasonable to believe Ms. Knapp could have accessed
her purse and used the firearm contained within at the time of the search, we need not
reach Ms. Knapp’s other arguments that the search was separated from the arrest by
intervening events, and that the officers chose to place the purse within reaching distance.

                                             13
drawers, night stand, or under his bed. See United States v. Baca, 417 F.2d 103, 105

(10th Cir. 1969); see also United States v. Leo, 792 F.3d 742, 750 (7th Cir. 2015)

(holding that a backpack was not in the defendant’s immediate control after an

investigatory stop where his “hands were cuffed behind his back,” and the backpack was

“no longer in [the defendant’s] possession,” reasoning that it was “inconceivable that” the

defendant “would have been able to lunge for the bag, unzip it, and grab the gun inside”).

Accordingly, although the district court noted that the purse was approximately three feet

away from her at the time of the search, and that she was not otherwise restrained by the

police officers, 1 R. 160, its finding that she could nevertheless have opened the purse

and retrieved the firearm from within was in error.

       The government relies on two Tenth Circuit cases from before Gant to support its

position. See Aplee. Br. at 21. The first, United States v. Parra, involved arresting

officers’ search under two pillows. At the time officers searched under the first pillow

the two arrestees were being handcuffed, but when police searched under the second, the

arrestees were handcuffed behind their backs and seated. 2 F.3d at 1066. The search

under the first pillow — before the arrestees were handcuffed — was permissible because

“there remained a strong possibility that [one of the arrestees] could break free and

retrieve whatever was hidden under the pillow.” Id. Even though both arrestees were

handcuffed, the search of the second pillow was reasonable because the arrestees could

have lunged for a weapon and easily brushed aside the pillow when no officers stood

between them and the pillow. Id. And, most importantly, police had found a handgun

under the first pillow. Id. Aside from the fact that the arrestees were handcuffed behind

                                            14
their backs in Parra, it is readily distinguishable from this case because the factors Parra

listed apply differently here. First, there was only one arrestee here and three police

officers, whereas Parra involved two arrestees. Second, Ms. Knapp’s purse was closed,

whereas the pillow in Parra could easily have been brushed aside. Finally, Ms. Knapp

tried repeatedly to leave her purse behind for the whole encounter (suggesting she was

not trying to effect an escape using a weapon held within it), while a defendant in Parra

glanced at the pillow when asked to raise his hands. Id.

       The second case, United States v. Dennison, 410 F.3d 1203, 1214 (10th Cir.

2005), also provides the government little support. In Dennison, this court upheld a

search incident to arrest when the arrestee was handcuffed and placed in a different area

than the one searched. This court rested this holding in part on the fact that a detainee

may still gain access to a weapon even when he is under police officers’ control. Id. at

1213. However, Dennison was decided before Gant, and thus did not apply the time-of-

search rule. Dennison is also inapposite because the officers had a reasonable suspicion

that the defendant was dangerous and able to gain access to weapons in the vehicle when

his fellow arrestee was arrested on an outstanding weapons charge. Id. at 1212–14.

Here, the government has never suggested that the officers had a reasonable suspicion

that Ms. Knapp was dangerous and able to access weapons.

       Because the search of Ms. Knapp’s purse was not one of her person for the

purposes of Robinson, and because the search of her purse was not actually supported by

the Chimel justifications, the exception for a search incident to arrest does not apply here.

       REVERSED and REMANDED.

                                             15

```

---

## GROUP: _overhaul2/lake/cases/united-states-v-landeros--4580892.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bd0f9326adfe60ff", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "united-states-v-landeros--4580892"}, "payload": {"all": [{"cite": "913 F.3d 862", "page": "862", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "913"}], "display": "913 F.3d 862", "official": {"cite": "913 F.3d 862", "page": "862", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "913"}, "official_selection_present": true, "record_id": "united-states-v-landeros--4580892"}}
{"assertion_id": "440c3478f6acbe7b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-landeros--4580892"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-landeros--4580892", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-landeros--4580892

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-landeros--4580892",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "United States v. Alfredo Landeros",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Landeros",
    "court": "U.S. Court of Appeals, 9th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": null,
    "year": 2019,
    "docket": "No. 17-10217",
    "cluster_id": 4580892,
    "lead_opinion_id": 4358145,
    "sibling_ids": [],
    "absolute_url": "/opinion/4580892/united-states-v-alfredo-landeros/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "913 F.3d 862",
      "volume": "913",
      "reporter": "F.3d",
      "page": "862",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "913 F.3d 862",
        "volume": "913",
        "reporter": "F.3d",
        "page": "862",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "913 F.3d 862",
    "official_selection": {
      "court_class": "coa",
      "selected": "913 F.3d 862",
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
    "date_created": "2026-07-06T13:13:28Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:13:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:13:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:13:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:13:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — united-states-v-landeros--4580892

```
                 FOR PUBLICATION

   UNITED STATES COURT OF APPEALS
        FOR THE NINTH CIRCUIT


UNITED STATES OF AMERICA,                 No. 17-10217
                  Plaintiff-Appellee,
                                             D.C. No.
                 v.                       4:16-cr-00855-
                                           RCC-BGM-1
ALFREDO ENOS LANDEROS,
              Defendant-Appellant.          OPINION



       Appeal from the United States District Court
                for the District of Arizona
        Raner C. Collins, District Judge, Presiding

       Argued and Submitted September 12, 2018
               San Francisco, California

                 Filed January 11, 2019

  Before: Marsha S. Berzon, Johnnie B. Rawlinson, and
           Paul J. Watford, Circuit Judges.

                Opinion by Judge Berzon
2                UNITED STATES V. LANDEROS

                          SUMMARY *


                          Criminal Law

    Reversing the district court’s denial of a motion to
suppress evidence obtained as a result of a traffic stop, the
panel held that law enforcement officers may not extend a
lawfully initiated vehicle stop because a passenger refuses to
identify himself, absent reasonable suspicion that the
individual has committed a criminal offense.

    The panel recognized that Rodriguez v. United States,
135 S. Ct. 1609 (2015) (holding that an officer may conduct
certain unrelated checks during an otherwise lawful traffic
stop but may not do so in a way that prolongs the stop, absent
the reasonable suspicion ordinarily demanded to justify
detaining an individual), at least partially abrogated United
States v. Turvin, 517 F.3d 1097 (9th Cir. 2008) (holding that
an officer did not transform a lawful traffic stop into an
unlawful one when, without reasonable suspicion, he took a
break from writing a traffic citation to ask the driver about a
methamphetamine laboratory and obtain the driver’s consent
to search the his truck). The panel held that because the
district court’s approval of the duration of the stop in this
case was based on Turvin and disregarded Rodriguez, it was
premised on legal error.

    Observing that the record does not demonstrate that the
officer had a reasonable suspicion that the defendant was out
past his curfew or drinking underage, the panel held that any

    *
      This summary constitutes no part of the opinion of the court. It
has been prepared by court staff for the convenience of the reader.
                UNITED STATES V. LANDEROS                      3

extension of the traffic stop to investigate those matters was
an unlawful seizure.

    Based on the plain text of Ariz. Rev. Stat. Ann. § 13-
2412(A), the panel rejected the government’s contention that
the defendant’s refusal to identify himself provided
reasonable suspicion of the additional offenses of failure to
provide identification and failure to comply with law
enforcement orders.

    Because the police could not lawfully order the
defendant to identify himself, the panel explained that the
defendant’s repeated refusal to do so did not constitute a
failure to comply with an officer’s lawful order under Ariz.
Rev. Stat. Ann. § 28-622(A). The panel concluded that there
was therefore no justification for the extension of the
detention to allow the officers to press the defendant further
for his identity.

    The panel held that the bullets the defendant was
convicted of possessing, only because he was ordered from
the car as part of the unlawfully extended seizure and
subsequently consented to a search of his pockets, cannot be
introduced at trial. The panel wrote that because the stop
was no longer lawful by the time the officers ordered the
defendant to leave the car, the validity or not of the exit order
does not matter.

    The panel addressed in a concurrently filed
memorandum disposition the defendant’s challenge to the
district court’s denial of his motion to dismiss the
indictment.
4                 UNITED STATES V. LANDEROS

                             COUNSEL

Lee Tucker (argued), Assistant Federal Defender; Jon M.
Sands, Federal Defender; Federal Public Defender’s Office,
Tucson, Arizona; for Defendant-Appellant.

Charisse Arce (argued) and Angela W. Woolridge, Assistant
United States Attorneys; Elizabeth A. Strange, First
Assistant United States Attorney; Robert L. Miskell,
Appellate Chief; United States Attorney’s Office, Tucson,
Arizona; for Plaintiff-Appellee.


                              OPINION

BERZON, Circuit Judge:

    Our question is whether law enforcement officers may
extend a lawfully initiated vehicle stop because a passenger
refuses to identify himself, absent reasonable suspicion that
the individual has committed a criminal offense. We
conclude that they may not do so. As a result, we reverse. 1

                                    I.

    Early in the morning of February 9, 2016, police officer
Clinton Baker pulled over a car driving 11 miles over the
speed limit. The stop occurred on a road near the Pascua
Yaqui Indian reservation. Alfredo Landeros sat in the front
passenger seat next to the driver. Two young women were in


    1
      Appellant also challenges the district court’s denial of his motion
to dismiss the indictment based on alleged police abuses after his arrest.
We address that challenge in a concurrently filed memorandum
disposition.
                 UNITED STATES V. LANDEROS                        5

the back seat. The driver apologized to Officer Baker for
speeding and provided identification.

    Officer Baker wrote in his incident report and testified
that he smelled alcohol in the car. The two women in the
backseat appeared to him to be minors, and therefore subject
to both the underage drinking laws and the 10:00 p.m.
Pascua Yaqui curfew. 2 According to the two women’s
testimony, Officer Baker requested their identification and
explained that he was asking because they looked younger
than 18 years old “and it was past a curfew.” The two
women—who were 21 and 19 years old—complied.

    As he stated at the suppression hearing, Officer Baker
did not believe that Landeros was underage, and he was not.
Nonetheless, Officer Baker, in his own words,
“commanded” Landeros to provide identification. Later,
Officer Baker explained it was “standard for [law
enforcement] to identify everybody in the vehicle.”
Landeros refused to identify himself, and informed Officer
Baker—correctly, as we shall explain—that he was not
required to do so. Officer Baker then repeated his “demand[]
to see [Landeros’s] ID.” Landeros again refused. As a result,
Officer Baker called for back-up, prolonging the stop.
Officer Frank Romero then arrived, and he too asked for
Landeros’s identification. The two officers also repeatedly
“commanded” Landeros to exit the car because he was not
being “compliant.”

   Landeros eventually did leave the car. At least several
minutes passed between Officer Baker’s initial request for


    2
      Officer Baker is a police officer with the Pascua Yaqui Police
Department who has authority to enforce both the Pascua Yaqui tribal
code and Arizona state laws.
6                 UNITED STATES V. LANDEROS

Landeros’s identification and his exit from the car, although
the record does not reflect the exact length of time.

    Officer Baker testified that, as Landeros exited the car,
he saw for the first time pocketknives, a machete, and two
open beer bottles on the floorboards by the front passenger
seat. Arizona prohibits open containers of alcohol in cars on
public highways, Ariz. Rev. Stat. Ann. § 4-251. Officer
Baker then placed Landeros under arrest. Consistent with
Officer Baker’s testimony, the government represented in its
district court briefing that Landeros was arrested both for
possessing an open container 3 and for “failure to provide his
true full name and refusal to comply with directions of police
officers.” See Ariz. Rev. Stat. Ann. § 13-2412(A) (“It is
unlawful for a person, after being advised that the person’s
refusal to answer is unlawful, to fail or refuse to state the
person’s true full name on request of a peace officer who has
lawfully detained the person based on reasonable suspicion
that the person has committed, is committing or is about to
commit a crime.”); id. § 28-622(A) (“A person shall not
willfully fail or refuse to comply with any lawful order or
direction of a police officer invested by law with authority
to direct, control or regulate traffic.”).

    The officers handcuffed Landeros as soon as he exited
the car. Officer Romero asked Landeros if he had any
weapons; Landeros confirmed that he had a knife in a
pocket. Officer Romero requested consent to search
Landeros’s pockets, and Landeros agreed. During that



    3
       We do not reach the question whether, if the seizure were otherwise
lawful, law enforcement could have lawfully detained and arrested
Landeros based on the open container of alcohol seen where he had been
sitting. He was never charged with that offense.
                UNITED STATES V. LANDEROS                     7

search, Officer Romero found a smoking pipe and six bullets
in Landeros’s pockets.

    Two and a half months later, Landeros was indicted for
possession of ammunition by a convicted felon, 18 U.S.C.
§§ 922(g)(1), 924(a)(2). He moved to suppress the evidence
based on the circumstances of the stop, and also to dismiss
the indictment based on alleged abuse by the police officers
after the search. The magistrate judge recommended the
district court deny both motions, and it did so in a single
sentence order. Landeros then entered into a plea agreement
that preserved his right to appeal the denials of the two
motions. The district court accepted the agreement and
sentenced Landeros to 405 days in prison and three years of
supervised release.

                              II.

    This case implicates two doctrines, one concerning the
circumstances under which law enforcement can prolong a
stop, and the other governing when law enforcement can
require a person to identify himself.

                              A.

    Rodriguez v. United States held that “[a]n officer . . . may
conduct certain unrelated checks during an otherwise lawful
traffic stop. But . . . he may not do so in a way that prolongs
the stop, absent the reasonable suspicion ordinarily
demanded to justify detaining an individual.” 135 S. Ct.
1609, 1615 (2015). In that case, a police officer stopped
Rodriguez for a minor traffic violation. Id. at 1612. The
officer collected Rodriguez’s license, registration, and proof
of insurance, ran a records check on both Rodriguez and a
passenger, and questioned the passenger about “where [they]
were coming from and where they were going.” Id. at 1613.
8              UNITED STATES V. LANDEROS

He then returned to the vehicle “to issue [a] written warning”
to Rodriguez for the traffic violation. Id.

    Although the reasons for the traffic stop were, at this
point, “out of the way,” the officer continued the stop, asking
Rodriguez for permission to walk a dog around the vehicle.
Id. When Rodriguez refused, the officer ordered Rodriguez
out of the car and called for back-up. Id. Several minutes
later, after a deputy sheriff arrived, the officer conducted a
dog sniff test, which resulted in the discovery of
methamphetamines within the car. Id.

    Based on the fruits of that search, Rodriguez was
indicted for possession with intent to distribute. Id. He
moved to suppress the evidence on the ground that there was
no reasonable suspicion of any offense other than the traffic
violation, so the stop was unlawfully prolonged by the dog
sniff. Id. The district court agreed with Rodriguez that the
officer lacked reasonable suspicion to extend the stop after
the written warning, but determined that the extension was
nonetheless permissible because of its brevity. Id. at 1613–
14. The Eighth Circuit affirmed. See United States v.
Rodriguez, 741 F.3d 905, 907–08 (8th Cir. 2014), vacated
and remanded, 135 S. Ct. 1609.

    The Supreme Court vacated the judgment on the basis
that law enforcement may not extend a traffic stop with tasks
unrelated to the traffic mission, absent independent
reasonable suspicion. Rodriguez, 135 S. Ct. at 1616–17. In
reaching this conclusion, the Court made clear that it would
not have mattered if the police officer conducted the dog
sniff test before, rather than after, he issued the warning.
What mattered was the added time, not at what point, in the
chronology of the stop, that time was added. Id.
               UNITED STATES V. LANDEROS                     9

    This court so emphasized in United States v. Evans,
published a month after Rodriguez. 786 F.3d 779, 786 (9th
Cir. 2015). There, we held that law enforcement
impermissibly extended a traffic stop by running an ex-felon
registration check unrelated to traffic safety and unsupported
by separate reasonable suspicion. Id. “That the ex-felon
registration check occurred before . . . the officer issued a
ticket [stemming from the initial traffic violation] is
immaterial,” we explained. Id. (brackets, citation, and
internal quotation marks omitted). “[R]ather, the critical
question is whether the check prolongs—i.e., adds time to—
the stop.” Id. (brackets, citation, and internal quotation
marks omitted).

    We recognize here, for the first time, that Rodriguez at
least partially abrogated this circuit’s previous precedent,
United States v. Turvin, 517 F.3d 1097 (9th Cir. 2008), upon
which the magistrate judge relied and to which the
government now cites for support. Turvin held that a police
officer did not transform a lawful traffic stop into an
unlawful one when, without reasonable suspicion, he took a
break from writing a traffic citation to ask the driver about a
methamphetamine laboratory and obtain the driver’s consent
to search his truck. Id. at 1098. Turvin concluded that
because “the circumstances surrounding the brief pause here
were reasonable,” the extension was permissible despite the
absence of reasonable suspicion. Id. at 1101–02.

    Rodriguez squarely rejected such a reasonableness
standard for determining whether prolonging a traffic stop
for reasons not justified by the initial purpose of the stop is
lawful. 135 S. Ct. at 1616. Instead, Rodriguez requires that a
traffic stop may be extended to conduct an investigation into
matters other than the original traffic violation only if the
10             UNITED STATES V. LANDEROS

officers have reasonable suspicion of an independent
offense. Id.

    Dissenting in Turvin, Judge Paez wrote, “Because I do
not believe that reasonable suspicion supported [the
officer’s] decision to prolong his traffic stop of Turvin, I
would affirm the district court’s order granting Turvin’s
motion to suppress.” 517 F.3d at 1104 (Paez, J., dissenting).
Judge Paez’s dissent aligns with the majority in Rodriguez,
and so highlights the “tension between Turvin, which
permits slight prolongations to ask unrelated questions, and
Rodriguez, which requires independent, reasonable
suspicion if [the additional investigation] adds any time to a
traffic stop.” United States v. Cornejo, 196 F. Supp. 3d 1137,
1151 (E.D. Cal. 2016). As Turvin’s reasonableness standard
cannot be reconciled with the holding of Rodriguez, Turvin
is no longer binding precedent. See Miller v. Gammie, 335
F.3d 889, 893 (9th Cir. 2003) (en banc) (“[W]here the
reasoning or theory of our prior circuit authority is clearly
irreconcilable with the reasoning or theory of intervening
higher authority, a three-judge panel should consider itself
bound by the later and controlling authority, and should
reject the prior circuit opinion as having been effectively
overruled.”).

    Here, the magistrate judge concluded that the extended
stop was permissible because it was “reasonable,” looking to
Turvin rather than Rodriguez to guide the inquiry. The
magistrate wrote, in relevant part:

       “[W]hether questioning unrelated to the
       purpose of the traffic stop and separate from
       the ticket-writing process that prolongs the
       duration of the stop may nonetheless be
       reasonable . . . [upon] examin[ation] [of] the
                 UNITED STATES V. LANDEROS                         11

        totality of the circumstances surrounding the
        stop, and [a] determin[ation] whether
        [Officer Baker’s] conduct was reasonable.”
        United States v. Turvin, 517 F.3d 1097, 1101
        (9th Cir. 2008) (internal quotations and
        citations omitted).

The district court adopted the magistrate judge’s
recommendation, and therefore his analysis, without
comment or explanation. Because it was based on Turvin and
disregarded Rodriguez, the district court’s approval of the
duration of the stop was premised on legal error.

                                 B.

    Applying Rodriguez, we shall assume that Officer Baker
was permitted to prolong the initially lawful stop to ask the
two women for identification, because he had reasonable
suspicion they were underage. 4 But the several minutes of
additional questioning to ascertain Landeros’s identity was
permissible only if it was (1) part of the stop’s “mission” or
(2) supported by independent reasonable suspicion. 135
S. Ct. at 1615.

    A demand for a passenger’s identification is not part of
the mission of a traffic stop. “When stopping an individual
for a minor traffic violation, ‘an officer’s mission includes
ordinary inquiries incident to the traffic stop.’” Evans, 786
F.3d at 786 (quoting Rodriguez, 135 S. Ct. at 1615). These
involve “checking the driver’s license, determining whether
there are outstanding warrants against the driver, and
inspecting the automobile’s registration and proof of
insurance,” and each shares “the same objective as

    4
      We really cannot tell whether the suspicion was reasonable as we
do not know what the two women looked like.
12             UNITED STATES V. LANDEROS

enforcement of the traffic code: ensuring that vehicles on the
road are operated safely and responsibly.” Rodriguez, 135
S. Ct. at 1615. The identity of a passenger, however, will
ordinarily have no relation to a driver’s safe operation of a
vehicle.

    Rodriguez also “recognized that ‘an officer may need to
take certain negligibly burdensome precautions in order to
complete his mission safely.’” Evans, 786 F.3d at 787
(quoting Rodriguez, 135 S. Ct. at 1616 (emphasis added by
Evans court). But knowing Landeros’s name would not have
made the officers any safer. Extending the stop, and thereby
prolonging the officers’ exposure to Landeros, was, if
anything, “inversely related to officer safety.” Evans, 786
F.3d at 787.

                             C.

    The officers’ extension of the stop therefore violated the
Fourth Amendment unless supported by independent
reasonable suspicion. Reasonable suspicion “exists when an
officer is aware of specific, articulable facts which, when
considered with objective and reasonable inferences, form a
basis for particularized suspicion.” United States v.
Montero-Camargo, 208 F.3d 1122, 1129 (9th Cir. 2000) (en
banc); see also Evans, 786 F.3d at 788. The government
argues that Officer Baker had reasonable suspicion of
“underage drinking and curfew violations” based on “the
smell of alcohol and belief that the back seat passengers were
younger than eighteen.” An extension of the traffic stop was
necessary, the government contends, because Landeros’s
“own conduct prevented the officers from being able to
determine whether he had committed the offenses of
underage drinking or curfew violation.” But, on cross-
examination, Officer Baker stated that Landeros did not look
               UNITED STATES V. LANDEROS                   13

“underage” to him at the time of the stop. Further, Officer
Baker’s testimony and reports indicate he asked Landeros
for identification because it was “standard” procedure, not
because he was concerned about Landeros’s age. Indeed, the
reports specifically mention that Officer Baker believed the
two women were underage, but make no mention of
Landeros’s age. As a result, the record does not demonstrate
that Officer Baker had a reasonable suspicion that Landeros
was out past his curfew or drinking underage. Any extension
of the traffic stop to investigate those matters was an
unlawful seizure.

    The government also contends that Landeros’s refusal to
identify himself “provided reasonable suspicion of the
additional offenses of failure to provide identification and
failure to comply with law enforcement orders.” Arizona law
provides:

       It is unlawful for a person, after being advised
       that the person’s refusal to answer is
       unlawful, to fail or refuse to state the person’s
       true full name on request of a peace officer
       who has lawfully detained the person based
       on reasonable suspicion that the person has
       committed, is committing or is about to
       commit a crime.

Ariz. Rev. Stat. Ann. § 13-2412(A). By the plain text of the
statute, Landeros could not have violated Section 13-2412
because, as already explained, the officers lacked reasonable
suspicion, at the time they initially insisted he identify
himself, that Landeros had committed, was committing, or
was about to commit any crimes, including violating curfew
or drinking underage.
14              UNITED STATES V. LANDEROS

    Additionally, Arizona Law provides that “[a] person
shall not willfully fail or refuse to comply with any lawful
order or direction of a police officer invested by law with
authority to direct, control or regulate traffic.” Ariz. Rev.
Stat. Ann. § 28-622(A). The question that remains, then, is
whether law enforcement could lawfully order Landeros to
identify himself, absent reasonable suspicion that he had
committed an offense.

    In some circumstances, a suspect may be required to
respond to an officer’s request to identify herself, and may
be arrested if she does not. Hiibel v. Sixth Judicial District
Court upheld a Nevada “stop and identify” statute, similar to
Arizona’s, that permitted law enforcement to detain “any
person whom the officer encounters under circumstances
which reasonably indicate that the person has committed, is
committing or is about to commit a crime” so as to ascertain
that person’s identity. 542 U.S. 177, 181–82, 185 (2004)
(quoting Nev. Rev. Stat. § 171.123 (2003)). As
authoritatively interpreted by the Nevada Supreme Court,
the statute required only that a suspect disclose her name—
not produce a driver’s license or any other document. Id. at
185.

    The challenge to Nevada’s law arose out of Hiibel’s
arrest for failing to identify himself to law enforcement. Id.
at 181. Earlier on the day of the arrest, the local sheriff’s
department received a report of a man assaulting a woman
in a truck on a particular road. Id. at 180. When an officer
arrived at that road to investigate, he found a truck matching
the reported description, with a man—later identified as
Hiibel—standing outside, and a young woman sitting inside.
Id. at 180–81. The officer explained to the man that he was
investigating a reported fight and repeatedly asked him for
identification. Id. The officer warned Hiibel that if he did not
               UNITED STATES V. LANDEROS                   15

provide identification, he would be arrested for refusing to
identify himself. Id. at 181. Hiibel did not comply, so he was
arrested. Id. The Court determined this application of the
Nevada law permissible, because the request was
“‘reasonably related in scope to the circumstances which
justified’ the stop.” Id. at 189 (quoting Terry v. Ohio, 392
U.S. 1, 20 (1968)). (The Court did not mention that the
officer’s request for “identification,” which it understood as
“a request to produce a driver’s license or some other form
of written identification,” id. at 181, demanded more than
state law required Hiibel to provide.)

    In its opinion, the Court distinguished the circumstances
of Hiibel’s arrest from those of an earlier case, Brown v.
Texas, 443 U.S. 47 (1979). Brown overturned a conviction
under a Texas “stop and identify” law similar to that at issue
in Hiibel. Id. at 49–50. Unlike Hiibel, Brown was stopped,
detained, and interrogated about his identity even though
there was no reasonable suspicion that he had committed any
offense. Id. at 51–52; see also Hiibel, 542 U.S. at 184
(discussing Brown). Brown held squarely that law
enforcement may not require a person to furnish
identification if not reasonably suspected of any criminal
conduct. Brown, 443 U.S. at 52–53.

   In short, Brown holds that an officer may not lawfully
order a person to identify herself absent particularized
suspicion that she has engaged, is engaging, or is about to
engage in criminal activity, and Hiibel does not hold to the
contrary.

    As explained above, the officers insisted several times
that Landeros identify himself after he initially refused, and
detained him while making those demands. At the time they
did so, the officers had no reasonable suspicion that
16             UNITED STATES V. LANDEROS

Landeros had committed an offense. Accordingly, the police
could not lawfully order him to identify himself. His
repeated refusal to do so thus did not, as the government
claims, constitute a failure to comply with an officer’s lawful
order, Ariz. Rev. Stat. Ann. § 28-622(A). There was
therefore no justification for the extension of the detention
to allow the officers to press Landeros further for his
identity.

      Evidence obtained as the result of an unconstitutional
seizure “is ordinarily tainted by the prior illegality and thus
inadmissible, subject to a few recognized exceptions,” none
of which the government contends apply in this case. United
States v. Gorman, 859 F.3d 706, 716 (9th Cir. 2017) (internal
quotation marks omitted.) Here, “the challenged evidence
. . . is unquestionably the product of the illegal governmental
activity—i.e., the wrongful detention.’” New York v. Harris,
495 U.S. 14, 19 (1990) (internal quotation marks and
brackets omitted). The officers discovered the bullets
Landeros was convicted of possessing only because he was
ordered from the car as part of the unlawfully extended
seizure and subsequently consented to a search of his
pockets. As a result, the evidence cannot be introduced at
trial.

    The government repeatedly notes that this court’s
precedent permits police to “ask people [including
passengers in cars] who have legitimately been stopped for
identification without conducting a Fourth Amendment
search or seizure.” United States v. Diaz-Castaneda, 494
F.3d 1146, 1152 (9th Cir. 2007) (emphasis added). But we
need not resolve whether that precedent remains valid after
Rodriguez. Regardless of whether the first request for
Landeros’s identification was lawful, law enforcement’s
               UNITED STATES V. LANDEROS                 17

refusal to take “no” for an answer was not. Diaz-Castaneda
does not suggest otherwise.

    Landeros also refused to comply with the officers’
commands to leave the car. Police officers may order a
suspect out of a car during a traffic stop. Pennsylvania v.
Mimms, 434 U.S. 106, 111 (1977). The Supreme Court has
extended that rule to passengers detained during a lawful
stop. Maryland v. Wilson, 519 U.S. 408 (1997). But here, the
stop was no longer lawful by the time the officers ordered
Landeros to leave the car, as it had extended longer than
justified by either the suspected traffic violation or any
offense as to which there was independent reasonable
suspicion. See Rodriguez, 135 S. Ct. at 1616. As Officer
Baker had, before Landeros was ordered from the car,
impermissibly extended the stop based on Landeros’s refusal
to identify himself, the validity or not of the exit order
standing alone does not matter.

                            III.

   For the foregoing reasons, we REVERSE the district
court’s denial of Landeros’s motion to suppress.

```

---
