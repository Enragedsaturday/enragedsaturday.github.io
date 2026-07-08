#!/usr/bin/env python3
"""
LINT-21 — point -> S3-node binding map.  S3 · R5 (alias LINT-S3-binding; S9 R8
roster row 21).  FAIL-CLOSED.

Validates `_overhaul2/points/s2-binding.yaml` — the map that resolves S2's
provisional `treatment.point_overrides[].point` slugs to one or more
`registry.yaml` node ids (1:N / N:1 allowed). Checks:

  (0) the file EXISTS. Missing => HIGH, fail-closed.
  (a) every `point_overrides[].point` slug PRESENT in the lake
      (`_overhaul2/lake/cases/*.json`) resolves to >= 1 registry node id via the
      map. A slug carried by a case whose `cluster_id` matches a `pending[]` row
      (the points-README `pending_slug` convention) counts as bound-PENDING and
      is reported LOW, never HIGH (a pending row is a promise, not a live edge).
      A lake slug matching neither a `bound[]` row nor a pending case => HIGH.
  (b) every node id referenced anywhere in the map (bound[] + pending[]) EXISTS
      in the registry — a dangling node id => HIGH.

Belton's worked binding: `search.vehicle.sia-recent-occupant` (New York v.
Belton, cluster 110559) -> the SIA-Vehicles node, superseded_by Gant (145887).

Parsing is stdlib-only via `_common.parse_yaml_subset`.

Not a content scan: the `paths` scoping arg is accepted and ignored.

SELF-TEST (S1 A3): `python3 lint21_binding.py --self-test` over the
`fixtures/lint-21-*` fixtures (a fixture registry, binding maps, and fixture
lakes) plus a missing-file case.

Usage:
  python3 lint21_binding.py
  python3 lint21_binding.py --self-test
"""

import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-21"

REGISTRY_REL = os.path.join("_overhaul2", "points", "registry.yaml")
BINDING_REL = os.path.join("_overhaul2", "points", "s2-binding.yaml")
LAKE_CASES_REL = os.path.join("_overhaul2", "lake", "cases")

# a slug-shaped string (dotted kebab) — distinguishes a point slug from a case
# name (which carries " v. " and spaces). Used to pick up slug-valued
# composite_basis_ref alongside the primary point_overrides[].point scan.
SLUG_SHAPE_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*(?:\.[a-z0-9]+(?:-[a-z0-9]+)*)+$")


def load_registry_ids(registry_path):
    if not os.path.isfile(registry_path):
        return set()
    doc = c.parse_yaml_subset(c.read_text(registry_path).split("\n"))
    nodes = doc.get("nodes")
    if not isinstance(nodes, list):
        return set()
    return {n.get("id") for n in nodes
            if isinstance(n, dict) and isinstance(n.get("id"), str)}


def collect_lake_overrides(lake_dir):
    """Scan the lake for point-override slugs actually present now. Returns
    (overrides, unreadable): overrides is a list of (slug, cluster_id,
    source_file); unreadable is the list of case files that failed to parse.
    Primary source is treatment.point_overrides[].point; a slug-shaped
    treatment.composite_basis_ref is also collected (the binding map registers
    composite_basis_ref rows).

    A corrupt/unreadable case file is NOT silently dropped (that would let an
    unbound override slug in a broken record vanish from the scan) — it is
    returned in `unreadable` so the caller can surface it as a HIGH, fail-closed
    per this lint's mandate."""
    out = []
    unreadable = []
    for f in sorted(glob.glob(os.path.join(lake_dir, "*.json"))):
        try:
            with open(f, encoding="utf-8") as fh:
                d = json.load(fh)
        except (OSError, ValueError):
            unreadable.append(f)
            continue
        if not isinstance(d, dict):
            continue
        t = d.get("treatment")
        if not isinstance(t, dict):
            continue
        cluster = _cluster_id(d)
        pos = t.get("point_overrides")
        if isinstance(pos, list):
            for ov in pos:
                if isinstance(ov, dict):
                    slug = ov.get("point")
                    if isinstance(slug, str) and slug.strip():
                        out.append((slug.strip(), cluster, f))
        cbr = t.get("composite_basis_ref")
        if isinstance(cbr, str) and SLUG_SHAPE_RE.match(cbr.strip()):
            out.append((cbr.strip(), cluster, f))
    return out, unreadable


def _cluster_id(case_dict):
    """Best-effort cluster id from a lake case record (used to match pending
    rows). The lake keys vary; we probe the common locations."""
    for key in ("cluster_id",):
        v = case_dict.get(key)
        if v is not None:
            return str(v)
    ident = case_dict.get("identity")
    if isinstance(ident, dict):
        for key in ("cluster_id", "opinion_id"):
            v = ident.get(key)
            if v is not None:
                return str(v)
    cites = case_dict.get("citations")
    if isinstance(cites, dict):
        v = cites.get("cluster_id")
        if v is not None:
            return str(v)
    return None


def check_binding(binding_path, registry_ids, lake_overrides):
    """Validate one binding map against a registry-id set and the live lake
    override list. Returns a list of violations (fail-closed)."""
    if not os.path.isfile(binding_path):
        return [c.make_violation(
            LINT, binding_path, 1, c.HIGH,
            "binding map missing: %s not found — the point->node binding map is a "
            "required S3 R5 deliverable (fail-closed) [R5]"
            % c.relpath(binding_path))]

    doc = c.parse_yaml_subset(c.read_text(binding_path).split("\n"))
    # CR-10: a malformed binding file must NOT be normalized away — bound/pending
    # must both be lists, or the whole map fails closed (else a broken file
    # silently disappears from both the live-slug and dangling-node checks).
    if not isinstance(doc.get("bound"), list) or not isinstance(doc.get("pending"), list):
        return [c.make_violation(
            LINT, binding_path, 1, c.HIGH,
            "binding map has invalid bound/pending structure — both must be lists "
            "(fail-closed) [R5]")]
    bound = doc["bound"]
    pending = doc["pending"]

    out = []

    def _collect_nodes(row, section):
        """Nodes for one binding row. CR-10: a non-string node id (or a non-list
        `nodes`) is REJECTED as a HIGH, never silently skipped."""
        raw = row.get("nodes")
        if raw is None:
            return []
        if not isinstance(raw, list):
            out.append(c.make_violation(
                LINT, binding_path, 1, c.HIGH,
                "%s row `nodes` is not a list [R5]" % section))
            return []
        good = []
        for n in raw:
            if isinstance(n, str):
                good.append(n)
            else:
                out.append(c.make_violation(
                    LINT, binding_path, 1, c.HIGH,
                    "%s row has a non-string node id %r [R5]" % (section, n)))
        return good

    # bound slug -> nodes
    slug_map = {}
    mapped_nodes = set()
    for r in bound:
        if not isinstance(r, dict):
            out.append(c.make_violation(
                LINT, binding_path, 1, c.HIGH, "bound[] entry is not a mapping [R5]"))
            continue
        slug = r.get("s2_point")
        nodes = _collect_nodes(r, "bound")
        if isinstance(slug, str) and slug.strip():
            slug_map.setdefault(slug.strip(), []).extend(nodes)
        mapped_nodes.update(nodes)

    # pending case (by cluster_id) -> nodes
    pending_by_cluster = {}
    for r in pending:
        if not isinstance(r, dict):
            out.append(c.make_violation(
                LINT, binding_path, 1, c.HIGH, "pending[] entry is not a mapping [R5]"))
            continue
        nodes = _collect_nodes(r, "pending")
        cl = r.get("cluster_id")
        if cl is not None:
            pending_by_cluster[str(cl)] = nodes
        mapped_nodes.update(nodes)

    # (b) every mapped node id exists in the registry
    for nid in sorted(mapped_nodes):
        if nid not in registry_ids:
            out.append(c.make_violation(
                LINT, binding_path, 1, c.HIGH,
                "dangling node id %r in the binding map — no such node in "
                "registry.yaml [R5]" % nid))

    # (a) every live lake override slug resolves (bound) or is bound-pending (LOW)
    for slug, cluster, src in lake_overrides:
        if slug_map.get(slug):
            # bound live to >= 1 node (its nodes were dangling-checked above). A
            # bound[] row with missing/empty `nodes` registers an EMPTY list here
            # and must NOT count as bound — the invariant is "resolves to >= 1
            # registry node id" (contract (a)), so it falls through to HIGH.
            continue
        if cluster is not None and cluster in pending_by_cluster:
            out.append(c.make_violation(
                LINT, src, 1, c.LOW,
                "override slug %r (cluster %s) is bound-PENDING — matched a "
                "pending[] row by cluster; expected nodes %s [R5]"
                % (slug, cluster, pending_by_cluster[cluster])))
            continue
        out.append(c.make_violation(
            LINT, src, 1, c.HIGH,
            "unbound override slug %r (cluster %s) — present in the lake but "
            "resolves to no registry node via the binding map (fail-closed) [R5]"
            % (slug, cluster)))
    return out


def run(paths=None):  # noqa: ARG001 (roster signature; scoping arg ignored)
    registry_ids = load_registry_ids(os.path.join(c.REPO_ROOT, REGISTRY_REL))
    lake_overrides, unreadable = collect_lake_overrides(
        os.path.join(c.REPO_ROOT, LAKE_CASES_REL))
    out = [c.make_violation(
        LINT, f, 1, c.HIGH,
        "unreadable/corrupt lake case file %s — cannot scan it for point-override "
        "slugs; an unbound override hidden in a broken record would vanish from "
        "the check (fail-closed) [R5]" % c.relpath(f)) for f in unreadable]
    out.extend(check_binding(os.path.join(c.REPO_ROOT, BINDING_REL),
                             registry_ids, lake_overrides))
    return out


# --------------------------------------------------------------------------
# self-test — fixture registry + binding maps + fixture lakes
# --------------------------------------------------------------------------

def self_test():
    fixdir = os.path.join(c.HERE, "fixtures")
    reg = os.path.join(fixdir, "lint-21-registry.yaml")
    b_pass = os.path.join(fixdir, "lint-21-binding-pass.yaml")
    b_dangle = os.path.join(fixdir, "lint-21-binding-dangling-fail.yaml")
    b_emptynodes = os.path.join(fixdir, "lint-21-binding-emptynodes-fail.yaml")
    b_badstruct = os.path.join(fixdir, "lint-21-binding-badstruct-fail.yaml")
    b_nonstr = os.path.join(fixdir, "lint-21-binding-nonstring-node-fail.yaml")
    lake_bound = os.path.join(fixdir, "lint-21-lake-bound")
    lake_pending = os.path.join(fixdir, "lint-21-lake-pending")
    lake_unbound = os.path.join(fixdir, "lint-21-lake-unbound")
    lake_corrupt = os.path.join(fixdir, "lint-21-lake-corrupt")
    for req in (reg, b_pass, b_dangle, b_emptynodes, b_badstruct, b_nonstr):
        if not os.path.isfile(req):
            sys.stderr.write("[self-test] FAIL: missing fixture %s\n" % req)
            return 1

    reg_ids = load_registry_ids(reg)
    ok = True

    def case(desc, binding, lake_dir, expect):
        nonlocal ok
        ovr = collect_lake_overrides(lake_dir)[0] if lake_dir else []
        viols = check_binding(binding, reg_ids, ovr)
        n_high = sum(1 for v in viols if v["severity"] == c.HIGH)
        n_low = sum(1 for v in viols if v["severity"] == c.LOW)
        if expect == "pass":
            passed = n_high == 0 and n_low == 0
        elif expect == "low":
            passed = n_high == 0 and n_low >= 1
        else:  # "high"
            passed = n_high >= 1
        ok = ok and passed
        sys.stderr.write("[self-test] %-34s expect=%-4s -> %s (%d high, %d low)\n" % (
            desc, expect, "OK" if passed else "MISMATCH", n_high, n_low))
        if not passed:
            for v in viols:
                sys.stderr.write("             [%s] %s\n" % (v["severity"], v["message"]))

    # missing binding file -> HIGH
    mv = check_binding(os.path.join(fixdir, "lint-21-nope.yaml"), reg_ids, [])
    passed = len(mv) == 1 and mv[0]["severity"] == c.HIGH
    ok = ok and passed
    sys.stderr.write("[self-test] %-34s expect=high -> %s (%d viol)\n" % (
        "missing binding map", "OK" if passed else "MISMATCH", len(mv)))

    case("bound slug resolves", b_pass, lake_bound, "pass")
    case("pending slug (cluster match)", b_pass, lake_pending, "low")
    case("unbound lake slug", b_pass, lake_unbound, "high")
    case("dangling node id", b_dangle, lake_bound, "high")
    # CONFIRMED critical #1: a bound[] row with EMPTY nodes must NOT satisfy the
    # override check — the live lake slug it names resolves to zero nodes -> HIGH.
    case("empty-nodes bound row (bypass)", b_emptynodes, lake_bound, "high")

    # CR-10: a malformed binding structure (bound/pending not a list) is HIGH,
    # never coerced to []; a non-string node id is rejected, never silently dropped.
    # CR-S6: these two fail-closed fixtures are MANDATORY (asserted present above,
    # like reg/b_pass/b_dangle/b_emptynodes) — an optional os.path.isfile gate that
    # quietly no-ops is the self-test analogue of silent-success-on-missing-input.
    case("malformed bound/pending struct", b_badstruct, lake_bound, "high")
    case("non-string node id", b_nonstr, lake_bound, "high")

    # CONFIRMED critical #2: a corrupt/unreadable lake case file is surfaced as a
    # HIGH, never silently skipped (fail-closed).
    corrupt_ovr, corrupt_unread = collect_lake_overrides(lake_corrupt)
    passed = len(corrupt_unread) >= 1 and corrupt_ovr == []
    ok = ok and passed
    sys.stderr.write("[self-test] %-34s expect=1-unread -> %s (%d unreadable)\n" % (
        "corrupt lake case file", "OK" if passed else "MISMATCH", len(corrupt_unread)))

    sys.stderr.write("[self-test] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    c.cli_main(run, LINT)
