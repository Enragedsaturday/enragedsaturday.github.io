# CSSI — Search & Seizure (study wiki + flashcards)

A federal, **criminal-suppression Fourth Amendment** study wiki for the Certified Search & Seizure
Instructor (CSSI) course, built with [Quartz](https://quartz.jzhao.xyz/). Every case is verified
against CourtListener. Ships with a spaced-repetition flashcard deck (FSRS, 1,176 cards) and a
downloadable Anki deck.

- **Live site:** https://cssi-search-and-seizure.vercel.app
- **Flashcards:** https://cssi-search-and-seizure.vercel.app/flashcards
- **Anki deck (.apkg):** https://cssi-search-and-seizure.vercel.app/static/flashcards/cssi-search-and-seizure.apkg

## How it's built
- Wiki pages live in `content/` (synced from an Obsidian vault).
- Flashcard sources in `flashcard-src/decks/*.json` → `flashcard-src/merge.py` builds
  `quartz/static/flashcards/flashcards.json`; `make_apkg.py` (via `flashcard-src/.venv`) builds the `.apkg`.
- Hosted on **Vercel** — `vercel.json` runs `npx quartz build` → `public/`. **Pushing to `main` auto-deploys.**

## Updating
After editing content or decks (an ingest does this for you):

```sh
cd ~/Projects/cssi-quartz
git add -A && git commit -m "update" && git push
```

Vercel rebuilds and republishes automatically in ~2–3 minutes.

## Fork posture (frozen-and-owned Quartz 4.5.2)

`quartz/` is **owned code**, pinned to Quartz **4.5.2** (S4 · R9, user decision 2026-07-03).
We do **not** take routine upstream merges. Upstream is on Quartz 5, and our explorer,
search, treatment-badge, and casetable patches make a blind merge expensive and risky
(it would silently overwrite the reader-signaling and nav model).

- The `upstream` remote ([jackyzha0/quartz](https://github.com/jackyzha0/quartz)) is kept
  **for reference only** — never `git merge upstream/*`.
- A specific upstream fix is taken by **cherry-pick, case by case**, each with a
  Decision-Log note explaining why it was worth the risk.
- The keep-4.5.2-vs-adopt-5 question is **re-evaluated only at the maintenance loop**
  (GH#2), not opportunistically.

This note exists so a future contributor doesn't "helpfully" merge v5 and undo the fork.

---

Built on [jackyzha0/quartz](https://github.com/jackyzha0/quartz) (MIT) — see the fork posture above before pulling framework updates.
