# Shelf

A logo grid. Six shelves. Free tools first. One plain line saying what each shelf is for.

## Files

| File | What it is |
|---|---|
| `catalog.py` | The list. **The only file you edit by hand.** |
| `build.py` | Turns the catalog into `data/*.json` and writes `index.html`. |
| `update.py` | Daily job. Checks every domain still resolves. No API key needed. |
| `index.html` | The page. One file, no framework, no build step. |
| `data/` | One JSON per shelf. This is what goes in the bucket. |

## Adding a tool

One line in `catalog.py`:

```python
("Cursor", "cursor.com", True, ""),
#  name     domain        free?  Simple Icons slug (optional)
```

Then `python3 build.py`.

## Logos — how it works

You never download or store a logo. When someone opens the page, their browser
asks logo.dev for each domain and the logo comes back live. Your catalogue only
holds the domain name.

**Setup is one line.** Get your publishable key from the logo.dev dashboard
(it starts with `pk_`) and paste it into `index.html`:

```js
const LOGO_DEV_KEY = "pk_xxxxx";
```

The key is meant to be public — it sits in the page source by design. Lock it to
your own domain in the logo.dev dashboard so nobody else burns your quota.

If logo.dev misses a brand, the page falls back on its own, in this order:

1. **logo.dev** — the real company logo, by domain
2. **Simple Icons** — official brand SVG, free, no key. Set the 4th field in
   `catalog.py` to the slug (e.g. `"openai"`). Browse slugs at simpleicons.org.
3. **The company's own site icon** — DuckDuckGo, then Google
4. **A letter tile** — only if all four miss

Clearbit's free logo API was shut down in December 2025, which is why the old
approach stopped working.

**Attribution.** The footer carries a Logo.dev link, which is what their free
Community plan asks for. Leave it there.

## Getting it live — four steps

1. **Preview** — open `index.html`. Works offline; a snapshot is baked in.
2. **Upload `data/`** to Cloudflare R2, S3, or a public GitHub repo. Make it CORS-readable.
3. **Point at it** — one line near the bottom of `index.html`:
   `const DATA_BASE = "https://your-bucket/data";`
4. **Host `index.html`** on Cloudflare Pages or GitHub Pages. Free.

`.github/workflows/daily.yml` then runs `update.py` every morning at 07:00 IST.

## Before you publish

- **Get the logo.dev key.** Without it, roughly a third of these brands fall back to
  site icons, which look rougher than the rest of the grid.
- **Check the `free` flags.** Free tiers change constantly. Verify each one.
- **No submission form.** Adding a tool is a code change. That's what keeps it clean.
