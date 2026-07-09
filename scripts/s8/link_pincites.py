#!/usr/bin/env python3
"""
S8 split-pincite wiring pass (spec R4/R5; SD5/SD6). GATED, DRY-RUN BY DEFAULT.

Reads the validated external text-fragments the lake now carries
(`pinpoints[].fragment`, landed by `scripts/s2/ingest.py --apply-fragments`) and
wires them into reader-facing content as R4 split pincites:

  * CASE PAGES — for every end-of-block `^pin-N` whose pin carries a validated
    fragment, the block's own citation line gets the external fragment link:
        — 569 U.S. at 6        ->  — [569 U.S. at 6](CL-URL#:~:text=...)
    (whole-cite wrap, exactly as exhibited on Jardines/Walker). Three cite forms:
      `clean`      : `— <reporter|Id.> at <page>`      -> wrap the whole cite
      `id-nopage`  : `— *Id.*` (no page on the line)   -> wrap the `*Id.*`
      `slip-paren` : `— *Id.* (slip op., at <page>)`   -> wrap the inner page
    A pin without a validated fragment leaves its citation line untouched.

  * DOCTRINE SIDE — outside the R2 exemption zones (scripts/s8/zones.py), pincites
    adjacent to case links get the split treatment (page numbers external, name
    half internal-deep). Rule 1: name-half already `[[Case#^pin-N|…]]` -> wire the
    pincite page with THAT pin's fragment (validated) else plain external. Rule 2:
    page-level/plain name-half + a quotation in the sentence -> UNIQUE quote match
    against the case's pin quotes upgrades the name-half to `#^pin-N` and
    fragment-links the pincite; no/multi match -> leave name-half + plain external
    + journal. Rule 3: paraphrase (no quotation) -> pincite plain external, name
    half untouched (tier-3 downgrades NEVER get fragments).

External host is `https://www.courtlistener.com` + the lake `identity.absolute_url`;
any other host must sit on the S2 R14 whitelist or the pincite is refused + queued.

Emits an R12 ledger (`_run/o2-execute/s8-link-ledger.rows.jsonl`, actions
`linked-deep` / `linked-external` / `plain:*`) and a journal
(`_run/o2-execute/S8-PINCITE-JOURNAL.jsonl`). Idempotent. Python 3 stdlib only.

    python3 scripts/s8/link_pincites.py --self-test
    python3 scripts/s8/link_pincites.py --scope cases              # DRY RUN (default)
    python3 scripts/s8/link_pincites.py --scope cases --write      # after orchestrator GO
    python3 scripts/s8/link_pincites.py --scope doctrine           # DRY RUN
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zones  # noqa: E402  (frozen R2 zone API)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LAKE_CASES = os.path.join(REPO_ROOT, "_overhaul2", "lake", "cases")
CONTENT = os.path.join(REPO_ROOT, "content")
CONTENT_CASES = os.path.join(CONTENT, "cases")
LEDGER_OUT = os.path.join(REPO_ROOT, "_run", "o2-execute", "s8-link-ledger.rows.jsonl")
JOURNAL_OUT = os.path.join(REPO_ROOT, "_run", "o2-execute", "S8-PINCITE-JOURNAL.jsonl")
FIX_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures", "pincites")

CL_HOST = "https://www.courtlistener.com"
LANE = "s8-fragments"
MODEL = "claude-opus-4-8"
ALL_FORMS = ("clean", "id-nopage", "slip-paren")

# ---------------------------------------------------------------------------
# citation grammars
# ---------------------------------------------------------------------------

_REPORTER = r"\d{1,4}\s+[A-Z][A-Za-z0-9.'’ ]*?"
_IDCITE = r"\*?[Ii]d\.\*?"
_PAGES = r"\d{1,4}(?:[–—-]\d{1,4})?"
_CASE_CITE = r"(?:%s|%s)\s+at\s+(?P<p1>\d{1,4})(?:[–—-](?P<p2>\d{1,4}))?" % (_IDCITE, _REPORTER)
# `— <cite> at <pages>` : dash, optional space, then the whole cite (group `full`).
_CASE_LINE = re.compile(r"[–—-](?P<sp>\s*)(?P<full>" + _CASE_CITE + r")")
# counts every reporter/Id "at <page>" cite in a block, WIRED OR PLAIN (the wired
# form `[*Id.* at 6](url)` still carries the inner phrase), so the sole-cite
# fallback stays stable across passes (idempotency).
_CITE_ANY = re.compile(r"(?:\*?[Ii]d\.\*?|\d{1,4}\s+[A-Z][A-Za-z0-9.'’ ]*?)\s+at\s+\d{1,4}")


def _idnum(pin_id):
    m = re.search(r"(\d+)", pin_id or "")
    return m.group(1) if m else None


def _range_end(p1, p2):
    """Reconstruct a Bluebook abbreviated page range end (`118–19` -> `119`)."""
    if not p2:
        return None
    if len(p2) >= len(p1):
        return p2
    return p1[:len(p1) - len(p2)] + p2


# ---------------------------------------------------------------------------
# lake + content maps
# ---------------------------------------------------------------------------

def load_lake(cases_dir=LAKE_CASES):
    """record_id -> {url, pins:{pin_id:{fragment,quote,fidelity}}}."""
    out = {}
    for path in sorted(glob.glob(os.path.join(cases_dir, "*.json"))):
        with open(path, encoding="utf-8") as fh:
            r = json.load(fh)
        pins = {}
        for p in r.get("pinpoints") or []:
            pins[p.get("id")] = {"fragment": p.get("fragment"), "quote": p.get("quote"),
                                 "fidelity": p.get("quote_fidelity")}
        out[r["record_id"]] = {"url": (r.get("identity") or {}).get("absolute_url"), "pins": pins}
    return out


def _frontmatter_record_id(text):
    m = re.search(r"^\s*record_id:\s*(.+?)\s*$", text, re.M)
    return m.group(1).strip().strip('"') if m else None


def cl_external_url(absolute_url):
    """Full opinion URL from the lake absolute_url, host-guarded (R14). Returns
    (url, None) or (None, reason) when the host is off-whitelist."""
    if not absolute_url:
        return None, "no_absolute_url"
    if absolute_url.startswith("http"):
        url = absolute_url
    else:
        url = CL_HOST + absolute_url
    if not url.startswith(CL_HOST + "/"):
        # Only courtlistener.com is minted here; anything else must be queued for
        # an explicit R14 whitelist decision (the lake carries no other host today).
        return None, "off_whitelist_host"
    return url, None


# ---------------------------------------------------------------------------
# CASE-PAGE wiring
# ---------------------------------------------------------------------------

def _block_for(blocks, pos):
    for b in blocks:
        if b["start"] <= pos <= b["end"] + 2:
            return b
    return None


def _already_wired_page(seg, form_hint):
    return "#:~:text=" in seg


def locate_case_cite(seg, pin_id, forms):
    """Within a pin's block segment, find the citation span to wrap.
    Returns (rel_start, rel_end, form) for the text to replace, or (None, reason)."""
    idnum = _idnum(pin_id)

    # form `clean`: `— <cite> at <page>` (whole-cite wrap). A wired line begins
    # `— [` so the cite group cannot match it (idempotent). Selection order:
    #   1. the (unwired) cite whose page matches the pin (idnum, incl. abbreviated
    #      range end `118–19`==119) — the block may carry several cites for other
    #      quotes; only this pin's page is wired;
    #   2. sole-cite fallback ONLY when the block holds exactly one cite total
    #      (wired + plain), so a leftover sibling cite is never wired on a re-run.
    if "clean" in forms:
        cands = list(_CASE_LINE.finditer(seg))
        if cands:
            if idnum is not None:
                keep = [m for m in cands
                        if idnum in (m.group("p1"), m.group("p2"), _range_end(m.group("p1"), m.group("p2")))]
                if len(keep) == 1:
                    m = keep[0]
                    return (m.start("full"), m.end("full"), "clean")
                if len(keep) > 1:
                    return (None, "ambiguous_multi_cite")
            total = len(_CITE_ANY.findall(seg))
            if total == 1 and len(cands) == 1:
                m = cands[0]
                return (m.start("full"), m.end("full"), "clean")
            return (None, "ambiguous_multi_cite")

    # form `slip-paren`: `— *Id.* (slip op., at N)` -> wrap the inner page number.
    # STRICT to `slip op.`: a `(quoting … at N)` / `(citing … at N)` parenthetical
    # points at a DIFFERENT authority, so its page must never be fragment-linked to
    # this opinion. The slip page must also match the pin's page (idnum).
    if "slip-paren" in forms:
        sp = re.search(
            r"[–—-]\s*\*?[Ii]d\.\*?\s*\(\s*slip op\.,?\s*at\s+(?P<page>\d{1,4})(?P<range>(?:[–—-]\d{1,4})?)\)",
            seg)
        if sp and (idnum is None or sp.group("page") == idnum):
            return (sp.start("page"), sp.end("range"), "slip-paren")

    # form `id-nopage`: `— *Id.*` (optionally a signal/structural paren such as
    # `(Part IV)` / `(citing X)` / `(quoting Y)`) immediately before THIS pin's
    # anchor, with no page of its own -> wrap the `*Id.*` itself.
    if "id-nopage" in forms:
        idp = re.search(
            r"[–—-]\s*(?P<id>\*?[Ii]d\.\*?)(?:\s*\([^)]*\))?[\s.]*\^" + re.escape(pin_id) + r"\b",
            seg)
        if idp:
            return (idp.start("id"), idp.end("id"), "id-nopage")

    return (None, "no_wireable_cite")


def wrap_case(orig, form, url):
    if form == "clean":
        return "[%s](%s)" % (orig, url)
    if form == "id-nopage":
        return "[%s](%s)" % (orig, url)
    if form == "slip-paren":
        return "[%s](%s)" % (orig, url)
    raise ValueError("unknown case form: %r" % form)


def wire_case_page(text, record_id, lake_entry, forms):
    """Returns (new_text, ledger_rows, journal_rows)."""
    ledger = []
    journ = []
    url_base, host_reason = cl_external_url(lake_entry.get("url"))
    blocks = zones.iter_blocks(text)
    anchors = list(re.finditer(r"\^(pin-[A-Za-z0-9-]+)", text))
    edits = []  # (abs_start, abs_end, replacement, pin_id, form, action)
    for am in anchors:
        pin_id = am.group(1)
        pin = lake_entry["pins"].get(pin_id, {})
        fragment = pin.get("fragment")
        blk = _block_for(blocks, am.start())
        if blk is None:
            continue
        base = blk["start"]
        seg = text[blk["start"]:blk["end"]]
        # idempotency: after remediation there is one pin per block, so a fragment
        # link already in this block means THIS pin is wired. Record the TERMINAL
        # state (linked-external, preexisting) — re-derive the form off the stripped
        # cite — so the R12 ledger is stable across runs and re-runs change 0 bytes.
        if fragment and "#:~:text=" in seg:
            stripped = re.sub(
                r"\[([^\]]*)\]\(https://www\.courtlistener\.com/[^)]*#:~:text=[^)]*\)",
                r"\1", seg)
            sloc = locate_case_cite(stripped, pin_id, forms)
            form = sloc[2] if sloc[0] is not None else None
            row = _l(record_id, pin_id, "linked-external", None, form=form)
            row["preexisting"] = True
            ledger.append(row)
            continue
        rel_s, form_or_reason = None, None
        loc = locate_case_cite(seg, pin_id, forms)
        rel_s, rel_e = loc[0], (loc[1] if loc[0] is not None else None)
        if rel_s is None:
            # nothing to wire on this block for this pin (or ambiguous)
            if fragment:
                journ.append(_j(record_id, pin_id, "plain:%s" % loc[1]))
                ledger.append(_l(record_id, pin_id, "plain:%s" % loc[1], None))
            continue
        form = loc[2]
        if fragment is None:
            journ.append(_j(record_id, pin_id, "plain:no-validated-fragment", form=form))
            ledger.append(_l(record_id, pin_id, "plain:no-validated-fragment", None, form=form))
            continue
        if url_base is None:
            journ.append(_j(record_id, pin_id, "plain:%s" % host_reason, form=form))
            ledger.append(_l(record_id, pin_id, "plain:%s" % host_reason, None, form=form))
            continue
        abs_s, abs_e = base + rel_s, base + rel_e
        orig = text[abs_s:abs_e]
        repl = wrap_case(orig, form, url_base + fragment)
        if orig == repl:
            continue
        edits.append((abs_s, abs_e, repl, pin_id, form, "linked-external"))

    # apply in reverse, guarding against overlap
    edits.sort(key=lambda e: -e[0])
    last_start = None
    for abs_s, abs_e, repl, pin_id, form, action in edits:
        if last_start is not None and abs_e > last_start:
            journ.append(_j(record_id, pin_id, "plain:overlap-skip", form=form))
            continue
        orig = text[abs_s:abs_e]
        text = text[:abs_s] + repl + text[abs_e:]
        last_start = abs_s
        journ.append(_j(record_id, pin_id, action, form=form, before=orig, after=repl))
        ledger.append(_l(record_id, pin_id, action, repl, form=form, before=orig))
    return text, ledger, journ


# ---------------------------------------------------------------------------
# DOCTRINE wiring  (rules 1/2/3; zone-aware; conservative / fail-closed)
# ---------------------------------------------------------------------------

# The pincite that trails a case reference. The DOCTRINE convention wraps ONLY the
# page number(s) (the reporter volume stays plain). A pincite exists in exactly two
# forms; a BARE first-page cite (`391 U.S. 543`) is a general signal cite with NO
# pincite and is never wired. The trailing `(?!\s+[A-Z])` rejects a parallel
# reporter (`569 U.S. 1, 133 S. Ct. 1409`) so a parallel volume is never mistaken
# for a pincite page.
_PINCITE_TAIL = r"(?P<page>\d{1,4})(?P<range>(?:[–—-]\d{1,4})?)(?!\s+[A-Z])(?!\d)"
_DPIN_AT = re.compile(r"^\*?,?\s*\d{1,4}\s+[A-Z][A-Za-z.'’ ]*?\s+at\s+" + _PINCITE_TAIL)
_DPIN_COMMA = re.compile(r"^\*?,?\s*\d{1,4}\s+[A-Z][A-Za-z.'’ ]*?\s+\d{1,4},\s+" + _PINCITE_TAIL)
_QUOTE_SPAN = re.compile(r"[\"“]([^\"“”]{8,})[\"”]")
_MIN_QUOTE_MATCH = 20  # a rule-2 quote must share >=20 chars with a pin quote


def _norm_q(s):
    return re.sub(r"\s+", " ", s or "").strip().lower()


def match_doctrine_pincite(after):
    """(rel_start, rel_end, page_text) of the pincite page in `after` (text just
    past a case wikilink), or None. Already-wired (`[8](…)`) fails to match."""
    for rx in (_DPIN_AT, _DPIN_COMMA):
        m = rx.match(after)
        if m:
            return (m.start("page"), m.end("range"), after[m.start("page"):m.end("range")])
    return None


def _unique_quote_pin(entry, quotes):
    """The single pin (matched-fidelity, validated fragment) whose quote overlaps a
    sentence quotation by >=_MIN_QUOTE_MATCH chars. Returns pin_id, '__AMBIG__', or None."""
    hit = None
    for pin_id, pin in entry["pins"].items():
        if pin.get("fidelity") != "matched" or not pin.get("fragment"):
            continue
        pq = _norm_q(pin.get("quote"))
        for q in quotes:
            nq = _norm_q(q)
            if len(nq) >= _MIN_QUOTE_MATCH and (nq in pq or pq in nq):
                if hit and hit != pin_id:
                    return "__AMBIG__"
                hit = pin_id
    return hit


def wire_doctrine_page(text, page2rid, lake, forms=("rule1", "rule2", "rule3")):
    """Doctrine split-pincite wiring (spec R4, rules 1/2/3). Returns
    (new_text, ledger, journal). Edits ONLY outside R2 zones and ONLY the pincite
    page number; rule 2 upgrades a name-half solely on a UNIQUE quote match."""
    ledger = []
    journ = []
    z = zones.compute_zones(text)
    masked = zones.mask(text, z, fill="\x00")  # zone chars blanked; offsets preserved

    link_re = re.compile(r"\[\[(?P<target>[^\]|#]+?)(?P<anchor>#\^pin-[A-Za-z0-9-]+)?(?:\|(?P<disp>[^\]]+))?\]\]")
    edits = []  # (p_s, p_e, repl, rid, pin_id, action, before, extra_anchor_edit?)

    def queue(lm, pm_span, url, action, rid, pin_id, rule, fragment, upgrade=None):
        p_s = lm.end() + pm_span[0]
        p_e = lm.end() + pm_span[1]
        page_txt = text[p_s:p_e]
        repl = "[%s](%s)" % (page_txt, url)
        edits.append([p_s, p_e, repl, rid, pin_id, action, page_txt, rule, fragment])
        if upgrade:
            tgt_e = lm.start() + len("[[") + len(lm.group("target"))
            edits.append([tgt_e, tgt_e, upgrade, rid, pin_id, "linked-deep", "", rule, True])

    for lm in link_re.finditer(text):
        if "\x00" in masked[lm.start():lm.end()]:
            continue  # link sits inside a zone (quote/heading/citation/…); never edit
        target = lm.group("target").strip()
        rid = page2rid.get(target) or page2rid.get(target.replace("_", " "))
        if not rid or rid not in lake:
            continue
        entry = lake[rid]
        # allow a closing italic `*` (and only that) between `]]` and the cite
        after = text[lm.end():lm.end() + 90]
        pm = match_doctrine_pincite(after)
        if pm is None:
            continue  # mention-only or bare signal cite -> nothing to wire
        url_base, host_reason = cl_external_url(entry.get("url"))
        if url_base is None:
            journ.append(_j(rid, None, "plain:%s" % host_reason))
            ledger.append(_l(rid, None, "plain:%s" % host_reason, None))
            continue
        anchor = lm.group("anchor")
        if anchor:  # RULE 1 — name-half already pin-deep
            pin_id = anchor.lstrip("#").lstrip("^")
            pin = entry["pins"].get(pin_id, {})
            frag = pin.get("fragment")
            if frag:
                queue(lm, pm, url_base + frag, "linked-external", rid, pin_id, 1, True)
            else:  # tier-3 downgrade / unvalidatable: plain external, never a fragment
                queue(lm, pm, url_base, "linked-external", rid, pin_id, 1, False)
            continue
        # page-level name-half: RULE 2 (quotation -> unique upgrade) or RULE 3
        sent = _sentence_around(text, lm.start())
        quotes = _QUOTE_SPAN.findall(sent)
        matched = _unique_quote_pin(entry, quotes) if quotes else None
        if matched and matched != "__AMBIG__":  # RULE 2
            queue(lm, pm, url_base + entry["pins"][matched]["fragment"],
                  "linked-external", rid, matched, 2, True, upgrade="#^%s" % matched)
        else:  # RULE 3 (or fail-closed rule-2): pincite plain external, name-half untouched
            if matched == "__AMBIG__":
                journ.append(_j(rid, None, "rule2-ambiguous-quote-left-plain"))
            queue(lm, pm, url_base, "linked-external", rid, None, 3, False)

    # apply reverse, non-overlap (audit-complete: overlap-skips are journaled)
    text = _apply_doctrine_edits(text, edits, ledger, journ)
    return text, ledger, journ


def _apply_doctrine_edits(text, edits, ledger, journ):
    """Splice the queued doctrine page-number edits right-to-left, skipping any that
    overlap an already-applied edit.

    CR-S8-21: a skipped edit is JOURNALED (`plain:overlap-skip`) into both the
    ledger and the journal, mirroring the case-page apply loop. The doctrine loop
    previously dropped it with a bare `continue` — the computed edit vanished with
    no audit row, breaking the trail this verified pipeline otherwise maintains.
    """
    edits.sort(key=lambda e: -e[0])
    last = None
    for p_s, p_e, repl, rid, pin_id, action, before, rule, fragment in edits:
        if last is not None and p_e > last:
            row = _l(rid, pin_id, "plain:overlap-skip", None, before=before)
            row["rule"] = rule
            row["fragment"] = fragment
            ledger.append(row)
            jr = _j(rid, pin_id, "plain:overlap-skip", before=before)
            jr["rule"] = rule
            journ.append(jr)
            continue
        text = text[:p_s] + repl + text[p_e:]
        last = p_s
        row = _l(rid, pin_id, action, repl, before=before)
        row["rule"] = rule
        row["fragment"] = fragment
        ledger.append(row)
        jr = _j(rid, pin_id, action, before=before, after=repl)
        jr["rule"] = rule
        journ.append(jr)
    return text


def _sentence_around(text, pos):
    lo = max(text.rfind(". ", 0, pos), text.rfind("\n", 0, pos))
    hi = text.find("\n", pos)
    if hi < 0:
        hi = len(text)
    return text[lo + 1:hi]


# ---------------------------------------------------------------------------
# ledger / journal rows
# ---------------------------------------------------------------------------

def _l(record_id, pin_id, action, after, form=None, before=None):
    # Every R12 ledger row carries {lane, model} per S1 (the mentions lane flagged
    # earlier lane:null rows) + a `scope` so cases/doctrine rows coexist in the one
    # canonical ledger and each scope re-runs idempotently.
    row = {"record_id": record_id, "pin_id": pin_id, "action": action,
           "lane": LANE, "model": MODEL}
    if form:
        row["form"] = form
    if before is not None:
        row["before"] = before
    if after is not None:
        row["after"] = after
    return row


def _j(record_id, pin_id, action, form=None, before=None, after=None):
    row = {"record_id": record_id, "pin_id": pin_id, "action": action,
           "lane": LANE, "model": MODEL}
    if form:
        row["form"] = form
    if before is not None:
        row["before"] = before
    if after is not None:
        row["after"] = after
    return row


# ---------------------------------------------------------------------------
# drivers
# ---------------------------------------------------------------------------

def build_page2rid(content_cases=CONTENT_CASES):
    """content wikilink target -> lake record_id (basename, title, aliases)."""
    out = {}
    for f in sorted(glob.glob(os.path.join(content_cases, "*.md"))):
        text = open(f, encoding="utf-8").read()
        rid = _frontmatter_record_id(text)
        if not rid:
            continue
        stem = os.path.splitext(os.path.basename(f))[0]
        out[stem] = rid
        tm = re.search(r'^\s*title:\s*"?(.+?)"?\s*$', text, re.M)
        if tm:
            out[tm.group(1).strip()] = rid
    return out


def run_cases(forms=ALL_FORMS, write=False, limit=None, cases_dir=CONTENT_CASES,
              lake_dir=LAKE_CASES):
    lake = load_lake(lake_dir)
    files = sorted(glob.glob(os.path.join(cases_dir, "*.md")))
    all_ledger = []
    all_journ = []
    diffs = []
    changed_files = 0
    for f in files:
        text = open(f, encoding="utf-8").read()
        rid = _frontmatter_record_id(text)
        if not rid or rid not in lake:
            continue
        # skip pages with no validated fragment on any pin (fast path)
        if not any(p.get("fragment") for p in lake[rid]["pins"].values()):
            continue
        new_text, ledger, journ = wire_case_page(text, rid, lake[rid], forms)
        rel = os.path.relpath(f, REPO_ROOT)
        for row in ledger:
            row["file"] = rel
            row["scope"] = "cases"
        for row in journ:
            row["file"] = rel
            row["scope"] = "cases"
        if new_text != text:
            changed_files += 1
            within_limit = (limit is None) or (changed_files <= limit)
            if write and within_limit:
                with open(f, "w", encoding="utf-8") as fh:
                    fh.write(new_text)
            elif write and not within_limit:
                # CR-S8-22: --limit reached this run — the file is NOT written, so
                # its computed rows must NOT claim the pincite is wired. Downgrade
                # them before they reach the canonical ledger; otherwise the ledger
                # falsely certifies citations linked in files never touched on disk.
                for row in ledger:
                    if row["action"].startswith("linked"):
                        row["action"] = "plain:limit-skipped"
                for row in journ:
                    if row["action"].startswith("linked"):
                        row["action"] = "plain:limit-skipped"
            for row in ledger:
                if row["action"].startswith("linked") and len(diffs) < 10000:
                    diffs.append({"file": rel, "pin_id": row["pin_id"],
                                  "form": row.get("form"), "before": row.get("before"),
                                  "after": row.get("after")})
        all_ledger.extend(ledger)
        all_journ.extend(journ)
    _emit(all_ledger, all_journ, write, scope="cases")
    return {"ledger": all_ledger, "journal": all_journ, "diffs": diffs,
            "changed_files": changed_files, "write": write}


def run_doctrine(write=False, cases_dir=CONTENT_CASES, lake_dir=LAKE_CASES,
                 content_dir=CONTENT):
    lake = load_lake(lake_dir)
    page2rid = build_page2rid(cases_dir)
    files = [f for f in sorted(glob.glob(os.path.join(content_dir, "**", "*.md"), recursive=True))
             if os.path.dirname(f) != cases_dir]
    all_ledger = []
    all_journ = []
    diffs = []
    changed_files = 0
    for f in files:
        text = open(f, encoding="utf-8").read()
        new_text, ledger, journ = wire_doctrine_page(text, page2rid, lake)
        rel = os.path.relpath(f, REPO_ROOT)
        for row in ledger:
            row["file"] = rel
            row["scope"] = "doctrine"
        for row in journ:
            row["file"] = rel
            row["scope"] = "doctrine"
        all_ledger.extend(ledger)
        all_journ.extend(journ)
        if new_text != text:
            changed_files += 1
            for row in ledger:
                if row["action"].startswith("linked") and len(diffs) < 10000:
                    diffs.append({"file": rel, "pin_id": row["pin_id"],
                                  "before": row.get("before"), "after": row.get("after")})
            if write:
                with open(f, "w", encoding="utf-8") as fh:
                    fh.write(new_text)
    _emit(all_ledger, all_journ, write, scope="doctrine")
    return {"ledger": all_ledger, "journal": all_journ, "diffs": diffs,
            "changed_files": changed_files, "write": write}


def _read_jsonl(path):
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return out


def _emit(ledger, journ, write, scope):
    """Merge this scope's rows into the single canonical ledger, preserving the
    OTHER scope's rows (cases + doctrine coexist) and dropping legacy untagged
    rows (the pre-backfill lane:null set) so every surviving row carries
    {lane, model, scope}. A NO-OP re-run (0 rows for this scope — everything is
    already wired, e.g. the doctrine pass which has no preexisting-detection)
    PRESERVES the prior run's rows for the scope rather than blanking the R12
    record. Idempotent per scope.

    CR-S8-23: DRY-RUN IS READ-ONLY. The canonical R12 ledger is (re)written only
    under --write, so a preview can never overwrite the rows assemble_ledger.py
    later consumes to prove R1."""
    if not write:
        return
    os.makedirs(os.path.dirname(LEDGER_OUT), exist_ok=True)
    existing = _read_jsonl(LEDGER_OUT)
    kept = [r for r in existing if r.get("scope") and r.get("scope") != scope]
    if not ledger:
        ledger = [r for r in existing if r.get("scope") == scope]
    with open(LEDGER_OUT, "w", encoding="utf-8") as fh:
        for r in kept + ledger:
            fh.write(json.dumps(r, sort_keys=True) + "\n")
    with open(JOURNAL_OUT, "a", encoding="utf-8") as fh:
        for r in journ:
            fh.write(json.dumps(r, sort_keys=True) + "\n")


def summarize(result):
    import collections
    acts = collections.Counter(r["action"] for r in result["ledger"])
    forms = collections.Counter(r.get("form") for r in result["ledger"] if r["action"].startswith("linked"))
    return {"actions": dict(acts), "linked_forms": dict(forms),
            "changed_files": result["changed_files"]}


# ---------------------------------------------------------------------------
# self-test
# ---------------------------------------------------------------------------

def _self_test():
    failures = []

    def check(cond, msg):
        if not cond:
            failures.append(msg)

    # synthetic lake for the fixtures
    lake = {"fixture-sample": {
        "url": "/opinion/999999/fixture-sample/",
        "pins": {
            "pin-6": {"fragment": "#:~:text=holding", "quote": "The quoted holding of the case appears here in full.", "fidelity": "matched"},
            "pin-9": {"fragment": "#:~:text=second", "quote": "A second quoted passage sits on the very next page.", "fidelity": "matched"},
            "pin-119": {"fragment": "#:~:text=third", "quote": "A third passage runs across a page break here.", "fidelity": "matched"},
            "pin-14": {"fragment": "#:~:text=fourth", "quote": "A fourth passage has only an id. cite on its line.", "fidelity": "matched"},
            "pin-op12": {"fragment": "#:~:text=fifth", "quote": "A fifth passage cites the slip opinion only.", "fidelity": "matched"},
            "pin-20": {"fragment": None, "quote": "An unpinned-in-lake passage.", "fidelity": "mismatch"},
        }}}

    # ---- CASE PAGE forms ----
    text = open(os.path.join(FIX_DIR, "case_forms.md"), encoding="utf-8").read()
    new, ledger, journ = wire_case_page(text, "fixture-sample", lake["fixture-sample"], ALL_FORMS)
    by_pin = {r["pin_id"]: r for r in ledger}
    check("[569 U.S. at 6](https://www.courtlistener.com/opinion/999999/fixture-sample/#:~:text=holding)" in new,
          "case clean-cite whole-wrap failed")
    check(by_pin.get("pin-6", {}).get("action") == "linked-external", "pin-6 not linked-external")
    check("[*Id.* at 9]" in new, "case id-page whole-wrap failed")
    check("[*Id.* at 118–19]" in new, "case abbreviated-range wrap failed (pin-119)")
    check(by_pin.get("pin-14", {}).get("form") == "id-nopage", "pin-14 not recognized as id-nopage")
    check("[*Id.*](https://www.courtlistener.com/opinion/999999/fixture-sample/#:~:text=fourth) ^pin-14" in new,
          "id-nopage wrap failed")
    check("(slip op., at [12]" in new, "slip-paren inner-page wrap failed")
    check(by_pin.get("pin-op12", {}).get("form") == "slip-paren", "pin-op12 not slip-paren")
    # pin-20 has no validated fragment -> untouched + plain journal
    check("— 569 U.S. at 20. ^pin-20" in new, "pin-20 (no fragment) must be left untouched")
    check(any(r["pin_id"] == "pin-20" and r["action"] == "plain:no-validated-fragment" for r in journ),
          "pin-20 not journaled plain:no-validated-fragment")
    # idempotency
    new2, _, _ = wire_case_page(new, "fixture-sample", lake["fixture-sample"], ALL_FORMS)
    check(new2 == new, "case-page wiring is not idempotent")

    # host guard: an off-CL url refuses (plain), never mints a bad host
    bad = {"url": "https://evil.example.com/x/", "pins": {"pin-6": {"fragment": "#:~:text=x", "quote": "q", "fidelity": "matched"}}}
    _n, _led, _jr = wire_case_page("A. — 569 U.S. at 6. ^pin-6\n", "x", bad, ALL_FORMS)
    check(any(r["action"].startswith("plain:off_whitelist") for r in _jr), "off-whitelist host not refused")

    # ---- DOCTRINE rules ----
    page2rid = {"Fixture v. Sample": "fixture-sample"}
    dtext = open(os.path.join(FIX_DIR, "doctrine_rules.md"), encoding="utf-8").read()
    dnew, dled, djr = wire_doctrine_page(dtext, page2rid, lake)
    dby = [r for r in dled if r["action"].startswith("linked")]
    # rule 1: pin-deep name-half -> page number linked external (page-only wrap)
    check("569 U.S. at [6](https://www.courtlistener.com/opinion/999999/fixture-sample/#:~:text=holding)" in dnew,
          "doctrine rule1 page-only external wrap failed")
    # rule 2: quotation 'second quoted passage' -> unique upgrade to #^pin-9 + deep link
    check("[[Fixture v. Sample#^pin-9|Sample]]" in dnew, "doctrine rule2 anchor upgrade failed")
    check("569 U.S. at [9](https://www.courtlistener.com/opinion/999999/fixture-sample/#:~:text=second)" in dnew,
          "doctrine rule2 pincite deep-link failed")
    # rule 3: paraphrase -> plain external page (no fragment), name-half untouched
    check("569 U.S. at [12](https://www.courtlistener.com/opinion/999999/fixture-sample/)" in dnew,
          "doctrine rule3 plain-external failed")
    check("[[Fixture v. Sample|Sample]]*, 569 U.S. at [12]" in dnew, "doctrine rule3 must not upgrade the name-half")
    # zone guard: the pincite inside the direct quotation is never rewritten
    check('"see 569 U.S. at 6 for the point."' in dnew, "doctrine must not edit inside a quote zone")
    # idempotency
    dnew2, _, _ = wire_doctrine_page(dnew, page2rid, lake)
    check(dnew2 == dnew, "doctrine wiring is not idempotent")

    # CR-S8-21: a doctrine edit dropped for overlap is journaled to BOTH the
    # ledger and the journal (audit-trail completeness), never silently dropped.
    _led, _jr = [], []
    _ov_edits = [
        [10, 15, "[X](u)", "rid", "pin-1", "linked-external", "ABCD", 1, True],
        [5, 12, "[Y](u)", "rid", "pin-2", "linked-external", "5678", 2, True],  # overlaps
    ]
    _out = _apply_doctrine_edits("0123456789ABCDEF", _ov_edits, _led, _jr)
    check(any(r["action"] == "plain:overlap-skip" for r in _led),
          "CR-S8-21: overlap-skip missing from ledger")
    check(any(r["action"] == "plain:overlap-skip" for r in _jr),
          "CR-S8-21: overlap-skip missing from journal")
    check(sum(1 for r in _led if r["action"] == "linked-external") == 1,
          "CR-S8-21: expected exactly one applied edit")

    # CR-S8-22 / CR-S8-23: --limit gates the LEDGER (not just the file write), and a
    # dry-run never writes the canonical ledger. Exercised via run_cases over a
    # hermetic temp corpus with the ledger/journal globals redirected to temp.
    import tempfile
    import shutil
    global LEDGER_OUT, JOURNAL_OUT
    _save_l, _save_j = LEDGER_OUT, JOURNAL_OUT
    _td = tempfile.mkdtemp()
    try:
        _cases = os.path.join(_td, "cases")
        _lake = os.path.join(_td, "lake")
        os.makedirs(_cases)
        os.makedirs(_lake)
        for i, stem in enumerate(("Alpha v. State", "Beta v. State")):
            rid = "rec-%d" % i
            page = 6 + i
            with open(os.path.join(_cases, stem + ".md"), "w", encoding="utf-8") as fh:
                fh.write("---\nrecord_id: %s\n---\n\nA point. — 1 U.S. at %d. ^pin-%d\n"
                         % (rid, page, page))
            with open(os.path.join(_lake, stem + ".json"), "w", encoding="utf-8") as fh:
                json.dump({"record_id": rid,
                           "identity": {"absolute_url": "/opinion/%d/x/" % i},
                           "pinpoints": [{"id": "pin-%d" % page, "quote_fidelity": "matched",
                                          "fragment": "#:~:text=q%d" % page, "quote": "q"}]}, fh)
        LEDGER_OUT = os.path.join(_td, "ledger.jsonl")
        JOURNAL_OUT = os.path.join(_td, "journal.jsonl")

        # (a) DRY-RUN must not write the canonical ledger (CR-S8-23)
        run_cases(write=False, cases_dir=_cases, lake_dir=_lake)
        check(not os.path.exists(LEDGER_OUT),
              "CR-S8-23: dry-run wrote the canonical ledger")

        # (b) WRITE --limit=1 wires exactly one file; the over-limit file's rows are
        #     downgraded (never claimed linked), and only one file is mutated (CR-S8-22)
        res = run_cases(write=True, limit=1, cases_dir=_cases, lake_dir=_lake)
        _on_disk = sum(1 for fn in os.listdir(_cases)
                       if "#:~:text=" in open(os.path.join(_cases, fn), encoding="utf-8").read())
        check(_on_disk == 1, "CR-S8-22: --limit=1 should write exactly 1 file, wrote %d" % _on_disk)
        _acts = [r["action"] for r in res["ledger"]]
        check("linked-external" in _acts, "CR-S8-22: written file's row missing")
        check("plain:limit-skipped" in _acts,
              "CR-S8-22: over-limit file's rows NOT downgraded -> %s" % _acts)
        check(os.path.exists(LEDGER_OUT), "CR-S8-22: --write did not emit the ledger")
    finally:
        LEDGER_OUT, JOURNAL_OUT = _save_l, _save_j
        shutil.rmtree(_td, ignore_errors=True)

    if failures:
        print("link_pincites.py --self-test: FAIL")
        for f in failures:
            print("  - " + f)
        return 1
    print("link_pincites.py --self-test: PASS (case forms clean/id-nopage/slip-paren + "
          "host guard + doctrine rules 1/2/3 + zone guard + idempotency + "
          "doctrine overlap-journal + --limit ledger-gate + dry-run read-only)")
    return 0


# ---------------------------------------------------------------------------
# cli
# ---------------------------------------------------------------------------

def main(argv):
    ap = argparse.ArgumentParser(description="S8 R4/R5 split-pincite wiring (GATED, dry-run default)")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--scope", choices=("cases", "doctrine"), default="cases")
    ap.add_argument("--write", action="store_true", help="apply edits (requires orchestrator GO)")
    ap.add_argument("--forms", default=",".join(ALL_FORMS),
                    help="case-page cite forms to wire (comma list of clean,id-nopage,slip-paren)")
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args(argv)

    if args.self_test:
        return _self_test()

    forms = tuple(x.strip() for x in args.forms.split(",") if x.strip())
    if args.scope == "cases":
        res = run_cases(forms=forms, write=args.write, limit=args.limit)
    else:
        res = run_doctrine(write=args.write)
    s = summarize(res)
    mode = "WRITE" if args.write else "DRY-RUN"
    print("link_pincites %s scope=%s | changed files: %d" % (mode, args.scope, s["changed_files"]))
    print("actions: %s" % json.dumps(s["actions"], sort_keys=True))
    print("linked forms: %s" % json.dumps(s["linked_forms"], sort_keys=True))
    print("ledger: %s" % LEDGER_OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
