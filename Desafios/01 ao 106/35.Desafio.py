# Ultimo desafio do mundo 1
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário 
# se elas podem ou não formar um triângulo.

print('-=-' * 30)
print('Analisador de Triângulos')
print('-=-' * 30)

l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

lista = sorted([l1,l2,l3]) # ordena menor ao maior

if lista[2] >= lista[0] + lista[1]: # se o maior numero for igual ou maior que a soma dos outro 2
    print('Infelizmente não é possivel formar um triângulos com essas 3 retas')
else:
    print('É possivel formar um triângulo!')
