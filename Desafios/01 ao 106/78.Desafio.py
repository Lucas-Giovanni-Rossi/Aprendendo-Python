# Ler 5 número e guarde em uma linsta
# Depois mostre o maior e o menor

numeros = []

for c in range(1, 6):
    numeros.append(int(input(f'Digite o {c}º número: ')))

print('-=' * 30)
print('Lista: ', numeros)
print(f'O maior numero é: {max(numeros)} na posição {numeros.index(max(numeros))}.\nO menor número é: {min(numeros)} na posição {numeros.index(min(numeros))}.')
print('-=' * 30)

# ============================================================================================================================
print('Segundo jeito: ')  # Caso tenha mais de uma posição

maior = max(numeros)
menor = min(numeros)

pos_maior = [identificar for identificar, valor in enumerate(numeros) if valor == maior]
pos_menor = [indice for indice, valor in enumerate(numeros) if valor == menor]

print(f'O maior numero é: {max(numeros)} nas posições: {pos_maior}.\nO menor número é: {min(numeros)} nas posições: {pos_menor}.')
print('-=' * 30)

print('OBS: As posições estão em metodo pyhton, ou seja começa no 0')
