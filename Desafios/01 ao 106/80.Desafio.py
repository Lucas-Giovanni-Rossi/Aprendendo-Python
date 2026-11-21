# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

numeros = []

for pos in range(0, 5):
    n = int(input(f'Insera o {pos + 1}º valor: '))
    if pos == 0:
        numeros.append(n)
        print('1º item da lista')
    elif n > max(numeros):
        numeros.append(n)
        print('Número adicionado a última posição...')
    elif n < min(numeros):
        numeros.insert(0, n)
        print('Número adicionado a posição 0')
    else:
        desc = 0
        while True:
            if n <= numeros[desc]:
                numeros.insert(desc, n)
                print(f'Número inserido na posição {desc}')
                break
            desc += 1

print(numeros)
