"""
==============================================================================
BUILDER: Pure Prompt Multi-Stage Suite (SIN ControlNet)
==============================================================================
Genera flujos de 10 etapas/ramas basados 100% en Prompts Puros + LoRA de Personaje
+ Slider de Dilatación (Pussy Adjuster) + KSamplers Ultra-Rápidos.

Características:
- CERO dependencias de imágenes de referencia o ControlNet.
- 10 Etapas completas con análisis anatómico profundo (90% adentro, 10% visible).
- Expresiones de máximo éxtasis / ahegao con lengua afuera, pupilas de corazón y lágrimas.
- CERO menciones de testículos / balls.
- Cero deriva de color, máxima nitidez nativa en 832x1216.
==============================================================================
"""

import os
import json

PURE_BRANCHES = [
    # 1. ANCLA MADRE
    {
        "key": "01_ancla",
        "title": "⭐ Etapa 01: Retrato Ancla (Ropa Completa)",
        "undress_type": "full",
        "slider_weight": -0.40,
        "slider_tags": "closed_legs",
        "expr": "seductive_smile, light_blush, looking_at_viewer, flirting, parted_lips",
        "action": "solo, teasing_pose, standing, no_penetration",
        "male_tags": "1girl, solo",
        "prefix": "01_ancla"
    },
    # 2. PRELIMINARES
    {
        "key": "02_preliminares",
        "title": "🌿 Etapa 02: Preliminares (Ropa Semi-Abierta)",
        "undress_type": "partial",
        "slider_weight": 0.25,
        "slider_tags": "teasing",
        "expr": "((lustful_expression:1.4)), blushing_deeply, heavy_breathing, parted_lips, moaning, anticipation",
        "action": "(imminent_penetration:1.2), tip_touching, thigh_contact, passionate_touch",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "prefix": "02_preliminares"
    },
    # 3. INSERCION VAGINAL BASE
    {
        "key": "03_insercion_base",
        "title": "🌿 Etapa 03: Inserción Vaginal Base (penis_in_pussy)",
        "undress_type": "partial",
        "slider_weight": 0.50,
        "slider_tags": "(spread_pussy:1.2)",
        "expr": "((sweet_pain:1.3)), ((crying_with_pleasure:1.4)), blushing_deeply, open_mouth, heavy_breathing, panting",
        "action": "((penis_in_pussy:1.5)), ((deep_penetration:1.5)), (1penis:1.4), (erect_penis:1.3), (motion_lines:1.2)",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "prefix": "03_insercion_base"
    },
    # 3B. AGARRE DE PECHOS & DEEP PENETRATION
    {
        "key": "03_breast_grab_deep",
        "title": "🍈 Rama 03-Busto: Agarre & Amasado de Pechos con Penetración Profunda (90% Adentro)",
        "undress_type": "partial",
        "slider_weight": 0.65,
        "slider_tags": "(spread_pussy:1.3), (stretched_pussy:1.3)",
        "expr": "((extreme_ahegao:1.5)), ((tongue_out:1.5)), ((drooling:1.4)), ((heart_pupils:1.4)), ((sweet_pain:1.3)), ((crying_with_pleasure:1.4))",
        "action": "((grabbing_breasts:1.5)), ((breasts_squeezed:1.5)), ((cleavage:1.4)), ((deep_penetration:1.6)), ((cervix_penetration:1.5)), ((penis_in_pussy:1.5)), (1penis:1.4), ((motion_lines:1.4))",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "prefix": "03_breast_grab"
    },
    # 3C. MASTURBACION DE CLITORIS & PENETRACION TOTAL
    {
        "key": "03_clit_masturbation_deep",
        "title": "✨ Rama 03-Clítoris: Masturbación & Estimulación Clitoral con Pene 90% Adentro",
        "undress_type": "partial",
        "slider_weight": 0.70,
        "slider_tags": "(spread_pussy:1.3), (clitoris:1.3)",
        "expr": "((overstimulated:1.5)), ((extreme_ahegao:1.5)), ((tongue_out:1.5)), ((drooling:1.4)), ((heart_pupils:1.4)), (trembling:1.4)",
        "action": "((clitoral_stimulation:1.5)), ((masturbation_while_penetrated:1.5)), ((deep_penetration:1.6)), ((penis_in_pussy:1.5)), (1penis:1.4), ((motion_lines:1.4))",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "prefix": "03_clit_masturb"
    },
    # 3D. SUB-RAMA 03-DELTA A (DEEP PENETRATION RÍTMICO)
    {
        "key": "03_delta_thrust",
        "title": "🔥 Rama 03-Delta A: Deep Penetration Rítmico & Mordisco de Labio (Líneas de Movimiento)",
        "undress_type": "partial",
        "slider_weight": 0.65,
        "slider_tags": "(spread_pussy:1.3), (stretched_pussy:1.3)",
        "expr": "((biting_lip:1.4)), ((sweet_pain:1.3)), ((crying_with_pleasure:1.4)), (blushing_deeply:1.4), (heavy_breathing:1.4)",
        "action": "((deep_penetration:1.6)), ((cervix_penetration:1.5)), ((penis_in_pussy:1.5)), (1penis:1.4), ((thrusting:1.5)), ((impact_lines:1.4)), ((motion_lines:1.5))",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "prefix": "03_delta_thrust"
    },
    # 3E. SUB-RAMA 03-DELTA B (DEEP PENETRATION CERVICAL & LLANTO DE PLACER)
    {
        "key": "03_delta_crying_pleasure",
        "title": "🔥 Rama 03-Delta B: Deep Penetration Cervical & Llanto de Placer (Impact Lines)",
        "undress_type": "partial",
        "slider_weight": 0.70,
        "slider_tags": "(spread_pussy:1.3), (stretched_pussy:1.4)",
        "expr": "((extreme_ahegao:1.5)), ((tongue_out:1.4)), ((drooling:1.4)), ((crying_with_pleasure:1.5)), ((heart_pupils:1.4))",
        "action": "((cervix_penetration:1.6)), ((deep_penetration:1.6)), ((penis_in_pussy:1.5)), (1penis:1.4), ((impact_lines:1.5)), ((motion_lines:1.5))",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "prefix": "03_delta_crying"
    },
    # 3F. SUB-RAMA 03-ANAL (INSERCION ANAL)
    {
        "key": "03_anal_insercion",
        "title": "🍑 Rama 03-Anal: Inserción Anal Intensa & Dolor-Placer (Líneas de Movimiento)",
        "undress_type": "partial",
        "slider_weight": 0.60,
        "slider_tags": "(anal_stretch:1.4)",
        "expr": "((extreme_ahegao:1.4)), ((tongue_out:1.4)), ((sweet_pain:1.4)), ((crying_with_pleasure:1.4)), (drooling:1.3)",
        "action": "((deep_anal_penetration:1.6)), ((penis_in_anal:1.5)), (1penis:1.4), (anal_stretch:1.4), ((motion_lines:1.4))",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "prefix": "03_anal_insercion"
    },
    # 4. CLIMAX REGULAR
    {
        "key": "04_climax_regular",
        "title": "🌿 Etapa 04: Clímax Regular (penis_in_pussy)",
        "undress_type": "partial",
        "slider_weight": 0.65,
        "slider_tags": "(spread_pussy:1.2)",
        "expr": "((extreme_ahegao:1.4)), ((tongue_out:1.3)), ((heart_pupils:1.4)), (drooling:1.3), (crying_with_pleasure:1.3)",
        "action": "((deep_penetration:1.5)), ((penis_in_pussy:1.5)), ((creampie:1.4)), (1penis:1.4), (impact_lines:1.3)",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "prefix": "04_climax_regular"
    },
    # 4B. AGARRE DE CADERAS & EMPUJE TOTAL
    {
        "key": "04_hip_grab_thrust",
        "title": "🍑 Rama 04-Caderas: Agarre Firme de Caderas & Empuje Cervical Máximo",
        "undress_type": "partial",
        "slider_weight": 0.70,
        "slider_tags": "(spread_pussy:1.3), (wide_hips:1.3)",
        "expr": "((extreme_ahegao:1.5)), ((tongue_out:1.5)), ((drooling:1.4)), ((biting_lip:1.3)), ((crying_with_pleasure:1.5))",
        "action": "((holding_hips:1.5)), ((deep_penetration:1.6)), ((cervix_penetration:1.5)), ((penis_in_pussy:1.5)), (1penis:1.4), ((impact_lines:1.5)), ((motion_lines:1.5))",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "prefix": "04_hip_grab"
    },
    # 4C. SUB-RAMA 04-DELTA (EXTASIS EXTREMO - CERO BALLS)
    {
        "key": "04_delta_extremo",
        "title": "🔥 Rama 04-Delta: Éxtasis Extremo & Deep Penetration Full (Sin Balls)",
        "undress_type": "partial",
        "slider_weight": 0.75,
        "slider_tags": "(spread_pussy:1.3), (stretched_pussy:1.4)",
        "expr": "((extreme_ahegao:1.5)), ((tongue_out:1.5)), ((drooling:1.4)), ((heart_pupils:1.4)), ((sweet_pain:1.3)), ((crying_with_pleasure:1.4))",
        "action": "((deep_penetration:1.6)), ((cervix_penetration:1.5)), ((penis_in_pussy:1.5)), ((massive_creampie:1.4)), ((cum_overflow:1.4)), (1penis:1.4), (impact_lines:1.3)",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "prefix": "04_delta_extremo"
    },
    # 5. CLIMAX CONTINUO & ORINA / SQUIRT
    {
        "key": "05_climax_orina",
        "title": "🌿 Etapa 05: Clímax Continuo & Orina / Squirt",
        "undress_type": "nude",
        "slider_weight": 0.65,
        "slider_tags": "(spread_pussy:1.2), (gaping:1.2)",
        "expr": "((extreme_ahegao:1.4)), ((tongue_out:1.4)), ((drooling:1.3)), ((crying_with_pleasure:1.4)), (sweat:1.3)",
        "action": "((deep_penetration:1.5)), ((penis_in_pussy:1.5)), (1penis:1.4), ((squirt:1.4)), ((peeing:1.3)), (puddle:1.2), (semen_drip:1.2)",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
        "prefix": "05_climax_orina"
    },
    # 5B. SUB-RAMA 05-DELTA (CLIMAX MAXIMO & DESBORDE TOTAL)
    {
        "key": "05_delta_desborde",
        "title": "🔥 Rama 05-Delta: Clímax Máximo, Orina & Desborde Total",
        "undress_type": "nude",
        "slider_weight": 0.75,
        "slider_tags": "(spread_pussy:1.3), (gaping:1.3)",
        "expr": "((extreme_ahegao:1.5)), ((tongue_out:1.5)), ((drooling:1.5)), ((heart_pupils:1.4)), ((sweet_pain:1.3)), ((crying_with_pleasure:1.4))",
        "action": "((deep_penetration:1.6)), ((cervix_penetration:1.5)), ((penis_in_pussy:1.5)), (1penis:1.4), ((massive_creampie:1.4)), ((cum_overflow:1.4)), ((squirt:1.4)), ((peeing:1.3)), (puddle:1.3)",
        "male_tags": "1girl, 1man, naked_man, dark-skinned_male, muscular_male, faceless_male",
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
        "char": "isolda_(lost_sword), isolda, lost sword, blonde hair, long hair, very long hair, braided hair, single braid, golden eyes, yellow eyes, looking at viewer, elegant, delicate face, slender, medium breasts, narrow waist, toned body",
        "outfit": "white dress, backless dress, highleg dress, side slit, cleavage cutout, gold trim, ornate trim, bare shoulders, collarbone, bare back, white high heels",
        "seed": 42424249
    },
    "orihime_swimsuit": {
        "name": "orihime",
        "lora": "lora_orihime_swimsuit.safetensors",
        "lora_strength": 0.80,
        "char": "orihime_swimsuit, orihime inoue, bleach, bleach brave souls, orange hair, long hair, hair pins, grey eyes, huge breasts, massive cleavage, wide hips, thick thighs",
        "outfit": "orange bikini, micro bikini, string bikini, halterneck bikini, lowleg bikini bottom, barefoot, bare shoulders",
        "seed": 42424249
    },
    "morgana_lost_sword": {
        "name": "morgana",
        "lora": "lora_morgana_lost_sword.safetensors",
        "lora_strength": 0.80,
        "char": "morgana_(lost_sword), morgana, lost sword, witch hat, huge hat, black hat, long hair, purple hair, bangs, red eyes, evil smile, huge breasts, cleavage cutout, hourglass figure, wide hips",
        "outfit": "black robe, wizard robe, exposed shoulders, thighhighs, black thighhighs, black boots, high heels, gold trim",
        "seed": 42424249
    },
    "ran_lost_sword": {
        "name": "ran",
        "lora": "lora_ran_lost_sword.safetensors",
        "lora_strength": 0.80,
        "char": "ran_(lost_sword), ran, lost sword, fox girl, fox ears, animal ears, fox tail, multiple tails, nine tails, white hair, long hair, red eyes, red facial markings, large breasts, massive cleavage",
        "outfit": "traditional clothes, open kimono, white kimono, red hakama, sash, obi, bare shoulders, cleavage",
        "seed": 42424249
    },
    "claire_lost_sword": {
        "name": "claire",
        "lora": "lora_claire_lost_sword.safetensors",
        "lora_strength": 0.80,
        "char": "claire_(lost_sword), claire, lost sword, silver hair, white hair, short hair, hair between eyes, blue eyes, knight, armored, athletic, medium breasts, narrow waist, toned abdomen",
        "outfit": "silver armor, chestplate, shoulder armor, gauntlets, armored boots, white undershirt, blue tunic",
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
    base_outfit = char_cfg.get("outfit", "")
    if undress_type == "full":
        return f"{base_outfit}, fully_clothed, complete_outfit, neat_clothes"
    elif undress_type == "partial":
        return f"{base_outfit}, clothing_undone, breasts_exposed, clothes_around_waist, partially_unbuttoned, panties_pulled_aside, bare_breasts, bare_pussy"
    elif undress_type == "nude":
        return "completely nude, naked, bare breasts, bare nipples, bare pussy, nipples, areolae, navel, discarded clothes"
    return base_outfit

def generate_pure_prompt_workflow(char_key, char_cfg):
    nodes = {}
    node_id = 1
    
    # 1. Checkpoint Loader
    nodes[str(node_id)] = {
        "class_type": "CheckpointLoaderSimple",
        "inputs": {"ckpt_name": "illustriousXL_v01.safetensors"},
        "_meta": {"title": "Checkpoint Loader (Illustrious XL)"}
    }
    ckpt_id = node_id
    node_id += 1
    
    # 2. Character LoRA Loader
    nodes[str(node_id)] = {
        "class_type": "LoraLoader",
        "inputs": {
            "model": [str(ckpt_id), 0],
            "clip": [str(ckpt_id), 1],
            "lora_name": char_cfg["lora"],
            "strength_model": char_cfg["lora_strength"],
            "strength_clip": char_cfg["lora_strength"]
        },
        "_meta": {"title": f"LoRA Personaje: {char_cfg['name'].capitalize()} ({char_cfg['lora_strength']})"}
    }
    char_lora_id = node_id
    node_id += 1
    
    # 3. Concept Slider Base Loader (Pussy Adjuster)
    nodes[str(node_id)] = {
        "class_type": "LoraLoader",
        "inputs": {
            "model": [str(char_lora_id), 0],
            "clip": [str(char_lora_id), 1],
            "lora_name": "pussy_adjuster_xl.safetensors",
            "strength_model": 0.50,
            "strength_clip": 0.50
        },
        "_meta": {"title": "LoRA Slider Concept (Pussy Adjuster XL)"}
    }
    concept_lora_id = node_id
    node_id += 1
    
    # 4. CLIP Skip -2
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
    
    # 5. Negative Prompt Master
    nodes[str(node_id)] = {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [str(clip_skip_id), 0],
            "text": NEG_PROMPT_UNIFIED
        },
        "_meta": {"title": "Negative Prompt Master (Anti-Ropa / Anti-Miedo / Anti-Duplicados)"}
    }
    neg_id = node_id
    node_id += 1
    
    # 6. Empty Latent Compartido (832x1216 Vertical SDXL)
    nodes[str(node_id)] = {
        "class_type": "EmptyLatentImage",
        "inputs": {"width": 832, "height": 1216, "batch_size": 1},
        "_meta": {"title": "Base Latent Master (832x1216 Vertical SDXL)"}
    }
    initial_latent_id = node_id
    node_id += 1
    
    char_tags = char_cfg["char"]
    base_seed = char_cfg["seed"]
    
    for b_idx, branch in enumerate(PURE_BRANCHES, 1):
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
        
        # Positive Prompt
        prompt_title = f"📝 [PROMPT {branch['prefix'].upper()}]: {branch['title']}"
        
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
        
        # KSampler Directo (Generación Pura sin ControlNet a Denoise 1.0)
        nodes[str(node_id)] = {
            "class_type": "KSampler",
            "inputs": {
                "model": [str(stg_slider_id), 0],
                "positive": [str(stg_pos_id), 0],
                "negative": [str(neg_id), 0],
                "latent_image": [str(initial_latent_id), 0],
                "seed": base_seed,
                "control_after_generate": "fixed",
                "steps": 24,
                "cfg": 5.0,
                "sampler_name": "euler_ancestral",
                "scheduler": "karras",
                "denoise": 1.0
            },
            "_meta": {"title": f"KSampler Puro [{branch['prefix']}]"}
        }
        stg_ksampler_id = node_id
        node_id += 1
        
        # VAEDecode Estándar conectado al VAE del Modelo Checkpoint [str(ckpt_id), 2]
        nodes[str(node_id)] = {
            "class_type": "VAEDecode",
            "inputs": {
                "samples": [str(stg_ksampler_id), 0],
                "vae": [str(ckpt_id), 2]
            },
            "_meta": {"title": f"VAE Decode [{branch['prefix']}]"}
        }
        stg_decode_id = node_id
        node_id += 1
        
        # SaveImage
        nodes[str(node_id)] = {
            "class_type": "SaveImage",
            "inputs": {
                "filename_prefix": f"ComfyUI_Vault_{char_cfg['name']}_pure_{branch['prefix']}",
                "images": [str(stg_decode_id), 0]
            },
            "_meta": {"title": f"💾 Guardar [{branch['prefix']}]"}
        }
        node_id += 1
        
    return nodes

def main():
    print("Generating Pure Prompt Workflows (SIN ControlNet) for all 10 characters...")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    for char_key, char_cfg in CHARACTERS.items():
        char_dir = os.path.join(base_dir, char_key)
        os.makedirs(char_dir, exist_ok=True)
        
        short_name = char_cfg["name"]
        wf_data = generate_pure_prompt_workflow(char_key, char_cfg)
        
        out_path = os.path.join(char_dir, f"workflow_{short_name}_pure_prompt.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(wf_data, f, indent=2, ensure_ascii=False)
            
        print(f"  [OK] Created Pure Prompt JSON: {out_path}")

    print("\nAll Pure Prompt workflows generated successfully!")

if __name__ == "__main__":
    main()
