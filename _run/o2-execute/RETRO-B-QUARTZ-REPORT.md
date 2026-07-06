# RETRO Dispatch B + S2-gate quartz additions — fix report

- lane: `{lane: o2-execute-s5-quartz-fix, model: claude-opus-4-8}`
- date: 2026-07-06
- ownership honored: touched ONLY `scripts/s5/`, `_overhaul2/scripts/audit_cases.py`,
  `quartz/` (components/styles/layout), `quartz.layout.ts`. NOTHING under `scripts/s2/` or
  `scripts/lint/`.
- discipline: find -> adjudicate -> fix; each item verified against code before patching.

## Counts

- findings adjudicated: 10 (grouped) — **10 FIXED, 0 REFUTED**
- files changed: 8 (`git diff --stat`: 91 insertions, 25 deletions)
- verification: tsc `--noEmit` exit 0 · convert_tables self-test PASS · convert_tables
  exit-code matrix 2/1/0 correct · quartz build exit 0 (571 files, 2050 emitted) ·
  py_compile OK (both .py) · my edits add ZERO new prettier violations.

---

## WORK ORDER 1 — Dispatch B (S5 converter, `scripts/s5/convert_tables.py`)

### B-1 CONFIRMED critical — `main()` unconditional `sys.exit(0)` — FIXED
`main()` caught per-page exceptions, recorded a `{page, error}` row, and then called
`sys.exit(0)` at the tail regardless of errors; an empty `paths` (bad glob) also exited 0,
indistinguishable from a clean run. Adjudication: CONFIRMED against code (old line 565).
Fix applied:
- added `n_errors` counter, incremented on each per-page exception;
- summary line now prints `%d error(s)` (Dispatch B: "count and print n_errors");
- exit is now fail-closed: `exit 2` on empty page set (with a "no pages matched" note),
  `exit 1` on any per-page error, `exit 0` only on a non-empty clean run.

Verified (temp fixtures):
```
(1) bad glob        -> "[convert] no pages matched the given path(s)/glob(s)"  exit 2
(2) broken symlink  -> "[convert] ERROR ...: No such file..."                  exit 1
(3) clean 1-page    -> "[convert] 1 page(s): 0 would change (dry-run)..."      exit 0
(combined 1 ok + 1 err) -> exit 1
```

### B-1b consistent report shape — FIXED
The error report row was `{page, error}` — missing the `changed/actions/deferred` keys every
success row has, so downstream `r.get("actions")` / `r["changed"]` iteration was uneven. Fix:
the error row now carries `{page, changed:False, actions:[], deferred:[], error:str(e)}` — a
superset of the success shape (uniform keys + an explicit `error` marker). Verified via
`--report-json`: success row keys `[actions, changed, deferred, page]`; error row is the same
set plus `error`.

### B-2 minor — `dropped_columns` under-reports — FIXED
`dropped = sorted({k for k in kinds if k in ("weight","treatment","year")})` (old line 121)
only counted the three data roles. The schema rewrite drops EVERY source column whose role is
not in the target schema's `order` (e.g. an unmapped `other`/`Notes` column is silently lost).
Adjudication: CONFIRMED (`classify_case_header` maps date->`year`, so date is covered by
`year`, but any non-schema role was uncounted). Fix: `order_set = set(order)` then
`dropped = sorted({k for k in kinds if k not in order_set})` — reports all stripped roles; a
strict superset of the old output for the three data roles, so no regression. Self-test PASS
(schema rewrite unchanged).

---

## WORK ORDER 1 — Dispatch C ("any quartz dispatch section": quartz)

### C-1 major (a11y) — `casetable.scss` pill has `:hover` but no `:focus-visible` — FIXED
`a.casetable-pill` is now a real interactive anchor (S4 R5) with a `:hover` brighten but no
keyboard focus indicator. Adjudication: CONFIRMED (repo has no other focus-ring convention;
only `outline:0`/`none` elsewhere). Fix: added `&:focus-visible { outline: 2px solid
var(--secondary); outline-offset: 2px; }` (matches Quartz's `--secondary` accent usage). Note:
the fix pairs with S2-gate (b) below — when `goodLawHref` is absent the pill degrades to a
`<span>` (non-focusable), and the `a.casetable-pill` selector correctly applies the ring only
to the interactive anchor form.

### C-2 minors — bare `//` empty comment + `currentColor` casing — FIXED
Same file items as S2-gate (d); fixed once (see below).

### C-3 minor — `spa.inline.ts` `flashTargetBlock` `decodeURIComponent` throw — FIXED
`document.getElementById(decodeURIComponent(hash.substring(1)))` throws a `URIError` on a
malformed `%`-hash (e.g. `#%E0%A4`). Adjudication: CONFIRMED — the call at the same-page click
path (line 169) runs AFTER `event.preventDefault()` (line 166) and is NOT inside the
`navigate()` try/catch, so a malformed hash would silently break navigation with an unhandled
rejection. Fix: wrapped the decode in try/catch inside `flashTargetBlock`; on failure it
returns `null` (no target) instead of throwing, protecting both call sites (line 110 and 169).
tsc clean; prettier clean.

---

## WORK ORDER 2 — S2-gate additions (`_run/gates/S2-coderabbit-50ef21f.md`)

### (a) `casetable.inline.ts` ~266-273 — case-name sort picks the injected pill anchor — FIXED
`sortValue`'s `case "case"` used `cell.querySelector("a, em, i")?.textContent`. When the case
name is plain text (no link/em/i) and `injectCaseMeta` appended the treatment PILL anchor, that
pill was the only `<a>` in the cell, so the sort value became the treatment label — breaking
the case-column sort for exactly the rows it was meant to protect. Adjudication: CONFIRMED.
Fix: rewrote the arm to (1) prefer the first `a/em/i` that is NOT inside the injected
`.casetable-case-meta` span, and (2) for a plain-text name, sum the cell's child-node text
excluding the meta node — never the pill's label. Reuses the outer `cell`/`txt` (no shadowing);
`Array.from(...)` used for NodeList iteration for target-safety. tsc clean; prettier clean.

### (b) `casetable.inline.ts` ~162-174 — treatment pill = dead `<a href="#">` — FIXED
`index.goodLawHref` is optional; when absent the pill still rendered as
`<a class="internal ..." href="#">`, scrolling-to-top on click. Adjudication: CONFIRMED. Fix:
`document.createElement(index.goodLawHref ? "a" : "span")` and set `href` only when known
(`if (index.goodLawHref && pill instanceof HTMLAnchorElement) pill.href = index.goodLawHref`).
The `HTMLAnchorElement | HTMLSpanElement` union type-narrows correctly; all other pill mutations
(`className`, `title`, `dataset`, `appendChild`) are valid on both. tsc clean.

### (c) `quartz.layout.ts` ~30-33 — explorer `filterFn` hides homonyms at any depth — FIXED
`FileTrieNode.filter` recurses onto every node, so the bare `slugSegment !== "tags"/"about"/
"cases"` test would also hide any NESTED page/folder named about/tags/cases. Adjudication:
CONFIRMED (`fileTrie.ts` `filter()` recurses children). Fix: scope to top-level only — a
top-level node's full `slug` is exactly its own segment (a file) or `<segment>/index` (a
folder), so `topLevel = node.slug === node.slugSegment || node.slug === \`${node.slugSegment}/
index\``; hide only when `named && topLevel`. Closure-free (only reads `node`), so it still
serializes to the client. Verified: top-level cases (`cases/index`)/about/tags hidden; nested
`1-foundations/cases` kept. tsc clean; build clean.

### (d) SCSS minors — FIXED
- `custom.scss`: inserted a blank line before the 4 `//` comments that directly followed a
  declaration/brace (the two in `.explorer .explorer-content`, and the tree-connector comments
  after `&::before`/`&::after`) — `scss/double-slash-comment-empty-line-before`.
- `casetable.scss`: standalone empty `//` (line 6) replaced with a genuine blank line
  (preserves the paragraph break while clearing `scss/comment-no-empty`); `background:
  currentColor` -> `currentcolor` (`value-keyword-case`).
- `treatmentBadge.scss`: standalone empty `//` (line 5) -> blank line.
Adjudication: CONFIRMED the offending source exists as described.

### (e) `audit_cases.py` ~623-626 — `assert` stripped under `-O` — FIXED
`assert_no_page_collisions` used a bare `assert` — the last-line collision guarantee would be
compiled out under `python -O`/`PYTHONOPTIMIZE`, silently passing a colliding roster.
Adjudication: CONFIRMED. Fix: `if index.match(...) is not None: raise AssertionError(...)`.
py_compile OK.

---

## Observations (NOT fixed — out of scope / not a regression)

- **No active stylelint gate**: the repo has no `.stylelintrc*` and `package.json`'s `check`
  script is `tsc --noEmit && npx prettier . --check` (no stylelint). The (d)/(C-2) SCSS lint
  fixes are therefore forward-looking — they align the source with the stylelint rules
  CodeRabbit assumes but do not currently fail any live gate. Applied per work order; harmless.
- **Pre-existing prettier debt (baseline, left untouched)**: `git show HEAD:` shows both
  `quartz.layout.ts` (the multi-line `afterBody` array) and `casetable.inline.ts` (`?
  FIELD_I_LABELS[v] ?? v :` needing `(...)` under prettier 3.6.2) were ALREADY prettier-dirty
  before my edits — the repo was formatted under a different printWidth. I reformatted only my
  OWN new `filterFn` lines to prettier's form so I add zero new violations; I deliberately did
  NOT run `prettier --write` on the whole files (it would collapse unrelated pre-existing lines
  and muddy the diff). Flagging for a separate formatting pass if the `check` gate is enforced.

## Verification transcript (key lines)

```
npx tsc --noEmit                                  -> exit 0
python3 scripts/s5/convert_tables.py --self-test  -> [self-test] PASS  exit 0
convert_tables exit matrix                        -> empty:2  error:1  clean:0  combined:1
report-json shape  success:[actions,changed,deferred,page]  error:+[error]
py_compile convert_tables.py audit_cases.py       -> OK
npx quartz build --output /tmp/qz-verify          -> Done processing 571 files  exit 0
prettier (my additions)                           -> 0 new violations (2 pre-existing baseline)
```
