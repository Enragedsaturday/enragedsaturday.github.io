# S9 ledger schema (draft for interview sign-off — worked instance: F-DEMO-001)

One machine-emitted, reconcilable trail: **findings → votes → adjudications → fixes → inventory**.
JSON-lines files under `_run/s9/` at EXECUTE (`findings.jsonl`, `votes.jsonl`, `adjudications.jsonl`,
`fixes.jsonl`), joined to `assertion-inventory.json` by `assertion_id`. Every row type carries
`schema` (versioned) + lane identity. A script — not an agent — checks the reconciliation
invariants in CI.

## Row types

**`s9.finding.v1`** — emitted by reviewer lanes; reviewers never edit.
`id` · `run` · `object` (path) · `object_class` (case | doctrine | overview | reference | glossary
| index | nav | lake-record | ledger-row | tooling) · `dimension` (D1–D14 | D-TOOL) · `gate`
(G1–G10 | null) · `assertion_id` (join key | null) · `locator {section, lines, verbatim}` ·
`problem` · `severity` (high|medium|low) · `proposed_fix` · `needs_cl` (bool) · `found_by {lane,
model, note, register?}` · `confidence`.

**`s9.vote.v1`** — one per panel lane per paneled finding (legal-assertion dimensions).
`finding_id` · `lane` · `model` · `sandbox` (reviewer lanes = read-only) · `independent`
(isolation statement) · `verdict` (refuted | stands | stands-modified) · `reasons[]` ·
`breaks_true_positives` · `residual_risks[]` · `suggested_tightening`. Votes are recorded
**before** mutual disclosure; the Claude vote records
`recorded_before_other_votes_read: true`.

**`s9.adjudication.v1`** — one per finding.
`finding_id` · `refute_tally {per-lane, rule: ">=2-of-3 refute kills", result}` · `verdict`
(UPHELD | MODIFIED | DISMISSED | ESCALATE) · `adjudicated_holding[]` · `evidence[] {kind:
live-repro | register | spec | panel | lake | cl | web | fixture-baseline, ref}` — a legal
verdict MUST carry lake/cl/web evidence · `adjudicator {lane, model}` · `role_separation`
(the writer≠checker statement, machine-checkable lane ids) · `spawned_findings[]` · `at`.

**`s9.fix.v1`** — one per UPHELD/MODIFIED finding.
`finding_id` · `applied_by {lane, model}` · `artifacts[]` (diff pointers/commits) ·
`content_edits` · `loops[] {loop, re_review {lane, model, round, verdict, issue?}}` —
re-review lane ≠ fix author, always · `loop_cap: 3` (then ESCALATE →
`_review-needed/<slug>.md`) · `writer_neq_checker` · `at`.

## Reconciliation invariants (CI script, fail-closed)

1. Every finding has exactly one adjudication; every UPHELD/MODIFIED adjudication has a fix row
   whose final loop verdict is FIXED, or an escalation file.
2. Every paneled finding's tally has all three lane votes; `>=2 refuted` ⟹ verdict ∈
   {DISMISSED, MODIFIED, ESCALATE} (never plain UPHELD-as-framed).
3. Lane-identity checks: `found_by.lane` ≠ `adjudicator.lane` on legal findings;
   `fix.applied_by.lane` ∉ re-review lanes; no lane closes its own queue row.
4. Every DISMISSED carries a reason (false-positive log — the over-correction defense).
5. Counts reconcile: findings = adjudications; UPHELD+MODIFIED = fixes+escalations; every
   `assertion_id` referenced exists in the inventory; zero inventory items without a verdict.

## The worked instance (this directory)

F-DEMO-001 (COH-28, LINT-3 precision): finding → 3-lane panel (2× gpt-5.5 read-only + Claude,
votes recorded blind) → tally 2-refute+1-stands-modified → **killed as framed**, adjudicated
MODIFIED (the O1 ticket's "pure false positive" premise was wrong per TEACH-01; the proposed
window patch broke true positives two ways) → fix applied (adjudicated fixture; no lint patch;
no content edits — freeze holds) → codex-C re-review round 1 **NOT-FIXED** (caught a stale
evidence pointer) → loop-2 correction → round 2 **FIXED**.
