# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
#  qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

numero = int(input('Quantas pessoas deseja informar o peso: '))

idademedia = 0
idadehomem = 0
nomehomem = ''
contmulher = 0

# Repetição de input par ao usuario
for pessoa in range(1, numero + 1):
    print('-=' * 10, '{}º PESSOA'.format(pessoa), '-=' * 10)
    nome = input('Nome: ').strip().capitalize()
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip().upper()

    # Idade total do grupo para saber média depois
    idademedia += idade

    # Contador de quantas mulheres tem menos de 20 anos
    if sexo == 'F' and idade < 20:
        contmulher += 1

    # Saber o nome e idade do homem mais velho
    if sexo == 'M' and idade > idadehomem:
        idadehomem = idade
        nomehomem = nome

print('A idade média do grupo é igual a: {:.2f} anos.'.format(idademedia / numero))
print('Existe {} mulhere(s) com menos de 20 anos neste grupo.'.format(contmulher))
print('O homem mais velho tem {} e se chama {}.'.format(idadehomem, nomehomem))
