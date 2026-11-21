# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número inteiro: '))

escolha = int(
    input(
        """
Agora escolha como deseja que esse número seja convertido :
    Digite "1" para BINÁRIO.
    Digite "2" para OCTAL.
    Digite "3" para HEXADECIMAL.
    
Qual a opção escolhida? """
    )
)

if escolha == 1:
    print('\nO número {} em valor binário é igual a: {}'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('\nO número {} em valor binário é igual a: {}'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('\nO número {} em valor binário é igual a: {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida, tente novamente.')
