from rich import print
from rich.traceback import install

install()


class Caneta:
    def __init__(self, cor='white'):
        self.valor = cor
        self.tampado = False

    def destampar(self):
        self.tampada = True

    def tampar(self):
        self.tampada = False

    def escrever(self, msg):
        if not self.tampada:
            print('🚨 Caneta tampada, destampe para usar.')
        else:
            print(f'[{self.valor}]{msg}[/]')


c1 = Caneta('blue')
c2 = Caneta('red')
c3 = Caneta('yellow')


c1.destampar()
c1.escrever('Qualquer coisa em azul!')
c1.tampar()
c1.escrever('Não pode escrever')
