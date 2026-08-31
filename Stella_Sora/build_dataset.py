import json, os

B = r"E:/ComfyUI/characters/Stella_Sora"
CKPT = "rinIllusionRNSFW_v30.safetensors"

# ═══════════════════════════════════════════════════════
# CONFIGURACIÓN DEL PERSONAJE — CAMBIÁ SOLO ESTO
# ═══════════════════════════════════════════════════════
CHARACTER = {
    "lora": "Stella-Virigia-v1.safetensors",   # archivo del LoRA del personaje
    "lora_strength": 1.0,
    # trigger + rasgos del personaje (identidad)
    "char": (
        "stell4virigiadef, 1girl, white hair, long hair, blunt bangs, "
        "double-parted bangs, red eyes, demon horns, low wings, large breasts"
    ),
    # OUTFITS — uno por línea. Si el personaje tiene 2 outfits, agregá el 2do
    # (se repartirán entre las imágenes para que el LoRA aprenda ambos)
    "outfits": [
        "black dress, white cloak, white bonnet, high heels",
        # "white dress, red ribbon, brown shoes",   # ← outfit 2 opcional
    ],
    "extra_neg": "",   # negativo extra del personaje (ej: ", tail, animal tail")
}

# Negativo LIMPIO para dataset (sin NSFW — es referencia de identidad)
NEG = (
    "lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, "
    "crossed eyes, missing fingers, extra digits, fewer digits, worst quality, "
    "low quality, blurry, ugly, censored, watermark, signature, text, logo, "
    "artist name, multiple views, multiple girls, 2girls"
)

# Calidad + estilo (SFW, fondo simple para que el LoRA NO aprenda el fondo)
STYLE = "source_anime, simple_background, white_background, masterpiece, best_quality"

# ═══════════════════════════════════════════════════════
# DATASET — ~30 imágenes variadas (ángulos × planos × expresiones × poses)
# (nombre, tags_extra, width, height)
# ═══════════════════════════════════════════════════════
SHOTS = [
    # ── Cuerpo completo: 4 ángulos ──
    ("full_front",   "full_body, front_view, standing, neutral_expression", 1024, 1536),
    ("full_back",    "full_body, back_view, standing, neutral_expression", 1024, 1536),
    ("full_side",    "full_body, side_view, standing, neutral_expression", 1024, 1536),
    ("full_34",      "full_body, three-quarter_view, standing, neutral_expression", 1024, 1536),

    # ── Cuerpo completo: 4 poses ──
    ("full_sit",     "full_body, sitting, legs_together, front_view, neutral_expression", 1024, 1536),
    ("full_walk",    "full_body, walking, side_view, neutral_expression", 1024, 1536),
    ("full_hips",    "full_body, hands_on_hips, front_view, neutral_expression", 1024, 1536),
    ("full_arms",    "full_body, arms_crossed, front_view, neutral_expression", 1024, 1536),

    # ── Medio cuerpo: 6 ángulos ──
    ("upper_front",  "upper_body, front_view, neutral_expression", 1216, 832),
    ("upper_34",     "upper_body, three-quarter_view, neutral_expression", 1216, 832),
    ("upper_side",   "upper_body, side_view, neutral_expression", 1216, 832),
    ("upper_back",   "upper_body, back_view, neutral_expression", 1216, 832),
    ("upper_above",  "upper_body, from_above, looking_up, neutral_expression", 1216, 832),
    ("upper_below",  "upper_body, from_below, looking_down, neutral_expression", 1216, 832),

    # ── Retrato: 8 expresiones ──
    ("face_neutral", "portrait, front_view, neutral_expression", 1024, 1024),
    ("face_smile",   "portrait, front_view, smile", 1024, 1024),
    ("face_angry",   "portrait, front_view, angry, furrowed_brow", 1024, 1024),
    ("face_shy",     "portrait, three-quarter_view, shy, blush", 1024, 1024),
    ("face_surprise","portrait, front_view, surprised, open_mouth, wide_eyes", 1024, 1024),
    ("face_happy",   "portrait, front_view, happy, closed_eyes, smile", 1024, 1024),
    ("face_sad",     "portrait, three-quarter_view, sad, downcast_eyes", 1024, 1024),
    ("face_serious", "portrait, front_view, serious, flat_expression", 1024, 1024),

    # ── Cuerpo completo con expresión (4) ──
    ("full_smile",   "full_body, front_view, standing, smile", 1024, 1536),
    ("full_shy",     "full_body, three-quarter_view, standing, shy, blush", 1024, 1536),
    ("full_angry",   "full_body, front_view, standing, angry", 1024, 1536),
    ("full_lookback","full_body, back_view, looking_back, neutral_expression", 1024, 1536),
]

# ═══════════════════════════════════════════════════════
# CONSTRUCCIÓN DEL WORKFLOW
# ═══════════════════════════════════════════════════════
def build_dataset_workflow():
    outfits = CHARACTER["outfits"]
    nodes = {}
    nodes["ckpt"] = {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}}
    nodes["clip_skip"] = {"class_type": "CLIPSetLastLayer", "inputs": {"clip": ["ckpt", 1], "stop_at_clip_layer": -2}}
    nodes["lora_char"] = {"class_type": "LoraLoader", "inputs": {
        "model": ["ckpt", 0], "clip": ["clip_skip", 0],
        "lora_name": CHARACTER["lora"],
        "strength_model": CHARACTER["lora_strength"], "strength_clip": 1.0,
    }}
    nodes["neg"] = {"class_type": "CLIPTextEncode", "inputs": {
        "text": NEG + CHARACTER["extra_neg"], "clip": ["lora_char", 1],
    }}

    n_outfits = len(outfits)
    for i, (name, shot_tags, w, h) in enumerate(SHOTS):
        outfit = outfits[i % n_outfits]  # repartir outfits entre imágenes
        prompt = (
            f"score_9, score_8_up, {CHARACTER['char']}, {outfit}, "
            f"{shot_tags}, {STYLE}"
        ).replace(", ,", ",").replace(",,", ",")

        nodes[f"e_{name}"] = {"class_type": "EmptyLatentImage", "inputs": {"width": w, "height": h, "batch_size": 1}}
        nodes[f"p_{name}"] = {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["lora_char", 1]}}
        nodes[f"k_{name}"] = {"class_type": "KSampler", "inputs": {
            "seed": 42424249, "steps": 28, "cfg": 4.5,
            "sampler_name": "dpmpp_2m", "scheduler": "karras", "denoise": 1,
            "model": ["lora_char", 0], "positive": [f"p_{name}", 0],
            "negative": ["neg", 0], "latent_image": [f"e_{name}", 0],
        }}
        nodes[f"d_{name}"] = {"class_type": "VAEDecode", "inputs": {"samples": [f"k_{name}", 0], "vae": ["ckpt", 2]}}
        nodes[f"s_{name}"] = {"class_type": "SaveImage", "inputs": {
            "filename_prefix": f"dataset_{name}", "images": [f"d_{name}", 0],
        }}

    return nodes

if __name__ == "__main__":
    wf = build_dataset_workflow()
    out = os.path.join(B, "workflow_dataset_generator.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(wf, f, indent=2, ensure_ascii=False)
    n = sum(1 for v in wf.values() if v.get("class_type") == "SaveImage")
    print(f"✅ workflow_dataset_generator.json → {n} imágenes SFW de referencia")
    print(f"   Personaje: {CHARACTER['lora']}")
    print(f"   Outfits: {len(CHARACTER['outfits'])}")
