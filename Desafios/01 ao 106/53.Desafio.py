# Crie um programa que diga se a frase é um palindromo

f = input('Informe a frase: ').split()  # tirar o todos os espaços dividindo

frase1 = ''.join(f).upper()  # juntas os caracteres e colocar em maisculo
caracteres = len(frase1) - 1
frase2 = ''

for p in range(caracteres, -1, -1):
    frase2 += frase1[p]

print('\nO inverso da frase citada é : {}'.format(frase2))

if frase1 == frase2:
    print('ESTA FRASE É UM PALÍNDROMO!!')
else:
    print('Esta frase NÃO é um palindromo.')


frase2 = frase1[::-1]
print('\nTeste bonus (Fatiamento em vez do for): ', frase2)  # fatiamente
