import numpy as np
from skyfield.api import Topos, load

def calculate_gravity_perturbation():
    print("================================================================================")
    print("🌋 EXTRACTEUR DU TENSEUR DE MARÉE TERRESTRE (RNIOG ULTRA-CORE) - RAW")
    print("================================================================================")
    
    # Constantes physiques brutes
    # G * M en m³/s² (Paramètres gravitationnels standards de la NASA)
    GM_MOON = 4902.801 * (10**9)
    GM_SUN = 132712440018 * (10**9)
    R_EARTH = 6371008.0 # Rayon moyen de l'Estrie en mètres
    
    # Chargement
    ts = load.timescale()
    eph = load('de421.bsp')
    earth, sun, moon = eph['earth'], eph['sun'], eph['moon']
    magog_station = earth + Topos(latitude_degrees=45.2683, longitude_degrees=-72.1481, elevation_m=200)
    
    now = ts.now()
    state_station = magog_station.at(now)
    
    # Vecteurs bruts de position (distance r en mètres)
    pos_sun = state_station.observe(sun).apparent()
    dist_sun_m = pos_sun.distance().m
    alt_sun, _, _ = pos_sun.altaz()
    
    pos_moon = state_station.observe(moon).apparent()
    dist_moon_m = pos_moon.distance().m
    alt_moon, _, _ = pos_moon.altaz()
    
    # Angles zénithaux complexes (psi = 90° - altitude)
    psi_sun = np.radians(90.0 - alt_sun.degrees)
    psi_moon = np.radians(90.0 - alt_moon.degrees)
    
    # Équation différentielle de Longman pour la composante verticale (en m/s²)
    # delta_g = (GM * R / r³) * (3*cos²(psi) - 1)
    dg_sun = (GM_SUN * R_EARTH / (dist_sun_m**3)) * (3 * np.cos(psi_sun)**2 - 1.0)
    dg_moon = (GM_MOON * R_EARTH / (dist_moon_m**3)) * (3 * np.cos(psi_moon)**2 - 1.0)
    
    # Conversion en microgals (1 m/s² = 10^8 microgals)
    dg_sun_ugal = dg_sun * (10**8)
    dg_moon_ugal = dg_moon * (10**8)
    dg_total = dg_sun_ugal + dg_moon_ugal
    
    print(f"[+] Vecteurs de distance radiale (NASA DE421) :")
    print(f" * Distance R-Lune : {dist_moon_m / 1000.0:.3f} km")
    print(f" * Distance R-Soleil : {dist_sun_m / 1000.0:.3f} km")
    print("-" * 80)
    print("[+] Accélération gravitationnelle induite (Composante Verticale) :")
    print(f" * Perturbation Solaire : {dg_sun_ugal:.6f} μGal")
    print(f" * Perturbation Lunaire : {dg_moon_ugal:.6f} μGal")
    print(f" * Distorsion Totale    : {dg_total:.6f} μGal")
    print("-" * 80)
    print(f"[+] Statut dynamique : L'écorce terrestre locale subit une variation brute de {dg_total/100:.6f} mg.")
    print("================================================================================")

if __name__ == "__main__":
    calculate_gravity_perturbation()
