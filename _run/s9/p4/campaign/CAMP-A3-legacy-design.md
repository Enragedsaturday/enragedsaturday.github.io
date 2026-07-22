# CAMP-A3 — LINT-11 legacy design report (partition ii)

Packet: CAMP-A3 · lane `CAMP-A3` · model `claude-opus-4-8` · branch `overhaul2/execute`
Governing law: **S1 A2** (R14-broadened pipeline-vocab ban) · `scripts/lint/lint11_pipeline_vocab.py`
docstring · RULING **P4-16(d)**. This is a **findings/design** artifact — partition (ii) is **not**
edited by this packet (`do NOT mass-edit`); it is scoped, counted, and handed to Wave B.

---

## 1. What the committed exclusion-list design actually is

Read from the lint source + `scripts/lint/fixtures/lint11-allowlist.json` + S1 A2 (spec lines
255–305). The lint bans five grep classes over **rendered prose only** — frontmatter, HTML
comments, fenced code, and inline-code spans are masked first; the About page is allowlisted by
stem/title. Its exclusion design has exactly **three** legitimate escape hatches, and no more:

1. **Class-1 committed safe-context list** (`_DEFAULT_ALLOWLIST`, always live): `S\. Ct\.`,
   `L\. Ed\.`, `F\.\s?(2d|3d|4th)`, `§\s?\d`, `No\.\s?\d`, docket `\d{2}-\d`. A class-1 hit whose
   ±18-char context matches any of these is suppressed. This is the "reporter cites / statute
   sections / docket formats never match" carve-out named in the S1 A2 pattern table. **It is
   class-1 only** (`if cls == "1" and any(...)`).
2. **`safe_context_patterns`** (allowlist file, currently `[]`): appends more class-1 safe
   contexts. Empty on disk — nothing added.
3. **`adjudicated_hits`** (allowlist file, currently `[]`): per-hit `"<relpath>:<match>"` keys that
   clear a hit of **any** class. The docstring names this as the sanctioned path for a *semantic*
   false positive ("a physical `wrapper`, a legal `split from`, an English `placeholder`") — "the
   lint author never suppresses; the orchestrator adjudicates entries in" under `CHECKLIST:D10`.

**What the design does NOT contain — the load-bearing negative finding.** There is **no
Sources-note carve-out**, no "provenance parenthetical" exemption, no `S[1-9]`/`R\d` allowance in
rendered bullets. S1 A2 line 273: *"Where such state must persist, it moves to an **HTML comment**
… or a **frontmatter key** — never rendered prose."* S1 A2 line 281 names the current spec-ref
prose the *"today's live leaks"* whose stripping is *"S7 work (register TEACH-02c)."* S7 R (spec
lines 138–139) sets the standard as *"S1 A2's five grep classes = 0 over reader-facing text,"* and
S7 lines 109/253 put every conversion's provenance in the **research annex (§11) / the S9 ledger
row**, never in a reader-facing Sources note. I grepped all nine specs for any language that
*sanctions* a spec-ref in rendered Sources prose (`may cite`, `allowed in prose`, `sources … may`,
`provenance … render`) — **zero hits**. So a Sources-note `per S2 A3` is a leak, not a convention.

**Consequence for triage.** A legacy hit is *intended-excluded* **iff** it is a semantic false
positive the regex over-matched (escape hatch #3, or a regex word-boundary fix). Everything else —
including every spec/rule ref in a rendered Sources note — is a **genuine leak** the design intends
caught and stripped (Wave B / relocate to HTML comment or frontmatter).

---

## 2. Partition of the 227 legacy rows

| Group | Rows | Lines | Files | Disposition |
|---|---|---|---|---|
| **FP** — semantic false positives | 14 | 13 | 7 | **Intended-excluded** → `adjudicated_hits` / regex fix; **no content edit** |
| **B1** — root-index roster provenance | 123 | 41 | 1 | Genuine leak → Wave B (one template) |
| **B2** — Sources-note pin-conversion provenance | 77 | 64 | 59 | Genuine leak → Wave B |
| **B3** — body-prose rule refs | 11 | 8 | 8 | Genuine leak → Wave B |
| **B4** — `No standalone case page` meta-label | 2 | 2 | 1 | Genuine leak → Wave B |
| **Total** | **227** | | | 14 excluded-by-design + 213 genuine leaks |

Token tallies: FP `pending Cl`×8, `wrapper`×4, `split from`×1, `placeholder`×1. B1 `S3`×41 +
`S6`×41 + `S7`×41. B2 `S2`×44, `R5`×14, `S7`×11, `S6`×2, `R15`×2, `L6`/`SR-5`/`R14`/`S1`×1 each.
B3 `R15`×4, plus `L6`/`N1`/`SR-5`/`S4`/`R11`/`R10`/`S7`×1 each. B4 `No standalone case page`×2.

---

## 3. FP — surfaces the design INTENDED excluded (no reword)

These are regex over-matches on ordinary legal/English text, not pipeline vocabulary. The design's
sanctioned remedy is `adjudicated_hits` (per-hit, CHECKLIST:D10) — except the `pending Cl` class,
which is a genuine **regex defect** and is better closed with a one-line word-boundary fix.

| FP class | Hits | Files | Why it is a false positive | Recommended remedy |
|---|---|---|---|---|
| `pending Cl` (class 3, `pending CL`) | 8 | Landor (×6), Case Index (×1), Suing Federal Officers (×1) | Matches **"S​pending Cl​ause"** — the pattern `pending CL` has no left word-boundary, so it fires inside *Spending Clause* (a load-bearing legal term; RLUIPA/§1983 pages). Not a status marker. | **Regex fix** in lint: `(?<![A-Za-z])pending CL` (or `\bpending CL\b`). Closes all 8 + any future *Spending Clause* page. Cleaner than 8 `adjudicated_hits`. |
| `wrapper` (class 5a, `\bwrapper\b`) | 4 | Loines (×2), Case Index (×1), Plain View Doctrine (×1) | Every hit is the **physical "Black & Mild cigar wrapper"** — the object seen in the plain-view search. Not the internal-artifact "wrapper". | `adjudicated_hits`: 4 keys (physical-object noun). |
| `split from` (class 2) | 1 | United States v. Robinson (4th Cir. en banc):79 | Legal **circuit-split** language ("illustrates a circuit split"), not a re-homing provenance note. | `adjudicated_hits`: 1 key. |
| `placeholder` (class 4) | 1 | CREW.md:33 | Pedagogical prose: *"'Recognized Exception' is a **placeholder** for a whole syllabus."* Reader-facing teaching use, not a stub meta-label. | `adjudicated_hits`: 1 key. |

Suggested `lint11-allowlist.json` seed (orchestrator adjudicates in under CHECKLIST:D10):

```json
"adjudicated_hits": [
  "content/cases/United States v. Loines.md:wrapper",
  "content/legal-system-research-and-reference/Case Index.md:wrapper",
  "content/searches/Plain View Doctrine.md:wrapper",
  "content/cases/United States v. Robinson (4th Cir. en banc).md:split from",
  "content/instructor-craft-and-study/CREW.md:placeholder"
]
```
Plus the one-line regex hardening for `pending CL` (a lint-amendment, not a content edit — outside
CAMP-A3 write-scope; flagged for the lint-owner lane).

---

## 4. Genuine leaks — Wave-B surfaces (per-file counts)

### B1 — root-index roster provenance (123 rows / 41 lines / `content/index.md`) — the dominant class (54%)
One template repeated on all 41 category-roster entries:
`- [[X]] — *placed by S3 — S6 verifies cases, S7 authors prose.*`
This is a verbatim pipeline description (which phase places / verifies / authors) in reader prose.
**Highest-leverage Wave-B target**: one mechanical edit clears 123 of 213 genuine leaks.

### B2 — Sources-note pin-conversion provenance (77 rows / 64 lines / 59 files)
Spec/rule refs in `## Sources` parentheticals recording *why* a pinpoint is in slip/case form:
`per S2 A3` (S2×44), `per S7 R5` / `R5 T3` / `S7 R5 T3` (S7×11 + R5×14), plus stragglers. Per S1 A2
this state belongs in an HTML comment / the S9 ledger, not the rendered bullet. **Note:** this class
includes the 10-line `R5 T3` family that CAMP-A3 partition (i) deliberately did **not** touch — it
carries legacy `S7`/`R5` spec-refs and is not in the FIX-T3 footprint, so it is Wave-B, not
P4-authored. Heaviest files: Emergency Aid (9), Community Caretaking (6), Exigent Circumstances (4);
the remaining 56 files carry 1–2 each (long tail — best done as a mechanical per-parenthetical
reword packet, not hand-editing 59 files).

### B3 — body-prose rule refs (11 rows / 8 lines / 8 files)
`R15 treatment audit` narrative refs (R15×6 across Florida v. Meyers, Brendlin, Jacobson, Kuhlmann,
Case Index, State v. Christensen) + scattered `N1`/`SR-5`/`S4`/`R11`/`R10`/`L6`/`S7` singletons in
recent-developments / status prose. These are in narrative sentences — reword in the editorial pass,
not mechanically.

### B4 — `No standalone case page` meta-label (2 rows / `Entrapment.md:100–101`)
Explicitly enumerated in S1 A2 class-4 ("×12 files live today"); 2 survive. Reader-facing meta-label
`(Binding in-circuit — 8th Cir.; no standalone case page)`. Drop the trailer (the fact, if needed,
moves to an HTML comment).

---

## 5. Five worked Wave-B reword shapes (illustrative — NOT applied)

1. **B1 index roster** (×41, one template) — drop the pipeline trailer:
   `- [[Trespass]] — *placed by S3 — S6 verifies cases, S7 authors prose.*`
   → `- [[Trespass]]`   *(placement provenance belongs in the S9 ledger / an HTML comment, per S1 A2)*

2. **B2 `per S2 A3` Sources note** (Landor:79 exemplar) — swap the spec-ref for its plain reason:
   `… no U.S. Reports cite assigned yet (S2 A3 slip precedent).`
   → `… no U.S. Reports cite assigned yet (Current-Term slip opinion; official-reporter pagination not yet issued).`

3. **B2 `S7 R5 T3` conversion note** (Newman/Securing the Scene exemplar) — plain-English the reason:
   `(F.4th reporter cite; post-2020 slip pins paraphrased per S7 R5 T3)`
   → `(F.4th reporter cite; the CourtListener text is the slip opinion, so interior pinpoints are paraphrased rather than page-cited)`

4. **B3 `R15` body prose** (Brendlin/Jacobson exemplar) — drop the rule id:
   `… remain unresolved pending the R15 treatment audit.`
   → `… remain unresolved pending a treatment-history audit.`

5. **B4 `No standalone case page`** (Entrapment:100) — drop the meta-label:
   `(Binding in-circuit — 8th Cir.; no standalone case page)`
   → `(Binding in-circuit — 8th Cir.)`

All five preserve legal content and introduce no new banned token (each candidate string was
checked against the five S1 A2 classes).

---

## 6. Recommendations to the orchestrator

- **Adjudicate the 14 FP** in via one `lint11-allowlist.json` edit (5 `adjudicated_hits` above) **plus**
  a one-line `pending CL` word-boundary regex hardening (lint-owner lane). This clears 14 CI-red
  hits that are not defects, unblocking a green baseline for the genuine-leak work.
- **Wave-B packet split** (by shape, not by file): (B1) one `content/index.md` roster pass — 123/41;
  (B2) one mechanical Sources-parenthetical reword pass — 77/64/59 (the `R5 T3` family rides here);
  (B3+B4) one editorial pass — 13/10/9. Total genuine-leak reword = 213 rows / 92 lines.
- **Expected post-Wave-B state:** LINT-11 highs → the 14 FP only, which the allowlist/regex retires
  to 0 → **green**. No `_review-needed` escalation required (no spec-vs-build conflict here, unlike
  P4-04 deep-equals — S1 A2 is unambiguous that these are leaks).
