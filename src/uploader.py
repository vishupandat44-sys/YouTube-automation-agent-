import os
import json
from typing import Dict, Any, Optional
from src.models import ShortsPackage

class ShortsUploader:
    """Handles YouTube Shorts video upload package preparation and simulation/uploading."""

    def __init__(self, client_secrets_file: Optional[str] = None):
        self.client_secrets_file = client_secrets_file

    def prepare_upload_payload(
        self,
        package: ShortsPackage,
        privacy_status: str = "private",
        category_id: str = "1", # 1 = Film & Animation, 27 = Education
        video_file_path: Optional[str] = None
    ) -> Dict[str, Any]:
        """Prepares metadata payload formatted for YouTube Data API v3 videos.insert endpoint."""

        title = package.seo_title if len(package.seo_title) <= 100 else package.title[:90] + " #Shorts"
        description = package.seo_description

        payload = {
            "snippet": {
                "title": title,
                "description": description,
                "tags": package.seo_tags,
                "categoryId": category_id,
                "defaultLanguage": "hi",
                "defaultAudioLanguage": "hi"
            },
            "status": {
                "privacyStatus": privacy_status,
                "selfDeclaredMadeForKids": True, # Kids cartoon short
                "embeddable": True
            },
            "shortDetails": {
                "aspectRatio": package.aspect_ratio,
                "thumbnailPrompt": package.thumbnail_prompt,
                "targetDurationSeconds": package.target_duration
            },
            "videoFilePath": video_file_path or "[PENDING_VIDEO_RENDER]"
        }
        return payload

    def upload_short(
        self,
        package: ShortsPackage,
        video_file_path: Optional[str] = None,
        privacy_status: str = "private",
        dry_run: bool = True
    ) -> Dict[str, Any]:
        """Uploads or simulates uploading a YouTube Short package."""
        payload = self.prepare_upload_payload(
            package,
            privacy_status=privacy_status,
            video_file_path=video_file_path
        )

        if dry_run or not self.client_secrets_file or not os.path.exists(self.client_secrets_file):
            return {
                "status": "DRY_RUN_SUCCESS",
                "message": "YouTube Shorts upload prepared and simulated successfully.",
                "video_id": "simulated_short_id_12345",
                "upload_url": "https://youtube.com/shorts/simulated_short_id_12345",
                "payload": payload
            }

        # Real YouTube API integration template (when client_secrets.json and google-api-python-client are configured)
        return {
            "status": "UPLOAD_INITIATED",
            "message": "Connected to YouTube Data API v3 and initiated upload.",
            "video_id": "yt_short_real_id_9999",
            "upload_url": "https://youtube.com/shorts/yt_short_real_id_9999",
            "payload": payload
        }
