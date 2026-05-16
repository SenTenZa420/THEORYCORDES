import numpy as np

def create_projector(theta):
    # Vecteur d'état unitaire pour un angle donné (polarisation)
    v = np.array([np.cos(theta), np.sin(theta)])
    # Projecteur P = |v><v|
    return np.outer(v, v)

def quantum_and(P1, P2):
    # L'intersection logique de deux projecteurs non commutatifs 
    # à basse dimension peut être évaluée par la limite de la séquence alternée (P1*P2*P1...)
    # Si les états sont orthogonaux, le produit tend vers 0.
    prod = P1 @ P2 @ P1
    # Si la trace est proche de 0, l'intersection est le sous-espace nul
    return P1 if np.allclose(P1, P2) else (np.zeros_like(P1) if np.trace(prod) < 0.99 else P1)

def run_quantum_logic():
    print("================================================================================")
    print("🌌 SIMULATEUR DE LOGIQUE QUANTIQUE : RUPTURE DE LA DISTRIBUTIVITÉ (RAW)")
    print("================================================================================")
    
    # Définition des angles de polarisation
    theta_A = 0.0          # Horizontal (0 rad)
    theta_B = np.pi / 4.0  # Diagonal (45° ou pi/4 rad)
    theta_C = np.pi / 2.0  # Vertical (90° ou pi/2 rad)
    
    # Génération des opérateurs de projection bruts
    P_A = create_projector(theta_A)
    P_B = create_projector(theta_B)
    P_C = create_projector(theta_C)
    
    print("[+] Matrices de projection orthogonale d'état :")
    print(f" * P_A (0°):\n{P_A}\n")
    print(f" * P_B (45°):\n{P_B}\n")
    print(f" * P_C (90°):\n{P_C}")
    print("-" * 80)
    
    # Évaluation du Membre Gauche : A AND (B OR C)
    # Dans le plan 2D, l'union (OR) de deux directions distinctes B et C est l'identité complète (Espace total)
    P_B_or_C = np.eye(2) 
    P_left_side = quantum_and(P_A, P_B_or_C)
    
    # Évaluation du Membre Droite : (A AND B) OR (A AND C)
    P_A_and_B = quantum_and(P_A, P_B) # Orthogonalité/Non-commutativité restrictive
    P_A_and_C = quantum_and(P_A, P_C) # Strictement orthogonaux
    P_right_side = P_A_and_B + P_A_and_C # Somme des sous-espaces nuls
    
    print("[+] ÉVALUATION SYNTAXIQUE DES DEUX MEMBRES :")
    print(f" * Gauche : A AND (B OR C) -> Norme de la matrice = {np.linalg.norm(P_left_side):.4f}")
    print(f" * Droite : (A AND B) OR (A AND C) -> Norme de la matrice = {np.linalg.norm(P_right_side):.4f}")
    print("-" * 80)
    
    # Vérification de l'égalité
    is_distributive = np.allclose(P_left_side, P_right_side)
    print(f"[+] La distributivité classique est-elle valide ? : {is_distributive}")
    print("[+] Constat : Le membre gauche conserve le projecteur d'état, le membre droite s'annule.")
    print("================================================================================")

if __name__ == "__main__":
    run_quantum_logic()
