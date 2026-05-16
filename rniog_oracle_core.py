import sys
import os
import re
import io

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("================================================================================")
print("🔮 RUN CENTRAL V8 : INTERCEPTION INTERNE DU STDOUT DE CAPTURE (RAW ONLY)")
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
    
    # 2. Tenseur de marée crustale avec interception du STDOUT
    stdout_capture = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = stdout_capture
    try:
        rniog_gravity_tensor.calculate_gravity_perturbation()
    finally:
        sys.stdout = old_stdout
    
    gravity_output = stdout_capture.getvalue()
    print(gravity_output.strip())
    print("\n")
    
    # Extraction Regex Marée
    match_g = re.search(r"Distorsion Totale\s*:\s*([\d\.]+)\s*μGal", gravity_output)
    if match_g:
        g_distortion = float(match_g.group(1))
    else:
        raise ValueError("[-] Erreur critique : Impossible de parser la distorsion gravitationnelle brute.")
        
    # 3. Analyse spectrale FFT avec interception du STDOUT
    stdout_capture = io.StringIO()
    sys.stdout = stdout_capture
    try:
        rniog_spectral_fft.run_spectral_analysis()
    finally:
        sys.stdout = old_stdout
        
    fft_output = stdout_capture.getvalue()
    print(fft_output.strip())
    print("\n")
    
    # Extraction Regex Schumann Freq 7.8Hz
    match_s = re.search(r"7\.8000\s*\|\s*([\d\.]+)", fft_output)
    if match_s:
        s_amplitude = float(match_s.group(1))
    else:
        raise ValueError("[-] Erreur critique : Impossible de parser l'amplitude Schumann brute.")
    
    # 4. Télémétrie atmosphérique
    rniog_weather_oracle.run_weather_oracle()
    print("\n")
    
    # 5. Métrologie sexagésimale (Projet K.L.I.S.H.)
    klish_metrology_translator.run_klish_metrology()
    print("\n")
    
    # 6. Référentiel Orion
    rniog_orion_matrix.run_orion_calibration()
    print("\n")
    
    # 7. Archivage persistant enrichi V2 (Valeurs 100% dynamiques et vérifiées)
    rniog_matrix_logger.log_current_matrix(gravity_distortion=g_distortion, schumann_amplitude=s_amplitude)
    print("\n")
    
    # 8. Moteur de dérive et calcul de Pearson
    rniog_correlation_engine.analyze_telemetry_drift()
    
    print("-" * 80)
    print("[+] Fin de séquence V8 : Flux de console purifiés d'artefacts.")
    print("================================================================================")

except ImportError as e:
    print(f"[-] Erreur de structure : Un des modules du noyau est introuvable. {str(e)}")
except Exception as e:
    print(f"[-] Interruption du noyau : {str(e)}")
