#aumento de salario

s = float(input('Parabéns!!\n' \
'Você ganhou um aumento, digite a seguir seu salário atual para calcularmos: R$1'))

s1 = s+(s*0.15)

print('Seu novo salário a partir do próximo pagamento é :\n' \
'R${:.2f}'.format(s1))