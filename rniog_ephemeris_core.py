import numpy as np
from skyfield.api import Topos, load

def run_ephemeris_audit():
    print("================================================================================")
    print("🛰️ AUDIT D'ÉPHÉMÉRIDES BRUTES (RNIOG ULTRA-CORE) - SANS LISSAGE")
    print("================================================================================")
    
    # Chargement des éphémérides planétaires de la NASA (DE421)
    ts = load.timescale()
    eph = load('de421.bsp')
    
    earth, sun, moon = eph['earth'], eph['sun'], eph['moon']
    
    # Point d'ancrage : Magog, Québec (SGE)
    magog_station = earth + Topos(latitude_degrees=45.2683, longitude_degrees=-72.1481, elevation_m=200)
    
    # Temps présent (UTC) pour le calcul brut
    now = ts.now()
    print(f"[+] Horodatage du Run (Temps Terrestre Julian Date TT) : {now.tt:.6f}")
    print("-" * 80)
    
    # Calcul des positions absolues
    astro_sun = magog_station.at(now).observe(sun).apparent()
    alt_sun, az_sun, _ = astro_sun.altaz()
    
    astro_moon = magog_station.at(now).observe(moon).apparent()
    alt_moon, az_moon, _ = astro_moon.altaz()
    
    print("[+] Coordonnées locales brutes du Soleil :")
    print(f" * Altitude : {alt_sun.degrees:.6f}°")
    print(f" * Azimut   : {az_sun.degrees:.6f}°")
    print("\n[+] Coordonnées locales brutes de la Lune :")
    print(f" * Altitude : {alt_moon.degrees:.6f}°")
    print(f" * Azimut   : {az_moon.degrees:.6f}°")
    print("-" * 80)
    
    # Calcul de la séparation angulaire brute entre le Soleil et la Lune (Phase)
    r_alt_sun, r_az_sun = np.radians(alt_sun.degrees), np.radians(az_sun.degrees)
    r_alt_moon, r_az_moon = np.radians(alt_moon.degrees), np.radians(az_moon.degrees)
    
    cos_separation = (np.sin(r_alt_sun) * np.sin(r_alt_moon) + 
                      np.cos(r_alt_sun) * np.cos(r_alt_moon) * np.cos(r_az_sun - r_az_moon))
    
    separation_deg = np.degrees(np.arccos(np.clip(cos_separation, -1.0, 1.0)))
    
    print(f"[+] Séparation angulaire Soleil-Lune : {separation_deg:.4f}°")
    
    # Interprétation de l'alignement des forces
    if separation_deg < 10.0 or separation_deg > 170.0:
        print("[!] Statut : Alignement de Syzygie détecté. Vecteurs de marée cumulés.")
    else:
        print("[*] Statut : Configuration quadratique standard. Forces distribuées.")
    print("================================================================================")

if __name__ == "__main__":
    run_ephemeris_audit()
