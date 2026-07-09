# S8 work order — R12 ledger assembly + R13 lint kit rewrite (lane: o2-opus-xhigh)

**Read first:** spec R12 + R13 (+ §5 Method 8, §7 acceptance) · handoff §2.2 (LINT-5 2767 MED
class, LINT-7 136 HIGH register-exemption decision) · `scripts/s8/zones.py` (frozen — both
lints import it) · current `scripts/lint/lint5_link_every_case.py` + `lint7_glossary.py` +
`scripts/lint/_common.py` conventions + `scripts/lint/fixtures/` shape · row sources:
`_run/o2-execute/s8-link-ledger.rows.mentions.jsonl` (13996) · `s8-link-ledger.rows.jsonl`
(cases 400 + doctrine 564, {lane,model,scope}) · `s8-term-rows.jsonl` ·
`s8-adjudication-queue.jsonl` (187) + `s8-adjudication-resolutions.jsonl` (187) ·
`s8-embed-rows.jsonl` (4 rows, landing shortly) · `_run/s6-coverage-ledger.json` (252) ·
`_run/o2-execute/s8-caption-index.json`.

## Deliverable 1 — `scripts/s8/assemble_ledger.py` (R12)

Merges the lane row files into the canonical `_run/s8-link-ledger.json`:
- `mentions[]` — every case-mention occurrence row (schema from spec R12: file, line,
  matched_text, caption_key, resolution{target, method, rationale?}, action). Adjudicated
  rows get `method: adjudicated` + the resolution rationale joined from the resolutions file.
- `terms{}` — per-page register coverage counts (from s8-term-rows.jsonl).
- `embeds[]` — every `![[` with source anchor (from s8-embed-rows.jsonl + a fresh corpus
  scan for pre-existing exhibit embeds — the scan is authoritative, the rows are provenance).
- `pincites[]` — the cases+doctrine rows (scope-tagged).
- Header: {generated, lane, model, spec: S8, counts, sources[]}.
- **The COH-15 join** (a subcommand `--join`): re-derive the distinct bare-mention caption
  set from the ledger; join × the S6 coverage ledger; emit `_run/o2-execute/s8-coh15-join.json`
  proving R1: every in-scope mention of an `authored`/page-backed caption is linked or
  queue-resolved; every plain mention cites a non-page terminal, an exemption zone, or a
  fail-closed resolution; report the re-derived NUM-04 count. **A script, not an agent** —
  deterministic, re-runnable, exit 1 on any join violation.
- `--self-test` + fixtures.

## Deliverable 2 — R13 lint rewrites (fixtures for EVERY check, pass + fail)

**(a) LINT-5 REWRITTEN** (`lint5_link_every_case.py`): ledger-aware bare-caption check —
bare `authored`/page-backed caption in prose = FAIL; bare non-page-terminal caption = PASS
(the rule, not an exception; read the S6 ledger + caption index); markdown-link text masked
(kills the Sources false-positive class); R2 zones shared via zones.py import; **broken
anchor (wikilink `#^…`/`#…` target that does not resolve) escalates MEDIUM → HIGH**;
`![[` embed targets must be full-slug (path-qualified) — non-full-slug embed = HIGH.
**(b) LINT-7 REWRITTEN** (`lint7_glossary.py`): the first-occurrence-only rule (old check c)
is **DELETED — inverted by D1**; replaced by: register-coverage review flags (a routed
term's occurrence outside zones that is NOT linked = MEDIUM review item, register-driven
from term-register v2 route/target/match columns); dead register anchors/targets = HIGH
(fail); keep the v1 banned_variants check. The page-title-variant known-false-positive
class (handoff §2.2) — the register carve-out decision: **route rows whose target page
title equals the term surface do not flag on their own target page** (that kills the
~140-row FP class mechanically; document in the lint header).
**(c) pipe-escape check** (new `lint27_table_pipes.py` or next free number — check the
roster in run_all.py; numbering provisional per S1 A5): unescaped `|` inside a wikilink
inside a table row = HIGH. **(d) fragment well-formedness** (new lint, same numbering rule):
every `#:~:text=` link in content — syntax-valid WICG fragment, host ∈ CL/whitelist,
URL-encoding valid. SYNTAX ONLY (semantic validation lives in R5 at write time; CI never
calls CL). **(e) R9 shingle boundary check** (new lint or a `--check` mode on shingles.py
wired into run_all): rule-node overlap ≥25t outside an embed = HIGH; pin overlap that is a
re-typed BLOCK QUOTE = HIGH; inline-woven/list quoted overlaps = exempt (the adjudicated
sanctioned class).
Wire (c)/(d)/(e) + rewritten 5/7 into `run_all.py` per its existing roster conventions
(LINT-15/16 stay standalone per batch-1 rule C — check how run_all excludes them).

## Execution

1. Build assembler + self-test → run → emit ledger + join. Report join verdict + counts +
   any violations found (violations = evidence, not silent fixes — report them).
2. Rewrite/add lints + fixtures → run each on the corpus → report per-lint counts vs the
   old counts (LINT-5 was 2767 MED, LINT-7 136 HIGH — explain the new numbers class-by-class).
3. `python3 scripts/lint/run_all.py` summary before/after. Zero-new-HIGH rule: new HIGHs
   must be real defects surfaced by the better checks — enumerate every one.

Constraints: COMMIT NOTHING · zero CL · stdlib only · touch only `scripts/s8/assemble_ledger.py`,
`scripts/lint/**` (the named lints + run_all roster + fixtures), `_run/s8-link-ledger.json`,
`_run/o2-execute/s8-coh15-join.json`. Content is read-only for you. Sibling lanes are
writing content concurrently (4 embed conversions + 42 resolution links + a term-recovery
pass) — run your corpus-facing scans LAST and note the git HEAD you scanned at.
