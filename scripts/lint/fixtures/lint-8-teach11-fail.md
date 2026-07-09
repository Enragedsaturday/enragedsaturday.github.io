---
title: LINT-8 TEACH-11 fail fixture
type: reference
---

# LINT-8 TEACH-11 fail fixture

Each line below passes a naive text lint (the device name is spelled correctly and
the maxim reads fluently) but fails the TEACH-11 target+wording check.

- MISLINK: the reader sees the CREW device but the link goes to the wrong page —
  [[Fourth Amendment Framework|C.R.E.W.]] (target resolves, but not to the CREW
  register page). *(S7 04f class.)*
- BROKEN TARGET: [[No Such Register Page 9Z|Three Golden Rules]] — the device
  wikilink does not resolve at all.
- INVERTED MAXIM: the Fourth Amendment deals in **possibilities, not probabilities** — the Golden-Rule #3 wording is inverted. *(S7 04a class.)*
