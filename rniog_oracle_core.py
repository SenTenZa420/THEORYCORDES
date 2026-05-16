import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("================================================================================")
print("🔮 RUN CENTRAL V3 : ARCHITECTURE GLOBALE INTÉGRÉE (RNIOG / K.L.I.S.H.)")
print("================================================================================")

try:
    import rniog_ephemeris_core
    import rniog_gravity_tensor
    import rniog_spectral_fft
    import rniog_weather_oracle
    import klish_metrology_translator
    import rniog_orion_matrix
    
    print("[+] Initialisation de la séquence d'audit global unifiée...")
    print("-" * 80)
    
    # 1. Flux Astrodynamique (NASA DE421)
    rniog_ephemeris_core.run_ephemeris_audit()
    print("\n")
    
    # 2. Flux Gravitationnel (Tenseur de Longman)
    rniog_gravity_tensor.calculate_gravity_perturbation()
    print("\n")
    
    # 3. Flux Spectral (FFT Raw)
    rniog_spectral_fft.run_spectral_analysis()
    print("\n")
    
    # 4. Flux Atmosphérique (Télémétrie Locale)
    rniog_weather_oracle.run_weather_oracle()
    print("\n")
    
    # 5. Flux Métrologique Antique (Protocole K.L.I.S.H.)
    klish_metrology_translator.run_klish_metrology()
    print("\n")
    
    # 6. Flux Stellaire Fixe (Référentiel Orion)
    rniog_orion_matrix.run_orion_calibration()
    
    print("-" * 80)
    print("[+] Fin de séquence V3 : Alignement global verrouillé de manière pérenne.")
    print("================================================================================")

except ImportError as e:
    print(f"[-] Erreur de structure : Un des modules du noyau est introuvable. {str(e)}")
except Exception as e:
    print(f"[-] Interruption du noyau : {str(e)}")
