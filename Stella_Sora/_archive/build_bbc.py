import json, os

B = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"

NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark, holding mirror, red mirror, mirror"

CHAR = "stell4virigiadef, 1girl, white hair, long hair, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, large breasts"
# Hombre BBC (negro, sin cara, pene enorme)
BBC = "1boy, dark-skinned_male, tan-skinned_male, faceless_male, head_out_of_frame, tan_penis, huge_penis, large_penis, size_difference"

CHRONOLOGY = [
    # Fase 1: Encuentro
    ("01_encuentro",  "first_meeting, eye_contact, nervous, standing, white dress, outdoors, daylight"),
    ("02_atraccion",  "attraction, staring, blush, size_difference, white dress, outdoors"),
    ("03_acercamiento","flirting, leaning_closer, curious, white dress, outdoors"),

    # Fase 2: Atracción física
    ("04_tocando",    "touching, muscular, dark-skinned_male, blushing, white dress, indoors"),
    ("05_primer_beso","first_kiss, interracial, embracing, closed_eyes, indoors, romantic"),
    ("06_viendo",     "undressing, seeing_penis, shocked, huge_penis, nervous, bedroom"),

    # Fase 3: Primera intimidad
    ("07_caricias",   "groping, black_penis, nervous, skin_contact, bedroom, dim_lighting"),
    ("08_oral",       "blowjob, oral, huge_penis, kneeling, on_knees, bedroom"),
    ("09_comparando", "about_to_penetrate, size_comparison, scared, huge_penis, bedroom"),

    # Fase 4: Primera vez
    ("10_primera_vez","first_time, interracial_sex, (pain:1.3), missionary_position, nude, bed, (imminent penetration:1.2)"),
    ("11_estirando",  "stretching, huge_penis, screaming, tears_streaming, nude, bed, tip_in_pussy"),
    ("12_adaptando",  "adjusting, pleasure, moaning, nude, bed, (deep penetration:1.3)"),

    # Fase 5: Adaptación
    ("13_cowgirl",    "cowgirl_position, girl_on_top, riding, black_penis, confident, nude, bed, (deep penetration:1.4)"),
    ("14_doggystyle", "doggystyle, from_behind, deep, moaning, interracial, nude, bed, (deep penetration:1.4)"),
    ("15_mating",     "mating_press, legs_above_head, deep_penetration, ahegao, nude, bed, (deep penetration:1.5)"),

    # Fase 6: Adicción
    ("16_adicta",     "addicted, begging, desperate, black_penis, nude, bed, (deep penetration:1.5)"),
    ("17_obsesion",   "obsessed, interracial, passionate, creampie, nude, bed, balls_deep"),
    ("18_ansia",      "craving, daily_sex, eager, nude, bed, after_sex"),

    # Fase 7: Intensidad
    ("19_pasional",   "rough_sex, intense, ahegao, size_difference, nude, bed, balls_deep, (motion lines:1.4)"),
    ("20_creampie",   "mind_break, creampie, excessive_cum, heart_pupils, nude, bed, balls_deep, (motion lines:1.5)"),
    ("21_agotada",    "orgasm, exhausted, gaping, cum_overflow, nude, bed, after_sex"),

    # Fase 8: Consagración
    ("22_compromiso","committed, interracial_relationship, loving, gentle_sex, nude, bed, missionary_position"),
    ("23_manana",    "morning_after, cuddling, disheveled, satisfied, nude, bed, sunlight"),
    ("24_embarazada","pregnant, belly, family, interracial, nude, bed, peaceful"),
]

nodes = {}
nodes["ckpt"] = {"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":CKPT}}
nodes["latent_shared"] = {"class_type":"EmptyLatentImage","inputs":{"width":1024,"height":1536,"batch_size":1}}
nodes["clip_skip"] = {"class_type":"CLIPSetLastLayer","inputs":{"clip":["ckpt",1],"stop_at_clip_layer":-2}}
nodes["lora_char"] = {"class_type":"LoraLoader","inputs":{"model":["ckpt",0],"clip":["clip_skip",0],"lora_name":"Stella-Virigia-v1.safetensors","strength_model":1.0,"strength_clip":1.0}}
nodes["lora_depth"] = {"class_type":"LoraLoader","inputs":{"model":["lora_char",0],"clip":["lora_char",1],"lora_name":"penetration_depth.safetensors","strength_model":1.5,"strength_clip":1.0}}
nodes["lora_size"] = {"class_type":"LoraLoader","inputs":{"model":["lora_depth",0],"clip":["lora_depth",1],"lora_name":"Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors","strength_model":2.0,"strength_clip":1.0}}
nodes["neg"] = {"class_type":"CLIPTextEncode","inputs":{"text":NEG,"clip":["lora_size",1]}}

for n, tags in CHRONOLOGY:
    prompt = f"score_9, score_8_up, source_anime, rating_explicit, {CHAR}, {BBC}, interracial, {tags}, {LIGHT}, anime, masterpiece, best_quality"
    prompt = prompt.replace(", ,", ",").replace(",,", ",")
    nodes[f"p_{n}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":["lora_size",1]}}
    nodes[f"k_{n}"] = {"class_type":"KSampler","inputs":{"seed":42424249,"steps":20,"cfg":3.5,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":["lora_size",0],"positive":[f"p_{n}",0],"negative":["neg",0],"latent_image":["latent_shared",0]}}
    nodes[f"d_{n}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{n}",0],"vae":["ckpt",2]}}
    nodes[f"s_{n}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"virigia_bbc_{n}","images":[f"d_{n}",0]}}

with open(os.path.join(B, "workflow_virigia_bbc.json"), "w", encoding="utf-8") as f:
    json.dump(nodes, f, indent=2, ensure_ascii=False)

n = sum(1 for v in nodes.values() if v.get("class_type")=="SaveImage")
print(f"✅ workflow_virigia_bbc.json → {n} imagenes (8 fases x 3, BBC)")
