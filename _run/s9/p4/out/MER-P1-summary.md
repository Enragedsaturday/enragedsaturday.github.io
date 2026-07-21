# MER-P1 summary (WS=MER, S9 R11 Mermaid pass)

Packet: MER-P1. Lane/model: `claude-opus-4-8`. Write-scope: `_run/s9/p4/` only.
Findings-only; verdicts are non-normative candidate rows for orchestrator adjudication.

## Coverage
- **Assigned:** 15 blocks — MER-001 … MER-015.
- **Examined:** 15 / 15 (rendered + visually Read + compared node-by-node against host page).
- **Skipped:** 0.
- **Renders:** 15 / 15 `ok`. MER-001..003 PNGs reused from bootstrap (not re-rendered, per packet);
  MER-004..015 rendered fresh via `mmdc … -p pptr.json -b white -w 1000`, all exited clean
  ("Generating single mermaid chart", non-trivial PNGs 11 KB–165 KB).

## Verdict tally
- **faithful=PASS:** 15 / 15.
- **faithful=FINDING:** 0.
- **legible=true:** 15 / 15.
- **Candidate findings emitted (`MER-P1-findings.jsonl`):** 0 rows (file created empty — deterministic zero).

## Per-block result (verdict rows in `MER-P1-verdicts.jsonl`)
| id | file (repo-rel) | render | legible | faithful |
|----|-----------------|--------|---------|----------|
| MER-001 | content/confessions-interrogation-and-the-fifth-amendment/Due-Process Voluntariness of Confessions.md | ok | yes | PASS |
| MER-002 | content/confessions-interrogation-and-the-fifth-amendment/Miranda Waiver and Invocation.md | ok | yes | PASS |
| MER-003 | content/confessions-interrogation-and-the-fifth-amendment/Miranda and Custodial Interrogation.md | ok | yes | PASS |
| MER-004 | content/confessions-interrogation-and-the-fifth-amendment/Public-Employee Compelled Statements (Garrity).md | ok | yes | PASS |
| MER-005 | content/fair-trial-and-reliability-doctrines/Brady and Giglio.md | ok | yes | PASS |
| MER-006 | content/fair-trial-and-reliability-doctrines/Entrapment.md | ok | yes | PASS |
| MER-007 | content/fair-trial-and-reliability-doctrines/Eyewitness Identification.md | ok | yes | PASS |
| MER-008 | content/foundations-and-the-fourth-amendment/Common Law Origins.md | ok | yes | PASS |
| MER-009 | content/foundations-and-the-fourth-amendment/Fourth Amendment Framework.md | ok | yes | PASS |
| MER-010 | content/foundations-and-the-fourth-amendment/Fourth Amendment Recalibration.md | ok | yes | PASS |
| MER-011 | content/instructor-craft-and-study/CREW.md | ok | yes | PASS |
| MER-012 | content/instructor-craft-and-study/Three Golden Rules.md | ok | yes | PASS |
| MER-013 | content/legal-system-research-and-reference/Reading and Citing Cases.md | ok | yes | PASS |
| MER-014 | content/legal-system-research-and-reference/The Federal Court System.md | ok | yes | PASS |
| MER-015 | content/searches/Abandonment.md | ok | yes | PASS |

## Method
For each block: wrote body to `render/<id>.mmd`; rendered to `<id>.png`; visually Read the PNG;
Read the full host page (rule/BLUF callout + Brief + Key-cases table); compared every node,
branch label, and case attribution against the page's stated rule. Verdict basis recorded
node-by-node in each verdict row's `notes`.

## Cosmetic observations (PASS, severity none — no candidate rows)
- **MER-002:** two edge labels ("Butler / Thompkins", "Counsel present · Minnick") partially
  overlap adjacent node boxes but remain readable (same layout crowding the bootstrap noted).
- **MER-010:** extreme wide aspect ratio inherent to a 10-node `flowchart LR` timeline; per-box
  text small but readable, no overlap. Color classes render exactly per the page legend caption
  (red=expand, purple=incorporation, blue=contract). The `-->|"overruled by Katz →"|` label sits
  on the chronological Olmstead→Wolf edge as a forward annotation; it does NOT assert Wolf
  overruled Olmstead and is explicitly supported by the page caption ("The Olmstead node is
  later overruled by Katz"). Not a contradiction.

## For the orchestrator
- No node/branch contradicted its host page's stated rule; no case was mislabeled at a node;
  no controlling branch was missing; no illegible render. Zero FINDINGs across MER-001..015.
- `.mmd` sources and PNGs are under `_run/s9/p4/render/`; verdicts at
  `_run/s9/p4/out/MER-P1-verdicts.jsonl`; empty findings at `_run/s9/p4/out/MER-P1-findings.jsonl`.
