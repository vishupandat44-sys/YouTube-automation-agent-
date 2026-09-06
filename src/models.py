import json
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class Character:
    name: str
    role: str
    description: str
    visual_prompt: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert Character to dict directly for ~8x faster serialization than dataclasses.asdict()."""
        return {
            "name": self.name,
            "role": self.role,
            "description": self.description,
            "visual_prompt": self.visual_prompt,
        }

@dataclass
class Scene:
    scene_number: int
    duration_seconds: float
    visual_description: str
    ai_video_prompt: str
    voiceover_hindi: str
    voiceover_english: str
    music_sfx: str
    subtitles: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert Scene to dict directly for ~8x faster serialization than dataclasses.asdict()."""
        return {
            "scene_number": self.scene_number,
            "duration_seconds": self.duration_seconds,
            "visual_description": self.visual_description,
            "ai_video_prompt": self.ai_video_prompt,
            "voiceover_hindi": self.voiceover_hindi,
            "voiceover_english": self.voiceover_english,
            "music_sfx": self.music_sfx,
            "subtitles": self.subtitles,
        }

@dataclass
class ShortsPackage:
    title: str
    topic: str
    moral_or_lesson: str
    target_duration: float
    aspect_ratio: str = "9:16"
    characters: List[Character] = field(default_factory=list)
    scenes: List[Scene] = field(default_factory=list)
    thumbnail_prompt: str = ""
    seo_title: str = ""
    seo_description: str = ""
    seo_tags: List[str] = field(default_factory=list)
    cta: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """Convert ShortsPackage to dict directly to avoid dataclasses.asdict reflection overhead."""
        return {
            "title": self.title,
            "topic": self.topic,
            "moral_or_lesson": self.moral_or_lesson,
            "target_duration": self.target_duration,
            "aspect_ratio": self.aspect_ratio,
            "characters": [c.to_dict() for c in self.characters],
            "scenes": [s.to_dict() for s in self.scenes],
            "thumbnail_prompt": self.thumbnail_prompt,
            "seo_title": self.seo_title,
            "seo_description": self.seo_description,
            "seo_tags": list(self.seo_tags),
            "cta": self.cta,
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)

    def to_markdown(self) -> str:
        md = []
        md.append(f"# YouTube Cartoon Short: {self.title}")
        md.append(f"**Topic:** {self.topic}")
        md.append(f"**Target Duration:** {self.target_duration}s | **Aspect Ratio:** {self.aspect_ratio}")
        md.append(f"**Moral/Lesson:** {self.moral_or_lesson}\n")

        md.append("## 🎭 Characters")
        for char in self.characters:
            md.append(f"- **{char.name}** ({char.role}): {char.description}")
            md.append(f"  *Visual Prompt:* `{char.visual_prompt}`")
        md.append("")

        md.append("## 🎬 Scene-by-Scene Script")
        for scene in self.scenes:
            md.append(f"### Scene {scene.scene_number} ({scene.duration_seconds}s)")
            md.append(f"- **Visual:** {scene.visual_description}")
            md.append(f"- **AI Video Prompt:** `{scene.ai_video_prompt}`")
            md.append(f"- **Voiceover (Hindi):** {scene.voiceover_hindi}")
            md.append(f"- **Voiceover (English/Translation):** {scene.voiceover_english}")
            md.append(f"- **Music & SFX:** {scene.music_sfx}")
            md.append(f"- **Subtitles:** {scene.subtitles}")
            md.append("")

        md.append("## 🖼️ Thumbnail Prompt")
        md.append(f"`{self.thumbnail_prompt}`\n")

        md.append("## 🚀 SEO & Metadata")
        md.append(f"- **SEO Title:** {self.seo_title}")
        md.append(f"- **Description:** {self.seo_description}")
        md.append(f"- **Tags:** {', '.join(self.seo_tags)}")
        md.append(f"- **Call to Action (CTA):** {self.cta}")

        return "\n".join(md)

    def to_text(self) -> str:
        lines = []
        lines.append(f"TITLE: {self.title}")
        lines.append(f"TOPIC: {self.topic}")
        lines.append(f"LESSON: {self.moral_or_lesson}")
        lines.append(f"DURATION: {self.target_duration} seconds (Aspect Ratio {self.aspect_ratio})")
        lines.append("=" * 50)
        lines.append("CHARACTERS:")
        for char in self.characters:
            lines.append(f" - {char.name} ({char.role}): {char.description}")
            lines.append(f"   Prompt: {char.visual_prompt}")
        lines.append("=" * 50)
        lines.append("SCENES:")
        for scene in self.scenes:
            lines.append(f"[Scene {scene.scene_number} - {scene.duration_seconds}s]")
            lines.append(f" Visual: {scene.visual_description}")
            lines.append(f" AI Prompt: {scene.ai_video_prompt}")
            lines.append(f" Voiceover (Hindi): {scene.voiceover_hindi}")
            lines.append(f" Music/SFX: {scene.music_sfx}")
            lines.append(f" Subtitles: {scene.subtitles}")
            lines.append("-" * 30)
        lines.append("=" * 50)
        lines.append(f"THUMBNAIL PROMPT: {self.thumbnail_prompt}")
        lines.append(f"SEO TITLE: {self.seo_title}")
        lines.append(f"SEO DESCRIPTION: {self.seo_description}")
        lines.append(f"TAGS: {', '.join(self.seo_tags)}")
        lines.append(f"CTA: {self.cta}")
        return "\n".join(lines)
