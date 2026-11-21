# Faça um programa que leia um número qualquer e mostre o seu fatorial
# (bonus use while, for e biblioteca math).

from math import factorial

print('=' * 15, 'Descubra o Fatorial de um número', '=' * 15)

while True:  # enquanto não acionar o break o loop continua.
    numero = int(input('Digite um número: '))
    print(f'{numero}! = ', end='')

    for sequencia in range(numero, 0, -1):
        print(sequencia, end='')
        print(' * ' if sequencia > 1 else ' = ', end='')

    print(f'{factorial(numero):,}')  # ajustar formatação de número grandes com f'{:,}'.

    continuar = input('Deseja calcular outro fatorial? [S/N] ').strip().upper()

    # Validação
    while continuar == '' or continuar[0] not in 'SN':
        continuar = input('Opção inválida! Deseja calcular outro fatorial? [S/N] ').strip().upper()

    print('-=' * 30, '\n')

    if continuar[0] == 'N':
        break

print('Finalizado! Volte sempre!')
