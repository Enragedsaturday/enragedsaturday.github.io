# EXECUTE wrapper — the one autonomous Overhaul-2 run (paste-pointer thread)

You are running the **CSSI Overhaul-2 EXECUTE run**: all nine specs signed, the coherence pass
PASSED, the AUDIT-CLOSURE gate STAMPED (`_overhaul2/COHERENCE-REPORT.md`). The planning content
freeze is over — this thread builds the product. **The signed specs are the law** (RUNBOOK §0
precedence: specs > RUNBOOK > PRACTICES > wrappers); execute each spec's Method/Deliverables/
Acceptance to the letter, **including every Amendments section** (S2 A1–A15 · S3 A1–A9 · S6 A1–A2
· S9 A1 · the cross-spec notes).

## Read first
`_overhaul2/RUNBOOK.md` §0–§3 (precedence · **the 7-pause human-pause register — the ONLY stops**
· wave order) → all nine `_overhaul2/specs/*.spec.md` (each at its wave; §5 Method is the work
order) → `_overhaul2/PRACTICES.md` + `_overhaul2/CL-DATA-INVENTORY.md` →
`_overhaul2/COHERENCE-REPORT.md` (the final amendments) → `_overhaul2/s9-demo/LEDGER-SCHEMA.md`
(the signed verification ledger).

## Wave order (RUNBOOK §3; build ≠ authoring order, deliberately)
- **Wave 0 — S1 rulebook:** `docs/STANDARDS.md` (updated) + `docs/STYLE.md` (new) + the lint
  scaffolding per S1 §5. Everything downstream conforms to it.
- **Wave 1 (concurrent) — S2 lake + S4 platform:** S2 is the **multi-day paced background lane**
  (~15–25k CL calls at ≤~14/min; Codex builder exclusively owns the token — S1 A1/L4′; journal +
  budget checkpoints + per-lane resume, S2 A9; seed = `_overhaul2/S6-SEED.md`). S4 lands the nav
  working-standard, search, About, pill mechanism (mockup commits normative); **R8's publish
  retirement waits for the very end** (S4 D5 sequencing).
- **Wave 2 — S3 restructure + S5 entry models:** S3: generate + commit `url-inventory.json`
  **BEFORE the first move** (A1), then tree/re-homing/registry/binding map/weights (A8). S5:
  components as mocked + `convert_tables.py` tooling.
- **Wave 3 — S6 → S7 → S8:** S6 coverage/ingest (pause packets A/B per R3/R4; dual-model
  frontier per **A2**; candidate queue through S2's lane, R7). S7 doctrine production
  (change-list is the run ledger; mechanical passes first, R15). S8 linking (pin remediation
  FIRST, then mentions → pincites/fragments → terms → embeds; ledger R12).
- **Wave 4 — S9 verify + release:** the full pipeline per the S9 spec (panel, blind
  re-derivation + concordance, completeness instruments + tripwire, lint roster 1–30
  fail-closed, self-audit) → the release gate (R13) → **the G8 publish pause (user go-ahead)**
  → deploy → verify live → S4 R8 retirement + re-verify (S9 R15) → maintenance handoff to GH#2
  (R12).

## Model fleet (user decision, 2026-07-04)
Launch this thread on **Fable** — it is the orchestrator AND the high-judgment lanes:
discordance adjudications ("what diverged / which stands"), doctrine-grain blind
re-derivations, borderline + human-pause packet calls, the release-gate evaluation.
**Opus 4.8** carries the heavy-but-structured fleets — S6 R8 page authoring, S5 converter
batches, lint implementation, inventory/ledger plumbing, mechanical corpus passes — **and the
Claude PANEL-VOTE lane** (tallies then span three model flavors: 2× gpt-5.5 lens-diverse +
Opus, with Fable as a fourth perspective at adjudication — extra diversity at the COH-17
seam). **Sonnet** takes pure-mechanical sweeps (greps, counters, regeneration checks).
**Codex gpt-5.5** stays per spec: lake builder + 2 review lanes + case-grain Thread-N reads +
web-search discovery lanes.
*Mechanics:* sub-agents via the Agent tool's `model:` parameter (sonnet/opus/haiku/fable;
**forks always inherit the parent** — use regular spawns for cross-tier work); Workflow
`agent()` takes `opts.model`; Codex via the `codex exec` recipes. Every ledger row records the
**exact model id** (`claude-fable-5` / `claude-opus-4-8` / `gpt-5.5`) in its `{lane, model}`
fields so writer≠checker and tally diversity stay machine-auditable. At P0, confirm the
CL-MCP connector is reachable from a sub-agent lane; if not, the identity slice runs in the
orchestrator's own session (still the Claude credential, still serial).

## Standing disciplines (non-negotiable)
Thin orchestrator + fresh sub-agents + small on-disk handoffs; **one serial CL lane per
credential** (builder token = builder only; Claude MCP = interactive spot-checks; consumer
identity + credential fingerprint journaled — S1 A1); writer ≠ checker everywhere (reviewer
lanes read-only; input manifests journaled — S9 R1); find→adjudicate→fix, loop-cap-3 →
`_review-needed/`; every measured planning input (roster counts, pin counts, pipe lists) is
**re-derived at EXECUTE — seed, not gospel**; checkpoint + commit per wave step (resumable);
Codex recipes: reviewer `codex exec -s read-only …` / discovery `-c tools.web_search=true`
(the root `--search` flag does NOT pass through `exec`) / builder per S2 R10 — all stdin
`/dev/null`, caller-side timeout (COH-31). The officer-BLUF layer stays banned (S1 §2.2/R6).
The 7 enumerated pauses (§0) are the only stops; report each with evidence attached.

## Done
= the S9 R13 release gate: every box PASS or a logged `_review-needed/` escalation; zero silent
gaps; zero guessed legal assertions; deployed, verified live, legacy pipeline retired; the final
report served as an HTML brief with the maintenance handoff filed.
