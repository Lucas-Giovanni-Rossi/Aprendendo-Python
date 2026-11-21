# Parte 2 de encapsulamento
from rich import inspect, print


class Avaliação:
    def __init__(self, nome, disciplina, nota='Sem nota'):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota  # Atributo protect (#)

    def get_nota(self):
        return self._nota

    def set_nota(self, valor):
        if 0 < valor <= 10:
            self._nota = valor
        else:
            print('Nota inválida')


av1 = Avaliação('Pedro', 'Matématica')
av1.set_nota(9)
inspect(av1, private=True)
