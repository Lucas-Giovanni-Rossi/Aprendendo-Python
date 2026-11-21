# Iniciando POO

# Declaração de Classe
class Gafanhoto:
    def __init__(self):  # Método Construtor
        # Atributos de Instância
        self.nome = ''
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'


# Declaração de objetos
p1 = Gafanhoto()  # Chamado a classe
p1.nome = 'Lucas'
p1.idade = 25
p1.aniversario()  # Chamando metodo

p2 = Gafanhoto()  # Chamado a classe
p2.nome = 'Amanda'
p2.idade = 27

print(p1.mensagem())  # Chamando metodo
print(p2.mensagem())
