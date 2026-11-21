# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
"""
A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""

total = mais1k = barato = qtd = 0
nomebarato = ''

print('~' * 50)
print('LOJAS ONLINES'.center(50))
print('~' * 50)

while True:
    qtd += 1
    print('=' * 10, f'Cadastre o {qtd}º produto', '=' * 10)
    nome = input('Nome do Produto: ').strip().capitalize()
    preco = float(input('Preço: R$'))
    total += preco

    if qtd == 1:
        barato = preco
        nomebarato = nome
    elif barato > preco:
        barato = preco
        nomebarato = nome

    if preco >= 1000:
        mais1k += 1

    continuar = '-'
    while continuar not in 'SN':
        continuar = input('Cadastrar proximo produto? [S/N] ').strip().upper()[0]

    print('-=' * 30)
    if continuar == 'N':
        break

print(f'\nCOMPRA FINALIZADA!\n\n{qtd} produtos cadastrados no total.')
print(
    f'Valor total gasto: R${total:.2f}\nProdutos que custam mais de R$1.000: {mais1k}\
      \nO produto mais barato cadastro: {nomebarato} com o valor de R${barato:.2f}'
)
