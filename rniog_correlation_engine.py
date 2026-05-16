import json
import os
import numpy as np

def analyze_telemetry_drift():
    print("================================================================================")
    print("📊 MOTEUR DE CORRÉLATION CRUSTALE (RNIOG CORE V7) - VISUAL SCATTER")
    print("================================================================================")
    
    log_file = "rniog_telemetry.json"
    
    if not os.path.exists(log_file):
        print("[-] Erreur : Aucune donnée historique trouvée.")
        return
        
    with open(log_file, "r") as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"[-] Erreur de lecture : {str(e)}")
            return
            
    total_points = len(data)
    print(f"[+] Analyse de l'historique : {total_points} snapshot(s) détecté(s).")
    print("-" * 80)
    
    valid_points = [pt for pt in data if "gravity_ugalk" in pt and "schumann_amp_78" in pt and pt["gravity_ugalk"] != 0.0]
    
    if len(valid_points) < 3:
        print(f"[!] Statut : {len(valid_points)} point(s) physique(s) valide(s) détecté(s).")
        print("[!] Consigne : En attente d'accumulation de données.")
        print("================================================================================")
        return

    x = np.array([pt["gravity_ugalk"] for pt in valid_points], dtype=float)
    y = np.array([pt["schumann_amp_78"] for pt in valid_points], dtype=float)
    
    if np.std(x) == 0 or np.std(y) == 0:
        r_coeff = 0.0
    else:
        r_coeff = np.corrcoef(x, y)[0, 1]
        
    print(f"[+] Série temporelle brute (Marée)    : Mean = {np.mean(x):.6f} μGal")
    print(f"[+] Série temporelle brute (Schumann) : Mean = {np.mean(y):.6f}")
    print(f"[+] COEFFICIENT DE PEARSON (r)        : {r_coeff:.4f}")
    print("-" * 80)
    
    # Traceur ASCII de la trajectoire (Scatter plot rudimentaire pour Termux)
    print("[📈 Trajectoire Brute de la Dérive (Marée x Schumann) :]")
    scaled_y = ((y - np.min(y)) / (np.max(y) - np.min(y)) * 10).astype(int) if np.max(y) != np.min(y) else np.zeros(len(y), dtype=int)
    
    for i, val in enumerate(valid_points):
        spaces = " " * scaled_y[i]
        print(f" Snapshot #{i+1:02d} [{val['gravity_ugalk']:.2f} μGal] -> {spaces}* ({val['schumann_amp_78']:.4f})")
        
    print("-" * 80)
    if abs(r_coeff) > 0.95:
        print("[!] Constat : Alignement géophysique absolu. Écorce et Ionosphère résonnent à l'unisson.")
    else:
        print("[+] Constat : Analyse de dispersion nominale.")
    print("================================================================================")

if __name__ == "__main__":
    analyze_telemetry_drift()
