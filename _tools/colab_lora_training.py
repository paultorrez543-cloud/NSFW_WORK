# ═════════════════════════════════════════════════════════════════════
# GOOGLE COLAB: SCRIPT DE ENTRENAMIENTO DE LORAS (ILLUSTRIOUS SDXL)
# Personajes: Marcia (Make Drama) y Nelliel Tu Odelschwanck [Heart]
# ═════════════════════════════════════════════════════════════════════

"""
Copiar y pegar estas celdas directamente en un Notebook de Google Colab (con GPU T4 / A100 / L4).
"""

# ── CELDA 1: INSTALACIÓN DE KOHYA_SS / SD-SCRIPTS ──
# @title 1. Instalar entorno de entrenamiento (sd-scripts)
# !git clone --depth 1 https://github.com/kohya-ss/sd-scripts.git
# %cd sd-scripts
# !pip install -q --upgrade pip
# !pip install -q torch==2.1.2 torchvision==0.16.2 --index-url https://download.pytorch.org/whl/cu121
# !pip install -q --upgrade -r requirements.txt
# !pip install -q xformers==0.0.23.post1 bitsandbytes lion-pytorch prodigy-opt


# ── CELDA 2: DESCARGA DEL MODELO BASE (ILLUSTRIOUS SDXL) ──
# @title 2. Descargar modelo base Illustrious / rinIllusion
# !mkdir -p /content/models
# !wget -c -O /content/models/illustrious-xl-v0.1.safetensors "https://huggingface.co/OnomaAIResearch/Illustrious-xl-early-release-v0-1/resolve/main/Illustrious-XL-v0.1.safetensors"


# ── CELDA 3: CONFIGURACIÓN Y ENTRENAMIENTO DE MARCIA (MAKE DRAMA) ──
# @title 3. Entrenar LoRA: Marcia (Make Drama)
"""
# 1. Crear directorios
!mkdir -p /content/dataset/marcia/10_marcia_make_drama
!mkdir -p /content/output/marcia

# 2. Subir tus imágenes y .txt a /content/dataset/marcia/10_marcia_make_drama/

# 3. Lanzar Entrenamiento SDXL con Kohya
%cd /content/sd-scripts
!accelerate launch --mixed_precision=fp16 --num_cpu_threads_per_process 2 \
  /content/sd-scripts/sdxl_train_network.py \
  --pretrained_model_name_or_path="/content/models/illustrious-xl-v0.1.safetensors" \
  --train_data_dir="/content/dataset/marcia" \
  --output_dir="/content/output/marcia" \
  --output_name="lora_marcia_make_drama" \
  --save_model_as="safetensors" \
  --network_module="networks.lora" \
  --network_dim=32 \
  --network_alpha=16 \
  --resolution="1024,1024" \
  --enable_bucket \
  --min_bucket_reso=512 \
  --max_bucket_reso=1536 \
  --learning_rate=1e-4 \
  --unet_lr=1e-4 \
  --text_encoder_lr=5e-5 \
  --lr_scheduler="cosine" \
  --lr_warmup_steps=50 \
  --max_train_epochs=10 \
  --save_every_n_epochs=2 \
  --mixed_precision="fp16" \
  --save_precision="fp16" \
  --optimizer_type="AdamW8bit" \
  --cache_latents \
  --gradient_checkpointing
"""


# ── CELDA 4: CONFIGURACIÓN Y ENTRENAMIENTO DE NELLIEL [HEART] ──
# @title 4. Entrenar LoRA: Nelliel Tu Odelschwanck [Heart]
"""
# 1. Crear directorios
!mkdir -p /content/dataset/nelliel_heart/10_nelliel_swimsuit
!mkdir -p /content/output/nelliel_heart

# 2. Subir tus imágenes y .txt a /content/dataset/nelliel_heart/10_nelliel_swimsuit/

# 3. Lanzar Entrenamiento SDXL con Kohya
%cd /content/sd-scripts
!accelerate launch --mixed_precision=fp16 --num_cpu_threads_per_process 2 \
  /content/sd-scripts/sdxl_train_network.py \
  --pretrained_model_name_or_path="/content/models/illustrious-xl-v0.1.safetensors" \
  --train_data_dir="/content/dataset/nelliel_heart" \
  --output_dir="/content/output/nelliel_heart" \
  --output_name="lora_nelliel_heart" \
  --save_model_as="safetensors" \
  --network_module="networks.lora" \
  --network_dim=32 \
  --network_alpha=16 \
  --resolution="1024,1024" \
  --enable_bucket \
  --min_bucket_reso=512 \
  --max_bucket_reso=1536 \
  --learning_rate=1e-4 \
  --unet_lr=1e-4 \
  --text_encoder_lr=5e-5 \
  --lr_scheduler="cosine" \
  --lr_warmup_steps=50 \
  --max_train_epochs=10 \
  --save_every_n_epochs=2 \
  --mixed_precision="fp16" \
  --save_precision="fp16" \
  --optimizer_type="AdamW8bit" \
  --cache_latents \
  --gradient_checkpointing
"""
