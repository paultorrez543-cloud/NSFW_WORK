import json, os, re

B = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"
MALE = "disembodied_penis, 2penises, black_penis, dark_penis"
DP = "doublepen, vaginal, anal, double_penetration"
# POSE cucaracha: boca arriba, piernas levantadas y abiertas
POSE = "on_back, legs_up, spread_legs, feet_in_air, legs_lifted, missionary_position, front_view"
EXPR = "rolled_back_eyes, tongue_out, drooling, ahegao"
DEPTH = "(deep penetration:1.4), full_penetration"

NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark"

def extract_chars(fn):
    src = open(fn, encoding="utf-8").read()
    ns = {}
    # Extraer constantes base (CHITOSE_BASE, NOYA_BASE) si existen
    for const in ["CHITOSE_BASE", "NOYA_BASE"]:
        m = re.search(rf'{const}\s*=\s*"([^"]*)"', src)
        if m:
            ns[const] = m.group(1)
    # Encontrar "CHARS = {" y su cierre balanceado
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
    block = src[i:j+1]
    exec("CHARS = " + block, ns)
    return ns["CHARS"]

# Fusionar roster de todos los scripts
roster = {}
for fn in ["build_depth_versions.py", "build_more_chars.py", "build_final_chars.py"]:
    try:
        roster.update(extract_chars(fn))
    except Exception as e:
        print(f"⚠️ {fn}: {e}")

print(f"✅ Roster cargado: {len(roster)} variantes")

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
    nodes[cs] = {"class_type":"CLIPSetLastLayer","inputs":{"clip":["ckpt",1],"stop_at_clip_layer":-2}}
    nodes[lc] = {"class_type":"LoraLoader","inputs":{"model":["ckpt",0],"clip":[cs,0],"lora_name":cfg["lora"],"strength_model":strength,"strength_clip":strength}}
    nodes[ld] = {"class_type":"LoraLoader","inputs":{"model":[lc,0],"clip":[lc,1],"lora_name":"penetration_depth.safetensors","strength_model":1.5,"strength_clip":1.0}}
    nodes[dp] = {"class_type":"LoraLoader","inputs":{"model":[ld,0],"clip":[ld,1],"lora_name":"doublepenetration_r1.safetensors","strength_model":1.0,"strength_clip":1.0}}
    nodes[ls] = {"class_type":"LoraLoader","inputs":{"model":[dp,0],"clip":[dp,1],"lora_name":"Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors","strength_model":0.5,"strength_clip":1.0}}
    nodes[ng] = {"class_type":"CLIPTextEncode","inputs":{"text":NEG + cfg.get("extra_neg",""),"clip":[ls,1]}}

    prompt = f"score_9, score_8_up, source_anime, rating_explicit, {cfg['char']}, {cfg['outfit']}, {MALE}, {DP}, {DEPTH}, {POSE}, {EXPR}, {LIGHT}, anime, masterpiece, best_quality"
    prompt = prompt.replace(", ,", ",").replace(",,", ",")
    nodes[f"p_{cname}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":[ls,1]}}
    nodes[f"k_{cname}"] = {"class_type":"KSampler","inputs":{"seed":cfg.get("seed",42424299),"steps":20,"cfg":3.5,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":[ls,0],"positive":[f"p_{cname}",0],"negative":[ng,0],"latent_image":["latent_shared",0]}}
    nodes[f"d_{cname}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{cname}",0],"vae":["ckpt",2]}}
    nodes[f"s_{cname}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"cucaracha_{cname}","images":[f"d_{cname}",0]}}

with open(os.path.join(B, "workflow_cucaracha.json"), "w", encoding="utf-8") as f:
    json.dump(nodes, f, indent=2, ensure_ascii=False)

n = sum(1 for v in nodes.values() if v.get("class_type")=="SaveImage")
print(f"✅ workflow_cucaracha.json → {n} imagenes (1 por personaje)")
