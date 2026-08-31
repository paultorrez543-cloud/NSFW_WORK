import json, os

B = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
SEED = 42424249
NEG = "lowres, bad anatomy, bad eyes, deformed eyes, bad hands, extra fingers, worst_quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section"
ENV = "dimly_lit, dark_ambiance, soft_lighting, (dark lighting:1.5), (dim room:1.4), anime, masterpiece, best_quality, absurdres"
MALE = "disembodied_penis, floating_penis, invisible_man, penis, 2penises"
DP = "doublepen, vaginal, anal, double_penetration, both_holes, pussy_and_ass"

STAGES = [
    {"n":"01_miedo","depth":"standing, looking at viewer, (imminent penetration:1.0)",
     "hands":"hands_together","eyes":"looking_at_viewer","clothes":"intact_clothing","bed":"simple background",
     "motion":"","fluids":"","hair":"neat_hair","sound":"",
     "expr":"scared, trembling, nervous_sweat, refusal, struggling, looking_away, pushing_away, fearful_expression, tears_forming"},
    {"n":"02_resistencia","depth":"(imminent penetration:1.5), about_to_penetrate, penis_on_pussy, penis_on_anus",
     "hands":"pushing_away","eyes":"wide_eyes, looking_away","clothes":"clothes_lift","bed":"bed, pillow",
     "motion":"(motion lines:1.2)","fluids":"blush, sweat, tears","hair":"slightly_messy_hair","sound":"",
     "expr":"crying, tears, struggling, resisting, pushing_away, screaming, begging, desperate, terrified, held_down, gagging"},
    {"n":"03_dolor","depth":"tip_in_pussy, tip_in_ass, first_insertion, stretching",
     "hands":"hands_gripping_sheets","eyes":"wide_eyes, horrified","clothes":"clothes_lift, skirt_lift","bed":"bed, crumpled_sheets",
     "motion":"(motion lines:1.3), (speed lines:1.2)","fluids":"sweat, tears_streaming, drooling","hair":"messy_hair","sound":"sound_effects, onomatopoeia",
     "expr":"(pain:1.4), screaming, crying, tears_streaming, painful_penetration, first_time, virgin, struggling, wide_eyes, horrified, sweat"},
    {"n":"04_sufrimiento","depth":"half_insertion, (penetration:1.3), stretching",
     "hands":"hands_above_head, restrained","eyes":"crying_eyes, tears_streaming","clothes":"clothes_lift, skirt_lift, panties_around_one_leg","bed":"bed, messy_sheets",
     "motion":"(motion lines:1.4), impact_lines","fluids":"sweat, tears_streaming, drooling, saliva_string","hair":"messy_hair, hair_stuck_to_face","sound":"sound_effects, onomatopoeia",
     "expr":"(pain:1.5), sobbing, tears_streaming, screaming, begging, please_stop, struggling_weakening, defeated_expression, messy_tears, runny_nose, saliva"},
    {"n":"05_quebranto","depth":"(deep penetration:1.3), (half insertion:1.2), thrusting",
     "hands":"hands_above_head","eyes":"half-closed_eyes, tears_streaming","clothes":"clothes_pulled_aside, breasts_outside_clothes","bed":"bed, wet_sheets",
     "motion":"(motion lines:1.4), (speed lines:1.3)","fluids":"sweat_drops, tears_streaming, drooling, saliva_string","hair":"very_messy_hair, hair_stuck_to_face","sound":"sound_effects, onomatopoeia",
     "expr":"half-closed_eyes, tears_streaming, drooling, saliva_string, giving_up, broken_spirit, pain_mixed_with_pleasure, involuntary_moaning, defeated"},
    {"n":"06_ahegao_inicio","depth":"(deep penetration:1.4), (full insertion:1.3), cervix_penetration",
     "hands":"hands_above_head","eyes":"rolled_back_eyes, open_mouth","clothes":"clothes_pulled_aside, breasts_outside_clothes","bed":"bed, soaked_sheets",
     "motion":"(motion lines:1.4), (speed lines:1.3), impact_lines","fluids":"excessive_sweat, tears_of_pleasure, drooling, saliva_string","hair":"very_messy_hair, hair_stuck_to_face","sound":"sound_effects, onomatopoeia, japanese_text_sound_effects",
     "expr":"rolled_back_eyes, tongue_out, drooling, tears_of_pleasure, forced_orgasm, ahegao, mind_break_starting, convulsing, involuntary_response"},
    {"n":"07_ahegao_total","depth":"(deep penetration:1.5), (full insertion:1.4), (balls deep:1.3)",
     "hands":"hands_above_head, clenched_hands","eyes":"heart_pupils, rolled_back_eyes, wide_open_mouth","clothes":"clothes_torn, breasts_outside_clothes","bed":"bed, soaked_sheets",
     "motion":"(motion lines:1.5), (speed lines:1.4), impact_lines","fluids":"excessive_sweat, tears_of_pleasure, excessive_drooling","hair":"disheveled_hair, hair_stuck_to_face, wet_hair","sound":"sound_effects, onomatopoeia, japanese_text_sound_effects",
     "expr":"ahegao, heart_pupils, rolled_back_eyes, tongue_out, wide_open_mouth, excessive_drooling, tears_of_pleasure, forced_orgasm, mind_break, convulsing, shaking, screaming_in_pleasure, excessive_cum, creampie"},
    {"n":"08_rota","depth":"(balls deep:1.5), (full insertion:1.5), (gaping:1.3)",
     "hands":"hands_resting, limp_arms","eyes":"blank_eyes, thousand_yard_stare","clothes":"clothes_torn, clothes_discarded","bed":"bed, destroyed_bed, soaked_sheets",
     "motion":"","fluids":"excessive_cum, cum_drip, creampie, semen_on_body","hair":"disheveled_hair, wet_hair, hair_plastered_to_face","sound":"",
     "expr":"blank_eyes, empty_expression, tongue_out, drooling, broken, defeated, mind_break, limp_body, given_up, thousand_yard_stare, tears_streaming, catatonic"},
    {"n":"09_destruida","depth":"(gaping:1.4), after_sex, semen_drip",
     "hands":"hands_resting","eyes":"half-closed_eyes, crying","clothes":"clothes_discarded","bed":"bed, messy_bed, soaked_sheets, semen_on_sheets",
     "motion":"","fluids":"exhausted, heavy_sweat, panting, creampie, cum_drip, cum_pool, semen_on_body, semen_on_face, excessive_cum","hair":"disheveled_hair, wet_hair","sound":"",
     "expr":"exhausted, half-closed_eyes, crying, tears_streaming, semen_on_face, semen_on_body, cum_drip, creampie, gaping, defeated, messy, ruined, shaking, panting"},
    {"n":"10_inconsciente","depth":"after_sex, sleeping",
     "hands":"hands_resting","eyes":"closed_eyes, unconscious","clothes":"clothes_discarded","bed":"bed, messy_bed, wet_sheets, cum_pool",
     "motion":"","fluids":"sleeping, creampie, cum_drip, semen_on_body, semen_on_face","hair":"messy_hair, wet_hair","sound":"",
     "expr":"closed_eyes, unconscious, sleeping, tears_dried, semen_on_face, semen_on_body, cum_pool, creampie, gaping, bruised, defeated, messy_hair, wet_hair"},
]

for outfit_name, (char, clothes_base) in {
    "default": ("stell4virigiadef, 1girl, white hair, long hair, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, large breasts",
                "black dress, see-through dress, white cloak, white bonnet, black gloves, white pantyhose, high heels, holding mirror"),
    "bunny": ("stell4virigiabnuy, 1girl, white hair, half up braid, red eyes, demon horns, low wings, mole on hip, large breasts",
              "bunny outfit, bunny ears, leotard, fishnet stockings, high heels"),
}.items():
    nodes = {}
    nodes["ckpt"] = {"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":CKPT}}
    nodes["lora_char"] = {"class_type":"LoraLoader","inputs":{"model":["ckpt",0],"clip":["ckpt",1],"lora_name":"Stella-Virigia-v1.safetensors","strength_model":0.8,"strength_clip":0.8}}
    nodes["lora_depth"] = {"class_type":"LoraLoader","inputs":{"model":["lora_char",0],"clip":["lora_char",1],"lora_name":"penetration_depth.safetensors","strength_model":1.5,"strength_clip":1.0}}
    nodes["lora_dp"] = {"class_type":"LoraLoader","inputs":{"model":["lora_depth",0],"clip":["lora_depth",1],"lora_name":"doublepenetration_r1.safetensors","strength_model":1.0,"strength_clip":1.0}}
    nodes["lora_size"] = {"class_type":"LoraLoader","inputs":{"model":["lora_dp",0],"clip":["lora_dp",1],"lora_name":"Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors","strength_model":2.0,"strength_clip":1.0}}
    nodes["neg"] = {"class_type":"CLIPTextEncode","inputs":{"text":NEG,"clip":["lora_size",1]}}

    for s in STAGES:
        clothes = f"{clothes_base}, {s['clothes']}"
        prompt = f"{char}, {clothes}, {MALE}, {DP}, {s['depth']}, cowgirl_position, girl_on_top, straddling, {s['hands']}, {s['eyes']}, {s['bed']}, {s['motion']}, {s['fluids']}, {s['hair']}, {s['sound']}, {s['expr']}, {ENV}"
        prompt = prompt.replace(", ,", ",").replace(" ,", ",").replace(",,", ",").strip(", ")

        nodes[f"e_{s['n']}"] = {"class_type":"EmptyLatentImage","inputs":{"width":1216,"height":832,"batch_size":1}}
        nodes[f"p_{s['n']}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":["lora_size",1]}}
        nodes[f"k_{s['n']}"] = {"class_type":"KSampler","inputs":{"seed":SEED,"steps":28,"cfg":4.0,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":["lora_size",0],"positive":[f"p_{s['n']}",0],"negative":["neg",0],"latent_image":[f"e_{s['n']}",0]}}
        nodes[f"d_{s['n']}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{s['n']}",0],"vae":["ckpt",2]}}
        nodes[f"s_{s['n']}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"virigia_{outfit_name}_{s['n']}","images":[f"d_{s['n']}",0]}}

    fpath = os.path.join(B, f"workflow_sequence_{outfit_name}.json")
    with open(fpath,"w",encoding="utf-8") as f:
        json.dump(nodes,f,indent=2,ensure_ascii=False)
    n = sum(1 for v in nodes.values() if v.get("class_type")=="SaveImage")
    print(f"✅ workflow_sequence_{outfit_name}.json -> {n} etapas")

print(f"\n🎯 20 imagenes | tematica non-con | dolor -> ahegao -> rota -> inconsciente")
