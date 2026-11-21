# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# Tabuada a partir de um número

numero = int(input('Informe um número para verificar a sua tabuada: '))

print('\n')
for tabuada in range(0, 11):
    print('{} x {:2} = {}'.format(numero, tabuada, numero * tabuada))

print('\nBONS ESTUDOS!')
