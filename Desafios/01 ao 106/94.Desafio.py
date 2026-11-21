#  Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

galera = []
pessoa = {}
velhos = []
qtd = int(input('Quantas pessoas deseja cadastrar? '))

# Loop para escolhar quantas pessoas cadastras no dicionario e se deseja continuar ou nõa.
cont = 0
while True:
    while cont < qtd:
        cont += 1
        print('-=' * 10, f'{cont}º pessoa', '-=' * 10)
        pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
        while pessoa['sexo'] not in 'MF':
            pessoa['sexo'] = str(input('Sexo invalido !: [M ou F] ')).strip().upper()[0]
        pessoa['idade'] = int(input('Idade: '))
        galera.append(pessoa.copy())
        pessoa.clear()

    print('~' * 50)
    prox = '-'
    while prox[0] not in 'SN':
        prox = str(input('Quer cadastrar mais pessoas? ')).strip().upper()[0]
        if prox[0] == 'S':
            qtd += int(input('Quantas pessoas deseja acrescentar? '))

    if prox[0] == 'N':
        break
print('-=' * 30)

# Ler qtd de pessoas sem usar o qtd informado no inicio
print(f' - Foram cadastradas {len(galera)} pessoas.')

# Ler so as idades a partir da lista completa
idade = [p['idade'] for p in galera]
print(f' - A média de idade é igual a: {sum(idade) / len(idade):.2f}')

# Guardar o nome so das mulheres a partir da lista completa
mulheres = [p['nome'] for p in galera if p['sexo'] == 'F']
print(f' - Lista de mulheres: {"; ".join(mulheres)}.')

# Guardar o nome das idades acima da média a partir da lista completa
velhos = [v['nome'] for v in galera if v['idade'] > sum(idade) / len(idade)]
print(f' - Litas de idades acima da média: {"; ".join(velhos)}.')
