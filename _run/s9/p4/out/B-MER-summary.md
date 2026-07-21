# B-MER bootstrap summary (WS=MER)

Packet: B-MER (bootstrap). Lane/model: claude-opus-4-8. Write-scope: `_run/s9/p4/` only.
Findings-only bootstrap — no `content/` edits, no diagram adjudication (fleet does that).

## 1. Extraction results

- **Total mermaid blocks extracted: 75** → `_run/s9/p4/mermaid-blocks.json`
- **Files containing ≥1 block: 75** (exactly one ```mermaid block per file; zero files with multiple blocks)
- Markdown files scanned under `content/`: 724
- Ordering: `mermaid-blocks.json` array is sorted by repo-relative file path; ids assigned
  sequentially in that order (`MER-001` … `MER-075`).

### Schema (per element)
`{"id":"MER-NNN","file":"<repo-rel>","line_start":N,"line_end":N,"body":"<raw block body>"}`
- `line_start` = 1-based line of the ```mermaid opening fence.
- `line_end` = 1-based line of the closing ``` fence.
- `body` = raw text between the fences (fence lines excluded), trailing newlines stripped.

### Extraction method
- Recursive walk of `content/` for `*.md`; per file, regex `^\s*```+\s*mermaid\s*$`
  (case-insensitive) opens a block, next `^\s*```+\s*$` closes it. Indented fences tolerated.
  Cross-checked against `grep -rc '```mermaid'` = 75 files / 75 fences. No unterminated blocks.

## 2. Render harness — CONFIRMED WORKING

### chrome binary used
`chrome-headless-shell` found under `~/.cache/puppeteer` (system Chrome fallback NOT needed):
`/Users/johngalt/.cache/puppeteer/chrome-headless-shell/mac_arm-150.0.7871.24/chrome-headless-shell-mac-arm64/chrome-headless-shell`

### pptr.json that worked (`_run/s9/p4/render/pptr.json`)
```json
{
  "executablePath": "/Users/johngalt/.cache/puppeteer/chrome-headless-shell/mac_arm-150.0.7871.24/chrome-headless-shell-mac-arm64/chrome-headless-shell",
  "args": ["--no-sandbox", "--disable-setuid-sandbox"]
}
```

### render command (run per block from `_run/s9/p4/render/`)
```
npx -y -p @mermaid-js/mermaid-cli mmdc -i MER-00N.mmd -o MER-00N.png -p pptr.json -b white -w 1000
```
Recipe: write block `body` to `<id>.mmd`, then run the command above. All 3 exited clean
("Generating single mermaid chart", no errors), producing non-trivial PNGs (77–109 KB).

## 3. Sample render verdicts (first three blocks, visually Read)

| id | file | verdict |
|----|------|---------|
| MER-001 | content/confessions-interrogation-and-the-fifth-amendment/Due-Process Voluntariness of Confessions.md | **LEGIBLE** — full flowchart (Connelly→coercion/causation→voluntary vs involuntary + McNabb-Mallory branch + Chapman/Fulminante harmless-error tail); all node text crisp. |
| MER-002 | content/confessions-interrogation-and-the-fifth-amendment/Miranda Waiver and Invocation.md | **LEGIBLE** — waiver/invocation flowchart renders; all nodes/edges present and readable. Cosmetic only: two edge labels ("Butler / Thompkins", "Counsel present · Minnick") sit under adjacent labels — diagram-content layout artifact, not a harness failure. |
| MER-003 | content/confessions-interrogation-and-the-fifth-amendment/Miranda and Custodial Interrogation.md | **LEGIBLE** — custody→interrogation→Quarles public-safety flowchart; all node text and Yes/No edge labels clear. |

All three are non-blank, non-error, and legible. Harness green for the fleet.

## 4. Coverage
- Assigned: bootstrap (extract all mermaid blocks + prove render harness).
- Examined: 724 md files scanned; 75 blocks extracted; 3 blocks rendered + visually verified.
- Skipped: diagram-by-diagram correctness inspection of MER-004…MER-075 — **out of scope by
  design** (fleet lanes inspect all diagrams; this packet only bootstraps).

## 5. For the orchestrator
- Fleet lanes can consume `_run/s9/p4/mermaid-blocks.json` directly (stable ids MER-001…075).
- Reuse `_run/s9/p4/render/pptr.json` verbatim; the `~/.cache/puppeteer` chrome-headless-shell
  path is valid on this machine, so system-Chrome fallback is unnecessary.
- Minor label overlaps like MER-002's are inherent to dense diagram bodies, not render defects;
  lanes judging legibility should distinguish content-layout crowding from harness failure.
