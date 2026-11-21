# Jogar Jokenpô

from random import randint
from time import sleep

print('-=-' * 20, ' Jokenpô ', '-=-' * 20)

print("""
Vamos jogar !
Escolha uma opção:
      [1] PEDRA
      [2] PAPEL
      [3] TESOURA""")
player = int(input('Qual a sua jogada? '))
pc = randint(1, 3)

if player == 1:
    player = 'PEDRA'
elif player == 2:
    player = 'PAPEL'
elif player == 3:
    player = 'TESOURA'
else:
    player = 'uma opção invalida'

if pc == 1:
    pc = 'PEDRA'
elif pc == 2:
    pc = 'PAPEL'
elif pc == 3:
    pc = 'TESOURA'

print('\nJO....')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ!\n')
sleep(0.5)

print('-=-' * 30)
if (
    player == 'PEDRA'
    and pc == 'PEDRA'
    or player == 'PAPEL'
    and pc == 'PAPEL'
    or player == 'TESOURA'
    and pc == 'TESOURA'
):
    print('Empate!!')
elif (
    player == 'PEDRA'
    and pc == 'PAPEL'
    or player == 'PAPEL'
    and pc == 'TESOURA'
    or player == 'TESOURA'
    and pc == 'PEDRA'
):
    print('O JOGADOR PERDEU!!')
elif (
    player == 'PEDRA'
    and pc == 'TESOURA'
    or player == 'PAPEL'
    and pc == 'PEDRA'
    or player == 'TESOURA'
    and pc == 'PAPEL'
):
    print('O JOGADOR GANHOU!!!')
else:
    pc = 'nada! Não sou besta.'
print('-=-' * 30)
print('*Você escolheu {} e eu escolhi {}.\n'.format(player, pc))
