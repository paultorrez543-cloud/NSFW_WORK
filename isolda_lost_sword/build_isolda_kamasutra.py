import os
import json
import sys

# Dedicated builder for Isolda Kamasutra workflow
sys.path.append(r"E:\ComfyUI\characters")
from build_vault_workflows_kamasutra import CHARACTERS, generate_kamasutra_workflow

def build():
    char_cfg = CHARACTERS["isolda_lost_sword"]
    wf = generate_kamasutra_workflow("isolda_lost_sword", char_cfg)
    out_path = os.path.join(os.path.dirname(__file__), "workflow_isolda_kamasutra.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(wf, f, indent=2)
    print("Generated Kamasutra workflow JSON at:", out_path)

if __name__ == "__main__":
    build()
