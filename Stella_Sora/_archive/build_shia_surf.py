import json, os

B = "E:/ComfyUI/characters/Stella_Sora/shia"
CKPT = "waiIllustriousSDXL_v170.safetensors"
SEED = 42424252

CHAR = "shia, stella sora, 1girl"
OUTFIT = "bunny girl, bunny ears, sailor collar, bikini, covered midriff"
NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark"

# Surf: iluminacion natural de playa (no dark room)
ENV = "beach, ocean, waves, sky, clouds"

STAGES = [
    {"n":"01_llegada",      "pose":"standing, looking at viewer, full body", "board":"holding surfboard", "expr":"smile, happy, blush", "env":"beach, sand, sunny, blue sky", "extra":"surfing, surfboard, bikini"},
    {"n":"02_caminata",     "pose":"walking, from_behind, full body", "board":"holding surfboard, surfboard_under_arm", "expr":"looking_back, smile", "env":"beach, shoreline, wet sand, ocean, waves", "extra":"surfing, surfboard, footprints"},
    {"n":"03_entrando",     "pose":"walking, in_water, depth_of_field", "board":"holding surfboard", "expr":"smile, excited", "env":"ocean, shallow_water, waves, splashing", "extra":"surfing, surfboard, water_splash"},
    {"n":"04_remando",      "pose":"lying, on_surfboard, paddling, from_above", "board":"surfboard, lying_on_surfboard", "expr":"focused, determined", "env":"ocean, deep_water, waves, foam", "extra":"surfing, surfboard, paddling"},
    {"n":"05_esperando",    "pose":"sitting, on_surfboard, side_view", "board":"sitting_on_surfboard", "expr":"relaxed, looking_at_horizon, smile", "env":"ocean, calm_sea, horizon, sunset_glow", "extra":"surfing, surfboard, waiting_for_wave"},
    {"n":"06_ola",          "pose":"standing, on_surfboard, dynamic_pose, arms_out", "board":"surfboard, standing_on_surfboard", "expr":"excited, open_mouth, smile", "env":"ocean, big_wave, riding_wave, water_splash, motion_lines", "extra":"surfing, surfboard, riding_wave"},
    {"n":"07_maniobra",     "pose":"surfing_trick, crouching, one_arm_back, dynamic", "board":"surfboard, surfing", "expr":"concentrated, biting_lip", "env":"ocean, wave_crest, water_spray, speed_lines", "extra":"surfing, surfboard, trick, carve"},
    {"n":"08_caida",        "pose":"falling, in_air, splash, from_side", "board":"surfboard, flying_surfboard", "expr":"surprised, wide_eyes, open_mouth", "env":"ocean, water_splash, wave, foam", "extra":"surfing, surfboard, wipeout, splash"},
    {"n":"09_emergiendo",   "pose":"emerging_from_water, half_body, close-up", "board":"surfboard, floating_surfboard", "expr":"laughing, smile, wet_hair", "env":"ocean, water_surface, wet, dripping", "extra":"surfing, surfboard, wet, water_droplets"},
    {"n":"10_descanso",     "pose":"sitting, on_surfboard, on_shore, sunset", "board":"sitting_on_surfboard", "expr":"satisfied, relaxed, gentle_smile, blush", "env":"beach, sunset, golden_hour, warm_light, orange_sky", "extra":"surfing, surfboard, sunset, golden_hour"},
]

nodes = {}
nodes["ckpt"] = {"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":CKPT}}
nodes["clip_skip"] = {"class_type":"CLIPSetLastLayer","inputs":{"clip":["ckpt",1],"stop_at_clip_layer":-2}}
nodes["lora_char"] = {"class_type":"LoraLoader","inputs":{"model":["ckpt",0],"clip":["clip_skip",0],"lora_name":"Shia_Stella_Sora__シア_ステラソラ.safetensors","strength_model":1.0,"strength_clip":1.0}}
nodes["neg"] = {"class_type":"CLIPTextEncode","inputs":{"text":NEG,"clip":["lora_char",1]}}
nodes["latent_shared"] = {"class_type":"EmptyLatentImage","inputs":{"width":1216,"height":832,"batch_size":1}}

for s in STAGES:
    prompt = f"score_9, score_8_up, source_anime, rating_safe, {CHAR}, {OUTFIT}, {s['pose']}, {s['board']}, {s['expr']}, {s['env']}, {s['extra']}, anime, masterpiece, best_quality"
    prompt = prompt.replace(", ,", ",").replace(",,", ",")
    sn = s["n"]
    nodes[f"p_{sn}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":["lora_char",1]}}
    nodes[f"k_{sn}"] = {"class_type":"KSampler","inputs":{"seed":SEED,"steps":20,"cfg":3.5,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":["lora_char",0],"positive":[f"p_{sn}",0],"negative":["neg",0],"latent_image":["latent_shared",0]}}
    nodes[f"d_{sn}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{sn}",0],"vae":["ckpt",2]}}
    nodes[f"s_{sn}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"shia_surf_{sn}","images":[f"d_{sn}",0]}}

with open(os.path.join(B, "workflow_surf.json"), "w", encoding="utf-8") as f:
    json.dump(nodes, f, indent=2, ensure_ascii=False)

n = sum(1 for v in nodes.values() if v.get("class_type")=="SaveImage")
print(f"✅ shia/workflow_surf.json → {n} etapas")
print(f"   {len(nodes)} nodos | surf theme | rating_safe")
