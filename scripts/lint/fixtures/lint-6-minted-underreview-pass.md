---
title: "Fixture Minted Case"
type: case
citation: "1 U.S. 1 (2020)"
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: unverified
  as_of_content: 2026-07-07
  as_of_treatment: 2026-07-07
lake:
  record_id: "Fixture Minted Case"
  status: under_review
  projected_at: 2026-07-07
---

# Fixture Minted Case

A born-draft mint page (adjudicated E1): Field-I `unverified` + `lake.status:
under_review`. S5 R15 renders the ⚪ banner from `lake.status ∈ {draft,
under_review}`, so R2 ("⚪ never reaches a reader unbannered") is satisfied WITHOUT
`draft: true` (which would hide the page from the build). Must PASS LINT-6.
