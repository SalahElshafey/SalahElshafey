# Profile assets

The README displays local GIF, PNG, and SVG files; visitors need no build tools. To regenerate the procedural artwork, see [the design and maintenance guide](../docs/DESIGN.md).

## Visual system

- `contact/`: five original contact buttons in dark/light themes, plus desktop/mobile website invitation cards. Regenerate with `python3 scripts/generate_contact_assets.py`.
- `hero/`: original animated desktop and mobile heroes in dark and light themes, each with a static PNG companion.
- `motion/`: the Data → Models → Systems signature, with horizontal and stacked mobile compositions.
- `projects/`: animated Edge SLM diagrams in desktop/mobile and dark/light variants, with static PNG companions.
- `project-*.svg`: the six existing vector project illustrations. The distributed-training and GPT illustrations remain full-width; the three systems illustrations use a more compact presentation. Their dark palette follows the new hero.
- `profile-hero*.svg`: the previous static hero compositions, retained as editable vector artwork and for existing references.
- `icons/`: eight unmodified [Devicon v2.17.0](https://github.com/devicons/devicon/tree/v2.17.0/icons) icons and their [MIT license](icons/LICENSE).

All diagrams are conceptual illustrations, not software screenshots, measured model traces, or benchmark results. They use no scripts, remote fonts, or runtime image services. All core identity, project scope, technologies, and contact information remain native Markdown.

The three animated placements select a single theme and viewport variant through `<picture>`. Reduced-motion sources select still PNGs before animated sources. The first GIF frame is also a complete composition. See [validation results](../docs/VALIDATION.md) for the boundaries of local preview testing.

## Project references

Portfolio copy was checked against public READMEs and representative source on 20 October 2026. These links pin the inspected revisions so later edits can distinguish documented capabilities from new work.

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

All six pinned project revisions were rechecked during the redesign. Current READMEs and representative source files were read through Git or raw HTTPS; the revisions above are unchanged. See [the validation report](../docs/VALIDATION.md) for the files inspected and link-check results.

Activity links point directly to GitHub. No third-party statistics cards, contribution metrics, visitor counters, or image-service credentials are used.
