# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
partidas = []

jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
qtd = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for g in range(1, qtd + 1):
    partidas.append(int(input(f' - Quantos gols na {g}º partida. ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)

# Mostrar dicionario
print(jogador)
print('-=' * 30)

# Mostrar com for cada keys
for k, v in jogador.items():
    print(f'O campo {k} tem o valor de {v}.')
print('-=' * 30)

# Mostrar com mais detalhes cada gols
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for i, v in enumerate(jogador['gols'], start=1):
    print(f'=> Na partida {i}, fez {v} gols.')

# Mostra o total de gols
print(f'=> Foi um total de {jogador["total"]} gols.')
