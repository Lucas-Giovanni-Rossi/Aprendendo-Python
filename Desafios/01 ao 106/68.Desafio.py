#  Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

print(f'{"-=" * 40}\n{"VAMOS JOGAR PAR OU ÍMPAR":^80}\n{"-=" * 40}')


cont = 0

while True:  # joga até perde
    computador = randint(0, 10)
    pessoa = int(input('Digite um valor: '))

    # Não quebra se colocar opção invalida
    while True:
        p1 = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
        if p1 == 'P':
            c1 = 'I'
            break
        elif p1 == 'I':
            c1 = 'P'
            break

    soma = computador + pessoa
    print(f'Computador jogou {computador} e você jogou {pessoa}. Total de {soma}', end=' → ')

    # Logica de ganho ou perca
    if soma % 2 == 0:
        if p1 == 'P':
            print('DEU PAR\nO jogador GANHOU!!')
            cont += 1
        elif c1 == 'P':
            print('DEU PAR\nVocê PERDEU!! ')
            break
    if soma % 2 == 1:
        if p1 == 'I':
            print('DEU ÍMPAR\nO jogador GANHOU!!')
            cont += 1
        elif c1 == 'I':
            print('DEU ÍMPAR\nVocê PERDEU!! ')
            break

    print('-=' * 40)
    print('VAMO JOGAR NOVAMENTE!...')
    sleep(2)
sleep(2)
print('-=' * 40)
print(f'\nVocê ganhou {cont} vezes(s).\n\n{"~" * 33}{"  GAME OVER!  "}{"~" * 33}')
