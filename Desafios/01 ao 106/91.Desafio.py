# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from operator import itemgetter
from random import randint
from time import sleep

ranking = []
temp = {}

for d in range(1, 5):
    sorte = randint(1, 6)
    print(f'O {d}º jogador tirou: {sorte}')
    temp['jogador'] = f'Jogador {d}'
    temp['dado'] = sorte
    ranking.append(temp.copy())
    temp.clear()
    sleep(1)

print('-=' * 15)
print(f'{"RANKING DE JOGADORES":^30}')
print('-=' * 15)

ranking = sorted(ranking, key=itemgetter('dado'), reverse=True)  # Entra conceito de chaves e novo modulo

cont = 1
for k in ranking:
    print(f'{cont}º lugar: {k["jogador"]} com {k["dado"]} pontos.')
    cont += 1
    sleep(1)
