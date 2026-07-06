---
title: "LINT-9 anchor immediately followed by a wikilink (fail)"
---

# LINT-9 mid-line anchor adjacent to a wikilink

See rule ^pin-3[[Terry v. Ohio]]

The `^pin-3` block anchor above is NOT the last token on its line (the wikilink
follows it with no separating whitespace), so Quartz renders it literally. With
the old 'x' filler the masked line became `See rule ^pin-3xxxxxxxxxxxxxxxxx` and
the anchor match ran through the fill to end-of-line — a false negative. The '#'
filler stops the match at the anchor's true end, flagging the leak HIGH.
