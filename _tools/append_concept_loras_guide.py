import os

section_7 = """
---

## 🧩 7. LoRAs de Concepto, Interacción y Modelos ADetailer

Además de los LoRAs de personajes, estos modelos y LoRAs complementarios se utilizan para mejorar la interacción, el contraste visual y la precisión anatómica en ComfyUI:

---

### 1. 🖤 BBC Interracial (Concept LoRA)
* **Enlace / Modelo:** [Civitai - BBC Interracial](https://civitai.red/models/2526457/bbc-interracial)
* **Tipo:** LoRA de Concepto / Interacción
* **Archivo:** `lora_bbc_interracial.safetensors`
* **Peso Recomendado en ComfyUI:** `0.60 - 0.80` (para no interferir con la cara del personaje femenino)
* **Trigger Words Principales:** `dark-skinned male, interracial, bbc_int`
* **Tags Complementarios:** `dark skin male, muscular male, tall male, large penis, skin tone contrast, height difference`
* **Uso en Flujos:** Se encadena en un segundo nodo `LoraLoader` o en `LoraLoaderStack` junto al LoRA del personaje.

---

### 2. 🔍 Pussy ADetailer (Modelo de Detalle Anatómico / Impact Pack)
* **Enlace / Modelo:** [Civitai - Pussy ADetailer](https://civitai.red/models/150234/pussy-adetailer)
* **Tipo:** Modelo Detector YOLO / LoRA de Refinamiento Anatómico
* **Ubicación en ComfyUI:**
  * Si es modelo YOLO (`.pt`): `ComfyUI/models/ultralytics/bbox/` o `segm/`
  * Si es LoRA (`.safetensors`): `ComfyUI/models/loras/`
* **Uso con ComfyUI Impact Pack:**
  * Conectar el modelo al nodo `UltralyticsDetectorProvider` o `FaceDetailer` / `DetailerForeach`.
  * **Guía de Inpainting:** Denoise `0.35 - 0.45` con prompt `detailed pussy, bare pussy, masterpiece, best quality`.
  * **Beneficio:** Corrige automáticamente cualquier imperfección anatómica en planos generales o medios sin deformar el resto de la imagen.
"""

guides = [
    r"C:\Users\NEO\Downloads\LoRA_Characters_Vault\LORA_CHARACTERS_VAULT_GUIDE.md",
    r"E:\ComfyUI\characters\LORA_CHARACTERS_VAULT_GUIDE.md"
]

for g in guides:
    if os.path.exists(g):
        with open(g, "r", encoding="utf-8") as f:
            c = f.read()
        if "## 🧩 7. LoRAs de Concepto" not in c:
            c += section_7
            with open(g, "w", encoding="utf-8") as f:
                f.write(c)
            print("[OK] Appended Section 7 in:", g)
