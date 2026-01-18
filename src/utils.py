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
