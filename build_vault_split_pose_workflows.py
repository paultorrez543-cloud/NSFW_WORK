import os
import json

# ==============================================================================
# 🏛️ GENERADOR DE WORKFLOWS INDIVIDUALES POR POSE (SEGMENTACIÓN EN SUBCARPETAS)
# Genera 15 workflows independientes (1 por pose x 5 etapas) para cada personaje.
# ==============================================================================

POSES = [
    {
        "id": "01_cowgirl",
        "name": "Vaquera Frontal",
        "tags": "cowgirl_position, straddling, girl_on_top, sitting_on_partner, front_view, thighs"
    },
    {
        "id": "02_reverse_cowgirl",
        "name": "Vaquera Invertida",
        "tags": "reverse_cowgirl, reverse_cowgirl_position, girl_on_top, facing_away, back_view, ass_focus"
    },
    {
        "id": "03_doggystyle",
        "name": "De Perrito",
        "tags": "doggystyle, from_behind, all_fours, arched_back, back_view, ass_focus"
    },
    {
        "id": "04_missionary",
        "name": "Misionero Frontal",
        "tags": "missionary_position, lying_on_back, legs_spread, spread_legs, legs_up, front_view"
    },
    {
        "id": "05_mating_press",
        "name": "Mating Press",
        "tags": "mating_press, folded, legs_above_head, knees_to_chest, front_view"
    },
    {
        "id": "06_prone_bone",
        "name": "Prone Bone (Boca Abajo)",
        "tags": "prone_bone, lying_on_stomach, from_behind, arched_back, ass_focus"
    },
    {
        "id": "07_spooning",
        "name": "Cucharita De Lado",
        "tags": "spooning, spooning_position, lying_on_side, from_behind, side_view"
    },
    {
        "id": "08_standing_sex",
        "name": "De Pie Contra Pared",
        "tags": "standing_sex, standing, lifted, against_wall, leg_wrap"
    },
    {
        "id": "09_bent_over",
        "name": "Inclinada Sobre Mesa",
        "tags": "bent_over, bent_over_furniture, leaning_forward, ass_up, on_table, desk"
    },
    {
        "id": "10_seated_sex",
        "name": "Sentados Cara a Cara",
        "tags": "seated_sex, sitting, lap_sit, face_to_face, hugging, embrace"
    },
    {
        "id": "11_piledriver",
        "name": "Piledriver Invertido",
        "tags": "piledriver, upside_down, legs_up, folded, vertical_penetration"
    },
    {
        "id": "12_paizuri",
        "name": "Paizuri (Pechos)",
        "tags": "paizuri, breast_smother, breasts_focus, cleavage_fuck"
    },
    {
        "id": "13_fellatio",
        "name": "Sexo Oral De Rodillas",
        "tags": "fellatio, oral, deepthroat, kneeling, looking_up"
    },
    {
        "id": "14_cunnilingus",
        "name": "Cunnilingus (Placer Femenino)",
        "tags": "cunnilingus, oral, face_between_legs, spread_legs, lying_on_back"
    },
    {
        "id": "15_sixtynine",
        "name": "Posición 69 Mutua",
        "tags": "69_position, mutual_oral, reciprocal_oral, lying_on_side"
    }
]

STAGES = [
    {
        "id": "01_seduccion",
        "name": "Seducción y Teasing (Ropa Completa / Sin Pene)",
        "undress_type": "full",
        "slider_weight": -0.6,
        "slider_tags": "closed_legs, discrete",
        "expr": "seductive smile, blush, looking at viewer, flirting, playful, teasing, parted_lips, blushing",
        "action": "no_penetration, teasing_pose",
        "interracial_tags": ""
    },
    {
        "id": "02_preliminares",
        "name": "Preliminares y Contacto Inminente (Ropa Semi-Abierta)",
        "undress_type": "partial",
        "slider_weight": 0.3,
        "slider_tags": "teasing",
        "expr": "blushing deeply, heavy_breathing, parted_lips, moaning, excited, anticipation, lust",
        "action": "(imminent penetration:1.3), tip_touching, teasing, thigh_contact, disembodied_penis",
        "interracial_tags": "dark-skinned male, interracial, bbc_int, dark skin male, muscular male, large penis, skin tone contrast"
    },
    {
        "id": "03_primera_insercion",
        "name": "Pasión y Primera Inserción (Ropa Semi-Abierta)",
        "undress_type": "partial",
        "slider_weight": 0.7,
        "slider_tags": "(spread pussy:1.2), stretching",
        "expr": "pleasure, tears_of_pleasure, blushing, open_mouth, heavy_breathing, panting, moaning",
        "action": "(tip_in_pussy:1.4), (first_insertion:1.3), stretching, (motion lines:1.3), disembodied_penis",
        "interracial_tags": "dark-skinned male, interracial, bbc_int, dark skin male, muscular male, large penis, skin tone contrast"
    },
    {
        "id": "04_extasis",
        "name": "Éxtasis, Clímax y Corrida (Ropa Semi-Abierta)",
        "undress_type": "partial",
        "slider_weight": 0.9,
        "slider_tags": "(spread pussy:1.4), (labia spread:1.3)",
        "expr": "ecstasy, intense_pleasure, ahegao, heart_pupils, drooling, open_mouth, excessive_sweat, eye_contact",
        "action": "(deep penetration:1.6), (balls_deep:1.4), (creampie:1.3), (motion lines:1.5), impact_lines, disembodied_penis",
        "interracial_tags": "dark-skinned male, interracial, bbc_int, dark skin male, muscular male, large penis, skin tone contrast"
    },
    {
        "id": "05_afterglow",
        "name": "Afterglow y Placer Satisfecho (Totalmente Desnuda)",
        "undress_type": "nude",
        "slider_weight": 0.8,
        "slider_tags": "(spread pussy:1.3), (pussy spread:1.3), (gaping:1.3)",
        "expr": "afterglow, satisfied, gentle_smile, blushing, heavy_breathing, sweat, relaxed, exhausted_smile",
        "action": "(after_sex:1.3), (pull_out:1.3), (cum_leak:1.4), (gaping:1.3), semen_drip, semen_on_body, disembodied_penis",
        "interracial_tags": "dark-skinned male, interracial, bbc_int, dark skin male, muscular male, large penis"
    }
]

CHARACTERS = {
    "elisia_make_drama": {
        "name": "elisia",
        "lora": "lora_elisia_make_drama.safetensors",
        "lora_strength": 0.85,
        "char": "elisia_(make_drama), elisia, make drama, 1girl, solo, demon girl, demon horns, curved horns, black horns, pointy ears, long hair, wavy hair, bangs, delicate face, curvy, hourglass figure, huge breasts, massive cleavage, narrow waist, wide hips, huge ass, big ass, bubble butt, thick thighs",
        "outfit": "open collar shirt, black crop top, high-waisted shorts, black shorts, belt, thong, visible thong, high heels, bare shoulders, bare midriff",
        "seed": 42424249
    },
    "isolda_lost_sword": {
        "name": "isolda",
        "lora": "lora_isolda_lost_sword.safetensors",
        "lora_strength": 0.85,
        "char": "isolda_(lost_sword), isolda, 1girl, solo, purple hair, short hair, hair between eyes, yellow eyes, small breasts",
        "outfit": "detailed dress, black dress, armor, pauldrons, breastplate, white cape, black gloves, thighhighs, boots, high heels",
        "seed": 42424249
    },
    "orihime_swimsuit": {
        "name": "orihime",
        "lora": "lora_orihime_swimsuit.safetensors",
        "lora_strength": 0.85,
        "char": "orihime inoue, bleach, bleach brave souls, 1girl, solo, long hair, orange hair, side braid, flower hair ornament, pearl chain, brown eyes, large breasts",
        "outfit": "swimsuit, bikini, pink swimsuit, frilled bikini, bows, bare shoulders, cleavage, navel, sandals, flip-flops",
        "seed": 42424249
    },
    "morgana_lost_sword": {
        "name": "morgana",
        "lora": "lora_morgana_lost_sword.safetensors",
        "lora_strength": 0.85,
        "char": "morgana_(lost_sword), morgana, 1girl, solo, mage, wizard, white hair, long hair, green eyes, flat chest, petite",
        "outfit": "black dress, black corset, bare shoulders, detailed fabric",
        "seed": 42424249
    },
    "ran_lost_sword": {
        "name": "ran",
        "lora": "lora_ran_lost_sword.safetensors",
        "lora_strength": 0.85,
        "char": "ran_(lost_sword), ran, 1girl, solo, oni, white hair, high ponytail, black horns, pointy ears, red eye makeup, hair between eyes, large breasts, mole on breast",
        "outfit": "japanese clothes, white kimono, single bare shoulder, chest sarashi, cleavage, black hakama, hakama skirt, fur scarf, manaita obi, white socks, platform sandals, geta",
        "seed": 42424249
    },
    "claire_lost_sword": {
        "name": "claire",
        "lora": "lora_claire_lost_sword.safetensors",
        "lora_strength": 0.80,
        "char": "claire_(lost_sword), claire, 1girl, solo, gray hair, long hair, blindfold, blindfold covering eyes, not visible eyes",
        "outfit": "nun, veil, white veil, nun habit, detached sleeves, detailed white dress, gold accents",
        "seed": 42424249
    },
    "nelliel_parasol": {
        "name": "nelliel",
        "lora": "lora_nelliel_parasol.safetensors",
        "lora_strength": 0.85,
        "char": "nelliel_parasol, nelliel tu odelschwanck, bleach, bleach brave souls, 1girl, solo, green hair, green eyes, ram skull, hollow mask on head, facial mark, red facial stripe, large breasts, massive cleavage",
        "outfit": "open floral kimono robe, open kimono, floral kimono, bikini top, sarong, bare legs, bare shoulders",
        "seed": 42424249,
        "denoise": 0.66
    },
    "jennie_make_drama": {
        "name": "jennie",
        "lora": "lora_jennie_make_drama.safetensors",
        "lora_strength": 0.85,
        "char": "jennie_(make_drama), jennie, make drama, 1girl, solo, teal hair, cyan hair, long hair, ponytail, white ribbon, hair ribbon, bangs, parted bangs, golden eyes, yellow eyes, amber eyes",
        "outfit": "business attire, office lady, white collared shirt, black blazer, black suit, black pencil skirt, dark pantyhose, black high heels",
        "seed": 42424249
    },
    "marcia_make_drama": {
        "name": "marcia",
        "lora": "lora_marcia_make_drama.safetensors",
        "lora_strength": 0.85,
        "char": "marcia_(make_drama), marcia, make drama, 1girl, solo, pink hair, high twintails, twintails, long hair, heart ahoge, purple eyes, fang, smirking, cute, petite, chubby thighs, barcode on thigh, bandaid on knee",
        "outfit": "futuristic bodysuit, highleg leotard, black and white bodysuit, cleavage cutout, white jacket, crop jacket, detached jacket, black gloves, asymmetric legwear, black thighhigh, single thighhigh, garter strap, mechanical boots",
        "seed": 42424249
    },
    "nelliel_heart": {
        "name": "nelliel",
        "lora": "lora_nelliel_heart.safetensors",
        "lora_strength": 0.85,
        "char": "nelliel_swimsuit, nelliel tu odelschwanck, bleach, bleach brave souls, 1girl, solo, tan, dark skin, green hair, wavy hair, long hair, green eyes, ram skull, hollow mask on head, facial mark, red facial stripe, large breasts, massive cleavage, wide hips",
        "outfit": "white bikini, halterneck bikini top, side-tie bikini bottom, yellow sarong, yellow pareo, floral pareo, beaded necklace, flower on waist",
        "seed": 42424249,
        "denoise": 0.66
    }
}

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

def generate_single_pose_workflow(char_key, char_cfg, pose, p_idx):
    nodes = {}
    node_id = 1
    
    # 1. Base Checkpoint Loader
    nodes[str(node_id)] = {
        "class_type": "CheckpointLoaderSimple",
        "inputs": {"ckpt_name": "illustrious-xl-v0.1.safetensors"},
        "_meta": {"title": "Base Model (Illustrious XL)"}
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
            "strength_clip": 1.0
        },
        "_meta": {"title": f"LoRA 1: {char_cfg['name'].capitalize()}"}
    }
    char_lora_id = node_id
    node_id += 1
    
    # 3. Chained Concept LoRA: BBC Interracial
    nodes[str(node_id)] = {
        "class_type": "LoraLoader",
        "inputs": {
            "model": [str(char_lora_id), 0],
            "clip": [str(char_lora_id), 1],
            "lora_name": "lora_bbc_interracial.safetensors",
            "strength_model": 0.70,
            "strength_clip": 0.70
        },
        "_meta": {"title": "LoRA 2: BBC Interracial"}
    }
    concept_lora_id = node_id
    node_id += 1
    
    # 4. ControlNet Loader (Depth)
    nodes[str(node_id)] = {
        "class_type": "ControlNetLoader",
        "inputs": {"control_net_name": "controlnet-depth-sdxl-1.0.safetensors"},
        "_meta": {"title": "ControlNet Depth Loader"}
    }
    cnet_loader_id = node_id
    node_id += 1
    
    # 5. Master Negative Prompt
    neg_prompt = "worst quality, low quality, bad anatomy, bad hands, missing fingers, extra fingers, watermark, signature, artist name, mutated hands, poorly drawn hands, poorly drawn face, disfigured, deformed, malformed limbs, missing limbs, extra limbs, bright background, white background, flat lighting, sunny, overexposed"
    nodes[str(node_id)] = {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [str(concept_lora_id), 1],
            "text": neg_prompt
        },
        "_meta": {"title": "Negative Prompt Master"}
    }
    neg_id = node_id
    node_id += 1
    
    char_tags = char_cfg["char"]
    base_seed = char_cfg["seed"]
    atmos_tags = "dark background, blurry background, depth of field, bokeh, dim lighting, dark room, soft rim light, cinematic lighting"
    
    p_name = pose["id"]
    p_tags = pose["tags"]
    
    # Stage 1: 01_seduccion (Base Pose & Depth Map Extraction)
    stg1 = STAGES[0]
    outfit1 = get_outfit_tags(char_cfg, stg1["undress_type"])
    stg1_prompt = clean_tags(f"score_9, score_8_up, score_7_up, source_anime, rating_explicit, {char_tags}, {outfit1}, {p_tags}, {atmos_tags}, {stg1['slider_tags']}, {stg1['expr']}, {stg1['action']}, masterpiece, best quality, highly detailed")
    
    # Stage 1 Slider LoRA (-0.6)
    nodes[str(node_id)] = {
        "class_type": "LoraLoader",
        "inputs": {
            "model": [str(concept_lora_id), 0],
            "clip": [str(concept_lora_id), 1],
            "lora_name": "pussy_adjuster_xl.safetensors",
            "strength_model": stg1["slider_weight"],
            "strength_clip": stg1["slider_weight"]
        },
        "_meta": {"title": f"Slider Stage 1 ({stg1['slider_weight']:+.1f})"}
    }
    stg1_slider_id = node_id
    node_id += 1
    
    # Positive Prompt Stage 1
    nodes[str(node_id)] = {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [str(stg1_slider_id), 1],
            "text": stg1_prompt
        },
        "_meta": {"title": f"{stg1['name']} (Prompt)"}
    }
    stg1_pos_id = node_id
    node_id += 1
    
    # Latent Stage 1
    nodes[str(node_id)] = {
        "class_type": "EmptyLatentImage",
        "inputs": {"width": 1024, "height": 1024, "batch_size": 1},
        "_meta": {"title": "Base Latent (1024x1024)"}
    }
    stg1_latent_id = node_id
    node_id += 1
    
    stg1_denoise = char_cfg.get("denoise", 1.0)
    
    # KSampler Stage 1
    nodes[str(node_id)] = {
        "class_type": "KSampler",
        "inputs": {
            "model": [str(stg1_slider_id), 0],
            "positive": [str(stg1_pos_id), 0],
            "negative": [str(neg_id), 0],
            "latent_image": [str(stg1_latent_id), 0],
            "seed": base_seed + (p_idx * 100),
            "steps": 20,
            "cfg": 4.5,
            "sampler_name": "dpmpp_2m",
            "scheduler": "karras",
            "denoise": stg1_denoise
        },
        "_meta": {"title": f"KSampler {stg1['id']}"}
    }
    stg1_ksampler_id = node_id
    node_id += 1
    
    # VAE Decode Stage 1
    nodes[str(node_id)] = {
        "class_type": "VAEDecode",
        "inputs": {
            "samples": [str(stg1_ksampler_id), 0],
            "vae": [str(ckpt_id), 2]
        },
        "_meta": {"title": f"VAE Decode {stg1['id']}"}
    }
    stg1_vae_id = node_id
    node_id += 1
    
    # SaveImage Stage 1 (Segmented Output Subdirectory)
    nodes[str(node_id)] = {
        "class_type": "SaveImage",
        "inputs": {
            "images": [str(stg1_vae_id), 0],
            "filename_prefix": f"{char_cfg['name']}/poses/{p_name}/{stg1['id']}"
        },
        "_meta": {"title": f"Save {stg1['id']}"}
    }
    node_id += 1
    
    # MiDaS DepthMap Preprocessor
    nodes[str(node_id)] = {
        "class_type": "MiDaS-DepthMapPreprocessor",
        "inputs": {
            "image": [str(stg1_vae_id), 0],
            "a": 6.28,
            "bg_threshold": 0.1,
            "resolution": 1024
        },
        "_meta": {"title": f"Depth Preprocessor (Pose {p_idx:02d} 3D Map)"}
    }
    depth_prep_id = node_id
    node_id += 1
    
    # Stages 2 through 5 (Branched with Depth ControlNet & Dynamic Slider)
    for s_idx, stg in enumerate(STAGES[1:], 2):
        outfit = get_outfit_tags(char_cfg, stg["undress_type"])
        interracial_tags = stg["interracial_tags"]
        stg_prompt = clean_tags(f"score_9, score_8_up, score_7_up, source_anime, rating_explicit, {char_tags}, {outfit}, {p_tags}, {interracial_tags}, {atmos_tags}, {stg['slider_tags']}, {stg['expr']}, {stg['action']}, masterpiece, best quality, highly detailed")
        
        # Stage Slider LoRA
        nodes[str(node_id)] = {
            "class_type": "LoraLoader",
            "inputs": {
                "model": [str(concept_lora_id), 0],
                "clip": [str(concept_lora_id), 1],
                "lora_name": "pussy_adjuster_xl.safetensors",
                "strength_model": stg["slider_weight"],
                "strength_clip": stg["slider_weight"]
            },
            "_meta": {"title": f"Slider Stage {s_idx} ({stg['slider_weight']:+.1f})"}
        }
        stg_slider_id = node_id
        node_id += 1
        
        # CLIP Text Encode
        nodes[str(node_id)] = {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "clip": [str(stg_slider_id), 1],
                "text": stg_prompt
            },
            "_meta": {"title": f"{stg['name']} (Prompt)"}
        }
        stg_pos_id = node_id
        node_id += 1
        
        # Apply ControlNet
        nodes[str(node_id)] = {
            "class_type": "ControlNetApply",
            "inputs": {
                "conditioning": [str(stg_pos_id), 0],
                "control_net": [str(cnet_loader_id), 0],
                "image": [str(depth_prep_id), 0],
                "strength": 0.75
            },
            "_meta": {"title": f"Apply Depth ControlNet ({stg['id']})"}
        }
        stg_cnet_applied_id = node_id
        node_id += 1
        
        # KSampler Stage s
        nodes[str(node_id)] = {
            "class_type": "KSampler",
            "inputs": {
                "model": [str(stg_slider_id), 0],
                "positive": [str(stg_cnet_applied_id), 0],
                "negative": [str(neg_id), 0],
                "latent_image": [str(stg1_latent_id), 0],
                "seed": base_seed + (p_idx * 100) + s_idx,
                "steps": 20,
                "cfg": 4.5,
                "sampler_name": "dpmpp_2m",
                "scheduler": "karras",
                "denoise": 1.0
            },
            "_meta": {"title": f"KSampler {stg['id']}"}
        }
        stg_ksampler_id = node_id
        node_id += 1
        
        # VAE Decode
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
        
        # SaveImage (Segmented Output Subdirectory)
        nodes[str(node_id)] = {
            "class_type": "SaveImage",
            "inputs": {
                "images": [str(stg_vae_id), 0],
                "filename_prefix": f"{char_cfg['name']}/poses/{p_name}/{stg['id']}"
            },
            "_meta": {"title": f"Save {stg['id']}"}
        }
        node_id += 1

    return nodes

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print("Generating Segmented Individual Pose Workflows for all characters...")
    
    for char_key, char_cfg in CHARACTERS.items():
        char_name = char_cfg["name"]
        poses_dir = os.path.join(base_dir, char_key, "poses")
        os.makedirs(poses_dir, exist_ok=True)
        
        for p_idx, pose in enumerate(POSES, 1):
            pose_id = pose["id"]
            pose_subfolder = os.path.join(poses_dir, pose_id)
            os.makedirs(pose_subfolder, exist_ok=True)
            
            # Generar workflow individual para esta pose
            wf_nodes = generate_single_pose_workflow(char_key, char_cfg, pose, p_idx)
            json_filename = f"workflow_{char_name}_{pose_id}.json"
            json_path = os.path.join(pose_subfolder, json_filename)
            
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(wf_nodes, f, indent=2)
            
        print(f"  [OK] Segmented 15 pose workflows in: {poses_dir}")

    print("\nAll segmented pose workflows created successfully across all 10 characters!")

if __name__ == "__main__":
    main()
