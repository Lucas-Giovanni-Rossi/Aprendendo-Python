# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

"""Não faz sentido esse exercicio pq o python ta tem essa função com a max()"""

from time import sleep


def maior(*num):
    cont = maior = 0

    print('-=' * 30)
    print('Analisando valores...')

    for valor in num:
        print(f'{valor}', end=', ', flush=True)
        sleep(0.25)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(1, 3, 5, 7, 9, 11, 13)
maior(2, 4, 6, 8, 10, 12, 14)
maior(10, -5, 23, 0, 8, 99, -42)
maior(6)
maior()
