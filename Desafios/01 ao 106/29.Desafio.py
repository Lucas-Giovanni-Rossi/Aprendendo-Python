#Calular multa de transito

n = int(input('Quantos km o motorista estava percorrendo? '))
m = n-80
p = m*7

if n <= 80:
    print('\nO motorista estava dentro do limite de velocidade.\n'
          'A multa não se aplica. Tenha um ótimo dia!')
else:
    print('\nO motorista esta acima do limite de 80Km por hora.\n' \
    'Ele deverá pagar R${:.2f} de multa pois ultrapassou {}Km do limite'.format(p,m))

print('\n Não se esqueça! Se beber não dirija!')