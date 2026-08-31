"""
Generator script for Ryuuou no Oshigoto Prompts
Generates prompts for each character and saves txt files into their respective subfolders.
"""

import os
import json
import random

CHARACTERS_CONFIG = {
    "hinatsuru_ai": {
        "tags": "hinatsuru ai, 1girl, child, short hair, brown hair, brown eyes, hair ribbon",
        "outfits": ["school uniform, blue sailor dress", "traditional yukata, floral pattern", "casual summer dress"],
    },
    "yashajin_ai": {
        "tags": "yashajin ai, 1girl, child, twintails, black hair, red eyes, hair ribbon",
        "outfits": ["gothic lolita dress, black frills", "school uniform, red ribbon", "casual dark dress"],
    },
    "sora_ginko": {
        "tags": "sora ginko, 1girl, short hair, silver hair, blue eyes, sharp gaze",
        "outfits": ["school uniform, blazer", "winter coat, scarf", "formal dark dress"],
    },
    "charlotte_izo": {
        "tags": "charlotte izo, 1girl, child, long hair, blonde hair, blue eyes, beret",
        "outfits": ["pink frilly dress, ribbon", "french style outfit, beret", "cute casual dress"],
    },
    "keika_kiyotaki": {
        "tags": "keika kiyotaki, 1girl, mature female, long hair, brown hair, brown eyes, ponytail",
        "outfits": ["traditional japanese kimono", "professional suit jacket", "casual sweater"],
    },
    "ayano_sadatou": {
        "tags": "ayano sadatou, 1girl, long hair, black hair, purple eyes, gentle expression",
        "outfits": ["elegant kimono", "school uniform", "stylish blouse and skirt"],
    },
    "mio_mizukoshi": {
        "tags": "mio mizukoshi, 1girl, short hair, orange hair, green eyes, energetic smile",
        "outfits": ["casual t-shirt, shorts", "school uniform", "sportswear tracksuit"],
    }
}

POSES = [
    "close-up portrait, looking at viewer",
    "medium shot, sitting at shogi board, holding shogi piece",
    "full body, standing pose, cheerful expression",
    "upper body, turning head with a warm smile",
    "profile view, focused expression"
]

BACKGROUNDS = [
    "traditional japanese tatami room, shogi board, wooden sliding doors",
    "japanese shogi hall, soft ambient indoor light",
    "cherry blossom garden background, falling sakura petals",
    "sunlit room, cozy atmosphere",
    "simple neutral background, studio lighting"
]

QUALITY_TAGS = "masterpiece, best quality, ultra-detailed, anime style, 8k wallpaper"
NEGATIVE_PROMPT = "worst quality, low quality, bad anatomy, bad hands, missing fingers, extra digit, cropped, watermark, blurry, 3d"

def generate_prompts_for_ryuuou():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    all_prompts = []

    print(f"Generating prompts for Ryuuou no Oshigoto characters...")

    for char_key, config in CHARACTERS_CONFIG.items():
        char_folder = os.path.join(base_dir, char_key)
        prompts_dir = os.path.join(char_folder, "prompts")
        os.makedirs(prompts_dir, exist_ok=True)
        
        char_prompts = []
        for i in range(1, 6):
            pose = random.choice(POSES)
            outfit = random.choice(config["outfits"])
            bg = random.choice(BACKGROUNDS)
            
            prompt_text = f"{config['tags']}, {pose}, {outfit}, {bg}, {QUALITY_TAGS}"
            file_base = f"{char_key}_{i:02d}"
            
            txt_path = os.path.join(prompts_dir, f"{file_base}.txt")
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(prompt_text + "\n")
                
            char_prompts.append({
                "id": file_base,
                "character": char_key,
                "prompt": prompt_text,
                "negative_prompt": NEGATIVE_PROMPT
            })
            
        all_prompts.extend(char_prompts)
        print(f"  - Created 5 prompt files in '{char_key}/prompts/'")

    # Save summary json
    summary_path = os.path.join(base_dir, "ryuuou_prompts_all.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(all_prompts, f, indent=2, ensure_ascii=False)

    print(f"\nAll prompts generated successfully!")
    print(f"Summary saved to: {summary_path}")

if __name__ == "__main__":
    generate_prompts_for_ryuuou()
