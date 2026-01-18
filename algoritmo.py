# ============================================
# ESTRUTURAS DE DADOS
# ============================================

class PlantingCandidate:
    """Local candidato ao plantio"""
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

class InterestPoint:
    """Ponto de interesse a ser coberto"""
    def __init__(self, id, x, y, weight, name=""):
        self.id = id
        self.x = x
        self.y = y
        self.weight = weight
        self.name = name

# ============================================
# FUNÇÕES AUXILIARES
# ============================================

import math

def distance(p1, p2):
    """Distância euclidiana entre dois pontos"""
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def build_coverage_matrix(plants, interests, radius):
    """
    Constrói matriz de cobertura
    
    coverage[p][i] = True se planta p cobre interesse i
    
    Complexidade: O(|P| × |I|)
    """
    coverage = {}
    for p in plants:
        coverage[p.id] = {}
        for i in interests:
            coverage[p.id][i.id] = distance(p, i) <= radius
    return coverage

def get_covered_interests(selected_plants, coverage_matrix, interests):
    """
    Retorna conjunto de interesses cobertos pelas plantas selecionadas
    
    Complexidade: O(|selected| × |I|)
    """
    covered = set()
    for plant in selected_plants:
        for interest in interests:
            if coverage_matrix[plant.id][interest.id]:
                covered.add(interest.id)
    return covered

def calculate_value(covered_interest_ids, interests):
    """
    Calcula valor total dos interesses cobertos
    
    Complexidade: O(|I|)
    """
    total = 0
    for interest in interests:
        if interest.id in covered_interest_ids:
            total += interest.weight
    return total

# ============================================
# ALGORITMO GULOSO
# ============================================

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

from itertools import combinations

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

# ============================================
# INSTÂNCIA DE EXEMPLO
# ============================================

def create_example_instance():
    """
    Cria uma instância pequena para demonstração
    
    Praça hipotética 50m × 50m
    """
    # Pontos de interesse
    interests = [
        InterestPoint(0, 10, 10, 2, "Entrada"),
        InterestPoint(1, 15, 30, 4, "Banco Norte"),
        InterestPoint(2, 35, 30, 4, "Banco Sul"),
        InterestPoint(3, 25, 40, 5, "Playground"),
        InterestPoint(4, 40, 15, 3, "Mesa"),
        InterestPoint(5, 20, 20, 3, "Bebedouro"),
    ]
    
    # Candidatos ao plantio
    plants = [
        PlantingCandidate(0, 12, 15),
        PlantingCandidate(1, 18, 25),
        PlantingCandidate(2, 30, 35),
        PlantingCandidate(3, 35, 20),
        PlantingCandidate(4, 25, 30),
        PlantingCandidate(5, 10, 35),
        PlantingCandidate(6, 40, 40),
        PlantingCandidate(7, 45, 10),
    ]
    
    return plants, interests

# ============================================
# MAIN - EXECUÇÃO
# ============================================

def main():
    print("="*60)
    print("OTIMIZAÇÃO DE PLANTIO DE ÁRVORES EM ESPAÇOS PÚBLICOS")
    print("="*60)
    
    # Parâmetros
    k = 6         # Número de árvores disponíveis
    radius = 6   # Raio de sombra em metros
    
    # Cria instância
    plants, interests = create_example_instance()
    
    print(f"\nParâmetros:")
    print(f"  - Candidatos ao plantio: {len(plants)}")
    print(f"  - Pontos de interesse: {len(interests)}")
    print(f"  - Árvores disponíveis: {k}")
    print(f"  - Raio de sombra: {radius}m")
    
    # Constrói matriz de cobertura
    print(f"\nConstruindo matriz de cobertura...")
    coverage_matrix = build_coverage_matrix(plants, interests, radius)
    
    # Mostra matriz (opcional)
    print(f"\nMatriz de Cobertura:")
    print(f"{'Planta':<8}", end="")
    for i in interests:
        print(f"{i.name:<12}", end="")
    print()
    for p in plants:
        print(f"P{p.id:<7}", end="")
        for i in interests:
            symbol = "✓" if coverage_matrix[p.id][i.id] else "-"
            print(f"{symbol:<12}", end="")
        print()
    
    # Executa Algoritmo Guloso
    print(f"\n{'='*60}")
    print("ALGORITMO GULOSO")
    print("="*60)
    
    import time
    start = time.time()
    greedy_solution = greedy_planting(plants, interests, k, coverage_matrix)
    greedy_time = time.time() - start
    
    greedy_covered = get_covered_interests(greedy_solution, coverage_matrix, interests)
    greedy_value = calculate_value(greedy_covered, interests)
    
    print(f"\nSolução Gulosa:")
    print(f"  Plantas selecionadas: {[p.id for p in greedy_solution]}")
    print(f"  Interesses cobertos: {sorted(greedy_covered)}")
    print(f"  Valor total: {greedy_value}")
    print(f"  Tempo: {greedy_time:.6f}s")
    
    # Executa Força Bruta
    print(f"\n{'='*60}")
    print("FORÇA BRUTA (SOLUÇÃO ÓTIMA)")
    print("="*60)
    
    start = time.time()
    bf_solution, bf_value = brute_force(plants, interests, k, coverage_matrix)
    bf_time = time.time() - start
    
    bf_covered = get_covered_interests(bf_solution, coverage_matrix, interests)
    
    print(f"\nSolução Ótima:")
    print(f"  Plantas selecionadas: {[p.id for p in bf_solution]}")
    print(f"  Interesses cobertos: {sorted(bf_covered)}")
    print(f"  Valor total: {bf_value}")
    print(f"  Tempo: {bf_time:.6f}s")
    
    # Comparação
    print(f"\n{'='*60}")
    print("COMPARAÇÃO")
    print("="*60)
    
    ratio = greedy_value / bf_value if bf_value > 0 else 0
    print(f"\nTaxa de Aproximação: {ratio:.2%}")
    print(f"Gap: {bf_value - greedy_value} ({(1-ratio)*100:.1f}%)")
    print(f"\nSpeedup: {bf_time/greedy_time:.2f}x mais rápido (Guloso)")
    
    # Detalhamento
    print(f"\n{'='*60}")
    print("DETALHAMENTO DA SOLUÇÃO GULOSA")
    print("="*60)
    for interest in interests:
        covered = "SIM" if interest.id in greedy_covered else "NÃO"
        print(f"{interest.name:<15} (peso={interest.weight}) → Coberto: {covered}")

if __name__ == "__main__":
    main()