# S6 Packet B — final adjudicator work order

You are the THIRD member of the packet-B panel: the adjudicator. Two mutually-blind reviewers
(lanes `fable` and `codex`) have independently adjudicated the 16 borderline items from the
recommendation-stripped ITEMS.md. Your job: reconcile the two reviews AGAINST the full record
and issue the final determination + recommendation per item. The user delegated these
dispositions to this panel ("once the determination is made, then you can implement"), so your
determinations are what the orchestrator implements — sign only what you would defend.

Repo root: /Users/johngalt/Projects/cssi-quartz (all paths relative).

## Inputs, in reading order

1. `_run/o2-execute/packetb-panel/ITEMS.md` — the neutral item statements.
2. `_run/o2-execute/packetb-panel/review-fable.jsonl` + `review-codex.jsonl` — the two blind
   reviews (per-item verdict/prong/confidence/rationale/evidence/flags).
3. `_run/s6-borderline.md` — the ORIGINAL packet WITH the orchestrator's recommendations
   (you are the only panel member allowed to read these; weigh them as one more opinion, not
   as ground truth).
4. The governing spec: `_overhaul2/specs/S6-coverage-ingest.spec.md` (R2 gate + prongs + D1
   flip · R3 · R6/D5 frontier floor · R9 fold rules · §10 GAP-04f) — rule text controls over
   every opinion including the orchestrator's.
5. Wherever the reviewers disagree, or either flags a factual surprise, verify yourself:
   grep the corpus (`content/`), the lake manifest (`_overhaul2/lake/_manifest.json`),
   `_run/s6-candidates/gap-docket.jsonl`, and the web (NO CourtListener in any form — REST,
   MCP, or site).

## Known flags you must resolve (from the fable lane; verify, don't inherit)

- ITEMS.md's "three distinct Villarreals" premise: the fable lane says *Villarreal v.
  Alaniz* (No. 25-29) is the SAME litigation as *Villarreal v. City of Laredo* (the
  Lagordiloca case, renamed on cert). If true, item 12's disposition space changes shape:
  determine what the correct litigation map is and what that does to (a) the GAP-04f
  referent question, (b) the existing Alaniz noted-order ledger row, (c) any City-of-Laredo
  gate verdict (same-litigation R9 fold rules apply).
- Item 15: whether *Hernandez v. Mesa* is actually named in corpus prose (ITEMS asserted it;
  the fable lane says it is not — check `content/` yourself; the D5 floor + D1 flip read
  differently depending on the answer).
- Item 13: the lake record's official_cite "140 F.4th 733" for the 2019 6th-Cir. Carpenter
  remand — both lanes may comment; state what the correct disposition of that data anomaly
  is (it rides the re-key/authoring lane, but name it precisely).

## Decision discipline

- Where the lanes AGREE and the rule text supports them: confirm, briefly.
- Where they DISAGREE: decide on the rule text + verified facts, and say which lane's
  reasoning fails and why. No splitting the difference without a rule basis.
- Where BOTH lanes agree but you find the rule text cuts the other way: the rule wins —
  overrule both, with the citation.
- Every Group-I verdict names its prong (or the craft it remits to). Every Group-III call
  cites the governing rule (R9 fold exception / R6-D5 floor / D1 flip) explicitly.
- A verdict that expands authoring volume (pages) is not a cost decision — decide on the
  rules, note volume implications for the orchestrator.

## Output

Write `_run/o2-execute/packetb-panel/ADJUDICATION.md`:
- A 16-row determination table: item · caption · lane-fable verdict · lane-codex verdict ·
  FINAL determination · rule basis · one-line why.
- Below the table, a per-item section ONLY where the lanes disagreed, either flagged
  something, or you overruled — with your reasoning and the evidence you checked.
- A "premise corrections" section: any ITEMS.md/packet factual assertion you found wrong
  (Villarreal litigation map, Hernandez-in-prose, cite anomalies), each with evidence.
- A final "IMPLEMENTATION NOTES for the orchestrator" section: the concrete ledger states,
  re-keys, page-mints, folds, and mention/bullet placements your determinations entail —
  precise enough to execute without re-deciding anything.

Your final chat message: the path + a one-line per-item verdict list + which items you
overruled or resolved against a lane.