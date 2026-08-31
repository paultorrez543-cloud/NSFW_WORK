import os

guides = [
    r"C:\Users\NEO\Downloads\LoRA_Characters_Vault\LORA_CHARACTERS_VAULT_GUIDE.md",
    r"E:\ComfyUI\characters\LORA_CHARACTERS_VAULT_GUIDE.md"
]

for g in guides:
    if os.path.exists(g):
        with open(g, "r", encoding="utf-8") as f:
            c = f.read()
        
        c = c.replace(
            "3. **`03_primera_insercion` (Totalmente Desnuda / Primera Entrada):**",
            "3. **`03_primera_insercion` (Ropa Semi-Abierta / Primera Entrada):**"
        )
        c = c.replace(
            "4. **`04_extasis` (Totalmente Desnuda / Clímax y Ahegao):**",
            "4. **`04_extasis` (Ropa Semi-Abierta / Clímax y Ahegao):**"
        )
        with open(g, "w", encoding="utf-8") as f:
            f.write(c)
        print("[OK] Updated stage descriptions in:", g)
