# Program que le um intervalo de tempo e mostra todos os números pares

print('Esse programa mostra todo números pares de um intervalo.')

i = int(input('Inicio: '))
f = int(input('Fim: '))

for par in range(i, f + 1):
    if par % 2 == 0:
        print(par, end=' ')
print('\nFim!')
