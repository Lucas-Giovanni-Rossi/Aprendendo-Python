from abc import ABC, abstractmethod
from random import randint, randrange

from rich import print


class Personagem(ABC):  # Classe mãe
    def __init__(self, nome, vida):
        self.name = nome
        self.lifemax = vida
        self.life = vida
        self.hit = []

    def attack(self, alvo, dano=50):
        if self.life > 0 and alvo.life > 0:
            hit = self.hit[randrange(0, len(self.hit))]

            print(f'> [green]{self.name}[/] atacou [red]{alvo.name}[/] com [yellow]{hit}[/]', end='')
            alvo.getdamage(dano)
            print(f'> [red]{alvo.name}[/] tem {alvo.life} de vida.\n')

        else:
            print(f'> O ataque de [green]{self.name}[/] -> [red]{alvo.name}[/] não pode acontecer.')

    def getdamage(self, dano):
        fator = randint(0, dano)
        self.life = self.life - fator
        if self.life < 0:
            self.life = 0
        print(f' recebendo [red]{fator}[/] de dano!')

    @abstractmethod
    def heal(self):  # Classe obrigatoria
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.hit = ['Soco', 'Chute', 'Agarrão']

    def heal(self):
        fator = randint(0, int(self.lifemax * 0.03))
        self.life += fator
        if self.life > self.lifemax:
            self.life = self.lifemax

        print(f'> [green]{self.name}[/] limpou as feridas e curou [green]{fator}[/] pontos.')
        print(f'> Vida atual de {self.life}.\n')


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.hit = ['Bola de fogo', 'Bola de gelo', 'Avada kedava']

    def heal(self):
        fator = randint(0, int(self.lifemax * 0.1))
        self.life += fator
        if self.life > self.lifemax:
            self.life = self.lifemax

        print(f'> [green]{self.name}[/] acelerou tempo da ferida e curou [green]{fator}[/] pontos.')
        print(f'> Vida atual de {self.life}.\n')
