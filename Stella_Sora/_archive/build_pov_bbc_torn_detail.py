import json, os

B = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"

NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark, holding mirror, red mirror, mirror"

CHAR = "stell4virigiadef, 1girl, white hair, long hair, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, large breasts"
BBC = "1boy, dark-skinned_male, tan-skinned_male, faceless_male, head_out_of_frame, tan_penis, huge_penis, size_difference"
OUTFIT = "white bonnet, white cloak, frilled cloak, black dress, detached collar, black bowtie, red ribbon, cleavage, black gloves, white pantyhose, high heels"

# Cronología mejorada con todos los detalles (sin los 7 excluidos)
CHRONOLOGY = [
    ("01_saludo",      "pov, looking_at_viewer, greeting, bedroom, smile"),
    ("02_coqueteo",    "pov, looking_at_viewer, flirting, bedroom, blush"),
    ("03_acercandose", "pov, looking_at_viewer, nervous, bedroom, leaning, glistening"),

    ("04_pecho",       "pov, clothes_lift, breast_touching, looking_at_viewer, moaning, close_up, glistening, precum"),
    ("05_dedos",       "pov, skirt_lift, fingering, panties_aside, looking_at_viewer, aroused, close_up, precum_dripping"),
    ("06_oral",        "pov, blowjob, looking_up_at_viewer, oral, deepthroat, saliva_string, drooling, close_up"),
    ("07_desgarro",    "pov, torn_clothes, ripping, dress_tearing, looking_at_viewer, surprised, motion_lines"),

    ("08_rasgada",     "pov, torn_clothes, torn_dress, exposed_breasts, looking_at_viewer, shy, glistening"),
    ("09_insercion",   "pov, torn_clothes, missionary_position, first_insertion, looking_at_viewer, (pain:1.3), (imminent penetration:1.2), veins, throbbing, stomach_bulge"),
    ("10_estirando",   "pov, torn_clothes, stretching, screaming, looking_at_viewer, tip_in_pussy, veins, stomach_bulge, tears_streaming"),
    ("11_ritmo",       "pov, torn_clothes, thrusting, moaning, looking_at_viewer, (deep penetration:1.3), motion_lines, glistening, sound_effects"),

    ("12_cowgirl",     "pov, torn_clothes, cowgirl_position, girl_on_top, exposed_breasts, looking_at_viewer, riding, (deep penetration:1.4), stomach_bulge, heart_pupils, motion_lines"),
    ("13_reverse",     "pov, torn_clothes, reverse_cowgirl, facing_away, torn_skirt, pov_crotch, ass_view, (deep penetration:1.4), dutch_angle, impact_lines"),
    ("14_doggystyle",  "pov, torn_clothes, doggystyle, from_behind, torn_dress, looking_back_at_viewer, (deep penetration:1.4), impact_lines, sound_effects"),
    ("15_mating_press","pov, torn_clothes, mating_press, legs_above_head, folded, looking_at_viewer, (deep penetration:1.5), stomach_bulge, ahegao, motion_lines"),
    ("16_standing",    "pov, torn_clothes, standing_sex, lifted, torn_dress, looking_at_viewer, wall, (deep penetration:1.5), motion_lines, steam"),
    ("17_prone",       "pov, torn_clothes, prone_bone, lying, from_behind, deep, impact_lines"),
    ("18_anal",        "pov, torn_clothes, anal_sex, anal_penetration, looking_back_at_viewer, gaping_anus, close_up"),
    ("19_full_nelson", "pov, torn_clothes, full_nelson, held_up, legs_spread, looking_at_viewer, ahegao, motion_lines"),
    ("20_lotus",       "pov, torn_clothes, lotus_position, facing, hugging, looking_at_viewer, dutch_angle"),

    ("21_cerca",       "pov, tattered_clothes, deep_penetration, ahegao, looking_at_viewer, extreme_close_up, balls_deep, stomach_bulge, veins, throbbing"),
    ("22_creampie",    "pov, tattered_clothes, creampie, cum_in_pussy, mind_break, looking_at_viewer, balls_deep, heart_pupils, blank_eyes"),
    ("23_cumdrip",     "pov, tattered_clothes, cumdrip, cum_leaking, gaping, pov_crotch, close_up, gaping_pussy"),
    ("24_overflow",    "pov, tattered_clothes, cum_overflow, excessive_cum, cum_on_clothes, close_up, gaping_pussy, squirting"),
    ("25_creampie2",   "pov, tattered_clothes, second_creampie, cum_overflow, gaping, female_ejaculation, squirting"),
    ("26_anal_creampie","pov, tattered_clothes, anal_creampie, cum_in_ass, gaping_anus, cumdrip"),

    ("27_ronda2",      "pov, ripped_clothes, second_round, re-aroused, cowgirl_position, energetic, lactation, breast_milk"),
    ("28_ronda2_intensa","pov, ripped_clothes, intense, rough_sex, ahegao, (deep penetration:1.5), motion_lines, impact_lines, saliva_string, steam"),
    ("29_ronda2_climax","pov, ripped_clothes, final_creampie, exhausted, cum_on_clothes, mind_break, squirting"),

    ("30_gaping",      "pov, ruined_clothes, gaping, cum_pool, creampie_aftermath, close_up, gaping_pussy"),
    ("31_agotada",     "pov, ruined_clothes, exhausted, tongue_out, long_tongue, looking_at_viewer, disheveled, dried_tears, body_writing"),
    ("32_bukake",      "pov, ruined_clothes, bukkake, cum_covered, semen_on_face, semen_on_clothes, looking_at_viewer, body_writing"),
    ("33_bukake_llena","pov, ruined_clothes, cum_covered, excessive_cum, dripping, exhausted, painted_on_text"),
    ("34_agotada_bukake","pov, ruined_clothes, bukkake, cum_covered, semen_on_face, exhausted, sleeping, dried_tears, body_writing"),
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
    prompt = f"score_9, score_8_up, source_anime, rating_explicit, {CHAR}, {OUTFIT}, {BBC}, interracial, {tags}, {LIGHT}, anime, masterpiece, best_quality"
    prompt = prompt.replace(", ,", ",").replace(",,", ",")
    nodes[f"p_{n}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":["lora_size",1]}}
    nodes[f"k_{n}"] = {"class_type":"KSampler","inputs":{"seed":42424249,"steps":20,"cfg":3.5,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":["lora_size",0],"positive":[f"p_{n}",0],"negative":["neg",0],"latent_image":["latent_shared",0]}}
    nodes[f"d_{n}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{n}",0],"vae":["ckpt",2]}}
    nodes[f"s_{n}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"virigia_pov_bbc_torn_detail_{n}","images":[f"d_{n}",0]}}

with open(os.path.join(B, "workflow_virigia_pov_bbc_torn_detail.json"), "w", encoding="utf-8") as f:
    json.dump(nodes, f, indent=2, ensure_ascii=False)

n = sum(1 for v in nodes.values() if v.get("class_type")=="SaveImage")
print(f"✅ workflow_virigia_pov_bbc_torn_detail.json → {n} imagenes (todos los detalles)")
