# S9 P4 — Completeness + sweeps (thin-orchestrator plan)

**Sanctioned:** 2026-07-20, user: "Execute p4 as the thin orchestrator."
**Governing text:** `_overhaul2/specs/S9-verification.spec.md` §5 P4 — the five R7 instruments
(dual-model); contradiction sweep (R6); S8-handoff + coherence + per-spec samples (R9–R11);
discoveries → S6 R8 (pause >10 pages); tripwire evaluated. Spec > RUNBOOK > PRACTICES > wrappers.

## Roles (writer ≠ checker; verdicts = orchestrator only)
- **fable orchestrator (this session):** packet cutting, class rulings, ALL adjudications,
  tripwire evaluation, Claude-credential serial CL lane (marker re-poll, spot-checks), browser
  visual checks (R9c/e, S4 samples), journal/commits.
- **o2-opus-xhigh fleet:** mechanical/structured sweeps — Mermaid render+inspect, R10 deep-equal,
  R6 pair packets, R9a/b/d, R7 I2/I3 mechanics, absence-claim enumeration, Claude-side web
  discovery lanes, fix packets. Findings-only output; NO verdicts; NO CL MCP.
- **codex gpt-5.5 (xhigh):** web_search discovery lanes (I1 web / I4 web / I5 frontier);
  panel referee votes on R6/I4 hits per R1. Read-only sandboxes, fresh `exec` each, stdin
  /dev/null, caller-side timeout, `-c model_reasoning_effort=xhigh`.
- **Serial CL lanes (S1 A1, one per credential):** S2 builder token = batched recency +
  absence-claim CL queries (paced ≤14/min, journaled `p4-cl-calls.log`); Claude MCP =
  orchestrator-only interactive spot-checks + marker re-poll.

## Workstreams → artifacts (all under `_run/s9/p4/`)
| WS | Spec | Work | Output |
|---|---|---|---|
| MER | R11 | render all 75 mermaid blocks + inspect vs page rule | `render/*.png`, `out/MER-*-verdicts.jsonl` |
| COH | R10 | callout↔registry deep-equal; override slugs; S2F-07b; prose↔lake; LINT-12/14; REVIEW rows | `out/COH-report.json` + findings |
| PAIR | R6 | contradiction sweep, 100% shared-point pairs | `pair-list.json`, `out/PAIR-*-findings.jsonl` |
| S8H | R9 | NUM-03 greps; S8 ledger ≥1-in-10 + 100% ambiguity; fragments (browser); shingle; visual samples | `out/S8H-*.jsonl` + browser logs |
| I1 | R7.1 | marker re-poll (orch) + recency lanes (builder) + bounded dual-model web sweep | `marker-poll-p4.jsonl`, `out/I1-*` |
| I2 | R7.2 | citing-graph gap check from lake + lane-3 | `out/I2-gap-findings.jsonl` |
| I3 | R7.3 | registry-point home statements + LaFave/NJLEH chapter sweep | `out/I3-toc-dispositions.jsonl` |
| I4 | R7.4 | absence-claim enumeration + two-direction search + panel | `absence-claims.jsonl`, `out/I4-*` |
| I5 | R7.5 | frontier re-run digital + civil-remedies + 1 random; diff vs S6 logs; tripwire | `out/I5-diff.json`, tripwire verdict |
| SMP | R11 | S6 gate-verdict sample; S7 TEACH-03 by tier; S4 UI samples | `out/SMP-*.jsonl` |

## Finding flow
Sweep candidate rows (`p4.candidate.v1`, non-normative) → orchestrator triage → real findings
enter the R4 machine as `s9.finding.v1` (+3 panel votes where legal-assertion class) →
adjudication (fable) → fix packet (opus) → non-author re-review → ledger. Discovered NEW
cases/topics route two-key → relevance gate → S6 R8 born-draft; >10 new pages ⇒ HUMAN PAUSE.
Tripwire (I5): any two-key-real gate-passing case/point S6's logs don't account for ⇒ full
13-category re-run fires (fail-closed) — orchestrator evaluates, user notified either way.

## Sequencing
Wave M (free, no CL): bootstrap artifacts → MER + COH + PAIR + S8H(a,b,d) + I2 + I3 + SMP.
Wave S (serial CL): marker re-poll (orch) → builder-lane recency + absence batches.
Wave W (dual-model web): I1 web + I4 web + I5, codex + claude lanes in parallel.
Wave F: triage → panel where owed → adjudicate → fix → re-review → journal/commit.
Checkpoint commit at each wave boundary. Lane-outage rule (§0 #8) applies to codex lanes.

## P3 carryovers folded in
- Touset lake pin-IIIa.quote qf-harvest-artifact (P3 note) → PAIR/QF triage row.
- Mirror-flag verify list (P3-RESIDUE-NOTES "Cross-surface mirror flags") → S8H verify pass.
- The 22 `_review-needed/s9-p3-underreview-promotions.md` escalations stay ESCALATED (gate-
  compatible); their serial-CL promotion workorder is NOT sanctioned by "execute p4" — flagged
  in the P4 report for a user decision before/at P5.

## Pacing amendment (2026-07-21, user directive after monthly-limit reset)
Target ≤50% of each 5-hour usage window: max 3 concurrent fleet lanes; ≤8 lane-dispatches
per window; sonnet for pure-mechanical; RESUME killed lanes via preserved context instead of
fresh spawns. Killed 2026-07-20 in the limit event: PAIR-P1..P4, COH, I3, I1-PREP, B-ABS,
I2-GAP, S8H-A (partial artifacts on disk; MER-P1 completed before death => WS-MER complete).
