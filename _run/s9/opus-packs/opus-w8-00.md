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

## GROUP: _overhaul2/lake/cases/Milam v. United States.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Milam v. United States
type: case
citation: "296 F. 629 (1924)"
parallel_cite: ""
neutral_cite: 1924 U.S. App. LEXIS 3380
court: 4th Cir.
court_level: coa
circuit: ca4
year: 1924
date_decided: ""
docket: ""
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
  opinion_url: "https://www.courtlistener.com/opinion/8849836/milam-v-united-states/"
  cluster_id: 8849836
  opinion_id: null
  identity_checked: true
lake:
  record_id: Milam v. United States
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Fourth Amendment Recalibration]]"
    role: Key
related:
  - "[[Fourth Amendment Recalibration]]"
  - "[[Carroll v. United States]]"
tags:
  - case
  - fourth-amendment
  - automobile-search
  - prohibition
  - reasonableness
  - living-constitution
holding: "The meaning of 'unreasonable searches' is not fixed but changes with social, economic, and legal conditions; on that reasoning the warrantless stop and search of a truck (which turned up smuggled persons rather than the expected liquor) was not unreasonable and the evidence was competent."
---

# Milam v. United States

*296 F. 629 (4th Cir. 1924)* · U.S. Court of Appeals for the Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 8849836 → opinion 8835196 (296 F. 629, decided 1924-02-08 per CourtListener; the lake stub's date_decided is empty — noted for recovery). Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Federal prohibition officers, tipped that an automobile loaded with whisky was en route from Florida, watched a bridge in Dinwiddie County, Virginia, for several days. Near midnight they stopped a motor truck; when Milam said it held "nothing," an officer opened the door and instead found eighteen Chinese immigrants being unlawfully transported. Milam and codefendants were convicted, and challenged the admission of evidence obtained by the warrantless search.

## Issue
Whether the warrantless stop and search of a motor vehicle, conducted on information of criminal activity, yields inadmissible evidence, and how the reasonableness of such a search should be judged.

## Rule
Writing a year before the Supreme Court's *[[Carroll v. United States|Carroll]]* decision, the Fourth Circuit declined to extend the exclusionary rule beyond then-existing Supreme Court precedent and framed reasonableness as an evolving standard: "The constitutional expression, 'unreasonable searches,' is not fixed and absolute in meaning. The meaning in some degree must change with changing social, economic and legal conditions." — 296 F. at 631. Applying that view to a vehicle stopped on definite information, the court held: "Assuming that this was a search of the truck, under these circumstances we hold that the search was not unreasonable, and that the evidence obtained was competent." — *Id.* at 632.

## Application
The court distinguished the warrantless search of a dwelling (generally unlawful) from the search of a mobile vehicle for evidence of crime, which the Supreme Court had not condemned. Given the officers' definite information and the mobility of the truck, the intrusion was reasonable; that the officers expected liquor but found smuggled persons did not render the otherwise-valid search unlawful.

## Conclusion
The convictions were largely **affirmed** (with a modification reducing the number of conspiracies proved); the warrantless vehicle search was reasonable and its fruits admissible.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Milam* is an early marker in the Fourth Amendment's long recalibration: its statement that "unreasonable" is not a fixed quantity but shifts with conditions anticipated the mobility-based automobile reasoning the Supreme Court would adopt in *[[Carroll v. United States]]* (1925), and it illustrates how courts have repeatedly reset the reasonableness balance as technology and enforcement needs change.

## Appears on
- [[Fourth Amendment Recalibration]] — *Key*

## Sources
- [*Milam v. United States*, 296 F. 629 (4th Cir. 1924)](https://www.courtlistener.com/opinion/8849836/milam-v-united-states/) — pinpoints: 631 (the "not fixed and absolute" recalibration passage), 632 (the reasonableness holding); Rule quotes string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "51f1cc41945a5299", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Milam v. United States"}, "payload": {"all": [{"cite": "296 F. 629", "page": "629", "reporter": "F.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "296"}, {"cite": "1924 U.S. App. LEXIS 3380", "page": "3380", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1924"}], "display": "296 F. 629", "official": {"cite": "296 F. 629", "page": "629", "reporter": "F.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "296"}, "official_selection_present": true, "record_id": "Milam v. United States"}}
{"assertion_id": "1431bf707f4fa962", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Milam v. United States"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Milam v. United States", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Milam v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Milam v. United States",
  "status": "under_review",
  "identity": {
    "case_name": "Milam v. United States",
    "case_name_short": "Milam",
    "case_name_full": "MILAM v. UNITED STATES",
    "input_case_name": "Milam v. United States",
    "court": "4th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca4",
    "state": null,
    "date_decided": null,
    "year": 1924,
    "docket": null,
    "cluster_id": 8849836,
    "lead_opinion_id": 8835196,
    "sibling_ids": [],
    "absolute_url": "/opinion/8849836/milam-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "296 F. 629",
      "volume": "296",
      "reporter": "F.",
      "page": "629",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1924 U.S. App. LEXIS 3380",
        "volume": "1924",
        "reporter": "U.S. App. LEXIS",
        "page": "3380",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "296 F. 629",
        "volume": "296",
        "reporter": "F.",
        "page": "629",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1924 U.S. App. LEXIS 3380",
        "volume": "1924",
        "reporter": "U.S. App. LEXIS",
        "page": "3380",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "296 F. 629",
    "official_selection": {
      "court_class": "coa",
      "selected": "296 F. 629",
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
    "date_created": "2026-07-07T01:37:44Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:37:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:37:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:37:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:37:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "milam-v-united-states--8849836",
      "to_record_id": "Milam v. United States",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Milam v. United States

```
<opinion type="majority">
<author id="b651-22">WOODS, Circuit Judge.</author>
<p id="AlT1">There was a general verdict of guilty on an indictment containing four counts, each charging a separate conspiracy to conceal, harbor, transport, and convey persons of Chinese descent not.duly admitted into the United Statés by an immigration inspector, nor entitled to reside in the United States. The chinaman <page-number citation-index="1" label="630">*630</page-number>mentioned in the first count was'Moy Gong Chue, alias Lee Chu; in the second, Tong Yuen, alias Poy Jong; in the third, Gee Yuen, alias Toi Lock. In the fourth count 18 Chinamen were mentioned by name, including those mentioned in the first, second, and third counts. The sentence was that the defendants—</p>
<blockquote id="b652-4">“each be imprisoned in the penitentiary at- Atlanta, Ga., for the period of two years under, each of the three counts of the indictment, said terms of imprisonment to commence in.each instance at the expiration of the term of two years on each of the three counts.”</blockquote>
<p id="b652-5">It does not clearly appear which three of the four counts was referred to in the sentence, but, as the fourth embraced the other three, it seems fair to refer the sentence to the first three counts. The court refused a motion to direct a verdict of acquittal, made on the grounds: First, that the Immigration Act of February 5, 1917 (Comp. St. 1918, Comp. St. Ann. Supp. 1919, § 4289J4a et seq.), mentioned in the indictment, does not apply to Chinese; and, second, that the court admitted evidence obtained by illegal search, without which there would have been no basis for conviction.</p>
<p id="b652-6">The first position is disposed of by the adverse decision of the Supreme Court on the precise question. United States v. Butt, <span class="citation" data-id="99635"><a href="/opinion/99635/united-states-v-butt/" aria-description="Citation for case: United States v. Butt">254 U. S. 38</a></span>, 41 Sup. Ct. 37, <span class="citation" data-id="99635"><a href="/opinion/99635/united-states-v-butt/" aria-description="Citation for case: United States v. Butt">65 L. Ed. 119</a></span>. The evidence referred to in the second ground was obtained in this way: Federal prohibition officers, having information that an automobile loaded with whisky was on its way from Florida, via Savannah, had been on the watch for several days to intercept it at a bridge in Dinwiddie county, Va. About 10 o’clock on the night of August 16, 1922, the officers, without a search warrant, stopped at the bridge a motor truck in charge of two of the defendants. In answer to the question what was in the truck, Milam, one of them, answered, “Nothing.” One of the officers then opened the door of the truck, and discovered 18 Chinamen referred to by name in the indictment.</p>
<p id="b652-7">The decisions of the Supreme Court as to the incompetency of evidence obtained by unreasonable search and seizure are too familiar for restatement or citation. As they do not control in the( enforcement of state laws, many state courts of last resort have refused to follow them. Review of the decisions, federal and state, will be found in the notes in 3 A. L. R. 1514, 13 A. L. R. 1316, and 24 A. L. R. 1408; documents 3713 and 3781, printed for use of the Judiciary Committee of the Senate; annotation of H. R. 7294; American Bar Association Journal, August, 1922, and December, 1923; 34 Harvard Law Review, 361.</p>
<p id="b652-8">Full effect must be given here to the decisions of the Supreme Court holding that evidence obtained by an unreasonable, and therefore unlawful, search is not competent. Search of a dwelling house, possibly any house, without the authority of a search warrant, the court has declared as a general rule unlawful. But it has not declared unlawful all searches without warrant. It has not declared unlawful search without warrant of motor vehicles for intoxicating liquor or other evidence of crime. Nor has the co'urt ever explicitly decided that, if officers making an unlawful search for the discovery of evidence of one <page-number citation-index="1" label="631">*631</page-number>crime find evidence of another, the evidence so unexpectedly discovered may not be used.</p>
<p id="b653-4">We are not inclined to extend the rule of exclusion of evidence obtained by unlawful search beyond the decisions of the Supreme Court. The constitutional expression, “unreasonable searches,” is not fixed and absolute in meaning. The meaning in some degree must change with changing social, economic and legal conditions. The obligation to enforce the Eighteenth Amendment is no less solemn than that to give effect to the Fourth and Fifth Amendments. The courts are therefore under the duty of deciding what is an unreasonable search of motor cars, in the light of the mandate of the Constitution that intoxicating liquors shall not be manufactured, sold, or transported for beverage purposes. Every constitutional or statutory provision must be construed, with the purpose of giving effect, if possible, to every other constitutional and statutory provision, and in view of new conditions and circumstances in the progress of the nation and the state. Downes v. Bidwell, <span class="citation" data-id="9417865"><a href="/opinion/95504/downes-v-bidwell/" aria-description="Citation for case: Downes v. Bidwell">182 U. S. 244</a></span>, 21 Sup. Ct. 770, <span class="citation" data-id="9417865"><a href="/opinion/95504/downes-v-bidwell/" aria-description="Citation for case: Downes v. Bidwell">45 L. Ed. 1088</a></span>; South Carolina v. United States, <span class="citation" data-id="9418012"><a href="/opinion/96357/south-carolina-v-united-states/" aria-description="Citation for case: South Carolina v. United States">199 U. S. 437</a></span>, 26 Sup. Ct. 110, <span class="citation" data-id="9418012"><a href="/opinion/96357/south-carolina-v-united-states/" aria-description="Citation for case: South Carolina v. United States">50 L. Ed. 261</a></span>, 4 Ann. Cas. 737; Elrod v. Moss (C. C. A. 4th Circuit) <span class="citation" data-id="8823999"><a href="/opinion/8838892/elrod-v-moss/#129" aria-description="Citation for case: Elrod v. Moss">278 Fed. 123, 129</a></span>; Agnello v. United States (C. C. A. 2d Circuit) <span class="citation" data-id="8831130"><a href="/opinion/8845856/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">290 Fed. 671</a></span>.</p>
<p id="b653-5">In view of the difficulties of enforcing the mandate of the Eighteenth Amendment and the statutes passed in pursuance of it, we cannot shut our eyes to the fact known to everybody that the traffic in intoxicating liquors is carried on chiefly by professional criminals in motor cars. Robberies and other crimes are committed, and criminals escape by their use. To hold that such motor cars must never be stopped or searched without a search warrant would be a long step by the courts in aid of the traffic outlawed by the Constitution. The argument in favor of stopping and searching without warrant motor, cars in the effort to detect robbery and other crimes and to discover stolen goods is also very strong, but with that we are not now concerned. Objections to such searches made by officers with due courtesy and judgment generally come, not from citizens interested in the observance of the law, but from criminals who invoke the Constitution as a means of concealment of crime.</p>
<p id="b653-6">Property forfeited by reason of the crime with which it is connected is not entitled to legal protection. A person in possession of forfeited property has no right to the protection of his possession, and such forfeited property is always rightfully subject to seizure on behalf of the government. United States v. Stowell, <span class="citation" data-id="92645"><a href="/opinion/92645/united-states-v-stowell/" aria-description="Citation for case: United States v. Stowell">133 U. S. 19</a></span>, 10 Sup. Ct. 244, <span class="citation" data-id="92645"><a href="/opinion/92645/united-states-v-stowell/" aria-description="Citation for case: United States v. Stowell">33 L. Ed. 555</a></span>; Taylor v. United States, <span class="citation" data-id="86316"><a href="/opinion/86316/taylor-v-united-states/#205" aria-description="Citation for case: Taylor v. United States">3 How. 197, 205</a></span>, <span class="citation" data-id="86316"><a href="/opinion/86316/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">11 L. Ed. 559</a></span>; Boyd v. United States (4th Circuit) <span class="citation" data-id="8829028"><a href="/opinion/8843807/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">286 Fed. 930</a></span>; United States v. Welsh (D. C.) <span class="citation" data-id="8806081"><a href="/opinion/8821422/united-states-v-welsh/" aria-description="Citation for case: United States v. Welsh">247 Fed. 239</a></span>. Search and seizure of automobiles without search warrant in enforcement of the National Prohibition Act (Comp. St. Ann. Supp. 1923, §■ 10138% et seq.) has been justified on this ground. United States v. Fenton (D. C.) <span class="citation" data-id="8817907"><a href="/opinion/8832920/united-states-v-fenton/" aria-description="Citation for case: United States v. Fenton">268 Fed. 221</a></span>; United States v. Bateman (D. C.) <span class="citation" data-id="8824033"><a href="/opinion/8838926/united-states-v-bateman/" aria-description="Citation for case: United States v. Bateman">278 Fed. 231</a></span>; United States v. Rembert (D. C.) <span class="citation" data-id="8827993"><a href="/opinion/8842783/united-states-v-rembert/" aria-description="Citation for case: United States v. Rembert">284 Fed. 996</a></span>. We leave in abeyance the general question of the right of an officer to search an automobile whenever and where-<page-number citation-index="1" label="632">*632</page-number>ever he sees fit, to the end that he may obtain evidence and ascertain whether the car and liquor contained in it had been forfeited.</p>
<p id="b654-4">The case before us is this: Federal prohibition officers, having definite information that professional criminals were conveying in a motor car a quantity of whisky along a certain road about a certain time, were on the watch to intercept it. They stopped the defendants’ truck, opened it, and found, instead of whisky; Chinamen in the course of unlawful transportation. Assuming that this was a search of the truck, under these circumstances we hold that the search was not unreasonable, and that the evidence obtained was competent.</p>
<p id="b654-5">We are of opinion that only two conspiracies were proved. One was to transport and conceal the 2 Chinamen, Poy Jong and Fi Fong, alias Fi Fing, brought from Cuba. There was no proof of a separate conspiracy, except as to the other 16 Chinamen. On the contrary, precisely the same proof of conspiracy was adduced as to all the other 16 in the course of transportation. Gavieres v. United States, <span class="citation" data-id="97395"><a href="/opinion/97395/gavieres-v-united-states/" aria-description="Citation for case: Gavieres v. United States">220 U. S. 338</a></span>, 31 Sup. Ct. 421, <span class="citation" data-id="97395"><a href="/opinion/97395/gavieres-v-united-states/" aria-description="Citation for case: Gavieres v. United States">55 L. Ed. 489</a></span>. It follows that the sentence should have been imposed for conviction on two counts, instead of three counts, of the indictment. The sentence, must therefore be reduced to two terms of two years each under each of two counts of the indictment.</p>
<p id="b654-6">Sentence modified.</p>
<p id="b654-7">ROSE, Circuit Judge, concurs in result.</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Mincey v. Arizona.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Mincey v. Arizona"
type: case
citation: "437 U.S. 385 (1978)"
parallel_cite: "98 S. Ct. 2408; 57 L. Ed. 2d 290"
neutral_cite: 1978 U.S. LEXIS 115
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1978
date_decided: 1978-06-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1978-06-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Mincey v. Arizona
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109905/mincey-v-arizona/"
  cluster_id: 109905
  opinion_id: 109905
  identity_checked: true
homes:
  - page: "[[Emergency Aid]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brigham City v. Stuart]]", "[[Michigan v. Fisher]]", "[[Caniglia v. Strom]]"]
aliases: []
tags: ["case", "fourth-amendment", "emergency-aid", "exigent-circumstances", "warrantless-search", "home"]
holding: "No 'murder scene' exception: the seriousness of the offense does not by itself create exigency. BUT police may make warrantless entries…"
lake:
  record_id: Mincey v. Arizona
  status: verified
  projected_at: 2026-07-09
---

# Mincey v. Arizona

*437 U.S. 385 (1978)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
During an undercover narcotics buy, an officer was shot and killed inside Mincey's apartment, and Mincey was wounded. After the shooting, homicide detectives conducted an exhaustive four-day warrantless search of the apartment, opening drawers and gathering hundreds of items. Arizona defended the search under a "murder scene" exception to the warrant requirement.

## Issue
Whether there is a "murder scene" exception permitting a warrantless search of the scene of a homicide, and what warrantless activity the Fourth Amendment does permit in emergencies.

## Rule
There is no murder-scene exception, and the seriousness of the offense does not by itself create [[Exigent Circumstances and Hot Pursuit|exigent circumstances]]. The Fourth Amendment does, however, permit warrantless action to render aid: "the Fourth Amendment does not bar police officers from making warrantless entries and searches when they reasonably believe that a person within is in need of immediate aid." — 437 U.S. at 392. ^pin-392

And "the police may seize any evidence that is in plain view during the course of their legitimate emergency activities." — [*Id.* at 393](https://www.courtlistener.com/opinion/109905/mincey-v-arizona/#:~:text=the%20police%20may%20seize%20any). ^pin-393

But any such warrantless search must be strictly circumscribed by the emergency that justifies it.

## Application
The shooting victims were promptly attended to, so the extended four-day search of Mincey's apartment was not justified by any ongoing emergency, and the seriousness of the homicide did not by itself supply [[Exigent Circumstances and Hot Pursuit|exigent circumstances]]. Because the search far exceeded anything a genuine emergency could justify and was conducted without a warrant, it violated the Fourth Amendment.

## Conclusion
Reversed in relevant part; the warrantless four-day "murder scene" search was unconstitutional.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The emergency-aid principle recognized in *Mincey* was later restated and applied as an objective inquiry in [[Brigham City v. Stuart]] and [[Michigan v. Fisher]].

## Appears on
- [[Emergency Aid]] — *Key — Progeny / Refinement*

## Sources
- *Mincey v. Arizona*, 437 U.S. 385 (1978) — https://www.courtlistener.com/opinion/109905/mincey-v-arizona/ — pinpoints: 392, 393.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c460ecd12fdcb4f1", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Mincey v. Arizona"}, "payload": {"all": [{"cite": "437 U.S. 385", "page": "385", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "437"}, {"cite": "98 S. Ct. 2408", "page": "2408", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "98"}, {"cite": "57 L. Ed. 2d 290", "page": "290", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "57"}, {"cite": "1978 U.S. LEXIS 115", "page": "115", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1978"}], "display": "437 U.S. 385", "official": {"cite": "437 U.S. 385", "page": "385", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "437"}, "official_selection_present": true, "record_id": "Mincey v. Arizona"}}
{"assertion_id": "0f4fa74acd1f7810", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-393", "record_id": "Mincey v. Arizona"}, "payload": {"fragment": "#:~:text=the%20police%20may%20seize%20any", "page": null, "pin_id": "pin-393", "pinpoint_status": "star-verified", "quote": "the police may seize any evidence that is in plain view during the course of their legitimate emergency activities.", "quote_fidelity": "matched", "record_id": "Mincey v. Arizona", "star_marker": "393"}}
{"assertion_id": "817ed0ece8759726", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-392", "record_id": "Mincey v. Arizona"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-392", "pinpoint_status": "slip-only", "quote": "exception permitting a warrantless search of the scene of a homicide, and what warrantless activity the Fourth Amendment does permit in emergencies. ## Rule There is no murder-scene exception, and the seriousness of the offense does not by itself create exigent circumstances. The Fourth Amendment does, however, permit warrantless action to render aid:", "quote_fidelity": "mismatch", "record_id": "Mincey v. Arizona", "star_marker": null}}
{"assertion_id": "afa9df3e4ee05106", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Mincey v. Arizona"}, "payload": {"as_of_content": "1978-06-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Mincey v. Arizona", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Mincey v. Arizona

```json
{
  "schema_version": "s2.v1",
  "record_id": "Mincey v. Arizona",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Mincey v. Arizona",
    "case_name_short": "Mincey",
    "case_name_full": "Mincey v. Arizona",
    "input_case_name": "Mincey v. Arizona",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1978-06-21",
    "year": 1978,
    "docket": null,
    "cluster_id": 109905,
    "lead_opinion_id": 109905,
    "sibling_ids": [
      109905,
      9427279,
      9427280,
      9427281
    ],
    "absolute_url": "/opinion/109905/mincey-v-arizona/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "437 U.S. 385",
      "volume": "437",
      "reporter": "U.S.",
      "page": "385",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "98 S. Ct. 2408",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "2408",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 L. Ed. 2d 290",
        "volume": "57",
        "reporter": "L. Ed. 2d",
        "page": "290",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1978 U.S. LEXIS 115",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "115",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "437 U.S. 385",
        "volume": "437",
        "reporter": "U.S.",
        "page": "385",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 S. Ct. 2408",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "2408",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 L. Ed. 2d 290",
        "volume": "57",
        "reporter": "L. Ed. 2d",
        "page": "290",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1978 U.S. LEXIS 115",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "115",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "437 U.S. 385",
    "official_selection": {
      "court_class": "scotus",
      "selected": "437 U.S. 385",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-392",
      "page": null,
      "quote": "exception permitting a warrantless search of the scene of a homicide, and what warrantless activity the Fourth Amendment does permit in emergencies. ## Rule There is no murder-scene exception, and the seriousness of the offense does not by itself create exigent circumstances. The Fourth Amendment does, however, permit warrantless action to render aid:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-393",
      "page": null,
      "quote": "the police may seize any evidence that is in plain view during the course of their legitimate emergency activities.",
      "star_marker": "393",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 14053,
      "fragment": "#:~:text=the%20police%20may%20seize%20any",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1978-06-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Mincey v. Arizona",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Wright",
          "cluster_id": 10658752,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mincey v. Arizona:lane1_negative"
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
        "journal_ref": "Mincey v. Arizona:lane1_negative"
      },
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
        "journal_ref": "Mincey v. Arizona:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 4600764,
          "cite": [
            "119 N.E.3d 257",
            "481 Mass. 604"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mincey v. Arizona:lane1_negative"
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
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Delaware v. Prouse",
          "cluster_id": 110045,
          "cite": [
            "59 L. Ed. 2d 660",
            "99 S. Ct. 1391",
            "440 U.S. 648",
            "1979 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
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
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ross",
          "cluster_id": 110719,
          "cite": [
            "72 L. Ed. 2d 572",
            "102 S. Ct. 2157",
            "456 U.S. 798",
            "1982 U.S. LEXIS 18",
            "50 U.S.L.W. 4580"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
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
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Belton",
          "cluster_id": 110559,
          "cite": [
            "69 L. Ed. 2d 768",
            "101 S. Ct. 2860",
            "453 U.S. 454",
            "1981 U.S. LEXIS 13"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Brown",
          "cluster_id": 110901,
          "cite": [
            "75 L. Ed. 2d 502",
            "103 S. Ct. 1535",
            "460 U.S. 730",
            "1983 U.S. LEXIS 143",
            "51 U.S.L.W. 4361"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Horton v. California",
          "cluster_id": 112448,
          "cite": [
            "110 L. Ed. 2d 112",
            "110 S. Ct. 2301",
            "496 U.S. 128",
            "1990 U.S. LEXIS 2937"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Gant",
          "cluster_id": 145887,
          "cite": [
            "173 L. Ed. 2d 485",
            "129 S. Ct. 1710",
            "556 U.S. 332",
            "2009 U.S. LEXIS 3120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Dickerson",
          "cluster_id": 112873,
          "cite": [
            "124 L. Ed. 2d 334",
            "113 S. Ct. 2130",
            "508 U.S. 366",
            "1993 U.S. LEXIS 4018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
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
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
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
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New Jersey v. T. L. O.",
          "cluster_id": 111301,
          "cite": [
            "83 L. Ed. 2d 720",
            "105 S. Ct. 733",
            "469 U.S. 325",
            "1985 U.S. LEXIS 41",
            "53 U.S.L.W. 4083"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brigham City v. Stuart",
          "cluster_id": 145654,
          "cite": [
            "164 L. Ed. 2d 650",
            "126 S. Ct. 1943",
            "547 U.S. 398",
            "2006 U.S. LEXIS 4155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
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
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miller v. Fenton",
          "cluster_id": 111542,
          "cite": [
            "88 L. Ed. 2d 405",
            "106 S. Ct. 445",
            "474 U.S. 104",
            "1985 U.S. LEXIS 144",
            "54 U.S.L.W. 4022"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Segura v. United States",
          "cluster_id": 111259,
          "cite": [
            "82 L. Ed. 2d 599",
            "104 S. Ct. 3380",
            "468 U.S. 796",
            "1984 U.S. LEXIS 150",
            "52 U.S.L.W. 5128"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
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
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Hicks",
          "cluster_id": 111834,
          "cite": [
            "94 L. Ed. 2d 347",
            "107 S. Ct. 1149",
            "480 U.S. 321",
            "1987 U.S. LEXIS 1056",
            "55 U.S.L.W. 4258"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arkansas v. Sanders",
          "cluster_id": 110119,
          "cite": [
            "61 L. Ed. 2d 235",
            "99 S. Ct. 2586",
            "442 U.S. 753",
            "1979 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
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
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kentucky v. King",
          "cluster_id": 216733,
          "cite": [
            "179 L. Ed. 2d 865",
            "131 S. Ct. 1849",
            "563 U.S. 452",
            "2011 U.S. LEXIS 3541"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
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
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Riley v. Cal. United States",
          "cluster_id": 2680439,
          "cite": [
            "189 L. Ed. 2d 430",
            "134 S. Ct. 2473",
            "2014 U.S. LEXIS 4497",
            "82 U.S.L.W. 4558"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
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
        "journal_ref": "Mincey v. Arizona:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109905 OR 9427279 OR 9427280 OR 9427281) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTMyNDc2ODAwMDAwJnM9NDUyMTQ5NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109905+OR+9427279+OR+9427280+OR+9427281%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 4,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      },
      "lane2_top_cited": {
        "query": "cites:(109905 OR 9427279 OR 9427280 OR 9427281)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NTYmcz0xMTI4NDcmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109905+OR+9427279+OR+9427280+OR+9427281%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109905 OR 9427279 OR 9427280 OR 9427281)",
        "reviewed": 68,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 68,
        "triage_read": 1,
        "triage_snippet_classified": 67
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109905 OR 9427279 OR 9427280 OR 9427281)",
    "indexed_citing_opinions": 2353,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109905,
        "count": 2048,
        "count_source": "search"
      },
      {
        "opinion_id": 9427279,
        "count": 356,
        "count_source": "search"
      },
      {
        "opinion_id": 9427280,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427281,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3851,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mincey-v-arizona.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwOTQ0ODQmcz0xMDI5MDE3OCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109905+OR+9427279+OR+9427280+OR+9427281%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109905,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 104997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 106544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 106881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 107340,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 107419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 107526,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 107650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 107893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 108995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 260805,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 263973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 294877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 306714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 312200,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 341541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 349349,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 1128787,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 1129017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 1182305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 1185352,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 1186434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 1504707,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 1827954,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 1874080,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 1996376,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 2050147,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 2269993,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109905,
        "cited_id": 2387463,
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
    "date_created": "2026-07-05T13:51:31Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:51:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:51:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:53:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:51:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Mincey v. Arizona

```
<div>
<center><b><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U.S. 385</a></span> (1978)</b></center>
<center><h1>MINCEY<br>
v.<br>
ARIZONA.</h1></center>
<center>No. 77-5353.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 21, 1978.</center>
<center>Decided June 21, 1978.</center>
CERTIORARI TO THE SUPREME COURT OF ARIZONA.
<p><span class="star-pagination">*387</span> <i>Richard Oseran</i> argued the cause for petitioner. With him on the brief was <i>Frederick S. Klein.</i></p>
<p><i>Galen H. Wilkes,</i> Assistant Attorney General of Arizona, argued the cause for respondent. With him on the brief were <i>Bruce E. Babbitt,</i> Attorney General, <i>Philip G. Urry,</i> Assistant Attorney General, and <i>William J. Schafer III.</i></p>
<p>MR. JUSTICE STEWART delivered the opinion of the Court.</p>
<p>On the afternoon of October 28, 1974, undercover police officer Barry Headricks of the Metropolitan Area Narcotics Squad knocked on the door of an apartment in Tucson, Ariz., occupied by the petitioner, Rufus Mincey. Earlier in the day, Officer Headricks had allegedly arranged to purchase a quantity of heroin from Mincey and had left, ostensibly to obtain money. On his return he was accompanied by nine other plainclothes policemen and a deputy county attorney. The door was opened by John Hodgman, one of three acquaintances of Mincey who were in the living room of the apartment. Officer Headricks slipped inside and moved quickly into the bedroom. Hodgman attempted to slam the door in order to keep the other officers from entering, but was pushed back against the wall. As the police entered the apartment, a rapid volley of shots was heard from the bedroom. Officer Headricks emerged and collapsed on the floor. When other officers entered the bedroom they found Mincey lying on the floor, wounded and semiconscious. Officer Headricks died a few hours later in the hospital.</p>
<p>The petitioner was indicted for murder, assault,<sup>[1]</sup> and three <span class="star-pagination">*388</span> counts of narcotics offenses. He was tried at a single trial and convicted on all the charges. At his trial and on appeal, he contended that evidence used against him had been unlawfully seized from his apartment without a warrant and that statements used to impeach his credibility were inadmissible because they had not been made voluntarily. The Arizona Supreme Court reversed the murder and assault convictions on state-law grounds,<sup>[2]</sup> but affirmed the narcotics convictions. <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/" aria-description="Citation for case: State v. Mincey">115 Ariz. 472</a></span>, <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/" aria-description="Citation for case: State v. Mincey">566 P. 2d 273</a></span>. It held that the warrantless search of a homicide scene is permissible under the Fourth and Fourteenth Amendments and that Mincey's statements were voluntary. We granted certiorari to consider these substantial constitutional question. <span class="citation multiple-matches"><a href="/c/U.%20S./434/902/">434 U. S. 902</a></span>.</p>
<p></p>
<h2>I</h2>
<p>The first question presented is whether the search of Mincey's apartment was constitutionally permissible. After the shooting, the narcotics agents, thinking that other persons in the apartment might have been injured, looked about quickly for other victims. They found a young woman wounded in the bedroom closet and Mincey apparently unconscious in the bedroom, as well as Mincey's three acquaintances (one of whom had been wounded in the head) in the living room. Emergency assistance was requested, and some medical aid was administered to Officer Headricks. But the agents refrained from further investigation, pursuant to a Tucson Police Department directive that police officers should not investigate incidents in which they are involved. They neither searched further nor seized any evidence; they merely guarded the suspects and the premises.</p>
<p>Within 10 minutes, however, homicide detectives who had <span class="star-pagination">*389</span> heard a radio report of the shooting arrived and took charge of the investigation. They supervised the removal of Officer Headricks and the suspects, trying to make sure that the scene was disturbed as little as possible, and then proceeded to gather evidence. Their search lasted four days,<sup>[3]</sup> during which period the entire apartment was searched, photographed, and diagrammed. The officers opened drawers, closets, and cupboards, and inspected their contents; they emptied clothing pockets; they dug bullet fragments out of the walls and floors; they pulled up sections of the carpet and removed them for examination. Every item in the apartment was closely examined and inventoried, and 200 to 300 objects were seized. In short, Mincey's apartment was subjected to an exhaustive and intrusive search. No warrant was ever obtained.</p>
<p>The petitioner's pretrial motion to suppress the fruits of this search was denied after a hearing. Much of the evidence introduced against him at trial (including photographs and diagrams, bullets and shell casings, guns, narcotics, and narcotics paraphernalia) was the product of the four-day search of his apartment. On appeal, the Arizona Supreme Court reaffirmed previous decisions in which it had held that the warrantless search of the scene of a homicide is constitutionally permissible.<sup>[4]</sup> It stated its ruling as follows:</p>
<blockquote>"We hold a reasonable, warrantless search of the scene of a homicideor of a serious personal injury with likelihood of death where there is reason to suspect foul play <span class="star-pagination">*390</span> does not violate the Fourth Amendment to the United States Constitution where the law enforcement officers were legally on the premises in the first instance. . . . For the search to be reasonable, the purpose must be limited to determining the circumstances of death and the scope must not exceed that purpose. The search must also begin within a reasonable period following the time when the officials first learn of the murder (or potential murder)." <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#482" aria-description="Citation for case: State v. Mincey">115 Ariz., at 482</a></span>, <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#283" aria-description="Citation for case: State v. Mincey">566 P. 2d, at 283</a></span>.</blockquote>
<p>Since the investigating homicide detectives knew that Officer Headricks was seriously injured, began the search promptly upon their arrival at the apartment, and searched only for evidence either establishing the circumstances of death or "relevant to motive and intent or knowledge (narcotics, e. g.)." <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#483" aria-description="Citation for case: State v. Mincey"><i>id.,</i> at 483</a></span>, <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#284" aria-description="Citation for case: State v. Mincey">566 P. 2d, at 284</a></span>, the court found that the warrantless search of the petitioner's apartment had not violated the Fourth and Fourteenth Amendments.</p>
<p>We cannot agree. The Fourth Amendment proscribes all unreasonable searches and seizures, and it is a cardinal principle that "searches conducted outside the judicial process, without prior approval by judge or magistrate, are <i>per se</i> unreasonable under the Fourth Amendmentsubject only to a few specifically established and well-delineated exceptions." <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (footnotes omitted); see also <i>South Dakota</i> v. <i>Opperman,</i> <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#381" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 381</a></span> (POWELL, J., concurring); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#481" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 481</a></span>; <i>Vale</i> v. <i>Louisiana,</i> <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#34" aria-description="Citation for case: Vale v. Louisiana">399 U. S. 30, 34</a></span>; <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20</a></span>; <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/#705" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699, 705</a></span>. The Arizona Supreme Court did not hold that the search of the petitioner's apartment fell within any of the exceptions to the warrant requirement previously recognized by this Court, but rather that the search of a homicide scene should be recognized as an additional exception.</p>
<p>Several reasons are advanced by the State to meet its "burden <span class="star-pagination">*391</span>. . . to show the existence of such an exceptional situation" as to justify creating a new exception to the warrant requirement. See <i>Vale</i> v. <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#34" aria-description="Citation for case: Vale v. Louisiana"><i>Louisiana, supra,</i> at 34</a></span>; <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span>. 51. None of these reasons, however, persuades us of the validity of the generic exception delineated by the Arizona Supreme Court.</p>
<p>The first contention is that the search of the petitioner's apartment did not invade any constitutionally protected right of privacy. See <i>Katz</i> v. <i>United States, supra</i><i>.</i> This argument appears to have two prongs. On the one hand, the State urges that by shooting Officer Headricks, Mincey forfeited any reasonable expectation of privacy in his apartment. We have recently rejected a similar waiver argument in <i>Michigan</i> v. <i>Tyler,</i> <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#505" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 505-506</a></span>; it suffices here to say that this reasoning would impressibly convict the suspect even before the evidence against him was gathered.<sup>[5]</sup> On the other hand, the State contends that the police entry to arrest Mincey was so great an invasion of his privacy that the additional intrusion caused by the search was constitutionally irrelevant. But this claim is hardly tenable in light of the extensive nature of this search. It is one thing to say that one who is legally taken into police custody has a lessened right of privacy in his person. See <i>United States</i> v. <i>Edwards,</i> <span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/#808" aria-description="Citation for case: United States v. Edwards">415 U. S. 800, 808-809</a></span>; <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span>. It is quite another to argue that he also has a lessened right of privacy in his entire house. Indeed this very argument was rejected when it was advanced to support the warrantless search of a dwelling where a search occurred as "incident" to the arrest of its occupant. <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>, 766 n. 12. <span class="star-pagination">*392</span> Thus, this search cannot be justified on the ground that no constitutionally protected right of privacy was invaded.</p>
<p>The State's second argument in support of its categorical exception to the warrant requirement is that a possible homicide presents an emergency situation demanding immediate action. We do not question the right of the police to respond to emergency situations. Numerous state<sup>[6]</sup> and federal<sup>[7]</sup> cases have recognized that the Fourth Amendment does not bar police officers from making warrantless entries and searches when they reasonably believe that a person within is in need of immediate aid. Similarly, when the police come upon the scene of a homicide they may make a prompt warrantless search of the area to see if there are other victims or if a killer is still on the premises. Cf. <i>Michigan</i> v. <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#509" aria-description="Citation for case: Michigan v. Tyler"><i>Tyler, supra,</i> at 509-510</a></span>. "The need to protect or preserve life or avoid serious injury is justification for what would be otherwise illegal absent an exigency or emergency." <i>Wayne</i> v. <span class="star-pagination">*393</span> <i>United States,</i> 115 U. S. App. D. C. 234, 241, <span class="citation" data-id="9449370"><a href="/opinion/260805/lewis-l-wayne-v-united-states/#212" aria-description="Citation for case: Lewis L. Wayne v. United States">318 F. 2d 205, 212</a></span> (opinion of Burger, J.). And the police may seize any evidence that is in plain view during the course of their legitimate emergency activities. <i>Michigan</i> v. <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#509" aria-description="Citation for case: Michigan v. Tyler"><i>Tyler, supra,</i> at 509-510</a></span>; <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#465" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 465-466</a></span>.</p>
<p>But a warrantless search must be "strictly circumscribed by the exigencies which justify its initiation," <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#25" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 25-26</a></span>, and it simply cannot be contended that this search was justified by any emergency threatening life or limb. All the persons in Mincey's apartment had been located before the investigating homicide officers arrived there and began their search. And a four-day search that included opening dresser drawers and ripping up carpets can hardly be rationalized in terms of the legitimate concerns that justify an emergency search.</p>
<p>Third, the State points to the vital public interest in the prompt investigation of the extremely serious crime of murder. No one can doubt the importance of this goal. But the public interest in the investigation of other serious crimes is comparable. If the warrantless search of a homicide scene is reasonable, why not the warrantless search of the scene of a rape, a robbery, or a burglary? "No consideration relevant to the Fourth Amendment suggests any point of rational limitation" of such a doctrine. <i>Chimel</i> v. <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#766" aria-description="Citation for case: Chimel v. California"><i>California, supra,</i> at 766</a></span>.</p>
<p>Moreover, the mere fact that law enforcement may be made more efficient can never by itself justify disregard of the Fourth Amendment. Cf. <i>Coolidge</i> v. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#481" aria-description="Citation for case: Coolidge v. New Hampshire"><i>New Hampshire, supra,</i> at 481</a></span>. The investigation of crime would always be simplified if warrants were unnecessary. But the Fourth Amendment reflects the view of those who wrote the Bill of Rights that the privacy of a person's home and property may not be totally sacrificed in the name of maximum simplicity in enforcement of the criminal law. See <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span>. 6-11. For this reason, warrants are <span class="star-pagination">*394</span> generally required to search a person's home or his person unless "the exigencies of the situation" make the needs of law enforcement so compelling that the warrantless search is objectively reasonable under the Fourth Amendment. <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#456" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 456</a></span>; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14-15</a></span>. See, <i>e. g., </i><i>Chimel</i> v. <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">California, supra</a></span></i> (search of arrested suspect and area within his control for weapons or evidence); <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 298-300</a></span> ("hot pursuit" of fleeing suspect); <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 770-771</a></span> (imminent destruction of evidence); see also <i>supra,</i> at 392-393.</p>
<p>Except for the fact that the offense under investigation was a homicide, there were no exigent circumstances in this case, as, indeed, the Arizona Supreme Court recognized. <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#482" aria-description="Citation for case: State v. Mincey">115 Ariz., at 482</a></span>, <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#283" aria-description="Citation for case: State v. Mincey">566 P. 2d, at 283</a></span>. There was no indication that evidence would be lost, destroyed, or removed during the time required to obtain a search warrant. Indeed, the police guard at the apartment minimized that possibility. And there is no suggestion that a search warrant could not easily and conveniently have been obtained. We decline to hold that the seriousness of the offense under investigation itself creates exigent circumstances of the kind that under the Fourth Amendment justify a warrantless search.</p>
<p>Finally, the State argues that the "murder scene exception" is constitutionally permissible because it is narrowly confined by the guidelines set forth in the decision of the Arizona Supreme Court, see <i>supra,</i> at 389-390.<sup>[8]</sup> In light of the extensive search that took place in this case it may be questioned what protection the guidelines afford a person in whose home a homicide or assault occurs. Indeed, these so-called guidelines <span class="star-pagination">*395</span> are hardly so rigidly confining as the State seems to assert. They confer unbridled discretion upon the individual officer to interpret such terms as "reasonable . . . search," "serious personal injury with likelihood of death where there is reason to suspect foul play," and "reasonable period." It is precisely this kind of judgmental assessment of the reasonableness and scope of a proposed search that the Fourth Amendment requires be made by a neutral and objective magistrate, not a police officer. See, <i>e. g., </i><i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#316" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 316</a></span>; <i>Coolidge</i> v. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#449" aria-description="Citation for case: Coolidge v. New Hampshire"><i>New Hampshire, supra,</i> at 449-453</a></span>; <i>Mancusi</i> v. <i>DeForte,</i> <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#371" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364, 371</a></span>; <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#481" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 481-482</a></span>.</p>
<p>It may well be that the circumstances described by the Arizona Supreme Court would usually be constitutionally sufficient to warrant a search of substantial scope. But the Fourth Amendment requires that this judgment in each case be made in the first instance by a neutral magistrate.</p>
<blockquote>"The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime." <i>Johnson</i> v. <i>United States, supra,</i> at 13-14.</blockquote>
<p>In sum, we hold that the "murder scene exception" created by the Arizona Supreme Court is inconsistent with the Fourth and Fourteenth Amendmentsthat the warrantless search of Mincey's apartment was not constitutionally permissible simply because a homicide had recently occurred there."<sup>[9]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*396</span> II</h2>
<p>Since there will presumably be a new trial in this case,<sup>[10]</sup> it is appropriate to consider also the petitioner's contention that statements he made from a hospital bed were involuntary, and therefore could not constitutionally be used against him at his trial.</p>
<p>Mincey was brought to the hospital after the shooting and taken immediately to the emergency room where he was examined and treated. He had sustained a wound in his hip, resulting in damage to the sciatic nerve and partial paralysis of his right leg. Tubes were inserted into his throat to help him breathe, and through his nose into his stomach to keep him from vomiting; a catheter was inserted into his bladder. He received various drugs, and a device was attached to his arm so that he could be fed intravenously. He was then taken to the intensive care unit.</p>
<p>At about eight o'clock that evening, Detective Hust of the Tucson Police Department came to the intensive care unit to interrogate him. Mincey was unable to talk because of the tube in his mouth, and so he responded to Detective Hust's questions by writing answers on pieces of paper provided by the hospital.<sup>[11]</sup> Hust told Mincey he was under arrest for the murder of a police officer, gave him the warnings required by <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, and began to ask questions about the events that had taken place in Mincey's apartment a few hours earlier. Although Mincey asked repeatedly that the interrogation stop until he could get a lawyer, Hust continued to question him until almost midnight.</p>
<p><span class="star-pagination">*397</span> After a pretrial hearing, see <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">378 U. S. 368</a></span>, the trial court found that Mincey had responded to this interrogation voluntarily.<sup>[12]</sup> When Mincey took the witness stand at his trial his statements in response to Detective Hust's questions were used in an effort to impeach his testimony in several respects.<sup>[13]</sup> On appeal, the Arizona Supreme Court indicated its belief that because Detective Hust had failed to honor Mincey's request for a lawyer, the statements would have been inadmissible as part of the prosecution's case in chief. <i>Miranda</i> v. <i>Arizona, supra</i><i>.</i> But, relying on <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span>, and <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714</a></span>, it held that since the trial court's finding of voluntariness was not "clear[ly] and manifest[ly]" erroneous the statements were properly used for purposes of impeachment. <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#480" aria-description="Citation for case: State v. Mincey">115 Ariz., at 480</a></span>, <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#281" aria-description="Citation for case: State v. Mincey">566 P. 2d, at 281</a></span>.</p>
<p>Statements made by a defendant in circumstances violating the strictures of <i>Miranda</i> v. <i>Arizona, supra</i><i>,</i> are admissible for <span class="star-pagination">*398</span> impeachment if their "trustworthiness . . . satisfies legal standards." <i>Harris</i> v. <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#224" aria-description="Citation for case: Harris v. New York"><i>New York, supra,</i> at 224</a></span>; <i>Oregon</i> v. <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#722" aria-description="Citation for case: Oregon v. Hass"><i>Hass, supra,</i> at 722</a></span>. But <i>any</i> criminal trial use against a defendant of his <i>involuntary</i> statement is a denial of due process of law "even though there is ample evidence aside from the confession to support the conviction." <i>Jackson</i> v. <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#376" aria-description="Citation for case: Jackson v. Denno"><i>Denno, supra,</i> at 376</a></span>; <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#518" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503, 518</a></span>; <i>Lynumn</i> v. <i>Illinois,</i> <span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/#537" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528, 537</a></span>; <i>Stroble</i> v. <i>California,</i> <span class="citation" data-id="9420722"><a href="/opinion/104997/stroble-v-california/#190" aria-description="Citation for case: Stroble v. California">343 U. S. 181, 190</a></span>; see <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span>, 23 and n. 8. If, therefore, Mincey's statements to Detective Hust were not "`the product of a rational intellect and a free will,'" <i>Townsend</i> v. <i>Sain,</i> <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/#307" aria-description="Citation for case: Townsend v. Sain">372 U. S. 293, 307</a></span>, quoting <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#208" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 208</a></span>, his conviction cannot stand. In making this critical determination, we are not bound by the Arizona Supreme Court's holding that the statements were voluntary. Instead, this Court is under a duty to make an independent evaluation of the record. <i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#741" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737, 741-742</a></span>; <i>Haynes</i> v. <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#515" aria-description="Citation for case: Haynes v. Washington"><i>Washington, supra,</i> at 515-516</a></span>.</p>
<p>It is hard to imagine a situation less conducive to the exercise of "a rational intellect and a free will" than Mincey's. He had been seriously wounded just a few hours earlier, and had arrived at the hospital "depressed almost to the point of coma," according to his attending physician. Although he had received some treatment, his condition at the time of Hust's interrogation was still sufficiently serious that he was in the intensive care unit.<sup>[14]</sup> He complained to Hust that the pain in his leg was "unbearable." He was evidently confused and unable to think clearly about either the events of that afternoon or the circumstances of his interrogation, since some <span class="star-pagination">*399</span> of his written answers were on their face not entirely coherent.<sup>[15]</sup> Finally, while Mincey was being questioned he was lying on his back on a hospital bed, encumbered by tubes, needles, and breathing apparatus. He was, in short, "at the complete mercy" of Detective Hust, unable to escape or resist the thrust of Hust's interrogation. Cf. <i>Beecher</i> v. <i>Alabama,</i> <span class="citation" data-id="9423505"><a href="/opinion/107526/beecher-v-alabama/#38" aria-description="Citation for case: Beecher v. Alabama">389 U. S. 35, 38</a></span>.</p>
<p>In this debilitated and helpless condition, Mincey clearly expressed his wish not to be interrogated. As soon as Hust's questions turned to the details of the afternoon's events, Mincey wrote: "This is all I can say without a lawyer." Hust nonetheless continued to question him, and a nurse who was present suggested it would be best if Mincey answered. Mincey gave unresponsive or uninformative answers to several more questions, and then said again that he did not want to talk without a lawyer. Hust ignored that request and another made immediately thereafter.<sup>[16]</sup> Indeed, throughout the interrogation <span class="star-pagination">*400</span> Mincey vainly asked Hust to desist. Moreover, he complained several times that he was confused or unable to think clearly, or that he could answer more accurately <span class="star-pagination">*401</span> the next day.<sup>[17]</sup> But despite Mincey's entreaties to be let alone, Hust ceased the interrogation only during intervals when Mincey lost consciousness or received medical treatment, and after each such interruption returned relentlessly to his task. The statements at issue were thus the result of virtually continuous questioning of a seriously and painfully wounded man on the edge of consciousness.</p>
<p>There were not present in this case some of the gross abuses that have led the Court in other cases to find confessions involuntary, such as beatings, see <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span>, or "truth serums," see <i>Townsend</i> v. <i>Sain,</i> <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">372 U. S. 293</a></span>. But "the blood of the accused is not the only hallmark of an unconstitutional inquisition." <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama">361 U. S., at 206</a></span>. Determination of whether a statement is involuntary "requires more than a mere color-matching of cases." <i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/#442" aria-description="Citation for case: Reck v. Pate">367 U. S. 433, 442</a></span>. It requires careful evaluation of all the circumstances of the interrogation.<sup>[18]</sup></p>
<p>It is apparent from the record in this case that Mincey's statements were not "the product of his free and rational choice." <i>Greenwald</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9423651"><a href="/opinion/107650/greenwald-v-wisconsin/#521" aria-description="Citation for case: Greenwald v. Wisconsin">390 U. S. 519, 521</a></span>. To the contrary, the undisputed evidence makes clear that Mincey wanted <i>not</i> to answer Detective Hust. But Mincey was weakened by pain and shock, isolated from family, friends, and legal counsel, and barely conscious, and his will was simply <span class="star-pagination">*402</span> overborne. Due process of law requires that statements obtained as these were cannot be used in any way against a defendant at his trial.</p>
<p></p>
<h2>III</h2>
<p>For the foregoing reasons, the judgment of the Arizona Supreme Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE BRENNAN joins, concurring.</p>
<p>I join the opinion of the Court, which holds that petitioner's rights under the Fourth and Fourteenth Amendments have been violated. I write today to emphasize a point that is illustrated by the instant case, but that applies more generally to all cases in which we are asked to review Fourth Amendment issues arising out of state criminal convictions.</p>
<p>It is far from clear that we would have granted certiorari solely to resolve the involuntary-statement issue in this case, for that could have been resolved on federal habeas corpus. With regard to the Fourth Amendment issue, however, we had little choice but to grant review, because our decision in <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U. S. 465</a></span> (1976), precludes federal habeas consideration of such issues. In <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span></i> the Court held that, "where the State has provided an opportunity for full and fair litigation of a Fourth Amendment claim, a state prisoner may not be granted federal habeas corpus relief on the ground that evidence obtained in an unconstitutional search or seizure was introduced at his trial." <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#494" aria-description="Citation for case: Stone v. Powell"><i>Id.,</i> at 494</a></span> (footnotes omitted). Because of this holding, petitioner would not have been able to present to a federal habeas court the Fourth Amendment claim that the Court today unanimously upholds.</p>
<p>The additional responsibilities placed on this Court in the wake of <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span></i> become apparent upon examination of decisions <span class="star-pagination">*403</span> of the Arizona Supreme Court on the Fourth Amendment issue presented here. The Arizona court created its "murder scene exception" in a 1971 case. <i>State</i> v. <i>Sample,</i> <span class="citation" data-id="1185352"><a href="/opinion/1185352/state-v-sample/#409" aria-description="Citation for case: State v. Sample">107 Ariz. 407, 409-410</a></span>, <span class="citation" data-id="1185352"><a href="/opinion/1185352/state-v-sample/#46" aria-description="Citation for case: State v. Sample">489 P. 2d 44, 46-47</a></span>. A year later, when the defendant in that case sought federal habeas corpus relief, the United States Court of Appeals for the Ninth Circuit ruled, as we do today, that the exception could not be upheld under the Fourth Amendment. <i>Sample</i> v. <i>Eyman,</i> <span class="citation" data-id="9458899"><a href="/opinion/306714/lynn-sample-v-frank-a-eyman/#821" aria-description="Citation for case: Lynn Sample v. Frank A. Eyman">469 F. 2d 819, 821-822</a></span> (1972). When the Arizona Supreme Court next gave plenary consideration to the issue, prior to our decision in <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span>,</i> it apparently felt bound by the Ninth Circuit's <i>Sample</i> decision, although it found the case before it to be distinguishable. <i>State</i> v. <i>Duke,</i> <span class="citation" data-id="1129017"><a href="/opinion/1129017/state-v-duke/#324" aria-description="Citation for case: State v. Duke">110 Ariz. 320, 324</a></span>, <span class="citation" data-id="1129017"><a href="/opinion/1129017/state-v-duke/#574" aria-description="Citation for case: State v. Duke">518 P. 2d 570, 574</a></span> (1974).<sup>[1]</sup></p>
<p>When the Arizona Supreme Court rendered its decision in the instant case, however, it took a different approach. The decision, issued nearly a year after <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span>,</i> merely noted that the Ninth Circuit had "disagreed" with the Arizona court's view of the validity of the murder-scene exception. <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/" aria-description="Citation for case: State v. Mincey">115 Ariz. 472</a></span>, 482 n. 4, <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/" aria-description="Citation for case: State v. Mincey">566 P. 2d 273</a></span>, 283 n. 4 (1977). It thus created an effective "conflict" for us to resolve. Cf. this Court's Rule 19 (1) (b). If certiorari had not been granted, we would have left standing a decision of the State's highest court on a question of federal constitutional law that had been resolved in a directly opposing way by the highest federal court having <span class="star-pagination">*404</span> special responsibility for the State. Regardless of which court's view of the Constitution was the correct one, such nonuniformity on Fourth Amendment questions is obviously undesirable; it is as unfair to state prosecutors and judges who must make difficult determinations regarding what evidence is subject to exclusionas it is to state criminal defendants.</p>
<p>Prior to <i>Stone</i> v. <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Powell</a></span></i><i>,</i> there would have been no need to grant certiorari in a case such as this, since the federal habeas remedy would have been available to the defendant. Indeed, prior to <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span></i> petitioner here probably would not even have had to utilize federal habeas, since the Arizona courts were at that earlier time more inclined to follow the federal constitutional pronouncements of the Ninth Circuit, as discussed above. But <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span></i> eliminated the habeas remedy with regard to Fourth Amendment violations, thus allowing state-court rulings to diverge from lower federal-court rulings on these issues and placing a correspondingly greater burden on this Court to ensure uniform federal law in the Fourth Amendment area.</p>
<p>At the time of <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span></i> my Brother BRENNAN wrote that "institutional constraints totally preclude any possibility that this Court can adequately oversee whether state courts have properly applied federal law." 428 U. S., at 526 (dissenting opinion); see <i>id.,</i> at 534. Because of these constraints, we will often be faced with a Hobson's choice in cases of less than national significance that could formerly have been left to the lower federal courts: either to deny certiorari and thereby let stand divergent state and federal decisions with regard to Fourth Amendment rights; or to grant certiorari and thereby add to our calendar, which many believe is already overcrowded, cases that might better have been resolved elsewhere. In view of this problem and others,<sup>[2]</sup> I hope that the <span class="star-pagination">*405</span> Court will at some point reconsider the wisdom of <i>Stone</i> v. <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Powell</a></span></i><i>.</i><sup>[3]</sup></p>
<p>MR. JUSTICE REHNQUIST, concurring in part and dissenting in part.</p>
<p>Petitioner was indicted for murder, assault, and three counts of narcotics offenses. He was convicted on all charges. On appeal, the Supreme Court of Arizona reversed all but the narcotics convictions. <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/" aria-description="Citation for case: State v. Mincey">115 Ariz. 472</a></span>, <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/" aria-description="Citation for case: State v. Mincey">566 P. 2d 273</a></span> (1977). In his petition for certiorari, petitioner challenged the introduction of evidence material to his narcotics convictions that was seized during a lengthy warrantless search of his apartment. Petitioner also challenged on voluntariness grounds the introduction of various statements made to the police relating to the murder charge. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./434/902/">434 U. S. 902</a></span>, and the Court today reverses the Supreme Court of Arizona on both issues. While I agree with the Court that the warrantless search was not justifiable on the grounds advanced by the Arizona Supreme Court, I dissent from the Court's holding that Mincey's statements were involuntary and thus inadmissible.</p>
<p></p>
<h2>I</h2>
<p>I join Part I of the Court's opinion. As the Supreme Court of Arizona recognized, the four-day warrantless search of petitioner's apartment did not, on the facts developed at trial, "fit within [any] usual `exigent circumstances' exception." <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#482" aria-description="Citation for case: State v. Mincey">115 Ariz., at 482</a></span>, <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#283" aria-description="Citation for case: State v. Mincey">566 P. 2d, at 283</a></span>. Instead, the State of <span class="star-pagination">*406</span> Arizona asks us to adopt a separate "murder scene" exception to the warrant requirement and the Court, for the reasons stated in its opinion, correctly rejects this invitation.</p>
<p>I write separately on this issue only to emphasize that the question of what, if any, evidence <i>was</i> seized under established Fourth Amendment standards is left open for the Arizona courts to resolve on remand. <i>Ante,</i> at 395 n. 9. Much of the evidence introduced by the State at trial was apparently removed from the apartment the same day as the shooting. App. 40. And the State's brief suggests that some evidence for example, blood on the floorrequired immediate examination. Brief for Respondent 70-71. The question of what evidence would have been "lost, destroyed, or removed" if a warrant had been obtained, <i>ante,</i> at 394, otherwise required an immediate search, or was in plain view should be considered on remand by the Arizona courts.</p>
<p>In considering whether exigencies required the search for or seizure of particular evidence, the previous events within the apartment cannot be ignored. I agree with the Court that the police's entry to arrest Mincey, followed by the shooting and the search for victims, did not justify the later four-day search of the apartment. <i>Ante,</i> at 391-392. But the constitutionality of a particular search is a question of reasonableness and depends on "a balance between the public interest and the individual's right to personal security free from arbitrary interference by law officers." <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975). See <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19</a></span> (1968). In <i>Pennsylvania</i> v. <i>Mimms,</i> <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106</a></span> (1977), we held that once a motor vehicle had been lawfully detained for a traffic violation, police officers could constitutionally order the driver out of the vehicle. In so holding, we emphasized that the challenged intrusion was "occasioned not by the initial stop of the vehicle, which was admittedly justified, but by the order to get out of the car. We think this additional intrusion can only be described as <i>de minimis.</i>" <span class="star-pagination">*407</span> <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#111" aria-description="Citation for case: Pennsylvania v. Mimms"><i>Id.,</i> at 111</a></span>. Similarly, in the instant case, the prior intrusions occasioned by the shooting and the police's response thereto may legitimize a search under some exigencies that in tamer circumstances might not permit a search.</p>
<p></p>
<h2>II</h2>
<p>The Court in Part II of its opinion advises the Arizona courts on the admissibility of certain statements made by Mincey that are relevant only to the murder charge. Because Mincey's murder conviction was reversed by the Arizona Supreme Court, and it is not certain that there will be a retrial. I would not reach this issue. Since the Court addresses the issue, however, I must register my disagreement with its conclusion.</p>
<p>Before trial, Mincey moved to suppress as involuntary certain statements that he had made while confined in an intensive care unit some hours after the shooting. As the Court acknowledges, the trial court found "`with unmistakable clarity'" that the statements were voluntary, <i>ante,</i> at 397 n. 12, and the Supreme Court of Arizona unanimously affirmed. <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#479" aria-description="Citation for case: State v. Mincey">115 Ariz., at 479-480</a></span>, <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#280" aria-description="Citation for case: State v. Mincey">566 P. 2d, at 280-281</a></span>. This Court now disagrees and holds that "Mincey's statements were not `the product of his free and rational choice'" and therefore "cannot be used in any way against [him] at his trial." <i>Ante,</i> at 401, 402. Because I believe that the Court both has failed to accord the state-court finding the deference that the Court has always found such findings due and also misapplied our past precedents, I dissent.</p>
<p>As the Court notes, <i>ante,</i> at 398, past cases of this Court hold that a state-court finding as to voluntariness which is "not fairly supported by the record cannot be <i>conclusive</i> of federal rights." <i>Townsend</i> v. <i>Sain,</i> <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/#316" aria-description="Citation for case: Townsend v. Sain">372 U. S. 293, 316</a></span> (1963) (emphasis added). Instead, these cases require the Court to "make an independent determination <i>on the undisputed facts.</i>" <i>Stroble</i> v. <i>California,</i> <span class="citation" data-id="9420722"><a href="/opinion/104997/stroble-v-california/#190" aria-description="Citation for case: Stroble v. California">343 U. S. 181, 190</a></span> (1952) (emphasis added); <span class="star-pagination">*408</span> <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#404" aria-description="Citation for case: Malinski v. New York">324 U. S. 401, 404</a></span> (1945). It is well established that, "for purposes of review in this Court, the determination of the trial judge or of the jury will ordinarily be taken to resolve evidentiary conflicts and may be entitled to some weight even with respect to the ultimate conclusion on the crucial issue of voluntariness." <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#515" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503, 515</a></span> (1963). See <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#238" aria-description="Citation for case: Lisenba v. California">314 U. S. 219, 238</a></span> (1941); <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#205" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 205</a></span>, and n. 5 (1960). Such deference, particularly on the resolution of evidentiary conflicts, "is particularly apposite because the trial judge and jury are closest to the trial scene and thus afforded the best opportunity to evaluate contradictory testimony." <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#516" aria-description="Citation for case: Haynes v. Washington"><i>Haynes, supra,</i> at 516</a></span>.</p>
<p>The Court in this case, however, ignores entirely some evidence of voluntariness and distinguishes away yet other testimony. There can be no discounting that Mincey was seriously wounded and laden down with medical equipment. Mincey was certainly not able to move about and, because of the breathing tube in his mouth, had to answer Detective Hust's questions on paper. But the trial court was certainly not required to find, as the Court would imply, that Mincey was "a seriously and painfully wounded man on the edge of consciousness." <i>Ante,</i> at 401. Nor is it accurate to conclude that Detective Hust "ceased the interrogation only during intervals when Mincey lost consciousness or received medical treatment, and after each such interruption returned relentlessly to his task." <i><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">Ibid.</a></span></i></p>
<p>As the Arizona Supreme Court observed in affirming the trial court's finding of voluntariness, Mincey's nurse</p>
<blockquote>"testified that she had not given [Mincey] any medication and that [he] was alert and able to understand the officer's questions. . . . She said that [Mincey] was in moderate pain but was very cooperative with everyone. The interrogating officer also testified that [Mincey] did not appear to be under the influence of drugs and that <span class="star-pagination">*409</span> [his] answers were generally responsive to the questions." <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#480" aria-description="Citation for case: State v. Mincey">115 Ariz., at 480</a></span>, <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#281" aria-description="Citation for case: State v. Mincey">566 P. 2d, at 281</a></span>.</blockquote>
<p>See App. 50-51 (testimony of Detective Hust), 63 and 66 (testimony of Nurse Graham).<sup>[1]</sup> The uncontradicted testimony of Detective Hust also reveals a questioning that was far from "relentless." While the interviews took place over a three-hour time span, the interviews were not "very long; probably not more than an hour total for everything." <i>Id.,</i> at 59. Hust would leave the room whenever Mincey received medical treatment "or if it looked like he was getting a little bit exhausted." <i>Ibid.</i> According to Detective Hust, Mincey never "los[t] consciousness at any time." <i>Id.,</i> at 58.</p>
<p>As the Court openly concedes, there were in this case none of the "gross abuses that have led the Court in other cases to find confessions involuntary, such as beatings . . . or `truth serums.'" <i>Ante,</i> at 401. Neither is this a case, however, where the defendant's will was "simply overborne" by "mental coercion." Cf. <i>Blackburn</i> v. <i>Alabama, supra,</i> at 206; <i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#741" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737, 741</a></span> (1966); <i>Greenwald</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9423651"><a href="/opinion/107650/greenwald-v-wisconsin/#521" aria-description="Citation for case: Greenwald v. Wisconsin">390 U. S. 519, 521</a></span> (1968). As the Supreme Court of Arizona observed, it was the testimony of both Detective Hust and Nurse Graham "that neither mental or physical force nor abuse was used on [Mincey] . . . . Nor were any promises made." <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#480" aria-description="Citation for case: State v. Mincey">115 Ariz., at 480</a></span>, 566 P. 2d. at 281. See App. 58-59 (testimony of Detective Hust) and 63 (testimony of Nurse Graham). According to Mincey's own testimony, he wanted <span class="star-pagination">*410</span> to help Hust "the best I could" and tried to answer each question "to the best of my recollection at the time that this was going on." <i>Id.,</i> at 86. Mincey did not claim that he felt compelled by Detective Hust to answer the questions propounded.<sup>[2]</sup> Cf. <span class="citation" data-id="9423651"><a href="/opinion/107650/greenwald-v-wisconsin/#521" aria-description="Citation for case: Greenwald v. Wisconsin"><i>Greenwald, supra,</i> at 521</a></span>.</p>
<p>By all of these standards enunciated in our previous cases, I think the Court today goes too far in substituting its own judgment for the judgment of a trial court and the highest court of a State, both of which decided these disputed issues differently than does this Court, and both of which were a good deal closer to the factual occurrences than is this Court. Admittedly we may not abdicate our duty to decide questions of constitutional law under the guise of wholly remitting to state courts the function of fact finding which is a necessary ingredient of the process of constitutional decision. But the authorities previously cited likewise counsel us against going to the other extreme, and attempting to extract from a cold record bits and pieces of evidence which we then treat as the "facts" of the case. I believe that the trial court was entitled to conclude that, notwithstanding Mincey's medical condition, his statements in the intensive care unit were admissible. The fact that the same court might have been equally entitled to reach the opposite conclusion does not justify this Court's adopting the opposite conclusion.</p>
<p>I therefore dissent from Part II of the Court's opinion.</p>
<h2>NOTES</h2>
<p>[1]  The assault charge was based on the wounding of a person in the living room who was hit by a bullet that came through the wall.</p>
<p>[2]  The state appellate court held that the jury had been improperly instructed on criminal intent. It appears from the record in this case that the retrial of the petitioner on the murder and assault charges was stayed by the trial court after certiorari was granted by this Court.</p>
<p>[3]  The police also returned to the apartment in November 1974, at the request of the petitioner's landlord, to remove property of the petitioner that remained in the apartment after his lease had expired on October 31.</p>
<p>[4]  <i>State</i> v. <i>Sample,</i> <span class="citation" data-id="1185352"><a href="/opinion/1185352/state-v-sample/" aria-description="Citation for case: State v. Sample">107 Ariz. 407</a></span>, <span class="citation" data-id="1185352"><a href="/opinion/1185352/state-v-sample/" aria-description="Citation for case: State v. Sample">489 P. 2d 44</a></span>; <i>State ex rel. Berger</i> v. <i>Superior Court,</i> <span class="citation" data-id="1182305"><a href="/opinion/1182305/state-ex-rel-berger-v-superior-ct-cty-of-maricopa/" aria-description="Citation for case: State Ex Rel. Berger v. SUPERIOR CT., CTY. OF MARICOPA">110 Ariz. 281</a></span>, <span class="citation" data-id="1182305"><a href="/opinion/1182305/state-ex-rel-berger-v-superior-ct-cty-of-maricopa/" aria-description="Citation for case: State Ex Rel. Berger v. SUPERIOR CT., CTY. OF MARICOPA">517 P. 2d 1277</a></span>; <i>State</i> v. <i>Duke,</i> <span class="citation" data-id="1129017"><a href="/opinion/1129017/state-v-duke/" aria-description="Citation for case: State v. Duke">110 Ariz. 320</a></span>, <span class="citation" data-id="1129017"><a href="/opinion/1129017/state-v-duke/" aria-description="Citation for case: State v. Duke">518 P. 2d 570</a></span>. The Court of Appeals for the Ninth Circuit reversed the denial of a petition for a writ of habeas corpus filed by the defendant whose conviction was upheld in <i>State</i> v. <i>Sample, supra</i><i>,</i> on the ground, <i>inter alia,</i> that the warrantless search of the homicide scene violated the Fourth and Fourteenth Amendments. <i>Sample</i> v. <i>Eyman,</i> <span class="citation" data-id="9458899"><a href="/opinion/306714/lynn-sample-v-frank-a-eyman/" aria-description="Citation for case: Lynn Sample v. Frank A. Eyman">469 F. 2d 819</a></span>.</p>
<p>[5]  Moreover, this rationale would be inapplicable if a homicide occurred at the home of the victim or of a stranger, yet the Arizona cases indicate that a warrantless search in such a case would also be permissible under the "murder scene exception." Cf. <i>State</i> v. <i>Sample, supra,</i> at 409, <span class="citation" data-id="1185352"><a href="/opinion/1185352/state-v-sample/#46" aria-description="Citation for case: State v. Sample">489 P. 2d, at 46</a></span>.</p>
<p>[6]  <i>E. g., </i><i>People</i> v. <i>Hill,</i> <span class="citation" data-id="1388061"><a href="/opinion/1388061/people-v-hill/#753" aria-description="Citation for case: People v. Hill">12 Cal. 3d 731, 753-757</a></span>, <span class="citation" data-id="1388061"><a href="/opinion/1388061/people-v-hill/#18" aria-description="Citation for case: People v. Hill">528 P. 2d 1, 18-21</a></span>; <i>Patrick</i> v. <i>State,</i> <span class="citation" data-id="2269993"><a href="/opinion/2269993/patrick-v-state/#488" aria-description="Citation for case: Patrick v. State">227 A. 2d 486, 488-490</a></span> (Del.); <i>People</i> v. <i>Brooks,</i> <span class="citation" data-id="2050147"><a href="/opinion/2050147/people-v-brooks/#775" aria-description="Citation for case: People v. Brooks">7 Ill. App. 3d 767, 775-777</a></span>, <span class="citation" data-id="2050147"><a href="/opinion/2050147/people-v-brooks/#212" aria-description="Citation for case: People v. Brooks">289 N. E. 2d 207, 212-214</a></span>; <i>Maxey</i> v. <i>State,</i> <span class="citation" data-id="9707318"><a href="/opinion/1996376/maxey-v-state/#649" aria-description="Citation for case: Maxey v. State">251 Ind. 645, 649-650</a></span>, <span class="citation" data-id="9707318"><a href="/opinion/1996376/maxey-v-state/#653" aria-description="Citation for case: Maxey v. State">244 N. E. 2d 650, 653-654</a></span>; <i>Davis</i> v. <i>State,</i> <span class="citation" data-id="9642688"><a href="/opinion/1504707/davis-v-state/#395" aria-description="Citation for case: Davis v. State">236 Md. 389, 395-397</a></span>, <span class="citation" data-id="9642688"><a href="/opinion/1504707/davis-v-state/#80" aria-description="Citation for case: Davis v. State">204 A. 2d 76, 80-82</a></span>; <i>State</i> v. <i>Hardin,</i> <span class="citation" data-id="1128787"><a href="/opinion/1128787/state-v-hardin/" aria-description="Citation for case: State v. Hardin">90 Nev. 10</a></span>, <span class="citation" data-id="1128787"><a href="/opinion/1128787/state-v-hardin/" aria-description="Citation for case: State v. Hardin">518 P. 2d 151</a></span>; <i>State</i> v. <i>Gosser,</i> 50 N. J. 438, 446-448, <span class="citation" data-id="2387463"><a href="/opinion/2387463/state-v-gosser/#381" aria-description="Citation for case: State v. Gosser">236 A. 2d 377, 381-382</a></span>; <i>People</i> v. <i>Mitchell,</i> 39 N. Y. 2d 173, <span class="citation" data-id="5530448"><a href="/opinion/5681983/people-v-mitchell/" aria-description="Citation for case: People v. Mitchell">347 N. E. 2d 607</a></span>; <i>State</i> v. <i>Pires,</i> <span class="citation" data-id="9687213"><a href="/opinion/1827954/state-v-pires/#603" aria-description="Citation for case: State v. Pires">55 Wis. 2d 597, 603-605</a></span>, <span class="citation" data-id="9687213"><a href="/opinion/1827954/state-v-pires/#156" aria-description="Citation for case: State v. Pires">201 N. W. 2d 153, 156-158</a></span>. Other cases are collected in Note, The Emergency Doctrine, Civil Search and Seizure, and the Fourth Amendment, 43 Ford. L. Rev. 571, 584 n. 102 (1975). See also ALI Model Code of Pre-Arraignment Procedure § SS 260.5 (Prop. Off. Draft 1975). By citing these cases and those in the note following, of course, we do not mean to approve the specific holding of each case.</p>
<p>[7]  <i>E. g., </i><i>Root</i> v. <i>Gauper,</i> <span class="citation" data-id="294877"><a href="/opinion/294877/helen-frances-sutton-root-v-isabel-h-gauper/#364" aria-description="Citation for case: Helen Frances Sutton Root v. Isabel H. Gauper">438 F. 2d 361, 364-365</a></span> (CA8); <i>United States</i> v. <i>Barone,</i> <span class="citation" data-id="263973"><a href="/opinion/263973/united-states-v-salvatore-j-barone/" aria-description="Citation for case: United States v. Salvatore J. Barone">330 F. 2d 543</a></span> (CA2); <i>Wayne</i> v. <i>United States,</i> 115 U. S. App. D. C. 234, 238-243, <span class="citation" data-id="9449370"><a href="/opinion/260805/lewis-l-wayne-v-united-states/#209" aria-description="Citation for case: Lewis L. Wayne v. United States">318 F. 2d 205, 209-214</a></span> (opinion of Burger, J.); <i>United States</i> v. <i>James,</i> <span class="citation" data-id="1874080"><a href="/opinion/1874080/united-states-v-james/#533" aria-description="Citation for case: United States v. James">408 F. Supp. 527, 533</a></span> (SD Miss.); <i>United States ex rel. Parson</i> v. <i>Anderson,</i> <span class="citation" data-id="1380706"><a href="/opinion/1380706/united-states-ex-rel-parson-v-anderson/#1086" aria-description="Citation for case: United States Ex Rel. Parson v. Anderson">354 F. Supp. 1060, 1086-1087</a></span> (Del.), aff'd, <span class="citation" data-id="312200"><a href="/opinion/312200/united-states-of-america-ex-rel-norman-benjamin-parson-v-raymond-w/" aria-description="Citation for case: United States of America Ex Rel. Norman Benjamin Parson...">481 F. 2d 94</a></span> (CA3); see <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 298-299</a></span>; <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#454" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 454-456</a></span>; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14-15</a></span>.</p>
<p>[8]  The State also relies on the fact that observance of these guidelines can be enforced by a motion to suppress evidence. But the Fourth Amendment "is designed to prevent, not simply to redress, unlawful police action." <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>, 766 n. 12.</p>
<p>[9]  To what extent, if any, the evidence found in Mincey's apartment was permissibly seized under established Fourth Amendment standards will be for the Arizona courts to resolve on remand.</p>
<p>[10]  See also n. 2, <i>supra.</i></p>
<p>[11]  Because of the way in which the interrogation was conducted, the only contemporaneous record consisted of Mincey's written answers. Hust testified that the next day he went over this document and made a few notes to help him reconstruct the conversation. In a written report dated about a week later. Hust transcribed Mincey's answers and added the questions he believed he had asked. It was this written report that was used to cross-examine Mincey at his subsequent trial.</p>
<p>[12]  The trial court made no findings of fact, nor did it make a specific finding of voluntariness, and the petitioner contends that admission of the statements therefore violated <i>Jackson</i> v. <i><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">Denno</a></span></i><i>.</i> We agree with the Arizona Supreme Court, however, that the finding of voluntariness "appear[s] from the record with unmistakable clarity." <i>Sims</i> v. <i>Georgia,</i> <span class="citation" data-id="107340"><a href="/opinion/107340/sims-v-georgia/#544" aria-description="Citation for case: Sims v. Georgia">385 U. S. 538, 544</a></span>. The petitioner had originally moved to suppress his written answers to Hust's questions on two grounds: that they had been elicited in violation of <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, and that they had been involuntary. During the hearing, the prosecution stipulated that the answers would be used only to impeach the petitioner if he took the witness stand. Any violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> thus became irrelevant. <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714</a></span>; <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span>. The testimony and the briefs and arguments of counsel were thereafter directed solely to whether the answers had been voluntarily given, and the court specifically ruled that they would be admissible for impeachment purposes only. The court thus necessarily held that Mincey's responses to Hust's interrogation were voluntary.</p>
<p>[13]  In light of our holding that Mincey's hospital statements were not voluntarily given, it is unnecessary to reach his alternative contention that their use against him was impermissible because they were not sufficiently inconsistent with his trial testimony.</p>
<p>[14]  A nurse testified at the suppression hearing that the device used to aid Mincey's respiration was reserved for "more critical" patients. Moreover, Mincey apparently remained hospitalized for almost a month after the shooting. According to docket entries in the trial court his arraignment was postponed several times because he was still in the hospital; he was not arraigned until November 26, 1974.</p>
<p>[15]  For example, two of the answers written by Mincey were: "Do you me Did he give me some money (no)" and "Every body know Every body." And Mincey apparently believed he was being questioned by several different policemen, not Hust alone; although it was Hust who told Mincey he had killed a policeman, later in the interrogation Mincey indicated he thought it was someone else.</p>
<p>[16]  In his reconstruction of the interrogation, see n. 11, <i>supra,</i> Hust stated that, after he asked Mincey some questions to try to identify one of the other victims, the following ensued:
</p>
<p>"HUST: . . . What do you remember that happened?</p>
<p>"MINCEY: I remember somebody standing over me saying `move nigger, move.' I was on the floor beside the bed.</p>
<p>"HUST: Do you remember shooting anyone or firing a gun?</p>
<p>"MINCEY: <i>This is all I can say without a lawyer.</i></p>
<p>"HUST: If you want a lawyer now, I cannot talk to you any longer, however, you don't have to answer any questions if you don't want to. Do you still want to talk to me?</p>
<p>"MINCEY: (Shook his head in an affirmative manner.)</p>
<p>"HUST: What else can you remember?</p>
<p>"MINCEY: I'm going to have to put my head together. There are so many things that I don't remember I. Like how did they get into the apartment?</p>
<p>"HUST: How did who get into the apartment?</p>
<p>"MINCEY: Police.</p>
<p>"HUST: Did you sell some narcotics to the guy that was shot?</p>
<p>"MINCEY: Do you mean, did he give me some money?</p>
<p>"HUST: Yes.</p>
<p>"MINCEY: No.</p>
<p>"HUST: Did you give him a sample?</p>
<p>"MINCEY: What do you call a sample?</p>
<p>"HUST: A small amount of drug or narcotic to test?</p>
<p>"MINCEY: <i>I can't say without a lawyer.</i></p>
<p>"HUST: Did anyone say police or narcs when they came into the apartment?</p>
<p>"MINCEY: Let me get myself together first. You see, I'm not for sure everything happened so fast. I can't answer at this time because I don't think so, but I can't say for sure. Some questions aren't clear to me at the present time.</p>
<p>"HUST: Did you shoot anyone?</p>
<p>"MINCEY: <i>I can't say, I have to see a lawyer.</i>" (Emphasis supplied.)</p>
<p>While some of Mincey's answers seem relatively responsive to the questions, it must be remembered that Hust added the questions at a later date, with the answers in front of him. See n. 11, <i>supra.</i> The reliability of Hust's report is uncertain. For example, Hust claimed that immediately after Mincey first expressed a desire to remain silent, Hust said Mincey need not answer any questions but Mincey responded by indicating that he wanted to continue. There is no contemporaneous record supporting Hust's statement that Mincey acted so inconsistently immediately after asserting his wish not to respond further, nor did the nurse who was present during the interrogation corroborate Hust. The Arizona Supreme Court apparently disbelieved Hust in this respect, since it stated that "after <i>each</i> indication from [Mincey] that he wanted to consult an attorney or that he wanted to stop answering questions, the police officer continued to question [him]." <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#479" aria-description="Citation for case: State v. Mincey">115 Ariz., at 479</a></span>, <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#280" aria-description="Citation for case: State v. Mincey">566 P. 2d, at 280</a></span> (emphasis supplied).</p>
<p>[17]  In addition to the statements quoted in n. 16, <i>supra,</i> Mincey wrote at various times during the interrogation: "There are a lot of things that aren't clear," "Thats why I have to have time to redo everything that happened in my mind," and "I'm not sure as of now." He also wrote: "If its possible to get a lawyer now. We can finish the talk. He could direct me in the right direction where as without a lawyer I might saw something thinking that it means something else." And at another point he wrote: "Lets rap tomarrow, face to face. I can't give facts. If something happins that I don't know about." Before the interrogation ended, Mincey made two further requests for a lawyer.</p>
<p>[18]  <i>E. g., </i><i>Boulden</i> v. <i>Holman,</i> <span class="citation" data-id="9423981"><a href="/opinion/107893/boulden-v-holman/#480" aria-description="Citation for case: Boulden v. Holman">394 U. S. 478, 480</a></span>; <i>Clewis</i> v. <i>Texas,</i> <span class="citation" data-id="107419"><a href="/opinion/107419/clewis-v-texas/#708" aria-description="Citation for case: Clewis v. Texas">386 U. S. 707, 708</a></span>; <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#513" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503, 513-514</a></span>.</p>
<p>[1]  In its <i>Mincey</i> opinion, <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#482" aria-description="Citation for case: State v. Mincey">115 Ariz. 472, 482</a></span>, <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/#283" aria-description="Citation for case: State v. Mincey">566 P. 2d 273, 283</a></span> (1977), the Arizona Supreme Court indicated that one case other than <i>Sample</i> and <i><span class="citation" data-id="1129017"><a href="/opinion/1129017/state-v-duke/" aria-description="Citation for case: State v. Duke">Duke</a></span></i> involved the murder-scene exception. <i>State ex rel. Berger</i> v. <i>Superior Court,</i> <span class="citation" data-id="1182305"><a href="/opinion/1182305/state-ex-rel-berger-v-superior-ct-cty-of-maricopa/" aria-description="Citation for case: State Ex Rel. Berger v. SUPERIOR CT., CTY. OF MARICOPA">110 Ariz. 281</a></span>, <span class="citation" data-id="1182305"><a href="/opinion/1182305/state-ex-rel-berger-v-superior-ct-cty-of-maricopa/" aria-description="Citation for case: State Ex Rel. Berger v. SUPERIOR CT., CTY. OF MARICOPA">517 P. 2d 1277</a></span> (1974). The two-sentence opinion in the latter case, however, provides no explanation of the underlying facts and does not cite to either the Arizona court's or the Ninth Circuit's decision in <i>Sample.</i> There is thus no way to determine whether the situation in <i>Berger</i> was in any way comparable to those in <i>Sample, Duke,</i> and <i>Mincey,</i> nor any way to determine whether the <i>Berger</i> court simply disregarded the Ninth Circuit's <i>Sample</i> decision or instead, as in <i><span class="citation" data-id="1129017"><a href="/opinion/1129017/state-v-duke/" aria-description="Citation for case: State v. Duke">Duke</a></span></i> (decided just two weeks after <i>Berger</i>), viewed <i>Sample</i> as distinguishable.</p>
<p>[2]  The <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span></i> holding has not eased the burden on the lower federal courts as much as the <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span></i> majority might have hoped, since those courts have had to struggle over what this Court meant by "an opportunity for full and fair litigation of a Fourth Amendment claim," 428 U. S., at 494. See, <i>e. g., </i><i>Gates</i> v. <i>Henderson,</i> <span class="citation" data-id="9464450"><a href="/opinion/352276/arthur-richard-gates-v-robert-j-henderson-superintendent-auburn/" aria-description="Citation for case: Arthur Richard Gates v. Robert J. Henderson,...">568 F. 2d 830</a></span> (CA2 1977); <i>United States ex rel. Petillo</i> v. <i>New Jersey,</i> <span class="citation" data-id="349349"><a href="/opinion/349349/united-states-of-america-ex-rel-frank-petillo-v-state-of-new-jersey-and/" aria-description="Citation for case: United States of America Ex Rel. Frank Petillo v. State...">562 F. 2d 903</a></span> (CA3 1977); <i>O'Berry</i> v. <i>Wainwright,</i> <span class="citation" data-id="9463390"><a href="/opinion/341541/charles-wesley-oberry-v-louie-l-wainwright-director-division-of/" aria-description="Citation for case: Charles Wesley O&#x27;Berry v. Louie L. Wainwright, Director,...">546 F. 2d 1204</a></span> (CA5 1977).</p>
<p>[3]  A bill currently pending in the Congress would have the effect of overruling <i>Stone</i> v. <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Powell</a></span></i><i>,</i> S. 1314, 95th Cong., 1st Sess. (1977); see 123 Cong. Rec. 11347-11353 (1977).</p>
<p>[1]  The Supreme Court of Arizona also emphasized "the fact that [Mincey] was able to write his answers in a legible and fairly sensible fashion." <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/" aria-description="Citation for case: State v. Mincey">115 Ariz., at 480</a></span> n. 3, <span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/" aria-description="Citation for case: State v. Mincey">566 P. 2d, at 281</a></span> n. 3. The Court concedes that "Mincey's answers seem relatively responsive to the questions," <i>ante,</i> at 400 n. 16, but chooses to ignore this evidence on the ground that the "reliability of Hust's report is uncertain." <i><span class="citation" data-id="9552208"><a href="/opinion/1186434/state-v-mincey/" aria-description="Citation for case: State v. Mincey">Ibid.</a></span></i> Despite the contrary impression given by the Court, <i>ibid.,</i> the Arizona Supreme Court's opinion casts no doubt on the testimony or report of Detective Hust. The Court is thus left solely with its own conclusion as to the reliability of various witnesses based on a re-examination of the record on appeal.</p>
<p>[2]  While Mincey asked at several points to see a lawyer, he also expressed his willingness to continue talking to Detective Hust even without a lawyer. See <i>ante,</i> at 399-400, n. 16. As the Court notes, since Mincey's statements were not used as part of the prosecution's case in chief but only in impeachment, any violation of <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), was irrelevant. See <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971); <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714</a></span> (1975).</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Minnesota v. Carter.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Minnesota v. Carter"
type: case
citation: "525 U.S. 83 (1998)"
parallel_cite: "119 S. Ct. 469; 142 L. Ed. 2d 373"
neutral_cite: 1998 U.S. LEXIS 7844
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1998
date_decided: 1998-12-01
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1998-12-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Minnesota v. Carter
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118249/minnesota-v-carter/"
  cluster_id: 118249
  opinion_id: 118249
  identity_checked: true
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: "Key — Progeny / Refinement"
related: ["[[Minnesota v. Olson]]", "[[Rakas v. Illinois]]", "[[Byrd v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "standing", "expectation-of-privacy", "home", "commercial"]
holding: "A short-term visitor present in another's home for a purely commercial purpose (bagging drugs), with no prior relationship and no…"
lake:
  record_id: Minnesota v. Carter
  status: verified
  projected_at: 2026-07-10
---

# Minnesota v. Carter

*525 U.S. 83 (1998)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Acting on a tip, an officer looked through a gap in a closed apartment-window blind and saw Carter and a companion bagging cocaine. The two did not live in the apartment; they had come from another city and were present only a few hours, packaging drugs in exchange for some of the cocaine. They moved to suppress the officer's observations.

## Issue
Whether a temporary visitor present in another's home for a commercial transaction has a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] entitling him to challenge a search of that home.

## Rule
No. "Thus, an overnight guest in a home may claim the protection of the Fourth Amendment, but one who is merely present with the consent of the householder may not." — 525 U.S. at 90. ^pin-90

Whether a visitor has a legitimate expectation of privacy turns on factors such as the purely commercial nature of the visit, its short duration, and the absence of any prior connection to the home.

## Application
Carter was not an overnight guest; he was present essentially for a business transaction — bagging cocaine — for only a matter of hours, with no prior relationship to the householder. Given the purely commercial purpose, the brief stay, and the lack of any connection to the home, he had no legitimate expectation of privacy there and could not challenge the officer's observation.

## Conclusion
Reversed; Carter lacked a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] and so could not contest the search.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Carter* refines the standing framework of [[Rakas v. Illinois]] and marks the boundary of the overnight-guest rule of [[Minnesota v. Olson]].

## Appears on
- [[Standing to Challenge a Search]] — *Key — Progeny / Refinement*

## Sources
- *Minnesota v. Carter*, 525 U.S. 83 (1998) — https://www.courtlistener.com/opinion/118249/minnesota-v-carter/ — pinpoint: 90.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a2d46858925f4726", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Minnesota v. Carter"}, "payload": {"all": [{"cite": "525 U.S. 83", "page": "83", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "525"}, {"cite": "119 S. Ct. 469", "page": "469", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "119"}, {"cite": "142 L. Ed. 2d 373", "page": "373", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "142"}, {"cite": "1998 U.S. LEXIS 7844", "page": "7844", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1998"}], "display": "525 U.S. 83", "official": {"cite": "525 U.S. 83", "page": "83", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "525"}, "official_selection_present": true, "record_id": "Minnesota v. Carter"}}
{"assertion_id": "cf874d0d898b4fe7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-90", "record_id": "Minnesota v. Carter"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-90", "pinpoint_status": "slip-only", "quote": "--- # Minnesota v. Carter *525 U.S. 83 (1998)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting on a tip, an officer looked through a gap in a closed apartment-window blind and saw Carter and a companion bagging cocaine. The two did not live in the apartment; they had come from another city and were present only a few hours, packaging drugs in exchange for some of the cocaine. They moved to suppress the officer's observations. ## Issue Whether a temporary visitor present in another's home for a commercial transaction has a reasonable expectation of privacy entitling him to challenge a search of that home. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "Minnesota v. Carter", "star_marker": null}}
{"assertion_id": "6c223527b041f200", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Minnesota v. Carter"}, "payload": {"as_of_content": "1998-12-01", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Minnesota v. Carter", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Minnesota v. Carter

```json
{
  "schema_version": "s2.v1",
  "record_id": "Minnesota v. Carter",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Minnesota v. Carter",
    "case_name_short": "Carter",
    "case_name_full": "Minnesota v. Carter",
    "input_case_name": "Minnesota v. Carter",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1998-12-01",
    "year": 1998,
    "docket": null,
    "cluster_id": 118249,
    "lead_opinion_id": 118249,
    "sibling_ids": [
      118249,
      9433723,
      9433724,
      9433725,
      9433726,
      9433727
    ],
    "absolute_url": "/opinion/118249/minnesota-v-carter/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8171879,
        "score": 10,
        "case_name": "Roberson v. Minnesota"
      },
      {
        "cluster_id": 9183639,
        "score": 10,
        "case_name": "Johnson v. Gillis"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "525 U.S. 83",
      "volume": "525",
      "reporter": "U.S.",
      "page": "83",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "119 S. Ct. 469",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "469",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "142 L. Ed. 2d 373",
        "volume": "142",
        "reporter": "L. Ed. 2d",
        "page": "373",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1998 U.S. LEXIS 7844",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "7844",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "525 U.S. 83",
        "volume": "525",
        "reporter": "U.S.",
        "page": "83",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "119 S. Ct. 469",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "469",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "142 L. Ed. 2d 373",
        "volume": "142",
        "reporter": "L. Ed. 2d",
        "page": "373",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 U.S. LEXIS 7844",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "7844",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "525 U.S. 83",
    "official_selection": {
      "court_class": "scotus",
      "selected": "525 U.S. 83",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-90",
      "page": null,
      "quote": "--- # Minnesota v. Carter *525 U.S. 83 (1998)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting on a tip, an officer looked through a gap in a closed apartment-window blind and saw Carter and a companion bagging cocaine. The two did not live in the apartment; they had come from another city and were present only a few hours, packaging drugs in exchange for some of the cocaine. They moved to suppress the officer's observations. ## Issue Whether a temporary visitor present in another's home for a commercial transaction has a reasonable expectation of privacy entitling him to challenge a search of that home. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1998-12-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Minnesota v. Carter",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Andrew Lennette, Individually and on behalf of C.L., O.L. and S.L., Minor Children v. State of Iowa, Melody Siver, Amy Howell, and Valerie Lovaglia",
          "cluster_id": 6476611,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Aiken",
          "cluster_id": 8619549,
          "cite": [
            "877 F.3d 451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brock v. Dunning",
          "cluster_id": 2722122,
          "cite": [
            "288 Neb. 909"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Howard",
          "cluster_id": 2698731,
          "cite": [
            "2013 Ohio 2884"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Howard",
          "cluster_id": 2698874,
          "cite": [
            "2013 Ohio 1972"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ortiz",
          "cluster_id": 8477550,
          "cite": [
            "507 F. App'x 339"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Tony Lavan v. City of Los Angeles",
          "cluster_id": 807915,
          "cite": [
            "693 F.3d 1022",
            "2012 WL 3834659",
            "2012 U.S. App. LEXIS 18639"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Keith, 08ap-28 (11-25-2008)",
          "cluster_id": 4000684,
          "cite": [
            "2008 Ohio 6122"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Funk",
          "cluster_id": 4002857,
          "cite": [
            "896 N.E.2d 203",
            "177 Ohio App. 3d 814",
            "2008 Ohio 4086"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City of Akron v. Callaway",
          "cluster_id": 3971187,
          "cite": [
            "826 N.E.2d 879",
            "160 Ohio App. 3d 229",
            "2005 Ohio 1471"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Damen Anthony Davis",
          "cluster_id": 782371,
          "cite": [
            "332 F.3d 1163",
            "2003 Daily Journal DAR 6324",
            "2003 Cal. Daily Op. Serv. 4998",
            "2003 U.S. App. LEXIS 11556",
            "2003 WL 21349353"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Walter v. State",
          "cluster_id": 1755500,
          "cite": [
            "28 S.W.3d 538",
            "2000 Tex. Crim. App. LEXIS 84",
            "2000 WL 1348504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Linette Perez, United States of America v. Juancho Alcantera, United States of America v. Edmundo Batoon",
          "cluster_id": 776532,
          "cite": [
            "280 F.3d 318",
            "2002 WL 171241"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ayala",
          "cluster_id": 2551468,
          "cite": [
            "1 P.3d 3",
            "96 Cal. Rptr. 2d 682",
            "23 Cal. 4th 225",
            "2000 Cal. Daily Op. Serv. 4490",
            "2000 Daily Journal DAR 6037",
            "2000 Cal. LEXIS 4545"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Figueroa v. Mazza",
          "cluster_id": 3209159,
          "cite": [
            "825 F.3d 89",
            "2016 U.S. App. LEXIS 10152",
            "2016 WL 3126772"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, State of California, Intervenor v. Raphyal Crawford, AKA Aarmyl Crawford",
          "cluster_id": 786677,
          "cite": [
            "372 F.3d 1048",
            "2004 U.S. App. LEXIS 12116",
            "2004 WL 1375521"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'HARA v. State",
          "cluster_id": 2275765,
          "cite": [
            "27 S.W.3d 548",
            "2000 Tex. Crim. App. LEXIS 83",
            "2000 WL 1347932"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beeman v. State",
          "cluster_id": 2351958,
          "cite": [
            "86 S.W.3d 613",
            "2002 Tex. Crim. App. LEXIS 198",
            "2002 WL 31255414"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Espinosa v. City and County of San Francisco",
          "cluster_id": 1224431,
          "cite": [
            "598 F.3d 528",
            "2010 U.S. App. LEXIS 4905",
            "2010 WL 775891"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robles",
          "cluster_id": 5607956,
          "cite": [
            "23 Cal. 4th 789",
            "3 P.3d 311",
            "2000 Daily Journal DAR 7789",
            "97 Cal. Rptr. 2d 914",
            "2000 Cal. Daily Op. Serv. 5894",
            "2000 Cal. LEXIS 5217"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Loria v. Gorman",
          "cluster_id": 7108550,
          "cite": [
            "306 F.3d 1271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sarkisian",
          "cluster_id": 7079538,
          "cite": [
            "197 F.3d 966",
            "1999 WL 1083966"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robles",
          "cluster_id": 2545158,
          "cite": [
            "3 P.3d 311",
            "97 Cal. Rptr. 2d 914",
            "23 Cal. 4th 789"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Granville, Anthony",
          "cluster_id": 2950015,
          "cite": [
            "423 S.W.3d 399",
            "2014 WL 714730",
            "2014 Tex. Crim. App. LEXIS 237"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Sanders",
          "cluster_id": 2545822,
          "cite": [
            "73 P.3d 496",
            "2 Cal. Rptr. 3d 630",
            "31 Cal. 4th 318"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Poe",
          "cluster_id": 171851,
          "cite": [
            "556 F.3d 1113",
            "2009 U.S. App. LEXIS 5237",
            "2009 WL 514069"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moreno v. Baca",
          "cluster_id": 792690,
          "cite": [
            "431 F.3d 633",
            "2005 WL 3338300"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Juan Rodrigo Gamez-Orduno, Jose Martinez-Carra, Jesus Martinez-Villa",
          "cluster_id": 771497,
          "cite": [
            "235 F.3d 453",
            "2000 Daily Journal DAR 13260",
            "2000 Cal. Daily Op. Serv. 9936",
            "2000 U.S. App. LEXIS 31826"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Schmitz",
          "cluster_id": 821521,
          "cite": [
            "55 Cal. 4th 909",
            "288 P.3d 1259",
            "149 Cal. Rptr. 3d 640",
            "2012 WL 5990981",
            "2012 Cal. LEXIS 11006"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Welch v. State",
          "cluster_id": 1891607,
          "cite": [
            "93 S.W.3d 50",
            "2002 Tex. Crim. App. LEXIS 167",
            "2002 WL 31080716"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Frederick Alonzo Waller",
          "cluster_id": 792220,
          "cite": [
            "426 F.3d 838",
            "2005 U.S. App. LEXIS 22941",
            "2005 WL 2708784"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Theodore E. Loria v. Charles Gorman, Individually and in His Capacity as a Police Officer for the City of Rochester, Robert Nitchman, Individually and in His Capacity as a Police Officer for the City of Rochester, City of Rochester, Mark Wiater, George Markert, Individually and in His Capacity as a Police Officer for the City of Rochester, Vasquez, Individually and in His Capacity as a Police Officer for the City of Rochester, Debra Stritzel, Individually and in Her Capacity as an Employee of the City of Rochester, Theodore E. Loria v. Dale Feor, Individually and in His Capacity as a Police Officer for the City of Rochester, City of Rochester",
          "cluster_id": 779429,
          "cite": [
            "306 F.3d 1271",
            "2002 U.S. App. LEXIS 20458"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rhiger",
          "cluster_id": 162945,
          "cite": [
            "315 F.3d 1283",
            "115 A.L.R. 5th 797",
            "2003 U.S. App. LEXIS 519",
            "2003 WL 116128"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morse v. Cloutier",
          "cluster_id": 4421636,
          "cite": [
            "869 F.3d 16"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Martin (Slip Opinion)",
          "cluster_id": 4425665,
          "cite": [
            "2017 Ohio 7556"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Carter:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118249 OR 9433723 OR 9433724 OR 9433725 OR 9433726 OR 9433727) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 179,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 11,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 179,
        "triage_read": 12,
        "triage_snippet_classified": 167
      },
      "lane2_top_cited": {
        "query": "cites:(118249 OR 9433723 OR 9433724 OR 9433725 OR 9433726 OR 9433727)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NCZzPTc5ODE1NyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118249+OR+9433723+OR+9433724+OR+9433725+OR+9433726+OR+9433727%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118249 OR 9433723 OR 9433724 OR 9433725 OR 9433726 OR 9433727)",
        "reviewed": 24,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 24,
        "triage_read": 0,
        "triage_snippet_classified": 24
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118249 OR 9433723 OR 9433724 OR 9433725 OR 9433726 OR 9433727)",
    "indexed_citing_opinions": 268,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118249,
        "count": 115,
        "count_source": "search"
      },
      {
        "opinion_id": 9433723,
        "count": 166,
        "count_source": "search"
      },
      {
        "opinion_id": 9433724,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433725,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433726,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433727,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1223,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/minnesota-v-carter.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5OTA3OCZzPTEwMTIxNjg4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118249+OR+9433723+OR+9433724+OR+9433725+OR+9433726+OR+9433727%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118249,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 106282,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 108770,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 110325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 111504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 111927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 112175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 112416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 1691283,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 1833260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118249,
        "cited_id": 1833688,
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
    "date_created": "2026-07-05T13:53:43Z",
    "date_modified": "2026-07-10T00:12:42Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:54:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:54:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:58:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:54:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Minnesota v. Carter

```
<div>
<center><b><span class="citation no-link">525 U.S. 83</span> (1998)</b></center>
<center><h1>MINNESOTA<br>
v.<br>
CARTER</h1></center>
<center>No. 97-1147.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued October 6, 1998.</center>
<center>Decided December 1, 1998.<sup>[*]</sup></center>
CERTIORARI TO THE SUPREME COURT OF MINNESOTA
<p><span class="star-pagination">*84</span> Rehnquist, C. J., delivered the opinion of the Court, in which O'Connor, Scalia, Kennedy, and Thomas, JJ., joined. Scalia, J., filed a concurring opinion, in which Thomas, J., joined, <i>post,</i> p. 91. Kennedy, J., filed a concurring opinion, <i>post,</i> p. 99. Breyer, J., filed an opinion concurring in the judgment, <i>post,</i> p. 103. Ginsburg, J., filed a dissenting opinion, in which Stevens and Souter, JJ., joined, <i>post,</i> p. 106.</p>
<p><i>James C. Backstrom</i> argued the cause for petitioner. With him on the briefs were <i>Hubert H. Humphrey III,</i> Attorney General of Minnesota, and <i>Phillip D. Prokopowicz.</i></p>
<p><i>Jeffrey A. Lamken</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Waxman, Acting Assistant Attorney General Keeney,</i> and <i>Deputy Solicitor General Dreeben.</i></p>
<p><i>Bradford Colbert</i> argued the cause for respondents. With him on the brief were <i>John M. Stuart, Lawrence Hammerling, Marie L. Wolf,</i> and <i>Scott G. Swanson.</i><sup>[]</sup></p>
<p><span class="star-pagination">*85</span> Chief Justice Rehnquist delivered the opinion of the Court.</p>
<p>Respondents and the lessee of an apartment were sitting in one of its rooms, bagging cocaine. While so engaged they were observed by a police officer, who looked through a drawn window blind. The Supreme Court of Minnesota held that the officer's viewing was a search that violated respondents' Fourth Amendment rights. We hold that no such violation occurred.</p>
<p>James Thielen, a police officer in the Twin Cities' suburb of Eagan, Minnesota, went to an apartment building to investigate a tip from a confidential informant. The informant said that he had walked by the window of a ground-floor apartment and had seen people putting a white powder into bags. The officer looked in the same window through a gap in the closed blind and observed the bagging operation for several minutes. He then notified headquarters, which began preparing affidavits for a search warrant while he returned to the apartment building. When two men left the building in a previously identified Cadillac, the police stopped the car. Inside were respondents Carter and Johns. As the police opened the door of the car to let Johns out, they observed a black, zippered pouch and a handgun, later determined to be loaded, on the vehicle's floor. Carter and Johns were arrested, and a later police search of the vehicle the next day discovered pagers, a scale, and 47 grams of cocaine in plastic sandwich bags.</p>
<p><span class="star-pagination">*86</span> After seizing the car, the police returned to apartment 103 and arrested the occupant, Kimberly Thompson, who is not a party to this appeal. A search of the apartment pursuant to a warrant revealed cocaine residue on the kitchen table and plastic baggies similar to those found in the Cadillac. Thielen identified Carter, Johns, and Thompson as the three people he had observed placing the powder into baggies. The police later learned that while Thompson was the lessee of the apartment, Carter and Johns lived in Chicago and had come to the apartment for the sole purpose of packaging the cocaine. Carter and Johns had never been to the apartment before and were only in the apartment for approximately 2<sup>[1]</sup>20442 hours. In return for the use of the apartment, Carter and Johns had given Thompson one-eighth of an ounce of the cocaine.</p>
<p>Carter and Johns were charged with conspiracy to commit a controlled substance crime in the first degree and aiding and abetting in a controlled substance crime in the first degree, in violation of <span class="citation no-link">Minn. Stat. §§ 152.021</span>, subds. 1(1), 3(a), 609.05 (1996). They moved to suppress all evidence obtained from the apartment and the Cadillac, as well as to suppress several postarrest incriminating statements they had made. They argued that Thielen's initial observation of their drug packaging activities was an unreasonable search in violation of the Fourth Amendment and that all evidence obtained as a result of this unreasonable search was inadmissible as fruit of the poisonous tree. The Minnesota trial court held that since, unlike the defendant in <i>Minnesota</i> v. <i>Olson,</i> <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">495 U. S. 91</a></span> (1990), Carter and Johns were not overnight social guests but temporary out-of-state visitors, they were not entitled to claim the protection of the Fourth Amendment against the government intrusion into the apartment. The trial court also concluded that Thielen's observation was not a search within the meaning of the Fourth Amendment. After a trial, Carter and Johns were each convicted of both offenses. The Minnesota Court of Appeals <span class="star-pagination">*87</span> held that respondent Carter did not have "standing" to object to Thielen's actions because his claim that he was predominantly a social guest was "inconsistent with the only evidence concerning his stay in the apartment, which indicates that he used it for a business purposeto package drugs." <span class="citation" data-id="1691283"><a href="/opinion/1691283/state-v-carter/#698" aria-description="Citation for case: State v. Carter">545 N. W. 2d 695, 698</a></span> (1996). In a separate appeal, the Court of Appeals also affirmed Johns' conviction, without addressing what it termed the "standing" issue. <i>State</i> v. <i>Johns,</i> No. C9-95-1765 (June 11, 1996), App. D-1, D-3 (unpublished).</p>
<p>A divided Minnesota Supreme Court reversed, holding that respondents had "standing" to claim the protection of the Fourth Amendment because they had "`a legitimate expectation of privacy in the invaded place.' " <span class="citation" data-id="9687539"><a href="/opinion/1833260/state-v-carter/#174" aria-description="Citation for case: State v. Carter">569 N. W. 2d 169, 174</a></span> (1997) (quoting <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 143</a></span> (1978)). The court noted that even though "society does not recognize as valuable the task of bagging cocaine, we conclude that society does recognize as valuable the right of property owners or leaseholders to invite persons into the privacy of their homes to conduct a common task, be it legal or illegal activity. We, therefore, hold that [respondents] had standing to bring [their] motion to suppress the evidence gathered as a result of Thielen's observations." <span class="citation" data-id="9687539"><a href="/opinion/1833260/state-v-carter/#176" aria-description="Citation for case: State v. Carter">569 N. W. 2d, at 176</a></span>; see also <span class="citation multiple-matches"><a href="/c/N.%20W.%202d/569/180/">569 N. W. 2d 180</a></span>, 181 (1997). Based upon its conclusion that respondents had "standing" to raise their Fourth Amendment claims, the court went on to hold that Thielen's observation constituted a search of the apartment under the Fourth Amendment, and that the search was unreasonable. <i>Id.,</i> at 176-179. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./523/1003/">523 U. S. 1003</a></span> (1998), and now reverse.</p>
<p>The Minnesota courts analyzed whether respondents had a legitimate expectation of privacy under the rubric of "standing" doctrine, an analysis that this Court expressly rejected 20 years ago in <i>Rakas.</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#139" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 139-140</a></span>. In that case, we held that automobile passengers could not assert the protection of the Fourth Amendment against the <span class="star-pagination">*88</span> seizure of incriminating evidence from a vehicle where they owned neither the vehicle nor the evidence. <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Ibid.</a></span></i> Central to our analysis was the idea that in determining whether a defendant is able to show the violation of his (and not someone else's) Fourth Amendment rights, the "definition of those rights is more properly placed within the purview of substantive Fourth Amendment law than within that of standing." <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#140" aria-description="Citation for case: Rakas v. Illinois"><i>Id.,</i> at 140</a></span>. Thus, we held that in order to claim the protection of the Fourth Amendment, a defendant must demonstrate that he personally has an expectation of privacy in the place searched, and that his expectation is reasonable; <i>i. e.,</i> one that has "a source outside of the Fourth Amendment, either by reference to concepts of real or personal property law or to understandings that are recognized and permitted by society." <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois"><i>Id.,</i> at 143-144</a></span>, and n. 12. See also <i>Smith</i> v. <i>Maryland,</i> <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#740" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735, 740-741</a></span> (1979).</p>
<p>The Fourth Amendment guarantees: "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." The Amendment protects persons against unreasonable searches of "their persons [and] houses" and thus indicates that the Fourth Amendment is a personal right that must be invoked by an individual. See <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967) ("[T]he Fourth Amendment protects people, not places"). But the extent to which the Fourth Amendment protects people may depend upon where those people are. We have held that "capacity to claim the protection of the Fourth Amendment depends . . . upon whether the person who claims the protection of the Amendment has a legitimate expectation of privacy in the invaded place." <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois"><i>Rakas, supra,</i> at 143</a></span>. See also <i>Rawlings</i> v. <i>Kentucky,</i> <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/#106" aria-description="Citation for case: Rawlings v. Kentucky">448 U. S. 98, 106</a></span> (1980).</p>
<p><span class="star-pagination">*89</span> The text of the Amendment suggests that its protections extend only to people in "their" houses. But we have held that in some circumstances a person may have a legitimate expectation of privacy in the house of someone else. In <i>Minnesota</i> v. <i>Olson,</i> <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">495 U. S. 91</a></span> (1990), for example, we decided that an overnight guest in a house had the sort of expectation of privacy that the Fourth Amendment protects. We said:</p>
<blockquote>"To hold that an overnight guest has a legitimate expectation of privacy in his host's home merely recognizes the every day expectations of privacy that we all share. Staying overnight in another's home is a longstanding social custom that serves functions recognized as valuable by society. We stay in others' homes when we travel to a strange city for business or pleasure, when we visit our parents, children, or more distant relatives out of town, when we are in between jobs or homes, or when we house-sit for a friend. . . . "From the overnight guest's perspective, he seeks shelter in another's home precisely because it provides him with privacy, a place where he and his possessions will not be disturbed by anyone but his host and those his host allows inside. We are at our most vulnerable when we are asleep because we cannot monitor our own safety or the security of our belongings. It is for this reason that, although we may spend all day in public places, when we cannot sleep in our own home we seek out another private place to sleep, whether it be a hotel room, or the home of a friend." <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/#98" aria-description="Citation for case: Minnesota v. Olson"><i>Id.,</i> at 98-99</a></span>.</blockquote>
<p>In <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#259" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 259</a></span> (1960), the defendant seeking to exclude evidence resulting from a search of an apartment had been given the use of the apartment by a friend. He had clothing in the apartment, had slept there "`maybe a night,' " and at the time was the sole occupant of the apartment. But while the holding of <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> that a search of the apartment violated the defendant's <span class="star-pagination">*90</span> Fourth Amendment rightsis still valid, its statement that "anyone legitimately on the premises where a search occurs may challenge its legality," <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States"><i>id.,</i> at 267</a></span>, was expressly repudiated in <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978). Thus, an overnight guest in a home may claim the protection of the Fourth Amendment, but one who is merely present with the consent of the householder may not.</p>
<p>Respondents here were obviously not overnight guests, but were essentially present for a business transaction and were only in the home a matter of hours. There is no suggestion that they had a previous relationship with Thompson, or that there was any other purpose to their visit. Nor was there anything similar to the overnight guest relationship in <i><span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">Olson</a></span></i> to suggest a degree of acceptance into the household.<sup>[*]</sup> While the apartment was a dwelling place for Thompson, it was for these respondents simply a place to do business.</p>
<p>Property used for commercial purposes is treated differently for Fourth Amendment purposes from residential property. "An expectation of privacy in commercial premises, however, is different from, and indeed less than, a similar expectation in an individual's home." <i>New York</i> v. <i>Burger,</i>  <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#700" aria-description="Citation for case: New York v. Burger">482 U. S. 691, 700</a></span> (1987). And while it was a "home" in which respondents were present, it was not their home. Similarly, the Court has held that in some circumstances a worker can claim Fourth Amendment protection over his <span class="star-pagination">*91</span> own workplace. See, <i>e. g., </i><i>O'Connor</i> v. <i>Ortega,</i> <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709</a></span> (1987). But there is no indication that respondents in this case had nearly as significant a connection to Thompson's apartment as the worker in <i><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O'Connor</a></span></i> had to his own private office. See <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#716" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><i>id.,</i> at 716-717</a></span>.</p>
<p>If we regard the overnight guest in <i>Minnesota</i> v. <i><span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">Olson</a></span></i> as typifying those who may claim the protection of the Fourth Amendment in the home of another, and one merely "legitimately on the premises" as typifying those who may not do so, the present case is obviously somewhere in between. But the purely commercial nature of the transaction engaged in here, the relatively short period of time on the premises, and the lack of any previous connection between respondents and the householder, all lead us to conclude that respondents' situation is closer to that of one simply permitted on the premises. We therefore hold that any search which may have occurred did not violate their Fourth Amendment rights.</p>
<p>Because we conclude that respondents had no legitimate expectation of privacy in the apartment, we need not decide whether the police officer's observation constituted a "search." The judgments of the Supreme Court of Minnesota are accordingly reversed, and the cause is remanded for proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>Justice Scalia, with whom Justice Thomas joins, concurring.</p>
<p>I join the opinion of the Court because I believe it accurately applies our recent case law, including <i>Minnesota</i> v. <i>Olson,</i> <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">495 U. S. 91</a></span> (1990). I write separately to express my view that that case lawlike the submissions of the parties in this casegives short shrift to the text of the Fourth Amendment, and to the well and long understood meaning of that text. Specifically, it leaps to apply the fuzzy standard of "legitimate expectation of privacy"a consideration that <span class="star-pagination">*92</span> is often relevant to whether a search or seizure covered by the Fourth Amendment is "unreasonable"to the threshold question whether a search or seizure covered by the Fourth Amendment <i>has occurred.</i> If that latter question is addressed first and analyzed under the text of the Constitution as traditionally understood, the present case is not remotely difficult.</p>
<p>The Fourth Amendment protects "[t]he right of the people to be secure in <i>their</i> persons, houses, papers, and effects, against unreasonable searches and seizures . . . ." U. S. Const., Amdt. 4 (emphasis added). It must be acknowledged that the phrase "their . . . houses" in this provision is, in isolation, ambiguous. It could mean "their respective houses," so that the protection extends to each person only in his <i>own</i> house. But it could also mean "their respective and each other's houses," so that each person would be protected even when visiting the house of someone else. As today's opinion for the Court suggests, however, <i>ante,</i> at 88-90, it is not linguistically possible to give the provision the latter, expansive interpretation with respect to "houses" without giving it the same interpretation with respect to the nouns that are parallel to "houses""persons, . . . papers, and effects"which would give me a constitutional right not to have your person unreasonably searched. This is so absurd that it has to my knowledge never been contemplated. The obvious meaning of the provision is that <i>each</i> person has the right to be secure against unreasonable searches and seizures in <i>his own</i> person, house, papers, and effects.</p>
<p>The founding-era materials that I have examined confirm that this was the understood meaning. (Strangely, these materials went unmentioned by the State and its <i>amici</i>  unmentioned even in the State's reply brief, even though respondents had thrown down the gauntlet: "In briefs totaling over 100 pages, the State of Minnesota, the amici 26 attorneys general, and the Solicitor General of the United States of America have not mentioned one word about the history <span class="star-pagination">*93</span> and purposes of the Fourth Amendment or the intent of the framers of that amendment." Brief for Respondents 12, n. 4.) Like most of the provisions of the Bill of Rights, the Fourth Amendment was derived from provisions already existing in state constitutions. Of the four of those provisions that contained language similar to that of the Fourth Amendment,<sup>[1]</sup> two used the same ambiguous "their" terminology. See Pa. Const., Art. X (1776) ("That the people have a right to hold themselves, their houses, papers, and possessions free from search and seizure . . ."); Vt. Const., ch. I, § XI (1777) ("That the people have a right to hold themselves, their houses, papers, and possessions free from search or seizure. . ."). The other two, however, avoided the ambiguity by using the singular instead of the plural. See Mass. Const., pt. I, Art. XIV (1780) ("Every subject has a right to be secure from all unreasonable searches, and seizures of his person, his houses, his papers, and all his possessions"); N. H. Const., § XIX (1784) ("Every subject hath a right to be secure from all unreasonable searches and seizures of his person, his houses, his papers, and all his possessions"). The New York Convention that ratified the Constitution proposed an amendment that would have given every freeman "a right to be secure from all unreasonable searches and seizures of <i>his</i>  person <i>his</i> papers or <i>his</i> property," 4 B. Schwartz, The Roots of the Bill of Rights 913 (1980) (reproducing New York proposed amendments, 1778) (emphases added), and the Declaration of Rights that the North Carolina Convention demanded prior to its ratification contained a similar provision protecting a freeman's right against "unreasonable searches and seizures of <i>his</i> person, <i>his</i> papers and property," <i>id.,</i> at 968 (reproducing North Carolina proposed Declaration of Rights, 1778) (emphases added). There is no indication anyone believed <span class="star-pagination">*94</span> that the Massachusetts, New Hampshire, New York, and North Carolina texts, by using the word "his" rather than "their," narrowed the protections contained in the Pennsylvania and Vermont Constitutions.</p>
<p>That "their . . . houses" was understood to mean "their respective houses" would have been clear to anyone who knew the English and early American law of arrest and trespass that underlay the Fourth Amendment. The people's protection against unreasonable search and seizure in their "houses" was drawn from the English common-law maxim, "A man's home is <i>his</i> castle." As far back as <i>Semayne's Case</i> of 1604, the leading English case for that proposition (and a case cited by Coke in his discussion of the proposition that Magna Carta outlawed general warrants based on mere surmise, 4 E. Coke, Institutes 176-177 (1797)), the King's Bench proclaimed that "the house of any one is not a castle or privilege but for himself, and shall not extend to protect any person who flies to his house." 5 Co. Rep. 91a, 93a, 77 Eng. Rep. 194, 198 (K. B.). Thus Cooley, in discussing Blackstone's statement that a bailiff could not break into a house to conduct an arrest because "every man's house is looked upon by the law to be his castle," 3 W. Blackstone, Commentaries on the Laws of England 288 (1768), added the explanation: "[I]t is the defendant's own dwelling which by law is said to be his castle; for if he be in the house of another, the bailiff or sheriff may break and enter it to effect his purpose. . . ." 3 W. Blackstone, Commentaries on the Laws of England 287, n. 5 (T. Cooley 2d rev. ed. 1872). See also <i>Johnson</i>  v. <i>Leigh,</i> 6 Taunt. 246, 248, 128 Eng. Rep. 1029, 1030 (C. P. 1815) ("[I]n many cases the door of a third person may be broken where that of the Defendant himself cannot; for though every man's house is his own castle, it is not the castle of another man").<sup>[2]</sup></p>
<p><span class="star-pagination">*95</span> Of course this is not to say that the Fourth Amendment protects only the Lord of the Manor who holds his estate in fee simple. People call a house "their" home when legal title <span class="star-pagination">*96</span> is in the bank, when they rent it, and even when they merely occupy it rent free<i>so long as they actually live there.</i>  That this is the criterion of the people's protection against government intrusion into "their" houses is established by the leading American case of <i>Oystead</i> v. <i>Shed,</i> <span class="citation" data-id="6404533"><a href="/opinion/6530830/oystead-v-shed/" aria-description="Citation for case: Oystead v. Shed">13 Mass. 520</a></span> (1816), which held it a trespass for the sheriff to break into a dwelling to capture a boarder who lived there. The court reasoned that the "inviolability of dwelling-houses" described by Foster, Hale, and Coke extends to "the occupier or any of his family . . . who have their domicile or ordinary residence there," including "a boarder or a servant" "who have made the house <i>their</i> home." <span class="citation" data-id="6404533"><a href="/opinion/6530830/oystead-v-shed/#523" aria-description="Citation for case: Oystead v. Shed"><i>Id.,</i> at 523</a></span> (emphasis added). But, it added, "the house shall not be made a sanctuary" for one such as "a stranger, or perhaps a visitor," who "upon a pursuit, take[s] refuge in the house of another," for "the house is not <i>his</i> castle; and the officer may break open the doors or windows in order to execute his process." <i><span class="citation" data-id="6404533"><a href="/opinion/6530830/oystead-v-shed/" aria-description="Citation for case: Oystead v. Shed">Ibid.</a></span></i>  (emphasis in original).</p>
<p>Thus, in deciding the question presented today we write upon a slate that is far from clean. The text of the Fourth Amendment, the common-law background against which it was adopted, and the understandings consistently displayed after its adoption make the answer clear. We were right to hold in <i>Chapman</i> v. <i>United States,</i> <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span> (1961), that the Fourth Amendment protects an apartment tenant against an unreasonable search of his dwelling, even though he is only a leaseholder. And we were right to hold in <i>Bumper</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543</a></span> (1968), that an unreasonable search of a grandmother's house violated her resident grandson's Fourth Amendment rights because the area searched "was <i>his</i> home," <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#548" aria-description="Citation for case: Bumper v. North Carolina"><i>id.,</i> at 548, n. 11</a></span> (emphasis added). We went to the absolute limit of what text and tradition permit in <i>Minnesota</i> v. <i>Olson,</i> <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">495 U. S. 91</a></span> (1990), when we protected a mere overnight guest against an unreasonable <span class="star-pagination">*97</span> search of his hosts' apartment. But whereas it is plausible to regard a person's overnight lodging as at least his "temporary" residence, it is entirely impossible to give that characterization to an apartment that he uses to package cocaine. Respondents here were not searched in "their . . . hous[e]" under any interpretation of the phrase that bears the remotest relationship to the well-understood meaning of the Fourth Amendment.</p>
<p>The dissent believes that "[o]ur obligation to produce coherent results" requires that we ignore this clear text and 4-century-old tradition, and apply instead the notoriously unhelpful test adopted in a "benchmar[k]" decision that is 31 years old. <i>Post,</i> at 110, citing <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967). In my view, the only thing the past three decades have established about the <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> test (which has come to mean the test enunciated by Justice Harlan's separate concurrence in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> see <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States"><i>id.,</i> at 360</a></span>) is that, unsurprisingly, those "actual (subjective) expectation[s] of privacy" "that society is prepared to recognize as `reasonable,' " <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States"><i>id.,</i>  at 361</a></span>, bear an uncanny resemblance to those expectations of privacy that this Court considers reasonable. When that self-indulgent test is employed (as the dissent would employ it here) to determine whether a "search or seizure" within the meaning of the Constitution has <i>occurred</i> (as opposed to whether that "search or seizure" is an "unreasonable" one), it has no plausible foundation in the text of the Fourth Amendment. That provision did not guarantee some generalized "right of privacy" and leave it to this Court to determine which particular manifestations of the value of privacy "society is prepared to recognize as `reasonable.' " <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Ibid.</a></span></i>  Rather, it enumerated ("persons, houses, papers, and effects") the objects of privacy protection to which the <i>Constitution</i> would extend, leaving further expansion to the good <span class="star-pagination">*98</span> judgment, not of this Court, but of the people through their representatives in the legislature.<sup>[3]</sup></p>
<p>The dissent may be correct that a person invited into someone else's house to engage in a common business (even common monkey business, so to speak) <i>ought</i> to be protected against government searches of the room in which that business is conducted; and that persons invited in to deliver milk or pizza (whom the dissent dismisses as "classroom hypotheticals," <i>post,</i> at 107, as opposed, presumably, to flesh-andblood hypotheticals) ought <i>not</i> to be protected against government searches of the rooms that they occupy. I am not sure of the answer to those policy questions. But I am sure that the answer is not remotely contained in the Constitution, which means that it is leftas <i>many,</i> indeed <i>most,</i> important questions are leftto the judgment of state and federal legislators. We go beyond our proper role as judges in a democratic society when we restrict the people's power to <span class="star-pagination">*99</span> govern themselves over the full range of policy choices that the Constitution has left available to them.</p>
<p>Justice Kennedy, concurring.</p>
<p>I join the Court's opinion, for its reasoning is consistent with my view that almost all social guests have a legitimate expectation of privacy, and hence protection against unreasonable searches, in their host's home.</p>
<p>The Fourth Amendment protects "[t]he right of the people to be secure in their . . . houses," and it is beyond dispute that the home is entitled to special protection as the center of the private lives of our people. Security of the home must be guarded by the law in a world where privacy is diminished by enhanced surveillance and sophisticated communication systems. As is well established, however, Fourth Amendment protection, though dependent upon spatial definition, is in essence a personal right. Thus, as the Court held in <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978), there are limits on who may assert it.</p>
<p>The dissent, as I interpret it, does not question <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span></i> or the principle that not all persons in the company of the property owner have the owner's right to assert the spatial protection. <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span>,</i> it is true, involved automobiles, where the necessities of law enforcement permit more latitude to the police than ought to be extended to houses. The analysis in <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span></i> was not conceived, however, as a utilitarian exception to accommodate the needs of law enforcement. The Court's premise was a more fundamental one. Fourth Amendment rights are personal, and when a person objects to the search of a place and invokes the exclusionary rule, he or she must have the requisite connection to that place. The analysis in <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span></i> must be respected with reference to dwellings unless that precedent is to be overruled or so limited to its facts that its underlying principle is, in the end, repudiated.</p>
<p>As to the English authorities that were the historical basis for the Fourth Amendment, the Court has observed that <span class="star-pagination">*100</span> scholars dispute their proper interpretation. See, <i>e. g., </i><i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#592" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 592</a></span> (1980). <i>Semayne's Case,</i> 5 Co. Rep. 91a, 77 Eng. Rep. 194 (K. B. 1604), says that "the house of every one is to him as his castle and fortress" and the home is privileged for the homeowner, "his family," and "his own proper goods." <i><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Id.,</a></span></i> at 91b, 93a, 77 Eng. Rep., at 195, 198. Read narrowly, the protections recognized in <i>Semayne's Case</i> might have been confined to the context of civil process, and so be of limited application to enforcement of the criminal law. Even if, at the time of <i>Semayne's Case,</i>  a man's home was not his castle with respect to incursion by the King in a criminal matter, that would not be dispositive of the question before us. The axiom that a man's home is his castle, or the statement attributed to Pitt that the King cannot enter and all his force dares not cross the threshold, see <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#307" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 307</a></span> (1958), has acquired over time a power and an independent significance justifying a more general assurance of personal security in one's home, an assurance which has become part of our constitutional tradition.</p>
<p>It is now settled, for example, that for a routine felony arrest and absent exigent circumstances, the police must obtain a warrant before entering a home to arrest the homeowner. <i>Payton</i> v. <i>New York, supra,</i> at 576. So, too, the Court held in <i>Steagald</i> v. <i>United States,</i> <span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">451 U. S. 204</a></span> (1981), that, absent exigent circumstances or consent, the police cannot search for the subject of an arrest warrant in the home of a third party, without first obtaining a search warrant directing entry.</p>
<p>These cases strengthen and protect the right of the homeowner to privacy in his own home. They do not speak, however, to the right to claim such a privacy interest in the home of another. See, <span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/#218" aria-description="Citation for case: Steagald v. United States"><i>e. g., id.,</i> at 218-219</a></span> (noting that the issue in <i><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">Steagald</a></span></i> was the homeowner's right to privacy in his own home, and not the right to "claim sanctuary from arrest in the home of a third party"). <i><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">Steagald</a></span></i> itself affirmed that, <span class="star-pagination">*101</span> in accordance with the common law, our Fourth Amendment precedents "recogniz[e] . . .that rights such as those conferred by the Fourth Amendment are personal in nature, and cannot bestow vicarious protection on those who do not have a reasonable expectation of privacy in the place to be searched." <span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/#219" aria-description="Citation for case: Steagald v. United States"><i>Id.,</i> at 219</a></span>.</p>
<p>The homeowner's right to privacy is not atissue in this case. The Court does not reach the question whether the officer's unaided observations of Thompson's apartment constituted a search. If there was in fact a search, however, then Thompson had the right to object to the unlawful police surveillance of her apartment and the right to suppress any evidence disclosed by the search. Similarly, if the police had entered her home without a search warrant to arrest respondents, Thompson's own privacy interests would be violated and she could presumably bring an action under Rev. Stat. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>, or an action for trespass. Our cases establish, however, that respondents have no independent privacy right, the violation of which results in exclusion of evidence against them, unless they can establish a meaningful connection to Thompson's apartment.</p>
<p>The settled rule is that the requisite connection is an expectation of privacy that society recognizes as reasonable. <i>Katz</i> v.<i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 361</a></span> (1967) (Harlan, J., concurring). The application of that rule involves consideration of the kind of place in which the individual claims the privacy interest and what expectations of privacy are traditional and well recognized. <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Ibid.</a></span></i> I would expect that most, if not all, social guests legitimately expect that, in accordance with social custom, the homeowner will exercise her discretion to include or exclude others for the guests' benefit. As we recognized in <i>Minnesota</i> v. <i>Olson,</i> <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">495 U. S. 91</a></span> (1990), where these social expectations existas in the case of an overnight guestthey are sufficient to create a legitimate expectation of privacy, even in the absence of any property right to exclude others. In this respect, the dissent <span class="star-pagination">*102</span> must be correct that reasonable expectations of the owner are shared, to some extent, by the guest. This analysis suggests that, as a general rule, social guests will have an expectation of privacy in their host's home. That isnot the case before us, however.</p>
<p>In this case respondents have established nothing more than a fleeting and insubstantial connection with Thompson's home. For all that appears in the record, respondents used Thompson's house simply as a convenient processing station, their purpose involving nothing more than the mechanical act of chopping and packing a substance for distribution. There is no suggestion that respondents engaged in confidential communications with Thompson about their transaction. Respondents had not been to Thompson's apartment before, and they left it even before their arrest. The Minnesota Supreme Court, which overturned respondents' convictions, acknowledged that respondents could not be fairly characterized as Thompson's "guests." <span class="citation" data-id="9687539"><a href="/opinion/1833260/state-v-carter/#175" aria-description="Citation for case: State v. Carter">569 N. W. 2d 169, 175-176</a></span> (1997); see also <span class="citation" data-id="1691283"><a href="/opinion/1691283/state-v-carter/#698" aria-description="Citation for case: State v. Carter">545 N. W. 2d 695, 698</a></span> (Minn. Ct. App. 1996) (noting that Carter's only evidencethat he was there to package cocainewas inconsistent with his claim that "he was predominantly a social guest" in Thompson's apartment).</p>
<p>If respondents here had been visiting 20 homes, each for a minute or two, to drop off a bag of cocaine and were apprehended by a policeman wrongfully present in the 19th home; or if they had left the goods at a home where they were not staying and the police had seized the goods in their absence, we would have said that <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span></i> compels rejection of any privacy interest respondents might assert. So it does here, given that respondents have established no meaningful tie or connection to the owner, the owner's home, or the owner's expectation of privacy.</p>
<p>We cannot remain faithful to the underlying principle in <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span></i> without reversing in this case, and I am not persuaded that we need depart from it to protect the homeowner's <span class="star-pagination">*103</span> own privacy interests. Respondents have made no persuasive argument that we need to fashion a <i>per se</i> rule of home protection, with an automatic right for all in the home to invoke the exclusionary rule, in order to protect homeowners and their guests from unlawful police intrusion. With these observations, I join the Court's opinion.</p>
<p>Justice Breyer, concurring in the judgment.</p>
<p>I agree with Justice Ginsburg that respondents can claim the Fourth Amendment's protection. Petitioner, however, raises a second question, whether under the circumstances Officer Thielen's observation made "from a public area outside the curtilage of the residence" violated respondents' Fourth Amendment rights. See Pet. for Cert. i. In my view, it did not.</p>
<p>I would answer the question on the basis of the following factual assumptions, derived from the evidentiary record presented here: (1) On the evening of May 15, 1994, an anonymous individual approached Officer Thielen, telling him that he had just walked by a nearby apartment window through which he had seen some people bagging drugs; (2) the apartment in question was a garden apartment that was partly below ground level; (3) families frequently used the grassy area just outside the apartment's window for walking or for playing; (4) members of the public also used the area just outside the apartment's window to store bicycles; (5) in an effort to verify the tipster's information, Officer Thielen walked to a position about 1 to 1<sup>[1]</sup>20442 feet in front of the window; (6) Officer Thielen stood there for about 15 minutes looking down through a set of venetian blinds; (7) what he saw, namely, people putting white powder in bags, verified the account he had heard; and (8) he then used that information to help obtain a search warrant. See App. E-1 to E-3, E-9 to E-12, G-8 to G-9, G-12 to G-14, G-26, G-29 to G-30, G-32, G-39 to G-40, G-67 to G-71, I-2 to I-3.</p>
<p><span class="star-pagination">*104</span> The trial court concluded that persons then within Ms. Thompson's kitchen "did not have an expectation of privacy from the location where Officer Thielen made his observations . . . ," No. K9-94-0985 (Minn. Dist. Ct., Dec. 16, 1994), App. E-10 (unpublished), because Officer Thielen stood outside the apartment's "curtilage" when he made his observations, <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">id.</a></span></i> , at E-10 to E-12. And the Minnesota Supreme Court, while finding that Officer Thielen had violated the Fourth Amendment, did not challenge the trial court's curtilage determination; indeed, it assumed that Officer Thielen stood outside the apartment's curtilage. <span class="citation" data-id="9687539"><a href="/opinion/1833260/state-v-carter/#177" aria-description="Citation for case: State v. Carter">569 N. W. 2d 169, 177</a></span>, and n. 10 (1997) (stating "it is plausible that Thielen's presence just outside the apartment window was legitimate").</p>
<p>Officer Thielen, then, stood at a place used by the public and from which one could see through the window into the kitchen. The precautions that the apartment's dwellers took to maintain their privacy would have failed in respect to an ordinary passerby standing in that place. Given this Court's well-established case law, I cannot say that the officer engaged in what the Constitution forbids, namely, an "unreasonable search." See, <i>e. g., </i><i>Florida</i> v. <i>Riley,</i> <span class="citation" data-id="9431518"><a href="/opinion/112175/florida-v-riley/#448" aria-description="Citation for case: Florida v. Riley">488 U. S. 445, 448</a></span> (1989) (finding observation of greenhouse from helicopters in public airspace permissible, even though owners had enclosed greenhouse on two sides, relied on bushes blocking ground-level observations through remaining two sides, and covered 90% of roof); <i>California</i> v. <i>Ciraolo,</i> <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#209" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207, 209</a></span> (1986) (finding observation of backyard from plane in public airspace permissible despite 6-foot outer fence and 10-foot inner fence around backyard); cf. <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967).</p>
<p>The Minnesota Supreme Court reached a different conclusion in part because it believed that Officer Thielen had engaged in unusual activity, that he "climbed over some bushes, crouched down and placed his face 12 to 18 inches from the window," and in part because he saw into the apartment <span class="star-pagination">*105</span> through "a small gap" in blinds that were drawn. <span class="citation" data-id="9687539"><a href="/opinion/1833260/state-v-carter/#177" aria-description="Citation for case: State v. Carter">569 N. W. 2d, at 177-178</a></span>. But I would not here determine whether the crouching and climbing or "plac[ing] his face" makes a constitutional difference because the record before us does not contain support for those factual conclusions. That record indicates that Officer Thielen would not have needed to, and did not, climb over bushes or crouch. See App. G-12 to G-13, G-27 to G-30, G-43 to G-46 (Officer Thielen's testimony); <i><span class="citation" data-id="9687539"><a href="/opinion/1833260/state-v-carter/" aria-description="Citation for case: State v. Carter">id.,</a></span></i> at I-3 (photograph of apartment building). And even though the primary evidence consists of Officer Thielen's own testimony, who else could have known? Given the importance of factual nuance in this area of constitutional law, I would not determine the constitutional significance of factual assertions that the record denies. Cf. <i>Walters</i> v. <i>National Assn. of Radiation Survivors,</i> <span class="citation" data-id="9430161"><a href="/opinion/111504/walters-v-national-assn-of-radiation-survivors/#342" aria-description="Citation for case: Walters v. National Assn. of Radiation Survivors">473 U. S. 305, 342</a></span> (1985) (Brennan, J., dissenting) (citing <i>Brown</i>  v. <i>Chote,</i> <span class="citation" data-id="108770"><a href="/opinion/108770/brown-v-chote/#457" aria-description="Citation for case: Brown v. Chote">411 U. S. 452, 457</a></span> (1973)).</p>
<p>Neither can the matter turn upon "gaps" in drawn blinds. Whether there were holes in the blinds or they were simply pulled the "wrong way" makes no difference. One who lives in a basement apartment that fronts a publicly traveled street, or similar space, ordinarily understands the need for care lest a member of the public simply direct his gaze downward.</p>
<p>Putting the specific facts of this case aside, there is a benefit to an officer's decision to confirm an informant's tip by observing the allegedly illegal activity from a public vantage point. Indeed, there are reasons why Officer Thielen stood in a public place and looked through the apartment window. He had already received information that a crime was taking place in the apartment. He intended to apply for a warrant. He needed to verify the tipster's credibility. He might have done so in other ways, say, by seeking general information about the tipster's reputation and then obtaining a warrant and searching the apartment. But his chosen methodobserving the apartment from a public vantage pointwould <span class="star-pagination">*106</span> more likely have saved an innocent apartment dweller from a physically intrusive, though warrant-based, search if the constitutionally permissible observation revealed no illegal activity.</p>
<p>For these reasons, while agreeing with Justice Ginsburg, I also concur in the Court's judgment reversing the Minnesota Supreme Court.</p>
<p>Justice Ginsburg, with whom Justice Stevens and Justice Souter join, dissenting.</p>
<p>The Court's decision undermines not only the security of short-term guests, but also the security of the home resident herself. In my view, when a homeowner or lessee personally invites a guest into her home to share in a common endeavor, whether it be for conversation, to engage in leisure activities, or for business purposes licit or illicit, that guest should share his host's shelter against unreasonable searches and seizures.</p>
<p>I do not here propose restoration of the "legitimately on the premises" criterion stated in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 267</a></span> (1960), for the Court rejected that formulation in <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#142" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 142</a></span> (1978), as it did the "automatic standing rule" in <i>United States</i> v. <i>Salvucci,</i> <span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/#95" aria-description="Citation for case: United States v. Salvucci">448 U. S. 83, 95</a></span> (1980). First, the disposition I would reach in this case responds to the unique importance of the home the most essential bastion of privacy recognized by the law. See <i>United States</i> v. <i>Karo,</i> <span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/#714" aria-description="Citation for case: United States v. Karo">468 U. S. 705, 714</a></span> (1984) ("[P]rivate residences are places in which the individual normally expects privacy free of governmental intrusion not authorized by a warrant . . . . Our cases have not deviated from this basic Fourth Amendment principle."); <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#589" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 589</a></span> (1980) ("The Fourth Amendment protects the individual's privacy in a variety of settings. In none is the zone of privacy more clearly defined than when bounded by the unambiguous physical dimensions of an individual's home."). Second, even within the home itself, the <span class="star-pagination">*107</span> position to which I would adhere would not permit "a casual visitor who has never seen, or been permitted to visit, the basement of another's house to object to a search of the basement if the visitor happened to be in the kitchen of the house at the time of the search." <i>Rakas,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#142" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 142</a></span>. Further, I would here decide only the case of the homeowner who chooses to share the privacy of her home and her company with a guest, and would not reach classroom hypotheticals like the milkman or pizza deliverer.</p>
<p>My concern centers on an individual's choice to share her home and her associations there with persons she selects. Our decisions indicate that people have a reasonable expectation of privacy in their homes in part because they have the prerogative to exclude others. See <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#149" aria-description="Citation for case: Rakas v. Illinois"><i>id.,</i> at 149</a></span> (legitimate expectation of privacy turns in large part on ability to exclude others from place searched). The power to exclude implies the power to include. See, <i>e. g.,</i> Coombs, Shared Privacy and the Fourth Amendment, or the Rights of Relationships, <span class="citation no-link">75 Calif. L. Rev. 1593</span>, 1618 (1987) ("One reason we protect the legal right to exclude others is to empower the owner to choose to share his home or other property with his intimates."); Alschuler, Interpersonal Privacy and the Fourth Amendment, <span class="citation no-link">4 N. Ill. U. L. Rev. 1</span>, 13 (1983) ("[O]ne of the main rights attaching to property is the right to share its shelter, its comfort and its privacy with others."). Our Fourth Amendment decisions should reflect these complementary prerogatives.</p>
<p>A homedweller places her own privacy at risk, the Court's approach indicates, when she opens her home to others, uncertain whether the duration of their stay, their purpose, and their "acceptance into the household" will earn protection. <i>Ante,</i> at 90.<sup>[1]</sup> It remains textbook law that "[s]earches and seizures inside a home without a warrant are presumptively <span class="star-pagination">*108</span> unreasonable absent exigent circumstances." <i>Karo,</i> <span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/#714" aria-description="Citation for case: United States v. Karo">468 U. S., at 714-715</a></span>. The law in practice is less secure. Human frailty suggests that today's decision will tempt police to pry into private dwellings without warrant, to find evidence incriminating guests who do not rest there through the night. See Simien, The Interrelationship of the Scope of the Fourth Amendment and Standing to Object to Unreasonable Searches, <span class="citation no-link">41 Ark. L. Rev. 487</span>, 539 (1988) ("[I]f the police have no probable cause, they have everything to gain and nothing to lose if they search under circumstances where they know that at least one of the potential defendants will not have standing."). <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span></i> tolerates that temptation with respect to automobile searches. See Ashdown, The Fourth Amendment and the "Legitimate Expectation of Privacy," <span class="citation no-link">34 Vand. L. Rev. 1289</span>, 1321 (1981) (criticizing <i>Rakas</i> as "present[ing] a framework in which there may be nothing to lose and something to gain by the illegal search of a car that carries more than one occupant"); see also <i>Rakas,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#169" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 169</a></span> (White, J., dissenting) ("After this decision, police will have little to lose by unreasonably searching vehicles occupied by more than one person."). I see no impelling reason to extend this risk into the home. See <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 511</a></span> (1961) ("At the very core [of the Fourth Amendment] stands the right of a man to retreat into his own home and there be free from unreasonable governmental intrusion."). As I see it, people are not genuinely "secure in their . . . houses . . . against unreasonable searches and seizures," U. S. Const., Amdt. 4, if their invitations to others increase the risk of unwarranted governmental peering and prying into their dwelling places.</p>
<p>Through the host's invitation, the guest gains a reasonable expectation of privacy in the home. <i>Minnesota</i> v. <i>Olson,</i>  <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">495 U. S. 91</a></span> (1990), so held with respect to an overnight guest. The logic of that decision extends to shorter term guests as well. See 5 W. LaFave, Search and Seizure: A Treatise on the Fourth Amendment § 11.3(b), p. 137 (3d ed. <span class="star-pagination">*109</span> 1996) ("[I]t is fair to say that the <i><span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">Olson</a></span></i> decision lends considerable support to the claim that shorter-term guests also have standing."). Visiting the home of a friend, relative, or business associate, whatever the time of day, "serves functions recognized as valuable by society." <i>Olson,</i> <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/#98" aria-description="Citation for case: Minnesota v. Olson">495 U. S., at 98</a></span>. One need not remain overnight to anticipate privacy in another's home, "a place where [the guest] and his possessions will not be disturbed by anyone but his host and those his host allows inside." <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/#99" aria-description="Citation for case: Minnesota v. Olson"><i>Id.,</i> at 99</a></span>. In sum, when a homeowner chooses to share the privacy of her home and her company with a short-term guest, the twofold requirement "emerg[ing] from prior decisions" has been satisfied: Both host and guest "have exhibited an actual (subjective) expectation of privacy"; that "expectation [is] one [our] society is prepared to recognize as `reasonable.' " <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 361</a></span> (1967) (Harlan, J., concurring).<sup>[2]</sup></p>
<p>As the Solicitor General acknowledged, the illegality of the host-guest conduct, the fact that they were partners in crime, would not alter the analysis. See Tr. of Oral Arg. <span class="star-pagination">*110</span> 22-23. In <i><span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">Olson</a></span>,</i> for example, the guest whose security this Court's decision shielded stayed overnight while the police searched for him. <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/#93" aria-description="Citation for case: Minnesota v. Olson">495 U. S., at 93-94</a></span>. The Court held that the guest had Fourth Amendment protection against a warrantless arrest in his host's home despite the guest's involvement in grave crimes (first-degree murder, armed robbery, and assault). Other decisions have similarly sustained Fourth Amendment pleas despite the criminality of the defendants' activities. See<i>, e. g., </i><i>Payton,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York">445 U. S., at 583-603</a></span> (murder and armed robbery); <i>Katz,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#348" aria-description="Citation for case: Katz v. United States">389 U. S., at 348-359</a></span> (telephoning across state lines to place illegal wagers); <i>Silverman,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#508" aria-description="Citation for case: Silverman v. United States">365 U. S., at 508-512</a></span> (gambling offenses). Indeed, it must be this way. If the illegality of the activity made constitutional an otherwise unconstitutional search, such Fourth Amendment protection, reserved for the innocent only, would have little force in regulating police behavior toward either the innocent or the guilty.</p>
<p>Our leading decision in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> is key to my view of this case. There, we ruled that the Government violated the petitioner's Fourth Amendment rights when it electronically recorded him transmitting wagering information while he was inside a public telephone booth. <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States">389 U. S., at 353</a></span>. We were mindful that "the Fourth Amendment protects people, not places," <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States"><i>id.,</i> at 351</a></span>, and held that this electronic monitoring of a business call "violated the privacy upon which [the caller] justifiably relied while using the telephone booth," <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States"><i>id.,</i> at 353</a></span>. Our obligation to produce coherent results in this often visited area of the law requires us to inform our current expositions by benchmarks already established. As Justice Harlan explained in his dissent in <i>Poe</i> v. <i>Ullman,</i> <span class="citation" data-id="9422267"><a href="/opinion/106282/poe-v-ullman/#544" aria-description="Citation for case: Poe v. Ullman">367 U. S. 497, 544</a></span> (1961):</p>
<blockquote>"Each new claim to Constitutional protection must be considered against a background of Constitutional purposes, as they have been rationally perceived and historically developed<i>.</i> Though we exercise limited and <span class="star-pagination">*111</span> sharply restrained judgment, yet there is no `mechanical yardstick,' no `mechanical answer.' The decision of an apparently novel claim must depend on grounds which follow closely on well-accepted principles and criteria. The new decision must take `its place in relation to what went before and further [cut] a channel for what is to come.' " <i><span class="citation" data-id="9422267"><a href="/opinion/106282/poe-v-ullman/" aria-description="Citation for case: Poe v. Ullman">Ibid.</a></span></i> (quoting <i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#147" aria-description="Citation for case: Irvine v. California">347 U. S. 128, 147</a></span> (1954) (Frankfurter, J., dissenting)).</blockquote>
<p>The Court's decision in this case veers sharply from the path marked in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>.</i> I do not agree that we have a more reasonable expectation of privacy when we place a business call to a person's home from a public telephone booth on the side of the street, see <i>Katz,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States">389 U. S., at 353</a></span>, than when we actually enter that person's premises to engage in a common endeavor.<sup>[3]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*112</span> * * *</h2>
<p>For the reasons stated, I dissent from the Court's judgment, and would retain judicial surveillance over the warrantless searches today's decision allows.</p>
<h2>NOTES</h2>
<p>[*]   Together with <i>Minnesota</i> v. <i>Johns,</i> also on certiorari to the same court (see this Court's Rule 12.4).</p>
<p>[]   A brief of <i>amici curiae</i> urging reversal was filed for the State of Maryland et al. by <i>J. Joseph Curran, Jr.,</i> Attorney General of Maryland, <i>Annabelle L. Lisic,</i> Assistant Attorney General, <i>Alan G. Lance,</i> Attorney General of Idaho, and <i>Myrna A. I. Stahman,</i> Deputy Attorney General, joined by the Attorneys General for their respective States as follows: <i>Bill Pryor</i>  of Alabama, <i>Bruce M. Botelho</i> of Alaska, <i>Grant Woods</i> of Arizona, <i>Daniel E. Lungren</i> of California, <i>M. Jane Brady</i> of Delaware, <i>Thurbert E. Baker</i>  of Georgia, <i>Margery S. Bronster</i> of Hawaii, <i>Jeffrey A. Modisett</i> of Indiana, <i>Carla J. Stovall</i> of Kansas, <i>Richard P. Ieyoub</i> of Louisiana, <i>Scott Harshbarger</i> of Massachusetts, <i>Frank J. Kelley</i> of Michigan, <i>Joseph P. Mazurek</i>  of Montana, <i>Don Stenberg</i> of Nebraska, <i>Frankie Sue Del Papa</i> of Nevada, <i>Peter Verniero</i> of New Jersey, <i>Dennis C. Vacco</i> of New York, <i>Heidi Heitkamp</i> of North Dakota, <i>W. A. Drew Edmondson</i> of Oklahoma, <i>Jeffrey B. Pine</i> of Rhode Island, <i>Charles M. Condon</i> of South Carolina, <i>Jan Graham</i>  of Utah, <i>William H. Sorrell</i> of Vermont, and <i>Mark L. Earley</i> of Virginia.
</p>
<p><i>Tracey Maclin, Steven R. Shapiro,</i> and <i>Lisa B. Kemler</i> filed a brief for the American Civil Liberties Union et al.as <i>amici curiae</i> urging affirmance.</p>
<p>[1]   Justice Ginsburg's dissent, <i>post,</i> at 108-109, would render the operative language in <i>Minnesota</i> v. <i>Olson,</i> <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">495 U. S. 91</a></span> (1990), almost entirely superfluous. There, we explained the justification for extending Fourth Amendment protection to the overnight visitor: "Staying overnight in another's home is a longstanding social custom that serves functions recognized as valuable by society. . . . We are at our most vulnerable when we are asleep because we cannot monitor our own safety or the security of our belongings." <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/#98" aria-description="Citation for case: Minnesota v. Olson"><i>Id.,</i> at 98-99</a></span>. If any short-term business visitby a stranger entitles the visitor to share the Fourth Amendment protection of the leaseholder's home, the Court's explanation of its holding in <i><span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">Olson</a></span></i> was quite unnecessary.</p>
<p>[*]  Four others contained provisions proscribing general warrants, but unspecific as to the objects of the protection. See Va. Const. § 10 (1776); Del. Const., Art. I, § 6 (1776); Md. Const., Art. XXIII (1776); N. C. Const., Art. XI (1776).</p>
<p>[1]  Justice Kennedy seeks to cast doubt upon this historical evidence by the carefully generalized assertion that "scholars dispute [the] proper interpretation" of "the English authorities." <i>Post,</i> at 99-100 (concurring opinion). In support of this, he cites only a passage from <i>Payton</i> v. <i>New</i>  <i>York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980), which noted "a deep divergence among scholars" as to whether <i>Semayne's Case</i> accurately described one aspect of the common law of arrest. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#592" aria-description="Citation for case: Payton v. New York">445 U. S., at 592</a></span>. Unfortunately for purposes of its relevance here, that aspect had nothing whatever to do with whether one man's house was another man's castle, but pertained to whether "a constable had the authority to make [a] warrantless [arrest] in the home on mere suspicion of a felony." <i><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Ibid.</a></span></i> The "deep divergence" is a red herring.
</p>
<p>Justice Kennedy also attempts to distinguish <i>Semayne's Case</i> on the ground that it arose in "the context of civil process," and so may be "of limited application to enforcement of the criminal law." <i>Post,</i> at 100. But of course the distinction cuts in precisely the opposite direction from the one that would support Justice Kennedy's case: If one man's house is not another man's castle for purposes of serving civil process, it is <i>a fortiori</i> not so for purposes of resisting the government's agents in pursuit of crime. <i>Semayne's Case</i> itself makes clear that the King's rights are greater: "And all the said books, which prove, that when the process concerns the King, that the Sheriff may break the house, imply that at the suit of the party, the house may not be broken: otherwise the addition (at the suit of the King) would be frivolous." 5 Co. Rep. 92b, 77 Eng. Rep., at 198. See also <i><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">id.,</a></span></i> at 92a, 77 Eng. Rep., at 197 ("In every felony the King has interest, and where the King has interest the writ is <i>non omittas propter aliquam libertatem;</i> and so the liberty or privilege of a house doth not hold against the King"); <i><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">id.,</a></span></i> at 91b, 77 Eng. Rep., at 196 ("J. beats R. so as he is in danger of death, J. flies, and thereupon hue and cry is made, J. retreats into the house of T. they who pursue him, if the house be kept and defended with force . . . may lawfully break the house of T. for it is at the [King's] suit").</p>
<p>Finally, Justice Kennedy suggests that, whatever the Fourth Amendment meant at the time it was adopted, it does not matter, since "[t]he axiom that a man's home is his castle . . . has acquired over time a power and an independent significance justifying a more general assurance of personal security in one's home, an assurance which has become part of our constitutional tradition." <i>Post,</i> at 100. The issue in this case, however, is not "personal security in one's home," but personal security in someone else's home, as to which Justice Kennedy fails to identify <i>any</i> "constitutional tradition" other than the one I have describedleaving us with nothing but his personal assurance that some degree of protection higher than that (and higher than what the people have chosen to provide by law) is "justif[ied]."</p>
<p>[2]  The dissent asserts that I "undervalu[e]" the <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> Court's observation that "the Fourth Amendment protects people, not places." <i>Post,</i> at 111, n. 3, citing <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S., at 351</a></span>. That catchy slogan would be a devastating response to someone who maintained that <i>a location</i> could claim protection of the Fourth Amendmentsomeone who asserted, perhaps, that "primeval forests have rights, too." Cf. Stone, Should Trees Have Standing?Toward Legal Rights for Natural Objects, <span class="citation no-link">45 S. Cal. L. Rev. 450</span> (1972). The issue here, however, is the less druidical one of whether respondents (who are people) have suffered a violation of <i>their</i> right "to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures." U. S. Const., Amdt. 4. That the Fourth Amendment does not protect places is simply unresponsive to the question whether the Fourth Amendment protects people in other people's homes. In saying this, I do not, as the dissent claims, clash with "the <i>leitmotif</i> of Justice Harlan's concurring opinion" in <i>Katz, post,</i> at 111, n. 3; <i>au contraire</i>  (or, to be more Wagnerian, <i>im Gegenteil</i> ), in this regard I am entirely in harmony with that opinion, and it is the dissent that sings from another opera. See <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S., at 361</a></span> (Harlan, J., concurring): "As the Court's opinion states, `the Fourth Amendment protects people, not places.' The question, however, is what protection it affords to those people. Generally, as here, the answer to that question requires reference to a `place.' "</p>
<p>[3]  At oral argument, counsel for petitioner informed the Court that the lessee of the apartment was charged, tried, and convicted of the same crimes as respondents. Tr. of Oral Arg. 10-11.</p>
<p>[1]  In his concurring opinion, Justice Kennedy maintains that respondents here lacked "an expectation of privacy that society recognizes as reasonable," <i>ante,</i> at 101, because they "established nothing more than a fleeting and insubstantial connection" with the host's home, <i>ante,</i> at 102. As the Minnesota Supreme Court reported, however, the stipulated facts showed that respondents were inside the apartment with the host's permission, remained inside for at least 2½ hours, and, during that time, engaged in concert with the host in a collaborative venture. See <span class="citation" data-id="9687539"><a href="/opinion/1833260/state-v-carter/#175" aria-description="Citation for case: State v. Carter">569 N. W. 2d 169, 175-176</a></span> (1997). These stipulated factswhich scarcely resemble a stop of a minute or two at the 19th of 20 homes to drop off a packet, see <i>ante,</i> at 102securely demonstrate that the host intended to share her privacy with respondents, and that respondents, therefore, had entered into the homeland of Fourth Amendment protection. While I agree with the Minnesota Supreme Court that, under the rule settled since <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> the reasonableness of the expectation of privacy controls, not the visitor's status as social guest, invitee, licensee, or business partner, <span class="citation" data-id="9687539"><a href="/opinion/1833260/state-v-carter/#176" aria-description="Citation for case: State v. Carter">569 N. W. 2d, at 176</a></span>, I think it noteworthy that five Members of the Court would place under the Fourth Amendment's shield, at least, "almost all social guests," <i>ante,</i> at 99 (Kennedy, J., concurring).</p>
<p>[1]  Justice Scalia's lively concurring opinion deplores our adherence to <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>.</i> In suggesting that we have elevated Justice Harlan's concurring opinion in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> to first place, see <i>ante,</i> at 97, Justice Scalia undervalues the clear opinion of the Court that "the Fourth Amendment protects people, not places," <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S., at 351</a></span>. That core understanding is the <i>leitmotif</i> of Justice Harlan's concurring opinion. One cannot avoid a strong sense of d<i>éjà vu</i> on reading Justice Scalia's elaboration. It so vividly recalls the opinion of Justice Black <i>in dissent</i> in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>.</i> See <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#365" aria-description="Citation for case: Katz v. United States">389 U. S., at 365</a></span> (Black, J., dissenting) ("While I realize that an argument based on the meaning of words lacks the scope, and no doubt the appeal, of broad policy discussions and philosophical discourses . . . , for me the language of the Amendment is the crucial place to look."); <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#373" aria-description="Citation for case: Katz v. United States"><i>id.,</i> at 373</a></span> ("[B]y arbitrarily substituting the Court's language . . . for the Constitution's language the Court has made the Fourth Amendment its vehicle for holding all laws violative of the Constitution which offend the Court's broadest concept of privacy."); <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">ibid.</a></span></i> ("I will not distort the words of the Amendment in order to `keep the Constitution up to date' or `to bring it into harmony with the times.' "). Justice Scalia relies on what he deems "clear text," <i>ante,</i> at 97, to argue that the Fourth Amendment protects people from searches only in the places where they live, <i>ante,</i> at 96. Again, as Justice Stewart emphasized in the majority opinion in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> which <i>stare decisis</i> and reason require us to follow, "the Fourth Amendment protects people, not places." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S., at 351</a></span>.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Minnesota v. Dickerson.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Minnesota v. Dickerson"
type: case
citation: "508 U.S. 366 (1993)"
parallel_cite: "113 S. Ct. 2130; 124 L. Ed. 2d 334"
neutral_cite: 1993 U.S. LEXIS 4018
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1993
date_decided: 1993-06-07
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1993-06-07
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Minnesota v. Dickerson
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112873/minnesota-v-dickerson/"
  cluster_id: 112873
  opinion_id: 9432823
  identity_checked: true
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Key — Progeny / Refinement"
related: ["[[Terry v. Ohio]]", "[[Horton v. California]]", "[[Arizona v. Hicks]]"]
aliases: []
tags: ["case", "fourth-amendment", "plain-feel", "plain-view", "terry", "frisk"]
holding: "Plain-feel corollary: contraband whose identity is immediately apparent by touch during a lawful *Terry* frisk may be seized — but not where the officer squeezed/manipulated it to ID it."
lake:
  record_id: Minnesota v. Dickerson
  status: verified
  projected_at: 2026-07-06
---

# Minnesota v. Dickerson

*508 U.S. 366 (1993)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers conducting a *[[Terry v. Ohio|Terry]]* stop frisked Dickerson. The officer felt a small lump in his jacket pocket and, after squeezing, sliding, and otherwise manipulating it, concluded it was crack cocaine and seized it. He had already satisfied himself that the object was not a weapon before manipulating it.

## Issue
Whether contraband detected through the sense of touch during a lawful *[[Terry v. Ohio|Terry]]* frisk may be seized without a warrant.

## Rule
Yes, within limits — a "plain-feel" corollary to the [[Plain View Doctrine|plain-view doctrine]]: "If a police officer lawfully pats down a suspect's outer clothing and feels an object whose contour or mass makes its identity immediately apparent, there has been no invasion of the suspect's privacy beyond that already authorized by the officer's search for weapons; if the object is contraband, its warrantless seizure would be justified by the same practical considerations that inhere in the plain-view context." — 508 U.S. at 375-376. ^pin-375

## Application
Here the incriminating character of the lump was not immediately apparent: the officer determined it was contraband only after squeezing, sliding, and otherwise manipulating the pocket's contents — continued exploration after he already knew the object was not a weapon. Because that manipulation went beyond the scope of a lawful protective frisk, the seizure was not justified by the plain-feel rule.

## Conclusion
Affirmed; the seizure was invalid because the officer exceeded the bounds of a *[[Terry v. Ohio|Terry]]* frisk.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Dickerson* extends the plain-view seizure logic ([[Horton v. California]]; [[Arizona v. Hicks]]) to tactile discoveries during a lawful [[Terry v. Ohio]] frisk.

## Appears on
- [[Plain View Doctrine]] — *Key — Progeny / Refinement*

## Sources
- *Minnesota v. Dickerson*, 508 U.S. 366 (1993) — https://www.courtlistener.com/opinion/112873/minnesota-v-dickerson/ — pinpoint: 375-376.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7d9b610531cc3d34", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Minnesota v. Dickerson"}, "payload": {"all": [{"cite": "508 U.S. 366", "page": "366", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "508"}, {"cite": "113 S. Ct. 2130", "page": "2130", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "113"}, {"cite": "124 L. Ed. 2d 334", "page": "334", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "124"}, {"cite": "1993 U.S. LEXIS 4018", "page": "4018", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1993"}], "display": "508 U.S. 366", "official": {"cite": "508 U.S. 366", "page": "366", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "508"}, "official_selection_present": true, "record_id": "Minnesota v. Dickerson"}}
{"assertion_id": "bbbd99798a4062b0", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-375", "record_id": "Minnesota v. Dickerson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-375", "pinpoint_status": "slip-only", "quote": "--- # Minnesota v. Dickerson *508 U.S. 366 (1993)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers conducting a *Terry* stop frisked Dickerson. The officer felt a small lump in his jacket pocket and, after squeezing, sliding, and otherwise manipulating it, concluded it was crack cocaine and seized it. He had already satisfied himself that the object was not a weapon before manipulating it. ## Issue Whether contraband detected through the sense of touch during a lawful *Terry* frisk may be seized without a warrant. ## Rule Yes, within limits — a", "quote_fidelity": "mismatch", "record_id": "Minnesota v. Dickerson", "star_marker": null}}
{"assertion_id": "e328541b263ca3c8", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Minnesota v. Dickerson"}, "payload": {"as_of_content": "1993-06-07", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Minnesota v. Dickerson", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Minnesota v. Dickerson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Minnesota v. Dickerson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Minnesota v. Dickerson",
    "case_name_short": "Dickerson",
    "case_name_full": "Minnesota v. Dickerson",
    "input_case_name": "Minnesota v. Dickerson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1993-06-07",
    "year": 1993,
    "docket": null,
    "cluster_id": 112873,
    "lead_opinion_id": 9432823,
    "sibling_ids": [
      112873,
      9432823,
      9432824,
      9432825
    ],
    "absolute_url": "/opinion/112873/minnesota-v-dickerson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "508 U.S. 366",
      "volume": "508",
      "reporter": "U.S.",
      "page": "366",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "113 S. Ct. 2130",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "2130",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 L. Ed. 2d 334",
        "volume": "124",
        "reporter": "L. Ed. 2d",
        "page": "334",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1993 U.S. LEXIS 4018",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "4018",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "508 U.S. 366",
        "volume": "508",
        "reporter": "U.S.",
        "page": "366",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 S. Ct. 2130",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "2130",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 L. Ed. 2d 334",
        "volume": "124",
        "reporter": "L. Ed. 2d",
        "page": "334",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 U.S. LEXIS 4018",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "4018",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "508 U.S. 366",
    "official_selection": {
      "court_class": "scotus",
      "selected": "508 U.S. 366",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-375",
      "page": null,
      "quote": "--- # Minnesota v. Dickerson *508 U.S. 366 (1993)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers conducting a *Terry* stop frisked Dickerson. The officer felt a small lump in his jacket pocket and, after squeezing, sliding, and otherwise manipulating it, concluded it was crack cocaine and seized it. He had already satisfied himself that the object was not a weapon before manipulating it. ## Issue Whether contraband detected through the sense of touch during a lawful *Terry* frisk may be seized without a warrant. ## Rule Yes, within limits \u2014 a",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1993-06-07",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Minnesota v. Dickerson",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Ivarson",
          "cluster_id": 10780539,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Louisiana v. K.B.",
          "cluster_id": 10581696,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Torres",
          "cluster_id": 9381469,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 9352593,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6620965,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6478743,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bock (A169480)",
          "cluster_id": 10134134,
          "cite": [
            "310 Or. App. 329",
            "485 P.3d 931"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Garrett",
          "cluster_id": 4552162,
          "cite": [
            "2018 Ohio 4530",
            "123 N.E.3d 327"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Spencer v. Kemna",
          "cluster_id": 118176,
          "cite": [
            "140 L. Ed. 2d 43",
            "118 S. Ct. 978",
            "523 U.S. 1",
            "1998 U.S. LEXIS 1597"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
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
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. State",
          "cluster_id": 2466562,
          "cite": [
            "973 S.W.2d 954",
            "1998 Tex. Crim. App. LEXIS 87",
            "1998 WL 375422"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estrada v. State",
          "cluster_id": 1397881,
          "cite": [
            "154 S.W.3d 604",
            "2005 Tex. Crim. App. LEXIS 112",
            "2005 WL 156830"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richards v. Wisconsin",
          "cluster_id": 118103,
          "cite": [
            "137 L. Ed. 2d 615",
            "117 S. Ct. 1416",
            "520 U.S. 385",
            "1997 U.S. LEXIS 2794"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neal v. State",
          "cluster_id": 2347917,
          "cite": [
            "256 S.W.3d 264",
            "2008 Tex. Crim. App. LEXIS 754",
            "2008 WL 2437667"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
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
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
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
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ehly",
          "cluster_id": 1448102,
          "cite": [
            "854 P.2d 421",
            "317 Or. 66",
            "1993 Ore. LEXIS 91"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. State",
          "cluster_id": 1796535,
          "cite": [
            "182 S.W.3d 899",
            "2005 Tex. Crim. App. LEXIS 2038",
            "2005 WL 3310462"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walter v. State",
          "cluster_id": 1755500,
          "cite": [
            "28 S.W.3d 538",
            "2000 Tex. Crim. App. LEXIS 84",
            "2000 WL 1348504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Windell Clay",
          "cluster_id": 77667,
          "cite": [
            "483 F.3d 739",
            "2007 U.S. App. LEXIS 7616",
            "2007 WL 968837"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Petitioner: Wesley Richard DePriest v. Respondent: The People of the State of Colorado.",
          "cluster_id": 10018912,
          "cite": [
            "2021 CO 40"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
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
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ross",
          "cluster_id": 1060457,
          "cite": [
            "49 S.W.3d 833",
            "2001 Tenn. LEXIS 563",
            "2001 WL 760100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Sorenson",
          "cluster_id": 2167114,
          "cite": [
            "752 N.E.2d 1078",
            "196 Ill. 2d 425",
            "256 Ill. Dec. 836",
            "2001 Ill. LEXIS 776"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walczyk v. Rio",
          "cluster_id": 2704,
          "cite": [
            "496 F.3d 139",
            "2007 WL 2199005"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
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
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Martin Gonzalez Munoz",
          "cluster_id": 756462,
          "cite": [
            "150 F.3d 401"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baker v. Monroe Township",
          "cluster_id": 692283,
          "cite": [
            "50 F.3d 1186",
            "1995 U.S. App. LEXIS 10075"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Prost v. Anderson",
          "cluster_id": 205239,
          "cite": [
            "636 F.3d 578",
            "2011 U.S. App. LEXIS 3461",
            "2011 WL 590334"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "El Bey v. Roop",
          "cluster_id": 1189624,
          "cite": [
            "530 F.3d 407",
            "2008 U.S. App. LEXIS 13776",
            "2008 WL 2572935"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Caballes",
          "cluster_id": 2192166,
          "cite": [
            "851 N.E.2d 26",
            "221 Ill. 2d 282",
            "303 Ill. Dec. 128",
            "2006 Ill. LEXIS 625"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Garvin",
          "cluster_id": 2592928,
          "cite": [
            "207 P.3d 1266"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jones",
          "cluster_id": 2058953,
          "cite": [
            "830 N.E.2d 541",
            "215 Ill. 2d 261",
            "294 Ill. Dec. 129",
            "2005 Ill. LEXIS 632"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnesota v. Dickerson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112873 OR 9432823 OR 9432824 OR 9432825) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTAzMjczNjAwMDAwJnM9NDQyMDMyNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112873+OR+9432823+OR+9432824+OR+9432825%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112873 OR 9432823 OR 9432824 OR 9432825)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTEmcz03NzY5MDEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112873+OR+9432823+OR+9432824+OR+9432825%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112873 OR 9432823 OR 9432824 OR 9432825)",
        "reviewed": 61,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 61,
        "triage_read": 2,
        "triage_snippet_classified": 59
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112873 OR 9432823 OR 9432824 OR 9432825)",
    "indexed_citing_opinions": 1630,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112873,
        "count": 1432,
        "count_source": "search"
      },
      {
        "opinion_id": 9432823,
        "count": 224,
        "count_source": "search"
      },
      {
        "opinion_id": 9432824,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9432825,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2670,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/minnesota-v-dickerson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4MzU2NiZzPTk1MTQwMzcmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28112873+OR+9432823+OR+9432824+OR+9432825%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112873,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 111013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 111302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 111834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 112448,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 112608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 112795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 112814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 490903,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 525639,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 560550,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 568550,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 586858,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 1173996,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 1251064,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 1281913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 1293458,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 1350157,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 1369743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 1527482,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 1865816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112873,
        "cited_id": 2001156,
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
    "date_created": "2026-07-05T13:58:41Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:58:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:58:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:02:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:58:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Minnesota v. Dickerson

```
<opinion type="majority">
<author id="b416-7">Justice White</author>
<p id="A4jd">delivered the opinion of the Court.</p>
<p id="b416-8">In this ease, we consider whether the Fourth Amendment permits the seizure of contraband detected through a police officer’s sense of touch during a protective patdown search.</p>
<p id="b416-9">I</p>
<p id="b416-10">On the evening of November 9,1989, two Minneapolis police officers were patrolling an area on the city’s north side in a marked squad car. At about 8:15 p.m., one of the officers observed respondent leaving a 12-unit apartment building on Morgan Avenue North. The officer, having previously responded to complaints of drug sales in the building’s hallways and having executed several search warrants on the premises, considered the building to be a notorious “crack house.” According to testimony credited by the trial court, respondent began walking toward the police but, upon spot<page-number citation-index="1" label="369">*369</page-number>ting the squad ear and making eye contact with one of the officers, abruptly halted and began walking in the opposite direction. His suspicion aroused, this officer watched as respondent turned and entered an alley on the other side of the apartment building. Based upon respondent’s seemingly evasive actions and the fact that he had just left a building known for cocaine traffic, the officers decided to stop respondent and investigate further.</p>
<p id="b417-4">The officers pulled their squad car into the alley and ordered respondent to stop and submit to a patdown search. The search revealed no weapons, but the officer conducting the search did take an interest in a small lump in respondent’s nylon jacket. The officer later testified:</p>
<blockquote id="b417-5">“[A]s I pat-searched the front of his body, I felt a lump, a small lump, in the front pocket. I examined it with my fingers and it slid and it felt to be a lump of crack cocaine in cellophane.” Tr. 9 (Feb. 20,1990).</blockquote>
<p id="b417-6">The officer then reached into respondent’s pocket and retrieved a small plastic bag containing one fifth of one gram of crack cocaine. Respondent was arrested and charged in Hennepin County District Court with possession of a controlled substance.</p>
<p id="b417-7">Before trial, respondent moved to suppress the cocaine. The trial court first concluded that the officers were justified under <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), in stopping respondent to investigate whether he might be engaged in criminal activity. The court further found that the officers were justified in frisking respondent to ensure that he was not carrying a weapon. Finally, analogizing to the “plain-view” doctrine, under which officers may make a warrantless seizure of contraband found in plain view during a lawful search for other items, the trial court ruled that the officers’ seizure of the cocaine did not violate the Fourth Amendment:</p>
<blockquote id="b417-8">“To this Court there is no distinction as to which sensory perception the officer uses to conclude that the ma<page-number citation-index="1" label="370">*370</page-number>terial is contraband. An experienced officer may rely upon his sense of smell in DWI stops or in recognizing the smell of burning marijuana in an automobile. The sound of a shotgun being racked would clearly support certain reactions by an officer. The sense of touch, grounded in experience and training, is as reliable as perceptions drawn from other senses. ‘Plain feel/ therefore, is no different than plain view and will equally support the seizure here.” App. to Pet. for Cert. C-5.</blockquote>
<p id="b418-5">His suppression motion having failed, respondent proceeded to trial and was found guilty.</p>
<p id="b418-6">On appeal, the Minnesota Court of Appeals reversed. The court agreed with the trial court that the investigative stop and protective patdown search of respondent were lawful under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>because the officers had a reasonable belief based on specific and articulable facts that respondent was engaged in criminal behavior and that he might be armed and dangerous. The court concluded, however, that the officers had overstepped the bounds allowed by <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>in seizing the cocaine. In doing so, the Court of Appeals “deeline[d] to adopt the plain feel exception” to the warrant requirement. <span class="citation" data-id="1865816"><a href="/opinion/1865816/state-v-dickerson/#466" aria-description="Citation for case: State v. Dickerson">469 N. W. 2d 462, 466</a></span> (1991).</p>
<p id="b418-7">The Minnesota Supreme Court affirmed. Like the Court of Appeals, the State Supreme Court held that both the stop and the frisk of respondent were valid under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>but found the seizure of the cocaine to be unconstitutional. The court expressly refused “to extend the plain view doctrine to the sense of touch” on the grounds that “the sense of touch is inherently less immediate and less reliable than the sense of sight” and that “the sense of touch is far more intrusive into the personal privacy that is at the core of the [Fjourth [AJmendment.” <span class="citation multiple-matches"><a href="/c/N.%20W.%202d/481/840/">481 N. W. 2d 840</a></span>, 845 (1992). The court thus appeared to adopt a categorical rule barring the seizure of any contraband detected by an officer through the sense of touch during a patdown search for weapons. The court further noted that “[e]ven if we recognized a ‘plain feel’ ex<page-number citation-index="1" label="371">*371</page-number>ception, the search in this case would not qualify” because “[t]he pat search of the defendant went far beyond what is permissible under <em>Terry.” Id., </em>at 843, 844, n. 1. As the State Supreme Court read the record, the officer conducting the search ascertained that the lump in respondent’s jacket was contraband only after probing and investigating what he certainly knew was not a weapon. See <em>id., </em>at 844.</p>
<p id="b419-5">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./506/814/">506 U. S. 814</a></span> (1992), to resolve a conflict among the state and federal courts over whether contraband detected through the sense of touch during a patdown search may be admitted into evidence.<footnotemark>1</footnotemark> We now affirm.<footnotemark>2</footnotemark></p>
<p id="b420-4"><page-number citation-index="1" label="372">*372</page-number>II</p>
<p id="b420-5">A</p>
<p id="b420-6">The Fourth Amendment, made applicable to the States by way of the Fourteenth Amendment, <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), guarantees “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures.” Time and again, this Court has observed that searches and seizures “ ‘conducted outside the judicial process, without prior approval by judge or magistrate, are <em>per se </em>unreasonable under the Fourth Amendment — subject only to a few specifically established and well delineated exceptions/” <em>Thompson </em>v. <em>Louisiana, </em><span class="citation" data-id="111282"><a href="/opinion/111282/thompson-v-louisiana/#19" aria-description="Citation for case: Thompson v. Louisiana">469 U. S. 17, 19-20</a></span> (1984) <em>(per curiam) </em>(quoting <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (1967) (footnotes omitted)); <em>Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#390" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 390</a></span> (1978); see also <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#701" aria-description="Citation for case: United States v. Place">462 U. S. 696, 701</a></span> (1983). One such exception was <page-number citation-index="1" label="373">*373</page-number>recognized in <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), which held that “where a police officer observes unusual conduct which leads him reasonably to conclude in light of his experience that criminal activity may be afoot . . . ,” the officer may briefly stop the suspicious person and make “reasonable inquiries” aimed at confirming or dispelling his suspicions. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 30</a></span>; see also <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#145" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 145-146</a></span> (1972).</p>
<p id="b421-5"><em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>further held that “[w]hen an officer is justified in believing that the individual whose suspicious behavior he is investigating at close range is armed and presently dangerous to the officer or to others,” the officer may conduct a patdown search “to determine whether the person is in fact carrying a weapon.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 24</a></span>. “The purpose of this limited search is not to discover evidence of crime, but to allow the officer to pursue his investigation without fear of violence . . . .” <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams"><em>Adams, supra, </em>at 146</a></span>. Rather, a protective search — permitted without a warrant and on the basis of reasonable suspicion less than probable cause — must be strictly “limited to that which is necessary for the discovery of weapons which might be used to harm the officer or others nearby.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#26" aria-description="Citation for case: Terry v. Ohio"><em>Terry, supra, </em>at 26</a></span>; see also <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1049" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1049</a></span>, and 1052, n. 16 (1983); <em>Ybarra </em>v. <em>Illinois, </em><span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/#93" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85, 93-94</a></span> (1979). If the protective search goes beyond what is necessary to determine if the suspect is armed, it is no longer valid under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>and its fruits will be suppressed. <em>Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#65" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 65-66</a></span> (1968).</p>
<p id="b421-6">These principles were settled 25 years ago when, on the same day, the Court announced its decisions in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>and <em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">Sibron</a></span>. </em>The question presented today is whether police officers may seize nonthreatening contraband detected during a protective patdown search of the sort permitted by <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>. </em>We think the answer is clearly that they may, so long as the officers’ search stays within the bounds marked by <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</em></p>
<p id="b422-4"><page-number citation-index="1" label="374">*374</page-number>B</p>
<p id="b422-5">We have already held that police officers, at least under certain circumstances, may seize contraband detected during the lawful execution of a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>search. In <em>Michigan </em>v. <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long, supra,</a></span> </em>for example, police approached a man who had driven his car into a ditch and who appeared to be under the influence of some intoxicant. As the man moved to reenter the car from the roadside, police spotted a knife on the floorboard. The officers stopped the man, subjected him to a patdown search, and then inspected the interior of the vehicle for other weapons. During the search of the passenger compartment, the police discovered an open pouch containing marijuana and seized it. This Court upheld the validity of the search and seizure under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>. </em>The Court held first that, in the context of a roadside encounter, where police have reasonable suspicion based on specific and articulable facts to believe that a driver may be armed and dangerous, they may conduct a protective search for weapons not only of the driver’s person but also of the passenger compartment of the automobile. <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1049" aria-description="Citation for case: Michigan v. Long">463 U. S., at 1049</a></span>. Of course, the protective search of the vehicle, being justified solely by the danger that weapons stored there could be used against the officers or bystanders, must be “limited to those areas in which a weapon may be placed or hidden.” <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Ibid.</a></span> </em>The Court then held: “If, while conducting a legitimate <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>search of the interior of the automobile, the officer should, as here, dis-. cover contraband other than weapons, he clearly cannot be required to ignore the contraband, and the Fourth Amendment does not require its suppression in such circumstances.” <em>Id., </em>at 1050; accord, <em>Sibron, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#69" aria-description="Citation for case: Sibron v. New York">392 U. S., at 69-70</a></span> (White, J., concurring); <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#79" aria-description="Citation for case: Sibron v. New York"><em>id., </em>at 79</a></span> (Harlan, J., concurring in result).</p>
<p id="b422-6">The Court in <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span> </em>justified this latter holding by reference to our cases under the “plain-view” doctrine. See <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1050" aria-description="Citation for case: Michigan v. Long"><em>Long, supra, </em>at 1050</a></span>; see also <em>United States </em>v. <em>Hensley, </em><span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/#235" aria-description="Citation for case: United States v. Hensley">469 U. S. 221, 235</a></span> (1985) (upholding plain-view seizure in context <page-number citation-index="1" label="375">*375</page-number>of <em>Terry </em>stop). Under that doctrine, if police are lawfully in a position from which they view an object, if its incriminating character is immediately apparent, and if the officers have a lawful right of access to the object, they may seize it without a warrant. See <em>Horton </em>v. <em>California, </em><span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#136" aria-description="Citation for case: Horton v. California">496 U. S. 128, 136-137</a></span> (1990); <em>Texas </em>v. <em>Brown, </em><span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#739" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 739</a></span> (1983) (plurality opinion). If, however, the police lack probable cause to believe that an object in plain view is contraband without conducting some further search of the <em>object </em>— i. <em>e., </em>if “its incriminating character [is not] ‘immediately apparent,’” <em><span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/" aria-description="Citation for case: Horton v. California">Horton, supra,</a></span> </em>at 136—the plain-view doctrine cannot justify its seizure. <em>Arizona </em>v. <em>Hicks, </em><span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/" aria-description="Citation for case: Arizona v. Hicks">480 U. S. 321</a></span> (1987).</p>
<p id="b423-5">We think that this doctrine has an obvious application by analogy to cases in which an officer discovers contraband through the sense of touch during an otherwise lawful search. The rationale of the plain-view doctrine is that if contraband is left in open View and is observed by a police officer from a lawful vantage point, there has been no invasion of a legitimate expectation of privacy and thus no “search” within the meaning of the Fourth Amendment — or at least no search independent of the initial intrusion that gave the officers their vantage point. See <em>Illinois </em>v. <em>Andreas, </em><span class="citation" data-id="9429344"><a href="/opinion/111013/illinois-v-andreas/#771" aria-description="Citation for case: Illinois v. Andreas">463 U. S. 765, 771</a></span> (1983); <em>Texas </em>v. <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#740" aria-description="Citation for case: Texas v. Brown"><em>Brown, supra, </em>at 740</a></span>. The warrantless seizure of contraband that presents itself in this manner is deemed justified by the realization that resort to a neutral magistrate under such circumstances would often be impracticable and would do little to promote the objectives of the Fourth Amendment. See <span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#326" aria-description="Citation for case: Arizona v. Hicks"><em>Hicks, supra, </em>at 326-327</a></span>; <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#467" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 467-468, 469-470</a></span> (1971) (opinion of Stewart, J.). The same can be said of tactile discoveries of contraband. If a police officer lawfully pats down a suspect’s outer clothing and feels an object whose contour or mass makes its identity immediately apparent, there has been no invasion of the suspect’s privacy beyond that already authorized by the officer’s search for weapons; if the object is contraband, its warrantless seizure <page-number citation-index="1" label="376">*376</page-number>would be justified by the same practical considerations that inhere in the plain-view context.<footnotemark>3</footnotemark></p>
<p id="b424-5">The Minnesota Supreme Court rejected an analogy to the plain-view doctrine on two grounds: first, its belief that “the sense of touch is inherently less immediate and less reliable than the sense of sight,” and second, that “the sense of touch is far more intrusive into the personal privacy that is at the core of the [Fjourth [Ajmendment.” 481 N. W. 2d, at 845. We have a somewhat different view. First, <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>itself demonstrates that the sense of touch is capable of revealing the nature of an object with sufficient reliability to support a seizure. The very premise of <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>after all, is that officers will be able to detect the presence of weapons through the sense of touch and <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>upheld precisely such a seizure. Even if it were true that the sense of touch is generally less reliable than the sense of sight, that only suggests that officers will less often be able to justify seizures of unseen contraband. Regardless of whether the officer detects the contraband by sight or by touch, however, the Fourth Amendment’s requirement that the officer have probable cause to believe that the item is contraband before seizing it ensures against excessively speculative seizures.<footnotemark>4</footnotemark> The <page-number citation-index="1" label="377">*377</page-number>court’s second concern — that touch is more intrusive into privacy than is sight — is inapposite in light of the fact that the intrusion the court fears has already been authorized by the lawful search for weapons. The seizure of an item whose identity is already known occasions no further invasion of privacy. See <em>Soldal </em>v. <em>Cook County, </em><span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/#66" aria-description="Citation for case: Soldal v. Cook County">506 U. S. 56, 66</a></span> (1992); <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#141" aria-description="Citation for case: Horton v. California"><em>Horton, supra, </em>at 141</a></span>; <em>United States </em>v. <em>Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#120" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 120</a></span> (1984). Accordingly, the suspect’s privacy interests are not advanced by a categorical rule barring the seizure of contraband plainly detected through the sense of touch.</p>
<p id="b425-5">Ill</p>
<p id="b425-6">It remains to apply these principles to the facts of this case. Respondent has not challenged the finding made by the trial court and affirmed by both the Court of Appeals and the State Supreme Court that the police were justified under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>in stopping him and frisking him for weapons. Thus, the dispositive question before this Court is whether the officer who conducted the search was acting within the lawful bounds marked by <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>at the time he gained probable cause to believe that the lump in respondent’s jacket was contraband. The State District Court did not make precise findings on this point, instead finding simply that the officer, after feeling “a small, hard object wrapped in plastic” in respondent’s pocket, “formed the opinion that the object. . . was crack . . . cocaine.” App. to Pet. for Cert. C-2. The <page-number citation-index="1" label="378">*378</page-number>District Court also noted that the officer made “no claim that he suspected this object to be a weapon,” <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">id.,</a></span> </em>at C-5, a finding affirmed on appeal, see <span class="citation" data-id="1865816"><a href="/opinion/1865816/state-v-dickerson/#464" aria-description="Citation for case: State v. Dickerson">469 N. W. 2d, at 464</a></span> (the officer “never thought the lump was a weapon”). The Minnesota Supreme Court, after “a close examination of the record,” held that the officer’s own testimony “belies any notion that he ‘immediately’” recognized the lump as crack cocaine. See 481 N. W. 2d, at 844. Rather, the court concluded, the officer determined that the lump was contraband only after “squeezing, sliding and otherwise manipulating the contents of the defendant’s pocket” — a pocket which the officer already knew contained no weapon. <em>Ibid.</em></p>
<p id="b426-5">Under the State Supreme Court’s interpretation of the record before it, it is clear that the court was correct in holding that the police officer in this ease overstepped the bounds of the “strictly circumscribed” search for weapons allowed under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>. </em>See <em>Terry, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#26" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 26</a></span>. Where, as here, “an officer who is executing a valid search for one item seizes a different item,” this Court rightly “has been sensitive to the danger . . . that officers will enlarge a specific authorization, furnished by a warrant or an exigency, into the equivalent of a general warrant to rummage and seize at will.” <em>Texas </em>v. <em>Brown, </em><span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#748" aria-description="Citation for case: Texas v. Brown">460 U. S., at 748</a></span> (Stevens, J., concurring in judgment). Here, the officer’s continued exploration of respondent’s pocket after having concluded that it contained no weapon was unrelated to “[t]he sole justification of the search [under Terry:]. .. the protection of the police officer and others nearby.” 392 U. S., at 29. It therefore amounted to the sort of evidentiary search that <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>expressly refused to authorize, see <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#26" aria-description="Citation for case: Terry v. Ohio"><em>id., </em>at 26</a></span>, and that we have condemned in subsequent cases. See <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1049" aria-description="Citation for case: Michigan v. Long">463 U. S., at 1049, n. 14</a></span>; <em>Sibron, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#65" aria-description="Citation for case: Sibron v. New York">392 U. S., at 65-66</a></span>.</p>
<p id="b426-6">Once again, the analogy to the plain-view doctrine is apt. In <em>Arizona </em>v. <em>Hicks, </em><span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/" aria-description="Citation for case: Arizona v. Hicks">480 U. S. 321</a></span> (1987), this Court held invalid the seizure of stolen stereo equipment found by police while executing a valid search for other evidence. Although <page-number citation-index="1" label="379">*379</page-number>the police were lawfully on the premises, they obtained probable cause to believe that the stereo equipment was contraband only after moving the equipment to permit officers to read its serial numbers. The subsequent seizure of the equipment could not be justified by the plain-view doctrine, this Court explained, because the incriminating character of the stereo equipment was not immediately apparent; rather, probable cause to believe that the equipment was stolen arose only as a result of a further search — the moving of the equipment — that was not authorized by a search warrant or by any exception to the warrant requirement. The facts of this case are very similar. Although the officer was lawfully in a position to feel the lump in respondent’s pocket, because <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>entitled him to place his hands upon respondent’s jacket, the court below determined that the incriminating character of the object was not immediately apparent to him. Rather, the officer determined that the item was contraband only after conducting a further search, one not authorized by <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>or by any other exception to the warrant requirement. Because this further search of respondent’s pocket was constitutionally invalid, the seizure of the cocaine that followed is likewise unconstitutional. <em>Horton, </em><span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#140" aria-description="Citation for case: Horton v. California">496 U. S., at 140</a></span>.</p>
<p id="b427-5">IV</p>
<p id="b427-6">For these reasons, the judgment of the Minnesota Supreme Court is</p>
<p id="b427-7">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b419-6"> Most state and federal courts have recognized a so-called “plain-feel” or “plain-touch” corollary to the plain-view doctrine. See <em>United States </em>v. <em>Coleman, </em><span class="citation" data-id="586858"><a href="/opinion/586858/united-states-v-floyd-coleman/#132" aria-description="Citation for case: United States v. Floyd Coleman">969 F. 2d 126, 132</a></span> (CA5 1992); <em>United States </em>v. <em>Salazar, </em><span class="citation" data-id="9482105"><a href="/opinion/568550/united-states-v-antonio-duran-salazar/#51" aria-description="Citation for case: United States v. Antonio Duran Salazar">945 F. 2d 47, 51</a></span> (CA2 1991), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./504/923/">504 U. S. 923</a></span> (1992); <em>United States </em>v. <em>Buchannon, </em><span class="citation" data-id="9479232"><a href="/opinion/525639/united-states-v-keith-buchannon/#1067" aria-description="Citation for case: United States v. Keith Buchannon">878 F. 2d 1065, 1067</a></span> (CA8 1989); <em>United States </em>v. <em>Williams, </em>262 U. S. App. D. C. 112, 119-124, <span class="citation" data-id="490903"><a href="/opinion/490903/united-states-v-randolph-williams/#1181" aria-description="Citation for case: United States v. Randolph Williams">822 F. 2d 1174, 1181-1186</a></span> (1987); <em>United States </em>v. <em>Norman, </em><span class="citation" data-id="9470347"><a href="/opinion/415216/united-states-v-paul-mayhew-norman-united-states-of-america-v-ramon/#297" aria-description="Citation for case: United States v. Paul Mayhew Norman, United States of...">701 F. 2d 295, 297</a></span> (CA4), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./464/820/">464 U. S. 820</a></span> (1983); <em>People </em>v. <em>Chavers, </em><span class="citation" data-id="9547861"><a href="/opinion/1173996/people-v-chavers/#471" aria-description="Citation for case: People v. Chavers">33 Cal. 3d 462, 471-473</a></span>, <span class="citation" data-id="9547861"><a href="/opinion/1173996/people-v-chavers/#102" aria-description="Citation for case: People v. Chavers">658 P. 2d 96, 102-104</a></span> (1983); <em>Dickerson </em>v. <em>State, </em>No. 228, <span class="citation no-link">1993 Del. LEXIS 12</span>, *3-*4 (Jan. 26, 1993); <em>State </em>v. <em>Guy, </em><span class="citation" data-id="9583593"><a href="/opinion/1251064/state-v-guy/#101" aria-description="Citation for case: State v. Guy">172 Wis. 2d 86, 101-102</a></span>, <span class="citation" data-id="9583593"><a href="/opinion/1251064/state-v-guy/#317" aria-description="Citation for case: State v. Guy">492 N. W. 2d 311, 317-318</a></span> (1992). Some state courts, however, like the Minnesota court in this case, have rejected such a corollary. See <em>People </em>v. <em>Diaz, </em>81 N. Y. 2d 106, <span class="citation" data-id="9786461"><a href="/opinion/2583506/people-v-diaz/" aria-description="Citation for case: People v. Diaz">612 N. E. 2d 298</a></span> (1993); <em>State </em>v. <em>Collins, </em><span class="citation" data-id="1254712"><a href="/opinion/1254712/state-v-collins/#435" aria-description="Citation for case: State v. Collins">139 Ariz. 434, 435-438</a></span>, <span class="citation multiple-matches"><a href="/c/P.%202d/679/80/">679 P. 2d 80</a></span>, 81-84 (Ct. App. 1983); <em>People </em>v. <em>McCarty, </em><span class="citation" data-id="2001156"><a href="/opinion/2001156/people-v-mccarty/#422" aria-description="Citation for case: People v. McCarty">11 Ill. App. 3d 421, 422</a></span>, <span class="citation multiple-matches"><a href="/c/N.%20E.%202d/296/862/">296 N. E. 2d 862</a></span>, 863 (1973); <em>State </em>v. <em>Rhodes, </em><span class="citation" data-id="9854175"><a href="/opinion/1293458/state-v-rhodes/#1381" aria-description="Citation for case: State v. Rhodes">788 P 2d 1380, 1381</a></span> (Okla. Crim. App. 1990); <em>State </em>v. <em>Broadnax, </em><span class="citation" data-id="9605200"><a href="/opinion/1369743/state-v-broadnax/#296" aria-description="Citation for case: State v. Broadnax">98 Wash. 2d 289, 296-301</a></span>, <span class="citation" data-id="9605200"><a href="/opinion/1369743/state-v-broadnax/#101" aria-description="Citation for case: State v. Broadnax">654 P. 2d 96, 101-103</a></span> (1982); cf. <em>Commonwealth v. Marconi, </em><span class="citation" data-id="9647869"><a href="/opinion/1527482/commonwealth-v-marconi/#611" aria-description="Citation for case: Commonwealth v. Marconi">408 Pa. Super. 601, 611-615</a></span>, and n. 17, <span class="citation" data-id="9647869"><a href="/opinion/1527482/commonwealth-v-marconi/#621" aria-description="Citation for case: Commonwealth v. Marconi">597 A. 2d 616, 621-623</a></span>, and n. 17 (1991), appeal denied, <span class="citation no-link">531 Pa. 638</span>, <span class="citation no-link">611 A. 2d 711</span> (1992).</p>
</footnote>
<footnote label="2">
<p id="b419-7"> Before reaching the merits of the Fourth Amendment issue, we must address respondent’s contention that the case is moot. After respondent was found guilty of the drug possession charge, the trial court sentenced respondent under a diversionary sentencing statute to a 2-year period of probation. As allowed by the diversionary scheme, no judgment of conviction was entered and, upon respondent’s successful completion of probation, the original charges were dismissed. See <span class="citation no-link">Minn. Stat. § 152.18</span> (1992). Respondent argues that the case has been rendered moot by the dismissal of the original criminal charges. We often have observed, however, that <page-number citation-index="1" label="372">*372</page-number>"the possibility of a criminal defendant’s suffering ‘collateral legal consequences’ from a sentence already served” precludes a finding of mootness. <em>Pennsylvania </em>v. <em>Minims, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#108" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 108</a></span>, it 3 (1977) <em>(per curiam); </em>see also <em>Evitts </em>v. <em>Lucey, </em><span class="citation" data-id="9429817"><a href="/opinion/111302/evitts-v-lucey/#391" aria-description="Citation for case: Evitts v. Lucey">469 U. S. 387, 391, n. 4</a></span> (1985); <em>Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#53" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 53-58</a></span> (1968). In this case, Minnesota law provides that the proceeding which culminated in finding respondent guilty “shall not be deemed a conviction for purposes of disqualifications or disabilities imposed by law upon conviction of a crime or for any other purpose.” <span class="citation no-link">Minn. Stat. § 152.18</span> (1992). The statute also provides, however, that a nonpublic record of the charges dismissed pursuant to the statute “shall be retained by the department of public safety for the purpose of use by the courts in determining the merits of subsequent proceedings” against the respondent. <em><span class="citation no-link">Ibid.</span> </em>Construing this provision, the Minnesota Supreme Court has held that “[t]he statute contemplates use of the record should [a] defendant have ‘future difficulties with the law.’” <em>State </em>v. <em>Goodrich, </em><span class="citation" data-id="1281913"><a href="/opinion/1281913/state-v-goodrich/#512" aria-description="Citation for case: State v. Goodrich">256 N. W. 2d 506, 512</a></span> (1977). Moreover, the Court of Appeals for the Eighth Circuit has held that a diversionary disposition under § 152.18 may be included in calculating a defendant’s criminal history category in the event of a subsequent federal conviction. <em>United States </em>v. <em>Frank, </em><span class="citation" data-id="560550"><a href="/opinion/560550/united-states-v-david-lee-frank/#701" aria-description="Citation for case: United States v. David Lee Frank">932 F. 2d 700, 701</a></span> (1991). Thus, we must conclude that reinstatement of the record of the charges against respondent would carry collateral legal consequences and that, therefore, a live controversy remains.</p>
</footnote>
<footnote label="3">
<p id="b424-6"> “[T]he police officer in each [case would have] had a prior justification for an intrusion in the course of which he came inadvertently across a piece of evidence incriminating the accused. The doctrine serves to supplement the prior justification . . , and permits the warrantless seizure.” <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#466" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 466</a></span> (1971) (opinion of Stewart, J.).</p>
</footnote>
<footnote label="4">
<p id="b424-7"> We also note that this Court’s opinion in <em>Ybarra </em>v. <em>Illinois, </em><span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85</a></span> (1979), appeared to contemplate the possibility that police officers could obtain probable cause justifying a seizure of contraband through the sense of touch In that case, police officers had entered a tavern and subjected its patrons to patdown searches. While patting down the petitioner Ybarra, an “officer felt what he described as ‘a cigarette pack with objects in it,'” seized it, and discovered heroin inside. <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/#88" aria-description="Citation for case: Ybarra v. Illinois"><em>Id., </em>at 88-89</a></span>. The State argued that the seizure was constitutional on the grounds that the officer obtained probable cause to believe that Ybarra was carrying contraband during the course of a lawful <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>frisk. <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/#92" aria-description="Citation for case: Ybarra v. Illinois"><em>Ybarra, supra, </em>at 92</a></span>. This <page-number citation-index="1" label="377">*377</page-number>Court rejected that argument on the grounds that “[t]he initial frisk of Ybarra was simply not supported by a reasonable belief that he was armed and presently dangerous,” as required by <em>Terry. </em><span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/#92" aria-description="Citation for case: Ybarra v. Illinois">444 U. S., at 92-93</a></span>. The Court added: “[s]ince we conclude that the initial patdown of Ybarra was not justified under the Fourth and Fourteenth Amendments, we need not decide whether or not the presence on Ybarra's person of 'a cigarette pack with objects in it’ yielded probable cause to believe that Ybarra was carrying any illegal substance.” <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/#93" aria-description="Citation for case: Ybarra v. Illinois"><em>Id., </em>at 93, n. 5</a></span>. The Court’s analysis does not suggest, and indeed seems inconsistent with, the existence of a categorical bar against seizures of contraband detected manually during a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>patdown search.</p>
</footnote>
</opinion>
```

---
