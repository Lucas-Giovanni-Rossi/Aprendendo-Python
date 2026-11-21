# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

todos = [[], []]

for n in range(1, 8):
    numero = int(input(f'Digite o {n}º número: '))
    if numero % 2 == 0:
        todos[0].append(numero)
    else:
        todos[1].append(numero)

todos[0].sort()
todos[1].sort()

print(f'\nPares: {todos[0]}')
print(f'Ímpares: {todos[1]}')
