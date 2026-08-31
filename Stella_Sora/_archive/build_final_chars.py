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

# Chitose base appearance (trigger dvychitose)
CHITOSE_BASE = "purple eyes, bright pupils, white pupils, multicolored hair, colored inner hair, black hair, purple hair"
# Noya base appearance (trigger stsrnya)
NOYA_BASE = "blonde hair, long hair, blue eyes, star-shaped pupils, single earring, gradient hair, half crown braid, streaked hair, ahoge, large breasts"

CHARS = {
    "chitose_default": {"lora":"Chitose_Dovellys.safetensors","seed":42424291,"strength":1.0,
        "char":f"dvydfchitose, 1girl, {CHITOSE_BASE}, ahoge, one side up, two-tone hair, hair ornament",
        "outfit":"black serafuku, black sailor collar, collared shirt, crop top overhang, purple ribbon, black skirt, bandaged leg, clothes_lift","extra_neg":""},
    "chitose_kimono": {"lora":"Chitose_Dovellys.safetensors","seed":42424292,"strength":1.0,
        "char":f"dvykmchitose, 1girl, {CHITOSE_BASE}, twintails",
        "outfit":"japanese clothes, white kimono, bare shoulders, wide sleeves, long sleeves, puffy sleeves, ribbon trimmed sleeves, off shoulder, pom pom hair ornament, blue hairclip, x hair ornament, detached collar, blue collar, obi, purple sash, hakama skirt, pleated skirt, miniskirt, blue skirt, blue hakama, white thigh strap, thighhighs, white thighhighs, clothes_lift","extra_neg":""},
    "chitose_swimsuit": {"lora":"Chitose_Dovellys.safetensors","seed":42424293,"strength":1.0,
        "char":f"dvyswchitose, 1girl, {CHITOSE_BASE}, high ponytail, large breasts",
        "outfit":"side-tie bikini bottom, multi-strapped bikini bottom, string bikini, highleg bikini, o-ring bikini, o-ring top, front-tie top, clothes_lift","extra_neg":""},
    "noya_default": {"lora":"Noya_stella_sora.safetensors","seed":42424294,"strength":1.0,
        "char":f"stsrnya, 1girl, {NOYA_BASE}",
        "outfit":"white dress, two-tone dress, high-low dress, jewelry, red ribbon, shirt, sideboob, navel, belt, pouch, teddy bear, white skirt, black frills, arm strap, black gloves, thighs, black footwear, boots, clothes_lift","extra_neg":""},
    "noya_loungewear": {"lora":"Noya_stella_sora.safetensors","seed":42424295,"strength":1.0,
        "char":f"stsrnya, 1girl, {NOYA_BASE}",
        "outfit":"cropped shirt, yellow shirt, print shirt, clothes writing, drawstring, crop top overhang, bra strap, sleeves past wrists, long sleeves, bare shoulders, off shoulder, open jacket, white jacket, open clothes, midriff, short shorts, yellow shorts, teddy bear, clothes_lift","extra_neg":""},
    "noya_bikini": {"lora":"Noya_stella_sora.safetensors","seed":42424296,"strength":1.0,
        "char":f"stsrnya, 1girl, {NOYA_BASE}",
        "outfit":"vertical-striped bikini, red-framed eyewear, sunglasses, eyewear on head, heart-shaped eyewear, halterneck, aqua bikini, white bikini, black trim, white straps, thigh belt, bead necklace, star necklace, black straps, mismatched bikini, front-tie bikini top, wrist scrunchie, white belt, studded belt, heart o-ring, highleg bikini, teddy bear, clothes_lift","extra_neg":""},
    "otoha_ninja": {"lora":"Otoha_stella_sora.safetensors","seed":42424286,"strength":1.0,
        "char":"stsroto, 1girl, long hair, half up braid, white hair, grey hair, mole, blue eyes, animal ear fluff, animal ears, fox ears, fox tail, large breasts",
        "outfit":"ninja, black leotard, highleg leotard, sleeveless leotard, bare shoulders, cleavage cutout, sarashi, underbust, belt, neck flower, red tassel, black gloves, elbow gloves, fingerless gloves, brown pantyhose, thighs, hair ornament, hair flower, black footwear, high heels, knee boots, high heel boots, clothes_lift","extra_neg":""},
    "tyrant_pijama": {"lora":"tyrant_v2.safetensors","seed":42424287,"strength":0.8,
        "char":"tyrant, 1girl, grey hair, long hair, blue eyes, pointy ears",
        "outfit":"white dress, sleep mask, jewelry, sleeveless dress, necklace, mask on head, wrist scrunchie, clothes_lift","extra_neg":""},
    "tyrant_bikini": {"lora":"tyrant_v2.safetensors","seed":42424288,"strength":0.8,
        "char":"tyrant, 1girl, grey hair, long hair, blue eyes, pointy ears",
        "outfit":"alternate costume, bikini, frilled bikini, single leg garter, highleg, bare legs, hairband, clothes_lift","extra_neg":""},
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

print(f"\n🎯 {len(CHARS)} outfits nuevos")
