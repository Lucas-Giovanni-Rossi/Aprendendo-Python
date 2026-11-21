# Estrutura de repetição com while ( quando não sei limite do loop)

n = 1
par = 0
impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('Foram digitados {} pares e {} ímpares.'.format(par, impar))
print('Fim')
