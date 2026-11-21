# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

lista = (
    'python',
    'programacao',
    'algoritmo',
    'computador',
    'teclado',
    'monitor',
    'internet',
    'software',
    'hardware',
    'dados',
    'variavel',
    'funcao',
    'lista',
    'tupla',
    'dicionario',
    'loop',
    'condicao',
    'sistema',
    'codigo',
    'debug',
)

vogais = 'aeiou'

for palavra in lista:
    print(f'\nNa palavra *{palavra.upper()}* temos as vogais: ', end='')

    for letra in palavra:
        if letra in vogais:
            print(letra.upper(), end=' ')
