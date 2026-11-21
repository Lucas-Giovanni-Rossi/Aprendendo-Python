from rich import inspect, print


class Pessoa:  # Classe Mãe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1


class Prof(Pessoa):
    def __init__(self, nome, idade, especialista, nivel):
        super().__init__(nome, idade)
        self.especialista = especialista
        self.nivel = nivel

    def dar_aula(self):
        print(f'O professor {self.nome} entrou na aula.')


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'{self.nome} acabou de finalizar a matricula')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'{self.nome} bateu o ponto.')


a1 = Aluno('Lucas', 25, 'Economia', 'T01')
p1 = Prof('Samuel', 35, 'Relaçõe Internacionais', 'Mestre')

inspect(a1, methods=True)
print()
inspect(p1, methods=True)
