import os

doc_interracial = """
---

## ⚡ 8. Generador Kamasutra Interracial Chained (LoRA Personaje + LoRA BBC)

Para generar secuencias que combinen automáticamente el LoRA del personaje con el LoRA de concepto interracial (`lora_bbc_interracial.safetensors`), se utiliza:
[`build_vault_workflows_kamasutra_interracial.py`](file:///E:/ComfyUI/characters/build_vault_workflows_kamasutra_interracial.py)

### 🔗 Estructura de Nodos Encadenados:
* **Node 1 (Checkpoint):** `illustrious-xl-v0.1.safetensors`
* **Node 2 (LoRA 1 - Personaje):** `lora_<personaje>.safetensors` (Fuerza: `0.85`)
* **Node 3 (LoRA 2 - Concepto):** `lora_bbc_interracial.safetensors` (Fuerza: `0.70`)
* **Node 4 (ControlNet Depth):** `controlnet-depth-sdxl-1.0.safetensors`
* **Prompts:** Integra automáticamente los tags `dark-skinned male, interracial, bbc_int, dark skin male, muscular male, large penis, skin tone contrast` en las etapas 2, 3, 4 y 5 manteniendo la ropa semi-abierta hasta la etapa 4.
"""

guides = [
    r"C:\Users\NEO\Downloads\LoRA_Characters_Vault\LORA_CHARACTERS_VAULT_GUIDE.md",
    r"E:\ComfyUI\characters\LORA_CHARACTERS_VAULT_GUIDE.md"
]

for g in guides:
    if os.path.exists(g):
        with open(g, "r", encoding="utf-8") as f:
            c = f.read()
        if "## ⚡ 8. Generador Kamasutra Interracial" not in c:
            c += doc_interracial
            with open(g, "w", encoding="utf-8") as f:
                f.write(c)
            print("[OK] Documented Section 8 in:", g)
