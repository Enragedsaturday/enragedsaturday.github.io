# S8 work order — R9 transclusion embeds via shingle detector (lane: o2-opus-xhigh)

**Read first:** spec R9 (+ §5 Method 7, Decision Log SD2/D6) · exhibits on
`content/searches/Curtilage.md` (commit 981b286/51e1f4b: the [!rule] shell embed + the
pinned-quote embed — the two flavors, rendered live) · `scripts/s8/zones.py` (frozen;
`iter_blocks` is your block segmentation) · S1 A3 (the shingle detector is S1's mechanism —
read its spec text in `_overhaul2/specs/S1-standards.spec.md`; if a detector implementation
already exists in scripts/, extend it, don't fork it — check `scripts/` + `grep -r shingle scripts/`).

## Deliverable 1 — `scripts/s8/shingles.py` (detector)

- Tokenize prose blocks (outside R2 zones; embeds `![[…]]` excluded from matching by
  construction) and detect ≥25-token overlapping runs (shingled n-gram compare) between:
  (a) any prose block and any FOREIGN page's `^rule-*` callout block; (b) any prose block
  and any FOREIGN case page's `^pin-N` block (the pinned quote). Same-page overlap is fine
  (a page may restate its own rule).
- Output `_run/o2-execute/s8-shingle-report.jsonl`: `{file, line, overlap_tokens, source_page,
  source_anchor, kind: rule|pin, snippet}` + a summary. `--self-test` + fixtures
  `scripts/s8/fixtures/shingles/` (above/below threshold, embed-excluded, same-page-excluded,
  quote-zone handling).

## Deliverable 2 — conversion proposals (ADJUDICATION INPUT, no content writes yet)

For every detector hit, propose the conversion in
`_run/o2-execute/S8-EMBED-PROPOSALS.md`: the offending block · the proposed embed —
**(a) rule embeds:** `![[<full-slug>#^rule-<tail>]]` inside a `> [!rule] Black-letter rule —
stated on [[Home Page]]` shell; **(b) pinned-quote embeds:** `![[cases/<Case>#^pin-N]]`
replacing a re-typed block quote (short inline snippets woven into a sentence stay ordinary
quoted text — NOT embed candidates) · what prose (if any) remains around it. **FULL-SLUG
targets only** (the alias-stub resolver trap — spec R9; verify each target resolves as a
full slug against the actual file tree). STOP after the report — the orchestrator adjudicates
which conversions apply (an embed changes rendered content; that is a judgment surface).

Constraints: COMMIT NOTHING · zero CL · stdlib only · read-only vs content until the
orchestrator's apply GO · do not touch other lanes' scripts or artifacts.
