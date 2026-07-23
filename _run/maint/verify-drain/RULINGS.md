# MAINT-1 verify-drain rulings — 2026-07-23 (orchestrator: claude-fable-5)

Context: loop-1 drain promoted 142 but left 31 party-leg and 5 cite-leg failures that are
evidence-model gaps, not genuine identity doubts. CL's Harvard-sourced opinion text carries **no
caption block**, so a party that the body prose never names (petitioner sheriffs, state officers,
"Petitioner" style) cannot satisfy a body-text-only party leg — *Marbury v. Madison* fails on
"madison", *Berkemer* on "berkemer", *Frazier v. Cupp* on both sides ("Petitioner was convicted…").
The S2 R2 two-key's PURPOSE (G1/G3: never trust name-rank; block fabricated identities) is served
by evidence anchored to the citation-pinned cluster, not by body prose specifically.

**MAINT-1-R1 — caption-leg fallback (party leg).** When `expected_citation_found` is true (the
cluster is pinned by the official cite in `cluster.citations[]`) and `canonical_name_match` is true
(the cluster's OWN caption — fetched by cluster id, never by name-rank — names our parties), a
party side absent from the caption-less body text is earned from the cluster caption, provided at
least one side IS present in the body text (ties the fetched text to the case). Recorded distinctly
in the promotion warning as `caption-leg`.

**MAINT-1-R2 — structural fallback (party leg, zero body-side case).** Where NO side appears in
body text (e.g. *Frazier v. Cupp* — "Petitioner" throughout; *State v. Demesme* — 94-char writ
denial), the party leg may be earned only when, in addition to R1's cite + canonical-caption keys,
the lead opinion is confirmed **structurally bound** to the pinned cluster (lead_opinion_id present
in the cluster's `sub_opinions[]`, live-fetched). Recorded as `structural-leg`. Fail-closed
otherwise.

**MAINT-1-R3 — web-dual-leg citation key (cite leg).** Where CL's cluster carries an empty
`citations[]` (CL data gap) but the lake official cite has `source: "web-dual-leg"` (two
independent web lanes confirmed the cite during S9 — the A16 off-CL two-key analogue), the cite
leg is satisfied by that provenance. Applies to: Alasaad v. Wolf, Carroll v. Carman, Jimerson v.
Lewis, People v. Frederick, United States v. Kolsuz (all canonical_match=true, party leg passed).

**Token-selection repair (not a ruling — bug fix).** Side matching now tries every significant
token of a side, not one heuristic "last token" (fixes `etc`/`individual`/`importing` artifacts in
LaDuke, Knight, Go-Bart).

**Explicitly NOT promoted:** `illinois-v-fisher--5141053` (stub, canonical_name_match=false —
the only failure without the caption key; stays under_review pending individual review).

Slip-opinion status (user directive 2026-07-23): genuinely cite-less recent cases get
`status: slip_opinion` (informational banner, not the unverified warning) once the party leg is
earned; they re-enter the drain automatically when CL assigns a reporter cite (cite_appeared rows).
