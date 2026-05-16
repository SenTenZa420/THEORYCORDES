import numpy as np
from skyfield.api import Topos, load, Star

def run_orion_calibration():
    print("================================================================================")
    print("✨ ARCHITECTURE STELLAIRE D'ORION (RNIOG ULTRA-CORE) - FIXED VECTORS")
    print("================================================================================")
    
    ts = load.timescale()
    eph = load('de421.bsp')
    earth = eph['earth']
    
    # Point d'ancrage géodésique SGE : Magog
    magog_station = earth + Topos(latitude_degrees=45.2683, longitude_degrees=-72.1481, elevation_m=200)
    now = ts.now()
    
    print(f"[+] Alignement temporel (Julian Date) : {now.tt:.6f}")
    print("-" * 80)
    print(f"{'ÉTOILE':<12} | {'RA (DECIMALE)':<15} | {'DEC (DECIMALE)':<15} | {'ALTITUDE':<12} | {'AZIMUT'}")
    print("-" * 80)
    
    # Base de données J2000 brute des sommets et du Baudrier
    orion_catalog = {
        "Betelgeuse": {"ra": (5, 55, 10.3), "dec": (7, 24, 25)},
        "Bellatrix":  {"ra": (5, 25, 7.9),  "dec": (6, 20, 59)},
        "Alnitak":    {"ra": (5, 40, 45.5), "dec": (-1, -56, -34)},
        "Alnilam":    {"ra": (5, 36, 12.8), "dec": (-1, -12, -7)},
        "Mintaka":    {"ra": (5, 32, 0.4),  "dec": (0, -17, -57)},
        "Saiph":      {"ra": (5, 47, 45.4), "dec": (-9, -40, -11)},
        "Rigel":      {"ra": (5, 14, 32.3), "dec": (-8, -12, -6)}
    }
    
    for name, coords in orion_catalog.items():
        # Conversion brute en heures décimales pour l'Ascension Droite
        ra_h = coords["ra"][0] + coords["ra"][1]/60.0 + coords["ra"][2]/3600.0
        
        # Conversion brute en degrés décimaux pour la Déclinaison
        d, m, s = coords["dec"]
        sign = -1.0 if (d < 0 or m < 0 or s < 0) else 1.0
        dec_d = sign * (abs(d) + abs(m)/60.0 + abs(s)/3600.0)
        
        # Définition de la cible fixe
        star_target = Star(ra_hours=ra_h, dec_degrees=dec_d)
        
        # Calcul de la position apparente locale brute
        astrometric = magog_station.at(now).observe(star_target).apparent()
        alt, az, _ = astrometric.altaz()
        
        print(f"{name:<12} | {ra_h:<15.6f} | {dec_d:<15.6f} | {alt.degrees:<12.4f} | {az.degrees:.4f}°")
        
    print("-" * 80)
    print("[+] Constat spatial : Les vecteurs fixes d'Orion sont résolus pour l'horizon SGE.")
    print("================================================================================")

if __name__ == "__main__":
    run_orion_calibration()
