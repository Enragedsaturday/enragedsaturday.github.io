# MER-P5 summary (S9 R11 Mermaid pass)

**Lane:** MER-P5 · **Model:** claude-opus-4-8 · **Scope:** MER-061 .. MER-075 (15 blocks)

## Coverage (deterministic)
- Assigned: 15
- Examined: 15 (rendered + visually Read PNG + Read host page + node/branch/label compare vs page rule)
- Skipped: 0
- Render: 15/15 `ok` (npx mmdc, pptr.json chrome-headless-shell, -b white -w 1000)
- Legible: 15/15 `true`
- Faithful: **15/15 PASS**, 0 FINDING

## Method
For each block: extracted body from `mermaid-blocks.json` -> `render/MER-0NN.mmd`; rendered to `render/MER-0NN.png`; visually inspected the PNG; Read the full host `.md`; compared every node, decision branch, and case label against the page's black-letter rule, Brief, decision structure, and Key-cases table. Cosmetic-only issues recorded as PASS-with-note per brief. No CL, lake-only + rendered pages.

## Blocks (all PASS)
| id | page | verdict |
|---|---|---|
| MER-061 | Community Caretaking | PASS — 3-way triage (home barred Caniglia / vehicle Cady+inventory / person Garner+Rideau, mental-health Graham) faithful |
| MER-062 | Destruction of Evidence | PASS — King forfeit, McNeely/Mitchell/Cupp dissipation, McArthur/Segura freeze faithful |
| MER-063 | Emergency Aid | PASS — Brigham City basis-to-believe, Ryburn, Case v. Montana no-further-gloss, Mincey/Tyler/Clifford end faithful |
| MER-064 | Entry to Arrest | PASS — Payton/Steagald warrants, Vaneaton vs Nora/Al-Azzawy/Maez, Harris remedy faithful |
| MER-065 | Exigent Circumstances & Hot Pursuit | PASS — PC->King->3 exigencies->continuity(Newman)->felony/misdemeanor(Welsh/Lange) faithful |
| MER-066 | Securing the Scene | PASS — Buie two tiers, McArthur/Segura freeze, Summers-line detain, Mincey/Thompson/Flippo faithful |
| MER-067 | Border Searches | PASS — Almeida-Sanchez/Ramsey/Montoya + device split (9/4/1 RS, 11 none, manual routine) faithful |
| MER-068 | Special Needs & Administrative | PASS — purpose gate + persons-balance categories + premises(Camara/Burger) faithful |
| MER-069 | SIA Alcohol Tests | PASS — breath rides arrest / blood needs warrant-consent-exigency (Schmerber/McNeely/Mitchell) faithful |
| MER-070 | SIA Cell Phones | PASS — seize OK, physical 387 / data warrant 403 (Riley), Carpenter alt faithful |
| MER-071 | SIA Persons | PASS — Knowles/Moore predicate, Preston/Shipley/Chadwick contemporaneity, Robinson/Chimel faithful |
| MER-072 | Automobile Exception | PASS — Collins curtilage, mobility+PC, Ross/Acevedo/Houghton scope, Chambers/Johns/Thomas timing faithful |
| MER-073 | Checkpoints & Roadblocks | PASS — Edmond purpose gate, Brown balance, Prouse floor, Sitz/Lidster/Martinez-Fuerte poles faithful |
| MER-074 | Inventory Searches | PASS — lawful custody -> standardized policy (Wells) -> no-ruse (Wells/Bertine) -> valid (Opperman/Bertine/Lafayette) faithful |
| MER-075 | SIA Vehicles | PASS — Gant two prongs, neither->no SIA, Belton/Thornton scope, other-theories alt faithful |

## Cosmetic notes carried to verdict rows (non-substantive; no FINDING owed)
1. **MER-062** — `K -> FREEZE` is an unlabeled parallel edge (the preserve-only freeze alternative, McArthur/Segura). Reads as an available option rather than a labeled branch outcome; content correct.
2. **MER-067** — the `Manual search (broad consensus)` out-edge hangs off the device-split node `E` whose incoming edge is labeled `Forensic search of an electronic device`. Substance is correct (manual = routine, forensic = split), but a manual outcome nested under a "Forensic" parent edge is a minor structural imperfection. Flagged for the orchestrator; not a faithfulness defect.
3. **MER-071** — `CT -> W` (wingspan/immediate-control) edge is unlabeled, reading as the companion of the `yes` person-search branch.
4. **MER-075** — one edge-label ((a) prong) text slightly overflows its highlight box on the left; fully legible.

## For orchestrator
No legal-assertion FINDINGs; `MER-P5-findings.jsonl` is intentionally empty. The four cosmetic notes above (esp. MER-067's manual-under-forensic nesting) are the only items a re-reviewer might want to eyeball; none rise to a candidate row. No `needs_cl`.
