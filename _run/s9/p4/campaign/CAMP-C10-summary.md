# CAMP-C10 — LINT-10 em-dash renovation (summary)

Lane: `claude` · model: `claude-opus-4-8` · brief: `_run/s9/p4/campaign/LINT10-PACKET-BRIEF.md` (RULING P4-16(e), S1 A7/A8)

Executed as 5 disjoint-partition `o2-opus-4-8` sub-lanes (11/10/10/10/10 files),
each per-file read-modify-write only, then aggregated + verified by the packet owner
(1 owner-correction applied — see Hard-constraint compliance).

## Coverage

| metric | value |
|---|---|
| files assigned | 51 |
| lint rows assigned (manifest `row_total`) | 263 |
| distinct flagged blocks | 138 |
| blocks fixed | 138 |
| lint rows fixed | 263 |
| escalated | 0 |
| LINT-10 highs before → after | **263 → 0** |

Per-file LINT-10 highs went to 0 for every one of the 51 files, verified two ways:
each sub-lane re-ran `scripts/lint/lint10_emdash.py` on its own files, and the packet
owner re-ran the full non-CL suite over the 51-file list from a clean HEAD worktree
baseline (263 → 0, no other content lint moved). Row detail (one row per block, masked
em-dash count before/after + technique) in `CAMP-C10-fixes.jsonl` (138 rows).

Before-count distribution of the fixed blocks: **128 blocks had 2 em-dashes, 7 had 3,
3 had 4** (A Quantity of Books L71, Newman L53, Virginia v. Moore L64). Every block now
carries ≤1 (max `block_emdash_after` = 1); the 3-/4-em-dash blocks were brought to
budget by keeping the single load-bearing em-dash and restructuring the rest (doctrine #4).

## Techniques (by frequency)

Structured bullets (76 blocks) — the repeated case-page template shapes:
- **T2-source (40)** — Sources bullets `*Case*, cite — url — pinpoints: …`: kept the
  `cite — url` em-dash, converted the pre-annotation em-dash to a period and capitalized
  the annotation (`… url. Pinpoints: …` / `. Interior pincite(s) …`). Case names, reporters,
  pin ranges (en-dashes), and CourtListener URLs are byte-identical (the URL is now followed
  by `.` instead of ` —`, with no character of the URL itself changed — proven below).
- **T1-role (36)** — Appears-on / homes bullets `[[Page]] — *Key — Sub*`: kept the
  sanctioned link↔role ` — ` separator, converted the inner role tier→sub em-dash to a colon
  (`*Key: Sub*`). Role display strings unchanged except the tier punctuation.

Prose / editorial (62 blocks), doctrine per block:
- **parenthetical / comma pair → parentheses or commas (#1) — 38** (32 parens + 6 comma-pair):
  the bulk of Background/Issue/Rule/Application/Conclusion/Treatment asides
  (e.g. "had not been — and might never be — adjudicated" → "had not been, and might never
  be, adjudicated"; "package — and a field chemical test — after" → "package (and a field
  chemical test) after");
- **sentence split at the em-dash (#2) — 8** (6 split + 2 comma-join): independent clause
  after the dash → period/semicolon (e.g. "No —" openers, quote-then-independent-clause);
- **colon for elaboration (#3)** and **load-bearing keeper (#4)** carry the remaining
  restructures.

Load-bearing carve-out (doctrine #4): **17 blocks** reached budget by keeping the single
most load-bearing em-dash and restructuring the rest — the treatment-badge lead-in
(`**Historical — a foundational origin…**`), the `**Status: … —**` ⚪-banner em-dash
(house convention: Moore L74, Keith L76, Fazaga L70, Knight L74, Mendoza L74, Donovan…),
or a citation/pincite em-dash (`— 466 U.S. at 113`, `— *Id.* at 1608`, `— 435 F.3d at 1149`,
Newman `^pin-op10`, Williams `^pin-1149`). Notably Newman L53 (4-em) relocated the *Santana*
attribution into an appositive lead-in so the quoted holding is untouched while the em-dash
disappears; Virginia v. Moore L64 (4-em) took two paren pairs.

## Hard-constraint compliance

- **Quotations never edited — verified corpus-wide.** Every straight/curly double-quoted
  span is byte-identical HEAD → working tree across all 51 files (multiset check). The lint
  masks quoted spans before counting, so every flagged block carried ≥2 real em-dashes
  outside quotes; all fixes sit outside quoted/blockquote spans. **One owner-correction:**
  a sub-lane's Chavez v. Martinez L59 split had moved the sentence period *inside* the
  closing quote (`occurs"` → `occurs."`); the owner reverted it to a semicolon *outside*
  the quote (`occurs"; the privilege is…`), keeping the block at 1 em-dash and restoring the
  quoted string byte-for-byte. No all-em-dashes-inside-quotes escalation arose.
- **Controlled authority-weight labels untouched** ("Binding — SCOTUS" etc.); citation text,
  reporters, parallel cites, pin/date ranges and case-line **en-dashes** (`*Marcus*–*Stanford*–
  *Heller*–*Roaden*`, `*Wade*–*Gilbert*–*Kirby*`, `692–693`) unchanged — en-dash total
  20 → 20. CourtListener URLs verified byte-identical: the 40 "URL changed" fingerprint hits
  are all the benign T2-source trailing period (`…/case/` → `…/case/.`); stripping the
  trailing `.` yields **0** URL-body differences.
- **Pin anchors preserved** (`^pin-…` set unchanged across all 51 files).
- **Frontmatter untouched.** No `holding:` string was flagged (all flagged lines are body
  prose, ≥ line 47); frontmatter blocks byte-identical HEAD → working tree for all 51 files.
- **Legal meaning, emphasis, and instructor voice preserved**; only punctuation/structure
  changed within each block. Spot-checked the five 3-/4-em-dash files' diffs by hand.

## No new violations

Diffed the full non-CL lint suite (`scripts/lint/run_all.py --summary-json`) scoped to the
51 files, **HEAD (clean detached worktree) vs working tree**: the only high-severity delta is
**LINT-10 263 → 0**. Every other content lint (2–29) is unchanged at 0 high. LINT-30 (ledger
reconciliation, not a content lint) is unchanged at 25 high — pre-existing and outside this
pass's surface. No new banned lexicon, no new >3-case walls, no structural breakage.
Net em-dash change across the packet: **720 → 531 (−189)**.

## Escalations

None. All 138 flagged blocks fell to authored prose or structured bullets outside
quotations; no lint-masking (all-em-dashes-inside-quotes) escalation was required.
