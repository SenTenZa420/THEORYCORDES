import numpy as np
import pandas as pd

def compute_string_spectrum():
    print("================================================================================")
    print("🎻 EXTRACTEUR QUANTIQUE : SPECTRE DE VIRASORO & DIMENSIONS CRITIQUES (RAW)")
    print("================================================================================")
    
    # Paramètres fondamentaux (Échelle de Planck / Regge slope)
    alpha_prime = 1.0  # Fixé à l'unité pour l'analyse pure
    
    # Dimensions à tester pour l'anomalie
    dimensions_to_test = [4, 10, 11, 26, 60]
    
    print(f"[+] Analyse de l'anomalie conforme quantique (Régularisation Zêta: -1/12)")
    print("-" * 80)
    print(f"{'DIMENSION D':<12} | {'INTERCEPT a':<15} | {'ANOMALIE DE WEYL':<20} | {'STATUS'}")
    print("-" * 80)
    
    for D in dimensions_to_test:
        # Énergie du point zéro pour D champs scalaires transverses (D - 2)
        # Chaque coordonnée transverse contribue à hauteur de -1/24 à l'énergie du vide
        intercept = (D - 2) * (1.0 / 24.0)
        
        # L'anomalie s'annule uniquement si l'intercept physique est exactement égal à 1
        anomalie = 1.0 - intercept
        
        if abs(anomalie) < 1e-9:
            status = "⚡ CRITIQUE (ZÉRO ANOMALIE)"
        else:
            status = "ASYMÉTRIQUE / GHOSTS"
            
        print(f"{D:<12} | {intercept:<15.4f} | {anomalie:<20.4f} | {status}")
        
    print("-" * 80)
    print("[+] Génération des premiers modes vibratoires (Corde Fermée Sans Masse)")
    print("-" * 80)
    print(f"{'NIVEAU EXCIT.':<14} | {'SPIN EXCIT.':<12} | {'MASSE CARRÉE (M²)':<20} | {'PARTICULE ÉMERGENTE'}")
    print("-" * 80)
    
    # Mode de vide (Tachyone dans le modèle bosonique critique D=26)
    a_critical = 1.0
    m2_vacuum = (4.0 / alpha_prime) * (0 - a_critical)
    print(f"{0:<14} | {0:<12} | {m2_vacuum:<20.1f} | Tachyone (Instabilité du vide)")
    
    # Premier niveau excité (Modes transverses combinés gauche/droite)
    # N = \tilde{N} = 1
    m2_excited_1 = (4.0 / alpha_prime) * (1 - a_critical)
    print(f"{1:<14} | {'2 (Symétrique)':<12} | {m2_excited_1:<20.1f} | Graviton (G_μν)")
    print(f"{1:<14} | {'1 (Antisym.)':<12} | {m2_excited_1:<20.1f} | Kalb-Ramond (B_μν)")
    print(f"{1:<14} | {'0 (Scalaire)':<12} | {m2_excited_1:<20.1f} | Dilaton (Φ)")
    
    print("================================================================================")

if __name__ == "__main__":
    compute_string_spectrum()
