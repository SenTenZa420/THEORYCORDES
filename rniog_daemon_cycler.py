import os
import sys
import time
import subprocess

def run_continuous_audit(interval_seconds=60, max_runs=10):
    print("================================================================================")
    print("🛸 DÉMON D'ACQUISITION CONTINU V8 (RNIOG / K.L.I.S.H.)")
    print("================================================================================")
    print(f"[+] Cadence configurée : 1 snapshot toutes les {interval_seconds} secondes.")
    print(f"[+] Limite de la séquence : {max_runs} runs consécutifs.")
    print("-" * 80)

    try:
        for loop in range(1, max_runs + 1):
            print(f"\n[🔄 LOOP {loop:02d}/{max_runs:02d}] Initialisation de l'acquisition...")
            
            # Exécution de l'Oracle principal
            process = subprocess.Popen([sys.executable, "rniog_oracle_core.py"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            
            # Lecture du flux en temps réel pour affichage console
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    print(output.strip())
                    
            rc = process.poll()
            if rc != 0:
                print(f"[-] Alerte : L'Oracle a retourné un code d'erreur ({rc}). Interruption.")
                break
                
            if loop < max_runs:
                print(f"\n[⏳ ATTENTE] Temporisation brute de {interval_seconds}s avant le prochain vecteur...")
                time.sleep(interval_seconds)
                
        print("\n================================================================================")
        print("[+] Fin de la boucle d'acquisition automatique V8. Historique enrichi.")
        print("================================================================================")
        
    except KeyboardInterrupt:
        print("\n[-] Démon interrompu manuellement par l'opérateur (SIGINT).")
        print("================================================================================")

if __name__ == "__main__":
    # Configuration par défaut : 60 secondes d'intervalle, 5 runs pour accumuler la dérive
    run_continuous_audit(interval_seconds=60, max_runs=5)
