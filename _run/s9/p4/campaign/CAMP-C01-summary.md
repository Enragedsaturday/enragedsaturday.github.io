# CAMP-C01 — LINT-10 em-dash renovation (summary)

Lane: `claude` · model: `claude-opus-4-8` · brief: `_run/s9/p4/campaign/LINT10-PACKET-BRIEF.md` (RULING P4-16(e), S1 A7/A8)

## Coverage

| metric | value |
|---|---|
| files assigned | 40 |
| lint rows assigned (manifest `row_total`) | 264 |
| distinct flagged blocks | 139 |
| blocks fixed | 139 |
| lint rows fixed | 264 |
| escalated | 0 |
| LINT-10 highs before → after | **264 → 0** |

Per-file LINT-10 highs went to 0 for every one of the 40 files (verified by
re-running `scripts/lint/lint10_emdash.py` on the full file list). Row detail
(one row per block, with masked block em-dash count before/after + technique) in
`_run/s9/p4/campaign/CAMP-C01-fixes.jsonl`.

## Techniques (by frequency)

Mechanical (94 blocks):
- **T1-role (22)** — Appears-on / homes bullets `[[Page]] — *Key — Sub*`: kept the
  universal ` — ` link/role separator (753-instance corpus convention), converted the
  role tier→sub em-dash to a colon (`*Key: Sub*`). Role string is a rendered leaf
  (reconcile reads `homes[].role` from frontmatter, not the rendered line), so no
  cross-surface desync.
- **T2-source (31)** — Sources bullets `*Case*, cite — url — pinpoints: …`: kept the
  `cite — url` em-dash, converted the pre-pinpoint em-dash to a period + capitalized
  the annotation. Matches the canonical single-dash Sources shape (cf. *State v. Mansor*).
  URLs, case names, reporters, pin ranges untouched.
- **T4-note (37) / T4-alias+note (4)** — index.md stub bullets
  `[[Page]] — *placed by S3 — S6 verifies cases, S7 authors prose.*`: kept the separator,
  split the internal note (`S3. S6`); on the 4 SIA + 1 Exigent alias bullets also
  converted the display-alias em-dash to a colon (`SIA: Persons`, etc.).

Prose / editorial (45 blocks), doctrine per block:
- parenthetical em-dash pair → parentheses (doctrine #1) — the bulk of case Issue/Rule/
  Application/Background blocks;
- appositive / participial / list-intro em-dash → comma (#1);
- independent clause → period-split (#2);
- elaboration / example em-dash → colon (#3);
- "quote — cite" doubles → first attribution parenthesized, load-bearing pincite kept (#4);
- ⚪-banner cases (Imbler, Konan, Aigbekaen, Loines, Von Neumann, Will): kept the
  `**Status: … —**` em-dash, restructured the other(s).

## Hard-constraint compliance

- **Quotations never edited.** Blocks with in-quote em-dashes (Brower, Lombardo) were
  fixed only on the non-quoted em-dashes; quoted spans are byte-identical. Colons/parens
  added at Stanford/Milam/Leon/Welsh/Glover sit outside the quote marks.
- **Controlled authority-weight labels untouched.** index.md L55 `Persuasive (outside
  circuit) — 9th Cir. & 10th Cir.` (an A8 allowlist label, masked by the lint) was left
  intact; that block reached budget via the parenthetical-pair fix alone.
- **Citations preserved.** Case names, reporters, parallel cites, pin ranges (en-dashes),
  and CourtListener URLs unchanged. Frontmatter untouched.
- **Legal meaning preserved**; role taxonomy words retained verbatim (only tier→sub
  punctuation changed).

## No new violations

Diffed the content-text lints (HEAD vs working tree) over the 40 files: every lint's
high/medium count is unchanged or lower. LINT-10 264→0; LINT-11 139→131 and LINT-4 1→0
and LINT-23 unchanged (incidental improvements, no regressions). No new banned lexicon,
no new >3-case walls, no structural breakage.

## Escalations

None. All 264 rows fell to authored prose or structured bullets outside quotations;
no lint-masking escalation (all-em-dashes-inside-quotes) block occurred in this packet.
