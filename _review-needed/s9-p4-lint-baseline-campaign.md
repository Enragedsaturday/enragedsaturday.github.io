# S9 P4 escalation — the S8-close KNOWN-RED lint baseline needs its own fix campaign

**Filed:** 2026-07-21 (P4). **Adjudicator:** claude-fable-5-orchestrator.

S9 R8/R13 require the roster GREEN at the release gate. S8 closed handing S9 a documented
KNOWN-RED baseline (`run_all` TOTAL 4176 / HIGH 3381, journal 2026-07-09) that P1–P4 were never
sanctioned to fix (they built and ran the verification machine). Current content-scope highs
after P4's fix waves:

| Lint | Highs | Class | Fix shape |
|---|---|---|---|
| LINT-10 em-dash budget | ~3,180 | S6-era style backlog (unit=block; quotes/labels exempt) | largely scriptable conversion + review lane |
| LINT-11 pipeline-vocab | 405 | rendered-prose vocabulary (TEACH-02b classes) | editorial micro-rewrites, packetable |
| LINT-3 >3-cases-per-paragraph | 74 | case-wall paragraphs → labeled bullets (S1 A9) | editorial restructure, packetable |
| LINT-7 register coverage | 50 | glossary register coverage flags | review lane |
| LINT-13/14/12 | ~small | PROMO loop-2 in flight; residual = FIX-A1 escalations + serializer FP (code fix owed in `scripts/lint/_common.py::_unquote`) | mechanical |
| LINT-16 case-tables (standalone) | 622 | documented standalone backlog | needs its own triage |
| LINT-4 / LINT-17 | 4 / 3 | small | fold into any wave |

**Ask:** sanction a dedicated pre-gate mechanical/editorial campaign (est. 2–4 windows of
paced fleet work: script-assisted LINT-10 conversion with S1 A7 exemption logic + opus review;
LINT-3/11 editorial packets; LINT-16 triage) — or adjudicate documented thresholds/waivers for
specific classes at the gate. R13 cannot tick "roster 1–30 green" until one of these happens.
