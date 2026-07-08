#!/usr/bin/env python3
"""
S7 worklist builder — regenerates the S7 change-list against the post-S3/S5/S6
tree (spec §5 step 1). Consumes _run/o2-execute/s7-survey.json (the survey this
run rebuilt) and the SIGNED tier + fix roster transcribed from
_overhaul2/S7-CHANGELIST.md (2026-07-03). Emits:

  * _run/o2-execute/s7-worklist.json   (machine ledger)
  * _run/o2-execute/S7-WORKLIST.md     (rendered)

Discipline: tiers are USER-OWNED (spec R2) and carried UNCHANGED — this builder
never edits one. Paths are resolved PROGRAMMATICALLY (basename lookup against the
survey page set, with explicit overrides for the three parent pages that
dissolved into sub-umbrella index landings). A row whose page cannot be located
is flagged `unresolved` (never guessed). Read-only; writes only under
_run/o2-execute/.

Usage: python3 scripts/s7/build_worklist.py [--stdout]
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
SURVEY_REL = os.path.join("_run", "o2-execute", "s7-survey.json")
OUT_JSON_REL = os.path.join("_run", "o2-execute", "s7-worklist.json")
OUT_MD_REL = os.path.join("_run", "o2-execute", "S7-WORKLIST.md")

# --------------------------------------------------------------------------
# Table 1 — the 48 existing pages: (n, old path under content/, S3 target short,
# SIGNED tier, fix-tag summary, split/move note). Current path resolved below.
# Tiers + fix tags transcribed verbatim-in-substance from S7-CHANGELIST Table 1.
# --------------------------------------------------------------------------
T1 = [
    (1, "1-foundations-history/Common Law Origins.md", "1 Foundations → Common Law Origins", "C",
     "Riley→Related; TEACH-04g(:38); TEACH-04d(2); TEACH-12a; TEACH-12b", ""),
    (2, "3-what-is-a-search/Fourth Amendment Framework.md", "1 Foundations → FA Framework (re-homed)", "B (hub)",
     "TEACH-01(worst,:76-79); TEACH-02c(CL-confirm); TEACH-04d(6); TEACH-08; TEACH-12a; TEACH-12b(hub)", ""),
    (3, "3-what-is-a-search/Fourth Amendment Analysis Checklist.md", "1 Foundations → Analysis Checklist (re-homed)", "C",
     "TEACH-12a; TEACH-12b", ""),
    (4, "3-what-is-a-search/Fourth Amendment Recalibration.md", "1 Foundations → FA Recalibration (re-homed)", "C",
     "TEACH-12a; TEACH-12b; TEACH-04d(9)", ""),
    (5, "5-levels-of-suspicion/Probable Cause and Reasonable Suspicion.md", "2 Standards of Proof (splits RS+PC; +Proof Ladder)", "A",
     "TEACH-04a(:66); TEACH-04f(:66); TEACH-02c(:73); TEACH-04e(1); already-LCD-standard", "split → RS + PC siblings (T2#1 Proof Ladder)"),
    (6, "3-what-is-a-search/Two Definitions of Search.md", "3 Searches → Two Definitions (splits Trespass+REP)", "A",
     "TEACH-01(:73/:75/:78/:79); TEACH-02c(CL-confirm :48/:126); TEACH-03(3); TEACH-05; TEACH-08", "SPLIT: parent dissolved into sub-umbrella index landing + Trespass/REP children"),
    (7, "3-what-is-a-search/Curtilage.md", "3 Searches → Curtilage (splits Open Fields)", "A",
     "Dunn-in-Rule; TEACH-02c(:82/:83); TEACH-12a; TEACH-03(1); TEACH-08; D7-SACO-section+node", "splits → Open Fields (T2#4)"),
    (8, "3-what-is-a-search/The Third-Party Doctrine and Digital Surveillance.md", "3 Searches → Third-Party sub-umbrella (A6)", "A",
     "GAP-03b; GAP-03c; woven-in(:25); TEACH-03(1); TEACH-04e; TEACH-08", "SUB-UMBRELLA: parent → index landing + CSS/Reverse-Keyword/Real-Time/IGG children + Title III sibling"),
    (9, "3-what-is-a-search/Abandonment.md", "3 Searches → Abandonment", "B",
     "TEACH-04e(3); TEACH-08", ""),
    (10, "3-what-is-a-search/Tents.md", "3 Searches → Tents & Temporary Dwellings (retitle)", "C",
     "TEACH-02c(1); TEACH-04e; TEACH-08", ""),
    (11, "7-exceptions-warrant/7a-pc-needed/Plain View Doctrine.md", "3 Searches → Plain View & Plain Feel (re-homed)", "A",
     "TEACH-02c(No-standalone×4+CL-confirm×2); TEACH-03(5); TEACH-08; Plain-Feel-note(T2#12)", ""),
    (12, "4-what-is-a-seizure/Seizure of the Person.md", "4 Seizures → When a Seizure Occurs (retitle)", "A",
     "TEACH-04b(:48); TEACH-04e-donor(:54); TEACH-08", ""),
    (13, "4-what-is-a-seizure/Terry Stops and Reasonable Suspicion.md", "4 Seizures → Terry Stops & RS", "A",
     "TEACH-12a; TEACH-04e(2); TEACH-05; TEACH-08", ""),
    (14, "4-what-is-a-seizure/Traffic Stops.md", "4 Seizures → Traffic Stops (Brendlin in)", "A",
     "TEACH-08", ""),
    (15, "4-what-is-a-seizure/Arrest in the Home.md", "4 Seizures → Arrests → Arrest in the Home", "A",
     "TEACH-12a; TEACH-03(1); TEACH-08", "feeds Entry to Arrest (T2#30)"),
    (16, "4-what-is-a-seizure/Collective Knowledge and the Fellow-Officer Rule.md", "4 Seizures → Collective Knowledge", "A",
     "Herring→Key(+Whiteley); horizontal-pooling-split; Pringle-keep; TEACH-08", ""),
    (17, "6-warrant-requirement/The Warrant Requirement.md", "5 The Warrant (splits getting/executing)", "A",
     "TEACH-01(:109/:111/:114); TEACH-04h(:149); TEACH-02c; GAP-06(:62); TEACH-03(1); TEACH-08", "SPLIT → Getting a Warrant + Executing a Warrant children (T2#17-23)"),
    (18, "7-exceptions-warrant/7b-pc-not-needed/Search Incident to Arrest.md", "6 Warrant Exceptions (splits SIA family)", "A",
     "TEACH-05; TEACH-08; Inventory-teaching-text-extracted", "SPLIT → SIA Persons/Cell/Alcohol/Vehicles (T2#24-27)"),
    (19, "7-exceptions-warrant/7a-pc-needed/Automobile Exception.md", "6 → Searching a Vehicle → Automobile (re-parent)", "A",
     "TEACH-12a; TEACH-02c(:85); TEACH-03(1); TEACH-04e(2); TEACH-08", ""),
    (20, "7-exceptions-warrant/7b-pc-not-needed/Special Needs and Administrative Searches.md", "6 → Programmatic & Special-Needs (splits Inventory+Checkpoints)", "B",
     "TEACH-02c(:114/:115); TEACH-08", "splits → Inventory (T2#28) + Checkpoints (T2#29)"),
    (21, "7-exceptions-warrant/7b-pc-not-needed/Border Searches.md", "6 → Programmatic & Special-Needs → Border (re-parent)", "B",
     "TEACH-02c(No-standalone×6); TEACH-03(4); TEACH-05; TEACH-08", ""),
    (22, "7-exceptions-warrant/7b-pc-not-needed/Consent Searches.md", "6 → Consent", "A",
     "Matlock; consent-3-prongs+scope; TEACH-02c(:84/:85); TEACH-12a; TEACH-08", ""),
    (23, "7-exceptions-warrant/7b-pc-not-needed/Knock and Talk.md", "6 → Knock and Talk", "A",
     "PATTERN PAGE — implied-license DONE(e0935ce/4b48a4a); TEACH-03(11); TEACH-12a; TEACH-08", "PATTERN PAGE (normative template)"),
    (24, "7-exceptions-warrant/7a-pc-needed/Exigent Circumstances and Hot Pursuit.md", "6 → Home Entry (splits Hot-Pursuit + Destruction)", "A",
     "Bandiero; Santana-limited-by-Lange; TEACH-02c(:73); TEACH-12a; TEACH-03(7); TEACH-04e; TEACH-08", "splits → Hot Pursuit (retained parent, T2#31) + Destruction of Evidence (T2#32)"),
    (25, "7-exceptions-warrant/7a-pc-needed/Emergency Aid.md", "6 → Home Entry → Emergency Aid", "A",
     "TEACH-03(8); TEACH-02c(1); TEACH-08; Brigham-City-entry-standard; D5-cross-link", ""),
    (26, "7-exceptions-warrant/7a-pc-needed/Community Caretaking.md", "6 → Home Entry → Community Caretaking", "A",
     "caretaking-reaches-persons REFUTED→D5-reshape; TEACH-03(5); TEACH-08; D5-section+node", ""),
    (27, "7-exceptions-warrant/7b-pc-not-needed/Securing the Scene.md", "6 → Home Entry → Protective Sweeps & Securing", "B",
     "TEACH-03(3); TEACH-08; Buie-sweep-prose(T2#33)", ""),
    (28, "8-exclusionary-rule-remedies/The Exclusionary Rule.md", "7 ER → The Exclusionary Rule (splits A4)", "A",
     "TEACH-01(:122/:124/:129); TEACH-02c(CL-confirm+No-standalone :130); TEACH-05(worst); TEACH-08", "SPLIT: parent → sub-umbrella index landing + Fruits/Good-Faith/Inevitable children (T2#36-38)"),
    (29, "8-exclusionary-rule-remedies/Standing to Challenge a Search.md", "7 ER → Standing (Brendlin+Katz out)", "A",
     "TEACH-01(:74/:76/:80); TEACH-02c(:80/:118); TEACH-03(4); TEACH-08", ""),
    (30, "9-confessions-interrogation/Due-Process Voluntariness of Confessions.md", "8 Confessions → Due-Process Voluntariness", "B",
     "TEACH-08", ""),
    (31, "9-confessions-interrogation/Miranda and Custodial Interrogation.md", "8 Confessions → Miranda & Custodial Interrogation", "A",
     "TEACH-04c two-Cs(:23 cut-not-register); TEACH-08", ""),
    (32, "9-confessions-interrogation/Miranda Waiver and Invocation.md", "8 Confessions → Miranda Waiver & Invocation", "A",
     "TEACH-04e; TEACH-08", ""),
    (33, "9-confessions-interrogation/Public-Employee Compelled Statements (Garrity).md", "8 Confessions → Garrity", "B",
     "TEACH-04e; TEACH-08", ""),
    (34, "9-confessions-interrogation/Sixth Amendment Right to Counsel.md", "9 Right to Counsel → Sixth Amendment RtC (de-rip)", "A",
     "TEACH-02c(1); TEACH-05; TEACH-08; +Lineups(T2#39)", ""),
    (35, "9-confessions-interrogation/Eyewitness Identification.md", "10 Fair-Trial → Eyewitness ID (re-homed)", "B",
     "TEACH-03(2); TEACH-08", ""),
    (36, "10-use-of-force-liability/Brady and Giglio.md", "10 Fair-Trial → Brady & Giglio (re-homed)", "B",
     "TEACH-03(2); TEACH-04e; TEACH-05; TEACH-08", ""),
    (37, "11-adjacent-doctrines/Entrapment.md", "10 Fair-Trial → Entrapment (re-homed; cat dissolves)", "B",
     "TEACH-02c(:64/:65); TEACH-08", ""),
    (38, "10-use-of-force-liability/Use of Force.md", "11 Use of Force & Liability → Use of Force (Graham in)", "A",
     "TEACH-03(5); TEACH-08; BWC-prose", ""),
    (39, "10-use-of-force-liability/Section 1983 Liability and Qualified Immunity.md", "11 → §1983 (splits QI)", "A",
     "LAW-05(:188 Zorn-legend); TEACH-03(9); TEACH-04e(2); TEACH-05; TEACH-08", "splits → Qualified Immunity (T2#40); Bivens/§242 deferred-R6"),
    (40, "2-legal-system-research/The Federal Court System.md", "12 Reference → Federal Court System", "C",
     "TEACH-12a; TEACH-04d(1)", ""),
    (41, "2-legal-system-research/Reading and Citing Cases.md", "12 Reference → Reading & Citing Cases", "C",
     "add-State-Citations/opencase; TEACH-12a", "feeds State Citations (T2#44)"),
    (42, "2-legal-system-research/Legal Research Tools.md", "12 Reference → Legal Research Tools (split)", "C",
     "split-Legal-Research + State-Citations/opencase; TEACH-12a", "feeds State Citations (T2#44)"),
    (43, "2-legal-system-research/Verifying Good Law.md", "12 Reference → Verifying Good Law", "C",
     "TEACH-12a; TEACH-05", ""),
    (44, "2-legal-system-research/Common Legal Terms.md", "12 Reference → Common Legal Terms", "no-op",
     "S8-owned glossary — S7 no-op", ""),
    (45, "2-legal-system-research/Case Index.md", "12 Reference → Case Index", "no-op",
     "generated (S3 regen; S8 routes) — S7 no-op", ""),
    (46, "12-instructor-craft-study/Three Golden Rules.md", "13 Instructor Craft → Three Golden Rules", "C",
     "TEACH-12a; TEACH-12b; TEACH-04d(3)", ""),
    (47, "3-what-is-a-search/CREW.md", "13 Instructor Craft → C.R.E.W. (re-homed)", "C",
     "CREW R→RE; TEACH-12a; TEACH-12b; TEACH-02c(1)", ""),
    (48, "12-instructor-craft-study/Instructor Development.md", "13 Instructor Craft → Instructor Development", "C",
     "TEACH-12a; TEACH-04e(1)", ""),
]

# Explicit current-path overrides for the parents that dissolved into
# sub-umbrella index LANDINGS (basename 'index.md' cannot be basename-resolved).
T1_SPLIT_LANDINGS = {
    6: "content/searches/two-definitions-of-search/index.md",
    8: "content/searches/the-third-party-doctrine-and-digital-surveillance/index.md",
    28: "content/the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/index.md",
}

# --------------------------------------------------------------------------
# Table 2 — the 45 new-node rows: (n, node name, expected current basename OR
# special, SIGNED tier, source note). Resolved to current path below.
# --------------------------------------------------------------------------
T2 = [
    (1, "2 Standards of Proof → The Proof Ladder [new]", "The Proof Ladder.md", "C", "PC/RS Brief proof-continuum"),
    (2, "3 Searches → Two Definitions → Trespass", "Trespass.md", "A", "Two Definitions (trespass/Jones)"),
    (3, "3 Searches → Two Definitions → Reasonable Expectation of Privacy", "Reasonable Expectation of Privacy.md", "A", "Two Definitions (Katz; Katz re-homed from Standing)"),
    (4, "3 Searches → Open Fields", "Open Fields.md", "B", "Curtilage (open-fields)"),
    (5, "3 Searches → Aerial & Enhanced Surveillance [new]", "Aerial and Enhanced Surveillance.md", "B", "new prose (R7)"),
    (6, "3 → Digital → Cell-Site Simulators [new]", "Cell-Site Simulators.md", "B (D6)", "new (A6)"),
    (7, "3 → Digital → Reverse-Keyword & Geofence Warrants [new]", "Reverse-Keyword and Geofence Warrants.md", "B (D6)", "geofence RD bullets (T1#2/6/17/28/29)"),
    (8, "3 → Digital → Real-Time Tracking [new]", "Real-Time Tracking.md", "C (D6)", "new (A6)"),
    (9, "3 → Digital → Investigative Genetic Genealogy [new]", "Investigative Genetic Genealogy.md", "C (D6)", "new (A6)"),
    (10, "3 → Electronic Surveillance & Title III [new]", "Electronic Surveillance and Title III.md", "C (+GAP-03c)", "new (A6); §702 per GAP-03c"),
    (11, "3 → Private & Foreign Searches [new]", "Private and Foreign Searches.md", "B", "private-search bullets in FA Framework RD :83-84"),
    (12, "3 → Plain Feel note (in-page on Plain View)", "__INPAGE:Plain View Doctrine.md:Dickerson", "in-page", "Plain View Doctrine.md"),
    (13, "4 Seizures → Seizure of Property [new]", "Seizure of Property.md", "B", "new"),
    (14, "4 Seizures → Stop-and-Identify [new]", "Stop-and-Identify.md", "C", "new (R7 Hiibel)"),
    (15, "4 → Arrests → Arrest & Arrest Warrants", "Arrest and Arrest Warrants.md", "B", "no existing source page"),
    (16, "4 → Arrests → Prompt Probable-Cause Determination [new]", "Prompt Probable-Cause Determination.md", "C", "new (R7 Gerstein-McLaughlin)"),
    (17, "5 → Getting a Warrant → Probable Cause in the Affidavit", "Probable Cause in the Affidavit.md", "A", "Warrant Requirement (split)"),
    (18, "5 → Getting a Warrant → The Neutral & Detached Magistrate", "The Neutral and Detached Magistrate.md", "B", "Warrant Requirement (Johnson/Lo-Ji :149)"),
    (19, "5 → Getting a Warrant → Particularity", "Particularity.md", "A", "Warrant Requirement (digital note :62)"),
    (20, "5 → Getting a Warrant → Franks Challenges [new]", "Franks Challenges.md", "B", "new (R7)"),
    (21, "5 → Executing a Warrant → Knock-and-Announce", "Knock-and-Announce.md", "A", "Warrant Requirement (:42 block)"),
    (22, "5 → Executing a Warrant → Detention & Search of Persons at the Scene [new]", "Detention and Search of Persons at the Scene.md", "B", "new (R7 Summers/Bailey/Ybarra)"),
    (23, "5 → Executing a Warrant → Scope, Manner & Related Issues", "Scope Manner and Related Issues.md", "B", "Warrant Requirement (split remainder)"),
    (24, "6 → Searching a Person → SIA — Persons", "SIA Persons.md", "A", "SIA (split)"),
    (25, "6 → Searching a Person → SIA — Cell Phones", "SIA Cell Phones.md", "A", "SIA (split)"),
    (26, "6 → Searching a Person → SIA — Alcohol Tests", "SIA Alcohol Tests.md", "B", "SIA (split)"),
    (27, "6 → Searching a Vehicle → SIA — Vehicles", "SIA Vehicles.md", "A", "SIA (split; Belton→Gant)"),
    (28, "6 → Searching a Vehicle → Inventory Searches", "Inventory Searches.md", "B", "Special Needs + SIA (A7(2))"),
    (29, "6 → Searching a Vehicle → Checkpoints & Roadblocks", "Checkpoints and Roadblocks.md", "B", "Special Needs (mega-page)"),
    (30, "6 → Home Entry → Entry to Arrest", "Entry to Arrest.md", "A", "Arrest in the Home (Payton/Steagald; D7 SACO)"),
    (31, "6 → Home Entry → Exigent — Hot Pursuit", "__PARENT:Exigent Circumstances and Hot Pursuit.md", "A", "Exigent (retained parent = Hot Pursuit; T1#24)"),
    (32, "6 → Home Entry → Exigent — Destruction of Evidence", "Destruction of Evidence.md", "A", "Exigent (split)"),
    (33, "6 → Home Entry → Protective Sweeps & Securing the Scene", "__PARENT:Securing the Scene.md", "B", "Securing the Scene (retained parent; Buie prose = new unit; T1#27)"),
    (34, "6 → Home Entry → Fire-Scene Entries [new]", "Fire-Scene Entries.md", "C", "new (R7)"),
    (35, "6 → Searching Effects & Containers", "Searching Effects and Containers.md", "B", "Automobile + SIA container strands"),
    (36, "7 ER → Fruits & Attenuation [new-split]", "Fruits and Attenuation.md", "A", "ER (A4)"),
    (37, "7 ER → The Good-Faith Exception [new-split]", "The Good-Faith Exception.md", "A", "ER (A4)"),
    (38, "7 ER → Inevitable Discovery & Independent Source [new-split]", "Inevitable Discovery and Independent Source.md", "B", "ER (A4)"),
    (39, "9 → Lineups & the Right to Counsel [new]", "Lineups and the Right to Counsel.md", "B", "new"),
    (40, "11 → Qualified Immunity [new-split]", "Qualified Immunity.md", "A", "§1983 (R7); Zorn LAW-05 legend case"),
    (41, "11 → Retaliatory Arrest [new]", "Retaliatory Arrest.md", "C", "new (A5; Nieves/Gonzalez)"),
    (42, "11 → Malicious Prosecution under the 4A [new]", "Malicious Prosecution under the Fourth Amendment.md", "C", "new (A5; Thompson/Chiaverini)"),
    (43, "11 → Civil Asset Forfeiture [new]", "Civil Asset Forfeiture.md", "C", "new (A5; Culley)"),
    (44, "12 → State Citations & Conventions [new]", "State Citations and Conventions.md", "C", "Reading&Citing + Legal Research split; opencase.com"),
    (45, "6 → Automobile Exception — CROSS-REF (not new prose)", "__CROSSREF:Automobile Exception.md", "— (cross-ref)", "existing page re-parented (T1#19)"),
]

# --------------------------------------------------------------------------
# Table 3 — snapshot corpus-pass sizes (2026-07-03) for the delta columns.
# --------------------------------------------------------------------------
T3_SNAPSHOT = {
    "TEACH-03 slip-op (doctrine pages)": "76 hits / 20 doctrine pages (+43/47 case pages)",
    "TEACH-05 em-dash": "3,943 em-dashes / 153,274 words / 48 pages (25.7/1k)",
    "TEACH-02c pipeline-vocab leak lines": "41 leak lines / 19 pages (class1=23, class2=10, class3=5, class4=1)",
    "TEACH-04d inverted labels": "21 sites / 5 pages",
    "TEACH-04e field-framing": "19 hits / 13 pages (broad officer-framing heuristic)",
    "TEACH-08 RD-family heading": "35 pages (34 'Recent developments' + 1 '& subsequent treatment')",
    "TEACH-12a missing H1": "18 pages",
    "TEACH-12b legacy Rule skeleton": "6 pages",
}


def load_survey():
    with open(os.path.join(REPO_ROOT, SURVEY_REL), encoding="utf-8") as f:
        return json.load(f)


def build_indexes(survey):
    by_path = {r["path"]: r for r in survey["pages"]}
    by_base = {}
    for r in survey["pages"]:
        by_base.setdefault(os.path.basename(r["path"]), []).append(r["path"])
    return by_path, by_base


def resolve_t1_current(n, old_rel, by_base):
    if n in T1_SPLIT_LANDINGS:
        return T1_SPLIT_LANDINGS[n], "split-into-sub-umbrella-index-landing"
    base = os.path.basename(old_rel)
    hits = by_base.get(base, [])
    if len(hits) == 1:
        return hits[0], "basename-match"
    if len(hits) > 1:
        return None, "AMBIGUOUS:%s" % ";".join(hits)
    return None, "unresolved"


def flags_str(row):
    if row is None:
        return "(no survey row)"
    lk = row["leak_lines"]
    return ("H1%s · Rule-skel%s · slip %d · %s%s · ff %d · lk %d(c1=%d,c2=%d,c3=%d,c4=%d) "
            "· inv %d · em %d (%.1f/1k) · %s") % (
        "✓" if row["h1_present"] else "✗",
        "!" if row["rule_skeleton"] else "-",
        row["slip_ops"],
        "RD" if row["rd_heading"] else "no-RD",
        "/LCD" if row["lcd_heading"] else "",
        row["field_framing"], lk["total"],
        lk["class1_no_standalone"], lk["class2_cl_confirm"],
        lk["class3_meta_intro"], lk["class4_woven_in"],
        row["inverted_labels"], row["em_dashes"], row["emdash_per_1k"],
        (row["diagnostics"]["status"] or "no-status"))


def build_t1(by_path, by_base):
    out = []
    for (n, old_rel, s3, tier, fixes, note) in T1:
        cur, how = resolve_t1_current(n, old_rel, by_base)
        row = by_path.get(cur) if cur else None
        out.append({
            "n": n, "old_path": "content/" + old_rel, "s3_target": s3,
            "tier_signed": tier, "current_path": cur, "resolution": how,
            "resolved": cur is not None, "split_note": note,
            "fix_tags": fixes, "current_flags": row,
        })
    return out


def classify_t2_state(row):
    """authored | stub | (absent handled by caller)."""
    if row is None:
        return "absent"
    w = row["words"]
    if w < 120:
        return "placed-stub"
    return "authored"


def build_t2(by_path, by_base):
    out = []
    for (n, node, spec, tier, src) in T2:
        cur = None
        kind = None
        note = ""
        if spec.startswith("__INPAGE:"):
            _, page, marker = spec.split(":", 2)
            hits = by_base.get(page, [])
            cur = hits[0] if len(hits) == 1 else None
            kind = "in-page"
            note = "hosted in-page on %s (marker: %s)" % (page, marker)
        elif spec.startswith("__PARENT:"):
            page = spec.split(":", 1)[1]
            hits = by_base.get(page, [])
            cur = hits[0] if len(hits) == 1 else None
            kind = "retained-parent"
            note = "materialized as retained parent page (see T1)"
        elif spec.startswith("__CROSSREF:"):
            page = spec.split(":", 1)[1]
            hits = by_base.get(page, [])
            cur = hits[0] if len(hits) == 1 else None
            kind = "cross-ref"
            note = "existing page, not new prose (T1#19)"
        else:
            hits = by_base.get(spec, [])
            cur = hits[0] if len(hits) == 1 else None
            row = by_path.get(cur) if cur else None
            kind = classify_t2_state(row)
        row = by_path.get(cur) if cur else None
        out.append({
            "n": n, "node": node, "expected_basename": spec, "tier_signed": tier,
            "source": src, "current_path": cur, "exists": cur is not None,
            "state": kind, "note": note,
            "words": (row["words"] if row else None),
            "status": (row["diagnostics"]["status"] if row else None),
        })
    return out


def build_t3(survey):
    t = survey["totals"]
    cp = survey["case_pages"]
    rows = []

    def add(pas, snap, cur, note):
        rows.append({"pass": pas, "snapshot": snap, "current": cur, "note": note})

    add("TEACH-03 slip-op (substantive doctrine pages)",
        T3_SNAPSHOT["TEACH-03 slip-op (doctrine pages)"],
        "%d hits / %d substantive pages; case pages: %d hits / %d pages" % (
            t["slip_ops"], t["pages"], cp["slip_ops"], cp["count"]),
        "76-11 (pattern page Knock-and-Talk converted) = 65 on the doctrine side; "
        "only the pattern page's slip-ops are converted so far.")
    add("TEACH-05 em-dash",
        T3_SNAPSHOT["TEACH-05 em-dash"],
        "%d em-dashes / %d words / %d pages (%.1f/1k mean)" % (
            t["em_dashes"], t["words"], t["pages"], t["emdash_per_1k_mean"]),
        "page set grew 48→%d (41 stub nodes + splits add ~17k words, ~200 em-dashes; "
        "pattern page 96→38). Rewrite pass not yet run corpus-wide." % t["pages"])
    lk = t["leak_lines"]
    add("TEACH-02c pipeline-vocab leak lines",
        T3_SNAPSHOT["TEACH-02c pipeline-vocab leak lines"],
        "%d leak lines / classes c1=%d, c2=%d, c3=%d, c4=%d" % (
            lk["total"], lk["class1_no_standalone"], lk["class2_cl_confirm"],
            lk["class3_meta_intro"], lk["class4_woven_in"]),
        "c1/c2 hold EXACT (23/10); c3 meta-intro proliferated 5→%d (S5/S6 templated the "
        "'Role-based ... no SCOTUS' developments-intro corpus-wide); c4 1→2 (Tents)."
        % lk["class3_meta_intro"])
    add("TEACH-04d inverted labels",
        T3_SNAPSHOT["TEACH-04d inverted labels"],
        "%d sites / %d pages" % (t["inverted_labels"],
                                 sum(1 for r in survey["pages"] if r["inverted_labels"] > 0)),
        "grew 21→%d: FA Framework 6→12 + 6 more pages gained inverted weight cells as "
        "S6 populated Key/Related tables." % t["inverted_labels"])
    add("TEACH-04e field-framing (literal donor label)",
        T3_SNAPSHOT["TEACH-04e field-framing"],
        "%d literal 'Field framing (apply it angle)' labels / %d pages" % (
            t["field_framing"], sum(1 for r in survey["pages"] if r["field_framing"] > 0)),
        "METRIC DIFFERENCE, not migration: snapshot's 19 used a broad officer-framing "
        "heuristic ('Apply it', 'In the field', ...) still present on legacy pages; this "
        "counts only the exact donor label. Re-derive TEACH-04e prose targets at authoring.")
    add("TEACH-08 RD-family heading",
        T3_SNAPSHOT["TEACH-08 RD-family heading"],
        "%d pages carry RD-family; %d pages already on LCD standard" % (
            t["rd_heading_pages"], t["lcd_heading_pages"]),
        "35→%d (pattern page Knock-and-Talk migrated RD→'Lower-court developments'; PC/RS "
        "was already conformant)." % t["rd_heading_pages"])
    add("TEACH-12a missing H1",
        T3_SNAPSHOT["TEACH-12a missing H1"],
        "%d pages missing H1" % t["missing_h1_pages"],
        "18→%d (pattern page gained its H1). The 41 placed-stub nodes all carry H1." % t["missing_h1_pages"])
    add("TEACH-12b legacy Rule skeleton",
        T3_SNAPSHOT["TEACH-12b legacy Rule skeleton"],
        "%d pages carry '## Rule' skeleton" % t["rule_skeleton_pages"],
        "unchanged 6/6 (Common Law Origins, FA Analysis Checklist, FA Framework, "
        "FA Recalibration, CREW, Three Golden Rules).")
    return rows


def render_md(survey, t1, t2, t3):
    L = []
    W = L.append
    tot = survey["totals"]
    W("# S7 Doctrine Production — regenerated worklist (post-S3/S5/S6 tree)")
    W("")
    W("Regenerated by `scripts/s7/build_worklist.py` from `_run/o2-execute/s7-survey.json` "
      "(rebuilt by `scripts/s7/survey.py`) against the CURRENT tree. Supersedes the "
      "2026-07-03 snapshot in `_overhaul2/S7-CHANGELIST.md` for PATHS + DEFECT FLAGS; "
      "**tiers are user-owned (spec R2) and carried UNCHANGED**. Regenerate-don't-hand-edit.")
    W("")
    W("**State of the tree:** S3 restructure DONE (13-category tree; 41 Table-2 nodes "
      "placed as draft stubs; 3 Table-1 parents dissolved into sub-umbrella `index.md` "
      "landings). S5 converter + S6 case-minting DONE (607 case pages). **S7 doctrine "
      "authoring NOT done except the pattern page (Knock and Talk).** The 46 non-no-op "
      "Table-1 legacy pages remain `status: verified` with legacy defects; the 41 Table-2 "
      "nodes are `status: draft` placed-empty stubs (30-37 words, 'Placed by S3' placeholder).")
    W("")
    W("Flag legend (from survey, current): H1✓/✗ · Rule-skel !/- · slip N (TEACH-03) · "
      "RD|no-RD[/LCD] (TEACH-08) · ff N literal field-framing labels (TEACH-04e) · "
      "lk N pipeline-vocab leak lines with class split (TEACH-02c) · inv N inverted "
      "weight labels (TEACH-04d) · em N (per-1k) (TEACH-05) · frontmatter status.")
    W("")
    W("## Table 1 — existing pages (48): old path → current path, tier carried, flags refreshed")
    W("")
    W("| # | Old path (content/) | Current path | Tier (signed) | Current flags | Fix tags | Note |")
    W("|---|---|---|---|---|---|---|")
    for r in t1:
        cur = r["current_path"] or "**UNRESOLVED**"
        W("| %d | %s | %s | %s | %s | %s | %s |" % (
            r["n"], r["old_path"].replace("content/", ""), cur, r["tier_signed"],
            flags_str(r["current_flags"]), r["fix_tags"],
            (r["split_note"] or ("resolved: " + r["resolution"] if r["resolution"] != "basename-match" else ""))))
    unresolved = [r for r in t1 if not r["resolved"]]
    W("")
    W("Table 1 resolution: **%d/%d resolved**, %d unresolved." % (
        len(t1) - len(unresolved), len(t1), len(unresolved)))
    W("")
    W("## Table 2 — new-prose nodes (45): existence + authoring state")
    W("")
    W("| # | Node | Expected file | Tier (signed) | Current path | State | words/status | Source |")
    W("|---|---|---|---|---|---|---|---|")
    for r in t2:
        cur = r["current_path"] or "**ABSENT**"
        ws = ("%s/%s" % (r["words"], r["status"])) if r["words"] is not None else "—"
        exp = r["expected_basename"]
        if exp.startswith("__"):
            exp = exp.split(":", 1)[-1]
        W("| %d | %s | %s | %s | %s | %s | %s | %s |" % (
            r["n"], r["node"], exp, r["tier_signed"], cur, r["state"], ws, r["source"]))
    absent = [r for r in t2 if not r["exists"]]
    stubs = [r for r in t2 if r["state"] == "placed-stub"]
    authored = [r for r in t2 if r["state"] == "authored"]
    W("")
    W("Table 2: **%d/%d nodes exist** (%d placed-stub · %d authored · %d in-page/retained-parent/cross-ref), "
      "%d absent." % (
        sum(1 for r in t2 if r["exists"]), len(t2), len(stubs), len(authored),
        sum(1 for r in t2 if r["state"] in ("in-page", "retained-parent", "cross-ref")),
        len(absent)))
    W("")
    W("## Table 3 — corpus passes: snapshot → current (recomputed from survey)")
    W("")
    W("| Pass | Snapshot (2026-07-03) | Current (survey) | Note |")
    W("|---|---|---|---|")
    for r in t3:
        W("| %s | %s | %s | %s |" % (r["pass"], r["snapshot"], r["current"], r["note"]))
    W("")
    W("Corpus totals (survey): %d substantive pages · %d em-dashes / %d words (%.1f/1k) · "
      "slip-op %d · leak-lines %d · inverted %d · field-framing %d · missing-H1 %d · "
      "rule-skel %d · RD %d · LCD %d · case-pages %d (slip-op %d)." % (
        tot["pages"], tot["em_dashes"], tot["words"], tot["emdash_per_1k_mean"],
        tot["slip_ops"], tot["leak_lines"]["total"], tot["inverted_labels"],
        tot["field_framing"], tot["missing_h1_pages"], tot["rule_skeleton_pages"],
        tot["rd_heading_pages"], tot["lcd_heading_pages"],
        survey["case_pages"]["count"], survey["case_pages"]["slip_ops"]))
    W("")
    return "\n".join(L) + "\n"


def main(argv):
    survey = load_survey()
    by_path, by_base = build_indexes(survey)
    t1 = build_t1(by_path, by_base)
    t2 = build_t2(by_path, by_base)
    t3 = build_t3(survey)
    worklist = {
        "generated_by": "scripts/s7/build_worklist.py",
        "source_survey": SURVEY_REL,
        "source_changelist": "_overhaul2/S7-CHANGELIST.md (2026-07-03; tiers signed)",
        "discipline": "tiers user-owned (R2), carried unchanged; paths resolved "
                      "programmatically; unlocated pages flagged unresolved not guessed",
        "table1": t1, "table2": t2, "table3": t3,
        "summary": {
            "t1_rows": len(t1),
            "t1_resolved": sum(1 for r in t1 if r["resolved"]),
            "t1_unresolved": [r["n"] for r in t1 if not r["resolved"]],
            "t1_split_into_index_landing": sorted(T1_SPLIT_LANDINGS.keys()),
            "t2_rows": len(t2),
            "t2_exists": sum(1 for r in t2 if r["exists"]),
            "t2_absent": [r["n"] for r in t2 if not r["exists"]],
            "t2_placed_stub": [r["n"] for r in t2 if r["state"] == "placed-stub"],
            "t2_authored": [r["n"] for r in t2 if r["state"] == "authored"],
        },
    }
    md = render_md(survey, t1, t2, t3)
    if "--stdout" in argv:
        sys.stdout.write(json.dumps(worklist, ensure_ascii=False, indent=2) + "\n")
        sys.stdout.write("\n----- S7-WORKLIST.md -----\n")
        sys.stdout.write(md)
        return 0
    with open(os.path.join(REPO_ROOT, OUT_JSON_REL), "w", encoding="utf-8") as f:
        json.dump(worklist, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(os.path.join(REPO_ROOT, OUT_MD_REL), "w", encoding="utf-8") as f:
        f.write(md)
    s = worklist["summary"]
    sys.stderr.write(
        "[s7-worklist] T1 %d/%d resolved (unresolved=%s) | T2 %d/%d exist "
        "(stub=%d authored=%d absent=%s)\n" % (
            s["t1_resolved"], s["t1_rows"], s["t1_unresolved"],
            s["t2_exists"], s["t2_rows"], len(s["t2_placed_stub"]),
            len(s["t2_authored"]), s["t2_absent"]))
    sys.stderr.write("[s7-worklist] wrote %s + %s\n" % (OUT_JSON_REL, OUT_MD_REL))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
