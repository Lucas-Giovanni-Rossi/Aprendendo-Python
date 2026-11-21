# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# Jogo de advinhação

from random import randint
from time import sleep

print('-=-' * 30)
print('Vou pensar em um número de 0 a 10! Tente advinhar....')
print('-=-' * 30)
sleep(2)  # comando para pc esperar 3 segs

n = randint(0, 10)  # pensa em um numero

ad = int(input('Pensei! Advinhe qual número pensei: '))  # jogador tenta advinhar

print('-=-' * 30)
print('Vamos ver.....')
print('-=-' * 30, '\n')
sleep(1)  # comando para pc esperar 2 segs

contador = 1
while ad != n:
    if ad < n:
        ad = int(input('Mais... tente outro palpite: '))
    else:
        ad = int(input('Menos ! tente outro palpite: '))
    contador += 1


print('\nMuito bem!\nCom {} tentativas você acertou!'.format(contador))

print('Eu pensei no número: {}.'.format(n))
