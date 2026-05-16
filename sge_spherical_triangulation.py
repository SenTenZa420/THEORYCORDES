import numpy as np

def haversine_distance_and_arc(coord1, coord2):
    # Rayon moyen de la Terre (km)
    R = 6371.008
    
    lat1, lon1 = np.radians(coord1)
    lat2, lon2 = np.radians(coord2)
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    
    distance = R * c
    return distance, c  # Retourne la distance en km ET l'arc en radians (ê)

def calculate_spherical_angle(arc_a, arc_b, arc_c):
    # Loi des cosines sphériques pour l'angle opposé à l'arc_c
    cos_angle = (np.cos(arc_c) - np.cos(arc_a) * np.cos(arc_b)) / (np.sin(arc_a) * np.sin(arc_b))
    return np.degrees(np.arccos(np.clip(cos_angle, -1.0, 1.0)))

def run_sge_spherical():
    print("================================================================================")
    print("📐 ANALYSEUR GÉODÉSIQUE SGE V2 : TRIGONOMÉTRIE SPHÉRIQUE BRUTE (RAW)")
    print("================================================================================")
    
    # Coordonnées du triangle fondamental de l'Estrie
    sommets = {
        "Mont Orford": (45.3181, -72.2442),
        "Owl's Head": (45.0636, -72.2983),
        "Mont Sutton": (45.0844, -72.5592)
    }
    
    # Extraction des distances et des arcs unitaires (radians)
    dist_A, arc_A = haversine_distance_and_arc(sommets["Owl's Head"], sommets["Mont Sutton"])   # Côté opposé à Orford
    dist_B, arc_B = haversine_distance_and_arc(sommets["Mont Sutton"], sommets["Mont Orford"])  # Côté opposé à Owl's Head
    dist_C, arc_C = haversine_distance_and_arc(sommets["Mont Orford"], sommets["Owl's Head"])   # Côté opposé à Sutton
    
    print("[+] Matrice des arcs et distances géodésiques :")
    print(f" * Orford <-> Owl's Head (c) : {dist_C:.4f} km  [Arc: {arc_C:.6f} rad]")
    print(f" * Owl's Head <-> Sutton (a) : {dist_A:.4f} km  [Arc: {arc_A:.6f} rad]")
    print(f" * Sutton <-> Orford     (b) : {dist_B:.4f} km  [Arc: {arc_B:.6f} rad]")
    print("-" * 80)
    
    # Calcul des angles réels par la loi sphérique
    angle_orford = calculate_spherical_angle(arc_B, arc_C, arc_A)
    angle_owls = calculate_spherical_angle(arc_A, arc_C, arc_B)
    angle_sutton = calculate_spherical_angle(arc_A, arc_B, arc_C)
    
    somme_angles = angle_orford + angle_owls + angle_sutton
    exces_spherique = somme_angles - 180.0
    
    # Conversion de l'excès en secondes d'arc pour mesurer la déviation micro-géodésique
    exces_secondes = exces_spherique * 3600.0
    
    print("[+] Structure angulaire réelle (Non-Euclidienne) :")
    print(f" * Angle au sommet (Mont Orford) : {angle_orford:.6f}°")
    print(f" * Angle au sommet (Owl's Head)  : {angle_owls:.6f}°")
    print(f" * Angle au sommet (Mont Sutton)  : {angle_sutton:.6f}°")
    print(f" * Somme réelle des angles       : {somme_angles:.6f}°")
    print(f" * Excès sphérique calculé       : {exces_spherique:.8f}° ({exces_secondes:.4f} secondes d'arc)")
    print("================================================================================")

if __name__ == "__main__":
    run_sge_spherical()
