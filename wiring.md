# wiring.md

Append-only change log for every code fix. Read top-to-bottom before any new fix in the same area.

Format: newest entries at top. Never delete entries — if superseded, add a new entry referencing the old one.

---

## [2026-11-05 21:00] Featured protolift band at top — this commit

**Symptom:** The founder asked for one featured component at the top of Proto.Shelf, protolift. The page had no way to feature a single product above the category list.
**Root cause:** catalog.py only modelled categories of tools and build_seed.py only generated `SEED` and the `<main>` category markup. The only top band (the "by Proto.Engineer" hero) is hand-written in the HTML shell, so a featured product would have had to be hand-typed into the generated file and its JSON-LD with no single source.
**Fix:** New `FEATURED` dict in `catalog.py`. `build_seed.py` now renders it between `<!-- featured:start -->` and `<!-- featured:end -->` at the top of `<main>` (above the hero), and upserts a `SoftwareApplication` node (`@id` `https://shelf.proto-engineer.com/#protolift`) into the page `@graph`. Band styles (`.feat*`) sit with the other styles in `index.html`, light only like the rest of the page.
**Files touched:** `catalog.py` (FEATURED at the end), `build_seed.py` (featured render, `ld_dump`, `upsert_ld`), `index.html` (markers, `.feat*` CSS, 640px, reduced-motion and forced-colours rules, regenerated output)
**Wiring mapped (callers/consumers of touched symbols):**
- `build_seed.py` is the only writer of `index.html` (README.md).
- `index.html` `render()` rewrites only `#main`, `#chips`, `#ladder`, `#foot`. The featured band is outside `#main`, so JS never overwrites it.
- `bindSpy()` observes `main section`. The band is an `<article>`, so the scroll spy ignores it.
- `.feat + .hero` pulls the existing hero up under the band. The hero itself is unchanged.
- grep: `FEATURED|featured|feat-` → only the new code.
**Blast radius:** 3 files, low. Static site, no shared modules.
**Tests run:** `python3 build_seed.py` twice → `OK: 12 shelves, 139 tools`, output byte-identical (idempotent). SEED and `<main>` markup unchanged. Headless check at 1440, 375 and 320: no sideways scroll at 320 (scrollWidth 320), both links 44px tall.
**Regression risks (for next fix in this area):**
- `upsert_ld` re-serialises the whole JSON-LD block with `ld_dump` (short flat lists and objects stay inline). Hand edits to the `@graph` must stay valid JSON or the build stops.
- The featured markers must stay inside `<main>` and outside `<div id="main">`, or `render()` will wipe the band.
- Outside links in the band use `rel="noopener noreferrer"`. Older tile links still use `rel="noopener"`.
**Related:** none.

---
