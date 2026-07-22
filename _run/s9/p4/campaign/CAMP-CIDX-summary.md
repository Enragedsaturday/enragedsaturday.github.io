# CAMP-CIDX summary — final LINT-10 content packet (Case Index)

**Packet:** CAMP-CIDX · **lane:** claude · **model:** claude-opus-4-8
**Scope:** content/cases/ frontmatter `holding:` strings · `Case Index.md` (regen only) ·
C09 role-compound lines · `_run/s9/p4/CI_HEAD.md` (override source) · `_run/s9/p4/campaign/`.
Doctrine: LINT10-PACKET-BRIEF (S1 A7/A8) + RULING P4-16(e) (max 1 em-dash/block; Case-Index
rows fix at the SOURCE frontmatter `holding:` then FIN-INDEX regen).

## (1) INDEX EM-DASH SOURCE FIX — 169 holdings, deterministic

The per-file LINT-10 strips frontmatter, so `holding:` em-dashes surface ONLY when rendered
into the Case-Index table (the whole table = one paragraph block). HEAD baseline: **73 highs**
(1 block-level w/ 249 unmasked em-dashes + 72 sentence-level), 249 em-dashes distributed:
holding cells 242, CL-placeholder cells 5, flagged captions 2.

Fixed the em-dash budget in **169 case-page `holding:` frontmatter strings** (241 em-dashes;
`content/cases/*.md`) via meaning-preserving punctuation transforms — the source of every
sentence-flagged row plus every within-budget holding em-dash. Applier
(`scratch/cidx/apply_holdings.py`) validated per holding: 0 residual em-dash, letters
byte-identical (except 3 sanctioned `— and`→`.` splits that drop the coordinating "and"),
JSON round-trip. Only the `holding:` line changed per file (verified).

Technique mix: 73 paren-pair (`X — aside — Y`→`X (aside) Y`, 7 with a tail comma),
40 colon, 27 comma, 20 period-split, 3 drop-emdash (truncated `—…`→`…`: Brady/Groh/McArthur),
5 period-split (incl. 3 `and`-drop), 1 semicolon. Truncated `…` SSOT holdings kept verbatim
(un-truncation is out of scope). Quotes/labels never edited. Corrected-holding gates
(Mitcham inevitable-discovery, Perez SIA/Eatherton+Chadwick/Gant, Loera inevitable-discovery)
preserved through the rewrite.

`content/index.md` (site home): swept — **0 LINT-10 highs** (already clean from earlier packets).

## (2) REGEN + GATE CHECKLIST

`python3 _run/s9/p4/fin_index_build.py --write` against the CURRENT tree (no HEAD checkout).

| Gate | Result |
|---|---|
| index LINT-10 | **73 highs → 1 high** (block-level; 8 residual em-dashes — ESCALATED below) |
| index sentence-level LINT-10 highs | **0** (all 72 cleared) |
| index LINT-11 | **0** — L494 Cruz carry-forward reword preserved (see below) |
| index LINT-16 | **0** (F-S5-04 carve-out holds) |
| Rows vs content/cases | 610 case rows == 610 files; +2 flagged = **612**; `added=[]`, `removed=[]` |
| Blank Good-law cells (N13) | **0** |
| Dead register targets | **0** |
| Fidelity (unchanged cells reproduce HEAD) | `fidelity_fail=[]` (398 unchanged cells byte-exact) |
| Term-link coverage delta | HEAD 238 → final 254; drops 4 / adds 18, ALL on P2/P3/CIDX-changed cells (S8 re-derivation), logged in FIN-INDEX-fixes.jsonl |
| Mitcham / Perez / Loera corrections | present ✓ (inevitable-discovery / SIA-Eatherton / inevitable-discovery) |
| Case-cell resolution | all resolve via Quartz PageIndex; 3 strict-stem-check flags (`[[Case Index]]` self-row + Fare/Marshall filename-vs-title punctuation) are PRE-EXISTING, resolve by title |
| Pipeline fixed point | two `--write` runs byte-identical (md5 `4e6f3b3b…` STABLE) |

**LINT-11 / L494 carry-forward reword (root-caused + fixed).** The task flagged "the L494
carry-forward reword must survive regen." It did NOT under a naive regen: `fin_index_build`'s
flagged-override forces the flagged rows to `CI_HEAD.md` verbatim (this SUPERSEDES the
live-index flagged row that `build_case_index.flagged_rows()` re-emits — the mechanism the task
author expected to carry the reword). `CI_HEAD.md`'s Cruz row still held the pre-reword text
with pipeline tokens **`R10`** and **`S7`**, so the first regen reintroduced 2 LINT-11 highs at
L494. Fix: synced the override source — `CI_HEAD.md:494` `(R10 carry-forward)`→`(carried
forward as an unverifiable caption)` and dropped ` at the S7 pass` (the already-adjudicated
L494 reword, verbatim from the live index). Re-regen → **LINT-11 = 0**, override now a no-op at
the fixed point (`flagged_overridden=[]`). Cruz row keeps its Byrd substitution + escaped
reporter wikilink.

**ESCALATION — residual block-level LINT-10 high (8 em-dashes, NOT frontmatter-fixable).**
After draining all 242 holding-cell em-dashes, the table block retains 8 structural em-dashes I
did not fix within scope:

- **5 × CL-placeholder** (`[[Case Index]]` self-row, Entick, Wilkes, + both flagged rows):
  `build_case_index.py` emits em-dash `U+2014` as the missing-`opinion_url` placeholder
  (`cl = ... else "—"`). Cannot fabricate opinion URLs; the generator is a signed FIN-INDEX-lane
  tool outside my write-scope.
- **2 × flagged caption** + **1 × flagged holding** em-dash (Self-help, Cruz): adjudicated
  carry-forward text sourced from `CI_HEAD.md`; the task's LINT-11 note directs these rows be
  PRESERVED as carry-forwards.

RULING P4-16(e)/the "0 highs" target did not anticipate the generator CL-placeholder. **0 highs
is unreachable via frontmatter alone.** Recommended (orchestrator / FIN-INDEX lane to adjudicate):
(A) change the generator CL placeholder `—`(U+2014)→`–`(U+2013 en-dash, NOT counted by LINT-10)
or `n/a` — removes all 5; (B) reword the flagged captions ` — TAG`→` (TAG)` and Cruz holding
`exists — removed`→`exists; removed` in `CI_HEAD.md` — removes the other 3; **A+B ⇒ index
LINT-10 0 highs**. Alternatively (C) a LINT-10 Case-Index carve-out mirroring LINT-16 F-S5-04 for
generated/flagged content. I did not perform A/B (signed generator + adjudicated carry-forward
text); returned for adjudication.

## (3) ROLE-STYLE NORMALIZATION — 31 normalized, 2 left

From `CAMP-C09-fixes.jsonl` rows with technique `role-paren|role-comma` (33 total). Corpus
precedent (verified: 319→350 `*Key:*` vs the 27 `*Key (*` + 4 `*Key,*` C09 forms; `*Key —*`=0):
normalized the **31 genuine "Key" role-compounds** to the colon form (`*Key (X)*`→`*Key: X*`;
`*Key, X*`→`*Key: X*`) — display text only, wikilink/role words verbatim, no em-dash added
(the `] — *label*` list separator stays within the 1-per-item budget). Residual `*Key (*` /
`*Key,*` = **0 / 0**; LINT-10 on the 31 files = **0 highs**.

**LEFT verbatim (documented, NOT colon-ized):** the 2 role-comma rows whose comma is
descriptor-internal, not a Role separator — `United States v. Karo.md` `*Related (cross-ref,
umbrella)*` and `United States v. Jones.md` `*Related (cross-ref, mosaic seed for Carpenter)*`.
Both are already the standard `*Related (descriptor)*` form (131 in corpus; `*Related:*` = 1
anomaly). C09 correctly replaced an inner em-dash with a comma there; colon-izing would break the
Related-paren precedent.

## Coverage (deterministic)

- (1) 169/169 holding em-dashes drained (241 em-dashes); content/index.md 0 highs.
- (2) index regen: sentence-level LINT-10 0/72, block-level 1 (8 residual ESCALATED),
  LINT-11 0, LINT-16 0, all FIN-INDEX gates PASS, fixed point stable.
- (3) 31/31 Key role-compounds → colon; 2 Related left (documented).

## LOOP-2 — RULING P4-21 adjudication applied (A + B, no carve-out)

The loop-1 escalation (8 residual block-level em-dashes) was adjudicated: apply A + B.

- **(A) generator** `scripts/build_case_index.py`: missing-opinion CL placeholder
  `—`(U+2014)→`–`(U+2013 en-dash) via a `NO_OPINION` constant + R12-visible doc comment
  beside the flagged-splitter fix. LINT-10 counts only em-dashes, so on regen the 3 case-page
  CL placeholders (Case Index self-row, Entick, Wilkes) clear. (Both `page_rows` and `brief_rows`
  placeholders updated for one convention.)
- **(B) flagged carry-forwards** (Self-help L400, Cruz L494): reworded per budget doctrine —
  caption ` — TAG`→`: TAG` (colon); Cruz holding `exists — removed`→`exists; removed` (semicolon);
  CL cell `—`→`–` (en-dash). Applied **identically to BOTH the live index (build source) and
  `CI_HEAD.md` (override source)**: the flagged-override keys on the caption, so a caption reword
  requires both sources to match or the override would revert it — this makes the fix regen-durable
  (override is a no-op at the fixed point). Rows still `is_flagged` (UNVERIFIABLE/UNCONFIRMED
  retained); L494 R10/S7-free reword + Byrd substitution preserved. (The earlier preserve directive
  protected content, not punctuation — per P4-21.)

**Verification (all PASS):** index LINT-10 **73 → 0 highs**; corpus-wide content-scope LINT-10
**0 highs**; LINT-11 **0** (index + corpus); LINT-16 **0** (index + corpus); fixed-point md5
`ea2d366958553efbc686fd2f75c13935` STABLE across two `--write` runs; FIN-INDEX gates hold (612
rows, added/removed=[], fidelity_fail=[], 0 blank Good-law, 0 dead targets, Mitcham/Perez/Loera
present, term-links 238→254). The 1 remaining in-index em-dash is the byte-preserved preamble
prose (1/block = within A8 budget, not a violation). Loop-2 rows appended to CAMP-CIDX-fixes.jsonl.

## Artifacts

- `content/cases/*.md` — 169 `holding:` frontmatter edits + 31 role-label edits (+2 Related left)
- `content/legal-system-research-and-reference/Case Index.md` — regenerated (fixed point); 2 flagged rows reworded (loop-2)
- `scripts/build_case_index.py` — loop-2 P4-21(A): NO_OPINION en-dash placeholder (R12-visible)
- `_run/s9/p4/CI_HEAD.md` — flagged Cruz row synced to L494 reword (LINT-11); both flagged rows reworded (loop-2 P4-21(B))
- `_run/s9/p4/FIN-INDEX-fixes.jsonl` / `FIN-INDEX-droplog.jsonl` — regen term-link deltas (regenerated)
- `_run/s9/p4/campaign/CAMP-CIDX-fixes.jsonl` — 205 rows (169 holding + 33 role + 1 CI_HEAD-sync + 1 regen + 1 escalation)
- `_run/s9/p4/campaign/scratch/cidx/` — appliers (apply_holdings.py, apply_roles.py), holdings_todo.json, diffs.txt
