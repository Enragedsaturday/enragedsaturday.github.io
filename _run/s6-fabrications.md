# S6 Packet A — fabrication resolution (R4; human pause #2)

**Generated 2026-07-06 at S6 Method step 1 close. Awaiting user dispositions — no removal or
borderline authoring proceeds until this packet returns (R4/R10).**

Verification protocol: dual-model two-key re-run — Codex gpt-5.5 web-discovery leg
(`_run/o2-execute/s6-webverify-codex.jsonl`) ∥ independent Claude Opus-4.8 leg
(`s6-webverify-claude.jsonl` + `-batches.jsonl`), mutually blind, zero CL calls (R7), Key-2
from authoritative web sources only. Orchestrator (Fable) diffed the legs and adjudicated the
4 divergences. Full row data in the JSONL files; this packet is the decision surface.

## Headline

**The fabrication queue dissolves almost entirely: 27 of 29 rows are REAL cases** — thin
caption-only seeds that S2's fail-closed identity guard refused honestly, now recovered with
full identity keys from the web. Only 2 rows are genuinely unverifiable. **All four O1-era
SEED §a fabrication suspects are REFUTED** (real cases, holdings matching our text).

## Group 1 — RESOLVED-REAL, recommend RE-KEY through the R7 queue then normal pipeline (21 rows)

Every row below: both legs REAL-with-keys (convergent), full keys recovered. Recommended
disposition: queue a re-ingest through S2's serial lane (R7) with the recovered keys; the row
then flows the normal R2-gate → R8-authoring path. No user action needed beyond packet
approval; per-row keys are in the JSONLs.

district-of-columbia-v-heller · united-states-v-verdugo-urquidez · wyman-v-james ·
trupiano-v-united-states (dead law: overruled by Rabinowitz — history framing) ·
**arkansas-v-sanders** ⚠️ (the S2 stub matched the WRONG case — the 2024 Gov.-Sanders
prison-board suit, cluster 10601315; the real case is Arkansas v. Sanders, 442 U.S. 753 (1979),
docket 77-1497, overruled by California v. Acevedo — re-key entirely) ·
**martin-v-united-states** (= GAP-04g, user-decided AUTHOR; 605 U.S. 395 (2025), docket
24-362) · united-states-v-amos (88 F.4th 446, 3d Cir. 2023) · united-states-v-daniels
(101 F.4th 770, 10th Cir. 2024 — NOT the 5th Cir. Bruen Daniels) · united-states-v-mendez
(103 F.4th 1303, 7th Cir. 2024) · united-states-v-meyer (8th Cir. 2021, docket 20-2958) ·
united-states-v-perez (89 F.4th 247, 1st Cir. 2023) · laduke-v-nelson (762 F.2d 1318, 9th Cir.
1985) · milam-v-united-states (296 F. 629, 4th Cir. 1924 — cited by Carroll itself;
conflation hazard vs the 1974 9th Cir. Milam noted) · united-states-v-berkowitz (927 F.2d
1376, 7th Cir. 1991) · united-states-v-liddell (517 F.3d 1007, 8th Cir. 2008) ·
united-states-v-ganias (824 F.3d 199, 2d Cir. 2016 en banc) · united-states-v-reddick
(900 F.3d 636, 5th Cir. 2018) · robinson-v-commonwealth (real; Key-2 sourcing thinner —
CL-web only on the Codex leg; Claude leg corroborated) · **state-v-weaver** (349 S.W.3d 521,
Tex. Crim. App. 2011 — REAL but framing caution: the holding is scope-of-consent; the
commercial-REP point our page cites it for is supporting reasoning. Keep, with an S7 prose
note) · + 2 further convergent-REAL rows per the JSONLs.

## Group 2 — caption adjudications, recommend ALIAS-FOLD not separate pages (3 rows)

- **morse-v-french** → cert-denial caption of the *French v. Merrill* litigation (15 F.4th
  116 (1st Cir. 2021), reh'g en banc denied 24 F.4th 93, cert. denied sub nom. Morse v.
  French, 143 S. Ct. 301 (2022)). Recommend: ledger alias-fold into French v. Merrill;
  mention-site prose keeps the Morse caption as the cert-posture reference.
- **carroll-v-carman ↔ carman-v-carroll** → one litigation: SCOTUS per curiam Carroll v.
  Carman, 574 U.S. 13 (2014) reversing 3d Cir. Carman v. Carroll, 749 F.3d 192. Recommend:
  SCOTUS caption is the page candidate; lower-court caption alias-folds.
- **united-states-v-chatrie stub** → the record_id names the 4th Cir. en banc decision below
  (136 F.4th 100 (2025)) while its cluster 10881683 is the SCOTUS merits *Chatrie v. United
  States*, 609 U.S. ___ (2026) (No. 25-112, geofence = search). The Chatrie v. United States
  PAGE row already tracks the SCOTUS case (s6-dedupe-pointer journaled at S2 close).
  Recommend: fold the stub into that page's history thread; the 4th Cir. below enters as
  Lower-court developments, not its own page.

## Group 3 — genuinely unverifiable, recommend REMOVE + RE-ANCHOR (2 rows) ⚠️ USER DECISION

Both legs exhausted the ladder; R1's "not found ≠ fabricated" honored — but no matching
authority exists for the propositions as cited:

- **united-states-v-west--10653830** — bare caption, no reporter, claimed for a
  stolen-vehicle/no-standing proposition. Codex: NOT-FOUND. Claude: NOT-FOUND (nearest real
  authorities for the proposition are captioned Ostrum / Smith (4th Cir. 2023)).
  **Recommend: REMOVE per R4** — prose surgery at the mention site(s): re-anchor the
  proposition to a real authority (S7-coordinated), omissions-register tombstone, ledger
  `removed` row. Never silent deletion.
- **united-states-v-white--10349533** — same proposition family. Codex: CONTEXT-MISMATCH
  (the famous SCOTUS White, 401 U.S. 745, is the false-friend recording case — wrong
  proposition). Claude: NOT-FOUND (near-miss: an 8th Cir. 2020 Robert L. White rental-car
  standing case — rental ≠ stolen, identity unconfirmed). Orchestrator adjudication:
  UNVERIFIABLE for the claimed proposition. **Recommend: REMOVE + RE-ANCHOR, same protocol.**

## Group 4 — SEED §a watch-list: ALL REFUTED as fabrications (4 rows, no action)

- **Mayville** (955 F.3d 825, 10th Cir. 2020) · **Small** (944 F.3d 490, 4th Cir. 2019) ·
  **Lyle** (919 F.3d 716, 2d Cir. 2019) — real; the O1 "invented-framework" suspicions are
  unfounded; holdings match our text.
- **Moore-Bush** (36 F.4th 320, 1st Cir. 2022 en banc) — real; the O1 "backwards-holding"
  scar is NOT in the current text (3-3 on the search question; unanimous reversal via Davis
  good-faith; cert. denied 2023). Text accurate as it stands.
- Minor: stub-suffix cluster ids for Small/Lyle/Moore-Bush differ between artifacts
  (e.g. Small 10593041 vs 4684957) — cluster-vs-sibling id nuances to resolve
  authoritatively AT the R7 re-key, not adjudicated from the web.

## For the record

- `LLC v. John Doe`: no stub by design (manifest §c documented exclusion) — noted, no action.
- The second bare "United States v. Jackson" (O1 S5 R9): adjudicated in its Exclusionary-Rule
  context at the S7 pass per R4's text, not by caption here.

## Dispositions requested

1. **Approve Group 1** (21 re-keys through R7) — [approve / list exceptions]
2. **Approve Group 2** (3 alias-folds) — [approve / list exceptions]
3. **Group 3: approve the 2 removals** (with re-anchor surgery + tombstones) — [approve /
   hold either for more research]
4. **Acknowledge Group 4** (no action) — [ack]
