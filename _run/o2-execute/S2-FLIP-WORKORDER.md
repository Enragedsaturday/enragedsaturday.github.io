# S2 verified-flip work order (Method step 7 final act — R15 gate-checked)

Orchestrator adjudication 2026-07-06. Pre-conditions ALL MET at dispatch: LINT-12 = 0 (post
first-projection) · LINT-13 = 0 (post repair) · spot-check PASS (68 records live, 0 errors) ·
treatment audit flags all closed (F-S2-28/29 fixed + reruns executed; 248 lane3 proposals
staged proposed-only for S9) · CodeRabbit spec gate result on file (see gate artifact in
_run/gates/). LINT-14 = 2 (Entick/Wilkes) carried as a NAMED open pair riding the user's R14
whitelist decision — not a silent gap, not a flip blocker (neither row is flip-eligible).

## Implement `--flip-verified` in scripts/s2/ingest.py

Eligibility (ALL required, mechanical):
- status == under_review
- identity_method == "citation+party-text" AND expected_citation_found AND party_name_in_text
- record schema-valid (validate via the real lint13 validator in-process)

Expected flip count: 421 (orchestrator pre-count). Report the actual count and DIFF any
mismatch by record_id — do not proceed past a mismatch silently.

Explicitly NOT flipped (assert these remain untouched): 21 name+docket + 14 pending-method
under_review rows (S9's deep pass) · 65 verified_identity frontier shells (SD10: never
`verified`, no treatment/progeny promotion — they are S6's queue) · 25 fabrication_suspected ·
5 not_found.

Each flip journals one event: {step: "r15-flip", record_id, gates: ["schema", "two-key",
"a1-replacement", "dual-dates+provenance", "drift", "spot-check", "treatment-audit",
"coderabbit"], adjudicated_by: "orchestrator claude-fable-5"}. Then regenerate the manifest
counts and re-run the projector (`project.py --write` — lake.status changes on flipped pages),
re-run LINT-12/13/14, and report all three counts (expect 0 / 0 / 2).

Self-test: a flip fixture (eligible flips; each ineligible class does not; journal event
shape). Full suite green. No commits (orchestrator commits).
