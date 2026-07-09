# S8 work order — R3 adjudication-queue resolution (lane: o2-opus-xhigh, READ-ONLY analysis)

**Input:** `_run/o2-execute/s8-adjudication-queue.jsonl` (187 rows: 135 ambiguous-short-name ·
49 unknown-caption · 3 ambiguous-caption) · `_run/o2-execute/s8-caption-index.json` ·
`_run/s6-coverage-ledger.json` · the content files each row points at (read the surrounding
context; the sentence's subject-matter, cited reporter volume, court, year, and quoted text
identify the intended case) · the lake records (`_overhaul2/lake/cases/*.json` — citations,
courts, years are decisive evidence).

**Output:** `_run/o2-execute/s8-adjudication-resolutions.jsonl` — one row per queue row:
`{file, line, matched_text, resolution: {target: "<page stem>"|"plain", rationale: "<one line>",
confidence: high|medium|low}, evidence: "<the decisive fact: reporter cite match / year /
court / subject>", lane: "o2-opus-xhigh", model: "claude-opus-4-8"}`.
**WRITE NO CONTENT** — this lane only proposes; the orchestrator reviews (low-confidence rows
individually), then a separate apply step wires the links. S9 re-reviews 100% of these rows.

Rules:
- **Wrong-authority links are worse than no link.** If the context genuinely underdetermines
  the case (no cite, no year, no distinguishing subject), resolve `plain` with rationale
  "underdetermined — left plain" and confidence high. Never guess.
- A short name whose context cites a reporter volume/page → match against the candidates'
  lake citations (decisive). A quoted passage → match against candidates' pin quotes.
- The Carman class: a mention referring to the folded/reversed twin of a page-backed survivor
  resolves `plain` (ledger rule — never resurrect) with the twin named in the rationale.
- **unknown-caption rows (49):** classify each as (a) real case, genuinely uncovered →
  `plain` + tag `s9-coverage-inbox: true` (S9 owns whether to ingest; you NEVER mint);
  (b) pedagogical example caption (the State Citations and Conventions set: Smith v. Jones,
  State v. Smith, etc.) → `plain` + tag `pedagogical: true`; (c) detector artifact (the
  Rabinowitz over-extension) → tag `artifact: true`, no action.
- The 3 bare `Davis v. United States` rows: the 1994 §2255 Davis vs the 2011 good-faith
  Davis — the citing context (Smith v. Illinois L61 = right-to-counsel invocation; State v.
  Demesme = ambiguous invocation) determines which; cite evidence required.

Report: per-class resolution counts, confidence histogram, every LOW-confidence row in full,
and 10 worked examples with their evidence lines. COMMIT NOTHING.
