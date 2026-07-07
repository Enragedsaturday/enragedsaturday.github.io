# CodeRabbit gate — S6-R8PIPE @ da8adb3 (base: HEAD~1)

- run: 2026-07-07T11:54:11Z
- cli: 0.6.4
- mode: --plain --type committed --base origin/HEAD~1 --dir /var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T//cr-gate-S6-R8PIPE-ZfDDeP/scripts
- scope: .coderabbit.yaml path filters (code only) · restricted to scripts

```
Notice: Detected claude environment. Use `coderabbit review --agent` for structured agent-friendly output.
Connecting to CodeRabbit... 20s elapsed
Preparing review... 22s elapsed
────────────────────────────────────────
CodeRabbit Review

Diff      : committed changes only
Compare   : HEAD → origin/HEAD~1
Directory : cr-gate-S6-R8PIPE-ZfDDeP/scripts
────────────────────────────────────────

(\(\
(• .•)  C*deR*bb*t: The uncensored bug hunter.

Preparing sandbox... 23s elapsed
Summarizing changes... 36s elapsed
Summarizing changes... 1m 20s elapsed - still working
Summarizing changes... 2m 20s elapsed - still working
Summarizing changes... 3m 20s elapsed - still working
Finishing analysis tools... 4m 10s elapsed - still working
Writing review comments... 4m 10s elapsed - still working
Writing review comments... 4m 20s elapsed - still working
Writing review comments... 5m 20s elapsed - still working
Writing review comments... 6m 20s elapsed - still working

────────────────────────────────────────────────────────────────────────
  minor [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/lint/lint14_pagerecord.py:61scripts/lint/lint14_pagerecord.py:61-63]8;;

  or fallback masks an explicitly empty record_id in page frontmatter.

  If a page sets lake: {record_id: ""} (empty string, a plausible
  authoring mistake), the falsy check silently falls back to the filename
  stem instead of flagging the malformed override. This is exactly the kind
  of "empty result recorded as verified state" the fail-closed mandate warns
  against.


  Proposed fix

   def page_record_id(path, fm):
       lake = fm.get("lake") if isinstance(fm.get("lake"), dict) else {}
  -    return lake.get("record_id") or os.path.splitext(os.path.basename(path))[0]
  +    rid = lake.get("record_id")
  +    if rid is None:
  +        return os.path.splitext(os.path.basename(path))[0]
  +    return rid

  As per path instructions, "Prioritize: fail-closed behavior (errors must
  never pass silently as success)... correctness of comparison/normalization
  logic."


────────────────────────────────────────────────────────────────────────
  major [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/lint/lint24_urls.py:180scripts/lint/lint24_urls.py:180-221]8;;

  Retired-path check misses wikilink-syntax related:/homes: values.

  _retired_in matches _RETIRED_SEG_RE, which requires the prefix be
  preceded by start-of-string or /. When a homes:/related: frontmatter
  value is written as a wikilink string (e.g.
  "[[7-exceptions-warrant/Automobile Exception]]", as in
  lint-24-oldpath-fail.md line 6), the prefix is preceded by [[, so the
  regex never matches and the reference silently passes. Body wikilinks are
  correctly unwrapped before matching
  (m.group(1).split("|")[0].split("#")[0] at Line 213), but frontmatter
  values aren't. The self-test still reports "high" for this fixture only
  because the sibling homes: value (a bare path, no brackets)
  independently trips a violation — the related: miss is masked.

  This directly undermines the R13(c) guarantee "Zero references to any of
  the 12 retired numbered top-level folders remain in source," since a
  wikilink-style related:/homes: entry is recorded as clean.


  🛡️ Proposed fix: unwrap wikilink syntax before matching

   def _retired_in(value):
       """Return the retired prefix found as a path segment in `value`, or None."""
       if not isinstance(value, str):
           return None
  -    m = _RETIRED_SEG_RE.search(value)
  +    v = value.strip()
  +    wl = re.match(r"^\[\[(.*?)\]\]$", v)
  +    if wl:
  +        v = wl.group(1).split("|")[0].split("#")[0].strip()
  +    m = _RETIRED_SEG_RE.search(v)
       return m.group(1) if m else None

  As per path instructions for scripts/: "Flag any path where an exception
  or empty result could be recorded as a verified state."


────────────────────────────────────────────────────────────────────────
  minor [Stability & Availability]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/gates/coderabbit_gate.sh:33scripts/gates/coderabbit_gate.sh:33]8;;

  CR_GATE_TIMEOUT=0 silently disables the alarm.

  ${CR_GATE_TIMEOUT:-3600} only defaults on unset/empty, so an explicit
  0 (or a non-numeric value that perl coerces to 0) reaches alarm 0,
  which cancels the timer. That defeats the documented "can never hang a
  session" guarantee (Lines 20-21). A trivial guard preserves the invariant.






  🛡️ Reject non-positive/non-numeric timeouts

   CR_GATE_TIMEOUT="${CR_GATE_TIMEOUT:-3600}"
  +case "$CR_GATE_TIMEOUT" in
  +  ''|*[!0-9]*|0) echo "coderabbit_gate: CR_GATE_TIMEOUT must be a positive integer" >&2; exit 2 ;;
  +esac


────────────────────────────────────────────────────────────────────────
  major [Data Integrity & Integration]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/lint/lint13_schema.py:25scripts/lint/lint13_schema.py:25-53]8;;

  Unsupported format values silently pass validation instead of failing
  closed.

  unsupported_schema_keywords()/self-test only verify that schema keyword
  names are covered, not that format values used in the schema are
  supported. format_matches() (lines 245-264) explicitly returns True
  for any format other than date/date-time/uri (line 264). If
  _overhaul2/lake/_schema.json ever adds e.g. "format": "email" or
  "uuid" to a field, this validator will silently accept any string for
  that field — with no self-test failure to flag the gap — undermining the
  "fail-closed" guarantee this lint exists to enforce for the authority
  lake.


  🔧 Proposed fix: track supported format values and fail closed on unknowns

  +SUPPORTED_FORMATS = {"date", "date-time", "uri"}
  +
  +
  +def schema_formats(schema):
  +    formats = set()
  +
  +    def walk(node):
  +        if isinstance(node, list):
  +            for item in node:
  +                walk(item)
  +            return
  +        if not isinstance(node, dict):
  +            return
  +        for key, value in node.items():
  +            if key == "format" and isinstance(value, str):
  +                formats.add(value)
  +            ...
  +    walk(schema)
  +    return formats
  +
   def unsupported_schema_keywords(schema):
       return sorted(schema_keywords(schema) - SUPPORTED_SCHEMA_KEYWORDS)
  +
  +
  +def unsupported_schema_formats(schema):
  +    return sorted(schema_formats(schema) - SUPPORTED_FORMATS)

  Then check unsupported_schema_formats(schema) in both run() and
  self_test() the same way unsupported_schema_keywords is checked, and
  have format_matches return False (not True) for unrecognized formats
  as a defensive fallback.





  As per path instructions, "Flag any path where an exception or empty
  result could be recorded as a verified state" for scripts/.


  Also applies to: 95-96, 245-264


────────────────────────────────────────────────────────────────────────
  major [Data Integrity & Integration]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/lint/lint13_schema.py:283scripts/lint/lint13_schema.py:283-296]8;;

  Missing/empty lake/cases directory silently yields zero violations.

  glob.glob() returns [] without error if _overhaul2/lake/cases
  doesn't exist or is empty (e.g., due to a path typo, accidental deletion,
  or a broken upstream ingest step). Unlike the manifest load a few lines
  below (which raises and is caught as a violation), this loop simply
  produces no output in that case — the lint would report "0 violations" for
  a lake with no case records at all, which could be interpreted as
  verified/passing rather than flagged as suspicious.


  🔧 Proposed fix: assert the directory exists / fail if no case files found

       case_paths = sorted(glob.glob(os.path.join(c.REPO_ROOT, "_overhaul2", "lake", "cases", "*.json")))
  +    cases_dir = os.path.join(c.REPO_ROOT, "_overhaul2", "lake", "cases")
  +    if not os.path.isdir(cases_dir):
  +        out.append(v(cases_dir, "lake/cases directory is missing"))
  +    elif not case_paths:
  +        out.append(v(cases_dir, "lake/cases directory contains no record JSON files"))
       ids = []

  As per path instructions, "Flag any path where an exception or empty
  result could be recorded as a verified state" for scripts/.


────────────────────────────────────────────────────────────────────────
  major [Security & Privacy]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/lint/_common.py:647scripts/lint/_common.py:647-686]8;;

  Normalize dash variants in weight_label_in_cell. Exact — matching
  means labels written with - or – return None, so LINT-16 can treat a
  leaked label as clean.

Writing review comments... 8m 46s elapsed - still working - 6 findings so far

────────────────────────────────────────────────────────────────────────
  minor [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/s2/serializer.py:202scripts/s2/serializer.py:202-214]8;;

  Empty top-level dict serializes to key: (parses back as null), not `key:
  {}`.

  Empty lists are special-cased (key: []), but an empty dict value falls
  through to Line 210 and emits a bare key: with no children. When that
  output is re-parsed, key: becomes null, not an empty mapping — so
  canonicalize({}) vs canonicalize(None) will report drift for managed
  dict keys (e.g. lake, treatment, courtlistener). This mirrors the
  empty-dict handling already present in _dump_yaml_lines and also affects
  replace_frontmatter, which renders each key through this same body
  helper.





  🐛 Proposed fix

       for key, value in frontmatter.items():
           if isinstance(value, (dict, list)):
               rendered = _dump_yaml_lines(value, 2)
               if isinstance(value, list) and not value:
                   lines.append("%s: []" % key)
  +            elif isinstance(value, dict) and not value:
  +                lines.append("%s: {}" % key)
               else:
                   lines.append("%s:" % key)
                   lines.extend(rendered)


────────────────────────────────────────────────────────────────────────
  major [Data Integrity & Integration]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/s6/fixtures/worklist-fixture.json:32scripts/s6/fixtures/worklist-fixture.json:32-39]8;;

  Align the worklist status with the paired stub.

  Row 3 still marks fixture-wrongstatus--900003 as verified_identity,
  but the paired stub is explicitly status: "not_found" with
  identity_method: "none" and no cluster/opinion IDs. That turns the
  negative-path fixture into a promotable record and weakens the fail-closed
  gate.


  Proposed fix

  -      "status_checked": "verified_identity"
  +      "status_checked": "not_found"


────────────────────────────────────────────────────────────────────────
  major [Data Integrity & Integration]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/lint/lint21_binding.py:139scripts/lint/lint21_binding.py:139-166]8;;

  Reject malformed binding rows instead of normalizing them away.

  bound/pending are coerced to [] when they are missing or the wrong
  type, and non-string nodes entries are silently dropped from
  mapped_nodes. That lets a broken binding file disappear from both the
  live-slug check and the dangling-node check, so the gate can pass on
  malformed input whenever the current lake snapshot doesn't exercise it.


  🔧 Suggested fix

  -    bound = doc.get("bound") if isinstance(doc.get("bound"), list) else []
  -    pending = doc.get("pending") if isinstance(doc.get("pending"), list) else []
  +    if not isinstance(doc.get("bound"), list) or not isinstance(doc.get("pending"), list):
  +        return [c.make_violation(
  +            LINT, binding_path, 1, c.HIGH,
  +            "binding map has invalid bound/pending structure [R5]")]
  +    bound = doc["bound"]
  +    pending = doc["pending"]

  Also reject any nodes entry that is not a string instead of skipping it.


────────────────────────────────────────────────────────────────────────
  major [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/lint/run_all.py:99scripts/lint/run_all.py:99-110]8;;

  Self-test rows lose per-lint identity — hardcoded "SELFTEST" name.

  lint_name is unpacked from SELF_TESTS and correctly used in
  c.make_violation, but rows.append hardcodes the literal "SELFTEST"
  instead of lint_name. All four self-test rows (LINT-10/12/13/14) end up
  identically labeled in both the printed roster table and the
  --summary-json output ("lint": "SELFTEST"), making it impossible to
  tell which self-test failed from the summary alone (especially with
  --quiet, where the per-violation JSON line carrying the real lint_name
  is suppressed).


  🐛 Proposed fix

  -        rows.append(("SELFTEST", desc, len(selftest_viols), st_high, 0, 0))
  +        rows.append((lint_name, desc, len(selftest_viols), st_high, 0, 0))


────────────────────────────────────────────────────────────────────────
  minor [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/lint/lint22_derip.py:46scripts/lint/lint22_derip.py:46-65]8;;

  Keep the banned-title normalization aligned with folder-derived labels.

  _folder_display_name() turns probable-cause-exceptions into `probable
  cause exceptions, but _norm()` currently leaves hyphens/underscores
  intact. That means titleless pages under the retired folders will never
  match these banned entries.


  Proposed fix

   def _norm(s):
  -    return re.sub(r"\s+", " ", (s or "").strip().lower())
  +    return re.sub(r"[\s\-_]+", " ", (s or "").strip().lower())


────────────────────────────────────────────────────────────────────────
  major [Data Integrity & Integration]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/s2/project.py:300scripts/s2/project.py:300-332]8;;

  Uncaught project_record exception mid-write-loop can leave a
  partially-projected corpus without a clean gate summary.

  authority_weight() (lines 126-151) raises ValueError for COA records
  with a missing/unrecognized circuit, and this is invoked from
  project_record() (line 316) inside this loop, after the a13 gate has
  already passed. Since a13_gate() never calls project_record() to
  pre-validate, a bad record only surfaces once the write loop reaches it —
  by which point earlier pages in the loop may already have been rewritten
  via os.replace (line 332). The run then dies with a bare traceback
  instead of the structured refused/exit-code-2 path the rest of the tool
  uses for bad data, leaving operators without a clear signal about which
  pages were and weren't updated.

  Consider validating project_record(record) for every matched record
  before any writes occur (similar to how a13_gate accumulates
  unmapped/missing/unmatched), so a bad circuit value blocks the whole
  batch cleanly instead of causing a partial, mid-run crash.


────────────────────────────────────────────────────────────────────────
  major [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/s2/project.py:73scripts/s2/project.py:73-77]8;;

  Non-deterministic fallback breaks idempotence guarantee.

  date_from_record() falls back to dt.date.today() when a record lacks
  (or has a malformed) provenance.date_modified, and this value is written
  into lake.projected_at. For any such record, every run on a new day
  produces a fresh "diff" purely from the date change, defeating the
  idempotence contract this tool explicitly tests via
  verify_idempotent()/self_test(). Since the rest of the file treats
  malformed/missing critical fields as fail-closed conditions (e.g.
  authority_weight raises rather than guessing), this fallback is
  inconsistent with that posture.

  As per path instructions, "resumability/idempotence" and "correctness of
  ... normalization logic" should be prioritized for scripts/.


  🔧 Suggested fix: fail closed instead of guessing today's date

   def date_from_record(record):
       modified = record.get("provenance", {}).get("date_modified")
       if isinstance(modified, str) and len(modified) >= 10:
           return modified[:10]
  -    return dt.date.today().isoformat()
  +    rid = record.get("record_id") or "<unknown>"
  +    raise ValueError(
  +        "record %r lacks provenance.date_modified; fill it before projection" % rid
  +    )


────────────────────────────────────────────────────────────────────────
  major [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/lint/lint15_skeleton.py:176scripts/lint/lint15_skeleton.py:176-179]8;;

  Case-type draft stubs have no analog to the doctrine placed-stub
  exemption.

  check_doctrine exempts a status: draft page with zero H2 headings (S3
  R7 placed stub) at Line 178. check_case has no equivalent — a
  freshly-placed type: case stub with no H2s yet will hit `titles !=
  BIRAC` and always emit a violation, even though it's not yet authored.
  This is inconsistent with the documented intent that "placed nodes fail
  LINT-15 only once authored."


  🔧 Proposed fix

  -def check_case(path, body, start):
  +def check_case(path, body, start, fm):
       out = []
       body_lines = body.split("\n")
  +    h2s = _h2_titles(body_lines)
  +    if str(fm.get("status", "")).strip().lower() == "draft" and not h2s:
  +        return []
       titles = [t for (_i, t) in _h2_titles(body_lines)]

       if ptype == "case":
  -        return check_case(path, body, start)
  +        return check_case(path, body, start, fm)

  Also applies to: 260-276, 298-299

Writing review comments... 12m 49s elapsed - still working - 14 findings so far

────────────────────────────────────────────────────────────────────────
  major [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/s2/ingest.py:522scripts/s2/ingest.py:522-536]8;;

  Handle cadc/cafc in parse_circuit

  parse_circuit() recognizes D.C. and federal, but CourtListener uses
  the slugs cadc and cafc for those circuits. Add those two values here
  so circuit-based matching/filtering doesn’t drop them to None.


────────────────────────────────────────────────────────────────────────
  major [Data Integrity & Integration]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/s5/convert_tables.py:129scripts/s5/convert_tables.py:129-154]8;;

  Per-row blank Opinion cells are silently blank-filled, not deferred.

  The table-level guard at Line 133 (if "opinion" in missing) only catches
  a missing Opinion column. If the column exists but an individual row's
  cell is empty, normalize_opinion_cell("") (Line 89-91) returns "" and
  the row is rewritten as schema-conformant with a blank Opinion cell — the
  exact "laundering a missing source" failure mode described in the comment
  at Line 129-132, just at row granularity instead of table granularity. No
  fixture covers this path.






  🛡️ Proposed fix: defer the whole table if any row's Opinion cell is blank

  -        new_rows = ["| " + " | ".join(headers) + " |",
  -                    "|" + "|".join(["---"] * len(headers)) + "|"]
  -        for ridx in rows:
  -            src = c.split_table_row(body_lines[ridx])
  -            cells = []
  -            for role in order:
  -                val = src[col_of[role]] if (role in col_of and col_of[role] < len(src)) else ""
  -                if role == "opinion":
  -                    val = normalize_opinion_cell(val)
  -                cells.append(val)
  -            new_rows.append("| " + " | ".join(cells) + " |")
  +        row_data = []
  +        blank_opinion_lines = []
  +        for ridx in rows:
  +            src = c.split_table_row(body_lines[ridx])
  +            cells = []
  +            for role in order:
  +                val = src[col_of[role]] if (role in col_of and col_of[role] < len(src)) else ""
  +                if role == "opinion":
  +                    val = normalize_opinion_cell(val)
  +                    if val == "":
  +                        blank_opinion_lines.append(ridx + 1)
  +                cells.append(val)
  +            row_data.append(cells)
  +
  +        if blank_opinion_lines:
  +            plans[hidx] = (None, None, {
  +                "pass": "tables",
  +                "reason": "blank-opinion-cell",
  +                "detail": "Case table has an Opinion column but row(s) at "
  +                          "line(s) %s carry no link — deferred (opinion links "
  +                          "must be sourced, never blank-filled)" % blank_opinion_lines,
  +                "line": hidx + 1,
  +            }, end)
  +            continue
  +
  +        new_rows = ["| " + " | ".join(headers) + " |",
  +                    "|" + "|".join(["---"] * len(headers)) + "|"]
  +        for cells in row_data:
  +            new_rows.append("| " + " | ".join(cells) + " |")


────────────────────────────────────────────────────────────────────────
  major [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/s5/convert_tables.py:435scripts/s5/convert_tables.py:435-448]8;;

  Reported line numbers are off by the frontmatter length.

  convert_tables/convert_frontier/convert_sources/convert_pitfalls
  all compute "line" from body_lines indices (post-frontmatter), never
  adding len(prefix). Every actions/deferred entry therefore reports a
  line number that's short by the frontmatter's line count on any page with
  frontmatter — the report this pipeline exists to hand to S7 for human
  judgment points at the wrong line.






  🛡️ Proposed fix: offset all reported line numbers by the frontmatter
  length

       body_lines = convert_tables(body_lines, report)
       body_lines = convert_frontier(body_lines, report)
       body_lines = convert_sources(body_lines, report)
       body_lines = convert_pitfalls(body_lines, report)
   
  +    offset = len(prefix)
  +    for entry in report["actions"] + report["deferred"]:
  +        if "line" in entry:
  +            entry["line"] += offset
  +
       new_text = "\n".join(prefix + body_lines)
       report["changed"] = new_text != text
       return report, new_text


────────────────────────────────────────────────────────────────────────
  minor [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-R8PIPE-ZfDDeP/scripts/s6/mint_page.py:744scripts/s6/mint_page.py:744-803]8;;

  homes_roles_desync check can break the documented idempotent no-op
  guarantee.

  The bijection check runs unconditionally before the old_exists branch
  that classifies the row as already-authored/crash-tail/wedged/fresh. If a
  row is already fully authored (page + lake rename + manifest + ledger all
  landed) but the worklist's homes/roles for that record_id are later
  edited into a desynced state, a re-run that should hit the clean
  already_authored no-op path (Lines 772-774) instead refuses with
  REFUSE_HOMES_ROLES_DESYNC — contradicting the stated "Re-running an
  already-promoted row is a clean already-authored no-op (S6 R8
  resumability)" contract (Line 34-35).

  Move the desync check after the already-authored/crash-tail classification
  (or skip it once old_exists is False and the promoted record is found),
  so a fully-completed row's idempotent no-op is never disturbed by later
  worklist edits.


────────────────────────────────────────
Review complete
18 findings ✔

Major    13
Minor    5
────────────────────────────────────────

Print all AI prompts: coderabbit review --show-prompts
```
