# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual é o valor da casa dos seus sonhos? R$'))
sal = float(input('Qual é a sua renda mensal? R$'))
anos = int(input('Quantos anos será o financimento? '))

parcela = casa/(anos*12)
limite = sal * 0.30

if parcela > limite:
    print(
        '\nInfelizmente não será possivel financiar a casa.\n' \
        'Você teria {} parcelas a pagar.\n' \
        'Com o valor maximo R${:.2f}, o que infelizmente é maior que 30% ' 'da renda mensal.\n'.format(anos*12,parcela))
else:
    print(
        '\nParabéns! Podemos seguir com o financimento.\n' \
        'Você terá {} parcelas a pagar.\n' \
        'Com o valor de R${:.2f}.\n'.format(anos*12,parcela))

print('Tenha um bom dia!')
