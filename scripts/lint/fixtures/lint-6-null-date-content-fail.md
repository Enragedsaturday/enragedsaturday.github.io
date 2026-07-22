---
title: "Fixture Null-Date Reader-Facing Case"
type: case
citation: "3 U.S. 3 (1984)"
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: null
  as_of_treatment: 2026-06-30
lake:
  record_id: "Fixture Null-Date Reader-Facing Case"
  status: verified
  projected_at: 2026-07-22
---

# Fixture Null-Date Reader-Facing Case

P5 R14-B null-token precision fixture. This page is NOT banner-driven
(`lake.status: verified`, Field-I `good_law`, no `draft: true`), so it reaches a
reader as settled and R3 requires BOTH currency dates non-blank. Its
`as_of_content` is the literal YAML-null placeholder `null`, which the stdlib
frontmatter subset parser leaves as the STRING 'null'. Before the null-token fix
that string was non-blank and slipped the date sub-check (the R14-B false green);
`c.is_null_token` now folds it to blank, so LINT-6 must FIRE HIGH here. Must FAIL.
