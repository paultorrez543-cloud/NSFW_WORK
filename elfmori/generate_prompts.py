"""
Generator script for Elfmori (Youkoso Sukebe Elf no Mori e) Prompts
Works locally or inside Google Colab.
"""

import os
import json
import random

# Base configuration
STYLE_TRIGGER = "elfmori"
CHARACTERS = ["nol", "delva", "lucie", "elda", "misery", "phyllis", "evelyn"]

POSES = [
    "close-up portrait, looking at viewer",
    "medium shot, sitting gracefully",
    "full body, standing pose",
    "upper body, turning head to viewer",
    "profile view, serene expression"
]

EXPRESSIONS = [
    "gentle smile",
    "blushing, embarrassed expression",
    "seductive smile, subtle blush",
    "open mouth, surprised expression",
    "calm and quiet expression"
]

CLOTHING = [
    "traditional elf dress, gold trim",
    "white lace robe, translucent frills",
    "forest guardian tunic, leather accents",
    "casual off-shoulder dress",
    "fantasy priestess gown"
]

BACKGROUNDS = [
    "mystical forest background, glowing particles, sunlight filtering",
    "ancient tree hollow, soft ambient lighting",
    "flower meadow background, vibrant colors, bokeh",
    "lake side, water reflections, moonlight",
    "simple neutral background, studio lighting"
]

QUALITY_TAGS = "masterpiece, best quality, ultra-detailed, anime style, 8k wallpaper"
NEGATIVE_PROMPT = "worst quality, low quality, bad anatomy, bad hands, missing fingers, extra digit, cropped, watermark, blurry, 3d"

def generate_prompt_for_character(char_name):
    pose = random.choice(POSES)
    expression = random.choice(EXPRESSIONS)
    outfit = random.choice(CLOTHING)
    bg = random.choice(BACKGROUNDS)
    
    prompt = f"{STYLE_TRIGGER}, {char_name}, 1girl, elf, long pointy ears, {pose}, {expression}, {outfit}, {bg}, {QUALITY_TAGS}"
    return prompt

def generate_all_datasets(output_dir="./prompts_output"):
    os.makedirs(output_dir, exist_ok=True)
    generated_data = []

    print(f"Generating prompts for {len(CHARACTERS)} characters...")

    for char in CHARACTERS:
        char_prompts = []
        for i in range(1, 6):  # 5 variations per character
            prompt_text = generate_prompt_for_character(char)
            file_base = f"{char}_{i:02d}"
            
            # Save txt file
            txt_path = os.path.join(output_dir, f"{file_base}.txt")
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(prompt_text + "\n")
                
            char_prompts.append({
                "id": file_base,
                "character": char,
                "prompt": prompt_text,
                "negative_prompt": NEGATIVE_PROMPT
            })
        
        generated_data.extend(char_prompts)
        print(f"  - Generated 5 prompts for '{char}'")

    # Save summary json
    json_path = os.path.join(output_dir, "elfmori_prompts.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(generated_data, f, indent=2, ensure_ascii=False)

    print(f"\nAll prompts generated in '{os.path.abspath(output_dir)}'")
    print(f"Summary saved to '{json_path}'")

if __name__ == "__main__":
    generate_all_datasets()
