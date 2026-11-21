# Calcular a passagem da viagem

km = float(input('Me diga quantos km irá viajar parar calcular a passagem: '))

if km > 200:
    passagem = 0.45
else:
    passagem = 0.50

print('\nSua viagem custará no valor de R${:.2f}.'.format(passagem*km))