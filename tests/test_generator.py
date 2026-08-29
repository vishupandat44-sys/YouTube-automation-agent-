import json
import unittest
import os
import tempfile
from src.models import Character, Scene, ShortsPackage
from src.generator import ShortsGenerator, PRESET_TOPICS
from src.cli import run_cli

class TestModels(unittest.TestCase):
    def test_shorts_package_to_dict(self):
        char = Character("TestChar", "Hero", "A brave lion", "3D Pixar lion")
        scene = Scene(1, 10.0, "Lion roaring", "3D lion roaring", "शेर गरजा", "Lion roared", "Roar SFX", "शेर गरजा")
        package = ShortsPackage(
            title="Test Title",
            topic="test",
            moral_or_lesson="Be brave",
            target_duration=30.0,
            characters=[char],
            scenes=[scene],
            thumbnail_prompt="3D lion thumbnail",
            seo_title="Test SEO Title",
            seo_description="Test SEO Desc",
            seo_tags=["lion", "brave"],
            cta="Subscribe!"
        )

        dict_data = package.to_dict()
        self.assertEqual(dict_data["title"], "Test Title")
        self.assertEqual(len(dict_data["characters"]), 1)
        self.assertEqual(dict_data["characters"][0]["name"], "TestChar")

        json_str = package.to_json()
        data_from_json = json.loads(json_str)
        self.assertEqual(data_from_json["title"], "Test Title")

        markdown_str = package.to_markdown()
        self.assertIn("# YouTube Cartoon Short: Test Title", markdown_str)
        self.assertIn("TestChar", markdown_str)

        text_str = package.to_text()
        self.assertIn("TITLE: Test Title", text_str)


class TestShortsGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = ShortsGenerator()

    def test_generate_preset_topics(self):
        for topic_name in PRESET_TOPICS:
            package = self.generator.generate_short(topic=topic_name, duration=60.0)
            self.assertEqual(package.topic, topic_name)
            self.assertEqual(package.target_duration, 60.0)
            self.assertGreater(len(package.characters), 0)
            self.assertGreater(len(package.scenes), 0)
            self.assertTrue(package.thumbnail_prompt)
            self.assertTrue(package.seo_title)
            self.assertTrue(package.seo_description)
            self.assertGreater(len(package.seo_tags), 0)

    def test_generate_custom_title(self):
        package = self.generator.generate_short(
            topic="sharing",
            custom_title="Custom Sharing Title",
            duration=30.0
        )
        self.assertEqual(package.title, "Custom Sharing Title")
        self.assertEqual(package.target_duration, 30.0)

    def test_scene_duration_calculation(self):
        package = self.generator.generate_short(duration=40.0)
        total_calculated = sum(s.duration_seconds for s in package.scenes)
        self.assertAlmostEqual(total_calculated, 40.0, places=1)


class TestCLI(unittest.TestCase):
    def test_cli_list_topics(self):
        result = run_cli(["--list-topics"])
        self.assertEqual(result, 0)

    def test_cli_generate_file_output(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            out_file = os.path.join(tmpdir, "output_short.md")
            result = run_cli(["-t", "sharing", "-f", "markdown", "-o", out_file])
            self.assertEqual(result, 0)
            self.assertTrue(os.path.exists(out_file))
            with open(out_file, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("# YouTube Cartoon Short:", content)


if __name__ == "__main__":
    unittest.main()
