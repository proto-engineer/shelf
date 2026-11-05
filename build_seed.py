"""Rebuild the inline SEED constant in index.html from catalog.py."""
import json, re, sys, importlib.util

import os
ROOT = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("catalog", f"{ROOT}/catalog.py")
cat = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cat)

seed = {"updated": "2026-08-20", "categories": []}
for c in sorted(cat.CATALOG, key=lambda c: c["name"].lower()):
    seed["categories"].append({
        "slug": c["slug"], "name": c["name"], "kind": c["kind"], "lad": c.get("lad", c["name"][:2]),
        "tools": [
            {
                "name": t["name"], "domain": t["domain"], "free": t["free"],
                "icon": t["icon"], "use": t["use"],
                "desc": cat.DESCS.get(t["name"], ""),
                **({"href": t["href"]} if t.get("href") else {}),
                **({"oss": True} if t.get("oss") else {}),
                **({"repo": t["repo"]} if t.get("repo") else {}),
                **({"offer": t["offer"]} if t.get("offer") else {}),
                **({"img": t["img"]} if t.get("img") else {}),
                **({"alts": [{"name": a[0], "domain": a[1], "note": a[2],
                              **({"icon": a[3]} if len(a) > 3 else {})} for a in t["alts"]]}
                   if t.get("alts") else {}),
            }
            for t in c["tools"]
        ],
    })

js = "const SEED = " + json.dumps(seed, separators=(",", ":")) + ";"
html = open(f"{ROOT}/index.html").read()
new, count = re.subn(r"const SEED = \{.*?\};", lambda m: js, html, count=1, flags=re.S)
if count != 1:
    sys.exit("SEED line not found")

# Pre-render the catalog into <main> so non-JS crawlers (GPTBot, ClaudeBot,
# PerplexityBot, Bing) see every tool + link; the JS render() hydrates over it.
from html import escape as e
def tile_html(t):
    href = t.get("href") or f"https://{t['domain']}"
    badge = '<span class="free">free</span>' if t["free"] else ""
    return (f'<a class="tile" href="{e(href)}" target="_blank" rel="noopener">{badge}'
            f'<span class="nm">{e(t["name"])}</span>'
            f'<span class="use">{e(t["use"])}</span></a>')
main_html = "".join(
    f'<section id="{e(c["slug"])}"><div class="head"><div class="head-top">'
    f'<h2>{e(c["name"])}</h2><span class="rule"></span>'
    f'<span class="n">{len(c["tools"])}</span></div>'
    f'<p class="kind">{e(c["kind"])}</p></div>'
    f'<div class="grid">{"".join(tile_html(t) for t in c["tools"])}</div></section>'
    for c in seed["categories"])
new, count = re.subn(r'(<div id="main">).*?(</div>\s*</main>)',
                     lambda m: m.group(1) + main_html + m.group(2), new, count=1, flags=re.S)
if count != 1:
    sys.exit("main element not found")

# Featured band (catalog.FEATURED): static markup between the featured markers at
# the top of <main>, plus a SoftwareApplication node in the page's JSON-LD @graph.
# render() never touches it, so it shows with or without JS.
f = cat.FEATURED
EXT = 'target="_blank" rel="noopener noreferrer"'
NEW_TAB = '<span class="vh"> (opens in a new tab)</span>'
CHECK = ('<svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" '
         'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path d="M3.5 8.5l3 3 6-7"/></svg>')
LIFT = ('<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" '
        'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<path d="M12 16V4M6.5 9.5 12 4l5.5 5.5M5 20h14"/></svg>')
featured_html = (
    f'<article class="feat" aria-labelledby="feat-h">'
    f'<div class="feat-top"><span class="feat-mark" aria-hidden="true">{LIFT}</span>'
    f'<div class="feat-id"><p class="feat-eye"><span class="feat-tag">Featured</span>'
    f'<span>by {e(f["by"])}</span></p>'
    f'<h2 id="feat-h">{e(f["name"])}</h2></div></div>'
    f'<p class="feat-line">{e(f["line"])}</p>'
    f'<ul class="feat-pts">{"".join(f"<li>{CHECK}<span>{e(p)}</span></li>" for p in f["points"])}</ul>'
    f'<div class="feat-act">'
    f'<a class="feat-go" href="{e(f["href"])}" {EXT}>{e(f["cta"])}{NEW_TAB}'
    f'<span aria-hidden="true">→</span></a>'
    f'<a class="feat-src" href="{e(f["repo"])}" {EXT}>{e(f["repo_label"])}{NEW_TAB}</a>'
    f'</div>'
    f'<p class="feat-note"><span class="feat-tag">Free</span><span class="feat-tag">Open source</span>'
    f'<span>{e(f["license"])} · {e(f["cta_note"])}</span></p>'
    f'</article>')
new, count = re.subn(r"(<!-- featured:start -->).*?(<!-- featured:end -->)",
                     lambda m: m.group(1) + featured_html + m.group(2), new, count=1, flags=re.S)
if count != 1:
    sys.exit("featured markers not found")

LD_ID = f"https://shelf.proto-engineer.com/#{f['id']}"
ld_node = {
    "@type": "SoftwareApplication",
    "@id": LD_ID,
    "name": f["name"],
    "description": f["line"],
    "url": f["href"],
    "sameAs": [f["repo"]],
    "applicationCategory": "DeveloperApplication",
    "featureList": f["points"],
    "license": f["license_url"],
    "isAccessibleForFree": True,
    "publisher": {"@id": "https://www.proto-engineer.com/#organization"},
}
def ld_dump(v, ind=0):
    """json.dumps(indent=2), but short flat lists and objects stay on one line,
    the way the hand-written @graph was laid out."""
    flat = lambda x: not any(isinstance(y, (dict, list)) for y in (x.values() if isinstance(x, dict) else x))
    j = lambda x: json.dumps(x, ensure_ascii=False)
    pad, inner = " " * ind, " " * (ind + 2)
    if isinstance(v, dict):
        one = "{ " + ", ".join(f"{j(k)}: {j(x)}" for k, x in v.items()) + " }"
        if flat(v) and len(one) <= 72:
            return one
        return "{\n" + ",\n".join(f"{inner}{j(k)}: {ld_dump(x, ind + 2)}" for k, x in v.items()) + f"\n{pad}}}"
    if isinstance(v, list):
        one = "[" + ", ".join(j(x) for x in v) + "]"
        if flat(v) and len(one) <= 72:
            return one
        return "[\n" + ",\n".join(f"{inner}{ld_dump(x, ind + 2)}" for x in v) + f"\n{pad}]"
    return j(v)

def upsert_ld(m):
    data = json.loads(m.group(2))
    data["@graph"] = [n for n in data["@graph"] if n.get("@id") != LD_ID] + [ld_node]
    return m.group(1) + ld_dump(data) + m.group(3)
new, count = re.subn(r'(<script type="application/ld\+json">\n)(.*?)(\n</script>)',
                     upsert_ld, new, count=1, flags=re.S)
if count != 1:
    sys.exit("JSON-LD block not found")
open(f"{ROOT}/index.html", "w").write(new)
tools = sum(len(c["tools"]) for c in cat.CATALOG)
print(f"OK: {len(cat.CATALOG)} shelves, {tools} tools")
