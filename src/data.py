# ============================================
# INSTÂNCIA DE EXEMPLO
# ============================================

from models import PlantingCandidate, InterestPoint


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
