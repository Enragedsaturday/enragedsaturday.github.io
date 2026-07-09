# S8 pin-anchor review queue (R6 fail-closed)

> lane `o2-opus-xhigh` · model `claude-opus-4-8` · 2026-07-09
>
> Each row is a mid-block `^pin-N` definition the remediator refused to edit
> because a whitespace paragraph split cannot fix it without touching wording
> or structure. A writer lane resolves each; S9 reviews. NOT auto-edited.

- `content/cases/Steele v. United States.md:56` — `^pin-503b` — pin sits mid-sentence — the run after it does not begin a new sentence or a new quote

## Disposition (orchestrator, 2026-07-09)
- `Steele v. United States.md` `^pin-503b` — ADJUDICATED + FIXED by the orchestrator (Fable):
  anchor MOVED to end-of-block (spec R6's sanctioned "or the anchor moved" branch — the block
  contains the pinned quote, so block-anchor semantics are preserved; zero inbound deep links).
  The em-dash parenthetical `— *Id.* —` reads correctly without the interposed token.
  Post-fix: LINT-9 HIGH = 0 corpus-wide; remediate_pins --verify PASS. Queue is now EMPTY.
