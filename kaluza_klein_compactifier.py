import numpy as np
import pandas as pd

def simulate_kaluza_klein():
    print("================================================================================")
    print("🌀 COMPACTIFICATEUR DE KALUZA-KLEIN : SPECTRE MOMENTUM & WINDING (RAW)")
    print("================================================================================")
    
    alpha_prime = 1.0
    R_values = [2.0, 0.5] 
    
    states = [
        (1, 0, "Pure Momentum"),
        (0, 1, "Pure Winding"),
        (1, 1, "Mixte (1,1)"),
        (2, 0, "Momentum double")
    ]
    
    for R in R_values:
        print(f"\n[+] Analyse du spectre pour le Rayon Compact R = {R} (α' = {alpha_prime})")
        print("-" * 85)
        print(f"{'ÉTAT (m, n)':<15} | {'TYPE D’EXCITATION':<18} | {'M² MOMENTUM':<13} | {'M² WINDING':<12} | {'M² TOTALE'}")
        print("-" * 85)
        
        for m, n, label in states:
            m2_momentum = (m ** 2) / (R ** 2)
            m2_winding = (n ** 2) * (R ** 2) / (alpha_prime ** 2)
            m2_total = m2_momentum + m2_winding
            
            state_str = f"({m}, {n})"
            print(f"{state_str:<15} | {label:<18} | {m2_momentum:<13.4f} | {m2_winding:<12.4f} | {m2_total:.4f}")
            
        print("-" * 85)
        
    print("[+] Observation physique : Le spectre de R = 2.0 est l'exact miroir de R = 0.5.")
    print("[+] Les modes d'impulsion et d'enroulement se sont inversés de manière stricte.")
    print("================================================================================")

if __name__ == "__main__":
    simulate_kaluza_klein()
