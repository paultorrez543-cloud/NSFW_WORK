import json, os

B = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"

NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark, holding mirror, red mirror, mirror"

CHAR = "stell4virigiadef, 1girl, white hair, long hair, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, large breasts"
OUTFIT = "white bonnet, white cloak, frilled cloak, black dress, detached collar, black bowtie, red ribbon, cleavage, black gloves, white pantyhose, high heels"
MALE = "disembodied_penis, tan_penis"

# ── Fellatio: 7 etapas ──
FELLATIO_STAGES = [
    ("01_resistencia",     "intact_clothing, (penis_near_mouth:1.2), closed_mouth, refusing, trembling, tears, hands_pushing_away, full_shot"),
    ("02_primer_contacto", "licking_penis, parted_lips, tip_in_mouth, salivating, look_up_at_viewer, tears_in_eyes, cowboy_shot"),
    ("03_oral_ritmo",      "fellatio, penis_in_mouth, cheeks_sucked_in, rhythmic_sucking, bobbing_head, drooling, saliva_trail, medium_shot"),
    ("04_deepthroat",      "deepthroat, (throat_bulge:1.2), gagging, watery_eyes, tear_tracks, open_mouth, fingers_in_hair, medium_close-up"),
    ("05_facial_climax",   "oral_cumshot, excessive_cum, semen_on_face, mouth_open, cum_in_mouth, cum_drip, extreme_ahegao, heart_pupils, cowboy_shot"),
    ("06_post_swallow",    "cum_overflow, tongue_out, displaying_cum, blank_eyes, slack_jawed, drooling, close-up"),
    ("07_inconsciente",    "sleeping, relaxed_face, messy_face, dried_cum_on_face, dried_saliva, completely_nude, wide_shot, overhead_view"),
]

# ── Paizuri: 7 etapas ──
PAIZURI_STAGES = [
    ("01_resistencia",     "intact_clothing, exposed_cleavage, (penis_on_chest:1.2), embarrassed, looking_away, full_shot"),
    ("02_primer_ajuste",   "cleavage_press, hands_squeezing_breasts, penis_between_breasts, blushing, parted_lips, cowboy_shot"),
    ("03_ritmo_friccion",  "paizuri, breast_smother, breasts_squeezing, rhythmic_motion, sweat_gleam, bouncing_breasts, medium_shot"),
    ("04_intenso",         "intense_paizuri, extreme_cleavage_squish, (saliva_on_breasts:1.2), heavy_blush, ahegao, medium_close-up"),
    ("05_bukkake_climax",  "bukkake, cum_on_breasts, semen_between_breasts, cum_splatter, spasming, extreme_ahegao, heart_pupils, cowboy_shot"),
    ("06_post_desgaste",   "covered_in_cum, milk_and_cum, blank_eyes, relaxed_hands, drool, close-up"),
    ("07_inconsciente",    "sleeping, exhausted, breasts_resting, cum_pool_on_chest, completely_nude, wide_shot, overhead_view"),
]

# ── Poses (todas a 1024x1536) ──
FELLATIO_POSES = {
    "kneeling":  "kneeling, on_knees, looking_up_at_viewer",
    "lying_down":"lying, on_back, upside_down_oral, hanging_head",
    "bent_over": "bent_over, on_all_fours, looking_up_at_viewer",
    "looking_up":"sitting, looking_up_at_viewer, from_above",
}

PAIZURI_POSES = {
    "lying":      "lying, on_back, holding_breasts",
    "kneeling":   "kneeling, on_knees, squeezing_breasts",
    "sitting_lap":"sitting_on_lap, lap_pillow",
    "top_view":   "from_above, overhead_view, cleavage_view, pov",
}

def build_workflow(pose_dict, stages, prefix):
    nodes = {}
    nodes["ckpt"] = {"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":CKPT}}
    nodes["latent_shared"] = {"class_type":"EmptyLatentImage","inputs":{"width":1024,"height":1536,"batch_size":1}}
    nodes["clip_skip"] = {"class_type":"CLIPSetLastLayer","inputs":{"clip":["ckpt",1],"stop_at_clip_layer":-2}}
    nodes["lora_char"] = {"class_type":"LoraLoader","inputs":{"model":["ckpt",0],"clip":["clip_skip",0],"lora_name":"Stella-Virigia-v1.safetensors","strength_model":1.0,"strength_clip":1.0}}
    nodes["lora_size"] = {"class_type":"LoraLoader","inputs":{"model":["lora_char",0],"clip":["lora_char",1],"lora_name":"Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors","strength_model":0.5,"strength_clip":1.0}}
    nodes["neg"] = {"class_type":"CLIPTextEncode","inputs":{"text":NEG,"clip":["lora_size",1]}}

    for pose_name, pose_tags in pose_dict.items():
        for n, stage_tags in stages:
            if n == "01_resistencia":
                parts = ["score_9, score_8_up, source_anime, rating_explicit", CHAR, OUTFIT, MALE, stage_tags, pose_tags, LIGHT, "anime, masterpiece, best_quality"]
            else:
                parts = ["score_9, score_8_up, source_anime, rating_explicit", CHAR, MALE, stage_tags, pose_tags, LIGHT, "anime, masterpiece, best_quality"]
            prompt = ", ".join([p for p in parts if p]).replace(", ,", ",").replace(",,", ",")
            key = f"{pose_name}_{n}"
            nodes[f"p_{key}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":["lora_size",1]}}
            nodes[f"k_{key}"] = {"class_type":"KSampler","inputs":{"seed":42424249,"steps":20,"cfg":3.5,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":["lora_size",0],"positive":[f"p_{key}",0],"negative":["neg",0],"latent_image":["latent_shared",0]}}
            nodes[f"d_{key}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{key}",0],"vae":["ckpt",2]}}
            nodes[f"s_{key}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"{prefix}_{pose_name}_{n}","images":[f"d_{key}",0]}}
    return nodes

# Fellatio
wf = build_workflow(FELLATIO_POSES, FELLATIO_STAGES, "virigia_fellatio")
with open(os.path.join(B, "workflow_virigia_fellatio.json"), "w", encoding="utf-8") as f:
    json.dump(wf, f, indent=2, ensure_ascii=False)
print(f"✅ workflow_virigia_fellatio.json → {sum(1 for v in wf.values() if v.get('class_type')=='SaveImage')} img")

# Paizuri
wf = build_workflow(PAIZURI_POSES, PAIZURI_STAGES, "virigia_paizuri")
with open(os.path.join(B, "workflow_virigia_paizuri.json"), "w", encoding="utf-8") as f:
    json.dump(wf, f, indent=2, ensure_ascii=False)
print(f"✅ workflow_virigia_paizuri.json → {sum(1 for v in wf.values() if v.get('class_type')=='SaveImage')} img")
