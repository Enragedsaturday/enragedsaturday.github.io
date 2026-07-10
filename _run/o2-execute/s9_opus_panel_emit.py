#!/usr/bin/env python3
"""S9 R1 Opus PANEL-VOTE lane (pack-001) emission.
Lane: claude-opus-panel  model: claude-opus-4-8  lens: opus-both (model diversity).
Refute-framed, evidence = ONLY the opus-pack-001 disclosures.
Emits: s9.finding.v1 (defects) -> findings.jsonl
       s9.vote.v1                -> votes.jsonl
       s9.attestation.v1 (clean) -> panel-attestations.jsonl
       per-lane result JSONs (verdict_maps) -> panel-results/  (approvals record)
All appends flock-safe via lane_runner.locked_append / emit_row.
"""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "scripts", "s9"))
sys.path.insert(0, "/Users/johngalt/Projects/cssi-quartz/scripts/s9")
import lane_runner as lr

RUN = lr.RUN_DIR
MANIFEST_REF = "_run/s9/opus-packs/opus-pack-001.manifest.json"
LANE = "claude-opus-panel"
MODEL = "claude-opus-4-8"
NOW = lr._now

def vote_row(finding_id, verdict, panel_dim, reasons, residual=None, tightening=None, breaks_tp=False):
    return {
        "schema": "s9.vote.v1",
        "finding_id": finding_id,
        "lane": LANE,
        "model": MODEL,
        "sandbox": "n/a (Opus panel lane; opus-pack-001 inlined disclosure only)",
        "independent": "isolated pack; sibling votes + in-progress adjudications excluded (R1)",
        "recorded_before_other_votes_read": True,
        "manifest_ref": MANIFEST_REF,
        "verdict": verdict,
        "reasons": reasons,
        "breaks_true_positives": breaks_tp,
        "residual_risks": residual or [],
        "suggested_tightening": tightening,
        "panel_dimension": panel_dim,
        "at": NOW(),
    }

def attest_row(obj, oc, group_id, reviewed_ids, dims, defense_votes):
    return {
        "schema": "s9.attestation.v1",
        "id": "A-S9-PR-OPUS-%s" % lr._short(obj),
        "run": "prod",
        "object": obj,
        "object_class": oc,
        "group_id": group_id,
        "lens": "opus-both",
        "lane": LANE,
        "model": MODEL,
        "verdict": "clean",
        "sandbox": "read-only (opus-pack-001 inlined disclosure)",
        "independent": "isolated review; no sibling votes/adjudications disclosed",
        "reviewed_assertion_ids": reviewed_ids,
        "dimensions_reviewed": dims,
        "defense_votes_cast": defense_votes,
        "manifest_ref": MANIFEST_REF,
        "wall_clock_s": None,
        "tokens": None,
        "recorded_before_reconciliation": True,
        "at": NOW(),
    }

def persist_result(lane_id, summary):
    d = os.path.join(RUN, "panel-results")
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, "%s.json" % lane_id)
    with open(p, "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "raw_reply": None,
                   "parsed": None, "attestation_ref": None}, f,
                  ensure_ascii=False, indent=2, sort_keys=True)
    return p

emitted = {"findings": [], "votes": [], "attestations": [], "results": []}

# ------------------------------------------------------------------ findings
# One new defect: registry shard-1 geofence callout (refused).
geofence_fid = "F-S9-PR-abd71b69e2"
finding = {
    "schema": "s9.finding.v1",
    "id": geofence_fid,
    "run": "prod",
    "object": "_overhaul2/points/registry.yaml#shard-1",
    "object_class": "registry",
    "dimension": "D7",
    "gate": "G2",
    "assertion_id": "43c69d724ec4a300",
    "locator": {"section": {"id": "search.digital.geofence-threshold"}, "lines": None,
                "verbatim": "confirmed by *Chatrie v. United States* (2026, SCOTUS) and *United States v. Smith*, 110 F.4th 817 (5th Cir. 2024) (geofence acquisition IS a search)"},
    "problem": ("Black-letter callout declares geofence acquisition 'confirmed' to be a Fourth "
                "Amendment search on the strength of 'Chatrie v. United States (2026, SCOTUS)'. "
                "That 2026 SCOTUS merits decision is not verifiable from the disclosed evidence "
                "(the registry group discloses only the statement text + registry provenance; no "
                "lake record or opinion text for Chatrie or Smith is inlined). The 'confirmed... IS "
                "a search' framing also forecloses a documented circuit split — United States v. "
                "Smith, 110 F.4th 817 (5th Cir. 2024) treats acquisition as a search, while the "
                "Fourth Circuit en banc in United States v. Chatrie (2024) held the opposite under "
                "the third-party doctrine on the same facts. A draft rule should not present the "
                "threshold as settled absent a verified controlling decision."),
    "severity": "medium",
    "proposed_fix": ("Confirm via CourtListener the existence and precise holding of a 2026 SCOTUS "
                     "Chatrie decision before promotion draft->verified. If unconfirmed, reframe the "
                     "threshold as unsettled/split (Smith 5th Cir. = search; Chatrie 4th Cir. en banc "
                     "= not a search) rather than 'confirmed... IS a search'."),
    "needs_cl": True,
    "found_by": {"lane": LANE, "model": MODEL,
                 "note": "S9 R1 panel-review Opus model-diversity lane; refute-framed; sighted "
                         "(registry statement disclosed; no Chatrie/Smith lake/text in group)",
                 "register": "panel-review.jsonl"},
    "panel_dimension": "black_letter",
    "confidence": 0.7,
}
lr.emit_row(finding, RUN)
emitted["findings"].append(geofence_fid)

# ------------------------------------------------------------------ votes
# (a) the 4 pre-existing pilot findings on Three Golden Rules -> all STANDS
#     (disclosed opinion text moots the pilot lanes' 'no text / unverifiable' premise).
pre_existing = [
    ("F-S9-PR-6d73be7865", "existence", "stands",
     ["Buie opinion text disclosed in-pack (494 U.S. 325): the table cell mirrors Buie's own "
      "Section V holding statement (494 U.S. at 337) — 'a properly limited protective sweep... "
      "when the searching officer possesses a reasonable belief based on specific and articulable "
      "facts that the area to be swept harbors an individual posing a danger to those on the arrest "
      "scene'.",
      "'it is not automatic' tracks Buie verbatim ('decidedly not \"automati[c]\"', 494 U.S. at 336).",
      "The two-tier rule (suspicionless look into immediately-adjoining spaces vs. articulable-facts "
      "sweep beyond, 494 U.S. at 334) is stated in full in the page body (Nuances section); the table "
      "row is a faithful compressed summary, not an existence/support defect."],
     ["A reader taking the table cell in isolation could miss the suspicionless adjoining-spaces "
      "carve-out; the page body cures this."],
     "Optional standalone tightening: append 'beyond spaces immediately adjoining the arrest' to the "
     "table cell — not required, the body states it."),
    ("F-S9-PR-d1d2d45449", "existence", "stands",
     ["Gates opinion text disclosed in-pack: 'probable cause is a fluid concept — turning on the "
      "assessment of probabilities in particular factual contexts' appears verbatim at 462 U.S. 232 "
      "(paragraph b276-5, immediately after the *232 page marker) — exactly the pincite the page uses.",
      "The pilot finding's premise ('fluid' unverifiable / no text file) is mooted: the text is present "
      "and the word 'fluid' is verbatim at 462 U.S. 232."],
     [], None),
    ("F-S9-PR-6ffdcb45b8", "existence", "stands",
     ["Brinegar opinion text disclosed in-pack: 'In dealing with probable cause... we deal with "
      "probabilities. These are not technical; they are the factual and practical considerations of "
      "everyday life on which reasonable and prudent men, not legal technicians, act' appears verbatim "
      "at 338 U.S. 175 (the *175 page marker precedes it).",
      "The table holding is a faithful paraphrase of that verbatim passage; the pilot's 'no pinpoints / "
      "no text' premise is mooted by the disclosed text (pincite 175 confirmed)."],
     [], None),
    ("F-S9-PR-f14d40d43a", "existence", "stands",
     ["Gaetjens opinion text disclosed in-pack (7th Cir., §A The Home Entry): 'government officials may "
      "enter a home without a warrant \"to render assistance or prevent harm to persons or property "
      "within\"' and Allton had 'an objectively reasonable basis for believing that Gaetjens was "
      "experiencing a medical emergency that required immediate action' both appear verbatim — matching "
      "the page's 493-94 pincite and the emergency-aid table holding.",
      "Identity reconciled: the opinion caption is 'Gaetjens v. City of Loves Park, et al.' but same "
      "docket (20-1295), date (July 13, 2021), court (7th Cir.), and cite (4 F.4th 487); CL cluster "
      "4899427 is itself titled 'Sally Gaetjens v. Winnebago County, Illinois' — a co-defendant naming "
      "variant, not a wrong case.",
      "The pilot's 'no pinpoints / no text / unsupported' premise is mooted by the disclosed text."],
     ["Gaetjens lake record status is 'under_review' with empty pinpoints (S6-promotion frontier stub) "
      "— a build-lane artifact, not a content-page existence/support defect."],
     None),
]
tgr_defense_votes = []
for fid, pdim, verdict, reasons, residual, tight in pre_existing:
    lr.emit_row(vote_row(fid, verdict, pdim, reasons, residual, tight), RUN)
    emitted["votes"].append((fid, verdict))
    tgr_defense_votes.append({"finding_id": fid, "verdict": verdict})

# (b) my own new finding vote (geofence) -> refuted (assertion refuted / callout refused)
lr.emit_row(vote_row(
    geofence_fid, "refuted", "black_letter",
    ["The callout's 'confirmed... IS a search' rests on 'Chatrie v. United States (2026, SCOTUS)', "
     "unverifiable from the disclosed evidence (no Chatrie/Smith lake record or opinion text inlined).",
     "The framing overstates certainty against a documented circuit split (Smith 5th Cir. 2024 = search; "
     "Chatrie 4th Cir. en banc 2024 = not a search under the third-party doctrine).",
     "Refute-framed default: a currency-sensitive black-letter claim built on an unverifiable recent "
     "SCOTUS holding is withheld from >=2-approval promotion pending CL confirmation."],
    residual=["If a 2026 SCOTUS Chatrie decision did hold geofence acquisition is a search, the ultimate "
              "proposition may be correct; the defect is verification/currency, not necessarily the holding."],
    tightening="Pending CL confirmation of the 2026 SCOTUS Chatrie decision and its precise holding; else "
               "reframe as unsettled/split rather than 'confirmed'."), RUN)
emitted["votes"].append((geofence_fid, "refuted"))

# ------------------------------------------------------------------ attestations (clean groups)
GROUPS = {
    "bdb7e5f3": {
        "lane_id": "opus-panel-opus-pack-001-bdb7e5f3",
        "object": "content/instructor-craft-and-study/Three Golden Rules.md",
        "oc": "reference", "group_id": "content/instructor-craft-and-study/Three Golden Rules.md",
        "reviewed": ["2309c4de36a9cbe1", "36398c9a434c5c42", "441160dcc43226a9",
                     "4db5f3168693da19", "612bf9c23300c1bd"],
        "dims": ["existence"],
        "clean": True, "defense_votes": tgr_defense_votes,
        "verdict_map": {
            "2309c4de36a9cbe1": {"dimension": "existence", "verdict": "stands", "has_defect": False, "in_charter": True, "verifiable": True},
            "36398c9a434c5c42": {"dimension": "existence", "verdict": "stands", "has_defect": False, "in_charter": True, "verifiable": True},
            "441160dcc43226a9": {"dimension": "existence", "verdict": "stands", "has_defect": False, "in_charter": True, "verifiable": True},
            "4db5f3168693da19": {"dimension": "existence", "verdict": "stands", "has_defect": False, "in_charter": True, "verifiable": True},
            "612bf9c23300c1bd": {"dimension": "existence", "verdict": "stands", "has_defect": False, "in_charter": True, "verifiable": True},
        },
    },
    "29717571": {
        "lane_id": "opus-panel-opus-pack-001-29717571",
        "object": "content/cases/Adams v. Williams.md",
        "oc": "case", "group_id": "content/cases/Adams v. Williams.md",
        "reviewed": ["375f6cf75e380e1f", "3edc4f7d6c32a0a6", "ae1e5de25890641e",
                     "e296c5d3a888fbb9", "10b0337e79b61d1d", "a2f7e053970d5d58"],
        "dims": ["existence", "support", "treatment"],
        "clean": True, "defense_votes": [],
        "verdict_map": {
            "375f6cf75e380e1f": {"dimension": "existence", "verdict": "stands", "has_defect": False, "in_charter": True, "verifiable": True},
            "3edc4f7d6c32a0a6": {"dimension": "support", "verdict": "stands", "has_defect": False, "in_charter": True, "verifiable": True},
            "ae1e5de25890641e": {"dimension": "support", "verdict": "stands", "has_defect": False, "in_charter": True, "verifiable": True},
            "e296c5d3a888fbb9": {"dimension": "support", "verdict": "stands", "has_defect": False, "in_charter": True, "verifiable": True},
            "10b0337e79b61d1d": {"dimension": "treatment", "verdict": "stands", "has_defect": False, "in_charter": True, "verifiable": True},
            "a2f7e053970d5d58": {"dimension": "treatment", "verdict": "stands", "has_defect": False, "in_charter": True, "verifiable": True},
        },
    },
    "11f9d4c4": {
        "lane_id": "opus-panel-opus-pack-001-11f9d4c4",
        "object": "content/foundations-and-the-fourth-amendment/Common Law Origins.md",
        "oc": "doctrine", "group_id": "content/foundations-and-the-fourth-amendment/Common Law Origins.md",
        "reviewed": ["3ba96d7350dc4d1f", "45f4480d3c296341", "c23bbba29e39a8b9"],
        "dims": ["existence", "support"],
        "clean": True, "defense_votes": [],
        "verdict_map": {
            "3ba96d7350dc4d1f": {"dimension": "existence", "verdict": "stands", "has_defect": False, "in_charter": True, "verifiable": True},
            "45f4480d3c296341": {"dimension": "existence", "verdict": "stands", "has_defect": False, "in_charter": True, "verifiable": True},
            "c23bbba29e39a8b9": {"dimension": "support", "verdict": "stands", "has_defect": False, "in_charter": True, "verifiable": True},
        },
    },
}

for key, g in GROUPS.items():
    att = attest_row(g["object"], g["oc"], g["group_id"], g["reviewed"], g["dims"], g["defense_votes"])
    lr.locked_append(os.path.join(RUN, "panel-attestations.jsonl"),
                     json.dumps(att, ensure_ascii=False, sort_keys=True) + "\n")
    emitted["attestations"].append(att["id"])
    summ = {"lane_id": g["lane_id"], "group_id": g["group_id"], "lens": "opus-both",
            "lane": LANE, "model": MODEL, "run": "prod", "parse_status": "parsed",
            "reviewed_count": len(g["reviewed"]), "group_total_assertions": len(g["reviewed"]),
            "findings_emitted": [], "votes_emitted": [{"finding_id": v["finding_id"], "verdict": v["verdict"]} for v in g["defense_votes"]],
            "defense_votes": g["defense_votes"], "clean_attestation": True,
            "verdict_map": g["verdict_map"], "manifest_ref": MANIFEST_REF, "at": NOW()}
    emitted["results"].append(persist_result(g["lane_id"], summ))

# ------------------------------------------------------------------ registry shard-1 result (NOT clean; verdict_map records 26 approvals + 1 refusal)
REG_APPROVE = ["013daefa526380f3","03dec421583bfe70","0787dd6385707143","0986824463e04409",
    "0b964f78008575d8","127557776fcc56e9","1346b602d8057357","17bcb0defb32fa70",
    "1c7d74ed56db81cd","2394d265d63d7f8d","2689cebfe7396083","279187cc9e7295d9",
    "2a175fd27c04eeb8","3577da6c26db25f3","3821aff85041f942","38ed344844bf4425",
    "3ac40bb93369a793","3c0573ff146cff07","3e6ea71b12a92c94","3e9f0aceccfd9058",
    "3ff3ab3badb29c64","403fe0c9e161ec06","44bd386b4eddd1cd","452c9620ed58ea89",
    "48c6526fae5aa416","49c4827034b98c9d"]
REG_REFUSE = "43c69d724ec4a300"
reg_vmap = {aid: {"dimension": "black_letter", "verdict": "stands", "has_defect": False,
                  "in_charter": True, "verifiable": True} for aid in REG_APPROVE}
reg_vmap[REG_REFUSE] = {"dimension": "black_letter", "verdict": "refuted", "has_defect": True,
                        "in_charter": True, "verifiable": False}
assert len(reg_vmap) == 27, len(reg_vmap)
reg_summary = {"lane_id": "opus-panel-opus-pack-001-d208f639",
    "group_id": "_overhaul2/points/registry.yaml#shard-1", "lens": "opus-both",
    "lane": LANE, "model": MODEL, "run": "prod", "parse_status": "parsed",
    "reviewed_count": 27, "group_total_assertions": 27,
    "black_letter_needs_2_approvals": True,
    "findings_emitted": [geofence_fid],
    "votes_emitted": [{"finding_id": geofence_fid, "verdict": "refuted"}],
    "defense_votes": [], "clean_attestation": False,
    "black_letter_tally": {"approved": len(REG_APPROVE), "refused": 1},
    "verdict_map": reg_vmap, "manifest_ref": MANIFEST_REF, "at": NOW()}
emitted["results"].append(persist_result("opus-panel-opus-pack-001-d208f639", reg_summary))

print(json.dumps({
    "findings_appended": emitted["findings"],
    "votes_appended": emitted["votes"],
    "attestations_appended": emitted["attestations"],
    "result_files": [lr._rel(p) for p in emitted["results"]],
    "registry_tally": {"approved": len(REG_APPROVE), "refused": 1},
}, indent=2, ensure_ascii=False))
