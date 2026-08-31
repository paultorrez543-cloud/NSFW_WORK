import os
import shutil
import zipfile
import json
from PIL import Image

VAULT_DIR = r"C:\Users\NEO\Downloads\LoRA_Characters_Vault"

def build_notebook(char_name, char_folder, trigger, zip_name, lora_out):
    nb = {
        "nbformat": 4,
        "nbformat_minor": 0,
        "metadata": {
            "accelerator": "GPU",
            "colab": {
                "name": f"Entrenar_LoRA_{char_folder}_Colab.ipynb",
                "provenance": []
            },
            "kernelspec": {
                "display_name": "Python 3",
                "name": "python3"
            },
            "language_info": {
                "name": "python"
            }
        },
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# 🚀 Entrenamiento de LoRA: {char_name} (SDXL / Illustrious)\n",
                    f"### Modelo Base: Illustrious-XL v0.1 | Framework: Kohya_ss sd-scripts\n",
                    "---\n",
                    "Sigue las celdas en orden para instalar dependencias, cargar el dataset y entrenar el LoRA."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# @title 1. Instalar dependencias y clonar sd-scripts\n",
                    "!git clone --depth 1 https://github.com/kohya-ss/sd-scripts.git\n",
                    "%cd sd-scripts\n",
                    "!pip install -q --upgrade pip\n",
                    "!pip install -q torch==2.1.2 torchvision==0.16.2 --index-url https://download.pytorch.org/whl/cu121\n",
                    "!pip install -q --upgrade -r requirements.txt\n",
                    "!pip install -q xformers==0.0.23.post1 bitsandbytes lion-pytorch prodigy-opt accelerate"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# @title 2. Descargar Modelo Base (Illustrious-XL)\n",
                    "!mkdir -p /content/models\n",
                    "!wget -c -O /content/models/illustrious-xl-v0.1.safetensors \"https://huggingface.co/OnomaAIResearch/Illustrious-xl-early-release-v0-1/resolve/main/Illustrious-XL-v0.1.safetensors\""
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    f"# @title 3. Preparar Dataset de {char_name}\n",
                    "import os, zipfile\n",
                    f"!mkdir -p /content/dataset/8_{trigger}\n",
                    f"!mkdir -p /content/output/{char_folder}\n",
                    "\n",
                    f"# Sube el archivo '{zip_name}' a /content/ o usa Google Drive\n",
                    f"if os.path.exists('/content/{zip_name}'):\n",
                    f"    with zipfile.ZipFile('/content/{zip_name}', 'r') as z:\n",
                    f"        z.extractall('/content/dataset/8_{trigger}')\n",
                    f"    print('Dataset extraído correctamente en /content/dataset/8_{trigger}')\n",
                    "else:\n",
                    f"    print('Por favor, sube el archivo {zip_name} a /content/')\n"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    f"# @title 4. Iniciar Entrenamiento de LoRA ({char_name})\n",
                    "import os\n",
                    "os.chdir('/content/sd-scripts')\n",
                    "!accelerate launch --mixed_precision=fp16 --num_cpu_threads_per_process 2 \\\n",
                    "  /content/sd-scripts/sdxl_train_network.py \\\n",
                    "  --pretrained_model_name_or_path=\"/content/models/illustrious-xl-v0.1.safetensors\" \\\n",
                    "  --train_data_dir=\"/content/dataset\" \\\n",
                    f"  --output_dir=\"/content/output/{char_folder}\" \\\n",
                    f"  --output_name=\"{lora_out}\" \\\n",
                    "  --save_model_as=\"safetensors\" \\\n",
                    "  --network_module=\"networks.lora\" \\\n",
                    "  --network_dim=32 \\\n",
                    "  --network_alpha=16 \\\n",
                    "  --resolution=\"1024,1024\" \\\n",
                    "  --enable_bucket \\\n",
                    "  --min_bucket_reso=512 \\\n",
                    "  --max_bucket_reso=1536 \\\n",
                    "  --learning_rate=1e-4 \\\n",
                    "  --unet_lr=1e-4 \\\n",
                    "  --text_encoder_lr=5e-5 \\\n",
                    "  --lr_scheduler=\"cosine\" \\\n",
                    "  --lr_warmup_steps=50 \\\n",
                    "  --max_train_epochs=10 \\\n",
                    "  --save_every_n_epochs=2 \\\n",
                    "  --mixed_precision=\"fp16\" \\\n",
                    "  --save_precision=\"fp16\" \\\n",
                    "  --optimizer_type=\"AdamW8bit\" \\\n",
                    "  --cache_latents \\\n",
                    "  --gradient_checkpointing"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    f"# @title 5. Descargar LoRA Entrenado\n",
                    "from google.colab import files\n",
                    f"final_lora = f'/content/output/{char_folder}/{lora_out}.safetensors'\n",
                    "if os.path.exists(final_lora):\n",
                    "    files.download(final_lora)\n",
                    "else:\n",
                    f"    print('LoRA aún no generado o guardado con nombre de epoch.')\n",
                    f"    !ls -lh /content/output/{char_folder}\n"
                ]
            }
        ]
    }
    return nb

def main():
    # ── 1. ARCHIVAR 09_MARCIA_MAKE_DRAMA ──
    marcia_vault = os.path.join(VAULT_DIR, "09_Marcia_Make_Drama")
    marcia_sources = os.path.join(marcia_vault, "01_sources")
    marcia_curated = os.path.join(marcia_vault, "02_curated_dataset")
    os.makedirs(marcia_sources, exist_ok=True)
    os.makedirs(marcia_curated, exist_ok=True)

    # Copiar sources originales
    src_marcia = r"C:\Users\NEO\Downloads\Nueva carpeta (21)"
    for f in os.listdir(src_marcia):
        s_path = os.path.join(src_marcia, f)
        if os.path.isfile(s_path):
            shutil.copy2(s_path, os.path.join(marcia_sources, f))

    # Copiar dataset procesado de E:\ComfyUI\characters\marcia_make_drama\dataset
    src_marcia_dataset = r"E:\ComfyUI\characters\marcia_make_drama\dataset"
    for f in os.listdir(src_marcia_dataset):
        if f.startswith("marcia_"):
            shutil.copy2(os.path.join(src_marcia_dataset, f), os.path.join(marcia_curated, f))

    # Crear ZIP del dataset
    marcia_zip = os.path.join(marcia_vault, "dataset_marcia.zip")
    with zipfile.ZipFile(marcia_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in os.listdir(marcia_curated):
            zf.write(os.path.join(marcia_curated, f), f)

    # Crear Notebook Colab
    marcia_nb = build_notebook("Marcia (Make Drama)", "09_Marcia_Make_Drama", "marcia_make_drama", "dataset_marcia.zip", "lora_marcia_make_drama")
    with open(os.path.join(marcia_vault, "Entrenar_LoRA_Marcia_Make_Drama_Colab.ipynb"), "w", encoding="utf-8") as f:
        json.dump(marcia_nb, f, indent=2)

    # Crear tags_and_config.txt
    marcia_tags_txt = """================================================================================
FICHA TÉCNICA, TAGS Y CONFIGURACIÓN DE ENTRENAMIENTO / INFERENCIA
Personaje: Marcia | Franquicia: Make Drama
================================================================================

[ 1. TRIGGER WORDS PRINCIPALES ]
marcia_(make_drama), marcia, make drama, 1girl, solo

[ 2. ETIQUETAS VISUALES / DANBOORU TAGS ]
* Físico / Rasgos:
  pink hair, twintails, high twintails, long hair, heart ahoge, purple eyes, fang, smirking, cute, petite, chubby thighs, barcode on thigh, bandaid on knee

* Vestimenta Principal:
  futuristic bodysuit, highleg leotard, black and white bodysuit, cleavage cutout, white jacket, crop jacket, detached jacket, black gloves, asymmetric legwear, black thighhigh, single thighhigh, garter strap, mechanical boots, oversized cannon

* Control Anti-Armas / Objetos (Solo ropa limpia):
  empty hands, arms at sides, simple background, white background

--------------------------------------------------------------------------------
[ 3. CONFIGURACIÓN DE ENTRENAMIENTO (Google Colab / Kohya sd-scripts) ]
--------------------------------------------------------------------------------
* Modelo Base: Illustrious-XL v0.1 (SDXL)
* Archivo ZIP del Dataset: dataset_marcia.zip
* Carpeta de Concepto en Colab: /content/dataset/8_marcia_make_drama
* Repeticiones por Imagen (Repeats): 8 - 10
* Archivo LoRA de Salida: lora_marcia_make_drama.safetensors
* Network Dim (Rank): 32 (o 16)
* Network Alpha: 16 (0.5x del Rank)
* Optimizador: AdamW8bit
* Learning Rate U-Net: 1e-4
* LR Scheduler: cosine
* Epochs: 10 (guardado cada 2 épocas)
* Batch Size: 1
* Resolución: 1024x1024 con Bucketing (512 - 1536)
* Precisiones: FP16 Mixed Precision

--------------------------------------------------------------------------------
[ 4. PROMPTS RECOMENDADOS PARA INFERENCIA (ComfyUI / WebUI) ]
--------------------------------------------------------------------------------
> Prompt Positivo Estándar:
score_9, score_8_up, source_anime, rating_explicit, 1girl, marcia_(make_drama), marcia, make drama, solo, pink hair, high twintails, heart ahoge, purple eyes, fang, futuristic bodysuit, highleg leotard, cleavage cutout, white jacket, black thighhigh, boots, masterpiece, best quality

> Negative Prompt Universal:
worst quality, low quality, bad anatomy, bad hands, missing fingers, extra digits, fewer digits, blurry, watermark, signature, artist name, text, error, cropped
================================================================================
"""
    with open(os.path.join(marcia_vault, "tags_and_config.txt"), "w", encoding="utf-8") as f:
        f.write(marcia_tags_txt)

    # ── 2. ARCHIVAR 10_NELLIEL_HEART ──
    nelliel_vault = os.path.join(VAULT_DIR, "10_Nelliel_Heart")
    nelliel_sources = os.path.join(nelliel_vault, "01_sources")
    nelliel_curated = os.path.join(nelliel_vault, "02_curated_dataset")
    os.makedirs(nelliel_sources, exist_ok=True)
    os.makedirs(nelliel_curated, exist_ok=True)

    # Copiar sources originales
    src_nell = r"C:\Users\NEO\Downloads\Nelliel Tu Odelschwanck (1188) [Heart]"
    for f in os.listdir(src_nell):
        s_path = os.path.join(src_nell, f)
        if os.path.isfile(s_path):
            shutil.copy2(s_path, os.path.join(nelliel_sources, f))

    # Copiar dataset procesado de E:\ComfyUI\characters\nelliel_heart\dataset
    src_nell_dataset = r"E:\ComfyUI\characters\nelliel_heart\dataset"
    for f in os.listdir(src_nell_dataset):
        if f.startswith("nelliel_"):
            shutil.copy2(os.path.join(src_nell_dataset, f), os.path.join(nelliel_curated, f))

    # Crear ZIP del dataset
    nelliel_zip = os.path.join(nelliel_vault, "dataset_nelliel_heart.zip")
    with zipfile.ZipFile(nelliel_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in os.listdir(nelliel_curated):
            zf.write(os.path.join(nelliel_curated, f), f)

    # Crear Notebook Colab
    nell_nb = build_notebook("Nelliel [Heart / Swimsuit]", "10_Nelliel_Heart", "nelliel_swimsuit", "dataset_nelliel_heart.zip", "lora_nelliel_heart")
    with open(os.path.join(nelliel_vault, "Entrenar_LoRA_Nelliel_Heart_Colab.ipynb"), "w", encoding="utf-8") as f:
        json.dump(nell_nb, f, indent=2)

    # Crear tags_and_config.txt
    nell_tags_txt = """================================================================================
FICHA TÉCNICA, TAGS Y CONFIGURACIÓN DE ENTRENAMIENTO / INFERENCIA
Personaje: Nelliel Tu Odelschwanck [Heart / Swimsuit] | Franquicia: Bleach Brave Souls
================================================================================

[ 1. TRIGGER WORDS PRINCIPALES ]
nelliel_swimsuit, nelliel tu odelschwanck, bleach, bleach brave souls, 1girl, solo

[ 2. ETIQUETAS VISUALES / DANBOORU TAGS ]
* Físico / Rasgos:
  tan, dark skin, green hair, wavy hair, long hair, green eyes, ram skull, hollow mask on head, facial mark, red facial stripe, large breasts, massive cleavage, wide hips

* Vestimenta Principal:
  white bikini, halterneck bikini top, side-tie bikini bottom, yellow sarong, yellow pareo, floral pareo, beaded necklace, flower on waist

* Fondo / Entorno:
  beach, sunset, ocean, palm tree, tropical

--------------------------------------------------------------------------------
[ 3. CONFIGURACIÓN DE ENTRENAMIENTO (Google Colab / Kohya sd-scripts) ]
--------------------------------------------------------------------------------
* Modelo Base: Illustrious-XL v0.1 (SDXL)
* Archivo ZIP del Dataset: dataset_nelliel_heart.zip
* Carpeta de Concepto en Colab: /content/dataset/8_nelliel_swimsuit
* Repeticiones por Imagen (Repeats): 8 - 10
* Archivo LoRA de Salida: lora_nelliel_heart.safetensors
* Network Dim (Rank): 32 (o 16)
* Network Alpha: 16 (0.5x del Rank)
* Optimizador: AdamW8bit
* Learning Rate U-Net: 1e-4
* LR Scheduler: cosine
* Epochs: 10 (guardado cada 2 épocas)
* Batch Size: 1
* Resolución: 1024x1024 con Bucketing (512 - 1536)
* Precisiones: FP16 Mixed Precision

--------------------------------------------------------------------------------
[ 4. PROMPTS RECOMENDADOS PARA INFERENCIA (ComfyUI / WebUI) ]
--------------------------------------------------------------------------------
> Prompt Positivo Estándar:
score_9, score_8_up, source_anime, rating_explicit, 1girl, nelliel_swimsuit, nelliel tu odelschwanck, bleach, bleach brave souls, solo, tan, dark skin, green hair, wavy hair, green eyes, ram skull, hollow mask on head, facial mark, red facial stripe, large breasts, massive cleavage, white bikini, halterneck bikini top, yellow sarong, beaded necklace, beach, sunset, masterpiece, best quality

> Negative Prompt Universal:
worst quality, low quality, bad anatomy, bad hands, missing fingers, extra digits, fewer digits, blurry, watermark, signature, artist name, text, error, cropped
================================================================================
"""
    with open(os.path.join(nelliel_vault, "tags_and_config.txt"), "w", encoding="utf-8") as f:
        f.write(nell_tags_txt)

    print("[OK] Successfully organized and archived 09_Marcia_Make_Drama and 10_Nelliel_Heart in Vault!")

if __name__ == "__main__":
    main()
