# RETRO Dispatch A + S2-gate lint additions — fix-lane report

- lane: `{lane: o2-execute-lint, model: claude-opus-4-8}`
- date: 2026-07-06
- scope owned: `scripts/lint/` EXCEPT `lint12_drift.py` / `lint13_schema.py` / `lint14_pagerecord.py` (sibling S2 lane). Those three show working-tree diffs from the **sibling lane**, not me (verified: I never edited them). `lint23`/`lint26` untouched.
- sources of law: `_run/o2-execute/RETRO-W0W1-WORKORDER.md` (Dispatch A) · `_run/gates/RETRO-W0W1-lint-coderabbit-597bb3f.md` (exact findings) · `_run/gates/S2-coderabbit-50ef21f.md` (S2-gate additions) · `_overhaul2/specs/S3-taxonomy.spec.md` R9 · `quartz/util/path.ts`.

## Counts

- **FIXED: 24 findings** · **REFUTED: 1** (lint26 `_index`) · **new live-corpus catches from my fixes: 0**
- `run_all.py --quiet` → **exit 1** (unchanged from baseline; the pre-overhaul + mid-S2 corpus is red by design). Self-test gate (LINT-10/12/13/14) all PASS.
- All 14 self-test suites green (9,10,12,13,14,15,16,18,19,20,21,22,24,25). LINT-9 gained a self-test harness (had none).

## Live-corpus delta (baseline captured at session start vs. after)

Per-lint byte-level diff of the full `run_all` JSON output: **every lint I touched = 0 added / 0 removed.** The only run_all delta is:

- **LINT-6 +2 HIGH** on `content/cases/Entick v. Carrington.md` and `content/cases/Wilkes v. Wood.md` (`treatment 'unverified' but not draft`). **NOT MINE** — I do not own lint6 and never edited it. Isolation test: the +2 **persists with my `_common.py` reverted**, so it is a **concurrent content-projection artifact** (the sibling S2 lane re-projected these two case pages to `field_i_validity: unverified` / `status: not_found`; consistent with the recent "Entick v. Carrington not_found adjudicated TRUE" commit). **No adjudication of mine required.**

**Net: my changes introduced zero new live HIGHs.** Every fail-open→fail-closed hardening (lint18 empty-tree, lint19 stub/table + cases-exemption, lint20 also_on, lint21 corrupt/empty-nodes, lint24 non-string, lint25 corrupt-deck, lint16 host/short-row, lint9 filler, lint4 fenced-guard) caught **nothing** in the live corpus because the live artifacts are all well-formed. Nothing on this list needs your adjudication.

## Per-finding adjudication

### WORK ORDER 1 — Dispatch A

| # | Finding (file:loc) | Verdict | Note |
|---|---|---|---|
| 1 | lint21:168 empty-`nodes` bound row bypass (**critical**) | **FIXED** | `if slug in slug_map` → `if slug_map.get(slug)`; empty list is falsy → falls through to HIGH. |
| 2 | lint21:74-78 silent corrupt-file skip (**critical**) | **FIXED** | `collect_lake_overrides` now returns `(overrides, unreadable)`; `run()` surfaces each unreadable file as HIGH. |
| 3 | lint21:75 unclosed file handle (**major**) | **FIXED** | `with open(f, …) as fh: json.load(fh)`. |
| 4 | lint16:83-94 `_host()` userinfo bypass (**major, security**) | **FIXED** | rewrote `_host` to `urlsplit().hostname` + scheme check (try/except ValueError). Proof: OLD `_host("https://www.courtlistener.com:x@evil.com/…")` returned `www.courtlistener.com` (passed whitelist); NEW returns `evil.com` (rejected). |
| 5 | lint16:228-261 short rows + hostless URLs skip whitelist (**major**, companion) | **FIXED** | short row missing the Opinion cell → HIGH; empty host (`https:///…` / non-http) merged into the R17 check via `if not host or not _host_ok(host)`. |
| 6 | lint18:64-81 empty/missing content tree fail-open (**major**) | **FIXED** | unscoped run with zero markdown files → one HIGH (fail-closed); scoped runs may legitimately match zero, so guarded to the unscoped path only. |
| 7 | lint18:50-52 outside-root paths miscounted (**minor**) | **FIXED** | `_check_path` skips paths whose relpath is `..`-prefixed or absolute (not a taxonomy node). |
| 8 | lint19:47-54 `cases/*` exemption over-broad (**major**) | **FIXED** | `rel.split("/")[0]=="cases"` → `rel=="cases/index.md"` (spec/docstring exempt only the R13(d) router landing). Zero live delta (no `content/cases/*/index.md` exist). |
| 9 | lint19:65-80 table rows counted as prose (**minor**) | **FIXED** | prose counter now excludes table lines (header+separator+rows via `iter_tables`). Red-before proof: a table-only body counted 4 "prose" lines (false pass); now 0 → stub HIGH. |
| 10 | lint22:46-62 BANNED_TITLES missing slash-combined originals (**major**) | **FIXED** | added `"What is a Search/Seizure?"` and `"PC needed / PC not needed"` (R9 line 119 verbatim; matches CodeRabbit patch). |
| 11 | lint24:150-159 all-non-string `paths` fail-open (**major**) | **FIXED** | each non-string entry → HIGH; `checked==0` guard → HIGH (never a resolved state on zero real paths). |
| 12 | lint25:60-76 corrupt deck JSON silently dropped (**major**) | **FIXED** | `deck_stems` returns `(stems, errors)`; `check_decks` surfaces each load failure as HIGH; also `with open(...)`. |
| 13 | lint20:137-144 malformed `also_on` silent (**major**) | **FIXED** | non-list `also_on` → HIGH; non-string/empty list entry → HIGH (matches CodeRabbit patch). |
| 14 | lint4:217-233/382 lane (b) `_table_rows` no fenced guard (**major**) | **FIXED** | `_table_rows(…, fenced)`; call passes `fenced`. Red-before: OLD saw 2 data rows inside a ``` fence; NEW `check_file` on a fenced example weight table → 0 violations. |
| 15 | lint7:63-67 UnicodeDecodeError escapes OSError guard (**minor**) | **FIXED** | `except (OSError, UnicodeDecodeError)`. Proof: `load_register` on invalid-UTF-8 bytes now returns the fail-closed message instead of crashing. |
| 16 | lint26:113-132 `_index` suffix diverges from Quartz (**minor**) | **REFUTED** | CodeRabbit claims Quartz rewrites `foo_index`→`fooindex`. **False.** `quartz/util/path.ts:83` guards with `endsWith(slug,"_index")` = `slug==="_index" \|\| slug.endsWith("/_index")` (path.ts:269-271), so `foo_index` is **not** rewritten. lint26's guard (`slug=="_index" or slug.endswith("/_index")`) + `slug[:-len("_index")]+"index"` is byte-identical to Quartz's guarded `.replace(/_index$/,"index")`. **Applying the suggested "fix" would INTRODUCE a divergence** (wrongly rewriting `foo_index`). The code comment already documents this exactly. No change. |
| 17 | run_all.py:3 docstring roster stale | **FIXED** | now enumerates LINT-…,18,19,20,21,22,23,24,25,26 + S3 repo scans. |
| 18 | README:34 runner row / roster omits 18-25 | **FIXED** | added mapping-table rows for LINT-18…25 + reworded run_all row. |
| 19 | fixtures/lint-3-n5.md:47-49 Sources incomplete | **FIXED** | added `*[[Torres v. Madrid]]*` and `*[[Chatrie v. United States]]*` Sources bullets, grounded in citations already asserted in the body + existing case pages. **No fabricated URLs/cites** (cannot call CL; both cases already have pages). |

### WORK ORDER 2 — S2-gate additions

| # | Finding | Verdict | Note |
|---|---|---|---|
| 20 | lint9:51-63 fill char `'x'` inside anchor class (**major**) | **FIXED** | filler `'x'`→`'#'` (outside `[A-Za-z0-9-]`). Fixture reproduces `See rule ^pin-3[[Terry v. Ohio]]` → HIGH; red-before proof: OLD `'x'` filler → 0 violations (false negative). Added self-test harness + `--self-test`. |
| 21 | lint15:175-195 missing-vs-misplaced `[!rule]` folded (**major**) | **FIXED** | split into `callout_line is None` (missing) vs `callout_line >= first_h2_line` (after-first-H2, new distinct message + line). |
| 22 | lint15:196-202 `.title()` wrong display name (**major**) | **FIXED** | `REQUIRED_DOCTRINE_H2_DISPLAY` map → `"Key cases"` (not `"Key Cases"`). |
| 23 | _common.py:441 `is_table_row`/`iter_tables` unmasked pipes (**major**) | **FIXED** | new `_has_cell_pipe` mirrors `split_table_row`'s wikilink/code/escape masking; `is_table_row` requires an unmasked cell pipe. Red-before proof: `This [[Terry v. Ohio\|ruling]] is a landmark case.` + a separator line was read as a Case-table header → 1 HIGH; now 0. (Also improves `scripts/s5/convert_tables.py`, which shares `iter_tables` — a correctness win, consistent with its existing use of `split_table_row`.) |
| 24 | lint16 empty-host `if not host or not _host_ok(host)` | **FIXED** | merged with #4/#5 (single edit). |
| 25 | lint16:20 unicode `∪`→ASCII `or` (**minor**) | **FIXED** | docstring reworded. (Left `∈` — CodeRabbit did not flag it and the suggested edit keeps it.) |

## Fixtures added (13)

- `lint-21-binding-emptynodes-fail.yaml` — bound row with empty `nodes` → HIGH
- `lint-21-lake-corrupt/bad.json` — corrupt lake case file → surfaced HIGH
- `lint-16-userinfo-fail.md` — userinfo-bypass host + hostless `https:///` + short row (3 viols)
- `lint-16-prosepipe-pass.md` — wikilink-pipe prose not mis-read as a table (pass; _common masking)
- `lint-9-anchor-wikilink-fail.md` — `See rule ^pin-3[[Terry v. Ohio]]` mid-line leak → HIGH
- `lint-9-endline-pass.md` — end-of-line anchors + wikilink anchor ref + footnote (pass)
- `lint-15-callout-afterh2-fail.md` — `[!rule]` after first H2 → the new distinct message
- `lint-18/empty/.gitkeep` — empty content root → fail-closed HIGH
- `lint-19-table-only-stub-fail.md` — table-only body → stub HIGH (non-case table isolates the prose-count fix)
- `lint-20-registry-badalso-fail.yaml` — `also_on` as a bare string → HIGH
- `lint-22-slashcombined-fail.md` — title `"What is a Search/Seizure?"` → HIGH
- `lint-24-inventory-nonstring.json` — `paths:[123,456,{…}]` → HIGH
- `lint-25-decks-corrupt/{good,bad}.json` — corrupt deck among healthy siblings → HIGH

## Self-test outputs (post-fix)

```
lint9: PASS   lint10: PASS  lint12: PASS  lint13: PASS  lint14: PASS
lint15: PASS  lint16: PASS  lint18: PASS  lint19: PASS  lint20: PASS
lint21: PASS  lint22: PASS  lint24: PASS  lint25: PASS
```

New/extended self-test cases: lint21 (empty-nodes bypass, corrupt lake file), lint16 (userinfo/hostless/short-row, prose-pipe pass), lint9 (whole harness new), lint15 (callout-after-H2), lint18 (empty root, outside-root), lint19 (table-only stub), lint20 (bad also_on), lint22 (slash-combined), lint24 (all-non-string), lint25 (corrupt deck among siblings).

## Notes / non-improvisation

- Message-text was refined on several lints (lint15 callout split, lint16 short-row/host, lint19 stub, lint20/21/24/25 fail-closed messages). This changes the human-facing `message` field only — the `{lint, severity}` vocabulary S9 keys on is unchanged; the S2-gate work order explicitly requested the lint15 split into "two distinct violations." No severity or lint-id changed.
- lint22's `_is_overview_index` has the same `cases/*` over-broad pattern as lint19's (finding #8), but CodeRabbit flagged only lint19 and it has zero live impact; left unchanged to stay within the adjudicated scope. Flagged here for your awareness.
- `run_all.py` exit remained 1 (baseline was 1) — expected; the corpus is red by design pre-S7/S8.
