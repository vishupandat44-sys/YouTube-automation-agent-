# YouTube Cartoon Shorts Automation Generator

An automated tool to generate complete 30–60 second vertical kids YouTube Cartoon Shorts packages.

It automatically generates:
- Unique fun/educational Hindi moral stories & titles
- Cute consistent character visual descriptions & AI prompts
- Scene-by-scene script with timing and visual descriptions
- Dialogue and narrator voice-over in Hindi and English
- AI video generator prompts (for Runway, Midjourney, Pika, Sora, etc.)
- Music & SFX cues
- Subtitles & Call to Action (CTA)
- SEO optimization (Catchy Title, Description, and Tags)
- YouTube Shorts Thumbnail prompts (9:16 vertical aspect ratio)

---

## 🚀 Features

- **Preset Topics**: Built-in moral stories (`sharing`, `honesty`, `teamwork`).
- **Multiple Output Formats**: Export script packages in `markdown`, `json`, or `text`.
- **CLI & Python API**: Flexible usage from command line or directly imported into Python code.

---

## 🛠️ Installation & Usage

### 1. Command Line Interface (CLI)

List available preset topics:
```bash
python3 main.py --list-topics
```

Generate a Cartoon Short script package in Markdown format:
```bash
python3 main.py --topic sharing --duration 45 --format markdown --output generated_short.md
```

Generate JSON format output:
```bash
python3 main.py --topic honesty --format json
```

### 2. Python API Usage

```python
from src.generator import ShortsGenerator

generator = ShortsGenerator()

# Generate a 45-second short on 'teamwork'
package = generator.generate_short(topic="teamwork", duration=45.0)

# Export to Markdown or JSON
print(package.to_markdown())

# Or export to dictionary
data = package.to_dict()
```

---

## 🧪 Running Tests

To run the automated test suite:
```bash
python3 -m unittest discover -s tests
```

---

## 📜 License
MIT License
