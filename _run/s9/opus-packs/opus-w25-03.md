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

## GROUP: _overhaul2/lake/cases/zorn-v-linton--10813527.json  (`lake-record`, 1 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5aa7ac43972d3040", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "zorn-v-linton--10813527"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "zorn-v-linton--10813527", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — zorn-v-linton--10813527

```json
{
  "schema_version": "s2.v1",
  "record_id": "zorn-v-linton--10813527",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Zorn v. Linton",
    "case_name_short": "Zorn",
    "case_name_full": "",
    "input_case_name": "Zorn v. Linton",
    "court": "2026",
    "court_id": null,
    "court_level": null,
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": null,
    "docket": null,
    "cluster_id": 10813527,
    "lead_opinion_id": 11280281,
    "sibling_ids": [],
    "absolute_url": "/opinion/10813527/zorn-v-linton/",
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
      "note": "COURT FIX: SCOTUS per curiam No. 25-297, decided 2026-03-23 (607 U.S. ___; QI reversal of 2d Cir.). No S. Ct. page yet. (Search-floated '146 S. Ct. 926' rejected as fabricated.)",
      "legs": [
        {
          "source": "Cornell LII",
          "url": "https://www.law.cornell.edu/supremecourt/text/25-297",
          "cite": "No. 25-297, per curiam 2026-03-23, 607 U.S. ___"
        },
        {
          "source": "SCOTUSblog",
          "url": "https://www.dorsey.com/newsresources/publications/client-alerts/2026/3/march-23-supreme-court-update",
          "cite": "Zorn v. Linton, No. 25-297; no S. Ct. cite"
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
    "date_created": "2026-07-06T06:02:29Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T06:02:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T06:02:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T06:02:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T06:02:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — zorn-v-linton--10813527

```
                    Cite as: 607 U. S. ____ (2026)                 1

                              Per Curiam

SUPREME COURT OF THE UNITED STATES
          JACOB P. ZORN v. SHELA M. LINTON
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED
   STATES COURT OF APPEALS FOR THE SECOND CIRCUIT
                No. 25–297.   Decided March 23, 2026

   PER CURIAM.
   On the Governor’s inauguration day in Vermont, protest-
ers staged a sit-in at the state capitol. When the capitol
closed for the day, police officers told them that they would
be arrested for trespassing. They refused to leave. As of-
ficers removed the protesters one by one, Sergeant Jacob
Zorn asked Shela Linton to stand up and warned her that
he would eventually have to use force to remove her. She
refused to stand. Zorn took Linton’s arm, put it behind her
back, placed pressure on her wrist, and lifted her to her feet.
Linton sued Zorn for using excessive force, claiming that
the arrest left her with arm injuries and psychological dis-
orders. The Second Circuit held that Zorn was not entitled
to qualified immunity. We reverse.
                             I
  On January 8, 2015, Vermont hosted the inauguration for
Governor Peter Shumlin in the capitol.1 About 200 protest-
ers attended, and some of them staged a sit-in to demand
universal healthcare. Shela Linton joined them. She
planned to refuse to leave and anticipated being forcibly re-
moved. “That’s the point of the sit-in part of the protest,”
she later explained. Deposition of S. Linton in No. 5:18–cv–
5 (D Vt., June 3, 2022), ECF Doc. 74–4, p. 127.

——————
  1 Because this case comes here on Zorn’s motion for summary judg-

ment, we view the facts in the light most favorable to the nonmoving
party, Linton. City and County of San Francisco v. Sheehan, 575 U. S.
600, 603 (2015).
2                           ZORN v. LINTON

                               Per Curiam

   When the capitol closed to the public for the night, 29 pro-
testers remained in the legislative chamber, sitting on the
floor with their arms linked. At that point, police officers
explained that they would arrest the protesters for trespass
if they did not leave. The officers dealt with them one at a
time; some stood up and were escorted out of the chamber
without force, but others refused to stand and had to be
lifted to their feet or dragged out.
   After removing more than a dozen protesters, the officers
turned to Linton. Sergeant Jacob Zorn crouched down to
speak with her, but she remained seated with her arms in-
terlocked with those of her fellow protesters. As Linton pas-
sively resisted, Zorn unlinked her arm from another pro-
tester’s, put it behind her back in a rear wristlock, and
twisted her arm.2 Linton exclaimed “ ‘ ow, ow, ow,’ ” while
Zorn repeatedly implored her to “ ‘please stand up.’ ” App. to
Pet. for Cert. 47–48. After Linton responded, “ ‘I will not
stand up,’ ” Zorn told her that he would ask “ ‘one more
time’ ” and then would use more pain compliance. Id., at 48.
Linton refused, so Zorn placed pressure on her wrist and
lifted her up by her underarm. Linton yelled as she stood
up. Once on her feet, Linton continued to jerk her arms and
fell back to the floor. Zorn asked her to stand up again, and
when she did not, three officers picked her up by her arms
and legs and carried her outside. Linton alleged resulting
physical and psychological injuries including post-trau-
matic stress disorder.
   Linton sued Zorn under Rev. Stat. §1979, 42 U. S. C.
§1983, claiming that Zorn violated her Fourth Amendment
——————
  2 A rear wristlock is a technique that officers use to gain control over a

resistant person by gripping his wrist, placing it behind his back, and
bending it backward. See U.S. Dept. of Justice, Use of Force by Police:
Overview of National and Local Data 49 (Oct. 1999) (summarizing data
showing that “[w]hen the suspects used slight resistance, most incidents
involved officer use of verbal commands, handcuffing, or wrist/arm
locks”).
                  Cite as: 607 U. S. ____ (2026)            3

                           Per Curiam

right against excessive use of force. The District Court
granted summary judgment for Zorn after concluding that
he was entitled to qualified immunity. The District Court
reasoned that it was not clearly established at the time of
the encounter that, in these circumstances, lifting Linton
while putting pressure on her wrist violated the Fourth
Amendment.
  The Second Circuit reversed. It held that its decision in
Amnesty America v. West Hartford, 361 F. 3d 113 (2004),
clearly established that the “gratuitous” use of a rear wrist-
lock on a protester passively resisting arrest constitutes ex-
cessive force. 135 F. 4th 19, 35 (2025). It remanded for a
jury trial against Zorn. Judge Cabranes dissented. “The
case before us is not an exceptional case,” Judge Cabranes
reasoned, but “a routine arrest and removal.” Id., at 41.
                                II
   Government officials enjoy qualified immunity from suit
under §1983 unless their conduct violates clearly estab-
lished law. Rivas-Villegas v. Cortesluna, 595 U. S. 1, 5
(2021) (per curiam). “A right is clearly established when it
is ‘sufficiently clear that every reasonable official would
have understood that what he is doing violates that right.’ ”
Ibid. A right is not clearly established if existing precedent
does not place the constitutional question “ ‘beyond de-
bate.’ ” Ibid.
   To find that a right is clearly established, courts gener-
ally “need to identify a case where an officer acting under
similar circumstances . . . was held to have violated” the
Constitution. Escondido v. Emmons, 586 U. S. 38, 43
(2019) (per curiam) (internal quotation marks omitted).
The relevant precedent must define the right with a “high
degree of specificity,” so that “every reasonable official
would interpret it to establish the particular rule the plain-
tiff seeks to apply.” District of Columbia v. Wesby, 583 U. S.
48, 63 (2018) (internal quotation marks omitted).
4                         ZORN v. LINTON

                              Per Curiam

Principles stated generally, such as that “an officer may not
use unreasonable and excessive force,” do not suffice.
Kisela v. Hughes, 584 U. S. 100, 105 (2018) (per curiam). In
short, officers receive qualified immunity unless they could
have “read” the relevant precedent beforehand and
“know[ n]” that it proscribed their specific conduct. City
and County of San Francisco v. Sheehan, 575 U. S. 600, 616
(2015).
   The Second Circuit contravened these principles. Am-
nesty America did not clearly establish that Zorn’s specific
conduct violated the Fourth Amendment.3 Whether any
particular use of force violates the Fourth Amendment de-
pends on “the facts and circumstances of each particular
case,” Graham v. Connor, 490 U. S. 386, 396 (1989), includ-
ing whether the officer gave “warnings” before using force,
Barnes v. Felix, 605 U. S. 73, 80 (2025). In Amnesty Amer-
ica, the court considered a wide range of allegations of ex-
cessive force. The officers rammed a protester’s head into a
wall, dragged another protester across the ground, and
used rear wristlocks on two more protesters to lift them up
before throwing one of them to the ground. 361 F. 3d, at
123. Nothing indicated that the officers gave the protesters
any warning that they would use such force.
   Amnesty America did not hold that any of those actions
violated the Fourth Amendment, let alone all of them. In-
stead, it remanded for a jury trial because, while a “reason-
able jury could . . . find that the officers gratuitously in-
flicted pain,” it was also “entirely possible that a reasonable
jury would find . . . that the police officers’ use of force was
objectively reasonable given the circumstances.” Id., at 124
(emphasis added). Relevant here, Amnesty America even
relied on a decision approving the practice of warning

——————
  3 We assume without deciding that “controlling Circuit precedent” can

clearly establish law for qualified-immunity purposes. Rivas-Villegas v.
Cortesluna, 595 U. S. 1, 5 (2021) (per curiam).
                  Cite as: 607 U. S. ____ (2026)            5

                           Per Curiam

protesters and then using wristlocks to move them. Ibid.
(citing Forrester v. San Diego, 25 F. 3d 804, 807–808 (CA9
1994)).
   Reasonable officials would not “interpret [Amnesty Amer-
ica] to establish” that using a routine wristlock to move a
resistant protester after warning her, without more, vio-
lates the Constitution. Wesby, 583 U. S., at 63; see
Sheehan, 575 U. S., at 615–616. Zorn repeatedly warned
Linton that he would have to use more force if she did not
stand up, and when she did not do so, he used a wristlock
to bring Linton to her feet. See App. to Pet. for Cert. 47–49.
Amnesty America never “held” that such conduct alone “vi-
olated” the Fourth Amendment. Emmons, 586 U. S., at 43
(internal quotation marks omitted). If anything, it implied
the opposite. See Amnesty America, 361 F. 3d, at 124 (cit-
ing Forrester, 25 F. 3d, at 807–808). And its statement that
officers who had engaged in a wide range of aggressive con-
duct may have used excessive force did not “put [Zorn] on
notice that his specific conduct was unlawful.” Rivas-Ville-
gas, 595 U. S., at 6.
   The Second Circuit concluded otherwise by reading Am-
nesty America to establish the general principle “that the
gratuitous use of pain compliance techniques—such as a
rear-wristlock—on a protestor who is passively resisting ar-
rest constitutes excessive force.” 135 F. 4th, at 35 (case be-
low). But that principle, even assuming Amnesty America
established it, lacks the “high degree of specificity” needed
to make it “clear” to officers which actions violate the law.
Wesby, 583 U. S., at 63 (internal quotation marks omitted).
It does not “obviously resolve” whether using a rear wrist-
lock to move a noncompliant protester after repeated warn-
ings violates the Fourth Amendment, id., at 64, as it fails
to specify which circumstances make the use of force “gra-
tuitous.”
   Because the Second Circuit failed to identify a case where
an officer taking similar actions in similar circumstances
6                    ZORN v. LINTON

                       Per Curiam

“was held to have violated” the Constitution, Emmons, 586
U. S., at 43 (internal quotation marks omitted), Zorn was
entitled to qualified immunity. We grant his petition for
writ of certiorari and reverse the judgment of the Second
Circuit.
                                          It is so ordered.
                  Cite as: 607 U. S. ____ (2026)            1

                   SOTOMAYOR, J., dissenting

SUPREME COURT OF THE UNITED STATES
         JACOB P. ZORN v. SHELA M. LINTON
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED
   STATES COURT OF APPEALS FOR THE SECOND CIRCUIT
              No. 25–297.   Decided March 23, 2026

  JUSTICE SOTOMAYOR, with whom JUSTICE KAGAN and
JUSTICE JACKSON join, dissenting.
  Sergeant Jacob Zorn used a “ ‘pain compliance tech-
nique’ ” called a rear wristlock on Shela Linton, a nonviolent
protestor who was peacefully demonstrating at a sit-in in
the Vermont capitol. 135 F. 4th 19, 24–25 CA2 (2025). The
Second Circuit held that Zorn was not entitled to qualified
immunity on Linton’s Fourth Amendment excessive force
claim, at least at the summary judgment stage, because
prior Circuit precedent had clearly established that using a
rear wristlock against a nonviolent protestor would violate
the protestor’s constitutional rights. That decision was not
erroneous, and certainly not so clearly erroneous as to war-
rant the “extraordinary remedy of a summary reversal.”
Major League Baseball Players Assn. v. Garvey, 532 U. S.
504, 512–513 (2001) (Stevens, J., dissenting). I respectfully
dissent.
                              I
  Given that this case is at the summary judgment stage,
the Court must “view the evidence . . . in the light most fa-
vorable to” Linton, the nonmovant, “with respect to the cen-
tral facts of the case.” Tolan v. Cotton, 572 U. S. 650, 657
(2014) (per curiam). Before Sergeant Zorn’s interaction
with Linton, officers had arrested 15 or 16 demonstrators:
The “officers tapp[ed] some of the demonstrators’ shoulders
or sp[oke] briefly with them before the officers placed them
under arrest.” App. to Pet. for Cert. 44 (App.). “Some of the
arrestees voluntarily stood up after officers approached
2                      ZORN v. LINTON

                    SOTOMAYOR, J., dissenting

them,” while the “[o]fficers lifted the demonstrators who did
not stand up voluntarily and escorted, dragged, or carried
them out of the chamber.” Ibid. “Consistent with the con-
cept of a nonviolent sit-in protest, . . . none of [the demon-
strators] attacked the officers or used any form of violence.”
Id., at 45. One officer, Trooper Richardson, described the
“level of safety threat in the environment [as] ‘[v]ery low.’ ”
Ibid. (alteration in original).
   When Zorn and Richardson first approached Linton, they
“did not issue any ‘clear request or command,’ ” and the
“video evidence appears to indicate that” one of them said
only, “ ‘ma’am?’ ” Id., at 46. About five seconds later, Zorn
and Richardson unlinked Linton’s arms from the other de-
monstrators’ arms. Without any warning—indeed, without
saying another word to Linton—Zorn placed Linton’s left
arm into a rear wristlock by twisting her arm and shoulder,
“snapp[ing]” her wrist, and “ ‘forc[ing] it down and to the
rear.’ ” Id., at 47; Plaintiff’s Supp. Affidavit in No. 5:18–cv–
5 (D Vt.), ECF Doc. 74–3, p. 2. Linton immediately ex-
claimed, “ ‘ow, ow, ow!’ ” App. 47. Only then did Zorn in-
struct Linton to “ ‘please stand up.’ ” Id., at 48.
   Linton did not stand up, at which point Zorn further
twisted Linton’s arm. “Linton’s face contorted in pain as
she stated, ‘my arm!’ or ‘don’t twist my arm!’ ” Ibid. Zorn
asked Linton to stand up several more times. Linton re-
fused and replied: “ ‘You’re hurting me.’ ” Ibid. Zorn then
warned Linton: “ ‘I’m going to ask you one more time . . . and
then I will use more pain compliance.’ ” Ibid. Linton re-
peated that Zorn was “ ‘hurting’ ” her and did not move to
stand up. Id., at 49. Zorn then applied pressure to Linton’s
wrist and lifted her upward, causing Linton to “contor[t] her
face in pain and . . . scream very loudly.” Ibid. Zorn whis-
pered to her that “she should have called her legislator.”
Ibid.
   After being hauled to her feet, Linton collapsed back onto
the floor “due to pain and feeling weak.” Id., at 50. Zorn,
                  Cite as: 607 U. S. ____ (2026)              3

                    SOTOMAYOR, J., dissenting

Richardson, and a third officer “lifted” her “by her arms and
legs and carried her out of the House chamber” without fur-
ther use of a rear wristlock or any other pain-compliance
technique. Id., at 51. As a result of this event, Linton “suf-
fered permanent damage to her left wrist and shoulder” and
has been “diagnosed with post-traumatic stress disorder,
depression, and anxiety.” 135 F. 4th, at 25.
                                II
   Officers are not entitled to qualified immunity if “(1) they
violated a federal statutory or constitutional right, and
(2) the unlawfulness of their conduct was ‘clearly estab-
lished at the time.’ ” District of Columbia v. Wesby, 583
U. S. 48, 62–63 (2018). The Second Circuit correctly held
that summary judgment must be denied because a jury
could find that Zorn violated Linton’s clearly established
Fourth Amendment rights.
                              A
  Starting with the first prong of the qualified immunity
analysis, Linton contends that Zorn violated her Fourth
Amendment rights by using excessive force during her ar-
rest. Determining whether a given use of force is excessive
requires a “careful balancing of ‘ “the nature and quality of
the intrusion on the individual’s Fourth Amendment inter-
ests” ’ against the countervailing governmental interests at
stake.” Graham v. Connor, 490 U. S. 386, 396 (1989). The
inquiry depends on the “ ‘totality of the circumstances,’ ” “in-
cluding the severity of the crime at issue, whether the sus-
pect poses an immediate threat to the safety of the officers
or others, . . . whether [s]he is actively resisting arrest or
attempting to evade arrest by flight,” ibid., the “relation-
ship between the need for the use of force and the amount
of force used[, and] the extent of [her] injury,” Kingsley v.
Hendrickson, 576 U. S. 389, 397 (2015).
4                      ZORN v. LINTON

                    SOTOMAYOR, J., dissenting

    Here, the Second Circuit rightly concluded that a reason-
able jury could find that Zorn’s use of force was excessive in
violation of the Fourth Amendment. See 135 F. 4th, at 36.
First, the crime of trespass for which Linton was arrested
is not “ ‘particularly severe.’ ” Ibid. Second, it is undisputed
that the threat to safety posed by Linton was relatively low.
Trooper Richardson described the level of safety risk as
“ ‘[v]ery low.’ ” Ibid. The protestors also “passed through
security (and therefore must have been considered to be un-
armed), did not significantly outnumber police,” and were
“not accused of being volatile or violent.” Ibid. Third, it is
also undisputed that Linton “suffered permanent loss of
motion in her left wrist and shoulder as a result of the inci-
dent.” Ibid. Fourth, there is a material dispute of fact as
to whether Linton was actively resisting arrest, and a jury
reasonably could conclude that Linton was only passively
resisting and that her failure to comply was because she
was “in too much pain to do so.” Id., at 37. Finally, a jury
also reasonably could conclude that the use of pain compli-
ance was not “reasonably related to any need to use force.”
Id., at 38. The officers purportedly “did not use pain com-
pliance techniques in the arrests of . . . fellow protestors,”
and Linton contends that “the Vermont State Police use-of-
force policy does not suggest . . . us[ing] pain compliance
techniques in response to passive resistance.” Ibid. Fur-
ther, Zorn’s own expert stated that “the general police prac-
tice in response to passive resistance is ‘low level physical
contact . . . with little or no pain.’ ” Ibid. Taken together, a
jury could reasonably conclude that Zorn used excessive
force in violation of Linton’s Fourth Amendment rights.
                              B
   The second prong of the qualified immunity analysis asks
whether the “unlawfulness of [the official’s] conduct was
‘clearly established at the time,’ ” Wesby, 583 U. S., at 63,
which requires assessing whether the “contours of the right
                  Cite as: 607 U. S. ____ (2026)            5

                   SOTOMAYOR, J., dissenting

[are] sufficiently clear that a reasonable official would un-
derstand that what he is doing violates that right,” Ander-
son v. Creighton, 483 U. S. 635, 640 (1987). “[E]arlier cases
involving ‘fundamentally similar’ facts can provide espe-
cially strong support for a conclusion that the law is clearly
established,” Hope v. Pelzer, 536 U. S. 730, 741 (2002), but
there need not be a “ ‘ “case directly on point,” ’ ” White v.
Pauly, 580 U. S. 73, 79 (2017) (per curiam).
   In addition to the long-established principle that officers
may use only the “amount of force that is necessary in a
particular situation,” Graham, 490 U. S., at 397, the Second
Circuit’s prior case, Amnesty America v. West Hartford, 361
F. 3d 113 (CA2 2004), “clearly establish[ed] that the gratu-
itous use of pain compliance techniques—such as a rear-
wristlock—on a protestor who is passively resisting arrest
constitutes excessive force.” 135 F. 4th, at 35. In that case,
officers used multiple forms of force to arrest anti-abortion
protestors who had chained themselves together in front of
a women’s center. Amnesty America, 361 F. 3d, at 118. The
plaintiffs alleged that the officers had used excessive force
to remove them, including by using a rear wristlock and
other pain compliance techniques. Ibid. Two plaintiffs in
that case were treated much like Linton was: Officers
“lift[ed] and pull[ed]” them off the floor “by pressing their
wrists back against their forearms in a way that caused
lasting damage.” Id., at 123. The Circuit then held that,
under past cases, “allegations involving comparable
amounts of force used during the arrest of a nonviolent sus-
pect are sufficient to allow a reasonable factfinder to con-
clude that the force used was excessive.” Id., at 123–124.
   Amnesty America’s specific discussion of rear wristlocks
thus clearly established that using a rear wristlock against
a nonviolent, passively resisting protestor could constitute
excessive force. It therefore put Zorn on notice, to a “high
‘degree of specificity,’ ” Wesby, 583 U. S., at 63, that using
the same technique against a passively resisting protestor
6                      ZORN v. LINTON

                    SOTOMAYOR, J., dissenting

like Linton would expose him to liability for violating Lin-
ton’s Fourth Amendment rights.
                                 C
   The Court’s attempts to distinguish Amnesty America are
mistaken. It first claims that Amnesty America differs from
this case because the officers there did not give “any warn-
ing” to the protestors, while Zorn “repeatedly warned Lin-
ton” here. Ante, at 4–5. That distinction misrepresents
both cases. Amnesty America, in fact, did involve warnings:
It observed that the “police purportedly employed” the pain-
compliance techniques “only after they were unsuccessful
in verbally convincing protestors to move.” 361 F. 3d, at
119. By comparison, in this case, construing the evidence
in favor of Linton (as is required), Zorn “did not issue any
‘clear request or command’ ” before applying a rear wrist-
lock and began asking her to stand only after he had initi-
ated the wristlock. App. 46; see ECF Doc. 74–3, p. 2 (Linton
“was not given warning before [Zorn] initiated the use of
pain compliance”). Amnesty America thus involved “ ‘an of-
ficer acting under similar circumstances,’ ” Escondido v.
Emmons, 586 U. S. 38, 43 (2019) (per curiam), and put Zorn
on notice that his actions would violate established law.
   It is true that, after initiating the wristlock, Zorn warned
Linton that he would use “ ‘more pain compliance’ ” if she
did not stand up, App. 48, whereas the Amnesty America
opinion does not specify whether similar warnings were
given after the initiation of the wristlocks. If that is the
difference on which the majority relies, the majority is es-
sentially requiring Linton to find a factually identical case,
a requirement that this Court has repeatedly rejected. See,
e.g., Anderson, 483 U. S., at 640 (“This is not to say that an
official action is protected by qualified immunity unless the
very action in question has previously been held unlawful”);
Hope, 536 U. S., at 741 (explaining that “ ‘fundamentally
similar’ ” cases can be helpful but are not necessary).
                  Cite as: 607 U. S. ____ (2026)             7

                    SOTOMAYOR, J., dissenting

   The majority also suggests that Amnesty America consid-
ered a “wide range” of conduct, implying that it did not spe-
cifically address rear wristlocks like the one at issue here.
Ante, at 4. That, too, is inconsistent with the actual opinion,
which recognized that each plaintiff had “standing to assert
only those constitutional deprivations that they themselves
[were] alleged to have suffered” and specifically identified
the use of a rear wristlock against some passively resisting
protestors as “sufficient to allow a reasonable factfinder to
conclude that the force used was excessive.” 361 F. 3d, at
123–124, and n. 6.
   The Court next reasons that Amnesty America did not
clearly establish any law because it stated that while a “rea-
sonable jury could . . . find that the officers” used excessive
force, it was also “entirely possible that a reasonable jury
would find . . . that the police officers’ use of force was ob-
jectively reasonable given the circumstances and the plain-
tiffs’ resistance techniques.” Id., at 124; see ante, at 4–5.
These statements in Amnesty America, however, reflect
that the Second Circuit was reviewing a district court’s
grant of summary judgment in favor of the defendants
where there was factual uncertainty. In reversing the
grant of summary judgment, the Second Circuit held that if
the plaintiffs’ allegations were true, they would be “suffi-
cient to allow a reasonable factfinder to conclude that the
force used was excessive,” but it found that there were ma-
terial disputes on “issues of fact” that could not be resolved
at summary judgment. 361 F. 3d, at 123–124. Thus, when
Amnesty America stated that a reasonable jury could rule
for the officers, it was merely acknowledging the reality
that the jury might well resolve those material factual dis-
putes in favor of the defendants and find that the officers’
use of force, under the circumstances that truly occurred,
was not excessive. Id., at 124. That possibility, however,
does not change the fact that the Second Circuit held the
use of a wristlock could be excessive if events had
8                       ZORN v. LINTON

                     SOTOMAYOR, J., dissenting

transpired the way plaintiffs alleged they had in that case.
See 135 F. 4th, at 33. Indeed, the Second Circuit has long
held that “a vacatur of a grant of summary judgment and a
remand in light of the existence of genuine issues of mate-
rial fact” may clearly establish a constitutional violation,
id., at 34, and the dissent below agreed, id., at 40
(Cabranes, J., concurring in part and dissenting in part).
   At bottom, the majority’s analysis rests on the assump-
tion that the law can be clearly established only by factually
identical “ ‘ “case[s] directly on point,” ’ ” despite the Court’s
rejection of such a standard. White, 580 U. S., at 79. In-
stead, it is “enough that governing law places ‘the constitu-
tionality of the officer’s conduct beyond debate.’ ” Kisela v.
Hughes, 584 U. S. 100, 120 (2018) (SOTOMAYOR, J., dissent-
ing) (quoting Wesby, 583 U. S., at 63). Here, taking the facts
in the light most favorable to Linton, it is “beyond debate”
that Zorn’s use of pain compliance against the passively re-
sisting Linton was excessive. Accordingly, Zorn was not en-
titled to summary judgment based on qualified immunity.
                         *    *     *
   For the foregoing reasons, the Second Circuit did not err
in holding that Zorn is not entitled to qualified immunity at
this stage. At the very least, the decision below was not so
wrong as to warrant the “extraordinary remedy of a sum-
mary reversal.” Garvey, 532 U. S., at 512–513 (Stevens, J.,
dissenting). Relying on disputed facts, the Court today
simply disagrees with how the Second Circuit applied a cor-
rectly stated legal standard (the requirement that law
be established to “ ‘a high degree of specificity’ ” in the
qualified immunity analysis) to this particular set of facts.
135 F. 4th, at 32 (quoting Wesby, 583 U. S., at 63). That is
a routine, and nowhere near extraordinary, dispute that did
not require the Court’s intervention.
   In the past, I have noted the “troubling asymmetry” in
this Court’s “unflinching willingness ‘to summarily reverse
                  Cite as: 607 U. S. ____ (2026)            9

                   SOTOMAYOR, J., dissenting

courts for wrongly denying officers the protection of quali-
fied immunity’ but ‘rarely interven[ing] where courts
wrongly afford officers the benefit of qualified immunity.’ ”
Kisela, 584 U. S., at 121 (SOTOMAYOR, J., dissenting). This
case unfortunately represents a resurgence and perpetua-
tion of this “one-sided approach to qualified immunity” that
“transforms the doctrine into an absolute shield for law en-
forcement officers, gutting the deterrent effect of the Fourth
Amendment.” Ibid. The majority today gives officers li-
cense to inflict gratuitous pain on a nonviolent protestor
even where there is no threat to officer safety or any other
reason to do so. That is plainly inconsistent with the Fourth
Amendment’s fundamental guarantee that officers may
only use “the amount of force that is necessary” under the
circumstances. Graham, 490 U. S., at 396. Therefore, I re-
spectfully dissent.

```

---

## GROUP: content/cases/A Quantity of Copies of Books v. Kansas.md  (`case`, 5 assertions)

### content_page

```
---
title: A Quantity of Copies of Books v. Kansas
type: case
citation: "378 U.S. 205 (1964)"
parallel_cite: "84 S. Ct. 1723; 12 L. Ed. 2d 809"
neutral_cite: 1964 U.S. LEXIS 823
court: U.S.
court_level: scotus
circuit: ""
year: 1964
date_decided: 1964-06-22
docket: 449
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
  opinion_url: "https://www.courtlistener.com/opinion/106878/a-quantity-of-copies-of-books-v-kansas/"
  cluster_id: 106878
  opinion_id: null
  identity_checked: true
lake:
  record_id: A Quantity of Copies of Books v. Kansas
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Particularity]]"
    role: Historical / origin
related:
  - "[[Stanford v. Texas]]"
  - "[[The Warrant Requirement]]"
tags:
  - case
  - fourth-amendment
  - first-amendment
  - warrant-requirement
  - seizure
  - obscenity
  - prior-restraint
  - historical
holding: "Seizing every copy of allegedly obscene books under a warrant issued on an ex parte finding, with no prior adversary hearing on obscenity, is constitutionally deficient — expressive material may not be swept up in a general seizure without the heightened, hearing-first warrant procedure the First and Fourteenth Amendments require."
---

# A Quantity of Copies of Books v. Kansas

*378 U.S. 205 (1964)* (No. 449) · Supreme Court of the United States · **Historical** · Treatment: **Historical — foundational origin (⚪ unverified, pending S9)**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the treatment framing below is authored orientation, not machine-certified. Identity cluster 106878 → 378 U.S. 205, decided 1964-06-22; Rule quote string-matched to the CL opinion text 2026-07-07. -->

## Background
A Kansas prosecutor presented a judge with seven allegedly obscene novels. On that [[Common Legal Terms#ex-parte|ex parte]] showing, the judge issued a warrant, and the sheriff seized 1,715 copies of 31 titles from a wholesale distributor (P-K News Service) — all before any hearing on whether the books were in fact obscene. The distributor moved to quash and return the books, arguing that the mass seizure of presumptively protected expression, without a prior adversary hearing, was unconstitutional.

## Issue
Whether a warrant authorizing the seizure of all copies of books, issued without a prior adversary hearing on the question of obscenity, satisfies the constitutional constraints on searches and seizures of expressive material.

## Rule
Building on *[[Marcus v. Search Warrant|Marcus v. Search Warrant of Property]]* (1961), the plurality (Brennan, J.) held that expressive material demands a warrant procedure sensitive to First Amendment values: the judge may not authorize a wholesale seizure that functions as a prior restraint without first affording the party an adversary hearing on obscenity. "We therefore conclude that in not first affording P-K an adversary hearing, the procedure leading to the seizure order was constitutionally deficient." — 378 U.S. at 211. ^pin-211

## Application
The vice was procedural: the seizure took a large inventory of books out of circulation on nothing more than a judge's [[Common Legal Terms#ex-parte|ex parte]] look at a handful of them, suppressing the distribution of material that had not been — and might never be — adjudicated obscene. Ordinary probable cause to believe an item is contraband is not enough when the item is a book; the Constitution requires a hearing before, not after, the expression is seized en masse.

## Conclusion
The judgment of the Supreme Court of Kansas was **reversed**; the seizure procedure was constitutionally deficient. Brennan, J., announced the judgment of the Court in a [[Common Legal Terms#plurality-opinion|plurality opinion]].

## Treatment & subsequent history
**Historical — a foundational origin, not overruled.** *A Quantity of Books* is an early anchor of the rule that seizing expressive material requires a warrant procedure more protective than the ordinary probable-cause showing — a prior adversary hearing or prompt judicial superintendence rather than a discretionary sweep. The doctrine it helped originate was refined the same decade and after in the *[[Marcus v. Search Warrant|Marcus]]*–*[[Stanford v. Texas|Stanford]]*–*[[Heller v. New York|Heller]]*–*[[Roaden v. Kentucky|Roaden]]* line, which governs today. It is rendered here as **history** — a doctrinal antecedent — because its treatment has not been machine-verified.

*Status note (⚪):* authored from a CourtListener-verified identity stub; renders under the ⚪ banner until S9 promotion. The successor pages *[[Marcus v. Search Warrant]]* and *[[Roaden v. Kentucky]]* are not yet in the corpus (queued in later authoring waves); they are named in plain text here to avoid dangling links.

## Appears on
- [[Particularity]] — *Historical / origin*

## Sources
- [*A Quantity of Copies of Books v. Kansas*, 378 U.S. 205 (1964)](https://www.courtlistener.com/opinion/106878/a-quantity-of-copies-of-books-v-kansas/) — pinpoint: 211 (plurality; Brennan, J.); Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "dd035817dbff2e31", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "378 U.S. 205 (1964)", "court": "U.S.", "neutral_cite": "1964 U.S. LEXIS 823", "official_citation_present": true, "parallel_cite": "84 S. Ct. 1723; 12 L. Ed. 2d 809", "title": "A Quantity of Copies of Books v. Kansas", "year": "1964"}}
{"assertion_id": "9e772178034ba164", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Seizing every copy of allegedly obscene books under a warrant issued on an ex parte finding, with no prior adversary hearing on obscenity, is constitutionally deficient — expressive material may not be swept up in a general seizure without the heightened, hearing-first warrant procedure the First and Fourteenth Amendments require.", "title": "A Quantity of Copies of Books v. Kansas"}}
{"assertion_id": "a02970dbba796599", "dimension": "support", "kind": "home_role", "locator": {"home": "Particularity"}, "payload": {"home": "Particularity", "role": "Historical / origin", "title": "A Quantity of Copies of Books v. Kansas"}}
{"assertion_id": "734943050fb024d0", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "A Quantity of Copies of Books v. Kansas", "varies_by_point": "false"}}
{"assertion_id": "fa916b82e1af0213", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "A Quantity of Copies of Books v. Kansas"}}
```

### lake record — A Quantity of Copies of Books v. Kansas

```json
{
  "schema_version": "s2.v1",
  "record_id": "A Quantity of Copies of Books v. Kansas",
  "status": "under_review",
  "identity": {
    "case_name": "A Quantity of Copies of Books v. Kansas",
    "case_name_short": "Copies of Books",
    "case_name_full": "A QUANTITY OF COPIES OF BOOKS Et Al. v. KANSAS",
    "input_case_name": "Quantity of Copies of Books v. Kansas",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1964-06-22",
    "year": 1964,
    "docket": "449",
    "cluster_id": 106878,
    "lead_opinion_id": 9422858,
    "sibling_ids": [],
    "absolute_url": "/opinion/106878/a-quantity-of-copies-of-books-v-kansas/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "378 U.S. 205",
      "volume": "378",
      "reporter": "U.S.",
      "page": "205",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "84 S. Ct. 1723",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1723",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 809",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "809",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1964 U.S. LEXIS 823",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "823",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "378 U.S. 205",
        "volume": "378",
        "reporter": "U.S.",
        "page": "205",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 S. Ct. 1723",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1723",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 809",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "809",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1964 U.S. LEXIS 823",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "823",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "378 U.S. 205",
    "official_selection": {
      "court_class": "scotus",
      "selected": "378 U.S. 205",
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
    "date_created": "2026-07-07T13:26:03Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:26:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:26:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:26:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:26:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "quantity-of-copies-of-books-v-kansas--106878",
      "to_record_id": "A Quantity of Copies of Books v. Kansas",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — A Quantity of Copies of Books v. Kansas

```
<opinion type="majority">
<author id="b236-9">Mr. Justice Brennan</author>
<p id="A4UH">announced the judgment of the Court and delivered an opinion in which</p>
<judges id="Ada">The Chief Justice, Mr. Justice White, and Mr. Justice Goldberg join.</judges>
<p id="b236-10">Under a Kansas statute authorizing the seizure of allegedly obscene books before an adversary determina<page-number citation-index="1" label="207">*207</page-number>tion of their obscenity and, after that determination, their destruction by burning or otherwise,<footnotemark>1</footnotemark> the Attorney General of Kansas obtained an order from the District Court of Geary County directing the sheriff of the county to seize and impound, pending hearing, copies of certain <page-number citation-index="1" label="208">*208</page-number>paperback novels at the place of business of P-K News Service, Junction City, Kansas. After hearing, the court entered a second order directing the sheriff to destroy the 1,715 copies of 31 novels which had been seized. The Kansas Supreme Court held that the procedures met constitutional requirements and affirmed the District Court’s order. <span class="citation" data-id="2610549"><a href="/opinion/2610549/state-v-a-quantity-of-copies-of-books/" aria-description="Citation for case: State v. a Quantity of Copies of Books">191 Kan. 13</a></span>, <span class="citation" data-id="2610549"><a href="/opinion/2610549/state-v-a-quantity-of-copies-of-books/" aria-description="Citation for case: State v. a Quantity of Copies of Books">379 P. 2d 254</a></span>. Probable jurisdiction was noted, <span class="citation multiple-matches"><a href="/c/U.%20S./375/919/">375 U. S. 919</a></span>. We conclude that the procedures followed in issuing the warrant for the seizure of the books, and authorizing their impounding pending hearing, were constitutionally insufficient because they did not adequately safeguard against the suppression of nonobscene books. For this reason we think the judgment must be reversed. Therefore we do not reach, and intimate no view upon, the appellants’ contention that the Kansas courts erred in holding that the novels are obscene.</p>
<p id="b238-5">Section 4 of the Kansas statute requires the filing of a verified Information stating only that “upon information and belief . . . there is [an] . . . obscene book . . . located within his county.” The State Attorney General went further, however, and filed an Information identifying by title 59 novels, and stating that “each of said books [has] been published as 'This is an original Nightstand Book.’ ” He also filed with the Information copies of seven novels published under that caption, six of which were named by title in the Information; particular passages in the seven novels were marked with penciled notations or slips of paper. Although also not expressly required by the statute, the district judge, on application of the Attorney General, conducted a 45-min-ute <em>ex parte </em>inquiry during which he “scrutinized” the seven books; at the conclusion of this examination, he stated for the record that they “appear to be obscene literature as defined” under the Kansas statute “and give this Court reasonable grounds to believe that any paper-<page-number citation-index="1" label="209">*209</page-number>backed publication carrying the following: 'This is an original Night Stand book’ would fall within the same category . . . He issued a warrant which authorized the sheriff to seize only the particular novels identified by title in the Information. When the warrant was executed on the date it was issued, only 31 of the titles were found on P-K’s premises. All copies of such titles, however, 1,715 books in all, were seized and impounded. At the hearing held 10 days later pursuant to a notice included in the warrant, P-K made a motion to quash the Information and the warrant on the ground, among others, that the procedure preceding the seizure was constitutionally deficient. The claim was that by failing first to afford P-K a hearing on the question whether the books were obscene, the procedure “operates as a prior restraint on the circulation and dissemination of books” in violation of the constitutional restrictions against abridgment of freedom of speech and press. The motion was denied, and following a final hearing held about seven weeks after the seizure (the hearing date was continued on motion of P-K), the court held that all 31 novels were obscene and ordered the sheriff to stand ready to destroy the 1,715 copies on further order.</p>
<p id="b239-4">The steps taken beyond the express requirements of the statute were thought by the Attorney General to be necessary under our decision in <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717</a></span>, decided a few weeks before the Information was filed. <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span> </em>involved a proceeding under a strikingly similar Missouri search and seizure statute and implementing rule of court. See <span class="citation multiple-matches"><a href="/c/U.%20S./367/719/">367 U. S. 719</a></span>, at notes 2, 3. In <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span> </em>the warrant gave the police virtually unlimited authority to seize any publications which they considered to be obscene, and was issued on a verified complaint lacking any specific description of the publications to be seized, and without prior submission of any publications whatever to the judge issuing the warrant. <page-number citation-index="1" label="210">*210</page-number>We reversed a judgment directing the destruction of the copies of 100 publications held to be obscene, holding that, even assuming that they were obscene, the procedures leading to their condemnation were constitutionally deficient for lack of safeguards to prevent suppression of nonobscene publications protected by the Constitution.</p>
<p id="b240-5">It is our view that since the warrant here authorized the sheriff to seize all copies of the specified titles, and since P-K was not afforded a hearing on the question of the obscenity even of' the seven novels before the warrant issued, the procedure was likewise constitutionally deficient.<footnotemark>2</footnotemark> This is the teaching of <em>Kingsley Books, Inc., </em>v. <em>Brown, </em><span class="citation" data-id="9421490"><a href="/opinion/105544/kingsley-books-inc-v-brown/" aria-description="Citation for case: Kingsley Books, Inc. v. Brown">354 U. S. 436</a></span>. See <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span>, </em>at pp. 734-738. The New York injunctive procedure there sustained does not afford <em>ex parte </em>relief but postpones all injunctive relief until “both sides have had an opportunity to be heard.” <em>Tenney </em>v. <em>Liberty News Distributors, </em>13 App. Div. 2d 770, 215 N. Y. S. 2d 663, 664. In <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span> </em>we explicitly said that <em>Kingsley Books </em>“does not support the proposition that the State may impose the extensive restraints imposed here on the distribution of these publications prior to an adversary proceeding on the issue of obscenity, irrespective of whether or not the material is legally obscene.” <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#735" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S., at 735-736</a></span>. A seizure of all copies of the named titles is indeed more repressive than an injunction preventing further sale of the books. State regulation of obscenity must “conform to procedures that will ensure against the curtailment of constitutionally protected expression, which is often separated from obscenity only by a dim and uncertain line.” <em>Bantam Books, Inc., </em>v. <em>Sullivan, </em><span class="citation" data-id="9422525"><a href="/opinion/106530/bantam-books-inc-v-sullivan/#66" aria-description="Citation for case: Bantam Books, Inc. v. Sullivan">372 U. S. 58, 66</a></span>; the Constitution requires a procedure “designed to focus searchingly on the question of obscenity,” <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span>, </em>p. 732. We therefore <page-number citation-index="1" label="211">*211</page-number>conclude that in not first affording P-K an adversary hearing, the procedure leading to the seizure order was constitutionally deficient. What we said of the Missouri procedure, <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#736" aria-description="Citation for case: Marcus v. Search Warrant of Property"><em>id., </em>at 736-737</a></span>, also fits the Kansas procedure employed to remove these books from circulation:</p>
<blockquote id="b241-4">“. . . there is no doubt that an effective restraint— indeed the most effective restraint possible — was imposed prior to hearing on the circulation of the publications in this case, because all copies on which the [sheriff] could lay [his] hands were physically removed . . . from the premises of the wholesale distributor. An opportunity ... to circulate the [books] . . . and then raise the claim of nonob-scenity by way of defense to a prosecution for doing so was never afforded these appellants because the copies they possessed were taken away. Their ability to circulate their publications was left to the chance of securing other copies, themselves subject to mass seizure under other such warrants. The public’s opportunity to obtain the publications was thus determined by the distributor’s readiness and ability to outwit the police by obtaining and selling other copies before they in turn could be seized. In addition to its unseemliness, we do not believe that this kind of enforced competition affords a reasonable likelihood that nonobscene publications, entitled to constitutional protection, will reach the public. A distributor may have every reason to believe that a publication is constitutionally protected and will be so held after judicial hearing, but his belief is unavailing as against the contrary <em>[ex </em>parte] judgment [pursuant to which the sheriff] . . . seizes it from him.”</blockquote>
<p id="b241-5">It is no answer to say that obscene books are contraband, and that consequently the standards governing searches and seizures of allegedly obscene books should <page-number citation-index="1" label="212">*212</page-number>not differ from those applied with respect to narcotics, gambling paraphernalia and other contraband. We rejected that proposition in <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span>. </em>We said, <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S., at 730</a></span>-731:</p>
<blockquote id="b242-4">“The Missouri Supreme Court’s assimilation of obscene literature to gambling paraphernalia or other contraband for purposes of search and seizure does not therefore answer the appellants’ constitutional claim, but merely restates the issue whether obscenity may be treated in the same way. The authority to the police officers under the warrants issued in this case, broadly to seize ‘obscene . . . publications,’ poses problems not raised by the warrants to seize ‘gambling implements’ and ‘all intoxicating liquors’ involved in the cases cited by the Missouri Supreme Court. 334 S. W. 2d, at 125. For the use of these warrants implicates questions whether the procedures leading to their issuance and surrounding their execution were adequate to avoid suppression of constitutionally protected publications. ‘. . . [T]he line between speech unconditionally guaranteed and speech which may legitimately be regulated, suppressed, or punished is finely drawn. . . . The separation of legitimate from illegitimate speech calls for . . . sensitive tools . . . .’ <em>Speiser </em>v. <em>Randall, </em><span class="citation" data-id="9421696"><a href="/opinion/105751/speiser-v-randall/#525" aria-description="Citation for case: Speiser v. Randall">357 U. S. 513, 525</a></span>. It follows that, under the Fourteenth Amendment, a State is not free to adopt whatever procedures it pleases for dealing with obscenity as here involved without regard to the possible consequences for constitutionally protected speech.”</blockquote>
<p id="b242-5">See also <em>Smith </em>v. <em>California, </em><span class="citation" data-id="9421895"><a href="/opinion/105972/smith-v-california/#152" aria-description="Citation for case: Smith v. California">361 U. S. 147, 152-153</a></span>.</p>
<p id="b242-6">Nor is the order under review saved because, after all 1,715 copies were seized and removed from circulation, P-K News Service was afforded a full hearing on the <page-number citation-index="1" label="213">*213</page-number>question of the obscenity of the novels. For if seizure of books precedes an adversary, determination of their obscenity, there is danger of abridgment of the right of the public in a free society to unobstructed circulation of non-obscene books. <em>Bantam Books </em>v. <em><span class="citation" data-id="9422525"><a href="/opinion/106530/bantam-books-inc-v-sullivan/" aria-description="Citation for case: Bantam Books, Inc. v. Sullivan">Sullivan, supra;</a></span> Roth </em>v. <em>United States, </em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">354 U. S. 476</a></span>; <em>Marcus </em>v. <em>Search <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Warrant, supra;</a></span> Smith </em>v. <em><span class="citation" data-id="9421895"><a href="/opinion/105972/smith-v-california/" aria-description="Citation for case: Smith v. California">California, supra.</a></span> </em>Here, as in <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span>, </em>“since a violation of the Fourteenth Amendment infected the proceedings, in order to vindicate appellants’ constitutional rights” <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#738" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S., at 738</a></span>, the judgment resting on a finding of obscenity must be reversed.</p>
<p id="b243-4">
<em>Reversed.</em>
</p>
<p id="b243-5">Opinion of</p>
<author id="A12">Mr. Justice Black,</author>
<judges id="AgG">with whom Mr. Justice Douglas joins.</judges>
<p id="b243-6">The Kansas State Court judgment here under review orders that 1,715 copies of 31 novels be burned or otherwise destroyed. This book-burning judgment was based upon findings by the trial judge that “the core [of the books] would seem to be that of sex, with the plot, if any, being subservient thereto,” that the “dominant purpose [of the books] was calculated to effectively incite sexual desires” and that “they would have this effect on the average person residing in this community . . . .” Relying on these findings and this Court’s holding in <em>Roth </em>v. <em>United States, </em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">354 U. S. 476</a></span>, the trial court held that the books “are not entitled to the . . . protection” of the First- Amendment to the Constitution. The State Supreme Court affirmed on the same grounds.</p>
<p id="b243-7">This Court now reverses. I concur in the judgment of reversal but do not find it necessary to consider the procedural questions. Compare <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#738" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717, 738</a></span> (concurring opinion). The Kansas courts may have been right to rely upon the Court’s <em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">Roth</a></span> </em>holding in ordering these books burned or <page-number citation-index="1" label="214">*214</page-number>otherwise destroyed. For reasons stated in the <em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">Roth</a></span> </em>case in a dissent by Mr. Justice Douglas, 354 U. S., at 508, in which I joined, I think the <em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">Roth</a></span> </em>case was wrongly decided. It is my belief, as stated in that dissent by Mr. Justice Douglas, in my concurring opinions in <em>Smith </em>v. <em>California, </em><span class="citation" data-id="9421895"><a href="/opinion/105972/smith-v-california/#155" aria-description="Citation for case: Smith v. California">361 U. S. 147, 155</a></span>, and <em>Kingsley International Pictures Corp. </em>v. <em>Regents, </em><span class="citation" data-id="9421871"><a href="/opinion/105937/kingsley-international-pictures-corp-v-regents-of-the-university/#690" aria-description="Citation for case: Kingsley International Pictures Corp. v. Regents of the...">360 U. S. 684, 690</a></span>, and in my dissent in <em>Beauharnais </em>v. <em>Illinois, </em><span class="citation" data-id="9420729"><a href="/opinion/105001/beauharnais-v-illinois/#267" aria-description="Citation for case: Beauharnais v. Illinois">343 U. S. 250, 267</a></span>, which Mr. Justice Douglas joined, that the Kansas statute ordering the burning of these books is in plain violation of the unequivocal prohibition of the First Amendment, made applicable to the States by the Fourteenth, against “abridging the freedom of speech, or of the press.”</p>
<p id="b244-4">Because of my belief that both <em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">Roth</a></span> </em>and <em>Beau-harnais </em>draw blueprints showing how to avoid the First Amendment’s guarantee of freedoms of speech and press, I would overrule both those cases as well as reverse the judgment here.</p>
<footnote label="1">
<p id="b237-4"> The statute is Kan. Gen. Stat. §21-1102 <em>et seq. </em>(Supp. 1961). Section 1 of Kan. Laws 1961, c. 186 (§ 21-1102), constitutes the selling or distribution of obscene materials (obscenity is defined in § 1 (b)) a criminal misdemeanor punishable by fine or imprisonment or both. Section 4 (§ 21 — 1102c) provides for the search and seizure procedure here involved:</p>
<blockquote id="b237-5">“Whenever any district, county, common pleas, or city court judge or justice of the peace shall receive an information or complaint, signed and verified upon information and belief by the county attorney or the attorney general, stating there is any prohibited lewd, lascivious or obscene book, magazine, newspaper, writing, pamphlet, ballad, printed paper, print, picture, motion pictures, drawing, photograph, publication or other thing, as set out in section 1 [21-1102] (a) of this act, located within his county, it shall be the duty of such judge to forthwith issue his search warrant directed to the sheriff or any other duly constituted peace officer to seize and bring before said judge or justice such a prohibited item or items. Any peace officer seizing such item or items as hereinbefore described shall leave a copy of such warrant with any manager, servant, employee or other person appearing or acting in the capacity of exercising any control over the premises where such item or items are found or, if no person is there found, such warrant may be posted by said peace officer in a conspicuous place upon the premises where found and said warrant shall serve as notice to all interested persons of a hearing to be had at a time not less than ten (10) days after such seizure. At such hearing, the judge or justice issuing the warrant shall determine whether or not the item or items so seized and brought before him pursuant to said warrant were kept upon the premises where found in violation of any of the provisions of this act. If he shall so find, he shall order such item or items to be destroyed by the sheriff or any duly constituted peace officer by burning or otherwise, at such time as such judge shall order, and satisfactory return thereof made to him: <em>Provided, however, </em>Such item or items shall not be destroyed so long as they may be needed as evidence in any criminal prosecution.”</blockquote>
</footnote>
<footnote label="2">
<p id="b240-6"> P-K News Service also asserts that its constitutional right against unreasonable searches and seizures was violated. The result here makes it unnecessary to pass upon this contention.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Abel v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Abel v. United States"
type: case
citation: "362 U.S. 217 (1960)"
parallel_cite: "80 S. Ct. 683; 4 L. Ed. 2d 668"
neutral_cite: 1960 U.S. LEXIS 1412
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1960
date_decided: 1960-03-28
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1960-03-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Abel v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106021/abel-v-united-states/"
  cluster_id: 106021
  opinion_id: 106021
  identity_checked: true
homes:
  - page: "[[Abandonment]]"
    role: "Key — Anchor"
related: ["[[Hester v. United States]]", "[[California v. Greenwood]]"]
aliases: ["Abel v. US"]
tags: ["case", "fourth-amendment", "abandonment"]
holding: "Items left in a hotel-room wastebasket after the guest paid up and **vacated** the room were abandoned ('bona vacantia'); their warrantless seizure was lawful."
lake:
  record_id: Abel v. United States
  status: verified
  projected_at: 2026-07-06
---

# Abel v. United States

*362 U.S. 217 (1960)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
INS agents arrested the petitioner — a Soviet intelligence officer using the alias "Martin Collins" — at a New York City hotel on an administrative deportation warrant. Immediately after the petitioner paid his bill and checked out, an FBI agent searched the vacated room with the hotel management's consent and recovered, from the room's wastepaper basket, a hollowed-out pencil and a block of wood containing a "cipher pad." These and other items were introduced against him in an espionage prosecution.

## Issue
Whether the warrantless search of a hotel room — and seizure of items the guest had discarded in the wastebasket — after the guest paid his bill and vacated the room violated the Fourth Amendment.

## Rule
No. Once the guest vacated the room, the hotel regained the exclusive right to possession and could consent to the search; and the items left in the wastebasket were abandoned, so their warrantless seizure was lawful. The search "was entirely lawful, although undertaken without a warrant," because "at the time of the search petitioner had vacated the room. The hotel then had the exclusive right to its possession, and the hotel management freely gave its consent that the search be made." — 362 U.S. at 241. ^pin-241

As to the discarded items: "So far as the record shows, petitioner had abandoned these articles. He had thrown them away. So far as he was concerned, they were *bona vacantia.* There can be nothing unlawful in the Government's appropriation of such abandoned property." — *Id.* at 241. ^pin-241a

## Application
On these facts the FBI agent did not enter until after the petitioner had paid his bill and given up the room, so the hotel — not the petitioner — controlled the space and validly consented to the entry; and the pencil and cipher-pad block had been thrown into the wastebasket as the petitioner packed to leave, marking them as abandoned. Seizing the abandoned articles without a warrant was therefore lawful, and their use in evidence did not offend the Fourth Amendment.

## Conclusion
The warrantless search of the vacated room and seizure of the abandoned wastebasket items were lawful; the evidence was admissible and the conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No subsequent negative treatment. *Abel* remains a foundational statement of the abandoned-property (*bona vacantia*) principle — that one who relinquishes property retains no Fourth Amendment interest in it.
- Related applications of the same abandonment principle: [[California v. Greenwood]] (no expectation of privacy in curbside garbage); [[Hester v. United States]] (open-fields / discarded containers).

## Appears on
- [[Abandonment]] — *Key — Anchor*

## Sources
- *Abel v. United States*, 362 U.S. 217 (1960) — https://www.courtlistener.com/opinion/106021/abel-v-united-states/ — pinpoint: 241.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ff1d706e7aed47cc", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "362 U.S. 217 (1960)", "court": "U.S. Supreme Court", "neutral_cite": "1960 U.S. LEXIS 1412", "official_citation_present": true, "parallel_cite": "80 S. Ct. 683; 4 L. Ed. 2d 668", "title": "Abel v. United States", "year": "1960"}}
{"assertion_id": "67232916ac3f9497", "dimension": "support", "kind": "home_role", "locator": {"home": "Abandonment"}, "payload": {"home": "Abandonment", "role": "Key — Anchor", "title": "Abel v. United States"}}
{"assertion_id": "8aa76f35ee508d29", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Items left in a hotel-room wastebasket after the guest paid up and **vacated** the room were abandoned ('bona vacantia'); their warrantless seizure was lawful.", "title": "Abel v. United States"}}
{"assertion_id": "794339253ee14c2c", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1960-03-28", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Abel v. United States", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Abel v. United States", "varies_by_point": "false"}}
{"assertion_id": "d6ed209b6d3327f2", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Abel v. United States"}}
```

### lake record — Abel v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Abel v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Abel v. United States",
    "case_name_short": "Abel",
    "case_name_full": "ABEL, Alias MARK, Alias COLLINS, Alias GOLDFUS, v. UNITED STATES",
    "input_case_name": "Abel v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1960-03-28",
    "year": 1960,
    "docket": null,
    "cluster_id": 106021,
    "lead_opinion_id": 106021,
    "sibling_ids": [
      106021,
      9421949,
      9421950,
      9421951
    ],
    "absolute_url": "/opinion/106021/abel-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8947572,
        "score": 10,
        "case_name": "Abel v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "362 U.S. 217",
      "volume": "362",
      "reporter": "U.S.",
      "page": "217",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "80 S. Ct. 683",
        "volume": "80",
        "reporter": "S. Ct.",
        "page": "683",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 L. Ed. 2d 668",
        "volume": "4",
        "reporter": "L. Ed. 2d",
        "page": "668",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1960 U.S. LEXIS 1412",
        "volume": "1960",
        "reporter": "U.S. LEXIS",
        "page": "1412",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "362 U.S. 217",
        "volume": "362",
        "reporter": "U.S.",
        "page": "217",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 S. Ct. 683",
        "volume": "80",
        "reporter": "S. Ct.",
        "page": "683",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 L. Ed. 2d 668",
        "volume": "4",
        "reporter": "L. Ed. 2d",
        "page": "668",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1960 U.S. LEXIS 1412",
        "volume": "1960",
        "reporter": "U.S. LEXIS",
        "page": "1412",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "362 U.S. 217",
    "official_selection": {
      "court_class": "scotus",
      "selected": "362 U.S. 217",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-241",
      "page": null,
      "quote": "These and other items were introduced against him in an espionage prosecution. ## Issue Whether the warrantless search of a hotel room \u2014 and seizure of items the guest had discarded in the wastebasket \u2014 after the guest paid his bill and vacated the room violated the Fourth Amendment. ## Rule No. Once the guest vacated the room, the hotel regained the exclusive right to possession and could consent to the search; and the items left in the wastebasket were abandoned, so their warrantless seizure was lawful. The search",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-241a",
      "page": null,
      "quote": "So far as the record shows, petitioner had abandoned these articles. He had thrown them away. So far as he was concerned, they were *bona vacantia.* There can be nothing unlawful in the Government's appropriation of such abandoned property.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1960-03-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Abel v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "People v. Konther",
          "cluster_id": 10874455,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ryan Mendoza",
          "cluster_id": 10771114,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Op. Atty. Gen. 3a; 390a6",
          "cluster_id": 10754685,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Bryant",
          "cluster_id": 10747664,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People of Guam v. Joseph Quichocho Taimanglo II (aka Joseph Quichocho Taimanglo; aka Baby Joe; aka Joseph Quintanilla Taimanglo II)",
          "cluster_id": 10713502,
          "cite": [
            "2025 Guam 7"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Charles Aaron Amble and John Joseph Mandracchia",
          "cluster_id": 10604543,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Charles Aaron Amble and John Joseph Mandracchia",
          "cluster_id": 10604323,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri v. Theresa O'Connor",
          "cluster_id": 10631514,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri v. Timothy R. Fernandez",
          "cluster_id": 10631444,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Jerry Lynn Burns",
          "cluster_id": 9388341,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Stark v. State",
          "cluster_id": 9371579,
          "cite": [
            "171 Idaho 541",
            "524 P.3d 43"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Terrance Baker",
          "cluster_id": 9371555,
          "cite": [
            "58 F.4th 1109"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Malagerio",
          "cluster_id": 8243624,
          "cite": [
            "49 F.4th 911"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jeremiah Edwards",
          "cluster_id": 6469003,
          "cite": [
            "34 F.4th 570"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Alan James Kuuttila",
          "cluster_id": 5290136,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bortree",
          "cluster_id": 5030192,
          "cite": [
            "2021 Ohio 2873"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Nicholas Dean Wright",
          "cluster_id": 5290145,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Nicholas Dean Wright",
          "cluster_id": 4894883,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Nicholas Dean Wright",
          "cluster_id": 4893114,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gerardo Gonzalez v. Ice",
          "cluster_id": 4784538,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dixon",
          "cluster_id": 4805743,
          "cite": [
            "947 N.W.2d 563",
            "306 Neb. 853"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Franz Grey",
          "cluster_id": 4756521,
          "cite": [
            "959 F.3d 1166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Quentin Ferebee",
          "cluster_id": 4747521,
          "cite": [
            "957 F.3d 406"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jose Leonel Oseguera-Viera v. State",
          "cluster_id": 4685787,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dontae Small",
          "cluster_id": 4684957,
          "cite": [
            "944 F.3d 490"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Holley",
          "cluster_id": 4658152,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Thomas",
          "cluster_id": 4647637,
          "cite": [
            "2019 IL App (1st) 170474"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Martha Ann McClancy",
          "cluster_id": 4647175,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Scottize Danyelle Brown",
          "cluster_id": 4658982,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Joseph Watson v. Patrick Pearson",
          "cluster_id": 4635243,
          "cite": [
            "928 F.3d 507"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Scottize Danyelle Brown",
          "cluster_id": 4635121,
          "cite": [
            "930 N.W.2d 840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Valles",
          "cluster_id": 4609283,
          "cite": [
            "2019 ND 108",
            "925 N.W.2d 404"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Chavez v. Carmichael",
          "cluster_id": 4550937,
          "cite": [
            "822 S.E.2d 131",
            "262 N.C. App. 196"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City of El Cenizo, Texas v. State of Texas",
          "cluster_id": 4496244,
          "cite": [
            "890 F.3d 164"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City of El Cenizo, Texas v. State of Texas",
          "cluster_id": 4476977,
          "cite": [
            "885 F.3d 332"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hull v. Town of Newtown",
          "cluster_id": 4453742,
          "cite": [
            "174 A.3d 174",
            "327 Conn. 402"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City of El Cenizo v. Texas",
          "cluster_id": 7326561,
          "cite": [
            "264 F. Supp. 3d 744"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Bruce Wayne Sutton",
          "cluster_id": 4393282,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Joseph Durward Watson, II - Dissenting Opinion",
          "cluster_id": 4382006,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Byrd",
          "cluster_id": 4319283,
          "cite": [
            "2016 Ohio 7670"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hayward",
          "cluster_id": 4319281,
          "cite": [
            "2016 Ohio 7671"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jackson",
          "cluster_id": 4319280,
          "cite": [
            "2016 Ohio 7669"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Samalia",
          "cluster_id": 4242519,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jeffrey B. Melling",
          "cluster_id": 3191981,
          "cite": [
            "160 Idaho 209",
            "370 P.3d 412",
            "2016 WL 1355089",
            "2016 Ida. App. LEXIS 46"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Traci Sheppard Schroeder v. State",
          "cluster_id": 3072000,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Williford",
          "cluster_id": 2766778,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Borders",
          "cluster_id": 2726708,
          "cite": [
            "236 N.C. App. 149",
            "762 S.E.2d 490",
            "2014 N.C. App. LEXIS 975"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Olvera v. City of Modesto",
          "cluster_id": 7308114,
          "cite": [
            "38 F. Supp. 3d 1162",
            "2014 WL 3858362",
            "2014 U.S. Dist. LEXIS 108452"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Lee",
          "cluster_id": 2674606,
          "cite": [
            "2014 IL App (1st) 130507"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Richard K. Ntim Jr.",
          "cluster_id": 2679977,
          "cite": [
            "2013 ME 80",
            "76 A.3d 370",
            "2013 WL 5201022",
            "2013 Me. LEXIS 81"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jerry Nelson, Jr.",
          "cluster_id": 2981963,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jerry Nelson, Jr.",
          "cluster_id": 1036714,
          "cite": [
            "725 F.3d 615",
            "92 Fed. R. Serv. 95",
            "2013 WL 4007652",
            "2013 U.S. App. LEXIS 16278"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Irizarry",
          "cluster_id": 858053,
          "cite": [
            "72 M.J. 100",
            "2013 WL 1628381",
            "2013 CAAF LEXIS 383"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "LAVAN v. City of Los Angeles",
          "cluster_id": 2113714,
          "cite": [
            "797 F. Supp. 2d 1005",
            "2011 U.S. Dist. LEXIS 67332",
            "2011 WL 2516484"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Wynn",
          "cluster_id": 2694594,
          "cite": [
            "2011 Ohio 1832"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Orval Roger Miller Jr. v. State",
          "cluster_id": 2954290,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Orval Roger Miller Jr. v. State",
          "cluster_id": 2954289,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Miller v. State",
          "cluster_id": 2280953,
          "cite": [
            "335 S.W.3d 847",
            "2011 Tex. App. LEXIS 1752",
            "2011 WL 832126"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Eaton",
          "cluster_id": 2393809,
          "cite": [
            "707 S.E.2d 642",
            "210 N.C. App. 142",
            "2011 N.C. App. LEXIS 319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Marshall",
          "cluster_id": 2273474,
          "cite": [
            "319 S.W.3d 352",
            "2010 Ky. LEXIS 182",
            "2010 WL 3374171"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Eddie Carlisle",
          "cluster_id": 3004320,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Carlisle",
          "cluster_id": 2530423,
          "cite": [
            "614 F.3d 750",
            "2010 U.S. App. LEXIS 17026",
            "2010 WL 3155876"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Maurice Levie v. ESL Partners, L.P.",
          "cluster_id": 152710,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Nesbitt",
          "cluster_id": 2397780,
          "cite": [
            "699 S.E.2d 368",
            "305 Ga. App. 28",
            "2010 Fulton County D. Rep. 2538",
            "2010 Ga. App. LEXIS 656"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Williamson v. State",
          "cluster_id": 1917905,
          "cite": [
            "993 A.2d 626",
            "413 Md. 521",
            "2010 Md. LEXIS 175"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. VASQUEZ-ARENIVAR",
          "cluster_id": 1255552,
          "cite": [
            "779 N.W.2d 117",
            "18 Neb. Ct. App. 265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Howe",
          "cluster_id": 1887352,
          "cite": [
            "986 A.2d 631",
            "159 N.H. 366"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Club Retro LLC v. Hilton",
          "cluster_id": 66452,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
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
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 5143869,
          "cite": [
            "962 A.2d 973",
            "2009 ME 6",
            "2009 Me. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Assistance of Counsel in Removal Proceedings (I)",
          "cluster_id": 6236949,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Crist",
          "cluster_id": 1974111,
          "cite": [
            "627 F. Supp. 2d 575",
            "2008 U.S. Dist. LEXIS 84980",
            "2008 WL 4682806"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Smith v. State",
          "cluster_id": 1360884,
          "cite": [
            "667 S.E.2d 65",
            "284 Ga. 304",
            "2008 Fulton County D. Rep. 2964",
            "2008 Ga. LEXIS 753"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Parson",
          "cluster_id": 2584947,
          "cite": [
            "44 Cal. 4th 332",
            "187 P.3d 1",
            "79 Cal. Rptr. 3d 269",
            "2008 Cal. LEXIS 8243"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 2414367,
          "cite": [
            "556 F. Supp. 2d 985",
            "2008 WL 2251248"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Martin v. Mukasey",
          "cluster_id": 170353,
          "cite": [
            "517 F.3d 1201",
            "2008 U.S. App. LEXIS 4155",
            "2008 WL 501113"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Duplessis",
          "cluster_id": 1794695,
          "cite": [
            "974 So. 2d 65",
            "2007 WL 4554325"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bruce v. Beary",
          "cluster_id": 77819,
          "cite": [
            "498 F.3d 1232",
            "2007 U.S. App. LEXIS 21283",
            "2007 WL 2492101"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tylan Lucas",
          "cluster_id": 3042966,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Lucas",
          "cluster_id": 1362932,
          "cite": [
            "499 F.3d 769",
            "2007 U.S. App. LEXIS 20076",
            "2007 WL 2386580"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Shawn Patrick Bryan v. State",
          "cluster_id": 2914087,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. McKinney",
          "cluster_id": 1392222,
          "cite": [
            "637 S.E.2d 868",
            "361 N.C. 53",
            "2006 N.C. LEXIS 1298"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Sutherland",
          "cluster_id": 3135291,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Sutherland",
          "cluster_id": 2036519,
          "cite": [
            "860 N.E.2d 178",
            "223 Ill. 2d 187",
            "307 Ill. Dec. 524"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hudson v. State",
          "cluster_id": 2173357,
          "cite": [
            "205 S.W.3d 600",
            "2006 Tex. App. LEXIS 7699",
            "2006 WL 2507311"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Sedrick Roshun Decoud, Jr., A/K/A Rab Shaun Dee Merced and Shaun Vance, United States of America v. Kendra Trice, United States of America v. Audra Israel",
          "cluster_id": 795230,
          "cite": [
            "456 F.3d 996",
            "70 Fed. R. Serv. 893",
            "2006 U.S. App. LEXIS 19599"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Decoud",
          "cluster_id": 3038224,
          "cite": [
            "456 F.3d 996",
            "2006 WL 2136603"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Edward J. Zakrzewski v. James McDonough",
          "cluster_id": 77399,
          "cite": [
            "455 F.3d 1254",
            "2006 U.S. App. LEXIS 17484",
            "2006 WL 1911328"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Marzook",
          "cluster_id": 2434582,
          "cite": [
            "435 F. Supp. 2d 778",
            "2006 U.S. Dist. LEXIS 41898",
            "2006 WL 1735322"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sherman",
          "cluster_id": 1129307,
          "cite": [
            "931 So. 2d 286",
            "2006 WL 860652"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Clifton M. Menton v. State",
          "cluster_id": 2891732,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Clifton M. Menton v. State",
          "cluster_id": 2891731,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Clifton M. Menton v. State",
          "cluster_id": 2891730,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Adron Thomas v. State",
          "cluster_id": 2916555,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Washington v. State",
          "cluster_id": 1694079,
          "cite": [
            "922 So. 2d 145",
            "2005 WL 435119"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Stevenson",
          "cluster_id": 2968064,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Lee Ronald Stevenson",
          "cluster_id": 789072,
          "cite": [
            "396 F.3d 538",
            "2005 U.S. App. LEXIS 1558",
            "2005 WL 221869"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Nieves",
          "cluster_id": 2402008,
          "cite": [
            "861 A.2d 62",
            "383 Md. 573",
            "2004 Md. LEXIS 722"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fulani",
          "cluster_id": 3014175,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ibrahim Hamud Fulani",
          "cluster_id": 786196,
          "cite": [
            "368 F.3d 351",
            "2004 U.S. App. LEXIS 9896",
            "2004 WL 1119635"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Murph Omar McNaughton v. State",
          "cluster_id": 2882131,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "UNITED STATES v. WILLIAM SOTO-BEN\u00cdQUEZ, UNITED STATES OF AMERICA v. JUAN SOTO-RAM\u00cdREZ, UNITED STATES OF AMERICA v. EDUARDO ALICEA-TORRES, UNITED STATES OF AMERICA v. RAMON FERN\u00c1NDEZ-MALAV\u00c9, UNITED STATES OF AMERICA v. CARMELO VEGA-PACHECO, UNITED STATES OF AMERICA v. ARMANDO GARC\u00cdA-GARC\u00cdA, UNITED STATES OF AMERICA v. JOSE LUIS DE LE\u00d3N MAYSONET, UNITED STATES OF AMERICA v. RENE GONZALEZ-AYALA, UNITED STATES OF AMERICA v. JUAN ENRIQUE CINTR\u00d3N-CARABALLO, UNITED STATES OF AMERICA v. MIGUEL VEGA-COL\u00d3N, UNITED STATES OF AMERICA v. MIGUEL VEGA-COSME",
          "cluster_id": 784866,
          "cite": [
            "356 F.3d 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Samuel Mondragon-Garcia v. State",
          "cluster_id": 2913182,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mondragon-Garcia v. State",
          "cluster_id": 1466707,
          "cite": [
            "129 S.W.3d 674",
            "2004 Tex. App. LEXIS 444",
            "2004 WL 67625"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dominguez, Carlos Martinez v. State",
          "cluster_id": 2835714,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dominguez v. State",
          "cluster_id": 1384895,
          "cite": [
            "125 S.W.3d 755",
            "2003 Tex. App. LEXIS 10758",
            "2003 WL 22999897"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "UNITED STATES v. WILLIAM SOTO-BENIQUEZ, UNITED STATES OF AMERICA v. JUAN SOTO-RAMIREZ, UNITED STATES OF AMERICA v. EDUARDO ALICEA-TORRES, UNITED STATES OF AMERICA v. RAMON FERNANDEZ-MALAV\u00c9, UNITED STATES OF AMERICA v. CARMELO VEGA-PACHECO, UNITED STATES OF AMERICA v. ARMANDO GARCIA-GARCIA, UNITED STATES OF AMERICA v. JOSE LUIS DE LEON MAYSONET, UNITED STATES OF AMERICA v. RENE GONZALEZ-AYALA, UNITED STATES OF AMERICA v. JUAN ENRIQUE CINTRON-CARABALLO, UNITED STATES OF AMERICA v. MIGUEL VEGA-COLON, UNITED STATES OF AMERICA v. MIGUEL VEGA-COSME",
          "cluster_id": 784248,
          "cite": [
            "350 F.3d 131",
            "2003 U.S. App. LEXIS 23655"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Soto-Beniquez",
          "cluster_id": 200734,
          "cite": [
            "356 F.3d 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jackson",
          "cluster_id": 2572005,
          "cite": [
            "360 F. Supp. 2d 24",
            "2003 U.S. Dist. LEXIS 27347",
            "2003 WL 24008994"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cedric E. Wingfield v. State",
          "cluster_id": 2844500,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cedric E. Wingfield v. State",
          "cluster_id": 2844499,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cedric E. Wingfield v. State",
          "cluster_id": 2844774,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cedric E. Wingfield v. State",
          "cluster_id": 2844773,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ahern",
          "cluster_id": 200539,
          "cite": [
            "68 F. App'x 209"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Martin v. State",
          "cluster_id": 1129477,
          "cite": [
            "931 So. 2d 736",
            "2003 WL 21246587"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Reed Mouton v. State",
          "cluster_id": 2881730,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mouton v. State",
          "cluster_id": 1634836,
          "cite": [
            "101 S.W.3d 686",
            "2003 Tex. App. LEXIS 2022",
            "2003 WL 845498"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Netto",
          "cluster_id": 6578659,
          "cite": [
            "438 Mass. 686",
            "783 N.E.2d 439",
            "2003 Mass. LEXIS 171"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Mosby",
          "cluster_id": 1773883,
          "cite": [
            "94 S.W.3d 410",
            "2003 Mo. App. LEXIS 37",
            "2003 WL 138232"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Willie Roy Woods v. State",
          "cluster_id": 2877945,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ballew v. Walker",
          "cluster_id": 7295232,
          "cite": [
            "50 F. App'x 24"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Mallory",
          "cluster_id": 6587233,
          "cite": [
            "56 Mass. App. Ct. 153",
            "775 N.E.2d 764",
            "2002 Mass. App. LEXIS 1218"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Maria Alicia Walker v. State",
          "cluster_id": 2920179,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Matthew Downing v. State of Texas",
          "cluster_id": 2915536,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Donald Lee Morrison v. State",
          "cluster_id": 2920639,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Morrison v. State",
          "cluster_id": 1662228,
          "cite": [
            "71 S.W.3d 821",
            "2002 Tex. App. LEXIS 1427",
            "2002 WL 254027"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Robinson",
          "cluster_id": 2140668,
          "cite": [
            "767 N.E.2d 638",
            "97 N.Y.2d 341",
            "741 N.Y.S.2d 147"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Preston v. State",
          "cluster_id": 2318723,
          "cite": [
            "784 A.2d 601",
            "141 Md. App. 54",
            "2001 Md. App. LEXIS 165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Rosenthal",
          "cluster_id": 6586859,
          "cite": [
            "52 Mass. App. Ct. 707",
            "755 N.E.2d 817",
            "2001 Mass. App. LEXIS 930"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Powell v. State",
          "cluster_id": 1946311,
          "cite": [
            "776 A.2d 700",
            "139 Md. App. 582",
            "2001 Md. App. LEXIS 126"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brixen & Christopher Architects, P.C. v. State",
          "cluster_id": 2599638,
          "cite": [
            "2001 UT App 210",
            "29 P.3d 650",
            "424 Utah Adv. Rep. 45",
            "2001 Utah App. LEXIS 49",
            "2001 WL 721723"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. McDermott",
          "cluster_id": 7089721,
          "cite": [
            "245 F.3d 133",
            "2001 WL 303634"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mitchell v. State",
          "cluster_id": 1852299,
          "cite": [
            "792 So. 2d 192",
            "2001 WL 302751"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. James J. McDermott Jr., Kathryn B. Gannon, Also Known as Kathryn B. Gannon-Akahoshi, Also Known as Marylin Star, and Anthony P. Pomponio",
          "cluster_id": 772671,
          "cite": [
            "245 F.3d 133",
            "56 Fed. R. Serv. 1086",
            "2001 U.S. App. LEXIS 5277"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Bin Laden",
          "cluster_id": 2457303,
          "cite": [
            "132 F. Supp. 2d 198",
            "2001 U.S. Dist. LEXIS 26300",
            "2001 WL 135858"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Citizen v. State",
          "cluster_id": 1947523,
          "cite": [
            "39 S.W.3d 367",
            "2001 Tex. App. LEXIS 1021",
            "2001 WL 126125"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Utecht, Kenneth L.",
          "cluster_id": 2994836,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth L. Utecht",
          "cluster_id": 771880,
          "cite": [
            "238 F.3d 882",
            "87 A.F.T.R.2d (RIA) 681",
            "2001 U.S. App. LEXIS 1060",
            "2001 WL 65066"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Lisenbee",
          "cluster_id": 2585425,
          "cite": [
            "13 P.3d 947",
            "116 Nev. 1124",
            "116 Nev. Adv. Rep. 117",
            "2000 Nev. LEXIS 132"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Ayala",
          "cluster_id": 2594572,
          "cite": [
            "6 P.3d 193",
            "99 Cal. Rptr. 2d 532",
            "24 Cal. 4th 243",
            "2000 WL 1210378"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Ayala",
          "cluster_id": 5593049,
          "cite": [
            "24 Cal. 243"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Pallone",
          "cluster_id": 2221553,
          "cite": [
            "2000 WI 77",
            "613 N.W.2d 568",
            "236 Wis. 2d 162",
            "2000 Wisc. LEXIS 415"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
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
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grant",
          "cluster_id": 2211483,
          "cite": [
            "614 N.W.2d 848",
            "2000 Iowa App. LEXIS 6",
            "2000 WL 504538"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "James Hollingsworth v. State",
          "cluster_id": 2863127,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hollingsworth v. State",
          "cluster_id": 2119689,
          "cite": [
            "15 S.W.3d 586",
            "2000 Tex. App. LEXIS 2033",
            "2000 WL 328041"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Beardslee",
          "cluster_id": 7079506,
          "cite": [
            "197 F.3d 378",
            "1999 WL 983680"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Florence Martha Beardslee, United States of America, Plaintiff-Appellant-Cross-Appellee v. Florence Martha Beardslee, Defendant-Appellee-Cross-Appellant",
          "cluster_id": 766868,
          "cite": [
            "197 F.3d 378",
            "99 Daily Journal DAR 11201",
            "99 Cal. Daily Op. Serv. 8756",
            "53 Fed. R. Serv. 494",
            "1999 U.S. App. LEXIS 28102"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Powell v. State",
          "cluster_id": 1660846,
          "cite": [
            "796 So. 2d 404",
            "1999 WL 982399"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Brauch",
          "cluster_id": 2614645,
          "cite": [
            "984 P.2d 703",
            "133 Idaho 215",
            "1999 Ida. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "James Edmond and Joell Palmer, on Their Own Behalf and on Behalf of a Class of Those Similarly Situated v. Stephen Goldsmith, in His Official Capacity as Mayor of the City of Indianapolis, Indiana City of Indianapolis, Indiana and Unknown Members of the Indianapolis Police Department",
          "cluster_id": 765145,
          "cite": [
            "183 F.3d 659",
            "1999 U.S. App. LEXIS 15010"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In Re Subpoenas Duces Tecum Nos. A99-0001, A99-0002, A99-0003 & A99-0004",
          "cluster_id": 2497025,
          "cite": [
            "51 F. Supp. 2d 726",
            "1999 U.S. Dist. LEXIS 10471",
            "1999 WL 451796"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Padilla",
          "cluster_id": 1441534,
          "cite": [
            "728 A.2d 279",
            "321 N.J. Super. 96"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Wilmington",
          "cluster_id": 1954189,
          "cite": [
            "729 A.2d 1160",
            "1999 Pa. Super. 66",
            "1999 Pa. Super. LEXIS 824"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gudema v. Nassau County",
          "cluster_id": 7075002,
          "cite": [
            "163 F.3d 717",
            "1998 WL 887048"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gudema v. Nassau County",
          "cluster_id": 760182,
          "cite": [
            "163 F.3d 717",
            "1998 U.S. App. LEXIS 31650"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Miller",
          "cluster_id": 2406906,
          "cite": [
            "26 F. Supp. 2d 415",
            "1998 U.S. Dist. LEXIS 15970",
            "1998 WL 709469"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gore",
          "cluster_id": 7069910,
          "cite": [
            "154 F.3d 34",
            "1998 WL 515720"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gore",
          "cluster_id": 757557,
          "cite": [
            "154 F.3d 34",
            "1998 U.S. App. LEXIS 20493"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "William Gerald Mitchell v. State of Mississippi",
          "cluster_id": 863672,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Holland v. State",
          "cluster_id": 1902684,
          "cite": [
            "713 A.2d 364",
            "122 Md. App. 532",
            "1998 Md. App. LEXIS 140"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Perkins",
          "cluster_id": 2023862,
          "cite": [
            "582 N.W.2d 876",
            "1998 Minn. LEXIS 388",
            "1998 WL 351051"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Reeves v. State",
          "cluster_id": 1534910,
          "cite": [
            "969 S.W.2d 471",
            "1998 Tex. App. LEXIS 2649",
            "1998 WL 220453"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Partee v. State",
          "cluster_id": 1997221,
          "cite": [
            "708 A.2d 1113",
            "121 Md. App. 237",
            "1998 Md. App. LEXIS 102"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Benjamin Armstrong v. State",
          "cluster_id": 2861573,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Armstrong v. State",
          "cluster_id": 2377535,
          "cite": [
            "966 S.W.2d 150",
            "1998 Tex. App. LEXIS 1841",
            "1998 WL 132941"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Holbrooks",
          "cluster_id": 1082984,
          "cite": [
            "983 S.W.2d 697",
            "1998 Tenn. Crim. App. LEXIS 175",
            "1998 WL 57527"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Bennett",
          "cluster_id": 1194986,
          "cite": [
            "17 Cal. 4th 373",
            "949 P.2d 947",
            "98 Daily Journal DAR 1155",
            "98 Cal. Daily Op. Serv. 863",
            "70 Cal. Rptr. 2d 850",
            "1998 Cal. LEXIS 28"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Larry Andre Sanders",
          "cluster_id": 748848,
          "cite": [
            "130 F.3d 1316",
            "1997 WL 762704"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Larry A. Sanders",
          "cluster_id": 3019806,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Neal v. State",
          "cluster_id": 1846732,
          "cite": [
            "731 So. 2d 609",
            "1997 WL 501462"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Maude C. Clarke",
          "cluster_id": 3018375,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Maude C. Clarke, Also Known as Tina Clarke, Also Known as Angela",
          "cluster_id": 739120,
          "cite": [
            "110 F.3d 612",
            "1997 U.S. App. LEXIS 6488",
            "1997 WL 160155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Calvin Porter",
          "cluster_id": 3018006,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Calvin Porter",
          "cluster_id": 736260,
          "cite": [
            "107 F.3d 582",
            "1997 U.S. App. LEXIS 3043",
            "1997 WL 71289"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "46 Fed. R. Evid. Serv. 240, 10 Fla. L. Weekly Fed. C 621 United States of America v. Ralph E. Brazel, Jr., Charles Hubbard, Norman L. Burgess, United States of America v. Sharvonne McKinnon United States of America v. Levine Justice Archer, A.K.A. Jamaican Joe, A.K.A. Joe, Willie Jefferson, Marlon McNealy A.K.A. Man",
          "cluster_id": 731292,
          "cite": [
            "102 F.3d 1120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Baldwin",
          "cluster_id": 1671891,
          "cite": [
            "686 So. 2d 682",
            "1996 WL 728697"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Lashawn Y. McDonald",
          "cluster_id": 729772,
          "cite": [
            "100 F.3d 1320",
            "1996 U.S. App. LEXIS 30224",
            "1996 WL 673246"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Stanberry v. State",
          "cluster_id": 2314219,
          "cite": [
            "684 A.2d 823",
            "343 Md. 720",
            "1996 Md. LEXIS 116"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Ienco",
          "cluster_id": 723976,
          "cite": [
            "92 F.3d 564",
            "45 Fed. R. Serv. 415",
            "1996 U.S. App. LEXIS 20183",
            "1996 WL 452248"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Richards",
          "cluster_id": 1840075,
          "cite": [
            "552 N.W.2d 197",
            "1996 Minn. LEXIS 444",
            "1996 WL 400300"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Roberts",
          "cluster_id": 1446652,
          "cite": [
            "928 F. Supp. 910",
            "1996 U.S. Dist. LEXIS 8590",
            "1996 WL 335492"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Clarke",
          "cluster_id": 2294285,
          "cite": [
            "925 F. Supp. 1433",
            "1996 U.S. Dist. LEXIS 6989",
            "1996 WL 268070"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Whren v. United States",
          "cluster_id": 118036,
          "cite": [
            "135 L. Ed. 2d 89",
            "116 S. Ct. 1769",
            "517 U.S. 806",
            "1996 U.S. LEXIS 3720"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Soca v. State",
          "cluster_id": 1657165,
          "cite": [
            "673 So. 2d 24",
            "1996 WL 196588"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Timothy Dwayne Austin",
          "cluster_id": 705154,
          "cite": [
            "66 F.3d 1115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Crittenden v. State",
          "cluster_id": 1506576,
          "cite": [
            "899 S.W.2d 668",
            "1995 Tex. Crim. App. LEXIS 57",
            "1995 WL 296354"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Walker",
          "cluster_id": 2264802,
          "cite": [
            "879 F. Supp. 1087",
            "1995 U.S. Dist. LEXIS 3297",
            "1995 WL 106386"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Perkins",
          "cluster_id": 1684979,
          "cite": [
            "871 F. Supp. 801",
            "1995 U.S. Dist. LEXIS 91",
            "1995 WL 7515"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lake County Mental Health Department v. Susan T.",
          "cluster_id": 2611902,
          "cite": [
            "884 P.2d 988",
            "8 Cal. 4th 1005",
            "36 Cal. Rptr. 2d 40",
            "94 Cal. Daily Op. Serv. 9381",
            "94 Daily Journal DAR 17330",
            "63 U.S.L.W. 2392",
            "1994 Cal. LEXIS 6211"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rockett v. State",
          "cluster_id": 2394789,
          "cite": [
            "890 S.W.2d 235",
            "318 Ark. 831",
            "1994 Ark. LEXIS 699"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Florez",
          "cluster_id": 1685213,
          "cite": [
            "871 F. Supp. 1411",
            "1994 U.S. Dist. LEXIS 19976",
            "1994 WL 728462"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jamal Deshon Segars",
          "cluster_id": 675779,
          "cite": [
            "31 F.3d 655",
            "1994 U.S. App. LEXIS 19724",
            "1994 WL 395230"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Schneckloth v. Bustamonte",
          "cluster_id": 108800,
          "cite": [
            "36 L. Ed. 2d 854",
            "93 S. Ct. 2041",
            "412 U.S. 218",
            "1973 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chimel v. California",
          "cluster_id": 107979,
          "cite": [
            "23 L. Ed. 2d 685",
            "89 S. Ct. 2034",
            "395 U.S. 752",
            "1969 U.S. LEXIS 1166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schmerber v. California",
          "cluster_id": 107262,
          "cite": [
            "16 L. Ed. 2d 908",
            "86 S. Ct. 1826",
            "384 U.S. 757",
            "1966 U.S. LEXIS 1129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. O'Brien",
          "cluster_id": 107701,
          "cite": [
            "20 L. Ed. 2d 672",
            "88 S. Ct. 1673",
            "391 U.S. 367",
            "1968 U.S. LEXIS 2910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Camara v. Municipal Court of City and County of San Francisco",
          "cluster_id": 107473,
          "cite": [
            "18 L. Ed. 2d 930",
            "87 S. Ct. 1727",
            "387 U.S. 523",
            "1967 U.S. LEXIS 1254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Robinson",
          "cluster_id": 108893,
          "cite": [
            "38 L. Ed. 2d 427",
            "94 S. Ct. 467",
            "414 U.S. 218",
            "1973 U.S. LEXIS 21",
            "66 Ohio Op. 2d 202"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warden, Maryland Penitentiary v. Hayden",
          "cluster_id": 107465,
          "cite": [
            "18 L. Ed. 2d 782",
            "87 S. Ct. 1642",
            "387 U.S. 294",
            "1967 U.S. LEXIS 2753"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ker v. California",
          "cluster_id": 106641,
          "cite": [
            "10 L. Ed. 2d 726",
            "83 S. Ct. 1623",
            "374 U.S. 23",
            "1963 U.S. LEXIS 2473",
            "24 Ohio Op. 2d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elkins v. United States",
          "cluster_id": 106107,
          "cite": [
            "4 L. Ed. 2d 1669",
            "80 S. Ct. 1437",
            "364 U.S. 206",
            "1960 U.S. LEXIS 1989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Watson",
          "cluster_id": 109352,
          "cite": [
            "46 L. Ed. 2d 598",
            "96 S. Ct. 820",
            "423 U.S. 411",
            "1976 U.S. LEXIS 121"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Tyler",
          "cluster_id": 109874,
          "cite": [
            "56 L. Ed. 2d 486",
            "98 S. Ct. 1942",
            "436 U.S. 499",
            "1978 U.S. LEXIS 97"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Santana",
          "cluster_id": 109504,
          "cite": [
            "49 L. Ed. 2d 300",
            "96 S. Ct. 2406",
            "427 U.S. 38",
            "1976 U.S. LEXIS 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Poe v. Ullman",
          "cluster_id": 106282,
          "cite": [
            "6 L. Ed. 2d 989",
            "81 S. Ct. 1752",
            "367 U.S. 497",
            "1961 U.S. LEXIS 1953"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. Lopez-Mendoza",
          "cluster_id": 111265,
          "cite": [
            "82 L. Ed. 2d 778",
            "104 S. Ct. 3479",
            "468 U.S. 1032",
            "1984 U.S. LEXIS 156",
            "52 U.S.L.W. 5190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lopez v. United States",
          "cluster_id": 106622,
          "cite": [
            "10 L. Ed. 2d 462",
            "83 S. Ct. 1381",
            "373 U.S. 427",
            "1963 U.S. LEXIS 2618"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Edwards",
          "cluster_id": 108995,
          "cite": [
            "39 L. Ed. 2d 771",
            "94 S. Ct. 1234",
            "415 U.S. 800",
            "1974 U.S. LEXIS 120"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gustafson v. Florida",
          "cluster_id": 108894,
          "cite": [
            "38 L. Ed. 2d 456",
            "94 S. Ct. 488",
            "414 U.S. 260",
            "1973 U.S. LEXIS 22",
            "66 Ohio Op. 2d 275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. LaSalle National Bank",
          "cluster_id": 109901,
          "cite": [
            "57 L. Ed. 2d 221",
            "98 S. Ct. 2357",
            "437 U.S. 298",
            "1978 U.S. LEXIS 112",
            "42 A.F.T.R.2d (RIA) 5198"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106021 OR 9421949 OR 9421950 OR 9421951) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03NzU3ODU2MDAwMDAmcz02NzU3NzkmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106021+OR+9421949+OR+9421950+OR+9421951%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 193
      },
      "lane2_top_cited": {
        "query": "cites:(106021 OR 9421949 OR 9421950 OR 9421951)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMjQmcz0zNjkwNzcmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28106021+OR+9421949+OR+9421950+OR+9421951%29&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 25
      },
      "lane3_recency": {
        "query": "cites:(106021 OR 9421949 OR 9421950 OR 9421951)",
        "reviewed": 9,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 9,
        "triage_read": 0,
        "triage_snippet_classified": 9
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106021 OR 9421949 OR 9421950 OR 9421951)",
    "indexed_citing_opinions": 995,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106021,
        "count": 916,
        "count_source": "search"
      },
      {
        "opinion_id": 9421949,
        "count": 104,
        "count_source": "search"
      },
      {
        "opinion_id": 9421950,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9421951,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1485,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/abel-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY3NDE4MDkmcz00NzQ3NTIxJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106021+OR+9421949+OR+9421950+OR+9421951%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106021,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 94479,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 95830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 97714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 100280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104978,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 105227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 105341,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 105343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 105407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 245929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 1484849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 1880326,
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
    "date_created": "2026-07-04T15:08:05Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T15:08:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T15:08:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T15:30:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T15:08:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Abel v. United States

```
<div>
<center><b><span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U.S. 217</a></span> (1960)</b></center>
<center><h1>ABEL, ALIAS MARK, ALIAS COLLINS, ALIAS GOLDFUS,<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 2.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 24-25, 1959.</center>
<center>Restored to the calendar for reargument March 23, 1959.</center>
<center>Reargued November 9, 1959.</center>
<center>Decided March 28, 1960.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT.
<p><span class="star-pagination">*218</span> <i>James B. Donovan</i> argued and reargued the cause for petitioner. With him on the briefs was <i>Thomas M. Debevoise II.</i></p>
<p><i>Solicitor General Rankin</i> argued and reargued the cause for the United States. With him on the original brief were <i>Acting Assistant Attorney General Yeagley, William F. Tompkins</i> and <i>Kevin T. Maroney.</i> With him on the supplemental brief on reargument were <i>Assistant Attorney General Yeagley, John F. Davis, William F. Tompkins</i> and <i>Kevin T. Maroney.</i></p>
<p>MR. JUSTICE FRANKFURTER delivered the opinion of the Court.</p>
<p>The question in this case is whether seven items were properly admitted into evidence at the petitioner's trial for conspiracy to commit espionage. All seven items were seized by officers of the Government without a search warrant. The seizures did not occur in connection with the exertion of the criminal process against petitioner. They arose out of his administrative arrest by the United States Immigration and Naturalization Service as a preliminary to his deportation. A motion to suppress these items as evidence, duly made in the District Court, was denied after a full hearing. <span class="citation" data-id="8725152"><a href="/opinion/8741899/united-states-v-abel/" aria-description="Citation for case: United States v. Abel">155 F. Supp. 8</a></span>. Petitioner was tried, convicted and sentenced to thirty years' imprisonment and to the payment of a fine of $3,000. The Court of Appeals affirmed, <span class="citation" data-id="245929"><a href="/opinion/245929/united-states-v-rudolph-ivanovich-abel-also-known-as-mark-and-also/" aria-description="Citation for case: United States v. Rudolph Ivanovich Abel, Also Known as...">258 F. 2d 485</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./358/813/">358 U. S. 813</a></span>, limiting the grant to the following two questions:</p>
<blockquote>"1. Whether the Fourth and Fifth Amendments to the Constitution of the United States are violated by <span class="star-pagination">*219</span> a search and the seizure of evidence without a search warrant, after an alien suspected and officially accused of espionage has been taken into custody for deportation, pursuant to an administrative Immigration Service warrant, but has not been arrested for the commission of a crime?</blockquote>
<blockquote>"2. Whether the Fourth and Fifth Amendments to the Constitution of the United States are violated when articles so seized are unrelated to the Immigration Service warrant and, together with other articles obtained from such leads, are introduced as evidence in a prosecution for espionage?"</blockquote>
<p>Argument was first heard at October Term, 1958. The case having been set down for reargument at this Term, <span class="citation multiple-matches"><a href="/c/U.%20S./359/940/">359 U. S. 940</a></span>, counsel were asked to discuss a series of additional questions, set out in the margin.<sup>[*]</sup></p>
<p>We have considered the case on the assumption that the conviction must be reversed should we find challenged items of evidence to have been seized in violation of the Constitution and therefore improperly admitted into evidence. We find, however, that the admission of these items was free from any infirmity and we affirm the judgment. (Of course the nature of the case, the fact that it was a prosecution for espionage, has no bearing <span class="star-pagination">*220</span> whatever upon the legal considerations relevant to the admissibility of evidence.)</p>
<p>The seven items, all in petitioner's possession at the time of his administrative arrest, the admissibility of which is in question, were the following:</p>
<blockquote>(1) a piece of graph paper, carrying groups of numbers arranged in rows, allegedly a coded message:</blockquote>
<blockquote>(2) a forged birth certificate, certifying the birth of "Martin Collins" in New York County in 1897:</blockquote>
<blockquote>(3) a birth certificate, certifying the birth of "Emil Goldfus" in New York in 1902 (Emil Goldfus died in 1903);</blockquote>
<blockquote>(4) an international certificate of vaccination, issued in New York to "Martin Collins" in 1957;</blockquote>
<blockquote>(5) a bank book of the East River Savings Bank containing the account of "Emil Goldfus";</blockquote>
<blockquote>(6) a hollowed-out pencil containing 18 microfilms; and</blockquote>
<blockquote>(7) a block of wood, wrapped in sandpaper, and containing within it a small booklet with a series of numbers on each page, a so-called "cipher pad."</blockquote>
<p>Items (2), (3), (4) and (5) were relevant to the issues of the indictment for which petitioner was on trial in that they corroborated petitioner's use of false identities. Items (1), (6) and (7) were incriminatory as useful means for one engaged in espionage.</p>
<p>The main claims which petitioner pressed upon the Court may be thus summarized: (1) the administrative arrest was used by the Government in bad faith; (2) administrative arrests as preliminaries to deportation are unconstitutional; and (3) regardless of the validity of the administrative arrest here, the searches and seizures through which the challenged items came into the Government's possession were not lawful ancillaries to such an arrest. These claims cannot be judged apart from the circumstances leading up to the arrest and the nature of <span class="star-pagination">*221</span> the searches and seizures. It becomes necessary to relate these matters in considerable detail.</p>
<p>Petitioner was arrested by officers of the Immigration and Naturalization Service (hereafter abbreviated as I. N. S.) on June 21, 1957, in a single room in the Hotel Latham in New York City, his then abode. The attention of the I. N. S. had first been drawn to petitioner several days earlier when Noto, a Deputy Assistant Commissioner of the I. N. S., was told by a liaison officer of the Federal Bureau of Investigation (hereafter abbreviated as F. B. I.) that petitioner was believed by the F. B. I. to be an alien residing illegally in the United States. Noto was told of the F. B. I.'s interest in petitioner in connection with espionage.</p>
<p>An uncontested affidavit before the District Court asserted the following with regard to the events leading up to the F. B. I.'s communication with Noto about petitioner. About one month before the F. B. I. communicated with Noto, petitioner had been mentioned by Hayhanen, a recently defected Russian spy, as one with whom Hayhanen had for several years cooperated in attempting to commit espionage. The F. B. I. had thereupon placed petitioner under investigation. At the time the F. B. I. communicated with the I. N. S. regarding petitioner, the case against him rested chiefly upon Hayhanen's story, and Hayhanen, although he was later to be the Government's principal witness at the trial, at that time insisted that he would refuse to testify should petitioner be brought to trial, although he would fully cooperate with the Government in secret. The Department of Justice concluded that without Hayhanen's testimony the evidence was insufficient to justify petitioner's arrest and indictment on espionage charges. The decision was thereupon made to bring petitioner to the attention of the I. N. S., with a view to commencing deportation proceedings against him.</p>
<p><span class="star-pagination">*222</span> Upon being notified of the F. B. I.'s belief that petitioner was residing illegally in this country, Noto asked the F. B. I. to supply the I. N. S. with further information regarding petitioner's status as an alien. The F. B. I. did this within a week. The I. N. S. concluded that if petitioner were, as suspected, an alien, he would be subject to deportation in that he had failed to comply with the legal duty of aliens to notify the Attorney General every January of their address in the United States. <span class="citation no-link">8 U. S. C. § 1305</span>. Noto then determined on petitioner's administrative arrest as a preliminary to his deportation. The F. B. I. was so informed. On June 20, two I. N. S. officers, Schoenenberger and Kanzler, were dispatched by Noto to New York to supervise the arrest. These officers carried with them a warrant for petitioner's arrest and an order addressed to petitioner directing him to show cause why he should not be deported. They met in New York with the District Director of the I. N. S. who, after the information in the possession of the I. N. S. regarding petitioner was put before him, signed the warrant and the order. Following this, Schoenenberger and Kanzler went to F. B. I. headquarters in New York where, by prearrangement with the F. B. I. in Washington, they were met by several F. B. I. officers. These agreed to conduct agents of the I. N. S. to petitioner's hotel so that the I. N. S. might accomplish his arrest. The F. B. I. officer in charge asked whether, before the petitioner was arrested, the F. B. I. might "interview" him in an attempt to persuade him to "cooperate" with regard to his espionage. To this Schoenenberger agreed.</p>
<p>At 7 o'clock the next morning, June 21, two officers of the I. N. S. and several F. B. I. men gathered in the corridor outside petitioner's room at the Hotel Latham. All but two F. B. I. agents, Gamber and Blasco, went into the room next to petitioner's, which the F. B. I. had occupied in the course of its investigation of petitioner. <span class="star-pagination">*223</span> Gamber and Blasco were charged with confronting petitioner and soliciting his cooperation with the F. B. I. They had no warrant either to arrest or to search. If petitioner proved cooperative their instructions were to telephone to their superior for further instructions. If petitioner failed to cooperate they were to summon the waiting I. N. S. agents to execute their warrant for his arrest.</p>
<p>Gamber rapped on petitioner's door. When petitioner released the catch, Gamber pushed open the door and walked into the room, followed by Blasco. The door was left ajar and a third F. B. I. agent came into the room a few minutes later. Petitioner, who was nude, was told to put on a pair of undershorts and to sit on the bed, which he did. The F. B. I. agents remained in the room questioning petitioner for about twenty minutes. Although petitioner answered some of their questions, he did not "cooperate" regarding his alleged espionage. A signal was thereupon given to the two agents of the I. N. S. waiting in the next room. These came into petitioner's room and served petitioner with the warrant for his arrest and with the order to show cause. Shortly thereafter Schoenenberger and Kanzler, who had been waiting outside the hotel, also entered petitioner's room. These four agents of the I. N. S. remained with petitioner in his room for about an hour. For part of this time an F. B. I. agent was also in the room and during all of it another F. B. I. agent stood outside the open door of the room, where he could observe the interior.</p>
<p>After placing petitioner under arrest, the four I. N. S. agents undertook a search of his person and of all of his belongings in the room, and the adjoining bathroom, which lasted for from fifteen to twenty minutes. Petitioner did not give consent to this search; his consent was not sought. The F. B. I. agents observed this search but took no part in it. It was Schoenenberger's testimony to <span class="star-pagination">*224</span> the District Court that the purpose of this search was to discover weapons and documentary evidence of petitioner's "alienage"that is, documents to substantiate the information regarding petitioner's status as an alien which the I. N. S. had received from the F. B. I. During this search one of the challenged items of evidence, the one we have designated (2), a birth certificate for "Martin Collins," was seized. Weapons were not found, nor was any other evidence regarding petitioner's "alienage."</p>
<p>When the search was completed, petitioner was told to dress himself, to assemble his things and to choose what he wished to take with him. With the help of the I. N. S. agents almost everything in the room was packed into petitioner's baggage. A few things petitioner deliberately left on a window sill, indicating that he did not want to take them, and several other things which he chose not to pack up into his luggage he put into the room's wastepaper basket. When everything had been assembled, petitioner asked and received permission to repack one of his suitcases. While petitioner was doing so, Schoenenberger noticed him slipping some papers into the sleeve of his coat. Schoenenberger seized these. One of them was the challenged item of evidence which we have designated (1), a piece of graph paper containing a coded message.</p>
<p>When petitioner's belongings had been completely packed, petitioner agreed to check out of the hotel. One of the F. B. I. agents obtained his bill from the hotel and petitioner paid it. Petitioner was then handcuffed and taken, along with his baggage, to a waiting automobile and thence to the headquarters of the I. N. S. in New York. At I. N. S. headquarters, the property petitioner had taken with him was searched more thoroughly than it had been in his hotel room, and three more of the challenged items were discovered and seized. These were the ones we have designated (3), (4) and (5), the "Emil <span class="star-pagination">*225</span> Goldfus" birth certificate, the international vaccination certificate, and the bank book.</p>
<p>As soon as petitioner had been taken from the hotel, an F. B. I. agent, Kehoe, who had been in the room adjoining petitioner's during the arrest and search and who, like the I. N. S. agents, had no search warrant, received permission from the hotel management to search the room just vacated by petitioner. Although the bill which petitioner had paid entitled him to occupy the room until 3 p. m. of that day, the hotel's practice was to consider a room vacated whenever a guest removed his baggage and turned in his key. Kehoe conducted a search of petitioner's room which lasted for about three hours. Among other things, he seized the contents of the wastepaper basket into which petitioner had put some things while packing his belongings. Two of the items thus seized were the challenged items of evidence we have designated (6) and (7): a hollow pencil containing microfilm and a block of wood containing a "cipher pad."</p>
<p>Later in the day of his arrest, petitioner was taken by airplane to a detention center for aliens in Texas. He remained there for several weeks until arrested upon the charge of conspiracy to commit espionage for which he was brought to trial and convicted in the Eastern District of New York.</p>
<p></p>
<h2>I.</h2>
<p>The underlying basis of petitioner's attack upon the admissibility of the challenged items of evidence concerns the motive of the Government in its use of the administrative arrest. We are asked to find that the Government resorted to a subterfuge, that the Immigration and Naturalization Service warrant here was a pretense and sham, was not what it purported to be. According to petitioner, it was not the Government's true purpose in arresting him under this warrant to take him into custody pending <span class="star-pagination">*226</span> a determination of his deportability. The Government's real aims, the argument runs, were (1) to place petitioner in custody so that pressure might be brought to bear upon him to confess his espionage and cooperate with the F. B. I., and (2) to permit the Government to search through his belongings for evidence of his espionage to be used in a designed criminal prosecution against him. The claim is, in short, that the Government used this administrative warrant for entirely illegitimate purposes and that articles seized as a consequence of its use ought to have been suppressed.</p>
<p>Were this claim justified by the record, it would indeed reveal a serious misconduct by law-enforcing officers. The deliberate use by the Government of an administrative warrant for the purpose of gathering evidence in a criminal case must meet stern resistance by the courts. The preliminary stages of a criminal prosecution must be pursued in strict obedience to the safeguards and restrictions of the Constitution and laws of the United States. A finding of bad faith is, however, not open to us on this record. What the motive was of the I. N. S. officials who determined to arrest petitioner, and whether the I. N. S. in doing so was not exercising its powers in the lawful discharge of its own responsibilities but was serving as a tool for the F. B. I. in building a criminal prosecution against petitioner, were issues fully canvassed in both courts below. The crucial facts were found against the petitioner.</p>
<p>On this phase of the case the district judge, having permitted full scope to the elucidation of petitioner's claim, having seen and heard witnesses, in addition to testimony by way of affidavits, and after extensive argument, made these findings:</p>
<blockquote>"[T]he evidence is persuasive that the action taken by the officials of the Immigration and Naturalization Service is found to have been in entire good faith. <span class="star-pagination">*227</span> The testimony of Schoenenberger and Noto leaves no doubt that while the first information that came to them concerning the [petitioner] . . . was furnished by the F. B. I.which cannot be an unusual happening the proceedings taken by the Department differed in no respect from what would have been done in the case of an individual concerning whom no such information was known to exist.</blockquote>
<blockquote>"The defendant argues that the testimony establishes that the arrest was made under the direction and supervision of the F. B. I., but the evidence is to the contrary, and it is so found.</blockquote>
<blockquote>"No good reason has been suggested why these two branches of the Department of Justice should not cooperate, and that is the extent of the showing made on the part of the defendant." <span class="citation" data-id="8725152"><a href="/opinion/8741899/united-states-v-abel/#11" aria-description="Citation for case: United States v. Abel">155 F. Supp. 8, 11</a></span>.</blockquote>
<p>The opinion of the Court of Appeals, after careful consideration of the matter, held that the answer "must clearly be in the affirmative" to the question "whether the evidence in the record supports the finding of good faith made by the court below." <span class="citation" data-id="245929"><a href="/opinion/245929/united-states-v-rudolph-ivanovich-abel-also-known-as-mark-and-also/#494" aria-description="Citation for case: United States v. Rudolph Ivanovich Abel, Also Known as...">258 F. 2d 485, 494</a></span>.</p>
<p>Among the statements in evidence relied upon by the lower courts in making these findings was testimony by Noto that the interest of the I. N. S. in petitioner was confined to petitioner's illegal status in the United States; that in informing the I. N. S. about petitioner's presence in the United States the F. B. I. did not indicate what action it wanted the I. N. S. to take; that Noto himself made the decision to arrest petitioner and to commence deportation proceedings against him; that the F. B. I. made no request of him to search for evidence of espionage at the time of the arrest; and that it was "usual and mandatory" for the F. B. I. and I. N. S. to work together in the manner they did. There was also the testimony of Schoenenberger, regarding the purpose of the search he <span class="star-pagination">*228</span> made of petitioner's belongings, that the motive was to look for weapons and documentary evidence of alienage. To be sure, the record is not barren of evidence supporting an inference opposed to the conclusion to which the two lower courts were led by the record as a whole: for example, the facts that the I. N. S. held off its arrest of petitioner while the F. B. I. solicited his cooperation, and that the F. B. I. held itself ready to search petitioner's room as soon as it was vacated. These elements, however, did not, and were not required to, persuade the two courts below in the face of ample evidence of good faith to the contrary, especially the human evidence of those involved in the episode. We are not free to overturn the conclusion of the courts below when justified by such solid proof.</p>
<p>Petitioner's basic contention comes down to this: even without a showing of bad faith, the F. B. I. and I. N. S. must be held to have cooperated to an impermissible extent in this case, the case being one where the alien arrested by the I. N. S. for deportation was also suspected by the F. B. I. of crime. At the worst, it may be said that the circumstances of this case reveal an opportunity for abuse of the administrative arrest. But to hold illegitimate, in the absence of bad faith, the cooperation between I. N. S. and F. B. I. would be to ignore the scope of rightful cooperation between two branches of a single Department of Justice concerned with enforcement of different areas of law under the common authority of the Attorney General.</p>
<p>The facts are that the F. B. I. suspected petitioner both of espionage and illegal residence in the United States as an alien. That agency surely acted not only with propriety but in discharge of its duty in bringing petitioner's illegal status to the attention of the I. N. S., particularly after it found itself unable to proceed with petitioner's prosecution for espionage. Only the I. N. S. is authorized to initiate deportation proceedings, and certainly the <span class="star-pagination">*229</span> F. B. I. is not to be required to remain mute regarding one they have reason to believe to be a deportable alien, merely because he is also suspected of one of the gravest of crimes and the F. B. I. entertains the hope that criminal proceedings may eventually be brought against him. The I. N. S., just as certainly, would not have performed its responsibilities had it been deterred from instituting deportation proceedings solely because it became aware of petitioner through the F. B. I., and had knowledge that the F. B. I. suspected petitioner of espionage. The Government has available two ways of dealing with a criminally suspect deportable alien. It would make no sense to say that branches of the Department of Justice may not cooperate in pursuing one course of action or the other, once it is honestly decided what course is to be preferred. For the same reasons this cooperation may properly extend to the extent and in the manner in which the F. B. I. and I. N. S. cooperated in effecting petitioner's administrative arrest. Nor does it taint the administrative arrest that the F. B. I. solicited petitioner's cooperation before it took place, stood by while it did, and searched the vacated room after the arrest. The F. B. I. was not barred from continuing its investigation in the hope that it might result in a prosecution for espionage because the I. N. S., in the discharge of its duties, had embarked upon an independent decision to initiate proceedings for deportation.</p>
<p>The Constitution does not require that honest law enforcement should be put to such an irrevocable choice between two recourses of the Government. For a contrast to the proper cooperation between two branches of a single Department of Justice as revealed in this case, see the story told in <i>Colyer</i> v. <i>Skeffington,</i> <span class="citation" data-id="8816033"><a href="/opinion/8831099/colyer-v-skeffington/" aria-description="Citation for case: Colyer v. Skeffington">265 F. 17</a></span>. That case sets forth in detail the improper use of immigration authorities by the Bureau of Investigation of the Department of Justice when the immigration service was <span class="star-pagination">*230</span> a branch of the Department of Labor and was acting not within its lawful authority but as the cat's paw of another, unrelated branch of the Government.</p>
<p>We emphasize again that our view of the matter would be totally different had the evidence established, or were the courts below not justified in not finding that the administrative warrant was here employed as an instrument of criminal law enforcement to circumvent the latter's legal restrictions, rather than as a bona fide preliminary step in a deportation proceeding. The test is whether the decision to proceed administratively toward deportation was influenced by, and was carried out for, a purpose of amassing evidence in the prosecution for crime. The record precludes such a finding by this Court.</p>
<p></p>
<h2>II.</h2>
<p>The claim that the administrative warrant by which petitioner was arrested was invalid, because it did not satisfy the requirements for "warrants" under the Fourth Amendment, is not entitled to our consideration in the circumstances before us. It was not made below; indeed, it was expressly disavowed. Statutes authorizing administrative arrest to achieve detention pending deportation proceedings have the sanction of time. It would emphasize the disregard for the presumptive respect the Court owes to the validity of Acts of Congress, especially when confirmed by uncontested historical legitimacy, to bring into question for the first time such a long-sanctioned practice of government at the behest of a party who not only did not challenge the exercise of authority below, but expressly acknowledged its validity.</p>
<p>The grounds relied on in the trial court and the Court of Appeals by petitioner were solely (in addition to the insufficiency of the evidence, a contention not here for review) (1) the bad faith of the Government's use of <span class="star-pagination">*231</span> the administrative arrest warrant and (2) the lack of a power incidental to the execution of an administrative warrant to search and seize articles for use as evidence in a later criminal prosecution. At no time did petitioner question the legality of the administrative arrest procedure either as unauthorized or as unconstitutional. Such challenges were, to repeat, disclaimed. At the hearing on the motion to suppress, petitioner's counsel was questioned by the court regarding the theory of relief relied upon:</p>
<blockquote>"The Court: They [the Government] were not at liberty to arrest him [petitioner]?</blockquote>
<blockquote>"Mr. Fraiman: No, your Honor.</blockquote>
<blockquote>"They were perfectly proper in arresting him.</blockquote>
<blockquote>"We don't contend that at all.</blockquote>
<blockquote>"As a matter of fact, we contend it was their duty to arrest this man as they did.</blockquote>
<blockquote>"I think it should show or rather, it showed admirable thinking on the part of the F. B. I. and the Immigration Service.</blockquote>
<blockquote>"We don't find any fault with that.</blockquote>
<blockquote>"Our contention is that although they were permitted to arrest this man, and in fact, had a duty to arrest this man in a manner in which they did, they did not have a right to search his premises for the material which related to espionage.</blockquote>
<blockquote>.....</blockquote>
<blockquote>". . . He was charged with no criminal offense in this warrant.</blockquote>
<blockquote>"The Court: He was suspected of being illegally in the country, wasn't he?</blockquote>
<blockquote>"Mr. Fraiman: Yes, your Honor.</blockquote>
<blockquote>"The Court: He was properly arrested.</blockquote>
<blockquote>"Mr. Fraiman: He was properly arrested, we concede that, your Honor."</blockquote>
<p><span class="star-pagination">*232</span> Counsel further made it plain that the arrest warrant whose validity he was conceding was "one of these Immigration warrants which is obtained without any background material at all." Affirmative acceptance of what is now sought to be questioned could not be plainer.</p>
<p>The present form of the legislation giving authority to the Attorney General or his delegate to arrest aliens pending deportation proceedings under an administrative warrant, not a judicial warrant within the scope of the Fourth Amendment, is § 242 (a) of the Immigration and Nationality Act of 1952. (<span class="citation no-link">8 U. S. C. § 1252</span> (a)). The regulations under this Act delegate the authority to issue these administrative warrants to the District Directors of the I. N. S. "[a]t the commencement of any proceeding [to deport] . . . or at any time thereafter . . . whenever, in [their] . . . discretion, it appears that the arrest of the respondent is necessary or desirable." <span class="citation no-link">8 CFR § 242.2</span> (a). Also, according to these regulations, proceedings to deport are commenced by orders to show cause issued by the District Directors or others; and the "Operating Instructions" of the I. N. S. direct that the application for an order to show cause should be based upon a showing of a prima facie case of deportability. The warrant of arrest for petitioner was issued by the New York District Director of the I. N. S. at the same time as he signed an order to show cause. Schoenenberger testified that, before the warrant and order were issued, he and Kanzler related to the District Director what they had learned from the F. B. I. regarding petitioner's status as an alien, and the order to show cause recited that petitioner had failed to register, as aliens must. Since petitioner was a suspected spy, who had never acknowledged his residence in the United States to the Government or openly admitted his presence here, there was ample reason to believe that his arrest pending deportation was "necessary or desirable." The arrest procedure followed <span class="star-pagination">*233</span> in the present case fully complied with the statute and regulations.</p>
<p>Statutes providing for deportation have ordinarily authorized the arrest of deportable aliens by order of an executive official. The first of these was in 1798. Act of June 25, 1798, c. 58, § 2, <span class="citation no-link">1 Stat. 571</span>. And see, since that time, and before the present Act, Act of Oct. 19, 1888, c. 1210, <span class="citation no-link">25 Stat. 566</span>; Act of Mar. 3, 1903, c. 1012, § 21, <span class="citation no-link">32 Stat. 1218</span>; Act of Feb. 20, 1907, c. 1134, § 20, <span class="citation no-link">34 Stat. 904</span>; Act of Feb. 5, 1917, c. 29, § 19, <span class="citation no-link">39 Stat. 889</span>; Act of Oct. 16, 1918, c. 186, § 2, <span class="citation no-link">40 Stat. 1012</span>; Act of May 10, 1920, c. 174, <span class="citation no-link">41 Stat. 593</span>; Internal Security Act of 1950, c. 1024, Title I, § 22, <span class="citation no-link">64 Stat. 1008</span>. To be sure, some of these statutes, namely the Acts of 1888, 1903 and 1907, dealt only with aliens who had landed illegally in the United States, and not with aliens sought to be deported by reason of some act or failure to act since entering. Even apart from these, there remains overwhelming historical legislative recognition of the propriety of administrative arrest for deportable aliens such as petitioner.</p>
<p>The constitutional validity of this long-standing administrative arrest procedure in deportation cases has never been directly challenged in reported litigation. Two lower court cases involved oblique challenges, which were summarily rejected. <i>Podolski</i> v. <i>Baird,</i> <span class="citation" data-id="1880326"><a href="/opinion/1880326/podolski-v-baird/" aria-description="Citation for case: Podolski v. Baird">94 F. Supp. 294</a></span>; <i>Ex parte Avakian,</i> <span class="citation" data-id="8779629"><a href="/opinion/8795568/ex-parte-avakian/#692" aria-description="Citation for case: Ex parte Avakian">188 F. 688, 692</a></span>. See also the discussion in <i>Colyer</i> v. <i>Skeffington,</i> <span class="citation" data-id="8816033"><a href="/opinion/8831099/colyer-v-skeffington/" aria-description="Citation for case: Colyer v. Skeffington">265 F. 17</a></span>, reversed on other grounds <i>sub nom. </i><i>Skeffington</i> v. <i>Katzeff,</i> <span class="citation" data-id="8823361"><a href="/opinion/8838268/skeffington-v-katzeff/" aria-description="Citation for case: Skeffington v. Katzeff">277 F. 129</a></span>, where the District Court made an exhaustive examination of the fairness of a group of deportation proceedings initiated by administrative arrests, but nowhere brought into question the validity of the administrative arrest procedure as such. This Court seems never expressly to have directed its attention to the particular question of the constitutional validity of administrative deportation warrants. It has <span class="star-pagination">*234</span> frequently, however, upheld administrative deportation proceedings shown by the Court's opinion to have been begun by arrests pursuant to such warrants. See <i>The Japanese Immigrant Case,</i> <span class="citation" data-id="95830"><a href="/opinion/95830/the-japanese-immigrant-case/" aria-description="Citation for case: The Japanese Immigrant Case">189 U. S. 86</a></span>; <i>Zakonaite</i> v. <i>Wolf,</i> <span class="citation" data-id="97714"><a href="/opinion/97714/zakonaite-v-wolf/" aria-description="Citation for case: Zakonaite v. Wolf">226 U. S. 272</a></span>; <i>Bilokumsky</i> v. <i>Tod,</i> <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">263 U. S. 149</a></span>; <i>Carlson</i> v. <i>Landon,</i> <span class="citation" data-id="9420689"><a href="/opinion/104978/carlson-v-landon/" aria-description="Citation for case: Carlson v. Landon">342 U. S. 524</a></span>. In <i>Carlson</i> v. <i><span class="citation" data-id="9420689"><a href="/opinion/104978/carlson-v-landon/" aria-description="Citation for case: Carlson v. Landon">Landon</a></span></i><i>,</i> the validity of the arrest was necessarily implicated, for the Court there sustained discretion in the Attorney General to deny bail to alien Communists held pending deportation on administrative arrest warrants. In the presence of this impressive historical evidence of acceptance of the validity of statutes providing for administrative deportation arrest from almost the beginning of the Nation, petitioner's disavowal of the issue below calls for no further consideration.</p>
<p></p>
<h2>III.</h2>
<p>Since petitioner's arrest was valid, we reach the question whether the seven challenged items, all seized during searches which were a direct consequence of that arrest, were properly admitted into evidence. This issue raises three questions: (1) Were the searches which produced these items proper searches for the Government to have made? If they were not, then whatever the nature of the seized articles, and however proper it would have been to seize them during a valid search, they should have been suppressed as the fruits of activity in violation of the Fourth Amendment. <i>E. g., </i><i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#393" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 393</a></span>. (2) Were the articles seized properly subject to seizure, even during a lawful search? We have held in this regard that not every item may be seized which is properly inspectible by the Government in the course of a legal search; for example, private papers desired by the Government merely for use as evidence may not be seized, no matter how lawful the search which <span class="star-pagination">*235</span> discovers them, <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#310" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 310</a></span>, nor may the Government seize, wholesale, the contents of a house it might have searched, <i>Kremen</i> v. <i>United States,</i> <span class="citation" data-id="8931353"><a href="/opinion/8940894/kremen-v-united-states/" aria-description="Citation for case: Kremen v. United States">353 U. S. 346</a></span>. (3) Was the Government free to use the articles, even if properly seized, as evidence in a criminal case, the seizures having been made in the course of a separate administrative proceeding?</p>
<p>The most fundamental of the issues involved concerns the legality of the search and seizures made in petitioner's room in the Hotel Latham. The ground of objection is that a search may not be conducted as an incident to a lawful administrative arrest.</p>
<p>We take as a starting point the cases in this Court dealing with the extent of the search which may properly be made without a warrant following a lawful arrest for crime. The several cases on this subject in this Court cannot be satisfactorily reconciled. This problem has, as is well-known, provoked strong and fluctuating differences of view on the Court. This is not the occasion to attempt to reconcile all the decisions, or to re-examine them. Compare <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span>, with <i>Go-Bart Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span>, and <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452</a></span>; compare <i><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">Go-Bart, supra,</a></span></i> and <i><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">Lefkowitz, supra,</a></span></i> with <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span>, and <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>; compare also <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris, supra,</a></span></i> with <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span>, and <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span></i> with <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz, supra</a></span></i> (overruling <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span></i>). Of these cases, <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> set by far the most permissive limits upon searches incidental to lawful arrests. In view of their judicial context, the trial judge and the Government justifiably relied upon these cases for guidance at the trial; and the petitioner himself accepted the <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> case on the motion to suppress, nor does he ask this Court to reconsider <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span>.</i> It would, under these circumstances, be unjustifiable retrospective <span class="star-pagination">*236</span> lawmaking for the Court in this case to reject the authority of these decisions.</p>
<p>Are there to be permitted incidental to valid administrative arrests, searches as broad in physical area as, and analogous in purpose to, those permitted by the applicable precedents as incidents to lawful arrests for crime? Specifically, were the officers of the I. N. S. acting lawfully in this case when, after his arrest, they searched through petitioner's belongings in his hotel room looking for weapons and documents to evidence his "alienage"? There can be no doubt that a search for weapons has as much justification here as it has in the case of an arrest for crime, where it has been recognized as proper. <i>E. g., </i><i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span>. It is no less important for government officers, acting under established procedure to effect a deportation arrest rather than one for crime, to protect themselves and to insure that their prisoner retains no means by which to accomplish an escape.</p>
<p>Nor is there any constitutional reason to limit the search for materials proving the deportability of an alien, when validly arrested, more severely than we limit the search for materials probative of crime when a valid criminal arrest is made. The need for the proof is as great in one case as in the other, for deportation can be accomplished only after a hearing at which deportability is established. Since a deportation arrest warrant is not a judicial warrant, a search incidental to a deportation arrest is without the authority of a judge or commissioner. But so is a search incidental to a criminal arrest made upon probable cause without a warrant, and under <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#60" aria-description="Citation for case: United States v. Rabinowitz">339 U. S., at 60</a></span>, such a search does not require a judicial warrant for its validity. It is to be remembered that an I. N. S. officer may not arrest and search on his own. Application for a warrant must be made to an independent responsible officer, the District Director <span class="star-pagination">*237</span> of the I. N. S., to whom a prima facie case of deportability must be shown. The differences between the procedural protections governing criminal and deportation arrests are not of a quality or magnitude to warrant the deduction of a constitutional difference regarding the right of incidental search. If anything, we ought to be more vigilant, not less, to protect individuals and their property from warrantless searches made for the purpose of turning up proof to convict than we are to protect them from searches for matter bearing on deportability. According to the uniform decisions of this Court deportation proceedings are not subject to the constitutional safeguards for criminal prosecutions. Searches for evidence of crime present situations demanding the greatest, not the least, restraint upon the Government's intrusion into privacy; although its protection is not limited to them, it was at these searches which the Fourth Amendment was primarily directed. We conclude, therefore, that government officers who effect a deportation arrest have a right of incidental search analogous to the search permitted criminal law-enforcement officers.</p>
<p>Judged by the prevailing doctrine, the search of petitioner's hotel room was justified. Its physical scope, being confined to the petitioner's room and the adjoining bathroom, was far less extensive than the search in <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span>.</i> The search here was less intensive than were the deliberately exhaustive quests in <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span>,</i> and its purpose not less justifiable. The only things sought here, in addition to weapons, were documents connected with petitioner's status as an alien. These may well be considered as instruments or means for accomplishing his illegal status, and thus proper objects of search under <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris, supra,</a></span></i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#154" aria-description="Citation for case: Harris v. United States">331 U. S., at 154</a></span>.</p>
<p>Two of the challenged items were seized during this search of petitioner's property at his hotel room. The first was item (2), a forged New York birth certificate <span class="star-pagination">*238</span> for "Martin Collins," one of the false identities which petitioner assumed in this country in order to keep his presence here undetected. This item was seizable when found during a proper search, not only as a forged official document by which petitioner sought to evade his obligation to register as an alien, but also as a document which petitioner was using as an aid in the commission of espionage, for his undetected presence in this country was vital to his work as a spy. Documents used as a means to commit crime are the proper subjects of search warrants, <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>, and are seizable when discovered in the course of a lawful search, <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span>.</p>
<p>The other item seized in the course of the search of petitioner's hotel room was item (1), a piece of graph paper containing a coded message. This was seized by Schoenenberger as petitioner, while packing his suitcase, was seeking to hide it in his sleeve. An arresting officer is free to take hold of articles which he sees the accused deliberately trying to hide. This power derives from the dangers that a weapon will be concealed, or that relevant evidence will be destroyed. Once this piece of graph paper came into Schoenenberger's hands, it was not necessary for him to return it, as it was an instrumentality for the commission of espionage. This is so even though Schoenenberger was not only not looking for items connected with espionage but could not properly have been searching for the purpose of finding such items. When an article subject to lawful seizure properly comes into an officer's possession in the course of a lawful search it would be entirely without reason to say that he must return it because it was not one of the things it was his business to look for. See <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris, supra,</a></span></i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#154" aria-description="Citation for case: Harris v. United States">331 U. S., at 154-155</a></span>.</p>
<p>Items (3), (4), and (5), a birth certificate for "Emil Goldfus" who died in 1903, a certificate of vaccination for "Martin Collins," and a bank book for "Emil Goldfus" <span class="star-pagination">*239</span> were seized, not in petitioner's hotel room, but in a more careful search at I. N. S. headquarters of the belongings petitioner chose to take with him when arrested. This search was a proper one. The property taken by petitioner to I. N. S. headquarters was all property which, under <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span>,</i> was subject to search at the place of arrest. We do not think it significantly different, when the accused decides to take the property with him, for the search of it to occur instead at the first place of detention when the accused arrives there, especially as the search of property carried by an accused to the place of detention has additional justifications, similar to those which justify a search of the person of one who is arrested. It is to be noted that this is not a case, like <i>Kremen</i> v. <i>United States,</i> <span class="citation" data-id="8931353"><a href="/opinion/8940894/kremen-v-united-states/" aria-description="Citation for case: Kremen v. United States">353 U. S. 346</a></span>, where the entire contents of the place where the arrest was made were seized. Such a mass seizure is illegal. The Government here did not seize the contents of petitioner's hotel room. Petitioner took with him only what he wished. He chose to leave some things behind in his room, which he voluntarily relinquished. And items (3), (4), and (5) were articles subject to seizure when found during a lawful search. They were all capable of being used to establish and maintain a false identity for petitioner, just as the forged "Martin Collins" birth certificate, and were seizable for the same reasons.</p>
<p>Items (1)-(5) having come into the Government's possession through lawful searches and seizures connected with an arrest pending deportation, was the Government free to use them as evidence in a criminal prosecution to which they related? We hold that it was. Good reason must be shown for prohibiting the Government from using relevant, otherwise admissible, evidence. There is excellent reason for disallowing its use in the case of evidence, though relevant, which is seized by the Government in violation of the Fourth Amendment to the Constitution. "If letters and private documents can thus <span class="star-pagination">*240</span> be seized and held and used in evidence against a citizen accused of an offense, the protection of the Fourth Amendment declaring his right to be secure against such searches and seizures is of no value, and, so far as those thus placed are concerned, might as well be stricken from the Constitution." <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#393" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 393</a></span>.</p>
<p>These considerations are here absent, since items (1)-(5) were seized as a consequence of wholly lawful conduct. That being so, we can see no rational basis for excluding these relevant items from trial: no wrong-doing police officer would thereby be indirectly condemned, for there were no such wrongdoers; the Fourth Amendment would not thereby be enforced, for no illegal search or seizure was made; the Court would be lending its aid to no lawless government action, for none occurred. Of course cooperation between the branch of the Department of Justice dealing with criminal law enforcement and the branch dealing with the immigration laws would be less effective if evidence lawfully seized by the one could not be used by the other. Only to the extent that it would be to the public interest to deter and prevent such cooperation, would an exclusionary rule in a case like the present be desirable. Surely no consideration of civil liberties commends discouragement of such cooperation between these two branches when undertaken in good faith. When undertaken in bad faith to avoid constitutional restraints upon criminal law enforcement the evidence must be suppressed. That is not, as we have seen, this case. Individual cases of bad faith cooperation should be dealt with by findings to that effect in the cases as they arise, not by an exclusionary rule preventing effective cooperation when undertaken in entirely good faith.</p>
<p>We have left to the last the admissibility of items (6) and (7), the hollowed-out pencil and the block of wood containing a "cipher pad," because their admissibility is founded upon an entirely different set of considerations. <span class="star-pagination">*241</span> These two items were found by an agent of the F. B. I. in the course of a search he undertook of petitioner's hotel room, immediately after petitioner had paid his bill and vacated the room. They were found in the room's wastepaper basket, where petitioner had put them while packing his belongings and preparing to leave. No pretense is made that this search by the F. B. I. was for any purpose other than to gather evidence of crime, that is, evidence of petitioner's espionage. As such, however, it was entirely lawful, although undertaken without a warrant. This is so for the reason that at the time of the search petitioner had vacated the room. The hotel then had the exclusive right to its possession, and the hotel management freely gave its consent that the search be made. Nor was it unlawful to seize the entire contents of the wastepaper basket, even though some of its contents had no connection with crime. So far as the record shows, petitioner had abandoned these articles. He had thrown them away. So far as he was concerned, they were <i>bona vacantia.</i> There can be nothing unlawful in the Government's appropriation of such abandoned property. See <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#58" aria-description="Citation for case: Hester v. United States">265 U. S. 57, 58</a></span>. The two items which were eventually introduced in evidence were assertedly means for the commission of espionage, and were themselves seizable as such. These two items having been lawfully seized by the Government in connection with an investigation of crime, we encounter no basis for discussing further their admissibility as evidence.</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE DOUGLAS, with whom MR. JUSTICE BLACK concurs, dissenting.</p>
<p>Cases of notorious criminalslike cases of small, miserable onesare apt to make bad law. When guilt permeates a record, even judges sometimes relax and let the police take shortcuts not sanctioned by constitutional <span class="star-pagination">*242</span> procedures. That practice, in certain periods of our history and in certain courts, has lowered our standards of law administration. The harm in the given case may seem excusable. But the practices generated by the precedent have far-reaching consequences that are harmful and injurious beyond measurement. The present decision is an excellent example.</p>
<p>The opening wedge that broadened the power of administrative officersas distinguished from policeto enter and search peoples' homes was <i>Frank</i> v. <i>Maryland,</i> <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360</a></span>. That case allowed a health inspector to enter a home without a warrant, even though he had ample time to get one. The officials of the Immigration and Naturalization Service (I. N. S.) are now added to the preferred list. They are preferred because their duties, being strictly administrative, put them in a separate category from those who enforce the criminal law. They need not go to magistrates, the Court says, for warrants of arrest. Their warrants are issued within the hierarchy of the agency itself.<sup>[1]</sup> Yet, as I attempted to show in my dissent in the <i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span></i> case, the Fourth Amendment in origin had to do as much with ferreting out heretics and collecting taxes as with enforcement of the criminal laws. <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#376" aria-description="Citation for case: Frank v. Maryland">359 U. S., at 376-379</a></span>.</p>
<p>Moreover, the administrative officer who invades the privacy of the home may be only a front for the police who are thus saved the nuisance of getting a warrant. We need not go far to find examples. In <i>Maryland</i> v. <i>Pettiford,</i> Sup. Bench Balt. City, The Daily Record, Dec. 16, 1959, the police used the mask of a health inspector <span class="star-pagination">*243</span> to make the <i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span></i> case serve as an easy way to get a search without a warrant. Happily, they were rebuked.<sup>[2]</sup> But that case shows the kind of problems the <i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span></i> doctrine generates. The present case is another example of the same kind, although here the police are not rebuked. The administrative official with an administrative warrant, over which no judicial official exercises any supervision and which by statute may be used only for deportation, performs a new role. The police wear his mask to do police work. That, in my view, may not be done, even though we assume that the administrative warrant <span class="star-pagination">*244</span> issued by an administrative rather than a judicial officer is valid for an arrest for the purpose of deportation. We take liberties with an Act of Congress, as well as the Constitution, when we permit this to be done. The statute permits the arrest of an alien on an administrative warrant "[p]ending a determination of deportability."<sup>[3]</sup> The Court now reads the Act as if it read "Pending an investigation of criminal conduct." Such was the nature of the arrest.</p>
<p>With due deference to the two lower courts, I think the record plainly shows that F. B. I. agents were the moving force behind this arrest and search. For at least a month they investigated the espionage activities of petitioner. They were tipped off concerning this man and his role in May; the arrest and search were made on June 21. The F. B. I. had plenty of time to get a search warrant, as much if not more time than they had in <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, and <i>Kremen</i> v. <i>United States,</i> <span class="citation" data-id="8931353"><a href="/opinion/8940894/kremen-v-united-states/" aria-description="Citation for case: Kremen v. United States">353 U. S. 346</a></span>, where the Court held warrantless searches illegal. But the F. B. I. did not go to a magistrate for a search warrant. They went instead to the I. N. S. and briefed the officials of that agency on what they had discovered. On the basis of this data a report was made to John Murff, Acting District Director of the I. N. S., who issued the warrant of arrest.</p>
<p>No effort was made by the F. B. I. to obtain a search warrant from any judicial officer, though, as I said, there was plenty of time for such an application. The administrative warrant of arrest was chosen with care and calculation as the vehicle through which the arrest and search were to be made. The F. B. I. had an agreement with the officials of I. N. S. that this warrant of arrest would not be served at least until petitioner refused to <span class="star-pagination">*245</span> "cooperate." The F. B. I. agents went with agents of the I. N. S. to apprehend petitioner in his hotel room. Again, it was the F. B. I. agents who were first. They were the ones who entered petitioner's room and who interrogated him to see if he would "cooperate"; and when they were unable to get him to "cooperate" by threatening him with arrest, they signaled agents of the I. N. S. who had waited outside to come in and make the arrest. The search was made both by the F. B. I. agents and by officers of the I. N. S. And when petitioner was flown 1,000 miles to a special detention camp and held for three weeks, the agents of the F. B. I. as well as I. N. S. interrogated him.<sup>[4]</sup></p>
<p>Thus the F. B. I. used an administrative warrant to make an arrest for criminal investigation both in violation of § 242 (a) of the Immigration and Nationality Act<sup>[5]</sup> and in violation of the Bill of Rights.</p>
<p>The issue is not whether these F. B. I. agents acted in bad faith. Of course they did not. The question is how far zeal may be permitted to carry officials bent on law enforcement. As Mr. Justice Brandeis once said, "Experience should teach us to be most on our guard to protect liberty when the Government's purposes are beneficent." <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#479" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 479</a></span> (dissenting opinion). The facts seem to me clearly to establish that the F. B. I. agents wore the mask of I. N. S. to do what otherwise they could not have done. They did what they could do only if they had gone to a judicial officer pursuant to the requirements of the Fourth Amendment, disclosed <span class="star-pagination">*246</span> their evidence, and obtained the necessary warrant for the searches which they made.</p>
<p>If the F. B. I. agents had gone to a magistrate, any search warrant issued would by terms of the Fourth Amendment have to "particularly" describe "the place to be searched" and the "things to be seized." How much more convenient it is for the police to find a way around those specific requirements of the Fourth Amendment! What a hindrance it is to work laboriously through constitutional procedures! How much easier to go to another official in the same department! The administrative officer can give a warrant good for unlimited search. No more showing of probable cause to a magistrate! No more limitations on what may be searched and when!</p>
<p>In <i>Rea</i> v. <i>United States,</i> <span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/" aria-description="Citation for case: Rea v. United States">350 U. S. 214</a></span>, federal police officers, who obtained evidence in violation of federal law governing searches and seizures and so lost their case in the federal court, repaired to a state court and proposed to use it there in a state criminal prosecution. The Court held that the Federal District Court could properly enjoin the federal official from using the illegal search and seizure as basis for testifying in the state court. The federal rules governing searches and seizures, we held, are "designed as standards for federal agents" no more to be defeated by devious than by direct methods. The present case is even more palpably vulnerable. No state agency is involved. Federal police seek to do what immigration officials can do to deport a person but what our rules, statutes, and Constitution forbid the police from doing to prosecute him for a crime.</p>
<p>The tragedy in our approval of these short cuts is that the protection afforded by the Fourth Amendment is removed from an important segment of our life. We today forget what the Court said in <i>Johnson</i> v. <i>United States, supra,</i> at 14, that the Fourth Amendment provision <span class="star-pagination">*247</span> for "probable cause" requires that those inferences "be drawn by a neutral and detached magistrate" not "by the officer engaged in the often competitive enterprise of ferreting out crime." This is a protection given not only to citizens but to aliens as well, as the opinion of the Court by implication holds. The right "of the people" covered by the Fourth Amendment certainly gives security to aliens in the same degree that "person" in the Fifth and "the accused" in the Sixth Amendments also protects them. See <i>Wong Wing</i> v. <i>United States,</i> <span class="citation" data-id="9883065"><a href="/opinion/94479/wong-wing-v-united-states/#242" aria-description="Citation for case: Wong Wing v. United States">163 U. S. 228, 242</a></span>. Here the F. B. I. works exclusively through an administrative agencythe I. N. S.to accomplish what the Fourth Amendment says can be done only by a judicial officer. A procedure designed to serve administrative endsdeportationis cleverly adapted to serve other endscriminal prosecution. We have had like examples of this same trend in recent times. Lifting the requirements of the Fourth Amendment for the benefit of health inspectors was accomplished by <i>Frank</i> v. <i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Maryland</a></span></i><i>,</i> as I have said. Allowing the Department of Justice rather than judicial officers to determine whether aliens will be entitled to release on bail pending deportation hearings is another. See <i>Carlson</i> v. <i>Landon,</i> <span class="citation" data-id="9420689"><a href="/opinion/104978/carlson-v-landon/" aria-description="Citation for case: Carlson v. Landon">342 U. S. 524</a></span>.</p>
<p>Some things in our protective scheme of civil rights are entrusted to the judiciary. Those controls are not always congenial to the police. Yet if we are to preserve our system of checks and balances and keep the police from being all-powerful, these judicial controls should be meticulously respected. When we read them out of the Bill of Rights by allowing short cuts as we do today and as the Court did in the <i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span></i> and <i><span class="citation" data-id="9420689"><a href="/opinion/104978/carlson-v-landon/" aria-description="Citation for case: Carlson v. Landon">Carlson</a></span></i> cases, police and administrative officials in the Executive Branch acquire powers incompatible with the Bill of Rights.</p>
<p>The F. B. I. agents stalked petitioner for weeks and had plenty of time to obtain judicial warrants for searching the <span class="star-pagination">*248</span> premises he occupied. I would require them to adhere to the command of the Fourth Amendment and not evade it by the simple device of wearing the masks of immigration officials while in fact they are preparing a case for criminal prosecution.</p>
<p>MR. JUSTICE BRENNAN, with whom THE CHIEF JUSTICE, MR. JUSTICE BLACK and MR. JUSTICE DOUGLAS join, dissenting.</p>
<p>This is a notorious case, with a notorious defendant. Yet we must take care to enforce the Constitution without regard to the nature of the crime or the nature of the criminal. The Fourth Amendment protects "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures." This right is a basic one of all the people, without exception; and this Court ruled in <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, that the fruits of governmental violation of this guarantee could not be used in a criminal prosecution. The Amendment's protection is thus made effective for everyone only by upholding it when invoked by the worst of men.</p>
<p>The opinion of the Court makes it plain that the seizure of certain of the items of petitioner taken from his room at the Hotel Latham and used in evidence against him must depend upon the existence of a broad power, without a warrant, to search the premises of one arrested, in connection with and "incidental" to his arrest. This power is of the sort recognized by <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span>, and later asserted even where the arresting officers, as here, had ample time and opportunity to secure a search warrant. <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>, overruling <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span>. The leading early cases do not recognize any such power to make a search generally through premises attendant upon an arrest. See <i>Go-Bart Importing Co.</i> v. <span class="star-pagination">*249</span> <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span>; <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452</a></span>.<sup>[1]</sup></p>
<p>The general question has been extensively canvassed here, in the general context of an arrest for crime, in the <i>Harris, Trupiano</i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> cases. Whether <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> should now be followed on their own facts is a question with which the Court is not now faced. Rather the question is whether the doctrine of those cases should be extended to a new and different set of facts facts which present a search made under circumstances much less consistent with the Fourth Amendment's prohibition against unreasonable searches than any which this Court has hitherto approved. Factual differences weigh heavily in this area: "There is no formula for the determination of reasonableness. Each case is to be decided on its own facts and circumstances." <i>Go-Bart Importing Co.</i> v. <i>United States, supra,</i> at 357. In <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span>,</i> the broad search was performed as an incident to an arrest for crime under warrants lawfully issued. <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#148" aria-description="Citation for case: Harris v. United States">331 U. S., at 148</a></span>; <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#58" aria-description="Citation for case: United States v. Rabinowitz">339 U. S., at 58</a></span>. The issuance of these warrants is by no means automaticit is controlled by a constitutionally prescribed standard. It thus could be held that sufficient protection was given the individual without the execution of a second warrant for the search. Cf. Clark, J., dissenting in <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9638337"><a href="/opinion/1484849/united-states-v-rabinowitz/#736" aria-description="Citation for case: United States v. Rabinowitz">176 F. 2d 732, 736</a></span>, reversed, <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>. And while a search generally through premises "incident" to an arrest for crime without a warrant has been sanctioned only inferentially here,<sup>[2]</sup> even if such a search be deemed permissible under the Fourth Amendment, it would not go so far as the result here. Such an arrest may <span class="star-pagination">*250</span> constitutionally be made only upon probable cause, the existence of which is subject to judicial examination, see <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#100" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 100</a></span>; and such an arrest demands the prompt bringing of the person arrested before a judicial officer, where the existence of probable cause is to be inquired into. Fed. Rules Crim. Proc., 5 (a) and (c). This Court has been astute to fashion methods of ensuring the due observance of these safeguards. <i>Henry</i> v. <i>United States, supra</i><i>; </i><i>Mallory</i> v. <i>United States,</i> <span class="citation" data-id="105545"><a href="/opinion/105545/mallory-v-united-states/" aria-description="Citation for case: Mallory v. United States">354 U. S. 449</a></span>; <i>McNabb</i> v. <i>United States,</i> <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U. S. 332</a></span>.</p>
<p>Even assuming that the power of Congress over aliens may be as great as was said in <i>Galvan</i> v. <i>Press,</i> <span class="citation" data-id="9421085"><a href="/opinion/105227/galvan-v-press/" aria-description="Citation for case: Galvan v. Press">347 U. S. 522</a></span>, and that deportation may be styled "civil," <i>Harisiades</i> v. <i>Shaughnessy,</i> <span class="citation" data-id="9420696"><a href="/opinion/104980/harisiades-v-shaughnessy/#594" aria-description="Citation for case: Harisiades v. Shaughnessy">342 U. S. 580, 594</a></span>, it does not follow that Congress may strip aliens of the protections of the Fourth Amendment and authorize unreasonable searches of their premises, books and papers. Even if Congress could make the exclusionary sanction of the Amendment inapplicable in deportation proceedings, the fruits of the search here were used in a prosecution whose criminal character no dialectic can conceal. Clearly the consequence of the Fourth Amendment in such a trial is that the fruits of such a search may not be given in evidence, under the rule declared in <i>Weeks</i> v. <i>United States, supra</i><i>.</i> We need not, in my view, inquire as to whether the sort of "administrative" arrest made here is constitutionally valid as to permit the officers to hold petitioner's person for deportation proceedings. With the Court, this issue may be treated as not properly before us for our consideration, and the arrest may be treated for the purposes of this case as lawful in itself. But even with <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i>Rabinowitz,</i> that does not conclude the matter as to the search. It is patent that the sort of search permitted by those cases, and necessary to sustain the seizures here, goes beyond what is reasonably related <span class="star-pagination">*251</span> to the mechanics of the arrest itselfensuring the safety of the arresting officers and the security of the arrest against the prisoner's escape. Since it does, I think it plain that before it can be concluded here that the search was not an unreasonable one, there must be some inquiry into the over-all protection given the individual by the totality of the processes necessary to the arrest and the seizure. Here the arrest, while had on what is called a warrant, was made totally without the intervention of an independent magistrate; it was made on the authorization of one administrative official to another. And after the petitioner was taken into custody, there was no obligation upon the administrative officials who arrested him to take him before any independent officer, sitting under the conditions of publicity that characterize our judicial institutions, and justify what had been done.<sup>[3]</sup> Concretely, what happened instead was this: petitioner, upon his arrest, was taken to a local administrative headquarters and then flown in a special aircraft to a special detention camp over 1,000 miles away. He was incarcerated in solitary confinement there. As far as the world knew, he had vanished. He was questioned daily at the place of incarceration for over three weeks. An executive procedure as to his deportability was had, at the camp, after a few days, but there was never any independent inquiry or judicial control over the circumstances of the arrest and the seizure till over five weeks after his arrest, when, at the detention camp, he was served with a bench warrant for his arrest on criminal charges, upon an indictment.</p>
<p>The Fourth Amendment imposes substantive standards for searches and seizures; but with them one of the important safeguards it establishes is a procedure; and <span class="star-pagination">*252</span> central to this procedure is an independent control over the actions of officers effecting searches of private premises. "Indeed, the informed and deliberate determinations of magistrates empowered to issue warrants as to what searches and seizures are permissible under the Constitution are to be preferred over the hurried action of officers and others who may happen to make arrests." <i>United States</i> v. <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#464" aria-description="Citation for case: United States v. Lefkowitz"><i>Lefkowitz, supra,</i> at 464</a></span>. "Absent some grave emergency, the Fourth Amendment has interposed a magistrate between the citizen and the police." <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 455</a></span>. It is one thing to say that an adequate substitute for this sort of intervention by a magistrate can be found in the strict protections with which federal criminal procedure surrounds the making of a criminal arrestwhere the action of the officers must receive an antecedent or immediately subsequent independent scrutiny. It goes much further to say that such a substitute can be found in the executive processes employed here. The question is not whether they are constitutionally adequate in their own termswhether they are a proper means of taking into custody one not charged with crime. The question is rather whether they furnish a context in which a search generally through premises can be said to be a reasonable one under the Fourth Amendment. These arrest procedures, as exemplified here, differ as night from day from the processes of an arrest for crime. When the power to make a broad, warrantless search is added to them, we create a complete concentration of power in executive officers over the person and effects of the individual. We completely remove any independent control over the powers of executive officers to make searches. They may take any man they think to be a deportable alien into their own custody, hold him without arraignment or bond, and, having been careful to apprehend him at home, make a search generally through his premises. I cannot see <span class="star-pagination">*253</span> how this can be said to be consistent with the Fourth Amendment's command; it was, rather, against such a concentration of executive power over the privacy of the individual that the Fourth Amendment was raised. I do not think the <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i>Rabinowitz</i> cases have taken us to this point.</p>
<p>If the search here were of the sort the Fourth Amendment contemplated, there would be no need for the elaborate, if somewhat pointless, inquiry the Court makes into the "good faith" of the arrest. Once it is established that a simple executive arrest of one as a deportable alien gives the arresting officers the power to search his premises, what precise state of mind on the part of the officers will make the arrest a "subterfuge" for the start of criminal proceedings, and render the search unreasonable? We are not, I fear, given any workable answer, and of course the practical problems relative to the trial of such a matter hardly need elaboration; but the Court verbalizes the issue as "whether the decision to proceed administratively toward deportation was influenced by, and was carried out for, a purpose of amassing evidence in the prosecution for crime." But under today's ruling, every administrative arrest offers this possibility of a facile search, theoretically for things connected with unlawful presence in the country, that may turn up evidence of crime; and this possibility will be well known to arresting officers. Perhaps the question is how much basis the officers had to suspect the person of crime; but it would appear a strange test as to whether a search which turns up criminal evidence is unreasonable, that the search is the more justifiable the less there was antecedent probable cause to suspect the defendant of crime. If the search were made on a valid warrant, there would be no such issue even if it turned up matter relevant to another crime. See <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#311" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 311-312</a></span>. External procedural control in accord with the <span class="star-pagination">*254</span> basic demands of the Fourth Amendment removes the grounds for abuse; but the Court's attitude here must be based on a recognition of the great possibilities of abuse its decision leaves in the present situation. These possibilities have been recognized before, in a case posing less danger: "Arrest under a warrant for a minor or a trumped-up charge has been familiar practice in the past, is a commonplace in the police state of today, and too well-known in this country. . . . The progress is too easy from police action unscrutinized by judicial authorization to the police state." <i>United States</i> v. <i>Rabinowitz, supra,</i> at 82 (dissenting opinion). Where a species of arrest is available that is subject to no judicial control, the possibilities become more and more serious. The remedy is not to invite fruitless litigation into the purity of official motives, or the specific direction of official purposes. One may always assume that the officers are zealous to perform their duty. The remedy is rather to recognize that the power to perform a search generally throughout premises upon a purely executive arrest is so unconfined by any safeguards that it cannot be countenanced as consistent with the Fourth Amendment.</p>
<p>One more word. We are told that the governmental power to make a warrantless search might be greater where the object of the search is not related to crime but to some other "civil" proceedingsuch as matter bearing on the issue whether a man should forcibly be sent from the country. The distinction is rather hollow here, where the proofs that turn up are in fact given in evidence in a criminal prosecution. And the distinction, again, invites a trial of the officers' purposes. But in any event, I think it perverts the Amendment to make this distinction. The Amendment states its own purpose, the protection of the privacy of the individual and of his property against the incursions of officials: the "right of the people to be secure in their persons, houses, papers, and effects." See <span class="star-pagination">*255</span> <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#627" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 627</a></span>. Like most of the Bill of Rights it was not designed to be a shelter for criminals, but a basic protection for everyone; to be sure, it must be upheld when asserted by criminals, in order that it may be at all effective, but it "reaches all alike, whether accused of crime or not." <i>Weeks</i> v. <i>United States, supra,</i> at 392. It is the individual's interest in privacy which the Amendment protects, and that would not appear to fluctuate with the "intent" of the invading officers. It is true that the greatest and most effective preventive against unlawful searches that has been devised is the exclusion of their fruits from criminal evidence, see <i>Weeks</i> v. <i>United States, supra</i><i>; </i><i>Boyd</i> v. <i>United States, supra</i><i>;</i> but it is strange reasoning to infer from this that the central thrust of the guarantee is to protect against a search for such evidence. The argument that it is seems no more convincing to me now than when it was made by the Court in <i>Frank</i> v. <i>Maryland,</i> <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360</a></span>. To be sure, the Court in <i>Boyd</i> v. <i>United States, supra</i><i>,</i> and in subsequent cases<sup>[4]</sup> has commented upon the intimate relationship between the privilege against unlawful searches and seizures and that against self-incrimination. This has been said to be erroneous history;<sup>[5]</sup> if it was, it was even less than a harmless error; it was part of the process through which the Fourth Amendment, by means of the exclusionary rule, has become more than a dead letter in the federal courts. Certainly this putative relationship between the guarantees is not to be used as a <span class="star-pagination">*256</span> basis of a stinting construction of eitherit was the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case itself<sup>[6]</sup> which set what might have been hoped to be the spirit of later construction of these Amendments by declaring that the start of abuse can "only be obviated by adhering to the rule that constitutional provisions for the security of person and property should be liberally construed." <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U. S., at 635</a></span>.</p>
<p>Since evidence was introduced against petitioner which had been obtained in violation of his constitutional guarantees as embodied in the Fourth Amendment, I would reverse his conviction for a new trial on the evidence not subject to this objection.</p>
<h2>NOTES</h2>
<p>[*]  "1. Whether under the laws and Constitution of the United States (a) the administrative warrant of the New York Acting District Director of the Immigration and Naturalization Service was validly issued, (b) such administrative warrant constituted a valid basis for arresting petitioner or taking him into custody, and (c) such warrant furnished a valid basis for the searches and seizures affecting his person, luggage, and the room occupied by him at the Hotel Latham.
</p>
<p>"2. Whether, independently of such administrative warrant, petitioner's arrest, and the searches and seizures affecting his person, luggage, and the room occupied by him at the Hotel Latham, were valid under the laws and Constitution of the United States.</p>
<p>"3. Whether on the record before us the issues involved in Questions `1 (a),' `1 (b),' and `2' are properly before the Court."</p>
<p>[1]  Section 242 (a) of the Immigration and Nationality Act of 1952, <span class="citation no-link">66 Stat. 208</span>, <span class="citation no-link">8 U. S. C. § 1252</span> (a), provides "Pending a determination of deportability in the case of any alien . . . such alien may, upon warrant of the Attorney General, be arrested and taken into custody."</p>
<p>[2]  In the <i>Pettiford</i> case it appears that a police officer assigned to the Sanitation Division gained entrance into a home without a warrant and discovered that the defendant who occupied the premises was engaged in lottery activities. He then signaled to a policeman in charge of gambling activities who was waiting outside in accordance with a prior agreement. Lottery slips were seized and over the defendant's objection were received in evidence in a criminal trial. A motion for a new trial was granted. The Supreme Bench of Baltimore City said in its opinion:
</p>
<p>"Section 120 of Article 12 of the Baltimore City Code provides that if the Commissioner of Health has cause to suspect that a nuisance exists in any home, he may demand entry therein in the day-time and the owner or occupier is subject to a fine if entry is denied. A conviction under this Section by the Criminal Court of Baltimore City was sustained by the Supreme Court of the United States in a five to four decision. <i>Frank vs. Maryland</i> [<span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360</a></span>]. . . .</p>
<p>.....</p>
<p>"In this case, it is evident that a principal, if not the chief purpose of the entry of the police officer assigned to the sanitation division was to endeavor to secure evidence of a lottery violation for his colleague. "The security of one's privacy against arbitrary intrusion by the police . . . is basic to a free society.' <i>Wolf vs. Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span>. An exception to that security, upheld because indispensible for the maintenance of the community health, is not to be used to cover searches without warrants inconsistent with the conceptions of human rights [embodied] in our State and Federal Constitutions."</p>
<p>[3]  Note 1, <i>supra.</i></p>
<p>[4]  Immigration officials (who often claim that their actions have an administrative finality beyond the reach of courts, see <i>Ludecke</i> v. <i>Watkins,</i> <span class="citation" data-id="9420220"><a href="/opinion/104589/ludecke-v-watkins/" aria-description="Citation for case: Ludecke v. Watkins">335 U. S. 160</a></span>: <i>Jay</i> v. <i>Boyd,</i> <span class="citation" data-id="9421310"><a href="/opinion/105407/jay-v-boyd/" aria-description="Citation for case: Jay v. Boyd">351 U. S. 345</a></span>) have no authority to detain suspects for secret interrogation. See <i>United States</i> v. <i>Minker,</i> <span class="citation" data-id="9421220"><a href="/opinion/105341/united-states-v-minker/" aria-description="Citation for case: United States v. Minker">350 U. S. 179</a></span>.</p>
<p>[5]  Note 1, <i>supra.</i></p>
<p>[1]  Earlier expressions looking the other way, <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span>; <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#198" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 198-199</a></span>, were put in proper perspective by their author in <i>Go-Bart</i> and <i><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">Lefkowitz</a></span>.</i> See <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#358" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S., at 358</a></span>; <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#465" aria-description="Citation for case: United States v. Lefkowitz">285 U. S., at 465</a></span>.</p>
<p>[2]  See <i>United States</i> v. <i>Rabinowitz, supra,</i> at 60.</p>
<p>[3]  This procedure is statutorily based on § 242 (a) of the Immigration and Nationality Act of 1952, <span class="citation no-link">66 Stat. 208</span>, <span class="citation no-link">8 U. S. C. § 1252</span> (a).</p>
<p>[4]  See, <i>e. g., </i><i>Gouled</i> v. <i>United States, supra,</i> at 306; <i>United States</i> v. <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#466" aria-description="Citation for case: United States v. Lefkowitz"><i>Lefkowitz, supra,</i> at 466-467</a></span>. The <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case itself, though drawing great support from <i>Boyd,</i> appears to rest most heavily on the Fourth Amendment itself.</p>
<p>[5]  The famous attack on the <i>Boyd</i> case's historical basis is, of course, to be found in 8 Wigmore, Evidence (3d ed. 1940), §§ 2184, 2264. The attack is incident to Wigmore's strictures on the exclusionary rule. <i>Id.,</i> §§ 2183-2184.</p>
<p>[6]  It is not without interest to note, too, that the <i>Boyd</i> case itself involved a search not in connection with a prosecution to impose fine or imprisonment, but simply with an action to forfeit 35 cases of plate glass said to have been imported into the country under a false customs declaration.</p>

</div>
```

---

## GROUP: content/cases/Agnello v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Agnello v. United States"
type: case
citation: "269 U.S. 20 (1925)"
parallel_cite: "46 S. Ct. 4; 70 L. Ed. 145; 51 A.L.R. 409"
neutral_cite: 1925 U.S. LEXIS 2
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1925
date_decided: 1925-10-12
docket: 6
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1925-10-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Agnello v. United States
  varies_by_point: false
  scope_note: "Foundational early limit on search incident to arrest; the rule that a SITA does not reach a separate home away from the arrest survives and is consistent with Chimel v. California."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/100711/agnello-v-united-states/"
  cluster_id: 100711
  opinion_id: 100711
  identity_checked: true
homes:
  - page: "[[SIA Persons]]"
    role: "Key — Historical / Foundational"
related: ["[[Chimel v. California]]", "[[Go-Bart Importing Co. v. United States]]", "[[Weeks v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "home", "historical", "warrant-requirement"]
holding: "A search incident to arrest reaches the arrestee's person and the place where the arrest is made, but does not extend to a separate house blocks away that is entered and searched without a warrant after the arrest is complete and the suspects are in custody elsewhere."
lake:
  record_id: Agnello v. United States
  status: verified
  projected_at: 2026-07-06
---

# Agnello v. United States

*269 U.S. 20 (1925)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal revenue agents watched a cocaine sale at Alba's house and, when it was consummated, rushed in and arrested the defendants there, seizing cocaine on the table and on Frank Agnello's person. While some agents took the defendants to the station, others went — without a search warrant — to Frank Agnello's home several blocks away, searched his bedroom, and found a can of cocaine. That can was ultimately admitted against him.

## Issue
Whether the warrantless search of the arrestee's home, several blocks from the place of arrest and after he was in custody elsewhere, can be justified as a [[Search Incident to Arrest|search incident to arrest]].

## Rule
A [[Search Incident to Arrest|search incident to arrest]] is real but bounded to the arrest scene: "The right without a search warrant contemporaneously to search persons lawfully arrested while committing crime and to search the place where the arrest is made in order to find and seize things connected with the crime as its fruits or as the means by which it was committed, as well as weapons and other things to effect an escape from custody, is not to be doubted." — 269 U.S. at 30. ^pin-30

But it does not reach a separate home: "But the right does not extend to other places. Frank Agnello's house was several blocks distant from Alba's house, where the arrest was made. When it was entered and searched, the conspiracy was ended and the defendants were under arrest and in custody elsewhere. That search cannot be sustained as an incident of the arrests." — *Id.* at 30–31. ^pin-30a

## Application
The arrests and the searches and seizures at Alba's house — where the arrests occurred — were not questioned. But Agnello's house was blocks away; by the time agents entered and searched it without a warrant, the sale was over and the defendants were already in custody at or en route to the station. Nothing about the arrest justified that separate, later search, so the can of cocaine found in his bedroom was the product of an unreasonable warrantless search.

## Conclusion
Reversed. The warrantless search of Agnello's distant home could not be sustained as incident to the arrest; the evidence should have been excluded. *Agnello* fixes an early geographic and temporal limit on [[Search Incident to Arrest|search incident to arrest]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The limit survives and is consistent with the modern boundary drawn in [[Chimel v. California]] (SITA confined to the arrestee's person and the area within immediate control); it is companion to [[Go-Bart Importing Co. v. United States]] (no general exploratory search) and builds on [[Weeks v. United States]].

## Appears on
- [[SIA Persons]] — *Key — Historical / Foundational*

## Sources
- *Agnello v. United States*, 269 U.S. 20 (1925) — https://www.courtlistener.com/opinion/100711/agnello-v-united-states/ — pinpoints: 30, 31.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d9ebf80326bab179", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "269 U.S. 20 (1925)", "court": "U.S. Supreme Court", "neutral_cite": "1925 U.S. LEXIS 2", "official_citation_present": true, "parallel_cite": "46 S. Ct. 4; 70 L. Ed. 145; 51 A.L.R. 409", "title": "Agnello v. United States", "year": "1925"}}
{"assertion_id": "39f1a340db4a39e5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A search incident to arrest reaches the arrestee's person and the place where the arrest is made, but does not extend to a separate house blocks away that is entered and searched without a warrant after the arrest is complete and the suspects are in custody elsewhere.", "title": "Agnello v. United States"}}
{"assertion_id": "f3480c9b9320040b", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Persons"}, "payload": {"home": "SIA Persons", "role": "Key — Historical / Foundational", "title": "Agnello v. United States"}}
{"assertion_id": "01a1d39ad8879ad6", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Agnello v. United States"}}
{"assertion_id": "bf6893b847fae0cd", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1925-10-12", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Agnello v. United States", "field_i_validity": "good_law", "scope_note": "Foundational early limit on search incident to arrest; the rule that a SITA does not reach a separate home away from the arrest survives and is consistent with Chimel v. California.", "title": "Agnello v. United States", "varies_by_point": "false"}}
```

### lake record — Agnello v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Agnello v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Agnello v. United States",
    "case_name_short": "Agnello",
    "case_name_full": "AGNELLO Et Al. v. UNITED STATES",
    "input_case_name": "Agnello v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1925-10-12",
    "year": 1925,
    "docket": "6",
    "cluster_id": 100711,
    "lead_opinion_id": 100711,
    "sibling_ids": [
      100711
    ],
    "absolute_url": "/opinion/100711/agnello-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "269 U.S. 20",
      "volume": "269",
      "reporter": "U.S.",
      "page": "20",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "46 S. Ct. 4",
        "volume": "46",
        "reporter": "S. Ct.",
        "page": "4",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "70 L. Ed. 145",
        "volume": "70",
        "reporter": "L. Ed.",
        "page": "145",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 A.L.R. 409",
        "volume": "51",
        "reporter": "A.L.R.",
        "page": "409",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1925 U.S. LEXIS 2",
        "volume": "1925",
        "reporter": "U.S. LEXIS",
        "page": "2",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "269 U.S. 20",
        "volume": "269",
        "reporter": "U.S.",
        "page": "20",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "46 S. Ct. 4",
        "volume": "46",
        "reporter": "S. Ct.",
        "page": "4",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "70 L. Ed. 145",
        "volume": "70",
        "reporter": "L. Ed.",
        "page": "145",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1925 U.S. LEXIS 2",
        "volume": "1925",
        "reporter": "U.S. LEXIS",
        "page": "2",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 A.L.R. 409",
        "volume": "51",
        "reporter": "A.L.R.",
        "page": "409",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "269 U.S. 20",
    "official_selection": {
      "court_class": "scotus",
      "selected": "269 U.S. 20",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-30",
      "page": null,
      "quote": "--- # Agnello v. United States *269 U.S. 20 (1925)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal revenue agents watched a cocaine sale at Alba's house and, when it was consummated, rushed in and arrested the defendants there, seizing cocaine on the table and on Frank Agnello's person. While some agents took the defendants to the station, others went \u2014 without a search warrant \u2014 to Frank Agnello's home several blocks away, searched his bedroom, and found a can of cocaine. That can was ultimately admitted against him. ## Issue Whether the warrantless search of the arrestee's home, several blocks from the place of arrest and after he was in custody elsewhere, can be justified as a search incident to arrest. ## Rule A search incident to arrest is real but bounded to the arrest scene:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-30a",
      "page": null,
      "quote": "But the right does not extend to other places. Frank Agnello's house was several blocks distant from Alba's house, where the arrest was made. When it was entered and searched, the conspiracy was ended and the defendants were under arrest and in custody elsewhere. That search cannot be sustained as an incident of the arrests.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1925-10-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Agnello v. United States",
    "varies_by_point": false,
    "scope_note": "Foundational early limit on search incident to arrest; the rule that a SITA does not reach a separate home away from the arrest survives and is consistent with Chimel v. California.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Leonard",
          "cluster_id": 10789713,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Camper",
          "cluster_id": 9454678,
          "cite": [
            "232 N.E.3d 419",
            "2023 Ohio 4673"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jenkins v. Dragoo & Assocs., Inc.",
          "cluster_id": 9439763,
          "cite": [
            "229 N.E.3d 140",
            "2023 Ohio 4103"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Renee Michelle Parady v. Commonwealth of Virginia",
          "cluster_id": 9411484,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Hannah Marie Kilby",
          "cluster_id": 5290146,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Hannah Marie Kilby",
          "cluster_id": 4893115,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Manuel Garcia",
          "cluster_id": 10109643,
          "cite": [
            "951 N.W.2d 631",
            "394 Wis. 2d 743",
            "2020 WI App 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Whittington v. State",
          "cluster_id": 10021170,
          "cite": [
            "230 A.3d 148",
            "246 Md. App. 451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "v. Johnson",
          "cluster_id": 4672578,
          "cite": [
            "2019 COA 159"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pacheco v. State",
          "cluster_id": 10048657,
          "cite": [
            "465 Md. 311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pacheco v. State",
          "cluster_id": 4647520,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jessica M. Randall",
          "cluster_id": 4635900,
          "cite": [
            "930 N.W.2d 223",
            "2019 WI 80",
            "387 Wis. 2d 744"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Mayfield",
          "cluster_id": 4588394,
          "cite": [
            "434 P.3d 58",
            "192 Wash. 2d 871"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Corona",
          "cluster_id": 5310101,
          "cite": [
            "2018 UT App 154",
            "436 P.3d 174"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ward",
          "cluster_id": 4433423,
          "cite": [
            "2017 Ohio 8141",
            "98 N.E.3d 1257"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gutierrez-Hernandez v. State",
          "cluster_id": 4409141,
          "cite": [
            "221 So. 3d 792",
            "2017 Fla. App. LEXIS 10099",
            "2017 WL 2989013"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vincent Milewski v. Town of Dover",
          "cluster_id": 4408481,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vincent Milewski v. Town of Dover",
          "cluster_id": 4407393,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vincent Milewski v. Town of Dover",
          "cluster_id": 4407039,
          "cite": [
            "377 Wis. 2d 38",
            "2017 WI 79",
            "899 N.W.2d 303",
            "2017 WL 2883925",
            "2017 Wisc. LEXIS 396"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Leslie",
          "cluster_id": 4389764,
          "cite": [
            "477 Mass. 48",
            "76 N.E.3d 978"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "UNITED STATES v. DAVID D. LEWIS",
          "cluster_id": 4281856,
          "cite": [
            "147 A.3d 236",
            "2016 D.C. App. LEXIS 369",
            "2016 WL 5539892"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In the Int. of: I.M.S., a Minor",
          "cluster_id": 2898309,
          "cite": [
            "124 A.3d 311",
            "2015 Pa. Super. 188",
            "2015 Pa. Super. LEXIS 514"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Washington v. Heath T. Wisdom",
          "cluster_id": 2801822,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Paselk, Ex Parte Carol",
          "cluster_id": 4262512,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City of Beatrice v. Meints",
          "cluster_id": 2757932,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Littell",
          "cluster_id": 2744514,
          "cite": [
            "2014 Ohio 4654"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brandon Q. Gales v. State of Mississippi",
          "cluster_id": 2741345,
          "cite": [
            "153 So. 3d 632",
            "2014 Miss. LEXIS 501",
            "2014 WL 5035944"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Amended October 15, 2014 State of Iowa v. Justin Dean Short",
          "cluster_id": 4472150,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Justin Dean Short",
          "cluster_id": 2687558,
          "cite": [
            "851 N.W.2d 474",
            "2014 WL 3537029",
            "2014 Iowa Sup. LEXIS 86"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Perea-Rey",
          "cluster_id": 801335,
          "cite": [
            "680 F.3d 1179",
            "2012 U.S. App. LEXIS 10941",
            "2012 WL 1948973"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Gentle",
          "cluster_id": 6589626,
          "cite": [
            "80 Mass. App. Ct. 243",
            "952 N.E.2d 426",
            "2011 Mass. App. LEXIS 1134"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Harding",
          "cluster_id": 2550601,
          "cite": [
            "9 A.3d 547",
            "196 Md. App. 384",
            "2010 Md. App. LEXIS 182"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Joshua Daniel Fleming",
          "cluster_id": 4472496,
          "cite": [
            "790 N.W.2d 560",
            "2010 Iowa Sup. LEXIS 110"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Marshall",
          "cluster_id": 2273474,
          "cite": [
            "319 S.W.3d 352",
            "2010 Ky. LEXIS 182",
            "2010 WL 3374171"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ramirez",
          "cluster_id": 149658,
          "cite": [
            "609 F.3d 495",
            "2010 U.S. App. LEXIS 13200",
            "2010 WL 2574123"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Belote v. State",
          "cluster_id": 1912680,
          "cite": [
            "981 A.2d 1247",
            "411 Md. 104",
            "2009 Md. LEXIS 743"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tatman",
          "cluster_id": 2482593,
          "cite": [
            "615 F. Supp. 2d 664",
            "2008 U.S. Dist. LEXIS 106022",
            "2008 WL 5431163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Keith",
          "cluster_id": 3965884,
          "cite": [
            "178 Ohio App. 3d 46",
            "2008 Ohio 4326",
            "896 N.E.2d 764"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Smith, 07-Ca-47 (7-25-2008)",
          "cluster_id": 4015581,
          "cite": [
            "2008 Ohio 3717"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sanders",
          "cluster_id": 1873366,
          "cite": [
            "2008 WI 85",
            "752 N.W.2d 713",
            "311 Wis. 2d 257",
            "2008 Wisc. LEXIS 336"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sharpe",
          "cluster_id": 3971545,
          "cite": [
            "174 Ohio App. 3d 498",
            "2008 Ohio 267",
            "882 N.E.2d 960"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gray",
          "cluster_id": 2968497,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Joshua Brent Gray, United States of America v. Terrence A. Askew",
          "cluster_id": 798157,
          "cite": [
            "491 F.3d 138",
            "2007 U.S. App. LEXIS 15760",
            "2007 WL 1881194"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Warren",
          "cluster_id": 1800687,
          "cite": [
            "949 So. 2d 1215",
            "2007 WL 530029"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sherman",
          "cluster_id": 1129307,
          "cite": [
            "931 So. 2d 286",
            "2006 WL 860652"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Carvalho",
          "cluster_id": 1925493,
          "cite": [
            "892 A.2d 140",
            "2006 R.I. LEXIS 29",
            "2006 WL 537913"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Eckel",
          "cluster_id": 2112994,
          "cite": [
            "888 A.2d 1266",
            "185 N.J. 523",
            "2006 N.J. LEXIS 2"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thornton v. United States",
          "cluster_id": 134746,
          "cite": [
            "158 L. Ed. 2d 905",
            "124 S. Ct. 2127",
            "541 U.S. 615",
            "2004 U.S. LEXIS 3681"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Carter",
          "cluster_id": 2639057,
          "cite": [
            "85 P.3d 887"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Carpenter, Sheila",
          "cluster_id": 2971092,
          "cite": [
            "360 F.3d 591",
            "2004 WL 419906"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Carpenter",
          "cluster_id": 785340,
          "cite": [
            "360 F.3d 591",
            "2004 U.S. App. LEXIS 4435"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Spencer v. City of Bay City",
          "cluster_id": 2331528,
          "cite": [
            "292 F. Supp. 2d 932",
            "2003 U.S. Dist. LEXIS 21242",
            "2003 WL 22801139"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dunnuck v. State",
          "cluster_id": 1469197,
          "cite": [
            "786 A.2d 695",
            "367 Md. 198",
            "2001 Md. LEXIS 943"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gilley",
          "cluster_id": 4282804,
          "cite": [
            "56 M.J. 113",
            "2001 CAAF LEXIS 1378",
            "2001 WL 1441832"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mason v. Wrightson",
          "cluster_id": 2206253,
          "cite": [
            "109 A.2d 128",
            "205 Md. 481"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Griffin v. State",
          "cluster_id": 2269214,
          "cite": [
            "92 A.2d 743",
            "200 Md. 569"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Funkhouser",
          "cluster_id": 2386458,
          "cite": [
            "782 A.2d 387",
            "140 Md. App. 696",
            "2001 Md. App. LEXIS 161"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Parker",
          "cluster_id": 1401702,
          "cite": [
            "987 P.2d 73"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Matthews",
          "cluster_id": 4282934,
          "cite": [
            "53 M.J. 465",
            "2000 CAAF LEXIS 950",
            "2000 WL 1239211"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Moyer v. Commonwealth",
          "cluster_id": 1065604,
          "cite": [
            "531 S.E.2d 580",
            "33 Va. App. 8",
            "2000 Va. App. LEXIS 557"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Moyer v. Commonwealth",
          "cluster_id": 1238318,
          "cite": [
            "520 S.E.2d 371",
            "30 Va. App. 744",
            "1999 Va. App. LEXIS 596"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Longcore",
          "cluster_id": 2209414,
          "cite": [
            "593 N.W.2d 412",
            "226 Wis. 2d 1",
            "1999 Wisc. App. LEXIS 307"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Glasco v. Commonwealth",
          "cluster_id": 1059787,
          "cite": [
            "513 S.E.2d 137",
            "257 Va. 433",
            "1999 Va. LEXIS 41"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Wagoner",
          "cluster_id": 2609356,
          "cite": [
            "966 P.2d 176",
            "126 N.M. 9",
            "1998 NMCA 124"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pierce v. Smith",
          "cluster_id": 12443,
          "cite": [
            "117 F.3d 866",
            "13 I.E.R. Cas. (BNA) 8",
            "1997 U.S. App. LEXIS 17907",
            "1997 WL 395259"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Titus v. State",
          "cluster_id": 1728813,
          "cite": [
            "696 So. 2d 1257",
            "1997 WL 360959"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Accardi",
          "cluster_id": 3136153,
          "cite": [
            "284 Ill. App. 3d 31"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Green v. State",
          "cluster_id": 2194990,
          "cite": [
            "676 N.E.2d 755",
            "1997 WL 33862"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kristopher Roth v. State",
          "cluster_id": 2859172,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Roth v. State",
          "cluster_id": 1723172,
          "cite": [
            "917 S.W.2d 292",
            "1995 Tex. App. LEXIS 3296",
            "1995 WL 675583"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Stubbs",
          "cluster_id": 883728,
          "cite": [
            "892 P.2d 547",
            "270 Mont. 364",
            "52 State Rptr. 232",
            "1995 Mont. LEXIS 50"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Pierce",
          "cluster_id": 2009627,
          "cite": [
            "642 A.2d 947",
            "136 N.J. 184",
            "1994 N.J. LEXIS 495"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chun Yen Chiu",
          "cluster_id": 2008300,
          "cite": [
            "857 F. Supp. 353",
            "1993 U.S. Dist. LEXIS 20112",
            "1993 WL 721298"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wilkes v. United States",
          "cluster_id": 2329036,
          "cite": [
            "631 A.2d 880",
            "1993 D.C. App. LEXIS 233",
            "1993 WL 375307"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Miller",
          "cluster_id": 7906180,
          "cite": [
            "29 Conn. App. 207",
            "614 A.2d 1229",
            "1992 Conn. App. LEXIS 368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Mullins",
          "cluster_id": 6080465,
          "cite": [
            "179 A.D.2d 48",
            "582 N.Y.S.2d 810",
            "1992 N.Y. App. Div. LEXIS 5279"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Fairchild",
          "cluster_id": 1424081,
          "cite": [
            "829 P.2d 550",
            "121 Idaho 960",
            "1992 Ida. App. LEXIS 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Six Hundred Thirty-Nine Thousand Five Hundred and Fifty-Eight Dollars ($639,558) in United States Currency",
          "cluster_id": 577094,
          "cite": [
            "955 F.2d 712",
            "293 U.S. App. D.C. 384",
            "1992 U.S. App. LEXIS 1433",
            "1992 WL 18289"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rivera",
          "cluster_id": 8708533,
          "cite": [
            "762 F. Supp. 49",
            "1991 U.S. Dist. LEXIS 4014",
            "1991 WL 60088"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gordon v. State",
          "cluster_id": 1638510,
          "cite": [
            "801 S.W.2d 899",
            "1990 Tex. Crim. App. LEXIS 203",
            "1990 WL 199137"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Garcia",
          "cluster_id": 2437892,
          "cite": [
            "794 S.W.2d 472",
            "1990 WL 83587"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. O'DELL",
          "cluster_id": 1435360,
          "cite": [
            "576 A.2d 425",
            "1990 R.I. LEXIS 118",
            "1990 WL 79415"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Camilleri",
          "cluster_id": 2143661,
          "cite": [
            "220 Cal. App. 3d 1199",
            "269 Cal. Rptr. 862",
            "1990 Cal. App. LEXIS 550"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Roundtree",
          "cluster_id": 1874558,
          "cite": [
            "694 F. Supp. 1230",
            "1988 WL 96725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Crosby v. Commonwealth",
          "cluster_id": 1225752,
          "cite": [
            "367 S.E.2d 730",
            "6 Va. App. 193",
            "4 Va. Law Rep. 2341",
            "1988 Va. App. LEXIS 39"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Malik",
          "cluster_id": 1533332,
          "cite": [
            "534 A.2d 27",
            "221 N.J. Super. 114"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Brunelle",
          "cluster_id": 1533148,
          "cite": [
            "534 A.2d 198",
            "148 Vt. 347",
            "1987 Vt. LEXIS 513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Reed Wayne Hamilton v. Crispus Nix, Warden, and Attorney General of the State of Iowa",
          "cluster_id": 481691,
          "cite": [
            "809 F.2d 463",
            "1987 U.S. App. LEXIS 938"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cathey",
          "cluster_id": 1658376,
          "cite": [
            "493 So. 2d 842"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Voelkel v. State",
          "cluster_id": 2461220,
          "cite": [
            "717 S.W.2d 314",
            "1986 Tex. Crim. App. LEXIS 1274"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Collins v. United States",
          "cluster_id": 2265688,
          "cite": [
            "491 A.2d 480"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kao",
          "cluster_id": 878927,
          "cite": [
            "697 P.2d 903",
            "215 Mont. 277"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ralph Joseph Palumbo",
          "cluster_id": 440435,
          "cite": [
            "742 F.2d 656",
            "1984 U.S. App. LEXIS 18582"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ortiz",
          "cluster_id": 1159713,
          "cite": [
            "683 P.2d 822",
            "67 Haw. 181",
            "1984 Haw. LEXIS 107"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "LeMasters v. People",
          "cluster_id": 1216986,
          "cite": [
            "678 P.2d 538",
            "1984 Colo. LEXIS 501"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ringer",
          "cluster_id": 1248379,
          "cite": [
            "674 P.2d 1240",
            "100 Wash. 2d 686",
            "1983 Wash. LEXIS 1922"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Stackhouse v. State",
          "cluster_id": 2275066,
          "cite": [
            "468 A.2d 333",
            "298 Md. 203",
            "1983 Md. LEXIS 341"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Dickson",
          "cluster_id": 2163530,
          "cite": [
            "144 Cal. App. 3d 1046",
            "192 Cal. Rptr. 897",
            "1983 Cal. App. LEXIS 1897"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lopez-Mendoza v. Immigration & Naturalization Service",
          "cluster_id": 8927000,
          "cite": [
            "705 F.2d 1059",
            "1983 U.S. App. LEXIS 28584"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Castaneda v. State",
          "cluster_id": 5234027,
          "cite": [
            "650 S.W.2d 211",
            "1983 Tex. App. LEXIS 4340"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Russell v. State",
          "cluster_id": 2456197,
          "cite": [
            "644 S.W.2d 554"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Calegar",
          "cluster_id": 1178435,
          "cite": [
            "661 P.2d 311",
            "104 Idaho 526",
            "1983 Ida. LEXIS 420"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Golden v. State",
          "cluster_id": 1647005,
          "cite": [
            "429 So. 2d 45"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Caraher",
          "cluster_id": 1188275,
          "cite": [
            "653 P.2d 942",
            "293 Or. 741",
            "1982 Ore. LEXIS 1190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Duncan v. State",
          "cluster_id": 1518530,
          "cite": [
            "639 S.W.2d 314",
            "1982 Tex. Crim. App. LEXIS 1108"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States of America Ex Rel. Ronald Doss v. Lou v. Brewer, Warden",
          "cluster_id": 407609,
          "cite": [
            "685 F.2d 1003"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Bradley",
          "cluster_id": 2119659,
          "cite": [
            "132 Cal. App. 3d 737",
            "183 Cal. Rptr. 434",
            "1982 Cal. App. LEXIS 1657"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Heumiller",
          "cluster_id": 1641433,
          "cite": [
            "317 N.W.2d 126",
            "1982 S.D. LEXIS 271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Capps",
          "cluster_id": 1222613,
          "cite": [
            "641 P.2d 484",
            "97 N.M. 453"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gill v. State",
          "cluster_id": 1770662,
          "cite": [
            "625 S.W.2d 307",
            "1981 Tex. Crim. App. LEXIS 1283"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Congeni",
          "cluster_id": 3937272,
          "cite": [
            "445 N.E.2d 698",
            "3 Ohio App. 3d 392",
            "3 Ohio B. 457",
            "1981 Ohio App. LEXIS 10078"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Evans",
          "cluster_id": 1899913,
          "cite": [
            "438 A.2d 340",
            "181 N.J. Super. 455"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robbins v. California",
          "cluster_id": 110558,
          "cite": [
            "69 L. Ed. 2d 744",
            "101 S. Ct. 2841",
            "453 U.S. 420",
            "1981 U.S. LEXIS 132"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Roberts",
          "cluster_id": 1502467,
          "cite": [
            "434 A.2d 257",
            "1981 R.I. LEXIS 1258"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Henighan v. United States",
          "cluster_id": 2280122,
          "cite": [
            "433 A.2d 1059",
            "1981 D.C. App. LEXIS 315"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Parkhurst v. State",
          "cluster_id": 2605745,
          "cite": [
            "628 P.2d 1369",
            "1981 Wyo. LEXIS 347"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Hernandez",
          "cluster_id": 389504,
          "cite": [
            "646 F.2d 970",
            "8 Fed. R. Serv. 794",
            "1981 U.S. App. LEXIS 12727"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Steagald v. United States",
          "cluster_id": 110464,
          "cite": [
            "68 L. Ed. 2d 38",
            "101 S. Ct. 1642",
            "451 U.S. 204",
            "1981 U.S. LEXIS 89",
            "49 U.S.L.W. 4418"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Griffin",
          "cluster_id": 2613893,
          "cite": [
            "626 P.2d 478",
            "1981 Utah LEXIS 723"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Donelson",
          "cluster_id": 2172888,
          "cite": [
            "302 N.W.2d 125",
            "1981 Iowa Sup. LEXIS 890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Luz-Estella Alvarez-Porras, Jose Garcia-Perez, and Roberto Colon-Diaz",
          "cluster_id": 388070,
          "cite": [
            "643 F.2d 54",
            "8 Fed. R. Serv. 242",
            "1981 U.S. App. LEXIS 20295"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ross v. Stahl",
          "cluster_id": 1512993,
          "cite": [
            "502 F. Supp. 107",
            "7 Fed. R. Serv. 1306",
            "1980 U.S. Dist. LEXIS 14639"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Spies",
          "cluster_id": 1242066,
          "cite": [
            "615 P.2d 710",
            "200 Colo. 434",
            "1980 Colo. LEXIS 709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Havens",
          "cluster_id": 110267,
          "cite": [
            "64 L. Ed. 2d 559",
            "100 S. Ct. 1912",
            "446 U.S. 620",
            "1980 U.S. LEXIS 103"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Payton v. New York",
          "cluster_id": 110235,
          "cite": [
            "63 L. Ed. 2d 639",
            "100 S. Ct. 1371",
            "445 U.S. 573",
            "1980 U.S. LEXIS 13"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Christian v. State",
          "cluster_id": 1566358,
          "cite": [
            "592 S.W.2d 625",
            "1980 Tex. Crim. App. LEXIS 1063"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Heitman",
          "cluster_id": 1571293,
          "cite": [
            "589 S.W.2d 249",
            "1979 Mo. LEXIS 338"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ramos v. Seidl",
          "cluster_id": 2263801,
          "cite": [
            "479 F. Supp. 771",
            "1979 U.S. Dist. LEXIS 8741"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Charles Emmett Hoffman",
          "cluster_id": 370457,
          "cite": [
            "607 F.2d 280",
            "1979 U.S. App. LEXIS 10927"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ibn-Tamas v. United States",
          "cluster_id": 1910611,
          "cite": [
            "407 A.2d 626",
            "1979 D.C. App. LEXIS 457"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Knox v. State",
          "cluster_id": 1632971,
          "cite": [
            "586 S.W.2d 504",
            "1979 Tex. Crim. App. LEXIS 1650"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hudson v. State",
          "cluster_id": 1510190,
          "cite": [
            "588 S.W.2d 348",
            "1979 Tex. Crim. App. LEXIS 1616"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Federici",
          "cluster_id": 1973144,
          "cite": [
            "179 Conn. 46",
            "425 A.2d 916",
            "1979 Conn. LEXIS 912"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Stanley",
          "cluster_id": 2082590,
          "cite": [
            "401 A.2d 1166",
            "265 Pa. Super. 194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Seiss",
          "cluster_id": 1497008,
          "cite": [
            "402 A.2d 972",
            "168 N.J. Super. 269"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Anthony Hickey, United States v. William Lloyd Ferreira",
          "cluster_id": 365612,
          "cite": [
            "596 F.2d 1082",
            "1979 U.S. App. LEXIS 15297"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Erb, Mark C. Perschbacher, John E. Lavell, Michael S. Mosley",
          "cluster_id": 365526,
          "cite": [
            "596 F.2d 412",
            "1979 U.S. App. LEXIS 15624"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. J. Lee Havens",
          "cluster_id": 363621,
          "cite": [
            "592 F.2d 848",
            "1979 U.S. App. LEXIS 15634"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Forsythe",
          "cluster_id": 364657,
          "cite": [
            "594 F.2d 947"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cadena",
          "cluster_id": 360399,
          "cite": [
            "585 F.2d 1252"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Wise",
          "cluster_id": 5683261,
          "cite": [
            "46 N.Y.2d 321",
            "385 N.E.2d 1262",
            "413 N.Y.S.2d 334",
            "14 A.L.R. 4th 666",
            "1978 N.Y. LEXIS 2422"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Garle A. Whitson",
          "cluster_id": 361132,
          "cite": [
            "587 F.2d 948"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Warren",
          "cluster_id": 1417762,
          "cite": [
            "589 P.2d 1338",
            "121 Ariz. 306",
            "1978 Ariz. App. LEXIS 719"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cadena",
          "cluster_id": 8919342,
          "cite": [
            "585 F.2d 1252",
            "1979 A.M.C. 1934"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brenneman v. State",
          "cluster_id": 1773897,
          "cite": [
            "573 S.W.2d 47",
            "264 Ark. 460",
            "1978 Ark. LEXIS 2141"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Saundra Prescott",
          "cluster_id": 358848,
          "cite": [
            "581 F.2d 1343",
            "1978 U.S. App. LEXIS 9041"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ross",
          "cluster_id": 1225463,
          "cite": [
            "246 S.E.2d 780",
            "295 N.C. 488",
            "1978 N.C. LEXIS 1015"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Silo",
          "cluster_id": 2073312,
          "cite": [
            "389 A.2d 62",
            "480 Pa. 15",
            "1978 Pa. LEXIS 780"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Payton",
          "cluster_id": 5683033,
          "cite": [
            "45 N.Y.2d 300",
            "408 N.Y.S.2d 395",
            "1978 N.Y. LEXIS 2144",
            "380 N.E.2d 224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Parkinson",
          "cluster_id": 2073303,
          "cite": [
            "389 A.2d 1",
            "1978 Me. LEXIS 770"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Means",
          "cluster_id": 876687,
          "cite": [
            "581 P.2d 406",
            "177 Mont. 193",
            "1978 Mont. LEXIS 835"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Providence Journal Co. v. Federal Bureau of Investigation",
          "cluster_id": 2093217,
          "cite": [
            "460 F. Supp. 762",
            "27 Fed. R. Serv. 2d 143",
            "1978 U.S. Dist. LEXIS 17769"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ward v. United States",
          "cluster_id": 1935714,
          "cite": [
            "386 A.2d 1180",
            "1978 D.C. App. LEXIS 375"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Maxwell",
          "cluster_id": 2147794,
          "cite": [
            "78 Cal. App. 3d 124",
            "144 Cal. Rptr. 95",
            "1978 Cal. App. LEXIS 1289"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Volpicelli v. Salamack",
          "cluster_id": 1620955,
          "cite": [
            "447 F. Supp. 652",
            "1978 U.S. Dist. LEXIS 19416"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Shaw",
          "cluster_id": 2388761,
          "cite": [
            "383 A.2d 496",
            "476 Pa. 543",
            "1978 Pa. LEXIS 840"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Peterson v. State",
          "cluster_id": 1468214,
          "cite": [
            "379 A.2d 164",
            "281 Md. 309",
            "1977 Md. LEXIS 595"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Stinchfield v. State",
          "cluster_id": 2056758,
          "cite": [
            "367 N.E.2d 1150",
            "174 Ind. App. 423",
            "1977 Ind. App. LEXIS 992"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Isaacks v. State",
          "cluster_id": 1927176,
          "cite": [
            "350 So. 2d 1340"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. George Moss and American Identification Products",
          "cluster_id": 349228,
          "cite": [
            "562 F.2d 155",
            "14 Collier Bankr. Cas. 2d 279",
            "1977 U.S. App. LEXIS 11674"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Crawl",
          "cluster_id": 1892052,
          "cite": [
            "257 N.W.2d 86",
            "401 Mich. 1",
            "1977 Mich. LEXIS 154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. William Courtney Batts",
          "cluster_id": 347031,
          "cite": [
            "558 F.2d 513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kidd",
          "cluster_id": 2168949,
          "cite": [
            "375 A.2d 1105",
            "281 Md. 32",
            "1977 Md. LEXIS 570"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Perez",
          "cluster_id": 1817744,
          "cite": [
            "440 F. Supp. 272",
            "1977 U.S. Dist. LEXIS 16266"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. John R. James, Jr.",
          "cluster_id": 345567,
          "cite": [
            "555 F.2d 992",
            "181 U.S. App. D.C. 55",
            "1 Fed. R. Serv. 895",
            "1977 U.S. App. LEXIS 13953"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Monahan",
          "cluster_id": 2229181,
          "cite": [
            "251 N.W.2d 421",
            "76 Wis. 2d 387",
            "261 N.W.2d 421",
            "1977 Wisc. LEXIS 1362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. John D. Ehrlichman",
          "cluster_id": 341470,
          "cite": [
            "546 F.2d 910",
            "178 U.S. App. D.C. 144"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cravero",
          "cluster_id": 340675,
          "cite": [
            "545 F.2d 406"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Tyler",
          "cluster_id": 1273756,
          "cite": [
            "250 N.W.2d 467",
            "399 Mich. 564"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Carroll D. Ford. United States of America v. Wesley Dessaso A/K/A Wesley Dessaso, Jr. United States of America v. Steve F. Dacosta. United States of America v. Daniel Haile, Jr. United States of America v. Melvin E. Smith",
          "cluster_id": 344771,
          "cite": [
            "553 F.2d 146"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 1722607,
          "cite": [
            "249 N.W.2d 693",
            "399 Mich. 350",
            "1976 Mich. LEXIS 220"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Wolgemuth",
          "cluster_id": 2245378,
          "cite": [
            "356 N.E.2d 1139",
            "43 Ill. App. 3d 335",
            "1 Ill. Dec. 857",
            "1976 Ill. App. LEXIS 3294"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Alfred B. Diggs",
          "cluster_id": 340058,
          "cite": [
            "544 F.2d 116",
            "1976 U.S. App. LEXIS 7361"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cravero",
          "cluster_id": 8912462,
          "cite": [
            "545 F.2d 406",
            "2 Fed. R. Serv. 223"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ralph Mariani",
          "cluster_id": 338326,
          "cite": [
            "539 F.2d 915",
            "1976 U.S. App. LEXIS 7955"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Opperman",
          "cluster_id": 109537,
          "cite": [
            "49 L. Ed. 2d 1000",
            "96 S. Ct. 3092",
            "428 U.S. 364",
            "1976 U.S. LEXIS 15"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Glover v. State",
          "cluster_id": 1296375,
          "cite": [
            "227 S.E.2d 921",
            "139 Ga. App. 162",
            "1976 Ga. App. LEXIS 1719"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. COOPER",
          "cluster_id": 1538291,
          "cite": [
            "240 Pa. Super. 477",
            "362 A.2d 1041",
            "1976 Pa. Super. LEXIS 1937"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Fisher v. United States",
          "cluster_id": 109432,
          "cite": [
            "48 L. Ed. 2d 39",
            "96 S. Ct. 1569",
            "425 U.S. 391",
            "1976 U.S. LEXIS 98",
            "37 A.F.T.R.2d (RIA) 1244"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Evans",
          "cluster_id": 5946417,
          "cite": [
            "52 A.D.2d 32",
            "382 N.Y.S.2d 399",
            "1976 N.Y. App. Div. LEXIS 11525"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thomas v. State",
          "cluster_id": 1774097,
          "cite": [
            "572 S.W.2d 507",
            "1976 Tex. Crim. App. LEXIS 1210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Disbrow",
          "cluster_id": 1185789,
          "cite": [
            "545 P.2d 272",
            "16 Cal. 3d 101",
            "127 Cal. Rptr. 360",
            "1976 Cal. LEXIS 210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Diaz",
          "cluster_id": 6354097,
          "cite": [
            "85 Misc. 2d 41",
            "1975 N.Y. Misc. LEXIS 3274",
            "376 N.Y.S.2d 849"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Terry v. Ohio",
          "cluster_id": 107729,
          "cite": [
            "20 L. Ed. 2d 889",
            "88 S. Ct. 1868",
            "392 U.S. 1",
            "1968 U.S. LEXIS 1345",
            "44 Ohio Op. 2d 383"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
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
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Glasser v. United States",
          "cluster_id": 103597,
          "cite": [
            "315 U.S. 60",
            "62 S. Ct. 457",
            "86 L. Ed. 680",
            "1942 U.S. LEXIS 979"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
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
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chimel v. California",
          "cluster_id": 107979,
          "cite": [
            "23 L. Ed. 2d 685",
            "89 S. Ct. 2034",
            "395 U.S. 752",
            "1969 U.S. LEXIS 1166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. United States",
          "cluster_id": 106022,
          "cite": [
            "4 L. Ed. 2d 697",
            "80 S. Ct. 725",
            "362 U.S. 257",
            "1960 U.S. LEXIS 1413",
            "78 A.L.R. 2d 233"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chambers v. Maroney",
          "cluster_id": 108184,
          "cite": [
            "26 L. Ed. 2d 419",
            "90 S. Ct. 1975",
            "399 U.S. 42",
            "1970 U.S. LEXIS 19"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ventresca",
          "cluster_id": 106990,
          "cite": [
            "13 L. Ed. 2d 684",
            "85 S. Ct. 741",
            "380 U.S. 102",
            "1965 U.S. LEXIS 2438",
            "16 A.F.T.R.2d (RIA) 5787"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. United States",
          "cluster_id": 104504,
          "cite": [
            "92 L. Ed. 2d 436",
            "68 S. Ct. 367",
            "333 U.S. 10",
            "1948 U.S. LEXIS 2583",
            "92 L. Ed. 436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gilbert v. California",
          "cluster_id": 107487,
          "cite": [
            "18 L. Ed. 2d 1178",
            "87 S. Ct. 1951",
            "388 U.S. 263",
            "1967 U.S. LEXIS 1086"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Camara v. Municipal Court of City and County of San Francisco",
          "cluster_id": 107473,
          "cite": [
            "18 L. Ed. 2d 930",
            "87 S. Ct. 1727",
            "387 U.S. 523",
            "1967 U.S. LEXIS 1254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Robinson",
          "cluster_id": 108893,
          "cite": [
            "38 L. Ed. 2d 427",
            "94 S. Ct. 467",
            "414 U.S. 218",
            "1973 U.S. LEXIS 21",
            "66 Ohio Op. 2d 202"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warden, Maryland Penitentiary v. Hayden",
          "cluster_id": 107465,
          "cite": [
            "18 L. Ed. 2d 782",
            "87 S. Ct. 1642",
            "387 U.S. 294",
            "1967 U.S. LEXIS 2753"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Draper v. United States",
          "cluster_id": 105820,
          "cite": [
            "3 L. Ed. 2d 327",
            "79 S. Ct. 329",
            "358 U.S. 307",
            "1959 U.S. LEXIS 1607"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ker v. California",
          "cluster_id": 106641,
          "cite": [
            "10 L. Ed. 2d 726",
            "83 S. Ct. 1623",
            "374 U.S. 23",
            "1963 U.S. LEXIS 2473",
            "24 Ohio Op. 2d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elkins v. United States",
          "cluster_id": 106107,
          "cite": [
            "4 L. Ed. 2d 1669",
            "80 S. Ct. 1437",
            "364 U.S. 206",
            "1960 U.S. LEXIS 1989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Olmstead v. United States",
          "cluster_id": 101320,
          "cite": [
            "277 U.S. 438",
            "48 S. Ct. 564",
            "72 L. Ed. 944",
            "1928 U.S. LEXIS 694",
            "66 A.L.R. 376"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rabinowitz",
          "cluster_id": 104769,
          "cite": [
            "94 L. Ed. 2d 653",
            "70 S. Ct. 430",
            "339 U.S. 56",
            "1950 U.S. LEXIS 2298",
            "94 L. Ed. 653"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNabb v. United States",
          "cluster_id": 103791,
          "cite": [
            "318 U.S. 332",
            "63 S. Ct. 608",
            "87 L. Ed. 819",
            "1943 U.S. LEXIS 1280"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Preston v. United States",
          "cluster_id": 106771,
          "cite": [
            "11 L. Ed. 2d 777",
            "84 S. Ct. 881",
            "376 U.S. 364",
            "1964 U.S. LEXIS 1578"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(100711) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xODY4ODMyMDAwMDAmcz02MzU0MDk3JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&order_by=dateFiled+desc&page_size=100&q=cites%3A%28100711%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 194
      },
      "lane2_top_cited": {
        "query": "cites:(100711)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDIzJnM9MTA1MTg4JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28100711%29&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 25
      },
      "lane3_recency": {
        "query": "cites:(100711)",
        "reviewed": 3,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 3,
        "triage_read": 0,
        "triage_snippet_classified": 3
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(100711)",
    "indexed_citing_opinions": 1070,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 100711,
        "count": 1070,
        "count_source": "search"
      }
    ],
    "citation_count": 1597,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/agnello-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU0NzM2NDImcz00NDA4NDgxJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28100711%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 100711,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100711,
        "cited_id": 94272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100711,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100711,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100711,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100711,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100711,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100711,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100711,
        "cited_id": 3502705,
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
    "date_created": "2026-07-04T15:53:16Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T15:53:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T15:53:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T16:18:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T15:53:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Agnello v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion data-order="23" data-type="opinion" id="x999-1" type="majority">
<author id="b79-9">
  Mr. Justice Butler
 </author>
<p id="AG">
  delivered the opinion of the Court.
 </p>
<p id="b79-10">
  Thomas Agnello, Frank Agnello, Stephen Alba, Antonio Centorino and Thomas Pace were indicted in the District Court, Eastern District of New York, under § 37, Criminal Code, c. 321, <span class="citation no-link">35 Stat. 1088</span>, 1096, for a conspiracy to violate the Harrison Act, c. 1, <span class="citation no-link">38 Stat. 785</span>, as amended by
  <span citation-index="1" class="star-pagination" label="28"> 
   *28
   </span>
  • §§1006, 1007, 1008 of the Revenue Act of 1918, c. 18, <span class="citation no-link">40 Stat. 1057,1130</span>. The indictment charges that defendants conspired together to sell cocaine without having registered with the Collector of Internal Revenue and without having paid the prescribed tax. The overt acts charged are that defendants had cocaine in their possession, solicited'the sale of it, met in the home of defendant Alba at---.l-38 Union Street, Brooklyn, and made arrangéments ■ for the purpose of selling it, brought ,a large quantity of it to that place, and sold it in violation of the Act. The jury found defendants guilty. Each was sentenced to serve two years in the penitentiary and to pay a fine of $5,000. The Circuit Court of Appeals affirmed the judgment. <span class="citation" data-id="8831130"><a href="/opinion/8845856/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">290 Fed. 671</a></span>.
 </p>
<p id="b80-5">
  The evidence introduced by the Government was sufficient to warrant a finding of the following facts: Pasquale Napolitano and Nunzio Dispenza, employed by government revenue agents for that purpose, went to the home of Alba, Saturday, January 14, 1922, and there offered to buy. narcotics from Alba and Centorino. Alba gave them some samples. They arranged to come again on Monday following. They returned at the time agreed. Six revenue agents and a city policeman followed them and remained oh watch outside. Alba left the house and returned with Centorino. They did not then produce any drug. After discussion and the refusal of Napolitano' and Dispenza to go to Centorino’s house to get the drug, Centorino went to fetch it. He was followed by some of the agents. He first went to his own house, 172 Columbia Street; thence to 167 Columbia Street, — one part of which was a grocery store belonging to Pace and Thomas Agnello, and another part of which, connected with the grocery store, was the home of Frank Agnello and Pace. In a short time, Centorino, Pace and the Agnellos came out of the last mentioned place, and all went to Alba’s house. Looking through the windows, those on watch saw
  <span citation-index="1" class="star-pagination" label="29"> 
   *29
   </span>
  Frank Agnello produce a number of small packages for delivery to Napolitano and saw the latter hand over money to Alba. Upon the apparent consummation of the sale, the agents rushed in and arrested all the defendants. They found some of the packages on the table where the. transaction took place and found others in the pockets of Frank Agnello. All contained cocaine. On searching Alba, they found the money given him by Napolitano.
 </p>
<p id="b81-6">
  And as a part of its case in chief, the Government offered testimony tending to show .that, while some of the revenue agents were taking the defendants to the police station, the others and the city policeman went to the home of Centorino and searched it but did not find any narcotics; that they then went to 167 Columbia Street and searched it, and in Frank Agnello’s bedroom found a can of cocaine which was produced and offered in evidence. The evidence w,as excluded on the ground that the search and seizure were made without a search warrant. In defense, Centorino and others gave testimony to the effect that the packages of cocaine which were brought to arid seized in Alba’s house at the time of the arrests had been furnished to Centorino by Dispenza to induce an ap - parent sale of cocaine to Napolitano, that is, to incite crime or acts having the appearance of crime, for the purpose of entrapping and punishing defendants. Centorino testified that, after leaving Napolitano and Dispenza with Alba at the latter’s home, he went to his own house and got the packages of cocaine which had been given him by Dispenza and took them to 167 Columbia Street, and there gave them to Frank Agnello to be taken to Alba’s house. Frank Agnello testified on direct examination that he received the packages from Centorino but that he did not know their contents, and that he would not have carried them if he had known that they contained cocaine or narcotics. On cross examination, he said that he had never seen narcotics. Then, notwithstanding objection
  <span citation-index="1" class="star-pagination" label="30"> 
   *30
   </span>
  by defendants, the prosecuting attorney produced the can of cocaine which the Government claimed was seized in Agnello’s bedroom and asked him whether he had ever seen it. He said he had not, and specifically stated he had never seen it in his house. In rebuttal, over objec-. tions of defendants, the Government was permitted to put in the evidence of the search and seizure of the can of cocaine in Frank Agnello’s room, which theretofore had been offered and excluded.
 </p>
<p id="b82-4">
  The case involves the questions whether search of the house of Frank’ Agnello and seizure of the cocaine there found, without a search warrant, violated the Fourth Amendment, and whether the admission of evidence of such search and seizure violated the Fifth Amendment. The Fourth Amendment is: “The.right of the people to be secure in their persons, houses; papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.” The provision of the Fifth Amend-. ment invoked is this: “No person . . . shall be compelled in any criminal case to be a witness against himself:”
 </p>
<p id="b82-5">
  The right without a search warrant contemporaneously to search persons lawfully arrested while committing crime and to search the place where the arrest is made in order to find and seize things connected with the crime as. its fruits or as the means by which it was committed, as well as weapons and other things to effect an escape from custody, is not to be doubted. See
  <em>
   Carroll
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 158</a></span>;
  <em>
   Weeks
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span>. The legality of the arrests or of the searches and seizures made at the home of Alba is not questioned. Such searches and seizures naturally and usually appertain to and attend such arrests. But the right does not extend to other places. Frank Agnello’s
  <span citation-index="1" class="star-pagination" label="31"> 
   *31
   </span>
  house was several blocks distant from Alba’s house, where the arrest was made. When it was entered and searched, the conspiracy was ended and the defendants were under arrest and in custody elsewhere. That search cannot be sustained as an incident of the arrests. See
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#391" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 391</a></span>;
  <em>
   People
  </em>
  v.
  <em>
   Conway,
  </em>
  <span class="citation" data-id="3502705"><a href="/opinion/3532274/people-v-conway/" aria-description="Citation for case: People v. Conway">225 Mich. 152</a></span>;
  <em>
   Gamble
  </em>
  v.
  <em>
   Keyes,
  </em>
  35 S. D. 645, 650.
 </p>
<p id="b83-6">
  Under the Harrison Act (§ 8; § 1 as amended by § 1006) it is unlawful for any person who has not registered and paid a special tax, to have cocaine in his possession, and all unstamped packages of such drug found in his possession are subject to forfeiture. We assume, as contended by the Government, that defendants obtained from Frank Agnello’s house the cocaine that was taken to Alba’s house and there seized; that, the can of cocaine which later was found in Agnello’s house was unlawfully in his control and subject to seizure, and that it was a part of the cocaine which was the subject matter of the conspiracy.
 </p>
<p id="b83-7">
  The Government cites
  <em>
   Carroll
  </em>
  v.
  <em>
   United States, supra;
  </em>
  but it does not support the search and seizure complained of. That case involved the legality of a search of an automobile and the seizure of intoxicating liquors being transported therein in violation of the National Prohibition Act. The search and seizure were made by prohibition agents without a warrant. After referencé to various acts of Congress relating to the seizure of contraband goods, the court said (p. 153):
  <em>
   “
  </em>
  We have made a somewhat extended reference to these statutes to show that the guaranty of freedom from unreasonable searches and seizures by the Fourth Amendment has been construed, practically since the beginning of the Government, as recognizing a necessary difference between a search of a store, dwelling house or other structure in respect of which a proper official warrant readily may be obtained, and a
  <span citation-index="1" class="star-pagination" label="32"> 
   *32
   </span>
  search of a ship, motor boat, wagon or automobile, for contraband goods, where it is not practicable to secure a warrant because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought.” It was held that,
  <em>
   “
  </em>
  The facts and circumstances within their knowledge and of which they had reasonably trustworthy information were sufficient in themselves to warrant a man of reasonable caution in the belief that intoxicating liquor was being' transported in the automobile which they stopped and searched.” (p. 162.) And on that ground the court held the search and seizure without warrant justified.
 </p>
<p id="b84-6">
  While the question has never been directly decided by this court, it has always been assumed that one’s house cannot lawfully be searched without a search warrant, except as an incident to a lawful arrest therein:
  <em>
   Boyd
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 624</a></span>,
  <em>
   et seq.,
  </em>
  630;
  <em>
   Weeks
  </em>
  v.
  <em>
   United States, supra,
  </em>
  393;
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States, supra,
  </em>
  391;
  <em>
   Gouled
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#308" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 308</a></span>. The protection of the Fourth Amendment extends to all equally, — to those justly suspected or accused, as well as to the innocent. The search of a private dwelling without a warrant is in itself unreasonable and abhorrent to our laws. Congress has never passed an act purporting to authorize the search of a house without a warrant. On the other hand, special limitations have been set about the obtaining of search warrants for that purpose. Thus, the National Prohibition Act, approved October 28, 1919, c. 85, Tit. II, § 25, <span class="citation no-link">41 Stat. 305</span>, 315-, provides that no search warrant shall issue to search any private dwelling occupied as such unless it is being used for the unlawful sale of intoxicating liquor or is in part used for business purposes, such as store, shop, saloon, restaurant, hotel or boarding house. And later, to the end that government employees without a warrant shall not invade the homes of the people and violate the priva
  <span citation-index="1" class="star-pagination" label="33"> 
   *33
   </span>
  cies of life, Congress made it a criminal offense, punishable by heavy penalties, for any officer, agent or employee of the United States engaged in the enforcement of any law to search a private dwelling house without a warrant directing such search. Act of November 23, 1921, c. 134, § 6, <span class="citation no-link">42 Stat. 222</span>, 223. Safeguards similar to the Fourth Amendment are deemed necessary and have been provided in the. constitution or laws of every State of the Union.
  <a class="footnote" href="#fn*" id="fn*_ref">
   *
  </a>
  We think there is no state statute authorizing the search of a house without a warrant; and, in a number of state laws recently enacted for the enforcement of prohibition in respect of intoxicating liquors, there are provisions similar to- those in § 25 of the National Prohibition Act. Save in certain cases as incident to arrest, there is no sanction in the decisions of the courts, federal or state, for the search of a private dwelling house without a warrant. Absence of any judicial approval is persuasive authority that it is unlawful. See
  <em>
   Entick
  </em>
  v.
  <em>
   Carrington,
  </em>
  19 Howard’s State Trials, 1030, 1066. Belief, however well founded, that an article sought is concealed in a dwelling house furnishes no justification for a search of that place without a warrant. And such searches are held unlawful notwithstanding facts unquestionably showing probable cause. See
  <em>
   Temperani
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9335965"><a href="/opinion/9340620/temperani-v-united-states/" aria-description="Citation for case: Temperani v. United States">299 Fed. 365</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Rembert,
  </em>
  <span class="citation" data-id="8827993"><a href="/opinion/8842783/united-states-v-rembert/#1000" aria-description="Citation for case: United States v. Rembert">284 Fed. 996, 1000</a></span>;
  <em>
   Connelly
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8822127"><a href="/opinion/8837062/connelly-v-united-states/" aria-description="Citation for case: Connelly v. United States">275 Fed. 509</a></span>;
  <em>
   McClurg
  </em>
  v.
  <em>
   Brenton,
  </em>
  <span class="citation" data-id="7110885"><a href="/opinion/7199636/mcclurg-v-brenton/#372" aria-description="Citation for case: McClurg v. Brenton">123 Ia. 368, 372</a></span>;
  <em>
   People
  </em>
  v.
  <em>
   Margolis,
  </em>
  <span class="citation" data-id="7951962"><a href="/opinion/7998119/people-v-margolis/" aria-description="Citation for case: People v. Margolis">220 Mich. 431</a></span>;
  <em>
   Childers
  </em>
  v.
  <em>
   Commonwealth,
  </em>
  <span class="citation" data-id="7148020"><a href="/opinion/7235601/childers-v-commonwealth/" aria-description="Citation for case: Childers v. Commonwealth">198 Ky. 848</a></span>;
  <em>
   State
  </em>
  v.
  <em>
   Warfield,
  </em>
  <span class="citation" data-id="8194400"><a href="/opinion/8230088/state-v-warfield/" aria-description="Citation for case: State v. Warfield">184 Wis. 56</a></span>. The search of Frank Agnello’s house and seizure of the can of cocaine violated the Fourth Amendment.
 </p>
<p id="b85-6">
  It' is well settled that, when properly invoked, the Fifth Amendment protects every person from incrimination by
  <span citation-index="1" class="star-pagination" label="34"> 
   *34
   </span>
  the use of evidence obtained through search or seizure made in violation of his rights under the Fourth Amendment.
  <em>
   Boyd v. United States, supra,
  </em>
  630,
  <em>
   et seq.; Weeks
  </em>
  v.
  <em>
   United States, supra,
  </em>
  398;
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States, supra,
  </em>
  391, 392;
  <em>
   Gouled
  </em>
  v.
  <em>
   United States, supra,
  </em>
  306;
  <em>
   Amos
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/#316" aria-description="Citation for case: Amos v. United States">255 U. S. 313, 316</a></span>. The Government contends that, even if the search and seizure were unlawful, the evidence was admissible because no application on behálf of defendant was made to the court for the return of the can of cocaine. The reason for such application, where required, is that the court will not pause in ,a criminal case to determine collateral issues as to how the evidence was obtained. See
  <em>
   Adams v. New York,
  </em>
  <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/#594" aria-description="Citation for case: Adams v. New York">192 U. S. 585, 594</a></span>, affirming <span class="citation multiple-matches"><a href="/c/N.%20Y./176/351/">176 N. Y. 351</a></span>. But in this case, the facts disclosing that the search and- seizure violated the Fourth Amendment were not in controversy.. They were shown by the examination of the witness called to give the evidence. There was no search warrant; and from the first, the position of the Government has been that none was necessary. In substance, Frank Agnello testified that he never had possession of the can of cocaine and never saw it until it was produced in court. Thére is nothing to show that, in advance of its offer in evidence, he knew that the Government claimed it had searched his house and found cocaine there, or that the prosecutor intended to introduce evidence of any search or seizure. It would be unreasonable to hold that he was bound to apply for the return of an article which he maintained he never had. Where, by uncontroverted facts, it appears that a search ,and seizure were made in violation of the Fourth Amendment, there is no reason why one whose rights have been so violated and who is sought to be incriminated by evidence so obtained, may not invoke protection of the Fifth Amendment immediately and without any application for the return of the thing seized. “A rule of practice must not be allowed for any technical reason to prevail over
  <span citation-index="1" class="star-pagination" label="35"> 
   *35
   </span>
  a constitutional right.”
  <em>
   Gouled
  </em>
  v.
  <em>
   United States, supra,
  </em>
  313. And the contention that the evidence of the search and seizure was admissible in rebuttal is without merit. In his direct examination, Agnello was not asked and did not testify concerning the can of cocaine. In cross-examination, in answer to; a question permitted over his objection, he said he had never seen it. He did nothing to waive his constitutional protection or to justify cross-examination in respect of the evidence claimed to have been obtained by the search. As said in
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States, supra,
  </em>
  392, “ The essence of a provision forbidding the acquisition of evidence in a certain way is that not merely evidence so acquired shall not be used before the Court but that it shall not be. used at all.” The admission of evidence obtained by the search and seizure was error and prejudicial to the substantial rights of Frank Agnello. The judgment against him must be set aside and a new trial awarded.
 </p>
<p id="b87-6">
  But the judgment against the other defendants may stand. The introduction of the evidence of the search and seizure did not transgress their constitutional rights. And it was not prejudicial error against them. The possession by Frank Agnello of the can of cocaine which was seized tended to show guilty knowledge and criminal intent on his part; but it was not submitted as attributable to the other defendants. During the summing up of the case to the jury by the prosecuting attorney, the court distinctly ^ indicated that the evidence was admissible only against Frank Agnello. The other defendants did not request any instruction to the jury in reference to the matter, and they do not contend that any erroneous instruction was given.
  <em>
   Isaacs
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="94272"><a href="/opinion/94272/isaacs-v-united-states/#491" aria-description="Citation for case: Isaacs v. United States">159 U. S. 487, 491</a></span>.
 </p>
<p id="b87-7">
  The packages of-cocaine seized at-Alba’s house were carried to'that place by Frank Agnello. He did this at the instance of Centorino; and in his behalf it is claimed he acted innocently and without knowledge of the con
  <span citation-index="1" class="star-pagination" label="36"> 
   *36
   </span>
  tents of the package. The evidence of the search and seizure made in his house tended to show that he knew what he was doing and was a willing participant in the conspiracy charged. But so far as concerns the other defendants, it is immaterial whether he acted innocently and without knowledge of the contents of the package or knowingly to effect the object of the conspiracy. In either case, his act would be equally chargeable to his codefendants. They are not entitled to a new trial. See
  <em>
   Rossi
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8824066"><a href="/opinion/8838959/rossi-v-united-states/#354" aria-description="Citation for case: Rossi v. United States">278 Fed. 349, 354</a></span>;
  <em>
   Belfi
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8812898"><a href="/opinion/8828045/belfi-v-united-states/#828" aria-description="Citation for case: Belfi v. United States">259 Fed. 822, 828</a></span>;
  <em>
   Feder et al.
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8811695"><a href="/opinion/8826870/feder-v-united-states/" aria-description="Citation for case: Feder v. United States">257 Fed. 694</a></span>;
  <em>
   Browne
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8760616"><a href="/opinion/8776964/browne-v-united-states/#13" aria-description="Citation for case: Browne v. United States">145 Fed. 1, 13</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Cohn,
  </em>
  <span class="citation" data-id="8753798"><a href="/opinion/8770268/united-states-v-cohn/#626" aria-description="Citation for case: United States v. Cohn">128 Fed. 615, 626</a></span>.
 </p>
<judges id="b88-5">
<em>
   Judgment against Frank Agnello reversed; judgment against other defendants affirmed.
  </em>
</judges>

<div class="footnotes"><div class="footnote" id="fn*" label="*">
<a class="footnote" href="#fn*_ref">
   *
  </a>
<p id="b85-7">
   See p. 1268, Index Digest of State Constitutions (prepared for New York State Constitutional Convention Commission, 1915); also § 8, c. 7, Consolidated Laws, New York, as amended by L. 1923, c. 80.
  </p>
</div></div></opinion>
```

---
