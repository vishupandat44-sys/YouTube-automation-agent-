import random
from typing import List, Optional
from src.models import Character, Scene, ShortsPackage

PRESET_TOPICS = {
    "sharing": {
        "title": "Chintu Aur Magical Apple - Sharing Is Caring!",
        "moral": "Sharing brings happiness to everyone.",
        "characters": [
            Character(
                name="Chintu The Rabbit",
                role="Protagonist",
                description="A cute, fluffy white rabbit with big blue eyes and blue dungarees.",
                visual_prompt="3D cute Pixar style fluffy white rabbit wearing blue dungarees, expressive face, vibrant lighting, 9:16 vertical aspect ratio"
            ),
            Character(
                name="Moti The Puppy",
                role="Friend",
                description="A friendly golden retriever puppy with a red collar.",
                visual_prompt="3D cute Disney style golden retriever puppy wearing a red collar, happy expression, 9:16 vertical aspect ratio"
            )
        ],
        "scenes_data": [
            {
                "visual": "Chintu rabbit finds a shiny glowing red apple in a lush green enchanted meadow.",
                "ai_prompt": "3D cute Pixar style fluffy white rabbit discovering a glowing giant red apple in a colorful sunny meadow, cinematic, 9:16 portrait ratio, highly detailed",
                "vo_hindi": "एक दिन चिंटू ख़रगोश को मिला एक जादुई मीठा सेब! वाह, कितना रसीला सेब है!",
                "vo_eng": "One day Chintu rabbit found a magical sweet apple! Wow, what a juicy apple!",
                "sfx": "Upbeat whimsical music, cheerful gasp sound effect",
                "subtitles": "एक दिन चिंटू को मिला जादुई सेब!"
            },
            {
                "visual": "Moti puppy comes walking by looking sad and hungry, tummy rumbling.",
                "ai_prompt": "3D Pixar animation cute sad golden puppy walking towards white rabbit, hungry expression, soft warm outdoor lighting, 9:16 vertical",
                "vo_hindi": "तभी वहाँ भूखा मोती कुत्ता आया। मोती बोला: 'चिंटू, मुझे बहुत भूख लगी है!'",
                "vo_eng": "Just then, hungry Moti puppy arrived. Moti said: 'Chintu, I am very hungry!'",
                "sfx": "Stomach rumbling SFX, gentle sad clarinet melody",
                "subtitles": "मोती बोला: 'मुझे बहुत भूख लगी है!'"
            },
            {
                "visual": "Chintu smiles warmly and splits the big glowing apple in half, giving half to Moti.",
                "ai_prompt": "3D Pixar style white rabbit smiling and sharing half a shiny red apple with a golden puppy, hearts floating, bright cheerful atmosphere, 9:16 vertical",
                "vo_hindi": "चिंटू ने बिना सोचे सेब के दो टुकड़े किए और आधा सेब मोती को दे दिया!",
                "vo_eng": "Without hesitating, Chintu split the apple into two and gave half to Moti!",
                "sfx": "Sparkle magic chime, upbeat happy whistle",
                "subtitles": "चिंटू ने आधा सेब मोती को दे दिया!"
            },
            {
                "visual": "Both Chintu and Moti happily eat the apple and dance together with sparkling rainbow sparkles appearing around them.",
                "ai_prompt": "3D animated cute white rabbit and golden puppy dancing happily together eating delicious apple, magical sparkles, vibrant colors, 9:16 vertical",
                "vo_hindi": "दोनों ने मज़े से सेब खाया! बाँटने से ख़ुशी दुगनी हो जाती है!",
                "vo_eng": "Both enjoyed eating the apple! Sharing doubles the happiness!",
                "sfx": "Joyful celebration fanfare, kids cheering SFX",
                "subtitles": "बाँटने से ख़ुशी दुगनी हो जाती है!"
            }
        ]
    },
    "honesty": {
        "title": "Golu Elephant & The Golden Magic Bell",
        "moral": "Honesty is always rewarded.",
        "characters": [
            Character(
                name="Golu Elephant",
                role="Protagonist",
                description="A adorable baby elephant with big ears and a yellow cap.",
                visual_prompt="3D Pixar style cute baby elephant wearing a yellow baseball cap, cheerful, 9:16 vertical"
            ),
            Character(
                name="Wise Owl",
                role="Mentor",
                description="A wise old owl with spectacles resting on a wooden branch.",
                visual_prompt="3D cute animated wise brown owl wearing round glasses perched on a branch, 9:16 vertical"
            )
        ],
        "scenes_data": [
            {
                "visual": "Golu baby elephant finds a shiny golden bell lying near the riverbank.",
                "ai_prompt": "3D Pixar cute baby elephant finding a golden glowing bell on a sunny riverbank, jungle backdrop, 9:16 portrait",
                "vo_hindi": "गोलू हाथी को नदी किनारे एक चमकती हुई सोने की घंटी मिली!",
                "vo_eng": "Golu elephant found a shiny golden bell near the riverbank!",
                "sfx": "Bell chime ring SFX, playful jungle background score",
                "subtitles": "गोलू को मिली सोने की घंटी!"
            },
            {
                "visual": "Wise owl swoops down and asks if the bell belongs to Golu.",
                "ai_prompt": "3D cute owl with glasses landing near baby elephant, colorful forest setting, 9:16 portrait",
                "vo_hindi": "उल्लू दादा ने पूछा: 'गोलू, क्या यह घंटी तुम्हारी है?'",
                "vo_eng": "Grandpa Owl asked: 'Golu, does this bell belong to you?'",
                "sfx": "Whoosh wings sound, owl hoot SFX",
                "subtitles": "क्या यह घंटी तुम्हारी है?"
            },
            {
                "visual": "Golu shakes his head honestly and says it's not his.",
                "ai_prompt": "3D cute baby elephant shaking head politely, honest innocent expression, 9:16 vertical",
                "vo_hindi": "गोलू ने ईमानदारी से कहा: 'नहीं दादा, यह मेरी नहीं है!'",
                "vo_eng": "Golu honestly replied: 'No grandpa, this isn't mine!'",
                "sfx": "Soft sweet xylophone melody",
                "subtitles": "'नहीं दादा, यह मेरी नहीं है!'"
            },
            {
                "visual": "Wise owl praises Golu and gifts him a magical crown of flowers.",
                "ai_prompt": "3D cute baby elephant wearing a crown of glowing colorful flowers, owl smiling, magical sparkles, 9:16 portrait",
                "vo_hindi": "गोलू की सच बोलने की आदत देखकर उल्लू दादा ने उसे सुंदर फूलों का ताज दिया! हमेशा सच बोलो!",
                "vo_eng": "Seeing Golu's honesty, Grandpa Owl gifted him a beautiful flower crown! Always tell the truth!",
                "sfx": "Magic harp cascade, joyful trumpeting elephant SFX",
                "subtitles": "सच्चाई की हमेशा जीत होती है!"
            }
        ]
    },
    "teamwork": {
        "title": "The Little Ants & The Huge Strawberry",
        "moral": "Teamwork makes the dream work!",
        "characters": [
            Character(
                name="Pip & Pop Ants",
                role="Protagonists",
                description="Two tiny energetic 3D cartoon red ants with large friendly eyes.",
                visual_prompt="3D cute Pixar style tiny red cartoon ants wearing tiny colorful helmets, 9:16 vertical"
            )
        ],
        "scenes_data": [
            {
                "visual": "Pip the tiny ant discovers a giant delicious red strawberry in the garden.",
                "ai_prompt": "3D Pixar style tiny red cartoon ant standing next to a massive glossy red strawberry, garden background, macro view, 9:16 vertical",
                "vo_hindi": "छोटे पिप चींटी को बाग़ में मिला एक विशाल मीठा स्ट्रॉबेरी!",
                "vo_eng": "Tiny Pip ant found a huge sweet strawberry in the garden!",
                "sfx": "Excited bouncy music, tiny gasp SFX",
                "subtitles": "पिप को मिला विशाल स्ट्रॉबेरी!"
            },
            {
                "visual": "Pip tries to push it alone but cannot move it at all.",
                "ai_prompt": "3D animated tiny ant struggling to push huge strawberry, funny exaggerated expression, 9:16 vertical",
                "vo_hindi": "पिप ने अकेले उठाने की कोशिश की, लेकिन स्ट्रॉबेरी हिल भी नहीं सकी!",
                "vo_eng": "Pip tried to lift it alone, but the strawberry wouldn't even budge!",
                "sfx": "Funny grunt sound effect, comical slide whistle",
                "subtitles": "पिप अकेले उसे उठा नहीं पाया!"
            },
            {
                "visual": "Pip calls his ant friends. A marching line of friendly ants arrives.",
                "ai_prompt": "3D cute cartoon ants marching together in line smiling and waving, bright sunny day, 9:16 portrait",
                "vo_hindi": "पिप ने अपने सभी दोस्तों को बुलाया। सारे दोस्त ख़ुशी-ख़ुशी मदद के लिए दौड़ पड़े!",
                "vo_eng": "Pip called all his friends. All his buddies ran cheerfully to help!",
                "sfx": "Upbeat marching drumbeat, cheery cheering SFX",
                "subtitles": "पिप ने सभी दोस्तों को बुलाया!"
            },
            {
                "visual": "Together, all the tiny ants lift the giant strawberry up high and carry it home, celebrating.",
                "ai_prompt": "3D cute cartoon ant squad lifting big red strawberry together triumphantly, confetti and sparkles, 9:16 vertical",
                "vo_hindi": "सबने मिलकर जोर लगाया और स्ट्रॉबेरी उठा ली! एकता में ही सबसे बड़ी शक्ति है!",
                "vo_eng": "Together they pushed hard and lifted the strawberry! Unity is the greatest strength!",
                "sfx": "Grand triumphant fanfare, joyful party horn",
                "subtitles": "एकता में ही सबसे बड़ी शक्ति है!"
            }
        ]
    }
}


class ShortsGenerator:
    """Automated generator for 30-60 second Hindi Kids Cartoon YouTube Shorts."""

    def __init__(self):
        pass

    def generate_short(
        self,
        topic: Optional[str] = None,
        custom_title: Optional[str] = None,
        duration: float = 45.0
    ) -> ShortsPackage:
        """Generates a complete YouTube Shorts package based on topic or random preset."""
        selected_key = None
        if topic:
            topic_clean = topic.lower().strip()
            for key in PRESET_TOPICS:
                if key in topic_clean or topic_clean in key:
                    selected_key = key
                    break

        if not selected_key:
            selected_key = random.choice(list(PRESET_TOPICS.keys()))

        preset = PRESET_TOPICS[selected_key]
        title = custom_title if custom_title else preset["title"]
        moral = preset["moral"]
        characters = preset["characters"]
        raw_scenes = preset["scenes_data"]

        num_scenes = len(raw_scenes)
        scene_duration = round(duration / num_scenes, 1)

        scenes: List[Scene] = []
        for idx, sdata in enumerate(raw_scenes, start=1):
            scenes.append(
                Scene(
                    scene_number=idx,
                    duration_seconds=scene_duration,
                    visual_description=sdata["visual"],
                    ai_video_prompt=sdata["ai_prompt"],
                    voiceover_hindi=sdata["vo_hindi"],
                    voiceover_english=sdata["vo_eng"],
                    music_sfx=sdata["sfx"],
                    subtitles=sdata["subtitles"]
                )
            )

        main_char = characters[0].name if characters else "Cartoon Character"
        thumbnail_prompt = (
            f"3D Pixar Disney style vertical 9:16 banner featuring {main_char} with vibrant colorful background, "
            f"bold expressive face, bright lighting, high quality 8k render, YouTube Shorts thumbnail"
        )

        seo_title = f"{title} 🎨 | Moral Stories For Kids | Hindi Kahaniya #Shorts"
        seo_description = (
            f"Watch this fun and educational cartoon short for kids: '{title}'! "
            f"Learn the valuable lesson: {moral}. "
            f"Subscribe to our channel for more cute 3D animated Hindi stories, fairy tales, and moral lessons every day! "
            f"#KidsCartoons #HindiKahaniya #MoralStories #Shorts #Animation #3DCartoon"
        )
        seo_tags = [
            "Kids Cartoons",
            "Hindi Kahaniya",
            "Moral Stories",
            "YouTube Shorts",
            "3D Animation",
            "Educational Shorts",
            "Bedtime Stories",
            "Children Stories",
            "Hindi Animated Stories",
            selected_key.capitalize()
        ]
        cta = "👍 Like, Share, and Subscribe for more fun cartoon stories every day! 🔔 Press the bell icon!"

        return ShortsPackage(
            title=title,
            topic=selected_key,
            moral_or_lesson=moral,
            target_duration=duration,
            aspect_ratio="9:16",
            characters=characters,
            scenes=scenes,
            thumbnail_prompt=thumbnail_prompt,
            seo_title=seo_title,
            seo_description=seo_description,
            seo_tags=seo_tags,
            cta=cta
        )
