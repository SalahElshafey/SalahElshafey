# Intelligence, engineered

The profile follows one idea: **DATA → MODELS → SYSTEMS**. The hero turns that path into an original schematic: source nodes converge on three abstract model planes, then signals leave for an application, a vision system, and a device. It is an illustration of the engineering lifecycle, not a trace of a running model.

## Composition and hierarchy

The hero keeps the existing circuit vocabulary, midnight palette, and precise line work. A large, fixed headline carries the first impression; thin orbital construction lines frame the model. Motion stays inside the diagram. Name, positioning, project scope, technologies, and contacts also appear as native Markdown.

Edge SLM is the primary feature, with an animated provenance diagram. Distributed fine-tuning and GPT Visualization follow as full-width features. Wearable vision, exercise recognition, and the Android app use compact illustrations and shorter entries. All six existing projects remain linked. Existing vector compositions were retained and their palettes aligned with the new artwork.

The toolbox uses labeled groups and the existing licensed icons. There are no proficiency meters. GitHub activity uses direct links, avoiding a dependency on third-party statistics services. A terminal illustration was omitted because it repeated the introduction without adding engineering context. Three animated placements establish the motion hierarchy.

## Palette and typography

| Role | Dark | Light |
| --- | --- | --- |
| Background | `#080D19` | `#F7FAFF` |
| Model/card surface | `#0E1728` | `#EBF1FA` |
| Primary text | `#F0F5FC` | `#101E38` |
| Secondary text | `#A0B2CB` | `#4A607D` |
| Data / primary accent | `#45DBFF` | `#006B9C` |
| Model / violet accent | `#AD96FF` | `#6941C6` |
| Systems / teal accent | `#49E3C2` | `#087D68` |

Generated images use DejaVu Sans for headlines and DejaVu Sans Mono for schematic labels. Fonts are rasterized into assets; visitors download no fonts. Existing SVGs retain their system-font stacks. Decorative construction lines deliberately use lower contrast than text.

## Motion and accessibility

All GIFs loop over **9.6 seconds**, with 160 frames at 60 ms per frame. Signals enter from data sources, activate small marks on the stacked planes, and leave toward systems. Paths use staggered phases; particles fade at their endpoints so the last-to-first transition is continuous. No text disappears, no scene zooms, and no large area flashes.

The PNG companions contain the complete first-frame composition. `<picture>` puts reduced-motion PNG sources before GIF sources, with separate light/dark and mobile selections. The hero, pipeline, and Edge SLM diagram have purpose-built mobile compositions selected at viewport widths up to 600 px. Desktop hero dimensions are 1200 × 500; mobile dimensions are 720 × 760. Markdown carries the same essential information independently of imagery.

GIFs use a shared 128-color palette within each file, no dithering, and optimized frame differences. Only one variant per animated placement is displayed. See [validation](VALIDATION.md) for measurements and rendering limits.

## Regenerate the artwork

Viewing or editing the Markdown requires no install. Regeneration needs Python 3.10+, Pillow, and DejaVu Sans fonts. On Debian/Ubuntu the fonts are supplied by `fonts-dejavu-core`; the script expects `/usr/share/fonts/truetype/dejavu/`. The original art is procedural; no stock imagery, model downloads, external image APIs, or credentials are required.

From the repository root:

```bash
python3 -m venv /tmp/profile-assets-venv
/tmp/profile-assets-venv/bin/python -m pip install -r scripts/requirements-assets.txt
/tmp/profile-assets-venv/bin/python scripts/generate_assets.py
/tmp/profile-assets-venv/bin/python scripts/validate_assets.py
git diff --check
```

If Pillow is already installed, the shorter commands are:

```bash
python3 scripts/generate_assets.py
python3 scripts/validate_assets.py
```

For a quick composition pass, use `python3 scripts/generate_assets.py --stills`. Regenerate the GIFs before committing so static companions and animation match. To update one family, use `--only hero`, `--only pipeline`, or `--only edge`; each regenerates both themes and both viewport compositions. Output paths resolve relative to the script, so invocation from other directories works too.

Change geometry, text, palette, or timing in [generate_assets.py](../scripts/generate_assets.py). Maintain frame timing as a multiple of 10 ms, which GIF supports. Edit the existing `assets/project-*.svg` pairs directly when changing those vector illustrations. Do not edit Devicon source artwork without revisiting its attribution.

## Review after an edit

Run the validator, inspect actual first and intermediate frames, and review the README at desktop and narrow widths in both themes. Check reduced-motion selection as well as normal GIF playback. Keep text away from the diagram bounds. Recheck project descriptions against source before claiming any new capability; pinned references live in [the asset notes](../assets/README.md).

The README uses Markdown plus supported `a`, `picture`, `source`, `img`, `br`, `sub`, and `strong` elements. It contains no CSS, JavaScript, iframe, or video dependency. Local GitHub-style previews approximate layout; review GitHub's hosted rendering before considering publication visually verified. No GitHub Actions workflow is needed to maintain these local assets.

## Website and contact links

The personal website now leads the contact links at the top of the profile. A linked “Beyond the README” card introduces it again beside the closing invitation. The exact destination is `https://salah-elshafey.netlify.app/`.

Website, email, LinkedIn, resume, and GitHub links use original SVG button artwork with consistent line icons, directional arrows, fine borders, and subtle surface gradients. The website uses a stronger blue surface to establish hierarchy. Every button is a normal anchor around a theme-aware image, so GitHub does not need to support custom CSS or JavaScript. Each displayed button is 136 × 45 px; inline links wrap naturally on narrow screens. The website card has a separate mobile composition. Native website and email links remain readable below the buttons.

Regenerate these 14 SVG files with the standard library alone:

```bash
python3 scripts/generate_contact_assets.py
python3 scripts/validate_assets.py
```

The button/card generator does not touch the animated assets. Edit `THEMES`, `LABELS`, or the vector geometry in `scripts/generate_contact_assets.py`; README anchors own the destinations. All button icons are original line drawings and require no additional icon library.
