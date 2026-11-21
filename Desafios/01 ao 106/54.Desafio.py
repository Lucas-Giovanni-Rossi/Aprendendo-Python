# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.7

from datetime import date

numero = int(input('Quantas pessoas deseja informar a data de nacimento: '))

maior = 0
menor = 0
ano = date.today().year

print()
for pessoas in range(1, numero + 1):
    idade = int(input('Qual o ano de nascimento da {}º pessoa?'.format(pessoas)))
    if idade + 18 >= ano:
        menor += 1
    else:
        maior += 1

print(
    '\nDas {} pessoas informadas, {} são maiores de idade e {} são menores de idade no ano de {}'.format(
        numero, maior, menor, ano
    )
)
