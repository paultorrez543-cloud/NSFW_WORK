import os, shutil

BASE_DIR = r"E:/ComfyUI/characters/Stella_Sora"
ARCHIVE_DIR = os.path.join(BASE_DIR, "_archive")
os.makedirs(ARCHIVE_DIR, exist_ok=True)

# Archivos esenciales que DEBEN permanecer en la raíz
KEEP_FILES = {
    "build_poses.py",
    "build_bernina_bunny.py",
    "build_chitose_kimono.py",
    "build_more_characters.py",
    "stella_sora_loras_triggers.md",
    "character_config.json",
    "organize_workspace.py"
}

moved_files = []

for item in os.listdir(BASE_DIR):
    item_path = os.path.join(BASE_DIR, item)
    
    # Solo procesar archivos sueltos en la raíz (no tocar las carpetas de personajes)
    if os.path.isfile(item_path):
        if item not in KEEP_FILES:
            dest_path = os.path.join(ARCHIVE_DIR, item)
            shutil.move(item_path, dest_path)
            moved_files.append(item)

print(f"[OK] Se archivaron {len(moved_files)} archivos obsoletos/antiguos en: {ARCHIVE_DIR}")
for f in moved_files[:15]:
    print(f"  -> {f}")
if len(moved_files) > 15:
    print(f"  ... y {len(moved_files) - 15} archivos más.")
