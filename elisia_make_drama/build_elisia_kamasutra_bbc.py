import os
import json
import sys

# Dedicated builder for Elisia Kamasutra BBC Interracial workflow
sys.path.append(r"E:\ComfyUI\characters")
from build_vault_workflows_kamasutra_interracial import CHARACTERS, generate_kamasutra_interracial_workflow

def build():
    char_cfg = CHARACTERS["elisia_make_drama"]
    wf = generate_kamasutra_interracial_workflow("elisia_make_drama", char_cfg)
    out_path = os.path.join(os.path.dirname(__file__), "workflow_elisia_kamasutra_bbc.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(wf, f, indent=2)
    print("Generated Kamasutra BBC workflow JSON at:", out_path)

if __name__ == "__main__":
    build()
