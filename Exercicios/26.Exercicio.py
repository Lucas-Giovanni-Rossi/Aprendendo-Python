from rich import inspect, print
from rich.panel import Panel
from rich.table import Table

caixa = Panel('Esse aqui é um painel de exemplo', title='Título', style='red', width=40)

print(caixa)

tabela = Table(title='Tabela de preço')


tabela.add_column('Nome')
tabela.add_column('Preço')
tabela.add_row('Lápis', 'R$1,50')
tabela.add_row('Boracha', 'R$2,50')

print(tabela)

inspect(tabela)
