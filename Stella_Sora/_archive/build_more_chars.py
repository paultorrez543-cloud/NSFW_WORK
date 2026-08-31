import json, os

B = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"
MALE = "disembodied_penis, 2penises, black_penis, dark_penis"
DP = "doublepen, vaginal, anal, double_penetration"
POSE = "reverse_cowgirl, girl_on_top, facing_away, looking_back, front_view"

NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark"

STAGES = [
    ("01_miedo",       "(imminent penetration:1.2)", "scared, nervous_sweat, struggling", "", "nervous_sweat", ""),
    ("02_resistencia", "about_to_penetrate, penis_on_pussy", "crying, (screaming:1.5), struggling, begging", "(motion lines:1.2)", "sweat, tears_streaming", ""),
    ("03_dolor",       "tip_in_pussy, first_insertion", "(pain:1.3), tears_streaming, screaming", "(motion lines:1.3), (speed lines:1.2)", "sweat, tears_streaming", "sound_effects"),
    ("04_sufrimiento", "half_insertion, stretching", "(pain:1.4), sobbing, tears_streaming", "(motion lines:1.3), impact_lines", "sweat, tears_streaming, drooling", "sound_effects, onomatopoeia"),
    ("05_quebranto",   "(deep penetration:1.3)", "tears_streaming, broken_spirit, defeated", "(motion lines:1.4), (speed lines:1.3)", "sweat_drops, tears_streaming, drooling", "sound_effects, onomatopoeia"),
    ("06_ahegao_inicio","(deep penetration:1.4), full_penetration", "rolled_back_eyes, tongue_out, drooling, ahegao", "(motion lines:1.4), impact_lines", "sweat_drops, tears_of_pleasure, drooling", "sound_effects, onomatopoeia"),
    ("07_ahegao_total","(deep penetration:1.5), balls_deep", "ahegao, heart_pupils, mind_break, excessive_cum, creampie", "(motion lines:1.5), (speed lines:1.4), impact_lines", "excessive_sweat, tears_of_pleasure, drooling", "sound_effects, onomatopoeia, japanese_text_sound_effects"),
    ("08_rota",         "balls_deep, gaping", "blank_eyes, mind_break, tears_streaming", "", "excessive_sweat, tears_streaming, drooling", ""),
    ("09_destruida",    "after_sex, gaping", "exhausted, crying, semen_on_body, cum_pool", "", "excessive_sweat, dried_tears, semen_on_body", ""),
    ("10_inconsciente", "after_sex, sleeping", "sleeping, tears_streaming, semen_on_face", "", "dried_tears, semen_on_body", ""),
]

def hands_for(n):
    if n in ["01_miedo","02_resistencia"]: return "hands_above_head"
    if n in ["03_dolor","04_sufrimiento"]: return "hands_gripping_sheets"
    if n in ["08_rota","09_destruida","10_inconsciente"]: return "hands_resting, limp_arms"
    return "hands_above_head"

CHARS = {
    "nazuna": {"lora":"NazunaStellaSora_IXL.safetensors","seed":42424281,"strength":1.0,
        "char":"zzNazuna, 1girl, pink eyes, purple eyes, green hair, hair between eyes, long hair, multicolored hair, streaked hair, two-tone hair, white hair, twin braids",
        "outfit":"brown beret, loose socks, sleeves past fingers, white dress, yellow jacket, clothes_lift","extra_neg":""},
    "bastelina": {"lora":"bastelina_stellasora-v01.safetensors","seed":42424282,"strength":1.0,
        "char":"bastelina_stella, 1girl, folded braids, white hair, green eyes",
        "outfit":"white coat, white hat, white pencil dress, exposed shoulders, white pantyhose, white belt, multiple belts, gold trim, white bag, shoes, clothes_lift","extra_neg":""},
    "flora": {"lora":"Flora_Stella_Sora.safetensors","seed":42424283,"strength":1.0,
        "char":"Flora stella sora, 1girl",
        "outfit":"hat, elbow gloves, detached sleeves, pantyhose, dress, high heels, clothes_lift","extra_neg":""},
    "tyrant": {"lora":"tyrant_v2.safetensors","seed":42424284,"strength":0.8,
        "char":"tyrant, 1girl, grey hair, long hair, blue eyes, pointy ears",
        "outfit":"gloves, thighhighs, dress, white thighhighs, black gloves, hairband, blue dress, sleeveless, blue hairband, necktie, sleeveless dress, collared dress, clothes_lift","extra_neg":""},
    "otoha": {"lora":"Otoha_stella_sora.safetensors","seed":42424285,"strength":1.0,
        "char":"stsroto, 1girl, long hair, half up braid, white hair, grey hair, mole, blue eyes, animal ear fluff, animal ears, fox ears, fox tail, large breasts",
        "outfit":"wa maid, cleavage, long sleeves, detached sleeves, wide sleeves, frills, floral print, frilled apron, white apron, waist apron, maid apron, blue kimono, sash, obi, purple gemstone, star-shaped gem, elbow gloves, white gloves, pleated skirt, long skirt, side slit, white thighhighs, hair ornament, hair flower, maid headdress, white flower, black footwear, high heels, clothes_lift","extra_neg":", holding umbrella"},
}

def build(cname, cfg):
    nodes = {}
    nodes["ckpt"] = {"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":CKPT}}
    nodes["clip_skip"] = {"class_type":"CLIPSetLastLayer","inputs":{"clip":["ckpt",1],"stop_at_clip_layer":-2}}
    nodes["lora_char"] = {"class_type":"LoraLoader","inputs":{"model":["ckpt",0],"clip":["clip_skip",0],"lora_name":cfg["lora"],"strength_model":cfg["strength"],"strength_clip":cfg["strength"]}}
    nodes["lora_depth"] = {"class_type":"LoraLoader","inputs":{"model":["lora_char",0],"clip":["lora_char",1],"lora_name":"penetration_depth.safetensors","strength_model":1.5,"strength_clip":1.0}}
    nodes["lora_dp"] = {"class_type":"LoraLoader","inputs":{"model":["lora_depth",0],"clip":["lora_depth",1],"lora_name":"doublepenetration_r1.safetensors","strength_model":1.0,"strength_clip":1.0}}
    nodes["lora_size"] = {"class_type":"LoraLoader","inputs":{"model":["lora_dp",0],"clip":["lora_dp",1],"lora_name":"Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors","strength_model":0.5,"strength_clip":1.0}}
    nodes["neg"] = {"class_type":"CLIPTextEncode","inputs":{"text":NEG + cfg["extra_neg"],"clip":["lora_size",1]}}
    nodes["latent_shared"] = {"class_type":"EmptyLatentImage","inputs":{"width":1024,"height":1536,"batch_size":1}}

    for n, depth, expr, motion, fluids, sound in STAGES:
        parts = ["score_9, score_8_up, source_anime, rating_explicit", cfg["char"], cfg["outfit"], MALE, DP, depth, POSE, hands_for(n), expr, fluids]
        if motion: parts.append(motion)
        if sound: parts.append(sound)
        parts.append(LIGHT + ", anime, masterpiece, best_quality")
        prompt = ", ".join([p for p in parts if p]).replace(", ,", ",").replace(",,", ",")
        nodes[f"p_{n}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":["lora_size",1]}}
        nodes[f"k_{n}"] = {"class_type":"KSampler","inputs":{"seed":cfg["seed"],"steps":20,"cfg":3.5,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":["lora_size",0],"positive":[f"p_{n}",0],"negative":["neg",0],"latent_image":["latent_shared",0]}}
        nodes[f"d_{n}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{n}",0],"vae":["ckpt",2]}}
        nodes[f"s_{n}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"{cname}_{n}","images":[f"d_{n}",0]}}
    return nodes

for cname, cfg in CHARS.items():
    cdir = os.path.join(B, cname)
    os.makedirs(cdir, exist_ok=True)
    wf = build(cname, cfg)
    with open(os.path.join(cdir, "workflow_master.json"), "w", encoding="utf-8") as f:
        json.dump(wf, f, indent=2, ensure_ascii=False)
    print(f"✅ {cname}/workflow_master.json (strength={cfg['strength']})")

print(f"\n🎯 {len(CHARS)} personajes nuevos (Illustrious)")
print("⚠️ Chitose y Noya son base ANIMA — incompatibles con waiIllustrious")
