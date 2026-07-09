# S8 CodeRabbit gate — adjudication (base 4c47b72 → HEAD f244451)

- lane: `o2-opus-xhigh` · model: `claude-opus-4-8`
- gate artifact: `_run/gates/S8-coderabbit-f244451.md` (CLI 0.6.5, `--plain --type committed`, code paths only)
- protocol: S7 precedent (`S7-coderabbit-adjudication.md`). Writer ≠ checker: this lane
  emits fixes + proofs; S9 adjudicates.
- findings parsed exhaustively: **23** (2 critical, 15 major, 6 minor).
- verdict: **22 UPHELD (fixed) · 1 REFUTED**. Every UPHELD carries an extended `--self-test`
  case proving the fix; all suites still PASS.
- scope touched: `scripts/**` + regenerated `_run` machine artifacts only. **Zero `content/**.md`
  edits. Zero CourtListener. COMMIT NOTHING.**

## Adjudication table (CR-S8-1 … CR-S8-23)

| # | sev | file:line | verdict | evidence (live code) | fix |
|---|-----|-----------|---------|----------------------|-----|
| CR-S8-1 | minor | fixtures/mentions/zones_exempt.md:15-17 | **UPHELD** | bare ```` ``` ```` fence → MD040 (no language tag). | Labeled the fence ` ```text `. link_cases self-test still finds the "code" zone (fence detection is tag-agnostic). |
| CR-S8-2 | major | assemble_ledger.py:384-395,483-485 | **UPHELD** | If `mentions` is absent/empty or every row lacks `caption_key`, `universe={}`, A/B/C/D all count 0 and `clean` becomes `True` at L484 — R1 certified over zero captions. | `join()` appends `E-empty-universe` when `not universe`; added `E_empty_universe` to the `checks` block. Regenerated join stays CLEAN (real universe 644, `E=0`). |
| CR-S8-3 | major | assemble_ledger.py:265-269 | **UPHELD** | `auto = _load_jsonl(src["mentions"]) or []` swallows an absent/empty mentions set → empty universe reaches `join()`. | `assemble()` records a gap (mirrors the embeds guard) when `not auto`; `join()` then fails closed via CR-S8-2. |
| CR-S8-4 | major | zones.py:287-320 | **UPHELD** | `_first_cell_spans_of_case_table` treated every `(?<!\\)\|` as a column boundary → an aliased first-cell wikilink `[[Terry v. Ohio\|Terry]]` truncated at the inner pipe, leaking the tail to the linkers. | New `_row_pipe_positions()` blanks wikilink-internal pipes before the delimiter scan (header + data rows). Fixture `casecell_aliased.md` proves the tail after both raw and `\|`-escaped aliases stays in `casecell`. **Content-impact: ZERO (see below).** |
| CR-S8-5 | major | shingles.py:371-373,485-491 | **UPHELD** | `sweep()` captures per-file read failures into `stats["read_errors"]` but `main()` always `return 0` → a file silently excluded from source+prose detection, reported as success. | `main()` prints `read_errors` to stderr and `return 1` when non-empty. Self-test: broken symlink → `main()` exits 1. |
| CR-S8-6 | minor | shingles.py:393-399 | **UPHELD** | `os.makedirs(os.path.dirname(out_path), exist_ok=True)` → `os.makedirs("")` raises `FileNotFoundError` for a bare `--out` filename (a documented CLI invocation). | Guard: `if out_dir: os.makedirs(...)`. Self-test writes a bare-name report from a temp cwd. |
| CR-S8-7 | major | lint28_fragments.py:42-50 | **UPHELD** | `_host_ok` accepts `host.endswith("."+s)`; bare `google.com`/`cornell.edu`/`uchicago.edu` admit ANY subdomain (drive.google.com, admissions.cornell.edu), making the narrow Scholar/LII/press-pubs entries dead — a silent widening of the R14 authority gate past the docstring. | Removed the three bare parents (kept the narrow forms). Self-test asserts `drive.google.com`/`admissions.cornell.edu`/`www.uchicago.edu` now REJECT while Scholar/LII pass. Corpus impact: **0** (all 231 fragment URLs are `courtlistener.com`). |
| CR-S8-8 | major | link_terms.py:550-552,472-474 | **UPHELD** | `run()`/`run_unlink()` open content `.md` in `"w"` and write directly — a killed mid-write truncates a corpus page. | New `_atomic_write()` (temp + `os.replace`) at both sites. Self-test asserts correct content + no leftover `.tmp`. |
| CR-S8-9 | minor | link_terms.py:201-230 | **UPHELD** | `except OSError: continue` in `build_page_index` drops unreadable pages silently → `validate_register` later reports "target does not resolve", indistinguishable from a deleted page. | `except OSError as exc: print("WARN: could not read … : %s", file=sys.stderr)`. Self-test: a dir named `*.md` (IsADirectoryError) → WARN emitted, good page still indexed. |
| CR-S8-10 | major | fragments.py:358-365 | **UPHELD** | Ledger written directly with `open(out_path,"w")` — a killed run leaves a partial `s8-fragments.jsonl` a downstream consumer treats as complete. | Atomic temp + `os.replace`. Self-test asserts output present, no `.tmp` left. |
| CR-S8-11 | major | fragments.py:295-335 | **UPHELD** | `glob.glob` over a missing `cases_dir` returns `[]` silently → an empty-but-well-formed output with exit 0, indistinguishable from "genuinely zero pinpoints". | `load_matched_pinpoints` raises `FileNotFoundError` if `not os.path.isdir(cases_dir)`. Self-test asserts the raise. |
| CR-S8-12 | minor | caption_index.py:148-170 | **UPHELD** | Malformed inline `aliases: [...]` → `except Exception: pass` → block-form finds nothing → `parse_aliases` returns `[]`; a page with real-but-broken aliases reads as a page with none ("the WIKILINK TRUTH"). | Warn on inline-JSON parse failure (`source=` passes the filename), then fall through. New `--self-test` proves the WARN + `[]`. |
| CR-S8-13 | major | caption_index.py:233-236 | **UPHELD** | Comment says the year stem "is a variant of the bare form" but code did `e["variants"].add(stem)` — adds the entry's own key to its own variants; downstream `if nv in stem_norms: continue` (L356) always skips it → **no-op**; the bare form was never registered. | `e["variants"].add(m.group(1))` (the bare form). New `--self-test`: a lone year-stem page's bare caption becomes auto-linkable; a genuine bare/year sibling pair stays fail-closed ambiguous. |
| CR-S8-14 | major | caption_index.py:245-265 | **UPHELD** | `except Exception: continue` drops a corrupt lake identity file before `n_lake` increments — a broken record and an absent one are indistinguishable in the index that feeds the R1-R3 linker. | `n_lake_errors` counter + stderr WARN + surfaced in `sources.lake_parse_errors`. Self-test: a broken `.json` is counted (1) and warned. |
| CR-S8-15 | major | remediate_pins.py:312-320,393-416 | **UPHELD** | `_read_jsonl_header` returns `None` on any exception → `verify()` treats a corrupt header identically to "no prior `--write`", silently degrading the count-invariant to "skip", still printing `VERIFY: PASS`. | Returns `(header, corrupt)`; new `_verify_ok(...)` forces FAIL when `header_corrupt`. Self-test: missing→(None,False), corrupt→(None,True), valid→(dict,False); `_verify_ok` truth table. |
| CR-S8-16 | major | remediate_pins.py:62-84 | **UPHELD** | `_begins_new_sentence` returns `True` on ANY opening quote — a mid-sentence quoted phrase (`^pin "reasonable" under…`) opens lowercase yet is mechanically split, the exact "genuinely mid-sentence" case the tool must fail closed on. | Require the quoted text to itself start a sentence (uppercase past emphasis) or fail closed. Fixtures `quote_split.md` (uppercase → split) + `quote_lowercase.md` (lowercase → queue) + a `_begins_new_sentence` unit table. |
| CR-S8-17 | major | link_cases.py:869-916 | **UPHELD** | `--apply-resolutions` branch `return 0` unconditionally, even when `res["bad_target"]` / `res["stale"]` (human-adjudicated links that failed to apply) are non-empty → a gate reads success. | New `_apply_exit_code(res)` = `1 if (bad_target or stale) else 0`; used in `main()`. Self-test: unit truth table + an integration where an unresolvable target surfaces as `bad_target` → exit 1, a `plain` resolution → exit 0. Default `run()` branch left at 0 (queued ambiguity is expected). |
| CR-S8-18 | major | lint7_glossary.py:73-132,216-261 | **UPHELD** | `load_register` drops `skip_phrases`; the coverage scan flags MEDIUM "routed term left unlinked" for wrong-sense occurrences (`vacated the room`, `Washington Post reporter`) the register documents as defects-if-linked. | Carry `skip_phrases`/`skip_rx` per routed term; suppress a coverage match contained in a skip span (mirrors the linker). Fixture `lint-7-skipphrase.md` + self-test (with skip→0 MED, without→1 MED). Corpus effect: **−8 MEDIUM** (see run_all delta), HIGH untouched. |
| CR-S8-19 | minor | link_cases.py:169-182 | **REFUTED** | Claim: `\([^)]*\)\s*$` filter makes year-suffixed captions "invisible to auto-linking". Live evidence: the exclusion is **documented/intentional** — the bare stem catches the name and `(court year)` stays OUTSIDE the wikilink per the exhibit convention `[[People v. Frederick]] (Mich. 2017)`. Of **56** year-suffixed `link_captions`, **54** have the bare form present in `link_captions` (detected + linked) and the **2** exceptions (the `Davis v. United States` 1994/2011 pair) are correctly routed to `ambiguous_captions` (year-sibling fail-close). The proposed fix would emit `[[People v. Frederick (Mich. 2017)]]`, contradicting the convention. With CR-S8-13 fixed, a lone year-stem's bare form is registered too. No mention is invisible. | none (refuted). |
| CR-S8-20 | minor | link_cases.py:196-200 | **UPHELD** | `_PARTY`'s inner alternation `…|[A-Z][A-Za-z.'’&\-]*|[A-Z]\.` — `[A-Z]\.` is subsumed by the earlier greedy `[A-Z][A-Za-z.'’&\-]*` (the `.` is in its class), giving two derivations per initial token; on a long capitalised run without `v.`, `_GENERIC_RE` backtracks catastrophically. | Removed the redundant, language-preserving `[A-Z]\.` (proof: the earlier alt is tried first and its `*` backtracks to the same `X.` boundary — the dead alt never enables a match the greedy path can't reach). Self-test: 40-initial run completes <1s; `Foo v. Bar`, `United States v. Smith`, `J. D. B. v. North Carolina` still match with identical captures. |
| CR-S8-21 | major | link_pincites.py:394-409 | **UPHELD** | The case-page apply loop journals `plain:overlap-skip` (L272-275); the doctrine loop's equivalent `continue` (L399) records nothing — a computed edit vanishes with no ledger/journal row, breaking audit completeness. | Extracted `_apply_doctrine_edits()` which journals `plain:overlap-skip` to both ledger and journal. Self-test drives a synthetic overlapping edit set → overlap-skip rows emitted, one edit applied. |
| CR-S8-22 | **critical** | link_pincites.py:471-509 | **UPHELD** | `all_ledger.extend(ledger)` (L495) runs for every file BEFORE the `--limit` file-write check (L504) → `--write --limit=N` persists `linked-external` rows for files beyond N that were never mutated on disk. Not exercised by `--self-test`. | Restructured `run_cases`: over-limit changed files are NOT written and their `linked*` rows/journal are downgraded to `plain:limit-skipped` before extending; `all_ledger.extend` moved after. Self-test (hermetic temp corpus, redirected ledger globals): `--write --limit=1` writes exactly 1 file; over-limit rows are `plain:limit-skipped`. |
| CR-S8-23 | **critical** | link_pincites.py:563-582 | **UPHELD** | `_emit` rewrites `LEDGER_OUT` unconditionally — a DRY-RUN preview overwrites the canonical rows `assemble_ledger.py` consumes to prove R1, and there is no computed/applied flag. | Gated the whole `_emit` write behind `write` (dry-run is now read-only). Self-test: `run_cases(write=False)` leaves the ledger absent; `write=True` emits it. |

## Content-impact finding (CR-S8-4 zone-fix audit)

Scanned all 724 content files: every case-table first cell honoring `[[...]]` boundaries.

- case-table first cells with an **escaped** aliased wikilink `[[X\|Y]]`: **0**
- case-table first cells with an **unescaped** aliased wikilink `[[X|Y]]`: **0**
- case-table first cells with a **nested/corrupt** `[[…[[…]]` link: **0**

No live corpus case-table first cell contains an aliased wikilink at all (they carry bare
`[[Terry v. Ohio]]` links or plain text). The truncation bug is a **latent logic defect with
ZERO live content impact**; no linker wrote a link into a formerly-truncated tail. **No
content-impact findings; no content edits made.**

## Re-run gate outputs

### Self-tests (every touched script) — 11/11 PASS
```
PASS  s8/zones.py            (9 zone kinds + casecell aliased-wikilink tail)
PASS  s8/shingles.py         (read_errors→exit1, bare --out makedirs guard)
PASS  s8/assemble_ledger.py  (A/B/C/D/E-empty-universe fail-paths, absent-mentions gap)
PASS  s8/caption_index.py    (NEW self-test: alias-warn / year-stem bare variant / year-sibling / lake parse-error)
PASS  s8/fragments.py        (missing-lake raise, atomic ledger write)
PASS  s8/remediate_pins.py   (quote-split / quote-lowercase-queue / begins-sentence unit / jsonl-header absent-vs-corrupt)
PASS  s8/link_terms.py       (_atomic_write, build_page_index unreadable WARN)
PASS  s8/link_cases.py       (_GENERIC_RE linear + semantics, apply-resolutions exit code)
PASS  s8/link_pincites.py    (doctrine overlap-journal, --limit ledger-gate, dry-run read-only)
PASS  lint/lint7_glossary.py (skip_phrases suppress: skip→0 MED / no-skip→1 MED)
PASS  lint/lint28_fragments.py (subdomain rejection: drive.google/admissions.cornell/uchicago bare)
```

### assemble_ledger + `--join` (R1 proof) — CLEAN, exit 0
```
ledger: _run/s8-link-ledger.json
  mentions 14184 (auto 14183 + adjudicated 187) | embeds 4 | pincites 964 | terms pages 539
join: _run/o2-execute/s8-coh15-join.json
  NUM-04 re-derived distinct captions: 644 (page-backed 595, non-page 49; seed 388)
  checks: {"A_authored_plain": 0, "B_plain_uncited": 0, "C_resurrected": 0, "D_dangling": 0, "E_empty_universe": 0}
  clean: True
join exit: 0
```
The new `E_empty_universe` join key (CR-S8-2) PASSES on the real corpus (universe = 644 captions,
non-empty). Machine artifacts `_run/s8-link-ledger.json` and `_run/o2-execute/s8-coh15-join.json`
regenerated (permitted `_run` artifacts).

### run_all (full content sweep) — zero-new-HIGH
```
                    TOTAL   HIGH   MED   LOW
baseline (f244451)   4184   3381   782    21
after fixes          4176   3381   774    21   (run_all exit 1 == pre-existing HIGH, unchanged)
```
**HIGH unchanged (3381 → 3381).** The only delta is **−8 MEDIUM in LINT-7**, entirely from
CR-S8-18 (a lint-code change; content untouched):

| surface | before | after | Δ | cause |
|---------|--------|-------|---|-------|
| `vacated` | 10 | 3 | −7 | wrong-sense `vacated the room/premises` occurrences now suppressed by register `skip_phrases` |
| `reporter` | 12 | 11 | −1 | `Washington Post reporter` occurrence now suppressed |

These are the only two register terms carrying `skip_phrases`; no other surface changed. LINT-28
(CR-S8-7) delta = 0 (all 231 corpus fragments are `courtlistener.com`, unaffected by narrowing).

### `npx quartz build` — green, exit 0
```
Found 724 input files from `content`
Parsed 724 Markdown files
Emitted 2873 files to `public`
Done processing 724 files
build exit: 0
```

## Notes for the machine (S9)

- **caption_index artifact NOT regenerated (CR-S8-13/14/12).** The code fixes are forward-looking;
  the committed `_run/o2-execute/s8-caption-index.json` was produced by the pre-fix code and is
  consumed by the committed `s8-link-ledger.rows.mentions.jsonl`. Regenerating only the index would
  desync it from the mentions ledger (which is NOT re-run here) and would also churn a pre-existing
  set-ordering non-determinism in the index (str-hash-randomized `short_names`/`collision_map` key
  order — observed 92/92 line reshuffle on a no-op re-run; **out of gate scope, not a finding**).
  The bare-variant/lake-error/alias-warn behaviour takes effect on the next full pipeline re-run
  (`caption_index → link_cases → assemble`), which the join re-derivation does not require: the join
  reads `entries[cap]` by exact caption_key + S6, and the newly-registered bare variants are not
  themselves mention `caption_key`s, so page_backed/nonpage_terminal for the fixed universe is
  unchanged (join stays CLEAN).
- **CR-S8-16 (remediate_pins heuristic)** was proven hermetically; the R6 pin pass is not in
  f244451's ancestry, so no committed R6 artifact depends on it. The change is strictly more
  fail-closed (opening-quote-lowercase → queue, never auto-split).
```
```
