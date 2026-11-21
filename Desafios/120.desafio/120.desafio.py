from rich import print
from rich.panel import Panel
from rich.traceback import install

install()


class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def add(self, *n):
        for i in n:
            self.favoritos.append(i)

    def ficha(self):
        sorted(self.favoritos)
        jogos = ' \n'.join(f'🎮 [blue]{i}[/]' for i in self.favoritos)
        conteudo = f'Nome real: [black on white]{self.nome}[/]\
                   \nJogos favoritos:\
                   \n{jogos}'

        print(Panel(conteudo, title=f'Jogador <[yellow]{self.nick}[/]>', width=40))


j1 = Gamer('Lucas Rossi', 'luketa')
j1.add('God of War', 'Fortnite')
j1.add('Until down')
j1.ficha()
