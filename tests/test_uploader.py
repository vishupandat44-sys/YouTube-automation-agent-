import unittest
from src.generator import ShortsGenerator
from src.uploader import ShortsUploader
from src.cli import run_cli

class TestShortsUploader(unittest.TestCase):
    def setUp(self):
        self.generator = ShortsGenerator()
        self.uploader = ShortsUploader()

    def test_prepare_upload_payload(self):
        package = self.generator.generate_short(topic="sharing", duration=30.0)
        payload = self.uploader.prepare_upload_payload(
            package,
            privacy_status="unlisted",
            video_file_path="sample_video.mp4"
        )

        self.assertIn("snippet", payload)
        self.assertEqual(payload["snippet"]["defaultLanguage"], "hi")
        self.assertEqual(payload["status"]["privacyStatus"], "unlisted")
        self.assertTrue(payload["status"]["selfDeclaredMadeForKids"])
        self.assertEqual(payload["videoFilePath"], "sample_video.mp4")

    def test_upload_short_dry_run(self):
        package = self.generator.generate_short(topic="honesty")
        result = self.uploader.upload_short(package, dry_run=True)

        self.assertEqual(result["status"], "DRY_RUN_SUCCESS")
        self.assertIn("simulated_short_id", result["video_id"])
        self.assertIn("https://youtube.com/shorts/", result["upload_url"])

    def test_cli_upload_flag(self):
        res = run_cli(["-t", "teamwork", "--upload", "--privacy", "public"])
        self.assertEqual(res, 0)

if __name__ == "__main__":
    unittest.main()
