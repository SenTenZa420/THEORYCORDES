import requests
import json

def run_weather_oracle():
    print("================================================================================")
    print("🌤️ CAPTEUR ATMOSPHÉRIQUE BRUT (RNIOG ORACLE V1) - ZERO SIMULATION")
    print("================================================================================")
    
    # Configuration des paramètres bruts pour la station locale (Magog, QC)
    API_KEY = "927c16121d6bee5ec9ed0ef12d63604b"
    LAT = "45.2683"
    LON = "-72.1481"
    
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if response.status_code == 200:
            # Extraction des variables physiques pures
            pression = data["main"]["pressure"]  # en hPa
            temperature = data["main"]["temp"]    # en °C
            humidite = data["main"]["humidity"]  # en %
            vitesse_vent = data["wind"]["speed"]  # en m/s
            
            print(f"[+] Données physiques extraites en temps réel pour Magog :")
            print(f" * Température de l'air : {temperature:.2f}°C")
            print(f" * Pression Barométrique : {pression} hPa")
            print(f" * Humidité Relative    : {humidite} %")
            print(f" * Vélocité du Vent      : {vitesse_vent:.2f} m/s")
            print("-" * 80)
            print("[+] Constat atmosphérique : Données télémétriques brutes prêtes pour l'indexation RNIOG.")
        else:
            print(f"[-] Erreur de protocole API : Code {response.status_code}")
            print(f"[-] Message : {data.get('message', 'Inconnu')}")
            
    except Exception as e:
        print(f"[-] Échec de la connexion au flux de données : {str(e)}")
        
    print("================================================================================")

if __name__ == "__main__":
    run_weather_oracle()
