# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
"""
A) quantas pessoas tem mais de 17 anos.
B) quantos homens foram cadastrados e o nome e idade do mais velho
C) quantas mulheres tem menos de 21 anos."""

qtd = 1
mais18 = mulher20 = homemidadevelho = qtdhomem = 0
homemnomevelho = ''

while True:
    print('=' * 10, f'{qtd}º pessoa', '-' * 10)
    nome = input('NOME: ').strip().capitalize()
    idade = int(input('IDADE: '))

    # Validar Sexo
    while True:
        sexo = input('SEXO: [M/F] ').strip().upper()
        if sexo[0] == 'M':
            break
        elif sexo[0] == 'F':
            break

    # Conta quantos são maiores de idade
    if idade >= 18:
        mais18 += 1

    # Se feminino e se masculino
    if sexo == 'F' and idade <= 20:
        mulher20 += 1
    elif sexo == 'M':
        qtdhomem += 1
        if homemidadevelho < idade:
            homemnomevelho = nome
            homemidadevelho = idade

    # Se quer continuar
    while True:
        continuar = input('Quer continuar? [S/N] ').strip().upper()
        if continuar[0] == 'N':
            break
        elif continuar[0] == 'S':
            qtd += 1
            break

    print('-=' * 30)

    if continuar[0] == 'N':
        break


print(
    '\n'
    f'Foi registrado o cadastro de {qtd} de pessoas no sistema.\n'
    f'{mais18} pessoas são maiores de idade.\n'
    f'{qtdhomem} homens dentre eles {homemnomevelho} é o mais velho com {homemidadevelho} anos de idade.\n'
    f'E {mulher20} mulheres com menos de 20 anos de idade.'
)
