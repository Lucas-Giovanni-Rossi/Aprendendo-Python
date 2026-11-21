# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

print('Este program lê 6 número inteiros e mostra a soma apenas dos número pares.')

soma = 0
cont = 0

for n in range(1, 7):
    num = int(input('Digite o {}º número: '.format(n)))
    if num % 2 == 0:
        cont += 1
        soma += num
print(
    'Você informou {} número(s) pare(s) e a soma deles é igual a {}.'.format(cont, soma)
)
