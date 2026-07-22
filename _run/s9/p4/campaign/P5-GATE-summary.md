# P5-GATE summary — R13 release-gate table assembly

**Packet:** P5-GATE · **lane/model:** `P5-GATE` / `claude-opus-4-8` · **branch:** overhaul2/execute · **generated:** 2026-07-22T09:26Z
**Write-scope honored:** only `_run/s9/p4/campaign/` written (`R13-GATE-TABLE.md`, `R13-GATE-TABLE.jsonl`, this file). Everything else read-only. No CL. No verdicts — `status_proposed` are proposals for the orchestrator.

## Deterministic coverage

| Unit | Assigned | Examined | Skipped |
|---|---|---|---|
| R13 gate boxes | 15 | 15 | 0 |
| Doctrine pages (composite) | 79 (type=doctrine) | 79 | 0 |
| `_review-needed/` files | 9 | 9 | 0 |
| Inventory items (R2 join) | 24619 | 24619 | 0 |
| Ledger rows (findings/adj/fixes) | 2331 / 2331 / 541 | all | 0 |
| R6 pairs | 437 | 437 | 0 |

Box outcome: **11 PASS · 4 ESCALATED · 0 BLOCKED**. No box is BLOCKED; every ESCALATED box carries a logged basis (R13-compatible).

## Method
- **R2:** joined assertion-inventory.json (24619/9 classes) × findings×adjudications × P4-LEDGER-BRIDGE; ran `check_ledger --completeness`.
- **R4/R8:** ran `check_ledger.py` (09:24:56) and `run_all.py --summary-json/--quiet` (09:17:57 pre-amendment, 09:25:59 post-amendment) myself, read-only.
- **R5:** reproduced thread-P content_hash from items[] canonical JSON; traced git-immutability; confirmed 1947 N-reads recorded_before_reconciliation post-freeze; read reconciliation-summary.json.
- **R6/R7/R9/R10/R11:** read the packet summaries + dispositions + RULINGS P4-01..21 / P5-01.
- **Brief composite:** joined 79 type=doctrine pages × opus-reviews group_ids × codex panel-results group_ids × findings/adjudications/fixes/escalations. No page re-reviewed.

## Items flagged for orchestrator adjudication (not papered over)
1. **R2 completeness (ESCALATED):** `check_ledger --completeness` fires 1 HIGH — 22318 inventory items carry no explicit per-item verdict (they passed with no finding). Orchestrator must rule whether 'no finding = implicit-PASS' satisfies R2's 'zero verdict-less', or per-item verdict emission is required. (2301 items are finding-referenced; every finding is adjudicated.)
2. **R4/R8 timing (informational):** sibling **P5-LEDGER** amended `check_ledger.py` + created `ledger-exceptions.jsonl` (22 rows) + reconstructed 2 orphan findings DURING assembly. LINT-30 flipped 22 HIGH (09:17) → 0 HIGH (09:25). These files are git-modified/untracked (uncommitted). Re-run `check_ledger.py` + `run_all.py` at the true gate moment to confirm the final state after P5-LEDGER commits.
3. **R5 sidecar nit (benign):** `shasum -c _run/s9/thread-P.sha256` FAILS cosmetically — the sidecar records the canonical CONTENT hash (8e51d0c8), not the file-bytes hash (45904bc5), by design. Freeze integrity holds (git-immutable + reproducing content_hash). Consider a note in the sidecar or a second file-bytes sidecar so a future `shasum -c` auditor is not misled.
4. **Brief composite (ESCALATED):** 3 section-`index.md` landing pages flagged (2 no-callout with rules on child pages; 1 registry-home parent un-paneled). Convention-exempt candidates — confirm the S5 overview/hub convention covers them (Amendment A2/A3 + COH-B precedent).
5. **R12 (ESCALATED/PENDING):** maintenance-handoff artifact not yet on disk (sibling packet owns it).
6. **G8 (SCHEDULED):** publish pause is a P6/R15 human gate; recorded so it is never silently skipped.
7. **5 open `_review-needed/` files** (delgado, entrap2, lint3-chatrie, threadN-lyle, coverage/batch4-dup-CL) — all gate-compatible ESCALATED; batch4-dup-CL is an unmarked S5-era stand-down note likely resolved-by-completion.

## Files emitted
- `_run/s9/p4/campaign/R13-GATE-TABLE.md`
- `_run/s9/p4/campaign/R13-GATE-TABLE.jsonl`
- `_run/s9/p4/campaign/P5-GATE-summary.md`
