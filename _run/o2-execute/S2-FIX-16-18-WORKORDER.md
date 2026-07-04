# S2 fix work order — F-S2-16 / F-S2-17 / F-S2-18 (paced-run session-3 findings)

Adjudicated by the orchestrator (claude-fable-5) 2026-07-04 from session-3 evidence. All three
UPHELD as code defects in `scripts/s2/ingest.py`. Fix them exactly as specified; stdlib only; NO
network calls (offline code + self-tests only — the re-adjudication run happens inside the next
paced builder session); NO git commits (orchestrator commits).

## Evidence base (already verified live — do not re-derive)

Session 3 flagged 5 rows fail-closed:
- `fabrication_suspected`: Benn v. Lambert · Bivens v. Six Unknown Named Agents · Board of
  Education v. Earls · Brower v. County of Inyo
- `not_found`: Birchfield v. North Dakota

Bivens/Earls/Brower: two-key PASSED (`expected_citation_found: true`, `party_name_in_text: true`),
correct clusters selected (108375 / 121171 / 112218) — the exact-slug caption gate alone branded
them fabrication. CL canonicals: "Bivens v. Six Unknown Named Agents of Federal Bureau of
Narcotics" · "Board of Education of Independent School District No. 92 of Pottawatomie County v.
Earls" · "Brower Ex Rel. Estate of Caldwell v. County of Inyo".

Benn: cluster 776954 correct; expected `283 F.3d 1040 (9th Cir. 2002)` never matched because
`normalize_cite` only strips a bare `(YYYY)` tail; party key legitimately false ("Lambert" — the
habeas warden — appears 0× in the 109KB opinion text; "Benn" 154×). Post-fix expected outcome:
`under_review`, method `name+docket`.

Birchfield: the single `case_name="Birchfield v. North Dakota"` + court=scotus + 2016-window
search returns count 0 because CL's canonical caseName for the merits cluster (3216497, 579 U.S.
438, filed 2016-06-23) is the mangled consolidated caption "Birchfield v. N. Dakota. William
Robert Bernard". Verified live: same query with `q=` instead of `case_name=` finds it (rank 3 of
14, easily disambiguated by citation+date scoring vs the two cert-stage orders 8424452/8423610);
`citation="579 U.S. 438"` finds it rank 1 of 2.

## F-S2-16 — caption gate: exact slug equality is the wrong comparator, and it outranks the two-key

`canonical_caption_match` (line ~520) is `slugify(input) == slugify(canonical)`, and in
`apply_identity` a miss hard-gates to `fabrication_suspected` even when R2's own authoritative
confirmation (citation AND party-in-text) passed. Spec grounding: R2 makes citation+party-text the
verification keys; R2(c)'s "name ≠ canonical" check exists to catch name-rank substitution
(live proof class: "Adams v. Williams" vs *Williams v. Adams*) — not caption-style shortening.

**Fix (two parts):**
1. Replace the comparator with an order-sensitive per-side token containment match:
   - Split input and canonical captions on the `v.` boundary (reuse the `first_party_terms`
     splitting approach; strip any trailing year parenthetical first).
   - Tokenize each side via slugify-style normalization.
   - Match iff for each side respectively: input-side tokens ⊆ canonical-side tokens OR
     canonical-side ⊆ input-side. NO cross-side matching — "Adams v. Williams" vs "Williams v.
     Adams" MUST still fail (fixture required).
   - Compare against ALL of `cluster.case_name`, `case_name_full`, `case_name_short` (accept if
     any matches). Handle non-`v.` captions (In re, Ex parte) by whole-caption containment.
2. Precedence in `apply_identity`:
   - containment PASS → existing two-key branches unchanged.
   - containment FAIL + BOTH two-key keys PASS → `under_review`, reason_code
     `caption_mismatch_canonical`, warning kept ("input caption does not match CL canonical
     caption"), identity_method `citation+party-text`. NOT fabrication.
   - containment FAIL + two-key not both satisfied → `fabrication_suspected` (unchanged,
     fail-closed).

Expected post-fix: Bivens/Earls/Brower → containment PASS → `under_review` via citation+party-text.
Birchfield (post-F-S2-18) → containment FAIL ("North" ∉ {"N.", …}) but two-key PASS →
`under_review` + caption warning.

## F-S2-17 — normalize_cite: circuit-style parentheticals never stripped

`normalize_cite` strips only `\(\d{4}\)$`-shaped tails. Every COA/state roster row carries
`"283 F.3d 1040 (9th Cir. 2002)"`-shaped expected citations → the citation key can NEVER match
for those rows (silently degrades scoring and identity method corpus-wide; interacted with
F-S2-16 to produce the Benn false flag).

**Fix:** strip any trailing parenthetical containing a plausible year:
`re.sub(r"\s*\([^()]*(?:17|18|19|20)\d{2}\)\s*$", "", cite)`. Fixtures: `"283 F.3d 1040 (9th Cir.
2002)"` → `"283 F.3d 1040"`; `"389 U.S. 35 (1967)"` → `"389 U.S. 35"`; a cite with NO
parenthetical unchanged; do not strip a mid-string parenthetical.

## F-S2-18 — identity search: no fallback ladder before not_found

`resolve_identity` makes exactly one `case_name=`-filtered search; count 0 → `not_found`. R2(d)
demands cross-check before that verdict.

**Fix:** on zero results (or zero viable candidates after cluster fetch), run a fallback ladder,
journaling each rung (`step="identity.search.fallback"`, rung name, result count):
1. Same filters but the caption in `q=` instead of `case_name=`.
2. `citation=normalize_cite(expected_citation)` (keep `court` filter; DROP the date window —
   cert-stage siblings are separated by the existing citation+date candidate scoring).
3. `docket_number=<docket>` + `court` (only if the roster row carries a docket).
Stop at the first rung yielding a viable candidate; candidates flow through the EXISTING scoring +
two-key + caption logic unchanged. `not_found` only after the ladder exhausts, with the rung trail
journaled (R7 cross-check trail). Keep total added calls bounded: ≤ ~4 extra calls per zero-hit
case (each rung is 1 search + cluster fetches only for the top hits, page_size 10 as today).

## Re-adjudication mechanism (required for the 5 flagged rows)

`set_record_status` fail-closed preservation + journal `step_complete("identity")` currently make
the 5 rows unrecoverable by resume. Add an explicit path:
- CLI: `--readjudicate <record_id>` (repeatable) or `--readjudicate-file <path>`.
- For each named record: journal an adjudication event `{step: "adjudication", record_id,
  findings: ["F-S2-16","F-S2-17","F-S2-18"], adjudicated_by: "orchestrator claude-fable-5",
  action: "reset-identity-and-rerun"}`, clear the identity-step (and downstream lanes') resume
  completion for that record, reset status to `pending` via an `explicit_adjudication=True`
  transition, then let the normal pipeline re-run it end-to-end in the same session.
- The 5 rows: `Benn v. Lambert` · `Bivens v. Six Unknown Named Agents` · `Board of Education v.
  Earls` · `Brower v. County of Inyo` · `Birchfield v. North Dakota`.

## Low-priority (fix if trivial, do not let it grow the diff)

- `counts.cl_calls` in manifest rows stamps the session-cumulative counter at write time, not the
  per-record cost (Brower shows 823; its true cost was ~6 calls). Make it per-record.
- Diagnostic: when a party term is not found in lead text, journal which term missed (one line;
  aids S9 sampling of the name+docket class).

## Acceptance

- All existing self-tests green + new fixtures: reversed-caption still flags; shortened-caption
  two-key-pass → under_review; `(9th Cir. 2002)` cite matches; zero-hit ladder reaches rung 2 for
  a Birchfield-shaped stub; readjudicate resets and re-runs a fail-closed stub record.
- No behavior change for records whose captions match exactly (the 46 citation+party-text
  completions must be resume-stable: zero new calls on resume, statuses unchanged).
- Report: files touched, fixture list, self-test output tail, and the exact new CLI usage line
  for the session-4 launch.
