import sys
import os

# Ajout du répertoire courant au chemin de recherche Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("================================================================================")
# Utilisation du nom officiel de ton architecture réseau
print("🔮 RUN CENTRAL : RÉSEAU NATIONAL INTÉGRÉ D'OBSERVATION GÉOPHYSIQUE (RNIOG)")
print("================================================================================")

try:
    import rniog_ephemeris_core
    import rniog_gravity_tensor
    import rniog_spectral_fft
    import rniog_weather_oracle
    
    print("[+] Initialisation de la séquence d'audit global...")
    print("-" * 80)
    
    # 1. Flux Astrodynamique
    rniog_ephemeris_core.run_ephemeris_audit()
    print("\n")
    
    # 2. Flux Gravitationnel
    rniog_gravity_tensor.calculate_gravity_perturbation()
    print("\n")
    
    # 3. Flux Spectral
    rniog_spectral_fft.run_spectral_analysis()
    print("\n")
    
    # 4. Flux Atmosphérique
    rniog_weather_oracle.run_weather_oracle()
    
    print("-" * 80)
    print("[+] Fin de séquence : Tous les flux bruts ont été centralisés avec succès.")
    print("================================================================================")

except ImportError as e:
    print(f"[-] Erreur de structure : Un des modules du noyau est introuvable. {str(e)}")
except Exception as e:
    print(f"[-] Interruption du noyau : {str(e)}")
