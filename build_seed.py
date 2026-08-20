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
open(f"{ROOT}/index.html", "w").write(new)
tools = sum(len(c["tools"]) for c in cat.CATALOG)
print(f"OK: {len(cat.CATALOG)} shelves, {tools} tools")
