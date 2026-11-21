#Aprendendo modulos

from math import sqrt # importação parcial

num = int(input('Digite um número inteiro: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {:.3f}'.format(num,raiz))

print('\n===========================================================================================\n')

import random
#random.random é por padrçao de 0 a 1 com float
#random.ranint é numero inteiro e ao lado coloca a margem
n1 = random.randint(1,100)
print('Número aleátorio de 1 a 100: ',n1)

print('\n===========================================================================================\n')

# Emoji manualmente inserido
print("Sorriso: 😊")
print("Coração: ❤️")
print("Joinha: 👍")
print("Sol: 🌞")