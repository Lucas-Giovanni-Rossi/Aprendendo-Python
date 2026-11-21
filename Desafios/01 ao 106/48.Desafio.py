# Programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print(
    'Esse programa mostra todos os números ímpares múltiplos de três e a sua soma dentro de um intervalo.'
)

i = int(input('Inicio do intervalo: '))
f = int(input('Fim do intervalo: '))

contador = 0
soma = 0

print('')
for div3 in range(i, f + 1):
    if div3 % 3 == 0 and div3 % 2 == 1:
        print(div3, end=' ')
        contador += 1
        soma += div3
print(
    '\n\nExistem {} números ímpares múltiplos de três dentro do intervalo acima e sua soma é igual a {}.'.format(
        contador, soma
    )
)
print('\nFim!')
