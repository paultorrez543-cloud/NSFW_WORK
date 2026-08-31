import json, os

B = r"E:/ComfyUI/characters/Stella_Sora"
CKPT = "rinIllusionRNSFW_v30.safetensors"

# ── Elisia (Make Drama) — datos del vault ──
LORA = "lora_elisia_make_drama.safetensors"
LORA_STRENGTH = 0.85  # peso recomendado en la ficha
SEED = 42424249

CHAR = (
    "elisia_(make_drama), elisia, make drama, 1girl, "
    "demon girl, demon horns, curved horns, black horns, pointy ears, "
    "long hair, wavy hair, bangs, delicate face"
)
OUTFIT = (
    "gothic dress, black dress, red accents, gold trim, corset, "
    "bare shoulders, cleavage, detached sleeves, thighhighs"
)

MALE = "disembodied_penis, 2penises"
DP = "doublepen, vaginal, anal, double_penetration, both_holes"

NEG = (
    "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, "
    "deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, "
    "fewer digits, worst quality, low quality, blurry, ugly, censored, "
    "(bright lighting:1.5), overexposed, glare, flash, bloom, glowing, "
    "x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, "
    "signature, watermark, (holding weapon:1.4), (weapon:1.4), (sword:1.4)"
)

LIGHTING = "dimly_lit, dark_ambiance, (dark lighting:1.4)"

# 6 etapas (progresión non-con)
STAGES = [
    ("01_miedo",       "(imminent penetration:1.2)", "scared, trembling, refusal, nervous_sweat", "", "nervous_sweat", ""),
    ("02_dolor",       "tip_in_pussy, first_insertion", "(pain:1.3), tears_streaming, screaming", "(motion lines:1.3)", "sweat, tears_streaming", "sound_effects"),
    ("03_quebranto",   "(deep penetration:1.3)", "crying, defeated, broken_spirit", "(motion lines:1.4)", "sweat_drops, drooling", "sound_effects, onomatopoeia"),
    ("04_ahegao",      "(deep penetration:1.5), balls_deep", "ahegao, heart_pupils, mind_break, creampie", "(motion lines:1.5), impact_lines", "excessive_sweat, tears_of_pleasure, drooling", "sound_effects, onomatopoeia"),
    ("05_rota",        "balls_deep, gaping", "blank_eyes, thousand_yard_stare, semen_on_body", "", "excessive_sweat, dried_tears, semen_on_body", ""),
    ("06_inconsciente","after_sex, sleeping", "sleeping, tears_streaming, semen_on_face", "", "dried_tears, cum_pool", ""),
]

# 5 poses
POSES = {
    "cowgirl":         "cowgirl_position, girl_on_top, straddling, front_view",
    "doggystyle":      "doggystyle, from_behind, all_fours, front_view",
    "missionary":      "missionary_position, legs_up, spread_legs, front_view",
    "mating_press":    "mating_press, legs_above_head, folded, front_view",
    "reverse_cowgirl": "reverse_cowgirl, girl_on_top, facing_away, front_view",
}

nodes = {}
nodes["ckpt"] = {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}}
nodes["latent_shared"] = {"class_type": "EmptyLatentImage", "inputs": {"width": 1024, "height": 1536, "batch_size": 1}}
nodes["clip_skip"] = {"class_type": "CLIPSetLastLayer", "inputs": {"clip": ["ckpt", 1], "stop_at_clip_layer": -2}}
nodes["lora_char"] = {"class_type": "LoraLoader", "inputs": {"model": ["ckpt", 0], "clip": ["clip_skip", 0], "lora_name": LORA, "strength_model": LORA_STRENGTH, "strength_clip": LORA_STRENGTH}}
nodes["lora_depth"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_char", 0], "clip": ["lora_char", 1], "lora_name": "penetration_depth.safetensors", "strength_model": 1.5, "strength_clip": 1.0}}
nodes["lora_dp"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_depth", 0], "clip": ["lora_depth", 1], "lora_name": "doublepenetration_r1.safetensors", "strength_model": 1.0, "strength_clip": 1.0}}
nodes["lora_size"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_dp", 0], "clip": ["lora_dp", 1], "lora_name": "Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors", "strength_model": 0.5, "strength_clip": 1.0}}
nodes["neg"] = {"class_type": "CLIPTextEncode", "inputs": {"text": NEG, "clip": ["lora_size", 1]}}

for pose_name, pose_tags in POSES.items():
    for n, depth, expr, motion, fluids, sound in STAGES:
        parts = ["score_9, score_8_up, source_anime, rating_explicit", CHAR, OUTFIT, MALE, DP, depth, pose_tags, expr, fluids]
        if motion: parts.append(motion)
        if sound: parts.append(sound)
        parts.append(LIGHTING + ", anime, masterpiece, best_quality")
        prompt = ", ".join([p for p in parts if p]).replace(", ,", ",").replace(",,", ",")
        key = f"{pose_name}_{n}"
        nodes[f"p_{key}"] = {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["lora_size", 1]}}
        nodes[f"k_{key}"] = {"class_type": "KSampler", "inputs": {"seed": SEED, "steps": 28, "cfg": 5.0, "sampler_name": "dpmpp_2m", "scheduler": "karras", "denoise": 1, "model": ["lora_size", 0], "positive": [f"p_{key}", 0], "negative": ["neg", 0], "latent_image": ["latent_shared", 0]}}
        nodes[f"d_{key}"] = {"class_type": "VAEDecode", "inputs": {"samples": [f"k_{key}", 0], "vae": ["ckpt", 2]}}
        nodes[f"s_{key}"] = {"class_type": "SaveImage", "inputs": {"filename_prefix": f"elisia_{pose_name}_{n}", "images": [f"d_{key}", 0]}}

with open(os.path.join(B, "workflow_elisia_30img.json"), "w", encoding="utf-8") as f:
    json.dump(nodes, f, indent=2, ensure_ascii=False)

n = sum(1 for v in nodes.values() if v.get("class_type") == "SaveImage")
print(f"✅ workflow_elisia_30img.json → {n} imágenes (5 poses x 6 etapas)")
