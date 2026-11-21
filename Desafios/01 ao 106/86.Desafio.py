# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]

for n in range(1, 4):
    matriz[0].append(input(f'Digite a posição {n},0,0: '))
    matriz[1].append(input(f'Digite a posição 0,{n},0: '))
    matriz[2].append(input(f'Digite a posição 0,0,{n}: '))

print('-=' * 30)

cont = 0
for item in matriz:
    print(f' ({matriz[0][cont]})({matriz[1][cont]})({matriz[2][cont]})')
    cont += 1


# Esse deu trabalho para pensar
