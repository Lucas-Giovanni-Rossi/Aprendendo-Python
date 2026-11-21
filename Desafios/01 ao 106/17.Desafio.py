# Ler os catetos e calcule a hipotenusa
from math import hypot

c1 = float(input('Qual é o 1º cateto? '))
c2 = float(input('Qual é o 2º cateto do triângulo? '))

h = hypot(c1,c2) # import que cacula hipotenusa

print('Então a hipotenusa do triângulo retângulo é igual a: ',h)