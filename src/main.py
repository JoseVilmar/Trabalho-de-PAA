# ============================================
# MAIN - EXECUÇÃO
# ============================================

import time
from data import create_example_instance
from utils import build_coverage_matrix, get_covered_interests, calculate_value
from algorithms import greedy_planting, brute_force


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
