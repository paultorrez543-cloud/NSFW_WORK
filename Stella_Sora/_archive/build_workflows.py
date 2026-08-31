import json, os

OUT = "E:/ComfyUI/characters/Stella_Sora"

CHARS = {
    "virigia_default": {
        "trigger": "stell4virigiadef",
        "desc": "1girl, white hair, long hair, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, large breasts",
        "outfit": "white bonnet, multicolored hat, white cloak, frilled cloak, tassel, detached collar, black bowtie, cleavage, black dress, grey dress, two-tone dress, see-through dress, black gloves, lace-trimmed gloves, white pantyhose, ankle lace-up, high heels, holding mirror",
        "lora": "Stella-Virigia-v1.safetensors", "seed": 42424249
    },
    "virigia_bunny": {
        "trigger": "stell4virigiabnuy",
        "desc": "1girl, white hair, long hair, half up braid, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, mole on hip, large breasts",
        "outfit": "bunny outfit, bunny ears, leotard, fishnet stockings, high heels",
        "lora": "Stella-Virigia-v1.safetensors", "seed": 42424250
    },
}

CKPT = "waiIllustriousSDXL_v170.safetensors"
NEG_BASE = "lowres, bad anatomy, bad eyes, deformed eyes, asymmetrical_eyes, different_sized_eyes, bad hands, extra fingers, worst_quality, blurry, ugly, censored, thick lines, black outlines, lineart, (deformed:1.5), (bad hand:1.3), extra finger, mutated, poorly drawn face, character fusion, fused males, merged males, conjoined twins, connected bodies, double heads, duplicate limbs, fused bodies, (duplicate panties:1.4), (multiple panties:1.4), extra underwear, duplicate bra, wrong hair length, mutated hair, mature, old woman, hag, wrinkled skin, adult female, semi-realistic, 3d, 3d render, photorealistic, realistic, real life, 3d model, cg render, photography, red_hair, pink_hair"
STYLE = "Hentai comic style, multi-view, 1-2 panels, (focus lines:1.2), (vibration lines:1.1), sound effects, comic-style facial expressions, bedroom, bed, dark_room, dim_lighting, film_grain, game cg, official art, digital painting, semi-realistic, soft lighting, detailed background, fantasy, clean linework, ornate details, sharp_focus, detailed_skin, detailed_eyes, eyelashes, detailed_eyelashes, hair_detail, matte_skin, natural_lighting, depth_of_field, (blurred background:1.3), (bokeh:0.3)"
MALE_DP = "1boy, male, huge_penis, size_difference, simple_background_male, generic_man, anonymous_male, short_hair, masculine, head_out_of_frame, faceless_male, cropped_male_face, no_male_face, male_from_neck_down, male_body_only, female_focus"
MALE_TP = "3boys, male, huge_penis, size_difference, multiple_penises, anonymous_males, generic_men, short_hair, masculine, head_out_of_frame, faceless_male, cropped_male_face, no_male_face, male_from_neck_down, male_body_only, female_focus, group, gangbang"

POSES = [
    ("missionary", "lying, on_back, legs_up, spread_legs, held_down"),
    ("cowgirl", "cowgirl_position, girl_on_top, straddling"),
    ("doggystyle", "doggystyle, from_behind, arched_back, hands_on_hips"),
    ("piledriver", "piledriver, inverted, legs_up, upside_down"),
    ("prone_bone", "prone_bone, lying, on_stomach, from_behind, legs_closed"),
    ("standing", "standing_sex, against_wall, held_up, legs_around_waist"),
    ("reverse_cowgirl", "reverse_cowgirl, cowgirl_position, girl_on_top, facing_away, looking_back"),
    ("spooning", "spooning, spoon_position, lying, on_side, from_behind, legs_together"),
    ("full_nelson", "full_nelson, nelson_position, restrained, legs_folded, held_up, pinned"),
    ("mating_press", "mating_press, folded, shoulders_pressed, legs_on_shoulders, pinned, deep"),
    ("oral", "fellatio, blowjob, oral, penis_in_mouth, facefuck, deepthroat, on_knees, looking_up"),
    ("paizuri", "paizuri, titfuck, between_breasts, breast_sandwich, penis_between_breasts"),
    ("sitting", "sitting_on_lap, sitting_position, lap_sex, straddling_sitting, chair, arms_around_neck"),
]

S_DP = {
    "inicio": "both_erect, penis_presented, penis_on_pussy, penis_on_anus, imminent_double, about_to_penetrate, nervous, anticipation, blush, sweat",
    "entrada": "double_penetration, simultaneous_insertion, both_holes, tip_in_pussy, tip_in_ass, first_insertion, stretching, pain, tears, screaming",
    "penetrada": "double_penetration, vaginal, anal, deep, balls_deep, full_insertion, both_holes, pussy_and_ass, thrusting, ahegao, rolled_back_eyes, drooling, forced_orgasm",
    "final": "double_penetration, climax, vaginal, anal, cum, cum_in_pussy, cum_in_ass, both_cumming, ahegao, forced_orgasm, mind_break, convulsing, heavy_sweat, excessive_cum",
    "xray": "double_penetration, x-ray, internal_shot, cross-section, vaginal, anal, deep, both_holes, penis_inside, stomach_bulge, internal_cumshot, cum_in_pussy, cum_in_ass, ahegao, mind_break",
}
S_TP = {
    "inicio": "triple_penetration, three_cocks, penis_presented, spitroast, imminent_triple, about_to_penetrate, nervous, anticipation, blush, sweat",
    "entrada": "triple_penetration, simultaneous_insertion, three_holes, tip_in_pussy, tip_in_ass, tip_in_mouth, first_insertion, stretching, pain, tears, gagging",
    "penetrada": "triple_penetration, vaginal, anal, oral, deep, balls_deep, full_insertion, one_in_pussy, one_in_ass, one_in_mouth, mmf_threesome, thrusting, ahegao, rolled_back_eyes, drooling, forced_orgasm",
    "final": "triple_penetration, climax, vaginal, anal, oral, cum, cum_in_pussy, cum_in_ass, cum_in_mouth, excessive_cum, ahegao, forced_orgasm, mind_break, convulsing, heavy_sweat",
    "xray": "triple_penetration, x-ray, internal_shot, cross-section, vaginal, anal, deep, three_cocks, penis_inside, stomach_bulge, internal_cumshot, cum_in_pussy, cum_in_ass, cum_in_mouth, ahegao, mind_break",
}

NEG_NUDE = "standing fully clothed, solo standing, standing outside, text_bubbles, speech_bubble, dialogue, onomatopoeia, japanese_text, english_text, white_box, text_box, letter, word, clothed, dress, clothes, outfit, " + NEG_BASE
NEG_NOR = "standing fully clothed, solo standing, standing outside, text_bubbles, speech_bubble, dialogue, onomatopoeia, japanese_text, english_text, white_box, text_box, letter, word, nude, naked, exposed_breasts, exposed_pussy, completely_nude, " + NEG_BASE

def build(char_name, cfg, om, pm):
    stages = S_DP if pm == "dp" else S_TP
    male = MALE_DP if pm == "dp" else MALE_TP
    neg = NEG_NUDE if om == "nude" else NEG_NOR
    outfit = "nude, naked, completely_nude, exposed_breasts, exposed_pussy" if om == "nude" else cfg["outfit"] + ", clothes_lift, clothes_pulled_aside"
    char_tags = cfg["trigger"] + ", " + cfg["desc"]
    prefix = f"{char_name}_{om}_{pm}"
    seed = cfg["seed"]

    nodes = {}
    nodes["ckpt"] = {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}}
    nodes["lora_char"] = {"class_type": "LoraLoader", "inputs": {"model": ["ckpt",0], "clip": ["ckpt",1], "lora_name": cfg["lora"], "strength_model": 0.8, "strength_clip": 0.8}}
    nodes["lora_stab"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_char",0], "clip": ["lora_char",1], "lora_name": "stabilizer_animaginexl.safetensors", "strength_model": 0.20, "strength_clip": 0.20}}
    nodes["lora_ugly"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_stab",0], "clip": ["lora_stab",1], "lora_name": "faceless-ugly-man-illustriousxl-lora-nochekaiser.safetensors", "strength_model": 1.0, "strength_clip": 1.0}}
    nodes["lora_dp"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_ugly",0], "clip": ["lora_ugly",1], "lora_name": "doublepenetration_r1.safetensors", "strength_model": 1.0, "strength_clip": 1.0}}
    nodes["lora_size"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_dp",0], "clip": ["lora_dp",1], "lora_name": "Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors", "strength_model": -0.5, "strength_clip": -0.5}}
    nodes["neg"] = {"class_type": "CLIPTextEncode", "inputs": {"text": neg, "clip": ["lora_size",1]}}

    nid = 100
    for pn, pt in POSES:
        for sn, st in stages.items():
            prompt = f"{char_tags}, 1girl, {outfit}, {male}, {pt}, {st}, {STYLE}"
            sid, lid, kid, vid, svid = str(nid), str(nid+1), str(nid+2), str(nid+3), str(nid+4)
            nodes[sid] = {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["lora_size",1]}}
            nodes[lid] = {"class_type": "EmptyLatentImage", "inputs": {"width": 832, "height": 1216, "batch_size": 1}}
            nodes[kid] = {"class_type": "KSampler", "inputs": {"seed": seed, "steps": 28, "cfg": 4.0, "sampler_name": "dpmpp_2m", "scheduler": "karras", "denoise": 1, "model": ["lora_size",0], "positive": [sid,0], "negative": ["neg",0], "latent_image": [lid,0]}}
            nodes[vid] = {"class_type": "VAEDecode", "inputs": {"samples": [kid,0], "vae": ["ckpt",2]}}
            nodes[svid] = {"class_type": "SaveImage", "inputs": {"filename_prefix": f"{prefix}_{pn}_{sn}", "images": [vid,0]}}
            nid += 5

    poutfit = cfg["outfit"] + ", clothes_lift, clothes_pulled_aside" if om == "nor" else "nude, naked, completely_nude, exposed_breasts, exposed_pussy"
    pprompt = f"{char_tags}, 1girl, {poutfit}, standing, looking at viewer, full body, solo, character_introduction, portrait, front_view, simple background, official art style, character_focus, {STYLE}"
    sid, lid, kid, vid, svid = str(nid), str(nid+1), str(nid+2), str(nid+3), str(nid+4)
    nodes[sid] = {"class_type": "CLIPTextEncode", "inputs": {"text": pprompt, "clip": ["lora_size",1]}}
    nodes[lid] = {"class_type": "EmptyLatentImage", "inputs": {"width": 832, "height": 1216, "batch_size": 1}}
    nodes[kid] = {"class_type": "KSampler", "inputs": {"seed": seed, "steps": 28, "cfg": 4.0, "sampler_name": "dpmpp_2m", "scheduler": "karras", "denoise": 1, "model": ["lora_size",0], "positive": [sid,0], "negative": ["neg",0], "latent_image": [lid,0]}}
    nodes[vid] = {"class_type": "VAEDecode", "inputs": {"samples": [kid,0], "vae": ["ckpt",2]}}
    nodes[svid] = {"class_type": "SaveImage", "inputs": {"filename_prefix": f"{prefix}_presentacion", "images": [vid,0]}}
    return nodes

variants = [("nude","dp"), ("nude","tp"), ("nor","dp"), ("nor","tp")]
total = 0
for cn, cfg in CHARS.items():
    cdir = os.path.join(OUT, cn)
    os.makedirs(cdir, exist_ok=True)
    for om, pm in variants:
        wf = build(cn, cfg, om, pm)
        fpath = os.path.join(cdir, f"workflow_{om}_{pm}.json")
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(wf, f, indent=2, ensure_ascii=False)
        n = sum(1 for v in wf.values() if v.get("class_type") == "SaveImage")
        print(f"✅ {cn}/{om}_{pm} → {n} img")
        total += n

print(f"\n🎯 {total} imágenes en {len(CHARS)*4} workflows")
print(f"🔗 char(0.8) → stabilizer(0.20) → ugly(1.0) → dp(1.0) → penis(-0.5)")
