import json
import os

B = os.path.dirname(os.path.abspath(__file__))
CKPT = "rinIllusionRNSFW_v30.safetensors"

LORA = "lora_isolda_lost_sword.safetensors"
LORA_STRENGTH = 0.8
SEED = 42424249

CHAR = "isolda_(lost_sword), isolda, 1girl, solo, long hair, platinum blonde hair, wavy hair, magenta eyes, pink flower hair ornament, hair flower, delicate face"
OUTFIT = "white dress, slit wrap dress, high slit, bare shoulders, green scarf, green shawl, floating fabrics, gold bracelets, gold armlet, gold jewelry"

MALE = "disembodied_penis, 2penises"
DP = "doublepen, vaginal, anal, double_penetration, both_holes"
NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark, (holding weapon:1.4), (weapon:1.4), (sword:1.4)"
LIGHTING = "dimly_lit, dark_ambiance, (dark lighting:1.4)"

STAGES = [('01_miedo', '(imminent penetration:1.2)', 'scared, trembling, refusal, nervous_sweat', '', 'nervous_sweat', ''), ('02_dolor', 'tip_in_pussy, first_insertion', '(pain:1.3), tears_streaming, screaming', '(motion lines:1.3)', 'sweat, tears_streaming', 'sound_effects'), ('03_quebranto', '(deep penetration:1.3)', 'crying, defeated, broken_spirit', '(motion lines:1.4)', 'sweat_drops, drooling', 'sound_effects, onomatopoeia'), ('04_ahegao', '(deep penetration:1.5), balls_deep', 'ahegao, heart_pupils, mind_break, creampie', '(motion lines:1.5), impact_lines', 'excessive_sweat, tears_of_pleasure, drooling', 'sound_effects, onomatopoeia'), ('05_rota', 'balls_deep, gaping', 'blank_eyes, thousand_yard_stare, semen_on_body', '', 'excessive_sweat, dried_tears, semen_on_body', ''), ('06_inconsciente', 'after_sex, sleeping', 'sleeping, tears_streaming, semen_on_face', '', 'dried_tears, cum_pool', '')]
POSES = {'cowgirl': 'cowgirl_position, girl_on_top, straddling, front_view', 'doggystyle': 'doggystyle, from_behind, all_fours, front_view', 'missionary': 'missionary_position, legs_up, spread_legs, front_view', 'mating_press': 'mating_press, legs_above_head, folded, front_view', 'reverse_cowgirl': 'reverse_cowgirl, girl_on_top, facing_away, front_view'}

def build_workflow():
    nodes = {}
    nodes["ckpt"] = {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}}
    nodes["latent_shared"] = {"class_type": "EmptyLatentImage", "inputs": {"width": 1024, "height": 1536, "batch_size": 1}}
    nodes["clip_skip"] = {"class_type": "CLIPSetLastLayer", "inputs": {"clip": ["ckpt", 1], "stop_at_clip_layer": -2}}
    nodes["lora_char"] = {
        "class_type": "LoraLoader",
        "inputs": {
            "model": ["ckpt", 0],
            "clip": ["clip_skip", 0],
            "lora_name": LORA,
            "strength_model": LORA_STRENGTH,
            "strength_clip": LORA_STRENGTH
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
                    "seed": SEED,
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
                    "filename_prefix": f"isolda_{pose_name}_{n}",
                    "images": [f"d_{key}", 0]
                }
            }
            last_ksampler = f"k_{key}"
            
    return nodes

if __name__ == "__main__":
    wf = build_workflow()
    wf_path = os.path.join(B, "workflow_isolda_chained.json")
    with open(wf_path, "w", encoding="utf-8") as f:
        json.dump(wf, f, indent=2, ensure_ascii=False)
    print(f"Generated workflow JSON at: {wf_path}")
