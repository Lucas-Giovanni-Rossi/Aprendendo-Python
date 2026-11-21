# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Digite um sexo [M/F]: ').strip().upper()[0]

while sexo not in ('MF'):  # enquanto o 'sexo' não for M ou F
    sexo = input('\nDado é INVALIDO.\nDigite novamente seu sexo: ').strip().upper()[0]

if sexo == 'M':
    sexo = 'masculino'
else:
    sexo = 'feminino'

print('\nDado {} registrado com sucesso.'.format(sexo))
