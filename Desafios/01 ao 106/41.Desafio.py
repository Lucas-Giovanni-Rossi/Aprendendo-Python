# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade:

from datetime import date

nascimento = int(input('Digite ano de nascimento: '))

idade = date.today().year - nascimento
lista = ['mirim', 'juvenil', 'junior', 'sênior', 'master']

if idade <= 9:
    categoria = lista[0]
elif idade <= 14:
    categoria = lista[1]
elif idade <= 17:
    categoria = lista[2]
elif idade <= 25:
    categoria = lista[3]
else:
    categoria = lista[4]

print(
    'Como a idade do atleta é {} anos, ele(a) entrará na categoria {}.'.format(
        idade, categoria.upper()
    )
)
