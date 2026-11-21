# Iniciando Mundo 2
#Condições aninhadas

nome = input('Me diga seu nome: ').upper()

if nome == 'LUCAS':
    print('Que nome bonito!') 
elif nome == 'NICOLLAS' or nome == 'PEDRO' or nome == 'GUSTAVO': #nova função aprendida
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia {}!'.format(nome.capitalize()))