# O2 EXECUTE run journal

One autonomous run per `_overhaul2/wrappers/EXECUTE.wrapper.md`. The signed specs + Amendments are
the law (RUNBOOK §0 precedence). The §0 register's 8 enumerated pauses are the ONLY stops. Done =
the S9 R13 release gate, deployed and verified live.

Checkpoint discipline: one entry per wave step, appended at completion, with commit hash. A fresh
context resumes from this file + the task list.

Model fleet (user decision 2026-07-04): Fable = orchestrator + high-judgment lanes; Opus 4.8 at
xhigh (`o2-opus-xhigh` agent) = heavy structured fleets + Claude panel-vote; Sonnet = pure
mechanical sweeps; Codex gpt-5.5 at xhigh = lake builder + 2 review lanes + case-grain reads +
web-discovery lanes. Exact model ids in every ledger row.

---

## P0 — preflight (2026-07-04)

- Branch: `overhaul2/execute` cut from `overhaul2/planning` (ba5cdd3).
- `o2-opus-xhigh` agent definition present (`.claude/agents/o2-opus-xhigh.md`).
- Codex headless sanity: `codex exec -s read-only -c model_reasoning_effort=xhigh` → OK
  (codex-cli 0.142.4, model gpt-5.5, xhigh confirmed in session header). Codex's own CL-MCP
  transport emits the known expired-OAuth error — expected; the S2 builder uses direct REST v4,
  never MCP (S2 R10). Not a lane outage.
- CL token present, mode 600, `~/.config/cssi/cl-token` (out-of-repo).
- **CL-MCP connector IS reachable from a sub-agent lane** (probe: `search(type="o",
  q="Terry v. Ohio")` → count 40341, top hit Terry v. Ohio). The ≥1-in-10 identity spot-check
  slice (COH-17) may run in Claude sub-agent lanes; orchestrator-session fallback not needed.
  Probe gotcha recorded: `get_counts` takes only a `query_id` from a prior search — not a `q`.
- `.orca/` added to `.gitignore` (COH-14: copyrighted drops are local-only).
- Wave tasks #1–#10 registered in the task tracker with wave-order dependencies.

Next: Wave 0 (S1 rulebook).

## Wave 0 — S1 rulebook (2026-07-04)

- `docs/STANDARDS.md` rewritten (commit 37ef085): 35-rule catalog — O1 carried (L1–L8, N1–N13,
  SR-1…SR-5, D1–D14) with the amended rewrites (L4′ per-credential lanes A1; L8 sharpened R7;
  N4/N5/N13 for 3-field treatment; SR-1 realized via the S2 lake) + the O2 standard rules
  SR-6…SR-14 (3-field vocabulary §3.1 + A4 migration §3.2; 10-gate protocol §5A; AI guardrails
  §5B with the 10-row enforcement map; Variant A §8.1 + project-wide officer-BLUF ban; panel +
  machine ledger §6; pipeline-vocab ban §7.3; slip-op current-term; voice/em-dash/density;
  term register + SSOT). Lexicon = exact A8 allowlist (§3.0). Roster rows 1–14 documented;
  S9 codifies 1–30.
- `docs/STYLE.md` authored (new): precedence stack (project → Bluebook → Chicago + escape
  valve), house style, em-dash budget, Humanizer ADOPT/ADAPT/REJECT, term-register rules
  (machine source = `scripts/lint/term-register.yml`, seeded 23 terms), verified mnemonic
  register (CREW=3, CRON removed), citation style notes.
- Lint scaffolding: two Opus-4.8-xhigh lanes via Workflow (run wf_3af550f7-6a5; the committed
  `o2-opus-xhigh` agent type was not loaded in this session's registry — used the wrapper's
  sanctioned fallback `agent(…, {model:'opus', effort:'xhigh'})`). Lane A: lint9_carat_leak.py +
  lint10_emdash.py + fixture + run_all registration. Lane B: LINT-4 exact allowlist, LINT-5
  fail-closed resolve, LINT-6 3-field/dual-dates/glyph, LINT-7 register consumption.

### Wave-0 review loop (writer ≠ checker) — CLOSED ✅

Codex gpt-5.5 xhigh read-only review of all S1 deliverables → 8 findings (F-S1-01..08) →
adjudicated by the orchestrator (ledger: `_run/o2-execute/wave0-s1-review-ledger.json`) →
fixed (2 by orchestrator-as-fixer, 5 by a fresh Opus-xhigh lane, 1 dismissed-with-reason) →
Codex round-2 re-review: 7 FIXED + 1 residual (F-S1-05 frontmatter authority_weight unvalidated;
UPHELD — draft pages are LINT-12-exempt) → loop-3 fix + round-3 verify: FIXED. ALL-CLEAR.
Notable adjudications: Field-I enum = S2 R5's machine tokens (PRACTICES slash-forms are display
composites — now documented in STANDARDS §3.1); A4 migration counts were genuinely inverted in
the first STANDARDS draft (caught by review — fixed to A4 exact). Lint state at wave close:
LINT-4 = 34 HIGH (21 inversions + 9 prose inversions + 2 non-allowlist + 1 banned phrase + 1
prose suffix-missing — all S7 remediation) · LINT-5 = 126 HIGH broken pin anchors (S8) + 2282
MED bare names (S8) · LINT-6 = 456 LOW legacy-awaiting-projection (S2) · LINT-7 = 118 HIGH
register drift (S3 renames + S7 prose) · LINT-9 = 297 HIGH mid-line pins (S8 R6) · LINT-10 =
3989 HIGH em-dash budget (S7 rewrite pass; [!rule] callouts exempt) · self-test wired
fail-closed into run_all. Wave-0 acceptance (S1 §7): all criteria delivered or explicitly
deferred to their owning spec (LINT-11 → S9 per A2/A5; LINT-3 rebuild → S9; LINT-12/13/14 → S2).

## Wave 1 — S2 lake ∥ S4 platform (2026-07-04)

### S4 platform — wave-1 scope COMPLETE ✅ (R8 retirement deliberately rides Wave 4)

Opus-xhigh lane (wf_a6ab4eda) landed the post-mockup deltas: R3 weight-reading sortFn
(ContentDetails.weight; folder inherit via trie index assignment; unweighted rendering
byte-identical to stock — the one §1983/Brady adjacent swap vs the interim mockup sort is the
intended interim→stock correction, on record); R10c prefix-with-separator; R10d continue; R5
casetable badge = a.internal.treatment-badge (delegation was already in-tree from mockup);
LINT-26 goodlaw-target; R6 tooltip verified already-correct with S2's as_of_content/as_of_treatment
names; R9 fork-posture in README. about.md finalized (R7). Build clean (523 files).
Review loop (Codex xhigh read-only): 4 findings — F-S4-01 HIGH upheld (LINT-26 basename resolve =
false-negative class for the raw-href constant → rewritten to exact-FullSlug matching mirroring
quartz sluggify, incl. loop-2 segment-aware _index fix verified against quartz/util/path.ts
source + unit tests); F-S4-02 about.md alias dropped (R12 literal); F-S4-03 roster docs;
F-S4-04 README wording. Commits: a1b179d · 6dd84e1 · 02a3cb3 · 23778a9.

### S2 lake — builder authored; review loop in flight (CLEAR-TO-SMOKE: no → loop 2)

Codex xhigh authored the lake scaffold (_schema/_advisory/_reporter-precedence/
_treatment-migration/_manifest 458+93/README) + scripts/s2/ingest.py (62KB stdlib) + README;
self-test green (commit cadc668). **Roster drift, fully attributed by the review lane:** 457→458
pages (United States v. Smith (2024) authored at the S6 interview — its roster row self-closed);
89→94 scan rows (+6: Carroll v. Carman, Morgan v. Fairfield County, People v. Frederick, State v.
Christensen — all S6 A1 planning-time discoveries now named in the Knock-and-Talk mockup content —
plus 2 caption variants for S6 to adjudicate: Carman v. Carroll (lower-court caption of the same
litigation) and Morse v. French (cert-denial caption of French v. Merrill)). Manifest = 93
frontier rows (LLC v. John Doe excluded per seed §c).
**Pre-run review (2nd Codex lane, read-only): 9 findings, 7 HIGH — CLEAR-TO-SMOKE: no.** The
review provably paid for itself: resume was run-id-scoped (every relaunch would re-burn ALL
treatment quota), treatment lanes had no partial cursors, a cluster_id could still reach
/opinions/ (the A1 scar), verified+unverified-treatment records violated the schema, 40
circuit/state manifest rows used a court vocabulary the lane filters don't recognize, and the
token bucket allowed a 27-call first minute. All 9 UPHELD → builder lane fixing (loop 2), then
re-review, then smoke (Terry + Chatrie), then the paced run.

### S2 smoke loop (2026-07-04) + THE FULL-RUN LAUNCH RECIPE

Smoke 1 (Terry+Chatrie): DO-NOT-PROCEED — three new findings, all UPHELD and fixed (ledger
updated): F-S2-11 unbounded progeny pagination (bounded per R4/A5: page-1 count + per-sibling
counts + complete_query + cursor; outbound edges persisted for intra_edges) · F-S2-12 budget
exhaustion crashed without persisting (now clean interruption + partial record + checkpoints) ·
F-S2-13 1.0s inter-call gaps (root cause: post-response log timestamps + a real analyze-bucket
bypass; now ONE global ≤14/min gate for every call, analyze's 60/min stacked after it). Chatrie
smoke record committed (first lake record: under_review, name+docket, cluster 10881683 / lead
11349205 — the A1 must-ingest guard passed live). Smoke cap now 80. Codex writable_roots
verified for ~/cssi-lake.

**FULL-RUN LAUNCH RECIPE (repeat until `_manifest.json` shows roster complete; relaunch on each
session-end notification after checking the budget checkpoint in the journal tail):**

```sh
codex exec -s workspace-write -c approval_policy=never \
  -c 'sandbox_workspace_write.network_access=true' \
  -c 'sandbox_workspace_write.writable_roots=["/Users/johngalt/cssi-lake"]' \
  -c model_reasoning_effort=xhigh --skip-git-repo-check \
  -C /Users/johngalt/Projects/cssi-quartz \
  "S2 BUILDER session. CSSI_LAKE_ROOT=/Users/johngalt/cssi-lake python3 scripts/s2/ingest.py \
   --session-minutes 150. On exit report: the end budget checkpoint (calls this session / \
   cumulative / remaining estimate), cases completed this session, current manifest counts by \
   status, any anomalies (429s, backoff events, fabrication_suspected, not_found)." \
  < /dev/null   # run as a BACKGROUND Bash task; commit lake records at each session end
```

Session cadence: ~150 min each; commit `_overhaul2/lake/` after each session (checkpoint
discipline); relaunches are idempotent (stable build_id resume — F-S2-01). Wave 2 (S3+S5)
runs concurrently; S6 waits on lake completion + R15 build-QA.

### S2 PACED RUN LAUNCHED (2026-07-04) — session 1 in flight

Smoke loop closed across 3 iterations + F-S2-14 (transport-timeout resilience; crash-safe
wrapper; record writes confirmed repo-side). Re-smoke #3 live-proved: journal resume (0 calls
before lane-1 cursor resume), pacing (min 4.0s truncated-second gaps), clean interruption +
checkpoints, identity/cites/bounded-progeny on the mega-case. **Orchestrator adjudication:**
Terry (22k progeny) structurally cannot finish treatment inside a smoke budget (lane-1 cap =
200 reads by design); the two un-exercised paths (lane cap_hit evidence · normal-case
three-lane completion) are GATE-CHECKED at the session-1 end-of-session report before session 2
launches. Session 1 = 150 min, launched as background codex task btmj2azgp. Launch recipe above.

## Wave 2 — S3 restructure + S5 entry models (OPENED 2026-07-04)

Gate artifact committed BEFORE any move: `_overhaul2/url-inventory.json` (1,336 pre-move paths
from the emitted HTML set, commit 5519c69) — S3 A1/R13 satisfied. Sequencing: S3 tree
materialization first (content/ structure), S5 table conversion after the tree settles (both
touch content/); S5 component work was already landed by the mockups + S4.

### Wave-2 progress (2026-07-04, continued)

**S3-P1 TREE MIGRATION LANDED (commit aa9b6a6):** 13 unnumbered categories (weights 10–130 =
Appendix A order, independently verified from contentIndex), 48 moves with full old-path aliases,
41 placed-empty nodes, de-rip relabels, cases/ frozen (0 renames) + router index + explorer
unlisting (filterFn, added by orchestrator — the lane correctly flagged it out of its scope),
master index regenerated. Verification: crawl **1336/1336 independently re-confirmed by the
orchestrator**, deck stems 44/44, lint5 HIGH unchanged, clean build 571 files. Two-Definitions
split deferred-as-index (no clean severance; children placed empty; S7 extracts). Known
transients for S7: index pages holding full content while split children are empty;
[[Qualified Immunity]] resolves to §1983's alias until QI is authored. A planning-session
leftover `quartz build --serve` watcher was killed (it raced our builds); legacy :8787 server
left running (its retirement is the Wave-4 R8 step).

**S5 tooling review:** 11 findings (10 blocking) — all UPHELD. **F-S5-11 was the live proof of
the fail-closed design: the migration moved Verifying Good Law and LINT-26 caught the stale
GOOD_LAW_SLUG, naming the correct new path in its message; one-constant edit, green (7f4db81).**
F-S5-01..10 (converter damage classes, LINT-15/16 FP/FN classes, host whitelist, typed-page
fail-closed) dispatched to a fresh fix lane with adjudicated semantics (required doctrine
sections = callout + Brief + Key cases + Sources; placed-empty draft stubs exempt until authored).

**In flight:** S2 paced session 1 (gate-checked before session 2) · S5 fix lane · S3-P2
overview prose · S3-P3 point registry + binding map (granularity mints come back to the
orchestrator for adjudication). S3-P4 (the six S3 lints → LINT-18..25) waits for the S5 fix
lane to settle _common.py.

### WAVE 2 CLOSED ✅ (2026-07-04) — S3 restructure + S5 entry models

S3 executed in four phases, all committed + review-closed: P1 tree migration (aa9b6a6) · P2
20 overviews (lint-clean) + P3 registry (76 nodes, orchestrator-adjudicated APPROVED-draft) +
binding map (4 bound incl. the Belton→Gant worked binding + 10 pending mandatory rows)
(da0a0a3) · P4 lints 18–25 with 34 fixtures (9cf19ae) — live run: depth/points/binding/derip/
weights/urls/deck ALL ZERO on the migrated tree. Acceptance review (Codex, 19 criteria): 16
PASS; F-S3-01 fixed (Case Index generator re-pointed + regenerated, ac5c20e); F-S3-02
DEFER-TO-S7 (ER-split homes re-point rides the content extraction); F-S3-03 DISMISSED (R6
governs minting — reference pages carry no point of law). S5 tooling closed after a 12-finding
review loop (ledger: `_run/o2-execute/wave2-review-ledger.json`) — the headline: **LINT-26
caught the migration-moved GOOD_LAW_SLUG live, naming the fix** (the fail-closed design's
first real catch). Known-red rows all carry named owners (S7/S8/S9 per the ledger).

**Wave 3 (S6 → S7 → S8) opens when the S2 lake lands** (S6's candidate queue + verification
read from it; R15 build-QA gates the handoff). S2 session 1 still in flight at wave-2 close.

### S2 session-1 GATE: FAIL → the F-S2-15 cost-model adjudication (2026-07-04)

Session 1 (150 min, 1,525 calls): pipeline HEALTHY (clean boundary exit, 0 crashes, 9 transport
errors all auto-recovered, pacing min 4s, 0×429; 6 cases completed end-to-end, 9 lake records
committed e2634b4) — but the COST MODEL failed the gate: ~228 calls per completed case
(alphabetically-early mega-cases; full-text reads on every lane-1/3 treatment hit dominate),
projecting ~105k calls corpus-wide vs the signed 15–25k envelope (weeks, not the signed
multi-day run). **Orchestrator adjudication (F-S2-15), under S2 §9's execution-tunable lane
parameters ("revisit against real hit-rates during the run" — this is that revisit):
snippet-first triage for lanes 1/3** — full opinion reads only for genuine candidates (negative
keyword near the target case's name / binding-court ambiguity / no snippet), every triage
decision journaled per hit, lane 2 (top-25) keeps full reads, negative events remain
proposed-only behind S9's two-reviewer rule. Recall risk bounded + documented; S9's blind
re-derivation samples validate the triage. Builder implementing; then a validation session
(finish Terry + normal-case sample) re-gates before the cadence resumes.

### S2 CADENCE GATE: PASS (2026-07-04) — steady state entered

Validation session (60 min, 508 calls): triage read-rate 3.69% (73/1,979, every decision
journaled with reason), snippet classifications spot-verified sound, per-completed-case
44–55 calls (median 51), **whole-run projection ~22.9–23.5k — inside the signed 15–25k
envelope**. 10 substantive completions; zero-call resume-skips on all 6 prior completions
(idempotence live-proven again). Terry completes in roster order (cursor preserved — no
re-burn; the partial-resume mechanism was proven in re-smoke #3); Ashcraft supplied lane-cap
evidence. **Cadence resumed: 150-min sessions, relaunched per the recipe above after each
end-of-session checkpoint review; anomalies surface by exception.** At ~500 calls/hr the lake
lands in ~2–3 days of sessions. Wave 3 (S6 → S7 → S8) opens on lake completion + R15 build-QA.

### S2 session-3 gate: pipeline PASS, 5 fail-closed flags → F-S2-16/17/18 fix loop (2026-07-04)

Session 3 (150 min, 1,265 calls, 3,431 cumulative vs ~23k, 0×429, min 4s/median 6s, clean
boundary exit at California v. Greenwood): 34 new completions committed (b479fb8), roster now at
50 under_review / 496 pending. **But 5 rows landed fail-closed and all five are code-defect
false flags, adjudicated from record + journal + cached-response evidence + live CL-MCP
spot-checks:** (a) **F-S2-16** — the caption gate is exact slug equality vs CL canonical and
outranks the PASSED two-key: Bivens/Earls/Brower had citation+party-in-text confirmed on the
correct clusters and were still branded fabrication_suspected (CL canonicals are the long-form
captions). (b) **F-S2-17** — normalize_cite strips only bare "(YYYY)": every COA/state expected
citation shaped "283 F.3d 1040 (9th Cir. 2002)" silently fails the citation key (Benn; its
party key is genuinely false — "Lambert", the habeas warden, appears 0× in the opinion body —
so post-fix Benn correctly lands under_review/name+docket). (c) **F-S2-18** — one
case_name-filtered search then not_found: Birchfield's CL canonical is the mangled consolidated
caption "Birchfield v. N. Dakota. William Robert Bernard" (cluster 3216497); a q= or citation=
fallback finds it (verified live). Fix semantics + a --readjudicate mechanism for the 5 rows
specced in `_run/o2-execute/S2-FIX-16-18-WORKORDER.md`; Codex builder fix lane dispatched;
ledger rows appended. Session 4 relaunches after fix + read-only re-review, with the 5-row
re-adjudication as its pre-step.

*Harness note:* this session's permission mode denied `-c approval_policy=never` on codex
launches; lanes now run with codex exec's default fail-closed approvals (escalations auto-deny)
inside the same sandbox configs — functionally identical for our recipes, which never request
escalations.

### F-S2-16/17/18 fix loop CLOSED ✅ (2026-07-04) — CLEAR-TO-RELAUNCH

Three-loop writer≠checker cycle on scripts/s2/ingest.py (Codex builder wrote, 2nd Codex lane
read-only reviewed, orchestrator adjudicated): loop-1 implemented the work order (caption
containment + two-key precedence · normalize_cite year-parenthetical strip · zero-hit fallback
ladder · --readjudicate CLI); loop-2 review returned CLEAR-TO-RELAUNCH: no with three UPHELD
findings (R-01 unbounded rungs + premature ladder stop → cap 3 clusters/rung, viable-only
termination, best-so-far last resort; R-02 readjudication left stale identity payload →
empty-shell rebuild with roster-only preserves + field-level journaling; R-03 self-test gaps →
bounded-call/continuation/exhaustion/stale-cluster fixtures); loop-3 targeted re-verify: all
three FIXED with file:line evidence, no new drift, CLEAR-TO-RELAUNCH: yes. Orchestrator
independently ran the full self-test suite green (the read-only review lane cannot — temp
files). Ledger rows F-S2-16..18 closed. **Session 4 launch adds the five-row re-adjudication
pre-step:** `--readjudicate` × {Benn v. Lambert, Bivens v. Six Unknown Named Agents, Board of
Education v. Earls, Brower v. County of Inyo, Birchfield v. North Dakota}; expected outcomes:
Bivens/Earls/Brower → under_review (citation+party-text) · Benn → under_review (name+docket;
"Lambert" absent from opinion body is data-truth) · Birchfield → under_review via the fallback
ladder (cluster 3216497) with caption_mismatch_canonical warning.

### S2 session-4 gate: PASS — F-S2-16/17/18 live-validated; F-S2-19/20 micro-loop (2026-07-04)

Session 4 (150 min, 1,310 calls, 4,741 cumulative vs ~23k, 0×429, min 4s/median 5s): **all five
readjudicated rows landed exactly as predicted** — Bivens/Earls/Brower under_review via
citation+party-text on the correct clusters, Benn under_review name+docket (party-absence is
data-truth), Birchfield under_review via the fallback ladder to merits cluster 3216497. ~32 new
completions; lake at 87 under_review / 463 pending (48b601b). One new flag, adjudicated FP with
two NEW small gaps (the F-S2-16/17/18 machinery itself behaved correctly — ladder found the
right cluster, fail-closed held): **F-S2-19** caption containment lacks legal-abbreviation
normalization (CL's "Com. v. Herlth, J." vs "Commonwealth v. Herlth"; T6 class) and **F-S2-20**
cite equality is punctuation/case-sensitive ("2026 PA Super 114" vs CL "2026 Pa. Super. 114").
Fixed via deterministic contraction table + comparison-key wrapper (no stored-form leakage,
reviewer-verified); single-loop review CLEAR-TO-RELAUNCH: yes, no findings; orchestrator ran
the self-test suite green independently. Session 5 relaunches with
`--readjudicate "Commonwealth v. Herlth"` (expected: under_review, citation+party-text,
cluster 10870804).

### S2 session-5 gate: PASS clean (2026-07-05) — steady state holding

Session 5 (1,093 calls, 5,834 cumulative vs ~23k, 0×429, min 4s/median 6s): Herlth
readjudicated to under_review/citation+party-text/10870804 exactly as predicted (F-S2-19/20
live-validated); 33 new completions; lake 119 under_review / 431 pending; Florida v. Meyers
cursor-preserved at session limit. One not_found, **adjudicated TRUE**: Entick v. Carrington
(1765, Court of Common Pleas, 19 How. St. Tr. 1029) is an English case outside CL's corpus —
the fallback ladder exhausted honestly (q + citation rungs zero, journaled); R2(d)/R7 resting
state correct; S7/S8/S9 source Entick off-CL. No fix loop. Cadence continues; journal entries
stay compact while sessions gate clean.

The signed pool root `/Volumes/AIStore2` (S2 A10) does not exist; the AIStore2 APFS volume is
mounted at `/Users/Shared/AIStore/store2` but **TCC-blocked (EPERM) for every process in this
session chain** — orchestrator shell (sandboxed AND unsandboxed) and codex (workspace-write with
explicit writable_roots) alike. A TCC grant is GUI-only = user-only fix (same class as
interactive re-auth). Per S2 A10's env-overridable single path constant, the run proceeds with
**`CSSI_LAKE_ROOT=/Users/johngalt/cssi-lake`** (internal disk, 754 GiB free; dirs created:
cache/http, progeny, text, journal, logs, db). No verification guarantee is affected (storage
placement only; cache is regenerable/movable). **Remediation path:** grant Full Disk Access to
the session's responsible app (or fix the volume's TCC), then rsync `~/cssi-lake/` →
`/Users/Shared/AIStore/store2/cssi-lake/` and flip the constant. User notified.

### S2 sessions 6–8 + F-S2-21/22 loop (2026-07-05)

Sessions 6–7 gated clean (0 anomalies; 32 + 33 completions; journal-verified cumulative 7,970
at session-7 close — builder reports now cite the journal call-log count). Session 8 (+35, lake
219/330, 9,141 cumulative = 39.7%): one flag, **Lewis v. United States (1966)
fabrication_suspected = wrong-candidate rejection** (fail-closed held; nothing wrong ingested).
Adjudicated two defects: **F-S2-21** — the wiki year-disambiguator "(1966)" flowed raw into
search params (case_name zero-hits; fallback q returned Demko/Hoffa/Catto noise; 8-row class,
4 prior completions were q-rung luck: Henry/Chapman/Davis/Harris); **F-S2-22** — rung viability
accepted year+court alone, so same-year same-court Demko (385 U.S. 149) terminated the ladder
before the citation rung that finds Lewis precisely (385 U.S. 206, docket 36). Fixed
(strip-params-only + citation-gated viability when expected cite exists; no-cite rows keep
year+court per R2(b)); single-loop review CLEAR (298/309 added lines are fixtures, incl.
resume-stability for the 4 lucky-path rows); orchestrator self-test green. Session 9 relaunches
with `--readjudicate "Lewis v. United States (1966)"`; the 3 pending class rows (Mathis 1968,
US v. Harris 1971, US v. Smith 2024) now de-risked ahead of the M's.

### S2 sessions 9–10 + F-S2-23 loop (2026-07-05)

Session 9: clean gate — Lewis readjudicated under_review/citation+party-text/107312 (385 U.S.
206 confirmed; F-S2-21/22 live-validated; Mathis passed the fixed path silently); +39; lake
259/291; 10,376 cumulative (45%). Session 10: +41, lake 300/249, 11,588 (50.4%); one flag —
**Peters v. New York, adjudicated = the consolidated-companion class**: CL has no separate
Peters cluster (Peters is decided inside Sibron v. New York, 392 U.S. 40); the citation rung's
search results held the true Sibron cluster 107730 at rank 5 with the exact cite in the row's
own citation array, but the bounded fetch (top-3) never examined it; fail-closed refused the
wrong best-so-far (a Warner memorandum). **F-S2-23**: exact citation_compare_key prefilter on
search-row citation arrays before spending any fetch budget (primary + all rungs), prefiltered
rows first, no-match paths byte-identical; loop-2 (review R-01): prefilter-matched primary
capped at 3, baseline top-10 untouched (conservative scope, adjudicated); loop-3 re-verify
FIXED. Session 11 relaunches with `--readjudicate "Peters v. New York"` (expected: under_review
via two-key on Sibron 107730 + caption_mismatch_canonical — the honest companion-case resting
state for S6/S9).
