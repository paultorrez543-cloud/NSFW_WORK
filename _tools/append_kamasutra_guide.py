import os

section_6 = """
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
3. **`03_primera_insercion` (Totalmente Desnuda / Primera Entrada):**
   * Pasión y placer intenso (`completely nude, pleasure, tears_of_pleasure, moaning`).
   * Entrada de la punta (`(tip_in_pussy:1.4), (first_insertion:1.3), stretching`).
4. **`04_extasis` (Totalmente Desnuda / Clímax y Ahegao):**
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
"""

guides = [
    r"C:\Users\NEO\Downloads\LoRA_Characters_Vault\LORA_CHARACTERS_VAULT_GUIDE.md",
    r"E:\ComfyUI\characters\LORA_CHARACTERS_VAULT_GUIDE.md"
]

for g in guides:
    if os.path.exists(g):
        with open(g, "r", encoding="utf-8") as f:
            c = f.read()
        if "## 💖 6. Generador Kamasutra Seductor" not in c:
            c += section_6
            with open(g, "w", encoding="utf-8") as f:
                f.write(c)
            print("[OK] Appended Section 6 in:", g)
