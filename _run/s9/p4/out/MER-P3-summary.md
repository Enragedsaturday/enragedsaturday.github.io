# MER-P3 summary (WS=MER, S9 R11 Mermaid pass)

Lane/model: `MER-P3` / `claude-opus-4-8`. Write-scope: `_run/s9/p4/` only.
Findings-only; no `content/`, lake, registry, or ledger edits.

## Coverage (deterministic)
- **Assigned: 15** — blocks MER-031 … MER-045 (`_run/s9/p4/mermaid-blocks.json`).
- **Examined: 15** — each block written to `_run/s9/p4/render/<id>.mmd`, rendered to `<id>.png`,
  visually Read, and compared node-by-node/branch-by-branch against its host page's stated rule.
- **Skipped: 0.**
- **Renders: 15/15 `ok`** (mmdc clean exit, non-trivial PNG 51–105 KB).
- **Legible: 15/15 true.**
- **Faithful: 15/15 PASS. FINDINGs: 0.** (`MER-P3-findings.jsonl` is intentionally empty.)

## Method
Per block: extract body -> `<id>.mmd`; render `mmdc -i <id>.mmd -o <id>.png -p pptr.json -b white -w 1000`
(reused `_run/s9/p4/render/pptr.json`, chrome-headless-shell path from B-MER bootstrap); Read PNG;
Read host page's `## Visual` block plus the Brief / Key-cases / Related-cases prose that states the
rule each node encodes. Checked: (a) branch logic matches the doctrinal test, (b) each case sits at
the node its holding governs, (c) no node contradicts the page's black-letter rule, (d) legibility.
Where a diagram cites a case, confirmed the case appears on the page at the corresponding node
(e.g., MER-034 `Vinton` verified at page lines 40/60/87; all 11 diagram cases present).

## Per-block result
| id | page | render | legible | faithful |
|----|------|--------|---------|----------|
| MER-031 | Seizure of Property | ok | y | PASS |
| MER-032 | Seizure of the Person (When a Seizure Occurs) | ok | y | PASS |
| MER-033 | Terry Stops and Reasonable Suspicion | ok | y | PASS |
| MER-034 | Traffic Stops | ok | y | PASS |
| MER-035 | Arrest and Arrest Warrants | ok | y | PASS |
| MER-036 | Arrest in the Home | ok | y | PASS |
| MER-037 | Prompt Probable-Cause Determination | ok | y | PASS |
| MER-038 | Probable Cause | ok | y | PASS |
| MER-039 | Reasonable Suspicion | ok | y | PASS |
| MER-040 | Standing to Challenge a Search | ok | y | PASS (cosmetic) |
| MER-041 | Fruits and Attenuation | ok | y | PASS (cosmetic) |
| MER-042 | Inevitable Discovery and Independent Source | ok | y | PASS |
| MER-043 | The Good-Faith Exception | ok | y | PASS |
| MER-044 | the-exclusionary-rule/index | ok | y | PASS (cosmetic) |
| MER-045 | Lineups and the Right to Counsel | ok | y | PASS |

## Cosmetic notes (PASS, not FINDINGs — per B-MER precedent that dense-body label crowding is layout, not a defect)
- **MER-040** — dense edge labels: the `Rawlings` and `Mancusi` case tokens partially underlap the
  adjacent `Carter` / `Byrd` labels. `.mmd` source is correct; branch logic and case-to-node mapping
  are all faithful; only two tokens are visually crowded.
- **MER-041** — the three escape-hatch edge labels crowd near the `ADMITTED — taint purged`
  convergence; all readable.
- **MER-044** — the four exception edge labels crowd at the `ADMITTED — no suppression`
  convergence; all readable.

## For the orchestrator
- Zero content/faithfulness defects in MER-031…045; no re-adjudication or CL needed (`needs_cl` n/a).
- One item worth a ruling if desired (not filed as a FINDING): **MER-045** groups "show-up" with
  lineup/prelim-hearing ID as a corporeal confrontation feeding the Cobb charged-offense gate. That
  tracks the settled Wade/Gilbert black-letter rule; the page itself flags a *lower-court* frontier
  (post-charge showup as trial-like confrontation vs due-process field ID) only under
  "Lower-court developments," so the teaching flowchart's simplification does not contradict the
  page. Recorded here as an FYI, not a defect.
- Cosmetic label-crowding in MER-040/041/044 could be eased later (widen `-w`, or split long edge
  labels) if a redraw pass is run; not required for correctness.
