---
title: "LINT-16 opinion-scope fixture (pass)"
type: doctrine
status: verified
---

# LINT-16 opinion-scope fixture (pass)

F-S5-08: anchor/host checks are scoped to the Opinion column ONLY. A non-opinion
markdown link in a Holding cell (arbitrary anchor, non-whitelisted host) must NOT
be flagged as a bad opinion link.

## Key cases

| Case | Holding | Opinion |
|---|---|---|
| *[[Katz v. United States]]*, 389 U.S. 347 (1967) | Reasonable expectation of privacy; see the [statutory backdrop](https://www.congress.gov/bill/statute) discussed in the brief. | [opinion](https://www.courtlistener.com/opinion/107724/katz-v-united-states/) |
