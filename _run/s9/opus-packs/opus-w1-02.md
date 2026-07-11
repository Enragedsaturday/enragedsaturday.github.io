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

## GROUP: _overhaul2/lake/cases/Anderson v. Creighton.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Anderson v. Creighton
type: case
citation: "483 U.S. 635 (1987)"
parallel_cite: "107 S. Ct. 3034; 97 L. Ed. 2d 523; 55 U.S.L.W. 5092"
neutral_cite: 1987 U.S. LEXIS 2894
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-06-25
docket: 85-1520
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
  opinion_url: "https://www.courtlistener.com/opinion/111953/anderson-v-creighton/"
  cluster_id: 111953
  opinion_id: null
  identity_checked: true
lake:
  record_id: Anderson v. Creighton
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Foundational (clearly-established at the appropriate level of particularity)"
related:
  - "[[White v. Pauly]]"
  - "[[Harlow v. Fitzgerald]]"
  - "[[Malley v. Briggs]]"
  - "[[Ashcroft v. al-Kidd]]"
  - "[[Pearson v. Callahan]]"
  - "[[Bivens v. Six Unknown Named Agents]]"
tags:
  - case
  - fourth-amendment
  - qualified-immunity
  - section-1983
  - clearly-established-law
  - warrantless-search
  - bivens
holding: "A government official sued for a constitutional violation keeps qualified immunity unless the right was clearly established in a particularized sense — its contours sufficiently clear that a reasonable official would understand his conduct violates it; for a warrantless search the dispositive inquiry is the objective, fact-specific question whether a reasonable officer could have believed the search lawful in light of clearly established law and the information the officers possessed."
---

# Anderson v. Creighton

*483 U.S. 635 (1987)* (No. 85-1520) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the treatment framing below is authored orientation, not machine-certified. Identity cluster 111953 → 483 U.S. 635, No. 85-1520, decided 1987-06-25 (Scalia, J.); Rule/Application quotes string-matched to the CL opinion text 2026-07-07. -->

## Background
On November 11, 1983, FBI agent Russell Anderson led a warrantless search of the Creighton family's home, looking for Vadaain Dixon, a bank-robbery suspect who was not there. The Creightons sued Anderson for money damages under *[[Bivens v. Six Unknown Named Agents|Bivens]]*, alleging a Fourth Amendment violation. Anderson sought summary judgment on [[Qualified Immunity|qualified immunity]]. The District Court granted it (finding probable cause and [[Exigent Circumstances and Hot Pursuit|exigent circumstances]]), but the Eighth Circuit reversed, holding that the right to be free of a warrantless home search absent probable cause and [[Exigent Circumstances and Hot Pursuit|exigency]] was "clearly established," so Anderson could claim no immunity. The Supreme Court granted [[Reading and Citing Cases#certiorari-cert|certiorari]].

## Issue
At what level of generality must a right be "clearly established" before an officer loses [[Qualified Immunity|qualified immunity]] — and, for a warrantless search, whether the officer may still prevail by showing that a reasonable officer could have believed the search lawful.

## Rule
[[Qualified Immunity|Qualified immunity]] turns on whether the right was clearly established at a **particularized** level, not an abstract one. Writing for the Court, Justice Scalia held that "the right the official is alleged to have violated must have been 'clearly established' in a more particularized, and hence more relevant, sense: The contours of the right must be sufficiently clear that a reasonable official would understand that what he is doing violates that right." — 483 U.S. at 640. It is not necessary that "the very action in question ha[ve] previously been held unlawful," "but it is to say that in the light of pre-existing law the unlawfulness must be apparent." — *Id.* ^pin-640

## Application
The Eighth Circuit erred by pitching the right at too high a level of generality — a general right against warrantless home searches lacking probable cause and [[Exigent Circumstances and Hot Pursuit|exigency]]. Framed correctly, the inquiry is fact-specific: "The relevant question in this case, for example, is the objective (albeit fact-specific) question whether a reasonable officer could have believed Anderson's warrantless search to be lawful, in light of clearly established law and the information the searching officers possessed. Anderson's subjective beliefs about the search are irrelevant." — 483 U.S. at 641. [[Reading and Citing Cases#on-remand|On remand]] Anderson was entitled to argue that, as a matter of law, a reasonable officer could have thought the search lawful. ^pin-641

## Conclusion
**Reversed and [[Reading and Citing Cases#on-remand|remanded]].** Scalia, J., wrote for the Court; Stevens, J., dissented (joined by Brennan and Marshall, JJ.). Anderson could press his qualified-immunity defense on the objective-reasonableness standard.

## Treatment & subsequent history
**Good law — foundational.** *Anderson* is the decision that fixed [[Qualified Immunity|qualified immunity]]'s "clearly established" inquiry at a particularized level of generality, and it is the direct antecedent the corpus reaches through *[[White v. Pauly]]* — where the Court again warned that clearly established law must not be defined "at a high level of generality." The particularization principle runs through *[[Ashcroft v. al-Kidd]]* and *[[Mullenix v. Luna]]* and remains the governing frame today.

*Status note (⚪):* authored from a CourtListener-verified identity stub (two-key: cluster 111953 + 483 U.S. 635); renders under the ⚪ banner until S9 promotion. *Mitchell v. Forsyth*, cited in the opinion, is not yet in the corpus and is named in plain text to avoid a dangling link.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Foundational (clearly-established at the appropriate level of [[Particularity|particularity]])*

## Sources
- [*Anderson v. Creighton*, 483 U.S. 635 (1987)](https://www.courtlistener.com/opinion/111953/anderson-v-creighton/) — pinpoints: 640 (particularized "clearly established" standard; Scalia, J.), 641 (objective reasonable-officer question); quotes string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "98d45daaa3dfe8f8", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Anderson v. Creighton"}, "payload": {"all": [{"cite": "483 U.S. 635", "page": "635", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "483"}, {"cite": "107 S. Ct. 3034", "page": "3034", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "107"}, {"cite": "97 L. Ed. 2d 523", "page": "523", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "97"}, {"cite": "1987 U.S. LEXIS 2894", "page": "2894", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1987"}, {"cite": "55 U.S.L.W. 5092", "page": "5092", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "55"}], "display": "483 U.S. 635", "official": {"cite": "483 U.S. 635", "page": "635", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "483"}, "official_selection_present": true, "record_id": "Anderson v. Creighton"}}
{"assertion_id": "0c60d71c69a662d0", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Anderson v. Creighton"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Anderson v. Creighton", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Anderson v. Creighton

```json
{
  "schema_version": "s2.v1",
  "record_id": "Anderson v. Creighton",
  "status": "under_review",
  "identity": {
    "case_name": "Anderson v. Creighton",
    "case_name_short": "Anderson",
    "case_name_full": "ANDERSON v. CREIGHTON Et Al.",
    "input_case_name": "Anderson v. Creighton",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-06-25",
    "year": 1987,
    "docket": "85-1520",
    "cluster_id": 111953,
    "lead_opinion_id": 9431119,
    "sibling_ids": [],
    "absolute_url": "/opinion/111953/anderson-v-creighton/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "483 U.S. 635",
      "volume": "483",
      "reporter": "U.S.",
      "page": "635",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 3034",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "3034",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 L. Ed. 2d 523",
        "volume": "97",
        "reporter": "L. Ed. 2d",
        "page": "523",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 5092",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "5092",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 2894",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "2894",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "483 U.S. 635",
        "volume": "483",
        "reporter": "U.S.",
        "page": "635",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 3034",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "3034",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 L. Ed. 2d 523",
        "volume": "97",
        "reporter": "L. Ed. 2d",
        "page": "523",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 2894",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "2894",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 5092",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "5092",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "483 U.S. 635",
    "official_selection": {
      "court_class": "scotus",
      "selected": "483 U.S. 635",
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
    "date_created": "2026-07-08T00:38:32Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [
      "W10 on-read identity re-verification 2026-07-07: docket 85-1520 confirmed verbatim from CL lead-opinion caption (html_with_citations)"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-08T00:38:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T00:38:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T00:38:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-08T00:38:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "anderson-v-creighton--111953",
      "to_record_id": "Anderson v. Creighton",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Anderson v. Creighton

```
<opinion type="majority">
<author id="b686-10">Justice Scalia</author>
<p id="Av4Q">delivered the opinion of the Court.</p>
<p id="b686-11">The question presented is whether a federal law enforcement officer who participates in a search that violates the Fourth Amendment may be held personally liable for money <page-number citation-index="1" label="637">*637</page-number>damages if a reasonable officer could have believed that the search comported with the Fourth Amendment.</p>
<p id="b687-5">I</p>
<p id="b687-6">Petitioner Russell Anderson is an agent of the Federal Bureau of Investigation. On November 11, 1983, Anderson and other state and federal law enforcement officers conducted a warrantless search of the home of respondents, the Creighton family. The search was conducted because Anderson believed that Vadaain Dixon, a man suspected of a bank robbery committed earlier that day, might be found there. He was not.</p>
<p id="b687-7">The Creightons later filed suit against Anderson in a Minnesota state court, asserting among other things a claim for money damages under the Fourth Amendment, see <em>Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971).<footnotemark>1</footnotemark> After removing the suit to Federal District Court, Anderson filed a motion to dismiss or for summary judgment, arguing that the <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span> </em>claim was barred by Anderson’s qualified immunity from civil damages liability. See <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800</a></span> (1982). Before any discovery took place, the District Court granted summary judgment on the ground that the search was lawful, holding that the undisputed facts revealed that Anderson had had probable cause to search the Creighton’s home and that his failure to obtain a warrant was justified by the presence of exigent circumstances. App. to Pet. for Cert. 23a-25a.</p>
<p id="b687-8">The Creightons appealed to the Court of Appeals for the Eighth Circuit, which reversed. <em>Creighton </em>v. <em>St. Paul, </em><span class="citation multiple-matches"><a href="/c/F.%202d/766/1269/">766 F. 2d 1269</a></span> (1985). The Court of Appeals held that the issue of the lawfulness of the search could not properly be decided on summary judgment, because unresolved factual disputes <page-number citation-index="1" label="638">*638</page-number>made it impossible to determine as a matter of law that the warrantless search had been supported by probable cause and exigent circumstances. <em>Id., </em>at 1272-1276. The Court of Appeals also held that Anderson was not entitled to summary judgment on qualified immunity grounds, since the right Anderson was alleged to have violated — the right of persons to be protected from warrantless searches of their home unless the searching officers have probable cause and there are exigent circumstances — was clearly established. <em>Ibid.</em></p>
<p id="b688-5">Anderson filed a petition for certiorari, arguing that the Court of Appeals erred by refusing to consider his argument that he was entitled to summary judgment on qualified immunity grounds if he could establish as a matter of law that a reasonable officer could have believed the search to be lawful. We granted the petition, <span class="citation multiple-matches"><a href="/c/U.%20S./478/1003/">478 U. S. 1003</a></span> (1986), to consider that important question.</p>
<p id="b688-6">II</p>
<p id="b688-7">When government officials abuse their offices, “action[s] for damages may offer the only realistic avenue for vindication of constitutional guarantees.” <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#814" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 814</a></span>. On the other hand, permitting damages suits against government officials can entail substantial social costs, including the risk that fear of personal monetary liability and harassing litigation will unduly inhibit officials in the discharge of their duties. <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Ibid.</a></span> </em>Our cases have accommodated these conflicting concerns by generally providing government officials performing discretionary functions with a qualified immunity, shielding them from civil damages liability as long as their actions could reasonably have been thought consistent with the rights they are alleged to have violated. See, <em>e. g., Malley </em>v. <em>Briggs, </em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#341" aria-description="Citation for case: Malley v. Briggs">475 U. S. 335, 341</a></span> (1986) (qualified immunity protects “all but the plainly incompetent or those who knowingly violate the law”); <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#344" aria-description="Citation for case: Malley v. Briggs"><em>id., </em>at 344-345</a></span> (police officers applying for warrants are immune if a <page-number citation-index="1" label="639">*639</page-number>reasonable officer could have believed that there was probable cause to support the application); <em>Mitchell </em>v. <em>Forsyth, </em><span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/#528" aria-description="Citation for case: Mitchell v. Forsyth">472 U. S. 511, 528</a></span> (1985) (officials are immune unless “the law clearly proscribed the actions” they took); <em>Davis </em>v. <em>Scherer, </em><span class="citation" data-id="9429708"><a href="/opinion/111241/davis-v-scherer/#191" aria-description="Citation for case: Davis v. Scherer">468 U. S. 183, 191</a></span> (1984); <span class="citation" data-id="9429708"><a href="/opinion/111241/davis-v-scherer/#198" aria-description="Citation for case: Davis v. Scherer"><em>id., </em>at 198</a></span> (Brennan, J., concurring in part and dissenting in part); <em>Harlow </em>v. <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#819" aria-description="Citation for case: Harlow v. Fitzgerald"><em>Fitzgerald, supra, </em>at 819</a></span>. Cf., <em>e. g., Procunier </em>v. <em>Navarette, </em><span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/#562" aria-description="Citation for case: Procunier v. Navarette">434 U. S. 555, 562</a></span> (1978). Somewhat more concretely, whether an official protected by qualified immunity may be held personally liable for an allegedly unlawful official action generally turns on the “objective legal reasonableness” of the action, <em>Harlow, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#819" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 819</a></span>, assessed in light of the legal rules that were “clearly established” at the time it was taken, <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald"><em>id., </em>at 818</a></span>.</p>
<p id="b689-5">The operation of this standard, however, depends substantially upon the level of generality at which the relevant “legal rule” is to be identified. For example, the right to due process of law is quite clearly established by the Due Process Clause, and thus there is a sense in which any action that violates that Clause (no matter how unclear it may be that the particular action is a violation) violates a clearly established right. Much the same could be said of any other constitutional or statutory violation. But if the test of “clearly established law” were to be applied at this level of generality, it would bear no relationship to the “objective legal reasonableness” that is the touchstone of <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span>. </em>Plaintiffs would be able to convert the rule of qualified immunity that our cases plainly establish into a rule of virtually unqualified liability simply by alleging violation of extremely abstract rights. <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>would be transformed from a guarantee of immunity into a rule of pleading. Such an approach, in sum, would destroy “the balance that our cases strike between the interests in vindication of citizens’ constitutional rights and in public officials’ effective performance of their.duties,” by making it impossible for officials “reasonably [to] anticipate when their conduct may give rise to liability for damages.” <em><span class="citation" data-id="9429708"><a href="/opinion/111241/davis-v-scherer/" aria-description="Citation for case: Davis v. Scherer">Davis</a></span>, </em><page-number citation-index="1" label="640">*640</page-number><em>swpra </em>at 195.<footnotemark>2</footnotemark> It should not be surprising, therefore, that our cases establish that the right the official is alleged to have violated must have been “clearly established” in a more particularized, and hence more relevant, sense: The contours of the right must be sufficiently clear that a reasonable official would understand that what he is doing violates that right. This is not to say that an official action is protected by qualified immunity unless the very action in question has previously been held unlawful, see <span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/#535" aria-description="Citation for case: Mitchell v. Forsyth"><em>Mitchell, supra, </em>at 535, n. 12</a></span>; but it is to say that in the light of pre-existing law the unlawfulness must be apparent. See, <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#344" aria-description="Citation for case: Malley v. Briggs"><em>e. g., Malley, supra, </em>at 344-345</a></span>; <span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/#528" aria-description="Citation for case: Mitchell v. Forsyth"><em>Mitchell, supra, </em>at 528</a></span>; <span class="citation" data-id="9429708"><a href="/opinion/111241/davis-v-scherer/#191" aria-description="Citation for case: Davis v. Scherer"><em>Davis, supra, </em>at 191, 195</a></span>.</p>
<p id="b690-5">Anderson contends that the Court of Appeals misapplied these principles. We agree. The Court of Appeals’ brief discussion of qualified immunity consisted of little more than an assertion that a general right Anderson was alleged to have violated — the right to be free from warrantless searches of one’s home unless the searching officers have probable cause and there are exigent circumstances — was clearly established. The Court of Appeals specifically refused to consider the argument that it was <em>not </em>clearly established that the circumstances with which Anderson was confronted did <page-number citation-index="1" label="641">*641</page-number>not constitute probable cause and exigent circumstances. The previous discussion should make clear that this refusal was erroneous. It simply does not follow immediately from the conclusion that it was firmly established that warrantless searches not supported by probable cause and exigent circumstances violate the Fourth Amendment that Anderson’s search was objectively legally unreasonable. We have recognized that it is inevitable that law enforcement officials will in some cases reasonably but mistakenly conclude that probable cause is present, and we have indicated that in such cases those officials — like other officials who act in ways they reasonably believe to be lawful — should not be held personally liable. See <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#344" aria-description="Citation for case: Malley v. Briggs"><em>Malley, supra, </em>at 344-345</a></span>. The same is true of their conclusions regarding exigent circumstances.</p>
<p id="b691-5">It follows from what we have said that the determination whether it was objectively legally reasonable to conclude that a given search was supported by probable cause or exigent circumstances will often require examination of the information possessed by the searching officials. But contrary to the Creightons’ assertion, this does not reintroduce into qualified immunity analysis the inquiry into officials’ subjective intent that <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>sought to minimize. See <em>Harlow, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#815" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 815-820</a></span>. The relevant question in this case, for example, is the objective (albeit fact-specific) question whether a reasonable officer could have believed Anderson’s warrantless search to be lawful, in light of clearly established law and the information the searching officers possessed. Anderson’s subjective beliefs about the search are irrelevant.</p>
<p id="b691-6">The principles of qualified immunity that we reaffirm today require that Anderson be permitted to argue that he is entitled to summary judgment on the ground that, in light of the clearly established principles governing warrantless searches, he could, as a matter of law, reasonably have believed that the search of the Creightons’ home was lawful.<footnotemark>3</footnotemark></p>
<p id="b692-4"><page-number citation-index="1" label="642">*642</page-number>Ill</p>
<p id="b692-5">In addition to relying on the reasoning of the Court of Appeals, the Creightons advance three alternative grounds for affirmance. All of these take the same form, <em>i. e., </em>that even if Anderson is entitled to qualified immunity under the usual principles of qualified immunity law we have just described, an exception should be made to those principles in the circumstances of this case. We note at the outset the heavy burden this argument must sustain to be successful. We have emphasized that the doctrine of qualified immunity reflects a balance that has been struck “across the board,” <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#821" aria-description="Citation for case: Harlow v. Fitzgerald"><em>Harlow, supra, </em>at 821</a></span> (Brennan, J., concurring). See also <em>Malley, </em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#340" aria-description="Citation for case: Malley v. Briggs">475 U. S., at 340</a></span> (“ ‘For executive officers in general, . . . qualified immunity represents the norm’ ” (quoting <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#807" aria-description="Citation for case: Harlow v. Fitzgerald"><em>Harlow, supra, </em>at 807</a></span>)).<footnotemark>4</footnotemark> Although we have in narrow circumstances provided officials with an absolute immunity, see, <page-number citation-index="1" label="643">*643</page-number><em>e. g., Nixon </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428860"><a href="/opinion/110762/nixon-v-fitzgerald/" aria-description="Citation for case: Nixon v. Fitzgerald">457 U. S. 731</a></span> (1982), we have been unwilling to complicate qualified immunity analysis by making the scope or extent of immunity turn on the precise nature of various officials’ duties or the precise character of the particular rights alleged to have been violated. An immunity that has as many variants as there are modes of official action and types of rights would not give conscientious officials that assurance of protection that it is the object of the doctrine to provide. With that observation in mind, we turn to the particular arguments advanced by the Creightons.</p>
<p id="b693-5">First, and most broadly, the Creightons argue that it is inappropriate to give officials alleged to have violated the Fourth Amendment — and thus necessarily to have <em>unreasonably </em>searched or seized — the protection of a qualified immunity intended only to protect reasonable official action. It is not possible, that is, to say that one “reasonably” acted unreasonably. The short answer to this argument is that it is foreclosed by the fact that we have previously extended qualified immunity to officials who were alleged to have violated the Fourth Amendment. See <em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">Malley, supra</a></span> </em>(police officers alleged to have caused an unconstitutional arrest); <em>Mitchell </em>v. <em>Forsyth, </em><span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/" aria-description="Citation for case: Mitchell v. Forsyth">472 U. S. 511</a></span> (1985) (officials alleged to have conducted warrantless wiretaps). Even if that were not so, however, we would still find the argument unpersuasive. Its surface appeal is attributable to the circumstance that the Fourth Amendment’s guarantees have been expressed in terms of “unreasonable” searches and seizures. Had an equally serviceable term, such as “undue” searches and seizures been employed, what might be termed the “reasonably unreasonable” argument against application of <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>to the Fourth Amendment would not be available — just as it <em>would </em>be available against application of <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>to the Fifth Amendment if the term “reasonable process of law” had been employed there. The fact is that, regardless of the terminology used, the precise content of most of the Constitution’s <page-number citation-index="1" label="644">*644</page-number>civil-liberties guarantees rests upon an assessment of what accommodation between governmental need and individual freedom is reasonable, so that the Creightons’ objection, if it has any substance, applies to the application of <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>generally. We have frequently observed, and our many cases on the point amply demonstrate, the difficulty of determining whether particular searches or seizures comport with the Fourth Amendment. See, <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#341" aria-description="Citation for case: Malley v. Briggs"><em>e. g., Malley, supra, </em>at 341</a></span>. Law enforcement officers whose judgments in making these difficult determinations are objectively legally reasonable should no more be held personally liable in damages than should officials making analogous determinations in other areas of law.</p>
<p id="b694-5">For the same reasons, we also reject the Creightons’ narrower suggestion that we overrule <em><span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/" aria-description="Citation for case: Mitchell v. Forsyth">Mitchell, supra</a></span> </em>(extending qualified immunity to officials who conducted warrantless wiretaps), by holding that qualified immunity may never be extended to officials who conduct unlawful warrant-less searches.</p>
<p id="b694-6">Finally, we reject the Creightons’ narrowest and most Procrustean proposal: that no immunity should be provided to police officers who conduct unlawful warrantless searches of innocent third parties’ homes in search of fugitives. They rest this proposal on the assertion that officers conducting such searches were strictly liable at English common law if the fugitive was not present. See, <em>e. g., Entick </em>v. <em>Carrington, </em>19 How. St. Tr. 1029, 95 Eng. Rep. 807 (K. B. 1765). Although it is true that we have observed that our determinations as to the scope of official immunity are made in the light of the “common-law tradition,”<footnotemark>5</footnotemark> <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#342" aria-description="Citation for case: Malley v. Briggs"><em>Malley, supra, </em>at 342</a></span>, <page-number citation-index="1" label="645">*645</page-number>we have never suggested that the precise contours of official immunity can and should be slavishly derived from the often arcane rules of the common law. That notion is plainly contradicted by <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span>, </em>where the Court completely reformulated qualified immunity along principles not at all embodied in the common law, replacing the inquiry into subjective malice so frequently required at common law with an objective inquiry into the legal reasonableness of the official action. See <em>Harlow, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#815" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 815-820</a></span>. As we noted before, <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>clearly expressed the understanding that the general principle of qualified immunity it established would be applied “across the board.”</p>
<p id="b695-5">The approach suggested by the Creightons would introduce into qualified immunity analysis a complexity rivaling that which we found sufficiently daunting to deter us from tailoring the doctrine to the nature of officials’ duties or of the rights allegedly violated. See <em>supra, </em>at 642-643. Just in the field of unlawful arrests, for example, a cursory examination of the Restatement (Second) of Torts (1965) suggests that special exceptions from the general rule of qualified immunity would have to be made for arrests pursuant to a warrant but outside the jurisdiction of the issuing authority, §§ 122, 129(a), arrests after the warrant had lapsed, §§ 122, 130(a), and arrests without a warrant, § 121. Both the complexity and the unsuitability of this approach are betrayed by the fact that the Creightons’ proposal itself does not actually apply the musty rule that is purportedly its justification but instead suggests an exception to qualified immunity for all fugitive searches of third parties’ dwellings, and not merely (as the English rule appears to have provided) for all <em>unsuccessful </em>fugitive searches of third parties’ dwellings. Moreover, from the sources cited by the Creightons it appears to have been a corollary of the English rule that where the search <em>was </em>successful, no civil action would lie, whether or not probable cause for the search existed. That also is (quite pru<page-number citation-index="1" label="646">*646</page-number>dently but quite illogically) not urged upon us in the Creightons’ selective use of the common law.</p>
<p id="b696-5">The general rule of qualified immunity is intended to provide government officials with the ability “reasonably [to] anticipate when their conduct may give rise to liability for damages.” <em>Davis, </em><span class="citation" data-id="9429708"><a href="/opinion/111241/davis-v-scherer/#195" aria-description="Citation for case: Davis v. Scherer">468 U. S., at 195</a></span>. Where that rule is applicable, officials can know that they will not be held personally liable as long as their actions are reasonable in light of current American law. That security would be utterly defeated if officials were unable to determine whether they were protected by the rule without entangling themselves in the vagaries of the English and American common law. We are unwilling to Balkanize the rule of qualified immunity by carving exceptions at the level of detail the Creightons propose. We therefore decline to make an exception to the general rule of qualified immunity for cases involving allegedly unlawful warrantless searches of innocent third parties’ homes in search of fugitives.</p>
<p id="b696-6">For the reasons stated, we vacate the judgment of the Court of Appeals and remand the case for further proceedings consistent with this opinion.<footnotemark>6</footnotemark></p>
<p id="b696-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b687-9"> The Creightons also named other defendants and advanced various other claims against both Anderson and the other defendants. Only the <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span> </em>claim against Anderson remains at issue in this case, however.</p>
</footnote>
<footnote label="2">
<p id="b690-6"> The dissent, which seemingly would adopt this approach, seeks to avoid the unqualified liability that would follow by advancing the suggestion that officials generally (though not law enforcement officials, see <em>post, </em>at 654, 661-662, and officials accused of violating the Fourth Amendment, see <em>post, </em>at 659-667) be permitted to raise a defense of reasonable good faith, which apparently could be asserted and proved only at trial. See <em>post, </em>at 653. But even when so modified (and even for the fortunate officials to whom the modification applies) the approach would totally abandon the concern — which was the driving force behind Harlow’s substantial reformulation of qualified-immunity principles — that “insubstantial claims” against government officials be resolved prior to discovery and on summary judgment if possible. <em>Harlow, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 818-819</a></span>. A passably clever plaintiff would always be able to identify an abstract clearly established right that the defendant could be alleged to have violated, and the good-faith defense envisioned by the dissent would be available only at trial.</p>
</footnote>
<footnote label="3">
<p id="b691-7"> The Creightons argue that the qualified immunity doctrine need not be expanded to apply to the circumstances of this case, because the Federal <page-number citation-index="1" label="642">*642</page-number>Government and various state governments have established programs through which they reimburse officials for expenses and liability incurred in suits challenging actions they have taken in their official capacities. Because our holding today does not extend official qualified immunity beyond the bounds articulated in <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>and our subsequent cases, an argument as to why we should not do so is beside the point. Moreover, even assuming that conscientious officials care only about their personal liability and not the liability of the government they serve, the Creightons do not and could not reasonably contend that the programs to which they refer make reimbursement sufficiently certain and generally available to justify reconsideration of the balance struck in <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>and subsequent cases. See <span class="citation no-link">28 CFR § 50.15</span>(c) (1987) <em>(permitting </em>reimbursement of Department of Justice employees when the Attorney General finds reimbursement appropriate); 5 F. Harper, F. James, &amp; O. Gray, Law of Torts § 29.9, n. 20 (2d ed. 1986) (listing various state programs).</p>
</footnote>
<footnote label="4">
<p id="b692-10"> These decisions demonstrate the emptiness of the dissent’s assertion that “[tjoday this Court makes the fundamental error of simply assuming that <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>immunity is just as appropriate for federal law enforcement officers ... as it is <em>for </em>high <em>government </em>officials.” <em>Post, at 654 (footnote </em>omitted). Just last Term the Court unanimously held that state and federal law enforcement officers were protected by the qualified immunity described in <em>Harlow. Malley </em>v. <em>Briggs, </em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">475 U. S. 335</a></span> (1986). We see no reason to overrule that holding.</p>
</footnote>
<footnote label="5">
<p id="b694-7"> Of course, it is the American rather than the English common-law tradition that is relevant, cf. <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#340" aria-description="Citation for case: Malley v. Briggs"><em>Malley, supra, </em>at 340-342</a></span>; and the American rule appears to have been considerably less draconian than the English. See Restatement (Second) of Torts §§ 204, 206 (1965) (officers with an arrest warrant are privileged to enter a third party’s house to effect arrest if they reasonably believe the fugitive to be there).</p>
</footnote>
<footnote label="6">
<p id="b696-8"> Noting that no discovery has yet taken place, the Creightons renew their argument that, whatever the appropriate qualified immunity standard, some discovery would be required before Anderson’s summary judgment motion could be granted. We think the matter somewhat more complicated. One of the purposes of the <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>qualified immunity standard is to protect public officials from the “broad-ranging discovery” that can be “peculiarly disruptive of effective government.” 457 U. S., at 817 (footnote omitted). For this reason, we have emphasized that qualified immunity questions should be resolved at the earliest possible stage of a litigation. <em>Id., </em>at 818. See also <em>Mitchell </em>v. <em>Forsyth, </em><span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/#526" aria-description="Citation for case: Mitchell v. Forsyth">472 U. S. 511, 526</a></span> (1986). Thus, on remand, it should first be determined whether the actions the Creightons allege Anderson to have taken are actions that a reasonable officer could have believed lawful. If they are, then Anderson is entitled to dismissal prior to discovery. Cf. <em><span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/" aria-description="Citation for case: Mitchell v. Forsyth">ibid.</a></span> </em>If they are not, and if the actions Anderson claims he took are different from those the Creightons allege (and are actions that a reasonable officer could have believed lawful), <page-number citation-index="1" label="647">*647</page-number>then discovery may be necessary before Anderson’s motion for summary judgment on qualified immunity grounds can be resolved. Of course, any such discovery should be tailored specifically to the question of Anderson’s qualified immunity.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Andresen v. Maryland.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Andresen v. Maryland"
type: case
citation: "427 U.S. 463 (1976)"
parallel_cite: "96 S. Ct. 2737; 49 L. Ed. 2d 627"
neutral_cite: 1976 U.S. LEXIS 78
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-06-29
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-06-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Andresen v. Maryland
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109522/andresen-v-maryland/"
  cluster_id: 109522
  opinion_id: 109522
  identity_checked: true
homes:
  - page: "[[Particularity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Groh v. Ramirez]]", "[[Coolidge v. New Hampshire]]", "[[Warden v. Hayden]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant", "particularity", "fifth-amendment", "business-records"]
holding: "A particularized warrant to search for and seize a person's business records, and their introduction in evidence, does not violate the…"
lake:
  record_id: Andresen v. Maryland
  status: verified
  projected_at: 2026-07-06
---

# Andresen v. Maryland

*427 U.S. 463 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Maryland investigators probing a real-estate false-pretenses scheme involving the sale of "Lot 13T" obtained warrants and searched the offices of Andresen, an attorney, seizing his business records — some of which contained statements he had written. The records were introduced at trial and he was convicted of false pretenses and fraudulent misappropriation.

## Issue
(1) Whether seizing an individual's own business records under a search warrant, and introducing them at his trial, violates the Fifth Amendment privilege against self-incrimination; and (2) whether a warrant's catch-all phrase — "together with other fruits, instrumentalities and evidence of crime at this [time] unknown" — rendered it an impermissibly general warrant.

## Rule
No Fifth Amendment violation: records voluntarily created before the search are not compelled testimony. "[P]etitioner was not asked to say or to do anything. The records seized contained statements that petitioner had voluntarily committed to writing." — 427 U.S. at 473. ^pin-473

The Court therefore held: "we hold that the search of an individual's office for business records, their seizure, and subsequent introduction into evidence do not offend the Fifth Amendment's proscription that '[n]o person . . . shall be compelled in any criminal case to be a witness against himself.'" — *Id.* at 477. ^pin-477

The warrant was sufficiently particular when its catch-all phrase is read in context: "the challenged phrase must be read as authorizing only the search for and seizure of evidence relating to 'the crime of false pretenses with respect to Lot 13T.'" — *Id.* at 480. ^pin-480

## Application
On these facts the seized records had been voluntarily committed to paper before officers arrived, Andresen was never required to say or do anything, and the documents were authenticated at trial by a handwriting expert rather than by him — so there was no compulsion and no Fifth Amendment violation. And the contested "other fruits" clause appeared at the end of a long sentence listing particular Lot-13T documents; read in that context it reached only evidence of the false-pretenses crime concerning Lot 13T, so the warrant was not a forbidden general warrant.

## Conclusion
Neither the Fifth Amendment nor the [[Particularity|particularity]] requirement was violated; the judgment of the Maryland Court of Special Appeals was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Andresen* remains the leading authority that pre-existing, voluntarily prepared business records seized under a valid warrant are not "compelled" testimony, and that a particular list of items is not made "general" by a contextually limited catch-all phrase. Compare [[Groh v. Ramirez]] (a warrant that fails altogether to describe the things to be seized is facially invalid).

## Appears on
- [[Particularity]] — *Key — Progeny / Refinement*

## Sources
- *Andresen v. Maryland*, 427 U.S. 463 (1976) — https://www.courtlistener.com/opinion/109522/andresen-v-maryland/ — pinpoints: 473, 477, 480.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "59edb912afa15736", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Andresen v. Maryland"}, "payload": {"all": [{"cite": "427 U.S. 463", "page": "463", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "427"}, {"cite": "96 S. Ct. 2737", "page": "2737", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "96"}, {"cite": "49 L. Ed. 2d 627", "page": "627", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "49"}, {"cite": "1976 U.S. LEXIS 78", "page": "78", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1976"}], "display": "427 U.S. 463", "official": {"cite": "427 U.S. 463", "page": "463", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "427"}, "official_selection_present": true, "record_id": "Andresen v. Maryland"}}
{"assertion_id": "1035ce1de370f3de", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-473", "record_id": "Andresen v. Maryland"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-473", "pinpoint_status": "slip-only", "quote": "— rendered it an impermissibly general warrant. ## Rule No Fifth Amendment violation: records voluntarily created before the search are not compelled testimony.", "quote_fidelity": "mismatch", "record_id": "Andresen v. Maryland", "star_marker": null}}
{"assertion_id": "be9349f42212c1c3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-477", "record_id": "Andresen v. Maryland"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-477", "pinpoint_status": "slip-only", "quote": "we hold that the search of an individual's office for business records, their seizure, and subsequent introduction into evidence do not offend the Fifth Amendment's proscription that '[n]o person . . . shall be compelled in any criminal case to be a witness against himself.'", "quote_fidelity": "mismatch", "record_id": "Andresen v. Maryland", "star_marker": null}}
{"assertion_id": "c3a74c101496e14b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-480", "record_id": "Andresen v. Maryland"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-480", "pinpoint_status": "slip-only", "quote": "the challenged phrase must be read as authorizing only the search for and seizure of evidence relating to 'the crime of false pretenses with respect to Lot 13T.'", "quote_fidelity": "mismatch", "record_id": "Andresen v. Maryland", "star_marker": null}}
{"assertion_id": "086341120640a967", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Andresen v. Maryland"}, "payload": {"as_of_content": "1976-06-29", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Andresen v. Maryland", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Andresen v. Maryland

```json
{
  "schema_version": "s2.v1",
  "record_id": "Andresen v. Maryland",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Andresen v. Maryland",
    "case_name_short": "Andresen",
    "case_name_full": "Andresen v. Maryland",
    "input_case_name": "Andresen v. Maryland",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-06-29",
    "year": 1976,
    "docket": null,
    "cluster_id": 109522,
    "lead_opinion_id": 109522,
    "sibling_ids": [
      109522,
      9426530,
      9426531,
      9426532
    ],
    "absolute_url": "/opinion/109522/andresen-v-maryland/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9006080,
        "score": 10,
        "case_name": "Andresen v. Maryland"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "427 U.S. 463",
      "volume": "427",
      "reporter": "U.S.",
      "page": "463",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 2737",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "2737",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 627",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "627",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 78",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "78",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "427 U.S. 463",
        "volume": "427",
        "reporter": "U.S.",
        "page": "463",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 2737",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "2737",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 627",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "627",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 78",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "78",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "427 U.S. 463",
    "official_selection": {
      "court_class": "scotus",
      "selected": "427 U.S. 463",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-473",
      "page": null,
      "quote": "\u2014 rendered it an impermissibly general warrant. ## Rule No Fifth Amendment violation: records voluntarily created before the search are not compelled testimony.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-477",
      "page": null,
      "quote": "we hold that the search of an individual's office for business records, their seizure, and subsequent introduction into evidence do not offend the Fifth Amendment's proscription that '[n]o person . . . shall be compelled in any criminal case to be a witness against himself.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-480",
      "page": null,
      "quote": "the challenged phrase must be read as authorizing only the search for and seizure of evidence relating to 'the crime of false pretenses with respect to Lot 13T.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-06-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Andresen v. Maryland",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Porath v. State",
          "cluster_id": 1770795,
          "cite": [
            "148 S.W.3d 402",
            "2004 WL 1660763"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Triumph Capital Group, Inc.",
          "cluster_id": 8751433,
          "cite": [
            "211 F.R.D. 31",
            "2002 U.S. Dist. LEXIS 21615",
            "2002 WL 31487754"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hernandez v. State",
          "cluster_id": 1882057,
          "cite": [
            "60 S.W.3d 106",
            "2001 Tex. Crim. App. LEXIS 104",
            "2001 WL 1415274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Leon",
          "cluster_id": 111262,
          "cite": [
            "82 L. Ed. 2d 677",
            "104 S. Ct. 3405",
            "468 U.S. 897",
            "1984 U.S. LEXIS 153"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Waller v. Georgia",
          "cluster_id": 111186,
          "cite": [
            "81 L. Ed. 2d 31",
            "104 S. Ct. 2210",
            "467 U.S. 39",
            "1984 U.S. LEXIS 86",
            "52 U.S.L.W. 4618",
            "10 Media L. Rep. (BNA) 1714"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
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
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
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
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
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
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Garrison",
          "cluster_id": 111823,
          "cite": [
            "94 L. Ed. 2d 72",
            "107 S. Ct. 1013",
            "480 U.S. 79",
            "1987 U.S. LEXIS 559",
            "55 U.S.L.W. 4190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Muniz",
          "cluster_id": 112464,
          "cite": [
            "110 L. Ed. 2d 528",
            "110 S. Ct. 2638",
            "496 U.S. 582",
            "1990 U.S. LEXIS 3211"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Stenson",
          "cluster_id": 1172684,
          "cite": [
            "940 P.2d 1239"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
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
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Messerschmidt v. Millender",
          "cluster_id": 623242,
          "cite": [
            "182 L. Ed. 2d 47",
            "132 S. Ct. 1235",
            "565 U.S. 535",
            "2012 U.S. LEXIS 1687"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
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
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "G. M. Leasing Corp. v. United States",
          "cluster_id": 109579,
          "cite": [
            "50 L. Ed. 2d 530",
            "97 S. Ct. 619",
            "429 U.S. 338",
            "1977 U.S. LEXIS 33",
            "39 A.F.T.R.2d (RIA) 475"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Doe",
          "cluster_id": 111110,
          "cite": [
            "79 L. Ed. 2d 552",
            "104 S. Ct. 1237",
            "465 U.S. 605",
            "1984 U.S. LEXIS 169",
            "15 Fed. R. Serv. 1",
            "52 U.S.L.W. 4296",
            "57 A.F.T.R.2d (RIA) 1270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ewing v. City of Stockton",
          "cluster_id": 1310475,
          "cite": [
            "588 F.3d 1218",
            "2009 U.S. App. LEXIS 26799",
            "2009 WL 4641736"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Melson",
          "cluster_id": 2442934,
          "cite": [
            "638 S.W.2d 342",
            "1982 Tenn. LEXIS 431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe v. United States",
          "cluster_id": 112123,
          "cite": [
            "101 L. Ed. 2d 184",
            "108 S. Ct. 2341",
            "487 U.S. 201",
            "1988 U.S. LEXIS 2869",
            "56 U.S.L.W. 4708",
            "25 Fed. R. Serv. 632",
            "62 A.F.T.R.2d (RIA) 5744"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Willie H. Dennis",
          "cluster_id": 380192,
          "cite": [
            "625 F.2d 782"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hubbell",
          "cluster_id": 1087666,
          "cite": [
            "147 L. Ed. 2d 24",
            "120 S. Ct. 2037",
            "530 U.S. 27",
            "2000 U.S. LEXIS 3768"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Young",
          "cluster_id": 8934968,
          "cite": [
            "745 F.2d 733"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Davis",
          "cluster_id": 8923386,
          "cite": [
            "636 F.2d 1028"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Joe Whitten, John Elmer Gaiefsky, Jack Wayne Gish, Richard Lawrence Shimel",
          "cluster_id": 418069,
          "cite": [
            "706 F.2d 1000",
            "13 Fed. R. Serv. 384",
            "1983 U.S. App. LEXIS 27369"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matter of Vanderbilt (Rosner-Hickey)",
          "cluster_id": 2592656,
          "cite": [
            "57 N.Y.2d 66",
            "439 N.E.2d 378",
            "453 N.Y.S.2d 662",
            "1982 N.Y. LEXIS 3577"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John F. Gardiner (05-1247) Ronald Lupo (05-1248)",
          "cluster_id": 795717,
          "cite": [
            "463 F.3d 445",
            "2006 U.S. App. LEXIS 23176",
            "2006 WL 2597365"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Thompson",
          "cluster_id": 4858089,
          "cite": [
            "2021 CO 15"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
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
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109522 OR 9426530 OR 9426531 OR 9426532) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05MjgzNjgwMDAwMDAmcz03NjQ3MzcmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109522+OR+9426530+OR+9426531+OR+9426532%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      },
      "lane2_top_cited": {
        "query": "cites:(109522 OR 9426530 OR 9426531 OR 9426532)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTMmcz0xMTk2MTc0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109522+OR+9426530+OR+9426531+OR+9426532%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109522 OR 9426530 OR 9426531 OR 9426532)",
        "reviewed": 18,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 18,
        "triage_read": 0,
        "triage_snippet_classified": 18
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109522 OR 9426530 OR 9426531 OR 9426532)",
    "indexed_citing_opinions": 849,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109522,
        "count": 752,
        "count_source": "search"
      },
      {
        "opinion_id": 9426530,
        "count": 109,
        "count_source": "search"
      },
      {
        "opinion_id": 9426531,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426532,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1306,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/andresen-v-maryland.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyMTA2MTcmcz0xMDYyODQyOCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109522+OR+9426530+OR+9426531+OR+9426532%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109522,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 97758,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 97862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 104016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 104655,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 108650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 108710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 108830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 109046,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 109332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 109432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 284440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 297692,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 299281,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 303166,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 305642,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 317124,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 330234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 1480134,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 1895902,
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
    "date_created": "2026-07-04T18:01:08Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:01:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:01:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:07:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:01:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Andresen v. Maryland

```
<div>
<center><b><span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">427 U.S. 463</a></span> (1976)</b></center>
<center><h1>ANDRESEN<br>
v.<br>
MARYLAND.</h1></center>
<center>No. 74-1646.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 25, 1976.</center>
<center>Decided June 29, 1976.</center>
CERTIORARI TO THE COURT OF SPECIAL APPEALS OF MARYLAND.
<p><span class="star-pagination">*464</span> <i>Peter C. Andresen,</i> petitioner, <i>pro se,</i> argued the cause and filed a brief.</p>
<p><i>Jon F. Oster,</i> Deputy Attorney General of Maryland, argued the cause for respondent. With him on the brief were <i>Francis B. Burch,</i> Attorney General, and <i>Clarence W. Sharp</i> and <i>Gilbert Rosenthal,</i> Assistant Attorneys General.</p>
<p><i>Deputy Solicitor General Randolph</i> argued the cause for the United States as <i>amicus curiae</i> urging affirmance. On the brief were <i>Solicitor General Bork, Deputy Solicitor</i> <span class="star-pagination">*465</span> <i>General Frey, Stuart A. Smith,</i> and <i>Edward R. Korman.</i></p>
<p>MR. JUSTICE BLACKMUN delivered the opinion of the Court.</p>
<p>This case presents the issue whether the introduction into evidence of a person's business records, seized during a search of his offices, violates the Fifth Amendment's command that "[n]o person . . . shall be compelled in any criminal case to be a witness against himself." We also must determine whether the particular searches and seizures here were "unreasonable" and thus violated the prohibition of the Fourth Amendment.</p>
<p></p>
<h2>I</h2>
<p>In early 1972, a Bi-County Fraud Unit, acting under the joint auspices of the State's Attorneys' Offices of Montgomery and Prince George's Counties, Md., began an investigation of real estate settlement activities in the Washington, D. C., area. At the time, petitioner Andresen was an attorney who, as a sole practitioner, specialized in real estate settlements in Montgomery County. During the Fraud Unit's investigation, his activities came under scrutiny, particularly in connection with a transaction involving Lot 13T in the Potomac Woods subdivision of Montgomery County. The investigation, which included interviews with the purchaser, the mortgage holder, and other lienholders of Lot 13T, as well as an examination of county land records, disclosed that petitioner, acting as settlement attorney, had defrauded Standard-Young Associates, the purchaser of Lot 13T. Petitioner had represented that the property was free of liens and that, accordingly, no title insurance was necessary, when in fact, he knew that there were two outstanding liens on the property. In addition, investigators <span class="star-pagination">*466</span> learned that the lienholders, by threatening to foreclose their liens, had forced a halt to the purchaser's construction on the property. When Standard-Young had confronted petitioner with this information, he responded by issuing, as an agent of a title insurance company, a title policy guaranteeing clear title to the property. By this action, petitioner also defrauded that insurance company by requiring it to pay the outstanding liens.</p>
<p>The investigators, concluding that there was probable cause to believe that petitioner had committed the state crime of false pretenses, see Md. Ann. Code, Art. 27, § 140 (1976), against Standard-Young, applied for warrants to search petitioner's law office and the separate office of Mount Vernon Development Corporation, of which petitioner was incorporator, sole shareholder, resident agent, and director. The application sought permission to search for specified documents pertaining to the sale and conveyance of Lot 13T. A judge of the Sixth Judicial Circuit of Montgomery County concluded that there was probable cause and issued the warrants.</p>
<p>The searches of the two offices were conducted simultaneously during daylight hours on October 31, 1972.<sup>[1]</sup> Petitioner was present during the search of his law office and was free to move about. Counsel for him was present during the latter half of the search. Between 2% and 3% of the files in the office were seized. A single investigator, in the presence of a police officer, conducted <span class="star-pagination">*467</span> the search of Mount Vernon Development Corporation. This search, taking about four hours, resulted in the seizure of less than 5% of the corporation's files.</p>
<p>Petitioner eventually was charged, partly by information and partly by indictment, with the crime of false pretenses, based on his misrepresentation to Standard-Young concerning Lot 13T, and with fraudulent misappropriation by a fiduciary, based on similar false claims made to three home purchasers. Before trial began, petitioner moved to suppress the seized documents. The trial court held a full suppression hearing. At the hearing, the State returned to petitioner 45 of the 52 items taken from the offices of the corporation. The trial court suppressed six other corporation items on the ground that there was no connection between them and the crimes charged. The net result was that the only item seized from the corporation's offices that was not returned by the State or suppressed was a single file labeled "Potomac Woods General." In addition, the State returned to petitioner seven of the 28 items seized from his law office, and the trial court suppressed four other law office items based on its determination that there was no connection between them and the crime charged.</p>
<p>With respect to all the items not suppressed or returned, the trial court ruled that admitting them into evidence would not violate the Fifth and Fourth Amendments. It reasoned that the searches and seizures did not force petitioner to be a witness against himself because he had not been required to produce the seized documents, nor would he be compelled to authenticate them. Moreover, the search warrants were based on probable cause, and the documents not returned or suppressed were either directly related to Lot 13T, and therefore within the express language of the warrants, or properly seized and otherwise admissible to show a pattern of <span class="star-pagination">*468</span> criminal conduct relevant to the charge concerning Lot 13T.</p>
<p>At trial, the State proved its case primarily by public land records and by records provided by the complaining purchasers, lienholders, and the title insurance company. It did introduce into evidence, however, a number of the seized items. Three documents from the "Potomac Woods General" file, seized during the search of petitioner's corporation, were admitted. These were notes in the handwriting of an employee who used them to prepare abstracts in the course of his duties as a title searcher and law clerk. The notes concerned deeds of trust affecting the Potomac Woods subdivision and related to the transaction involving Lot 13T.<sup>[2]</sup> Five items seized from petitioner's law office were also admitted. One contained information relating to the transactions with one of the defrauded home buyers. The second was a file partially devoted to the Lot 13T transaction; among the documents were settlement statements, the deed conveying the property to Standard-Young Associates, and the original and a copy of a notice to the buyer about releases of liens. The third item was a file devoted exclusively to Lot 13T. The fourth item consisted of a copy of a deed of trust, dated March 27, 1972, from the seller of certain lots in the Potomac Woods subdivision to a lienholder.<sup>[3]</sup> The fifth item contained drafts of <span class="star-pagination">*469</span> documents and memoranda written in petitioner's handwriting.</p>
<p>After a trial by jury, petitioner was found guilty upon five counts of false pretenses and three counts of fraudulent misappropriation by a fiduciary. He was sentenced to eight concurrent two-year prison terms.</p>
<p>On appeal to the Court of Special Appeals of Maryland, four of the five false-pretenses counts were reversed because the indictment had failed to allege intent to defraud, a necessary element of the state offense. Only the count pertaining to Standard-Young's purchase of Lot 13T remained. With respect to this count of false pretenses and the three counts of misappropriation by a fiduciary, the Court of Special Appeals rejected petitioner's Fourth and Fifth Amendment Claims.<sup>[4]</sup> Specifically, it held that the warrants were supported by probable cause, that they did not authorize a general search in violation of the Fourth Amendment, and that the items admitted into evidence against petitioner at trial were within the scope of the warrants or were otherwise properly seized. It agreed with the trial court that the search had not violated petitioner's Fifth Amendment rights because petitioner had not been compelled to do anything. <span class="citation" data-id="1480134"><a href="/opinion/1480134/andresen-v-state/" aria-description="Citation for case: Andresen v. State">24 Md. App. 128</a></span>, <span class="citation" data-id="1480134"><a href="/opinion/1480134/andresen-v-state/" aria-description="Citation for case: Andresen v. State">331 A. 2d 78</a></span> (1975).</p>
<p><span class="star-pagination">*470</span> We granted certiorari limited to the Fourth and Fifth Amendment issues. <span class="citation multiple-matches"><a href="/c/U.%20S./423/822/">423 U. S. 822</a></span> (1975).<sup>[5]</sup></p>
<p></p>
<h2>II</h2>
<p>The Fifth Amendment, made applicable to the States by the Fourteenth Amendment, <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#8" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 8</a></span> (1964), provides that "[n]o person . . . shall be compelled in any criminal case to be a witness against himself." As the Court often has noted, the development of this protection was in part a response to certain historical practices, such as ecclesiastical inquisitions and the proceedings of the Star Chamber, "which placed a premium on compelling subjects of the investigation to admit guilt from their own lips." <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#440" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 440</a></span> (1974). See generally L. Levy, Origins of the Fifth Amendment (1968). The "historic function" of the privilege has been to protect a " `natural individual from compulsory incrimination through his <span class="star-pagination">*471</span> own testimony or personal records.' " <i>Bellis</i> v. <i>United States,</i> <span class="citation" data-id="9425735"><a href="/opinion/109046/bellis-v-united-states/#89" aria-description="Citation for case: Bellis v. United States">417 U. S. 85, 89-90</a></span> (1974), quoting from <i>United States</i> v. <i>White,</i> <span class="citation" data-id="104016"><a href="/opinion/104016/united-states-v-white/#701" aria-description="Citation for case: United States v. White">322 U. S. 694, 701</a></span> (1944).</p>
<p>There is no question that the records seized from petitioner's offices and introduced against him were incriminating. Moreover, it is undisputed that some of these business records contain statements made by petitioner. Cf. <i>United States</i> v. <i>Mara,</i> <span class="citation" data-id="9425147"><a href="/opinion/108710/united-states-v-mara/#21" aria-description="Citation for case: United States v. Mara">410 U. S. 19, 21-22</a></span> (1973); <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1</a></span> (1973); <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#266" aria-description="Citation for case: Gilbert v. California">388 U. S. 263, 266-267</a></span> (1967); <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967); and <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966). The question, therefore, is whether the seizure of these business records, and their admission into evidence at his trial, compelled petitioner to testify against himself in violation of the Fifth Amendment. This question may be said to have been reserved in <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#302" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 302-303</a></span> (1967), and it was adverted to in <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">425 U. S. 435</a></span>, 441 n. 3 (1976).</p>
<p>Petitioner contends that "the Fifth Amendment prohibition against compulsory self-incrimination applies as well to personal business papers seized from his offices as it does to the same papers being required to be produced under a subpoena." Brief for Petitioner 9. He bases his argument, naturally, on dicta in a number of cases which imply, or state, that the search for and seizure of a person's private papers violate the privilege against self-incrimination. Thus, in <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#633" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 633</a></span> (1886), the Court said: "[W]e have been unable to perceive that the seizure of a man's private books and papers to be used in evidence against him is substantially different from compelling him to be a witness against himself." And in <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#76" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 76</a></span> (1906), it was observed that "the substance of the offense is the compulsory production of private <span class="star-pagination">*472</span> papers, whether under a search warrant or a <i>subpoena duces tecum,</i> against which the person . . . is entitled to protection."</p>
<p>We do not agree, however, that these broad statements compel suppression of this petitioner's business records as a violation of the Fifth Amendment. In the very recent case of <i>Fisher</i> v. <i>United States,</i> <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/" aria-description="Citation for case: Fisher v. United States">425 U. S. 391</a></span> (1976), the Court held that an attorney's production, pursuant to a lawful summons, of his client's tax records in his hands did not violate the Fifth Amendment privilege of the taxpayer "because enforcement against a taxpayer's lawyer would not `compel' the taxpayer to do anythingand certainly would not compel him to be a `witness' against himself." <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/#397" aria-description="Citation for case: Fisher v. United States"><i>Id.,</i> at 397</a></span>. We recognized that the continued validity of the broad statements contained in some of the Court's earlier cases had been discredited by later opinions. <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/#407" aria-description="Citation for case: Fisher v. United States"><i>Id.,</i> at 407-409</a></span>. In those earlier cases, the legal predicate for the inadmissibility of the evidence seized was a violation of the Fourth Amendment; the unlawfulness of the search and seizure was thought to supply the compulsion of the accused necessary to invoke the Fifth Amendment.<sup>[6]</sup> Compulsion of the accused was also absent in <i>Couch</i> v. <i>United States,</i> <span class="star-pagination">*473</span> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">409 U. S. 322</a></span> (1973), where the Court held that a summons served on a taxpayer's accountant requiring him to produce the taxpayer's personal business records in his possession did not violate the taxpayer's Fifth Amendment rights.<sup>[7]</sup></p>
<p>Similarly, in this case, petitioner was not asked to say or to do anything. The records seized contained statements that petitioner had voluntarily committed to writing. The search for and seizure of these records were conducted by law enforcement personnel. Finally, when these records were introduced at trial, they were authenticated by a handwriting expert, not by petitioner. Any compulsion of petitioner to speak, other than the inherent psychological pressure to respond at trial to unfavorable evidence, was not present.</p>
<p>This case thus falls within the principle stated by Mr. Justice Holmes: "A party is privileged from producing the evidence but not from its production." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="97862"><a href="/opinion/97862/johnson-v-united-states/#458" aria-description="Citation for case: Johnson v. United States">228 U. S. 457, 458</a></span> (1913). This principle recognizes that the protection afforded by the Self-Incrimination Clause of the Fifth Amendment "adheres basically to the person, not to information that may incriminate him." <i>Couch</i> v. <i>United States,</i> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#328" aria-description="Citation for case: Couch v. United States">409 U. S., at 328</a></span>. Thus, although the Fifth Amendment may protect an individual from complying with a subpoena for the <span class="star-pagination">*474</span> production of his personal records in his possession because the very act of production may constitute a compulsory authentication of incriminating information, see <i>Fisher</i> v. <i>United States, supra</i><i>,</i> a seizure of the same materials by law enforcement officers differs in a crucial respectthe individual against whom the search is directed is not required to aid in the discovery, production, or authentication of incriminating evidence.</p>
<p>A contrary determination that the seizure of a person's business records and their introduction into evidence at a criminal trial violates the Fifth Amendment, would undermine the principles announced in earlier cases. Nearly a half century ago, in <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span> (1927), the Court upheld, against both Fourth and Fifth Amendment claims, the admission into evidence of business records seized during a search of the accused's illegal liquor business. And in <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span> (1960), the Court again upheld, against both Fourth and Fifth Amendment claims, the introduction into evidence at an espionage trial of false identity papers and a coded message seized during a search of the accused's hotel room. These cases recognize a general rule: "There is no special sanctity in papers, as distinguished from other forms of property, to render them immune from search and seizure, if only they fall within the scope of the principles of the cases in which other property may be seized, and if they be adequately described in the affidavit and warrant." <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#309" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 309</a></span> (1921).</p>
<p>Moreover, a contrary determination would prohibit the admission of evidence traditionally used in criminal cases and traditionally admissible despite the Fifth Amendment. For example, it would bar the admission of an accused's gambling records in a prosecution for <span class="star-pagination">*475</span> gambling; a note given temporarily to a bank teller during a robbery and subsequently seized in the accused's automobile or home in a prosecution for bank robbery; and incriminating notes prepared, but not sent, by an accused in a kidnaping or blackmail prosecution.</p>
<p>We find a useful analogy to the Fifth Amendment question in those cases that deal with the "seizure" of oral communications. As the Court has explained, " `[t]he constitutional privilege against self-incrimination. . . is designed to prevent the use of legal process to force from the lips of the accused individual the evidence necessary to convict him or to force him to produce and authenticate any personal documents or effects that might incriminate him.' " <i>Bellis</i> v. <i>United States,</i> <span class="citation" data-id="9425735"><a href="/opinion/109046/bellis-v-united-states/#88" aria-description="Citation for case: Bellis v. United States">417 U. S., at 88</a></span>, quoting <i>United States</i> v. <i>White,</i> <span class="citation" data-id="104016"><a href="/opinion/104016/united-states-v-white/#698" aria-description="Citation for case: United States v. White">322 U. S., at 698</a></span>. The significant aspect of this principle was apparent and applied in <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293</a></span> (1966), where the Court rejected the contention that an informant's "seizure" of the accused's conversation with him, and his subsequent testimony at trial concerning that conversation, violated the Fifth Amendment. The rationale was that, although the accused's statements may have been elicited by the informant for the purpose of gathering evidence against him, they were made voluntarily. We see no reasoned distinction to be made between the compulsion upon the accused in that case and the compulsion in this one. In each, the communication, whether oral or written, was made voluntarily. The fact that seizure was contemporaneous with the communication in <i><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">Hoffa</a></span></i> but subsequent to the communication here does not affect the question whether the accused was compelled to speak.</p>
<p>Finally, we do not believe that permitting the introduction into evidence of a person's business records seized during an otherwise lawful search would offend or undermine <span class="star-pagination">*476</span> any of the policies undergirding the privilege. <i>Murphy</i> v. <i>Waterfront Comm'n,</i> <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#55" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 55</a></span> (1964).<sup>[8]</sup></p>
<p>In this case, petitioner, at the time he recorded his communication, at the time of the search, and at the time the records were admitted at trial, was not subjected to "the cruel trilemma of self-accusation, perjury or contempt." <i><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">Ibid.</a></span></i> Indeed, he was never required to say or to do anything under penalty of sanction. Similarly, permitting the admission of the records in question does not convert our accusatorial system of justice into an inquisitorial system. "The requirement of specific charges, their proof beyond a reasonable doubt, the protection of the accused from confessions extorted through whatever form of police pressures, the right to a prompt hearing before a magistrate, the right to assistance of counsel, to be supplied by government when circumstances make it necessary, the duty to advise an accused of his constitutional rightsthese are all characteristics of the accusatorial system and manifestations of its demands." <i>Watts</i> v. <i>Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#54" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 54</a></span> (1949). None of these <span class="star-pagination">*477</span> attributes is endangered by the introduction of business records "independently secured through skillful investigation." <i><span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/" aria-description="Citation for case: Watts v. Indiana">Ibid.</a></span></i> Further, the search for and seizure of business records pose no danger greater than that inherent in every search that evidence will be "elicited by inhumane treatment and abuses." 378 U. S., at 55. In this case, the statements seized were voluntarily committed to paper before the police arrived to search for them, and petitioner was not treated discourteously during the search. Also, the "good cause" to "disturb," <i>ibid.,</i> petitioner was independently determined by the judge who issued the warrants; and the State bore the burden of executing them. Finally, there is no chance, in this case, of petitioner's statements being self-deprecatory and untrustworthy because they were extracted from himthey were already in existence and had been made voluntarily.</p>
<p>We recognize, of course, that the Fifth Amendment protects privacy to some extent. However, "the Court has never suggested that every invasion of privacy violates the privilege." <i>Fisher</i> v. <i>United States,</i> 425 U. S., at 399. Indeed, we recently held that unless incriminating testimony is "compelled," any invasion of privacy is outside the scope of the Fifth Amendment's protection, saying that "the Fifth Amendment protects against `compelled self-incrimination, not [the disclosure of] private information.' " <i>Id.,</i> at 401. Here, as we have already noted, petitioner was not compelled to testify in any manner.</p>
<p>Accordingly, we hold that the search of an individual's office for business records, their seizure, and subsequent introduction into evidence do not offend the Fifth Amendment's proscription that "[n]o person . . . shall be compelled in any criminal case to be a witness against himself."</p>
<p></p>
<h2>
<span class="star-pagination">*478</span> III</h2>
<p>We turn next to petitioner's contention that rights guaranteed him by the Fourth Amendment were violated because the descriptive terms of the search warrants were so broad as to make them impermissible "general" warrants, and because certain items were seized in violation of the principles of <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967).<sup>[9]</sup></p>
<p><span class="star-pagination">*479</span> <i>The specificity of the search warrants.</i> Although petitioner concedes that the warrants for the most part were models of particularity, Brief for Petitioner 28, he contends that they were rendered fatally "general" by the addition, in each warrant, to the exhaustive list of particularly described documents, of the phrase "together with other fruits, instrumentalities and evidence of crime at this [time] unknown." App. A. 95-A. 96, A. 115. The quoted language, it is argued, must be read in isolation and without reference to the rest of the long sentence at the end of which it appears. When <span class="star-pagination">*480</span> read "properly," petitioner contends, it permits the search for and seizure of any evidence of any crime.</p>
<p>General warrants, of course, are prohibited by the Fourth Amendment. "[T]he problem [posed by the general warrant] is not that of intrusion <i>per se,</i> but of a general, exploratory rummaging in a person's belongings. . . . [The Fourth Amendment addresses the problem] by requiring a `particular description' of the things to be seized." <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#467" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 467</a></span> (1971). This requirement " `makes general searches . . . impossible and prevents the seizure of one thing under a warrant describing another. As to what is to be taken, nothing is left to the discretion of the officer executing the warrant.' " <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 485</a></span> (1965), quoting <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U. S., at 196</a></span>.</p>
<p>In this case we agree with the determination of the Court of Special Appeals of Maryland that the challenged phrase must be read as authorizing only the search for and seizure of evidence relating to "the crime of false pretenses with respect to Lot 13T." <span class="citation" data-id="1480134"><a href="/opinion/1480134/andresen-v-state/#167" aria-description="Citation for case: Andresen v. State">24 Md. App., at 167</a></span>, <span class="citation" data-id="1480134"><a href="/opinion/1480134/andresen-v-state/#103" aria-description="Citation for case: Andresen v. State">331 A. 2d, at 103</a></span>. The challenged phrase is not a separate sentence. Instead, it appears in each warrant at the end of a sentence containing a lengthy list of specified and particular items to be seized, all pertaining to Lot 13T.<sup>[10]</sup> We think it clear from the context <span class="star-pagination">*481</span> that the term "crime" in the warrants refers only to the crime of false pretenses with respect to the sale of Lot 13T. The "other fruits" clause is one of a series that follows the colon after the word "Maryland." All clauses in the series are limited by what precedes that colon, namely, "items pertaining to . . . lot 13, block T." The warrants, accordingly, did not authorize the executing officers to conduct a search for evidence of <span class="star-pagination">*482</span> other crimes but only to search for and seize evidence relevant to the crime of false pretenses and Lot 13T.<sup>[11]</sup></p>
<p><i>The admissibility of certain items of evidence in light of </i><i>Warden v. Hayden</i><i>.</i> Petitioner charges that the seizure of documents pertaining to a lot other than Lot 13T violated the principles of <i>Warden</i> v. <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden</a></span></i> and therefore should have been suppressed. His objection appears to be that these papers were not relevant to the Lot 13T charge and were admissible only to prove another crime with which he was charged after the search. The fact that these documents were used to help form the evidentiary basis for another charge, it is argued, shows that the documents were seized solely for that purpose.</p>
<p>The State replies that <i>Warden</i> v. <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden</a></span></i> was not violated and that this is so because the challenged evidence is relevant to the question whether petitioner committed the crime of false pretenses with respect to Lot 13T. In Maryland, the crime is committed when a person <span class="star-pagination">*483</span> makes a false representation of a past or existing fact, with intent to defraud and knowledge of its falsity, and obtains any chattel, money, or valuable security from another, who relies on the false representation to his detriment. <i>Polisher</i> v. <i>State,</i> <span class="citation" data-id="1895902"><a href="/opinion/1895902/polisher-v-state/#560" aria-description="Citation for case: Polisher v. State">11 Md. App. 555, 560</a></span>, <span class="citation" data-id="1895902"><a href="/opinion/1895902/polisher-v-state/#104" aria-description="Citation for case: Polisher v. State">276 A. 2d 102, 104</a></span> (1971). Thus, the State is required to prove intent to defraud beyond a reasonable doubt. The State consequently argues that the documents pertaining to another lot in the Potomac Woods subdivision demonstrate that the misrepresentation with respect to Lot 13T was not the result of mistake on the part of petitioner.</p>
<p>In <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#307" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S., at 307</a></span>, the Court stated that when the police seize " `mere evidence,' probable cause must be examined in terms of cause to believe that the evidence sought will aid in a particular apprehension or conviction. In so doing, consideration of police purposes will be required." In this case, we conclude that the trained special investigators reasonably could have believed that the evidence specifically dealing with another lot in the Potomac Woods subdivision could be used to show petitioner's intent with respect to the Lot 13T transaction.</p>
<p>The Court has often recognized that proof of similar acts is admissible to show intent or the absence of mistake. In <i>Nye &amp; Nissen</i> v. <i>United States,</i> <span class="citation" data-id="9420303"><a href="/opinion/104655/nye-nissen-v-united-states/" aria-description="Citation for case: Nye &amp; Nissen v. United States">336 U. S. 613</a></span> (1949), for example, a case involving a scheme of fraudulent conduct, it was said:</p>
<blockquote>"The evidence showed the presentation of eleven other false invoices. . . . The trial court also admitted it at the conclusion of the case `for the sole purpose of proving guilty intent, motive, or guilty knowledge' of the defendants. Evidence that similar and related offenses were committed in this period tended to show a consistent pattern of conduct highly relevant to the issue of intent." <span class="citation" data-id="9420303"><a href="/opinion/104655/nye-nissen-v-united-states/#618" aria-description="Citation for case: Nye &amp; Nissen v. United States"><i>Id.,</i> at 618</a></span>.</blockquote>
<p><span class="star-pagination">*484</span> In the present case, when the special investigators secured the search warrants, they had been informed of a number of similar charges against petitioner arising out of Potomac Woods transactions. And, by reading numerous documents and records supplied by the Lot 13T and other complainants, and by interviewing witnesses, they had become familiar with petitioner's method of operation. Accordingly, the relevance of documents pertaining specifically to a lot other than Lot 13T, and their admissibility to show the Lot 13T offense, would have been apparent. Lot 13T and the other lot had numerous features in common. Both were in the same section of the Potomac Woods subdivision; both had been owned by the same person; and transactions concerning both had been handled extensively by petitioner. Most important was the fact that there were two deeds of trust in which both lots were listed as collateral. Unreleased liens respecting both lots were evidenced by these deeds of trusts. Petitioner's transactions relating to the other lot, subject to the same liens as Lot 13T, therefore, were highly relevant to the question whether his failure to deliver title to Lot 13T free of all encumbrances was mere inadvertence. Although these records subsequently were used to secure additional charges against petitioner, suppression of this evidence in this case was not required. The fact that the records could be used to show intent to defraud with respect to Lot 13T permitted the seizure and satisfied the requirements of <i>Warden</i> v. <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden</a></span></i><i>.</i></p>
<p>The judgment of the Court of Special Appeals of Maryland is affirmed.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE BRENNAN, dissenting.</p>
<p>In a concurring opinion earlier this Term in <i>Fisher</i> v. <i>United States,</i> <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/#414" aria-description="Citation for case: Fisher v. United States">425 U. S. 391, 414</a></span> (1976), I stated my view <span class="star-pagination">*485</span> that the Fifth Amendment protects an individual citizen against the compelled production of testimonial matter that might tend to incriminate him, provided it is matter that comes within the zone of privacy recognized by the Amendment to secure to the individual "a private inner sanctum of individual feeling and thought." <i>Couch</i> v. <i>United States,</i> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#327" aria-description="Citation for case: Couch v. United States">409 U. S. 322, 327</a></span> (1973). Accordingly, the production of testimonial material falling within this zone of privacy may not be compelled by subpoena. The Court holds today that the search and seizure, pursuant to a valid warrant, of business records in petitioner's possession and containing statements made by the petitioner does not violate the Fifth Amendment. I can perceive no distinction of meaningful substance between compelling the production of such records through subpoena and seizing such records against the will of the petitioner. Moreover, I believe that the warrants under which petitioner's papers were seized were impermissibly general. I therefore dissent.<sup>[1]</sup></p>
<p></p>
<h2>I</h2>
<p>"There is no question that the records seized from petitioner's offices and introduced against him were incriminating. Moreover, it is undisputed that some of these business records contain statements made by petitioner." <i>Ante,</i> at 471. It also cannot be questioned that these records fall within the zone of privacy protected by the Fifth Amendment. <i>Bellis</i> v. <i>United States,</i> <span class="citation" data-id="9425735"><a href="/opinion/109046/bellis-v-united-states/#87" aria-description="Citation for case: Bellis v. United States">417 U. S. 85, 87-88</a></span> (1974), squarely recognized that "[t]he privilege applies to the business records of the sole proprietor or sole practitioner <span class="star-pagination">*486</span> as well as to personal documents containing more intimate information about the individual's private life." The Court today retreats from this view. Though recognizing the value of privacy protected by the Fifth Amendment, see <i>ante,</i> at 477, and the " `right of each individual "to a private enclave where he may lead a private life," ' " <i>ante,</i> at 476 n. 8, the Court declines, without adequate explanation, to include business records within that private zone comprising the mere physical extensions of an individual's thoughts and knowledge. As I noted in <i><span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/" aria-description="Citation for case: Fisher v. United States">Fisher</a></span>,</i> the failure to give effect to such a zone ignores the essential spirit of the Fifth Amendment: "[Business] records are at least an extension of an aspect of a person's activities, though concededly not the more intimate aspects of one's life. Where the privilege would have protected one's mental notes of his business affairs in a less complicated day and age, it would seem that that protection should not fall away because the complexities of another time compel one to keep business records. Cf. <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#474" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 474</a></span> (1928) (Brandeis, J., dissenting)." 425 U. S., at 426-427 (BRENNAN, J., concurring in judgment).</p>
<p>As indicated at the outset, today's assault on the Fifth Amendment is not limited to narrowing this view of the scope of privacy respected by it. The Court also sanctions circumvention of the Amendment by indulging an unjustified distinction between production compelled by subpoena and production secured against the will of the petitioner through warrant. But a privilege protecting against the compelled production of testimonial material is a hollow guarantee where production of that material may be secured through the expedient of search and seizure.</p>
<p>The matter cannot be resolved on any simplistic notion of compulsion. Search and seizure is as rife with <span class="star-pagination">*487</span> elements of compulsion as subpoena. The intrusion occurs under the lawful process of the State. The individual is not free to resist that authority. To be sure, as the Court observes, "[p]etitioner was present during the search of his law office and was free to move about," <i>ante,</i> at 466, but I do not believe the Court means to suggest that petitioner was free to obstruct the investigators' search through his files.<sup>[2]</sup></p>
<p>And compulsion does not disappear merely because the individual is absent at the time of search and seizure. The door to one's house, for example, is as much the individual's resistance to the intrusion of outsiders as his personal physical efforts to prevent the same. To refuse recognition to the sanctity of that door and, more generally, to confine the dominion of privacy to the mind, compels an unconstitutional disclosure by denying to the individual a zone of physical freedom necessary for conducting one's affairs. True to this principle, a value enshrined by the Fifth Amendment, the Court carefully observed in <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span></i> that "actual possession of documents bears the most significant relationship to Fifth Amendment protections against governmental compulsions upon the individual accused of crime," <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#333" aria-description="Citation for case: Couch v. United States">409 U. S., at 333</a></span>, and that "[w]e do indeed attach constitutional importance to possession, but only because of its close relationship to those personal compulsions and intrusions which the Fifth Amendment forbids." <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Id.,</a></span></i> at 336 n. 20. <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span></i> also plainly indicated that it is not necessary that <span class="star-pagination">*488</span> there be actual possession in order to invoke Fifth Amendment limitations, for "situations may well arise where constructive possession is so clear or the relinquishment of possession is so temporary and insignificant as to leave the personal compulsions upon the accused substantially intact." <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#333" aria-description="Citation for case: Couch v. United States"><i>Id.,</i> at 333</a></span>.<sup>[3]</sup></p>
<p>Though the records involved in this case were clearly within petitioner's possession or at least constructive possession, the Court avoids application of these principles and the values they protect by what I submit is a mischaracterization of <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span></i> as concerned with the "possibility of compulsory self-incrimination by the principal's implicit or explicit `testimony' that the documents were those identified in the summons." <i>Ante,</i> at 473 n. 7. Whether or not <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span></i> was concerned with this possibility and I believe that even under the most strained reading it was not<span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States"><i>Couch</i></a></span> was clearly concerned with whether production of documents in the possession of the accused's accountant pursuant to a summons directed to the accountant operated personally to compel the accused. It was in this regard that <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span></i> recognized that "possession bears the closest relationship to the personal compulsion forbidden by the Fifth Amendment," <span class="star-pagination">*489</span> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#331" aria-description="Citation for case: Couch v. United States">409 U. S., at 331</a></span>, a matter with which the Court refuses to deal in its treatment of <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span>.</i></p>
<p><i>Couch</i> only reflects the view of a long line of decisions explicitly recognizing that the seizure of private papers may violate the Fifth Amendment. As early as <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#633" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 633</a></span> (1886), the Court was "unable to perceive that the seizure of a man's private books and papers to be used in evidence against him is substantially different from compelling him to be a witness against himself." Though the Court in <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> held that compelling a person to be a witness against himself was tantamount to an unreasonable search and seizure, it never required a search and seizure to be independently unreasonable in order that it violate the Fifth Amendment. And though the several decisions which have found a Fifth Amendment violation stemming from a search and seizure all involved unreasonable search and seizures, it has never been established, contrary to the Court's assertion, <i>ante,</i> at 472, that the unlawfulness of the search and seizure is necessary to invoke the Fifth Amendment. <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span> (1921), though also involving a Fourth Amendment violation, makes it clear that the illegality of the search and seizure is not a prerequisite for a Fifth Amendment violation. Under <i><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span>,</i> a Fifth Amendment violation exists because the "[accused] is the unwilling source of the evidence," <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#306" aria-description="Citation for case: Gouled v. United States"><i>id.,</i> at 306</a></span>, a matter which does not depend on the illegality <i>vel non</i> of the search and seizure.<sup>[4]</sup></p>
<p>Until today, no decision by this Court had held that the seizure of testimonial evidence by legal process did <span class="star-pagination">*490</span> not violate the Fifth Amendment. Indeed, with few exceptions,<sup>[5]</sup> the indications were strongly to the contrary. See, <i>e. g., </i><i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#465" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 465-467</a></span> (1932); <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#397" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 397</a></span> (1914); <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#76" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 76</a></span> (1906).<sup>[6]</sup> More <span class="star-pagination">*491</span> recently, <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#767" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 767</a></span> (1966), noted that the "values protected by the Fourth Amendment . . . substantially overlap those the Fifth Amendment helps to protect," and clearly indicated that in considering whether to suppress seized evidence, a first inquiry is whether its testimonial nature, if any, precludes its introduction in evidence. See <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#760" aria-description="Citation for case: Schmerber v. California"><i>id.,</i> at 760-765</a></span>. Subsequent to <i>Schmerber, Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#302" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 302-303</a></span> (1967), carefully observed that the items of clothing seized in that case were "not `testimonial' or `communicative' in nature, and their introduction therefore did not compel respondent to become a witness against himself in violation of the Fifth Amendment."<sup>[7]</sup> These cases all reflect the root understanding of <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S., at 630</a></span>: "It is not the breaking of his doors, and the rummaging of his drawers, that constitutes the essence of the offence [to the Fifth Amendment]; but it is the invasion of his indefeasible right of personal security, personal liberty <span class="star-pagination">*492</span> and private property . . . . [A]ny forcible and compulsory extortion of a man's own testimony or of his private papers to be used as evidence to convict him of crime . . . , is within the condemnation of [the Amendment]. In this regard the Fourth and Fifth Amendments run almost into each other."</p>
<p></p>
<h2>II</h2>
<p>Even if a Fifth Amendment violation is not to be recognized in the seizure of petitioner's papers, a violation of Fourth Amendment protections clearly should be, for the warrants under which those papers were seized were impermissibly general. General warrants are especially prohibited by the Fourth Amendment. The problem to be avoided is "not that of intrusion <i>per se,</i> but of a general, exploratory rummaging in a person's belongings." <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#467" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 467</a></span> (1971). Thus the requirement plainly appearing on the face of the Fourth Amendment that a warrant specify with particularity the place to be searched and the things to be seized is imposed to the end that "unauthorized invasions of `the sanctity of a man's home and the privacies of life' " be prevented. <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#58" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 58</a></span> (1967). " `As to what is to be taken, nothing is left to the discretion of the officer executing the warrant.' " <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 485</a></span> (1965) (quoting <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 196</a></span> (1927)).</p>
<p>The Court recites these requirements, but their application in this case renders their limitation on unlawful governmental conduct an empty promise. After a lengthy and admittedly detailed listing of items to be seized, the warrants in this case further authorized the seizure of "other fruits, instrumentalities and evidence of crime at this [time] unknown." App. A. 96, A. 115. The Court construes this sweeping authorization to be <span class="star-pagination">*493</span> limited to evidence pertaining to the crime of false pretenses with respect to the sale of Lot 13T. However, neither this Court's construction of the warrants nor the similar construction by the Court of Special Appeals of Maryland was available to the investigators at the time they executed the warrants. The question is not how those warrants are to be viewed in hindsight, but how they were in fact viewed by those executing them. The overwhelming quantity of seized material that was either suppressed or returned to petitioner is irrefutable testimony to the unlawful generality of the warrants.<sup>[8]</sup> The Court's attempt to cure this defect by <i>post hoc</i> judicial construction evades principles settled in this Court's Fourth Amendment decisions. "The scheme of the Fourth Amendment becomes meaningful only when it is assured that at some point the conduct of those charged with enforcing the laws can be subjected to the more detached, neutral scrutiny of a judge . . . ." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 21</a></span> (1968). See <i>Berger</i> v. <i>New York, supra,</i> at 54; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-14</a></span> (1948). It is not the function of a detached and neutral review to give effect to warrants whose terms unassailably authorize the far-reaching search and seizure of a person's papers, especially where that has in fact been the result of executing those warrants.</p>
<p>MR. JUSTICE MARSHALL, dissenting.</p>
<p>I agree with MR. JUSTICE BRENNAN that the business records introduced at petitioner's trial should have been suppressed because they were seized pursuant to a general warrant. Accordingly, I need not consider <span class="star-pagination">*494</span> whether petitioner's alternative contentionthat the Fifth Amendment precludes the seizure of private papers, even pursuant to a warrantcan survive <i>Fisher</i> v. <i>United States,</i> <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/" aria-description="Citation for case: Fisher v. United States">425 U. S. 391</a></span> (1976), and, if so, whether this Fifth Amendment argument would protect the business records seized in this case.</p>
<h2>NOTES</h2>
<p>[1]  Before these search warrants were executed, the Bi-County Fraud Unit had also received complaints concerning other Potomac Woods real estate transactions conducted by petitioner. The gist of the complaints was that petitioner, as settlement attorney, took money from three sets of home purchasers upon assurances that he would use it to procure titles to their properties free and clear of all encumbrances. It was charged that he had misappropriated the money so that they had not received clear title to the properties as promised.</p>
<p>[2]  It is established that the privilege against self-incrimination may not be invoked with respect to corporate records. <i>Bellis</i> v. <i>United States,</i> <span class="citation" data-id="9425735"><a href="/opinion/109046/bellis-v-united-states/#88" aria-description="Citation for case: Bellis v. United States">417 U. S. 85, 88-89</a></span> (1974); <i>Grant</i> v. <i>United States,</i> <span class="citation" data-id="97758"><a href="/opinion/97758/grant-v-united-states/" aria-description="Citation for case: Grant v. United States">227 U. S. 74</a></span> (1913); <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#70" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 70</a></span> (1906). It appears, however, that the records seized at the corporation's office were really not corporate records, but were records generated by petitioner's practice as a real estate lawyer. United States Appendix of Exhibits 1-3.</p>
<p>[3]  This item was introduced as proof that petitioner failed to pay recording taxes, a charge that was abandoned before the case was submitted to the jury.</p>
<p>[4]  The Solicitor General, in an <i>amicus</i> brief filed with this Court, has suggested that the evidence forming the basis of two of the counts of misappropriation by a fiduciary, which were upheld on appeal, was obtained entirely from sources other than petitioner's offices. Brief for United States as <i>Amicus Curiae</i> 12-14, 24-25, n. 17. This fact, if true, does not, of course, affect our jurisdiction but it would permit us to apply the discretionary concurrent-sentence doctrine, <i>Benton</i> v. <i>Maryland,</i> <span class="citation" data-id="9424099"><a href="/opinion/107980/benton-v-maryland/#791" aria-description="Citation for case: Benton v. Maryland">395 U. S. 784, 791</a></span> (1969), and thereby decline to consider petitioner's constitutional claims. <i>Barnes</i> v. <i>United States,</i> <span class="citation" data-id="9425368"><a href="/opinion/108830/barnes-v-united-states/" aria-description="Citation for case: Barnes v. United States">412 U. S. 837</a></span>, 848 n. 16 (1973).</p>
<p>[5]  Both the trial and appellate courts in this case recognized the conflict among the Federal Courts of Appeals over whether documentary evidence not obtainable by means of a subpoena or a summons may be obtained by means of a search warrant. Thus, in <i>Hill</i> v. <i>Philpott,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/445/144/">445 F. 2d 144</a></span> (CA7), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./404/991/">404 U. S. 991</a></span> (1971), the Court of Appeals held that evidence not obtainable by means of a subpoena could not be seized by means of a search warrant. The substantial majority position is of the opposite view. <i>Shaffer</i> v. <i>Wilson,</i> <span class="citation" data-id="9462146"><a href="/opinion/330234/wendell-l-shaffer-and-marjorie-m-shaffer-v-robert-c-wilson-special/" aria-description="Citation for case: Wendell L. Shaffer and Marjorie M. Shaffer v. Robert C....">523 F. 2d 175</a></span> (CA10 1975), cert. pending, No. 75-601; <i>United States</i> v. <i>Murray,</i> <span class="citation" data-id="8892672"><a href="/opinion/8905447/united-states-v-murray/#191" aria-description="Citation for case: United States v. Murray">492 F. 2d 178, 191</a></span> (CA9 1973); <i>Taylor</i> v. <i>Minnesota,</i> <span class="citation" data-id="305642"><a href="/opinion/305642/robert-muller-taylor-v-state-of-minnesota/" aria-description="Citation for case: Robert Muller Taylor v. State of Minnesota">466 F. 2d 1119</a></span> (CA8 1972), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./410/956/">410 U. S. 956</a></span> (1973); <i>United States</i> v. <i>Blank,</i> <span class="citation" data-id="303166"><a href="/opinion/303166/united-states-v-john-blank/" aria-description="Citation for case: United States v. John Blank">459 F. 2d 383</a></span> (CA6), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./409/887/">409 U. S. 887</a></span> (1972); <i>United States</i> v. <i>Scharfman,</i> <span class="citation" data-id="299281"><a href="/opinion/299281/united-states-v-max-scharfman/" aria-description="Citation for case: United States v. Max Scharfman">448 F. 2d 1352</a></span> (CA2 1971), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./405/919/">405 U. S. 919</a></span> (1972); <i>United States</i> v. <i>Bennett,</i> <span class="citation" data-id="284440"><a href="/opinion/284440/united-states-v-charles-t-bennett-wilbert-haywood-elmer-jessup-henry/#896" aria-description="Citation for case: United States v. Charles T. Bennett, Wilbert Haywood,...">409 F. 2d 888, 896</a></span> (CA2), cert. denied <i>sub nom. </i><i>Jessup</i> v. <i>United States,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./396/852/">396 U. S. 852</a></span> (1969). The majority position accords with the views of Wigmore. 8 J. Wigmore, Evidence § 2264, p. 380 (McNaughton Rev. 1961).
</p>
<p>The Court of Special Appeals adopted the majority position and, therefore, upheld the admission of the records into evidence.</p>
<p>[6]  In <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886), for example, it was held that the Government could not, consistently with the Fourth Amendment, obtain "mere evidence" from the accused; accordingly, a subpoena seeking "mere evidence" constituted compulsion of the accused against which he could invoke the Fifth Amendment. The "mere evidence" rule was overturned in <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#301" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 301-302</a></span> (1967).
</p>
<p>The "convergence theory" of the Fourth and Fifth Amendments is also illustrated by <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span> (1925), where the seizure of contraband pursuant to a search not incident to arrest and otherwise unlawful in violation of the Fourth Amendment was held to permit the accused to invoke the Fifth Amendment when the Government sought to introduce this evidence in a criminal proceeding against him.</p>
<p>[7]  Petitioner relies on the statement in <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span></i> that "possession bears the closest relationship to the personal compulsion forbidden by the Fifth Amendment," <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#331" aria-description="Citation for case: Couch v. United States">409 U. S., at 331</a></span>, in support of his argument that possession of incriminating evidence itself supplies the predicate for invocation of the privilege. <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span>,</i> of course, was concerned with the production of documents pursuant to a summons directed to the accountant where there might have been a possibility of compulsory self-incrimination by the principal's implicit or explicit "testimony" that the documents were those identified in the summons. The risk of authentication is not present where the documents are seized pursuant to a search warrant.</p>
<p>[8]  "The privilege against self-incrimination . . . reflects many of our fundamental values and most noble aspirations: our unwillingness to subject those suspected of crime to the cruel trilemma of self-accusation, perjury or contempt; our preference for an accusatorial rather than an inquisitorial system of criminal justice; our fear that self-incriminating statements will be elicited by inhumane treatment and abuses; our sense of fair play which dictates `a fair state-individual balance by requiring the government to leave the individual alone until good cause is shown for disturbing him and by requiring the government in its contest with the individual to shoulder the entire load' . . . ; our respect for the inviolability of the human personality and of the right of each individual `to a private enclave where he may lead a private life' . . . ; our distrust of self-deprecatory statements; and our realization that the privilege, while sometimes `a shelter to the guilty,' is often `a protection to the innocent.' "</p>
<p>[9]  Petitioner also contends that the affidavits do not establish probable cause and that the failure of the State formally to introduce the warrants into evidence violated his constitutional rights. These contentions may be disposed of summarily.
</p>
<p>The bases of petitioner's argument that the affidavits failed to establish probable cause are two: The affidavits, in violation of <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), did not establish the reliability of the information or the credibility of the informants; and the information on which they were based was so stale that there was no reason to believe that the documents sought were still in petitioner's possession.</p>
<p>The affidavits clearly establish the reliability of the information related and the credibility of its sources. The complainants are named, their positions are described, and their transactions with petitioner are related in a comprehensive fashion. In addition, the special-agent affiants aver that they have verified, at least in part, the complainants' charges by examining their correspondence with petitioner, numerous documents reflecting the transactions, and public land records. Copies of many of these records and documents are attached to the affidavits; others are described in detail. Finally, the agents aver that they have interviewed, with positive results, other persons involved in the real estate transactions that were the object of the investigation. Rarely have we seen warrant-supporting affidavits so complete and so thorough. Petitioner's probable-cause argument is without merit. See <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102</a></span> (1965).</p>
<p>It is also argued that there was a three-month delay between the completion of the transactions on which the warrants were based, and the ensuing searches, and that this time lapse precluded a determination that there was probable cause to believe that petitioner's offices contained evidence of the crime. This contention is belied by the particular facts of the case. The business records sought were prepared in the ordinary course of petitioner's business in his law office or that of his real estate corporation. It is eminently reasonable to expect that such records would be maintained in those offices for a period of time and surely as long as the three months required for the investigation of a complex real estate scheme. In addition, special investigators knew that petitioner had secured a release on Lot 13T with respect to one lienholder only three weeks before the searches and that another lien remained to be released. All this, when considered with other information demonstrating that Potomac Woods was still a current concern of petitioner, amply supports the belief that petitioner retained the sought-for records.</p>
<p>The final contention is that under <i>Bumper</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543</a></span>, 550 n. 15 (1968), the failure of the prosecution formally to introduce the warrants into evidence precludes the State from relying upon them to justify the searches. We reject the argument for two reasons. First, it appears that petitioner based this claim of error solely on state grounds in the Court of Special Appeals. Second, even if the claim is properly before us, it fails. Both the State and the petitioner referred to and extensively discussed the language and terms of the warrants during the suppression hearing, and the trial judge, in deciding the motion to suppress, made numerous references to the warrants. The present case, therefore, is a far cry from <i><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">Bumper</a></span></i> where the prosecution's assertion that it had a search warrant was made for the first time during oral argument before this Court. There is nothing in the Fourth Amendment that requires us so to exalt formalism over substance.</p>
<p>[10]  "[T]he following items pertaining to sale, purchase, settlement and conveyance of lot 13, block T, Potomac Woods subdivision, Montgomery County, Maryland:
</p>
<p>"title notes, title abstracts, title rundowns; contracts of sale and/or assignments from Raffaele Antonelli and Rocco Caniglia to Mount Vernon Development Corporation and/or others; lien payoff correspondence and lien pay-off memoranda to and from lienholders and noteholders; correspondence and memoranda to and from trustees of deeds of trust; lenders instructions for a construction loan or construction and permanent loan; disbursement sheets and disbursement memoranda; checks, check stubs and ledger sheets indicating disbursement upon settlement; correspondence and memoranda concerning disbursements upon settlement; settlement statements and settlement memoranda; fully or partially prepared deed of trust releases, whether or not executed and whether or not recorded; books, records, documents, papers, memoranda and correspondence, showing or tending to show a fraudulent intent, and/or knowledge as elements of the crime of false pretenses, in violation of Article 27, Section 140, of the Annotated Code of Maryland, 1957 Edition, as amended and revised, together with other fruits, instrumentalities and evidence of crime at this [time] unknown." App. A. 95-A. 96, A. 115.</p>
<p>Petitioner also suggests that the specific list of the documents to be seized constitutes a "general" warrant. We disagree. Under investigation was a complex real estate scheme whose existence could be proved only by piecing together many bits of evidence. Like a jigsaw puzzle, the whole "picture" of petitioner's false-pretense scheme with respect to Lot 13T could be shown only by placing in the proper place the many pieces of evidence that, taken singly, would show comparatively little. The complexity of an illegal scheme may not be used as a shield to avoid detection when the State has demonstrated probable cause to believe that a crime has been committed and probable cause to believe that evidence of this crime is in the suspect's possession. The specificity with which the documents are named here contrasts sharply with the absence of particularity in <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#58" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 58-59</a></span> (1967), where a state eavesdropping statute which authorized eavesdropping "without requiring belief that any particular offense has been or is being committed; nor that the `property' sought, the conversations, be particularly described," was invalidated.</p>
<p>[11]  The record discloses that the officials executing the warrants seized numerous papers that were not introduced into evidence. Although we are not informed of their content, we observe that to the extent such papers were not within the scope of the warrants or were otherwise improperly seized, the State was correct in returning them voluntarily and the trial judge was correct in suppressing others.
</p>
<p>We recognize that there are grave dangers inherent in executing a warrant authorizing a search and seizure of a person's papers that are not necessarily present in executing a warrant to search for physical objects whose relevance is more easily ascertainable. In searches for papers, it is certain that some innocuous documents will be examined, at least cursorily, in order to determine whether they are, in fact, among those papers authorized to be seized. Similar dangers, of course, are present in executing a warrant for the "seizure" of telephone conversations. In both kinds of searches, responsible officials, including judicial officials, must take care to assure that they are conducted in a manner that minimizes unwarranted intrusions upon privacy.</p>
<p>[1]  Today's decision is doubtless consistent with the recent trend of decisions to eviscerate Fourth Amendment protections. See, <i>e. g., </i><i>Texas</i> v. <i>White,</i> <span class="citation" data-id="9426226"><a href="/opinion/109332/texas-v-white/" aria-description="Citation for case: Texas v. White">423 U. S. 67</a></span> (1975); <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">425 U. S. 435</a></span> (1976); <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976); <i>United States</i> v. <i>Santana, ante,</i> p. 38.</p>
<p>[2]  There is no meaningful distinction between requiring petitioner in this case to stand idly by while papers are extracted from his files and requiring the petitioner in <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966), similarly to submit to the extraction of blood from his body. In either case, seizure is obtained by compulsion, yet in <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>,</i> unlike here, Fifth Amendment limitations were recognized as applicable.</p>
<p>[3]  Similarly, I recognized writing separately in <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span>:</i>
</p>
<p>"[S]urely the availability of the Fifth Amendment privilege cannot depend on whether or not the owner of the documents is compelled personally to turn the documents over to the Government. If private, testimonial documents held in the owner's own possession are privileged under the Fifth Amendment, then the Government cannot nullify that privilege by finding a way to obtain the documents without requiring the owner to take them in hand and personally present them to the Government agents. Where the Government takes private records from, for example, a safety deposit box against the will of the owner of the documents, the owner has been compelled, in my view, to incriminate himself within the meaning of the Fifth Amendment." <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">409 U. S., at 337</a></span> n. (concurring).</p>
<p>[4]  As the Court notes, <i>ante,</i> at 474, <i><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span></i> also observed that there is no special sanctity in papers rendering them immune from search and seizure. <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#309" aria-description="Citation for case: Gouled v. United States">255 U. S., at 309</a></span>. The observation, however, was hedged with qualifications, see <i>ibid.,</i> and <i><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span></i> itself makes clear that this was only a general proposition inapplicable in the case of private papers. See <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#306" aria-description="Citation for case: Gouled v. United States"><i>id.,</i> at 306</a></span>.</p>
<p>[5]  The Court cites <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span> (1927), as one exception, that decision having permitted the seizure of business records during the search of an illegal liquor business. <i><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">Marron</a></span>,</i> however, provides little, if any, foundation for the Court's view. Though erring in the light of subsequent cases, the Court there did not view the business records as private papers or testimonial evidence. Rather, the records were viewed merely as "a part of the outfit or equipment actually used to commit the offense." <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#199" aria-description="Citation for case: Marron v. United States"><i>Id.,</i> at 199</a></span>. Moreover, the aspect of <i><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">Marron</a></span></i> upon which the Court relies was clearly overruled in <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452</a></span> (1932)the ostensible effort in <i><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">Lefkowitz</a></span></i> to distinguish it from <i><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">Marron</a></span></i> notwithstanding.
</p>
<p>The Court also cites <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span> (1960), as supporting its position that private testimonial papers may be seized without violating the Fifth Amendment. The papers seized in that case, however, even if fairly characterizable as private and testimoniala matter about which I have doubtwere not admitted for the purpose of utilizing their testimonial contents as evidence.</p>
<p>Finally, this Court's wiretapping cases also lend little support to the Court's position. Two of those cases expressly recognized the danger to Fifth Amendment rights posed by wiretapping. See <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#56" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 56, 62</a></span> (1967); <i>Osborn</i> v. <i>United States,</i> <span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/" aria-description="Citation for case: Osborn v. United States">385 U. S. 323</a></span>, 329 n. 7 (1966). All cases permitting seizure have involved conversations between two or more parties under other than what could be considered confidential circumstances. Grave questions would be raised, however, where conversations are seized from the privacy of the home or where the conversations are between parties who speak at other than arm's length. In such circumstances there is danger that the zone of privacy recognized by the Fifth Amendment will have been invaded. See <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#471" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 471-479</a></span> (1928) (Brandeis, J., dissenting).</p>
<p>[6]  Though one component of the rationale in these cases precluding the seizure of papers appears to be the "mere evidence" rule, which was repudiated in <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967), they also view such seizures as tantamount to the compulsion of testimony, an unlawful act conceptually distinct from the once unlawful act of seizing mere evidence. <i>United States</i> v. <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#466" aria-description="Citation for case: United States v. Lefkowitz"><i>Lefkowitz, supra,</i> at 466-467</a></span>, for example, reiterates <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i>'s condemnation of the <i>compulsory</i> extraction of a man's private papers. Similarly, <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#397" aria-description="Citation for case: Weeks v. United States">232 U. S., at 397</a></span>, recognized that the seizure of a man's papers was an offense because it constituted the <i>compulsory</i> production of private papers. Accordingly, the doctrinal demise of the "mere evidence" rule left untouched the principles of these cases respecting the Fifth Amendment. See <i>Fisher</i> v. <i>United States,</i> <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/#420" aria-description="Citation for case: Fisher v. United States">425 U. S. 391, 420-422, n. 5</a></span> (1976) (BRENNAN, J., concurring in judgment).</p>
<p>[7]  By further observing that "[t]his case thus does not require that we consider whether there are items of evidential value whose very nature precludes them from being the object of a reasonable search and seizure," <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#303" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S., at 303</a></span>, <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden</a></span>,</i> at the very least, clearly left open the question whether lawful seizure of testimonial evidence violated the Fifth Amendment.</p>
<p>[8]  Testimony by investigators at the suppression hearing requested by the petitioner indicates that seizure of many of his papers occurred indiscriminately. See App. A. 155, A. 156.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Arizona v. Evans.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Arizona v. Evans"
type: case
citation: "514 U.S. 1 (1995)"
parallel_cite: "115 S. Ct. 1185; 131 L. Ed. 2d 34"
neutral_cite: 1995 U.S. LEXIS 1806
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1995
date_decided: 1995-03-01
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1995-03-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Arizona v. Evans
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/117905/arizona-v-evans/"
  cluster_id: 117905
  opinion_id: 9433091
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Leon]]", "[[Herring v. United States]]", "[[Illinois v. Krull]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "good-faith"]
holding: "The good-faith exception extends to evidence seized on a mistaken arrest record caused by clerical errors of court employees (here, a…"
lake:
  record_id: Arizona v. Evans
  status: verified
  projected_at: 2026-07-09
---

# Arizona v. Evans

*514 U.S. 1 (1995)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Phoenix police stopped Evans for a traffic violation; the patrol-car computer showed an outstanding misdemeanor arrest warrant. Officers arrested him and, in a [[Search Incident to Arrest|search incident to arrest]], found marijuana. In fact the warrant had been quashed weeks earlier, but a court clerk's error left it in the computer system. Evans moved to suppress the marijuana as the fruit of an unlawful arrest.

## Issue
Whether the exclusionary rule requires suppression of evidence seized incident to an arrest that resulted from inaccurate computer records attributable to the clerical error of a *court* employee rather than the police.

## Rule
No. Under the *[[United States v. Leon|Leon]]* cost-benefit framework, suppression is unwarranted because it would not deter the kind of error at issue: "the exclusionary rule was historically designed as a means of deterring police misconduct, not mistakes by court employees." — 514 U.S. at 14. ^pin-14

Court clerks "are not adjuncts to the law enforcement team engaged in the often competitive enterprise of ferreting out crime," so excluding evidence would not deter their recordkeeping errors. Accordingly, "[a]pplication of the *Leon* framework supports a categorical exception to the exclusionary rule for clerical errors of court employees." — [*Id.* at 16](https://www.courtlistener.com/opinion/117905/arizona-v-evans/#:~:text=are%20not%20adjuncts%20to%20the). ^pin-16

## Application
On these facts the inaccurate warrant record resulted from a court clerk's failure to remove a quashed warrant, and the arresting officer reasonably relied on the police computer. Because the error was the court's, not the arresting officer's, and exclusion could not be expected to deter such court-clerk mistakes, the deterrence purpose of the exclusionary rule did not justify suppressing the evidence here.

## Conclusion
The exclusionary rule did not require suppression; the judgment of the Arizona Supreme Court was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Evans* applies the [[United States v. Leon]] good-faith / deterrence analysis to court-clerk recordkeeping errors. The same cost-benefit reasoning was later extended to isolated **negligent police** recordkeeping errors in [[Herring v. United States]] (2009).

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *Arizona v. Evans*, 514 U.S. 1 (1995) — https://www.courtlistener.com/opinion/117905/arizona-v-evans/ — pinpoints: 14, 16.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3d57f302e0c5522a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Arizona v. Evans"}, "payload": {"all": [{"cite": "514 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "514"}, {"cite": "115 S. Ct. 1185", "page": "1185", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "115"}, {"cite": "131 L. Ed. 2d 34", "page": "34", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "131"}, {"cite": "1995 U.S. LEXIS 1806", "page": "1806", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1995"}], "display": "514 U.S. 1", "official": {"cite": "514 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "514"}, "official_selection_present": true, "record_id": "Arizona v. Evans"}}
{"assertion_id": "94a7b86adf53d3cd", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-16", "record_id": "Arizona v. Evans"}, "payload": {"fragment": "#:~:text=are%20not%20adjuncts%20to%20the", "page": null, "pin_id": "pin-16", "pinpoint_status": "star-verified", "quote": "are not adjuncts to the law enforcement team engaged in the often competitive enterprise of ferreting out crime,", "quote_fidelity": "matched", "record_id": "Arizona v. Evans", "star_marker": "15"}}
{"assertion_id": "ae41d4c3ed91c1d7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-14", "record_id": "Arizona v. Evans"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-14", "pinpoint_status": "slip-only", "quote": "--- # Arizona v. Evans *514 U.S. 1 (1995)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Phoenix police stopped Evans for a traffic violation; the patrol-car computer showed an outstanding misdemeanor arrest warrant. Officers arrested him and, in a search incident to arrest, found marijuana. In fact the warrant had been quashed weeks earlier, but a court clerk's error left it in the computer system. Evans moved to suppress the marijuana as the fruit of an unlawful arrest. ## Issue Whether the exclusionary rule requires suppression of evidence seized incident to an arrest that resulted from inaccurate computer records attributable to the clerical error of a *court* employee rather than the police. ## Rule No. Under the *Leon* cost-benefit framework, suppression is unwarranted because it would not deter the kind of error at issue:", "quote_fidelity": "mismatch", "record_id": "Arizona v. Evans", "star_marker": null}}
{"assertion_id": "ec1cf964551d5076", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Arizona v. Evans"}, "payload": {"as_of_content": "1995-03-01", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Arizona v. Evans", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Arizona v. Evans

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arizona v. Evans",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Arizona v. Evans",
    "case_name_short": "Evans",
    "case_name_full": "Arizona v. Evans",
    "input_case_name": "Arizona v. Evans",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1995-03-01",
    "year": 1995,
    "docket": null,
    "cluster_id": 117905,
    "lead_opinion_id": 9433091,
    "sibling_ids": [
      117905,
      9433091,
      9433092,
      9433093,
      9433094,
      9433095
    ],
    "absolute_url": "/opinion/117905/arizona-v-evans/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "514 U.S. 1",
      "volume": "514",
      "reporter": "U.S.",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "115 S. Ct. 1185",
        "volume": "115",
        "reporter": "S. Ct.",
        "page": "1185",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 L. Ed. 2d 34",
        "volume": "131",
        "reporter": "L. Ed. 2d",
        "page": "34",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1995 U.S. LEXIS 1806",
        "volume": "1995",
        "reporter": "U.S. LEXIS",
        "page": "1806",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "514 U.S. 1",
        "volume": "514",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "115 S. Ct. 1185",
        "volume": "115",
        "reporter": "S. Ct.",
        "page": "1185",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 L. Ed. 2d 34",
        "volume": "131",
        "reporter": "L. Ed. 2d",
        "page": "34",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1995 U.S. LEXIS 1806",
        "volume": "1995",
        "reporter": "U.S. LEXIS",
        "page": "1806",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "514 U.S. 1",
    "official_selection": {
      "court_class": "scotus",
      "selected": "514 U.S. 1",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-14",
      "page": null,
      "quote": "--- # Arizona v. Evans *514 U.S. 1 (1995)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Phoenix police stopped Evans for a traffic violation; the patrol-car computer showed an outstanding misdemeanor arrest warrant. Officers arrested him and, in a search incident to arrest, found marijuana. In fact the warrant had been quashed weeks earlier, but a court clerk's error left it in the computer system. Evans moved to suppress the marijuana as the fruit of an unlawful arrest. ## Issue Whether the exclusionary rule requires suppression of evidence seized incident to an arrest that resulted from inaccurate computer records attributable to the clerical error of a *court* employee rather than the police. ## Rule No. Under the *Leon* cost-benefit framework, suppression is unwarranted because it would not deter the kind of error at issue:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-16",
      "page": null,
      "quote": "are not adjuncts to the law enforcement team engaged in the often competitive enterprise of ferreting out crime,",
      "star_marker": "15",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 41308,
      "fragment": "#:~:text=are%20not%20adjuncts%20to%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1995-03-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Arizona v. Evans",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 10705828,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Raenard Romalle Douglas",
          "cluster_id": 10129058,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kruse",
          "cluster_id": 4643214,
          "cite": [
            "303 Neb. 799",
            "931 N.W.2d 148"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
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
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Arredondo",
          "cluster_id": 6238731,
          "cite": [
            "199 Cal. Rptr. 3d 563",
            "245 Cal. App. 4th 186",
            "2016 Cal. App. LEXIS 153"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Rush",
          "cluster_id": 3164356,
          "cite": [
            "808 F.3d 1007",
            "2015 U.S. App. LEXIS 22212",
            "2015 WL 9269763"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4288590,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4287047,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4286131,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chad Camou",
          "cluster_id": 2759861,
          "cite": [
            "773 F.3d 932",
            "2014 U.S. App. LEXIS 23347",
            "2014 WL 6980135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Shondolyn Blevins",
          "cluster_id": 2678617,
          "cite": [
            "755 F.3d 312",
            "2014 WL 2711159",
            "2014 U.S. App. LEXIS 11138"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Isaac John Russell v. State",
          "cluster_id": 3076235,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Smith v. Robbins",
          "cluster_id": 118332,
          "cite": [
            "145 L. Ed. 2d 756",
            "120 S. Ct. 746",
            "528 U.S. 259",
            "2000 U.S. LEXIS 825"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
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
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herring v. United States",
          "cluster_id": 145922,
          "cite": [
            "172 L. Ed. 2d 496",
            "129 S. Ct. 695",
            "555 U.S. 135",
            "2009 U.S. LEXIS 581"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 218926,
          "cite": [
            "180 L. Ed. 2d 285",
            "131 S. Ct. 2419",
            "564 U.S. 229",
            "2011 U.S. LEXIS 4560"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Morrison",
          "cluster_id": 118363,
          "cite": [
            "146 L. Ed. 2d 658",
            "120 S. Ct. 1740",
            "529 U.S. 598",
            "2000 U.S. LEXIS 3422"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Groh v. Ramirez",
          "cluster_id": 131161,
          "cite": [
            "157 L. Ed. 2d 1068",
            "124 S. Ct. 1284",
            "540 U.S. 551",
            "2004 U.S. LEXIS 1624",
            "2004 WL 330057"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hudson v. Michigan",
          "cluster_id": 145646,
          "cite": [
            "165 L. Ed. 2d 56",
            "126 S. Ct. 2159",
            "547 U.S. 586",
            "2006 U.S. LEXIS 4677"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Labron",
          "cluster_id": 118063,
          "cite": [
            "135 L. Ed. 2d 1031",
            "116 S. Ct. 2485",
            "518 U.S. 938",
            "1996 U.S. LEXIS 4268"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania Bd. of Probation and Parole v. Scott",
          "cluster_id": 118235,
          "cite": [
            "141 L. Ed. 2d 344",
            "118 S. Ct. 2014",
            "524 U.S. 357",
            "1998 U.S. LEXIS 4037"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bennis v. Michigan",
          "cluster_id": 118005,
          "cite": [
            "134 L. Ed. 2d 68",
            "116 S. Ct. 994",
            "516 U.S. 442",
            "1996 U.S. LEXIS 1565"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ana Maria Lanza v. John Ashcroft, Attorney General",
          "cluster_id": 788423,
          "cite": [
            "389 F.3d 917",
            "2004 U.S. App. LEXIS 24281",
            "2004 WL 2650828"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. Virginia",
          "cluster_id": 4501697,
          "cite": [
            "584 U.S. 586",
            "138 S. Ct. 1663",
            "201 L. Ed. 2d 9",
            "2018 U.S. LEXIS 3210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Shareef",
          "cluster_id": 154170,
          "cite": [
            "100 F.3d 1491",
            "1996 U.S. App. LEXIS 29483",
            "1996 WL 657885"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 1654613,
          "cite": [
            "760 N.W.2d 35",
            "277 Neb. 37"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Powell",
          "cluster_id": 1736,
          "cite": [
            "175 L. Ed. 2d 1009",
            "130 S. Ct. 1195",
            "559 U.S. 50",
            "2010 U.S. LEXIS 1898"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Raymond A. Berg, Jr. v. County of Allegheny Allegheny County Adult Probation Services Debbie Benton Richard R. Gardner Glenn Allen Wolfgang Ginny Demko",
          "cluster_id": 769512,
          "cite": [
            "219 F.3d 261",
            "2000 U.S. App. LEXIS 16681"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
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
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of California v. the Little Sisters of the Poor",
          "cluster_id": 4573161,
          "cite": [
            "911 F.3d 558"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Christopher Frazier",
          "cluster_id": 791897,
          "cite": [
            "423 F.3d 526",
            "2005 U.S. App. LEXIS 19190",
            "2005 WL 2123792"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. McCane",
          "cluster_id": 172450,
          "cite": [
            "573 F.3d 1037",
            "2009 U.S. App. LEXIS 16557",
            "2009 WL 2231658"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Travis Kinte Echols",
          "cluster_id": 1043929,
          "cite": [
            "382 S.W.3d 266",
            "2012 Tenn. LEXIS 738"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Handy",
          "cluster_id": 2559301,
          "cite": [
            "18 A.3d 179",
            "206 N.J. 39",
            "2011 N.J. LEXIS 566"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Daugherty",
          "cluster_id": 1777786,
          "cite": [
            "931 S.W.2d 268",
            "1996 Tex. Crim. App. LEXIS 88",
            "1996 WL 350804"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Goodridge v. Department of Public Health",
          "cluster_id": 6578806,
          "cite": [
            "440 Mass. 309"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Christopher Duguay",
          "cluster_id": 724910,
          "cite": [
            "93 F.3d 346",
            "1996 WL 467316"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(117905 OR 9433091 OR 9433092 OR 9433093 OR 9433094 OR 9433095) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjgyNzgwODAwMDAwJnM9MjYzMjExMiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28117905+OR+9433091+OR+9433092+OR+9433093+OR+9433094+OR+9433095%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 12,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(117905 OR 9433091 OR 9433092 OR 9433093 OR 9433094 OR 9433095)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzcmcz00NDkzODM4JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28117905+OR+9433091+OR+9433092+OR+9433093+OR+9433094+OR+9433095%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(117905 OR 9433091 OR 9433092 OR 9433093 OR 9433094 OR 9433095)",
        "reviewed": 34,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 34,
        "triage_read": 2,
        "triage_snippet_classified": 32
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(117905 OR 9433091 OR 9433092 OR 9433093 OR 9433094 OR 9433095)",
    "indexed_citing_opinions": 536,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 117905,
        "count": 456,
        "count_source": "search"
      },
      {
        "opinion_id": 9433091,
        "count": 99,
        "count_source": "search"
      },
      {
        "opinion_id": 9433092,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433093,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433094,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433095,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 886,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/arizona-v-evans.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1NTU5MTUmcz05NDQ3NTM5JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28117905+OR+9433091+OR+9433092+OR+9433093+OR+9433094+OR+9433095%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 117905,
        "cited_id": 85330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 91840,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 101688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 101887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 103012,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 103332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 110100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 110267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111156,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111207,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111835,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 112205,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 112475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 112640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 312873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 1142841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 1403994,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 1445040,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 2144680,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 2609885,
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
    "date_created": "2026-07-04T18:08:00Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:08:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:08:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:14:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:08:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Arizona v. Evans

```
<opinion type="majority">
<author id="b77-11">Chief Justice Rehnquist</author>
<p id="Ar">delivered the opinion of the Court.</p>
<p id="b77-12">This case presents the question whether evidence seized in violation of the Fourth Amendment by an officer who <page-number citation-index="1" label="4">*4</page-number>acted in reliance on a police record indicating the existence of an outstanding arrest <em>warrant </em>— a record that is later determined to be erroneous — must be suppressed by virtue of the exclusionary rule regardless of the source of the error. The Supreme Court of Arizona held that the exclusionary rule required suppression of evidence even if the erroneous information resulted from an error committed by an employee of the office of the Clerk of Court. We disagree.</p>
<p id="b78-5">In January 1991, Phoenix police officer Bryan Sargent observed respondent Isaac Evans driving the wrong way on a one-way street in front of the police station. The officer stopped respondent and asked to see his driver’s license. After respondent told him that his license had been suspended, the officer entered respondent’s name into a computer data terminal located in his patrol car. The computer inquiry confirmed that respondent’s license had been suspended and also indicated that there was an outstanding misdemeanor warrant for his arrest. Based upon the outstanding warrant, Officer Sargent placed respondent under arrest. While being handcuffed, respondent dropped a hand-rolled cigarette that the officers determined smelled of marijuana. Officers proceeded to search his car and discovered a bag of marijuana under the passenger’s seat.</p>
<p id="b78-6">The State charged respondent with possession of marijuana. When the police notified the Justice Court that they had arrested him, the Justice Court discovered that the arrest warrant previously had been quashed and so advised the police. Respondent argued that because his arrest was based on a warrant that had been quashed 17 days prior to his arrest, the marijuana seized incident to the arrest should be suppressed as the fruit of an unlawful arrest. Respondent also argued that “[t]he ‘good faith’ exception to the exclusionary rule [was] inapplicable ... because it was police error, not judicial error, which caused the invalid arrest.” App. 5.</p>
<p id="b78-7">At the suppression hearing, the Chief Clerk of the Justice Court testified that a Justice of the Peace had issued the <page-number citation-index="1" label="5">*5</page-number>arrest warrant on December 13, 1990, because respondent had failed to appear to answer for several, traffic violations. On December 19,1990, respondent appeared before a <em>pro tem </em>Justice of the Peace who entered a notation in respondent’s file to “quash warrant.” <em>Id., </em>at 13.</p>
<p id="b79-5">The Chief Clerk also testified regarding the standard court procedure for quashing a warrant. Under that procedure a justice court clerk calls and informs the warrant section of the Sheriff’s Office when a warrant has been quashed. The Sheriff’s Office then removes the warrant from its computer records. After calling the Sheriff’s Office, the clerk makes a note in the individual’s file indicating the clerk who made the phone call and the person at the Sheriff’s Office to whom the clerk spoke. The Chief Clerk testified that there was no indication in respondent’s file that a clerk had called and notified the Sheriff’s Office that his arrest warrant had been quashed. A records clerk from the Sheriff’s Office also testified that the Sheriff’s Office had no record of a telephone call informing it that respondent’s arrest warrant had been quashed. <em>Id., </em>at 42-43.</p>
<p id="b79-6">At the close of testimony, respondent argued that the evidence obtained as a result of the arrest should be suppressed because “the purposes of the exclusionary rule would be served here by making the clerks for the court, or the clerk for the Sheriff’s office, whoever is responsible for this mistake, to be more careful about making sure that warrants are removed from the records.” <em>Id., </em>at 47. The trial court granted the motion to suppress because it concluded that the State had been at fault for failing to quash the warrant. Presumably because it could find no “distinction between State action, whether it happens to be the police department or not,” <em>id., </em>at 52, the trial court made no factual finding as to whether the Justice Court or Sheriff’s Office was responsible for the continued presence of the quashed warrant in the police records.</p>
<p id="b80-4"><page-number citation-index="1" label="6">*6</page-number>A divided panel of the Arizona Court of Appeals reversed because it “believe[d] that the exclusionary rule [was] not intended to deter justice court employees or Sheriff’s Office employees who are not directly associated with the arresting officers or the arresting officers’ police department.” <span class="citation" data-id="9631692"><a href="/opinion/1445040/state-v-evans/#317" aria-description="Citation for case: State v. Evans">172 Ariz. 314, 317</a></span>, <span class="citation" data-id="9631692"><a href="/opinion/1445040/state-v-evans/#1027" aria-description="Citation for case: State v. Evans">836 P. 2d 1024, 1027</a></span> (1992). Therefore, it concluded, “the purpose of the exclusionary rule would not be served by excluding the evidence obtained in this case.” <em><span class="citation" data-id="9631692"><a href="/opinion/1445040/state-v-evans/" aria-description="Citation for case: State v. Evans">Ibid.</a></span></em></p>
<p id="b80-5">The Arizona Supreme Court reversed. <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/" aria-description="Citation for case: State v. Evans">177 Ariz. 201</a></span>, <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/" aria-description="Citation for case: State v. Evans">866 P. 2d 869</a></span> (1994). The court rejected the “distinction drawn by the court of appeals ... between clerical errors committed by law enforcement personnel and similar mistakes by court employees.” <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/#203" aria-description="Citation for case: State v. Evans"><em>Id., </em>at 203</a></span>, <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/#871" aria-description="Citation for case: State v. Evans">866 P. 2d, at 871</a></span>. The court predicted that application of the exclusionary rule would “hopefully serve to improve the efficiency of those who keep records in our criminal justice system.” <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/#204" aria-description="Citation for case: State v. Evans"><em>Id., </em>at 204</a></span>, <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/#872" aria-description="Citation for case: State v. Evans">866 P. 2d, at 872</a></span>. Finally, the court concluded that “[e]ven assuming that deterrence is the principal reason for application of the exclusionary rule, we disagree with the court of appeals that such a purpose would not be served where carelessness by a court clerk results in an unlawful arrest.” <em><span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/" aria-description="Citation for case: State v. Evans">Ibid.</a></span></em></p>
<p id="b80-6">We granted certiorari to determine whether the exclusionary rule requires suppression of evidence seized incident to an arrest resulting from an inaccurate computer record, regardless of whether police personnel or court personnel were responsible for the record’s continued presence in the police computer. <span class="citation multiple-matches"><a href="/c/U.%20S./511/1126/">511 U. S. 1126</a></span> (1994).<footnotemark>1</footnotemark> We now reverse.</p>
<p id="b80-7">We first must consider whether we have jurisdiction to review the Arizona Supreme Court’s decision. Respondent argues that we lack jurisdiction under <span class="citation no-link">28 U. S. C. § 1257</span> because the Arizona Supreme Court never passed upon the <page-number citation-index="1" label="7">*7</page-number>Fourth Amendment issue and instead based its decision on the Arizona good-faith statute, <span class="citation no-link">Ariz. Rev. Stat. Ann. § 13-3925</span> (1993), an adequate and independent state ground. In the alternative, respondent asks that we remand to the Arizona Supreme Court for clarification.</p>
<p id="b81-5">In <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983), we adopted a standard for determining whether a state-court decision rested upon an adequate and independent state ground. When “a state court decision fairly appears to rest primarily on federal law, or to be interwoven with the federal law, and when the adequacy and independence of any possible state law ground is not clear from the face of the opinion, we will accept as the most reasonable explanation that the state court decided the case the way it did because it believed that federal law required it to do so.” <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long"><em>Id., </em>at 1040-1041</a></span>. We adopted this practice, in part, to obviate the “unsatisfactory and intrusive practice of requiring state courts to clarify their decisions to the satisfaction of this Court.” <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1041" aria-description="Citation for case: Michigan v. Long"><em>Id., </em>at 1041</a></span>. We also concluded that this approach would “provide state judges with a clearer opportunity to develop state jurisprudence unimpeded by federal interference, and yet will preserve the integrity of federal law.” <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Ibid.</a></span></em></p>
<p id="b81-6">Justice Ginsburg would overrule <em>Michigan </em>v. <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long, supra,</a></span> </em>because she believes that the rule of that case “impedes the States’ ability to serve as laboratories for testing solutions to novel legal problems.” <em>Post, </em>at 24.<footnotemark>2</footnotemark> The opin<page-number citation-index="1" label="8">*8</page-number>ion in <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span> </em>describes the 60-year history of the Court’s differing approaches to the determination whether the judgment of the highest court of a State rested on federal or nonfederal grounds. <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1038" aria-description="Citation for case: Michigan v. Long">463 U. S., at 1038-1040</a></span>. When we were in doubt, on some occasions we dismissed the writ of certiorari; on other occasions we vacated the judgment of the state court and remanded so that it might clarify the basis for its decision. See <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">ibid.</a></span> </em>The latter approach did not always achieve the desired result and burdened the state courts with additional work. <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Ibid.</a></span></em></p>
<p id="b82-5">We believe that <em>Michigan </em>v. <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span> </em>properly serves its purpose and should not be disturbed. Under it, state courts are absolutely free to interpret state constitutional provisions to accord greater protection to individual rights than do similar provisions of the United States Constitution. They also are free to serve as experimental laboratories, in the sense that Justice Brandéis used that term in his dissenting opinion in <em>New State Ice Co. </em>v. <em>Liebmann, </em><span class="citation" data-id="9418740"><a href="/opinion/101887/new-state-ice-co-v-liebmann/#311" aria-description="Citation for case: New State Ice Co. v. Liebmann">285 U. S. 262, 311</a></span> (1932) (urging that the Court not impose federal constitutional restraints on the efforts of a State to “serve as a laboratory”). Under our decision today, the State of Arizona remains free to seek whatever solutions it chooses to problems of law enforcement posed by the advent of computerization.<footnotemark>3</footnotemark> Indeed, it is freer to do so because it is disabused of its erroneous view of what the United States Constitution requires.</p>
<p id="b82-6">State courts, in appropriate cases, are not merely free to— they are bound to — interpret the United States Constitution. In doing so, they are <em>not </em>free from the final authority of this <page-number citation-index="1" label="9">*9</page-number>Court. This principle was enunciated in <em>Cohens </em>v. <em>Virginia, </em><span class="citation" data-id="85330"><a href="/opinion/85330/cohens-v-virginia/" aria-description="Citation for case: Cohens v. Virginia">6 Wheat. 264</a></span> (1821), and presumably Justice Ginsburg does not quarrel with it.<footnotemark>4</footnotemark> In <em>Minnesota </em>v. <em>National Tea Co., </em><span class="citation" data-id="9419097"><a href="/opinion/103332/minnesota-v-national-tea-co/" aria-description="Citation for case: Minnesota v. National Tea Co.">309 U. S. 551</a></span> (1940), we recognized that our authority as final arbiter of the United States Constitution could be eroded by a lack of clarity in state-court decisions.</p>
<blockquote id="b83-5">“It is fundamental that state courts be left free and unfettered by us in interpreting their state constitutions. But it is equally important that ambiguous or obscure adjudications by state courts do not stand as barriers to a determination by this Court of the validity under the federal constitution of state action. Intelligent exercise of our appellate powers compels us to ask for the elimination of the obscurities and ambiguities from the opinions in such cases. ... For no other course assures that important federal issues, such as have been argued here, will reach this Court for adjudication; that state courts will not be the final arbiters of important issues under the federal constitution; and that we will not encroach on the constitutional jurisdiction of the states.” <span class="citation" data-id="9419097"><a href="/opinion/103332/minnesota-v-national-tea-co/#557" aria-description="Citation for case: Minnesota v. National Tea Co."><em>Id., </em>at 557</a></span>.</blockquote>
<p id="b83-6">We therefore adhere to the standard adopted in <em>Michigan </em>v. <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long, supra.</a></span></em></p>
<p id="b83-7">Applying that standard here, we conclude that we have jurisdiction. In reversing the Court of Appeals, the Arizona Supreme Court stated that “[w]hile it may be inappropriate to invoke the exclusionary rule where a magistrate has issued a facially valid warrant (a discretionary judicial function) based on an erroneous evaluation of the facts, the law, or both, <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U. S. 897</a></span> ... (1984), it is useful and proper <page-number citation-index="1" label="10">*10</page-number>to do so where negligent record keeping (a purely clerical function) results in an unlawful arrest.” <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/#204" aria-description="Citation for case: State v. Evans">177 Ariz., at 204</a></span>, <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/#872" aria-description="Citation for case: State v. Evans">866 P. 2d, at 872</a></span>. Thus, the Arizona Supreme Court’s decision to suppress the evidence was based squarely upon its interpretation of federal law. See <em><span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/" aria-description="Citation for case: State v. Evans">ibid.</a></span> </em>Nor did it offer a plain statement that its references to federal law were “being used only for the purpose of guidance, and d[id] not themselves compel the result that [it] reached.” <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1041" aria-description="Citation for case: Michigan v. Long"><em>Long, supra, </em>at 1041</a></span>.</p>
<p id="b84-5">The Fourth Amendment states that “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.” We have recognized, however, that the Fourth Amendment contains no provision expressly precluding the use of evidence obtained in violation of its commands. See <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 906</a></span> (1984). “The wrong condemned by the [Fourth] Amendment is ‘fully accomplished’ by the unlawful search or seizure itself,” <em>ibid, </em>(quoting <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#354" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 354</a></span> (1974)), and the use of the fruits of a past unlawful search or seizure “ ‘work[s] no new Fourth Amendment wrong,’ ” <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon, supra,</a></span> </em>at 906 (quoting <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#354" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 354</a></span>).</p>
<p id="b84-6">“The question whether the exclusionary rule’s remedy is appropriate in a particular context has long been regarded as an issue separate from the question whether the Fourth Amendment rights of the party seeking to invoke the rule were violated by police conduct.” <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#223" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 223</a></span> (1983); see also <em>United States </em>v. <em>Havens, </em><span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#627" aria-description="Citation for case: United States v. Havens">446 U. S. 620, 627-628</a></span> (1980); <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 486-487</a></span> (1976); <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>. The exclusionary rule operates as a judicially created remedy designed to safeguard against future violations of Fourth Amendment rights through the rule’s general deterrent effect. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at <page-number citation-index="1" label="11">*11</page-number>906</a></span>; <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>. As with any remedial device, the rule’s application has been restricted to those instances where its remedial objectives are thought most efficaciously served. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#908" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 908</a></span>; <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>. Where “the exclusionary rule does not result in appreciable deterrence, then, clearly, its use ... is unwarranted.” <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#454" aria-description="Citation for case: United States v. Janis">428 U. S. 433, 454</a></span> (1976).</p>
<p id="b85-5">In <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>, </em>we applied these principles to the context of a police search in which the officers had acted in objectively reasonable reliance on a search warrant, issued by a neutral and detached Magistrate, that later was determined to be invalid. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#905" aria-description="Citation for case: United States v. Leon">468 U. S., at 905</a></span>. On the basis of three factors, we determined that there was no sound reason to apply the exclusionary rule as a means of deterring misconduct on the part of judicial officers who are responsible for issuing warrants. See <em>Illinois </em>v. <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#348" aria-description="Citation for case: Illinois v. Krull">480 U. S. 340, 348</a></span> (1987) (analyzing <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon, supra).</a></span> </em>First, we noted that the exclusionary rule was historically designed “‘to deter police misconduct rather than to punish the errors of judges and magistrates.’ ” <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull, supra,</a></span> </em>at 348 (quoting <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#916" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 916</a></span>). Second, there was “ ‘no evidence suggesting that judges and magistrates are inclined to ignore or subvert the Fourth Amendment or that lawlessness among these actors requires the application of the extreme sanction of exclusion.’” <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull, supra,</a></span> </em>at 348 (quoting <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#916" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 916</a></span>). Third, and of greatest importance, there was no basis for believing that exclusion of evidence seized pursuant to a warrant would have a significant deterrent effect on the issuing judge or magistrate. <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#348" aria-description="Citation for case: Illinois v. Krull"><em>Krull, supra, </em>at 348</a></span>.</p>
<p id="b85-6">The <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>Court then examined whether application of the exclusionary rule could be expected to alter the behavior of the law enforcement officers. We concluded:</p>
<blockquote id="b85-7">“[W]here the officer’s conduct is objectively reasonable, ‘excluding the evidence will not further the ends of the exclusionary rule in any appreciable way; for it is painfully apparent that... the officer is acting as a reason<page-number citation-index="1" label="12">*12</page-number>able officer would and should act in similar circumstances. Excluding the evidence can in no way affect his future conduct unless it is to make him less willing to do his duty.’” <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon, supra,</a></span> </em>at 919-920 (quoting <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#539" aria-description="Citation for case: Stone v. Powell"><em>Stone, supra, </em>at 539-540</a></span> (White, J., dissenting)).</blockquote>
<p id="AH">See also <em>Massachusetts </em>v. <em>Sheppard, </em><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#990" aria-description="Citation for case: Massachusetts v. Sheppard">468 U. S. 981, 990-991</a></span> (1984) (“[Suppressing evidence because the judge failed to make all the necessary clerical corrections despite his assurances that such changes would be made will not serve the deterrent function that the exclusionary rule was designed to achieve”). Thus, we held that the “marginal or nonexistent benefits produced by suppressing evidence obtained in objectively reasonable reliance on a subsequently invalidated search warrant cannot justify the substantial costs of exclusion.” <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 922</a></span>.</p>
<p id="b86-6">Respondent relies on <em>United States </em>v. <em>Hensley, </em><span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/" aria-description="Citation for case: United States v. Hensley">469 U. S. 221</a></span> (1985), and argues that the evidence seized incident to his arrest should be suppressed because he was the victim of a Fourth Amendment violation. Brief for Respondent 10-12, 21-22. In <em><span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/" aria-description="Citation for case: United States v. Hensley">Hensley</a></span>, </em>the Court determined that evidence uncovered as a result of a stop pursuant to <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), was admissible because the officers who made the stop acted in objectively reasonable reliance on a flyer that had been issued by officers of another police department who possessed a reasonable suspicion to justify a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop. <span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/#231" aria-description="Citation for case: United States v. Hensley">469 U. S., at 231</a></span>. Because the <em><span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/" aria-description="Citation for case: United States v. Hensley">Hensley</a></span> </em>Court determined that there had been no Fourth Amendment violation, <span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/#236" aria-description="Citation for case: United States v. Hensley"><em>id., </em>at 236</a></span>, the Court never considered whether the seized evidence should have been excluded. <em><span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/" aria-description="Citation for case: United States v. Hensley">Hensley</a></span> </em>does not contradict our earlier pronouncements that “[t]he question whether the exclusionary rule’s remedy is appropriate in a particular context has long been regarded as an issue separate from the question whether the Fourth Amendment rights of the party seeking to invoke the rule were violated by police conduct.” <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#223" aria-description="Citation for case: Illinois v. Gates"><em>Gates, supra, </em>at 223</a></span>; see also <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell"><em>Stone, supra, </em>at 486-487</a></span>; <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>.</p>
<p id="b87-4"><page-number citation-index="1" label="13">*13</page-number>Respondent also argues that <em>Whiteley </em>v. <em>Warden, Wyo. State Penitentiary, </em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560</a></span> (1971), compels exclusion of the evidence. In <em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span>, </em>the Court determined that the Fourth Amendment had been violated when police officers arrested Whiteley and recovered inculpatory evidence based upon a radio report that two suspects had been involved in two robberies. <span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#568" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary"><em>Id., </em>at 568-569</a></span>. Although the “police were entitled to act on the strength of the radio bulletin,” the Court determined that there had been a Fourth Amendment violation because the initial complaint, upon which the arrest warrant and subsequent radio bulletin were based, was insufficient to support an independent judicial assessment of probable cause. <span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#568" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary"><em>Id., </em>at 568</a></span>. The Court concluded that “an otherwise illegal arrest cannot be insulated from challenge by the decision of the instigating officer to rely on fellow officers to make the arrest.” <em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Ibid.</a></span> </em>Because the “arrest violated [Whiteley’s] constitutional rights under the Fourth and Fourteenth Amendments; the evidence secured as an incident thereto should have been excluded from his trial. <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961).” <em>Id., </em>at 568-569.</p>
<p id="b87-5">Although <em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span> </em>clearly retains relevance in determining whether police officers have violated the Fourth Amendment, see <span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/#230" aria-description="Citation for case: United States v. Hensley"><em>Hensley, supra, </em>at 230-231</a></span>, its precedential value regarding application of the exclusionary rule is dubious. In <em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span>, </em>the Court treated identification of a Fourth Amendment violation as synonymous with application of the exclusionary rule to evidence secured incident to that violation. <span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#568" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S., at 568-569</a></span>. Subsequent case law has rejected this reflexive application of the exclusionary rule. Cf. <em>Illinois </em>v. <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">480 U. S. 340</a></span> (1987); <em><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard, supra;</a></span> United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U. S. 897</a></span> (1984); <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">414 U. S. 338</a></span> (1974). These later cases have emphasized that the issue of exclusion is separate from whether the Fourth Amendment has been violated, see, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon"><em>e. g., Leon, supra, </em>at 906</a></span>, and exclusion is appropriate only if the <page-number citation-index="1" label="14">*14</page-number>remedial objectives of the rule are thought most efficaciously served, see <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>.</p>
<p id="b88-5">Our approach is consistent with the dissenting Justices’ position in <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull</a></span>, </em>our only major case since <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>and <em><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard</a></span> </em>involving the good-faith exception to the exclusionary rule. In that case, the Court found that the good-faith exception applies when an officer conducts a search in objectively reasonable reliance on the constitutionality of a statute that subsequently is declared unconstitutional. <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#346" aria-description="Citation for case: Illinois v. Krull"><em>Krull, supra, </em>at 346</a></span>. Even the dissenting Justices in <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull</a></span> </em>agreed that <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>provided the proper framework for analyzing whether the exclusionary rule applied; they simply thought that “application of <em>Leon’s </em>stated rationales le[d] to a contrary result.” <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#362" aria-description="Citation for case: Illinois v. Krull">480 U. S., at 362</a></span> (O’Connor, J., dissenting). In sum, respondent does not persuade us to abandon the <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>framework.</p>
<p id="b88-6">Applying the reasoning of <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>to the facts of this ease, we conclude that the decision of the Arizona Supreme Court must be reversed. The Arizona Supreme Court determined that it could not “support the distinction drawn ... between clerical errors committed by law enforcement personnel and similar mistakes by court employees,” <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/#203" aria-description="Citation for case: State v. Evans">177 Ariz., at 203</a></span>, <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/#871" aria-description="Citation for case: State v. Evans">866 P. 2d, at 871</a></span>, and that “even assuming... that responsibility for the error rested with the justice court, it does not follow that the exclusionary rule should be inapplicable to these facts,” <em><span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/" aria-description="Citation for case: State v. Evans">ibid.</a></span></em></p>
<p id="b88-7">This holding is contrary to the reasoning of <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon, supra;</a></span> Massachusetts </em>v. <em><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard, supra;</a></span> </em>and, <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull, supra.</a></span> </em>If court employees were responsible for the erroneous computer record, the exclusion of evidence at trial would not sufficiently deter fiiture errors so as to warrant such a severe sanction. First, as we noted in <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>, </em>the exclusionary rule was historically designed as a means of deterring police misconduct, not mistakes by court employees. See <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#916" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 916</a></span>; see also <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#350" aria-description="Citation for case: Illinois v. Krull"><em>Krull, supra, </em>at 350</a></span>. Second, respondent offers no evidence that court employees are in-<page-number citation-index="1" label="15">*15</page-number>dined to ignore or subvert the Fourth Amendment or that lawlessness among these actors requires application of the extreme sanction of exclusion. See <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#916" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 916</a></span>, and n. 14; see also <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#350" aria-description="Citation for case: Illinois v. Krull"><em>Krull, supra, </em>at 350-351</a></span>. To the contrary, the Chief Clerk of the Justice Court testified at the suppression hearing that this type of error occurred once every three or four years. App. 37.</p>
<p id="b89-5">Finally, and most important, there is no basis for believing that application of the exclusionary rule in these circumstances will have a significant effect on court employees responsible for informing the police that a warrant has been quashed. Because court clerks are not adjuncts to the law enforcement team engaged in the often competitive enterprise of ferreting out crime, see <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948), they have no stake in the outcome of particular criminal prosecutions. Cf. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#917" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 917</a></span>; <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#352" aria-description="Citation for case: Illinois v. Krull"><em>Krull, supra, </em>at 352</a></span>. The threat of exclusion of evidence could not be expected to deter such individuals from failing to inform police officials that a warrant had been quashed. Cf. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#917" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 917</a></span>; <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#352" aria-description="Citation for case: Illinois v. Krull"><em>Krull, supra, </em>at 352</a></span>.</p>
<p id="b89-6">If it were indeed a court clerk who was responsible for the erroneous entry on the police computer, application of the exclusionary rule also could not be expected to alter the behavior of the arresting officer. As the trial court in this case stated: “I think the police officer [was] bound to arrest. I think he would [have been] derelict in his duty if he failed to arrest.” App. 51. Cf. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#920" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 920</a></span> (“ ‘Excluding the evidence can in no way affect [the officer’s] future conduct unless it is to make him less willing to do his duty.’ ” quoting <em>Stone, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#540" aria-description="Citation for case: Stone v. Powell">428 U. S., at 540</a></span> (White, J., dissenting)). The Chief Clerk of the Justice Court testified that this type of error occurred “on[c]e every three or four years.” App. 37. In fact, once the court clerks discovered the error, they immediately corrected it, <em>id., </em>at 30, and then proceeded to search their files to make sure that no similar mistakes had occurred, <em>id., </em>at 37. There is no indication that the arresting <page-number citation-index="1" label="16">*16</page-number>officer was not acting objectively reasonably when he relied upon the police computer record. Application of the <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>framework supports a categorical exception to the exclusionary rule for clerical errors of court employees. See <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#916" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 916-922</a></span>; <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#990" aria-description="Citation for case: Massachusetts v. Sheppard"><em>Sheppard, supra, </em>at 990-991</a></span>.<footnotemark>5</footnotemark></p>
<p id="b90-5">The judgment of the Supreme Court of Arizona is therefore reversed, and the case is remanded to that court for proceedings not inconsistent with this opinion.</p>
<p id="b90-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b80-8"> Petitioner has conceded that respondent's arrest violated the Fourth Amendment. Brief for Petitioner 10. We decline to review that determination. Cf. <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#905" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 905</a></span> (1984); <em>Illinois </em>v. <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#357" aria-description="Citation for case: Illinois v. Krull">480 U. S. 340, 357, n. 13</a></span> (1987).</p>
</footnote>
<footnote label="2">
<p id="b81-7"> Justice Ginsburg certainly is correct when she notes that “‘[s]ince <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span>, </em>we repeatedly have followed [its] “plain statement” requirement.’” <em>Post, </em>at 33 (quoting <em>Harris </em>v. <em>Reed, </em><span class="citation" data-id="9431577"><a href="/opinion/112205/harris-v-reed/#261" aria-description="Citation for case: Harris v. Reed">489 U. S. 255, 261, n. 7</a></span> (1989) (opinion of Blackmun, J.)); see also <em>Illinois </em>v. <em>Rodriguez, </em><span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/#182" aria-description="Citation for case: Illinois v. Rodriguez">497 U. S. 177, 182</a></span> (1990) (opinion of Scalia, J.); <em>Pennsylvania </em>v. <em>Muniz, </em><span class="citation" data-id="9432075"><a href="/opinion/112464/pennsylvania-v-muniz/#588" aria-description="Citation for case: Pennsylvania v. Muniz">496 U. S. 582, 588, n. 4</a></span> (1990) (opinion of Brennan, J.); <em>Maryland </em>v. <em>Garrison, </em><span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#83" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79, 83-84</a></span> (1987) (opinion of Stevens, J.); <em>Caldwell </em>v. <em>Mississippi, </em><span class="citation" data-id="111471"><a href="/opinion/111471/caldwell-v-mississippi/#327" aria-description="Citation for case: Caldwell v. Mississippi">472 U. S. 320, 327-328</a></span> (1985) (opinion of Marshall, J.); <em>California </em>v. <em>Carney, </em><span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#389" aria-description="Citation for case: California v. Carney">471 U. S. 386, 389, n. 1</a></span> (1985) (opinion of Burger, C. J.); <em>Ohio </em>v. <em>Johnson, </em><span class="citation" data-id="9429653"><a href="/opinion/111207/ohio-v-johnson/#497" aria-description="Citation for case: Ohio v. Johnson">467 U. S. 493, 497-498, n. 7</a></span> (1984) (opinion of Rehnquist, J.); <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#175" aria-description="Citation for case: Oliver v. United States">466 U. S. 170, 175-176, n. 5</a></span> (1984) (opinion of Powell, J.); cf. <em>Coleman </em><page-number citation-index="1" label="8">*8</page-number>v. <em>Thompson, </em><span class="citation" data-id="9842121"><a href="/opinion/112640/coleman-v-thompson/#740" aria-description="Citation for case: Coleman v. Thompson">501 U. S. 722, 740</a></span> (1991) (opinion of O’Connor, J.) (declining to expand the <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span> </em>and <em><span class="citation" data-id="9431577"><a href="/opinion/112205/harris-v-reed/" aria-description="Citation for case: Harris v. Reed">Harris</a></span> </em>presumption to instances “where the relevant state court decision does not fairly appear to rest primarily on federal law or to be interwoven with such law”).</p>
</footnote>
<footnote label="3">
<p id="b82-9"> Justice Ginsburg acknowledges as much when she states that since <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span>, </em>“state courts, on remand, have reinstated their prior judgments after clarifying their reliance on state grounds.” <em>Post, </em>at 32 (citing statistics).</p>
</footnote>
<footnote label="4">
<p id="b83-8"> Surely if we have jurisdiction to vacate and remand a state-court judgment for clarification, <em>post, </em>at 34, n. 7, we also must have jurisdiction to determine whether a state-court judgment is based upon an adequate and independent state ground. See <em>Abie State Bank </em>v. <em>Bryan, </em><span class="citation" data-id="101688"><a href="/opinion/101688/abie-state-bank-v-bryan/#773" aria-description="Citation for case: Abie State Bank v. Bryan">282 U. S. 765, 773</a></span> (1931).</p>
</footnote>
<footnote label="5">
<p id="b90-10"> The Solicitor General, as <em>amicus curiae, </em>argues that an analysis similar to that we apply here to court personnel also would apply in order to determine whether the evidence should be suppressed if police personnel were responsible for the error. As the State has not made any such argument here, we agree that “[t]he record in this case ... does not adequately present that issue for the Court’s consideration.” Brief for United States as <em>Amicus Curiae </em>13. Accordingly, we decline to address that question.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Arizona v. Fulminante.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Arizona v. Fulminante"
type: case
citation: "499 U.S. 279 (1991)"
parallel_cite: "111 S. Ct. 1246; 113 L. Ed. 2d 302"
neutral_cite: 1991 U.S. LEXIS 1854
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1991
date_decided: 1991-05-20
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1991-05-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Arizona v. Fulminante
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112566/arizona-v-fulminante/"
  cluster_id: 112566
  opinion_id: 112566
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Colorado v. Connelly]]", "[[Chambers v. Florida]]"]
aliases: []
tags: ["case", "due-process", "confessions", "voluntariness", "harmless-error"]
holding: "The admission of an involuntary/coerced confession is a \"trial error\" subject to harmless-error analysis under Chapman, not automatic…"
lake:
  record_id: Arizona v. Fulminante
  status: verified
  projected_at: 2026-07-09
---

# Arizona v. Fulminante

*499 U.S. 279 (1991)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Fulminante was suspected of murdering his stepdaughter. While later incarcerated on an unrelated federal charge, he was befriended by Anthony Sarivola, a fellow inmate who was secretly a paid FBI informant. Knowing Fulminante was receiving rough treatment from other inmates over a rumor that he was a child-killer, Sarivola offered to protect him if he told the truth about the murder. Fulminante confessed to Sarivola, and later to Sarivola's wife. Both confessions were admitted at his murder trial; he was convicted and sentenced to death.

## Issue
(1) Whether a confession given out of fear of violence from other inmates, in exchange for an informant's protection, was coerced in violation of due process; and (2) whether the erroneous admission of a coerced confession is subject to harmless-error analysis or instead requires automatic reversal.

## Rule
A credible threat of violence can render a confession involuntary — coercion may be mental, not only physical: "Our cases have made clear that a finding of coercion need not depend upon actual violence by a government agent; a credible threat is sufficient." — 499 U.S. at 287. ^pin-287

The Court then overruled the prior automatic-reversal rule for coerced confessions: "The Court today properly concludes that the admission of an 'involuntary' confession at trial is subject to harmless-error analysis." — *Id.* at 303. ^pin-303

A coerced confession is a "trial error," not a structural defect: "The admission of an involuntary confession—a classic 'trial error'—is markedly different from the other two constitutional violations referred to in the *Chapman* footnote as not being subject to harmless-error analysis." — [*Id.* at 309](https://www.courtlistener.com/opinion/112566/arizona-v-fulminante/#:~:text=though%20a%20%22-,trial%20error%2C). ^pin-309

## Application
On these facts the Court accepted the finding that Fulminante confessed out of fear of physical violence from other inmates — violence Sarivola, a government agent, offered to prevent only if Fulminante confessed — a credible threat that overbore his will and made the confession coerced. And although harmless-error review now applies to such confessions, the Court held that admitting *this* confession was not harmless [[Common Legal Terms#beyond-a-reasonable-doubt|beyond a reasonable doubt]], because the State could not show the jury would have convicted without it.

## Conclusion
The confession was coerced; harmless-error analysis applies to coerced confessions, but the error here was not harmless. The judgment of the Arizona Supreme Court — reversing the conviction and ordering a retrial without the confession — was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Fulminante* is the seminal modern statement that (a) a credible threat of violence can coerce a confession (mental coercion suffices), and (b) the erroneous admission of a coerced confession is "trial error" reviewable for harmlessness under *Chapman v. California*, in contrast to "structural defects" that defy harmless-error analysis.

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Arizona v. Fulminante*, 499 U.S. 279 (1991) — https://www.courtlistener.com/opinion/112566/arizona-v-fulminante/ — pinpoints: 287, 303, 309.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "10f5b41e3ac0e033", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Arizona v. Fulminante"}, "payload": {"all": [{"cite": "499 U.S. 279", "page": "279", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "499"}, {"cite": "111 S. Ct. 1246", "page": "1246", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "111"}, {"cite": "113 L. Ed. 2d 302", "page": "302", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "113"}, {"cite": "1991 U.S. LEXIS 1854", "page": "1854", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1991"}], "display": "499 U.S. 279", "official": {"cite": "499 U.S. 279", "page": "279", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "499"}, "official_selection_present": true, "record_id": "Arizona v. Fulminante"}}
{"assertion_id": "062ff54bfbb437cb", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-303", "record_id": "Arizona v. Fulminante"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-303", "pinpoint_status": "slip-only", "quote": "The Court today properly concludes that the admission of an 'involuntary' confession at trial is subject to harmless-error analysis.", "quote_fidelity": "mismatch", "record_id": "Arizona v. Fulminante", "star_marker": null}}
{"assertion_id": "5ac63eb4bb84ed24", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-287", "record_id": "Arizona v. Fulminante"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-287", "pinpoint_status": "slip-only", "quote": "--- # Arizona v. Fulminante *499 U.S. 279 (1991)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Fulminante was suspected of murdering his stepdaughter. While later incarcerated on an unrelated federal charge, he was befriended by Anthony Sarivola, a fellow inmate who was secretly a paid FBI informant. Knowing Fulminante was receiving rough treatment from other inmates over a rumor that he was a child-killer, Sarivola offered to protect him if he told the truth about the murder. Fulminante confessed to Sarivola, and later to Sarivola's wife. Both confessions were admitted at his murder trial; he was convicted and sentenced to death. ## Issue (1) Whether a confession given out of fear of violence from other inmates, in exchange for an informant's protection, was coerced in violation of due process; and (2) whether the erroneous admission of a coerced confession is subject to harmless-error analysis or instead requires automatic reversal. ## Rule A credible threat of violence can render a confession involuntary — coercion may be mental, not only physical:", "quote_fidelity": "mismatch", "record_id": "Arizona v. Fulminante", "star_marker": null}}
{"assertion_id": "7afcc461879db5ff", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-309", "record_id": "Arizona v. Fulminante"}, "payload": {"fragment": "#:~:text=though%20a%20%22-,trial%20error%2C", "page": null, "pin_id": "pin-309", "pinpoint_status": "star-verified", "quote": "trial error,", "quote_fidelity": "matched", "record_id": "Arizona v. Fulminante", "star_marker": "291"}}
{"assertion_id": "99c6e71ab76d1438", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Arizona v. Fulminante"}, "payload": {"as_of_content": "1991-05-20", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Arizona v. Fulminante", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Arizona v. Fulminante

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arizona v. Fulminante",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Arizona v. Fulminante",
    "case_name_short": "Fulminante",
    "case_name_full": "Arizona v. Fulminante",
    "input_case_name": "Arizona v. Fulminante",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1991-05-20",
    "year": 1991,
    "docket": null,
    "cluster_id": 112566,
    "lead_opinion_id": 112566,
    "sibling_ids": [
      112566,
      9432240,
      9432241,
      9432242
    ],
    "absolute_url": "/opinion/112566/arizona-v-fulminante/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9109110,
        "score": 10,
        "case_name": "Arizona v. Fulminante"
      },
      {
        "cluster_id": 9109109,
        "score": 10,
        "case_name": "Arizona v. Fulminante"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "499 U.S. 279",
      "volume": "499",
      "reporter": "U.S.",
      "page": "279",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "111 S. Ct. 1246",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "1246",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 L. Ed. 2d 302",
        "volume": "113",
        "reporter": "L. Ed. 2d",
        "page": "302",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1991 U.S. LEXIS 1854",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "1854",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "499 U.S. 279",
        "volume": "499",
        "reporter": "U.S.",
        "page": "279",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "111 S. Ct. 1246",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "1246",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 L. Ed. 2d 302",
        "volume": "113",
        "reporter": "L. Ed. 2d",
        "page": "302",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 U.S. LEXIS 1854",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "1854",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "499 U.S. 279",
    "official_selection": {
      "court_class": "scotus",
      "selected": "499 U.S. 279",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-287",
      "page": null,
      "quote": "--- # Arizona v. Fulminante *499 U.S. 279 (1991)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Fulminante was suspected of murdering his stepdaughter. While later incarcerated on an unrelated federal charge, he was befriended by Anthony Sarivola, a fellow inmate who was secretly a paid FBI informant. Knowing Fulminante was receiving rough treatment from other inmates over a rumor that he was a child-killer, Sarivola offered to protect him if he told the truth about the murder. Fulminante confessed to Sarivola, and later to Sarivola's wife. Both confessions were admitted at his murder trial; he was convicted and sentenced to death. ## Issue (1) Whether a confession given out of fear of violence from other inmates, in exchange for an informant's protection, was coerced in violation of due process; and (2) whether the erroneous admission of a coerced confession is subject to harmless-error analysis or instead requires automatic reversal. ## Rule A credible threat of violence can render a confession involuntary \u2014 coercion may be mental, not only physical:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-303",
      "page": null,
      "quote": "The Court today properly concludes that the admission of an 'involuntary' confession at trial is subject to harmless-error analysis.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-309",
      "page": null,
      "quote": "trial error,",
      "star_marker": "291",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 33183,
      "fragment": "#:~:text=though%20a%20%22-,trial%20error%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1991-05-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Arizona v. Fulminante",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Louisiana v. Michael Steven White",
          "cluster_id": 10804933,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Chambers",
          "cluster_id": 10603767,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Chambers",
          "cluster_id": 10591292,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Watt",
          "cluster_id": 9459195,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jenkins v. State",
          "cluster_id": 10680001,
          "cite": [
            "894 S.E.2d 566",
            "317 Ga. 585"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Eric Calvin Tuazon v. the State of Texas",
          "cluster_id": 9380404,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Olano",
          "cluster_id": 112848,
          "cite": [
            "123 L. Ed. 2d 508",
            "113 S. Ct. 1770",
            "507 U.S. 725",
            "1993 U.S. LEXIS 2986"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heck v. Humphrey",
          "cluster_id": 117864,
          "cite": [
            "129 L. Ed. 2d 383",
            "114 S. Ct. 2364",
            "512 U.S. 477",
            "1994 U.S. LEXIS 4824"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rose v. Lee",
          "cluster_id": 773551,
          "cite": [
            "252 F.3d 676",
            "2001 U.S. App. LEXIS 10698",
            "2001 WL 558079"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brecht v. Abrahamson",
          "cluster_id": 112845,
          "cite": [
            "123 L. Ed. 2d 353",
            "113 S. Ct. 1710",
            "507 U.S. 619",
            "1993 U.S. LEXIS 2981"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Puckett v. United States",
          "cluster_id": 145896,
          "cite": [
            "173 L. Ed. 2d 266",
            "129 S. Ct. 1423",
            "556 U.S. 129",
            "2009 U.S. LEXIS 2330"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neder v. United States",
          "cluster_id": 118298,
          "cite": [
            "144 L. Ed. 2d 35",
            "119 S. Ct. 1827",
            "527 U.S. 1",
            "1999 U.S. LEXIS 4007"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mateo",
          "cluster_id": 2006639,
          "cite": [
            "811 N.E.2d 1053",
            "2 N.Y.3d 383",
            "779 N.Y.S.2d 399",
            "2 N.Y. 383",
            "2004 N.Y. LEXIS 263"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. United States",
          "cluster_id": 118106,
          "cite": [
            "137 L. Ed. 2d 718",
            "117 S. Ct. 1544",
            "520 U.S. 461",
            "1997 U.S. LEXIS 2847"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lockhart v. Fretwell",
          "cluster_id": 112807,
          "cite": [
            "122 L. Ed. 2d 180",
            "113 S. Ct. 838",
            "506 U.S. 364",
            "1993 U.S. LEXIS 1016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sullivan v. Louisiana",
          "cluster_id": 112868,
          "cite": [
            "124 L. Ed. 2d 182",
            "113 S. Ct. 2078",
            "508 U.S. 275",
            "1993 U.S. LEXIS 3741"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lewis",
          "cluster_id": 4902617,
          "cite": [
            "281 Cal. Rptr. 3d 521",
            "491 P.3d 309",
            "11 Cal. 5th 952"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gaudin",
          "cluster_id": 117958,
          "cite": [
            "132 L. Ed. 2d 444",
            "115 S. Ct. 2310",
            "515 U.S. 506",
            "1995 U.S. LEXIS 4068"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edwards v. Balisok",
          "cluster_id": 118112,
          "cite": [
            "137 L. Ed. 2d 906",
            "117 S. Ct. 1584",
            "520 U.S. 641",
            "1997 U.S. LEXIS 3075"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dominguez Benitez",
          "cluster_id": 136986,
          "cite": [
            "159 L. Ed. 2d 157",
            "124 S. Ct. 2333",
            "542 U.S. 74",
            "2004 U.S. LEXIS 4177",
            "17 Fla. L. Weekly Fed. S 379",
            "72 U.S.L.W. 4478"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gonzalez-Lopez",
          "cluster_id": 145633,
          "cite": [
            "165 L. Ed. 2d 409",
            "126 S. Ct. 2557",
            "548 U.S. 140",
            "2006 U.S. LEXIS 5165",
            "19 Fla. L. Weekly Fed. S 368",
            "33 A.L.R. Fed. 2d 661",
            "74 U.S.L.W. 4453"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Breverman",
          "cluster_id": 1198942,
          "cite": [
            "960 P.2d 1094",
            "77 Cal. Rptr. 2d 870",
            "19 Cal. 4th 142",
            "98 Cal. Daily Op. Serv. 6812",
            "98 Daily Journal DAR 9358",
            "1998 Cal. LEXIS 5589"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ewing v. California",
          "cluster_id": 127897,
          "cite": [
            "155 L. Ed. 2d 108",
            "123 S. Ct. 1179",
            "538 U.S. 11",
            "2003 U.S. LEXIS 1952"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mickens v. Taylor",
          "cluster_id": 118492,
          "cite": [
            "152 L. Ed. 2d 291",
            "122 S. Ct. 1237",
            "535 U.S. 162",
            "2002 U.S. LEXIS 2146"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bergerud",
          "cluster_id": 2592837,
          "cite": [
            "223 P.3d 686",
            "2010 WL 59254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ward",
          "cluster_id": 2460345,
          "cite": [
            "256 P.3d 801",
            "292 Kan. 541",
            "2011 Kan. LEXIS 249"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Green v. State",
          "cluster_id": 1657475,
          "cite": [
            "934 S.W.2d 92",
            "1996 Tex. Crim. App. LEXIS 185",
            "1996 WL 512395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mendez v. State",
          "cluster_id": 1449351,
          "cite": [
            "138 S.W.3d 334",
            "2004 Tex. Crim. App. LEXIS 1031",
            "2004 WL 1462178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mitchell v. Esparza",
          "cluster_id": 131144,
          "cite": [
            "157 L. Ed. 2d 263",
            "124 S. Ct. 7",
            "540 U.S. 12",
            "2003 U.S. LEXIS 8191"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Washington v. Recuenco",
          "cluster_id": 145631,
          "cite": [
            "165 L. Ed. 2d 466",
            "126 S. Ct. 2546",
            "548 U.S. 212",
            "2006 U.S. LEXIS 5164"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112566 OR 9432240 OR 9432241 OR 9432242) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjc3MTEwNDAwMDAwJnM9OTM4MDQwNCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112566+OR+9432240+OR+9432241+OR+9432242%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 6,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 6,
        "triage_snippet_classified": 194
      },
      "lane2_top_cited": {
        "query": "cites:(112566 OR 9432240 OR 9432241 OR 9432242)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03Mzgmcz00ODkxNDUzJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112566+OR+9432240+OR+9432241+OR+9432242%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112566 OR 9432240 OR 9432241 OR 9432242)",
        "reviewed": 196,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 5,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 196,
        "triage_read": 5,
        "triage_snippet_classified": 191
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112566 OR 9432240 OR 9432241 OR 9432242)",
    "indexed_citing_opinions": 3674,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112566,
        "count": 3108,
        "count_source": "search"
      },
      {
        "opinion_id": 9432240,
        "count": 645,
        "count_source": "search"
      },
      {
        "opinion_id": 9432241,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9432242,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6063,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/arizona-v-fulminante.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0Njc4NDkmcz0xMDY0NDc2NyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28112566+OR+9432240+OR+9432241+OR+9432242%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112566,
        "cited_id": 94082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 101031,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 104010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 104387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 104933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 104997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 107684,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 107952,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108111,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 109631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 109757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 109872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 110038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 110081,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 110138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 110711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 110933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111051,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111726,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 112080,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 112291,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 112298,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 112333,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 112400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 112452,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 375540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 420788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 457158,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 463284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 466083,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 487141,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 1155888,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 1298321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
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
    "date_created": "2026-07-04T18:14:58Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:15:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:15:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:20:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:15:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Arizona v. Fulminante

```
<div>
<center><b><span class="citation" data-id="9432240"><a href="/opinion/112566/arizona-v-fulminante/" aria-description="Citation for case: Arizona v. Fulminante">499 U.S. 279</a></span> (1991)</b></center>
<center><h1>ARIZONA<br>
v.<br>
FULMINANTE</h1></center>
<center>No. 89-839.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued October 10, 1990.</center>
<center>Decided March 26, 1991.</center>
CERTIORARI TO THE SUPREME COURT OF ARIZONA
<p><span class="star-pagination">*281</span> <i>Barbara M. Jarrett,</i> Senior Assistant Attorney General of Arizona, argued the cause for petitioner. With her on the briefs were <i>Robert K. Corbin,</i> Attorney General, and <i>Jessica Gifford Funkhouser.</i></p>
<p><i>Paul J. Larkin, Jr.,</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Starr, Assistant Attorney General Dennis, Deputy Solicitor General Bryson,</i> and <i>Joel M. Gershowitz.</i></p>
<p><i>Stephen R. Collins,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./495/902/">495 U. S. 902</a></span>, argued the cause and filed a brief for respondent.<sup>[*]</sup></p>
<p><span class="star-pagination">*282</span> JUSTICE WHITE delivered an opinion, Parts I, II, and IV of which are the opinion of the Court, and Part III of which is a dissenting opinion.<sup>[]</sup></p>
<p>The Arizona Supreme Court ruled in this case that respondent Oreste Fulminante's confession, received in evidence at his trial for murder, had been coerced and that its use against him was barred by the Fifth and Fourteenth Amendments to the United States Constitution. The court also held that the harmless-error rule could not be used to save the conviction. We affirm the judgment of the Arizona court, although for different reasons than those upon which that court relied.</p>
<p></p>
<h2>I</h2>
<p>Early in the morning of September 14, 1982, Fulminante called the Mesa, Arizona, Police Department to report that his 11-year-old stepdaughter, Jeneane Michelle Hunt, was missing. He had been caring for Jeneane while his wife, Jeneane's mother, was in the hospital. Two days later, Jeneane's body was found in the desert east of Mesa. She had been shot twice in the head at close range with a large caliber weapon, and a ligature was around her neck. Because of the decomposed condition of the body, it was impossible to tell whether she had been sexually assaulted.</p>
<p>Fulminante's statements to police concerning Jeneane's disappearance and his relationship with her contained a number of inconsistencies, and he became a suspect in her killing. When no charges were filed against him, Fulminante left Arizona for New Jersey. Fulminante was later convicted in New Jersey on federal charges of possession of a firearm by a felon.</p>
<p>Fulminante was incarcerated in the Ray Brook Federal Correctional Institution in New York. There he became <span class="star-pagination">*283</span> friends with another inmate, Anthony Sarivola, then serving a 60-day sentence for extortion. The two men came to spend several hours a day together. Sarivola, a former police officer, had been involved in loansharking for organized crime but then became a paid informant for the Federal Bureau of Investigation. While at Ray Brook, he masqueraded as an organized crime figure. After becoming friends with Fulminante, Sarivola heard a rumor that Fulminante was suspected of killing a child in Arizona. Sarivola then raised the subject with Fulminante in several conversations, but Fulminante repeatedly denied any involvement in Jeneane's death. During one conversation, he told Sarivola that Jeneane had been killed by bikers looking for drugs; on another occasion, he said he did not know what had happened. Sarivola passed this information on to an agent of the Federal Bureau of Investigation, who instructed Sarivola to find out more.</p>
<p>Sarivola learned more one evening in October 1983, as he and Fulminante walked together around the prison track. Sarivola said that he knew Fulminante was "starting to get some tough treatment and whatnot" from other inmates because of the rumor. App. 83. Sarivola offered to protect Fulminante from his fellow inmates, but told him, "`You have to tell me about it,' you know. I mean, in other words, `For me to give you any help.'" <i>Ibid.</i> Fulminante then admitted to Sarivola that he had driven Jeneane to the desert on his motorcycle, where he choked her, sexually assaulted her, and made her beg for her life, before shooting her twice in the head. <i>Id.,</i> at 84-85.</p>
<p>Sarivola was released from prison in November 1983. Fulminante was released the following May, only to be arrested the next month for another weapons violation. On September 4, 1984, Fulminante was indicted in Arizona for the first-degree murder of Jeneane.</p>
<p>Prior to trial, Fulminante moved to suppress the statement he had given Sarivola in prison, as well as a second confession <span class="star-pagination">*284</span> he had given to Donna Sarivola, then Anthony Sarivola's fiancée and later his wife, following his May 1984 release from prison. He asserted that the confession to Sarivola was coerced, and that the second confession was the "fruit" of the first. <i>Id.,</i> at 6-8. Following the hearing, the trial court denied the motion to suppress, specifically finding that, based on the stipulated facts, the confessions were voluntary. <i>Id.,</i> at 44, 63. The State introduced both confessions as evidence at trial, and on December 19, 1985, Fulminante was convicted of Jeneane's murder. He was subsequently sentenced to death.</p>
<p>Fulminante appealed, arguing, among other things, that his confession to Sarivola was the product of coercion and that its admission at trial violated his rights to due process under the Fifth and Fourteenth Amendments to the United States Constitution. After considering the evidence at trial as well as the stipulated facts before the trial court on the motion to suppress, the Arizona Supreme Court held that the confession was coerced, but initially determined that the admission of the confession at trial was harmless error, because of the overwhelming nature of the evidence against Fulminante. <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/" aria-description="Citation for case: State v. Fulminante">161 Ariz. 237</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/" aria-description="Citation for case: State v. Fulminante">778 P. 2d 602</a></span> (1988). Upon Fulminante's motion for reconsideration, however, the court ruled that this Court's precedent precluded the use of the harmless-error analysis in the case of a coerced confession. <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#262" aria-description="Citation for case: State v. Fulminante"><i>Id.,</i> at 262</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#627" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 627</a></span>. The court therefore reversed the conviction and ordered that Fulminante be retried without the use of the confession to Sarivola.<sup>[1]</sup> Because of differing <span class="star-pagination">*285</span> views in the state and federal courts over whether the admission at trial of a coerced confession is subject to a harmless-error analysis, we granted the State's petition for certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./494/1055/">494 U. S. 1055</a></span> (1990). Although a majority of this Court finds that such a confession is subject to a harmless-error analysis, for the reasons set forth below, we affirm the judgment of the Arizona court.</p>
<p></p>
<h2>II</h2>
<p>We deal first with the State's contention that the court below erred in holding Fulminante's confession to have been coerced. The State argues that it is the totality of the circumstances that determines whether Fulminante's confession was coerced, cf. <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 226</a></span> (1973), but contends that rather than apply this standard, the Arizona court applied a "but for" test, under which the court found that but for the promise given by Sarivola, Fulminante would not have confessed. Brief for Petitioner 14-15. In support of this argument, the State points to the Arizona court's reference to <i>Bram</i> v. <i>United States,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./168/532/">168 U. S. 532</a></span> (1897). Although the Court noted in <i>Bram</i> that a confession cannot be obtained by "`any direct or implied promises, however slight, nor by the exertion of any improper influence,'" <i>id.,</i> at 542-543 (quoting 3 H. Smith &amp; A. Keep, Russell on Crimes and Misdemeanors 478 (6th ed. 1896)), it is clear that this passage from <i>Bram,</i> which under current precedent does not state the standard for determining the voluntariness of a confession, was not relied on by the Arizona court in reaching its conclusion. Rather, the court cited this language as part of a longer quotation from an Arizona case which accurately described the State's burden of proof for establishing voluntariness. See <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#244" aria-description="Citation for case: State v. Fulminante">161 Ariz., at 244</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 609</a></span> (citing <i>State</i> v. <i>Thomas,</i> <span class="citation" data-id="1155888"><a href="/opinion/1155888/state-v-thomas/#227" aria-description="Citation for case: State v. Thomas">148 Ariz. 225, 227</a></span>, <span class="citation" data-id="1155888"><a href="/opinion/1155888/state-v-thomas/#397" aria-description="Citation for case: State v. Thomas">714 P. 2d 395, 397</a></span> (1986); <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#7" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 7</a></span> (1964); and <i>Bram, supra,</i> at 542-543). Indeed, the Arizona Supreme Court stated that a "determination regarding <span class="star-pagination">*286</span> the voluntariness of a confession . . . must be viewed in a totality of the circumstances," <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#243" aria-description="Citation for case: State v. Fulminante">161 Ariz., at 243</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#608" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 608</a></span>, and under that standard plainly found that Fulminante's statement to Sarivola had been coerced.</p>
<p>In applying the totality of the circumstances test to determine that the confession to Sarivola was coerced, the Arizona Supreme Court focused on a number of relevant facts. First, the court noted that "because [Fulminante] was an alleged child murderer, he was in danger of physical harm at the hands of other inmates." <i><span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/" aria-description="Citation for case: State v. Fulminante">Ibid.</a></span></i> In addition, Sarivola was aware that Fulminante had been receiving "`rough treatment from the guys.'" <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#244" aria-description="Citation for case: State v. Fulminante"><i>Id.,</i> at 244, n. 1</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#609" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 609, n. 1</a></span>. Using his knowledge of these threats, Sarivola offered to protect Fulminante in exchange for a confession to Jeneane's murder, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#243" aria-description="Citation for case: State v. Fulminante"><i>id.,</i> at 243</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#608" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 608</a></span>, and "[i]n response to Sarivola's offer of protection, [Fulminante] confessed." <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#244" aria-description="Citation for case: State v. Fulminante"><i>Id.,</i> at 244</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#609" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 609</a></span>. Agreeing with Fulminante that "Sarivola's promise was `extremely coercive,'" <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#243" aria-description="Citation for case: State v. Fulminante"><i>id.,</i> at 243</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#608" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 608</a></span>, the Arizona court declared: "[T]he confession was obtained as a direct result of extreme coercion and was tendered in the belief that the defendant's life was in jeopardy if he did not confess. This is a true coerced confession in every sense of the word." <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#262" aria-description="Citation for case: State v. Fulminante"><i>Id.,</i> at 262</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#627" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 627</a></span>.<sup>[2]</sup></p>
<p><span class="star-pagination">*287</span> We normally give great deference to the factual findings of the state court. <i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#741" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737, 741</a></span> (1966); <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#515" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503, 515</a></span> (1963); <i>Culombe</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#603" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568, 603-604</a></span> (1961). Nevertheless, "the ultimate issue of `voluntariness' is a legal question requiring independent federal determination." <i>Miller</i> v. <i>Fenton,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#110" aria-description="Citation for case: Miller v. Fenton">474 U. S. 104, 110</a></span> (1985). See also <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#398" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 398</a></span> (1978); <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#741" aria-description="Citation for case: Davis v. North Carolina"><i>Davis, supra,</i> at 741-742</a></span>; <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#515" aria-description="Citation for case: Haynes v. Washington"><i>Haynes, supra,</i> at 515</a></span>; <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#228" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227, 228-229</a></span> (1940).</p>
<p>Although the question is a close one, we agree with the Arizona Supreme Court's conclusion that Fulminante's confession was coerced.<sup>[3]</sup> The Arizona Supreme Court found a credible threat of physical violence unless Fulminante confessed. Our cases have made clear that a finding of coercion need not depend upon actual violence by a government agent;<sup>[4]</sup> a credible threat is sufficient. As we have said, "coercion can be mental as well as physical, and . . . the blood of the accused is not the only hallmark of an unconstitutional inquisition." <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 206</a></span> (1960). See also <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#584" aria-description="Citation for case: Culombe v. Connecticut"><i>Culombe, supra,</i> at 584</a></span>; <i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/#440" aria-description="Citation for case: Reck v. Pate">367 U. S. 433, 440-441</a></span> (1961); <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#540" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 540</a></span> (1961); <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span>, 561 <span class="star-pagination">*288</span> (1958); <i>Watts</i> v. <i>Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#52" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 52</a></span> (1949). As in <i><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">Payne</a></span>,</i> where the Court found that a confession was coerced because the interrogating police officer had promised that if the accused confessed, the officer would protect the accused from an angry mob outside the jailhouse door, <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#564" aria-description="Citation for case: Payne v. Arkansas">356 U. S., at 564-565, 567</a></span>, so too here, the Arizona Supreme Court found that it was fear of physical violence, absent protection from his friend (and Government agent) Sarivola, which motivated Fulminante to confess. Accepting the Arizona court's finding, permissible on this record, that there was a credible threat of physical violence, we agree with its conclusion that Fulminante's will was overborne in such a way as to render his confession the product of coercion.</p>
<p></p>
<h2>III</h2>
<p>Four of us, JUSTICES MARSHALL, BLACKMUN, STEVENS, and myself, would affirm the judgment of the Arizona Supreme Court on the ground that the harmless-error rule is inapplicable to erroneously admitted coerced confessions. We thus disagree with the Justices who have a contrary view.</p>
<p>The majority today abandons what until now the Court has regarded as the "axiomatic [proposition] that a defendant in a criminal case is deprived of due process of law if his conviction is founded, in whole or in part, upon an involuntary confession, without regard for the truth or falsity of the confession, <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534</a></span> [(1961)], and even though there is ample evidence aside from the confession to support the conviction. <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span> [(1945)]; <i>Stroble</i> v. <i>California,</i> <span class="citation" data-id="9420722"><a href="/opinion/104997/stroble-v-california/" aria-description="Citation for case: Stroble v. California">343 U. S. 181</a></span> [(1952)]; <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span>." <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#376" aria-description="Citation for case: Jackson v. Denno">378 U. S. 368, 376</a></span> (1964). The Court has repeatedly stressed that the view that the admission of a coerced confession can be harmless error because of the other evidence to support the verdict is "an impermissible doctrine," <i>Lynumn</i> v. <i>Illinois,</i> <span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/#537" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528, 537</a></span> (1963); for "the admission in evidence, <span class="star-pagination">*289</span> over objection, of the coerced confession vitiates the judgment because it violates the Due Process Clause of the Fourteenth Amendment," <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#568" aria-description="Citation for case: Payne v. Arkansas"><i>Payne, supra,</i> at 568</a></span>. See also <i>Rose</i> v. <i>Clark,</i> <span class="citation" data-id="9430690"><a href="/opinion/111750/rose-v-clark/#578" aria-description="Citation for case: Rose v. Clark">478 U. S. 570, 578, n. 6</a></span> (1986); <i>New Jersey</i> v. <i>Portash,</i> <span class="citation" data-id="9427490"><a href="/opinion/110038/new-jersey-v-portash/#459" aria-description="Citation for case: New Jersey v. Portash">440 U. S. 450, 459</a></span> (1979); <i>Lego</i> v. <i>Twomey,</i> <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#483" aria-description="Citation for case: Lego v. Twomey">404 U. S. 477, 483</a></span> (1972); <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#23" aria-description="Citation for case: Chapman v. California">386 U. S. 18, 23</a></span>, and n. 8 (1967); <i>Haynes</i> v. <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#518" aria-description="Citation for case: Haynes v. Washington"><i>Washington, supra,</i> at 518</a></span>; <i>Blackburn</i> v. <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama"><i>Alabama, supra,</i> at 206</a></span>; <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#324" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 324</a></span> (1959); <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#475" aria-description="Citation for case: Brown v. Allen">344 U. S. 443, 475</a></span> (1953); <i>Stroble</i> v. <i>California,</i> <span class="citation" data-id="9420722"><a href="/opinion/104997/stroble-v-california/#190" aria-description="Citation for case: Stroble v. California">343 U. S. 181, 190</a></span> (1952); <i>Gallegos</i> v. <i>Nebraska,</i> <span class="citation" data-id="9420632"><a href="/opinion/104933/gallegos-v-nebraska/#63" aria-description="Citation for case: Gallegos v. Nebraska">342 U. S. 55, 63</a></span> (1951); <i>Haley</i> v. <i>Ohio,</i> <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/#599" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596, 599</a></span> (1948); <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#404" aria-description="Citation for case: Malinski v. New York">324 U. S. 401, 404</a></span> (1945); <i>Lyons</i> v. <i>Oklahoma,</i> <span class="citation" data-id="9419526"><a href="/opinion/104010/lyons-v-oklahoma/#597" aria-description="Citation for case: Lyons v. Oklahoma">322 U. S. 596, 597, n. 1</a></span> (1944). As the decisions in <i><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">Haynes</a></span></i> and <i><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">Payne, supra,</a></span></i> show, the rule was the same even when another confession of the defendant had been properly admitted into evidence. Today, a majority of the Court, without any justification, cf. <i>Arizona</i> v. <i>Rumsey,</i> <span class="citation" data-id="9842058"><a href="/opinion/111194/arizona-v-rumsey/#212" aria-description="Citation for case: Arizona v. Rumsey">467 U. S. 203, 212</a></span> (1984), overrules this vast body of precedent without a word and in so doing dislodges one of the fundamental tenets of our criminal justice system.</p>
<p>In extending to coerced confessions the harmless-error rule of <i>Chapman</i> v. <i>California, supra</i><i>,</i> the majority declares that because the Court has applied that analysis to numerous other "trial errors," there is no reason that it should not apply to an error of this nature as well. The four of us remain convinced, however, that we should abide by our cases that have refused to apply the harmless-error rule to coerced confessions, for a coerced confession is fundamentally different from other types of erroneously admitted evidence to which the rule has been applied. Indeed, as the majority concedes, <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span></i> itself recognized that prior cases "have indicated that there are some constitutional rights so basic to a fair trial that their infraction can <i>never</i> be treated as harmless error," and it placed in that category the constitutional rule against using a defendant's coerced confession against <span class="star-pagination">*290</span> him at his criminal trial. <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#23" aria-description="Citation for case: Chapman v. California">386 U. S., at 23</a></span>, and n. 8 (emphasis added). Moreover, cases since <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span></i> have reiterated the rule that using a defendant's coerced confession against him is a denial of due process of law regardless of the other evidence in the record aside from the confession. <i>Lego</i> v. <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#483" aria-description="Citation for case: Lego v. Twomey"><i>Twomey, supra,</i> at 483</a></span>; <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#398" aria-description="Citation for case: Mincey v. Arizona">437 U. S., at 398</a></span>; <i>New Jersey</i> v. <span class="citation" data-id="9427490"><a href="/opinion/110038/new-jersey-v-portash/#459" aria-description="Citation for case: New Jersey v. Portash"><i>Portash, supra,</i> at 459</a></span>; <i>Rose</i> v. <span class="citation" data-id="9430690"><a href="/opinion/111750/rose-v-clark/#577" aria-description="Citation for case: Rose v. Clark"><i>Clark, supra,</i> at 577, 578</a></span>, and n. 6.</p>
<p><i>Chapman</i> specifically noted three constitutional errors that could not be categorized as harmless error: using a coerced confession against a defendant in a criminal trial, depriving a defendant of counsel, and trying a defendant before a biased judge. The majority attempts to distinguish the use of a coerced confession from the other two errors listed in <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span></i> first by distorting the decision in <i><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">Payne</a></span>,</i> and then by drawing a meaningless dichotomy between "trial errors" and "structural defects" in the trial process. Viewing <i><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">Payne</a></span></i> as merely rejecting a test whereby the admission of a coerced confession could stand if there were "sufficient evidence," other than the confession, to support the conviction, the majority suggests that the Court in <i><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">Payne</a></span></i> might have reached a different result had it been considering a harmless-error test. <i>Post,</i> at 309 (opinion of REHNQUIST, C. J.). It is clear, though, that in <i><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">Payne</a></span></i> the Court recognized that <i>regardless</i> of the amount of other evidence, "the admission in evidence, over objection, of the coerced confession vitiates the judgment," because "where, as here, a coerced confession constitutes a part of the evidence before the jury and a general verdict is returned, no one can say what credit and weight the jury gave to the confession." <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#568" aria-description="Citation for case: Payne v. Arkansas">356 U. S., at 568</a></span>. The inability to assess its effect on a conviction causes the admission at trial of a coerced confession to "defy analysis by `harmless-error' standards," cf. <i>post,</i> at 309 (opinion of REHNQUIST, C. J.), just as certainly as do deprivation of counsel and trial before a biased judge.</p>
<p><span class="star-pagination">*291</span> The majority also attempts to distinguish "trial errors" which occur "during the presentation of the case to the jury," <i>post,</i> at 307, and which it deems susceptible to harmless-error analysis, from "structural defects in the constitution of the trial mechanism," <i>post,</i> at 309, which the majority concedes cannot be so analyzed. This effort fails, for our jurisprudence on harmless error has not classified so neatly the errors at issue. For example, we have held susceptible to harmless-error analysis the failure to instruct the jury on the presumption of innocence, <i>Kentucky</i> v. <i>Whorton,</i> <span class="citation" data-id="9427578"><a href="/opinion/110081/kentucky-v-whorton/" aria-description="Citation for case: Kentucky v. Whorton">441 U. S. 786</a></span> (1979), while finding it impossible to analyze in terms of harmless error the failure to instruct a jury on the reasonable-doubt standard, <i>Jackson</i> v. <i>Virginia,</i> <span class="citation" data-id="9427680"><a href="/opinion/110138/jackson-v-virginia/#320" aria-description="Citation for case: Jackson v. Virginia">443 U. S. 307, 320, n. 14</a></span> (1979). These cases cannot be reconciled by labeling the former "trial error" and the latter not, for both concern the exact same stage in the trial proceedings. Rather, these cases can be reconciled only by considering the nature of the right at issue and the effect of an error upon the trial. A jury instruction on the presumption of innocence is not constitutionally required in every case to satisfy due process, because such an instruction merely offers an additional safeguard beyond that provided by the constitutionally required instruction on reasonable doubt. See <span class="citation" data-id="9427578"><a href="/opinion/110081/kentucky-v-whorton/#789" aria-description="Citation for case: Kentucky v. Whorton"><i>Whorton, supra,</i> at 789</a></span>; <i>Taylor</i> v. <i>Kentucky,</i> <span class="citation" data-id="9427215"><a href="/opinion/109872/taylor-v-kentucky/#488" aria-description="Citation for case: Taylor v. Kentucky">436 U. S. 478, 488-490</a></span> (1978). While it may be possible to analyze as harmless the omission of a presumption of innocence instruction when the required reasonable-doubt instruction has been given, it is impossible to assess the effect on the jury of the omission of the more fundamental instruction on reasonable doubt. In addition, omission of a reasonable-doubt instruction, though a "trial error," distorts the very structure of the trial because it creates the risk that the jury will convict the defendant even if the State has not met its required burden of proof. Cf. <i>Cool</i> v. <i>United States,</i> <span class="citation" data-id="9425051"><a href="/opinion/108635/cool-v-united-states/#104" aria-description="Citation for case: Cool v. United States">409 U. S. 100, 104</a></span> (1972); <i>In re Winship,</i> <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#364" aria-description="Citation for case: In Re WINSHIP">397 U. S. 358, 364</a></span> (1970).</p>
<p><span class="star-pagination">*292</span> These same concerns counsel against applying harmless-error analysis to the admission of a coerced confession. A defendant's confession is "probably the most probative and damaging evidence that can be admitted against him," <i>Cruz</i> v. <i>New York,</i> <span class="citation" data-id="9430920"><a href="/opinion/111864/cruz-v-new-york/#195" aria-description="Citation for case: Cruz v. New York">481 U. S. 186, 195</a></span> (1987) (WHITE, J., dissenting), so damaging that a jury should not be expected to ignore it even if told to do so, <i>Bruton</i> v. <i>United States,</i> <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/#140" aria-description="Citation for case: Bruton v. United States">391 U. S. 123, 140</a></span> (1968) (WHITE, J., dissenting), and because in any event it is impossible to know what credit and weight the jury gave to the confession. Cf. <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#568" aria-description="Citation for case: Payne v. Arkansas"><i>Payne, supra,</i> at 568</a></span>. Concededly, this reason is insufficient to justify a <i>per se</i> bar to the use of <i>any</i> confession. Thus, <i>Milton</i> v. <i>Wainwright,</i> <span class="citation" data-id="9424959"><a href="/opinion/108585/milton-v-wainwright/" aria-description="Citation for case: Milton v. Wainwright">407 U. S. 371</a></span> (1972), applied harmless-error analysis to a confession obtained and introduced in circumstances that violated the defendant's Sixth Amendment right to counsel.<sup>[5]</sup> Similarly, the Courts of Appeals have held that the introduction of incriminating statements taken from defendants in violation of <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), is subject to treatment as harmless error.<sup>[6]</sup></p>
<p>Nevertheless, in declaring that it is "impossible to create a meaningful distinction between confessions elicited in violation of the Sixth Amendment and those in violation of the Fourteenth Amendment," <i>post,</i> at 312 (opinion of REHNQUIST, C. J.), the majority overlooks the obvious. Neither <i>Milton</i> v. <i><span class="citation" data-id="9424959"><a href="/opinion/108585/milton-v-wainwright/" aria-description="Citation for case: Milton v. Wainwright">Wainwright</a></span></i> nor any of the other cases upon which <span class="star-pagination">*293</span> the majority relies involved a defendant's <i>coerced</i> confession, nor were there present in these cases the distinctive reasons underlying the exclusion of coerced incriminating statements of the defendant.<sup>[7]</sup> First, some coerced confessions may be untrustworthy. <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#385" aria-description="Citation for case: Jackson v. Denno">378 U. S., at 385-386</a></span>; <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#320" aria-description="Citation for case: Spano v. New York">360 U. S., at 320</a></span>. Consequently, admission of coerced confessions may distort the truth-seeking function of the trial upon which the majority focuses. More importantly, however, the use of coerced confessions, "whether true or false," is forbidden "because the methods used to extract them offend an underlying principle in the enforcement of our criminal law: that ours is an accusatorial and not an inquisitorial system  a system in which the State must establish guilt by evidence independently and freely secured and may not by coercion prove its charge against an accused out of his own mouth," <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#540" aria-description="Citation for case: Rogers v. Richmond">365 U. S., at 540-541</a></span>; see also <i>Lego,</i> <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#485" aria-description="Citation for case: Lego v. Twomey">404 U. S., at 485</a></span>. This reflects the "strongly felt attitude of our society that important human values are sacrificed where an agency of the government, in the course of securing a conviction, wrings a confession out of an accused against his will," <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama">361 U. S., at 206-207</a></span>, as well as "the deep-rooted feeling that the police must obey the law while enforcing the law; that in the end life and liberty can be as much endangered from illegal methods used to convict those thought to be criminals as from the actual criminals themselves," <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#320" aria-description="Citation for case: Spano v. New York"><i>Spano, supra,</i> at 320-321</a></span>. Thus, permitting a coerced confession to be part of the evidence on which a jury is free to base its verdict of guilty is inconsistent with the thesis that ours is not an <span class="star-pagination">*294</span> inquisitorial system of criminal justice. Cf. <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#235" aria-description="Citation for case: Chambers v. Florida">309 U. S., at 235-238</a></span>.</p>
<p>As the majority concedes, there are other constitutional errors that invalidate a conviction even though there may be no reasonable doubt that the defendant is guilty and would be convicted absent the trial error. For example, a judge in a criminal trial "is prohibited from entering a judgment of conviction or directing the jury to come forward with such a verdict, see <i>Sparf &amp; Hansen</i> v. <i>United States,</i> <span class="citation" data-id="9417675"><a href="/opinion/94082/sparf-v-united-states/#105" aria-description="Citation for case: Sparf v. United States">156 U. S. 51, 105</a></span> (1895); <i>Carpenters</i> v. <i>United States,</i> <span class="citation" data-id="9419949"><a href="/opinion/104387/united-brotherhood-of-carpenters-joiners-of-america-v-united-states/#408" aria-description="Citation for case: United Brotherhood of Carpenters &amp; Joiners of America v....">330 U. S. 395, 408</a></span> (1947), regardless of how overwhelmingly the evidence may point in that direction." <i>United States</i> v. <i>Martin Linen Supply Co.,</i> <span class="citation" data-id="9426742"><a href="/opinion/109631/united-states-v-martin-linen-supply-co/#572" aria-description="Citation for case: United States v. Martin Linen Supply Co.">430 U. S. 564, 572-573</a></span> (1977). A defendant is entitled to counsel at trial, <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span> (1963), and as <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span></i> recognized, violating this right can never be harmless error. <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#23" aria-description="Citation for case: Chapman v. California">386 U. S., at 23</a></span>, and n. 8. See also <i>White</i> v. <i>Maryland,</i> <span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span> (1963), where a conviction was set aside because the defendant had not had counsel at a preliminary hearing without regard to the showing of prejudice. In <i>Vasquez</i> v. <i>Hillery,</i> <span class="citation" data-id="9430252"><a href="/opinion/111552/vasquez-v-hillery/" aria-description="Citation for case: Vasquez v. Hillery">474 U. S. 254</a></span> (1986), a defendant was found guilty beyond reasonable doubt, but the conviction had been set aside because of the unlawful exclusion of members of the defendant's race from the grand jury that indicted him, despite overwhelming evidence of his guilt. The error at the grand jury stage struck at fundamental values of our society and "undermine[d] the structural integrity of the criminal tribunal itself, and [was] not amenable to harmless-error review." <span class="citation" data-id="9430252"><a href="/opinion/111552/vasquez-v-hillery/#263" aria-description="Citation for case: Vasquez v. Hillery"><i>Id.,</i> at 263-264</a></span>. <i><span class="citation" data-id="9430252"><a href="/opinion/111552/vasquez-v-hillery/" aria-description="Citation for case: Vasquez v. Hillery">Vasquez</a></span>,</i> like <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span>,</i> also noted that rule of automatic reversal when a defendant is tried before a judge with a financial interest in the outcome, <i>Tumey</i> v. <i>Ohio,</i> <span class="citation" data-id="101031"><a href="/opinion/101031/tumey-v-ohio/#535" aria-description="Citation for case: Tumey v. Ohio">273 U. S. 510, 535</a></span> (1927), despite a lack of any indication that bias influenced the decision. <i>Waller</i> v. <i>Georgia,</i> <span class="citation" data-id="111186"><a href="/opinion/111186/waller-v-georgia/#49" aria-description="Citation for case: Waller v. Georgia">467 U. S. 39, 49</a></span> (1984), recognized that violation of the guarantee of a public trial required reversal without any showing of prejudice and even though the values <span class="star-pagination">*295</span> of a public trial may be intangible and unprovable in any particular case.</p>
<p>The search for truth is indeed central to our system of justice, but "certain constitutional rights are not, and should not be, subject to harmless-error analysis because those rights protect important values that are unrelated to the truth-seeking function of the trial." <i>Rose</i> v. <i>Clark,</i> <span class="citation" data-id="9430690"><a href="/opinion/111750/rose-v-clark/#587" aria-description="Citation for case: Rose v. Clark">478 U. S., at 587</a></span> (STEVENS, J., concurring in judgment). The right of a defendant not to have his coerced confession used against him is among those rights, for using a coerced confession "abort[s] the basic trial process" and "render[s] a trial fundamentally unfair." <span class="citation" data-id="9430690"><a href="/opinion/111750/rose-v-clark/#577" aria-description="Citation for case: Rose v. Clark"><i>Id.,</i> at 577, 578, n. 6</a></span>.</p>
<p>For the foregoing reasons the four of us would adhere to the consistent line of authority that has recognized as a basic tenet of our criminal justice system, before and after both <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span>,</i> the prohibition against using a defendant's coerced confession against him at his criminal trial. <i>Stare decisis</i> is "of fundamental importance to the rule of law," <i>Welch</i> v. <i>Texas Dept. of Highways and Public Transportation,</i> <span class="citation" data-id="9431106"><a href="/opinion/111949/welch-v-texas-department-of-highways-public-transportation/#494" aria-description="Citation for case: Welch v. Texas Department of Highways &amp; Public...">483 U. S. 468, 494</a></span> (1987); the majority offers no convincing reason for overturning our long line of decisions requiring the exclusion of coerced confessions.</p>
<p></p>
<h2>IV</h2>
<p>Since five Justices have determined that harmless-error analysis applies to coerced confessions, it becomes necessary to evaluate under that ruling the admissibility of Fulminante's confession to Sarivola. Cf. <i>Pennsylvania</i> v. <i>Union Gas Co.,</i> <span class="citation" data-id="9431727"><a href="/opinion/112291/pennsylvania-v-union-gas-co/#45" aria-description="Citation for case: Pennsylvania v. Union Gas Co.">491 U. S. 1, 45</a></span> (1989) (WHITE, J., concurring in judgment in part and dissenting in part); <span class="citation" data-id="9431727"><a href="/opinion/112291/pennsylvania-v-union-gas-co/#57" aria-description="Citation for case: Pennsylvania v. Union Gas Co."><i>id.,</i> at 57</a></span> (O'CONNOR, J., dissenting). <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#24" aria-description="Citation for case: Chapman v. California">386 U. S., at 24</a></span>, made clear that "before a federal constitutional error can be held harmless, the court must be able to declare a belief that it was harmless beyond a reasonable doubt." The Court has the power to review the record <i>de novo</i> in order to determine an error's harmlessness. See <i>ibid.; </i><i>Satterwhite</i> v. <span class="star-pagination">*296</span> <i>Texas,</i> 486 U. S., at 258. In so doing, it must be determined whether the State has met its burden of demonstrating that the admission of the confession to Sarivola did not contribute to Fulminante's conviction. <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#26" aria-description="Citation for case: Chapman v. California"><i>Chapman, supra,</i> at 26</a></span>. Five of us are of the view that the State has not carried its burden and accordingly affirm the judgment of the court below reversing respondent's conviction.</p>
<p>A confession is like no other evidence. Indeed, "the defendant's own confession is probably the most probative and damaging evidence that can be admitted against him. . . . [T]he admissions of a defendant come from the actor himself, the most knowledgeable and unimpeachable source of information about his past conduct. Certainly, confessions have profound impact on the jury, so much so that we may justifiably doubt its ability to put them out of mind even if told to do so." <i>Bruton</i> v. <i>United States,</i> <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/#139" aria-description="Citation for case: Bruton v. United States">391 U. S., at 139-140</a></span> (WHITE, J., dissenting). See also <i>Cruz</i> v. <i>New York,</i> <span class="citation" data-id="9430920"><a href="/opinion/111864/cruz-v-new-york/#195" aria-description="Citation for case: Cruz v. New York">481 U. S., at 195</a></span> (WHITE, J., dissenting) (citing <i><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></i>). While some statements by a defendant may concern isolated aspects of the crime or may be incriminating only when linked to other evidence, a full confession in which the defendant discloses the motive for and means of the crime may tempt the jury to rely upon that evidence alone in reaching its decision. In the case of a coerced confession such as that given by Fulminante to Sarivola, the risk that the confession is unreliable, coupled with the profound impact that the confession has upon the jury, requires a reviewing court to exercise extreme caution before determining that the admission of the confession at trial was harmless.</p>
<p>In the Arizona Supreme Court's initial opinion, in which it determined that harmless-error analysis could be applied to the confession, the court found that the admissible second confession to Donna Sarivola rendered the first confession to Anthony Sarivola cumulative. <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#245" aria-description="Citation for case: State v. Fulminante">161 Ariz., at 245-246</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#610" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 610-611</a></span>. The court also noted that circumstantial physical evidence concerning the wounds, the ligature around Jeneane's neck, the location of the body, and the presence of <span class="star-pagination">*297</span> motorcycle tracks at the scene corroborated the second confession. <i><span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/" aria-description="Citation for case: State v. Fulminante">Ibid.</a></span></i> The court concluded that "due to the overwhelming evidence adduced from the second confession, if there had not been a first confession, the jury would still have had the same basic evidence to convict" Fulminante. <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#246" aria-description="Citation for case: State v. Fulminante"><i>Id.,</i> at 246</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#611" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 611</a></span>.</p>
<p>We have a quite different evaluation of the evidence. Our review of the record leads us to conclude that the State has failed to meet its burden of establishing, beyond a reasonable doubt, that the admission of Fulminante's confession to Anthony Sarivola was harmless error. Three considerations compel this result.</p>
<p>First, the transcript discloses that both the trial court and the State recognized that a successful prosecution depended on the jury believing the two confessions. Absent the confessions, it is unlikely that Fulminante would have been prosecuted at all, because the physical evidence from the scene and other circumstantial evidence would have been insufficient to convict. Indeed, no indictment was filed until nearly two years after the murder.<sup>[8]</sup> App. 2. Although the police had suspected Fulminante from the beginning, as the prosecutor acknowledged in his opening statement to the jury, "[W]hat brings us to Court, what makes this case fileable, and prosecutable and triable is that later, Mr. Fulminante confesses this crime to Anthony Sarivola and later, to Donna Sarivola, his wife." <i>Id.,</i> at 65-66. After trial began, during a renewed hearing on Fulminante's motion to suppress, the trial court opined, "You know, I think from what little I know about this trial, the character of this man [Sarivola] for truthfulness or untruthfulness and his credibility is the centerpiece of this case, is it not?" The prosecutor responded, "It's very important, there's no doubt." <i>Id.,</i> at 62. Finally, in his <span class="star-pagination">*298</span> closing argument, the prosecutor prefaced his discussion of the two confessions by conceding: "[W]e have a lot of [circumstantial] evidence that indicates that this is our suspect, this is the fellow that did it, but it's a little short as far as saying that it's proof that he actually put the gun to the girl's head and killed her. So it's a little short of that. We recognize that." 10 Tr. 75 (Dec. 17, 1985).</p>
<p>Second, the jury's assessment of the confession to Donna Sarivola could easily have depended in large part on the presence of the confession to Anthony Sarivola. Absent the admission at trial of the first confession, the jurors might have found Donna Sarivola's story unbelievable. Fulminante's confession to Donna Sarivola allegedly occurred in May 1984, on the day he was released from Ray Brook, as she and Anthony Sarivola drove Fulminante from New York to Pennsylvania. Donna Sarivola testified that Fulminante, whom she had never before met, confessed in detail about Jeneane's brutal murder in response to her casual question concerning why he was going to visit friends in Pennsylvania instead of returning to his family in Arizona. App. 167-168. Although she testified that she was "disgusted" by Fulminante's disclosures, <i>id.,</i> at 169, she stated that she took no steps to notify authorities of what she had learned, <i>id.,</i> at 172-173. In fact, she claimed that she barely discussed the matter with Anthony Sarivola, who was in the car and overheard Fulminante's entire conversation with Donna. <i>Id.,</i> at 174-175. Despite her disgust for Fulminante, Donna Sarivola later went on a second trip with him. <i>Id.,</i> at 173-174. Although Sarivola informed authorities that he had driven Fulminante to Pennsylvania, he did not mention Donna's presence in the car or her conversation with Fulminante. <i>Id.,</i> at 159-161. Only when questioned by authorities in June 1985 did Anthony Sarivola belatedly recall the confession to Donna more than a year before, and only then did he ask if she would be willing to discuss the matter with authorities. <i>Id.,</i> at 90-92.</p>
<p><span class="star-pagination">*299</span> Although some of the details in the confession to Donna Sarivola were corroborated by circumstantial evidence, many, including details that Jeneane was choked and sexually assaulted, were not. <i>Id.,</i> at 186-188. As to other aspects of the second confession, including Fulminante's motive and state of mind, the <i>only</i> corroborating evidence was the first confession to Anthony Sarivola.<sup>[9]</sup> No. CR 142821 (Super. Ct. Maricopa County, Ariz., Feb. 11, 1986), pp. 3-4. Thus, contrary to what the Arizona Supreme Court found, it is clear that the jury might have believed that the two confessions reinforced and corroborated each other. For this reason, one confession was <i>not</i> merely cumulative of the other. While in some cases two confessions, delivered on different occasions to different listeners, might be viewed as being independent of each other, cf. <i>Milton</i> v. <i>Wainwright,</i> <span class="citation" data-id="9424959"><a href="/opinion/108585/milton-v-wainwright/" aria-description="Citation for case: Milton v. Wainwright">407 U. S. 371</a></span> (1972), it strains credulity to think that the jury so viewed the two confessions in this case, especially given the close relationship between Donna and Anthony Sarivola.</p>
<p><span class="star-pagination">*300</span> The jurors could also have believed that Donna Sarivola had a motive to lie about the confession in order to assist her husband. Anthony Sarivola received significant benefits from federal authorities, including payment for information, immunity from prosecution, and eventual placement in the federal Witness Protection Program. App. 79, 114, 129-131. In addition, the jury might have found Donna motivated by her own desire for favorable treatment, for she, too, was ultimately placed in the Witness Protection Program. <i>Id.,</i> at 176, 179-180.</p>
<p>Third, the admission of the first confession led to the admission of other evidence prejudicial to Fulminante. For example, the State introduced evidence that Fulminante knew of Sarivola's connections with organized crime in an attempt to explain why Fulminante would have been motivated to confess to Sarivola in seeking protection. <i>Id.,</i> at 45-48, 67. Absent the confession, this evidence would have had no relevance and would have been inadmissible at trial. The Arizona Supreme Court found that the evidence of Sarivola's connections with organized crime reflected on Sarivola's character, not Fulminante's, and noted that the evidence could have been used to impeach Sarivola. <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#245" aria-description="Citation for case: State v. Fulminante">161 Ariz., at 245-246</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#610" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 610-611</a></span>. This analysis overlooks the fact that had the confession not been admitted, there would have been no reason for Sarivola to testify and thus no need to impeach his testimony. Moreover, we cannot agree that the evidence did not reflect on Fulminante's character as well, for it depicted him as someone who willingly sought out the company of criminals. It is quite possible that this evidence led the jury to view Fulminante as capable of murder.<sup>[10]</sup></p>
<p><span class="star-pagination">*301</span> Finally, although our concern here is with the effect of the erroneous admission of the confession on Fulminante's conviction, it is clear that the presence of the confession also influenced the sentencing phase of the trial. Under Arizona law, the trial judge is the sentencer. <span class="citation no-link">Ariz. Rev. Stat. Ann. § 13-703</span>(B) (1989). At the sentencing hearing, the admissibility of information regarding aggravating circumstances is governed by the rules of evidence applicable to criminal trials. § 13-703(C). In this case, "based upon admissible evidence produced at the trial," No. CR 142821, <i>supra,</i> at 2, the judge found that only one aggravating circumstance existed beyond a reasonable doubt, <i>i. e.,</i> that the murder was committed in "an <i>especially</i> heinous, cruel, and depraved manner." <i>Ibid.;</i> see § 13-703(F)(6). In reaching this conclusion, the judge relied heavily on evidence concerning the manner of the killing and Fulminante's motives and state of mind which could only be found in the two confessions. For example, in labeling the murder "cruel," the judge focused in part on Fulminante's alleged statements that he choked Jeneane and made her get on her knees and beg before killing her. No. CR 142821, <i>supra,</i> at 3. Although the circumstantial evidence was not inconsistent with this determination, neither was it sufficient to make such a finding beyond a reasonable doubt. Indeed, the sentencing judge acknowledged that the confessions were only partly corroborated by other evidence. <i>Ibid.</i></p>
<p>In declaring that Fulminante "acted with an especially heinous and depraved state of mind," the sentencing judge relied solely on the two confessions. <i>Id.,</i> at 4. While the judge found that the statements in the confessions regarding the alleged sexual assault on Jeneane should not be considered on the issue of cruelty because they were not corroborated by other evidence, the judge determined that they were worthy of belief on the issue of Fulminante's state of <span class="star-pagination">*302</span> mind. <i>Ibid.</i> The judge then focused on Anthony Sarivola's statement that Fulminante had made vulgar references to Jeneane during the first confession, and on Donna Sarivola's statement that Fulminante had made similar comments to her. <i>Ibid.</i> Finally, the judge stressed that Fulminante's alleged comments to the Sarivolas concerning torture, choking, and sexual assault, "whether they all occurred or not," <i>ibid.,</i> depicted "a man who was bragging and relishing the crime he committed." <i>Id.,</i> at 5.</p>
<p>Although the sentencing judge might have reached the same conclusions even without the confession to Anthony Sarivola, it is impossible to say so beyond a reasonable doubt. Furthermore, the judge's assessment of Donna Sarivola's credibility, and hence the reliability of the second confession, might well have been influenced by the corroborative effect of the erroneously admitted first confession. Indeed, the fact that the sentencing judge focused on the similarities between the two confessions in determining that they were reliable suggests that either of the confessions alone, even when considered with all the other evidence, would have been insufficient to permit the judge to find an aggravating circumstance beyond a reasonable doubt as a requisite prelude to imposing the death penalty.</p>
<p>Because a majority of the Court has determined that Fulminante's confession to Anthony Sarivola was coerced and because a majority has determined that admitting this confession was not harmless beyond a reasonable doubt, we agree with the Arizona Supreme Court's conclusion that Fulminante is entitled to a new trial at which the confession is not admitted. Accordingly the judgment of the Arizona Supreme Court is</p>
<p><i>Affirmed.</i></p>
<p>CHIEF JUSTICE REHNQUIST, with whom JUSTICE O'CONNOR joins, JUSTICE KENNEDY and JUSTICE SOUTER join as to Parts I and II, and JUSTICE SCALIA joins as to Parts II and <span class="star-pagination">*303</span> III, delivered the opinion of the Court with respect to Part II, and a dissenting opinion with respect to Parts I and III.</p>
<p>The Court today properly concludes that the admission of an "involuntary" confession at trial is subject to harmless-error analysis. Nonetheless, the independent review of the record which we are required to make shows that respondent Fulminante's confession was not in fact involuntary. And even if the confession were deemed to be involuntary, the evidence offered at trial, including a second, untainted confession by Fulminante, supports the conclusion that any error here was certainly harmless.</p>
<p></p>
<h2>I</h2>
<p>The question whether respondent Fulminante's confession was voluntary is one of federal law. "Without exception, the Court's confession cases hold that the ultimate issue of `voluntariness' is a legal question requiring independent federal determination." <i>Miller</i> v. <i>Fenton,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#110" aria-description="Citation for case: Miller v. Fenton">474 U. S. 104, 110</a></span> (1985). In <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span> (1978), we overturned a determination by the Supreme Court of Arizona that a statement of the defendant was voluntary, saying "we are not bound by the Arizona Supreme Court's holding that the statements were voluntary. Instead, this Court is under a duty to make an independent evaluation of the record." <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#398" aria-description="Citation for case: Mincey v. Arizona"><i>Id.,</i> at 398</a></span>.</p>
<p>The admissibility of a confession such as that made by respondent Fulminante depends upon whether it was voluntarily made. "The ultimate test remains that which has been the only clearly established test in Anglo-American courts for two hundred years: the test of voluntariness. Is the confession the product of an essentially free and unconstrained choice by its maker? If it is, if he has willed to confess, it may be used against him. If it is not, if his will has been overborne and his capacity for self-determination critically impaired, the use of his confession offends due process." <span class="star-pagination">*304</span> <i>Culombe</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#602" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568, 602</a></span> (1961) (quoted in <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#225" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 225-226</a></span> (1973)).</p>
<p>In this case the parties stipulated to the basic facts at the hearing in the Arizona trial court on respondent's motion to suppress the confession. Anthony Sarivola, an inmate at the Ray Brook Prison, was a paid confidential informant for the FBI. While at Ray Brook, various rumors reached Sarivola that Oreste Fulminante, a fellow inmate who had befriended Sarivola, had killed his stepdaughter in Arizona. Sarivola passed these rumors on to his FBI contact, who told him "to find out more about it." Sarivola, having already discussed the rumors with respondent on several occasions, asked him whether the rumors were true, adding that he might be in a position to protect Fulminante from physical recriminations in prison, but that "[he] must tell him the truth." Fulminante then confessed to Sarivola that he had in fact killed his stepdaughter in Arizona, and provided Sarivola with substantial details about the manner in which he killed the child. At the suppression hearing, Fulminante stipulated to the fact that "[a]t no time did the defendant indicate he was in fear of other inmates nor did he ever seek Mr. Sarivola's `protection.'" App. 10. The trial court was also aware, through an excerpt from Sarivola's interview testimony which respondent appended to his reply memorandum, that Sarivola believed Fulminante's time was "running short" and that he would "have went out of the prison horizontally." <i>Id.,</i> at 28. The trial court found that respondent's confession was voluntary.</p>
<p>The Supreme Court of Arizona stated that the trial court committed no error in finding the confession voluntary based on the record before it. But it overturned the trial court's finding of voluntariness based on the more comprehensive trial record before it, which included, in addition to the facts stipulated at the suppression hearing, a statement made by Sarivola at the trial that "the defendant had been receiving `rough treatment from the guys, and if the defendant would <span class="star-pagination">*305</span> tell the truth, he could be protected.'" <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#244" aria-description="Citation for case: State v. Fulminante">161 Ariz. 237, 244, n. 1</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#609" aria-description="Citation for case: State v. Fulminante">778 P. 2d 602, 609, n. 1</a></span> (1989). It also had before it the presentence report, which showed that Fulminante was no stranger to the criminal justice system: He had six prior felony convictions and had been imprisoned on three prior occasions.</p>
<p>On the basis of the record before it, the Supreme Court stated:</p>
<blockquote>"Defendant contends that because he was an alleged child murderer, he was in danger of physical harm at the hands of other inmates. Sarivola was aware that defendant faced the possibility of retribution from other inmates, and that in return for the confession with respect to the victim's murder, Sarivola would protect him. Moreover, the defendant maintains that Sarivola's promise was `extremely coercive' because the `obvious' inference from the promise was that his life would be in jeopardy if he did not confess. We agree." <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#243" aria-description="Citation for case: State v. Fulminante"><i>Id.,</i> at 243</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#608" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 608</a></span>.</blockquote>
<p>Exercising our responsibility to make the independent examination of the record necessary to decide this federal question, I am at a loss to see how the Supreme Court of Arizona reached the conclusion that it did. Fulminante offered no evidence that he believed that his life was in danger or that he in fact confessed to Sarivola in order to obtain the proffered protection. Indeed, he had stipulated that "[a]t no time did the defendant indicate he was in fear of other inmates nor did he ever seek Mr. Sarivola's `protection.'" App. 10. Sarivola's testimony that he told Fulminante that "if [he] would tell the truth, he could be protected," adds little if anything to the substance of the parties' stipulation. The decision of the Supreme Court of Arizona rests on an assumption that is squarely contrary to this stipulation, and one that is not supported by any testimony of Fulminante.</p>
<p>The facts of record in the present case are quite different from those present in cases where we have found confessions <span class="star-pagination">*306</span> to be coerced and involuntary. Since Fulminante was unaware that Sarivola was an FBI informant, there existed none of "the danger of coercion result[ing] from the interaction of custody and official interrogation." <i>Illinois</i> v. <i>Perkins,</i> <span class="citation" data-id="9432050"><a href="/opinion/112452/illinois-v-perkins/#297" aria-description="Citation for case: Illinois v. Perkins">496 U. S. 292, 297</a></span> (1990). The fact that Sarivola was a Government informant does not by itself render Fulminante's confession involuntary, since we have consistently accepted the use of informants in the discovery of evidence of a crime as a legitimate investigatory procedure consistent with the Constitution. See, <i>e. g., </i><i>Kuhlmann</i> v. <i>Wilson,</i> <span class="citation" data-id="9430620"><a href="/opinion/111726/kuhlmann-v-wilson/" aria-description="Citation for case: Kuhlmann v. Wilson">477 U. S. 436</a></span> (1986); <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/" aria-description="Citation for case: United States v. White">401 U. S. 745</a></span> (1971); <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#304" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 304</a></span> (1966). The conversations between Sarivola and Fulminante were not lengthy, and the defendant was free at all times to leave Sarivola's company. Sarivola at no time threatened him or demanded that he confess; he simply requested that he speak the truth about the matter. Fulminante was an experienced habitue of prisons and presumably able to fend for himself. In concluding on these facts that Fulminante's confession was involuntary, the Court today embraces a more expansive definition of that term than is warranted by any of our decided cases.</p>
<p></p>
<h2>II</h2>
<p>Since this Court's landmark decision in <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967), in which we adopted the general rule that a constitutional error does not automatically require reversal of a conviction, the Court has applied harmless-error analysis to a wide range of errors and has recognized that most constitutional errors can be harmless. See, <i>e. g., </i><i>Clemons</i> v. <i>Mississippi,</i> <span class="citation" data-id="9431962"><a href="/opinion/112400/clemons-v-mississippi/#752" aria-description="Citation for case: Clemons v. Mississippi">494 U. S. 738, 752-754</a></span> (1990) (unconstitutionally overbroad jury instructions at the sentencing stage of a capital case); <i>Satterwhite</i> v. <i>Texas,</i> <span class="citation" data-id="9431315"><a href="/opinion/112080/satterwhite-v-texas/" aria-description="Citation for case: Satterwhite v. Texas">486 U. S. 249</a></span> (1988) (admission of evidence at the sentencing stage of a capital case in violation of the Sixth Amendment Counsel Clause); <i>Carella</i> v. <i>California,</i> <span class="citation" data-id="9431750"><a href="/opinion/112298/carella-v-california/#266" aria-description="Citation for case: Carella v. California">491 U. S. 263, 266</a></span> (1989) <span class="star-pagination">*307</span> (jury instruction containing an erroneous conclusive presumption); <i>Pope</i> v. <i>Illinois,</i> <span class="citation" data-id="9430947"><a href="/opinion/111877/pope-v-illinois/#501" aria-description="Citation for case: Pope v. Illinois">481 U. S. 497, 501-504</a></span> (1987) (jury instruction misstating an element of the offense); <i>Rose</i> v. <i>Clark,</i> <span class="citation" data-id="9430690"><a href="/opinion/111750/rose-v-clark/" aria-description="Citation for case: Rose v. Clark">478 U. S. 570</a></span> (1986) (jury instruction containing an erroneous rebuttable presumption); <i>Crane</i> v. <i>Kentucky,</i> <span class="citation" data-id="111687"><a href="/opinion/111687/crane-v-kentucky/#691" aria-description="Citation for case: Crane v. Kentucky">476 U. S. 683, 691</a></span> (1986) (erroneous exclusion of defendant's testimony regarding the circumstances of his confession); <i>Delaware</i> v. <i>Van Arsdall,</i> <span class="citation" data-id="9430412"><a href="/opinion/111625/delaware-v-van-arsdall/" aria-description="Citation for case: Delaware v. Van Arsdall">475 U. S. 673</a></span> (1986) (restriction on a defendant's right to cross-examine a witness for bias in violation of the Sixth Amendment Confrontation Clause); <i>Rushen</i> v. <i>Spain,</i> <span class="citation" data-id="9429404"><a href="/opinion/111051/rushen-v-spain/#117" aria-description="Citation for case: Rushen v. Spain">464 U. S. 114, 117-118</a></span>, and n. 2 (1983) (denial of a defendant's right to be present at trial); <i>United States</i> v. <i>Hasting,</i> <span class="citation" data-id="9429194"><a href="/opinion/110933/united-states-v-hasting/" aria-description="Citation for case: United States v. Hasting">461 U. S. 499</a></span> (1983) (improper comment on defendant's silence at trial, in violation of the Fifth Amendment Self-Incrimination Clause); <i>Hopper</i> v. <i>Evans,</i> <span class="citation" data-id="9428768"><a href="/opinion/110711/hopper-v-evans/" aria-description="Citation for case: Hopper v. Evans">456 U. S. 605</a></span> (1982) (statute improperly forbidding trial court's giving a jury instruction on a lesser included offense in a capital case in violation of the Due Process Clause); <i>Kentucky</i> v. <i>Whorton,</i> <span class="citation" data-id="9427578"><a href="/opinion/110081/kentucky-v-whorton/" aria-description="Citation for case: Kentucky v. Whorton">441 U. S. 786</a></span> (1979) (failure to instruct the jury on the presumption of innocence); <i>Moore</i> v. <i>Illinois,</i> <span class="citation" data-id="9427017"><a href="/opinion/109757/moore-v-illinois/#232" aria-description="Citation for case: Moore v. Illinois">434 U. S. 220, 232</a></span> (1977) (admission of identification evidence in violation of the Sixth Amendment Confrontation Clause); <i>Brown</i> v. <i>United States,</i> <span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/#231" aria-description="Citation for case: Brown v. United States">411 U. S. 223, 231-232</a></span> (1973) (admission of the out-of-court statement of a nontestifying codefendant in violation of the Sixth Amendment Confrontation Clause); <i>Milton</i> v. <i>Wainwright,</i> <span class="citation" data-id="9424959"><a href="/opinion/108585/milton-v-wainwright/" aria-description="Citation for case: Milton v. Wainwright">407 U. S. 371</a></span> (1972) (confession obtained in violation of <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964)); <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 52-53</a></span> (1970) (admission of evidence obtained in violation of the Fourth Amendment); <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#10" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1, 10-11</a></span> (1970) (denial of counsel at a preliminary hearing in violation of the Sixth Amendment Counsel Clause).</p>
<p>The common thread connecting these cases is that each involved "trial error"error which occurred during the presentation of the case to the jury, and which may therefore <span class="star-pagination">*308</span> be quantitatively assessed in the context of other evidence presented in order to determine whether its admission was harmless beyond a reasonable doubt. In applying harmless-error analysis to these many different constitutional violations, the Court has been faithful to the belief that the harmless-error doctrine is essential to preserve the "principle that the central purpose of a criminal trial is to decide the factual question of the defendant's guilt or innocence, and promotes public respect for the criminal process by focusing on the underlying fairness of the trial rather than on the virtually inevitable presence of immaterial error." <span class="citation" data-id="9430412"><a href="/opinion/111625/delaware-v-van-arsdall/#681" aria-description="Citation for case: Delaware v. Van Arsdall"><i>Van Arsdall, supra,</i> at 681</a></span> (citations omitted).</p>
<p>In <i>Chapman</i> v. <i>California, supra</i><i>,</i> the Court stated:</p>
<blockquote>"Although our prior cases have indicated that there are some constitutional rights so basic to a fair trial that their infraction can never be treated as harmless error,8 this statement in <i>Fahy</i> itself belies any belief that all trial errors which violate the Constitution automatically call for reversal.</blockquote>
<blockquote>"8 See, <i>e. g., </i><i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span> (coerced confession); <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span> (right to counsel); <i>Tumey</i> v. <i>Ohio,</i> <span class="citation" data-id="101031"><a href="/opinion/101031/tumey-v-ohio/" aria-description="Citation for case: Tumey v. Ohio">273 U. S. 510</a></span> (impartial judge)."</blockquote>
<blockquote>
<i>Id.,</i> at 23.</blockquote>
<p>It is on the basis of this language in <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span></i> that JUSTICE WHITE in dissent concludes that the principle of <i>stare decisis</i> requires us to hold that an involuntary confession is not subject to harmless-error analysis. We believe that there are several reasons which lead to a contrary conclusion. In the first place, the quoted language from <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span></i> does not by its terms adopt any such rule in that case. The language that "[a]lthough our prior cases have indicated," coupled with the relegation of the cases themselves to a footnote, is more appropriately regarded as a historical reference to the holdings of these cases. This view is buttressed by an examination of the opinion in <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span> (1958), which is the case referred to for the proposition that <span class="star-pagination">*309</span> an involuntary confession may not be subject to harmless-error analysis. There the Court said:</p>
<blockquote>"Respondent suggests that, apart from the confession, there was adequate evidence before the jury to sustain the verdict. But where, as here, an involuntary confession constitutes a part of the evidence before the jury and a general verdict is returned, no one can say what credit and weight the jury gave to the confession. And in these circumstances this Court has uniformly held that even though there may have been sufficient evidence, apart from the coerced confession, to support a judgment of conviction, the admission in evidence, over objection, of the coerced confession vitiates the judgment because it violates the Due Process Clause of the Fourteenth Amendment." <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#567" aria-description="Citation for case: Payne v. Arkansas"><i>Id.,</i> at 567-568</a></span>.</blockquote>
<p>It is apparent that the State's argument which the Court rejected in <i><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">Payne</a></span></i> is not the harmless-error analysis later adopted in <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span>,</i> but a much more lenient rule which would allow affirmance of a conviction if the evidence other than the involuntary confession was sufficient to sustain the verdict. This is confirmed by the dissent of Justice Clark in that case, which adopted the more lenient test. Such a test would, of courseunlike the harmless-error testmake the admission of an involuntary confession virtually risk free for the State.</p>
<p>The admission of an involuntary confessiona classic "trial error"is markedly different from the other two constitutional violations referred to in the <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span></i> footnote as not being subject to harmless-error analysis. One of those violations, involved in <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span> (1963), was the total deprivation of the right to counsel at trial. The other violation, involved in <i>Tumey</i> v. <i>Ohio,</i> <span class="citation" data-id="101031"><a href="/opinion/101031/tumey-v-ohio/" aria-description="Citation for case: Tumey v. Ohio">273 U. S. 510</a></span> (1927), was a judge who was not impartial. These are structural defects in the constitution of the trial mechanism, which defy analysis by "harmless-error" standards. The entire conduct of the trial from beginning to end is obviously <span class="star-pagination">*310</span> affected by the absence of counsel for a criminal defendant, just as it is by the presence on the bench of a judge who is not impartial. Since our decision in <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span>,</i> other cases have added to the category of constitutional errors which are not subject to harmless error the following: unlawful exclusion of members of the defendant's race from a grand jury, <i>Vasquez</i> v. <i>Hillery,</i> <span class="citation" data-id="9430252"><a href="/opinion/111552/vasquez-v-hillery/" aria-description="Citation for case: Vasquez v. Hillery">474 U. S. 254</a></span> (1986); the right to self-representation at trial, <i>McKaskle</i> v. <i>Wiggins,</i> <span class="citation" data-id="9429486"><a href="/opinion/111095/mckaskle-v-wiggins/#177" aria-description="Citation for case: McKaskle v. Wiggins">465 U. S. 168, 177-178, n. 8</a></span> (1984); and the right to public trial, <i>Waller</i> v. <i>Georgia,</i> <span class="citation" data-id="111186"><a href="/opinion/111186/waller-v-georgia/#49" aria-description="Citation for case: Waller v. Georgia">467 U. S. 39, 49, n. 9</a></span> (1984). Each of these constitutional deprivations is a similar structural defect affecting the framework within which the trial proceeds, rather than simply an error in the trial process itself. "Without these basic protections, a criminal trial cannot reliably serve its function as a vehicle for determination of guilt or innocence, and no criminal punishment may be regarded as fundamentally fair." <i>Rose</i> v. <i>Clark,</i> <span class="citation" data-id="9430690"><a href="/opinion/111750/rose-v-clark/#577" aria-description="Citation for case: Rose v. Clark">478 U. S., at 577-578</a></span> (citation omitted).</p>
<p>It is evident from a comparison of the constitutional violations which we have held subject to harmless error, and those which we have held not, that involuntary statements or confessions belong in the former category. The admission of an involuntary confession is a "trial error," similar in both degree and kind to the erroneous admission of other types of evidence. The evidentiary impact of an involuntary confession, and its effect upon the composition of the record, is indistinguishable from that of a confession obtained in violation of the Sixth Amendmentof evidence seized in violation of the Fourth Amendmentor of a prosecutor's improper comment on a defendant's silence at trial in violation of the Fifth Amendment. When reviewing the erroneous admission of an involuntary confession, the appellate court, as it does with the admission of other forms of improperly admitted evidence, simply reviews the remainder of the evidence against the defendant to determine whether the admission of the confession was harmless beyond a reasonable doubt.</p>
<p><span class="star-pagination">*311</span> Nor can it be said that the admission of an involuntary confession is the type of error which "transcends the criminal process." This Court has applied harmless-error analysis to the violation of other constitutional rights similar in magnitude and importance and involving the same level of police misconduct. For instance, we have previously held that the admission of a defendant's statements obtained in violation of the Sixth Amendment is subject to harmless-error analysis. In <i>Milton</i> v. <i>Wainwright,</i> <span class="citation" data-id="9424959"><a href="/opinion/108585/milton-v-wainwright/" aria-description="Citation for case: Milton v. Wainwright">407 U. S. 371</a></span> (1972), the Court held the admission of a confession obtained in violation of <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964), to be harmless beyond a reasonable doubt. We have also held that the admission of an out-of-court statement by a nontestifying codefendant is subject to harmless-error analysis. <i>Brown</i> v. <i>United States,</i> <span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/#231" aria-description="Citation for case: Brown v. United States">411 U. S., at 231-232</a></span>; <i>Schneble</i> v. <i>Florida,</i> <span class="citation" data-id="9424785"><a href="/opinion/108488/schneble-v-florida/" aria-description="Citation for case: Schneble v. Florida">405 U. S. 427</a></span> (1972); <i>Harrington</i> v. <i>California,</i> <span class="citation" data-id="9424056"><a href="/opinion/107952/harrington-v-california/" aria-description="Citation for case: Harrington v. California">395 U. S. 250</a></span> (1969). The inconsistent treatment of statements elicited in violation of the Sixth and Fourteenth Amendments, respectively, can be supported neither by evidentiary or deterrence concerns nor by a belief that there is something more "fundamental" about involuntary confessions. This is especially true in a case such as this one where there are no allegations of physical violence on behalf of the police. A confession obtained in violation of the Sixth Amendment has the same evidentiary impact as does a confession obtained in violation of a defendant's due process rights. Government misconduct that results in violations of the Fourth and Sixth Amendments may be at least as reprehensible as conduct that results in an involuntary confession. For instance, the prisoner's confession to an inmate-informer at issue in <i><span class="citation" data-id="9424959"><a href="/opinion/108585/milton-v-wainwright/" aria-description="Citation for case: Milton v. Wainwright">Milton</a></span>,</i> which the Court characterized as implicating the Sixth Amendment right to counsel, is similar on its facts to the one we face today. Indeed, experience shows that law enforcement violations of these constitutional guarantees can involve conduct as egregious as police conduct used to elicit statements in violation of the Fourteenth Amendment. It is thus <span class="star-pagination">*312</span> impossible to create a meaningful distinction between confessions elicited in violation of the Sixth Amendment and those in violation of the Fourteenth Amendment.</p>
<p>Of course an involuntary confession may have a more dramatic effect on the course of a trial than do other trial errorsin particular cases it may be devastating to a defendant but this simply means that a reviewing court will conclude in such a case that its admission was not harmless error; it is not a reason for eschewing the harmless-error test entirely. The Supreme Court of Arizona, in its first opinion in the present case, concluded that the admission of Fulminante's confession <i>was</i> harmless error. That court concluded that a second and more explicit confession of the crime made by Fulminante after he was released from prison was not tainted by the first confession, and that the second confession, together with physical evidence from the wounds (the victim had been shot twice in the head with a large calibre weapon at close range and a ligature was found around her neck) and other evidence introduced at trial rendered the admission of the first confession harmless beyond a reasonable doubt. <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#245" aria-description="Citation for case: State v. Fulminante">161 Ariz., at 245-246</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#610" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 610-611</a></span>.</p>
<p></p>
<h2>III</h2>
<p>I would agree with the finding of the Supreme Court of Arizona in its initial opinionin which it believed harmless-error analysis was applicable to the admission of involuntary confessionsthat the admission of Fulminante's confession was harmless. Indeed, this seems to me to be a classic case of harmless error: a second confession giving more details of the crime than the first was admitted in evidence and found to be free of any constitutional objection. Accordingly, I would affirm the holding of the Supreme Court of Arizona in its initial opinion and reverse the judgment which it ultimately rendered in this case.</p>
<p><span class="star-pagination">*313</span> JUSTICE KENNEDY, concurring in the judgment.</p>
<p>For the reasons stated by THE CHIEF JUSTICE, I agree that Fulminante's confession to Anthony Sarivola was not coerced. In my view, the trial court did not err in admitting this testimony. A majority of the Court, however, finds the confession coerced and proceeds to consider whether harmless-error analysis may be used when a coerced confession has been admitted at trial. With the case in this posture, it is appropriate for me to address the harmless-error issue.</p>
<p>Again for the reasons stated by THE CHIEF JUSTICE, I agree that harmless-error analysis should apply in the case of a coerced confession. That said, the court conducting a harmless-error inquiry must appreciate the indelible impact a full confession may have on the trier of fact, as distinguished, for instance, from the impact of an isolated statement that incriminates the defendant only when connected with other evidence. If the jury believes that a defendant has admitted the crime, it doubtless will be tempted to rest its decision on that evidence alone, without careful consideration of the other evidence in the case. Apart, perhaps, from a video-tape of the crime, one would have difficulty finding evidence more damaging to a criminal defendant's plea of innocence. For the reasons given by JUSTICE WHITE in Part IV of his opinion, I cannot with confidence find admission of Fulminante's confession to Anthony Sarivola to be harmless error.</p>
<p>The same majority of the Court does not agree on the three issues presented by the trial court's determination to admit Fulminante's first confession: whether the confession was inadmissible because coerced; whether harmless-error analysis is appropriate; and if so whether any error was harmless here. My own view that the confession was not coerced does not command a majority.</p>
<p>In the interests of providing a clear mandate to the Arizona Supreme Court in this capital case, I deem it proper to accept in the case now before us the holding of five Justices that the <span class="star-pagination">*314</span> confession was coerced and inadmissible. I agree with a majority of the Court that admission of the confession could not be harmless error when viewed in light of all the other evidence; and so I concur in the judgment to affirm the ruling of the Arizona Supreme Court.</p>
<h2>NOTES</h2>
<p>[*]  <i>Gregory U. Evans, Daniel B. Hales, Joseph A. Morris, George D. Webster, Jack E. Yelverton, Fred E. Inbau, Wayne W. Schmidt, Bernard J. Farber,</i> and <i>James P. Manak</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging reversal.
</p>
<p><i>H. Gerald Beaver</i> and <i>Richard B. Glazier</i> filed a brief for the National Association of Criminal Defense Lawyers as <i>amicus curiae</i> urging affirmance.</p>
<p>[]  JUSTICE MARSHALL, JUSTICE BLACKMUN, and JUSTICE STEVENS join this opinion in its entirety; JUSTICE SCALIA joins Parts I and II; and JUSTICE KENNEDY joins Parts I and IV.</p>
<p>[1]  In its initial opinion, the Arizona Supreme Court had determined that the second confession, to Donna Sarivola, was not the "fruit of the poisonous tree," because it was made six months after the confession to Sarivola; it occurred after Fulminante's need for protection from Sarivola presumably had ended; and it took place in the course of a casual conversation with someone who was not an agent of the State. <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#246" aria-description="Citation for case: State v. Fulminante">161 Ariz. 237, 246</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#611" aria-description="Citation for case: State v. Fulminante">778 P. 2d 602, 611</a></span> (1988). The court adhered to this determination in its supplemental opinion. <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#262" aria-description="Citation for case: State v. Fulminante"><i>Id.,</i> at 262</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#627" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 627</a></span>. This aspect of the Arizona Supreme Court's decision is not challenged here.</p>
<p>[2]  There are additional facts in the record, not relied upon by the Arizona Supreme Court, which also support a finding of coercion. Fulminante possesses low average to average intelligence; he dropped out of school in the fourth grade. Record 88i, 88o. He is short in stature and slight in build. <i>Id.,</i> at 88. Although he had been in prison before, <i>ibid.,</i> he had not always adapted well to the stress of prison life. While incarcerated at the age of 26, he had "felt threatened by the [prison] population," <i>id.,</i> at 88x, and he therefore requested that he be placed in protective custody. Once there, however, he was unable to cope with the isolation and was admitted to a psychiatric hospital. <i>Id.,</i> at 88t-88b1. The Court has previously recognized that factors such as these are relevant in determining whether a defendant's will has been overborne. See, <i>e. g., </i><i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#567" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560, 567</a></span> (1958) (lack of education); <i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/#441" aria-description="Citation for case: Reck v. Pate">367 U. S. 433, 441</a></span> (1961) (low intelligence). Cf. <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 226</a></span> (1973) (listing potential factors); <i>Culombe</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#602" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568, 602</a></span> (1961) (same). In addition, we note that Sarivola's position as Fulminante's friend might well have made the latter particularly susceptible to the former's entreaties. See <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#323" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 323</a></span> (1959).</p>
<p>[3]  Our prior cases have used the terms "coerced confession" and "involuntary confession" interchangeably "by way of convenient shorthand." <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#207" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 207</a></span> (1960). We use the former term throughout this opinion, as that is the term used by the Arizona Supreme Court.</p>
<p>[4]  The parties agree that Sarivola acted as an agent of the Government when he questioned Fulminante about the murder and elicited the confession. Brief for Petitioner 19; Brief for Respondent 2.</p>
<p>[5]  In <i>Satterwhite</i> v. <i>Texas,</i> <span class="citation" data-id="9431315"><a href="/opinion/112080/satterwhite-v-texas/" aria-description="Citation for case: Satterwhite v. Texas">486 U. S. 249</a></span> (1988), and <i>Moore</i> v. <i>Illinois,</i> <span class="citation" data-id="9427017"><a href="/opinion/109757/moore-v-illinois/" aria-description="Citation for case: Moore v. Illinois">434 U. S. 220</a></span> (1977), the harmless-error rule was applied to the admission of evidence in violation of the Sixth Amendment Counsel Clause, but in neither case did the error involve admitting a confession or an incriminating statement of the defendant, which was the case in <i>Milton</i> v. <i>Wainwright</i><i>.</i></p>
<p>[6]  <i>Howard</i> v. <i>Pung,</i> <span class="citation" data-id="515504"><a href="/opinion/515504/donald-wayne-howard-v-orville-pung-commissioner-of-corrections-and-frank/#1351" aria-description="Citation for case: Donald Wayne Howard v. Orville Pung, Commissioner of...">862 F. 2d 1348, 1351</a></span> (CA8 1988), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./492/920/">492 U. S. 920</a></span> (1989); <i>United States</i> v. <i>Johnson,</i> <span class="citation" data-id="487141"><a href="/opinion/487141/united-states-v-johnson-richard/#923" aria-description="Citation for case: United States v. Johnson, Richard">816 F. 2d 918, 923</a></span> (CA3 1987); <i>Bryant</i> v. <i>Vose,</i> <span class="citation" data-id="466083"><a href="/opinion/466083/clayton-m-bryant-v-george-a-vose-jr-superintendent-of-massachusetts/#367" aria-description="Citation for case: Clayton M. Bryant v. George A. Vose, Jr., Superintendent...">785 F. 2d 364, 367</a></span> (CA1), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./477/907/">477 U. S. 907</a></span> (1986); <i>Martin</i> v. <i>Wainwright,</i> <span class="citation" data-id="9473880"><a href="/opinion/457158/nollie-lee-martin-v-louie-l-wainwright/#932" aria-description="Citation for case: Nollie Lee Martin v. Louie L. Wainwright">770 F. 2d 918, 932</a></span> (CAll 1985), modified, <span class="citation" data-id="463284"><a href="/opinion/463284/nollie-lee-martin-v-louie-l-wainwright/" aria-description="Citation for case: Nollie Lee Martin v. Louie L. Wainwright">781 F. 2d 185</a></span>, cert. denied, <span class="citation" data-id="9058387"><a href="/opinion/9064759/martin-v-wainwright/" aria-description="Citation for case: Martin v. Wainwright">479 U. S. 909</a></span> (1986); <i>United States</i> v. <i>Ramirez,</i> <span class="citation" data-id="420788"><a href="/opinion/420788/united-states-v-roy-moreno-ramirez-united-states-of-america-v-robert-h/#542" aria-description="Citation for case: United States v. Roy Moreno Ramirez, United States of...">710 F. 2d 535, 542-543</a></span> (CA9 1983); <i>Harryman</i> v. <i>Estelle,</i> <span class="citation" data-id="9466546"><a href="/opinion/375540/burley-clifton-harryman-v-w-j-estelle-jr-director-texas-department/#875" aria-description="Citation for case: Burley Clifton Harryman v. W. J. Estelle, Jr., Director,...">616 F. 2d 870, 875</a></span> (CA5) (en banc), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/860/">449 U. S. 860</a></span> (1980).</p>
<p>[7]  The same can be said of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> cases. As the Court has recognized, a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation "does not mean that the statements received have actually been coerced, but only that the courts will presume the privilege against compulsory self-incrimination has not been intelligently exercised." <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#310" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 310</a></span> (1985). See also <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#654" aria-description="Citation for case: New York v. Quarles">467 U. S. 649, 654</a></span> (1984).</p>
<p>[8]  Although Fulminante had allegedly confessed to Donna Sarivola several months previously, police did not yet know of this confession, which Anthony Sarivola did not mention to them until June 1985. App. 90-92. They did, however, know of the first confession, which Fulminante had given to Anthony Sarivola nearly a year before.</p>
<p>[9]  The inadmissible confession to Anthony Sarivola was itself subject to serious challenge. Sarivola's lack of moral integrity was demonstrated by his testimony that he had worked for organized crime during the time he was a uniformed police officer. App. 74-75, 104-105. His overzealous approach to gathering information for which he would be paid by authorities, <i>id.,</i> at 79, was revealed by his admission that he had fabricated a tape recording in connection with an earlier, unrelated FBI investigation, <i>id.,</i> at 96-98. He received immunity in connection with the information he provided. <i>Id.,</i> at 129. His eagerness to get in and stay in the federal Witness Protection Program provided a motive for giving detailed information to authorities. <i>Id.,</i> at 114, 129-131. During his first report of the confession, Sarivola failed to hint at numerous details concerning an alleged sexual assault on Jeneane; he mentioned them for the first time more than a year later during further interrogation, at which he also recalled, for the first time, the confession to Donna Sarivola. <i>Id.,</i> at 90-92, 148-149. The impeaching effect of each of these factors was undoubtedly undercut by the presence of the second confession, which, not surprisingly, recounted a quite similar story and thus corroborated the first confession. Thus, each confession, though easily impeachable if viewed in isolation, became difficult to discount when viewed in conjunction with the other.</p>
<p>[10]  Fulminante asserts that other prejudicial evidence, including his prior felony convictions and incarcerations, and his prison reputation for untruthfulness, likewise would not have been admitted had the confession to Sarivola been excluded. Brief for Respondent 31-32. Because we find that the admission of the confession was not harmless in any event, we express no opinion as to the effect any of this evidence might have had on Fulminante's conviction.</p>

</div>
```

---
