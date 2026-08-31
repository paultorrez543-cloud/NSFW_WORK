import json, os

B = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"
MALE = "disembodied_penis, black_penis, dark_penis"

NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark"

# 6 etapas — dominación + fluidos progresivos
STAGES = [
    ("01_orden",        "(imminent penetration:1.2)", "obedient, kneeling, blush, nervous_sweat, hands_on_male_chest", "", "nervous_sweat", ""),
    ("02_resistencia",  "about_to_penetrate, penis_on_pussy", "reluctant, struggling, tears_streaming, crying, pushing_away", "(motion lines:1.2)", "sweat, tears_streaming", ""),
    ("03_castigo",      "tip_in_pussy, first_insertion", "(pain:1.3), bound, spanking, tears_streaming, screaming", "(motion lines:1.3), impact_lines", "sweat, tears_streaming, drooling", "sound_effects"),
    ("04_sumision",     "(deep penetration:1.4)", "submissive, moaning, ahegao, tongue_out, rolled_back_eyes", "(motion lines:1.4)", "sweat_drops, excessive_drooling", "sound_effects, onomatopoeia"),
    ("05_climax",       "(deep penetration:1.5), balls_deep", "ahegao, heart_pupils, mind_break, orgasm, creampie", "(motion lines:1.5), (speed lines:1.4), impact_lines", "excessive_sweat, tears_of_pleasure, drooling", "sound_effects, onomatopoeia, japanese_text_sound_effects"),
    ("06_ruina",        "after_sex, gaping", "exhausted, broken, semen_on_body, cum_pool, blank_eyes", "", "excessive_sweat, dried_tears, semen_on_body", ""),
]

# 5 poses
POSES = {
    "cowgirl":         "cowgirl_position, girl_on_top, straddling, front_view",
    "doggystyle":      "doggystyle, from_behind, all_fours, front_view",
    "missionary":      "missionary_position, legs_up, spread_legs, front_view",
    "mating_press":    "mating_press, legs_above_head, folded, front_view",
    "reverse_cowgirl": "reverse_cowgirl, girl_on_top, facing_away, front_view",
}

# Personaje (cambiable)
CHAR = "stell4virigiadef, 1girl, white hair, long hair, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, large breasts"
OUTFIT = "white bonnet, white cloak, frilled cloak, black dress, detached collar, black bowtie, red ribbon, cleavage, black gloves, white pantyhose, high heels, clothes_lift"
EXTRA_NEG = ", holding mirror, red mirror, mirror"
LORA = "Stella-Virigia-v1.safetensors"
SEED = 42424249

nodes = {}
nodes["ckpt"] = {"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":CKPT}}
nodes["latent_shared"] = {"class_type":"EmptyLatentImage","inputs":{"width":1024,"height":1536,"batch_size":1}}
nodes["clip_skip"] = {"class_type":"CLIPSetLastLayer","inputs":{"clip":["ckpt",1],"stop_at_clip_layer":-2}}
nodes["lora_char"] = {"class_type":"LoraLoader","inputs":{"model":["ckpt",0],"clip":["clip_skip",0],"lora_name":LORA,"strength_model":1.0,"strength_clip":1.0}}
nodes["lora_depth"] = {"class_type":"LoraLoader","inputs":{"model":["lora_char",0],"clip":["lora_char",1],"lora_name":"penetration_depth.safetensors","strength_model":1.5,"strength_clip":1.0}}
nodes["lora_dp"] = {"class_type":"LoraLoader","inputs":{"model":["lora_depth",0],"clip":["lora_depth",1],"lora_name":"doublepenetration_r1.safetensors","strength_model":1.0,"strength_clip":1.0}}
nodes["lora_size"] = {"class_type":"LoraLoader","inputs":{"model":["lora_dp",0],"clip":["lora_dp",1],"lora_name":"Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors","strength_model":0.5,"strength_clip":1.0}}
nodes["neg"] = {"class_type":"CLIPTextEncode","inputs":{"text":NEG + EXTRA_NEG,"clip":["lora_size",1]}}

for pose_name, pose_tags in POSES.items():
    for n, depth, expr, motion, fluids, sound in STAGES:
        parts = ["score_9, score_8_up, source_anime, rating_explicit", CHAR, OUTFIT, MALE, "doublepen, vaginal, anal, double_penetration, both_holes", depth, pose_tags, expr, fluids]
        if motion: parts.append(motion)
        if sound: parts.append(sound)
        parts.append(LIGHT + ", anime, masterpiece, best_quality")
        prompt = ", ".join([p for p in parts if p]).replace(", ,", ",").replace(",,", ",")
        key = f"{pose_name}_{n}"
        nodes[f"p_{key}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":["lora_size",1]}}
        nodes[f"k_{key}"] = {"class_type":"KSampler","inputs":{"seed":SEED,"steps":20,"cfg":3.5,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":["lora_size",0],"positive":[f"p_{key}",0],"negative":["neg",0],"latent_image":["latent_shared",0]}}
        nodes[f"d_{key}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{key}",0],"vae":["ckpt",2]}}
        nodes[f"s_{key}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"virigia_{pose_name}_{n}","images":[f"d_{key}",0]}}

with open(os.path.join(B, "workflow_virigia_30img.json"), "w", encoding="utf-8") as f:
    json.dump(nodes, f, indent=2, ensure_ascii=False)

n = sum(1 for v in nodes.values() if v.get("class_type")=="SaveImage")
print(f"✅ workflow_virigia_30img.json → {n} imagenes (5 poses x 6 etapas)")
