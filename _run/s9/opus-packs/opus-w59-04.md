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

## GROUP: content/seizures/Stop-and-Identify.md  (`doctrine`, 5 assertions)

### content_page

```
---
weight: 40
title: "Stop-and-Identify"
aliases:
  - "stop-and-identify"
  - "stop and identify"
topic: "Stop-and-identify: when a valid Terry stop can compel a name"
type: doctrine
amendment: "U.S. Const. amend. IV; U.S. Const. amend. V"
jurisdiction: "Federal (U.S. Const. amend. IV & V); SCOTUS baseline; obligation depends on state law"
status: draft
related:
  - "[[Terry Stops and Reasonable Suspicion]]"
  - "[[When a Seizure Occurs]]"
  - "[[Reasonable Suspicion]]"
  - "[[Probable Cause]]"
---

# Stop-and-Identify

*Can an officer compel a lawfully stopped suspect to give his name, and jail him for refusing? Only where a state stop-and-identify statute so provides, the underlying stop is a valid* Terry *stop, and disclosure would not itself incriminate.*

> [!rule] Black-letter rule
> **A state stop-and-identify statute, applied during a valid *[[Terry v. Ohio|Terry]]* stop, may compel a suspect to disclose his name, consistent with the Fourth and Fifth Amendments.** Where a suspect is lawfully detained on reasonable suspicion, a statute requiring him to identify himself is reasonable under the Fourth Amendment so long as the request for identity is **reasonably related to the circumstances justifying the stop**, and it does not violate the Fifth Amendment unless the **disclosure of the name itself would be incriminating**. *[[Hiibel v. Sixth Judicial Dist. Court#^pin-188|Hiibel]]*, 542 U.S. 177, [188](https://www.courtlistener.com/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/) (2004). The duty to identify comes from **state law, not the Fourth Amendment**, so it exists only where a statute imposes it and that statute is not void for vagueness. *[[Kolender v. Lawson|Kolender]]*, 461 U.S. 352 (1983).
> ^rule-stop-and-identify

## The Brief

**The rule and its two anchors (*[[Hiibel v. Sixth Judicial Dist. Court|Hiibel]]*).** A *[[Terry v. Ohio|Terry]]* stop lets an officer briefly detain a person on reasonable, articulable suspicion. Whether that detention can be turned into a *legal command* to identify, enforced by arrest, is a separate question, and it was open until *[[Hiibel v. Sixth Judicial Dist. Court|Hiibel]]*. The Court held that a Nevada statute compelling a lawfully stopped suspect to disclose his name is constitutional. "Obtaining a suspect's name in the course of a *Terry* stop serves important government interests," including officer safety and knowing whom one is dealing with. *[[Hiibel v. Sixth Judicial Dist. Court|Hiibel]]*, 542 U.S. at [186](https://www.courtlistener.com/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/). The obligation is narrow: the Nevada law reached only the suspect's **name**, not answers to any other question.

**Fourth Amendment: the demand must ride a valid stop and fit it.** The identity request is reasonable only when the stop is itself lawful and the request is tied to it. An officer "may not arrest a suspect for failure to identify himself if the request for identification is not reasonably related to the circumstances justifying the stop." *[[Hiibel v. Sixth Judicial Dist. Court#^pin-188|Hiibel]]*, 542 U.S. at [188](https://www.courtlistener.com/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/). And there is no power to demand identity in the first place without reasonable suspicion: police "may not stop a person and demand identification" on nothing, because a suspicionless detention is itself an unreasonable seizure. *[[Brown v. Texas#^pin-53|Brown v. Texas]]*, 443 U.S. 47, [53](https://www.courtlistener.com/opinion/110128/brown-v-texas/) (1979). The stop-and-identify power is therefore parasitic on a valid *[[Terry Stops and Reasonable Suspicion|Terry]]* stop; it never supplies the suspicion that justifies the stop.

**Fifth Amendment: compelling a name is usually not incrimination.** Forcing disclosure of a name is ordinarily not testimonial self-incrimination, because a name "in most cases" furnishes no link in the chain of evidence needed to prosecute. *[[Hiibel v. Sixth Judicial Dist. Court|Hiibel]]* itself found no Fifth Amendment problem, because Hiibel never explained how giving his name could incriminate him. The Court **reserved** the different case, where disclosure of identity would "furnish a link in the chain of evidence needed to prosecute the claimant." *[[Hiibel v. Sixth Judicial Dist. Court|Hiibel]]*, 542 U.S. at [190–191](https://www.courtlistener.com/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/). In that situation the privilege against self-incrimination could bar compelled disclosure.

**The obligation is a creature of state law, and the statute must be definite.** Nothing in the Fourth Amendment by itself makes silence a crime. An officer may always *ask* a suspect to identify himself during a stop, *[[Berkemer v. McCarty|Berkemer]]*, 468 U.S. 420 (1984), but he may *arrest* for refusal only where a statute makes refusal an offense. That statute must give fair notice of what compliance requires. In *[[Kolender v. Lawson|Kolender]]* the Court struck down a California statute that required a suspect to give "credible and reliable" identification, holding it void for vagueness because it "vests virtually complete discretion in the hands of the police" to decide what a suspect must produce. *[[Kolender v. Lawson#^pin-358|Kolender]]*, 461 U.S. at [358](https://www.courtlistener.com/opinion/110926/kolender-v-lawson/). A bare **name-disclosure** requirement like Nevada's survives; an open-ended "satisfactory identification" requirement does not.

**Honest scope: check the local statute.** Because the duty is statutory, the answers vary by jurisdiction. Some States make refusal to identify a misdemeanor; some treat it only as a factor in a larger offense such as loitering; and in others a suspect may decline to give his name without penalty. What a suspect must provide also varies: *[[Hiibel v. Sixth Judicial Dist. Court|Hiibel]]* upholds a **name-only** command, and it does not decide whether a State may compel more (for example, a document or address). Teach the framework, then read the controlling statute.

**Burden, standard of review, and remedy.** The **government** bears the burden of showing the stop was valid and the identity demand reasonably related to it; the validity of the stop is reviewed with historical facts for [[Common Legal Terms#clear-error|clear error]] and the ultimate Fourth Amendment question [[Common Legal Terms#de-novo|de novo]]. Evidence obtained from an identity demand that rode an **unlawful** stop is subject to suppression as its fruit (see [[The Exclusionary Rule]]).

**Apply it.**
1. **Confirm a valid *[[Terry v. Ohio|Terry]]* stop first.** No reasonable suspicion means no lawful detention and no power to demand identity. *[[Brown v. Texas|Brown v. Texas]]*.
2. **Find the statute.** The duty to identify comes from state law. Without a statute compelling disclosure, refusal to answer is not itself a crime; you may ask, not arrest. *[[Berkemer v. McCarty|Berkemer]]*.
3. **Match the demand to the stop.** The identity request must be reasonably related to the circumstances that justified the stop. *[[Hiibel v. Sixth Judicial Dist. Court|Hiibel]]*.
4. **Keep it to a name.** *[[Hiibel v. Sixth Judicial Dist. Court|Hiibel]]* upholds a name-only command; it does not authorize compelling documents or answers to further questions.
5. **Watch for a real Fifth Amendment claim.** If disclosing the name would itself furnish a link in the chain of evidence to prosecute, the privilege may bar compelled disclosure. *[[Hiibel v. Sixth Judicial Dist. Court|Hiibel]]*.

**Common pitfalls.**
- **Treating stop-and-identify as a free-standing federal power.** The duty is statutory; absent a valid state statute, refusal to give a name is not a crime. *[[Kolender v. Lawson|Kolender]]*.
- **Demanding identity without reasonable suspicion.** No suspicion, no stop, no lawful demand. *[[Brown v. Texas|Brown v. Texas]]*.
- **Reading *[[Hiibel v. Sixth Judicial Dist. Court|Hiibel]]* to compel more than a name.** It upholds a name-only requirement and reserves whether a State may demand documents or an address.
- **Assuming the Fifth Amendment is never in play.** It usually is not, but it bars compelled disclosure where the name itself would incriminate. *[[Hiibel v. Sixth Judicial Dist. Court|Hiibel]]*.
- **Enforcing a vague "satisfactory identification" statute.** A law that lets the officer decide what counts is void for vagueness. *[[Kolender v. Lawson|Kolender]]*.

## Key cases

| Case | Holding | Opinion |
|---|---|---|
| *[[Hiibel v. Sixth Judicial Dist. Court]]*, 542 U.S. 177 (2004) | **Anchor.** A state stop-and-identify statute compelling a suspect to disclose his name during a valid *[[Terry v. Ohio\|Terry]]* stop is consistent with the Fourth Amendment (request reasonably related to the stop) and the Fifth Amendment (unless the name itself would incriminate). | [opinion](https://www.courtlistener.com/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/) |
| *[[Kolender v. Lawson]]*, 461 U.S. 352 (1983) | A stop-and-identify statute requiring "credible and reliable" identification is void for vagueness; it hands police standardless discretion to decide what satisfies it. | [opinion](https://www.courtlistener.com/opinion/110926/kolender-v-lawson/) |

## Related cases across doctrines

These are treated in full on their own pages but frame the stop-and-identify power.

| Case | Relevance here | Primary home | Opinion |
|---|---|---|---|
| *[[Brown v. Texas]]*, 443 U.S. 47 (1979) | ***No suspicion, no demand.*** Police may not stop a person and demand identification without reasonable suspicion; the stop-and-identify power presupposes a lawful stop. | [[Terry Stops and Reasonable Suspicion]] | [opinion](https://www.courtlistener.com/opinion/110128/brown-v-texas/) |
| *[[Berkemer v. McCarty]]*, 468 U.S. 420 (1984) | ***May ask.*** An officer may ask a lawfully stopped suspect to identify himself; a *[[Terry v. Ohio\|Terry]]* stop is ordinarily non-custodial, the [[Common Legal Terms#dicta\|dicta]] *[[Hiibel v. Sixth Judicial Dist. Court\|Hiibel]]* later built on. | [[Miranda and Custodial Interrogation]] | [opinion](https://www.courtlistener.com/opinion/111249/berkemer-v-mccarty/) |

## Sources

- [*Brown v. Texas*, 443 U.S. 47 (1979)](https://www.courtlistener.com/opinion/110128/brown-v-texas/) (pinpoint: 53)
- [*Kolender v. Lawson*, 461 U.S. 352 (1983)](https://www.courtlistener.com/opinion/110926/kolender-v-lawson/) (pinpoints: 357, 358)
- [*Berkemer v. McCarty*, 468 U.S. 420 (1984)](https://www.courtlistener.com/opinion/111249/berkemer-v-mccarty/) (an officer may ask a stopped suspect to identify himself; home = [[Miranda and Custodial Interrogation]])
- [*Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.*, 542 U.S. 177 (2004)](https://www.courtlistener.com/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/) (pinpoints: 186, 187, 188, 190–191)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "18c8a359e7d7f29e", "dimension": "existence", "kind": "case_cite", "locator": {"case": "Kolender v. Lawson", "table_line": 43}, "payload": {"case": "Kolender v. Lawson", "cells": ["*[[Kolender v. Lawson]]*, 461 U.S. 352 (1983)", "A stop-and-identify statute requiring \"credible and reliable\" identification is void for vagueness; it hands police standardless discretion to decide what satisfies it.", "[opinion](https://www.courtlistener.com/opinion/110926/kolender-v-lawson/)"], "header": ["Case", "Holding", "Opinion"]}}
{"assertion_id": "21234ba3f14b0e61", "dimension": "existence", "kind": "case_cite", "locator": {"case": "Berkemer v. McCarty", "table_line": 52}, "payload": {"case": "Berkemer v. McCarty", "cells": ["*[[Berkemer v. McCarty]]*, 468 U.S. 420 (1984)", "***May ask.*** An officer may ask a lawfully stopped suspect to identify himself; a *[[Terry v. Ohio\\|Terry]]* stop is ordinarily non-custodial, the [[Common Legal Terms#dicta\\|dicta]] *[[Hiibel v. Sixth Judicial Dist. Court\\|Hiibel]]* later built on.", "[[Miranda and Custodial Interrogation]]", "[opinion](https://www.courtlistener.com/opinion/111249/berkemer-v-mccarty/)"], "header": ["Case", "Relevance here", "Primary home", "Opinion"]}}
{"assertion_id": "9f843b8786cf8279", "dimension": "existence", "kind": "case_cite", "locator": {"case": "Brown v. Texas", "table_line": 51}, "payload": {"case": "Brown v. Texas", "cells": ["*[[Brown v. Texas]]*, 443 U.S. 47 (1979)", "***No suspicion, no demand.*** Police may not stop a person and demand identification without reasonable suspicion; the stop-and-identify power presupposes a lawful stop.", "[[Terry Stops and Reasonable Suspicion]]", "[opinion](https://www.courtlistener.com/opinion/110128/brown-v-texas/)"], "header": ["Case", "Relevance here", "Primary home", "Opinion"]}}
{"assertion_id": "e9836ca0b5c9208a", "dimension": "existence", "kind": "case_cite", "locator": {"case": "Hiibel v. Sixth Judicial Dist. Court", "table_line": 42}, "payload": {"case": "Hiibel v. Sixth Judicial Dist. Court", "cells": ["*[[Hiibel v. Sixth Judicial Dist. Court]]*, 542 U.S. 177 (2004)", "**Anchor.** A state stop-and-identify statute compelling a suspect to disclose his name during a valid *[[Terry v. Ohio\\|Terry]]* stop is consistent with the Fourth Amendment (request reasonably related to the stop) and the Fifth Amendment (unless the name itself would incriminate).", "[opinion](https://www.courtlistener.com/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/)"], "header": ["Case", "Holding", "Opinion"]}}
{"assertion_id": "e6ec71dfb6c4d753", "dimension": "support", "kind": "proposition", "locator": {"callout": "^rule-stop-and-identify"}, "payload": {"anchor": "^rule-stop-and-identify", "statement": "[!rule] Black-letter rule\n**A state stop-and-identify statute, applied during a valid *[[Terry v. Ohio|Terry]]* stop, may compel a suspect to disclose his name, consistent with the Fourth and Fifth Amendments.** Where a suspect is lawfully detained on reasonable suspicion, a statute requiring him to identify himself is reasonable under the Fourth Amendment so long as the request for identity is **reasonably related to the circumstances justifying the stop**, and it does not violate the Fifth Amendment unless the **disclosure of the name itself would be incriminating**. *[[Hiibel v. Sixth Judicial Dist. Court#^pin-188|Hiibel]]*, 542 U.S. 177, [188](https://www.courtlistener.com/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/) (2004). The duty to identify comes from **state law, not the Fourth Amendment**, so it exists only where a statute imposes it and that statute is not void for vagueness. *[[Kolender v. Lawson|Kolender]]*, 461 U.S. 352 (1983)."}}
```

### lake record — Berkemer v. McCarty

```json
{
  "schema_version": "s2.v1",
  "record_id": "Berkemer v. McCarty",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Berkemer v. McCarty",
    "case_name_short": "Berkemer",
    "case_name_full": "BERKEMER, SHERIFF OF FRANKLIN COUNTY, OHIO v. McCARTY",
    "input_case_name": "Berkemer v. McCarty",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-07-02",
    "year": 1984,
    "docket": "83-710",
    "cluster_id": 111249,
    "lead_opinion_id": 9429728,
    "sibling_ids": [
      111249,
      9429728,
      9429729
    ],
    "absolute_url": "/opinion/111249/berkemer-v-mccarty/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9047277,
        "score": 10,
        "case_name": "Berkemer v. McCarty"
      },
      {
        "cluster_id": 9287487,
        "score": 10,
        "case_name": "Berkemer v. McCarty"
      }
    ],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "468 U.S. 420",
      "volume": "468",
      "reporter": "U.S.",
      "page": "420",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 3138",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3138",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 317",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "317",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 5023",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "5023",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 140",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "140",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "468 U.S. 420",
        "volume": "468",
        "reporter": "U.S.",
        "page": "420",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 3138",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3138",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 317",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "317",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 140",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "140",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 5023",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "5023",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "468 U.S. 420",
    "official_selection": {
      "court_class": "scotus",
      "selected": "468 U.S. 420",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-434",
      "page": null,
      "quote": "requiring Miranda warnings. ## Rule Miranda applies to custodial interrogation no matter how minor the offense:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-440",
      "page": null,
      "quote": "The similarly noncoercive aspect of ordinary traffic stops prompts us to hold that persons temporarily detained pursuant to such stops are not 'in custody' for the purposes of *Miranda*.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-07-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Berkemer v. McCarty",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Louisiana v. John Noehl and Analise Noehl",
          "cluster_id": 10618700,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Poulson v. Commonwealth",
          "cluster_id": 10375911,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane1_negative"
      },
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
        "journal_ref": "Berkemer v. McCarty:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Chase Robert Griffin",
          "cluster_id": 9438185,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane1_negative"
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
        "journal_ref": "Berkemer v. McCarty:lane1_negative"
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
        "journal_ref": "Berkemer v. McCarty:lane1_negative"
      },
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
        "journal_ref": "Berkemer v. McCarty:lane1_negative"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Siegert v. Gilley",
          "cluster_id": 112594,
          "cite": [
            "114 L. Ed. 2d 277",
            "111 S. Ct. 1789",
            "500 U.S. 226",
            "1991 U.S. LEXIS 2909",
            "59 U.S.L.W. 4465"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Caballes",
          "cluster_id": 137742,
          "cite": [
            "160 L. Ed. 2d 842",
            "125 S. Ct. 834",
            "543 U.S. 405",
            "2005 U.S. LEXIS 769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dickerson v. United States",
          "cluster_id": 118380,
          "cite": [
            "147 L. Ed. 2d 405",
            "120 S. Ct. 2326",
            "530 U.S. 428",
            "2000 U.S. LEXIS 4305"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Johnson",
          "cluster_id": 145912,
          "cite": [
            "172 L. Ed. 2d 694",
            "129 S. Ct. 781",
            "555 U.S. 323",
            "2009 U.S. LEXIS 868"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brendlin v. California",
          "cluster_id": 145712,
          "cite": [
            "168 L. Ed. 2d 132",
            "127 S. Ct. 2400",
            "551 U.S. 249",
            "2007 U.S. LEXIS 7897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of Trustees of State Univ. of NY v. Fox",
          "cluster_id": 112329,
          "cite": [
            "106 L. Ed. 2d 388",
            "109 S. Ct. 3028",
            "492 U.S. 469",
            "1989 U.S. LEXIS 3289",
            "57 U.S.L.W. 5015"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Taylor v. Freeland & Kronz",
          "cluster_id": 112725,
          "cite": [
            "118 L. Ed. 2d 280",
            "112 S. Ct. 1644",
            "503 U.S. 638",
            "1992 U.S. LEXIS 2546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Yee v. City of Escondido",
          "cluster_id": 112719,
          "cite": [
            "118 L. Ed. 2d 153",
            "112 S. Ct. 1522",
            "503 U.S. 519",
            "1992 U.S. LEXIS 2115"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.",
          "cluster_id": 136990,
          "cite": [
            "159 L. Ed. 2d 292",
            "124 S. Ct. 2451",
            "542 U.S. 177",
            "2004 U.S. LEXIS 4385",
            "17 Fla. L. Weekly Fed. S 406",
            "72 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Knowles v. Iowa",
          "cluster_id": 118250,
          "cite": [
            "142 L. Ed. 2d 492",
            "119 S. Ct. 484",
            "525 U.S. 113",
            "1998 U.S. LEXIS 8068"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Lee Rusher, United States of America v. Sarah Jean Shoemaker Rusher, A/K/A Sarah Anne Rusher, United States of America v. James Joseph Flannery, A/K/A James Joseph Fleming, A/K/A Richard J. Mutschler",
          "cluster_id": 584528,
          "cite": [
            "966 F.2d 868",
            "1992 U.S. App. LEXIS 12338"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111249 OR 9429728 OR 9429729) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTk0MDgwMDAwMDAwJnM9MTAwMTkyNDAmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111249+OR+9429728+OR+9429729%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111249 OR 9429728 OR 9429729)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00Mjkmcz0zOTQxMzE2JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111249+OR+9429728+OR+9429729%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111249 OR 9429728 OR 9429729)",
        "reviewed": 116,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 5,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 116,
        "triage_read": 5,
        "triage_snippet_classified": 111
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111249 OR 9429728 OR 9429729)",
    "indexed_citing_opinions": 3076,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111249,
        "count": 2653,
        "count_source": "search"
      },
      {
        "opinion_id": 9429728,
        "count": 474,
        "count_source": "search"
      },
      {
        "opinion_id": 9429729,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4858,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/berkemer-v-mccarty.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzODE3OTYmcz0xMDU5NzQ3NCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111249+OR+9429728+OR+9429729%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111249,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 105591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 107676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 108153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 108350,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 108585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 109252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 109430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 109587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 109930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 110032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 110183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 110245,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 110474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 110832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111101,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111110,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111211,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 279036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 282815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 283849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 338963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 421705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 424072,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1146993,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1158866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1217972,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1220711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1223447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1262034,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1325690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1381407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1430357,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1592530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1725045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1935505,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1939088,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1981202,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 2011645,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 2086722,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 2102837,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 2380940,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 2452444,
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
    "date_created": "2026-07-04T19:55:03Z",
    "date_modified": "2026-07-06T07:20:20Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T19:55:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T19:55:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:59:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T19:55:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### lake record — Brown v. Texas

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brown v. Texas",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Brown v. Texas",
    "case_name_short": "Brown",
    "case_name_full": "Brown v. Texas",
    "input_case_name": "Brown v. Texas",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-06-25",
    "year": 1979,
    "docket": null,
    "cluster_id": 110128,
    "lead_opinion_id": 110128,
    "sibling_ids": [
      110128
    ],
    "absolute_url": "/opinion/110128/brown-v-texas/",
    "identity_method": "pending",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9021114,
        "score": 10,
        "case_name": "Brown v. Texas"
      },
      {
        "cluster_id": 9020748,
        "score": 10,
        "case_name": "Brown v. Texas"
      }
    ],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "443 U.S. 47",
      "volume": "443",
      "reporter": "U.S.",
      "page": "47",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 2637",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2637",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 357",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "357",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 136",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "136",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "443 U.S. 47",
        "volume": "443",
        "reporter": "U.S.",
        "page": "47",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 2637",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2637",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 357",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "357",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 136",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "136",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "443 U.S. 47",
    "official_selection": {
      "court_class": "scotus",
      "selected": "443 U.S. 47",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-51",
      "page": null,
      "quote": "but could point to no specific facts; he acknowledged the only reason for the stop was to ascertain Brown's identity. Brown refused to identify himself and was arrested and convicted under a Texas statute (\u00a7 38.02) making it a crime to refuse to give one's name to an officer who has lawfully stopped him. ## Issue Whether officers may detain an individual and require him to identify himself, on penalty of criminal punishment for refusing, when they lack reasonable suspicion that he is engaged in criminal activity. ## Rule No. The constitutionality of a seizure short of arrest is judged by a balancing test:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-51b",
      "page": null,
      "quote": "the Fourth Amendment requires that a seizure must be based on specific, objective facts indicating that society's legitimate interests require the seizure of the particular individual, or that the seizure must be carried out pursuant to a plan embodying explicit, neutral limitations on the conduct of individual officers.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-53",
      "page": null,
      "quote": "## Application The officers had no such basis. One could say only that the alley",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1979-06-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Brown v. Texas",
    "varies_by_point": false,
    "scope_note": "Good law. Police may not detain a person and demand identification without reasonable suspicion; the case supplies the three-factor balancing test for suspicionless seizures. Hiibel v. Sixth Judicial Dist. Court (2004) later upheld an identify-yourself demand during a lawful Terry stop \u2014 the question Brown expressly reserved \u2014 and does not disturb Brown.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 10843215,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cobb",
          "cluster_id": 9352626,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cobb",
          "cluster_id": 6466320,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sievers - supplemental opinion",
          "cluster_id": 4571040,
          "cite": [
            "301 Neb. 806",
            "920 N.W.2d 443"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Baskins",
          "cluster_id": 4524209,
          "cite": [
            "818 S.E.2d 381",
            "260 N.C. App. 589"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Christian",
          "cluster_id": 4477521,
          "cite": [
            "2018 Ohio 957",
            "109 N.E.3d 183"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hairston",
          "cluster_id": 4426228,
          "cite": [
            "2017 Ohio 7612",
            "97 N.E.3d 784"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Elvis Elvis Ramirez-Tamayo v. State",
          "cluster_id": 4311099,
          "cite": [
            "501 S.W.3d 788",
            "2016 Tex. App. LEXIS 10905",
            "2016 WL 5874327"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ashworth",
          "cluster_id": 4243394,
          "cite": [
            "790 S.E.2d 173",
            "248 N.C. App. 649",
            "2016 N.C. App. LEXIS 816"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Carlos Gonzalez v. Able Huerta",
          "cluster_id": 3216824,
          "cite": [
            "826 F.3d 854",
            "2016 U.S. App. LEXIS 11530",
            "2016 WL 3457258"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Leming v. State",
          "cluster_id": 5447022,
          "cite": [
            "493 S.W.3d 552",
            "2016 WL 1458242",
            "2016 Tex. Crim. App. LEXIS 73"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mocek v. City of Albuquerque",
          "cluster_id": 3164764,
          "cite": [
            "813 F.3d 912",
            "2015 U.S. App. LEXIS 22435",
            "2015 WL 9298662"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Mercedes-De la Cruz",
          "cluster_id": 2803337,
          "cite": [
            "787 F.3d 61",
            "2015 U.S. App. LEXIS 8624",
            "2015 WL 3378255"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Illinois v. Gates",
          "cluster_id": 110959,
          "cite": [
            "76 L. Ed. 2d 527",
            "103 S. Ct. 2317",
            "462 U.S. 213",
            "1983 U.S. LEXIS 54",
            "51 U.S.L.W. 4709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Royer",
          "cluster_id": 110890,
          "cite": [
            "75 L. Ed. 2d 229",
            "103 S. Ct. 1319",
            "460 U.S. 491",
            "1983 U.S. LEXIS 151",
            "51 U.S.L.W. 4293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mendenhall",
          "cluster_id": 110264,
          "cite": [
            "64 L. Ed. 2d 497",
            "100 S. Ct. 1870",
            "446 U.S. 544",
            "1980 U.S. LEXIS 102"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cortez",
          "cluster_id": 110377,
          "cite": [
            "66 L. Ed. 2d 621",
            "101 S. Ct. 690",
            "449 U.S. 411",
            "1981 U.S. LEXIS 58",
            "49 U.S.L.W. 4099"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Bostick",
          "cluster_id": 112631,
          "cite": [
            "115 L. Ed. 2d 389",
            "111 S. Ct. 2382",
            "501 U.S. 429",
            "1991 U.S. LEXIS 3625",
            "59 U.S.L.W. 4708",
            "91 Daily Journal DAR 7328",
            "91 Cal. Daily Op. Serv. 4671",
            "1991 WL 105224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Wardlow",
          "cluster_id": 118326,
          "cite": [
            "145 L. Ed. 2d 570",
            "120 S. Ct. 673",
            "528 U.S. 119",
            "2000 U.S. LEXIS 504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Hodari D.",
          "cluster_id": 112579,
          "cite": [
            "113 L. Ed. 2d 690",
            "111 S. Ct. 1547",
            "499 U.S. 621",
            "1991 U.S. LEXIS 2397",
            "91 Cal. Daily Op. Serv. 2893",
            "59 U.S.L.W. 4335",
            "91 Daily Journal DAR 4665"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kolender v. Lawson",
          "cluster_id": 110926,
          "cite": [
            "75 L. Ed. 2d 903",
            "103 S. Ct. 1855",
            "461 U.S. 352",
            "1983 U.S. LEXIS 159",
            "51 U.S.L.W. 4532"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rawlings v. Kentucky",
          "cluster_id": 110326,
          "cite": [
            "65 L. Ed. 2d 633",
            "100 S. Ct. 2556",
            "448 U.S. 98",
            "1980 U.S. LEXIS 142"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hensley",
          "cluster_id": 111294,
          "cite": [
            "83 L. Ed. 2d 604",
            "105 S. Ct. 675",
            "469 U.S. 221",
            "1985 U.S. LEXIS 34",
            "53 U.S.L.W. 4053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Summers",
          "cluster_id": 110534,
          "cite": [
            "69 L. Ed. 2d 340",
            "101 S. Ct. 2587",
            "452 U.S. 692",
            "1981 U.S. LEXIS 118",
            "49 U.S.L.W. 4776"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. Delgado",
          "cluster_id": 111148,
          "cite": [
            "80 L. Ed. 2d 247",
            "104 S. Ct. 1758",
            "466 U.S. 210",
            "1984 U.S. LEXIS 57",
            "52 U.S.L.W. 4436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ford v. State",
          "cluster_id": 1355298,
          "cite": [
            "158 S.W.3d 488",
            "2005 Tex. Crim. App. LEXIS 399",
            "2005 WL 544796"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 1828048,
          "cite": [
            "433 So. 2d 688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan Department of State Police v. Sitz",
          "cluster_id": 112459,
          "cite": [
            "110 L. Ed. 2d 412",
            "110 S. Ct. 2481",
            "496 U.S. 444",
            "1990 U.S. LEXIS 3144",
            "58 U.S.L.W. 4781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reid v. Georgia",
          "cluster_id": 110336,
          "cite": [
            "65 L. Ed. 2d 890",
            "100 S. Ct. 2752",
            "448 U.S. 438",
            "1980 U.S. LEXIS 148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wyoming v. Houghton",
          "cluster_id": 118277,
          "cite": [
            "143 L. Ed. 2d 408",
            "119 S. Ct. 1297",
            "526 U.S. 295",
            "1999 U.S. LEXIS 2347"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.",
          "cluster_id": 136990,
          "cite": [
            "159 L. Ed. 2d 292",
            "124 S. Ct. 2451",
            "542 U.S. 177",
            "2004 U.S. LEXIS 4385",
            "17 Fla. L. Weekly Fed. S 406",
            "72 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schall v. Martin",
          "cluster_id": 111198,
          "cite": [
            "81 L. Ed. 2d 207",
            "104 S. Ct. 2403",
            "467 U.S. 253",
            "1984 U.S. LEXIS 96",
            "52 U.S.L.W. 4681"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Howard",
          "cluster_id": 5684310,
          "cite": [
            "50 N.Y.2d 583",
            "408 N.E.2d 908",
            "430 N.Y.S.2d 578",
            "1980 N.Y. LEXIS 2454"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110128) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzkyNzY4MDAwMDAwJnM9MjY3OTQ2MSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110128%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 13,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(110128)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNzEmcz0yOTQ3NzE2JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110128%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110128)",
        "reviewed": 32,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 32,
        "triage_read": 1,
        "triage_snippet_classified": 31
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110128)",
    "indexed_citing_opinions": 1635,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110128,
        "count": 1635,
        "count_source": "search"
      }
    ],
    "citation_count": 2680,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brown-v-texas.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1MjY3NCZzPTk0Mzg0MTMmdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28110128%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110128,
        "cited_id": 103170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 246074,
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
    "date_created": "2026-07-04T20:53:09Z",
    "date_modified": "2026-07-06T07:26:24Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:53:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:53:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:56:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:53:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### lake record — Hiibel v. Sixth Judicial Dist. Court

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hiibel v. Sixth Judicial Dist. Court",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.",
    "case_name_short": "Hiibel",
    "case_name_full": "HIIBEL v. SIXTH JUDICIAL DISTRICT COURT OF NEVADA, HUMBOLDT COUNTY, Et Al.",
    "input_case_name": "Hiibel v. Sixth Judicial Dist. Court",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-06-21",
    "year": 2004,
    "docket": null,
    "cluster_id": 136990,
    "lead_opinion_id": 136990,
    "sibling_ids": [
      136990,
      9434645,
      9434646,
      9434647
    ],
    "absolute_url": "/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "542 U.S. 177",
        "volume": "542",
        "reporter": "U.S.",
        "page": "177",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 2451",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2451",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "159 L. Ed. 2d 292",
        "volume": "159",
        "reporter": "L. Ed. 2d",
        "page": "292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fla. L. Weekly Fed. S 406",
        "volume": "17",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "406",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 U.S.L.W. 4509",
        "volume": "72",
        "reporter": "U.S.L.W.",
        "page": "4509",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 4385",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "4385",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "542 U.S. 177",
        "volume": "542",
        "reporter": "U.S.",
        "page": "177",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 2451",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2451",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "159 L. Ed. 2d 292",
        "volume": "159",
        "reporter": "L. Ed. 2d",
        "page": "292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 4385",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "4385",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fla. L. Weekly Fed. S 406",
        "volume": "17",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "406",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 U.S.L.W. 4509",
        "volume": "72",
        "reporter": "U.S.L.W.",
        "page": "4509",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "scotus",
      "selected": null,
      "reason": "unlisted_reporter:Fla. L. Weekly Fed. S"
    }
  },
  "pinpoints": [
    {
      "id": "pin-186",
      "page": null,
      "quote": "statute requiring a person detained on reasonable suspicion to disclose his name. ## Issue Whether a state stop-and-identify law that compels a suspect to disclose his name during a valid *Terry* stop is consistent with the Fourth Amendment. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-187",
      "page": null,
      "quote": "[t]he principles of Terry permit a State to require a suspect to disclose his name in the course of a Terry stop.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-188",
      "page": null,
      "quote": "[a] state law requiring a suspect to disclose his name in the course of a valid Terry stop is consistent with Fourth Amendment prohibitions against unreasonable searches and seizures.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2004-06-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hiibel v. Sixth Judicial Dist. Court",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Tanguay",
          "cluster_id": 4598184,
          "cite": [
            "918 F.3d 1"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Young",
          "cluster_id": 4460263,
          "cite": [
            "2018 Ohio 164",
            "104 N.E.3d 128"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Carlos Gonzalez v. Able Huerta",
          "cluster_id": 3216824,
          "cite": [
            "826 F.3d 854",
            "2016 U.S. App. LEXIS 11530",
            "2016 WL 3457258"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
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
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mocek v. City of Albuquerque",
          "cluster_id": 3164764,
          "cite": [
            "813 F.3d 912",
            "2015 U.S. App. LEXIS 22435",
            "2015 WL 9298662"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cruz, Adelfo Ramirez",
          "cluster_id": 2950538,
          "cite": [
            "461 S.W.3d 531",
            "2015 Tex. Crim. App. LEXIS 561",
            "2015 WL 2236982"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Prall v. City of Boston",
          "cluster_id": 8729956,
          "cite": [
            "985 F. Supp. 2d 115",
            "2013 WL 6076462",
            "2013 U.S. Dist. LEXIS 166128"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kareen Rasul Griffin",
          "cluster_id": 809546,
          "cite": [
            "696 F.3d 1354",
            "2012 WL 4496817",
            "2012 U.S. App. LEXIS 20543"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Davis v. Washington",
          "cluster_id": 145641,
          "cite": [
            "165 L. Ed. 2d 224",
            "126 S. Ct. 2266",
            "547 U.S. 813",
            "2006 U.S. LEXIS 4886"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
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
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Caballes",
          "cluster_id": 137742,
          "cite": [
            "160 L. Ed. 2d 842",
            "125 S. Ct. 834",
            "543 U.S. 405",
            "2005 U.S. LEXIS 769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Bryant",
          "cluster_id": 2959736,
          "cite": [
            "179 L. Ed. 2d 93",
            "131 S. Ct. 1143",
            "562 U.S. 344",
            "2011 U.S. LEXIS 1713"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Laurie Tsao v. Desert Palace, Inc.",
          "cluster_id": 810771,
          "cite": [
            "698 F.3d 1128",
            "2012 WL 5200336"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. King",
          "cluster_id": 873669,
          "cite": [
            "186 L. Ed. 2d 1",
            "133 S. Ct. 1958",
            "2013 U.S. LEXIS 4165",
            "569 U.S. 435",
            "24 Fla. L. Weekly Fed. S 234",
            "81 U.S.L.W. 4343",
            "2013 WL 2371466"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cortez v. McCauley",
          "cluster_id": 167088,
          "cite": [
            "478 F.3d 1108",
            "2007 WL 503819"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scroggins",
          "cluster_id": 71470,
          "cite": [
            "599 F.3d 433",
            "2010 U.S. App. LEXIS 4551",
            "2010 WL 724688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Letner and Tobin",
          "cluster_id": 2630926,
          "cite": [
            "235 P.3d 62",
            "50 Cal. 4th 99",
            "112 Cal. Rptr. 3d 746",
            "2010 Cal. LEXIS 7290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Koch v. City of Del City",
          "cluster_id": 616534,
          "cite": [
            "660 F.3d 1228",
            "2011 U.S. App. LEXIS 22095",
            "2011 WL 5176164"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cady, Davy v. Sheahan, Michael",
          "cluster_id": 2999846,
          "cite": [
            "467 F.3d 1057",
            "2006 WL 3113670"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Woodard",
          "cluster_id": 2540788,
          "cite": [
            "341 S.W.3d 404",
            "2011 Tex. Crim. App. LEXIS 447",
            "2011 WL 1261320"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hosvaldo Lopez",
          "cluster_id": 797423,
          "cite": [
            "482 F.3d 1067",
            "2007 WL 725641",
            "2007 U.S. App. LEXIS 5709"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Pineiro",
          "cluster_id": 1980861,
          "cite": [
            "853 A.2d 887",
            "181 N.J. 13",
            "2004 N.J. LEXIS 931"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Center for Bio-Ethical Reform, Inc. v. Los Angeles County Sheriff Department",
          "cluster_id": 1235108,
          "cite": [
            "533 F.3d 780",
            "2008 U.S. App. LEXIS 13975",
            "2008 WL 2599683"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Kerwick, Stacie Michelle",
          "cluster_id": 2948618,
          "cite": [
            "393 S.W.3d 270",
            "2013 WL 690840",
            "2013 Tex. Crim. App. LEXIS 430"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Castleberry",
          "cluster_id": 2282066,
          "cite": [
            "332 S.W.3d 460",
            "2011 Tex. Crim. App. LEXIS 283",
            "2011 WL 709697"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morris v. Noe",
          "cluster_id": 623700,
          "cite": [
            "672 F.3d 1185",
            "2012 WL 604170",
            "2012 U.S. App. LEXIS 3927"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Arnold",
          "cluster_id": 797722,
          "cite": [
            "486 F.3d 177",
            "73 Fed. R. Serv. 583",
            "2007 U.S. App. LEXIS 11616",
            "2007 WL 1452230"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Waters v. B. Madson",
          "cluster_id": 4609057,
          "cite": [
            "921 F.3d 725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillip Turner v. Driver",
          "cluster_id": 4349754,
          "cite": [
            "848 F.3d 678",
            "2017 WL 650186",
            "2017 U.S. App. LEXIS 2769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Cameron Kincade",
          "cluster_id": 787362,
          "cite": [
            "379 F.3d 813",
            "2004 U.S. App. LEXIS 17191",
            "2004 WL 1837840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Derrick L. Foster",
          "cluster_id": 787028,
          "cite": [
            "376 F.3d 577",
            "65 Fed. R. Serv. 1",
            "2004 U.S. App. LEXIS 15267",
            "2004 WL 1606725"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. City of New York",
          "cluster_id": 2828542,
          "cite": [
            "798 F.3d 94",
            "2015 U.S. App. LEXIS 14517",
            "2015 WL 4924395"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(136990 OR 9434645 OR 9434646 OR 9434647) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzEzNDUyODAwMDAwJnM9Mjk5MTYwNCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28136990+OR+9434645+OR+9434646+OR+9434647%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(136990 OR 9434645 OR 9434646 OR 9434647)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTMmcz0xNDI3ODc4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28136990+OR+9434645+OR+9434646+OR+9434647%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(136990 OR 9434645 OR 9434646 OR 9434647)",
        "reviewed": 26,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 26,
        "triage_read": 0,
        "triage_snippet_classified": 26
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(136990 OR 9434645 OR 9434646 OR 9434647)",
    "indexed_citing_opinions": 480,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 136990,
        "count": 392,
        "count_source": "search"
      },
      {
        "opinion_id": 9434645,
        "count": 95,
        "count_source": "search"
      },
      {
        "opinion_id": 9434646,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434647,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 890,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hiibel-v-sixth-judicial-dist-court.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg0NjEyODUmcz05NDI4NDMyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28136990+OR+9434645+OR+9434646+OR+9434647%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 136990,
        "cited_id": 93149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 104912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108472,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108965,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 109432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110426,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 111378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 111382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 112123,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 112464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 118326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 127927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 134724,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 1087666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 2621305,
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
    "date_created": "2026-07-05T07:06:13Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:06:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:06:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:10:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:06:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### lake record — Kolender v. Lawson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kolender v. Lawson",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Kolender v. Lawson",
    "case_name_short": "Kolender",
    "case_name_full": "KOLENDER, CHIEF OF POLICE OF SAN DIEGO, Et Al. v. LAWSON",
    "input_case_name": "Kolender v. Lawson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-05-02",
    "year": 1983,
    "docket": null,
    "cluster_id": 110926,
    "lead_opinion_id": 9429183,
    "sibling_ids": [
      110926,
      9429183,
      9429184,
      9429185
    ],
    "absolute_url": "/opinion/110926/kolender-v-lawson/",
    "identity_method": "pending",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "461 U.S. 352",
      "volume": "461",
      "reporter": "U.S.",
      "page": "352",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 1855",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1855",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 903",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "903",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4532",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4532",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 159",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "159",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "461 U.S. 352",
        "volume": "461",
        "reporter": "U.S.",
        "page": "352",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 1855",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1855",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 903",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "903",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 159",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "159",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4532",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4532",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "461 U.S. 352",
    "official_selection": {
      "court_class": "scotus",
      "selected": "461 U.S. 352",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-353",
      "page": null,
      "quote": "identification is unconstitutionally vague under the Due Process Clause. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-357",
      "page": null,
      "quote": "the void-for-vagueness doctrine requires that a penal statute define the criminal offense with sufficient definiteness that ordinary people can understand what conduct is prohibited and in a manner that does not encourage arbitrary and discriminatory enforcement.",
      "star_marker": "357",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 6679,
      "fragment": "#:~:text=the%20void%2Dfor%2Dvagueness%20doctrine%20requires%20that",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-358",
      "page": null,
      "quote": "contains no standard for determining what a suspect has to do in order to satisfy the requirement to provide a 'credible and reliable' identification. As such, the statute vests virtually complete discretion in the hands of the police to determine whether the suspect has satisfied the statute and must be permitted to go on his way in the absence of probable cause to arrest.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1983-05-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Kolender v. Lawson",
    "varies_by_point": false,
    "scope_note": "Good law. A stop-and-identify statute requiring a suspect to provide 'credible and reliable' identification is void for vagueness (Fourteenth Amendment Due Process) because it gives police standardless discretion. Hiibel v. Sixth Judicial Dist. Court (2004) distinguished Kolender, upholding a narrower statute that required only that the suspect state his name.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Manning v. Caldwell for City of Roanoke",
          "cluster_id": 4639944,
          "cite": [
            "930 F.3d 264"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Demott",
          "cluster_id": 8443719,
          "cite": [
            "906 F.3d 231"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dianna Helmers v. City of Des Moines",
          "cluster_id": 4483928,
          "cite": [
            "918 N.W.2d 501"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Illinois v. Gates",
          "cluster_id": 110959,
          "cite": [
            "76 L. Ed. 2d 527",
            "103 S. Ct. 2317",
            "462 U.S. 213",
            "1983 U.S. LEXIS 54",
            "51 U.S.L.W. 4709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. United States",
          "cluster_id": 2812210,
          "cite": [
            "576 U.S. 591",
            "135 S. Ct. 2551",
            "192 L. Ed. 2d 569",
            "2015 U.S. LEXIS 4251",
            "83 U.S.L.W. 4576",
            "25 Fla. L. Weekly Fed. S 459"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
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
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Place",
          "cluster_id": 110979,
          "cite": [
            "77 L. Ed. 2d 110",
            "103 S. Ct. 2637",
            "462 U.S. 696",
            "1983 U.S. LEXIS 74",
            "51 U.S.L.W. 4844"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sharpe",
          "cluster_id": 111378,
          "cite": [
            "84 L. Ed. 2d 605",
            "105 S. Ct. 1568",
            "470 U.S. 675",
            "1985 U.S. LEXIS 74",
            "53 U.S.L.W. 4346"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pruitt v. Mote",
          "cluster_id": 1218369,
          "cite": [
            "503 F.3d 647",
            "2007 U.S. App. LEXIS 23109",
            "2007 WL 2850448"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Davis",
          "cluster_id": 4632235,
          "cite": [
            "588 U.S. 445",
            "139 S. Ct. 2319",
            "2019 U.S. LEXIS 4210",
            "204 L. Ed. 2d 757"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
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
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lanier",
          "cluster_id": 118098,
          "cite": [
            "137 L. Ed. 2d 432",
            "117 S. Ct. 1219",
            "520 U.S. 259",
            "1997 U.S. LEXIS 2079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "R. A. v. v. City of St. Paul",
          "cluster_id": 112774,
          "cite": [
            "120 L. Ed. 2d 305",
            "112 S. Ct. 2538",
            "505 U.S. 377",
            "1992 U.S. LEXIS 3863"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roberts v. United States Jaycees",
          "cluster_id": 111255,
          "cite": [
            "82 L. Ed. 2d 462",
            "104 S. Ct. 3244",
            "468 U.S. 609",
            "1984 U.S. LEXIS 146",
            "52 U.S.L.W. 5076"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Isassi v. State",
          "cluster_id": 2280007,
          "cite": [
            "330 S.W.3d 633",
            "2010 Tex. Crim. App. LEXIS 1641",
            "2010 WL 3894792"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Houston v. Hill",
          "cluster_id": 111919,
          "cite": [
            "96 L. Ed. 2d 398",
            "107 S. Ct. 2502",
            "482 U.S. 451",
            "1987 U.S. LEXIS 2617",
            "55 U.S.L.W. 4823"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pacific Mutual Life Insurance v. Haslip",
          "cluster_id": 112557,
          "cite": [
            "113 L. Ed. 2d 1",
            "111 S. Ct. 1032",
            "499 U.S. 1",
            "1991 U.S. LEXIS 1306",
            "59 U.S.L.W. 4157",
            "18 Media L. Rep. (BNA) 1753",
            "91 Daily Journal DAR 2599",
            "91 Cal. Daily Op. Serv. 1626"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hill v. Colorado",
          "cluster_id": 118385,
          "cite": [
            "147 L. Ed. 2d 597",
            "120 S. Ct. 2480",
            "530 U.S. 703",
            "2000 U.S. LEXIS 4486"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Chicago v. Morales",
          "cluster_id": 118299,
          "cite": [
            "144 L. Ed. 2d 67",
            "119 S. Ct. 1849",
            "527 U.S. 41",
            "1999 U.S. LEXIS 4005"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James v. United States",
          "cluster_id": 145743,
          "cite": [
            "167 L. Ed. 2d 532",
            "127 S. Ct. 1586",
            "550 U.S. 192",
            "2007 U.S. LEXIS 4337"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Boos v. Barry",
          "cluster_id": 112027,
          "cite": [
            "99 L. Ed. 2d 333",
            "108 S. Ct. 1157",
            "485 U.S. 312",
            "1988 U.S. LEXIS 1445"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Secretary of State of Md. v. Joseph H. Munson Co.",
          "cluster_id": 111226,
          "cite": [
            "81 L. Ed. 2d 786",
            "104 S. Ct. 2839",
            "467 U.S. 947",
            "1984 U.S. LEXIS 123",
            "52 U.S.L.W. 4875"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Skilling v. United States",
          "cluster_id": 149286,
          "cite": [
            "561 U.S. 358",
            "130 S. Ct. 2896",
            "177 L. Ed. 2d 619",
            "2010 U.S. LEXIS 5259"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Montoya De Hernandez",
          "cluster_id": 111509,
          "cite": [
            "87 L. Ed. 2d 381",
            "105 S. Ct. 3304",
            "473 U.S. 531",
            "1985 U.S. LEXIS 120",
            "53 U.S.L.W. 5048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sessions v. Dimaya",
          "cluster_id": 4487345,
          "cite": [
            "584 U.S. 148",
            "138 S. Ct. 1204",
            "200 L. Ed. 2d 549",
            "2018 U.S. LEXIS 2497"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Osborne v. Ohio",
          "cluster_id": 112417,
          "cite": [
            "109 L. Ed. 2d 98",
            "110 S. Ct. 1691",
            "495 U.S. 103",
            "1990 U.S. LEXIS 2036"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.",
          "cluster_id": 136990,
          "cite": [
            "159 L. Ed. 2d 292",
            "124 S. Ct. 2451",
            "542 U.S. 177",
            "2004 U.S. LEXIS 4385",
            "17 Fla. L. Weekly Fed. S 406",
            "72 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clark v. Martinez",
          "cluster_id": 137741,
          "cite": [
            "160 L. Ed. 2d 734",
            "125 S. Ct. 716",
            "543 U.S. 371",
            "2005 U.S. LEXIS 627"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110926 OR 9429183 OR 9429184 OR 9429185) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTIxMDcyMDAwMDAwJnM9NDQ3NzkwMSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110926+OR+9429183+OR+9429184+OR+9429185%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110926 OR 9429183 OR 9429184 OR 9429185)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00Nzgmcz0xNzIxOTImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110926+OR+9429183+OR+9429184+OR+9429185%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110926 OR 9429183 OR 9429184 OR 9429185)",
        "reviewed": 69,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 69,
        "triage_read": 0,
        "triage_snippet_classified": 69
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110926 OR 9429183 OR 9429184 OR 9429185)",
    "indexed_citing_opinions": 2222,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110926,
        "count": 1927,
        "count_source": "search"
      },
      {
        "opinion_id": 9429183,
        "count": 345,
        "count_source": "search"
      },
      {
        "opinion_id": 9429184,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429185,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3308,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/kolender-v-lawson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzOTA5OTYmcz0xMDYwMTgzOSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110926+OR+9429183+OR+9429184+OR+9429185%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110926,
        "cited_id": 89266,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 91256,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 96198,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 100759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 102991,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 103170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 103243,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 103305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 103347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 104453,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 104532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 105716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 106514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 106884,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 107869,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 108335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 108472,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 108598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 108876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 108965,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 108985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 108988,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 109077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 109134,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 109253,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 109335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 109966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 110127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 110661,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 280147,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 393990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 2138359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 2169575,
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
    "date_created": "2026-07-05T10:24:36Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:26:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:26:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:29:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:26:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

---
