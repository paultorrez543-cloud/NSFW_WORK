"""
Script to create individual character folders for Elfmori characters:
nol, delva, lucie, elda, misery, phyllis, evelyn.
Populates each folder with prompt .txt files.
"""

import os
import random

STYLE_TRIGGER = "elfmori"

CHARACTERS_DATA = {
    "nol": {
        "name": "nol",
        "features": "nol, 1girl, elf, long pointy ears, blonde hair, blue eyes",
        "outfits": ["traditional elf dress", "white frilly gown", "casual forest tunic"]
    },
    "delva": {
        "name": "delva",
        "features": "delva, 1girl, elf, long pointy ears, silver hair, purple eyes",
        "outfits": ["dark elf armor", "purple silk robe", "noble elf dress"]
    },
    "lucie": {
        "name": "lucie",
        "features": "lucie, 1girl, elf, long pointy ears, green hair, green eyes",
        "outfits": ["druid leaf gown", "floral corset dress", "forest ranger tunic"]
    },
    "elda": {
        "name": "elda",
        "features": "elda, 1girl, elf, long pointy ears, golden hair, amber eyes",
        "outfits": ["royal golden dress", "white priestess gown", "elegant silk robe"]
    },
    "misery": {
        "name": "misery",
        "features": "misery, 1girl, elf, long pointy ears, dark hair, red eyes",
        "outfits": ["gothic elf gown", "black lace outfit", "shadow tunic"]
    },
    "phyllis": {
        "name": "phyllis",
        "features": "phyllis, 1girl, elf, long pointy ears, pink hair, blue eyes",
        "outfits": ["cute pink dress", "spring flower tunic", "casual frilled dress"]
    },
    "evelyn": {
        "name": "evelyn",
        "features": "evelyn, 1girl, elf, long pointy ears, light brown hair, hazel eyes",
        "outfits": ["archaeologist tunic", "adventure gear", "simple linen dress"]
    }
}

POSES = [
    "close-up portrait, gentle smile, looking at viewer",
    "medium shot, sitting gracefully, serene expression",
    "full body, standing pose, looking at viewer",
    "upper body, 3/4 view, turning head with a subtle blush",
    "profile view, calm expression, detailed face"
]

BACKGROUNDS = [
    "mystical forest background, glowing particles, sunlight filtering",
    "ancient tree hollow, soft ambient lighting",
    "flower meadow background, vibrant colors, bokeh",
    "lake side, water reflections, moonlight",
    "simple neutral background, studio lighting"
]

QUALITY = "masterpiece, best quality, ultra-detailed, anime style, 8k wallpaper"

def build_character_folders():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print("Building Elfmori character folders...")

    for char_key, info in CHARACTERS_DATA.items():
        char_dir = os.path.join(base_dir, char_key)
        os.makedirs(char_dir, exist_ok=True)
        
        for i in range(1, 6):
            pose = random.choice(POSES)
            outfit = random.choice(info["outfits"])
            bg = random.choice(BACKGROUNDS)
            
            prompt_content = f"{STYLE_TRIGGER}, {info['features']}, {pose}, {outfit}, {bg}, {QUALITY}"
            
            file_name = f"{char_key}_{i:02d}.txt"
            file_path = os.path.join(char_dir, file_name)
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(prompt_content + "\n")
                
        print(f"  [+] Created folder '{char_key}' with 5 prompt files")

    print("\nSuccessfully created all character folders and prompt files!")

if __name__ == "__main__":
    build_character_folders()
