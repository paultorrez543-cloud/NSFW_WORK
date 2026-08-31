import json, os

B = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"

NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark, holding mirror, red mirror, mirror"

CHAR = "stell4virigiadef, 1girl, white hair, long hair, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, large breasts"
# Hombre feo/calvo (ugly bastard) — trigger del LoRA
UGLY = "1boy, faceless ugly man, ugly man, faceless_male, bald, mature male, fat, head_out_of_frame, penis"

CHRONOLOGY = [
    ("01_saludo",      "pov, looking_at_viewer, greeting, white dress, bedroom, smile"),
    ("02_coqueteo",    "pov, looking_at_viewer, flirting, white dress, bedroom, blush"),
    ("03_desnudando",  "pov, undressing, white dress, dress_lift, looking_at_viewer, nervous"),
    ("04_pecho",       "pov, white bra, skirt, clothes_lift, breast_touching, looking_at_viewer, moaning"),
    ("05_dedos",       "pov, white bra, white panties, fingering, wet, looking_at_viewer, aroused"),
    ("06_oral",        "pov, white bra, white panties, blowjob, looking_up_at_viewer, oral, deepthroat"),
    ("07_paizuri",     "pov, nude_top, white panties, titfuck, paizuri, between_breasts, looking_at_viewer"),
    ("08_desnuda",     "pov, nude, completely_nude, looking_at_viewer, shy, covering"),
    ("09_insercion",   "pov, nude, missionary_position, first_insertion, looking_at_viewer, (pain:1.3), (imminent penetration:1.2)"),
    ("10_estirando",   "pov, nude, stretching, screaming, looking_at_viewer, tip_in_pussy"),
    ("11_ritmo",       "pov, nude, thrusting, moaning, looking_at_viewer, (deep penetration:1.3), motion_lines"),
    ("12_cowgirl",     "pov, nude, cowgirl_position, girl_on_top, looking_at_viewer, riding, (deep penetration:1.4)"),
    ("13_reverse",     "pov, nude, reverse_cowgirl, facing_away, pov_crotch, ass_view, (deep penetration:1.4)"),
    ("14_doggystyle",  "pov, nude, doggystyle, from_behind, looking_back_at_viewer, (deep penetration:1.4)"),
    ("15_mating_press","pov, nude, mating_press, legs_above_head, folded, looking_at_viewer, (deep penetration:1.5)"),
    ("16_standing",    "pov, nude, standing_sex, lifted, looking_at_viewer, wall, (deep penetration:1.5)"),
    ("17_prone",       "pov, nude, prone_bone, lying, from_behind, deep"),
    ("18_anal",        "pov, nude, anal_sex, anal_penetration, looking_back_at_viewer"),
    ("19_full_nelson", "pov, nude, full_nelson, held_up, legs_spread, looking_at_viewer"),
    ("20_lotus",       "pov, nude, lotus_position, facing, hugging, looking_at_viewer"),
    ("21_cerca",       "pov, nude, deep_penetration, ahegao, looking_at_viewer, close_up, balls_deep"),
    ("22_creampie",    "pov, nude, creampie, cum_in_pussy, mind_break, looking_at_viewer, balls_deep"),
    ("23_cumdrip",     "pov, nude, cumdrip, cum_leaking, gaping, pov_crotch, close_up"),
    ("24_overflow",    "pov, nude, cum_overflow, excessive_cum, gaping, close_up"),
    ("25_creampie2",   "pov, nude, second_creampie, cum_in_pussy_again, cum_overflow, gaping"),
    ("26_anal_creampie","pov, nude, anal_creampie, cum_in_ass, gaping_anus, cumdrip"),
    ("27_ronda2",      "pov, nude, second_round, re-aroused, cowgirl_position, energetic"),
    ("28_ronda2_intensa","pov, nude, intense, rough_sex, ahegao, (deep penetration:1.5), motion_lines"),
    ("29_ronda2_climax","pov, nude, final_creampie, exhausted, cum_overflow, mind_break"),
    ("30_gaping",      "pov, nude, gaping, cum_pool, creampie_aftermath, close_up"),
    ("31_agotada",     "pov, nude, exhausted, tongue_out, looking_at_viewer, excessive_sweat"),
    ("32_bukake",      "pov, nude, bukkake, cum_covered, semen_on_face, semen_on_body, looking_at_viewer"),
    ("33_bukake_llena","pov, nude, cum_covered, excessive_cum, dripping, exhausted"),
    ("34_agotada_bukake","pov, nude, bukkake, cum_covered, semen_on_face, exhausted, sleeping"),
]

nodes = {}
nodes["ckpt"] = {"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":CKPT}}
nodes["latent_shared"] = {"class_type":"EmptyLatentImage","inputs":{"width":1024,"height":1536,"batch_size":1}}
nodes["clip_skip"] = {"class_type":"CLIPSetLastLayer","inputs":{"clip":["ckpt",1],"stop_at_clip_layer":-2}}
nodes["lora_char"] = {"class_type":"LoraLoader","inputs":{"model":["ckpt",0],"clip":["clip_skip",0],"lora_name":"Stella-Virigia-v1.safetensors","strength_model":1.0,"strength_clip":1.0}}
nodes["lora_ugly"] = {"class_type":"LoraLoader","inputs":{"model":["lora_char",0],"clip":["lora_char",1],"lora_name":"faceless-ugly-man-illustriousxl-lora-nochekaiser.safetensors","strength_model":1.0,"strength_clip":1.0}}
nodes["lora_depth"] = {"class_type":"LoraLoader","inputs":{"model":["lora_ugly",0],"clip":["lora_ugly",1],"lora_name":"penetration_depth.safetensors","strength_model":1.5,"strength_clip":1.0}}
nodes["lora_size"] = {"class_type":"LoraLoader","inputs":{"model":["lora_depth",0],"clip":["lora_depth",1],"lora_name":"Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors","strength_model":0.5,"strength_clip":1.0}}
nodes["neg"] = {"class_type":"CLIPTextEncode","inputs":{"text":NEG,"clip":["lora_size",1]}}

for n, tags in CHRONOLOGY:
    prompt = f"score_9, score_8_up, source_anime, rating_explicit, {CHAR}, {UGLY}, {tags}, {LIGHT}, anime, masterpiece, best_quality"
    prompt = prompt.replace(", ,", ",").replace(",,", ",")
    nodes[f"p_{n}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":["lora_size",1]}}
    nodes[f"k_{n}"] = {"class_type":"KSampler","inputs":{"seed":42424249,"steps":20,"cfg":3.5,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":["lora_size",0],"positive":[f"p_{n}",0],"negative":["neg",0],"latent_image":["latent_shared",0]}}
    nodes[f"d_{n}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{n}",0],"vae":["ckpt",2]}}
    nodes[f"s_{n}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"virigia_pov_ugly_{n}","images":[f"d_{n}",0]}}

with open(os.path.join(B, "workflow_virigia_pov_ugly.json"), "w", encoding="utf-8") as f:
    json.dump(nodes, f, indent=2, ensure_ascii=False)

n = sum(1 for v in nodes.values() if v.get("class_type")=="SaveImage")
print(f"✅ workflow_virigia_pov_ugly.json → {n} imagenes (POV + Creampie + Ugly Bastard)")
