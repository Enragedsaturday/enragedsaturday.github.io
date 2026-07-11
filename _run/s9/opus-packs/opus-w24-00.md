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

## GROUP: _overhaul2/lake/cases/millbrook-v-united-states--856345.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "826acf31360e7be9", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "millbrook-v-united-states--856345"}, "payload": {"all": [{"cite": "133 S. Ct. 1441", "page": "1441", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "133"}, {"cite": "185 L. Ed. 2d 531", "page": "531", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "185"}, {"cite": "2013 U.S. LEXIS 2543", "page": "2543", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2013"}, {"cite": "569 U.S. 50", "page": "50", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "569"}, {"cite": "24 Fla. L. Weekly Fed. S 123", "page": "123", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "24"}, {"cite": "81 U.S.L.W. 4223", "page": "4223", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "81"}, {"cite": "2013 WL 1222647", "page": "1222647", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2013"}], "display": null, "official": null, "official_selection_present": false, "record_id": "millbrook-v-united-states--856345"}}
{"assertion_id": "f915497eb515aa71", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "millbrook-v-united-states--856345"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "millbrook-v-united-states--856345", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — millbrook-v-united-states--856345

```json
{
  "schema_version": "s2.v1",
  "record_id": "millbrook-v-united-states--856345",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Millbrook v. United States",
    "case_name_short": "Millbrook",
    "case_name_full": "Kim MILLBROOK, Petitioner v. UNITED STATES.",
    "input_case_name": "Millbrook v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2013-03-27",
    "year": 2013,
    "docket": "No. 11-10362",
    "cluster_id": 856345,
    "lead_opinion_id": 856345,
    "sibling_ids": [],
    "absolute_url": "/opinion/856345/millbrook-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "133 S. Ct. 1441",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "1441",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "185 L. Ed. 2d 531",
        "volume": "185",
        "reporter": "L. Ed. 2d",
        "page": "531",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "569 U.S. 50",
        "volume": "569",
        "reporter": "U.S.",
        "page": "50",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 123",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "123",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 U.S.L.W. 4223",
        "volume": "81",
        "reporter": "U.S.L.W.",
        "page": "4223",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2013 U.S. LEXIS 2543",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "2543",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 WL 1222647",
        "volume": "2013",
        "reporter": "WL",
        "page": "1222647",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "133 S. Ct. 1441",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "1441",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "185 L. Ed. 2d 531",
        "volume": "185",
        "reporter": "L. Ed. 2d",
        "page": "531",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 U.S. LEXIS 2543",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "2543",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "569 U.S. 50",
        "volume": "569",
        "reporter": "U.S.",
        "page": "50",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 123",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "123",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 U.S.L.W. 4223",
        "volume": "81",
        "reporter": "U.S.L.W.",
        "page": "4223",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 WL 1222647",
        "volume": "2013",
        "reporter": "WL",
        "page": "1222647",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "other",
      "selected": null,
      "reason": "unlisted_reporter:S. Ct."
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
    "date_created": "2026-07-06T13:42:26Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:42:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:42:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:42:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:42:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — millbrook-v-united-states--856345

```
(Slip Opinion)              OCTOBER TERM, 2012                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                 MILLBROOK v. UNITED STATES

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE THIRD CIRCUIT

 No. 11–10362.       Argued February 19, 2013—Decided March 27, 2013
The Federal Tort Claims Act (FTCA) waives the Government’s sover-
  eign immunity from tort suits, but excepts from that waiver certain
  intentional torts, 28 U. S. C. §2680(h). Section §2680(h), in turn, con-
  tains a proviso that extends the waiver of immunity to claims for six
  intentional torts, including assault and battery, that are based on the
  “acts or omissions” of an “investigative or law enforcement officer”
  i.e., a federal officer “who is empowered by law to execute searches, to
  seize evidence, or to make arrests.” Petitioner Millbrook, a federal
  prisoner, sued the United States under the FTCA, alleging, inter alia,
  assault and battery by correctional officers. The District Court
  granted the Government summary judgment, and the Third Circuit
  affirmed, hewing to its precedent that the “law enforcement proviso”
  applies only to tortious conduct that occurs during the course of exe-
  cuting a search, seizing evidence, or making an arrest.
Held: The law enforcement proviso extends to law enforcement officers’
 acts or omissions that arise within the scope of their employment, re-
 gardless of whether the officers are engaged in investigative or law
 enforcement activity, or are executing a search, seizing evidence, or
 making an arrest. The proviso’s plain language supports this conclu-
 sion. On its face, the proviso applies where a claim arises out of one
 of six intentional torts and is related to the “acts or omissions” of an
 “investigative or law enforcement officer.” §2680(h). And by cross-
 referencing §1346(b), the proviso incorporates an additional require-
 ment that the “acts or omissions” occur while the officer is “acting
 within the scope of his office or employment.” §1346(b)(1). Nothing
 in §2680(h)’s text supports further limiting the proviso to conduct
 arising out of searches, seizures of evidence, or arrests. The FTCA’s
 only reference to those terms is in §2680(h)’s definition of “investiga-
2                   MILLBROOK v. UNITED STATES

                                 Syllabus

    tive or law enforcement officer,” which focuses on the status of per-
    sons whose conduct may be actionable, not the types of activities that
    may give rise to a claim. This confirms that Congress intended im-
    munity determinations to depend on a federal officer’s legal author-
    ity, not on a particular exercise of that authority. Nor does the pro-
    viso indicate that a waiver of immunity requires the officer to be
    engaged in investigative or law enforcement activity. The text never
    uses those terms. Had Congress intended to further narrow the
    waiver’s scope, it could have used language to that effect. See Ali v.
    Federal Bureau of Prisons, 552 U. S. 214, 227. Pp. 4−8.
477 Fed. Appx. 4, reversed and remanded.

    THOMAS, J., delivered the opinion for a unanimous Court.
                        Cite as: 569 U. S. ____ (2013)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                  No. 11–10362
                                   _________________


 KIM MILLBROOK, PETITIONER v. UNITED STATES
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE THIRD CIRCUIT

                                [March 27, 2013]


   JUSTICE THOMAS delivered the opinion of the Court.
   Petitioner Kim Millbrook, a prisoner in the custody of
the Federal Bureau of Prisons (BOP), alleges that correc-
tional officers sexually assaulted and verbally threatened
him while he was in their custody. Millbrook filed suit
in Federal District Court under the Federal Tort Claims
Act, 28 U. S. C. §§1346(b), 2671–2680 (FTCA or Act),
which waives the Government’s sovereign immunity from
tort suits, including those based on certain intentional torts
committed by federal law enforcement officers, §2680(h).
The District Court dismissed Millbrook’s action, and the
Court of Appeals affirmed. The Court of Appeals held
that, while the FTCA waives the United States’ sovereign
immunity for certain intentional torts by law enforcement
officers, it only does so when the tortious conduct occurs in
the course of executing a search, seizing evidence, or
making an arrest. Petitioner contends that the FTCA’s
waiver is not so limited. We agree and reverse the judg-
ment of the Court of Appeals.1
——————
  1 Because no party defends the judgment, we appointed Jeffrey S.

Bucholtz to brief and argue this case, as amicus curiae, in support of
the judgment below. 568 U. S. ___ (2012). Amicus Bucholtz has ably
2                MILLBROOK v. UNITED STATES

                         Opinion of the Court

                               I

                               A

   The FTCA “was designed primarily to remove the sover-
eign immunity of the United States from suits in tort.”
Levin v. United States, 568 U. S. ___, ___ (2013) (slip op.,
at 2) (internal quotation marks omitted). The Act gives
federal district courts exclusive jurisdiction over claims
against the United States for “injury or loss of property,
or personal injury or death caused by the negligent or
wrongful act or omission” of a federal employee “acting
within the scope of his office or employment.” 28 U. S. C.
§1346(b)(1). This broad waiver of sovereign immunity is
subject to a number of exceptions set forth in §2680. One
such exception, relating to intentional torts, preserves the
Government’s immunity from suit for “[a]ny claim arising
out of assault, battery, false imprisonment, false arrest,
malicious prosecution, abuse of process, libel, slander,
misrepresentation, deceit, or interference with contract
rights.” §2680(h). We have referred to §2680(h) as the
“intentional tort exception.” Levin, supra, at ___ (slip op.,
at 2) (internal quotation marks omitted).
   In 1974, Congress carved out an exception to §2680(h)’s
preservation of the United States’ sovereign immunity
for intentional torts by adding a proviso covering claims
that arise out of the wrongful conduct of law enforcement
officers. See Act of Mar. 16, 1974, Pub. L. 93–253, §2, 88
Stat. 50. Known as the “law enforcement proviso,” this
provision extends the waiver of sovereign immunity to
claims for six intentional torts, including assault and
battery, that are based on the “acts or omissions of inves-
tigative or law enforcement officers.” §2680(h). The pro-
viso defines “ ‘investigative or law enforcement officer’ ” to
mean “any officer of the United States who is empowered
—————— 

discharged his assigned responsibilities, and the Court thanks him for

his well-stated arguments. 

                     Cite as: 569 U. S. ____ (2013)                    3

                          Opinion of the Court

by law to execute searches, to seize evidence, or to make
arrests for violations of Federal law.” Ibid.
                              B
  On January 18, 2011, Millbrook filed suit against the
United States under the FTCA, asserting claims of negli-
gence, assault, and battery. In his complaint, Millbrook
alleged that, on March 5, 2010, he was forced to per-
form oral sex on a BOP correctional officer, while another
officer held him in a choke hold and a third officer stood
watch nearby. Millbrook claimed that the officers threat-
ened to kill him if he did not comply with their demands.
Millbrook alleged that he suffered physical injuries as a
result of the incident and, accordingly, sought compensa-
tory damages.
  The Government argued that the FTCA did not waive
the United States’ sovereign immunity from suit on
Millbrook’s intentional tort claims, because they fell with-
in the intentional tort exception in §2680(h). The Govern-
ment contended that §2680(h)’s law enforcement proviso
did not save Millbrook’s claims because of the Third Cir-
cuit’s binding precedent in Pooler v. United States, 787
F. 2d 868 (1986), which interpreted the proviso to apply
only to tortious conduct that occurred during the course
of “executing a search, seizing evidence, or making an ar-
rest.” Id., at 872. The District Court agreed and granted
summary judgment for the United States because the
alleged conduct “did not take place during an arrest,
search, or seizure of evidence.” Civ. Action No. 3:11–cv–
00131 (MD Pa., Feb. 16, 2012), App. 96.2 The Third Cir-
cuit affirmed. 477 Fed. Appx. 4, 5–6 (2012) (per curiam).
  We granted certiorari, 567 U. S. ___ (2012), to resolve a
Circuit split concerning the circumstances under which
——————
  2 The District Court also concluded that Millbrook failed to state an

actionable negligence claim because “it is clear that the alleged assault
and battery was intentional.” App. 96. This issue is not before us.
4              MILLBROOK v. UNITED STATES

                      Opinion of the Court

intentionally tortious conduct by law enforcement officers
can give rise to an actionable claim under the FTCA.
Compare Pooler, supra; and Orsay v. United States Dept.
of Justice, 289 F. 3d 1125, 1136 (CA9 2002) (law enforce-
ment proviso “reaches only those claims asserting that the
tort occurred in the course of investigative or law enforce-
ment activities” (emphasis added)); with Ignacio v. United
States, 674 F. 3d 252, 256 (CA4 2012) (holding that the
law enforcement proviso “waives immunity whenever an
investigative or law enforcement officer commits one of the
specified intentional torts, regardless of whether the officer
is engaged in investigative or law enforcement activity”
(emphasis added)).
                            II
  The FTCA waives the United States’ sovereign immu-
nity for certain intentional torts committed by law en-
forcement officers. The portion of the Act relevant here
provides:
       “The provisions of this chapter and section 1346(b)
    of this title shall not apply to—
      .           .            .             .        .
        “(h) Any claim arising out of assault, battery, false
    imprisonment, false arrest, malicious prosecution,
    abuse of process, libel, slander, misrepresentation, de-
    ceit, or interference with contract rights: Provided,
    That, with regard to acts or omissions of investigative
    or law enforcement officers of the United States Gov-
    ernment, the provisions of this chapter and section
    1346(b) of this title shall apply to any claim arising
    . . . out of assault, battery, false imprisonment, false
    arrest, abuse of process, or malicious prosecution.” 28
    U. S. C. §2680(h).
On its face, the law enforcement proviso applies where a
claim both arises out of one of the proviso’s six intentional
                    Cite as: 569 U. S. ____ (2013)                   5

                         Opinion of the Court

torts, and is related to the “acts or omissions” of an “inves-
tigative or law enforcement officer.” The proviso’s cross-
reference to §1346(b) incorporates an additional require-
ment that the acts or omissions giving rise to the claim
occur while the officer is “acting within the scope of his
office or employment.” §1346(b)(1). The question in this
case is whether the FTCA further limits the category
of “acts or omissions” that trigger the United States’
liability.3
   The plain language of the law enforcement proviso
answers when a law enforcement officer’s “acts or omis-
sions” may give rise to an actionable tort claim under the
FTCA. The proviso specifies that the conduct must arise
from one of the six enumerated intentional torts and,
by expressly cross-referencing §1346(b), indicates that the
law enforcement officer’s “acts or omissions” must fall
“within the scope of his office or employment.” §§2680(h),
1346(b)(1). Nothing in the text further qualifies the cate-
gory of “acts or omissions” that may trigger FTCA liability.
   A number of lower courts have nevertheless read into
the text additional limitations designed to narrow the
scope of the law enforcement proviso. The Ninth Circuit,
for instance, held that the law enforcement proviso does
not apply unless the tort was “committed in the course of
investigative or law enforcement activities.” Orsay, supra,
at 1135. As noted, the Third Circuit construed the law
enforcement proviso even more narrowly in holding that it
applies only to tortious conduct by federal officers during
the course of “executing a search, seizing evidence, or
making an arrest.” Pooler, 787 F. 2d, at 872. Court-
——————
   3 The Government conceded in the proceedings below that the correc-

tional officer whose alleged conduct is at issue was acting within the
scope of his employment and that the named correctional officers
qualify as “investigative or law enforcement officers” within the mean-
ing of the FTCA. App. 54–55, 84–85; Brief for United States 30.
Accordingly, we express no opinion on either of these issues.
6               MILLBROOK v. UNITED STATES

                      Opinion of the Court

appointed amicus curiae (Amicus) similarly asks us to
construe the proviso to waive “sovereign immunity only for
torts committed by federal officers acting in their capacity
as ‘investigative or law enforcement officers.’ ” Brief for
Amicus 5. Under this approach, the conduct of federal
officers would be actionable only when it “aris[es] out of
searches, seizures of evidence, arrests, and closely related
exercises of investigative or law-enforcement authority.”
Ibid.
  None of these interpretations finds any support in the
text of the statute. The FTCA’s only reference to “searches,”
“seiz[ures of ] evidence,” and “arrests” is found in the
statutory definition of “investigative or law enforcement
officer.” §2680(h) (defining “ ‘investigative or law enforce-
ment officer’ ” to mean any federal officer who is “empow-
ered by law to execute searches, to seize evidence, or to
make arrests for violations of Federal law”). By its terms,
this provision focuses on the status of persons whose con-
duct may be actionable, not the types of activities that
may give rise to a tort claim against the United States.
The proviso thus distinguishes between the acts for which
immunity is waived (e.g., assault and battery), and the
class of persons whose acts may give rise to an actionable
FTCA claim. The plain text confirms that Congress in-
tended immunity determinations to depend on a federal
officer’s legal authority, not on a particular exercise of that
authority. Consequently, there is no basis for concluding
that a law enforcement officer’s intentional tort must oc-
cur in the course of executing a search, seizing evidence,
or making an arrest in order to subject the United States
to liability.
  Nor does the text of the proviso provide any indication
that the officer must be engaged in “investigative or law
enforcement activity.” Indeed, the text never uses the
term. Amicus contends that we should read the reference
to “investigative or law-enforcement officer” as implicitly
                  Cite as: 569 U. S. ____ (2013)            7

                      Opinion of the Court

limiting the proviso to claims arising from actions taken
in an officer’s investigative or law enforcement capacity.
But there is no basis for so limiting the term when Con-
gress has spoken directly to the circumstances in which a
law enforcement officer’s conduct may expose the United
States to tort liability. Under the proviso, an intentional
tort is not actionable unless it occurs while the law en-
forcement officer is “acting within the scope of his office or
employment.” §§2680(h), 1346(b)(1). Had Congress in-
tended to further narrow the scope of the proviso, Con-
gress could have limited it to claims arising from “acts or
omissions of investigative or law enforcement officers
acting in a law enforcement or investigative capacity.” See
Ali v. Federal Bureau of Prisons, 552 U. S. 214, 227 (2008).
Congress adopted similar limitations in neighboring provi-
sions, see §2680(a) (referring to “[a]ny claim based upon
an act or omission of an employee of the Government . . .
in the execution of a statute or regulation” (emphasis
added)), but did not do so here. We, therefore, decline to
read such a limitation into unambiguous text. Jimenez v.
Quarterman, 555 U. S. 113, 118 (2009) (“[W]hen the statu-
tory language is plain, we must enforce it according to its
terms”); Barnhart v. Sigmon Coal Co., 534 U. S. 438, 450
(2002) (“The inquiry ceases if the statutory language is
unambiguous and the statutory scheme is coherent and
consistent” (internal quotation marks omitted)).
                        *    *    *
  We hold that the waiver effected by the law enforcement
proviso extends to acts or omissions of law enforcement
officers that arise within the scope of their employment,
regardless of whether the officers are engaged in investi-
gative or law enforcement activity, or are executing a
search, seizing evidence, or making an arrest. Accord-
ingly, we reverse the judgment of the Court of Appeals and
remand the case for further proceedings consistent with
8               MILLBROOK v. UNITED STATES

                     Opinion of the Court

this opinion.
                                            It is so ordered.

```

---

## GROUP: _overhaul2/lake/cases/morgan-v-fairfield-county--u2812be2f.json  (`lake-record`, 1 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1c114546ec0e87a7", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "morgan-v-fairfield-county--u2812be2f"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "morgan-v-fairfield-county--u2812be2f", "scope_note": null, "varies_by_point": false}}
```

### lake record — morgan-v-fairfield-county--u2812be2f

```json
{
  "schema_version": "s2.v1",
  "record_id": "morgan-v-fairfield-county--u2812be2f",
  "stub": true,
  "status": "not_found",
  "identity": {
    "case_name": null,
    "case_name_short": null,
    "case_name_full": null,
    "input_case_name": "Morgan v. Fairfield County",
    "court": "6th Cir. 2018",
    "court_id": null,
    "court_level": null,
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": null,
    "docket": null,
    "cluster_id": null,
    "lead_opinion_id": null,
    "sibling_ids": [],
    "absolute_url": null,
    "identity_method": "not_found",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": null,
    "alternates": [],
    "reason_code": "frontier_no_candidate_cluster"
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": null,
      "selected": null,
      "reason": null
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
    "scope_note": null,
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
    "date_created": "2026-07-06T05:47:09Z",
    "date_modified": "2026-07-06T05:47:15Z",
    "warnings": [
      "frontier not_found requires web/second-source cross-check before fabrication inference"
    ],
    "field_provenance": {
      "identity": {
        "src": "pending",
        "at": "2026-07-06T05:47:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "pending",
        "at": "2026-07-06T05:47:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "pending",
        "at": "2026-07-06T05:47:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "pending",
        "at": "2026-07-06T05:47:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

---

## GROUP: _overhaul2/lake/cases/morse-v-french--6536632.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "cbb97c137adafe72", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "morse-v-french--6536632"}, "payload": {"all": [{"cite": "68 Mass. 111", "page": "111", "reporter": "Mass.", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "68"}], "display": "68 Mass. 111", "official": {"cite": "68 Mass. 111", "page": "111", "reporter": "Mass.", "selected_official": true, "source": "cluster.citations[]", "type": 2, "volume": "68"}, "official_selection_present": true, "record_id": "morse-v-french--6536632"}}
{"assertion_id": "ac2f42ef043ba296", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "morse-v-french--6536632"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "morse-v-french--6536632", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — morse-v-french--6536632

```json
{
  "schema_version": "s2.v1",
  "record_id": "morse-v-french--6536632",
  "stub": true,
  "status": "folded-alias",
  "identity": {
    "case_name": "French v. Morse",
    "case_name_short": "French",
    "case_name_full": "Abram French v. Jonathan Morse",
    "input_case_name": "Morse v. French",
    "court": "2022",
    "court_id": null,
    "court_level": null,
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": null,
    "docket": null,
    "cluster_id": 6536632,
    "lead_opinion_id": null,
    "sibling_ids": [],
    "absolute_url": "/opinion/6536632/french-v-morse/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": false,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "68 Mass. 111",
      "volume": "68",
      "reporter": "Mass.",
      "page": "111",
      "type": 2,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "68 Mass. 111",
        "volume": "68",
        "reporter": "Mass.",
        "page": "111",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "68 Mass. 111",
    "official_selection": {
      "court_class": "state",
      "selected": "68 Mass. 111",
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
    "date_created": "2026-07-06T05:47:16Z",
    "date_modified": "2026-07-07T01:43:35Z",
    "warnings": [
      "folded-alias: subsumed into French v. Merrill (packet-A Group-2); see _manifest.json folded_into + journal s6-dedupe-pointer"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:47:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:47:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:47:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:47:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

---

## GROUP: _overhaul2/lake/cases/new-jersey-v-portash--110038.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e2bc48a720757238", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "new-jersey-v-portash--110038"}, "payload": {"all": [{"cite": "440 U.S. 450", "page": "450", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "440"}, {"cite": "99 S. Ct. 1292", "page": "1292", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "99"}, {"cite": "59 L. Ed. 2d 501", "page": "501", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "59"}, {"cite": "1979 U.S. LEXIS 73", "page": "73", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1979"}], "display": null, "official": null, "official_selection_present": false, "record_id": "new-jersey-v-portash--110038"}}
{"assertion_id": "6d975458d1272bfe", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "new-jersey-v-portash--110038"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "new-jersey-v-portash--110038", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — new-jersey-v-portash--110038

```json
{
  "schema_version": "s2.v1",
  "record_id": "new-jersey-v-portash--110038",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "New Jersey v. Portash",
    "case_name_short": "Portash",
    "case_name_full": "New Jersey v. Portash",
    "input_case_name": "New Jersey v. Portash",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-03-20",
    "year": 1979,
    "docket": null,
    "cluster_id": 110038,
    "lead_opinion_id": 9427490,
    "sibling_ids": [],
    "absolute_url": "/opinion/110038/new-jersey-v-portash/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "440 U.S. 450",
        "volume": "440",
        "reporter": "U.S.",
        "page": "450",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 1292",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "59 L. Ed. 2d 501",
        "volume": "59",
        "reporter": "L. Ed. 2d",
        "page": "501",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 73",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "73",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "440 U.S. 450",
        "volume": "440",
        "reporter": "U.S.",
        "page": "450",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 1292",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "59 L. Ed. 2d 501",
        "volume": "59",
        "reporter": "L. Ed. 2d",
        "page": "501",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 73",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "73",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "other",
      "selected": null,
      "reason": "unlisted_reporter:U.S."
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
    "date_created": "2026-07-06T13:48:41Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:48:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:48:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:48:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:48:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — new-jersey-v-portash--110038

```
<opinion type="majority">
<author id="b521-7">Mr. Justice Stewart</author>
<p id="Aeh">delivered the opinion of the Court.</p>
<p id="b521-8">This case involves the scope of the privilege against compulsory self-incrimination, grounded in the Fifth Amendment and made binding against the States by the Fourteenth. The precise question is whether, despite this constitutional privilege, a prosecutor may use a person’s legislatively immunized grand jury testimony to impeach his credibility as a testifying defendant in a criminal trial.</p>
<p id="b521-9">I</p>
<p id="b521-10">In the early 1970’s, Joseph Portash was Mayor of Manchester Township, Executive Director of the Pinelands Environmental Council, and a member of both the Ocean County Board of Freeholders and the Manchester Municipal Utilities Authority in New Jersey. In November 1974, after a lengthy investigation, a state grand jury subpoenaed Portash. He expressed an intention to claim his privilege against compulsory self-incrimination. The prosecutors and Portash’s lawyers then agreed that, if Portash testified before the grand jury, neither his statements nor any evidence derived from them could, under New Jersey law, be used in subsequent criminal proceedings (except in prosecutions for perjury or <page-number citation-index="1" label="452">*452</page-number>false swearing) ,<footnotemark>1</footnotemark> After Portash’s testimony, the parties tried to come to an agreement to avoid a criminal prosecution against Portash, but no bargain was reached. In April 1975, Portash was indicted for misconduct in office and extortion by a public official.<footnotemark>2</footnotemark></p>
<p id="b522-5">Before trial, defense counsel sought to obtain a ruling from the trial judge that no use of the immunized grand jury testimony would be permitted. The judge refused to rule that the prosecution could not use this testimony for purposes of impeachment. After the completion of the State’s case, defense counsel renewed his request for a ruling by the trial judge as to the use of the grand jury testimony. There followed an extended colloquy, and the judge finally ruled that if Portash testified and gave an answer on direct or cross-examination which was materially inconsistent with his grand jury testimony, the prosecutor could use that testimony in his cross-examination of Portash. Defense counsel then stated that, because of this ruling, he would advise his client not to take the stand. Portash did not testify, and the jury ultimately found him guilty on one of the two counts.</p>
<p id="b523-4"><page-number citation-index="1" label="453">*453</page-number>The New Jersey Appellate Division reversed the conviction. 151 N. J. Super. 200, <span class="citation" data-id="1907630"><a href="/opinion/1907630/state-v-portash/" aria-description="Citation for case: State v. Portash">376 A. 2d 950</a></span> .(1977). That court held that the Constitution requires that the immunity granted by the New Jersey statute must be at least coextensive with the privilege afforded by the Fifth and Fourteenth Amendments. To confer such protection, the court reasoned, the grant of immunity must “leave defendant and the State in the position each would have occupied had defendant’s claim of privilege [before the grand jury] been honored.” <em>Id., </em>at 205, <span class="citation" data-id="1907630"><a href="/opinion/1907630/state-v-portash/#953" aria-description="Citation for case: State v. Portash">376 A. 2d, at 953</a></span>. Use of the immunized grand jury testimony to impeach a defendant at his trial, it held, did not meet this test. Because Portash’s decision not to testify was based upon the trial court’s erroneous ruling to the contrary, the Appellate Division reversed the conviction and remanded the case for a new trial.<footnotemark>3</footnotemark> The New Jersey Supreme Court denied the State’s petition for certification of an appeal. 75 N. J. 597, <span class="citation multiple-matches"><a href="/c/A.%202d/384/827/">384 A. 2d 827</a></span> (1978). We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./436/955/">436 U. S. 955</a></span>.</p>
<p id="b523-5">II</p>
<p id="b523-6">New Jersey presents two questions. First, it argues that Portash cannot properly invoke the privilege against compulsory incrimination because he did not take the witness stand and, as a result, his immunized grand jury testimony was never used against him. Second, it urges that the Fifth and <page-number citation-index="1" label="454">*454</page-number>Fourteenth Amendments do not prohibit the use of immunized grand jury testimony to impeach materially inconsistent statements made at trial.</p>
<p id="b524-5">A</p>
<p id="b524-6">The State contends that the issue presented by Portash is abstract and hypothetical because he did not, in fact, become a witness. Portash could have taken the stand, testified, objected to the prosecution’s use of the immunized testimony to impeach him, and appealed any subsequent conviction. Absent that, the State would have us hold that the constitutional question was not and is not presented. This argument must be rejected. First, it is clear that although the trial judge was concerned about making a ruling before specific questions were asked, he did rule on the merits of the constitutional question:</p>
<blockquote id="b524-7">“THE COURT: Well, this is what the Court was concerned with and still is and I thought the Court had straightened it out previously, the witness taking the stand and testifying as to something and then have counsel saying didn’t you say before the grand jury such and such.</blockquote>
<blockquote id="b524-8">“MR. WILBERT [defense counsel]: That’s the problem that we have. We don’t know whether he’s going to be able to use that or not, your Honor, especially if he didn’t touch that area in his examination—</blockquote>
<blockquote id="b524-9">“THE COURT: Mr. Wilbert, suppose your client takes the stand and he testifies that I worked for Donald Safran and suppose he testified before the grand jury I never worked for Donald Safran?</blockquote>
<blockquote id="b524-10">“MR. WILBERT: Inconsistency and under your Honor’s ruling that can be used in this case.</blockquote>
<blockquote id="b524-11">“THE COURT: <em>No doubt about it.</em></blockquote>
<blockquote id="b524-12">“MR. WILBERT: Your Honor, I would submit it could be used over my objection, of course.</blockquote>
<blockquote id="b525-4"><page-number citation-index="1" label="455">*455</page-number>“THE COURT: You have a standing objection with respect to the use at all of the grand jury testimony.” (Emphasis added.) App. 223a.</blockquote>
<p id="b525-5">Second, the New Jersey appellate court necessarily concluded that the federal constitutional question had been properly presented, because it ruled in Portash’s favor on the merits.<footnotemark>4</footnotemark> See <em>Raley </em>v. <em>Ohio, </em><span class="citation" data-id="105925"><a href="/opinion/105925/raley-v-ohio/#435" aria-description="Citation for case: Raley v. Ohio">360 U. S. 423, 435-437</a></span>; cf. <em>Jenkins </em>v. <em>Georgia, </em><span class="citation" data-id="9425796"><a href="/opinion/109085/jenkins-v-georgia/#157" aria-description="Citation for case: Jenkins v. Georgia">418 U. S. 153, 157</a></span>; <em>Coleman </em>v. <em>Alabama, </em><span class="citation" data-id="106812"><a href="/opinion/106812/coleman-v-alabama/#133" aria-description="Citation for case: Coleman v. Alabama">377 U. S. 129, 133</a></span>; <em>Whitney </em>v. <em>California, </em><span class="citation" data-id="9418596"><a href="/opinion/101097/whitney-v-california/#360" aria-description="Citation for case: Whitney v. California">274 U. S. 357, 360-361</a></span>; <em>Manhattan Life Ins. Co. </em>v. <em>Cohen, </em><span class="citation" data-id="98212"><a href="/opinion/98212/manhattan-life-ins-co-of-ny-v-cohen/#134" aria-description="Citation for case: Manhattan Life Ins. Co. of NY v. Cohen">234 U. S. 123, 134</a></span>.</p>
<p id="b525-6">Moreover, there is nothing in federal law to prohibit New Jersey from following such a procedure, or, so long as the “case or controversy” requirement of Art. Ill is met, to foreclose our consideration of the substantive constitutional issue now that the New Jersey courts have decided it. This is made clear by a case decided by this Court in 1972, <em>Brooks </em>v. <em>Tennessee, </em><span class="citation" data-id="108551"><a href="/opinion/108551/brooks-v-tennessee/" aria-description="Citation for case: Brooks v. Tennessee">406 U. S. 605</a></span>. There the Court held unconstitutional a Tennessee statutory requirement that a defendant in a criminal case had to be his own first witness if he was to take the stand at all. The Court held that such a requirement unconstitutionally penalized a defendant’s right to remain silent, since a defendant could remain silent immediately after the close of the State’s case only at the cost of never testifying in his own defense. Although Brooks had not testified, the Tennessee court considered the constitutional validity of the state statute, and so did this Court. Because the rule imposed <page-number citation-index="1" label="456">*456</page-number>a penalty on the right to remain silent, the Court found that his constitutional rights had been infringed even though he had never taken the stand. <em><span class="citation" data-id="108551"><a href="/opinion/108551/brooks-v-tennessee/" aria-description="Citation for case: Brooks v. Tennessee">Id.,</a></span> </em>at 611 n. 6.</p>
<p id="b526-5">In <em><span class="citation" data-id="108551"><a href="/opinion/108551/brooks-v-tennessee/" aria-description="Citation for case: Brooks v. Tennessee">Brooks</a></span> </em>the Court held that the defendant’s Fifth and Fourteenth Amendment rights had been violated because, in order to assert his Fifth Amendment right to remain silent after the prosecution’s case in chief had been presented, the defendant would have had to pay a penalty. He could never testify. Here, as in <em><span class="citation" data-id="108551"><a href="/opinion/108551/brooks-v-tennessee/" aria-description="Citation for case: Brooks v. Tennessee">Brooks</a></span>, </em>federal law does not insist that New Jersey was wrong in not requiring Portash to take the witness stand in order to raise his constitutional claim.<footnotemark>5</footnotemark></p>
<p id="b526-6">B</p>
<p id="b526-7">In both Great Britain and in what later became the United States, immunity statutes, like the privilege against compulsory self-incrimination, predate the adoption of the Constitution. <em>Kastigar </em>v. <em>United States, </em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441</a></span>, 445 n. 13, 446 n. 14. This Court first considered a constitutional challenge to an immunity statute in <em>Counselman </em>v. <em>Hitchcock, </em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547</a></span>. The witness in that case had refused to testify before a federal grand jury in spite of a grant of immunity under the relevant federal statute. The Court overturned his contempt conviction. It construed the statute to permit the use of evidence <em>derived </em>from his immunized testimony. The witness was held to have validly asserted his privilege because “legislation cannot abridge a constitutional privilege, and . . . it cannot replace or supply one, at least unless it is so broad <page-number citation-index="1" label="457">*457</page-number>as to have the same extent in scope and effect.” <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#585" aria-description="Citation for case: Counselman v. Hitchcock"><em>Id., </em>at 585</a></span>. See also <em>Brown </em>v. <em>United States, </em><span class="citation" data-id="9421773"><a href="/opinion/105848/brown-v-united-states/" aria-description="Citation for case: Brown v. United States">359 U. S. 41</a></span>; <em>Ullmann </em>v. <em>United States, </em><span class="citation" data-id="9421245"><a href="/opinion/105363/ullmann-v-united-states/" aria-description="Citation for case: Ullmann v. United States">350 U. S. 422</a></span>; <em>Brown </em>v. <em>Walker, </em><span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/" aria-description="Citation for case: Brown v. Walker">161 U. S. 591</a></span>. After the holding in <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span>, that the Fifth Amendment privilege against compulsory self-incrimination is also contained in the Fourteenth Amendment, this rule is necessarily applicable to state immunity statutes as well. Cf. <em>Murphy </em>v. <em>Waterfront Comm’n, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52</a></span>.<footnotemark>6</footnotemark></p>
<p id="b527-5">Language in <em><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/" aria-description="Citation for case: Counselman v. Hitchcock">Counselman</a></span> </em>and its progeny was read by some to require that the witness must be immune from prosecution for the transaction his testimony concerned. Indeed, the federal statutes subsequently upheld by the Court granted such transactional immunity. <em>Brown </em>v. <em>United States, supra; Ullman </em>v. <em>United States, supra; Heike </em>v. <em>United States, </em><span class="citation" data-id="97764"><a href="/opinion/97764/heike-v-united-states/" aria-description="Citation for case: Heike v. United States">227 U. S. 131</a></span>; <em>Brown </em>v. <em><span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/" aria-description="Citation for case: Brown v. Walker">Walker, supra.</a></span></em><footnotemark><em>7</em></footnotemark><em> </em>The adoption of <span class="citation no-link">Pub. L. 91-452 </span>in 1970 marked a change in federal immunity legislation from the provision of transactional immunity to the provision of what is known as “use” immunity. 18 U. S. C §§ 6001, 6002. This immunity, similar to that provided by the New Jersey statute in this case, protects the witness from the use of his compelled testimony and any information derived from it. In <em>Kastigar </em>v. <em>United States, supra, </em>the Court upheld that statute against a challenge that mere use immunity is not coextensive with the Fifth Amendment’s privilege.</p>
<blockquote id="b527-6">“The privilege has never been construed to mean that one who invokes it cannot subsequently be prosecuted. Its <page-number citation-index="1" label="458">*458</page-number>sole concern is to afford protection against being 'forced to give testimony leading to the infliction of “penalties affixed to . . . criminal acts.” ’ Immunity from the use of compelled testimony, as well as evidence derived directly and indirectly therefrom, affords this protection. It prohibits the prosecutorial authorities from using the compelled testimony in <em>any </em>respect, and it therefore insures that the testimony cannot lead to the infliction of criminal penalties on the witness.” 406 U. S., at 453. (Emphasis in original; footnote omitted.)</blockquote>
<p id="b528-4">Against this broad statement of the necessary constitutional scope of testimonial immunity, the State asks us to weigh <em>Harris </em>v. <em>New York, </em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span>, and <em>Oregon </em>v. <em>Hass, </em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714</a></span>.<footnotemark>8</footnotemark> Those cases involved the use of statements, con-cededly taken in violation of <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, to impeach a defendant’s testimony at trial. In both eases the Court weighed the incremental deterrence of police illegality against the strong policy against countenancing perjury. In the balance, use of the incriminating statements for impeachment purposes prevailed. The State asks that we apply the same reasoning to this case. It points out that the interest in preventing perjury is just as strongly involved, and that the statements made to the grand jury are at least as reliable as those made by the defendants in <em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">Harris</a></span> </em>and <em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">Hass</a></span>.</em></p>
<p id="b528-5">But the State has overlooked a crucial distinction between those cases and this one. In <em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">Harris</a></span> </em>and <em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">Hass</a></span> </em>the Court expressly noted that the defendant made “no claim that the statements made to the police were coerced or involuntary,” <em>Harris </em>v. <em>New York, supra, </em>at 224; <em>Oregon </em>v. <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#722" aria-description="Citation for case: Oregon v. Hass"><em>Hass, supra, </em>at <page-number citation-index="1" label="459">*459</page-number>722-723</a></span>. That recognition was central to the decisions in those cases.</p>
<p id="b529-4">The Fifth and the Fourteenth Amendments provide that no person “shall be <em>compelled </em>in any criminal case to be a witness against himself.” As we reaffirmed last Term, a defendant’s compelled statements, as opposed to statements taken in violation of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>may not be put to any testimonial use whatever against him in a criminal trial. “But <em>any </em>criminal trial use against a defendant of his <em>involuntary </em>statement is a denial of due process of law.” (Emphasis in original.) <em>Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#398" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 398</a></span>.<footnotemark>9</footnotemark></p>
<p id="b529-5">Testimony given in response to a grant of legislative immunity is the essence of coerced testimony. In such cases there is no question whether physical or psychological pressures overrode the defendant’s will; the witness is told to talk or face the government’s coercive sanctions, notably, a conviction for contempt. The information given in response to a grant of immunity may well be more reliable than information beaten from a helpless defendant, but it is no less compelled. The Fifth and Fourteenth Amendments provide a privilege against <em>compelled </em>self-incrimination, not merely against unreliable self-incrimination. Balancing of interests was thought to be necessary in <em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">Harris</a></span> </em>and <em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">Hass</a></span> </em>when the attempt to deter unlawful police conduct collided with the need to prevent perjury. Here, by contrast, we deal with the constitutional privilege against compulsory self-incrimination in its most pristine form. Balancing, therefore, is not simply unnecessary. It is impermissible.</p>
<p id="b529-6">The Superior Court of New Jersey, Appellate Division, correctly ruled that a person’s testimony before a grand jury <page-number citation-index="1" label="460">*460</page-number>under a grant of immunity cannot constitutionally be used to impeach him when he is a defendant in a later criminal trial.<footnotemark>10</footnotemark> Accordingly, the judgment is affirmed.</p>
<p id="b530-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b522-6"> At that time a New Jersey statute provided as follows:</p>
<p id="b522-7">“If any public employee testifies before any court, grand jury or the State Commission of Investigation, such testimony and the- evidence derived therefrom shall not be used against such public employee in a subsequent criminal proceeding under the laws of this State; provided that no such public employee shall be exempt from prosecution or punishment for perjury committed while so testifying.” New Jersey Public Employees Immunity Statute, N. J. Stat. Ann. § 2A:81-17.2a2 (West 1976).</p>
</footnote>
<footnote label="2">
<p id="b522-8"> Portash has not contended that the indictment was based on information disclosed by or “derived” from his immunized testimony. Before trial he did move for dismissal of the indictment on two grounds. First, he argued that the course of dealings between himself and the prosecution established an agreement that he would not be prosecuted so long as he cooperated with the State. Second, he contended that he had impermis-sibly been forced to incriminate himself by providing certain employment records to the grand jury. The trial court rejected both arguments; neither is urged here.</p>
</footnote>
<footnote label="3">
<p id="b523-7"> We read the state-court opinion as resting its judgment unambiguously and exclusively on the Federal Constitution. The court said:</p>
<p id="b523-9"><em>“The </em>immunity device, however, will only be deemed a sufficient answer to a claim of privilege if the scope of immunity afforded is commensurate in all respects with the privilege against self-incrimination which it replaces. <em>United. States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">414 U. S. 338</a></span>, 346 . . . (1974); <em>Kastigar </em>v. <em>United States, </em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441</a></span>, 459 . . . (1972).” 151 N. J. Super., at 205, <span class="citation" data-id="1907630"><a href="/opinion/1907630/state-v-portash/#953" aria-description="Citation for case: State v. Portash">376 A. 2d, at 953</a></span>.</p>
<p id="b523-11">Both <em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">Calandra</a></span> </em>and <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>were, of course, federal constitutional decisions. The court discussed several other federal cases in the course of its opinion, and nowhere indicated any reliance on principles of state constitutional or common law.</p>
</footnote>
<footnote label="4">
<p id="b525-7"><em> Lefkowitz </em>v. <em>Newsome, </em><span class="citation" data-id="9426003"><a href="/opinion/109196/lefkowitz-v-newsome/" aria-description="Citation for case: Lefkowitz v. Newsome">420 U. S. 283</a></span>, was another case where provisions of state law allowed federal review that may not otherwise have been available. There, New York law allowed a defendant to appeal defeat of a motion to suppress even though he later pleaded guilty. The Court held that because the State recognized such a procedure, a state prisoner who had pleaded guilty could assert his Fourth and Fourteenth Amendment claim in a federal habeas corpus proceeding, even though federal habeas corpus relief would not generally have been available to one who had pleaded guilty.</p>
</footnote>
<footnote label="5">
<p id="b526-8"> A similar situation existed in <em>Wardius </em>v. <em>Oregon, </em><span class="citation" data-id="9425341"><a href="/opinion/108811/wardius-v-oregon/" aria-description="Citation for case: Wardius v. Oregon">412 U. S. 470</a></span>. The Court held in that case that state notice-of-alibi requirements could be enforced only if the State provided reciprocal discovery rights for the defendant. The defendant in that case had not given a notice of alibi. The State argued that he could not assert his constitutional claim, because he should have given his notice of alibi and then argued that the State had to grant him reciprocal discovery. The Court rejected that argument, and held that he need not give notice to raise his constitutional claim.</p>
</footnote>
<footnote label="6">
<p id="b527-8"><em> </em>The <em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">Murphy</a></span> </em>ease dealt with the problem of dual sovereignty. The issue was whether a State could grant constitutionally sufficient immunity if another jurisdiction could use the immunized testimony in a prosecution. The Court proceeded on the premise that a State is required to provide at least use immunity, and held that such immunity would have to be honored by the Federal Government. See <em>Kastigar </em>v. <em>United States, </em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#455" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 455-459</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b527-9"> See <em>Shapiro </em>v. <em>United States, </em><span class="citation" data-id="9420211"><a href="/opinion/104585/shapiro-v-united-states/" aria-description="Citation for case: Shapiro v. United States">335 U. S. 1</a></span>, 6 n. 4, for a list of the federal statutes that provided transactional immunity.</p>
</footnote>
<footnote label="8">
<p id="b528-6"> The Court in both the <em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">Harris</a></span> </em>and <em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">Hass</a></span> </em>cases relied on <em>Walder </em>v. <em>United States, </em><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span>, a case in which the Court held that the Fourth Amendment’s exclusionary rule does not prevent the use of unconstitutionally seized evidence to impeach a defendant’s credibility.</p>
</footnote>
<footnote label="9">
<p id="b529-7"> We express no view as to whether possibly truthful immunized testimony may be used in a subsequent false-declarations prosecution premised on an inconsistency between that testimony and later, nonimmunized, testimony. That question will be presented in <em>Dunn </em>v. <em>United States, </em>No. 77-6949, cert. granted, <span class="citation multiple-matches"><a href="/c/U.%20S./439/1045/">439 U. S. 1045</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b530-10"> There is discussion in the briefs of the parties regarding the admissibility of statements made by Portash during pre-indictment negotiations with the state prosecutors. We do not understand the opinion of the state appellate court to have dealt with this issue, and nothing said in this opinion bears on it.</p>
</footnote>
</opinion>
```

---
