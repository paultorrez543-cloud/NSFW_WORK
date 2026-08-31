import json, os

B = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"
MALE = "disembodied_penis, 2penises, black_penis, dark_penis"
DP = "doublepen, vaginal, anal, double_penetration"
POSE = "reverse_cowgirl, girl_on_top, facing_away, looking_back, front_view"
EXPR = "rolled_back_eyes, tongue_out, drooling, ahegao"

NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark"

DEPTH_VERSIONS = {
    "minima":   {"strength": -2, "tags": "imminent penetration, penis, POV"},
    "estandar": {"strength": 0,  "tags": "penis, POV"},
    "maxima":   {"strength": 2,  "tags": "deep penetration, penis, POV"},
}

CHARS = {
    # ── Originales ──
    "virigia_default": {"lora":"Stella-Virigia-v1.safetensors","seed":42424249,
        "char":"stell4virigiadef, 1girl, white hair, long hair, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, large breasts",
        "outfit":"white bonnet, white cloak, frilled cloak, black dress, detached collar, black bowtie, red ribbon, cleavage, black gloves, white pantyhose, high heels, clothes_lift","extra_neg":", holding mirror, red mirror, mirror"},
    "virigia_bunny": {"lora":"Stella-Virigia-v1.safetensors","seed":42424250,
        "char":"stell4virigiabnuy, 1girl, white hair, long hair, half up braid, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, mole on hip, large breasts",
        "outfit":"fake animal ears, rabbit ears, lace hairband, black hairband, detached collar, red bowtie, lace collar, fur armlet, cleavage, white leotard, strapless leotard, side-tie leotard, cross-laced leotard, highleg leotard, crotch zipper, showgirl skirt, white thighhighs, single fishnet thighhigh, mismatched legwear, frilled thigh strap, heart o-ring, wrist cuffs, lace-trimmed wrist cuffs, ankle strap, red high heels, clothes_lift",
        "extra_neg":", holding mirror, red mirror, mirror, tail, demon tail"},
    "shia": {"lora":"Shia_Stella_Sora.safetensors","seed":42424251,
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
    # ── Nuevos ──
    "amber": {"lora":"Amber_Stella_Sora.safetensors","seed":42424261,
        "char":"AmberSora, 1girl, black hair, yellow eyes, hair ornament, hood down, fingerless gloves",
        "outfit":"white dress, sideless dress, thighhighs, thigh boots, clothes_lift","extra_neg":", black cat"},
    "portia": {"lora":"Portia_Stella_Sora.safetensors","seed":42424262,
        "char":"Portia, 1girl, visor cap, long hair, green hair, mole under eye, mole under mouth",
        "outfit":"employee uniform, strap slip, button gap, waist apron, clothes_lift","extra_neg":""},
    "freesia": {"lora":"Freesia_Stella-10.safetensors","seed":42424263,
        "char":"Freesia_Stella, 1girl, long hair, red eyes, side ponytail, grey hair, hair ornament, hair flower, white flower, sidelocks, blunt bangs",
        "outfit":"long sleeves, red shirt, collared shirt, double-breasted, buttons, pleated skirt, miniskirt, grey skirt, blue jacket, peaked cap, military hat, black headwear, military uniform, necktie, white pantyhose, thigh strap, clothes_lift","extra_neg":""},
    "laru": {"lora":"Laru_Dovellys.safetensors","seed":42424264,
        "char":"laru stella sora, 1girl, twintails, grey hair, purple eyes, skin fang",
        "outfit":"peaked cap, blue headwear, white dress, puffy long sleeves, blue cape, blue jacket, white thighhighs, blue footwear, high heels, high heel boots, clothes_lift","extra_neg":""},
    "nazuka": {"lora":"Nazuka_Dovellys.safetensors","seed":42424265,
        "char":"nazuka stella sora, 1girl, black hair, red eyes, hairband, hair flower, hair ornament",
        "outfit":"short dress, orange dress, white shirt, blue cape, detached sleeves, frilled sleeves, white choker, frilled choker, frilled gloves, white gloves, clothes_lift","extra_neg":", staff, holding staff"},
    "kaede": {"lora":"Kaede_Dovellys.safetensors","seed":42424266,
        "char":"kaede stella sora, 1girl, pink hair, blue eyes, hair ornament, hair flower",
        "outfit":"white dress, fur collar, bare shoulders, puffy long sleeves, red shawl, yellow bow, black pantyhose, black footwear, clothes_lift","extra_neg":""},
    "tilia": {"lora":"Tilia_Dovellys.safetensors","seed":42424267,
        "char":"tilia stella sora, 1girl, blonde hair, red eyes, hairclip, hair ornament, ahoge, side ponytail",
        "outfit":"black shirt, white collar, shoulder armor, gauntlets, pauldrons, blue skirt, white thighhighs, armored boots, high heel boots, clothes_lift","extra_neg":""},
    "canace": {"lora":"Canace_Dovellys.safetensors","seed":42424268,
        "char":"canace stella sora, 1girl, purple eyes, semi-rimless eyewear, purple hair, grey hair, hair ribbon",
        "outfit":"white dress, bare shoulders, red necktie, necktie between breasts, miniskirt, pleated skirt, white skirt, clothes_lift","extra_neg":""},
    "caramel": {"lora":"Caramel_Dovellys.safetensors","seed":42424269,
        "char":"caramel stella sora, 1girl, animal ears, animal ear fluff, multicolored hair, blonde hair, twintails, drill hair, hair ribbon",
        "outfit":"black dress, purple jacket, striped clothes, spiked collar, black collar, frilled skirt, black skirt, asymmetrical legwear, mismatched legwear, fishnets, lace-trimmed legwear, striped thighhighs, o-ring thigh strap, knee boots, pink ribbon, purple ribbon, clothes_lift","extra_neg":""},
    "cosette": {"lora":"Cosette_Dovellys.safetensors","seed":42424270,
        "char":"cosette stella sora, 1girl, green eyes, two-tone hair, multicolored hair, white hair, black hair, hair ornament",
        "outfit":"black dress, clothing cutout, stomach cutout, navel cutout, cleavage cutout, pelvic curtain, black cloak, blue cape, torn thighhighs, blue thighhighs, single thighhigh, asymmetrical legwear, leg tattoo, o-ring, o-ring bottom, thigh strap, black footwear, clothes_lift","extra_neg":", bandage"},
    "fuyuka": {"lora":"FuyukaSS-10.safetensors","seed":42424271,
        "char":"fuyuka_ss, 1girl, long hair, red eyes, white hair, large breasts",
        "outfit":"long sleeves, black gloves, white shorts, yellow boots, gold gauntlets, cleavage cutout, clothes_lift","extra_neg":""},
    "firefly": {"lora":"FFSS-10.safetensors","seed":42424272,
        "char":"ffstella, 1girl, short hair, huge ahoge, ahoge, red eyes, brown hair, streaked hair, white hair",
        "outfit":"scarf, white dress, sleeveless dress, black hairband, socks, loafers, bare shoulders, clothes_lift","extra_neg":""},
    "iris": {"lora":"IrisStellaSora_IXL.safetensors","seed":42424273,
        "char":"zzIris, 1girl, red eyes, purple hair, long hair",
        "outfit":"hair ornament, long sleeves, hat, white shirt, hairclip, puffy sleeves, black skirt, cape, black pantyhose, black headwear, beret, knee boots, juliet sleeves, red necktie, cross-laced footwear, high heel boots, high-waist skirt, lace-up boots, clothes_lift","extra_neg":""},
    "mistique": {"lora":"MistiqueStellaSora_IXL.safetensors","seed":42424274,
        "char":"zzMistique, 1girl, orange eyes, orange hair, hair between eyes, long hair, twintails",
        "outfit":"witch, black dress, frilled dress, pink bow, purple bow, juliet sleeves, puffy sleeves, garter straps, witch hat, brooch, clothes_lift","extra_neg":""},
}

nodes = {}
nodes["ckpt"] = {"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":CKPT}}
nodes["latent_shared"] = {"class_type":"EmptyLatentImage","inputs":{"width":1024,"height":1536,"batch_size":1}}

for cname, cfg in CHARS.items():
    cs = f"clip_skip_{cname}"
    lc = f"lora_char_{cname}"
    nodes[cs] = {"class_type":"CLIPSetLastLayer","inputs":{"clip":["ckpt",1],"stop_at_clip_layer":-2}}
    nodes[lc] = {"class_type":"LoraLoader","inputs":{"model":["ckpt",0],"clip":[cs,0],"lora_name":cfg["lora"],"strength_model":1.0,"strength_clip":1.0}}

    for vname, vcfg in DEPTH_VERSIONS.items():
        ld = f"lora_depth_{cname}_{vname}"
        dp = f"lora_dp_{cname}_{vname}"
        ls = f"lora_size_{cname}_{vname}"
        ng = f"neg_{cname}_{vname}"
        nodes[ld] = {"class_type":"LoraLoader","inputs":{"model":[lc,0],"clip":[lc,1],"lora_name":"penetration_depth.safetensors","strength_model":vcfg["strength"],"strength_clip":1.0}}
        nodes[dp] = {"class_type":"LoraLoader","inputs":{"model":[ld,0],"clip":[ld,1],"lora_name":"doublepenetration_r1.safetensors","strength_model":1.0,"strength_clip":1.0}}
        nodes[ls] = {"class_type":"LoraLoader","inputs":{"model":[dp,0],"clip":[dp,1],"lora_name":"Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors","strength_model":0.5,"strength_clip":1.0}}
        nodes[ng] = {"class_type":"CLIPTextEncode","inputs":{"text":NEG + cfg["extra_neg"],"clip":[ls,1]}}

        prompt = f"score_9, score_8_up, source_anime, rating_explicit, {cfg['char']}, {cfg['outfit']}, {MALE}, {DP}, {vcfg['tags']}, {POSE}, {EXPR}, {LIGHT}, anime, masterpiece, best_quality".replace(", ,", ",").replace(",,", ",")
        key = f"{cname}_{vname}"
        nodes[f"p_{key}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":[ls,1]}}
        nodes[f"k_{key}"] = {"class_type":"KSampler","inputs":{"seed":cfg["seed"],"steps":20,"cfg":3.5,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":[ls,0],"positive":[f"p_{key}",0],"negative":[ng,0],"latent_image":["latent_shared",0]}}
        nodes[f"d_{key}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{key}",0],"vae":["ckpt",2]}}
        nodes[f"s_{key}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"depth_{vname}_{cname}","images":[f"d_{key}",0]}}

with open(os.path.join(B, "workflow_depth_versions.json"), "w", encoding="utf-8") as f:
    json.dump(nodes, f, indent=2, ensure_ascii=False)

n = sum(1 for v in nodes.values() if v.get("class_type")=="SaveImage")
print(f"✅ workflow_depth_versions.json → {n} imagenes")
print(f"   {len(CHARS)} personajes x 3 profundidades (minima/estandar/maxima)")
