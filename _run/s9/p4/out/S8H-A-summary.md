# S8H-A summary — WS S8H, R9 items (a) NUM-03 verification + (d) shingle scope check

Packet: `S8H-A`. Findings-only, WRITE-SCOPE `_run/s9/p4/` only. Model: `claude-sonnet-5`.

## Coverage
- Items assigned: 2 (task a — NUM-03; task d — shingle scope, R8 #29).
- Items examined: 2.
- Items skipped: 0.
- Corpus scanned: all of `content/**/*.md` (724 files, `find content -name '*.md' | wc -l`),
  the same default glob every lint below uses when invoked with no path args, and the
  glob the independent script re-derives from scratch (`os.path.join(CONTENT, "**", "*.md")`).

## Task (a) — NUM-03 verification

**LINT-9 (carat-leak / mid-line `^pin-N`)**
```
python3 scripts/lint/lint9_carat_leak.py --self-test
python3 scripts/lint/lint9_carat_leak.py content
python3 scripts/lint/lint9_carat_leak.py            # no-arg cross-check
```
- Self-test: PASS, 2/2 fixtures (`lint-9-anchor-wikilink-fail.md` expect=fail -> 1 viol OK;
  `lint-9-endline-pass.md` expect=pass -> 0 viol OK).
- Corpus (scoped `content` and no-arg, identical): **0 violations** (0 high/medium/low).
- Raw output: `_run/s9/p4/out/S8H-A-lint9-stdout.jsonl` (empty), stderr summary in
  `_run/s9/p4/out/S8H-A-lint9-stderr.txt`.

**LINT-5 (link-every-case / wikilink+anchor resolution)**
```
python3 scripts/lint/lint5_link_every_case.py --self-test
python3 scripts/lint/lint5_link_every_case.py content
```
- Self-test: PASS, 7/7 checks (incl. `anchor+deadlink+badembed-HIGH` = 3, `pass-clean` = []).
- Corpus: **23 violations, all `severity=medium`, 0 high, 0 low.**
  All 23 are the bare-page-backed-caption class ("`bare page-backed case name '...' is
  not a [[wikilink]]... [S8 R1/R13a]`") — a different LINT-5 concern (missing wikilinking
  of a caption), **not** a NUM-03 pin/anchor defect. LINT-5's own broken-anchor /
  dead-wikilink / bad-embed checks (fail-closed, escalate to HIGH, and specifically cover
  `#^pin-N` anchors via `idx.has_anchor`) produced **zero** hits corpus-wide. The 23 rows
  are reproduced verbatim in `_run/s9/p4/out/S8H-A-report.json` under
  `task_a_num03.lint5_link_every_case.rows_verbatim` and in the raw
  `_run/s9/p4/out/S8H-A-lint5-stdout.jsonl`. They are NOT filed as p4 candidates here:
  they belong to LINT-5's own steady-state gate (already enforced at `run_all.py`,
  non-zero-high threshold), are already MEDIUM (not blocking), and are out of this
  packet's NUM-03/shingle scope — flagged in this summary for the orchestrator's
  awareness rather than filed as a candidate row.

**Independent verification (script written from scratch, not a re-run of the lints)**

Script: `_run/s9/p4/out/S8H-A-independent-check.py` (read-only).
```
python3 _run/s9/p4/out/S8H-A-independent-check.py
```
Output: `_run/s9/p4/out/S8H-A-independent-check-out.json`.

- **Mid-line `^pin-N` count** (a caret-pin token NOT at start-of-line/block-anchor
  end-of-line position — the visible-carat risk): masks frontmatter/fences/HTML
  comments/`[[wikilinks]]`/`![[embeds]]`/`` `inline code` `` with its own separately
  written regex set, then flags any `^token` that does not end the (rstripped) line.
  **Result: 0.** Agrees with LINT-9.
  - Raw cross-check: `grep -rnoE '\^pin-[A-Za-z0-9]+' content --include='*.md' | wc -l`
    = **1403** total `^pin-N` tokens anywhere in the corpus (legal end-of-line anchors +
    tokens inside wikilinks/embeds + any leaks); of those, 0 are both outside a
    wikilink/embed AND not at end-of-line.

- **Broken pin wikilinks** ( `[[...#^pin-N]]` / `![[...#^pin-N]]` whose target page
  lacks that exact anchor): every pin-anchored wikilink/embed in the corpus
  (pipe-display stripped per the R11 `\|` convention) resolved to a target page by
  stem/basename match, then the target page's body was scanned for a line ending in
  that exact `^pin-N` token (the Obsidian block-anchor definition rule).
  - **Total pin-wikilink references: 287.**
  - **Resolving: 287. Broken: 0.**
  - Raw cross-check: `grep -rno '#\^pin-[A-Za-z0-9]*' content --include='*.md' | wc -l`
    = **287**, exactly matching the script's pre-resolution reference count (confirms
    the parser isn't over/under-counting before attempting resolution).
  - No broken-link rows to report — the "file+line for every broken one" requirement
    is vacuous here (empty list, present as `pin_wikilink_broken: []` in the JSON).

**NUM-03 verdict-relevant data point (findings-only, no verdict claimed):** all four
independent measures (LINT-9, LINT-5's anchor/embed checks, the from-scratch mid-line
scan, the from-scratch pin-resolution scan) agree at **zero** for both halves of NUM-03
(visible carats / broken pin links) as of this sweep. `_overhaul2/specs/S9-verification.spec.md`
records the seed count as already stale by 2026-07-04 (299/233 audit seed drifted to
~404/267); this sweep is a fresh corpus-wide re-measurement per that instruction and
shows the S8 R6 remediation + S9 R8 #9 guard holding at zero.

## Task (d) — shingle scope check (R8 #29)

**LINT-29 self-test (fixture verification: embeds excluded, raw restatements fire)**
```
python3 scripts/lint/lint29_shingle_boundary.py --self-test
```
PASS, 8/8 checks:
- Unit `classify_hit` checks: rule-hit -> HIGH, pin-blockquote -> HIGH,
  pin-para/listitem -> exempt (`None`).
- Fixture sweep over `scripts/lint/fixtures/lint-29/content/` (Demo v. Case.md,
  Rule Home.md / Rule Restate.md, Pin Blockquote.md, Pin Inline.md): exactly **2 HIGH**
  (one `rule`-kind restatement, one `pin`-kind re-typed blockquote), and the inline-woven
  pin fixture (`Pin Inline.md`) produces **0** — confirms raw restatements FIRE and the
  sanctioned inline/list-quote carve-out does not.

**Deeper detector self-test (embed-exclusion asserted directly)**
```
python3 scripts/s8/shingles.py --self-test
```
PASS: "normalize + lcr units; above/below threshold, embed-excluded, same-page-excluded,
quote-zone handling." The dedicated embed-exclusion fixture,
`scripts/s8/fixtures/shingles/already_embed.md`, transcludes foreign rule/pin prose via
`![[...]]` and yields **zero tokens** — `normalize_inplace` blanks embeds by construction
before tokenizing (module docstring: "EMBED-EXCLUDED BY CONSTRUCTION"), so a transclusion
can never itself trigger a hit, independent of the LINT-29-level fixtures. Note: LINT-29's
own `fixtures/lint-29/content/` set does not include a standalone "page that embeds a
foreign rule/pin block" fixture (only rule/blockquote-restate/inline-pin), so the
embed-exclusion guarantee for THIS packet's verification rests on (1) shingles.py's own
`already_embed.md` self-test above (direct, dedicated) and (2) the "Embeds are excluded
from matching BY CONSTRUCTION" property being structural (`shingles.normalize` blanks
`![[...]]` before any tokenization, so LINT-29 never sees embed content at all) rather
than an emergent property that could regress silently between fixture sets.

**Corpus run**
```
python3 scripts/lint/lint29_shingle_boundary.py
```
**Result: 0 violations** (0 high/medium/low) — no real-corpus rule-restatement or
re-typed-blockquote-pin hits at time of this sweep. Raw output:
`_run/s9/p4/out/S8H-A-lint29-stdout.jsonl` (empty), stderr in
`_run/s9/p4/out/S8H-A-lint29-stderr.txt`.

## Adjudication cross-check
`grep -ic 'carat\|shingle\|pin-leak\|num-03\|num03' _run/s9/adjudications.jsonl` = **0**.
Nothing in this packet's scope carries a prior P2/P3 verdict; no
`adjudication-regression` risk to flag.

## Candidates filed
**0.** `_run/s9/p4/out/S8H-A-findings.jsonl` created empty (append-only, ready for future
rows if a later re-run of this packet finds something). Nothing in this sweep met the bar
for a `p4.candidate.v1` row — both lint suites, both self-tests, and both from-scratch
independent scripts agree the corpus is currently clean for NUM-03 and for R8 #29's
embed/restatement boundary.

## Ambiguity for the orchestrator
- The 23 LINT-5 MEDIUM bare-caption rows (listed above) are real, reproducible, and
  already covered by LINT-5's own steady-state gate — they are NOT NUM-03/shingle
  defects and were not filed as candidates by this packet, but are surfaced here in
  case another WS packet's scope (e.g. a linking/glossary lane) should pick them up.
- LINT-29's fixture set has no dedicated "foreign embed present, expect 0 hits" case at
  the LINT-29 level (only at the underlying `shingles.py` level via `already_embed.md`).
  This is a coverage gap in the fixture roster, not a defect in the lint's behavior —
  noting it in case the orchestrator wants a fixture added under
  `scripts/lint/fixtures/lint-29/content/` for defense-in-depth.
