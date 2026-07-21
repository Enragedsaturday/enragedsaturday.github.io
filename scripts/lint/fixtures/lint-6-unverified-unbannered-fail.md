---
title: "Fixture Unbannered Case"
type: case
treatment:
  field_i_validity: "unverified_stub"
  as_of_content: 2026-07-07
  as_of_treatment: 2026-07-07
lake:
  record_id: "Fixture Unbannered Case"
  status: verified
  projected_at: 2026-07-07
---

# Fixture Unbannered Case

A malformed/injected Field-I whose value TEXTUALLY says "unverified" but is NOT the
canonical `unverified` token. Post-P4-14, `_banner_driven` mirrors the component: a
page whose validity RESOLVES to the `unverified` composite is always banner-driven,
so a genuine `unverified` page can no longer be unbannered. This value does NOT
resolve to that composite (`resolveTreatment()`/`normFieldI` reject it), so the R15
banner would NOT render (`lake.status: verified`, no `draft: true`) and the page
fails visible: leg (a) out-of-enum `field_i_validity`, AND leg (d) unverified-textual
validity with no banner state. This mirrors caseHelpers' "an injected bogus status
fails VISIBLE" defense-in-depth. Must FAIL.
