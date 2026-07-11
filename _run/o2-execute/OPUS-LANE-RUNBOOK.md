# S9 Opus 3rd-Lens Panel Lane — Drive Runbook

The panel is N-of-3: **codex-A** + **codex-B** (both driven by `scripts/s9/run_panel.py`)
plus **one Opus model-diversity lens** (`lane = claude-opus-panel`, `model = claude-opus-4-8`,
`lens = opus-both` — reviews *every* paneled dimension, no charter subset). This runbook drives the
Opus lane at scale so every codex-complete group also carries the 3rd vote and the `>=2-of-3` tally
(check_ledger inv-2) has its full quorum.

Status at authoring: Opus lens done for **4 / 1357** groups (`opus-pack-001` pilot). **1353 owed.**

## 0. What the machine already knows (ground truth)

- **The 3 distinct panel lanes are `codex-A`, `codex-B`, `claude-opus-panel`.** The pilot's 5 votes +
  3 attestations and the orchestrator's 5 adjudication tallies all key on `claude-opus-panel`. That is
  the vote/attestation `lane` string — **not** `opus-panel`, which is only the per-invocation
  `lane_id` prefix (`opus-panel-<batch>-<short>`, the panel-results filename). The lane string is the
  single constant `emit_opus_pack.OPUS_LANE`; change it in one place if the orchestrator ever re-keys.
- **Finding ids are deterministic:** `F-S9-PR-sha1(object|assertion_id|dimension)[:10]`. An Opus
  refutation of an assertion a codex lane already raised MERGES onto that finding — a 2-vote finding
  becomes a 3-vote paneled finding. No new finding row; +1 vote row.
- **Vote verdict is FINDING-semantics** (via `panel_review._ASSERTION_TO_FINDING_VERDICT`): the
  reviewer's per-assertion `refuted` (defect real) → vote `verdict = "stands"` (the finding stands);
  assertion `stands` → vote `refuted` (the sibling's finding is wrong). `emit_opus_pack` applies this
  through the shared `emit_lens_result`; do not hand-map.

## 1. Pipeline (per batch, repeat until 0 owed)

```
(a) select N codex-complete, not-yet-opus-done groups   ── checkpoint scan
(b) generate packs (panel_review --panel-review-opus)   ── one .md + .manifest.json per batch
(c) dispatch fresh o2-opus-xhigh reviewer agents         ── one per pack, parallel, each -> a JSON file
(d) emit  (emit_opus_pack.py --reviews … --manifests …)  ── writes finding/vote/attestation rows
(e) reconcile + checkpoint                               ── re-scan; loop
```

### (a) Select groups — the resumable checkpoint

A group (= object path) is **opus-done** iff it already carries an Opus attestation **OR** any of its
findings already has a `claude-opus-panel` vote. `emit_opus_pack.opus_done_objects(ledger_dir)`
computes exactly this set from the live ledger (robust to a crash between vote-append and
result-persist). To list owed groups:

```python
import sys; sys.path.insert(0, "scripts/s9")
import emit_opus_pack as eo, panel_review as pr
wl   = pr.load_worklist_index(pr._default_worklist())          # 1357 groups
done = eo.opus_done_objects(eo.lr.RUN_DIR)                      # opus-done set (4 at start)
# codex-complete = group has a codex-A AND codex-B attestation or vote; the codex driver's
# checkpoint (run_panel.py) is authoritative. Restrict the owed set to codex-complete groups
# so Opus never reviews a group the codex lanes have not finished.
owed = [g for g in wl if g not in done]                        # + codex-complete filter
```

Only dispatch Opus over **codex-complete** groups (both codex lanes attested/voted) — the panel is a
tally, and an Opus vote on a group the codex lanes have not finished cannot reach quorum yet. Use
`run_panel.py`'s checkpoint (codex attestations/votes by lane) as the codex-complete gate.

### (b) Generate packs

```bash
python3 scripts/s9/panel_review.py --panel-review-opus "<gid1>,<gid2>,<gid3>,<gid4>" \
        --batch-id opus-pack-013 --out-dir _run/s9/opus-packs
# writes _run/s9/opus-packs/opus-pack-013.md  +  opus-pack-013.manifest.json
```

- **Groups per pack: 4** (pilot-proven; `opus-pack-001` = 4 groups / 41 assertions / 0 blindness
  violations). Measured disclosure size (120-group sample): **mean ~81.6K chars/group ≈ 21.5K input
  tokens**, p90 ~145K chars. So a 4-group pack is **~330K chars ≈ ~86K input tokens (mean)**, and a
  p90-heavy pack ~153K input tokens — both fit an o2-opus-xhigh reviewer's context with headroom for
  xhigh thinking + the JSON reply. `text_cap=120000` already truncates any single opinion text, so no
  one group can blow the pack.
- **Optional char-budget guard for the heavy tail:** when slicing the owed list into packs, close a
  pack early if its running disclosed-char total would exceed **~330,000 chars** (the 4-group mean).
  Heavy groups then pack 2–3; light (existence/treatment-only, lake-only) groups pack 5–6. Keeps every
  pack's input ≲ ~90–100K tokens. 6/pack is viable **only** if the reviewers are confirmed on
  1M-context Opus; default to 4 for a portable 200K-safe size.
- Each pack `.md` is fully self-contained (framing + inlined content page + full lake records +
  capped opinion texts + `group_inventory`); the manifest carries one review-manifest per group with
  `blindness_violations` pre-checked. **Do not dispatch a pack whose manifest shows a group with
  non-empty `blindness_violations`** — pull that group and regenerate.

### (c) Dispatch reviewers — fresh o2-opus-xhigh agents, one per pack, parallel

- **One agent per pack**, launched in the same message for concurrency. Each agent:
  reads **only** the inlined pack `.md` evidence (no filesystem, no CL, no outside knowledge);
  is refute-framed, default-refute-on-uncertainty; writes its reply to a file
  `_run/s9/opus-reviews/opus-pack-013.json` and returns that path.
- **Reviewer output contract** (the shape `emit_opus_pack` consumes):
  ```json
  {"packs": [
     {"group_id": "<echo the GROUP header>", "lens": "opus-both",
      "reviewed": [ {"assertion_id": "...", "dimension": "existence|support|quote_fidelity|pincite|treatment|black_letter",
                     "verdict": "stands|refuted|stands-modified", "verifiable_from_disclosed": true,
                     "defect": null | {"problem","severity","proposed_fix","evidence_quote","needs_cl","locator_note"},
                     "reasons": ["..."], "breaks_true_positives": false,
                     "residual_risks": [], "suggested_tightening": null}, ... ]},
     ... one entry per GROUP in the pack ...
  ]}
  ```
  Every `assertion_id` in each group's `group_inventory` must appear exactly once in that group's
  `reviewed[]`. A group the reviewer finds wholly clean returns all-`stands`.
- **Reviewer parallelism: 8–10 concurrent agents** (mirrors the codex fleet's proven 2→12 ramp; the
  bottleneck is Opus agent dispatch, not the emit step). Do not exceed the fleet's concurrency budget.
- **Writer ≠ checker:** these reviewer agents are the panel vote — they must be *fresh* (no prior
  panel context), and the orchestrator/emit step never re-reviews their assertions. The emit step is
  pure plumbing.

### (d) Emit — `emit_opus_pack.py` (stdlib; the clean, driven path that replaced the hand-written pilot)

```bash
python3 scripts/s9/emit_opus_pack.py \
        --reviews  _run/s9/opus-reviews/opus-pack-013.json [more…] \
        --manifests _run/s9/opus-packs/opus-pack-013.manifest.json [more…] \
        --run-id prod
# or --dry-run first to see routing/coverage without writing a row
```

Per group it routes through the exact `panel_review.emit_lens_result` contract (lane=claude-opus-panel):
- defects → `s9.finding.v1` (deduped by deterministic id) + `s9.vote.v1`;
- agreement on a sibling's finding → `s9.vote.v1` (merges 2→3);
- wholly clean (no in-charter defect) → `s9.attestation.v1`;
- full verdict map → `panel-results/<lane_id>.json` (orchestrator backfill).
- **Fail-closed:** a group in the manifest but missing/empty/malformed in the reviewer JSON → a
  `no_review` result (no rows, no false clean attestation) — driver re-dispatches that group next batch.
- **Idempotent:** a group already opus-done is skipped — re-running emit over the same JSON never
  double-counts and never writes a duplicate-lane vote (inv-2 forbids two votes from one lane on one
  finding). Safe to re-run after a partial crash.

Batch many packs into one emit call (pass all `--reviews` + all `--manifests`); the report's
`totals` gives `emitted_groups / skipped_done / no_review / findings_new / votes_new /
clean_attestations` and lists any `unroutable_packs` (a pack group_id not in the supplied manifests)
or `bad_files`.

### (e) Reconcile + checkpoint

- After each emit, re-run `opus_done_objects` — the owed count drops by `emitted_groups`. Any
  `no_review` groups stay owed and get re-packed next batch.
- Periodically run the LINT-30 gate (`python3 scripts/s9/check_ledger.py _run/s9`) to confirm the
  merged ledger stays green (3 distinct lanes per paneled finding; no duplicate-lane votes;
  `>=2-refute` findings never plain-UPHELD). Adjudication of the newly-3-voted findings is the
  orchestrator's job, not this lane's.

## 2. Cost / throughput model

From the pilot (`opus-pack-001` = 4 groups / 41 assertions) + a 120-group disclosure-size sample
(mean 81.6K chars/group ≈ 21.5K input tok; 97.5% of groups carry an opinion text). Corpus:
**1353 owed groups**, ~6454 owed assertions, ~4.8 assertions/group. Opus 4.8 pricing: **$5.00 / 1M
input, $25.00 / 1M output** (`claude-opus-4-8`, 1M context).

| Unit | Input tokens | Output+thinking tokens (xhigh) | Cost (Opus 4.8) |
|---|---|---|---|
| **Per group** | ~21.5K | ~3–6K (xhigh thinking dominates the ~1.4K JSON) | ~$0.11–0.26 |
| **Per pack (4 groups)** | ~86K (+645 framing) | ~15–24K | **~$0.60–1.05** |
| **Full 1353 (≈339 packs)** | **~29.3M** | **~5–9M** (≈6.8M mid) | **~$260–430** (≈**$316** mid: $146 in + $170 out) |

- **Wall-clock:** ~339 packs. An xhigh Opus review of ~19 assertions across 4 groups over ~86K input
  tokens is a minutes-long turn — estimate **~6–12 min/pack (≈8 min median)**. At **10 concurrent
  reviewers**: ⌈339/10⌉ ≈ 34 waves × ~8 min ≈ **~4.5 h**; at 8 concurrent ≈ **~5.6 h**. The emit +
  checkpoint steps add seconds per batch, not hours.
- **No Batch-API / cache discount assumed:** packs are one-shot interactive agent reviews with only a
  ~645-token shared framing prefix — prompt caching across packs isn't worth it, and the reviewers run
  as live agents, not through the 50%-off Batches endpoint. If a future run routes reviews through
  Batches, halve the token cost (but lose interactivity).

## 3. Risks in scaling the lane

1. **Reviewer context overflow on the heavy tail.** A pack of 4 large text-promoted groups can hit
   ~150K+ input tokens; at 200K reviewer context that leaves thin room for xhigh thinking + output and
   risks a truncated / `no_review` reply. Mitigation: the char-budget guard in (b), and 4/pack (not 6)
   as the default. Confirm the reviewer model's context window before raising groups-per-pack.
2. **Codex-complete gating.** If Opus reviews a group before both codex lanes finish, the finding
   won't reach 3 votes and inv-2 will flag `<3 distinct lanes`. Always intersect the owed set with the
   codex checkpoint (run_panel.py) — do **not** drive Opus off the raw worklist.
3. **Under_review lake stubs.** Some groups' lake records are S6-promotion frontier stubs (empty
   pinpoints, `under_review`); the pack still discloses the opinion text, but the reviewer may flag a
   coverage gap rather than a content defect. That is a correct `no_review`/note, not a lane bug — it
   routes to the coverage inbox, not a fabricated finding.
4. **Reviewer JSON drift.** A reviewer that echoes a wrong/oddly-formatted `group_id`, or returns
   `reviewed` as a non-list, lands as `unroutable_packs` / `no_review` — never a fabricated finding,
   but it costs a re-dispatch. Keep the GROUP header verbatim in the prompt and validate the JSON file
   parses before the emit step (the emit step already fail-closes, but an early `--dry-run` catches it
   cheaper).
5. **Lane-name divergence.** If any component emits under `opus-panel` instead of `claude-opus-panel`,
   the pilot's already-adjudicated findings would fork into two opus lanes and inv-2 would miscount.
   The single `OPUS_LANE` constant is the guard — never inline the string elsewhere.

---

## PROVEN RESUME PROCEDURE (as run 2026-07-11, waves 1-2 = 72 groups + 6 val = 83/1357 opus-done)

The Opus 3rd-lens lane is a RESUMABLE MULTI-SESSION GRIND. Checkpoint = `opus_done_objects()` (any object with a claude-opus-panel attestation OR vote). To continue, repeat this wave loop:

1. **Pick next batch** (LIGHT groups first — case pages + lake records; doctrine pages are HEAVY, do them last at 1-2/pack): select codex-complete (both codex-A + codex-B lanes present) AND not-yet-opus-done groups, 40 at a time.
2. **Generate 10 packs of 4** via `panel_review.py --panel-review-opus "<comma-ids>" --batch-id opus-wN-KK --out-dir _run/s9/opus-packs`. Verify max pack size < ~600KB (light groups are safe; if a pack >800KB, it slipped in a heavy group — reduce that pack).
3. **Dispatch 10 fresh o2-opus-xhigh reviewer agents** (the orchestrator does this via the Agent tool — a shell driver CANNOT spawn them). Each: read its pack .md, review using ONLY inlined evidence (HARD independence — no other file/search/memory/ledger), write `{"packs":[...]}` JSON to `_run/s9/opus-reviews/opus-wN-KK.json`, return ≤4-line summary. No emit/commit by the reviewer.
4. **Wait** via a background bash `until [ $(ls opus-wN-*.json|wc -l) -ge 10 ]` (or the agent notifications).
5. **Batch-emit:** `emit_opus_pack.py --reviews _run/s9/opus-reviews/opus-wN-*.json --manifests _run/s9/opus-packs/opus-wN-*.manifest.json`. Expect 0 no_review/unroutable/bad; votes merge onto codex finding-ids; clean groups → opus attestations; idempotent.
6. **Commit** the wave (findings/votes/attestations + packs/reviews) as a checkpoint.
7. Repeat until light groups exhausted (~24 more waves), then doctrine pages (1-2/pack), then the ~251 groups that finish codex on the next window.

RECURRING DEFECT CLASSES the opus lens surfaces (for P3 fix, mostly mechanical/class-wide): (a) corrupt harvested `pinpoint.quote` fields = content-page `## Issue`/`## Rule` markdown instead of opinion text (rendered quotes are verbatim-faithful → low-severity, class-wide re-harvest fix); (b) leaked build placeholders in `treatment.scope_note` (Roberson, Brendlin); (c) `date_decided` contradictions vs opinion text (Acevedo, Fulminante, Carroll, Brewer); (d) many extractor `quote_fidelity=mismatch` flags are FALSE POSITIVES the opus lens overturns.

**PACK-GEN BUGFIX (wave-6):** case names with COMMAS (e.g. "Lo-Ji Sales, Inc. v. New York") BREAK the `--panel-review-opus` CLI (it splits its arg on commas). DO NOT shell out to the CLI with comma-joined ids. Instead call the generator DIRECTLY: `import panel_review as pr; pr.generate_opus_pack(group_ids_LIST, batch_id, out_dir="_run/s9/opus-packs")`. Waves 1-5 were unaffected (no comma-named groups slipped in; a comma one hard-fails the whole pack, so all-10-generated == clean).
