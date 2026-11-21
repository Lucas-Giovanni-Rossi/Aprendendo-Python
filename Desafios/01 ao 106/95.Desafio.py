# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

clube = []  # Dicionario do time final
jogador = {}  # jogador temporario
partidas = []  # Gols marcodos por partida temporario

# Loop para cadastro de jogadores
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    qtd = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for g in range(1, qtd + 1):
        partidas.append(int(input(f' - Quantos gols na {g}º partida. ')))

    jogador['gols'] = partidas[:]  # Copia da lista para não fazer ligação
    jogador['total'] = sum(partidas)

    clube.append(jogador.copy())  # Adiciona todas informações a lista do clube em forma de copia

    # Limpa list() e dict() temporarios para o proximo jogador
    jogador.clear()
    partidas.clear()

    # Loop se continua cadastro ou não.
    print('~' * 35)
    prox = '-'
    while prox[0] not in 'SN':
        prox = str(input('Quer continuar? [S/N] ')).strip().upper()
    print('~' * 35)

    if prox[0] == 'N':
        break

# Tabela do time
print()
print(f'{"COD":<4}{"JOGADOR":^12}{"GOLS":^20}{"TOTAL":>6}')
print('-' * 44)

# Loop para tabela
for i, v in enumerate(clube):
    gols = ', '.join(map(str, v['gols']))  # formata a lista dentro da chave dentro da lista
    print(f'{i + 1:<4}{v["nome"]:^12}{gols:^20}{v["total"]:>6}')

soma = sum(v['total'] for v in clube)
print(f'=> O time fez {soma} gols no total <=')
print('~' * 44)
print()

# Loop para detalhemento dos jogadores buscando na lista principal com os dict()
while True:
    cod = int(input('Digite o COD. para mais informações ou "000" para encerrar: '))
    print()
    if cod == 0:
        break
    elif cod > len(clube):
        print('Codigo INVALIDO!')
    else:
        cod -= 1
        print(f'Nome do jogador: {clube[cod]["nome"]}')
        print(f'Total de gols: {clube[cod]["total"]}')
        print('Detalhamento por partida: ')
        print('-' * 30)
        for i, v in enumerate(clube[cod]['gols'], start=1):
            print(f'=> Na partida {i}, fez {v} gols.')
    print('~=' * 30)

print('*** PROGRAMA ENCERRADO ***')
