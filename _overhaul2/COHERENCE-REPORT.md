# O2 COHERENCE REPORT — cross-spec pass over all nine specs + AUDIT-CLOSURE gate

Run: 2026-07-04, per `_overhaul2/wrappers/COHERENCE.wrapper.md`. All nine specs signed at entry
(RUNBOOK §7 all ✅; S9 signed at `c2df16a`). Fixes below land as amendments + forward notes only
(§0 precedence stack). The AUDIT-CLOSURE stamp (§B) is made by an adversarial **non-writer lane**
— an agent that authored no edit verified here; disk is ground truth.

## A — Coherence findings register

Vocabulary per `AUDIT-2026-07-02.md`. Sev: H high · M medium · L low.

| ID | Sev | Seam / finding (one line) | Disposition | Pointer |
|---|---|---|---|---|
| COH2-01 | M | S7/S8/S9 wrappers lacked the COH-26 SUPERSEDED banner (S5/S6 have it) | fixed-now | banners added to all three wrappers, 2026-07-04 |
| COH2-02 | L | Header grammar forks at S6: S6–S9 use `gates:` in the **gated-by** sense (S1–S5 use `depends-on`/`gates` lists) | rejected:no-defect-in-effect | prose parentheticals make the reading unambiguous; **RUNBOOK §3's table is the single dependency authority** (COH-04); no signed-header churn |
| COH2-03 | L | S1/S2 header `gates:` lists are loose supersets (e.g. S2 lists S4, which does not depend on S2) | rejected:no-defect-in-effect | same authority rule (COH-04) |
| COH2-04 | M | S9 R8 row "18–25 S3 set" lacked the explicit per-lint id mapping (EXECUTE ambiguity) | amended:S9 | S9 § Amendments A1(1) — LINT-18 depth … LINT-25 deck |
| COH2-05 | M | S9 R9(c) fragment-trace check vs the S2-A14 schema-freeze contingency (S8 §9): if fragments live in the S8 ledger, the "lake field present" check can't hold | amended:S9 | S9 A1(2) — trace runs ledger→lake quote; field check defers to the next lake build; tier-3 ban unconditional |
| COH2-06 | M | LINT-1's live-CL batch had no assigned credential under L4′ (one consumer per credential) | amended:S9 | S9 A1(3) — builder credential runs the batch; Claude MCP lane keeps the ≥1-in-10 judgment slice (COH-17) |
| COH2-07 | H | §0 human-pause register claims "nothing else stops the line" while FOUR signed scope-guard pauses were unenumerated (S6 §9 >150 · S7 §9 >10 promotions · S9 R7 >10 discoveries · S9 R7.5 tripwire) | fixed-now | RUNBOOK §0 register, new pause #7 |
| COH2-08 | M | LINT-3 acceptance fixture used the legacy `Recent developments` heading TEACH-08/S5-R11 rename; sweep also surfaced a THIRD legacy-lint defect — its `recent-dev*` hints don't know the successor heading, so the renamed section falls out of scope entirely | fixed-now | fixture re-headed + baseline paragraph corrected; verified live: current lint emits 0 findings on the renamed fixture (proves the under-scoping); rewrite scope covers both headings |
| COH2-09 | L | Lint-name census across specs/RUNBOOK/PRACTICES: no numeric collisions, no orphaned lint lacking a roster row; all `LINT-S2/S3/S4-*` names alias-mapped | rejected:no-defect | census run 2026-07-04 (grep, all docs) |
| COH2-10 | L | NUM-03 boundary continuity (pins minted after S8's pass): S6 R8 pages born conformant, S7 pins written back per S2 R3, LINT-9 guards in CI post-S8 | rejected:no-defect | analysis vs S5 R16 / S8 R6 / S9 R8 #9 |
| COH2-11 | L | S2F-07b chain (S2 A8 preconditions ↔ S3 R5 binding lint ↔ S9 R10(a) recheck) incl. lint-activation timing | rejected:no-defect | consistent as written |
| COH2-12 | L | The 388/88 reconciliation chain (S6 R11 ledger ↔ S8 R12 join ↔ S9 R9(b) sampling) | rejected:no-defect | consistent; machine-join artifacts named identically in all three |
| COH2-13 | L | Retirement sequencing (S4 R8/D5 deploy-then-retire ↔ S9 R15 re-verification) | rejected:no-defect | consistent |
| COH2-14 | L | Deferred-run preconditions: deck stems (S3 A2 / LINT-25 ↔ S9 R12 attestation); maintenance seeds (S9 R12 → GH#2) | rejected:no-defect | consistent |
| COH2-15 | L | Dangling-reference sweep: `S6-SEED.md` + `audit_cases.py` exist; Prompt.md / book-PDF drops noted at every reference site; `registry.yaml`/`s2-binding.yaml` correctly framed as EXECUTE PRECONDITIONS (S2 A8) | rejected:no-defect | disk checks 2026-07-04 |
| COH2-16 | L | O1 `_review-needed/lint3-…-false-positive.md` ticket: closure path is recorded (closes at EXECUTE when the S7 content half + the LINT-3 rewrite land) | covered-by-spec | S9 Decision Log, COH-28 disposition |
| COH2-17 | L | S5 §9's provisional LINT-15/16 numbering | covered-by-spec | confirmed by the S9 R8 roster |
| COH2-18 | L | PRACTICES supersession notes (§5 ×2) still accurate; no new notes needed | rejected:no-defect | read-through 2026-07-04 |

**Summary: 18 rows — 4 fixed-now · 3 amended:S9 · 2 covered-by-spec · 9 rejected:no-defect. Zero
`conflict:user-decision-needed`.**

## B — AUDIT-CLOSURE gate (RUNBOOK §7; blocking, fail-closed)

Conditions: (1) every row in `AUDIT-2026-07-02.md` carries a terminal disposition + a real
pointer; (2) every `injected:S4..S9` ID carries an explicit adopt / adapt / reject-with-rationale
disposition in its spec's Decision Log.

**Closure stamp (verbatim from the non-writer lane):**

## ✅ AUDIT-CLOSURE stamp — 2026-07-04

**Verifier:** adversarial non-writer closure lane (authored no edit verified here; read-only).

**Condition 1 (register integrity): PASS** — 162/162 rows mechanically swept: every Status value
is terminal vocabulary, the tally reproduces the 2026-07-02 closure table exactly, and zero rows
have an empty Pointer cell. No row regressed to non-terminal. 12 pointers spot-verified against
disk, weighted CRITICAL/HIGH (COH-01 all four ban sites + PRACTICES supersession · COH-02a
S6-SEED + audit_cases.py · S2F-01a denylist reversal · LAW-01 corrected verbatim quote · LAW-02b
frontmatter identity fields · LAW-03 vote lineup · TAX-03a R13/urls · COH-06 pause register 1-7 ·
COH-07 L4' per-credential · CODE-01a commits 8655398/be02044 · GAP-01a cat-11 placed nodes ·
LAW-05 stale legend correctly still in place pending S7) — all PASS.

**Condition 2 (injected-ID dispositions): PASS** — 58 injected IDs extracted (61 spec-legs;
dual-routed IDs counted in each named spec); 58/58 dispositioned, 61/61 legs found verbatim in
the named specs' Decision Logs: S4 11 legs (incl. COH-18) · S5 8 legs (incl. TEACH-08 + COH-18) ·
S6 11 legs (incl. GAP-04f REJECT-WITH-RATIONALE + COH-15) · S7 20 legs (LAW-04 dispositioned via
named absorption inside TEACH-03's ADOPT entry, exactly per the register's own routing) · S8 3
legs (incl. COH-15's second leg) · S9 7 legs (incl. NUM-03's reciprocal S8/S9 boundary pointers).
Missing: NONE.

**Condition 3 (coherence-pass fixes): PASS** — (a) SUPERSEDED banners verified atop the S7/S8/S9
wrappers; (b) RUNBOOK §0 pause #7 names all four scope-guard pauses; (c) S9 Amendments A1 items
(1)(2)(3) present; (d) fixture re-headed to `## Lower-court developments`, and a LIVE run of
lint3 on it returned 0 findings — reproducing exactly the under-scoping the fixture documents;
(e) S2 A15 + S6 A2 present at end-of-file.

**Gate result: PASS.** All three conditions hold against disk; item (d) confirmed by live
execution, not by the report.

