import json, os

NORMAL_DIR = r"E:/ComfyUI/characters/Stella_Sora/normal"
CKPT = "waiIllustriousSDXL_v170.safetensors"
SEED = 42424249
NEG_BASE = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark, holding mirror, red mirror, mirror"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"
MALE = "disembodied_penis, 2penises, black_penis, dark_penis"
DP = "doublepen, vaginal, anal, double_penetration, both_holes"

OUTFITS = {
    "default": {
        "char": "stell4virigiadef, 1girl, white hair, long hair, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, large breasts",
        "outfit": "white bonnet, white cloak, frilled cloak, black dress, detached collar, black bowtie, red ribbon, cleavage, black gloves, white pantyhose, high heels",
        "tail_neg": "",
    },
    "bunny": {
        "char": "stell4virigiabnuy, 1girl, white hair, long hair, half up braid, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, mole on hip, large breasts",
        "outfit": "fake animal ears, rabbit ears, lace hairband, black hairband, detached collar, red bowtie, lace collar, fur armlet, cleavage, white leotard, strapless leotard, side-tie leotard, cross-laced leotard, highleg leotard, crotch zipper, showgirl skirt, white thighhighs, single fishnet thighhigh, mismatched legwear, frilled thigh strap, heart o-ring, wrist cuffs, lace-trimmed wrist cuffs, ankle strap, red high heels",
        "tail_neg": ", tail, demon tail, animal tail",
    },
}

POSES = {
    "cowgirl":         "cowgirl_position, girl_on_top, straddling, front_view",
    "reverse_cowgirl": "reverse_cowgirl, girl_on_top, facing_away, looking_back_at_viewer, ass_view",
    "missionary":      "missionary_position, on_back, legs_spread, front_view",
    "doggystyle":      "doggystyle, from_behind, on_all_fours, arched_back, looking_back_at_viewer",
    "mating_press":    "mating_press, folded, shoulders_pressed, legs_on_shoulders, front_view",
    "prone_bone":      "prone_bone, lying, on_stomach, from_behind, ass_view",
    "full_nelson":     "full_nelson, nelson_position, lifted, legs_folded, front_view",
    "piledriver":      "piledriver, inverted, legs_up, upside_down, front_view",
    "standing":        "standing_sex, against_wall, held_up, legs_around_waist, front_view",
    "spooning":        "spooning, lying, on_side, from_behind, legs_together",
    "suspended":       "suspended_congress, held_up, legs_around_waist, lifting, front_view",
    "lotus":           "lotus_position, legs_entwined, facing_each_other, front_view",
    "spitroast":       "spitroast, on_all_fours, arched_back, oral, side_view",
}

STAGES = [
    {
        "n": "01_miedo",
        "depth": "(imminent penetration:1.1)",
        "expr": "wide_eyes, trembling, furrowed_brow, nervous, sweat_drop, looking_at_viewer",
        "hands": "hands_pushing_away",
        "fluids": "",
        "clothes_mod": "clothes_lift",
        "motion": "",
        "sound": "",
    },
    {
        "n": "02_resistencia",
        "depth": "(imminent penetration:1.3), penis_on_pussy",
        "expr": "screaming, open_mouth, clenched_teeth, furrowed_brow, teary_eyes, crying",
        "hands": "hands_pushing_away",
        "fluids": "sweat, tears_streaming",
        "clothes_mod": "clothes_lift, panties_aside",
        "motion": "(motion lines:1.2)",
        "sound": "",
    },
    {
        "n": "03_dolor",
        "depth": "tip_in_pussy, first_insertion, stretching",
        "expr": "clenched_eyes, grimace, parted_lips, furrowed_brow, painful_expression",
        "hands": "hands_gripping_sheets",
        "fluids": "sweat, tears_streaming",
        "clothes_mod": "clothes_lift, panties_aside",
        "motion": "(motion lines:1.3), (speed lines:1.2)",
        "sound": "sound_effects",
    },
    {
        "n": "04_sufrimiento",
        "depth": "half_insertion, (penetration:1.3), stretching",
        "expr": "crying_with_eyes_open, sobbing, trembling_lip, messy_tears",
        "hands": "hands_above_head, clenched_hands",
        "fluids": "sweat, saliva_string",
        "clothes_mod": "clothes_pulled_aside, breasts_outside",
        "motion": "(motion lines:1.3), impact_lines",
        "sound": "sound_effects, onomatopoeia",
    },
    {
        "n": "05_quebranto",
        "depth": "(deep penetration:1.3), thrusting",
        "expr": "half-closed_eyes, glazed_eyes, heavy_breathing, parted_lips, flushed_face, tear_tracks",
        "hands": "hands_above_head",
        "fluids": "sweat_drops, drooling",
        "clothes_mod": "clothes_pulled_aside, exposed_breasts",
        "motion": "(motion lines:1.4), (speed lines:1.3)",
        "sound": "sound_effects, onomatopoeia",
    },
    {
        "n": "06_ahegao_inicio",
        "depth": "(deep penetration:1.4), full_penetration",
        "expr": "ahegao, rolled_back_eyes, tongue_out, drooling, open_mouth, heavy_blush",
        "hands": "hands_above_head",
        "fluids": "sweat_drops, tears_of_pleasure",
        "clothes_mod": "clothes_torn, exposed_breasts",
        "motion": "(motion lines:1.4), impact_lines",
        "sound": "sound_effects, onomatopoeia",
    },
    {
        "n": "07_ahegao_total",
        "depth": "(deep penetration:1.5), (balls_deep:1.4)",
        "expr": "extreme_ahegao, heart_pupils, rolled_back_eyes, cross-eyed, tongue_out, excessive_drooling",
        "hands": "hands_above_head, trembling_fingers",
        "fluids": "excessive_sweat, tears_of_pleasure, excessive_cum, creampie",
        "clothes_mod": "clothes_torn, nude",
        "motion": "(motion lines:1.5), (speed lines:1.4), impact_lines",
        "sound": "sound_effects, onomatopoeia, japanese_text_sound_effects",
    },
    {
        "n": "08_rota",
        "depth": "balls_deep, (gaping:1.3)",
        "expr": "blank_eyes, empty_eyes, thousand_yard_stare, slack-jawed, mouth_slightly_open, emotionless",
        "hands": "limp_arms, hands_resting",
        "fluids": "excessive_cum, cum_drip, drooling",
        "clothes_mod": "completely_nude",
        "motion": "",
        "sound": "",
    },
    {
        "n": "09_destruida",
        "depth": "after_sex, gaping, cum_pool",
        "expr": "exhausted, panting, half-closed_eyes, heavy_blush",
        "hands": "limp_arms, hands_resting",
        "fluids": "heavy_sweat, semen_on_body, semen_on_face, cum_drip",
        "clothes_mod": "completely_nude",
        "motion": "",
        "sound": "",
    },
    {
        "n": "10_inconsciente",
        "depth": "after_sex, gaping",
        "expr": "closed_eyes, sleeping, relaxed_face, serene_expression, dried_tears",
        "hands": "limp_arms, relaxed_posture",
        "fluids": "semen_on_face, semen_on_body, cum_pool",
        "clothes_mod": "completely_nude",
        "motion": "",
        "sound": "",
    },
]

def clean_tag_list(tags_str):
    raw_tags = [t.strip() for t in tags_str.split(",") if t.strip()]
    seen = set()
    cleaned = []
    for t in raw_tags:
        if t not in seen:
            seen.add(t)
            cleaned.append(t)
    return ", ".join(cleaned)

def build_workflow(outfit_name, pose_name, prefix_slug):
    cfg = OUTFITS[outfit_name]
    pose = POSES[pose_name]
    nodes = {}
    nodes["ckpt"] = {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}}
    nodes["clip_skip"] = {"class_type": "CLIPSetLastLayer", "inputs": {"clip": ["ckpt", 1], "stop_at_clip_layer": -2}}
    nodes["lora_char"] = {"class_type": "LoraLoader", "inputs": {"model": ["ckpt", 0], "clip": ["clip_skip", 0], "lora_name": "Stella-Virigia-v1.safetensors", "strength_model": 1.0, "strength_clip": 1.0}}
    nodes["lora_depth"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_char", 0], "clip": ["lora_char", 1], "lora_name": "penetration_depth.safetensors", "strength_model": 1.5, "strength_clip": 1.0}}
    nodes["lora_dp"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_depth", 0], "clip": ["lora_depth", 1], "lora_name": "doublepenetration_r1.safetensors", "strength_model": 1.0, "strength_clip": 1.0}}
    nodes["lora_size"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_dp", 0], "clip": ["lora_dp", 1], "lora_name": "Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors", "strength_model": 0.5, "strength_clip": 1.0}}
    nodes["neg"] = {"class_type": "CLIPTextEncode", "inputs": {"text": NEG_BASE + cfg["tail_neg"], "clip": ["lora_size", 1]}}

    for s in STAGES:
        parts = [
            "score_9, score_8_up, source_anime, rating_explicit",
            cfg["char"],
            cfg["outfit"],
            s["clothes_mod"],
            MALE,
            DP,
            s["depth"],
            pose,
            s["hands"],
            s["expr"],
            s["fluids"]
        ]
        if s["motion"]: parts.append(s["motion"])
        if s["sound"]: parts.append(s["sound"])
        parts.append(LIGHT + ", anime, masterpiece, best_quality")

        raw_combined = ", ".join([p for p in parts if p])
        prompt = clean_tag_list(raw_combined)

        sn = s["n"]
        nodes[f"e_{sn}"] = {"class_type": "EmptyLatentImage", "inputs": {"width": 1216, "height": 832, "batch_size": 1}}
        nodes[f"p_{sn}"] = {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["lora_size", 1]}}
        nodes[f"k_{sn}"] = {"class_type": "KSampler", "inputs": {"seed": SEED, "steps": 28, "cfg": 4.0, "sampler_name": "dpmpp_2m", "scheduler": "karras", "denoise": 1, "model": ["lora_size", 0], "positive": [f"p_{sn}", 0], "negative": ["neg", 0], "latent_image": [f"e_{sn}", 0]}}
        nodes[f"d_{sn}"] = {"class_type": "VAEDecode", "inputs": {"samples": [f"k_{sn}", 0], "vae": ["ckpt", 2]}}
        nodes[f"s_{sn}"] = {"class_type": "SaveImage", "inputs": {"filename_prefix": f"virigia_{prefix_slug}_{sn}", "images": [f"d_{sn}", 0]}}
    return nodes

# Mapping of file names exactly matching the 26 files in normal/
FILE_MAPPING = [
    # Bunny (13 files)
    ("workflow_sequence_bunny.json", "bunny", "cowgirl", "bunny_cowgirl"),
    ("workflow_sequence_bunny_doggystyle.json", "bunny", "doggystyle", "bunny_doggystyle"),
    ("workflow_sequence_bunny_full_nelson.json", "bunny", "full_nelson", "bunny_full_nelson"),
    ("workflow_sequence_bunny_lotus.json", "bunny", "lotus", "bunny_lotus"),
    ("workflow_sequence_bunny_mating_press.json", "bunny", "mating_press", "bunny_mating_press"),
    ("workflow_sequence_bunny_missionary.json", "bunny", "missionary", "bunny_missionary"),
    ("workflow_sequence_bunny_piledriver.json", "bunny", "piledriver", "bunny_piledriver"),
    ("workflow_sequence_bunny_prone_bone.json", "bunny", "prone_bone", "bunny_prone_bone"),
    ("workflow_sequence_bunny_reverse_cowgirl.json", "bunny", "reverse_cowgirl", "bunny_reverse_cowgirl"),
    ("workflow_sequence_bunny_spitroast.json", "bunny", "spitroast", "bunny_spitroast"),
    ("workflow_sequence_bunny_spooning.json", "bunny", "spooning", "bunny_spooning"),
    ("workflow_sequence_bunny_standing.json", "bunny", "standing", "bunny_standing"),
    ("workflow_sequence_bunny_suspended.json", "bunny", "suspended", "bunny_suspended"),
    # Default (13 files)
    ("workflow_sequence_default.json", "default", "cowgirl", "default_cowgirl"),
    ("workflow_sequence_default_full_nelson.json", "default", "full_nelson", "default_full_nelson"),
    ("workflow_sequence_default_lotus.json", "default", "lotus", "default_lotus"),
    ("workflow_sequence_default_mating_press.json", "default", "mating_press", "default_mating_press"),
    ("workflow_sequence_default_missionary.json", "default", "missionary", "default_missionary"),
    ("workflow_sequence_default_piledriver.json", "default", "piledriver", "default_piledriver"),
    ("workflow_sequence_default_prone_bone.json", "default", "prone_bone", "default_prone_bone"),
    ("workflow_sequence_default_reverse_cowgirl.json", "default", "reverse_cowgirl", "default_reverse_cowgirl"),
    ("workflow_sequence_default_spitroast.json", "default", "spitroast", "default_spitroast"),
    ("workflow_sequence_default_spooning.json", "default", "spooning", "default_spooning"),
    ("workflow_sequence_default_standing.json", "default", "standing", "default_standing"),
    ("workflow_sequence_default_suspended.json", "default", "suspended", "default_suspended"),
    ("workflow_sequence_doggystyle.json", "default", "doggystyle", "default_doggystyle"),
]

updated_count = 0
for fname, outfit, pose, slug in FILE_MAPPING:
    wf = build_workflow(outfit, pose, slug)
    target_file = os.path.join(NORMAL_DIR, fname)
    with open(target_file, "w", encoding="utf-8") as f:
        json.dump(wf, f, indent=2, ensure_ascii=False)
    updated_count += 1
    print(f"Updated: {fname} (Outfit: {outfit}, Pose: {pose})")

print(f"\nAll {updated_count} files in {NORMAL_DIR} updated successfully.")
