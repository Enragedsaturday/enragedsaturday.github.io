# COHERENCE wrapper — the cross-spec pass + AUDIT-CLOSURE gate (paste-pointer thread)

You are running the **CSSI Overhaul-2 COHERENCE PASS** in a clean context: all nine specs are
signed (S1–S9, RUNBOOK §7 all ✅, last commit `c2df16a`). This is an **audit/gate thread, not an
interview thread** — no mockups, no AskUserQuestion rounds except for genuine
`conflict:user-decision-needed` escalations. Fixes land as **amendments + forward supersession
notes only** (RUNBOOK §0 precedence stack: approved specs > RUNBOOK > PRACTICES > wrappers) —
never silent rewrites.

## Read first (grounding)
1. `_overhaul2/RUNBOOK.md` — §0 (precedence stack + human-pause register), §1–§3, §7 (the
   **AUDIT-CLOSURE gate** text — your exit condition).
2. ALL NINE specs in `_overhaul2/specs/` **including every Amendments section and the cross-spec
   notes** (S2 A14/A15 · S6 A1/A2 · S8's filed notes · S9's Cross-spec section).
3. `_overhaul2/AUDIT-2026-07-02.md` (register + closure block + disposition vocabulary — your
   findings register reuses its format) · `_overhaul2/PRACTICES.md` (supersession notes must
   still be accurate) · `_overhaul2/s9-demo/` (the signed ledger schema + worked machine).
4. Wrappers are SUPERSEDED by their signed specs (banners) — check banners exist on S5–S9's.

## Mission (two halves, in order)

**A — The coherence sweep.** Hunt cross-spec contradictions, dangling references, seam gaps, and
unowned obligations across the nine specs + RUNBOOK + PRACTICES. Every finding gets a register
row (`id · sev · seam · disposition · pointer` — audit-register vocabulary). Known seams to
check (seed list, not a ceiling):
- **Lint roster**: S9 R8's LINT-1…30 table vs S1 A5 aliases, S2 A15, S3's eight `LINT-S3-*`,
  S4's goodlaw-target, S5 LINT-15/16, S6 LINT-17, S8's rewrites + new checks — no collisions,
  no orphaned lint named anywhere that lacks a roster row.
- **TEACH-08 heading rename**: everything that greps `Recent developments` (S1 A2's N5 check,
  LINT-3 + its committed fixture `scripts/lint/fixtures/lint-3-n5.md`, S5 R11) must handle the
  successor heading `Lower-court developments` — including the transition window at EXECUTE.
- **Human-pause register (§0)** vs the pauses specs actually define: S6's packets A/B, S9's
  release gate + `>10 new pages` pause + the frontier-re-run **tripwire** pause + S6's `>150
  pages` scope guard — reconcile the enumerated list.
- **NUM-03 boundary**: S8 R6 (content remediation) ↔ S9 LINT-9 + R9(a) (guard/verify) — no gap
  for pins minted AFTER S8's pass.
- **S2F-07b chain**: S2 A8 ↔ S3 R5 binding map ↔ S9 R10(a) provisional-slug recheck.
- **The 388/88 reconciliation chain**: S6 R11 ledger ↔ S8 R12 join ↔ S9 R9(b) sampling.
- **S2 A14/A15 vs the builder's schema freeze** (S8 §9 contingency) and S6 A2 (dual-model
  frontier) vs S6 R7's web-never-asserts queue.
- **Retirement sequencing**: S4 R8/D5 ↔ S9 R15 (deploy first, retire after, re-verify).
- **Exec-wave concurrency vs `gates:` headers** (COH-04's authoring-vs-execution rule holds).
- **Deferred-run preconditions**: deck stems (S3 A2 / LINT-25 ↔ S9 R12 attestation);
  maintenance-loop seeds (S9 R12 ↔ GH#2); the O1 `_review-needed/lint3-…` ticket's closure
  pointer (per S9's COH-28 disposition).

**B — The AUDIT-CLOSURE gate (blocking, fail-closed).** The pass FAILS unless BOTH hold
(RUNBOOK §7): (1) every row in `AUDIT-2026-07-02.md` has a terminal disposition + a real
pointer; (2) every `injected:S4..S9` ID has an explicit adopt/adapt/reject-with-rationale
disposition in its spec's Decision Log. **The closure stamp is made by an adversarial NON-WRITER
lane** — an agent that authored none of this thread's fixes walks the register against disk and
stamps it (the 2026-07-02 closure-block precedent; disk is ground truth, writer claims are
claims).

## Deliverables
`_overhaul2/COHERENCE-REPORT.md` (findings register + dispositions + the closure stamp) ·
fixes as spec Amendments / forward notes (commits referenced per row) · RUNBOOK §7 footer
updated (coherence ✅) · **author `_overhaul2/wrappers/EXECUTE.wrapper.md`** — the launcher for
the one autonomous EXECUTE run (wave order per RUNBOOK §3: S1 rulebook → S2 lake (multi-day,
paced) + S4 nav → S3 + S5 → S6 → S7 → S8 → S9 verify + release; carry the §0 pause register,
the per-credential CL lanes (S1 A1/L4′), and the S9 R13 gate as the ship condition). Hand the
EXECUTE wrapper back as a SHORT paste-pointer like this one.
