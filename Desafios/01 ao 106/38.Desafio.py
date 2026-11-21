# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 == n2:
    print('Os 2 números são IGUAIS.')
elif n1 > n2:
    print('O PRIMEIRO número é maior.')
else:
    print('O SEGUNDO é maior.')

 