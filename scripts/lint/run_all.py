#!/usr/bin/env python3
"""
Runner for the NON-CL CSSI lints (LINT-2,3,4,5,6,7,8,9,10,12,13,14,17,18,19,20,
21,22,23,24,25,26) over content/ and the S3 repo scans. Fixture self-tests for
LINT-10/12/13/14/17 run first, fail-closed. The full numeric roster LINT-1…30 is
codified at S9 (S9 R8); rows land here as their owning specs execute.

LINT-1 (CourtListener identity) is DELIBERATELY EXCLUDED here: it touches the
network and must run only through its assigned serial credential lane at the
publish gate (S1 L4'). This runner never makes a CL call.

Prints each lint's JSON-line violations (unless --quiet) and a per-lint summary
table. Exits non-zero if any lint reports a high-severity violation.

Usage:
  python3 run_all.py [glob ...]      # scope to a subset (default: all content)
  python3 run_all.py --quiet         # summary only, no per-violation JSON
  python3 run_all.py --summary-json  # emit the summary as one JSON object too
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

import lint2_quote_pinpoint as l2  # noqa: E402
import lint3_structure as l3       # noqa: E402
import lint4_lexicon as l4         # noqa: E402
import lint5_link_every_case as l5  # noqa: E402
import lint6_treatment_status as l6  # noqa: E402
import lint7_glossary as l7        # noqa: E402
import lint8_guardrails as l8      # noqa: E402
import lint9_carat_leak as l9      # noqa: E402
import lint10_emdash as l10        # noqa: E402
import lint12_drift as l12         # noqa: E402
import lint13_schema as l13        # noqa: E402
import lint14_pagerecord as l14    # noqa: E402
import lint17_coverage as l17      # noqa: E402
import lint18_depth as l18         # noqa: E402
import lint19_overview as l19      # noqa: E402
import lint20_points as l20        # noqa: E402
import lint21_binding as l21       # noqa: E402
import lint22_derip as l22         # noqa: E402
import lint23_order_weight as l23  # noqa: E402
import lint24_urls as l24          # noqa: E402
import lint25_deck as l25          # noqa: E402
import lint26_goodlaw_target as l26  # noqa: E402

# LINT-24 (URL resolution) reads the CURRENT BUILD OUTPUT (public/). Unlike
# LINT-1 (network CL identity, serial-gate-only), it is CI-SAFE to register here:
# it self-guards — if public/ is absent/stale (no public/index.html) it emits ONE
# MEDIUM and skips (exit 0, never a false HIGH), so it runs cleanly in CI right
# after the `npx quartz build` step. The remaining S3 lints are pure repo scans.
LINTS = [
    ("LINT-2", "quote/pinpoint (L1)", l2.run),
    ("LINT-3", "structure / no-SCOTUS-in-recent-dev (N5/N8)", l3.run),
    ("LINT-4", "authority lexicon (N2)", l4.run),
    ("LINT-5", "link-every-case + wikilink resolution (N7)", l5.run),
    ("LINT-6", "treatment-status presence (N13)", l6.run),
    ("LINT-7", "glossary wiring (N11, auto half)", l7.run),
    ("LINT-8", "guardrails (D6)", l8.run),
    ("LINT-9", "carat-leak (mid-line ^block anchors) (R13)", l9.run),
    ("LINT-10", "em-dash budget (R8/A7/A8)", l10.run),
    ("LINT-12", "S2 lake/frontmatter drift (R12/A13)", l12.run),
    ("LINT-13", "S2 authority-record schema (R1/A5/A16)", l13.run),
    ("LINT-14", "S2 case page-to-record gate (R12/A16)", l14.run),
    ("LINT-17", "S6 coverage: prose caption->page|ledger (R12, fail-closed)", l17.run),
    ("LINT-18", "S3 depth cap (R1/R10, fail-closed)", l18.run),
    ("LINT-19", "S3 overview: body + no case table (R2)", l19.run),
    ("LINT-20", "S3 point registry (R4, fail-closed)", l20.run),
    ("LINT-21", "S3 point->node binding (R5, fail-closed)", l21.run),
    ("LINT-22", "S3 de-rip naming (R9)", l22.run),
    ("LINT-23", "S3 order/weight (R10/A8c)", l23.run),
    ("LINT-24", "S3 url stability (R13/A1, build-guarded)", l24.run),
    ("LINT-25", "S3 deck-stem preservation (R14/A2, fail-closed)", l25.run),
    ("LINT-26", "good-law target resolves (S4 R5, fail-closed)", l26.run),
]

SELF_TESTS = [
    ("LINT-10", "LINT-10 self-test gate (S1 A3, fail-closed)", l10.self_test, l10.FIXTURE),
    ("LINT-12", "LINT-12 self-test gate (S2 R12/A13, fail-closed)", l12.self_test, os.path.join(c.HERE, "fixtures")),
    ("LINT-13", "LINT-13 self-test gate (S2 schema, fail-closed)", l13.self_test, os.path.join(c.HERE, "fixtures")),
    ("LINT-14", "LINT-14 self-test gate (S2 R12/A16, fail-closed)", l14.self_test, os.path.join(c.HERE, "fixtures")),
    ("LINT-17", "LINT-17 self-test gate (S6 R11/R12, fail-closed)", l17.self_test, os.path.join(c.HERE, "fixtures")),
]


def main():
    args = sys.argv[1:]
    quiet = "--quiet" in args
    summary_json = "--summary-json" in args
    paths = [a for a in args if not a.startswith("-")] or None

    rows = []
    total_high = 0

    # Fail-closed self-test gate: these self-tests must pass BEFORE we trust
    # the corpus scan. A broken lint must never green-light a publish, so a
    # self-test failure becomes a synthetic HIGH violation and forces a nonzero
    # exit. self_test() prints its own [self-test] diagnostics to stderr.
    for lint_name, desc, test_fn, source_path in SELF_TESTS:
        selftest_viols = []
        if test_fn() != 0:
            selftest_viols.append(c.make_violation(
                lint_name, source_path, 1, c.HIGH,
                "%s self-test FAILED; refusing to certify the corpus scan "
                "(fail-closed)" % lint_name))
        if not quiet:
            c.emit(selftest_viols)
        st_high = sum(1 for v in selftest_viols if v["severity"] == c.HIGH)
        total_high += st_high
        # CR-05: carry the real per-lint name (not a hardcoded "SELFTEST"), so a
        # batch-close roster/summary can tell WHICH self-test failed.
        rows.append((lint_name, desc, len(selftest_viols), st_high, 0, 0))

    for name, desc, run_fn in LINTS:
        violations = run_fn(paths)
        if not quiet:
            c.emit(violations)
        n_high = sum(1 for v in violations if v["severity"] == c.HIGH)
        n_med = sum(1 for v in violations if v["severity"] == c.MEDIUM)
        n_low = sum(1 for v in violations if v["severity"] == c.LOW)
        total_high += n_high
        rows.append((name, desc, len(violations), n_high, n_med, n_low))

    out = sys.stderr
    out.write("\n" + "=" * 78 + "\n")
    out.write("CSSI LINT roster — non-CL dry run (LINT-1 excluded; serial CL "
              "gate only)\n")
    out.write("=" * 78 + "\n")
    out.write("%-8s %-44s %6s %5s %5s %5s\n" %
              ("LINT", "checks", "total", "high", "med", "low"))
    out.write("-" * 78 + "\n")
    for name, desc, total, h, m, lo in rows:
        out.write("%-8s %-44s %6d %5d %5d %5d\n" %
                  (name, desc[:44], total, h, m, lo))
    out.write("-" * 78 + "\n")
    out.write("%-8s %-44s %6d %5d %5d %5d\n" % (
        "TOTAL", "", sum(r[2] for r in rows), sum(r[3] for r in rows),
        sum(r[4] for r in rows), sum(r[5] for r in rows)))
    out.write("=" * 78 + "\n")

    if summary_json:
        import json
        c.emit([])  # no-op spacer
        sys.stdout.write(json.dumps({
            "summary": [
                {"lint": n, "total": t, "high": h, "medium": m, "low": lo}
                for (n, _d, t, h, m, lo) in rows
            ]
        }, ensure_ascii=False) + "\n")

    sys.exit(1 if total_high else 0)


if __name__ == "__main__":
    main()
