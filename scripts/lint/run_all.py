#!/usr/bin/env python3
"""
Runner for the NON-CL CSSI lints (LINT-2,3,4,5,6,7,8,9,10,12,13,14,17,18,19,20,
21,22,23,24,25,26,27,28,29,30) over content/, the S3 repo scans, and the S9 ledger.
Fixture self-tests for LINT-3,5,7,8,10,12,13,14,17,27,28,29,30 run first, fail-closed.
The full numeric roster LINT-1…30 is codified at S9 (S9 R8).

LINT-1 (CourtListener identity) is DELIBERATELY EXCLUDED here: it touches the
network and must run only through its assigned serial credential lane at the
publish gate (S1 L4'). This runner never makes a CL call.

LINT-15 (skeleton) / LINT-16 (case-tables) remain STANDALONE (batch-1 rule C, kept
by S9 R8's wiring): they scan repo structure the way the S3/S5 tooling drives them,
not the content sweep, and the S8-close baseline (TOTAL 4176 / HIGH 3381) was
measured with them out of this runner (LINT-16 carries a 622-HIGH standalone
backlog). They run via their own self_test/standalone invocation. S9 R8's "run_all
runs 2–30" is honored for the content/data/ledger rows; 15/16's runner placement
is left to the orchestrator (they stay standalone here to preserve the baseline).

S9 R8 rebuilds folded in here: LINT-3 rebuilt lake-driven — the O1 token-window N5
heuristic is DEAD; N5 is now section-scoped against the S2 lake court field, plus
the S1 A9 >3-cases-per-paragraph sub-check (F-DEMO-001 acceptance fixture
lint-3-n5.md). LINT-8 gains TEACH-11 (mnemonic/maxim wikilink-target + register
wording). LINT-30 is the R4 ledger-reconciliation invariant script (bootstrap-aware:
NO-ROWS-YET green until the ledger fills, fail-closed after).

S8 R13 additions: LINT-5 (ledger-aware bare-caption + broken-anchor HIGH + embed
full-slug) and LINT-7 (register coverage + dead-anchor HIGH; old first-occurrence
rule DELETED) are rewritten; LINT-27 (table pipes, R11), LINT-28 (fragment
well-formedness, R13d) and LINT-29 (shingle boundary, R9) are new.

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
import lint27_table_pipes as l27    # noqa: E402
import lint28_fragments as l28      # noqa: E402
import lint29_shingle_boundary as l29  # noqa: E402

# LINT-30 (the R4 ledger reconciliation invariants) lives under scripts/s9/.
sys.path.insert(0, os.path.join(os.path.dirname(c.HERE), "s9"))
import check_ledger as l30          # noqa: E402

# LINT-24 (URL resolution) reads the CURRENT BUILD OUTPUT (public/). Unlike
# LINT-1 (network CL identity, serial-gate-only), it is CI-SAFE to register here:
# it self-guards — if public/ is absent/stale (no public/index.html) it emits ONE
# MEDIUM and skips (exit 0, never a false HIGH), so it runs cleanly in CI right
# after the `npx quartz build` step. The remaining S3 lints are pure repo scans.
LINTS = [
    ("LINT-2", "quote/pinpoint (L1)", l2.run),
    ("LINT-3", "structure + N5 lake-driven + A9 case-wall (N5/N8/A9)", l3.run),
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
    ("LINT-27", "table pipe-escaping (S8 R11/NUM-02)", l27.run),
    ("LINT-28", "external text-fragment well-formedness (S8 R13d)", l28.run),
    ("LINT-29", "R9 transclusion/shingle boundary (S8 R9)", l29.run),
    ("LINT-30", "R4 ledger reconciliation invariants (S9 R4, bootstrap-aware)", l30.run),
]

SELF_TESTS = [
    ("LINT-3", "LINT-3 self-test gate (N5 lake-driven + A9, fail-closed)", l3.self_test, l3.FIXTURE),
    ("LINT-5", "LINT-5 self-test gate (S8 R13a, fail-closed)", l5.self_test, l5.FIXTURE),
    ("LINT-8", "LINT-8 self-test gate (TEACH-11 target+wording, fail-closed)", l8.self_test, l8.FIXTURE),
    ("LINT-7", "LINT-7 self-test gate (S8 R13b, fail-closed)", l7.self_test, l7.FIXTURE),
    ("LINT-10", "LINT-10 self-test gate (S1 A3, fail-closed)", l10.self_test, l10.FIXTURE),
    ("LINT-12", "LINT-12 self-test gate (S2 R12/A13, fail-closed)", l12.self_test, os.path.join(c.HERE, "fixtures")),
    ("LINT-13", "LINT-13 self-test gate (S2 schema, fail-closed)", l13.self_test, os.path.join(c.HERE, "fixtures")),
    ("LINT-14", "LINT-14 self-test gate (S2 R12/A16, fail-closed)", l14.self_test, os.path.join(c.HERE, "fixtures")),
    ("LINT-17", "LINT-17 self-test gate (S6 R11/R12, fail-closed)", l17.self_test, os.path.join(c.HERE, "fixtures")),
    ("LINT-27", "LINT-27 self-test gate (S8 R11, fail-closed)", l27.self_test, l27.FIXTURE),
    ("LINT-28", "LINT-28 self-test gate (S8 R13d, fail-closed)", l28.self_test, l28.FIXTURE),
    ("LINT-29", "LINT-29 self-test gate (S8 R9, fail-closed)", l29.self_test, l29.FIXTURE),
    ("LINT-30", "LINT-30 self-test gate (R4 invariants + F-DEMO-001, fail-closed)", l30.self_test, l30.DEMO_DIR),
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
