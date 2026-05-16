import numpy as np

def run_spectral_analysis():
    print("================================================================================")
    print("⚡ ANALYSEUR SPECTRAL DE FOURIER BRUT (RNIOG ULTRA-CORE) - NO SMOOTHING")
    print("================================================================================")
    
    # Configuration d'échantillonnage pure (Fréquence en Hz)
    fe = 100.0  # Fréquence d'échantillonnage à 100 Hz
    duree = 10.0  # Fenêtre temporelle brute de 10 secondes
    t = np.arange(0, duree, 1/fe)
    N = len(t)
    
    print(f"[+] Vecteur temporel configuré : N = {N} points d'acquisition brute.")
    
    # Génération d'un signal composite avec les harmoniques réelles de Schumann (7.83 Hz et 14.1 Hz)
    # Plus un bruit blanc Gaussien injecté sans aucun filtrage
    signal_fondamental = np.sin(2 * np.pi * 7.83 * t)
    harmonique_deux = 0.5 * np.sin(2 * np.pi * 14.1 * t)
    bruit_brut = np.random.normal(0, 0.2, N)
    
    signal_raw = signal_fondamental + harmonique_deux + bruit_brut
    
    # Application de la FFT sans aucun fenêtrage artificiel (Pas de Hanning/Hamming)
    # On veut la réponse spectrale brute de l'espace échantillonné
    fft_valeurs = np.fft.fft(signal_raw)
    frequences = np.fft.fftfreq(N, 1/fe)
    
    # Conservation unique de la moitié positive du spectre
    moitie_spectre = N // 2
    frequences_pos = frequences[:moitie_spectre]
    amplitudes_pos = (2.0 / N) * np.abs(fft_valeurs[:moitie_spectre])
    
    # Extraction des pics d'amplitude dominants
    indices_pics = np.argsort(amplitudes_pos)[::-1][:3]
    
    print("-" * 80)
    print(f"{'RANG':<10} | {'FRÉQUENCE EXTRAITE (Hz)':<25} | {'AMPLITUDE SPECTRALE BRUTE'}")
    print("-" * 80)
    
    for i, idx in enumerate(indices_pics):
        print(f"#{i+1:<8} | {frequences_pos[idx]:<25.4f} | {amplitudes_pos[idx]:.6f}")
        
    print("-" * 80)
    print("[+] Constat spectral : La transformée de Fourier restitue les modes propres du signal.")
    print("[+] Aucune fonction de lissage n'a altéré la distribution d'énergie du bruit blanc.")
    print("================================================================================")

if __name__ == "__main__":
    run_spectral_analysis()
