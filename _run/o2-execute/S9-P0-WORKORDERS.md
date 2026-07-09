# S9 P0 work orders — bootstrap lanes (all o2-opus-xhigh; COMMIT NOTHING; zero CL; content read-only)

**Every lane reads first:** `_overhaul2/specs/S9-verification.spec.md` (the law; your R-section
in full) · `_run/o2-execute/S8-TO-S9-HANDOFF.md` · `_overhaul2/s9-demo/LEDGER-SCHEMA.md`.
O1's `_run/{assertion-inventory.json,thread-P.json,S9-LEDGER.json}` are HISTORICAL — never
overwrite; O2-S9 artifacts live under `_run/s9/`.

## Lane P0-A — assertion inventory (R2)

`scripts/s9/build_inventory.py` → `_run/s9/assertion-inventory.json`.
Deterministic extraction of every tracked assertion from every object class (spec R2 list:
case pages · doctrine/overview/reference pages · glossary · Case Index · nav/About · lake
records · S6 coverage-ledger rows · S8 link-ledger rows): case-cite · proposition ·
quote+pinpoint (+pinpoint_status +fragment) · treatment fields · weight label · homes/roles ·
registry point↔callout pair · mermaid block · link/embed targets. Every item gets a stable
`assertion_id` (content-hash based — re-runs must re-derive identical ids on unchanged
content). Header: {generated, lane, model, corpus_head}. Self-test + fixtures
`scripts/s9/fixtures/inventory/`. Report: counts per class, id-stability proof (run twice,
diff empty), 5 sample items per class.

## Lane P0-B — Thread P freeze (R5)

`scripts/s9/build_thread_p.py` → `_run/s9/thread-P.json` + `thread-P.sha256`.
Deterministic extraction of the BUILT corpus's conclusions: per case (from page + frontmatter
+ lake record): holding/disposition · treatment on taught points · homes/roles · split
positions; per doctrine page: case-set + split calls. NO judgment of correctness — P is what
the corpus CLAIMS. Freeze = emit + hash + timestamp; the hash goes in the header AND the
sidecar. Self-test + fixtures. Report: per-class counts, the hash, 3 sample case rows +
2 doctrine rows, and the no-regression floor baseline (total P items — every one must be
dispositioned by the concordance later; this number is the floor).

## Lane P0-C — lint roster codification (R8)

The R8 table IS the roster. Work:
1. **Renumber** the S3 set → LINT-18..25 and S4 goodlaw-target → LINT-26 (aliases survive on
   first mention only; grep scripts/lint for the current names — some may already be numbered;
   the table wins on collision, Decision-Log the correction).
2. **Rebuild LINT-3 lake-driven** per the R8 #3 row (section-scoped frontier checks from lake
   court data; the token-window heuristic DIES; committed acceptance fixture
   `scripts/lint/fixtures/lint-3-n5.md` must pass; + the S1 A9 >3-cases-per-paragraph
   sub-check).
3. **LINT-8 + TEACH-11**: mnemonic/maxim wikilink-target checks (target exists + matches the
   register entry).
4. **LINT-30** = the R4 ledger-invariant script (`scripts/s9/check_ledger.py`, invariants 1–5
   from spec R4, joined by assertion_id; runs green on an empty-but-initialized `_run/s9/`
   ledger set ONLY in a bootstrap mode that says NO-ROWS-YET — it must FAIL-CLOSED once rows
   exist and any invariant breaks; validate against the F-DEMO-001 demo rows in
   `_overhaul2/s9-demo/` as the acceptance test).
5. Wire 2–30 into `run_all.py` fail-closed per its conventions (1 stays serial-gate-only);
   every touched/new lint ships pass+fail fixtures.
Report: roster table as-wired (number → file → fixtures y/n), LINT-3 rebuild before/after
counts on the corpus with class explanations, lint-30 demo validation output, full run_all
summary vs the S8-close baseline (TOTAL 4176 / HIGH 3381) — zero-new-HIGH with every new HIGH
enumerated + justified, or the delta explained class-by-class (renumbering must not change
verdicts).

## Shared constraints

Stdlib only · fixtures for everything · idempotent · deterministic (no Date.now-style
nondeterminism in ids) · do not touch `content/`, the lake, single-writer surfaces, or
another lane's files. The orchestrator (Fable) reviews and commits.
