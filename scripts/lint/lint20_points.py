#!/usr/bin/env python3
"""
LINT-20 — point-of-law registry.  S3 · R4 (alias LINT-S3-points; S9 R8 roster
row 20).  FAIL-CLOSED.

Validates `_overhaul2/points/registry.yaml` — the controlled list of points of
law (atomic legal propositions finer than a page). Checks (all HIGH):

  (0) the file EXISTS. Missing => HIGH, fail-closed (the registry is a required
      S3 deliverable; its absence must block, never silently pass).
  (1) every node carries the R4 core schema: `id`, `label`, a `statement` KEY
      (value may be '' for a placed-empty node, R7), `home_page`, and
      `status` in {draft, verified}.
  (2) `id` grammar: kebab `area.object.point` — 2+ dot-separated segments, each
      segment lowercase [a-z0-9] with internal hyphens (e.g. `proof.probable-cause`,
      `search.home.exigency.emergency-aid`).
  (3) ids are UNIQUE across the registry.
  (4) every `home_page` and every `also_on[]` entry resolves to a file on disk.

Parsing is stdlib-only via `_common.parse_yaml_subset` (the block-YAML subset
the roster already relies on; verified against the real registry.yaml).

Not a content scan: the `paths` scoping arg is accepted and ignored.

SELF-TEST (S1 A3): `python3 lint20_points.py --self-test` over the labeled
`fixtures/lint-20-registry-*.yaml` fixtures plus a missing-file case.

Usage:
  python3 lint20_points.py
  python3 lint20_points.py --self-test
"""

import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-20"

REGISTRY_REL = os.path.join("_overhaul2", "points", "registry.yaml")

STATUS_ENUM = {"draft", "verified"}
# kebab area.object.point — >= 2 dotted segments, each [a-z0-9] with inner hyphens
ID_GRAMMAR_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*(?:\.[a-z0-9]+(?:-[a-z0-9]+)*)+$")


def _resolve_on_disk(rel_or_abs):
    """A registry home_page/also_on path resolves iff the file exists on disk.
    Paths are repo-relative (content/...); resolved against REPO_ROOT."""
    p = rel_or_abs
    if not os.path.isabs(p):
        p = os.path.join(c.REPO_ROOT, rel_or_abs)
    return os.path.isfile(p)


def check_registry(registry_path):
    """Validate one registry.yaml. Returns a list of violations (fail-closed)."""
    if not os.path.isfile(registry_path):
        return [c.make_violation(
            LINT, registry_path, 1, c.HIGH,
            "registry missing: %s not found — the point-of-law registry is a "
            "required S3 R4 deliverable (fail-closed) [R4]"
            % c.relpath(registry_path))]

    text = c.read_text(registry_path)
    doc = c.parse_yaml_subset(text.split("\n"))
    nodes = doc.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        return [c.make_violation(
            LINT, registry_path, 1, c.HIGH,
            "registry has no `nodes:` list (or it is empty) — cannot validate any "
            "point of law (fail-closed) [R4]")]

    out = []
    seen_ids = {}
    for idx, node in enumerate(nodes, start=1):
        if not isinstance(node, dict):
            out.append(c.make_violation(
                LINT, registry_path, 1, c.HIGH,
                "registry node #%d is not a mapping — expected "
                "{id,label,statement,home_page,also_on,status} [R4]" % idx))
            continue
        nid = node.get("id")
        label = node.get("label")
        home = node.get("home_page")
        status = node.get("status")
        where = "node %r" % (nid if nid else "#%d" % idx)

        # (1) required core fields present + status enum
        if not (isinstance(nid, str) and nid.strip()):
            out.append(c.make_violation(
                LINT, registry_path, 1, c.HIGH,
                "%s: missing/empty `id` [R4]" % where))
        if not (isinstance(label, str) and label.strip()):
            out.append(c.make_violation(
                LINT, registry_path, 1, c.HIGH,
                "%s: missing/empty `label` [R4]" % where))
        if "statement" not in node:
            out.append(c.make_violation(
                LINT, registry_path, 1, c.HIGH,
                "%s: missing `statement` key (value may be '' for a placed-empty "
                "node, but the key is required) [R4/R7]" % where))
        if not (isinstance(home, str) and home.strip()):
            out.append(c.make_violation(
                LINT, registry_path, 1, c.HIGH,
                "%s: missing/empty `home_page` [R4]" % where))
        if str(status).strip() not in STATUS_ENUM:
            out.append(c.make_violation(
                LINT, registry_path, 1, c.HIGH,
                "%s: status=%r not in {draft, verified} [R4]" % (where, status)))

        # (2) id grammar
        if isinstance(nid, str) and nid.strip() and not ID_GRAMMAR_RE.match(nid):
            out.append(c.make_violation(
                LINT, registry_path, 1, c.HIGH,
                "%s: id %r is not kebab `area.object.point` (>= 2 dotted "
                "lowercase segments) [R4]" % (where, nid)))

        # (3) unique ids
        if isinstance(nid, str) and nid.strip():
            if nid in seen_ids:
                out.append(c.make_violation(
                    LINT, registry_path, 1, c.HIGH,
                    "duplicate id %r (also on node #%d) — ids are unique [R4]"
                    % (nid, seen_ids[nid])))
            else:
                seen_ids[nid] = idx

        # (4) home_page + also_on resolve on disk
        if isinstance(home, str) and home.strip() and not _resolve_on_disk(home):
            out.append(c.make_violation(
                LINT, registry_path, 1, c.HIGH,
                "%s: home_page %r does not resolve on disk [R4]" % (where, home)))
        also = node.get("also_on")
        if also is not None and not isinstance(also, list):
            # malformed shape (e.g. a bare string) — do NOT silently skip
            # validation; a non-list also_on is fail-closed HIGH [R4].
            out.append(c.make_violation(
                LINT, registry_path, 1, c.HIGH,
                "%s: also_on must be a YAML list of content paths, got %r [R4]"
                % (where, also)))
        elif isinstance(also, list):
            for ao in also:
                if not (isinstance(ao, str) and ao.strip()):
                    out.append(c.make_violation(
                        LINT, registry_path, 1, c.HIGH,
                        "%s: also_on entry %r is not a non-empty string [R4]"
                        % (where, ao)))
                elif not _resolve_on_disk(ao):
                    out.append(c.make_violation(
                        LINT, registry_path, 1, c.HIGH,
                        "%s: also_on entry %r does not resolve on disk [R4]"
                        % (where, ao)))
    return out


def run(paths=None):  # noqa: ARG001 (roster signature; scoping arg ignored)
    return check_registry(os.path.join(c.REPO_ROOT, REGISTRY_REL))


# --------------------------------------------------------------------------
# self-test — labeled registry fixtures + a missing-file case
# --------------------------------------------------------------------------

def self_test():
    fixdir = os.path.join(c.HERE, "fixtures")
    files = sorted(glob.glob(os.path.join(fixdir, "lint-20-registry-*.yaml")))
    ok = True

    # missing-file fail-closed case
    missing = os.path.join(fixdir, "lint-20-does-not-exist.yaml")
    mv = check_registry(missing)
    passed = len(mv) == 1 and mv[0]["severity"] == c.HIGH
    ok = ok and passed
    sys.stderr.write("[self-test] %-34s expect=high -> %s (%d viol)\n" % (
        "missing registry", "OK" if passed else "MISMATCH", len(mv)))

    if not files:
        sys.stderr.write("[self-test] FAIL: no lint-20-registry-*.yaml fixtures\n")
        return 1
    for f in files:
        name = os.path.basename(f)
        expect = "pass" if name.endswith("-pass.yaml") else \
                 "fail" if name.endswith("-fail.yaml") else None
        if expect is None:
            continue
        viols = check_registry(f)
        passed = (len(viols) == 0) if expect == "pass" else (len(viols) > 0)
        ok = ok and passed
        sys.stderr.write("[self-test] %-34s expect=%-4s -> %s (%d viol)\n" % (
            name, expect, "OK" if passed else "MISMATCH", len(viols)))
        if not passed:
            for v in viols:
                sys.stderr.write("             %s\n" % v["message"])
    sys.stderr.write("[self-test] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    c.cli_main(run, LINT)
