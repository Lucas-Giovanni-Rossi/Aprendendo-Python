# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

inteiros = []
par = []
impar = []
cont = 0

while True:
    cont += 1
    n = int(input(f'Digite o {cont}º número: '))
    inteiros.append(n)

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    prox = '-'
    while prox[0] not in 'SN':
        prox = input('Quer continuar? [S/N] ').strip().upper()

    if prox == 'N':
        break
print('-=' * 30)

inteiros.sort()
par.sort()
impar.sort()

print(f'Você digitou {cont} números : {inteiros}\nNúmeros pares: {par}\nNúmeros ímpares: {impar}\n')
