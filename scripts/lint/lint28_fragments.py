#!/usr/bin/env python3
"""
LINT-28 — external text-fragment well-formedness (S8 R13(d), R4/R5 syntax half).

SYNTAX ONLY. The SEMANTIC guarantee (a fragment matches exactly one span of the
source opinion) is R5's, enforced at WRITE time against S2's CACHED opinion text
by `scripts/s8/fragments.py` — CI NEVER calls CourtListener (S1 A1/L4'). This lint
checks that every `#:~:text=` link already in content is a well-formed WICG text
fragment on an allowed host with valid percent-encoding.

  For every `#:~:text=` URL in content/**/*.md:
    (1) HOST — the URL host must be CourtListener or an S2 R14 whitelisted source
        (Justia, Google Scholar, Cornell LII, official court/reporter site, and the
        A16/A17 off-CL sources: BAILII, Founders' Constitution/English Reports).
        R5 derives fragments from CL cached text, so in practice host == CL; a
        fragment on any other host = HIGH.
    (2) WICG GRAMMAR — value = `[prefix-,]textStart[,textEnd][,-suffix]`: 1-4
        comma-parts; the prefix (if present) is the first part ending `-`, the
        suffix (if present) is the last part starting `-`, leaving 1-2 non-empty
        core terms (textStart[,textEnd]). Any empty term / >4 parts / missing
        start = HIGH.
    (3) ENCODING — per the R5/SD6 generator contract each term is percent-encoded
        with `-` `,` `&` ALSO encoded (%2D/%2C/%26) so they cannot collide with the
        directive delimiters; every `%` is followed by two hex digits and terms
        carry no whitespace. A raw `-`/`&`/bad-`%`/space in a term = HIGH.

Multiple `&text=` directives on one URL are each validated. READ-ONLY, stdlib only.

Usage: python3 lint28_fragments.py [glob ...]   ( --self-test for the gate )
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-28"

# CL + S2 R14 (+A16/A17) whitelist host suffixes.
# CR-S8-7: NARROW, not the bare parent domains. `_host_ok` accepts any host that
# `endswith("." + s)`, so a bare `google.com`/`cornell.edu`/`uchicago.edu` would
# admit ANY subdomain (drive.google.com, admissions.cornell.edu) and make the
# narrow Scholar/LII/press-pubs entries dead — silently widening the verified-
# authority trust boundary past the docstring's Scholar / Cornell LII / Founders'
# Constitution sources.
ALLOWED_HOST_SUFFIXES = (
    "courtlistener.com",
    "justia.com",
    "scholar.google.com",
    "law.cornell.edu",
    "supremecourt.gov",
    "bailii.org", "commonlii.org",
    "press-pubs.uchicago.edu",
)

# a URL bearing a text fragment (stops at markdown/quote/space delimiters)
_FRAG_URL_RE = re.compile(r"https?://[^\s)\]\"'<>]*#:~:text=[^\s)\]\"'<>]*")
_PCT_RE = re.compile(r"%[0-9A-Fa-f]{2}")
_HEXPAIR_OK = re.compile(r"^(?:[^%]|%[0-9A-Fa-f]{2})*$")


def _host_ok(url):
    m = re.match(r"https?://([^/]+)", url)
    if not m:
        return False
    host = m.group(1).lower().split("@")[-1].split(":")[0]
    return any(host == s or host.endswith("." + s) for s in ALLOWED_HOST_SUFFIXES)


def _valid_term(term):
    """A single percent-encoded fragment term (delimiters already stripped)."""
    if term == "":
        return "empty term"
    if any(ch.isspace() for ch in term):
        return "whitespace in term (must be percent-encoded)"
    if "-" in term or "&" in term:
        return "raw '-' or '&' in term (must be %2D/%26 per the generator contract)"
    if not _HEXPAIR_OK.match(term):
        return "invalid percent-encoding (a %% not followed by two hex digits)"
    return None


def _validate_text_value(value):
    """Validate one `text=` directive VALUE. Returns an error string or None."""
    if value == "":
        return "empty text directive"
    parts = value.split(",")
    if len(parts) > 4:
        return "too many comma parts (max prefix,start,end,suffix)"
    core = list(parts)
    prefix = suffix = None
    if core and core[0].endswith("-"):
        prefix = core[0][:-1]
        core = core[1:]
    if core and core[-1].startswith("-"):
        suffix = core[-1][1:]
        core = core[:-1]
    if len(core) < 1 or len(core) > 2:
        return "malformed grammar (need textStart[,textEnd] between prefix/suffix)"
    terms = []
    if prefix is not None:
        terms.append(prefix)
    terms.extend(core)
    if suffix is not None:
        terms.append(suffix)
    for t in terms:
        err = _valid_term(t)
        if err:
            return err
    return None


def validate_fragment_url(url):
    """Return a list of error strings for one fragment-bearing URL (empty == ok)."""
    errs = []
    if not _host_ok(url):
        host = re.match(r"https?://([^/]+)", url)
        errs.append("fragment on a non-whitelisted host: %s (host in S2 R14 "
                    "whitelist ∪ CourtListener required)"
                    % (host.group(1) if host else url[:60]))
    frag = url.split("#:~:", 1)[1]      # after the fragment directive marker
    directives = frag.split("&")
    text_dirs = [d for d in directives if d.startswith("text=")]
    if not text_dirs:
        errs.append("no `text=` directive after #:~:")
    for d in text_dirs:
        err = _validate_text_value(d[len("text="):])
        if err:
            errs.append(err)
    return errs


def check_file(path):
    out = []
    text = c.read_text(path)
    _fm, body, start = c.split_frontmatter(text)
    fenced = c.fenced_line_numbers(body.split("\n"))
    for i, line in enumerate(body.split("\n")):
        if i in fenced:
            continue
        for m in _FRAG_URL_RE.finditer(line):
            for err in validate_fragment_url(m.group(0)):
                out.append(c.make_violation(
                    LINT, path, start + i, c.HIGH,
                    "malformed text-fragment link: %s [S8 R13d]" % err))
    return out


def run(paths=None):
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path))
    return out


# --------------------------------------------------------------------------
# self-test
# --------------------------------------------------------------------------

FIXTURE = os.path.join(c.HERE, "fixtures")


def self_test():
    ok = True

    def check(name, got, want):
        nonlocal ok
        p = (got == want)
        ok = ok and p
        sys.stderr.write("[self-test] %-46s -> %s (got=%s want=%s)\n"
                         % (name, "OK" if p else "MISMATCH", got, want))

    CL = "https://www.courtlistener.com/opinion/1/x/"
    # unit: host
    check("host-cl-ok", _host_ok(CL + "#:~:text=a"), True)
    check("host-cornell-ok", _host_ok("https://www.law.cornell.edu/x#:~:text=a"), True)
    check("host-scholar-ok", _host_ok("https://scholar.google.com/x#:~:text=a"), True)
    check("host-bad", _host_ok("https://evil.example.com/x#:~:text=a"), False)
    # CR-S8-7: bare parent domains must NOT admit arbitrary subdomains
    check("host-drive-google-bad", _host_ok("https://drive.google.com/x#:~:text=a"), False)
    check("host-admissions-cornell-bad",
          _host_ok("https://admissions.cornell.edu/x#:~:text=a"), False)
    check("host-uchicago-bare-bad", _host_ok("https://www.uchicago.edu/x#:~:text=a"), False)
    # unit: value grammar + encoding
    check("value-start-only-ok", _validate_text_value("rests%20rather%20on"), None)
    check("value-start-end-ok",
          _validate_text_value("the%20start,the%20end"), None)
    check("value-prefix-suffix-ok",
          _validate_text_value("pre%20-,mid%20term,-suf%20fix"), None)
    check("value-empty-fails", _validate_text_value("") is not None, True)
    check("value-badpct-fails", _validate_text_value("bad%2") is not None, True)
    check("value-rawdash-fails",
          _validate_text_value("well-settled") is not None, True)
    check("value-emptystart-fails",
          _validate_text_value(",word") is not None, True)
    check("value-toomany-fails",
          _validate_text_value("a-,b,c,-d,e") is not None, True)

    vf = check_file(os.path.join(FIXTURE, "lint-28-fail.md"))
    check("fail-fixture-HIGH>=4",
          sum(1 for v in vf if v["severity"] == c.HIGH) >= 4, True)
    vp = check_file(os.path.join(FIXTURE, "lint-28-pass.md"))
    check("pass-fixture-clean", vp, [])

    sys.stderr.write("[self-test] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    c.cli_main(run, LINT)
