import numpy as np

def analyze_d_branes():
    print("================================================================================")
    print("🧱 EXTRACTEUR DE D-BRANES : TENSION GÉOMÉTRIQUE & SPECTRE ENTRÉMÊLÉ (RAW)")
    print("================================================================================")
    
    alpha_prime = 1.0  # Constante de Regge
    string_tension = 1.0 / (2.0 * np.pi * alpha_prime)
    
    # Séparations spatiales brutes (en mètres de Planck / unités arbitraires non lissées)
    # Entre Brane A et Brane B
    separations = [0.0, 0.5, 2.0, 10.0]
    
    print(f"[+] Tension de la corde fondamentale (T) : {string_tension:.4f}")
    print("-" * 85)
    print(f"{'DIST. SÉPARATION (Y)':<22} | {'NIVEAU EXCIT. N':<15} | {'MASSE CARRÉE DE LA CORDE (M²)'}")
    print("-" * 85)
    
    for Y in separations:
        # La contribution géométrique de l'étirement à la masse carrée est (Y / (2 * pi * alpha_prime))² * (2 * pi)²
        # Ce qui se simplifie rigoureusement en : (Y / alpha_prime)² / (4 * pi²) * 4 * pi² = Y² / alpha_prime²
        m2_stretching = (Y / alpha_prime) ** 2
        
        for N in [0, 1]:
            # Pour une corde ouverte bosonique, l'intercept du vide est a = 1
            # M² = (Y / alpha_prime)² + (1 / alpha_prime) * (N - 1)
            m2_total = m2_stretching + (1.0 / alpha_prime) * (N - 1.0)
            
            if N == 0:
                label = "0 (Vide / Tachyone)"
            else:
                label = "1 (Mode de Jauge)"
                
            print(f"{Y:<22.2f} | {label:<15} | {m2_total:.4f}")
        print("-" * 85)
        
    print("[+] Fait physique : À séparation nulle (Y = 0), le mode N=1 est de masse strictement nulle.")
    print("[+] Il donne naissance au Photon (champ de jauge U(1)) localisé sur la brane.")
    print("[+] Lorsque les branes s'écartent, les champs de jauge acquièrent une masse (Mécanisme de Higgs).")
    print("================================================================================")

if __name__ == "__main__":
    analyze_d_branes()
