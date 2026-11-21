# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(n, g):
    if n == '' or n.isnumeric():
        n = '<desconhecido>'

    if g.isnumeric():
        g = int(g)
    else:
        g = '<??>'

    print(f'O jogador {n} fez {g} gols no total.')


nome = input('Nome do jogador: ').strip().capitalize()
gols = input('Quantos gols marcados: ')

ficha(nome, gols)
