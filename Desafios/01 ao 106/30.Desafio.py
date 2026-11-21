# Diga se é impar ou par

n = int(input('Digite um numero inteiro qualquer: '))

if n % 2 == 1:
    print('O número {} é ÍMPAR.'.format(n))
else:
    print('O número {} é PAR.'.format(n))