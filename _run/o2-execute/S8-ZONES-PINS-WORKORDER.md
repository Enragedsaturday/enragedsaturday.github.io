# S8 work order — R2 zone catalog + R6 pin-anchor remediation (lane: o2-opus-xhigh)

**Read first:** `_overhaul2/specs/S8-linking-glossary.spec.md` R2 + R6 (+ §5 Method 1–2) ·
`_run/o2-execute/S7-TO-S8-HANDOFF.md` §3 (binding decisions) · exhibit form:
`content/cases/United States v. Walker.md` (each pinned quote = its own paragraph, `^pin-N`
end-of-block) vs the defect form: `content/cases/Kyllo v. United States.md:61` (`^pin-37`
mid-paragraph — dead anchor). Phase-0 seed (re-derive, seed-not-gospel):
`/private/tmp/claude-501/-Users-johngalt-Projects-cssi-quartz/04e025bb-33f5-4efc-b449-0b3e326d139b/scratchpad/s8_phase0.json`
(242 mid-line defs / 208 files by line-level heuristic; your tool does BLOCK-level truth).

## Deliverable 1 — `scripts/s8/zones.py` (R2: the one catalog, encoded once)

The exemption-zone module the linker AND the LINT-5/7 rewrites will import. **This API is a
frozen contract — downstream lanes are being built against it; do not rename or re-sign:**

```python
ZONE_KINDS = ("heading","code","quote","citation","sources","frontmatter","comment","selfpage","casecell")
def compute_zones(text: str, *, page_stem: str | None = None) -> list[dict]:
    """Zones as {start,end,kind} char-offset dicts, sorted, non-overlapping-normalized."""
def mask(text: str, zones: list[dict] | None = None, fill: str = " ") -> str:
    """Same-length text with zone spans blanked (offset-preserving)."""
def is_exempt(offset: int, zones: list[dict]) -> bool: ...
def iter_blocks(text: str) -> list[dict]:
    """Block segmentation {start,end,kind in (para,listitem,blockquote,table,heading,code,frontmatter)}.
    Shared by the pin remediator now and the shingle detector later."""
```

Zone semantics (spec R2, verbatim intent):
(a) headings; (b) code fences + mermaid; (c) direct quotations — any `"…"`/`“…”` span
(quoted opinion text is never marked up); (d) citation strings — reporter volume/page runs
(`799 F.3d 1361`, `533 U.S. 27, 34 (2001)`, `— *Id.* at 37.` citation lines) + parenthetical
history ("(per curiam)", "rev'd on qualified-immunity grounds", "reh'g en banc denied");
(e) `## Sources` sections entire; (f) frontmatter + HTML comments; (g) selfpage — handled as
a *caption-level* rule by the linker (zones.py exposes `page_stem` so the linker can skip
self-mentions; no span math needed beyond providing the stem back); (h) the sanctioned Case
cells of S5-R6 case tables (first column of case tables — read S5 spec R6 for the shape;
those cells are already wikilinked by construction).

**Fixtures:** `scripts/s8/fixtures/zones/` — one .md fixture per zone kind + a mixed fixture;
`python3 scripts/s8/zones.py --self-test` runs them (repo convention: see
`scripts/s7/survey.py` self-test + `scripts/lint/fixtures/`). Every zone kind needs at least
one pass and one near-miss case (e.g. a caption *inside* quoted text stays exempt; the same
caption outside links).

## Deliverable 2 — `scripts/s8/remediate_pins.py` (R6)

Block-level remediation so every `^pin-N` anchor def ends its own block (paragraph or list
item) and Quartz mints the id. Contract:

- Scan `content/**/*.md` using `zones.iter_blocks` (skip code/frontmatter). Classify every
  `^pin-N` **definition** (not `[[…#^pin-N]]` references, incl. `![[` embeds) as
  end-of-block (OK) or mid-block (defect).
- **Fix = split the block** immediately after the pin token (insert blank line) so the pin
  ends its own paragraph; for list items, split into its own list item at the same indent.
  **Content order and wording byte-untouched** — the only permitted edit is whitespace/blank-line
  insertion (+ moving nothing). Walker/Lundin are the rendered target form.
- **Fail-closed:** if the character run after the split point does not begin a new sentence
  or a new quote (i.e. the pin sits genuinely mid-sentence), or the pin sits inside a table
  row, heading, or other structure a paragraph split can't fix — DO NOT EDIT; queue it in
  `_run/o2-execute/S8-PIN-REVIEW-QUEUE.md` with file:line + a one-line reason.
- Default dry-run; `--write` applies. Idempotent (second run = 0 edits). Emits
  `_run/o2-execute/S8-PIN-REMEDIATION.jsonl` — one row per edit `{file, line, pin, action:"split-para"|"split-listitem"}`
  + a header row `{lane:"o2-opus-xhigh", model:"claude-opus-4-8", tool:"remediate_pins", date}`.
- Post-pass verification built in (`--verify`): (1) mid-block pin defs = 0 (minus queued);
  (2) every `[[…#^pin-N]]` / `![[…#^pin-N]]` reference corpus-wide resolves to an
  end-of-block def in its target file (resolve targets by exact stem AND by
  `cases/<stem>` path form); (3) count of pre-existing pin references unchanged.
- `--self-test` with fixtures under `scripts/s8/fixtures/pins/` (mid-para split, list-item
  split, already-clean idempotence, fail-closed mid-sentence queue case, blockquote case).

## Execution steps (in order)

1. Build zones.py + fixtures → self-test green.
2. Build remediate_pins.py + fixtures → self-test green.
3. Dry-run on the corpus; eyeball 5 diffs; then `--write` + `--verify`.
4. `npx quartz build` must stay green (724 in / ~2873 out; do NOT commit anything).
5. Report back: block-level defect count found, edits applied, queue size + queue contents,
   verify output, build result, self-test outputs, and 3 representative before/after diffs.

## Constraints (binding)

- **COMMIT NOTHING** — the orchestrator reviews and commits.
- **Zero CourtListener** (this lane never touches CL, MCP or REST).
- Touch ONLY: `scripts/s8/**`, the two `_run/o2-execute/S8-PIN-*` artifacts, and content
  edits strictly of the whitespace-split form above.
- Do not edit `scripts/lint/**` (the LINT rewrites are a later lane), do not edit the
  Case Index, coverage ledger, lake, or registry (single-writer surfaces).
- Python 3 stdlib only (repo convention; no new deps).
