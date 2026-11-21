# Parte 2 de encapsulamento
from rich import inspect, print


class Avaliação:
    def __init__(self, nome, disciplina, nota='Sem nota'):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota  # Atributo protect (#)

    # Criando Atributo Validável
    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        if 0 < valor <= 10:
            self._nota = valor
        else:
            print('Nota inválida')


av1 = Avaliação('Pedro', 'Matématica')
av1.nota = 7.5

inspect(av1, private=True)
