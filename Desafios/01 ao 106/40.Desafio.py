# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Incrementei ponderancia nas notas pesando na minnha faculdade

corte = 7

print(
    'Vamos calcular a média das suas notas?\n'
    'Lembrando que a nota de corte é\033[1;31m {}\033[m.\n'
    '[A1 possui um peso de 30%]\n'
    '[A2 possui um peso de 30%]\n'
    '[A3 possui um peso de 40%]\n'.format(corte)
)
print('-=-' * 10, 'BOA SORTE!!!', '-=-' * 10)

a1 = float(input('Qual a nota da sua A1? ')) * 0.3
a2 = float(input('Qual a nota da sua A2? ')) * 0.3
a3 = float(input('Qual a nota da sua A3? ')) * 0.4

media = sum([a1, a2, a3])

if media < corte - 2:
    print('O aluno \033[1;31mREPROVOU\033[m')
elif media < corte:
    print(
        '\nO aluno ficou de \033[1;33mRecuperação\033[m. \n'
        'Vamos trabalhar em um plano de melhoria!!'
    )
elif corte + 0.5 > media >= corte:
    print('\n\033[1;33mO aluno passou por pouco!!!\033[m')
else:
    print('\nParabéns!!! Você foi \033[1;32mAPROVADO\033[m.')

print('Sua nota final é: {:.2f} pontos do total de 10 pontos.'.format(media))
print(input('Aperte enter para finalizar'))
