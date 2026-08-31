import os
import json

# ==============================================================================
# 🏛️ MASTER BUILDER: DOBLE PENETRACIÓN (DP) CON TODAS LAS MEJORAS AVANZADAS
# - ControlNetApplyAdvanced (strength: 0.40, start_percent: 0.0, end_percent: 0.70)
# - CLIPSetLastLayer (stop_at_clip_layer: -2 / CLIP Skip 2)
# - VAEDecodeTiled (tile_size: 512, anti-OOM)
# - EmptyLatentImage (832x1216 Vertical SDXL)
# - Personajes masculinos 100% desnudos y anclados
# ==============================================================================

DP_STAGES = [
    {
        "id": "01_seduccion",
        "name": "Seducción y Anticipación (Ropa Completa / Sin Contacto)",
        "undress_type": "full",
        "cnet_strength": 0.60,
        "slider_weight": -0.40,
        "slider_tags": "closed_legs, discrete",
        "expr": "seductive smile, blush, looking at viewer, flirting, playful, teasing, parted_lips",
        "action": "no_penetration, teasing_pose",
        "male_tags": "1girl, solo"
    },
    {
        "id": "02_doble_preliminar",
        "name": "Preliminares Dobles y Contacto Simultáneo (Ropa Semi-Abierta)",
        "undress_type": "partial",
        "cnet_strength": 0.45,
        "slider_weight": 0.30,
        "slider_tags": "teasing, lubricated",
        "expr": "blushing deeply, heavy_breathing, parted_lips, moaning, excited, anticipation, lust, glistening skin",
        "action": "(imminent double penetration:1.3), (tip_touching:1.2), vaginal_contact, anal_contact, teasing, sandwich, standing behind and kneeling front",
        "male_tags": "1girl, 2boys, 2men, nude males, naked males, completely naked men, dark-skinned male, tall male, muscular male, faceless male, bare chest, shirtless male, skin tone contrast, male bodies, muscular build"
    },
    {
        "id": "03_primera_doble_insercion",
        "name": "Pasión y Primera Doble Inserción (Ropa Semi-Abierta)",
        "undress_type": "partial",
        "cnet_strength": 0.40,
        "slider_weight": 0.55,
        "slider_tags": "(spread pussy:1.2), (stretched:1.3)",
        "expr": "pleasure, tears_of_pleasure, blushing, open_mouth, heavy_breathing, panting, moaning, flushed skin, sweat drops",
        "action": "(double_penetration:1.4), (dp:1.3), (first_insertion:1.3), (real penises:1.4), (human male penises:1.4), (erect penises:1.4), (dark-skinned penises:1.3), testicles, (vaginal:1.3), (anal:1.3), (both_holes:1.3), (2penises:1.4), (two_penises:1.4), stretching, (motion lines:1.2)",
        "male_tags": "1girl, 2boys, 2men, nude males, naked males, completely naked men, dark-skinned male, tall male, muscular male, faceless male, bare chest, shirtless male, skin tone contrast, male bodies, muscular build"
    },
    {
        "id": "04_extasis_dp",
        "name": "Éxtasis Total, Doble Clímax y Doble Corrida (Ropa Semi-Abierta)",
        "undress_type": "partial",
        "cnet_strength": 0.40,
        "slider_weight": 0.70,
        "slider_tags": "(spread_pussy:1.3), (labia_spread:1.3), (stretched:1.4)",
        "expr": "ecstasy, intense_pleasure, ahegao, heart_pupils, drooling, open_mouth, excessive_sweat, eye_contact, tears_of_pleasure, heavy_panting",
        "action": "(penis_in_pussy:1.4), (penis_in_anal:1.4), (deep_double_penetration:1.5), (dp:1.4), (balls_deep:1.3), (2penises:1.4), (both_holes:1.4), (creampie:1.3), (anal_creampie:1.3), (motion_lines:1.3), impact_lines",
        "male_tags": "1girl, 2boys, 2men, nude_males, naked_males, completely_naked_men, dark-skinned_male, tall_male, muscular_male, faceless_male, bare_chest, shirtless_male, skin_tone_contrast, male_bodies, muscular_build"
    },
    {
        "id": "05_afterglow_dp",
        "name": "Afterglow y Placer Satisfecho (Totalmente Desnuda / Doble Derrame)",
        "undress_type": "nude",
        "cnet_strength": 0.50,
        "slider_weight": 0.60,
        "slider_tags": "(spread pussy:1.3), (vaginal_gaping:1.3), (anal_gaping:1.3), (gaping:1.3)",
        "expr": "afterglow, satisfied, gentle_smile, blushing, heavy_breathing, sweat, relaxed, exhausted_smile, half-closed eyes",
        "action": "(after_double_penetration:1.3), (pull_out:1.3), (cum_leak:1.4), (anal_leak:1.4), semen_overflow, semen_drip, semen_on_body",
        "male_tags": "1girl, 2boys, 2men, nude males, naked males, completely naked men, dark-skinned male, tall male, muscular male, faceless male, bare chest, skin tone contrast"
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

NEG_PROMPT_DP = (
    "worst quality, low quality, bad anatomy, bad hands, missing fingers, extra fingers, "
    "clothed male, male clothes, shirt on male, pants on male, underwear on male, boxer shorts, male underwear, "
    "sex_toy, dildo, vibrator, strap-on, harness, artificial penis, glass dildo, silicone toy, machine, tentacles, "
    "disembodied_penis, floating penis, floating limbs, floating arms, floating legs, "
    "fused penis, monopenis, single penis, deformed penis, conjoined bodies, "
    "disfigured, deformed, malformed limbs, missing limbs, extra limbs, fused limbs, "
    "bad proportions, unnatural body, distorted body, duplicate limbs, overlapping limbs, "
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

def generate_dp_manual_workflow(char_key, char_cfg):
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
    
    # 4. Opción 3: CLIPSetLastLayer (stop_at_clip_layer: -2 / CLIP Skip 2)
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
    
    # 5. ControlNet Depth Loader
    nodes[str(node_id)] = {
        "class_type": "ControlNetLoader",
        "inputs": {"control_net_name": "controlnet-depth-sdxl-1.0.safetensors"},
        "_meta": {"title": "ControlNet Depth Loader"}
    }
    cnet_loader_id = node_id
    node_id += 1
    
    # 6. LoadImage (Manual DP Reference)
    nodes[str(node_id)] = {
        "class_type": "LoadImage",
        "inputs": {"image": "reference_dp_pose.png", "upload": "image"},
        "_meta": {"title": "📥 Cargar Imagen de Referencia (Pose DP)"}
    }
    manual_load_id = node_id
    node_id += 1
    
    # 7. Depth Preprocessor (bg_threshold: 0.01 captura completa, resolution: 1024)
    nodes[str(node_id)] = {
        "class_type": "MiDaS-DepthMapPreprocessor",
        "inputs": {
            "image": [str(manual_load_id), 0],
            "a": 6.28,
            "bg_threshold": 0.01,
            "resolution": 1024
        },
        "_meta": {"title": "⚙️ Depth Preprocessor (Mapa 3D DP)"}
    }
    manual_depth_id = node_id
    node_id += 1
    
    # 7B. Vista Previa del Mapa 3D (Permite ver y guardar con Clic Derecho)
    nodes[str(node_id)] = {
        "class_type": "PreviewImage",
        "inputs": {
            "images": [str(manual_depth_id), 0]
        },
        "_meta": {"title": "👁️ Mapa 3D DP Generado (Clic Derecho -> Guardar Imagen)"}
    }
    node_id += 1
    
    # 8. Negative Prompt Master
    nodes[str(node_id)] = {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [str(clip_skip_id), 0],
            "text": NEG_PROMPT_DP
        },
        "_meta": {"title": "Negative Prompt Master (Sin Ropa Masculina / Anti-Deformidades)"}
    }
    neg_id = node_id
    node_id += 1
    
    # 9. Opción 6: Shared Empty Latent (832x1216 Vertical SDXL)
    nodes[str(node_id)] = {
        "class_type": "EmptyLatentImage",
        "inputs": {"width": 832, "height": 1216, "batch_size": 1},
        "_meta": {"title": "Base Latent (832x1216 Vertical SDXL)"}
    }
    shared_latent_id = node_id
    node_id += 1
    
    char_tags = char_cfg["char"]
    base_seed = char_cfg["seed"]
    
    stg1_ksampler_id = None
    
    for s_idx, stg in enumerate(DP_STAGES, 1):
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
            "_meta": {"title": f"{'⭐' if s_idx == 1 else '🌿'} {stg['name']} (Prompt)"}
        }
        stg_pos_id = node_id
        node_id += 1
        
        # ControlNetApplyAdvanced
        nodes[str(node_id)] = {
            "class_type": "ControlNetApplyAdvanced",
            "inputs": {
                "positive": [str(stg_pos_id), 0],
                "negative": [str(neg_id), 0],
                "control_net": [str(cnet_loader_id), 0],
                "image": [str(manual_depth_id), 0],
                "strength": stg["cnet_strength"],
                "start_percent": 0.0,
                "end_percent": 0.70
            },
            "_meta": {"title": f"Apply ControlNet Advanced ({stg['cnet_strength']:.2f}, 0.0-0.70) [{stg['id']}]"}
        }
        stg_cnet_applied_id = node_id
        node_id += 1
        
        # KSampler Rama: Lee del latente Ancla de la Etapa 1
        in_latent = [str(shared_latent_id), 0] if s_idx == 1 else [str(stg1_ksampler_id), 0]
        stg_denoise = 1.0 if s_idx == 1 else (0.72 if s_idx == 4 else 0.70)
        
        nodes[str(node_id)] = {
            "class_type": "KSampler",
            "inputs": {
                "model": [str(stg_slider_id), 0],
                "positive": [str(stg_cnet_applied_id), 0],
                "negative": [str(stg_cnet_applied_id), 1],
                "latent_image": in_latent,
                "seed": base_seed,
                "control_after_generate": "fixed",
                "steps": 10,
                "cfg": 3.0,
                "sampler_name": "dpmpp_2m",
                "scheduler": "karras",
                "denoise": stg_denoise
            },
            "_meta": {"title": f"{'⭐' if s_idx == 1 else '🌿'} KSampler {stg['id']} {'[ANCLA]' if s_idx == 1 else '(Nace de Ancla 01)'}"}
        }
        if s_idx == 1:
            stg1_ksampler_id = node_id
        stg_ksampler_id = node_id
        node_id += 1
        
        # VAE Decode Estándar (Rápido y Continuo)
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
                "filename_prefix": f"{char_cfg['name']}/double_penetration/{stg['id']}"
            },
            "_meta": {"title": f"Save {stg['id']}"}
        }
        node_id += 1

    return nodes

def main():
    base_dir = r"E:\ComfyUI\characters"
    print("Compiling Advanced Double Penetration (DP) Workflows with Tiled VAE, CLIP Skip 2, and Step Scheduling...")
    
    for char_key, char_cfg in CHARACTERS.items():
        char_name = char_cfg["name"]
        char_dir = os.path.join(base_dir, char_key)
        os.makedirs(char_dir, exist_ok=True)
        
        wf_nodes = generate_dp_manual_workflow(char_key, char_cfg)
        json_path = os.path.join(char_dir, f"workflow_{char_name}_double_penetration.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(wf_nodes, f, indent=2)
        print(f"  [OK] Updated Advanced DP JSON: {json_path}")

    print("\nAll DP workflows updated with Advanced Features successfully!")

if __name__ == "__main__":
    main()
