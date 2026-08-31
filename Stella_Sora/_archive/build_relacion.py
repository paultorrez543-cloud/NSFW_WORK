import json, os

B = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"

NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark, holding mirror, red mirror, mirror"

CHAR = "stell4virigiadef, 1girl, white hair, long hair, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, large breasts"

# Cronología de desarrollo de relación sexual — 8 fases × 3 imágenes
# Cada etapa: (nombre, tags de prompt completos)
CHRONOLOGY = [
    # ── Fase 1: Encuentro (exterior, vestida) ──
    ("01_encuentro",  "first_meeting, eye_contact, blush, shy, standing, white dress, outdoors, daylight"),
    ("02_coqueteo",   "flirting, smiling, leaning_closer, blush, white dress, outdoors, wind"),
    ("03_caminata",   "holding_hands, walking_together, nervous, white dress, outdoors, sunset"),

    # ── Fase 2: Acercamiento (interior) ──
    ("04_cita",       "date, restaurant, talking, smiling, white dress, indoors, warm_lighting"),
    ("05_cercania",   "arm_around_shoulder, leaning, blush, white dress, indoors, couch"),
    ("06_primer_beso","first_kiss, embracing, closed_eyes, blush, white dress, indoors, romantic"),

    # ── Fase 3: Primera intimidad ──
    ("07_besos",      "kissing, groping, clothes_shift, blush, black dress, bedroom, dim_lighting"),
    ("08_desnudando", "undressing, shirt_lift, skin_contact, nervous, exposed_shoulders, bedroom"),
    ("09_expuesta",   "nude, covering_self, shy, exposed, breasts, bedroom"),

    # ── Fase 4: Primera relación sexual ──
    ("10_primera_vez","first_time, missionary_position, gentle, nervous, nude, bed, (imminent penetration:1.2)"),
    ("11_dolor",      "defloration, (pain:1.3), tears_streaming, clinging, nude, bed, tip_in_pussy"),
    ("12_primer_orgasmo", "first_orgasm, moaning, pleasure, hugging, nude, bed, (deep penetration:1.3)"),

    # ── Fase 5: Consolidación / Rutina ──
    ("13_cowgirl",    "cowgirl_position, girl_on_top, confident, nude, bed, (deep penetration:1.4)"),
    ("14_doggystyle", "doggystyle, from_behind, mutual_pleasure, moaning, nude, bed, (deep penetration:1.4)"),
    ("15_juguetona",  "riding, playful, smiling, sweat, nude, bed, (deep penetration:1.5)"),

    # ── Fase 6: Exploración / Kinks ──
    ("16_atada",      "bondage, tied_up, blindfold, excited, nude, bed, ropes"),
    ("17_juguetes",   "sex_toy, vibrator, masturbation, aroused, nude, bed"),
    ("18_rol",        "roleplay, costume, submissive, collar, nude, bed"),

    # ── Fase 7: Intensificación / Pasión ──
    ("19_pasional",   "passionate, rough_sex, intense, ahegao, nude, bed, (deep penetration:1.5), balls_deep, (motion lines:1.4)"),
    ("20_creampie",   "creampie, mind_break, heart_pupils, excessive_sweat, nude, bed, balls_deep, (motion lines:1.5)"),
    ("21_agotada",    "orgasm, exhausted, excessive_sweat, tongue_out, nude, bed, after_sex"),

    # ── Fase 8: Compromiso / Estabilidad ──
    ("22_casados",    "wedding_ring, married, loving, gentle_sex, nude, bed, missionary_position"),
    ("23_manana",     "morning_after, domestic, cuddling, disheveled, nude, bed, sunlight"),
    ("24_dormidos",   "afterglow, embracing, satisfied, sleeping, nude, bed, peaceful"),
]

nodes = {}
nodes["ckpt"] = {"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":CKPT}}
nodes["latent_shared"] = {"class_type":"EmptyLatentImage","inputs":{"width":1024,"height":1536,"batch_size":1}}
nodes["clip_skip"] = {"class_type":"CLIPSetLastLayer","inputs":{"clip":["ckpt",1],"stop_at_clip_layer":-2}}
nodes["lora_char"] = {"class_type":"LoraLoader","inputs":{"model":["ckpt",0],"clip":["clip_skip",0],"lora_name":"Stella-Virigia-v1.safetensors","strength_model":1.0,"strength_clip":1.0}}
nodes["lora_depth"] = {"class_type":"LoraLoader","inputs":{"model":["lora_char",0],"clip":["lora_char",1],"lora_name":"penetration_depth.safetensors","strength_model":1.5,"strength_clip":1.0}}
nodes["lora_size"] = {"class_type":"LoraLoader","inputs":{"model":["lora_depth",0],"clip":["lora_depth",1],"lora_name":"Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors","strength_model":0.5,"strength_clip":1.0}}
nodes["neg"] = {"class_type":"CLIPTextEncode","inputs":{"text":NEG,"clip":["lora_size",1]}}

for n, tags in CHRONOLOGY:
    prompt = f"score_9, score_8_up, source_anime, rating_explicit, {CHAR}, {tags}, {LIGHT}, anime, masterpiece, best_quality"
    prompt = prompt.replace(", ,", ",").replace(",,", ",")
    nodes[f"p_{n}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":["lora_size",1]}}
    nodes[f"k_{n}"] = {"class_type":"KSampler","inputs":{"seed":42424249,"steps":20,"cfg":3.5,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":["lora_size",0],"positive":[f"p_{n}",0],"negative":["neg",0],"latent_image":["latent_shared",0]}}
    nodes[f"d_{n}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{n}",0],"vae":["ckpt",2]}}
    nodes[f"s_{n}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"virigia_relacion_{n}","images":[f"d_{n}",0]}}

with open(os.path.join(B, "workflow_virigia_relacion.json"), "w", encoding="utf-8") as f:
    json.dump(nodes, f, indent=2, ensure_ascii=False)

n = sum(1 for v in nodes.values() if v.get("class_type")=="SaveImage")
print(f"✅ workflow_virigia_relacion.json → {n} imagenes (8 fases x 3)")
