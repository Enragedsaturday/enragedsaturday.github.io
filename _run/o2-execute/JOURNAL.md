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
