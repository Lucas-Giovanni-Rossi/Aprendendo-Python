# leia o valor em metros e exiba convertido em cen´timetros e milimetros

n = float(input('Digite um número em metros: '))

c = n * 100
mm = c * 100

print('Se o metro é igual a: {}\n' \
'Equivale a {} centímetros e {} milímetros'.format(n,c,mm))