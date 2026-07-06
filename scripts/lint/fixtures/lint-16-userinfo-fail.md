---
title: "LINT-16 userinfo/hostless/short-row fixture (fail)"
type: doctrine
status: verified
---

# LINT-16 userinfo host bypass + hostless + short row (fail)

F-RETRO-A: URL userinfo must not smuggle a whitelisted string past the R17
host check; a hostless `https:///` URL and a row missing its Opinion cell must
both fail closed rather than skip the whitelist check.

## Key cases

| Case | Holding | Opinion |
|---|---|---|
| *[[Userinfo Bypass]]*, 1 U.S. 1 (1900) | userinfo names evil host. | [opinion](https://www.courtlistener.com:x@evil.com/opinion/1) |
| *[[Hostless URL]]*, 2 U.S. 2 (1901) | hostless https URL. | [opinion](https://///opinion/2) |
| *[[Short Row]]*, 3 U.S. 3 (1902) | row missing its Opinion cell. |
