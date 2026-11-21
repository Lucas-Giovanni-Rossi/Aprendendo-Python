#Aluguel de carros

d = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos km voce rodou? '))

p = (d*60) + (km*0.15)

print('O valor a pagar pelo aluguel é: R${:.2f}'.format(p))
