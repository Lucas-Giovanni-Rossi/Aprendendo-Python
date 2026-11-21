# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:

"""IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida"""

print('-=-' * 30)
print('Analisador de Índice de Massa Corporal (IMC)')
print('-=-' * 30)

peso = float(input('Informe o peso em Kg: '))
altura = float(input('Infome a altura em metros: '))

imc = peso / altura**2

if imc < 18.5:
    print('O paciente está abaixo do peso.')
elif imc <= 25:
    print('O paciente está com o peso ideal. Parabéns!')
elif imc <= 30:
    print('O paciente está em sobrepeso.')
elif imc <= 40:
    print('O paciente está com obesidade.')
else:
    print('O paciente está em Obesidade Mórbita!!!')
print('O IMC do paciente atualmente é: {:.2f}'.format(imc))
