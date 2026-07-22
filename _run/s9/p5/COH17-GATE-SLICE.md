# COH-17 gate judgment slice (Claude MCP lane, per RULING P5-04(a)) — 2026-07-22

Input: the completed LINT-1 batch (4,425 refs, cluster-first semantics, builder credential).
Batch result: 4,380 pass / 45 mismatch rows after transient retry.

## Violation adjudication (all 45, source-line + cross-credential)
- **5 REAL wrong-cluster URLs** (doctrine-page roster/Sources lines; canonical ids
  MCP-confirmed): SIA Alcohol Tests.md:78 McNeely 882802->858288; :79 Mitchell v. Wisconsin
  4218101->9231242; Aerial and Enhanced Surveillance.md:97 Jardines 2094497->856347;
  Third-Party Doctrine and CSLI.md:120 Gratkowski 4772500->4765051 (964 F.3d 307 cite matches);
  Terry Stops and Reasonable Suspicion.md:156 Dickerson 112879->112873.
- **38 FALSE POSITIVES, two classes** (adjudicated from source lines; URLs verified correct):
  (a) nearest-name pairing grabs a DIFFERENT case named on the same line (Case Index holding
  cells naming related/overruling cases; *Id.* quote-links on case pages; roster lines) — 36
  rows; (b) tokenizer digit-truncation ("District 47J v. Acton" -> want-tokens lose 'acton') —
  2 rows (Vernonia). Lint-heuristic hygiene items -> P5 handoff (pairing should prefer the
  row's [[wikilink]] subject / skip Id.-links; tokenizer should not truncate at digits
  mid-caption). NOT data defects.
- **2 line-ambiguity rows** (Collective Knowledge Cook/Balser shared link -> the URL is
  Balser's, correct as placed; Ramirez row -> URL correct): FP, noted.

## Pass sample (10, deterministic every-Nth, MCP cross-credential)
Quantity of Books (106878 + opinion 9422858 bound ✓), Hill (108305 ✓), Shipley (107982 ✓),
Wayne Walker (2844024 ✓), Katz-on-Recalibration (107564 ✓), Crumble (4456532 ✓ full name
'Prentiss Anthony Crumble', row verified), Knotts-on-Real-Time-Tracking (110882 ✓),
Hayden-on-Arrest-in-the-Home (107465 ✓), Garrison-on-Scope-Manner (111823 ✓),
Cady-on-Community-Caretaking (108850 ✓). 10/10 CONFIRM.

## Verdict
LINT-1 gate box: PASS once the 5 URL fixes land (fix packet FIX-L1URLS); the 38+2 FPs are
documented lint-heuristic items, not corpus defects. Prior-slice lineage: P1 identity slice
75 rows + P4 promo cross-credential fetches + this gate slice.
