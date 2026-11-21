# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep


# Funções
def sorteia():
    qtd = randint(1, 20)
    print(f'Sorteando {qtd} valores entre 0 e 100...')
    for i in range(0, qtd):
        numeros.append(randint(0, 100))
        print(numeros[i], end=' → ', flush=True)
        sleep(0.25)
    print('Fim!')


def somapar():
    s = 0
    for i in enumerate(numeros):
        if i[1] % 2 == 0:
            s += i[1]
    tam = f'Dentre os {len(numeros)} valores sorteados a soma dos números pares é: {s}'
    print(tam)
    print('~' * len(tam))


# Programa Principal
numeros = []

sorteia()
somapar()
