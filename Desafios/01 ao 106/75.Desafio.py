# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
"""
A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares."""

n = tuple(int(input('Digite um número: ')) for _ in range(4))


print(f'Voce digitou: {n}')
print(f'Numero 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O número 3 apareceu na posição {n.index(3) + 1}º')
else:
    print('O número 3 não apareceu em nenhuma posição')

par = ()
for num in n:
    if num % 2 == 0:
        par += (num,)
print(f'Foram digitados os número pares: {par}')
