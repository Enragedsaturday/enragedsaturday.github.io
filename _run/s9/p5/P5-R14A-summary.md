# P5-R14A — S9 R14 self-audit (checks 1, 4, 5, 7)

Lane `claude-opus-4-8` (packet P5-R14A). WRITE-SCOPE `_run/s9/p5/` only. Read-only over
`_run/s9/**`. No CL. Adjudicated P2/P3/P4 rows treated as law (not re-litigated); this is a
meta-audit of the pass's own accounting, blindness, coverage, and escalations.

| # | Check | Result |
|---|-------|--------|
| (1) | False-positive accounting | **PASS** |
| (4) | Blindness audit | **PASS** |
| (5) | Inventory completeness | **PASS** |
| (7) | Escalation audit | **PASS** |

Outputs: `R14-1-fp-accounting.json`, `R14-4-blindness.json`, `R14-5-completeness.json`,
`R14-7-escalations.json` (each `{check, method, counts, result, exceptions[]}`).

---

## (1) False-positive accounting — PASS

- **2,331 adjudications** (incl. the 2 P5-reconstructed `F-S9-PR-d1d2d45449` / `F-S9-PR-6ffdcb45b8`,
  both DISMISSED disclosure-induced FPs with holdings, RULING P5-01(i)).
  Verdicts: UPHELD 227 · MODIFIED 271 · **DISMISSED 1,831** · ESCALATE 2. FP rate **78.55%**.
- **DISMISSED without a reason: 0.** All 1,831 carry a non-empty `adjudicated_holding` list.
- **Per-lane refute/dismiss signal** (prompt-tuning only; join panel-lane vote verdict × final adjudication):

| Lane | votes | refute-rate | refute-precision (refuted→DISMISSED) | stands-precision (stands→UPHELD/MOD) |
|------|-------|-------------|--------------------------------------|--------------------------------------|
| codex-A | 2,291 | 32.6% | 97.7% (729/746; 17 overruled) | 29.7% |
| codex-B | 2,294 | 63.7% | 79.3% (1160/1462; 302 overruled) | 21.3% |
| claude-opus-panel | 2,296 | 81.7% | 92.4% (1732/1875; 143 overruled) | 79.8% |

Signal read: **codex-A** is the conservative refuter — rarely refutes, near-perfect when it does,
but 70% of the findings it lets "stand" are dismissed by the 2-of-3 quorum (under-sensitive to
false positives). **codex-B** is the most trigger-happy false-refuter (302 refutes overruled).
**claude-opus-panel** is the designed adversarial refuter (highest refute-rate) and best-calibrated
on both axes. Tuning signal, never auto-suppression (spec R14(1)).

## (4) Blindness audit — PASS

- **Freeze hash proven.** `thread-P.sha256` = header `content_hash` = recomputed `items[]` canonical
  sha256 = the `thread_p_hash_at_issue` attested in **all 1,357 opus-pack groups and 3,945 codex
  manifests** = `8e51d0c8…6433c8`. Note: the sidecar is a *content-hash anchor* (items[] only,
  excludes header/`generated` — per `build_thread_p` docstring), **not** a raw-file checksum
  (`shasum -c` would fail by design; raw-file sha = `45904bc5…`). Documented, not a violation.
- **Frozen before N.** thread-P `generated` 2026-07-09T19:51:56Z **<** earliest thread-N read
  2026-07-09T22:19:25Z (Δ 8,849 s ≈ 2 h 27 m).
- **No contamination.** 2,121 attestations all assert `independent="isolated review; no sibling
  votes/adjudications disclosed"` + `recorded_before_reconciliation=true`; 1,357 opus groups all
  carry `fields_excluded=[sibling_votes, in_progress_adjudications]` and **0 blindness_violations**;
  3,956 codex manifests + 3 worklists + 1,947 thread-N reads: **0** disclosed vote/verdict/adjudication
  fields; all 6,881 panel votes `recorded_before_other_votes_read=true`. 11 manifests lack the
  hash field (10 Fable doctrine-rederive lanes that explicitly exclude thread-P + lake judgment
  fields; 1 pilot-vote) — benign; case-read lanes carry a *stronger* exclusion set. **No contaminated
  manifest to name.**

## (5) Inventory completeness — PASS

- Inventory: **24,619** items, 0 duplicate ids. Object→assertion reconstruction per
  `build_worklists.py` `PANEL_DIM` (the 9 legal-assertion kinds are 3-lane-panel scope; other kinds
  are editorial/structural → D3 "1 reviewer + lints").
- **Panel-scoped items: 7,459.** Worklist panel-assigned ids = 7,459 (exact). Covered by
  reviewed_assertion_ids ∪ assigned ∪ finding_ids = **7,459 / 7,459. Verdict-less panel items: 0.**
- Non-panel structural items: 17,160 → 17,006 join to a verdicted file; **154 residual**
  (42 glossary definitions + 112 section-index nav `link_target`/`link_mention`) route to the R8
  corpus-wide lint roster by design and join no panel-vote/adjudication/P4-bridge row (they never go
  to the panel). Verdict = green lint status → **deferred to the sibling R14(6) lint spot-verification
  packet.** Not silent drops: every residual maps to an existing content page (enumerated in the
  JSON `exceptions[].files`). The R14.5 core claim (zero verdict-less panel items) holds.

## (7) Escalation audit — PASS

- **498 distinct fix chains, all terminate FIXED** (terminal status = {FIXED: 498}).
  Max-loop {1: 455, 2: 21, 3: 22}.
- **Bijective owed-fix ↔ fix:** 498 UPHELD/MODIFIED adjudications ⇔ 498 fix chains; 0 owed-fix without
  a fix row, 0 fix row without an owed adjudication.
- **42 NOT-FIXED rows** (all loop-1 residue) each superseded by a higher-loop FIXED — 22 at loop-3
  (the `under_review`-blocked promotions), 20 at loop-2. **0 NOT-FIXED terminals.**
- **22/22 loop-cap (loop-3) chains** terminate FIXED **and** are all enumerated in
  `_review-needed/s9-p3-underreview-promotions.md`.
- **2 ESCALATE adjudications** (F-S9-P2-DELGADO, F-S9-P2-ENTRAP2) both carry `_review-needed` routing
  files. 6 P4-lane authority-weight escalations dispositioned via `P4-RULINGS.md`.
- **Nothing silently dropped.**

---

### Coverage / method notes for the orchestrator

- Every number re-derived from disk this pass (script in scratchpad; read-only). Sources joined:
  adjudications (2,331), votes (6,882; 6,881 panel-lane), findings (2,331), fixes (541),
  panel-attestations (2,121), thread-N-reads (1,947), 375 opus-pack manifests / 3,956 codex
  manifests, panel-review worklist (1,356 objects), assertion-inventory (24,619),
  P4-LEDGER-BRIDGE (725 candidates) + 114 `p4/out` sweep artifacts, `_review-needed/` register.
- **One item for orchestrator ruling** (C5): the 154 lint-governed structural residuals — confirm
  they are R14(6)'s domain (lint spot-verification), not an R14(5) gate failure. I read them as
  by-design (D3) and set C5 = PASS accordingly; the sibling lint packet owns their green-status
  verdict.
- No writes outside `_run/s9/p5/`. No CL. No re-adjudication of P2/P3/P4 verdicts.
