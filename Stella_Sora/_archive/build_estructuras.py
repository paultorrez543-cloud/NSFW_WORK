import json, os

B = "E:/ComfyUI/characters/Stella_Sora"
CKPT = "waiIllustriousSDXL_v170.safetensors"
LIGHT = "dimly_lit, dark_ambiance, (dark lighting:1.5)"
MALE = "disembodied_penis, black_penis, dark_penis"

NEG = "score_4, score_5, score_6, lowres, bad anatomy, bad hands, bad eyes, deformed eyes, extra eyes, crossed eyes, missing fingers, extra digits, fewer digits, worst quality, low quality, blurry, ugly, censored, (bright lighting:1.5), overexposed, glare, flash, bloom, glowing, x-ray, internal_shot, cross-section, text_bubbles, speech_bubble, signature, watermark"

POSES = {
    "cowgirl":         "cowgirl_position, girl_on_top, straddling, front_view",
    "doggystyle":      "doggystyle, from_behind, all_fours, front_view",
    "missionary":      "missionary_position, legs_up, spread_legs, front_view",
    "mating_press":    "mating_press, legs_above_head, folded, front_view",
    "reverse_cowgirl": "reverse_cowgirl, girl_on_top, facing_away, front_view",
}

# 30 estructuras. Cada etapa: (nombre, depth, expr, motion, fluids, sound)
STRUCTURES = {
    "consentida": [
        ("01_carino", "", "blush, holding_hands, gentle, shy_smile", "", "", ""),
        ("02_besos", "(imminent penetration:1.2)", "kissing, embracing, closed_eyes, tender", "", "blush", ""),
        ("03_desnudar", "about_to_penetrate", "undressing, skin_contact, nervous, exposed", "", "nervous_sweat", ""),
        ("04_intimo", "(deep penetration:1.3)", "gentle_sex, loving, eyes_contact, missionary", "(motion lines:1.2)", "sweat", ""),
        ("05_placer", "(deep penetration:1.5)", "moaning, pleasure, arching_back, orgasm", "(motion lines:1.4)", "excessive_sweat", "sound_effects"),
        ("06_climax", "balls_deep", "orgasm, creampie, afterglow, cuddling", "", "semen_on_body", ""),
    ],
    "dominacion": [
        ("01_orden", "(imminent penetration:1.2)", "commanding, kneeling, collared, obedient", "", "nervous_sweat", ""),
        ("02_resistencia", "about_to_penetrate", "reluctant, blush, hesitant", "", "sweat", ""),
        ("03_castigo", "tip_in_pussy, first_insertion", "spanking, bound, tears, punishment", "(motion lines:1.3), impact_lines", "sweat, tears_streaming", "sound_effects"),
        ("04_sumision", "(deep penetration:1.3)", "submissive, begging, desperate", "(motion lines:1.3)", "sweat, drooling", "sound_effects"),
        ("05_recompensa", "(deep penetration:1.5), balls_deep", "rewarding, oral, servitude, moaning", "(motion lines:1.4)", "excessive_sweat, drooling", "sound_effects, onomatopoeia"),
        ("06_aftercare", "after_sex", "exhausted, embraced, gentle, cum_covered", "", "semen_on_body", ""),
    ],
    "seduccion": [
        ("01_provocar", "", "teasing, smirk, revealing, seductive", "", "", ""),
        ("02_strip", "(imminent penetration:1.2)", "undressing, strip_tease, show_off", "", "blush", ""),
        ("03_tentacion", "about_to_penetrate", "masturbation, fingers, inviting", "", "sweat", ""),
        ("04_deseo", "(deep penetration:1.3)", "begging, aroused, needy", "(motion lines:1.2)", "sweat, drooling", ""),
        ("05_sexo", "(deep penetration:1.5), balls_deep", "intense_sex, rough, passionate, ahegao", "(motion lines:1.5)", "excessive_sweat, drooling", "sound_effects, onomatopoeia"),
        ("06_aftermath", "after_sex", "satisfied, messy, cum_covered", "", "semen_on_body, cum_pool", ""),
    ],
    "fluidos": [
        ("01_seca", "(imminent penetration:1.2)", "dry, anticipation, no_fluids", "", "", ""),
        ("02_sudor", "about_to_penetrate", "sweating, nervous, glistening", "", "sweat", ""),
        ("03_drool", "(deep penetration:1.3)", "drooling, saliva_string, panting", "(motion lines:1.2)", "sweat, drooling", ""),
        ("04_pre_cum", "(deep penetration:1.4)", "precum, wet, dripping", "(motion lines:1.3)", "excessive_sweat, drooling", "sound_effects"),
        ("05_creampie", "(deep penetration:1.5), balls_deep", "creampie, cum_overflow, gaping, ahegao", "(motion lines:1.5)", "excessive_sweat", "sound_effects, onomatopoeia"),
        ("06_overflow", "after_sex, gaping", "excessive_cum, cum_pool, soaked, exhausted", "", "semen_on_body, cum_pool", ""),
    ],
    "cosplay": [
        ("01_vestida", "", "full_outfit, clean, neat", "", "", ""),
        ("02_despeinada", "(imminent penetration:1.2)", "disheveled, clothes_askew", "", "blush", ""),
        ("03_semidesnuda", "about_to_penetrate", "clothes_lift, breasts_out", "", "sweat", ""),
        ("04_rota", "(deep penetration:1.3)", "torn_clothes, exposed", "(motion lines:1.2)", "sweat, drooling", ""),
        ("05_desnuda", "(deep penetration:1.5), balls_deep", "nude, only_accessories, ahegao", "(motion lines:1.4)", "excessive_sweat", "sound_effects"),
        ("06_ruinada", "after_sex", "ruined_outfit, cum_stained, exhausted", "", "semen_on_body", ""),
    ],
    "hipnosis": [
        ("01_normal", "", "innocent, unaware, normal_expression", "", "", ""),
        ("02_hipnosis", "(imminent penetration:1.2)", "spiral_eyes, dazed, suggestible, blush", "", "nervous_sweat", ""),
        ("03_orden", "about_to_penetrate", "obedient, blank_expression, following_command", "", "sweat", ""),
        ("04_obediencia", "(deep penetration:1.3)", "mechanical, emotionless, complying", "(motion lines:1.3)", "sweat, drooling", "sound_effects"),
        ("05_placer", "(deep penetration:1.5), balls_deep", "heart_pupils, ahegao, broken_will, moaning", "(motion lines:1.5)", "excessive_sweat, drooling", "sound_effects, onomatopoeia"),
        ("06_controlada", "after_sex, gaping", "empty_eyes, puppet, cum_covered, exhausted", "", "semen_on_body", ""),
    ],
    "corrupcion": [
        ("01_inocente", "", "pure, naive, cheerful, schoolgirl", "", "", ""),
        ("02_curiosa", "(imminent penetration:1.2)", "curious, blushing, hesitant", "", "nervous_sweat", ""),
        ("03_tentada", "about_to_penetrate", "tempted, aroused, guilty_expression", "", "sweat, blush", ""),
        ("04_cayendo", "(deep penetration:1.3)", "moaning, eyes_closed, surrendering", "(motion lines:1.3)", "sweat, drooling", "sound_effects"),
        ("05_corrupta", "(deep penetration:1.5), balls_deep", "ahegao, addicted, seductive, tongue_out", "(motion lines:1.5)", "excessive_sweat, drooling", "sound_effects, onomatopoeia"),
        ("06_perdida", "after_sex, gaping", "mind_break, cum_stained, ruined, blank_eyes", "", "semen_on_body, cum_pool", ""),
    ],
    "afrodisiaco": [
        ("01_normal", "", "calm, unaware, sitting, relaxed", "", "", ""),
        ("02_droga", "(imminent penetration:1.2)", "dizzy, blurred_vision, flushed", "", "nervous_sweat", ""),
        ("03_calor", "about_to_penetrate", "sweating, panting, hot_flush, aroused", "", "excessive_sweat", ""),
        ("04_excitada", "(deep penetration:1.3)", "aroused, needy, restless, moaning", "(motion lines:1.3)", "excessive_sweat, drooling", "sound_effects"),
        ("05_incontrol", "(deep penetration:1.5), balls_deep", "orgasm, convulsing, ahegao, heart_pupils", "(motion lines:1.5)", "excessive_sweat, tears_of_pleasure", "sound_effects, onomatopoeia"),
        ("06_desmayada", "after_sex", "collapsed, drooling, exhausted, unconscious", "", "semen_on_body, drool", ""),
    ],
    "orificios": [
        ("01_solo_pussy", "vaginal_penetration", "shy, blush, missionary", "", "nervous_sweat", ""),
        ("02_pussy_dedos", "vaginal, fingering", "moaning, fingers, additional_stimulation", "", "sweat", ""),
        ("03_anal_inicio", "anal_plug, anal_fingering", "nervous, preparing, stretching", "(motion lines:1.2)", "sweat, drooling", ""),
        ("04_DP", "double_penetration, vaginal, anal", "ahegao, screaming, stretched", "(motion lines:1.4)", "excessive_sweat, tears", "sound_effects"),
        ("05_triple", "triple_penetration, all_holes", "mind_break, tongue_out, convulsing", "(motion lines:1.5)", "excessive_sweat, drooling", "sound_effects, onomatopoeia"),
        ("06_todo_lleno", "gaping_everywhere, after_sex", "cum_overflow, exhausted, broken", "", "semen_on_body, cum_pool", ""),
    ],
    "tamano": [
        ("01_pequeno", "(penetration:1.0)", "easy, comfortable, relaxed", "", "nervous_sweat", ""),
        ("02_mediano", "(penetration:1.2)", "medium, stretching, slight_pain, blush", "", "sweat", ""),
        ("03_grande", "(deep penetration:1.3)", "large, bulging, groaning, stomach_bulge", "(motion lines:1.3)", "sweat, drooling", "sound_effects"),
        ("04_enorme", "(deep penetration:1.4)", "huge, stomach_bulge, straining, screaming", "(motion lines:1.4)", "excessive_sweat, tears", "sound_effects"),
        ("05_gigante", "(deep penetration:1.5), balls_deep", "massive, gaping, screaming, ahegao", "(motion lines:1.5)", "excessive_sweat, drooling", "sound_effects, onomatopoeia"),
        ("06_colosal", "balls_deep, gaping", "impossible_size, unconscious, broken", "", "semen_on_body", ""),
    ],
    "multitud": [
        ("01_solo", "(imminent penetration:1.2)", "intimate, blush, one_on_one", "", "nervous_sweat", ""),
        ("02_dos", "(penetration:1.2)", "mmf threesome, surprised, overwhelmed", "", "sweat", ""),
        ("03_tres", "(deep penetration:1.3)", "group_sex, surrounded, moaning", "(motion lines:1.3)", "sweat, drooling", "sound_effects"),
        ("04_cinco", "(deep penetration:1.4)", "gangbang, overwhelmed, screaming", "(motion lines:1.4)", "excessive_sweat, tears", "sound_effects"),
        ("05_muchos", "(deep penetration:1.5), balls_deep", "large_group, mob, lost_in_crowd, ahegao", "(motion lines:1.5)", "excessive_sweat, drooling", "sound_effects, onomatopoeia"),
        ("06_cubierta", "after_sex", "bukkake, cum_covered, exhausted", "", "semen_on_body, cum_pool", ""),
    ],
    "tentaculos": [
        ("01_descubierta", "", "curious, tentacle_emerging, surprised", "", "", ""),
        ("02_atrapada", "(imminent penetration:1.2)", "tentacle_grab, restrained, struggling", "(motion lines:1.2)", "nervous_sweat", ""),
        ("03_envuelta", "about_to_penetrate", "tentacle_wrap, bound, helpless", "(motion lines:1.3)", "sweat", ""),
        ("04_penetrada", "(deep penetration:1.4)", "tentacle_in_pussy, tentacle_in_ass, gaping, screaming", "(motion lines:1.4)", "excessive_sweat, tears", "sound_effects"),
        ("05_llena", "(deep penetration:1.5)", "multiple_tentacles, all_holes, mind_break, ahegao", "(motion lines:1.5)", "excessive_sweat, drooling", "sound_effects, onomatopoeia"),
        ("06_abandonada", "after_sex, gaping", "tentacle_slime, exhausted, egg_implanted", "", "semen_on_body, slime", ""),
    ],
    "posesion": [
        ("01_normal", "", "pure, calm, innocent", "", "", ""),
        ("02_posesion", "(imminent penetration:1.2)", "glowing_eyes, dark_aura, trembling", "", "nervous_sweat", ""),
        ("03_transformada", "about_to_penetrate", "demon_horns, dark_skin, corrupting", "", "sweat", ""),
        ("04_controlada", "(deep penetration:1.3)", "demonic, sadistic_smile, dominant", "(motion lines:1.3)", "sweat, drooling", "sound_effects"),
        ("05_desatada", "(deep penetration:1.5), balls_deep", "wild, ahegao, demonic_power, insane", "(motion lines:1.5)", "excessive_sweat, drooling", "sound_effects, onomatopoeia"),
        ("06_agotada", "after_sex", "possession_end, exhausted, marked", "", "semen_on_body", ""),
    ],
    "sueno_humedo": [
        ("01_dormida", "", "sleeping, peaceful, in_bed", "", "", ""),
        ("02_sueno", "(imminent penetration:1.2)", "dreaming, blush, tossing", "", "nervous_sweat", ""),
        ("03_excitada", "about_to_penetrate", "moaning_in_sleep, aroused, sweating", "", "sweat", ""),
        ("04_inconsciente", "(deep penetration:1.3)", "somnophilia, sleep_sex, unaware", "(motion lines:1.2)", "sweat, drooling", ""),
        ("05_orgasmo", "(deep penetration:1.5), balls_deep", "wet_dream, orgasm, convulsing_in_sleep", "(motion lines:1.4)", "excessive_sweat", "sound_effects"),
        ("06_despierta", "after_sex", "waking_up, confused, messy, wet", "", "semen_on_body", ""),
    ],
    "virginidad": [
        ("01_virgen", "", "virgin, innocent, nervous, schoolgirl", "", "", ""),
        ("02_nerviosa", "(imminent penetration:1.2)", "trembling, blush, scared, first_time", "", "nervous_sweat", ""),
        ("03_desnudada", "about_to_penetrate", "undressing, shy, covering_self", "", "sweat", ""),
        ("04_primera_vez", "tip_in_pussy, first_insertion", "defloration, pain, hymen, tears", "(motion lines:1.3)", "sweat, tears_streaming", "sound_effects"),
        ("05_placer", "(deep penetration:1.5)", "first_orgasm, moaning, clinging", "(motion lines:1.4)", "excessive_sweat", "sound_effects"),
        ("06_despues", "after_sex", "blood_stained, cuddling, afterglow", "", "semen_on_body", ""),
    ],
    "esclava": [
        ("01_reclutada", "", "collared, confused, new_slave", "", "", ""),
        ("02_instruida", "(imminent penetration:1.2)", "obedience_training, following_orders", "", "nervous_sweat", ""),
        ("03_domada", "about_to_penetrate", "broken_spirit, submissive, kneeling", "", "sweat", ""),
        ("04_entrenada", "(deep penetration:1.3)", "skilled, eager_to_please, service", "(motion lines:1.3)", "sweat, drooling", "sound_effects"),
        ("05_adicta", "(deep penetration:1.5), balls_deep", "addicted, begging, desperate_for_pleasure, ahegao", "(motion lines:1.4)", "excessive_sweat, drooling", "sound_effects"),
        ("06_consagrada", "after_sex", "branded, devoted, mind_fully_broken", "", "semen_on_body", ""),
    ],
    "boda": [
        ("01_vestida", "", "wedding_dress, veil, blushing_bride", "", "", ""),
        ("02_ceremonia", "(imminent penetration:1.2)", "wedding_ring, vows, happy", "", "blush", ""),
        ("03_primera_noche", "about_to_penetrate", "undressing, nervous, honeymoon", "", "nervous_sweat", ""),
        ("04_consumando", "(deep penetration:1.3)", "first_night, gentle_sex, married", "(motion lines:1.2)", "sweat", ""),
        ("05_apasionada", "(deep penetration:1.5), balls_deep", "passionate, moaning, newlywed", "(motion lines:1.4)", "excessive_sweat", "sound_effects"),
        ("06_despertar", "after_sex", "morning_after, disheveled, ring_on_finger", "", "semen_on_body", ""),
    ],
    "embarazo": [
        ("01_plana", "", "flat_belly, normal", "", "", ""),
        ("02_sospecha", "(imminent penetration:1.2)", "nausea, worried, pregnancy_test", "", "nervous_sweat", ""),
        ("03_creciendo", "about_to_penetrate", "slight_belly, pregnant, rubbing_belly", "", "sweat", ""),
        ("04_embarazada", "(deep penetration:1.3)", "big_belly, pregnant, lactating", "(motion lines:1.2)", "sweat, breast_milk", ""),
        ("05_lactando", "(deep penetration:1.5)", "breast_milk, lactation, milking, ahegao", "(motion lines:1.4)", "excessive_sweat, breast_milk", "sound_effects"),
        ("06_madura", "after_sex", "heavily_pregnant, about_to_give_birth", "", "semen_on_body", ""),
    ],
    "parasito": [
        ("01_normal", "", "healthy, unaware, clean", "", "", ""),
        ("02_infectada", "(imminent penetration:1.2)", "parasite_entering, scared, pain", "", "nervous_sweat", ""),
        ("03_creciendo", "about_to_penetrate", "stomach_bulge, sick, fever", "", "sweat", ""),
        ("04_controlada", "(deep penetration:1.3)", "parasite_control, eyes_changed, obedient", "(motion lines:1.2)", "sweat, drooling", ""),
        ("05_desovando", "(deep penetration:1.5)", "egg_laying, oviposition, gaping, ahegao", "(motion lines:1.4)", "excessive_sweat, drooling", "sound_effects"),
        ("06_huevos", "after_sex", "eggs_implanted, exhausted, marked", "", "semen_on_body, slime", ""),
    ],
    "robot": [
        ("01_apagada", "", "blank_expression, robot, standby", "", "", ""),
        ("02_encendida", "(imminent penetration:1.2)", "booting, mechanical_eyes, confused", "", "", ""),
        ("03_programada", "about_to_penetrate", "programming, obeying, emotionless", "", "", ""),
        ("04_sensorial", "(deep penetration:1.3)", "sensors_overloaded, first_pleasure, error", "(motion lines:1.3)", "sweat", "sound_effects"),
        ("05_desbordada", "(deep penetration:1.5), balls_deep", "overload, sparking, ahegao, malfunction", "(motion lines:1.5)", "excessive_sweat, drooling", "sound_effects, onomatopoeia"),
        ("06_reiniciada", "after_sex", "reset, blank, cum_on_metal", "", "semen_on_body", ""),
    ],
    "angel_caido": [
        ("01_celestial", "", "angel, halo, wings, pure, white_robes", "", "", ""),
        ("02_tentada", "(imminent penetration:1.2)", "tempted, blushing, forbidden_desire", "", "blush", ""),
        ("03_cayendo", "about_to_penetrate", "wings_darkening, halo_cracking, surrendering", "", "sweat", ""),
        ("04_caida", "(deep penetration:1.3)", "black_wings, fallen, corrupted", "(motion lines:1.3)", "sweat, drooling", ""),
        ("05_libertina", "(deep penetration:1.5), balls_deep", "lustful, seductive, ahegao, dark_angel", "(motion lines:1.4)", "excessive_sweat, drooling", "sound_effects"),
        ("06_condenada", "after_sex", "broken_halo, cum_stained, forsaken", "", "semen_on_body", ""),
    ],
    "vampiro": [
        ("01_presa", "", "victim, scared, neck_exposed", "", "", ""),
        ("02_mordida", "(imminent penetration:1.2)", "bite, blood, fangs, dizzy", "", "nervous_sweat", ""),
        ("03_drenada", "about_to_penetrate", "weakened, pale, blood_loss", "", "sweat", ""),
        ("04_transformada", "(deep penetration:1.3)", "fangs_growing, red_eyes, turning", "(motion lines:1.2)", "sweat", ""),
        ("05_vampira", "(deep penetration:1.5), balls_deep", "vampire, seductive, bloodthirsty, ahegao", "(motion lines:1.4)", "excessive_sweat, drooling", "sound_effects"),
        ("06_eterna", "after_sex", "immortal, dark, cum_covered", "", "semen_on_body", ""),
    ],
    "apuesta": [
        ("01_confiada", "", "cocky, betting, overconfident", "", "", ""),
        ("02_jugando", "(imminent penetration:1.2)", "card_game, tense, nervous", "", "nervous_sweat", ""),
        ("03_perdiendo", "about_to_penetrate", "losing, worried, desperate", "", "sweat", ""),
        ("04_perdida", "(deep penetration:1.3)", "lost_bet, defeated, reluctant", "", "sweat, tears", ""),
        ("05_pagando", "(deep penetration:1.5), balls_deep", "paying_up, forced, humiliated, ahegao", "(motion lines:1.4)", "excessive_sweat, drooling", "sound_effects"),
        ("06_sin_apuesta", "after_sex", "broke, cum_covered, no_way_out", "", "semen_on_body, cum_pool", ""),
    ],
    "clon": [
        ("01_original", "", "solo, alone, unaware", "", "", ""),
        ("02_duplicada", "(imminent penetration:1.2)", "clone_appearing, confused, mirror", "", "nervous_sweat", ""),
        ("03_dos", "about_to_penetrate", "clone, double, threesome_with_self", "", "sweat", ""),
        ("04_multiples", "(deep penetration:1.3)", "many_clones, surrounded_by_self", "(motion lines:1.3)", "sweat, drooling", ""),
        ("05_orgia_self", "(deep penetration:1.5), balls_deep", "selfcest, clone_gangbang, ahegao", "(motion lines:1.5)", "excessive_sweat, drooling", "sound_effects, onomatopoeia"),
        ("06_fusion", "after_sex", "clones_merging, exhausted, single_again", "", "semen_on_body", ""),
    ],
    "ntr": [
        ("01_fiel", "", "loyal, in_love, committed", "", "", ""),
        ("02_dudando", "(imminent penetration:1.2)", "tempted, guilty, torn", "", "nervous_sweat", ""),
        ("03_ocultando", "about_to_penetrate", "secret_meeting, hidden, blush", "", "sweat", ""),
        ("04_traicion", "(deep penetration:1.3)", "cheating, pleasure, betrayal", "(motion lines:1.3)", "sweat, drooling", "sound_effects"),
        ("05_descubierta", "(deep penetration:1.5), balls_deep", "caught, guilt, exposed, ahegao", "(motion lines:1.4)", "excessive_sweat", "sound_effects"),
        ("06_ruptura", "after_sex", "alone, regret, cum_covered, broken", "", "semen_on_body", ""),
    ],
    "sirena": [
        ("01_nadando", "", "underwater, tail, graceful, mermaid", "", "", ""),
        ("02_superficie", "(imminent penetration:1.2)", "surfacing, wet, curious", "", "wet", ""),
        ("03_tierra", "about_to_penetrate", "legs_forming, naked, vulnerable", "", "sweat", ""),
        ("04_primer_sexo", "(deep penetration:1.3)", "first_human_contact, curious, shy", "(motion lines:1.2)", "sweat", ""),
        ("05_apasionada", "(deep penetration:1.5), balls_deep", "intense, wet, moaning, splashing, ahegao", "(motion lines:1.4)", "excessive_sweat", "sound_effects"),
        ("06_reposo", "after_sex", "floating, exhausted, glowing_scales", "", "semen_on_body", ""),
    ],
    "fotografia": [
        ("01_vestida", "", "posed, clothed, gravure_style, smiling", "", "", ""),
        ("02_semidesnuda", "(imminent penetration:1.2)", "revealing, blushing, embarrassed", "", "blush", ""),
        ("03_desnuda", "about_to_penetrate", "nude_model, covering, nervous", "", "nervous_sweat", ""),
        ("04_provocativa", "(deep penetration:1.3)", "lewd_pose, spread, inviting", "(motion lines:1.2)", "sweat", ""),
        ("05_explicita", "(deep penetration:1.5), balls_deep", "full_exposure, toys, masturbation, ahegao", "(motion lines:1.4)", "excessive_sweat, drooling", "sound_effects"),
        ("06_final", "after_sex", "cum_covered, exhausted, camera_flash", "", "semen_on_body", ""),
    ],
    "enfermera": [
        ("01_consulta", "", "nurse_outfit, professional, calm", "", "", ""),
        ("02_examen", "(imminent penetration:1.2)", "checkup, exposed, embarrassed", "", "nervous_sweat", ""),
        ("03_tratamiento", "about_to_penetrate", "injection, medicine, weird_feeling", "", "sweat", ""),
        ("04_efecto", "(deep penetration:1.3)", "dizzy, flushed, side_effect", "(motion lines:1.2)", "sweat, drooling", ""),
        ("05_necesitada", "(deep penetration:1.5), balls_deep", "patient_desperate, begging, arousal, ahegao", "(motion lines:1.4)", "excessive_sweat, drooling", "sound_effects"),
        ("06_curada", "after_sex", "treated, satisfied, messy", "", "semen_on_body", ""),
    ],
    "profesora": [
        ("01_clase", "", "student_uniform, attentive, innocent", "", "", ""),
        ("02_asesoria", "(imminent penetration:1.2)", "after_school, close, blush", "", "nervous_sweat", ""),
        ("03_tocando", "about_to_penetrate", "inappropriate_touch, nervous, frozen", "", "sweat", ""),
        ("04_rendida", "(deep penetration:1.3)", "surrendering, moaning, forbidden", "(motion lines:1.3)", "sweat, drooling", "sound_effects"),
        ("05_adicta", "(deep penetration:1.5), balls_deep", "secret_affair, eager, passionate, ahegao", "(motion lines:1.4)", "excessive_sweat", "sound_effects"),
        ("06_calificada", "after_sex", "graded, cum_covered, ruined_uniform", "", "semen_on_body", ""),
    ],
    "guerra": [
        ("01_capturada", "", "prisoner, bound, defiant", "", "", ""),
        ("02_interrogada", "(imminent penetration:1.2)", "interrogation, threatened, scared", "", "nervous_sweat", ""),
        ("03_quebrada", "about_to_penetrate", "broken, crying, defeated", "", "sweat, tears_streaming", ""),
        ("04_servil", "(deep penetration:1.3)", "forced_service, obedient, humiliated", "(motion lines:1.3)", "sweat, drooling", "sound_effects"),
        ("05_usada", "(deep penetration:1.5), balls_deep", "used_by_enemy, ahegao, mind_broken", "(motion lines:1.4)", "excessive_sweat, tears", "sound_effects"),
        ("06_liberada", "after_sex", "released, scarred, cum_stained", "", "semen_on_body", ""),
    ],
}

CHAR = "stell4virigiadef, 1girl, white hair, long hair, blunt bangs, double-parted bangs, red eyes, demon horns, low wings, large breasts"
OUTFIT = "white bonnet, white cloak, frilled cloak, black dress, detached collar, black bowtie, red ribbon, cleavage, black gloves, white pantyhose, high heels, clothes_lift"
EXTRA_NEG = ", holding mirror, red mirror, mirror"
LORA = "Stella-Virigia-v1.safetensors"
SEED = 42424249

count = 0
for sname, stages in STRUCTURES.items():
    nodes = {}
    nodes["ckpt"] = {"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":CKPT}}
    nodes["latent_shared"] = {"class_type":"EmptyLatentImage","inputs":{"width":1024,"height":1536,"batch_size":1}}
    nodes["clip_skip"] = {"class_type":"CLIPSetLastLayer","inputs":{"clip":["ckpt",1],"stop_at_clip_layer":-2}}
    nodes["lora_char"] = {"class_type":"LoraLoader","inputs":{"model":["ckpt",0],"clip":["clip_skip",0],"lora_name":LORA,"strength_model":1.0,"strength_clip":1.0}}
    nodes["lora_depth"] = {"class_type":"LoraLoader","inputs":{"model":["lora_char",0],"clip":["lora_char",1],"lora_name":"penetration_depth.safetensors","strength_model":1.5,"strength_clip":1.0}}
    nodes["lora_dp"] = {"class_type":"LoraLoader","inputs":{"model":["lora_depth",0],"clip":["lora_depth",1],"lora_name":"doublepenetration_r1.safetensors","strength_model":1.0,"strength_clip":1.0}}
    nodes["lora_size"] = {"class_type":"LoraLoader","inputs":{"model":["lora_dp",0],"clip":["lora_dp",1],"lora_name":"Penis Size Slider - Illustrious - V5_alpha1.0_rank4_noxattn_last.safetensors","strength_model":0.5,"strength_clip":1.0}}
    nodes["neg"] = {"class_type":"CLIPTextEncode","inputs":{"text":NEG + EXTRA_NEG,"clip":["lora_size",1]}}

    for pose_name, pose_tags in POSES.items():
        for n, depth, expr, motion, fluids, sound in stages:
            parts = ["score_9, score_8_up, source_anime, rating_explicit", CHAR, OUTFIT, MALE, "doublepen, vaginal, anal, double_penetration, both_holes", depth, pose_tags, expr, fluids]
            if motion: parts.append(motion)
            if sound: parts.append(sound)
            parts.append(LIGHT + ", anime, masterpiece, best_quality")
            prompt = ", ".join([p for p in parts if p]).replace(", ,", ",").replace(",,", ",")
            key = f"{pose_name}_{n}"
            nodes[f"p_{key}"] = {"class_type":"CLIPTextEncode","inputs":{"text":prompt,"clip":["lora_size",1]}}
            nodes[f"k_{key}"] = {"class_type":"KSampler","inputs":{"seed":SEED,"steps":20,"cfg":3.5,"sampler_name":"dpmpp_2m","scheduler":"karras","denoise":1,"model":["lora_size",0],"positive":[f"p_{key}",0],"negative":["neg",0],"latent_image":["latent_shared",0]}}
            nodes[f"d_{key}"] = {"class_type":"VAEDecode","inputs":{"samples":[f"k_{key}",0],"vae":["ckpt",2]}}
            nodes[f"s_{key}"] = {"class_type":"SaveImage","inputs":{"filename_prefix":f"virigia_{sname}_{pose_name}_{n}","images":[f"d_{key}",0]}}

    with open(os.path.join(B, f"workflow_virigia_{sname}.json"), "w", encoding="utf-8") as f:
        json.dump(nodes, f, indent=2, ensure_ascii=False)
    count += 1

print(f"✅ {count} estructuras x 30 img = {count*30} imagenes")
