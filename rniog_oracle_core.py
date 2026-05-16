import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("================================================================================")
print("🔮 RUN CENTRAL V5 : COUPLAGE GÉOPHYSIQUE ET MOTEUR DE DÉRIVE (RNIOG / K.L.I.S.H.)")
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
    
    # Archivage persistant
    rniog_matrix_logger.log_current_matrix()
    print("\n")
    
    # Analyse de la dérive différentielle
    rniog_correlation_engine.analyze_telemetry_drift()
    
    print("-" * 80)
    print("[+] Fin de séquence V5 : Alignement, persistance et diagnostic de dérive achevés.")
    print("================================================================================")

except ImportError as e:
    print(f"[-] Erreur de structure : Un des modules du noyau est introuvable. {str(e)}")
except Exception as e:
    print(f"[-] Interruption du noyau : {str(e)}")
