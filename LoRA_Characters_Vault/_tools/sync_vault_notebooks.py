import os
import json

VAULT_DIR = r"C:\Users\NEO\Downloads\LoRA_Characters_Vault"
TEMPLATE_PATH = os.path.join(VAULT_DIR, "08_Jennie_Make_Drama", "Entrenar_LoRA_Jennie_Make_Drama_Colab.ipynb")

with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    base_nb = json.load(f)

# 1. GENERATE FOR MARCIA MAKE DRAMA
marcia_nb = json.loads(json.dumps(base_nb)) # deep copy

# Cell 0 (Markdown header)
marcia_nb["cells"][0]["source"] = [
    "# 🚀 Entrenamiento de LoRA: Marcia (Make Drama) (SDXL / Illustrious)\n",
    "### Modelo Base: Illustrious-XL v0.1 | Framework: Kohya_ss sd-scripts\n",
    "---\n",
    "Ejecuta las celdas en orden para instalar dependencias, configurar el dataset y entrenar el LoRA."
]

# Cell 3 (Dataset extraction & toml)
cell3_marcia = """# @title 3. 📦 Extraer Dataset y Generar dataset.toml para Marcia (Make Drama)
import os, shutil, zipfile, glob, toml

CONCEPT_NAME = 'marcia'
REPEATS = 8
CLASS_TOKENS = 'marcia_(make_drama), marcia, make drama'
LORA_OUTPUT_NAME = 'lora_marcia_make_drama'

DATASET_DIR = '/content/dataset'
OUTPUT_DIR = '/content/output_lora'
TARGET_DIR = f'/content/dataset/{REPEATS}_{CONCEPT_NAME}'

if os.path.exists(DATASET_DIR):
    shutil.rmtree(DATASET_DIR)
os.makedirs(TARGET_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

posibles_zips = ['/content/dataset_marcia.zip', '/content/dataset.zip', '/content/drive/MyDrive/dataset_marcia.zip', '/content/drive/MyDrive/dataset.zip']
zip_encontrado = None
for p in posibles_zips:
    if os.path.exists(p):
        zip_encontrado = p
        break

if not zip_encontrado:
    buscados = glob.glob('/content/dataset*.zip') + glob.glob('/content/*.zip')
    if buscados:
        zip_encontrado = buscados[0]

if zip_encontrado and os.path.exists(zip_encontrado):
    print(f'Descomprimiendo {zip_encontrado} en {TARGET_DIR}...')
    with zipfile.ZipFile(zip_encontrado, 'r') as z:
        z.extractall(TARGET_DIR)
    imgs = [f for f in os.listdir(TARGET_DIR) if f.endswith(('.png', '.jpg', '.webp'))]
    txts = [f for f in os.listdir(TARGET_DIR) if f.endswith('.txt')]
    print(f'✅ Dataset listo: {len(imgs)} imágenes y {len(txts)} etiquetas (.txt)')
else:
    print('⚠️ No se encontró dataset_marcia.zip. Sube el archivo ZIP a Colab.')

# Generar dataset.toml
dataset_config = {
    'general': {
        'enable_bucket': True,
        'caption_extension': '.txt',
        'shuffle_caption': False,
        'bucket_reso_steps': 64,
        'min_bucket_reso': 512,
        'max_bucket_reso': 2048
    },
    'datasets': [
        {
            'resolution': 1024,
            'min_bucket_reso': 512,
            'max_bucket_reso': 2048,
            'caption_dropout_rate': 0.0,
            'subsets': [
                {
                    'image_dir': TARGET_DIR,
                    'num_repeats': REPEATS,
                    'class_tokens': CLASS_TOKENS
                }
            ]
        }
    ]
}

with open('/content/dataset.toml', 'w') as f:
    toml.dump(dataset_config, f)
print('✓ Archivo /content/dataset.toml configurado.')
"""
marcia_nb["cells"][3]["source"] = [l + "\n" for l in cell3_marcia.split("\n")]

# Cell 4 (Training command output name)
cell4_marcia_str = "".join(marcia_nb["cells"][4]["source"])
cell4_marcia_str = cell4_marcia_str.replace("lora_jennie_make_drama", "lora_marcia_make_drama").replace("Jennie (Make Drama)", "Marcia (Make Drama)")
marcia_nb["cells"][4]["source"] = [l + "\n" for l in cell4_marcia_str.split("\n")]

# Cell 6 (Inference prompt)
cell6_marcia_str = "".join(marcia_nb["cells"][6]["source"])
cell6_marcia_str = cell6_marcia_str.replace("lora_jennie_make_drama.safetensors", "lora_marcia_make_drama.safetensors")
cell6_marcia_str = cell6_marcia_str.replace("jennie_(make_drama), jennie, solo, teal hair, cyan hair, long hair, ponytail, white ribbon, hair ribbon, golden eyes, yellow eyes, business attire, white collared shirt, black blazer, black pencil skirt", "marcia_(make_drama), marcia, make drama, solo, pink hair, high twintails, heart ahoge, purple eyes, fang, futuristic bodysuit, highleg leotard, cleavage cutout, white jacket, black thighhigh, boots")
marcia_nb["cells"][6]["source"] = [l + "\n" for l in cell6_marcia_str.split("\n")]

marcia_nb_path = os.path.join(VAULT_DIR, "09_Marcia_Make_Drama", "Entrenar_LoRA_Marcia_Make_Drama_Colab.ipynb")
with open(marcia_nb_path, "w", encoding="utf-8") as f:
    json.dump(marcia_nb, f, indent=2)
print("[OK] Generated template-matched notebook for Marcia!")


# 2. GENERATE FOR NELLIEL HEART
nell_nb = json.loads(json.dumps(base_nb)) # deep copy

# Cell 0 (Markdown header)
nell_nb["cells"][0]["source"] = [
    "# 🚀 Entrenamiento de LoRA: Nelliel [Heart / Swimsuit] (SDXL / Illustrious)\n",
    "### Modelo Base: Illustrious-XL v0.1 | Framework: Kohya_ss sd-scripts\n",
    "---\n",
    "Ejecuta las celdas en orden para instalar dependencias, configurar el dataset y entrenar el LoRA."
]

# Cell 3 (Dataset extraction & toml)
cell3_nell = """# @title 3. 📦 Extraer Dataset y Generar dataset.toml para Nelliel [Heart / Swimsuit]
import os, shutil, zipfile, glob, toml

CONCEPT_NAME = 'nelliel_swimsuit'
REPEATS = 8
CLASS_TOKENS = 'nelliel_swimsuit, nelliel tu odelschwanck, bleach, bleach brave souls'
LORA_OUTPUT_NAME = 'lora_nelliel_heart'

DATASET_DIR = '/content/dataset'
OUTPUT_DIR = '/content/output_lora'
TARGET_DIR = f'/content/dataset/{REPEATS}_{CONCEPT_NAME}'

if os.path.exists(DATASET_DIR):
    shutil.rmtree(DATASET_DIR)
os.makedirs(TARGET_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

posibles_zips = ['/content/dataset_nelliel_heart.zip', '/content/dataset.zip', '/content/drive/MyDrive/dataset_nelliel_heart.zip', '/content/drive/MyDrive/dataset.zip']
zip_encontrado = None
for p in posibles_zips:
    if os.path.exists(p):
        zip_encontrado = p
        break

if not zip_encontrado:
    buscados = glob.glob('/content/dataset*.zip') + glob.glob('/content/*.zip')
    if buscados:
        zip_encontrado = buscados[0]

if zip_encontrado and os.path.exists(zip_encontrado):
    print(f'Descomprimiendo {zip_encontrado} en {TARGET_DIR}...')
    with zipfile.ZipFile(zip_encontrado, 'r') as z:
        z.extractall(TARGET_DIR)
    imgs = [f for f in os.listdir(TARGET_DIR) if f.endswith(('.png', '.jpg', '.webp'))]
    txts = [f for f in os.listdir(TARGET_DIR) if f.endswith('.txt')]
    print(f'✅ Dataset listo: {len(imgs)} imágenes y {len(txts)} etiquetas (.txt)')
else:
    print('⚠️ No se encontró dataset_nelliel_heart.zip. Sube el archivo ZIP a Colab.')

# Generar dataset.toml
dataset_config = {
    'general': {
        'enable_bucket': True,
        'caption_extension': '.txt',
        'shuffle_caption': False,
        'bucket_reso_steps': 64,
        'min_bucket_reso': 512,
        'max_bucket_reso': 2048
    },
    'datasets': [
        {
            'resolution': 1024,
            'min_bucket_reso': 512,
            'max_bucket_reso': 2048,
            'caption_dropout_rate': 0.0,
            'subsets': [
                {
                    'image_dir': TARGET_DIR,
                    'num_repeats': REPEATS,
                    'class_tokens': CLASS_TOKENS
                }
            ]
        }
    ]
}

with open('/content/dataset.toml', 'w') as f:
    toml.dump(dataset_config, f)
print('✓ Archivo /content/dataset.toml configurado.')
"""
nell_nb["cells"][3]["source"] = [l + "\n" for l in cell3_nell.split("\n")]

# Cell 4 (Training command output name)
cell4_nell_str = "".join(nell_nb["cells"][4]["source"])
cell4_nell_str = cell4_nell_str.replace("lora_jennie_make_drama", "lora_nelliel_heart").replace("Jennie (Make Drama)", "Nelliel [Heart / Swimsuit]")
nell_nb["cells"][4]["source"] = [l + "\n" for l in cell4_nell_str.split("\n")]

# Cell 6 (Inference prompt)
cell6_nell_str = "".join(nell_nb["cells"][6]["source"])
cell6_nell_str = cell6_nell_str.replace("lora_jennie_make_drama.safetensors", "lora_nelliel_heart.safetensors")
cell6_nell_str = cell6_nell_str.replace("jennie_(make_drama), jennie, solo, teal hair, cyan hair, long hair, ponytail, white ribbon, hair ribbon, golden eyes, yellow eyes, business attire, white collared shirt, black blazer, black pencil skirt", "nelliel_swimsuit, nelliel tu odelschwanck, bleach, bleach brave souls, solo, tan, dark skin, green hair, wavy hair, green eyes, ram skull, hollow mask on head, facial mark, red facial stripe, large breasts, massive cleavage, white bikini, halterneck bikini top, yellow sarong, beaded necklace, beach, sunset")
nell_nb["cells"][6]["source"] = [l + "\n" for l in cell6_nell_str.split("\n")]

nell_nb_path = os.path.join(VAULT_DIR, "10_Nelliel_Heart", "Entrenar_LoRA_Nelliel_Heart_Colab.ipynb")
with open(nell_nb_path, "w", encoding="utf-8") as f:
    json.dump(nell_nb, f, indent=2)
print("[OK] Generated template-matched notebook for Nelliel Heart!")
