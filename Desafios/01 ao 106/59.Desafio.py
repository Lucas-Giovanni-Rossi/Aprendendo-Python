# Crie um programa que leia dois valores e mostre um menu na tela:
from time import sleep

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

indice = False
reinicia = False

while not indice:
    if reinicia:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
        reinicia = False

    print("""   
    [1] Somar 
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair
    """)
    menu = int(input('>>>> Digite uma opção do Menu:'))

    if menu == 1:
        soma = n1 + n2
        print('\nA soma de {} + {} é igual a: {}.'.format(n1, n2, soma))
    elif menu == 2:
        mult = n1 * n2
        print('\nA multiplicação de {} * {} é igual a: {}.'.format(n1, n2, mult))
    elif menu == 3:
        if n1 > n2:
            print('\nEntre {} e {} o maior é: {}'.format(n1, n2, n1))
        elif n1 < n2:
            print('\nEntre {} e {} o maior é: {}'.format(n1, n2, n2))
        else:
            print('\nOs dois números são iguais!')
    elif menu == 4:
        reinicia = True  # reiniciar ciclo
    elif menu == 5:
        indice = True
        print('\nEncerrando....')
    else:
        menu = int(input('Opção invalida! Digite novamente:'))

    print('-=' * 20)
    sleep(2)

print('Fim! Volte sempre!.')
