# O2 EXECUTE run journal

One autonomous run per `_overhaul2/wrappers/EXECUTE.wrapper.md`. The signed specs + Amendments are
the law (RUNBOOK §0 precedence). The §0 register's 8 enumerated pauses are the ONLY stops. Done =
the S9 R13 release gate, deployed and verified live.

Checkpoint discipline: one entry per wave step, appended at completion, with commit hash. A fresh
context resumes from this file + the task list.

Model fleet (user decision 2026-07-04): Fable = orchestrator + high-judgment lanes; Opus 4.8 at
xhigh (`o2-opus-xhigh` agent) = heavy structured fleets + Claude panel-vote; Sonnet = pure
mechanical sweeps; Codex gpt-5.5 at xhigh = lake builder + 2 review lanes + case-grain reads +
web-discovery lanes. Exact model ids in every ledger row.

---

## P0 — preflight (2026-07-04)

- Branch: `overhaul2/execute` cut from `overhaul2/planning` (ba5cdd3).
- `o2-opus-xhigh` agent definition present (`.claude/agents/o2-opus-xhigh.md`).
- Codex headless sanity: `codex exec -s read-only -c model_reasoning_effort=xhigh` → OK
  (codex-cli 0.142.4, model gpt-5.5, xhigh confirmed in session header). Codex's own CL-MCP
  transport emits the known expired-OAuth error — expected; the S2 builder uses direct REST v4,
  never MCP (S2 R10). Not a lane outage.
- CL token present, mode 600, `~/.config/cssi/cl-token` (out-of-repo).
- **CL-MCP connector IS reachable from a sub-agent lane** (probe: `search(type="o",
  q="Terry v. Ohio")` → count 40341, top hit Terry v. Ohio). The ≥1-in-10 identity spot-check
  slice (COH-17) may run in Claude sub-agent lanes; orchestrator-session fallback not needed.
  Probe gotcha recorded: `get_counts` takes only a `query_id` from a prior search — not a `q`.
- `.orca/` added to `.gitignore` (COH-14: copyrighted drops are local-only).
- Wave tasks #1–#10 registered in the task tracker with wave-order dependencies.

Next: Wave 0 (S1 rulebook).

## Wave 0 — S1 rulebook (2026-07-04)

- `docs/STANDARDS.md` rewritten (commit 37ef085): 35-rule catalog — O1 carried (L1–L8, N1–N13,
  SR-1…SR-5, D1–D14) with the amended rewrites (L4′ per-credential lanes A1; L8 sharpened R7;
  N4/N5/N13 for 3-field treatment; SR-1 realized via the S2 lake) + the O2 standard rules
  SR-6…SR-14 (3-field vocabulary §3.1 + A4 migration §3.2; 10-gate protocol §5A; AI guardrails
  §5B with the 10-row enforcement map; Variant A §8.1 + project-wide officer-BLUF ban; panel +
  machine ledger §6; pipeline-vocab ban §7.3; slip-op current-term; voice/em-dash/density;
  term register + SSOT). Lexicon = exact A8 allowlist (§3.0). Roster rows 1–14 documented;
  S9 codifies 1–30.
- `docs/STYLE.md` authored (new): precedence stack (project → Bluebook → Chicago + escape
  valve), house style, em-dash budget, Humanizer ADOPT/ADAPT/REJECT, term-register rules
  (machine source = `scripts/lint/term-register.yml`, seeded 23 terms), verified mnemonic
  register (CREW=3, CRON removed), citation style notes.
- Lint scaffolding: two Opus-4.8-xhigh lanes via Workflow (run wf_3af550f7-6a5; the committed
  `o2-opus-xhigh` agent type was not loaded in this session's registry — used the wrapper's
  sanctioned fallback `agent(…, {model:'opus', effort:'xhigh'})`). Lane A: lint9_carat_leak.py +
  lint10_emdash.py + fixture + run_all registration. Lane B: LINT-4 exact allowlist, LINT-5
  fail-closed resolve, LINT-6 3-field/dual-dates/glyph, LINT-7 register consumption.

### Wave-0 review loop (writer ≠ checker) — CLOSED ✅

Codex gpt-5.5 xhigh read-only review of all S1 deliverables → 8 findings (F-S1-01..08) →
adjudicated by the orchestrator (ledger: `_run/o2-execute/wave0-s1-review-ledger.json`) →
fixed (2 by orchestrator-as-fixer, 5 by a fresh Opus-xhigh lane, 1 dismissed-with-reason) →
Codex round-2 re-review: 7 FIXED + 1 residual (F-S1-05 frontmatter authority_weight unvalidated;
UPHELD — draft pages are LINT-12-exempt) → loop-3 fix + round-3 verify: FIXED. ALL-CLEAR.
Notable adjudications: Field-I enum = S2 R5's machine tokens (PRACTICES slash-forms are display
composites — now documented in STANDARDS §3.1); A4 migration counts were genuinely inverted in
the first STANDARDS draft (caught by review — fixed to A4 exact). Lint state at wave close:
LINT-4 = 34 HIGH (21 inversions + 9 prose inversions + 2 non-allowlist + 1 banned phrase + 1
prose suffix-missing — all S7 remediation) · LINT-5 = 126 HIGH broken pin anchors (S8) + 2282
MED bare names (S8) · LINT-6 = 456 LOW legacy-awaiting-projection (S2) · LINT-7 = 118 HIGH
register drift (S3 renames + S7 prose) · LINT-9 = 297 HIGH mid-line pins (S8 R6) · LINT-10 =
3989 HIGH em-dash budget (S7 rewrite pass; [!rule] callouts exempt) · self-test wired
fail-closed into run_all. Wave-0 acceptance (S1 §7): all criteria delivered or explicitly
deferred to their owning spec (LINT-11 → S9 per A2/A5; LINT-3 rebuild → S9; LINT-12/13/14 → S2).

### ⚠️ DEVIATION — pool storage root (user-visible, reversible)

The signed pool root `/Volumes/AIStore2` (S2 A10) does not exist; the AIStore2 APFS volume is
mounted at `/Users/Shared/AIStore/store2` but **TCC-blocked (EPERM) for every process in this
session chain** — orchestrator shell (sandboxed AND unsandboxed) and codex (workspace-write with
explicit writable_roots) alike. A TCC grant is GUI-only = user-only fix (same class as
interactive re-auth). Per S2 A10's env-overridable single path constant, the run proceeds with
**`CSSI_LAKE_ROOT=/Users/johngalt/cssi-lake`** (internal disk, 754 GiB free; dirs created:
cache/http, progeny, text, journal, logs, db). No verification guarantee is affected (storage
placement only; cache is regenerable/movable). **Remediation path:** grant Full Disk Access to
the session's responsible app (or fix the volume's TCC), then rsync `~/cssi-lake/` →
`/Users/Shared/AIStore/store2/cssi-lake/` and flip the constant. User notified.
