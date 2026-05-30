import csv

class Imovel:
    """Classe base que representa um imóvel genérico."""
    def __init__(self, tipo, valor_base):
        self.tipo = tipo
        self.valor_base = valor_base

    def calcular_aluguel(self):
        return self.valor_base
        
class Apartamento(Imovel):
    """Subclasse para gerenciar as regras específicas de Apartamentos."""
    def __init__(self, quartos, tem_garagem, tem_criancas):
        super().__init__("Apartamento", 700.00)  # Valor base para 1 quarto
        self.quartos = quartos
        self.tem_garagem = tem_garagem
        self.tem_criancas = tem_criancas

    def calcular_aluguel(self):
        valor = self.valor_base
        # Adicional por quarto extra
        if self.quartos == 2:
            valor += 200.00
        # Adicional de vaga de garagem
        if self.tem_garagem:
            valor += 300.00
        # Desconto de 5% se não houver crianças
        if not self.tem_criancas:
            valor *= 0.95
        return valor
        
class Casa(Imovel):
    """Subclasse para gerenciar as regras específicas de Casas."""
    def __init__(self, quartos, tem_garagem):
        super().__init__("Casa", 900.00)  # Valor base para 1 quarto
        self.quartos = quartos
        self.tem_garagem = tem_garagem

    def calcular_aluguel(self):
        valor = self.valor_base
        # Adicional por quarto extra
        if self.quartos == 2:
            valor += 250.00
        # Adicional de vaga de garagem
        if self.tem_garagem:
            valor += 300.00
        return valor

class Estudio(Imovel):
    """Subclasse para gerenciar as regras específicas de Estúdios."""
    def __init__(self, vagas_estacionamento):
        super().__init__("Estúdio", 1200.00)
        self.vagas = vagas_estacionamento

    def calcular_aluguel(self):
        valor = self.valor_base
        # Regra de vagas para Estúdio
        if self.vagas > 0:
            if self.vagas <= 2:
                valor += 250.00
            else:
                valor += 250.00 + ((self.vagas - 2) * 60.00)
        return valor
