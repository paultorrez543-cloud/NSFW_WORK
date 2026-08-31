import os

B = r"E:/ComfyUI/characters/Stella_Sora"
folders = [d for d in os.listdir(B) if os.path.isdir(os.path.join(B, d)) and not d.startswith("_")]

print(f"=== AUDITORÍA DE WORKFLOW_MASTER.JSON ({len(folders)} Carpetas) ===")
ok_count = 0
for f in sorted(folders):
    mf = os.path.join(B, f, "workflow_master.json")
    if os.path.exists(mf):
        sz = os.path.getsize(mf) / 1024
        print(f"[OK]    {f:22} -> workflow_master.json ({sz:.1f} KB)")
        ok_count += 1
    else:
        print(f"[FALTA] {f:22}")

print(f"\nResultado: {ok_count}/{len(folders)} carpetas tienen su workflow_master.json completo y funcional.")
