# Mostrar se é ano bissexto

from datetime import date

ano = int(input('Qual ano você quer analisar?\n'
'(Coloque "0" se quiser analisar ano atual): '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO!'.format(ano))
else:
    print('O ano de {} NÃO é BISSEXTO.'.format(ano))