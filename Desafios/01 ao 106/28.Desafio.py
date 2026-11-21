# Jogo de advinhação

from random import randint
from time import sleep

print('-=-' * 30)
print('Vou pensar em um número de 0 a 5! Tente advinhar....')
print('-=-' * 30)
sleep(3) # comando para pc esperar 4 segs

n = randint(0,5) # pensa em um numero

ad = int(input('Pensei! Advinhe qual número pensei: ')) # jogador tenta advinhar

print('-=-' * 30)
print('Vamos ver.....')
print('-=-' * 30)
sleep(2)

if ad == n:
    print('Muito bem! Você venceu!')
else:
    print('Perdeuuu Losseerr!')

print('Eu pensei no número : ',n)