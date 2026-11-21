# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[], [], []]
for n in range(1, 4):
    matriz[0].append(int(input(f'Digite a posição {n},0,0: ')))
    matriz[1].append(int(input(f'Digite a posição 0,{n},0: ')))
    matriz[2].append(int(input(f'Digite a posição 0,0,{n}: ')))
print('-=' * 30)

cont = 0
for item in matriz:
    print(f' ({matriz[0][cont]:^5})({matriz[1][cont]:^5})({matriz[2][cont]:^5})')
    cont += 1

pares = 0
for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            pares += valor
print(f'\nA soma de todos valores pares digitados é igual a: {pares}.')

soma = sum(matriz[2])
print(f'A soma da terceira coluna é igual a: {soma}.')

maior = []
for linha in matriz:
    maior.append(linha[1])
maior.sort(reverse=True)
print(f'O maior valor na segunda linha é igual a: {maior[0]}.')
