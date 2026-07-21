# S8H orchestrator browser samples (R9 c+e, S4 R2/R4/R5/R6/R12 legs) — 2026-07-21

Lane: claude-fable-5-orchestrator, real Chrome via claude-in-chrome, local build @ localhost:8080
(quartz build --serve, corpus at working tree post-P3).

| Check | Spec | Result | Evidence |
|---|---|---|---|
| SPA deep-link landing (cross-page `#pin-40` click from Abandonment → Greenwood) | S8 R10 / R9(e) | **PASS** | Landed on pin block, persistent tint applied, block in view (scrollIntoView center), history URL correct |
| Same-page tint persistence | S8 R10 | PASS | `.s8-target`/`:target` styling visible on pin-40 block |
| Hard-load deep-link landing (`/cases/Horton-v.-California#pin-136`, also Greenwood#pin-40; reproduced incl. cmd+R reload) | S8 R10 / R9(e) | **FAIL → FINDING P4-S8H-001** | Element exists, `:target` matches (tint would show), but viewport stays at top: measured `scrollY=5`, elTop=899px. Native smooth-scroll anchor jump cancelled during hydration (`scroll-behavior: smooth` on html, base.scss:8; no load-path re-scroll leg in spa.inline.ts — its hash leg runs only on SPA navigations) |
| Popover (S4 R5) | R9(e) | PASS | Hover/click on Greenwood wikilink rendered popover with target-page content; badge popover rendered Verifying Good Law page |
| Treatment tooltip vs projected frontmatter (S4 R6) | R9(e) | PASS | Greenwood badge title: "Good law · content verified 1988-05-16 · treatment checked 2026-06-30" == frontmatter as_of_content/as_of_treatment exactly |
| Search did-you-mean (S4 R4) | R11 | PASS | "Mirranda" → No results + suggestions: Miranda v. Arizona / Miranda Waiver and Invocation / Miranda and Custodial Interrogation |
| Scroll round-trip (S4 R2) | R11 | PASS | Deep-scrolled Abandonment → SPA to Seizure of the Person → browser Back → position restored (same content region) |
| Deck non-breakage (R11/R12 precondition) | R12 | PASS | /flashcards loads: 1,176 cards / 26 subdecks, card front renders, .apkg download link present, FSRS counters live |
| ⚪ unverified banner spot-checks | R13 | PASS (2/2 incidental) | Horton + Ganias both render "This entry has not completed verification — treat as unverified" banner + Unverified pill |
| Fragment end-to-end (`#:~:text=`) sample (R9(c)) | S8 R13(d) | **PARTIAL — see note** | 12-URL sample drawn (logged below). DOM-presence leg verified on live CL for Crews sample: fragment prefix text found verbatim in opinion body (find tool, exact match). VISUAL highlight leg BLOCKED: (i) Chrome does not activate text fragments on extension-programmatic navigations; (ii) omnibox-typed retry tripped CourtListener bot-verification (CAPTCHA) — not bypassed, per policy. Disposition: mechanical fragment→cached-text trace assigned to worker packet S8H-B; visual leg DEFERRED to R15 verify-live (spec already samples fragments there); logged as stated limitation, not a silent pass. |

Fragment sample (12): Horton 112448, Moran 111614, Walter 110314, Crews 110230, NASA 118306,
Grubbs 145670, Strieff 8176208, Dalia 110061, Townsend 106544, Davis 107912, Carney 111423,
Sgro 101970 (URLs in /tmp/frag-sample.txt reproduction: grep ':~:text=' | awk 'NR%19==3').

## FINDING P4-S8H-001 (candidate, class s8-hardload-landing, severity high)
Hard-load navigation to any `#<block-id>` deep link lands at page top (scroll cancelled during
hydration); S8 R10 requires centered + flash + persistent tint on BOTH SPA and hard loads. Tint
half works (:target CSS); scroll half broken. Repro: load
http://localhost:8080/cases/Horton-v.-California#pin-136 fresh → scrollY≈5, target el at ~899px.
Suspected fix shape: a load-path leg (DOMContentLoaded/after-hydration re-scroll to location.hash
target, mirroring spa.inline.ts flashTargetBlock + scrollIntoView) or scroll-behavior guard.
NOT applied — goes through the R4 machine (adjudication then fix packet).
