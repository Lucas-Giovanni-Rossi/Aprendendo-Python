# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nascimento = int(input('Qual seu ano de nascimento: '))

alistamento = nascimento + 18
atual = date.today().year
tempo = abs(atual - alistamento)

if alistamento < atual:
    print(
        'Você deveria ter se alistado em {} que ocorreu há {} anos atras.\n'
        'Caso não tenha se alistado procure porgão reponsável IMEDIATAMENTE'.format(
            alistamento, tempo
        )
    )
elif alistamento > atual:
    print('Seu alistamento ocorrerá daqui a {} anos'.format(tempo))
else:
    print('Quem nasceu em {} deve se alistar esse ano ({})'.format(nascimento, atual))
