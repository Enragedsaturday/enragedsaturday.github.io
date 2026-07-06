# CodeRabbit gate — RETRO-W0W1-lint @ 597bb3f (base: main)

- run: 2026-07-06T00:19:52Z
- cli: 0.6.4
- mode: --plain --type committed --base main --dir /var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T//cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint
- scope: .coderabbit.yaml path filters (code only) · restricted to scripts/lint

```
Notice: Detected claude environment. Use `coderabbit review --agent` for structured agent-friendly output.

────────────────────────────────────────
CodeRabbit CLI 0.6.4
What's new

Auth         : SSO and self-hosted login flows are more reliable
Git          : remote detection handles SSH aliases, self-hosted hosts, Bitbucket slugs, and runtime host overrides
────────────────────────────────────────

Connecting to CodeRabbit... 7s elapsed
Preparing review... 9s elapsed
────────────────────────────────────────
CodeRabbit Review

Diff      : committed changes only
Compare   : HEAD → main
Directory : cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint
────────────────────────────────────────

(\(\
(• .•)  Making your code shine like the top of the Chrysler Building.

Preparing sandbox... 10s elapsed
Summarizing changes... 14s elapsed
Summarizing changes... 1m 07s elapsed - still working
Finishing analysis tools... 2m 01s elapsed - still working
Writing review comments... 2m 01s elapsed - still working
Writing review comments... 2m 07s elapsed - still working
Writing review comments... 3m 07s elapsed - still working

────────────────────────────────────────────────────────────────────────
  minor [Maintainability & Code Quality]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/fixtures/lint-3-n5.md:47scripts/lint/fixtures/lint-3-n5.md:47-49]8;;

  Ground the Sources section in every authority mentioned above.

  The body references Torres v. Madrid and Chatrie v. United States, but the
  Sources section only links Riley v. California. Either add the missing
  source entries or trim the body text so the fixture stays internally
  consistent.


────────────────────────────────────────────────────────────────────────
  major [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/lint22_derip.py:46scripts/lint/lint22_derip.py:46-62]8;;

  Add the exact copied surface forms to BANNED_TITLES.

  The docstring names slash-combined originals (What is a Search/Seizure?
  and PC needed / PC not needed), but the list only includes split
  variants. Those originals can still slip past check_label().


  Fix

   BANNED_TITLES = (
  @@
       "What is a Search?",
       "What is a Seizure?",
  +    "What is a Search/Seizure?",
  @@
       "Probable Cause Not Needed",
       "Probable-Cause Exceptions",
       "Suspicion-Based / Per-Se Exceptions",
  +    "PC needed / PC not needed",
   )


────────────────────────────────────────────────────────────────────────
  critical [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/lint21_binding.py:136scripts/lint/lint21_binding.py:136-145]8;;

  slug in slug_map doesn't verify ≥1 valid node — an empty nodes list is
  treated as "bound."

  The docstring's contract (a) requires a live override slug to resolve "to
  >= 1 registry node id via the map." But `slug_map.setdefault(slug,
  []).extend(nodes) will register a key with an empty list if a bound[]`
  row has a missing/empty nodes field, and Line 168's `if slug in
  slug_map: continue` only checks dict-key presence, not that the mapped
  list is non-empty. Such a row silently satisfies the override check with
  zero actual bound nodes — no HIGH is ever raised (the dangling-node loop
  at Lines 159-164 also can't catch it since nothing was added to
  mapped_nodes). This gap isn't covered by the current self-test fixtures.


  🐛 Proposed fix

       for slug, cluster, src in lake_overrides:
  -        if slug in slug_map:
  +        if slug_map.get(slug):
               continue  # bound live (its nodes were dangling-checked above)

  Also applies to: 166-169


────────────────────────────────────────────────────────────────────────
  major [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/lint18_depth.py:64scripts/lint/lint18_depth.py:64-81]8;;

  Fail closed when content_root yields no markdown files.

  check_tree() currently treats a missing/empty content/ tree as success
  because glob.glob(..., recursive=True) returns [] and the loop reports
  no violations. Raise on a missing root or an empty scan so this gate
  cannot certify an empty corpus.


────────────────────────────────────────────────────────────────────────
  major [Stability & Availability]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/lint21_binding.py:75scripts/lint/lint21_binding.py:75-76]8;;

  Unclosed file handle.

  open(f, encoding="utf-8") is never closed. Use a context manager. (The
  static-analysis path-traversal warning on this line is a false positive —
  f comes from glob.glob over a fixed directory, not external input.)


  ♻️ Proposed fix

  -            d = json.load(open(f, encoding="utf-8"))
  +            with open(f, encoding="utf-8") as fh:
  +                d = json.load(fh)


────────────────────────────────────────────────────────────────────────
  critical [Data Integrity & Integration]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/lint21_binding.py:74scripts/lint/lint21_binding.py:74-78]8;;

  Silent skip on unreadable/corrupt lake case files defeats fail-closed
  contract.

  except (OSError, ValueError): continue drops a case file from the scan
  entirely with no violation recorded. A corrupt/unreadable case.json that
  actually carries an unbound override slug will simply vanish from the
  check — an exception is being treated as an empty (passing) result rather
  than surfacing as a lint failure, contrary to the fail-closed mandate for
  this pipeline.


  🛡️ Proposed fix — surface unreadable files as violations instead of
  silently skipping

  -    for f in sorted(glob.glob(os.path.join(lake_dir, "*.json"))):
  -        try:
  -            d = json.load(open(f, encoding="utf-8"))
  -        except (OSError, ValueError):
  -            continue
  +    unreadable = []
  +    for f in sorted(glob.glob(os.path.join(lake_dir, "*.json"))):
  +        try:
  +            with open(f, encoding="utf-8") as fh:
  +                d = json.load(fh)
  +        except (OSError, ValueError):
  +            unreadable.append(f)
  +            continue

  Then propagate unreadable back to check_binding/run as HIGH
  violations rather than dropping it.


  As per path instructions, "Flag any path where an exception or empty
  result could be recorded as a verified state."


────────────────────────────────────────────────────────────────────────
  minor [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/lint18_depth.py:50scripts/lint/lint18_depth.py:50-52]8;;

  Scope paths to content_root before depth checks

  iter_markdown_files(paths) can yield absolute .md files outside
  content_root, so _check_path() will see ../... segments and miss
  EXEMPT_TOP while applying the wrong depth count. Skip non-descendants of
  content_root or normalize paths to that root first.
  scripts/lint/lint18_depth.py:47-72


────────────────────────────────────────────────────────────────────────
  minor [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/lint19_overview.py:65scripts/lint/lint19_overview.py:65-80]8;;

  Exclude table rows from the prose counter.

  The current loop treats every non-heading, non-blank line as prose, so a
  table-only body can satisfy MIN_PROSE_LINES and pass as non-stub. That
  weakens the overview check.


────────────────────────────────────────────────────────────────────────
  major [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/lint19_overview.py:47scripts/lint/lint19_overview.py:47-54]8;;

  Scope the cases exemption to the landing page only.

  rel.split("/")[0] == "cases" suppresses every content/cases//index.md,
  but the spec only exempts content/cases/index.md. Nested overview pages
  under content/cases/ would be skipped entirely.


  Proposed fix

  -    if rel.split("/")[0] == "cases":  # cases/index.md — R13(d) router landing
  +    if rel == "cases/index.md":  # only the router landing is exempt
           return False

  As per path instructions, prioritize correctness of
  comparison/normalization logic.


────────────────────────────────────────────────────────────────────────
  minor [Maintainability & Code Quality]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/README.md:34scripts/lint/README.md:34]8;;

  Runner row understates coverage — omits LINT-18 through LINT-25.

  The description says the runner covers lints (2–10, 26), but
  run_all.py's LINTS roster also runs LINT-18, 19, 20, 21, 22, 23, 24,
  and 25. Update the row so the README matches the actual roster.





  📝 Suggested wording

  -| `run_all.py` | runner | — | Runs the **non-CL** lints (2–10, 26) over `content/`, LINT-10 self-test first (fail-closed), and prints a per-lint violation summary. |
  +| `run_all.py` | runner | — | Runs the **non-CL** lints (2–10, 18–26) over `content/` (plus the S3 repo scans), LINT-10 self-test first (fail-closed), and prints a per-lint violation summary. |


────────────────────────────────────────────────────────────────────────
  minor [Maintainability & Code Quality]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/run_all.py:3scripts/lint/run_all.py:3-6]8;;

  Docstring roster is stale — omits LINT-18 through LINT-25.

  The header enumerates (LINT-2,3,4,5,6,7,8,9,10 + LINT-26), but the
  LINTS roster (Lines 61-68) also runs LINT-18, 19, 20, 21, 22, 23, 24,
  and 25. A reader relying on this docstring will underestimate what the
  runner actually executes.





  📝 Suggested wording

  -Runner for the NON-CL CSSI lints (LINT-2,3,4,5,6,7,8,9,10 + LINT-26) over
  -content/. LINT-10's fixture self-test runs first, fail-closed (S1 A3). The
  +Runner for the NON-CL CSSI lints (LINT-2..10, LINT-18..26) over content/ and
  +the S3 repo scans. LINT-10's fixture self-test runs first, fail-closed (S1 A3).
  +The


────────────────────────────────────────────────────────────────────────
  major [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/lint4_lexicon.py:382scripts/lint/lint4_lexicon.py:382-396]8;;

  Lane (b) should skip fenced code blocks in
  scripts/lint/lint4_lexicon.py:217-233, 382-396.

  _table_rows() has no fenced-block guard, so a markdown example table
  inside a ``` fence can still be parsed as a real authority table and emit
  a spurious HIGH violation. Reuse the existing fenced set here, or switch
  lane (b) to c.iter_tables().


────────────────────────────────────────────────────────────────────────
  major [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/lint24_urls.py:150scripts/lint/lint24_urls.py:150-159]8;;

  Fail-open: an inventory whose paths are all non-string silently PASSES.

  paths is validated as a non-empty list at Line 134, but the resolution
  loop continues on every non-str entry. If the artifact contains only
  non-string entries (e.g. paths: [123, 456] or a list of objects), the
  loop checks nothing, out stays empty, and check (A) reports a
  verified/clean state despite resolving zero URLs. That is exactly the
  "empty result recorded as a verified state" hazard for a fail-closed gate.

  As per path instructions: "Flag any path where an exception or empty
  result could be recorded as a verified state."





  🛡️ Proposed fail-closed fix

       routes = emitted_routes(public_root)
       out = []
  +    checked = 0
       for p in paths:
           if not isinstance(p, str):
  +            out.append(c.make_violation(
  +                LINT, inventory_path, 1, c.HIGH,
  +                "url-inventory contains a non-string path entry %r — malformed "
  +                "artifact (fail-closed) [R13/A1]" % (p,)))
               continue
  +        checked += 1
           if normalize_url(p) not in routes:
               out.append(c.make_violation(
                   LINT, inventory_path, 1, c.HIGH,
                   "inventory path %r (normalized %r) resolves to no emitted page or "
                   "alias redirect in the build output — a pre-O2 URL that now 404s "
                   "(fail-closed) [R13/A1]" % (p, normalize_url(p))))
  +    if checked == 0:
  +        out.append(c.make_violation(
  +            LINT, inventory_path, 1, c.HIGH,
  +            "url-inventory has no checkable string paths — fail-closed [R13/A1]"))
       return out


────────────────────────────────────────────────────────────────────────
  minor [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/lint26_goodlaw_target.py:113scripts/lint/lint26_goodlaw_target.py:113-132]8;;

  Match Quartz's _index suffix handling slugifyFilePath() rewrites any
  slug ending in _index (foo_index → fooindex), not just a final
  /_index segment. _quartz_full_slug() should mirror that string-level
  behavior to avoid wrong FullSlug matches.


────────────────────────────────────────────────────────────────────────
  minor [Stability & Availability]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/lint7_glossary.py:63scripts/lint/lint7_glossary.py:63-67]8;;

  Broaden the register-read guard in scripts/lint/lint7_glossary.py:63-67
  to stay fail-closed on unreadable UTF-8.

  c.read_text(path) can raise UnicodeDecodeError (a ValueError), which
  escapes except OSError and turns a bad register into a crash instead of
  the intended fail-closed violation.


────────────────────────────────────────────────────────────────────────
  major [Data Integrity & Integration]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/lint20_points.py:137scripts/lint/lint20_points.py:137-144]8;;

  Malformed also_on silently skips validation instead of flagging it.

  Only isinstance(also, list) entries are checked, and within that only
  isinstance(ao, str) items are validated. A registry node with also_on
  set to a non-list (e.g. a bare string) or containing non-string entries
  produces zero violations for that field — i.e., malformed data passes as
  "verified" rather than being fail-closed flagged. Given this script's
  stated FAIL-CLOSED design, these should be surfaced as HIGH violations
  rather than silently ignored.





  🛡️ Proposed fix to flag malformed also_on

           also = node.get("also_on")
  -        if isinstance(also, list):
  +        if also is not None and not isinstance(also, list):
  +            out.append(c.make_violation(
  +                LINT, registry_path, 1, c.HIGH,
  +                "%s: also_on must be a list [R4]" % where))
  +        elif isinstance(also, list):
               for ao in also:
  -                if isinstance(ao, str) and ao.strip() and not _resolve_on_disk(ao):
  +                if not (isinstance(ao, str) and ao.strip()):
  +                    out.append(c.make_violation(
  +                        LINT, registry_path, 1, c.HIGH,
  +                        "%s: also_on entry %r is not a non-empty string [R4]"
  +                        % (where, ao)))
  +                elif not _resolve_on_disk(ao):
                       out.append(c.make_violation(
                           LINT, registry_path, 1, c.HIGH,
                           "%s: also_on entry %r does not resolve on disk [R4]"
                           % (where, ao)))


────────────────────────────────────────────────────────────────────────
  major [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/lint25_deck.py:60scripts/lint/lint25_deck.py:60-76]8;;

  Malformed/schema-invalid deck JSON is silently dropped instead of failing
  closed.

  deck_stems swallows json.load failures (Line 66-67) and non-list
  cards (Line 69-70) with a bare continue. check_decks only fails when
  the entire extracted set is empty (Line 123-127); if one deck file among
  several is corrupted or has an unexpected shape while its siblings parse
  fine, that file's cards are silently excluded from the audit — a
  broken/frozen deck could sail through the FAIL-CLOSED lint with zero
  violations. This is precisely the pattern called out for scripts under
  this path: an exception here is effectively recorded as a verified/clean
  state instead of a failure.


  🛡️ Proposed fix: surface per-file failures as HIGH violations

  -def deck_stems(decks_dir):
  -    """Union of `page` stems across every deck JSON (A2 extraction set)."""
  +def deck_stems(decks_dir, errors=None):
  +    """Union of `page` stems across every deck JSON (A2 extraction set).
  +    Appends (path, reason) to `errors` for any file that fails to parse or
  +    lacks a valid card list, so callers can fail closed on them."""
       stems = set()
       for f in sorted(glob.glob(os.path.join(decks_dir, "*.json"))):
           try:
               d = json.load(open(f, encoding="utf-8"))
  -        except (OSError, ValueError):
  +        except (OSError, ValueError) as e:
  +            if errors is not None:
  +                errors.append((f, "parse error: %s" % e))
               continue
           cards = d if isinstance(d, list) else d.get("cards") if isinstance(d, dict) else None
           if not isinstance(cards, list):
  +            if errors is not None:
  +                errors.append((f, "no card list found"))
               continue
           for card in cards:
               if isinstance(card, dict) and isinstance(card.get("page"), str):
                   p = card["page"].strip()
                   if p:
                       stems.add(p)
       return stems

   def check_decks(decks_dir, content_root, spec_path=None):
       stems = deck_stems(decks_dir)
  +    errors = []
  +    stems = deck_stems(decks_dir, errors)
  +    out = [c.make_violation(LINT, f, 1, c.HIGH,
  +                             "deck file failed to load (%s) — fail-closed [R14/A2]" % reason)
  +           for f, reason in errors]
       if not stems:
  -        return [c.make_violation(
  +        return out + [c.make_violation(
               LINT, decks_dir, 1, c.HIGH,
               "no deck `page` stems extracted from %s — the frozen deck's join key "
               "is absent (fail-closed) [R14/A2]" % c.relpath(decks_dir))]

  As per path instructions, "Flag any path where an exception or empty
  result could be recorded as a verified state."





  Also applies to: 119-130

Writing review comments... 8m 49s elapsed - still working - 17 findings so far

────────────────────────────────────────────────────────────────────────
  major [Security & Privacy]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/lint16_casetables.py:83scripts/lint/lint16_casetables.py:83-94]8;;

  _host() host-extraction can be bypassed via URL userinfo, defeating the
  R17 whitelist.

  re.match(r"https?://([^/]+)", url) captures everything up to the first
  /, including any userinfo component, and .split(":")[0] then takes the
  username portion when the URL contains user:pass@host. For a URL like
  https://www.courtlistener.com:x@evil.com/fake, this returns
  "www.courtlistener.com" — which passes _host_ok() — while the
  browser/HTTP client would actually resolve evil.com as the host. This is
  exactly the "no broad accept" guarantee the docstring calls out
  (OPINION_HOST_WHITELIST, Lines 47-49: an "EXACT host set"), and the
  exploit bypasses it entirely.

  As per path instructions, "correctness of comparison / normalization
  logic" is a priority for scripts/, and this false-positive host match
  lets non-whitelisted content pass the R17 check silently.


  🛡️ Proposed fix using urllib.parse

  +from urllib.parse import urlsplit
  +
   def _host(url):
  -    m = re.match(r"https?://([^/]+)", url.strip())
  -    if not m:
  -        return ""
  -    return m.group(1).lower().split(":")[0]
  +    try:
  +        parsed = urlsplit(url.strip())
  +    except ValueError:
  +        return ""
  +    if parsed.scheme not in ("http", "https"):
  +        return ""
  +    return (parsed.hostname or "").lower()

  As per path instructions, scripts/ tooling should prioritize
  "correctness of comparison/normalization logic," and this URL-parsing gap
  allows an unwhitelisted host to be recorded as verified.

Writing review comments... 10m 01s elapsed - still working - 18 findings so far

────────────────────────────────────────────────────────────────────────
  major [Data Integrity & Integration]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-lint-TJ5Nfa/scripts/lint/lint16_casetables.py:228scripts/lint/lint16_casetables.py:228-261]8;;

  Flag short rows and hostless opinion URLs
  - iter_tables() still admits rows that are one cell shorter than the
  header, so a row missing the final Opinion/Primary home cell reaches
  this code and skips the targeted checks entirely.
  - MDLINK_URL_RE already excludes relative links, but
  https:///...-style URLs still match; _host() returns "" and the
  whitelist check is bypassed.

  Treat those cases as violations so malformed case rows can’t pass clean.


────────────────────────────────────────
Review complete
19 findings ✔

Critical 2
Major    10
Minor    7
────────────────────────────────────────

Print all AI prompts: coderabbit review --show-prompts
```
