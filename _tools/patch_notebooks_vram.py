import os
import json

vault_dir = r"C:\Users\NEO\Downloads\LoRA_Characters_Vault"

for root, dirs, files in os.walk(vault_dir):
    for f in files:
        if f.endswith(".ipynb"):
            nb_path = os.path.join(root, f)
            with open(nb_path, "r", encoding="utf-8") as nbf:
                nb = json.load(nbf)
            
            if len(nb["cells"]) >= 7:
                cell6 = nb["cells"][6]
                src = "".join(cell6.get("source", []))
                
                # Replace purge logic
                if "if 'pipe' in globals():" not in src:
                    src = src.replace(
                        "import torch, gc, os",
                        "import torch, gc, os\n\nif 'pipe' in globals():\n    del pipe\ngc.collect()\ntorch.cuda.empty_cache()"
                    )
                
                # Replace .to('cuda') with enable_model_cpu_offload()
                src = src.replace(").to('cuda')", ")")
                if "pipe.enable_model_cpu_offload()" not in src:
                    src = src.replace(
                        "use_safetensors=True\n    )",
                        "use_safetensors=True\n    )\n    pipe.enable_model_cpu_offload()"
                    )
                    src = src.replace(
                        "use_safetensors=True\n)",
                        "use_safetensors=True\n)\npipe.enable_model_cpu_offload()"
                    )
                
                cell6["source"] = [l + "\n" for l in src.split("\n")]
                with open(nb_path, "w", encoding="utf-8") as nbf:
                    json.dump(nb, nbf, indent=2)
                print("[OK] Configured enable_model_cpu_offload() in:", f)
