import itertools
import pandas as pd

def evaluate_implication(A, B):
    # Règle brute : A -> B est équivalent à (not A) or B
    return not A or B

def evaluate_equivalence(A, B):
    return A == B

def run_logic_engine():
    print("================================================================================")
    print("🎛️ ANALYSEUR LOGIQUE SYSTEMIQUE : TABLES DE VÉRITÉ BRUTES")
    print("================================================================================")
    
    # Variables propositionnelles (2^3 = 8 combinaisons)
    variables = ['A', 'B', 'C']
    combinations = list(itertools.product([True, False], repeat=len(variables)))
    
    rows = []
    
    for A, B, C in combinations:
        # Évaluation de propositions complexes distinctes
        # P1: Modus Ponens prémisse -> ((A -> B) and A)
        p1_premise = evaluate_implication(A, B) and A
        # P1_Full: ((A -> B) and A) -> B
        p1_full = evaluate_implication(p1_premise, B)
        
        # P2: Contradiction classique (A and not A)
        p2_contradiction = A and not A
        
        # P3: Expression contingente standard: (A or B) and not C
        p3_contingence = (A or B) and not C
        
        rows.append({
            'A': int(A),
            'B': int(B),
            'C': int(C),
            'A->B': int(evaluate_implication(A, B)),
            'Modus Ponens': int(p1_full),
            'Contradiction': int(p2_contradiction),
            'Contingence': int(p3_contingence)
        })
    
    # Transformation en DataFrame pour un affichage tabulaire strict
    df = pd.DataFrame(rows)
    
    print("[+] Affichage de la matrice logique (0 = Faux, 1 = Vrai) :")
    print("-" * 80)
    print(df.to_string(index=False))
    print("-" * 80)
    
    # Analyse de la nature des expressions
    print("[+] Analyse structurelle des colonnes :")
    for col in ['Modus Ponens', 'Contradiction', 'Contingence']:
        unique_values = df[col].unique()
        if len(unique_values) == 1 and unique_values[0] == 1:
            status = "TAUTOLOGIE (Vérité absolue / Invariante)"
        elif len(unique_values) == 1 and unique_values[0] == 0:
            status = "CONTRADICTION (Absurdité / Impossible)"
        else:
            status = "CONTINGENCE (Dépend des conditions d'entrée)"
        print(f" * L'expression [{col:<13}] est une : {status}")
        
    print("================================================================================")

if __name__ == "__main__":
    run_logic_engine()
