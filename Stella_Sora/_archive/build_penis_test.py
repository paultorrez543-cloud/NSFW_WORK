#!/usr/bin/env python3
"""Genera workflow de test: penis size slider × 4 fuerzas para Virigia."""
import json, os

OUT = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
SEED = 42424249

TRIGGER = "stell4virigiadef"
DESC = "1girl, white hair, long hair, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, large breasts"
OUTFIT = "white bonnet, white cloak, frilled cloak, black dress, see-through dress, black gloves, white pantyhose, high heels, holding mirror"
NEG = "lowres, bad anatomy, bad eyes, deformed eyes, bad hands, extra fingers, worst_quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, white background"
STYLE = "dimly_lit, low_light, dark_ambiance, soft_lighting, (dark lighting:1.5), (dim room:1.4), depth_of_field, anime, cel shading, masterpiece, best_quality, absurdres"

PROMPT = f"{TRIGGER}, {DESC}, {OUTFIT}, clothes_lift, clothes_pulled_aside, 1boy, male, faceless male, head_out_of_frame, male_from_neck_down, male_body_only, female_focus, missionary_position, male_on_top, female_on_bottom, vaginal_penetration, penetration, blush, sweat, {STYLE}"

TESTS = [
    ("gigante", -1.0, "-1.0"),
    ("grande",  -0.5, "-0.5"),
    ("normal",   0.0, "0.0"),
    ("chico",    0.5, "+0.5"),
]

nodes = {}
nodes["ckpt"] = {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}}
nodes["lora_char"] = {"class_type": "LoraLoader", "inputs": {"model": ["ckpt",0], "clip": ["ckpt",1], "lora_name": "Stella-Virigia-v1.safetensors", "strength_model": 0.8, "strength_clip": 0.8}}

for i, (label, strength, tag) in enumerate(TESTS):
    sid = f"lora_size_{i}"
    nodes[sid] = {"class_type": "LoraLoader", "inputs": {"model": ["lora_char",0], "clip": ["lora_char",1], "lora_name": "Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors", "strength_model": strength, "strength_clip": strength}}
    
    neg_id = f"neg_{i}"
    nodes[neg_id] = {"class_type": "CLIPTextEncode", "inputs": {"text": NEG, "clip": [sid,1]}}
    
    nodes[f"e_{i}"] = {"class_type": "EmptyLatentImage", "inputs": {"width": 832, "height": 1216, "batch_size": 1}}
    nodes[f"p_{i}"] = {"class_type": "CLIPTextEncode", "inputs": {"text": PROMPT, "clip": [sid,1]}}
    nodes[f"k_{i}"] = {"class_type": "KSampler", "inputs": {"seed": SEED, "steps": 28, "cfg": 4.0, "sampler_name": "dpmpp_2m", "scheduler": "karras", "denoise": 1, "model": [sid,0], "positive": [f"p_{i}",0], "negative": [neg_id,0], "latent_image": [f"e_{i}",0]}}
    nodes[f"d_{i}"] = {"class_type": "VAEDecode", "inputs": {"samples": [f"k_{i}",0], "vae": ["ckpt",2]}}
    nodes[f"s_{i}"] = {"class_type": "SaveImage", "inputs": {"filename_prefix": f"virigia_penis_test_{label}", "images": [f"d_{i}",0]}}

fpath = os.path.join(OUT, "workflow_penis_size_test.json")
with open(fpath, "w", encoding="utf-8") as f:
    json.dump(nodes, f, indent=2, ensure_ascii=False)

print(f"✅ {fpath}")
for label, strength, tag in TESTS:
    print(f"   virigia_penis_test_{label}: strength={tag}")
print(f"\n🔒 seed={SEED} | 4 txt2img | mismo prompt | solo cambia penis slider")
