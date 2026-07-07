---
title: Empty ID Page
type: case
lake:
  record_id: ""
  status: verified
---

# Empty ID Page

CR-12: this page's `lake.record_id` is an explicit empty string (an authoring
mistake). Before the fix, page_record_id() masked it as the filename stem — which
happens to match a valid record — so the page↔record gate passed silently. After
the fix, the empty override is returned as-is and flagged HIGH.
