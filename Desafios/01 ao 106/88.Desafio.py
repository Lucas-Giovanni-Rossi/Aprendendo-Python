# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

temp = []
palpite = []

print('-' * 60)
print(f'{"JOGO DA MEGA SENA":^60}')
print('-' * 60)
print()

qtd = int(input('Quanto jogos deseja gerar? '))

for sorteio in range(1, qtd * 6 + 1):
    while True:
        jogo = randint(1, 60)
        if jogo not in temp:
            break
    temp.append(jogo)

    if sorteio % 6 == 0:
        temp.sort()
        palpite.append(temp[:])
        temp.clear()
print()

print('=' * 30, f'{" SORTEANDO "}', '=' * 30)

# Fiz uma versão simples e deu certo, depois pedi pro chat me ajudar em uma versão melhor para melhor aparencia.
for i, j in enumerate(palpite):
    print(f'{i + 1:02}º jogo:', end=' ')
    print('  '.join(f'[{num:02}]' for num in j))  # um pouco avançado mas com treino da para pegar
    sleep(1)
print()

print('>' * 20, f'{" BOA SORTE!!! "}', '<' * 20)
