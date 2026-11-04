[← Back to Capstone Projects](../README.md)

# AI4HC Capstone: Rural Health Kiosk Showcase Poster

![HTML](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

Designed the showcase poster for a 5-person AI-for-Healthcare capstone team, then wrote the Python pipeline that rendered it into a 48x36 in, print-ready PDF matching the on-screen version exactly.

**View:** [light theme](https://matthewqilanthompson.github.io/Data-Science-Portfolio/projects/capstone/ai4hc-info698/index_v1.html) · [dark theme](https://matthewqilanthompson.github.io/Data-Science-Portfolio/projects/capstone/ai4hc-info698/index_dark.html) · [print PDF](./iShowcase_Final.pdf) · [team codebase](https://github.com/UA-AICore/Emergency-Room-Simulator-Repository)

---

## What I built

**The poster: one visual for the whole system.** Took Abhiram Varma Nandimandalam's initial HTML draft ([isjustabhi/AI4HC](https://github.com/isjustabhi/AI4HC)) and developed it into the team's final capstone poster, distilling the entire product (the RAG pipeline, the HeyGen avatar integration, the voice-to-voice pipeline, the learner flow) into a single layout a viewer could read in under a minute. Two theme variants: light for the project slide demo, dark for the printed banner.

**The print pipeline.** Wrote [`scripts/export_poster.py`](./scripts/export_poster.py), a Python pipeline that renders the poster HTML in headless Chrome at 4608x3456 px, screenshots it, and embeds the PNG losslessly into a 48x36 in PDF with print-shop metadata (title, author, subject, keywords). The team printed straight from this PDF for the iShowcase event, and the physical poster matched the on-screen render exactly.

**Avatar source footage.** Recorded the 1-minute source clip used for the team's HeyGen avatar and handed it to the project coordinator, who wired the HeyGen integration.

---

## What I didn't build

The team's product, the Rural Health Kiosk (an AI-powered healthcare access system for underserved rural communities), is a FastAPI service around a fine-tuned MedGemma 4B model with retrieval-augmented generation over a medical knowledge base, voice-to-voice interaction (Whisper speech-to-text, ElevenLabs voice) and a HeyGen streaming avatar ("Dr. Dexter"), with Claude Opus 4.6 also in the stack, packaged with Docker on a Jetstream GPU (per the team's poster), all built by the engineering members of the team. My contribution was the poster, the print pipeline, and the avatar source footage; the codebase isn't mine.

---

## Skills applied

| Category | Techniques |
|---|---|
| Information design | Distilling a multi-service system (RAG pipeline, avatar integration, voice pipeline) into one poster layout |
| Front-end | HTML5/CSS3, theme variants, print-vs-screen layout rules |
| Build automation | Python, headless Chrome scripting, `img2pdf`, print-shop PDF metadata |
| Collaboration | 5-person cross-functional capstone team, healthcare-AI domain |

---

<details>
<summary>Repo structure</summary>

```text
ai4hc-info698/
├── index_v1.html            # Poster source, unified version
├── index_dark.html          # Dark-theme variant of the poster source
├── iShowcase_Final.pdf      # Final printed showcase poster
├── AI4HC_poster_dark.pdf    # Dark-theme variant of the print PDF
├── system_workflow.png      # System architecture diagram embedded in the poster
├── qr-final-codira.png      # QR code from the poster (links to the live demo)
├── UA_logo.svg              # UA branding asset
└── scripts/
    └── export_poster.py     # Headless Chrome + img2pdf pipeline
```

</details>

<details>
<summary>Rebuild the print PDF</summary>

Requires Python 3.9+, Chrome or Chromium, and `img2pdf`.

```bash
pip3 install img2pdf
python3 scripts/export_poster.py
```

Renders the HTML in headless Chrome at 4608x3456 px, screenshots it, then embeds the PNG losslessly into a 48x36 in PDF. Runtime is about 10 seconds. Flags: `--out <path>` for a custom filename, `--keep-png` to keep the intermediate PNG.

</details>

---

<sub>Graduate capstone, INFO 698 (AI for Healthcare), University of Arizona, Spring 2026, 5-person team (UofA AI Core).</sub>
