#  Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def área(larg, comp):
    t = larg * comp
    print(f'A área de um terrono {larg} x {comp} é de {t}m².')


print(f'{"CONTROLE DE TERRENOS":^40}')
print('~' * 50)

L = int(input('Largura (m): '))
C = int(input('Comprimento (m): '))
área(L, C)
