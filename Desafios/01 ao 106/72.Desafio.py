# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = (
    'zero',
    'um',
    'dois',
    'três',
    'quatro',
    'cinco',
    'seis',
    'sete',
    'oito',
    'nove',
    'dez',
    'onze',
    'doze',
    'treze',
    'catorze',
    'quinze',
    'dezesseis',
    'dezessete',
    'dezoito',
    'dezenove',
    'vinte',
)

while True:
    n1 = int(input('Digite um número de 0 a 20: '))

    while n1 < 0 or n1 > 20:
        n1 = int(input('Tente novamente. Digite entre 0 e 20: '))

    print(f'Você digitou o número {numeros[n1]}.')

    prox = '-'
    while prox not in 'SN':
        prox = input('Quer continuar? [S/N] ').strip().upper()[0]

    if prox == 'N':
        break
