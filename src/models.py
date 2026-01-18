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
