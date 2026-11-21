# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
from moeda import aumentar, diminuir, dobro, metade

preco = input('Digite um preço: R$')
taxa = input('Qual a taxa? ')

print(
    f'A metade é R${metade(preco):.2f}.\n'
    f'O dobro é R${dobro(preco):.2f}.\n'
    f'Aumentando {taxa}% temos R${aumentar(preco, taxa):.2f}.\n'
    f'Diminuindo {taxa}% temos R${diminuir(preco, taxa):.2f},'
)
