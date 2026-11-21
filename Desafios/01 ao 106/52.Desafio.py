# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número  para saber se ele é primo: '))

print()

contador = 0
for primo in range(1, numero + 1):
    if numero % primo == 0:
        print('\033[34m', end=' ')
        contador += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(primo), end=' ')

print('\n')
print(
    '\033[mO número {} é divisivel por {} número(s) incluindo ele mesmo, portanto:\n'.format(
        numero, contador
    )
)

if contador == 2:
    print('-=' * 10, ' O número {} é PRIMO!'.format(numero), '-=' * 10, '\n')
else:
    print('-=' * 10, ' O número {} NÃO é primo.'.format(numero), '-=' * 10, '\n')
