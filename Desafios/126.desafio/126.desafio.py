from abc import ABC
from locale import LC_ALL, currency, setlocale

from rich import print
from rich.panel import Panel

setlocale(LC_ALL, '')  # Usando para definir padrões locais como a moeda


class Funcionario(ABC):
    sal_minimo = 1_612
    inss = 0.075

    def __init__(self, nome, sal_bruto):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.sal_liquido = sal_bruto - (sal_bruto * self.inss)

    def analisar_sal(self):
        conteudo = f'O salário de [blue]{self.nome}[/] [yellow]({type(self).__name__})[/] é de [green]{currency(self.sal_liquido)}[/]\
 e corresponde a [red]{self.sal_liquido / self.sal_minimo:.2f} salários minimos.[/]'
        return print(Panel(conteudo, width=55, title='Análise de Salário'))


class Horista(Funcionario):
    def __init__(self, nome, horas, horas_trabalho):
        super().__init__(nome, sal_bruto=horas * horas_trabalho)


class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto)


h1 = Horista('Lucas', 200, 20)
h1.analisar_sal()
m1 = Mensalista('Jorge', 9500)
m1.analisar_sal()
