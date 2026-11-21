# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#  No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['Nome'] = input('Nome do aluno: ').strip().capitalize()
aluno['Média'] = float(input(f'Média do {aluno["Nome"]}: '))

print('-=' * 30)

for k, v in aluno.items():
    print(f' - {k} é {v}')

if aluno['Media'] < 5:
    print(' - Reprovado.')
elif aluno['Média'] < 7:
    print(' - Recuperação.')
else:
    print(' - Aprovado. Parabéns!')
