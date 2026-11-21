from locale import LC_ALL, currency, setlocale

from rich import print
from rich.panel import Panel
from rich.traceback import install

install()
setlocale(LC_ALL, '')


class Churrasco:
    consumo_1 = 0.4  # em kilos
    preço_kg = 82.40
    custo = preço_kg * consumo_1

    def __init__(self, titulo, qtd):
        self.titulo = titulo
        self.qtd = qtd

    def analisar(self):
        total_kg = self.qtd * self.consumo_1
        total_custo = total_kg * self.preço_kg

        conteudo = f'Analisando [green]{self.titulo}[/] com [blue]{self.qtd} convidados[/].\
                  \nConsiderando consumo médio de [yellow]{self.consumo_1}Kg[/] e cada Kg custa [red]{currency(self.preço_kg, grouping=True)}[/].\
                  \nRecomendo comprar [blue]{total_kg:.1f}Kg[/] de carne.\
                  \nCusto total de [green]{currency(total_custo, grouping=True)}[/].\
                  \nCada pessoa pagará [yellow]{currency(self.custo, grouping=True)}[/] para participar.'

        print(Panel(conteudo, title=self.titulo, width=70))


c1 = Churrasco('Churras Domingo', 51)
c1.analisar()
