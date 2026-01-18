# ============================================
# ALGORITMO GULOSO
# ============================================

from itertools import combinations
from utils import get_covered_interests, calculate_value


def greedy_planting(plants, interests, k, coverage_matrix):
    """
    Algoritmo Guloso para Maximum Coverage
    
    Estratégia: A cada iteração, escolhe a planta que
    cobre o maior valor de interesses ainda não cobertos
    
    Complexidade: O(k × |P| × |I|)
    
    Pseudocódigo:
    1. selected ← ∅
    2. covered ← ∅
    3. Para i = 1 até k:
    4.   melhor ← planta com maior ganho marginal
    5.   selected ← selected ∪ {melhor}
    6.   covered ← covered ∪ cobertura(melhor)
    7. Retornar selected
    """
    selected = []
    covered = set()
    
    for iteration in range(k):
        best_plant = None
        best_gain = -1
        
        # Testa cada planta não selecionada
        for plant in plants:
            if plant not in selected:
                # Calcula ganho marginal
                new_covered = set()
                for interest in interests:
                    if coverage_matrix[plant.id][interest.id]:
                        new_covered.add(interest.id)
                
                # Conta apenas interesses NOVOS
                marginal_covered = new_covered - covered
                gain = sum(i.weight for i in interests 
                          if i.id in marginal_covered)
                
                if gain > best_gain:
                    best_gain = gain
                    best_plant = plant
        
        # Se encontrou planta com ganho positivo
        if best_plant and best_gain > 0:
            selected.append(best_plant)
            # Atualiza interesses cobertos
            for interest in interests:
                if coverage_matrix[best_plant.id][interest.id]:
                    covered.add(interest.id)
        else:
            # Nenhuma planta adiciona valor, pode parar
            break
    
    return selected


# ============================================
# FORÇA BRUTA (SOLUÇÃO ÓTIMA)
# ============================================

def brute_force(plants, interests, k, coverage_matrix):
    """
    Testa todas as combinações de k plantas
    
    Complexidade: O(C(|P|,k) × k × |I|)
    onde C(|P|,k) = |P|! / (k! × (|P|-k)!)
    
    Exemplos:
    - |P|=10, k=3 → 120 combinações
    - |P|=15, k=4 → 1365 combinações
    - |P|=20, k=5 → 15504 combinações
    
    USAR APENAS para |P| ≤ 15
    """
    best_value = 0
    best_selection = None
    
    # Testa todas as combinações de k plantas
    for selection in combinations(plants, k):
        # Calcula valor desta seleção
        covered = get_covered_interests(selection, coverage_matrix, interests)
        value = calculate_value(covered, interests)
        
        if value > best_value:
            best_value = value
            best_selection = selection
    
    return list(best_selection), best_value
