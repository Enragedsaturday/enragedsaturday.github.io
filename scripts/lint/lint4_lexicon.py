#!/usr/bin/env python3
"""
LINT-4 — authority-weight lexicon.   Enforces S1 R10 + Amendment A8 · CHECKLIST:D6.

Every authority-weight label site-wide must be ONE of the six S1 §3.D tiers, in
the exact spaced-em-dash form fixed by Amendment A8 (rev. per Codex review
2026-07-02). The tier word comes FIRST; the qualifier follows the em-dash:

   1. "Binding — SCOTUS"
   2. "Binding in-circuit — <circuit>"        (circuit suffix MANDATORY)
   3. "Persuasive (outside circuit) — <circuit>" (circuit suffix MANDATORY)
   4. "Persuasive — state, illustrative"
   5. "Persuasive only — non-precedential"
   6. "Historical"

   <circuit> = (1st|2d|3d|4th|5th|6th|7th|8th|9th|10th|11th|D.C.|Fed.) Cir.

Checks:
  (a) Banned phrase "persuasive, not binding" (and kindred) anywhere — HIGH.
  (b) Weight cells in an authority table (a column headed Weight / Authority /
      Precedential — NOT a "Controlling authority" citation column) are validated
      against the A8 allowlist EXACTLY. Only markdown emphasis is stripped before
      comparing (composite "Weight · Treatment" cells keep only the weight part,
      i.e. the text before the middle-dot). Any non-allowlist label = HIGH, with
      the message naming the defect class: inverted order, unspaced em-dash,
      en-dash/hyphen in place of the em-dash, case variant, missing mandatory
      circuit suffix, or any other non-allowlist label.
  (c) Prose + table cells: the inverted-label pattern [TEACH-04d] = an em-dash
      whose RIGHT side is a tier word {binding, persuasive, historical} within 3
      words. Conservative (em-dash only): flag only genuine inverted authority
      labels — a canonical qualifier (SCOTUS / <circuit> Cir. / "state,
      illustrative" / "non-precedential" / "outside circuit") immediately
      precedes the em-dash — so a correctly-ordered canonical label
      ("Binding in-circuit — 9th Cir.") and ordinary prose are never flagged.
      HIGH.

Cell splitting is bracket-aware (a wikilink display pipe [[A|B]] is NOT a cell
boundary) so the exact validation is not fooled by unescaped table pipes.

Usage: python3 lint4_lexicon.py [glob ...]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-4"

EM = "—"        # em dash  —
EN = "–"        # en dash  –
MIDDOT = "·"    # middle dot  ·  (composite "Weight · Treatment" separator)
# The A8 tier words + allowlist are the ONE canonical copy in _common (shared
# with LINT-16 — F-S5-07). Rebound here (identical values) so this lint keeps
# its short local names without maintaining a second copy.
TIER_WORDS = c.WEIGHT_TIER_WORDS

# banned phrasings (R10)
BANNED_RE = re.compile(
    r"persuasive\s*,?\s*(?:but\s+)?not\s+binding"
    r"|not\s+binding\s*,?\s*(?:but\s+)?persuasive", re.IGNORECASE)

# --- the A8 exact allowlist (canonical copy in _common, F-S5-07) ------------
_CIRCUIT = c.WEIGHT_CIRCUIT_RE_SRC
_EXACT_LABELS = c.WEIGHT_EXACT_LABELS
_BINDING_INCIRCUIT_RE = c.WEIGHT_BINDING_INCIRCUIT_RE
_PERSUASIVE_OUTSIDE_RE = c.WEIGHT_PERSUASIVE_OUTSIDE_RE

# Prefix (start-anchored, no trailing `$`) forms of the two circuit-suffixed
# labels — used by the prose candidate scanner (lane D) to decide whether a
# bounded candidate BEGINS with a canonical label (canonical label + trailing
# prose is valid — the "modulo the trailing-context trim" of A8's exact check).
_BINDING_INCIRCUIT_PREFIX_RE = re.compile(r"Binding in-circuit — %s" % _CIRCUIT)
_PERSUASIVE_OUTSIDE_PREFIX_RE = re.compile(
    r"Persuasive \(outside circuit\) — %s" % _CIRCUIT)

TIER_WORD_RE = re.compile(r"(?i)\b(?:binding|persuasive|historical)\b")

# The inverted-label pattern (TEACH-04d) is an authority label written
# "<qualifier> — <tier>" (the reverse of the canonical "<tier> — <qualifier>").
# A conservative detector requires a canonical authority QUALIFIER immediately
# before the em-dash — this fires on "SCOTUS — binding" / "9th Cir. — persuasive"
# but NEVER on a correctly-ordered canonical label ("Binding in-circuit — 9th
# Cir.") or on ordinary prose that merely contains a tier word after a dash.
_QUALIFIER_BEFORE_RE = re.compile(
    r"(?i)(?:SCOTUS"
    r"|(?:1st|2d|3d|4th|5th|6th|7th|8th|9th|10th|11th|D\.C\.|Fed\.)\s*Cir\."
    r"|state,?\s*illustrative"
    r"|non-precedential"
    r"|outside\s+circuit)\s*$")

WEIGHT_HEADER_RE = re.compile(r"\b(?:weight|authority|precedential)\b", re.IGNORECASE)


def _strip_emphasis(s):
    """Strip markdown emphasis (* _ `) — and NOTHING else (per A8)."""
    return re.sub(r"[*_`]", "", s)


def _label_ok(label):
    """Exact allowlist membership (case-sensitive, spaced-em-dash forms only)."""
    return (label in _EXACT_LABELS
            or bool(_BINDING_INCIRCUIT_RE.match(label))
            or bool(_PERSUASIVE_OUTSIDE_RE.match(label)))


# --- defect classification (message only; PASS/FAIL is decided by _label_ok) --

def _is_inverted(label):
    """A tier word appears within 3 words to the RIGHT of an em/en/hyphen
    separator, and the label does NOT lead with a tier word (so canonical-order
    labels with trailing junk are not mislabeled 'inverted')."""
    lead = re.match(r"\s*([A-Za-z][A-Za-z\-]*)", label)
    if lead and lead.group(1).lower() in TIER_WORDS:
        return False
    for m in re.finditer(r"%s|%s|\s-\s" % (EM, EN), label):
        for w in label[m.end():].split()[:3]:
            if TIER_WORD_RE.search(w):
                return True
    return False


def _wrong_separator(label):
    """No em-dash present, but swapping an en-dash / hyphen separator for the
    em-dash yields an allowlisted label."""
    if EM in label:
        return False
    cand = label.replace(EN, EM)
    cand2 = re.sub(r"\s-\s", " %s " % EM, cand)
    cand3 = re.sub(r"(?i)^(binding in-circuit|binding|persuasive only|"
                   r"persuasive \(outside circuit\)|persuasive|historical)\s*-\s*",
                   r"\1 %s " % EM, cand2)
    return any(_label_ok(x) for x in (cand, cand2, cand3))


def _case_variant(label):
    """Case-insensitive match against the allowlist while the case-sensitive
    match failed — i.e. the only defect is letter case."""
    if label.lower() in {s.lower() for s in _EXACT_LABELS}:
        return True
    if re.match(r"(?i)^Binding in-circuit — %s$" % _CIRCUIT, label):
        return True
    if re.match(r"(?i)^Persuasive \(outside circuit\) — %s$" % _CIRCUIT, label):
        return True
    return False


def _missing_circuit_suffix(label):
    low = label.lower()
    if low.startswith("binding in-circuit") or \
            low.startswith("persuasive (outside circuit)"):
        if not re.search(r"—\s*%s" % _CIRCUIT, label):
            return True
    return False


def _defect_class(label):
    reasons = []
    if _is_inverted(label):
        reasons.append("inverted order (tier word after the em-dash)")
    if EM in label and (" %s " % EM) not in label:
        reasons.append("unspaced em-dash")
    if _wrong_separator(label):
        reasons.append("en-dash or hyphen in place of the em-dash")
    if _case_variant(label):
        reasons.append("case variant")
    if _missing_circuit_suffix(label):
        reasons.append("missing mandatory circuit suffix")
    if not reasons:
        reasons.append("non-allowlist weight label")
    return "; ".join(reasons)


# --- bracket-aware table parsing --------------------------------------------

def _split_cells(row):
    """Split a GFM table row into cells on unescaped `|` that are NOT inside a
    [[wikilink]] (its display pipe) or an inline `code` span."""
    row = row.strip()
    if row.startswith("|"):
        row = row[1:]
    if row.endswith("|"):
        row = row[:-1]
    cells, buf = [], []
    i, n, depth, incode = 0, len(row), 0, False
    while i < n:
        ch = row[i]
        if ch == "`":
            incode = not incode
            buf.append(ch)
            i += 1
        elif not incode and ch == "[" and i + 1 < n and row[i + 1] == "[":
            depth += 1
            buf.append("[[")
            i += 2
        elif not incode and ch == "]" and i + 1 < n and row[i + 1] == "]" \
                and depth > 0:
            depth -= 1
            buf.append("]]")
            i += 2
        elif ch == "\\" and i + 1 < n and row[i + 1] == "|":
            buf.append("|")
            i += 2
        elif ch == "|" and depth == 0 and not incode:
            cells.append("".join(buf))
            buf = []
            i += 1
        else:
            buf.append(ch)
            i += 1
    cells.append("".join(buf))
    return [x.strip() for x in cells]


def _table_rows(body_lines, start):
    """Yield (lineno, cells, header_cells) for GFM data rows, pairing each with
    its table's header row. Bracket-aware cell splitting."""
    i, n = 0, len(body_lines)
    while i < n:
        line = body_lines[i]
        if "|" in line and i + 1 < n and re.match(
                r"^\s*\|?[\s:|\-]+\|?\s*$", body_lines[i + 1]) and line.strip():
            header = _split_cells(line)
            j = i + 2
            while j < n and "|" in body_lines[j] and body_lines[j].strip():
                yield start + j, _split_cells(body_lines[j]), header
                j += 1
            i = j
        else:
            i += 1


def _weight_col(header):
    for k, h in enumerate(header):
        hl = _strip_emphasis(h).strip().lower()
        if "controlling" in hl or "source" in hl or hl in ("cite", "citation"):
            continue
        if WEIGHT_HEADER_RE.search(hl):
            return k
    return None


# --- lane D: conservative PROSE weight-label candidate scanner (A8 "every
#     weight label site-wide") ---------------------------------------------
#
# Anchors on a capitalized tier word {Binding, Persuasive} IMMEDIATELY followed
# (optionally through a recognized mid-qualifier: in-circuit / only / (outside
# circuit)) by a dash separator — em (—), en (–), or spaced hyphen ( - ). That
# tight anchor is what keeps ordinary prose ("Binding precedent — the court…",
# "Persuasive authority — as always") from ever matching: a non-qualifier word
# between the tier word and the dash breaks the anchor. Only Binding/Persuasive
# are prose anchors; standalone "Historical" prose is NEVER a candidate (it is a
# candidate ONLY inside a weight cell, which lane B already validates).
_PROSE_ANCHOR_RE = re.compile(
    r"\b(?:Binding|Persuasive)"
    r"(?:\s+in-circuit|\s+only|\s+\(outside circuit\))?"
    r"(?:\s*[—–]|\s+-\s+)")

_STRAIGHT_DQUOTE_RE = re.compile(r'"[^"]*"')
_CURLY_DQUOTE_RE = re.compile("“[^”]*”")   # “ ... ”


def _blank_span(m):
    return " " * (m.end() - m.start())


def _mask_prose(line):
    """Exempt (length-preserving) code spans, [[wikilink]] targets, and direct
    quotations, then strip markdown emphasis, so the prose weight-label scanner
    never fires inside code, a wikilink target, or quoted opinion text."""
    line = c.INLINE_CODE_RE.sub(_blank_span, line)
    line = c.WIKILINK_RE.sub(_blank_span, line)
    line = _STRAIGHT_DQUOTE_RE.sub(_blank_span, line)
    line = _CURLY_DQUOTE_RE.sub(_blank_span, line)
    return _strip_emphasis(line)


def _val_window(masked, anchor):
    """Generous validation window from the tier word to the next table-cell `|`,
    closing `]`, +80 chars, or EOL. Deliberately does NOT stop at a period, so a
    canonical circuit suffix ('9th Cir.', 'D.C. Cir.') is never truncated."""
    end = min(anchor + 80, len(masked))
    for j in range(anchor, end):
        if masked[j] in "|]":
            end = j
            break
    return masked[anchor:end]


def _begins_with_canonical(window):
    """True iff `window` BEGINS with an exact A8 allowlist label at a clean
    right boundary (next char non-alphanumeric, or end-of-window). This is A8's
    exact validation 'modulo the trailing-context trim': a canonical label
    followed by ordinary prose validates and is NOT flagged."""
    def clean(i):
        return i >= len(window) or not window[i].isalnum()
    for lbl in _EXACT_LABELS:
        if window.startswith(lbl) and clean(len(lbl)):
            return True
    for rx in (_BINDING_INCIRCUIT_PREFIX_RE, _PERSUASIVE_OUTSIDE_PREFIX_RE):
        m = rx.match(window)
        if m and clean(m.end()):
            return True
    return False


def _candidate_str(window):
    """A bounded, readable candidate substring for the violation message: stop
    at a sentence-ending period (period + space/EOL), a `|`/`]`, or 60 chars."""
    cut = min(len(window), 60)
    for j, ch in enumerate(window[:cut]):
        if ch in "|]":
            cut = j
            break
        if ch == "." and (j + 1 >= len(window) or window[j + 1] == " "):
            cut = j
            break
    return window[:cut].strip()


def _scan_prose_candidates(path, body_lines, fenced, start, skip_lines, out):
    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        lineno = start + i
        if lineno in skip_lines:                 # lane B already validated
            continue
        masked = _mask_prose(line)
        seen = set()
        for m in _PROSE_ANCHOR_RE.finditer(masked):
            window = _val_window(masked, m.start())
            if _begins_with_canonical(window):
                continue                         # canonical label — OK
            cand = _candidate_str(window)
            if not cand or cand in seen:
                continue
            seen.add(cand)
            out.append(c.make_violation(
                LINT, path, lineno, c.HIGH,
                "authority-weight label '%s' (prose) fails the S1 A8 allowlist: "
                "%s [R10/A8]" % (cand, _defect_class(cand))))


def _is_exact_label(s):
    """True iff s is exactly one of the six A8 allowlist strings."""
    return (s in _EXACT_LABELS
            or bool(_BINDING_INCIRCUIT_RE.match(s))
            or bool(_PERSUASIVE_OUTSIDE_RE.match(s)))


def check_file(path):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    body_lines = body.split("\n")
    fenced = c.fenced_line_numbers(body_lines)

    # (e) frontmatter authority_weight — exact allowlist (F-S1-05 round-2).
    # S2's projector derives this field from court_level (valid by
    # construction) and LINT-12 catches drift on promoted pages, but `draft`
    # pages are drift-exempt — a hand-authored bogus weight on a draft page
    # would otherwise pass every gate until promotion. Fail it here.
    aw = fm.get("authority_weight")
    if isinstance(aw, str) and aw.strip() and not _is_exact_label(aw.strip()):
        out.append(c.make_violation(
            LINT, path, 1, c.HIGH,
            "frontmatter authority_weight '%s' fails the S1 A8 allowlist: "
            "%s [R10/A8]" % (aw.strip(), _defect_class(aw.strip()))))

    # (a) banned phrase anywhere (skip code fences) — unchanged
    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        if BANNED_RE.search(line):
            out.append(c.make_violation(
                LINT, path, start + i, c.HIGH,
                "banned authority phrasing 'persuasive, not binding' — use a "
                "six-tier label (e.g. 'Persuasive (outside circuit)') [R10]"))

    # (b) exact-allowlist validation of weight cells
    weight_cell_lines = set()
    for lineno, cells, header in _table_rows(body_lines, start):
        widx = _weight_col(header)
        if widx is None or widx >= len(cells):
            continue
        label = _strip_emphasis(cells[widx]).split(MIDDOT)[0].strip()
        if not label or set(label) <= set("-: "):
            continue
        if not _label_ok(label):
            weight_cell_lines.add(lineno)
            out.append(c.make_violation(
                LINT, path, lineno, c.HIGH,
                "authority-weight label '%s' fails the S1 A8 allowlist: %s "
                "[R10/A8]" % (label, _defect_class(label))))

    # (c) inverted-label pattern in prose + table cells (conservative,
    #     em-dash only): a canonical qualifier immediately before an em-dash
    #     with a tier word within 3 words after it. Skip lines already flagged
    #     as inverted weight cells. Cell boundaries `|` bound both sides so the
    #     window never crosses into an adjacent (canonical) cell.
    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        lineno = start + i
        if lineno in weight_cell_lines:
            continue
        scan = _strip_emphasis(c.INLINE_CODE_RE.sub(" ", line))
        pos = scan.find(EM)
        while pos != -1:
            left = scan[:pos].rsplit("|", 1)[-1]
            first3 = scan[pos + 1:].split("|", 1)[0].split()[:3]
            if _QUALIFIER_BEFORE_RE.search(left) and \
                    any(TIER_WORD_RE.search(w) for w in first3):
                out.append(c.make_violation(
                    LINT, path, lineno, c.HIGH,
                    "inverted authority-label pattern — a qualifier precedes an "
                    "em-dash with a tier word within 3 words after it "
                    "[TEACH-04d]"))
                break
            pos = scan.find(EM, pos + 1)

    # (d) conservative PROSE candidate scanner (A8 "every weight label
    #     site-wide"): tier-word-led candidates in prose validated exactly
    #     against the allowlist (modulo trailing-context trim). Skips lines
    #     already flagged as weight cells by lane (b).
    _scan_prose_candidates(path, body_lines, fenced, start,
                           weight_cell_lines, out)
    return out


def run(paths=None):
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path))
    return out


if __name__ == "__main__":
    c.cli_main(run, LINT)
