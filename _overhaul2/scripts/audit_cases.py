#!/usr/bin/env python3
"""audit_cases.py — S6 "named-but-no-page" roster regenerator (audit COH-02 / NUM-05).

Scans `content/**/*.md` prose (excluding `content/cases/`) for case captions —
`X v. Y`, `In re X`, `Ex parte X` — that are NOT wikilinked at the mention site
and have NO page in `content/cases/` (matching against filenames, `title:` and
`aliases:` frontmatter, normalized). Emits the S6 seed roster as markdown and/or
JSON. This is the **named-in-prose lane only**: the S6 relevance gate and the
GAP-05 SCOTUS term-by-term sweep are separate seed sources that EXTEND it.

Method lineage
--------------
Reimplements and hardens the 2026-07-02 claims-audit measurement (scratchpad
`measure5.py`, claim #5: 127 raw -> ~80-84 cleaned, residual noise +/-4).
Documented divergences from that script (each removes false "no-page" rows or
improves capture; see S6-SEED.md "Divergence" for the net effect):
  1. Year-disambiguated page filenames ("Harris v. United States (1968).md")
     now match their bare prose captions (prior method false-missed ~6).
  2. Party token-set matching: "Brower v. Inyo County" == "Brower v. County of
     Inyo" (word-order/connector insensitive within a party).
  3. Multi-word parties with lowercase connectors are captured ("District of
     Columbia", "County of Inyo", "Board of Chosen Freeholders"), so the prior
     truncation artifacts ("Columbia v. Heller", "Brower v. County") collapse
     into their real captions instead of polluting the roster.
  4. Trailing possessives stripped ("Arizona v. Gant's" -> Arizona v. Gant,
     which then page-matches).
  5. `In re` / `Ex parte` captions scanned (prior method: X v. Y only).
  6. Classification lanes instead of silent drops: roster / citation-format
     placeholder / fabrication-flagged / carried-forward-UNVERIFIABLE /
     variant-candidate annotations.

Determinism: no randomness, no network, stdlib only; output sorted by
normalized caption; re-runnable byte-identically against the same tree.

Usage
-----
  python3 _overhaul2/scripts/audit_cases.py                # markdown to stdout
  python3 _overhaul2/scripts/audit_cases.py --format json  # JSON to stdout
  python3 _overhaul2/scripts/audit_cases.py --format both \
      --out-md /tmp/roster.md --out-json /tmp/roster.json
  python3 _overhaul2/scripts/audit_cases.py --show-dropped # audit the exclusions

Flags
-----
  --repo PATH        repo root (default: two levels up from this script)
  --content PATH     content dir (default: <repo>/content)
  --o1-list PATH     O1 missed-cases list for the residual cross-check
                     (default: <repo>/_overhaul/coverage/missed-cases.md;
                     skipped silently if absent)
  --format md|json|both   (default md)
  --out-md / --out-json   write to files instead of stdout
  --show-dropped     append the page-matched/truncation exclusions (debug)
"""

import argparse
import glob
import json
import os
import re
import sys
import unicodedata
from collections import OrderedDict

GENERATED_STAMP = "regenerated from audit finding COH-02 [CRITICAL] / NUM-05"

# ---------------------------------------------------------------------------
# Curated provenance lists (documented, auditable — not silent magic)
# ---------------------------------------------------------------------------

# (a) Fabrication-risk flags: docs/FINAL-QA-SPEC.md §0.3 ("backwards holding
# (Moore-Bush), invented frameworks (Mayville/Lyle/Small)") and RUNBOOK §4-S6.
# NOTE: O1 s9-adjudications.md later confirmed Mayville (10th Cir. 2020) and
# Small (4th Cir. 2019) real + correctly stated — they stay `unverified` here
# because S6 re-verifies via two-key; "not found != fabricated".
FABRICATION_FLAGGED = {
    "united states v mayville",
    "united states v small",
    "united states v lyle",
    "united states v moore bush",
}

# Carried-forward UNVERIFIABLE bare-name captures: O1 S5 spec R9
# (_overhaul/specs/S5-case-ingest.spec.md:246-249) + Case Index rows 396/458.
# "United States v. Jackson" is excluded here because a *different* U.S. v.
# Jackson page exists and norm-matches; the "second bare Jackson" nuance is
# carried in S6-SEED prose, not the mechanical roster.
CARRYFORWARD_UNVERIFIABLE = {
    "united states v cruz",
    "united states v west",
    "united states v white",
}

# (c) Citation-format placeholders: teaching templates in
# content/2-legal-system-research/Reading and Citing Cases.md:106,113
# (Bluebook short-form + civil-caption examples). Not cases; ignore.
PLACEHOLDER_CAPTIONS = {
    "state v smith",
    "stern v florida",
    "stern v state",
    "state v randolph",   # short-form example of Georgia v. Randolph (page exists)
    "smith v jones",
}
# Backstop for future edits to the teaching pages: both parties generic.
GENERIC_PLACEHOLDER_PARTIES = {"smith", "jones", "doe", "roe", "stern", "state"}

# Curated per-row notes (norm -> note), appended to flags with provenance.
INCIDENTAL_NOTES = {
    # Strike 3 Holdings, LLC v. John Doe (D.D.C. BitTorrent docket): named only
    # as the corrupted-CL-object warning on the Zorn v. Linton entry
    # (10-use-of-force-liability/Section 1983 ... .md:188). Not 4A material.
    "llc v john doe": "incidental non-4A mention (Strike 3 Holdings BitTorrent "
                      "docket, corrupted-CL-object warning for Zorn) — ignore",
    # Same 1st Cir. border-device case under successor-official captions
    # (Alasaad v. Nielsen (D. Mass.) -> Wolf -> Mayorkas): one case, two rows.
    "alasaad v mayorkas": "caption variant of Alasaad v. Wolf (same 1st Cir. "
                          "case, successor DHS secretary)",
    "alasaad v wolf": "caption variant of Alasaad v. Mayorkas (same 1st Cir. "
                      "case, successor DHS secretary)",
}

# Government-style litigants (for variant heuristics).
GOV_PARTIES = {
    "united states", "us", "u s", "state", "people", "commonwealth",
    "government",
}
STATE_NAMES = {
    "alabama", "alaska", "arizona", "arkansas", "california", "colorado",
    "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho",
    "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine",
    "maryland", "massachusetts", "michigan", "minnesota", "mississippi",
    "missouri", "montana", "nebraska", "nevada", "new hampshire", "new jersey",
    "new mexico", "new york", "north carolina", "north dakota", "ohio",
    "oklahoma", "oregon", "pennsylvania", "rhode island", "south carolina",
    "south dakota", "tennessee", "texas", "utah", "vermont", "virginia",
    "washington", "west virginia", "wisconsin", "wyoming",
}

# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------

YEAR_PAREN_RE = re.compile(r"\s*\(\s*(?:17|18|19|20)\d{2}\s*\)\s*$")
PARTY_STOPWORDS = {"of", "the", "and", "for", "a", "an"}

# Caption-abbreviation expansion so "Dist. Court of Nev." == "District Court
# of Nevada" and "Dep't"/"Dept." == "Department" across prose and filenames.
TOKEN_EXPAND = {
    "dist": "district", "nev": "nevada", "dept": "department",
    "cnty": "county", "bd": "board",
}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = s.replace("’", "'").replace("‘", "'")
    s = s.lower().replace("'", "")          # Dep't -> dept, Barlow's -> barlows
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return " ".join(TOKEN_EXPAND.get(t, t) for t in s.split())


def strip_year(s: str) -> str:
    return YEAR_PAREN_RE.sub("", s).strip()


def party_tokens(party_norm: str) -> frozenset:
    """Order/connector-insensitive token set for one party."""
    return frozenset(t for t in party_norm.split() if t not in PARTY_STOPWORDS)


def htokens(s: str):
    """Structural tokens that KEEP intra-word hyphens, so 'Perez' is NOT a
    token-prefix of 'Perez-Rodriguez' (different surname, different case),
    while 'City' IS a token-prefix of 'City of Seattle' (true truncation)."""
    s = unicodedata.normalize("NFKD", s)
    s = s.replace("’", "'").replace("‘", "'").lower().replace("'", "")
    s = re.sub(r"[^a-z0-9 -]", " ", s)
    toks = [t.strip("-") for t in s.split()]
    return tuple(TOKEN_EXPAND.get(t, t) for t in toks if t)


def hsplit_caption(caption: str):
    """Raw caption -> (first htokens, second htokens) or None."""
    parts = re.split(r"\s+v\.?\s+", caption, maxsplit=1, flags=re.I)
    if len(parts) == 2:
        f, s = htokens(parts[0]), htokens(parts[1])
        if f and s:
            return f, s
    return None


def split_caption(caption_norm: str):
    """'x v y' -> ('x','y') or None for In re/Ex parte."""
    parts = caption_norm.split(" v ")
    if len(parts) == 2 and parts[0] and parts[1]:
        return parts[0].strip(), parts[1].strip()
    return None


# ---------------------------------------------------------------------------
# Page index (content/cases/)
# ---------------------------------------------------------------------------

def read_file(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def frontmatter(text: str) -> str:
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    return m.group(1) if m else ""


def parse_aliases(fm: str):
    """aliases: [] | inline list | block list. YAML-lite, deterministic."""
    out = []
    m = re.search(r"^aliases:\s*\[(.*?)\]\s*$", fm, re.M)
    if m:
        for item in m.group(1).split(","):
            item = item.strip().strip("\"'")
            if item:
                out.append(item)
        return out
    m = re.search(r"^aliases:\s*$", fm, re.M)
    if m:
        for line in fm[m.end():].splitlines():
            lm = re.match(r"^\s+-\s*(.+?)\s*$", line)
            if lm:
                out.append(lm.group(1).strip().strip("\"'"))
            elif line.strip():
                break
    return out


class PageIndex:
    def __init__(self, cases_dir: str):
        self.exact = {}      # norm(name) -> filename        (incl. year-stripped)
        self.pairs = {}      # (tokset1, tokset2) -> filename (v.-captions)
        self.parties = []    # (first_norm, second_norm, filename)
        self.hparties = []   # (first_htokens, second_htokens, filename)
        self.filenames = []
        for path in sorted(glob.glob(os.path.join(cases_dir, "*.md"))):
            fname = os.path.basename(path)
            self.filenames.append(fname)
            stem = os.path.splitext(fname)[0]
            text = read_file(path)
            fm = frontmatter(text)
            names = [stem]
            tm = re.search(r'^title:\s*"?([^"\n]+?)"?\s*$', fm, re.M)
            if tm:
                names.append(tm.group(1))
            names.extend(parse_aliases(fm))
            for name in names:
                for variant in {name, strip_year(name)}:
                    key = norm(variant)
                    if not key:
                        continue
                    self.exact.setdefault(key, fname)
                    sp = split_caption(key)
                    if sp:
                        first, second = sp
                        self.pairs.setdefault(
                            (party_tokens(first), party_tokens(second)), fname)
                        self.parties.append((first, second, fname))
                        hsp = hsplit_caption(variant)
                        if hsp:
                            self.hparties.append((hsp[0], hsp[1], fname))

    def match(self, caption_norm: str, caption_raw: str = None):
        """Return (filename, how) if the caption resolves to an existing page."""
        if caption_norm in self.exact:
            return self.exact[caption_norm], "exact"
        sp = split_caption(caption_norm)
        if not sp:
            return None
        first, second = sp
        key = (party_tokens(first), party_tokens(second))
        if key in self.pairs:
            return self.pairs[key], "token-set"
        # Truncation artifact of an existing page: caption first party is a
        # token-suffix of the page's first party AND caption second party is a
        # token-prefix of the page's second party (e.g. "Canton v. Harris" <-
        # "City of Canton v. Harris"; "See v. City" <- "See v. City of Seattle").
        # Also the reverse (prose caption extends the page's shortened title,
        # e.g. "Hiibel v. Sixth Judicial Dist. Court of Nev." vs the page
        # "Hiibel v. Sixth Judicial Dist. Court"). Uses hyphen-preserving
        # tokens so "Perez" never matches "Perez-Rodriguez".
        hsp = hsplit_caption(caption_raw if caption_raw is not None
                             else caption_norm)
        if not hsp:
            return None
        cf, cs = list(hsp[0]), list(hsp[1])
        for pft, pst, fname in self.hparties:
            pft, pst = list(pft), list(pst)
            if len(cf) <= len(pft) and len(cs) <= len(pst) \
                    and pft[-len(cf):] == cf and pst[:len(cs)] == cs \
                    and (len(cf) < len(pft) or len(cs) < len(pst)):
                return fname, "truncation-of-page"
            if len(pft) <= len(cf) and len(pst) <= len(cs) \
                    and cf[-len(pft):] == pft and cs[:len(pst)] == pst \
                    and (len(pft) < len(cf) or len(pst) < len(cs)):
                return fname, "extension-of-page"
        return None

    def variant_candidates(self, caption_norm: str):
        """Annotate probable-but-unproven page matches (S6 adjudicates)."""
        notes = []
        sp = split_caption(caption_norm)
        if not sp:
            return notes
        first, second = sp
        ft, st = party_tokens(first), party_tokens(second)
        for pf, ps, fname in self.parties:
            pft, pst = party_tokens(pf), party_tokens(ps)
            if ft == pst and st == pft:
                notes.append(f"swapped-caption match: `{fname}`")
                continue
            # One distinctive party matches exactly; the other is a government
            # litigant on both sides -> possible same case, different caption.
            for cparty, pparty, cother, pother in (
                    (first, pf, second, ps), (second, ps, first, pf)):
                if cparty == pparty and cparty not in GOV_PARTIES \
                        and cparty not in STATE_NAMES and len(cparty) > 3 \
                        and _govish(cother) and _govish(pother) \
                        and cother != pother:
                    notes.append(f"possible variant of `{fname}`")
        return sorted(set(notes))


def _govish(party_norm: str) -> bool:
    return party_norm in GOV_PARTIES or party_norm in STATE_NAMES


# ---------------------------------------------------------------------------
# Prose scan
# ---------------------------------------------------------------------------

CAP_TOKEN = r"[A-Z][A-Za-z.'’&-]*"
CONNECTOR = r"(?:of|the|and|for|de|del|la|van|von|&)"
PARTY = rf"{CAP_TOKEN}(?:\s+(?:{CONNECTOR}\s+){{0,2}}{CAP_TOKEN}){{0,6}}"
# "v." only — the corpus's prose comparisons use "vs." ("Wolf vs. Mapp",
# "Role vs. Carpenter" table headers), which are not case captions.
VS_RE = re.compile(rf"\b({PARTY})\s+v\.\s+({PARTY})")
INRE_RE = re.compile(rf"\b((?:In re|Ex parte)\s+{CAP_TOKEN}(?:\s+{CAP_TOKEN}){{0,2}})")
POSSESSIVE_RE = re.compile(r"(?:'|’)s$")

# Sentence-boundary control: a party token ending in "." may only sit mid-party
# if it is an initial ("G.", "U.S.", "J.D.B.") or a caption abbreviation.
INITIALS_RE = re.compile(r"^(?:[A-Z]\.)+$")
MID_ABBREVS = {
    "inc.", "corp.", "co.", "dept.", "dep't.", "bd.", "cnty.", "ct.", "st.",
    "mt.", "no.", "bros.", "ltd.", "mfg.", "r.r.", "ry.", "ins.", "twp.",
    "vill.", "univ.", "sch.", "dist.", "jud.", "nat'l.", "ass'n.", "sav.",
}
# Capitalized sentence-starters that never begin/end a real caption party;
# stripped from the left of party 1 and the right of party 2.
NOISE_WORDS = {
    "The", "A", "An", "And", "But", "Or", "Nor", "It", "Its", "That", "This",
    "These", "Those", "However", "Also", "If", "So", "As", "See", "Held",
    "Compare", "Contrast", "When", "Where", "While", "After", "Before",
    "Under", "Over", "Not", "No", "His", "Her", "Their", "Some", "Most",
    "Both", "Such", "Then", "There", "They", "He", "She", "We", "You", "Is",
    "Are", "Was", "Were", "Because", "Since", "Although", "Though", "Unlike",
    "Like", "Per", "Via", "Whether", "What", "Why", "How", "Only", "Even",
}


def _token_may_continue(tok: str) -> bool:
    """May a "."-terminated token be followed by more of the same party?"""
    return bool(INITIALS_RE.match(tok)) or tok.lower() in MID_ABBREVS


def trim_party(party: str, side: str) -> str:
    """Cut a captured party at sentence boundaries + strip noise words.

    side='first': keep only the segment after the last bad "." token
    ("...in Kyllo. United States" -> "United States"), then strip leading
    noise words ("After Caniglia" -> "Caniglia").
    side='second': cut at the first bad "." token ("Ohio. Italicized" ->
    "Ohio"), then strip trailing noise words ("Chatrie The" -> "Chatrie").
    """
    toks = party.split()
    if side == "first":
        start = 0
        for i, t in enumerate(toks[:-1]):
            if t.endswith(".") and not _token_may_continue(t):
                start = i + 1
        toks = toks[start:]
        while toks and toks[0] in NOISE_WORDS:
            toks = toks[1:]
    else:
        for i, t in enumerate(toks[:-1]):
            if t.endswith(".") and not _token_may_continue(t):
                toks = toks[:i + 1]
                break
        while toks and toks[-1] in NOISE_WORDS:
            toks = toks[:-1]
    # cosmetic: bare trailing sentence period / edge quotes
    out = []
    for j, t in enumerate(toks):
        t = t.strip("'’‘\"“”")
        if j == len(toks) - 1 and t.endswith(".") and not _token_may_continue(t):
            t = t[:-1]
        if t:
            out.append(t)
    return " ".join(out)

WIKILINK_RE = re.compile(r"\[\[[^\]]*\]\]")
MDLINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
URL_RE = re.compile(r"https?://\S+")
CODE_RE = re.compile(r"`[^`]*`")
EMPH_RE = re.compile(r"[*_]{1,3}")

COURT_PAREN_RE = re.compile(r"^[^()\n]{0,80}?\(([^()]{1,60})\)")
COURT_SIGNAL_RE = re.compile(
    r"\d{1,2}(?:st|nd|rd|th)\s+Cir|Cir\.|U\.?S\.|S\.\s?Ct|F\.\d|F\.\s?Supp|"
    r"So\.\s?\d|en banc|per curiam|(?:17|18|19|20)\d{2}|[A-Z][a-z]{1,5}\.")


def clean_line(line: str) -> str:
    line = WIKILINK_RE.sub(" ", line)      # wikilinked mentions are already linked
    line = MDLINK_RE.sub(r"\1", line)      # keep link text (external link != page)
    line = URL_RE.sub(" ", line)
    line = CODE_RE.sub(" ", line)
    line = EMPH_RE.sub("", line)           # *italic*/**bold** wrappers
    return line


def strip_possessive(party: str) -> str:
    toks = party.split()
    toks[-1] = POSSESSIVE_RE.sub("", toks[-1])
    return " ".join(toks)


def guess_court_era(tail: str) -> str:
    """Cheap heuristic on the same-line text after the caption."""
    m = COURT_PAREN_RE.match(tail)
    if m and COURT_SIGNAL_RE.search(m.group(1)) \
            and not re.match(r"^\d{4}-\d{2}-\d{2}$", m.group(1).strip()):
        return m.group(1).strip()
    win = tail[:120]
    m = re.search(r"\d{1,2}(?:st|nd|rd|th)\s+Cir\.?(?:\s+(?:17|18|19|20)\d{2})?", win)
    if m:
        return m.group(0)
    m = re.search(r"(?:17|18|19|20)\d{2}", win)
    if m:
        return m.group(0)
    return "unknown"


def iter_content_files(content_dir: str, cases_dir: str):
    for path in sorted(glob.glob(os.path.join(content_dir, "**", "*.md"),
                                 recursive=True)):
        if os.path.commonpath([path, cases_dir]) == cases_dir:
            continue
        yield path


def scan(content_dir: str, cases_dir: str, index: PageIndex):
    """Return (kept OrderedDict norm->row, dropped list, raw_count)."""
    found = OrderedDict()   # norm -> row dict
    dropped = []
    raw_distinct = set()
    in_code_block = False
    for path in iter_content_files(content_dir, cases_dir):
        rel = os.path.relpath(path, content_dir)
        text = read_file(path)
        body = re.sub(r"^---\n.*?\n---", lambda m: "\n" * m.group(0).count("\n"),
                      text, count=1, flags=re.S)  # keep line numbers stable
        in_code_block = False
        for lineno, line in enumerate(body.splitlines(), start=1):
            if line.lstrip().startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue
            cl = clean_line(line)
            matches = []
            for m in VS_RE.finditer(cl):
                first = trim_party(m.group(1).strip(), "first")
                second = trim_party(m.group(2).strip(), "second")
                if not first or not second:
                    continue
                caption = f"{first} v. {second}"
                # match against both the caption as-is and its
                # possessive-stripped form ("Arizona v. Gant's" -> Gant)
                stripped = (f"{strip_possessive(first)} v. "
                            f"{strip_possessive(second)}")
                matches.append((caption, stripped, cl[m.end():]))
            for m in INRE_RE.finditer(cl):
                cap = m.group(1).strip()
                matches.append((cap, cap, cl[m.end():]))
            for caption, stripped, tail in matches:
                cn = norm(strip_year(caption))
                cn_stripped = norm(strip_year(stripped))
                if not cn or " v " in cn and not split_caption(cn):
                    continue
                raw_distinct.add(cn)
                page = (index.match(cn, caption)
                        or index.match(cn_stripped, stripped))
                if page:
                    dropped.append({"caption": caption, "norm": cn,
                                    "match": page[0], "how": page[1],
                                    "source": f"{rel}:{lineno}"})
                    continue
                cn = cn_stripped  # store possessive-stripped as canonical
                caption = stripped
                row = found.get(cn)
                if row is None:
                    row = {"caption": caption, "norm": cn,
                           "court_era": "unknown", "sources": [],
                           "mentions": 0, "status": "unverified", "flags": []}
                    found[cn] = row
                row["mentions"] += 1
                row["sources"].append(f"{rel}:{lineno}")
                guess = guess_court_era(tail)
                if guess != "unknown" and (
                        row["court_era"] == "unknown"
                        or len(guess) > len(row["court_era"])):
                    row["court_era"] = guess
                if len(caption) > len(row["caption"]):
                    row["caption"] = caption
    return found, dropped, len(raw_distinct)


def collapse_truncations(found: OrderedDict):
    """Merge roster rows that are truncation artifacts of longer roster rows
    (hyphen-preserving tokens: "Perez" never merges into "Perez-Rodriguez")."""
    keys_by_len = sorted(found, key=lambda k: (-len(k.split()), k))
    merged = []
    for short in sorted(found, key=lambda k: (len(k.split()), k)):
        if short not in found:
            continue
        ssp = hsplit_caption(found[short]["caption"])
        if not ssp:
            continue
        sf, ss = list(ssp[0]), list(ssp[1])
        for longk in keys_by_len:
            if longk == short or longk not in found or short not in found:
                continue
            lsp = hsplit_caption(found[longk]["caption"])
            if not lsp:
                continue
            lf, ls = list(lsp[0]), list(lsp[1])
            if len(sf) <= len(lf) and len(ss) <= len(ls) \
                    and lf[-len(sf):] == sf and ls[:len(ss)] == ss \
                    and (len(sf) < len(lf) or len(ss) < len(ls)):
                tgt = found[longk]
                src = found.pop(short)
                tgt["mentions"] += src["mentions"]
                tgt["sources"].extend(src["sources"])
                merged.append((src["caption"], tgt["caption"]))
                break
    return merged


def classify(found: OrderedDict, index: PageIndex):
    roster, placeholders = [], []
    for cn in sorted(found):
        row = found[cn]
        sp = split_caption(cn)
        is_placeholder = cn in PLACEHOLDER_CAPTIONS or (
            sp is not None
            and party_tokens(sp[0]) <= GENERIC_PLACEHOLDER_PARTIES
            and party_tokens(sp[1]) <= GENERIC_PLACEHOLDER_PARTIES)
        if is_placeholder:
            row["flags"].append("citation-format-placeholder")
            placeholders.append(row)
            continue
        if cn in FABRICATION_FLAGGED:
            row["flags"].append("fabrication-flagged (FINAL-QA §0.3)")
        if cn in CARRYFORWARD_UNVERIFIABLE:
            row["flags"].append("UNVERIFIABLE carry-forward (O1 S5 R9)")
        if cn in INCIDENTAL_NOTES:
            row["flags"].append(INCIDENTAL_NOTES[cn])
        row["variant_notes"] = index.variant_candidates(cn)
        roster.append(row)
    return roster, placeholders


def annotate_o1_omissions(roster, omissions_path: str):
    """Carry O1's deliberate-exclusion adjudications onto matching rows."""
    if not os.path.isfile(omissions_path):
        return
    disp = {}
    for line in read_file(omissions_path).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and " v. " in cells[0]:
            name = norm(strip_year(re.sub(r"[*_]", "", cells[0])))
            if name and cells[2] and not cells[2].startswith("-"):
                disp[name] = f"O1 omissions: {cells[2]} → {cells[3]}"
    for row in roster:
        note = disp.get(row["norm"])
        if note:
            row["flags"].append(note)


# ---------------------------------------------------------------------------
# O1 residual cross-check (section d)
# ---------------------------------------------------------------------------

def o1_residual(o1_path: str, index: PageIndex):
    if not os.path.isfile(o1_path):
        return None
    text = read_file(o1_path)
    listed = re.findall(r"^\|\s*\d+\s*\|\s*\*\*(.+?)\*\*", text, re.M)
    rows = []
    for name in listed:
        base = re.sub(r"\s*\(.*?\)\s*$", "", name).strip()
        cn = norm(base)
        page = index.match(cn, base)
        rows.append({"o1_name": name, "norm": cn,
                     "page_today": page[0] if page else None,
                     "match_how": page[1] if page else None})
    residual = [r for r in rows if r["page_today"] is None]
    return {"listed": len(listed), "residual": residual, "all": rows}


# ---------------------------------------------------------------------------
# Sanity + output
# ---------------------------------------------------------------------------

def assert_no_page_collisions(roster, index: PageIndex):
    # Explicit raise (not `assert`): this collision gate is the last-line guarantee
    # that no roster row aliases an existing case page, and `assert` is compiled out
    # under `python -O` / PYTHONOPTIMIZE — which would let a colliding roster emit
    # silently as a PASS. The check must not be optimizable away.
    for row in roster:
        if index.match(row["norm"], row["caption"]) is not None:
            raise AssertionError(
                f"roster row matches an existing case page: {row['caption']}")


def fmt_sources(sources, cap=3):
    uniq = list(OrderedDict.fromkeys(sources))
    shown = uniq[:cap]
    extra = len(uniq) - len(shown)
    s = "; ".join(shown)
    return s + (f"; +{extra} more" if extra > 0 else "")


def md_escape(s: str) -> str:
    return s.replace("|", "\\|")


def render_md(result) -> str:
    out = []
    r = result
    out.append(f"<!-- generated by _overhaul2/scripts/audit_cases.py — {GENERATED_STAMP} -->")
    out.append(f"Roster rows: **{len(r['roster'])}** · placeholders (ignored): "
               f"{len(r['placeholders'])} · raw distinct captions scanned: {r['raw_distinct']}")
    out.append("")
    out.append("| # | Caption (as found) | Court / era (heuristic) | Source file:line(s) | Mentions | Flags / variant notes | Status |")
    out.append("|---|---|---|---|---|---|---|")
    for i, row in enumerate(r["roster"], 1):
        notes = row["flags"] + row.get("variant_notes", [])
        out.append("| {} | {} | {} | {} | {} | {} | {} |".format(
            i, md_escape(row["caption"]), md_escape(row["court_era"]),
            md_escape(fmt_sources(row["sources"])), row["mentions"],
            md_escape("; ".join(notes)) if notes else "—", row["status"]))
    out.append("")
    out.append("### Citation-format placeholders (ignore — teaching templates, not cases)")
    for row in r["placeholders"]:
        out.append(f"- {row['caption']} — {fmt_sources(row['sources'])}")
    if r.get("o1") is not None:
        o1 = r["o1"]
        out.append("")
        out.append(f"### O1 missed-cases residual ({o1['listed']} listed; "
                   f"{len(o1['residual'])} still page-less)")
        for row in o1["residual"]:
            out.append(f"- {row['o1_name']}")
    return "\n".join(out) + "\n"


def main(argv=None):
    here = os.path.dirname(os.path.abspath(__file__))
    default_repo = os.path.dirname(os.path.dirname(here))
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", default=default_repo)
    ap.add_argument("--content", default=None)
    ap.add_argument("--o1-list", default=None)
    ap.add_argument("--o1-omissions", default=None)
    ap.add_argument("--format", choices=["md", "json", "both"], default="md")
    ap.add_argument("--out-md", default=None)
    ap.add_argument("--out-json", default=None)
    ap.add_argument("--show-dropped", action="store_true")
    args = ap.parse_args(argv)

    content_dir = os.path.abspath(args.content or os.path.join(args.repo, "content"))
    cases_dir = os.path.join(content_dir, "cases")
    o1_path = args.o1_list or os.path.join(
        args.repo, "_overhaul", "coverage", "missed-cases.md")
    omissions_path = args.o1_omissions or os.path.join(
        args.repo, "_overhaul", "coverage", "omissions.md")

    index = PageIndex(cases_dir)
    found, dropped, raw_distinct = scan(content_dir, cases_dir, index)
    merged = collapse_truncations(found)
    roster, placeholders = classify(found, index)
    annotate_o1_omissions(roster, omissions_path)
    assert_no_page_collisions(roster, index)

    result = {
        "generated_by": "audit_cases.py",
        "provenance": GENERATED_STAMP,
        "case_pages": len(index.filenames),
        "raw_distinct": raw_distinct,
        "roster_count": len(roster),
        "placeholder_count": len(placeholders),
        "roster": roster,
        "placeholders": placeholders,
        "truncations_merged": merged,
        "o1": o1_residual(o1_path, index),
    }
    if args.show_dropped:
        result["dropped_page_matches"] = dropped

    outputs = []
    if args.format in ("md", "both"):
        md = render_md(result)
        if args.show_dropped:
            md += "\n### Dropped (matched an existing page)\n"
            for d in dropped:
                md += f"- {d['caption']} -> {d['match']} ({d['how']}) [{d['source']}]\n"
        outputs.append((args.out_md, md))
    if args.format in ("json", "both"):
        outputs.append((args.out_json, json.dumps(result, indent=2,
                                                  ensure_ascii=False) + "\n"))
    for dest, payload in outputs:
        if dest:
            with open(dest, "w", encoding="utf-8") as f:
                f.write(payload)
        else:
            sys.stdout.write(payload)
    print(f"[audit_cases] pages={len(index.filenames)} raw={raw_distinct} "
          f"roster={len(roster)} placeholders={len(placeholders)} "
          f"sanity=PASS (no roster row matches an existing case page)",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
