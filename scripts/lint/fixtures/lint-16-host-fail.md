---
title: "LINT-16 host whitelist fixture (fail)"
type: doctrine
status: verified
---

# LINT-16 host whitelist fixture (fail)

F-S5-06: broad `.us` / `.gov` suffixes are NOT accepted — only the exact
whitelist plus the official-court host set / `.uscourts.gov` zone.

## Key cases

| Case | Holding | Opinion |
|---|---|---|
| *[[Bad Dot Us]]*, 1 U.S. 1 (1900) | Arbitrary `.us` host must fail. | [opinion](https://evil.us/opinion/1) |
| *[[Bad Dot Gov]]*, 2 U.S. 2 (1901) | Arbitrary `.gov` host must fail. | [opinion](https://evil.gov/opinion/2) |
