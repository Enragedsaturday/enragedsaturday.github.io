# S6 FRONTIER WAVE 2 — CLAUDE lane log

- **Lane:** `{lane:"claude-frontier-w2", model:"claude-opus-4-8", effort:"xhigh"}`
- **Pairing:** R6 + A2 blind dual-model pair (Claude leg). No `s6-frontier-*codex*` file read; no CourtListener; web-only (WebSearch/WebFetch); no sub-agents; no commits.
- **Categories (6):** the-warrant · confessions-interrogation-and-the-fifth-amendment · the-right-to-counsel · fair-trial-and-reliability-doctrines · foundations-and-the-fourth-amendment · standards-of-proof.
- **Method:** S6 R6 (web-first discovery → CL/stub confirmation via S2 R7 queue; ≤2 expansion hops beyond seed; PRACTICES §4 saturation stops) under the D5 stricter frontier floor (page ⇔ clearly-controlling **or** named both-sides split-marker; else mention/history). REMIT GUARD enforced: officer field conduct / admissibility-suppression / officer civil liability IN; trial-craft OUT (esp. fair-trial + right-to-counsel — kept only identifications, Massiah/field attachment, suppression-side doctrine).

## Corpus baseline read
All 6 wave-2 category trees read in full (indexes + every authored doctrine node): The Warrant Requirement (+ getting-a-warrant ×4 sub-nodes and executing-a-warrant ×3 sub-nodes verified present by directory listing); Miranda and Custodial Interrogation; Miranda Waiver and Invocation; Due-Process Voluntariness of Confessions; Public-Employee Compelled Statements (Garrity); Sixth Amendment Right to Counsel; Lineups and the Right to Counsel (STUB/draft); Eyewitness Identification; Brady and Giglio; Entrapment; Common Law Origins; Fourth Amendment Framework; Probable Cause and Reasonable Suspicion; The Proof Ladder (STUB/draft). The wave-2 corpus is **extraordinarily complete** on the SCOTUS canon and already flags nearly every live circuit/state frontier.

## Pre-check discipline (every candidate)
Grep-checked each candidate caption against: `content/cases/` (459 pages), `_overhaul2/lake/_manifest.json`, and `_run/s6-candidates/{r7-queue-batch1.jsonl, gated.jsonl, gap-docket.jsonl}`. Web never asserts; every page-candidate is emitted to the S2 R7 queue for two-key identity + fabrication confirmation before authoring. Grep-confirmed absences noted per row ("not found ≠ fabricated").

## Discovery evidence
Cites are discovery evidence (Justia / supremecourt.gov / Cornell LII / govinfo U.S. Reports / law reviews), flagged for CL confirmation at S2 R7. No CourtListener calls made.

## Headline result

| category | page-candidates | mentions/history | notes |
|---|---|---|---|
| fair-trial-and-reliability-doctrines | **3** (Trombetta, Youngblood, Fisher) | 1 (Youngblood bad-faith frontier) | duty-to-PRESERVE-evidence line — the missing sibling of Brady's duty-to-disclose |
| the-right-to-counsel | **1** (Moore v. Illinois) | 1 (Coleman v. Alabama, remit-borderline) | post-charge preliminary-hearing showup = 6A critical stage; fills the Lineups stub |
| the-warrant | 0 | 1 (Marron, history) | canon saturated |
| confessions-interrogation-and-the-fifth-amendment | 0 | 1 (Kastigar, remit-borderline mention) | canon saturated |
| foundations-and-the-fourth-amendment | 0 | 1 (Burdeau, history) | framework/history saturated |
| standards-of-proof | 0 (field-facing) | 2 (Winship, Addington) | field rungs saturated; trial/civil rungs out of remit |

**Total: 4 page-candidates + 6 mentions/history, 0 new split-markers.**

## Strongest finds (rationale)

### 1. Duty-to-preserve-evidence trilogy — fair-trial-and-reliability (THE gap)
The Brady and Giglio page is **disclosure-only**. The distinct due-process duty to **preserve** evidence — the officer-side/evidence-handling mirror of Brady — is entirely absent from the corpus, though it passes the same remit gate the corpus already used to page the "Brady cop" officer-disclosure theory (suppression-side + officer field conduct: breath samples, biological/rape-kit swabs, dashcam, lab handling).
- **California v. Trombetta**, 467 U.S. 479 (1984) — duty to preserve reaches only evidence of **apparent exculpatory value** the defendant cannot replace by reasonable means. grep 0.
- **Arizona v. Youngblood**, 488 U.S. 51 (1988) — for merely **"potentially useful"** evidence, the defendant must show police **bad faith**; negligence is not a due-process violation. grep 0. The anchor.
- **Illinois v. Fisher**, 540 U.S. 544 (2004) (per curiam) — the bad-faith requirement applies **even with a pending discovery request**; completes the trilogy. grep 0. (Borderline page vs. fold-as-Youngblood-bullet.)
- Distinguish **Michigan v. Fisher** (555 U.S. 45 (2009), emergency-aid) which IS in corpus — different case.

### 2. Moore v. Illinois — the-right-to-counsel (fills the Lineups stub)
**Moore v. Illinois**, 434 U.S. 220 (1977) — a corporeal identification at a **post-charge preliminary hearing** with no counsel present is a Wade/Gilbert **critical stage**; the uncounseled pretrial ID is barred from the case-in-chief under Gilbert's per se rule. Extends the counsel-at-identification right beyond the stationhouse lineup to a courtroom showup — the strongest showup application the corpus lacks. grep 0 (only Virginia v. Moore present). Identification-facing = in remit. Filed once here to avoid double-count with its Eyewitness-Identification cross-home.

## Saturation stops fired (honest, per PRACTICES §4)
- **the-warrant** ✔ — issuance/knock-and-announce/execution/on-scene-control/good-faith all present (Summers/Bailey/Muehler/Rettele/Ybarra grep-confirmed). Only Marron v. United States (1927) plausibly omittable → history/mention (payload carried by Stanford/Groh/Steele). Digital warrant splits (Holcomb 9th, Smith 5th) already flagged.
- **confessions/5A** ✔ — Miranda/waiver-invocation/voluntariness/Garrity exhaustively complete; Vega (2022) in. Only Kastigar (1972) adjacent → remit-borderline mention (grand-jury/trial-side). Public-safety (Liddell), Seibert two-step (Capers/Williams), Shatzer (Wint) splits already flagged.
- **foundations** ✔ — framework/history; Burdeau (1921) state-action origin → history/mention (subsumed by Jacobsen/Skinner). Hash-match, pole-camera, geofence splits already flagged.
- **standards-of-proof** ✔ — field rungs complete; Winship/Addington are trial/civil rungs → mentions (out of field remit; PC/RS page itself marks BARD as non-field). Daniels 10th RS-floor already in corpus.
- **right-to-counsel / fair-trial** ✔ — every SCOTUS line complete except the two genuine omissions above; no new named both-sides federal split found (Youngblood bad-faith divergence is diffuse + state-constitutional departures → floored to mention).

## Searches run (WebSearch)
1. "California v. Trombetta Arizona v. Youngblood Illinois v. Fisher due process duty to preserve evidence bad faith standard" → confirmed the three holdings + the materially-exculpatory vs potentially-useful distinction.
2. "Moore v. Illinois 434 U.S. 220 (1977) right to counsel identification preliminary hearing critical stage showup" → confirmed the post-charge-showup critical-stage holding + per se exclusion.
3. "Arizona v. Youngblood bad faith requirement circuit split federal courts lost evidence due process" → 'bad faith' left open to the circuits (diffuse divergence, not a clean named both-sides split) + state-constitutional departures; floored to mention.
4. "Supreme Court 2024 2025 term Fifth Amendment Miranda Sixth Amendment right to counsel eyewitness identification decision" → no post-2022 controlling omission surfaced beyond corpus (Vega 2022 / Glossip 2025 / Chatrie 2026 all in).

## Grep checks against corpus (absence-confirmation)
0 hits (absent → candidate/mention): Trombetta, Youngblood, Illinois v. Fisher, Moore v. Illinois, Coleman v. Alabama, Winship, Addington, Kastigar, Burdeau, Marron.
Present (excluded): Michigan v. Summers, Bailey v. United States, Muehler v. Mena, L.A. County v. Rettele, Michigan v. Fisher (emergency-aid — NOT the preserve case), Virginia v. Moore (NOT Moore v. Illinois), Andresen, Segura, Murray, Gerstein, Wong Sun, Stoner, Chapman (1961), plus the entire seed canon.
