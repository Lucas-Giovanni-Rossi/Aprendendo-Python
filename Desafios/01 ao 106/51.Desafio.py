# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('=-' * 10, ' Este programa lê os 10 primeiros termos de uma PA ', '=-' * 10)

termo = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))

contador = 0
print()
for pa in range(termo, termo + razao * 10, razao):
    print(pa, end=' → ')
    contador += 1
    if contador == 10:
        print('ACABOU')

print('\nEsses são os {} primeiros termos encontrados. '.format(contador))
