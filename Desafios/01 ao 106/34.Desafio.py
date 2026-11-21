# Escreva um programa que pergunte o salário de um funcionário e 
# calcule o valor do seu aumento. Para salários superiores a R$1250,00, 
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Parabéns!!! Você ganhou um aumento.\n' \
'Para calcular digite ao lado seu salário atual: R$'))

if sal > 1250:
    aumento = sal * 1.10
else:
    aumento = sal * 1.15 

print('Seu novo salario a partir do próximo mês é:\n R$',aumento)