import json, os

B = r"E:/ComfyUI/characters/Stella_Sora"

# Checkpoint oficial actualizado
CKPT = "rinIllusionRNSFW_v30.safetensors"

NEG_BASE = (
    "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, "
    "extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, "
    "low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, "
    "bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, "
    "signature, watermark, holding mirror, red mirror, mirror"
)

LIGHTING_PRO = (
    "dimly_lit, dark_ambiance, (dark lighting:1.4), rim_lighting, sweat_gleam, "
    "glossy_skin, dramatic_shadows, depth_of_field, anime, masterpiece, best_quality"
)

MALE = "disembodied_penis, 2penises"
DP = "doublepen, vaginal, anal, double_penetration, both_holes"

POSES = {
    # 25 Poses (1024x1024)
    "cowgirl":           ("cowgirl_position, girl_on_top, straddling, front_view", 1024, 1024),
    "reverse_cowgirl":   ("reverse_cowgirl, girl_on_top, facing_away, looking_back_at_viewer, ass_view", 1024, 1024),
    "missionary":        ("missionary_position, on_back, legs_spread, front_view", 1024, 1024),
    "doggystyle":        ("doggystyle, from_behind, on_all_fours, arched_back, looking_back_at_viewer", 1024, 1024),
    "prone_bone":        ("prone_bone, lying, on_stomach, from_behind, ass_view", 1024, 1024),
    "spooning":          ("spooning, lying, on_side, from_behind, legs_together", 1024, 1024),
    "lotus":             ("lotus_position, legs_entwined, facing_each_other, front_view", 1024, 1024),
    "spitroast":         ("spitroast, on_all_fours, arched_back, oral, side_view", 1024, 1024),
    "desk_sex":          ("bent_over_desk, hands_on_desk, skirt_lift, from_behind, arched_back", 1024, 1024),
    "edge_of_bed":       ("edge_of_bed, lying_on_back, legs_spread_wide, hanging_legs, front_view", 1024, 1024),
    "double_vaginal":    ("double_vaginal, 2penises_in_one_hole, extreme_stretch, vaginal_penetration, front_view", 1024, 1024),
    "chair_straddle":    ("sitting_on_chair, straddling, lap_sit, thighs_spread, front_view", 1024, 1024),
    "pillow_face_plant": ("on_all_fours, face_pressed_in_pillow, ass_up, chest_on_bed, arched_back, from_behind", 1024, 1024),
    "cowgirl_bridge":    ("cowgirl_position, girl_on_top, leaning_back, hands_behind_back, arched_back, front_view", 1024, 1024),
    "against_glass":     ("pressed_against_glass, hands_on_glass, squished_breasts_against_glass, front_view", 1024, 1024),
    "mating_press":        ("mating_press, folded, shoulders_pressed, legs_on_shoulders, thigh_squish, front_view", 1024, 1024),
    "full_nelson":         ("full_nelson, nelson_position, lifted, legs_folded, front_view", 1024, 1024),
    "piledriver":          ("piledriver, inverted, legs_up, upside_down, front_view", 1024, 1024),
    "standing":            ("standing_sex, against_wall, held_up, legs_around_waist, front_view", 1024, 1024),
    "suspended":           ("suspended_congress, held_up, legs_around_waist, lifting, front_view", 1024, 1024),
    "standing_split":      ("standing_sex, one_leg_lifted, leg_on_shoulder, against_wall, standing_split, front_view", 1024, 1024),
    "wheelbarrow":         ("wheelbarrow_position, held_by_legs, hands_on_floor, arched_back, from_behind, looking_back_at_viewer", 1024, 1024),
    "jackknife":           ("jackknife_position, on_back, legs_folded_to_chest, extreme_flexibility, thighs_to_ears, front_view", 1024, 1024),
    "wall_pin":            ("pinned_against_wall, against_wall, one_leg_lifted, lifted_by_thigh, front_view", 1024, 1024),
    "inverted_suspension": ("suspended_upside_down, inverted, legs_spread_wide, hanging, front_view", 1024, 1024),
}

# Configuración Completa de Personajes
CHARACTERS = {
    # 1. Virigia
    "virigia_default": {
        "dir": os.path.join(B, "virigia_default"),
        "lora": "Stella-Virigia-v1.safetensors",
        "lora_strength": 1.0,
        "seed": 42424249,
        "char": "stell4virigiadef, 1girl, white hair, long hair, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, large breasts, collarbone, navel, hip_bones",
        "base_clothes": "white bonnet, multicolored hat, white cloak, frilled cloak, tassel, detached collar, black bowtie, red ribbon, neck ribbon, cleavage, black dress, grey dress, two-tone dress, hobble dress, long dress, ribbed dress, strapless, see-through dress, black bow, black gloves, lace-trimmed gloves, white pantyhose, ankle lace-up, high heels",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, dress_lift, pantyhose_pull, panties_aside",
            "02_primer_impacto": "dress_lift, torn_dress, torn_pantyhose, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    "virigia_bunny": {
        "dir": os.path.join(B, "virigia_bunny"),
        "lora": "Stella-Virigia-v1.safetensors",
        "lora_strength": 1.0,
        "seed": 42424250,
        "char": "stell4virigiabnuy, 1girl, white hair, long hair, half up braid, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, mole on hip, large breasts, collarbone, navel, hip_bones",
        "base_clothes": "bunny outfit, bunny ears, leotard, fishnet stockings, high heels",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, leotard_aside, fishnets_pull",
            "02_primer_impacto": "torn_leotard, torn_fishnets, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 2. Bernina Default
    "bernina_default": {
        "dir": os.path.join(B, "bernina_default"),
        "lora": "Stella-Bernina-v1.safetensors",
        "lora_strength": 1.0,
        "seed": 42424287,
        "char": "stell4berninadef, 1girl, pink hair, gradient hair, short hair with long locks, red hair ribbon, inverted cross, pink eyes, curled horns, low wings, (large breasts:1.3), collarbone, navel, hip_bones",
        "base_clothes": "black dress, gothic dress, detached collar, red necktie, frilled dress, black thighhighs",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, dress_lift, panties_aside",
            "02_primer_impacto": "dress_lift, torn_dress, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 3. Chitose (Default & Swimsuit)
    "chitose_default": {
        "dir": os.path.join(B, "chitose_default"),
        "lora": "Chitose_Dovellys.safetensors",
        "lora_strength": 1.0,
        "seed": 42424291,
        "char": "dvydfchitose, 1girl, purple eyes, bright pupils, white pupils, multicolored hair, colored inner hair, black hair, purple hair, ahoge, one side up, two-tone hair, hair ornament, huge breasts, collarbone, navel, hip_bones",
        "base_clothes": "black serafuku, black sailor collar, collared shirt, crop top overhang, purple ribbon, black skirt, bandaged leg",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, serafuku_lift, skirt_lift, panties_aside",
            "02_primer_impacto": "serafuku_lift, torn_shirt, broken_strap, exposed_breasts",
            "03_ritmo": "shredded_clothes, single_bare_shoulder, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    "chitose_swimsuit": {
        "dir": os.path.join(B, "chitose_swimsuit"),
        "lora": "Chitose_Dovellys.safetensors",
        "lora_strength": 1.0,
        "seed": 42424293,
        "char": "dvyswchitose, 1girl, purple eyes, bright pupils, white pupils, multicolored hair, colored inner hair, black hair, purple hair, high ponytail, huge breasts, collarbone, navel, hip_bones",
        "base_clothes": "side-tie bikini bottom, multi-strapped bikini bottom, string bikini, highleg bikini, o-ring bikini, o-ring top, front-tie top",
        "clothes_stages": {
            "01_resistencia": "intact_bikini, bikini_pull, string_bikini_aside",
            "02_primer_impacto": "untied_bikini_top, untied_bikini, exposed_breasts, broken_strap",
            "03_ritmo": "bikini_pulled_down, exposed_breasts, micro_bikini_displaced",
            "04_ahegao": "bikini_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_bikini, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 4. Freesia
    "freesia": {
        "dir": os.path.join(B, "freesia"),
        "lora": "Freesia_Stella-10.safetensors",
        "lora_strength": 1.0,
        "seed": 42424263,
        "char": "Freesia_Stella, 1girl, long hair, red eyes, side ponytail, grey hair, hair ornament, hair flower, white flower, sidelocks, blunt bangs, collarbone, navel, hip_bones",
        "base_clothes": "long sleeves, red shirt, collared shirt, double-breasted, buttons, pleated skirt, miniskirt, grey skirt, blue jacket, peaked cap, military hat, black headwear, military uniform, necktie, white pantyhose, thigh strap",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, clothes_lift, skirt_lift, panties_aside",
            "02_primer_impacto": "clothes_lift, torn_shirt, unbuttoned_shirt, exposed_breasts",
            "03_ritmo": "shredded_clothes, open_jacket, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 5. Nazuna
    "nazuna": {
        "dir": os.path.join(B, "nazuna"),
        "lora": "NazunaStellaSora_IXL.safetensors",
        "lora_strength": 1.0,
        "seed": 42424262,
        "char": "zzNazuna, 1girl, pink eyes, purple eyes, green hair, hair between eyes, long hair, multicolored hair, streaked hair, two-tone hair, white hair, twin braids, collarbone, navel, hip_bones",
        "base_clothes": "brown beret, sloose socks, sleeves past fingers, white dress, yellow jacket",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, dress_lift, panties_aside",
            "02_primer_impacto": "dress_lift, torn_dress, exposed_breasts",
            "03_ritmo": "shredded_clothes, open_jacket, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 6. Bastelina
    "bastelina": {
        "dir": os.path.join(B, "bastelina"),
        "lora": "bastelina_stellasora-v01.safetensors",
        "lora_strength": 1.0,
        "seed": 42424261,
        "char": "bastelina_stella, 1girl, folded braids, white hair, green eyes, collarbone, navel, hip_bones",
        "base_clothes": "white coat, white hat, white pencil dress, exposed shoulders, white pantyhose, white belt, multiple belts, gold trim, white bag, shoes",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, pencil_dress_lift, pantyhose_pull, panties_aside",
            "02_primer_impacto": "dress_lift, torn_pantyhose, torn_dress, exposed_breasts",
            "03_ritmo": "shredded_clothes, unbuttoned_coat, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 7. Noya (Default, Loungewear, Bikini)
    "noya_default": {
        "dir": os.path.join(B, "noya_default"),
        "lora": "Noya_stella_sora.safetensors",
        "lora_strength": 1.0,
        "seed": 42424264,
        "char": "stsrnya, 1girl, blonde hair, long hair, blue eyes, star-shaped pupils, single earring, gradient hair, half crown braid, streaked hair, ahoge, (large breasts:1.2), collarbone, navel, hip_bones",
        "base_clothes": "white dress, two-tone dress, high-low dress, jewelry, red ribbon, shirt, sideboob, navel, belt, pouch, white skirt, black frills, arm strap, black gloves, thighs, black footwear, boots",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, dress_lift, skirt_lift, panties_aside",
            "02_primer_impacto": "dress_lift, torn_dress, broken_strap, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    "noya_loungewear": {
        "dir": os.path.join(B, "noya_loungewear"),
        "lora": "Noya_stella_sora.safetensors",
        "lora_strength": 1.0,
        "seed": 42424265,
        "char": "stsrnya, 1girl, blonde hair, long hair, blue eyes, star-shaped pupils, single earring, gradient hair, half crown braid, streaked hair, ahoge, (large breasts:1.2), collarbone, navel, hip_bones",
        "base_clothes": "cropped shirt, yellow shirt, print shirt, drawstring, crop top overhang, bra strap, sleeves past wrists, long sleeves, bare shoulders, off shoulder, open jacket, white jacket, open clothes, midriff, short shorts, yellow shorts",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, shorts_pull, panties_aside",
            "02_primer_impacto": "lifted_shirt, unbuttoned_shorts, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    "noya_bikini": {
        "dir": os.path.join(B, "noya_bikini"),
        "lora": "Noya_stella_sora.safetensors",
        "lora_strength": 1.0,
        "seed": 42424266,
        "char": "stsrnya, 1girl, blonde hair, long hair, blue eyes, star-shaped pupils, single earring, gradient hair, half crown braid, streaked hair, ahoge, (large breasts:1.2), collarbone, navel, hip_bones",
        "base_clothes": "vertical-striped bikini, sunglasses on head, halterneck, aqua bikini, white bikini, black trim, white straps, thigh belt, bead necklace, star necklace, black straps, mismatched bikini, front-tie bikini top, wrist scrunchie, highleg bikini",
        "clothes_stages": {
            "01_resistencia": "intact_bikini, bikini_pull, string_bikini_aside",
            "02_primer_impacto": "untied_bikini_top, untied_bikini, exposed_breasts, broken_strap",
            "03_ritmo": "bikini_pulled_down, exposed_breasts, micro_bikini_displaced",
            "04_ahegao": "bikini_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_bikini, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 8. Flora
    "flora": {
        "dir": os.path.join(B, "flora"),
        "lora": "Flora_Stella_Sora.safetensors",
        "lora_strength": 1.0,
        "seed": 42424267,
        "char": "Flora, 1girl, collarbone, navel, hip_bones",
        "base_clothes": "Flora \\(stella sora\\), hat, elbow gloves, detached sleeves, pantyhose, dress, high heels",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, dress_lift, pantyhose_pull, panties_aside",
            "02_primer_impacto": "dress_lift, torn_dress, torn_pantyhose, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 9. Tyrant (Default, Pijama, Bikini)
    "tyrant": {
        "dir": os.path.join(B, "tyrant"),
        "lora": "tyrant_v2.safetensors",
        "lora_strength": 0.8,
        "seed": 42424268,
        "char": "tyrant, 1girl, loli, child, petite, grey hair, long hair, blue eyes, pointy ears, collarbone, navel, hip_bones",
        "base_clothes": "gloves, thighhighs, dress, white thighhighs, black gloves, hairband, blue dress, sleeveless, blue hairband, necktie, sleeveless dress, collared dress",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, dress_lift, panties_aside",
            "02_primer_impacto": "dress_lift, torn_dress, unbuttoned_collar, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    "tyrant_pijama": {
        "dir": os.path.join(B, "tyrant_pijama"),
        "lora": "tyrant_v2.safetensors",
        "lora_strength": 0.8,
        "seed": 42424269,
        "char": "tyrant, 1girl, loli, child, petite, grey hair, long hair, blue eyes, pointy ears, collarbone, navel, hip_bones",
        "base_clothes": "white dress, sleep mask, jewelry, sleeveless dress, necklace, mask on head, wrist scrunchie",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, dress_lift, panties_aside",
            "02_primer_impacto": "dress_lift, torn_dress, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    "tyrant_bikini": {
        "dir": os.path.join(B, "tyrant_bikini"),
        "lora": "tyrant_v2.safetensors",
        "lora_strength": 0.8,
        "seed": 42424270,
        "char": "tyrant, 1girl, loli, child, petite, grey hair, long hair, blue eyes, pointy ears, collarbone, navel, hip_bones",
        "base_clothes": "alternate costume, bikini, frilled bikini, single leg garter, highleg, bare legs, hairband",
        "clothes_stages": {
            "01_resistencia": "intact_bikini, bikini_pull, string_bikini_aside",
            "02_primer_impacto": "untied_bikini_top, untied_bikini, exposed_breasts, broken_strap",
            "03_ritmo": "bikini_pulled_down, exposed_breasts, micro_bikini_displaced",
            "04_ahegao": "bikini_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 10. Otoha (Wa-Maid, Ninja)
    "otoha": {
        "dir": os.path.join(B, "otoha"),
        "lora": "Otoha_stella_sora.safetensors",
        "lora_strength": 0.95,
        "seed": 42424271,
        "char": "stsroto, 1girl, long hair, half up braid, white hair, grey hair, mole, blue eyes, animal ear fluff, animal ears, fox ears, fox tail, (large breasts:1.2), collarbone, navel, hip_bones",
        "base_clothes": "wa maid, cleavage, long sleeves, detached sleeves, wide sleeves, frills, floral print, frilled apron, white apron, maid apron, blue kimono, sash, obi, purple gemstone, elbow gloves, white gloves, pleated skirt, long skirt, white thighhighs, maid headdress",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, kimono_lift, apron_lift, panties_aside",
            "02_primer_impacto": "kimono_lift, torn_kimono, torn_apron, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    "otoha_ninja": {
        "dir": os.path.join(B, "otoha_ninja"),
        "lora": "Otoha_stella_sora.safetensors",
        "lora_strength": 0.95,
        "seed": 42424272,
        "char": "stsroto, 1girl, long hair, half up braid, white hair, grey hair, mole, blue eyes, animal ear fluff, animal ears, fox ears, fox tail, (large breasts:1.2), collarbone, navel, hip_bones",
        "base_clothes": "ninja, black leotard, highleg leotard, sleeveless leotard, bare shoulders, cleavage cutout, sarashi, underbust, belt, red tassel, black gloves, elbow gloves, fingerless gloves, brown pantyhose, thighs",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, leotard_aside, pantyhose_pull",
            "02_primer_impacto": "torn_leotard, torn_sarashi, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 11. Amber
    "amber": {
        "dir": os.path.join(B, "amber"),
        "lora": "Amber_Stella_Sora.safetensors",
        "lora_strength": 1.0,
        "seed": 42424273,
        "char": "AmberSora, 1girl, black hair, yellow eyes, hair ornament, hood down, fingerless gloves, collarbone, navel, hip_bones",
        "base_clothes": "white dress, sideless dress, thighhighs, thigh boots",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, dress_lift, panties_aside",
            "02_primer_impacto": "dress_lift, torn_dress, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": "black cat"
    },
    # 12. Portia
    "portia": {
        "dir": os.path.join(B, "portia"),
        "lora": "Portia_Stella_Sora.safetensors",
        "lora_strength": 1.0,
        "seed": 42424274,
        "char": "Portia, 1girl, visor cap, long hair, green hair, mole under eye, mole under mouth, collarbone, navel, hip_bones",
        "base_clothes": "employee uniform, strap slip, button gap, waist apron",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, apron_lift, uniform_lift, panties_aside",
            "02_primer_impacto": "unbuttoned_uniform, torn_uniform, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 13. Laru
    "laru": {
        "dir": os.path.join(B, "laru"),
        "lora": "Laru_Dovellys.safetensors",
        "lora_strength": 1.0,
        "seed": 42424275,
        "char": "laru stella sora, 1girl, twintails, grey hair, purple eyes, skin fang, collarbone, navel, hip_bones",
        "base_clothes": "peaked cap, blue headwear, white dress, puffy long sleeves, blue cape, blue jacket, white thighhighs, blue footwear, high heels, high heel boots",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, dress_lift, panties_aside",
            "02_primer_impacto": "dress_lift, torn_dress, exposed_breasts",
            "03_ritmo": "shredded_clothes, open_jacket, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 14. Nazuka
    "nazuka": {
        "dir": os.path.join(B, "nazuka"),
        "lora": "Nazuka_Dovellys.safetensors",
        "lora_strength": 1.0,
        "seed": 42424276,
        "char": "nazuka stella sora, 1girl, black hair, red eyes, hairband, hair flower, hair ornament, collarbone, navel, hip_bones",
        "base_clothes": "short dress, orange dress, white shirt, blue cape, detached sleeves, frilled sleeves, white choker, frilled choker, frilled gloves, white gloves",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, dress_lift, panties_aside",
            "02_primer_impacto": "dress_lift, torn_dress, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": "staff, holding staff"
    },
    # 15. Kaede
    "kaede": {
        "dir": os.path.join(B, "kaede"),
        "lora": "Kaede_Dovellys.safetensors",
        "lora_strength": 1.0,
        "seed": 42424277,
        "char": "kaede stella sora, 1girl, pink hair, blue eyes, hair ornament, hair flower, collarbone, navel, hip_bones",
        "base_clothes": "white dress, fur collar, bare shoulders, puffy long sleeves, red shawl, yellow bow, black pantyhose, black footwear",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, dress_lift, pantyhose_pull, panties_aside",
            "02_primer_impacto": "dress_lift, torn_dress, torn_pantyhose, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 16. Tilia
    "tilia": {
        "dir": os.path.join(B, "tilia"),
        "lora": "Tilia_Dovellys.safetensors",
        "lora_strength": 1.0,
        "seed": 42424278,
        "char": "tilia stella sora, 1girl, blonde hair, red eyes, hairclip, hair ornament, ahoge, side ponytail, collarbone, navel, hip_bones",
        "base_clothes": "black shirt, white collar, shoulder armor, gauntlets, pauldrons, blue skirt, white thighhighs, armored boots, high heel boots",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, skirt_lift, panties_aside",
            "02_primer_impacto": "skirt_lift, torn_shirt, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 17. Canace
    "canace": {
        "dir": os.path.join(B, "canace"),
        "lora": "Canace_Dovellys.safetensors",
        "lora_strength": 1.0,
        "seed": 42424279,
        "char": "canace stella sora, 1girl, purple eyes, semi-rimless eyewear, purple hair, grey hair, hair ribbon, collarbone, navel, hip_bones",
        "base_clothes": "white dress, bare shoulders, red necktie, necktie between breasts, miniskirt, pleated skirt, white skirt",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, skirt_lift, panties_aside",
            "02_primer_impacto": "dress_lift, torn_dress, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 18. Caramel
    "caramel": {
        "dir": os.path.join(B, "caramel"),
        "lora": "Caramel_Dovellys.safetensors",
        "lora_strength": 1.0,
        "seed": 42424280,
        "char": "caramel stella sora, 1girl, animal ears, animal ear fluff, multicolored hair, blonde hair, twintails, drill hair, hair ribbon, collarbone, navel, hip_bones",
        "base_clothes": "black dress, purple jacket, striped clothes, spiked collar, black collar, frilled skirt, black skirt, asymmetrical legwear, mismatched legwear, fishnets, lace-trimmed legwear, striped thighhighs, o-ring thigh strap, knee boots, pink ribbon, purple ribbon",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, skirt_lift, panties_aside",
            "02_primer_impacto": "dress_lift, torn_dress, torn_fishnets, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 19. Cosette
    "cosette": {
        "dir": os.path.join(B, "cosette"),
        "lora": "Cosette_Dovellys.safetensors",
        "lora_strength": 1.0,
        "seed": 42424281,
        "char": "cosette stella sora, 1girl, green eyes, two-tone hair, multicolored hair, white hair, black hair, hair ornament, collarbone, navel, hip_bones",
        "base_clothes": "black dress, clothing cutout, stomach cutout, navel cutout, cleavage cutout, pelvic curtain, black cloak, blue cape, torn thighhighs, blue thighhighs, single thighhigh, asymmetrical legwear, leg tattoo, o-ring, o-ring bottom, thigh strap, black footwear",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, pelvic_curtain_aside, panties_aside",
            "02_primer_impacto": "torn_dress, torn_cutout, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": "bandage"
    },
    # 20. Fuyuka
    "fuyuka": {
        "dir": os.path.join(B, "fuyuka"),
        "lora": "FuyukaSS-10.safetensors",
        "lora_strength": 1.0,
        "seed": 42424282,
        "char": "fuyuka_ss, 1girl, long hair, red eyes, white hair, large breasts, collarbone, navel, hip_bones",
        "base_clothes": "long sleeves, black gloves, white shorts, yellow boots, gold gauntlets, cleavage cutout",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, shorts_pull, panties_aside",
            "02_primer_impacto": "unbuttoned_shorts, torn_top, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 21. Firefly
    "firefly": {
        "dir": os.path.join(B, "firefly"),
        "lora": "FFSS-10.safetensors",
        "lora_strength": 1.0,
        "seed": 42424283,
        "char": "ffstella, 1girl, short hair, huge ahoge, ahoge, red eyes, brown hair, streaked hair, white hair, collarbone, navel, hip_bones",
        "base_clothes": "scarf, white dress, sleeveless dress, black hairband, socks, loafers, bare shoulders",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, dress_lift, panties_aside",
            "02_primer_impacto": "dress_lift, torn_dress, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 22. Iris
    "iris": {
        "dir": os.path.join(B, "iris"),
        "lora": "IrisStellaSora_IXL.safetensors",
        "lora_strength": 1.0,
        "seed": 42424284,
        "char": "zzIris, 1girl, red eyes, purple hair, long hair, collarbone, navel, hip_bones",
        "base_clothes": "hair ornament, long sleeves, hat, white shirt, hairclip, puffy sleeves, black skirt, cape, black pantyhose, black headwear, beret, knee boots, juliet sleeves, red necktie, cross-laced footwear, high heel boots, high-waist skirt, lace-up boots",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, skirt_lift, pantyhose_pull, panties_aside",
            "02_primer_impacto": "skirt_lift, torn_shirt, torn_pantyhose, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 23. Mistique
    "mistique": {
        "dir": os.path.join(B, "mistique"),
        "lora": "MistiqueStellaSora_IXL.safetensors",
        "lora_strength": 1.0,
        "seed": 42424285,
        "char": "zzMistique, 1girl, orange eyes, orange hair, hair between eyes, long hair, twintails, collarbone, navel, hip_bones",
        "base_clothes": "witch, black dress, frilled dress, pink bow, purple bow, juliet sleeves, puffy sleeves, garter straps, witch hat, brooch",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, dress_lift, garter_pull, panties_aside",
            "02_primer_impacto": "dress_lift, torn_dress, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 24. Shia
    "shia": {
        "dir": os.path.join(B, "shia"),
        "lora": "Shia_Stella_Sora.safetensors",
        "lora_strength": 1.0,
        "seed": 42424286,
        "char": "shia, stella sora, 1girl, collarbone, navel, hip_bones",
        "base_clothes": "bunny girl, bunny ears, sailor collar, top, bikini, covered midriff",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, bikini_pull, string_bikini_aside",
            "02_primer_impacto": "untied_bikini, torn_top, exposed_breasts",
            "03_ritmo": "shredded_clothes, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_bikini, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
    # 25. Reisen
    "reisen": {
        "dir": os.path.join(B, "reisen"),
        "lora": "Reisen_ridge_-_Stella_Sora.safetensors",
        "lora_strength": 1.0,
        "seed": 42424288,
        "char": "ReisenStellaS, 1girl, blonde hair, antenna hair, very long hair, low-tied long hair, yellow eyes, thick thighs, large breasts, collarbone, navel, hip_bones",
        "base_clothes": "mask on head, plague doctor mask, goggles, goggles on head, jacket, black jacket, open jacket, bowtie, black bowtie, white shirt, underbust, brown belt, shorts, black shorts, white thighhighs, skindentation, black boots, fold-over boots",
        "clothes_stages": {
            "01_resistencia": "intact_clothing, skirt_lift, panties_aside",
            "02_primer_impacto": "skirt_lift, torn_shirt, exposed_breasts",
            "03_ritmo": "shredded_clothes, open_jacket, exposed_breasts",
            "04_ahegao": "shredded_clothes, clothes_falling_off, nude_top, exposed_breasts",
            "05_climax": "ruined_outfit, nude",
            "06_rota": "completely_nude, discarded_clothes",
            "07_inconsciente": "completely_nude",
        },
        "extra_neg": ""
    },
}

# 🎬 FÓRMULA DE 7 ETAPAS (Formato Doujinshi Pro con Encuadre Dinámico)
STAGES_7 = [
    {
        "n": "01_resistencia",
        "depth": "(imminent penetration:1.2), penis_on_pussy",
        "expr": "wide_eyes, trembling, furrowed_brow, nervous, screaming, open_mouth",
        "hands": "hands_pushing_away, skin_indentation",
        "phys": "mattress_indentation",
        "fluids": "sweat_drops, tears",
        "cam": "full_shot, front_view, (motion lines:1.2)",
    },
    {
        "n": "02_primer_impacto",
        "depth": "tip_in_pussy, first_insertion, stretching",
        "expr": "clenched_eyes, grimace, parted_lips, furrowed_brow, painful_expression, crying",
        "hands": "hands_gripping_sheets, white_knuckles",
        "phys": "breast_squish, hair_stuck_to_face, mattress_indentation",
        "fluids": "sweat, tears_streaming, saliva_string",
        "cam": "cowboy_shot, dutch_angle, (motion lines:1.3), (speed lines:1.2), sound_effects",
    },
    {
        "n": "03_ritmo",
        "depth": "(deep penetration:1.3), thrusting, (half insertion:1.2)",
        "expr": "half-closed_eyes, heavy_breathing, parted_lips, flushed_face, tear_tracks",
        "hands": "hands_above_head, clenched_hands",
        "phys": "bouncing_breasts, breast_squish, thigh_squish, flying_sweat_drops",
        "fluids": "sweat_drops, drooling, saliva_string, messy_tears",
        "cam": "medium_shot, dutch_angle, (motion lines:1.4), (speed lines:1.3), impact_lines, sound_effects, onomatopoeia",
    },
    {
        "n": "04_ahegao",
        "depth": "(deep penetration:1.4), full_penetration, (belly_bulge:1.1)",
        "expr": "ahegao, rolled_back_eyes, tongue_out, drooling, open_mouth, heavy_blush, forced_orgasm",
        "hands": "hands_above_head, fingers_twitching",
        "phys": "bouncing_breasts, belly_bulge, flying_sweat_drops",
        "fluids": "sweat_drops, tears_of_pleasure, excessive_drooling",
        "cam": "medium_close-up, dutch_angle, (motion lines:1.4), impact_lines, sound_effects, onomatopoeia",
    },
    {
        "n": "05_climax",
        "depth": "(deep penetration:1.5), (balls_deep:1.4), (belly_bulge:1.3)",
        "expr": "extreme_ahegao, heart_pupils, rolled_back_eyes, cross-eyed, tongue_out",
        "hands": "hands_above_head, trembling_fingers",
        "phys": "bouncing_breasts, belly_bulge, flying_sweat_drops, spasming",
        "fluids": "excessive_sweat, tears_of_pleasure, excessive_cum, creampie, cum_overflow",
        "cam": "cowboy_shot, dutch_angle, dynamic_angle, (motion lines:1.5), (speed lines:1.4), impact_lines, sound_effects, onomatopoeia, japanese_text_sound_effects",
    },
    {
        "n": "06_rota",
        "depth": "balls_deep, (gaping:1.3), belly_bulge",
        "expr": "blank_eyes, empty_eyes, thousand_yard_stare, slack-jawed, mouth_slightly_open, emotionless",
        "hands": "limp_arms, hands_resting",
        "phys": "spasming_legs, mattress_indentation, hair_stuck_to_face",
        "fluids": "excessive_cum, cum_drip, cum_overflow, drooling",
        "cam": "close-up, low_angle, depth_of_field",
    },
    {
        "n": "07_inconsciente",
        "depth": "after_sex, gaping, cum_pool",
        "expr": "closed_eyes, sleeping, relaxed_face, serene_expression, dried_tears",
        "hands": "limp_arms, relaxed_posture",
        "phys": "disheveled_hair, messy_bed, soaked_sheets",
        "fluids": "dried_tears, semen_on_face, semen_on_body, cum_pool",
        "cam": "wide_shot, overhead_view, high_angle, depth_of_field",
    },
]

def clean_tags(tags_str):
    raw = [t.strip() for t in tags_str.split(",") if t.strip()]
    seen = set()
    cleaned = []
    for t in raw:
        if t not in seen:
            seen.add(t)
            cleaned.append(t)
    return ", ".join(cleaned)

def build_single_pose_workflow(char_key, pose_name):
    c = CHARACTERS[char_key]
    pose_tags, width, height = POSES[pose_name]
    nodes = {}
    nodes["ckpt"] = {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}}
    nodes["clip_skip"] = {"class_type": "CLIPSetLastLayer", "inputs": {"clip": ["ckpt", 1], "stop_at_clip_layer": -2}}
    nodes["lora_char"] = {"class_type": "LoraLoader", "inputs": {"model": ["ckpt", 0], "clip": ["clip_skip", 0], "lora_name": c["lora"], "strength_model": c.get("lora_strength", 1.0), "strength_clip": 1.0}}
    nodes["lora_depth"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_char", 0], "clip": ["lora_char", 1], "lora_name": "penetration_depth.safetensors", "strength_model": 1.5, "strength_clip": 1.0}}
    nodes["lora_dp"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_depth", 0], "clip": ["lora_depth", 1], "lora_name": "doublepenetration_r1.safetensors", "strength_model": 1.0, "strength_clip": 1.0}}
    nodes["lora_size"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_dp", 0], "clip": ["lora_dp", 1], "lora_name": "Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors", "strength_model": 0.5, "strength_clip": 1.0}}
    nodes["neg"] = {"class_type": "CLIPTextEncode", "inputs": {"text": NEG_BASE + (f", {c['extra_neg']}" if c['extra_neg'] else ""), "clip": ["lora_size", 1]}}

    for s in STAGES_7:
        sn = s["n"]
        clothes_tag = c["clothes_stages"][sn]
        parts = [
            "score_9, score_8_up, source_anime, rating_explicit",
            c["char"],
            c["base_clothes"],
            clothes_tag,
            MALE,
            DP,
            s["depth"],
            pose_tags,
            s["hands"],
            s["phys"],
            s["expr"],
            s["fluids"],
            s["cam"],
            LIGHTING_PRO
        ]
        prompt = clean_tags(", ".join([p for p in parts if p]))
        nodes[f"e_{sn}"] = {"class_type": "EmptyLatentImage", "inputs": {"width": width, "height": height, "batch_size": 1}}
        nodes[f"p_{sn}"] = {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["lora_size", 1]}}
        nodes[f"k_{sn}"] = {"class_type": "KSampler", "inputs": {"seed": c["seed"], "steps": 40, "cfg": 6.0, "sampler_name": "euler_ancestral", "scheduler": "karras", "denoise": 1, "model": ["lora_size", 0], "positive": [f"p_{sn}", 0], "negative": ["neg", 0], "latent_image": [f"e_{sn}", 0]}}
        nodes[f"d_{sn}"] = {"class_type": "VAEDecode", "inputs": {"samples": [f"k_{sn}", 0], "vae": ["ckpt", 2]}}
        nodes[f"s_{sn}"] = {"class_type": "SaveImage", "inputs": {"filename_prefix": f"Stella_Sora/{char_key}/{pose_name}/{char_key}_{pose_name}_{sn}", "images": [f"d_{sn}", 0]}}
    return nodes

def build_master_workflow(char_key):
    c = CHARACTERS[char_key]
    nodes = {}
    nodes["ckpt"] = {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}}
    nodes["clip_skip"] = {"class_type": "CLIPSetLastLayer", "inputs": {"clip": ["ckpt", 1], "stop_at_clip_layer": -2}}
    nodes["lora_char"] = {"class_type": "LoraLoader", "inputs": {"model": ["ckpt", 0], "clip": ["clip_skip", 0], "lora_name": c["lora"], "strength_model": c.get("lora_strength", 1.0), "strength_clip": 1.0}}
    nodes["lora_depth"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_char", 0], "clip": ["lora_char", 1], "lora_name": "penetration_depth.safetensors", "strength_model": 1.5, "strength_clip": 1.0}}
    nodes["lora_dp"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_depth", 0], "clip": ["lora_depth", 1], "lora_name": "doublepenetration_r1.safetensors", "strength_model": 1.0, "strength_clip": 1.0}}
    nodes["lora_size"] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_dp", 0], "clip": ["lora_dp", 1], "lora_name": "Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors", "strength_model": 0.5, "strength_clip": 1.0}}
    nodes["neg"] = {"class_type": "CLIPTextEncode", "inputs": {"text": NEG_BASE + (f", {c['extra_neg']}" if c['extra_neg'] else ""), "clip": ["lora_size", 1]}}

    for pose_name, (pose_tags, width, height) in POSES.items():
        for s in STAGES_7:
            sn = s["n"]
            clothes_tag = c["clothes_stages"][sn]
            parts = [
                "score_9, score_8_up, source_anime, rating_explicit",
                c["char"],
                c["base_clothes"],
                clothes_tag,
                MALE,
                DP,
                s["depth"],
                pose_tags,
                s["hands"],
                s["phys"],
                s["expr"],
                s["fluids"],
                s["cam"],
                LIGHTING_PRO
            ]
            prompt = clean_tags(", ".join([p for p in parts if p]))
            key = f"{pose_name}_{sn}"
            nodes[f"e_{key}"] = {"class_type": "EmptyLatentImage", "inputs": {"width": width, "height": height, "batch_size": 1}}
            nodes[f"p_{key}"] = {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["lora_size", 1]}}
            nodes[f"k_{key}"] = {"class_type": "KSampler", "inputs": {"seed": c["seed"], "steps": 40, "cfg": 6.0, "sampler_name": "euler_ancestral", "scheduler": "karras", "denoise": 1, "model": ["lora_size", 0], "positive": [f"p_{key}", 0], "negative": ["neg", 0], "latent_image": [f"e_{key}", 0]}}
            nodes[f"d_{key}"] = {"class_type": "VAEDecode", "inputs": {"samples": [f"k_{key}", 0], "vae": ["ckpt", 2]}}
            nodes[f"s_{key}"] = {"class_type": "SaveImage", "inputs": {"filename_prefix": f"Stella_Sora/{char_key}/{pose_name}/{char_key}_{pose_name}_{sn}", "images": [f"d_{key}", 0]}}
    return nodes

def generate_for(char_key):
    c = CHARACTERS[char_key]
    os.makedirs(c["dir"], exist_ok=True)
    count = 0
    for pose_name in POSES:
        wf = build_single_pose_workflow(char_key, pose_name)
        fname = f"workflow_sequence_{pose_name}.json"
        fpath = os.path.join(c["dir"], fname)
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(wf, f, indent=2, ensure_ascii=False)
        count += 1

    master_wf = build_master_workflow(char_key)
    master_fpath = os.path.join(c["dir"], "workflow_master.json")
    with open(master_fpath, "w", encoding="utf-8") as f:
        json.dump(master_wf, f, indent=2, ensure_ascii=False)
    
    total_imgs = count * 7
    print(f"[OK] [{char_key}] 25 workflows individuales + workflow_master.json generados ({total_imgs} imgs)")

if __name__ == "__main__":
    for char in CHARACTERS:
        generate_for(char)
