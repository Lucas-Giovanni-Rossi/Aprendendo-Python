# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


# Era para ser exercio simples mas foi mais divertido que achei.
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    print('~' * 30)
    cont = f'Contando de {inicio} até {fim} de {passo * -1 if passo < 0 else passo} em {passo * -1 if passo < 0 else passo}.'
    print(cont)

    # Ajustar range de python
    if inicio < fim:
        fim += 1
    elif inicio > fim:
        fim -= 1

    for c in range(inicio, fim, passo):
        print(c, end=' → ', flush=True)
        sleep(0.45)  # tempo entre cada número

    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -1)

print('~' * 30)
print('Agora é a sua vez de contar!')
while True:
    i = int(input('Inicio: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))

    # Ajustando possivel engano do usuario
    if i > f and p > 0:
        p = -p
    contador(i, f, p)

    prox = '-'
    while prox[0] not in 'SN':
        prox = input('Quer contar novamente? [S/N] ').strip().upper()
        print('-=' * 15)

    if prox[0] == 'N':
        break

print('Fim do programa. Volte sempre!')
