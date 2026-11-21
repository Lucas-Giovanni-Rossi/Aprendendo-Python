# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

numero = int(input('Quantas pessoas deseja informar o peso: '))

lista = []
for quant in range(1, numero + 1):
    peso = float(input('Qual peso a {}º pessoa? '.format(quant)))
    lista.append(peso)

lista.sort()
print('O menor peso neste grupo é {}Kg.'.format(lista[0]))
lista.sort(reverse=True)
print('E o maior peso no grupo é {}Kg'.format(lista[0]))
