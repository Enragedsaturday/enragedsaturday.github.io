# W9 tail plan — staged 2026-07-07 (dispatch at the W8 gate)

One combined CL-lane session: cite recovery first (bounded), then mint everything ready, then
terminal updates. Ground truth is the lake at dispatch time — re-derive this matrix, don't trust
this prose.

## Mintable NOW (8)
- district-of-columbia-v-r-w--10845431 (slip-stamped, identity complete) — W1 skip
- egbert-v-boule--6475794 (identity repaired; cite present) — W1 skip
- gutierrez-v-saenz--10776824 — W1 skip; **read via the plain_text REST method recorded in
  CONSOLIDATED-REPAIR-REPORT.md §task-5** (MCP read_document is blind to it)
- united-states-v-cole--5307612 (re-keyed from military namesake; cite present) — W4 skip
- landor / olivier / postal-service-v-konan / the-geo-group (W2 skips; slip-stamped +
  identity-complete per the slip-support build report)

## Cite work first, then mint if it lands (7)
- people-v-frederick--4396951 — enrich (cluster fetch; Michigan 2017, expect 500 Mich. 228)
- robinson-v-commonwealth--10838748 — **slip stamp did NOT survive the re-key** (stamped the old
  record id, deleted at re-key); re-stamp via the allowlist path with the new id (2026 Va. Ct.
  App., slip) or enrich if a cite exists
- state-v-larson--1187724 — prepared enrich (1 call; expect 159 Or. App. 34 / 977 P.2d 1175
  parallel; LEXIS noise-list already landed)
- united-states-v-lewis--9424185 · mendoza--10771114 · porter--10810059 · trent--10855903 —
  cluster enrich attempt; where citations[] genuinely empty → dual-leg web-cite (R3 pattern) or
  slip-stamp (identity-complete check); never invent
- trent carries an S9-reverify flag (hand-reconstructed docket) — keep it in the mint note

## Terminal updates (no pages; fold into worklist + R11 inputs at the gate)
- united-states-v-holcomb--10670143 → **watch** (adjudicated: panel withdrew 132 F.4th 1118,
  no successor; pointer ca9 No. 23-469 / cluster 10365516)
- zorn-v-linton--10813527 → **data-escalation / unverifiable-pending** (corrupt CL cluster,
  Strike-3 text; off-CL identity path is an S9-adjacent decision — do not resurrect silently)
- davis--4881258 → folded-alias (DONE at W6 gate)

## After W9: R11 ledger assembly
148-row partition proof target: authored (per s6-authored-ledger.jsonl) + folded-duplicate(1) +
watch(1) + escalated/unverifiable + any residual deferred — every worklist row exactly one
terminal. Then the 58 non-page placements ledger fold (R8-NONPAGE-LEDGER.json), LINT-17 wiring
(R12), S6-to-S7 handoff (incl. the ledger-deferred homes rows + Case-Index schema-3 flip note +
history Field-I S9 items).
