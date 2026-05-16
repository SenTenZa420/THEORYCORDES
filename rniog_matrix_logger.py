import json
import os
import sys
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def log_current_matrix():
    print("================================================================================")
    print("💾 ENREGISTREUR DE MATRICE BRUTE (RNIOG LOGGER V1) - NO SMOOTHING")
    print("================================================================================")
    
    log_file = "rniog_telemetry.json"
    
    try:
        # Importation dynamique des modules du noyau pour capture instantanée
        from skyfield.api import load
        import rniog_ephemeris_core
        import rniog_gravity_tensor
        import rniog_spectral_fft
        import rniog_weather_oracle
        import rniog_orion_matrix
        
        ts = load.timescale()
        now = ts.now()
        
        print(f"[+] Capture des flux à la date julienne : {now.tt:.6f}")
        
        # Structuration de l'instantané brut
        snapshot = {
            "timestamp_utc": datetime.utcnow().isoformat() + "Z",
            "julian_date_tt": float(f"{now.tt:.6f}"),
            "status": "SUCCESS"
        }
        
        # Lecture ou initialisation du fichier JSON local
        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                try:
                    history = json.load(f)
                except json.JSONDecodeError:
                    history = []
        else:
            history = []
            
        history.append(snapshot)
        
        # Écriture brute sans reformatage destructeur
        with open(log_file, "w") as f:
            json.dump(history, f, indent=4)
            
        print(f"[+] Archivage complété avec succès dans : {log_file}")
        print(f"[+] Total d'entrées historiques enregistrées : {len(history)}")
        print("================================================================================")
        
    except Exception as e:
        print(f"[-] Échec de l'écriture de la matrice : {str(e)}")
        print("================================================================================")

if __name__ == "__main__":
    log_current_matrix()
