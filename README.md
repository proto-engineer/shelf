# Proto.Shelf

A hand-picked shelf of AI tools, startup credits and builder services. Free tiers first,
with an open-source alternative for every tool. Live at https://shelf.proto-engineer.com/


## Files

| File | What it is |
|---|---|
| `catalog.py` | The data. **The only file you edit by hand.** |
| `index.html` | The page. One file, no framework, no build step. Its inline `SEED` constant and the static `<main>` markup are both generated from the catalog. |
| `assets/` | Local images: the Proto.Engineer mark, the social card, offer screenshots. |
| `robots.txt`, `sitemap.xml` | SEO plumbing, written for the custom domain. |

## Editing the catalog

Every tool is a dict inside a category in `catalog.py`:

```python
{"name": "Supabase", "domain": "supabase.com", "free": True, "icon": "supabase",
 "use": "Postgres backend", "repo": "https://github.com/supabase/supabase", "oss": True,
 "alts": [("Appwrite", "appwrite.io", "Open backend platform", "appwrite")]},
```

| Key | Meaning |
|---|---|
| `name`, `domain`, `use` | Display name, link and logo lookup, one short line on the tile |
| `free` | True only for a recurring free plan. Trials and one-time credits do not count |
| `icon` | Simple Icons slug, verified against cdn.simpleicons.org. `""` falls back to the site icon |
| `href` | Optional deep link. Public URLs only, never links with auth or tracking IDs |
| `oss` | True when the tool itself is open source, open weights, or source-available fair-code |
| `repo` | Code link, shown in the popup when `oss` is set |
| `alts` | Open-source alternatives: `(name, domain, note[, simpleicons_slug])` |
| `offer`, `img` | Optional promo line and screenshot for the popup |

Plain-English popup descriptions live in the `DESCS` dict at the bottom of the same file.
Every tool needs one.

After editing, regenerate the page (the script injects `SEED` and the crawler-visible
static markup into `index.html`), then commit both files together:

```bash
python3 build_seed.py   # keep a copy of the generator next to the repo
git add catalog.py index.html && git commit && git push
```

GitHub Pages redeploys on push. Categories render alphabetically; order inside a
category is free-first.

## Logos

Nothing is stored. Tiles try Simple Icons first, then the company's own site icon,
then a letter tile. The footer credit and the optional logo.dev key slot remain in
`index.html` if crisper logos are ever wanted.
