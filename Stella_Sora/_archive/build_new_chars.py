import json, os

B = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"
MALE = "disembodied_penis, 2penises, black_penis, dark_penis"
DP = "doublepen, vaginal, anal, double_penetration"
POSE = "reverse_cowgirl, girl_on_top, facing_away, looking_back, front_view"

NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark"

# 10 etapas non-con (reutilizadas)
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
    "amber":     {"lora":"Amber_Stella_Sora.safetensors","seed":42424261,
        "char":"AmberSora, 1girl, black hair, yellow eyes, hair ornament, hood down, fingerless gloves",
        "outfit":"white dress, sideless dress, thighhighs, thigh boots, clothes_lift","extra_neg":" black cat"},
    "portia":    {"lora":"Portia_Stella_Sora.safetensors","seed":42424262,
        "char":"Portia, 1girl, visor cap, long hair, green hair, mole under eye, mole under mouth",
        "outfit":"employee uniform, strap slip, button gap, waist apron, clothes_lift","extra_neg":""},
    "freesia":   {"lora":"Freesia_Stella-10.safetensors","seed":42424263,
        "char":"Freesia_Stella, 1girl, long hair, red eyes, side ponytail, grey hair, hair ornament, hair flower, white flower, sidelocks, blunt bangs",
        "outfit":"long sleeves, red shirt, collared shirt, double-breasted, buttons, pleated skirt, miniskirt, grey skirt, blue jacket, peaked cap, military hat, black headwear, military uniform, necktie, white pantyhose, thigh strap, clothes_lift","extra_neg":""},
    "laru":      {"lora":"Laru_Dovellys.safetensors","seed":42424264,
        "char":"laru stella sora, 1girl, twintails, grey hair, purple eyes, skin fang",
        "outfit":"peaked cap, blue headwear, white dress, puffy long sleeves, blue cape, blue jacket, white thighhighs, blue footwear, high heels, high heel boots, clothes_lift","extra_neg":""},
    "nazuka":    {"lora":"Nazuka_Dovellys.safetensors","seed":42424265,
        "char":"nazuka stella sora, 1girl, black hair, red eyes, hairband, hair flower, hair ornament",
        "outfit":"short dress, orange dress, white shirt, blue cape, detached sleeves, frilled sleeves, white choker, frilled choker, frilled gloves, white gloves, clothes_lift","extra_neg":" staff, holding staff"},
    "kaede":     {"lora":"Kaede_Dovellys.safetensors","seed":42424266,
        "char":"kaede stella sora, 1girl, pink hair, blue eyes, hair ornament, hair flower",
        "outfit":"white dress, fur collar, bare shoulders, puffy long sleeves, red shawl, yellow bow, black pantyhose, black footwear, clothes_lift","extra_neg":""},
    "tilia":     {"lora":"Tilia_Dovellys.safetensors","seed":42424267,
        "char":"tilia stella sora, 1girl, blonde hair, red eyes, hairclip, hair ornament, ahoge, side ponytail",
        "outfit":"black shirt, white collar, shoulder armor, gauntlets, pauldrons, blue skirt, white thighhighs, armored boots, high heel boots, clothes_lift","extra_neg":""},
    "canace":    {"lora":"Canace_Dovellys.safetensors","seed":42424268,
        "char":"canace stella sora, 1girl, purple eyes, semi-rimless eyewear, purple hair, grey hair, hair ribbon",
        "outfit":"white dress, bare shoulders, red necktie, necktie between breasts, miniskirt, pleated skirt, white skirt, clothes_lift","extra_neg":""},
    "caramel":   {"lora":"Caramel_Dovellys.safetensors","seed":42424269,
        "char":"caramel stella sora, 1girl, animal ears, animal ear fluff, multicolored hair, blonde hair, twintails, drill hair, hair ribbon",
        "outfit":"black dress, purple jacket, striped clothes, spiked collar, black collar, frilled skirt, black skirt, asymmetrical legwear, mismatched legwear, fishnets, lace-trimmed legwear, striped thighhighs, o-ring thigh strap, knee boots, pink ribbon, purple ribbon, clothes_lift","extra_neg":""},
    "cosette":   {"lora":"Cosette_Dovellys.safetensors","seed":42424270,
        "char":"cosette stella sora, 1girl, green eyes, two-tone hair, multicolored hair, white hair, black hair, hair ornament",
        "outfit":"black dress, clothing cutout, stomach cutout, navel cutout, cleavage cutout, pelvic curtain, black cloak, blue cape, torn thighhighs, blue thighhighs, single thighhigh, asymmetrical legwear, leg tattoo, o-ring, o-ring bottom, thigh strap, black footwear, clothes_lift","extra_neg":" bandage"},
    "fuyuka":    {"lora":"FuyukaSS-10.safetensors","seed":42424271,
        "char":"fuyuka_ss, 1girl, long hair, red eyes, white hair, large breasts",
        "outfit":"long sleeves, black gloves, white shorts, yellow boots, gold gauntlets, cleavage cutout, clothes_lift","extra_neg":""},
    "firefly":   {"lora":"FFSS-10.safetensors","seed":42424272,
        "char":"ffstella, 1girl, short hair, huge ahoge, ahoge, red eyes, brown hair, streaked hair, white hair",
        "outfit":"scarf, white dress, sleeveless dress, black hairband, socks, loafers, bare shoulders, clothes_lift","extra_neg":""},
    "iris":      {"lora":"IrisStellaSora_IXL.safetensors","seed":42424273,
        "char":"zzIris, 1girl, red eyes, purple hair, long hair",
        "outfit":"hair ornament, long sleeves, hat, white shirt, hairclip, puffy sleeves, black skirt, cape, black pantyhose, black headwear, beret, knee boots, juliet sleeves, red necktie, cross-laced footwear, high heel boots, high-waist skirt, lace-up boots, clothes_lift","extra_neg":""},
    "mistique":  {"lora":"MistiqueStellaSora_IXL.safetensors","seed":42424274,
        "char":"zzMistique, 1girl, orange eyes, orange hair, hair between eyes, long hair, twintails",
        "outfit":"witch, black dress, frilled dress, pink bow, purple bow, juliet sleeves, puffy sleeves, garter straps, witch hat, brooch, clothes_lift","extra_neg":""},
}

def build(cname, cfg):
    nodes = {}
    nodes["ckpt"] = {"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":CKPT}}
    nodes["clip_skip"] = {"class_type":"CLIPSetLastLayer","inputs":{"clip":["ckpt",1],"stop_at_clip_layer":-2}}
    nodes["lora_char"] = {"class_type":"LoraLoader","inputs":{"model":["ckpt",0],"clip":["clip_skip",0],"lora_name":cfg["lora"],"strength_model":1.0,"strength_clip":1.0}}
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
    print(f"✅ {cname}/workflow_master.json → 10 etapas")

print(f"\n🎯 {len(CHARS)} personajes nuevos (reverse cowgirl x 10 etapas)")
print(f"   NOTA: Firenze (2597586) sin triggers en API — requiere extracción manual")
