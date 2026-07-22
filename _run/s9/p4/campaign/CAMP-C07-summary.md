# CAMP-C07 — LINT-10 em-dash renovation (summary)

Lane: `claude` · model: `claude-opus-4-8` · brief: `_run/s9/p4/campaign/LINT10-PACKET-BRIEF.md` (RULING P4-16(e), S1 A7/A8)

Executed as 6 disjoint-partition `o2-opus-4-8` sub-lanes (groups of 9/9/9/8/8/8 files),
each per-file read-modify-write only, then aggregated + verified by the packet owner.

## Coverage

| metric | value |
|---|---|
| files assigned | 51 |
| lint rows assigned (manifest `row_total`) | 263 |
| distinct flagged blocks | 137 |
| blocks fixed | 137 |
| lint rows fixed | 263 |
| escalated | 0 |
| LINT-10 highs before → after | **263 → 0** |

Per-file LINT-10 highs went to 0 for every one of the 51 files, verified two ways:
each sub-lane re-ran `scripts/lint/lint10_emdash.py` on its own files, and the packet
owner re-ran it over the full 51-file list (0 remaining highs). Row detail (one row per
block, masked em-dash count before/after + technique) in `CAMP-C07-fixes.jsonl` (137 rows).

Before-count distribution of the fixed blocks: 125 blocks had 2 em-dashes, 11 had 3,
1 had 4 (United States v. Loera L68). Every block now carries ≤1 (max `block_emdash_after` = 1).

## Techniques (by frequency)

Structured bullets (66 blocks) — the repeated case-page template shapes:
- **T2-source (35)** — Sources bullets `*Case*, cite — url — pinpoints: …`: kept the
  `cite — url` em-dash, converted the pre-pinpoint em-dash to a period and capitalized the
  annotation (`… url. Pinpoints: …`). This is the C01-sanctioned Sources shape; case names,
  reporters, pin ranges (en-dashes), and CourtListener URLs are byte-identical (the URL is
  now followed by `.` instead of ` —`, with no character of the URL itself changed).
- **T1-role (31)** — Appears-on / homes bullets `[[Page]] — *Key — Sub*`: kept the
  sanctioned link↔role ` — ` separator, converted the inner role tier→sub em-dash to a colon
  (`*Key: Sub*`). Role display strings unchanged except the tier punctuation.

Prose / editorial (71 blocks), doctrine per block:
- **parenthetical / comma pair → parentheses or commas (#1) — 64** (the bulk of Background/
  Issue/Rule/Application/Conclusion/Treatment asides, and the Common Legal Terms glossary
  entries, e.g. "identified — or excluded —" → "identified (or excluded)");
- **sentence split at the em-dash (#2) — 5** (independent clause after the dash → period;
  e.g. "Yes —"/"No —" openers, and quote-attribution splits);
- **colon for elaboration (#3) — 2**.

Load-bearing carve-out (doctrine #4): ~10 of the blocks above (chiefly the 3- and 4-em-dash
blocks and quote/badge blocks) reached budget by **keeping the single most load-bearing
em-dash** and restructuring the rest — the `**Status: … —**` ⚪-banner em-dash (house
convention), a citation/pincite em-dash, or a quote-attribution `." — *Id.*` em-dash.

## Hard-constraint compliance

- **Quotations never edited.** The lint masks quoted spans before counting, so every flagged
  block carried ≥2 real em-dashes outside quotes; all fixes sit outside straight/curly double
  quotes and blockquote lines. No escalation (all-em-dashes-inside-quotes) block occurred.
- **Controlled authority-weight labels untouched** ("Binding — SCOTUS" etc.); citation text,
  reporters, parallel cites, pin/date ranges (en-dashes), and CourtListener URLs unchanged
  (URL sets verified identical modulo the benign trailing period the T2-source form appends).
- **Pin anchors preserved** (`^pin-…` set unchanged across all 51 files).
- **Frontmatter untouched by this pass.** No `holding:` string was flagged (all flagged lines
  are body prose, ≥ line 47). See the concurrency note below re: Arkansas v. Sanders.
- **Legal meaning, emphasis, and instructor voice preserved**; only punctuation/structure
  changed within each block.

## No new violations

Diffed the full non-CL lint suite (`scripts/lint/run_all.py`) HEAD vs working tree, scoped to
the 51 files: **zero high-severity regressions on any lint**. LINT-10 263→0; incidental
improvements LINT-11 −1, LINT-12 −1, LINT-23 −50 (the LINT-23 drop is attributable to a
concurrent lane's Sanders metadata promotion, not this pass); LINT-2/3/4/5/6/7/8/9/13/14/
24/27/28/29 unchanged. No new banned lexicon, no new >3-case walls, no structural breakage.
Net em-dash change across the packet: −199.

## Concurrency observation (not this pass's work)

`content/cases/Arkansas v. Sanders.md` frontmatter was modified by a **concurrent non-LINT10
lane** during this run (`authority_weight` Historical → "Binding — SCOTUS", `opinion_id`
null → 9427641, `projected_at` 2026-07-07 → 2026-07-10). This packet did **not** author those
edits and correctly left the sibling lane's work intact; its own Sanders edits are only the
L53 header treatment-badge (em-dash → colon, keeping the load-bearing "— overruled by"
em-dash) and the L69 conclusion (comma pair). Frontmatter is lint-exempt, so the em-dash
before/after counts are unaffected. Flagged here for the machine's awareness only.

## Escalations

None. All 137 flagged blocks fell to authored prose or structured bullets outside
quotations; no lint-masking (all-em-dashes-inside-quotes) escalation was required.
