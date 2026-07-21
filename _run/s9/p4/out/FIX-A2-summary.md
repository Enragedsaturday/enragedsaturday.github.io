# FIX-A2 summary — P4-S8H-001 (s8-hardload-landing, high) — LOOP 2

**Packet:** FIX-A2 · **Lane/model:** FIX-A2 / claude-opus-4-8
**WRITE-SCOPE:** `quartz/components/scripts/` + `quartz/styles/` + `_run/s9/p4/`
**Resolves:** finding `P4-S8H-001` (`_run/s9/p4/out/S8H-ORCH-findings.jsonl`)
**Spec:** S8 R10 / R9(e) — centered + flash + persistent tint on BOTH SPA and hard loads.
**Status:** loop 2 shipped; awaiting orchestrator browser re-verify.

## Loop history
- **Loop 1 (NOT-FIXED, refuted by browser verify):** added a load-path leg that re-ran the
  SPA landing path — `flashTargetBlock` + `scrollIntoView({block:"center"})` — inside a
  `requestAnimationFrame` on DOMContentLoaded/direct. Orchestrator real-Chrome hard reload
  of `/cases/Horton-v.-California#pin-136`: the leg **ran** (`el.classList.contains('s8-target')===true`)
  but the viewport ended at `scrollY=56` with the target at `849px`. Root cause of the
  miss: under `html{scroll-behavior:smooth}` the `scrollIntoView` was an **animated** scroll,
  cancelled almost immediately by in-flight hydration/layout work — the same mechanism that
  killed the browser's native anchor jump.
- **Loop 2 (this):** make the hard-load re-scroll an **atomic** jump so it cannot be
  cancelled.

## Fix (loop 2 — minimal; single file; no CSS change)
The hard-load leg now passes `behavior:"instant"` to `scrollIntoView` (atomic, uncancellable
jump). The `requestAnimationFrame` wrapper is dropped (unnecessary once the jump is instant),
and a `window`-`load` re-assert (`{once:true}`) is added to re-center after late font/image
layout shifts. The SPA leg (`_navigate`) and the same-page click leg keep `behavior` unset
(**smooth**, unchanged).

### Exact diff (current working tree vs HEAD)
```diff
--- a/quartz/components/scripts/spa.inline.ts
+++ b/quartz/components/scripts/spa.inline.ts
@@ -211,6 +211,32 @@ function createRouter() {
 createRouter()
 notifyNav(getFullSlug(window))
 
+// S8 — hard-load deep-link landing. On a fresh (non-SPA) page load the browser
+// performs a native anchor jump to `location.hash`, but `scroll-behavior: smooth`
+// (base.scss) turns it into an animated scroll that the hydration layout shifts
+// from the `nav` listeners above cancel — the viewport is left pinned at the top
+// even though `:target` still matches (so the tint shows but the centered landing
+// is lost). The SPA leg's hash handling never runs on a hard load, so re-run the
+// same landing path to give hard loads the same centered flash + persistent tint
+// as SPA navigations. Crucially, the re-scroll must be an ATOMIC jump
+// (behavior: "instant"): an animated scrollIntoView is killed by the same in-flight
+// hydration/layout work that killed the native jump. The SPA / same-page legs stay
+// smooth. Re-centering is idempotent, so this is correct even when the native jump
+// landed; we also re-assert once on `load` for late font/image layout shifts.
+if (window.location.hash) {
+  const landInitialHash = () => {
+    const el = flashTargetBlock(window.location.hash)
+    el?.scrollIntoView({ block: "center", behavior: "instant" })
+  }
+
+  if (document.readyState === "loading") {
+    document.addEventListener("DOMContentLoaded", landInitialHash, { once: true })
+  } else {
+    landInitialHash()
+  }
+  window.addEventListener("load", landInitialHash, { once: true })
+}
+
 if (!customElements.get("route-announcer")) {
```

### Why this is safe (no regressions)
- **SPA leg** (`_navigate`, `scrollIntoView({block:"center"})` line 111) — smooth, untouched.
- **Same-page click leg** (`createRouter` click handler, lines 177–182) — smooth, untouched.
- **popstate leg** (lines 187–192) — untouched.
- `behavior:"instant"` is applied to the hard-load leg **only**. In the built bundle
  `block:"center"` occurs 3× — the 2 SPA/same-page ones carry no `behavior` (smooth), the 1
  hard-load one carries `behavior:"instant"`.
- **Leg gating:** runs only when `window.location.hash` is set (no scroll-to-top regression
  on hashless hard loads) and only on the load path (DOMContentLoaded-once / direct call /
  `window` load-once); it is never a `nav` listener, so it never re-fires on SPA nav.
- **Double-scroll case:** always re-centers; correct per spec even if the native jump landed.
- `behavior:"instant"` is valid per TS 5.9.2 `lib.dom.d.ts`
  (`type ScrollBehavior = "auto" | "instant" | "smooth"`) — no cast, no type regression.
- Style matches the file: no-semi, double quotes, 2-space indent, reuses `flashTargetBlock`.

## Verification (headless — what I could confirm)
1. **Build:** `npx quartz build` → PASS (`Emitted 2873 files`, `Done processing 724 files`,
   0 errors; only the pre-existing unrelated LaTeX `warn` on U+2014).
2. **Transpiled leg carries the instant flag** (isolated build **and** served on `:8080`):
   ```
   {let z=()=>{Et(window.location.hash)?.scrollIntoView({block:"center",behavior:"instant"})};document.readyState==="loading"?document.addEventListener("DOMContentLoaded",z,{once:!0}):z(),window.addEventListener("load",z,{once:!0})}
   ```
   (`Et` = minified `flashTargetBlock`; `z` = `landInitialHash`.) In the bundle
   `behavior:"instant"` occurs **2×** — 1 is the pre-existing `popover.inline.ts`
   `#popover-internal` scroll (unrelated), 1 is this leg; `block:"center"` occurs **3×**
   (2 smooth SPA/same-page + 1 instant hard-load).
3. **Served on `:8080`:** `GET /postscript.js` carries `block:"center",behavior:"instant"`;
   `GET /cases/Horton-v.-California` → 200 and carries `id="pin-136"`.

### Build-collision incident + recovery (transparency)
My first loop-2 verification build used the default output (`public/`) and **collided with
the coordinator's `:8080` watcher rebuild** — both cleaned `public/` at once →
`ENOTEMPTY: rmdir 'public/cases'`, which transiently corrupted the shared `public/`
(postscript.js missing, `:8080` serving 404s). I recovered it by touching the source once to
trigger a single, uncontested `:8080` hot-rebuild: `public/` repopulated (1220 case files,
`postscript.js` 721754 B) and `:8080` is healthy again (Horton 200, instant flag served).
All subsequent verification used an **isolated** `-o <scratchpad>/verify-public` build that
does not touch `public/`. The coordinator's `:8080` dev server was left running per
instruction. I started/killed no servers of my own this loop.

## What remains for BROWSER verification (orchestrator, in real Chrome)
Headless cannot read the actual post-load viewport `scrollY` or the visual flash. Re-run the
loop-1 repro with cache bypass:
- Hard reload `http://localhost:8080/cases/Horton-v.-California#pin-136` and
  `…/California-v.-Greenwood#pin-40`: assert the pin block is now **centered** (loop-1 was
  `scrollY=56`, `elTop=849`), `:target` **tint persists**, **flash** present on landing.
- Confirm **SPA cross-page** deep-link and **same-page click** landings are unregressed
  (still smooth + centered).
- Confirm **hashless** hard loads still top-land (leg is hash-gated).

## Coverage
- Items assigned: 1 (P4-S8H-001). Examined: 1. Skipped: 0.
- Files changed: `quartz/components/scripts/spa.inline.ts` only (+26 lines, 1 leg). No
  `quartz/styles/` change (`scroll-behavior:smooth` intentionally left intact; only the
  hard-load re-scroll is made `instant`).
