# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

cont = 1
numeros = []

while True:
    numeros.append(int(input(f'Insira o {cont}º número: ')))

    proximo = '-'
    while proximo[0] not in 'NS':
        proximo = input('Deseja continuar? [S/N] ').strip().upper()

    if proximo[0] == 'N':
        break

    cont += 1

print('-=' * 30)

numeros.sort(reverse=True)
print(f'Você inseriu {cont} números no total.\nOrdenei em forma decrescente: {numeros}')

if 5 in numeros:
    print('Vocês inseriu o número 5 e ficou na posição: ', end='')
    for c, v in enumerate(numeros):
        if v == 5:
            print(c, end='')
else:
    print('O número 5 não foi informado para inserção.')
