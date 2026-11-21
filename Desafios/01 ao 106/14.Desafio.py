#Conversor de temperatura

C = float(input('Qual a temperatura em ºc: '))

F = ( ( 9 * C ) / 5 ) + 32

print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF!'.format(C,F))