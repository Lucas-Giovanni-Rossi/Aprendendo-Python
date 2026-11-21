from rich import inspect, print
from rich.traceback import install

install()


class Funcionario:
    # Atributos de classe:
    empresa = 'Microsoft'

    def __init__(self, nome='<desconhecido>', setor='<desconhecido>', cargo='<desconhecido>'):
        # Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:  # Essa função retorna uma string
        print(
            f'🤝 Olá, meu nome é [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor}\
            \n   Prazer em conhecer vocês e fazer parte da {Funcionario.empresa}.'
        )


c1 = Funcionario('Pedro', 'TI', 'Programador')
c1.apresentacao()
inspect(c1, methods=True)

c2 = Funcionario('Lucas', 'TI', 'Desenvolvedor')
c2.apresentacao()
