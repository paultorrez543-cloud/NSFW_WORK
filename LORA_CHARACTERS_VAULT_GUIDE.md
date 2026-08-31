# 📚 LoRA Characters Vault — Guía Maestra de Personajes y Entrenamiento

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
* **Rasgos Físicos:** `demon girl, demon horns, curved horns, black horns, pointy ears, long hair, wavy hair, bangs, delicate face, curvy, hourglass figure, huge breasts, massive cleavage, heavy breasts, narrow waist, wide hips, huge ass, big ass, bubble butt, thick thighs`
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
$$\text{Pasos Totales (Total Steps)} = \frac{\text{Número de Imágenes} \times \text{Repeats (Repeticiones)} \times \text{Epochs (Épocas)}}{\text{Batch Size}}$$

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
---

## 💖 6. Generador Kamasutra Seductor (15 Poses x 5 Etapas = 75 Imágenes)

Para generar secuencias completas de seducción y placer para cualquiera de los 10 personajes, se utiliza el script:
[`build_vault_workflows_kamasutra.py`](file:///E:/ComfyUI/characters/build_vault_workflows_kamasutra.py)

### 🎭 Las 5 Etapas de Progresión Seductora:
1. **`01_seduccion` (Ropa Completa / Sin Pene):**
   * Pura seducción y teasing (`seductive smile, blush, looking at viewer, flirting, playful, teasing, parted_lips`).
   * Sin penetración ni pene visible (`no_penetration, teasing_pose`).
   * El nodo `MiDaS-DepthMapPreprocessor` extrae el mapa 3D limpio del cuerpo.
2. **`02_preliminares` (Ropa Semi-Abierta / Contacto Inminente):**
   * Ropa desabrochada y pechos expuestos (`clothing_undone, breasts_exposed`).
   * Contacto inicial y anticipación (`(imminent penetration:1.3), tip_touching, teasing, thigh_contact`).
3. **`03_primera_insercion` (Ropa Semi-Abierta / Primera Entrada):**
   * Pasión y placer intenso (`completely nude, pleasure, tears_of_pleasure, moaning`).
   * Entrada de la punta (`(tip_in_pussy:1.4), (first_insertion:1.3), stretching`).
4. **`04_extasis` (Ropa Semi-Abierta / Clímax y Ahegao):**
   * Máximo éxtasis (`ecstasy, ahegao, heart_pupils, drooling, excessive_sweat`).
   * Penetración profunda a fondo y corrida interna (`(deep penetration:1.6), (balls_deep:1.4), (creampie:1.3)`).
5. **`05_afterglow` (Totalmente Desnuda / Placer Satisfecho):**
   * Sonrisa de satisfacción y descanso (`afterglow, satisfied, gentle_smile, relaxed, sweat`).
   * Salida y derrame de semen (`(after_sex:1.3), (pull_out:1.3), (cum_leak:1.4), (gaping:1.3)`).

### 📐 Las 15 Poses Disponibles:
1. `01_cowgirl` (Vaquera Frontal)
2. `02_reverse_cowgirl` (Vaquera Invertida)
3. `03_doggystyle` (De Perrito)
4. `04_missionary` (Misionero Frontal)
5. `05_mating_press` (Mating Press Plegada)
6. `06_prone_bone` (Prone Bone - Boca Abajo)
7. `07_spooning` (Cucharita de Lado)
8. `08_standing_sex` (De Pie Contra Pared)
9. `09_bent_over` (Inclinada Sobre Mesa)
10. `10_seated_sex` (Sentados Cara a Cara / Lap Sit)
11. `11_piledriver` (Piledriver Invertido)
12. `12_paizuri` (Paizuri / Pechos)
13. `13_fellatio` (Sexo Oral de Rodillas)
14. `14_cunnilingus` (Cunnilingus / Placer Femenino)
15. `15_sixtynine` (Posición 69 Mutua)

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

---

### 3. 🎛️ Pussy Adjuster XL / Animagine (Slider LoRA)
* **Enlace / Modelo:** [Civitai - Pussy Adjuster XL](https://civitai.red/models/264525/pussyadjusterxlanimagine)
* **Model ID:** `264525`
* **Tipo:** Slider LoRA de Control Anatómico / Apertura
* **Archivo:** `pussy_adjuster_xl.safetensors`
* **Trigger Words:** `spread pussy, pussy spread, open pussy, labia spread`
* **Funcionamiento por Pesos (Slider):**
  * **Peso Positivo (`+0.6 a +1.0`):** Fuerza una apertura anatómica más amplia (`spread pussy`, ideal para etapas 3, 4 y 5 de penetración o gaping).
  * **Peso Negativo (`-0.6 a -1.0`):** Mantiene la zona cerrada o ajustada (ideal para preliminares o poses discretas).
* **Uso en ComfyUI:** Se carga en un `LoraLoader` con peso variable según la etapa de la secuencia.

---

## 📏 9. Guía Maestra de Tamaños de Cuerpos Femeninos y Proporciones Anatómicas

Para asegurar que cada personaje se genere con su anatomía exacta y evitar inconsistencias en SDXL e Illustrious, utiliza esta taxonomía estandarizada de etiquetas de Danbooru:

---

### 1. 👗 Silueta y Complexión General (Body Build)

| Tipo de Cuerpo | Tags Danbooru / Illustrious Recomendados | Descripción Visual |
|---|---|---|
| **Petite / Menuda** | `petite, short, small body, slender, delicate frame, small stature` | Estatura baja, huesos finos y cuerpo compacto. |
| **Esbelta / Delgada** | `slender, slim, thin, graceful, lean, delicate body` | Silueta clásica estilizada y elegante. |
| **Atlética / Tonificada** | `athletic, toned, fit, subtle abs, defined waist, muscular build` | Cuerpo firme, abdomen plano/marcado y piernas fuertes. |
| **Curvilínea / Reloj de Arena** | `curvy, hourglass figure, wide hips, narrow waist, voluptuous` | Cintura estrecha con pechos y caderas prominentes. |
| **Chubby / Muslos Gruesos** | `chubby, soft body, thick thighs, plump, chubby belly, full hips` | Cuerpo suave, curvas rellenas y muslos carnosos. |
| **Alta / Imponente** | `tall, long legs, slender and tall, statuesque, tall girl` | Piernas largas y porte alto. |

---

### 2. 👙 Escala de Tamaño de Pechos (Breast Sizes)

| Tamaño | Tags Recomendados | Nivel de Escote |
|---|---|---|
| **Plano (Flat)** | `flat chest, small breasts` | Pecho totalmente plano sin relieve. |
| **Pequeño (Small)** | `small breasts, subtle cleavage` | Busto discreto y firme. |
| **Mediano (Medium)** | `medium breasts, natural cleavage, perky breasts` | Proporción natural estándar (Copa B/C). |
| **Grande (Large)** | `large breasts, deep cleavage, sideboob, heavy breasts` | Busto prominente con escote profundo (Copa D/E). |
| **Muy Grande (Huge)** | `huge breasts, massive breasts, massive cleavage, sagging breasts` | Busto exagerado con peso visual notable (Copa F+). |
| **Gigante (Gigantic)** | `gigantic breasts, enormous breasts, hyper breasts` | Proporciones extremas de fantasía/hentai. |

---

### 3. 🍑 Caderas, Glúteos y Muslos (Hips & Thighs)

| Zona Anatómica | Nivel / Variación | Tags Recomendados |
|---|---|---|
| **Cintura** | Estrecha / Avispa | `narrow waist, slender waist, tiny waist, cinched waist` |
| **Caderas** | Anchas / Marcadas | `wide hips, broad hips, childbearing hips, pear figure` |
| **Glúteos** | Firme / Atlético | `small ass, firm ass, athletic buttocks, round ass` |
| **Glúteos** | Grande / Prominente | `huge ass, big ass, bubble butt, wide ass, plump buttocks` |
| **Muslos** | Gruesos / Carnosos | `thick thighs, chubby thighs, plump thighs, soft thighs` |
| **Muslos** | Delgados con espacio | `slender legs, thigh gap, thin legs` |

---

### 📋 4. Perfil Anatómico de los 10 Personajes del Vault:

1. **01. Elisia (Make Drama):** `curvy, hourglass figure, huge breasts, massive cleavage, heavy breasts, narrow waist, wide hips, huge ass, big ass, bubble butt, thick thighs, plump thighs`
2. **02. Isolda (Lost Sword):** `petite, slender, small breasts, flat chest, slim legs`
3. **03. Orihime Swimsuit (BBS):** `curvy, hourglass figure, large breasts, massive cleavage, wide hips, thick thighs`
4. **04. Morgana (Lost Sword):** `petite, flat chest, slender, narrow waist, small body`
5. **05. Ran (Lost Sword):** `athletic, toned body, large breasts, wide hips, thick thighs, muscular build`
6. **06. Claire (Lost Sword):** `slender, graceful, medium breasts, narrow waist, delicate frame`
7. **07. Nelliel Parasol (BBS):** `curvy, voluptuous, large breasts, massive cleavage, wide hips, round ass`
8. **08. Jennie (Make Drama):** `slender, office lady, slender waist, medium breasts, long legs`
9. **09. Marcia (Make Drama):** `petite, cute, small breasts, chubby thighs, narrow waist, petite body`
10. **10. Nelliel Heart (BBS):** `tan, dark skin, voluptuous, massive breasts, wide hips, thick thighs, round ass`

---

## 🎭 10. Catálogo de Outfits Alternativos, Iluminación y Moduladores Emocionales

Para personalizar al máximo cualquier personaje en ComfyUI, se han estandarizado los siguientes presets modulares:

---

### 👗 1. Catálogo de Outfits Alternativos (Outfit Switcher)

| Preset de Traje | Tags en Etapa 1 (Completa) | Tags en Etapa 2..4 (Semi-Abierta) |
|---|---|---|
| **Default** | Traje oficial del personaje | `clothing_undone, breasts_exposed, panties_pulled_aside` |
| **Bunny Girl** | `bunny suit, playboy bunny, black leotard, fake bunny ears, fishnet pantyhose, collar, cuffs, bow tie, high heels` | `bunny suit, open leotard, breasts_exposed, clothes_pulled_down, torn fishnet, bare breasts, bare pussy` |
| **French Maid** | `maid outfit, black maid dress, white apron, frilled headband, white thighhighs, detached sleeves, garter straps` | `maid outfit, unbuttoned maid dress, lifted apron, breasts_exposed, panties_pulled_aside, bare breasts, bare pussy` |
| **Lace Lingerie** | `black lace lingerie, see-through lingerie, lace bra, lace panties, garter belt, black thighhighs, sheer fabric` | `lace lingerie, bra pulled down, panties pushed aside, exposed breasts, bare nipples, bare pussy, sheer fabric` |
| **Micro Bikini** | `micro bikini, strappy bikini, string bikini, revealing swimwear, tie-side bottoms, cleavage, navel` | `micro bikini, bikini top pulled aside, bikini bottom untied, bare breasts, bare nipples, bare pussy` |
| **Office Lady** | `business attire, office lady, white collared shirt, black blazer, black pencil skirt, dark pantyhose, black high heels` | `office lady, unbuttoned collared shirt, open blazer, skirt lifted, torn pantyhose, exposed breasts, bare pussy` |
| **Gym / Spats** | `sports bra, tight spats, bicycle shorts, crop top, athletic wear, bare shoulders, bare midriff` | `sports bra pulled up, spats pulled down, breasts_exposed, bare breasts, bare nipples, bare pussy, glistening skin` |

---

### 🕯️ 2. Presets de Iluminación y Atmósfera (Lighting Switcher)

1. **Dark Sensual (Por Defecto):**
   `dark background, blurry background, depth of field, bokeh, dim lighting, dark room, soft rim light, cinematic lighting`
2. **Luz de Velas Cálida (Candlelight):**
   `dark background, blurry background, candlelight, warm lighting, candle flame, flickering light, intimate atmosphere, golden glow, deep shadows`
3. **Red Room / Neón Sensual:**
   `dark background, blurry background, neon lights, red room, magenta lighting, deep blue shadows, cyberpunk rim light, moody atmosphere`
4. **Golden Hour (Atardecer Dorado):**
   `dark background, blurry background, golden hour, sunset lighting, sunbeams through blinds, warm glow, volumetric light, cinematic`

---

### 🎚️ 3. Moduladores de Expresión y Emociones por Etapa

* **Etapa 1 (Seducción):** `seductive smile, light blush, looking at viewer, flirting, playful, teasing, parted_lips`
* **Etapa 2 (Preliminares):** `blushing deeply, heavy_breathing, parted_lips, moaning, excited, anticipation, lust, glistening skin, light sweat`
* **Etapa 3 (Inserción):** `pleasure, tears_of_pleasure, blushing, open_mouth, heavy_breathing, panting, moaning, sweat drops, flushed skin`
* **Etapa 4 (Éxtasis / Ahegao):** `ecstasy, intense_pleasure, ahegao, heart_pupils, drooling, open_mouth, excessive_sweat, eye_contact, tears_of_pleasure, heavy panting`
* **Etapa 5 (Afterglow):** `afterglow, satisfied, gentle_smile, blushing, heavy_breathing, sweat, relaxed, exhausted_smile, half-closed eyes`

---

## 🎛️ 11. Suite de Flujos Maestros ControlNet SDXL (5 Modalidades por Personaje)

Cada una de las 10 chicas del Vault cuenta con **5 flujos especializados** diseñados con arquitectura de **Raíz Única** (1 solo cálculo del mapa, distribuido a las 5 etapas en paralelo):

| Archivo de Flujo | Modelo ControlNet | Preprocesador | Cuándo Usarlo |
|---|---|---|---|
| [`workflow_<char>_manual_controlnet.json`](file:///E:/ComfyUI/characters/elisia_make_drama/workflow_elisia_manual_controlnet.json) | `controlnet-depth-sdxl-1.0.safetensors` | `MiDaS` (Resolución 1024) | Poses 3D complejas de **Pareja**, volumen corporal y contactos íntimos apretados. |
| [`workflow_<char>_manual_openpose.json`](file:///E:/ComfyUI/characters/elisia_make_drama/workflow_elisia_manual_openpose.json) | `controlnet-openpose-sdxl.safetensors` | `OpenposePreprocessor` (1024) | Dibujos **Anime 2D**, calcar posturas exactas ignorando la ropa de la imagen original. |
| [`workflow_<char>_manual_canny.json`](file:///E:/ComfyUI/characters/elisia_make_drama/workflow_elisia_manual_canny.json) | `controlnet-canny-sdxl.safetensors` | `Canny` (100 / 200) | **Lineart y contornos exactos** de bocetos o ilustraciones limpias. |
| [`workflow_<char>_manual_solo.json`](file:///E:/ComfyUI/characters/elisia_make_drama/workflow_elisia_manual_solo.json) | `controlnet-depth-sdxl-1.0.safetensors` | `MiDaS` (Resolución 1024) | Fotos de la chica **sola** o en perspectiva **POV / Paizuri en regazo** (cero deformidades). |
| [`workflow_<char>_double_penetration.json`](file:///E:/ComfyUI/characters/elisia_make_drama/workflow_elisia_double_penetration.json) | `controlnet-depth-sdxl-1.0.safetensors` | `MiDaS` (Resolución 1024) | **3 Actores** (Ella + 2 Hombres), 2 penises reales anatómicos, doble penetración simultánea. |
| [`workflow_<char>_manual_tree_delta.json`](file:///E:/ComfyUI/characters/elisia_make_drama/workflow_elisia_manual_tree_delta.json) | `controlnet-depth-sdxl-1.0.safetensors` | `MiDaS` (Resolución 1024) | **Árbol Multi-Rama Completo** con 10 ramas (Vaginal, Sub-Ramas Deep Thrust, Cervical Crying, Anal, 04-Delta Deep Penetration sin balls, y 05-Delta Orina/Squirt). |
| [`workflow_<char>_pure_prompt.json`](file:///E:/ComfyUI/characters/elisia_make_drama/workflow_elisia_pure_prompt.json) | **NINGUNO (Puro Prompt)** | *Sin Preprocesador* | **10 Etapas Ultra-Rápidas Sin ControlNet**: Generación libre con máximo deep penetration (90% adentro / 10% visible), ahegao extremo con lengua afuera y cero dependencias de imágenes. |

---

## ⚡ 13. Suite de Flujos Prompts Puros (SIN ControlNet)

El flujo [`workflow_<char>_pure_prompt.json`](file:///E:/ComfyUI/characters/elisia_make_drama/workflow_elisia_pure_prompt.json) permite generar la progresión completa de 10 imágenes al instante sin necesidad de cargar ninguna imagen de pose ni calcular mapas de profundidad:

* **⚡ Velocidad Máxima:** 0% de retraso de preprocesadores o carga de ControlNet.
* **🍆 Penetración Cervical Profunda:** `((deep_penetration:1.6)), ((full_insertion:1.6)), ((almost_entire_penis_inside_pussy:1.5)), ((only_base_of_penis_visible:1.4))` (90% enterrado adentro / 10% visible, cero balls).
* **👅 Ahegao & Expresiones Extremas:** `((extreme_ahegao:1.5)), ((tongue_out:1.5)), ((drooling:1.4)), ((heart_pupils:1.4)), ((sweet_pain:1.3)), ((crying_with_pleasure:1.4))`.
* **🔒 Semilla Fija Idéntica:** Mantiene la coherencia facial y física en las 10 etapas en paralelo.


