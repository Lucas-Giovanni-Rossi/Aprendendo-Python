# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
from moeda import aumentar, diminuir, dobro, metade

preco = int(input('Digite um preço: R$'))
taxa = int(input('Qual a taxa? '))

print(
    f'A metade é {metade(preco, True)}.\
    \nO dobro é {dobro(preco, True)}.\
    \nAumentando {taxa}% temos {aumentar(preco, taxa, True)}.\
    \nDiminuindo {taxa}% temos {diminuir(preco, taxa, True)}.'
)
