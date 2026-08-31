import os
import json

# ==============================================================================
# 🏛️ MASTER BUILDER: MULTI-BRANCH TREE DELTA WORKFLOWS
# - Etapa 1: Punto Ancla Madre (Ropa Completa, Rostro, Cabello, Fondo Bloom, Denoise 1.0)
# - Etapa 2: Preliminares (Denoise 0.70, nace de 1)
# - Etapa 3: Inserción Vaginal Base (Denoise 0.70, nace de 1)
#     └─ Sub-Rama 03-Delta: Vaginal Intensa / Stretching (Denoise 0.68, nace de 3)
#     └─ Sub-Rama 03-Anal: Inserción Anal Intensa (Denoise 0.72, nace de 3)
# - Etapa 4: Clímax Regular (Denoise 0.70, nace de 1)
#     └─ Sub-Rama 04-Delta: Éxtasis Extremo & Deep Penetration Full (Sin balls, Denoise 0.75, nace de 4)
# - Etapa 5: Clímax Continuo & Orina / Squirt (Denoise 0.72, nace de 1)
#     └─ Sub-Rama 05-Delta: Clímax Máximo & Desborde Total (Denoise 0.75, nace de 5)
# ==============================================================================

TREE_BRANCHES = [
    # 1. ANCLA MADRE
    {
        "key": "01_ancla",
        "title": "⭐ Etapa 01: Punto Ancla Madre (Ropa Completa)",
        "parent": None,
        "undress_type": "full",
        "slider_weight": -0.40,
        "slider_tags": "closed_legs",
        "expr": "seductive_smile, light_blush, looking_at_viewer, flirting, parted_lips",
        "action": "solo, teasing_pose, standing, no_penetration",
        "male_tags": "1girl, solo",
        "cnet_strength": 0.60,
        "denoise": 1.0,
        "prefix": "01_ancla"
    },
    # 2. PRELIMINARES
    {
        "key": "02_preliminares",
        "title": "🌿 Etapa 02: Preliminares (Ropa Semi-Abierta)",
        "parent": None,
        "undress_type": "partial",
        "slider_weight": 0.25,
        "slider_tags": "teasing",
        "expr": "((lustful_expression:1.4)), blushing_deeply, heavy_breathing, parted_lips, moaning, anticipation",
        "action": "(imminent_penetration:1.2), tip_touching, thigh_contact, passionate_touch",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "cnet_strength": 0.55,
        "denoise": 1.0,
        "prefix": "02_preliminares"
    },
    # 3. INSERCION VAGINAL BASE
    {
        "key": "03_insercion_base",
        "title": "🌿 Etapa 03: Inserción Vaginal Base (penis_in_pussy)",
        "parent": None,
        "undress_type": "partial",
        "slider_weight": 0.50,
        "slider_tags": "(spread_pussy:1.2)",
        "expr": "((sweet_pain:1.3)), ((crying_with_pleasure:1.4)), blushing_deeply, open_mouth, heavy_breathing, panting",
        "action": "((penis_in_pussy:1.5)), ((deep_penetration:1.5)), (1penis:1.4), (erect_penis:1.3), (motion_lines:1.2)",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "cnet_strength": 0.55,
        "denoise": 1.0,
        "prefix": "03_insercion_base"
    },
    # 3B. AGARRE DE PECHOS & DEEP PENETRATION
    {
        "key": "03_breast_grab_deep",
        "title": "🍈 Rama 03-Busto: Agarre & Amasado de Pechos con Penetración Profunda (90% Adentro)",
        "parent": None,
        "undress_type": "partial",
        "slider_weight": 0.65,
        "slider_tags": "(spread_pussy:1.3), (stretched_pussy:1.3)",
        "expr": "((extreme_ahegao:1.5)), ((tongue_out:1.5)), ((drooling:1.4)), ((heart_pupils:1.4)), ((sweet_pain:1.3)), ((crying_with_pleasure:1.4))",
        "action": "((grabbing_breasts:1.5)), ((breasts_squeezed:1.5)), ((cleavage:1.4)), ((deep_penetration:1.6)), ((cervix_penetration:1.5)), ((penis_in_pussy:1.5)), (1penis:1.4), ((motion_lines:1.4))",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "cnet_strength": 0.50,
        "denoise": 1.0,
        "prefix": "03_breast_grab"
    },
    # 3C. MASTURBACION DE CLITORIS & PENETRACION TOTAL
    {
        "key": "03_clit_masturbation_deep",
        "title": "✨ Rama 03-Clítoris: Masturbación & Estimulación Clitoral con Pene 90% Adentro",
        "parent": None,
        "undress_type": "partial",
        "slider_weight": 0.70,
        "slider_tags": "(spread_pussy:1.3), (clitoris:1.3)",
        "expr": "((overstimulated:1.5)), ((extreme_ahegao:1.5)), ((tongue_out:1.5)), ((drooling:1.4)), ((heart_pupils:1.4)), (trembling:1.4)",
        "action": "((clitoral_stimulation:1.5)), ((masturbation_while_penetrated:1.5)), ((deep_penetration:1.6)), ((penis_in_pussy:1.5)), (1penis:1.4), ((motion_lines:1.4))",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "cnet_strength": 0.50,
        "denoise": 1.0,
        "prefix": "03_clit_masturb"
    },
    # 3D. SUB-RAMA 03-DELTA A (DEEP PENETRATION RÍTMICO)
    {
        "key": "03_delta_thrust",
        "title": "🔥 Rama 03-Delta A: Deep Penetration Rítmico & Mordisco de Labio (Líneas de Movimiento)",
        "parent": None,
        "undress_type": "partial",
        "slider_weight": 0.65,
        "slider_tags": "(spread_pussy:1.3), (stretched_pussy:1.3)",
        "expr": "((biting_lip:1.4)), ((sweet_pain:1.3)), ((crying_with_pleasure:1.4)), (blushing_deeply:1.4), (heavy_breathing:1.4)",
        "action": "((deep_penetration:1.6)), ((cervix_penetration:1.5)), ((penis_in_pussy:1.5)), (1penis:1.4), ((thrusting:1.5)), ((impact_lines:1.4)), ((motion_lines:1.5))",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "cnet_strength": 0.50,
        "denoise": 1.0,
        "prefix": "03_delta_thrust"
    },
    # 3E. SUB-RAMA 03-DELTA B (DEEP PENETRATION CERVICAL & LLANTO DE PLACER)
    {
        "key": "03_delta_crying_pleasure",
        "title": "🔥 Rama 03-Delta B: Deep Penetration Cervical & Llanto de Placer (Impact Lines)",
        "parent": None,
        "undress_type": "partial",
        "slider_weight": 0.70,
        "slider_tags": "(spread_pussy:1.3), (stretched_pussy:1.4)",
        "expr": "((extreme_ahegao:1.5)), ((tongue_out:1.4)), ((drooling:1.4)), ((crying_with_pleasure:1.5)), ((heart_pupils:1.4))",
        "action": "((cervix_penetration:1.6)), ((deep_penetration:1.6)), ((penis_in_pussy:1.5)), (1penis:1.4), ((impact_lines:1.5)), ((motion_lines:1.5))",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "cnet_strength": 0.48,
        "denoise": 1.0,
        "prefix": "03_delta_crying"
    },
    # 3F. SUB-RAMA 03-ANAL (INSERCION ANAL)
    {
        "key": "03_anal_insercion",
        "title": "🍑 Rama 03-Anal: Inserción Anal Intensa & Dolor-Placer (Líneas de Movimiento)",
        "parent": None,
        "undress_type": "partial",
        "slider_weight": 0.60,
        "slider_tags": "(anal_stretch:1.4)",
        "expr": "((extreme_ahegao:1.4)), ((tongue_out:1.4)), ((sweet_pain:1.4)), ((crying_with_pleasure:1.4)), (drooling:1.3)",
        "action": "((deep_anal_penetration:1.6)), ((penis_in_anal:1.5)), (1penis:1.4), (anal_stretch:1.4), ((motion_lines:1.4))",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "cnet_strength": 0.50,
        "denoise": 1.0,
        "prefix": "03_anal_insercion"
    },
    # 4. CLIMAX REGULAR
    {
        "key": "04_climax_regular",
        "title": "🌿 Etapa 04: Clímax Regular (penis_in_pussy)",
        "parent": None,
        "undress_type": "partial",
        "slider_weight": 0.65,
        "slider_tags": "(spread_pussy:1.2)",
        "expr": "((extreme_ahegao:1.4)), ((tongue_out:1.3)), ((heart_pupils:1.4)), (drooling:1.3), (crying_with_pleasure:1.3)",
        "action": "((deep_penetration:1.5)), ((penis_in_pussy:1.5)), ((creampie:1.4)), (1penis:1.4), (impact_lines:1.3)",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "cnet_strength": 0.55,
        "denoise": 1.0,
        "prefix": "04_climax_regular"
    },
    # 4B. AGARRE DE CADERAS & EMPUJE TOTAL
    {
        "key": "04_hip_grab_thrust",
        "title": "🍑 Rama 04-Caderas: Agarre Firme de Caderas & Empuje Cervical Máximo",
        "parent": None,
        "undress_type": "partial",
        "slider_weight": 0.70,
        "slider_tags": "(spread_pussy:1.3), (wide_hips:1.3)",
        "expr": "((extreme_ahegao:1.5)), ((tongue_out:1.5)), ((drooling:1.4)), ((biting_lip:1.3)), ((crying_with_pleasure:1.5))",
        "action": "((holding_hips:1.5)), ((deep_penetration:1.6)), ((cervix_penetration:1.5)), ((penis_in_pussy:1.5)), (1penis:1.4), ((impact_lines:1.5)), ((motion_lines:1.5))",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "cnet_strength": 0.50,
        "denoise": 1.0,
        "prefix": "04_hip_grab"
    },
    # 4C. SUB-RAMA 04-DELTA (EXTASIS EXTREMO - CERO BALLS)
    {
        "key": "04_delta_extremo",
        "title": "🔥 Rama 04-Delta: Éxtasis Extremo & Deep Penetration Full (Sin Balls)",
        "parent": None,
        "undress_type": "partial",
        "slider_weight": 0.75,
        "slider_tags": "(spread_pussy:1.3), (stretched_pussy:1.4)",
        "expr": "((extreme_ahegao:1.5)), ((tongue_out:1.5)), ((drooling:1.4)), ((heart_pupils:1.4)), ((sweet_pain:1.3)), ((crying_with_pleasure:1.4))",
        "action": "((deep_penetration:1.6)), ((cervix_penetration:1.5)), ((penis_in_pussy:1.5)), ((massive_creampie:1.4)), ((cum_overflow:1.4)), (1penis:1.4), (impact_lines:1.3)",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "cnet_strength": 0.45,
        "denoise": 1.0,
        "prefix": "04_delta_extremo"
    },
    # 5. CLIMAX CONTINUO & ORINA / SQUIRT
    {
        "key": "05_climax_orina",
        "title": "🌿 Etapa 05: Clímax Continuo & Orina / Squirt",
        "parent": None,
        "undress_type": "nude",
        "slider_weight": 0.65,
        "slider_tags": "(spread_pussy:1.2), (gaping:1.2)",
        "expr": "((extreme_ahegao:1.4)), ((tongue_out:1.4)), ((drooling:1.3)), ((crying_with_pleasure:1.4)), (sweat:1.3)",
        "action": "((deep_penetration:1.5)), ((penis_in_pussy:1.5)), (1penis:1.4), ((squirt:1.4)), ((peeing:1.3)), (puddle:1.2), (semen_drip:1.2)",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "cnet_strength": 0.55,
        "denoise": 1.0,
        "prefix": "05_climax_orina"
    },
    # 5B. SUB-RAMA 05-DELTA (CLIMAX MAXIMO & DESBORDE TOTAL)
    {
        "key": "05_delta_desborde",
        "title": "🔥 Rama 05-Delta: Clímax Máximo, Orina & Desborde Total",
        "parent": None,
        "undress_type": "nude",
        "slider_weight": 0.75,
        "slider_tags": "(spread_pussy:1.3), (gaping:1.3)",
        "expr": "((extreme_ahegao:1.5)), ((tongue_out:1.5)), ((drooling:1.5)), ((heart_pupils:1.4)), ((sweet_pain:1.3)), ((crying_with_pleasure:1.4))",
        "action": "((deep_penetration:1.6)), ((cervix_penetration:1.5)), ((penis_in_pussy:1.5)), (1penis:1.4), ((massive_creampie:1.4)), ((cum_overflow:1.4)), ((squirt:1.4)), ((peeing:1.3)), (puddle:1.3)",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "cnet_strength": 0.45,
        "denoise": 1.0,
        "prefix": "05_delta_desborde"
    }
]

CHARACTERS = {
    "elisia_make_drama": {
        "name": "elisia",
        "lora": "lora_elisia_make_drama.safetensors",
        "lora_strength": 0.80,
        "char": "elisia_(make_drama), elisia, make drama, demon girl, demon horns, curved horns, black horns, pointy ears, long hair, wavy hair, bangs, delicate face, curvy, hourglass figure, huge breasts, massive cleavage, narrow waist, wide hips, huge ass, big ass, bubble butt, thick thighs",
        "outfit": "open collar shirt, black crop top, high-waisted shorts, black shorts, belt, thong, visible thong, high heels, bare shoulders, bare midriff",
        "seed": 42424249
    },
    "isolda_lost_sword": {
        "name": "isolda",
        "lora": "lora_isolda_lost_sword.safetensors",
        "lora_strength": 0.80,
        "char": "isolda_(lost_sword), isolda, purple hair, short hair, hair between eyes, yellow eyes, small breasts",
        "outfit": "detailed dress, black dress, armor, pauldrons, breastplate, white cape, black gloves, thighhighs, boots, high heels",
        "seed": 42424249
    },
    "orihime_swimsuit": {
        "name": "orihime",
        "lora": "lora_orihime_swimsuit.safetensors",
        "lora_strength": 0.80,
        "char": "orihime inoue, bleach, bleach brave souls, long hair, orange hair, side braid, flower hair ornament, pearl chain, brown eyes, large breasts",
        "outfit": "swimsuit, bikini, pink swimsuit, frilled bikini, bows, bare shoulders, cleavage, navel, sandals, flip-flops",
        "seed": 42424249
    },
    "morgana_lost_sword": {
        "name": "morgana",
        "lora": "lora_morgana_lost_sword.safetensors",
        "lora_strength": 0.80,
        "char": "morgana_(lost_sword), morgana, mage, wizard, white hair, long hair, green eyes, flat chest, petite",
        "outfit": "black dress, black corset, bare shoulders, detailed fabric",
        "seed": 42424249
    },
    "ran_lost_sword": {
        "name": "ran",
        "lora": "lora_ran_lost_sword.safetensors",
        "lora_strength": 0.80,
        "char": "ran_(lost_sword), ran, oni, white hair, high ponytail, black horns, pointy ears, red eye makeup, hair between eyes, large breasts, mole on breast",
        "outfit": "japanese clothes, white kimono, single bare shoulder, chest sarashi, cleavage, black hakama, hakama skirt, fur scarf, manaita obi, white socks, platform sandals, geta",
        "seed": 42424249
    },
    "claire_lost_sword": {
        "name": "claire",
        "lora": "lora_claire_lost_sword.safetensors",
        "lora_strength": 0.75,
        "char": "claire_(lost_sword), claire, gray hair, long hair, blindfold, blindfold covering eyes, not visible eyes",
        "outfit": "nun, veil, white veil, nun habit, detailed white dress, gold accents",
        "seed": 42424249
    },
    "nelliel_parasol": {
        "name": "nelliel",
        "lora": "lora_nelliel_parasol.safetensors",
        "lora_strength": 0.80,
        "char": "nelliel_parasol, nelliel tu odelschwanck, bleach, bleach brave souls, green hair, green eyes, ram skull, hollow mask on head, facial mark, red facial stripe, large breasts, massive cleavage",
        "outfit": "open floral kimono robe, open kimono, floral kimono, bikini top, sarong, bare legs, bare shoulders",
        "seed": 42424249
    },
    "jennie_make_drama": {
        "name": "jennie",
        "lora": "lora_jennie_make_drama.safetensors",
        "lora_strength": 0.80,
        "char": "jennie_(make_drama), jennie, make drama, teal hair, cyan hair, long hair, ponytail, white ribbon, hair ribbon, bangs, parted bangs, golden eyes, yellow eyes, amber eyes",
        "outfit": "business attire, office lady, white collared shirt, black blazer, black suit, black pencil skirt, dark pantyhose, black high heels",
        "seed": 42424249
    },
    "marcia_make_drama": {
        "name": "marcia",
        "lora": "lora_marcia_make_drama.safetensors",
        "lora_strength": 0.80,
        "char": "marcia_(make_drama), marcia, make drama, pink hair, high twintails, twintails, long hair, heart ahoge, purple eyes, fang, smirking, cute, petite, chubby thighs, barcode on thigh, bandaid on knee",
        "outfit": "futuristic bodysuit, highleg leotard, black and white bodysuit, cleavage cutout, white jacket, crop jacket, detached jacket, black gloves, asymmetric legwear, black thighhigh, single thighhigh, garter strap, mechanical boots",
        "seed": 42424249
    },
    "nelliel_heart": {
        "name": "nelliel",
        "lora": "lora_nelliel_heart.safetensors",
        "lora_strength": 0.80,
        "char": "nelliel_swimsuit, nelliel tu odelschwanck, bleach, bleach brave souls, tan, dark skin, green hair, wavy hair, long hair, green eyes, ram skull, hollow mask on head, facial mark, red facial stripe, large breasts, massive cleavage, wide hips",
        "outfit": "white bikini, halterneck bikini top, side-tie bikini bottom, yellow sarong, yellow pareo, floral pareo, beaded necklace, flower on waist",
        "seed": 42424249
    }
}

NEG_PROMPT_UNIFIED = (
    "2boys, 2men, 2penises, two_penises, multiple_penises, extra_penis, duplicate_penis, group_sex, threesome, gangbang, "
    "shallow_penetration, half_inserted, mostly_outside, detached_penis, penis_outside, tip_only, partial_insertion, "
    "fear, scared, terrified, horrified, fear_expression, sad, sadness, sorrow, crying_in_sadness, crying_in_fear, frowning, angry, disgusted, distress, rape, resistance, unwilling, "
    "color_shift, color_drift, hue_shift, tint, color_cast, washed_out_colors, dull_colors, oversaturated, desaturated, grayscale, sepia, monochrome, yellow_tint, green_tint, purple_tint, "
    "inconsistent_lighting, mismatched_skin_tone, blown_out_highlights, overexposed, underexposed, harsh_shadows, "
    "worst quality, low quality, bad anatomy, bad hands, missing fingers, extra fingers, "
    "clothed male, male clothes, shirt on male, pants on male, underwear on male, boxer shorts, male underwear, "
    "sex_toy, dildo, vibrator, strap-on, harness, artificial penis, glass dildo, silicone toy, machine, tentacles, "
    "disembodied_penis, floating penis, floating limbs, floating arms, floating legs, "
    "fused fingers, too many fingers, mutated hands, poorly drawn hands, poorly drawn face, "
    "fused limbs, bad proportions, unnatural body, distorted body, duplicate limbs, overlapping limbs, "
    "extra arms, extra legs, poorly drawn eyes, cross-eyed, asymmetrical eyes, "
    "detailed background, sharp background, complex background, bright background, white background, flat lighting, sunny, lowres"
)

QUALITY_PREFIX = "score_9, score_8_up, score_7_up, source_anime, rating_explicit, masterpiece, best quality, highly detailed, perfect anatomy, accurate anatomy, detailed eyes, detailed face"
ATMOS_TAGS = "(vibrant anime colors:1.3), (rich color palette:1.2), (consistent color tone:1.3), (clean anime coloring:1.3), (smooth anime shading:1.2), (natural skin tone:1.2), (soft lighting:1.2), (balanced contrast:1.2), (blurry background:1.4), (depth of field:1.3), dark background, dim lighting"

def clean_tags(tags_str):
    raw = [t.strip() for t in tags_str.split(",") if t.strip()]
    seen = set()
    out = []
    for t in raw:
        tl = t.lower()
        if tl not in seen:
            seen.add(tl)
            out.append(t)
    return ", ".join(out)

def get_outfit_tags(char_cfg, undress_type):
    full_outfit = char_cfg["outfit"]
    if undress_type == "full":
        return full_outfit
    elif undress_type == "partial":
        return f"{full_outfit}, clothing_undone, breasts_exposed, clothes_around_waist, partially_unbuttoned, panties_pulled_aside, bare_breasts, bare_pussy"
    elif undress_type == "nude":
        return "completely nude, naked, bare breasts, bare nipples, bare pussy, nipples, areolae, navel, discarded clothes"
    return full_outfit

def generate_multi_branch_tree(char_key, char_cfg):
    nodes = {}
    node_id = 1
    
    # 1. Base Checkpoint
    nodes[str(node_id)] = {
        "class_type": "CheckpointLoaderSimple",
        "inputs": {"ckpt_name": "illustrious-xl-v0.1.safetensors"},
        "_meta": {"title": "Base Model (Illustrious XL)"}
    }
    ckpt_id = node_id
    node_id += 1
    
    # 2. LoRA 1: Personaje (0.80)
    nodes[str(node_id)] = {
        "class_type": "LoraLoader",
        "inputs": {
            "model": [str(ckpt_id), 0],
            "clip": [str(ckpt_id), 1],
            "lora_name": char_cfg["lora"],
            "strength_model": char_cfg["lora_strength"],
            "strength_clip": 0.80
        },
        "_meta": {"title": f"LoRA 1: {char_cfg['name'].capitalize()}"}
    }
    char_lora_id = node_id
    node_id += 1
    
    # 3. LoRA 2: BBC Interracial (1.00)
    nodes[str(node_id)] = {
        "class_type": "LoraLoader",
        "inputs": {
            "model": [str(char_lora_id), 0],
            "clip": [str(char_lora_id), 1],
            "lora_name": "lora_bbc_interracial.safetensors",
            "strength_model": 1.00,
            "strength_clip": 1.00
        },
        "_meta": {"title": "LoRA 2: BBC Interracial"}
    }
    concept_lora_id = node_id
    node_id += 1
    
    # 4. CLIPSetLastLayer (stop_at_clip_layer: -2 / CLIP Skip 2)
    nodes[str(node_id)] = {
        "class_type": "CLIPSetLastLayer",
        "inputs": {
            "clip": [str(concept_lora_id), 1],
            "stop_at_clip_layer": -2
        },
        "_meta": {"title": "CLIP Set Last Layer (CLIP Skip -2)"}
    }
    clip_skip_id = node_id
    node_id += 1
    
    # 5. ControlNet Depth Loader (controlnet-depth-sdxl-1.0.safetensors)
    nodes[str(node_id)] = {
        "class_type": "ControlNetLoader",
        "inputs": {"control_net_name": "controlnet-depth-sdxl-1.0.safetensors"},
        "_meta": {"title": "ControlNet Depth Loader (SDXL)"}
    }
    cnet_loader_id = node_id
    node_id += 1
    
    # 6. LoadImage (Manual Pose Reference)
    nodes[str(node_id)] = {
        "class_type": "LoadImage",
        "inputs": {"image": "reference_custom_pose.png", "upload": "image"},
        "_meta": {"title": "📥 Cargar Imagen de Pose (Referencia 3D)"}
    }
    manual_load_id = node_id
    node_id += 1
    
    # 7. MiDaS Depth Preprocessor (bg_threshold: 0.01, resolution: 1024) -> RAÍZ ÚNICA DEL MAPA 3D
    nodes[str(node_id)] = {
        "class_type": "MiDaS-DepthMapPreprocessor",
        "inputs": {
            "image": [str(manual_load_id), 0],
            "a": 6.28,
            "bg_threshold": 0.01,
            "resolution": 1024
        },
        "_meta": {"title": "⚙️ Depth Preprocessor (Mapa 3D Raíz Única 1024)"}
    }
    manual_depth_id = node_id
    node_id += 1
    
    # 7B. Vista Previa del Mapa 3D
    nodes[str(node_id)] = {
        "class_type": "PreviewImage",
        "inputs": {
            "images": [str(manual_depth_id), 0]
        },
        "_meta": {"title": "👁️ Mapa 3D Generado (Clic Derecho -> Guardar)"}
    }
    node_id += 1
    
    # 8. Negative Prompt Master
    nodes[str(node_id)] = {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [str(clip_skip_id), 0],
            "text": NEG_PROMPT_UNIFIED
        },
        "_meta": {"title": "Negative Prompt Master (Anti-Ropa / Anti-Juguetes)"}
    }
    neg_id = node_id
    node_id += 1
    
    # 9. Empty Latent para el Ancla Raíz (832x1216 Vertical SDXL)
    nodes[str(node_id)] = {
        "class_type": "EmptyLatentImage",
        "inputs": {"width": 832, "height": 1216, "batch_size": 1},
        "_meta": {"title": "Base Latent Etapa 1 (832x1216 Vertical SDXL)"}
    }
    initial_latent_id = node_id
    node_id += 1
    
    char_tags = char_cfg["char"]
    base_seed = char_cfg["seed"]
    
    # Diccionario para almacenar el KSampler ID de cada rama para alimentar a sus hijas
    branch_ksamplers = {}
    
    for b_idx, branch in enumerate(TREE_BRANCHES, 1):
        b_key = branch["key"]
        is_delta = "delta" in branch["prefix"] or "anal" in branch["prefix"]
        
        outfit = get_outfit_tags(char_cfg, branch["undress_type"])
        male_tags = branch["male_tags"]
        stg_prompt = clean_tags(f"{QUALITY_PREFIX}, {char_tags}, {male_tags}, {outfit}, {ATMOS_TAGS}, {branch['slider_tags']}, {branch['expr']}, {branch['action']}")
        
        # Slider LoRA
        nodes[str(node_id)] = {
            "class_type": "LoraLoader",
            "inputs": {
                "model": [str(concept_lora_id), 0],
                "clip": [str(clip_skip_id), 0],
                "lora_name": "pussy_adjuster_xl.safetensors",
                "strength_model": branch["slider_weight"],
                "strength_clip": branch["slider_weight"]
            },
            "_meta": {"title": f"Slider [{branch['prefix']}] ({branch['slider_weight']:+.2f})"}
        }
        stg_slider_id = node_id
        node_id += 1
        
        # Positive Prompt (Caja de Texto Editable Pura)
        prompt_title = f"📝 [DELTA PROMPT {branch['prefix'].upper()}]: (Solo Tags Delta / Modificadores)" if is_delta else f"📝 [PROMPT {branch['prefix'].upper()}]: {branch['title']}"
        
        nodes[str(node_id)] = {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "clip": [str(stg_slider_id), 1],
                "text": stg_prompt
            },
            "_meta": {"title": prompt_title}
        }
        stg_pos_id = node_id
        node_id += 1
        
        # ControlNet Apply Advanced
        nodes[str(node_id)] = {
            "class_type": "ControlNetApplyAdvanced",
            "inputs": {
                "positive": [str(stg_pos_id), 0],
                "negative": [str(neg_id), 0],
                "control_net": [str(cnet_loader_id), 0],
                "image": [str(manual_depth_id), 0],
                "strength": branch["cnet_strength"],
                "start_percent": 0.0,
                "end_percent": 0.70
            },
            "_meta": {"title": f"Apply ControlNet 3D [{branch['prefix']}]"}
        }
        stg_cnet_applied_id = node_id
        node_id += 1
        
        # Determinar Latente de Entrada (EmptyLatent si es Ancla, o el KSampler de su Padre)
        parent_key = branch["parent"]
        if parent_key is None:
            in_latent = [str(initial_latent_id), 0]
        else:
            parent_ksampler = branch_ksamplers[parent_key]
            in_latent = [str(parent_ksampler), 0]
            
        # KSampler
        nodes[str(node_id)] = {
            "class_type": "KSampler",
            "inputs": {
                "model": [str(stg_slider_id), 0],
                "positive": [str(stg_cnet_applied_id), 0],
                "negative": [str(stg_cnet_applied_id), 1],
                "latent_image": in_latent,
                "seed": base_seed,
                "control_after_generate": "fixed",
                "steps": 24,
                "cfg": 5.0,
                "sampler_name": "euler_ancestral",
                "scheduler": "karras",
                "denoise": branch["denoise"]
            },
            "_meta": {"title": f"KSampler [{branch['prefix']}]"}
        }
        branch_ksamplers[b_key] = node_id
        stg_ksampler_id = node_id
        node_id += 1
        
        # VAEDecode Estándar
        nodes[str(node_id)] = {
            "class_type": "VAEDecode",
            "inputs": {
                "samples": [str(stg_ksampler_id), 0],
                "vae": [str(ckpt_id), 2]
            },
            "_meta": {"title": f"VAE Decode [{branch['prefix']}]"}
        }
        stg_vae_id = node_id
        node_id += 1
        
        # SaveImage
        nodes[str(node_id)] = {
            "class_type": "SaveImage",
            "inputs": {
                "images": [str(stg_vae_id), 0],
                "filename_prefix": f"{char_cfg['name']}/tree_delta/{branch['prefix']}"
            },
            "_meta": {"title": f"Save [{branch['prefix']}]"}
        }
        node_id += 1

    return nodes

def main():
    base_dir = r"E:\ComfyUI\characters"
    print("Generating Master Multi-Branch Tree Delta Workflows for all 10 characters...")
    
    for char_key, char_cfg in CHARACTERS.items():
        char_name = char_cfg["name"]
        char_dir = os.path.join(base_dir, char_key)
        os.makedirs(char_dir, exist_ok=True)
        
        wf_nodes = generate_multi_branch_tree(char_key, char_cfg)
        json_path = os.path.join(char_dir, f"workflow_{char_name}_manual_tree_delta.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(wf_nodes, f, indent=2)
        print(f"  [OK] Created Tree Delta JSON: {json_path}")

    print("\nAll Tree Delta workflows generated successfully!")

if __name__ == "__main__":
    main()
