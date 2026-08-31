import os
import json

# ==============================================================================
# 🏛️ MASTER BUILDER: BRANCHED ANCHOR WORKFLOWS (PUNTO ANCLA ETAPA 1 -> RAMAS 2..5)
# - La Etapa 1 genera la imagen base ancla (fija rostro, cabello, fondo bloom y proporciones)
# - Las Etapas 2, 3, 4 y 5 nacen directamente del LATENTE de la Etapa 1 (denoise: 0.70)
# - Conserva al 100% el Mapa 3D MiDaS (resolución 1024, bg_threshold 0.01) + Vista Previa
# - Máximo Bloom cinemático, KSampler 10 pasos, CFG 3.0, dpmpp_2m + karras, fixed
# - Stage 4 con (penis_in_pussy:1.4), penises reales y cero juguetes
# ==============================================================================

STAGES = [
    {
        "id": "01_seduccion",
        "name": "Seducción y Teasing (Ropa Completa / Punto Ancla)",
        "undress_type": "full",
        "slider_weight": -0.40,
        "slider_tags": "closed_legs, discrete",
        "expr": "seductive_smile, light_blush, looking_at_viewer, flirting, playful, teasing, parted_lips, blushing",
        "action": "no_penetration, teasing_pose",
        "male_tags": "1girl, solo",
        "denoise": 1.0
    },
    {
        "id": "02_preliminares",
        "name": "Preliminares y Contacto Inminente (Ropa Semi-Abierta / Rama 2)",
        "undress_type": "partial",
        "slider_weight": 0.25,
        "slider_tags": "teasing",
        "expr": "blushing_deeply, heavy_breathing, parted_lips, moaning, excited, anticipation, lust, glistening_skin, light_sweat",
        "action": "(imminent_penetration:1.2), tip_touching, thigh_contact",
        "male_tags": "1girl, 1boy, 1man, nude_males, naked_males, completely_naked_men, dark-skinned_male, tall_male, muscular_male, faceless_male, bare_chest, shirtless_male, skin_tone_contrast, male_body, muscular_build",
        "denoise": 0.70
    },
    {
        "id": "03_primera_insercion",
        "name": "Pasión y Primera Inserción (Ropa Semi-Abierta / Rama 3)",
        "undress_type": "partial",
        "slider_weight": 0.50,
        "slider_tags": "(spread_pussy:1.1), stretching",
        "expr": "pleasure, tears_of_pleasure, blushing, open_mouth, heavy_breathing, panting, moaning, sweat_drops, flushed_skin",
        "action": "(tip_in_pussy:1.3), (first_insertion:1.3), (real_penis:1.4), (human_male_penis:1.4), (erect_penis:1.4), (dark-skinned_penis:1.3), testicles, stretching, (motion_lines:1.2)",
        "male_tags": "1girl, 1boy, 1man, nude_males, naked_males, completely_naked_men, dark-skinned_male, tall_male, muscular_male, faceless_male, bare_chest, shirtless_male, skin_tone_contrast, male_body, muscular_build",
        "denoise": 0.70
    },
    {
        "id": "04_extasis",
        "name": "Éxtasis, Clímax y Corrida (Ropa Semi-Abierta / Rama 4)",
        "undress_type": "partial",
        "slider_weight": 0.65,
        "slider_tags": "(spread_pussy:1.2), (labia_spread:1.2)",
        "expr": "ecstasy, intense_pleasure, ahegao, heart_pupils, drooling, open_mouth, excessive_sweat, eye_contact, tears_of_pleasure, heavy_panting",
        "action": "(penis_in_pussy:1.4), (deep_penetration:1.4), (balls_deep:1.3), (creampie:1.2), (real_penis:1.4), (human_male_penis:1.4), (motion_lines:1.3), impact_lines",
        "male_tags": "1girl, 1boy, 1man, nude_males, naked_males, completely_naked_men, dark-skinned_male, tall_male, muscular_male, faceless_male, bare_chest, shirtless_male, skin_tone_contrast, male_body, muscular_build",
        "denoise": 0.72
    },
    {
        "id": "05_afterglow",
        "name": "Afterglow y Placer Satisfecho (Totalmente Desnuda / Rama 5)",
        "undress_type": "nude",
        "slider_weight": 0.55,
        "slider_tags": "(spread_pussy:1.2), (gaping:1.2)",
        "expr": "afterglow, satisfied, gentle_smile, blushing, heavy_breathing, sweat, relaxed, exhausted_smile, half-closed_eyes",
        "action": "(after_sex:1.2), (pull_out:1.2), (cum_leak:1.3), semen_drip, semen_on_body",
        "male_tags": "1girl, 1boy, 1man, nude_males, naked_males, completely_naked_men, dark-skinned_male, tall_male, muscular_male, faceless_male, bare_chest, skin_tone_contrast",
        "denoise": 0.70
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
        "seed": 42424249,
        "denoise": 0.66
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
        "seed": 42424249,
        "denoise": 0.66
    }
}

NEG_PROMPT_UNIFIED = (
    "worst quality, low quality, bad anatomy, bad hands, missing fingers, extra fingers, "
    "clothed male, male clothes, shirt on male, pants on male, underwear on male, boxer shorts, male underwear, "
    "sex_toy, dildo, vibrator, strap-on, harness, artificial penis, glass dildo, silicone toy, machine, tentacles, "
    "disembodied_penis, floating penis, floating limbs, floating arms, floating legs, "
    "fused fingers, too many fingers, mutated hands, poorly drawn hands, poorly drawn face, "
    "fused limbs, bad proportions, unnatural body, distorted body, duplicate limbs, overlapping limbs, "
    "extra arms, extra legs, poorly drawn eyes, cross-eyed, asymmetrical eyes, "
    "detailed background, sharp background, complex background, bright background, white background, flat lighting, sunny, overexposed, lowres"
)

QUALITY_PREFIX = "score_9, score_8_up, score_7_up, source_anime, rating_explicit, masterpiece, best quality, highly detailed, perfect anatomy, accurate anatomy, detailed eyes, detailed face"
ATMOS_TAGS = "(blurry_background:1.4), (heavy_bokeh:1.3), (bloom:1.5), (heavy_bloom:1.4), (cinematic_bloom:1.4), (glowing_background:1.3), (glowing_bokeh:1.3), (volumetric_lighting:1.3), (light_rays:1.3), (god_rays:1.2), (glowing_particles:1.2), (lens_flare:1.3), (soft_glowing_rim_light:1.4), (backlighting:1.3), (depth_of_field:1.3), (extreme_depth_of_field:1.2), (dark_background:1.3), dark_room, dim_lighting, dramatic_shadows, dramatic_lighting"

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

def generate_branched_workflow(char_key, char_cfg):
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
    
    # 7. MiDaS Depth Preprocessor (bg_threshold: 0.01, resolution: 1024) -> RAÍZ DEL MAPA 3D
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
    
    # 7B. Vista Previa del Mapa 3D (No se elimina, se muestra en pantalla)
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
        "_meta": {"title": "Negative Prompt Master (Anti-Ropa Masculina / Anti-Deformidades)"}
    }
    neg_id = node_id
    node_id += 1
    
    # 9. Empty Latent para la Etapa 1 (832x1216 Vertical SDXL)
    nodes[str(node_id)] = {
        "class_type": "EmptyLatentImage",
        "inputs": {"width": 832, "height": 1216, "batch_size": 1},
        "_meta": {"title": "Base Latent Etapa 1 (832x1216 Vertical SDXL)"}
    }
    initial_latent_id = node_id
    node_id += 1
    
    char_tags = char_cfg["char"]
    base_seed = char_cfg["seed"]
    
    stg1 = STAGES[0]
    outfit1 = get_outfit_tags(char_cfg, stg1["undress_type"])
    male_tags1 = stg1["male_tags"]
    stg1_prompt = clean_tags(f"{QUALITY_PREFIX}, {char_tags}, {male_tags1}, {outfit1}, {ATMOS_TAGS}, {stg1['slider_tags']}, {stg1['expr']}, {stg1['action']}")
    
    # =========================================================================
    # 🌟 ETAPA 01: PUNTO ANCLA RAIZ (Genera el latente base madre)
    # =========================================================================
    nodes[str(node_id)] = {
        "class_type": "LoraLoader",
        "inputs": {
            "model": [str(concept_lora_id), 0],
            "clip": [str(clip_skip_id), 0],
            "lora_name": "pussy_adjuster_xl.safetensors",
            "strength_model": stg1["slider_weight"],
            "strength_clip": stg1["slider_weight"]
        },
        "_meta": {"title": f"Slider Stage 1 ({stg1['slider_weight']:+.2f})"}
    }
    stg1_slider_id = node_id
    node_id += 1
    
    nodes[str(node_id)] = {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [str(stg1_slider_id), 1],
            "text": stg1_prompt
        },
        "_meta": {"title": f"⭐ {stg1['name']} (Prompt)"}
    }
    stg1_pos_id = node_id
    node_id += 1
    
    nodes[str(node_id)] = {
        "class_type": "ControlNetApplyAdvanced",
        "inputs": {
            "positive": [str(stg1_pos_id), 0],
            "negative": [str(neg_id), 0],
            "control_net": [str(cnet_loader_id), 0],
            "image": [str(manual_depth_id), 0],
            "strength": 0.60,
            "start_percent": 0.0,
            "end_percent": 0.70
        },
        "_meta": {"title": "Apply ControlNet 3D [01_Ancla]"}
    }
    stg1_cnet_applied_id = node_id
    node_id += 1
    
    # KSampler Etapa 1 (Denoise 1.0 - PUNTO ANCLA)
    nodes[str(node_id)] = {
        "class_type": "KSampler",
        "inputs": {
            "model": [str(stg1_slider_id), 0],
            "positive": [str(stg1_cnet_applied_id), 0],
            "negative": [str(stg1_cnet_applied_id), 1],
            "latent_image": [str(initial_latent_id), 0],
            "seed": base_seed,
            "control_after_generate": "fixed",
            "steps": 10,
            "cfg": 3.0,
            "sampler_name": "dpmpp_2m",
            "scheduler": "karras",
            "denoise": 1.0
        },
        "_meta": {"title": "⭐ KSampler 01 [PUNTO ANCLA MADRE]"}
    }
    anchor_latent_id = node_id
    node_id += 1
    
    nodes[str(node_id)] = {
        "class_type": "VAEDecode",
        "inputs": {
            "samples": [str(anchor_latent_id), 0],
            "vae": [str(ckpt_id), 2]
        },
        "_meta": {"title": "VAE Decode 01_Ancla"}
    }
    stg1_vae_id = node_id
    node_id += 1
    
    nodes[str(node_id)] = {
        "class_type": "SaveImage",
        "inputs": {
            "images": [str(stg1_vae_id), 0],
            "filename_prefix": f"{char_cfg['name']}/branched_anchor/{stg1['id']}"
        },
        "_meta": {"title": "Save 01_Ancla"}
    }
    node_id += 1
    
    # =========================================================================
    # 🌿 ETAPAS 2 A 5: RAMAS DERIVADAS DIRECTAMENTE DEL LATENTE ANCLA (Etapa 1)
    # =========================================================================
    for s_idx, stg in enumerate(STAGES[1:], 2):
        outfit = get_outfit_tags(char_cfg, stg["undress_type"])
        male_tags = stg["male_tags"]
        stg_prompt = clean_tags(f"{QUALITY_PREFIX}, {char_tags}, {male_tags}, {outfit}, {ATMOS_TAGS}, {stg['slider_tags']}, {stg['expr']}, {stg['action']}")
        
        # Slider LoRA
        nodes[str(node_id)] = {
            "class_type": "LoraLoader",
            "inputs": {
                "model": [str(concept_lora_id), 0],
                "clip": [str(clip_skip_id), 0],
                "lora_name": "pussy_adjuster_xl.safetensors",
                "strength_model": stg["slider_weight"],
                "strength_clip": stg["slider_weight"]
            },
            "_meta": {"title": f"Slider Stage {s_idx} ({stg['slider_weight']:+.2f})"}
        }
        stg_slider_id = node_id
        node_id += 1
        
        # Positive Prompt
        nodes[str(node_id)] = {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "clip": [str(stg_slider_id), 1],
                "text": stg_prompt
            },
            "_meta": {"title": f"🌿 {stg['name']} (Prompt)"}
        }
        stg_pos_id = node_id
        node_id += 1
        
        # ControlNet 3D aplicado a la rama
        nodes[str(node_id)] = {
            "class_type": "ControlNetApplyAdvanced",
            "inputs": {
                "positive": [str(stg_pos_id), 0],
                "negative": [str(neg_id), 0],
                "control_net": [str(cnet_loader_id), 0],
                "image": [str(manual_depth_id), 0],
                "strength": 0.55,
                "start_percent": 0.0,
                "end_percent": 0.70
            },
            "_meta": {"title": f"Apply ControlNet 3D [{stg['id']}]"}
        }
        stg_cnet_applied_id = node_id
        node_id += 1
        
        # KSampler Rama: LEE DIRECTAMENTE DEL LATENTE ANCLA [anchor_latent_id, 0] a denoise 0.70
        nodes[str(node_id)] = {
            "class_type": "KSampler",
            "inputs": {
                "model": [str(stg_slider_id), 0],
                "positive": [str(stg_cnet_applied_id), 0],
                "negative": [str(stg_cnet_applied_id), 1],
                "latent_image": [str(anchor_latent_id), 0],
                "seed": base_seed,
                "control_after_generate": "fixed",
                "steps": 10,
                "cfg": 3.0,
                "sampler_name": "dpmpp_2m",
                "scheduler": "karras",
                "denoise": stg["denoise"]
            },
            "_meta": {"title": f"🌿 KSampler {stg['id']} (Nace de Ancla 01)"}
        }
        stg_ksampler_id = node_id
        node_id += 1
        
        # VAEDecode Estándar
        nodes[str(node_id)] = {
            "class_type": "VAEDecode",
            "inputs": {
                "samples": [str(stg_ksampler_id), 0],
                "vae": [str(ckpt_id), 2]
            },
            "_meta": {"title": f"VAE Decode {stg['id']}"}
        }
        stg_vae_id = node_id
        node_id += 1
        
        # SaveImage
        nodes[str(node_id)] = {
            "class_type": "SaveImage",
            "inputs": {
                "images": [str(stg_vae_id), 0],
                "filename_prefix": f"{char_cfg['name']}/branched_anchor/{stg['id']}"
            },
            "_meta": {"title": f"Save {stg['id']}"}
        }
        node_id += 1

    return nodes

def main():
    base_dir = r"E:\ComfyUI\characters"
    print("Generating Master Branched Anchor Workflows with 3D Depth Map for all 10 characters...")
    
    for char_key, char_cfg in CHARACTERS.items():
        char_name = char_cfg["name"]
        char_dir = os.path.join(base_dir, char_key)
        os.makedirs(char_dir, exist_ok=True)
        
        wf_nodes = generate_branched_workflow(char_key, char_cfg)
        json_path = os.path.join(char_dir, f"workflow_{char_name}_manual_branched.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(wf_nodes, f, indent=2)
        print(f"  [OK] Created Branched Anchor JSON: {json_path}")

    print("\nAll Branched Anchor workflows generated successfully!")

if __name__ == "__main__":
    main()
