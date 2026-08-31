import os

content = """# 📚 LoRA Characters Vault — Guía Maestra de Personajes y Entrenamiento

Bienvenido a la **Bóveda Maestra de Personajes LoRA (LoRA Characters Vault)** para **Illustrious SDXL**, **SDXL** y **ComfyUI**.

Este documento recopila la documentación técnica completa de todos los personajes actuales, sus palabras desencadenantes (**Trigger Words**), rasgos de anatomía, vestimentas, parámetros de entrenamiento en Google Colab con **Kohya_ss / sd-scripts**, y la plantilla estandarizada para agregar **futuros personajes**.

---

## 📑 Índice
1. [Personajes Actuales en el Vault (1 al 8)](#-1-personajes-actuales-en-el-vault)
2. [Nuevos Personajes Agregados (9 y 10)](#-2-nuevos-personajes-agregados)
3. [Guía de Pasos, Repeticiones y Parámetros de Entrenamiento](#-3-guía-de-pasos-repeticiones-y-parámetros-de-entrenamiento)
4. [Plantilla Estandarizada para Futuros Personajes](#-4-plantilla-estandarizada-para-futuros-personajes)
5. [Guía de Integración Rápida con ComfyUI](#-5-guía-de-integración-rápida-con-comfyui)

---

## 🏛️ 1. Personajes Actuales en el Vault

### 01. Elisia (Make Drama)
* **Carpeta Vault:** `01_Elisia_Make_Drama`
* **Archivo LoRA:** `lora_elisia_make_drama.safetensors`
* **Peso Sugerido en ComfyUI:** `0.85`
* **Trigger Principal:** `elisia_(make_drama), elisia, make drama, 1girl, solo`
* **Rasgos Físicos:** `demon girl, demon horns, curved horns, black horns, pointy ears, long hair, wavy hair, bangs, delicate face`
* **Outfit Default:** `open collar shirt, black crop top, high-waisted shorts, black shorts, belt, thong, visible thong, high heels, bare shoulders, bare midriff`

---

### 02. Isolda (Lost Sword)
* **Carpeta Vault:** `02_Isolda_Lost_Sword`
* **Archivo LoRA:** `lora_isolda_lost_sword.safetensors`
* **Peso Sugerido en ComfyUI:** `0.85`
* **Trigger Principal:** `isolda_(lost_sword), isolda, 1girl, solo`
* **Rasgos Físicos:** `purple hair, short hair, hair between eyes, yellow eyes, small breasts`
* **Outfit Default:** `detailed dress, black dress, armor, pauldrons, breastplate, white cape, black gloves, thighhighs, boots, high heels`

---

### 03. Orihime Swimsuit (Bleach Brave Souls)
* **Carpeta Vault:** `03_Orihime_Swimsuit`
* **Archivo LoRA:** `lora_orihime_swimsuit.safetensors`
* **Peso Sugerido en ComfyUI:** `0.85`
* **Trigger Principal:** `orihime_swimsuit, inoue orihime, bleach, bleach brave souls, 1girl, solo`
* **Rasgos Físicos:** `orange hair, long hair, bangs, grey eyes, large breasts, massive cleavage, wide hips, hair clip`
* **Outfit Default:** `white bikini, halterneck bikini, micro bikini, ribbon on bikini, sarong, pareo, beach, flower in hair`

---

### 04. Morgana (Lost Sword)
* **Carpeta Vault:** `04_Morgana_Lost_Sword`
* **Archivo LoRA:** `lora_morgana_lost_sword.safetensors`
* **Peso Sugerido en ComfyUI:** `0.85`
* **Trigger Principal:** `morgana_(lost_sword), morgana, 1girl, solo`
* **Rasgos Físicos:** `red hair, long hair, wavy hair, red eyes, large breasts, seductive`
* **Outfit Default:** `black dress, seductive dress, cleavage cutout, bare shoulders, thigh slit, high heels, jewelry`

---

### 05. Ran (Lost Sword)
* **Carpeta Vault:** `05_Ran_Lost_Sword`
* **Archivo LoRA:** `lora_ran_lost_sword.safetensors`
* **Peso Sugerido en ComfyUI:** `0.85`
* **Trigger Principal:** `ran_(lost_sword), ran, 1girl, solo`
* **Rasgos Físicos:** `blue hair, short hair, blue eyes, athletic, medium breasts`
* **Outfit Default:** `ninja outfit, tactical gear, black sleeveless bodysuit, arm guards, leg guards, scarf`

---

### 06. Claire (Lost Sword)
* **Carpeta Vault:** `06_Claire_Lost_Sword`
* **Archivo LoRA:** `lora_claire_lost_sword.safetensors`
* **Peso Sugerido en ComfyUI:** `0.80`
* **Trigger Principal:** `claire_(lost_sword), claire, 1girl, solo`
* **Rasgos Físicos:** `gray hair, long hair, blindfold, blindfold covering eyes, not visible eyes`
* **Outfit Default:** `nun, veil, white veil, nun habit, detached sleeves, detailed white dress, gold accents`

---

### 07. Nelliel Parasol (Bleach Brave Souls)
* **Carpeta Vault:** `07_Nelliel_Parasol`
* **Archivo LoRA:** `lora_nelliel_parasol.safetensors`
* **Peso Sugerido en ComfyUI:** `0.85`
* **Trigger Principal:** `nelliel_parasol, nelliel tu odelschwanck, bleach, bleach brave souls, 1girl, solo`
* **Rasgos Físicos:** `green hair, green eyes, ram skull, hollow mask on head, facial mark, red facial stripe, large breasts, massive cleavage`
* **Outfit Default:** `open floral kimono robe, open kimono, floral kimono, bikini top, sarong, bare legs, bare shoulders`

---

### 08. Jennie (Make Drama)
* **Carpeta Vault:** `08_Jennie_Make_Drama`
* **Archivo LoRA:** `lora_jennie_make_drama.safetensors`
* **Peso Sugerido en ComfyUI:** `0.85`
* **Trigger Principal:** `jennie_(make_drama), jennie, make drama, 1girl, solo`
* **Rasgos Físicos:** `brown hair, long hair, brown eyes, delicate face, slender`
* **Outfit Default:** `office lady, white blouse, pencil skirt, black skirt, collared shirt, necktie, pantyhose, high heels`

---

## 🌟 2. Nuevos Personajes Agregados

### 09. Marcia (Make Drama)
* **Carpeta Vault:** `09_Marcia_Make_Drama`
* **Archivo LoRA Previsto:** `lora_marcia_make_drama.safetensors`
* **Peso Sugerido en ComfyUI:** `0.85 - 1.0`
* **Trigger Principal:** `marcia_(make_drama), marcia, make drama, 1girl, solo`
* **Rasgos Físicos:** `pink hair, twintails, high twintails, long hair, heart ahoge, purple eyes, fang, smirking, cute, petite, chubby thighs, barcode on thigh, bandaid on knee`
* **Outfit Default:** `futuristic bodysuit, highleg leotard, black and white bodysuit, cleavage cutout, white jacket, crop jacket, detached jacket, black gloves, asymmetric legwear, black thighhigh, single thighhigh, garter strap, mechanical boots, oversized cannon`

---

### 10. Nelliel [Heart / Swimsuit] (Bleach Brave Souls)
* **Carpeta Vault:** `10_Nelliel_Heart`
* **Archivo LoRA Previsto:** `lora_nelliel_heart.safetensors`
* **Peso Sugerido en ComfyUI:** `0.85 - 1.0`
* **Trigger Principal:** `nelliel_swimsuit, nelliel tu odelschwanck, bleach, bleach brave souls, 1girl, solo`
* **Rasgos Físicos:** `tan, dark skin, green hair, wavy hair, long hair, green eyes, ram skull, hollow mask on head, facial mark, red facial stripe, large breasts, massive cleavage, wide hips`
* **Outfit Swimsuit:** `white bikini, halterneck bikini top, side-tie bikini bottom, yellow sarong, yellow pareo, floral pareo, beaded necklace, flower on waist`

---

## ⚙️ 3. Guía de Pasos, Repeticiones y Parámetros de Entrenamiento

### 📐 Fórmula Maestra de Pasos Totales
$$\\text{Pasos Totales (Total Steps)} = \\frac{\\text{Número de Imágenes} \\times \\text{Repeats (Repeticiones)} \\times \\text{Epochs (Épocas)}}{\\text{Batch Size}}$$

---

### 📊 Tabla de Configuración Recomendada según el Tamaño del Dataset

| Tipo de Dataset | Cantidad de Imágenes | Repeticiones (`REPEATS`) | Épocas (`EPOCHS`) | Pasos Totales (`Total Steps`) | Objetivo y Comportamiento |
|---|---|---|---|---|---|
| **Micro-Dataset** (Recortes de 1 sola fuente) | **5 – 7 imágenes** | **30 – 40** | **10** | **1,500 – 2,000 pasos** | Necesario para que el LoRA aprenda la cara y ropa sin quedarse 'crudo'. |
| **Dataset Pequeño** | **10 – 15 imágenes** | **10 – 15** | **10** | **1,200 – 1,800 pasos** | Buen balance para personajes con 1 o 2 trajes. |
| **Dataset Estándar / Curado** (Recomendado) | **20 – 35 imágenes** | **6 – 8** | **10** | **1,500 – 2,500 pasos** | ⭐ **Ideal**: Aprende múltiples poses, expresiones y permite desvestirse con facilidad. |
| **Dataset Grande** (Multi-outfit) | **40 – 60 imágenes** | **3 – 5** | **10** | **1,800 – 3,000 pasos** | Ideal para personajes con 3 o más atuendos completos. |

---

### 💾 Estrategia de Checkpoints por Épocas (`--save_every_n_epochs=2`)

Al entrenar con **10 épocas** y guardar cada 2 épocas, obtendrás 5 archivos `.safetensors`:

* **Época 2 (~400 pasos):** *LoRA Inicial*. Fija la paleta de colores base y silueta.
* **Época 4 (~800 pasos):** *LoRA Temprano*. Rasgos faciales claros y estructura general.
* **Época 6 (~1,200 pasos):** ⭐ **Punto Óptimo de Flexibilidad**. Excelente parecido y máxima respuesta a cambios de poses/ropa.
* **Época 8 (~1,600 pasos):** ⭐ **Punto Óptimo de Fidelidad**. Máximo parecido idéntico al arte oficial con alta definición.
* **Época 10 (~2,000 pasos):** *LoRA Final*. Fidelidad absoluta. Si notas que fuerza demasiado la pose original, baja a la Época 8 o 6.

---

### 🛠️ Parámetros Técnicos en Kohya_ss (`sdxl_train_network.py`)

| Parámetro | Valor Recomendado | Explicación |
|---|---|---|
| **Base Model** | `illustrious-xl-v0.1.safetensors` o `rinIllusionRNSFW_v30.safetensors` | Modelo base SDXL Anime |
| **Network Dim (Rank)** | `32` (o `16`) | Capacidad suficiente para aprender anatomía sin sobreajuste |
| **Network Alpha** | `16` (o `8`) | Relación estándar 0.5x con el Rank |
| **Resolution** | `1024,1024` (`--enable_bucket`) | Mantiene la máxima resolución de detalle con bucketing (512 - 2048) |
| **Learning Rate** | `1e-4` (U-Net) / `5e-5` (Text Encoder) | Tasa de aprendizaje óptima para SDXL |
| **LR Scheduler** | `cosine` con 50 warmup steps | Decaimiento suave para evitar artefactos visuales |
| **Optimizer** | `AdamW8bit` | Ahorro de VRAM para GPUs Colab (T4 / L4 / A100) |
| **Cache Latents** | `--cache_latents --cache_latents_to_disk` | Acelera el entrenamiento x3 veces en Colab |
| **Precision** | `fp16` o `bf16` | Precisión mixta rápida con `--fp8_base` |

---

## 📝 4. Plantilla Estandarizada para Futuros Personajes

Cuando agregues un nuevo personaje a este Vault, sigue esta plantilla:

```markdown
### [Número]. [Nombre del Personaje] ([Nombre del Juego / Franquicia])
* **Carpeta Vault:** `[Numero]_[Nombre_Personaje]_[Franquicia]`
* **Archivo LoRA:** `lora_[nombre_personaje].safetensors`
* **Peso Sugerido en ComfyUI:** `0.85`
* **Trigger Principal:** `[trigger_name], [nombre], [franquicia], 1girl, solo`
* **Rasgos Físicos:** `[color de pelo], [peinado], [color de ojos], [tipo de cuerpo], [detalles unicos como tatuajes, cuernos, marcas]`
* **Outfit 1 (Default):** `[prenda superior], [prenda inferior], [calzado], [accesorios]`
* **Outfit 2 (Alternativo):** `[descripción del segundo atuendo si existe]`
```

### Reglas de Etiquetado para el Dataset (`.txt`):
1. **Trigger único:** Siempre al inicio (`nombre_personaje, franquicia, 1girl, solo`).
2. **Separación de Outfit:** No incluyas la ropa en el trigger principal. Permite que el LoRA aprenda la ropa por separado para que el personaje pueda desvestirse o cambiar de atuendo libremente.
3. **Variedad de Planos:** El dataset debe contener al menos:
   - 2 fotos de cuerpo completo (`full body, standing`)
   - 2 fotos de plano medio (`upper body`)
   - 2 primeros planos de rostro (`portrait, close-up, face`)
   - 1 toma de detalles o ropa (`thighs focus, cleavage focus`)

---

## 🔄 5. Guía de Integración Rápida con ComfyUI

Una vez entrenado el archivo `.safetensors`, colócalo en tu carpeta de LoRAs de ComfyUI (`models/loras/`) y conéctalo al nodo `LoraLoader`:
* **Strength Model:** `0.85`
* **Strength CLIP:** `1.0`
* **Prompt Positivo:**
  ```text
  score_9, score_8_up, source_anime, rating_explicit,
  [TRIGGER_DEL_PERSONAJE], [RASGOS_FISICOS], [OUTFIT_O_DESNUDO],
  [ACCION_O_POSE], masterpiece, best_quality
  ```
"""

paths = [
    r"C:\Users\NEO\Downloads\LoRA_Characters_Vault\LORA_CHARACTERS_VAULT_GUIDE.md",
    r"E:\ComfyUI\characters\LORA_CHARACTERS_VAULT_GUIDE.md"
]

for p in paths:
    with open(p, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print("[OK] Overwritten guide at:", p)
