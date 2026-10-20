# Portfolio validation

Latest refinement checked on 20 October 2026. Browser results below describe local GitHub-style previews; hosted GitHub rendering is not implied.

## Full portfolio action refinement

- All standalone root README actions now use image-backed links: four navigation pills, six featured repository buttons, four supporting-project cards, two GitHub activity cards, and contact/social buttons. All six featured illustrations also link to their repository.
- The root README contains no remaining plain Markdown action links. All 19 prior external destinations are preserved exactly, including the website, resume query string, GitHub activity tabs, and social accounts.
- `python3 scripts/validate_assets.py` passes: 114 local image references, section anchors, alt metadata, the HTML allowlist, 86 valid SVGs, and all 12 unchanged GIF variants.
- Sixteen local Chromium combinations passed at 1280, 768, 390, and 320 px, with both color schemes and motion preferences. All 45 displayed images load, all 35 links contain artwork, each action resolves to its exact catalogue destination, navigation anchors resolve, mobile repository variants are selected correctly, and no horizontal overflow occurs.
- Text bounds were inspected in all 48 new SVG variants; no text extends outside its image. Desktop and mobile screenshots were reviewed, including project cards, the supporting-project grid, navigation, and the closing contact area.
- All 62 contact/action SVGs regenerate byte for byte from a different working directory. The 48 new variants total 69,742 bytes; selected additional artwork totals 24,824 bytes for dark desktop before caching/request overhead.
- No technical project descriptions, achievements, or existing animated assets were changed. `git diff --check` passes. Hosted GitHub rendering remains outside these local preview checks.

## Website and contact refinement

- Added the exact personal website URL: `https://salah-elshafey.netlify.app/`.
- Introduced Website, Email me, LinkedIn, Resume, and GitHub SVG buttons in both themes, plus a website invitation card with desktop/mobile compositions.
- `python3 scripts/validate_assets.py` passes: 66 README image references, all 18 prior external destinations preserved, 38 valid SVGs, and all 12 existing GIF variants still pass.
- Local Chromium checked 16 width/theme/motion combinations at 1280, 768, 390, and 320 px: all 27 images load, all 11 image-link anchors use expected destinations, theme and mobile artwork selection matches, and no horizontal overflow occurs. Normal/reduced motion selection still works.
- Actual desktop and mobile contact screenshots were reviewed. Buttons wrap naturally at narrow widths; all card text and controls remain inside their compositions.
- All 14 new SVG files reproduce byte for byte when regenerated from a different working directory. They total 20,022 bytes across all variants. The selected five buttons and desktop card total 8,047 bytes in dark mode before browser caching and request overhead; repeated button rows share the same assets.
- Website HTTPS availability could not be confirmed: this environment's proxy denied the request with a 403 tunnel error. The supplied URL was preserved exactly. Existing social-link access limitations still apply.
- The new assets need only Python's standard library: `python3 scripts/generate_contact_assets.py`. No new package, service, secret, or workflow is required.

The following sections retain the original redesign audit and its earlier measurements.

## Content and source audit

The checkout started clean at `86b6d47fd886b96414ebcbbccfc25d24b755da96`. The existing README, all SVG compositions, icon license, asset documentation, and recent history were inspected before editing. All six featured projects, four supporting project destinations, and existing professional/social links remain present. No metrics, employers, production deployments, or individual credit for team-wide work were added.

All six upstream HEAD revisions still match the [pinned references](../assets/README.md#project-references). Their current READMEs and the following representative source were inspected:

| Project | Source inspected | Boundary retained in the profile |
| --- | --- | --- |
| Edge SLM | `pipeline/ingestion/schema.py`, `pipeline/ingestion/chunking.py`, `GUI/app.py` | Ingestion, provenance, chunking, and task preparation are implemented; later model stages remain downstream. |
| Distributed fine-tuning | `Cluster/Project 1 - Fine Tuning Distilgpt2/finetune_lora_distilgpt2.py`, `Cluster/Project 2 - Course Project/finetune_lora_opt_pp.py`; SLURM launchers identified | LoRA, DDP, and pipeline-parallel experiments; no public access to the private cluster or new performance claims. |
| GPT Visualization | Code cells in `GPT2 From Scratch.ipynb` and `Aufgaben.ipynb` | Educational transformer components and exercises. |
| Aria recognition | `1-Train.py`, `YOLOv8n_Live_Streaming_AriaGlasses_Code.py` | YOLOv8n training and streaming experiments, with README-documented connection limitations. |
| VR fitness | `Train.py`, `Test_LiveStream.py` on the default `MachineLearning` branch | Training, inference, and MQTT class messages; Unity and sensing belong to the wider team system. |
| Home Security App | `app/build.gradle`, `MainActivity.java` through `MainActivity5.java` | Firebase authentication, locker state, buzzer alerts, and timestamped history; no camera-streaming claim. |

Upstream applications were not installed or executed; this change is a profile and asset pipeline redesign.

## Automated asset checks

Run from the repository root with `python3 scripts/validate_assets.py`:

- All 42 local README image references resolve; section links resolve.
- All 18 distinct original external destinations are preserved exactly.
- Every image has alt metadata; redundant technology icons use empty alt text next to text labels.
- README HTML passes a restricted allowlist, with no custom CSS, JavaScript, or event handlers.
- All 24 existing SVGs parse, with no script or external resource dependency.
- All 12 GIFs fully decode: 160 frames, 60 ms/frame, 9.6-second duration, infinite loop.
- Each GIF changes between sampled frames, has the expected dimensions, and passes a last-to-first frame-difference check.
- Hero text stays identical between sampled frames. Each PNG matches its GIF's first frame after applying the GIF palette, within a 0.25 RMS channel tolerance for palette compaction on the 0–255 scale.
- Every GIF remains below the 3 MB target. `git diff --check` passes.

The Edge SLM family was regenerated from `/tmp` and all eight GIF/PNG outputs matched their earlier SHA-256 hashes byte for byte. Generated files are replaced atomically, so a preview cannot read a partly written image during regeneration.

## Asset budget

| Animated placement | Dark desktop | Light desktop | Dark mobile | Light mobile |
| --- | ---: | ---: | ---: | ---: |
| Hero | 242,894 B | 237,098 B | 249,461 B | 240,592 B |
| Engineering pipeline | 109,503 B | 105,738 B | 106,152 B | 104,867 B |
| Edge SLM | 175,916 B | 169,459 B | 188,142 B | 179,595 B |
| Selected three animations | 528,313 B | 512,295 B | 543,755 B | 525,054 B |

All 12 variants together occupy 2,109,417 bytes. `<picture>` selects one variant per placement; the table's final row describes the selected GIF payload, excluding static illustrations and browser-specific request/caching overhead.

## Browser and visual review

A local Chromium preview used Python-Markdown 3.8.2 and `github-markdown-css` 5.8.1. The preview's CSS and HTML are development-only files outside the checkout; no custom style is embedded in the README.

Sixteen combinations were checked: viewport widths **1280, 768, 390, and 320 px**, each in light/dark appearance and normal/reduced motion. In every combination:

- All 16 displayed images loaded successfully.
- The intended theme, mobile composition, and GIF/PNG motion variant were selected.
- Section navigation resolved to the rendered headings.
- Document width matched viewport width, with no horizontal overflow.

Desktop and mobile screenshots in both themes, first frames, and quarter-loop frames were inspected. A desktop Edge SLM headline overlap found during review was corrected, regenerated, and rechecked. Mobile hero, pipeline, and Edge SLM compositions are rearranged rather than cropped from desktop artwork.

Generated-art text colors were checked against their backgrounds: dark-mode ratios range from 7.93:1 to 17.72:1; light-mode ratios range from 4.84:1 to 15.87:1. These calculations cover solid text colors in the procedural art, not a full WCAG audit of GitHub or decorative line work.

## Link access and remaining limits

Read-only Git checks succeeded for the profile repository, all six featured projects, and all four further-exploration repositories. LinkedIn, Google Drive resume, X/Twitter, and Facebook HEAD requests were denied by the environment's network proxy with 403 tunnel errors. Their original destinations were preserved; their availability is unverified. Email delivery was not tested.

GitHub API requests and Chromium `file://` navigation were also denied here. Source inspection used the existing authenticated Git route and raw HTTPS; browser previews used an internal loopback HTTP server. The denied routes are not needed to view the final repository assets.

The local preview does not exercise GitHub's hosted Markdown sanitizer, image proxy, profile container, or every browser's GIF/autoplay preferences. Native Markdown and complete first frames preserve the content when animation is unavailable. No changes were pushed, and the hosted profile has not been visually verified. The working tree is ready for review.
