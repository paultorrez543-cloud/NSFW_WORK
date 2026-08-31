import os
import json
import sys

# Dedicated builder for Isolda Manual ControlNet workflow
sys.path.append(r"E:\ComfyUI\characters")
from build_vault_manual_controlnet_workflows import CHARACTERS, generate_manual_controlnet_workflow

def build():
    char_cfg = CHARACTERS["isolda_lost_sword"]
    wf = generate_manual_controlnet_workflow("isolda_lost_sword", char_cfg)
    out_path = os.path.join(os.path.dirname(__file__), "workflow_isolda_manual_controlnet.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(wf, f, indent=2)
    print("Generated Manual ControlNet workflow JSON at:", out_path)

if __name__ == "__main__":
    build()
