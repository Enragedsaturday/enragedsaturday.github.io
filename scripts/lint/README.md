# CSSI automated LINT roster

Deterministic lint scripts for the CSSI overhaul, implementing the enforcement
model of **S1 §3.H** (the `LINT-1…8` table). Standard-library Python 3 only —
no pip installs (the repo already runs `python3` for flashcards).

Every lint:

- recursively scans `content/**/*.md` (keeps working after the S2 folder
  restructure — scanning is recursive, link/anchor resolution indexes the whole
  corpus regardless of scoping);
- is tolerant of the **pre-overhaul** corpus — it reports many violations today;
  that is *informational*, not a tooling failure;
- prints violations as **JSON lines** — `{lint, file, line, severity, message}`
  — and exits **non-zero** if any `high`-severity violation is found;
- accepts an optional path/glob arg to scope to a subset, e.g.
  `python3 lint5_link_every_case.py "content/Curtilage.md"`.

## Rule → lint mapping (S1 §3.H)

| Script | Lint | Enforces | What it checks |
|---|---|---|---|
| `lint1_cl_identity.py` | **LINT-1** | **L3, D7** | Every CourtListener `opinion_url`/`opinion_id` (frontmatter) and CL opinion URL (prose) resolves **HTTP 200** *and* the returned cluster names the case (identity — cluster-id ≠ opinion-id). **WRITE-ONLY / serial-CL-gate-only — see below.** |
| `lint2_quote_pinpoint.py` | **LINT-2** | **L1, D7** | Every block quotation and every substantial inline quotation has a pinpoint cite nearby (else de-quote / pin). |
| `lint3_structure.py` | **LINT-3** | **N5, N8, D10** | Brief-first doctrine section-order presence; **no SCOTUS case in a "Recent developments" section**; a single controlling amendment in frontmatter. |
| `lint4_lexicon.py` | **LINT-4** | **N2, D6** | Every authority/weight label is one of the six S1 §3.D tiers; bans `"persuasive, not binding"`; circuit labels name the circuit. |
| `lint5_link_every_case.py` | **LINT-5** | **N7, D13** | Every named case (`Foo v. Bar`) resolves to a `[[wikilink]]` (no bare names); every `[[Page]]` / `[[Page#anchor]]` target resolves to a page/anchor in the corpus. |
| `lint6_treatment_status.py` | **LINT-6** | **N13, D3** | Every `type: case` page carries a non-blank `treatment.status` + `as_of`; every Case-Index row has a non-blank treatment cell. |
| `lint7_glossary.py` | **LINT-7-AUTO** | **N11, D13** | The automatable half of S7·R10 (a–d): `[[Common Legal Terms#x]]` / `[[Reading and Citing Cases#x]]` anchors resolve; no term linked >1×/page. *(Novel-term discovery + definition accuracy are CHECKLIST-only — S1 §9.)* |
| `lint8_guardrails.py` | **LINT-8** | **D6** | No apocryphal Holiday/McCall(/Smith) trio (the real `United States v. Smith` geofence case is legit); mnemonics carry no citation; no inline `## Flashcards` heading. |
| `lint9_carat_leak.py` | **LINT-9** | **L1, D7, D13** | Carat-leak: `^pin-N` block-ref anchors must never render as visible text — zero MID-LINE block anchors (end-of-line anchors are masked by Quartz and legal). Content remediation of the existing ~300 leaks is S8 R6's; this is the steady-state guard (S9 R8 #9). |
| `lint10_emdash.py` | **LINT-10** | **SR-13, D9** | Prose em-dash budget (S1 A7/A8): unit = block (paragraph/list item); >1 per block or 2+ per sentence fails; direct quotations, controlled labels, and `[!rule]` callouts exempt. Ships `fixtures/lint-10.md` + `--self-test` (run fail-closed by the runner). |
| `lint12_drift.py` | **LINT-12** | **S2 R12/A13** | Case-page managed frontmatter must deep-equal the S2 lake projection by parsed value; draft pages exempt; unmapped legacy treatment blocks projection. |
| `lint13_schema.py` | **LINT-13** | **S2 R1/R13/A5/A16** | S2 authority records parse and satisfy the live `_overhaul2/lake/_schema.json`; the stdlib schema interpreter fails closed on unsupported schema keywords and self-tests keyword coverage. |
| `lint14_pagerecord.py` | **LINT-14** | **S2 R12/A16** | Every non-draft `type: case` page resolves to a lake record whose status is `verified`, `under_review`, or `verified_off_cl`; records need not have pages. |
| `lint18_depth.py` | **LINT-18** | **S3 R1/R10** | Depth cap — the tree nests no deeper than category → sub-umbrella → page (folder depth ≤ 2); a 4th level is HIGH. `cases/`, `tags/` exempt. Fail-closed on a missing/empty content root. (Alias `LINT-S3-depth`; S9 R8 row 18.) |
| `lint19_overview.py` | **LINT-19** | **S3 R2** | Every category / sub-umbrella `index.md` overview carries an authored, non-stub body (≥ 2 non-table prose lines) and **no** case table. Exempts only `content/index.md` + `content/cases/index.md`. (Alias `LINT-S3-overview`; S9 R8 row 19.) |
| `lint20_points.py` | **LINT-20** | **S3 R4** | Point-of-law `registry.yaml` schema/grammar/uniqueness; every `home_page`/`also_on` resolves on disk (malformed `also_on` fails closed). Missing registry ⇒ HIGH. (Alias `LINT-S3-points`; S9 R8 row 20.) |
| `lint21_binding.py` | **LINT-21** | **S3 R5** | `s2-binding.yaml` resolves every live lake point-override slug to ≥ 1 registry node (empty `nodes` ≠ bound); no dangling node ids; corrupt lake case files surface as HIGH. (Alias `LINT-S3-binding`; S9 R8 row 21.) |
| `lint22_derip.py` | **LINT-22** | **S3 R9** | No category / sub-umbrella label reproduces a banned (Bandiero / retired-split) part title, incl. the slash-combined originals. (Alias `LINT-S3-derip`; S9 R8 row 22.) |
| `lint23_order_weight.py` | **LINT-23** | **S3 R10/A8c** | Intra-category ordering weights are present, integer, and non-negative. (Alias `LINT-S3-order`; S9 R8 row 23.) |
| `lint24_urls.py` | **LINT-24** | **S3 R13/A1** | The pre-move URL inventory exists, is non-empty, and every path resolves against the current build output (`public/`); zero retired old-path references remain in source. Build-guarded (MEDIUM + skip if `public/` absent). (Alias `LINT-S3-urls`; S9 R8 row 24.) |
| `lint25_deck.py` | **LINT-25** | **S3 R14/A2** | Every frozen flashcard-deck `page` stem resolves to an emitted page stem or bare-stem alias; corrupt deck JSON fails closed. (Alias `LINT-S3-deck`; S9 R8 row 25.) |
| `lint26_goodlaw_target.py` | **LINT-26** | **S4 R5** | The exported `GOOD_LAW_SLUG` constant (treatment-pill target) is the EXACT Quartz FullSlug of a real content page — a stale path fails the build instead of shipping dead pill links. (Alias `LINT-S4-goodlaw-target`; S9 R8 row 26.) |
| `run_all.py` | runner | — | Runs the **non-CL** lints (2–10, 12–14, 18–26) over `content/` plus the S3 repo scans, LINT-10/12/13/14 self-tests first (fail-closed), and prints a per-lint violation summary. |
| `_common.py` | shared lib | — | Frontmatter parsing (stdlib YAML subset), corpus page/anchor index, shared regexes, JSON-line emission. |

## LINT-1 is serial-CL-gate-only (L4)

`lint1_cl_identity.py` is the **only** lint that touches the network, and it is
**not run by `run_all.py`**. All CourtListener traffic in the project is
concurrency-1, **always** (S1 **L4**). LINT-1:

- collects its references with **no network I/O** (importable / testable);
- **refuses** to make any CL call from the CLI unless the operator passes the
  explicit serial-lane flag `--i-am-the-serial-cl-lane`;
- paces serially (sleep between every call, target 15/min, well under 20/min)
  and is checkpointable via `--ledger=…`.

> RUN ONLY THROUGH THE SINGLE SERIAL CL LANE AT THE GATE — never in parallel,
> never alongside another CL caller. It is authored here but executed later,
> once, by the serial lane at the publish gate.

```
# serial lane only:
python3 lint1_cl_identity.py --i-am-the-serial-cl-lane --ledger=cl-ledger.json
```

## Usage

```
python3 run_all.py                 # non-CL roster over all of content/
python3 run_all.py --quiet         # summary table only (no per-violation JSON)
python3 run_all.py "content/Curtilage.md"   # scope to a subset
python3 lint4_lexicon.py [glob…]   # run a single lint standalone
```

Exit code is non-zero when any `high`-severity violation is present, so the
roster can gate `redeploy.sh` / CI (SR-4).

## Severity convention

- **high** — unambiguous, build-gating (e.g. SCOTUS case in Recent developments;
  banned `"persuasive, not binding"`; broken wikilink target; inline
  `## Flashcards`; apocryphal trio; CL non-resolution/identity mismatch).
- **medium** — content fix needed but not mechanically certain (bare case name,
  quote missing pinpoint, non-tier weight label, blank Case-Index treatment).
- **low** — informational / pre-overhaul structural drift (missing canonical
  section, no/multiple controlling amendment, duplicate glossary link).

## Format assumptions

- Wikilinks `[[Page]]` / `[[Page#anchor]]` / `[[Page#^block]]` / `[[Page|alias]]`
  resolve by **basename** (Quartz convention), plus frontmatter
  `title`/`topic`/`aliases`.
- Anchors are H2–H6 heading slugs (GitHub/Quartz slugging) plus `^block` ids.
  Glossary **terms are currently bold-led, not headings**, so term-level anchors
  do not exist pre-S7; LINT-7's anchor check lights up once S7 introduces the
  anchored term scheme.
- A pinpoint cite is a reporter pincite (`547 U.S. at 403`, `569 U.S. 1, 6`).
- Authority-weight labels are validated where they appear in a table column
  headed Weight/Authority/Precedential; free-prose weight framing is left to
  CHECKLIST:D6.
- The controlling amendment is read from a dedicated `amendment` /
  `controlling_amendment` frontmatter field if present, else parsed from
  `jurisdiction` (the current pre-overhaul location).
