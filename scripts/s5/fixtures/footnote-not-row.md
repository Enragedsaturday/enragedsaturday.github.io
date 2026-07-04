---
title: "convert: footnote is not a table row (fixture)"
type: doctrine
---

# convert: footnote is not a table row

F-S5-03: a footnote definition (or block anchor) abutting a table — with no
blank line between — must NOT be swallowed as a table row and rewritten.

## Key cases

| Case | Holding | Opinion |
|---|---|---|
| *[[Terry v. Ohio]]*, 392 U.S. 1 (1968) | A brief stop and frisk. [^note] | [opinion](https://www.courtlistener.com/opinion/107729/terry-v-ohio/) |
[^note]: This is a footnote with a | pipe that must never become a table row.
