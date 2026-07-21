---
title: "Fixture Promoted Identity Case"
type: case
citation: "2 U.S. 2 (2021)"
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: unverified
  as_of_content: 2026-07-07
  as_of_treatment: 2026-07-07
lake:
  record_id: "Fixture Promoted Identity Case"
  status: verified_identity
  projected_at: 2026-07-07
---

# Fixture Promoted Identity Case

P4-14 regression fixture. A verified_identity PROMOTION carries the legitimate state
{lake.status: verified_identity, treatment.field_i_validity: unverified} — the
identity is CL-confirmed but treatment/progeny is not yet machine-verified.
`caseHelpers.shouldDraftBanner` renders the ⚪ banner via its third leg
(`resolveTreatment().fieldI === "unverified"`), because `lake.status` is neither
`draft` nor `under_review`. R2 ("⚪ never reaches a reader unbannered") is therefore
satisfied WITHOUT a separate banner signal, so `_banner_driven` (mirroring the
component) must treat this page as banner-driven. Must PASS LINT-6.
