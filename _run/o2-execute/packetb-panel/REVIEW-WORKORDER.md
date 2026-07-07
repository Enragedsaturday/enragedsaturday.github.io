# S6 Packet B — independent reviewer work order

You are ONE of TWO mutually-blind reviewers adjudicating the 16 borderline items in
`_run/o2-execute/packetb-panel/ITEMS.md` (read it first; paths are relative to the repo root
`/Users/johngalt/Projects/cssi-quartz`). A third adjudicator will reconcile the two reviews.
The user has delegated these dispositions to this panel, so review as if your verdict ships:
research each item until you would sign it, not until an answer merely sounds plausible.

## The project, in brief

CSSI is a federal search-and-seizure instructor wiki for law-enforcement officers (the
students are officers, not lawyers). The corpus teaches Fourth/Fifth/Sixth-Amendment doctrine
as it bears on FIELD work: searches, seizures, suppression, and officers' civil-liability
exposure. Overhaul-2 (O2) is a spec-governed rebuild; wave 3 / spec S6 closes the coverage
gap: every case the corpus relies on gets verified and, if it passes the
officer-field-relevance gate, authored as a case page. Packet B is the human-pause batch of
gate-ambiguous candidates. The user has directed a two-reviewer + adjudicator panel instead
of deciding item-by-item personally.

## Governing texts (read before deciding; cite rules by name in rationales)

- `_overhaul2/specs/S6-coverage-ingest.spec.md` — the controlling spec. Most load-bearing:
  R2 (the gate + prongs + D1 flip), R3 (borderline protocol), R6 + D5 (frontier inclusion
  floor: page iff clearly controlling or split-marker; else Lower-court-developments bullet),
  R9 (alias/fold rules; fold-by-default with a load-bearing-point exception), D1–D8 user
  decisions, §10 GAP-docket dispositions (esp. GAP-04f).
- `_overhaul2/specs/S2-authority-database.spec.md` §R11 (stub states) if lake mechanics matter
  to your reasoning.
- `_run/s6-candidates/gap-docket.jsonl` — the GAP docket rows (item 12 evidence).
- `_overhaul2/lake/_manifest.json` — the lake manifest; grep it to re-verify any lake fact
  ITEMS.md asserts (statuses, cluster ids, cites). Report any mismatch you find.
- The corpus: `content/` — e.g. grep for where a candidate case is named in prose to judge
  whether a point is load-bearing (items 13–16), what the §1983/immunity line already carries
  (items 1–7), and what the exclusionary/forfeiture/expressive-material pages rely on.

## Research rules

- Web research is ALLOWED and expected for the legal substance (what each case actually held,
  its posture, which court, what line of doctrine it sits in). Prefer primary/authoritative
  sources (official slip opinions at supremecourt.gov, court sites, Oyez, SCOTUSblog, Justia,
  Cornell LII). Wikipedia is context only, never load-bearing.
- CourtListener is OFF-LIMITS in every form (REST API, MCP tools, and courtlistener.com in a
  browser/fetch). The run's CL quota is budgeted elsewhere; S6 lanes are zero-CL by spec (R7).
- BLINDNESS: do not open `_run/s6-borderline.md`, `~/briefs/*.html`,
  `_run/o2-execute/JOURNAL.md`, `_run/o2-execute/S6-STEP1-*`, any `frontier-*adjudications*`
  file, or the other reviewer's output. If a web search surfaces this project's own published
  site (cssi-search-and-seizure.vercel.app), do not treat it as authority for a verdict.
- The corpus and specs ARE fair game (they are the decision inputs, not the decision record).

## What to produce, per item

For every item 1–16, decide the disposition from the item's lawful-disposition set. Reason
from: (a) the gate text as written (prongs a/b/c; "EXCLUDE names its craft"); (b) what the
case actually holds (verify via web — do not trust the one-line proposition blindly);
(c) what the corpus actually does with the case today (grep `content/`); (d) the paging rules
(R6/D5/R9) for Group III. For item 12, determine the referent from the gap-docket row text,
the spec §10 GAP-04f line, and web facts about the three Villarreals — then give the per-case
dispositions the referent determination entails.

Guard rails from the corpus's standing policy you must honor (they bound the disposition
space, not the verdict): a cert-denial-with-statement is at most a noted-order mention, never
a page; SCOTUS merits boundary-markers within prong (c) are page-eligible; a page's absence
of any 4A/5A/6A-field or §1983-officer nexus should make you ask "which craft does this
belong to" per R2.

## Output format (STRICT)

Write EXACTLY one file: `_run/o2-execute/packetb-panel/review-<LANE>.jsonl`
(your lane name is given in your launch instructions). One JSON object per line, items 1–16
in order:

{"item": 1, "caption": "Health & Hospital Corp. v. Talevski",
 "verdict": "<one of the item's lawful dispositions, stated exactly>",
 "prong": "<a|b|c|none — Group I/II only>",
 "confidence": "<high|medium|low>",
 "rationale": "<3-8 sentences: the holding as you verified it, the rule(s) applied, why this side of the line>",
 "corpus_evidence": "<what you found in content/ that bears on it, with file paths>",
 "web_sources": ["<url>", "..."],
 "lake_check": "<ok | mismatch: describe>",
 "flags": "<anything the adjudicator must see: split-risk, factual surprises, data anomalies; else null>"}

For item 12 add: "referent": "<City of Laredo | Texas 24-557>",
"per_case": {"villarreal_v_city_of_laredo": "<verdict>", "villarreal_v_texas": "<verdict>"}.
For items 14 and 16 give a per-case verdict map in "per_case" as well.

After the 16 lines, append one final line:
{"item": "SUMMARY", "counts": {...}, "notes": "<anything systemic>"}

Do not edit any other file. Your final chat/text output should be ONLY: the path of the file
you wrote + a one-line count (e.g., "16 items + summary written"). The JSONL is the
deliverable; the adjudicator reads the file, not your chat output.
