import json, os

B = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"

NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark, holding mirror, red mirror, mirror"

CHAR = "stell4virigiadef, 1girl, white hair, long hair, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, large breasts"
BBC = "1boy, dark-skinned_male, tan-skinned_male, faceless_male, head_out_of_frame, tan_penis, huge_penis, size_difference"
# Outfit FIJO (se mantiene vestida en todas las imágenes)
OUTFIT = "white bonnet, white cloak, frilled cloak, black dress, detached collar, black bowtie, red ribbon, cleavage, black gloves, white pantyhose, high heels"
CLOTHED = "clothed_sex, clothes_lift, skirt_lift, clothing_aside"

CHRONOLOGY = [
    ("01_saludo",      "pov, looking_at_viewer, greeting, bedroom, smile"),
    ("02_coqueteo",    "pov, looking_at_viewer, flirting, bedroom, blush"),
    ("03_acercandose", "pov, looking_at_viewer, nervous, bedroom, leaning"),

    ("04_pecho",       "pov, clothes_lift, breast_touching, looking_at_viewer, moaning"),
    ("05_dedos",       "pov, skirt_lift, fingering, panties_aside, looking_at_viewer, aroused"),
    ("06_oral",        "pov, blowjob, looking_up_at_viewer, oral, deepthroat, clothed"),
    ("07_paizuri",     "pov, titfuck, paizuri, breasts_outside_clothes, between_breasts, looking_at_viewer"),

    ("08_expuesta",    "pov, clothes_lift, breasts_outside_clothes, looking_at_viewer, shy"),
    ("09_insercion",   "pov, skirt_lift, missionary_position, first_insertion, looking_at_viewer, (pain:1.3), (imminent penetration:1.2)"),
    ("10_estirando",   "pov, skirt_lift, stretching, screaming, looking_at_viewer, tip_in_pussy"),
    ("11_ritmo",       "pov, skirt_lift, thrusting, moaning, looking_at_viewer, (deep penetration:1.3), motion_lines"),

    ("12_cowgirl",     "pov, cowgirl_position, girl_on_top, skirt_lift, looking_at_viewer, riding, (deep penetration:1.4)"),
    ("13_reverse",     "pov, reverse_cowgirl, facing_away, skirt_lift, pov_crotch, ass_view, (deep penetration:1.4)"),
    ("14_doggystyle",  "pov, doggystyle, from_behind, skirt_lift, looking_back_at_viewer, (deep penetration:1.4)"),
    ("15_mating_press","pov, mating_press, legs_above_head, skirt_lift, folded, looking_at_viewer, (deep penetration:1.5)"),
    ("16_standing",    "pov, standing_sex, lifted, skirt_lift, looking_at_viewer, wall, (deep penetration:1.5)"),
    ("17_prone",       "pov, prone_bone, lying, skirt_lift, from_behind, deep"),
    ("18_anal",        "pov, anal_sex, anal_penetration, skirt_lift, looking_back_at_viewer"),
    ("19_full_nelson", "pov, full_nelson, held_up, skirt_lift, legs_spread, looking_at_viewer"),
    ("20_lotus",       "pov, lotus_position, facing, skirt_lift, hugging, looking_at_viewer"),

    ("21_cerca",       "pov, deep_penetration, ahegao, looking_at_viewer, close_up, balls_deep"),
    ("22_creampie",    "pov, creampie, cum_in_pussy, mind_break, looking_at_viewer, balls_deep"),
    ("23_cumdrip",     "pov, cumdrip, cum_leaking, gaping, pov_crotch, close_up"),
    ("24_overflow",    "pov, cum_overflow, excessive_cum, cum_on_clothes, close_up"),
    ("25_creampie2",   "pov, second_creampie, cum_overflow, cum_on_skirt, gaping"),
    ("26_anal_creampie","pov, anal_creampie, cum_in_ass, gaping_anus, cumdrip"),

    ("27_ronda2",      "pov, second_round, re-aroused, cowgirl_position, skirt_lift, energetic"),
    ("28_ronda2_intensa","pov, intense, rough_sex, ahegao, skirt_lift, (deep penetration:1.5), motion_lines"),
    ("29_ronda2_climax","pov, final_creampie, exhausted, cum_on_clothes, mind_break"),

    ("30_gaping",      "pov, gaping, cum_pool, creampie_aftermath, close_up"),
    ("31_agotada",     "pov, exhausted, tongue_out, looking_at_viewer, disheveled, cum_stained_clothes"),
    ("32_bukake",      "pov, bukkake, cum_covered, semen_on_face, semen_on_clothes, looking_at_viewer"),
    ("33_bukake_llena","pov, cum_covered, excessive_cum, dripping, cum_stained_clothes, exhausted"),
    ("34_agotada_bukake","pov, bukkake, cum_covered, semen_on_face, ruined_clothes, exhausted, sleeping"),
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
    prompt = f"score_9, score_8_up, source_anime, rating_explicit, {CHAR}, {OUTFIT}, {BBC}, interracial, {CLOTHED}, {tags}, {LIGHT}, anime, masterpiece, best_quality"
    prompt = prompt.replace(", ,", ",").replace(",,", ",")
    nodes[f"p_{n}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":["lora_size",1]}}
    nodes[f"k_{n}"] = {"class_type":"KSampler","inputs":{"seed":42424249,"steps":20,"cfg":3.5,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":["lora_size",0],"positive":[f"p_{n}",0],"negative":["neg",0],"latent_image":["latent_shared",0]}}
    nodes[f"d_{n}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{n}",0],"vae":["ckpt",2]}}
    nodes[f"s_{n}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"virigia_pov_bbc_clothed_{n}","images":[f"d_{n}",0]}}

with open(os.path.join(B, "workflow_virigia_pov_bbc_clothed.json"), "w", encoding="utf-8") as f:
    json.dump(nodes, f, indent=2, ensure_ascii=False)

n = sum(1 for v in nodes.values() if v.get("class_type")=="SaveImage")
print(f"✅ workflow_virigia_pov_bbc_clothed.json → {n} imagenes (POV + Creampie + BBC + CLOTHED)")
