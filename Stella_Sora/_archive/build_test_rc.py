import json, os

B = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"
MALE = "disembodied_penis, 2penises, black_penis, dark_penis"
DP = "doublepen, vaginal, anal, double_penetration, both_holes"
POSE = "reverse_cowgirl, girl_on_top, facing_away, looking_back, front_view"
DEPTH = "(deep penetration:1.4), full_penetration"
EXPR = "rolled_back_eyes, tongue_out, drooling, ahegao"

NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark"

CHARS = {
    "virigia_default": {"lora":"Stella-Virigia-v1.safetensors","seed":42424249,
        "char":"stell4virigiadef, 1girl, white hair, long hair, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, large breasts",
        "outfit":"white bonnet, white cloak, frilled cloak, black dress, detached collar, black bowtie, red ribbon, cleavage, black gloves, white pantyhose, high heels, clothes_lift","extra_neg":", holding mirror, red mirror, mirror"},
    "virigia_bunny": {"lora":"Stella-Virigia-v1.safetensors","seed":42424250,
        "char":"stell4virigiabnuy, 1girl, white hair, long hair, half up braid, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, mole on hip, large breasts",
        "outfit":"fake animal ears, rabbit ears, lace hairband, black hairband, detached collar, red bowtie, lace collar, fur armlet, cleavage, white leotard, strapless leotard, side-tie leotard, cross-laced leotard, highleg leotard, crotch zipper, showgirl skirt, white thighhighs, single fishnet thighhigh, mismatched legwear, frilled thigh strap, heart o-ring, wrist cuffs, lace-trimmed wrist cuffs, ankle strap, red high heels, clothes_lift",
        "extra_neg":", holding mirror, red mirror, mirror, tail, demon tail"},
    "shia": {"lora":"Shia_Stella_Sora__シア_ステラソラ.safetensors","seed":42424251,
        "char":"shia, stella sora, 1girl, (large breasts:1.3)",
        "outfit":"bunny girl, bunny ears, sailor collar, top, bikini, covered midriff, clothes_lift","extra_neg":", tail, demon tail"},
    "bernina_default": {"lora":"Stella-Bernina-v1.safetensors","seed":42424253,
        "char":"stell4berninadef, 1girl, pink hair, gradient hair, short hair with long locks, red hair ribbon, inverted cross, pink eyes, curled horns, low wings, (large breasts:1.3)",
        "outfit":"maid headdress, white shrug, puffy sleeves, wide sleeves, black dress, red dress, two-tone dress, hobble dress, long dress, layered dress, strapless, red o-ring, buttons, see-through cleavage, fishnet top, black gloves, fishnet gloves, black bow, high heels boots, black boots, clothes_lift",
        "extra_neg":", tail, demon tail, lantern, holding lantern"},
    "bernina_bunny": {"lora":"Stella-Bernina-v1.safetensors","seed":42424254,
        "char":"stell4berninabnuy, 1girl, pink hair, gradient hair, short hair with long locks, red hair ribbon, inverted cross, pink eyes, curled horns, low wings, (large breasts:1.3)",
        "outfit":"fake animal ears, rabbit ears, detached collar, red necktie, necktie between breasts, black leotard, strapless, highleg leotard, side-tie leotard, half gloves, black gloves, fishnet pantyhose, thigh belt, red high heels, tight clothes, clothes_lift",
        "extra_neg":", tail, demon tail"},
    "reisen": {"lora":"Reisen_ridge_-_Stella_Sora.safetensors","seed":42424255,
        "char":"ReisenStellaS, 1girl, blonde hair, antenna hair, very long hair, low-tied long hair, yellow eyes, thick thighs, large breasts",
        "outfit":"mask on head, plague doctor mask, goggles, goggles on head, jacket, black jacket, open jacket, bowtie, black bowtie, white shirt, underbust, brown belt, shorts, black shorts, white thighhighs, skindentation, black boots, fold-over boots, clothes_lift",
        "extra_neg":""},
}

nodes = {}
nodes["ckpt"] = {"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":CKPT}}
nodes["latent_shared"] = {"class_type":"EmptyLatentImage","inputs":{"width":1024,"height":1536,"batch_size":1}}

for cname, cfg in CHARS.items():
    cs = f"clip_skip_{cname}"
    lc = f"lora_char_{cname}"
    ld = f"lora_depth_{cname}"
    dp = f"lora_dp_{cname}"
    ls = f"lora_size_{cname}"
    ng = f"neg_{cname}"

    nodes[cs] = {"class_type":"CLIPSetLastLayer","inputs":{"clip":["ckpt",1],"stop_at_clip_layer":-2}}
    nodes[lc] = {"class_type":"LoraLoader","inputs":{"model":["ckpt",0],"clip":[cs,0],"lora_name":cfg["lora"],"strength_model":1.0,"strength_clip":1.0}}
    nodes[ld] = {"class_type":"LoraLoader","inputs":{"model":[lc,0],"clip":[lc,1],"lora_name":"penetration_depth.safetensors","strength_model":1.5,"strength_clip":1.0}}
    nodes[dp] = {"class_type":"LoraLoader","inputs":{"model":[ld,0],"clip":[ld,1],"lora_name":"doublepenetration_r1.safetensors","strength_model":1.0,"strength_clip":1.0}}
    nodes[ls] = {"class_type":"LoraLoader","inputs":{"model":[dp,0],"clip":[dp,1],"lora_name":"Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors","strength_model":0.5,"strength_clip":1.0}}
    nodes[ng] = {"class_type":"CLIPTextEncode","inputs":{"text":NEG + cfg["extra_neg"],"clip":[ls,1]}}

    prompt = f"score_9, score_8_up, source_anime, rating_explicit, {cfg['char']}, {cfg['outfit']}, {MALE}, {DP}, {DEPTH}, {POSE}, {EXPR}, {LIGHT}, anime, masterpiece, best_quality"
    nodes[f"p_{cname}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":[ls,1]}}
    nodes[f"k_{cname}"] = {"class_type":"KSampler","inputs":{"seed":cfg["seed"],"steps":20,"cfg":3.5,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":[ls,0],"positive":[f"p_{cname}",0],"negative":[ng,0],"latent_image":["latent_shared",0]}}
    nodes[f"d_{cname}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{cname}",0],"vae":["ckpt",2]}}
    nodes[f"s_{cname}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"test_rc_{cname}","images":[f"d_{cname}",0]}}

with open(os.path.join(B, "workflow_test_reverse_cowgirl.json"), "w", encoding="utf-8") as f:
    json.dump(nodes, f, indent=2, ensure_ascii=False)

n = sum(1 for v in nodes.values() if v.get("class_type")=="SaveImage")
print(f"✅ workflow_test_reverse_cowgirl.json → {n} imagenes")
print(f"   cadena completa: char(1.0) → depth(1.5) → dp(1.0) → penis(0.5)")
