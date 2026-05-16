import numpy as np

def run_clifford_spinor():
    print("================================================================================")
    print("📐 ALGÈBRE DE CLIFFORD & RETOURNEMENT DE PHASE DES SPINEURS DE DIRAC (RAW)")
    print("================================================================================")
    
    # Matrices de Pauli (Générateurs de l'algèbre de Clifford en 2D complexe)
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
    
    print("[+] Validation de la non-commutativité de l'algèbre {sigma_x, sigma_y} :")
    anticommutateur = (sigma_x @ sigma_y) + (sigma_y @ sigma_x)
    print(f" * {{sigma_x, sigma_y}} =\n{anticommutateur}")
    print("-" * 80)
    
    # Spineur d'état initial brut |psi> (spin Up normalisé selon z)
    psi_initial = np.array([1.0, 0.0], dtype=complex)
    
    # Angles de rotation à tester (en radians)
    # pi = 180°, 2*pi = 360° (un tour complet), 4*pi = 720° (deux tours)
    angles = {
        "0 (Initial)": 0.0,
        "pi (180°)": np.pi,
        "2*pi (360° / Tour complet)": 2.0 * np.pi,
        "3*pi (540°)": 3.0 * np.pi,
        "4*pi (720° / Double tour)": 4.0 * np.pi
    }
    
    print(f"{'ANGLE DE ROTATION':<30} | {'SPINEUR RÉSULTANT (RAW)':<32} | {'PRODUIT SCALAIRE <ψ₀|ψₘ>'}")
    print("-" * 85)
    
    for label, theta in angles.items():
        # Opérateur de rotation spinorielle autour de l'axe y : R(theta) = exp(-i * theta * sigma_y / 2)
        # Ce qui s'exprime rigoureusement par : cos(theta/2)*I - i*sin(theta/2)*sigma_y
        op_rotation = np.cos(theta / 2.0) * np.eye(2) - 1j * np.sin(theta / 2.0) * sigma_y
        
        # Application de la transformation au spineur
        psi_rotated = op_rotation @ psi_initial
        
        # Produit scalaire complexe (amplitude de probabilité) avec l'état initial
        produit_scalaire = np.vdot(psi_initial, psi_rotated)
        
        spinor_str = f"[{psi_rotated[0]:.2f}, {psi_rotated[1]:.2f}]"
        print(f"{label:<30} | {spinor_str:<32} | {produit_scalaire:.4f}")
        
    print("-" * 85)
    print("[+] Constat topologique : À 360° (2*pi), le produit scalaire vaut strictement -1.0000.")
    print("[+] La phase a été inversée. Le système exige 720° (4*pi) pour retrouver sa cohérence (+1).")
    print("================================================================================")

if __name__ == "__main__":
    run_clifford_spinor()
