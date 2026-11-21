from abc import ABC, abstractmethod

from rich import print
from rich.panel import Panel


class BebidaQuente(ABC):  # CLASSE MÃE = ABSTRATA
    def __init__(self, tipo='', cor='white'):
        self.tipo = tipo
        self.cor = cor

    def preparar(self):
        conteudo = self.ferver_agua() + self.misturar() + self.servir()
        painel = Panel(conteudo, title=f'Preparando {self.tipo}', border_style=f'{self.cor}', width=60, padding=(1))
        return print(painel)

    def ferver_agua(self):
        inicio = ' Iniciando Processo '.center(56, '-')
        passo1 = '\n\n1. Fervendo água há 100 graus Celsius.\n'
        return inicio + passo1

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class BlackCoffe(BebidaQuente):
    def __init__(self, tipo='Café Puro', cor='#8B4513'):
        super().__init__(tipo, cor)

    def misturar(self):
        passo2 = '2. Passando água pressurizada pelo pó de café moído.\n'
        return passo2

    def servir(self):
        passo3 = '3. Servindo em xícara pequena.\n\n'
        fim = ' Bebida Pronta '.center(56, '-')
        return passo3 + fim


class Tea(BebidaQuente):
    def __init__(self, tipo='Chá', cor='#6B8E23'):
        super().__init__(tipo, cor)

    def misturar(self):
        passo2 = '2. Megulhando o sachê de ervas na água.\n'
        return passo2

    def servir(self):
        passo3 = '3. Servindo em caneca de porcelana com limão.\n\n'
        fim = ' Bebida Pronta '.center(56, '-')
        return passo3 + fim


class Latte(BebidaQuente):
    def __init__(self, tipo='Café c/ Leite', cor='#FFFDD0'):
        super().__init__(tipo, cor)

    def misturar(self):
        passo2 = '2. Passando vapor pressurizado pelo bico do leite..\n'
        return passo2

    def servir(self):
        passo3 = '3. Servindo na caneca grande, já com café\n\n'
        fim = ' Bebida Pronta '.center(56, '-')
        return passo3 + fim


# ----- PROGRAMA PRINCIPAL ------ #

b1 = BlackCoffe()
b1.preparar()

b2 = Tea()
b2.preparar()

b3 = Latte()
b3.preparar()
