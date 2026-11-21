#Ler seno cosseno e tanjente a partir de um angulo
from math import radians,sin,cos,tan

angulo = float(input("Digite um ângulo para saber seno coseno e tanjente: "))

rad = radians(angulo)

seno = sin(rad)
cosseno = cos(rad)
tanjente = tan(rad)

print('O seno é igual a: {:.4f}\n' \
'O cosseno é igual a: {:.4f}\n' \
'A tajente é igual a: {:.4f}'.format(seno,cosseno,tanjente))