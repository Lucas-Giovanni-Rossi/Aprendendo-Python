from abc import ABC, abstractmethod
from locale import LC_ALL, currency, setlocale

from rich import print
from rich.table import Table

setlocale(LC_ALL, '')  # Usando para definir padrões locais como a moeda


class Transporte(ABC):
    fator = int

    @abstractmethod
    def __init__(self, distancia, frete=fator):
        self.distancia = distancia
        self.frete = frete

    @abstractmethod
    def cal_frete(self):
        pass


class Moto(Transporte):
    # Atributos de Classe
    fator = 0.50

    def __init__(self, distancia, frete=fator):
        super().__init__(distancia, frete)

    def cal_frete(self):
        valor = currency(self.distancia * self.frete)
        return valor


class Caminhão(Transporte):
    fator = 1.20

    def __init__(self, distancia, frete=fator):
        super().__init__(distancia, frete)

    def cal_frete(self):
        if self.distancia < 50:
            valor = 'Distância mínima permitida de 50km'
        else:
            valor = currency(self.distancia * self.frete)
        return valor


class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia, frete=fator):
        super().__init__(distancia, frete)

    def cal_frete(self):
        if self.distancia > 10:
            valor = 'Distância máxima permitida de 10km'
        else:
            valor = currency(self.distancia * self.frete)
        return valor


# ----- PROGRAMA PRINCIPAL ----- #
dist = int(input('Qual distância deseja calcular o frete? [Km] '))
viagem = [Moto(dist), Caminhão(dist), Drone(dist)]

tabela = Table(title='Tabela de Fretes', style='bold blue')
tabela.add_column('Distância', justify='center')
tabela.add_column('Opções')
tabela.add_column('Frete')

for item in viagem:
    tabela.add_row(f'{dist}Km', type(item).__name__, item.cal_frete())

print('\n', tabela, '\n')
