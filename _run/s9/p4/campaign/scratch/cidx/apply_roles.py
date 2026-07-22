#!/usr/bin/env python3
"""CAMP-CIDX part 3: normalize C09 role-compound labels to the colon precedent.
role-paren  '*Key (X)*'  -> '*Key: X*'
role-comma  '*Key, X*'   -> '*Key: X*'  (Key-compounds only)
The 2 role-comma rows on '*Related (cross-ref, ...)*' (Karo L73, Jones L76) are
LEFT verbatim: they are standard '*Related (descriptor)*' labels (131 in corpus)
whose comma is descriptor-internal, not a Role separator; colon-izing would make
the anomalous '*Related:*' form. Display text only; wikilink/role words verbatim;
no em-dash added. Modes: dry (default) | --write."""
import sys, os

BASE = "content/cases/"
# (file, old_label, new_label). old_label must be unique in the file.
EDITS = [
 ("Arizona v. Gant.md", "*Key (Anchor)*", "*Key: Anchor*"),
 ("Arizona v. Roberson.md", "*Key (Progeny / Refinement)*", "*Key: Progeny / Refinement*"),
 ("Atwater v. City of Lago Vista.md", "*Key (Anchor)*", "*Key: Anchor*"),
 ("Berghuis v. Thompkins.md", "*Key (Anchor)*", "*Key: Anchor*"),
 ("City and County of San Francisco v. Sheehan.md", "*Key (Progeny / Refinement)*", "*Key: Progeny / Refinement*"),
 ("City of Indianapolis v. Edmond.md", "*Key (Progeny / Refinement)*", "*Key: Progeny / Refinement*"),
 ("Cone v. Bell.md", "*Key (Progeny / Refinement)*", "*Key: Progeny / Refinement*"),
 ("Delaware v. Prouse.md", "*Key (Progeny / Refinement)*", "*Key: Progeny / Refinement*"),
 ("District of Columbia v. Wesby.md", "*Key (Progeny / Refinement)*", "*Key: Progeny / Refinement*"),
 ("Haynes v. Washington.md", "*Key (Progeny / Refinement)*", "*Key: Progeny / Refinement*"),
 ("Hiibel v. Sixth Judicial Dist. Court.md", "*Key (Progeny / Refinement)*", "*Key: Progeny / Refinement*"),
 ("Kaupp v. Texas.md", "*Key (Progeny)*", "*Key: Progeny*"),
 ("Manson v. Brathwaite.md", "*Key (Anchor)*", "*Key: Anchor*"),
 ("Maryland v. Garrison.md", "*Key (Progeny / Refinement)*", "*Key: Progeny / Refinement*"),
 ("Michigan v. Summers.md", "*Key (Anchor)*", "*Key: Anchor*"),
 ("New York v. Belton.md", "*Key (Progeny / Refinement)*", "*Key: Progeny / Refinement*"),
 ("Rhode Island v. Innis.md", "*Key (Anchor)*", "*Key: Anchor*"),
 ("Strickler v. Greene.md", "*Key (Progeny / Refinement)*", "*Key: Progeny / Refinement*"),
 ("Taylor v. Riojas.md", "*Key (Limiting)*", "*Key: Limiting*"),
 ("Thornton v. United States.md", "*Key (Progeny / Refinement)*", "*Key: Progeny / Refinement*"),
 ("United States v. Basher.md", "*Key (Progeny / Refinement)*", "*Key: Progeny / Refinement*"),
 ("United States v. Garner.md", "*Key (Anchor)*", "*Key: Anchor*"),
 ("United States v. Grubbs.md", "*Key (Progeny / Refinement)*", "*Key: Progeny / Refinement*"),
 ("United States v. Jones.md", "*Key (Anchor)*", "*Key: Anchor*"),
 ("United States v. Leary.md", "*Key (Progeny / Refinement)*", "*Key: Progeny / Refinement*"),
 ("United States v. Padilla.md", "*Key (Progeny)*", "*Key: Progeny*"),
 ("Yarborough v. Alvarado.md", "*Key (Progeny / Refinement)*", "*Key: Progeny / Refinement*"),
 # role-comma (Key-compounds)
 ("Mooney v. Holohan.md", "*Key, Anchor (historical origin)*", "*Key: Anchor (historical origin)*"),
 ("Shipley v. California.md", "*Key, Limiting (contemporaneity)*", "*Key: Limiting (contemporaneity)*"),
 ("United States v. Jones.md", "*Key, cross-ref (GPS trespass; mosaic [[Common Legal Terms#concurring-opinion|concurrences]])*", "*Key: cross-ref (GPS trespass; mosaic [[Common Legal Terms#concurring-opinion|concurrences]])*"),
 ("United States v. Karo.md", "*Key, Anchor (interior context-flip)*", "*Key: Anchor (interior context-flip)*"),
]
# LEFT verbatim (documented): standard Related-paren, comma is descriptor-internal
SKIP = [
 ("United States v. Karo.md", "*Related (cross-ref, umbrella)*", "role-comma: standard Related-paren form (comma internal), colon N/A"),
 ("United States v. Jones.md", "*Related (cross-ref, mosaic seed for Carpenter)*", "role-comma: standard Related-paren form (comma internal), colon N/A"),
]

write = "--write" in sys.argv
EM = "—"
changed=0; errs=[]
for fn, old, new in EDITS:
    p = BASE+fn
    s = open(p, encoding="utf-8").read()
    c = s.count(old)
    if c != 1:
        errs.append((fn, old, "count=%d"%c)); continue
    ns = s.replace(old, new)
    # guard: no em-dash added anywhere; new label present; old gone
    if ns.count(EM) != s.count(EM):
        errs.append((fn, old, "em-dash count changed")); continue
    if write:
        open(p, "w", encoding="utf-8").write(ns)
    changed += 1
    print("  %-46s %s  ->  %s"%(fn, old, new))
print("="*50)
print("normalized: %d/31   skipped(Related): %d   errors: %d"%(changed, len(SKIP), len(errs)))
for e in errs: print("  ERR", e)
for fn,lbl,why in SKIP: print("  SKIP %-30s %s  [%s]"%(fn,lbl,why))
