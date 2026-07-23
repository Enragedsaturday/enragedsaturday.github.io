#!/usr/bin/env python3
"""
LINT-14 - S2 case page-to-record gate (alias LINT-S2-pagerecord).

Every non-draft `type: case` page must resolve to a lake record whose status is
publish-eligible for S2: verified, under_review, slip_opinion, verified_off_cl,
or verified_identity. Records do not need pages.
"""

import glob
import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

REPO_ROOT = c.REPO_ROOT
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from scripts.s2 import serializer  # noqa: E402

LINT = "LINT-14"
# RULING P4-18(ii) (2026-07-22) — verified_identity JOINS the publish gate, mirroring
# A16's verified_off_cl addition. `verified_identity` is a legitimate S2 R1 listed status:
# the identity two-key is confirmed, but either the party-name-in-text half is not earnable
# from the lead-opinion cache text (party-name-miss / cache-miss) or field_i_validity is
# still `unverified` (breadth-marked promotions), so the record cannot reach `verified`
# without fabricating a two-key leg (schema allOf[1]; S2 R2). Reader safety is the P4-14
# fieldI reader banner, which models exactly {status: verified_identity, field_i: unverified},
# plus every content assertion carrying its own pin/quote discipline. The stronger `verified`
# state is still EARNED per P4-18(i) wherever the cache text supplies the missing leg.
ACCEPTED = {
    "verified",
    "under_review",
    "slip_opinion",
    "verified_off_cl",
    "verified_identity",
}


def load_records(cases_dir=None):
    cases_dir = cases_dir or os.path.join(c.REPO_ROOT, "_overhaul2", "lake", "cases")
    records = {}
    violations = []
    for path in sorted(glob.glob(os.path.join(cases_dir, "*.json"))):
        try:
            record = json.load(open(path, encoding="utf-8"))
        except json.JSONDecodeError as exc:
            violations.append(c.make_violation(
                LINT,
                path,
                getattr(exc, "lineno", 1),
                c.HIGH,
                "S2 lake record JSON parse failed; page-record gate fails closed: %s" % exc.msg,
            ))
            continue
        rid = record.get("record_id")
        if rid in records:
            first_path, _first = records[rid]
            violations.append(c.make_violation(
                LINT,
                path,
                1,
                c.HIGH,
                "duplicate S2 lake record_id %r in %s; first seen in %s"
                % (rid, c.relpath(path), c.relpath(first_path)),
            ))
            continue
        records[rid] = (path, record)
    return records, violations


def page_record_id(path, fm):
    lake = fm.get("lake") if isinstance(fm.get("lake"), dict) else {}
    # CR-12: only fall back to the filename stem when record_id is ABSENT. An
    # explicitly empty `record_id: ""` (an authoring mistake) must NOT be masked as
    # the stem — return it as-is so the page↔record gate flags the malformed override.
    rid = lake.get("record_id")
    if rid is None:
        return os.path.splitext(os.path.basename(path))[0]
    return rid


def check_page(path, records):
    text = serializer.read_markdown(path)
    fm, _body, _start = serializer.split_frontmatter(text)
    if fm.get("type") != "case" or serializer.is_draft_page(fm):
        return []
    out = []
    stem = os.path.splitext(os.path.basename(path))[0]
    rid = page_record_id(path, fm)
    if rid != stem:
        out.append(c.make_violation(
            LINT,
            path,
            1,
            c.HIGH,
            "case page resolves to lake.record_id=%r, but page-backed record_id "
            "must equal filename stem %r [A6/R12]" % (rid, stem),
        ))
    if rid not in records:
        out.append(c.make_violation(
            LINT,
            path,
            1,
            c.HIGH,
            "case page has no matching S2 lake record %r at "
            "_overhaul2/lake/cases/%s.json" % (rid, rid),
        ))
        return out
    record_path, record = records[rid]
    if record.get("stub"):
        out.append(c.make_violation(
            LINT,
            path,
            1,
            c.HIGH,
            "case page resolves to stub record %s; S6 promotion must rename the "
            "record to the page stem in the same commit [A6]" % c.relpath(record_path),
        ))
    status = record.get("status")
    if status not in ACCEPTED:
        out.append(c.make_violation(
            LINT,
            path,
            1,
            c.HIGH,
            "case page record %s has status=%r; publish gate accepts only "
            "verified, under_review, slip_opinion, verified_off_cl, or "
            "verified_identity [R12/A16/P4-18]"
            % (c.relpath(record_path), status),
        ))
    return out


def run(paths=None):
    records, out = load_records()
    for path in c.iter_markdown_files(paths or [os.path.join("content", "cases")]):
        out.extend(check_page(path, records))
    return out


def self_test():
    fixdir = os.path.join(c.HERE, "fixtures")
    pages = sorted(glob.glob(os.path.join(fixdir, "lint-14-page-*.md")))
    if not pages:
        sys.stderr.write("[self-test] FAIL: no lint-14-page-*.md fixtures\n")
        return 1
    records = {
        "lint-14-page-pass": ("fixtures/lint-14-pass.json", {"record_id": "lint-14-page-pass", "status": "verified_off_cl", "stub": False}),
        "lint-14-page-fail": ("fixtures/lint-14-bad.json", {"record_id": "lint-14-page-fail", "status": "not_found", "stub": False}),
        # CR-12: a valid record at the emptyid page's STEM, so before the fix the
        # empty record_id masked to this (clean) record; after the fix the empty
        # override is flagged instead of silently resolving here.
        "lint-14-page-emptyid-fail": ("fixtures/lint-14-emptyid.json", {"record_id": "lint-14-page-emptyid-fail", "status": "verified", "stub": False}),
        # RULING P4-18(ii): a page-backed record at status=verified_identity is
        # publish-eligible (the P4-14 fieldI reader banner carries reader safety).
        "lint-14-page-vident-pass": ("fixtures/lint-14-vident.json", {"record_id": "lint-14-page-vident-pass", "status": "verified_identity", "stub": False}),
        "lint-14-page-slip-opinion-pass": ("fixtures/lint-14-slip-opinion.json", {"record_id": "lint-14-page-slip-opinion-pass", "status": "slip_opinion", "stub": False}),
    }
    ok = True
    with tempfile.TemporaryDirectory(prefix="lint14-load-records-self-test-") as tmp:
        with open(os.path.join(tmp, "bad.json"), "w", encoding="utf-8") as f:
            f.write("{not json")
        with open(os.path.join(tmp, "one.json"), "w", encoding="utf-8") as f:
            json.dump({"record_id": "dup-case", "status": "verified", "stub": False}, f)
        with open(os.path.join(tmp, "two.json"), "w", encoding="utf-8") as f:
            json.dump({"record_id": "dup-case", "status": "verified", "stub": False}, f)
        loaded, load_violations = load_records(tmp)
        load_records_ok = (
            set(loaded) == {"dup-case"}
            and len(load_violations) == 2
            and all(v["severity"] == c.HIGH for v in load_violations)
        )
    ok = ok and load_records_ok
    sys.stderr.write("[self-test] %-32s expect=%-4s -> %s (%d viol)\n" % (
        "load-records-failclosed", "fail", "OK" if load_records_ok else "MISMATCH", len(load_violations)))
    for path in pages:
        name = os.path.basename(path)
        expect = "pass" if name.endswith("-pass.md") else "fail" if name.endswith("-fail.md") else None
        if expect is None:
            continue
        violations = check_page(path, records)
        passed = (len(violations) == 0) if expect == "pass" else (len(violations) > 0)
        ok = ok and passed
        sys.stderr.write("[self-test] %-32s expect=%-4s -> %s (%d viol)\n" % (
            name, expect, "OK" if passed else "MISMATCH", len(violations)))
        if not passed:
            for violation in violations:
                sys.stderr.write("             %s\n" % violation["message"])
    sys.stderr.write("[self-test] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    c.cli_main(run, LINT)
