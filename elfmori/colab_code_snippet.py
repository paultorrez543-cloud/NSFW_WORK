# ==========================================
# Google Colab Snippet: Download LoRA & Generate Prompts
# ==========================================

import os, requests, json, random

# 1. Download LoRA from Civitai in Colab
CIVITAI_TOKEN = ""  # Add your Civitai API Token if needed
LORA_VERSION_ID = "1626271"
LORA_DIR = "/content/ComfyUI/models/loras"
os.makedirs(LORA_DIR, exist_ok=True)

lora_url = f"https://civitai.com/api/download/models/{LORA_VERSION_ID}"
params = {"token": CIVITAI_TOKEN} if CIVITAI_TOKEN else {}

print("Downloading Elfmori LoRA...")
r = requests.get(lora_url, params=params, stream=True)
if r.status_code == 200:
    lora_path = os.path.join(LORA_DIR, "elfmori_illustrious.safetensors")
    with open(lora_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024*1024):
            f.write(chunk)
    print(f"✅ LoRA downloaded successfully to: {lora_path}")
else:
    print(f"❌ Download error HTTP {r.status_code}")

# 2. Generator for Elfmori Character Prompts
STYLE_TRIGGER = "elfmori"
CHARACTERS = ["nol", "delva", "lucie", "elda", "misery", "phyllis", "evelyn"]

POSES = [
    "close-up portrait, looking at viewer",
    "medium shot, sitting gracefully",
    "full body, standing pose",
    "upper body, turning head to viewer"
]
EXPRESSIONS = ["gentle smile", "blushing, embarrassed expression", "seductive smile", "open mouth"]
OUTFITS = ["traditional elf dress, gold trim", "white lace robe", "casual off-shoulder dress"]
BACKGROUNDS = ["mystical forest background, glowing particles", "flower meadow, sunlight filtering", "simple neutral background"]
QUALITY = "masterpiece, best quality, ultra-detailed, anime style"

prompts_list = []
for char in CHARACTERS:
    for i in range(1, 4):
        p = f"{STYLE_TRIGGER}, {char}, 1girl, elf, long pointy ears, {random.choice(POSES)}, {random.choice(EXPRESSIONS)}, {random.choice(OUTFITS)}, {random.choice(BACKGROUNDS)}, {QUALITY}"
        prompts_list.append({"character": char, "prompt": p})

# Save generated prompts to file in Colab
with open("/content/elfmori_generated_prompts.json", "w") as f:
    json.dump(prompts_list, f, indent=2)

print(f"✅ Generated {len(prompts_list)} prompts and saved to /content/elfmori_generated_prompts.json")
