# Profile assets

The profile has no build step. Edit the root `README.md` and the SVG files directly.

## Visual system

- `profile-hero.svg` and `profile-hero-light.svg`: desktop hero, 960 × 280.
- `profile-hero-mobile.svg` and `profile-hero-mobile-light.svg`: compact composition, 600 × 280. The README selects these at viewport widths up to 600 px.
- `project-*.svg` and their `*-light.svg` companions: six conceptual project illustrations, 960 × 136. These are diagrams, not screenshots or benchmark results.
- `icons/`: eight unmodified SVGs from [Devicon v2.17.0](https://github.com/devicons/devicon/tree/v2.17.0/icons), with the upstream [MIT license](icons/LICENSE).

The default artwork uses midnight navy `#0B1020`, slate `#151E32`, cyan `#38BDF8`, teal `#2DD4BF`, and violet `#A78BFA`. Light variants use pale slate backgrounds and darker accent colors for contrast. Keep paired assets in sync when editing.

All artwork is local, static SVG with system-font fallbacks. It contains no scripts, external fonts, embedded bitmaps, or network dependencies. Native Markdown carries every project description, technology list, and contact link so the portfolio remains useful without images. The README uses GitHub-supported Markdown, images, links, tables, and `<picture>` elements; it needs no custom CSS or JavaScript.

## Project references

Portfolio copy was checked against public READMEs and representative source on 19 October 2026. These links pin the inspected revisions so later edits can distinguish documented capabilities from new work.

| Project | Evidence and scope |
| :--- | :--- |
| [Edge SLM](https://github.com/SalahElshafey/Edge-SLM-Offline-Domain-Specific-Small-Language-Model-Pipeline/tree/df4de6457fb84e0d960b8228ab20ae25fbf29d5d) | README, ingestion schema/chunking, and `GUI/app.py`. Data preparation and local ingestion are implemented; model enrichment, fine-tuning, and deployment are downstream stages. |
| [Distributed LLM Fine-Tuning](https://github.com/SalahElshafey/VT-Cluster--Parallel-and-Distributed-Programming-of-Machine-Learning-Models/tree/15d2b14a215663bd9115508cb94e67a01d3ad990) | README, DistilGPT2 and OPT training scripts under `Cluster/`, and dependencies. LoRA, distributed training, DeepSpeed pipelines, and SLURM are documented; the original CPU cluster is private. |
| [GPT Visualization](https://github.com/SalahElshafey/GPT-Visualization/tree/e4fb4738b71d85a7111d27573ebfd9a999fc8386) | README and both notebooks. Educational GPT-style implementations and exercises; the profile makes no claim to a production GPT-2 replica or original model architecture. |
| [Aria Object Recognition](https://github.com/SalahElshafey/RGU-Aria-Meta-Glasses-Object-Recognition-in-Daily-Life/tree/9b3050141a5c52e1347ae0fc4b27242dc2f8f148) | README, YOLO training/video inference, and Aria streaming code. Includes dataset preparation and streaming experiments, with documented streaming limitations. |
| [VR Fitness Trainer](https://github.com/SalahElshafey/Virtual-Reality-Fitness-Trainer/tree/cedec28e8a5a3dd5ce047d3d60e1cb237cbec846) | README, `Train.py`, and `Test_LiveStream.py` on the default `MachineLearning` branch. Team-project architecture includes Unity and sensing; this branch contains ML and MQTT work. It is not presented as a turnkey deployed system. |
| [Home Security App](https://github.com/SalahElshafey/HomeSecurityApp/tree/3fc29c261b368aa9d8cb18ebbaf764f9bf8b4c04) | README, Gradle dependencies, manifest, and Java activities. Verified Firebase authentication, Realtime Database locker controls, buzzer alerts, and history. The profile avoids unsupported camera-streaming and production-security claims. |

Other public repository pages and relevant READMEs were reviewed before selecting these six. The original profile supplies the display name, Computer Systems Engineer description, C background, learning interests, email, CV, and social links. No employment, qualifications, awards, benchmark results, or individual credit for team-wide work were added.

## Rendering and link checks

Local Chromium previews use GitHub-style Markdown CSS. Review desktop and narrow layouts in both color schemes after changing content. This approximates GitHub rendering; it does not exercise GitHub's hosted sanitizer, image proxy, or profile container. Keep the native text and links readable independently of the illustrations.

Repository destinations were reachable during the audit. The existing Google Drive CV, LinkedIn, X/Twitter, and Facebook URLs were preserved exactly, but this environment's network policy prevented confirming their availability. The email address was preserved; delivery was not tested.

The coding GIF, trophy panel, and dynamic statistics/streak images were removed. They could not be validated under the network policy and added third-party requests. Direct links to GitHub repositories and activity replace the statistics widgets; no static or invented metrics are displayed.
