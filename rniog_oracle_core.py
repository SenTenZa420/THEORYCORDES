import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("================================================================================")
print("🔮 RUN CENTRAL V4 : ARCHITECTURE GLOBALE ET LOGGING INTERNE (RNIOG / K.L.I.S.H.)")
print("================================================================================")

try:
    import rniog_ephemeris_core
    import rniog_gravity_tensor
    import rniog_spectral_fft
    import rniog_weather_oracle
    import klish_metrology_translator
    import rniog_orion_matrix
    import rniog_matrix_logger
    
    print("[+] Initialisation de la séquence d'audit global unifiée...")
    print("-" * 80)
    
    # Exécution séquentielle des flux physiques et métrologiques
    rniog_ephemeris_core.run_ephemeris_audit()
    print("\n")
    rniog_gravity_tensor.calculate_gravity_perturbation()
    print("\n")
    rniog_spectral_fft.run_spectral_analysis()
    print("\n")
    rniog_weather_oracle.run_weather_oracle()
    print("\n")
    klish_metrology_translator.run_klish_metrology()
    print("\n")
    rniog_orion_matrix.run_orion_calibration()
    print("\n")
    
    # Exécution du module d'archivage persistant
    rniog_matrix_logger.log_current_matrix()
    
    print("-" * 80)
    print("[+] Fin de séquence V4 : Alignement et persistance des données validés.")
    print("================================================================================")

except ImportError as e:
    print(f"[-] Erreur de structure : Un des modules du noyau est introuvable. {str(e)}")
except Exception as e:
    print(f"[-] Interruption du noyau : {str(e)}")
