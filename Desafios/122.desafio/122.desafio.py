from rich import print
from rich.panel import Panel


class ControleRemoto:
    canal_min = 1
    canal_max = 6
    vol_min = 1
    vol_max = 5

    def __init__(self, canal=1, volume=2):
        self.canal = canal
        self.volume = volume
        self.ligado: bool = False

    def liga_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal == self.canal_max:
                self.canal = self.canal_min
            else:
                self.canal += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal == self.canal_min:
                self.canal = self.canal_max
            else:
                self.canal -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume < self.vol_max:
                self.volume += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume >= self.vol_min:
                self.volume -= 1

    def mostrar_tv(self):
        if not self.ligado:
            conteudo = '[red] 🚨 A TV está desligada[/]'.center(26)
        else:
            conteudo = 'CANAL =  '
            for canal in range(self.canal_min, self.canal_max + 1):
                if canal == self.canal:
                    conteudo += f'[black on yellow] {canal} [/]'
                else:
                    conteudo += f' {canal} '

            conteudo += '\nVOLUME = '
            for volume in range(self.vol_min, self.vol_max + 1):
                if volume <= self.volume:
                    conteudo += '[black on cyan] [/]'
                else:
                    conteudo += '[black on white] [/]'
        tv = Panel(conteudo, title='📺 TV', width=31)
        print(tv)


c = ControleRemoto()

while True:
    c.mostrar_tv()
    botao = input(f'Ligar @    < CH_{c.canal} >    - VOL_{c.volume} +\n')
    if botao == '0':
        break
    elif botao == '@':
        c.liga_desliga()
    elif botao == '+':
        c.volume_mais()
    elif botao == '-':
        c.volume_menos()
    elif botao == '<':
        c.canal_menos()
    elif botao == '>':
        c.canal_mais()
    else:
        print('Oção inválida!')
    print('\n' * 10)

print('FIM DO PROGRAMA')
