---
title: LINT-10 em-dash budget self-test fixture
type: fixture
---

# LINT-10 em-dash budget fixture

<!--
CONVENTION (S1 A3 self-test):
Each labeled block below is immediately preceded by a marker HTML comment whose
body reads "expect: TOKEN" (delimiters omitted here so the parser does not match
this doc). The block is the run of non-blank lines that follows, up to the next
blank line. Recognized TOKENs:
  pass          -> the lint must emit ZERO violations for the block
  fail-block    -> the lint must emit a per-BLOCK violation (>1 em-dash in block)
  fail-sentence -> the lint must emit a per-SENTENCE violation (>=2 in a sentence)
  fail          -> the lint must emit AT LEAST ONE violation of any kind
All em-dashes below are U+2014; en-dashes/hyphens are never counted. These are
HTML comments, so the lint masks them and never counts their text.
-->

<!-- expect: pass -->
A clean paragraph with no long dashes at all, just ordinary prose about a search of a home and the reasonableness inquiry that follows.

<!-- expect: pass -->
A paragraph with exactly one em-dash — which is within the per-paragraph budget and must not be flagged.

<!-- expect: fail-block -->
This paragraph carries two em-dashes across two sentences. The first sentence spends one — right here. The second sentence spends another — over there.

<!-- expect: fail-sentence -->
This single sentence spends two em-dashes — one here — and one more there, so the per-sentence budget is blown.

<!-- expect: pass -->
The witness testified that "the officer approached — quickly — and knocked twice" and the em-dashes sit inside a direct quotation, so they are exempt.

<!-- expect: pass -->
The court wrote “the search — a warrantless entry — was unreasonable” and said nothing further, so the curly-quoted em-dashes are exempt.

<!-- expect: pass -->
Under the authority-weight lexicon the tier reads Binding — SCOTUS as a controlled label, and its em-dash is exempt from the budget.

<!-- expect: fail -->
- A single list item that spends two em-dashes — one — and then two, which exceeds the per-item budget.
