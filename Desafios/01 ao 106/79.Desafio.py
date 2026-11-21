# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

qtd = int(input('Quantos números deseja digitar? '))
cont = 0
numeros = []
while cont < qtd:
    cont += 1
    n = int(input(f'Qual o {cont}º número? '))
    numeros.append(n)

numeros_unicos = sorted(set(numeros))
print('-=' * 30)
print(f'Você inseriu os números do menor ao maior: {numeros_unicos}.\n*Retirando números repetidos')
