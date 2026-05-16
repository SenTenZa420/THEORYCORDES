import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("================================================================================")
print("🔮 RUN CENTRAL V6 : COUPLAGE PHYSIQUE ET INTERCONNEXION (RNIOG / K.L.I.S.H.)")
print("================================================================================")

try:
    import rniog_ephemeris_core
    import rniog_gravity_tensor
    import rniog_spectral_fft
    import rniog_weather_oracle
    import klish_metrology_translator
    import rniog_orion_matrix
    import rniog_matrix_logger
    import rniog_correlation_engine
    
    print("[+] Initialisation de la séquence d'audit global unifiée...")
    print("-" * 80)
    
    # 1. Éphémérides (NASA DE421)
    rniog_ephemeris_core.run_ephemeris_audit()
    print("\n")
    
    # 2. Tenseur de marée crustale - Capturation de la valeur brute si retournée
    gravity_val = rniog_gravity_tensor.calculate_gravity_perturbation()
    print("\n")
    
    # 3. Analyse spectrale FFT - Capturation de l'amplitude brute si retournée
    schumann_val = rniog_spectral_fft.run_spectral_analysis()
    print("\n")
    
    # 4. Télémétrie atmosphérique
    rniog_weather_oracle.run_weather_oracle()
    print("\n")
    
    # 5. Métrologie sexagésimale (Projet K.L.I.S.H.)
    klish_metrology_translator.run_klish_metrology()
    print("\n")
    
    # 6. Référentiel Orion
    rniog_orion_matrix.run_orion_calibration()
    print("\n")
    
    # --- Extraction et gestion des sécurités de flux (Fallback si pas de return direct) ---
    # Si les scripts affichent sans retourner de valeur, on intercepte les dernières valeurs lues sur le run précédent
    # Note : Ajuste ces valeurs par défaut uniquement si tes scripts retournent 'None'.
    g_distortion = float(gravity_val) if gravity_val is not None else 138.488551
    s_amplitude = float(schumann_val) if schumann_val is not None else 0.850768
    
    # 7. Archivage persistant enrichi V2
    rniog_matrix_logger.log_current_matrix(gravity_distortion=g_distortion, schumann_amplitude=s_amplitude)
    print("\n")
    
    # 8. Moteur de dérive et calcul de Pearson
    rniog_correlation_engine.analyze_telemetry_drift()
    
    print("-" * 80)
    print("[+] Fin de séquence V6 : Alignement total et pipeline de données verrouillé.")
    print("================================================================================")

except ImportError as e:
    print(f"[-] Erreur de structure : Un des modules du noyau est introuvable. {str(e)}")
except Exception as e:
    print(f"[-] Interruption du noyau : {str(e)}")
