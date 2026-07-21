# S8H-B summary — WS S8H, R9 (b) S8 ledger review + (c-mechanical) fragment→cache trace

Packet: `S8H-B`. Findings-only, WRITE-SCOPE `_run/s9/p4/` only. Model: `claude-opus-4-8`.
Evidence sources: `_run/s8-link-ledger.json`, `_overhaul2/lake/cases/*.json`,
`~/cssi-lake/cache/text/<id>.txt`, `content/**/*.md`. No live CL (1 row carries `needs_cl`).

Ledger under review was scanned at `scanned_head=f24445143` (an ancestor of HEAD `62fb8a8b`);
**260 content files changed since**, so line numbers drift — all checks are drift-tolerant
(locate `matched_text` in the current file, re-derive the masking zone at the current line).

## Coverage (assigned / examined / skipped)

| Surface | Assigned | Examined | Skipped | Flagged |
|---|---|---|---|---|
| (b.i) mentions rows | 14,184 | 1,419 sampled (every 10th) | 0 | 0 |
| (b.i) terms.pages rows | 539 | 54 sampled (every 10th) | 0 | 0 |
| (b.ii) adjudicated resolutions | 188 | 188 (100%) | 0 | 0 |
| (c) `#:~:text=` fragments | 231 | 231 (100%) | 0 | 7 |

Skipped: **none.** Every assigned row was examined. Total findings filed: **7** (2 low, 5 medium; 1 `needs_cl`).

## Adjudication-marker convention (asked)
The ledger's judgment surface = mention rows where **`resolution.method == "adjudicated"`
OR the row carries an `adjudication` object**. Union = **188** rows (187 carry the full
`adjudication{candidates,reason,confidence,evidence,s9_coverage_inbox}` object; +1 is the
appended `Smith v. Illinois` → `Davis v. United States` year-sibling row that has
`method=="adjudicated"` but no object — matching `counts.mentions_adjudicated=187` +
`mentions_adjudicated_appended=1`). `reason` taxonomy: `ambiguous-short-name (no unique
rung-1/2/3)` 132 · `unknown-caption (not in lake/pages/ledger)` 49 · `ambiguous-short-name
(page binds >1 caption)` 3 · `ambiguous-caption (year-sibling pages)` 3 · appended 1.
Note: the brief's illustrative "three-Morgans class" is **not** literally in this ledger's
adjudicated set (only 4 `Morgan v.` mentions ledger-wide, none adjudicated); the convention
above is the operative marker.

## (b.i) Every-10th sample — method + result
Deterministic rule: **0-based index % 10 == 0** (indices 0,10,…,14180 → N=1419 mentions;
0,10,…,530 → N=54 terms.pages). Per row: (1) locate `matched_text` in the current file;
(2) re-derive the masking zone (frontmatter / heading / fenced-code / HTML-comment /
blockquote / table) at the occurrence; (3) check the recorded `action`/`resolution` still holds.
- **at recorded line 1392 · line-drift 27 · absent 0.** All 27 drifted rows re-checked at the
  relocated line — zone/disposition still sound.
- **558/558 maskable rows** (frontmatter/heading/code/comment/quote/casecell) passed the
  zone re-derivation; **55/55 `exempt:selfpage`** matched the page's own case.
- **Corpus-wide confirmations run beyond the sample** (cheap + high-signal): dead link targets
  **0 / 6058** `linked` rows resolve to a real page; stale `plain:no-page` **0 / 82** (none has
  since gained a page); `terms.pages` by_route sums == `links` for all sampled pages.
- Light-touch (examined, no hard assertion — heuristic too noisy to fail-close): `exempt:sources`
  (170 in sample), `exempt:citation` (6), `plain:adjudicated` (14). None showed an obvious
  misclass on read.
Output: `S8H-B-ledger-sample.jsonl` (header + 1419 mention rows + 54 term rows).

## (b.ii) 100% adjudicated re-review — method + result
All 188 confirmed against current corpus + lake identity fields. Checks:
- **unknown-caption (49; 42 `s9_coverage_inbox`)** — re-confirmed **still genuinely uncovered**:
  none of the 49 captions is now in the lake (668 records) or a content page, so "left plain,
  S9 owns ingest" remains correct (spot-verified: Rabinowitz, Mathews v. Eldridge, Barker v.
  Wingo, Jackson v. Denno, US v. Conroy, Texas v. White — all lake:NONE page:NONE).
- **ambiguous-short-name self-reference** — own-page match confirmed (e.g. `Alabama v. White`
  L67 "*White* anchors the rule…" is left plain / self-referential, not a broken link).
- **year-sibling (3 + 1 appended)** — target resolves / plain disposition preserved.
No stale-coverage, no dead-target, no self-ref mismatch. **0 findings.**
Output: `S8H-B-ambiguity-rereview.jsonl` (header + 188 rows).

## (c) Fragment→cache trace — method + result
231 `#:~:text=` fragments extracted repo-wide. Per fragment: URL-decode (text-fragment grammar
`[prefix-,]start[,end][,-suffix]`, literal `,` = delimiter, `%2C` = comma); resolve opinion id
from `/opinion/<id>/`; load `~/cssi-lake/cache/text/<id>.txt`, **falling back to the lake
record's `lead_opinion_id` when the url-id cache file is absent** (sanctioned by the task);
verbatim-check (whitespace-insensitive, with de-hyphenation of cache line-break hyphens);
G3 trace to `pinpoints[].quote` family (G3-passed ⇔ `quote_fidelity=="matched"`).
- **230 MATCH · 1 MATCH-VARIANT · 0 MISS · 0 NO-CACHE.**
- **G3: 226 → matched (G3-passed) pin · 2 → mismatch pin · 3 → no pin · 0 → no lake record.**
- 21 fragments matched via the **normal url-absent→lead fallback** (recorded as row notes, **not**
  findings — this is the prescribed behavior).
Output: `S8H-B-fragment-trace.jsonl` (header + 231 rows).

### The 7 fragment findings (for orchestrator adjudication)
1. **`frag-on-mismatch-pin` (medium) — Florida v. Jardines.md L57** + **`frag-variant` (low,
   needs_cl)** same fragment `There is no customary invitation to do that`. Cache `856347.txt`
   stores the word hyphenated across a line break (`invita-\ntion`); the fragment matches only
   after de-hyphenation (fails a strict whitespace-insensitive test), and lake `pin-9` is
   `quote_fidelity="mismatch"` for the same reason. Substantively correct quote; highlight
   should resolve on live CL (no hyphenation there). Fix owner decides: re-verify/upgrade pin-9,
   or accept.
2. **`frag-on-mismatch-pin` (medium) — United States v. Walker.md L55**, fragment `did not exceed
   the geographic limit on the knock and talk exception`. **Verbatim MATCH** in cache `2844024.txt`,
   but the record's only covering pin (`pin-1364`) is `mismatch` (a stitched quote with `. . .`
   ellipsis); the record has **no** G3-passed pin. Fragment works; provenance pin is not G3.
3. **`frag-cache-id-partial-sibling` (low) — United States v. Cano.md L55**, fragment `exceeded the
   proper scope of a border search and was unreasonable as a border search under the`. URL uses
   `/opinion/4649091/` (cluster id); `4649091.txt` (21 KB partial sibling) **lacks** the quote,
   but lead `4426344.txt` (75 KB) has it verbatim and `pin-op29` is `matched`. S8 R5's url-id
   validation would fail even though the fragment is valid — the fragment validator should key on
   `lead_opinion_id`, not the cluster id.
4. **`frag-no-lake-pin` ×3 (medium) — Knock and Talk.md L19** (a blockquote with 3 fragments):
   Jardines `approach the home by the front path`, Jardines `limited not only to a particular
   area but also to a specific purpose`, King `the occupant has no obligation to open the door`.
   All three are **verbatim MATCH** in cache but trace to **no** pinpoint in the target lake
   records (Jardines has 2 pins, King has 1 — none carry these spans). Additional signal: the
   second fragment's own wikilink anchors `[[Florida v. Jardines#^pin-9|id.]]`, yet lake `pin-9`'s
   quote is *different* text ("trained police dog…no customary invitation to do that") — a
   content-anchor↔lake-pin desync. Orchestrator decides: register these pins in the lake (A14
   write-back), accept doctrine-page authored fragments, or re-anchor.

## Cross-checks
- `_run/s9/adjudications.jsonl` checked before filing: the only hits near these targets are P2
  **home-mirror tally** adjudications (Bostick/Drayton/Walker *progeny placement* on the Knock and
  Talk page — a different surface, all DISMISSED). **None** adjudicates fragment provenance; no
  re-litigation.
- All 182 lake pinpoints carrying an A14 `fragment` field are `quote_fidelity="matched"` (baseline
  intact); the 7 findings are all fragments whose provenance falls *outside* that written-back set.

## Outputs
- `_run/s9/p4/out/S8H-B-ledger-sample.jsonl`
- `_run/s9/p4/out/S8H-B-ambiguity-rereview.jsonl`
- `_run/s9/p4/out/S8H-B-fragment-trace.jsonl`
- `_run/s9/p4/out/S8H-B-findings.jsonl` (7 rows)
- `_run/s9/p4/out/S8H-B-summary.md`
