# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = tuple(randint(0, 100) for _ in range(5))  # muito legal, criar uma tupla usando randint e repetição com for sem usar variavel.

print('Valores sorteados foram: ', numeros)
print('O maior valor é: ', max(numeros))  # max de maximo valor
print('O menor valor é: ', min(numeros))  # min de minimo valor
