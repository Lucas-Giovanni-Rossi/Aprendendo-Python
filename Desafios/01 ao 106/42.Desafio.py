# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

print('-=-' * 30)
print('Analisador de Triângulos')
print('-=-' * 30)

l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

lista = sorted([l1, l2, l3])  # ordena menor ao maior

if lista[2] >= lista[0] + lista[1]:
    print('Infelizmente não é possivel formar um triângulos com essas 3 retas')
else:
    print('É possivel formar um triângulo ', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO|')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
