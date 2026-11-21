# Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

todos = []
cont = 0

# 🔹 Loop de cadastro
while True:
    cont += 1
    print('-=' * 10, f'{cont}º pessoa', '-=' * 10)

    nome = str(input('Nome: ')).strip().capitalize()
    peso = float(input('Peso: '))
    todos.append([nome, peso])  # Criando listas dentro de um lista

    prox = '-'
    while prox[0] not in 'SN':
        prox = input('Quer continuar? [S/N] ').strip().upper()

    if prox[0] == 'N':
        break

print('-=-' * 30)
print(f'{cont} pessoas foram cadastradas.\n')

# 🔹 Começa assumindo o primeiro nome como maior e menor
maior = todos[0][1]
menor = todos[0][1]

# 🔹 Descobrindo maior e menor
for p in todos:
    if p[1] > maior:
        maior = p[1]
    if p[1] < menor:
        menor = p[1]

# 🔹 Pegando os nomes
nomes_maior = [p[0] for p in todos if p[1] == maior]
nomes_menor = [p[0] for p in todos if p[1] == menor]

print(f'O maior peso foi de {maior}Kg. De: {nomes_maior}')
print(f'O menor peso foi de {menor}Kg. De: {nomes_menor}')
