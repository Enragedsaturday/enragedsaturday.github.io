# P5-LEDGER — LINT-30 ledger tidy (RULING P5-01)

Lane `P5-LEDGER` · model `claude-opus-4-8` · 2026-07-22 · branch `overhaul2/execute`.
Authority: RULING P5-01 (P4-RULINGS.md). WRITE-SCOPE honored exactly (findings.jsonl append-only;
ledger-exceptions.jsonl new; check_ledger.py + fixtures; campaign/).

## Result

`python3 scripts/s9/check_ledger.py` -> **HIGH=0** (exit 0); was HIGH=25 at start.
Summary line: `status=CHECKED HIGH=0 resolved-escalations=22 open-escalations=0`.
`python3 scripts/s9/check_ledger.py --self-test` -> **EXIT 0**. F-DEMO-001 acceptance green.

Residual (all non-high, by design): 21 `[inv2] ... [documented exception P5-01]` MEDIUM rows —
the 21 sub-quorum paneled findings, now documented rather than gating.

## (i) Two orphan finding rows reconstructed — APPEND-ONLY to `_run/s9/findings.jsonl`

| finding_id | case | object | dim/gate/panel | assertion_id | verdict | sev |
|---|---|---|---|---|---|---|
| F-S9-PR-d1d2d45449 | Illinois v. Gates ('fluid concept', 462 U.S. 232) | content/instructor-craft-and-study/Three Golden Rules.md | D2 / G1 / existence | 441160dcc43226a9 | DISMISSED | low |
| F-S9-PR-6ffdcb45b8 | Brinegar v. United States (338 U.S. 175) | content/instructor-craft-and-study/Three Golden Rules.md | D2 / G1 / existence | 4db5f3168693da19 | DISMISSED | medium |

- **Source of truth:** the authoritative original pilot rows in `_run/s9/panel-pilot/findings.jsonl`
  (run=pilot). Their claim/object/dimension are fully consistent with what votes.jsonl + the
  adjudication rows independently attest (both DISMISSED disclosure-induced FPs; the single
  `claude-opus-panel` vote per finding, `verdict=refuted`, `semantics_normalized.from="stands"`,
  cutover `2026-07-10T01:33:09Z` — the vote-semantics cutover that dropped the sibling votes and
  left the finding rows unpersisted).
- **Provenance marking:** each reconstructed row carries top-level `provenance` =
  `"reconstructed-at-P5-tidy (vote-semantics cutover gap); source=_run/s9/panel-pilot/findings.jsonl ...; RULING P5-01(i)"`,
  `reconstructed_at_p5=true`, and an augmented `found_by.note`.
- **assertion_id safety:** both pilot assertion_ids were verified present as genuine keys in
  `assertion-inventory.json` (same object as the finding), so no new `[inv5] ... absent from the
  inventory` HIGH is introduced.
- **Effect:** the two `[inv1] adjudication references finding_id ... with no finding row` HIGHs
  cleared; findings 2329 -> **2331 == 2331 adjudications** -> `[inv5] count mismatch` row GREEN
  (2331=2331, R14.1 FP-accounting preserved).

## (ii) `_run/s9/ledger-exceptions.jsonl` (new) + inv2 amendment

- File = 1 header/design-note row (cites RULING P5-01 and the lint11-allowlist `adjudicated_hits`
  precedent, `scripts/lint/fixtures/lint11-allowlist.json`, P4-17(d)/P4-19) + **21** exception rows,
  one per sub-quorum finding id, enumerated from check_ledger's inv2 output using the exact inv2
  predicate (distinct non-`-confirm` lanes < 3). Verdict split: 19 MODIFIED + 2 DISMISSED. Row shape:
  `{finding_id, exception:"sub-quorum-adjudicated", votes_present:N, adjudication_verdict, basis:"P2 adjudication on evidence; panel era closed; RULING P5-01(ii)"}`.
- `check_ledger.load_ledger()` now reads `<dir>/ledger-exceptions.jsonl` into
  `data["ledger_exceptions"]` (finding_ids only; header skipped). inv2: a listed sub-quorum id
  reports **MEDIUM** with suffix `[documented exception P5-01]`; **any unlisted sub-quorum id stays
  HIGH (fail-closed)**. File is read from the ledger dir so fixtures carry their own.

The 21 ids: 06ec90ca5a, 0d1fcbac97, 1c2fc2e007, 4dcc841f1d, 53b8aa949c, 55e47042d0, 588808eb93,
6ffdcb45b8, 785c7c812d, 7d4ef26bce, 87abc048a2, a929835ba5, bafce48906, bbd4083c24, c9839ea0aa,
d1d2d45449, d2bcd90e7e, e3dbc1c7ff, ecdb869fd5, feddf80687, ffc452cd3f (all prefixed `F-S9-PR-`).

## (iii) inv5 reconciliation amendment (resolved-escalation absorption)

- Root cause: the 22 escalations that were later resolved on the loop-3 path each carried BOTH a
  terminal FIXED fix AND a `_review-needed` mention, so the old formula counted them twice
  (`fixed_n` + `escal_fix`): `498 != 498 + 22`.
- Amended: `fixed_n = |need_fix_ids ∩ fixed_ids|` (distinct-finding basis, robust to multi-loop
  rows); an ESCALATE-path finding whose fix rows include a terminal FIXED (any loop) is **absorbed**
  — counted once as fixed, not as an open escalation. Only escalations WITHOUT a FIXED fix count as
  `open_escalations`. Reconciliation: `need_fix_n == fixed_n + open_escalations`. Distinct
  `resolved-escalations` / `open-escalations` counters threaded via an optional `stats` out-param
  and printed in the summary line.
- Real data: need_fix=498, fixed=498, **resolved-escalations=22**, open=0 -> 498 == 498 + 0 GREEN.
  Resolution record: `_review-needed/s9-p3-underreview-promotions.md` + the loop-3 fix rows.

## Fixtures + self-test (fail-closed proofs)

Added `scripts/s9/fixtures/ledger/{p5_pass, p5_fail_exception, p5_fail_escalation}/`, wired into
`self_test()` (with `want_medium` / `want_resolved_esc` assertions on the extended `expect()`):

- **p5_pass** — PASS for (ii)+(iii): a listed sub-quorum finding -> exactly 1 MEDIUM, 0 HIGH; an
  escalation-path finding with a terminal loop-3 FIXED -> absorbed, `resolved-escalations == 1`.
- **p5_fail_exception** — FAIL-CLOSED for (ii): a sub-quorum id NOT in `ledger-exceptions.jsonl`
  stays HIGH **even though the file is present** (it lists a different id).
- **p5_fail_escalation** — FAIL-CLOSED for (iii): an UPHELD finding whose loop-3 re-review is
  NOT-FIXED and which has no escalation file stays HIGH (inv1 + inv5). Proves absorption is gated on
  a real terminal FIXED (or a real escalation file), never on the escalation label alone.

## Coverage

- Items assigned: RULING P5-01 parts (i)/(ii)/(iii) + fixtures + verification.
- Items examined: 2 orphan adjudications; 21 sub-quorum findings; 22 resolved escalations; the full
  498 need-fix / 498 FIXED / 25 escalation-mention set; F-DEMO-001 acceptance; run()/completeness
  entry points.
- Items skipped: none in scope. `--completeness` mode still reports 1 HIGH (the R14.5 verdict-less-
  inventory gate over 24619 inventory items) — this is OFF the normal roster/bootstrap gate by
  design (docstring), independent of the LINT-30 reconciliation invariants, and outside this
  packet's scope; unchanged by these edits.

## Notes for the machine (nothing owed back)

- Writer != checker preserved: this lane emits reconstructions + tooling amendments + fixtures; it
  does NOT re-adjudicate any finding. The two reconstructed findings retain their existing P2
  DISMISSED verdicts (finder lanes codex/opus-panel != adjudicator orchestrator; inv3 clean).
- `_run/s9/ledger-exceptions.jsonl` is a committed adjudicated-allowlist: expanding it is an
  orchestrator act (fail-closed for any id not listed), mirroring lint11.
- `needs_orchestrator=false` on all 6 fix rows: everything ran cache/lake/artifact-local, no CL.
