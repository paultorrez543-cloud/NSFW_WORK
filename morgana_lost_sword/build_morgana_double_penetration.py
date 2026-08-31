import os
import json
import sys

# Dedicated builder for Morgana Double Penetration (DP) workflow
sys.path.append(r"E:\ComfyUI\characters")
from build_vault_workflows_double_penetration import CHARACTERS, generate_dp_manual_workflow

def build():
    char_cfg = CHARACTERS["morgana_lost_sword"]
    wf = generate_dp_manual_workflow("morgana_lost_sword", char_cfg)
    out_path = os.path.join(os.path.dirname(__file__), "workflow_morgana_double_penetration.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(wf, f, indent=2)
    print("Generated DP workflow JSON at:", out_path)

if __name__ == "__main__":
    build()
