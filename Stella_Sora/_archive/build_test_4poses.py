import json, os

B = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"
EXPR = "rolled_back_eyes, tongue_out, drooling, ahegao"
DEPTH = "(deep penetration:1.4), full_penetration"

NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark"

CHAR = "stell4virigiadef, 1girl, white hair, long hair, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, large breasts"
OUTFIT = "white bonnet, white cloak, frilled cloak, black dress, detached collar, black bowtie, red ribbon, cleavage, black gloves, white pantyhose, high heels, clothes_lift"
EXTRA_NEG = ", holding mirror, red mirror, mirror"

POSES = {
    "amazon": {
        "pose": "amazon_position, cowgirl_position, girl_on_top, facing_away, legs_up, feet_in_air, front_view",
        "dp_lora": "doublepenetration_r1.safetensors",
        "dp_trig": "doublepen, vaginal, anal, double_penetration, both_holes",
        "male": "disembodied_penis, 2penises, black_penis, dark_penis",
    },
    "double_vaginal": {
        "pose": "double_vaginal, two_penises_in_one_pussy, missionary_position, legs_up, spread_legs, front_view",
        "dp_lora": "concept_double_vaginal-ill_d.safetensors",
        "dp_trig": "double vaginal, two_penises_in_one_pussy",
        "male": "disembodied_penis, 2penises, black_penis, dark_penis",
    },
    "triple_vaginal": {
        "pose": "triple_vaginal, three_penises_in_one_pussy, missionary_position, legs_up, spread_legs, front_view",
        "dp_lora": "concept_double_vaginal-ill_d.safetensors",
        "dp_trig": "triple vaginal, three_penises_in_one_pussy",
        "male": "disembodied_penis, 2penises, black_penis, dark_penis",
    },
    "double_anal": {
        "pose": "double_anal, two_penises_in_one_ass, anal_penetration, doggystyle, from_behind, front_view",
        "dp_lora": "double_anal_ilxl_goofy.safetensors",
        "dp_trig": "double anal, mmf threesome, group sex, two_penises_in_one_ass",
        "male": "disembodied_penis, 2penises, black_penis, dark_penis",
    },
}

nodes = {}
nodes["ckpt"] = {"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":CKPT}}
nodes["latent_shared"] = {"class_type":"EmptyLatentImage","inputs":{"width":1024,"height":1536,"batch_size":1}}
nodes["clip_skip"] = {"class_type":"CLIPSetLastLayer","inputs":{"clip":["ckpt",1],"stop_at_clip_layer":-2}}
nodes["lora_char"] = {"class_type":"LoraLoader","inputs":{"model":["ckpt",0],"clip":["clip_skip",0],"lora_name":"Stella-Virigia-v1.safetensors","strength_model":1.0,"strength_clip":1.0}}

for pname, pcfg in POSES.items():
    ld = f"lora_depth_{pname}"
    dp = f"lora_dp_{pname}"
    ls = f"lora_size_{pname}"
    ng = f"neg_{pname}"

    nodes[ld] = {"class_type":"LoraLoader","inputs":{"model":["lora_char",0],"clip":["lora_char",1],"lora_name":"penetration_depth.safetensors","strength_model":1.5,"strength_clip":1.0}}
    nodes[dp] = {"class_type":"LoraLoader","inputs":{"model":[ld,0],"clip":[ld,1],"lora_name":pcfg["dp_lora"],"strength_model":1.0,"strength_clip":1.0}}
    nodes[ls] = {"class_type":"LoraLoader","inputs":{"model":[dp,0],"clip":[dp,1],"lora_name":"Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors","strength_model":0.5,"strength_clip":1.0}}
    nodes[ng] = {"class_type":"CLIPTextEncode","inputs":{"text":NEG + EXTRA_NEG,"clip":[ls,1]}}

    prompt = f"score_9, score_8_up, source_anime, rating_explicit, {CHAR}, {OUTFIT}, {pcfg['male']}, {pcfg['dp_trig']}, {DEPTH}, {pcfg['pose']}, {EXPR}, {LIGHT}, anime, masterpiece, best_quality"
    prompt = prompt.replace(", ,", ",").replace(",,", ",")
    nodes[f"p_{pname}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":[ls,1]}}
    nodes[f"k_{pname}"] = {"class_type":"KSampler","inputs":{"seed":42424249,"steps":20,"cfg":3.5,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":[ls,0],"positive":[f"p_{pname}",0],"negative":[ng,0],"latent_image":["latent_shared",0]}}
    nodes[f"d_{pname}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{pname}",0],"vae":["ckpt",2]}}
    nodes[f"s_{pname}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"test_{pname}_virigia","images":[f"d_{pname}",0]}}

with open(os.path.join(B, "workflow_test_4poses.json"), "w", encoding="utf-8") as f:
    json.dump(nodes, f, indent=2, ensure_ascii=False)

n = sum(1 for v in nodes.values() if v.get("class_type")=="SaveImage")
print(f"✅ workflow_test_4poses.json → {n} imagenes (4 poses, 1 personaje)")
