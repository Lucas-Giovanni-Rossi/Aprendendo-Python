from locale import LC_MONETARY, currency, setlocale

from rich import print
from rich.panel import Panel
from rich.traceback import install

install()
setlocale(LC_MONETARY, '')


class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def etiqueta(self):
        preço_local = f' {currency(self.preço, grouping=True)} '
        conteudo = f'[yellow]{self.nome.center(32)}[/] ' + '-' * 32 + f' [green]{preço_local.center(32, ".")}[/] ' + '-' * 32

        print(
            Panel(
                conteudo,
                title='Produto',
                style='white',
                width=36,
            )
        )


p1 = Produto('Lápis', 1.50)
p2 = Produto('Notebook', 2_999.99)
p1.etiqueta()
p2.etiqueta()
