# Cores no Terminal

# ANSI \o33[m

from time import sleep

print('\033[1;31;41mTeste\033[m')
print('\033[0:33;44mTeste\033[m')


a = 3
b = 5

print('Os valores são \033[1;30;41m{}\033[m e \033[1;30;42m{}\033[m '.format(a,b))


sleep(5)
#achei horrivel, vou esperar aprender import colorama ou sla oq