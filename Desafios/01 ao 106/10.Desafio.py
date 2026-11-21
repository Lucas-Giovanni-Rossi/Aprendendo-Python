#Converter em dolar com uma cotação fixa

print('Olá, tudo bem?')

n = float(input('Quantos reais você tem na carteira hoje?'))

d = n/3.27

print('Com a cotação do dolar em\n' \
'US$1.00 = R$3.27\n' \
'Você poderia comprar US${:.2f}.'.format(d))