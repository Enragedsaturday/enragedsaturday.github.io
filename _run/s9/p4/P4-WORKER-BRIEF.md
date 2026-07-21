# P4 worker brief (all fleet lanes read this first)

You are one lane of the S9 P4 sweep fleet (CSSI overhaul-2, branch `overhaul2/execute`).
Repo root: `/Users/johngalt/Projects/cssi-quartz`. Your packet file names your scope.

## Hard rules (violations void your output)
1. **Findings-only.** You report candidates; you NEVER edit `content/`, `_overhaul2/lake/`,
   `_overhaul2/points/registry.yaml`, or any ledger. Fix work happens later under separate
   fix packets. (Exception: packets explicitly marked WRITE-SCOPE list their writable paths.)
2. **No CL MCP, no live CourtListener.** Evidence sources: the lake
   (`_overhaul2/lake/cases/*.json`), the text cache (`~/cssi-lake/cache/text/<opinion_id>.txt`),
   rendered pages (`content/`), run artifacts (`_run/`). If a check NEEDS live CL, emit the row
   with `"needs_cl": true` and move on — the serial lane handles it.
3. **No verdicts.** `verdict`/`adjudication` fields are orchestrator-only. You emit candidates.
4. **Deterministic coverage.** Your summary MUST state: items assigned / items examined /
   items skipped (with reason each). Silent truncation = packet failure.
5. **Evidence per row**: file path + line (or assertion_id / opinion_id + cache offset), the
   exact text you compared, and why it fails. A row a re-reviewer can't reproduce is noise.

## Candidate row format (`p4.candidate.v1`, one JSON object per line)
{"row":"p4.candidate.v1","ws":"<MER|COH|PAIR|S8H|I1|I2|I3|I4|I5|SMP>","packet":"<packet-id>",
 "class":"<short-slug>","severity":"high|medium|low","file":"<repo-rel or lake path>","line":N,
 "assertion_id":"<if known, from _run/s9/assertion-inventory.json>",
 "claim":"<one-sentence defect statement>","evidence":"<compared texts + source refs>",
 "needs_cl":false,"lane":"<packet-id>","model":"claude-opus-4-8"}
Write rows to `_run/s9/p4/out/<packet-id>-findings.jsonl` (create if absent; append-only).
Also write `_run/s9/p4/out/<packet-id>-summary.md`: coverage numbers, method, anything
ambiguous you want the orchestrator to rule on.

## Reference points
- Standards: `docs/STANDARDS.md`; specs in `_overhaul2/specs/` (S9 governs; S1 lexicon/lint).
- Assertion inventory: `_run/s9/assertion-inventory.json` (join key `assertion_id`).
- Registry parse: stdlib-only via `scripts/lint/_common.py::parse_yaml_subset` (no PyYAML).
- Mermaid render recipe: write block to `in.mmd`;
  `npx -y -p @mermaid-js/mermaid-cli mmdc -i in.mmd -o out.png -p pptr.json -b white -w 1000`;
  `pptr.json` = {"executablePath":"<chrome-headless-shell under ~/.cache/puppeteer>",
  "args":["--no-sandbox","--disable-setuid-sandbox"]}. Then visually Read the PNG.
- Prior-phase conventions: star-verified iff star page cache-confirmed; slip pins slip-only;
  6-tier lexicon exact strings per S1 A8; treatment 3-field + dual dates.
- Do NOT re-litigate adjudicated P2/P3 items: check `_run/s9/adjudications.jsonl` before
  filing a row on something that already carries a verdict (cite the adjudication id if you
  believe it was applied wrong — class `adjudication-regression`).
