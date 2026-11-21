# Conflito de reuniões e salas minimas
from rich import print


def min_reunioes(reunioes):
    try:
        inicio = sorted([horario[0] for horario in reunioes])
        fim = sorted([horario[1] for horario in reunioes])
    except Exception:
        return print('[red]Reunião aberta, confirme horário de entrada/saída e tente novamente.[/]')

    salas_atuais = 0
    max_salas = 0
    contar_inicio = contar_fim = 0

    while contar_inicio < len(reunioes):
        if inicio[contar_inicio] < fim[contar_fim] + 0.07:
            salas_atuais += 1
            max_salas = max(max_salas, salas_atuais)
            contar_inicio += 1
        else:
            salas_atuais -= 1
            contar_fim += 1

    if max_salas == 0:
        max_salas = 'nenhuma'

    return print(f'Será necessário [green]{max_salas}[/] sala(s).')


agenda = [(15.5, 16.3), (17, 18), (10, 15.5)]
agenda2 = [(8, 9), (9, 10), (10, 11), (11, 12)]
agenda3 = [10]
agenda4 = [(10, 15), (11, 14), (12, 16), (13, 17)]
agenda5 = [(9, 10.5), (10, 11), (10.5, 11.9), (11.5, 13), (12, 14)]
agenda6 = []
agenda7 = [(10, 12), (10, 11), (10, 13)]
agenda8 = [(10, 11), (12, 13)]
agenda9 = [(8, 12), (9, 12), (10, 12)]

min_reunioes(agenda)
min_reunioes(agenda2)
min_reunioes(agenda3)
min_reunioes(agenda4)
min_reunioes(agenda5)
min_reunioes(agenda6)
min_reunioes(agenda7)
min_reunioes(agenda8)
min_reunioes(agenda9)
