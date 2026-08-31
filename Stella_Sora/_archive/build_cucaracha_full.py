import json, os, re

B = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"
MALE = "disembodied_penis, 2penises, black_penis, dark_penis"
DP = "doublepen, vaginal, anal, double_penetration"
# POSE cucaracha (fija en las 10 etapas)
POSE = "on_back, legs_up, spread_legs, feet_in_air, legs_lifted, missionary_position, front_view"

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

def extract_chars(fn):
    src = open(fn, encoding="utf-8").read()
    ns = {}
    for const in ["CHITOSE_BASE", "NOYA_BASE"]:
        m = re.search(rf'{const}\s*=\s*"([^"]*)"', src)
        if m:
            ns[const] = m.group(1)
    start = src.index("CHARS = {")
    i = start + len("CHARS = ")
    depth = 0
    j = i
    while j < len(src):
        if src[j] == "{":
            depth += 1
        elif src[j] == "}":
            depth -= 1
            if depth == 0:
                break
        j += 1
    exec("CHARS = " + src[i:j+1], ns)
    return ns["CHARS"]

roster = {}
for fn in ["build_depth_versions.py", "build_more_chars.py", "build_final_chars.py"]:
    try:
        roster.update(extract_chars(fn))
    except Exception as e:
        print(f"⚠️ {fn}: {e}")

print(f"✅ Roster: {len(roster)} skins")

nodes = {}
nodes["ckpt"] = {"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":CKPT}}
nodes["latent_shared"] = {"class_type":"EmptyLatentImage","inputs":{"width":1024,"height":1536,"batch_size":1}}

for cname, cfg in roster.items():
    cs = f"clip_skip_{cname}"
    lc = f"lora_char_{cname}"
    ld = f"lora_depth_{cname}"
    dp = f"lora_dp_{cname}"
    ls = f"lora_size_{cname}"
    ng = f"neg_{cname}"

    strength = cfg.get("strength", 1.0)
    # Cadena LoRA compartida (1 por personaje, reutilizada en las 10 etapas)
    nodes[cs] = {"class_type":"CLIPSetLastLayer","inputs":{"clip":["ckpt",1],"stop_at_clip_layer":-2}}
    nodes[lc] = {"class_type":"LoraLoader","inputs":{"model":["ckpt",0],"clip":[cs,0],"lora_name":cfg["lora"],"strength_model":strength,"strength_clip":strength}}
    nodes[ld] = {"class_type":"LoraLoader","inputs":{"model":[lc,0],"clip":[lc,1],"lora_name":"penetration_depth.safetensors","strength_model":1.5,"strength_clip":1.0}}
    nodes[dp] = {"class_type":"LoraLoader","inputs":{"model":[ld,0],"clip":[ld,1],"lora_name":"doublepenetration_r1.safetensors","strength_model":1.0,"strength_clip":1.0}}
    nodes[ls] = {"class_type":"LoraLoader","inputs":{"model":[dp,0],"clip":[dp,1],"lora_name":"Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors","strength_model":0.5,"strength_clip":1.0}}
    nodes[ng] = {"class_type":"CLIPTextEncode","inputs":{"text":NEG + cfg.get("extra_neg",""),"clip":[ls,1]}}

    for n, depth, expr, motion, fluids, sound in STAGES:
        parts = ["score_9, score_8_up, source_anime, rating_explicit", cfg["char"], cfg["outfit"], MALE, DP, depth, POSE, hands_for(n), expr, fluids]
        if motion: parts.append(motion)
        if sound: parts.append(sound)
        parts.append(LIGHT + ", anime, masterpiece, best_quality")
        prompt = ", ".join([p for p in parts if p]).replace(", ,", ",").replace(",,", ",")
        key = f"{cname}_{n}"
        nodes[f"p_{key}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":[ls,1]}}
        nodes[f"k_{key}"] = {"class_type":"KSampler","inputs":{"seed":cfg.get("seed",42424299),"steps":20,"cfg":3.5,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":[ls,0],"positive":[f"p_{key}",0],"negative":[ng,0],"latent_image":["latent_shared",0]}}
        nodes[f"d_{key}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{key}",0],"vae":["ckpt",2]}}
        nodes[f"s_{key}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"cucaracha_{cname}_{n}","images":[f"d_{key}",0]}}

with open(os.path.join(B, "workflow_cucaracha_full.json"), "w", encoding="utf-8") as f:
    json.dump(nodes, f, indent=2, ensure_ascii=False)

saves = sum(1 for v in nodes.values() if v.get("class_type")=="SaveImage")
ks = sum(1 for v in nodes.values() if v.get("class_type")=="KSampler")
loras = sum(1 for k in nodes if k.startswith("lora_char_"))
print(f"✅ workflow_cucaracha_full.json")
print(f"   {saves} imagenes | {ks} KSamplers | {len(nodes)} nodos | {loras} personajes")
