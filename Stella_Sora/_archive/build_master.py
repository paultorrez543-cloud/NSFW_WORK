import json, os

B = "E:/ComfyUI/characters/Stella_Sora/fast"
CKPT = "waiIllustriousSDXL_v170.safetensors"
SEED = 42424249
NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"
MALE = "disembodied_penis, 2penises, black_penis, dark_penis"
DP = "doublepen, vaginal, anal, double_penetration, both_holes"

OUTFITS = {
    "default": {
        "char": "stell4virigiadef, 1girl, white hair, long hair, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, large breasts",
        "outfit": "white bonnet, white cloak, frilled cloak, black dress, detached collar, black bowtie, red ribbon, cleavage, black gloves, white pantyhose, high heels, clothes_lift",
        "tail_neg": "",
    },
    "bunny": {
        "char": "stell4virigiabnuy, 1girl, white hair, long hair, half up braid, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, mole on hip, large breasts",
        "outfit": "fake animal ears, rabbit ears, lace hairband, black hairband, detached collar, red bowtie, lace collar, fur armlet, cleavage, white leotard, strapless leotard, side-tie leotard, cross-laced leotard, highleg leotard, crotch zipper, showgirl skirt, white thighhighs, single fishnet thighhigh, mismatched legwear, frilled thigh strap, heart o-ring, wrist cuffs, lace-trimmed wrist cuffs, ankle strap, red high heels, clothes_lift",
        "tail_neg": ", tail, demon tail, animal tail",
    },
}

POSES = {
    "cowgirl":         "cowgirl_position, girl_on_top, straddling, front_view",
    "doggystyle":      "doggystyle, from_behind, arched_back, hands_on_hips, front_view",
    "missionary":      "missionary_position, male_on_top, female_on_bottom, legs_spread, front_view",
    "full_nelson":     "full_nelson, nelson_position, restrained, legs_folded, front_view",
    "mating_press":    "mating_press, folded, shoulders_pressed, legs_on_shoulders, front_view",
    "spitroast":       "spitroast, on_all_fours, from_behind, arched_back, oral, front_view",
    "prone_bone":      "prone_bone, lying, on_stomach, from_behind, legs_together, front_view",
    "reverse_cowgirl": "reverse_cowgirl, girl_on_top, facing_away, looking_back, front_view",
    "piledriver":      "piledriver, inverted, legs_up, upside_down, front_view",
    "standing":        "standing_sex, against_wall, held_up, legs_around_waist, front_view",
    "spooning":        "spooning, lying, on_side, from_behind, legs_together, front_view",
    "suspended":       "suspended_congress, held_up, legs_around_waist, lifting, front_view",
    "lotus":           "lotus_position, legs_entwined, facing_each_other, front_view",
}

STAGES = [
    {"n":"01_miedo",       "depth":"(imminent penetration:1.2)", "expr":"scared, nervous_sweat, struggling", "motion":"", "fluids":"nervous_sweat", "sound":""},
    {"n":"02_resistencia", "depth":"about_to_penetrate, penis_on_pussy", "expr":"crying, (screaming:1.5), struggling, begging", "motion":"(motion lines:1.2)", "fluids":"sweat, tears_streaming", "sound":""},
    {"n":"03_dolor",       "depth":"tip_in_pussy, first_insertion", "expr":"(pain:1.3), tears_streaming, screaming", "motion":"(motion lines:1.3), (speed lines:1.2)", "fluids":"sweat, tears_streaming", "sound":"sound_effects"},
    {"n":"04_sufrimiento", "depth":"half_insertion, stretching", "expr":"(pain:1.4), sobbing, tears_streaming", "motion":"(motion lines:1.3), impact_lines", "fluids":"sweat, tears_streaming, drooling", "sound":"sound_effects, onomatopoeia"},
    {"n":"05_quebranto",   "depth":"(deep penetration:1.3)", "expr":"tears_streaming, broken_spirit, defeated", "motion":"(motion lines:1.4), (speed lines:1.3)", "fluids":"sweat_drops, tears_streaming, drooling", "sound":"sound_effects, onomatopoeia"},
    {"n":"06_ahegao_inicio","depth":"(deep penetration:1.4), full_penetration", "expr":"rolled_back_eyes, tongue_out, drooling, ahegao", "motion":"(motion lines:1.4), impact_lines", "fluids":"sweat_drops, tears_of_pleasure, drooling", "sound":"sound_effects, onomatopoeia"},
    {"n":"07_ahegao_total","depth":"(deep penetration:1.5), balls_deep", "expr":"ahegao, heart_pupils, mind_break, excessive_cum, creampie", "motion":"(motion lines:1.5), (speed lines:1.4), impact_lines", "fluids":"excessive_sweat, tears_of_pleasure, drooling", "sound":"sound_effects, onomatopoeia, japanese_text_sound_effects"},
    {"n":"08_rota",         "depth":"balls_deep, gaping", "expr":"blank_eyes, mind_break, tears_streaming", "motion":"", "fluids":"excessive_sweat, tears_streaming, drooling", "sound":""},
    {"n":"09_destruida",    "depth":"after_sex, gaping", "expr":"exhausted, crying, semen_on_body, cum_pool", "motion":"", "fluids":"excessive_sweat, dried_tears, semen_on_body", "sound":""},
    {"n":"10_inconsciente", "depth":"after_sex, sleeping", "expr":"sleeping, tears_streaming, semen_on_face", "motion":"", "fluids":"dried_tears, semen_on_body", "sound":""},
]

def hands_for(stage):
    n = stage["n"]
    if n in ["01_miedo","02_resistencia"]: return "hands_above_head"
    if n in ["03_dolor","04_sufrimiento"]: return "hands_gripping_sheets"
    if n in ["08_rota","09_destruida","10_inconsciente"]: return "hands_resting, limp_arms"
    return "hands_above_head"

def build_master(outfit_name):
    cfg = OUTFITS[outfit_name]
    nodes = {}
    # Shared base (una sola cadena LoRA para las 13 poses)
    nodes["ckpt"] = {"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":CKPT}}
    nodes["clip_skip"] = {"class_type":"CLIPSetLastLayer","inputs":{"clip":["ckpt",1],"stop_at_clip_layer":-2}}
    nodes["lora_char"] = {"class_type":"LoraLoader","inputs":{"model":["ckpt",0],"clip":["clip_skip",0],"lora_name":"Stella-Virigia-v1.safetensors","strength_model":1.0,"strength_clip":1.0}}
    nodes["lora_depth"] = {"class_type":"LoraLoader","inputs":{"model":["lora_char",0],"clip":["lora_char",1],"lora_name":"penetration_depth.safetensors","strength_model":1.5,"strength_clip":1.0}}
    nodes["lora_dp"] = {"class_type":"LoraLoader","inputs":{"model":["lora_depth",0],"clip":["lora_depth",1],"lora_name":"doublepenetration_r1.safetensors","strength_model":1.0,"strength_clip":1.0}}
    nodes["lora_size"] = {"class_type":"LoraLoader","inputs":{"model":["lora_dp",0],"clip":["lora_dp",1],"lora_name":"Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors","strength_model":0.5,"strength_clip":1.0}}
    nodes["neg"] = {"class_type":"CLIPTextEncode","inputs":{"text":NEG + cfg["tail_neg"],"clip":["lora_size",1]}}
    # Un solo latent compartido por todas las poses/etapas
    nodes["latent_shared"] = {"class_type":"EmptyLatentImage","inputs":{"width":1024,"height":768,"batch_size":1}}

    for pose_name, pose_tags in POSES.items():
        for s in STAGES:
            parts = ["score_9, score_8_up, source_anime, rating_explicit", cfg["char"], cfg["outfit"], MALE, DP, s["depth"], pose_tags, hands_for(s), s["expr"], s["fluids"]]
            if s["motion"]: parts.append(s["motion"])
            if s["sound"]: parts.append(s["sound"])
            parts.append(LIGHT + ", anime, masterpiece, best_quality")
            prompt = ", ".join(parts).replace(", ,", ",").replace(",,", ",")
            
            key = f"{pose_name}_{s['n']}"
            nodes[f"p_{key}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":["lora_size",1]}}
            nodes[f"k_{key}"] = {"class_type":"KSampler","inputs":{"seed":SEED,"steps":20,"cfg":3.5,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":["lora_size",0],"positive":[f"p_{key}",0],"negative":["neg",0],"latent_image":["latent_shared",0]}}
            nodes[f"d_{key}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{key}",0],"vae":["ckpt",2]}}
            nodes[f"s_{key}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"virigia_{outfit_name}_{pose_name}_{s['n']}","images":[f"d_{key}",0]}}
    
    return nodes

for outfit in OUTFITS:
    wf = build_master(outfit)
    fname = f"workflow_master_{outfit}.json"
    with open(os.path.join(B, fname), "w", encoding="utf-8") as f:
        json.dump(wf, f, indent=2, ensure_ascii=False)
    n = sum(1 for v in wf.values() if v.get("class_type")=="SaveImage")
    print(f"✅ workflow_master_{outfit}.json → {n} imagenes ({len(POSES)} poses x {len(STAGES)} etapas)")

print(f"\n🎯 2 masters: 1 por outfit, cadena LoRA compartida (más eficiente)")
