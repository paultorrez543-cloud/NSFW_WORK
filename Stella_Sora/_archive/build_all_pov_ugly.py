import json, os, re

B = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"

NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark, holding mirror, red mirror, mirror"

# Hombre feo/calvo (ugly bastard)
UGLY = "1boy, faceless ugly man, ugly man, faceless_male, bald, mature male, fat, head_out_of_frame, penis"

# Cronología: intro (outfit del personaje) → foreplay (white bra) → nude
CHRONOLOGY = [
    ("01_saludo",      "pov, looking_at_viewer, greeting, bedroom, smile", "outfit"),
    ("02_coqueteo",    "pov, looking_at_viewer, flirting, bedroom, blush", "outfit"),
    ("03_acercandose", "pov, looking_at_viewer, nervous, bedroom, leaning", "outfit"),
    ("04_pecho",       "pov, white bra, skirt, clothes_lift, breast_touching, looking_at_viewer, moaning", ""),
    ("05_dedos",       "pov, white bra, white panties, fingering, wet, looking_at_viewer, aroused", ""),
    ("06_oral",        "pov, white bra, white panties, blowjob, looking_up_at_viewer, oral, deepthroat", ""),
    ("07_paizuri",     "pov, nude_top, white panties, titfuck, paizuri, between_breasts, looking_at_viewer", ""),
    ("08_desnuda",     "pov, nude, completely_nude, looking_at_viewer, shy, covering", ""),
    ("09_insercion",   "pov, nude, missionary_position, first_insertion, looking_at_viewer, (pain:1.3), (imminent penetration:1.2)", ""),
    ("10_estirando",   "pov, nude, stretching, screaming, looking_at_viewer, tip_in_pussy", ""),
    ("11_ritmo",       "pov, nude, thrusting, moaning, looking_at_viewer, (deep penetration:1.3), motion_lines", ""),
    ("12_cowgirl",     "pov, nude, cowgirl_position, girl_on_top, looking_at_viewer, riding, (deep penetration:1.4)", ""),
    ("13_reverse",     "pov, nude, reverse_cowgirl, facing_away, pov_crotch, ass_view, (deep penetration:1.4)", ""),
    ("14_doggystyle",  "pov, nude, doggystyle, from_behind, looking_back_at_viewer, (deep penetration:1.4)", ""),
    ("15_mating_press","pov, nude, mating_press, legs_above_head, folded, looking_at_viewer, (deep penetration:1.5)", ""),
    ("16_standing",    "pov, nude, standing_sex, lifted, looking_at_viewer, wall, (deep penetration:1.5)", ""),
    ("17_prone",       "pov, nude, prone_bone, lying, from_behind, deep", ""),
    ("18_anal",        "pov, nude, anal_sex, anal_penetration, looking_back_at_viewer", ""),
    ("19_full_nelson", "pov, nude, full_nelson, held_up, legs_spread, looking_at_viewer", ""),
    ("20_lotus",       "pov, nude, lotus_position, facing, hugging, looking_at_viewer", ""),
    ("21_cerca",       "pov, nude, deep_penetration, ahegao, looking_at_viewer, close_up, balls_deep", ""),
    ("22_creampie",    "pov, nude, creampie, cum_in_pussy, mind_break, looking_at_viewer, balls_deep", ""),
    ("23_cumdrip",     "pov, nude, cumdrip, cum_leaking, gaping, pov_crotch, close_up", ""),
    ("24_overflow",    "pov, nude, cum_overflow, excessive_cum, gaping, close_up", ""),
    ("25_creampie2",   "pov, nude, second_creampie, cum_in_pussy_again, cum_overflow, gaping", ""),
    ("26_anal_creampie","pov, nude, anal_creampie, cum_in_ass, gaping_anus, cumdrip", ""),
    ("27_ronda2",      "pov, nude, second_round, re-aroused, cowgirl_position, energetic", ""),
    ("28_ronda2_intensa","pov, nude, intense, rough_sex, ahegao, (deep penetration:1.5), motion_lines", ""),
    ("29_ronda2_climax","pov, nude, final_creampie, exhausted, cum_overflow, mind_break", ""),
    ("30_gaping",      "pov, nude, gaping, cum_pool, creampie_aftermath, close_up", ""),
    ("31_agotada",     "pov, nude, exhausted, tongue_out, looking_at_viewer, excessive_sweat", ""),
    ("32_bukake",      "pov, nude, bukkake, cum_covered, semen_on_face, semen_on_body, looking_at_viewer", ""),
    ("33_bukake_llena","pov, nude, cum_covered, excessive_cum, dripping, exhausted", ""),
    ("34_agotada_bukake","pov, nude, bukkake, cum_covered, semen_on_face, exhausted, sleeping", ""),
]

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

outdir = os.path.join(B, "pov_ugly")
os.makedirs(outdir, exist_ok=True)

for cname, cfg in roster.items():
    nodes = {}
    nodes["ckpt"] = {"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":CKPT}}
    nodes["latent_shared"] = {"class_type":"EmptyLatentImage","inputs":{"width":1024,"height":1536,"batch_size":1}}
    nodes["clip_skip"] = {"class_type":"CLIPSetLastLayer","inputs":{"clip":["ckpt",1],"stop_at_clip_layer":-2}}
    strength = cfg.get("strength", 1.0)
    nodes["lora_char"] = {"class_type":"LoraLoader","inputs":{"model":["ckpt",0],"clip":["clip_skip",0],"lora_name":cfg["lora"],"strength_model":strength,"strength_clip":strength}}
    nodes["lora_ugly"] = {"class_type":"LoraLoader","inputs":{"model":["lora_char",0],"clip":["lora_char",1],"lora_name":"faceless-ugly-man-illustriousxl-lora-nochekaiser.safetensors","strength_model":1.0,"strength_clip":1.0}}
    nodes["lora_depth"] = {"class_type":"LoraLoader","inputs":{"model":["lora_ugly",0],"clip":["lora_ugly",1],"lora_name":"penetration_depth.safetensors","strength_model":1.5,"strength_clip":1.0}}
    nodes["lora_size"] = {"class_type":"LoraLoader","inputs":{"model":["lora_depth",0],"clip":["lora_depth",1],"lora_name":"Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors","strength_model":0.5,"strength_clip":1.0}}
    nodes["neg"] = {"class_type":"CLIPTextEncode","inputs":{"text":NEG + cfg.get("extra_neg",""),"clip":["lora_size",1]}}

    for n, tags, mode in CHRONOLOGY:
        if mode == "outfit":
            parts = ["score_9, score_8_up, source_anime, rating_explicit", cfg["char"], cfg["outfit"], UGLY, tags, LIGHT, "anime, masterpiece, best_quality"]
        else:
            parts = ["score_9, score_8_up, source_anime, rating_explicit", cfg["char"], UGLY, tags, LIGHT, "anime, masterpiece, best_quality"]
        prompt = ", ".join([p for p in parts if p]).replace(", ,", ",").replace(",,", ",")
        nodes[f"p_{n}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":["lora_size",1]}}
        nodes[f"k_{n}"] = {"class_type":"KSampler","inputs":{"seed":cfg.get("seed",42424299),"steps":20,"cfg":3.5,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":["lora_size",0],"positive":[f"p_{n}",0],"negative":["neg",0],"latent_image":["latent_shared",0]}}
        nodes[f"d_{n}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{n}",0],"vae":["ckpt",2]}}
        nodes[f"s_{n}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"pov_ugly_{cname}_{n}","images":[f"d_{n}",0]}}

    with open(os.path.join(outdir, f"workflow_{cname}.json"), "w", encoding="utf-8") as f:
        json.dump(nodes, f, indent=2, ensure_ascii=False)

print(f"✅ {len(roster)} workflows generados en pov_ugly/ (34 img c/u)")
