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

class Orcamento:
    """Classe responsável por consolidar os valores e gerar o relatório/CSV."""
    def __init__(self, imovel, parcelas_contrato):
        self.imovel = imovel
        self.valor_contrato_total = 2000.00
        # Garante que o parcelamento esteja entre 1 e 5 vezes
        self.parcelas_contrato = max(1, min(5, parcelas_contrato))

    def exibir_resumo(self):
        aluguel_mensal = self.imovel.calcular_aluguel()
        valor_parcela = self.valor_contrato_total / self.parcelas_contrato
        
        print("\n" + "="*40)
        print(f"     ORÇAMENTO IMOBILIÁRIA R.M")
        print("="*40)
        print(f"Tipo de Imóvel: {self.imovel.tipo}")
        print(f"Valor do Aluguel Mensal: R$ {aluguel_mensal:.2f}")
        print(f"Taxa de Contrato Total: R$ {self.valor_contrato_total:.2f}")
        print(f"Parcelamento da Taxa: {self.parcelas_contrato}x de R$ {valor_parcela:.2f}")
        print("-"*40)
        print(f"Total no Primeiro Mês: R$ {(aluguel_mensal + valor_parcela):.2f}")
        print("="*40)

def gerar_csv(self, nome_arquivo="orcamento_12_meses.csv"):
        aluguel_mensal = self.imovel.calcular_aluguel()
        valor_parcela = self.valor_contrato_total / self.parcelas_contrato

        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Cabeçalho do CSV
            writer.writerow(["Mês", "Aluguel Mensal (R$)", "Parcela Contrato (R$)", "Total Mensal (R$)"])
            
            # Cronograma de 12 parcelas (meses)
            for mes in range(1, 13):
                p_contrato = valor_parcela if mes <= self.parcelas_contrato else 0.0
                total_mensal = aluguel_mensal + p_contrato
                writer.writerow([mes, f"{aluguel_mensal:.2f}", f"{p_contrato:.2f}", f"{total_mensal:.2f}"])
        
        print(f"\n[Sucesso] Arquivo '{nome_arquivo}' gerado com o cronograma de 12 meses!")
