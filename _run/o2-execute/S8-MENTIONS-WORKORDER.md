# S8 work order — R1/R3/R12 case-mention link pass (lane: o2-opus-xhigh)

**Read first:** spec `_overhaul2/specs/S8-linking-glossary.spec.md` R1 + R2 + R3 + R12 (+ §5
Method 3) · handoff `_run/o2-execute/S7-TO-S8-HANDOFF.md` §2.2/§3 · the normative density
exhibit `content/warrant-exceptions/Knock and Talk.md` (link forms below are exactly its
forms) · `scripts/s8/zones.py` (the frozen R2 zone contract — IMPORT it, never re-implement
zone logic).

## Normative link forms (from the exhibit — byte conventions)

- Full caption, italicized in prose: `*Florida v. Jardines*` → `*[[Florida v. Jardines]]*`
  (italics stay OUTSIDE the wikilink).
- Full caption, non-italic prose: `Florida v. Jardines` → `[[Florida v. Jardines]]`.
- Short name: `*Jardines*` → `*[[Florida v. Jardines|Jardines]]*`.
- Possessive short name: `*Terry*'s` → `*[[Terry v. Ohio|Terry]]*'s` (apostrophe outside).
- NEVER touch: existing wikilinks/markdown links (mask first), R2 zones, `id.`/`Id.`
  (the R4 lane owns id.-chains), eponym phrases (below).

## Deliverable 1 — `scripts/s8/caption_index.py`

Builds `_run/o2-execute/s8-caption-index.json` from three sources (no CL, all local):
1. **Lake** (`_overhaul2/lake/cases/*.json`): record_id + identity.case_name +
   case_name_short + case_name_full + input_case_name per record, with status.
2. **Case pages** (`content/cases/*.md`): stem + frontmatter `aliases:` (the wikilink
   truth — a mention links only to an existing page stem/alias).
3. **Coverage ledger** (`_run/s6-coverage-ledger.json`): caption/canonical → `terminal`
   state (the R1 ledger rule: `authored` ⇒ must link; `brief-mention`/`excluded-remit`/
   `unverifiable`/`removed`/`folded-alias`/`watch` ⇒ stays PLAIN, never resurrected).
Output per caption: `{caption_key, page_stem|null, terminal, short_names[], variants[]}`.
Short-name derivation: identity.case_name_short when present; else the non-governmental
party surname convention (United States v. X → *X*; X v. State-name → *X*); ALSO index
every parenthetical-year variant present in stems (`United States v. Smith (2024)`).
Collision map: any short name or caption claimed by >1 page ⇒ marked ambiguous (feeds the
R3 ladder rung 3 fail-closed).

## Deliverable 2 — `scripts/s8/link_cases.py` (the R1–R3 auto-linker)

- Walks a file set (`--paths`, default `content/`), masks R2 zones via `zones.mask`,
  finds every full-caption AND short-name mention of an indexed caption.
- **Eponym guard:** load eponym phrases from the term register
  (`scripts/lint/term-register.yml`; until the R7 columns land, use the built-in seed list:
  Terry stop/frisk, Miranda warnings/rights/waiver, Katz test, Brady material/violation,
  Franks hearing, Batson challenge, Garrity warning/statement, Kastigar hearing, Daubert
  standard, Monell claim/liability, Bivens action/claim, Chimel rule, Belton rule, Gant
  rule, Rodriguez moment, Montejo rule, Massiah rule, Edwards rule, Salinas rule, Miranda
  card) — a case name inside a register eponym phrase is NOT a case mention (routes as a
  term in the R7 lane). The bare italic name (`*Terry*`) IS a case mention.
- **R3 fail-closed ladder for short names** (in order, stop at first unique hit):
  1. page-scope binding — an earlier same-page full-caption mention (linked or plain-but-
     ledger-plain) binds that short form for the rest of the page;
  2. page-roster — unique match against the page's frontmatter `homes:`/Key-cases table/
     Related/Sources captions;
  3. corpus caption index — unique match corpus-wide.
  Ambiguous at every rung ⇒ NO edit; emit an adjudication-queue row.
- **Ledger rule:** mention of an `authored` caption ⇒ link. Non-page terminal ⇒ leave
  plain, action `plain:no-page`. Caption in NO index source ⇒ leave plain, queue row
  `unknown-caption` (S9 coverage inbox — never auto-link, NEVER mint).
- **Self-page rule (zone g):** on a case page, mentions of that page's own caption stay
  plain.
- Emits R12 ledger rows per occurrence (append-safe JSONL →
  `_run/o2-execute/s8-link-ledger.rows.jsonl`, one row:
  `{file, line, matched_text, caption_key, resolution:{target, method: caption|page-scope|roster|corpus|adjudicated, rationale?}, action: linked|linked-deep|plain:no-page|plain:adjudicated|exempt:<zone>, lane, model}`)
  — the R12 assembler (later lane) consumes these. Queue rows →
  `_run/o2-execute/s8-adjudication-queue.jsonl` `{file, line, matched_text, candidates[], reason}`.
- Default dry-run; `--write` applies; idempotent (re-run ⇒ 0 new edits, rows re-derive
  identically); `--self-test` with fixtures `scripts/s8/fixtures/mentions/` covering: the
  ladder's 3 rungs, ambiguity queue, eponym guard, ledger-plain rule, unknown-caption,
  self-page, italic/possessive forms, zone exemptions (one per zone kind).

## Execution steps

1. Build + self-test both scripts (green).
2. Run caption_index; report collision map size + sample.
3. Dry-run link_cases on ONE category (`content/warrant-exceptions/`); report stats +
   10 sample diffs + queue rows. **STOP and wait for orchestrator approval** (SendMessage
   pattern: your report ends the turn; the orchestrator reviews and replies GO/adjust).
4. On GO: run `--write` per category batch in this order, one report line each:
   foundations-and-the-fourth-amendment · searches · seizures · the-warrant ·
   warrant-exceptions · standards-of-proof · the-exclusionary-rule-remedies-and-standing ·
   confessions-interrogation-and-the-fifth-amendment · the-right-to-counsel ·
   fair-trial-and-reliability-doctrines · use-of-force-and-liability ·
   legal-system-research-and-reference · instructor-craft-and-study · cases ·
   root index.md + about.md.
5. `npx quartz build` green after the full pass. Recount: bare authored-caption mentions
   remaining = 0 outside zones/queue (report the grep).

## Constraints (binding)

- COMMIT NOTHING (orchestrator commits per batch review). Zero CL. Stdlib only.
- Touch only `scripts/s8/**`, the three `_run/o2-execute/s8-*` artifacts, and content
  edits of exactly the link-wrapping form (wording/order byte-identical otherwise).
- Do NOT link inside `## Sources` (zone e), do NOT create new pages, do NOT edit
  single-writer surfaces (Case Index / coverage ledger / lake / registry).
- The adjudication queue is NOT yours to resolve — rows carry candidates + reason only.
