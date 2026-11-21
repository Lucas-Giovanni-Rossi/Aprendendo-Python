# Iniciando POO parte 2

# Declaração de Classe
class Gafanhoto:
    """Classe:
    Cria gafanhotos com nome e idade.
    Para executar use:
    obj = Gafanhoto(nome,idade)"""

    def __init__(self, nome='<desconhecido>', idade=0):  # Método Construtor com parâmetro opcional
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self):  # Dunder method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'


# Declaração de objetos
p1 = Gafanhoto('Lucas', 21)  # Chamado a classe
p1.aniversario()  # Chamando metodo

p2 = Gafanhoto('Amanda', 27)

p3 = Gafanhoto()  # Sem parametro

print(p1)
print(p1.__dict__)  # Atributo, mostra como dicionario
print(p1.__getstate__())  # Metodo, posso personalizar dentro da classe
