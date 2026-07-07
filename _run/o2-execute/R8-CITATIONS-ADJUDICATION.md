# Orchestrator adjudication — S2 enrich-citations escalations (2026-07-07)

Lane report: `_run/o2-execute/R8-ENRICH-CITATIONS-REPORT.md` (80-row scope; 32 enriched, 0 live CL
calls — 100% cache; 48 still mint-blocked). Spot-checks validated: McDonough = 588 U.S. 109,
Wyman = 400 U.S. 309; the guard's mis-key diagnoses match known merits cites (Bennis 516 U.S. 442,
Austin 509 U.S. 602).

## Ratifications
- **(a) Court-class ladder — RATIFIED.** Deterministic, exclusive, journaled, fail-closed to the
  signed serializer's `same_rank_tie`; signed serializer + identity untouched. The SD10 residue
  (corrupt roster court fields) is the disease; this is an honest bounded workaround.
- **(b) Mis-key cross-check guard — RATIFIED.** `roster expected_citation must appear in the
  verified cluster's citations` — it caught 7 wrong-cluster cites the unguarded pass would have
  shipped, and the builder reverted+re-ran clean under it. Keep permanently.

## The 48 blocked rows — recovery lanes (work order: R8-CITE-RECOVERY-WORKORDER.md)
- **R1 — identity re-keys (up to 14):** 7 cite-mismatch (austin, bennis, board-of-county-bryan,
  scott, giordano, g-m-leasing, quantity — verified cluster = orders/cert/rehearing/companion, not
  merits) + 7 no-display suspects (carroll-v-carman, alvarez, maez, owen, donovan,
  frank-v-maryland, robbins). Same machinery as packet A: dual-leg web verification →
  `--apply-web-keys` → `--readjudicate-file` on the serial lane. Per-row notes: carroll-v-carman
  may be the RIGHT cluster merely missing its `U.S.` cite (SCOTUS per curiam 574 U.S. 13 carries
  S. Ct./L. Ed. 2d — investigate before re-keying; if right, it moves to R3 web-cite handling);
  frank-v-maryland (1959) keyed to an `F.3d` cluster and robbins (SCOTUS 1981) to California state
  reporters are facially wrong; maez is keyed to a CAAF military cluster.
- **R2 — serializer policy (6):** mendez, grady, manuel, james-daniel-good, ziglar, northrup — a
  valid official cite exists but `select_official_cite` hard-fails on a stray type-1 specialty
  reporter (`Fla. L. Weekly Fed. S`, `FED App.`). **AUTHORIZED (execution-tunable precedent,
  F-S2-15):** a narrow, named specialty-reporter noise list excluded from official-selection
  candidacy — signed serializer amended surgically, fixtured + self-tested, fail-closed for
  anything off the named list; rides the same writer≠checker + CodeRabbit gates as all S2 code.
- **R3 — web-cite recovery (28 citations-empty):** CL cluster data gaps on real published cases
  (alasaad = 988 F.3d 8, kolsuz = 890 F.3d 133, …). **AUTHORIZED under the packet-A web-keys +
  A17 whitelist precedents:** two INDEPENDENT web legs must agree on the official cite; the
  citations block lands with a distinct provenance source value (schema + LINT-13 pairwise
  extension for it — never disguised as `cluster.citations[]`); leg disagreement = escalate, never
  average. Genuinely slip-only cases (too recent for a reporter) take the S2 A3 slip precedent:
  journaled `slip-only` terminal, page renders slip-style; no fabricated cite, ever.

## Wave gating
W1 launches on the code gate (17/18 mintable; 1 deferred-recovery). Recovery lane targets landing
before W2 (8 blocked) / W3 (9 blocked). Blocked rows a wave batch reaches before recovery lands
are SKIPPED with a journaled `deferred-recovery` note — never guessed, never silently dropped;
they mint in a tail batch (W9) after recovery.
