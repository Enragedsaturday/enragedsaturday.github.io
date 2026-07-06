---
title: "LINT-16 wikilink-pipe prose is not a table (pass)"
type: doctrine
status: verified
---

# Prose with a wikilink display pipe must not be read as a case table

This [[Terry v. Ohio|ruling]] is a landmark case.
| --- |

The F-S5-03 pipe masking keeps a wikilink display pipe (and code-span pipes)
from tripping GFM table detection — before the fix, iter_tables read the prose
line above as a Case-table header because a separator-shaped line follows it.
