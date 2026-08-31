import json, os

TARGET_DIR = r"E:/ComfyUI/characters/Stella_Sora/normal"
OUTPUT_FILE = os.path.join(TARGET_DIR, "workflow_example_danbooru_master.json")

CKPT = "waiIllustriousSDXL_v170.safetensors"
SEED = 42424249

# Negativo perfeccionado para SDXL Illustrious
NEG = (
    "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, "
    "extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, "
    "low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, "
    "bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, "
    "signature, watermark, holding mirror, red mirror, mirror"
)

# Iluminación y Shading de piel Danbooru Pro
LIGHTING_PRO = (
    "dimly_lit, dark_ambiance, (dark lighting:1.4), rim_lighting, sweat_gleam, "
    "glossy_skin, dramatic_shadows, depth_of_field, anime, masterpiece, best_quality"
)

CHAR_BASE = (
    "stell4virigiadef, 1girl, white hair, long hair, blunt bangs, double-parted bangs, "
    "red eyes, demon horns, low wings, large breasts, collarbone, navel, hip_bones"
)

OUTFIT_BASE = (
    "white bonnet, white cloak, frilled cloak, black dress, detached collar, "
    "black bowtie, red ribbon, cleavage, black gloves, white pantyhose, high heels"
)

MALE = "disembodied_penis, 2penises"
DP = "doublepen, vaginal, anal, double_penetration, both_holes"
POSE = "mating_press, folded, shoulders_pressed, legs_on_shoulders, thigh_squish, front_view"

# 10 Etapas con micro-anatomía, física de movimiento y degradación de ropa
STAGES_PRO = [
    {
        "n": "01_miedo",
        "depth": "(imminent penetration:1.1)",
        "expr": "wide_eyes, trembling, furrowed_brow, nervous, sweat_drop, looking_at_viewer",
        "hands": "hands_pushing_away, skin_indentation",
        "phys": "mattress_indentation",
        "clothes": "intact_clothing, clothes_lift",
        "fluids": "sweat_drops",
        "cam": "front_view",
    },
    {
        "n": "02_resistencia",
        "depth": "(imminent penetration:1.3), penis_on_pussy",
        "expr": "screaming, open_mouth, clenched_teeth, furrowed_brow, teary_eyes, crying",
        "hands": "hands_pushing_away, trembling_hands",
        "phys": "mattress_indentation, hair_stuck_to_face",
        "clothes": "clothes_lift, panties_aside, broken_strap",
        "fluids": "sweat, tears_streaming",
        "cam": "dutch_angle, (motion lines:1.2)",
    },
    {
        "n": "03_dolor",
        "depth": "tip_in_pussy, first_insertion, stretching",
        "expr": "clenched_eyes, grimace, parted_lips, furrowed_brow, painful_expression",
        "hands": "hands_gripping_sheets, white_knuckles",
        "phys": "breast_squish, mattress_indentation, hair_stuck_to_face",
        "clothes": "clothes_lift, torn_dress, exposed_breasts",
        "fluids": "sweat, tears_streaming, saliva_string",
        "cam": "dutch_angle, (motion lines:1.3), (speed lines:1.2), sound_effects",
    },
    {
        "n": "04_sufrimiento",
        "depth": "half_insertion, (penetration:1.3), stretching",
        "expr": "crying_with_eyes_open, sobbing, trembling_lip, messy_tears",
        "hands": "hands_above_head, clenched_hands",
        "phys": "breast_squish, thigh_squish, flying_sweat_drops",
        "clothes": "torn_dress, single_bare_shoulder, exposed_breasts",
        "fluids": "sweat, saliva_string, messy_tears",
        "cam": "dutch_angle, (motion lines:1.3), impact_lines, sound_effects, onomatopoeia",
    },
    {
        "n": "05_quebranto",
        "depth": "(deep penetration:1.3), thrusting",
        "expr": "half-closed_eyes, glazed_eyes, heavy_breathing, parted_lips, flushed_face, tear_tracks",
        "hands": "hands_above_head, fingers_twitching",
        "phys": "bouncing_breasts, breast_squish, flying_sweat_drops",
        "clothes": "shredded_clothes, clothes_falling_off, exposed_breasts",
        "fluids": "sweat_drops, drooling, saliva_string",
        "cam": "(motion lines:1.4), (speed lines:1.3), sound_effects, onomatopoeia",
    },
    {
        "n": "06_ahegao_inicio",
        "depth": "(deep penetration:1.4), full_penetration, belly_bulge",
        "expr": "ahegao, rolled_back_eyes, tongue_out, drooling, open_mouth, heavy_blush",
        "hands": "hands_above_head, limp_wrists",
        "phys": "bouncing_breasts, belly_bulge, flying_sweat_drops",
        "clothes": "shredded_clothes, nude_top, exposed_breasts",
        "fluids": "sweat_drops, tears_of_pleasure, excessive_drooling",
        "cam": "dutch_angle, (motion lines:1.4), impact_lines, sound_effects, onomatopoeia",
    },
    {
        "n": "07_ahegao_total",
        "depth": "(deep penetration:1.5), (balls_deep:1.4), (belly_bulge:1.2)",
        "expr": "extreme_ahegao, heart_pupils, rolled_back_eyes, cross-eyed, tongue_out",
        "hands": "hands_above_head, trembling_fingers",
        "phys": "bouncing_breasts, belly_bulge, flying_sweat_drops, spasming",
        "clothes": "ruined_outfit, nude",
        "fluids": "excessive_sweat, tears_of_pleasure, excessive_cum, creampie",
        "cam": "dutch_angle, (motion lines:1.5), (speed lines:1.4), impact_lines, sound_effects, onomatopoeia, japanese_text_sound_effects",
    },
    {
        "n": "08_rota",
        "depth": "balls_deep, (gaping:1.3), belly_bulge",
        "expr": "blank_eyes, empty_eyes, thousand_yard_stare, slack-jawed, mouth_slightly_open, emotionless",
        "hands": "limp_arms, hands_resting",
        "phys": "spasming_legs, mattress_indentation, hair_stuck_to_face",
        "clothes": "completely_nude, discarded_clothes",
        "fluids": "excessive_cum, cum_drip, cum_overflow, drooling",
        "cam": "low_angle, depth_of_field",
    },
    {
        "n": "09_destruida",
        "depth": "after_sex, gaping, cum_pool",
        "expr": "exhausted, panting, half-closed_eyes, heavy_blush",
        "hands": "limp_arms, hands_resting",
        "phys": "trembling_body, disheveled_hair, mattress_indentation",
        "clothes": "completely_nude, discarded_clothes",
        "fluids": "heavy_sweat, semen_on_body, semen_on_face, cum_drip, cum_pool",
        "cam": "low_angle, depth_of_field",
    },
    {
        "n": "10_inconsciente",
        "depth": "after_sex, gaping",
        "expr": "closed_eyes, sleeping, relaxed_face, serene_expression, dried_tears",
        "hands": "limp_arms, relaxed_posture",
        "phys": "disheveled_hair, messy_bed, soaked_sheets",
        "clothes": "completely_nude",
        "fluids": "dried_tears, semen_on_face, semen_on_body, cum_pool",
        "cam": "overhead_view, depth_of_field",
    },
]

def clean_tags(tags_str):
    raw = [t.strip() for t in tags_str.split(",") if t.strip()]
    seen = set()
    cleaned = []
    for t in raw:
        if t not in seen:
            seen.add(t)
            cleaned.append(t)
    return ", ".join(cleaned)

nodes = {}
nodes["ckpt"] = {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}}
nodes["clip_skip"] = {"class_type": "CLIPSetLastLayer", "inputs": {"clip": ["ckpt", 1], "stop_at_clip_layer": -2}}
nodes["lora_char"] = {"class_type": "LoraLoader", "inputs": {"model": ["ckpt", 0], "clip": ["clip_skip", 0], "lora_name": "Stella-Virigia-v1.safetensors", "strength_model": 1.0, "strength_clip": 1.0}}
nodes["lora_depth"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_char", 0], "clip": ["lora_char", 1], "lora_name": "penetration_depth.safetensors", "strength_model": 1.5, "strength_clip": 1.0}}
nodes["lora_dp"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_depth", 0], "clip": ["lora_depth", 1], "lora_name": "doublepenetration_r1.safetensors", "strength_model": 1.0, "strength_clip": 1.0}}
nodes["lora_size"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_dp", 0], "clip": ["lora_dp", 1], "lora_name": "Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors", "strength_model": 0.5, "strength_clip": 1.0}}
nodes["neg"] = {"class_type": "CLIPTextEncode", "inputs": {"text": NEG, "clip": ["lora_size", 1]}}

for s in STAGES_PRO:
    sn = s["n"]
    parts = [
        "score_9, score_8_up, source_anime, rating_explicit",
        CHAR_BASE,
        OUTFIT_BASE,
        s["clothes"],
        MALE,
        DP,
        s["depth"],
        POSE,
        s["hands"],
        s["phys"],
        s["expr"],
        s["fluids"],
        s["cam"],
        LIGHTING_PRO
    ]
    prompt = clean_tags(", ".join([p for p in parts if p]))

    nodes[f"e_{sn}"] = {"class_type": "EmptyLatentImage", "inputs": {"width": 832, "height": 1216, "batch_size": 1}}
    nodes[f"p_{sn}"] = {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["lora_size", 1]}}
    nodes[f"k_{sn}"] = {"class_type": "KSampler", "inputs": {"seed": SEED, "steps": 28, "cfg": 4.0, "sampler_name": "dpmpp_2m", "scheduler": "karras", "denoise": 1, "model": ["lora_size", 0], "positive": [f"p_{sn}", 0], "negative": ["neg", 0], "latent_image": [f"e_{sn}", 0]}}
    nodes[f"d_{sn}"] = {"class_type": "VAEDecode", "inputs": {"samples": [f"k_{sn}", 0], "vae": ["ckpt", 2]}}
    nodes[f"s_{sn}"] = {"class_type": "SaveImage", "inputs": {"filename_prefix": f"virigia_example_master_{sn}", "images": [f"d_{sn}", 0]}}

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(nodes, f, indent=2, ensure_ascii=False)

print(f"[DONE] Workflow de ejemplo creado: {OUTPUT_FILE}")
