# MER-P4 summary (WS=MER, S9 R11 Mermaid pass)

Lane/model: `MER-P4` / `claude-opus-4-8`. Write-scope: `_run/s9/p4/` only.
Findings-only: no `content/`, lake, registry, or ledger edits. No verdicts adjudicated
(the `faithful` field records the lane's render-vs-page comparison, not an orchestrator verdict).

## Coverage (deterministic)
- **Assigned: 15** — blocks MER-046 … MER-060 (`_run/s9/p4/mermaid-blocks.json`).
- **Examined: 15/15** — each block written to `render/<id>.mmd`, rendered to `render/<id>.png`,
  visually Read, and compared node-by-node / branch-by-branch against its host page's stated
  rule (rule callout + The Brief + Key-cases table).
- **Skipped: 0.**
- Render: **15/15 ok** (all `mmdc` exits clean; PNGs 39–147 KB, non-trivial).
- Legible: **15/15 true.**
- Faithful: **15/15 PASS. 0 FINDING.**

## Method
Per block: `npx -y -p @mermaid-js/mermaid-cli mmdc -i <id>.mmd -o <id>.png -p pptr.json -b white -w 1000`
(reused fleet `render/pptr.json` = chrome-headless-shell under `~/.cache/puppeteer`). Then Read
the PNG and Read the full host page; verified (a) every node/branch label is present and matches
the diagram source fenced block, (b) branch logic matches the doctrine (correct gate order, Yes/No
routing, terminal dispositions), (c) cases sit at the correct nodes with no contradiction against
the rule callout / brief, (d) text is legible at w=1000.

## Per-block result
| id | host page (topic) | render | legible | faithful |
|----|-------------------|--------|---------|----------|
| MER-046 | Sixth Amendment Right to Counsel | ok | yes | PASS |
| MER-047 | Detention & Search of Persons at the Scene | ok | yes | PASS |
| MER-048 | Knock-and-Announce | ok | yes | PASS |
| MER-049 | Scope, Manner & Related Issues | ok | yes | PASS |
| MER-050 | Franks Challenges | ok | yes | PASS |
| MER-051 | Particularity | ok | yes | PASS |
| MER-052 | Probable Cause in the Affidavit | ok | yes | PASS |
| MER-053 | The Neutral & Detached Magistrate | ok | yes | PASS |
| MER-054 | Qualified Immunity | ok | yes | PASS |
| MER-055 | Section 1983 & Municipal Liability | ok | yes | PASS |
| MER-056 | Suing Federal Officers | ok | yes | PASS |
| MER-057 | Use of Force | ok | yes | PASS |
| MER-058 | Consent Searches | ok | yes | PASS |
| MER-059 | Knock and Talk | ok | yes | PASS |
| MER-060 | Searching Effects & Containers | ok | yes | PASS |

## Notes for the orchestrator (cosmetic / layout only — all PASS)
- **MER-049** (Scope/Manner): 6-way manner fan-out is dense; text still legible at w=1000.
- **MER-053** (Neutral Magistrate): the three "No:" disqualifier edge labels crowd the middle
  band but remain readable; all three correctly converge on NOT-neutral->void.
- **MER-059** (Knock and Talk): largest/densest block (147 KB, 4-dimension ladder with four
  deviation edges all routing to one SEARCH node); long edge runs and a sprawling vertical
  layout, but no node text is clipped or overlapped illegibly. Content-layout crowding only,
  not a render defect — PASS.
- No node/branch/label contradicted its host page's rule callout, brief, or key-cases table.
  Diagram case-abbreviations (e.g., "Lo-Ji", "Rivas-Villegas", "Wilson v. Layne") match the
  cases the pages place at those nodes.

## Artifacts
- Verdicts: `_run/s9/p4/out/MER-P4-verdicts.jsonl` (15 rows, `p4.mermaid.v1`).
- Findings: `_run/s9/p4/out/MER-P4-findings.jsonl` (empty — 0 FINDINGs).
- Renders: `_run/s9/p4/render/MER-046.{mmd,png}` … `MER-060.{mmd,png}`.
