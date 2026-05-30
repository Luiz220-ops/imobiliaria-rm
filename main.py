import csv

class Imovel:
    """Classe base que representa um imóvel genérico."""
    def __init__(self, tipo, valor_base):
        self.tipo = tipo
        self.valor_base = valor_base

    def calcular_aluguel(self):
        return self.valor_base
