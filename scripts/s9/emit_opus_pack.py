#!/usr/bin/env python3
"""S9 R1 Opus panel-vote lane — clean, driven emission module.

The Opus model-diversity lane is the 3rd panel lens (1 Claude + 2 Codex, spec
S9 R1). `panel_review.generate_opus_pack` writes a self-contained prompt-pack; a
fresh o2-opus-xhigh reviewer Agent consumes ONLY that pack's inlined evidence and
returns one JSON object of the shape:

    {"packs": [ {"group_id": "<obj path>", "lens": "opus-both",
                 "reviewed": [ <per-assertion item>, ... ]}, ... ]}

where each `reviewed[]` item is the SAME per-assertion contract the two Codex
lenses return (`assertion_id`, `dimension`, `verdict` in
{stands|refuted|stands-modified}, `verifiable_from_disclosed`, `defect`|null,
`reasons`, `breaks_true_positives`, `residual_risks`, `suggested_tightening`).
The Opus lens is `opus-both`: it carries NO charter subset — it reviews and votes
on EVERY paneled dimension (model diversity on every tally).

This module reads one or more reviewer JSON files + their batch manifest(s) and
emits, through the EXACT `panel_review.emit_lens_result` contract (no fork), the
same deterministic finding-id + cross-lens dedup + fail-closed logic the Codex
lanes use:
  * s9.finding.v1     (defects only; id = F-S9-PR-sha1(object|assertion_id|dim)[:10])
  * s9.vote.v1        (lane=claude-opus-panel, model=claude-opus-4-8; `verdict`
                       in FINDING-semantics via _ASSERTION_TO_FINDING_VERDICT)
  * s9.attestation.v1 (wholly-clean groups only)
  * panel-results/<lane_id>.json (the full verdict map -> orchestrator backfill)

Because the finding-id is deterministic in (object, assertion_id, dimension), an
Opus refutation of an assertion a Codex lane already raised MERGES onto that same
finding — a 2-vote (codex-A + codex-B) finding becomes a 3-vote paneled finding
(the distinct 3rd lane the >=2-of-3 tally / check_ledger inv-2 requires).

Lane string — GROUND TRUTH (not the informal "opus-panel"): the vote /
attestation / finding.found_by `lane` field is **claude-opus-panel**. The pilot's
already-emitted rows and the orchestrator's already-written adjudication tallies
key on `claude-opus-panel` as the distinct 3rd lane beside `codex-A` / `codex-B`.
The `opus-panel-<batch>-<short>` token is ONLY the per-invocation `lane_id`
(panel-results filename), never the vote lane. Kept as the module constant
OPUS_LANE so it is a one-line change if the orchestrator ever re-keys.

Fail-closed: a group present in the batch manifest but MISSING / empty / malformed
in the reviewer JSON is emitted as a `no_review` result (no rows, no clean
attestation) — never a fabricated finding, never a false clean bill of health.

Idempotent / resumable: a group already carrying an Opus attestation OR an Opus
vote (checked against the live ledger, robust to a crash between vote-append and
result-persist) is SKIPPED — re-emit never double-counts and never writes a
duplicate-lane vote (inv-2 forbids two votes from one lane on one finding).

Stdlib only. COMMIT NOTHING. content/lake read-only. Zero CL, zero codex.
"""

import argparse
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lane_runner as lr          # noqa: E402
import panel_review as pr         # noqa: E402
import check_ledger               # noqa: E402

OPUS_MODEL = pr.OPUS_MODEL                 # claude-opus-4-8
OPUS_LANE = "claude-opus-panel"            # vote/attestation lane (inv-2 3rd lane)
OPUS_LENS = "opus-both"                    # reviews EVERY paneled dimension


# ==========================================================================
# 1. Inputs — batch manifests + reviewer JSON files
# ==========================================================================

def load_batch_manifest(path):
    """Load a `<batch_id>.manifest.json` (schema s9.opus-pack.v1). Returns
    {batch_id, path, groups:{group_id -> {lane_id, total}}}."""
    with open(path, encoding="utf-8") as f:
        m = json.load(f)
    batch_id = m.get("batch_id")
    groups = {}
    for g in m.get("groups", []):
        gid = g.get("group_id")
        if not gid:
            continue
        lane_id = g.get("lane_id") or ("opus-panel-%s-%s" % (batch_id, lr._short(gid)))
        groups[gid] = {"lane_id": lane_id, "total": g.get("total")}
    return {"batch_id": batch_id, "path": path, "groups": groups}


def load_reviews(paths):
    """Merge one or more {"packs":[...]} reviewer files -> {group_id -> reviewed}.
    `reviewed` is the reviewer's list, or None if absent/malformed. First
    occurrence of a group wins (later duplicates recorded, not merged). A file
    that will not parse / lacks packs[] is recorded as bad and skipped (a broken
    reviewer file NEVER fabricates a review)."""
    by_group, dupes, bad = {}, [], []
    for p in paths:
        try:
            with open(p, encoding="utf-8") as f:
                d = json.load(f)
        except (OSError, ValueError) as e:
            bad.append({"file": p, "error": "unreadable/unparseable: %s" % e})
            continue
        packs = d.get("packs") if isinstance(d, dict) else None
        if not isinstance(packs, list):
            bad.append({"file": p, "error": "no packs[] array"})
            continue
        for pk in packs:
            if not isinstance(pk, dict):
                continue
            gid = pk.get("group_id")
            if not gid:
                continue
            if gid in by_group:
                dupes.append(gid)
                continue
            reviewed = pk.get("reviewed")
            by_group[gid] = reviewed if isinstance(reviewed, list) else None
    return by_group, dupes, bad


# ==========================================================================
# 2. Resumable checkpoint — which objects are already Opus-done
# ==========================================================================

def opus_done_objects(ledger_dir, opus_lane=OPUS_LANE):
    """Objects (= panel group ids) already reviewed by the Opus lane: any object
    with an Opus attestation OR any object one of whose findings already carries
    an Opus vote (finding.id -> finding.object). Derived from the LIVE ledger
    rows (not just panel-results), so it is robust to a crash between the
    vote-append and the result-persist. This is the idempotency/resume key."""
    done = set()

    ap = os.path.join(ledger_dir, "panel-attestations.jsonl")
    if os.path.exists(ap):
        with open(ap, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if r.get("lane") == opus_lane and r.get("object"):
                    done.add(r["object"])

    fobj = {}
    fp = os.path.join(ledger_dir, "findings.jsonl")
    if os.path.exists(fp):
        with open(fp, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if r.get("id") and r.get("object"):
                    fobj[r["id"]] = r["object"]

    vp = os.path.join(ledger_dir, "votes.jsonl")
    if os.path.exists(vp):
        with open(vp, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if r.get("lane") == opus_lane:
                    obj = fobj.get(r.get("finding_id"))
                    if obj:
                        done.add(obj)
    return done


# ==========================================================================
# 3. The emit driver
# ==========================================================================

def _is_reviewed_ok(reviewed):
    return (isinstance(reviewed, list) and len(reviewed) > 0
            and all(isinstance(x, dict) for x in reviewed))


def emit_opus_packs(review_paths, manifest_paths, run_id="prod",
                    ledger_dir=lr.RUN_DIR, worklist_idx=None, inv_by_id=None,
                    dry_run=False, opus_lane=OPUS_LANE):
    """Emit Opus panel rows for every group the batch manifest(s) declare owed,
    routed from the reviewer JSON file(s). Returns a report dict.

    Contract, per group:
      * already Opus-done  -> SKIP (idempotent/resume).
      * well-formed review -> pr.emit_lens_result(lane=claude-opus-panel):
          defects -> finding (deduped) + vote; agreement on a sibling finding ->
          vote; wholly clean (no in-charter defect) -> clean attestation.
      * missing/empty/malformed review -> no_review (no rows; driver re-dispatches).
    """
    worklist_idx = worklist_idx or pr.load_worklist_index(pr._default_worklist())
    inv_by_id = inv_by_id if inv_by_id is not None else pr.load_inventory_index()

    reviews, dupes, bad_files = load_reviews(review_paths)
    manifests = [load_batch_manifest(p) for p in manifest_paths]
    done = opus_done_objects(ledger_dir, opus_lane)

    owed = {}   # group_id -> {lane_id, manifest_ref, total}
    for m in manifests:
        for gid, g in m["groups"].items():
            owed.setdefault(gid, {"lane_id": g["lane_id"],
                                  "manifest_ref": m["path"], "total": g["total"]})

    report = {"emitted": [], "skipped_done": [], "no_review": [],
              "unroutable_packs": sorted(g for g in reviews if g not in owed),
              "dupe_packs": dupes, "bad_files": bad_files,
              "run_id": run_id, "opus_lane": opus_lane, "dry_run": dry_run}

    for gid, g in sorted(owed.items()):
        lane_id = g["lane_id"]
        manifest_ref = g["manifest_ref"]
        if gid in done:
            report["skipped_done"].append(gid)
            continue
        try:
            resolved = pr.resolve_group(gid, worklist_idx=worklist_idx,
                                        inv_by_id=inv_by_id)
        except KeyError as e:
            report["no_review"].append({"group_id": gid, "lane_id": lane_id,
                                        "reason": "unresolvable group: %s" % e})
            continue

        reviewed = reviews.get(gid)
        parsed_ok = _is_reviewed_ok(reviewed)

        if dry_run:
            (report["emitted"] if parsed_ok else report["no_review"]).append(
                {"group_id": gid, "lane_id": lane_id, "dry_run": True,
                 "would_review": len(reviewed) if isinstance(reviewed, list) else 0,
                 "group_total": resolved["total"]})
            continue

        if parsed_ok:
            result = {"parse_status": "parsed", "attempts": 1,
                      "wall_clock_s": None, "tokens": None, "last_message": None}
            obj_json = {"reviewed": reviewed}
        else:
            result = {"parse_status": "no_review", "attempts": 1,
                      "wall_clock_s": None, "tokens": None, "last_message": None,
                      "note": "group absent/empty/malformed in reviewer JSON "
                              "(fail-closed no_review; driver re-dispatches)"}
            obj_json = None

        summary = pr.emit_lens_result(
            resolved, OPUS_LENS, OPUS_MODEL, run_id, lane_id, obj_json,
            result, manifest_ref, ledger_dir, lane=opus_lane)

        if parsed_ok:
            report["emitted"].append({
                "group_id": gid, "lane_id": lane_id,
                "findings_emitted": summary["findings_emitted"],
                "votes": len(summary["votes_emitted"]),
                "clean_attestation": summary["clean_attestation"],
                "reviewed_count": summary["reviewed_count"],
                "group_total": resolved["total"]})
        else:
            report["no_review"].append({"group_id": gid, "lane_id": lane_id,
                                        "parse_status": "no_review"})

    live = [e for e in report["emitted"] if not e.get("dry_run")]
    report["totals"] = {
        "owed_groups": len(owed),
        "emitted_groups": len(report["emitted"]),
        "skipped_done": len(report["skipped_done"]),
        "no_review": len(report["no_review"]),
        "unroutable_packs": len(report["unroutable_packs"]),
        "bad_files": len(bad_files),
        "findings_new": sum(len(e.get("findings_emitted", [])) for e in live),
        "votes_new": sum(e.get("votes", 0) for e in live),
        "clean_attestations": sum(1 for e in live if e.get("clean_attestation")),
    }
    return report


# ==========================================================================
# 4. Self-test (MOCK — no live Opus, no real ledger rows)
# ==========================================================================

def _write(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False)


def _reviewed_item(aid, dim, verdict, defect=None):
    return {"assertion_id": aid, "dimension": dim, "verdict": verdict,
            "verifiable_from_disclosed": True, "defect": defect,
            "reasons": ["mock reason"], "breaks_true_positives": False,
            "residual_risks": [], "suggested_tightening": None}


def _count_lines(p):
    return sum(1 for _ in open(p)) if os.path.exists(p) else 0


def _votes_for(ledger_dir, fid):
    out = []
    p = os.path.join(ledger_dir, "votes.jsonl")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                r = json.loads(line)
                if r.get("finding_id") == fid:
                    out.append(r)
    return out


def self_test():
    errs = []
    fx = pr._build_panel_fixtures()
    wl_idx = pr.load_worklist_index(fx["wl_path"])
    inv_idx = pr.load_inventory_index(fx["inv_path"])
    gid = fx["content_obj"]
    _orig_lake, _orig_text = pr.LAKE_CASES_DIR, pr.POOL_TEXT_DIR
    pr.LAKE_CASES_DIR = fx["lake_dir"]
    pr.POOL_TEXT_DIR = fx["text_dir"]
    tmp = []

    def _emit(review_obj, ledger_dir, **kw):
        rp = os.path.join(ledger_dir, "_review.json")
        _write(rp, review_obj)
        return emit_opus_packs([rp], [man_path], ledger_dir=ledger_dir,
                               worklist_idx=wl_idx, inv_by_id=inv_idx, **kw)

    # batch manifest with our one fixture group
    man_dir = tempfile.mkdtemp(prefix="s9-opus-fx-man-")
    tmp.append(man_dir)
    lane_id = "opus-panel-selftest-%s" % lr._short(gid)
    man_path = os.path.join(man_dir, "selftest-opus.manifest.json")
    _write(man_path, {"schema": "s9.opus-pack.v1", "batch_id": "selftest-opus",
                      "model": OPUS_MODEL,
                      "groups": [{"group_id": gid, "lane_id": lane_id, "total": 4}]})

    fid_quote = pr.finding_id_for(gid, "fx_quote", "quote_fidelity")

    try:
        # -- (a) clean group -> Opus attestation w/ lane=claude-opus-panel -----
        L = tempfile.mkdtemp(prefix="s9-opus-clean-"); tmp.append(L)
        clean_review = {"packs": [{"group_id": gid, "lens": OPUS_LENS, "reviewed": [
            _reviewed_item("fx_exist", "existence", "stands"),
            _reviewed_item("fx_support", "support", "stands"),
            _reviewed_item("fx_quote", "quote_fidelity", "stands"),
            _reviewed_item("fx_treat", "treatment", "stands"),
        ]}]}
        rep = _emit(clean_review, L)
        ap = os.path.join(L, "panel-attestations.jsonl")
        if _count_lines(ap) != 1:
            errs.append("(a) clean group did not emit exactly 1 attestation (%d)" % _count_lines(ap))
        else:
            att = json.loads(open(ap).readline())
            if att.get("lane") != OPUS_LANE:
                errs.append("(a) attestation lane=%r != %r" % (att.get("lane"), OPUS_LANE))
            if att.get("lens") != OPUS_LENS:
                errs.append("(a) attestation lens=%r != opus-both" % att.get("lens"))
        if _count_lines(os.path.join(L, "findings.jsonl")) != 0:
            errs.append("(a) clean group wrongly wrote a finding")
        if rep["totals"]["clean_attestations"] != 1:
            errs.append("(a) report clean_attestations != 1: %s" % rep["totals"])

        # -- (b) MERGE: 2 codex votes -> 3 votes; dedup; deterministic id; ----
        #        vote lane=claude-opus-panel; NO spurious clean attestation.
        L = tempfile.mkdtemp(prefix="s9-opus-merge-"); tmp.append(L)
        resolved = pr.resolve_group(gid, worklist_idx=wl_idx, inv_by_id=inv_idx)
        cod_iv = _reviewed_item("fx_quote", "quote_fidelity", "refuted",
                                defect={"problem": "quote drift", "severity": "high",
                                        "proposed_fix": "restore", "evidence_quote": "x",
                                        "needs_cl": False, "locator_note": "pin-1"})
        frow = pr.build_finding_row(resolved, cod_iv, "A", "selftest", None)
        lr.emit_row(frow, L)
        lr.emit_row(pr.build_vote_row(fid_quote, cod_iv, "A", pr.CODEX_MODEL, None), L)
        lr.emit_row(pr.build_vote_row(fid_quote, cod_iv, "B", pr.CODEX_MODEL, None), L)
        if frow["id"] != fid_quote:
            errs.append("(b) codex finding id %s != deterministic %s" % (frow["id"], fid_quote))
        merge_review = {"packs": [{"group_id": gid, "lens": OPUS_LENS, "reviewed": [
            _reviewed_item("fx_exist", "existence", "stands"),
            _reviewed_item("fx_support", "support", "stands"),
            _reviewed_item("fx_quote", "quote_fidelity", "refuted",
                           defect={"problem": "agree drift", "severity": "high",
                                   "proposed_fix": "restore", "evidence_quote": "x",
                                   "needs_cl": False, "locator_note": "pin-1"}),
            _reviewed_item("fx_treat", "treatment", "stands"),
        ]}]}
        rep = _emit(merge_review, L)
        if _count_lines(os.path.join(L, "findings.jsonl")) != 1:
            errs.append("(b) finding not deduped (%d rows; want 1)"
                        % _count_lines(os.path.join(L, "findings.jsonl")))
        vs = _votes_for(L, fid_quote)
        lanes = sorted(v.get("lane") for v in vs)
        if lanes != ["claude-opus-panel", "codex-A", "codex-B"]:
            errs.append("(b) merged finding lanes %s != codex-A/codex-B/claude-opus-panel" % lanes)
        if len(lanes) != len(set(lanes)):
            errs.append("(b) duplicate lane vote on merged finding: %s" % lanes)
        opus_v = [v for v in vs if v.get("lane") == OPUS_LANE]
        # assertion 'refuted' -> FINDING-semantics 'stands' (defect real; finding stands)
        if not opus_v or opus_v[0].get("verdict") != "stands":
            errs.append("(b) opus vote verdict %s != 'stands' (assertion->finding inversion)"
                        % (opus_v[0].get("verdict") if opus_v else None))
        if _count_lines(os.path.join(L, "panel-attestations.jsonl")) != 0:
            errs.append("(b) FAIL-OPEN: opus wrote a clean attestation on a group it refuted")

        # -- (c) fail-closed: group missing from reviewer JSON -> no_review ----
        L = tempfile.mkdtemp(prefix="s9-opus-noreview-"); tmp.append(L)
        rep = _emit({"packs": []}, L)   # manifest owes gid; reviewer returned none
        if rep["totals"]["no_review"] != 1:
            errs.append("(c) missing group not routed to no_review: %s" % rep["totals"])
        if _count_lines(os.path.join(L, "findings.jsonl")) != 0:
            errs.append("(c) no_review fabricated a finding")
        if _count_lines(os.path.join(L, "panel-attestations.jsonl")) != 0:
            errs.append("(c) no_review wrongly wrote a clean attestation (fail-open)")
        # malformed reviewed[] (not a list of dicts) -> also no_review
        L2 = tempfile.mkdtemp(prefix="s9-opus-garbage-"); tmp.append(L2)
        rep2 = _emit({"packs": [{"group_id": gid, "reviewed": "not-a-list"}]}, L2)
        if rep2["totals"]["no_review"] != 1 or _count_lines(os.path.join(L2, "findings.jsonl")) != 0:
            errs.append("(c) malformed reviewed[] not fail-closed: %s" % rep2["totals"])

        # -- (d) idempotent / resumable: re-emit does not double-count ---------
        L = tempfile.mkdtemp(prefix="s9-opus-idem-"); tmp.append(L)
        # seed the same 2 codex votes + finding so opus merges (defect path)
        lr.emit_row(pr.build_finding_row(resolved, cod_iv, "A", "selftest", None), L)
        lr.emit_row(pr.build_vote_row(fid_quote, cod_iv, "A", pr.CODEX_MODEL, None), L)
        lr.emit_row(pr.build_vote_row(fid_quote, cod_iv, "B", pr.CODEX_MODEL, None), L)
        r1 = _emit(merge_review, L)
        v1 = _count_lines(os.path.join(L, "votes.jsonl"))
        r2 = _emit(merge_review, L)          # re-run identical input
        v2 = _count_lines(os.path.join(L, "votes.jsonl"))
        if r1["totals"]["emitted_groups"] != 1:
            errs.append("(d) first emit did not emit the group: %s" % r1["totals"])
        if r2["totals"]["emitted_groups"] != 0 or r2["totals"]["skipped_done"] != 1:
            errs.append("(d) re-emit not idempotent (expected skip): %s" % r2["totals"])
        if v1 != v2:
            errs.append("(d) re-emit double-counted votes (%d -> %d)" % (v1, v2))
        vs = _votes_for(L, fid_quote)
        if len(vs) != len(set(v.get("lane") for v in vs)):
            errs.append("(d) re-emit created a duplicate-lane vote: %s"
                        % sorted(v.get("lane") for v in vs))

        # -- (e) LINT-30: real opus path -> 3-lane paneled finding reconciles --
        L = tempfile.mkdtemp(prefix="s9-opus-l30-"); tmp.append(L)
        lr.emit_row(pr.build_finding_row(resolved, cod_iv, "A", "selftest", None), L)
        lr.emit_row(pr.build_vote_row(fid_quote, cod_iv, "A", pr.CODEX_MODEL, None), L)
        lr.emit_row(pr.build_vote_row(fid_quote, cod_iv, "B", pr.CODEX_MODEL, None), L)
        _emit(merge_review, L)   # real opus emission -> 3rd vote (claude-opus-panel)
        # orchestrator-authored adjudication (MODIFIED) + fix (FIXED); role-separated
        adj = {"schema": "s9.adjudication.v1", "finding_id": fid_quote,
               "refute_tally": {"per-lane": {"codex-A": "stands", "codex-B": "stands",
                                             OPUS_LANE: "stands"},
                                "rule": ">=2-of-3 refute kills",
                                "result": "adjudicated on evidence"},
               "verdict": "MODIFIED", "adjudicated_holding": ["restore the verbatim quote"],
               "evidence": [{"kind": "lake", "ref": "pin-1"}],
               "adjudicator": {"lane": "claude-fable-5-orchestrator", "model": "claude-fable-5"},
               "role_separation": "finder codex-A != adjudicator claude-fable-5-orchestrator",
               "spawned_findings": [], "at": lr._now()}
        with open(os.path.join(L, "adjudications.jsonl"), "w") as f:
            f.write(json.dumps(adj) + "\n")
        fix = {"schema": "s9.fix.v1", "finding_id": fid_quote,
               "adjudication_verdict": "MODIFIED",
               "applied_by": {"lane": "o2-opus-xhigh", "model": OPUS_MODEL},
               "artifacts": ["fixture"], "content_edits": "restored quote",
               "loops": [{"loop": 1, "re_review": {"lane": "codex-C", "model": pr.CODEX_MODEL,
                                                   "round": 1, "verdict": "FIXED"}}],
               "loop_cap": 3, "writer_neq_checker": "author o2-opus-xhigh != reviewer codex-C",
               "at": lr._now()}
        with open(os.path.join(L, "fixes.jsonl"), "w") as f:
            f.write(json.dumps(fix) + "\n")
        viols, status = check_ledger.check_ledger(L)
        nh = sum(1 for x in viols if x["severity"] == check_ledger.c.HIGH)
        if status != "CHECKED" or nh != 0:
            errs.append("(e) opus-merged ledger not LINT-30 green: status=%s HIGH=%d %s"
                        % (status, nh, [x["message"][:70] for x in viols][:4]))
    finally:
        pr.LAKE_CASES_DIR = _orig_lake
        pr.POOL_TEXT_DIR = _orig_text
        for x in tmp + [fx["root"]]:
            shutil.rmtree(x, ignore_errors=True)

    for e in errs:
        sys.stderr.write("[self-test-opus] FAIL: %s\n" % e)
    sys.stderr.write("[self-test-opus] emit_opus_pack %s (%d breaches)\n"
                     % ("PASS" if not errs else "FAIL", len(errs)))
    return 0 if not errs else 1


# ==========================================================================
# 5. CLI
# ==========================================================================

def main(argv=None):
    ap = argparse.ArgumentParser(
        description="S9 R1 Opus panel-vote lane emission (claude-opus-panel).")
    ap.add_argument("--reviews", nargs="+", metavar="JSON",
                    help="one or more reviewer output files ({\"packs\":[...]})")
    ap.add_argument("--manifests", nargs="+", metavar="MANIFEST",
                    help="the matching batch manifest(s) (<batch_id>.manifest.json)")
    ap.add_argument("--run-id", default="prod")
    ap.add_argument("--ledger-dir", default=lr.RUN_DIR)
    ap.add_argument("--dry-run", action="store_true",
                    help="report routing/coverage without emitting any row")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()
    if not args.reviews or not args.manifests:
        ap.error("--reviews and --manifests are required (or use --self-test)")
    rep = emit_opus_packs(args.reviews, args.manifests, run_id=args.run_id,
                          ledger_dir=args.ledger_dir, dry_run=args.dry_run)
    sys.stdout.write(json.dumps(rep, ensure_ascii=False, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
