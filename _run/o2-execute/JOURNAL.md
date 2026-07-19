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

### S2 session 11 + F-S2-24 micro-loop (2026-07-05)

Session 11: Peters readjudicated under_review/citation+party-text/107730 (Sibron) +
caption_mismatch_canonical — F-S2-23 live-validated, consolidated-companion resting state
landed. +35 completions; lake 335/214; 12,557 cumulative (54.6%). One flag, adjudicated FP:
**Skinner v. Railway Labor Executives' Ass'n** — cite MATCHED and cluster 112219 correct, but
containment failed on apostrophe styling (ass'n vs CL "Assn.") and the party-text key used the
Bluebook abbreviation "ass'n", absent from opinion prose ("Association"). **F-S2-24**:
apostrophe-normalized caption tokens (ASCII+curly) + T6 association→assn + abbreviation-aware
party-term candidate set (last-word selection preserved). Single-loop review CLEAR, no
findings; orchestrator self-test green. Session 12 relaunches with
`--readjudicate "Skinner v. Railway Labor Executives' Ass'n"` (expected: under_review via
citation+party-text on 112219, no caption warning).

### S2 sessions 12–15 + the 2026-07-06 fix-window gate (F-S2-25/26/27)

Sessions 12–14 gated clean (commit-message checkpoints 12: Skinner readjudicated as predicted,
F-S2-24 live-validated, manifest fabrication_suspected=0 · 13: +37 incl. US v. Harris (1971)
silently · 14: +41 incl. US v. Smith (2024) silently — the F-S2-21/22 class fully retired;
Wilkes v. Wood not_found adjudicated TRUE, same off-CL class as Entick). Session 15 partial
(+7, frontier leg opened): CRASH — OSError 63 filename overflow building a frontier stub name
from a 300-char CL canonical caption (UNRESOLVED:arkansas-v-sanders × the 2024 Gov.-Sanders
prison-board case) → **F-S2-27** (input-caption-slug stub ids per the spec scheme + 100-char
filename cap + interrupted-row resume). alasaad-v-mayorkas not_found adjudicated TRUE — CL
files the litigation as Alasaad v. Wolf (4855246, already verified_identity via sibling row);
S6 caption-variant dedupe class.

**Side-session pickup (ORCHESTRATOR-NOTICE-2026-07-05):** absorbed A16 + RUNBOOK §5 standing
amendments (CodeRabbit spec gate · session_checkpoint.sh + pause push-notification protocol) +
draft PR #3. T–Z scan for the F-S2-25 party-key class: EMPTY — no readjudication batch.
Combined builder fix loop dispatched: **F-S2-25 + F-S2-26 + F-S2-27** (one loop, one review).
**R14 whitelist-extension decision SURFACED to the user per protocol** (terminal notification —
mobile push inactive — + served brief `2026-07-06-r14-whitelist-english-cases.html`): BAILII
hosts both English cases (Entick [1765] EWHC KB J98 — KB filing label vs historical C.P.
recorded as a cataloguing note; Wilkes [1763] EWHC CP J95); Founders' Constitution + English
Reports facsimiles are the second-source candidates; options 1/2/3 in the brief. Non-blocking:
cadence continues; Entick/Wilkes elevation waits on the answer + the F-S2-26 code landing.

### F-S2-25/26/27 combined loop CLOSED ✅ (2026-07-06) — CLEAR-TO-RELAUNCH

One builder loop, one review, one targeted re-verify (writer≠checker throughout): F-S2-25
(forward party-term candidates with the mandatory word-boundary bound — 1–2 char contractions
probed non-matching — + text-side apostrophe strip, straight+curly) · F-S2-26 (terminal-
not_found skip ends the Entick churn; warning dedupe; full A16 schema + --elevate-off-cl with
adjudication-file verification — reviewer confirmed BAILII is correctly REJECTED pending the
user's whitelist decision and the builder can never self-elevate) · F-S2-27 (input-caption stub
ids + 100-char filename cap; interrupted arkansas-v-sanders row re-runs on normal resume,
7-point confirmation reviewer-verified). Loop-2 fixed the single review finding (whitespace-
only official cite could pass elevation → strip-and-reject + schema pattern \\S); loop-3
FIXED with file:line evidence. Orchestrator ran the self-test suite green independently at
every loop. Session 16 relaunches into the frontier tail (89 pending).

### 🏁 S2 LAKE ROSTER COMPLETE (2026-07-06) — session 16, pending=0

Sixteen paced sessions, 15,959 cumulative CL calls (69% of the ~23k projection, inside the
signed 15–25k envelope), zero 429s across the entire run, pacing ≤14/min held throughout.
Final distribution: **456 under_review** (page rows) · **65 verified_identity** (frontier
shells) · **25 fabrication_suspected** (frontier flags = the designed S6 adjudication queue
per SD10, each with cross-check trail) · **5 not_found** (Entick + Wilkes = adjudicated-TRUE
off-CL class awaiting the R14 whitelist answer; alasaad-v-mayorkas = adjudicated caption
variant of verified alasaad-v-wolf; beautiful-struggle-v-baltimore-police-dep-t +
morgan-v-fairfield-county = frontier seeds for S6 cross-check). Session 16 live-validated
F-S2-27 (arkansas-v-sanders--10601315 bounded stub, fabrication_suspected as predicted) and
F-S2-26 defect 1 (Entick skipped=true/terminal_not_found=true, zero rewrites). Run-defect
ledger for the paced run: F-S2-16..27, all closed writer≠checker, every fix live-validated
on readjudication; fail-closed held every time — zero wrong ingestions.

**S2 the SPEC is not yet closed:** remaining Method deliverables — projector
(scripts/s2/project.py + canonical serializer), drift lints LINT-12/13/14 (incl. A16 checks),
R15 structural gates + verified-flips, the S6 handoff assembly — then the spec-completion
CodeRabbit gate (coderabbit_gate.sh S2) before verified-flips per the RUNBOOK §5 amendment.
Entick/Wilkes elevation rides the user's whitelist decision (brief served 2026-07-06).

### S2 close, part 1 (2026-07-06): Method 4/5/6 built + R15 treatment audit + four fix cycles

**Method 4/5/6 landed** (Codex builder, spec-as-work-order): authority.sqlite (551 cases /
4,093 citations / 14,326 edges / 6,089 intra_edges; A5 columns, A7 stamps, two-rebuild
determinism); project.py + ONE shared canonical serializer (managed-key splice — preserved
frontmatter BYTE-identical; A13 gate PASS: 456 legacy pages fully mapped, 0 REVIEW;
--verify-idempotent live proof: run-2 zero diffs on a temp tree; the REAL first projection
write stays HELD until treatment data settles); LINT-12/13/14 CI-fail-closed (LINT-13 =
live schema interpreter, fail-closed on unknown keywords — proven when it refused the
orchestrator's own oneOf edit). Review loop: 8 findings all UPHELD → fixed → re-verified.

**R15 Claude-lane treatment audit** (Opus-xhigh, read-only; R15-TREATMENT-AUDIT.md): safety
core HELD — 14,326/14,326 edges proposed-only, zero auto-applied negatives. 4 flags →
**F-S2-28** (lane3_recency inert corpus-wide: q-string injected a nonexistent filed_after:
field — 455 zero-result searches; + 3 lane2 terminal-boundary cursor losses) and **F-S2-29**
(pre-seed override corruption + name-only controlling refs). Both fixed through multi-loop
writer≠checker cycles with every repair value traced to a signed source (binding yaml,
migration table, the lake itself); Chatrie page/stub collision → page-row-over-stub rule +
s6-dedupe-pointer. **F-S2-30** (orchestrator schema adjudication, reviewer-checked): the new
LINT-13 exposed citing_case.cite parallel-cite ARRAYS vs the scaffold's string|null — schema
widened via citing_case_ref for edges only; 13,137 findings collapsed to the 8 known
Belton/Smith rows (which the repair zeroes, acceptance-fixtured against the real validator).

Lint truth-state at this gate: LINT-12 = 458 (expected: projection held) · LINT-13 = 8 (the
repair's target) · LINT-14 = 2 (Entick/Wilkes, user decision pending). Next: the rerun/repair
network session (lane3 corpus rerun + lane2 ×3 + --repair-migration-refs), then first
projection, 1-in-10 spot-check, structural gates, CodeRabbit gate, verified-flips, S6 handoff.

### 🏁 S2 SPEC CLOSED (2026-07-06) — the flip executed; Wave 3 opens

The full close sequence, all writer≠checker: rerun/repair session (migration refs ×19 →
LINT-13=0; lane2 ×3 cursors restored; **lane3 corpus rerun 456/456 in one session — 19,197
hits triaged, 248 proposed negative events where the broken lane had structural zero**, staged
proposed-only for S9's two-reviewer rule) → **THE FIRST PROJECTION** (458 pages, legacy →
3-field vocabulary + dual dates; LINT-12 458→0; idempotence proven live) → **spot-check** (2nd
Codex lane, 68 records live incl. all 15 readjudicated rows: 0 errors) → **CodeRabbit spec
gate** (27 findings: the critical CONFIRMED LIVE — migration seeding wrote field_i_validity
onto fail-closed records, bounded to Entick/Wilkes, repaired to unverified + re-projected
(F-S2-31); 6 S2 majors fixed fail-closed; RETRO re-detections deduped; lint/quartz items
routed: RETRO A 24 fixed/1 refuted-with-proof + B/C 10 fixed, all lanes tsc/build/self-test
clean) → **THE FLIP: 421/421 verified**, exact record-id match, untouched classes held
(35 under_review → S9 · 65+25 frontier → S6 · 5 not_found), 421 r15-flip journal events with
the full gate list.

**S2 §7 acceptance:** schema 100% (LINT-13=0) ✓ · two-key 100% on verified (flip construction)
✓ · A1 replacement gate ✓ · dual dates + provenance ✓ · drift + page↔record lints green EXCEPT
the one NAMED pair (Entick/Wilkes = LINT-14's 2 + LINT-6's 2 — rides the user's R14 whitelist
decision, elevation path built and gated on an orchestrator adjudication file) · spot-check
logged ✓ · treatment audit recorded (4 flags, all closed) ✓. **Total run: 17,169 CL calls =
74.7% of the ~23k projection, 0×429 across 16 paced sessions + reruns.** S6 handoff:
`_run/o2-execute/S6-HANDOFF.md` (25 flags + 65 shells + dedupe pairs + the S9 residuals note).
Defect ledger F-S2-16..31: every finding adjudicated, fixed, and live-validated; fail-closed
held every single time — zero wrong ingestions across the entire build.

## Wave 3 — S6 coverage/ingest (OPENED 2026-07-06)

**Step 1 + PACKET A (pause #2 — SURFACED, awaiting dispositions):** roster regenerated +
reconciled (94 rows, drift fully attributed; LLC v. John Doe = documented §c exclusion). R4
dual-model two-key re-verification (blind Codex web leg ∥ Claude Opus leg, zero CL): **27/29
fabrication suspects REAL-with-keys** — incl. all 4 O1-era SEED §a suspects REFUTED
(Mayville/Small/Lyle real, holdings match; Moore-Bush scar absent from current text) — 2
genuinely unverifiable (US v. West, US v. White: stolen-vehicle standing propositions) →
recommend REMOVE+re-anchor. Divergences adjudicated: arkansas-v-sanders stub matched the
WRONG case (2024 Gov.-Sanders; real = 442 U.S. 753 → re-key), Morse→French + Carroll/Carman +
Chatrie-stub = alias-folds. Packet: `_run/s6-fabrications.md` + served brief + notification.

**Step 2 (COMPLETE): GAP + term sweep.** GAP queue (7 new AUTHOR + Egbert-stub-exists +
Martin-rides-packet-A + Noem WATCH + Villarreal REJECT). Term sweep OT2019→present: blind
dual-model enumeration (Codex 63 ∥ Claude 48), 25 Codex singletons existence-verified — **0
fabrications in either leg** (frame divergence only); 3 docket corrections + 1 caption fix;
Wikipedia OT2025 flagged as hallucination-polluted (avoided). Reconciled universe: 73 rows.
**R2 gate** (Opus writer, 84 rows): 61 INGEST (48 page-candidates / 13 in-scope-non-page
incl. 9 noted-orders + Noem watch + 2 same-litigation folds) · 19 EXCLUDE · 4 BORDERLINE.
**Codex re-check** (19 sampled incl. all borderlines + 5 suspect picks): 4 DISAGREEMENTS
auto-promoted to packet B (Reed v. Goertz, Williams v. Reed → borderline; Price v. Montgomery
→ exclude-craft dispute; **Villarreal GAP-04f caption/rationale mismatch — the queued caption
is the in-scope Lagordiloca case while the reject rationale describes Villarreal v. Texas —
user resolution rides packet B**). Folds + no-Confrontation-line corpus check verified.
Packet-B accumulator: 4 writer-borderlines + 4 re-check promotions + R3's pre-registered
members. R7 queue batch 1: 30 rows (2 pulled pending packet B), every row docket/cite-keyed;
intake mechanism (--add-candidates, dedupe + journaled provenance) with the builder.

**ALL THREE DECISION SURFACES RETURNED (2026-07-06, new orchestrator session @ d134883):**
R14 = Option 1 → IMPLEMENTED same session (A17 amendment; BAILII/Founders'/Eng.-Rep.-facsimile
whitelist in code + schema (pairwise 10→28); Entick+Wilkes elevated verified_off_cl via
adjudication files, all 4 sources live-confirmed, BAILII via archive snapshots; Field-I
re-seeded good_law/migration-seed (F-S2-31 revert cured by elevation); re-projected;
LINT-6/12/13/14 ALL GREEN — S2 §7's named exception pair closed; +2 F-S2-33 orphan shells
removed+journaled; commit 80d11a8). Packet A = ALL FOUR GROUPS APPROVED → 23-row re-key +
alias-fold builder session dispatched (PACKET-A-REKEY-WORKORDER.md; lane note: Opus-xhigh
substitute builder — permission classifier declined the headless-Codex full-auto pattern;
same writer≠checker discipline). Group-3 removals EXECUTED (R4): West/White — Case Index
rows updated w/ Byrd re-anchor pointers, omissions tombstones, s6-removals.jsonl terminal
rows; lake stubs stay fabrication_suspected (CL-honest), no silent deletion.

**PACKET B = USER-DELEGATED 3-AGENT PANEL (user protocol, verbatim: blind Fable reviewer ∥
blind Codex reviewer → Fable adjudicator → implement).** Recommendation-stripped ITEMS.md;
both lanes zero-CL, mutually blind; adjudicator alone read this packet's recs. Outcomes
(packetb-dispositions.jsonl + panel ADJUDICATION.md): items 1-4 EXCLUDE-remit (unanimous);
5-6 EXCLUDE (both lanes; orchestrator's bullet recs DECLINED — INGEST needs a prong); 7
INGEST noted-order mention prong (c) (resolved against Codex); 8-10 INGEST-author (Wyman /
G.M. Leasing / Verdugo, re-key-gated); 11 EXCLUDE remedies-remit; 12 referent = Villarreal
v. Texas 24-557 (GAP-04f caption mislabel; D6→D7 attribution fix; PREMISE CORRECTION:
Alaniz IS the Laredo litigation — one ledger identity, alias folded into gated.jsonl:72,
en-banc merits = Lower-court-dev bullet, NO page); 13 OWN PAGE after re-key (record
10614578 mis-keyed to First Step Act decision; correct = 926 F.3d 313 / CL 4628336 —
CARPENTER-REKEY-WORKORDER.md queued behind packet-A session); 14 Bennis PAGE (orchestrator
bullets-rec OVERRULED) + Calero-Toledo bullet (against Codex); 15 all three Bivens PAGES
(Hernandez premise corrected: NOT in prose — R5.iv sweep leg basis); 16 Heller v. New York
PAGE (all-bullets rec OVERRULED) + 3 bullets (against Codex on P.J. Video/Fort Wayne).
Premise-correction ledger: 8 items incl. Hencely 2026-04-22 + Price cert-denial 2024-07-02
date fixes, stale statuses, stale path. Net +9 packet-B pages; within §9 scope guard.
Dispositions folded: s6-borderline.md + s6-fabrications.md + gap-docket.jsonl:12 +
gated.jsonl:72 + DISPOSITIONS-2026-07-06.md. R8 authoring waves unblock when the re-key
session lands (packet-A rows + Carpenter); R11 ledger emits at wave close.

**DISPOSITION PHASE CLOSED (2026-07-06/07):** packet-A re-keys EXECUTED (21 rows: 20 clean +
Robinson orchestrator-ratified on docket exact-match; arkansas-v-sanders wrong-case reset →
442 U.S. 753/110119; 52 calls, 0×429) + 3 alias-folds (new ratified `folded-alias` terminal,
spec A18) + Carpenter-remand re-key (10614578 → united-states-v-carpenter--4628336,
verified_identity, 926 F.3d 313, 2 calls; narrow opt-in --web-keys-allow-verified-identity
gate-reviewed) + West/White removals + R14 elevation. Manifest 662: 421 verified / 195
verified_identity / 35 under_review / 4 not_found / 3 folded-alias / 2 verified_off_cl / 2
fabrication_suspected (= the removed pair, ledger-terminal `removed`). Cumulative ~17,495
calls ≈ 76.1% envelope, zero 429s run-wide. ALL page-authoring preconditions satisfied →
next: R8 worklist assembly (homes+roles per candidate from gated.jsonl + panel implementation
notes + S3 tree), orchestrator gate, then the authoring waves (~95–130 pages incl. the 9
packet-B pages), R11 ledger at wave close, S7 opens.

**R8 WORKLIST SIGNED (2026-07-07):** assembler (Opus-xhigh) delivered R8-WORKLIST.json +
R8-NONPAGE-LEDGER.json with a partition proof (195 vi stubs = 147 pages + 4 escalations + 44
non-page, exact; removed/folded rows verified absent; Chapman double-count bug caught by the
partition check and fixed pre-delivery). Orchestrator gate: 4 escalations adjudicated —
Gaetjens = PAGE (prong a, D1 flip; quoted+weight-labeled reliance in Three Golden Rules; home
Emergency Aid) · Serge = excluded-remit (citation-format specimen on the S8 page) · DC v.
Heller = excluded-remit (2A; the corpus's own 'not Fourth Amendment authority' annotation is
the permanent treatment; caption trap vs Heller-NY logged) · Cruz = watch-S7-deferred
(bare-caption trap; R10/R4 discipline — identity ≠ proposition linkage). **Final: 148 pages**
(over the ~95–130 planning estimate, under the §9 guard of 150 — driver: frontier floor 41 +
D1-flip roster 67; surfaced per §9, no trim). By basis: 67 D1-flip · 37 frontier-controlling ·
18 sweep · 9 GAP · 7 packet-B (+2 overlap-based) · 5 history-D2 · 4 frontier-split. Non-page:
58 placements + 3 escalation terminals. NEXT SESSION: R8 pipeline BUILD (no promotion CLI
exists yet — stub→record promotion + born-conformant mint + Case-Index/homes/ledger rows, S5
R3 skeleton, specimen = U.S. v. Smith (2024)) via builder work order + review loop, then
authoring waves per R10 step 5 (GAP/sweep first, then roster, then frontier), serial lane,
~15–25/batch, R11 ledger at close.

**R8 PIPELINE BUILD (2026-07-07, orchestrator session post-d28e200):** builder work order
(`R8-PIPELINE-WORKORDER.md`) → Opus-xhigh builder delivered `scripts/s6/mint_page.py` + 16
fixtures: dry-run default, guarded --write, atomic staging w/ LINT-15/16/14 validation +
reverse-order rollback, A6 stub→record promotion, authored-ledger JSONL, idempotent no-op,
14 machine-readable refusal codes; self-test 19/19 PASS, Smith-specimen conformance PASS
(projector deep-equals modulo lake.status). 4 escalations adjudicated
(`R8-PIPELINE-ADJUDICATION.md`): E1 born-status `under_review` RATIFIED (schema-real; R8's
"draft" = R15 banner family; §8 names under_review) · E2/E3 NO corpus-wide convert-first
(preserves S5 §5.2 "S7 converts per-page") — Case-Index insertion REMOVED from the CLI
(single-writer = build_case_index.py, regenerated per wave batch; mint already merges payload
`holding:` + projects `homes`) and homes-page Key/Related rows LEDGER-DEFERRED to S7
(materialized from s6-authored-ledger.jsonl at per-page conversion; R8 atomic contract
transitionally amended; pre-publish window, no reader exposure; R11 close gains owed-homes
accounting; S7 handoff item) · E4 80/148 stubs identity-only (SD10, no citations block) →
bounded `--enrich-citations` ingest.py surface + paced run over exactly those rows
(~80–160 cluster fetches, cache-likely; `S2-ENRICH-CITATIONS-WORKORDER.md`). Deferred+journaled:
off_cl_links drop under born-status override (no off-CL row in the 148); R6 schema-3 index flip
(S7/S8, generator-owned). Wave plan staged: `R8-WAVE-PLAN.json` — 8 batches in R10 order
(W1 GAP+sweep 18 · W2 sweep+packet-B 16 · W3 history+roster 19 · W4–6 roster 18/18/18 ·
W7 frontier 21 · W8 frontier 20; Σ=148 exact, dedup-checked; each batch closes w/ index regen).
In flight: s6 builder loop-2 (surface removals) ∥ S2 citations builder (offline build, then the
serial-lane run). Next gate: reviewer lane over both diffs → orchestrator commit → CodeRabbit
spec-gate over scripts/s6 + scripts/s2 delta (standing amendment, PR #3 vehicle) →
session_checkpoint.sh → wave W1.

**R8 PIPELINE GATE CLOSED (2026-07-07, same session):** find→adjudicate→fix ran the full loop —
reviewer (fresh Opus-xhigh, read-only, 8 scar-class dimensions) returned 12 findings (2 HIGH:
unwired stub gate = same-stem write-then-delete lake destruction path; non-crash-atomic commit =
wedge/silent-ledger-drop windows), ALL UPHELD (F-R8-04 half-refuted: `renames` IS the manifest
schema's designated slot; stale-fields residue upheld; manifest ruled AUTHORITATIVE live state) →
builder loop-3 fixed all 12 (lake-derived completion classification w/ crash-tail roll-forward
journaled as `reconciled`, wedged-partial fail-loud, stub gate + old==new guard, fail-closed
manifest/desync/global-uniqueness checks, commit-time failure-injection test; self-tests 21→36/36)
→ reviewer VERIFY pass: 12/12 genuinely FIXED (ran tests itself), 1 new LOW F-R8-13 (reconcile
path trusts on-disk page w/o re-lint + orphaned partial ledger line appended-after not truncated;
both fail-safe/loud) — orchestrator disposition: ACCEPTED-DEFERRED, folds into the next s6 touch.
CLEAR-TO-COMMIT: YES. Also this gate: F-R8-11 root-caused to the orchestrator's own Gaetjens
worklist row (content/-prefixed home + bare-caption role) — normalized + noted in-row; all 148
rows now pass homes-existence + homes/roles-bijection. ∥ S2 ENRICH-CITATIONS lane landed: 80-row
scope, 32 enriched (100% cache-hit, 0 live CL calls, 0×429), 28 citations-empty (CL data gap,
honest), 13 no-display, 7 cite-mismatch — the new mis-key guard (roster expected_citation must
appear in cluster) caught 7 wrong-cluster cites pre-ship (orders/cert/companion clusters incl.
Bennis 517 U.S. 1163≠516 U.S. 442, Quantity 1967 proceeding≠1964 landmark); court-class ladder +
guard both RATIFIED (`R8-CITATIONS-ADJUDICATION.md`). 48 mint-blocked rows partitioned into
recovery lanes R1 (≤14 identity re-keys, packet-A machinery) · R2 (6 rows, AUTHORIZED narrow
noise-reporter exclusion in signed serializer, F-S2-15 precedent) · R3 (28 rows, AUTHORIZED
dual-leg web-cite recovery w/ distinct provenance source + schema/LINT-13 extension; slip-only →
A3 precedent) — work order `R8-CITE-RECOVERY-WORKORDER.md`. Wave gating: W1 17/18 mintable,
launches at gate close; blocked rows skip w/ journaled `deferred-recovery`, tail-batch W9.
Committing: scripts/s6 (mint CLI, 36/36 + specimen) + scripts/s2 --enrich-citations + 32 lake
records + manifest + worklist fix + adjudications/work-orders/reports/review-ledger + wave plan.
Next: scoped CodeRabbit gate (this commit's scripts delta) → session checkpoint → recovery lane
∥ wave W1.

**WAVE W1 CLOSED + RECOVERY LANE LANDED (2026-07-07):** W1 (GAP + sweep first half): **15 pages
minted** through the R8 pipeline (Chiaverini · Culley · Gonzalez-v-Trevino · Nieves · Thompson-v-
Clark · Cooley · Lombardo · Martin · Brownback · Dupree · Fazaga(2 homes) · Fikre · Goldey ·
Hernandez-v-Mesa · Lackey), all born under_review/⚪, exact BIRAC skeleton, verbatim pinned
holdings, R12 sources w/ corroboration trails (Nieves spot-checked instructor-grade: ^pin-406 +
star-pagination corroborated via Gonzalez 602 U.S. 653); 3 honest skips (R.W. deferred-recovery ·
Egbert data-escalation, repaired mid-batch by recovery lane via new --repair-identity-from-cache,
false-Historical→Binding-SCOTUS · Gutierrez cl-text-unavailable, no-fabrication). ~45 CL calls,
0×429, 3 transient 502s backed off clean. Build 586 files OK; Case Index regenerated; manifest
bijection EXACT under concurrent lanes (662=662, 15 renames, 195-15=180 vi / 35+15=50 ur). W1
agent self-fixed 2 self-introduced lint regressions (LINT-9 pin placement ×3, LINT-2 incidental
quotes ×6). ∥ RECOVERY lane (zero live CL, zero network): R1 13 re-keys dual-leg web-verified
READY-PENDING-LANE-GRANT (carroll reclassified → R3: right per-curiam cluster, CL just lacks the
U.S. cite); R2 DONE — serializer noise-list landed (Fla. L. Weekly Fed. S/FED App.), 6/6 enriched
cache-served; R3 10 web-dual-leg cites landed (LINT-13-conformant provenance) + 15 slip-only
journaled + 4 escalated (young/williams/lewis/black; black+lewis = suspected upstream mis-keys →
R1 candidates); CR-03/CR-15 fixed. **Two mint↔lint systemic gaps found+fixed same session (the
F-S2-21 class again):** LINT-13 rejected the mint's provenance.s6_promotion marker (schema
amendment, 15→0, pass/fail fixtures) and LINT-6 demanded literal draft:true where R15's banner
drivers are lake.status∈{draft,under_review}∨Field-I-unverified (lint amended w/ _banner_driven +
first-ever LINT-6 self-test, 15→0 HIGH, 0 other deltas; draft:true would have HIDDEN pages from
the build — wrong tool). Systemic follow-ups queued for the consolidated CL session: bulk
court_level re-derive (~30 SCOTUS-residue rows share Egbert's corruption) · R1 readjudication ·
black/lewis investigation · CR-13/14 project.py (deferred on a work-order scope contradiction the
builder correctly caught — scripts/s2 was locked) · Gutierrez text-availability check. Process
notes (honest): CR-03/15 addendum was briefly MISROUTED to the W1 agent (orchestrator dispatch
error; W1 refused correctly on file-boundary + collision grounds — the writer≠checker boundary
held); commit 70996d8's `git add scripts/lint` swept 3 in-flight recovery-lane LINT-13 web-cite
fixtures mid-work (benign, reconciled this commit). Known-endemic corpus reds unchanged (LINT-10
×48 / LINT-5 ×46, specimen-triggered, S8/S9 remit). Mintable arithmetic: 148 = 15 minted + 3 W1
skips + 16 recovery-unblocked + 13 R1-pending + 15 slip-only + 4 R3-escalated + rest already
mintable; W9 tail sweeps stragglers.

**W2 CLOSED + CONSOLIDATED REPAIR + SLIP-ONLY SUPPORT (2026-07-07):** W2: **11 minted** (4 sweep
§1983/QI: Nance·Perttu·Tanzin·Uzuegbunam + all 7 packet-B: Bennis(+Calero note)·G.M.Leasing·
Heller-NY(caption-trap vs DC-v-Heller)·Carpenter-remand-926-F.3d-313(caption-trap vs SCOTUS
Carpenter — spot-checked exemplary, ^pin-313)·Verdugo(corrected 494 U.S. 259)·Wyman·Ziglar), each
identity re-verified vs cluster pre-authoring; 5 journaled skips (4 slip-only deferred-recovery +
zorn data-escalation); ~35 MCP calls 0×429; mint-gate lints 0 findings; body-only prose
finalization (LINT-9 ×6/LINT-2 ×3/dead-wikilinks ×4 on own fresh pages) RATIFIED (W1 class; S9
certifies); corpus HIGH 4742→4731; build 597/2144 OK; Case Index 495 rows. ∥ CONSOLIDATED REPAIR
(35 CL calls REST-token — MCP lane unauthorized in that env, honest lane note): R1 13/13 re-keyed
verified_identity (scoped --smoke per row; unscoped --readjudicate-file now UNSAFE post-W1 —
would re-fetch minted pages, documented); 64 SCOTUS false-Historical repaired (0 remain); R3-esc
4/4 = one frontier mis-key CLASS (roster year unset → search grabbed 2025 same-surname cases) —
black/young/williams/lewis re-keyed dual-leg; CR-13/14 landed (project.py fail-closed dates +
pre-validate, 9/9 + idempotent + mint 37/37); Gutierrez text FOUND (plain_text 117KB — MCP
read_document is html_with_citations-BLIND; wave order amended w/ the fallback + stop-if-
unauthorized rule); zorn(corrupt Strike-3 cluster)+chapman(cert-orders mis-key, EXCLUDE-remit
anyway) left honest. ORCHESTRATOR: 17-row re-key remap applied to signed worklist+wave-plan
(journaled in-row); slip-only mint support RATIFIED both flags (Bluebook slip header `No. <dkt>,
slip op. (<court> <yr>)` behind explicit citations.slip_only marker — S9 to sample; stamper in
scripts/s6 since scripts/s2 wasn't free — builder's gate check caught my stale premise);
**stamp run EXECUTED at this gate: 15/15 stamped, 0 refused** (zorn stamped but still refuses
mint on identity-incomplete + corrupt-cluster escalation — belt+braces held). Mint self-tests
41/41. **Next repair queue (pre-W3, blocking 8/19 W3 rows):** 41 coa + 17 state court_level=
"other" residue (extend --repair-identity-from-cache w/ court→circuit/state derivation) + 9
slip-identity completions + zorn off-CL identity decision. Scoreboard: 26/148 minted, mintable
122+6-slip=near-full, envelope ~76.3%, 0×429 run-wide.

**COA/STATE IDENTITY REPAIR (2026-07-07):** `--repair-coa-state-from-cache` landed —
docket-court_id-authoritative derivation (court is NOT on cached clusters; docket structural for
ca1-11/cadc/cafc, court-object jurisdiction for state/district; D.C. trap resolved: court_id
"dc"→state), fail-closed on class/state swaps + military/unclassifiable + uncorroborated circuit
swaps. Run: 44/52 repaired (37 coa + 7 state; residue 65→21: 8 escalated-vi surfaced + 2 excluded
zorn/chapman + 11 off-scope non-vi); manifest coa 66→103 state 9→16; 0 projection errors, pages
473→484. W3-8: 7/8 CLEAN; people-v-frederick ESCALATED (roster-state-swap: cluster 10579458 = NY
namesake, corpus intends the Michigan knock-and-talk case — wrong-case re-key queued, W3 skips).
Slip: 12/15 mintable (6 newly completed incl. davis via ratified docket-match; wilson analogue
REFUTED + escalated — the discipline works both directions). NEW MIS-KEY CLASS: military
namesakes (cole/lyle/small/mendoza → armfor/nmcca clusters; why CL held no cite; correct targets
already web-recovered in R8-R3-web-cites.jsonl). Pre-existing bug noted: long-lake stub
circuit="ca2021" (parse_circuit-year artifact in s6_candidate_court_fields). 59 network calls,
0×429, 76% cache. Next repair batch queue: frederick re-key · military-namesake re-keys
(cole/lyle/small/mendoza) · ruiz CAAF off-model decision · wilson · 8 escalated-vi · long-lake
bug. W3 dispatching: 18 expected mints + frederick skip.

**W3 CLOSED (2026-07-07):** **17 minted** — 5 history D2 renders (Sanders·Frank·Quantity·Robbins·
Trupiano: Historical weight, precise overruling verb, wikilinked successor, ⚪ banner) + 12 roster
D1-flips (Alasaad·Alvarez·Carroll-v-Carman·Carter·Gaetjens·Jimerson·Johnson-v-Glick·Knight·
LaDuke·Milam·Christensen·Demesme); ~51 MCP calls 0×429 (2 upstream blips yielded+backed off);
mint-gate lints 0/0/0; Case Index 512 (+17 exact); build 614/2192 green. 2 data-escalation skips:
frederick (known NY namesake) + **robinson-v-commonwealth DISCOVERED wrong-case on read**
(cluster 10793178 = Mass. SJC Commonwealth-v-Daryen-T.-Robinson traffic-stop case, NOT the Va.
Flock-ALPR case; packet-A's docket-exact-match ratification was WRONG — record's own alternate
cluster 10838748 queued as likely-correct; honest correction, journaled). Body-only prose fixes
×3 RATIFIED (standing class). History Field-I unverified→superseded DEFERRED to S9 (treatment
promotion is S9 remit; pages already render Historical + verb). CARTER LINT-12 ESCALATION
adjudicated → s6 fix: slip-cite drift (mint writes slip cite to page frontmatter; project_record
returns '' for the promoted record) — fix = projector derives the SAME slip form from the
citations.slip_only marker via derive_slip_cite as single source; never write the slip form into
citations.display (would masquerade as a reporter cite). Repair queue (post-W4): frederick→
Michigan re-key · robinson→10838748 · military namesakes cole/lyle/small/mendoza · ruiz CAAF
investigation (R3 data) · wilson · 8 escalated-vi · long-lake ca2021 bug. W4 dispatching w/ cole
known-skip; W5 blockers lewis+lyle; W6 blockers mendoza/ruiz/small/wilson — all queued-class.
Scoreboard: 43/148 minted.

**W4 CLOSED + CARTER SLIP-FIX (2026-07-07):** W4: **11 minted** (Karston·Weaver·Wint·Aigbekaen·
Amos·Berkowitz·Black·Brinkley·Camou·Carlton-Williams·Daniels; ~55 calls 0×429; mint-gate 0/0/0;
Case Index 523 +11; build 625/2215; endemic-only lint delta, zero new signatures; ratified
body-only finalization ×4 incl. Berkowitz pincite upgraded star-verified). 7 skips: cole
(known military-namesake) + larson (deferred-recovery, a/k/a caption flag) + **5 wrong-case
clusters DISCOVERED on read: burgess/capers/castillo/chavez/crumble** — a residual mis-key class
(ambiguous US-v-surname rows resolved to modern criminal appeals; invisible to prior repairs
because they carry citations) — each confirmed by zero-hit doctrine-term searches, recommended
re-keys in W4 report. ∥ Carter LINT-12 slip-drift FIXED (derive_slip_cite moved to project.py as
single source; marker-derived, never enters citations.display; LINT-12 1→0 corpus-wide, zero
content diffs — the page was already right; projector/idempotent/mint 41/41/specimen/stamp 7/7
green). ORCHESTRATOR DECISION: re-key queue now ~15 (frederick·robinson→10838748·cole·lyle·
small·mendoza·ruiz·wilson·larson·lewis-nocite + burgess·capers·castillo·chavez·crumble) and the
class predicts more in W5/W6 → ONE comprehensive identity-audit + re-key session dispatched
BEFORE W5: (a) proactive audit of ALL 36 remaining unminted W5/W6/W7/W8 rows (cached cluster
reads + doctrine-term cross-check vs worklist note/homes — catch the class wholesale), (b)
dual-leg web re-keys for everything queued+found, (c) scoped readjudication. W5 waits on its
report. Scoreboard: 54/148 minted.

**PRE-W5 AUDIT + RE-KEYS LANDED (2026-07-07):** wholesale identity audit of 86 rows (77 pending
W5-W8 + 9 skip-queue): **63 CLEAN · 20 MIS-KEY · 2 cite-dup-swap · 1 escalate · 0 unsure**;
W7/W8 all-clean. **HEADLINE: the COA-STATE session's cite-corroboration was CIRCULAR** (roster
expected_citation derived from the mis-keyed cluster → self-corroborating wrong same-surname
cases) — masked 5 (loera/porter/trent/ruckman/davis); + new finds lee (274 U.S. 559; "Lee" was a
middle name), ruiz (536 U.S. 622 SCOTUS, not CAAF), larson (Or. 1999, not the Iowa a/k/a).
**22/22 re-keys landed** verified_identity/canonical (targets from the wiki's own opinion links +
direct CL verify; trent hand-reconstructed docket-collision → S9-reverify flag; robinson
slug-rename retry landed right cluster), bijection 662=662, 0×429 (57 REST + ~28 MCP).
ORCHESTRATOR: remap-2 (22 rows) applied to signed worklist + wave plan (journaled in-row);
ganias spurious Border-Searches home REMOVED per audit (2d Cir. data-retention case, no border
nexus; Plain View stands); holcomb ESCALATED (cites WITHDRAWN opinion 132 F.4th 1118 → W5 skip +
investigation queued); cache-only enrichment probe on the 4 nocite rows → 3 genuine CL cite gaps
(lewis/mendoza|porter/trent-class → slip/web-cite tail handling), 1 cache-miss resumable.
wiki_pageless flag (14 rows) reviewed: expected pre-authoring state, signed verdicts stand.
Queued micro-items: reddick ca5→ca3 label · larson same_rank_tie tiebreak · long-lake
parse_circuit bare-year bug (ingest.py:549) · holcomb superseding-opinion check. Readiness:
W5 16/18 (skips holcomb+lewis) · W6 15/18 · W7/W8 41/41. Scoreboard 54/148; W5 dispatching.

**W5 CLOSED (2026-07-07) — incl. mid-batch CL MCP OUTAGE handled by the book:** lane died after
the metadata pass (~21 calls in), tools never re-registered across ~8min retries → agent yielded
with a DEFINITIVE handoff (0 pages authored w/o pincites, wave-plan honestly left pending, cached
opinion→cluster map preserved) — orchestrator probed lane healthy + RESUMED SAME AGENT (L4
discipline; no relaunch, no duplicate lane). Outage productive: davis--4881258 diagnosed as
DUPLICATE of the already-authored Howard-Davis page (same cluster 4881258/997 F.3d 191; the mint
collision-checks by stem not cluster — would have double-paged) → orchestrator FOLD applied
(worklist terminal folded-duplicate, W5 row removed; lake fold + cluster-collision mint guard
queued); hunt RECLASSIFIED mintable (explicit slip_only marker, A3 path). Resume → **15 minted**
(Ganias·Hanapel·Hay·Hunt-slip·Kolsuz·Lee·Liddell·Loera·Loines·Lyle·Maez·Massenburg·May-Shaw·
Mayville·Mendez; star-pins where CL paginates, A3 slip pins elsewhere; Kolsuz spot-checked —
honest reporter+slip-pin hybrid; Loines lake docket mismatch caught+corrected on read 21-1516→
22-3073); 2 known skips (holcomb withdrawn-opinion, lewis cite-gap); ~61 calls 0×429; LINT-2 ×21
first-pass remediated body-only → 0; mint gate 0/0/0 ×15; Case Index 538 (+15); build 640 green;
zero new-signature lint. Scoreboard: **69/148 minted.** W6 dispatching (15/18 known-ready) ∥
offline micro-repair lane (cluster-collision guard · long-lake parse_circuit bare-year fix ·
holcomb/larson/reddick investigations; LAKE mutations incl. davis fold DEFERRED to W6 gate —
manifest is a shared write-point, no concurrent writers).

**W6 CLOSED + GATE MUTATIONS (2026-07-07):** W6: **15 minted** through a FLAPPING CL token (3
pre-verified rows minted offline from CL-locked quotes rather than zero-yield — ratified; then
lane held and 12 read+minted; 0×429, no expired-token retries, no alt paths); 3 known
deferred-recovery skips (mendoza/porter/trent → W9); Ruckman minted w/ adjudicated ¶-pin (¶ 9) —
carries 1 disclosed LINT-2 medium because PINCITE_RE lacks ¶ support (the O1-deferred FP class
resurfaces) → ADJUDICATED option (a): extend PINCITE_RE, fix dispatched w/ Larson LEXIS-noise-
list item; Ruckman stale-docket + Williams star-sparsity noted for S9. Case Index 553 (+15),
build 655/2343 green, mint gate 0/0/0 ×15. Micro-repair lane landed earlier: cluster-collision
mint guard (43/43, real dry-run of davis stub now REFUSED [cluster-collision]) · parse_circuit
bare-year fix (+2d/3d ordinal regression caught) · holcomb WATCH adjudicated (panel withdrew own
opinion, reh'g moot, NO successor as of 2026-07 → page-less watch terminal, pointer ca9 23-469 /
cluster 10365516) · larson official=159 Or. App. 34 (LEXIS-cite tie was spurious → noise-list
extension approved). GATE MUTATIONS: davis fold APPLIED (A18, alias-folds:1, record kept);
**reddick ca5→ca3 REFUTED-DECLINED** — orchestrator fetched ground truth at the gate (docket
7688717 court_id=ca5); the audit flag was wrong, W6's on-read mint correct; verify-before-mutate
held against the run's own audit artifact. Scoreboard: **84/148 minted** (W1-W6), W7/W8 41 rows
all-clean-audited, W9 tail ~8. W7 dispatching ∥ lint/serializer micro-fix.

**W7 CLOSED (2026-07-07):** **21/21 minted, 0 skips, 0 escalations** — the pre-W5 audit's
clean-frontier call held on read (every row re-verified; cluster-collision guard passed); 48 MCP
calls 0×429 no outage; Case Index 574 (+21); build 676/2464 green; mint-gate 0/0/0 ×21; LINT-2/9
= 0 after ratified body-only remediation (incl. de-linking Austin's forward refs to W8-pending
Timbs/Bajakajian — reciprocal re-link owed at W8). Data honesty: modern SCOTUS rows pinned to the
S.Ct. parallel reporter CL actually paginates; Lozman A3 slip; Burdeau/Ex-parte-Jackson OCR
normalized; Youngblood lake-year quirk (1989 vs decided 1988-11-29) flagged S2. ∥ Micro-fix lane
landed: PINCITE_RE ¶/¶¶ extension — LINT-2 corpus 311→302 (−9 = Ruckman + the O1-deferred
Carroll/Benn ¶-class, 0 NEW) + LEXIS type-2 state noise-list (5 literal reporters; federal
LEXIS structurally excluded) w/ larson enrich verified in-memory (159 Or. App. 34 / 977 P.2d
1175 parallel) PREPARED for the next lane session (cluster uncached). Scoreboard: **105/148
minted** (W1-W7). W8 (frontier 2, 20 rows) dispatching — last main wave; then W9 tail + R11.

**W8 CLOSED — MAIN WAVES COMPLETE (2026-07-07):** **20/20 minted, 0 skips/escalations** (Roaden·
Timbs·Bajakajian·$8,850·James-Daniel-Good·Von-Neumann·Scott·Donovan·Giordano·Keith·Stone-v-
Powell·Blue·Caceres·Satterfield·Neville·Weatherford·Will·Warshak·Robinson-4th-en-banc·Rochin);
~65 calls 0×429; Case Index 594 (+20); build 696/2575 green; mint-gate clean; Rochin history-
rendered per §7 (DP shocks-the-conscience live via Sacramento-v-Lewis, 4A-exclusion function
superseded by Mapp — precise, not disguised); Robinson-4th/Satterfield frontier-splits framed
per LINT-21 (Terry armed-vs-dangerous; Nix active-pursuit); Austin↔Timbs/Bajakajian reciprocal
re-link LANDED (owed from W7); modern-id cluster→sub-opinion trap caught on read (4591916-as-
opinion = 1993 Tax Court memo — refetched, verified). **MAIN-WAVE TOTALS W1–W8: 125/148 minted,
0×429 across ~400 wave CL calls, 2 CL outages survived per L4 discipline, 8 wrong-case mis-keys +
1 duplicate caught by on-read verification, zero pages authored on a broken identity.** W9 tail
dispatching per R8-W9-TAIL-PLAN.md (8 mintable now + ≤7 behind bounded cite recovery + holcomb-
watch/zorn terminals); then R11 ledger + non-page fold + LINT-17 + S7 handoff.

**W9 TAIL CLOSED — R8 AUTHORING COMPLETE (2026-07-07):** cite recovery 7/7 (larson enriched 159
Or. App. 34 · frederick web-cited 500 Mich. 228 dual-leg · robinson/lewis/mendoza/porter/trent
slip-stamped under CURRENT ids, allowlist +5, stamper 7/7) → **20 minted, 0 honest skips** — the
15 dispatched + 5 SUPPLEMENTAL (burgess/capers/castillo/chavez/crumble: re-keyed in the pre-W5
audit but never re-dispatched; agent re-derived mintable from the lake and closed them, driving
deferred to 0); gutierrez authored via the plain_text REST method as documented. Terminals:
holcomb→watch, zorn→data-escalation/unverifiable-pending (lake untouched, worklist in-row).
**FINAL R8 PARTITION (R11 input, sums exactly): authored 145 · folded 1 (davis) · watch 1
(holcomb) · escalated 1 (zorn) = 148.** ~55 calls 0×429; Case Index 614 (+20); build 716/2699
green; mint-gate LINT-14/15/16 = 0 CORPUS-WIDE. S9-owed carried honestly: capers/castillo lake-
docket mismatches (body uses CL-correct), capers/chavez best-effort star pincites, trent
unpublished-6th-Cir. reverify flag, plus the standing history-Field-I + Williams star + Ruckman
docket items. NEXT: S6 close-out — R11 coverage-ledger assembly (148-row proof + the 58 non-page
placements fold + mention-stub/removed/folded universe), LINT-17 wiring (R12), S6-close
CodeRabbit gate over the full S6 code surface, S6→S7 handoff (ledger-deferred homes rows ·
Case-Index schema-3 flip · plain_text blind-spot · Field-I S9 items).

**S6 CLOSE-OUT DELIVERED (2026-07-07):** R11 coverage ledger assembled PROGRAMMATICALLY
(`_overhaul2/scripts/build_coverage_ledger.py` from signed artifacts + manifest) — partition
PASS: **authored 145 + brief-mention 55 + excluded-remit 26 + folded-alias 8 + watch 3 +
removed 2 + unverifiable 1 = 240 captions**, every one exactly one terminal, authored 145/145
page+lake+manifest verified, folds name survivors, R8 148-partition re-derives exactly. NUM-04
handled HONESTLY: no machine artifact of the 388 exists → no fabricated reconciliation; ledger
exposes the join surface + a labeled corpus_mention_baseline instead. LINT-17 live:
fail-closed HIGH, frozen-allowlist, 9/9 self-tests, corpus 0/734 captions, registered in
run_all. Honest residual: 5 cite-format placeholders excluded-remit + 53 legacy antecedent
bare-mentions brief-mention/not-adjudicated w/ pointers. **LINT-17's FIRST CATCH (pre-CI): 3
page-less captions clearing R2 on their face — Anderson v. Creighton (QI, in White v. Pauly) ·
Bell v. Wolfish (detainee searches, in Florence) · Colonnade Catering (closely-regulated, in
Biswell). ORCHESTRATOR ADJUDICATION: mini-batch W10 through the standard leg (stub → R1 two-key
→ mint) — same D1-flip class as the worklist, §9 guard holds (148 ≤ 150), "surfaced not
trimmed."** Ledger + LINT-17 re-run after W10; then S6 CodeRabbit gate + handoff.

**W10 MINI-WAVE CLOSED — S6 AUTHORING FINAL (2026-07-07):** LINT-17's 3 catches minted through
the FULL standard leg (--add-candidates → --smoke R1 two-key → enrich → repair-from-cache →
R8 mint; no hand-written records; Colonnade seed-date corrected 03-05→02-25 by the cache-
authoritative repair): Anderson v. Creighton (QI Key) · Bell v. Wolfish (Special Needs Key +
SITA Related) · Colonnade (closely-regulated Key). 16 calls 0×429; LINT-13 0; mint-gate 0 ×3;
build 719/2710; Case Index 617 (+3 exact). **FINAL R11 PARTITION: authored 148 + brief-mention
55 + excluded-remit 26 + folded-alias 8 + watch 3 + removed 2 + unverifiable 1 = 243 distinct
captions, machine-checked PASS; ledger escalations 3→0** (Anderson's page surfaced Mitchell v.
Forsyth as a legit new brief-mention row — the ledger machinery working as designed). Scope
arithmetic stated honestly: authored PAGES = 148 ≤ §9 guard 150 (page-planned rows ever = 151;
3 of the original 148 went to honest non-page terminals). LINT-17 corpus PASS page-backed (not
allowlisted). S6 AUTHORING COMPLETE — remaining S6-close: spec-completion CodeRabbit gate over
the S6 code surface (formal trigger), S6→S7 handoff, run brief.

**S6 CLOSED (2026-07-07):** spec-completion CodeRabbit gate (formal trigger, artifact
S6-coderabbit-2f77004.md): 15 findings (12 major/3 minor), ALL UPHELD → ALL FIXED same session
(fail-closed hardening across gate.sh timeout, lint21 mandatory fixtures, lint17 allowlist
validation + 7 fail-closed self-tests, ingest state-None/slip-evidence/fetch-fail-queue/batch-
prevalidate/writeback-normalize + flag-dependency refusals + ruff batch, stamper WARN, mint
cluster-guard fail-open→RAISE, slip-test de-tautologized); item-10 read-only lake scan CLEAN
(665 records: 0 dup-year labels, 0 stale mutex fields — the executed repairs left no damage;
fix purely preventive). Suites: ingest/mint 43/43/projector/serializer/lint17/lint21 all green;
LINT-13 + LINT-17 corpus 0; run_all findings byte-identical to baseline. KNOWN-RED noted w/
owner: stamp_slip_only --self-test crashes on a hard-coded pre-promotion Landor path
(pre-existing, proven by stash test; stamper's real work complete + dormant; fix = fixture-seed,
next s6 touch). S6→S7 HANDOFF delivered (`_run/o2-execute/S6-TO-S7-HANDOFF.md`): scoreboard,
pipeline entry point + payload contract, **158 owed home_rows** (148 Key + 10 Related — S7
materializes at per-page conversion, zero-drop accounting) + 58 non-page placements, binding
amendments (per-page convert · schema-3 flip · plain_text fallback · L4 · no-S7-code-gate),
S9-owed register, lake state (665 records; 662-vs-665 prose-drift + baseline-56-vs-58 gaps
documented honestly in §6). **S6 IS CLOSED. NEXT: S7 opens with its USER INTERVIEW** (runbook:
Prompt.md regenerate-or-drop decision at minimum rides it) — autonomous stretch ends at this
pause; run brief served.

---

## S7 EXECUTE (opened 2026-07-08)

**S7 OPEN + PHASE 0 (2026-07-08):** User opened S7 at the S6-close pause. Prompt.md question
resolved from the record: COH-14 → S7 interview D3 (2026-07-03) DROPPED the reference — the
RUNBOOK §4-S7 fix-list is the record, verify-then-apply; no re-interview needed. Taxonomy
flexibility researched at user request (read-only): structure flexible BY DESIGN (R6 evergreen
test, A5/A6 reserve-don't-recut precedent, A8 weight-ordering); evidence sweep found scope
boundary HELD (Confrontation/habeas/§1983-mechanics clusters excluded on remit, 0 homeless
cases) but 3 intra-cat-11 strain signals: §1983/QI node absorbed 29 Keys across ~8
sub-doctrines (Bivens/§242 deferred R6 decision RIPE + unlogged; Tanzin/Landor awkward fits),
CAF (8 Keys) + Title III (4+3) under-tiered at C, officer-created-danger split-block
node-candidate. All deferred to cat-11 batch; Bivens shape surfaces to user before landing.
PHASE 0 committed 97dccb9: scripts/s7/survey.py (self-test 46/46) + build_worklist.py;
48/48 T1 rows path-resolved (0 unresolved), 45/45 T2 nodes exist (41 placed-stubs; only
pattern page authored — clean opening baseline), tiers carried UNCHANGED (R2); honest deltas:
slip 76→65 (pattern -11), c3 meta-intro 5→24 + inverted 21→36 (S5/S6 growth), TEACH-04e
19-vs-4 metric mismatch (re-derive at authoring).

**PHASE 1 MECHANICAL PASSES CLOSED (2026-07-08):** R15 step-1, one commit per pass, converter
deliberately NOT here (E2/E3: per-page at rewrite). **1a TEACH-12a (c3fc18d):** 17/17 H1s,
missing_h1 17→0; H1=title except 4 hook-title pages → canonical name per 72-page conformant
convention (ADJUDICATED; title-vs-hook rides R3 rewrites); run_all byte-identical 8372; build
719/2710. **1b TEACH-04d (1a37a0d):** 28 inverted labels → S1 canonical tier-word-first; 8
justified skips (incl. Framework:88 multi-circuit compound → its R3 rewrite); ORCHESTRATOR
REPAIR: worker's 3 Case-Index hand-edits re-rooted per single-writer — source = holding:
frontmatter on Basher/Gooch/Sandoval, sources fixed, index REGENERATED (converged byte-exact);
survey inverted 36→8 (=skips); run_all 8372→8337; S9-journaled: Basher tier disagreement vs
Curtilage:82, compound-label class. **1c TEACH-08:** 33/34 RD→"Lower-court developments"
renamed+moved above tables (verbatim content moves; [Brief, LCD, Key, Related, Visual,
Sources] order = exemplars); 1 FULL SKIP Fourth Amendment Framework (rule-skeleton legacy, no
Brief anchor, "& subsequent treatment" variant — rides its R3 rewrite); rd 34→1, lcd 2→35;
run_all 8337→8335 (the 2 known Chatrie LINT-3 FPs left the renamed scope — N5 re-pointing to
LCD headings is S9's roster job per S5 R11/§9, RECORDED: N5 coverage dark on renamed sections
until then); LINT-15 standalone 131→71 (rename-pending 30→0, order 30→0, HIGH 36→36 no new);
build 719/2710; transformer scripts/s7/teach08.py committed. NEXT: Phase 2 category batches —
pilot = cat-2 Standards of Proof (PC/RS split → RS + PC children Tier A + Proof Ladder C).

**PHASE 2 PILOT CLOSED — CAT-2 STANDARDS OF PROOF (2026-07-08):** PC/RS parent SPLIT → Reasonable
Suspicion (A) + Probable Cause (A), Proof Ladder stub AUTHORED (C), parent dissolved; all born
draft. R3 no-inheritance: 4 CL MCP spot-checks (Gates 238 / Brinegar 175 / Cortez 417-18 /
Pringle common-enterprise) CONFIRMED against primary text, opinion-ids from lake identity, 0 REST;
lake good-law re-verified (Aguilar/Spinelli superseded-correct foils; DANIELS under_review R3
catch → paraphrase + case-cite + ⚪, S9-owed). Named fixes: TEACH-04a maxim + 04f CREW mislink +
02c meta-intro APPLIED; 04e hit REFUTED-AS-TARGET (substantive who-decides doctrine, retained
reworded). 27 case pages re-homed/keyed (RS 9 + PC 14 + re-points); 1 owed home_row discharged
(Daniels→RS LCD, zero drops); aliases: PC = successor (old title + 2 old paths + DECK STEM
probable-cause-reasonable-suspicion per R13/R14 — 31-card deck resolves); registry re-pointed
(proof.* home_pages + proof-ladder statement filled). ORCHESTRATOR ADJUDICATIONS: rung anchors
Terry/Gates/Brinegar multi-homed Key-on Ladder (R3 model, Key-table truthfulness); Cortez+Sokolow
Key-on RS (A6 findability-without-re-homing, primaries stay Terry Stops); deck-stem successor PC
RATIFIED; mnemonic GR#3 placement RATIFIED. TEMPLATE RULES A-F adopted (split batch re-points own
category index + owns alias collisions; no broken mid-line pin deep-links; LINT-15/16 standalone
per batch — NOT in run_all roster; no bare weight-tier words in authored cells; plain-italic
registry mirror = S7 standard). Journaled: Case Index 622 LINT-16 pre-existing generated-schema
condition (schema-3 flip owed S7/S8 to generator); master-index + 11 doctrine-page wikilinks to
dissolved title resolve via alias, re-point in owning batches/S3 A7(4) regen. GATES: run_all
8335→8330 (all deltas explained; LINT-5 HIGH -2 broken anchors not reproduced; LINT-7 -2 incl.
stop-and-frisk register fix ×7; LINT-16 Historical-token catch FIXED in-batch), LINT-15/16
standalone 0/0 on authored+touched, survey 90 pages em 23.9/1k, build 720/2715 green (+1 input =
-1 parent +2 children). NEXT: cat-3a Two Definitions severance (deferred-as-index C1 item →
Trespass A + REP A, Katz re-homed in).

**BATCH 2 CLOSED — CAT-3a TWO DEFINITIONS SEVERANCE (2026-07-08):** the S3 wave-2
deferred-as-index item severed: index → lean sub-umbrella overview (R2 no-tables, born draft) +
Trespass (A) + Reasonable Expectation of Privacy (A) authored, born draft. R3/R6: 6 CL MCP
search_document calls, opinion-ids from lake identity incl. Katz HARLAN CONCURRENCE via
sibling_ids (never cluster), 0 REST 0x429; Jones *405 / Katz 351 / Harlan 361 confirmed;
Carpenter html_with_citations = SLIP-ONLY (no US star) → R5 T3 paraphrase-downgrade w/ 585 U.S.
296 case-cite (G3/G4 honest); Chatrie = T4 current-Term (corrupted CL cluster 10881683 noted,
no call). TEACH-01 APPLIED (Chatrie SCOTUS-in-developments → REP Key mention + cross-ref;
geofence exposition NOT authored — D6 digital batch owns); 02c leaks → HTML-comment provenance;
TEACH-05 worst-density page cleared (135 raw removed; children 0 LINT-10). KATZ APPENDIX-B MOVE
EXECUTED: primary REP Key-Anchor, Standing keeps Related cross-doctrine (Rakas measures REP).
27 case pages re-pointed row-by-row; owed home_rows 3/3 discharged (Grady→Trespass Anchor
[under_review honest, S9 promotes], Wilson+Moore-Bush→REP Related). ADJUDICATIONS ACCEPTED:
Jardines Key-on-Trespass (A6, primary stays Knock and Talk); Smith (2024) dead index-framing
DROPPED not re-pointed (digital batch carries Smith Key w/ Chatrie — OBLIGATION JOURNALED);
Carpenter primary→REP VERIFIED CORRECT (old primary WAS the dissolving index, not Third-Party;
digital batch may co-home); overview type:doctrine matches sibling (normalization Q → S9).
NEW TEMPLATE RULE G ADOPTED: dissolving-index Related rows whose substance belongs to a third
page are DROPPED with the real primary kept, never re-pointed into a wrong-scope child;
zero-drop binds only owed ledger home_rows. GATES: run_all 8330→8273 (-57, every lint ↓ or
held), LINT-15/16 standalone 0/0, survey em 23.0/1k slip 63, build 720/2722 green, Case Index
617 idempotent. NEXT: cat-3b Curtilage (A) + Open Fields split-out (B); SACO stays cat-6
Entry-to-Arrest per spec R10 precedence (changelist row-7 note is a cross-ref, not placement).

**BATCH 3 CLOSED — CAT-3b CURTILAGE + OPEN FIELDS (2026-07-08):** Curtilage REWRITTEN (A, born
draft) + Open Fields AUTHORED (B, born draft, honest no-LCD — no verified open-fields circuit
case, fail-closed not fabricated). R6: 11 MCP calls 0 REST 0x429, opinion-ids from lake
lead_opinion_id; Dunn ★301/★302, Oliver ★179/★173, Hester ★59, Jardines ★6/★7 CONFIRMED;
Collins 2018 = CL slip-only (same class as Carpenter) → R5 T3 paraphrase-downgrade w/ 584 U.S.
586 case-cite, evidence pos 48767; Curtilage slip 1→0 leaks 3→0. DUNN-FACTORS-IN-THE-RULE
APPLIED (own ^rule-curtilage callout, borrowed KT callout demoted to cross-ref — cleared the 2
baseline LINT-2 findings). Split re-homing: Hester+Oliver primary→Open Fields w/ Key-on
Curtilage (the line IS the training point); Dunn primary stays Curtilage (factors=test) w/
Key-on OF (barn=worked example); See/King/French/Basher +Curtilage:Related (A6). Owed
home_rows 6/6 discharged (GM Leasing Key-table; May-Shaw/Karston/Larson/Weaver ledger-Key →
LCD bullets; Moore-Bush Related→LCD). ADJUDICATIONS ACCEPTED + TEMPLATE RULES: H — ledger
home_row discharge = page-presence; presentational tier (Key-table vs LCD bullet) is the
author's S5 call, LCD honest for circuit/state developments. I — ZERO em-dashes inside table
cells (LINT-10 sums a table as one block, confirmed empirically). Aerial restraint held (SD7):
Ciraolo/Riley/Dow exposition deferred to T2#5, case frontmatter UNTOUCHED — AERIAL BATCH OWES
primary moves + search.aerial-surveillance statement fill (JOURNALED). Tuggle home gap
(Plain-View-only home, curtilage substance) → S9 coherence. SACO cross-ref only per spec R10.
Registry: curtilage statement +Dunn factors, open-fields filled. GATES: run_all 8273→8233
(-40 all-decrease), LINT-15/16 0/0, survey em 22.4/1k slip 62 leaks 53, build 720/2725, Case
Index 617 idempotent. NEXT: cat-3 digital sub-umbrella (SD2: Third-Party & CSLI parent A +
D6 children CSS B / Reverse-Keyword & Geofence B / Real-Time C / IGG C + Title III C sibling
w/ GAP-03c §702) — carries journaled obligations: Smith (2024) Key w/ Chatrie, Carpenter
co-home decision, Chatrie exposition home.

**BATCH 4 CLOSED — CAT-3 DIGITAL SUB-UMBRELLA + TITLE III (2026-07-08):** biggest batch: index
SEVERED (worker's substantive-index first-pass REFUTED BY LINT-19 — R2 no-tables — and
self-corrected; A6 taxonomy line confirms "Third-Party Doctrine & CSLI" is the FIRST CHILD) →
lean umbrella overview + 6 authored pages born draft: Third-Party & CSLI (A) · Reverse-Keyword
& Geofence (B, CHATRIE EXPOSITION HOME — batch-2 obligation discharged, Smith (2024) Key
alongside per journal) · Cell-Site Simulators (B) · Real-Time Tracking (C) · IGG (C, honest
no-controlling-precedent) · Electronic Surveillance & Title III (C + GAP-03c §702/parallel-
construction). R6: 7 MCP calls 0 REST (Smith-v-Maryland ★744, Miller ★443, Knotts 281, Karo
715, Berger ★56 confirmed); R5: Carpenter T3 / Chatrie T4 / Smith(2024) F.4th reporter pin.
18 case re-homes incl. CARPENTER CO-HOME RATIFIED (Key on CSLI child, primary stays REP);
Knotts/Karo primary→Real-Time; Berger primary→Title III; 10/10 owed home_rows discharged
(rule H: index-owed circuit rows → LCD honest tier). CHATRIE CLUSTER ADJUDICATED: lake record
IS the source of truth — cluster 10881683 GENUINE (lead 11349205, S2-built 07-04); the
batch-2 "corrupted/do-not-ingest" note was STALE pre-ingest state, RETIRED; T4 unaffected
(no reporter cite yet, status under_review current-Term). LINT-17 attestation: corpus 0 —
Andrews/Seymour/Gratkowski/Beautiful-Struggle cited as plain-italic brief-mention terminals,
Lambis avoided (no terminal), dead wikilinks to page-less captions FIXED. TEMPLATE RULE J
ADOPTED: net-additive AUTHORING batches are judged zero-new-HIGH + explained baseline-class
MED/LOW deltas, not strict run_all ≤ (mechanical passes keep strict ≤): run_all 8233→8252
(+19 all MED/LOW exemplar-class; LINT-10 0, 15/16 0/0, 17 corpus 0, 19 overview 0). Registry:
7 search.digital.* nodes existed, 4 statements filled, third-party home re-pointed. Build
720→721 (+1 severed child)/2755; Case Index 617 idempotent (18 rows = the re-homes).
RESIDUE JOURNALED: Riley disambiguation owed (Florida v. Riley = aerial batch; Riley v.
California umbrella Key-on → CSLI child or drop, aerial/SIA batches decide); 7 residual
LINT-2 med honest (5 Chatrie T4 quotes + 2 IGG paraphrase-rule heuristic — no unverified pin
added to silence a lint). NEXT: cat-3c sibling sweep — Aerial & Enhanced (B, OWES
Ciraolo/Florida-v-Riley/Dow primary moves + registry fill) + Private & Foreign (B) +
Abandonment (B) + Tents (C retitle w/ S3-owned alias); then Plain View & Plain Feel (A).

**BATCH 5 CLOSED — CAT-3c SIBLING SWEEP (2026-07-08):** 4 units born draft: Aerial & Enhanced
(B authored — batch-3 residue DISCHARGED: Ciraolo/Florida-v-Riley/Dow primary→Aerial w/
Curtilage homes dropped-not-Related [index-table consistency], Kyllo A6 co-home Key, Tuggle
home gap closed +Aerial Related) · Private & Foreign (B authored — Jacobsen ★115 / Walter
★657 T1; hash-match split Wilson/Reddick wikilinked vs 6th-Cir MILLER PLAIN-ITALIC
brief-mention w/ 1976-Miller disambiguation comment, LINT-17 honest) · Abandonment (B
born-again, ff 1→0 w/ LOGGED D2 dispositions: BLUF section DELETED w/ genuine content →
Apply-it items, em 25.2→3.1/1k) · Tents (C born-again RETITLED "Tents & Temporary Dwellings",
filename KEPT so slug satisfies R14(i) + bare-stem alias, deck 17 cards LINT-25=0, "(woven
in)" c4 leak cleared). 6 MCP calls 0 REST (Ciraolo ★215, Kyllo ★40/★35, Riley ★452 w/
FAA caveat, Dow ★239). FLORIDA-v-RILEY STALE DIGITAL MIS-HOME REMOVED (data error, aerial ≠
third-party — explains batch-4's "Riley homes to overview" residue); Riley v. California
confirmed SIA-owned, untouched. Owed home_rows 6/6 (Burdeau by-presence; Hunt/Small/Crumble→
Abandonment LCD; Ruckman Key + LaDuke lineage → Tents, stale no-page notes cleared). Drone/UAS
= honest gap, no terminal no case. ORCHESTRATOR REPAIR: Hester mirror drift (batch-3 ours) —
homes[] had dropped Abandonment, Appears-on missed Open Fields + stale Curtilage role; BOTH
SIDES repaired, index regenerated (own-run drift never accumulates to S9). OWED FORWARD:
FA-Framework batch demotes its private-search bullets/co-anchor homes to Private&Foreign
pointer (rule A); Case-Index-good vs lake-under_review divergence (Wilson/Verdugo/Burdeau)
pre-existing → S9; ER-index 4 LINT-19 HIGH pre-existing → its A4 severance batch. GATES:
run_all 8252→8198 all-decrease (introduced anchors fixed→0), LINT-15/16 0/0, LINT-17 0,
LINT-25 0, survey em 20.5/1k, build 721/2768 (+13 alias redirects). NEXT: Plain View & Plain
Feel (A, closes cat-3) — TEACH-02c ×6, TEACH-03 ×5, Dickerson in-page note T2#12.

**BATCH 6 CLOSED — PLAIN VIEW & PLAIN FEEL (2026-07-08) — CATEGORY 3 COMPLETE:** Tier-A
born-again rewrite as the App-A single node (Dickerson plain-feel = dedicated in-page H2 per
T2#12, not a child); filename KEPT per Tents precedent (slug=deck stem plain-view-doctrine,
LINT-25 0, 33 inbound links native; H1/title = "Plain View & Plain Feel", +4 alias redirects).
14 MCP calls 0 REST: Horton ★130/★137, Hicks ★325, Dickerson ★375-76/★378, Coolidge
★466-67 confirmed. EXEMPLARY R3 CATCH: Hicks ★328 "cursory inspection" missed segment
9430865 → RUN TO GROUND in sibling 9430866 = SCALIA MAJORITY rebutting O'Connor — attribution
STANDS ("not found ≠ fabricated"); S9 coherence note: check sibling pages for mis-attribution.
TEACH-02c 7→0 (4 no-standalone cases now paged + wikilinked LINT-17-checked; Chatrie
paged/Brief); TEACH-03 5→0 (Collins T3, Herlth 2026-PA-Super T3 no-CAP-no-T2, Chatrie general
cite no slip literal; pre-2020 anchors already T1). Owed rows 4/4 (Loines/Loera/Ganias/Burgess
ledger-Key → LCD honest tier, rule H). Chatrie moved OUT of LCD (N5 SCOTUS-in-frontier bar) →
Brief. D8 flashlight-scar concordance VERIFIED (exposed-vs-concealed line identical to KT).
ADJUDICATION + TEMPLATE RULE J AMENDED (J'): the worker leaned Buie/Long from Related rows to
a Brief vantage-source paragraph partly to avoid known-false-positive LINT-7 page-title HIGHs
— shape ACCEPTED as doctrinally defensible on its own terms (vantage-source pedagogy), but
the incentive was rule J's fault: HENCEFORTH known-false-positive classes (LINT-7 page-title
variant, 140 in baseline) are EXEMPT from zero-new-HIGH when the apparatus is doctrinally
correct, per-finding explained — LINT-AVOIDANCE MUST NEVER DRIVE CONTENT. LINT-7 register
exemption decision routed to S8/S9 (journaled). Andreas sole-home role="Related" semantics +
Horton/Brown mid-line ^pin carat-leak class → S9 sweep. GATES: run_all 8198→8136 (-62, HIGH
-54, strict all-decrease anyway), LINT-15/16 0/0, LINT-17 0/0/0, survey slip 65→59 em
19.9/1k, build 721/2772. CAT-3 DONE: 13 units (overview + 12 pages) across batches 2-6.
NEXT: cat-4a — When a Seizure Occurs (A retitle, TEACH-04b :48 qualifier + TEACH-04e DONOR
:54 conversion) + Seizure of Property (B new) + Stop-and-Identify (C new, Hiibel).

**BATCH 7 CLOSED — CAT-4a SEIZURE THRESHOLD (2026-07-08):** When a Seizure Occurs (A born-again
RETITLE, filename kept per precedent, deck 28 cards LINT-25 0, +"When a Seizure Occurs" alias)
+ Seizure of Property (B authored) + Stop-and-Identify (C authored, honest no-LCD both). 21 MCP
calls 0 REST: Mendenhall 554, Hodari ★626, Jacobsen ★113, Place ★709, Hiibel ★186/188
confirmed; TORRES = slip-only (no CAP star, "bullet that missed" 0 hits — Torres never
addresses missed shots) → T3 downgrade, all Torres quotes/pins removed. TEACH-04b APPLIED as
qualified rule: shot-that-HITS = force seizure at that instant (Torres); shot-that-MISSES = no
force seizure BUT show-of-authority + submission can still seize (Hodari/Mendenhall) — framed
as doctrinal inference, NO fabricated Torres quote. TEACH-04e DONOR CONVERTED (D2): the :54
"Field framing" decision sequence → 5-step Apply-it list, LOGGED; corpus ff 3→2. Re-homes:
Soldal Key-Anchor Trespass→Seizure-of-Property (SD2, batch-2 interim home superseded);
Hiibel Terry→Stop-and-Identify + Kolender added; Van Leeuwen +Key; Brendlin stale
Standing pointer → Traffic Stops (App-B). Owed rows 2/2 (Carter/Amos → LCD). Registry:
seizure.property + stop-and-identify statements filled. ORCHESTRATOR REPAIR (own-run drift,
Hester precedent): batch-2 Trespass page's stale Soldal Key-row DEMOTED to Related w/
[[Seizure of Property]] primary-home cell (run_all 8092→8091). J′ invoked properly: 2 LINT-7
Knock-and-Talk page-title FPs explained per-finding, content not lint-shaped. OWED FORWARD:
cat-4b Terry batch reconciles Hiibel(Key-on)/Kolender(Related) presentation; arrests batch
decides Atwater/Gerstein/Moore/McLaughlin Key placement (kept honest on Person page while
arrests/ stubs unauthored); 5 case pages w/ malformed mid-line ^pin anchors
(Jacobsen/Brower/Chesternut/Hiibel/Kolender) → S9/S6 anchor-cleanup register. GATES: run_all
8136→8091 (HIGH -39), LINT-15/16 0/0, LINT-17 0, LINT-25 0, survey em 19.1/1k Person
26.7→1.5/1k, build 721/2777 (+5 alias redirects). NEXT: cat-4b — Terry Stops (A) + Traffic
Stops (A, Brendlin Key landing) + Collective Knowledge (A, horizontal-pooling split section +
Herring→Key w/ Whiteley caveat).

**BATCH 8 CLOSED — CAT-4b STOPS FAMILY (2026-07-08):** 3 Tier-A born-again rewrites: Terry
Stops (em 137→10, ff 1→0 CONVERTED w/ logged D2, quantum/stop boundary split vs batch-1 RS
page) · Traffic Stops (em 118→4, BRENDLIN KEY SEAT landed ★251 MCP-confirmed, Glover Key
honest primary, Whren→Rodriguez→Heien spine) · Collective Knowledge (em 61→8, HERRING→KEY w/
WHITELEY CAVEAT as own Brief para — imputation baseline vs exclusion consequence + new
"reading Herring as imputation" pitfall; Pringle suspect-side STRENGTHENED w/ 371/373 pins).
7 MCP calls 0 REST. IDENTITY CATCH: D.C. v. R.W. stub identity_checked:false → CONFIRMED
GENUINE 2026 SCOTUS per curiam (op 11312795, anti-divide-and-conquer dispatch-stop rule) →
Key per N5, T4 slip; LAKE FLIP OWED to S2 repair lane (journaled). LINT-17 DISCIPLINE HELD:
Nafzger/Ibarra/Balser NOT NAMED (no page/no terminal — fail-closed refusal correct), Cook
dropped (framing depends on Balser); split taught w/ 4 page-backed circuits. ORCHESTRATOR
RULING: spec R9 signs the NAMED split (Massenburg / communication-nexus / Cook-Balser) —
completion via brief-mention coverage-ledger terminals dispatched as mini-lane L1 (identity
verify → disposition artifact → build_coverage_ledger regen → page naming patch), the honest
lightweight path vs 3 full mints. Owed rows 11/11 (Cooley+R.W. Key per N5; 9 circuit → LCD
rule H). Hiibel/Kolender batch-7 presentation reconciled (Related w/ Stop-and-Identify
primary). Anchor-cleanup register +4 (Hensley/Adams/Sibron/Whren mid-line pins; now 9 total).
Cooley Field-I unverified ⚪ → S9 standing class. GATES: run_all 8091→7904 (HIGH -138
strictly-decreasing), LINT-15/16 0/0, LINT-17 0, LINT-25 0, survey corpus em 3268 ff 1,
build 721/2777 byte-identical, Case Index idempotent. NEXT: mini-lane L1 (pooling terminals)
then cat-4c arrests (Arrest-in-the-Home A + Arrest & Arrest Warrants B + Prompt-PC C).

**MINI-LANE L1 CLOSED — SPEC-R9 NAMED POOLING SPLIT (2026-07-08):** Nafzger/Ibarra/Balser
identity-verified via MCP SEARCH-first (0 REST) w/ TWO ANNEX CORRECTIONS: Ibarra = 5th Cir.
2007 (493 F.3d 526, 530 — annex/dispatch guessed 10th; namesakes refuted) and Balser = 1st
Cir. 2023 (70 F.4th 613 — annex said 6th); Nafzger 974 F.2d 906, 913-14 (7th) exact.
IDENTITY CATCH #2 THIS SESSION: ledger "United States v. Cook" cluster 3165557 = OSHAN Cook
(2015), the doctrinal case is DONALD Cook 277 F.3d 82, 86 (1st Cir. 2002, cluster 776186) —
RE-KEY OWED to S2 repair lane (joins R.W. identity flip; consolidated repair before S7
close). Signed disposition artifact S7-L1-POOLING-DISPOSITIONS.{md,jsonl}; assembler gained
minimal section-6c loader (code delta — rides the standing code gate); ledger REGENERATED
PROGRAMMATICALLY: partition 243→246 (brief-mention 55→58), machine-check PASS 0 conflicts,
corpus_mention_baseline 56 unchanged; LINT-17 allowlist regenerated in-write. Collective
Knowledge page patched surgically (+9/-5): Ramirez accord-roster (Nafzger/Ibarra plain-italic
w/ verified pins), Cook–Balser reservation bullet (1st Cir. geography corrected), synthesis +
Sources. GATES: LINT-17 0, run_all 7904→7912 (+8 all LINT-5 MED page-less-name class, HIGH
unchanged 4825), LINT-15/16 0/0, build 721/2777. SPEC R9 NAMED SPLIT NOW COMPLETE on-page.
D7 PRE-FLIGHT FINDING: SACO family (Nora/Fisher-San-Jose/Al-Azzawy/Allen/Vaneaton) has NO
pages, NO terminals, NO manifest records — S6 A1 pre-seed did not cover it; Maez alone
authored. D7's Nora-spine section (pincites at 1055) requires a MINT WAVE. Mini-lane L2
dispatched TWO-PHASE: (a) identity verify + evidence + page-vs-terminal proposal per S6 D5
frontier floor, PAUSE; (b) orchestrator adjudicates, then standard-leg mint (W10 precedent).
Arrests batch (cat-4c + Entry-to-Arrest D7) holds until L2 lands.

**MINI-LANE L2 CLOSED — D7 SACO MINT WAVE (2026-07-08):** TWO-PHASE lane complete. Phase (a):
5 identities verified SEARCH-first (16 MCP 0 REST) — Nora 765 F.3d 1049 (9th 2014, ★1055
confirmed; corrects dispatch's 743 guess vs signed S6 A1), Al-Azzawy 784 F.2d 890 (9th 1986,
not the 1985 sister), Vaneaton 49 F.3d 1423 (9th 1995), Fisher-San-Jose 558 F.3d 1069 EN BANC
ONLY (panels barred), Allen 813 F.3d 76 (2d 2016, namesakes refuted); page-vs-terminal
proposal per S6 D5 frontier floor. ORCHESTRATOR ADJUDICATION: mint 3 (spine + both
containment-line poles) / terminal 2; §9 guard = S6's own scope guard, S7 discoveries ride
the mint w/ frontier floor (S6 148 untouched; S7-minted counter = 3); BERKOWITZ CORRECTION
(paged 7th-Cir narrow-side rep — L2a over-caution reversed, nameable). Phase (b): worker
STOPPED HONESTLY at credential boundary (no token in its env; refused to force) → terminals
booked + ledger 246→248 + payloads staged. ORCHESTRATOR RAN THE S2 BUILDER LEG (token at
~/.config/cssi/cl-token per memory): --add-candidates 3/3 appended (manifest 665→668) → R1
smokes 3/3 verified_identity (2+2+4 calls, cache-assisted, 0x429) → worklist +3 rows leg
s7-discovery w/ adjudication notes (W10 lint17-catch precedent; 151→154, s7_discoveries
counter) → dry-runs 3/3 clean staged-lint 0 → MINTED 3/3 born under_review. FINALIZATION
(body-only, own fresh pages, ratified class): 6 mid-line ^pin anchors → end-of-line splits,
5 em-dash blocks → parens/period-cite, ENRICH-CONFIRM resolved by orchestrator MCP
spot-check — Nora Payton-quote pin = ★1054 EXACT (position 15602 between markers 14213/22131,
evidence in-comment). Maez treatment enrich → S9 (cache absent, honest). LEDGER FINAL:
251 rows PASS (authored 151 + brief-mention 60 + excluded 26 + folded 8 + watch 3 + removed 2
+ unverifiable 1); Case Index 620. GATES: LINT-17 0, LINT-13 0, run_all 7933 (HIGH 4825 =
baseline EXACT, +21 MED/LOW baseline-class on 3 new case pages), build 724/2783. D7 reliance
map COMPLETE for the arrests batch: 9th at page grain (Nora/Al-Azzawy/Vaneaton) + Maez 10th
paged + Berkowitz 7th paged + Allen 2d/Fisher 9th terminals + Harris remedy tail paged;
1st/3d/4th/8th + Morgan-6th/Knight-11th honest-unmapped. NEXT: cat-4c arrests batch
(Arrest-in-the-Home A + Entry to Arrest A w/ D7 SACO section + point node + Arrest & Arrest
Warrants B + Prompt-PC C).

**BATCH 9 CLOSED — CAT-4c ARRESTS + D7 SACO (2026-07-08) — CATEGORY 4 COMPLETE:** Entry to
Arrest AUTHORED (A, T2#30) carrying the D7 SACO/constructive-entry section + NEW POINT NODE
seizure.person.constructive-entry (grammar corrected vs dispatch — sibling family is
seizure.person.*, no seizure.home object; LINT-20 0 + self-test PASS) — split taught honestly:
recognizing 2d(Allen terminal)/9th(Nora★1054-55/Al-Azzawy/Vaneaton pages)/10th(Maez page) +
6th named-only; narrow 7th(Berkowitz page)/11th(KNIGHT PAGE — IDENTITY CATCH #4: L2 map said
unnameable, ground truth = full authored page, split STRONGER)/5th named-only; 1st/3d/4th/8th
unmapped plainly; containment-line poles + Nora-1055 perimeter point + Harris remedy tail all
authored. Arrest in the Home born-again (A, em 81→2; SD2 held: constructive-entry strand
moved ONCE, Payton/Steagald black-letter stays canonical here w/ reason-to-believe LCD
Brinkley/Vasquez-Algarin); Arrest & Arrest Warrants (B) + Prompt-PC (C) authored. R5:
Case-v-Montana slip REFUTED-AS-TARGET (current-term sanctioned). Batch-7-owed re-homes
executed row-by-row (Atwater/Virginia-v-Moore/Gerstein/McLaughlin primary→arrests pages,
Seizure-of-Person tables demoted to Related; Moore-v-Illinois 6A namesake disambiguated,
untouched). 11/11 owed rows zero-drop. Registry: constructive-entry NEW + arrest-warrant +
prompt-pc statements filled. 5 MCP calls 0 REST (Watson ★424, Atwater 354, Devenpeck 153,
Gerstein 114, McLaughlin 56-57). Anchor-cleanup register +2 (Gerstein/McLaughlin → 11 total);
al-Kidd URL divergence → S9. GATES: run_all 7933→7913 (HIGH 4802, -23, zero new), LINT-15/16
0/0 x5, LINT-17 0 (no ledger regen needed — no new terminals), LINT-20/25 0, survey em 3190,
build 724/2794 (+11 alias redirects), Case Index 620 idempotent. SCOREBOARD: cats 2/3/4
COMPLETE = 30 doctrine units born draft + 3 S7-minted case pages; run_all 8372→7913 HIGH
-408 since S7 open. NEXT: cat-5 The Warrant (SD2 mega-batch: parent dissolves → Getting a
Warrant sub-umbrella [PC-Affidavit A · Magistrate B · Particularity A · Franks B] + Executing
[Knock-and-Announce A · Detention-at-Scene B · Scope-Manner B]; TEACH-01 Chatrie relocation +
GAP-06 :62 + TEACH-04h :149; geofence re-points now available to the authored digital page).

**BATCH 10 CLOSED — CAT-5 THE WARRANT (2026-07-08) — CATEGORY 5 COMPLETE:** the SD2 mega-batch
survived THREE consecutive API 529s (L4 discipline: same-agent resume x3 w/ 4-min + 15-min
backoffs; zero duplicate lanes, zero lost work). Parent The Warrant Requirement DISSOLVED
ENTIRELY (Appendix A has no such node) → 7 children authored born draft: Getting a Warrant
[PC-in-Affidavit A · Neutral Magistrate B (TEACH-04h :149 Johnson residue landed as Anchor) ·
Particularity A (expressive-materials strand surfaced: Marcus/Roaden/Heller/A-Quantity
page-backed + Fort-Wayne/Lee-Art terminals; GAP-06 verified no-residue; digital cross-ref
only, TEACH-01 held) · Franks B] + Executing [Knock-and-Announce A · Detention-at-Scene B ·
Scope-Manner B]. RESEARCH MODE ADAPTED TO OUTAGE: 0 MCP calls — every pin lake-grounded from
verified case-page records (the sanctioned S2-DB path); R3 carried assertions route to S9
panel as always; worker AUDITED ITS OWN 6 inferred opinion-ids wrong → corrected to case-page
values (citation-hygiene catch). 39 parent-homed cases re-pointed row-by-row + 5 detention
co-homes (primary kept Securing-the-Scene, cat-6 confirms) + rule-G drops (See/GM-Leasing/
Entick/Wilkes). Deck-stem warrant-requirement (33 cards) + 3 dying-path aliases → category
landing (ADJUDICATED); warrant.requirement node re-homed to landing. ORCHESTRATOR REPAIR:
worker's 3 hand-edited ledger pointers REVERTED by regen (single-source held — the assembler
is the only writer); Fort-Wayne/Lee-Art/PJ-Video rows remain valid terminals w/ STALE
POINTERS to the dead parent → coverage-repair register (joins Cook re-key + R.W. flip).
Anchor-cleanup register +21 (now ~32; the NUM-03 mid-line class, S9-owned). Hicks URL
111831-vs-111834 → S9 confirm. TEACH-02c leaks 41→37 + slip 60→59 (died with parent, no
conversion owed — Chatrie current-term). GATES: run_all 7913→7850 (HIGH 4755, -47 zero-new),
LINT-15/16 0/0 x7, LINT-17 0 (re-verified post-revert), LINT-19/20/24/25 0, survey 88 pages
em 3047, build 723/2806, Case Index 620 idempotent. SCOREBOARD: cats 2/3/4/5 COMPLETE — 37
doctrine units born draft + 3 S7-minted cases; HIGH -455 since S7 open. NEXT: cat-6 Warrant
Exceptions in sub-batches (6a searching-a-person SIA family; 6b searching-a-vehicle; 6c
home-entry w/ D5 caretaking + Emergency Aid + exigent splits; 6d consent/programmatic/
effects).

**BATCH 11 CLOSED — CAT-6a SIA FAMILY (2026-07-08):** parent SPLIT across two sub-umbrellas,
DISSOLVED (2nd-worst em-dash page cleared, -147): SIA Persons (A, deck-stem successor
ADJUDICATED child-model — 57-card whole-family deck + all parent aliases, LINT-24/25 0) +
SIA Cell Phones (A, Riley keeps signed primary) + SIA Alcohol Tests (B, Birchfield +
Schmerber/McNeely line) + SIA Vehicles (A). **R5 CALIBRATION ANCHOR HELD:** Belton→Gant
point-status renders EXACTLY per the S3 R5 worked binding — SIA-Vehicles carries the
superseding table (auto-compartment SUPERSEDED / scope-containers GOOD) + reconciling prose,
Belton composite stays caution/varies, LINT-21 binding green. MCP-live mode 15 calls 0 REST
(Robinson 235, Chimel 763, Gant 351, Thornton 623-24, Riley 403/387, Birchfield 474
confirmed). IDENTITY CATCHES #5/#6 → S2 register: Riley case-page opinion_id 8386852 = 184-char
DOCKET-ORDER STUB (true merits 2680439); Thornton frontmatter carries GANT's cluster 145887 +
its own cluster-as-opinion-id (true lead 9434613) — the cluster-vs-opinion trap live again.
Inventory strand PARKED on Special Needs (A7(2) source, avoids stub-primaries; cat-6b
reconciles the 5 stale Primary-home cells + extracts vehicle-inventory). 34 re-homes
two-sided; owed rows 3: Trupiano/Perez discharged + Bell rule-G (jail-intake = Special Needs
scope). Coverage-repair register grows: authored-ledger home_rows naming dead parents
(assembler-owned, not hand-edited) + Trupiano page-vs-brief-mention dedup (S6-owned).
Anchor register +4 (~36). GATES: run_all 7850→7781 (HIGH 4705, -50 zero-new), LINT-15/16 0/0
x4, LINT-17 0, LINT-19/20/21/24/25 clean, survey 87 pages em 2953, build 722/2809, Case
Index 620. CONSOLIDATED S2/COVERAGE REPAIR LANE now clearly warranted pre-close (register:
R.W. flip · Cook re-key · pointer triple · dead-parent home_rows · Riley/Thornton ids ·
Trupiano dedup · Hicks URL · Maez treatment · anchor class). NEXT: cat-6c home-entry (D5
batch): Community Caretaking A w/ D5 persons-seizure section + point node · Emergency Aid A
· Exigent splits (Hot Pursuit retained parent A + Destruction child A, Santana/Lange R13
point-status) · Protective Sweeps & Securing B (Buie unit) · Fire-Scene C.

**BATCH 12 CLOSED — CAT-6c HOME ENTRY & SEARCH (2026-07-08):** the last big interview payload:
**D5 REALIZED** — Community Caretaking (A born-again) shaped vehicles → "Seizing people for
non-investigative purposes (public)" + NEW NODE seizure.person.noninvestigative-caretaking
(2nd/2 interview-owed nodes; LINT-20 green) → home tombstone (→Emergency Aid); unsettled
taught as unsettled (Garner 10th 3-part · Rideau 5th en banc · Graham-v-Barnette 8th PAGED ·
ALITO OPEN FLAG MCP-VERIFIED verbatim from the Caniglia concurrence, T3 paraphrased);
welfare-check aliases live. **MORGAN FAIL-CLOSED:** lake record = not_found + year mismatch
(2018 vs spec's 2023) → NOT NAMED, routed to S2 identity lane (L1/L2 precedent); D5
function-cabining carried by verified Graham-v-Barnette meanwhile. **R13 EXEMPLAR AUTHORED:**
Santana/Lange point-status table on Hot Pursuit exactly per signed §11 (doorway ✓ · felony ✓
w/ reservation noted 594 U.S. 303-04 · broad reading LIMITED 313) + reconciling prose +
Bandiero hot/fresh-pursuit mnemonic woven register-verbatim (LINT-8 0); felony reservation →
COH-27 poll. Exigent SPLIT: Hot Pursuit (A retained) + Destruction of Evidence (A child,
King/Schmerber/McNeely/Mitchell/Cupp strand moved once). R5 SWEEP cleared the two biggest
slip loads (EA 8 + Exigent 7): **KING UPGRADED slip→T1 BOUND 462** (star *462 verified op
9441559 — also IDENTITY CATCH #7: case-page opinion_id=cluster_id 216733, true lead 9441559,
the cluster-vs-opinion trap AGAIN); Caniglia/Lange/Graham/Newman/August/Gaetjens T3;
Case-v-Montana T4 retained. Protective Sweeps & Securing (B authored at Buie-unit depth,
T2#33) + Fire-Scene (C). DETENTION-FAMILY PRIMARIES FLIPPED to the batch-10 Detention page
(taxonomy-grounded: warrant.detention-at-scene owns Summers/Muehler/Bailey/Rettele/Ybarra;
Securing keeps Buie/McArthur/Segura) — batch-10 deferral ratified. Owed rows 5/5 incl.
GAETJENS CATCH (O1 page never satisfied its ledger row — discharged as honest LCD). R3 flips:
4 O1-era illegitimate verified → draft. Rule-B: 21 broken deep-links to NUM-03 mid-line
anchors stripped (linter-parsed, working anchors preserved, 1 over-strip artifact caught +
repaired). GATES: run_all 7781→7621 (HIGH 4556, -149 zero-new), LINT-15/16 0/0 x6, LINT-17
0, LINT-20/24/25 0, survey em 2657 (-296 R11 delivered) slip 42, build 722/2820, Case Index
620. REGISTER GROWS: Morgan identity · King re-key · Gaetjens enrich. NEXT: cat-6b
programmatic family (Special Needs B parent + Inventory B + Checkpoints B extractions +
Border B re-parent + the 5 stale SIA cells).

**BATCH 13 CLOSED — CAT-6b PROGRAMMATIC & VEHICLE-ADMIN (2026-07-08):** the MEGA-PAGE CURE
delivered: Special Needs (B born-again, 41-case load accounted ZERO-DROP row-by-row) splits
out Inventory Searches (B: Opperman/Bertine/Wells/Lafayette + Evans/Braxton LCD) +
Checkpoints & Roadblocks (B: Sitz ✓ / Edmond ✗ / Lidster + Prouse/Martinez-Fuerte co-homes);
Border (B born-again re-parent): worst-leak page CLEARED 6→0 — ALL formerly-"(No standalone)"
device-split cases now PAGED → WIKILINKED (TEACH-02c upgrade beyond the R8 name-plainly
fallback, ADJUDICATED ACCEPTED); slip 4→0 (Cotterman/Cano T3 paraphrase-downgrades, G3/G4
fail-closed lake-only; T1 star upgrade available at S9 maintenance); em 37.2→10.5/1k.
BOOKING-INVENTORY LINE ADJUDICATED BY DOCTRINE: Lafayette → Inventory (same
standardized-criteria rule); Florence + Bell STAY Special Needs (Bell-v-Wolfish institutional
balancing ≠ property catalog; consistent w/ batch-11 rule-G). Batch-11-owed reconcile: 5
stale SIA primary cells resolved, zero stale refs remain. Mode = lake-grounded 0 CL calls
(batch-10 precedent); anchors re-verified at bound pins. Rule-B anchor repair: 5 broken
deep-links → plain wikilinks + prose pins (LINT-5 HIGH 83→77). Registry: inventory statement
filled + 2 also_on cleanups, 0 new nodes. ORCHESTRATOR NORMALIZATION: worker wrote
baseline/after survey side-files, canonical s7-survey.json left stale → regenerated canonical,
side-files removed (one-artifact convention; git history is the record). Residue → registers:
Riley opinion_url divergence (extends catch #5), Frank/Bell/Wyman + device-split field_i
unverified (S2/S9 treatment verification), Braxton doctrinal home ratified. GATES: run_all
7621→7532 (HIGH 4485, -71 zero-new), LINT-15/16 0/0 x4, LINT-17 0, LINT-19 4 pre-existing
ER-only, LINT-20/24/25 0, survey 87pp em 2470 (12.3/1k) slip 38 leaks 28, build 722/2823,
Case Index idempotent. CAT-6 REMAINING: 6d (Consent A w/ Matlock+3-prongs fixes · Automobile
A · Effects & Containers B) — then cat-6 COMPLETE.

**BATCH 14 CLOSED — CAT-6d (2026-07-08) — CATEGORY 6 COMPLETE:** Consent (A born-again, em
29.4→3.3/1k, worst-remaining page cleared: 3-prong test up front [Schneckloth/Matlock-
Rodriguez/Jimeno] + Osage destruction scope-pitfall in Brief AND pitfalls; Matlock
table-entry fix VERIFIED-HELD; Phase-1b compound-label residue RESOLVED via 3-col schema
migration; title/hook reconciled: title=H1=filename canonical, "Consent" hook preserved as
alias + router display) + Automobile (A born-again, em 29.9→2.6/1k, slip 1→0 Collins T3,
Carroll→Chambers→Ross→Acevedo→Labron/Dyson→Collins spine) + Effects & Containers (B authored
from 33-word stub: container-unification story, Chadwick luggage-vs-car anchor).
CONTAINER-FAMILY ADJUDICATED by exposition-ownership principle: Chadwick primary→Effects
(caution/varies IS the Effects charter, R13 prose), Acevedo/Ross Key on BOTH (vehicle-scope
vs unification, intentional multi-home), Sanders/Robbins stay Automobile (owed rows
discharged there zero-drop). STYLE MIGRATION RATIFIED: both O1-legacy 5-col Key tables →
current 3-col schema + plain wikilinks (resolves LINT-4, LINT-9 0). R5: Collins/Camou/
Morley/Lewis/Carlton-Williams T3 paraphrases (no fabricated pins, unverified-lake honored).
Mode lake-grounded 0 CL. Owed rows 5/5. TEACH-02c 5→0 w/ wikilink upgrade. GATES: run_all
7532→7434 (HIGH 4394, -91; sole increase = 1 LINT-7 J′-exempt page-title FP), LINT-15/16
0/0 x3, LINT-17 0, LINT-4 resolved, LINT-20/25 0, survey em 11.1/1k slip 37 leaks 23, build
722/2826, Case Index 620 (3 rows). Residue → S9: Chadwick index-glyph good-vs-caution
mapping, Frazier/Riley/Anchondo under_review status class. SCOREBOARD: CATS 2-6 COMPLETE =
55 doctrine units born draft + 3 S7-minted cases; HIGH since S7 open -546. NEXT: cat-7 ER
family (A4 severance: ER index [the pre-existing LINT-19 4-HIGH holder] → Fruits &
Attenuation A + Good-Faith A + Inevitable Discovery & Independent Source B; Standing A
born-again w/ TEACH-01 Chatrie relocation; 44 homed cases re-point; the inevitable-discovery
active-pursuit split-block placement lands).

**BATCH 15 CLOSED — CAT-7 ER FAMILY (2026-07-09) — CATEGORY 7 COMPLETE:** the A4 severance
delivered: ER index (mega-page heir, 49 homed cases — precise count vs 44 estimate) → R2
overview (LINT-19 4→0 CURED, the register's last pre-existing holder) + Fruits & Attenuation
(A: Wong Sun/Brown/Strieff + origin Weeks/Wolf/Mapp + impeachment line + DOMINOES mnemonic) +
Good-Faith (A: Leon line + deterrence-boundary Calandra/Janis/Scott + Herring DUAL-HOME
preserving batch-8 Collective-Knowledge Key-on) + Inevitable/Independent (B: Nix/Murray/
Crews + THE OWED SPLIT-BLOCK LANDED — Satterfield ★846 required-side page vs Kennedy ★500 /
Cunningham not-required terminals, MCP-verified). IDENTITY CATCH #8: R8 note's required-side
"Conner (8th)" = the CONSENT Conner (127 F.3d 663, ★666, Securing home) NOT inevitable-
discovery — REFUSED fail-closed, Satterfield carries alone, intended 8th-Cir case → S2
register. Standing born-again (A: TEACH-01 Chatrie OUT of all LCDs w/ digital cross-refs,
slip 4→0 incl. Byrd T3 [CL slip-only, upgradeable], Rakas ★143, App-B Brendlin/Katz
presentation verified, callout+Apply-it added, em 104→10). 49-case arithmetic: 18 Fruits +
17 Good-Faith + 7 Inevitable + 7 retained-on-overview = 49 zero-drop; boundary trio
(Stone/Blue/Caceres) retained on persisting overview ADJUDICATED-ACCEPTED. Worker
self-caught its 3 re-introduced meta-intro leaks at survey regen. Deck: NO successor needed
(index persists; 3 decks resolve, LINT-25 0). Owed rows 12/12 by presence. 7 MCP 0 REST.
GATES: run_all 7434→7269 (HIGH 4242, -152 zero-new), LINT-19 0, LINT-15/16 0/0 x5, LINT-17
0, survey em 9.8/1k slip 31 leaks 16, build 722/2834, Case Index idempotent. SCOREBOARD:
CATS 2-7 COMPLETE = 60 units born draft. NEXT: cat-8 Confessions batch; BIVENS/§242
CONSULTATION surfaced to user in parallel (cat-11 gate).

**USER DECISION — CAT-11 BIVENS/§242 SHAPE (2026-07-09): FULLER BUILD-OUT.** The deferred A5
R6 decision (TAX-02b residual) is RESOLVED by user selection from the three-option
consultation (evidence = the taxonomy sweep + S6 homing data): cat-11 gains TWO new placed
nodes beyond the signed §1983/QI split — (1) "Suing Federal Officers — Bivens & the FTCA"
(Tier B; absorbs Hernandez/Ziglar/Egbert/Fazaga + Brownback/Martin/Konan + Tanzin/Landor —
the honest home for the non-§1983 federal-officer suits) and (2) "Absolute Immunity" (Tier
C/B; Imbler/Buckley/Briscoe/Rehberg functional-approach line). Monell stays within "§1983 &
Municipal Liability". TWO S3 Decision-Log entries owed at the cat-11 batch (the A5-mandated
logging); R6 justifications: distinct black-letter rules w/ their own dockets; depth ≤3
holds (cat-11 → node). CAF tier bump C→B rides the same batch as a logged R2 amendment
(orchestrator call per the R2 machinery, evidence = 8 Keys / 3 sub-doctrines).

**BATCH 16 CLOSED — CAT-8 CONFESSIONS (2026-07-09) — CATEGORY 8 COMPLETE:** 4 born-again
rewrites (no splits): Due-Process Voluntariness (B) · Miranda & Custodial (A, TEACH-04c
"two C's" CUT per SD8 — rephrased as the two unnamed triggers, LINT-8 0, escalation path
stays journaled) · Miranda Waiver & Invocation (A, Seibert/Edwards/Shatzer spine, Bobby v.
Dixon Related→Key self-home fix RATIFIED) · Garrity (B, instructor-critical: the
Kastigar/Uniformed-Sanitation/Lefkowitz/Portash immunity family named via frozen ledger
brief-mention terminals w/ exact canonical captions, 4 owed rows discharged; NASA v. FLRA
kept statutory w/ anti-conflation pitfall). TEACH-04e stale-premise RECONCILED: dispatch's
"1 ff hit" per page was a Phase-0-era artifact already cleared — canonical survey 0, no
conversion owed (CONFIRMED not-missed). Mode lake-grounded 0 CL. Owed rows 5/5 (Chapman
excluded-remit by presence). R3 flips: 4x verified→draft. Rule-B: 5 mid-line deep-links
demoted (-5 LINT-5 HIGH), targets → anchor-cleanup register. Cat-8 em 22.8-28.3 → 2.1-4.7/1k.
GATES: run_all 7269→7204 (HIGH 4169, -73 zero-new; +8 MED = the immunity-family page-less
class), LINT-15/16 0/0 x4, LINT-17 0, LINT-8 0, LINT-20/25 0, survey em 8.5/1k leaks 14,
build 722/2834 byte-stable. SCOREBOARD: CATS 2-8 COMPLETE = 64 units born draft. NEXT:
batch 17 cat-9+10 (6A RtC A + Lineups B new + Eyewitness B + Brady B + Entrapment B); then
cat-1, cat-12/13, cat-11 (NOW UNBLOCKED per user decision), consolidated repair lane, close.

**BATCH 17 CLOSED — CAT-9 + CAT-10 (2026-07-09) — CATEGORIES 9 AND 10 COMPLETE:** 6A Right to
Counsel (A born-again: attachment→offense-specific→Massiah→Montejo-overrules-Jackson spine,
em 35.2→7.2/1k) + Lineups & RtC (B AUTHORED: Wade/Gilbert critical-stage + per-se, Kirby/Ash
limits; counsel-presence/reliability boundary held vs Eyewitness w/ intentional Wade/Gilbert
dual-home per registry) + Eyewitness ID (B: Stovall→Biggers→Manson→Perry; Perry T3 — cache
L.Ed.2d-only, no U.S. pins, refused proportional fabrication) + Brady & Giglio (B:
officer-credibility framing, Kyles prosecution-team duty, Youngblood/Trombetta preserve-duty
companion line added via owed rows; Smith-v-Cain T3) + Entrapment (B: subjective-test spine).
**SELF-CAUGHT FABRICATION (the finest-grain catch of the run):** worker's draft Gilbert quote
"the direct result of the illegal lineup" NOT IN TEXT → replaced w/ the verified per-se
language at ★273; McNeil "serve different interests" carried quote REFUTED → paraphrase. R3
+ G3/G4 working at draft grain. STALE PREMISE CAUGHT AGAIN (Brady 04e — canonical 0, no
conversion owed). Mode lake-grounded 0 CL (cache text pool). Owed rows 5/5 by presence w/
case-level cites (no fabricated pins on under_review shells). TEACH-02c 6→0 across the 5
pages; TEACH-04d Brady inverted 1→0; LINT-16 weight-label catches (Benn/Escobedo/Jackson
cells). Rule-B: 22 broken deep-links → plain links (register +~26). Registry counsel.lineup
statement filled. GATES: run_all 7204→7059 (HIGH 4018, -151 zero-new; +11 MED = Lineups
bibliography class), LINT-15/16 0/0 x5, LINT-17 0, LINT-20/25 0, survey em 7.1/1k slip 27
leaks 8 inverted 3, build 722/2839 (+5 aliases), Case Index byte-idempotent. S9 residue:
S.Ct.-paginated cache pins (Wearry/Turner/Connick/Rothgery/Montejo) flagged for U.S.-pin
confirm; 5 owed cases under_review status class. SCOREBOARD: CATS 2-10 COMPLETE = 69 units
born draft. NEXT: batch 18 cat-1 Foundations (Framework B-hub w/ TEACH-01-worst + 12b hub
migration + :88 multi-circuit label + batch-5-owed private-search demote; 3 C siblings).

**BATCH 18 CLOSED — CAT-1 FOUNDATIONS (2026-07-09) — CATEGORY 1 COMPLETE:** FA Framework
REBUILT AS PURE ROUTER HUB per SD1/§9 (H1 → orienting question → Brief roadmap
[gov-action→threshold→standing→CREW→remedy] → non-case steps table → pitfalls → Visual;
NO callout, NO Key table — the old Key table was pure drift, none of its cases homed here);
FOUR standing debts cleared in one rewrite: TEACH-01-worst (Chatrie bullet OUT → digital
cross-ref), Phase-1c full-skip ("& subsequent treatment" variant heading DEAD, survey RD
1→0), Phase-1b Framework:88 (compound label resolved-by-relocation, LINT-4 3→2),
batch-5-owed private-search demote (Jacobsen/Walter/Verdugo/Wilson/Reddick FA-Framework
homes dropped two-sided, real primaries kept, Case Index 10 rows). Common Law (C: TEACH-04g
Historical-tier language, Riley→Related w/ SIA-Cell-Phones primary, title=canonical +
filename kept) + Analysis Checklist (C, type:practical, checklist IS the body) +
Recalibration (C, Katz→Jones/Carpenter narrative, 04d residue 0). TEACH-12b: rule-skel 6→2
(residual = CREW + Golden Rules, cat-13's). ADAMS QUOTE DOWNGRADED to paraphrase
(least-certain, per batch-17 discipline); Otis/Camden/Boyd quote-pins → S9 G3/G4
(quote_fidelity mismatch flags). ORCHESTRATOR FIX — LINT-15 HUB HOOK: the worker correctly
REFUSED to fake a callout when LINT-15 (built pre-SD1) demanded one on the hub; resolution =
"hub" added to EXEMPT_TYPES (auditable frontmatter classification, NOT the overview:true
hack) + FA Framework type:doctrine→hub; self-test PASS, Framework findings 0, code delta
rides the standing gate. Registry node foundations.fourth-amendment-framework now
semantically orphaned (hub owns no point) → S3 DECISION JOURNALED (re-home to Two
Definitions family or retire; LINT-20 stays green meanwhile). Owed rows 0 (verified all 251
pointers). Mode lake-grounded 0 CL; Riley stub divergence re-confirmed (register);
Lee/Milam/Verdugo-⚪ + Terry court_id:null → S9. GATES: run_all 7059→7001 (HIGH 3984→
stable, -34 zero-new), LINT-15 hub 0 + suite 0/0, LINT-17 0, LINT-4 3→2, survey em 6.5/1k
slip 26 leaks 7 inverted 1 rule-skel 2 RD 0, build 722/2839. SCOREBOARD: CATS 1-10 COMPLETE
(all but 11-13) = 73 units born draft. NEXT: batch 19 cat-12+13 (Reference: Fed Courts C +
Reading & Citing C + State Citations NEW C + Legal Research split C + Verifying Good Law C;
Craft: Golden Rules C + CREW C + Instructor Development C — the last rule-skels die); then
cat-11 FULLER BUILD-OUT batch; repair lane; close.

**BATCH 19 CLOSED — CATS 12+13 (2026-07-09) — CATEGORIES 12 AND 13 COMPLETE:** 8 Tier-C units
(5 reference + 3 craft): Fed Court System · Reading & Citing (state-conventions H2 moved once)
· State Citations AUTHORED (opencase.com landed HONESTLY as national-tool cross-ref w/
hallucination caveat, not blind "state tool" framing — verify-then-apply) · Legal Research
Tools + Verifying Good Law (title hooks → aliases per convention; the LINT-4 :51 banned
phrase resolved — corpus LINT-4 → 1, only the generated index:55 remains for A7(4) regen) ·
Golden Rules + CREW + Instructor Dev. **CREW HYPOTHESIS REFUTED against the signed register**
(S1 R9: C/RE/W three justifications NEVER four, exigency inside RE; the R→RE fix was already
applied — clarifier added, LINT-8 0). LAST RULE-SKELETONS DEAD (survey 2→0) + LAST INVERTED
LABEL DEAD (1→0). Stale premises reconciled x2 (CREW leak, Instr-Dev ff — canonical 0).
Honest-typing: first type:craft pages (pre-existing exempt class, no code change) + 2
reference retypes (one load-bearing vs LINT-15). Integrity note: unverifiable Cornell URL
REMOVED rather than shipped. Owed rows 0; registry clean (no node claims cat-12/13). Mode
lake-grounded 0 CL. GATES: run_all 7001→6936 (HIGH 3934, -50 zero-new strict-decrease),
LINT-15/16 0/0 x8 + self-tests PASS, LINT-17 0, LINT-4 →1, LINT-8 0, survey em 5.5/1k
rule-skel 0 inverted 0, build 722/2845 (+6 aliases). S9 candidate: LINT-2 [!note]-callout FP
class (mirror the [!rule] carve-out). SCOREBOARD: CATS 1-10+12+13 COMPLETE = 81 units born
draft; ONLY CAT-11 REMAINS. NEXT: batch 20 — cat-11 FULLER BUILD-OUT per user decision
(2 new nodes + 2 S3 Decision-Log entries + CAF C→B amendment + the 29-case mega-node
dissolution + officer-created-danger split-block placement + Cruz disposition).

**BATCH 20 CLOSED — CAT-11 FULLER BUILD-OUT (2026-07-09) — ALL 13 CATEGORIES COMPLETE:** the
user decision REALIZED: §1983 mega-node (29 Keys/~8 sub-doctrines) DISSOLVED → §1983 &
Municipal Liability (A, filename kept for URL+deck stability, Monell family + genuine-§1983
remedies stay) + Qualified Immunity (A: Harlow→Anderson→Pearson spine + QI-critique docket
plain-italic + ZORN as the 2026 per-curiam legend case w/ LAW-05 pipeline-legend VERIFIED
STRIPPED) + NEW Suing Federal Officers (B: Bivens/Abbasi/Egbert + FTCA trio + Tanzin/Landor
honest home; em-dash dropped from filename, full title in topic/aliases) + NEW Absolute
Immunity (C: Imbler functional-approach quartet) + Use of Force (A: Graham→Garner→Barnes
spine + OWED officer-created-danger split-block placed — ADJUDICATED SPLIT-BLOCK-NOT-NODE,
Allen-v-Muskogee/Billington NOT NAMED fail-closed [no terminals], Mendez/Barnes carry + BWC
evidence-practice prose no-node per A6) + Retaliatory Arrest (C: Nieves/Gonzalez) + Malicious
Prosecution (C: Thompson/Chiaverini) + CAF (B — the LOGGED R2 AMENDMENT C→B, three titled
strands: Excessive Fines / procedural DP / innocent owner). S3 DECISION-LOG A10 APPENDED
(the A5-mandated TAX-02b logging): liability.federal-officer-suits + liability.absolute-
immunity w/ R6 justifications + user-decision date; registry 2 new nodes + 3 statements
filled, LINT-20 0. THE FIELD-FRAMING CLASS DIED CORPUS-WIDE (last hit converted D2, survey
ff 0). 42-case redistribution row-by-row two-sided (22→QI, 11→Suing, 4→Absolute, 5 force-
mirror drops, 16+family stay); GEO-Group/Fikre adjudicated OUT of cat-11 scope. CRUZ
DISPOSITION (S7-owned): lake = Negron-Cruz frontier stub, no verified proposition →
TERMINAL WATCH fail-closed ("not found ≠ fabricated"); S2 can promote if wanted. Konan/
Landor 2026 at issue-altitude, holdings owed S2 treatment-derivation. Slip 26→12 (cat-11
cleared). Mode lake-grounded 0 CL. GATES: run_all 6936→6833 (HIGH 3782, -152 zero-new;
LINT-5 35→1 the Neville pre-existing), LINT-15/16 0/0 x8, LINT-17 0 (84-case spine
pre-verified), LINT-20/25 0, survey 89 pages em 4.9/1k ff 0, build 724/2873 (+2 pages).
**PHASE 2 COMPLETE: 89 units born draft across all 13 categories + 3 S7-minted case pages.
HIGH 5212→3782 since S7 open (-1430). NEXT: consolidated repair lane (the register), then
S7 close (acceptance greps, dispositions, run brief, S7→S8 handoff).**

**REPAIR LANE CLOSED — phases (b1)+(b2) (2026-07-09):** (b1) TWO SANCTIONED SURFACES built in
ingest.py mirroring --repair-identity-from-cache (fail-closed, journaled, max_calls=0,
self-tests green): --rekey-lead-opinion-from-cache (harmonized lead = head(sub_opinions)
dropping the legacy cluster-id-equal entry ONLY when >1 opinion — the single-self carve-out
discovered via the Riley merits fixture; refused-needs-panel guard on plausible leads) +
--rekey-cluster-panel (explicit target + EXPECT-CITE GUARD — the exact Riley-trap check —
+ evidence pointer journaled). (b2) ORCHESTRATOR TOKEN LEGS RUN: Surface-1 batch 6/6 rekeyed
cache-served (King 216733→9441559 · Thornton 134746→9434613 · Gaetjens None→4703206 · R.W.
None→11312795 [batch-8 flip DISCHARGED] · Konan None→11266325 · Landor None→11346052
[metadata only, holdings stay S9]); Surface-2 Riley PANEL RE-KEY (cluster 8416508→2680439,
cite 572-U.S.-1055→134-S.Ct.-2473, expect-cite guard passed; U.S.-display 573 U.S. 373 =
optional --apply-web-cites follow-up); project.py --write re-projected 7 case pages
(projector owns the courtlistener block). MORGAN RESOLVED on the orchestrator MCP lane:
United States v. Jaron Howard Morgan, 71 F.4th 540 (6th Cir. 2023-06-26, Sutton, J., docket
22-1445), cluster 9409483 / lead 9404959 — I hit the cluster-vs-opinion trap MYSELF (URL id
as opinion id → 0 hits) and resolved via sub_opinions, then confirmed the function-cabining
holding verbatim; disposition artifact S7-RL-DISPOSITIONS.jsonl + 6c-3 loader (header-tolerant)
→ ledger 252 rows PASS; D5 ROSTER COMPLETED: Morgan LCD bullet + Sources on Community
Caretaking (plain-italic, terminal-backed); the not_found morgan-v-fairfield-county record
stays honest (different case). COOK ADJUDICATED HONEST-RESIDUE: proper cure = panel re-key of
the manifest stub, but target cluster 776186 is a CACHE MISS (fail-closed guard held when my
first artifact-edit attempt minted a slug-captioned duplicate — REVERTED); 3-step S2 work
order documented AT SOURCE in the R8-NONPAGE row note; page prose already cites the correct
Donald Cook. GATES: run_all 6829 (HIGH 3781 zero-new), LINT-17 0, LINT-13 0, ledger 252
PASS, ingest self-test PASS, build 724/2873. REGISTER DISPOSITION: repaired 7 ids + Morgan +
Neville + 6 pointers + 8 index dupes; honest residue = Cook 3-step + Maez/Konan/Landor
treatments + optional 8th-Cir hunt (all S9/S2-registered). NEXT: S7 CLOSE.

---

**S7 CLOSED (2026-07-09).** The doctrine-production spec is complete. CLOSE RECORD:
**Acceptance:** 11/11 spec-§7 criteria PASS or PASS-WITH-NOTE, machine-evidenced
(S7-ACCEPTANCE-SWEEP.md); exactly ONE logged tier amendment (CAF C→B) vs the >10 pause guard;
D5 + D7 + Bivens + Absolute-Immunity nodes live w/ filled statements; the corpus defect
classes are DEAD (field-framing 0, rule-skel 0, inverted 0, RD-family 0, missing-H1 0,
reader-facing pipeline vocab 0 on touched pages). **Zero-drop:** 164 home_rows (158 S6-owed
+ 6 S7-mint) + 58+3 non-page placements fully accounted (S7-OWED-ROWS-ACCOUNTING.md w/
dead-parent→successor map); honest residue registered, nothing silent. **Close-blocker
catches (fail-closed working on the orchestrator too):** the close sweep caught MY
repair-lane over-claim — Riley's panel-rekey identity_method missing from the schema enum
(LINT-13 1 HIGH, cured by additive enum extension per the web_legs precedent) + the
un-regenerated Case Index (cured; 612 rows, dedup guard confirmed live). **Code gate:**
S7-coderabbit-66d8f79.md — 11 findings, ALL UPHELD on the merits → ALL FIXED same session
w/ extended self-tests (S7-coderabbit-adjudication.md); one reviewer patch REFINED with
live evidence (the literal fix would have false-flagged stub-excluded-but-real landings);
suites byte-identical post-fix. Worklist snapshot ADJUDICATED: stays committed as the
Phase-0 planning record (ledgers are records; dispositions live in the journal + sweep).
**FINAL GATES:** run_all 6828 (HIGH 3781; from 8372/5212 at S7 open = -1544/-1431), LINT-13
0, LINT-15 0, LINT-17 0 (252-row ledger PASS 151/151/151), LINT-8/20/24/25 0, LINT-16 =
the generated-index schema class (S8-owed flip), build 724/2873, ingest+survey self-tests
PASS, Case Index 612 idempotent. **HANDOFF:** S7-TO-S8-HANDOFF.md delivered (scoreboard ·
delivered · S8 inherits [388 join surface, linking passes, schema-3 flip, transclusion] ·
binding decisions · CONSOLIDATED S9 REGISTER [anchor class ~60+, Field-I promotions,
treatment derivations Maez/Konan/Landor, Cook 3-step, quote-fidelity items, lint
refinements, the born-draft 89-unit corpus for the panel] · lake state 668 records · honest
gaps). **S7 IS CLOSED. NEXT: S8 opens with its own read of the handoff; the S9 panel
inherits the draft corpus. Run brief served.**

---

# S8 — Legal-Term & Case Linking + Glossary (opened 2026-07-09)

**S8 OPEN (2026-07-09).** Orchestrator (Fable) read: S8 spec (signed 2026-07-04) · S7-TO-S8-HANDOFF ·
S7-ACCEPTANCE-SWEEP + OWED-ROWS pointers · RUNBOOK §0–§5 + §4-S8 · EXECUTE wrapper. The 5 normative
mockup commits (981b286/51e1f4b/baa1e17/5b48d85/5d747f9) confirmed ANCESTORS of HEAD — the R10
landing-highlight mechanism + density exhibits are on-branch. **PHASE-0 INVENTORY (fresh, seed-not-gospel;
scratchpad scans, to be re-derived by the real S8 tooling):**
- **Mid-line `^pin-N` defs: 242 across 208 files** (audit seed 299/233 — drift confirmed, S7 rewrites).
  End-of-line pin defs 601 across 423 files (line-level heuristic; R6 tool does block-level).
- **Broken `[[Case#^pin-N]]` deep links: 0** by exact-stem match (spec measured 128 on 2026-07-04;
  consistent with S7 rule-B stripping broken deep-links — handoff §4.2). 239 live pin refs found.
- **Unescaped wikilink pipes in table lines: 32 across 15 files** (audit seed 18/69 → 19/58 → now 32/15).
- **Bare full-caption mentions: 472 distinct lake captions / 523 occurrences** (NUM-04 seed 388 —
  corpus grew 262→724 files since; short-name mentions not yet counted, they ride the R3 resolver).
- **Fragment eligibility (R5):** lake pinpoints 968 total — `quote_fidelity: matched` **184**
  (the operational G3-pass: whitespace-collapsed string match vs cached source, `harvest_pinpoints`
  ingest.py:2500); star-verified 158 / slip-only 810. Cached text pool located:
  `/Users/johngalt/cssi-lake/cache/text` (7,413 opinion texts; `CSSI_LAKE_ROOT` default).
- Coverage ledger loaded: 252 rows, `terminal` enum (authored/brief-mention/excluded-remit/…);
  corpus_mention_baseline 57. Lake 668 records. Term register `scripts/lint/term-register.yml`
  (term-register.v1, 141 lines) — routing columns NOT yet present (R7 extends).
**Execution order (spec §5 + EXECUTE wrapper):** zones (R2) → pin remediation (R6, one mechanical
commit) → case-mention pass (R1–R3, category batches) → split-pincite+fragments (R4–R5) → terms (R7)
→ glossary (R8) → embeds (R9) → pipes (R11) → ledger+lints (R12–R13) → acceptance + CodeRabbit gate +
handoff. Fleet: `o2-opus-xhigh` builds tooling/batches; orchestrator adjudicates + commits (workers
COMMIT NOTHING). Zero CL from S8 lanes (fragment validation = cached text only).

**R2+R6 COMPLETE (2026-07-09).** Lane o2-opus-xhigh built `scripts/s8/zones.py` (frozen API:
compute_zones/mask/is_exempt/iter_blocks; 9 zone kinds; fixtures + self-test PASS) and
`scripts/s8/remediate_pins.py` (block-level; dry-run/--write/--verify/--self-test). **298 mid-block
pin defs found (block-level truth; the line-level 242 undercounted multi-pin blocks) → 297
split-para edits across 232 files + 1 fail-closed queue row.** Orchestrator verification
(writer≠checker): re-ran both self-tests PASS; independent non-whitespace byte-equality proof vs
HEAD — 232 files, 0 mismatches; --verify PASS (271/271 pin refs resolve, count unchanged; the 396
seed was pre-S7-rule-B, seed-not-gospel). Queue disposition: Steele `^pin-503b` mid-sentence pin —
orchestrator moved the anchor to end-of-block (spec R6 sanctioned branch), LINT-9 HIGH 1→0.
GATES: run_all TOTAL 6370 / HIGH **3315** (S7 close: 6828/3781 — the splits cured 466 LINT-10
block-density HIGHs as a side effect; zero-new-HIGH holds), LINT-9 0, build 724/2873 green.
Artifacts: S8-PIN-REMEDIATION.jsonl (297 rows), S8-PIN-REVIEW-QUEUE.md (dispositioned EMPTY).
R6 acceptance state: mid-line pins 0 · broken pin anchors 0 · pre-existing refs intact. NEXT:
R1/R3 mention pass (workorder staged).

**R4 PINCITES COMPLETE + R6-baseline adjudication (2026-07-09).** Doctrine write: 564 edits/72
files (r1 181 [27 frag + 154 plain-external, tier-3 never fragmented] · r2 16 frag + 16 name-half
`#^pin-N` upgrades [incl the Jones "legitimately on premises" short-match — distinctive standing
phrase, uniquely resolving; ALL 16 → S9 register for sample review] · r3 351 plain-external).
Strip-verified 72/72, idempotent, build green. Lane self-caught + fixed a ledger-wipe bug
(no-op re-run blanked scope rows; _emit now preserves). Ledger 964 rows all {lane,model,scope}.
**remediate_pins --verify check (3) now reads 287 refs vs 271 baseline — ADJUDICATED NOT-A-DEFECT:**
the baseline was the R6-epoch "remediation adds no refs" invariant; the 16 r2 upgrades legitimately
add refs. Load-bearing check (2) = 287/287 resolve, 0 unresolved. Steady-state guard moves to the
R13 LINT-5 broken-anchor=HIGH rewrite. Corpus pincite state: 182 case-page + 548 doctrine external
CL links (225 fragment-deep total), 16 deep upgrades, zero live CL.

**Record correction (d4c87b4):** the commit-time build invocation raced the still-running :8080
dev server (ENOTEMPTY on public/seizures) and the pipe masked the exit code — the "build green"
claim in d4c87b4's message was premature at commit time. Server killed; clean rebuild verified:
724 in / 2873 emitted, exit 0. Content state unaffected (public/ is gitignored; the race was
emit-side only). Honest-record note per reporting discipline.

---

**S8 CLOSED (2026-07-09).** The linking/glossary spec is complete. CLOSE RECORD:
**Acceptance:** 9/9 spec-§7 criteria PASS machine-evidenced (S8-ACCEPTANCE-SWEEP.md; R10
PASS-WITH-NOTE — tint machine-verified both paths, centering re-sampled at S9 R15 foregrounded
dogfood). **The web is wired:** 6,058 case-mention links (0 bare page-backed captions), 2,429
term links + 42-anchor glossary, 730 external pincites (225 fragment-deep, validated vs cached
text, zero live CL), 287/287 pin deep-links resolve, 4 embeds (adjudicated boundary now LINT-29
law), COH-15 join CLEAN A/B/C/D=0 w/ E-empty-universe fail-closed guard (NUM-04 re-derived 644 vs
388 seed). **Judgment surfaces for S9:** 187 adjudicated resolutions (100% review mandatory),
16 r2 deep upgrades, 49-caption coverage inbox, sanctioned-quote class (123), LINT-7 carve-out
question (30). **CodeRabbit gate:** S8-coderabbit-f244451.md (base 4c47b72 after payload-too-large
vs main; self-resolved per pause-#8 discipline) — 23 findings: 22 UPHELD→FIXED same session w/
extended self-tests (2 criticals: dry-run ledger clobber + --limit ledger leak, both in
link_pincites _emit path) + 1 REFUTED w/ live evidence (parenthetical-caption exhibit convention);
S8-coderabbit-adjudication.md. **FINAL GATES:** run_all 4176 / HIGH 3381 zero-new (new kit;
composition attributed: LINT-10 3171 S6-backlog · LINT-7 49 · LINT-12 160 · LINT-4 1), join clean
exit 0, build 724/2873 exit 0, self-tests 11/11. **Commit-hygiene notes:** d4c87b4 swept the
mentions lane's 42 links w/ the R11 sweep (concurrent tree); its build claim corrected a60dd12.
**HANDOFF:** S8-TO-S9-HANDOFF.md delivered. S8 IS CLOSED. NEXT: S9 verification (wave 4) —
the panel inherits the born-draft corpus + the S8 register.

---

# S9 — Verification Pipeline & Release Gate (opened 2026-07-09)

**S9 OPEN (2026-07-09).** Orchestrator (Fable) read: S9 spec in full (R1–R15, method P0–P6,
acceptance, decision log) · S8-TO-S9-HANDOFF · LEDGER-SCHEMA pointer. **Codex lane health probe
PASS** (codex-cli 0.142.4; `codex exec -s read-only` returned LANE-OK — the 2-Codex panel lanes,
case-grain Thread-N reads, and dual-model discovery are GO; pause-#8 not triggered). S8 close
brief served (2026-07-09-cssi-s8-close.html). **P0 LAUNCHED** — three parallel build lanes per
S9-P0-WORKORDERS.md: P0-A assertion inventory (R2, `_run/s9/assertion-inventory.json`) · P0-B
Thread-P freeze (R5, deterministic extraction + sha256, frozen BEFORE any Thread-N manifest) ·
P0-C lint roster codification (R8: S3-set renumber →18–25, S4→26, LINT-3 rebuilt lake-driven
w/ committed acceptance fixture, TEACH-11 target checks, LINT-30 = the R4 invariant script
validated against F-DEMO-001). O1's `_run/` S9 artifacts preserved as historical; O2-S9 lives
under `_run/s9/`. Next after P0 review+commit: P1 fan-out (panel review + Thread-N blind reads,
Codex case-grain / Claude doctrine-grain; manifests journaled; Claude serial lane starts the
≥1-in-10 identity slice + COH-27 pending-marker polls).

**P0 COMPLETE (2026-07-09).** Three lanes returned, orchestrator-reviewed:
- **P0-A inventory:** 24,619 assertions / 9 classes, deterministic ids (byte-identical rebuild
  proof; body_sha256 1d8dfe69…), cross-ties reconcile exactly (968 pinpoints, 14,184 mention rows,
  252 coverage rows, 80 registry nodes, 42 glossary). Honest residuals → currency sweep: 35
  unselected-official-cite pages (71 lake records), 5 cite-less 2022–26 cases; 3 holding-less
  SACO mints; 2 no-CL English cases.
- **P0-B Thread-P FROZEN:** 724 items (609 case/115 doctrine), hash 8e51d0c8… (header+sidecar),
  idempotent, 779/779 homes resolved, no-regression floor = 724. R5 ordering law: NO Thread-N
  manifest before this freeze — freeze commits now.
- **P0-C roster:** renumbering already-in-place (no correction); LINT-3 REBUILT lake-driven
  (N5 section-scoped; acceptance fixture passes; +2 TRUE N5 HIGHs at Arrest and Arrest
  Warrants:53/54; +72 A9 case-wall HIGHs = genuine TEACH-07 content-remediation class);
  LINT-8+TEACH-11 target/wording checks (corpus 0); LINT-30 invariant script validates
  F-DEMO-001 clean + fail-fixture fires all 5 invariants; run_all TOTAL 4250 / HIGH 3455
  (+74, all attributed to the LINT-3 rebuild — real findings, not FPs).
**ORCHESTRATOR ADJUDICATIONS:** (1) A9 72 → R4-machine content findings at P3; (2) N5
defect-scoped reading RATIFIED (2 fires vs 110 literal — F-DEMO-001 precedent); (3) LINT-15/16
stay standalone (batch-1 rule C) but must be green at R13 — and the **Case Index schema-3 flip
is ORPHANED work** (S7 handoff assigned S8; signed S8 spec never included it; S9 absorbs it as
a mechanical generator+regen fix in P3, clearing the LINT-16 621-HIGH class); (4) LINT-11
(TEACH-02b pipeline-vocab) = missing script, S9 R8 build item, next lane batch.
NEXT: commit P0 → P1 fan-out (panel + Thread-N; manifests; Claude serial identity slice +
COH-27 marker polls).

**⚠ LANE OUTAGE — pause #8 elevation (2026-07-09).** The claude.ai CourtListener MCP token is
HARD-EXPIRED (first call 3× unauthorized + explicit "requires re-authorization (token expired)").
Interactive re-auth = user-only; per the register the CL-dependent workflow HALTS and elevates;
independent work continues. **Halted:** the COH-17 identity slice — checkpointed resumable at
index 0 (`_run/s9/identity-slice-sample.json`, 74 deterministic rows incl the 7-record risk set;
`identity-slice.jsonl` header STOPPED_AUTH_FAILURE). The COH-27 marker poll COMPLETED before
expiry (12/12 UNCHANGED, 18 calls; caveat: CL cannot evidence cert denials — P4 web sweep
supplements). **Pre-flight finding (offline, no CL needed) → R4 machine:**
`illinois-v-fisher--5141053.json` carries identity.case_name "In re Mirsky" (DC bar matter) under
input "Illinois v. Fisher" — reason_code caption_mismatch_accepted_by_docket_number, status
verified_identity: a builder acceptance of the WRONG CASE on a docket-number coincidence. Push
notification fired. Continuing: P1-H harness+pilot (Codex lanes healthy), all cache-fed work.

**COH-17 IDENTITY SLICE COMPLETE (2026-07-09, post-re-auth).** 74/74 live-checked (77 calls,
paced, 3 transient retries): **72 MATCH / 2 MISMATCH / 0 UNREACHABLE.** The ≥1-in-10 requirement
(662 keyed records → 67 sampled + 7 risk) is SATISFIED with verdicts recorded
(`_run/s9/identity-slice.jsonl`). **Risk set 7/7 CONFIRMED** — Riley 2680439 merits cluster,
King lead 9441559, Thornton lead 9434613, Carpenter, Md. v. King, Rideau, Morgan special row:
every S7 repair-lane re-key HOLDS live. **Findings → R4 machine:**
(1) `illinois-v-fisher--5141053` WRONG-CASE — live cluster = In re Mirsky (DC bar discipline,
2004-10-21); record identity internally consistent with the WRONG case; builder acceptance via
caption_mismatch_accepted_by_docket_number; cure = S2-surface re-key to the real Illinois v.
Fisher (540 U.S. 544, per curiam 2004-02-23, docket 03-374) at P2/P3 adjudication (record is a
verified_identity frontier shell — page blast radius to be assessed).
(2) `Lewis v. United States (1966)` — lake-internal year (1966) vs date_decided 1967-01-09
(live-confirmed); minor derivation defect. The lane also self-caught a checkpointing slip
(Barrett row) via its coverage assert — restored, 74/74 accounted.

**MIS-KEY SWEEP (mechanical, offline).** 208 raw suspects → 198 = the known under_review
no-lead mint class (expected, awaits S9 promotion — NOT mis-keys); true suspects 10: the 7
S7-re-keyed records lack pool text under their NEW lead ids (re-key without text re-fetch —
coherent class, identity itself live-confirmed), both Davis records are stubs (88B/154B),
Flippo = likely regex FP. Riley nuance: lead text is 82KB (pilot read it) vs doctrine lanes'
motions-order claim — P2 reconciles. S2 builder work order staged
(S9-S2-CACHE-REPAIR-WORKORDER.md, ~15 REST calls). Findings 6 filed, LINT-30 holding open.

**Doctrine-N D-3/D-8 in (8/10 lanes).** D-8's Carman cluster-collision claim REFUTED by direct
record evidence: survivor Carroll v. Carman = cluster 2750102, folded-alias carman-v-carroll =
8693292 — distinct clusters, the alias design working; dismissed with evidence, not filed
(R4 inv-4 FP-log discipline). D-8 P2 items: Barnes v. Felix (2025) resolved moment-of-threat —
verify the UoF page reflects it; retaliatory-arrest anchors (Nieves line) reported absent from
lake — reconcile vs page/ledger state at P2. D-3: Riley motions-order claim now from a THIRD
lane (vs the 82KB pool file — P2 must read the file head and settle it); Chatrie lead text
missing (already in cache-repair order); LaDuke + chatrie-4th fabrication_suspected stubs noted.

**CACHE/IDENTITY REPAIR ARC (2026-07-09, spanning builder leg + caption lane + lead backfill).**
Builder-token leg (SANCTIONED, 18 paced REST calls via ingest.py's own client, journaled
consumer=S2-BUILDER-AUTHORING): 3 targets staged, 3 guarded panel-rekeys landed (Davis-1994
117863/9433017 · Davis-2011 218926/9441776 · Fisher 131160/9434538), 18/18 pool texts fetched +
content-head verified. Lead backfill (cache-fed, 8 records incl Wyman 9424375). NEW SANCTIONED
SURFACE --repair-caption-from-cache (Fisher-class complement of the caption-preserving Riley-class
contract; self-tests both guards) → Fisher caption cured loop-2. project.py --write: 169 pages
(9 substantive). Fragments 182→183 (Thornton pin-622 RECOVERED — the S8 fail-closed row cured).
run_all delta +246 fully attributed (=+397 LINT-11 online −160 LINT-12 cured +9 LINT-30 state).
**LINT-30 vs the orchestrator:** inv-3 fired on my self-adjudications — check scoped to spec text
(D-TOOL exempt; legal self-adjudication clears only w/ independent confirmation vote, R14.2) +
flat-fix-row shape accepted (production shape; demo loops[] still honored); self-tests green.
DN-002 fix row booked. IN FLIGHT: DN-004 independent confirmation vote + IDS-002 six-date
web-evidence fix (diagnosis INVERTED at adjudication: date_decided carries CL date_filed
artifacts — rehearing/argument dates; year is reporter-correct). LINT-11's 397 HIGH = new
backlog class for P3 adjudication-first (FP-rate unknown).

**VOTE-SEMANTICS RULING + NORMALIZATION (2026-07-09, mid-grind).** The panel machine emitted
vote rows carrying per-ASSERTION verdicts while the checker + signed demo read vote verdicts as
about THE FINDING — inverse semantics on findings. RULING: vote.verdict refers to the FINDING
(canonical per check_ledger inv-2 + F-DEMO-001). build_vote_row now maps assertion→finding
(refuted→stands, stands→refuted); cutover recorded (vote-semantics-cutover.json); 32 pre-cutover
panel rows normalized in place w/ provenance stamps; grind picks the fix up per-invocation
(fresh import each lane). Panel self-test PASS post-patch. ADJUDICATIONS: 4 pilot findings
DISMISSED (disclosure-induced FPs — Opus verbatim-proved every quote once the ratified
text-promotion disclosed the opinions); geofence-threshold refusal DISMISSED w/ pool evidence
(SCOTUS Chatrie 2026 verbatim holds acquisition IS a search; 11349205.txt) — the callout's
≥2-approvals promotion restored via evidence-cited adjudication. Registry shard-1: 26 approved
+ 1 adjudication-restored = 27/27.

**FLEET PAUSE #9 (2026-07-10 18:35).** Codex usage window closed again (403 wss, pause-#8
surface) after ~1h50m of combined conc-18 grinding — same signature as the overnight collapse
(23:13→~03:12). Both drivers KILLED cleanly at checkpoint: panel 3690 cumulative ok (of 2714
lanes incl re-dispatches; ledger-truth recomputed at relaunch), thread-N sweep mid-pass
(1070/1218 pairs done, 148 to run incl 4 permanent Entick/Wilkes off-CL placeholders).
Probe loop armed (15-min cadence, cheap PROBE-OK exec); fleets relaunch on window-open.
Thread-N unblock arc completed earlier this session: 187 sanctioned lead writes, 154 worklist
rows cured, re-reads REAL (verified). Stub-text triage filed to P2 queue (chapman-v-california
likely mis-key; Demesme concurrence gap; O'Brien correct-as-is).

**RESUME 2026-07-11 00:16 (orchestrator re-seat, procedures re-read).** Re-grounded on
S9 spec + EXECUTE.wrapper + RUNBOOK §3 (CL protocol) before acting. Operating model confirmed:
thin orchestrator (ledger/specs/statuses only), all substantive work in fresh sub-agents,
find→adjudicate→fix HARD-SEPARATED (reviewers never edit; legal verdicts cite CL via single
serial lane L4; loop cap 3 -> _review-needed/), checkpoint every sub-phase.
POSITION FIX: P1 panel review 1230/2714 lanes done (1488 residual); P1b thread-N 1070/1218
pairs (148 to run incl 4 permanent Entick/Wilkes off-CL placeholders). Codex window REOPENED
after ~5.5h rest (PROBE-OK 00:14). ROOT-CAUSE POSTURE on pause-8/9: 403-after-~1h50m-at-conc-18
+ ~5h recovery = ChatGPT-codex ROLLING USAGE CAP, not a per-minute 429. OPERATING DECISION:
never re-run the combined-conc-18 config that burned twice. Sequence = thread-N finishes SOLO
(conc-6, running pid 93042) -> then panel SOLO conc-12 (steady-state 12 < 18 burn peak).
Multi-window grind accepted: pause clean on 403 cascade, resume on probe-detected reopen,
drain across windows. Reconciler (P2) runs the moment thread-N drains, in parallel with panel.

**P2 SR-5 RECONCILIATION LANE FULLY CLOSED (2026-07-11 ~01:55).** Sequence this session:
thread-N drained (Lyle A/B escalated) -> reconcile re-run VALIDATED the leg-C unblock arc
(UNREADABLE 200->3, STRONG 298->460 +162 double-verified, JOIN-MISS 1->0, floor 724/724) ->
112 discordant-candidates all adjudicated from cached evidence (0 CL calls): 111 benign
(76 caption-variance + 16 correctly-keyed incl cluster-collision watch Lange/Gant/Fernandez,
Lange spot-checked live-from-cache + 6 no-printed-caption + 10 N-blind-unread + 4 already-resolved)
-> P2-DISCORDANCE-DISPOSITIONS.jsonl (reconcile-free R5); 1 genuine mis-key F-S9-P2-CHAPMANCAL
UPHELD+FIXED (chapman-v-california re-keyed 2016-cert-denial cluster 8428427 -> merits 386 U.S. 18
cluster 107359/lead 9423348; 1 sanctioned prime CL call + cache-only rekey; no re-projection).
Commits 9ce5cfba/60a34ffe/b94aecd6. Role-sep held: finders=codex-thread-N, evidence-prep=opus,
adjudicator=fable, fixer=opus, re-review=fable — all distinct lanes.
NEXT PHASE: panel P1 review still grinding (clean 246/0 @ conc-12 solo, ~246/1488 this window;
multi-window expected). Once P1 drains -> P2 panel-findings adjudication (~1335 findings, the big
remaining load; check_ledger inv2/inv5 are its end-of-run gates, firing benign mid-grind now).

**SESSION CHECKPOINT 2026-07-11 ~08:55 (codex P1 DONE; opus 26%; opus quota-paused).**
Full-session arc: re-seated as orchestrator -> read procedures (S9 spec/EXECUTE wrapper/RUNBOOK §3)
-> thread-N drained (Lyle escalated) -> reconcile validated leg-C unblock arc (UNREADABLE 200->3,
STRONG 298->460, floor 724/724) -> all 112 P2 discordances adjudicated (111 benign + chapman-v-california
mis-key UPHELD+FIXED, full re-key to 386 U.S. 18 cluster 107359) -> DISCOVERED the panel N-of-3 is
2 codex + 1 OPUS lens and the Opus lens was 4/1357 (owed) -> built+validated emit_opus_pack.py (opus
emission harness, deterministic merge onto codex finding-ids, idempotent, latent fail-open bug fixed)
-> drove 9 opus reviewer waves (359/1357 groups, 298 findings full-3-vote, 0 emit errors) -> codex
2-lens resumed on window-reopen (07:04) and COMPLETED all 1357 groups (08:53, 0-residual).
CONSTRAINTS learned: codex window = ChatGPT rolling cap (~5.5h recovery, burns at conc-18/~1h50m;
conc-12 solo lasts ~3h); Claude account has its OWN session/usage limit (opus reviewers at 10/wave
exhausted it @ wave-9). RESUME PLAN: opus lane at ~5 reviewers/wave when Claude quota resets; ~998
groups remain (all now codex-complete). THEN: P2 panel-findings adjudication (~1884 findings, the big
remaining judgment work — 5 mechanical defect classes cataloged for class-wide P3 fixes), P3 fix,
P4 sweeps (Mermaid/lint/coherence/glossary/Case-Index), P5 release gate, P6 publish-brief.
Commits this session: 9ce5cfba 60a34ffe b94aecd6 a9fde5d3 b3e0e2aa 2c5b7742 e30723d9 b90939e6
5e2ca828 cdb2a57e 5ecac82d 2d278937 089bbee7 (+ restart commits).

**OPUS 3RD-LENS COMPLETE 1357/1357 (2026-07-19 ~07:15) — PROMO-SPRINT ARC.** Resumed from the
weekly-quota pause (wave-32/823 groups) on 2026-07-18 ~05:50 after user-directed pacing analysis.
Arc: bursts of 4 waves per 5h cron (waves 33-48, +50% promo headroom confirmed via usage meter
24%/19%/3%), then user-directed acceleration (2026-07-19 ~05:30) to continuous 10-wide rounds
(waves 49-66). Totals: waves 33-66, ~172 packs, 535 groups, ~5,600 assertions reviewed by fresh
o2-opus-xhigh reviewers; 0 no_review, 0 unroutable after the wave-33 group_id normalization fix
(reviewers echoed annotated GROUP headers; prompt fixed + mechanical normalizer added). Doctrine
tail (77 pages) packed 1-2/pack with size guard; 928KB Miranda mega-page reviewed clean on
1M-context, no truncation. Comma-named (Lo-Ji) and parenthetical-named (Carpenter remand,
Robinson en banc) and non-.md (points registry.yaml#shard) group_ids all routed clean.
DEFECT HARVEST (new-to-panel, P2/P3 classes): home_role mirror class ~15 cases across 3 families
(Fruits&Attenuation↔ExclusionaryRule: Wolf/Mapp/Walder/James inapt + Silverthorne/Nardone/WongSun/
Weeks/NYvHarris/Strieff/Kaupp/Taylor mirror-only; QI↔S1983: Hanlon/Hope/Wright/Graham/Harlow/
Pearson/White/WilsonLayne/Malley/Messerschmidt; GoodFaith↔ExclusionaryRule: LopezMendoza/Scott/
Calandra inapt + Krull/Leon/DeFillippo/Mathis/Leary/Sheppard mirror); exigency Key-Anchor
self-conflict 4 cases (King/Schmerber/McNeely/Mitchell — Destruction-of-Evidence vs
Exigent-Circumstances); high-severity holding errors: Mitcham (independent-source vs inevitable-
discovery), Perez (Chadwick+Gant misnamed as Gant+Riley), Loera (affirmance-basis misstated),
Trent (unpublished-6thCir labeled binding); Fla-L-Weekly cite-selector class re-confirmed
(Rothgery/McNeely/Safford/Salinas/Soldal/Hiibel/Plumhoff/Wearry/White/FloresMontano/Tarantino);
anachronistic L.Ed.2d parallel dupes x5 (Wolf/Johnson/Walder/Rochin/Trupiano); truncated-holding
class ~15; date_decided-uses-rehearing-date class ~8; alternate-cluster opinion links ~10
(Jardines/Dickerson/Barnes/al-Kidd/Tahlequah/Groh/JL/Mitchell/McNeely/NASA); leaked build
placeholders (Steagald/Kuhlmann/Kyles/Labron/Garrison). Doctrine pages near-spotless (substance);
their defect signature is link plumbing only.
LINT-30 GATE at completion: status CHECKED, 3,682 highs — ALL in the two documented P2-pending
classes (inv1 2,299 findings-without-adjudication = the P2 workload; inv2 1,380 sub-quorum
findings awaiting orchestrator backfill from panel-results verdict maps; inv5 count gate).
Zero structural/lane/duplicate-vote failures. Cron 5458d4c9 deleted.
NEXT: P2 panel-findings adjudication (~2,299 findings; mechanical classes above enable class-wide
dispositions) -> P3 fixes -> P4 sweeps -> P5 gate -> P6 publish-brief.

**P2 PANEL-FINDINGS ADJUDICATION COMPLETE (2026-07-19 ~12:45).** Same-day arc after the lens
completion, user-directed budget (~17 boosted points, stop 02:30): (1) QUORUM BACKFILL — 1,443
votes projected from persisted panel-result verdict maps (P2-BACKFILL-RULING: verdicts blind at
source, projection stamped); inv2 1,380->21. (2) TALLY PASS — 2,003 verdicts under >=2-of-3
(1,803 DISMISSED / 200 UPHELD->P3). (3) SM PASS — 75 MODIFIED under P2-SM-RULING (>=2 stands-
modified = adopt tightened framing). (4) INDIVIDUAL PASS — 221 orchestrator-reasoned verdicts
over the escalate queue (12 evidence packets): 15 UPHELD, ~197 MODIFIED, 9 DISMISSED incl 2 more
disclosure-induced FPs (Bryan County, Olivier) + role-taxonomy-overreach dismissals; P2-QF-RULING
formalized the quote-fidelity sub-classes (130 harvest-artifact MODIFIED staged mechanically,
verified by sample; 14 residue individually incl genuine rendered-quote defects Oliver
'in rural areas' truncation + Vinton Alton/Aton, and cached-text OCR corruptions Lopez-Mendoza
'Jams', Stovall 'conductive' where the PAGES are right). Role-sep held: staging/evidence-prep=
opus workers, all verdicts+rulings=fable orchestrator, spot-checks both directions.
END STATE: adjudications 32 -> 2,331 (all 2,329 findings adjudicated); gate highs 3,682 -> 512 =
487 fix-owed (THE P3 QUEUE: ~200 tally-UPHELD + ~75 SM + ~212 individual) + 21 unresolvable
sub-quorum (adjudicated) + 2 orphan adjudication refs (pre-existing, P5 tidy) + inv5 counts.
Zero unadjudicated. P3 (content fixes) NOT started — not sanctioned this run; class catalog +
per-finding proposed fixes ready. Spend: ~10 worker dispatches + orchestration, well under cap.
