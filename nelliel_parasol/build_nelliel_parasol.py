import json
import os

TARGET_DIR = r"E:/ComfyUI/characters/nelliel_parasol"
os.makedirs(TARGET_DIR, exist_ok=True)

CKPT = "waiIllustriousSDXL_v170.safetensors"
LORA_NAME = "nelliel_parasol.safetensors"
LORA_STRENGTH = 0.9
SEED = 42424292
STEPS = 28
CFG = 6.0
SAMPLER = "euler_ancestral"
SCHEDULER = "karras"

NEG_BASE = (
    "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, "
    "extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, "
    "low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, "
    "bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, "
    "signature, watermark, holding mirror, red mirror, mirror"
)

LIGHTING_PRO = (
    "dimly_lit, dark_ambiance, (dark lighting:1.4), rim_lighting, sweat_gleam, "
    "glossy_skin, dramatic_shadows, depth_of_field, anime, masterpiece, best_quality"
)

CHAR_BASE = (
    "nelliel_parasol, 1girl, bleach, nelliel tu odelschwanck, green hair, long hair, "
    "ram skull, hollow mask on head, red facial stripe, large breasts, cleavage"
)

OUTFIT_BASE = (
    "open floral kimono robe, bikini top, sarong, japanese parasol, wagasa"
)

MALE = "disembodied_penis, 2penises"
DP = "doublepen, vaginal, anal, double_penetration, both_holes"

POSES = {
    # 25 Poses (832x1216 & 1024x1024)
    "cowgirl":           ("cowgirl_position, girl_on_top, straddling, front_view", 832, 1216),
    "reverse_cowgirl":   ("reverse_cowgirl, girl_on_top, facing_away, looking_back_at_viewer, ass_view", 832, 1216),
    "missionary":        ("missionary_position, on_back, legs_spread, front_view", 832, 1216),
    "doggystyle":        ("doggystyle, from_behind, on_all_fours, arched_back, looking_back_at_viewer", 832, 1216),
    "prone_bone":        ("prone_bone, lying, on_stomach, from_behind, ass_view", 832, 1216),
    "spooning":          ("spooning, lying, on_side, from_behind, legs_together", 832, 1216),
    "lotus":             ("lotus_position, legs_entwined, facing_each_other, front_view", 832, 1216),
    "spitroast":         ("spitroast, on_all_fours, arched_back, oral, side_view", 832, 1216),
    "desk_sex":          ("bent_over_desk, hands_on_desk, skirt_lift, from_behind, arched_back", 832, 1216),
    "edge_of_bed":       ("edge_of_bed, lying_on_back, legs_spread_wide, hanging_legs, front_view", 832, 1216),
    "double_vaginal":    ("double_vaginal, 2penises_in_one_hole, extreme_stretch, vaginal_penetration, front_view", 832, 1216),
    "chair_straddle":    ("sitting_on_chair, straddling, lap_sit, thighs_spread, front_view", 832, 1216),
    "pillow_face_plant": ("on_all_fours, face_pressed_in_pillow, ass_up, chest_on_bed, arched_back, from_behind", 832, 1216),
    "cowgirl_bridge":    ("cowgirl_position, girl_on_top, leaning_back, hands_behind_back, arched_back, front_view", 832, 1216),
    "against_glass":     ("pressed_against_glass, hands_on_glass, squished_breasts_against_glass, front_view", 832, 1216),
    "mating_press":        ("mating_press, folded, shoulders_pressed, legs_on_shoulders, thigh_squish, front_view", 832, 1216),
    "full_nelson":         ("full_nelson, nelson_position, lifted, legs_folded, front_view", 832, 1216),
    "piledriver":          ("piledriver, inverted, legs_up, upside_down, front_view", 832, 1216),
    "standing":            ("standing_sex, against_wall, held_up, legs_around_waist, front_view", 832, 1216),
    "suspended":           ("suspended_congress, held_up, legs_around_waist, lifting, front_view", 832, 1216),
    "standing_split":      ("standing_sex, one_leg_lifted, leg_on_shoulder, against_wall, standing_split, front_view", 832, 1216),
    "wheelbarrow":         ("wheelbarrow_position, held_by_legs, hands_on_floor, arched_back, from_behind, looking_back_at_viewer", 832, 1216),
    "jackknife":           ("jackknife_position, on_back, legs_folded_to_chest, extreme_flexibility, thighs_to_ears, front_view", 832, 1216),
    "wall_pin":            ("pinned_against_wall, against_wall, one_leg_lifted, lifted_by_thigh, front_view", 832, 1216),
    "inverted_suspension": ("suspended_upside_down, inverted, legs_spread_wide, hanging, front_view", 832, 1216),
}

STAGES_7 = [
    {
        "n": "01_resistencia",
        "depth": "(imminent penetration:1.2), penis_on_pussy",
        "expr": "wide_eyes, trembling, furrowed_brow, nervous, screaming, open_mouth",
        "hands": "hands_pushing_away, skin_indentation",
        "phys": "mattress_indentation",
        "clothes": "intact_clothing, kimono_lift, bikini_top, sarong_aside, panties_aside",
        "fluids": "sweat_drops, tears",
        "cam": "full_shot, front_view, (motion lines:1.2)",
    },
    {
        "n": "02_primer_impacto",
        "depth": "tip_in_pussy, first_insertion, stretching",
        "expr": "clenched_eyes, grimace, parted_lips, furrowed_brow, painful_expression, crying",
        "hands": "hands_gripping_sheets, white_knuckles",
        "phys": "breast_squish, hair_stuck_to_face, mattress_indentation",
        "clothes": "torn_kimono, exposed_breasts, bikini_top_aside, single_bare_shoulder",
        "fluids": "sweat, tears_streaming, saliva_string",
        "cam": "cowboy_shot, dutch_angle, (motion lines:1.3), (speed lines:1.2), sound_effects",
    },
    {
        "n": "03_ritmo",
        "depth": "(deep penetration:1.3), thrusting, (half insertion:1.2)",
        "expr": "half-closed_eyes, heavy_breathing, parted_lips, flushed_face, tear_tracks",
        "hands": "hands_above_head, clenched_hands",
        "phys": "bouncing_breasts, breast_squish, thigh_squish, flying_sweat_drops",
        "clothes": "shredded_kimono, exposed_breasts, open_kimono",
        "fluids": "sweat_drops, drooling, saliva_string, messy_tears",
        "cam": "medium_shot, dutch_angle, (motion lines:1.4), (speed lines:1.3), impact_lines, sound_effects, onomatopoeia",
    },
    {
        "n": "04_ahegao",
        "depth": "(deep penetration:1.4), full_penetration, (belly_bulge:1.1)",
        "expr": "ahegao, rolled_back_eyes, tongue_out, drooling, open_mouth, heavy_blush, forced_orgasm",
        "hands": "hands_above_head, fingers_twitching",
        "phys": "bouncing_breasts, belly_bulge, flying_sweat_drops",
        "clothes": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
        "fluids": "sweat_drops, tears_of_pleasure, excessive_drooling",
        "cam": "medium_close-up, dutch_angle, (motion lines:1.4), impact_lines, sound_effects, onomatopoeia",
    },
    {
        "n": "05_climax",
        "depth": "(deep penetration:1.5), (balls_deep:1.4), (belly_bulge:1.3)",
        "expr": "extreme_ahegao, heart_pupils, rolled_back_eyes, cross-eyed, tongue_out",
        "hands": "hands_above_head, trembling_fingers",
        "phys": "bouncing_breasts, belly_bulge, flying_sweat_drops, spasming",
        "clothes": "ruined_outfit, nude",
        "fluids": "excessive_sweat, tears_of_pleasure, excessive_cum, creampie, cum_overflow",
        "cam": "cowboy_shot, dutch_angle, dynamic_angle, (motion lines:1.5), (speed lines:1.4), impact_lines, sound_effects, onomatopoeia, japanese_text_sound_effects",
    },
    {
        "n": "06_rota",
        "depth": "balls_deep, (gaping:1.3), belly_bulge",
        "expr": "blank_eyes, empty_eyes, thousand_yard_stare, slack-jawed, mouth_slightly_open, emotionless",
        "hands": "limp_arms, hands_resting",
        "phys": "spasming_legs, mattress_indentation, hair_stuck_to_face",
        "clothes": "completely_nude, discarded_clothes",
        "fluids": "excessive_cum, cum_drip, cum_overflow, drooling",
        "cam": "close-up, low_angle, depth_of_field",
    },
    {
        "n": "07_inconsciente",
        "depth": "after_sex, gaping, cum_pool",
        "expr": "closed_eyes, sleeping, relaxed_face, serene_expression, dried_tears",
        "hands": "limp_arms, relaxed_posture",
        "phys": "disheveled_hair, messy_bed, soaked_sheets",
        "clothes": "completely_nude",
        "fluids": "dried_tears, semen_on_face, semen_on_body, cum_pool",
        "cam": "wide_shot, overhead_view, high_angle, depth_of_field",
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

def build_single_pose_workflow(pose_name):
    pose_tags, width, height = POSES[pose_name]
    nodes = {}
    nodes["ckpt"] = {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}}
    nodes["clip_skip"] = {"class_type": "CLIPSetLastLayer", "inputs": {"clip": ["ckpt", 1], "stop_at_clip_layer": -2}}
    nodes["lora_char"] = {"class_type": "LoraLoader", "inputs": {"model": ["ckpt", 0], "clip": ["clip_skip", 0], "lora_name": LORA_NAME, "strength_model": LORA_STRENGTH, "strength_clip": 1.0}}
    nodes["lora_depth"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_char", 0], "clip": ["lora_char", 1], "lora_name": "penetration_depth.safetensors", "strength_model": 1.5, "strength_clip": 1.0}}
    nodes["lora_dp"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_depth", 0], "clip": ["lora_depth", 1], "lora_name": "doublepenetration_r1.safetensors", "strength_model": 1.0, "strength_clip": 1.0}}
    nodes["lora_size"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_dp", 0], "clip": ["lora_dp", 1], "lora_name": "Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors", "strength_model": 0.5, "strength_clip": 1.0}}
    nodes["neg"] = {"class_type": "CLIPTextEncode", "inputs": {"text": NEG_BASE, "clip": ["lora_size", 1]}}

    for s in STAGES_7:
        parts = [
            "score_9, score_8_up, source_anime, rating_explicit",
            CHAR_BASE,
            OUTFIT_BASE,
            s["clothes"],
            MALE,
            DP,
            s["depth"],
            pose_tags,
            s["hands"],
            s["phys"],
            s["expr"],
            s["fluids"],
            s["cam"],
            LIGHTING_PRO
        ]
        prompt = clean_tags(", ".join([p for p in parts if p]))
        sn = s["n"]
        nodes[f"e_{sn}"] = {"class_type": "EmptyLatentImage", "inputs": {"width": width, "height": height, "batch_size": 1}}
        nodes[f"p_{sn}"] = {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["lora_size", 1]}}
        nodes[f"k_{sn}"] = {"class_type": "KSampler", "inputs": {"seed": SEED, "steps": STEPS, "cfg": CFG, "sampler_name": SAMPLER, "scheduler": SCHEDULER, "denoise": 1, "model": ["lora_size", 0], "positive": [f"p_{sn}", 0], "negative": ["neg", 0], "latent_image": [f"e_{sn}", 0]}}
        nodes[f"d_{sn}"] = {"class_type": "VAEDecode", "inputs": {"samples": [f"k_{sn}", 0], "vae": ["ckpt", 2]}}
        nodes[f"s_{sn}"] = {"class_type": "SaveImage", "inputs": {"filename_prefix": f"Bleach/nelliel_parasol/{pose_name}/nelliel_parasol_{pose_name}_{sn}", "images": [f"d_{sn}", 0]}}
    return nodes

def build_master_workflow():
    nodes = {}
    nodes["ckpt"] = {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}}
    nodes["clip_skip"] = {"class_type": "CLIPSetLastLayer", "inputs": {"clip": ["ckpt", 1], "stop_at_clip_layer": -2}}
    nodes["lora_char"] = {"class_type": "LoraLoader", "inputs": {"model": ["ckpt", 0], "clip": ["clip_skip", 0], "lora_name": LORA_NAME, "strength_model": LORA_STRENGTH, "strength_clip": 1.0}}
    nodes["lora_depth"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_char", 0], "clip": ["lora_char", 1], "lora_name": "penetration_depth.safetensors", "strength_model": 1.5, "strength_clip": 1.0}}
    nodes["lora_dp"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_depth", 0], "clip": ["lora_depth", 1], "lora_name": "doublepenetration_r1.safetensors", "strength_model": 1.0, "strength_clip": 1.0}}
    nodes["lora_size"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_dp", 0], "clip": ["lora_dp", 1], "lora_name": "Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors", "strength_model": 0.5, "strength_clip": 1.0}}
    nodes["neg"] = {"class_type": "CLIPTextEncode", "inputs": {"text": NEG_BASE, "clip": ["lora_size", 1]}}

    for pose_name, (pose_tags, width, height) in POSES.items():
        for s in STAGES_7:
            parts = [
                "score_9, score_8_up, source_anime, rating_explicit",
                CHAR_BASE,
                OUTFIT_BASE,
                s["clothes"],
                MALE,
                DP,
                s["depth"],
                pose_tags,
                s["hands"],
                s["phys"],
                s["expr"],
                s["fluids"],
                s["cam"],
                LIGHTING_PRO
            ]
            prompt = clean_tags(", ".join([p for p in parts if p]))
            key = f"{pose_name}_{s['n']}"
            nodes[f"e_{key}"] = {"class_type": "EmptyLatentImage", "inputs": {"width": width, "height": height, "batch_size": 1}}
            nodes[f"p_{key}"] = {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["lora_size", 1]}}
            nodes[f"k_{key}"] = {"class_type": "KSampler", "inputs": {"seed": SEED, "steps": STEPS, "cfg": CFG, "sampler_name": SAMPLER, "scheduler": SCHEDULER, "denoise": 1, "model": ["lora_size", 0], "positive": [f"p_{key}", 0], "negative": ["neg", 0], "latent_image": [f"e_{key}", 0]}}
            nodes[f"d_{key}"] = {"class_type": "VAEDecode", "inputs": {"samples": [f"k_{key}", 0], "vae": ["ckpt", 2]}}
            nodes[f"s_{key}"] = {"class_type": "SaveImage", "inputs": {"filename_prefix": f"Bleach/nelliel_parasol/{pose_name}/nelliel_parasol_{pose_name}_{s['n']}", "images": [f"d_{key}", 0]}}
    return nodes

def generate():
    count = 0
    for pose_name in POSES:
        wf = build_single_pose_workflow(pose_name)
        fname = f"workflow_sequence_{pose_name}.json"
        fpath = os.path.join(TARGET_DIR, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(wf, f, indent=2, ensure_ascii=False)
        count += 1
        print(f"[OK] [{count}/{len(POSES)}] {fname} ({POSES[pose_name][1]}x{POSES[pose_name][2]}) -> 7 etapas")

    master_wf = build_master_workflow()
    master_fpath = os.path.join(TARGET_DIR, "workflow_master.json")
    with open(master_fpath, "w", encoding="utf-8") as f:
        json.dump(master_wf, f, indent=2, ensure_ascii=False)
    
    total_imgs = count * len(STAGES_7)
    print(f"\n[DONE] nelliel_parasol completado: {count} workflows individuales + workflow_master.json ({total_imgs} imagenes en total).")

if __name__ == "__main__":
    generate()
