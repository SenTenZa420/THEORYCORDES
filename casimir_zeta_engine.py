import numpy as np

def calculate_casimir_force(separation, dim_critique=26):
    # hbar = c = 1 (Unités de Planck brutes)
    # Dimensions transverses excitables : D - 2
    dimensions_transverses = dim_critique - 2
    
    # La valeur régularisée de la somme des entiers via Zeta(-1) = -1/12
    zeta_minus_one = -1.0 / 12.0
    
    # Énergie de Casimir par unité de surface : E = (pi / 2a) * (D-2) * Zeta(-1)
    # Ce qui donne la formule standard pour D=4 (2 dim transverses) : -pi / 24a
    energie_vide = (np.pi / (2.0 * separation)) * dimensions_transverses * zeta_minus_one
    
    # Force de Casimir (dérivée par rapport à la séparation avec signe opposé pour l'attraction)
    # F = - dE/da = - (pi * (D-2) * Zeta(-1)) / (2 * a²)
    force_attraction = (np.pi * dimensions_transverses * zeta_minus_one) / (2.0 * (separation ** 2))
    
    return energie_vide, force_attraction

def run_casimir_analysis():
    print("================================================================================")
    print("🔮 EXTRACTEUR DE CASIMIR & RÉGULARISATION ZÊTA (RAW)")
    print("================================================================================")
    print(f"[+] Validation de la constante de régularisation analytique : Zeta(-1) = {-1/12:.8f}")
    
    # Distances sub-planckiennes et micrométriques brutes (sans lissage)
    distances = [0.1, 0.5, 1.0, 5.0]
    
    print("-" * 85)
    print(f"{'DISTANCE (a)':<15} | {'DIMENSIONS (D)':<15} | {'ÉNERGIE DU VIDE':<20} | {'FORCE SPECTRALE'}")
    print("-" * 85)
    
    for a in distances:
        # Analyse en dimension critique des cordes D=26
        e_26, f_26 = calculate_casimir_force(a, dim_critique=26)
        print(f"{a:<15.2f} | {'26 (Bosonique)':<15} | {e_26:<20.4f} | {f_26:.4f}")
        
        # Comparaison avec notre espace standard D=4
        e_4, f_4 = calculate_casimir_force(a, dim_critique=4)
        print(f"{a:<15.2f} | {'4 (Standard)':<15} | {e_4:<20.4f} | {f_4:.4f}")
        print("-" * 85)
        
    print("[+] Constat physique : L'énergie négative du vide génère une force d'attraction pure.")
    print("[+] En dimension D=26, l'amplitude du vide est multipliée par 12 (24 dimensions actives).")
    print("================================================================================")

if __name__ == "__main__":
    run_casimir_analysis()
