# ler numero entra 0 e 9999 e mostre unidades ](forma matematica)

nint = int(input('Digite um número inteiro de 0 a 9999: '))

u = nint % 10
d = nint // 10 % 10 # divido inteiro por 10 - depois pega o resultado e faz o modulo de 10, dai tem a medida.
c = nint // 100 % 10 # mesma logica
m = nint // 1000 % 10 # mesma logica

print('Analisando o número : ',nint)
print('\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar {}'.format(u,d,c,m))