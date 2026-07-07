---
title: Wikilink Oldpath
weight: 10
related: ["[[7-exceptions-warrant/Automobile Exception]]"]
---

# Wikilink Oldpath

CR-07 isolation fixture: this page's ONLY retired-folder reference is a
wikilink-syntax `related:` frontmatter value (no bare-path homes/related, no body
wikilink). Before the fix, `_retired_in` saw the leading `[[` and never matched, so
the reference passed silently; after the fix it is flagged HIGH.
