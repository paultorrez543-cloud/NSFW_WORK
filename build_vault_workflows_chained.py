import json
import os
import sys

BASE_DIR = r"E:/ComfyUI/characters"

CKPT = "rinIllusionRNSFW_v30.safetensors"
NEG = (
    "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, "
    "deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, "
    "fewer digits, worst quality, low quality, blurry, ugly, censored, "
    "(bright lighting:1.5), overexposed, glare, flash, bloom, glowing, "
    "x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, "
    "signature, watermark, (holding weapon:1.4), (weapon:1.4), (sword:1.4)"
)

MALE = "disembodied_penis, 2penises"
DP = "doublepen, vaginal, anal, double_penetration, both_holes"
LIGHTING = "dimly_lit, dark_ambiance, (dark lighting:1.4)"

STAGES = [
    ("01_miedo",        "(imminent penetration:1.2)", "scared, trembling, refusal, nervous_sweat", "", "nervous_sweat", ""),
    ("02_dolor",        "tip_in_pussy, first_insertion", "(pain:1.3), tears_streaming, screaming", "(motion lines:1.3)", "sweat, tears_streaming", "sound_effects"),
    ("03_quebranto",    "(deep penetration:1.3)", "crying, defeated, broken_spirit", "(motion lines:1.4)", "sweat_drops, drooling", "sound_effects, onomatopoeia"),
    ("04_ahegao",       "(deep penetration:1.5), balls_deep", "ahegao, heart_pupils, mind_break, creampie", "(motion lines:1.5), impact_lines", "excessive_sweat, tears_of_pleasure, drooling", "sound_effects, onomatopoeia"),
    ("05_rota",         "balls_deep, gaping", "blank_eyes, thousand_yard_stare, semen_on_body", "", "excessive_sweat, dried_tears, semen_on_body", ""),
    ("06_inconsciente", "after_sex, sleeping", "sleeping, tears_streaming, semen_on_face", "", "dried_tears, cum_pool", ""),
]

POSES = {
    "cowgirl":         "cowgirl_position, girl_on_top, straddling, front_view",
    "doggystyle":      "doggystyle, from_behind, all_fours, front_view",
    "missionary":      "missionary_position, legs_up, spread_legs, front_view",
    "mating_press":    "mating_press, legs_above_head, folded, front_view",
    "reverse_cowgirl": "reverse_cowgirl, girl_on_top, facing_away, front_view",
}

CHARACTERS = {
    "elisia_make_drama": {
        "name": "elisia",
        "lora": "lora_elisia_make_drama.safetensors",
        "lora_strength": 0.85,
        "char": "elisia_(make_drama), elisia, make drama, 1girl, demon girl, demon horns, curved horns, black horns, pointy ears, long hair, wavy hair, bangs, delicate face",
        "outfit": "gothic dress, black dress, red accents, gold trim, corset, bare shoulders, cleavage, detached sleeves, thighhighs",
        "seed": 42424249
    },
    "isolda_lost_sword": {
        "name": "isolda",
        "lora": "lora_isolda_lost_sword.safetensors",
        "lora_strength": 0.8,
        "char": "isolda_(lost_sword), isolda, 1girl, solo, long hair, platinum blonde hair, wavy hair, magenta eyes, pink flower hair ornament, hair flower, delicate face",
        "outfit": "white dress, slit wrap dress, high slit, bare shoulders, green scarf, green shawl, floating fabrics, gold bracelets, gold armlet, gold jewelry",
        "seed": 42424249
    },
    "orihime_swimsuit": {
        "name": "orihime",
        "lora": "lora_orihime_swimsuit.safetensors",
        "lora_strength": 0.8,
        "char": "orihime inoue, bleach, bleach brave souls, 1girl, solo, long hair, orange hair, side braid, flower hair ornament, pearl chain, brown eyes, large breasts",
        "outfit": "swimsuit, bikini, pink swimsuit, frilled bikini, bows, bare shoulders, cleavage, navel, sandals, flip-flops",
        "seed": 42424249
    },
    "morgana_lost_sword": {
        "name": "morgana",
        "lora": "lora_morgana_lost_sword.safetensors",
        "lora_strength": 0.8,
        "char": "morgana_(lost_sword), morgana, 1girl, solo, mage, wizard, white hair, long hair, green eyes, flat chest, petite",
        "outfit": "black dress, black corset, bare shoulders, detailed fabric",
        "seed": 42424249
    },
    "ran_lost_sword": {
        "name": "ran",
        "lora": "lora_ran_lost_sword.safetensors",
        "lora_strength": 0.8,
        "char": "ran_(lost_sword), ran, 1girl, solo, oni, white hair, high ponytail, black horns, pointy ears, red eye makeup, hair between eyes, large breasts, mole on breast",
        "outfit": "japanese clothes, white kimono, single bare shoulder, chest sarashi, cleavage, black hakama, hakama skirt, fur scarf, manaita obi, white socks, platform sandals, geta",
        "seed": 42424249
    },
    "claire_lost_sword": {
        "name": "claire",
        "lora": "lora_claire_lost_sword.safetensors",
        "lora_strength": 0.8,
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
        "seed": 42424249
    },
    "jennie_make_drama": {
        "name": "jennie",
        "lora": "lora_jennie_make_drama.safetensors",
        "lora_strength": 0.85,
        "char": "jennie_(make_drama), jennie, make drama, 1girl, solo, teal hair, cyan hair, long hair, ponytail, white ribbon, hair ribbon, bangs, parted bangs, golden eyes, yellow eyes, amber eyes",
        "outfit": "business attire, office lady, white collared shirt, black blazer, black suit, black pencil skirt, dark pantyhose, black high heels",
        "seed": 42424249
    }
}

def clean_tags(tags_str):
    raw = [t.strip() for t in tags_str.split(",") if t.strip()]
    seen = set()
    cleaned = []
    for t in raw:
        if t not in seen:
            seen.add(t)
            cleaned.append(t)
    return ", ".join(cleaned)

def build_workflow_json(c):
    nodes = {}
    nodes["ckpt"] = {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}}
    nodes["latent_shared"] = {"class_type": "EmptyLatentImage", "inputs": {"width": 1024, "height": 1536, "batch_size": 1}}
    nodes["clip_skip"] = {"class_type": "CLIPSetLastLayer", "inputs": {"clip": ["ckpt", 1], "stop_at_clip_layer": -2}}
    nodes["lora_char"] = {
        "class_type": "LoraLoader",
        "inputs": {
            "model": ["ckpt", 0],
            "clip": ["clip_skip", 0],
            "lora_name": c["lora"],
            "strength_model": c["lora_strength"],
            "strength_clip": c["lora_strength"]
        }
    }
    nodes["lora_depth"] = {
        "class_type": "LoraLoader",
        "inputs": {
            "model": ["lora_char", 0],
            "clip": ["lora_char", 1],
            "lora_name": "penetration_depth.safetensors",
            "strength_model": 1.5,
            "strength_clip": 1.0
        }
    }
    nodes["lora_dp"] = {
        "class_type": "LoraLoader",
        "inputs": {
            "model": ["lora_depth", 0],
            "clip": ["lora_depth", 1],
            "lora_name": "doublepenetration_r1.safetensors",
            "strength_model": 1.0,
            "strength_clip": 1.0
        }
    }
    nodes["lora_size"] = {
        "class_type": "LoraLoader",
        "inputs": {
            "model": ["lora_dp", 0],
            "clip": ["lora_dp", 1],
            "lora_name": "Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors",
            "strength_model": 0.5,
            "strength_clip": 1.0
        }
    }
    nodes["neg"] = {"class_type": "CLIPTextEncode", "inputs": {"text": NEG, "clip": ["lora_size", 1]}}

    for pose_name, pose_tags in POSES.items():
        nodes[f"cn_loader_{pose_name}"] = {
            "class_type": "ControlNetLoader",
            "inputs": {
                "control_net_name": "controlnet-depth-sdxl.safetensors"
            }
        }
        nodes[f"cn_image_{pose_name}"] = {
            "class_type": "LoadImage",
            "inputs": {
                "image": f"control_poses/{pose_name}.png"
            }
        }
        
        last_ksampler = None
        
        for idx, (n, depth, expr, motion, fluids, sound) in enumerate(STAGES):
            if n in ["05_rota", "06_inconsciente"]:
                outfit_stage = "completely nude, naked, discarded clothes"
            else:
                outfit_stage = c["outfit"]
            parts = ["score_9, score_8_up, source_anime, rating_explicit", c["char"], outfit_stage, MALE, DP, depth, pose_tags, expr, fluids]
            if motion:
                parts.append(motion)
            if sound:
                parts.append(sound)
            parts.append(LIGHTING + ", anime, masterpiece, best_quality")
            
            prompt = clean_tags(", ".join([p for p in parts if p]))
            key = f"{pose_name}_{n}"
            nodes[f"p_{key}"] = {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["lora_size", 1]}}
            nodes[f"cn_apply_{key}"] = {
                "class_type": "ControlNetApply",
                "inputs": {
                    "strength": 0.9,
                    "conditioning": [f"p_{key}", 0],
                    "control_net": [f"cn_loader_{pose_name}", 0],
                    "image": [f"cn_image_{pose_name}", 0]
                }
            }
            
            if idx == 0:
                latent_input = ["latent_shared", 0]
                denoise_val = 1.0
            else:
                latent_input = [last_ksampler, 0]
                denoise_val = 0.55

            nodes[f"k_{key}"] = {
                "class_type": "KSampler",
                "inputs": {
                    "seed": c["seed"],
                    "steps": 28,
                    "cfg": 5.0,
                    "sampler_name": "dpmpp_2m",
                    "scheduler": "karras",
                    "denoise": denoise_val,
                    "model": ["lora_size", 0],
                    "positive": [f"cn_apply_{key}", 0],
                    "negative": ["neg", 0],
                    "latent_image": latent_input
                }
            }
            nodes[f"d_{key}"] = {"class_type": "VAEDecode", "inputs": {"samples": [f"k_{key}", 0], "vae": ["ckpt", 2]}}
            nodes[f"s_{key}"] = {
                "class_type": "SaveImage",
                "inputs": {
                    "filename_prefix": f"{c['name']}_{pose_name}_{n}",
                    "images": [f"d_{key}", 0]
                }
            }
            last_ksampler = f"k_{key}"
            
    return nodes

def generate_all():
    print("Starting generation of chained 30-image workflows for vault characters...")
    for folder, c in CHARACTERS.items():
        char_dir = os.path.join(BASE_DIR, folder)
        os.makedirs(char_dir, exist_ok=True)
        
        # 1. Generate workflow JSON
        wf_nodes = build_workflow_json(c)
        wf_path = os.path.join(char_dir, f"workflow_{c['name']}_chained.json")
        with open(wf_path, "w", encoding="utf-8") as f:
            json.dump(wf_nodes, f, indent=2, ensure_ascii=False)
        print(f"  [OK] Created JSON: {wf_path}")

        # 2. Generate python builder script
        py_content = f'''import json
import os

B = os.path.dirname(os.path.abspath(__file__))
CKPT = "{CKPT}"

LORA = "{c['lora']}"
LORA_STRENGTH = {c['lora_strength']}
SEED = {c['seed']}

CHAR = "{c['char']}"
OUTFIT = "{c['outfit']}"

MALE = "{MALE}"
DP = "{DP}"
NEG = "{NEG}"
LIGHTING = "{LIGHTING}"

STAGES = {repr(STAGES)}
POSES = {repr(POSES)}

def build_workflow():
    nodes = {{}}
    nodes["ckpt"] = {{"class_type": "CheckpointLoaderSimple", "inputs": {{"ckpt_name": CKPT}}}}
    nodes["latent_shared"] = {{"class_type": "EmptyLatentImage", "inputs": {{"width": 1024, "height": 1536, "batch_size": 1}}}}
    nodes["clip_skip"] = {{"class_type": "CLIPSetLastLayer", "inputs": {{"clip": ["ckpt", 1], "stop_at_clip_layer": -2}}}}
    nodes["lora_char"] = {{
        "class_type": "LoraLoader",
        "inputs": {{
            "model": ["ckpt", 0],
            "clip": ["clip_skip", 0],
            "lora_name": LORA,
            "strength_model": LORA_STRENGTH,
            "strength_clip": LORA_STRENGTH
        }}
    }}
    nodes["lora_depth"] = {{
        "class_type": "LoraLoader",
        "inputs": {{
            "model": ["lora_char", 0],
            "clip": ["lora_char", 1],
            "lora_name": "penetration_depth.safetensors",
            "strength_model": 1.5,
            "strength_clip": 1.0
        }}
    }}
    nodes["lora_dp"] = {{
        "class_type": "LoraLoader",
        "inputs": {{
            "model": ["lora_depth", 0],
            "clip": ["lora_depth", 1],
            "lora_name": "doublepenetration_r1.safetensors",
            "strength_model": 1.0,
            "strength_clip": 1.0
        }}
    }}
    nodes["lora_size"] = {{
        "class_type": "LoraLoader",
        "inputs": {{
            "model": ["lora_dp", 0],
            "clip": ["lora_dp", 1],
            "lora_name": "Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors",
            "strength_model": 0.5,
            "strength_clip": 1.0
        }}
    }}
    nodes["neg"] = {{"class_type": "CLIPTextEncode", "inputs": {{"text": NEG, "clip": ["lora_size", 1]}}}}

    for pose_name, pose_tags in POSES.items():
        nodes[f"cn_loader_{{pose_name}}"] = {{
            "class_type": "ControlNetLoader",
            "inputs": {{
                "control_net_name": "controlnet-depth-sdxl.safetensors"
            }}
        }}
        nodes[f"cn_image_{{pose_name}}"] = {{
            "class_type": "LoadImage",
            "inputs": {{
                "image": f"control_poses/{{pose_name}}.png"
            }}
        }}
        
        last_ksampler = None
        
        for idx, (n, depth, expr, motion, fluids, sound) in enumerate(STAGES):
            if n in ["05_rota", "06_inconsciente"]:
                outfit_stage = "completely nude, naked, discarded clothes"
            else:
                outfit_stage = OUTFIT
            parts = ["score_9, score_8_up, source_anime, rating_explicit", CHAR, outfit_stage, MALE, DP, depth, pose_tags, expr, fluids]
            if motion: parts.append(motion)
            if sound: parts.append(sound)
            parts.append(LIGHTING + ", anime, masterpiece, best_quality")
            
            raw = [t.strip() for t in ", ".join([p for p in parts if p]).split(",") if t.strip()]
            seen = set()
            cleaned = []
            for t in raw:
                if t not in seen:
                    seen.add(t)
                    cleaned.append(t)
            prompt = ", ".join(cleaned)

            key = f"{{pose_name}}_{{n}}"
            nodes[f"p_{{key}}"] = {{"class_type": "CLIPTextEncode", "inputs": {{"text": prompt, "clip": ["lora_size", 1]}}}}
            nodes[f"cn_apply_{{key}}"] = {{
                "class_type": "ControlNetApply",
                "inputs": {{
                    "strength": 0.9,
                    "conditioning": [f"p_{{key}}", 0],
                    "control_net": [f"cn_loader_{{pose_name}}", 0],
                    "image": [f"cn_image_{{pose_name}}", 0]
                }}
            }}
            
            if idx == 0:
                latent_input = ["latent_shared", 0]
                denoise_val = 1.0
            else:
                latent_input = [last_ksampler, 0]
                denoise_val = 0.55

            nodes[f"k_{{key}}"] = {{
                "class_type": "KSampler",
                "inputs": {{
                    "seed": SEED,
                    "steps": 28,
                    "cfg": 5.0,
                    "sampler_name": "dpmpp_2m",
                    "scheduler": "karras",
                    "denoise": denoise_val,
                    "model": ["lora_size", 0],
                    "positive": [f"cn_apply_{{key}}", 0],
                    "negative": ["neg", 0],
                    "latent_image": latent_input
                }}
            }}
            nodes[f"d_{{key}}"] = {{"class_type": "VAEDecode", "inputs": {{"samples": [f"k_{{key}}", 0], "vae": ["ckpt", 2]}}}}
            nodes[f"s_{{key}}"] = {{
                "class_type": "SaveImage",
                "inputs": {{
                    "filename_prefix": f"{c['name']}_{{pose_name}}_{{n}}",
                    "images": [f"d_{{key}}", 0]
                }}
            }}
            last_ksampler = f"k_{{key}}"
            
    return nodes

if __name__ == "__main__":
    wf = build_workflow()
    wf_path = os.path.join(B, "workflow_{c['name']}_chained.json")
    with open(wf_path, "w", encoding="utf-8") as f:
        json.dump(wf, f, indent=2, ensure_ascii=False)
    print(f"Generated workflow JSON at: {{wf_path}}")
'''
        
        py_path = os.path.join(char_dir, f"build_{c['name']}_chained.py")
        with open(py_path, "w", encoding="utf-8") as f:
            f.write(py_content)
        print(f"  [OK] Created Script: {py_path}")

    print("All characters generated successfully!")

if __name__ == "__main__":
    generate_all()
