# YouTube Cartoon Shorts Automation Generator & Uploader

An automated tool to generate complete 30–60 second vertical kids YouTube Cartoon Shorts packages and prepare or upload them directly to YouTube Shorts.

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
- **YouTube Shorts Upload Workflow**: Prepares YouTube Data API v3 upload payloads and simulates/manages video uploads.

---

## 🚀 Features

- **Preset Topics**: Built-in moral stories (`sharing`, `honesty`, `teamwork`).
- **Multiple Output Formats**: Export script packages in `markdown`, `json`, or `text`.
- **YouTube Shorts Upload Preparation**: Generates ready-to-use YouTube Data API payloads with privacy settings, kids category flags, and vertical short tags.
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

Generate story and simulate/prepare uploading to YouTube Shorts:
```bash
python3 main.py --topic honesty --upload --privacy private --video-file my_rendered_video.mp4
```

Generate JSON format output:
```bash
python3 main.py --topic honesty --format json
```

### 2. Python API Usage

```python
from src.generator import ShortsGenerator
from src.uploader import ShortsUploader

generator = ShortsGenerator()
uploader = ShortsUploader()

# Generate a 45-second short on 'teamwork'
package = generator.generate_short(topic="teamwork", duration=45.0)

# Export to Markdown or JSON
print(package.to_markdown())

# Prepare YouTube Shorts upload payload
upload_result = uploader.upload_short(
    package,
    video_file_path="teamwork_video.mp4",
    privacy_status="private",
    dry_run=True
)

print("Simulated Upload Video ID:", upload_result["video_id"])
```

---

## 🧪 Running Tests

To run the automated test suite:
```bash
python3 /home/jules/self_created_tools/test_runner.py
# Or: python3 -m unittest discover -s tests
```

---

## 📜 License
MIT License
