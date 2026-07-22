#!/usr/bin/env python3
"""CAMP-CIDX holding em-dash renovation applier.
Per-index transform spec over the frontmatter-scan order (holdings_todo.json).
Modes: dry (default, verify+diff) | --write.
Doctrine S1 A7/A8: paren-pair / comma / colon / semicolon / period-split / drop.
Only punctuation around unmasked em-dashes changes; all other text byte-identical."""
import json, os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", "..", "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "scripts"))
sys.path.insert(0, os.path.join(REPO, "scripts", "lint"))
import _common as c
import lint10_emdash as L
import build_case_index as B

EM = "—"
todo = json.load(open(os.path.join(HERE, "holdings_todo.json")))

# spec: index -> ("pair"[,"comma"]) | ("single", code) | ("snippet",[(old,new)...])
# codes: comma colon semicolon period
SPEC = {
 0:("single","period"),1:("single","comma"),2:("pair",),3:("pair",),4:("single","colon"),
 5:("pair",),6:("single","comma"),7:("single","colon"),8:("pair",),9:("single","colon"),
 10:("single","comma"),11:("single","colon"),12:("pair",),13:("snippet",[(" —…","…")]),
 14:("pair",),15:("single","comma"),16:("single","colon"),17:("single","period"),
 18:("single","colon"),19:("pair","comma"),20:("pair",),21:("single","period"),
 22:("single","period"),23:("single","period"),24:("single","comma"),25:("single","period"),
 26:("single","period"),27:("single","comma"),28:("pair",),29:("pair",),
 30:("single","comma"),31:("snippet",[("Massiah — and the Sixth","Massiah. The Sixth")]),
 32:("single","comma"),33:("single","colon"),34:("single","comma"),35:("single","colon"),
 36:("single","comma"),37:("single","colon"),38:("pair",),39:("snippet",[(" —…","…")]),
 40:("pair",),41:("single","colon"),42:("single","colon"),43:("single","period"),
 44:("single","colon"),45:("single","period"),46:("single","colon"),47:("pair",),
 48:("snippet",[(" —…","…")]),49:("single","comma"),50:("pair",),51:("single","comma"),
 52:("single","colon"),53:("single","period"),54:("single","colon"),55:("pair",),
 56:("single","period"),57:("single","comma"),58:("pair",),59:("single","colon"),
 60:("pair",),61:("pair",),62:("single","period"),63:("pair",),64:("single","colon"),
 65:("single","colon"),66:("single","colon"),67:("single","colon"),68:("single","colon"),
 69:("pair",),70:("single","comma"),71:("single","period"),72:("pair",),73:("single","colon"),
 74:("single","comma"),75:("pair",),76:("single","colon"),77:("pair",),78:("single","comma"),
 79:("pair",),80:("pair",),81:("single","colon"),82:("pair",),83:("single","colon"),
 84:("pair",),85:("single","comma"),86:("pair",),87:("pair",),88:("pair",),
 89:("single","comma"),90:("pair",),91:("single","colon"),92:("single","colon"),
 93:("single","colon"),94:("pair",),95:("single","semicolon"),96:("pair",),
 97:("single","colon"),98:("single","colon"),99:("snippet",[("the area — and because","the area. Because")]),
 100:("single","period"),101:("pair",),102:("single","comma"),103:("single","colon"),
 104:("single","comma"),105:("single","comma"),106:("single","period"),107:("single","colon"),
 108:("single","comma"),109:("single","colon"),110:("single","comma"),111:("pair",),
 112:("single","comma"),113:("pair",),114:("single","period"),115:("pair",),116:("pair",),
 117:("pair",),118:("single","colon"),119:("snippet",[("circumstances — and here","circumstances. Here")]),
 120:("pair",),121:("pair","comma"),122:("pair",),123:("single","colon"),124:("pair",),
 125:("pair",),126:("single","colon"),127:("pair",),128:("single","colon"),
 129:("single","comma"),130:("single","period"),131:("single","colon"),132:("pair",),
 133:("pair",),134:("pair",),135:("pair",),136:("pair",),137:("pair",),138:("pair",),
 139:("single","comma"),140:("pair","comma"),141:("pair","comma"),142:("pair",),
 143:("pair",),144:("pair","comma"),145:("pair","comma"),146:("pair",),147:("single","comma"),
 148:("single","period"),149:("pair",),150:("pair",),151:("pair",),152:("pair",),
 153:("single","comma"),154:("pair",),155:("pair",),156:("pair",),157:("pair",),
 158:("pair",),159:("pair",),160:("pair","comma"),161:("single","comma"),162:("single","colon"),
 163:("single","comma"),164:("single","comma"),165:("single","colon"),166:("single","colon"),
 167:("pair",),168:("pair",),
}

def cap_first(s):
    for i,ch in enumerate(s):
        if ch.isalpha():
            return s[:i]+ch.upper()+s[i+1:]
    return s

def transform(h, spec):
    kind=spec[0]
    if kind=="pair":
        parts=h.split(" — ")
        assert len(parts)==3, "pair expects 2 em-dashes, got %d"%(len(parts)-1)
        tail=", " if (len(spec)>1 and spec[1]=="comma") else " "
        return parts[0]+" ("+parts[1]+")"+tail+parts[2]
    if kind=="single":
        parts=h.split(" — ")
        assert len(parts)==2, "single expects 1 em-dash, got %d"%(len(parts)-1)
        A,Bp=parts
        code=spec[1]
        if code=="comma": return A+", "+Bp
        if code=="colon": return A+": "+Bp
        if code=="semicolon": return A+"; "+Bp
        if code=="period": return A+". "+cap_first(Bp)
        raise ValueError(code)
    if kind=="snippet":
        out=h
        for old,new in spec[1]:
            assert out.count(old)==1, "snippet %r count=%d"%(old,out.count(old))
            out=out.replace(old,new)
        return out
    raise ValueError(kind)

def raw_holding_lineno(text):
    for idx,ln in enumerate(text.split("\n")[1:], start=2):
        if ln.strip()=="---": break
        if re.match(r"^holding:\s*(.*\S)\s*$", ln): return idx
    return None

write = "--write" in sys.argv
verbose = "-v" in sys.argv
changed=0; errors=[]
for i,it in enumerate(todo):
    spec=SPEC.get(i)
    if spec is None:
        errors.append((i,it['title'],"NO SPEC")); continue
    h=it['holding']
    try:
        nh=transform(h,spec)
    except AssertionError as e:
        errors.append((i,it['title'],"transform-fail: %s"%e)); continue
    # validations
    if nh.count(EM)!=0:
        errors.append((i,it['title'],"residual em-dash: %r"%[nh[max(0,j-8):j+8] for j in range(len(nh)) if nh[j]==EM])); continue
    if nh==h:
        errors.append((i,it['title'],"no change")); continue
    # ensure no chars added other than transform: strip all em/paren/punct diffs -> letters equal
    # (snippet transforms may intentionally drop a coordinating "and" on a period-split)
    def letters(s): return re.sub(r"[^0-9A-Za-z]","",s)
    la,lb=letters(h),letters(nh)
    if spec[0]!="snippet" and la.lower()!=lb.lower():
        errors.append((i,it['title'],"letter-drift:\n  OLD=%s\n  NEW=%s"%(la,lb))); continue
    if verbose:
        print("### %03d %s [%s]"%(i,it['title'],"/".join(map(str,spec))))
        print("  -",h)
        print("  +",nh); print()
    if write:
        p=it['file']; text=c.read_text(p)
        ln=raw_holding_lineno(text)
        lines=text.split("\n")
        newline="holding: "+json.dumps(nh,ensure_ascii=False)
        lines[ln-1]=newline
        with open(p,"w",encoding="utf-8") as fh:
            fh.write("\n".join(lines))
        # verify round-trip
        chk=B.read_holding(c.read_text(p))
        assert chk==nh, "roundtrip mismatch %s"%p
    changed+=1

print("="*60)
print("planned/applied changes: %d / 169"%changed)
print("errors: %d"%len(errors))
for e in errors: print("  ERR",e)
