---
title: "LINT-16 opinion-count fixture (fail)"
type: doctrine
status: verified
---

# LINT-16 opinion-count fixture (fail)

F-S5-01: the Opinion column must carry EXACTLY ONE non-empty opinion link per
data row — a blank Opinion cell (zero links) and a double-linked cell both fail.

## Key cases

| Case | Holding | Opinion |
|---|---|---|
| *[[Weeks v. United States]]*, 232 U.S. 383 (1914) | Federal exclusionary rule; Opinion cell left blank. |  |
| *[[Mapp v. Ohio]]*, 367 U.S. 643 (1961) | Exclusionary rule incorporated; two links in one cell. | [opinion](https://www.courtlistener.com/opinion/106285/mapp-v-ohio/) [opinion](https://supreme.justia.com/cases/federal/us/367/643/) |
