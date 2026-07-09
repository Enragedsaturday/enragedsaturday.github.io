# S8 acceptance sweep — spec §7, machine-evidenced (orchestrator, 2026-07-09)

> Branch `overhaul2/execute` · swept at `f244451` · every criterion below cites its machine
> artifact. Commits this spec: 4dda884 (R2+R6) · 796d34f (R5+tooling) · 22c59ac (R7/R8) ·
> c3dc0a9 (R1/R3) · 1786ef2 (R4 cases) · def91fd (R4 doctrine) · cdd0471 (R9) · d4c87b4+a60dd12
> (R10/R11 + record correction) · f244451 (recovery+R12/R13).

| # | Criterion (spec §7) | Verdict | Evidence |
|---|---|---|---|
| 1 | R1/R12 join clean: zero in-scope plain mentions of authored captions; every plain mention cites a non-page terminal or exemption; 388 re-derived from ledger | **PASS** | `_run/o2-execute/s8-coh15-join.json` exit 0 — checks A_authored_plain 0 · B_plain_uncited 0 · C_resurrected 0 · D_dangling 0; NUM-04 re-derived **644** distinct captions (page-backed 595 / non-page 49; the 388 seed consumed seed-not-gospel per the spec's NUM-04 ADOPT) |
| 2 | R3: zero ambiguous auto-links; every adjudication row carries rationale; register eponyms never link case pages | **PASS** | resolver journal: 187 ambiguous/unknown rows queued, 0 auto-linked (`s8-adjudication-queue.jsonl`); 187/187 resolutions with rationale+evidence (`s8-adjudication-resolutions.jsonl`, 1:1 key match); eponym guard register-driven (11 `eponym: true` rows + seed union), fixture-tested; **wrong-authority catches live**: Carman folded-twin, Mendez same-caption-different-case, Florida-v.-Riley disambiguation |
| 3 | R4/R5: both halves wired on quoted propositions; every fragment re-validates at exactly one match; zero fragments on tier-3 paraphrases; fragments in lake | **PASS** | 182/184 G3-matched pins → validated fragments (2 honest fail-closed: Thornton no-cached-text, Rideau multi-match-no-star → `s8-fragments.jsonl`); independent re-validation 182/182 exactly-one; r3 paraphrases = 351 plain-external, 0 fragments (ledger `scope:doctrine`); lake write-back 182 rows via sanctioned `--apply-fragments` (journaled, LINT-13 0) |
| 4 | R6: mid-line pins 0; broken pin anchors 0 (HIGH); pre-existing pin links intact | **PASS** | 298 mid-block pins → 297 split + 1 orchestrator-dispositioned (Steele move-anchor); LINT-9 = 0; 287/287 pin refs resolve, 0 unresolved (`remediate_pins --verify` check 2; check-3 baseline delta 271→287 = the 16 sanctioned r2 upgrades, adjudicated in journal) |
| 5 | R7/R8: register routing complete; sampled pages fully linked at density; glossary entries citation-free; no dual-routed term | **PASS** | register v2 125 rows (page 34/glossary 38/citing 9/skip 44) + `skip_phrases` correctness guard; 2429 lane term-links live (guarded 1954 + recovery 483 − 8 wrong-sense), 0 dead targets, 0 zone violations, idempotent; glossary 42 anchors, machine audit 0 citations/case-tied; dual-route check in lint7 rewrite = 0 |
| 6 | R9: shingle detector green with embeds sanctioned; all `![[` full-slug + resolving; two flavors render as exhibited | **PASS** | residual 123 hits / 0 rule-node / 0 re-typed block-quote under the adjudicated boundary (rule-overlap always embeds; pin-overlap embeds only when block-quoted; inline/list quoted+R4-linked = sanctioned class); 4/4 embeds full-slug + resolving (`s8-embed-rows.jsonl`); both flavors verified as `class="transclude"` in emitted HTML; LINT-29 = 0 |
| 7 | R10: flash + persistent tint + centered landing, SPA and hard loads | **PASS-WITH-NOTE** | machine-verified on :8080 — SPA click applies `s8-target` + tint rgba(255,208,84,0.55); hard load `:target` same tint; centering code = the user-signed mockup commits (5b48d85/5d747f9, unchanged); the centering *animation* is unobservable in an occluded automation tab (visibility:hidden, 0 rAF ticks — environment artifact, journaled). **S9 R15 foregrounded dogfood re-samples visually** |
| 8 | R11: unescaped table pipes = 0 | **PASS** | 183 escaped (d4c87b4) + 1 italics-wrapped residual surfaced by the NEW LINT-27 and fixed (f244451); LINT-27 = 0 corpus-wide |
| 9 | R13: lint kit + fixtures delivered; old LINT-7(c) deleted; broken-anchor = HIGH | **PASS** | LINT-5 rewrite (ledger-aware, Sources-masked, broken-anchor MED→HIGH, full-slug embeds) 14H/2493M → 0H/23M all-FP-removal proven; LINT-7 rewrite (first-occurrence rule DELETED; 183H → 49H strict subset + 122M coverage flags); NEW LINT-27/28/29 with pass+fail fixtures; wired into run_all (LINT-15/16 standalone per batch-1 rule C) |

**Final gates at close:** run_all TOTAL 4184 / HIGH 3381 (new kit; old-kit apples-to-apples
6973/3529 → −148 proven-FP −1 fixed-real). HIGH composition fully attributed: LINT-10 3171
(S6 case-page em-dash backlog, S9-owed) · LINT-7 49 (30 = the hyphen-compound register
carve-out question → S9) · LINT-12 160 (pre-existing drift class) · LINT-4 1 (S3-owned A7(4)
index regen). COH-15 join clean exit 0. Build 724/2873 exit 0. Zero live CourtListener across
every S8 lane (fragment validation = cached text only).
