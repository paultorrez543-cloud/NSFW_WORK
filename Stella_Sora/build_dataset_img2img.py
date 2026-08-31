import json, os

B = r"E:/ComfyUI/characters/Stella_Sora"
CKPT = "rinIllusionRNSFW_v30.safetensors"

# ═══════════════════════════════════════════════════════
# CONFIGURACIÓN — CAMBIÁ SOLO ESTO
# ═══════════════════════════════════════════════════════
# Imagen de referencia: ponela en la carpeta 'input' de ComfyUI
# y escribí su nombre acá (sin la ruta)
REFERENCE_IMAGE = "character_ref.png"

CHARACTER = {
    "lora": "Stella-Virigia-v1.safetensors",
    "lora_strength": 1.0,
    "char": (
        "stell4virigiadef, 1girl, white hair, long hair, blunt bangs, "
        "double-parted bangs, red eyes, demon horns, low wings, large breasts"
    ),
    "outfits": [
        "black dress, white cloak, white bonnet, high heels",
    ],
    "extra_neg": "",
}

# Fuerza de img2img (denoise). Clave:
#  0.30-0.45 → cambios sutiles (expresión, iluminación)
#  0.50-0.65 → cambios moderados (pose, gesto)  ← recomendado
#  0.70-0.85 → cambios fuertes (ángulo, composición)
DENOISE = 0.60

NEG = (
    "lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, "
    "crossed eyes, missing fingers, extra digits, fewer digits, worst quality, "
    "low quality, blurry, ugly, censored, watermark, signature, text, logo, "
    "artist name, multiple views, multiple girls, 2girls"
)

STYLE = "source_anime, simple_background, white_background, masterpiece, best_quality"

# ═══════════════════════════════════════════════════════
# VARIACIONES — 26 prompts que transforman la referencia
# ═══════════════════════════════════════════════════════
SHOTS = [
    # Ángulos cuerpo completo
    ("full_front",   "full_body, front_view, standing, neutral_expression"),
    ("full_back",    "full_body, back_view, standing, neutral_expression"),
    ("full_side",    "full_body, side_view, standing, neutral_expression"),
    ("full_34",      "full_body, three-quarter_view, standing, neutral_expression"),
    # Poses
    ("full_sit",     "full_body, sitting, legs_together, front_view, neutral_expression"),
    ("full_walk",    "full_body, walking, side_view, neutral_expression"),
    ("full_hips",    "full_body, hands_on_hips, front_view, neutral_expression"),
    ("full_arms",    "full_body, arms_crossed, front_view, neutral_expression"),
    # Medio cuerpo
    ("upper_front",  "upper_body, front_view, neutral_expression"),
    ("upper_34",     "upper_body, three-quarter_view, neutral_expression"),
    ("upper_side",   "upper_body, side_view, neutral_expression"),
    ("upper_back",   "upper_body, back_view, neutral_expression"),
    ("upper_above",  "upper_body, from_above, looking_up, neutral_expression"),
    ("upper_below",  "upper_body, from_below, looking_down, neutral_expression"),
    # Retratos / expresiones
    ("face_neutral", "portrait, front_view, neutral_expression"),
    ("face_smile",   "portrait, front_view, smile"),
    ("face_angry",   "portrait, front_view, angry, furrowed_brow"),
    ("face_shy",     "portrait, three-quarter_view, shy, blush"),
    ("face_surprise","portrait, front_view, surprised, open_mouth, wide_eyes"),
    ("face_happy",   "portrait, front_view, happy, closed_eyes, smile"),
    ("face_sad",     "portrait, three-quarter_view, sad, downcast_eyes"),
    ("face_serious", "portrait, front_view, serious, flat_expression"),
    # Cuerpo entero con expresión
    ("full_smile",   "full_body, front_view, standing, smile"),
    ("full_shy",     "full_body, three-quarter_view, standing, shy, blush"),
    ("full_angry",   "full_body, front_view, standing, angry"),
    ("full_lookback","full_body, back_view, looking_back, neutral_expression"),
]

# ═══════════════════════════════════════════════════════
# CONSTRUCCIÓN DEL WORKFLOW IMG2IMG
# ═══════════════════════════════════════════════════════
def build_img2img_dataset():
    outfits = CHARACTER["outfits"]
    nodes = {}

    # Base compartida
    nodes["ckpt"] = {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}}
    nodes["clip_skip"] = {"class_type": "CLIPSetLastLayer", "inputs": {"clip": ["ckpt", 1], "stop_at_clip_layer": -2}}
    nodes["lora_char"] = {"class_type": "LoraLoader", "inputs": {
        "model": ["ckpt", 0], "clip": ["clip_skip", 0],
        "lora_name": CHARACTER["lora"],
        "strength_model": CHARACTER["lora_strength"], "strength_clip": 1.0,
    }}
    nodes["load_ref"] = {"class_type": "LoadImage", "inputs": {"image": REFERENCE_IMAGE}}
    # Codificar la referencia UNA vez (latente compartido para todas las variaciones)
    nodes["vae_encode"] = {"class_type": "VAEEncode", "inputs": {
        "pixels": ["load_ref", 0], "vae": ["ckpt", 2],
    }}
    nodes["neg"] = {"class_type": "CLIPTextEncode", "inputs": {
        "text": NEG + CHARACTER["extra_neg"], "clip": ["lora_char", 1],
    }}

    n_outfits = len(outfits)
    for i, (name, shot_tags) in enumerate(SHOTS):
        outfit = outfits[i % n_outfits]
        prompt = (
            f"score_9, score_8_up, {CHARACTER['char']}, {outfit}, "
            f"{shot_tags}, {STYLE}"
        ).replace(", ,", ",").replace(",,", ",")

        nodes[f"p_{name}"] = {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["lora_char", 1]}}
        # img2img: latente viene de VAEEncode (no EmptyLatentImage) y denoise < 1
        nodes[f"k_{name}"] = {"class_type": "KSampler", "inputs": {
            "seed": 42424249, "steps": 28, "cfg": 4.5,
            "sampler_name": "dpmpp_2m", "scheduler": "karras", "denoise": DENOISE,
            "model": ["lora_char", 0], "positive": [f"p_{name}", 0],
            "negative": ["neg", 0], "latent_image": ["vae_encode", 0],
        }}
        nodes[f"d_{name}"] = {"class_type": "VAEDecode", "inputs": {"samples": [f"k_{name}", 0], "vae": ["ckpt", 2]}}
        nodes[f"s_{name}"] = {"class_type": "SaveImage", "inputs": {
            "filename_prefix": f"dataset_img2img_{name}", "images": [f"d_{name}", 0],
        }}

    return nodes

if __name__ == "__main__":
    wf = build_img2img_dataset()
    out = os.path.join(B, "workflow_dataset_img2img.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(wf, f, indent=2, ensure_ascii=False)
    n = sum(1 for v in wf.values() if v.get("class_type") == "SaveImage")
    print(f"✅ workflow_dataset_img2img.json → {n} variaciones img2img")
    print(f"   Referencia: {REFERENCE_IMAGE}")
    print(f"   Denoise: {DENOISE} (subir a 0.75+ para cambios de ángulo más fuertes)")
