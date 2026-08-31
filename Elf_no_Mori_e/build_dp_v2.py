import json, os

OUT = "E:/ComfyUI/characters/Elf_no_Mori_e/workflow_all_7_dp_doggy.json"
CKPT = "waiIllustriousSDXL_v170.safetensors"
PENIS_LORA = "Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors"
DP_LORA = "doublepenetration_r1.safetensors"
DEPTH_LORA = "penetration_depth.safetensors"

CHARS = {
    "nol": {
        "trigger": "Nol_YSEnMe",
        "desc": "1girl, red hair, long hair, red eyes, pointy ears, elf, small breasts",
        "outfit": "clothes_lift, skirt_lift",
        "lora": "Nol_Youkoso_Sukebe_Elf_no_Mori_e.safetensors",
    },
    "delva": {
        "trigger": "cerebrien_cnr",
        "desc": "1girl, dark elf, dark skin, dark-skinned female, gradient hair, long hair, purple hair, yellow eyes, large breasts, shiny skin, pointy ears",
        "outfit": "clothes_lift, skirt_lift",
        "lora": "Delva_Cerebrien.safetensors",
    },
    "elda": {
        "trigger": "barred_cnr",
        "desc": "1girl, dark elf, dark skin, dark-skinned female, gradient hair, short hair, blonde hair, green eyes, large breasts, shiny skin, pointy ears",
        "outfit": "clothes_lift, skirt_lift",
        "lora": "Elda_Barred.safetensors",
    },
    "evelyn": {
        "trigger": "evelycede",
        "desc": "1girl, huge breasts, dark elf, dark-skinned female, pointy ears, yellow eyes, sidelocks, white hair, blunt bangs, tress ribbon, hair ribbon, red ribbon",
        "outfit": "clothes_lift, skirt_lift",
        "lora": "evelyn_celebrian-koto-illustrious.safetensors",
    },
    "lucie": {
        "trigger": "luciemena1",
        "desc": "1girl, blonde hair, pointy ears, elf, blue eyes, hair flower, multicolored hair, gradient hair, large breasts",
        "outfit": "clothes_lift, skirt_lift",
        "lora": "lucy_menelumia-koto-illustrious-000006.safetensors",
    },
    "misery": {
        "trigger": "miserydg",
        "desc": "1girl, long hair, blonde hair, red eyes, elf, pointy ears, multicolored hair, small breasts",
        "outfit": "clothes_lift, skirt_lift",
        "lora": "Misery NoobAiLoraV2.safetensors",
    },
    "phyllis": {
        "trigger": "Phyllis Hagerhelm",
        "desc": "1girl, mature female, elf, very long hair, grey hair, blue hair, gradient hair, twintails, red eyes, slit pupils, pointy ears, huge breasts",
        "outfit": "clothes_lift, skirt_lift",
        "lora": "R5NNJJJEJPN85K317A2ME3GFE0.safetensors",
    },
}

MALE = "disembodied_penis, floating_penis, invisible_man, penis, 2penises"
DP_TAGS = "doublepen, vaginal, anal, double_penetration, both_holes, pussy_and_ass"
DEPTH_TAGS = "(deep penetration:1.5), (balls deep:1.4), (stomach bulge:1.3), (imminent penetration:1.2), penetration"
POSE = "cowgirl_position, girl_on_top, straddling"
EXTRA = "erect_penis, penis_visible, dimly_lit, dark_ambiance, soft_lighting, (dark lighting:1.5), (dim room:1.4), anime, masterpiece, best_quality, absurdres"
NEG = "lowres, bad anatomy, bad eyes, deformed eyes, bad hands, extra fingers, worst_quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, white background, x-ray, internal_shot, cross-section"

VARIANTS = [
    {"name": "v1_inicio", "seed": 42424241, "expr": "blush, sweat, anticipation, nervous"},
    {"name": "v2_movimiento", "seed": 42424242, "expr": "blush, sweat, heavy_breathing, open_mouth, moaning, rolling_eyes, drooling, ahegao"},
    {"name": "v3_climax", "seed": 42424243, "expr": "blush, sweat, climax, orgasmic_expression, heart_pupils, ahegao, tongue_out, drooling, tears_of_pleasure, excessive_cum, creampie"},
]

nodes = {}
nodes["ckpt"] = {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}}
nodes["latent_base"] = {"class_type": "EmptyLatentImage", "inputs": {"width": 1216, "height": 832, "batch_size": 1}}

for char_id, cfg in CHARS.items():
    cid = f"lora_char_{char_id}"
    did = f"lora_depth_{char_id}"
    dpid = f"lora_dp_{char_id}"
    psid = f"lora_ps_{char_id}"
    nid = f"neg_{char_id}"
    
    nodes[cid] = {"class_type": "LoraLoader", "inputs": {"model": ["ckpt",0], "clip": ["ckpt",1], "lora_name": cfg["lora"], "strength_model": 0.8, "strength_clip": 0.8}}
    nodes[did] = {"class_type": "LoraLoader", "inputs": {"model": [cid,0], "clip": [cid,1], "lora_name": DEPTH_LORA, "strength_model": 1.5, "strength_clip": 1.0}}
    nodes[dpid] = {"class_type": "LoraLoader", "inputs": {"model": [did,0], "clip": [did,1], "lora_name": DP_LORA, "strength_model": 1.0, "strength_clip": 1.0}}
    nodes[psid] = {"class_type": "LoraLoader", "inputs": {"model": [dpid,0], "clip": [dpid,1], "lora_name": PENIS_LORA, "strength_model": 2.0, "strength_clip": 1.0}}
    nodes[nid] = {"class_type": "CLIPTextEncode", "inputs": {"text": NEG, "clip": [psid,1]}}
    
    for v in VARIANTS:
        prompt = f"{cfg['trigger']}, {cfg['desc']}, {cfg['outfit']}, {MALE}, {DP_TAGS}, {DEPTH_TAGS}, {POSE}, {v['expr']}, {EXTRA}"
        pid = f"p_{v['name']}_{char_id}"
        kid = f"k_{v['name']}_{char_id}"
        diid = f"d_{v['name']}_{char_id}"
        siid = f"s_{v['name']}_{char_id}"
        
        nodes[pid] = {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": [psid,1]}}
        nodes[kid] = {"class_type": "KSampler", "inputs": {"seed": v["seed"], "steps": 28, "cfg": 4.0, "sampler_name": "dpmpp_2m", "scheduler": "karras", "denoise": 1, "model": [psid,0], "positive": [pid,0], "negative": [nid,0], "latent_image": ["latent_base",0]}}
        nodes[diid] = {"class_type": "VAEDecode", "inputs": {"samples": [kid,0], "vae": ["ckpt",2]}}
        nodes[siid] = {"class_type": "SaveImage", "inputs": {"filename_prefix": f"all_7_dp_v2/{v['name']}/{char_id}_{v['name']}", "images": [diid,0]}}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(nodes, f, indent=2, ensure_ascii=False)

n = sum(1 for v in nodes.values() if v.get("class_type") == "SaveImage")
print(f"✅ {OUT}")
print(f"   {n} imagenes ({len(CHARS)} elfas x 3 variantes)")
print(f"🔗 char(0.8) → depth(1.5) → dp(1.0) → penis(2.0)")
print(f"👻 disembodied_penis + invisible_man")
print(f"🎯 pesos depth en prompt, sin x-ray, sin ugly_man")
print(f"🍈 Lucie: large breasts")
