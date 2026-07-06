#!/usr/bin/env python3
"""
LINT-12 - S2 lake/frontmatter drift (alias LINT-S2-drift). Fail-closed.

Compares case-page managed frontmatter against the S2 lake projection by parsed
value, using scripts/s2/serializer.py and scripts/s2/project.py. Draft pages are
exempt. Legacy treatment migration is gated by S2 A13 before any comparison.
"""

import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

REPO_ROOT = c.REPO_ROOT
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from scripts.s2 import project as s2_project  # noqa: E402
from scripts.s2 import serializer  # noqa: E402

LINT = "LINT-12"


def _record_path(record_id):
    return os.path.join(c.REPO_ROOT, "_overhaul2", "lake", "cases", "%s.json" % record_id)


def _project_command(path):
    return "python3 scripts/s2/project.py --write %s" % c.relpath(path)


def check_page(path, record, record_path):
    text = serializer.read_markdown(path)
    fm, _body, _start = serializer.split_frontmatter(text)
    actual = serializer.managed_subset(fm)
    expected = s2_project.project_record(record)
    diffs = serializer.diff_paths(actual, expected)
    if not diffs:
        return []
    shown = ", ".join(diffs[:12])
    if len(diffs) > 12:
        shown += ", ..."
    return [c.make_violation(
        LINT,
        path,
        1,
        c.HIGH,
        "S2 managed frontmatter drift in %s; differing fields: %s. Edit the "
        "lake record, not frontmatter: %s. Re-project with: %s"
        % (c.relpath(path), shown, c.relpath(record_path), _project_command(path)),
    )]


def run(paths=None):
    out = []
    gate = s2_project.a13_gate(paths)
    for path, value in gate["unmapped"]:
        out.append(c.make_violation(
            LINT,
            path,
            1,
            c.HIGH,
            "A13 pre-projection gate failed: legacy treatment.status=%r has no "
            "mapping in _overhaul2/lake/_treatment-migration.json; projector "
            "refuses to overwrite managed treatment until mapped" % value,
        ))
    for path in gate["review"]:
        out.append(c.make_violation(
            LINT,
            path,
            1,
            c.HIGH,
            "A13 REVIEW page staged for S9: projector will not overwrite managed "
            "treatment until adjudicated",
        ))
    if out:
        return out

    records, record_paths = s2_project.load_records()
    for path in s2_project.case_page_paths(paths):
        text = serializer.read_markdown(path)
        fm, _body, _start = serializer.split_frontmatter(text)
        if fm.get("type") != "case" or serializer.is_draft_page(fm):
            continue
        lake = fm.get("lake") if isinstance(fm.get("lake"), dict) else {}
        rid = lake.get("record_id") or os.path.splitext(os.path.basename(path))[0]
        record = records.get(rid)
        if not record:
            out.append(c.make_violation(
                LINT,
                path,
                1,
                c.HIGH,
                "S2 drift check cannot resolve lake record %r; create/fix "
                "_overhaul2/lake/cases/%s.json before projection"
                % (rid, rid),
            ))
            continue
        out.extend(check_page(path, record, record_paths[rid]))
    return out


def self_test():
    fixdir = os.path.join(c.HERE, "fixtures")
    record_path = os.path.join(fixdir, "lint-12-record.json")
    record = json.load(open(record_path, encoding="utf-8"))
    files = sorted(glob.glob(os.path.join(fixdir, "lint-12-drift-*.md")))
    if not files:
        sys.stderr.write("[self-test] FAIL: no lint-12-drift-*.md fixtures\n")
        return 1
    ok = True
    for path in files:
        name = os.path.basename(path)
        expect = "pass" if name.endswith("-pass.md") else "fail" if name.endswith("-fail.md") else None
        if expect is None:
            continue
        violations = check_page(path, record, record_path)
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
